# Arbeitsnotiz: Von der Röhre zum integrierten Schaltkreis (ST1 Einführung), Stil 3

Erstes ST1-Thema, 22.10.2026. Dateien: `content/st1/01-einfuehrung/01-geschichte-der-schaltungstechnik.md` (kompakt) und
`…-ausfuehrlich.md`. Frontmatter aus `notizen/st1/themenplan.md`: title „Von der Röhre zum integrierten Schaltkreis“,
pfad `Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Einführung`, order 33010100, tags Elektronenröhre, Transistor,
integrierte Schaltung, Mooresches Gesetz, CMOS. Zahlen: `notizen/st1/zahlen_einfuehrung.py` → `.txt`.

Quelle: Skript PDF S. 9–14 (gedruckt 1–6), Abschnitt 1.1; aus 1.2 (sonst entfallen) nur die Sachaussage zur Steuerung
(FET wie Röhre rein kapazitiv gesteuert, Bipolartransistor braucht Eingangsstrom; beide als spannungsgesteuerte
Stromquelle behandelt).

## 1. Ein-Satz-Prinzip

**Jede elektronische Schaltung beruht auf einem gesteuerten Ventil, in dem eine kleine Steuergröße einen großen Strom
aus einer Versorgung steuert; die Geschichte der Schaltungstechnik ist die Geschichte, dieses Ventil kleiner,
sparsamer und schneller zu machen, bis Milliarden davon gemeinsam auf einem Siliziumchip entstehen und jedes einzelne
fast nichts mehr kostet.**

Jeder Meilenstein ist eine Seite davon: Triode (erstes Ventil, Feldsteuerung), Rückkopplung und Überlagerung (was man
mit Ventilen baut), Transistor (Ventil ohne Heizung), Silizium und Planartechnik (Ventile und Verdrahtung in denselben
Prozessschritten), MOSFET (Feldsteuerung wie die Röhre), CMOS (Ventilpaare ohne Ruhestrom), Mooresches Gesetz (Folge
des gemeinsamen Herstellens und Verkleinerns), Funk-SoC (gleiche Ventile auf einem Chip gleichen sich genau).

## 2. Schwierigkeit und Längenspannen

**schwer (nach Umfang).** Kein einzelner schwerer Mechanismus, aber drei Kipp-Stellen und acht Mechanismen
(Raumladungssteuerung, Rückkopplung, Mischung, Leckstrom/Oxid, Planartechnik, Umladeleistung, exponentielles Wachstum,
Skalierung) mit zwölf Formeln, dazu die ganze Geschichte des Quellabschnitts. Zunächst als „mittel“ geplant; beim
Schreiben zeigte sich, dass schon die Pflichtinhalte über 5000 Wörter ausführlich tragen. Spannen (ERKLAER_PROMPT §3.3):
kompakt 1800–4000 Wörter, ausführlich 3500–7000. Ergebnis: kompakt 4260, ausführlich 6825 Wörter Hauptpfad (nach dem
Streichen von Doppelungen; die FET-Fehlvorstellung wurde in den Geschichtsabsatz integriert, weil sie ihn wiederholte).
Die kompakte Fassung liegt leicht über der Spanne, weil Begriffserklärungen (§5.1) und die Korrekturen der
Faktenprüfung hinzukamen; weiter kürzen ließe sie sich nur durch Weglassen von Kerninhalt.

## 3. Vorwissen-Kette

- Strom, Spannung, Leistung P = U I, Widerstand: Schulphysik bzw. ET1 Kap. 5 (nur erinnern).
- Kondensator Q = C U und Energie ½ C U²: [Der Kondensator und seine Kapazität] verlinken; die Energie leite ich im
  CMOS-Kasten selbst her (ein Schritt).
- Elektronen, Feld, Potential: Schulphysik; Feld zieht negative Ladung zum höheren Potential.
- Halbleiter, Eigenleitungsdichte n_i, Dotierung: [Halbleiter und das Bändermodell] verlinken; I_S ∝ n_i² aus [Die
  Diode und ihre Kennlinie] in einem Satz erinnern.
- Bipolartransistor, Basisstrom: [Der Bipolartransistor – Aufbau und Wirkungsweise] verlinken (Steuerung über U_BE,
  Basisstrom als Begleiterscheinung).
- Gegenkopplung beim OPV: [Der Operationsverstärker – idealer OPV und Rückkopplung] verlinken (A = v_D/(1 + k v_D)).
- Produkt zweier Kosinus: Additionstheoreme (Schulmathematik); ausführlicher in [Schwebung und das Produkt zweier
  Sinussignale]. Im Kasten selbst hergeleitet.
