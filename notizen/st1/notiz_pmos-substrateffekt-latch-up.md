# Arbeitsnotiz: PMOS-Transistor, Substrateffekt und Latch-Up (ST1, MOS-Feldeffekttransistoren, Thema 3)

Dateien: `content/st1/03-mos-feldeffekttransistoren/03-pmos-substrateffekt-latch-up.md` (kompakt) und `…-ausfuehrlich.md`.
Frontmatter aus dem Themenplan: title „PMOS-Transistor, Substrateffekt und Latch-Up“, pfad „Elektrotechnik / 3. Semester /
Schaltungstechnik 1 / MOS-Feldeffekttransistoren“, order 33030300, tags „PMOS, Substrateffekt, Body-Effekt, Latch-Up,
CMOS“. Quelle: PDF S. 79–80 (Abschnitte 3.7 und 3.8) und S. 87 (3.10), Volltext `st1_clean.txt` Zeilen 6527–6676 und
7048–7088. Zahlen: `zahlen_mosfet.py` Abschnitte S bis V (Beispiel-Transistorpaar aus Thema 1).

## 1. Ein-Satz-Prinzip

Ein MOSFET ist nur durch gesperrte pn-Übergänge von seiner Umgebung getrennt, und sein Bulk wirkt wie ein zweites Gate:
Beim PMOS sind Gebiete und Vorzeichen vertauscht, eine Sperrspannung zwischen Bulk und Source vergrößert die
Verarmungsladung und damit den Betrag der Schwelle, und werden die trennenden Übergänge leitend, bilden Wanne und Substrat einen
Thyristor, der die Versorgung kurzschließt.

## 2. Schwierigkeit und Längenspannen

**schwer**: drei getrennte Mechanismen (gespiegelter Transistor mit Vorzeichenkonventionen, Substrateffekt mit
Herleitung, parasitärer Thyristor mit Mitkopplung), zwei Kipp-Stellen. Spannen: kompakt 1800–4000, ausführlich
3500–7000 Wörter; erwartet eher am unteren Rand, weil jeder Teil für sich mittelschwer ist.

## 3. Vorwissen-Kette

- Aufbau von NMOS und PMOS, n-Wanne, Bulkregel, Inversdiode, Schwellenspannung als Spannungsbilanz
  (U_th0 = U_FB + 2Φ_F + |Q'_dep|/C'_ox), Verarmungsladung mit Wurzelgesetz, C'_dep: Thema 1, erinnern und verlinken.
- Kennlinien, Triodengleichung, Quadratgesetz, Kanallängenmodulation, Großsignalmodell, Sourcefolger-Grundidee
  (Arbeitspunkt mit Stromquelle): Thema 2, erinnern und verlinken.
- Bipolartransistor (npn/pnp, Stromverstärkung B bzw. β, Basis-Emitter-Einsatz um 0,6 V, Sättigung): ET1 Kap. 11,
  erinnern und verlinken.
- Thyristor: nicht vorausgesetzt, hier aufbauen (Vierschichtstruktur, Mitkopplung, Haltestrom).
- Mitkopplung/Schleifenverstärkung: ET1-OPV-Artikel (Rückkopplung) erwähnen, hier am konkreten Fall erklären.
- Modul-Test: GEMB1 „Der MOSFET“ behandelt weder PMOS-Konventionen noch Substrateffekt noch Latch-Up; dieser Artikel
  ist tiefer.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Warum sind beim PMOS alle Spannungen und der Strom negativ?“ → Text PMOS-Abschnitt, beide.
2. „Warum braucht der PMOS die vierfache Weite?“ → Frage-Kasten, beide (H: Löcherbeweglichkeit).
3. Fehlvorstellung: „Beim PMOS setze ich die negativen Spannungen in die NMOS-Gleichung ein.“ → Fehlvorstellungs-Kasten,
   beide (2,25 mA statt 0,25 mA).
4. „Warum hebt eine Spannung zwischen Bulk und Source die Schwelle, obwohl der Bulk nicht am Kanal liegt?“ → Kipp-Stelle
   K1, Text, beide.
