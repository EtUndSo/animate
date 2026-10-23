# Arbeitsnotiz: Testquellen und Transientenanalyse linearer Schaltungen (ST1, Netzwerkanalyse, Thema 4)

Dateien: `content/st1/02-netzwerkanalyse/04-testquellen-und-transientenanalyse.md` (kompakt) und `…-ausfuehrlich.md`.
Frontmatter aus dem Themenplan: title „Testquellen und Transientenanalyse linearer Schaltungen“, pfad „Elektrotechnik /
3. Semester / Schaltungstechnik 1 / Netzwerkanalyse“, order 33020400, tags „Testquelle, Eingangswiderstand,
Ausgangswiderstand, Transientenanalyse, Zeitkonstante“. Quelle: PDF S. 45–53 (Abschnitte 2.4.6, 2.5, 2.5.1 bis zum
Beginn von 2.6).

## 1. Ein-Satz-Prinzip

Die Matrix des Gleichungssystems beschreibt die Schaltung, die rechte Seite ihre Anregung: Testquellen fragen die
Schaltung ab, ohne die Matrix zu verändern, und in der Zeit bringt das Begleitmodell jedes Kondensators und jeder Spule
die Vorgeschichte als Stromquelle auf die rechte Seite, sodass jeder Zeitschritt wieder ein lineares Gleichungssystem
ist.

## 2. Schwierigkeit und Längenspannen

**schwer** nach Umfang: zwei Teile (Testquellen; Transientenanalyse mit numerischer Integration, Begleitmodellen,
Stabilität und nichtlinearer Erweiterung), drei Kipp-Stellen. Spannen: kompakt 1800–4000, ausführlich 3500–7000
Wörter.

## 3. Vorwissen-Kette

- Knotenpotentialanalyse, Leitwertmatrix, gesteuerte Quellen; Ersatzquelle mit Innenimpedanz, Testspannung am Drain
  (8,90 kΩ), gesteuerte Quellen bleiben beim Abschalten aktiv: ST1 Thema 2 (ersatzquellen-maschen-und-knotenanalyse),
  erinnern und verlinken.
- Eintragsmuster, modifizierte Knotenanalyse mit Zusatzstrom (gezählt in den Pluspol), Cramersche Regel, Inverse und
  Streichungsmatrix, Pole als Nullstellen der Determinante, Eckfrequenzen 3,58 MHz und 159 MHz der Stufe mit
  Kapazitäten: ST1 Thema 3 (modifizierte-knotenanalyse), erinnern und verlinken.
- Arbeitspunkt, Kleinsignalgrößen klein geschrieben, Newton-Verfahren mit Begleitmodell (Leitwert g und Stromquelle
  I_eq,ν), MOS-Diode mit Arbeitspunkt 1 V: ST1 Thema 1 (arbeitspunkt-und-linearisierung), erinnern und verlinken.
- Kondensator I = C dU/dt, Laden über einen Widerstand, Zeitkonstante τ = RC: ET1 Kap. 4 (laden-und-entladen),
  erinnern und verlinken.
- Spule U = L dI/dt: im Text in einem Satz erinnern (ET1-Artikel zur Induktivität noch alter Stil).
- Zweitor: ET1 Kap. 7 (zweitore), verlinken; Vierpole folgen als ST1 Thema 5.
- Ableitung als Steigung, Tangente, Exponentialfunktion, Taylor-Entwicklung bis zum quadratischen Glied, Mittelwertsatz:
  Schulmathematik, in je einem Satz erinnern.
- Hier aufbauen: Testquelle, Abschalten als Nullsetzen der rechten Seite, Impedanz als Diagonaleintrag der Inversen,
  Testspannungsquelle am Eingang, Eingangsadmittanz, Übertragungsfunktion, Ausgangsimpedanz, Übertragung zwischen
  beliebigen Knoten, Arbeitspunkt-Argument, Ersatzzweitor mit Rückwirkungsgrenze, explizites und implizites
  Euler-Verfahren, Fehlerordnung, Stabilität, Begleitmodelle von Kondensator und Spule, Steifheit, Sprungantwort der
  Stufe und Zeitkonstanten als Kehrwerte der Eckkreisfrequenzen, verschachtelte Schleifen für nichtlineare Schaltungen.

## 4. Fragenkatalog (Stelle → Antwortort → Fassung)

