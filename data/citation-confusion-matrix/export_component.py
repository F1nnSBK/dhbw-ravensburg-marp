#!/usr/bin/env python3
"""Export an interactive, static HTML confusion matrix for a Marp iframe."""

from __future__ import annotations

import argparse
import csv
import html
import json
from collections import Counter
from pathlib import Path


GROUPS = {
    (False, False): ("TN", "Kein Problem vorhanden und keines gemeldet"),
    (False, True): ("FP", "Fälschlich als Problem gemeldet"),
    (True, False): ("FN", "Vorhandenes Problem nicht erkannt"),
    (True, True): ("TP", "Problem vorhanden und erkannt"),
}


def parse_bool(value: str | None, field: str, line_number: int) -> bool:
    if value is None:
        raise ValueError(f"CSV-Zeile {line_number}: Feld {field!r} fehlt.")
    normalized = value.strip().lower()
    if normalized not in {"true", "false"}:
        raise ValueError(
            f"CSV-Zeile {line_number}: {field!r} erwartet true/false, erhalten: {value!r}."
        )
    return normalized == "true"


def summarize_attempts(path: Path) -> tuple[dict, str | None, int]:
    cells = {
        group: {
            "count": 0,
            "statuses": Counter(),
            "errors": Counter(),
            "examples": [],
            "with_errors": 0,
            "without_errors": 0,
            "invalid_json": 0,
            "invalid_errors": 0,
        }
        for group, (name, _) in GROUPS.items()
    }
    evaluation_ids: set[str] = set()
    row_count = 0

    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        required = {
            "evaluation_id",
            "case_id",
            "expected_problem",
            "predicted_problem",
            "answer_json",
            "actual_status",
        }
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV-Spalten fehlen: {', '.join(sorted(missing))}")

        for line_number, row in enumerate(reader, start=2):
            row_count += 1
            evaluation_ids.add(row["evaluation_id"])
            expected = parse_bool(row["expected_problem"], "expected_problem", line_number)
            predicted = parse_bool(row["predicted_problem"], "predicted_problem", line_number)
            group = GROUPS[(expected, predicted)][0]
            cell = cells[(expected, predicted)]
            cell["count"] += 1

            try:
                answer = json.loads(row["answer_json"]) if row["answer_json"] else None
            except json.JSONDecodeError:
                answer = None
            if not isinstance(answer, dict):
                cell["invalid_json"] += 1
                continue

            status = answer.get("status", row.get("actual_status"))
            cell["statuses"][str(status) if status not in (None, "") else "Fehlend"] += 1

            errors = answer.get("errors")
            if not isinstance(errors, list):
                cell["invalid_errors"] += 1
                continue

            messages = [
                message
                if isinstance(message, str)
                else json.dumps(message, ensure_ascii=False, sort_keys=True)
                for message in errors
            ]
            if messages:
                cell["with_errors"] += 1
            else:
                cell["without_errors"] += 1
            cell["errors"].update(messages)
            if len(cell["examples"]) < 3:
                cell["examples"].append((row.get("case_id", ""), messages[:2]))

    if row_count == 0:
        raise ValueError(f"Keine Versuche in {path}.")
    if len(evaluation_ids) != 1:
        raise ValueError(f"Erwartet wurde genau eine Evaluation, gefunden: {evaluation_ids}.")
    return cells, next(iter(evaluation_ids)), row_count


def tooltip_html(group_key: tuple[bool, bool], cell: dict, row_total: int) -> str:
    group, description = GROUPS[group_key]
    count = cell["count"]
    row_percent = 100 * count / row_total if row_total else 0
    status_text = ", ".join(
        f"{html.escape(status)}: {amount:,}"
        for status, amount in sorted(cell["statuses"].items())
    ) or "keine"
    error_items = "".join(
        f"<li>{html.escape(message)} <strong>({amount:,}×)</strong></li>"
        for message, amount in cell["errors"].most_common(5)
    ) or "<li>Keine Fehlereinträge</li>"
    examples = "".join(
        "<li>"
        f"<strong>{html.escape(case_id)}</strong>: "
        f"{html.escape('; '.join(messages) if messages else 'keine Fehlereinträge')}"
        "</li>"
        for case_id, messages in cell["examples"]
    ) or "<li>Keine gültigen Antworten mit Fehlerliste</li>"

    return (
        f"<strong>{group}: {html.escape(description)}</strong><br>"
        f"Fälle: {count:,}, Anteil der Referenzklasse: {row_percent:.1f}%<br>"
        f"Ausgabestatus aus answer_json: {status_text}<br>"
        f"Fälle mit / ohne Fehlereinträge: {cell['with_errors']:,} / "
        f"{cell['without_errors']:,}<br>"
        f"Ungültiges / fehlendes Antwort-JSON: {cell['invalid_json']:,}; "
        f"ungültige / fehlende Fehlerliste: {cell['invalid_errors']:,}<br>"
        "<strong>Häufigste exakte Fehlereinträge (max. 5):</strong>"
        f"<ul>{error_items}</ul>"
        f"<strong>Fallbeispiele (max. 3):</strong><ul>{examples}</ul>"
        "<small>Fehlertexte sind Modellausgaben, keine referenzierten Gold-Kategorien.</small>"
    )


