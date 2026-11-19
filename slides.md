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
.kpi-stack.compact .kpi-card { padding: 12px 20px; }
.kpi-stack.compact .kpi-card .number { font-size: 34px; }

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

<!--
Einstieg: In Sprint 1 haben wir einen Prüfer gebaut und auf 200 Zitaten getestet. Heute: Was passiert, wenn er auf den ganzen Datensatz mit 9.354 Zitaten läuft? Erst die Frage, wie wir das überhaupt schaffen, dann, was dabei herauskommt.
-->

---

###### Überblick
# Agenda

<div class="agenda">
<div><span>01</span>Projektstand</div>
<div><span>04</span>Warum so viele Fehlalarme?</div>
<div><span>02</span>RTX 6000 & Laufzeit</div>
<div><span>05</span>Ausblick</div>
<div><span>03</span>Läufe, Prompt v7.2 und Vergleich</div>
</div>

---

###### 01 · Projektstand · letztes Mal
# Wo wir bei der letzten Präsentation standen

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
<div class="board-col compact">
<div class="board-head">To Do <span>0</span></div>
</div>
<div class="board-col compact">
<div class="board-head">In Arbeit <span>3</span></div>
<div class="board-card"><b>CE-25 <span class="who">Maximilian</span></b>Judgement Calls & parallele Worker</div>
<div class="board-card"><b>CE-23 <span class="who">Florian</span></b>Neue Kategoriendefinition testen</div>
<div class="board-card"><b>CE-22 <span class="who">Finn</span></b>RTX 6000 für parallele Samples</div>
</div>
<div class="board-col compact">
<div class="board-head">In Review <span>1</span></div>
<div class="board-card"><b>CE-24 <span class="who">Finn</span></b>Präsentation mit Marp</div>
</div>
<div class="board-col compact">
<div class="board-head">Erledigt <span>2</span></div>
<div class="board-card done"><b>CE-21 <span class="who">Tino</span></b>Rechenleistung angefragt</div>
<div class="board-card done"><b>CE-26 <span class="who">Tino</span></b>Ergebnis-UI verbessern</div>
</div>
</div>

<p class="note">Snapshot aus der letzten Präsentation — Status und Aufgaben wie damals übernommen.</p>

<!--
Zur Erinnerung: Stand aus Präsentation 1. Zwei Dinge waren offen, die den Vollauf bestimmen: die RTX 6000 (CE-22) und die Judgement Calls (CE-25).
-->

---

###### 01 · Projektstand · jetzt
# Vollauf abgeschlossen, Analyse läuft weiter

<div class="board" style="grid-template-columns: repeat(5, 1fr); gap: 12px;">
<div class="board-col compact">
<div class="board-head">Backlog <span>8</span></div>
<div class="board-card"><b>CE-30</b>DSGVO & Recht</div>
<div class="board-card"><b>CE-31</b>Statistische Tests</div>
<div class="board-card"><b>CE-33</b>CLI ausbauen</div>
<div class="board-card"><b>CE-28</b>Multi-User-Zugriff</div>
<div class="board-card"><b>CE-29</b>Status Modellserver</div>
<div class="board-card"><b>CE-22 <span class="who">Finn</span></b>RTX 6000 für parallele Samples</div>
<div class="board-card"><b>CE-34</b>WebUI mit Login</div>
<div class="board-card"><b>CE-32</b>WebUI statt SSH</div>
</div>
<div class="board-col compact">
<div class="board-head">To Do <span>2</span></div>
<div class="board-card"><b>CE-40</b>Modellvergleich Qwen vs. GPT vs. Deepseek</div>
<div class="board-card"><b>CE-41</b>Open-Weights-Modelle auf RTX 6000 / DGX Spark</div>
</div>
<div class="board-col compact">
<div class="board-head">In Arbeit <span>2</span></div>
<div class="board-card"><b>CE-44 <span class="who">Tino</span></b>Docker-Worker sammelt Zombie-Prozesse an</div>
<div class="board-card"><b>CE-37 <span class="who">Finn</span></b>Kritische Prüfung der Modellwahl</div>
</div>
<div class="board-col compact">
<div class="board-head">In Review <span>0</span></div>
</div>
<div class="board-col compact" style="padding: 10px;">
<div class="board-head">Erledigt <span>10</span></div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-38</b>Datensatz-Analyse</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-43 <span class="who">Tino</span></b>Test auf V6</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-39 <span class="who">Florian</span></b>Drilldown-Feature</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-23 <span class="who">Florian</span></b>Neue Kategoriendefinition</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-25 <span class="who">Maximilian</span></b>Judge-Calls</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-26 <span class="who">Tino</span></b>UI verbessern</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-24 <span class="who">Finn</span></b>Präsentation mit Marp</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-42 <span class="who">Finn</span></b>Slides an Schilling</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-21 <span class="who">Tino</span></b>Rechenleistung</div>
<div class="board-card done" style="font-size: 12px; padding: 4px 8px; margin-bottom: 4px;"><b>CE-36 <span class="who">Finn</span></b>Steckdose aussuchen</div>
</div>
</div>

<p class="note">YouTrack, Stand 19.11.2026. Offen bleiben die statistische Auswertung, der Modellvergleich und die geplanten Zugriffs-/CLI-Funktionen.</p>

<!--
Heute: 10 Tickets erledigt, 2 in Arbeit, 2 als Nächstes. Der Vollauf ist durch, offen ist vor allem die Auswertung. Überleitung: Wie kam es, dass der Vollauf plötzlich machbar war? Das war eine Frage der Laufzeit.
-->

---

###### 02 · Hardware
# Läufe auf der RTX 6000 statt auf der Spark

<div class="grid g3">
<div class="kpi-card"><div class="number">9.354 / 9.354</div><div class="label">gültige Antworten je Vollauf</div><div class="sub">0 fatale Fehler · Chromium-Zombieprozesse behoben</div></div>
<div class="kpi-card hl"><div class="number">2</div><div class="label">Vollläufe mit je 9.354 Zitaten</div><div class="sub">Run 1 mit Prompt v6 · Run 2 mit v7.2</div></div>
<div class="kpi-card"><div class="number">gpt-oss-120b</div><div class="label">auf dem RTX6000-Server</div><div class="sub">Browser-use · 600 s Timeout je Zitat</div></div>
</div>

