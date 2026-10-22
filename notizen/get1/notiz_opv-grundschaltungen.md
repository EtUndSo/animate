# Arbeitsnotiz: Die OPV-Grundschaltungen (ET1 Kap. 12.5, 12.6 und 12.8), Stil 3

Skript S. 203–214 (PDF 209–220): invertierender Verstärker mit Aussteuergrenze (Bilder 12.7–12.9), nichtinvertierender Verstärker
(12.10, Gl. 12.5), Addierer (12.11), Subtrahierer (12.12, Gl. 12.6, 12.7), Integrator (12.13), Differenzierer (12.14), Logarithmierer
(12.15), Exponentialfunktion (12.16), analoge Multiplikation (12.17, 12.18), Impedanzwandler (12.19); 12.6 negativer Widerstand (NIC)
und Transimpedanzverstärker; 12.8 Rechnen mit Potentialen (Bild 12.20), Kaskade (12.21) und Rechenschema (12.22). Der Mechanismus der
Gegenkopplung vom Anfang von 12.5 und die goldenen Regeln stehen in 12/01; der reale OPV (12.7) folgt in 12/03.

## 1. Ein-Satz-Prinzip

Bei Gegenkopplung stellt sich der Ausgang des OPV so ein, dass zwischen seinen Eingängen keine Spannung liegt, und in die Eingänge des
idealen OPV fließt kein Strom; aus diesen beiden Regeln und den Gleichungen der äußeren Bauteile folgt jede Grundschaltung, und welche
Bauteile im Eingangs- und im Rückkopplungszweig sitzen (Widerstand, Kondensator, Diode), bestimmt die Rechenoperation. Die
stromlosen Eingänge sind eine Eigenschaft des idealen OPV, kein Ergebnis der Regelung.

## 2. Schwierigkeit und Längenspannen

Mittel in der Tiefe (ein Verfahren, viele Anwendungen), aber breit: 14 Schaltungen mit je eigener Formel. Deshalb die Spannen von
„schwer“: kompakt 1800–2800 Wörter, ausführlich 3500–5000 Wörter; Ziel kompakt etwa 2300, ausführlich etwa 3800. Jede Schaltung knapp:
Schaltbild, Mechanismus in zwei bis vier Sätzen, Formel, Herleitung im Kasten; Beispiele nur für die tragenden Schaltungen.

## 3. Vorwissen-Kette

- Goldene Regeln, virtueller Kurzschluss, Rückkopplungsfaktor, Sättigung: 12/01 → erinnern, verlinken.
- Ohmsches Gesetz, Kirchhoffsche Regeln, Spannungsteiler, Superposition: 05/06, 07 → erinnern, verlinken.
- Kondensatorgleichung $i = C\,du/dt$ und $u = \frac{1}{C}\int i\,dt$: 04 → erinnern, verlinken.
- Diodenkennlinie $I = I_S\exp(U/U_T)$, Temperaturgang, reale Abweichungen: 10/02 → erinnern, verlinken.
- Transfergleichung des Transistors: 11/01 → für den Logarithmierer mit Transistor.
- Ideales Spannungsmessgerät, Innenwiderstand: 06 Strom- und Spannungsmessung → erinnern, verlinken.
- Hier aufbauen: virtuelle Masse, alle Grundschaltungen, Eingangswiderstände, Rechenschema, Kaskade, NIC, Transimpedanz.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Der Minuseingang ist gar nicht mit Masse verbunden, warum liegt er auf 0 V?“ → invertierender Verstärker → Text (K1) → beide.
2. „Fließt der Strom durch R_1 nicht in den OPV hinein?“ (Fehlvorstellung) → invertierender Verstärker → Text (Schritt) → beide.
3. „Warum ist der Eingangswiderstand des invertierenden Verstärkers nur R_1, der OPV-Eingang ist doch unendlich hochohmig?“ →
   invertierender Verstärker → Frage-Kasten → beide.
4. „Dann kann ich den Minuseingang doch gleich mit Masse verbinden?“ (Fehlvorstellung) → invertierender Verstärker →
   Fehlvorstellungs-Kasten → ausführlich.
