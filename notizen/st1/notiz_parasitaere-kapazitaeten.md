# Arbeitsnotiz: Parasitäre Kapazitäten des MOSFET (ST1, MOS-Feldeffekttransistoren, Thema 4)

Dateien: `content/st1/03-mos-feldeffekttransistoren/04-parasitaere-kapazitaeten.md` (kompakt) und `…-ausfuehrlich.md`.
Frontmatter aus dem Themenplan: title „Parasitäre Kapazitäten des MOSFET“, pfad „Elektrotechnik / 3. Semester /
Schaltungstechnik 1 / MOS-Feldeffekttransistoren“, order 33030400, tags „MOS-Kapazität, Gate-Kapazität,
Überlappkapazität, Sperrschichtkapazität“. Quelle: PDF S. 81–86 (Abschnitt 3.9), Volltext `st1_clean.txt` Zeilen
6677–7047. Zahlen: `zahlen_mosfet.py` Abschnitte W bis AD (Beispiel-Transistorpaar aus Thema 1).

## 1. Ein-Satz-Prinzip

Eine Kapazität im MOSFET ist die Ladung, die ein Anschluss je Volt Spannungsänderung liefern muss; ihr Wert hängt davon
ab, wo die Gegenladung sitzt und aus welchem Anschluss sie nachfließt, und ihre Wirkung davon, um wie viel sich die
Spannung über ihr tatsächlich ändert.

## 2. Schwierigkeit und Längenspannen

**schwer**: mehrere Mechanismen (Gateladung und ihre Gegenladung je Betriebsbereich, Aufteilung der Kanalladung auf
Source und Drain, Sperrschichten von Source und Drain mit Geometrie, Leitungen, Miller-Effekt), zwei Kipp-Stellen. Jeder
Teil ist für sich mittelschwer. Spannen: kompakt 1800–4000, ausführlich 3500–7000 Wörter; erwartet im unteren Drittel.

## 3. Vorwissen-Kette

- Kondensator, Plattenkondensator, Reihenschaltung von Kondensatoren, Zeitkonstante RC: ET1 (Kondensator und
  Kapazität, Kondensatorschaltungen, Laden und Entladen), erinnern und verlinken.
- MOS-Kondensator: C'_ox = 6,91 fF/µm², C_ox = 69,06 fF, Zustände Anreicherung/Verarmung/Inversion, Flachband −1,027 V,
  Schwelle 0,5 V, C(U) niederfrequent/hochfrequent mit Reihenschaltung Oxid–Verarmungszone (0,30 C'_ox bei 0 V,
  0,247 an der Schwelle), Inversionsschicht ohne Source nur durch Wärme (rund 90 s): Thema 1, erinnern und verlinken.
- Kennlinien: Kanal als Keil, örtliche Ladung C'_ox (U_GS − U_th − U(x)), Abschnürung, Profil √(1 − x/L) an der
  Abschnürgrenze, Laufzeit 92 ps: Thema 2, erinnern und verlinken.
- Substrateffekt (η = 0,327) und Sourcefolger (Steigung 0,80): Thema 3, nur ausführlich (Vertiefung, Beispiel).
- Sperrschichtkapazität C_j = εA/w(U) = C_j0/√(1 − U/U_Diff): ET1 Diode und Kennlinie (Abschnitt Kapazitätsdiode,
  dort hergeleitet), erinnern und verlinken; m = 1/3 für lineare Dotierung hier aufbauen (ausführlich).
- Kleinsignalverstärkung der Source-Schaltung (g_m = 1 mS, g_o = 25 µS, A_V = −g_m/(G_D + g_o)): Netzwerkanalyse
  (Arbeitspunkt und Linearisierung; Vierpole mit erstem Auftreten des Miller-Effekts), erinnern und verlinken.