> Die Spark-Ausfälle sind kein Risiko mehr: **Beide Vollläufe** liefen auf der RTX 6000 durch.

<!--
Ausgangsfrage: 9.354 Zitate mit ~150 s auf der Spark wären über 16 Tage und ein hohes Ausfallrisiko (die Spark ist zweimal überhitzt). Die RTX 6000 hat den Vollauf ohne fatalen Fehler durchgetragen. Die nächsten Folien zeigen, woher die Zeitersparnis genau kommt.
-->

---

###### 02 · Laufzeit
# Vollauf in 6,5 Tagen statt 16

<div class="columns" style="align-items: center;">
<div class="kpi-stack compact" style="flex: 0 0 340px; gap: 10px;">
<div class="kpi-card hl"><div class="number">45 s</div><div class="label">Median je Zitat</div><div class="sub">geplant: 157 s</div></div>
<div class="kpi-card"><div class="number">≈ 3×</div><div class="label">RTX 6000 statt Spark</div><div class="sub">schnellerer Modellserver</div></div>
<div class="kpi-card"><div class="number">−10 bis −17 %</div><div class="label">Judges aus</div><div class="sub">gleiches Ergebnis, weniger LLM-Calls</div></div>
</div>
<div style="flex: 1;">

<img src="assets/runtime-planned-vs-measured.svg" alt="Geplant gegen gemessen im Vollauf" style="width: 100%; display: block;">

</div>
</div>

> Zwei Gründe: **schnellerer Server** und **Judges aus**. Ein Worker, noch ohne Parallelität.

<p class="note">Run 1 · gpt-oss-120b · Browser-use · Prompt v6 · n = 9.354 · 02.–09.11.2026 · Run 2 (v7.2): Median 51 s · Faktor 3× zur Spark grob (anderer Split, Codestand, Hardware)</p>

<!--
- Geplant hatten wir 16 Tage, gerechnet mit 157 s je Zitat auf der Spark.
- Der Vollauf mit 9.354 Zitaten hat 6,5 Tage gedauert, im Median 45 s je Zitat.
- Warum kürzer? Zwei Gründe, beide in den Vollläufen aktiv:
  - Schnellerer Server: RTX 6000 statt Spark, grob Faktor 3. Grob, weil Split, Codestand und Hardware sich unterscheiden.
  - Judges aus: spart 10 bis 17 % je Zitat, ohne das Ergebnis zu ändern. Das zeige ich auf der nächsten Folie.
- Wichtig: Beide Vollläufe liefen mit einem Worker, also noch ohne Parallelität. Dazu danach.
-->

---

###### 02 · Laufzeit · Judges
# Judges aus: gleiches Ergebnis, weniger Calls

<div class="columns" style="align-items: start;">
<div style="flex: 1.3;">

| Mittel je Quelle, Test-Split | Qwen3.8-27B | GPT-OSS-120B |
| :--- | ---: | ---: |
| Zeit mit Judges | 63,6 s | 48,3 s |
| Zeit ohne Judges | 48,3 s | 43,5 s |
| Ersparnis gemessen | **−24 %** | **−10 %** |
| davon Judges direkt | 10,4 s | 8,0 s (16,6 %) |
| LLM-Calls | 5,0 → 2,7 | 6,1 → 4,6 |
| Qualität | unverändert | unverändert |

</div>
<div class="kpi-stack" style="flex: 1; gap: 12px;">
<div class="card"><p><strong>Was sind Judges?</strong> browser-use bewertet nach jeder Prüfung den Verlauf mit 2 zusätzlichen LLM-Calls. Unser Ergebnis ändert das nicht: <strong>bytegleiches Endergebnis</strong>.</p></div>
<div class="card red"><p><strong>Verworfen</strong>, weil sie Entscheidungen ändern: reasoning low (−42 %), Flash (−53 %), No-Thinking (−39 %)</p></div>
</div>
</div>

<p class="note">Test-Split, 10 Fälle × 3 Wiederholungen · Schalter BU_DISABLE_JUDGE, BU_DISABLE_SIMPLE_JUDGE · Nebenbefund: Telemetrie von browser-use an PostHog jetzt fest aus</p>

<!--
- Judges: browser-use macht nach jeder fertigen Prüfung zwei zusätzliche LLM-Calls, Simple Judge und Full Judge. Die bewerten nur den Verlauf, nicht die Quelle.
- Unser Ergebnis ändern sie nicht. Test mit dem echten Agenten: bytegleiches Endergebnis. Außerdem laufen sie außerhalb der Timeouts.
- Lösung: zwei Schalter. Standard ist "an", damit alte Läufe reproduzierbar bleiben.
- Achtung, andere Messgröße als auf der Folie davor: hier Mittelwert auf dem Test-Split, nicht Median im Vollauf.
- Messung: Qwen spart 24 %, GPT-OSS 10 %. Direkt gemessen kosten die Judges bei GPT-OSS 16,6 % der Zeit. Dass nur 10 % herauskamen, liegt an Zufall: In den Läufen ohne Judges waren 3 Cloudflare-Sperren.
- LLM-Calls sinken um 47 % (Qwen) bzw. 25 % (GPT-OSS).
- Andere Schalter waren schneller, ändern aber Einzelentscheidungen. Deshalb verworfen.
- Nebenbefund Datenschutz: browser-use schickte standardmäßig Zitat, URLs und Ergebnis an PostHog. Das ist jetzt fest aus.
-->

---

###### 02 · Laufzeit · Ausblick
# Noch mehr drin: 8 parallele Prüfungen, 3,9× Durchsatz

<div class="columns" style="align-items: center;">
<div style="flex: 1.2;">

<img src="assets/parallel-throughput.svg" alt="Durchsatz nach Anzahl Worker" style="width: 100%; display: block;">

</div>
<div class="kpi-stack compact" style="flex: 1; gap: 10px;">
<div class="kpi-card hl"><div class="number">8</div><div class="label">Requests gleichzeitig</div><div class="sub">mehr verarbeitet der Server nicht, darüber Warteschlange</div></div>
<div class="kpi-card"><div class="number">85–90 %</div><div class="label">binäre Genauigkeit bis 8 Worker</div><div class="sub">bei 12 Workern 82 %</div></div>
<div class="kpi-card"><div class="number">~28 h</div><div class="label">Hochrechnung für 9.354 Zitate</div><div class="sub">statt 105–113 h seriell mit Judges aus</div></div>
</div>
</div>