5. „Warum wächst die Verschiebung nur mit der Wurzel?“ → So liest man das, beide.
6. Fehlvorstellung: „Die Schwellenspannung ist eine feste Eigenschaft des Transistors.“ → Fehlvorstellungs-Kasten,
   ausführlich; kompakt im Text.
7. „Was passiert, wenn der Bulk über der Source liegt?“ → Frage-Kasten, ausführlich.
8. „Warum haben Einzeltransistoren keinen Substrateffekt?“ → Text, beide.
9. „Kann man NMOS-Transistoren nicht in eigene Wannen setzen?“ → Frage-Kasten, ausführlich (Triple-Well).
10. „Warum folgt der Ausgang eines Sourcefolgers nicht eins zu eins?“ → Beispiel, beide.
11. Fehlvorstellung: „Latch-Up ist ein Durchbruch im Transistor; ist die Störung vorbei, verschwindet der Kurzschluss.“ →
    Fehlvorstellungs-Kasten, beide.
12. „Warum zündet der Thyristor nicht im Normalbetrieb?“ → Frage-Kasten, beide.
13. „Wie wird Latch-Up geprüft und verhindert?“ → Abschnitt Gegenmaßnahmen, beide (Prüfnorm nur ausführlich).
14. „Warum steigt die Gefahr mit der Temperatur?“ → Frage-Kasten, ausführlich.
15. „Gibt es Latch-Up auch ohne gemeinsames Substrat (SOI)?“ → Satz in den Gegenmaßnahmen, ausführlich.

## 5. Kipp-Stellen

**K1: Substrateffekt.** Schritte: (1) Inversion heißt: Elektronendichte an der Oberfläche gleich der Dotierung, gemessen
gegen das Potential, auf dem die Elektronen liegen, das ist das der Source (Kanal mit Source verbunden); (2) liegt die
Source um U_SB über dem Bulk, muss die Oberfläche um 2Φ_F + U_SB über das Innere gehoben werden; (3) dafür ist die
Verarmungszone breiter und enthält mehr feste Ladung (Wurzel); (4) diese Ladung muss das Gate zusätzlich tragen, die
Oxidspannung wächst; (5) gegen die Source gemessen steigt die Schwelle um γ(√(2Φ_F + U_SB) − √(2Φ_F)). Tragende Zahlen:
U_SB = 1 V: 45,8 → 66,2 nm, 4,17 → 6,02 fC/µm², ΔU_th = 0,268 V, U_th = 0,768 V. Zweite Sichtweise: Bulk als zweites
Gate mit η = C'_dep/C'_ox = 0,327 bei 0 V. Abbildungen 03-substrateffekt-querschnitt, 03-schwelle-ubs. Herleitung:
Schwellenspannung mit U_SB. Beispiel: Schwellen über U_SB, Sourcefolger.

