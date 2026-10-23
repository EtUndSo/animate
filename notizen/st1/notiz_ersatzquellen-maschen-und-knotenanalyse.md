# Arbeitsnotiz: Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse (ST1, Netzwerkanalyse, Thema 2)

Dateien: `content/st1/02-netzwerkanalyse/02-ersatzquellen-maschen-und-knotenanalyse.md` (kompakt) und
`…-ausfuehrlich.md`. Frontmatter aus dem Themenplan: title „Ersatzquellen, Maschenstrom- und
Knotenpotentialanalyse“, pfad „Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse“, order 33020200,
tags „Thévenin, Norton, Maschenstromanalyse, Knotenpotentialanalyse, gesteuerte Quelle“. Quelle: PDF S. 24–31
(Abschnitte 2.4 bis 2.4.3) und S. 273–274 (Anhang C, Quellensymbole).

## 1. Ein-Satz-Prinzip

In einer linearen Schaltung hängt jede Spannung und jeder Strom linear von den unabhängigen Quellen ab; deshalb verhält sich die
Schaltung an zwei Klemmen wie eine einzige Quelle mit Innenimpedanz, und ihr Gleichungssystem wird klein, wenn man als
Unbekannte Knotenpotentiale oder Maschenströme wählt, weil diese eine der beiden Kirchhoffschen Regeln schon von
selbst erfüllen.

## 2. Schwierigkeit und Längenspannen

**schwer** (nach Umfang): drei Verfahren (Ersatzquelle, Maschen, Knoten), dazu komplexe Wechselstromrechnung und
gesteuerte Quellen, zwei bis drei Kipp-Stellen. Spannen: kompakt 1800–4000, ausführlich 3500–7000 Wörter. Die
Gleichstromfassungen der Verfahren sind in ET1 ausführlich behandelt (Ersatzquellen 6200, Maschenstrom 4100,
Knotenpotential 11 000 Wörter, alter Stil); dieser Artikel erklärt von Grund auf, verlinkt sie und ergänzt, was
in Schaltungstechnik dazukommt: Impedanzen, gesteuerte Quellen, unsymmetrische Matrix, Innenimpedanz mit Testquelle.

## 3. Vorwissen-Kette

- Kirchhoffsche Gesetze, Knoten, Zweige, Maschen: erklärt in ET1 (kirchhoffsche-gesetze, topologische-grundbegriffe);
  hier in je einem Satz erinnern, Zählung k − 1 und z − k + 1 kurz herleiten.
- Ohmsches Gesetz, Leitwert, Spannungs- und Stromquellen, reale Quellen: ET1 (ideale-und-reale-quellen), erinnern.
- Zeiger (komplexe Amplitude), Ableiten wird Multiplizieren mit jω: mmet (zeiger-und-sinussignale), erinnern; die
  Impedanzen von Spule und Kondensator hier herleiten (fehlen bisher auf der Website).
- Linearisierung, Kleinsignal-Ersatzschaltbild, Gleichquellen werden Kurzschluss bzw. Unterbrechung: ST1 Thema 1
  (arbeitspunkt-und-linearisierung), erinnern.
- Überlagerung: ET1 (superpositionsverfahren) als Verfahren; hier als Eigenschaft linearer Schaltungen aufbauen.
- Lineares Gleichungssystem, Matrixschreibweise, Determinante und Cramersche Regel: Schulmathematik bzw. HöMa;
  Cramer hier nur für 2×2 benutzen und in einem Satz erklären (das systematische Lösen folgt im nächsten Thema).
- Hier aufbauen: Linearität und gesteuerte Quellen, Satz von der Ersatzquelle mit gesteuerten Quellen, Maschen- und
  Knotenanalyse mit Aufstellen nach Augenschein, Wahl des Verfahrens.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

