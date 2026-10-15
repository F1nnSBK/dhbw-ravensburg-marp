---
marp: true
theme: dhbw
paginate: true
header: "Citation Evaluation"
footer: "Capstone-Project · Präsentation 1 · 20.10.2026"
---

<style>
/* ---------- Modern, flat layer on top of the DHBW theme ---------- */
:root {
  --ink: #1B1E22;
  --muted: #5C6971;
  --faint: #9AA5AC;
  --surface: #F3F4F6;
  --rule: #E2E6E9;
  --red: #E2001A;
  --red-soft: #FDF0F1;
}

section { padding: 96px 72px 70px; font-size: 22px; color: var(--ink); }
section p, section li { color: var(--ink); }
header { border-bottom: none; font-size: 12px; color: var(--faint); letter-spacing: 0.04em; }
footer { border-top: none; font-size: 12px; color: var(--faint); }
section::after { border-top: none; font-size: 12px; color: var(--faint); font-weight: 600; }

/* Kicker above the headline: ###### Text */
h6 {
  font-size: 13px; font-weight: 700; color: var(--red);
  text-transform: uppercase; letter-spacing: 0.14em; margin: 0 0 8px;
}
h1 { font-size: 36px; font-weight: 750; letter-spacing: -0.03em; line-height: 1.15; margin: 0 0 26px; }
h3 {
  font-size: 13px; font-weight: 700; color: var(--muted);
  text-transform: uppercase; letter-spacing: 0.1em; margin: 0 0 10px;
}
strong { color: var(--ink); }

ul > li::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--red); top: 0.62em; left: -1em; }
ul { padding-left: 1em; }
li { font-size: 21px; margin-bottom: 8px; }

/* Takeaway line */
blockquote {
  background: none; box-shadow: none; border-left: 3px solid var(--red);
  border-radius: 0; padding: 2px 0 2px 18px; margin: 22px 0 0;
}
blockquote p { font-size: 20px; color: var(--ink); }

/* Tables: rules only, no fills */
table { font-size: 17px; margin: 0; display: table; width: 100%; }
table th {
  background: none; color: var(--muted); border-bottom: 1.5px solid var(--ink);
  font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; padding: 8px 12px;
}
table td { border: none; border-bottom: 1px solid var(--rule); padding: 9px 12px; }
table th { border-top: none; border-left: none; border-right: none; }
table tr, table tr:nth-child(2n) { border: none; background: none; }
table tr:nth-child(even) td { background: none; }

code { background: var(--surface); border: none; color: var(--ink); }

/* Cards, KPIs, steps: one flat surface style */
.card, .kpi-card, .step-item, .board-col {
  background: var(--surface); border: none; border-radius: 14px; box-shadow: none;
}
.card { padding: 20px 22px; margin: 0; }
.card.accent, .card.slate { background: var(--surface); border: none; }
.card.red { background: var(--red-soft); }
.card p { margin: 0; }

.grid { display: grid; gap: 16px; }
.g2 { grid-template-columns: 1fr 1fr; }
.g3 { grid-template-columns: repeat(3, 1fr); }
.g4 { grid-template-columns: repeat(4, 1fr); }
.columns { gap: 36px; margin-top: 0; }

.kpi-card { text-align: left; padding: 18px 22px; border-top: none; }
.kpi-card .number { font-size: 44px; font-weight: 750; color: var(--ink); letter-spacing: -0.035em; margin: 0; }
.kpi-card.hl .number { color: var(--red); }
.kpi-card .label { font-size: 16px; font-weight: 600; color: var(--ink); margin-top: 2px; }
.kpi-card .sub { font-size: 14px; color: var(--muted); }
.kpi-stack { display: flex; flex-direction: column; gap: 14px; }

.step-item { padding: 20px 22px; border-top: none; }
.step-item.active { background: var(--red-soft); border-top: none; box-shadow: none; }
.step-num { font-size: 13px; color: var(--muted); letter-spacing: 0.1em; }
.step-item.active .step-num { color: var(--red); }
.step-title { font-size: 22px; font-weight: 700; margin: 4px 0 6px; }
.step-desc { font-size: 16px; color: var(--muted); line-height: 1.4; }
.steps { gap: 16px; margin: 0; }

.tag { border: none; border-radius: 999px; padding: 4px 12px; font-size: 11px; background: var(--surface); color: var(--muted); }
.tag.red { background: var(--red-soft); color: var(--red); }

/* Agenda */
.agenda { display: grid; grid-template-columns: 1fr 1fr; gap: 0 56px; margin-top: 8px; }
.agenda div { display: flex; align-items: baseline; gap: 20px; padding: 16px 0; border-bottom: 1px solid var(--rule); font-size: 24px; font-weight: 600; }
.agenda span { font-size: 15px; font-weight: 700; color: var(--red); letter-spacing: 0.08em; min-width: 26px; }

