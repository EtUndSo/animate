# Arbeitsnotiz: Der Bipolartransistor – Aufbau und Wirkungsweise (ET1 Kap. 11.1 und 11.7), Stil 3

## 1. Ein-Satz-Prinzip
Ein gesperrter pn-Übergang führt so viel Strom, wie Nachschub an Minoritätsträgern zu ihm gelangt; im Bipolartransistor liefert ein leitender Übergang diesen Nachschub durch eine sehr dünne Basis, sodass U_BE den Kollektorstrom exponentiell festlegt, U_CE ihn kaum beeinflusst und nur ein kleiner, fester Bruchteil als Basisstrom fließt.

## 2. Schwierigkeit und Längenspannen
Schwer (ERKLAER_PROMPT §3.3 nennt den Bipolartransistor ausdrücklich): drei zusammenwirkende Mechanismen (Injektion und Transport, Verluste und B, zweiter Übergang in Durchlass) plus zwei Sichtweisen und die Rechenmodelle der Arbeitsbereiche. Kompakt 1800–2800 Wörter, ausführlich 3500–5000.

## 3. Vorwissen-Kette
| Voraussetzung | Weg |
|---|---|
| Dotierung, Majoritäts-/Minoritätsträger, n p = n_i², Boltzmann-Verteilung, pn-Übergang, Zwei-Ströme-Bild | „Halbleiter und das Bändermodell“ (erinnern, verlinken) |
| Durchlass senkt die Barriere (exp(U/U_T)), Sperrstrom = Nachschub an Minoritätsträgern, Shockley-Gleichung | „Die Diode und ihre Kennlinie“ (erinnern, verlinken) |
| Annahme und Probe mit Ersatzschaltungen, Arbeitsgerade | „Arbeitspunkt und Ersatzschaltung der Diode“ (verlinken) |
| Knoten- und Maschenregel | „Kirchhoffsche Gesetze“ (verlinken) |
| Diffusion, Diffusionskonstante, Ficksches Gesetz, Lebensdauer, Diffusionslänge | hier aufbauen (je ein Satz, im Herleitungskasten das Gesetz) |
| Stromquelle, gesteuerte Quelle | hier in einem Satz; Zweitore verlinken |

## 4. Fragenkatalog
| Nr. | Frage | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Warum fließt überhaupt Strom durch den gesperrten Basis-Kollektor-Übergang?“ | Transistoreffekt (K1) | Text, Schritte | beide |
| 2 | Fehlvorstellung (User, MiNa): „Wenn man U_CE anlegt, entsteht dadurch I_C; mehr U_CE, mehr Strom.“ | Transistoreffekt (K1) | Fehlvorstellung (ausf.), Text + Quiz (komp.) | beide |
| 3 | „Kann man einen Transistor aus zwei Dioden zusammenlöten?“ | Transistoreffekt | Frage-Kasten | beide |
| 4 | „Warum muss die Basis so dünn sein?“ | Transistoreffekt (K1) | Text (Schritt 3) | beide |
| 5 | „Woher kommt der Basisstrom, wenn die Elektronen zum Kollektor gehen?“ | Basisstrom (K2) | Text, Schritte | beide |
| 6 | Fehlvorstellung (Skript-Wasseranalogie): „Der Basisstrom öffnet den Transistor; die Elektronen kommen über die Basis.“ | Strom/Spannung | Fehlvorstellung | beide |
| 7 | „Wozu braucht man den Basisstrom dann überhaupt? Was passiert bei offener Basis?“ | Basisstrom | Frage-Kasten | beide |
| 8 | „Warum streut B so stark?“ | Basisstrom | Text (α) | beide (komp. kurz) |
| 9 | „Warum ist der Kollektor schwach dotiert? Kann man Emitter und Kollektor vertauschen?“ | Basisstrom/Arbeitsbereiche | Frage-Kasten | ausf. |
| 10 | „Steuert nun der Strom oder die Spannung?“ | Strom/Spannung | Text + Beispiel | beide |
| 11 | Fehlvorstellung: „In der Sättigung liefert der Transistor seinen größten Strom.“ | Arbeitsbereiche (K3) | Fehlvorstellung | beide |
| 12 | „Warum liegt die Grenze bei 0,2 V und nicht bei U_CE = U_BE?“ | Arbeitsbereiche (K3) | Frage-Kasten | beide |
| 13 | „Wie schnell schaltet ein Transistor?“ | Schalter | Frage-Kasten | ausf. |
| 14 | „Wozu braucht man pnp-Transistoren, und warum ist npn häufiger?“ | pnp | Text | beide (komp. kurz) |

