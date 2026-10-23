# Arbeitsnotiz: Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse (ST1, Netzwerkanalyse, Thema 3)

Dateien: `content/st1/02-netzwerkanalyse/03-modifizierte-knotenanalyse.md` (kompakt) und `…-ausfuehrlich.md`.
Frontmatter aus dem Themenplan: title „Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse“, pfad
„Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse“, order 33020300, tags „Leitwertmatrix,
modifizierte Knotenpotentialanalyse, Cramersche Regel, Determinante“. Quelle: PDF S. 32–44 (Abschnitte 2.4.4 und
2.4.5) und S. 265–270 (Anhang A, Cramersche Regel).

## 1. Ein-Satz-Prinzip

Jedes Bauelement schreibt seinen Beitrag als festes Muster in eine Matrix, ohne den Rest der Schaltung zu kennen;
Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon als Unbekannte geführten Strom ergibt,
bringen diesen Strom als zusätzliche Unbekannte und ihre Zweiggleichung als zusätzliche Zeile mit, und das so
entstehende quadratische System liefert, wenn es eindeutig lösbar ist, jede Größe als Quotient zweier Determinanten.

(Fassung nach der Faktenprüfung: Die stromgesteuerte Stromquelle hat keine Leitwertbeschreibung und braucht trotzdem
keine Zusatzzeile; ein singuläres System hat keinen Determinantenquotienten.)

## 2. Schwierigkeit und Längenspannen

**schwer**: drei zusammenwirkende Teile (Eintragsmuster mit Bezugsknoten, Determinanten und Cramersche Regel,
Erweiterung um Zweigströme mit sechs Mustern) und dazu der Frequenzgang als Anwendung; drei Kipp-Stellen. Spannen:
kompakt 1800–4000, ausführlich 3500–7000 Wörter. Der Stoff überschneidet sich mit dem Exkurs im alten ET1-Artikel
„Das Knotenpotentialverfahren“ (alter Stil); dieser Artikel ist gleich tief oder tiefer und verlinkt ihn.

## 3. Vorwissen-Kette

- Knotenregel, Bezugsknoten, Knotenpotentialanalyse, Leitwertmatrix (Diagonale, Nebeneinträge), gesteuerte Stromquelle
  in der Knotengleichung, Symmetrie: erklärt in ST1 Thema 2 (ersatzquellen-maschen-und-knotenanalyse), erinnern und
  verlinken.
- Zeiger, Impedanz und Admittanz von R, L, C: ST1 Thema 2 und mmet (zeiger-und-sinussignale), erinnern.
- Kleinsignal-Ersatzschaltbild der Verstärkerstufe (g_m = 1 mS, g_o = 25 µS): ST1 Thema 1 und 2, erinnern.
- Begleitmodell des Newton-Verfahrens: ST1 Thema 1 (ausführlich), erinnern (nur ausführliche Fassung).
- Idealer OPV, Leerlaufverstärkung v_D, virtueller Kurzschluss, invertierender Verstärker: ET1 Kap. 12
  (idealer-opv-und-rueckkopplung, opv-grundschaltungen), erinnern und verlinken.
- Lineares Gleichungssystem in Matrixform: Schulmathematik, in einem Satz erinnern. Determinante, Laplace-Entwicklung,
  Sarrus, Cramersche Regel, Adjunkte: hier aufbauen (kein Artikel auf der Website).
- Dezibel, Dekade, logarithmische Achse: hier in je einem Satz erklären (ausführlich).
- Hier aufbauen: Eintragsmuster, vollständige Matrix und Streichen des Bezugsknotens, Vorzeichenregel aus zwei
  Faktoren, Zweigströme als Unbekannte, Muster von Spannungsquelle, Impedanz, Tor, gesteuerten Spannungsquellen,
  stromgesteuerten Quellen und Nullor, gemeinsamer Nenner und Pole.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