> Bisher **nur getestet**, in den Vollläufen noch nicht genutzt. Sweet Spot: 8 Worker je Server.

<p class="note">GPT-OSS-120B auf RTX 6000 · Judges aus · je Worker-Anzahl ein Lauf · 0 HTTP-Fehler · Grenze vermutlich max_num_seqs = 8 · KV-Cache max. 13 % belegt</p>

<!--
- Das ist der nächste Hebel, den wir bisher nur getestet haben. In den Vollläufen war er noch nicht drin.
- Gemessen mit GPT-OSS auf der RTX, Judges aus, mit 1, 2, 4, 8 und 12 Workern.
- Seriell schaffen wir 86 Quellen pro Stunde, mit 8 Workern 330, also 3,9-fach.
- Jede einzelne Prüfung wird dabei langsamer (Median 36 s auf 80 s), aber es laufen 8 gleichzeitig.
- Warum 8? Der Server verarbeitet höchstens 8 Requests gleichzeitig, vermutlich max_num_seqs = 8. Bei 12 Workern warten bis zu 4 in der Warteschlange, der längste LLM-Call liegt mit 71 s knapp am LLM-Call-Timeout von 75 s, und die Qualität fällt auf 82 %.
- Bis 8 Worker ist die Qualität stabil bei 85 bis 90 %.
- Der GPU-Speicher ist kein Engpass: KV-Cache maximal 13 % belegt.
- Hochgerechnet: ~28 h für alle 9.354 Zitate statt 105 bis 113 h seriell.
-->

---

###### 02 · Laufzeit · Nächste Schritte
# Drei Dinge vor dem 28-h-Lauf

<div class="steps">
<div class="step-item active">
<div class="step-num">01 · Runner</div>
<div class="step-title">8 Worker je Server erlauben</div>
<div class="step-desc">Der Runner startet bisher nur einen Versuch je Modellserver. Änderung in runner.py, eigenes Ticket.</div>
</div>
<div class="step-item">
<div class="step-num">02 · Kontext</div>
<div class="step-title">max_model_len ≥ 64k</div>
<div class="step-desc">Größter Prompt 27,9k Token + 4.096 Antwort ≈ 32k von 32.768. Sonst drohen Abbrüche.</div>
</div>
<div class="step-item">
<div class="step-num">03 · Drosselung</div>
<div class="step-title">Testlauf 1–2 h mit 8 Workern</div>
<div class="step-desc">Ungetestet, ob DuckDuckGo oder Cloudflare bei ~1.000 Suchen pro Stunde drosseln.</div>
</div>
</div>

> Danach läuft der volle CiteAudit-Lauf in **gut einem Tag** statt gut zwei Wochen.

<p class="note">10 Fälle × 3 Wiederholungen reichen nur für grobe Aussagen: Unterschiede unter ~15 Prozentpunkten sind nicht belegbar.</p>

<!--
- Bevor wir den 28-h-Lauf starten, müssen drei Dinge passieren.
- Erstens der Runner: Er erlaubt aktuell nur einen Versuch pro Modellserver. Für 8 Worker braucht es eine Änderung in evaluation/app/runner.py, das wird ein eigenes Ticket.
- Zweitens die Kontextlänge: Der größte Prompt hatte 27,9k Token, mit 4.096 Antwort-Token sind das fast die vollen 32.768. Bei 9.354 Quellen sind Abbrüche wahrscheinlich, daher am RTX-Server auf mindestens 64k erhöhen.
- Drittens Drosselung: Mit 8 Workern machen wir rund 1.000 Suchen pro Stunde. Ob DuckDuckGo oder Cloudflare das über 28 h mitmachen, ist ungetestet. Deshalb vorher 1 bis 2 Stunden testen.
- Zur Einordnung: Die Messungen sind klein. Unterschiede unter etwa 15 Prozentpunkten können wir nicht belegen.
-->

---

###### 03 · Läufe
# Zwei Prompt-Versionen, zwei Testgrößen

<div class="grid g2">
<div class="card">

### Test: 200 Zitate (28.10.)

| Prompt | Genauigkeit | FPR | FNR |
| :--- | ---: | ---: | ---: |
| v7.1 | 90,0 % | 15 % | 5 % |
| v7.2 | **91,5 %** | **13 %** | **4 %** |

<p class="note" style="margin-top: 14px;"><strong>Nicht belastbar:</strong> Im Saldo 2 FP und 1 FN weniger. Fallweise sind 5 FP behoben, aber 3 neu dazugekommen.</p>

</div>
<div class="card">

### Vollauf: 9.354 Zitate

| Lauf | Genauigkeit | FPR | FNR |
| :--- | ---: | ---: | ---: |
| Run 1 · v6 | 87,4 % | 16,1 % | 5,2 % |
| Run 2 · v7.2 | **88,8 %** | **14,1 %** | **4,8 %** |

<p class="note" style="margin-top: 14px;"><strong>Belastbar:</strong> Die Fehlalarme sinken signifikant (McNemar p &lt; 0,001), die übersehenen Fakes nicht.</p>

</div>
</div>

> Der Test mit 200 Zitaten ist zu klein für eine Aussage. Tragen kann sie nur der Vergleich der Vollläufe.

<p class="note">gpt-oss-120b · RTX 6000 · Browser-use · Fake = positive Klasse · FPR/FNR: Falsch-positiv-/Falsch-negativ-Rate · Run 1: 02.–09.11., Run 2: 29.10.–16.11.</p>

<!--
Zwei Prompt-Versionen, zwei Größen, und die Kästen gehören jeweils zur Tabelle darüber. Links der Test auf 200 Zitaten: v7.2 wirkt leicht besser, aber im Saldo sind es nur 2 Fehlalarme, fallweise 5 behoben und 3 neu. Das ist Rauschen. Rechts die zwei Vollläufe auf allen 9.354 Zitaten: Run 1 mit Prompt v6 ist unsere Baseline, Run 2 mit v7.2. Dort ist der Rückgang der Fehlalarme signifikant. Deshalb stützen wir uns auf die Vollläufe.
-->

---

###### 03 · Baseline
# Run 1 (Prompt v6): Fakes erkannt, aber 1.031 Fehlalarme

