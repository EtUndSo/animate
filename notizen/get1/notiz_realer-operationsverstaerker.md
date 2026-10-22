# Arbeitsnotiz: Der reale Operationsverstärker (ET1 Kap. 12.7), Stil 3

Skript S. 212 (PDF 218), Abschnitt 12.7 „Nicht-Idealer Operationsverstärker und reale Bauteile“: endliche Verstärkung
$v_\mathrm{real}$ = 10⁵ … 10⁶, Ausgang zwischen $U_{A,\min}$ und $U_{A,\max}$, Offsetspannung (Definition, Mismatching, Abhängigkeit von
Temperatur, Betriebsspannung und Zeit), Gleichtaktunterdrückung CMRR in dB (60 bis 120 dB). Dazu S. 198/199: reale Einflüsse
lassen sich zum idealen OPV „hinzufügen“; Exemplarstreuung, Temperatur, Verringerung der Verstärkung bei höheren Frequenzen;
Halbleiterbauelemente zwischen Ausgang und Versorgung. 12/01 und 12/02 verweisen ausdrücklich hierher: Werte der
Gleichtaktunterdrückung realer OPVs, Frequenzkompensation, Überschwingen bei großem $k$, Ruhestrom, Verfälschung der
Grundschaltungen. Der Skriptabschnitt ist kurz; Ruheströme, Frequenzgang und Anstiegsgeschwindigkeit ergänzt das Thema nach
Datenblatt (LM741) und Fachliteratur.

## 1. Ein-Satz-Prinzip

Ein realer OPV ist ein idealer mit kleinen Fehlerquellen: Fehler im Verstärker teilt die Gegenkopplung durch die
Schleifenverstärkung, Fehler an den Eingängen verstärkt sie wie ein Signal; weil die Schleifenverstärkung mit der Frequenz
fällt, wirkt die Gegenkopplung nur bis zu einer Grenzfrequenz, und große Signale begrenzen zusätzlich Aussteuerbereich und
Anstiegsgeschwindigkeit.

## 2. Schwierigkeit und Längenspannen

Jede einzelne Abweichung ist ein Mechanismus mittlerer Tiefe, zusammen aber breit, mit drei Kipp-Stellen (Rauschverstärkung,
Bandbreite, Anstiegsgrenze). Deshalb die Spannen von „schwer“: kompakt 1800–2800 Wörter, ausführlich 3500–5000 Wörter; Ziel
kompakt etwa 2300, ausführlich etwa 3900.

## 3. Vorwissen-Kette

- Leerlaufverstärkung, Ausgangsgrenzen, linearer Bereich ±70 µV, Offsetspannung als Begriff: 12/01 *Der ideale
  Operationsverstärker* → erinnern, verlinken.
- Rückkopplungsfaktor $k$, Schleifenverstärkung, $A = v_D/(1 + k v_D)$: 12/01 *Der Ruhezustand* → erinnern, verlinken.
- Modell $dU_A/dt = \omega_T U_D$, $f_T$, Anstiegsgeschwindigkeit 0,5 V/µs (15 µA in 30 pF), Einschwingen $\tau = 1/(k\omega_T)$,
  Frequenzkompensation: 12/01 *Warum die Schaltung zur Ruhe kommt* → erinnern, verlinken.
- Differenzverstärker, Gleichtaktspannung, Fußpunktstromquelle: 12/01 *Der Differenzverstärker* → erinnern; CMRR hier aufbauen.
- Dezibel mit 20 lg für Spannungsverhältnisse: 12/01 *Rauschen und Signal-Rausch-Verhältnis* → erinnern.
- Grundschaltungen (invertierend, nichtinvertierend, Folger, Integrator): 12/02 → erinnern, verlinken.
- Transfergleichung, Basisstrom $I_C/B$: 11/01; Early-Effekt, $r_{CE}$: 11/03 → erinnern.
- Überlagerungsprinzip: 07/03 → erinnern, verlinken.
- Ableitung des Sinus, Additionstheorem (Sinus plus Kosinus): Schulmathematik → im Kasten benutzen.
- Hier aufbauen: Ersatzschaltbild des realen OPV, zwei Arten von Fehlern, Rauschverstärkung, Offset (Ursache, Wirkung, Drift,
  Abgleich), Ruheströme und Kompensationswiderstand, CMRR und SVRR, Frequenzgang und Verstärkungs-Bandbreite-Produkt,
  Überschwingen, Leistungsbandbreite, Aussteuergrenzen.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Gelten die goldenen Regeln für einen realen OPV überhaupt noch?“ → Was am realen OPV anders ist → Text → beide.
