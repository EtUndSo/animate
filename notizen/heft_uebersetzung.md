# Auftrag: Arbeitsheft übersetzen (en, es, zh, fr, tr)

Übersetze die deutschen Heftdateien eines Teils nach Englisch, Spanisch, vereinfachtem Chinesisch, Französisch oder Türkisch (der Auftrag nennt die Sprachen). Vorbild sind die ET3-Fassungen in C:\Bücher\ET3\Arbeitshefte (kap1_stufen_en.tex, _es, _zh, Kap1_Faltung_en.tex usw.): dieselbe Struktur, dieselben Umgebungen, dieselben Labels. Präambeln praeambel_en/_es/_zh/_fr/_tr.tex liegen in jedem Heftordner (ET1, ET3, HöMa1, HöMa3, GEMB, EtUndSo\Cybersecurity, EtUndSo\MachineLearning).

Regeln:
- Dateien: Kap<N>_<Name>_<lang>.tex, kap<N>_stufen_<lang>.tex, kap<N>_loesungen_<lang>.tex. Das Hauptdokument bindet `praeambel_<lang>` und die _<lang>-Dateien ein. Titelblock übersetzen.
- Nichts kürzen, nichts ergänzen. Formeln, Labels, Zahlenwerte unverändert. Text in Formeln (`\text{...}`, Indizes aus Wörtern wie `W_\text{außen}`) wird übersetzt. Zahlwörter werden umgerechnet: Milliarde = billion = mil millones = 十亿 = milliard = milyar, Billion = trillion = billón = 万亿 = billion (fr!) = trilyon. Dezimaltrennzeichen: en und zh Punkt (0.7), es, fr und tr Komma (0{,}7). Einheiten bleiben.
- Englisch amerikanische Schreibweise. Begriffe: Stufe = stage, Aufgabe = exercise, Spannung = voltage, Strom = current, Knoten = node, Masche = mesh/loop, Zählpfeil = reference arrow, Ersatzquelle = equivalent source. Das Wort Arbeitsheft wird workbook, cuaderno, 本册 (so erkennt es der Umwandler).
- Wörter: Verbindlich sind die Bildwörter in tools/szenen/<modul>_teil<N>.py (`s.tr`), die Titel in tools/heft_zu_artikel.py (MODULE["<modul>"], dort stehen auch die fr- und tr-Titel aller Teile) und die Wahl aus Teil 1: en ground, curl-free; es tensión, nudo, masa; zh 电位, 接地点. Zählpfeile: en passive sign convention (Verbraucherzählpfeil), active sign convention (Erzeugerzählpfeil).
- Titelblock wie ET3: „Workbook“, „Cuaderno de trabajo“, 练习册; Datum en `31~October 2026`. Im Fließtext heißt das Heft aber workbook, cuaderno, 本册.
- Verweise auf andere Hefte (seit 09.11.2026 in allen Modulen „Kapitel“): `Chapter~2`, `capítulo~2`, `第~2~章`, `chapitre~2`, `Bölüm~2`, aus einem anderen Modul mit Kurznamen (`HöMa1, Chapter~2`). Genau die Wendungen im Abschnitt „Verweise auf andere Hefte“ unten; dort wird auch „…, Abschnitt M“ zum Link auf den Abschnitt.
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
| Verweis auf ein Heft (seit 09.11.2026) | `chapitre~2` (Artikel: „le chapitre~2“, „du chapitre~2“, am Satzanfang „Le chapitre~2“) | `Bölüm~2` (Endung mit Apostroph: `Bölüm~2'de`) |
| Absatz „So arbeitest du …“ | „Comment travailler avec ce cahier.“ | „Bu çalışma kitabıyla nasıl çalışılır?“ |
| Absatz „Ein Prinzip …“ | „Un principe derrière tous les résultats.“ | „Tüm sonuçların ardındaki tek ilke.“ |
| kernbox „Die Antwort in drei Sätzen (…)“ | „La réponse en trois phrases (à la fin du cahier, elles devraient vous sembler évidentes)“ | „Üç cümlede cevap (çalışma kitabının sonunda bunlar size apaçık gelmeli)“ |
| kernbox „Das Wichtigste“ / „… bis hier“ | „L’essentiel“ / „L’essentiel jusqu’ici“ | „Temel noktalar“ / „Buraya kadarki temel noktalar“ |
| Abschnitt „Lösungen“ | Solutions | Çözümler |
| „Die Idee.“ | „L’idée.“ | „Fikir.“ |
| `\begin{beispiel}{}` (setzt „Beispiel.“) | `\begin{beispiel}{}` (setzt „Exemple.“) | `\begin{beispiel}{}` (setzt „Örnek.“) |
| Datum im Titelblock | `31~octobre 2026` | `31~Ekim 2026` |