**K2: Latch-Up.** Schritte: (1) CMOS enthält die Schichtfolge p⁺(PMOS-Source)–n-Wanne–p-Substrat–n⁺(NMOS-Source):
vertikaler pnp und lateraler npn, Basis des einen = Kollektor des anderen, dazu Wannen- und Substratwiderstand;
(2) ein Störstrom ins Substrat erzeugt an R_sub eine Spannung; ab etwa 0,6 V leitet der npn; (3) sein Kollektorstrom
fließt aus der Wanne durch R_well und lässt die Wanne am PMOS absinken; ab 0,6 V leitet der pnp; (4) dessen
Kollektorstrom fließt ins Substrat und verstärkt Schritt 2: Mitkopplung; (5) ist β_npn β_pnp > 1, wachsen die Ströme bis
zur Begrenzung durch die Versorgung, die Spannung über dem Pfad fällt auf rund 0,8 V; (6) der Zustand hält sich selbst,
auch wenn der Auslöser weg ist, bis die Versorgung abgeschaltet wird. Tragende Zahlen (angenommene Werte): R_sub 1 kΩ →
0,6 mA Zündstrom; β 5 und 50 → Schleifenverstärkung 250; Haltestrom rund 1 mA; mit 1 Ω Quelle 1,7 A und 1,4 W.
Abbildungen 03-latchup-struktur, 03-latchup-kennlinie. Herleitung: Zündbedingung. Beispiel: Zündstrom, Haltestrom.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| PMOS: Löcher, n-Wanne, Source oben, negative Spannungen und Ströme (Zählpfeile wie beim NMOS) | K | Abschnitt | Abschnitt |
| PMOS-Gleichungen in Vorzeichenform, λ als Betrag mit (1 − λU_DS), Bereichsbedingungen umgekehrt | K | Formel, Herleitung | Formel, Herleitung |
| Betragsform (U_SG, U_SD, I_SD), Gleichwertigkeit an Zahlen | K | Text, Beispiel | Text, Beispiel |
| µ_p = 72 gegen µ_n = 290, W_p = 4 W_n für gleiches K | H | Frage-Kasten | Frage-Kasten |
| PMOS-Großsignal-Ersatzschaltbild | K | Abbildung | Abbildung |
| PMOS als Schalter zur Versorgung (250 Ω) | V | Beispiel-Teil | Beispiel-Teil |
| Fehler: negative Spannungen in NMOS-Gleichung | K | Fehlvorstellung | Fehlvorstellung |
| Substrateffekt, Formel, γ, Herleitung aus der Spannungsbilanz | K | Kipp-Stelle | Kipp-Stelle |
| vollständige Rechnung bestätigt die Formel (Ausgleich der Randterme) | V | – | Satz im Beispiel |
| Bulk als zweites Gate, η = C'_dep/C'_ox | H | ein Satz | Formel, Herleitung |
| Bulk über Source (Vorwärts-Bias): Schwelle sinkt, Diode | H | – | Frage-Kasten |
| γ bestimmen aus zwei Schwellen | V | – | Beispiel-Teil |
| γ hängt von der Dotierung ab (0,08/0,26/0,63 √V) | H | – | So liest man das |
| PMOS-Substrateffekt (γ_p = 0,615 √V) | K | Text, Zahl | Text, Beispiel |
| Wo tritt er auf (NMOS im gemeinsamen Substrat, Sourcefolger), Einzeltransistor (Bulk an Source, Inversdiode) | K | Abschnitt | Abschnitt |
| Sourcefolger NMOS mit/ohne Substrateffekt, PMOS in eigener/gemeinsamer Wanne | K | Beispiel | Beispiel, Abbildung, Steigung 1/(1+η) |
| eigene Wanne kostet Fläche; Triple-Well für NMOS | H/V | Satz | Frage-Kasten, Abbildung |
| Latch-Up-Struktur, parasitäre Transistoren, R_sub, R_well | K | Kipp-Stelle | Kipp-Stelle |
| Zündbedingung β_npn β_pnp > 1 | K | Formel, Herleitung | Formel, Herleitung |
| Haltestrom, Haltespannung, Zerstörung durch Strom | H | ein Satz | Beispiel, Abbildung |
| Auslöser: Einschalten (Ladestrom der Wanne), Überspannung an Ein-/Ausgängen, ESD, Strahlung | K | Text | Text, Zahl |
| Gegenmaßnahmen: Abstand, Kontakte, Schutzringe, Epitaxie, SOI | K | Text | Abschnitt, Abbildung |
| Prüfnorm JESD78 (100 mA, 1,5-fache Spannung) | V | – | Text, Zahl 6 Ω |
| Temperatur | V | – | Frage-Kasten |
| Geschichte (erste CMOS-Schaltungen) | V | – | Satz |
| Kleinsignal-Substratsteilheit g_mB | S (Thema 5) | – | Ausblick |

## 7. Abbildungsplan (Szene-IDs st1/mos-feldeffekttransistoren/03-…)

