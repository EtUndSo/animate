# Koordination: wie der Haupt-Agent Schreib- und Übersetzungs-Agenten führt

Gilt für alle Heftreihen: Cybersecurity, Machine Learning, Programmieren, Linux und die Uni-Module bei ihrer Überarbeitung. Der Haupt-Agent schreibt selbst keine Hefte, er plant, beauftragt, prüft und berichtet. Der Arbeitsstand je Reihe steht in `zusatzreihen_stand.md` bzw. `ueberarbeitung_stand.md`.

## Wer gleichzeitig arbeiten darf
- **Schreiben:** höchstens ein Schreib-Agent zur Zeit, immer auf Opus (`model: "opus"`). Seit 09.11.2026 entsteht jedes Heft in **zwei Phasen mit je einem frischen Agenten**, nacheinander, siehe unten.
- **Übersetzen:** parallel dazu höchstens ein Übersetzungs-Agent, nur für endgültige Hefte.
  - Er arbeitet nach `notizen/heft_uebersetzung.md` und dem Brief mit Glossar `notizen/uebersetzung_brief_zusatzreihen.md`, entstanden bei Grundlagen 2.
  - Er prüft jede Datei mit `python tools/uebersetzung_struktur_check.py <de.tex> <L.tex> <L>`.
  - Er verteilt die Dateien nacheinander an einzelne Hilfsagenten, weil ein Heft in fünf Sprachen nicht in einen Kontext passt.
  - Neue Fachbegriffe trägt er ins Glossar des Briefs ein, damit spätere Hefte sie gleich übersetzen.
- **Recherche:** Unteragenten höchstens 3 gleichzeitig, immer auf Sonnet, nur zum Suchen und Exzerpieren.
- **Programmieren am Werkzeug** (Editor, Konverter, Website): ein eigener Agent, der die Dateien der Schreib-Agenten nicht anfasst. Gemeinsam benutzte Werkzeuge hält er jederzeit lauffähig.

## Zwei Phasen je Heft (seit 09.11.2026)
Der User: „wir müssen den Verbrauch senken ohne dabei die Qualität zu beeinflussen“. Ein Heft-Agent kam auf 0,8 bis 1 Million Tokens Kontext. Den größten Teil bezahlte die Schlussphase: viele kleine Schritte (PDF bauen, prüfen, Kleinigkeit ändern, Szene exportieren), jeder mit dem ganzen Kontext samt Quellen. Deshalb:
1. **Schreib-Agent (Phase 1):** liest die Quellen ganz, recherchiert, schreibt das Heft samt Lösungen, TikZ-Abbildungen, Code und `rechnung_kap<N>.py`. Den Code testet er beim Schreiben. Zum Schluss schreibt er die Übergabe `uebergabe_kap<N>.md` und berichtet. PDF, Szenen und Konverter macht er nicht.
2. **Prüf-Agent (Phase 2), frisch gestartet:** liest Auftrag, Leitfaden, WISSEN-Datei des Hefts, Übergabe, die Zusammenfassungen der früheren Hefte und das ganze Heft samt Lösungen. Dann:
   - Satz-für-Satz-Prüfung nach UEBERARBEITUNG §7 und Korrekturen;
   - Beispiele und Wortwahl (§2b): keine Elektrotechnik außerhalb der ET-Module, keine seltenen oder komisch klingenden Wörter;
   - PDF und `pdf_pruefen.py`;
   - Abgleich aller Code-Blöcke mit echter Ausführung;
   - Editor-Szenen mit Kontaktblatt;
   - Konverter und Themenkarte;
   - `zusammenfassung_kap<N>.md` und Bericht.

   Seine frischen Augen sind zugleich eine unabhängige Durchsicht. Die Quellen braucht er nicht ganz, denn ob nichts Wichtiges fehlt, prüft er an der WISSEN-Datei. Einzelne Aussagen schlägt er gezielt nach.

Phase 2 startet erst nach dem Bericht von Phase 1. Es arbeitet also weiterhin nur ein Schreib-Agent zur Zeit.

**Viele Abbildungen (seit 10.11.2026, erstmals Linux 2 mit 31 Szenen):** Ab etwa 15 Szenen teilt sich Phase 2 in zwei frische Agenten nacheinander, damit keiner die Szenenarbeit mit dem ganzen Heft im Kontext macht.
- **2a Prüfen:** Satz-für-Satz-Prüfung, Beispiele und Wortwahl, Code-Abgleich, `rechnung_kap<N>.py`, Korrekturen, `zusammenfassung_kap<N>.md`.
- **2b Abbildungen und Bau:**
  - Szenen nach der Tabelle der Übergabe (samt `s.tr` in sechs Sprachen), Export `--animiert`, Kontaktblätter;
  - PDF und `pdf_pruefen`;
  - Konverter, Themenkarte, build_wissen, URL-Prüfung.

  Das Heft liest der Agent nur an den Stellen der Abbildungen.