1. „Was ist an einer Schaltung linear, wenn Kondensatoren und Spulen drin sind?“ → Abschnitt Linearität, Text (K/A).
2. „Gilt das alles auch für Wechselstrom? Spule und Kondensator sind doch keine Widerstände.“ → Text Impedanzen (K/A).
3. „Warum ist von den k Knotengleichungen eine überflüssig?“ → Herleitungskasten Zählung; Frage-Kasten in K (K/A).
4. „Darf man für den Innenwiderstand einfach alle Quellen auf null setzen?“ (Fehlvorstellung) → Kasten (K/A).
5. „Warum hängt der Innenwiderstand des Verstärkers vom Widerstand in der Source-Leitung ab?“ → Text Kipp-Stelle (K/A).
6. „Ist die Ersatzquelle auch innen gleichwertig, etwa bei der Verlustleistung?“ → Frage (A).
7. „Ist ein Maschenstrom ein echter Strom, den man messen kann?“ → Frage (A).
8. „Darf man die Richtung der Maschenströme beliebig wählen?“ → Frage (A).
9. „Wie geht man in der Maschenanalyse mit einer idealen Stromquelle um? Umwandeln geht ja nicht.“ → Frage (A), Satz (K).
10. „Was macht man mit einer idealen Spannungsquelle in der Knotenanalyse?“ → Frage (K/A).
11. „Die Matrix muss symmetrisch sein, sonst habe ich mich verrechnet.“ (Fehlvorstellung) → Kasten (K/A).
12. „Woher weiß ich, welches Verfahren weniger Gleichungen braucht?“ → Text Verfahrenswahl (K/A).
13. „Warum rechnen Simulatoren mit Knotenpotentialen und nicht mit Maschenströmen?“ → Frage (A), Satz (K).
14. „Was ist eine gesteuerte Quelle, und wieso ist sie linear?“ → Text (K/A).

## 5. Kipp-Stellen

**K1 Ersatzquelle, auch mit gesteuerten Quellen.** Schritte: (1) Last durch eine Stromquelle I_A ersetzen;
(2) Überlagerung: innere unabhängige Quellen allein (I_A = 0) ergeben U_LL; (3) I_A allein, innere unabhängige Quellen
null, gesteuerte Quellen bleiben, weil ihr Wert von Größen in der Schaltung abhängt, ergibt −Z_i I_A; (4) Summe:
Klemmenspannung U_AB = U_LL − Z_i I_A, eine Gerade, zwei Zahlen genügen; (5) Z_i = U_LL/I_KS oder mit Testquelle.
Zahlen: Source-Schaltung, U_LL = −43,96 mV (u_q = 10 mV), I_KS = −4,938 µA, Z_i = 8,901 kΩ; Zweig aus Transistor
und R_S 81 kΩ = r_o(1 + g_m R_S) + R_S statt 41 kΩ, die Drain-Source-Strecke allein 80 kΩ statt 40 kΩ; mit falsch
abgeschalteter gesteuerter Quelle 8,04 kΩ (−9,7 %).
Abbildungen: Überlagerung (02-ersatzquelle-ueberlagerung), Testquelle (02-innenwiderstand). Herleitung: Kasten.
Beispiel: Ersatzquelle am Ausgang der Verstärkerstufe.

**K2 Knotenpotentialanalyse.** Schritte: (1) Bezugsknoten, Knotenpotentiale; jede Maschenregel ist damit von selbst
erfüllt; (2) Zweigstrom = Admittanz mal Potentialdifferenz; (3) Knotenregel je Knoten; (4) nach Potentialen ordnen:
Diagonale = Summe der Admittanzen am Knoten, Nebendiagonale = −Koppeladmittanz, rechts eingeprägte Ströme;
(5) spannungsgesteuerte Stromquelle: Einträge ±g_m in den Zeilen der Knoten, zwischen denen sie liegt, und den Spalten
der steuernden Knoten, deshalb unsymmetrisch. Zahlen: RC-Tiefpass U_2 = −j/3 V; Verstärkerstufe U_D = −23,26 mV,
Verstärkung −2,33. Abbildungen: 02-knotenpotentiale, 02-gesteuerte-quelle-matrix. Herleitung: Kasten. Beispiele.

