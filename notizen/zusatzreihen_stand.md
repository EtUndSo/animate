# Stand der Zusatzreihen Cybersecurity und Machine Learning (ab 04.11.2026)

Auftrag je Heft: `heft_auftrag_zusatzreihen.md`, Regeln: `UEBERARBEITUNG.md`. Es schreibt immer nur ein Agent (Opus); Recherche-Unteragenten höchstens 3 gleichzeitig auf Sonnet. Zuerst nur Deutsch, Übersetzungen erst nach Freigabe der Reihe durch den User.

Reihenfolge: Pilot cyber 1, ml 1 → Abnahme durch den User → danach abwechselnd ein Cybersecurity-Heft, ein ML-Heft; erst der Stamm (cyber T01–T14, ml T01–T22), dann die Äste (cyber A zuerst, G vorletzt, H zuletzt; ml A → B → F, E parallel, C, D, G).

## Infrastruktur (04.11.2026)
- Heftordner `C:\Bücher\EtUndSo\Cybersecurity\Arbeitshefte`, `C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte`, je mit `praeambel.tex`: Kästen wie ET3 (hintergrund, herleitung, beweis, kernbox, aufgabe …), neu `warnung` (immer offen), Code-Umgebungen `konsole bash python ccode cppcode asm gas ausgabe` (listings, Inconsolata, optionaler Titel), TikZ-Stile `blk geraet zelle fluss kn`; ML zusätzlich Makros `\vx \mX \T \E \Var \argmin …` nach den Notationsentscheidungen.
- `tools/heft_zu_artikel.py`: Module `cyber` und `ml` (Pfad „Informatik / Cybersecurity“ bzw. „Informatik / Machine Learning“ in vier Sprachen, alle Stamm-Hefte eingetragen, Äste später ab Nummer 101). Code-Umgebungen werden zu ```` ```<sprache> <titel> ````-Blöcken (bis zum Schluss als Platzhalter, damit kein Textschritt den Code verändert), `%` in Code, `\verb`, `\lstinline` und `\url` ist kein Kommentar mehr, `\texttt` setzt Sonderzeichen richtig, `warnung` → `:::warnung`, Makros ohne Argument kommen aus der Modul-Präambel, eigener Lesehinweis je Reihe, Teil-Links nur auf vorhandene Hefte, fehlende Hefte werden übersprungen, KaTeX-Prüfung ohne Code-Blöcke. Rückwärtsprüfung an et3/hm3/gemb1/et1/hm1: Ausgabe unverändert.
- `build_wissen.py`: Code-Blöcke mit Kopfzeile (Titel, Sprache) und Farben über Pygments (Tag und Nacht, Prompt nicht markierbar), Kasten `:::warnung` („Achtung“, rot), UI-Wörter warnung/konsole in vier Sprachen.
- Szenen-Gerüste `tools/szenen/cyber_teil1.py`, `tools/szenen/ml_teil1.py`.
- Prüfumgebung (nur für die Agenten, nur auf dem Rechner des Users): Ubuntu 26.04 LTS unter WSL 2 (`student@labor`, sudo ohne Passwort, systemd, Werkzeuge siehe Auftrag; uutils coreutils und sudo-rs!), dazu Git Bash, MinGW gcc/g++/gdb, CMake, Python 3.13 mit NumPy 2.3 und scikit-learn 1.9, kein PyTorch.
- Regel des Users (04.11.2026): Die Leser richten ihre Übungsumgebung selbst nach den Anleitungen der Hefte ein; die Website stellt keine Umgebung bereit (keine Online-Terminals/Sandboxes), wegen der Sicherheitsrisiken.

## Umbau ML: Grundlagen und Pfad (Entscheidung des Users, 05.11.2026)
- T01–T06 werden „Grundlagen 1–6“ in einem eigenen Bereich „Mathematische Grundlagen (zum Nachschlagen)“. Der ML-Pfad beginnt (seit 06.11., siehe unten) mit T08 als „Teil 1“ (ML-Teil N = T(N+7)).
- Jedes Pfad-Heft fasst benötigte Mathematik in „Was du dafür brauchst“ kurz zusammen und verweist mit Link auf „Grundlagen N, Abschnitt M“. Grundlagen-Abschnitte zeigen auf der Website automatisch, welche ML-Artikel sie verwenden.
- Reihenfolge: nach Grundlagen 5 (T05, läuft) direkt Pfad-Teil 1 (T07 Python/NumPy) und Teil 2 (T08 Lernen aus Daten). Grundlagen 6 (T06 Optimierung) erst vor dem Gradientenabstieg.
- **Umgesetzt am 06.11.2026** (Infrastruktur-Agent; Details im Auftrag unter „Nummern“ und „Verweise“, Wendungen in `heft_uebersetzung.md`, Themenkarte `notizen/themenkarte.md` + `tools/themenkarte.py`):
  - Konverter und Website: eigener Bereich und Pfad, Beschriftung „Grundlagen N“ bzw. „Teil N“ in sechs Sprachen, Verweise „Grundlagen N“ und „Teil N“ als Links, automatische Rückverweise „verwendet in“;
  - in den Heften T01–T05 und allen Übersetzungen „Teil N“ durch „Grundlagen N“ ersetzen (Titelzeilen, Rückverweise);
  - Dateinamen und Szenennamen bleiben (Kap1_Vektoren …, ml/k1…); die Pfad-Hefte bekommen die Dateien Kap8_… usw. weiter nach Lernpfad-Nummer, nur die Anzeige zählt ab 1 (Kap7 entfällt).

## Gemeinsame Bereiche, nichts doppelt (Entscheidung des Users, 06.11.2026)
- Der User: „Inhalte nicht mehrfach auf der Webseite vollständig erklären“. Jedes Thema wird genau einmal vollständig erklärt, andere Hefte verweisen mit Link und setzen es voraus. Die Regel steht im Auftrag unter „Nichts doppelt erklären“.
- **Neue Bereiche:**
  - **„Programmieren“:** Python mit Sprache, Datenstrukturen, Funktionen, Module, venv und NumPy-Grundlagen; später C und C++.
  - **„Linux und Kommandozeile“:** Shell, Dateien, Rechte, Prozesse.
  - ML und Cybersecurity setzen beide voraus. Cyber T03–T05 (Linux/Shell), T08 (Python) und T09 (C) werden dadurch zu cyber-spezifischen Heften oder fallen weg; das legt eine Recherche fest.
- **ML-Teil 1 (T07 Python/NumPy) entfällt im ML-Pfad.** Der ML-Pfad beginnt direkt mit „Lernen aus Daten“ (T08) als Teil 1. ML-eigene Werkzeuge wie scikit-learn und das Laden von Datensätzen kommen dort, wo sie zuerst gebraucht werden. Damit gilt: ML-Teil N = T(N+7).
- **ML-Grundlagen gegen HöMa:** prüfen und verlinken. Was ein HöMa-Artikel schon vollständig erklärt, steht in den Grundlagen nur als Kurzfassung mit Link. Das wird bei der nächsten Überarbeitung über die Themenkarte geprüft.
- **`notizen/themenkarte.md`** muss angelegt werden: Thema → Bereich/Heft/Abschnitt, aus den vorhandenen Heften und Lernpfaden.

## Entscheidungen des Users zu Programmieren, Linux und Cybersecurity (06.11.2026)
- **Reihenfolge:** erst die Python-Hefte, die ML-Teil 1 braucht (etwa Python 1–5, 12, 13), dann ML-Teil 1 „Lernen aus Daten“ (T08). Danach die übrigen Python-Hefte und Linux im Wechsel mit ML. Immer nur ein Schreib-Agent.
- **Cybersecurity umbauen** nach dem Vorschlag in `C:\Bücher\EtUndSo\Programmieren\Recherche\ZUSAMMENFASSUNG.md`:
  - T03 und T04 entfallen (Inhalt in Linux 1–6 und 10);
  - T05 → Fachheft „Linux-Sicherheit“ (neues Teil 3);
  - T08 → „Python für die Sicherheitsarbeit“;
  - T09 → „Speicherfehler“ (setzt C 1–9 voraus);
  - T02 → „Schutzgrenzen in Hardware und Betriebssystem“;
  - der Stamm hat dann 12 Hefte. Cyber-LERNPFAD und MODULE["cyber"] anpassen, bevor Cyber Teil 2 geschrieben wird.
- **Zusatzhefte:** git (Programmieren), pandas (Programmieren), SSH und tmux (Linux 11), C 10 Bits/Register/Mikrocontroller (Programmieren). In die Lernpfade aufnehmen.
- **Testumgebung:** Agenten dürfen in WSL eine venv mit NumPy, Matplotlib, pytest und Jupyter im Benutzerordner einrichten, für Linux 1, 9 und 11 eine Test-VM bzw. einen nur lokal erreichbaren SSH-Server. Sonst gilt weiter „nichts installieren“.
- **Selbst entschieden, weil der User nichts anderes sagte:**
  - 13 Python-Hefte, versionsneutral geschrieben, getestet mit 3.13 (Windows) und 3.14 (WSL);
  - Linux 1 zeigt WSL, VM und Live-USB gleichwertig; Live-USB bleibt die erste Cyber-Praxis;
  - C++-Aufgaben in ML werden später geklärt.

## Entscheidung des Users (09.11.2026): Cybersecurity zuerst, über Linux
- Der User: „weiter mit den Themen bei Cybersecurity“. Auf Rückfrage: **erst Linux 1–8**, weil Cyber Teil 2 und 3 sie voraussetzen; danach Cyber Teil 2 („Schutzgrenzen“), Linux 9–10, Cyber Teil 3 („Linux-Sicherheit“), dann Cyber Teil 4–5 (Netzwerke).
- Python 3 läuft zu Ende; Python 4, 5, 12, 13 und ML-Teil 1 folgen später.
- **User, 09.11. abends:** „Fahre danach mit der Erstellung der Artikel zu Cybersecurity fort“ (nach der Kapitel-Umstellung).
  - Umgesetzt als: weiter auf dem Cyber-Weg, also Linux 2 (Phase 1/2), weil Cyber Teil 2 Linux 1–8 voraussetzt. Der User kann direkt Cyber Teil 2 verlangen.
  - Der Editor-Ausbau (L3 …) läuft als Werkzeug-Agent parallel. Er muss rückwärtsverträglich bleiben: Alle vorhandenen Szenen werden als Regressionstest exportiert, damit der Schreib-Agent nicht gestört wird.
- Vorbereitet 09.11.: `MODULE["linux"]["hefte"]` 1–11 (sechs Sprachen), Heftordner `EtUndSo\Linux\Arbeitshefte` mit Präambeln (Kopie Programmieren), `tools/szenen/linux_teil1.py`.
- **Beispiele zugeklappt (Wunsch des Users, 09.11.):** FERTIG 09.11.
  - Umgebung `beispiel` in allen 54 Präambeln; Konverter und build_wissen angepasst (`<details class="beispiel">`, Sprung auf Anker klappt auf).
  - 2297 Kästen in allen Modulen und Sprachen.
  - Prüfung: URL-Menge gleich (nur +17 tr-Seiten G1), Struktur-Checks ohne neue Abweichung, 140 PDFs fehlerfrei.
  - Sicherung und Protokolle im Scratchpad unter `beispiele_sicherung` bzw. `bsp`.
  - **Offen:** 22 Fachbegriffe stehen mit `\fb` nur im Kasten, werden aber später benutzt (Liste in `scratchpad\bsp\umbau_bericht.txt`, Abschnitt „begriff“): et1 7, gemb1 4, hm1 4, hm3 2, cyber 3, ml 2. ml/Knick erledigt der G3-Übersetzer; cyber und ml/Mittelwert der Beispiele bei der ET-Überarbeitung; ET-Module samt Übersetzungen später mit einem kleinen Korrektur-Agenten.
  - **Nicht rückgängig zu machen:** Die PDFs von HöMa3 Teil 3 und GEMB 16/17/19 sind aus dem unfertigen Stand neu gebaut.
- **Übersetzung G3:** FERTIG 09.11. abends, alle fünf Sprachen.
  - Seiten: de 74, en 73, es 74, zh 64, fr 75, tr 72; `pdf_pruefen` meldet überall 0 Stellen.
  - Konverter: 13 Artikel, 20 Abbildungen, 42 Aufgaben, KaTeX ohne Fehler; build_wissen läuft.
  - Sechs Korrekturen am deutschen Original, darunter Checkpointing-Aussage und V-Kurve; Liste im Brief `uebersetzung_brief_zusatzreihen.md`.
  - Zweifelsfälle für Muttersprachler stehen im Brief, z. B. tr „eşlenik (adjoint)“, fr « nœud carré ».
  - Offen: Titelblatt „Stand: 5. November 2026“; `zusammenfassung_kap3.md` nennt Checkpointing nur allgemein.
- **Übersetzung, weiter:** G4, G5, Cyber 1 und Python 1–3 sind EE-frei. Wann sie kommen, wird nach Namensumstellung und Abbildungswellen entschieden.
- **Adressänderung Python 3:** Die Seite „anwendung-der-arbeitspunkt-einer-diode“ heißt jetzt „anwendung-der-zinssatz-eines-ratenkredits“, weil der Inhalt ausgetauscht wurde. Die alte Adresse war veröffentlicht (e3311ac3). Es gibt keine Weiterleitung, weil build_wissen keine kennt.
- **Beispiele für jeden (Wunsch des Users, 09.11.):** außerhalb der ET keine Elektrotechnik, nur Alltagsbeispiele; seltene Wörter ersetzen (UEBERARBEITUNG §2b).
  - **Grep 09.11.:** ET-Bezüge in Python 1 (~80), Python 2 (~190), Python 3 (~320, eigener Abschnitt Diode), ML G4/G5 und Cyber 1 einzelne Stellen.
  - **Präzisiert vom User:** Alle ET-Bezüge werden ersetzt, aber nur in der Informatik (Programmieren, Linux, Cyber, ML). ET1, ET3, GEMB, HöMa1 und HöMa3 bleiben unverändert.
  - **Python 1 überarbeitet 09.11.** (46 S., pdf_pruefen 0, neues `code\kap1\heft_pruefen.py` 48 Blöcke 0 Abweichungen auf Windows/WSL; Tabelle alt→neu in zusammenfassung_kap1.md §7).
  - **Python 2 überarbeitet 09.11.:**
    - 87 S., pdf_pruefen 0; heft_pruefen Windows 113 / Linux 118 Blöcke ohne Abweichung; rechnung 90 Prüfungen.
    - Szene k2rc → k2drehen (Uhrzeiger).
    - Labels umbenannt, siehe zusammenfassung_kap2.md §7.
    - „Zeiger“ nur noch für Uhrzeiger, komplexe Zahl = „Pfeil“.
    - °C als `30\,{}^\circ\mathrm C`, weil KaTeX `30\,^\circ` nicht liest.
  - **Python 3 überarbeitet 09.11.:**
    - 83 S., pdf_pruefen 0; heft_pruefen Windows 191 / Linux 192 ohne Abweichung; rechnung 105 Prüfungen.
    - Abschnitt 9 jetzt Ratenkredit (20 000 € / 60 × 400 € → 0,6183 % im Monat, effektiv 7,68 %).
    - Neue Bezeichnungen: T(t), T_Z, T_0; x̄; K, R, n, S_k, q, f.
    - k_B, U_T, I_S entfallen; `k3diode` → `k3kredit`.
    - Offen: die Fremdsprachen-SVGs von k3if/k3block/k3elif/k3rmittel kommen mit der Übersetzung.
  - **ML G1/G2/G4/G5 + Cyber 1 FERTIG 09.11.:**
    - Tabellen alt→neu in den Zusammenfassungen (G1 §9, G2 §7, G4 §9, G5 §8, Cyber §…).
    - G1/G2 in allen 6 Sprachen nachgezogen. Neue feste Wörter: „Verlauf“ (time series …), „quadratischer Mittelwert“ statt Effektivwert.
    - Python 3: Monatszins heißt r, im Code `zins`; ZINS/RATE-Satz an der Microsoft-Doku belegt.
    - Begriffe aus den Kästen in den Haupttext verschoben.
    - Alle PDFs 0, Struktur-Checks wie vorher.
    - Präambel-Wunsch: zh-Schreibmaschinenschrift (Warnung „TU/zi4/m/n undefined“ bei `\texttt`).
    - Ursprünglicher Auftrag:
    - Python 3: Monatszins i → anderes Symbol (i doppelt belegt), ZINS/RATE-Satz prüfen;
    - Begriffe nur im Kasten verschieben (ML „Mittelwert der Beispiele“, Cyber „Erpressungssoftware“/„Sicherungskopie“/„Phishing“).
- **Shotts (User, 09.11.):** „Ja, Shotts-Kapitel ganz lesen“. Ab Linux 2 liest der Schreib-Agent die Shotts-Kapitel seines Hefts ganz (Auftrag „Zuerst lesen“ 4a). Linux 1 kannte Shotts nur über die Recherche-Auszüge (Kap. 15).
- **Umbenennung (Wunsch des Users, 09.11.):** „Die Bezeichnungen "Python 2" und "Python 3" sind verwirrend, weil es ja wirklich die Versionen von Python gibt … Sie sollten als Kapitel 2 bzw. 3 bezeichnet werden“.
  - **Zielschema:**
    - Anzeige im Python-Bereich „Kapitel N: Titel“; Titelzeile des PDFs „Arbeitsheft Programmieren, Python, Kapitel~N“;
    - innerhalb von Programmieren „Kapitel~N, Abschnitt~M“;
    - Verweise aus anderen Reihen „Python-Kapitel~N, Abschnitt~M“, sinngemäß in allen Sprachen;
    - für C/C++ entsprechend „C-Kapitel“/„C++-Kapitel“ (C11, C++11 wären sonst ebenso missverständlich).
    - Echte Versionsangaben („Python 3.13“) bleiben.
  - **Umsetzung:** nach der Python-3-Überarbeitung durch einen Werkzeug-Agenten:
    - Konverter `MODULE["prog"]` mit Namen und Link-Erkennung in 6 Sprachen;
    - Hefte (prog, Linux 1, Cyber/ML-Verweise) samt Übersetzungen;
    - Lernpfad Programmieren, Auftrag, Themenkarte;
    - Neubau.
  - **Erweitert vom User:** „Führe diese Schreibweise bzw. Unterkategoriesierung bei allen Modulen durch, sodass wir eine einheitliche Sortierung haben“. Das gilt also für alle Module: et1, et3, gemb1, hm1, hm3, cyber, ml (Grundlagen und Pfad), prog (Python, C, C++) und linux.
  - **Einheitliches Schema:**
    - Im Baum jedes Bereichs „Kapitel N: Titel“, nach N sortiert. Ersetzt „Teil N“, „Grundlagen N“, „Python N“, „Linux N“ und Titel ohne Nummer.
    - Titelzeile im PDF: „Arbeitsheft <Bereich>, Kapitel~N“, z. B. „Arbeitsheft Programmieren, Python, Kapitel~3“ oder „Arbeitsheft Linux und Kommandozeile, Kapitel~1“.
    - Verweise im selben Bereich: „Kapitel~N, Abschnitt~M“.
    - Verweise in einen anderen Bereich: „<Kurzname>, Kapitel~N, Abschnitt~M“, Kurznamen Python, C, C++, Linux, Cybersecurity, Machine Learning, Grundlagen (= ML-Mathematik), HöMa 1 usw. Das gilt sinngemäß in allen sechs Sprachen.
    - Überblicksartikel ohne Heftnummer im Titel (Linux 1 hatte „Überblick: Linux 1 – …“).
    - **URLs bleiben unverändert.**
  - **Modulnamen (User, 09.11.):** „erst die Abkürzung …, z.B. Gemb1 oder ET3 und dann den vollständigen Namen, der in den Skripten genannt wird. Bei ET3 steht aktuell nämlich "Signale und System". Das übersieht man vielleicht, wenn man eigentlich ET3 sucht“. Namen laut Titelseiten:
    - ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse
    - ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme
    - GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1
    - HöMa1 – Höhere Mathematik 1
    - HöMa3 – Höhere Mathematik 3 (Skript schreibt „III“; einheitlich arabisch)
    - In allen 6 Sprachen: Abkürzung gleich, Name übersetzt.
    - Die Informatik-Bereiche haben keine Skripte, sie bleiben.
    - **URLs bleiben:** `basis` ist fest. Achtung: Bereichsnamen unter `bereiche` (z. B. „Mathematische Grundlagen“, „Python“, „C und C++“) gehen per slugify in die URL, dort den Slug festhalten.
  - **Umsetzung:** ein Werkzeug-Agent, wenn Python-3-Überarbeitung, G3-Übersetzung und Animations-Agent fertig sind, und vor Linux 2.
    - **Aufgeteilt am 09.11. abends auf zwei Agenten:**
      1. Agent A: FERTIG 09.11.
         - URL-Menge gleich (1677 HTML); content mit neuen Kopffeldern `adresse:`/`knoten:`.
         - Probelauf: 338 Hefte.
         - Vorher bestehende Fehler: et3 Kap 2 en/es/zh passen nicht zur Gliederung, hm1 Kap 3 es/zh unvollständig.
         - Meine Entscheidungen zu seinen Fragen (User darf umwerfen):
           - ET-Titelzeile mit vollem Modulnamen;
           - GEMB-Ergänzungen „Kapitel N: Titel (Ergänzung)“;
           - zh-Kurzname 数学基础.
         - Agent B: FERTIG 10.11.
           - 338 .tex umgestellt, 144 PDFs neu gebaut ohne neue Fehler.
           - content: gleiche Dateinamen, keine Linkziele verloren. URL-Menge gleich (1677).
           - Übergangsformen im Umwandler bleiben, bis et3 Kap 2 und hm1 Kap 3 (Übersetzungen) neu sind.
           - hm3 Kap 3: .tex ist umgestellt, umwandeln erst nach seiner Überarbeitung.
    - **Danach (10.11.):**
      - Linux 2 FERTIG 10.11. (Phase 1, 2a, 2b; siehe Tabelle).
      - Linux 3 **Phase 1 fertig 10.11.**:
        - 10 Abschnitte, 61 Unterabschnitte, 37 Aufgaben (26 am Rechner), 49 `\szenenabb` (davon 4 Rechenbilder), etwa 21 800 Wörter.
        - Lese-Nachweis geprüft: Shotts Kap. 2–4 (Z. 1076–2366) und 17 (Z. 8882–9506) ganz, OSTEP 39 ganz.
        - Neues Prüfwerkzeug `code\kap3\sitzung.py`, weil die Blöcke aufeinander aufbauen.
      - **Phase 2a fertig 10.11.:**
        - 12 fachliche Korrekturen, u. a. Verzeichnisgröße nicht fest 4096, FHS heute bei freedesktop.org, „Dateisystem“ statt „Datenträger“ bei mv/Links, ext4 speichert die Art im Eintrag.
        - uutils-Eigenheiten als „Stand uutils 0.8“ markiert.
        - Doppelungen zu Kapitel 2 durch Verweise ersetzt; 8 Wortersetzungen.
        - 8 Abbildungen gestrichen, 41 bleiben (Abschnitte 1–5: 20, 6–10: 21).
        - Neues `code\kap3\heft_pruefen.py`: 106 von 108 Blöcken in frischer Sitzung, 0 Abweichungen; Rechnung 0 Abweichungen.
        - `zusammenfassung_kap3.md` liegt vor.
      - **Phase 2b-1 fertig 10.11.:**
        - 20 Szenen animiert in 6 Sprachen (4,5–9,6 s, 13–181 KB, ≤ 525 px).
        - Kontaktblatt de von mir angesehen; Zahlen stimmen (hostname-Bytes, Ä = 2 Bytes, ls-Sortierungen).
        - Rich-Text-Fallen in `s.text` (`_ ^ \`) per Maskierung gelöst; Werkzeug-Wunsch: `s.text` „roh“, Pfeilspitzengröße bei `s.weg`.
      - **Phase 2b-2 fertig 10.11., Linux 3 abgenommen:**
        - 21 Szenen (5,5–9,6 s, 24–202 KB); Kontaktblatt de von mir angesehen, Inhalte stimmen (Inode/Links, du-Summe, find -size/-mtime, Muster-Tabelle).
        - `Kap3_Dateien.pdf` 90 S., pdf_pruefen 0; zwei kleine Umstellungen gegen Overfull (10.2, Lösung a:k3wohin).
        - 12 Artikel, 41 Abbildungen, 37 Aufgaben, 76 Beispiele zu, 0 KaTeX-Fehler; HTML 1686 → 1698, genau die 12 neuen Seiten.
        - Alle 12 Seiten im Browser bei 390 px ohne Fehler und ohne waagrechtes Scrollen.
        - Gemeinsames Werkzeug geändert (von mir geprüft, eine Zeile): `tools/pdf_pruefen.py` überspringt unsichtbare Textstücke (`alpha == 0`, ausgeblendete Texte animierter Szenen).
        - `k3einkauf` (Hälfte 1) korrigiert: `\mathtt{einkauf.txt}` setzte einen Abstand nach dem Punkt, jetzt `\texttt`.
        - Werkzeug-Wünsche: `s.text` Inhalt ersetzen ohne unsichtbaren Rest; `s.text` roh und in Schreibmaschinenschrift; Favicon-Link (404 auf `/favicon.ico` auf der ganzen Website).
      - **Linux 4 Phase 1 fertig 10.11.:**
        - 7 Abschnitte, 35 Unterabschnitte, 25 Aufgaben (23 am Rechner), 30 `\szenenabb`, etwa 16 600 + 3 300 Wörter.
        - Lese-Nachweis geprüft: Shotts Kap. 6 (S. 56–70) und 27 ganz, OSTEP 5 ganz.
        - `code\kap4\heft_pruefen.py`: 98 Blöcke, 0 Abweichungen; `sitzung.py` setzt SIGPIPE zurück, damit `yes | head` Status 141 liefert.
      - **Linux 4 Phase 2a läuft.** Entschieden:
        - §7 bleibt bei 4 Abbildungen.
        - Aufgabe `|&` nur mit erklärter Regel.
        - Here-Document ohne `$`.
        - `bash -c 'exit 300'` nur, wenn `bash -c` eingeführt ist.
        - PIPESTATUS als Rezept.
        - 128 + n mit dash testen, ksh93 256 + n belegen.
      - **Linux 4 Phase 2a fertig 10.11.:**
        - Fachlich ergänzt: Regel „Pipe vor Umleitung“ samt genauer Wirkung von `|&`. Korrigiert: Gruppenklammern, Jahreszahlen zur Geschichte; ausdrücklich gesagt, dass dash `&>` nicht kennt.
        - Dateien, die spätere Abschnitte voraussetzen, entstehen jetzt im Haupttext statt im zugeklappten Beispiel.
        - `/dev/null` verweist auf Kapitel 3; Tabelle `tab:k4reihenfolge` gestrichen, die Abbildung ersetzt sie.
        - `k4undsicher` gestrichen, 29 Abbildungen bleiben.
        - 128 + n mit bash/dash getestet, ksh93 256 + n belegt.
        - Code 97 Blöcke, 0 Abweichungen; Rechnung 53/0; `zusammenfassung_kap4.md` liegt vor.
      - **Linux 4 Phase 2b fertig 10.11., abgenommen:**
        - 29 Szenen (4,6–11,3 s, 13–195 KB, ≤ 543 px); Kontaktblatt de von mir angesehen, Inhalte stimmen (Reihenfolge der Umleitungen, PIPESTATUS, 141/130/127/126, Kürzungsfalle, `a && b || c`).
        - `Kap4_Stroeme.pdf` 64 S., pdf_pruefen 0; 9 Artikel, 25 Aufgaben, 47 Beispiele zu, 0 KaTeX-Fehler.
        - Gemeinsame Werkzeuge geändert (von mir geprüft): `|` in Tabellenzellen außerhalb von Formeln wird als `\|` geschrieben (`Heft.cell`), und build_wissen trennt Zellen nur an ungeschütztem `|`. Laut Agent ändert sich nur Linux 4 de.
        - **Von mir nachgezogen:** Der Titel im Baum war „Programme verbinden: Ströme, Umleitung, Pipes, Exit-Status“, das Heft heißt „Ströme, Umleitung, Pipes und Exit-Status“. MODULE-Eintrag in 6 Sprachen auf den Heft-Titel geändert, neue Adresse `…/strome-umleitung-pipes-und-exit-status`; die Seiten waren unveröffentlicht. Konverter, Themenkarte und build_wissen neu.
        - Regel im Auftrag ergänzt: Heft-Titel = MODULE-Titel; Abweichungen nennt Phase 1, Phase 2b passt MODULE an.
        - Werkzeug-Wünsche: Linux-Helfer (`prozess`, `rohr`, `nummer`) in eine gemeinsame Datei; Warnung, wenn ein später erscheinender gefüllter Kasten Text verdeckt.
        - Nach der Umbenennung: HTML weiter 1707, nur die 9 Adressen von Kapitel 4 neu (alte entfernt), alle 9 Seiten im Browser in Ordnung, Tabelle „Das Wichtigste“ mit 16 Zeilen × 2 Spalten.
      - **Linux 5 Phase 1 fertig 10.11.:**
        - 6 Abschnitte, 37 Unterabschnitte, 23 Aufgaben (22 am Rechner), 28 Szenen (1 Rechenbild), etwa 13 100 + 1 950 Wörter; Titel wie MODULE.
        - Lese-Nachweis geprüft: Shotts Kap. 7, 11, 24 ganz.
        - Code 91/92 Blöcke, 0 Abweichungen; Rechnung 60/0.
        - `~/.bashrc` per SHA-256 wiederhergestellt.
        - **Vorfall:** Einmal wurde WSL ohne `--exec` mit einer Pipe gestartet. Das löste Ubuntus einmalige Abfrage „Help improve Ubuntu“ (Berichte an Canonical) aus, und die Testzeile wurde als Antwort gelesen. In WSL ist keine Zustimmung gespeichert (`ubuntu-insights consent`: keine Datei); in Windows (Registry HKCU\Software, AppData) fand ich nichts. Dem User gemeldet. Regel „immer `--exec`“ in den Auftrag (Prüfumgebung) aufgenommen.
      - **Linux 5 Phase 2a fertig 10.11.** (nach Pause fortgesetzt):
        - Code 92/93 Blöcke, Rechnung 60, je 0 Abweichungen; `~/.bashrc` per SHA-256 unverändert; Lese-Nachweis: Heft samt Lösungen ganz.
        - Fachlich korrigiert: „command not found“ kommt von Ubuntus command-not-found, nicht von bash; `hash` nach Verschieben (No such file, 127, bis `hash -r`); führendes Minus deutet das Programm (`--`); zsh NOMATCH; Tilde in Zuweisungen.
        - Aufgaben 6(b), 12, 16(a) entschärft bzw. Regel ergänzt; Sitzungszustand hängt nicht mehr an zugeklappten Kästen; Vorgriff Regex gestrichen.
        - Abbildungen 27 (5/4/5/5/4/4): `k5aliaserbe` gestrichen, `k5vorne` → `k5pathneu`; mehrere auf das Neue gekürzt (Wiederholung von k2suche/k2arten).
        - Für 2b: `\verb` in tabularx und `"` unter babel-ngerman im PDF prüfen; MODULE-Titel unverändert.
      - **Linux 5 Phase 2b fertig 10.11.** (nach Commit de9b4f5d):
        - 27 Szenen animiert, 6 Sprachen, 162 Vektor-PDFs; Durchsicht je Sprache (es/tr je zwei Wörter). Kontaktblatt von mir angesehen: in Ordnung.
        - `Kap5_Expansion.pdf` 62 S., `pdf_pruefen` 0 Stellen (von mir nachgeprüft); `Kap2_Shell.pdf`/`Kap4_Stroeme.pdf` neu gesetzt, je 0 Stellen.
        - Heft-Auszeichnung (Wortlaut gleich): `kap5_stufen.tex` Z. 754 `\textquotedbl{}` (babel), Z. 347 Überschrift mit `\texttt{\$NAME}` (sonst Formel auf der Website).
        - Gemeinsame Werkzeuge: `heft_zu_artikel.code_span` (Code mit Gravis als `` `` a ` b `` ``), `\textasciitilde` im Fließtext → `~`; `build_wissen.inline` liest die Form. Alle 153 Fassungen alt gegen neu: nur Linux 2/5 de anders.
        - Linux 1 und Python 1 (de): 4 Dateien mit neuen Links auf Linux, Kapitel 2. Linux 2 (de) von mir neu umgewandelt: einzige Änderung die Alias-Tabelle in „Arten von Befehlen“ (vorher zerrissen).
        - Build 740 Artikel, 1715 HTML (+8); Browser 390 px: keine Fehler, kein waagrechtes Scrollen, 3 Vorwissen-Kästen.
        - Werkzeug-Wünsche (für E4 oder später): `s.ersetzen` für schon bewegte Texte (springt zurück); wörtliches `$` in Überschriften ohne `\texttt`; einstellbare Eckenrundung bei `s.box(form="round")`.
        - Danach: Linux 6 2b-1, 6 2b-2, 7 2b, 8 2b-1, 8 2b-2. Nach jedem neuen Linux-Kapitel die früheren Linux-Hefte und Python neu umwandeln (Vorwärtsverweise).
      - **Linux 6 Phase 2b-1 fertig 10.11.:** 17 Szenen animiert, 6 Sprachen, 102 Vektor-PDFs, alle `.anim.svg` aktuell, keine Exportwarnung; Breite 317–522 px, 5,2–10,7 s, 14–61 KB; kein MathJax. Kontaktblatt und Zahlen (`k6minuten` 466, `k6haeufigkeit`, `k6schluessel`, `k6seq`) von mir geprüft. Behoben in der Szene: `BETONE` im selben Schritt wie `EIN` ließ ein Objekt unsichtbar (`fill-opacity="0"`), der Export meldet das nicht. Keine Bildunterschrift geändert. Werkzeug-Wünsche: Export soll unsichtbare, nie ausgeblendete Objekte melden; `s.summe(werte=[…])` mit laufender Zwischensumme. `SZENEN_2` für 2b-2 vorbereitet.
      - **Linux 6 Phase 2b-2 fertig 11.11.:** 17 Szenen (204/204 `.anim.svg` aktuell), `Kap6_Textwerkzeuge.pdf` 78 S., pdf_pruefen 0 (von mir nachgeprüft), 12 Artikel, Build 1727 HTML (+12), Browser ok; Kontaktblatt und Zahlen (`k6mittel` 7,1, `k6array`, `k6klassen` 12/5/6) von mir geprüft. Heft: `\titleformat{\section}…\raggedright` nur in `Kap6_Textwerkzeuge.tex`, zwei `\textquotedbl{}`, `\texttt{\$1}` in Überschrift 9.2. Werkzeug-Wunsch: aria-label der Abbildungen mit Leerzeichen vor Satzzeichen nach Code. Danach `svg_painter._d` mit Schutz für leere Kontur, Tests FAIL=0.
      - **Website-Ideen-Agent fertig 11.11.** (Befunde von mir stichprobenartig bestätigt: 77 von 767 deutschen Seiten mit Inhaltsverzeichnis, 16 Titel mit rohem TeX, `web/` 14 843 Dateien gegen 20 000 im Gratis-Tarif von Cloudflare Pages); offene Fragen an den User in `notizen/website_ideen.md` §7. Früher: (Wunsch des Users: Features für die ganze Website, Schnell-Info-Box oben im Artikel, Verständnis-Werkzeuge, Optik). Nur Konzept, Ergebnis `notizen/website_ideen.md`; nichts beschlossen.
      - **Ab 11.11.: Englisch-Schleife** (User: erst übersetzen, Linux 7/8 2b warten; HöMa3 Kap. 3 auslassen). Warteschlange und Ablauf: `notizen/uebersetzung_en_schleife.md`, Brief `notizen/uebersetzung_en_brief.md`. Danach (User 11.11.) die Editor-Änderungen „Bildschirme und Fenster“ (`notizen/editor_bildschirme_plan.md`, F1 zuerst, Umsetzung vorher mit dem User abstimmen), dann Linux 7 2b, 8 2b-1, 8 2b-2.
      - (alt) Linux 6 Phase 2b-2 lief seit 11.11. (nach Commit 1d2a4024; Scratchpad `linuxk6b2`). 2b-2 (17 Szenen der Abschnitte 6–10 + PDF, Artikel, Build, frühere Hefte neu umwandeln; Hinweise für 2b in `uebergabe_kap6.md` beachten).
      - **Linux 6 Phase 1 fertig 10.11.** (parallel zu E1): 10 Abschnitte, 50 Unterabschnitte, 29 Aufgaben, 34 Szenen (2 Rechenbilder `k6minuten`, `k6mittel`), etwa 20 800 Wörter. Daten: Lauftagebuch `laeufe.csv` statt Messdaten. Code 132 Blöcke, Rechnung 88, je 0 Abweichungen; `~/.bashrc` unverändert. Lese-Nachweis geprüft: Recherche-Dateien und Shotts Kap. 19/20 ganz. Neue Bezeichnungen: „Suchtext“, „Grundform“/„erweiterte Form“ (BRE/ERE), „Zeilenadresse“ (sed), „Bedingung“ (awk), „assoziatives Array“.
      - **Linux 6 Phase 2a fertig 10.11.** (offene Fragen entschieden: de_DE-Sortierung knapp und als ungeprüft gekennzeichnet; kein `k6locale`; `k6automat` im Haupttext ok; Abschnitt 4 bleibt; Bentley/Knuth/McIlroy mit Namen und CACM, belegt):
        - Fachlich: `sort -n` unter de_DE liest `10.5` als 105 (Tausenderpunkt); GNU `cut -c` zählt erst ab coreutils 9.11 (April 2026) Zeichen; `\+ \? \|` in der Grundform = GNU-Zugabe; „gierig“ von POSIX-längstem Treffer getrennt (Python `a|ab` → `a`, grep → `ab`); awk auch mit mawk geprüft.
        - Sitzung hing an Beispielkästen (`kurz.csv`, `klein.csv`, `kopie.csv`) → jetzt Haupttext.
        - 34 Abbildungen (4/4/4/2/3/4/4/4/4/1), Hälften: 2b-1 Abschnitte 1–5 (17), 2b-2 Abschnitte 6–10 (17). Geändert: `k6ausschnitt`, `k6haeufigkeit`, `k6sedi`, `k6automat`.
        - Code 133 Blöcke, Rechnung 95, je 0 Abweichungen; `~/.bashrc` unverändert; Lese-Nachweis: Heft ganz; `zusammenfassung_kap6.md` liegt vor. Wortzahl ~24 500 (nach wc -w, Korrekturen glichen Kürzungen aus).
        - Für 2b: KaTeX/Konverter bei `\texttt{[]-]}` (6.4), maskierten `\+ \? \|` (7.5) und `\verb` in Warnung 8.6 prüfen. Kapitel 10 verweist für Windows-Zeilenenden in Skripten auf Linux, Kapitel 6, Abschnitt 1.4.
      - **Linux 7 Phase 1 fertig 10.11.** (nach Netzabbruch fortgesetzt): 9 Abschnitte, 50 Unterabschnitte, 25 Aufgaben, 28 Szenen (4 Rechenbilder `k7oktal`, `k7umask`, `k7undnicht`, `k7vierziffern`), etwa 22 900 Wörter. Code 91 Blöcke, Rechnung, je 0 Abweichungen. SHA-256 von 10 Dateien (`/etc/passwd`, `group`, `shadow`, `gshadow`, `subuid`, `subgid`, `sudoers`, 2× `sudoers.d`, `~/.bashrc`) vorher = nachher; `anna`, `ben`, `kochclub` entfernt (von mir in WSL nachgeprüft, Gruppe `sudo` nur `student`).
        - Zwischenfall: Nach einer Probe mit `su - anna` war `anna` kurz mit Wegwerfpasswort in `sudo`, weil `deluser` an laufenden Prozessen scheiterte. Sofort entfernt; `sitzung.py` beendet seitdem die Prozesse des Testbenutzers. Für 2a: Testkonten nie in `sudo`.
        - Lese-Nachweis geprüft: Recherche-Dateien, WISSEN_07, Shotts Kap. 9 (754 Z.) ganz; OSTEP 39.16 und 55.3/55.6 gelesen.
        - Reihenfolge gegenüber Lernpfad begründet umgestellt (sudo vor chown/SUID, Benutzer anlegen vor chgrp/SGID/Sticky). `--` in `\texttt` als `-{}-` (zi4-Ligaturen; wie Kap. 2/3).
      - **Linux 7 Phase 2a fertig 10.11.**:
        - Fachlich: „neues Terminal = neue Anmeldung“ nur unter WSL richtig (am Desktop ab-/anmelden; überall `sudo -iu "$USER"`); `chmod +x` ohne „wer“ beachtet die umask (Definition jetzt `a+x`); `stat`-Vorlage in `'…'` wegen Leerzeichen; `auth.log` gehört `syslog:adm`; yescrypt `$y$` ergänzt; Hinweise für VM/Live-Leser (Benutzer `ubuntu`, umask 0002). „superuser do“ vorsichtig, sudo.ws schreibt „su do“.
        - Leser-Sicherheit: `adduser --disabled-password --comment "Anna Berg" anna` (kein Schritt brauchte ihr Passwort); Warnung „Testkonten nie in sudo“; 9.9 räumt `anna`, `ben`, `kochclub` auf.
        - 28 Abbildungen (4/4/2/2/3/4/3/2/4), keine gestrichen, 5 Beschreibungen geändert → **2b mit einem Agenten**. Für 2b: neue `\verb` in „Kurz gesagt“ 7.4, Lösung 17, 9.9; `\texttt{\$y\$}` in 1.8; Ligaturen in `\texttt` im PDF; Verweise „Kapitel~2, Abschnitt~7.2“, „Kapitel~3, Abschnitt~10“, „Kapitel~4, Abschnitt~4.4“, „Kapitel~5, Abschnitt~5.4/6.3“ im Konverter. Titel passt.
        - Code 92 Blöcke (91 geprüft), Rechnung 1145/1146, je 0 Abweichungen; 10 SHA-256 gleich; Testkonten entfernt (von mir in WSL nachgeprüft). Wortzahl 23 630. Lese-Nachweis: Heft ganz. `zusammenfassung_kap7.md` aktuell.
      - **Linux 8 Phase 1 fertig 10.11.** (Prozesse, Signale, Dienste; Gerüst `tools/szenen/linux_teil8.py`):
        - Umfang: 8 Abschnitte, 54 Unterabschnitte, 26 Aufgaben (18 am Rechner), 30 Szenen, darunter die Rechenbilder `k8exitrechnung`, `k8lastrechnung` und `k8niceanteil`; etwa 25 100 Wörter.
        - Prüfung: Code-Abgleich 105 Blöcke, Rechnung 59 Prüfungen, je 0 Abweichungen. Prüfwerkzeug mit zwei echten Terminals (Strg+Z, SIGHUP).
        - Lese-Nachweis: Shotts Kap. 10, OSTEP 4/5 und die Recherche ganz.
        - Testumgebung: von mir in WSL nachgeprüft. Prüfsummen gleich `linuxk7/sha_final.txt`, keine Versuchsprozesse, keine `k8*`-Einheit, `~/linuxk8` entfernt.
        - Präambel: ● und ○ ins `literate` aller sechs Präambeln, für die echte erste Zeile von `systemctl status`.
      - **Linux 8 Phase 2a fertig 10.11.** (von mir geprüft: Heft ganz gelesen, WSL sauber, Prüfsummen gleich):
        - Fachliche Korrekturen: `pid_max`, Namenskürzung auf 15 Zeichen durch den Kernel, `Relay(570)(569)`, pgrep-Muster als ERE, Lösung 19(c) 14 %, Aufgabe 13(b) Eltern/Kind.
        - Ergänzt: Zustand `t`, SIGKILL bei D, Signalnummern 1–15 überall gleich, CAP_KILL/SIGCONT, `huponexit`, EEVDF seit 6.6, linger, WSL ohne systemd, `RestartSec=`, Journal dauerhaft vs. `/run`.
        - `heft_pruefen.py` verschärft (feste Zahlen wörtlich, Zuordnung beidseitig eindeutig, Selbsttest `linuxk8p/selbsttest.py`).
        - Ergebnisse: 105 Blöcke/826 Zeilen, Rechnung 68 Prüfungen, je 0 Abweichungen.
        - 30 Szenen (4/4/4/4/4/3/4/3) → **2b-1 Abschnitte 1–4 (16), 2b-2 Abschnitte 5–8 (14)**. Für 2b: lange Code-Zeilen, `\verb` in 7.2, ●/○/× in 7.4.
        - Wortzahl 26 054 (+980 durch verlangte Ergänzungen). Titel passt.
      - **Vorwissen-Kästen (User 10.11.):** „Was du dafür brauchst: …“ wird auf der Website ein zugeklappter Kasten.
        - Konverter fertig (`VORWISSEN_RE`, `vorwissen_kasten`, kein eigener Artikel beim Teilen). Trockenlauf: 79 Kästen, Unterschiede nur durch die Kästen. Schon vorher abweichend und nicht angefasst: HöMa3 Kap. 3 (Inhalt älter als das Heft), Linux 1 und Python 1 je 2 Artikel, ET3 Kap. 2 en/es/zh.
        - **Nach E3, vor Linux 5 2b:**
          1. `build_wissen.py`: `:::::vorwissen` in `md_to_html` (Kopf am ersten Doppelpunkt geteilt; CSS weiß mit grüner Kopfleiste, Klasse `vo-k`/`vo-body`), `lesezeit` ohne Vorwissen, `verwendet_html` erkennt die Titel auch im Kasten.
          2. `python …\scratchpad\vorwissen_inhalt.py --schreiben` (48 Dateien, 75 Kästen, nur die Kästen; Textweg = Konverter geprüft).
          3. build_wissen, 1707 Seiten, Browser-Prüfung: Link auf einen Anker im Kasten klappt ihn auf.
      - **Linux 8 Phase 2a (Entscheidungen vom Start):**
        - `&` im Zombie-Versuch ok;
        - konstruierte `ps aux`-Zeile ok;
        - `PPid` nachvollziehbar machen;
        - 30 Szenen ok → 2b in zwei Hälften;
        - lange Zeilen prüft 2b.
      - **User 10.11.:** weiterhin nur ein Schreib-Agent gleichzeitig, auch über Bereichsgrenzen.
      - **Reihenfolge danach (Stand 10.11. spätabends):** E2 fertig, User hat committet (5643a95f). **E3 fertig 10.11., von mir geprüft:**
        - L5: `s.gitter`, `s.vektor`, `s.abbilden(matrix, objekte, weg="drehung", parameter="s")`, `s.abbilden_funktion` (nichtlinear), `s.vieleck`.
        - L4: `s.kamera_start`, `s.kamera(theta, phi, zoom, blickpunkt, drehen)`, `s.kamera_kreisen`, `s.kugel`, `s.zuoberst`, `s.achsen3d`, `s.flaeche3d`; 3D-Koordinaten mit Parametern.
        - Export Weg (b): Der Spieler (`wissen.js`) projiziert selbst. Beispiel `k6kubisch` 150 KB statt 473 KB.
        - 9 Vorführszenen `beispiel/anim_l5_*`/`anim_l4_*`; Kontaktblatt von mir angesehen.
        - Fehlerbehebung: verschachteltes `gleichzeitig()`; 3 Beispielszenen laufen dadurch kürzer.
        - Prüfung: Tests `FAIL=0` (von mir). Spieler mit alten und neuen Animationen ohne Konsolenfehler (von mir). Regression 812 JSON gleich, 1892 Exportdateien gleich.
        - Grenze: Vorhandene 3D-Szenen (gemb1/hm1) sind für eine feste Kamera gebaut; für Fahrten mit `kugel` und 3D-Strecken neu aufbauen (Nachrüsten). Doku `animationen.md` §9/§10.
      - **Vorwissen-Kästen fertig 10.11.** (nach E3):
        - build_wissen: `:::::vorwissen`, CSS mit Nachtmodus, Lesezeit, „Verwendet in“, Suchindex unverändert.
        - 48 Artikeldateien mit 75 Kästen.
        - Build 732 Artikel / 1707 Seiten, geändert nur 48 Seiten plus `wissen.css`/`wissen.js`.
        - Browser (de/fr/zh, HöMa3 mit 9 Kästen): zu beim Laden, Klick öffnet, Sprung auf den Anker öffnet, Nachtmodus ok, keine Konsolenfehler. Wenn Linux 8 2a und E3 fertig sind: die 2b-Agenten nacheinander (Linux 5 2b, 6 2b-1, 6 2b-2, 7 2b, 8 2b-1, 8 2b-2), dazwischen kein Werkzeug-Agent. E4 nur parallel zu Phase 1/2a. Linux 5 2b (27 Szenen, dazu `Kap2_Shell.pdf`/`Kap4_Stroeme.pdf` neu setzen) erst, wenn kein Werkzeug-Agent und kein anderer Schreib-Agent läuft; dann Linux 6 2b-1/2b-2.
      - **Editor-Ausbau gestartet 10.11.** (User: „Weiter“, ohne Commit; letzter Commit weiter fca61c05). Plan, Werkzeug-Agenten nacheinander, jeder mit Regressionstest aller 809 Szenen:
        - E1 Text und Werkzeugpflege, **fertig 10.11., von mir geprüft:** `s.text(schrift="tt")`/`roh=True`, `s.ersetzen`/`s.umformen` Text → Text, `\mathtt`-Punkt und gerade `'` in `\texttt`, `Szene(reihenfolge="anlegen")` + Warnung „Text unter deckender Fläche“, `szenen_ansehen.py --animiert`/`--ohne-export`, `s.weg(spitze=…)`, `s.summe(..., exakt=True)`, Favicon, `tools/szenen/linux_hilfen.py` (neu: `schreibmaschine("text")` am Dateianfang für Kapitel 5+), build_wissen 27 → 20 s (byte-gleich).
          - Regression: 809 Szenen de/zh, nur `k2alias`, `k2fehlermeldung`, `k2rsuche`, `k4rohre` geändert (gerade Anführungszeichen, Kontaktblatt von mir angesehen); alle Szenen-Skripte bauen byte-gleiche JSON.
          - Von mir nachgeprüft: 25 Testdateien (aus `web/` als Skript starten; zwei brauchen `PYTHONIOENCODING=utf-8`) und 2 Node-Tests grün; 1707 Seiten; Linux 2/4 bei 390 px ohne Fehler; Favicon 200.
          - **Offen:** `Kap2_Shell.pdf` und `Kap4_Stroeme.pdf` (de) zeigen die vier geänderten Bilder erst nach neuem LaTeX-Lauf → Auftrag an Linux 5 2b.
          - Hinweise für E2 im Bericht: `draw_text` nimmt `font="mono"`/`raw=True`; neue Szenen-Einstellungen an drei Stellen (`editor.js toPythonModel`, `export_szenen.python_model`, `sceneData`/`applyScene`); neue Schlüssel nur schreiben, wenn sie vom Standard abweichen; Regressionswerkzeuge im Scratchpad `editor_e1/` (`szenen_bauen.py`, `vergleich.py`, `wissen_vergleich.py`).
        - E2 L3 Parameter über die Zeit, **fertig 10.11., von mir geprüft** (Scratchpad `editor_e2/stand.md`; Doku `notizen/animationen.md` §8, `EDITOR_WERKZEUGE.md` G1–G7, ENGINE_CONTRACT „Parameters over time“):
          - API: `s.parameter(name, wert, von, bis, schritt, ganzzahlig)`, `s.verstellen(name, ziel, dauer, rate="glatt"|"linear")`, `s.zahl(...)` (Zahlenanzeige, Dezimalzeichen je Sprache), `s.marke(...)` (Marker mit Projektionen), `s.tangente(...)`, `kurve/flaeche(punkte=)`. Ausdrücke in Koordinaten (`"r*cos(phi)"`), Parameter darf `t` heißen. Modell: Animation `ChangeValue`.
          - Grenzen (§8.5): Verschieben/Drehen/Umformen eines Parameter-Objekts nur am Startwert; Achsen, MathTex, Σ/Faltung werden nicht neu gebaut; Text ohne Parameter (dafür `s.zahl`).
          - Vorführszenen `beispiel/anim_l3_{welle,tangente,zeitmarker,zeiger,grenzwert,flaeche}` in 6 Sprachen, 44–124 KB; Kontaktblatt von mir angesehen.
          - Regression: 809 Szenen byte-gleich, Export de/zh 1868 gleich, 0 anders; von mir nachgeprüft: alle 25 Testdateien + pytest + 2 Node-Tests grün, build_wissen 1707 Seiten, `web/wissen` unverändert.
          - Für E3: L5 kann auf L3 aufsetzen (Builder in `_build_object`, konstante Punktzahl); L4-Kamera wäre ein Tracker in `ModelScene.seek`, Dateigröße bleibt das Problem.
        - E3 L5 Gitter-Morph und L4 Kamera.
        - E4 L6 Teilchen, L7 Operationen, L8 Code-Objekt, diskrete Faltung, komplexe Rechenbilder, Pfeil umhängen.
        - Danach die Ansicht Szene ↔ Code, dann die Nachrüstwellen. **User 10.11.:** Plan bleibt, also kein vorgezogenes Nachrüsten mit dem heutigen Editor. Nicht wieder vorschlagen.
        - **Verzahnung:** Phase 1 und 2a der Linux-Hefte laufen parallel zu den Werkzeug-Agenten, weil sie keine Repo-Werkzeuge benutzen. Phase 2b eines Hefts startet nie, während ein Werkzeug-Agent läuft, und umgekehrt.
        - Ein Commit ist unsicher, solange ein Werkzeug-Agent läuft.
      - (Linux 3, erledigt:) Phase 2b geteilt: 2b-1 baute die Szenen der Abschnitte 1–5, 2b-2 die Szenen der Abschnitte 6–10 sowie PDF, Artikel und Build.
      - Den Editor-Ausbau starte ich erst, wenn der User committet hat. Er ändert gemeinsam benutzte Werkzeuge, und ein Commit mitten in seiner Arbeit wäre unsicher.
      2. Agent B: Skript auf die Hefte anwenden, alle PDFs neu bauen, `pdf_pruefen`, neu umwandeln, build_wissen, URL-Vergleich.
    - **Ausnahmen:** hm3 Kap 3 nicht aus dem .tex umwandeln, weil die Überarbeitung angehalten ist; dort nur die Markdown-Dateien umbenennen. GEMB 16+ nie umwandeln.
    - Der User hatte vor dem Start nicht committet; letzter Commit fca61c05.
    - Konverter-Namen und Link-Erkennung aller Module in 6 Sprachen;
    - alle Hefte samt Übersetzungen (Verweise, Titelzeilen), dann PDFs neu und pdf_pruefen;
    - Artikel neu, build_wissen, URL-Vergleich;
    - Doku: Auftrag (Verweise), heft_uebersetzung, Lernpfade, Themenkarte.
  - **Reihenfolge, je ein Schreib-Agent:**
    1. nach Linux 1 Phase 2 die Überarbeitung von Python 1–3 (Heft für Heft, vor der Übersetzung);
    2. die Einzelstellen in ML G1–G5 (G1/G2 samt Übersetzungen) und Cyber 1;
    3. dann weiter mit Linux 2.
  - **Spätere Python-Hefte:** Lernpfad- und WISSEN-Anwendungen ersetzen.
