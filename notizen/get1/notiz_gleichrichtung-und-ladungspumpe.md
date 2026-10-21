# Arbeitsnotiz: Gleichrichtung und Ladungspumpe (ET1 Kap. 10.6), Stil 3

## 1. Ein-Satz-Prinzip
Eine Diode lässt Strom nur in eine Richtung: Gleichrichter lenken damit beide Halbwellen in derselben Richtung durch die Last, Kondensatoren halten die Ladung zwischen den Spitzen fest und glätten oder stapeln so die Spannung, und jede leitende Diode kostet ihre Durchlassspannung.

## 2. Schwierigkeit und Längenspannen
Mittel: zwei Schaltungen mit Dioden als Ventilen und Kondensatoren als Speicher, eine Abschätzung (Brummspannung) und eine Ladungsbilanz. Kompakt 1000–1800 Wörter, ausführlich 2000–3500.

## 3. Vorwissen-Kette
| Voraussetzung | Weg |
|---|---|
| Diode, Durchlassspannung, Ersatzschaltung mit U_F0, Annahmen und Probe | „Die Diode und ihre Kennlinie“, „Arbeitspunkt und Ersatzschaltung der Diode“ (verlinken) |
| Kondensator, Q = C U, Strom und Spannung am Kondensator, Laden und Entladen | „Kondensator und Kapazität“, „Laden und Entladen“ (verlinken) |
| Sinusspannung, Scheitelwert, Frequenz, Periode | Schulphysik, hier kurz |
| Mittelwert und Effektivwert | hier aufbauen (ausführlich), Integral als Fläche |
| Ladungserhaltung, Knotenregel | „Kirchhoffsche Gesetze“ (verlinken) |

## 4. Fragenkatalog
| Nr. | Frage | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Warum leiten in der Brücke immer zwei Dioden gleichzeitig?“ | Brücke (K1) | Text | beide |
| 2 | „Warum braucht man vier Dioden, zwei würden doch reichen?“ | Brücke | Frage-Kasten | beide |
| 3 | „Warum fehlen am Ausgang 1,2 V?“ | Brücke (K1) | Text | beide |
| 4 | Fehlvorstellung: „Hinter dem Gleichrichter liegt eine Gleichspannung von 10 V.“ | Brücke | Fehlvorstellung | beide |
| 5 | „Was ist der Mittelwert einer gleichgerichteten Spannung?“ | Mittelwert | Text + Formel | ausf. |
| 6 | „Warum wird die Spannung mit Kondensator glatter?“ | Glättung (K2) | Text | beide |
| 7 | Fehlvorstellung: „Die Dioden im Netzteil führen den Laststrom gleichmäßig.“ | Glättung (K2) | Fehlvorstellung | beide |
| 8 | „Wie groß muss der Ladekondensator sein?“ | Glättung | Beispiel | beide |
| 9 | „Was begrenzt den Spitzenstrom?“ | Glättung | Frage-Kasten | ausf. |
| 10 | „Warum sperrt D1 in Takt 2?“ | Ladungspumpe (K3) | Text | beide |
| 11 | „Warum ist C2 nicht nach einer Periode voll?“ | Ladungspumpe (K3) | Text | beide |
| 12 | Fehlvorstellung: „Die Ladungspumpe gewinnt Leistung, weil sie die Spannung verdoppelt.“ | Ladungspumpe | Fehlvorstellung | beide |

## 5. Kipp-Stellen
**K1 Strompfade der Brücke:** positive Halbwelle über D1, Last, D3; negative über D4, Last, D2; Last immer gleich gepolt; zwei Dioden in Reihe kosten 2 U_F; Totzone |u_e| < 1,2 V (0,77 ms je Nulldurchgang). Abb. Brücke und Zeitverlauf. Beispiel: Spitze 8,8 V (Modell), 8,60 V (Beispieldioden), Mittel 5,21 V, Sperrspannung 9,4 V.

**K2 Glättung:** C lädt nahe der Spitze, dazwischen sperren alle Dioden und C speist die Last allein; Brumm ≈ I/(2 f C) als obere Schätzung; Dioden leiten nur 2,2 ms je Halbwelle mit 118 mA Spitze bei 17,4 mA Laststrom. Simulation: Ri = 5 Ω, C = 470 µF, RL = 470 Ω: 8,05 bis 8,34 V, Brumm 0,29 V gegen Schätzung 0,37 V.