**K3 Maschenstromanalyse.** Schritte: (1) z − k + 1 unabhängige Maschen, je ein Maschenstrom; er fließt in jeden
Knoten hinein und wieder heraus, deshalb ist jede Knotenregel von selbst erfüllt; (2) Zweigstrom = Summe bzw.
Differenz der Maschenströme; (3) Maschenregel je Masche; (4) ordnen: Diagonale = Summe der Impedanzen der Masche,
Nebendiagonale = Summe der gemeinsamen Impedanzen, jede mit σ_μ σ_ν = ±1, rechts Quellenspannungen, positiv, wenn
die Quelle den Maschenstrom antreibt.
Zahlen: RC-Tiefpass, det Z = −j3·10⁶ Ω², I_I = (0,667 + j0,333) mA, I_II = 0,333 mA. Abbildung: 02-maschenstroeme.
Herleitung: Kasten. Beispiel.

## 6. Aussortier-Liste

| Inhalt | Kat. | Kompakt | Ausführlich |
|---|---|---|---|
| lineare Schaltung, Überlagerung (Definition mit konkretem Fall vorab) | K | Text | Text |
| lineare Bauelemente R, L, C, unabhängige und gesteuerte Quellen, vier Arten | K | Text, Kurzliste | Text + Abbildung Quellensymbole |
| Impedanzen Z_R, Z_L, Z_C und Admittanzen, Herleitung über jω | K | Formel + Kasten | Formel + Kasten + Abbildung |
| Knoten, Zweige, Maschen, Zählung 2z = z + (k−1) + (z−k+1) | K | Text + Kasten | Text + Kasten + Abbildung Graph |
| Satz von der Ersatzquelle (Thévenin/Norton), Herleitung über Überlagerung | K | Formel + Kasten | dito |
| Z_i aus U_LL/I_KS, durch Abschalten der unabhängigen Quellen, mit Testquelle | K | Text | Text |
| gesteuerte Quellen bleiben beim Abschalten aktiv | K | Kipp-Stelle | Kipp-Stelle |
| Quellenumwandlung, ideale Quellen nicht umwandelbar | K | Text | Text |
| Ersatzquelle nur nach außen gleichwertig (Verlustleistung) | H | – | Frage |
| Maschenanalyse: Verfahren, Aufstellen nach Augenschein, Vorzeichen | K | Text + Kasten + Beispiel | dito |
| Maschenstrom als Rechengröße, Richtung frei | H | – | Fragen |
| ideale Stromquelle in der Maschenanalyse | H | ein Satz | Frage |
| Knotenanalyse: Verfahren, Aufstellen nach Augenschein | K | Text + Kasten + Beispiel | dito |
| spannungsgesteuerte Stromquelle in der Leitwertmatrix, Unsymmetrie | K | Kipp-Stelle | dito |
| Symmetrie ohne gesteuerte Quellen, Grund | H | ein Satz | Text |
| geerdete ideale Spannungsquelle: Potential bekannt; schwebende: nächstes Thema | H | Frage | Frage |
| Grenzen: Widerstand null, ideale Spule bei ω = 0 | H | ein Satz | Text |
| Verfahrenswahl k − 1 gegen z − k + 1, Tabelle | K | Text | Text + Tabelle |
| Simulatoren nutzen die Knotenanalyse, Gründe | H | ein Satz (Ausblick) | Frage |
| Quellensymbole (Gleich-, Kleinsignal-, gesteuerte Quellen), Kleinsignalschicksal | H | ein Satz | Abbildung + Text |
| Übertragungsfunktion des RC-Tiefpasses allgemein | V | – | Variation im Beispiel |
| Beweis über Inzidenzmatrizen | S | – | – |
| Überlagerungsverfahren als Rechenweg, Leistungsanpassung | S (ET1, verlinken) | – | Link |

## 7. Abbildungsplan (Szene-IDs st1/netzwerkanalyse/02-…)