- Exponentialfunktion, Logarithmus: Schulmathematik.
- Hier aufbauen: Ventilprinzip, Raumladung, Durchgriff, Steilheit, Innenwiderstand, Rückkopplung als Schleife,
  Mischung, Zwischen- und Spiegelfrequenz, Planartechnik, Fotolithografie, MOSFET-Prinzip (nur Steuerung), CMOS,
  Umladeleistung, Verdopplungszeit, Technologieknoten, Skalierung, Transitfrequenz, Direktumsetzer, SoC.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Wie kann eine kleine Spannung am Gitter einen großen Strom steuern?“ → Röhre, Schrittfolge (Text) → beide.
2. „Woher kommt die zusätzliche Leistung, macht der Verstärker Energie?“ (Fehlvorstellung) → Kasten nach Schritt 5,
   Zahl: Heizung 0,945 W + 0,44 W Gleichleistung gegen 0,19 mW Signal → beide.
3. „Warum muss die Kathode geheizt werden?“ → Frage-Kasten (Glühemission, rund 1000 K) → beide.
4. „Warum ist das Gitter negativ?“ → Text, Schritt 4 → beide.
5. „Warum schwingt ein rückgekoppelter Verstärker ohne Eingangssignal?“ → Text Rückkopplung (Rauschen als Anstoß,
   Begrenzung durch Nichtlinearität) → beide.
6. „Warum mischt man auf eine Zwischenfrequenz, statt direkt zu filtern?“ → Text, Güte 500 gegen 53,5 → beide.
7. „Landet beim Mischen nicht auch ein zweiter Sender auf der ZF?“ → ausführlich Text (Spiegelfrequenz 121,4 MHz),
   kompakt Frage-Kasten.
8. „Warum hat der Transistor die Röhre verdrängt?“ → Text, 275 MW Heizleistung gegen 65 W → beide.
9. „Warum Silizium statt Germanium?“ → Text (Oxid, n_i², 4 Mio.) → beide; „Warum waren die ersten Transistoren dann
   aus Germanium?“ → Frage-Kasten ausführlich.
10. „Eine integrierte Schaltung ist doch nur eine winzige Platine mit Einzelteilen.“ (Fehlvorstellung) → Kasten
    ausführlich; kompakt im Text (ein Satz in der Planartechnik).
11. „Warum wird ein Transistor billiger, wenn man ihn kleiner macht?“ → Text, Kipp-Stelle 2 → beide.
12. „Stimmt es, dass sich die Transistorzahl alle 18 Monate verdoppelt?“ (Fehlvorstellung) → Kasten, 2,33·10¹⁰ statt
    2,91·10⁸ → beide.
13. „Ist das Mooresche Gesetz ein Naturgesetz?“ (Fehlvorstellung) → Text Moore + Quiz → beide.
14. „Der FET ist doch eine Weiterentwicklung des Bipolartransistors.“ (Fehlvorstellung) → im Text beider Fassungen
    (Idee 1925, Oberflächenzustände, gebaut 1959; ausführlich mit dem Satz „Der Feldeffekttransistor ist also die
    ältere Idee …“); ein eigener Kasten hätte den Geschichtsabsatz wiederholt.
15. „Verbraucht CMOS überhaupt Strom, wenn immer ein Transistor sperrt?“ → Text, Kipp-Stelle 3 → beide.
16. „Warum laufen Prozessoren seit Jahren mit nur wenigen GHz?“ → Frage-Kasten → beide.
17. „Was heißt 65-nm-Technologie?“ → Begriff im Text bei erster Nennung; Frage-Kasten ausführlich.
18. „Wozu braucht ein Digitalchip analoge Schaltungstechnik?“ → Frage-Kasten ausführlich; kompakt ein Satz im Ausblick.

## 5. Kipp-Stellen

**K1 Das gesteuerte Ventil (Triode).** Schritte: (1) geheizte Kathode emittiert Elektronen; (2) die Elektronenwolke
vor der Kathode (Raumladung) stößt nachfolgende zurück, es fließt nur so viel Strom, wie das Feld an der Kathode
zulässt; (3) das Gitter liegt nahe an der Kathode und bestimmt dieses Feld 100-mal stärker als die Anode (µ = 100,
D = 0,01): −1 V statt −2 V am Gitter wirkt wie 350 V statt 250 V an der Anode, beides 3,115 mA im Modell; (4) das Gitter
ist negativ, es fängt keine Elektronen, Steuerung fast ohne Leistung; (5) die Energie liefert die Anodenquelle: 0,1 V
am Gitter ändern den Strom um 0,16 mA, an 100 kΩ (mit R_i 38,5 kΩ wirksam) 6,15 V. Abbildungen: Triodenaufbau,
Kennlinienschar (ausführlich). Herleitung: Steuerspannung und Barkhausen (ausführlich), v_u = −S(R_i‖R_a).
Beispiel: Stufe −61,5. Analogie: Wasserhahn bzw. „valve“.

