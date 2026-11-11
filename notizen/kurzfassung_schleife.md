# Kurzfassungen und Formelsammlungen für alle Artikel (seit 11.11.2026)

Entscheidung des Users (11.11.2026): „Ja, wir sollten zu allen Artikeln die Formelsammlung und die kurze Erklärung neu erstellen.“ Der Pilot ET3, Kapitel 2 ist abgenommen: „Ja, beide sehen gut aus, gut gemacht.“

## Muster (aus dem Pilot)
- **Dateien je Heft im Heftordner:**
  - `kap<N>_kurz.tex` und `kap<N>_formeln.tex`;
  - Hauptdateien `Kap<N>_<Name>_Kurz.tex` und `Kap<N>_<Name>_Formeln.tex` (PDFs);
  - Definitionen in `kurz_formeln_def.tex`, eine je Heftordner, beim ersten Heft eines Moduls aus `C:\Bücher\ET3\Arbeitshefte\kurz_formeln_def.tex` übernehmen und an die Präambel anpassen.
- **Kurzfassung:**
  - Format `\begin{kurzfassung}{<Schlüssel>}{<Titel>} … \end{kurzfassung}`, Schlüssel = erster `stufe`-Anker des Artikels.
  - Etwa 120–250 Wörter. Aufbau: Kernaussage, Begriffe mit knapper Bestimmung, zentrale Formel mit Bedeutung, Warum, typische Falle.
  - **Keine Kurzfassung für Überblicksartikel** (Erkenntnis aus dem Pilot: kaum kürzer als der Artikel; die Ansicht „Kurz“ zeigt dort den Überblick selbst) und keine für „Das Wichtigste bis hier“.
- **Formelsammlung:** `\begin{formelsammlung}{<Schlüssel>}{<Titel>}` mit `\formel{Name}{Formel}{Bedeutung; Bedingungen}`. Alle wichtigen Formeln, keine Zwischenschritte, keine Zahlenbeispiele.
- **Prüfung:**
  - jede Formel mit Beleg im Heft (Skript `scratchpad/pilot_kurz_et3k2/formelabgleich.py`);
  - Wortzahl (`wortzahl.py`);
  - PDFs dreimal bauen, `pdf_pruefen` 0.
- **Hinweis:** `\fb` trennt lange Komposita nicht; Sätze dann umstellen.
- **Vollständiger Brief des Pilots:** `notizen/kurzfassung_brief_pilot.md`, für jedes Heft anpassen: Modul, Kapitel, Dateien, Überblick weglassen, Hilfsmittel des Vorgängers.

## Website
Welle W4a legt die Haken an (`::::kurzfassung`, `::::formelsammlung` im Artikel-Markdown). Danach erweitere ich den Konverter (`tools/heft_zu_artikel.py`), der die Blöcke aus den beiden Dateien in die Artikel schreibt.

## Warteschlange
Ein Schreib-Agent zur Zeit, parallel zur Englisch-Schleife.
- **Formelreiche Module zuerst:**
  - ET3 Kap. 1, 3–8 (Kap. 2 = Pilot, fertig);
  - HöMa1 1–10;
  - HöMa3 1, 2, 4–8 (Kap. 3 erst nach seiner Überarbeitung);
  - ML-Grundlagen 1–5;
  - ET1 1–11;
  - GEMB1 1–15.
- **Danach Informatik** (Linux 1–6, Python 1–3, Cybersecurity 1): Statt Formeln eine **Befehls- und Syntaxübersicht** (User 11.11.: „Ja genau, dort die Befehls- und Syntaxübersicht“). Gleiche Datei `kap<N>_formeln.tex` und gleiches Format, Einträge Befehl/Schreibweise, Bedeutung, wichtige Optionen. Auf der Website heißt die Ansicht dort „Übersicht“, die Modulseite „Befehlsübersicht“.

| Modul | Kap | Status |
|---|---|---|
| et3 | 2 | fertig 11.11. (Pilot) |
| et3 | 1 | läuft seit 11.11. |