- **Mehr Abbildungen, Animationen mit Start/Stopp (Wunsch des Users, 09.11.):**
  - **Durchsicht fertig 09.11.** (`notizen/abbildungen_audit/UEBERSICHT.md`, 21 Paketdateien):
    - 670 → 1237 Abbildungen; neue Vorschläge A 455 / B 123 / C 19; 651 vorhandene eignen sich zum Abspielen.
    - 214 von 721 Artikeln hatten kein Bild; 85 von 95 Rechenbildern sind statisch.
    - Editor-Lücken L1–L9, größter Hebel L3 (Parameter über die Zeit).
    - Die Vorschläge zu GEMB 16/17/19 gelten erst, wenn diese Hefte erscheinen.
  - **Entscheidungen des Users 09.11.:** animierte SVG (keine Videos) mit Start/Stopp, Neustart und Zeitleiste; neue Abbildungen nur als Editor-Szene, das PDF zeigt ihr Endbild (Makro), vorhandene TikZ bleiben.
  - **Werkzeug-Agent FERTIG 09.11.** (Anleitung `notizen/animationen.md`; Regeln stehen jetzt im Auftrag, Abschnitt „Abbildungen“):
    - `<szene>.anim.svg` = Endbild plus Datenblock, JS-Spieler mit Start/Stopp, Neustart, Schritt vor/zurück, Zeitleiste mit Sprungmarken.
    - Größe 23–120 KB.
    - L1/L2/L9 gebaut, Rechenbilder laufen Zeile für Zeile; `\szenenabb` in allen 54 Präambeln (Vektor-PDF über `szenen_pdf.py`).
    - Fehlerbehebungen: clip_run, Ausdünnen der Kurven, Punktfolgen, `\textcolor`.
    - Offen: L3 (geschätzt 2–3 Agenten-Tage), L4 Kamerafahrt (braucht einen projizierenden Spieler), build_wissen dauert jetzt etwa 7 min.
    - Ursprünglicher Auftrag des Agenten:
    - animierter SVG-Export, Spieler in build_wissen;
    - L1/L2/L9 freischalten, Rechenbilder als Ablauf;
    - PDF-Makro für Szenen;
    - Engine-Fehler beheben;
    - Doku `notizen/animationen.md`.
  - **Danach:** die Regel in den Auftrag, dann das Nachrüsten in der Reihenfolge der Übersicht:
    1. Rechenbilder und Artikel ohne Bild;
    2. die Top 30;
    3. vorhandene Bilder animieren, Heft für Heft;
    4. L3;
    5. die Reste.
  - **Vorschlag der Durchsicht zur Zählregel:** Soll = das Größere aus Längen-Soll und Zahl der neuen Begriffe, 1–5; Rechenbilder in zugeklappten Kästen halb zählen. Der User antwortete „Ok“; ich nehme den Vorschlag als angenommen, Widerspruch steht ihm frei.
  - **Auftrag des Users 09.11.:** „baue dem Editor alles ein, was er noch braucht um alle Szenen abbilden zu können, die wir haben wollen. Dann die passenden Grafiken/Animationen. Beides erst nachdem die aktuellen Agenten fertig sind“.
    - Laufen gerade: Python-2-Überarbeitung, G3-Übersetzung, Animations-Werkzeug-Agent.
    - **Danach Editor vervollständigen:** alle Lücken aus UEBERSICHT.md:
      - L3 Parameter über die Zeit, L4 Kamera, L5 Gitter-Morph, L6 viele Teilchen, L7 weitere Operationen, L8 Code-Objekt;
      - diskrete Faltung, komplexe Zahlen im Rechenbild, Namenspfeil umhängen;
      - was der Animations-Agent offen lässt.
      - Werkzeug-Agenten nacheinander, jeder mit Tests.
    - **Vorgemerkt vom User (09.11.):** „die Funktion einzubauen, dass das im Editor gezeigte Foto als Code angezeigt wird bzw. andersherum“.
      - Die Reiter „Code“ und „Both“ in `web/editor.html` sind bisher abgeschaltet („coming in Batch 5“).
      - Ziel: Szene ↔ Python-Code (szenen_lib-Stil) in beide Richtungen, „Both“ zeigt beides nebeneinander und synchron.
      - Termin: nach der Vervollständigung des Editors, sofern der User nichts anderes sagt.
    - **Dann Grafiken/Animationen in Wellen:** je Heft ein Agent, der Szenen baut und `\szenenabb` ins Heft setzt, samt Bildunterschriften in allen vorhandenen Sprachen. Erst wenn die ET-Überarbeitung von Python/ML/Cyber durch ist, damit sich nichts überschneidet.