5. „Kann der nichtinvertierende Verstärker auch abschwächen?“ → nichtinvertierender Verstärker → Frage-Kasten → ausführlich.
6. „Wozu ein Verstärker mit der Verstärkung 1?“ → Impedanzwandler → Text (K2) → beide.
7. „Warum addiert der Addierer, die Spannungen liegen doch an verschiedenen Widerständen?“ → Addierer → Text → beide.
8. „Warum müssen beim Subtrahierer die Widerstandsverhältnisse so genau stimmen?“ → Subtrahierer → Frage-Kasten → ausführlich.
9. „Läuft der Integrator nicht irgendwann weg?“ → Integrator → Frage-Kasten → beide.
10. „Warum sieht man Differenzierer so selten?“ → Differenzierer → Frage-Kasten → ausführlich.
11. „Warum nimmt man für den Logarithmierer einen Transistor statt einer Diode?“ → Logarithmierer → Text/Frage → ausführlich.
12. „Ein negativer Widerstand verstößt doch gegen die Energieerhaltung?“ (Fehlvorstellung) → NIC → Fehlvorstellungs-Kasten → beide.
13. „Warum kehren fast alle Schaltungen das Vorzeichen um?“ → invertierender Verstärker → Text → beide.
14. „Multipliziert oder addiert man die Verstärkungen hintereinandergeschalteter Stufen?“ → Kaskade → Text → beide.
15. „Woran sehe ich, ob ich mit U_D = 0 rechnen darf?“ → Rechenschema → Text → beide.

## 5. Kipp-Stellen

**K1 Virtuelle Masse (invertierender Verstärker).** Schritte: (1) Pluseingang an Masse; (2) Gegenkopplung macht $U_D$ = 0, also liegt der
Minuseingang auf 0 V, ohne verbunden zu sein (mit $v_D$ = 200 000 auf 10 µV bei 2 V Ausgang); (3) Strom durch $R_1$ ist $U_E/R_1$, 0,1 mA bei
1 V; (4) er kann nicht in den OPV, also fließt er weiter durch $R_2$; (5) der Ausgang muss ihn abnehmen und liegt deshalb bei
$-R_2 I$ = −2 V; (6) die Quelle sieht $R_1$ nach virtueller Masse: Eingangswiderstand 10 kΩ. Abbildung 01-invertierer (Schaltung, Ströme,
Sinus mit Begrenzung). Zahlen: −1,99997 mit endlichem $v_D$; Sinus 5 V: A = −2 unverzerrt, A = −3 begrenzt (23,4 % der Zeit), Grenze
4,667 V, im Scheitel $U_D$ = −0,25 V. Herleitung über Knotenregel. Beispiel: Verstärker 10 kΩ/20 kΩ.

**K2 Eingangswiderstand und Impedanzwandler.** Schritte: (1) nichtinvertierend: Quelle am Pluseingang, kein Strom; (2) Teiler macht den
Minuseingang zu $k U_A$; (3) $U_D$ = 0 → $U_A = U_E/k = (1 + R_2/R_1) U_E$, mindestens 1; (4) Folger: ganzer Ausgang zurück, $A$ = 1;
(5) Nutzen: Quelle wird nicht belastet, Ausgang liefert Strom. Abbildung 02-nichtinvertierer (beide Schaltungen, Messaufbau). Zahlen:
3 statt −2 mit denselben Widerständen; Messung 5 V/100 kΩ: 4,545 V mit 1-MΩ-Messgerät, 4,992 V mit 741-Folger (80 nA Ruhestrom; mit ±1 mV Offset
4,991–4,993 V), 5,000 V ideal. Herleitung über Teilerregel und $U_D$ = 0. Beispiel: Messung.