| ausf. | kompakt | Szene | Inhalt |
|---|---|---|---|
| 1 | 1 | 03-cmos-ueberblick | CMOS-Querschnitt, alle Übergänge als Dioden; PMOS gespiegelt, angehobene NMOS-Source mit breiterer Zone, pnpn-Pfad |
| 2 | 2 | 03-pmos-kennlinien | Schaltzeichen mit Zählpfeilen und Ersatzschaltbild; Kennlinien im dritten Quadranten; Betragsdarstellung |
| 3 | 3 | 03-substrateffekt-querschnitt | NMOS an der Schwelle bei U_SB = 0 und 1 V: 45,8/66,2 nm, 4,17/6,02 fC/µm² |
| 4 | 4 | 03-schwelle-ubs | U_th über U_SB (NMOS) und |U_thp| über U_BS (PMOS), Tangente η, Bereich Bulk über Source |
| 5 | 5 | 03-sourcefolger | NMOS- und PMOS-Folger, Übertragungskennlinien mit und ohne Substrateffekt |
| 6 | – | 03-wannen-varianten | gemeinsame und eigene Wannen, Triple-Well |
| 7 | 6 | 03-latchup-struktur | Querschnitt mit npn, pnp, R_sub, R_well; Ersatzschaltbild; Schichtfolge |
| 8 | – | 03-latchup-kennlinie | Kennlinie des Pfads mit Zündpunkt, Haltepunkt, Arbeitsgerade der Versorgung (schematisch) |
| 9 | – | 03-latchup-gegenmassnahmen | Kontakte, Schutzringe, Epitaxieschicht, Abstand |

## 8. Zahlenwerk

Abschnitte S bis V in `zahlen_mosfet.py`: µ_p = 72,4 cm²/(V s), Verhältnis 4; PMOS −0,2163 mA (−1 V/−0,3 V), −0,30 mA
(−1 V/−2 V), Kennlinien −0,078/−0,3125/−0,703/−1,25 mA bei −2,5 V; Fehlrechnung 2,25 mA; Schalter 250 Ω (1 kΩ mit
W = 10 µm). Substrateffekt NMOS: γ_n = 0,629 √V, U_th = 0,500/0,646/0,768/0,875/0,971/1,059 V bei U_SB = 0…2,5 V,
vollständige Rechnung identisch; x_d 45,8/66,2 nm, |Q'_dep| 4,17/6,02 fC/µm², η 0,327/0,227; Bulk über Source: 0,431/
0,392/0,351 V; γ aus zwei Schwellen 0,629; γ bei 1e16/1e17 cm⁻³: 0,083/0,264 √V. PMOS: γ_p = 0,615 √V, 2Φ_F,n = 0,921 V,
|U_thp| = 0,500/0,643/0,762/0,867/0,961/1,048 V. Sourcefolger (0,25 mA, Übersteuerung 0,5 V): NMOS U_aus 0,385/0,783/
1,190 V bei 1,5/2/2,5 V (ohne Substrateffekt 0,5/1,0/1,5 V), Steigung 0,78–0,82, Differenzenquotient 0,796; PMOS
eigene Wanne U_ein + 1 V, gemeinsame Wanne 1,305/1,714 V bei 0/0,5 V. Latch-Up (angenommen R_sub 1 kΩ, R_well 2 kΩ,
0,6 V, β 5 und 50): ein Übergang leitet ab 0,6/0,3 mA, Zünden ab 0,66/0,312 mA, Schleife 250, Haltestrom 0,98 mA, Spannung 0,8 V, 1,7 A/1,4 W bei 1 Ω;
Gegenmaßnahmen β_npn = 0,01 → 0,5; 6 Ω für 100 mA; Einschalten: 1,73 nC für 10 mm² Wannenfläche, 1,7 mA bei 1 µs,
0,17 A bei 10 ns.

## 9. Profi-Abgleich