- Vor Cyber Teil 2 noch offen: Cyber-LERNPFAD auf 12 Hefte und `MODULE["cyber"]` umstellen (nur Kap1 existiert, deshalb Dateinummer = Anzeige-Teil 1–12).

## Koordination
Wie der Haupt-Agent Agenten beauftragt, prüft und berichtet, steht in `notizen/koordination.md`. Diese Datei vor jedem Arbeitsschritt lesen.

## Nächste Schritte (Stand 06.11.2026, früh)
1. ~~Grundlagen 5 fertigschreiben~~ (erledigt 06.11.)
2. ~~Übersetzung von Grundlagen 2~~ (erledigt 06.11.)
3. ~~Infrastruktur-Agent für den Umbau~~ (erledigt 06.11.: Grundlagen-Bereich in sechs Sprachen, 799 Verweise umgestellt, „Verwendet in“, Themenkarte notizen/themenkarte.md + tools/themenkarte.py, Gerüste MODULE["prog"]/["linux"]; 0 Unterschiede bei 1319 Artikeln anderer Module, 0 tote Links). Bekannt und älter: et3 Kap 2 en/es/zh und hm1 Kap 3 es/zh passen nicht zum überarbeiteten deutschen Heft, der Konverter bricht dort ab. Neu übersetzen, wenn die Module wieder dran sind.
   - ML-Grundlagen als eigener Bereich, Beschriftung „Grundlagen N“, „Teil N“ → „Grundlagen N“ in T01–T05 und allen Übersetzungen, automatische Rückverweise „verwendet in“;
   - ML-Pfad-Nummerierung mit Teil N = T(N+7);
   - Website-Bereiche „Programmieren“ und „Linux und Kommandozeile“ vorbereiten;
   - Link-Erkennung für „Programmieren, Python N“ usw.;
   - `notizen/themenkarte.md` anlegen.
