# Durchsicht Abbildungen und Animationen: Übersicht (09.11.2026)

Umfang: alle deutschen Website-Artikel, 8 Module, 21 Pakete (je ein Sonnet-Unteragent, Artikel ganz gelesen).
Grundlagen: `EDITOR_KANN.md` (was der Editor kann, Lücken L1–L10), `RICHTLINIEN.md` (Regeln, feste Vorschlagsform),
`SOLL_JE_ARTIKEL.md` (Soll je Artikel). Die Vorschläge stehen in `<modul>_<paket>.md`. Jedes Paket enthält eine
Kurzbilanz je Artikel, die Top 3, die Editor-Lücken, die Vorschläge V1…Vn und eine Zeile je vorhandener Abbildung
(animieren ja/nein, in welchen Schritten).

**Ausgangslage:** 670 Abbildungen in den Artikeln (703 Szenen-Dateien). **Keine einzige Szene hat eine Zeitachse.**
Nur 10 Szenen nutzen eine ablaufende Editor-Operation (Σ, ∏, Skalarprodukt). 214 von 721 Artikeln haben keine Abbildung.

## 1. Zahlen je Modul

| Modul | Artikel | vorh. | Soll | neu A | neu B | neu C | entfällt | nachher | vorh. zum Animieren geeignet | Rechenbilder statisch / Operation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| cyber | 12 | 18 | 45 | 19 | 11 | 0 | 3 | 45 | 15 von 15 verbleibenden | 10 / 0 |
| et1 | 131 | 123 | 156 | 53 | 4 | 0 | 2 | 178 | 117 | – |
| et3 | 90 | 55 | 109 | 73 | 10 | 0 | 3 | 135 | 54 | – |
| gemb1 | 192 | 141 | 226 | 60 | 28 | 15 | 0 | 241 | 141 | – |
| hm1 | 110 | 88 | 134 | 53 | 5 | 0 | 0 | 146 | 88 | – |
| hm3 | 83 | 85 | 122 | 53 | 14 | 0 | 8 | 144 | 77 von 77 verbleibenden | 1 / 0 |
| ml | 72 | 133 | 227 | 92 | 25 | 0 | 9 | 241 | 133 | 70 / 8 |
| prog | 31 | 27 | 110 | 52 | 26 | 4 | 2 | 107 | 26 | 4 / 2 |
| **Summe** | **721** | **670** | **1129** | **455** | **123** | **19** | **27** | **1237** | **651** | **85 / 10** |

- „neu“ enthält etwa 65 Wiederverwendungen vorhandener Szenen, vor allem für Überblicks- und „Das Wichtigste“-Artikel.
  Diese brauchen keine neue Zeichnung.
- Nicht mitgezählt sind 3 reine Animationsvorschläge vorhandener Bilder (gemb1_a) und 2 Umbauten von Rechenbildern
  (ml_3).
- „nachher“ = vorhanden − entfällt + neu.
- Rund zwei Drittel der neuen Vorschläge gehen mit dem heutigen Editor. Fast alle übrigen haben einen Notbehelf
  (feste Zustände nacheinander einblenden).

### Verteilung: Artikel mit 0 / 1–5 / über 5 Abbildungen

| Modul | vorher | nachher |
|---|---|---|
| cyber | 5 / 6 / 1 | 0 / 12 / 0 |
| et1 | 27 / 104 / 0 | 0 / 131 / 0 |
| et3 | 48 / 42 / 0 | 0 / 90 / 0 |
| gemb1 | 54 / 138 / 0 | 0 / 192 / 0 |
| hm1 | 29 / 81 / 0 | 0 / 110 / 0 |
| hm3 | 20 / 62 / 1 | 0 / 83 / 0 |
| ml | 17 / 53 / 2 | 0 / 72 / 0 |
| prog | 14 / 17 / 0 | 0 / 31 / 0 |

**Während der Durchsicht hat sich der Bestand geändert** (andere Agenten):
- hm3 Heft 3 hat jetzt 10 statt 3 Artikel. hm3_b hat die neuen Artikel durchgesehen, die Zahlen oben gelten für sie.
- Die Ordner `content/gemb1/16-…`, `17-…` und `19-…` (30 Artikel) fehlen inzwischen im Arbeitsverzeichnis. gemb1_c hat
  sie aus dem letzten Commit gelesen; ihre Vorschläge (in `gemb1_c.md`) gelten, sobald die Hefte wieder da sind oder
  für ihre Nachfolger. Zu Szenen `gemb1/k18*` (8 Stück) gibt es kein Heft 18.