| # | Frage (in den Worten einer Leserin) | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Muss ich beim Eintragen wissen, in welche Richtung der Strom wirklich fließt?“ (Fehlvorstellung) | Eintragsmuster | Fehlvorstellung | beide |
| 2 | „Warum steht ein Bauteil an Masse nur einmal auf der Diagonalen?“ | Bezugsknoten | Text (Streichen) | beide |
| 3 | „Wozu schreibt man Zeile und Spalte der Masse überhaupt hin, wenn man sie danach streicht?“ | vollständige Matrix | Frage-Kasten | ausführlich |
| 4 | „Warum ergibt die Entwicklung nach jeder Zeile dieselbe Zahl?“ | Determinante | Herleitung (Grenzen, Beweisidee) | beide |
| 5 | „Warum rechnen Simulatoren nicht mit der Cramerschen Regel?“ | Cramer | Text (ausführlich), Frage-Kasten (kompakt) | beide |
| 6 | „Warum kann man eine ideale Spannungsquelle nicht eintragen?“ | MNA | Text | beide |
| 7 | „Geht es nicht auch ohne zusätzliche Unbekannte?“ (Superknoten) | MNA | Frage-Kasten | beide |
| 8 | „Der zusätzliche Strom ist doch der Strom, den die Quelle liefert.“ (Fehlvorstellung) | MNA | Fehlvorstellung | beide |
| 9 | „Wozu braucht man ein Bauteil mit null Ohm?“ | Impedanzmuster | Frage-Kasten | beide |
| 10 | „Was bedeutet es, wenn die Determinante null wird?“ | Schwingkreis | Frage-Kasten | ausführlich |
| 11 | „Die Nullor-Zeile legt die Ausgangsspannung fest.“ (Fehlvorstellung) | Nullor | Fehlvorstellung | ausführlich |
| 12 | „Ist ein Nullor ein echtes Bauteil?“ | Nullor | Frage-Kasten | ausführlich |
| 13 | „Warum haben alle Knotenspannungen dieselben Eckfrequenzen?“ | Frequenzgang | Text | ausführlich (kompakt ein Satz) |
| 14 | „Warum heißt diese Stelle Pol, und warum knickt der Betrag gerade bei der Eckfrequenz ab?“ | Frequenzgang | Frage-Kasten | ausführlich |
| 15 | „Gehört eine gesteuerte Stromquelle nicht als Quelle auf die rechte Seite?“ (Fehlvorstellung) | VCCS-Muster | Text, Halbsatz mit Link auf Thema 2 | beide |

## 5. Kipp-Stellen

**K1 Eintragsmuster und Bezugsknoten.** Schritte: (1) Knotengleichung jeder Zeile als „abfließende Ströme gleich
eingespeiste Quellenströme“; (2) jedes Bauelement erscheint nur in den Zeilen seiner Knoten; (3) Admittanz: +Y auf den
Diagonalplätzen, −Y auf den Kreuzungsplätzen; gesteuerte Stromquelle: Zeilen der Stromknoten, Spalten der Steuerknoten;
Stromquelle: nur rechte Seite; (4) Matrix ist die Summe der Muster; (5) vollständige Matrix mit Bezugsknoten hat
Zeilen- und Spaltensummen null und ist singulär; Zeile und Spalte des Bezugsknotens streichen. Zahlen: Verstärkerstufe,
vollständige 4×4-Matrix (0, G, D, S) mit Diagonale 1,3 / 0,1 / 0,225 / 2,025 mS, reduziert genau die Matrix aus
Thema 2. Abbildungen: 03-eintragsmuster-knoten, 03-vollstaendige-matrix. Herleitung: Kasten (Muster aus der
Knotenregel) und Kasten (Summen null, Streichen). Beispiel: Verstärkerstufe Bauteil für Bauteil. Analogie
(ausführlich): doppelte Buchführung.

**K2 Modifizierte Knotenanalyse.** Schritte: (1) Strom des Elements als zusätzliche Unbekannte, Zählrichtung von a
durch das Element nach b (in den Pluspol hinein); (2) Spalte: +1 in Zeile a, −1 in Zeile b; (3) Zeile: Zweiggleichung
U_a − U_b − Z I_z = U_q; (4) System bleibt quadratisch. Zahlen: RC-Tiefpass mit idealer Quelle 1 V, 4×4-System,
det = −3j, U_3 = −j/3 V, I_z = −(2 + j)/3 mA (abgegeben 0,745 mA bei +26,6°). Abbildungen: 03-mna-spannungsquelle,
03-eintragsmuster-mna. Herleitung: Kasten. Beispiel: RC-Tiefpass. Fehlvorstellung: Vorzeichen des Zusatzstroms.

