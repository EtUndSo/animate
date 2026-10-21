# Arbeitsnotiz: Arbeitspunkt und Ersatzschaltung der Diode (ET1 Kap. 10.4–10.5), Stil 3

## 1. Ein-Satz-Prinzip
Der Arbeitspunkt ist der Punkt, an dem das Gesetz des Bauteils und die Gesetze des übrigen Netzes zugleich gelten, der Schnitt der Kennlinie mit der Arbeitsgeraden; weil die Diodenkennlinie gekrümmt ist, findet man ihn grafisch, durch Iteration oder mit linearen Ersatzschaltungen, deren Annahmen man am Ergebnis prüfen muss.

## 2. Schwierigkeit und Längenspannen
Mittel: eine zentrale Methode (Arbeitsgerade) mit drei Anwendungen (Ersatzschaltungen, mehrere Dioden, Kleinsignal). Kompakt 1000–1800 Wörter Hauptpfad, ausführlich 2000–3500.

## 3. Vorwissen-Kette
| Voraussetzung | Weg |
|---|---|
| Diodenkennlinie, Shockley-Gleichung, Durchlassspannung, Beispieldiode | erklärt in „Die Diode und ihre Kennlinie“ (verlinken) |
| Maschen- und Knotenregel | erklärt in „Kirchhoffsche Gesetze“ (verlinken) |
| ohmsches Gesetz | erklärt in „Der ohmsche Widerstand“ (verlinken) |
| Ersatzspannungsquelle (Leerlaufspannung, Innenwiderstand) | erklärt in „Ersatzquellen (Thévenin, Norton)“ (verlinken, ein Satz) |
| ideale Spannungsquelle | erklärt in „Ideale und reale Quellen“ (verlinken) |
| Potenzial | erklärt in „Arbeit, Potenzial und Spannung“ (verlinken) |
| Ableitung, Tangente, Logarithmus | Schulmathematik |
| Fixpunktiteration, Newton-Verfahren | hier aufbauen (ausführlich) |

## 4. Fragenkatalog
| Nr. | Frage | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Was genau ist ein Arbeitspunkt?“ | Anfang | Text (K) | beide |
| 2 | „Warum ist die Arbeitsgerade eine Gerade, wo doch eine Diode in der Schaltung steckt?“ | Arbeitsgerade (K1) | Text (K) | beide |
| 3 | Fehlvorstellung: „Die Arbeitsgerade ist eine Eigenschaft der Diode.“ | Arbeitsgerade | Fehlvorstellung | ausf.; kompakt im Text |
| 4 | „Warum rechnet man den Arbeitspunkt nicht einfach aus?“ | Arbeitspunkt der Diode | Frage-Kasten | beide |
| 5 | „Kann es mehrere Arbeitspunkte geben?“ | Arbeitspunkt der Diode | Frage-Kasten | ausf. |
| 6 | „Nehme ich im Modell 0,6 V oder 0,7 V?“ | Ersatzschaltungen | Text (K) | beide |
| 7 | „Woran erkenne ich, dass meine Annahme falsch war?“ | mehrere Dioden (K2) | Text (K) | beide |
| 8 | Fehlvorstellung: „Wenn die Rechnung mit ‚Diode leitet‘ ein Ergebnis liefert, stimmt es.“ | mehrere Dioden (K2) | Fehlvorstellung | beide |
| 9 | „Muss ich bei mehreren Dioden alle Fälle durchrechnen?“ | mehrere Dioden | Text (Potenzialbetrachtung) | beide |
| 10 | Fehlvorstellung: „Der Widerstand einer leitenden Diode ist Spannung durch Strom.“ | Kleinsignal (K3) | Fehlvorstellung | beide |
| 11 | „Warum darf man eine Diode für kleine Änderungen durch einen Widerstand ersetzen?“ | Kleinsignal (K3) | Text (K) | beide |
| 12 | „Wie klein ist klein?“ | Kleinsignal | Text (K) | beide |
| 13 | „Wie findet ein Simulator den Arbeitspunkt?“ | Iteration | Vertiefung | ausf. |
| 14 | „Warum hängt der differentielle Widerstand nicht von der Größe der Diode ab?“ | Kleinsignal | Frage-Kasten | ausf. |

## 5. Kipp-Stellen
**K1 Arbeitsgerade und Schnittpunkt.**
- **Schritte:** (1) Schaltung in nichtlineares Bauteil und linearen Rest teilen; (2) der Rest wirkt an den Klemmen wie eine Ersatzquelle, seine Kennlinie ist eine Gerade durch Leerlauf und Kurzschluss; (3) die Diode erzwingt ihre Kennlinie; (4) beide Gesetze gelten nur im Schnittpunkt; (5) steigende Kennlinie und fallende Gerade schneiden sich genau einmal.
- **Zahlen:** Leerlauf 5 V, Kurzschluss 5 mA, Arbeitspunkt 0,683 V und 4,32 mA.
- **Abbildung:** Abb. 1. **Herleitung:** Arbeitsgerade aus der Maschenregel. **Beispiel:** B1.

