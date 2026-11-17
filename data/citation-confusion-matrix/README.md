# Interaktive Konfusionsmatrix für Marp

Eigenständige HTML/CSS-Komponente mit Hover- und Tastatur-Fokus-Details für
TP/TN/FP/FN. Sie benötigt weder JavaScript noch externe Bibliotheken und
funktioniert in der **HTML-Ausgabe** der Präsentation. PDF- und PPTX-Exporte
unterstützen das interaktive Hover-Verhalten des eingebetteten HTMLs nicht.

## Einbinden

`npm run build:html` legt die Präsentation unter `dist/index.html` ab. In eine
Folie in `slides.md` kann dort dieses HTML eingefügt werden:

```html
<iframe
  src="../data/citation-confusion-matrix/index.html"
  title="Interaktive Konfusionsmatrix, Run 1"
  style="display:block; width:100%; height:540px; border:0;"
></iframe>
```

Die Pfadangabe ist relativ zu `dist/index.html` bzw. zur Marp-Server-URL
(`http://localhost:8080/slides.md`). Der Marp-Server liefert Dot-Verzeichnisse
wie `.agents/` nicht aus, deshalb liegt das Paket unter `data/`. Beim
Veröffentlichen müssen neben `dist/` auch `data/citation-confusion-matrix/`
und dessen `index.html` sowie `confusion-matrix.css` mit ausgeliefert werden.

Das Paket enthält:

- `index.html`: exportierte Matrix und die im HTML eingebetteten Zell-Details
- `confusion-matrix.css`: responsives Layout und Hover-/Fokus-Stile
- `export_component.py`: Standardbibliotheks-Exporter zum Aktualisieren der
  HTML-Datei aus einer `attempts.csv`

## Daten aktualisieren

```bash
python3 data/citation-confusion-matrix/export_component.py \
  --attempts /path/to/attempts.csv
```

Der Exporter schreibt `index.html` in den Paketordner. Die Referenzdaten
enthalten nur das binäre Label „Problem / kein Problem“; Tooltip-Fehlertexte
stammen deshalb ausdrücklich aus den Modellantworten (`answer_json.errors`)
und sind keine verifizierten Gold-Kategorien.