/* Kanban */
.board { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; align-items: start; }
.board-col { padding: 14px; }
.board-head { display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); margin-bottom: 10px; }
.board-card { background: #FFFFFF; border-radius: 10px; padding: 9px 12px; font-size: 16px; line-height: 1.3; margin-bottom: 8px; }
.board-card b { display: block; font-size: 11px; color: var(--faint); letter-spacing: 0.06em; margin-bottom: 2px; }
.board-card .prio { color: var(--red); }
.board-card .who { float: right; color: var(--muted); }
.board-card.done { color: var(--faint); text-decoration: line-through; }

/* Screenshots */
.shot img { width: 100%; max-height: 440px; object-fit: cover; object-position: top; border-radius: 10px; border: 1px solid var(--rule); display: block; }
.shot .cap { font-size: 13px; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; }
.shot.new .cap { color: var(--red); }
.note { font-size: 14px; color: var(--muted); margin-top: 10px; }

/* Placeholder */
.placeholder {
  display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
  border: 1.5px dashed #C6CDD2; border-radius: 14px; color: var(--muted); font-size: 16px; padding: 16px;
}

/* Status chips */
.st { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 8px; font-weight: 700; font-size: 15px; background: var(--surface); }
.st.f { background: var(--red-soft); color: var(--red); }

/* Title & end slides */
section.title h1, section.end h1 { font-size: 60px; letter-spacing: -0.04em; margin: 30px 0 10px; }
section.title h2, section.end h2 { font-size: 26px; font-weight: 500; color: var(--muted); margin: 0 0 40px; }
.meta { display: grid; grid-template-columns: repeat(3, auto); gap: 40px; justify-content: start; font-size: 16px; color: var(--muted); }
.meta strong { display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--red); margin-bottom: 4px; }
</style>

<!-- _class: title -->
<!-- _paginate: false -->

# Citation Evaluation
## KI-Agenten prüfen Literaturangaben

<div class="meta">
<div><strong>Team</strong>Finn Hertsch · Tino Strasser<br>Maximilian Vogt · Florian Dittmann</div>
<div><strong>Product Owner</strong>Prof. Dr. Andreas Schilling</div>
<div><strong>Sprint 1</strong>DSKI · WDS124 / WDS224<br>20.10.2026</div>
</div>

---

###### Überblick
# Agenda

<div class="agenda">
<div><span>01</span>Problem & Ziel</div>
<div><span>04</span>Neue Kategoriendefinition</div>
<div><span>02</span>System & Benchmark</div>
<div><span>05</span>Ergebnis-UI</div>
<div><span>03</span>Ergebnisse</div>
<div><span>06</span>Risiken & nächste Schritte</div>
</div>

---

###### 01 · Problem & Ziel
# KI erfindet Quellen – wir prüfen sie automatisch

<div class="grid g3">
<div class="card">

### Problem
Falsche Titel, Autor:innen, Jahre und DOIs fallen beim Lesen kaum auf.

</div>
<div class="card">

### Ansatz
Ein Agent sucht jede Quelle im Web, ein **lokales LLM** bewertet die Treffer.

</div>
<div class="card red">

### Ziel
Qualität und Laufzeit **reproduzierbar** am CiteAudit-Benchmark messen.

</div>
</div>

> Wir prüfen, ob eine Quelle **existiert und korrekt zitiert** ist, nicht ob sie die Aussage im Text belegt.

---

###### 02 · System
# Die Ground Truth verlässt den Evaluator nie

![w:1136](assets/citation-pipeline.svg)

<div class="grid g3" style="margin-top: 18px;">
<div class="card"><p><strong>Lokal</strong> auf DHBW-GPUs (RTX 6000, DGX Spark)</p></div>
<div class="card"><p><strong>3 Agenten:</strong> Browser-use, Hermes, OpenCode</p></div>
<div class="card"><p><strong>600 s</strong> Timeout, Läufe fortsetzbar</p></div>
</div>

---

###### 02 · Benchmark
# CiteAudit: 9.442 gelabelte Zitate

<div class="columns" style="align-items: center;">
<div class="kpi-stack" style="flex: 0.55;">
<div class="kpi-card"><div class="number">9.442</div><div class="label">Zitate, Label Real / Fake</div></div>
<div class="kpi-card hl"><div class="number">31 %</div><div class="label">davon Fake</div></div>
</div>
<div style="flex: 1.45;">

![w:720](assets/citeaudit-distribution.svg)

</div>
</div>

> Die Fake-Quote unterscheidet sich je Gruppe stark, deshalb werten wir **je `source_type`** aus.

---

###### 02 · Bewertung
# Vier Status, zwei Klassen

<div class="columns">
<div style="flex: 1.3;">