**K2 Gemeinsam herstellen, verkleinern, verdoppeln (IC und Moore).** Schritte: (1) diskret: jede Verbindung gelötet,
ENIAC 17 468 Röhren, rund 5 Mio. Lötstellen; (2) Planartechnik: Fotolithografie erzeugt alle Strukturen einer Ebene
gleichzeitig, Kosten je Fläche, nicht je Transistor; (3) Verkleinerung um 0,7 je Generation halbiert die Fläche je
Transistor; (4) alle zwei bis drei Jahre eine Generation plus größere Chips → Verdopplung etwa alle zwei Jahre;
(5) 8008 → Core 2 Duo: Faktor 83 143, 16,34 Verdopplungen in 34 Jahren, T_2 = 2,08 Jahre. Abbildungen:
Planartechnik, Moore-Diagramm. Herleitung: T_2 aus zwei Datenpunkten. Beispiel: 8008/Core 2 Duo/Xeon.

**K3 CMOS: kein Ruhestrom, Leistung nur beim Umladen.** Schritte: (1) Ausgangsknoten hat Kapazität C; (2) PMOS zur
Versorgung, NMOS zur Masse, immer genau einer leitet → kein Gleichstrompfad; (3) Laden entnimmt C U², die Hälfte wird
gespeichert, die Hälfte im PMOS Wärme; (4) Entladen setzt die gespeicherte Hälfte im NMOS um; (5) P = C U² f,
1 fF·(1 V)²·3 GHz = 3 µW, Chip 30 W; 1 µA Ruhestrom je Gatter ergäbe 100 W. Abbildung: CMOS-Inverter mit
Stromspitzen. Herleitung im Kasten. Beispiel Knoten + Chip. Ausführlich: Skalierung (Dennard) als Folge.

## 6. Aussortier-Liste (K/H/V/S; Fassung → Ort)

| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Ventilprinzip, Energie aus der Versorgung | K | Röhre, Schritte | Röhre, Schritte |
| Glühemission, Heizung | H | Frage-Kasten | Frage-Kasten |
| Raumladung, Gitter nahe Kathode, µ = 100 | K | Schritte 2–3 | Schritte 2–3 |
| Steuerspannung U_g + D U_a, S, R_i, Barkhausen, v_u | V | – | eigener Unterabschnitt, Formeln, Beispiel |
| Lieben 1906 (magnetisch, Steuerleistung) / 1910 Gitter, Gasfüllung; De Forest Audion; Hochvakuum (Langmuir 1913, Siemens-Serie 1916), Schottky Raumladungsgesetz und Schirmgitter | K/H | 4 Sätze Geschichte | Absatz Geschichte |
| Rückkopplung, A = v/(1 − kv), Schwingbedingung, Meißner 1913 | K | Abschnitt + Formel | Abschnitt + Formel + Gegenkopplung |
| Gegenkopplung als Gegenstück (Link OPV) | H | 1 Satz | Absatz + Kurz gesagt |
| Überlagerungsempfänger, Produktformel, f_ZF | K | Abschnitt + Formel | Abschnitt + Formel |
| Güteargument (500 gegen 53,5) | K | Text | Text |
| Spiegelfrequenz, 10,7 MHz | H | Frage-Kasten | Text + Formel + Beispiel |
| Lévy 1917, Schottky 1918, Armstrong 1918/19 | H | 1 Satz | 2 Sätze |
| Loewe 3NF 1926, Steuer je Fassung, Heizfaden-Ausfall; von Ardenne (OE333, Fernsehen 1931) | H | 1 Satz | Absatz |
| Transistor 1947/48, Vorteile, Heizleistung 275 MW | K | Text | Text |
| ENIAC-Zahlen | H | 1 Satz (in K2) | Text |
| Germanium → Silizium 1954: n_i², Oxid, Temperatur | K | Text | Text |
| Warum zuerst Germanium (Schmelzpunkt, Reinigung) | V | – | Frage-Kasten |
| IC: Kilby 1958 (Ge, Drähte), Noyce 1959 (Si, planar, Hoerni) | K | Text | Text |
| Planartechnik-Schritte | K | Text knapp | Text |
| IC ≠ kleine Platine | H | 1 Satz | Fehlvorstellung |
| erste ICs analog bipolar, µA741 (1968), TTL | H | 1 Halbsatz | 1–2 Sätze |
| Gleichlauf integrierter Bauelemente (0,1 % gegen 10–20 %) | H | 1 Satz im Funkabschnitt | Text IC + Funk |
| FET-Idee Lilienfeld 1925, Heil 1934; Oberflächenzustände; Atalla/Kahng 1959 | K/H | 2 Sätze | Text + Fehlvorstellung |
| MOSFET-Steuerung kapazitiv, kein Gatestrom; BJT braucht Basisstrom (zwei Sichtweisen) | K | Text | Text (beide Sichtweisen) |
| CMOS 1963, kein Ruhestrom, P = C U² f | K | Kipp-Stelle | Kipp-Stelle |
| Mikroprozessor 1971/72 PMOS, NMOS, CMOS ab 1980er | H | 1 Satz | 2 Sätze |
| Mooresches Gesetz 1965/1975, Formel, T_2, empirisch | K | Kipp-Stelle | Kipp-Stelle |
| 18-Monate-Irrtum (House) | K | Fehlvorstellung | Fehlvorstellung |
| Technologieknoten | H | Halbsatz | Frage-Kasten |
| Dennard-Skalierung | H/V | 2 Sätze | Unterabschnitt mit Tabelle + Herleitung |
| Ende der Skalierung, Takt-Plateau, Mehrkern | H | Frage-Kasten | Frage-Kasten |
| Takt-PLL, Bustreiber | H | 1 Satz Ausblick | Frage-Kasten |
| Mobilfunk: Kostendruck, Bipolar/SiGe-BiCMOS bis 2 GHz | K/H | 2 Sätze | Absatz |
| Direktumsetzer, I/Q, Gleichlauf | H | 1–2 Sätze | Absatz + Abbildung |
| Transitfrequenz, 180 nm, 50–70 GHz | H | 1 Satz | Absatz |
| HF-SoC Bluetooth 2000/01, CDMA2000, GSM Mitte 2000er | K | 1 Satz | Absatz |
| Halbleiterspeicher, 100 000 Transistoren 1980er | H | – | Moore-Absatz |
| Organisatorisches aus 1.2, „Ausblick“ auf andere Lehrveranstaltung | S | – | – |
| Meißner 10–20 W (nicht belegt) | S | – | – |
| von Ardennes Beteiligung an der 3NF selbst (umstritten) | S | – | – |

**Zusammenhänge in einem Satz (§5.11), in beiden Fassungen gleich:**
- Mischung: „Das Produkt zweier Kosinusschwingungen ist die halbe Summe zweier Kosinusschwingungen, eine mit der
  Differenz und eine mit der Summe der beiden Frequenzen.“ Probe: Zahlenwerk C (0,466873 = 0,466873).
- Umladeleistung: „Doppelte Spannung, vierfache Leistung; doppelte Frequenz oder doppelte Kapazität, doppelte
  Leistung.“ Probe G (Faktor 4, 2).
- Moore: „In gleich langen Zeitspannen wächst die Zahl um denselben Faktor: alle zwei Jahre um 2, in zehn Jahren um 32,
  in zwanzig um 1024.“ und „Die Verdopplungszeit ist die Zeitspanne geteilt durch die Anzahl der Verdopplungen; diese
  ist der Zweierlogarithmus des Wachstumsfaktors.“ Probe F (16,34; 2,08).
- Rückkopplung (nur ausführlich, Gegenkopplung): „Mitkopplung vergrößert die Verstärkung bis zur Selbsterregung,
  Gegenkopplung verkleinert sie und macht sie unempfindlich gegen Schwankungen des Verstärkers.“ Probe B (123,1;
  −20 % → −3,38 %).
- Röhrenstufe (beide): „Die Verstärkung ist Steilheit mal wirksamer Widerstand am Ausgang; ihr Höchstwert, bei
  unbegrenzt großem Arbeitswiderstand, ist Steilheit mal Innenwiderstand.“ Probe A (−61,5; Grenzwert −100).
- Barkhausen (nur ausführlich): „Die größtmögliche Spannungsverstärkung einer Triode ist der Faktor, um den ihr Gitter
  stärker auf den Strom wirkt als ihre Anode.“ Probe A (1,6 mA/V · 62,5 kΩ = 100 = 1/D).
- Skalierung (nur ausführlich): „Verkleinert man alle Längen und Spannungen um denselben Faktor, bleiben die
  Feldstärken und die Leistung je Fläche gleich.“ Probe H (×1,000).
