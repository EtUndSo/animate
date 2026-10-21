# Arbeitsnotiz: Die Diode und ihre Kennlinie (ET1 Kap. 10.3), Stil 3

## 1. Ein-Satz-Prinzip
Eine Diode ist ein pn-Übergang mit zwei Anschlüssen: In Durchlassrichtung senkt die Spannung die Barriere, und der Strom wächst exponentiell, eine Dekade je 60 mV; in Sperrrichtung bestimmt allein der Nachschub an Ladungsträgern den Strom, und den liefern Wärme kaum, Licht in Maßen und ein sehr starkes Feld im Überfluss.

## 2. Schwierigkeit und Längenspannen
Schwer: mehrere zusammenwirkende Mechanismen (reale Kennlinie, Temperatur, zwei Durchbruchmechanismen, Fotostrom) und drei Spezialdioden. Kompakt 1800–2800 Wörter Hauptpfad, ausführlich 3500–5000. Risiko: zu lang wegen der vielen Spezialdioden; deshalb Herleitungen konsequent in Kästen, Schaltverhalten und Leuchtdiode nur als Vertiefung.

## 3. Vorwissen-Kette
| Voraussetzung | Weg |
|---|---|
| pn-Übergang, Raumladungszone, U_Diff = 0,714 V, Zwei-Ströme-Bild, Shockley-Gleichung, I_S, U_T | erklärt in „Halbleiter und das Bändermodell“ (verlinken; Shockley in zwei Sätzen in Erinnerung, Kurzherleitung im Kasten mit Link) |
| Bandlücke, n_i und sein Temperaturgang (8,3 %/K), Minoritätsträger, Generation, Rekombination, Lebensdauer τ | erklärt im Piloten (verlinken, je ein Satz) |
| Zählpfeile, Verbraucherzählpfeilsystem, Vorzeichen der Leistung | erklärt in „Zählpfeile und Vorzeichen“, Leistung in „Der ohmsche Widerstand“ (verlinken) |
| Plattenkondensator C = εA/d, Gaußsches Gesetz | erklärt in „Kondensator und Kapazität“ (verlinken) |
| ideale Stromquelle | erklärt in „Ideale und reale Quellen“ (verlinken) |
| Photonen mit Energie h c/λ | Schulphysik (ein Satz) |
| Exponentialfunktion, Logarithmus, Ableitung | Schulmathematik |
| Feld einer Raumladungsschicht (Felddreieck) | hier aufbauen im Kasten zu Weite und Höchstfeld (aus dem Gaußschen Gesetz) |
| Stoßionisation, Tunneleffekt | hier aufbauen (je zwei Sätze) |

## 4. Fragenkatalog
| Nr. | Frage | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Welcher Anschluss ist die Anode, und woran erkenne ich ihn am Bauteil?“ | Aufbau | Text (K) | beide |
| 2 | „Warum zeigt das Dreieck im Symbol in Stromrichtung, wo doch Elektronen andersherum laufen?“ | Aufbau | Frage-Kasten | beide |
| 3 | „Ab welcher Spannung leitet eine Diode?“ | Durchlassspannung (K1) | Text (K) | beide |
| 4 | Fehlvorstellung: „Die Schleusenspannung von 0,7 V ist eine feste Eigenschaft der Siliziumdiode.“ | Durchlassspannung (K1) | Fehlvorstellung | beide |
| 5 | „Warum ist die Durchlassspannung kleiner als die Diffusionsspannung von 0,714 V?“ | Durchlassspannung | Frage-Kasten | ausf. |
| 6 | „Warum hat eine Germaniumdiode eine kleinere Durchlassspannung?“ | Material | Text (H) | ausf.; kompakt ein Satz |
| 7 | „Warum sinkt die Durchlassspannung bei Erwärmung, obwohl U_T im Exponenten wächst?“ | Temperatur (K1) | Text + Herleitung | beide (kompakt kurz) |
| 8 | „Warum ist der gemessene Sperrstrom viel größer als I_S?“ | reale Kennlinie | Text (H) bzw. Frage-Kasten | ausf. Text; kompakt Frage-Kasten |
| 9 | Fehlvorstellung: „Im Durchbruch geht die Diode kaputt.“ | Durchbruch (K2) | Fehlvorstellung | beide |
| 10 | „Warum heißt sie Zener-Diode, wenn bei 12 V gar kein Zener-Effekt wirkt?“ | Z-Diode | Frage-Kasten | ausf. |
| 11 | „Wie kann eine Diode die Spannung festhalten, wenn der Strom durch sie schwankt?“ | Z-Diode | Text (K) | beide |
| 12 | „Warum hängt die Kapazität einer Kapazitätsdiode von der Spannung ab, bei einem Kondensator aber nicht?“ | Kapazitätsdiode | Text (K) | beide |
| 13 | Fehlvorstellung: „Licht macht die Fotodiode leitend; der Fotostrom fließt in Durchlassrichtung.“ | Fotodiode (K3) | ausf.: Fehlvorstellung; kompakt: Frage-Kasten (dort schon zwei Fehlvorstellungen) | beide |
| 14 | „Warum liefert eine Solarzelle fast immer gut 0,5 V, egal wie hell es ist?“ | Solarzelle (K3) | Text (K) | beide |
| 15 | „Warum leuchtet eine Siliziumdiode nicht, wenn doch Elektronen und Löcher rekombinieren?“ | Leuchtdiode | Vertiefung | ausf. |