2. „Warum wird der Fehler durch die endliche Verstärkung bei großer Verstärkung der Schaltung größer?“ → Endliche
   Leerlaufverstärkung → Text → beide.
3. „Beim Umkehrer mit A = −1 wird der Offset doch gar nicht verstärkt?“ (Fehlvorstellung) → Offsetspannung →
   Fehlvorstellungs-Kasten → beide.
4. „Warum ändert sich der Offset mit der Temperatur?“ → Offsetspannung → Frage-Kasten → beide.
5. „Kann man den Offset nicht einfach abgleichen?“ → Offsetspannung → Frage-Kasten → beide.
6. „Durch 2 MΩ Eingangswiderstand bei Mikrovolt Differenzspannung sollen 80 nA fließen?“ (Fehlvorstellung) →
   Eingangsruheströme → Text → beide.
7. „Warum hilft ein zusätzlicher Widerstand am Pluseingang, durch den doch auch Ruhestrom fließt?“ → Eingangsruheströme →
   Text (Schritte) → beide.
8. „Am Spannungsfolger liegt doch keine Differenz an, wie soll da Gleichtakt stören?“ (Fehlvorstellung) → Gleichtakt →
   Fehlvorstellungs-Kasten → ausführlich.
9. „Warum ist die Gleichtaktunterdrückung nicht unendlich, wenn die Stromquelle die Summe festhält?“ → Gleichtakt →
   Frage-Kasten → ausführlich.
10. „Der 741 hat 1 MHz Transitfrequenz, also verstärkt er Signale bis 1 MHz.“ (Fehlvorstellung) → Frequenzgang →
    Fehlvorstellungs-Kasten → beide.
11. „Bleibt der kleine Ausgangswiderstand auch bei hohen Frequenzen?“ → Endliche Leerlaufverstärkung → Frage-Kasten →
    ausführlich.
12. „Warum schwingt der Spannungsfolger über, wenn das Modell kein Überschwingen kennt?“ → Frequenzgang → Frage-Kasten →
    ausführlich.
13. „Liegt das Signal in der Bandbreite, wird es doch unverzerrt übertragen?“ (Fehlvorstellung) → Anstiegsgeschwindigkeit →
    Text (Schritte) und Quiz → beide.
14. „Warum erreicht der Ausgang die Versorgungsspannung nicht?“ → Aussteuergrenzen → Text → beide.
15. „Was passiert, wenn die Eingänge den Gleichtaktbereich verlassen?“ → Aussteuergrenzen → Text → ausführlich.

## 5. Kipp-Stellen

**K1 Offset und Rauschverstärkung.** Schritte (invertierender Verstärker 10 kΩ/20 kΩ, Eingang 0 V): (1) Offset als Quelle vor
dem Pluseingang, Pluseingang auf 1 mV; (2) Gegenkopplung hält den Minuseingang ebenfalls auf 1 mV; (3) durch $R_1$ fließen
0,1 µA zur Quelle; (4) sie kommen über $R_2$ vom Ausgang, 2 mV Abfall, Ausgang 3 mV; (5) für die Offsetquelle ist die Schaltung
nichtinvertierend: Rauschverstärkung $1 + R_2/R_1$ = 3, nicht −2. Abbildung 03-offset (Ursache und Wirkung). Zahlen: 4 % $I_S$
→ 1,01 mV; A = −100 → 101 mV; Umkehrer → 2 mV. Herleitung über Überlagerung. Beispiel: Thermoelement Typ K, 1 mV ≙ 24,4 K.