**K3 Integrator.** Schritte: (1) virtuelle Masse am Minuseingang; (2) Strom $u_E/R$ fließt in den Kondensator; (3) seine Spannung wächst
mit dem Integral des Stroms; (4) der Ausgang liegt um diese Spannung unter der virtuellen Masse: $u_A = -\frac{1}{RC}\int u_E\,dt$;
(5) konstante Eingangsspannung → Rampe (−1 V/ms bei 1 V und 1 ms), Rechteck → Dreieck. Abbildung 05-integrator (Schaltungen und
Zeitverläufe). Zahlen: −14 V nach 14 ms; Rechteck ±1 V/1 kHz → 0,5 V Spitze-Spitze; Offset 1 mV → 14 s. Herleitung über
Kondensatorgleichung. Beispiel: Rechteck und Rampe.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Rechenschema (Bild 12.22): Kopplung prüfen, Übersteuerung prüfen, dann $U_D$ = 0 und Kirchhoff | K | Text | Text + Abbildung |
| invertierender Verstärker, virtuelle Masse, $A = -R_2/R_1$ | K | Schritte + Formel + Herleitung + Beispiel | dito |
| Eingangswiderstand $R_1$ | H | Frage-Kasten | Frage-Kasten |
| endliches $v_D$: −1,99997, 10 µV | H | 1 Satz | im Beispiel |
| Aussteuergrenze mit Sinus (Bilder 12.8/12.9) | K | Text mit Zahlen | Text + Abbildung + Beispiel |
| virtuelle Masse ≠ Masse | H | – | Fehlvorstellungs-Kasten |
| nichtinvertierender Verstärker (Gl. 12.5), $A \ge 1$ | K | Formel + Herleitung | dito + Frage-Kasten |
| Impedanzwandler, Messung an hochohmiger Quelle | K | Text + Formel | dito + Beispiel |
| Eingangswiderstand des realen Folgers, Ruhestrom | V | – | im Beispiel |
| Addierer, gewichtete Summe, Digital-Analog-Umsetzer | K | Formel + Herleitung | dito + Beispiel |
| Subtrahierer mit Superposition (Gl. 12.6, 12.7) | K | Formel + Herleitung | dito + Beispiel |
| Gleichtaktunterdrückung durch Widerstandsabgleich (1 % → 61 dB) | H | – | Frage-Kasten |
| Integrator, Rampe, Rechteck → Dreieck | K | Schritte + Formel + Herleitung + Beispiel | dito |
| Offset integriert, Parallelwiderstand | H | Frage-Kasten | Frage-Kasten |
| Differenzierer, Dreieck → Rechteck, Rauschen ∝ f | K/H | Formel + Herleitung | dito + Frage-Kasten |
| Logarithmierer, 59,5 mV je Dekade, nur positive Eingänge | K | Formel + Herleitung | dito + Beispiel |
| Temperaturgang (+23 mV bei 1 V und +10 K, Steigung +3,3 %), Transistor statt Diode | H | 1 Satz | Text/Frage |
| Exponentialfunktion | K | Formel + Herleitung | dito |
| Multiplikation über Logarithmen, Maßstab, Referenz | K/H | Text + Formel | dito + Abbildung + Präzisierung |
| Herkunft des Namens (Analogrechner) | V | – | 1 Satz |
| Transimpedanzverstärker, Fotodiode bei 0 V | K | Formel + Herleitung | dito + Beispiel |
| NIC, $R_E = -R_2$, Kompensation einer Stromquelle | K | Formel + Herleitung | dito + Beispiel |
| Stabilität des NIC (Mit- und Gegenkopplung zugleich) | H | 1 Satz | Text |
| negativer Widerstand und Energie | H | Fehlvorstellung | Fehlvorstellung |
| Kaskade: Produkt der Verstärkungen; Rechnen über Potentiale (Bild 12.20) | K | Text + Formel | dito + Skriptkorrektur |

## 7. Abbildungsplan (Szene-IDs get1/operationsverstaerker/02-…)