| Nr. kompakt / ausführlich | Szene-ID | Vorlage | Inhalt und Kernaussage |
|---|---|---|---|
| 1 / 1 | 02-verstaerker-kleinsignal | schaltbild-vergleich | (a) Source-Schaltung mit V_DD 5 V, R_D 10 kΩ, R_S 1 kΩ, Gate-Vorspannung 1,25 V, Signalquelle 10 mV mit 10 kΩ, Last 10 kΩ; (b) Kleinsignal-Ersatzschaltbild mit Knoten G, D, S; (c) Ersatzquelle am Ausgang 8,90 kΩ, −43,96 mV. Eine lineare Schaltung ist durch ihre Knotenpotentiale bestimmt, und vom Ausgang aus genügen zwei Zahlen. |
| – / 2 | 02-quellensymbole | symboltabelle | Gleich-, Kleinsignal- und vier gesteuerte Quellen mit Gleichung und Kleinsignalbild. |
| 2 / 3 | 02-impedanzen | kennlinie-loglog | Betrag der Impedanz von 1 kΩ, 100 mH und 100 nF über ω von 10² bis 10⁶ 1/s, Schnittpunkt bei 10⁴ 1/s und 1 kΩ; Winkel 0, +90°, −90°. Spule und Kondensator sind frequenzabhängige Widerstände mit ±90°. |
| – / 4 | 02-topologie | netzwerkgraph | Graph der Verstärkerschaltung: 4 Knoten, 6 Zweige, Baum aus 3 Zweigen, 3 Verbindungszweige schließen je eine Masche. Zählung k − 1 = 3, z − k + 1 = 3. |
| 3 / 5 | 02-ersatzquelle-ueberlagerung | schaltbild-ueberlagerung | Netz mit Last ersetzt durch Stromquelle I_A; Teil 1 (I_A = 0) liefert U_LL, Teil 2 (unabhängige Quellen null, gesteuerte aktiv) −Z_i I_A; daneben Thévenin- und Norton-Form. Zwei Beiträge, zwei Zahlen. |
| 4 / 6 | 02-innenwiderstand | schaltbild-vergleich | Testquelle am Drain: richtig mit aktiver gesteuerter Quelle 8,90 kΩ (Transistor 81 kΩ), falsch ohne 8,04 kΩ (41 kΩ). Gesteuerte Quellen bleiben. |
| 5 / 7 | 02-maschenstroeme | schaltbild-matrix | RC-Tiefpass mit Maschenströmen I_I, I_II und Z-Matrix. |
| 6 / 8 | 02-knotenpotentiale | schaltbild-matrix | RC-Tiefpass nach Quellenumwandlung, Knoten 1, 2, Y-Matrix. |
| – / 9 | 02-zeigerbild | zeigerdiagramm | Zeiger U_q, U_1, U_2 und I_I, I_II, I_C1; beide Verfahren gleich. |
| 7 / 10 | 02-gesteuerte-quelle-matrix | schaltbild-matrix | Kleinsignalschaltung der Verstärkerstufe mit 3×3-Leitwertmatrix, g_m-Einträge hervorgehoben, unsymmetrisch. |

Kompakt 7, ausführlich 10 (Reihenfolge wie in der ausführlichen Fassung).

## 8. Zahlenwerk

`notizen/st1/zahlen_netzwerkanalyse.py`, neue Abschnitte K (Impedanzen bei ω = 10⁴ 1/s, RC-Tiefpass mit Maschen- und
Knotenanalyse, Übertragungsfunktion), L (Source-Schaltung: Arbeitspunkt U_GS 1,0 V, I_D 0,25 mA, U_DS 2,25 V;
g_m 1 mS, g_o 25 µS angenommen; Leitwertmatrix, Verstärkung −2,3256 mit Last, −4,3956 ohne; Ersatzquelle U_LL
−43,956 mV, I_KS −4,9383 µA, Z_i 8,9011 kΩ; Testquelle; r_o(1 + g_m R_S) + R_S = 81 kΩ; falsch 41 kΩ bzw.
8,0392 kΩ), M (Zählung für vier Netze, Parallelschaltung 10,81 V).

