---
date: 2026-10-20
updated: 2026-10-20
project_id: citeaudit
project_title: "CiteAudit"
title: "GUI-Kurzanleitung"
topic: "Bedienung und Bedeutung aller UI-Kacheln"
type: documentation
tags: [projekt/citeaudit, thema/webentwicklung, typ/documentation]
status: review
---
# CiteAudit: GUI-Kurzanleitung

Die Oberfläche startet Literaturprüfungen und untersucht gespeicherte Ergebnisse. **Preview Dataset** ist der Demo-Run vom 18.10.2026, 22:50: 200 erhaltene Originalversuche mit ergänzter Mock-Telemetrie und 400 synthetische Vergleichsversuche. Mock-Werte beschreiben keine gemessene Modellleistung. Die Originaldaten bleiben getrennt erhalten.

## Einstieg, Seitenleiste und Kopfzeile

| Element | Funktion |
| --- | --- |
| **New run / Neuer Lauf** | Modelle, Agenten und Datensatz wählen; binäre Bewertung, Wiederholungen und Zeitlimit einstellen; Evaluation starten. Dafür werden echte konfigurierte Profile benötigt. Mock-Serveranzeigen stellen keine Verbindung her. |
| **Overview / Übersicht** links | Ergebnisse des gewählten Runs: Fortschritt, Qualitätsübersicht, Matrizen und Versuchstabelle. Nicht mit dem gleichnamigen Analyse-Reiter verwechseln. |
| **Analysis / Analyse** links | Die fünf unten erläuterten Analysebereiche. |
| **Runs / Läufe** | Run auswählen oder nach Name, ID, Modell und Agent suchen. Ausblenden entfernt ihn aus der Anzeige, löscht aber keine Ergebnisdaten. |
| **Pause / Fortsetzen** | Neue Starts pausieren beziehungsweise ausstehende Versuche fortsetzen. Aktive Versuche werden durch Pause nicht sofort beendet. |
| **Agents and models** | Erreichbare Server, geladene Modellinstanzen und Docker-Worker; Details über den Aufklappbereich. Im Preview Dataset sind alle Kapazitätsangaben ausdrücklich Mock. Ein konfiguriertes Profil beweist keine erreichbare oder geladene Instanz. |
| **Appearance** | Hell, Dunkel, Pink Glass oder Systemdesign; Liquid Glass und Animationen ein-/ausschalten; DE/EN/FR/ES. Präferenzen gelten im jeweiligen Browser. Systemvorgaben für reduzierte Bewegung/Transparenz haben Vorrang. |
| **Account** | Profil, Nutzung, Datenschutz, Warteschlange und berechtigte Administration. Lokale Nutzung kann den ausgewählten Run oder alle gespeicherten Runs nach Lauf und Modell zusammenfassen; Laden ist abbrechbar. Kontenansichten/Demorollen ersetzen keine echte Anmeldung oder Serverrechte. |
| **⚙ Konfiguration** | Konfidenzniveau, Parallelität, Zufallsstartwert und Docker-Worker. Browser-use nutzt das Zeitlimit seines Profils; das native CLI-Zeitlimit betrifft Hermes/OpenCode. Serveraktionen brauchen die entsprechende lokale Anbindung. |
| **Help / Statusmeldungen** | Bedienhinweise, fehlende Verbindungen und erneuter Verbindungsversuch. Ein Strich bedeutet unbekannt, nicht null Verbrauch oder unbegrenzte Kapazität. |

## Versuchstabelle und Run-Übersicht

Die Fortschrittsanzeige unterscheidet wartende, laufende, abgeschlossene, fehlgeschlagene und unterbrochene Versuche. Restzeiten sind Schätzungen. Technischer Abschluss und fachlich richtige Antwort sind getrennte Größen.

Die Tabelle lässt sich nach Modell, Agent, Zustand und Ergebnis filtern, durchsuchen und nach Fall oder Dauer sortieren. Filter zurücksetzen stellt die vollständige Auswahl wieder her; der CSV-Download übernimmt die Tabellenfilter. Eine Zeile öffnet Details mit Quelle, Antwort, Referenz, Bewertung, Fehlern, Laufzeiten, Tokens und Rohantwort/JSON-Vergleich.