4. **Recherche und Lernpfad** (gestartet 06.11. nachmittags, Ablage EtUndSo\Programmieren\Recherche und EtUndSo\Linux\Recherche) für „Programmieren“ (Python, später C/C++) und „Linux und Kommandozeile“, aus den vorhandenen WISSEN-Dateien (ML T07, Cyber T03–T05, T08, T09) und neuen Hauptquellen. Danach den Cyber-Lernpfad anpassen.
5. **Schreiben:**
   - Python-Hefte (Bereich Programmieren) zuerst;
   - dann ML-Pfad Teil 1 „Lernen aus Daten“ (T08), mit „erst selbst bauen, dann Bibliothek“ und Verweisen statt Wiederholung.
6. **Übersetzungen** (Grundlagen 1 läuft seit 06.11. abends): Grundlagen 1, 3, 4, 5, Cybersecurity Teil 1, Python 1, Python 2, Python 3, je ein Übersetzungs-Agent parallel zum Schreib-Agenten.
7. **Werkzeug-Wünsche (offen):**
   - aus dem Editor-Umbau (09.11.):
     - Lade-Animation beim Öffnen und paralleles Laden sind fertig: bereit kalt 2,6 → 2,4 s, gedrosselt kalt 7,1 → 5,6 s, gedrosselt warm 3,5 → 1,9 s.
     - Der User: „der große Umbau lohnt sich nicht, die Wartezeit ist ca. 5 Sekunden und die Lade-Animation reicht aus“. Also kein Web Worker, kein Snapshot.
     - Offen: Das Render-Overlay benutzt `backdrop-filter: blur` und bremst vermutlich das Vorberechnen der Frames, nicht gemessen.
   - aus der Startseite (09.11., Fourier-Video über `tools/startseite_video.py`):
     - `exportVideo` liefert auf langsamen Geräten Zeitlupe, weil MediaRecorder mit der echten Uhr stempelt; wichtig für Animationen in Artikeln.
   - **Erledigt 11.11. (vom User gemeldet), von mir direkt:**
     - Operationen Skalarprodukt/Summe/Produkt: die lange Parameterbeschreibung steht nicht mehr im Feld, nur noch als Tooltip am Namen (`editor.js` `renderCompProps`).
     - Video-Export war am Anfang und Ende abgeschnitten: jetzt Aufnahme erst nach dem `start`-Ereignis, Startbild 0,5 s und Endbild 1 s gehalten (`exportVideo`); geprüft mit ffmpeg (17 gleiche Bilder vorn, 31 hinten).
     - `web/py/canvas_painter._trace`: leere Teilkontur übersprungen. Vorher brach z. B. `beispiel/anim_umformen` beim Umformen mit IndexError ab, die Aufnahme lief endlos weiter; ein fehlerhaftes Bild hält die Aufnahme jetzt nicht mehr an.
     - Halten abschaltbar über `window.EXPORT_HALTEN = {vor:0, nach:0}`; `tools/startseite_video.py` setzt das (nahtlose Schleife), geprüft: 239 von 241 Bildern ohne Halten.
     - Startseite (`web/index.html`): Abschnitt „Der Editor“ steht jetzt vor „Fächer & Themen“, Überzeile „Das Herzstück“ entfernt (Wunsch des Users).
     - **Offen (nach Linux 6 2b-2, nicht während eines 2b-Agenten):** derselbe Schutz in `web/engine/svg_painter._d` (leere `pts` → `""`).
     - `engine/figures.py` `clip_run` vergleicht Gleitkomma-Endpunkte auf Gleichheit, dadurch entstehen abgeschnittene Kurven gestrichelt.
     - Der adaptive Plotter setzt über 8000 Punkte je Kurve.
     - Größe: Ein 12,5-s-Video in 1080p hat 0,8 MB (MP4) bzw. 1,4 MB (WebM).
   - aus Linux 1:
   - localizeTex macht aus „10.0.2.15“ „10,0,2,15“; Punktfolgen mit mehreren Punkten (IP, Version) sollten unverändert bleiben;
   - `\textcolor` in `s.formel` erzeugt einen schwarzen Balken;
   - Szenen sind zu breit gezeichnet, Linux 1 staucht sie per FAKTOR.
   - aus Linux 2 (10.11.): Schreibmaschinenschrift für `s.text` statt MathJax-`\texttt`; gerade `'`/`` ` `` in `\texttt`; Zeichenreihenfolge bei Erscheinen-Animationen dokumentieren; `szenen_ansehen.py` soll `.anim.svg` nicht veralten lassen.

   Älter: `s.summe`/`s.produkt` mit anderem Laufindex als i und exakten großen Brüchen (3/131072); `code\kap2\heft_pruefen.py` als allgemeines Werkzeug nach `tools/`. Erledigt 06.11.: `\jj` in der Programmieren-Präambel, Code in `\texttt`/`\mathtt` behält in Szenen den Dezimalpunkt (editor.js localizeTex), Backticks in Artikeltiteln (build_wissen).

## Hefte

| Reihe | Teil | Thema | Stand |
|---|---|---|---|
| cyber | 1 | Sicherheit, Schutzziele und Spielregeln | fertig 04.11. (68 S., 10 Abschnitte, 20 Aufgaben, 8 Abb.; Website de gebaut), wartet auf Abnahme |
| ml | 1 | Vektoren und Matrizen | fertig 04.11. (82 S., 15 Abschnitte, 37 Aufgaben, 15 Abb.; Website de gebaut), wartet auf Abnahme |

| ml | 2 | Projektion, Eigenwerte und Zerlegungen | fertig 04.11. (85 S., 12 Abschnitte, 38 Aufgaben, 11 Abb. + 18 Rechenbilder; Website de gebaut). Laut Protokoll alles vollständig gelesen (Muster, Teil 1, Lernpfad, Aufgaben, Quellen, Notizen). Endgültig, kann übersetzt werden (en/es/zh/fr/tr), sobald die fr/tr-Infrastruktur steht. |
| ml | 1 | Überarbeitung mit vollständigem Lesen + Rechenbilder | fertig 04.11. (91 S., 37 Aufgaben, 15 Abb. + 27 Rechenbilder; Website de gebaut). Endgültig, Übersetzung nach ml 2 einreihen. Offen: Rechenbild k1rmittelvektor zeigt 5/2 statt 2,5 (damals konnte s.formel noch keine Dezimalzahlen je Sprache; jetzt möglich, beim Übersetzen anpassen). Neue Regel im Heft: Vektoren mit Dezimalzahlen mit Semikolon (0,2; 0,25)ᵀ. |
| prog | 1 | Python 1: Programme und der Python-Interpreter | fertig 06.11. (45 S., 6 Abschnitte, 19 Aufgaben, 5 Abb.; Website de gebaut; zusammenfassung_kap1.md). Code in code\kap1 unter Windows 3.13 und WSL 3.14 getestet. Nicht getestet: neuer Python install manager (py install), VS Code, IDLE-Start. |
| prog | 2 | Python 2: Werte, Typen und Variablen | fertig 06.11. (85 S., 10 Abschnitte, 41 Aufgaben, davon 37 am Rechner; 7 Abb. + 4 Rechenbilder; 25 Hintergrund-Kästen; Website de gebaut, 12 Artikel; zusammenfassung_kap2.md). Quellen laut Protokoll ganz gelesen. Alle 111/116 Code-Blöcke gegen Windows 3.13 und WSL 3.14 geprüft (code\kap2\heft_pruefen.py), rechnung_kap2.py 82 Prüfungen. pdf_pruefen 0. Endgültig, Übersetzung einreihen. |
| prog | 3 | Python 3: Entscheidungen und Schleifen | fertig 09.11. (81 S., 9 Abschnitte, 35 Aufgaben, davon 30 am Rechner; 9 Abb. + 2 Rechenbilder, alle als Szene prog/k3…; 22 Hintergrund-Kästen, 3 Sätze mit 2 Beweisen; Website de gebaut, 11 Artikel; zusammenfassung_kap3.md). Quellen laut Protokoll ganz gelesen. heft_pruefen: 191 bzw. 192 Blöcke unter Windows 3.13 und WSL 3.14 ohne Abweichung, rechnung_kap3.py 92 Prüfungen. pdf_pruefen 0. Nicht live getestet: Auto-Einrücken im Windows-REPL, „^C“-Echo der Windows-Konsole. Endgültig, Übersetzung einreihen. |
| linux | 1 | Linux 1: Ein Linux zum Üben (WSL 2, VM, Live-USB) | fertig 09.11. (zwei Phasen; 63 S., 9 Abschnitte, 28 Aufgaben, davon 9 am Rechner; 13 Abb. als Szenen linux/k1…; 47 Beispiel-Kästen, 24 Hintergrund, 9 Warnung; Website de gebaut, 11 Artikel; zusammenfassung_kap1.md). Quellen in Phase 1 ganz gelesen; Phase 2 hat das Heft ganz geprüft. Fachlich korrigiert: Hardware-Virtualisierung, Systemaufruf, Rechenfehler 2^32. Code-Abgleich `code\kap1\heft_pruefen.py` 40 Prüfungen, 0 Abweichungen; pdf_pruefen 0. Test-VM (Alpine in qemu) aufgeräumt. Ungetestet nach Doku: wsl --install, VirtualBox, Rufus/Etcher, Firmware, BitLocker. Kontext: Phase 1 637k, Phase 2 541k. Szenen werden per FAKTOR horizontal gestaucht, die Schrift bleibt. |
| linux | 2 | Kapitel 2: Die Shell: erste Befehle | **Phase 1 fertig 10.11.**: 7 Abschnitte, 38 Unterabschnitte, 27 Aufgaben (16 am Rechner), 31 `\szenenabb`, etwa 18 800 Wörter. Code-Abgleich 130 Prüfungen, 0 Abweichungen; rechnung 33/0. Quellen ganz gelesen, Shotts Kap. 1/5/8 ganz (PDF in Recherche\Material). Kontext 554k. **Phase 2a fertig 10.11.:**
  - fachlich korrigiert: free „used“ = total − available, df-Reserve 5 %, Strg+C/D, echo eingebaut, uutils/POSIX;
  - neuer Unterabschnitt 4.4 Seitenanzeiger, Vorgriffe entfernt;
  - 11 Wortersetzungen (Schreibmarke → Cursor u. a.);
  - Code 130/0, Rechnung 37/0; zusammenfassung_kap2.md (142 Z.); Kontext 348k.
  
  **Phase 2b fertig 10.11., abgenommen:**
  - 31 Szenen `linux/k2…` animiert in 6 Sprachen (3,8–11,1 s, 14–294 KB, ≤ 536 px), Vektor-PDFs in `abb/<sprache>`; Kontaktblatt de von mir angesehen, inhaltlich stimmig.
  - `Kap2_Shell.pdf` 61 S., pdf_pruefen 0 (zwei Overfull durch kleine Umstellung in 6.5 und Lösung a:k2vierarten behoben).
  - 9 Artikel, 27 Aufgaben, 0 KaTeX-Fehler; HTML 1677 → 1686, genau die 9 neuen Seiten; Browser (auch 390 px) ohne Fehler, Beispiele zu.
  - Themenkarte: Terminal, Shell, Eingabeaufforderung, Befehl/Argument/Option, Hilfe, Verlauf, Tastenkürzel gelten als erklärt in Linux, Kapitel 2. Python, Kapitel 1 soll den Verweis „Linux, Kapitel 2“ beim nächsten Überarbeiten verlinken.
  - Werkzeug-Wünsche → Editor-Ausbau: Schreibmaschinenschrift für `s.text` (MathJax-Zeichen kosten 1,5–2 KB); `'` und `` ` `` in `\texttt` werden typografisch (k2rsuche zeigt ‘un’); Erscheinen-Objekte liegen über allem (in animationen.md vermerken); `szenen_ansehen.py` exportiert ohne `--animiert` und macht `.anim.svg` veraltet (bis dahin Kontaktblatt aus `abb/de/*.pdf`). |