**K2 Bandbreite.** Schritte: (1) OPV integriert, Leerlaufverstärkung $f_T/f$ ab 5 Hz; (2) Schleifenverstärkung $k f_T/f$ sinkt;
(3) solange groß, gilt $1/k$; (4) bei $f = k f_T$ ist sie 1, Differenzspannung und Rückführung gleich groß und um eine
Viertelperiode verschoben → 0,707; (5) darüber folgt die Schaltung $f_T/f$. Abbildung 03-frequenzgang (doppeltlogarithmisch).
Zahlen: 1/k = 10 → 100 kHz, 1/k = 100 → 10 kHz; A = −100 bei 20 kHz nur 44. Herleitung: Modell + Sinusansatz +
Additionstheorem. Beispiel: Audioverstärker ein- und zweistufig.

**K3 Anstiegsgrenze.** Schritte: (1) größte Steigung eines Sinus $2\pi f \hat U$; (2) darunter begrenzt nur die Bandbreite;
(3) darüber liefert die Eingangsstufe ihren ganzen Strom (im Modell ab 80 mV, real allmählich), Ausgang steigt mit SR; (4) Dreieck, höchstens SR mal Viertelperiode
(6,25 V), Simulation 6,0 V; (5) Grenze hängt von der Amplitude ab: bis 0,8 V Bandbreite, darüber Anstieg. Abbildung 03-anstieg.
Herleitung: Ableitung des Sinus. Beispiel: 1/k = 10 mit 0,05 V/20 kHz, 1 V/5 kHz, 1 V/20 kHz.

## 6. Aussortier-Liste

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Ersatzschaltbild: idealer OPV plus Quellen und Widerstände (Skript S. 198 „hinzufügen“) | K | Text + Abbildung | dito |
| Tabelle ideal gegen Beispiel-OPV (typisch, garantiert) | K | Tabelle | Tabelle |
| zwei Arten von Fehlern (im Verstärker / an den Eingängen) | K | Text | Text + Abbildung + Analogie |
| Verstärkungsfehler $1/(1 + k v_D)$, beide Schaltungen mit demselben $k$ | K | Formel + Herleitung | dito + Beispiel |
| Unempfindlichkeit gegen Schwankungen von $v_D$ | H | 1 Satz | im Beispiel |
| Ausgangswiderstand $R_a/(1 + k v_D)$, Eingangswiderstand $R_e(1 + k v_D)$ | H | 1 Satz | Text |
| Ausgangswiderstand wächst mit der Frequenz | V | – | Frage-Kasten |
| Aussteuergrenzen Ausgang (±14/±13 V, Kurzschlussstrom 25 mA) | K | Text | Text + Abbildung |
| Gleichtakt-Eingangsbereich ±13 V, Folgen beim Überschreiten | H | 1 Satz | Text |
| Rail-to-Rail-OPVs | V | – | 1 Satz |
| Offsetspannung: Definition, Ursache ($I_S$-Unterschied) | K | Text | Text + Abbildung |
| Offset mal Rauschverstärkung, auch invertierend | K | Schritte + Formel + Herleitung + Beispiel | dito |
| Offsetdrift 3,3 µV/K je mV; Versorgung; Lebensdauer | H | Frage-Kasten | Frage-Kasten |
| Offsetabgleich (Anschlüsse 1 und 5, ±15 mV), Präzisions- und Chopper-OPVs | H | Frage-Kasten | Frage-Kasten |
| Ruheströme als Basisströme; $I_B$, $I_{os}$; nicht durch $R_e$ | K | Text | Text |
| Wirkung $R_2 I_{B-}$, Kompensation $R_3 = R_1 \parallel R_2$, Rest $R_2 I_{os}$ | K/H | Schritte + Formel + Herleitung | dito + Abbildung + Beispiel |
| FET-Eingang: Pikoampere, Verdopplung je 10 K; interne Ruhestromkompensation | V | – | im Beispiel bzw. Kasten-Grenzen |
| CMRR: Definition, dB, Praxiswerte, 741: 95 dB | K | Formel + Text | dito |
| Gleichtakt wirkt wie $U_{Gl}/\mathrm{CMRR}$; wann er zählt | K | Formel + Herleitung | dito + Beispiel |
| Ursache endlicher CMRR ($r_{CE}$ der Fußpunktquelle, Unsymmetrie) | V | – | Frage-Kasten |
| SVRR 96 dB, 16 µV/V | H | 1 Satz | Text |
| Frequenzgang $v_D(f)$, Eckfrequenz 5 Hz | K | Text + Abbildung | dito |
| Grenzfrequenz $k f_T$, Verstärkungs-Bandbreite-Produkt | K | Schritte + Formel + Herleitung + Beispiel | dito |
| Zusammenhang mit $\tau = 1/(k\omega_T)$ | H | 1 Satz | 1 Satz |
| Überschwingen 5 % als Folger, zweite Verzögerung, Kompensation | H/V | – | Frage-Kasten |
| Anstiegsgeschwindigkeit, Leistungsbandbreite, Dreieck | K | Schritte + Formel + Herleitung + Beispiel | dito |
| Rauschen mal Rauschverstärkung | H | Halbsatz | 1 Satz mit Zahl |
| OPV-Auswahl nach dem maßgeblichen Fehler | H | 1 Satz | Bedeutung |
| Messung der Offsetspannung, Ersatzschaltbild für Wechselgrößen, Phasenreserve als Zahl | S | – | – |

