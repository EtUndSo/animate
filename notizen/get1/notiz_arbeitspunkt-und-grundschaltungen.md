# Arbeitsnotiz: Arbeitspunkt und Grundschaltungen des Transistors (ET1 Kap. 11.2 bis 11.4 und Grundschaltungen aus 11.5), Stil 3

## 1. Ein-Satz-Prinzip
Der Arbeitspunkt eines Transistors ist der Punkt, an dem seine Kennlinien und die Gleichungen der äußeren Schaltung zugleich gelten; gute Schaltungen legen ihn so fest, dass die unsicheren Kennwerte des Transistors, Stromverstärkung und Basis-Emitter-Spannung, kaum eingehen: durch Gegenkopplung oder dadurch, dass sie sich wie im Stromspiegel herauskürzen.

## 2. Schwierigkeit und Längenspannen
Schwer: mehrere Schaltungen mit eigenem Mechanismus (Gegenkopplung über Emitter und über Kollektor, Stromspiegel, Inverter, Grundschaltungen), dazu Betriebsgrenzen und die Rechentechnik mit Ersatzschaltbildern. Kompakt 1800–2800 Wörter, ausführlich 3500–5000. Der alte Artikel hatte 12 100 Wörter; Bereiche, Annahme und Probe sowie der Schalter stehen jetzt in 11/01 und werden hier nur erinnert.

## 3. Vorwissen-Kette
| Voraussetzung | Weg |
|---|---|
| Bereiche, Modelle 0,6 V/0,2 V, Annahme und Probe, Transfergleichung, B-Streuung (420–800), U_BE −2 mV/K, Early-Effekt | „Der Bipolartransistor – Aufbau und Wirkungsweise“ (erinnern, verlinken) |
| Arbeitsgerade und Schnittpunkt | „Arbeitspunkt und Ersatzschaltung der Diode“ (erinnern, verlinken) |
| Ersatzspannungsquelle (Leerlaufspannung, Innenwiderstand) | „Ersatzquellen nach Thévenin und Norton“ (verlinken) |
| Knoten- und Maschenregel | „Kirchhoffsche Gesetze“ (verlinken) |
| Gegenkopplung als Prinzip | hier aufbauen (Wirkungskette) |
| Verlustleistung, Wärmewiderstand | hier kurz |

## 4. Fragenkatalog
| Nr. | Frage | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Was genau ist der Arbeitspunkt, und wer legt ihn fest?“ | Arbeitsgerade | Text | beide |
| 2 | „Warum legt man den Arbeitspunkt in die Mitte?“ | Arbeitsgerade | Text | beide |
| 3 | „Warum schaltet man mit Sättigung statt im aktiven Bereich?“ | Arbeitsgerade | Text (Leistung) | beide |
| 4 | Fehlvorstellung: „Mit dem Basiswiderstand stelle ich den Kollektorstrom ein.“ | Basiswiderstand | Fehlvorstellung | beide |
| 5 | „Warum wird der Strom mit Emitterwiderstand unabhängig von B?“ | Stromgegenkopplung (K1) | Text, Schritte | beide |
| 6 | „Warum muss der Teilerstrom viel größer sein als der Basisstrom?“ | Stromgegenkopplung | Frage-Kasten | beide |
| 7 | „Kostet der Emitterwiderstand nicht Verstärkung?“ | Stromgegenkopplung | Frage-Kasten (Verweis 11/03) | ausf. |
| 8 | „Warum nicht gleich Spannungsgegenkopplung mit kleinem R_B?“ | Spannungsgegenkopplung | Text (Kompromiss) | beide |
| 9 | „Wie kann ein Transistor einen Strom kopieren?“ | Stromspiegel (K2) | Text, Schritte | beide |
| 10 | Fehlvorstellung: „Der Spiegel kopiert, weil beide Basen denselben Strom bekommen.“ | Stromspiegel | Fehlvorstellung | beide |
| 11 | „Warum ist der gespiegelte Strom bei 5 V größer als der Referenzstrom?“ | Stromspiegel | Text (Early) | ausf. |
| 12 | „Was passiert beim Inverter zwischen den logischen Pegeln?“ | Inverter | Text | beide |
| 13 | „Warum zählt die Versorgung als gemeinsamer Anschluss?“ | Grundschaltungen | Text | beide |
| 14 | Fehlvorstellung: „Die Kollektorschaltung verstärkt nicht.“ | Grundschaltungen | Fehlvorstellung | ausf. |