## 5. Kipp-Stellen
**K1 Was die Durchlassspannung festlegt.**
- **Schritte:** (1) jede Dekade Strom kostet U_T ln 10 = 59,5 mV; (2) die scheinbare Schwelle ist 1 % des Achsenendes, also eine Frage des Maßstabs; (3) das Material legt über n_i² den Sättigungsstrom fest und verschiebt die ganze Kennlinie; (4) Temperatur: I_S wächst um 16,6 %/K, schneller als der Exponent bremst, deshalb −2,1 mV/K.
- **Akteure:** U_F, I, I_S, U_T, n_i, W_g0.
- **Abbildungen:** A3 (Maßstab), A4 (Material), A6 (Temperatur).
- **Zahlen:** 0,4665 / 0,5260 / 0,5855 / 0,6451 / 0,7046 V bei 1 µA … 10 mA; Ge 0,252, Si 0,645, GaAs 1,083 V bei 1 mA; −2,13 mV/K bei 1 mA.
- **Herleitung:** U = U_T ln(I/I_S + 1); dU/dT = (U − 3U_T − W_g0/e)/T.
- **Beispiele:** B1 (Durchlassspannung und Maßstab), B3 (Material), B6 (Temperatur).

**K2 Warum der Sperrstrom im Durchbruch plötzlich steigt.**
- **Schritte:** (1) der Sperrstrom ist durch den Nachschub begrenzt (Generation, 20 pA bei −1 V); (2) das Feld in der Zone wächst mit der Wurzel der Spannung; (3) ab etwa 4·10⁵ V/cm gewinnen Ladungsträger zwischen zwei Stößen genug Energie für neue Paare: Lawine, in der Beispieldiode bei rund 100 V; (4) in sehr hoch dotierten Übergängen (10¹⁸ cm⁻³) ist die Zone so dünn, dass bei 10⁶ V/cm Elektronen durch die 11 nm breite verbotene Zone tunneln: Zener-Effekt, unter etwa 5 V; (5) entgegengesetzte Temperaturgänge, nahe null um 5 bis 6 V; (6) reversibel, zerstörend ist nur die Wärme U·I.
- **Akteure:** E_max, U_BR, N, W_g.
- **Abbildung:** A7.
- **Zahlen:** 4·10⁵ V/cm, 103 V (78–130 V je nach E_krit), 9,9·10¹⁷ cm⁻³, 131 nm, 11,2 nm.
- **Herleitung:** Weite und Höchstfeld der Zone (Felddreieck).
- **Beispiel:** B7.

**K3 Licht als Nachschub: Fotodiode und Solarzelle.**
- **Schritte:** (1) ein Photon mit h c/λ > W_g erzeugt ein Paar; (2) das Feld der Zone trennt es, das Elektron ins n-, das Loch ins p-Gebiet: Strom von n nach p, also in Sperrrichtung; (3) die Kennlinie verschiebt sich um −I_ph; (4) Kurzschluss: −I_ph, Leerlauf: U_L = U_T ln(I_ph/I_S + 1); (5) dazwischen ist U > 0 und I < 0: Leistungsabgabe, Maximum im MPP.
- **Akteure:** I_ph, λ, W_g, η, U_L, I_K.
- **Abbildung:** A10.
- **Zahlen:** 1107 nm, 0,548 A/W bei 850 nm, I_K = 35 µA und U_L = 0,558 V bei 1000 W/m² (A = 0,1 mm²), 0,499 V bei 100 W/m², MPP 0,481 V / 33,2 µA / 16 µW, Füllfaktor 0,82, Wirkungsgrad 16 %.
- **Herleitung:** Fotodiodengleichung, Grenzwellenlänge und Empfindlichkeit, Leerlaufspannung.
- **Beispiele:** B10, B11.

