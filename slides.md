---
marp: true
theme: dhbw
paginate: true
header: "Citation Evaluation"
footer: "Capstone-Project · Präsentation 2 · 19.11.2026"
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
## Prompt v7.2 und der erste Lauf auf der RTX 6000

<div class="meta">
<div><strong>Team</strong>Finn Hertsch · Tino Strasser<br>Maximilian Vogt · Florian Dittmann</div>
<div><strong>Product Owner</strong>Prof. Dr. Andreas Schilling</div>
<div><strong>Sprint 2</strong>DSKI · WDS124 / WDS224<br>19.11.2026</div>
</div>

---

###### Überblick
# Agenda

<div class="agenda">
<div><span>01</span>Projektstand</div>
<div><span>04</span>Fehlalarme & Prompt v7.2</div>
<div><span>02</span>RTX 6000 statt Spark</div>
<div><span>05</span>Ergebnis-UI</div>
<div><span>03</span>Lauf mit Prompt v7.1</div>
<div><span>06</span>Ausblick</div>
</div>

---

###### 01 · Projektstand
# Kanban-Board

<div class="placeholder" style="height: 400px;">
TODO: Board-Stand vom 19.11.2026 einfügen<br>
(Vorlage: Folie „Kanban-Board“ aus Präsentation 1 im Branch presentation/citation-evaluation)
</div>

---

###### 02 · Hardware
# Läufe auf der RTX 6000 statt auf der Spark

<div class="grid g3">
<div class="kpi-card"><div class="number">200 / 200</div><div class="label">gültige Antworten</div><div class="sub">Spark mit v6: 131 von 1.172</div></div>
<div class="kpi-card hl"><div class="number">2 Profile</div><div class="label">auf dem RTX6000-Server</div><div class="sub">gpt-oss-120b und Qwen3.8</div></div>
<div class="kpi-card"><div class="number">fest gezogen</div><div class="label">200 Zitate je Lauf</div><div class="sub">je 100 mit und ohne Problem</div></div>
</div>

> Die Spark-Ausfälle aus Sprint 1 sind damit kein Risiko mehr für den Lauf. Dieselbe Anzahl Zitate zieht dieselbe Stichprobe, Läufe sind vergleichbar.

---

###### 03 · Erster Lauf mit v7.1
# gpt-oss-120b: 90 % Genauigkeit auf 200 Zitaten

<div class="columns" style="align-items: center;">
<div style="flex: 1.3;">

| Kennzahl | v7.1 · RTX 6000 | v6 · Spark |
| :--- | :---: | :---: |
| Gültige Antworten | **200 / 200** | 131 / 1.172 |
| Genauigkeit | **90,0 %** | 84,7 % |
| Falsch-positiv-Rate | **15 %** (15/100) | 17,3 % (17/98) |
| Falsch-negativ-Rate | **5 %** (5/100) | 9,1 % (3/33) |

</div>
<div class="kpi-stack" style="flex: 0.7;">
<div class="card red"><p><strong>Nicht direkt vergleichbar:</strong> anderer Server, andere Stichprobe, nur 33 Fälle mit Problem bei v6</p></div>
<div class="card"><p>Aussage: v7.1 ist <strong>nicht schlechter</strong>, mehr nicht</p></div>
</div>
</div>

<p class="note">gpt-oss-120b · RTX 6000 · Browser-use · binärer Benchmark · Lauf f95d4a4c · 28.10.2026</p>

---

###### 04 · Fehlalarme
# 15 Fehlalarme zeigen drei Lücken im Prompt

<div class="columns" style="align-items: start;">
<div style="flex: 1.5;">

| Lücke | Beispiel | v7.1 | v7.2 |
| :--- | :--- | :---: | :---: |
| **Frühere Fassung** trägt Titel oder Autoren (arXiv v1, v2) | Doloriel 2025, 8 weitere Autoren in der aktuellen Fassung | 3 | **1** |
| **Proceedings- und Nachdruckjahr** | Liu et al., NeurIPS 36: Konferenzjahr 2023, Bandjahr 2024 | 3 | **1** |
| **Organisation als Autor**, fehlendes Jahr | Google Research, Med-Gemini, 2024b | 3 | **2** |
| **Mitwirkende einer Auflage** | Spirtes et al., MIT Press 2000 | 3 | **1** |
| **Gesperrte Quelle**, keine Alternative gesucht | OpenReview hinter Cloudflare | 4 | **1** |