| ml | G1 | Übersetzung en/es/zh/fr/tr | fertig 09.11. (en 89, zh 79, es 91, fr 93, tr 89 S.; je 0 Fehler, pdf_pruefen 0, Konverter ohne Warnung, je 17 Artikel; alle 42 k1-Szenen samt 27 Rechenbildern in allen Sprachen exportiert). 7 Korrekturen am deutschen Original in alle Fassungen übernommen, dazu Szenen k1ebene/k1reihenfolge ohne überlappende Achsenzahlen. Glossar um ~60 Einträge ergänzt. Offen: Gegenlesen fr/tr durch Muttersprachler; zh Merkmalsvektor = 特征向量 kollidiert mit Eigenvektor (mit englischem Zusatz gelöst); fr „produit extérieur“ (Glossar G2) ist mehrdeutig, Alternative „produit tensoriel“; Szene k1schatten: Beschriftung kreuzt die x₂-Achse. |
| ml | 2 | Übersetzung en/es/zh/fr/tr | fertig 06.11. (alle sechs Sprachen 0 Fehler, je 14 Artikel; 7 Korrekturen am deutschen Original in alle Fassungen übernommen; Aufgabentitel a:k2detklein jetzt „Determinante 1, trotzdem schlechte Kondition“). Brief mit Glossar: notizen/uebersetzung_brief_zusatzreihen.md. |
| cyber | 1 | Überarbeitung mit vollständigem Lesen + Rechenbilder | fertig 05.11. (74 S., 20 Aufgaben, 8 Abb. + 10 Rechenbilder; Website de gebaut). Alles ganz gelesen, Rechtsstand zum 05.11. unverändert (StGB zuletzt 20.03.2026, kein Reformentwurf). Endgültig, Übersetzung einreihen. Neu: Unterabschnitt Gesamtrisiko, CVSS-Formel im Haupttext, § 202a nach BGH 5 StR 614/19, Plattformregeln korrigiert (OverTheWire untersagt Passwörter, pwn.college bittet). Szene k1rcvss: Symbole W/E müssen in allen Sprachen gleich bleiben. |
| ml | 3 | Ableitung, Gradient, Kettenregel, autom. Differentiation | fertig 05.11. (73 S., 11 Abschnitte, 42 Aufgaben, 10 Abb. + 10 Rechenbilder; Website de gebaut). Alles ganz gelesen, Selbstprüfung über das ganze Heft. Endgültig, Übersetzung einreihen. |
| ml | 4 | Wahrscheinlichkeit | fertig 05.11. (78 S., 13 Abschnitte, 44 Aufgaben, 8 Abb. + 12 Rechenbilder; Website de gebaut). Alles ganz gelesen, Selbstprüfung über das ganze Heft. Endgültig, Übersetzung einreihen. Notation: P (Wahrscheinlichkeit), p (Dichte), Zufallsvariable groß X, Zufallsvektor fett klein x (weil X die Datenmatrix ist), ρ, θ (Bernoulli), 𝛍, 𝚺, Datenkovarianz 𝐒 = (1/N) X̃ᵀX̃, Rauschen ν, Mahalanobis Δ, Indikator 𝟙_A. Nach T05 verschoben: Likelihood, Prior/Posterior/MAP, Bessel, Entropie, Max-Entropie, Beta-Verteilung. |
| ml | 5 | Statistik und Information | fertig 06.11. (69 S., 11 Abschnitte, 48 Aufgaben, 11 Abb. + 11 Rechenbilder; Website de gebaut; zusammenfassung_kap5.md). Endgültig, Übersetzung einreihen. Notation: Likelihood 𝓛, ℓ, Datensatz 𝒟, N₁/N₀, Bias/SE/MSE als Operatoren, σ̂²_N bzw. σ̂²_{N−1}, Beta(α₁, α₀), Entropie H(𝐩) kursiv (Hesse-Matrix 𝐇_f fett), D_KL. Präambel: \vl \Bias \MSE. |