## 6. Aussortier-Liste
| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Aufbau p/n mit Metallkontakten, Anode/Kathode, Kathodenring, Symbol | K | Text + A1 | Text + A1 |
| Zählpfeile im Verbraucherzählpfeilsystem | K | ein Satz | Text |
| drei Bereiche der Kennlinie (Bild 10.7) | K | Text + A2 | Text + A2 |
| Shockley-Gleichung als Erinnerung, Skriptform (10.1) ohne −1, U_T = k_B T/e statt k_B·T | K | Formel + Kurzherleitung + Skriptkritik | dito |
| Durchlassspannung nach U aufgelöst, Dekade je 59,5 mV, Maßstabseffekt, Datenblattangabe U_F bei I_F | K | Text + A3 + B1 | Formel + A3 + B1 |
| Durchlassspannung kleiner als U_Diff | H | – | Frage-Kasten |
| Materialabhängigkeit über n_i² (Ge, Si, GaAs) | H | ein Satz | Text + A4 + B3 |
| Rekombination in der Zone (n = 2), starke Injektion, Bahnwiderstand, Emissionskoeffizient | H | ein Absatz ohne Formel | Abschnitt + Formel + A5 + B4 |
| realer Sperrstrom durch Generation in der Zone | H | Frage-Kasten | Text + Formel (gemeinsam mit Rekombination) + B5 |
| Temperatur: −2 mV/K, I_S +16,6 %/K, Sperrstrom-Verdopplung etwa alle 8 bis 10 K, Temperatursensor | K/H | −2 mV/K mit Grund in Worten | Abschnitt + Formel + A6 + B6 |
| Durchbruch: Lawine und Zener-Effekt, Temperaturgänge | K | Text + A7 | Text + A7 |
| Abschätzung U_BR der Beispieldiode, Dotierung der Z-Diode, Tunnelstrecke | H | – | Formel (Weite/Höchstfeld) + B7 |
| Durchbruch reversibel, Zerstörung durch Wärme (Skriptkritik) | K | Fehlvorstellung | Fehlvorstellung |
| Z-Diode: Kennlinie, Stabilisierung, Glättungsfaktor | K | Text + A8 + B8 (ohne Formelbox) | Text + Formel + A8 + B8 |
| Name Zener-Diode trotz Lawine | H | – | Frage-Kasten |
| Kapazitätsdiode: C_j = εA/w(U), Weite aus dem Felddreieck, Anwendung Schwingkreis | K | Formel + Herleitung, ohne Abbildung | Formel + A9 + B9 |
| hyperabrupte Kapazitätsdioden | V | – | ein Satz |
| Fotodiode: innerer Fotoeffekt, Grenzwellenlänge, Fotostrom in Sperrrichtung, Ersatzschaltbild, Empfindlichkeit | K/H | Text + Formel + A10 | Text + Formeln + A10 + B10 |
| Solarzelle: I_K proportional, U_L logarithmisch (Skript S. 165), Leistungsabgabe, MPP, Füllfaktor | K/H | Text + Formel U_L + B11 (verkürzt) | Text + Formel + B11 |
| Versuchsaufbau des Skripts (Lampe, Abstand, Potentiometer) | H | – | ein Satz |
| Leuchtdiode | V | – | Vertiefung |
| Schaltverhalten, Sperrverzögerung, Diffusionskapazität | V | – | Vertiefung |
| differentieller Widerstand r_d = U_T/I | S | Verweis auf Artikel 03 | Verweis auf Artikel 03 (r_Z nur als Steigung) |
| Arbeitspunkt, Arbeitsgerade, Ersatzschaltungen | S | Artikel 03 | Artikel 03 |
| Gleichrichter | S | Artikel 04 | Artikel 04 |
| Schottky-Diode, Avalanche-Fotodiode | S | – | – |