**K2 Annahmen und Probe bei Ersatzschaltungen.**
- **Schritte:** (1) jede Diode bekommt einen Zustand; (2) Ersatzschaltung einsetzen, linear rechnen; (3) Probe: leitende Dioden brauchen positiven Strom, sperrende Spannung unter U_F0; (4) Widerspruch heißt neue Annahme; (5) Potenziale schließen Fälle ohne Rechnung aus.
- **Zahlen:** Schutzdioden bei +9 V: beide sperrend gäbe 8,18 V am Eingang, also 3,18 V an D1, Widerspruch; D1 leitend: 5,6 V, 2,84 mA.
- **Abbildung:** Abb. Schutzdioden. **Beispiel:** B4.

**K3 Kleinsignal.**
- **Schritte:** (1) kleine Änderung um den Arbeitspunkt; (2) Kennlinie dort durch ihre Tangente ersetzen; (3) Steigung U_T/I; (4) Fehler u/(2U_T), also 2 % bei 1 mV; (5) für Änderungen ist die Diode ein Widerstand r_d.
- **Zahlen:** r_d 25,9 Ω bei 1 mA, 6,0 Ω im Arbeitspunkt; ±0,1 V an der Quelle ergeben ±0,6 mV an der Diode.
- **Abbildung:** Abb. Kleinsignal. **Herleitung:** r_d als Ableitung. **Beispiel:** B5.

## 6. Aussortier-Liste
| Inhalt | Kat. | kompakt | ausführlich |
|---|---|---|---|
| Arbeitspunkt, Analyse, Synthese (Skript 10.4.1) | K | Text | Text |
| linearer Fall: zwei Geraden (Skript 10.4.2) | K | ein Absatz | Absatz |
| Arbeitsgerade aus Leerlauf und Kurzschluss, Ersatzquelle | K | Formel + Abb. 1 | Formel + Abb. 1 |
| Schnittpunkt, Eindeutigkeit bei steigender Kennlinie | K | Text | Text |
| transzendente Gleichung | H | Frage-Kasten | Frage-Kasten |
| mehrere Schnittpunkte (Tunneldiode), Skript „Hysterese“ | V | – | Frage-Kasten |
| Iteration von Hand, Konvergenzfaktor r_d/R | H | ein Satz | Formel + Abb. + B1 |
| Newton im Simulator, Schrittbegrenzung, Lambert-W | V | – | Vertiefung |
| ideale Diode, Diode mit U_F0 (Skript 10.5) | K | Formel + Abb. 2 | dito |
| Knickkennlinie mit r_F | H | ein Satz | in Formel + B2 |
| Genauigkeit der Modelle | H | Zahlen im Text | Abb. + B2 |
| Verfahren mit Annahmen, 2^n, Probe | K | Text + B4 | Text + B4 |
| Potenzialbetrachtung | K | Text | Text |
| Synthese: Vorwiderstand | H | – | B3 |
| r_d = U_T/I, statischer gegen differentiellen Widerstand, Kleinsignalbedingung | K | Formel + Abb. + B5 | dito |
| Temperatur und Arbeitspunkt (−0,1 V, +2 % Strom bei 75 °C) | H | – | ein Satz |
| Gleichrichter, Z-Diode | S | Verweise | Verweise |

## 7. Abbildungsplan (Szene-IDs get1/halbleiterbauelemente/03-…)
| Nr. ausf. | Nr. kompakt | Szene · Vorlage | Inhalt | Kernaussage | Abschnitt |
|---|---|---|---|---|---|
| 1 | 1 | 03-arbeitsgerade · schaltung-und-kennlinie | Grundschaltung, Arbeitsgerade, Kennlinie, Arbeitspunkt, Ausschnitt | Arbeitspunkt = Schnittpunkt | Worum es geht |
| 2 | – | 03-iteration · kennlinie-iteration | Treppenweg der Fixpunktiteration | in zwei Schritten auf 0,1 mV genau | Arbeitspunkt der Diode |
| 3 | 2 | 03-ersatzschaltungen · kennlinie-modelle | drei Modelle mit Ersatzschaltbildern | einfache Modelle, gültig je Zustand | Ersatzschaltungen |
| 4 | – | 03-modellvergleich · kennlinie-ausschnitt | Arbeitspunkte der Modelle auf der Arbeitsgeraden | 0,6 V-Modell auf 2 % genau, ideal 16 % | Ersatzschaltungen |
| 5 | 3 | 03-schutzdioden · schaltung-potenziale | Eingangsschutz mit zwei Dioden, Potenziale der Annahmen | Widerspruch zeigt die falsche Annahme | mehrere Dioden |
| 6 | 4 | 03-kleinsignal · kennlinie-tangente | Tangente im Arbeitspunkt, kleines Signal, Ersatzschaltbild | für kleine Änderungen ein Widerstand U_T/I | Kleinsignal |