## 5. Kipp-Stellen
**K1 Stromgegenkopplung:** Schritte: Basis auf fester Spannung, Emitter folgt 0,6 V tiefer, Emitterstrom = (U_B − U_BE)/R_E, Abweichung des Stroms ändert U_RE und damit U_BE gegenläufig (Wirkungskette), Temperatur 2 mV/K wird durch R_E geteilt. Teiler als Thévenin-Quelle, Korrektur R_i/B. Zahlen: B 420→800 ändert I_C 0,975→1,034 mA (Basiswiderstand: Faktor 1,9); 0,19 %/K über U_BE, mit dem Temperaturgang von B (Empfindlichkeit 0,103) 0,24 bis 0,29 %/K statt 8 %/K; Skript-Gl. 11.1 ohne U_BE 1,71 mA statt 0,99 mA. Abb.: Schaltung, Wirkungskette, I_C über B für drei Einstellungen. Herleitung: Masche mit Thévenin. Beispiel: Dimensionierung 330 k/68 k/3,9 k/1 k.

**K2 Stromspiegel:** Schritte: T1 als Diode stellt U_BE auf seinen Strom ein, T2 mit derselben U_BE führt denselben Strom, Basisströme kosten 2/B, Ausgang ist Stromquelle bis ~0,3 V, Early-Effekt +1,3 %/V. Zahlen: 0,94 mA, −0,4 %, bei 5 V +5,7 %, 10 % I_S-Unterschied → +10 %. Herleitung Knotenregel. Beispiel 10 V/10 kΩ.

**K3 Spannungsgegenkopplung (Kompromiss):** relative B-Empfindlichkeit = (U_CE − U_BE)/(U_CC − U_BE): Mitte und Unabhängigkeit schließen sich aus. Zahlen R_B = 1 MΩ gegen 100 kΩ.

## 6. Aussortier-Liste
| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Arbeitspunkt als Schnittpunkt, Arbeitsgerade | K | Text + Formel | Text + Formel + Beispiel |
| Schalter (Sperr/Sättigung, kleine Leistung, Abstand) gegen Verstärker (aktiv, Mitte) (S. 178) | K | Text | Text |
| Mitte U_CE,AP = (U_CC + U_CE,sat)/2, symmetrischer Hub | K | Text | Text + Beispiel |
| Größte Verlustleistung U_CC²/(4 R_C) in der Mitte | H | – | Formel + Herleitung |
| Betriebsgrenzen U_CE,max, I_C,max, P_tot-Hyperbel (S. 181/182, Bild 11.9), Wärmewiderstand | K/H | Text | Text + Abb. + Beispiel |
| Lineare Ersatzschaltbilder (S. 182–184, Bild 11.10–11.13), Bereich aus Messwerten | K | Text + Abb. | Text + Abb. + Beispiel |
| Annahme und Probe | K | Verweis auf 11/01 | Verweis + Anwendung |
| Basiswiderstand (Bild 11.4), Formeln, Mitte dimensionieren | K | Formel + Beispiel | dito + volles Modell |
| Wandern durch B und Temperatur | K | Text | Text + Zahlen |
| Emitterwiderstand mit fester Basisspannung (Bild 11.5) | K | Text | Text |
| Stromgegenkopplung mit Teiler, Thévenin, Gl. 11.1 | K | Schritte + Formel + Beispiel | dito + Wirkungskette + Temperatur |
| Teilerstrom ≥ 10 I_B | H | Frage | Frage |
| Emitterwiderstand und Verstärkung (Überbrückung) | V | – | Frage mit Verweis |
| Spannungsgegenkopplung, Gl. 11.2 | K | Formel + Text | Formel + Beispiel |
| Kompromiss Mitte gegen Unabhängigkeit | H | ein Satz | Herleitung + Beispiel |
| Stromspiegel, Gl. 11.3 | K | Schritte + Formel + Beispiel | dito |
| Early-Effekt und Paarung im Spiegel | H | ein Satz | Text + Zahlen |
| Inverter, Kennlinie, Gl. 11.4 (korrigiert), Pegel | K | Formel + Beispiel | dito + volles Modell |
| Drei Grundschaltungen mit Gleichspannungskennlinien (S. 190–192) | K | Tabelle + Abb. | Tabelle + Abb. + Formel + Beispiel |
| Steigungen und Kleinsignalverhalten der Grundschaltungen | S | Verweis 11/03 | Verweis 11/03 |

