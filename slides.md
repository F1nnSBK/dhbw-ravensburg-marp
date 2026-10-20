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
.board-col.compact .board-card { font-size: 14px; padding: 6px 10px; margin-bottom: 6px; }
.board-col.compact .board-card b { font-size: 10px; margin-bottom: 0; }

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
<div><span>01</span>Projektmanagement</div>
<div><span>04</span>Neue Kategoriendefinition</div>
<div><span>02</span>Benchmark & Bewertung</div>
<div><span>05</span>Ergebnis-UI</div>
<div><span>03</span>Ergebnisse</div>
<div><span>06</span>Ausblick</div>
</div>

---

###### 01 · Projektstand
# Kanban-Board

<div class="board" style="grid-template-columns: repeat(5, 1fr); gap: 12px;">
<div class="board-col compact">
<div class="board-head">Backlog <span>7</span></div>
<div class="board-card"><b>CE-30</b>DSGVO & Recht</div>
<div class="board-card"><b>CE-31</b>Statistische Tests</div>
<div class="board-card"><b>CE-33</b>CLI ausbauen</div>
<div class="board-card"><b>CE-28</b>Multi-User-Zugriff</div>
<div class="board-card"><b>CE-29</b>Status Modellserver</div>
<div class="board-card"><b>CE-34</b>WebUI mit Login</div>
<div class="board-card"><b>CE-32</b>WebUI statt SSH</div>
</div>
<div class="board-col">
<div class="board-head">To Do <span>0</span></div>
</div>
<div class="board-col">
<div class="board-head">In Arbeit <span>3</span></div>
<div class="board-card"><b>CE-25 <span class="who">Maximilian</span></b>Judgement Calls & parallele Worker</div>
<div class="board-card"><b>CE-23 <span class="who">Florian</span></b>Neue Kategoriendefinition testen</div>
<div class="board-card"><b>CE-22 <span class="who">Finn</span></b>RTX 6000 für parallele Samples</div>
</div>
<div class="board-col">
<div class="board-head">In Review <span>1</span></div>
<div class="board-card"><b>CE-24 <span class="who">Finn</span></b>Präsentation mit Marp</div>
</div>
<div class="board-col">
<div class="board-head">Erledigt <span>2</span></div>
<div class="board-card done"><b>CE-21 <span class="who">Tino</span></b>Rechenleistung angefragt</div>
<div class="board-card done"><b>CE-26 <span class="who">Tino</span></b>Ergebnis-UI verbessern</div>
</div>
</div>

---

###### 01 · Zeitplan
# Projektplan (Oktober 2026)

![w:1136](assets/project-plan-gantt.svg)

---

###### 01 · Risikomanagement
# Risiken früh sehen, nicht erst im Ergebnis

<div class="columns" style="align-items: center;">
<div style="flex: 1.55;">

| | Risiko | Strategie | Maßnahme |
| :--- | :--- | :--- | :--- |
| **R1** | **Server fällt unbemerkt aus** (Spark 2× überhitzt) | Vermeiden | Läufe auf RTX 6000 (CE-22), Kapazitätsstatus (CE-29) |
| **R2** | **Viele Fehlalarme** | Vermindern | Fehlfälle analysieren, Prompt nachschärfen |
| **R3** | **Technische Ausfälle** | Vermindern | Worker stabilisieren, Resume testen |
| **R4** | **Bot-Erkennung**, Rate-Limits | Akzeptieren | Backoff, Fehler protokollieren |

</div>
<div style="flex: 0.75;">

<img src="assets/risk-matrix.svg" style="width: 100%; max-height: 400px; display: block;">

</div>
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

###### 03 · Erster Lauf
# DGX Spark: Vollauf geplant, 241 Zitate geschafft

<div class="columns" style="align-items: center;">
<div class="kpi-stack" style="flex: 0.9;">
<div class="card"><p>Ziel war ein <strong>Vollauf</strong> über alle 9.442 Zitate mit <strong>gpt-oss</strong> auf der <strong>DGX Spark</strong>.</p></div>
<div class="card red"><p>Die Spark ist <strong>zweimal überhitzt</strong> – und wir haben es jeweils <strong>viel zu spät</strong> bemerkt.</p></div>
<div class="card"><p>Übrig blieben <strong>241 Zitate</strong>: ein erster Anhaltspunkt, kein Endergebnis.</p></div>
</div>
<div style="flex: 1.1;">