| # | Frage (in den Worten einer Leserin) | Stelle | Antwortort | Fassung |
|---|---|---|---|---|
| 1 | „Warum nimmt man für die Impedanz eine Stromquelle und keine Spannungsquelle?“ | Teststrom | Text, Schritte | beide |
| 2 | „Muss der Teststrom 1 A sein, und hält die Schaltung das aus?“ | Teststrom | Frage-Kasten | beide |
| 3 | „Eine abgeschaltete Spannungsquelle nimmt man aus der Schaltung heraus.“ (Fehlvorstellung) | Ausgangsimpedanz | Fehlvorstellung | beide |
| 4 | „Ist der Strom der Testspannungsquelle nicht der Zusatzstrom aus der Lösung?“ | Eingangsadmittanz | Frage-Kasten | beide |
| 5 | „Warum darf man an einem inneren Knoten keine Spannungsquelle anschließen, sie liefert doch nur ein kleines Signal?“ | innere Knoten | Text | beide |
| 6 | „Regt eine Stromquelle den Knoten nicht anders an als im Betrieb, stimmt die Übertragung dann noch?“ | innere Knoten | Text und Herleitung | beide |
| 7 | „Warum bestimmt man die Ausgangsimpedanz nicht aus Leerlaufspannung und Kurzschlussstrom?“ | innere Knoten | Frage-Kasten | beide |
| 8 | „Eingangsadmittanz, Verstärkung und Ausgangsimpedanz beschreiben jede Schaltung vollständig.“ (Fehlvorstellung) | Ersatzzweitor | Fehlvorstellung | ausführlich (kompakt ein Satz) |
| 9 | „Das implizite Euler-Verfahren ist genauer als das explizite.“ (Fehlvorstellung) | Euler | Fehlvorstellung | beide |
| 10 | „Woher kennt das implizite Verfahren die Steigung am Ende des Schritts, bevor es den Wert dort kennt?“ | Euler | Frage-Kasten | beide |
| 11 | „Im Zeitschritt wird der Kondensator zu einem bloßen Widerstand.“ (Fehlvorstellung) | Begleitmodell | Fehlvorstellung (ausführlich), Satz im Text (kompakt) | beide |
| 12 | „Wie sieht das Modell einer Spule aus?“ | Begleitmodell | Unterabschnitt | ausführlich |
| 13 | „Warum wird bei 5 ns gerade das Gate instabil und nicht der Drain?“ | Verstärkerstufe | Frage-Kasten | ausführlich |
| 14 | „Ist die Matrix in jedem Zeitschritt dieselbe?“ | Verstärkerstufe | Text | beide |
| 15 | „Wie passen Newton-Verfahren und Zeitschritte zusammen?“ | nichtlinear | Abschnitt mit Abbildung und Beispiel | ausführlich (kompakt zwei Sätze) |

## 5. Kipp-Stellen

**K1 Testquellen verändern die Schaltung nicht.** Schritte: (1) Matrix = Schaltung, rechte Seite = unabhängige
Quellen; (2) eine ideale Stromquelle erscheint nur rechts; (3) abgeschaltet ist sie ein Leerlauf, die Gleichungen sind
die der Schaltung ohne sie; (4) Abschalten aller übrigen unabhängigen Quellen setzt nur ihre Einträge rechts null
(Stromquelle Leerlauf, Spannungsquelle Kurzschluss), gesteuerte bleiben; (5) Lösung = Spalte μ der Inversen mal I_T,
Impedanz = Diagonaleintrag. Zahlen: 1 µA in den Drain ergibt 8,901 mV, also 8,90 kΩ (= Innenimpedanz aus Thema 2);
det 0,02275 mS³, Unterdeterminante 0,2025 mS². Spannungsquelle ohne Gleichanteil an S: Triodenbereich, U_D 0,426 V,
I_D 0,457 mA, Ausgangsleitwert 0,648 mS statt 25 µS; Drain an Masse: I_D = 0, g_m = 0. Abbildungen: 04-teststrom-ausgang,
04-innerer-knoten. Herleitungen: H1 (Impedanz = Diagonaleintrag), H2 (Übertragung unabhängig von der Anregungsart).
Beispiele: Ausgangsimpedanz der Stufe; Übertragung mit Teststrom. Analogie (ausführlich): Voltmeter und Amperemeter.

**K2 Begleitmodell.** Schritte: (1) I = C dU/dt; (2) implizites Euler-Verfahren: Steigung am Schrittende = I_{n+1}/C;
(3) nach I_{n+1} aufgelöst: Leitwert G_C = C/h und bekannter Strom G_C U_n; (4) beide als Eintragsmuster, G_C an den
Plätzen von jωC; (5) neuer Wert wird Vorgeschichte des nächsten Schritts, Matrix bleibt bei festem h. Zahlen: RC mit
h = 10 µs: G_C = 10 mS, U_1 = 90,9 mV, U_2 = 173,6 mV, U_10 = 0,614 V (exakt 0,632 V); ohne Stromquelle 90,9 mV in jedem
Schritt. Abbildung: 04-begleitmodell-kondensator. Herleitung H6. Beispiel: RC-Glied. Fehlvorstellung: „wird zum
Widerstand“.