Hinweise prog 2 (verbindlich für spätere Hefte):
- **Reihenfolge in Python 2:** Objekte/Typen, int, Binär/Hex/Byte, float (IEEE 754), Rechnen mit float, Variablen, bool/Vergleiche/`is`/None, Module math und sys, complex (Präambel `\jj`), Zeichenketten/f-String/input/Runden.
- **Schon eingeführt:** Methode, Attribut, Modul/`import`, `is` (Abschnitt 7.5; laut Lernpfad eigentlich Python 5, dort zurückverweisen), Byte, Hexadezimalzahl, `divmod`, `math.isclose` mit Angaben „mit Namen“ (Begriff Schlüsselwortargument erst in Python 4).
- **Nicht vorweggenommen:** Wahrheitswert anderer Objekte (`bool("0")`) gehört zu Python 3; `sum`/`math.fsum` mit Listen zu Python 5.
- **Bezeichnungen:** Vorzeichen s, Exponentenfeld c (nicht e), Mantissenfeld t (nicht f), „Verschiebung“ statt Bias, ε_M = 2⁻⁵² wie in ML Grundlagen 3 (Rundungsschranke ε_M/2), „einstellig/zweistellig“ statt unär/binär.
- **Rückverweise möglich:** Cybersecurity (Bits/Bytes/Hex) und ML Grundlagen 3, Abschnitt 11.3 (ε_M) können auf „Programmieren, Python 2“ verweisen; in der Themenkarte eingetragen.