**K3 Cramersche Regel.** Schritte: (1) Determinante als Entwicklung (Definition), 2×2 und 3×3 als Formeln;
(2) Spalte ν durch rechte Seite ersetzen; (3) Quotient; (4) nach der Zeile oder Spalte mit den meisten Nullen
entwickeln; (5) Nenner für alle Unbekannten gleich, daraus die Pole. Zahlen: det Y = 0,043 mS³, D_D = −1 mS²·µA,
U_D = −23,26 mV, D_S = 0,2 → 4,65 mV; Rechenaufwand n = 20: Cramer 8,8·10¹⁹ gegen Gauß 3060 Multiplikationen.
Abbildungen: 03-cramer-laplace, 03-rechenaufwand, 03-bode. Herleitung: Kasten (2×2 und 3×3 aus der Definition),
Kasten (Cramer über Kofaktoren). Beispiel: Verstärkerstufe.

## 6. Aussortier-Liste

| Inhalt | Kat. | Kompakt | Ausführlich |
|---|---|---|---|
| Zeilen = Knotengleichungen, Y_μν = Strom in Gleichung μ je Volt an Knoten ν | K | Akteure | Akteure |
| Muster Admittanz, gesteuerte Stromquelle, unabhängige Stromquelle | K | Formel, Herleitung, Abb. | ebenso |
| Matrix als Summe der Muster | K | Kurz gesagt | ebenso |
| Vorzeichenregel aus zwei Faktoren (Zeile: Strom ab/zu, Spalte: Steuer +/−) | K | Text | Text |
| Bezugsknoten: vollständige Matrix, Zeile und Spalte streichen | K | Text, Herleitung | Text, Herleitung, Abb. |
| Zeilen- und Spaltensummen null, vollständige Matrix singulär | H | ein Satz in der Herleitung | Kurz gesagt, Frage-Kasten |
| doppelte Buchführung als Analogie | H | nein | Analogie |
| gesteuerte Stromquelle gehört in die Matrix (nicht rechte Seite) | K | Halbsatz, Link Thema 2 | ebenso |
| Determinante: Definition durch Entwicklung, Schachbrett, 2×2, 3×3 (Sarrus), 4×4 | K | Formel, Herleitung | ebenso, 4×4 im Text |
| Laplace: jede Zeile/Spalte gleich (Satz, Beweisidee) | K | Satz in der Formel, Grenzen | ebenso |
| Cramersche Regel | K | Formel, Herleitung, Beispiel | ebenso |
| Nenner für alle Unbekannten gleich | K | Kurz gesagt | ebenso |
| Entwicklung nach der dünnsten Zeile/Spalte | H | Text | Text |
| Rechenaufwand n! gegen n³, Simulatoren mit LU und dünn besetzten Matrizen | H/V | Frage-Kasten | Unterabschnitt mit Abb. |
| det(Aᵀ) = det(A), transponiertes System, Inverse über die Adjunkte (2×2, 3×3) | V | nein | Unterabschnitt mit Herleitung, Beispiel |
| Grenze der Knotenanalyse: ideale Spannungsquelle, Z = 0, Spule bei ω = 0, Spannungsquelle gesteuert | K | Text | Text |
| MNA: Zusatzstrom, Spalte ±1, Zeile Zweiggleichung, quadratisch | K | Schritte, Formel, Herleitung | ebenso |
| Vorzeichenkonvention des Zusatzstroms (in den Pluspol, SPICE-Konvention) | K | Fehlvorstellung | ebenso |
| Superknoten als Handverfahren | H | Frage-Kasten | Frage-Kasten |
| Muster Impedanz (auch Z = 0), Tor (reale Quelle) | K | Formel, Herleitung | ebenso |
| Spule bei Gleichstrom und Resonanz, det = 0 | H | Frage-Kasten (null Ohm) | Frage-Kasten, Beispiel Schwingkreis, Abb. |
| gesteuerte Spannungsquelle (VCVS) | K | Formel, Herleitung | ebenso |
| stromgesteuerte Quellen, Steuerstrom als Unbekannte (0-V-Quelle) | H | ein Satz | Text, Herleitung |
| Strommesser als 0-V-Quelle, Transitfrequenz f_T = g_m/(2π C_gs) | H | nein | Beispiel, Abb. |
| f_T mit C_gd (1,345 GHz) | V | nein | Variation |
| Nullor als Grenzfall v → ∞, Nullator und Norator | K | Formel, Herleitung, Abb., Beispiel | ebenso |
| endliche Leerlaufverstärkung 200 000 (−9,99945) | H | Einordnung | Variation |
| Determinante im Nenner aller Knotenspannungen, Pole als Nullstellen | H | ein bis zwei Sätze | Abschnitt mit Formel, Herleitung |
| Eckkreisfrequenz, Bode-Diagramm, −3 dB, −20 dB/Dekade, Phase | H | nein | Abschnitt, Abb., Beispiel |
| Pole mit Source-Widerstand (3,38 MHz und 287 MHz) | V | nein | Variation |
| Begriff „Pol“ (komplexe Frequenz) | V | nein | Frage-Kasten |
| Eintragsmuster auch für den Arbeitspunkt (Begleitmodell, Newton-Schritt 1,3077 V) | H | ein Satz in Bedeutung | Bedeutung und Ausblick mit Zahl |
| Leistungsprobe am Tiefpass (0,333 mW) | V | nein | Einordnung |
| SPICE-Bedienung, Netzlistensyntax eines bestimmten Programms | S | nein | nein |
| Leibniz-Formel mit Permutationen | S | nur Name und Idee (Herleitung Entwicklungssatz) | Name und Idee (Entwicklungssatz, Transponierte), keine Permutationsrechnung |
| Tableau-Analyse, Index differentiell-algebraischer Systeme, ideale Übertrager, Gyratoren | S | nein | nein |
| Eingangsimpedanz über Testquelle (Übung der Vorlage) | S | nein (Thema 4) | nein (Thema 4) |