- Verworfen: „Der doppelte Durchgriff halbiert die Verstärkung“ (gilt nur im Leerlauf); „Halbe Strukturgröße,
  doppelte Geschwindigkeit“ (gilt nur bei konstanter Feldstärke; als Bedingung im Skalierungssatz enthalten).

## 7. Abbildungsplan (Szene-IDs st1/einfuehrung/01-…)

| Nr. kompakt / ausführlich | Szene-ID | Vorlage | Inhalt und Kernaussage | Abschnitt |
|---|---|---|---|---|
| 1 / 1 | 01-drei-ventile | schaltbild-vergleich | Triode, npn-Transistor, n-MOSFET je mit Arbeitswiderstand an der Versorgung, über einer Zeitachse 1906–2010 mit den Epochen; Steuergröße und gesteuerter Strom markiert. Drei Generationen, ein Prinzip. | Worum es geht |
| 2 / 2 | 01-triode-aufbau | querschnitt | Kathode mit Heizfaden, Gitter, Anode; Raumladungswolke; Potentialverlauf schematisch für U_g = −2 und −1 V. Das Gitter steuert das Feld vor der Kathode. | Röhre |
| – / 3 | 01-triodenkennlinien | kennlinienschar | I_a(U_g) für U_a = 150, 200, 250 V aus dem Modell (Zahlenwerk A), Arbeitspunkt, Verschiebung 0,5 V je 50 V. 1 V Gitter wirkt wie 100 V Anode. | Steuerspannung |
| 3 / 4 | 01-rueckkopplung | blockschaltbild-graph | Signalfluss v, k; Graph A/v über kv (1/(1 − kv)); Meißner-Schaltung. Bei kv = 1 erhält sich die Schwingung selbst. | Rückkopplung |
| 4 / 5 | 01-ueberlagerung | blockschaltbild-spektrum | Empfänger als Blockbild; Spektrum 87,5–108 MHz, Empfangssignal 100, LO 110,7, ZF 10,7, Summe 210,7, Spiegel 121,4 MHz. Feste ZF, Spiegel außerhalb des Bandes. | Überlagerung |
| 5 / 6 | 01-planartechnik | querschnitt-prozess | Oxidieren, Belichten, Ätzen, Dotieren, Metallisieren; Querschnitt npn-Transistor und Widerstand mit Al-Bahnen auf SiO₂. Alles in denselben Schritten. | IC |
| 6 / 7 | 01-cmos-inverter | schaltbild-zeitverlauf | Inverter mit C; zwei Zustände; u_e, u_a, i(t) mit Stromspitzen nur beim Umschalten. | CMOS |
| 7 / 8 | 01-moore | kennlinie-semilog | 12 Intel-Prozessoren 1971–2010, Gerade T_2 = 2,04 Jahre, Moore 1965 (2⁶ → 2¹⁶), Gegenprobe 18 Monate. | Moore |
| – / 9 | 01-skalierung | schema-tabelle | MOSFET-Querschnitt vor/nach Skalierung um κ, gleiche Feldpfeile; Faktorentabelle. | Skalierung |
| – / 10 | 01-direktumsetzer | blockschaltbild | Überlagerungsempfänger mit externem ZF-Filter gegen Direktumsetzer mit I/Q-Mischern und integrierten Tiefpässen; Chipgrenze. | Funk |

Kompakt 7 (Richtwert 3–6, bei rund 2000 Wörtern eine je 300 Wörter, vertretbar), ausführlich 10.

## 8. Zahlenwerk

`notizen/st1/zahlen_einfuehrung.py`, Ausgabe `.txt`; Abschnitte A (Triode ECC83), B (Rückkopplung), C (Mischung,
Güte, Spiegel), D (Röhre gegen Transistor, ENIAC), E (Ge/Si), F (Moore, Fit, Gegenproben, Knoten), G (CMOS-Leistung),
H (Skalierung, Laufzeit, f_T, 60 mV/Dekade). Kennlinienmodell der Triode: 3/2-Potenz mit Durchgriff und Versatz
U_0 = 0,625 V, so angepasst, dass Strom, Steilheit und Innenwiderstand im Arbeitspunkt den Datenblattwerten entsprechen.

## 9. Profi-Abgleich

- Computer History Museum, The Silicon Engine: MOS-Transistor 1959/60 (Atalla, Kahng; thermisches Oxid gegen
  Oberflächenzustände), CMOS 1963 (Wanlass, Sah; „close to zero power in standby“, erste Großanwendung Uhren, ab 1978
  konkurrenzfähig), Planartechnik 1959 (Hoerni), Patente Kilby (Febr. 1959) und Noyce (Juli 1959):
  https://www.computerhistory.org/siliconengine/