## 7. Abbildungsplan (Szene-IDs get1/halbleiterbauelemente/02-…)
| Nr. ausf. | Nr. kompakt | Szene · Vorlage | Inhalt | Kernaussage | Abschnitt |
|---|---|---|---|---|---|
| 1 | 1 | 02-aufbau-symbol · bauteil-querschnitt-symbol | Querschnitt Kontakt–p–Zone–n–Kontakt, Symbol mit Zählpfeilen, Bauform mit Kathodenring | Strom in Durchlassrichtung von A nach K, in Pfeilrichtung | Worum es geht |
| 2 | 2 | 02-kennlinie-bereiche · kennlinie-bereiche | drei Bereiche mit getrennten Maßstäben | Durchlass mA, Sperr pA, Durchbruch bei hoher Sperrspannung | Kennlinie im Überblick |
| 3 | 3 | 02-schwelle-massstab · kennlinie-lin-zoom | dieselbe Kennlinie bei Achsenende 10 µA, 1 mA, 100 mA | scheinbare Schwelle 0,407 / 0,526 / 0,645 V | Durchlassspannung |
| 4 | – | 02-material-vergleich · kennlinienschar | Ge, Si, GaAs bei gleichem Aufbau | U(1 mA) 0,25 / 0,65 / 1,08 V | Durchlassspannung (Material) |
| 5 | – | 02-temperatur · kennlinienschar | 0/25/50/75 °C | −2,1 mV/K bei 1 mA | Temperaturabhängigkeit |
| 6 | – | 02-zone-unter-spannung · raumladung-felddreieck | Raumladung und Felddreieck bei 0 V und −5 V | Weite und Feld wachsen mit der Wurzel der Spannung | Raumladungszone unter Spannung |
| 7 | – | 02-kennlinie-real · kennlinie-semilog-anteile | ideal, Diffusion, Rekombination, real mit Injektion und R_B | m = 2 unten, m = 1 Mitte, Abknicken oben | reale Kennlinie |
| 8 | 4 | 02-durchbruch-mechanismen · banddiagramm-durchbruch | (a) Lawine (b) Tunneln | Paare durch das Feld | Durchbruch |
| 9 | 5 | 02-z-diode-stabilisierung · schaltung-und-kennlinie | Schaltung und Durchbruchast mit drei Arbeitspunkten | großer Stromhub, kleine Spannungsänderung | Z-Diode |
| 10 | 6 | 02-sperrschichtkapazitaet · funktionsgraph | C_j(U) 0 bis −25 V, Zonenweite | Zone breiter, Kapazität kleiner | Kapazitätsdiode |
| 11 | 7 | 02-fotodiode-quadranten · kennlinienschar-quadranten | Kennlinienschar 0 bis 35 µA Fotostrom, Quadranten, MPP, Ersatzschaltbild | Licht verschiebt die Kennlinie nach unten; im 4. Quadranten Leistungsabgabe | Fotodiode und Solarzelle |

Geprüft gegen §7.2: Einstieg Abb. 1; jeder Sach-Abschnitt hat eine Abbildung; jede Kipp-Stelle (Abb. 3/4/5, 8, 11); Schaltung Abb. 9; kompakt 7, ausführlich 11.

## 8. Zahlenwerk
`notizen/get1/zahlen_halbleiter.py`, Abschnitt „Diode als Bauteil (Thema 02)“ (Funktion `bericht_diode()`), Ausgabe in `zahlen_halbleiter.txt`. Neue Annahmen: Bahngebiete je 100 µm (R_B = 18,9 Ω), kritisches Lawinenfeld 4·10⁵ V/cm, Tunnelfeld 10⁶ V/cm, Fotostromdichte 35 mA/cm² bei 1000 W/m², Z-Diode 5,6 V bei 5 mA mit r_Z = 20 Ω, Schaltung U_E = 12 V ± 1 V, R_V = 330 Ω, R_L = 1 kΩ.