## 7. Abbildungsplan (Szene-IDs st1/netzwerkanalyse/03-…)

| Nr. ausf. | Nr. kompakt | Szene | Vorlage | Inhalt | Kernaussage | Abschnitt |
|---|---|---|---|---|---|---|
| 1 | 1 | 03-netzliste-matrix | netzliste-matrix | RC-Tiefpass mit idealer 1-V-Quelle, Netzliste (5 Zeilen), 4×4-Matrix mit Einträgen in Bauteilfarben | Jedes Bauteil schreibt ein festes Muster; die Matrix ist ihre Summe | Worum es geht |
| 2 | 2 | 03-eintragsmuster-knoten | musterkarten | Muster Admittanz, gesteuerte Stromquelle, Stromquelle | Ein Bauelement erscheint nur in den Zeilen seiner Stromknoten und den Spalten seiner Steuerknoten | Matrix Bauteil für Bauteil |
| 3 | – | 03-vollstaendige-matrix | schaltbild-matrix | Verstärkerstufe, vollständige 4×4-Matrix mit Summen 0, Zeile/Spalte 0 gestrichen | Summen null; Streichen liefert die lösbare Matrix | Bezugsknoten |
| 4 | 3 | 03-cramer-laplace | matrix-schema | Spalte D ersetzt, Entwicklung nach der Spalte mit einer 1, Schachbrett, Sarrus | Jede Unbekannte ist ein Quotient zweier Determinanten | Cramer |
| 5 | – | 03-rechenaufwand | kennlinie-semilog | Multiplikationen über n: Cramer (n+1)·M(n) gegen Gauß (n³ − n)/3 + n² | Determinanten wachsen wie n!, Elimination wie n³ | Rechenaufwand |
| 6 | 4 | 03-mna-spannungsquelle | schaltbild-matrix | ideale Quelle zwischen a und b, Leitwertmatrix ergänzt um Spalte ±1 und Zeile ±1 | Strom als Unbekannte, Zweiggleichung als Zeile | MNA |
| 7 | 5 | 03-eintragsmuster-mna | musterkarten | Muster Impedanz, Tor, VCVS, CCCS, CCVS, Nullor | Alle Elemente, deren Strom sich weder aus Potentialen noch aus einem geführten Strom ergibt, haben dasselbe Gerüst | weitere Muster |
| 8 | – | 03-schwingkreis | schaltbild-kurve | Stromquelle, 100 nF ∥ 100 mH; det(ω) = ω²LC − 1 von 0 bis 2·10⁴ 1/s | Mit Impedanzmuster bleibt die Determinante bei ω = 0 endlich, bei Resonanz wird sie null | Spule |
| 9 | – | 03-strommesser-transitfrequenz | schaltbild-kurve | Ersatzschaltbild mit 0-V-Quelle als Strommesser; |β| über f doppeltlogarithmisch, 1 bei 1,59 GHz (1,345 GHz mit C_gd, Grenzwert 0,167) | Die 0-V-Quelle schließt den Ausgang kurz und liefert den Kurzschlussstrom als Unbekannte | Strommesser |
| 10 | 6 | 03-nullor-verstaerker | schaltbild-matrix | invertierender Verstärker mit Nullor, 4×4-Matrix | Nullor: Eingangsbedingung als Zeile, Ausgangsstrom als Spalte | Nullor |
| 11 | – | 03-bode | bode | Verstärkerstufe ohne R_S mit C_gs, C_L; Betrag und Phase, Asymptoten, Eckfrequenzen 3,58 MHz und 159 MHz | Die Eckfrequenzen gehören zu den Polen, den Nullstellen der Determinante | Frequenzgang |