Hinweise prog 3 (verbindlich für spätere Hefte):
- **Reihenfolge in Python 3:** Bedingungen (verkettete Vergleiche, not/and/or, Kurzschluss, Wahrheitswert), if/elif/else mit Block und Einrückung, while (Endlosschleife, Strg+C, Gleitkomma-Falle), for/range, break/continue/Verschachtelung/Akkumulator, Raten und Prüfen, Bisektion (Zwischenwertsatz, Schrittzahl), Newton (Heron, quadratische Konvergenz), Diode als Anwendung.
- **Nicht vorweggenommen:** Listen und `for` über beliebige Folgen, `[]` als falscher Wert, `sum`/`max` über Listen (Python 5; Python 3 sagt „von den bisher bekannten Werten“); binäre Suche (Python 7).
- **Bezeichnungen:** Fehler d_n (nicht e_n), Boltzmann-Konstante k_B, Intervall im Zwischenwertsatz [x₁, x₂], Intervalllänge L, Stellenzahl p; Temperaturspannung 25,85 mV.
- **Gleitkomma-Schleifen** zählen ganzzahlig (`x < 1.0` statt `!=` reicht nicht); Newton mit relativer Toleranz.
- **Präambel:** `konsole` kennt seit 09.11. die Fortsetzungszeile `... ` (nur Programmieren, nicht Linux, wegen Ausgaben wie „Reading package lists... Done“).

