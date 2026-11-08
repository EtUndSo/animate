# Auftrag: Arbeitsheft übersetzen (en, es, zh, fr, tr)

Übersetze die deutschen Heftdateien eines Teils nach Englisch, Spanisch, vereinfachtem Chinesisch, Französisch oder Türkisch (der Auftrag nennt die Sprachen). Vorbild sind die ET3-Fassungen in C:\Bücher\ET3\Arbeitshefte (kap1_stufen_en.tex, _es, _zh, Kap1_Faltung_en.tex usw.): dieselbe Struktur, dieselben Umgebungen, dieselben Labels. Präambeln praeambel_en/_es/_zh/_fr/_tr.tex liegen in jedem Heftordner (ET1, ET3, HöMa1, HöMa3, GEMB, EtUndSo\Cybersecurity, EtUndSo\MachineLearning).

Regeln:
- Dateien: Kap<N>_<Name>_<lang>.tex, kap<N>_stufen_<lang>.tex, kap<N>_loesungen_<lang>.tex. Das Hauptdokument bindet `praeambel_<lang>` und die _<lang>-Dateien ein. Titelblock übersetzen.
- Nichts kürzen, nichts ergänzen. Formeln, Labels, Zahlenwerte unverändert. Text in Formeln (`\text{...}`, Indizes aus Wörtern wie `W_\text{außen}`) wird übersetzt. Zahlwörter werden umgerechnet: Milliarde = billion = mil millones = 十亿 = milliard = milyar, Billion = trillion = billón = 万亿 = billion (fr!) = trilyon. Dezimaltrennzeichen: en und zh Punkt (0.7), es, fr und tr Komma (0{,}7). Einheiten bleiben.
- Englisch amerikanische Schreibweise. Begriffe: Stufe = stage, Aufgabe = exercise, Spannung = voltage, Strom = current, Knoten = node, Masche = mesh/loop, Zählpfeil = reference arrow, Ersatzquelle = equivalent source. Das Wort Arbeitsheft wird workbook, cuaderno, 本册 (so erkennt es der Umwandler).
- Wörter: Verbindlich sind die Bildwörter in tools/szenen/<modul>_teil<N>.py (`s.tr`), die Titel in tools/heft_zu_artikel.py (MODULE["<modul>"], dort stehen auch die fr- und tr-Titel aller Teile) und die Wahl aus Teil 1: en ground, curl-free; es tensión, nudo, masa; zh 电位, 接地点. Zählpfeile: en passive sign convention (Verbraucherzählpfeil), active sign convention (Erzeugerzählpfeil).
- Titelblock wie ET3: „Workbook“, „Cuaderno de trabajo“, 练习册; Datum en `31~October 2026`. Im Fließtext heißt das Heft aber workbook, cuaderno, 本册.
- Verweise auf andere Teile: `Part~2`, `Parte~2`, `第 2 部分` (so werden sie auf der Website zu Links). In den Zusatzreihen (ML, Cybersecurity, Programmieren, Linux) gelten die Wendungen im Abschnitt „Verweise auf andere Hefte“ unten; dort wird auch „…, Abschnitt M“ zum Link auf den Abschnitt.
- In zh hat SimSun keine Kursive: Im Fließtext `\emph` zu `\textbf`.
- `\markboth` nach `\section*` in allen Sprachen setzen. Deutsche `\pagebreak` nicht übernehmen, sondern je Sprache prüfen, dass kein Boxtitel allein am Seitenfuß steht, und nötige Umbrüche selbst setzen.
- Absatzüberschriften wie in ET3: „How to work with this workbook.“, „Cómo trabajar con el cuaderno.“, „如何使用本册。“; Lösungen = Solutions, Soluciones, 解答; kernbox-Titel: Key points, Lo esencial, 要点.
- Bauen: en, es, fr und tr pdflatex, zh xelatex, je dreimal fehlerfrei, danach .aux .log .out .toc löschen. Nie nur einen Lauf nach gelöschtem aux.
- Prüfen vor dem Löschen der .aux: python tools/heft_zu_artikel.py <modul> --kap <N> --lang <lang> --pruefen --katex --aux C:/Bücher/<Ordner>/Arbeitshefte (im Repo C:\Users\info\PycharmProjects\pythonanimation) ohne Warnung.
- LaTeX nur mit Write oder Edit schreiben, nie per Bash-Heredoc (Backslash-Falle). `\szene{...}` bleibt unverändert, die PDFs liegen in abb/<lang>/ (siehe „Abbildungen“ unten).
- Fehler im deutschen Original: Wert wie im Original übernehmen, im Bericht mit Datei, Stelle und richtigem Wert nennen, nichts am Original ändern.
- Nichts committen, nichts außerhalb der Heftdateien des Teils ändern (Ausnahme: die fr/tr-Bildwörter, siehe unten).

