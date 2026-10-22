# Arbeitsnotiz: Der Operationsverstärker – idealer OPV und Rückkopplung (ET1 Kap. 12.1–12.4 und Anfang von 12.5), Stil 3

Skript S. 195–203 (PDF 201–209): Rauschen (12.1), Differenzverstärker (12.2, Bild 12.1), idealer OPV, Komparator und
Flash-Wandler (12.3, Bilder 12.2–12.5), Rückkopplung und invertierender Schmitt-Trigger (12.4, Bild 12.6). Der Mechanismus der
Gegenkopplung steht im Skript am Anfang von 12.5 (S. 202–203, an Bild 12.7); er gehört zum Thema „Rückkopplung“ und wird hier erklärt.
Die Grundschaltungen selbst (invertierender und nichtinvertierender Verstärker, Folger, Addierer, Subtrahierer, Integrator) folgen in 12/02,
der reale OPV (Bandbreite, Slew-Rate, Offset, Gleichtaktunterdrückung) in 12/03.

## 1. Ein-Satz-Prinzip

Ein Operationsverstärker verstärkt nur die Differenz seiner beiden Eingangsspannungen, und das so stark, dass er allein nur „größer“ oder
„kleiner“ melden kann; erst die Rückführung der Ausgangsspannung macht ihn brauchbar: Wirkt sie der Differenz entgegen (Gegenkopplung),
regelt der Ausgang die Differenz praktisch auf null und die äußeren Widerstände bestimmen das Ergebnis, verstärkt sie die Differenz
(Mitkopplung), kippt der Ausgang an eine Grenze und bleibt dort.

## 2. Schwierigkeit und Längenspannen

Schwer: vier zusammenwirkende Mechanismen (Statistik des Rauschens, Stromaufteilung im Differenzverstärker, Regelung durch Rückkopplung mit
der Frage der Stabilität, Hysterese) und drei Kipp-Stellen. Kompakt 1800–2800 Wörter, ausführlich 3500–5000 Wörter. Der Skriptabschnitt
umfasst fünf Teilthemen; liegt der Hauptpfad über der Spanne, dem User eine Teilung vorschlagen (Rauschen und Differenzverstärker | idealer
OPV und Rückkopplung), nicht eigenmächtig teilen.

## 3. Vorwissen-Kette

- Transfergleichung $I_C = I_S\exp(U_{BE}/U_T)$: 11/01 *Der Transistoreffekt* → erinnern, verlinken.
- Steilheit $g_m = I_C/U_T$, Spannungsverstärkung $-g_m R_C = -U_{RC}/U_T$ der Emitterschaltung, „klein gegen $U_T$“: 11/03 → erinnern,
  verlinken. Das Skript schreibt hier $S$ für die Steilheit.
- Stromspiegel als Stromquelle (Kollektorstrom unabhängig von $U_{CE}$), Emitterfolger: 11/02 → erinnern, verlinken.
- Unbelasteter Spannungsteiler: 05/06 *Zusammenschaltung von Widerständen* → erinnern, verlinken.
- Kondensatorgleichung $i = C\,du/dt$, exponentielles Laden mit Zeitkonstante: 04/03 *Laden und Entladen* → erinnern, verlinken.
- Leistung $U^2/R$ an einem Widerstand: 05 → ein Halbsatz.
- Gleichverteilungssatz (kinetische Gastheorie: mittlere Energie $kT/2$ je quadratischem Energieterm): Schulphysik → im Herleitungskasten
  in einem Satz.
- Hier aufbauen: Effektivwert, Rauschdichte, Signal-Rausch-Verhältnis, Rauschquellen, Differenzverstärker, Gleichtakt, idealer OPV,
  Komparator, Flash-Wandler, Rückkopplung, Gegen- und Mitkopplung, Stabilität, goldene Regeln, Schmitt-Trigger.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Wenn ich das Nutzsignal verstärke, wird das Signal-Rausch-Verhältnis doch besser?“ (Fehlvorstellung, Skript S. 195) → SNR →
   Fehlvorstellungs-Kasten → beide.
