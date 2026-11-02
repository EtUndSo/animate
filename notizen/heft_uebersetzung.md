# Auftrag: Arbeitsheft übersetzen (en, es, zh)

Übersetze die deutschen Heftdateien eines Teils nach Englisch, Spanisch und vereinfachtem Chinesisch. Vorbild sind die ET3-Fassungen in C:\Bücher\ET3\Arbeitshefte (kap1_stufen_en.tex, _es, _zh, Kap1_Faltung_en.tex usw.): dieselbe Struktur, dieselben Umgebungen, dieselben Labels. Präambeln praeambel_en/_es/_zh.tex liegen im Heftordner.

Regeln:
- Dateien: Kap<N>_<Name>_<lang>.tex, kap<N>_stufen_<lang>.tex, kap<N>_loesungen_<lang>.tex. Das Hauptdokument bindet die _<lang>-Dateien ein. Titelblock übersetzen.
- Nichts kürzen, nichts ergänzen. Formeln, Labels, Zahlenwerte unverändert. Text in Formeln (`	ext{...}`, Indizes aus Wörtern wie `W_	ext{außen}`) wird übersetzt. Zahlwörter werden umgerechnet: Milliarde = billion = mil millones = 十亿, Billion = trillion = billón = 万亿. Dezimaltrennzeichen: en und zh Punkt (0.7), es Komma (0{,}7). Einheiten bleiben.
- Englisch amerikanische Schreibweise. Begriffe: Stufe = stage, Aufgabe = exercise, Spannung = voltage, Strom = current, Knoten = node, Masche = mesh/loop, Zählpfeil = reference arrow, Ersatzquelle = equivalent source. Das Wort Arbeitsheft wird workbook, cuaderno, 本册 (so erkennt es der Umwandler).
- Wörter: Verbindlich sind die Bildwörter in tools/szenen/et1_teil<N>.py (`s.tr`), die Titel in tools/heft_zu_artikel.py (MODULE["et1"]) und die Wahl aus Teil 1: en ground, curl-free; es tensión, nudo, masa; zh 电位, 接地点. Zählpfeile: en passive sign convention (Verbraucherzählpfeil), active sign convention (Erzeugerzählpfeil).
- Titelblock wie ET3: „Workbook“, „Cuaderno de trabajo“, 练习册; Datum en `31~October 2026`. Im Fließtext heißt das Heft aber workbook, cuaderno, 本册.
- Verweise auf andere Teile: `Part~2`, `Parte~2`, `第 2 部分` (so werden sie auf der Website zu Links).
- In zh hat SimSun keine Kursive: Im Fließtext `emph` zu `	extbf`.
- `markboth` nach `section*` in allen Sprachen setzen. Deutsche `pagebreak` nicht übernehmen, sondern je Sprache prüfen, dass kein Boxtitel allein am Seitenfuß steht, und nötige Umbrüche selbst setzen.
- Absatzüberschriften wie in ET3: „How to work with this workbook.“, „Cómo trabajar con el cuaderno.“, „如何使用本册。“; Lösungen = Solutions, Soluciones, 解答; kernbox-Titel: Key points, Lo esencial, 要点.
- Bauen: en und es pdflatex, zh xelatex, je dreimal fehlerfrei, danach .aux .log .out .toc löschen. Nie nur einen Lauf nach gelöschtem aux.
- Prüfen vor dem Löschen der .aux: python tools/heft_zu_artikel.py et1 --kap <N> --pruefen --katex --aux C:/Bücher/ET1/Arbeitshefte (im Repo C:\Users\info\PycharmProjects\pythonanimation) ohne Warnung.
- LaTeX nur mit Write oder Edit schreiben, nie per Bash-Heredoc (Backslash-Falle). Die Abbildungen sind schon übersetzt: `\szene{...}` bleibt unverändert, PDFs liegen in abb/<lang>/.
- Fehler im deutschen Original: Wert wie im Original übernehmen, im Bericht mit Datei, Stelle und richtigem Wert nennen, nichts am Original ändern.
- Nichts committen, nichts außerhalb der Heftdateien des Teils ändern.

Bericht: Seitenzahlen je Sprache, gefundene Fehler im Original.