**K3 Stabilität explizit/implizit.** Schritte: Abweichung vom Endwert wird je Schritt mit 1 − h/τ bzw. 1/(1 + h/τ)
multipliziert; Grenze 2τ; implizit stabil für jedes h; Steifheit in Schaltungen mit sehr verschiedenen Zeitkonstanten.
Zahlen: h = 3τ: explizit 3, −3, 9, −15, 33 V, implizit 0,750, 0,938, 0,984 V; Stufe mit h = 5 ns: am Gate −4 gegen 1/6,
explizit 50, −150, 650, −2550 mV. Genauigkeit: h = τ/10 nach τ +0,0192 V und −0,0177 V, halbes h halbe Fehler.
Abbildungen: 04-euler-verfahren, 04-verstaerker-transiente. Herleitungen H4 (Euler und Fehlerordnung), H5
(Fehlerfaktoren). Beispiel: erste Zeitschritte der Stufe. Fehlvorstellung: „implizit genauer“.

## 6. Aussortier-Liste

| Inhalt | Kat. | Kompakt | Ausführlich |
|---|---|---|---|
| Testquelle darf die Schaltung (Matrix) nicht ändern; Stromquelle nur rechte Seite | K | Schritte, Abb. | ebenso |
| Abschalten = rechte Seite null; Stromquelle Leerlauf, Spannungsquelle Kurzschluss, gesteuerte aktiv | K | Schritt 4 | Schritt 4, Merke |
| Z_μ = U_μ/I_T = Diagonaleintrag der Inversen (Cramer) | K | Formel, H1, Beispiel | ebenso, Übertragungsimpedanz |
| 1 A im Simulator, Spannung in V = Impedanz in Ω | H | Frage-Kasten | Frage-Kasten |
| Eingangsadmittanz mit Testspannungsquelle, I_ein = −I_z | K | Text, Definition, Frage | ebenso |
| Übertragungsfunktion A_V aus demselben Lauf | K | Definition, Beispiel | ebenso |
| Ausgangsimpedanz mit abgeschalteter Eingangsquelle, gleiche Matrix | K | Definition, Beispiel | ebenso, Rechenaufwand |
| abgeschaltete Spannungsquelle = Kurzschluss, nicht entfernen | K | Fehlvorstellung | Fehlvorstellung |
| Spannungsquelle an innerem Knoten verschiebt den Arbeitspunkt | K | Text mit Zahlen | Text, Abb. |
| Topologie zwischen Arbeitspunkt und Kleinsignal gleich | K | Merke | Merke |
| Übertragung zwischen beliebigen Knoten mit Teststrom; gleich wie bei Spannungsanregung | K | Formel, H2 | ebenso, Beispiel |
| kein Kurzschlussversuch am Ausgang (Arbeitspunkt) | H | Frage-Kasten | Frage-Kasten |
| Ersatzzweitor Y_ein, A_V, Z_aus; Norton A_V/Z_aus | H | Absatz mit Zahlen | Abschnitt, Formel, H3, Beispiel |
| Rückwirkung: Ersatzzweitor nur rückwirkungsfrei exakt | H | ein Satz | Fehlvorstellung, Grenzen |
| Analogie Voltmeter/Amperemeter | V | nein | Analogie |
| numerische Integration statt geschlossener Lösung, Transientenanalyse | K | Text | Text |
| explizites und implizites Euler-Verfahren | K | Formel, H4 | ebenso |
| Fehlerordnung (Schritt ∝ h², über feste Zeit ∝ h) | H | Satz mit Zahlen | Text, H4 |
| Stabilität, Grenze 2τ, Fehlerfaktoren | K | Formel, H5, Abb. | ebenso |
| Trapezregel, Klingeln, Schrittweitensteuerung, Gear | V | nein | Vertiefung |
| Begleitmodell Kondensator, jωC-Plätze | K | Schritte, Formel, H6, Beispiel | ebenso |
| Begleitmodell Spule | H | ein Satz | Unterabschnitt, H7, Abb. |
| Schaltung mit gesteuerter Quelle im Zeitschritt, gleiche Matrix je Schritt | K | Text, Beispiel, Abb. | ebenso |
| Steifheit, Zeitkonstanten fs bis ms | H | Satz | Text, Frage-Kasten |
| exakte Sprungantwort der Stufe, Zeitkonstanten = 1/Eckkreisfrequenz | H | Zahlen | Formel, H8 |
| nichtlineare Transiente: Newton innen, Zeit außen | H | zwei Sätze | Abschnitt, Abb., Beispiel |
| Teststromquelle zwischen zwei Knoten (Tor ohne Masse), Impedanz aus den Spalten a und b der Inversen | H | Satz | Satz |
| Lauf A liefert zugleich die Übertragung zu jedem inneren Knoten | H | Halbsatz | Halbsatz |
| Begleitmodell der Trapezregel (2C/h, Quelle mit I_n) | V | nein | Vertiefung mit Formel |
| Jacobi-Matrix als Matrix des Newton-Durchlaufs | V | nein | Satz |
| Vorlagenschaltung mit 1 Ω, 0,1 F, 10 S | S | nein | nein (eigenes Beispiel) |
| Netzlistensyntax, Bedienung eines Simulators | S | nein | nein |