2. „Woher kommt eine Rauschspannung an einem Widerstand, an dem gar nichts angeschlossen ist?“ → thermisches Rauschen → Text → beide.
3. „Warum addiert man Rauschspannungen quadratisch und nicht einfach?“ → Effektivwert → Text + Herleitung → beide.
4. „Wenn weißes Rauschen bei allen Frequenzen gleich stark ist, ist seine Leistung dann nicht unendlich?“ → Rauschquellen → Frage-Kasten
   (kT/C) → ausführlich.
5. „Wozu sitzt unten im Differenzverstärker ein dritter Transistor?“ → Differenzverstärker → Text (Schritt 1) → beide; „Reicht nicht ein
   Widerstand?“ → Frage-Kasten → ausführlich.
6. „Bei Gleichtakt ändern sich doch beide Basisspannungen, warum bleiben die Ströme gleich?“ → Differenzverstärker → Text (Emitterknoten
   folgt) → beide.
7. „Löscht der Differenzverstärker auch das Rauschen seiner Transistoren aus?“ (Fehlvorstellung) → Differenzverstärker →
   Fehlvorstellungs-Kasten → ausführlich.
8. „Wie kommt ein OPV auf 200 000, wenn die Stufe nur knapp 200 schafft?“ → Differenzverstärker → Frage-Kasten → ausführlich.
9. „Unendliche Verstärkung, dann liefert der Ausgang doch beliebig große Spannungen?“ (Fehlvorstellung) → idealer OPV → Text (Grenzen,
   linearer Bereich 70 µV) → beide.
10. „Warum nimmt man den OPV nicht einfach ohne Rückkopplung als Verstärker?“ → Komparator → Text (70 µV gegen 1 mV Offset) → beide.
11. „Wenn $U_D$ null ist, muss doch auch $U_A = v_D U_D$ null sein?“ → Gegenkopplung → Frage-Kasten → beide.
12. „Virtueller Kurzschluss: Sind die Eingänge dann verbunden, fließt Strom zwischen ihnen?“ (Fehlvorstellung) → Gegenkopplung →
    Fehlvorstellungs-Kasten → beide.
13. „Warum kommt die gegengekoppelte Schaltung überhaupt zur Ruhe und schwingt nicht hin und her?“ → Gegenkopplung → Text (Kipp-Stelle)
    → beide.
14. „Mit- und Gegenkopplung haben dieselben Widerstände, warum verhalten sie sich so verschieden?“ → Rückkopplung → Text + Abbildung →
    beide.
15. „Gilt $U_D = 0$ auch beim Schmitt-Trigger?“ → Schmitt-Trigger → Text → beide.
16. „Warum bleibt ein Schmitt-Trigger beim Einschalten nicht bei 0 V stehen?“ → Schmitt-Trigger → Frage-Kasten → ausführlich.
17. „Wozu Hysterese, der Komparator schaltet doch genau an der Schwelle?“ → Schmitt-Trigger → Text + Abbildung → beide.

## 5. Kipp-Stellen

**K1 Der Differenzverstärker zählt nur die Differenz.** Schritte: (1) Die Stromquelle im Fußpunkt hält die Summe der Emitterströme fest
(1 mA). (2) Beide Emitter hängen am selben Knoten; die Basis-Emitter-Spannungen unterscheiden sich genau um $U_{e1} - U_{e2}$; nach der
Transfergleichung ist das Stromverhältnis $\exp((U_{e1}-U_{e2})/U_T)$. (3) Gleichtakt: Der Emitterknoten folgt (±5 V → Knoten −5,63 / +4,36 V),
die Ströme bleiben (0,4991 mA ± 0,01 %). (4) Kleine Differenz: Der Knoten bewegt sich um die halbe Änderung (0,4998), jede
Basis-Emitter-Spannung ändert sich um die Hälfte, $\Delta I_C = \pm g_m (U_{e1}-U_{e2})/2$, $U_A = -g_m R_C (U_{e1}-U_{e2})$: −193 (−182 mit
$r_{CE}$). (5) Große Differenz: 100 mV schieben 98 % des Stroms in einen Zweig, Stromschalter, Ausgang ±9,5 V. Abbildungen
01-differenzverstaerker, 01-gleichtakt (ausführlich). Herleitung: Stromaufteilung aus Transfergleichung und Summe; Kleinsignal aus der
Ableitung. Beispiel: Stufe mit 1 mA, 10 kΩ, ±15 V. Skriptkorrektur −2SR → −SR (−387 → −193).