## 7. Abbildungsplan (Szene-IDs get1/operationsverstaerker/03-…)

| ausf. | komp. | Szene · Vorlage | Inhalt | Kernaussage |
|---|---|---|---|---|
| 1 | 1 | 03-ersatzschaltbild · schaltplan | idealer OPV mit $v_D$ = 200 000 (ab 5 Hz fallend), 0,5 V/µs; außen $U_{os}$ = 1 mV, 2 × 80 nA, $R_e$ = 2 MΩ, $R_a$ = 75 Ω; Grenzen ±14 V, ±13 V, 95 dB | wo eine Abweichung sitzt, entscheidet, was die Gegenkopplung mit ihr macht |
| 2 | – | 03-fehlerorte · schaltung-zustaende | 1/k = 10 (10 kΩ/90 kΩ): (a) $v_D$ 200 000 → 50 000 ändert A von 9,9995 auf 9,998; $R_a$ 75 Ω wirkt wie 3,75 mΩ; (b) $U_{os}$ = 1 mV → 10 mV am Ausgang | innen geteilt, am Eingang verstärkt |
| 3 | – | 03-aussteuerung · schaltung-und-kennlinie | (a) Gegentakt-Emitterfolger mit Spannungsabfällen; (b) Bereiche: Versorgung ±15 V, Ausgang ±14/±13 V, Eingänge ±13 (±12) V | zwischen Signal und Versorgung liegen Transistorstrecken |
| 4 | 2 | 03-offset · schaltung-und-kennlinie | (a) $I_C(U_{BE})$ halblogarithmisch, zwei Transistoren mit 4 % verschiedenem $I_S$, 1,01 mV Versatz; (b) invertierender Verstärker 10 kΩ/20 kΩ, Offsetquelle, Ausgang 3 mV, umgezeichnet als nichtinvertierender | Offset wird mit der Rauschverstärkung verstärkt |
| 5 | 3 | 03-ruhestroeme · schaltung-strompfade | 100 kΩ/1 MΩ: (a) ohne $R_3$ 80 mV; (b) mit $R_3$ = 90,9 kΩ: Pluseingang −7,27 mV, 72,7 nA durch $R_1$, 7,27 nA durch $R_2$, Ausgang 0 (±20 mV mit $I_{os}$) | gleiche Ströme an gleichen Widerständen heben sich auf |
| 6 | 4 | 03-gleichtakt · schaltung-zustaende | (a) Folger an 10 V: 10 V Gleichtakt ≙ 0,18 mV; (b) invertierender Verstärker: Eingänge auf 0 V; (c) Skala 60–120 dB mit Faktoren, 95/80 dB (741), 61 dB (Subtrahierer 1 %) | Gleichtakt wirkt wie eine kleine Differenzspannung, nur wo die Eingänge mitlaufen |
| 7 | 5 | 03-frequenzgang · kennlinie-loglog | $v_D(f)$ und Schaltungsverstärkung für 1/k = 1, 10, 100, 1000 über 1 Hz–10 MHz; Abstand = Schleifenverstärkung | Bandbreite endet, wo die Schleifenverstärkung 1 wird |
| 8 | 6 | 03-anstieg · zeitverlauf | 1/k = 10: (a) 0,05 V/20 kHz → 0,49 V Sinus; (b) 1 V/5 kHz → 9,99 V Sinus; (c) 1 V/20 kHz → Dreieck ±6,0 V | Bandbreite begrenzt kleine, Anstiegsgeschwindigkeit große Signale |