- Zweistufiger Verstärker (nur Miller-Kompensation, ausführlich): hier in einem Satz aufbauen.
- Modul-Test: GEMB1 und ET1 behandeln keine Transistorkapazitäten; der Vierpol-Artikel nennt den Miller-Effekt nur mit
  angenommenen Werten. Dieser Artikel ist die vollständige Behandlung.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Der MOSFET nimmt am Gate keinen Strom auf, wieso braucht man dann Strom zum Umschalten?“ → Worum es geht und
   Abschnitt Kapazität zwischen Anschlüssen, Text, beide.
2. „Was heißt Kapazität zwischen Gate und Source, wenn die Gegenladung im Kanal sitzt?“ → Text (Definition über die
   Anschlüsse), beide.
3. Fehlvorstellung: „Die Gatekapazität ist immer C_ox.“ → Fehlvorstellungs-Kasten (gesperrt bei 0 V nur 0,30 C_ox,
   Sättigung 2/3), beide.
4. „Warum sinkt die Kapazität beim Transistor in der Inversion nicht ab wie beim MOS-Kondensator bei hoher Frequenz?“ →
   Text (Source und Drain liefern die Elektronen, R_on C_ox = 69 ps), beide.
5. „Warum verschwindet C_GB, sobald es einen Kanal gibt?“ → Text (Abschirmung, 98 % aus Source und Drain bei 1 V),
   beide.
6. „Warum ist C_GS in Sättigung zwei Drittel und nicht die ganze Oxidkapazität?“ → Kipp-Stelle K1, Text, beide.
7. „Warum hat der Drain in Sättigung keinen Einfluss auf die Gateladung?“ → K1, Text, beide.
8. Fehlvorstellung: „In Sättigung ist C_GD null, also kann man die Gate-Drain-Kapazität vergessen.“ →
   Fehlvorstellungs-Kasten im Miller-Abschnitt (3,45 fF wirken als 31 bzw. 142 fF), beide.
9. „Warum überlappt das Gate Source und Drain überhaupt?“ → Frage-Kasten, beide.
10. „Hat die Kapazität der Diffusionsgebiete etwas mit der Diffusionskapazität der Diode zu tun?“ → Satz im Text,
    ausführlich (kompakt: Begriff vermieden).
11. „Warum zählt der Rand eigens, die Fläche ist doch viel größer?“ → Text und Beispiel (19 % → 49 %), beide.
12. „Warum wird die Sperrschichtkapazität mit der Spannung kleiner?“ → So liest man das, beide.
13. Fehlvorstellung: „Ein gesperrter pn-Übergang isoliert, seine Kapazität ist klein gegen das Gate.“ →
    Fehlvorstellungs-Kasten (C_DB 37,8 fF gegen C_GS 49,5 fF), ausführlich; kompakt im Text.
14. „Wie kann eine Kapazität von 3,45 fF am Eingang wie 31 fF wirken, die Ladung entsteht doch nicht aus dem Nichts?“ →
    Kipp-Stelle K2, Text, beide.
15. „Gilt die Rechnung auch beim Sourcefolger?“ → Frage-Kasten, ausführlich (C_GS wirkt nur zu 20 %).
16. „Warum baut man absichtlich eine Kapazität zwischen Ein- und Ausgang?“ → Abschnitt Miller-Kompensation,
    ausführlich; kompakt ein Satz.
17. „Bis zu welcher Frequenz gelten diese Werte?“ → Vertiefung, ausführlich.

## 5. Kipp-Stellen