<div class="columns" style="align-items: center;">
<div class="kpi-stack" style="flex: 1;">
<div class="kpi-card"><div class="number">87,4 %</div><div class="label">Genauigkeit</div><div class="sub">8.171 von 9.354 richtig</div></div>
<div class="kpi-card hl"><div class="number">16,1 %</div><div class="label">Fehlalarme (FPR)</div><div class="sub">1.031 von 6.417 echten Zitaten</div></div>
<div class="kpi-card"><div class="number">5,2 %</div><div class="label">Fakes übersehen (FNR)</div><div class="sub">152 von 2.937 Fakes</div></div>
</div>
<div style="flex: 1.3;">

<img src="assets/run1-confusion.svg" alt="Confusion Matrix von Run 1" style="width: 100%; display: block;">

</div>
</div>

<p class="note">Run 1 · Prompt v6 · gpt-oss-120b · Browser-use · 02.–09.11.2026 · 5,1 Tage reine Laufzeit, Median 45 s · Fake = positive Klasse</p>

<!--
Das ist die Baseline, mit der wir den Rest vergleichen. Run 1, Prompt v6, alle 9.354 Zitate. Von den 2.937 Fakes erkennen wir 2.785, nur 152 rutschen durch. Die Schwäche sind die 1.031 Fehlalarme: echte Zitate, die wir fälschlich als Fake markieren, 16 Prozent aller echten Zitate.
-->

---

###### 03 · Runvergleich
# Prompt v7.2 senkt die Fehlalarme von 1.031 auf 905

<img src="assets/run1-run2-confusion.svg" alt="Vergleich der Confusion Matrices von Run 1 und Run 2" style="height: 260px; width: auto; max-width: 100%; display: block; margin: -10px auto 4px;">

<div class="grid g3" style="gap: 12px;">
<div class="kpi-card hl"><div class="number">+1,5 pp</div><div class="label">Genauigkeit</div><div class="sub">87,4 % → 88,8 %</div></div>
<div class="kpi-card"><div class="number">−126</div><div class="label">Fehlalarme (FP)</div><div class="sub">1.031 → 905 · McNemar p &lt; 0,001</div></div>
<div class="kpi-card"><div class="number">−12</div><div class="label">übersehene Fakes (FN)</div><div class="sub">152 → 140 · p = 0,39: nicht belegt</div></div>
</div>

<p class="note">Dieselben 9.354 Zitate, gepaart verglichen. Fehlalarme: 424 behoben, 298 neu, 607 in beiden Läufen falsch. Übersehene Fakes: 89 behoben, 77 neu. Exakter McNemar-Test, zweiseitig.</p>

<!--
Gleiche 9.354 Zitate, nur der Prompt ist anders, und wir haben die Einzelfälle beider Läufe. Die Genauigkeit steigt um 1,5 Prozentpunkte, die Fehlalarme sinken um 126. Gepaart (McNemar) ist das klar signifikant. Die übersehenen Fakes gehen nur um 12 zurück, das ist nicht belegbar.
Ehrlich dazu sagen: Netto sind es 126 weniger, aber dahinter stehen 424 behobene und 298 neu falsche echte Zitate. Und 607 Fehlalarme treten in beiden Läufen auf. Überleitung: Was ist zwischen Run 1 und Run 2 anders? Der Prompt. Woher kamen die Änderungen? Aus einer Handanalyse.
-->

---

###### 03 · Handanalyse
# Fünf Muster erklären 12 von 15 Fehlalarmen im Test mit 200 Zitaten

<div class="columns" style="align-items: start;">
<div style="flex: 1.6;">

| Was der Prüfer als Fehler wertete | Warum das kein Fehler ist | Fälle | später mit v7.2 behoben |
| :--- | :--- | :---: | :---: |
| **Frühere Fassung** (arXiv v1, v2) | Dasselbe Werk, andere Version: Doloriel 2025 hat in der aktuellen Fassung 8 weitere Autoren | 6 | **2** |
| **Konferenzjahr oder Jahr des Tagungsbands** | Beide sind üblich: Liu et al., NeurIPS 36 – Konferenz 2023, Tagungsband 2024 | 2 | **1** |
| **Organisation als Autor** | Google Research (Med-Gemini) ist der Autor, keine Person | 2 | **1** |
| **Mitwirkende einer Auflage** | Spirtes et al., MIT Press 2000: weitere Mitwirkende in der Auflage | 1 | **0** |
| **Gesperrte Quelle** | OpenReview hinter Cloudflare, keine Alternative gefunden | 1 | **1** |

</div>
<div class="kpi-stack" style="flex: 0.5;">
<div class="kpi-card hl"><div class="number">5 / 12</div><div class="label">mit v7.2 behoben</div><div class="sub">3 neue Fehlalarme dazugekommen</div></div>
</div>
</div>

<p class="note">Lauf v7.1 auf 200 Zitaten: 15 Fehlalarme, davon 12 mit diesen Mustern und 3 bewusst nicht ausgeglichen. Neu in v7.2: ca-00114, ca-02720, ca-03061.</p>

<!--
Die Handanalyse: 15 Fehlalarme aus dem 200er-Lauf von Hand angeschaut. 12 lassen sich fünf Mustern zuordnen, bei denen der Prüfer etwas als Fehler wertet, das keiner ist. Mit v7.2 sind 5 der 12 behoben, dafür kamen 3 neue Fehlalarme dazu (Captcha, Titel ohne Untertitel, fehlender Autor). Drei weitere gleichen wir bewusst nicht aus, dazu später bei den Messgrenzen. Überleitung: Aus diesen Mustern haben wir Prompt v7.2 abgeleitet.
-->

---

###### 03 · Prompt v7.2
# Prompt v7.2: lockerer bei der Form, strenger bei der Autorenliste

<div class="columns">
<div class="card" style="flex: 1;">

### Neu in v7.2
<p style="margin-bottom: 10px;">Titel, Autoren und Reihenfolge einer <strong>früheren Fassung</strong> sind kein Fehler</p>
<p style="margin-bottom: 10px;"><strong>Organisationen</strong> dürfen Autor von Webseiten, Blogeinträgen, Datensätzen und Software sein</p>
<p><strong>DBLP und Semantic Scholar</strong> vor Status 4 prüfen</p>

</div>
<div class="card red" style="flex: 1;">