| ausf. | komp. | Szene · Vorlage | Inhalt | Kernaussage |
|---|---|---|---|---|
| 1 | 1 | 02-invertierer · schaltung-und-zeitverlauf | (a) 10 kΩ/20 kΩ, 1 V, 0,1 mA, Minuseingang 0 V, Ausgang −2 V; (b) Sinus 5 V, Ausgang bei A = −2 (±10 V) und A = −3 (bei ±14 V begrenzt) | der Strom durch $R_1$ muss durch $R_2$; Grenzen der Aussteuerung |
| 2 | – | 02-rechenschema · ablaufdiagramm | Schema nach Skript Bild 12.22 | erst Kopplung und Übersteuerung prüfen, dann rechnen |
| 3 | 2 | 02-nichtinvertierer · schaltung-zustaende | (a) nichtinvertierender Verstärker 10/20 kΩ, A = 3; (b) Impedanzwandler; (c) Messung 5 V/100 kΩ mit 1 MΩ: 4,545 V, mit Folger 5,000 V | kein Strom aus der Quelle |
| 4 | 3 | 02-addierer-subtrahierer · schaltung-zustaende | (a) 3-Bit-Addierer 10/20/40 kΩ, Code 101 → −6,25 V; (b) Subtrahierer 10/100 kΩ, 2,500/2,505 V → 50 mV | Ströme addieren sich an der virtuellen Masse; Differenz × R_2/R_1 |
| 5 | 4 | 02-integrator · schaltung-und-zeitverlauf | (a) Integrator 10 kΩ/100 nF, Rechteck ±1 V 1 kHz → Dreieck 0,5 V Spitze-Spitze; (b) Differenzierer mit idealem OPV, Dreieck ±1 V → Rechteck ∓4 V | Kondensator im Rückweg integriert, am Eingang differenziert |
| 6 | 5 | 02-logarithmierer · kennlinie-semilog | (a) Logarithmierer und Exponentialschaltung (Beispieldiode, 10 kΩ, Polung angegeben); (b) $U_A$ über $U_E$ logarithmisch 10 mV–10 V: Gerade, 59,5 mV je Dekade; bei 310 K steiler (61,5 mV je Dekade) und 21–27 mV höher | Diode im Rückweg logarithmiert |
| 7 | – | 02-multiplizierer · blockschaltbild | Bild 12.17/12.18 nachgebildet mit Werten; Maßstab 1/(R I_S) und Referenz 10 V über einen Umkehrer im Addierer | ln x + ln y = ln xy, aber nur mit Referenz brauchbar |
| 8 | 6 | 02-transimpedanz-nic · schaltung-zustaende | (a) Fotodiode (Anode am Minuseingang) an Transimpedanzverstärker 100 kΩ, 1 µA → −0,1 V; (b) NIC 10 kΩ an Stromquelle 1 mA/10 kΩ, Last 1 kΩ: 0,909 mA ohne, 1,000 mA mit NIC | virtuelle Masse misst Ströme; negativer Widerstand hebt $R_q$ auf |

Kompakt 6, ausführlich 8.

## 8. Zahlenwerk

`notizen/get1/zahlen_opv.py`, Abschnitt „Thema 02“, Funktionen `a_invertierend`, `a_nichtinvertierend`, `subtrahierer`,
`bericht_grundschaltungen()`; Beispieldiode aus `zahlen_halbleiter.py` ($I_S$ = 1,457·10⁻¹⁴ A, `IS_von_T`, `spannung_real`); Beispiel-OPV wie
in 12/01.

## 9. Profi-Abgleich

- Analog Devices MT-077 „Log Amp Basics“: https://www.analog.com/media/en/training-seminars/tutorials/MT-077.pdf — Steigung und
  Achsenabschnitt des Dioden- bzw. Transistor-Logarithmierers temperaturabhängig, nur einpolige Signale; deshalb Kompensation.
- Analog Devices AD633 (Datenblatt, Kopie): https://www.electrokit.com/upload/product/40350/40350633/AD633.pdf — Vierquadranten-
  Analogmultiplizierer $W = (X_1 - X_2)(Y_1 - Y_2)/10\ \mathrm{V} + Z$ aus translinearer Zelle, vergrabener Z-Diode als Referenz und
  Ausgangsverstärker: Ein brauchbarer Multiplizierer braucht einen Maßstab; er multipliziert aber nicht über getrennte Logarithmierer.
- Segovia-Vargas u. a., Radioengineering 25 (2016) 409: https://www.radioeng.cz/fulltexts/2016/16_03_0409_0418.pdf — NIC-Schaltungen haben
  Stabilitätsprobleme; die Bedingung hängt von den angeschlossenen Impedanzen ab (hier mit dem einfachen Modell aus 12/01: Gegenkopplung
  muss die Mitkopplung überwiegen).
- Ergebnis: Formeln wie im Skript; Präzisierungen beim Multiplizierer (Maßstab) und NIC (Stabilität).

## 10. Skript-Abgleich

**Inhalte des Quellabschnitts (Vollständigkeit):**
- S. 203: ab jetzt $U_D$ = 0 bei Gegenkopplung; invertierender Verstärker Bild 12.7, Herleitung $A = -R_2/R_1$; nur äußere Bauteile in der
  Übertragungsfunktion; Beispiel $R_2/R_1$ = 2, Sinus 5 V, Grenzen ±10 V.
