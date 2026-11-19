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

---

###### Überblick
# Agenda

<div class="agenda">
<div><span>01</span>Projektstand</div>
<div><span>04</span>Fehlalarme & Prompt v7.2</div>
<div><span>02</span>RTX 6000 & Laufzeit</div>
<div><span>05</span>Ergebnis-UI</div>
<div><span>03</span>Läufe v7.1, v7.2 und Vollauf</div>
<div><span>06</span>Ausblick</div>
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

---

###### 01 · Projektstand · jetzt
# Vollauf abgeschlossen, Analyse läuft weiter

<div class="board" style="grid-template-columns: repeat(5, 1fr); gap: 12px;">
<div class="board-col compact">
<div class="board-head">Backlog <span>6</span></div>
<div class="board-card"><b>CE-30</b>DSGVO & Recht</div>
<div class="board-card"><b>CE-31</b>Statistische Tests</div>
<div class="board-card"><b>CE-33</b>CLI ausbauen</div>
<div class="board-card"><b>CE-28</b>Multi-User-Zugriff</div>
<div class="board-card"><b>CE-34</b>WebUI mit Login</div>
<div class="board-card"><b>CE-32</b>WebUI statt SSH</div>
</div>
<div class="board-col compact">
<div class="board-head">To Do <span>0</span></div>
</div>
<div class="board-col compact">
<div class="board-head">In Arbeit <span>2</span></div>
<div class="board-card"><b>CE-25</b>Judgement Calls & parallele Worker</div>
<div class="board-card"><b>CE-24</b>Präsentation mit Marp</div>
</div>
<div class="board-col compact">
<div class="board-head">In Review <span>0</span></div>
</div>
<div class="board-col compact">
<div class="board-head">Erledigt <span>7</span></div>
<div class="board-card done"><b>CE-21</b>Rechenleistung angefragt</div>
<div class="board-card done"><b>CE-22</b>RTX 6000 für Vollauf genutzt</div>
<div class="board-card done"><b>CE-23</b>Kategoriendefinition v7.2 getestet</div>
<div class="board-card done"><b>CE-26</b>Ergebnis-UI verbessert</div>
<div class="board-card done"><b>CE-29</b>Modellserver im Vollauf stabil</div>
<div class="board-card done"><b>Vollauf</b>9.354 Antworten, 0 fatale Fehler</div>
<div class="board-card done"><b>Bugfix</b>Chromium-Zombieprozesse behoben</div>
</div>
</div>

<p class="note">Offen bleiben insbesondere die statistische Auswertung und die noch geplanten Zugriffs-/CLI-Funktionen. Run 2 liegt hier aggregiert vor, nicht als Einzelfalldatensatz.</p>

---

###### 02 · Hardware
# Läufe auf der RTX 6000 statt auf der Spark

<div class="grid g3">
<div class="kpi-card"><div class="number">9.354 / 9.354</div><div class="label">gültige Antworten je Vollauf</div><div class="sub">0 fatale Fehler · Chromium-Zombieprozesse behoben</div></div>
<div class="kpi-card hl"><div class="number">2</div><div class="label">Vollläufe mit je 9.354 Zitaten</div><div class="sub">Run 1 mit Prompt v6 · Run 2 mit v7.2</div></div>
<div class="kpi-card"><div class="number">gpt-oss-120b</div><div class="label">auf dem RTX6000-Server</div><div class="sub">Browser-use · 600 s Timeout je Zitat</div></div>
</div>

> Die Spark-Ausfälle sind kein Risiko mehr: **Beide Vollläufe** liefen auf der RTX 6000 durch.

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
# Von 200 Zitaten zum Vollauf mit 9.354

<div class="columns" style="align-items: center;">
<div style="flex: 1.5;">

| Lauf | Prompt | Zitate | Genauigkeit | FPR | FNR |
| :--- | :--- | ---: | ---: | ---: | ---: |
| 28.10. | v7.1 | 200 | 90,0 % | 15 % | 5 % |
| 28.10. | v7.2 | 200 | **91,5 %** | **13 %** | **4 %** |
| 29.10. – 16.11. | v7.2 | **9.354** | 88,8 % | 14,1 % | 4,8 % |