### Zählmaßstab: Bewertung
- **Länge (1 Bild je 450 Wörter, Kästen halb):**
  - Für die langen Artikel (ml, prog, cyber, hm3) greift die Obergrenze 5.
  - Bei den kurzen Artikeln (et1, et3, gemb1, hm1, im Mittel 550–700 Wörter) ergibt sich fast immer Soll 1.
  - Dort gingen die Unteragenten in 103 Artikeln (14 %) begründet auf +1. Der Grund war meist ein zweiter neuer Begriff
    oder ein Pflicht-Rechenbild.
  - **Besserer Maßstab:** Soll = Maximum aus Längen-Soll und Zahl der neu eingeführten Begriffe und Verfahren
    (UEBERARBEITUNG §2: jeder neue Begriff bekommt eine Anschauung), begrenzt auf 1 bis 5. Das bildet die
    +1-Begründungen genau ab.
- **Rechenbilder:** Sie sind hier mitgezählt. Es gibt zwei Gründe, sie getrennt oder halb zu zählen:
  1. Pflicht-Rechenbilder verdrängten Begriffsbilder. hm3_a ließ Rechenbeispiele wegen des vollen Solls ohne Rechenbild.
     ml_1 (Artikel 03, 04) und cyber (Artikel 04 mit 7) mussten wegen der Rechenbilder zusammenlegen.
  2. Rechenbilder stehen meist im zugeklappten `beispiel`-Kasten, den der Leser nur aufgeklappt sieht.

  Vorschlag: Rechenbilder in Beispiel-Kästen zählen wie der Kasten nur halb. Pflicht-Rechenbilder haben Vorrang vor
  allen B- und C-Bildern.

## 2. Muster: wo am meisten fehlt
1. **Bewegung fehlt überall.** 651 vorhandene Abbildungen eignen sich zum Abspielen; jede Paketdatei nennt die Schritte.
   Am meisten bringt das bei Kennlinien mit Arbeitspunkt, Bänderbildern, Feldern, Wellen und Blockbildern.
2. **Ganze Artikel ohne Bild (214).**
   - Gehäuft betroffen sind die Artikel „Überblick“, „Von Grund auf“ und „Das Wichtigste“ (gemb1, hm1, et1). Dort genügt
     meist eine vorhandene Szene als Zusammenschau.
   - et3 Hefte 3–8: 41 von 69 Artikeln ohne Bild.
   - ml 4 Artikel 03, 06, 10: Axiome, Unabhängigkeit und mehrere Zufallsvariablen haben gar keine Anschauung.
3. **Verfahren stehen als reine Zahlenfolge da:**
   - Gauß (hm1, ml), Maschenstrom- und Knotenpotenzialverfahren, Laplace-Verfahren, Arbeitspunkt-Iteration
   - Potenzmethode, Vorwärtsmodus der automatischen Differentiation, Bisektion, Heron
   - Programmablauf Zeile für Zeile
4. **Rechenbilder:**
   - 85 der 95 vorhandenen Rechenbilder sind ein einziges statisches MathTex: ml 70 von 78, cyber 10 von 10, prog 4
     von 6, hm3 1. Sie laufen nicht ab und müssen auf Σ, ∏ oder Skalarprodukt umgebaut werden.
   - Dazu fehlen mindestens 30 Pflicht-Rechenbilder. Beispiele: et1 Σ der Leitwerte und Kapazitäten, Skalarprodukte im
     Plattenfeld; ml_5 Wohnungen, Spannungen, gewichtetes Mittel; hm3_c Erwartungswert und Varianz; ml_4 ∏ 0,95¹⁰.
5. **Physikalische Prozesse ohne Bewegung (gemb1, et1):** Wellen, Ladungsträger, Bänder unter Spannung,
   Raumladungszone, Abschnürung. Sie brauchen meist L3 oder L6.
6. **Größte absolute Lücke in den langen Reihen:** prog von 27 auf 107, ml von 133 auf 241, cyber von 18 auf 45.

## 3. Die 30 wichtigsten Vorschläge
Ausgewählt nach: Kernbegriff oder Kernverfahren eines Hefts ohne Bild, lebt von Bewegung, trägt Folgekapitel.
„machbar“ = heutiger Editor; sonst Lücke mit Notbehelf.