Kompakt 6, ausführlich 8. Geprüft gegen §7.2: jede Kipp-Stelle mit Abbildung, jede Schaltung mit Schaltbild, Einstieg in beiden.

## 8. Zahlenwerk

`notizen/get1/zahlen_opv.py`, Abschnitt „Thema 03“, `bericht_real()`; neue Datenblattwerte (LM741: $U_{os}$ max 5 mV, Abgleich
±15 mV, $I_{os}$ 20/200 nA, $I_B$ max 500 nA, $R_e$ min 0,3 MΩ, CMRR 95/80 dB, SVRR 96/86 dB, Eingangsbereich ±13/±12 V,
±13 V an 2 kΩ, 25 mA, Folger 0,3 µs und 5 %; µA741: $R_a$ 75 Ω), Thermoelement Typ K 4,096 mV bei 100 °C; Funktionen
`a_real`, `zweipol_sprung`, `ua_ruhestrom`; Simulationen mit `sim` (Anstiegsgrenze) und dem Zweipolmodell (Überschwingen).

## 9. Profi-Abgleich

- Texas Instruments, LM741 Operational Amplifier, Datenblatt SNOSC25D: https://www.ti.com/lit/ds/symlink/lm741.pdf — alle
  typischen und garantierten Werte des Beispiel-OPV, Innenschaltbild (Offset-Anschlüsse an den Emitterwiderständen des
  Stromspiegels), Überschwingen 5 % als Folger.
- Analog Devices, Tutorial MT-039 „Op Amp Total Output Offset Voltage Calculations“: https://www.analog.com/MT-039 — Offset und
  Ruhestromfehler auf den Eingang bezogen, mit der Rauschverstärkung $1 + R_2/R_1$ auf den Ausgang umgerechnet;
  Kompensationswiderstand $R_1 \parallel R_2$, nicht bei OPVs mit interner Ruhestromkompensation.
- Ergänzend: TI µA741-Datenblatt (Ausgabe 2018) für den Ausgangswiderstand 75 Ω; Drift $U_{os}/T$ eines Differenzpaars mit
  $I_S$-Unterschied nach Gray/Meyer, „Analysis and Design of Analog Integrated Circuits“ (Offsetdrift des Emitter-gekoppelten
  Paars).
- Ergebnis: Das Prinzip „innen geteilt, am Eingang mit der Rauschverstärkung verstärkt“ ist die Standardsicht der
  Herstellerliteratur; Zahlen wie im Zahlenwerk.

## 10. Skript-Abgleich

**Inhalte des Quellabschnitts (Vollständigkeit):**
- S. 198: reale Einflüsse lassen sich zum idealen OPV hinzufügen, etwa endliches $v_D$; endliche Verstärkung, Ausgangshub von
  $U_{a,\min}$ bis $U_{a,\max}$, darüber Sättigung; Störfaktoren: Exemplarstreuung, Temperatur, Verringerung der Verstärkung bei
  höheren Frequenzen.
- S. 199: zwischen Ausgang und Versorgung liegen Halbleiterbauelemente, an denen Spannung abfällt.
- S. 212: reale Verstärkung $v_\mathrm{real}$ = 10⁵ … 10⁶; Ausgang zwischen $U_{A,\min}$ und $U_{A,\max}$; Offsetspannung als
  Eingangsspannung bei Ausgang null, Ursache „Mismatching“, abhängig von Temperatur, Betriebsspannung und Langzeitverhalten;
  quantitative Behandlung in Schaltungstechnik 1 und 2; CMRR als Gütekriterium in dB, ideal unendlich, Praxis 60 dB (b = 10⁻³)
  bis 120 dB (b = 10⁻⁴), wichtig bei kleinen Signalen.

**Fehler und Ungenauigkeiten des Skripts:**
1. S. 212: „120 dB (b = 10⁻⁴)“ — 120 dB entsprechen 10⁻⁶; 10⁻⁴ sind 80 dB. 60 dB = 10⁻³ stimmt. $b$ ist nicht definiert, gemeint
   ist offenbar der Kehrwert $v_{Gl}/v_D$.