## 7. Abbildungsplan (Szene-IDs get1/bipolartransistoren/02-…)
| Nr. ausf. | Nr. kompakt | Szene · Vorlage | Inhalt | Kernaussage |
|---|---|---|---|---|
| 1 | 1 | 02-arbeitsgerade-grenzen · kennlinienfeld-arbeitsgerade | Kennlinienfeld, Gerade 10 V/2,2 kΩ mit Mitte, Grenzen BC547 (45 V, 100 mA, 625 mW), Gerade 30 V/200 Ω | Arbeitspunkt = Schnittpunkt; Gerade muss in den Grenzen bleiben |
| 2 | 2 | 02-ersatzschaltbilder · schaltung-zustaende | drei lineare Ersatzschaltbilder, linearisierte Kennlinien | Netzwerk mit Quellen statt Transistor |
| 3 | 3 | 02-einstellungen · schaltplan | (a) Basiswiderstand, (b) Teiler + R_E mit Ersatzquelle, (c) R_B vom Kollektor | drei Wege zum Arbeitspunkt |
| 4 | 4 | 02-streuung-vergleich · kennlinienfeld-arbeitsgerade | Arbeitspunkte bei B 420/500/800 und I_C(B) der drei Einstellungen | Gegenkopplung hält den Punkt fest |
| 5 | – | 02-gegenkopplung-kette · blockbild | Wirkungskette I_C↑ → U_RE↑ → U_BE↓ → I_C↓ | Abweichung regelt sich selbst zurück |
| 6 | – | 02-spannungsgk-kompromiss · kennlinie-parameter | I_C und U_CE über R_B für B 420 und 800 | Mitte und Unabhängigkeit schließen sich aus |
| 7 | 5 | 02-stromspiegel · schaltung-und-kennlinie | Schaltung, I_C2 über U_CE2 | Kopie über gleiche U_BE, Early-Anstieg |
| 8 | 6 | 02-inverter · schaltung-und-kennlinie | Schaltung, U_aus über U_E (Modell und voll) | drei Bereiche, steiler Übergang |
| 9 | 7 | 02-grundschaltungen · schaltung-und-kennlinie | drei Schaltungen, drei Kennlinien | gemeinsamer Anschluss bestimmt das Verhalten |

## 8. Zahlenwerk
`notizen/get1/zahlen_transistor.py`, Abschnitt Thema 02: `ap_einfach_basis`, `ap_voll_basis`, `ap_einfach_stromgk`, `ap_voll_stromgk`, `ap_einfach_spannungsgk`, `ap_voll_spannungsgk`, `spiegel_voll`, `inverter_voll`, `emitterschaltung_voll`, `kollektorschaltung_voll`, `basisschaltung_re_voll`, `bericht_arbeitspunkt()`. Modellwerte 0,6 V/0,2 V, B = 500 (BC547C 420–800), BC547-Grenzwerte (onsemi BC546/D): U_CEO 45 V, I_C 100 mA, P_D 625 mW, R_thJA 200 K/W.

## 9. Profi-Abgleich
- Arbeitspunkteinstellung mit Teiler und Emitterwiderstand, Faustregeln (Teiler steif gegen β R_E, Emitterspannung um 10 % der Versorgung): Grantham University, Electronics I, Week 5 Lecture 2: https://content.grantham.edu/academics/GU_ET212/W5Lecture2.htm; Victoria University Wellington XMUT204 Lecture 3b „BJT Biasing Circuits“: https://ecs.wgtn.ac.nz/foswiki/pub/Courses/XMUT204_2026T1/LectureSchedule/XMUT204%20Lecture%203b%20-%20BJT%20Biasing%20Circuits.pdf
- Stromspiegel mit Early-Effekt I_O = I_REF (1 + (U_O − U_BE)/U_A)/(1 + 2/β): Standardergebnis (Sedra/Smith, Tietze/Schenk); Zahlenwerk bestätigt (5 V: 1,057).
- BC547-Grenzwerte und h_FE: onsemi BC546/D (am PDF geprüft).