### Gegenmaßnahme
<p>Die <strong>vollständige Autorenliste</strong> muss abgeglichen werden, damit die Lockerung keine Fakes durchlässt. Im Test mit 200 Zitaten sinken die übersehenen Fakes von 5 auf 4</p>

</div>
</div>

> Die Regeln antworten auf die fünf Muster der Handanalyse. Im Vollauf sinken die Fehlalarme damit von 1.031 auf 905, aber nicht auf null.

<!--
Das ist der Unterschied zwischen Run 1 und Run 2, abgeleitet aus der Handanalyse. Prompt v7.2 ist lockerer bei der Form: frühere Fassungen und Organisationen als Autor sind kein Fehler, und bei gesperrten Quellen werden erst DBLP und Semantic Scholar geprüft. Als Gegenmaßnahme muss die vollständige Autorenliste abgeglichen werden, damit die Lockerung keine Fakes durchlässt. Im Test mit 200 Zitaten sinken die übersehenen Fakes von 5 auf 4.
-->

---

###### 04 · Warum so viele Fehlalarme?
# Kein Zufall: Zwei Prompts scheitern an denselben Zitaten

<div class="grid g3">
<div class="kpi-card hl"><div class="number">607</div><div class="label">in Run 1 und Run 2 falsch</div><div class="sub">67 % der 905 Fehlalarme in Run 2</div></div>
<div class="kpi-card"><div class="number">424</div><div class="label">nur in Run 1 falsch</div><div class="sub">in Run 2 richtig</div></div>
<div class="kpi-card"><div class="number">298</div><div class="label">nur in Run 2 falsch</div><div class="sub">in Run 1 noch richtig</div></div>
</div>

> Zwei verschiedene Prompts scheitern an **denselben** Zitaten. Das spricht für systematische Ursachen (Zitate, Label oder Verhalten des Modells), nicht für Zufall.

<p class="note">Run 1: 1.031 Fehlalarme = 607 + 424. Run 2: 905 Fehlalarme = 607 + 298. Dieselben 6.417 echten Zitate, gepaart verglichen.</p>

<!--
Erste Antwort auf die Frage vom letzten Mal: Die Fehlalarme sind kein Zufall. 607 von 905 treten in beiden Läufen auf, mit zwei verschiedenen Prompts. Zwischen den Läufen wechseln 424 Zitate zu richtig und 298 zu falsch, netto 126 weniger.
-->

---

###### 04 · Was das Modell behauptet
# Fast immer eine konkrete Abweichung, meist in der Autorenliste

<div class="columns" style="align-items: center;">
<div style="flex: 1.5;">

| Das Modell behauptet … | Fälle | Anteil |
| :--- | ---: | ---: |
| **Status 3 · Inhaltsfehler** | **755** | **83 %** |
| … in der Autorenliste | 396 | 44 % |
| … im Titel | 180 | 20 % |
| … im Jahr | 104 | 11 % |
| … bei Venue oder Seiten | 62 | 7 % |
| … sonstiges | 13 | 1 % |
| **Status 4 · Quelle nicht verifizierbar** | **150** | **17 %** |

</div>
<div class="kpi-stack" style="flex: 0.8;">
<div class="kpi-card hl"><div class="number">83 %</div><div class="label">behaupten einen Inhaltsfehler</div><div class="sub">755 von 905 (Status 3)</div></div>
</div>
</div>

<p class="note">Run 2 (v7.2), 905 FP. Zuordnung automatisch nach dem zuerst genannten Stichwort in der Begründung des Modells, nicht manuell geprüft.</p>

<!--
Was behauptet das Modell bei diesen Fehlalarmen? In 83 Prozent einen konkreten Inhaltsfehler, fast die Hälfte betrifft die Autorenliste: Reihenfolge, fehlende oder zusätzliche Autoren, abweichende Namen. Bei 150 Fällen kann es die Quelle nicht verifizieren, zum Beispiel wegen Cloudflare oder leerer Seiten.
-->

---

###### 04 · Autorenfehler
# Autorenfehler: Das Modell liest oft eine neuere Fassung

<div class="columns" style="align-items: center;">
<div style="flex: 1.3;">

| Vorwurf bei 392 Autoren-Fehlalarmen | Fälle | Anteil |
| :--- | ---: | ---: |
| Autor fehlt im Zitat | 142 | 36 % |
| Namensvariante, Initialen | 92 | 23 % |
| Autor im Zitat, nicht in der Quelle | 79 | 20 % |
| Reihenfolge | 42 | 11 % |
| sonstiges | 37 | 9 % |

</div>
<div class="kpi-stack" style="flex: 1; gap: 10px;">
<div class="kpi-card hl"><div class="number">58 %</div><div class="label">Zitat = arXiv v1</div><div class="sub">23 von 40 geprüften arXiv-Fällen (95 %: 42–72 %)</div></div>
<div class="kpi-card"><div class="number">47 % / 4 %</div><div class="label">letzte Version nach dem Snapshot</div><div class="sub">generated / realworld</div></div>
</div>
</div>

> Neue Autoren seit der Erfassung erklären **nur einen Teil**: bei generated knapp die Hälfte, bei realworld kaum. Der Kern ist allgemeiner: Das Zitat gibt eine **ältere Fassung** wieder, das Modell prüft die neueste.

<p class="note">generated = vom LLM erzeugte Zitate, realworld = Zitate aus echten PDFs, Snapshot = CiteAudit-Stand vom 30.04.2026. Autoren-FP = erster Vorwurf betrifft die Autoren (43 % der 905), Zuordnung per Regeln. 234 von 392 haben eine arXiv-ID, 158 nicht (Journals, Bücher): dort greift Versionsdrift nicht, Ursache nicht geprüft. Stichprobe 40, Seed 1, je Fall v1 und aktuelle Fassung bei arXiv verglichen; 30 % davon sind Modellfehler. <a href="belege/versionsdrift-stichprobe.md">Alle 40 Fälle mit Links</a>.</p>

