# AGENTS.md – Leitfaden für KI-Coding-Assistenten (DHBW Ravensburg Marp)

Dieser Leitfaden ist verbindlich für alle KI-Agenten (Antigravity, Cursor, GitHub Copilot etc.), die in diesem Repository arbeiten.

---

## 📌 1. Projekt-Überblick & Architektur

* **Repository:** DHBW Ravensburg Marp Presentation Template.
* **Technologie:** [Marp](https://marp.app/) (Markdown Presentation Ecosystem) mit `@marp-team/marp-cli`.
* **Standard-Format:** 16:9 Bildformat (`1280px` x `720px`).
* **Theme:** [themes/dhbw.css](file:///Users/finnhertsch/projects/dhbw-ravensburg-marp/themes/dhbw.css) (Eigenständiges DHBW Corporate Design Theme).

---

## 🌿 2. Git-Branching-Workflow (STRIKT EINHALTEN)

1. **`main`-Branch:**
   * Ist das **reine Template**. Hier liegen ausschließlich Theme-Dateien, Basis-Assets, Konfigurationen und die Vorlage [slides.md](file:///Users/finnhertsch/projects/dhbw-ravensburg-marp/slides.md).
   * **Niemals** themenspezifische Inhalte direkt auf `main` committen.

2. **Präsentations-Branches (`presentation/<name>`):**
   * Jede konkrete Arbeit (z. B. Praxisarbeit T2000, Bachelorarbeit, Seminarvortrag) muss in einem eigenen Branch liegen:
     ```bash
     npm run new <themen-name>
     # oder manuell:
     git checkout main
     git checkout -b presentation/<themen-name>
     ```
   * Folieninhalte werden in `slides.md` im jeweiligen Branch angepasst und versioniert.

---

## 🎨 3. Corporate Design & Layout-Regeln

### Farbpalette
* **DHBW Rot:** `#E2001A` (Akzente, Bullet Points, Links, Kennzahlen)
* **DHBW Weinrot / Dunkelrot:** `#8E130A` (Mittlere Bannerlinie, Code-Elemente)
* **DHBW Schiefergrau:** `#5C6971` (Tabellenköpfe, Untertitel, Kapitel-Hintergrund)
* **Dunkler Text:** `#22252A` (Hauptüberschriften, Fließtext)
* **Hellgrau:** `#F8F9FA` (Kartenhintergründe, Callouts)
* **Rahmenfarbe:** `#E2E6E9` (Trennlinien, Rahmen)

### ⚠️ WICHTIG: Vermeidung von vertikalem Content-Overflow
* Jede Folie hat eine Gesamthöhe von exakt **`720px`**.
* Die sichere Inhaltszone liegt zwischen `top: 86px` (unter der Kopfzeile) und `bottom: 62px` (über der Fußzeile) $\rightarrow$ **maximal 572px Inhalts-Höhe**.
* **Keinesfalls** dürfen Folieninhalte in die Fußzeile oder über die Ränder laufen.
* **Regel für komplexe Inhalte:** Wenn Kennzahlen (KPIs) **und** ein Diagramm auf einer Folie dargestellt werden, **immer** ein 2-Spalten-Layout (`<div class="columns">`) nutzen, niemals vertikal stapeln!

---

## 📊 4. Wissenschaftliche Grafiken & Diagramme

1. **Format:** Plots und Diagramme müssen **immer als SVG** erstellt werden (niemals als PNG oder JPEG).
2. **Stil:** Immer wissenschaftlich im minimalistischen **Edward Tufte-Stil** (hohe Data-to-Ink-Ratio, keine überflüssigen Gitternetze oder Verzierungen).
3. **Schriftarten:** Keine LaTeX-Befehle (kein `\textbf` o. ä.) und keine überladenen Annotationen innerhalb der SVGs.
4. **Chat-Ausgaben:** Schreibe keinen LaTeX-Code in den Chat-Ausgaben.

---

## 🧩 5. Vordefinierte Folienklassen & Komponenten

* **Titelfolie:** `<!-- _class: title -->` mit `<div class="title-meta-grid">`
* **Agenda:** `<div class="agenda-grid">` mit `<div class="agenda-item">` und nummerierten Badges
* **Phasen / Vorgehensmodell:** `<div class="steps">` mit `<div class="step-item">`
* **Vergleich:** `<div class="columns">` mit `<div class="card slate">` und `<div class="card accent">`
* **Zwischentitel:** `<!-- _class: chapter -->` mit `<div class="chapter-num">`
* **KPIs:** `<div class="kpi-grid">` mit `<div class="kpi-card">`
* **Abschluss / Q&A:** `<!-- _class: end -->` mit `<div class="end-grid">`
* **Dark Mode:** `<!-- _class: invert -->` (nutzt automatisch das freigestellte weiße Logo)

---

## 🛠️ 6. Befehle & Toolchain

```bash
# Neuen Präsentations-Branch erstellen
npm run new <name>

# Live-Server mit Auto-Reload starten (Port 8080)
npm start

# Standalone-Builds erzeugen
npm run build:all   # Baut HTML, PDF und PPTX in dist/

# Python-Skripte (falls nötig)
# IMMER das virtuelle Environment nutzen:
.venv/bin/python <script.py>
```