Symbole: komplexe Größen unterstrichen (U̲, I̲, Z̲, Y̲); Matrizen fett (wie ET1-Knotenpotentialartikel);
Maschenströme I̲_I, I̲_II (römische Indizes), Knotenpotentiale U̲_1, U̲_2 bzw. U̲_G, U̲_D, U̲_S; Ersatzquelle
U_LL, I_KS, Z_i, Y_i, Klemmengrößen U_AB, I_A (wie ET1, dort U_i = U_LL); Zählung k, z; Steilheit g_m, Ausgangsleitwert g_o.

## 9. Profi-Abgleich

- Satz von Thévenin/Norton mit abhängigen Quellen (Testquelle, abhängige Quellen bleiben aktiv): Alexander/Sadiku,
  Fundamentals of Electric Circuits, Kap. 4; https://en.wikipedia.org/wiki/Th%C3%A9venin%27s_theorem
- Knotenanalyse, Leitwertmatrix mit gesteuerten Quellen unsymmetrisch; Maschenanalyse: Alexander/Sadiku Kap. 3;
  https://en.wikipedia.org/wiki/Nodal_analysis
- Ausgangswiderstand der Source-Schaltung mit Source-Widerstand r_o(1 + g_m R_S) + R_S: Razavi, Design of Analog CMOS
  Integrated Circuits, Kap. 3.
- Websuche 23.10.2026, bestätigt: Bei abhängigen Quellen nur die unabhängigen abschalten, Innenwiderstand mit
  Testquelle oder als U_LL/I_KS: https://gab.wallawalla.edu/~curt.nelson/engr228/lecture/chap3_8%20zybook.pdf,
  https://jove.com/science-education/15053; Ausgangswiderstand r_o + (g_m r_o) R_S (+ R_S) bei Source-Widerstand:
  https://www.uio.no/studier/emner/matnat/ifi/INF3410/h18/forelesningsfoiler/chapter7.pdf

## 10. Skript-Abgleich (PDF-Seiten)

**Inhalte (Vollständigkeit):**
- S. 24: lineare Schaltungen: Bauelemente linear oder linearisiert; Überlagerung f(a₁u₁ + a₂u₂) = a₁f(u₁) + a₂f(u₂)
  (2.35); lineare Bauelemente R, C, L, konstante und gesteuerte Quellen; Kleinsignalbetrieb macht Verfahren für
  nichtlineare Schaltungen nutzbar; Bild 2.10 (lineare Schaltung mit Knoten und Zweigen, gesteuerte Quelle g U_i);
  Knoten (Stromverzweigung, Knotenregel; widerstandslose Leitungen bilden keinen Zweig, so verbundene Punkte sind
  ein Knoten), Zweige.
- S. 25: Maschen, Maschenregel in jedem Zeitpunkt; k, z, m; 2z Unbekannte: z Gleichungen aus dem Ohmschen Gesetz für
  Wechselstrom, k − 1 Knoten-, z − k + 1 unabhängige Maschengleichungen. 2.4.1: jedes lineare Netz mit zwei
  Klemmen durch Ersatzspannungs- bzw. Ersatzstromquelle mit Innenimpedanz ersetzbar; Nutzen (Zusammenspiel mit
  nachgeschaltetem Block, Quellenumwandlung für Maschen- und Knotenanalyse); Thévenin: Zweig ν mit Z_ν, Rest als U_0
  mit Z_0 (Bild 2.11).
- S. 26: U_0 = U_νL (2.36), Z_0 = U_νL/I_νK (2.37); Z_0 auch durch Kurzschließen der Spannungsquellen und Auftrennen
  der Stromquellen; Verfahren in 4 Schritten.
- S. 27: Norton: I_0 = I_νK (2.38), Y_0 = I_νK/U_νL (2.39), Verfahren in 4 Schritten. 2.4.2: k − 1 + z − k + 1 = z
  Gleichungen; Simulatoren (SPICE, Spectre) nutzen das Knotenpotentialverfahren; Maschenanalyse für überwiegend
  Spannungsquellen, Stromquellen vorher umwandeln; z − k + 1 Gleichungen.