**K1: Aufteilung der Kanalladung auf Source und Drain.** Schritte: (1) Die Gateladung über dem Kanal hat ihre
Gegenladung in den Kanalelektronen; jedes zusätzliche Elektron kommt aus Source oder Drain. (2) Die örtliche Ladung ist
C'_ox mal (Gate-Kanal-Spannung minus U_th); eine Anschlussspannung ändert sie nur dort, wo das Kanalpotential ihr folgt.
(3) Ohmscher Bereich mit kleiner U_DS: Hebt man die Source um ΔU, sinkt die Ladung an der Source um C'_ox ΔU, am Drain
gar nicht, dazwischen linear → Mittel 1/2 → C_GS = C_ox/2, ebenso C_GD. (4) Sättigung: Am abgeschnürten Ende erreicht
das Drainpotential den Kanal nicht → C_GD = 0. (5) Das Profil ist √(1 − x/L); die Übersteuerung skaliert es → Mittel
2/3 → C_GS = 2C_ox/3. (6) Dazwischen stetiger Übergang (Meyer). Tragende Zahlen: Source 10 mV höher → 0,460 fC =
2874 Elektronen (Sättigung) bzw. 0,345 fC (ohmsch); 46,0 / 34,5 fF; Zwischenpunkt 1,5 V/0,5 V 40,9/25,6 fF.
Abbildungen 04-kanalladung-aufteilung, 04-cgs-cgd-uds. Herleitung: Kanalladung, Grenzwerte; ausführlich allgemeine
Formel. Beispiel: Kapazitäten des Beispieltransistors.

**K2: Miller-Effekt.** Schritte: (1) C_GD verbindet Eingang und invertierten Ausgang. (2) Gate +10 mV → Drain −80 mV
(A_V = −8). (3) Spannung an C_GD ändert sich um 90 mV. (4) Die Quelle liefert 3,45 fF · 90 mV = 0,311 fC, so viel wie
31,1 fF bei 10 mV. (5) Eingang sieht C_GD(1 − A_V), Ausgang C_GD(A_V − 1)/A_V. (6) C_ein 80,6 statt 52,9 fF; mit
A_V = −40 191 fF, Miller-Anteil 2,86-mal C_GS. Abbildung 04-miller. Herleitung: Miller-Formeln. Beispiel:
Eingangskapazität und Zeitkonstante.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Kapazität als Ladung pro Spannung, nichtlineares Bauelement: Kleinsignal-Kapazität dQ/dU | K | Text | Text |
| Kapazität zwischen zwei Anschlüssen über die Gateladung, C_G = C_GS + C_GD + C_GB | K | Definition, Text | Definition, Herleitung der Summe |
| sieben Kapazitäten im Überblick (Tabelle mit Ladung, Gegenladung, Spannungsabhängigkeit) | K | Tabelle | Tabelle |
| MOS-Kondensator C(U) (Anreicherung, Verarmung, Inversion, NF/HF) | K, aber Thema 1 | 2–3 Sätze, Link | 1 Absatz, Link, Reihenschaltung als Formel mit Kasten |
| Transistor folgt der niederfrequenten Kurve, weil Source und Drain liefern (R_on C_ox 69 ps) | K | Text | Text, Zahl |
| gesperrt: C_GB < C_ox (0,30 C_ox bei 0 V), C_ox nur in Anreicherung (unter −1,03 V) | K | Text, Beispiel | Text, Beispiel |
| an der Schwelle je Hälfte Bulk/Kanal, darüber Abschirmung (98 % bei 1 V) | H | Satz | Text, Zahl |
| Aufteilung 1/2, 2/3, 0 (K1) | K | Formel, Herleitung, Beispiel | Formel, Herleitung, Beispiel |
| allgemeine Formel (Meyer) | V | – | Formel, Herleitung, Beispiel-Teil |
| Tabelle der drei Bereiche mit Zahlen | K | Tabelle | Tabelle |
| Überlappung: selbstjustiertes Gate, L_ov 50 nm, C_ov 3,45 fF, Randfeld | K | Text, Formel kurz | Abschnitt, Abbildung |
| Kanal-Bulk-Kapazität unter dem Kanal (22,6 fF, Aufteilung) | V | – | Frage-Kasten |
| genauere Rechnung: C_GB 0,08 C_ox in Sättigung, C_GS 0,60 bei 1 V, Gültigkeit bis GHz | V | – | Vertiefung |
| Sperrschichtkapazität Source/Drain: Formel C_j0(1 − U_j/U_Diff)^−m | K | Formel, Herleitung | Formel, Herleitung mit m = 1/3 |
| Fläche plus Rand, C'_jS = C'_jF x_j, A_D, P_D (Simulatorangaben AD, PD) | K | Formel, Beispiel | Formel, Beispiel, Abbildung |
| Verkleinerung: Randanteil 19 % → 49 % | H | Beispiel-Teil | Beispiel-Teil |
| Finger-Layout mit gemeinsamem Drain (−48 %) | V | – | Beispiel-Teil, Abbildung |
| Begriff „Diffusionskapazität“ der Vorlage ≠ Diffusionskapazität der Diode | H | Begriff vermieden | Satz |
| Verdrahtung: Plattenkondensator, Randfelder Faktor 1,75–3,55, Kopplung paralleler Bahnen | H/V | 2–3 Sätze mit Zahl | Abschnitt, Formel (empirisch), Beispiel, Abbildung |
| Umladezeit als Folge (C ΔU/I, RC) | K | Satz mit Zahl | Text |
| Miller-Effekt (K2) | K | Formel, Herleitung, Beispiel | Formel, Herleitung, Beispiel |
| Miller-Ausgangsseite (A_V − 1)/A_V, C_DB am Ausgang | K | Formel, Satz | Formel, Text |
| Grenze der Miller-Rechnung (statische Verstärkung) | H | Satz | Text, Zahl 96 MHz |
| Sourcefolger: C_GS wirkt nur (1 − A_V)-fach | V | – | Frage-Kasten |
| Miller-Kompensation, Flächenersparnis | H/V | Satz | Abschnitt, Beispiel, Abbildung |
| Kleinsignal-Ersatzschaltbild mit Kapazitäten, Bahnwiderstände | S (Thema 5) | Ausblick | Ausblick |
| Frequenzgang, Pole, Bode | S (Transistorgrundschaltungen) | Ausblick | Ausblick |
| Messung der C(U)-Kurve | S (Thema 1) | – | – |