## 7. Abbildungsplan (Szene-IDs st1/netzwerkanalyse/04-…)

| Nr. ausf. | Nr. kompakt | Szene | Vorlage | Inhalt | Kernaussage | Abschnitt |
|---|---|---|---|---|---|---|
| 1 | 1 | 04-uebersicht | schaltbild-matrix | Schaltung mit Testspannungsquelle am Eingang, Teststromquelle am Ausgang, feste Matrix mit drei rechten Seiten; Kondensator im Zeitschritt als Leitwert mit Stromquelle | Testquellen und Zeitschritte ändern nur die rechte Seite | Worum es geht |
| 2 | 2 | 04-teststrom-ausgang | schaltbild-matrix | Stufe mit 1 µA in den Drain, Matrix, Lösung = Spalte D der Inversen | Teststromquelle nur rechts; Diagonaleintrag = Impedanz | Teststromquellen |
| 3 | 3 | 04-testspannung-eingang | schaltbild-matrix | RC-Tiefpass, MNA-Matrix, zwei rechte Seiten, falsche Variante (Quelle entfernt) | zwei Läufe an derselben Matrix; abgeschaltet = Kurzschluss | Testspannungsquelle |
| 4 | – | 04-innerer-knoten | schaltbild-vergleich | Stufe mit Gleichgrößen, Teststromquelle gegen Spannungsquelle an S | Spannungsquelle verschiebt den Arbeitspunkt | innere Knoten |
| 5 | – | 04-ersatzzweitor | schaltbild | Ersatzzweitor (Thévenin und Norton) mit Werten der Stufe | drei Kenngrößen aus zwei Läufen | Ersatzzweitor |
| 6 | 4 | 04-euler-verfahren | zeitverlauf-schritte | Ladekurve mit Euler-Werten h = τ/2; Folgen bei h = 3τ | Steigung am Anfang gegen am Ende; explizit schaukelt sich auf | Euler |
| 7 | 5 | 04-begleitmodell-kondensator | schaltbild-ersatz | Kondensator = G_C ∥ Stromquelle; Matrixplätze; RC mit h = 10 µs | Kondensator wird Leitwert, Vorgeschichte Stromquelle | Begleitmodell |
| 8 | – | 04-begleitmodell-spule | schaltbild-ersatz | Spule = h/L ∥ Stromquelle I_n; RL-Glied | Spule hält ihren Strom über die Stromquelle | Spule |
| 9 | 6 | 04-verstaerker-transiente | schaltbild-kurve | Stufe mit Begleitmodellen, u_G und u_D exakt und implizit, explizit am Gate | gleiche Matrix je Schritt; schnelle Zeitkonstante begrenzt explizit | Verstärkerstufe |
| 10 | – | 04-spice-ablauf | blockbild | Ablaufdiagramm mit innerer Newton- und äußerer Zeitschleife, Newton-Durchläufe der MOS-Diode | zwei Schleifen, jedes Mal ein lineares System | nichtlinear |

Ausführlich 10 Abbildungen (Richtwert 6–12), kompakt 6 (3–6). Jede besprochene Schaltung hat ihr Schaltbild:
Verstärkerstufe (2, 4, 5), RC-Tiefpass (3), RC-Glied (6, 7), RL-Glied (8), Stufe mit Kapazitäten (9), MOS-Diode mit
Kondensator (10, als Teilbild).

## 8. Zahlenwerk

`notizen/st1/zahlen_netzwerkanalyse.py`, neue Abschnitte Z bis AF (Ausgabe `.txt`):
- Z: Testquellen an der Verstärkerstufe: 1 µA in D → 8,9011 mV (det 0,02275 mS³, Unterdeterminante 0,2025 mS²), mit
  R_L 4,7093 kΩ, Gate 10 kΩ, Übertragungen −2,3256 und 0,4651 mit Teststrom wie mit Signalquelle; MNA mit idealer
  Testspannungsquelle am Gate: A_V = −4,3956, Y_ein = 0, Z_aus = 8,9011 kΩ, A_V/Z_aus = −0,49383 mS
  (= g_m G_S/(g_m + g_o + G_S)), mit Last −2,3256.
- AA: RC-Tiefpass: Y_ein = (0,6667 + 0,3333j) mS, Z_ein = (1,2 − 0,6j) kΩ, A_V = −j/3, U_2/U_q = (1 − j)/3,
  Z_aus = (0,3333 − 0,6667j) kΩ, Strom in der kurzgeschlossenen Quelle −j/3 mA, falsch (Quelle entfernt)
  (0,2 − 0,6j) kΩ, mit 1 kΩ Last Y_ein = (0,6 + 0,3j) mS (−10 %), U_3 = (0,1 − 0,2j) V wie im Modell; Übertragung
  Knoten 2 → 3 (1 − j)/2 bei beiden Anregungen.