- **Ab etwa 30 Szenen** (erstmals Linux 3 mit 41) teilt sich 2b noch einmal, nacheinander:
  - 2b-1 baut die Szenen der ersten Hälfte der Abschnitte;
  - 2b-2 baut die zweite Hälfte, dann PDF, Konverter, Themenkarte und Build.

  2a liefert dazu die endgültige Abbildungsliste, nach Abschnitten in zwei Hälften geteilt.
- **Kontaktblätter** (seit 10.11.2026 repariert):
  - Website-Bilder: `python tools/szenen_ansehen.py <blatt.png> <modul/szene …> --lang <sprache>` exportiert mit `--animiert` (die `.anim.svg` bleibt aktuell) und fotografiert die `.svg`; mit `--ohne-export` nur die fertigen Dateien, etwa nach dem Export aller Sprachen. Der Vorschau-Server ist nicht nötig.
  - Heft-Bilder: `python tools/kontaktblatt_pdf.py <Heftordner>/abb/<sprache> <Ausgabeordner> [präfix | name1,name2,…]` aus den Vektor-PDFs, ohne Präfix alle; prüft, was wirklich im Heft steht.

## Auftrag an einen Schreib-Agenten (Phase 1) bzw. Prüf-Agenten (Phase 2)
Nach dem Muster der bisherigen Aufträge, mit folgenden Teilen:
1. **Verweis** auf den Auftrag der Reihe, z. B. `heft_auftrag_zusatzreihen.md` oder `ueberarbeitung_auftrag.md`.
2. **Eckdaten:** Reihe und Teil, Dateinamen wie in `MODULE[...]` von `tools/heft_zu_artikel.py`, Titelzeile mit Datum, Szenendatei (Gerüst vorher anlegen), Scratchpad-Ordner, Ablage der Recherche-Notizen.
3. **Pflichtlektüre:** Die **Quellen** liest der Agent ganz, von der ersten bis zur letzten Zeile: Leitfaden, Präambel, Lernpfad, WISSEN-Datei, AUFGABEN, ZUSAMMENFASSUNG, QUELLEN und die Notizen zum Heft, bei Uni-Modulen das ganze Skript.
   - **Eigene frühere Hefte** liest er nur über ihre Zusammenfassungen `zusammenfassung_kap<N>.md` und bei Rückverweisen die betroffene Stelle.
   - **Musterhefte:** einen Abschnitt und den Abschluss als Stilvorbild.
   - Der User (06.11.2026): „Mit vollständig lesen meinte ich die Quellen. Die eigenen erstellten Hefte müssen ja nicht nochmal vollständig gelesen werden, da reichen Zusammenfassungen.“
4. **Besonderheiten des Hefts:** was es nicht vorwegnehmen darf (konkrete Wortliste), Notation und Bezeichnungen aus früheren Heften, Startpunkte für die Warum-Kästen, Kandidaten für Rechenbilder, Abbildungsideen, Code-Regeln (erst selbst bauen, dann Bibliothek), Verweise statt Wiederholung (Themenkarte).
5. **Grenzen:** nur eigene Dateien; was andere gerade bearbeiten; kein git, nichts installieren; LaTeX und Python nur mit Write/Edit.
6. **Bericht und Zusammenfassung:** Der Agent liefert `zusammenfassung_kap<N>.md` für spätere Agenten. Im Bericht stehen Gliederung, Umfang, Warum-Kästen mit Quellen, bewusst Weggelassenes, still korrigierte Fehler der Quellen, neue Bezeichnungen, Wünsche an die Präambel und ein **Lese-Nachweis** (Datei → gelesene Zeilen, auch für das eigene Heft).

## Prüfroutine nach jedem Bericht
0. **Nach Phase 1:** nur Punkt 1 (Lese-Nachweis) und ob `uebergabe_kap<N>.md` vorliegt, dann sofort den Prüf-Agenten starten. Die Punkte 2–6 gelten nach Phase 2.
1. **Quellen vollständig gelesen?** Den Lese-Nachweis mit den Zeilenzahlen der Quelldateien vergleichen; eigene frühere Hefte müssen nicht ganz gelesen sein. Gibt es `zusammenfassung_kap<N>.md`? (`wc -l`). Im Zweifel die Read-Aufrufe (offset/limit) im Protokoll auswerten: `~/.claude/projects/C--B-cher/<sitzung>/subagents/agent-<id>.jsonl`. Fehlt etwas, auch bei der Selbstprüfung des ganzen Hefts samt Lösungen, den Agenten per SendMessage nachlesen und nacharbeiten lassen.
2. **Selbst nachprüfen:**
   - `python tools/pdf_pruefen.py <pdf> <scratch>` muss 0 Stellen melden. Das PDF nie als Seitenbilder lesen;
   - bei neuen oder geänderten Szenen ein Kontaktblatt über `tools/szenen_ansehen.py` ansehen. Überlappungen oder eine Breite über 548 px korrigiere ich selbst oder lasse sie korrigieren;
   - `PYTHONIOENCODING=utf-8 python build_wissen.py` und einen Artikel (am besten mit Rechenbild) im Browser ansehen, per Playwright auf localhost:8000.