**K3 Ladungspumpe:** Takt 1 lädt C1 auf U_e − U_F; Takt 2 stellt C1 auf U_e, oben 2 U_e − U_F, D1 sperrt, D2 leitet; Ausgleich mit C2; in der ersten Periode leitet D2 schon in Takt 1 (C2 auf U_e − 2U_F = 3,8 V), danach halbiert sich die Lücke je Periode bei C1 = C2 (6,3; 7,55; 8,18; 8,49 V … 8,8 V); mit Last bleibt D2 nach dem Ausgleich leitend, C1 und C2 teilen sich den Laststrom, am Ende von Takt 2 U_a = 2U_e − 2U_F − I/(f C1) = 8,7 V, Pendeln zwischen 8,65 und 8,725 V; Energiebilanz 2 mA Eingang bei 1 mA Ausgang.

## 6. Aussortier-Liste
| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Zweck der Gleichrichtung, Anwendungen (Skript) | K | Text | Text |
| Brücke nach Graetz, Strompfade, zwei Dioden je Halbwelle | K | Text + Abb. | Text + Abb. |
| Spitze Û − 2U_F, Totzone | K | Formel + Text | Formel + Text |
| Mittelwert, Effektivwert, Einweg gegen Doppelweg | H | – | Formel + Beispiel |
| Sperrspannung je Diode | H | ein Satz | Beispiel |
| Mittelpunktschaltung (zwei Dioden) | V | Frage-Kasten | Frage-Kasten |
| Glättung, Brummspannung, Stromflusswinkel, Spitzenströme | K/H | Text + Formel + Beispiel | dito + Simulation |
| Einschaltstrom, Innenwiderstand | V | – | Frage-Kasten |
| Ladungspumpe des Skripts in zwei Takten | K | Text + Abb. | Text + Abb. |
| Ladungsausgleich je Periode, Aufladen über viele Perioden | H | ein Satz | Herleitung + Abb. |
| Ausgang unter Last, Wahl von C1 | H | Formel | Formel + Beispiel |
| Energiebilanz | K | Fehlvorstellung | Fehlvorstellung |
| Kaskaden | V | ein Satz | ein Satz |
| Stabilisierung (Skript 11.6), Spannungsregler | S | Verweis | Verweis |

## 7. Abbildungsplan (Szene-IDs get1/halbleiterbauelemente/04-…)
| Nr. ausf. | Nr. kompakt | Szene · Vorlage | Inhalt | Kernaussage |
|---|---|---|---|---|
| 1 | 1 | 04-bruecke-strompfade · schaltung-strompfade | Graetz-Brücke, Strompfad der positiven und der negativen Halbwelle | Last immer gleich gepolt |
| 2 | 2 | 04-bruecke-zeitverlauf · zeitverlauf | u_e und u_a über 40 ms, Spitze 8,8 V, Totzonen, Mittelwert 5,21 V | Betrag der Eingangsspannung minus 1,2 V |
| 3 | 3 | 04-glaettung · schaltung-und-zeitverlauf | Schaltung mit C und RL, u_C und Diodenstrom gestapelt | kurze Strompulse, kleiner Brumm |
| 4 | 4 | 04-ladungspumpe-takte · schaltung-zustaende | Schaltung des Skripts in Takt 1 und Takt 2 mit Strompfaden und Spannungen | C1 wird auf die Eingangsspannung gestapelt |
| 5 | – | 04-ladungspumpe-aufladen · treppenverlauf | U_C2 über die Perioden ohne Last und eingeschwungen mit Last | Lücke halbiert sich je Periode; Last senkt das Ende von Takt 2 um I/(f C1) |

## 8. Zahlenwerk
`notizen/get1/zahlen_halbleiter.py`, Funktionen `glaettung_sim`, `glaettung_einschalten`, `ladungspumpe` (Grenzfall schnellen Ausgleichs), `pumpe_sim` (Schaltung mit R1, R2, Runge-Kutta), `bericht_gleichrichter()`. Annahmen: Quelle 10 V Scheitel, 50 Hz; Innenwiderstand 5 Ω (Transformator); 0,6 V-Modell wie im Skript; Ladungspumpe 5 V, 1 µF, 10 kHz, R1 = R2 = 10 Ω.