<!--
Woher kommen die vielen Autorenfehler? Zuerst die Art: In 36 Prozent fehlt laut Modell ein Autor im Zitat, in 23 Prozent geht es um Namensvarianten, in 20 Prozent steht ein Autor im Zitat, der in der Quelle fehlt. Dann die Ursache: Wir haben 40 Fälle mit arXiv-Nummer gegen arXiv geprüft. In 23, also 58 Prozent, entspricht das Zitat genau der ersten Fassung, und die aktuelle Fassung hat andere Autoren. In 30 Prozent hat das Modell dagegen selbst unrecht.
Zur Frage, ob seit der Erfassung neue Autoren dazugekommen sind: Teilweise. Bei den generierten Zitaten hat knapp die Hälfte der Papers ihre letzte Version nach dem Snapshot vom 30. April 2026, bei den realworld-Zitaten nur 4 Prozent. Von den 23 Drift-Fällen liegt bei 8 die Überarbeitung nach dem Snapshot, bei 15 davor. Allgemeiner Kern: Das Zitat ist eine ältere Fassung.
Grenzen: Die 158 Autorenfehler ohne arXiv-Nummer sind nicht erklärt. 40 Fälle sind eine kleine Stichprobe.
-->

---

###### 04 · Stichprobe
# Von 12 geprüften Fehlalarmen lag das Modell 10-mal falsch

<div class="grid g3">
<div class="kpi-card hl"><div class="number">10 / 12</div><div class="label">Modell falsch</div><div class="sub">8 durch Versionsdrift: Zitat = erste Fassung, das Modell prüft die neueste</div></div>
<div class="kpi-card"><div class="number">1 / 12</div><div class="label">Label falsch</div><div class="sub">zu nachsichtig (ca-02988)</div></div>
<div class="kpi-card"><div class="number">1 / 12</div><div class="label">nicht entscheidbar</div><div class="sub">ca-02260</div></div>
</div>

<table style="margin-top: 6px;">
<thead><tr><th>Fall</th><th>Zitat</th><th>Label</th><th>Modell behauptet</th><th>Befund</th></tr></thead>
<tbody>
<tr><td style="white-space: nowrap;"><a href="https://arxiv.org/abs/2512.23365v1"><code>ca‑08875</code></a></td><td>Lee et al., SpatialMosaic, 2025</td><td>Real</td><td>Autorenreihenfolge falsch</td><td>Zitat = arXiv <a href="https://arxiv.org/abs/2512.23365v1">v1</a>, das Modell prüfte die aktuelle Fassung <a href="https://arxiv.org/abs/2512.23365v4">v4</a></td></tr>
<tr><td style="white-space: nowrap;"><a href="https://arxiv.org/abs/2304.06767v1"><code>ca‑02169</code></a></td><td>Dong et al., RAFT, 2023</td><td>Real</td><td>Zwei Autoren fehlen</td><td><a href="https://arxiv.org/abs/2304.06767v1">v1</a> hat 8 Autoren wie zitiert, die <a href="https://arxiv.org/abs/2304.06767">aktuelle Fassung</a> 10</td></tr>
<tr><td style="white-space: nowrap;"><a href="https://doi.org/10.1038/s41586-025-09429-6"><code>ca‑02988</code></a></td><td>Correia et al., BindCraft, 2025</td><td>Real</td><td>Band und Seiten falsch</td><td>Stimmt: <a href="https://doi.org/10.1038/s41586-025-09429-6">Nature 646, 483–492</a>, das Label ist zu nachsichtig</td></tr>
</tbody>
</table>

<p class="note">12 der 607 wiederkehrenden FP (Seed 1, nach Fehlerart geschichtet), je Fall per Webquelle geprüft, Belege: Backup-Folie. Label-Fehler 1/12: 95-%-Intervall 1,5–35 %.</p>

<!--
Wir haben 12 der 607 wiederkehrenden Fehlalarme gegen die Quellen geprüft. In 10 Fällen lag das Modell falsch, in 8 davon wegen Versionsdrift: Das Zitat entspricht genau der ersten arXiv-Fassung, die später überarbeitet wurde, etwa um Autoren ergänzt. Das Modell liest die aktuelle Fassung und meldet einen Fehler. Nach unserer eigenen Regel aus v7.2 wäre das kein Fehler. Nur ein Fall ist ein echter Label-Fehler, BindCraft mit falschem Band. Ehrlich: Das sind 12 Fälle, das Intervall für den Label-Fehleranteil ist breit.
-->

---

###### 04 · Messgrenzen
# Nicht jeder Fehlalarm ist ein Modellfehler: fünf Grenzfälle

<table>
<thead><tr><th>Fall</th><th>Zitat</th><th>Label</th><th>Modell sagt</th><th>Bewertung</th></tr></thead>
<tbody>
<tr><td style="white-space: nowrap;"><a href="https://arxiv.org/abs/2001.08361"><code>ca‑01632</code></a></td><td>Kaplan et al., Scaling laws, 2020</td><td>Real</td><td>Jeffrey Wu fehlt in der Autorenliste</td><td><strong>Modell hat recht</strong>, Label vermutlich falsch</td></tr>
<tr><td style="white-space: nowrap;"><a href="https://arxiv.org/abs/2106.13008"><code>ca‑01851</code></a></td><td>Wu, Wang, Long, Autoformer, 2021</td><td>Real</td><td>Jiehui Xu fehlt in der Autorenliste</td><td><strong>Modell hat recht</strong>, Label vermutlich falsch</td></tr>
<tr><td style="white-space: nowrap;"><a href="https://doi.org/10.7551/mitpress/1754.001.0001"><code>ca‑03078</code></a></td><td>Spirtes et al., MIT Press, 2000</td><td>Real</td><td>Heckerman fehlt, Jahr 2001</td><td>Offen: laut Doku Mitwirkender der 2. Auflage, an der Quelle prüfen</td></tr>
<tr><td style="white-space: nowrap;"><a href="https://doi.org/10.1007/978-1-4471-0211-3"><code>ca‑03060</code></a></td><td>d’Avila Garcez et al., Springer, 2012</td><td>Real</td><td>Erstausgabe 2002, kein Beleg für 2012</td><td>Offen: Nachdruck 2012, an der Quelle prüfen</td></tr>
<tr><td style="white-space: nowrap;"><code>ca‑00997</code></td><td>„Revolutionizing data …“, 2024, ohne Autoren</td><td>Real</td><td>Keine passende Quelle gefunden (v7.1)</td><td>Offen: Quelle auch von uns nicht auffindbar (arXiv, Crossref)</td></tr>
</tbody>
</table>