| | Status | Binär |
| :---: | :--- | :--- |
| <span class="st">1</span> | korrekt | Real |
| <span class="st">2</span> | nur Formfehler | Real |
| <span class="st f">3</span> | Inhaltsfehler | Fake |
| <span class="st f">4</span> | nicht verifizierbar | Fake |

</div>
<div class="kpi-stack" style="flex: 0.7;">
<div class="card"><p><strong>Fake</strong> ist die positive Klasse: Precision, Recall, F1</p></div>
<div class="card"><p><strong>Status 4</strong> heißt „nicht gefunden“, nicht „bewiesen falsch“</p></div>
<div class="card"><p><strong>Timeouts</strong> zählen getrennt, nie als Fake</p></div>
</div>
</div>

---

###### 03 · Projektstand
# Kanban-Board

<div class="board">
<div class="board-col">
<div class="board-head">To Do <span>4</span></div>
<div class="board-card"><b>CE-32 · <span class="prio">KRITISCH</span></b>WebUI statt SSH (Reverse Proxy)</div>
<div class="board-card"><b>CE-34 · <span class="prio">HOCH</span></b>WebUI mit Login absichern</div>
<div class="board-card"><b>CE-22 <span class="who">Finn</span></b>RTX 6000 für parallele Samples</div>
<div class="board-card"><b>CE-29</b>Kapazitätsstatus der Modellserver</div>
</div>
<div class="board-col">
<div class="board-head">In Arbeit <span>4</span></div>
<div class="board-card"><b>CE-23</b>Neue Kategoriendefinition testen</div>
<div class="board-card"><b>CE-25</b>Judgement Calls & parallele Worker</div>
<div class="board-card"><b>CE-26 <span class="who">Tino</span></b>Ergebnis-UI verbessern</div>
<div class="board-card"><b>CE-24 <span class="who">Finn</span></b>Präsentation mit Marp</div>
</div>
<div class="board-col">
<div class="board-head">Erledigt <span>1</span></div>
<div class="board-card done"><b>CE-21 <span class="who">Tino</span></b>Rechenleistung angefragt</div>
</div>
<div class="board-col">
<div class="board-head">Backlog <span>4</span></div>
<div class="board-card"><b>CE-30</b>DSGVO & deutsches Recht</div>
<div class="board-card"><b>CE-31</b>Statistische Tests</div>
<div class="board-card"><b>CE-33</b>CLI ausbauen</div>
<div class="board-card"><b>CE-28</b>Multi-User-Zugriff</div>
</div>
</div>

---

###### 03 · Laufzeit
# Ein Vollauf dauert sequentiell gut zwei Wochen

<div class="grid g3">
<div class="kpi-card"><div class="number">~150 s</div><div class="label">pro Zitat</div><div class="sub">gemessen: 157 s Median (gpt-oss)</div></div>
<div class="kpi-card hl"><div class="number">~16 Tage</div><div class="label">für 9.442 Zitate</div><div class="sub">mit nur einem Worker</div></div>
<div class="kpi-card"><div class="number">4 Stufen</div><div class="label">bis zum Vollauf</div><div class="sub">erst skalieren, wenn valide</div></div>
</div>

<div class="steps" style="margin-top: 18px;">
<div class="step-item active"><div class="step-num">50</div><div class="step-title">Smoke-Test</div></div>
<div class="step-item active"><div class="step-num">200 – 500</div><div class="step-title">Pilot</div></div>
<div class="step-item"><div class="step-num">5.000</div><div class="step-title">Skalierung</div></div>
<div class="step-item"><div class="step-num">9.442</div><div class="step-title">Vollauf</div></div>
</div>

---

###### 03 · Ergebnis
# Fast alle Fakes erkannt – aber zu viele Fehlalarme

<div class="columns" style="align-items: center;">
<div class="kpi-stack" style="flex: 0.55;">
<div class="kpi-card hl"><div class="number">98 %</div><div class="label">Recall</div><div class="sub">55 von 56 Fakes</div></div>
<div class="kpi-card"><div class="number">57 %</div><div class="label">Precision</div><div class="sub">42 Fehlalarme</div></div>
<div class="kpi-card"><div class="number">166 / 200</div><div class="label">gültige Urteile</div><div class="sub">34 technische Ausfälle</div></div>
</div>
<div style="flex: 1.45;">

![w:680](assets/v7-confusion.svg)

</div>
</div>

<p class="note">Stichprobe von 200 Zitaten · qwen-rtx6000 · Browser-use · Prompt v7 · 13.10.2026</p>

---

###### 04 · Kategoriendefinition
# Form oder Inhalt?

<div class="columns">
<div style="flex: 1;">
<div class="card" style="margin-bottom: 16px;">