- AB: Arbeitspunkt 1,25 / 0,25 / 2,5 V, 0,25 mA; Drain an Masse: I_D = 0, g_m = 0, g_ds 1,5 mS; Source an Masse:
  Triode U_D 0,4258 V, I_D 0,4574 mA, g_m 0,8517 mS, g_ds 0,6483 mS (25,9-fach); Gate an 0 V: gesperrt.
- AC: RC-Glied τ = 0,1 ms: h = τ/10 nach τ: explizit 0,65132 (+0,01920), implizit 0,61446 (−0,01766), Trapez 0,63243
  (+0,000307), exakt 0,63212; h = τ/20: +0,00939, −0,00901, +0,000077; ein Schritt: +0,004837, −0,004253 (h²/2τ² 0,005);
  Faktoren; h = 3τ: explizit 3, −3, 9, −15, 33 V, implizit 0,75, 0,9375, 0,9844, Trapez 1,2, 0,96, 1,008; h = 2τ
  Schwingung 2/0 V; Datenreihe h = τ/2.
- AD: Begleitmodell C: G_C = 10 mS (100 Ω), U_1..U_5 = 0,09091, 0,17355, 0,24869, 0,31699, 0,37908 V, U_10 = 0,61446 V;
  ohne Stromquelle 0,09091 V je Schritt; Trapez-Begleitmodell 2C/h = 20 mS, U_10 = 0,632427 V; Spule h/L = 0,1 mS,
  U_1 = 0,90909 V, I_1 = 0,09091 mA, I_2 = 0,17355 mA, I_10 = 0,61446 mA.
- AE: Stufe mit C_gs, C_L: τ_G 1 ns, τ_D 44,444 ns, Endwert −44,444 mV, exakte Werte (−3,8217 mV bei 5 ns, −29,6833 mV
  bei 50 ns, −39,6522 mV bei 100 ns, −44,3912 mV bei 300 ns), Anstiegszeit 97,66 ns; implizit h = 5 ns: Matrix
  (0,12; 0 / 1; 2,225) mS, u_G1 8,3333 mV, u_D1 −3,7453 mV, u_D2 −7,7361 mV, 50 ns −28,7877 mV (Fehler 0,896 mV),
  300 ns −44,3686 mV; h = 1 ns Fehler 0,185 mV bei 50 ns; explizit h = 5 ns: u_G 50, −150, 650, −2550 mV (Faktor −4);
  explizit h = 0,5 ns: −39,7129 mV bei 100 ns; mehr als 150 Schritte.
- AF: MOS-Diode mit 1 nF, h = 0,1 µs: 2 Newton-Durchläufe je Schritt unterhalb der Schwelle (bis 1,151 µs), 3 bis 4
  darüber, 142 in 50 Schritten; U(5 µs) = 0,99146 V; Zeitkonstanten 4 µs und 0,8 µs.

## 9. Profi-Abgleich

- Qucs, Technische Dokumentation, Begleitmodelle: https://qucs.sourceforge.net/tech/node26.html — Kondensator bei
  implizitem Euler: Leitwert C/h parallel zu einer Quelle (C/h)·V_n, bei der Trapezregel 2C/h und zusätzlich I_n; Spule
  dual mit L/h in Reihe bzw. h/L parallel; Eintragsmuster wie ein Leitwert plus Stromquelle.
- Universität Ljubljana, Computer-Aided Optimization, Transientenanalyse:
  https://fides.fe.uni-lj.si/~zigar/CAO/_lectures/_09_lecture_more.php — implizite Verfahren (Backward Euler Ordnung 1,
  Trapez Ordnung 2, Gear), explizite Verfahren werden bei steifen Schaltungen instabil, Schrittweite durch die kürzeste
  Zeitkonstante begrenzt; Schrittweitensteuerung über den lokalen Fehler, nach Sprüngen Ordnung 1.
- MIT 18.086 (G. Strang), Stabilität von Euler-Verfahren: https://live.ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/e548f1cb5f6c6bc9a5c90ee5180a3b91_am51.pdf
  — explizites Euler für y′ = a y stabil nur für −2 ≤ a h ≤ 0, implizites für jedes h (A-stabil).
- EDN, „Making impedance measurements in SPICE“: https://www.ednasia.com/?p=4536 — Impedanz mit einer Teststromquelle
  von 1 A in der Wechselstromanalyse ablesen.

Erklärweg daraus: Abschalten als Nullsetzen der rechten Seite; Impedanz als Spalte bzw. Diagonaleintrag der Inversen
(verbindet mit Thema 3); Stabilität über den Faktor je Schritt; Begleitmodell als Eintragsmuster mit C/h an den Plätzen
von jωC; Trapez und Schrittweitensteuerung nur als Vertiefung.

## 10. Skript-Abgleich (PDF-Seiten)