Ausführlich 11 Abbildungen (Richtwert 6–12), kompakt 6 (3–6). Jede besprochene Schaltung hat ihr Schaltbild:
Tiefpass (1), Verstärkerstufe (3, in Thema 2 auch 02-verstaerker-kleinsignal), Schwingkreis (8), Strommesser (9),
OPV (10), Stufe mit Kapazitäten (11).

## 8. Zahlenwerk

`notizen/st1/zahlen_netzwerkanalyse.py`, neue Abschnitte O bis Y (Ausgabe `.txt`):
- O: vollständige Leitwertmatrix der Verstärkerstufe Bauteil für Bauteil, Summen, Streichen, Lösung.
- P: Entwicklungen nach allen Zeilen/Spalten (0,043 mS³), Sarrus, Cramer (D_G 0,43, D_D −1, D_S 0,2), 2×2 Tiefpass
  (D = 3j, D_2 = 1), Rechenaufwand, Transponierte, Adjunkte (Tiefpass und Stufe).
- Q: MNA Tiefpass 4×4 (det −3j; Zähler −3j, −1 − j, −1, −1 + 2j), Tor-Variante 3×3, Leistungsprobe.
- R: MNA Verstärkerstufe mit Tor (det −0,43, D_D 10, I_sig = 0).
- S: Schwingkreis 100 mH ∥ 100 nF an 1 mA: det = ω²LC − 1; ω = 0, 5000, 10⁴, 2·10⁴.
- T: Strommesser, β = −g_m/(jωC_gs), f_T 1,5915 GHz, mit C_gd 1,3451 GHz; |β| mit C_gd 132,63 / 13,26 / 1,337 /
  0,213 bei 10 MHz / 100 MHz / 1 GHz / 10 GHz, Grenzwert C_gd/(C_gs + C_gd) = 0,1667; offener Drain U_D = −40·U_G.
- U: Nullor, invertierender Verstärker (det −0,1, D_2 0,1, U_A −1 V), endliche v_D; Eingänge vertauscht: Nullor
  det +0,1, wieder −1 V; gesteuerte Quelle −10,00055 (2·10⁵) bzw. −10,00011 (10⁶), obwohl mitgekoppelt.
- V: Frequenzgang ohne R_S (Eckfrequenzen 3,581 MHz und 159,155 MHz, 12,96 dB), Datenreihe, mit R_S (3,377 MHz,
  286,674 MHz); 7,071 mV am Gate bei ω_G; nur G_L verdoppelt: 3,0769 und 5,1725 MHz, Produkt 15,915 MHz; ganzer
  Leitwert am Drain verdoppelt: 2,2222 und 7,162 MHz.
- W: singuläre Fälle; X: stromgesteuerte Quellen; Y: Begleitmodell als Muster (1,3077 V).

## 9. Profi-Abgleich

- Ljubljana, Computer-Aided Optimization, „Modified nodal analysis“:
  https://zrojec.fe.uni-lj.si/cao/modified-nodal-analysis/ — Strom der Spannungsquelle fließt in den Pluspol hinein;
  VCVS, CCVS und idealer OPV bekommen den Ausgangsstrom als Unbekannte, die CCCS nicht; ein Steuerstrom, der keine
  Unbekannte ist, wird durch eine in Reihe geschaltete 0-V-Quelle zu einer; „Modified nodal analysis is the approach
  used in most circuit simulators today“.
- Swarthmore (E. Cheever), „Modified Nodal Analysis“: https://lpsa.swarthmore.edu/Systems/Electrical/mna/MNA3.html —
  Blöcke G, B, C, D; C ist für unabhängige Spannungsquellen die Transponierte von B, mit gesteuerten Quellen nicht;
  D ist ohne gesteuerte Quellen null (mit Impedanzmustern steht dort −Z).
- Wikipedia, „Modified nodal analysis“: https://en.wikipedia.org/wiki/Modified_nodal_analysis — Strom der unabhängigen
  Spannungsquelle von Plus nach Minus durch die Quelle; Beispielmatrix [[G, −G, 1], [−G, G, 0], [1, 0, 0]].
- Queiroz 1995, „Compact Nodal Analysis With Controlled Sources Modeled by Ideal Operational Amplifiers“:
  https://www.coe.ufrj.br/~acmq/papers/compact1995.pdf — idealer OPV in der MNA: Ausgangsstrom als Unbekannte,
  Gleichung e₊ = e₋.