### Prüffrage
Verschwindet der Fehler, wenn Schreibweise, Leerzeichen, Interpunktion und Zitierstil ignoriert werden?

</div>
<div class="grid g2">
<div class="card"><p><span class="st">2</span>&nbsp; <strong>Ja:</strong> Formfehler</p></div>
<div class="card red"><p><span class="st f">3</span>&nbsp; <strong>Nein:</strong> Inhaltsfehler</p></div>
</div>

> Der **schwerste** Fehler bestimmt den Status.

</div>
<div style="flex: 1;">

| Beispiel | Status |
| :--- | :---: |
| Titel anders groß/klein geschrieben | 2 |
| Überflüssiges „et al.“ | 2 |
| Autorname falsch, auch ein Buchstabe | 3 |
| Autor:innen fehlen oder vertauscht | 3 |
| Falsches Jahr, Venue oder Seiten | 3 |
| DOI eines anderen Werks | 3 |

</div>
</div>

---

###### 04 · Vergleich v6 → v7
# Status 2 ist jetzt sauber

<div class="columns" style="align-items: center;">
<div style="flex: 0.85;">

| | v6 | v7 |
| :--- | ---: | ---: |
| Recall | 94 % | **98 %** |
| Precision | **63 %** | 57 % |
| F1 | **0,75** | 0,72 |
| Fakes in Status 2 | 4 | **0** |

<p class="note">v6: gpt-oss, 241 Zitate · v7: qwen, 166 Zitate.<br>Andere Modelle und Stichproben, also noch kein fairer A/B-Test.</p>

</div>
<div style="flex: 1.15;">

![w:600](assets/v6-v7-status.svg)

</div>
</div>

---

###### 04 · Vergleich
# Modelle und Agenten

<span class="tag red">Platzhalter</span>

| Modell | Agent | Recall | Precision | F1 | Ø Dauer |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **[Modell A]** | Browser-use | [xx %] | [xx %] | [0,xx] | [xx s] |
| | Hermes | [xx %] | [xx %] | [0,xx] | [xx s] |
| | OpenCode | [xx %] | [xx %] | [0,xx] | [xx s] |
| **[Modell B]** | Browser-use | [xx %] | [xx %] | [0,xx] | [xx s] |
| | Hermes | [xx %] | [xx %] | [0,xx] | [xx s] |
| | OpenCode | [xx %] | [xx %] | [0,xx] | [xx s] |

---

###### 05 · Ergebnis-UI
# Vom Formular zum Dashboard

<div class="grid g2" style="gap: 24px;">
<div class="shot">
<div class="cap">Vorher</div>

![](assets/ui-old.png)

</div>
<div class="shot new">
<div class="cap">Nachher</div>

![](assets/ui-new.png)

</div>
</div>

<p class="note">Beide Ansichten mit denselben synthetischen Vorschau-Daten, ohne Modellaufrufe.</p>

---

###### 05 · Ergebnis-UI
# Statistik mit Konfidenzintervallen

<div class="columns" style="align-items: center;">
<div style="flex: 0.6;">

* Läufe **vergleichen**
* **95 %-KI** per Bootstrap
* **Worker** steuern
* Hell, Dunkel, Pink Glass

</div>
<div class="shot" style="flex: 1.4;">

![](assets/ui-stats.png)

</div>
</div>

---

###### 06 · Risiken
# Was uns bremsen kann

| Risiko | Gegenmaßnahme |
| :--- | :--- |
| **Viele Fehlalarme** bei realworld | Fehlfälle analysieren, Prompt nachschärfen |
| **Technische Ausfälle** (17 %) | Worker stabilisieren, Resume testen |
| **Bot-Erkennung**, Rate-Limits | Backoff, Fehler protokollieren |
| **Lizenz** des Datensatzes unklar | vor jeder Weitergabe klären |

---

###### 06 · Ausblick
# Nächste Schritte

<div class="steps">
<div class="step-item active"><div class="step-num">01</div><div class="step-title">Fairer A/B-Test</div><div class="step-desc">v6 und v7 mit gleichem Modell und gleicher Stichprobe</div></div>
<div class="step-item"><div class="step-num">02</div><div class="step-title">Zugriff</div><div class="step-desc">WebUI mit Login statt SSH (CE-32, CE-34)</div></div>
<div class="step-item"><div class="step-num">03</div><div class="step-title">Skalieren</div><div class="step-desc">RTX 6000, parallele Worker, 5.000 Zitate</div></div>
</div>

---

<!-- _class: end -->
<!-- _paginate: false -->

# Danke!
## Fragen & Diskussion

<div class="meta">
<div><strong>Team</strong>Finn Hertsch · Tino Strasser<br>Maximilian Vogt · Florian Dittmann</div>
<div><strong>Repo</strong>github.com/FlorianDitt/citation-evaluation</div>
</div>
