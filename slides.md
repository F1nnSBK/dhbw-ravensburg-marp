---
marp: true
theme: dhbw
paginate: true
header: "DHBW Ravensburg"
footer: "Citation Evaluation | Projektstand | 2026"
---

<style>
.board {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
  margin-top: 8px;
  align-items: start;
}
.board-col {
  background: #F8F9FA;
  border: 1px solid #E2E6E9;
  border-radius: 8px;
  padding: 8px;
}
.board-head {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: #5C6971;
  margin-bottom: 6px;
}
.board-card {
  background: #FFFFFF;
  border: 1px solid #E2E6E9;
  border-left: 4px solid #5C6971;
  border-radius: 6px;
  padding: 6px 8px;
  font-size: 13px;
  line-height: 1.3;
  margin-bottom: 6px;
}
.board-card b {
  display: block;
  font-size: 11px;
  color: #5C6971;
}
.board-card small {
  display: block;
  font-size: 11px;
  color: #5C6971;
}
.board-card.crit { border-left-color: #E2001A; }
.board-card.crit small { color: #E2001A; font-weight: 700; }
.board-card.high { border-left-color: #8E130A; }
.board-card.high small { color: #8E130A; font-weight: 700; }
.board-card.done { color: #5C6971; text-decoration: line-through; }
.board-empty {
  font-size: 12px;
  color: #5C6971;
  text-align: center;
  padding: 10px 0;
}
.placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  border: 2px dashed #BBC3C8;
  border-radius: 8px;
  background: #F8F9FA;
  color: #5C6971;
  font-size: 15px;
  line-height: 1.4;
  padding: 12px;
  box-sizing: border-box;
}
.placeholder strong {
  font-size: 17px;
  color: #5C6971;
}
</style>

<!-- _class: title -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Citation Evaluation
## Projektstand, Kanban-Board und erste Ergebnisse

<div class="title-meta-grid">
<div class="title-meta-col">

**Team:** [Namen ergänzen]  
**Studiengang:** [Studiengang ergänzen]  
**Kurs:** [Kurs ergänzen]

</div>
<div class="title-meta-col">

**Projekt:** Literaturangaben mit KI-Agenten prüfen  
**Betreuer:** [Betreuer ergänzen]  
**Datum:** [Datum ergänzen]

</div>
</div>

---

# Agenda

<div class="agenda-grid">
  <div class="agenda-item">
    <div class="agenda-num">01</div>
    <div class="agenda-text">
      <strong>Projekt in Kürze</strong>
      <span>Was geprüft wird und mit welchen Datensätzen</span>
    </div>
  </div>

  <div class="agenda-item">
    <div class="agenda-num">02</div>
    <div class="agenda-text">
      <strong>Kanban-Board</strong>
      <span>Arbeitsstand, laufende Aufgaben und Backlog</span>
    </div>
  </div>

  <div class="agenda-item">
    <div class="agenda-num">03</div>
    <div class="agenda-text">
      <strong>Lauf mit dem großen Datensatz</strong>
      <span>CiteAudit-Benchmark mit binärer Bewertung</span>
    </div>
  </div>

  <div class="agenda-item">
    <div class="agenda-num">04</div>
    <div class="agenda-text">
      <strong>Vergleiche</strong>
      <span>Modelle, Agenten, Kategoriendefinition und Laufzeit</span>
    </div>
  </div>

  <div class="agenda-item">
    <div class="agenda-num">05</div>
    <div class="agenda-text">
      <strong>Verbesserte Ergebnis-UI</strong>
      <span>Lauf- und Statistikansicht</span>
    </div>
  </div>

  <div class="agenda-item">
    <div class="agenda-num">06</div>
    <div class="agenda-text">
      <strong>Nächste Schritte</strong>
      <span>Zugriff, Rechenleistung und Auswertung</span>
    </div>
  </div>
</div>

---

# 1. Projekt in Kürze

<div class="columns">
<div class="col">

### Was das System macht
* Prüft **Literaturangaben** automatisiert auf Existenz und Zitierfehler.
* Vergleicht Modellantworten über drei Agenten: **Browser-use**, **Hermes** und **OpenCode**.
* Bewertet jede Antwort gegen eine **Musterlösung**.

### Fachlicher Status je Zitat
* **1** korrekt · **2** nur Formfehler
* **3** Inhaltsfehler · **4** nicht verifizierbar

</div>
<div class="col">

### Datensätze

| Datensatz | Umfang | Zweck |
| :--- | :--- | :--- |
| **Techniktest** | 1 Zitat | Einrichtung prüfen |
| **Test** | 10 Zitate | Entwicklung |
| **Evaluation** | 50 Zitate | Abschließender Vergleich |
| **Benchmark** | 9.442 Zitate | CiteAudit, binär bewertet |

</div>
</div>

---

<!-- _class: chapter -->
<!-- _header: "" -->
<!-- _footer: "" -->

<div class="chapter-num">KAPITEL 02</div>

# 2. Kanban-Board
## Wo das Projekt gerade steht

13 Karten: vier in Arbeit, vier als Nächstes eingeplant, vier im Backlog und eine erledigt.

---

# 2. Kanban-Board im Überblick

<div class="board">
<div class="board-col">
<div class="board-head">To Do <span>4</span></div>
<div class="board-card"><b>CE-22</b>RTX 6000 für parallele Samples aufsetzen<small>Finn</small></div>
<div class="board-card"><b>CE-29</b>Rein lesender Kapazitätsstatus für Modellserver, Modelle und Instanzen</div>
<div class="board-card crit"><b>CE-32</b>Reverse Proxy und gleichzeitiger Zugriff via WebUI statt SSH<small>Kritisch</small></div>
<div class="board-card high"><b>CE-34</b>WebUI unabhängig von SSH mit Login absichern und freigeben<small>Hoch</small></div>
</div>
<div class="board-col">
<div class="board-head">In Bearbeitung <span>4</span></div>
<div class="board-card"><b>CE-26</b>UI verbessern<small>Tino</small></div>
<div class="board-card"><b>CE-25</b>Effizienz der Judgement Calls und parallele Worker</div>
<div class="board-card"><b>CE-24</b>Präsentation mit Marp aufsetzen<small>Finn</small></div>
<div class="board-card"><b>CE-23</b>Tests mit anderer Kategoriendefinition</div>
</div>
<div class="board-col">
<div class="board-head">In Review <span>0</span></div>
<div class="board-empty">keine Karten</div>
</div>
<div class="board-col">
<div class="board-head">Erledigt <span>1</span></div>
<div class="board-card done"><b>CE-21</b>E-Mail an Schilling: Rechenleistung<small>Tino</small></div>
</div>
<div class="board-col">
<div class="board-head">Backlog <span>4</span></div>
<div class="board-card"><b>CE-28</b>Erweiterung für Multi-User Access<small>Niedrig</small></div>
<div class="board-card"><b>CE-30</b>DSGVO und deutsches Recht</div>
<div class="board-card"><b>CE-31</b>Statistische Tests erweitern und vervollständigen</div>
<div class="board-card"><b>CE-33</b>CLI ausbauen, bis sie die meisten WebUI-Funktionen abdeckt</div>
</div>
</div>

---

# 2. In Bearbeitung

<div class="columns" style="margin-bottom: 0;">
<div class="col">
<div class="card accent">

### CE-23 · Andere Kategoriendefinition
* Grenze zwischen Status 2 und 3 neu gefasst: **Formfehler** gegen **Inhaltsfehler**.
* Neue Prompt-Version `citation-core-v7`, zwei Fälle neu eingestuft.

</div>
<div class="card slate">

### CE-25 · Judgement Calls & Worker
* Bewertungsaufrufe effizienter machen.
* Mehrere Worker parallel auslasten.

</div>
</div>
<div class="col">
<div class="card accent">

### CE-26 · UI verbessern
* Worker-Steuerung, Designs und eine klarere Statistikansicht.
* Zuständig: Tino.

</div>
<div class="card slate">

### CE-24 · Präsentation mit Marp
* DHBW-Vorlage als Grundlage für diese Folien.
* Zuständig: Finn.

</div>
</div>
</div>

---

# 2. Als Nächstes und Backlog

<div class="columns">
<div class="col">

### To Do
* <span class="tag red">Kritisch</span> **CE-32** Reverse Proxy, gleichzeitiger Zugriff via WebUI statt SSH
* <span class="tag red">Hoch</span> **CE-34** WebUI mit Login absichern und freigeben
* **CE-22** RTX 6000 für parallele Samples aufsetzen
* **CE-29** Rein lesender Kapazitätsstatus für Modellserver

</div>
<div class="col">

### Backlog
* **CE-30** DSGVO und deutsches Recht
* **CE-31** Statistische Tests erweitern
* **CE-33** CLI auf den Stand der WebUI bringen
* <span class="tag slate">Niedrig</span> **CE-28** Multi-User Access

</div>
</div>

> **Schwerpunkt:** Der Zugriff soll von SSH auf eine abgesicherte WebUI wechseln. Das ist die Voraussetzung dafür, dass mehrere Personen gleichzeitig Läufe starten können.

---

<!-- _class: chapter -->
<!-- _header: "" -->
<!-- _footer: "" -->

<div class="chapter-num">KAPITEL 03</div>

# 3. Ergebnisse
## Großer Lauf und Vergleiche

Die Zahlen und Diagramme auf den folgenden Folien sind Platzhalter und werden nach den Läufen eingesetzt.

---

# 3. Lauf mit dem großen Datensatz

<span class="tag red">Platzhalter</span>

<div class="columns" style="align-items: center; margin-top: 0;">
<div class="col" style="flex: 0.85;">

<div class="kpi-card" style="margin-bottom: 10px;">
  <div class="number">[n]</div>
  <div class="label">Ausgewertete Zitate</div>
  <div class="sub">von 9.442 im CiteAudit-Benchmark</div>
</div>

<div class="kpi-card" style="margin-bottom: 10px;">
  <div class="number">[xx %]</div>
  <div class="label">Fehlererkennungsgenauigkeit</div>
  <div class="sub">binäre Bewertung, [Modell] mit [Agent]</div>
</div>

<div class="kpi-card">
  <div class="number">[x %]</div>
  <div class="label">Technische Fehlerquote</div>
  <div class="sub">Timeouts und ungültige Antworten</div>
</div>

</div>
<div class="col" style="flex: 1.15;">

<div class="placeholder" style="height: 400px;">
  <strong>Diagramm: Ergebnis des großen Laufs</strong>
  z. B. richtig und falsch erkannte Zitate je Label<br>
  als SVG unter assets/ ablegen
</div>

</div>
</div>

---

# 3. Vergleich: Modelle und Agenten

<span class="tag red">Platzhalter</span>

| Modell | Agent | Statusgenauigkeit | Makro-F1 | Techn. Fehlerquote | Ø Dauer |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Modell A]** | Browser-use | [xx %] | [0,xx] | [x %] | [xx s] |
| **[Modell A]** | Hermes | [xx %] | [0,xx] | [x %] | [xx s] |
| **[Modell A]** | OpenCode | [xx %] | [0,xx] | [x %] | [xx s] |
| **[Modell B]** | Browser-use | [xx %] | [0,xx] | [x %] | [xx s] |
| **[Modell B]** | Hermes | [xx %] | [0,xx] | [x %] | [xx s] |
| **[Modell B]** | OpenCode | [xx %] | [0,xx] | [x %] | [xx s] |

> **Kernaussage:** [Welche Kombination aus Modell und Agent schneidet am besten ab, und um wie viel?]

---

# 3. Vergleich: Kategoriendefinition

<span class="tag red">Platzhalter</span>

<div class="columns" style="align-items: center; margin-top: 0;">
<div class="col">

### Alte gegen neue Definition (CE-23)

| Kennzahl | v6 | v7 |
| :--- | :--- | :--- |
| **Statusgenauigkeit** | [xx %] | [xx %] |
| **Makro-F1** | [0,xx] | [0,xx] |
| **Verwechslung 2 ↔ 3** | [n] | [n] |

* **v6:** bisherige Prompt-Definition
* **v7:** Formfehler ergibt Status 2, Inhaltsfehler Status 3

</div>
<div class="col">

<div class="placeholder" style="height: 380px;">
  <strong>Diagramm: Status 1 bis 4 je Definition</strong>
  z. B. Trefferquote je Statusklasse, v6 neben v7<br>
  als SVG unter assets/ ablegen
</div>

</div>
</div>

---

# 3. Vergleich: Laufzeit und Parallelität

<span class="tag red">Platzhalter</span>

<div class="columns" style="align-items: center; margin-top: 0;">
<div class="col" style="flex: 0.85;">

<div class="kpi-card" style="margin-bottom: 10px;">
  <div class="number">[xx s]</div>
  <div class="label">Ø Dauer je Zitat</div>
  <div class="sub">ein Worker, sequentiell</div>
</div>

<div class="kpi-card" style="margin-bottom: 10px;">
  <div class="number">[xx s]</div>
  <div class="label">Ø Dauer je Zitat</div>
  <div class="sub">[n] parallele Worker</div>
</div>

<div class="kpi-card">
  <div class="number">[x,x×]</div>
  <div class="label">Beschleunigung</div>
  <div class="sub">Gesamtlaufzeit im Vergleich</div>
</div>

</div>
<div class="col" style="flex: 1.15;">

<div class="placeholder" style="height: 400px;">
  <strong>Diagramm: Laufzeit je Konfiguration</strong>
  z. B. Boxplots der Ausführungszeit je Worker-Anzahl<br>
  als SVG unter assets/ ablegen
</div>

</div>
</div>

---

<!-- _class: chapter -->
<!-- _header: "" -->
<!-- _footer: "" -->

<div class="chapter-num">KAPITEL 04</div>

# 4. Verbesserte Ergebnis-UI
## Vom Einzelergebnis zur Statistikansicht

Die Oberfläche zeigt Läufe und ihre Auswertung jetzt in zwei getrennten Ansichten.

---

# 4. Ergebnis-UI: vorher und nachher

<span class="tag red">Platzhalter</span>

<div class="columns" style="margin-top: 0;">
<div class="col">

### Vorher

<div class="placeholder" style="height: 340px;">
  <strong>Screenshot: bisherige Ergebnisansicht</strong>
  Bild unter assets/ ablegen
</div>

</div>
<div class="col">

### Nachher

<div class="placeholder" style="height: 340px;">
  <strong>Screenshot: neue Ergebnisansicht</strong>
  Bild unter assets/ ablegen
</div>

</div>
</div>

---

# 4. Ergebnis-UI: Statistikansicht

<div class="columns" style="align-items: center;">
<div class="col" style="flex: 0.8;">

### Was neu ist
* Getrennte Ansichten **Lauf** und **Statistik**
* **Boxplots** für Warte- und Ausführungszeit je Konfiguration
* Wählbares **Konfidenzniveau**: 90, 95 oder 99 Prozent
* **Worker-Steuerung** für parallele Versuche
* Designs: Hell, Dunkel und Pink Glass

</div>
<div class="col" style="flex: 1.2;">

<div class="placeholder" style="height: 400px;">
  <strong>Screenshot: Statistikansicht</strong>
  Bild unter assets/ ablegen
</div>

</div>
</div>

---

# 5. Nächste Schritte

<span class="tag slate">Aus dem Kanban-Board</span>

<div class="steps">
  <div class="step-item active">
    <div class="step-num">Schritt 1</div>
    <div class="step-title">Zugriff</div>
    <div class="step-desc">Reverse Proxy einrichten und die WebUI mit Login freigeben (CE-32, CE-34).</div>
  </div>
  <div class="step-item">
    <div class="step-num">Schritt 2</div>
    <div class="step-title">Rechenleistung</div>
    <div class="step-desc">RTX 6000 für parallele Samples aufsetzen und den Kapazitätsstatus sichtbar machen (CE-22, CE-29).</div>
  </div>
  <div class="step-item">
    <div class="step-num">Schritt 3</div>
    <div class="step-title">Auswertung</div>
    <div class="step-desc">Statistische Tests vervollständigen und die CLI ausbauen (CE-31, CE-33).</div>
  </div>
</div>

> **Offen:** DSGVO und deutsches Recht (CE-30) sowie Multi-User Access (CE-28) liegen im Backlog und sind noch nicht eingeplant.

---

<!-- _class: end -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Vielen Dank für Ihre Aufmerksamkeit!
## Fragen & Diskussion

<div class="end-grid">
<div class="end-card">

<strong>Duale Hochschule Baden-Württemberg Ravensburg</strong>  
* **Campus Ravensburg:** Marienplatz 2, 88212 Ravensburg  
* **Campus Friedrichshafen:** Fallenbrunnen 2, 88045 Friedrichshafen  
* **Web:** [www.ravensburg.dhbw.de](https://www.ravensburg.dhbw.de)

</div>
<div class="end-card">

<strong>Projekt &amp; Kontakt</strong>  
* **Team:** [Namen ergänzen]  
* **E-Mail:** [Kontakt ergänzen]  
* **Projekt-Repo:** github.com/FlorianDitt/citation-evaluation

</div>
</div>