- S. 204: Bilder 12.8, 12.9 (Verhältnis 2 und 3); nur Eingänge bis ±10 V/3 unverzerrt.
- S. 205: Satz zur Begrenzung bei Gegenkopplung; nichtinvertierender Verstärker Bild 12.10, Gl. 12.5 $A = 1 + R_2/R_1$, $A > 1$, positiv;
  Vergleich invertierend/nichtinvertierend; Addierer mit drei Eingängen.
- S. 206: Bild 12.11, $U_A = -\sum R_4/R_i\,U_i$; Subtrahierer Bild 12.12, Superposition.
- S. 207: $U_{A1} = -R_2/R_1\,U_{E1}$; $U_{A2}$; Gl. 12.6; Gl. 12.7 mit $R_1 = R_3$, $R_2 = R_4$; Integrator mit Kondensatorgleichung.
- S. 208: Integrator $U_A = -\frac{1}{RC}\int U_E\,dt$ (Bild 12.13); Differenzierer $U_A = -RC\,dU_E/dt$ (Bild 12.14).
- S. 209: Logarithmierer (Bild 12.15) $U_A = -U_T\ln(U_E/(R I_S))$; Exponentialfunktion (Bild 12.16) $U_A = -R I_S \exp(U_E/U_T)$; Transistor und
  Temperaturkompensation; Herkunft des Namens.
- S. 210: Multiplikation über Logarithmen (Bilder 12.17, 12.18); Impedanzwandler $U_A = U_E$, unendlicher Eingangswiderstand,
  Messgerät.
- S. 211: Bild 12.19; 12.6 NIC: $U_1 = U_2$, $I_1 = -I_2$, $R_E = -R_2$; Kompensation des Innenwiderstands einer Stromquelle;
  Transimpedanzverstärker, niedriger Eingangswiderstand, Fotodiode.
- S. 212: $U_a = -I_e R$; (12.7 realer OPV → 12/03); 12.8 Einleitung.
- S. 213: Bild 12.20 über Potentiale (Subtrahierer); Kaskade Bild 12.21, $U_A = U_E \cdot R_4/R_3 \cdot R_2/R_1$.
- S. 214: Produkt der Übertragungsfunktionen; Rechenschema Bild 12.22; 12.9 Zusammenfassung.

**Fehler und Ungenauigkeiten des Skripts:**
1. S. 207: Zwischenschritt $\Phi_+ = U_{E2}\,R_3/(R_3 + R_4)$ — am Pluseingang liegt die Spannung an $R_4$, also $U_{E2}\,R_4/(R_3 + R_4)$; Gl. 12.6
   enthält richtig $R_4/(R_3 + R_4)$. Tippfehler.
2. S. 213: Endformel der Beispielschaltung 1, $U_2 \cdot \frac{R_1 + R_2}{R_3 + R_4} \cdot \frac{R_4}{R_3} - U_1 \frac{R_2}{R_1}$ — in einem Nenner steht
   $R_3$, wo $R_1$ stehen müsste; richtig (wie Gl. 12.6) $U_2 \cdot \frac{R_1 + R_2}{R_1} \cdot \frac{R_4}{R_3 + R_4} - U_1\frac{R_2}{R_1}$. Die Zeile
   davor ist richtig; solange $R_3 = R_1$ ist, fällt der Fehler nicht auf; bei 1/2/3/4 kΩ mit $U_2$ = 1 V und $U_1$ = 0: 1,714 V statt
   0,571 V.
3. S. 210: Multiplizierer Bild 12.18 — mit den gezeichneten Stufen ergibt sich $U_A = -U_X U_Y/(R_L I_S)$; der Maßstab $1/(R_L I_S)$ ist
   riesig (6,9·10⁹ 1/V mit 10 kΩ und der Beispieldiode): 1 mV an beiden Eingängen ergäbe −6862 V. Brauchbar wird die Schaltung erst mit einer
   Referenz (dritter Logarithmierer, über einen Umkehrer in den Addierer, also abgezogen); einen solchen festen Maßstab haben auch
   integrierte Multiplizierer (AD633: XY/10 V), die allerdings mit einer translinearen Zelle ohne getrennte Logarithmierer arbeiten und
   alle vier Quadranten verarbeiten. Die Schaltung hier arbeitet nur mit positiven Eingängen. Präzisieren.