## 7. Abbildungsplan (Szene-IDs st1/mos-feldeffekttransistoren/04-…)

| ausf. | kompakt | Szene | Inhalt |
|---|---|---|---|
| 1 | 1 | 04-kapazitaeten-uebersicht | NMOS-Querschnitt mit allen Kapazitäten und Werten in Sättigung; daneben Schaltzeichen mit den fünf Anschlusskapazitäten |
| 2 | 2 | 04-gatekapazitaet | C/C_ox über U_GS bei U_DS = 0: gesamt, Bulkanteil, Kanalanteil je Seite; MOS-Kondensator HF gestrichelt |
| 3 | – | 04-ueberlappung | Gatekante mit 50 nm Überlappung, Randfeld |
| 4 | 3 | 04-kanalladung-aufteilung | Kanalladung und ihre Änderung über x/L, ohmsch und Sättigung, Source bzw. Drain angehoben |
| 5 | 4 | 04-cgs-cgd-uds | C_GS, C_GD, Summe über U_DS bei U_GS = 1,5 V (Meyer), mit Überlappung gestrichelt |
| 6 | 5 | 04-sperrschicht-geometrie | Draingebiet: Aufsicht 10 × 2 µm, Querschnitt 0,2 µm tief, Boden und Rand |
| 7 | – | 04-sperrschicht-spannung | C_DB über U_DB, Anteile, m = 1/3 zum Vergleich |
| 8 | – | 04-finger-layout | ein Finger gegen zwei Finger mit gemeinsamem Drain |
| 9 | – | 04-leitung-randfeld | Leiterbahn über Oxid mit Feldlinien, Platte gegen Randfeld |
| 10 | 6 | 04-miller | Source-Schaltung mit C_GS, C_GD, C_DB; Schritt +10/−80 mV; Miller-Ersatz |
| 11 | – | 04-miller-kompensation | zweistufiger Verstärker mit C_M über der zweiten Stufe |