- S. 28–29: Verfahren in 4 Schritten (Umwandeln, Maschen wählen mit freier Richtung, Gleichungen, Lösen); Beispiel
  Bild 2.13 (k = 3, z = 5, R₁, C₁, L, C₂, R₃, U_q1, U_q3) mit Maschengleichungen und Matrix; allgemeine Form (2.40),
  symmetrische Impedanzmatrix, Hauptdiagonale Summe der Impedanzen, Koppelimpedanzen mit Vorzeichen nach
  Gleichsinnigkeit, Z_µν = Z_νµ; Quellenspannungen rechts mit Vorzeichenregel. 2.4.3: Knotenanalyse für überwiegend
  Stromquellen, Spannungsquellen vorher umwandeln; kein Inzidenzmatrix-Beweis.
- S. 29–30: k − 1 Knotengleichungen, vorteilhaft wenn k − 1 < z − k + 1; Verfahren in 4 Schritten (Umwandeln,
  Bezugsknoten mit Potential 0, Knotengleichungen, Lösen); Beispiel Bild 2.14 (G₁, C₁, L₁, C₂, L₂, G₂, C₃, I_q1,
  I_q2) mit Knotengleichungen.
- S. 31: Matrix, allgemeine Form (2.41), YU = I_q (2.42); symmetrische Admittanzmatrix, Diagonale Summe der
  Admittanzen am Knoten, Koppeladmittanzen negativ, Y_µν = Y_νµ, sonst 0; eingeprägte Ströme positiv, wenn sie
  hineinfließen; nur Admittanzen und anregende Stromquellen (einschließlich gesteuerter); keine idealen
  Spannungsquellen, reale umwandeln (auch gesteuerte), Widerstände nicht 0, ideale Induktivitäten nicht bei
  Frequenz 0.
- S. 273–274 (Anhang C): Quellensymbole; statische Quellen (Gleichspannung, Gleichstrom), im Kleinsignalbild
  Kurzschluss bzw. Unterbrechung; Kleinsignalquellen (meist periodisch: Sinus, Rechteck, Dreieck, Sägezahn);
  gesteuerte Quellen, wenn die steuernde Größe nicht an den eigenen Anschlüssen liegt (Drainstrom, gesteuert von
  U_GS); Tabelle C.1 (Groß- und Kleinsignal-Spannungs- und -Stromquelle, gesteuerte Spannungs- und Stromquelle).
- Die Netze der Vorlage (Bild 2.10, 2.13, 2.14) werden nicht übernommen; eigene Beispiele: zweistufiger RC-Tiefpass,
  Source-Schaltung, Parallelschaltung dreier Quellen.

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 26: Z_0 durch „Kurzschluss aller Spannungsquellen und Leitungsunterbrechung aller Stromquellen“ – gilt nur für
   unabhängige Quellen; gesteuerte Quellen bleiben aktiv (sonst falsch, im Beispiel 8,04 statt 8,90 kΩ).
2. S. 27: „Sind Stromquellen enthalten, so müssen diese zunächst … in Spannungsquellen umgewandelt werden“ – nur reale
   Stromquellen lassen sich umwandeln; eine ideale bestimmt den Maschenstrom der Masche, durch die nur er fließt.
3. S. 29: „Während die Maschenstromanalyse nur geeignet ist, Schaltungen mit Spannungsquellen zu analysieren“ – zu eng.
4. S. 29/31: Impedanz- bzw. Admittanzmatrix „symmetrisch“ – nur ohne gesteuerte Quellen; mit ihnen im Allgemeinen nicht.
5. S. 29: Spannungsquellen müssen in Stromquellen umgewandelt werden – nur reale; eine ideale Spannungsquelle gegen den
   Bezugsknoten legt ein Knotenpotential fest (weniger Unbekannte), eine schwebende braucht die modifizierte
   Knotenanalyse (nächstes Thema).