- Anrede: fr „vous“, tr „siz“ (wie die Oberfläche und die Hinweise der Website). Ton sachlich, nicht steif.
- Begriffe ET: Stufe = étape / aşama, Aufgabe = exercice / alıştırma, Spannung = tension / gerilim, Strom = courant / akım, Knoten = nœud / düğüm, Masche = maille / çevre, Ersatzquelle = source équivalente / eşdeğer kaynak, Masse (Bezugspunkt) = masse / toprak, Potenzial = potentiel / potansiyel, Verbraucherzählpfeil = convention récepteur / pasif işaret kuralı, Erzeugerzählpfeil = convention générateur / aktif işaret kuralı. Kastenwörter liefert die Präambel (Démonstration, Preuve, Contexte, Exercice / Türetme, İspat, Arka plan, Alıştırma).
- Französische Typografie: Vor `:` `;` `!` `?` und in « » ein normales Leerzeichen tippen (oder keines); babel-french setzt im PDF das richtige geschützte Leerzeichen, der Umwandler auf der Website ebenso. « » direkt tippen (die Präambel aktiviert sie). Apostroph typografisch: ’. In `\texttt`, Code und URLs ändert sich nichts. In TikZ-Bildern lädt die Präambel die TikZ-Bibliothek `babel`, Optionen mit `:` und `!` (Farben wie `red!50`, Polarkoordinaten `(0:1)`) funktionieren.
- Türkische Typografie: Die babel-Kurzbefehle sind aus (`shorthands=off`), also `:` und `!` ohne Leerzeichen davor, Anführungszeichen “ ”. Großes İ und kleines ı genau unterscheiden; Kopfzeilen in Großbuchstaben setzt LaTeX türkisch richtig (i → İ).
- MiKTeX: babel-french braucht die Pakete babel-french und carlisle (scalefnt.sty), babel-turkish das Paket babel-turkish. Alle drei sind seit 04.11.2026 installiert.

## Beispiel-Kästen (seit 09.11.2026, alle Sprachen)

Beispiele stehen im Kasten `\begin{beispiel}[Wort]{Titel} … \end{beispiel}` (UEBERARBEITUNG.md §2a). Auf der Website ist er zugeklappt.
- Der Name `beispiel` bleibt in jeder Sprache; nur Titel und optionales Wort werden übersetzt. Das Wort „Beispiel“ samt Doppelpunkt und Schlusspunkt setzt die Sprachpräambel selbst (Example, Ejemplo, 例, Exemple, Örnek), es gehört nicht in den Titel.
- Beispiele: `\begin{beispiel}{}` → überall `\begin{beispiel}{}`; `\begin{beispiel}{ein Rezept für die Wurzel aus 2}` → `{a recipe for the square root of 2}`; `\begin{beispiel}[Rechenbeispiel 2]{Titel}` → `[Worked example 2]` / `[Ejemplo numérico 2]` / `[算例 2]` / `[Exemple de calcul 2]` / `[Sayısal örnek 2]`; `[Gegenbeispiel]` → `[Counterexample]` / `[Contraejemplo]` / `[反例]` / `[Contre-exemple]` / `[Karşı örnek]`; `[Beispiele]` → `[Examples]` / `[Ejemplos]` / `[例]` / `[Exemples]` / `[Örnekler]`.
- Titel ohne Schlusspunkt (? und ! bleiben). fr: kein Leerzeichen vor dem Doppelpunkt nötig, die Präambel setzt „Exemple~:“.
- Anfang und Ende des Kastens an genau derselben Stelle wie im Deutschen; der Strukturvergleich zählt die Umgebung mit.

## Verweise auf andere Hefte (alle Module, seit 09.11.2026)

Jedes Heft heißt „Kapitel N“, gezählt in seinem Bereich (ML-Grundlagen, ML-Pfad, Python, C, C++, Linux, jedes übrige Modul). Der Umwandler erkennt genau diese Wendungen (mit `~` oder Leerzeichen) und macht daraus Links auf Artikel und Abschnitt. Die Nummer M (13.5, 3) bleibt in allen Sprachen mit Punkt. Vollständige Formentabelle (Modulnamen, Bereichsnamen, Titelzeilen, türkische Endungen): `notizen/kapitel_umstellung.md`.