## Die fünf Analyse-Kacheln

| Reiter | Was er zeigt und wofür er gedacht ist |
| --- | --- |
| **Overview** | Einstieg in die Analyse: gewählte Kennzahl, Datenmenge, Frage/Vergleichsbasis, Bestehensquoten, Gruppenmittelwerte und Diagramm. Vor der Interpretation Modellpaar, gemeinsame Zitate und Messabdeckung prüfen. |
| **Quality** | Fachliche Qualität: Bestehensquote, Konfusionsmatrix, Präzision, Recall, F1 und weitere Klassifikationswerte. Generations- oder Tokenmittelwerte werden hier nicht als Qualitätskennzahlen ausgegeben. |
| **Runtime & resources** | Zeiten, Wartezeit, Generationsgeschwindigkeit und Token-/Kostensummen. Bei ausgewählter Qualitätskennzahl zeigt der Laufzeit-Scatter die Wartezeit/Dauer; für eigene Zeit- oder Tokenverteilungen die Kennzahl oben umstellen. |
| **Model comparison** | Modell-/Agentenkonfiguration A gegen B, gepaarte Differenzen, gemeinsame Fälle, Intervalle und vorhandene Vergleichstests. Positives A−B bedeutet größer, nicht automatisch besser. |
| **Methodology & data** | Datenbasis, Zustände, JSON-Export, deskriptive Detailtabellen, Testvoraussetzungen, verfügbare/ungeeignete Methoden und fachliche Einschränkungen. Ein berechneter p-Wert bestätigt keine ungeprüfte Voraussetzung. |

Reiter ohne passende Datengrundlage erscheinen **grau mit 🔒** und werden bei der Tastaturnavigation übersprungen. Das Preview Dataset enthält Daten für alle fünf Bereiche. Einzelne statistische Verfahren können trotzdem wegen ihrer Voraussetzungen nicht verfügbar oder nur eingeschränkt interpretierbar sein.

## Bedeutung der Zahlenkacheln

| Kachel / Kennzahl | Bedeutung |
| --- | --- |
| **Assessment pass rate** | Fachlich richtige Antworten unter bewertbaren Abschlüssen. Binär zählt die richtige Problementscheidung; im vollständigen Modus die vollständig richtige Feldbewertung. Fehlgeschlagene Versuche werden dadurch nicht als richtige Antworten gezählt. |
| **Technical success / Fehlerquote** | Technisch abgeschlossene beziehungsweise fehlgeschlagene Versuche, getrennt von fachlicher Richtigkeit. |
| **Accuracy / Problemerkennung** | Anteil richtiger Klassifikationen. Im binären Benchmark gelten Status 1–2 als kein Problem, 3–4 als Problem. |
| **Precision / Recall / F1** | Präzision: richtige unter gemeldeten Problemen. Recall: gefundene unter tatsächlich problematischen Quellen. F1 verbindet beides. Bei Makro-Werten werden Klassen gleich gewichtet. |
| **FPR / FNR** | FPR: Fehlalarme unter unproblematischen Referenzen. FNR: übersehene Probleme unter problematischen Referenzen. Die Nenner unterscheiden sich. |
| **Balanced accuracy / MCC / Kappa** | Gleichgewichtete Trefferquote der Referenzklassen, binäre Zusammenhangsstärke beziehungsweise Übereinstimmung unter Berücksichtigung zufälliger Treffer. Fehlende Klassen/undefinierte Nenner bleiben unbekannt. |
| **Status / Autor / Titel / Jahr / Fehlerzahl** | Einzelne Bewertungsaspekte des vollständigen Modus. Im binären Run stehen diese Feldprüfungen nicht vollständig zur Verfügung. |
| **Mean / Median / Quantile / IQR** | Mittelwert, mittlerer Wert, Verteilungsschwellen wie P90/P95/P99 und Abstand zwischen oberem/unterem Quartil. Immer Fall-/Versuchszahl mitlesen. |
| **CI / Konfidenzintervall** | Unsicherheitsbereich für die bezeichnete Quote, den Mittelwert oder die Paardifferenz; kein Bereich aller Einzelwerte. |
| **Paired difference / Effekt / p / Holm** | Unterschied auf gemeinsamen Zitaten, Effektmaß, Test-p-Wert und gegebenenfalls Korrektur innerhalb der bezeichneten Testfamilie. Kein Beweis allgemeiner Modellüberlegenheit. |
| **Adapter / Queue / End-to-end** | Adapterlaufzeit, Wartezeit vor dem Adapterstart und deren Summe. Keine direkte GPU-Auslastung oder reine Modellzeit. |
| **Generation / Tokens/s** | Gemeldete Generationsdauer und -rate. Fehlende Messungen werden erklärt, nicht als null ausgegeben. Im Preview Dataset konservative Mock-Ergänzungen. |
| **Input / Output / Thinking** | Eingabe-, Ausgabe- und Denktokens. Thinking wird nur bei bestätigter separater Erfassung zusätzlich bepreist. Die Demo kennzeichnet ihre geschätzten Werte ausdrücklich. |
| **Total tokens / Kosten** | Gesamttokens zählen Input+Output desselben Versuchs, wenn beide vorliegen. Thinking ist separat. Kosten verwenden lokale Beispielpreise und bekannte Bestandteile; sie sind keine Providerrechnung. Preise lassen sich im Ressourcenbereich ändern/zurücksetzen. |
| **Exa limits / Messabdeckung** | Betroffene Versuche/Ereignisse der Exa-Telemetrie beziehungsweise verfügbare und ausgeschlossene Messungen. Unbekannt bleibt unbekannt. |