6. S. 31: gesteuerte Stromquellen „anregende Stromquellen“ – sie gehören nicht auf die rechte Seite, denn ihr Wert hängt
   von unbekannten Potentialen ab; sie stehen in der Leitwertmatrix.
7. S. 31: „Ideale Induktivitäten können nicht bei der Frequenz 0 betrachtet werden“ und die folgende Regel doppelt –
   zusammengefasst: bei ω = 0 ist ihre Admittanz unendlich.
8. S. 273: Kleinsignal-Kurzschluss bzw. -Unterbrechung „folgt daraus, dass eine Spannungsquelle einen sehr geringen
   Innenwiderstand haben muss …“ – Grund ist, dass sich der Wert einer Gleichquelle nicht ändert; der Innenwiderstand
   einer realen Quelle bleibt im Kleinsignalbild stehen.
9. S. 25: „Ohm’sches Gesetz für Wechselstrom“ – gemeint ist die Zweiggleichung U̲ = Z̲ I̲ der linearen Elemente;
   gesteuerte Quellen haben eine andere Zweiggleichung.
10. S. 25: Bezeichnung m für die Maschenzahl, aber z − k + 1 für die unabhängigen; im Artikel nur z − k + 1.
11. S. 24 (2.35): f(a₁u₁ + a₂u₂) = a₁f(u₁) + a₂f(u₂) für das System als Ganzes; Quellen selbst sind keine linearen
    Zweipole im Sinn von U = Z I, sondern die Anregung.

## 11. Faktenprüfung (23.10.2026)

Unabhängige Prüfung beider Fassungen (Bericht im Scratchpad `faktencheck_st1_nw2/bericht.md`): 3 falsch, 19 ungenau,
alle Zahlen richtig. Alle Befunde nachgeprüft und eingearbeitet; Herleitungskästen und Kern nur in der ausführlichen
Fassung geändert, die kompakte daraus neu erzeugt (Kästen identisch).

**Falsch:**
- F1: „Leerlaufspannung durch Kurzschlussstrom liefert die Innenimpedanz immer“ → nur, wenn beide endlich und von null
  verschieden sind.
- F2: Grenzen der Maschen-Herleitung verwiesen auf eine Fehlvorstellung, die die kompakte Fassung nicht hat →
  selbsttragender Satz (Maschen so legen, dass nur ein Maschenstrom durch die ideale Stromquelle fließt).
- F3: Knoten als „Punkt, an dem sich Ströme verzweigen“ widersprach k = 4 (am Gate verzweigt sich nichts) → Knoten ist
  jeder Verbindungspunkt, an dem Bauelemente aneinandergrenzen; Zusatz: Zusammenfassen hintereinanderliegender
  Bauelemente ändert z − k + 1 nicht, deshalb kommen beide Zählweisen auf dieselbe Maschenzahl.

**Ungenau (eingearbeitet):**
- Zählung: „liefert genau so viele Gleichungen wie Unbekannte“, „unabhängige“ Knoten-/Maschengleichung; Grenzen nennen
  entartete Fälle (zwei verschiedene bzw. gleiche ideale Spannungsquellen parallel, verlustloser LC-Kreis aus 100 mH
  und 100 nF an einer Stromquelle bei 10⁴ 1/s).
- Frequenzgang-Variation nur für R₁ = R₂ = R und C₁ = C₂ = C.
- Reziprozität: „Netze aus Widerständen, Spulen und Kondensatoren“ statt „passive Netze“ (es gibt passive,
  nichtreziproke Bauteile); Schluss: die gesteuerte Quelle überträgt vom Gate zum Drain und hebt die Reziprozität auf.
- Symmetrie: gesteuerte Quellen brechen sie „im Allgemeinen“; „eine einzelne“ gesteuerte Stromquelle.
- Ersatzquelle: Bedingung „gesteuerte Quellen nur von Größen im Netz selbst gesteuert“; Z_i = U_LL/I_KS nur bei
  endlichem, von null verschiedenem I_KS.