- Moore 1965 und 1975, House 18 Monate, Dennard-Ende 2005–2010: https://en.wikipedia.org/wiki/Moore%27s_law
- Überlagerungsempfänger, Priorität Lévy 1917, Schottky DRP 368 937 (angemeldet 19.6.1918), Armstrong US 1 342 885:
  https://ethw.org/Superheterodyne_Receiver, https://en.wikipedia.org/wiki/Lucien_L%C3%A9vy
- Loewe 3NF (1926, drei Trioden, vier Widerstände, zwei Kondensatoren in Glaskapseln, Steuer je Röhrenfassung):
  https://en.wikipedia.org/wiki/Loewe_3NF; von Ardenne: Deutsche Biographie (OE333 ja, 3NF nein; Fernsehen 1931).
- Liebenröhre (1906 magnetisch, 1910 Gittersteuerung, Quecksilberdampf; Lieben-Konsortium 1912):
  https://www.radiomuseum.org/tubes/tube_liebenroehre.html
- Siemens-Serienfertigung Hochvakuumröhren 1916 (A-Röhre), Schottky Schirmgitter DRP 300 617 (1916):
  https://www.radiomuseum.org/tubes/tube_a.html, Deutsche Biographie Schottky.
- GeO₂ wasserlöslich, zerfällt ab etwa 250 °C: Semiconductor Engineering „What's after silicon“.
- ECC83-Datenblattwerte: https://en.wikipedia.org/wiki/12AX7
- 180-nm-NMOS f_T 50–70 GHz: Tiemeijer et al., IEDM 2001; Chartered-RF-CMOS-Angaben.
- ENIAC (17 468 Röhren, 150 kW, rund 5 Mio. Lötstellen, Ausfall alle zwei Tage): https://en.wikipedia.org/wiki/ENIAC

## 10. Skript-Abgleich (PDF-Seiten; gedruckt = PDF − 8)

**Inhalte (Vollständigkeit):**
- S. 9: Kommunikationstechnik als Antrieb; Liebenröhre; Schottky und von Ardenne als deutsche Beiträge. Zeittafel:
  1906 Lieben-Patent; 191x Röhren in der Übertragungstechnik; 1912 De Forest Audioschaltung mit Triode (verstärkt und
  demoduliert); 1913 Meißner Rückkopplung, erster Röhrensender mit Liebenröhre (10–20 W); 1914 Siemens Hochvakuumröhre
  „A“ (Schottky), erste Poströhre in Serie; 1918 Schottky Überlagerungsempfänger, Lévy (1919), Armstrong (1920); 192x
  Radioempfänger mit Hochvakuumröhren, Loewe 3NF als Vorläufer der integrierten Schaltung, von Ardenne Fernsehen; 193x
  FET-Erfindung („Hall“) und Theorie der Halbleiterübergänge (Schottky); 1947 Bipolartransistor (Bardeen, Brattain,
  Shockley, Bell Labs); 195x diskrete BJTs, erste Bipolar-ICs; 1956 erste Si-Transistoren; 1958 IC bei TI (Kilby und
  „Gordon Moore“); 1959 Atalla und Kahng Isolierschicht-FET; 196x kommerzielle ICs; 1963 Sah und Wanlass
  komplementäre MOS-Logik mit fast null Ruheleistung. → alle im Artikel (Ausnahmen in §6: 10–20 W).
- S. 10: 1965 „erste bipolare ICs, erste FETs“; 197x CMOS-ICs, Mikroprozessoren; 1972 8008; 198x 100 000 Transistoren,
  Halbleiterspeicher; 199x 100 Mio. bei Speichern; 200x SoC Mobilfunk; 2001 Bluetooth-SoC; 2004 GSM-SoC. Text:
  Lieben 1906 magnetisch, hohe Ansteuerleistung; 1910 Triode; Schottky bei Siemens, Poströhre, Empfangstechnik;
  Überlagerungsempfänger Juni 1918, LO über Übertrager eingekoppelt; Verwertung nach dem Krieg verzögert; Armstrong
  1919. → im Artikel.
- S. 11: Schottky später Halbleitergrundlagen; Loewe 3NF (drei Trioden, R und C in Kapseln); Empfänger 1927;
  von Ardenne, Fernsehen Anfang 1930er; Transistor 1947, Röhre in den 1950ern noch vorherrschend; Ge, dann Si als
  Voraussetzung für ICs. → im Artikel.
