# Kurzfassungen und Formelsammlungen für alle Artikel (seit 11.11.2026)

Entscheidung des Users (11.11.2026): „Ja, wir sollten zu allen Artikeln die Formelsammlung und die kurze Erklärung neu erstellen.“ Der Pilot ET3, Kapitel 2 ist abgenommen: „Ja, beide sehen gut aus, gut gemacht.“

**Pause (User 11.11. abends):** Nach ET3 Kap. 3 startet kein neues Heft, bis die einmaligen Aufgaben in `notizen/aufgabenliste.md` (Abschnitt B) erledigt sind. Dann weiter als Loop C2.

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
| et3 | 1 | fertig 11.11. (10 Kurzfassungen 159–233 Wörter, 57 Formeln, alle belegt; PDFs 6/8 S.) |
| et3 | 3 | fertig 11.11. (11 Kurzfassungen 171–213 Wörter, 75 Formeln, alle belegt; PDFs 6/9 S.). Danach Pause laut Aufgabenliste. |

## Fragliche Stellen in den Heften (von den Schreibern gemeldet)
- ET3 Kap. 1: Heft nennt φ = −arctan x „Nacheilwinkel“; die Kurzfassung sagt „der Ausgang eilt um arctan x nach“. Bei der Dehnung des Dirac-Impulses fehlt im Heft die Bedingung b ≠ 0 (Kurzfassung nennt sie). Später im Heft prüfen.
- ET3 Kap. 3 (gemeldet 11.11.):
  - `kap3_stufen_b.tex:239` Existenzbedingung „∫|s|e^{−c|t|}dt<∞ für jedes c>0 genügt“ falsch (Gegenbeispiel e^{√|t|}); richtig: höchstens wie eine Potenz wachsen.
  - `:246` Gauß-Vertiefung: „Viele positive Impulse endlicher Fläche nähern sich einer Gaußkurve“ falsch (1/(1+t²) bleibt Cauchy); nötig: endliches zweites Moment.
  - `:154/162` Hilbert-Faltung nur als Hauptwert.
  - `:165` S₋/s₋ nie definiert.
  - si(0)=1 nur im Kommentar.
  - `kap3_stufen_a.tex:104` Gleichheit der Fourier-Reihe nur im Sinn verschwindender Fehlerleistung.
