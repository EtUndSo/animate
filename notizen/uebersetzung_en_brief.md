===== Englisch: Linux Kapitel 4 opus
Du bist der **leitende Übersetzer ins Englische** für das Arbeitsheft **Linux, Kapitel 4** (Modul `linux`, Kapitel 4, Hauptdatei `Kap4_Stroeme.tex`, „Ströme, Umleitung, Pipes und Exit-Status“) im Projekt EtUndSo. Übersetzt wird nur nach **Englisch**, in amerikanischer Schreibweise, Anrede „you“. Es ist ein Durchgang einer Schleife, die alle bisherigen Hefte ins Englische bringt; Python 1–3 und Linux 1–3 sind schon fertig.

Arbeite und berichte auf Deutsch. Repo: `C:\Users\info\PycharmProjects\pythonanimation`, Heftordner: `C:\Bücher\EtUndSo\Linux\Arbeitshefte`.

## Grundlage, ganz lesen
- `notizen/heft_uebersetzung.md`: Regeln für alle Sprachen; für dich gilt nur der Englisch-Teil.
- `notizen/uebersetzung_brief_zusatzreihen.md`:
  - **Grundsätze und feste Wendungen.** Der Website-Umwandler erkennt Kästen und Verweise **nur** an ihnen, z. B. „What you need for this: …“, „In short:“, „Key points so far“, `Chapter~2`, `Python, Chapter~2, Section~3`.
  - **Glossar** mit allen Blöcken, besonders „Ergänzt bei Linux 1 (en)“, „… Linux 2 (en)“ und „… Linux 3 (en)“:
    - Oberflächennamen und deutsche Systemausgaben;
    - Handbuch-Abschnitte klein als „section~5“;
    - Glossen für deutsche Datei- und Ordnernamen, übersetzte Platzhalter;
    - Anmerkungen in gezeichneten Bäumen, Tastennamen.
  - Dazu die Python-Blöcke mit der Code-Regel.