Erklärweg daraus: Konvention „Strom in den Pluspol“ ausdrücklich als Fehlvorstellung behandeln; die Transponierten-
Symmetrie bei unabhängigen Quellen als Probe nennen; Steuerströme über 0-V-Quellen.

## 10. Skript-Abgleich (PDF-Seiten)

**Definitionen, Formeln, Aussagen (Vollständigkeit):**
- S. 32: YU = I_q; n + 1 Knoten → n Unbekannte, ein Knoten Bezugspotential; U_i Knotenpotentiale, I_q Anregung durch
  unabhängige Stromquellen; Zeilen = Knotengleichungen; Y_ij Verkopplung Strom an i mit Spannung an j; Initialisieren
  mit null, Einträge je Bauelement; Muster der Admittanz mit I_Y = Y(U_i − U_k); Leitwert und Kondensator als
  Spezialfälle; Impedanz über Y = 1/Z, singulär bei Z = 0 (Spule bei ω = 0).
- S. 33: Muster der spannungsgesteuerten Stromquelle als verallgemeinerte Admittanz (Spalten p, q); Muster der
  unabhängigen Stromquelle nur im Anregungsvektor; dünn besetzte Matrizen; symbolische Lösung bis Dimension 4 mit
  Cramer; Simulatoren mit Sparse-Matrix-Verfahren.
- S. 34: Muster in der Wechselstromanalyse und in den linearisierten Matrizen der Arbeitspunktbestimmung; Beispiel
  Verstärker in Schritten mit vollständiger 3×3-Matrix inkl. Bezugsknoten.
- S. 35: gesteuerte Quelle eintragen, Bezugsknoten: oberste Zeile und linke Spalte weglassen; Cramer für U_2, U_1.
- S. 36: Frequenzverhalten, Zeitkonstantenform, Pole ω_i = G_q/C_i, ω_o = G_o/C_o, Bode-Diagramm, U_2/U_1 mit einem Pol.
- S. 37–38: zweites Beispiel mit Leitwert G_s, alle typischen Muster, Determinanten, Transimpedanz, Grenzfall G_s → ∞.
- S. 39: MNA, Grenze der Knotenanalyse, ideale Spannungsquelle: U_q Anregung, I_q Unbekannte, U_i − U_k = U_q,
  Erweiterung um eine Zeile und Spalte.
- S. 40–41: Spannungsquelle 0 V als Strommesser, Stromverstärkung −g/(jωC_i), Transitfrequenz f_T = g/(2π C_i);
  Verstärker mit idealer Spannungsquelle am Eingang, U_o/U_q = −g/(G_o + jωC_o).
- S. 41–42: Muster Impedanz (U_i − U_k) − Z I_Z = 0 mit −Z auf der Diagonalen; reale Spannungsquelle bzw. Tor
  (U_i − U_k) − Z_q I_q = U_q; Bezeichnung Tor/port.
- S. 42–43: VCVS (U_i − U_k) − A(U_p − U_q) = 0, auch mit Innenimpedanz; Nullor als Grenzwert A → ∞: U_p − U_q = 0;
  Beispiel OPV-Schaltung mit Nullor, Cramer, U_2 = −R_2/R_1 U_ein.
- S. 44: Merksatz: ideale Spannungsquellen und solche mit beliebigem Innenwiderstand, Widerstände null, gesteuerte
  Spannungsquellen, stromgesteuerte Quellen, ideale Induktivitäten bei Frequenz 0.
- S. 265–266: allgemeines LGS, reguläre Matrix (det ≠ 0), Cramer x_s = det A_s/det A mit ersetzter Spalte s;
  Determinante über Laplace-Entwicklung nach Zeile oder Spalte, Streichungsmatrix.
- S. 267–268: rekursive Definition bis 1×1, Schachbrettmuster, 1×1, 2×2, 3×3 (Entwicklung, Sarrus), 4×4.
- S. 269–270: Beispiel 3×3 (nicht übernommen); det A = det Aᵀ; transponiertes System über Zeilenersatz; Inverse über
  die Adjunkte, Formeln für 2×2 und 3×3.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 33: Verweis „Gleichungssystem 2.15“ statt 2.43.