2. S. 212: CMRR sage aus, wie eine „Instabilität der Eingangsspannung im Gleichtaktbetrieb“ übertragen wird — gemeint ist eine
   Gleichtaktspannung (bzw. deren Änderung), etwa eine Störung auf beiden Leitungen; mit Stabilität hat die Größe nichts zu tun.
   Präzisieren.
3. S. 212: Offset-Definition „Lässt man die Eingangsspannung variabel und setzt die Ausgangsspannung zu Null“ — gemeint: die
   Differenzspannung, die man anlegen muss, damit der Ausgang null wird. Sprachlich präzisieren, kein fachlicher Fehler.
4. S. 212: $v_\mathrm{real}$ = 10⁵ … 10⁶ sind typische Werte; garantiert sind beim 741 nur 5·10⁴ (über den Temperaturbereich
   2,5·10⁴). Ergänzen.
5. Abschnitt 12.7 nennt weder Ruheströme noch Bandbreite oder Anstiegsgeschwindigkeit, obwohl S. 198 die frequenzunabhängige
   Verstärkung ausdrücklich zu den Idealisierungen zählt. Ergänzung, kein Fehler.

## 11. Faktencheck (22.10.2026)

Unabhängige Prüfung durch einen zweiten Agenten (erster Versuch an einem Verbindungsfehler abgebrochen, zweiter vollständig):
2 Fehler, 17 Ungenauigkeiten, keine Rechenfehler; alle nachgeprüft und eingearbeitet.

- **F1** Betriebsspannungsunterdrückung: Der Gleichspannungswert 96 dB galt im Beispiel für 100-Hz-Brummen. Die Unterdrückung
  fällt mit der Frequenz (Analog Devices MT-043: ab der Eckfrequenz der Leerlaufverstärkung, Abschätzung bei 100 Hz rund
  70 dB, also etwa 20-mal schlechter). Beispiel jetzt mit einer langsamen Änderung (Batterie), Brummen qualitativ mit
  Abblockkondensator.
- **F2** „Reale OPVs bleiben unter 110 dB“ falsch; Präzisions-OPVs erreichen 120 dB und mehr (OP177, AD8628). Jetzt auf den
  741 (95 dB) bezogen.
- **Ungenauigkeiten:** 80 mV und 15 µA als Modellwerte der Anstiegsgrenze gekennzeichnet; Vorzeichen der Offsetquelle gegen die
  Skriptdefinition; Thermoelement-Quiz nur nichtinvertierend; Koppelkondensator in Reihe zu R_1 statt am Eingang;
  „Leistungsbandbreite“ nur für die volle Ausgangsamplitude (14 V, 5,68 kHz), allmählicher Beginn der Verzerrung;
  Additionstheorem im Frequenzgang-Kasten ausgeführt; typische Werte nicht als Grenzen (±12 V garantiert, Kurzschlussstrom
  typisch); Quellen der Tabelle (75 Ω und 1 MHz aus µA741-Datenblättern, Eingangswiderstand und Abgleichbereich für
  ±20 V); CMRR mit Betrag, Gleichtaktbeitrag mit ±; Formel für die Ausgangsamplitude nur nichtinvertierend; Eckfrequenz
  5 Hz gerundet (141 000); Zuschreibungen ans Skript (S. 198 „hinzufügen“, S. 212 Schaltungstechnik nur für den Offset);
  „Sättigungsstrom“ wie in 11/01; Superlativ beim Folger; Inhaltsangabe der ausführlichen Fassung; Verweise auf Abschnitte,
  die es nur in der ausführlichen Fassung von 12/01 gibt, jetzt dorthin verlinkt; Lupe in Abbildung 03-offset.
- **Eigene Selbstprüfung dazu:** zeitabhängige Größen in zwei Herleitungen klein geschrieben, zu breite Formel geteilt,
  Begriffe vor der Tabelle kurz erklärt, Satz zur Betriebsspannung aus einem Deutungsabsatz gelöst, Tabellen mit weichen
  Trennstellen auf Handybreite.