- S. 12: erste ICs Ende 1950er (TI), zunächst analoge Bipolarschaltungen (µA741); 1959 FET; 1963 CMOS (Fairchild);
  1965 Moore, „Verdopplung alle 8 Monate“, kleine Datenbasis, galt 40 Jahre; 8008: 3500, 10 µm PMOS; Core 2 Duo:
  291 Mio., 65 nm, 143 mm²; Xeon: 2,3 Mrd., 45 nm; Takt-PLL und Bustreiber brauchen Transistorebene;
  Kommunikationstechnik als Motor. → im Artikel.
- S. 13: Mobilfunk braucht Kostensenkung → Integration; Anfang 1990er nur Bipolar schnell genug bis 2 GHz →
  SiGe-BiCMOS; Abkehr vom Überlagerungskonzept; kontrollierte Prozessschwankungen → Direktumsetzer; kürzere Gates →
  höhere Transitfrequenz; ab 180 nm CMOS-HF wirtschaftlich; → monolithische Integration von HF und Basisband.
  → im Artikel.
- S. 14: HF-SoCs Bluetooth (CSR), CDMA2000 (Qualcomm), GSM (Infineon). 1.2 (entfällt bis auf): FET und BJT als
  spannungsgesteuerte Stromquellen, FET wie Röhre kapazitiv, BJT braucht Eingangsstrom. → im Artikel.

**Fehler und Ungenauigkeiten (im Artikel stillschweigend korrigiert):**
1. S. 9 und 12: „IC 1958 bei Texas Instruments durch Jack Kilby und Gordon Moore“ – falsch. Kilby (TI, 1958);
   Noyce (Fairchild, 1959, planar und monolithisch); Moore war Mitgründer von Fairchild, nicht bei TI.
2. S. 12: „Verdopplung der Integrationsdichte alle 8 Monate“ – falsch. 1965: jährlich; 1975: alle zwei Jahre;
   18 Monate ist ein verbreitetes Fehlzitat (House, Leistung).
3. S. 9: „Erfindung des FET-Transistors (Hall)“ – falscher Name. Lilienfeld (1925/26), Heil (1934/35).
4. S. 9 und 11: „Erfindung des bipolaren Transistors 1947 durch Bardeen, Brattain und Shockley“ – ungenau. 1947
   Spitzentransistor (Bardeen, Brattain); Flächentransistor (bipolar mit pn-Übergängen) Shockley 1948, gebaut 1950/51;
   Nobelpreis 1956 an alle drei.
5. S. 9: „1956 erste (bipolare) Silizium-Transistoren“ – ungenau. 1954 (Tanenbaum, Bell Labs; Teal, TI, erster
   kommerzieller).
6. S. 9: „1914 Siemens fertigt die erste Hochvakuumröhre, die A-Triode von Schottky“ – nicht belegt/ungenau.
   Hochvakuumröhren 1913 (Langmuir, Arnold); Siemens-Serie ab 1916 (A-Röhre 1916/17); belegte Schottky-Erfindung:
   Schirmgitterröhre 1916. Im Artikel ohne Zuschreibung der A-Röhre.
7. S. 9/10: „1918 Schottky erhält das erste Patent; Lévy (1919), Armstrong (1920)“ – ungenau. Lévy meldete im
   August 1917 an und hat die Priorität; Schottky meldete im Juni 1918 an (erteilt 1923); Armstrong Ende 1918/Anfang
   1919 (erteilt 1920). Die Jahreszahlen 1919/1920 sind Erteilungs- bzw. spätere Daten.
8. S. 9: Meißner-Sender „10–20 W“ – zunächst keine Quelle gefunden; die Faktenprüfung fand Meißner selbst (Proc. IRE
   1922) bzw. einen Museumseintrag mit 10–15 W. Für das Prinzip ohne Belang, deshalb weggelassen.
9. S. 10: „1965 erste bipolare ICs, erste FET-Transistoren“ – widerspricht der eigenen Zeittafel; weggelassen,
   stattdessen erste MOS-ICs Mitte der 1960er.
10. S. 10: „197x Siegeszug hochintegrierter CMOS-ICs (Geburt der Mikroprozessoren)“ – ungenau. Erste Mikroprozessoren
    PMOS (4004, 8008), dann NMOS; CMOS ab den 1980ern vorherrschend.