## 10. Skript-Abgleich (S. 178–188 und 190–192 = PDF 184–194 und 196–198)
**Inhalte:** Schalter (Sperr- und Sättigungsbereich, kleine Leistung, größerer Abstand zum Aus-Punkt) gegen Verstärker (aktiver Bereich, linear) (S. 178); Beispielschaltung 1 mit R_B: Sperrannahme bis 0,6 V, I_B = (U_E − U_BE,ein)/R_B, I_C = B I_B, U_CE = U_CC − I_B B R_C, Probe U_CE ≥ 0,2 V, sonst Sättigung mit I_C = (U_CC − U_CE,sat)/R_C < B I_B (S. 178/179); Beispielschaltung 2 mit R_E (S. 179); Strom- und Spannungsgegenkopplung: Motivation B-Streuung und temperaturabhängige Eingangsspannung, Teiler mit Ersatzquelle U_q, R_i, Formel und Gl. 11.1, Gl. 11.2 (S. 179–181); Betriebsgrenzen U_CE,max, I_C,max, Bild 11.9 (S. 181/182); linearisierte Kennlinien Bild 11.10, Ersatzschaltbilder Bild 11.11–11.13, Knoten I_B + I_C = I_E (S. 182/183); Beispiele zur Bereichsbestimmung und Dimensionierung (S. 184/185); Stromspiegel, Gl. 11.3 (S. 186); Inverter, Kennlinie, Gl. 11.4, Pegel, Bild 11.16–11.18 (S. 186–188); Grundschaltungen Emitter-, Kollektor-, Basisschaltung mit Kennlinien Bild 11.22–11.27 (S. 190–192).

**Fehler und Ungenauigkeiten:**
1. **S. 179, Beispielschaltung 2:** „I_E = (U_E − U_BE,ein)/R_E = 7 mA < B · I_B“ ist sinnlos (Emitter- gegen B-fachen Basisstrom); die Rechnung selbst stimmt.
2. **S. 180, Gl. 11.1, letzter Schritt:** I_C ≈ U_CC R2/(R_E(R1 + R2)) lässt U_BE weg; das gilt nur für U_q ≫ U_BE. Bei üblichen 1–2 V Basisspannung grob falsch (Beispiel: 1,71 statt 0,99 mA).
3. **S. 179:** Das Temperaturproblem werde erst in Schaltungstechnik 2 gelöst; die Stromgegenkopplung verkleinert die Temperaturdrift aber schon um den Faktor 40 (0,19 %/K statt 8 %/K).
4. **S. 181, Gl. 11.2:** Die Bedingung R_C ≫ R_B/B schiebt U_CE gegen U_BE, also nahe an die Sättigungsgrenze; der Kompromiss zur Mitte fehlt.
5. **S. 181/182:** Der Text nennt als Grenzen nur U_CE,max und I_C,max; Bild 11.9 zeigt zusätzlich die Verlustleistungshyperbel.
6. **S. 182:** „die Stromverstärkung … im Sättigungsbereich auf 0 absinkt“: Null wird die Steigung der Steuerkennlinie; I_C/I_B sinkt nur unter B.
7. **S. 186, Stromspiegel:** Der Early-Effekt fehlt; er ist bei verschiedenen U_CE der größte Fehler (5 V: +5,7 % gegen −0,4 % durch die Basisströme). Der Referenzwiderstand heißt im Bild R_C.
8. **S. 187/188:** „U_BE < 0,6 Ω“ (Einheit V, S. 187); „U_E = U_CC − U_CE · R_B/B· + U_BE“ (S. 187) und Gl. 11.4 (S. 188) verstümmelt: R_C fehlt und die Klammer um U_CC − U_CE,sat; nur um R_C ergänzt ergäbe sich 5,596 V statt 0,696 V. Richtig U_E = (U_CC − U_CE) R_B/(B R_C) + U_BE.
9. **S. 190:** Bild 11.23 sei „dieselbe Kennlinie wie in Abb. 11.18“; gemeint ist Bild 11.17 (11.18 ist der Zeitverlauf).
10. **S. 191:** „Die maximale Steigung der Basisschaltung ist größer als die der Emitterschaltung“: für die gezeichneten Schaltungen ohne Vorwiderstand richtig (Faktencheck 21.10.2026, erste Fassung dieser Notiz war falsch). Bei gleichem Kollektorstrom sind beide Steigungen gleich groß (R_C I_C/U_T, ideal 96,7, mit Early-Effekt 93,5 bei 2,5 mA); die Basisschaltung bleibt aber bis 5,41 mA aktiv (Kollektor bis −0,4 V), die Emitterschaltung bis 4,72 mA (Kollektor über 0,25 V): größte Steigung +194 gegen −170. Der viel größere Unterschied der Bilder 11.23 und 11.27 kommt von Bild 11.23, das über rund 0,5 V fällt (wie mit Basiswiderstand; das Skript nennt es selbst dieselbe Kennlinie wie die des Inverters), während Bild 11.22 keinen Vorwiderstand zeigt. Kein Skriptfehler im engeren Sinn, nur die Begründung fehlt.