![w:400](assets/spark-confusion.svg)

</div>
</div>

---

###### 04 · Kategoriendefinition
# v6 nennt Fehlertypen, v7 stellt eine Prüffrage

<div class="columns" style="gap: 24px; margin-bottom: 22px;">
<div class="card" style="flex: 1;">

### v6 · zwei Typenlisten
<p><strong>Status 2:</strong> Tippfehler, Formatierung, Groß-/Kleinschreibung</p>
<p><strong>Status 3:</strong> Autorname falsch, Jahr, URL-Domain, fehlende Metadaten</p>

<p class="note">Überschneidung: Ist ein Tippfehler im Autornamen ein Tippfehler oder ein falscher Autorname?</p>

</div>
<div class="card red" style="flex: 1;">

### v7 · Form oder Inhalt?
<p>Verschwindet der Fehler, wenn Schreibweise, Leerzeichen, Interpunktion und Zitierstil ignoriert werden?</p>
<p><strong>Ja → 2 Formfehler · Nein → 3 Inhaltsfehler</strong></p>

<p class="note">Der schwerste Fehler bestimmt den Status, nicht die Anzahl.</p>

</div>
</div>

| Beispiel | v6 | v7 |
| :--- | :---: | :---: |
| „Sennnrich“ statt „Sennrich“ | 2 oder 3 | **3** |
| Falsche Autorenreihenfolge | unklar | **3** |
| Titel anders groß/klein geschrieben | 2 | **2** |

---

###### 04 · Vergleich v6 → v7
# v7 erkennt mehr Fakes – die Fehlalarme bleiben

<div class="columns" style="align-items: center; gap: 28px;">
<div style="flex: 1.15;">

<img src="assets/ab-confusion.svg" style="width: 100%; max-height: 420px; display: block;">

</div>
<div style="flex: 0.85;">

<img src="assets/v6-v7-status.svg" style="width: 100%; display: block;">

</div>
</div>

<p class="note">qwen · RTX 6000 · Browser-use · dieselben 200 Zitate · v6: 18.10., v7: 13.10.2026</p>

---

###### 04 · Vergleich
# gpt-oss ist präziser, qwen findet mehr Fakes

<div class="columns" style="align-items: center;">
<div style="flex: 1;">

<img src="assets/model-comparison.svg" style="width: 100%; max-height: 420px; display: block;">

</div>
<div class="kpi-stack" style="flex: 0 0 280px;">
<div class="kpi-card"><div class="number">160 s</div><div class="label">gpt-oss pro Zitat</div><div class="sub">DGX Spark</div></div>
<div class="kpi-card hl"><div class="number">~240 s</div><div class="label">qwen pro Zitat</div><div class="sub">RTX 6000</div></div>
<div class="card"><p>Alle mit Browser-use. gpt-oss lief auf einer <strong>anderen Stichprobe</strong>, also nur grob vergleichbar.</p></div>
</div>
</div>

---

###### 05 · Ergebnis-UI
# Vorher / Nachher

<div class="grid g2" style="gap: 24px;">
<div class="shot">
<div class="cap">Vorher</div>
<img src="assets/ui-old.png" alt="Frühere Oberfläche mit Formular und Laufauswahl" style="height: 330px; object-fit: contain; background: var(--surface);">
<div class="card" style="margin-top: 14px; text-align: center;"><strong>Formular · Tabelle</strong></div>
</div>
<div class="shot new">
<div class="cap">Nachher</div>
<img src="assets/ui-preview-dataset.png" alt="Aktueller Arbeitsbereich mit Preview Dataset und ausdrücklich synthetischen Mock-Vergleichen" style="height: 330px; object-fit: contain; background: var(--surface);">
<div class="card red" style="margin-top: 14px; text-align: center;"><strong>Dashboard · Analyse</strong><span class="tag red" style="margin-left: 10px;">Mock-Werte</span></div>
</div>
</div>

---

