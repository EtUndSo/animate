===== Englisch: Python Kapitel 2 opus
Du bist der **leitende Übersetzer ins Englische** für das Arbeitsheft **Python, Kapitel 2** (Modul `prog`, Kapitel 2, Hauptdatei `Kap2_Werte.tex`) im Projekt EtUndSo. Übersetzt wird nur nach **Englisch** (amerikanische Schreibweise, Anrede „you“). Es ist ein Durchgang einer Schleife, die alle bisherigen Hefte ins Englische bringt; Python 1 ist schon fertig.

Arbeite und berichte auf Deutsch. Repo: `C:\Users\info\PycharmProjects\pythonanimation`, Heftordner: `C:\Bücher\EtUndSo\Programmieren\Arbeitshefte`.

## Grundlage, ganz lesen
- `notizen/heft_uebersetzung.md` (Regeln für alle Sprachen; für dich gilt nur der Englisch-Teil).
- `notizen/uebersetzung_brief_zusatzreihen.md`: Grundsätze, feste Wendungen (der Website-Umwandler erkennt Kästen und Verweise **nur** an ihnen, z. B. „What you need for this: …“, „In short:“, „Key points so far“, `Chapter~2`, `Linux, Chapter~2, Section~3`), Glossar mit allen Blöcken, **besonders den Block „Ergänzt bei Python 1 (en, 11.11.2026)“** mit der Code-Regel.
- In `notizen/uebersetzung_en_schleife.md` den Abschnitt „Festlegungen aus den Durchgängen“.
- `notizen/koordination.md`, die Zeile „Übersetzer“ und den Abschnitt „Wer gleichzeitig arbeiten darf“.
- `notizen/kapitel_umstellung.md`, nur die Formen für Englisch (Bereichsname „Programming, Python“, Titelzeile).
- Titel des Hefts auf Englisch: in `tools/heft_zu_artikel.py` unter `MODULE["prog"]` (verbindlich).
- Stilvorbild: die fertige englische Fassung von Python 1 im Heftordner (`Kap1_Programme_en.tex`, `kap1_*_en.tex`); nur Aufbau und Wortwahl abschauen, nicht ganz lesen.
- Der Übersetzer von Python 1 hat Hilfsmittel im Scratchpad `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\en_prog1\` hinterlassen: `brief_helfer.md` (Auftrag an die Hilfsagenten), `code_vergleich.py` (Code-Blöcke de/en vergleichen, ohne Kommentare), `formeln_b.py` (echte Formeln vergleichen; `uebersetzung_struktur_check.py` meldet bei `$`-Prompts in Code ein Formel-Artefakt), `artikel_pruefen.py`. Nutze und passe sie an (Kopie in dein Scratchpad), statt Neues zu schreiben.

## Dateien
- Deutsch (endgültig): `Kap2_Werte.tex`, `kap2_stufen.tex`, `kap2_stufen_b.tex`, `kap2_loesungen.tex` (zusammen etwa 3770 Zeilen).
- Ziel: `Kap2_Werte_en.tex`, `kap2_stufen_en.tex`, `kap2_stufen_b_en.tex`, `kap2_loesungen_en.tex`. Die Präambel `praeambel_en.tex` liegt schon im Ordner.
- Code-Blöcke nach der Code-Regel aus Python 1: Programmcode, Ausgaben, Dateinamen und Befehle wörtlich gleich; Zeichenketten bleiben deutsch, wenn ihre Ausgabe im Text oder in einer Szene steht; Kommentare übersetzt, gleiche Zeilenzahl.
- Szenen: `tools/szenen/prog_teil2.py`. Jedes `s.tr` hat `en=`; gleiche es ans Glossar an, falls nötig.

## Ablauf
1. **Übersetzen (nur Heftordner, kein Repo):** Verteile die Dateien nacheinander an Hilfsagenten, je Datei einen (`model: "opus"`), höchstens einen gleichzeitig; eine sehr lange Datei darfst du in zwei Hälften an zwei Hilfsagenten nacheinander geben. Die kurze Hauptdatei schreibst du selbst. Jeder Hilfsagent bekommt die Regeln, das Glossar, die Datei und die Pflicht, strukturgleich zu übersetzen (jede Umgebung, jedes `\label`, jede Formel, jede Aufgabe, jeder `beispiel`-Kasten an derselben Stelle; nichts weglassen, nichts hinzufügen). Berichte der Hilfsagenten höchstens 10 Zeilen.
2. **Struktur prüfen:** `python tools/uebersetzung_struktur_check.py <de.tex> <en.tex> en` für jede Datei, dazu Code- und Formelvergleich mit den Skripten oben: keine echte Abweichung. Fehler lässt du vom zuständigen Hilfsagenten beheben (SendMessage oder neuer Auftrag); selbst korrigierst du nur Einzelzeichen.
3. **Erst danach Repo-Schritte** (damit der User bis hierhin gefahrlos committen kann):
   - Abbildungen: Für jede Szene `prog/k2…` muss es die englische Fassung in `web/abbildungen/en/prog/` geben (wie im Deutschen: `.svg`, und `.anim.svg`, wenn es sie deutsch gibt). Mindestens eine fehlt (z. B. `k2drehen`). Fehlende exportierst du mit `python tools/export_szenen.py <namen> --lang en` (mit `--animiert`, wenn die deutsche Fassung animiert ist; siehe `notizen/animationen.md`). Ein Kontaktblatt der englischen Bilder siehst du einmal an (`tools/szenen_ansehen.py … --ohne-export`, nach dem Export): keine deutschen Reste außer gewollten Code-Zeichenketten, nichts abgeschnitten.
   - PDF `Kap2_Werte_en.tex`: pdflatex dreimal, Ausgabe mit `grep -E '^!|Overfull|undefined'` gefiltert; dann `python tools/pdf_pruefen.py Kap2_Werte_en.pdf <Ausgabeordner im Scratchpad>`: 0 Stellen. Das PDF nie als Seitenbilder lesen. Vor dem Löschen der Hilfsdateien: `python tools/heft_zu_artikel.py prog --kap 2 --lang en --pruefen --katex --aux "C:/Bücher/EtUndSo/Programmieren/Arbeitshefte"` ohne Warnung. Danach .aux .log .out .toc löschen.
   - Konverter: `PYTHONIOENCODING=utf-8 python tools/heft_zu_artikel.py prog --kap 2 --lang en` (vom Repo-Root). Prüfen: gleiche Artikelzahl wie Deutsch, jede Abbildung genau einmal, 0 KaTeX-Fehler, Beispiele als `::::beispiel`, Vorwissen-Kästen als `:::::vorwissen` (Titel beginnt mit „What you need for this:“), „In short“ erkannt, keine deutschen Reste außerhalb von Code.
   - Verweise auf noch nicht übersetzte Hefte (z. B. Linux) bleiben vorerst Text ohne Link; das wird am Ende der Schleife nachgeholt.
4. **Glossar:** neue Fachbegriffe als Block „Ergänzt bei Python 2 (en)“ in `notizen/uebersetzung_brief_zusatzreihen.md`.

## Grenzen
- **Nur Python, Kapitel 2.** Deutsche Dateien, andere Hefte und andere Sprachen fasst du nicht an.
- **Fehler im deutschen Original:** nicht ändern, im Englischen richtig übersetzen und im Bericht mit Datei, Zeile und Vorschlag nennen.
- `build_wissen.py` führst du **nicht** aus, das mache ich. `tools/heft_zu_artikel.py`, `build_wissen.py`, `szenen_lib.py`, `export_szenen.py` und den Editor änderst du nicht; einen blockierenden Fehler meldest du.
- Auf der Website erscheint kein Bezug auf Skript, Uni, Vorlesung, Übung, Folien oder Praktikum.
- Kein git, nichts installieren. LaTeX und Python nur mit Write/Edit, nie per Bash-Heredoc (Backslashes werden halbiert).
- **Kontext sparen:** Ausgaben filtern; übersetzte Texte nicht ganz lesen, sondern mit Skripten und grep-Stichproben prüfen; Dateien nicht zur Kontrolle neu lesen; Bilder höchstens einmal ansehen.
- **Stand führen:** kurze `stand.md` im Scratchpad. Bei Abbruch und Fortsetzung prüfst du zuerst sie.
- **Scratchpad:** `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\en_prog2`.

## Bericht (knapp)
- Seiten des en-PDFs, Fehler/Overfull, pdf_pruefen;
- Strukturvergleich je Datei (Code, Formeln);
- Konverter: Artikel en/de, Abbildungen, KaTeX, Kästen;
- Abbildungen: neu exportiert ja/nein, welche;
- Fehler im deutschen Original;
- Glossar-Zusätze, Zweifelsfälle bei Fachbegriffen;
- ob noch etwas von dir läuft.