## 8. Zahlenwerk
`notizen/get1/zahlen_halbleiter.py`, Funktion `bericht_ap()`. Grundschaltung: 5 V, 1 kΩ, ideale Beispieldiode. Schutzdioden: R = 1 kΩ, R_L = 10 kΩ, V_DD = 5 V, U_F0 = 0,6 V. Eigene Beispiele, keine Skriptaufgaben (Skript: 15 V/−10 V/10 kΩ/5 kΩ und 14 V/15 V).

## 9. Profi-Abgleich
- Lernskript MiNa, Kapitel 7 (differentieller Widerstand, Kleinsignal, .ac-Analyse in LTspice).
- Arbeitspunktanalyse in SPICE: Newton-Raphson mit Spannungsbegrenzung an pn-Übergängen (Nagel, SPICE2, 1975; LTspice-Hilfe „.op“) — Lehrbuchwissen; Newton kriecht ohne Begrenzung von 0 V aus mit je U_T zurück und braucht 171 Schritte (Zahlenwerk).

## 10. Skript-Abgleich (S. 165–170 = PDF 171–176)
**Inhalte:** Arbeitspunkt, AP-Analyse, AP-Synthese; linear per Kirchhoff, nichtlinear grafisch oder numerisch, von Hand mit linearen Ersatzschaltungen (10.4.1). Lineares Netz: Bauteilgleichung, Maschenregel, Arbeitsgerade (10.4.2, Gl. 10.2–10.4, Bild 10.13). Diode: Gl. 10.5, 10.6, Arbeitsgerade aus Leerlauf und Kurzschluss, Kennlinie aus dem Datenblatt, ein oder mehrere Schnittpunkte, Eindeutigkeit außer bei Hysterese (10.4.3). Ideale Diode (Bild 10.14, 10.15), Diode mit 0,6 V (Bild 10.16, 10.17), Verfahren in vier Schritten, 2^n Kombinationen, Rechenbeispiele 1 und 2 (Bild 10.18–10.21), Potenzialbetrachtung (Bild 10.22).

**Korrekturen und Präzisierungen:**
1. **S. 166 „ein oder mehrere Schnittpunkte“ und „eindeutig bestimmt (Ausnahme: hysteresebehaftete Kennlinien)“:** Präzisierung. Bei monoton steigender Kennlinie gibt es genau einen Schnittpunkt; mehrere sind nur bei Kennlinien mit fallendem Ast möglich (Tunneldiode), dann entscheiden Stabilität und Vorgeschichte.
2. **S. 170 Bild 10.22 „Rechenbeispiel 2, Potentialbetrachtung“:** Die Schaltung ist die von Rechenbeispiel 1 (Diode nach Masse, Diode mit Widerstand nach −10 V), nur mit 14 V statt 15 V.
3. **S. 167 Modell „Durchlassspannung 0,6 V“:** Präzisierung. Der passende Wert hängt vom Strom ab (Durchlassspannung je Dekade 59,5 mV); bei einigen mA sind 0,7 V oft genauer.

## 11. Unabhängige Faktenprüfung (21.10.2026, zweiter Agent)
Jeder Befund wurde vor dem Einarbeiten selbst nachgerechnet.

**Falsch (korrigiert):**
1. Kompakt, Beispiel Grundschaltung: „Eine weitere Runde ändert weniger als 1 µV“ stand einen Schritt zu früh (die nächste Runde ändert noch 103 µV).
2. Konvergenz der Iteration: Der Faktor ist U_T geteilt durch die Spannung am Widerstand und praktisch unabhängig von R; die Iteration divergiert, wenn am Widerstand nicht viel mehr als U_T abfällt (0,5 V an 1 kΩ: Faktor 8).

**Ungenau (präzisiert):** fünfte Stelle der Iteration mit 25,852 mV und 1,4572·10⁻¹⁴ A; u/(2U_T) als Näherung, die Prozentwerte exakt; (I + I_S) in der exakten Stromänderung; .ac-Analyse mit vollständigem Kleinsignalmodell; Tunneldiode als hoch dotierte pn-Diode, Prinzip ohne „einzige“; Unempfindlichkeit des Stroms durch die große Spannung am Widerstand, nicht durch den großen Widerstand; Kleinsignal: Der Widerstand übernimmt die Spannungsschwankung, die Diode führt die volle Stromschwankung; r_F als Kehrwert der Steigung; „auf das 0,006-Fache“; Synthese mit der Kennlinie, 0,7 V-Modell 860 Ω; Newton ab 0 V konvergiert nach 171 Schritten, scheitert nur an der Schrittgrenze; „transzendent“ nicht als Begründung; Zusammenfassung der kompakten Fassung.