**K2 Gegenkopplung regelt $U_D$ auf null, und warum die Schaltung dorthin läuft.** Schritte: (1) Teiler führt $k = 0{,}1$ von $U_A$ an den
Minuseingang. (2) Masche: $U_D = U_E - k U_A$. (3) Gleichung des OPV $U_A = v_D U_D$; zusammen Ruhelage $U_A = U_E\,v_D/(1 + k v_D)$, also
$U_D = U_E/(1 + k v_D)$: 25 µV bei 5 V. (4) Ergebnis hängt praktisch nur von $k$ ab (9,9995 bzw. 9,998 bei $v_D$ = 200 000 bzw. 50 000; 0,015 %
für −75 %). (5) Dynamik: Der Ausgang ändert sich mit der Geschwindigkeit $\omega_T U_D$; jede Änderung verkleinert bei Gegenkopplung ihre
Ursache, die Abweichung klingt mit $\tau = 1/(k\omega_T)$ = 1,59 µs ab, 0,1 % nach 11 µs; Ruhe nur bei $U_D = 0$. (6) Zyklenbild des Skripts
(Ausgang springt): Faktor −20 000 je Zyklus, divergiert. Abbildungen 01-gegen-mit, 01-einschwingen. Herleitung: Rückkopplungsformel
(Algebra); Einschwingen (Differentialgleichung erster Ordnung wie beim Kondensator). Beispiel: Verstärker mit 10 kΩ/90 kΩ.

**K3 Mitkopplung und Hysterese.** Schritte: (1) Dieselben Teile, Eingänge vertauscht: Teiler an den Pluseingang, Signal an den
Minuseingang. (2) Eine Abweichung ändert $U_A$, die Rückführung vergrößert die Abweichung, sie wächst mit derselben Zeitkonstante 1,59 µs
bis an die Grenze (aus 0,13 mV in 18 µs, mit Slew-Rate 38 µs). (3) An der Grenze liegt der Pluseingang auf $k U_{A,\max}$ = 1,4 V; der
Ausgang bleibt, solange $U_E$ darunter bleibt. (4) Überschreitet $U_E$ 1,4 V, kehrt $U_D$ das Vorzeichen, der Ausgang kippt nach −14 V, die
Schwelle springt auf −1,4 V. (5) Zwischen −1,4 und +1,4 V entscheidet die Vorgeschichte; ein Rauschen kleiner als die Hysterese (2,8 V gegen
0,2 V eff.) löst kein Mehrfachschalten aus. Abbildungen 01-schmitt-kennlinie, 01-schmitt-rauschen. Herleitung: Schwellen aus der
Bedingung $U_D = 0$ bei festem Ausgang. Beispiel: Schwellen und verrauschter Sinus.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| OPV: integrierte Schaltung, zwei Eingänge, Rechenoperationen | K | Worum | Worum |
| Rauschen als Zufallsprozess, Mittelwert null, Effektivwert | K | Text | Text |
| Gl. 12.1 Effektivwert aus der Rauschdichte, Einheiten V²/Hz und V/√Hz | K | Formel + Herleitung | dito + Beispiel |
| quadratische Addition unabhängiger Quellen | K | im Herleitungskasten + 1 Satz | Formel + Herleitung + Beispiel |
| Signal-Rausch-Verhältnis, dB | K | Formel | Formel + Beispiel |
| Verstärken verbessert das SNR nicht (Skript S. 195) | K | Fehlvorstellungs-Kasten | Kasten + Beispiel Messkette |
| thermisches Rauschen 4kTR (Gl. 12.2), Mechanismus, Zahlen | K | Formel + Herleitung + Zahl | dito + Beispiel |
| Herleitung von 4kTR über Gleichverteilung und kT/C | H | im Kasten (Beweisidee) | dito |
| kT/C, endliche Gesamtleistung trotz weißem Spektrum | V | – | Frage-Kasten |
| weißes Rauschen = Spektralform, keine eigene Ursache (Skriptkorrektur) | K | 1 Satz | Text |
| Schrotrauschen, $2eI$, relative Schwankung bei kleinen Strömen | H | 1 Satz | Text + Formel + Herleitung + Zahl |
| 1/f-Rauschen, Eckfrequenz, gleiche Leistung je Dekade | H | 1 Satz | Text + Formel + Herleitung |
| Differenzverstärker: Schaltung, Stromquelle, Gleichtakt, Stromaufteilung | K | Schritte + Abbildung + Formel | dito + Gleichtakt-Abbildung |
| Kleinsignalverstärkung $-g_m R_C$ (Skript −2SR) | K | Formel + Herleitung + Beispiel | dito |
| Gleichtaktspannung, Widerstand statt Stromquelle (48 dB) | H | – | Frage-Kasten |
| Grenze $U_{RC}/U_T$, „10 000“ im Skript, Aufbau des OPV aus Stufen | H | 1 Satz | Frage-Kasten |
| Differenzverstärker löscht kein Eigenrauschen | H | – | Fehlvorstellungs-Kasten |
| idealer OPV: vier Eigenschaften, Folgen, Werte des 741 | K | Tabelle | Tabelle |
| Ausgangsgrenzen, linearer Bereich 70 µV, Offset 1 mV | K | Text + Formel | dito + Beispiel |
| Komparator, Kennlinie | K | Text | Text + Abbildung |
| Flash-Wandler | H | 1–2 Sätze | Text + Abbildung + Beispiel |
| Rückkopplung, Mit- und Gegenkopplung (Definition) | K | Text | Text |
| Rückkopplungsformel, $U_D \to 0$, Unabhängigkeit von $v_D$ | K | Formel + Herleitung + Beispiel | dito |
| Einschwingen: Ausgang ändert sich mit $\omega_T U_D$, $\tau = 1/(k\omega_T)$, Stabilität | K | Formel + Herleitung + Zahl | dito + Abbildung |
| Miller-Kondensator 30 pF, $G_{m1}$ = 0,19 mS, Slew-Rate aus dem Stromschalter | V | – | Vertiefung |
| Zyklenbild des Skripts (S. 202) | H | 1–2 Sätze | Text + Zahl |
| goldene Regeln, nur mit Gegenkopplung und ohne Sättigung | K | Merke | Merke + Beispiel Sättigung |
| $U_A \ne 0$ trotz $U_D = 0$ | H | Frage-Kasten | Frage-Kasten |
| virtueller Kurzschluss ist keine Verbindung | K | Fehlvorstellungs-Kasten | dito |
| Schmitt-Trigger: Schaltung, Mechanismus, Schwellen, Hysterese | K | Schritte + Formel + Herleitung + Beispiel | dito |
| instabile Ruhelage, Einschalten | H | – | Frage-Kasten |
| Hysterese gegen verrauschte Eingänge | K | Text | Text + Abbildung |
| Offset, Bandbreite, Slew-Rate, Gleichtaktunterdrückung im Detail | S | Verweis 12/03 | Verweis 12/03 |
| Grundschaltungen (invertierend usw.) | S | Verweis 12/02 | Verweis 12/02 |