Hinweise ml 3 (verbindlich für spätere Hefte):
- **Layout-Konvention:** Vektoren sind Spalten; der Gradient ∇f hat die Form von x (Spalte); die Jacobi-Matrix J_g ∈ ℝ^{m×n} hat eine Zeile je Ausgang, (J)ᵢⱼ = ∂gᵢ/∂xⱼ, also J_f = ∇fᵀ.
- **Kettenregel:** J_{f∘g} = J_f J_g und ∇(f∘g) = J_gᵀ∇f. ∇_A f hat die Form von A. (H_f)ᵢⱼ = ∂²f/∂xᵢ∂xⱼ.
- **Automatische Differentiation:** Adjungierte ā = ∂f/∂a, Tangentenwert ḃ. ε_M = 2⁻⁵² heißt Maschinengenauigkeit.
- **Umbenennungen in Teil 3:** H aus Teil 2 heißt A, weil H die Hesse-Matrix ist; Schrittweite h; statt L (Verlust) überall ein allgemeines f. Die logistische Funktion σ ist eingeführt, mit σ′ = σ(1−σ), ohne ML-Zweck.
- **Präambel ergänzt:** `\mJ \vg \vt \vgamma`.

Hinweise ml 2:
- SVD als A = UDVᵀ mit d_j; Residuum r = y − Ax̂; ŷ, x̂, P; Drehungen heißen Q (R ist das R der QR-Zerlegung); λ_i, Λ, S mit s_i; Cholesky L; Links-/Rechtsinverse F/G; A⁺; κ = d₁/d_n; ‖·‖₂ Spektralnorm, ‖·‖_F Frobenius; z*; imaginäre Einheit j.
- Rechenbilder (Regel umgesetzt): je Rechenbeispiel im Haupttext, in dem Summe oder Skalarprodukt Kernstück ist; nicht für Proben, Wiederholungen, Beweise, Hintergrund und Lösungen. Vom User bestätigt am 04.11.2026: „bei Beweisen, Rechnungen, etc. brauchen wir die Animationen nicht“.
- Präambel ergänzt: `\vs \vh \vd \vi \vbeta \mF \mG \mL \mM`.

**Überarbeiten wegen gekürzten Lesens** (User 04.11.2026: „Bereits erstellte Artikel überarbeiten, falls sie noch das alte Prinzip für das Durchlesen genutzt haben“):
- **Befund aus den Agentenprotokollen:**
  - cyber 1 und ml 1 haben die Musterhefte nur in Teilen gelesen (ET3 `kap2_stufen.tex` bis etwa Zeile 760, `kap2_stufen_b.tex` gar nicht, HöMa3 `kap1_stufen.tex` 200–420 Zeilen, Lösungen 40–60 Zeilen), Lernpfad und Notizen nur in Ausschnitten.
  - Die WISSEN-Dateien und den Leitfaden haben sie ganz gelesen.
- **Reihenfolge,** je ein Schreib-Agent nacheinander, mit dem neuen Abschnitt „Zuerst lesen“: nach ml 2 zuerst ml 1 überarbeiten, dann cyber 1. Dabei auch die Summen- und Skalarprodukt-Abbildungen einbauen, sobald der Editor sie kann.
- **Uni-Module:** Ihre Hefte haben das Skript nur kapitelweise und die Muster teilweise gelesen. Sie stehen ohnehin auf der Überarbeitungsliste in `ueberarbeitung_stand.md` (HöMa pausiert); `ueberarbeitung_auftrag.md` verlangt jetzt ebenfalls vollständiges Lesen, auch des ganzen Skripts.

Hinweise ml 1:
- Festgelegte Bezeichnungen für alle späteren ML-Hefte stehen im Bericht des Agenten. Kern: N Beispiele (i), d Merkmale (j), x_i Spaltenvektor, X ∈ ℝ^{N×d} mit Zeilen x_iᵀ, Gewichte w, Vorhersage ŷ = Xw, rechte Seite y, Achsenabschnitt b, λ unbenutzt, std mit Nenner N, Einsvektor `\veins`, Tensorform N×C×H×W. Wiederverwendbarer Wohnungs-Datensatz X ∈ ℝ^{4×3}, w = (3, 10, −4), b = 20, y = (200, 130, 290, 240).
- Standardisieren ist schon in ml 1 eingeführt; T07/T08 verweisen nur zurück.
- Präambel ergänzt: `\vk \vp \veins \mK \mR`. Akzente auf Makros nur mit Klammern (`\bar{\vx}`), sonst KaTeX-Fehler.
- Szenen k1lgs und k1spann vom Haupt-Agenten nachgebessert (Titel über x₂, Abstände, ohne Zahlen bei spann).
- Der Agent hatte fast 800k Tokens Kontext, weil er das PDF zehnmal als Bilder gelesen hat. Deshalb gibt es jetzt `tools/pdf_pruefen.py`: Es prüft maschinell auf fehlende Verweise, Überstand über den Satzspiegel, überlappende und aneinanderstoßende Beschriftungen in Abbildungen und schreibt Ausschnitte und Übersichtsblätter. Steht im Auftrag. Getestet an fünf abgenommenen Heften (0 Fehlalarme) und an einem Fehlerbeispiel.

Hinweis cyber 1: Die Sitzung, die den Schreib-Agenten gestartet hatte, wurde kurz vor seinem Bericht beendet. Schlussprüfung deshalb vom Haupt-Agenten: PDF 0 Fehler, keine Overfull-Boxen, Konverter 0 KaTeX-Fehler, Szenen neu exportiert und angesehen, Rechtsteil gegen die Recherche-Notizen geprüft (Wortlaute, Strafrahmen, §§ 205/303c, BVerfG 2009, Reformstand). Recherche-Notizen des Agenten: `C:\Bücher\EtUndSo\Cybersecurity\Recherche\Notizen\L_heft1_recherche.md`.

## Entscheidungen des Users (04.11.2026)
- Eigene Zusammenfassungen in `C:\Bücher\allgemeineThemen` werden nicht korrigiert; es geht nur um die Website.
- ML-Ast F6 (TinyML) wird allgemein für einen typischen Mikrocontroller geschrieben, nicht für ein bestimmtes Board des Users.
- Linux zum Testen: ja → Ubuntu 26.04 unter WSL.