**Definitionen, Formeln, Aussagen (Vollständigkeit):**
- S. 45: Ein- bzw. Ausgangsimpedanz in einen Knoten hinein (Bild 2.31); Testschaltung darf Y nicht verändern;
  Teststromquelle beeinflusst nur den Anregungsvektor; Z_1 = U_1/I_T (2.76); andere unabhängige Quellen deaktivieren;
  System (2.77) mit I_T in Zeile 1; Simulator mit 1 A: U_1 in V = Z_1 in Ω. Testspannungsquelle für die
  Eingangsadmittanz Y_1 = I_q/U_q (2.78).
- S. 46: Teststromquelle dabei deaktiviert (I_T = 0); MNA-System (2.79) mit −1 in der Spalte von I_q (Strom in den
  Knoten) und Zeile (1, 0, …, 0 | U_q); Y_1 = I_q/1 V im Simulator; A_V = U_2/U_q aus derselben Lösung; Ausgangsimpedanz
  mit deaktivierter Signalquelle und Teststromquelle an Knoten 2 (2.80); Matrix für beide Testfälle unverändert, nur
  andere Anregung.
- S. 47: Übertragung zwischen beliebigen Knoten nicht mit Testspannungsquelle (Kurzschluss für andere Frequenzen,
  Gleichspannungsarbeitspunkt), sondern mit Teststromquelle (unendlicher Innenwiderstand); A_V = U_2/U_1, Z_1 = U_1/I_T;
  zusätzliche Teststromquelle an Knoten 2 für die Ausgangsimpedanz; deaktivierte Teststromquellen beeinflussen nichts;
  innere Parameter eines Ersatzzweitores (Bild 2.35: Y_1, A_V U_1, Z_2).
- S. 48: Y_1 und A_V mit aktiver Testspannungsquelle und I_T = 0; Z_2 mit U_q = 0 und I_T aktiv; Umrechnung reale VCVS
  (A_V, Z_2) in reale VCCS (g_m = A_V/Z_2, Y_2 = 1/Z_2); kein Kurzschlussversuch, Topologie bleibt; Kurzschluss am
  Ausgang würde den Arbeitspunkt verändern. Merkkasten: deaktivierte Teststromquelle = Leerlauf, Testspannungsquelle =
  Kurzschluss; Topologie zwischen Arbeitspunkt und Kleinsignalanalyse unverändert. 2.5: Einschaltverhalten mit
  Kondensator = Differentialgleichungssystem; analytisch nur für kleine Schaltungen; numerische Lösung =
  Transientenanalyse (SPICE); Grundidee: energiespeichernde Elemente durch zugeordnetes Modell ersetzen,
  Knotenanalyse je Zeitschritt; numerische Integration.
- S. 49: Schaltung Bild 2.36 (Stromquelle 1 A gepulst, R_1 = 1 Ω, C_1 = 0,1 F, g_m = 10 S, R_2 = 1 Ω; nicht übernommen);
  Forward Euler (2.82) mit h = t_{n+1} − t_n, Bild 2.37 links; Fehler proportional h; Backward Euler (2.83), Steigung bei
  t_{n+1}; „bessere Genauigkeit, weniger empfindlich gegen die Schrittweite“.
- S. 50: zwei Schritte (Integration auf Strom-Spannungs-Beziehung, zugeordnetes lineares Modell); U = Q/C (2.84),
  I = dQ/dt (2.85), (2.86)–(2.89), G_eq = C/h (2.90), I_{n+1} = G_eq(U_{n+1} − U_n) (2.91), I_eq = G_eq U_n (2.92).
- S. 51: Bild 2.38 (Modell: G_eq parallel I_eq, in den oberen Knoten); Bild 2.39 (Modell der Beispielschaltung);
  Gleichungssystem (2.93), Iterationsvorschrift (2.94); Anregung aus Konstantstromquellen und I_eq; Bild 2.40
  (Verlauf U_2 und I_q).
- S. 52: zugeordnete Modelle auch für aufwendigere Verfahren; Genauigkeit und Stabilität hängen von Verfahren und
  Schrittweite ab, moderne Simulatoren schalten beides dynamisch um; 2.5.1 Ablaufdiagramm Bild 2.41 (Arbeitspunkt,
  Modelle der Nichtlinearitäten, Laden, Lösen, Konvergenz, neuer Arbeitspunkt, Zeitschritt, Endzeit, Modelle für C, L);
  Newton plus Integration = SPICE-Algorithmus, lineares dünn besetztes MNA-System, Sparse-Matrix-Solver.
- S. 53 oben: Beschreibung des Ablaufs (Startwert z. B. 0, Jacobi-Matrix, Konvergenz, Zustand U(n), Schleife).

**Fehler und Ungenauigkeiten (stillschweigend korrigiert):**
1. S. 45: „der jeweilige Quellstrom wird zu 0 gesetzt“ – bei unabhängigen Spannungsquellen wird die Quellenspannung null
   (Kurzschluss); gesteuerte Quellen bleiben aktiv.
2. S. 46: Überschrift „Testspannungsquelle zur Bestimmung der Ausgangsimpedanz“ – verwendet wird eine Teststromquelle,
   die Signalspannungsquelle ist abgeschaltet.