11. S. 12: „Intel Core 8 Xeon“ – gemeint: achtkerniger Xeon 7500 (Nehalem-EX), 2010.
12. S. 13 (Bild 1.7): Core 2 Duo „2007“ – Markteinführung Juli 2006.
13. S. 10: „2004 erster GSM-SoC“ – Infineon E-GOLDradio Febr. 2005 angekündigt; im Artikel „Mitte der 2000er-Jahre“.
14. S. 11: Loewe 3NF „in den frühen zwanziger Jahren“ – 1926. Von Ardennes Beteiligung an der Röhre selbst ist
    umstritten (Deutsche Biographie: am Empfänger OE333 beteiligt, an der Dreifachröhre nicht).
15. S. 10: Satzbruch „somit kann die Diode D das Empfangs Aufgrund …“ – Text fehlt; ohne Belang.
16. S. 9: Liebenröhre 1910 als Beginn des „Siegeszugs“ – sie war gasgefüllt (Quecksilberdampf); den Durchbruch brachte
    das Hochvakuum ab 1913. Im Artikel richtiggestellt.
17. S. 9: De Forest „1912 erste Audioschaltung, verstärkt und demoduliert“ – vermischt: Das Audion (1906/07) arbeitete
    als Detektor, der zugleich gleichrichtet und verstärkt; ab 1912 als Niederfrequenzverstärker. Das Gitter-Audion
    (Patent angemeldet 29.01.1907) war vor Liebens Gittersteuerung (1910).
18. S. 12 (und Bildunterschrift 1.5): „Zunächst wurden vorwiegend analoge Bipolarschaltkreise realisiert“ – falsch. Die
    ersten käuflichen ICs (1961, Fairchild Micrologic, TI Series 51) waren Logik für Raumfahrt und Militär (Apollo,
    Minuteman); der erste verbreitete Analog-IC war der µA702 (1964), dann µA709 (1965) und µA741 (1968). Von der
    Faktenprüfung gefunden.
19. S. 12: „1959 wurde bereits der erste Feldeffekttransistor demonstriert“ – ungenau. Der erste funktionierende FET war
    der Sperrschicht-FET von Dacey und Ross (Bell Labs, 1953); Atalla und Kahng gelang 1959/60 der FET mit isoliertem
    Gate (MOSFET). Von der Faktenprüfung gefunden.
20. S. 12: Moore „1965 … Verdopplung“ und 1975 – Moore sagte 1975 voraus, dass sich das Wachstum ab etwa 1980 auf zwei
    Jahre je Verdopplung verlangsamt; so im Artikel.

## 11. Faktenprüfung (23.10.2026)

Unabhängige Prüfung durch einen Agenten, Bericht im Scratchpad der Sitzung (`faktencheck_st1_einf/bericht.md`):
7 falsch, 22 ungenau; alle selbst nachgeprüft und eingearbeitet (U22 betrifft nur diese Notiz).
- Falsch: Lieben „erstmals“ mit Gitter (de Forest 1907 früher); FET „erst 1959 gebaut“ (Sperrschicht-FET 1953) und
  „zwölf Jahre nach dem Bipolartransistor“ (gemeint: nach dem ersten Transistor); erste ICs „oft analog“ (Logik ab
  1961); „Kanal 65 nm“ (Gatelänge 35 nm); Sperrstrom „4 Millionen Mal“ nur ideal (mit Generationsstrom rund 5000-mal,
  Zahlenwerk E); Dennard-Schritt 4 widersprüchlich formuliert; „ohne dass die Kühlung mitwachsen musste“ (bis Anfang
  der 1990er 5 V, Leistung bis rund 100 W).
- Ungenau, eingearbeitet: Schottky 1913 in Jena; „beseitigt“ → „verringert“; 60 mV „höchstens“ und Schwellspannung
  erklärt; „alle linearen Verstärkerschaltungen“ mit OPV; Vorzeichen der Schleifenverstärkung gegenüber dem OPV-Artikel
  erklärt; I/Q-Gleichlauf 1 % und 1°; Antenne, Bandfilter, Quarz außerhalb des Chips; „unter den Siliziumtechniken“;
  65 W als Auslegungsleistung; Rundung −123; Mischen braucht quadratischen Anteil; Richardson-Faktor 6·10¹²;
  Potentialminimum und „praktisch kein Elektron“; Moore 1975 präzisiert; „geschlossene Formeln zu lang“; Durchgriff
  2,5 V statt „250 V heben sich auf“; T₂-Lesart; Dennard mit Dotierung ×κ; Symbole (Ableitung als dh/dU statt
  Strich, Funktion g entfernt, E eingeführt, t als Zeit in Jahren); ECC83 als Doppeltriode, I/Q-Begründung in der
  kompakten Fassung; AC128 90 bis 100 °C.
