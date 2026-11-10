# Umstellung auf „Kapitel N“ (Wunsch des Users, 09.11.2026)

Ziel: einheitliche Benennung auf der ganzen Website und in allen Heften. Jedes Heft heißt im Baum „Kapitel N: Titel“, gezählt in seinem Bereich. Jedes Modul zeigt zuerst seine Abkürzung, dann den vollen Namen. **Seitenadressen bleiben.** Herkunft und Entscheidungen: `notizen/zusatzreihen_stand.md`, Abschnitt „Umbenennung“.

Zwei Agenten: Agent 1 (Werkzeug: Formen, Konverter, Website, Skript, Doku) ist **fertig**. Agent 2 (Hefte umstellen, PDFs, neu umwandeln) ist **fertig** (10.11.2026, Abschnitt 6).

## 1. Formentabelle

### Kapitelwort und Verweise

| | de | en | es | fr | tr | zh |
|---|---|---|---|---|---|---|
| Kapitelwort (Baum) | Kapitel 1: Titel | Chapter 1: Title | Capítulo 1: título | Chapitre 1 : titre | Bölüm 1: Başlık | 第 1 章：标题 |
| Heft im selben Bereich | `Kapitel~2` | `Chapter~2` | `capítulo~2`; mit Artikel „el capítulo~2“, „del capítulo~2“, „al capítulo~2“, „en el capítulo~2“; „(capítulo~2)“; Satzanfang „El capítulo~2“ | `chapitre~2`; „le chapitre~2“, „du chapitre~2“, „au chapitre~2“, „dans le chapitre~2“; „(chapitre~2)“; Satzanfang „Le chapitre~2“ | `Bölüm~2` (immer groß) | `第~2~章` |
| Plural | `Kapitel~2 und~3`, „in den Kapiteln~2 bis~4“ | `Chapters~2 to~4` | „los capítulos~2 a~4“ | „les chapitres~2 à~4“ | `Bölümler~2 ve~3` | `第~2~章和第~3~章` |
| mit Abschnitt | `Kapitel~2, Abschnitt~13.5` | `Chapter~2, Section~13.5` | `capítulo~2, sección~13.5` | `chapitre~2, section~13.5` | `Bölüm~2, Kesim~13.5` | `第~2~章第~13.5~节` |
| zwei Abschnitte | `Kapitel~2, Abschnitte~10.1 und~11.4` | `…, Sections~10.1 and~11.4` | `…, secciones~10.1 y~11.4` | `…, sections~10.1 et~11.4` | `…, Kesim~10.1 ve~11.4` | `…第~10.1~节和第~11.4~节` |
| anderer Bereich oder anderes Modul | `Python, Kapitel~2, Abschnitt~3` | `Python, Chapter~2, Section~3` | `Python, capítulo~2, sección~3` | `Python, chapitre~2, section~3` | `Python, Bölüm~2, Kesim~3` | `Python~第~2~章第~3~节` (lateinischer Kurzname mit `~`), `数学基础第~1~章` (chinesischer direkt) |

- Die Abschnittsnummer M bleibt in allen Sprachen mit Punkt (13.5).
- Türkisch: „Abschnitt“ ist schon **Kesim**, „Kapitel“ wird **Bölüm** (keine Kollision; „bölüm“ kleingeschrieben heißt in Formeln auch „Quotient“, deshalb erkennt der Umwandler nur großes „Bölüm“). Die Website ersetzt „çalışma kitabı“ ohnehin durch „bölüm“.
- Versionen bleiben Text: „Python 3.13“, „Linux 6.8“, „C11“, „C++17“; „Python~3“/„Linux~2“ allein sind keine Verweise.
- Gewöhnliche Wörter („zum Teil“, „Realteil“, „Teilchen“, „teilweise“) und Aufgabenteile („Teil a)“, „Dein eigenes Gerät, Teil 1: …“) bleiben.

### Kurznamen (für Verweise über Bereiche und Module)

| Bereich | de | en | es | fr | tr | zh |
|---|---|---|---|---|---|---|
| prog Python / C / C++ | Python / C / C++ | gleich | gleich | gleich | gleich | gleich |
| linux | Linux | Linux | Linux | Linux | Linux | Linux |
| cyber | Cybersecurity | Cybersecurity | Ciberseguridad | Cybersécurité | Siber Güvenlik | 网络安全 |
| ml Pfad (ab T08) | Machine Learning | Machine Learning | Aprendizaje automático | Apprentissage automatique | Makine Öğrenmesi | 机器学习 |
| ml Mathematische Grundlagen (T01–T06) | Grundlagen | Foundations | Fundamentos | Fondements | Temeller | 数学基础 |
| et1, et3, gemb1, hm1, hm3 | ET1, ET3, GEMB1, HöMa1, HöMa3 | gleich | gleich | gleich | gleich | gleich |