4. S. 211: NIC — „Wir wissen $U_1 = U_2$“ setzt voraus, dass die Gegenkopplung überwiegt; die Schaltung ist zugleich mitgekoppelt (über den
   Widerstand zum Pluseingang). Stabil nur, solange der Widerstand am Pluseingang (Quelle und Last parallel) kleiner ist als $R_2$; ohne
   Last ist der Kompensationsfall genau der Grenzfall. „R_2 = R_S“ ist ein Tippfehler für $R_q$.
5. S. 205: „Wenn die Versorgungsspannung kleiner ist als die größtmögliche Ausgangsspannung, ist das Ausgangssignal durch die
   Versorgungsspannung begrenzt“ — gemeint: Wenn die rechnerische Ausgangsspannung die Aussteuergrenze übersteigt; begrenzt wird bei
   $U_{A,\max}$, etwas unter der Versorgung (±14 V an ±15 V). Präzisieren.
6. S. 208: Integrator und Differenzierer mit Großbuchstaben für zeitabhängige Größen und gemischt ($U_C$, $u_C(t)$); nach DIN Momentanwerte
   klein. Notationshinweis.
7. S. 209: „Den mathematischen Funktionen verdankt der OPV seinen Namen“ — richtig; der Satz zur Geschichte ist sprachlich verunglückt.
   Kein fachlicher Fehler.

## 11. Faktencheck (22.10.2026)

Prüfung durch einen unabhängigen Agenten gegen Skript, Zahlenwerk und Fachquellen: 3 Fehler, 18 Ungenauigkeiten; alle nachgerechnet
und eingearbeitet.

- **F1** Endliches $v_D$: 10 µV sind der 200 000ste Teil von 2 V ($U_A/v_D$), nicht ein Hunderttausendstel.
- **F2** Subtrahierer: Bedingung ist $R_4/R_3 = R_2/R_1$ (z. B. $R_3 = R_1$, $R_4 = R_2$), nicht nur die Gleichheit; Umformung im
  Kasten über $(1 + R_2/R_1)\cdot(R_2/R_1)/(1 + R_2/R_1)$.
- **F3** AD633 multipliziert nicht über Logarithmen (translinearer Vierquadranten-Multiplizierer); gemeinsam ist nur der Maßstab
  XY/10 V.
- **Ungenauigkeiten:** Beschreibung der Skriptkorrektur S. 213 ($R_3$ statt $R_1$ in einem Nenner; Werte für $U_2$ = 1 V, $U_1$ = 0);
  Differenzierer am realen OPV schwingt (12,6 kHz, Güte 79; 1 kΩ in Reihe dämpft und begrenzt auf 10), Abbildung als idealer OPV
  gekennzeichnet; Transimpedanzverstärker: Ruhestrom 80 nA überdeckt kleine Fotoströme, FET-Eingang; 310-K-Kennlinie steiler
  (61,5 mV je Dekade), Verschiebung 21–27 mV; Ein-Satz-Prinzip (Eingangs- und Rückkopplungszweig, stromlose Eingänge als Eigenschaft
  des idealen OPV); Tabellenzeile Integrator/Differenzierer; Polung der Dioden in den Bildbeschreibungen; Referenz des Multiplizierers
  über einen Umkehrer; Offset ±1 mV am Impedanzwandler (4,991–4,993 V); Integrator mit 1 MΩ parallel: rund 0,1 V aus dem Offset,
  80 mV aus dem Ruhestrom (0,8 V/s ohne Widerstand); $u_A(0)$ als Ausgangsspannung zur Zeit null; Transistor im Logarithmierer
  verbessert die Exponentialtreue, Temperaturgang braucht zweiten Transistor und temperaturabhängige Verstärkung; Umkehrung
  Logarithmierer/Exponentialschaltung nur mit Umkehrer dazwischen; Verweis auf den Abschnitt *Der ideale Operationsverstärker*;
  Liste der ausführlichen Inhalte; Akteure des Integrators; „Widerstand zum Plus- bzw. Minuseingang“ im NIC-Kasten; zweiter
  Rechenweg des Subtrahierers über Potentiale (Skript 12.8) im Herleitungskasten.
