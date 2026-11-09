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
- Vorbereitet 09.11.: `MODULE["linux"]["hefte"]` 1–11 (sechs Sprachen), Heftordner `EtUndSo\Linux\Arbeitshefte` mit Präambeln (Kopie Programmieren), `tools/szenen/linux_teil1.py`.
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
7. **Werkzeug-Wünsche aus den Heften (offen):** `s.summe`/`s.produkt` mit anderem Laufindex als i und exakten großen Brüchen (3/131072); `code\kap2\heft_pruefen.py` als allgemeines Werkzeug nach `tools/`. Erledigt 06.11.: `\jj` in der Programmieren-Präambel, Code in `\texttt`/`\mathtt` behält in Szenen den Dezimalpunkt (editor.js localizeTex), Backticks in Artikeltiteln (build_wissen).

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
| linux | 1 | Linux 1: Ein Linux zum Üben (WSL 2, VM, Live-USB) | Phase 1 (Schreiben) läuft seit 09.11.; danach Phase 2 (Prüfen) |
| ml | G1 | Übersetzung en/es/zh/fr/tr | in Arbeit (06.11.; en fertig, zh läuft, es/fr/tr offen; englische Rechenbilder k1r* noch nicht exportiert) |
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
