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
- T01–T06 werden „Grundlagen 1–6“ in einem eigenen Bereich „Mathematische Grundlagen (zum Nachschlagen)“. Der ML-Pfad beginnt mit T07 als „Teil 1“ (ML-Teil N = T(N+6)).
- Jedes Pfad-Heft fasst benötigte Mathematik in „Was du dafür brauchst“ kurz zusammen und verweist mit Link auf „Grundlagen N, Abschnitt M“. Grundlagen-Abschnitte zeigen auf der Website automatisch, welche ML-Artikel sie verwenden.
- Reihenfolge: nach Grundlagen 5 (T05, läuft) direkt Pfad-Teil 1 (T07 Python/NumPy) und Teil 2 (T08 Lernen aus Daten). Grundlagen 6 (T06 Optimierung) erst vor dem Gradientenabstieg.
- **Noch umzusetzen** (Infrastruktur-Agent, sobald T05 und die Übersetzung von T02 fertig sind):
  - Konverter und Website: eigener Bereich und Pfad, Beschriftung „Grundlagen N“ bzw. „Teil N“ in sechs Sprachen, Verweise „Grundlagen N“ und „Teil N“ als Links, automatische Rückverweise „verwendet in“;
  - in den Heften T01–T05 und allen Übersetzungen „Teil N“ durch „Grundlagen N“ ersetzen (Titelzeilen, Rückverweise);
  - Dateinamen und Szenennamen bleiben (Kap1_Vektoren …, ml/k1…); die Pfad-Hefte bekommen die Dateien Kap7_… usw. weiter nach Lernpfad-Nummer, nur die Anzeige zählt ab 1.

## Gemeinsame Bereiche, nichts doppelt (Entscheidung des Users, 06.11.2026)
- Der User: „Inhalte nicht mehrfach auf der Webseite vollständig erklären“. Jedes Thema wird genau einmal vollständig erklärt, andere Hefte verweisen mit Link und setzen es voraus. Die Regel steht im Auftrag unter „Nichts doppelt erklären“.
- **Neue Bereiche:**
  - **„Programmieren“:** Python mit Sprache, Datenstrukturen, Funktionen, Module, venv und NumPy-Grundlagen; später C und C++.
  - **„Linux und Kommandozeile“:** Shell, Dateien, Rechte, Prozesse.
  - ML und Cybersecurity setzen beide voraus. Cyber T03–T05 (Linux/Shell), T08 (Python) und T09 (C) werden dadurch zu cyber-spezifischen Heften oder fallen weg; das legt eine Recherche fest.
- **ML-Teil 1 (T07 Python/NumPy) entfällt im ML-Pfad.** Der ML-Pfad beginnt direkt mit „Lernen aus Daten“ (T08) als Teil 1. ML-eigene Werkzeuge wie scikit-learn und das Laden von Datensätzen kommen dort, wo sie zuerst gebraucht werden. Damit gilt: ML-Teil N = T(N+7).
- **ML-Grundlagen gegen HöMa:** prüfen und verlinken. Was ein HöMa-Artikel schon vollständig erklärt, steht in den Grundlagen nur als Kurzfassung mit Link. Das wird bei der nächsten Überarbeitung über die Themenkarte geprüft.
- **`notizen/themenkarte.md`** muss angelegt werden: Thema → Bereich/Heft/Abschnitt, aus den vorhandenen Heften und Lernpfaden.

## Koordination
Wie der Haupt-Agent Agenten beauftragt, prüft und berichtet, steht in `notizen/koordination.md`. Diese Datei vor jedem Arbeitsschritt lesen.

## Nächste Schritte (Stand 06.11.2026, früh)
1. ~~Grundlagen 5 fertigschreiben~~ (erledigt 06.11.)
2. ~~Übersetzung von Grundlagen 2~~ (erledigt 06.11.)
3. **Infrastruktur-Agent für den Umbau** (gestartet 06.11. nachmittags):
   - ML-Grundlagen als eigener Bereich, Beschriftung „Grundlagen N“, „Teil N“ → „Grundlagen N“ in T01–T05 und allen Übersetzungen, automatische Rückverweise „verwendet in“;
   - ML-Pfad-Nummerierung mit Teil N = T(N+7);
   - Website-Bereiche „Programmieren“ und „Linux und Kommandozeile“ vorbereiten;
   - Link-Erkennung für „Programmieren, Python N“ usw.;
   - `notizen/themenkarte.md` anlegen.
4. **Recherche und Lernpfad** (gestartet 06.11. nachmittags, Ablage EtUndSo\Programmieren\Recherche und EtUndSo\Linux\Recherche) für „Programmieren“ (Python, später C/C++) und „Linux und Kommandozeile“, aus den vorhandenen WISSEN-Dateien (ML T07, Cyber T03–T05, T08, T09) und neuen Hauptquellen. Danach den Cyber-Lernpfad anpassen.
5. **Schreiben:**
   - Python-Hefte (Bereich Programmieren) zuerst;
   - dann ML-Pfad Teil 1 „Lernen aus Daten“ (T08), mit „erst selbst bauen, dann Bibliothek“ und Verweisen statt Wiederholung.