- Impedanz-„Kurz gesagt“: Zeiger im eingeschwungenen Zustand, ±90° Phasenverschiebung.
- Maschen: Nebeneintrag ist die Summe der gemeinsamen Impedanzen mit σ_μ σ_ν (Herleitung Schritt 4 neu, Symmetrie aus
  der Vertauschbarkeit des Produkts); Vorzeichen s_ν → σ_ν.
- 81 kΩ und 41 kΩ gehören zum Zweig aus Transistor und R_S; die Drain-Source-Strecke allein hat 80 kΩ gegen 40 kΩ,
  genau das Doppelte (Zahlenwerk N); Gegenkopplung „wirkt einer Änderung des Drainstroms entgegen“.
- Zahlen: Testquellen-Summe mit vier Nachkommastellen (100 − 12,3457 + 24,6914 = 112,3457 µA, addiert sich exakt);
  Probe mit 8,901 kΩ und −2,326 µA; „knapp doppelt“, „knapp 10 %“.
- Amplitude, Zeiger und Betrag getrennt: Abbildung 1 nennt Zeiger und die gegenphasige Amplitude von 23,26 mV;
  Stromzeiger mit Winkel (0,745 mA bei +26,6°, 0,471 mA bei −45°); „Betrag der Verstärkung von 4,40 auf 2,33“.
- Kreisfrequenz 10⁴ 1/s „entsprechend der Frequenz 1,59 kHz“.
- Umbenennungen gegen Doppelbelegung: α₁, α₂ (a), w (v ist die Spannungsverstärkung), h_μ, h_A (c erinnert an
  Kapazität), n_M bzw. n_K in Akteuren, Matrizen und Herleitungsannahme. Index L bleibt doppelt (Z_L der Spule, R_L
  bzw. G_L der Last), weil ET1 dieselbe Konvention nutzt und beide nie in derselben Gleichung stehen.
- Zweiggleichung je Art (Impedanz, unabhängige Quelle, gesteuerte Quelle); Impedanz „jedes linearen, quellenfreien
  Zweipols“; Vorzeichen des Kurzschlussstroms in der kompakten Rechnung erklärt.
- Quellenarten: unabhängige und spannungsgesteuerte Stromquellen in die Knoten-, unabhängige und stromgesteuerte
  Spannungsquellen in die Maschengleichung; schwebende Spannungsquelle „zwischen zwei Knoten, von denen keiner der
  Bezugsknoten ist“; die modifizierte Knotenanalyse ergänzt ideale und gesteuerte Spannungsquellen.
- Kern und Prinzip: Homogenität ergänzt, „zusammenhängend“, „Sinusgrößen einer Frequenz im eingeschwungenen Zustand“,
  „linear von den unabhängigen Quellen“; „Kurz gesagt“ der Verfahren mit Bedingung an die Zweige.
- Wege zur Innenimpedanz: Stern-Dreieck-Transformation ergänzt (Link ET1); eine aktive gesteuerte Quelle ist „im
  Allgemeinen keine Impedanz und darf nicht abgeschaltet werden“.
- Kompakt: unabhängige Quelle „unabhängig von der übrigen Schaltung“; „drei reale Spannungsquellen parallel“.

## 12. Kennzahlen (nach der Faktenprüfung)

| | kompakt | ausführlich |
|---|---|---|
| Hauptpfad | 3155 Wörter (1800–4000) | 4542 Wörter (3500–7000) |
| Abbildungen | 7 | 10 |
| Beispiele | 4 | 8 |
| Quizfragen | 6 | 10 |
| Herleitungen | 6 (identisch) | 6 |
| Frage-Kästen / Fehlvorstellungen | 3 / 2 | 5 / 3 |
| Analogie / Vertiefung | – | 1 / 1 |

Checks: Build 112 Artikel (+14), KaTeX 0, widefind ×3 leer, splitalign ohne Fehler, Tabellen ≤ 330 px,
Karten = Verweise (4/4, 8/8), audit_inline 0, quellen_check leer, Abbildungsliste vollständig, Links gültig.