## 5. Kipp-Stellen
**K1 Transistoreffekt:** Schritte: BE leitet, BC sperrt; Boltzmann hebt die Randdichte um exp(U_BE/U_T) (10³ → 8,3·10¹³ cm⁻³ bei 0,65 V, 0,08 % von N_B); Diffusion durch 0,5 µm Basis (Transit 60 ps, Lebensdauer 80 ns, L_n = 12,9 µm); gesperrter BC-Übergang sammelt jedes ankommende Elektron (Randdichte null), unabhängig von U_CB; lineares Profil, Diffusionsstrom ∝ n(0) → I_C = I_S exp(U_BE/U_T). Abb.: Banddiagramm Gleichgewicht/aktiv und Basisprofil. Herleitung Transfergleichung (Boltzmann + Fick). Beispiel: I_C bei 0,60/0,65/0,70 V; 17,9 mV verdoppeln. Analogie (ausf.): Wasserfall aus dem Diodenartikel, Zufluss geregelt.

**K2 Basisstrom und B:** Schritte: kein Kollektor-Elektron geht über den Basisanschluss; Rückinjektion 12,5 Löcher je 10 000 Elektronen (μ_p/μ_n · N_B/N_E · W_B/W_E = 0,125 · 0,01 · 1); Rekombination 7,6 je 10 000 (60 ps/80 ns); beide ∝ exp(U_BE/U_T) → B ≈ 500, α = 0,998. Abb.: Stromaufteilung. Herleitung: B = α/(1−α) (Knotenregel), 1/B ≈ η + δ (ausf.). Beispiel: aus Strömen und aus Dotierung/Geometrie.

**K3 Sättigung:** Schritte: Arbeitsgerade, mehr I_B senkt U_CE; ab U_BC ≈ 0,5 V (U_CE ≈ 0,2 V) leitet der BC-Übergang; überschüssiger Basisstrom fließt als Löcher in den Kollektor (bei 20 µA: 9,6 µA Emitterverluste, 10,4 µA über BC), I_C bleibt beim Wert des Kollektorkreises (4,45 mA < B I_B = 10 mA); U_CE = U_BE − U_BC (0,696 − 0,552 = 0,144 V). Abb.: Arbeitsgerade mit drei Punkten; Trägerflüsse in der Sättigung (ausf.). Herleitung: Schaltbedingung I_B ≥ I_C,sat/B_min. Beispiel: drei Bereiche an 10 V/2,2 kΩ; LED-Schalter.