Geprüft gegen §7.2: Einstieg, je Sach-Abschnitt mindestens eine, beide Kipp-Stellen mit Abfolge, jede Schaltung mit
Schaltbild, jede Formel mit Graph oder Bild (Sperrschichtformel 04-sperrschicht-spannung, Miller 04-miller).

## 8. Zahlenwerk

Abschnitte W bis AD in `zahlen_mosfet.py`. C_ox = 69,06 fF (½: 34,53, ⅔: 46,04 fF). Gatekapazität bei U_DS = 0
(exakt, Kanalanteil über −dQ_G/dV): C_GG/C_ox 0,964 (−2,5 V) / 0,734 (−1,027 V) / 0,300 (0 V) / Minimum 0,264 (0,35 V)
/ 0,396 (0,5 V, je zur Hälfte Bulk und Kanal: 0,198) / 0,922 (1 V, Kanal 0,907, Bulk 0,015, 98,3 %) / 0,978 (2,5 V);
MOS-Kondensator HF 0,239 bei 1 V. R_on C_ox 69 ps (1 V), 35 ps (1,5 V); Laufzeit 92 ps. Meyer: U_GS = 1,5 V:
0,500/0,500, 0,593/0,370 (0,5 V), 0,640/0,240 (0,75 V), 0,667/0 ab 1 V. Kanalladung 34,5 fC (ohmsch) / 23,0 fC
(Sättigung, 143 685 Elektronen) bei 1 V. Source +10 mV: 0,460 fC (2874 Elektronen) bzw. 0,345 fC. Überlappung 50 nm:
C_ov = 3,453 fF (0,05 C_ox, 0,345 fF/µm). Bereiche: gesperrt 0 V: C_GB 20,70 fF, Summe mit Überlappungen 27,61 fF;
−2 V: 65,36 fF; Sättigung 1 V/1 V: 49,49 / 3,45 / 0 fF, Summe 52,95 fF; ohmsch 2,5 V/0,1 V: 38,57 / 37,39 fF; U_DS = 0:
37,98 fF je Seite. Ladungsschichtmodell: n = 1,327, (n − 1)/(3n) = 0,082; Sättigung 1 V/1,5 V: C_GS 0,602, C_GB 0,083,
C_GG 0,685; 1,5 V/2,5 V: 0,637/0,068; Sättigung schon ab U_DS ≈ 0,8 V. Sperrschicht: U_Diff = 1,0274 V (= −Φ_MS),
w0 48,4 nm, C'_jF0 2,142 fF/µm², x_j 0,2 µm, C'_jS0 0,4285 fF/µm; Drain 10 × 2 µm: 20 µm², 24 µm; C_DB 53,13 / 43,57 /
37,82 / 33,87 / 30,95 / 28,67 fF bei 0 / 0,5 / 1 / 1,5 / 2 / 2,5 V (Fläche 42,85 → 23,12, Rand 10,28 → 5,55, Randanteil
19,4 %); m = 1/3: 0,797 statt 0,712 bei 1 V; Viertel: 2,68 + 2,57 fF, 49 %; zwei Finger 19,52 statt 37,82 fF (−48 %);
Kanal-Bulk 22,6 fF (⅔: 15,1; ½: 11,3). Verdrahtung: ε_ox 0,03453 fF/µm; 2 µm × 1 mm über 1 µm: Platte 69,06 fF,
Sakurai–Tamaru 162,3 fF (2,35); 1 µm: 122,6 (3,55); 4 µm: 241,7 (1,75); Seitenflächen zweier Bahnen 17,3 fF. Miller:
A_V = −8, C_ein = 49,49 + 31,08 = 80,57 fF (ohne 52,95), Ausgang 37,82 + 3,885 = 41,71 fF; τ_ein mit 10 kΩ 0,530 →
0,806 ns, τ_aus 0,334 ns; A_V = −40: 191,1 fF (Miller 141,6 = 2,86 C_GS), τ_aus 40 kΩ · 41,36 fF (Eckfrequenz 96 MHz
gegen 83 MHz am Eingang); Sourcefolger 0,8: 13,35 statt 52,95 fF; Umladen Drainknoten 41,7 fF mit 0,25 mA um 1 V:
0,167 ns. Kompensation: A_2 = −50, 1 pF → 51 pF; 1000 statt 51 000 µm² bei 1 fF/µm²; 3,12 kHz mit 1 MΩ.