| # | Paket/V | Artikel (content/…) | Was | Lücke |
|---:|---|---|---|---|
| 1 | et3_a V6 | et3/01…/06-die-faltung-ausrechnen | Spiegeln und Schieben Schritt für Schritt (Alter statt Zeitpunkt) | machbar (Faltungs-Op.) |
| 2 | et3_a V16 | et3/02…/02-eigenfunktionen-von-lti-systemen | verschobene Kopie = skalierte Kopie: e-Funktion als Eigenfunktion | machbar |
| 3 | et3_a V22 | et3/02…/05-losung-von-differentialgleichungen | Laplace-Verfahren am RC-Sprung: DGL → Partialbruch → Rücktransformation | L2 |
| 4 | et3_b V2 | et3/03…/02-schwingungen-als-eigenfunktionen | Zeiger durch das LTI-System nur skaliert und gedreht (0,707, −45°) | L3 |
| 5 | et3_b V47 | et3/07…/11-das-korrelationsfilter-matched-filter | Filter gleitet über das verrauschte Signal, Spitze bei T | machbar (Faltungs-Op.) |
| 6 | et1_a V9 | et1/02…/08-die-knotenregel-ist-ladungserhaltung | Selbstregelung des Knotens: Potenzial steigt, bis Zu- = Abfluss | machbar |
| 7 | et1_a V4 | et1/01…/07-feldlinien-und-leiter | Influenz im Metallrohr, Feld im Inneren verschwindet | L1 |
| 8 | et1_b V15 | et1/08…/05-das-maschenstromverfahren | Matrix Z Zelle für Zelle aus der Schaltung ablesen | L9 |
| 9 | et1_c V9 | et1/10…/04-warum-strom-durch-die-gesperrte-diode-fliet | Elektronengefälle in der Basis; +18 mV verdoppelt den Strom | machbar |
| 10 | et1_c V15 | et1/11…/07-die-regel-und-die-virtuelle-masse | virtuelle Masse als Potenzialprofil (1 V, 0 V, −4 V) | L1, L2 |
| 11 | gemb1_a V12 | gemb1/02…/05-das-elektron-zwischen-zwei-wanden | nur ganze Halbwellen passen (kL = nπ): Quantisierung | L3 |
| 12 | gemb1_a V25 | gemb1/04…/04-das-wasserstoffatom | E_kin ~ 1/a², E_pot ~ −1/a, Minimum 0,0529 nm / −13,6 eV | machbar |
| 13 | gemb1_b V9 | gemb1/08…/04-bander-und-lucken | stehende Wellen am Zonenrand: Mechanismus der Bandlücke | machbar |
| 14 | gemb1_c V8 | gemb1/14…/04-der-ubergang-im-gleichgewicht | Raumladungszone bildet sich (Diffusion, Rekombination, Feld stoppt) | L6, L1 |
| 15 | gemb1_c V23 | gemb1/17…/06-ausgangskennlinien | Kanal schnürt ab, Punkt läuft gleichzeitig auf der Kennlinie | L2, L3 (Heft fehlt derzeit) |
| 16 | hm1_a V5 | hm1/01…/07-vollstandige-induktion-summe-und-produkt | Dominokette: Anfang stößt an, Schritt reicht weiter | machbar |
| 17 | hm1_a V25 | hm1/05…/09-maximum-minimum-gleichmaige-stetigkeit | ε-δ-Kasten wandert: x² gleiches δ, 1/x schrumpfendes δ | machbar |
| 18 | hm1_b V30 + ml_1 V14 | hm1/10…/09-der-gau-algorithmus, ml/01…/13-lineare-gleichungssysteme | Gauß-Tableau Zeile für Zeile (eine Vorlage, zwei Zahlensätze) | L2, L9 |
| 19 | hm3_a V17 | hm3/02…/04-mehrfachintegrale | Dreifachintegral als Stab → Platte → Quader (Ergebnis 18) | machbar |
| 20 | hm3_b V3 | hm3/03…/03-das-kurvenintegral | Kurvenintegral als wachsende Summe über Wegstücke (→ π/2), Rechenbild | machbar |
| 21 | hm3_b V10 | hm3/03…/09-integralsatze-in-der-ebene | Green: Innenkanten heben sich auf, nur der Rand bleibt | machbar |
| 22 | hm3_c V10 | hm3/07…/09-punktweise-konvergenz | Dirichlet-Kern gleitet über den Sprung: Gibbs-Überschwinger | machbar (Faltungs-Op.) |
| 23 | ml_2 V8 | ml/02…/08-diagonalisierung-und-spektralsatz | in der Eigenbasis wird nur gestreckt (×5, ×2) | machbar |
| 24 | ml_2 V12 | ml/02…/10-die-singularwertzerlegung | Einheitskreis wird Ellipse, v₁, v₂ → 4u₁, 1u₂ (behebt Vorgriff auf Abb. 23) | L5 |
| 25 | ml_3 V6 | ml/03…/04-partielle-ableitungen-und-der-gradient | Tangentialebene schmiegt sich an die Fläche | L4 |
| 26 | ml_4 V8 | ml/04…/05-der-satz-von-bayes | Basisrate: dasselbe Gerät bei 0,1 / 1 / 10 / 50 % Defekten | L6 |
| 27 | ml_5 V19 | ml/05…/12-maximum-likelihood-und-kl-divergenz | Kreuzentropie über θ; Marker 0,5 → 0,7, KL-Abstand → 0 | L3 |
| 28 | prog_a V37 | prog/02…/07-variablen-namen-fur-objekte | Zuweisungen Zeile für Zeile: Namen zeigen auf Objekte | L8, L-neu Pfeil umhängen |
| 29 | prog_b V7 | prog/03…/03-entscheidungen-if-elif-und-else | Skript Zeile für Zeile, übersprungener Block | L8 |
| 30 | cyber_1 V10 | cyber/01…/05-richtlinie-und-mechanismus | Nachricht unterwegs: Lauscher kopiert, Fälscher ersetzt | machbar |