## 6. Aussortier-Liste
| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Drei Gebiete, Dotierungen, dünne Basis, zwei Übergänge, npn/pnp (S. 175) | K | Text + Abb. 2 | Text + Abb. 2 |
| Name „bipolar“, npn häufiger (Beweglichkeit) | H | ein Satz | ein Satz |
| Schaltsymbol, Zählpfeile, I_E = I_B + I_C, U_CE = U_CB + U_BE (S. 175/176) | K | Formel | Formel + Beispiel |
| Transistoreffekt, Transfergleichung | K | Schritte + Formel + Herleitung + Beispiel | dito + Analogie |
| I_S aus Fläche, n_i², Basisdotierung und -weite (Gummel-Zahl) | H | in der Herleitung | in der Herleitung + Beispiel |
| Early-Effekt | V | – (ein Halbsatz) | ein Satz mit Zahl und Verweis auf Artikel 03 |
| Basisstrom: Rückinjektion und Rekombination; B, α, B = α/(1−α), Streuung, h_FE-Gruppen | K/H | Text + Definition | Text + Formel + Beispiel |
| 1/B aus Dotierung und Geometrie | H | – | Formel + Herleitung + Beispiel |
| Strom- und Spannungssicht (CCCS, S. 175), Eingangskennlinie als Formel | K | Text + Formel | Abschnitt + Beispiel + Fehlvorstellung |
| B → ∞, Superbeta, Temperatur als Belege | H | – | Text |
| Kennlinien (S. 176/177), U_BE,ein = 0,6 V, U_CE,sat = 0,2 V | K | Text + Abb. | Text + Abb. |
| B hängt vom Strom ab (kleine/große Ströme) | V | – | ein Satz mit Modellzahlen |
| Arbeitsbereiche, Annahme und Probe (S. 176) | K | Tabelle + Beispiel | Tabelle + Beispiel |
| Sättigung: Mechanismus, U_CE,sat als Differenz zweier Durchlassspannungen | K | Schritte | Schritte + Abb. + Frage |
| Inversbetrieb | V | – | im Frage-Kasten zum Kollektor |
| Schalter (S. 175), Übersteuerung, B_min | K/H | Beispiel | Abschnitt + Formel + Beispiel |
| Schaltgeschwindigkeit, Speicherzeit | V | – | Frage-Kasten |
| pnp-Transistor (S. 193/194) mit Bereichen | K | Text + Tabelle | Text + Tabelle + Beispiel |
| Wasseranalogie des Skripts (Bild 11.2) | S | – (nur Korrektur in der Fehlvorstellung) | dito |
| MOSFET | S | Verweis | Verweis |

## 7. Abbildungsplan (Szene-IDs get1/bipolartransistoren/01-…)
| Nr. ausf. | Nr. kompakt | Szene · Vorlage | Inhalt | Kernaussage |
|---|---|---|---|---|
| 1 | 1 | 01-npn-querschnitt · querschnitt-traegerfluesse | npn-Querschnitt, Elektronenstrom E → C, Löcher über die Basis, Werte bei 2 mA | I_C geht nicht über die Basis; die Basis ersetzt nur Verluste |
| 2 | 2 | 01-aufbau-symbole · aufbau-und-symbol | (a) npn, (b) pnp: Schichten, Dotierungen, Polung im Normalbetrieb, Symbol mit Zählpfeilen | drei Gebiete, zwei Übergänge, Pfeile wie im Skript |
| 3 | 3 | 01-transistoreffekt · banddiagramm-abfolge | Leitungsband Gleichgewicht/aktiv, Basisprofil linear | Barriere bestimmt den Nachschub, Kante sammelt ihn |
| 4 | 4 | 01-stromaufteilung · stromfluss-bilanz | je 10 000 Elektronen: 12,5 Löcher Rückinjektion, 7,6 Rekombination | B ≈ 500 aus zwei kleinen Verlusten |
| 5 | – | 01-zwei-sichten · zwei-schnitte | I_C über U_BE (halblog.) und über I_B (linear), gleicher Arbeitspunkt | beide Sichten, dieselben Zahlen |
| 6 | 5 | 01-kennlinien · kennlinien-drei | Eingang, Steuerung (log-log mit B(I_C)), Ausgangsfeld | Diode, Gerade, Stromquellenäste |
| 7 | 6 | 01-arbeitsgerade · kennlinienfeld-arbeitsgerade | Modellkennlinien, Arbeitsgerade 10 V/2,2 kΩ, Punkte bei 2, 8, 20 µA | Weg vom Sperren über aktiv in die Sättigung |
| 8 | – | 01-saettigung-fluesse · querschnitt-traegerfluesse | Trägerflüsse in der Sättigung: BC leitet, 10,4 µA Löcher in den Kollektor | überschüssiger Basisstrom fließt in den Kollektor ab |
| 9 | – | 01-led-schalter · schaltplan | 3,3-V-Pin, 12 kΩ, BC547C, 150 Ω, LED, 5 V | kleiner Pinstrom schaltet großen Laststrom |