3. S. 47 (2.81): Das MNA-System enthält die Zeile (1, 0, …, 0 | 0) der Spannungsquelle an Knoten 1; sie erzwingt U_1 = 0,
   der Teststrom flösse ganz in die Quelle, und A_V = U_2/U_1 wäre unbestimmt. Für Bild 2.34 (ohne Spannungsquelle) gilt
   die Knotenanalyse Y U = I_T e_1. Im Artikel richtig dargestellt.
4. S. 47: „Kurzschluss für andere Frequenzen“ – genauer legt eine Spannungsquelle zwischen Knoten und Masse das
   Potential des Knotens vollständig fest, auch seine Gleichspannung; im Artikel mit Arbeitspunktzahlen erklärt.
5. S. 47/48: A_V ist die Leerlaufverstärkung (I_T = 0), Z_2 die Ausgangsimpedanz bei kurzgeschlossenem Eingang
   (U_q = 0); das Ersatzzweitor ist nur ohne Rückwirkung exakt, sonst hängt Y_1 von der Last ab. Im Artikel ergänzt.
6. S. 48: Umrechnung g_m = A_V/Z_2 ohne Zählrichtung; für eine Quelle, die in den Ausgangsknoten einspeist, gilt
   A_V/Z_2, in Transistorrichtung (aus dem Knoten heraus) −A_V/Z_2. Im Artikel mit Zählrichtung.
7. S. 48: fehlendes Verb („… aktivierter Teststromquelle I_T [bestimmt] werden“); unerheblich.
8. S. 49: „Die Abweichung des Wertes x_{n+1} vom idealen Wert ist proportional zur Schrittweite h“ – der Fehler eines
   Schritts ist proportional zu h², der über eine feste Zeit angesammelte proportional zu h.
9. S. 49: „Das Backward-Euler Verfahren liefert eine bessere Genauigkeit“ – beide Verfahren sind von erster Ordnung, die
   Fehler gleich groß mit entgegengesetztem Vorzeichen (+0,0192 V gegen −0,0177 V bei h = τ/10); der Vorteil ist die
   Stabilität. Im Artikel als Fehlvorstellung.
10. S. 51 (2.93)/(2.94): Vorzeichen der Begleitquelle falsch. Mit I_eq = G_eq (U_{1,n} − U_{2,n}) und der
    Kondensatorspannung U_1 − U_2 muss die rechte Seite I_q + I_eq bzw. −I_eq lauten; mit I_q − I_eq und +I_eq läuft die
    Iteration gegen falsche Werte (nachgerechnet mit h = 0,1 s: zweiter Schritt U_C = 0,065 V statt 1,627 V, Endwerte
    U_1 = 0,12 V und U_2 = −0,32 V statt 1 V und −10 V; Skript scratchpad/pruef_vorlage_294.py).
11. S. 51 Bild 2.40: U_2 strebt gegen +10 V; mit der gezeichneten Richtung der gesteuerten Quelle (Knoten 2 nach Masse)
    und der Matrix (2.93) ist der Endwert −10 V (U_1 = 1 V, 10 A durch R_2 nach Masse gezogen); Zeitkonstante
    R_th C = 12 Ω · 0,1 F = 1,2 s. Bild und Schaltung passen im Vorzeichen nicht zusammen. Nicht übernommen.
12. S. 52 Bild 2.41: „Wähle Zeitschritt h(n)“ neben „t(n+1) = t(n) + h(n+1)“ – Indizes uneinheitlich.
13. S. 53: „Ausgehend von einem initialen Arbeitspunkt, z. B. 0“ – die Transiente beginnt beim Gleichspannungs-
    arbeitspunkt; 0 ist nur der Startwert der Newton-Iteration, die ihn berechnet.
14. S. 47: Die ideale Stromquelle beeinflusst das Gleichspannungsverhalten nur dann nicht, wenn sie keinen Gleichanteil
    hat; im Artikel steht deshalb „Stromquelle ohne Gleichanteil“.

## 11. Selbstprüfung und Faktenprüfung

**Selbstprüfung (B6, 20 Tests):** ergänzt wurden das Rechnen mit Zeigern als Voraussetzung, das
Kleinsignal-Ersatzschaltbild beim ersten Auftreten, die Streichungsmatrix in der kompakten Fassung, eine Erklärung der
Taylor-Entwicklung im Herleitungskasten der Euler-Verfahren, die Zeitkonstanten der Stufe als RC-Glieder an jedem Knoten
(Formeln jetzt nach den Akteuren), die MOS-Diode in der kompakten Fassung, die Gegenkopplung bei der wirksamen
Steilheit; Wörter mit „einfach“ aus Fragen und Fehlvorstellungen entfernt; zu breite Formeln und Tabellen auf
Handybreite umgebaut (Analogie-Tabelle ohne lange Komposita, Prinzip-Tabelle ohne „Differentialgleichung“).