Weitere starke Kandidaten:
- hm3_c V5 (laufendes Rechteck)
- et3_b V17 (DFT als Zeigerkette, Pflicht-Rechenbild)
- et1_b V18 (Netzliste stempelt die Matrix)
- gemb1_b V28 (drei Temperaturbereiche)
- ml_3 V18 (Vorwärtsmodus)
- prog_a V33 (0.1 + 0.2)

## 4. Editor-Lücken mit Häufigkeit
Gezählt aus den Paketberichten: zuerst neue Vorschläge, dann vorhandene Szenen. Darin enthalten sind Fälle, die die
Unteragenten nur als „hilfreich“ markiert haben.

| Lücke | Vorschläge | vorh. Szenen | Bemerkung |
|---|---:|---:|---|
| L10 Abspielknopf im Artikel | alle | alle | Voraussetzung für alles (anderer Agent) |
| L3 Parameter/Zeit animieren | 63 | 84 | Abstand größter Hebel: laufende Wellen, Arbeitspunkt wandert, Zeitmarker liest mehrere Kurven ab, Grenzprozesse |
| L1 Verschwinden (FadeOut) | 31 | 10 | Engine hat FadeOut, nur nicht im Modell |
| L9 Zellen einzeln betonen | 20 | 2 | Matrizen, Tableaus, Tabellen (ml, et1 Heft 8, cyber) |
| L2 Umformen (Transform, TransformMatchingTex) | 19 | 7 | Engine hat sie, nur nicht im Modell; Formel- und Formumformungen |
| L6 viele bewegte Teilchen | 19 | 2 | Ladungsträger, Stichproben, Netzwerkpakete |
| L7 weitere Operationen | 15 | 4 | Integral als Prozess, Matrix·Vektor, Korrelation |
| L5 Gitter-Morph (lineare Abbildung) | 13 | 10 | ml 1/2, hm1 Heft 10 |
| L4 Kamera-Animation (3D) | 12 | 6 | gemb1 Orbitale/Gitter, ml 3, hm3 |
| L8 Code-Objekt mit Zeilenmarke und Speicher | 7 | 0 | Kern jeder Programmier-Reihe; heute Behelf mit Textzeilen + Rechteck |
| L-neu Faltung/Korrelation diskreter Folgen (Stem) | 4 | – | et3_a V12, et3_b (3×): eine gemeinsame Funktion |
| L-neu komplexe Zahlen im Rechenbild | ≈4 | – | komplexe Multiplikation (hm1 H2), komplexes Skalarprodukt (ml_2), Σ komplexer Terme als Zeigerkette (gemb1_b V15, et3_b V17) |
| L-neu Pfeilende umhängen | 1 | – | Name → anderes Objekt bei Zuweisung (prog_a V37); zentral für prog |
| L-neu Einzelfälle | je 1 | – | Binomialkoeffizient im Σ-Term (hm3_c V16), Höhenlinie auf 3D-Fläche (ml_3 V5), Riemann links/rechts (hm3_a V15) |

## 5. Was zusammengehört (nichts doppelt bauen)
- **Gauß Zeile für Zeile:** hm1_b V30 und ml_1 V14 bekommen eine gemeinsame Vorlage. Dasselbe gilt für Matrix·Vektor,
  Matrixprodukt und Inverse (hm1_b ↔ ml_1 k1rmv, k1rprodukt, k1gauss, k1inverse).