Quelle im Code: `MODULE[..]["kurz"]` bzw. `["bereiche"][..]["kurz"]` in `tools/heft_zu_artikel.py`.

### Modulnamen (Baum, Brotkrumen, Suche; `pfad:`)

| | de | en | es | fr | tr | zh |
|---|---|---|---|---|---|---|
| et1 | ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse | ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis | ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos | ET1 – Fondements du génie électrique 1 : introduction à l’analyse des circuits | ET1 – Elektrik Mühendisliğinin Temelleri 1: Devre Analizine Giriş | ET1 – 电气工程基础 1：电路分析导论 |
| et3 | ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme | ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems | ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas | ET3 – Fondements du génie électrique 3 : signaux et systèmes | ET3 – Elektrik Mühendisliğinin Temelleri 3: Sinyaller ve Sistemler | ET3 – 电气工程基础 3：信号与系统 |
| gemb1 | GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 | GEMB1 – Fundamentals of Electronic Materials and Devices 1 | GEMB1 – Fundamentos de materiales y dispositivos electrónicos 1 | GEMB1 – Fondements des matériaux et composants électroniques 1 | GEMB1 – Elektronik Malzemeler ve Elemanların Temelleri 1 | GEMB1 – 电子材料与器件基础 1 |
| hm1 / hm3 | HöMa1 – Höhere Mathematik 1 / HöMa3 – Höhere Mathematik 3 | HöMa1 – Higher Mathematics 1 | HöMa1 – Matemáticas superiores 1 | HöMa1 – Mathématiques supérieures 1 | HöMa1 – Yüksek Matematik 1 | HöMa1 – 高等数学 1 |

Informatik-Bereiche unverändert: Programmieren (darin Python, C, C++), Linux und Kommandozeile, Cybersecurity, Machine Learning (darin Mathematische Grundlagen). C und C++ sind jetzt zwei eigene Äste „C“ und „C++“ (vorher gemeinsam „C und C++“; es gab noch kein Heft).

### Titelzeile des PDFs (`{\small …}` unter dem Untertitel; `TITELZEILE` im Umwandler)

de `Arbeitsheft <B>, Kapitel~N. Stand: …` · en `Workbook <B>, Chapter~N. Version: …` · es `Cuaderno de trabajo <B>, capítulo~N. Versión: …` · fr `Cahier d’exercices <B>, chapitre~N. Version : …` · tr `Çalışma Kitabı <B>, Bölüm~N. Sürüm: …` · zh `<B> 练习册，第~N~章。版本：…`

<B> (Bereich, `["titel"]`): bei den ET-Modulen der volle Modulname wie im Baum (Entscheidung Agent 1: lesbar und einheitlich, die Zeile bricht im `\small` höchstens einmal um), z. B. „Arbeitsheft ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme, Kapitel~2“. Sonst: „Cybersecurity“, „Machine Learning“, „Machine Learning, Mathematische Grundlagen“ (en „Machine Learning, Mathematical Foundations“, es „Aprendizaje automático, Fundamentos matemáticos“, fr „Apprentissage automatique, Fondements mathématiques“, tr „Makine Öğrenmesi, Matematiksel Temeller“, zh „机器学习 · 数学基础“), „Programmieren, Python“ (en „Programming, Python“, es „Programación, Python“, fr „Programmation, Python“, tr „Programlama, Python“, zh „编程 · Python“), C/C++ entsprechend, „Linux und Kommandozeile“ (übersetzt wie im Baum). Der Kopfkommentar der Hauptdatei („%  Arbeitsheft …, Kapitel N: Titel“) folgt derselben Form.

### Überblicksartikel

„Überblick: <Titel aus \LARGE>“, ohne Heftnummer (vorher „Überblick: Grundlagen 1 – …“, „Überblick: Linux 1 – …“).

### Türkische Endungen (hängen an der Zahl, nicht am Wort; ändern sich durch die Umstellung nicht)