<p class="note">ca-01632 und ca-01851 gleichen wir bewusst nicht aus: Ein fehlender Autor bleibt ein Inhaltsfehler, auch wenn CiteAudit „Real“ sagt.</p>

<!--
Nicht jeder Fehlalarm ist ein Fehler des Modells. Bei den ersten zwei liegt vermutlich das Label falsch: Ein Autor fehlt tatsächlich in der Zitierung. Zwei weitere beruhen auf bibliografischem Vorwissen und müssen noch an der Quelle bestätigt werden. Beim fünften (ca-00997) haben auch wir die Quelle nicht gefunden, er bleibt offen.
-->

---

###### 05 · Ausblick
# Nächste Schritte

<div class="steps">
<div class="step-item active" style="border: 1.5px solid rgba(226, 0, 26, 0.4);">
<div class="step-num" style="color: var(--red); font-weight: 700;">01 · Als Nächstes</div>
<div class="step-title" style="color: var(--red);">Versionsprüfung erzwingen</div>
<div class="step-desc">Bei arXiv und bioRxiv die Versionsliste abrufen und vor Status 3 gegen v1 abgleichen (Prompt v7.3)</div>
</div>
<div class="step-item">
<div class="step-num">02</div>
<div class="step-title">Label-Fehler belegen</div>
<div class="step-desc">Stichprobe auf 50–100 FP vergrößern, belegte Fälle als Revisionsdatei führen, Kennzahlen mit und ohne Korrektur</div>
</div>
<div class="step-item">
<div class="step-num">03</div>
<div class="step-title">Modelle und Agenten vergleichen</div>
<div class="step-desc">Qwen3.8, Hermes, OpenCode auf denselben Zitaten, getrennt nach realworld und generated (CE-40, CE-41)</div>
</div>
<div class="step-item">
<div class="step-num">04</div>
<div class="step-title">Zugriff</div>
<div class="step-desc">WebUI mit Login statt SSH (CE-32, CE-34)</div>
</div>
</div>
</div>

<!--
Schluss: Wir wissen jetzt, wo der Prüfer irrt. Als Nächstes die 905 Fehlalarme systematisch auswerten und Modelle auf denselben Zitaten vergleichen. Danach Fragen.
-->

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

###### Backup · Belege Stichprobe
# Alle 12 geprüften Fehlalarme mit Quelle

<style scoped>
table { font-size: 14px; }
th, td { padding: 4px 10px; }
</style>