## 9. Profi-Abgleich

- MIT 6.012, Lecture 10 „MOSFET in saturation, small-signal model, capacitances“:
  https://web.mit.edu/6.012/FALL00/www/handouts/lec10.pdf – Gatekapazität in Sättigung aus der Kanalladung
  Q_N = −(2/3) W L C_ox (V_GS − V_T), Ableitung nach V_GS; C_gd nur Überlappung.
- IIT Kanpur, Analog IC Design, Folien „MOSFET“: https://home.iitk.ac.in/~nallam/courses/AIC/2026/slides/MOSFET.pdf –
  Triode C_gs = C_gd = WLC_ox/2 + C_ov W, Sättigung C_gs = 2/3 WLC_ox + C_ov W, C_gd = C_ov W, gesperrt nur Überlappung.
- T. Sakurai, K. Tamaru, IEEE Trans. Electron Devices, Februar 1983: C/ε = 1,15 (W/H) + 2,80 (T/H)^0,222, Fehler unter
  6 % für 0,3 < W/H < 30 und 0,3 < T/H < 30 (zitiert u. a. in US-Patent 6774421).
- Linköping, TSEI03 Formelsammlung (typische Werte CJ ≈ 0,3–1 fF/µm², CJSW ≈ 0,2–0,3 fF/µm):
  https://www.isy.liu.se/edu/kurs/TSEI03/lektion/TSEI03-Formulary.pdf
- Eigene Herleitung (Ladungsmodell mit linear wachsender Verarmungsladung): C_GB = (n − 1)/(3n) C_ox in Sättigung,
  im Zahlenwerk mit dem Ladungsschichtmodell bestätigt (0,083 gegen 0,082).

## 10. Skript-Abgleich (PDF-Seiten)