6. **Übersetzungen einreihen:** Grundlagen 1, 3, 4, 5 und Cybersecurity Teil 1, je ein Übersetzungs-Agent parallel zum Schreib-Agenten.

## Hefte

| Reihe | Teil | Thema | Stand |
|---|---|---|---|
| cyber | 1 | Sicherheit, Schutzziele und Spielregeln | fertig 04.11. (68 S., 10 Abschnitte, 20 Aufgaben, 8 Abb.; Website de gebaut), wartet auf Abnahme |
| ml | 1 | Vektoren und Matrizen | fertig 04.11. (82 S., 15 Abschnitte, 37 Aufgaben, 15 Abb.; Website de gebaut), wartet auf Abnahme |

| ml | 2 | Projektion, Eigenwerte und Zerlegungen | fertig 04.11. (85 S., 12 Abschnitte, 38 Aufgaben, 11 Abb. + 18 Rechenbilder; Website de gebaut). Laut Protokoll alles vollständig gelesen (Muster, Teil 1, Lernpfad, Aufgaben, Quellen, Notizen). Endgültig, kann übersetzt werden (en/es/zh/fr/tr), sobald die fr/tr-Infrastruktur steht. |
| ml | 1 | Überarbeitung mit vollständigem Lesen + Rechenbilder | fertig 04.11. (91 S., 37 Aufgaben, 15 Abb. + 27 Rechenbilder; Website de gebaut). Endgültig, Übersetzung nach ml 2 einreihen. Offen: Rechenbild k1rmittelvektor zeigt 5/2 statt 2,5 (damals konnte s.formel noch keine Dezimalzahlen je Sprache; jetzt möglich, beim Übersetzen anpassen). Neue Regel im Heft: Vektoren mit Dezimalzahlen mit Semikolon (0,2; 0,25)ᵀ. |
| ml | 2 | Übersetzung en/es/zh/fr/tr | fertig 06.11. (alle sechs Sprachen 0 Fehler, je 14 Artikel; 7 Korrekturen am deutschen Original in alle Fassungen übernommen; Aufgabentitel a:k2detklein jetzt „Determinante 1, trotzdem schlechte Kondition“). Brief mit Glossar: notizen/uebersetzung_brief_zusatzreihen.md. |
| cyber | 1 | Überarbeitung mit vollständigem Lesen + Rechenbilder | fertig 05.11. (74 S., 20 Aufgaben, 8 Abb. + 10 Rechenbilder; Website de gebaut). Alles ganz gelesen, Rechtsstand zum 05.11. unverändert (StGB zuletzt 20.03.2026, kein Reformentwurf). Endgültig, Übersetzung einreihen. Neu: Unterabschnitt Gesamtrisiko, CVSS-Formel im Haupttext, § 202a nach BGH 5 StR 614/19, Plattformregeln korrigiert (OverTheWire untersagt Passwörter, pwn.college bittet). Szene k1rcvss: Symbole W/E müssen in allen Sprachen gleich bleiben. |
| ml | 3 | Ableitung, Gradient, Kettenregel, autom. Differentiation | fertig 05.11. (73 S., 11 Abschnitte, 42 Aufgaben, 10 Abb. + 10 Rechenbilder; Website de gebaut). Alles ganz gelesen, Selbstprüfung über das ganze Heft. Endgültig, Übersetzung einreihen. |
| ml | 4 | Wahrscheinlichkeit | fertig 05.11. (78 S., 13 Abschnitte, 44 Aufgaben, 8 Abb. + 12 Rechenbilder; Website de gebaut). Alles ganz gelesen, Selbstprüfung über das ganze Heft. Endgültig, Übersetzung einreihen. Notation: P (Wahrscheinlichkeit), p (Dichte), Zufallsvariable groß X, Zufallsvektor fett klein x (weil X die Datenmatrix ist), ρ, θ (Bernoulli), 𝛍, 𝚺, Datenkovarianz 𝐒 = (1/N) X̃ᵀX̃, Rauschen ν, Mahalanobis Δ, Indikator 𝟙_A. Nach T05 verschoben: Likelihood, Prior/Posterior/MAP, Bessel, Entropie, Max-Entropie, Beta-Verteilung. |
| ml | 5 | Statistik und Information | fertig 06.11. (69 S., 11 Abschnitte, 48 Aufgaben, 11 Abb. + 11 Rechenbilder; Website de gebaut; zusammenfassung_kap5.md). Endgültig, Übersetzung einreihen. Notation: Likelihood 𝓛, ℓ, Datensatz 𝒟, N₁/N₀, Bias/SE/MSE als Operatoren, σ̂²_N bzw. σ̂²_{N−1}, Beta(α₁, α₀), Entropie H(𝐩) kursiv (Hesse-Matrix 𝐇_f fett), D_KL. Präambel: \vl \Bias \MSE. |

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