## Französisch (fr) und Türkisch (tr)

Der Umwandler (tools/heft_zu_artikel.py) erkennt Kästen und Verweise an festen Wendungen. Genau diese verwenden:

| Zweck | fr | tr |
|---|---|---|
| Arbeitsheft im Fließtext | cahier (Titelblock: „Cahier d’exercices“) | çalışma kitabı mit Endungen: …kitabında, …kitabının, …kitabına, …kitabını, …kitabından, …kitabıyla, Plural …kitapları… (Titelblock: „Çalışma Kitabı“). Keine Possessivformen wie „kitabımız“. |
| daraus wird auf der Website | chapitre | bölüm (mit passender Endung) |
| Verweis auf einen Teil | `Partie~2` | `Kısım~2` (Endung mit Apostroph: `Kısım~2'de`) |
| Absatz „So arbeitest du …“ | „Comment travailler avec ce cahier.“ | „Bu çalışma kitabıyla nasıl çalışılır?“ |
| Absatz „Ein Prinzip …“ | „Un principe derrière tous les résultats.“ | „Tüm sonuçların ardındaki tek ilke.“ |
| kernbox „Die Antwort in drei Sätzen (…)“ | „La réponse en trois phrases (à la fin du cahier, elles devraient vous sembler évidentes)“ | „Üç cümlede cevap (çalışma kitabının sonunda bunlar size apaçık gelmeli)“ |
| kernbox „Das Wichtigste“ / „… bis hier“ | „L’essentiel“ / „L’essentiel jusqu’ici“ | „Temel noktalar“ / „Buraya kadarki temel noktalar“ |
| Abschnitt „Lösungen“ | Solutions | Çözümler |
| „Die Idee.“ / „Beispiel.“ | „L’idée.“ / „Exemple.“ | „Fikir.“ / „Örnek.“ |
| Datum im Titelblock | `31~octobre 2026` | `31~Ekim 2026` |

- Anrede: fr „vous“, tr „siz“ (wie die Oberfläche und die Hinweise der Website). Ton sachlich, nicht steif.
- Begriffe ET: Stufe = étape / aşama, Aufgabe = exercice / alıştırma, Spannung = tension / gerilim, Strom = courant / akım, Knoten = nœud / düğüm, Masche = maille / çevre, Ersatzquelle = source équivalente / eşdeğer kaynak, Masse (Bezugspunkt) = masse / toprak, Potenzial = potentiel / potansiyel, Verbraucherzählpfeil = convention récepteur / pasif işaret kuralı, Erzeugerzählpfeil = convention générateur / aktif işaret kuralı. Kastenwörter liefert die Präambel (Démonstration, Preuve, Contexte, Exercice / Türetme, İspat, Arka plan, Alıştırma).
- Französische Typografie: Vor `:` `;` `!` `?` und in « » ein normales Leerzeichen tippen (oder keines); babel-french setzt im PDF das richtige geschützte Leerzeichen, der Umwandler auf der Website ebenso. « » direkt tippen (die Präambel aktiviert sie). Apostroph typografisch: ’. In `\texttt`, Code und URLs ändert sich nichts. In TikZ-Bildern lädt die Präambel die TikZ-Bibliothek `babel`, Optionen mit `:` und `!` (Farben wie `red!50`, Polarkoordinaten `(0:1)`) funktionieren.
- Türkische Typografie: Die babel-Kurzbefehle sind aus (`shorthands=off`), also `:` und `!` ohne Leerzeichen davor, Anführungszeichen “ ”. Großes İ und kleines ı genau unterscheiden; Kopfzeilen in Großbuchstaben setzt LaTeX türkisch richtig (i → İ).
- MiKTeX: babel-french braucht die Pakete babel-french und carlisle (scalefnt.sty), babel-turkish das Paket babel-turkish. Alle drei sind seit 04.11.2026 installiert.

## Verweise auf andere Hefte (Zusatzreihen, seit 06.11.2026)

Der Umwandler erkennt nur genau diese Wendungen (mit `~` oder Leerzeichen) und macht daraus Links auf Artikel und Abschnitt. Die Nummer M (13.5, 3) bleibt in allen Sprachen mit Punkt. Endungen im Türkischen mit Apostroph hinter der letzten Zahl (`Temeller~1, Kesim~13.5'te`).