**Faktenprüfung (Hintergrund-Agent, Bericht im Scratchpad):** 2 FALSCH, 22 UNGENAU, alle übrigen Zahlen bestätigt, kein
Quellenbezug, alle 13 Vorlagenkorrekturen bestätigt (10 und 11 nachgerechnet). Alle Befunde nachgeprüft und
eingearbeitet (Skript scratchpad/faktenfix_tq.py, 41 Ersetzungen in A, 26 in der Kompakt-Vorlage):
- F1 Exaktwert bei 0,5τ: 0,393 V statt 0,394 V (doppelt gerundet); in der Abbildungsliste zusätzlich 0,941 statt 0,942.
- F2 wirksame Steilheit in K mit Zählrichtung: aus dem Drain heraus −0,494 mS, also 0,494 mA je Volt in den Drain,
  „rund halb so groß wie g_m“.
- U1 implizites Verfahren am Gate: klingt zu langsam ab (Faktor 1/6 statt exp(−5) = 0,007), nicht „zu stark gedämpft“.
- U2 Euler-Fehler „annähernd gleich groß“ bzw. „in führender Ordnung“ (+19,2 und −17,7 mV); Herleitungsschritt 4 mit
  dem Hinweis, dass die Steigung am Ende mit dem berechneten Wert gebildet wird.
- U3 Kurz gesagt und Kern zum Begleitmodell mit der Bedingung „implizites Euler-Verfahren“; Trapez-Begleitmodell
  (2C/h, Quelle 2C/h·U_n + I_n, 20 mS, 0,6324 V) in der Vertiefung.
- U4 Übertragung: Annahme det Y ungleich null ergänzt, Kurz gesagt „sofern die Schaltung mit der Stromquelle lösbar ist“,
  Grenzen mit dem Gegenbeispiel ohne Masseverbindung.
- U5 Merke allgemeiner (Teststromquelle parallel zum gesuchten Anschlusspaar, Testspannungsquelle, wo ein Kurzschluss
  nichts ändert, auch in Reihe in einen Zweig); Teststromquelle zwischen zwei Knoten a und b in beiden Fassungen.
- U6 bis U22: wenige Kondensatoren noch geschlossen lösbar; Kern ohne in K undefinierte Symbole; Stabilität als
  Voraussetzung der Fehlersumme; negativer Realteil (−0,667 − 0,333j) mS; Stabilitätsdefinition „abklingen“ passend zur
  Grenze 2τ; Abbildung 1 „mit fester Schrittweite“; Steigung U_q/τ = 10 V/ms; Grenzen bei det Y = 0 getrennt; nur der
  Signalanteil des Kurzschlussstroms ist null (0,5 mA Gleichstrom aus R_D); Zählrichtung im Kurz gesagt und in
  Abbildung 5b; Schwelle exakt 1,15 µs, gerechnet im Schritt 1,1 auf 1,2 µs; reale Stromquelle in K; Lage der Folgen
  über die Faktoren 0,9, 0,905, 0,909; Probe der Übertragungs-Herleitung erklärt; Vierpol, Trapezregel, Laplace,
  Anstiegszeit, G_L, C_gs und C_L, Inverse beim ersten Auftreten erklärt; Übertragung zu jedem inneren Knoten aus Lauf A;
  Jacobi-Matrix; Link in H6 auf die kompakte Fassung von Thema 1; „genau −2“ im Quiz.

**Bewusst beibehalten:** $U_q$ bezeichnet die Quellenspannung sowohl der Testspannungsquelle (Zeiger, unterstrichen)
als auch der Gleichspannungsquelle des RC-Glieds; beides ist die Quellenspannung der jeweils betrachteten Schaltung, wie
in Thema 3 ($\underline U_q$ = 1 V am Tiefpass). Ein eigenes Symbol für den Sprung bräuchte einen Namen, der nicht mit
$U_0$ (Wert bei n = 0) oder $U_S$ (Source) kollidiert.

## 12. Kennzahlen (Stand Commit)

- Kompakt: 3627 Wörter Hauptpfad (Spanne 1800–4000), Lesezeit ≈ 21 min; 5 Herleitungen (H1, H2, H4, H5, H6, wortgleich
  mit der ausführlichen Fassung), 4 Beispiele, 6 Abbildungen, 4 Frage-Kästen, 2 Fehlvorstellungen, 1 Merke, 6 Quizfragen,
  6 Formelkästen.
- Ausführlich: 5735 Wörter Hauptpfad (Spanne 3500–7000), Lesezeit ≈ 34 min; 8 Herleitungen, 9 Beispiele,
  10 Abbildungen, 5 Frage-Kästen, 4 Fehlvorstellungen, 1 Analogie, 1 Merke, 1 Vertiefung, 10 Quizfragen,
  9 Formelkästen.
- Keine Gedankenstriche, kein „nicht … sondern“, Verbotsliste leer, audit_inline 0, quellen_check leer.