###### 05 · Ergebnis-UI
# Live-Demo

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
<div><span class="tag">Preview Dataset</span> <span class="tag red">Mock-Werte</span></div>
<a href="http://127.0.0.1:8765/#run=preview-synthetic-evaluation&amp;view=statistics&amp;metric=generation_seconds&amp;chart=box&amp;unit=case" target="_blank" rel="noopener noreferrer" style="font-size: 20px; font-weight: 700;">Browser öffnen ↗</a>
</div>
<div style="height: 396px; border: 1px solid var(--rule); border-radius: 10px; overflow: hidden;">
<iframe src="http://127.0.0.1:8765/#run=preview-synthetic-evaluation&amp;view=statistics&amp;metric=generation_seconds&amp;chart=box&amp;unit=case" title="Live-Demo: Preview Dataset mit gekennzeichneten Mock-Werten" sandbox="allow-scripts allow-same-origin allow-downloads" loading="lazy" style="display: block; width: 1136px; height: 396px; border: 0;"></iframe>
</div>

---

###### 06 · Ausblick
# Nächste Schritte

<div class="steps">
<div class="step-item active" style="border: 1.5px solid rgba(226, 0, 26, 0.4);">
<div class="step-num" style="color: var(--red); font-weight: 700;">01 · Dringend</div>
<div class="step-title" style="color: var(--red);">Spark-Ausfälle ausschließen</div>
<div class="step-desc">Überhitzung verhindern, GPU-Monitoring & RTX 6000 (CE-22, CE-29)</div>
</div>
<div class="step-item">
<div class="step-num">02</div>
<div class="step-title">Fehlalarme senken</div>
<div class="step-desc">42 False Positives analysieren, Prompt nachschärfen</div>
</div>
<div class="step-item">
<div class="step-num">03</div>
<div class="step-title">Skalieren</div>
<div class="step-desc">RTX 6000, parallele Worker, 5.000 Zitate</div>
</div>
<div class="step-item">
<div class="step-num">04</div>
<div class="step-title">Zugriff</div>
<div class="step-desc">WebUI mit Login statt SSH (CE-32, CE-34)</div>
</div>
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

---

<!-- _class: chapter -->
<!-- _paginate: false -->

<div class="chapter-num">Backup</div>

# Backup-Folien

---

<!-- frontend-ui-status:start -->
###### Backup · Frontend
# UI-Stand

<div class="board" style="grid-template-columns: repeat(3, 1fr); gap: 18px;">
<div class="board-col">
<div class="board-head">Umgesetzt</div>
<div class="board-card" style="font-size: 18px; padding: 10px;">Navigation · Runs · Filter</div>
<div class="board-card" style="font-size: 18px; padding: 10px;">Themes · Sprachen</div>
<div class="board-card" style="font-size: 18px; padding: 10px;">Mobil · Tastatur</div>
<div class="board-card" style="font-size: 18px; padding: 10px;">Statistiken · Diagramme</div>
<div class="board-card" style="font-size: 18px; padding: 10px;">Vergleiche · Quantile</div>
<div class="board-card" style="font-size: 18px; padding: 10px;">Tokens · Thinking · Kosten</div>
<div class="board-card" style="font-size: 18px; padding: 10px;">CSV · JSON · SVG</div>
</div>
<div class="board-col">
<div class="board-head">Hinterlegt / vorbereitet</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">Konten · Rechte</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">Limits · Fair Queue</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">API-Verträge</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">Mock-Daten · Thinking</div>
<div class="card" style="padding: 12px 0;"><strong>Frontend vorbereitet</strong></div>
</div>
<div class="board-col" style="background: var(--red-soft);">
<div class="board-head">Fehlt</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">Login · Sitzungen</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">Konten-Persistenz</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">Quoten · Fair Queue</div>
<div class="board-card" style="font-size: 20px; padding: 14px;">Live-Modellstatus</div>
<div class="card red" style="padding: 12px 0;"><strong>Backend offen</strong><br><span style="font-size: 16px;">Multiuser · Live-Status</span></div>
</div>
</div>

---

<!-- frontend-ui-status:end -->
<!-- frontend-ui-functions:start -->
###### Backup · Frontend
# UI-Funktionen