**Inhalte:** S. 81 Einleitung (Speed hängt von parasitären Kapazitäten ab; Layoutoptimierung), 3.9.1 C(U) des
MOS-Kondensators mit Bild 3.18 (statisch f < 100 Hz, dynamisch), Gl. 3.19 C_ox = ε_ox A/t_ox (Anreicherung), Gl. 3.20
C_RLZ = ε_Si A/l_D; S. 82 Gl. 3.21 Reihenschaltung (Verarmung), Inversion NF/HF, 3.9.2 sieben Kapazitäten, C_ov
vernachlässigt, C_SB/C_DB nichtlinear, C_GS/C_GD je C_ox/2, C_GB mit RLZ in Reihe, Gl. 3.22 C_G = C_GS + C_GD + C_GB,
Fußnote C_DS vernachlässigt; S. 83 Bild 3.19, Gl. 3.23/3.24 C'_ox (7 nm), drei Bereiche: gesperrt (C_GS = C_GD = 0,
C_GB = C_ox bzw. Reihenschaltung), Triode (½ C'_ox WL, C_GB ≈ 0); S. 84 Bild 3.20, Sättigung (C_GD = 0, C_GB = 0,
C_GS = ⅔ C'_ox WL), genauere Analysen; 3.9.3 Diffusionsgebiete (Fläche und Seitenflächen, feinere Strukturen); S. 85
C'_jS, C'_jF, Gl. 3.25 C_j = C_j0(1 − U_j/Φ_Diff)^−m, m 0,3–0,5, C_Diff = C'_jF ab + 2C'_js(a + b), Kanalseite,
Bild 3.21, Verdrahtung als Plattenkondensator; S. 86 Randeffekte 1,5- bis 3-fach, parallele Leitungen, 3.9.4 Wirkung,
Bild 3.22 Miller, (1 − A) und (A − 1)/A, Miller-Kompensation mit C_M.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 81: Akkumulation „bei U_GB < 0“, Verarmung „bei geringer positiver Spannung“ – die Grenze ist die
   Flachbandspannung (beim n⁺-Gate −1,03 V); bei U_GB = 0 ist die Oberfläche schon verarmt.
2. S. 82: Austausch „über die Raumladungszone“ als Grund der HF-Kurve ungenau – ohne Source entstehen Elektronen nur durch
   thermische Generation (Thema 1); im Transistor liefern Source und Drain, deshalb gibt es dort keine HF-Kurve.
3. S. 82: Überlappungskapazitäten „so gering, dass sie entfallen sollen“ – in Sättigung sind sie die ganze
   Gate-Drain-Kapazität und über den Miller-Effekt maßgeblich; hier mitgeführt.
4. S. 83, Gl. 3.24: C'_ox = 3,9 ε0/7 nm = „3,9·10⁻³ pF/µm²“ – richtig 4,93·10⁻³ pF/µm² (eigenes Beispiel mit 5 nm).
5. S. 83: „im Trioden- sowie im Sättigungsgebiet … näherungsweise C_ox“ – in Sättigung ⅔ C_ox (widerspricht dem eigenen
   Bild 3.20).
6. S. 83: gesperrt „C_GS = C_GD = 0 und C_GB = C_ox bei U_GS ≪ U_th“ – C_GB = C_ox nur in der Anreicherung (unter
   U_FB); bei U_GS = 0 nur 0,30 C_ox; C_GS = C_GD = C_ov statt 0.
7. S. 84: „Es gilt weiterhin C_GB = 0“ in Sättigung – nur im einfachen Modell; genauer 0,08 C_ox (Vertiefung).
8. S. 84: „C_GS steigt in Sättigung leicht über 2/3 C_ox, C_GD sinkt nicht ganz auf 0“ ohne Mechanismus – Grund ist vor
   allem die Überlappung (und Randfelder); die Langkanalrechnung ergibt dicht über der Schwelle sogar etwas weniger
   als 2/3.
9. S. 85: „Diffusionskapazität C_Diff“ – Namensgleichheit mit der Diffusionskapazität der Diode in Durchlassrichtung;
   hier Sperrschichtkapazität der Source- und Draingebiete.
10. S. 85, Gl. 3.25: „U_j Sperrspannung … (neg.)“ unklar – U_j ist die Spannung am Übergang in Durchlassrichtung, in
    Sperrrichtung negativ; Φ_Diff → U_Diff (Bezeichnung wie in ET1); Symbol C'_jS/C'_js uneinheitlich.
11. S. 86, Bild 3.22: Ausgangselement Z_GD·A/(1 − A) – richtig Z_GD·A/(A − 1) (Text richtig: Kapazität (A − 1)/A).
12. S. 86: „drei dominante Kapazitäten C_GS, C_GD, C_DS“ – C_DS war vorher vernachlässigt; am Ausgang der
    Source-Schaltung wirkt die Drain-Bulk-Sperrschicht, die bei Source und Bulk an Masse zwischen Drain und Source liegt.
13. S. 86: Miller mit statischer Verstärkung ohne Gültigkeitsgrenze – gilt nur, solange die Verstärkung bei der
    betrachteten Frequenz noch etwa ihren Gleichstromwert hat.
14. Bild 3.19: C_GB ohne Pfeil (fest) gezeichnet, obwohl stark spannungsabhängig.