</div>
<div class="kpi-stack" style="flex: 0.5;">
<div class="kpi-card hl"><div class="number">12</div><div class="label">Fälle mit neuer Regel</div><div class="sub">Status nach v7.2 erwartet</div></div>
</div>
</div>

---

###### 04 · Prompt v7.2
# Lockerer an der Form, strenger bei der Autorenliste

<div class="columns">
<div class="card" style="flex: 1;">

### Neu in v7.2
<p>Titel, Autoren und Reihenfolge einer <strong>früheren Fassung</strong> sind kein Fehler</p>
<p><strong>Organisationen</strong> dürfen Autor von Webseiten, Datensätzen und Software sein</p>
<p><strong>DBLP und Semantic Scholar</strong> vor Status 4 prüfen</p>

</div>
<div class="card red" style="flex: 1;">

### Gegenmaßnahme
<p>Die <strong>vollständige Autorenliste</strong> muss abgeglichen werden: 5 Fälle mit Problem wurden akzeptiert, bei einem nannte das Modell nur den Erstautor</p>
<p class="note">Risiko: Behauptet das Modell eine frühere Fassung ohne Beleg, steigt die Falsch-negativ-Rate.</p>

</div>
</div>

> Der Effekt von v7.2 ist **noch nicht gemessen**. Dafür braucht es einen neuen Lauf auf denselben 200 Zitaten.

---

###### 04 · Messgrenzen
# Manchmal liegt das Modell richtig und das Label falsch

<div class="columns" style="align-items: center;">
<div style="flex: 1.2;">

| Fall | Zitat | Modell sagt |
| :--- | :--- | :--- |
| `ca-01632` | Kaplan et al., Scaling laws, 2020 | Jeffrey Wu fehlt in der Autorenliste |
| `ca-01851` | Wu, Wang, Long, Autoformer, 2021 | Jiehui Xu fehlt in der Autorenliste |

</div>
<div class="kpi-stack" style="flex: 0.8;">
<div class="card"><p>Fehlender Autor bleibt <strong>Inhaltsfehler</strong>, auch wenn CiteAudit „Real“ sagt</p></div>
<div class="card red"><p>Wir gleichen diese Fälle <strong>bewusst nicht aus</strong>: das Label ist vermutlich falsch</p></div>
</div>
</div>

<p class="note">Zwei Fälle bleiben außerdem unklar: ca-03078 und ca-03060 beruhen auf Vorwissen und müssen an der Quelle bestätigt werden.</p>

---

###### 05 · Ergebnis-UI
# Läufe verwalten, Fälle einzeln prüfen

<div class="columns" style="align-items: center;">
<div class="kpi-stack" style="flex: 0 0 340px;">

* **Drilldown:** Anfrage, Status und Musterlösung je Zitat
* **Filter** nach FP / FN / TP / TN aus der Confusion Matrix
* **Läufe** umbenennen, löschen, fehlgeschlagene Versuche wiederholen
* **Prompt-Version** je Lauf sichtbar

<div class="card red"><p><strong>Live-Demo</strong> → wir wechseln in die Anwendung</p></div>
</div>
<div class="shot" style="flex: 1;">

![](assets/ui-new.png)

</div>
</div>

---

###### 06 · Ausblick
# Nächste Schritte

<div class="steps">
<div class="step-item active" style="border: 1.5px solid rgba(226, 0, 26, 0.4);">
<div class="step-num" style="color: var(--red); font-weight: 700;">01 · Als Nächstes</div>
<div class="step-title" style="color: var(--red);">v7.2 messen</div>
<div class="step-desc">Neuer Lauf auf denselben 200 Zitaten, Worker neu bauen</div>
</div>
<div class="step-item">
<div class="step-num">02</div>
<div class="step-title">Falsch Negative</div>
<div class="step-desc">Fünf akzeptierte Zitate mit Problem-Label an der Quelle prüfen</div>
</div>
<div class="step-item">
<div class="step-num">03</div>
<div class="step-title">Skalieren</div>
<div class="step-desc">Parallele Worker, 5.000 Zitate, dann Vollauf</div>
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
