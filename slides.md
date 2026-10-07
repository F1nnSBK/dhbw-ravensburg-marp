---
marp: true
theme: dhbw
paginate: true
header: "DHBW Ravensburg"
footer: "Vorname Nachname | Titel der Präsentation | 2026"
---

<!-- _class: title -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Titel der Präsentation
## Untertitel der Arbeit oder des Projekts

<div class="meta">

**Referent:** Vorname Nachname  
**Studiengang:** Informatik / Wirtschaftsinformatik | Kurs: TINF23  
**Duales Partnerunternehmen:** Musterunternehmen SE & Co. KG  
**Betreuer:** Prof. Dr. Max Mustermann (DHBW) / Betreuer Name (Partner)  
**Datum:** 7. Oktober 2026

</div>

---

# Agenda

1. **Motivation & Problemstellung**
   * Ausgangslage und Herausforderungen in der Praxis
2. **Zielsetzung & Forschungsfragen**
   * Zieldefinition, SMART-Kriterien und Scope
3. **Stand der Technik & Methodik**
   * Bisherige Ansätze und wissenschaftliche Grundlagen
4. **Konzeption & Architektur**
   * Systementwurf, Komponenten und Datenfluss
5. **Implementierung & Prototyp**
   * Technische Umsetzung und Code-Architektur
6. **Evaluation & Ergebnisse**
   * Messungen, Benchmark-Vergleich und Analyse
7. **Fazit & Ausblick**
   * Zusammenfassung, Limitationen und nächste Schritte
8. **Diskussion & Q&A**

---

# 1. Motivation & Problemstellung

### Ausgangslage
* Zunehmende Komplexität moderner softwarebasierter Systeme im Unternehmensumfeld.
* Manuelle Prozesse führen zu Verzögerungen und erhöhter Fehleranfälligkeit.
* Bestehende Werkzeuge bieten unzureichende Integrationsfähigkeit in bestehende Toolchains.

### Kernherausforderungen
* **Skalierbarkeit:** Hoher Ressourcenbedarf bei wachsenden Datenmengen.
* **Wartbarkeit:** Heterogene Architekturansätze erschweren den Betrieb.
* **Compliance & Sicherheit:** Strengere Anforderungen an Datenkonsistenz und Zugriffsschutz.

> **Problemstatement:**  
> Bisherige Lösungen decken entweder nur isolierte Teilschritte ab oder erfordern unverhältnismäßig hohen Konfigurationsaufwand für cross-funktionale Teams.

---

# 2. Zielsetzung & Forschungsfragen

### Hauptforschungsfrage
> *Inwiefern lässt sich durch eine modulare, deklarative Architektur die Effizienz und Wartbarkeit bei gleichzeitiger Einhaltung industrieller Qualitätsstandards signifikant steigern?*

### Konkrete Projektziele
1. **Entwicklung eines lauffähigen Prototyps** zur automatisierten Verarbeitung und Transformation.
2. **Standardisierung der Schnittstellen** auf Basis offener Protokolle (z. B. REST, gRPC).
3. **Quantifizierbare Evaluation** hinsichtlich Durchsatz, Latenz und Entwicklerproduktivität.

### Scope & Abgrenzung
* **Im Fokus:** Kern-Pipeline, Schnittstellenvalidierung, Benchmarking im Laborumfeld.
* **Nicht im Fokus:** Migration historischer Altsysteme vor dem Stichtag.

---

# 3. Stand der Technik & Vergleich

<div class="columns">
<div class="col">

### Bisherige Ansätze
* Proprietäre Legacy-Systeme
* Hohe Lizenz- und Betriebskosten
* Geringe Flexibilität für Erweiterungen
* Fehlende Automatisierung

</div>
<div class="col">

### Moderner Ansatz
* Modulare Open-Source-Basis
* Deklarative Konfiguration
* Nahtlose CI/CD-Integration
* Reproduzierbare Deployments

</div>
</div>

### Systemvergleich

| Kriterium | Traditioneller Ansatz | Moderner Ansatz (Ziel) | Bewertung |
| :--- | :--- | :--- | :--- |
| **Setup-Zeit** | ~3-5 Tage manuell | < 15 Minuten automatisiert | **+90%** Zeitersparnis |
| **Wartungsaufwand** | Hoch (manuelle Patches) | Gering (Container & IaC) | Signifikant reduziert |
| **Testabdeckung** | < 40% (sporadisch) | > 85% (automatisiert) | Höhere Zuverlässigkeit |

---

<!-- _class: chapter -->
<!-- _header: "" -->
<!-- _footer: "" -->

# 4. Konzeption & Architektur
## Vom Entwurf zur technischen Realisierung

Strukturierte Systemmodellierung, Komponentenentwurf und Schnittstellendefinition für robuste Enterprise-Anwendungen.

---

# 4. Systemarchitektur & Ablauf

### Schichtenarchitektur