| Fall | Modell behauptet | Befund | Beleg |
| :--- | :--- | :--- | :--- |
| `ca‑01252` | Penzar fehlt, Titel weicht ab | Versionsdrift | [bioRxiv v1](https://www.biorxiv.org/content/10.1101/2023.06.12.544594v1) |
| `ca‑08875` | Reihenfolge falsch | Versionsdrift | [arXiv v1](https://arxiv.org/abs/2512.23365v1) · [v4](https://arxiv.org/abs/2512.23365v4) |
| `ca‑00599` | Filippas, Manning fehlen | Versionsdrift (NBER-Erstausgabe nicht direkt belegt) | [arXiv v1](https://arxiv.org/abs/2301.07543v1) · [NBER](https://www.nber.org/papers/w31122) |
| `ca‑02169` | Zwei Autoren fehlen | Versionsdrift | [arXiv v1](https://arxiv.org/abs/2304.06767v1) · [aktuell](https://arxiv.org/abs/2304.06767) |
| `ca‑01124` | 4 Autoren fehlen | Versionsdrift | [arXiv v1](https://arxiv.org/abs/2402.01788v1) |
| `ca‑07418` | Titel weicht ab, Koautoren fehlen | Versionsdrift | [arXiv v1](https://arxiv.org/abs/2512.18542v1) |
| `ca‑08703` | Titel weicht ab | Versionsdrift | [arXiv v1](https://arxiv.org/abs/2512.22777v1) |
| `ca‑06604` | Titel weicht ab | Versionsdrift | [arXiv v1](https://arxiv.org/abs/2601.00396v1) |
| `ca‑02809` | 1995 statt 1993 | Modell falsch (Clarendon Press 1993) | [Cambridge](https://www.cambridge.org/core/journals/language-in-society/article/abs/carol-myersscotton-social-motivations-for-codeswitching-evidence-from-africa-oxford-studies-in-language-contact-oxford-clarendon-1993-pp-xii-177-hb-3500/41026149A62638461EDEDADD3EB73D8A) |
| `ca‑00765` | Gehört zu keiner Reihe | Modell falsch (Bd. 56 der Reihe Texts in Applied Mathematics) | Link nicht abrufbar |
| `ca‑02260` | 2022 statt 2023 | nicht entscheidbar | [Zenodo](https://zenodo.org/records/7421784) |
| `ca‑02988` | Band und Seiten falsch | Label zu nachsichtig | [Nature, DOI](https://doi.org/10.1038/s41586-025-09429-6) |

<p class="note">Selbst nachgeprüft: ca‑08875, ca‑02169, ca‑02988 (Autorenlisten und Versionen bei arXiv, Band und Seiten über Crossref). Übrige Fälle nach der Prüfung durch einen Hilfs-Agenten, die Links sind erreichbar, Inhalte nicht einzeln von mir kontrolliert.</p>

---

###### Backup · Spark
# Die Spark überhitzt nicht mehr: Wachhund statt Dauerlast

<div class="grid g3">
<div class="kpi-card hl"><div class="number">85 °C</div><div class="label">Pause</div><div class="sub">keine neuen Versuche</div></div>
<div class="kpi-card"><div class="number">70 °C</div><div class="label">automatisch weiter</div><div class="sub">Hysterese gegen Flackern</div></div>
<div class="kpi-card"><div class="number">90 °C</div><div class="label">Abbruch</div><div class="sub">Pause bleibt bis zur manuellen Freigabe</div></div>
</div>

<div class="grid g2" style="margin-top: 16px;">
<div class="card">

### Regeln
<p style="margin-bottom: 10px;">Gemessen wird die <strong>heißeste Thermal-Zone</strong>, nicht nur die GPU</p>
<p style="margin-bottom: 10px;">Abbruch auch, wenn sich die GPU <strong>selbst drosselt</strong></p>
<p style="margin-bottom: 10px;">Nur <strong>ein</strong> schwerer Job gleichzeitig, erst eine <strong>10-Minuten-Probe</strong></p>

</div>
<div class="card">

### In der Evaluation
<p style="margin-bottom: 10px;">Der Wachhund liest die Temperatur per SSH und <strong>pausiert die Vergabe</strong> neuer Versuche an die Spark</p>
<p style="margin-bottom: 10px;"><strong>Mehrere Worker je Server</strong> sind einstellbar, Start mit 2 und Temperatur beobachten</p>

</div>
</div>

<p class="note">Herkunft: tools/spark-thermo (BeeHive-Projekt), dort zusätzlich Bremse im Training (halbe Rechenzeit, Pause ab 75 °C). In der Evaluation steuert der Wachhund nur die Vergabe, laufende Versuche enden regulär. Temperaturmessungen vorher/nachher liegen hier nicht vor.</p>

<!--
Backup, falls nach den Spark-Ausfällen gefragt wird. Die Spark ist zweimal überhitzt. Lösung aus dem BeeHive-Projekt: ein Wachhund misst die heißeste Thermal-Zone, pausiert ab 85 Grad, macht unter 70 Grad weiter und bricht ab 90 Grad ab. In der Evaluation ist das als Hitzeschutz in der Ablaufsteuerung eingebaut. Zusammen mit mehreren Workern je Server können wir die Spark gezielt auslasten, ohne sie zu überhitzen. Noch nicht belegt: Messwerte vorher/nachher.
-->

---

###### Backup · Metriken
# Accuracy und F1 messen Verschiedenes

<div class="columns" style="align-items: start;">
<div class="card" style="flex: 1.1;">

### Formeln (Fake = positive Klasse)
<p style="margin-bottom: 8px;"><strong>Accuracy</strong> = <code>(TP + TN) / (TP + TN + FP + FN)</code></p>
<p style="margin-bottom: 8px;"><strong>Precision</strong> = <code>TP / (TP + FP)</code></p>
<p style="margin-bottom: 8px;"><strong>Recall</strong> = <code>TP / (TP + FN)</code></p>
<p style="margin-bottom: 8px;"><strong>F1</strong> = <code>2 · P · R / (P + R)</code></p>
<p style="margin-left: 38px;">= <code>2 · TP / (2 · TP + FP + FN)</code></p>

</div>
<div style="flex: 1;">

| | Run 1 (v6) | Run 2 (v7.2) |
| :--- | ---: | ---: |
| Accuracy | 87,4 % | 88,8 % |
| Precision | 73,0 % | 75,6 % |
| Recall | 94,8 % | 95,2 % |
| **F1** | **82,5 %** | **84,3 %** |

</div>
</div>

> Accuracy zählt auch die richtig erkannten echten Zitate (TN). F1 ignoriert sie und zeigt, wie gut die **Fakes** gefunden werden, ohne zu viele Fehlalarme.

<p class="note">Nur 31 % der 9.354 Zitate sind Fakes. „Immer Real“ erreicht 68,6 % Accuracy, aber F1 = 0. Die Fehlalarme (FP) senken die Precision, deshalb liegt F1 unter der Accuracy.</p>

<!--
Accuracy ist der Anteil aller richtig klassifizierten Zitate. F1 ist das harmonische Mittel aus Precision und Recall für die Klasse Fake, die richtig erkannten echten Zitate zählen dort nicht mit. Weil nur 31 Prozent der Zitate Fakes sind, wäre "immer Real" schon 68,6 Prozent Accuracy, aber F1 null. Der niedrigere F1-Wert zeigt, dass die Fehlalarme die Precision drücken: Recall 95 Prozent, Precision 73 bis 76 Prozent.
-->

---

###### Backup · Statistik
# McNemar-Test: gepaarter Vergleich von Run 1 und Run 2

<div class="columns" style="align-items: center;">
<div style="flex: 1.5;">

| Klasse | Run 2 behoben (b) | Run 2 neu falsch (c) | p |
| :--- | ---: | ---: | ---: |
| Fehlalarme (6.417 echte) | 424 | 298 | **&lt;&nbsp;0,001** |
| Übersehene Fakes (2.937) | 89 | 77 | 0,39 |
| Gesamt (9.354) | 513 | 375 | **&lt;&nbsp;0,001** |

</div>
<div class="card" style="flex: 1;">

### Warum McNemar?
<p style="margin-bottom: 10px;">Beide Läufe prüfen <strong>dieselben 9.354 Zitate</strong>, die Messungen sind gepaart</p>
<p>Nur Zitate mit geändertem Ergebnis tragen Information. Wäre der Prompt egal, wären „behoben“ und „neu falsch“ <strong>gleich häufig</strong></p>

</div>
</div>

<div class="card" style="margin-top: 14px;">
<p style="margin-bottom: 6px;">Exakt: <code>p = 2 · Σ<sub>i=0…min(b,c)</sub> C(b+c, i) / 2<sup>b+c</sup></code></p>
<p>Näherung: <code>χ² = (b − c)² / (b + c)</code> · Fehlalarme: χ² = 126² / 722 ≈ 22,0 (1 Freiheitsgrad)</p>
</div>

<p class="note">Exakter Binomialtest, zweiseitig (p ≈ 3 · 10⁻⁶ bei den Fehlalarmen). Bonferroni (α = 0,025) ändert nichts am FP-Befund. Grenze: je Prompt nur ein Lauf, Modellrauschen nicht gemessen.</p>

<!--
Backup, falls nach dem Signifikanztest gefragt wird. McNemar ist der passende Test, weil beide Läufe dieselben 9.354 Zitate bewerten. Wir zählen nur die Zitate, bei denen sich das Ergebnis zwischen Run 1 und Run 2 ändert. Bei den echten Zitaten sind das 424, die jetzt richtig sind, und 298, die jetzt falsch sind. Wäre der Prompt egal, müssten die beiden Zahlen etwa gleich groß sein, das testen wir mit einem exakten Binomialtest. Ergebnis: p ungefähr 3 mal 10 hoch minus 6. Bei den übersehenen Fakes 89 gegen 77, p gleich 0,39, kein belegter Unterschied.
Grenze offen nennen: Wir haben je Prompt nur einen Lauf. Wie stark ein Lauf mit demselben Prompt von selbst schwankt, haben wir nicht gemessen. Das 298-neu-falsch deutet an, dass dieses Rauschen nicht klein ist.
-->
