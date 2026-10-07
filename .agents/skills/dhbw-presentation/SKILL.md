---
name: dhbw-presentation
description: Guide and automate creating, developing, styling, and exporting DHBW Ravensburg presentations using Marp. Enforces corporate identity, branch workflows, safe layout boundaries, and Tufte-style SVG plots.
---

# DHBW Ravensburg Marp Presentation Skill

This skill guides an AI assistant in creating, maintaining, and exporting academic and professional presentations for the **Duale Hochschule Baden-Württemberg (DHBW) Ravensburg** using Marp.

---

## 🎯 When to Use This Skill

Activate or refer to this skill whenever the user wants to:
1. Create a new presentation or branch for a project/bachelor thesis at DHBW Ravensburg.
2. Add, modify, or format slides in `slides.md`.
3. Create scientific plots, system architectures, or evaluation metrics.
4. Export presentations to standalone HTML, PDF, or PowerPoint (PPTX).
5. Debug layout, typography, or alignment issues in Marp.

---

## 🌿 Branching Protocol

* **Rule 1:** `main` is the pristine template. NEVER write presentation-specific content directly on `main`.
* **Rule 2:** To start a new presentation, create a branch:
  ```bash
  npm run new <themen-name>
  # Example: npm run new t2000-praxisarbeit
  ```
* **Rule 3:** Commit slide changes in that specific presentation branch.

---

## 🎨 DHBW Corporate Design Standards

### Color Constants
* `--dhbw-red`: `#E2001A` (Primary brand accent, bullets, key numbers)
* `--dhbw-dark-red`: `#8E130A` (Secondary dark red, code highlights)
* `--dhbw-slate`: `#5C6971` (Slate grey, headers, subtitles, chapter backgrounds)
* `--dhbw-dark`: `#22252A` (Text, titles)
* `--dhbw-light`: `#F8F9FA` (Cards, background highlights)
* `--dhbw-light-border`: `#E2E6E9` (Dividers, borders)

### Strict Layout Constraints (Preventing Overflow)
* Slide dimensions: `1280px` x `720px` (16:9).
* Safe content vertical area: **max 572px** (between `top: 86px` and `bottom: 62px`).
* **Rule:** If a slide contains both KPI cards and an SVG plot/diagram, ALWAYS use a two-column layout (`<div class="columns">`) instead of stacking them vertically.

---

## 📊 Scientific Data Visualization Rules

1. **Always SVG:** Never generate or use PNG/JPEG for data plots; always use clean, responsive SVG.
2. **Tufte Style:** Follow Edward Tufte's principles (high data-to-ink ratio, minimal axes, no decorative clutter).
3. **No LaTeX Code in SVGs or Chat:** Never use `\textbf` or LaTeX annotations inside SVG plots.
4. **Colors in Plots:** Use `#E2001A` for the primary data series, `#5C6971` for axes and secondary series, `#9AA5AC` for baselines.

---

## 🚀 Execution & Build Commands

```bash
# Start live development server (Port 8080 with auto-reload)
npm start

# Build all formats (HTML, PDF, PPTX)
npm run build:all

# Individual builds
npm run build:html  # dist/index.html
npm run build:pdf   # dist/slides.pdf
npm run build:pptx  # dist/slides.pptx
```