3. **Nacharbeit:** Fehlende Makros selbst in `praeambel.tex` ergänzen und danach `python tools/praeambel_sync.py <heftordner>` ausführen. Die Sprachpräambeln sind Kopien, ohne diesen Schritt bauen die Übersetzungen nicht. Bezeichnungen, die spätere Hefte übernehmen müssen, im Arbeitsstand unter „Hinweise …“ festhalten.
4. **Stand eintragen:** Tabelle im Arbeitsstand und das Gedächtnis der Reihe.
5. **Dem User berichten,** knapp: Umfang, Prüfergebnisse, inhaltliche Höhepunkte, Korrekturen, was gerade läuft, was als Nächstes kommt.
   - Dazu immer, ob er **jetzt committen und pushen** kann. Der User: „sag mir dann immer, wann ich comitten und pushen soll“.
   - **Sicher ist es,** wenn kein Agent Dateien im Repo ändert, build_wissen ohne Warnung lief und die Menge der Artikel-URLs geprüft ist.
   - **Sonst ausdrücklich abraten** und den Grund nennen.
6. **Das nächste Heft beauftragen,** in der Reihenfolge aus dem Arbeitsstand. Endgültige Hefte in die Übersetzung einreihen.

## Abbrüche und Sitzungswechsel
- **Abbruch am Sitzungslimit:** In derselben Sitzung den Agenten per SendMessage fortsetzen. In einer neuen Sitzung einen neuen Agenten starten, der zuerst den Stand der Dateien prüft und dann weitermacht; halbfertige Dateien liest er ganz.
- **Vor einem `/clear`:** Alles Wichtige muss in den Dateien stehen, also im Arbeitsstand mit „Nächste Schritte“, in dieser Datei, im Auftrag und im Gedächtnis.

## Token-Verbrauch
- **Die Schreib-Agenten verbrauchen am meisten.** Ein Heft kostete mit vollständigem Lesen aller früheren Hefte 0,6 bis 0,9 Millionen Tokens. Seit 06.11.2026 lesen die Agenten die früheren Hefte nur über Zusammenfassungen; dadurch wächst der Aufwand nicht mehr mit jedem Heft.
- **Die Chat-Länge des Haupt-Agenten** kommt hinzu, denn jede Antwort schickt den ganzen bisherigen Verlauf mit. Gegen diesen Anteil hilft `/clear` nach jedem größeren Abschnitt.
- **Sparen ohne Qualitätsverlust:** Der Haupt-Agent liest keine Agenten-Protokolle und keine großen Dateien unnötig in seinen eigenen Kontext, sondern wertet sie mit Skripten aus. Screenshots sieht er nur gezielt an.
- **Messen** (Skripte in `tools/agenten/`, Protokolle unter `~/.claude/projects/C--B-cher/<sitzung>/subagents/`):
  - `agent_tokens.py <subagents-ordner> <id> …` zeigt den aktuellen Kontext je Agent;
  - `agent_kontext.py <agent.jsonl>` zeigt, woraus er besteht;
  - `lese_nachweis.py <agent.jsonl>` zeigt, welche Zeilen jeder Datei gelesen wurden (für Prüfroutine Punkt 1).
- **Befund Python 3 (09.11.2026):** 797k Kontext, davon etwa 55 % Gelesenes (Quellen, eigenes Heft) und 30 % Geschriebenes. Vermeidbar waren: Dateien zweimal komplett geschrieben, zweimal ein Edit über fast die ganze Datei (50 000 Zeichen), ungefilterte Befehlsausgaben. Deshalb die Kontextregeln im Auftrag, Abschnitt „Sparsam mit dem Kontext“.
- **Übersetzer:** Der leitende Übersetzer bleibt schlank. Er vergibt Dateien an Hilfsagenten, prüft mit Skripten (`uebersetzung_struktur_check.py`, `pdf_pruefen.py`, gefilterte Build-Ausgabe) und lässt Fehler vom zuständigen Hilfsagenten beheben, per SendMessage oder als neuer Auftrag. Selbst korrigiert er nur Einzelzeichen. Übersetzte Texte liest er nicht ganz, sondern prüft sie mit grep-Stichproben. Bei Grundlagen 1 kam er mit 158 eigenen Edits auf 615k.