## 8. Zahlenwerk
`notizen/get1/zahlen_transistor.py` (neu, Oberthema Bipolartransistoren; importiert Konstanten aus `zahlen_halbleiter.py`), Ausgabe `zahlen_transistor.txt`. Beispieltransistor: N_E = 10¹⁹, N_B = 10¹⁷, N_C = 10¹⁶ cm⁻³; W_E = W_B = 0,5 µm, W_C = 5 µm; A = 0,015 mm²; τ_n = 80 ns; Minoritätsbeweglichkeiten 800/100/450 cm²/(V s) → I_S = 0,994·10⁻¹⁴ A, B = 498,5, B_R = 1,78, U_A ≈ 70 V. Elektrisches Modell (Ebers-Moll, Transportform): I_S = 10⁻¹⁴ A, B = 500 (bei U_CE = 5 V), B_R = 1,8, U_A = 70 V. Datenblattbezug BC547C/BC557C.

## 9. Profi-Abgleich
- onsemi BC546/D (BC547C): h_FE 420–800 bei 2 mA/5 V; U_BE(on) 0,55 bzw. 0,58–0,70 V bei 2 mA; U_CE(sat) typ. 0,09 V, max. 0,25 V bei 10 mA/0,5 mA; f_T typ. 300 MHz: https://www.onsemi.com/download/data-sheet/pdf/bc546-d.pdf
- Emitterwirkungsgrad, Transportfaktor, α = γ·α_T, β = α/(1−α): University of Illinois ECE 340, Lectures 38 und 40: https://ursemiconductors.web.illinois.edu/ECE340/Lecture38.pdf, https://ursemiconductors.web.illinois.edu/ECE340/Lecture40.pdf; α_T ≈ 1 − W_B²/(2 L_n²) Standardergebnis (Pierret, Neamen), hier selbst über Ladung/Lebensdauer hergeleitet.
- onsemi BC546/D, weitere Zeilen (am PDF geprüft): h_FE Gruppe C typisch 270 bei 10 µA, 520 bei 2 mA, 300 bei 100 mA; I_CES typ. 0,2 nA, max. 15 nA; U_BE(sat) 0,7 V bei 10/0,5 mA; U_CE(sat) 0,2 V typ. bei 100/5 mA; Bild 1 normierte Stromverstärkung über I_C. Das Gummel-Poon-Modell `b_von_ic` ist daran angepasst (ISE 6,4e-13 A, IKF 110 mA).
- 2N3904 Speicherzeit t_s ≤ 200 ns bei 10 mA, I_B1 = I_B2 = 1 mA (onsemi-Datenblatt, z. B. https://web.physics.ucsb.edu/~phys127A/lipman/handouts/datasheets/2n3904.pdf).
- Superbeta-Transistoren: typisch B ≈ 5000 bei 1 µA (National/TI AN-29 zum LM108): https://ti.com/lit/pdf/snoa624
- Eigenes Dokument „Bipolartransistor: spannungs- oder stromgesteuert?“ (EtUndSo/1.Semester/ET1/Bipolartransistor_Steuerung, 20.10.2026) und MiNa-Lernskript k8 („Der Kollektorstrom ist der Sperrstrom der Basis-Kollektor-Diode, nur dass ihm der Emitter einen riesigen Nachschub liefert“).

## 10. Skript-Abgleich (S. 175–177 und 193–194 = PDF 181–183 und 199–200)
**Inhalte:** Definition BJT, drei Gebiete E/B/C, Emitter am stärksten, Kollektor am schwächsten dotiert, Basis deutlich schmaler, npn/pnp, npn häufiger (S. 175, Bild 11.1 Aufbau und Symbol mit Zählpfeilen); CCCS-Sicht, Steuerstrom I_B von Basis zu Emitter, Kollektorstrom = Transferstrom, Elektronen diffundieren durch die Basis, weil sie schmaler als die Diffusionslänge ist; B = 10 bis 1000, streut; Schalter schnell und ohne Verschleiß; Physik ausgeklammert, MOSFET nicht Gegenstand (S. 175). Wasseranalogie (Bild 11.2); I_E = I_B + I_C, U_CE = U_CB + U_BE; Eingangskennlinie wie Diode mit U_BE,ein = 0,6 V; Stromsteuerkennlinie linear mit Steigung B, „geht in Sättigung“ bei großen Strömen; Ausgangskennlinie ab U_CE,sat flach wie Stromquelle, U_CE,sat = 0,2 V; drei Arbeitsbereiche mit Bedingungen (S. 176); Bild 11.3 Kennlinien (S. 177). pnp: Dotierfolge umgekehrt, Basis „schmaler und schwächer dotiert als Kollektor und Emitter“ (S. 193), Bild 11.30 npn/pnp mit Zählpfeilen, Bereiche mit U_BE,ein = −0,6 V, U_CE,sat = −0,2 V (S. 194).

**Fehler und Ungenauigkeiten:**
1. **S. 194, pnp-Sättigung „I_C ≥ I_B · B“:** Mit den Zählpfeilen von Bild 11.30 (I_B und I_C aus dem Transistor heraus, positive Werte) muss es I_C ≤ B · I_B heißen, wie beim npn. Das „≥“ stimmt nur, wenn man die Ströme wie beim npn hineinzählt (dann negativ).
2. **S. 193, pnp „Basis ... schwächer dotiert als Kollektor und Emitter“:** widerspricht S. 175 (Kollektor am schwächsten); bei beiden Typen ist der Kollektor am schwächsten dotiert (hohe Sperrspannung, kleiner Early-Effekt).
3. **S. 176, Stromsteuerkennlinie „flacht ab, der Transistor ‚geht in Sättigung‘“:** Das Abflachen bei großen Strömen in Bild 11.3b ist ein Rückgang von B (starke Injektion), nicht der Sättigungsbereich der Arbeitsbereiche; zwei verschiedene Dinge mit demselben Wort.
4. **S. 176 „Steigung entspricht B“ zu Bild 11.3b:** Das Bild ist doppelt logarithmisch; dort hat I_C = B·I_B die Steigung 1, B ist der Abstand von der Diagonalen. Die gestrichelte Gerade im Bild ist steiler als 1 (schematisch).
5. **Bild 11.3c:** Die Kennlinien entsprechen B ≈ 1600 (9 mA bei 5 µA, 31 mA bei 20 µA), mehr als die genannten 10–1000; die Linie „U_CE = U_BE“ ist bei mehreren Volt gezeichnet, liegt aber bei 0,6–0,7 V, weil sich U_BE kaum ändert; der Knick realer Kennlinien liegt bei 0,1–0,3 V.
6. **S. 175/176 Wasseranalogie (Bild 11.2) und „Steuerstrom“:** legt eine falsche Kausalität nahe (Basisstrom öffnet ein Ventil); die Elektronen des Kollektorstroms gehen nicht über die Basis, U_BE bestimmt den Strom. Als Rechenmodell bleibt die CCCS-Sicht richtig.
7. **S. 175 „B = 10–1000“:** Spanne realistisch; im Praktikum BC547C 420–800 (Gruppe C).
8. **S. 175 „streut in der Fertigung in gewissem Ausmaß“:** zurückhaltend; tatsächlich umfasst schon eine Gruppe den Faktor 2 (BC547C 420–800), die Familie 110–800. Im Artikel als „erheblich, wie auch das Skript anmerkt“.
9. **S. 178:** Der Schalter mit zwei Arbeitspunkten (Sperrbereich und Sättigung) steht dort, nicht auf S. 175; zitiert als S. 175 und 178.

## 11. Faktenprüfung (zweiter Agent, 21.10.2026)
Unabhängig nachgerechnet (eigener Code mit Nullstellensuche), Skriptbilder aus den PDF-Vektordaten, Datenblatt onsemi BC546/D am PDF geprüft. Jeder Befund selbst nachgerechnet und eingearbeitet:

**Falsch (5):**
1. 9,8 V / 2,2 kΩ = 4,4545 mA, also 4,45 mA statt 4,46 mA (doppelt gerundet); überall korrigiert.
2. B mit exakter Diffusionslösung 498,5, Näherung 498,6, beide gerundet 499 (nicht 498).
3. Die 2 in w_B²/(2 L_n²) stammt aus der Dreiecksfläche, nicht aus einer „halben Grundseite“.
4. Rückinjektion ist ein Löcherstrom über dieselbe Stufe, kein Teil des Elektronenstroms; Schritt 4 und Prinzip-Tabellen umformuliert.
5. pnp-Schalter an 3,3-V-Ausgang: Die Emitter-Basis-Strecke klemmt bei etwa 0,7 V, an R_B bleiben 1,0 V, I_B = 0,1 mA, genug für 42 bis 50 mA; nicht „1,7 V zwischen Emitter und Basis“. Zahlenwerk ebenso.

**Ungenau (13), eingearbeitet:**
1. I_S ist der Vorfaktor bzw. Elektronenanteil des Sperrstroms bei U_BE = 0; im Ebers-Moll-Modell ist der Kollektorstrom bei U_BE = 0 I_S(1 + 1/B_R), real überwiegt die Generation (I_CES typ. 0,2 nA).
2. f_T 300 MHz = 0,53 ns Verzögerung: Transitzeit des realen Transistors (länger als die 60 ps des Modells) plus Sperrschichtkapazitäten, nicht „durch Kapazitäten begrenzt“.
3. B(I_C)-Modell an das Datenblatt angepasst (vorher 345/175 bei 1 µA/100 mA, jetzt 122/260/500/285 bei 1 µA/10 µA/2 mA/100 mA); Ursache des Hochstromabfalls nicht aus dem Modelltransistor begründet (dessen Knick erst um 1 A).
4. B_min = 420 gilt bei 2 mA; bei größeren Strömen kleiner (typ. 300 bei 100 mA) → als Grund der Übersteuerung genannt.
5. LED-Verlust: 3,7 mW im Kollektorkreis + 0,15 mW Basis-Emitter = 3,9 mW (vollständiges Modell 2,3 mW); „höchstens 3,7 mW“ war keine Schranke.
6. Bei U_CB = 0 sammelt der BC-Übergang weiter alles ein, injiziert aber nichts („führt keinen Strom“ war falsch).
7. Praktisch aktiv erst oberhalb von etwa 0,25 V (bei 0,2 V schon 11 % des Basisstroms über BC, bei 0,25 V 1,7 %).
8. Zwei-Dioden-Frage: Diffusionslänge der Beispieldiode 57 µm, entscheidend ist der Metallkontakt; die 13 µm gehören zur Transistorbasis.
9. Bild 11.3b: B ist der senkrechte Abstand von der Diagonalen; die gestrichelte Gerade des Skripts ist zu steil (ausführlich erwähnt).
10. Kern der kompakten Fassung ohne α formuliert.
11. Temperaturfaktor exakt 2,21 statt linearisiert 2,26 → „rund 2,2“.
12. 9,6 µA in der Sättigung = Verluste durch Rückinjektion und Rekombination, nicht nur „am Emitter“.
13. Kleinigkeiten: Eingangskennlinie mit Basisströmen (35 nA, 5 nA), Emitter 10¹⁸ → B unter 100 (Beweglichkeit), Messbedingungen der Speicherzeit, Skriptzitate (S. 175/178, Bild 11.3 auf S. 177), Bild 11.3c 32 statt 31 mA, LED-Basisstrom 0,217 mA vorgerechnet, fehlende Bildverweise ergänzt.

**Zusätzlich:** B über einen weiten Strombereich „fast konstant“ präzisiert (auf 10 % zwischen 0,3 und 20 mA); Tabellen für Handybreite umgebaut; Formel für U_CE in eigener Zeile (Breite).