<div class="grid g3" style="gap: 12px; font-size: 17px; line-height: 1.35;">
<div class="card" style="padding: 12px 16px;">
<h3>Laufverwaltung</h3>
Modelle · Agenten · Datensatz<br>
Binärmodus · Wiederholungen · Timeout<br>
Start · Pause · Fortsetzen · Ausblenden<br>
Suche · Laufwahl · Fortschritt · Restzeit
</div>
<div class="card" style="padding: 12px 16px;">
<h3>Ergebnisansicht</h3>
Modell-/Agenten-/Statusfilter<br>
Suche · Sortierung · Filter zurücksetzen<br>
Fehlerdetails · Antwort · Referenz<br>
Rohdaten · JSON-Vergleich · Messwerte
</div>
<div class="card" style="padding: 12px 16px;">
<h3>Qualitätskennzahlen</h3>
Status · Autor · Titel · Jahr · Fehlerzahl<br>
Accuracy · Präzision · Recall · F1<br>
FPR · FNR · technische Fehler<br>
Balanced Accuracy · MCC · Kappa
</div>
<div class="card" style="padding: 12px 16px;">
<h3>Statistik &amp; Vergleiche</h3>
Mittelwert · Median · Quantile · IQR<br>
Konfidenzintervalle · Messabdeckung<br>
Paar-/Mehrfachtests · Effektgrößen<br>
Pearson · Spearman · Holm-Korrektur
</div>
<div class="card" style="padding: 12px 16px;">
<h3>Diagramme</h3>
Boxplot · Histogramm · ECDF<br>
Outcomes · Matrix · Scatter · Timeline<br>
Paare · Forest · Differenzen<br>
Richtung · Quantile
</div>
<div class="card" style="padding: 12px 16px;">
<h3>Ressourcen &amp; Nutzung</h3>
Adapter · Queue · Generation · Tokens/s<br>
Input · Output · Thinking · Kosten<br>
Exa-Limits · Mock-Kennzeichnung<br>
Nutzung je Lauf/Modell · alle Läufe
</div>
<div class="card" style="padding: 12px 16px;">
<h3>Darstellung &amp; Bedienung</h3>
Hell · Dunkel · Pink Glass · System<br>
Liquid Glass · Animationen · 4 Sprachen<br>
Mobil · Tastatur · reduzierte Bewegung<br>
Hilfe · Verbindungsstatus · Wiederholen
</div>
<div class="card" style="padding: 12px 16px;">
<h3>Export &amp; Konfiguration</h3>
CSV · JSON · SVG · Direktlinks<br>
Diagrammfilter · Beobachtungseinheit<br>
Konfidenzniveau · Parallelität · Seed<br>
Docker-Worker · Tokenpreise
</div>
<div class="card red" style="padding: 12px 16px;">
<h3>Vorbereitet · Backend offen</h3>
Profil · Login · Sitzungen · Rollen<br>
Nutzerverwaltung · Datenschutzaktionen<br>
Limits · Quoten · Fair Queue<br>
Live-Modellstatus
</div>
</div>

---

<!-- frontend-ui-functions:end -->
###### Backup · System
# Die Ground Truth verlässt den Evaluator nie

![w:1136](assets/citation-pipeline.svg)

<div class="grid g3" style="margin-top: 18px;">
<div class="card"><p><strong>Lokal</strong> auf DHBW-GPUs (RTX 6000, DGX Spark)</p></div>
<div class="card"><p><strong>3 Agenten:</strong> Browser-use, Hermes, OpenCode</p></div>
<div class="card"><p><strong>600 s</strong> Timeout, Läufe fortsetzbar</p></div>
</div>

---

###### Backup · Problem & Ziel
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

###### Backup · Fehleranalyse
# 42 Fehlalarme: Die Hälfte liegt am Agenten, nicht am Zitat

<div class="columns" style="align-items: center; gap: 28px;">
<div style="flex: 1.15;">

<img src="assets/fp-analysis.svg" style="width: 100%; max-height: 400px; display: block;">

</div>
<div class="kpi-stack" style="flex: 0.85;">
<div class="card"><p><strong>Wei et al. 2022</strong>, Chain-of-Thought: Status 4, keine Begründung – eines der meistzitierten Paper</p></div>
<div class="card"><p><strong>CoQA</strong>: Agent schreibt selbst „minor form error“, vergibt aber Status 3</p></div>
<div class="card red"><p><strong>„Philiph H. S. Torr“</strong>: nach v7-Regel Status 3, CiteAudit sagt Real – Rubrik und Benchmark widersprechen sich</p></div>
</div>
</div>

<p class="note">qwen · RTX 6000 · Browser-use · Prompt v7 · 13.10.2026 · 42 von 110 realen Zitaten fälschlich als Fake markiert</p>
