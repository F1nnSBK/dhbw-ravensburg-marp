---
marp: true
theme: dhbw
paginate: true
header: "Citation Evaluation"
footer: "Capstone-Project, Präsentation 2, 19.11.2026"
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
## KI-Agenten prüfen Literaturangaben – Meeting 2

<div class="meta">
<div><strong>Team</strong>Finn Hertsch, Tino Strasser<br>Maximilian Vogt, Florian Dittmann</div>
<div><strong>Product Owner</strong>Prof. Dr. Andreas Schilling</div>
<div><strong>Meeting 2</strong>DSKI, WDS124 / WDS224<br>19.11.2026</div>
</div>

---

###### Überblick
# Agenda

<div class="agenda">
<div><span>01</span>Rückblick &amp; Projektstand</div>
<div><span>04</span>Ergebnis-UI &amp; Demo</div>
<div><span>02</span>Fortschritt seit Meeting 1</div>
<div><span>05</span>Probleme &amp; Risiken</div>
<div><span>03</span>Neue Ergebnisse</div>
<div><span>06</span>Ausblick &amp; Nächste Schritte</div>
</div>

---

###### 01, Rückblick
# Wo wir in Meeting 1 standen

<div class="grid g3">
<div class="kpi-card"><div class="number">9.442</div><div class="label">CiteAudit-Zitate</div><div class="sub">Label Real / Fake, 31 % Fake</div></div>
<div class="kpi-card hl"><div class="number">241</div><div class="label">Zitate im ersten Lauf</div><div class="sub">DGX Spark, danach Überhitzung</div></div>
<div class="kpi-card"><div class="number">v7</div><div class="label">Neue Kategoriendefinition</div><div class="sub">Form- oder Inhaltsfehler?</div></div>
</div>

> Ausgangspunkt für heute: **Spark-Ausfälle ausschließen, Fehlalarme senken, skalieren.**

---

###### 01, Projektstand
# Kanban-Board

<div class="placeholder" style="height: 380px;">

**TODO: Aktuelles Board eintragen**

Backlog, To Do, In Arbeit, In Review, Erledigt – Stand zum Meeting 2

</div>

<p class="note">Vorlage aus Meeting 1: 5 Spalten (Backlog / To Do / In Arbeit / In Review / Erledigt) mit CE-Nummern und Zuständigkeiten.</p>

---

###### 01, Zeitplan
# Projektplan

![w:1136](assets/project-plan-gantt.svg)

<p class="note">TODO: Gantt bei Bedarf aktualisieren (scripts/generate_gantt.py) und Meilenstein für Meeting 2 markieren.</p>

---

###### 02, Fortschritt seit Meeting 1
# Was seit dem letzten Meeting passiert ist

<div class="steps">
<div class="step-item active"><div class="step-num">01</div><div class="step-title">Spark-Ausfälle ausschließen</div><div class="step-desc">TODO: GPU-Monitoring &amp; RTX 6000 (CE-22, CE-29) – Ergebnis eintragen</div></div>
<div class="step-item"><div class="step-num">02</div><div class="step-title">Fehlalarme senken</div><div class="step-desc">Noch offen: 1.031 FP (16,1 % der unauffälligen Zitate) in Run 1 – Analyse auf der Fehlerfolie</div></div>
<div class="step-item active"><div class="step-num">03</div><div class="step-title">Skalieren</div><div class="step-desc">Erreicht: Run 1 mit 9.354 Versuchen statt 200–241 in Meeting 1 (Evaluation db5213ce)</div></div>
<div class="step-item"><div class="step-num">04</div><div class="step-title">Zugriff</div><div class="step-desc">TODO: WebUI mit Login statt SSH (CE-32, CE-34) – Stand eintragen</div></div>
</div>

---

###### 03, Neue Ergebnisse
# Run 1: nahezu der gesamte Benchmark

<div class="columns" style="align-items: start;">
<div class="kpi-stack" style="flex: 0.5;">
<div class="kpi-card"><div class="number">9.354</div><div class="label">Versuche in Run 1</div><div class="sub">Evaluation db5213ce, von 9.442 CiteAudit-Zitaten</div></div>
<div class="kpi-card hl"><div class="number">0,82</div><div class="label">F1 (Problem = positiv)</div><div class="sub">Precision 73,0 %, Recall 94,8 %, Accuracy 87,4 %</div></div>
<div class="card red"><p><strong>Recall 94,8 %</strong>, aber <strong>1.031 Fehlalarme</strong> – Precision bleibt die Baustelle.</p></div>
</div>
<div style="flex: 1.5;">

<iframe src="../data/citation-confusion-matrix/index.html" title="Interaktive Konfusionsmatrix, Run 1" style="display:block; width:100%; height:460px; border:0;"></iframe>

</div>
</div>


---

###### 03, Fehleranalyse
# Fehlalarme dominieren – verpasste Probleme sind selten

<div class="columns">
<div class="card red" style="flex: 1;">

### 1.031 False Positives, 16,1 %

<p>Häufigste Modell-Fehlereinträge bei FP: <strong>Title mismatch</strong> (51×), <strong>Wrong publication year</strong> (37×), <strong>Author name mismatch</strong> (36×). Dazu blockierte Quellen (Captcha) als „nicht verifizierbar“.</p>

</div>
<div class="card" style="flex: 1;">

### Nur 152 False Negatives, 5,2 %

<p>Übersehene Probleme sind meist subtile Autorenabweichungen (Initialen, Namenszusätze). Bei TP führen dieselben Kategorien: Autor (114×), Titel (100×), Jahr (92×).</p>