2. S. 35/36: C_0 statt C_o in (2.46), (2.48), (2.50), (2.52); „iω“ statt „jω“ in (2.47).
3. S. 36: „Pole haben die Kreisfrequenzen ω_i, ω_o“ – das sind Eckkreisfrequenzen; die Nullstellen des Nenners liegen
   bei der komplexen Frequenz −ω_i bzw. −ω_o. Im Artikel getrennt benannt.
4. S. 36: Bode-Diagramm nur als Betragsverlauf beschrieben; zum Bode-Diagramm gehört auch die Phase. Im Artikel beides.
5. S. 37: „Netzwerk mit nur zwei Knoten“ – das erste Beispiel hat drei Knoten (zwei ohne Bezugsknoten).
6. S. 38: Klammerfehler in (2.60); „Kurzschluss des Leitwertes G_s“ meint G_s → ∞, also Kurzschluss von Knoten 3 gegen
   Masse.
7. S. 39: „Ideale Spannungsquellen und Impedanzen können nicht berücksichtigt werden“ – Impedanzen lassen sich als
   Y = 1/Z eintragen, solange Z ≠ 0; nur Z = 0 (Kurzschluss, Spule bei ω = 0) scheitert.
8. S. 40: f_T = g/(2π C_i) gilt nur ohne Gate-Drain-Kapazität; mit ihr g_m/sqrt(C_gs(C_gs + 2C_gd)) ≈
   g_m/(C_gs + C_gd). Im Artikel als Variation.
9. S. 41, Bild 2.24: „mit einer realen Spannungsquelle“ – im Gleichungssystem steht eine ideale.
10. S. 42: „reale Spannungsquelle … als Serienschaltung einer idealen Stromquelle und einer idealen Impedanz“ – richtig:
    ideale Spannungsquelle in Reihe mit einer Impedanz.
11. S. 44: Zwischenschritt der Determinante D ohne den Vorzeichenfaktor (−1)^(4+1); Ergebnis −R_1 G_2 stimmt; in
    (2.75) U_q statt U_ein.
12. S. 44: „Stromgesteuerte Quellen sind möglich“ ohne Muster; im Artikel ergänzt (Steuerstrom muss Unbekannte sein,
    notfalls über eine 0-V-Quelle).
13. S. 265: [G] neben [Y] für dieselbe Matrix; {U} „Spannungsvektor der unabhängigen Spannungen“ – es sind die
    unbekannten Knotenpotentiale.
14. S. 266: „D ∈ ℝ“ – in der Wechselstromrechnung ist die Determinante komplex.
15. S. 267: (−1)^(i+1) statt (−1)^(1+1) beim ersten Summanden der 2×2-Entwicklung.
16. S. 268: Unterklammer „A22A23 − A22A13“ statt „A12A23 − A22A13“; in der letzten Zeile der 3×3-Entwicklung
    „−A31(…)“ statt „+A31(…)“.
17. S. 269: „nach dem Laplace’schen Entwicklungssatz“, gerechnet wird aber nach Sarrus.
18. S. 269: det A = det Aᵀ „für die Transponierte einer quadratischen regulären Matrix“ – gilt für jede quadratische
    Matrix.

## 11. Selbstprüfung und Faktenprüfung

**Selbstprüfung (B6):** Verstärkerstufe mit Steilheit, Ausgangsleitwert und Zählrichtung von g_o eingeführt;
„Das Zusammenspiel“ zu K1 in vier Schritten; „umgewandelte Quelle“ und Einheitsmatrix erklärt; Cramer-Schritte 1–4
mit „So liest man das“ abgestimmt; Begründungen für die Transit-Variation und das Produkt aus Verstärkung und
Eckfrequenz; Gegenkopplung als Voraussetzung des Nullor-Modells („nur dann stellt sich die Lösung tatsächlich ein“);
Frequenzgang-Formelkasten auf zwei Zeilen (Handybreite).

**Faktenprüfung (Hintergrund-Agent, Bericht im Scratchpad):** 2 FALSCH, 26 UNGENAU, alle Zahlen bestätigt, kein
Quellenbezug. Alle Befunde nachgeprüft und eingearbeitet:
- F1 Prinzip und Gerüst-Sätze: „weder aus den Knotenpotentialen noch aus einem schon geführten Strom“, „wenn es
  eindeutig lösbar ist“; Hinweis, dass die stromgesteuerte Stromquelle das Gerüst nicht braucht (Text, Abb. 7/5,
  Kern, Akteure).
- F2 „Lastleitwert verdoppelt“ → ganzer Leitwert am Drain; nur G_L verdoppelt: 3,08 und 5,17 MHz, Produkt 15,9 MHz.
- U1 Nullor: Annahme „Ausgang so zurückgeführt, dass U endlich bleibt, während v wächst“; Grenzen mit vertauschten
  Eingängen (−1 V, −10,00055, Mitkopplung, Komparator).