def matrix_html(cells: dict, normalized: bool) -> str:
    labels = ["Kein Problem", "Problem"]
    order = [
        [(False, False), (False, True)],
        [(True, False), (True, True)],
    ]
    row_totals = [
        sum(cells[group]["count"] for group in row)
        for row in order
    ]
    max_count = max(cell["count"] for cell in cells.values())
    output = [
        '<section class="cm-matrix">',
        f"<h2>{'Anteil je Referenzklasse' if normalized else 'Anzahl'}</h2>",
        '<p class="cm-axis-title">Vorhersage</p>',
        '<div class="cm-grid">',
        '<span class="cm-corner">Referenz ↓</span>',
        *(f"<span>{label}</span>" for label in labels),
    ]

    for row_index, row in enumerate(order):
        output.append(f"<span>{labels[row_index]}</span>")
        for group_key in row:
            cell = cells[group_key]
            group = GROUPS[group_key][0]
            count = cell["count"]
            fraction = count / row_totals[row_index] if row_totals[row_index] else 0
            value = (
                f"{fraction:.1%}"
                if normalized and row_totals[row_index]
                else ("–" if normalized else f"{count:,}")
            )
            scale = fraction if normalized else count / max(max_count, 1)
            shade = round(246 - 130 * scale)
            details = tooltip_html(group_key, cell, row_totals[row_index])
            aria_label = (
                f"{group}, Referenz {labels[row_index]}, Vorhersage "
                f"{labels[int(group_key[1])]}: {value}; Details bei Fokus"
            )
            output.append(
                f'<div class="cm-cell" tabindex="0" role="group" '
                f'aria-label="{html.escape(aria_label, quote=True)}" '
                f'style="--cell-shade: {shade}">'
                f"<span>{group}<br><strong>{value}</strong></span>"
                f'<div class="cm-tooltip">{details}</div></div>'
            )
    output.append("</div></section>")
    return "".join(output)


def render_document(cells: dict, evaluation_id: str | None, row_count: int) -> str:
    matrix = (
        '<div class="cm-layout">'
        + matrix_html(cells, normalized=False)
        + matrix_html(cells, normalized=True)
        + "</div>"
    )
    evaluation = (
        f'<p class="cm-meta">Evaluation <code>{html.escape(evaluation_id)}</code>'
        f", {row_count:,} Versuche</p>"
        if evaluation_id
        else ""
    )
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Konfusionsmatrix, Run 1</title>
  <link rel="stylesheet" href="confusion-matrix.css">
</head>
<body>
  <main class="cm-component">
    <h1>Fehlererkennung, Run 1</h1>
    {evaluation}
    <p class="cm-intro">Mauszeiger über eine Zelle bewegen oder die Zelle per
    Tabulatortaste fokussieren, um Status, häufige Modell-Fehlereinträge und
    Beispiele zu sehen.</p>
    {matrix}
    <p class="cm-note"><strong>Referenz:</strong> Die Gold-Labels enthalten nur
    die binäre Klasse „Problem / kein Problem“, keine konkreten Fehlertypen.
    Angezeigte Fehlertexte stammen aus den Modellantworten in
    <code>answer_json</code>.</p>
  </main>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempts", type=Path, required=True, help="Pfad zur attempts.csv")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Zielordner für index.html (Standard: Ordner dieses Skripts)",
    )
    args = parser.parse_args()
    cells, evaluation_id, row_count = summarize_attempts(args.attempts)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    html_path = args.output_dir / "index.html"
    html_path.write_text(render_document(cells, evaluation_id, row_count), encoding="utf-8")
    print(f"Exportiert: {html_path} ({row_count:,} Fälle)")


if __name__ == "__main__":
    main()