</div>
</div>

<p class="note">Groß-/Kleinschreibung im Titel taucht v. a. bei korrekten Zitaten auf (TN: 155× + 84× + 51×) – ein Formthema, das nicht als Inhaltsfehler zählen darf (v7-Regel). Alle Fehlertexte: Modellausgaben aus <code>answer_json</code>, nicht verifizierte Gold-Kategorien.</p>

---

###### 03, Vergleich
# Vergleich zu Meeting 1

| Kennzahl | Meeting 1 (Pilot) | Meeting 2 (Run 1) |
| :--- | :---: | :---: |
| Stichprobe | 166–241 Zitate | **9.354 Versuche** |
| Beste Precision | 63 % (gpt-oss, Spark, v6) | **73,0 %** |
| Recall | 94–98 % | **94,8 %** |
| F1 | 0,72–0,75 | **0,82** |
| Accuracy | 74–83 % | **87,4 %** |

<p class="note">Achtung, nur grob vergleichbar: Meeting 1 = Fake/Real auf Pilot-Stichproben (qwen v7: n = 166, F1 0,72), Run 1 = Problem/kein Problem auf fast dem gesamten Benchmark. Der Sprung kommt v. a. aus der größeren, anders zusammengesetzten Stichprobe – nicht als reiner Modellgewinn lesen.</p>

---

###### 04, Ergebnis-UI
# Ergebnis-UI: Stand &amp; Demo

<div class="grid g2" style="gap: 24px;">
<div class="shot">
<div class="cap">Meeting 1</div>
<img src="assets/ui-preview-dataset.png" alt="Ergebnis-UI aus Meeting 1" style="height: 330px; object-fit: contain; background: var(--surface);">
<div class="card" style="margin-top: 14px; text-align: center;"><strong>Dashboard, Analyse</strong></div>
</div>
<div class="shot new">
<div class="cap">Meeting 2, TODO: Screenshot austauschen</div>
<div class="placeholder" style="height: 330px;">Neuen Screenshot hier einfügen<br><span class="note">assets/ui-*.png</span></div>
<div class="card red" style="margin-top: 14px; text-align: center;"><strong>TODO: Was ist neu?</strong></div>
</div>
</div>

---

###### 05, Probleme &amp; Risiken
# Was uns aktuell bremst

<div class="columns">
<div style="flex: 1.3;">

| | Risiko / Problem | Maßnahme |
| :--- | :--- | :--- |
| **R1** | **Server fällt unbemerkt aus** | TODO: Monitoring-Stand (CE-29) |
| **R2** | **Viele Fehlalarme** (1.031 FP, 16,1 %) | Titel-/Jahr-/Autoren-Checks schärfen, Formfehler (Großschreibung) konsequent als Status 2 werten |
| **R3** | **Blockierte Quellen** (Captcha, z. B. ScienceDirect) | Als „nicht verifizierbar“ getrennt ausweisen, nicht als Fake zählen; Backoff/Retry |
| **R4** | **Bot-Erkennung, Rate-Limits** | Backoff, Fehler protokollieren |

</div>
<div style="flex: 0.75;">

<img src="assets/risk-matrix.svg" style="width: 100%; max-height: 400px; display: block;">

</div>
</div>

---

###### 06, Ausblick
# Nächste Schritte

<div class="steps">
<div class="step-item active" style="border: 1.5px solid rgba(226, 0, 26, 0.4);">
<div class="step-num" style="color: var(--red); font-weight: 700;">01, Dringend</div>
<div class="step-title" style="color: var(--red);">Fehlalarme senken</div>
<div class="step-desc">1.031 FP angehen: Titel-, Jahr- und Autorenabgleich schärfen, Precision über 73,0 % heben</div>
</div>
<div class="step-item">
<div class="step-num">02</div>
<div class="step-title">Restabdeckung klären</div>
<div class="step-desc">9.354 von 9.442 Zitaten ausgewertet – verbleibende 88 Versuche abschließen</div>
</div>
<div class="step-item">
<div class="step-num">03</div>
<div class="step-title">FN-Fälle prüfen</div>
<div class="step-desc">152 übersehene Probleme sichten (v. a. Autoren-Initialen), Recall bei 94,8 % halten</div>
</div>
<div class="step-item">
<div class="step-num">04</div>
<div class="step-title">Zugriff &amp; Monitoring</div>
<div class="step-desc">TODO: WebUI mit Login statt SSH (CE-32, CE-34), GPU-Monitoring (CE-29) – Stand eintragen</div>
</div>
</div>

---

<!-- _class: end -->
<!-- _paginate: false -->

# Danke!
## Fragen & Diskussion

<div class="meta">
<div><strong>Team</strong>Finn Hertsch, Tino Strasser<br>Maximilian Vogt, Florian Dittmann</div>
<div><strong>Repo</strong>github.com/FlorianDitt/citation-evaluation</div>
</div>

---

<!-- _class: chapter -->
<!-- _paginate: false -->

<div class="chapter-num">Backup</div>

# Backup-Folien

---

###### Backup
# Pilot-Ergebnisse aus Meeting 1

<div class="columns" style="align-items: start;">
<div style="flex: 1;">

<img src="assets/ab-confusion.svg" style="width: 100%; display: block;">

</div>
<div style="flex: 1;">

<img src="assets/model-comparison.svg" style="width: 100%; display: block;">

<p class="note">Meeting 1, Pilot-Stichproben: v6 → v7 hob den Recall (95 % → 98 %), die FP blieben bei 42. Run 1 (n = 9.354) ist damit nur grob vergleichbar.</p>

</div>
</div>
