---
marp: true
theme: dhbw
paginate: true
header: "Capstone-Project · KI-Agent: Literatur Check"
footer: "Citation Evaluation · Präsentation 1 · 20.10.2026"
---

<style>
/* Agenda: larger type, more breathing room */
.agenda-grid { gap: 16px 24px; margin-top: 24px; }
.agenda-item { padding: 16px 18px; }
.agenda-num { width: 42px; height: 42px; font-size: 18px; }
.agenda-text strong { font-size: 21px; }
.agenda-text span { font-size: 16px; margin-top: 3px; }

/* Steps: readable from the back row */
.steps { gap: 16px; }
.step-item { padding: 16px 18px; }
.step-num { font-size: 13px; }
.step-title { font-size: 20px; margin-bottom: 6px; }
.step-desc { font-size: 16px; line-height: 1.4; color: #3F474C; }

/* KPI cards */
.kpi-card .label { font-size: 16px; }
.kpi-card .sub { font-size: 14px; }
.kpi-stack .kpi-card { margin-bottom: 12px; text-align: left; padding: 12px 18px; }
.kpi-stack .kpi-card .number { font-size: 34px; }

/* Kanban board */
.board {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-top: 6px;
  align-items: start;
}
.board-col {
  background: #F8F9FA;
  border: 1px solid #E2E6E9;
  border-radius: 8px;
  padding: 10px;
}
.board-head {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #5C6971;
  margin-bottom: 8px;
}
.board-card {
  background: #FFFFFF;
  border: 1px solid #E2E6E9;
  border-left: 4px solid #9AA5AC;
  border-radius: 6px;
  padding: 7px 10px;
  font-size: 15px;
  line-height: 1.3;
  margin-bottom: 7px;
}
.board-card b { display: block; font-size: 12px; color: #5C6971; letter-spacing: 0.03em; }
.board-card.crit { border-left-color: #E2001A; }
.board-card.high { border-left-color: #8E130A; }
.board-card.done { color: #5C6971; text-decoration: line-through; }
.board-card .prio { color: #E2001A; font-weight: 700; font-size: 12px; text-transform: uppercase; }
.board-card .who { color: #5C6971; font-size: 12px; float: right; }

/* Placeholder for figures that are not ready yet */
.placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  border: 1.5px dashed #BBC3C8;
  border-radius: 8px;
  color: #5C6971;
  font-size: 16px;
  line-height: 1.4;
  padding: 16px;
  box-sizing: border-box;
}
.placeholder strong { font-size: 18px; color: #3F474C; }

/* Scope list: check and cross markers */
ul.scope-in > li::before { content: "✓"; font-size: 0.9em; top: 0; }
ul.scope-out > li::before { content: "✕"; font-size: 0.85em; top: 0.05em; color: #5C6971; }

.figure { margin-top: 8px; }
.caption { font-size: 15px; color: #5C6971; margin-top: 4px; }
section table { font-size: 17px; }
</style>

<!-- _class: title -->
<!-- _paginate: false -->

# Citation Evaluation
## KI-Agenten prüfen Literaturangaben – Projektstand Sprint 1

<div class="title-meta-grid">
<div class="title-meta-col">

**Team:** Finn Hertsch, Tino Strasser, Maximilian Vogt, Florian Dittmann  
**Studiengang:** Data Science und Künstliche Intelligenz  
**Kurs:** WDS124 / WDS224 · Capstone-Project

</div>
<div class="title-meta-col">

**Product Owner:** Prof. Dr. Andreas Schilling  
**Anlass:** Präsentation 1 (Sprint 1)  
**Datum:** 20.10.2026

</div>
</div>

---

# Agenda

<div class="agenda-grid">
  <div class="agenda-item">
    <div class="agenda-num">01</div>
    <div class="agenda-text">
      <strong>Ausgangslage & Ziel</strong>
      <span>Warum Literaturangaben automatisch prüfen?</span>
    </div>
  </div>
  <div class="agenda-item">
    <div class="agenda-num">02</div>
    <div class="agenda-text">
      <strong>System & Methodik</strong>
      <span>Datenfluss, CiteAudit-Benchmark, Bewertung</span>
    </div>
  </div>
  <div class="agenda-item">
    <div class="agenda-num">03</div>
    <div class="agenda-text">
      <strong>Projektstand</strong>
      <span>Kanban-Board und laufende Arbeiten</span>
    </div>
  </div>
  <div class="agenda-item">
    <div class="agenda-num">04</div>
    <div class="agenda-text">
      <strong>Ergebnisse</strong>
      <span>Großer Lauf, Modelle, Agenten, Kategorien</span>
    </div>
  </div>
  <div class="agenda-item">
    <div class="agenda-num">05</div>
    <div class="agenda-text">
      <strong>Ergebnis-UI</strong>
      <span>Lauf- und Statistikansicht</span>
    </div>
  </div>
  <div class="agenda-item">
    <div class="agenda-num">06</div>
    <div class="agenda-text">
      <strong>Risiken & nächste Schritte</strong>
      <span>Was bis Sprint 2 passieren muss</span>
    </div>
  </div>
</div>

---

# Ausgangslage & Ziel

<div class="columns">
<div class="col" style="flex: 1.15;">

### Problem
* Generative KI **erfindet Quellen** oder liefert falsche Titel, Autor:innen, Venues, Jahre und DOIs.
* Diese Angaben von Hand zu prüfen kostet viel Zeit.

### Ziel
* Einen **lokal betriebenen, datenschutzkonformen** Prototyp aus einer Bachelorarbeit weiterentwickeln.
* Qualität und Laufzeit **reproduzierbar** am CiteAudit-Benchmark messen.

</div>
<div class="col" style="flex: 0.85;">
<div class="card accent">

### Im Scope
<ul class="scope-in">
<li>Existiert die Quelle?</li>
<li>Stimmen die bibliografischen Angaben?</li>
</ul>

</div>
<div class="card slate">

### Nicht im Scope
<ul class="scope-out">
<li>Belegt die Quelle die Aussage im Text?</li>
</ul>

</div>
</div>
</div>

---

# System: Datenfluss

<div class="figure">

![w:1140](assets/citation-pipeline.svg)

</div>

<div class="columns" style="margin-top: 14px;">
<div class="col">

* **Lokale Inferenz** auf DHBW-Infrastruktur (RTX 6000, DGX Spark)
* **Keine Datenleckage:** Die Ground Truth gelangt nie in Prompt oder Worker.

</div>
<div class="col">

* **Drei Agenten im Vergleich:** Browser-use als Baseline, dazu Hermes und OpenCode.
* Läufe lassen sich pausieren und fortsetzen, mit **600 s Hard-Timeout** je Zitat.

</div>
</div>

---

# Benchmark: CiteAudit

<div class="columns" style="align-items: center;">
<div class="col kpi-stack" style="flex: 0.6;">

<div class="kpi-card">
  <div class="number">9.442</div>
  <div class="label">gelabelte Zitate</div>
  <div class="sub">Shi et al., binäres Label Real / Fake</div>
</div>

<div class="kpi-card">
  <div class="number">31,4 %</div>
  <div class="label">Fake-Anteil gesamt</div>
  <div class="sub">2.967 von 9.442 Zitaten</div>
</div>

<div class="kpi-card">
  <div class="number">2 Gruppen</div>
  <div class="label">realworld und generated</div>
  <div class="sub">getrennt auswerten</div>
</div>

</div>
<div class="col" style="flex: 1.4;">

![w:700](assets/citeaudit-distribution.svg)

> Der Fake-Anteil unterscheidet sich je Gruppe um fast das Dreifache. Eine einzige Gesamt-Accuracy würde Schwächen bei **realworld** verdecken.

</div>
</div>

---

# Bewertung: vier Status, zwei Klassen

<div class="columns">
<div class="col" style="flex: 1.2;">

| Status | Bedeutung | Binär |
| :--- | :--- | :--- |
| **1** | bibliografisch korrekt | Real |
| **2** | nur Formfehler | Real |
| **3** | Inhaltsfehler, z. B. falsche Autor:innen | Fake |
| **4** | nicht verifizierbar | Fake |

* **Fake** ist die positive Klasse: Accuracy, Precision, Recall und F1 je `source_type`.
* Status 4 heißt **„nicht gefunden“**, nicht „bewiesen falsch“. Timeouts zählen getrennt.

</div>
<div class="col" style="flex: 0.8;">

### Datensätze

| Stufe | Zitate | Zweck |
| :--- | ---: | :--- |
| Techniktest | 1 | Setup |
| Test | 10 | Entwicklung |
| Evaluation | 50 | Vergleich |
| CiteAudit | 9.442 | Benchmark |

</div>
</div>

---

# Projektstand: Kanban-Board

<div class="board">
<div class="board-col">
<div class="board-head">To Do <span>4</span></div>
<div class="board-card crit"><b>CE-32 <span class="prio">· Kritisch</span></b>Reverse Proxy: Zugriff per WebUI statt SSH</div>
<div class="board-card high"><b>CE-34 <span class="prio" style="color:#8E130A">· Hoch</span></b>WebUI mit Login absichern</div>
<div class="board-card"><b>CE-22 <span class="who">Finn</span></b>RTX 6000 für parallele Samples</div>
<div class="board-card"><b>CE-29</b>Kapazitätsstatus der Modellserver</div>
</div>
<div class="board-col">
<div class="board-head">In Arbeit <span>4</span></div>
<div class="board-card"><b>CE-23</b>Tests mit neuer Kategoriendefinition</div>
<div class="board-card"><b>CE-25</b>Effizientere Judgement Calls, parallele Worker</div>
<div class="board-card"><b>CE-26 <span class="who">Tino</span></b>Ergebnis-UI verbessern</div>
<div class="board-card"><b>CE-24 <span class="who">Finn</span></b>Präsentation mit Marp</div>
</div>
<div class="board-col">
<div class="board-head">Erledigt <span>1</span></div>
<div class="board-card done"><b>CE-21 <span class="who">Tino</span></b>Rechenleistung bei Prof. Schilling angefragt</div>
</div>
<div class="board-col">
<div class="board-head">Backlog <span>4</span></div>
<div class="board-card"><b>CE-30</b>DSGVO und deutsches Recht</div>
<div class="board-card"><b>CE-31</b>Statistische Tests vervollständigen</div>
<div class="board-card"><b>CE-33</b>CLI auf WebUI-Stand bringen</div>
<div class="board-card"><b>CE-28</b>Multi-User-Zugriff</div>
</div>
</div>

> **Schwerpunkt:** Der Zugang wechselt von SSH zu einer abgesicherten WebUI. Erst dann können mehrere Personen gleichzeitig Läufe starten.

---

# Laufzeit: warum wir stufenweise skalieren

<div class="kpi-grid">
  <div class="kpi-card">
    <div class="number">~147 s</div>
    <div class="label">pro Zitat</div>
    <div class="sub">GPT-OSS-120B mit Browser-use (Bachelorarbeit)</div>
  </div>
  <div class="kpi-card">
    <div class="number">~16 Tage</div>
    <div class="label">für 9.442 Zitate</div>
    <div class="sub">bei rein sequentieller Ausführung</div>
  </div>
  <div class="kpi-card">
    <div class="number">94 %</div>
    <div class="label">Statusgenauigkeit (4 Stufen)</div>
    <div class="sub">Vortest mit ca. 900 Quellen, nicht repräsentativ</div>
  </div>
</div>

<div class="steps">
  <div class="step-item active">
    <div class="step-num">Stufe 1 · 50</div>
    <div class="step-title">Smoke-Test</div>
    <div class="step-desc">Setup, Datenformat, GT-Trennung und Parser prüfen</div>
  </div>
  <div class="step-item active">
    <div class="step-num">Stufe 2 · 500</div>
    <div class="step-title">Pilot</div>
    <div class="step-desc">Resume, Timeouts, Logs und Metriken prüfen</div>
  </div>
  <div class="step-item">
    <div class="step-num">Stufe 3 · 5.000</div>
    <div class="step-title">Skalierung</div>
    <div class="step-desc">Parallele Worker messen, Konfiguration einfrieren</div>
  </div>
  <div class="step-item">
    <div class="step-num">Stufe 4 · 9.442</div>
    <div class="step-title">Vollständig</div>
    <div class="step-desc">Nur wenn die Teilläufe valide sind</div>
  </div>
</div>

---

# Ergebnis: Stichprobe von 200 Zitaten (v7)

<span class="tag slate">qwen-rtx6000 · Browser-use · Seed 20260911 · 13.10.2026</span>

<div class="columns" style="align-items: center; margin-top: 4px;">
<div class="col kpi-stack" style="flex: 0.6;">

<div class="kpi-card">
  <div class="number">166 / 200</div>
  <div class="label">gültige Urteile</div>
  <div class="sub">34 technische Ausfälle, v. a. Worker</div>
</div>

<div class="kpi-card">
  <div class="number">98 %</div>
  <div class="label">Recall für Fake</div>
  <div class="sub">55 von 56 Fakes erkannt</div>
</div>

<div class="kpi-card">
  <div class="number">57 %</div>
  <div class="label">Precision für Fake</div>
  <div class="sub">42 echte Zitate fälschlich markiert</div>
</div>

</div>
<div class="col" style="flex: 1.4;">

![w:640](assets/v7-confusion.svg)

</div>
</div>

> Fast keine Fakes entgehen dem Agenten, aber er markiert zu viel – vor allem bei **realworld**. Accuracy gesamt: **74 %**.

---

# Neue Kategoriendefinition (v7)

<div class="columns">
<div class="col" style="flex: 1.05;">

### Prüffrage
Verschwindet die Abweichung, wenn Groß-/Kleinschreibung, Leerzeichen, Interpunktion, Bindestriche und Zitierstil ignoriert werden?

<div class="columns" style="gap: 14px; margin-top: 4px;">
<div class="card slate" style="flex: 1;">

**Ja → Formfehler → Status 2**

</div>
<div class="card accent" style="flex: 1;">

**Nein → Inhaltsfehler → Status 3**

</div>
</div>

* Der **schwerste** Fehler bestimmt den Status, nicht die Anzahl.
* Ab v7 hat kein Status-2-Fall mehr `GT = false`. Die Grenze passt damit zum binären Mapping.

</div>
<div class="col" style="flex: 0.95;">

| Abweichung | Status |
| :--- | :---: |
| Titel in anderer Groß-/Kleinschreibung | 2 |
| Leerzeichen in URL/DOI, gleiches Ziel | 2 |
| Überflüssiges „et al.“ | 2 |
| Autorname falsch, auch ein Buchstabe | 3 |
| Falsche Autorenreihenfolge | 3 |
| Autor:innen fehlen oder hinzugefügt | 3 |
| Falsches Jahr, Venue, Band, Seiten | 3 |
| URL/DOI eines anderen Werks | 3 |

</div>
</div>

---

# Vergleich: Modelle und Agenten

<span class="tag red">Platzhalter</span>

| Modell | Agent | Accuracy | F1 (Fake) | Techn. Fehler | Ø Dauer |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **[Modell A]** | Browser-use | [xx %] | [0,xx] | [x %] | [xx s] |
| | Hermes | [xx %] | [0,xx] | [x %] | [xx s] |
| | OpenCode | [xx %] | [0,xx] | [x %] | [xx s] |
| **[Modell B]** | Browser-use | [xx %] | [0,xx] | [x %] | [xx s] |
| | Hermes | [xx %] | [0,xx] | [x %] | [xx s] |
| | OpenCode | [xx %] | [0,xx] | [x %] | [xx s] |

> **Kernaussage:** [Welche Kombination schneidet am besten ab, und um wie viel?]

---

# Vergleich: Definition v6 → v7

<div class="columns" style="align-items: center;">
<div class="col" style="flex: 0.9;">

| Kennzahl | v6 | v7 |
| :--- | ---: | ---: |
| Gültige Urteile | 241 | 166 |
| Accuracy | 83 % | 74 % |
| Recall (Fake) | 94 % | **98 %** |
| Precision (Fake) | **63 %** | 57 % |
| F1 (Fake) | **0,75** | 0,72 |
| Fakes in Status 2 | 4 | **0** |

<p class="caption">v6: gpt-oss-spark, erste 241 Zitate · v7: qwen-rtx6000, Zufallsstichprobe</p>

</div>
<div class="col" style="flex: 1.1;">

![w:600](assets/v6-v7-status.svg)

</div>
</div>

> **Status 2 ist jetzt sauber**, aber Status 3 und 4 fangen mehr echte Zitate ein. Modell und Stichprobe unterscheiden sich, daher ist das **noch kein fairer A/B-Test**. Nächster Lauf: v7 mit gpt-oss auf derselben Stichprobe.

---

# Ergebnis-UI: Statistikansicht

<div class="columns" style="align-items: stretch;">
<div class="col" style="flex: 0.8;">

### Was neu ist
* Getrennte Ansichten **Lauf** und **Statistik**
* **Boxplots** für Warte- und Ausführungszeit je Konfiguration
* Wählbares **Konfidenzniveau** (90, 95 oder 99 %)
* **Worker-Steuerung** für parallele Versuche
* Designs: Hell, Dunkel, Pink Glass

</div>
<div class="col" style="flex: 1.2;">

<div class="placeholder" style="height: 100%;">
  <strong>Screenshot: Statistikansicht</strong>
  Bild in assets/ ablegen
</div>

</div>
</div>

---

# Risiken

| Risiko | Auswirkung | Gegenmaßnahme |
| :--- | :--- | :--- |
| **Unscharfe Grenze Status 2/3** | Urteile schwanken, Vergleich mit CiteAudit unfair | Beispiele und Mapping mit dem Betreuer abstimmen |
| **Langer Lauf bricht ab** | Tage an Rechenzeit verloren | Stufenplan, Timeout, Resume und Checkpoints |
| **Bot-Erkennung, Rate-Limits** | fehlende Belege, Abbrüche | Fehler loggen, Backoff, klein testen |
| **Ungleiche Klassen** | Gesamt-Accuracy verdeckt Schwächen | Metriken je `source_type` berichten |
| **Lizenz des Datensatzes unklar** | Veröffentlichung nicht zulässig | Lizenz vor jeder Weitergabe klären |

---

# Nächste Schritte

<div class="steps">
  <div class="step-item active">
    <div class="step-num">Schritt 1</div>
    <div class="step-title">Zugriff</div>
    <div class="step-desc">Reverse Proxy einrichten, WebUI mit Login freigeben (CE-32, CE-34)</div>
  </div>
  <div class="step-item">
    <div class="step-num">Schritt 2</div>
    <div class="step-title">Rechenleistung</div>
    <div class="step-desc">RTX 6000 für parallele Samples, Kapazitätsstatus sichtbar machen (CE-22, CE-29)</div>
  </div>
  <div class="step-item">
    <div class="step-num">Schritt 3</div>
    <div class="step-title">Auswertung</div>
    <div class="step-desc">Statistische Tests vervollständigen, CLI ausbauen (CE-31, CE-33)</div>
  </div>
</div>

> **Noch offen:** Status-Mapping mit dem Betreuer verbindlich festlegen. DSGVO (CE-30) und Multi-User-Zugriff (CE-28) liegen im Backlog.

---

<!-- _class: end -->
<!-- _paginate: false -->

# Vielen Dank!
## Fragen & Diskussion

<div class="end-grid">
<div class="end-card">

<strong>Team</strong>
Finn Hertsch · Tino Strasser · Maximilian Vogt · Florian Dittmann

</div>
<div class="end-card">

<strong>Projekt</strong>
Product Owner: Prof. Dr. Andreas Schilling  
Repo: github.com/FlorianDitt/citation-evaluation

</div>
</div>
