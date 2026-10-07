# DHBW Ravensburg – Marp Präsentations-Template 🎓

Ein modernes, leichtgewichtiges und CI-konformes Präsentations-Template für die **Duale Hochschule Baden-Württemberg (DHBW) Ravensburg**, basierend auf [Marp](https://marp.app/) (Markdown Presentation Ecosystem).

---

## 🌟 Highlights

* **100% Corporate Design der DHBW Ravensburg:** Originalfarben (`#E2001A`, `#8E130A`, `#5C6971`), Original-Logo als SVG und die charakteristische 3-Farben-Abschlussleiste.
* **Wissenschaftliche & moderne Layouts:** Titelfolie, Gliederung, 2-Spalten-Vergleich, Zwischentitel, KPI-Kennzahlenkarten, saubere Tabellen im Tufte-Stil, Code-Blöcke und Q&A-Abschluss.
* **Multi-Format Export:** Generierung von **HTML**, **PDF** und **PowerPoint (PPTX)** mit einem einzigen Befehl.
* **Live-Reload Dev-Server:** Schnelles Schreiben mit sofortiger Aktualisierung im Browser.
* **Zero-Config VS Code Support:** Vorkonfiguriert für die offizielle VS Code Erweiterung `marp-team.marp-vscode`.

---

## 📁 Repository-Struktur

```text
├── assets/
│   ├── dhbw-ravensburg-logo.svg   # Kombiniertes DHBW Ravensburg Vektor-Logo
│   ├── dhbw-logo.jpg              # Original DHBW Bildmarke
│   ├── ravensburg-text.jpg        # Original Ravensburg Schriftzug
│   ├── dhbw-banner-bottom.png     # Offizieller 3-Streifen-Banner (Unten)
│   ├── dhbw-accent-bar.png        # Roter Akzentstreifen
│   └── reference/
│       └── DHBW_RV_PPT-Template_16_9.pptx  # Original PowerPoint-Vorlage als Referenz
├── themes/
│   └── dhbw.css                   # Eigenständiges Marp-Theme (DHBW Ravensburg)
├── .vscode/
│   ├── settings.json              # VS Code Pfad zum DHBW-Theme & HTML-Aktivierung
│   └── extensions.json            # Empfohlene Erweiterung (marp-vscode)
├── dist/                          # Generierte Ausgabedateien (HTML, PDF, PPTX)
├── marp.config.mjs                # Marp CLI Konfiguration
├── package.json                   # Build- und Dev-Skripte
├── slides.md                      # 10-Folien-Musterpräsentation
└── README.md                      # Dokumentation & Git-Workflow
```

---

## 🚀 Schnelleinstieg

### Voraussetzungen
* [Node.js](https://nodejs.org/) (Version 18 oder neuer)

### 1. Abhängigkeiten installieren
```bash
npm install
```

### 2. Live-Vorschau starten (Dev-Server)
Startet einen lokalen Server mit automatischem Neuladen bei jeder Dateiänderung:
```bash
npm start
# Öffnet http://localhost:8080 im Browser
```

Alternativ Vorschau-Fenster öffnen:
```bash
npm run preview
```

### 3. Präsentation bauen / exportieren
```bash
# HTML-Präsentation bauen (dist/index.html)
npm run build:html

# PDF-Dokument exportieren (dist/slides.pdf)
npm run build:pdf

# PowerPoint-Datei exportieren (dist/slides.pptx)
npm run build:pptx

# Alle Formate auf einmal bauen
npm run build:all
```

---

## 🌿 Git-Branching-Strategie

Dieses Repository ist so strukturiert, dass der **`main`-Branch** als saubere Vorlage (Template) dient. Echte Präsentationen werden in separaten Branches gepflegt:

### Neuen Vortrag anlegen
Erstelle ausgehend vom `main`-Branch einen neuen Branch für deine konkrete Arbeit:

```bash
# Auf den Haupt-Branch wechseln und sicherstellen, dass alles aktuell ist
git checkout main

# Neuen Branch für deine Arbeit/Präsentation erstellen
git checkout -b presentation/t2000-praxisarbeit
# oder
git checkout -b presentation/bachelor-thesis
```

### Arbeiten & Committen
* Bearbeite `slides.md` mit deinen Inhalten.
* Eigene Grafiken und Diagramme kannst du im Ordner `assets/` ablegen.
* Committe deine Änderungen wie gewohnt im Präsentations-Branch:
```bash
git add slides.md assets/
git commit -m "feat: Folien für Praxisarbeit T2000 fertiggestellt"
```

### Template-Updates übernehmen
Wenn das Theme oder globale Skripte auf `main` verbessert werden, kannst du diese Aktualisierungen jederzeit in deinen Präsentations-Branch mergen:
```bash
git checkout presentation/t2000-praxisarbeit
git merge main
```

---

## 🎨 Verfügbare Folien-Klassen & Layouts

Das Theme stellt maßgeschneiderte Klassen bereit, die über Markdown-Direktiven auf Folien angewendet werden können:

### 1. Titelfolie (`title` / `lead`)
Großes DHBW Ravensburg Logo, Haupt- und Untertitel, Autoren-Metadaten und die offizielle 3-Farben-Abschlussleiste.
```markdown
<!-- _class: title -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Titel der Präsentation
## Untertitel der Arbeit

<div class="meta">
**Referent:** Max Mustermann | **Kurs:** TINF23  
**Unternehmen:** Partnerunternehmen GmbH  
**Datum:** 7. Oktober 2026
</div>
```

### 2. Standard-Inhaltsfolie
Jede Standardfolie erhält automatisch das DHBW-Logo oben links, eine feine Trennlinie und eine Fußzeile mit Referent, Thema und Seitennummerierung (`Folie / Gesamt`).
```markdown
# 1. Motivation & Problemstellung
* Wichtiger Punkt 1
* Wichtiger Punkt 2

> **Wichtiger Hinweis:** Hervorgehobene Information in der Callout-Box.
```

### 3. Zweispaltiges Layout (`columns`)
```markdown
# Vergleich zweier Ansätze

<div class="columns">
<div class="col">

### Ansatz A
* Punkt 1
* Punkt 2

</div>
<div class="col">

### Ansatz B
* Punkt 1
* Punkt 2

</div>
</div>
```

### 4. Kapitel- / Zwischentitel (`chapter`)
Dunkler Schiefergrau-Hintergrund (`#5C6971`) mit rotem Akzentbalken links.
```markdown
<!-- _class: chapter -->
<!-- _header: "" -->
<!-- _footer: "" -->

# 4. Konzeption & Architektur
## Vom Entwurf zur technischen Realisierung
```

### 5. KPI-Kennzahlenkarten (`kpi-grid`)
```markdown
# Evaluationsergebnisse

<div class="kpi-grid">
  <div class="kpi-card">
    <div class="number">-65%</div>
    <div class="label">Latenzreduktion</div>
  </div>
  <div class="kpi-card">
    <div class="number">99.4%</div>
    <div class="label">Genauigkeit</div>
  </div>
  <div class="kpi-card">
    <div class="number">3.2x</div>
    <div class="label">Durchsatzsteigerung</div>
  </div>
</div>
```

### 6. Abschluss- / Q&A-Folie (`end`)
```markdown
<!-- _class: end -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Vielen Dank für Ihre Aufmerksamkeit!
## Fragen & Diskussion

<div class="meta">
**Vorname Nachname**  
Duale Hochschule Baden-Württemberg Ravensburg  
E-Mail: vorname.nachname@student.dhbw-ravensburg.de
</div>
```

### 7. Dunkler Modus (`invert`)
```markdown
<!-- _class: invert -->

# Code Walkthrough
Dunkler Hintergrund für Code-Demonstrationen oder abendliche Präsentationen.
```

---

## 🎨 DHBW Ravensburg Corporate Design Farben

| Farbname | Hex-Code | Verwendung |
| :--- | :--- | :--- |
| **DHBW Rot** | `#E2001A` | Primäre Akzentfarbe, Aufzählungszeichen, Links |
| **DHBW Dunkelrot** | `#8E130A` | Mittlerer Balken im Banner, Code-Highlights |
| **DHBW Schiefergrau** | `#5C6971` | Tabellenkopf, Untertitel, Kapitel-Hintergrund |
| **DHBW Dunkelgrau** | `#22252A` | Hauptüberschriften, Textfarbe |
| **DHBW Hellgrau** | `#F4F6F7` | Hintergründe für Cards, Callouts, Code-Blöcke |
| **Rahmenfarbe** | `#DDE1E3` | Trennlinien, Tabellenränder |

---

## 💻 VS Code Integration

1. Öffne diesen Ordner in VS Code:
   ```bash
   code .
   ```
2. Installiere die empfohlene Erweiterung **Marp for VS Code** (`marp-team.marp-vscode`).
3. Öffne `slides.md` und drücke `Ctrl+K V` (bzw. `Cmd+K V` auf macOS) für die Echtzeit-Vorschau.
4. Über das Marp-Icon in der Menüleiste oben rechts können Folien direkt als PDF/HTML/PPTX exportiert werden.

---

## 📄 Lizenz
Template & Theme stehen unter der [MIT License](LICENSE).  
Die Bildmarken und Logos der DHBW Ravensburg unterliegen dem Marken- und Urheberrecht der Dualen Hochschule Baden-Württemberg.