## 9. Profi-Abgleich
- Vishay, „Zener and Avalanche Breakdown Diodes“ (Selector Guide 49494): Avalanche über etwa 6 V mit positivem, Zener darunter mit negativem Temperaturkoeffizienten, weicher Knick beim Zener-Effekt. https://www.vishay.com/docs/49494/49494.pdf
- 1N4148-Datenblätter (Vishay, onsemi/Fairchild): U_F ≤ 1 V bei 10 mA, I_R ≤ 25 nA bei 20 V, Durchbruch ≥ 100 V bei 100 µA, 4 pF, t_rr 4 ns. https://sy-dep-epc-lpc.web.cern.ch/components/datasheets/epc-lpc%20(converters)/1N4148%20Diode%20(FAIRCHILD).pdf
- Silizium-PIN-Fotodioden (Hamamatsu/Lasermate): 0,55–0,56 A/W bei 850 nm, Bereich 400–1100 nm, Maximum um 950 nm.
- Sze, Physics of Semiconductor Devices: Tunneldurchbruch bei Feldern um 10⁶ V/cm, Rekombinationsstrom ∝ exp(U/(2U_T)), Generationsstrom e n_i w/(2τ) (Lehrbuchwissen, im Lernskript Kap. 6 und 7 verwendet).
- BZX79-C5V6 (Distributor-Daten): differentieller Widerstand höchstens etwa 40 Ω bei 5 mA, Temperaturkoeffizient klein; deshalb im Beispiel r_Z = 20 Ω als Annahme.

## 10. Skript-Abgleich (GET1 WS 24/25, S. 162–165 = PDF 168–171)
**Inhalte:**
- S. 162: Querschnitt (Metall, p, n) und Schaltsymbol mit A und K (Bild 10.6); Kennlinie mit Durchlassstrom, −I_S und Durchbruch (Bild 10.7); Shockley-Gleichung (10.1) im Durchlassbereich; k_B, I_S als Sättigungssperrstrom, U_T; Durchbruch im Sperrbetrieb.
- S. 163: Zenerdiode (Symbol, Kennlinie mit ΔI, ΔU, −U_Z, −I_Sperr; Betrieb im Sperrzustand; vorwärts wie pn-Diode; Durchbruchspannung U_Z; Stabilisierung; reversibel ohne thermische Überlast). Kapazitätsdiode (Symbol, C_Sp über −U_AB von 200 auf 100 pF bis 25 V; Betrieb in Sperrrichtung; Sperrschicht als Kapazität, nimmt mit der Sperrspannung ab; Schwingkreise). Fotodiode (Licht am Übergang erzeugt Strom, innerer Fotoeffekt, Solarzellen, Sperrstrom steigt mit der Beleuchtungsstärke, Photonenenergie mindestens W_g, antiproportional zur Wellenlänge).
- S. 164: Fotodiode Kennlinie, Ersatzschaltbild, Symbol (Bild 10.10); Solarzelle schematisch, Kennlinie (Bild 10.11), Versuchsaufbau mit Lampe, Abstand und Potentiometer (Bild 10.12).
- S. 165: Ergebnis: Spannung materialabhängig (Si 0,5 V), schwach von der Einstrahlung abhängig; Strom proportional zur Bestrahlung.

**Korrekturen und Präzisierungen:**
1. **S. 162 „Das Produkt k_B · T wird häufig auch als thermische Spannung U_T bezeichnet“:** Fehler. k_B T ist eine Energie (25,85 meV), die Temperaturspannung ist U_T = k_B T/e (25,85 mV).
2. **S. 162, Gl. (10.1) ohne „−1“:** Präzisierung. Sie gilt für U ≫ U_T (ab etwa 0,1 V); die vollständige Form mit −1 beschreibt auch den Sperrbereich.
3. **S. 162 „Durchbruch, wodurch die Diode irreversibel zerstört wird“:** Fehler bzw. Widerspruch zu S. 163. Der Durchbruch selbst ist reversibel; zerstörend ist die Verlustleistung, bei gewöhnlichen Dioden oft örtlich konzentriert (Rand des Übergangs), weshalb Datenblätter ihn dort nicht zulassen.
4. **S. 162 „I_S … Sättigungssperrstrom (kurz Sperrstrom)“:** Präzisierung. Der gemessene Sperrstrom realer Siliziumdioden ist bei Raumtemperatur viel größer (Generation in der Zone, Oberflächenströme): Beispieldiode rund 20 pA statt 15 fA bei −1 V.
5. **S. 163 „Zener-Diode“:** Präzisierung. Oberhalb von etwa 6 V beruht der Durchbruch auf dem Lawineneffekt; Z-Diode ist der Oberbegriff.
6. **S. 163 „Stromfluss in fast beliebiger Höhe“:** Präzisierung. Die Höhe legt der äußere Kreis fest; Grenze ist die zulässige Verlustleistung.
7. **S. 163 „Energie der Strahlung … mindestens so groß wie die Bandlücke“:** sprachliche Präzisierung. Der Zusatz „antiproportional zur Wellenlänge“ zeigt, dass die Energie des einzelnen Photons, h c/λ, gemeint ist.
8. **S. 163 „Der Sperrstrom der Diode steigt mit der Beleuchtungsstärke“:** Präzisierung. Der Fotostrom fließt in Sperrrichtung und addiert sich bei jeder Spannung, auch bei U = 0 und U > 0 (Solarzelle).
9. **S. 165 „abgreifbare Spannung … (Si = 0,5 V)“:** Deutung. Vermutlich ist die Leerlaufspannung gemeint; bei voller Sonne liegt sie bei Siliziumzellen bei 0,6 bis 0,7 V, im Punkt größter Leistung bei etwa 0,5 V. Sie wächst um 59,5 mV je Faktor 10 Bestrahlung.