</div>
<div class="kpi-stack" style="flex: 0.6;">
<div class="card"><p>Dieselben <strong>200 Zitate</strong> in Zeile 1 und 2: v7.2 ist <strong>leicht besser</strong></p></div>
<div class="card red"><p>Nur <strong>2 Fälle</strong> Unterschied bei FP, 1 bei FN: statistisch noch <strong>nicht belastbar</strong></p></div>
</div>
</div>

<p class="note">gpt-oss-120b · RTX 6000 · Browser-use · binärer Benchmark (Fake = positive Klasse) · FPR/FNR: Falsch-positiv-/Falsch-negativ-Rate</p>

---

###### 03 · Vollauf
# 9.354 Zitate vollständig geprüft

<div class="columns" style="align-items: center;">
<div class="kpi-stack" style="flex: 1;">
<div class="kpi-card hl"><div class="number">88,8 %</div><div class="label">Genauigkeit</div><div class="sub">8.309 von 9.354 richtig</div></div>
<div class="kpi-card"><div class="number">4,8 %</div><div class="label">Fakes übersehen</div><div class="sub">140 von 2.937 Fakes</div></div>
</div>
<div style="flex: 1.3;">

| | Vorhersage Fake | Vorhersage Real |
| :--- | :---: | :---: |
| **Fake** (2.937) | 2.797 | 140 |
| **Real** (6.417) | 905 | 5.512 |

</div>
</div>

> Die Fakes werden fast alle erkannt. Das Problem sind die **905 Fehlalarme** (14,1 % der echten Zitate).

<p class="note">Lauf fb3ebb05 · Prompt v7.2 · 18 Tage Kalenderzeit mit Pausen, rund 5,5 Tage reine Laufzeit bei einem Worker (9.354 × 51 s)</p>

---

###### 03 · Runvergleich
# Run 2 senkt Fehlalarme bei gleicher Fallzahl

<img src="assets/run1-run2-confusion.svg" alt="Vergleich der Confusion Matrices von Run 1 und Run 2" style="height: 260px; width: auto; max-width: 100%; display: block; margin: -10px auto 4px;">

<div class="grid g3" style="gap: 12px;">
<div class="kpi-card hl"><div class="number">+1,5 pp</div><div class="label">Genauigkeit</div><div class="sub">87,4 % → 88,8 %</div></div>
<div class="kpi-card"><div class="number">−126</div><div class="label">Fehlalarme (FP)</div><div class="sub">1.031 → 905</div></div>
<div class="kpi-card"><div class="number">−12</div><div class="label">übersehene Fakes (FN)</div><div class="sub">152 → 140</div></div>
</div>

<p class="note">Beide Läufe: dieselben 9.354 case_ids. Run 1 aus attempts.csv; Run 2 aus den gemergten Vollauf-Aggregaten. Für Run 2 liegen hier keine Einzelfalldaten vor, daher kein fallweiser Signifikanztest.</p>

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

> Auf denselben 200 Zitaten ist v7.2 leicht besser als v7.1 (91,5 % gegenüber 90,0 %). Der Vollauf zeigt: 905 Fehlalarme bleiben.

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
* **Live-Dashboard** mit Laufzeitprognose und Export

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
<div class="step-title" style="color: var(--red);">905 Fehlalarme analysieren</div>
<div class="step-desc">Muster im Vollauf finden, Prompt nachschärfen</div>
</div>
<div class="step-item">
<div class="step-num">02</div>
<div class="step-title">Auswertung je Quelltyp</div>
<div class="step-desc">Statistische Tests, Konfidenzintervalle, Label-Fehler im Benchmark prüfen</div>
</div>
<div class="step-item">
<div class="step-num">03</div>
<div class="step-title">Modelle und Agenten vergleichen</div>
<div class="step-desc">Qwen3.8, Hermes, OpenCode auf denselben Zitaten</div>
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