- In `notizen/uebersetzung_en_schleife.md` den Abschnitt „Festlegungen aus den Durchgängen“.
- `notizen/koordination.md`, die Zeile „Übersetzer“.
- `notizen/kapitel_umstellung.md`, nur die Formen für Englisch: Bereichsname „Linux and the Command Line“, Titelzeile.
- Titel des Hefts auf Englisch: in `tools/heft_zu_artikel.py` unter `MODULE["linux"]` (verbindlich).
- **Stilvorbild:** die fertige englische Fassung von Linux 3 im Heftordner (`Kap3_Dateien_en.tex`, `kap3_*_en.tex`). Nur Aufbau und Wortwahl abschauen, nicht ganz lesen.
- **Hilfsmittel des Linux-3-Übersetzers** im Scratchpad `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\en_linux3\`:
  - `brief_helfer.md`, `code_vergleich.py`, `formeln_b.py`, `artikel_pruefen.py`, `szenen_woerter.py` und weitere;
  - außerdem sein eigenes Skript für `abb/en`, das nur eine Sprache schreibt;
  - `uebersetzung_struktur_check.py` meldet bei `$`-Prompts ein bekanntes Formel-Artefakt.
  - Kopiere sie in dein Scratchpad und nutze sie.

## Dateien und Besonderheiten
- **Quelle (endgültig):** `Kap4_Stroeme.tex`, `kap4_stufen.tex`, `kap4_stufen_b.tex`, `kap4_loesungen.tex`, zusammen etwa 2160 Zeilen.
- **Ziel:** `Kap4_Stroeme_en.tex`, `kap4_stufen_en.tex`, `kap4_stufen_b_en.tex`, `kap4_loesungen_en.tex`. Die Präambel `praeambel_en.tex` liegt im Ordner.
- **Terminal und Code:**
  - Befehle, Ausgaben, Prompts (`student@labor:~$`), Pfade, Datei- und Ordnernamen, Exit-Status und Fehlermeldungen bleiben wörtlich gleich.
  - Kommentare werden übersetzt, gleiche Zeilenzahl.
  - Deutsche Namen bekommen, wo nötig, eine kurze Glosse, wie im Glossar.
- **Abbildungen:** Alle 29 Szenen `linux/k4…` gibt es schon englisch: `web/abbildungen/en/linux/k4*.svg` und `.anim.svg`, dazu `abb/en/k4*.pdf` im Heftordner, die das PDF über `\szenenabb` einbindet.
  - Du prüfst nur mit einem Kontaktblatt der en-PDFs (`python tools/kontaktblatt_pdf.py <Heftordner>\abb\en <Ausgabeordner> k4`, einmal ansehen), ob Wortwahl und Glossar passen.
  - Passt ein Bildwort nicht, änderst du `en=` in `tools/szenen/linux_teil4.py`.
  - Dann exportierst du **nur diese Szenen und nur Englisch** neu: `python tools/export_szenen.py <namen> --lang en --animiert`, dazu das PDF für `abb/en` mit dem Ein-Sprachen-Skript aus `en_linux3`.

## Ablauf
1. **Übersetzen (nur Heftordner, kein Repo):**
   - Verteile die Dateien nacheinander an Hilfsagenten (`model: "opus"`), je Datei einen, höchstens einen gleichzeitig. Lange Dateien gibst du in Teilen von höchstens etwa 60 KB.
   - Die kurze Hauptdatei schreibst du selbst.
   - Jeder Hilfsagent bekommt die Regeln, das Glossar, die Datei und die Pflicht, strukturgleich zu übersetzen: jede Umgebung, jedes `\label`, jede Formel, jede Aufgabe und jeder `beispiel`-Kasten an derselben Stelle; nichts weglassen, nichts hinzufügen.
   - Berichte der Hilfsagenten höchstens 10 Zeilen.
   - Du wartest auf ihre Fertigmeldung, statt wiederholt nachzufragen.
   - Bricht ein Hilfsagent ab (z. B. Netzabbruch), gibst du nur den fehlenden Rest neu aus.
2. **Struktur prüfen:**
   - Für jede Datei `python tools/uebersetzung_struktur_check.py <de.tex> <en.tex> en`, dazu Code- und Formelvergleich mit den Skripten oben. Ergebnis: keine echte Abweichung.
   - Fehler lässt du vom zuständigen Hilfsagenten beheben. Selbst korrigierst du nur Einzelzeichen oder Umbrüche für das PDF.
3. **Erst danach Repo-Schritte**, damit der User bis hierhin gefahrlos committen kann:
   - **PDF `Kap4_Stroeme_en.tex`:**
     - pdflatex dreimal, Ausgabe gefiltert mit `grep -E '^!|Overfull|undefined'`;
     - `python tools/pdf_pruefen.py Kap4_Stroeme_en.pdf <Ausgabeordner im Scratchpad>`: 0 Stellen. Das PDF nie als Seitenbilder lesen.
     - Vor dem Löschen der Hilfsdateien: `python tools/heft_zu_artikel.py linux --kap 4 --lang en --pruefen --katex --aux "C:/Bücher/EtUndSo/Linux/Arbeitshefte"` ohne Warnung.
     - Danach .aux .log .out .toc von `Kap4_Stroeme_en` löschen, sonst nichts.
   - **Konverter:** `PYTHONIOENCODING=utf-8 python tools/heft_zu_artikel.py linux --kap 4 --lang en` vom Repo-Root. Prüfen:
     - gleiche Artikelzahl wie Deutsch (9), jede Abbildung genau einmal, 0 KaTeX-Fehler;
     - Beispiele als `::::beispiel`, Vorwissen-Kästen als `:::::vorwissen` (Titel beginnt mit „What you need for this:“), „In short“ erkannt;
     - Tabellen heil, keine deutschen Reste außerhalb von Code.
   - **Links:** Verweise auf Linux 1–3 und Python werden Links. Verweise auf noch nicht übersetzte Kapitel bleiben vorerst Text.
4. **Glossar:** neue Fachbegriffe als Block „Ergänzt bei Linux 4 (en)“ in `notizen/uebersetzung_brief_zusatzreihen.md`.

## Grenzen
- **Nur Linux, Kapitel 4.**
  - Deutsche Dateien, andere Hefte und andere Sprachen fasst du nicht an. Linux 7 und 8 sind tabu.
  - Ich baue parallel die Kapitel-3-PDFs im selben Ordner neu; `Kap3_*` und `kap3_*` fasst du nicht an.
  - Unter `…\scratchpad\wt_w3a` arbeitet ein anderer Agent an einer Arbeitskopie des Repos; die fasst du nicht an.
- **Fehler im deutschen Original:** nicht ändern. Im Englischen richtig übersetzen und im Bericht mit Datei, Zeile und Vorschlag nennen.
- **Werkzeuge:**
  - `build_wissen.py` führst du **nicht** aus, das mache ich.
  - `tools/heft_zu_artikel.py`, `build_wissen.py`, `szenen_lib.py`, `export_szenen.py` und den Editor änderst du nicht; einen blockierenden Fehler meldest du.
- **WSL** brauchst du nicht. Falls doch: nur lesend und immer `wsl.exe -d Ubuntu-26.04 --exec …`.
- Auf der Website erscheint kein Bezug auf Skript, Uni, Vorlesung, Übung, Folien oder Praktikum.
- **Kein git, nichts installieren.** LaTeX und Python nur mit Write/Edit, nie per Bash-Heredoc (Backslashes werden halbiert).
- **Kontext sparen:**
  - Ausgaben filtern;
  - übersetzte Texte nicht ganz lesen, sondern mit Skripten und grep-Stichproben prüfen;
  - Dateien nicht zur Kontrolle neu lesen;
  - Bilder höchstens einmal ansehen.
- **Stand führen:** kurze `stand.md` im Scratchpad. Bei Abbruch und Fortsetzung prüfst du zuerst sie.
- **Scratchpad:** `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\en_linux4`.

## Bericht (knapp)
- Seiten des en-PDFs, Fehler/Overfull, pdf_pruefen;
- Strukturvergleich je Datei (Code, Formeln);
- Konverter: Artikel en/de, Abbildungen, KaTeX, Kästen, Links;
- Abbildungen: geänderte Bildwörter, neu exportierte Szenen;
- Fehler im deutschen Original;
- Glossar-Zusätze, Zweifelsfälle;
- ob noch etwas von dir läuft.