## 9. Profi-Abgleich
- Brummspannung ΔU ≈ I/(2 f C) für den Brückengleichrichter als Standard-Abschätzung (Tietze/Schenk, Halbleiter-Schaltungstechnik, Netzgeräte); die Simulation zeigt, warum sie überschätzt (Entladung nur außerhalb der Ladezeit).
- Schaltkondensator-Spannungsverdoppler (z. B. ICL7660-Prinzip): Ausgangswiderstand etwa 1/(f C) — Lehrbuchwissen.
- 1N4001: höchstens 1,1 V bei 1 A (Datenblätter).
- Links (WebSearch 21.10.2026):
  - Ausgangswiderstand einer Ladungspumpe 1/(f C1), mit f als Pumpfrequenz, also einer Umladung je Periode (so im Artikel definiert); größere Kapazität hilft nur, bis Schalterwiderstand und ESR überwiegen: [Maxim/Analog Devices, Guide to Integrated Charge Pump DC-DC Conversion](https://www.analog.com/jp/resources/technical-articles/guide-to-integrated-charge-pump-dcdc-conversion.html).
  - 1N4001 höchstens 1,1 V bei 1 A: [onsemi 1N4001G bei DigiKey](https://azcus.digikey.com/en/products/detail/onsemi/1N4001G/1485468), [Multicomp 1N4001 bei element14](https://sg.element14.com/multicomp/1n4001/diode-standard-1a-50v-do-41/dp/9564993).

## 10. Skript-Abgleich (S. 170–173 = PDF 176–179)
**Inhalte:** Anwendungen (Ladungspumpe, Graetz-Brücke; Stabilisierung mit Verweis auf „Kapitel 11.5“, gemeint ist 11.6). Ladungspumpe: Schaltung mit D1, R1, R2, D2, C1, C2, Schalter (Bild 10.23, 10.24); ideale Dioden; Takt 1 lädt C1 auf U_e; Takt 2: Eingangsspannung und C1 in Reihe, D1 sperrt, D2 leitet, C2 auf ca. 2 U_e; weitere Stufen. Gleichrichter: Zweck, Anwendungen, Graetz-Brücke mit vier Dioden, Last als Widerstand (Bild 10.25); U_e > 0: D1, D3 leiten (Bild 10.26); U_e < 0: D2, D4 (Bild 10.27); Eingang 10 V, Ausgang 8,8 V, Durchlassspannung etwa 0,6 V, Totzone |U_e| < 1,2 V (Bild 10.28, 10.29).

**Präzisierungen:**
1. **S. 171 „als ideal zu betrachten“ gegen „U_e − U_D1“ in Bild 10.24 und „ca. 2 U_e“:** Mit idealen Dioden wird C2 genau 2 U_e; mit Durchlassspannungen 2 U_e − 2 U_F, bei 5 V und 0,6 V also 8,8 V statt 10 V. Das Skript mischt beide Sichtweisen.
2. **S. 171 „C2 auf ca. 2 U_e aufgeladen“:** Das geschieht nicht in einem Takt, sondern über viele Perioden: In der ersten leitet D2 schon in Takt 1 (C2 auf U_e − 2 U_F), danach halbiert sich bei C1 = C2 der Abstand zum Endwert je Periode. Unter Last liegt die Spannung am Ende von Takt 2 um I/(f C1) darunter.
3. **S. 172 „Bei negativer (oder sehr kleiner positiver) Spannung U_e gilt: D1, D3 sperren und D2, D4 leiten“:** Fehler. Bei sehr kleiner positiver Spannung leiten auch D2 und D4 nicht; für |U_e| < 1,2 V sperren alle vier, wie das Skript auf derselben Seite selbst schreibt. D2 und D4 leiten erst unterhalb von −1,2 V.
4. **S. 170 „Auf die Spannungsstabilisierung … wird in Kapitel 11.5 eingegangen“:** Verweisfehler. 11.5 ist „Transistor als linearer Verstärker“; die Stabilisierung mit Z-Diode und npn-Transistor steht in 11.6 „Beispielanwendung eines Transistors“ (S. 192, Bild 11.28/11.29).
5. **S. 171 Bild 10.23 und 10.24:** Die Unterseite von C1 ist außer mit dem Umschalter auch fest mit der Masseschiene verbunden. Zeichenfehler: In Schritt 2 schlösse der Umschalter darüber die Quelle kurz, C1 ließe sich nie stapeln. Im Artikel als Hinweis, in der Abbildungsliste ausdrücklich nicht übernehmen.

## 11. Faktenprüfung (zweiter Agent, 21.10.2026)
Unabhängig nachgerechnet mit eigenem ODE-Löser (LSODA) und den Skriptbildern aus den Vektordaten. Jeder Befund selbst nachgerechnet (`bericht_gleichrichter()`, neue Funktionen `ladungspumpe`, `pumpe_sim`, `glaettung_einschalten`) und eingearbeitet:

**Falsch (5):**
1. Strompfad der negativen Halbwelle: D2 und D4 vertauscht. Laut Bild 10.25/10.27 fließt der Strom vom unteren Eingang über D4 zum oberen Lastende und über D2 zum oberen Eingang. Text und Abb. 1b beider Fassungen korrigiert, Nummerierung in die Abbildungsliste.
2. Aufladetreppe der Ladungspumpe: Im ersten Takt 1 leitet D2 mit und lädt C2 auf U_e − 2 U_F = 3,8 V; danach 6,30 / 7,55 / 8,175 / 8,4875 / 8,644 V, nach zehn Perioden fehlen 5 V/2^10 = 4,9 mV. Schaltung mit 10 Ω: 3,10 V, dann 5,74 / 7,26 / 8,02 / 8,41 / 8,60 V, nach zehn Perioden 8,794 V. Altes Zahlenwerk rechnete Takt 1 nicht.
3. Ladungspumpe unter Last: D2 bleibt nach dem Ausgleich leitend, C1 und C2 teilen sich den Laststrom (Simulation: D2 führt am Ende von Takt 2 noch 0,501 mA = I_L C1/(C1+C2)). Grenzfall: Takt 1 −0,05 V, Ausgleich +0,075 V, Rest von Takt 2 −0,025 V; 8,65 bis 8,725 V, Ende Takt 2 8,70 V, Mittel 8,694 V. Schaltung: 8,644 bis 8,708 V, Mittel 8,684 V. Formel U_a = 2U_e − 2U_F − I/(f C1) gilt für das Ende von Takt 2; Herleitung neu über Masche am Ende von Takt 2 und Ladungsbilanz von C1. Energie: Ausgang 8,69 mW (Schaltung 8,68), Dioden 1,2 mW, Umladen 0,11 mW (= ½ C1 (0,1 V)² f + ½ C1C2/(C1+C2) (0,15 V)² f), statt 8,65 mW.
4. Ausblick „Kapitel 11.5“ → 11.6 (Verweisfehler des Skripts übernommen, s. Präzisierung 4).
5. Link „Halbleiter und das Bändermodell, Abbildung 2“ zeigte auf die kompakte Fassung, deren Abb. 2 ein anderes Bild ist; Fließtext-Links werden nicht umgelenkt. Jetzt Link auf die ausführliche Fassung.

**Ungenau (6), eingearbeitet:**
1. Sperrbedingung der Glättung: Die Dioden sperren, sobald |u_e| unter u_C + 2 U_F fällt (Simulation: bei 9,537 V und 8,336 V), nicht erst bei |u_e| < u_C; „an ihren Kathoden liegt die Kondensatorspannung“ gilt nur für D1 und D4.
2. „Takt“ in zwei Bedeutungen: jetzt Takt 1/Takt 2 = halbe Periode (50 µs), „Periode“ = 100 µs, „Taktfrequenz“ = f.
3. Kapazität für 0,1 V Brumm nach der Simulation: 1375 µF (Schätzung 1743 µF); jetzt „rund 1400 µF“.
4. Mittelwert mit Durchlassspannungen hat eine geschlossene Form: (2/π)[û cos θ1 − 2U_F(π/2 − θ1)], θ1 = arcsin(2U_F/û) = 0,1203 → 5,212 V; jetzt in den Grenzen der Herleitung.
5. „Jedes Netzteil mit Transformator“ → „die meisten“ (Mittelpunktschaltung im eigenen Frage-Kasten).
6. Kompakte Fassung: R1, R2 und die Zeitkonstante als Akteure ergänzt.

**Zusätzlich:** Einschaltstrom beziffert (Simulation: 1,76 A beim Einschalten im Scheitel, 0,80 A im Nulldurchgang); Sperrspannung beim Einweggleichrichter mit Kondensator 19,4 V („rund das Doppelte“).