## Die zwölf Diagramme

| Diagramm | Verwendung |
| --- | --- |
| **Boxplot** | Verteilung mit Quartilen, Median und Einzelwerten. |
| **Histogramm** | Häufigkeiten in Wertebereichen; gepoolt oder gruppiert. |
| **ECDF** | Anteil der Beobachtungen bis zu einem Wert; große Vorschauen können ausgedünnt sein. |
| **Outcomes** | Technische Versuchszustände je Konfiguration. |
| **Confusion matrix** | Referenzklassen gegen Modellklassen, einschließlich Fehlalarmen und übersehenen Problemen. |
| **Scatter** | Zusammenhang zwischen Wartezeit und Adapterdauer. |
| **Timeline** | Zeitlicher Verlauf der gewählten Evaluation. |
| **Pairs** | A/B-Werte derselben Zitate. |
| **Forest** | Gruppenmittelwerte mit vorhandenen Unsicherheitsintervallen. |
| **Differences** | Verteilung der gepaarten A−B-Differenzen. |
| **Directions** | Anzahl positiver, negativer und gleicher Paardifferenzen. |
| **Quantiles** | Median und weitere Verteilungsschwellen je Konfiguration. |

## Filter, Exporte und offene Anbindungen

Oben werden Kennzahl, A/B-Vergleich, Konfidenzniveau und gegebenenfalls gemessene Zeiten fehlgeschlagener Versuche gewählt. **Refresh statistics** lädt einen neuen Statistikstand; der angezeigte Stand ist ein Snapshot. Einzelversuche und Zitatmittelwerte sind unterschiedliche Beobachtungseinheiten; Vergleichstests verwenden gemeinsame Zitate.

**Visible configurations** filtert Diagramme und deren Datenexport. Kennzahlen und Tests behalten ihre vollständige Basis; die Timeline umfasst die ganze Evaluation. SVG exportiert die Grafik, CSV die bezeichneten Diagramm-/Tabellendaten, JSON den Statistikreport. Mock-Provenienz bleibt im Export erhalten.

Echte Anmeldung, Sitzungen, Kontenpersistenz, Benutzer-/Datenschutzaktionen, durchgesetzte Quoten/Fair Queue und Live-Modellstatus benötigen noch die entsprechenden Backend-Anbindungen. Vorbereitete Ansichten, Demorollen und Mock-Werte sind keine Umsetzung dieser Serverfunktionen.

Für die Demo: **Preview Dataset wählen → Overview → Quality → Runtime & resources → Model comparison → Methodology & data**. Bei jeder Zahl zuerst Datenquelle, Nenner, Beobachtungseinheit und Mock-Markierung prüfen.

Details: Methodische Detaildefinitionen und der Kontenvertrag liegen im CiteAudit-Projekt unter docs/STATISTICS_METHODS.md und frontend/multiuser/README.md.