| Zahl (gesprochen) | -de (in) | -den (aus) | -e (zu) | -in (von) |
|---|---|---|---|---|
| 1 (bir) | 1'de | 1'den | 1'e | 1'in |
| 2 (iki) | 2'de | 2'den | 2'ye | 2'nin |
| 3 (üç) | 3'te | 3'ten | 3'e | 3'ün |
| 4 (dört) | 4'te | 4'ten | 4'e | 4'ün |
| 5 (beş) | 5'te | 5'ten | 5'e | 5'in |
| 6 (altı) | 6'da | 6'dan | 6'ya | 6'nın |
| 7 (yedi) | 7'de | 7'den | 7'ye | 7'nin |
| 8 (sekiz) | 8'de | 8'den | 8'e | 8'in |
| 9 (dokuz) | 9'da | 9'dan | 9'a | 9'un |
| 10 (on) | 10'da | 10'dan | 10'a | 10'un |

11–19 wie die letzte Ziffer (13'te, 16'da), 20 (yirmi) 20'de/20'den/20'ye/20'nin. Bei „Bölüm~2, Kesim~13.5'te“ steht die Endung an der letzten Zahl (13.5 = „on üç nokta beş“ → wie 5).

## 2. Stand (Agent 1, 09.11.2026)

- **`tools/heft_zu_artikel.py`:**
  - ET-Module: neuer `pfad` (Modulname mit Abkürzung), `kurz`, `alt_modul` (alter Name für Übergangsverweise); `basis` unverändert.
  - Jedes Modul hat Bereiche (ohne Liste: ein Bereich), jeder mit `kurz` und `titel`; ml/prog mit festem `slug` (mathematische-grundlagen, python, c, cpp). Alte Heftnamen stehen als `alt` (Übergang).
  - Neu: `KAPITEL`, `KAPITEL_RE`, `TITELZEILE`, `kapitel_nr()`, `titelzeile()`, `heft_adresse()`. Jeder Artikel bekommt `knoten: Kapitel N: Titel` und `adresse:`; Überblick ohne Nummer.
  - Verweise (`verweis_arten`): neu „<Kurzname>, Kapitel N“ über alle Module, „Kapitel N“ im eigenen Bereich; übergangsweise alt „Teil N“, „Grundlagen N“, „Programmieren, Python N“, „Linux N“, „<alter Modulname>, Teil N“. Jetzt für **alle** Module mit Abschnitt-Ankern (vorher nur die Zusatzreihen).
  - Fehler behoben: „Teile 2 durch diese Zahl“ (prog Kap. 1) war ein Link auf Python 2; „Höhere Mathematik 1, Teil 2“ (prog Kap. 2) zeigte auf Python 2, jetzt auf HöMa1 Kapitel 2; „…, Teil 5, Abschnitt 8“ (prog Kap. 3) ist jetzt ein Link.
  - Adressen bleiben auch nach der Heft-Umstellung: Ein Abschnitt „Von Grund auf: Was aus Kapitel 9 gebraucht wird“ behält die Datei „…-was-aus-teil-9-…“, wenn es sie unter content/ schon gibt (`datei_stamm`; betrifft et1 Kap. 10, gemb1 Kap. 2, 5, 7 und 16).