```
+-------------------------------------------------------------+
| Presentation Layer: Marp CLI / Web Viewer / Export Engine  |
+-------------------------------------------------------------+
                              |
+-------------------------------------------------------------+
| Application Core: Theme Engine (DHBW CD) & Markdown Parser  |
+-------------------------------------------------------------+
                              |
+-------------------------------------------------------------+
| Asset & Template Store: SVG Logos, Color Schemes, Palettes  |
+-------------------------------------------------------------+
```

### Kernprinzipien des Entwurfs
* **Separation of Concerns:** Trennung von Inhalt (Markdown) und Stil (CSS Theme).
* **Corporate Identity Compliance:** Strikte Einhaltung des DHBW Corporate Designs.
* **Portabilität:** Eigenständige Distribution als HTML, PDF oder PowerPoint (PPTX).

---

# 5. Implementierung & Code-Beispiel

### Deklarative Folienkonfiguration

```markdown
---
marp: true
theme: dhbw
paginate: true
header: "DHBW Ravensburg"
footer: "Referent | Thema | 2026"
---

<!-- _class: split -->
# Zweispaltige Folie
Inhalte werden automatisch nach DHBW Corporate Design gerendert.
```

### Wesentliche Implementierungsaspekte
* **CSS Custom Properties:** Zentrale Farbdefinitionen (`--dhbw-red: #E2001A`, `--dhbw-slate: #5C6971`).
* **Vektor-Assets:** Verlustfreie Skalierung aller Bildmarken als SVG.
* **CLI-Automatisierung:** Vorkonfigurierte npm-Skripte für Hot-Reload und Multi-Format-Builds.

---

# 6. Evaluation & Ergebnisse

<div class="kpi-grid">
  <div class="kpi-card">
    <div class="number">-65%</div>
    <div class="label">Erstellungsaufwand pro Foliensatz</div>
  </div>
  <div class="kpi-card">
    <div class="number">100%</div>
    <div class="label">CI-Konformität (DHBW Ravensburg)</div>
  </div>
  <div class="kpi-card">
    <div class="number">3 Formate</div>
    <div class="label">HTML, PDF & PPTX auf Knopfdruck</div>
  </div>
</div>

### Wichtigste Evaluationsergebnisse
* **Produktivität:** Fokus auf Inhalte statt Formatierungsdetails in PowerPoint.
* **Versionierbarkeit:** Vollständige Git-Historie für Präsentationen (Diffs & Branches).
* **Cross-Plattform:** Identische Darstellung unter macOS, Linux und Windows.

---

# 7. Fazit & Ausblick

### Fazit
* Erfolgreiche Konzeption und Umsetzung des DHBW Ravensburg Marp-Templates.
* Vollständige Abdeckung aller typischen Folientypen (Titel, Inhalt, 2-Spalten, Tabellen, KPIs).
* Etablierung eines sauberen Workflows mit Git (`main` als Vorlage, Feature-Branches für Vorträge).

### Ausblick & Nächste Schritte
* **Theme-Varianten:** Ergänzung standortspezifischer Akzente (z. B. Campus Friedrichshafen).
* **CI/CD Automation:** GitHub Actions Pipeline für automatisierten PDF-Export bei Git-Tags.
* **Komponentenbibliothek:** Zusätzliche vorgefertigte Diagramme und Tabellen-Vorlagen.

---

<!-- _class: end -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Vielen Dank für Ihre Aufmerksamkeit!
## Fragen & Diskussion

<div class="meta">

**Vorname Nachname**  
Duale Hochschule Baden-Württemberg Ravensburg  
Campus Ravensburg: Marienplatz 2, 88212 Ravensburg  
Campus Friedrichshafen: Fallenbrunnen 2, 88045 Friedrichshafen  

* **E-Mail:** vorname.nachname@student.dhbw-ravensburg.de  
* **Web:** [www.ravensburg.dhbw.de](https://www.ravensburg.dhbw.de)

</div>

---

<!-- _class: blank -->
<!-- _header: "DHBW Ravensburg | Anhang" -->

# Quellen & Literaturverzeichnis

1. **Duale Hochschule Baden-Württemberg (DHBW)** (2021): *Corporate Design Manual & Präsentationsrichtlinien*, DHBW Ravensburg.
2. **Marp Team** (2026): *Marp: Markdown Presentation Ecosystem*, https://marp.app/.
3. **Tufte, E. R.** (2001): *The Visual Display of Quantitative Information*, Graphics Press, 2. Auflage.
4. **Sommerville, I.** (2018): *Software Engineering*, Pearson Studium, 10. aktualisierte Auflage.
5. **Gamma, E. et al.** (1994): *Design Patterns: Elements of Reusable Object-Oriented Software*, Addison-Wesley.

---

<!-- _class: invert -->

# Backup: Dunkler Folienstil (Invert Mode)

### Optionale Stil-Variante für technische Themen
* Durch Setzen von `<!-- _class: invert -->` wird ein eleganter dunkler Hintergrund aktiviert.
* Ideal geeignet für:
  * Ausführliche Code-Walkthroughs
  * Systemarchitekturen und Terminal-Demos
  * Abendpräsentationen mit reduzierter Blendwirkung

```bash
# Beispiel-Befehl für den Build-Vorgang
npm run build:all
```