- Texas Instruments, White Paper SCAA124 „Latch-Up“ (2015): https://www.ti.com/lit/pdf/scaa124 – vertikaler pnp (p⁺
  Source/Drain, n-Wanne, Substrat) und lateraler npn (n⁺, Substrat, Wanne), Mitkopplung, nur Abschalten der Versorgung
  beendet den Zustand; Gegenmaßnahmen Abstände, Schutzringe, Substrat- und Wannenkontakte, Epitaxieschicht auf hoch
  dotiertem Substrat; JESD78: Strompulse typisch 100 mA, Überspannung 1,5 × V_max, Pulsdauer 2–10 ms; Temperatur erhöht
  die Widerstände.
- D. Johns, University of Toronto, ECE331 „Body Effect“: https://www.eecg.utoronto.ca/~johns/ece331/lecture_notes/07b_bodyEffect.pdf –
  V_t = V_t0 + γ(√(2Φ_F + V_SB) − √(2Φ_F)), γ = √(2qN_Aε)/C_ox, Sourcefolger-Verstärkung sinkt; Utah State
  (Small-Signal Analysis): g_mb = η g_m mit η = γ/(2√(2φ + V_SB)).

## 10. Skript-Abgleich (PDF-Seiten)

**Inhalte:** S. 79 PMOS: Source oben, U_GS, U_DS, I_D negativ, λ und U_th negativ angegeben, Ungleichungen umgekehrt,
Gleichungen (3.17), Hinweis Betragsform; Bild 3.15 Großsignal-ESB des PMOS. S. 79 Substrateffekt (3.18) mit U_inv und γ,
gemeinsames Substrat, Einzeltransistor mit Bulk an Source im Gehäuse, Sourcefolger Bild 3.16 (NMOS T2 mit T1, PMOS T3
mit T4, U_aus = −U_BS,T2 bzw. U_B − U_BS,T3). S. 80 eigene n-Wanne für PMOS ohne Substrateffekt, Flächenaufwand,
Querschnitte Bild 3.17, Fußnote zu isolierten Gebieten. S. 87 Latch-Up: parasitärer Thyristor, npn und pnp, R_p und R_n,
Zünden über Spannungsabfall bis zur Einsatzspannung, Selbsthaltung, Zerstörung; Auslöser Einschalten und Spitzen;
Design Rules mit großen Abständen.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 79 (3.18): γ mit C_ox statt der flächenbezogenen C'_ox.
2. S. 79: „U_th vergrößert sich dem Betrage nach“ ohne Bedingung – gilt für U_BS in Sperrrichtung (NMOS U_BS < 0, PMOS
   U_BS > 0); in Durchlassrichtung sinkt die Schwelle. U_inv nicht erklärt (= 2Φ_F).
3. S. 79: „alle MOSFETs nutzen ein gemeinsames Substrat“ – nur die NMOS; PMOS sitzen in Wannen, die getrennt werden können.
4. S. 79: λ und U_th des PMOS „negativ“ – λ ist eine Konvention; hier λ als Betrag mit (1 − λU_DS), der Hinweis auf die
   andere Konvention ohne Quelle.
5. S. 80, Bild 3.17: Beschriftung „U_ref,in“ statt U_ref,n; Unterschrift „Unteres Bild: Substrateffekt T2“ passt nicht zum
   unteren Bild (PMOS in eigenen Wannen, kein Substrateffekt bei T3).
6. S. 80, Fußnote: „Freistellen eines n-dotierten Bereiches“ – für NMOS wird eine p-Wanne in einer tiefen n-Wanne isoliert
   (Triple-Well).
7. S. 87: „Der Emitterstrom muss über den jeweils anderen Widerstand abfließen“ – es ist der Kollektorstrom des einen
   Transistors, der durch den Basiswiderstand des anderen fließt.
8. S. 87: „kann nicht mehr abgestellt werden“ – nur durch Abschalten der Versorgung bzw. Unterschreiten des Haltestroms.
9. S. 87: „durch die Design Rules ein Latch-Up verhindert … nicht möglich“ – Abstände allein genügen nicht; Kontakte,
   Schutzringe und Epitaxie senken Widerstände und Stromverstärkungen; bei Strominjektion an Anschlüssen bleibt ein Risiko,
   das geprüft wird (JESD78).