- **Gradient, Richtungsableitung, Jacobi, Kettenregel:** hm3_a ↔ ml_3 (ml/k3*). Die Szenen sind eigenständig, aber
  nach einer Konstruktionsvorlage gebaut. Dazu passt die Vorlage „Pfeil dreht sich, Punkt läuft auf Kurve“: ml_3 V7,
  V11, V16, hm1_b V14 und et3_b V2.
- **Wahrscheinlichkeit:**
  - ml_4 ↔ hm3_c (k8wuerfel, k8mosaik, k8schwerpunkt, k8poisson, k8dichte, k8tscheb, k8mittel, k8zgs).
  - et3 Heft 7 verweist auf hm3 Heft 8.
- **Fourier:**
  - hm3_c V8 mit et3/k3kosinus abstimmen.
  - hm3_c V10 ergänzt et3/k3gibbs.
- **Weitere Wiederverwendungen:**
  - Euler: hm1/k7euler (für prog_a und et3_a V15).
  - Bisektion/Zwischenwertsatz: prog_b V20 nutzt hm1/k5nullstelle. Das Bild vorher teilen, es enthält drei Gedanken
    (hm1_a).
  - Drude: gemb1/k1drude erscheint auch in Heft 12.

## 6. Nebenbefunde für den Bau
- **„Abb. n“-Verweise:** Neue oder zusammengelegte Bilder verschieben Nummern. Betroffen sind:
  - et1 Heft 10 Artikel 05–07 (Abb. 6) und 10 Artikel in et1_c
  - ml_1 Artikel 13 (Abb. 30 → V7)
  - hm1_a V5 (Abb. 5)
  - hm3_a Abschnitt 1.15 (Abb. 5)
- **Vorgriffe und Ort:**
  - ml_2 Artikel 10, Abschnitt 9.1, verweist auf Abb. 23, bevor v, u, D eingeführt sind (V12 behebt das).
  - hm3/k2riemann steht im zugeklappten Hintergrund, obwohl „Säulensumme“ im Haupttext 3.4 eingeführt wird.
- **Teilen:** k12beweglichkeit (gemb1, vier Teilbilder) und hm1/k5nullstelle (drei Gedanken) vor dem Animieren in
  zwei bzw. drei Szenen teilen.

## 7. Empfohlene Reihenfolge zum Nachrüsten
1. **Technik zuerst:**
   - Abspielknopf im Artikel (L10).
   - L1 und L2 freischalten: FadeOut, Transform, ReplacementTransform und TransformMatchingTex sind in der Engine,
     fehlen aber in `ANIMATION_TYPES` (`scene_model.py`) und im Editor-Menü, dazu je ein Fall in `tests/test_contract.py`.
   - L9 (Indicate auf eine Tabellenzeile oder -zelle).
   - Diese drei sind voraussichtlich klein und machen rund 70 Vorschläge sauber.
2. **Regelverstöße beheben, ohne neue Funktion:**
   - 85 statische Rechenbilder auf Σ, ∏ und Skalarprodukt umbauen (ml, cyber, prog).
   - Die mindestens 30 fehlenden Pflicht-Rechenbilder anlegen.
   - Die 214 Artikel ohne Bild versorgen, zuerst mit den etwa 65 Wiederverwendungen (geringer Aufwand).
3. **Top 30 aus Abschnitt 3:** 15 davon sind heute machbar, sie zuerst.
4. **Vorhandene Abbildungen mit Zeitachse versehen**, Heft für Heft entlang der Schrittlisten in den Paketdateien.
   Reihenfolge:
   1. et3 (Pilot, Faltungs-Operation vorhanden)
   2. ml und prog (aktive Reihen, größte Lücke)
   3. hm1, hm3
   4. et1, gemb1
   5. cyber
5. **L3 Parameter über die Zeit bauen** (Parameter als ValueTracker, abhängige Objekte über Updater neu rechnen, im
   Einklang mit `ENGINE_CONTRACT.md`). Danach die 63 L3-Vorschläge und 84 vorhandene Szenen nachziehen. Das ist der
   größte Einzelgewinn für gemb1, et1 und et3.
6. **Danach** L6, L5, L4, L7 und L8. L8 vor dem nächsten Programmier-Heft. Dann die L-neu-Funktionen, zuerst diskrete
   Faltung und komplexe Rechenbilder.
7. **Zuletzt** die übrigen B- und C-Vorschläge.

Bauen wie bei den Heften: höchstens ein Schreib-Agent zur Zeit, Heft für Heft. Szenen in `tools/szenen/<modul>_teil<N>.py`,
Namen wie vorgeschlagen.