## 7. Abbildungsplan (Szene-IDs get1/operationsverstaerker/01-…)

| ausf. | komp. | Szene · Vorlage | Inhalt | Kernaussage |
|---|---|---|---|---|
| 1 | 1 | 01-opv-kennlinie · schaltung-und-kennlinie | (a) Schaltsymbol mit $U_D$ (Pfeil von + nach −), $U_A$ gegen Masse, ±15 V; (b) $U_A$ über $U_D$ von −200 bis +200 µV: Gerade mit Steigung 200 000 zwischen ±70 µV, darüber ±14 V | allein ist der OPV nur in ±70 µV linear |
| 2 | 2 | 01-rauschen · zeitverlauf-und-spektrum | (a) Rauschspannung 10 kΩ über 1 MHz, Effektivwert 12,9 µV; (b) Dichten doppelt-logarithmisch 0,1 Hz–1 MHz: 10 kΩ 12,9 nV/√Hz waagrecht, OPV 23 nV/√Hz mit 1/f-Anstieg unter 100 Hz | im Zeitverlauf unvorhersagbar, durch Effektivwert und Dichte beschrieben |
| 3 | – | 01-messkette · blockschaltbild-pegel | Sensor 1 mV / 1,82 µV → Verstärker (3,25 µV eigen, ×100) → Folgestufe 1 mV; SNR 54,8 / 48,6 / 48,6 / 39,4 dB; ohne Vorverstärker 0 dB | Verstärken schützt vor späterem Rauschen, verbessert das SNR aber nicht |
| 4 | 3 | 01-differenzverstaerker · schaltung-und-kennlinie | (a) Q1, Q2, $R_C$ = 10 kΩ an +15 V, Stromquelle 1 mA nach −15 V, Ruhewerte; (b) $I_{C1}$, $I_{C2}$ über $U_{e1}-U_{e2}$ von −150 bis +150 mV, Summe 1 mA, Tangente, 98 %/2 % bei ±100 mV | die Stromquelle hält die Summe, die Differenz verteilt sie |
| 5 | – | 01-gleichtakt · schaltung-zustaende | drei Zustände $U_{Gl}$ = −5 / 0 / +5 V: Knoten −5,63 / −0,63 / +4,36 V, Ströme je 0,499 mA, $U_A$ = 0 | der Emitterknoten folgt dem Gleichtakt, die Ströme bleiben |
| 6 | – | 01-flash-wandler · schaltung | 2 Bit, $U_{Ref}$ = 2 V, 4 × 1 kΩ, Schwellen 0,5/1,0/1,5 V, $U_E$ = 1,2 V → 0 1 1 | die Zahl der hohen Ausgänge ist der Messwert |
| 7 | 4 | 01-gegen-mit · schaltung-zustaende | gleiche Teile (10 kΩ, 90 kΩ), links Gegenkopplung (Verstärker ×10), rechts Mitkopplung (Schmitt-Trigger), Wirkungskette mit Vorzeichen | welcher Eingang das zurückgeführte Signal bekommt, entscheidet zwischen Regeln und Kippen |
| 8 | 5 | 01-einschwingen · zeitverlauf | (a) Sprung 10 mV: $U_A$ → 0,1 V mit τ = 1,59 µs, $U_D$ von 10 mV auf 5,8 µV bei 12 µs (Endwert 0,5 µV, log); (b) Mitkopplung aus 0,13 mV: exponentiell, dann Slew-Rate, −14 V nach 38 µs | Gegenkopplung: Abweichung klingt ab; Mitkopplung: wächst mit derselben Zeitkonstante |
| 9 | 6 | 01-schmitt-kennlinie · kennlinie-hysterese | $U_A$ über $U_E$ −3…+3 V, Sprünge bei +1,4 V (nach −14 V) und −1,4 V (nach +14 V), gestrichelt instabile Gerade $U_E/k$ | Gedächtnis zwischen den Schwellen |
| 10 | – | 01-schmitt-rauschen · zeitverlauf | Eingang 3 V cos 50 Hz + 0,2 V eff. Rauschen; Komparator 43–59 Umschaltungen je Nulldurchgang (Rauschen bis 100 kHz); Schmitt-Trigger eine, 0,9 bis 1,1 ms später (ohne Rauschen 1,55 ms) | Hysterese größer als das Rauschen verhindert Mehrfachschalten |