- U2 Pol als Stelle s = −ω_p der komplexen Frequenz, Eckkreisfrequenz getrennt benannt; „Nullstelle der Determinante“
  statt „Faktor“ (Kurz gesagt, Kern, Abb. 11, Frage-Kasten, kompakter Absatz). Nachgeschärft beim Gegenlesen: Kurz
  gesagt und Kern mit der Bedingung „Einträge Polynome in der komplexen Frequenz“ (Gegenbeispiel: Leitwertmatrix mit
  1/(jωL) und getrenntem Teilnetz, dort hat U_1 einen Pol bei s = 0, die Determinante aber keine Nullstelle);
  Spulen deshalb als Impedanz eintragen.
- U3/U4 Strommesser: 0-V-Quelle in Reihe; in Abb. 9a schließt sie den Ausgang kurz (Definition der
  Transitfrequenz); gestrichelte Kurve mit Werten bis 10 GHz und Grenzwert 0,167; Winkel +90°; gemessener Strom ist
  der Quellenstrom mit umgekehrtem Vorzeichen.
- U5 Symbole: Δ\underline U statt U_0 (U_0 wäre mit Knotenpotentialen verwechselbar); Index κ in der Cramer-Herleitung;
  RC-2×2-System mit U_2, U_3 (Knoten 2 und 3 aus Abb. 1), Ausgang U_3; Inverse auf Knoten 2/3 umgestellt.
- U6 Zählrichtung: Stromquelle von b nach a durch die Quelle (speist in a); „wie bei Admittanzen und gesteuerten
  Quellen“ statt „wie bei jedem Element“.
- U7 Zeiger: Vorzeichen zeigt bei Gleichgrößen die Richtung, bei Zeigern die Phasenlage zur Zählrichtung.
- U8/U9 Kurz gesagt und Quiz mit den Bedingungen det ≠ 0 bzw. Steuerstrom als Unbekannte.
- U10–U26 Einzelformulierungen (ideale Spannungsquelle in Reihe, Transponierte über die Leibniz-Idee statt Induktion,
  Vorzeichenregel „Potential mit plus in der Zweiggleichung“, Singularität der vollständigen Matrix, Symmetrie nur
  ohne gesteuerte Quellen, „meisten Schaltungssimulatoren, etwa SPICE“, 1/√2-Fache = 7,07 mV, G-Namen in Abb. 3,
  Zählung der Elimination für n = 2, Besetzung einer Zeile, „Multiplikationen und Divisionen“, Analogie-Grenze,
  CCCS-Probe mit Zählrichtung, Annahme „endliche Admittanz oder spannungsgesteuerte Stromquelle“, Hinweise auf die
  ausführliche Fassung).

**Bewusst beibehalten:** R_1, R_2 im invertierenden Verstärker neben R_1, R_2 im RC-Tiefpass. Beide Beispiele haben
ihr eigenes Schaltbild mit Werten (Abb. 1 bzw. Abb. 10/6), kommen in keinem gemeinsamen Satz oder Kasten vor, und
−R_2/R_1 ist die Schreibweise des verlinkten Artikels „Die OPV-Grundschaltungen“; die Leserin erkennt die
Verstärkungsformel dort wieder. Gleiches gilt für „Knoten 1“ (Tiefpass, Schwingkreis, Verstärker): Knotennummern
gelten je Schaltbild.

## 12. Kennzahlen (Stand Commit)

- Kompakt: 3284 Wörter Hauptpfad (Spanne 1800–4000), Lesezeit ≈ 19 min; 8 Herleitungen (H1, H2, H3, H4, H7, H8, H9,
  H11, wortgleich mit der ausführlichen Fassung), 4 Beispiele, 6 Abbildungen, 3 Frage-Kästen, 2 Fehlvorstellungen,
  6 Quizfragen, 8 Formelkästen.
- Ausführlich: 5577 Wörter Hauptpfad (Spanne 3500–7000), Lesezeit ≈ 33 min; 12 Herleitungen, 8 Beispiele,
  11 Abbildungen, 6 Frage-Kästen, 3 Fehlvorstellungen, 1 Analogie, 10 Quizfragen, 10 Formelkästen.
- Keine Gedankenstriche, kein „nicht … sondern“, Verbotsliste leer, audit_inline 0, quellen_check leer.