## 11. Unabhängige Faktenprüfung (21.10.2026, zweiter Agent)
Geprüft: beide Fassungen gegen Zahlenwerk und Skriptseiten 162–165. Jeder Befund wurde vor dem Einarbeiten selbst nachgerechnet.

**Falsch (korrigiert):**
1. Generations- und Rekombinationsstrom mit der vollen Zonenweite: In Sperrrichtung erzeugen nur die inneren Teile der Zone mit voller Rate (Randschichten von je 0,215 µm, in denen die Majoritätsdichte noch über n_i liegt); in Durchlassrichtung ist die Rate nur in einer Schicht von π U_T/E_max um die Mitte groß. Zahlenwerk auf die integrierte Shockley-Read-Hall-Rate umgestellt (`i_rg`), Formel mit effektiver Weite hergeleitet. Neue Werte: −19,9 pA bei −1 V (vorher 53 pA), −64 pA bei −5 V, Gleichstand von Rekombination und Diffusion bei 0,27 V (vorher 0,38 V), m = 1,3 bei 1 nA (vorher 2,0), Absenkung der Leerlaufspannung bei 10 W/m² 1,3 mV (vorher 8 mV). Auch im Piloten korrigiert (53 → 20 pA, 97 → 64 pA).
2. 1N4148: „höchstens 1 V bei 10 mA“ ist ein garantierter Höchstwert, typisch um 0,7 V; die Begründung über die neutralen Gebiete entfällt.
3. Kompakt, Z-Diode: Der Faktor 17,8 gilt für die absoluten Schwankungen, relativ ±8 % gegen ±1 %.
4. Herleitung der Durchbruchspannung: „zweite in die erste“ vertauscht.
5. Rundungen: U_T mit 1,3806·10⁻²³ und 1,6022·10⁻¹⁹; 102,7 V statt 102,8 V; 59,5 mV statt 59 mV.

**Ungenau (präzisiert):**
- Diffusionskapazität der langen Diode im Kleinsignal τI/(2U_T) = 19 nF statt 39 nF.
- Lawine: Ionisationsschwelle etwa 1,5 W_g; E_krit ist das Feld, bei dem jeder Ladungsträger im Mittel ein Paar erzeugt.
- „mehr Sperrspannung ändert fast nichts“: Der Generationsstrom wächst mit der Zonenbreite.
- Frage zu U_F < U_Diff: Die absolute Aussage über U_pn entfällt.
- 8,3 %/K des Exponenteneffekts gilt bei 0,645 V (1 mA).
- Simulatorformel: I_S und m sind dort Anpasswerte (1N4148-Modell: I_S einige nA).
- Starke Injektion: 8 % der Dotierung bei 0,65 V, 57 % bei 0,7 V.
- r_Z von einigen Ohm bis über 100 Ω, am kleinsten um 6 bis 8 V.
- Grenzen der Fotodiodengleichung: Bahnwiderstand bei starkem, Rekombination bei schwachem Licht, Leckpfade.
- Skriptkritik zur Photonenenergie fair formuliert (das Skript meint mit „antiproportional zur Wellenlänge“ das Photon).
- „auch sehr helles Licht keinen Fotostrom“ → „praktisch keinen“ (Zwei-Photonen-Absorption bei Pulslasern).
- Leuchtdiode: Fernbedienungen nutzen meist 940 nm; Hinweis entfernt.
- Temperaturgang als „ein wichtiger Grund“ für die Gegenkopplung.
- 0,5 V im Skript als Deutung (Leerlaufspannung vermutlich gemeint).
- Nicht übernommen: 16,6 %/K und 8,3 %/K sind logarithmische Ableitungen (stetige Änderungsrate); die Verdopplungszeiten sind damit konsistent, die Schreibweise entspricht dem Piloten.