| Zweck | de | en | es | fr | tr | zh |
|---|---|---|---|---|---|---|
| Heft im selben Bereich | `Kapitel~2` | `Chapter~2` | `capítulo~2` mit Artikel: „el capítulo~2“, „del capítulo~2“, „al capítulo~2“, „en el capítulo~2“; „(capítulo~2)“; Satzanfang „El capítulo~2“ | `chapitre~2`: „le chapitre~2“, „du chapitre~2“, „au chapitre~2“, „dans le chapitre~2“; „(chapitre~2)“; Satzanfang „Le chapitre~2“ | `Bölüm~2` (immer groß; Endung an der Zahl: `Bölüm~2'de`) | `第~2~章` |
| … mit Abschnitt | `Kapitel~2, Abschnitt~13.5` | `Chapter~2, Section~13.5` | `capítulo~2, sección~13.5` | `chapitre~2, section~13.5` | `Bölüm~2, Kesim~13.5` | `第~2~章第~13.5~节` |
| zwei Abschnitte | `…, Abschnitte~10.1 und~11.4` | `…, Sections~10.1 and~11.4` | `…, secciones~10.1 y~11.4` | `…, sections~10.1 et~11.4` | `…, Kesim~10.1 ve~11.4` | `…第~10.1~节和第~11.4~节` |
| anderer Bereich oder anderes Modul | `Python, Kapitel~2, Abschnitt~3` | `Python, Chapter~2, Section~3` | `Python, capítulo~2, sección~3` | `Python, chapitre~2, section~3` | `Python, Bölüm~2, Kesim~3` | `Python~第~2~章第~3~节` |
| Kurznamen | Python, C, C++, Linux, Cybersecurity, Machine Learning, Grundlagen, ET1, ET3, GEMB1, HöMa1, HöMa3 | … Cybersecurity, Machine Learning, Foundations … | … Ciberseguridad, Aprendizaje automático, Fundamentos … | … Cybersécurité, Apprentissage automatique, Fondements … | … Siber Güvenlik, Makine Öğrenmesi, Temeller … | … 网络安全, 机器学习, 数学基础 … (lateinische Kurznamen mit `~` vor 第, chinesische direkt: `数学基础第~1~章`) |

- Nicht mehr verwenden: `Part~N`, `Parte~N`, `Partie~N`, `Kısım~N`, `第~N~部分`, `Foundations~N`, `Fundamentos~N`, `Fondements~N`, `Temeller~N`, `基础篇~N`, `Programming, Python~N`, `Linux~N` (der Umwandler erkennt sie nur übergangsweise). „Python~3“ und „Linux~6.8“ allein sind Versionen.
- Titelzeile (unter dem Untertitel): en `Workbook <Bereich>, Chapter~N. Version: …`, es `Cuaderno de trabajo <Bereich>, capítulo~N. Versión: …`, zh `<Bereich> 练习册，第~N~章。版本：…`, fr `Cahier d’exercices <Bereich>, chapitre~N. Version : …`, tr `Çalışma Kitabı <Bereich>, Bölüm~N. Sürüm: …`; <Bereich> je Sprache in `notizen/kapitel_umstellung.md` (z. B. en „Machine Learning, Mathematical Foundations“, „Programming, Python“).
- Auf der Website heißen die Bereiche: Mathematische Grundlagen / Mathematical Foundations / Fundamentos matemáticos / Fondements mathématiques / Matematiksel Temeller / 数学基础; Programmieren / Programming / Programación / Programmation / Programlama / 编程 (darin Python, C, C++); Linux und Kommandozeile / Linux and the Command Line / Linux y la línea de comandos / Linux et ligne de commande / Linux ve Komut Satırı / Linux 与命令行. Jedes Heft steht im Baum als „Kapitel N: Titel“ (Chapter, Capítulo, 第 N 章, Chapitre, Bölüm).

## Abbildungen (Szenentexte)

- Die Bildwörter stehen in tools/szenen/<modul>_teil<N>.py: `s.tr("schluessel", de=…, en=…, es=…, zh=…, fr=…, tr=…)`. fr und tr sind freiwillig; fehlen sie, zeigt das Bild in diesen Sprachen den englischen Text. Zum Übersetzen fr= und tr= ergänzen, das Skript laufen lassen (`python tools/szenen/<modul>_teil<N>.py`).
- Danach exportieren: `python tools/export_szenen.py <modul>/k<N>… --lang fr` und `--lang tr` (ohne --lang alle sechs Sprachen) und für die Hefte `python tools/szenen_pdf.py <modul> "C:/Bücher/<Ordner>/Arbeitshefte" <namen>` (legt abb/fr und abb/tr an). Zahlen in Beschriftungen und Rechnungen bekommen in fr und tr automatisch das Dezimalkomma.
- Französische und türkische Beschriftungen sind oft länger als die englischen: Meldet der Export „breiter als die Spalte“, die Beschriftung kürzen oder umbrechen. Die Schrift (Arial) hat alle Zeichen (é ç œ « » ğ ş ı İ).

## Website

- Ohne `--lang` wandelt der Umwandler Deutsch und jede Sprache um, für die Kap<N>_<Name>_<lang>.tex schon da ist. Mit `--lang fr tr` nur diese; fehlt die Datei, meldet er es.
- Schreiben: `python tools/heft_zu_artikel.py <modul> --kap <N> --lang fr tr`, dann `python build_wissen.py`. Die Artikel landen unter /wissen/fr/… und /wissen/tr/…; im Sprachmenü werden Français und Türkçe für diese Seiten automatisch anklickbar.

Bericht: Seitenzahlen je Sprache, gefundene Fehler im Original.