Kompakt 6, ausführlich 10.

## 8. Zahlenwerk

`notizen/get1/zahlen_opv.py` (neu für das Oberthema), Ausgabe `zahlen_opv.txt`. Beispiel-OPV nach Art des 741 an ±15 V ($v_D$ = 200 000,
min. 50 000; $f_T$ = 1 MHz; Slew-Rate 0,5 V/µs; ±14 V; 2 MΩ; 80 nA; 1 mV Offset; 23 nV/√Hz; 30 pF Kompensation). Differenzverstärker mit dem
Beispieltransistor aus `zahlen_transistor.py`. Rauschen bei 300 K. Funktionen: `u_therm`, `u_ktc`, `enbw_rc`, `i_schrot`, `u_1f`,
`diffpaar`, `a_geschlossen`, `sim` (einpoliges OPV-Modell mit Slew-Rate und Grenzen), `schmitt_kette`.

## 9. Profi-Abgleich

- TI LM741, Datenblatt SNOSC25D, Electrical Characteristics: https://www.ti.com/document-viewer/LM741/datasheet/specifications —
  200 V/mV typ. (50 min.), ±14 V typ. bei 10 kΩ, 2 MΩ, 80 nA, 1 mV, 95 dB, 25 mA, 0,5 V/µs.
- ST UA741 (über LCSC, Datenblatt https://www.lcsc.com/datasheet/C7111.pdf): Verstärkungs-Bandbreite-Produkt 1 MHz, 23 nV/√Hz bei 1 kHz,
  0,5 V/µs.
- Analog Devices, Tutorials MT-047 und MT-048 (Op Amp Noise): https://www.analog.com/media/en/training-seminars/tutorials/MT-048.pdf —
  Spannungsrauschen typisch 1–20 nV/√Hz; 1/f-Eckfrequenz 1–10 Hz bei den besten rauscharmen, bis etwa 100 Hz bei Universal- und
  JFET-OPVs, bei CMOS oft mehrere kHz.
- Wikipedia „Operational amplifier“: 30 pF Kompensationskondensator im 741, zweite Stufe integriert den Strom der Eingangsstufe (Miller),
  Slew-Rate = größter Strom / Kapazität.
- Ergebnis: Rückkopplungsformel, Integratormodell $dU_A/dt = \omega_T U_D$ mit $\omega_T = G_{m1}/C_c$ und Slew-Rate = $I_{\max}/C_c$ stimmen
  mit dem Plan; aus 1 MHz und 30 pF folgen $G_{m1}$ = 0,19 mS und 15 µA Ladestrom (Zahlenwerk).

## 10. Skript-Abgleich

**Inhalte des Quellabschnitts (Vollständigkeit):**
- S. 195: OPV = integrierte Analogschaltung auf Transistorbasis, Operationen (addieren, subtrahieren, logarithmieren); Anwendung Entkopplung
  einer Messgröße von Rauschen. 12.1: Rauschen aus vielen harmonischen Schwingungen, Zufallsprozess, SNR, Effektivwert Gl. 12.1 aus der
  „Rauschspannungsdichte“ $|u_r(f)|^2$; thermisches Rauschen (Brownsche Bewegung, ohne Strom) Gl. 12.2 $4kTR$; weißes Rauschen (konstante
  Leistungsdichte, unendliche Gesamtleistung).
- S. 196: Schrotrauschen (Strom über eine Potentialbarriere, statistisch, pn-Übergang); 1/f-Rauschen (bis 10 kHz störend, Umladung von
  Oberflächenzuständen, Schwankung der Ladungsträgerzahl). 12.2: Differenzverstärker verstärkt $U_{e1} - U_{e2}$, Gl. 12.3 mit
  $v \approx 10\,000$; gleiche Spannungen → 0; Idee: gemeinsamer verrauschter Gleichanteil fällt heraus; Bild 12.1 (Q1, Q2, $R_C$, Q3 mit
  $U_{bias}$, Emitter von Q3 an Masse, $U_A$ zwischen den Kollektoren).
- S. 197: zwei symmetrische Emitterschaltungen; Q3 legt $I_{Q3}$ fest; Gl. 12.4 $I_{Q1} = I_{Q2} = I_{Q3}/2$; $U_A = U_{a1} - U_{a2} = 0$;
  Kleinsignal mit Steilheit $S = I_{C1}/U_T$, $\Delta I_{Q1} \approx u_{e,s} S$, $U_{a1}$, $U_{a2}$, $A = -2SR$; $A \approx 10\,000$; OPV gesamt
  $10^5$ bis $10^6$.
- S. 198: 12.3: Beschaltung bestimmt die Übertragung; Schaltsymbol Bild 12.2; Plus nichtinvertierend (wie $U_{e2}$), Minus invertierend (wie
  $U_{e1}$); $v_D$ verstärkt $U_D$; vier ideale Eigenschaften mit Folgen; realer OPV: endliche Verstärkung, Hub $U_{a,\min}$ bis $U_{a,\max}$,
  Sättigung, Exemplarstreuung, Temperatur, Abfall bei hohen Frequenzen.
- S. 199: Komparator (Bild 12.3), $U_D = U_1 - U_2$, $U_A = v_D U_D$, ideal $U_{B+}$ bzw. $U_{B-}$, real $U_{A,\max} < U_{B+}$ wegen
  Halbleiterstrecken; Kennlinie Bild 12.4.
- S. 200: 2-Bit-Flash-Wandler (Bild 12.5, $U_{Ref}$ = 3 V, drei R, 2,5 V Eingang); 12.4: Rückkopplung (Definition), Mitkopplung positiv
  bzw. phasenrichtig, Gegenkopplung negativ bzw. gegenphasig; Mitkopplung über den Plus-, Gegenkopplung über den Minuseingang;
  Gegenkopplung regelt $U_D$ auf null, Mitkopplung: $U_D \ne 0$.
- S. 201: invertierender Schmitt-Trigger (Bild 12.6: $U_E$ am Minuseingang, $R_2$ vom Ausgang zum Pluseingang, $R_1$ nach Masse);
  $U_E = 0$ stationär; Berechnungszyklus $U_D = -U_E(1 + v_D R_1/(R_1+R_2))$; instabil bei unbegrenzter Versorgung; begrenzt: Ausgang an
  $U_{B-}$ oder $U_{B+}$.
- S. 202: $U_E > 0$ → $U_{A,\min}$, stationär; Hystereseschleife, Vorgeschichte; Schwellen $U_{R1,\min} = U_{A,\min} R_1/(R_1+R_2)$ und
  $U_{R1,\max}$. Anfang 12.5: Gegenkopplung an Abb. 12.7 als Folge von Zyklen mit Vorzeichenwechsel von $U_D$; „man kann quantitativ
  zeigen, dass der Betrag von $U_D$ nach jedem Zyklus kleiner wird“.
- S. 203: „ab jetzt immer $U_D = 0$, wenn gegengekoppelt“.

**Fehler und Ungenauigkeiten des Skripts:**
1. S. 195: „jedoch kann das Nutzsignal verstärkt werden, sodass sich das Signal-Rausch-Verhältnis verbessert“ — Verstärkung hebt Signal und
   schon vorhandenes Rauschen gleich an und fügt eigenes Rauschen hinzu; das SNR wird dabei nicht besser (Beispiel 54,8 → 48,6 dB). Sie
   schützt nur gegen Rauschen, das erst hinter dem Verstärker hinzukommt (ohne Vorverstärker 0 dB, mit 39,4 dB). Präzisieren.
2. S. 195: thermisches Rauschen „proportional zur Temperatur T, zum Widerstandswert R und zur Boltzmann-Konstante“ gilt für die
   Leistungsdichte; die Rauschspannung wächst mit der Wurzel (10 kΩ: 12,9 nV/√Hz, 1 MΩ: 129). Als Ursache nennt das Skript richtig die
   Wärmebewegung; die Unvorhersagbarkeit führt es aber auch auf „unregelmäßige Gitterfehler“ zurück, die ortsfest sind (zufällig ist die
   Wärmebewegung), und „sporadisch“ ist irreführend, die Rauschspannung ist ständig da (nach Faktencheck präzisiert: Das Skript behauptet
   nicht, die Gitterfehler bestimmten die Größe). Die Beschreibung der Boltzmann-Konstante („Energie pro Kelvin, die einem Ladungsträger zugeführt
   wird“) ist ungenau: Sie verknüpft Temperatur und Energie; je quadratischem Energieterm entfällt im Mittel kT/2.
3. S. 195: „weißes Rauschen“ als zweite von vier Ursachen — „weiß“ beschreibt die Form des Spektrums, keinen Mechanismus; thermisches und
   Schrotrauschen sind weiß. Die unendliche Gesamtleistung gilt nur für das idealisierte Modell; jede reale Schaltung begrenzt die
   Bandbreite (an 10 pF bleiben 20 µV, unabhängig von R).
4. S. 196: Gl. 12.3 $U_a = v\,(U_{e1} - U_{e2})$ mit positivem $v$ passt nicht zur Schaltung, für die das Skript selbst $A = -2SR < 0$ erhält;
   $U_{e1}$ wirkt invertierend (wie S. 198 sagt). Vorzeichen klarstellen.
5. S. 197: $\Delta I_{Q1} \approx u_{e,s} S$ — der gemeinsame Emitterknoten steigt um die halbe Signaländerung, $U_{BE1}$ ändert sich nur um
   $u_{e,s}/2$, also $\Delta I_{Q1} = S u_{e,s}/2$ und $A = -SR$, nicht $-2SR$. Im Beispiel −193 statt −387; das vollständige Modell zeigt den
   Knoten mit 0,4998 der Änderung und −182 (mit $r_{CE}$).
6. S. 197: „Typischerweise nimmt A Werte in der Größenordnung 10000 an“ — mit Widerständen als Last ist $|A| = U_{RC}/U_T$, im Beispiel 193,
   an 15 V höchstens 580; Werte um $10^3$ bis $10^4$ je Stufe erst mit Stromquellen als Last (Stromspiegel: rund 1500 mit dem
   Beispieltransistor).
7. S. 199: „sofort $U_{B+}$ bzw. $U_{B+}$“ — Tippfehler, gemeint $U_{B-}$.
8. S. 201: „Für den Fall $U_E = 0$ verändert sich nichts“ (Schmitt-Trigger mit begrenzter Versorgung) — $U_A = 0$ ist eine Ruhelage, aber
   instabil: Jede Abweichung (1 mV Offset, Rauschen) wächst, nach einigen 10 µs liegt der Ausgang an einer Grenze (aus 0,13 mV: 38 µs mit
   Slew-Rate). Ein realer Schmitt-Trigger steht nie bei 0 V.
9. S. 202: Zyklenbild der Gegenkopplung — springt der Ausgang je Zyklus auf $v_D U_D$, wächst die Abweichung je Zyklus um den Faktor
   $-k v_D$ (−20 000 bei $k$ = 0,1); das Bild schaukelt auf, statt zu konvergieren, und die Behauptung, $|U_D|$ werde je Zyklus kleiner, gilt
   in ihm nur für $k v_D < 1$. Richtig: Der Ausgang ändert sich stetig, mit einer Geschwindigkeit proportional zu $U_D$; dann klingt jede
   Abweichung exponentiell ab ($\tau = 1/(k\omega_T)$ = 1,6 µs), ohne Vorzeichenwechsel.
10. S. 198/200: Mit unendlicher, frequenzunabhängiger Verstärkung allein ist nicht entscheidbar, ob eine Schaltung zur Ruhe kommt: Die
    Mitkopplung hat dieselbe rechnerische Ruhelage mit $U_D = 0$. Dass $U_D \ne 0$ „stets“ bei Mitkopplung gilt, stimmt für jeden stabilen
    Zustand. Präzisieren, kein Fehler.

11. S. 196: „Letzteres [das Nutzsignal] wird zudem verstärkt, was zu besseren SNR-Werten führt“ — beim Differenzverstärker wird das
    Verhältnis besser, weil das gemeinsame Rauschen herausfällt, nicht durch die Verstärkung (ergänzt nach dem Faktencheck).

## Faktencheck (22.10.2026)

7 Fehler, 14 Ungenauigkeiten, alle nachgerechnet und eingearbeitet. Fehler: Endwert der Differenzspannung beim Sprung 2,5 µV statt
25 µV (die 25 µV gehören zu 5 V Ausgang); „die 1 im Nenner ist der direkte Weg“ falsch, sie stammt von U_A/v_D; Schaltzeitpunkt des
Schmitt-Triggers mit Rauschen 0,91–1,09 ms statt 1,55 ms (Zahlenwerk ergänzt); 1/f-Rauschen wächst je Dekade im mittleren Quadrat,
nicht um 349 nV; Hörbereich ab 20 Hz +1,7 % statt „unter 1 %“; Skriptkorrektur zum thermischen Rauschen war unfair formuliert;
kT/C an 10 pF 20,4 statt 20,3 µV. Ungenau u. a.: SNR „bei gleicher Bandbreite“; Messkette braucht einen schnelleren Verstärker als
den 741; Eingangsruhestrom 80 nA statt nur 12,5 pA; Kernteil gegen Merke (zweite goldene Regel); Integratormodell beim 50-mV-Sprung
nur auf 11 % genau (tanh-Modell der Eingangsstufe) → Beispiel auf 10 mV umgestellt; Rauschbandbreite 100 kHz angegeben; „1/f“ ist
ebenfalls eine Spektralform; 23 nV/√Hz gilt bei 1 kHz; Begründungen der quadratischen Addition präzisiert; Integral endlich nur bei
Abfall schneller als 1/f; Flash-Wandler mit 2^n bzw. 2^n − 1 Widerständen; Q3 an −15 V als Abweichung vom Skriptbild gekennzeichnet;
doppelte Symbole (U_S, S, x) beseitigt, Schwellen heißen jetzt wie im Skript U_R1,max und U_R1,min; Querverweise der kompakten
Fassung bereinigt.
