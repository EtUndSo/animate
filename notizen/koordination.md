# Koordination: wie der Haupt-Agent Schreib- und Übersetzungs-Agenten führt

Gilt für alle Heftreihen: Cybersecurity, Machine Learning, Programmieren, Linux und die Uni-Module bei ihrer Überarbeitung. Der Haupt-Agent schreibt selbst keine Hefte, er plant, beauftragt, prüft und berichtet. Der Arbeitsstand je Reihe steht in `zusatzreihen_stand.md` bzw. `ueberarbeitung_stand.md`.

## Wer gleichzeitig arbeiten darf
- **Schreiben:** höchstens ein Schreib-Agent zur Zeit, immer auf Opus (`model: "opus"`).
- **Übersetzen:** parallel dazu höchstens ein Übersetzungs-Agent, nur für endgültige Hefte.
  - Er arbeitet nach `notizen/heft_uebersetzung.md` und dem Brief mit Glossar `notizen/uebersetzung_brief_zusatzreihen.md`, entstanden bei Grundlagen 2.
  - Er prüft jede Datei mit `python tools/uebersetzung_struktur_check.py <de.tex> <L.tex> <L>`.
  - Er verteilt die Dateien nacheinander an einzelne Hilfsagenten, weil ein Heft in fünf Sprachen nicht in einen Kontext passt.
  - Neue Fachbegriffe trägt er ins Glossar des Briefs ein, damit spätere Hefte sie gleich übersetzen.
- **Recherche:** Unteragenten höchstens 3 gleichzeitig, immer auf Sonnet, nur zum Suchen und Exzerpieren.
- **Programmieren am Werkzeug** (Editor, Konverter, Website): ein eigener Agent, der die Dateien der Schreib-Agenten nicht anfasst. Gemeinsam benutzte Werkzeuge hält er jederzeit lauffähig.

## Auftrag an einen Schreib-Agenten
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
1. **Quellen vollständig gelesen?** Den Lese-Nachweis mit den Zeilenzahlen der Quelldateien vergleichen; eigene frühere Hefte müssen nicht ganz gelesen sein. Gibt es `zusammenfassung_kap<N>.md`? (`wc -l`). Im Zweifel die Read-Aufrufe (offset/limit) im Protokoll auswerten: `~/.claude/projects/C--B-cher/<sitzung>/subagents/agent-<id>.jsonl`. Fehlt etwas, auch bei der Selbstprüfung des ganzen Hefts samt Lösungen, den Agenten per SendMessage nachlesen und nacharbeiten lassen.
2. **Selbst nachprüfen:**
   - `python tools/pdf_pruefen.py <pdf> <scratch>` muss 0 Stellen melden. Das PDF nie als Seitenbilder lesen;
   - bei neuen oder geänderten Szenen ein Kontaktblatt über `tools/szenen_ansehen.py` ansehen. Überlappungen oder eine Breite über 548 px korrigiere ich selbst oder lasse sie korrigieren;
   - `PYTHONIOENCODING=utf-8 python build_wissen.py` und einen Artikel (am besten mit Rechenbild) im Browser ansehen, per Playwright auf localhost:8000.
3. **Nacharbeit:** Fehlende Makros selbst in `praeambel.tex` ergänzen und danach `python tools/praeambel_sync.py <heftordner>` ausführen. Die Sprachpräambeln sind Kopien, ohne diesen Schritt bauen die Übersetzungen nicht. Bezeichnungen, die spätere Hefte übernehmen müssen, im Arbeitsstand unter „Hinweise …“ festhalten.
4. **Stand eintragen:** Tabelle im Arbeitsstand und das Gedächtnis der Reihe.
5. **Dem User berichten,** knapp: Umfang, Prüfergebnisse, inhaltliche Höhepunkte, Korrekturen, was gerade läuft, was als Nächstes kommt.
6. **Das nächste Heft beauftragen,** in der Reihenfolge aus dem Arbeitsstand. Endgültige Hefte in die Übersetzung einreihen.

## Abbrüche und Sitzungswechsel
- **Abbruch am Sitzungslimit:** In derselben Sitzung den Agenten per SendMessage fortsetzen. In einer neuen Sitzung einen neuen Agenten starten, der zuerst den Stand der Dateien prüft und dann weitermacht; halbfertige Dateien liest er ganz.
- **Vor einem `/clear`:** Alles Wichtige muss in den Dateien stehen, also im Arbeitsstand mit „Nächste Schritte“, in dieser Datei, im Auftrag und im Gedächtnis.

## Token-Verbrauch
- **Die Schreib-Agenten verbrauchen am meisten.** Ein Heft kostete mit vollständigem Lesen aller früheren Hefte 0,6 bis 0,9 Millionen Tokens. Seit 06.11.2026 lesen die Agenten die früheren Hefte nur über Zusammenfassungen; dadurch wächst der Aufwand nicht mehr mit jedem Heft.
- **Die Chat-Länge des Haupt-Agenten** kommt hinzu, denn jede Antwort schickt den ganzen bisherigen Verlauf mit. Gegen diesen Anteil hilft `/clear` nach jedem größeren Abschnitt.
- **Sparen ohne Qualitätsverlust:** Der Haupt-Agent liest keine Agenten-Protokolle und keine großen Dateien unnötig in seinen eigenen Kontext, sondern wertet sie mit Skripten aus. Screenshots sieht er nur gezielt an.