- **`build_wissen.py`:** neues Kopffeld `adresse:` (Slugs der Knoten, die Adresse bleibt, wenn `pfad:` die Namen ändert); Hinweise (`_reihe.md`) finden Knoten auch über den Namen; „Verwendet in“ zeigt „<Bereich/Modulkürzel> › Kapitel N: Titel › Artikel“.
- **`web/index.html`:** keine Änderung nötig (die Modulübersicht kommt aus `tree.json`).
- **content/** (veröffentlichte Kapitel neu umgewandelt): 1663 Dateien, 1657 geändert, 6 gleich (`_reihe*`). Änderungen nur in Kopfzeilen: `adresse:` neu (1657), `knoten:` neu (1323) bzw. geändert (334), `pfad:` geändert (1311, Modulnamen), Überblickstitel (24); im Text nur Links (5 neu verlinkt, 3 Ziel geändert/entfernt: die drei Fehler oben). Sicherung: `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\kapitel\content_vorher`.
  - Nicht aus dem Heft erzeugt, nur Kopfzeilen nachgezogen (`kapitel_umstellung.py --kopf`): hm3 Kap. 3 (alter Stand, `kap3_stufen.tex` in Überarbeitung) und **et3 Kap. 2 en/es/zh** (die Übersetzungen passen schon vor der Umstellung nicht mehr zur deutschen Gliederung: 7 statt 9 Artikel; der alte Umwandler scheitert genauso).
  - hm1 Kap. 3: nur de, en (es/zh unvollständig übersetzt, `kap3_stufen_es/zh.tex` fehlen; content hat für es/zh nichts).
  - gemb1 ab 16 nicht umgewandelt, keine Ordner entstanden.
- **Website** neu gebaut: 702 Artikel; HTML-Menge unter web/wissen/ genau gleich (1677 Dateien). Server-Stichprobe: Baum „ET1 – … / Kapitel 1: …“, Brotkrumen „Wissen › Informatik › Programmieren › Python › Kapitel 3: …“, Link prog → HöMa1 Kap. 5 #stufe-8 lädt.
- **`tools/kapitel_umstellung.py`** (neu): Probelauf und `--anwenden` für alle .tex; `--md` für Artikel, die nicht aus dem Heft entstehen; `--kopf` für deren Kopfzeilen. **Nicht angewendet.**
- **Doku:** `heft_auftrag_zusatzreihen.md` (Nummern, ML-Bereiche, Verweise, Dateien/Titelzeile), `heft_auftrag_et1/gemb1/hm1/hm3.md` (Titelzeile), `UEBERARBEITUNG.md` §4 und §6a, `ueberarbeitung_auftrag.md`, `heft_uebersetzung.md` (Abschnitt „Verweise auf andere Hefte“ neu), `uebersetzung_brief_zusatzreihen.md` (Feste Wendungen), `tools/themenkarte.py` + `notizen/themenkarte.md` (neu erzeugt, Handteil umgestellt), Lernpfade `C:\Bücher\EtUndSo\Programmieren\Recherche\LERNPFAD.md` und `…\Linux\Recherche\LERNPFAD.md` (Hefte als „Python, Kapitel N“, „C, Kapitel N“, „Kapitel N“ bzw. „Linux, Kapitel N“, Hinweis oben). ML- und Cyber-Lernpfad nennen Hefte nur mit T-Nummern („# Teil 1: Der Stamm“ ist ein Dokumentteil) und bleiben.
- **Szenen:** keine sichtbaren Texte mit Heftnamen (nur Docstrings/Kommentare „ET1 Teil 3“), nichts zu tun.

## 3. Probelauf `tools/kapitel_umstellung.py` (alle Module, alle Sprachen, auch hm3 `kap3_*` und GEMB 16–19)

338 Dateien würden geändert. Verweise / Titelzeile+Kopfkommentar je Modul und Sprache:

| Modul | de | en | es | fr | tr | zh |
|---|---|---|---|---|---|---|
| et1 | 175 / 22 | 175 / 22 | 175 / 22 (58 mit Artikel) | – | – | 175 / 22 |
| et3 | 50 / 16 | 50 / 16 | 50 / 16 (24 Artikel) | – | – | 50 / 16 |
| gemb1 (1–17, 19) | 234 / 36 | – | – | – | – | – |
| hm1 | 133 / 20 | 26 / 6 | 18 / 6 (11 Artikel) | – | – | 18 / 6 |
| hm3 | 84 / 16 | – | – | – | – | – |
| cyber | 0 / 2 | – | – | – | – | – |
| ml | 253 / 10 | 127 / 6 | 127 / 6 (125 Artikel) | 127 / 6 (125 Artikel) | 127 / 6 | 127 / 6 |
| prog | 76 / 6 (4 mit Kurzname) | – | – | – | – | – |
| linux | 6 / 2 (1 mit Kurzname) | – | – | – | – | – |

Prüfung (Agent 1): Ergebnis im Speicher auf Doppelungen, Artikel-Doppel, Reste alter Formen geprüft; Hefte (Kopien) umgestellt und umgewandelt: 740 Artikel, Linkziele gleich wie heute, dazu neue Links aus bisher unverlinkten „Python~1“ in prog; keine Adresse ändert sich.

**Grenzfälle (im Skript behandelt):**
- en „polynomial part 0“ (hm1 Kap. 3 Lösungen) und „part 1: … part 2: …“ (et3 Kap. 1): keine Heftverweise; das Skript nimmt im Englischen nur großes „Part“.
- cyber Kap. 1: „Dein eigenes Gerät, Teil 1: …“/„Teil 2: …“ in Aufgabentiteln: Aufgabenteile, übersprungen.
- prog Kap. 1: „Teile 2 durch diese Zahl“ (2×): Rechenanweisung, nur gemeldet.
- prog: „Python 3“, „Python 2“ mit gewöhnlichem Leerzeichen (10×, Kap. 1) sind Versionen und bleiben; nur „Python~N“ mit Tilde gilt als Heft.
- Kommentare werden nicht geändert, außer dem Kopfkommentar der Hauptdatei („%  Python 1, Abschnitte 1-3“ bleibt).
- es/fr: Artikel und Großschreibung passend gesetzt („de la Parte~2“ → „del capítulo~2“, „La Parte~1“ → „El capítulo~1“, „Según Fundamentos~1“ → „Según el capítulo~1“, „de Fondements~1“ → „du chapitre~1“, „Dans Fondements~1“ → „Dans le chapitre~1“, Satzanfang „Fondements~1 a fourni“ → „Le chapitre~1 a fourni“).
- zh: „基础篇~1~第~13.5~节“ → „第~1~章第~13.5~节“ (Abstand vor 第 entfällt).

**Bleibt für Agent 2 von Hand:**
- prog `kap2_stufen_b.tex`: „wie \verb|2 ** 0.5| in Kapitel~1 (Kapitel~1, Abschnitt~4.5)“ (aus „in Python~1 (Programmieren, Python~1, …)“) glätten, etwa „wie … in Kapitel~1, Abschnitt~4.5“.
- Deutsch: „der Teil“ ist männlich, „das Kapitel“ sächlich. Artikel vor „Teil N“ kamen nicht vor; ein Pronomen „er“, das sich auf „Teil N“ bezog, wäre jetzt „es“ (beim Durchsehen der Liste darauf achten).
- es/fr: in der Liste die Treffer mit „Artikel“ querlesen (Pronomen, die sich auf „la Parte“ bezogen).

## 4. Schritte für Agent 2

1. **Sicherung** (Scratchpad): alle `*.tex` der neun Heftordner (`MODULE[..]["quelle"]`), `content/`, die Liste `find web/wissen -name '*.html' | sort`.
2. **Probelauf:** `PYTHONIOENCODING=utf-8 python tools/kapitel_umstellung.py --aus <scratchpad>/liste.txt`. Zahlen mit Abschnitt 3 vergleichen (abweichend nur, wenn inzwischen jemand Hefte geändert hat; neue Treffer kurz ansehen).
3. **Anwenden:** `python tools/kapitel_umstellung.py --anwenden`; ein zweiter Probelauf meldet nur noch die Grenzfälle („gemeldet“, „übersprungen“). Dann die Handstellen aus Abschnitt 3.
4. **PDFs neu bauen** (jede Hauptdatei hat eine neue Titelzeile, also alle): im Heftordner dreimal `pdflatex -interaction=nonstopmode Kap<N>_<Name>[_<lang>].tex` für de, en, es, fr, tr, für zh `xelatex`. `grep -c '^!'` = 0. Vor dem Löschen von .aux/.log/.out/.toc: `python tools/heft_zu_artikel.py <modul> --kap <N> --lang <lang> --pruefen --katex --aux <Heftordner>` ohne Warnung. Dann `python tools/pdf_pruefen.py <pdf> <scratchpad>/pdf` (PDF nie als Bild lesen). Umfang: et1 1–11 (de en es zh), et3 1–8 (de en es zh), hm1 1–10 (de) und 1–3 (en es zh, es/zh nur soweit vollständig), hm3 1–8 (de; Kap. 3 nur, wenn die angehaltene Überarbeitung übersetzt), gemb1 1–17 und 19 (de), cyber 1, ml 1–5 (de) und 1–3 (en es zh fr tr), prog 1–3, linux 1. Achtung: Die Titelzeile der ET-Module ist länger; prüfen, dass der Titelblock auf Seite 1 bleibt.
5. **Neu umwandeln** mit denselben Ausnahmen wie Agent 1 (Skript `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\kapitel\umwandeln.sh`, erst mit `--pruefen --katex`, dann ohne):
   - et1 1–11; et3 1, 3–8, et3 2 nur `--lang de`; gemb1 1–15 (**nie** ab 16); hm1 1, 2, 4–10, hm1 3 nur `--lang de en`; hm3 1, 2, 4–8 (**nie** 3 aus dem .tex); cyber 1; ml 1–5; prog 1–3; linux 1.
   - Danach die Artikel, die nicht aus dem Heft entstehen: `python tools/kapitel_umstellung.py --md content/hm3/03-kurvenintegrale content/et3/02-laplace-transformation` (Probelauf: 8 Treffer de, 1 en, 1 zh), dann mit `--anwenden`. Kopfzeilen dort sind schon richtig (`--kopf` meldet 0).
   - Danach `ls content/gemb1` endet bei 15.
6. **Vergleich content/** gegen die Sicherung (Agent 1 hat dafür `…\scratchpad\kapitel\vergleich.py <sicherung>` benutzt): erwartet nur Linktexte und Text „Teil N“ → „Kapitel N“ usw., dieselben Linkziele, dieselben Dateinamen. Neue Dateinamen oder fehlende Dateien = Adressänderung: klären, bevor es weitergeht.
7. `PYTHONIOENCODING=utf-8 python build_wissen.py` (etwa 7 min, im Hintergrund, Ausgabe filtern); HTML-Menge unter web/wissen/ vorher/nachher genau gleich. Danach `python tools/themenkarte.py`.
8. **Übergangsformen im Umwandler:** behalten, bis die offenen Übersetzungen (et3 Kap. 2 en/es/zh, hm1 Kap. 3 es/zh) und jede Übersetzung, die noch aus einem alten Stand entsteht, in der neuen Form fertig sind; danach entfernen: in `verweis_arten` die Schritte 2, 3 und 5 (alte Formen), die Schlüssel `alt`, `alt_modul`, `praefix`, `extern`, `teil` und `TEIL_RE` (wird dann nur noch von `webtext` ohne `kap` benutzt). Prüfen vorher mit `grep`, dass in keinem Heft mehr „Teil~N“, „Grundlagen~N“, „Programmieren, Python~N“, „Linux~N“ steht (der zweite Probelauf zeigt das).

## 5. Offene Fragen an den User (vorläufig entschieden 09.11.2026; der User kann sie noch umwerfen)

- Titelzeile der ET-Module: voller Name („Arbeitsheft ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse, Kapitel~10“) oder kurz („Arbeitsheft ET1, Kapitel~10“)? **Entschieden: voller Name bleibt.** Geprüft: Titelblock und Inhaltsverzeichnis stehen in allen 144 PDFs auf Seite 1, die Titelzeile hat höchstens zwei Zeilen.
- GEMB-Ergänzungshefte: **Entschieden: „Kapitel N: <Titel> (Ergänzung)“** statt „Kapitel N: Ergänzung: <Titel>“, in allen sechs Sprachen (en „(Supplement)“, es „(complemento)“, fr „(complément)“, tr „(Ek)“, zh „（补充）“; es/fr-Titel beginnen jetzt groß). Umgesetzt in `MODULE["gemb1"]` (Kap. 19–28, Slugs unverändert), im \LARGE-Titel und Kopfkommentar von `Kap19_Licht.tex` und als Regel in `heft_auftrag_gemb1.md`.
- zh-Kurzname der ML-Grundlagen: **Entschieden: „数学基础“ bleibt** (statt bisher „基础篇“).

## 6. Stand Agent 2 (10.11.2026)

- **Sicherung:** `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\kapitel2` (`tex_vorher/`, `pdf_vorher/`, `content_vorher/`, `html_vorher.txt`; Skripte `bauen.py`, `auswerten.py`, `titelblock.py`, `vergleich2.py`, `absatz_test.py`).
- **Hefte umgestellt** (`kapitel_umstellung.py --anwenden`, Zahlen genau wie Abschnitt 3): 338 .tex-Dateien, also jedes Heft in jeder Sprache (Titelzeile): et1 11 × de/en/es/zh, et3 8 × de/en/es/zh, gemb1 18 (1–17, 19), hm1 10 de + 3 en/es/zh (Kap. 3 es/zh nur die Hauptdatei), hm3 8, cyber 1, ml 5 de + 3 × en/es/fr/tr/zh, prog 3, linux 1. Zweiter Probelauf: 0 Dateien, nur die bekannten Grenzfälle (cyber 2 Aufgabenteile, prog 10 Versionen, 2 „Teile 2 durch“).
- **Von Hand:** prog `kap2_stufen_b.tex` geglättet („in Kapitel~1, Abschnitt~4.5“); GEMB 19 Titel (s. o.); zh: 19 überflüssige Abstände nach „章“ entfernt (Rest aus „基础篇~1 中/基础篇~1~中“, nur ml Kap. 2 und 3: „第~1~章中“ statt „第~1~章~中“); fr ml Kap. 2 „du chapitre~1, on a“ → „on obtient“ (sonst Overfull 2,9 pt).
- **Sprachprüfung** (geänderte Zeilen, Grep über alle Sprachen): es/fr Artikel vor „capítulo/chapitre“ stimmen (nur el/del/al/los/El bzw. le/du/Le), keine Pronomen mehr, die sich auf „la Parte“/„er“ (Teil) beziehen; tr-Endungen unverändert (hängen an der Zahl); zh durchgehend „第~N~章“, „第~N~章第~M~节“.
- **Skript-Fix:** `kapitel_umstellung.py` erkannte die neue spanische Kopfzeile der ET-Module als alt (der Modulname „…eléctrica 1: introducción…“ enthält selbst einen Doppelpunkt) und hätte sie bei einem zweiten `--anwenden` verdoppelt; jetzt übersprungen.
- **PDFs:** alle 144 neu gebaut (pdflatex bzw. xelatex, dreimal), `grep -c '^!'` = 0 überall. Neue Overfull > 1 pt: keine (der eine neue, ml Kap. 2 fr, ist behoben). Schon vorher da (Zeile unverändert bzw. Absatz alt/neu einzeln gesetzt): et3 Kap. 2 en 1,5 pt, hm1 Kap. 3 en 2,6 pt (Formel), hm1 Kap. 7 6,6 pt (Beispiel z1z2, alt identisch), gemb1 Kap. 17 19,4 pt (Formel), hm3 Kap. 3 16,3 pt (Überschrift; dazu 5 undefinierte Lösungs-Labels, angehaltene Überarbeitung). `pdf_pruefen`: überall dieselben Stellen wie vorher, außer zh-Satzzeichen am Rand (dieselbe Art wie die vielen alten): et1 Kap. 5 zh +1, et3 Kap. 8 zh +1 (S. 1), ml Kap. 2 zh +1; et1 Kap. 11 zh eine weniger. Titelzeile: 78 Hefte brechen jetzt einmal um (vorher einzeilig), dadurch Seitenzahl anders: et1 Kap. 4 es, gemb1 Kap. 8 und 12, hm1 Kap. 7 je +1; ml Kap. 2 en/tr −1.
- **Konverter-Prüfung** (`--pruefen --katex --aux`, je Heft und Sprache vor dem Löschen der .aux): ohne Warnung, außer den bekannten Ausnahmen et3 Kap. 2 en/es/zh (Absturz, veraltete Übersetzung) und hm3 Kap. 3 (angehaltene Überarbeitung).
- **Neu umgewandelt** (Ausnahmen wie Agent 1; `--md … --anwenden`: 8 de, 1 en, 1 zh): `content/` 1663 Dateien, dieselben Namen (0 neu, 0 weg), `content/gemb1` endet bei 15. Geändert 881 (Text 875; Kopf: summary 49, title 8 — Dateinamen bleiben über `datei_stamm`). Linkziele: keines weg oder geändert; neu verlinkt in 16 Dateien: prog (bisher unverlinktes „Python~1/2“, jetzt „Kapitel~1/2“) und et3 Kap. 4, 5, 8 en/es („Chapters~1 to~3“/„los capítulos~1 a~3“ verlinken jetzt wie im Deutschen die erste Zahl; vorher erkannte der Umwandler „Parts“ nicht).
- **Website** neu gebaut (702 Artikel), HTML-Menge unter `web/wissen/` genau gleich (1677). `tools/themenkarte.py` neu erzeugt (GEMB 19 mit neuem Titel).
- **Übergangsformen** im Umwandler (Abschnitt 4, Schritt 8): **behalten**, weil et3 Kap. 2 en/es/zh und hm1 Kap. 3 es/zh noch offen sind. In keinem Heft steht mehr eine alte Form (zweiter Probelauf).
- **Reste:** Nichts aus Abschnitt 3 offen. Wenn hm3 Kap. 3 fertig überarbeitet ist, normal umwandeln (die .tex ist schon umgestellt). Bei neuen Übersetzungen von et3 Kap. 2 und hm1 Kap. 3 die neue Form verwenden, danach Schritt 8.