| Zweck | de | en | es | fr | tr | zh |
|---|---|---|---|---|---|---|
| ML-Grundlagen-Heft | `Grundlagen~1` | `Foundations~1` | `Fundamentos~1` (ohne Artikel: „de Fundamentos~1“) | `Fondements~1` (ohne Artikel: „dans Fondements~1“) | `Temeller~1` | `基础篇~1` |
| … mit Abschnitt | `Grundlagen~1, Abschnitt~13.5` | `Foundations~1, Section~13.5` | `Fundamentos~1, sección~13.5` | `Fondements~1, section~13.5` | `Temeller~1, Kesim~13.5` | `基础篇~1~第~13.5~节` |
| zwei Abschnitte | `…, Abschnitte~10.1 und~11.4` | `…, Sections~10.1 and~11.4` | `…, secciones~10.1 y~11.4` | `…, sections~10.1 et~11.4` | `…, Kesim~10.1 ve~11.4` | `…第~10.1~节和第~11.4~节` |
| ML-Pfad-Heft (Teil N = Kap N+7) | `Teil~1` | `Part~1` | `Parte~1` | `Partie~1` | `Kısım~1` | `第~1~部分` |
| Programmieren | `Programmieren, Python~2, Abschnitt~3` | `Programming, Python~2, Section~3` | `Programación, Python~2, sección~3` | `Programmation, Python~2, section~3` | `Programlama, Python~2, Kesim~3` | `编程，Python~2~第~3~节` |
| … später C, C++ | `Programmieren, C~1`, `Programmieren, C++~1` | `Programming, C~1` … | `Programación, C~1` … | `Programmation, C~1` … | `Programlama, C~1` … | `编程，C~1` … |
| Linux und Kommandozeile | `Linux~2, Abschnitt~3` | `Linux~2, Section~3` | `Linux~2, sección~3` | `Linux~2, section~3` | `Linux~2, Kesim~3` | `Linux~2~第~3~节` |

- „Python~3“ allein ist kein Verweis (Sprachversion), deshalb steht bei Programmieren immer der Bereichsname davor. „Linux~6.8“ (Versionsnummer) wird nie verlinkt.
- Titelblock der ML-Grundlagen (Zeile unter dem Untertitel): de `Mathematische Grundlagen für Machine Learning, Grundlagen~N`, en `Mathematical Foundations for Machine Learning, Foundations~N`, es `Fundamentos matemáticos para el aprendizaje automático, Fundamentos~N`, fr `Fondements mathématiques pour l’apprentissage automatique, Fondements~N`, tr `Makine Öğrenmesi için Matematiksel Temeller, Temeller~N`, zh `机器学习数学基础，基础篇~N`. ML-Pfad wie bisher „Arbeitsheft Machine Learning, Teil~N“ / `Workbook Machine Learning, Part~N` usw.
- Auf der Website heißen die Bereiche: Mathematische Grundlagen / Mathematical Foundations / Fundamentos matemáticos / Fondements mathématiques / Matematiksel Temeller / 数学基础; Programmieren / Programming / Programación / Programmation / Programlama / 编程; Linux und Kommandozeile / Linux and the Command Line / Linux y la línea de comandos / Linux et ligne de commande / Linux ve Komut Satırı / Linux 与命令行.

## Abbildungen (Szenentexte)

- Die Bildwörter stehen in tools/szenen/<modul>_teil<N>.py: `s.tr("schluessel", de=…, en=…, es=…, zh=…, fr=…, tr=…)`. fr und tr sind freiwillig; fehlen sie, zeigt das Bild in diesen Sprachen den englischen Text. Zum Übersetzen fr= und tr= ergänzen, das Skript laufen lassen (`python tools/szenen/<modul>_teil<N>.py`).
- Danach exportieren: `python tools/export_szenen.py <modul>/k<N>… --lang fr` und `--lang tr` (ohne --lang alle sechs Sprachen) und für die Hefte `python tools/szenen_pdf.py <modul> "C:/Bücher/<Ordner>/Arbeitshefte" <namen>` (legt abb/fr und abb/tr an). Zahlen in Beschriftungen und Rechnungen bekommen in fr und tr automatisch das Dezimalkomma.
- Französische und türkische Beschriftungen sind oft länger als die englischen: Meldet der Export „breiter als die Spalte“, die Beschriftung kürzen oder umbrechen. Die Schrift (Arial) hat alle Zeichen (é ç œ « » ğ ş ı İ).

## Website

- Ohne `--lang` wandelt der Umwandler Deutsch und jede Sprache um, für die Kap<N>_<Name>_<lang>.tex schon da ist. Mit `--lang fr tr` nur diese; fehlt die Datei, meldet er es.
- Schreiben: `python tools/heft_zu_artikel.py <modul> --kap <N> --lang fr tr`, dann `python build_wissen.py`. Die Artikel landen unter /wissen/fr/… und /wissen/tr/…; im Sprachmenü werden Français und Türkçe für diese Seiten automatisch anklickbar.

Bericht: Seitenzahlen je Sprache, gefundene Fehler im Original.
