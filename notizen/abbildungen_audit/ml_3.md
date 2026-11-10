# Abbildungen und Animationen — Paket ml_3 (Heft ml/03-ableitung-gradient-und-kettenregel)

Stand: 09.11.2026. Nur Vorschlagsplan, nichts an Artikeln/Szenen geändert.
Deutsche Artikel 01–13. 20 Szenen `ml/k3…` vorhanden: 10 Rechenbilder `k3r…` (alle nur ein statisches `MathTex`, keine Editor-Operation) und 10 Konzeptbilder (Achsen, Kurven, Pfeile, Kästen; keine hat eine Zeitachse). Vorschläge: V1–V25, davon 23 neue Abbildungen und 2 Umbauten (V8, V12) vorhandener Rechenbilder. Die Umbauten zählen in der Tabelle nicht als „neu“.

## Kurzbilanz je Artikel

| Artikel | Soll | vorh. | neu A | neu B | neu C | entfällt | nachher |
|---|---:|---:|---:|---:|---:|---:|---:|
| 01-ableitung-gradient-und-kettenregel | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| 02-die-ableitung | 5 | 3 | 2 | 0 | 0 | 0 | 5 |
| 03-die-kettenregel | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| 04-partielle-ableitungen-und-der-gradient | 4 | 2 | 2 | 0 | 0 | 0 | 4 |
| 05-richtungsableitung-und-steilster-anstieg | 4 | 2 | 1 | 1 | 0 | 0 | 4 |
| 06-die-jacobi-matrix | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| 07-die-kettenregel-fur-mehrere-variablen | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| 08-ableiten-nach-vektoren-und-matrizen | 4 | 2 | 1 | 1 | 0 | 0 | 4 |
| 09-die-hesse-matrix-und-die-quadratische-naherung | 4 | 2 | 2 | 0 | 0 | 0 | 4 |
| 10-rechengraphen | 3 | 2 | 1 | 0 | 0 | 0 | 3 |
| 11-automatische-differentiation | 5 | 1 | 2 | 2 | 0 | 0 | 5 |
| 12-numerische-ableitung-und-gradientenprufung | 4 | 1 | 2 | 1 | 0 | 0 | 4 |
| 13-das-wichtigste-bis-hier | 1 | 0 | 1 | 0 | 0 | 0 | 1 |
| **Summe** | 43 | 20 | 18 | 5 | 0 | 0 | 43 |

Das Soll ist in jedem Artikel genau eingehalten (keine +1-Überschreitung). Zusätzlich wird in den Artikeln 05, 07, 08, 09 und 10 je ein vorhandenes statisches Rechenbild durch die Editor-Operation (Skalarprodukt/Summation) ersetzt; das ändert die Zahl der Abbildungen nicht. Verworfen (Platz im Soll): Artikel 02 zweite Ableitung/Krümmung als Tangenten-Parabel-Bild und Ableitungsfunktion mit mitlaufender Tangente; Artikel 04 Gegenbeispiel $x_1x_2/(x_1^2+x_2^2)$ als Fläche; Artikel 06 Aufbau der Jacobi-Matrix als Zeilen/Spalten-Tabelle; Artikel 08 Layout-Konvention als Formen-Bild; Artikel 10 das Paar (Wert, Ableitung) der schrittweisen Produktregel; Artikel 12 der Knick bei $|x|$ mit $h=10^{-5}$.

## Top 3

- V6 [A] 04-partielle-ableitungen-und-der-gradient — Tangentialebene schmiegt sich an die Fläche (Schnittkurven, Ebene, Zoom) — der Begriff „Ebene als lineare Näherung“ trägt Gradient, Jacobi-Matrix und Kettenregel des ganzen Hefts und hat bisher kein Bild
- V18 [A] 11-automatische-differentiation — Vorwärtsmodus: der Tangentenwert läuft mit der Rechnung mit (mit Rechenbild) — Voraussetzung, um den Gewinn des Rückwärtsmodus zu sehen; das einzige Verfahren des Hefts ohne jedes Bild
- V7 [A] 05-richtungsableitung-und-steilster-anstieg — der Richtungspfeil dreht sich, die Steigung läuft als Kosinuskurve mit — macht den Cauchy-Schwarz-Beweis anschaulich und liefert die Zahlen 4, 6,4, 6,403, 0, −6,403 der Rechenbeispiele

Außerdem auffällig: Von 20 vorhandenen Szenen sind 10 „Rechenbilder“ (alle nur ein MathTex); Pflicht-Rechenbilder fehlen als Editor-Operation bei Taylor (k3rtaylor1, k3rtaylor2), Gradient (k3rlinear), Richtungsableitung (k3rrichtung), Jacobi (k3rjacobi), Wegesumme (k3rwege), Residuum und Rückwärtsregel (k3rresiduum, k3rrueck), Krümmung (k3rkruemmung), Produktregel am Rechengraphen (k3rvierfaktoren). Drei der neuen Szenen (V7, V16, V11) bauen auf demselben Bewegungsprinzip „Pfeil dreht sich/Punkt läuft auf Kurve“ auf und können eine gemeinsame Vorlage nutzen.

## Editor-Lücken

Für die 23 neuen Vorschläge (17 sind ohne neue Editor-Funktion machbar):
- L4: 3 (V5 hilfreich, V6 und V9 Zoom bzw. Kamera; Notbehelf jeweils fest eingestellte Ausschnitte)
- L1: 1 (V15; Notbehelf zwei getrennte Rechtecke)
- L9: 1 (V13; Notbehelf übergelegte Rechtecke)
- L7: 1 (V21; Matrix·Matrix als Prozess)
- L-neu: 1 (V5: Höhenlinie als Kurve auf einer 3D-Fläche markieren)
- L3 (Parameter/Zeit): bei keinem Vorschlag nötig, bei sechs hilfreich (V2, V10, V11, V22 und V7, V16 für einen stetigen Wert beim Drehen)

Für die vorhandenen Szenen: L4 bei k3lupe (Zoom); L3 bei k3sekante, k3logistisch (mitlaufende Tangente), k3vkurve (laufendes $h$); L7 bei k3rjacobi, falls Matrix·Vektor als eine Operation. L10 (Abspielknopf im Artikel) betrifft alle.


## Vorschläge

### Artikel 01 — Überblick (Soll 1, vorh. 0)

### V1 [A] Eingänge wackeln, der Ausgang antwortet verschieden stark (Zusammenschau)
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/01-ableitung-gradient-und-kettenregel.md
- **Stelle:** Worum es geht — „Eine Zahl hängt oft von vielen anderen Zahlen ab. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Blockbild von links nach rechts: drei Eingangskästen (TextBox) „Eingang 1“, „Eingang 2“, „Eingang 3“ mit Zahlen 2; 5; 1, ein Kasten „Rechnung“ in der Mitte, ein Ausgangskasten „Zahl y“ rechts. Von jedem Eingang ein Pfeil (LabeledArrow) zum Rechenkasten; die Pfeildicke und die Beschriftung zeigen die Empfindlichkeit, hier als frei gewähltes Beispiel 3; 0,5; −2 (blauer Pfeil für „y steigt“, roter für „y fällt“). Rechts unten ein kleines Achsenkreuz mit drei Komponenten-Balken (Stem), später als ein Pfeil.
- **Ablauf:** 1. Kästen und Pfeile erscheinen von links nach rechts (FadeIn, nacheinander). 2. Eingang 1 wird um 0,1 größer (Shift der Zahl, Indicate), der Ausgang springt um 0,3 (Scale der Zahl y), der Pfeil wird dick, Beschriftung „stark“. 3. Dasselbe für Eingang 2: Ausgang bewegt sich kaum (0,05), dünner Pfeil, „schwach“. 4. Eingang 3 wächst, der Ausgang fällt (−0,2), roter Pfeil, „gegenläufig“. 5. Die drei Empfindlichkeiten (3; 0,5; −2) wandern als Balken zu einem einzigen Pfeil zusammen: „In welche Richtung muss man alle Eingänge zugleich schieben, damit y am schnellsten wächst?“ — Haltepunkte: Schritt 2 und 5.
- **Verständnisproblem:** Der Leser sieht, dass „Empfindlichkeit“ je Eingang eine eigene Zahl ist, mit Vorzeichen, und dass das Kapitel diese Zahlen sammelt und nutzt; der Text führt drei Seiten lang auf einen Begriff hin, den man vorab sehen sollte.
- **Szenenname:** ml/k3ueberblick
- **Editor-Lücke:** machbar (Schritt 5 als Balken, die per Shift zu einem Pfeil werden; ein Zahlenwert, der mitrechnet, braucht L3, die Zahlen werden fest geschrieben)

### Artikel 02 — Die Ableitung (Soll 5, vorh. 3)

### V2 [A] Am Knick: Sekanten von beiden Seiten
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/02-die-ableitung.md
- **Stelle:** Die Ableitung — „Nicht jede Funktion ist überall differenzierbar. Eine typische Ausnahme ist ein Knick: …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes x in [−2; 2], y in [−0,5; 2,5]; FunctionGraph $|x|$ (blau); Punkt $(0,\,0)$ (Dot); rechts ein beweglicher Punkt $(h,\,h)$ auf dem Graphen mit Sekante (rot), links ein Punkt $(-h,\,h)$ mit Sekante (orange). Textfelder „$|h|/h = 1$“ und „$|h|/h = -1$“, am Ende „keine gemeinsame Steigung — keine Ableitung“.
- **Ablauf:** 1. Der Graph zeichnet sich (Create), der Punkt $(0,0)$ erscheint. 2. Rechter Punkt bei $h=1$, Sekante durch $(0,0)$ und $(1,1)$, Beschriftung „Steigung 1“. 3. Der rechte Punkt wandert in drei Stufen auf $h=0{,}5$ und $h=0{,}1$ (MoveTo): die Sekante bleibt dieselbe Gerade $y=x$, die Steigung bleibt 1. 4. Linker Punkt bei $h=-1$, Sekante durch $(0,0)$ und $(-1,1)$, Steigung $-1$, wandert ebenso auf $-0{,}5$ und $-0{,}1$. 5. Beide Sekanten stehen zugleich im Bild, dazwischen ein Doppelpfeil mit Kreuz (Mark): „zwei Grenzwerte, $+1$ und $-1$“. — Haltepunkte: Schritt 3 (der Grenzprozess bewegt sich, die Steigung nicht) und 5.
- **Verständnisproblem:** Warum „der Grenzwert existiert nicht“, wenn die Sekantensteigungen doch jeweils zur Ruhe kommen: Sie kommen von rechts und links zu verschiedenen Zahlen.
- **Szenenname:** ml/k3knick
- **Editor-Lücke:** machbar (Punkt wandert als MoveTo, Sekante liegt fest; ein stetig mitwandernder Punkt mit Sekante wäre L3)

### V3 [A] Produktregel als wachsendes Rechteck
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/02-die-ableitung.md
- **Stelle:** Ableitungsregeln — „Die Produktregel ist weniger offensichtlich. Ein Bild macht sie klar: Man denke sich $u\,v$ als Fläche eines Rechtecks …“ (der Text beschreibt das Bild, es gibt keins)
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Rechteck (Rectangle) mit den Seiten $u=3$ (waagrecht) und $v=2$ (senkrecht), Fläche $uv=6$ (blau, Beschriftung „$u\,v$“). Daran angebaut: ein Streifen rechts der Breite $\Delta u=0{,}5$ und Höhe $v$ (Fläche $v\,\Delta u=1$, orange), ein Streifen oben der Höhe $\Delta v=0{,}4$ und Breite $u$ (Fläche $u\,\Delta v=1{,}2$, grün) und das Eckstück $\Delta u\,\Delta v=0{,}2$ (rot). Rechts daneben dieselbe Konstruktion mit $\Delta u=\Delta v=0{,}1$ (Streifen $0{,}2$ und $0{,}3$, Eckstück $0{,}01$) im gleichen Maßstab. Die Maße erscheinen als Measure-Beschriftungen.
- **Ablauf:** 1. Das blaue Rechteck wächst aus der Ecke (GrowFromCenter oder Create), Seiten $u$ und $v$ werden bemaßt. 2. Der rechte Streifen erscheint (FadeIn), „$v\,\Delta u$“. 3. Der obere Streifen erscheint, „$u\,\Delta v$“. 4. Das Eckstück erscheint (rot, Indicate), „$\Delta u\,\Delta v$“. Darunter die Gleichung $\Delta(uv)=v\,\Delta u+u\,\Delta v+\Delta u\,\Delta v$ (Write, Summand für Summand passend gefärbt). 5. Die Variante mit den zehnmal kleineren Änderungen erscheint daneben: Das Eckstück ($0{,}01$) ist winzig neben den Streifen ($0{,}2$ und $0{,}3$), Beschriftung „verschwindet schneller“. — Haltepunkte: Schritt 4 und 5.
- **Verständnisproblem:** Warum in der Produktregel zwei Summanden stehen (jede Seite einmal ändern, die andere festhalten) und warum der gemischte Summand wegfällt.
- **Szenenname:** ml/k3produkt
- **Editor-Lücke:** machbar

### Artikel 03 — Die Kettenregel (Soll 3, vorh. 2)

### V4 [A] Eine Kette aus drei Gliedern: erst Werte, dann Faktoren, dann Produkt
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/03-die-kettenregel.md
- **Stelle:** Ketten aus vielen Gliedern — „Es sei $y=\dfrac1{(x^2+1)^3}$ an der Stelle $x=1$. Die Kette hat drei Glieder: …“ (Rechenbeispiel im Haupttext)
- **Art:** neue Animation (mit Rechenbild ∏)
- **Was zu sehen ist:** Obere Reihe (TextBox): $x=1$ → Kasten „$x^2+1$“ → $u_1=2$ → Kasten „$u_1^3$“ → $u_2=8$ → Kasten „$1/u_2$“ → $y=\tfrac18$, verbunden mit Pfeilen (LabeledArrow). Darunter, an jedem Kasten, die lokale Ableitung: $2x=2$; $3u_1^2=12$; $-1/u_2^2=-\tfrac1{64}$. Unten das Rechenbild als Editor-Operation Produkt (∏): $2\cdot12\cdot(-\tfrac1{64})=-\tfrac{24}{64}=-0{,}375$.
- **Ablauf:** 1. Die drei Kästen erscheinen von links nach rechts (FadeIn). 2. Ein Marker (Dot) läuft die Kette entlang (MoveAlongPath) und lässt die Werte 1, 2, 8, $\tfrac18$ stehen — „Vorwärts: Zwischenwerte“. 3. Unter den Kästen erscheinen nacheinander die drei Faktoren $2$; $12$; $-\tfrac1{64}$, jeder an dem Wert berechnet, an dem sein Kasten gearbeitet hat (Write), Hervorhebung des Werts darüber (Indicate). 4. Die drei Faktoren wandern in das Produkt-Rechenbild: Faktor für Faktor wird multipliziert, Zwischenergebnis $24$, dann $-\tfrac{24}{64}=-0{,}375$. 5. Daneben die Probe $-6/16$ als eine Zeile. — Haltepunkte: Schritt 2 (Reihenfolge: erst alle Werte) und 4.
- **Verständnisproblem:** Warum man zuerst vorwärts rechnet und warum jeder Faktor an seiner eigenen Stelle ($u_1$, $u_2$) und nicht überall an $x$ ausgewertet wird; dazu die Pflicht-Darstellung des Produkts mit Zahlen.
- **Szenenname:** ml/k3kette3
- **Editor-Lücke:** machbar (Operation Produkt vorhanden; die Kette lässt sich später in Artikel 10 und 11 als Rechengraph wiederverwenden)

### Artikel 04 — Partielle Ableitungen und der Gradient (Soll 4, vorh. 2)

### V5 [A] Funktion zweier Variablen als Gelände mit Höhenlinien
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/04-partielle-ableitungen-und-der-gradient.md
- **Stelle:** Funktionen mehrerer Variablen — „Für zwei Variablen hilft das Bild einer Landschaft. Der Vektor $\mathbf{x}=(x_1,\,x_2)^{\top}$ ist ein Ort auf einer Landkarte, …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links eine 3D-Ansicht der Fläche $z=f(x_1,x_2)=x_1^2x_2+x_2^2$ über $x_1\in[-2;2]$, $x_2\in[0;3]$ (FunctionGraph als Fläche), rechts die Landkarte (Axes $x_1\in[-2;2]$, $x_2\in[0;3]$) mit den Höhenlinien $f=2;4;6;8;10$ (die Werte aus Abb. 6). Der Punkt $(1,\,2)$ und seine Höhe $f=6$.
- **Ablauf:** 1. Landkarte mit dem Punkt $(1,2)$ (Dot, „Ort“). 2. Die Fläche erscheint links (Create), der Punkt hebt sich auf die Fläche, Höhe $6$ (Shift, senkrechte Hilfslinie, Beschriftung „Höhe $f=6$“). 3. Die Höhenlinie $f=6$ auf der Karte wird gezeichnet (Create) und zugleich auf der Fläche als Schnitt mit der Ebene $z=6$ (waagrechte Ebene fährt von unten herauf, Shift). 4. Die übrigen Höhenlinien folgen nacheinander ($2$, $4$, $8$, $10$), Beschriftung „dicht = steil, weit = flach“. — Haltepunkte: Schritt 3 und 4.
- **Verständnisproblem:** Der Leser hat nur den Text für „Funktion von $d$ Variablen“, „Graph als Gelände“ und „Höhenlinie als Ort gleicher Höhe“; das Bild verbindet Fläche und Karte, die später in Abb. 6, 9 immer als Karte erscheinen.
- **Szenenname:** ml/k3gelaende
- **Editor-Lücke:** braucht Editor-Funktion: L4 (3D drehen, hilfreich, nicht nötig) und L-neu: Höhenlinie als Kurve auf der 3D-Fläche; Notbehelf: waagrechte Ebene als zweite FunctionGraph-Fläche, ohne markierte Schnittlinie

### V6 [A] Die Tangentialebene schmiegt sich an die Fläche
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/04-partielle-ableitungen-und-der-gradient.md
- **Stelle:** Die lineare Näherung im Raum — „Bei zwei Variablen tritt an ihre Stelle eine Ebene. Unter der Lupe sieht ein glattes Gelände in der Nähe eines Punkts wie eine schräg gestellte Platte aus: …“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Fläche $z=x_1^2x_2+x_2^2$ in der Umgebung von $(1,\,2)$ ($x_1\in[0;2]$, $x_2\in[1;3]$), der Punkt $P=(1,\,2,\,6)$, die beiden Tangenten der Schnittkurven mit den Steigungen $4$ (in $x_1$-Richtung) und $5$ (in $x_2$-Richtung) als Pfeile, die Ebene $z=6+4(x_1-1)+5(x_2-2)$ als zweite Fläche (halbtransparent, orange).
- **Ablauf:** 1. Fläche und Punkt $P$. 2. Schnittkurve $x_2=2$ mit Tangente der Steigung $4$ (Create, Beschriftung „$\partial_1 f=4$“). 3. Schnittkurve $x_1=1$ mit Tangente der Steigung $5$ („$\partial_2 f=5$“). 4. Die Ebene durch beide Tangenten erscheint (FadeIn). 5. Der Ausschnitt wird verkleinert auf $\pm0{,}1$ (Zoom): Fläche und Ebene fallen zusammen; Beschriftung „$f(1{,}01;\,2{,}02)=6{,}1410$, Ebene $6{,}14$“. — Haltepunkte: Schritt 4 und 5.
- **Verständnisproblem:** Der Begriff Tangentialebene und der Satz „die Neigungen der Platte sind die partiellen Ableitungen“ haben im Text nur die Lupe als Anschauung; Abb. 6 zeigt nur die Karte, nicht die Platte.
- **Szenenname:** ml/k3ebene
- **Editor-Lücke:** braucht Editor-Funktion: L4 (Kamera-Zoom über die Zeit); Notbehelf: zwei feste Ausschnitte nacheinander per FadeIn

### Artikel 05 — Richtungsableitung und steilster Anstieg (Soll 4, vorh. 2)

### V7 [A] Der Richtungspfeil dreht sich: Steigung als Kosinuskurve
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/05-richtungsableitung-und-steilster-anstieg.md
- **Stelle:** Die Richtung des steilsten Anstiegs — „In welche Richtung muss man gehen, damit es am steilsten bergauf geht? …“ (und davor die Richtungsableitung als Steigung der Schnittkurve)
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Karte $x_1\in[-1;4]$, $x_2\in[0;5]$ mit dem Punkt $(1,\,2)$, dem Gradienten $\nabla f=(4,\,5)^{\top}$ als Pfeil (verkürzt auf ein Viertel gezeichnet) und einem Einheitspfeil $\mathbf{u}$ der Länge 1 am Punkt (gestrichelter Einheitskreis). Rechts Axes mit dem Winkel $\theta$ des Pfeils von $0^\circ$ bis $360^\circ$ waagrecht und der Steigung $D_{\mathbf{u}}f$ von $-7$ bis $7$ senkrecht; die Kurve $D_{\mathbf{u}}f(\theta)=\sqrt{41}\cos(\theta-51{,}3^\circ)$ (Gradientenwinkel $\arctan(5/4)\approx51{,}3^\circ$, Amplitude $\sqrt{41}\approx6{,}403$) mit einem Punkt, der mit $\mathbf{u}$ mitläuft.
- **Ablauf:** 1. Karte, Punkt, Gradient (Create, GrowFromCenter). 2. $\mathbf{u}=\mathbf{e}_1$, $\theta=0$: Punkt auf der Kurve bei $4$ (Beschriftung „$D=4$, die partielle Ableitung“). 3. $\mathbf{u}$ dreht sich (Rotate um den Punkt) und der Punkt läuft die Kurve entlang (MoveAlongPath, gleiche Dauer); Halt bei $\mathbf{u}=(0{,}6;\ 0{,}8)$, $\theta=53{,}1^\circ$: $6{,}4$. 4. Weiter bis $\mathbf{u}=\nabla f/\lVert\nabla f\rVert$, $\theta=51{,}3^\circ$: Höchstwert $\sqrt{41}=6{,}403$, Beschriftung „$\mathbf{u}$ liegt auf dem Gradienten“. 5. Weiter bis $\mathbf{u}\perp\nabla f$ bei $\theta=141{,}3^\circ$: Wert $0$, Beschriftung „entlang der Höhenlinie“. 6. Weiter bis $\mathbf{u}=-\nabla f/\lVert\nabla f\rVert$, $\theta=231{,}3^\circ$: Tiefstwert $-6{,}403$. — Haltepunkte: Schritt 3 (Zahl 6,4 des Rechenbeispiels), 4 und 5.
- **Verständnisproblem:** Der Beweis über Cauchy-Schwarz bleibt abstrakt; die Bewegung zeigt, dass die Steigung in jeder Richtung der Schatten des Gradienten ist und bei $\varphi=0$ maximal, bei $90^\circ$ null, bei $180^\circ$ am kleinsten wird.
- **Szenenname:** ml/k3drehen
- **Editor-Lücke:** machbar (Rotate des Pfeils um den Punkt plus MoveAlongPath des Punkts auf der Kurve mit gleicher Dauer; ein stetiger Zahlenwert beim Drehen wäre L3, die Zahlen stehen an den Haltepunkten fest)

### V8 [A] Die Richtungsableitung als echtes Skalarprodukt (ersetzt k3rrichtung)
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/05-richtungsableitung-und-steilster-anstieg.md
- **Stelle:** Die Richtungsableitung — „Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ mit $\nabla f=(4,\,5)^{\top}$ und der Richtung $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ …“
- **Art:** bestehende Abbildung als Animation
- **Was zu sehen ist:** Die Editor-Operation Skalarprodukt mit $(4,\,5)\cdot(0{,}6;\ 0{,}8)$, dazu die Länge von $\mathbf{u}$ als Probe ($0{,}36+0{,}64=1$) und die Ergebnisse für $-\mathbf{u}$ ($-6{,}4$) und $(0{,}8;\ -0{,}6)$ ($0{,}2$).
- **Ablauf:** 1. Beide Vektoren als Pfeile oder Zahlenspalten. 2. Die Produkte $4\cdot0{,}6=2{,}4$ und $5\cdot0{,}8=4{,}0$ entstehen einzeln. 3. Summe $6{,}4$. 4. Die beiden Vergleichsrichtungen mit demselben Schema (verkürzt). — Haltepunkte: Schritt 2.
- **Verständnisproblem:** Das Rechenbild ist heute ein statisches MathTex, obwohl die Rechnung Kern des Rechenbeispiels ist (Pflicht Skalarprodukt).
- **Szenenname:** ml/k3rrichtung (bestehende Szene umbauen)
- **Editor-Lücke:** machbar

### V9 [B] Die Höhenlinie unter der Lupe wird zur Geraden senkrecht zum Gradienten
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/05-richtungsableitung-und-steilster-anstieg.md
- **Stelle:** Der Gradient steht senkrecht auf den Höhenlinien — „Dass die Gerade die Höhenlinie berührt, folgt aus der Lupe: …“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Ellipse $x_1^2+4x_2^2=5$ (Höhenlinie der Schüssel, ParametricCurve), der Punkt $(1,\,1)$, der Gradient $(2,\,8)$ (verkürzt auf ein Viertel) senkrecht zur Tangente mit Richtung $(4,\,-1)$ (Gerade, rot) und die Ellipse in drei Ausschnitten der Breite $4$, $0{,}4$, $0{,}04$.
- **Ablauf:** 1. Ellipse (Create), Punkt, Gradient (GrowFromCenter). 2. Die Gerade durch $(1,\,1)$ in Richtung $(4,\,-1)$ erscheint, die Rechnung $f(1+4s,\,1-s)=5+20s^2$ als Beschriftung. 3. Zweiter und dritter Ausschnitt (je zehnmal enger): Ellipse und Gerade fallen zusammen. 4. Rechter-Winkel-Markierung zwischen Gradient und Gerade. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Warum „senkrecht“ nicht nur für diesen Punkt gilt, sondern eine Folge der Lupe ist: im Kleinen ist die Höhenlinie eine Gerade.
- **Szenenname:** ml/k3hoehelupe
- **Editor-Lücke:** braucht Editor-Funktion: L4 (Zoom); Notbehelf: drei feste Ausschnitte, nacheinander eingeblendet. Teilweise deckt k3lupe (Heft 3, Artikel 02) die Idee für eine Variable; keine Doppelung, da hier die Höhenlinie die Kurve ist.

### Artikel 06 — Die Jacobi-Matrix (Soll 2, vorh. 1)

### V10 [A] Die Jacobi-Matrix als lokale Lupe: Quadrat wird fast zum Parallelogramm
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/06-die-jacobi-matrix.md
- **Stelle:** Die lineare Näherung mit der Jacobi-Matrix — „In der Nähe von $\mathbf{x}$ wirkt $\mathbf{g}$ also wie die lineare Abbildung $\mathbf{h}\mapsto\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ …“ („Unter der Lupe verformt $\mathbf{g}$ ein kleines Gitter …“, ohne Bild)
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Eingabeebene ($x_1\in[0;2]$, $x_2\in[1;3]$) mit dem Quadrat der Seite $0{,}2$ um $(1,\,2)$. Rechts die Bildebene ($y_1\in[1;3]$, $y_2\in[4;8]$) mit $\mathbf{g}(1,2)=(2,\,6)$ und dem Bild der Quadratkanten unter $\mathbf{g}(\mathbf{x})=(x_1x_2,\ 2x_1+x_2^2)^{\top}$ (vier leicht gebogene Kurven mit den Ecken $(1{,}71;\ 5{,}41)$, $(2{,}09;\ 5{,}81)$, $(2{,}31;\ 6{,}61)$, $(1{,}89;\ 6{,}21)$). Darüber, gestrichelt, das Parallelogramm der Matrix $\mathbf{J}=\begin{pmatrix}2&1\\2&4\end{pmatrix}$ mit den Ecken $(1{,}7;\ 5{,}4)$, $(2{,}1;\ 5{,}8)$, $(2{,}3;\ 6{,}6)$, $(1{,}9;\ 6{,}2)$. Die Spalten von $\mathbf{J}$ als Pfeile $0{,}2\cdot(2,\,2)=(0{,}4;\ 0{,}4)$ und $0{,}2\cdot(1,\,4)=(0{,}2;\ 0{,}8)$.
- **Ablauf:** 1. Das Quadrat erscheint (Create), sein Mittelpunkt wird markiert. 2. Die Bildkurven entstehen, die Ecken laufen von den Quadratecken zu den Bildecken (MoveAlongPath). 3. Die zwei Spaltenpfeile wachsen am Bildpunkt $(2,\,6)$ (GrowFromCenter), dazu die Parallelogrammkanten gestrichelt (Create): Die Bildkurven schmiegen sich an. 4. Die Seite wird halbiert ($0{,}1$), dann nochmals ($0{,}05$): Der Abstand zwischen Bild und Parallelogramm schrumpft schneller als das Quadrat. 5. Beschriftung: Fläche $0{,}04\to0{,}24=6\cdot0{,}04$ (Determinante $6$). — Haltepunkte: Schritt 3 und 4.
- **Verständnisproblem:** „Jacobi-Matrix ist die Matrix der linearen Näherung“ bleibt ein Satz; hier sieht man, dass die Spalten die Bilder der Achsenschritte sind und dass die Näherung erst im Kleinen gut wird.
- **Szenenname:** ml/k3jacobilupe
- **Editor-Lücke:** machbar (Bildkurven als ParametricCurve, Parallelogramm als Polygon, drei Größen als drei Objekte); fließendes Schrumpfen wäre L3. Vorlage in Konstruktion: hm3/k1jacobi (andere Funktion, eigenständig).

### Artikel 07 — Die Kettenregel für mehrere Variablen (Soll 3, vorh. 2)

### V11 [A] Spaziergang über die Landkarte: wie schnell ändert sich die Höhe?
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/07-die-kettenregel-fur-mehrere-variablen.md
- **Stelle:** Ableitung entlang einer Kurve — „Ein Spaziergang über die Landkarte ist eine Kurve: Zu jeder Zeit $t$ ist man an einem Ort $\boldsymbol{\gamma}(t)\in\mathbb{R}^d$. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Karte ($x_1\in[-1;4]$, $x_2\in[0;6]$) mit den Höhenlinien $f=2;4;6;8;10$ von $f=x_1^2x_2+x_2^2$ und der Geraden $\boldsymbol{\gamma}(t)=(1+t,\ 2+2t)^{\top}$; ein Punkt auf ihr, der Geschwindigkeitsvektor $\boldsymbol{\gamma}'=(1,\,2)^{\top}$ als Pfeil am Punkt, bei $t=0$ zusätzlich der Gradient $(4,\,5)^{\top}$ (verkürzt gezeichnet). Rechts Axes $t\in[-0{,}5;\ 1]$, $f(\boldsymbol{\gamma}(t))=2(1+t)^3+4(1+t)^2\in[0;\ 35]$ (Werte $1{,}25$ bei $t=-0{,}5$, $6$ bei $t=0$, $32$ bei $t=1$) mit der Tangente der Steigung $14$ bei $t=0$.
- **Ablauf:** 1. Karte, Höhenlinien, Gerade (Create). 2. Der Punkt läuft von $t=-0{,}5$ nach $t=0$ (MoveAlongPath), rechts wächst die Kurve mit (Create, gleiche Dauer). 3. Halt bei $t=0$: Pfeile $\boldsymbol{\gamma}'$ und $\nabla f$, rechts die Tangente mit Steigung $14$; Beschriftung „$4\cdot1+5\cdot2=14$“. 4. Der Punkt läuft weiter bis $t=1$. 5. Zweiter Durchlauf auf der Höhenlinie $f=6$ (Tangentenrichtung $(5,\,-4)^{\top}$): rechts bleibt die Kurve waagrecht bei $6$, Beschriftung „$4\cdot5+5\cdot(-4)=0$: Gradient senkrecht“. — Haltepunkte: Schritt 3 und 5.
- **Verständnisproblem:** Was ein Geschwindigkeitsvektor ist und warum die Änderungsrate der Höhe das Skalarprodukt aus Gradient und Geschwindigkeit ist; zugleich, warum der Gradient senkrecht auf der Höhenlinie steht (Rate null).
- **Szenenname:** ml/k3spaziergang
- **Editor-Lücke:** machbar (Punkt per MoveAlongPath, Tangente bei $t=0$ fest); eine mitlaufende Tangente wäre L3. Die Szene teilt die Funktion mit ml/k3schnitt und ml/k3rrichtung.

### V12 [A] Wegesumme als zwei Skalarprodukte (umbauen von k3rwege)
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/07-die-kettenregel-fur-mehrere-variablen.md
- **Stelle:** Summe über alle Wege — Rechenbeispiel 1 „Für $F=f\circ\mathbf{g}$ aus dem vorigen Unterabschnitt sind die Kantenfaktoren an der Stelle $(1,\,2)$ …“ (und Rechenbeispiel 6.1 mit demselben Zahlenmaterial)
- **Art:** bestehende Abbildung als Animation
- **Was zu sehen ist:** Die Operation Skalarprodukt, zweimal: $(4,\,3)\cdot(2,\,2)=4\cdot2+3\cdot2=14$ (erste Spalte von $\mathbf{J}_{\mathbf g}$, also Eingang $x_1$) und $(4,\,3)\cdot(1,\,4)=4\cdot1+3\cdot4=16$ (zweite Spalte, Eingang $x_2$); die Summanden sind den Wegen über $u_1$ (blau) und $u_2$ (orange) farblich zugeordnet wie in der Wegeabbildung.
- **Ablauf:** 1. Die Zeile $(4\ \ 3)$ und die erste Spalte $(2,\,2)^{\top}$ erscheinen. 2. Die beiden Produkte $4\cdot2$ (Weg über $u_1$) und $3\cdot2$ (Weg über $u_2$) entstehen einzeln. 3. Summe $14$. 4. Dasselbe für die zweite Spalte: $4$ und $12$, Summe $16$, daneben das Ergebnis $\mathbf{J}_F=(14\ \ 16)$. — Haltepunkte: Schritt 2.
- **Verständnisproblem:** Heute ist k3rwege nur ein statisches MathTex; die Pflicht „Rechenbild für Skalarprodukt/Σ mit Zahlen“ ist für die Hauptrechnung des Artikels nicht mit der Editor-Operation erfüllt.
- **Szenenname:** ml/k3rwege (bestehende Szene umbauen)
- **Editor-Lücke:** machbar

### Artikel 08 — Ableiten nach Vektoren und Matrizen (Soll 4, vorh. 2)

### V13 [A] Wie reagiert die Zahl auf einen Matrixeintrag? (Gradient nach A als äußeres Produkt)
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/08-ableiten-nach-vektoren-und-matrizen.md
- **Stelle:** Rückwärts durch ein Matrixprodukt — „Oft ist ein Matrix-Vektor-Produkt $\mathbf{y}=\mathbf{A}\mathbf{x}$ nur ein Zwischenschritt einer längeren Rechnung …“ (auch Ableiten nach einer Matrix, davor)
- **Art:** neue Animation
- **Was zu sehen ist:** Als Table die $3\times2$-Matrix $\mathbf{A}=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}$, daneben die Spalte $\mathbf{x}=(2,\,1)^{\top}$, dann die Spalte $\mathbf{y}=\mathbf{A}\mathbf{x}=(4,\,-1,\,7)^{\top}$ und der Kasten $f(\mathbf{y})=y_1-y_3=-3$ mit $\nabla f=(1,\,0,\,-1)^{\top}$. Rechts eine zweite Table, die gesuchte Matrix $\nabla_{\mathbf{A}}F$ mit leeren Zellen, Form $3\times2$.
- **Ablauf:** 1. Matrix, Spalte $\mathbf{x}$, Spalte $\mathbf{y}$ und $f$ erscheinen (FadeIn, nacheinander). 2. Eintrag $a_{11}$ wird um $0{,}1$ größer (Indicate): nur $y_1$ ändert sich (um $0{,}1\cdot x_1=0{,}2$), über $f$ kommt $+0{,}2$ an; die Zelle $(1,1)$ der Ergebnismatrix wird mit $2$ gefüllt ($\partial f/\partial y_1\cdot x_1=1\cdot2$). 3. Ebenso $a_{12}$: $1\cdot1=1$. 4. Zeile 2: $a_{21}$ wirkt nur auf $y_2$, und $f$ hängt nicht von $y_2$ ab: Ergebnis $0$, $0$. 5. Zeile 3: $-2$ und $-1$. Die fertige Matrix wird als Produkt der Spalte $(1,\,0,\,-1)^{\top}$ mit der Zeile $(2\ \ 1)$ gedeutet (äußeres Produkt). 6. Gegenstück: Eingang $x_1$ wirkt auf alle drei $y_i$, die Beiträge $1\cdot1+0\cdot0+(-1)\cdot3=-2$ summieren sich (drei Wege). — Haltepunkte: Schritt 2 und 6.
- **Verständnisproblem:** Warum der Gradient nach den Gewichten ein äußeres Produkt aus „Reaktion des Ausgangs“ und „Eingabe“ ist, und warum der Gradient nach $\mathbf{x}$ dagegen eine Summe ist (ein Weg gegen mehrere Wege). Das ist das Muster der Rückwärtsrechnung in Abschnitt 10.
- **Szenenname:** ml/k3matrixgrad
- **Editor-Lücke:** braucht Editor-Funktion: L9 (Table-Zellen nacheinander hervorheben); Notbehelf: Rechtecke über den Zellen

### V14 [B] Gleiche Form, anderer Gradient? (A und ihr symmetrischer Anteil)
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/08-ableiten-nach-vektoren-und-matrizen.md
- **Stelle:** Quadratische Formen — „Nach Grundlagen 2, Abschnitt 5.2, hängt die quadratische Form nur vom symmetrischen Anteil $\mathbf{S}=\tfrac12(\mathbf{A}+\mathbf{A}^{\top})$ ab. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Karte ($x_1,x_2\in[-2;2]$) mit den Höhenlinien (Ellipsen) von $x^{\top}\mathbf{A}\mathbf{x}=x_1^2+2x_1x_2+3x_2^2$ für $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)$ und daneben mit $\mathbf{S}=\bigl(\begin{smallmatrix}1&1\\1&3\end{smallmatrix}\bigr)$: dieselben Linien. Am Punkt $(1,\,1)$ der Gradient $(4,\,8)^{\top}=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=2\mathbf{S}\mathbf{x}$ (verkürzt gezeichnet), senkrecht auf der Höhenlinie $f=6$. Der falsche Pfeil $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$ rot durchgestrichen.
- **Ablauf:** 1. Links $\mathbf{A}$ mit Höhenlinien, am Punkt $(1,\,1)$ der Gradient. 2. Rechts $\mathbf{S}$ erscheint: dieselbe Form, derselbe Gradient. 3. Der Pfeil $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$ erscheint (FadeIn) und steht schräg auf der Höhenlinie, Kreuz (Mark): „kein Gradient“. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Warum bei unsymmetrischem $\mathbf{A}$ der Faktor $2\mathbf{A}\mathbf{x}$ falsch ist und $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$ stimmt; der Text sagt es nur in Formeln.
- **Szenenname:** ml/k3quadform
- **Editor-Lücke:** machbar (Höhenlinien als Ellipsen)

### Artikel 09 — Die Hesse-Matrix und die quadratische Näherung (Soll 4, vorh. 2)

### V15 [A] Gemischte Differenz: Änderung der Änderung, in beiden Reihenfolgen
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/09-die-hesse-matrix-und-die-quadratische-naherung.md
- **Stelle:** Der Satz von Schwarz — „Den Grund sieht man an einer Rechnung, in der die Reihenfolge gar nicht vorkommt. Man verschiebt sich von $\mathbf{x}$ um $h$ in Richtung $x_1$ und um $k$ in Richtung $x_2$ …“
- **Art:** neue Animation
- **Was zu sehen ist:** Ein Rechteck in der Karte ($x_1\in[1;\,1{,}1]$, $x_2\in[2;\,2{,}1]$, stark vergrößert dargestellt) mit den vier Eckwerten von $f=x_1^2x_2+x_2^2$: $f(1,2)=6$ unten links, $f(1{,}1;\,2)=6{,}42$ unten rechts, $f(1;\,2{,}1)=6{,}51$ oben links, $f(1{,}1;\,2{,}1)=6{,}951$ oben rechts. Über und neben den Seiten die vier Kantendifferenzen als Beschriftungen: unten $0{,}42$, oben $0{,}441$, links $0{,}51$, rechts $0{,}531$. In der Mitte das Ergebnis $\Delta=0{,}021$ und $\Delta/(hk)=2{,}1\approx2x_1=2$.
- **Ablauf:** 1. Rechteck und Eckwerte erscheinen (FadeIn). 2. Erst waagrecht: die Differenzen unten ($0{,}42$) und oben ($0{,}441$) entstehen, dann ihre Differenz $0{,}441-0{,}42=0{,}021$ (Pfeil nach oben, Write): „Wie ändert sich der Anstieg in Richtung $x_1$, wenn man in Richtung $x_2$ geht?“ 3. Die Szene wird zurückgesetzt, jetzt senkrecht: links $0{,}51$, rechts $0{,}531$, Differenz $0{,}021$: dieselbe Zahl, andere Reihenfolge. 4. Beide Wege werden zu $\Delta/(hk)=2{,}1$ geteilt, daneben $\partial^2f/\partial x_2\partial x_1=2x_1=2$ (und die gleiche Zahl $\partial^2f/\partial x_1\partial x_2$). — Haltepunkte: Schritt 2 und 3.
- **Verständnisproblem:** Warum die Reihenfolge der Ableitungen gleichgültig ist: Beide lesen dieselben vier Zahlen, nur in anderer Klammerung.
- **Szenenname:** ml/k3schwarz
- **Editor-Lücke:** braucht Editor-Funktion: L1 (die waagrechten Beschriftungen müssen verschwinden, bevor die senkrechten kommen; Notbehelf: zwei getrennte Rechtecke nebeneinander); L9 nicht nötig

### V16 [A] Die Krümmung dreht mit der Richtung: zwischen kleinstem und größtem Eigenwert
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/09-die-hesse-matrix-und-die-quadratische-naherung.md
- **Stelle:** Die Krümmung in einer Richtung — „Wie stark ist das Gelände gewölbt, wenn man von $\mathbf{x}$ aus in Richtung $\mathbf{u}$ geht? …“
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Karte um $(1,\,2)$ ($x_1\in[0;2]$, $x_2\in[1;3]$) mit einem Einheitspfeil $\mathbf{u}$ am Punkt und den zwei Eigenrichtungen der Hesse-Matrix $\bigl(\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\bigr)$ (Eigenwerte $3\pm\sqrt5\approx5{,}236$ und $0{,}764$, Eigenvektoren bei $31{,}7^\circ$ und $121{,}7^\circ$ gestrichelt). Rechts Axes mit dem Winkel $\theta\in[0^\circ;180^\circ]$ waagrecht und der Krümmung $\mathbf{u}^{\top}\mathbf{H}\mathbf{u}=3+\cos2\theta+2\sin2\theta$ senkrecht ($0$ bis $6$), mit waagrechten Linien bei $0{,}764$ und $5{,}236$; ein Punkt auf der Kurve läuft mit $\mathbf{u}$ mit.
- **Ablauf:** 1. Karte und Eigenrichtungen. 2. $\mathbf{u}=\mathbf{e}_1$, $\theta=0$: Krümmung $4$ (Eintrag $H_{11}$). 3. $\mathbf{u}$ dreht sich (Rotate) und der Punkt läuft die Kurve entlang (MoveAlongPath); Halt bei $\mathbf{u}=(1,\,1)/\sqrt2$, $\theta=45^\circ$: $5$ (Rechenbeispiel $\tfrac12(4+2+2+2)$). 4. Weiter bis $31{,}7^\circ$: Höchstwert $5{,}236$ (Eigenvektor zu $\lambda_{\max}$), danach bis $121{,}7^\circ$: Tiefstwert $0{,}764$, beides auf den Linien. Beschriftung „zwischen $\lambda_{\min}$ und $\lambda_{\max}$“. 5. Zweite Kurve für die Schüssel $x_1^2+4x_2^2$ ($\mathbf{H}=\operatorname{diag}(2;8)$): Höchstwert $8$ bei $90^\circ$, Tiefstwert $2$ bei $0^\circ$, bei $45^\circ$ der Wert $5$. — Haltepunkte: Schritt 3 und 4.
- **Verständnisproblem:** „Die Krümmung liegt zwischen den Eigenwerten“ ist eine Zahlenaussage; die Bewegung zeigt, dass die Eigenvektoren die Richtungen größter und kleinster Wölbung sind und dass sie senkrecht aufeinander stehen.
- **Szenenname:** ml/k3kruemmdrehen
- **Editor-Lücke:** machbar (Rotate um den Punkt + MoveAlongPath auf der Kurve, wie V7)

### Artikel 10 — Rechengraphen (Soll 3, vorh. 2)

### V17 [A] Lokale Ableitungen an den Kanten, Summe über die Wege
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/10-rechengraphen.md
- **Stelle:** Lokale Ableitungen — „Im Graphen von Abb. 18 haben die vier Kanten von den Eingängen zu den Additionsknoten die lokale Ableitung $1$. …“ (Rechenbeispiel mit der Wegesumme $1\cdot5+1\cdot3=8$)
- **Art:** neue Animation (mit Rechenbild Skalarprodukt)
- **Was zu sehen ist:** Der Rechengraph von $f=(x_1+x_2)(x_2+x_3)$ wie in k3graph mit den Werten $x=(1,\,2,\,3)$, $v_1=3$, $v_2=5$, $f=15$, jetzt mit Zahlen an den Kanten: $x_1\to v_1$: $1$; $x_2\to v_1$: $1$; $x_2\to v_2$: $1$; $x_3\to v_2$: $1$; $v_1\to f$: $5$ ($=v_2$); $v_2\to f$: $3$ ($=v_1$). Darunter die Rechenbilder.
- **Ablauf:** 1. Der Graph mit den Vorwärtswerten steht da (vorhandene Szene wiederverwenden). 2. Die lokalen Ableitungen erscheinen an den Kanten nacheinander (Write): erst die vier Einsen, dann $5$ und $3$ (je mit Hinweis „$v_2$“, „$v_1$“ als gespeichertem Wert). 3. Für $x_1$ leuchtet der Weg $x_1\to v_1\to f$ auf (Indicate, blau), unten $1\cdot5=5$. 4. Für $x_3$ der Weg $x_3\to v_2\to f$: $1\cdot3=3$. 5. Für $x_2$ leuchten beide Wege nacheinander auf (blau, orange), unten das Rechenbild Skalarprodukt $(1,\,1)\cdot(5,\,3)=1\cdot5+1\cdot3=8$. — Haltepunkte: Schritt 5.
- **Verständnisproblem:** Warum der Eingang mit zwei Nachfolgern ($x_2$) beide Wege addiert, während $x_1$ und $x_3$ nur je einen Weg haben; und woher die Kantenzahlen $5$ und $3$ stammen (die gespeicherten Werte der Vorwärtsrechnung).
- **Szenenname:** ml/k3lokal
- **Editor-Lücke:** machbar (Operation Skalarprodukt vorhanden; Graph aus TextBox/LabeledArrow); diese Szene baut die Grundlage für den Rückwärtsmodus in Artikel 11

### Artikel 11 — Automatische Differentiation (Soll 5, vorh. 1)

### V18 [A] Vorwärtsmodus: der Tangentenwert läuft mit der Rechnung mit
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/11-automatische-differentiation.md
- **Stelle:** Der Vorwärtsmodus — „Die erste Möglichkeit folgt der Rechnung selbst. Man legt fest, in welche Richtung man die Eingänge verändert, und führt bei jedem Knoten neben seinem Wert mit, wie schnell er sich bei dieser Veränderung ändert.“
- **Art:** neue Animation (mit Rechenbild Skalarprodukt)
- **Was zu sehen ist:** Der Rechengraph von $f=(x_1+x_2)(x_2+x_3)$ wie in Abb. 18 (Szene ml/k3graph) an der Stelle $(1,\,2,\,3)$. An jedem Knoten zwei Zahlen: der Wert (grün, $1;\,2;\,3;\,3;\,5;\,15$) und der Tangentenwert (violett). Oben die gewählte Richtung $\dot{\mathbf{x}}=\mathbf{e}_2=(0,\,1,\,0)$. Unten rechts drei kleine Felder „Durchlauf $\mathbf{e}_1$“, „$\mathbf{e}_2$“, „$\mathbf{e}_3$“ für das Ergebnis $\dot f=5;\ 8;\ 3$.
- **Ablauf:** 1. Der Graph mit den grünen Werten steht da (wiederverwendete Szene, Werte schon vorhanden). 2. Die Tangentenwerte der Eingänge erscheinen: $0;\ 1;\ 0$ (Write). 3. Ein Marker (Dot) läuft die Kanten entlang (MoveAlongPath) zu $v_1$ und $v_2$: $\dot v_1=0+1=1$, $\dot v_2=1+0=1$. 4. Am Ergebnis das Rechenbild Skalarprodukt $(v_2,\ v_1)\cdot(\dot v_1,\ \dot v_2)=(5,\,3)\cdot(1,\,1)=5\cdot1+3\cdot1=8$ (Kern des Rechenbeispiels); das erste Feld füllt sich mit $8$ und dem Hinweis „$=\partial f/\partial x_2$“. 5. Die Szene läuft noch zweimal (Richtung $\mathbf{e}_1$: $\dot v_1=1$, $\dot v_2=0$, $\dot f=5$; $\mathbf{e}_3$: $\dot f=3$), die übrigen Felder füllen sich; Beschriftung „drei Durchläufe für drei Eingänge“. — Haltepunkte: Schritt 3 und 5.
- **Verständnisproblem:** Was ein „Tangentenwert“ ist (Änderungsrate eines Knotens bei einer festen Richtung der Eingänge) und warum ein Durchlauf nur eine Richtung, also eine Spalte liefert; das ist die Voraussetzung, um den Gewinn des Rückwärtsmodus zu sehen.
- **Szenenname:** ml/k3vorwaerts
- **Editor-Lücke:** machbar (Graph wie k3graph, Operation Skalarprodukt vorhanden); drei Durchläufe als drei Zustände nacheinander statt als echte Wiederholung (L1 würde die Zwischenwerte wieder verschwinden lassen)

### V19 [A] Ein Rückwärtsdurchlauf gegen n Vorwärtsdurchläufe: der Aufwand
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/11-automatische-differentiation.md
- **Stelle:** Der Aufwand — „Warum ist der Rückwärtsmodus so wichtig? Weil er den Gradienten einer Funktion mit sehr vielen Eingängen fast so billig liefert wie den Funktionswert selbst.“
- **Art:** neue Animation
- **Was zu sehen ist:** Oben ein kleiner Streifen mit $n=3$: links drei übereinanderstehende Mini-Graphen (je ein Vorwärtsdurchlauf, Beschriftung $\mathbf{e}_1$, $\mathbf{e}_2$, $\mathbf{e}_3$, Ergebnis $5$, $8$, $3$ je Durchlauf), rechts ein einziger Mini-Graph mit „vorwärts + rückwärts“ und allen drei Ergebnissen $(5,\,8,\,3)$ auf einmal. Darunter Axes mit logarithmischer Zeitachse (Sekunden, $1$ bis $10^{7}$) und drei waagrechten Balken für $n=10^6$ Eingänge und eine Sekunde je Auswertung: Vorwärtsmodus $10^6\,\mathrm{s}$ (gut $11$ Tage), zentrale Differenzen $2\cdot10^6\,\mathrm{s}$ (gut $23$ Tage, nur ungefähr richtig), Rückwärtsmodus etwa $3\,\mathrm{s}$ ($c\approx3$).
- **Ablauf:** 1. Die drei Mini-Graphen links erscheinen nacheinander (FadeIn), jeder liefert eine Zahl. 2. Rechts der eine Mini-Graph mit Hin- und Rückweg, alle drei Zahlen auf einmal. 3. Die Achse mit den Sekunden. 4. Die Balken wachsen nacheinander (Create): $10^6$, $2\cdot10^6$, dann der winzige für $3\,\mathrm{s}$; Beschriftung „Zeit wächst mit $n$“ gegen „Zeit unabhängig von $n$“. — Haltepunkte: Schritt 4.
- **Verständnisproblem:** Der Text behauptet „unabhängig von $n$“, aber erst das Nebeneinander von $n$ Durchläufen gegen einen zeigt, warum man Gradienten von Millionen Parametern überhaupt ausrechnen kann.
- **Szenenname:** ml/k3aufwand
- **Editor-Lücke:** machbar (Stem/Balken oder Rechtecke auf logarithmischer Achse; Axes kann log)

### V20 [B] Die fünf Muster im Rückwärtsfluss
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/11-automatische-differentiation.md
- **Stelle:** Muster im Rückwärtsfluss — „Nach Tabelle 4 verhalten sich die Grundoperationen beim Rückwärtsrechnen auf einfache, wiederkehrende Weise. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Fünf kleine Bausteine in einer Reihe, jeder mit der ankommenden Adjungierten $\bar b$ (rot) am Ausgang und den weitergegebenen Adjungierten an den Eingängen. (a) Addition, $\bar b=2$: beide Eingänge erhalten $2$. (b) Multiplikation mit $a_1=4$, $a_2=3$, $\bar b=2$: $\bar a_1=2\cdot3=6$, $\bar a_2=2\cdot4=8$ (vertauscht). (c) Maximum von $1$ und $2$, $\bar b=3$: $\bar a_1=0$, $\bar a_2=3$. (d) logistische Funktion mit $b=0{,}8$, $\bar b=2$: $\bar a=2\cdot0{,}8\cdot0{,}2=0{,}32$. (e) Knoten mit zwei Nachfolgern, $\bar b_1=5$, $\bar b_2=3$: $\bar a=5+3=8$.
- **Ablauf:** 1. Baustein (a): Die Zahl $2$ am Ausgang (FadeIn) läuft entgegen der Pfeilrichtung zu beiden Eingängen (Shift der roten Zahl) — „verteilt“. 2. (b): Die Zahl läuft zu jedem Eingang und wird mit dem Wert des anderen Eingangs multipliziert (Zahl wechselt) — „vertauscht“. 3. (c): Die Zahl läuft nur zum größeren Eingang, der kleinere erhält $0$ — „leitet weiter“. 4. (d): Die Zahl wird mit $0{,}16$ multipliziert — „bremst“. 5. (e): Zwei Zahlen $5$ und $3$ laufen aus verschiedenen Kanten zu einem Knoten und addieren sich zu $8$ — „addiert“. — Haltepunkte: Schritt 2 und 5.
- **Verständnisproblem:** Fünf Regeln, die nur als Aufzählung dastehen; sie sind das Handwerkszeug, um Rückwärtsrechnungen in Programmen zu lesen.
- **Szenenname:** ml/k3muster
- **Editor-Lücke:** machbar (TextBox, LabeledArrow, Zahl per Shift/MoveTo verschieben)

### V21 [B] Klammerung: Zeile mal Matrizen gegen Matrizen mal Matrizen
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/11-automatische-differentiation.md
- **Stelle:** Klammerung: Vektor mal Jacobi-Matrix — „Der Unterschied der beiden Modi lässt sich auch mit Matrizen beschreiben. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Die Kette $\mathbf{J}=\mathbf{J}_4\,\mathbf{J}_3\,\mathbf{J}_2\,\mathbf{J}_1$ als Reihe von Rechtecken (Rectangle): drei große Quadrate $1000\times1000$ ($\mathbf{J}_3,\mathbf{J}_2,\mathbf{J}_1$) und eine flache Zeile $1\times1000$ ($\mathbf{J}_4$) ganz links. Darunter ein Zähler „Rechenschritte“.
- **Ablauf:** 1. Die vier Rechtecke erscheinen (FadeIn). 2. Rückwärtsmodus (von links klammern): Die Zeile schiebt sich über $\mathbf{J}_3$ (Shift, beide verschmelzen zu einer neuen Zeile), Zähler $2\cdot10^6$; dann über $\mathbf{J}_2$, dann über $\mathbf{J}_1$; Zähler $6\cdot10^6$. Die Form bleibt dabei eine schlanke Zeile. 3. Zurücksetzen. 4. Vorwärtsmodus (von rechts klammern): $\mathbf{J}_2\mathbf{J}_1$ verschmelzen zu einem vollen Quadrat (Zähler $2\cdot10^9$), dann $\mathbf{J}_3$ mit ihm ($4\cdot10^9$), zuletzt die Zeile ($4\cdot10^9$). Beschriftung „rund $670$-mal so viel“. — Haltepunkte: Schritt 2 und 4.
- **Verständnisproblem:** Warum die Reihenfolge der Klammerung den Aufwand um den Faktor $670$ ändert, obwohl das Produkt gleich bleibt; der Text rechnet nur Zahlen.
- **Szenenname:** ml/k3klammer
- **Editor-Lücke:** braucht Editor-Funktion: L7 (Matrix·Matrix als Prozess); Notbehelf: Rechtecke, die sich per Shift/Scale vereinigen, Zähler als Text je Schritt

### Artikel 12 — Numerische Ableitung und Gradientenprüfung (Soll 4, vorh. 1)

### V22 [A] Vorwärts-, Rückwärts- und zentrale Sekante: die Krümmung hebt sich heraus
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/12-numerische-ableitung-und-gradientenprufung.md
- **Stelle:** Die zentrale Differenz — „Die Vorwärtsdifferenz misst die Steigung der Sekante zwischen $x$ und $x+h$, und diese Sekante ist bei einer gekrümmten Kurve systematisch steiler oder flacher als die Tangente in $x$. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Axes $x\in[0{,}5;\ 3]$, $y\in[0;\ 25]$; der Graph von $x^3$ (blau), der Punkt $(2,\,8)$, die Tangente der Steigung $12$ (gestrichelt, schwarz). Mit $h=0{,}5$: die Vorwärts-Sekante durch $(2,\,8)$ und $(2{,}5;\ 15{,}625)$ mit Steigung $15{,}25$ (rot, steiler), die Rückwärts-Sekante durch $(1{,}5;\ 3{,}375)$ und $(2,\,8)$ mit Steigung $9{,}25$ (orange, flacher) und die zentrale Sekante durch $(1{,}5;\ 3{,}375)$ und $(2{,}5;\ 15{,}625)$ mit Steigung $12{,}25$ (grün, fast parallel zur Tangente). Daneben eine kleine Fehlertafel für $h=0{,}5$ und $h=0{,}25$: vorwärts $3{,}25 \to 1{,}5625$, zentral $0{,}25\to0{,}0625$.
- **Ablauf:** 1. Graph, Punkt, Tangente (Create). 2. Die Vorwärts-Sekante erscheint (Create), Beschriftung „$15{,}25$, zu steil“. 3. Die Rückwärts-Sekante erscheint, „$9{,}25$, zu flach“. 4. Die zentrale Sekante erscheint, dazu der Hinweis „$12{,}25=\tfrac12(15{,}25+9{,}25)$“. 5. Mit $h=0{,}25$ erscheinen die drei Sekanten neu in blasseren Farben ($13{,}5625$; $10{,}5625$; $12{,}0625$); die Fehlertafel wird gefüllt: vorwärts halbiert sich nur (Faktor $\approx2$), zentral wird es viermal kleiner. — Haltepunkte: Schritt 4 und 5.
- **Verständnisproblem:** Warum die symmetrische Sekante genauer ist, obwohl sie nur eine Auswertung mehr braucht: Die beiden Fehler der einseitigen Sekanten haben entgegengesetztes Vorzeichen und mitteln sich fast weg.
- **Szenenname:** ml/k3zentral
- **Editor-Lücke:** machbar (TangentLine mit Sekante, drei Sekanten je zwei Punkte); eine fließend schrumpfende Schrittweite wäre L3. Nicht doppelt mit ml/k3sekante (Artikel 02): dort nähern sich Sekanten der Tangente, hier geht es um die Symmetrie.

### V23 [A] Gradientenprüfung: Komponente für Komponente gegen die Skala
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/12-numerische-ableitung-und-gradientenprufung.md
- **Stelle:** Die Gradientenprüfung — „Wer einen Gradienten von Hand herleitet oder als Rückwärtsschritte programmiert, macht leicht Fehler: …“ (Rechenbeispiel 1 mit dem vergessenen Faktor)
- **Art:** neue Animation
- **Was zu sehen ist:** Links die Funktion $f=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ und eine Tabelle mit den Spalten „berechnet $g_\mathrm{a}$“, „numerisch $g_\mathrm{n}$“, „$\rho$“. Rechts eine senkrechte logarithmische Skala für $\rho$ von $10^{-9}$ bis $1$ mit drei Bereichen: unter $10^{-7}$ grün („gut“), von $10^{-4}$ bis $10^{-2}$ gelb („verdächtig“), über $10^{-2}$ rot („Fehler in der Formel“).
- **Ablauf:** 1. Tabelle mit der Formel des Beispiels: $g_\mathrm{a}=(4,\,3)$ (Write). 2. Komponente 1: zwei Punkte $x_1\pm h$ auf der Karte (Dots, $h=0{,}001$), die Funktionswerte $6{,}004002$ und $5{,}996002$ erscheinen, daraus $g_{\mathrm n,1}=4$; $\rho_1=0$, ein grüner Marker. 3. Komponente 2: $x_2\pm h$, Werte $6{,}005001$ und $5{,}995001$, $g_{\mathrm n,2}=5$; $\rho_2=|3-5|/5=0{,}4$, ein roter Marker weit oben, Beschriftung „Komponente 2 falsch“. 4. Die korrigierte Formel $x_1^2+2x_2$ ergibt $g_\mathrm{a,2}=5$: der Marker fällt in den grünen Bereich. — Haltepunkte: Schritt 3.
- **Verständnisproblem:** Wie aus zwei Zahlenreihen ein Urteil wird und welche Größenordnung des relativen Fehlers „falsch“ und „richtig“ heißt; der Text nennt die Schwellen nur im Absatz.
- **Szenenname:** ml/k3pruefung
- **Editor-Lücke:** machbar (Marker auf logarithmischer Axes-Skala)

### V24 [B] Auslöschung: beim Abziehen bleiben nur noch die hinteren Stellen
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/12-numerische-ableitung-und-gradientenprufung.md
- **Stelle:** Was du dafür brauchst: Gleitkommazahlen — „Gefährlich wird die Rundung beim Abziehen fast gleicher Zahlen. …“
- **Art:** neue Animation
- **Was zu sehen ist:** Zwei Ziffernreihen (TextBox je Ziffer) untereinander, Ziffernanzahl $16$: $f(2+h)\approx8{,}000000120000001$ und $f(2)=8{,}000000000000000$ für $h=10^{-8}$ (schematisch, die letzte Stelle ist gerundet). Darunter die Differenz $0{,}000000120000001$. Die Rundungsfehler der Funktionswerte sind als Schraffur an den letzten ein bis zwei Stellen markiert. Rechts ein Zähler „richtige Stellen“.
- **Ablauf:** 1. Beide Zahlen erscheinen, alle $16$ Stellen sind „richtig“ (grün). 2. Die ersten acht Stellen, in denen die Zahlen übereinstimmen, werden ausgegraut und fallen beim Abziehen weg (Shift nach unten, Indicate). 3. Es bleiben die hinteren Stellen $1\,2\,0\,0\,0\,0\,0\,0\,1$; die letzte (oder die letzten beiden) wird rot, weil dort der Rundungsfehler steckt, der Zähler zeigt „etwa $8$“. 4. Die Division durch $h=10^{-8}$ verschiebt nur das Komma (Pfeil), die Zahl der richtigen Stellen bleibt: $12{,}000001\ldots$ mit etwa acht richtigen Stellen. — Haltepunkte: Schritt 2 und 3.
- **Verständnisproblem:** Warum gerade das Kleinerwerden von $h$, das den Abschneidefehler senkt, die Zahl der brauchbaren Stellen vernichtet; Auslöschung ist ein Begriff ohne Anschauung im Text.
- **Szenenname:** ml/k3ausloeschung
- **Editor-Lücke:** machbar (Ziffern als TextBox-Reihen; ein stellenweises Verschmelzen wäre L7)

### Artikel 13 — Das Wichtigste bis hier (Soll 1, vorh. 0)

### V25 [A] Ein Prinzip: unter der Lupe ist alles linear (vorhandene Szene wiederverwenden)
- **Artikel:** content/ml/03-ableitung-gradient-und-kettenregel/13-das-wichtigste-bis-hier.md
- **Stelle:** Ein Prinzip hinter allen Ergebnissen — „Fast alles in diesem Kapitel folgt aus einem Prinzip: Nahe genug an einer Stelle ist jede differenzierbare Funktion linear. …“
- **Art:** vorhandene Szene wiederverwenden
- **Was zu sehen ist:** ml/k3lupe aus Artikel 02: der Graph von $x^3$ und seine Tangente in drei Ausschnitten, jeder zehnmal schmaler als der vorige.
- **Ablauf:** wie bei der vorhandenen Szene (Ausschnitte nacheinander); Bildunterschrift neu: „Das eine Prinzip: Unter der Lupe wird eine glatte Funktion zur Geraden, im Raum zur Ebene, bei mehreren Ausgängen zur Matrix.“
- **Verständnisproblem:** Die Zusammenschau verweist auf ein Prinzip, das der Leser in Artikel 02 als Bild gesehen hat; hier erinnert dasselbe Bild daran, dass alle späteren Ergebnisse (Gradient, Jacobi-Matrix, Kettenregel) dieselbe Lupe in höheren Dimensionen sind.
- **Szenenname:** ml/k3lupe (wiederverwendet; die Animation kommt aus Artikel 02)
- **Editor-Lücke:** machbar (wie k3lupe: L4 für stetigen Zoom, sonst drei Ausschnitte)

## Vorhandene Abbildungen

### Artikel 02
- ml/k3sekante (02-die-ableitung.md): animieren ja — Schritte: 1. Graph $x^3$ (Create) und Punkt $(2,\,8)$. 2. Sekante $h=1$ (rot, Steigung 19) mit zweitem Punkt $(3,\,27)$. 3. Zweiter Punkt rückt nach $h=0{,}5$ (Steigung 15,25), dann $h=0{,}1$ (12,61). 4. Tangente gestrichelt, Steigung 12. | Lücke: machbar; L1 (alte Sekante verschwindet) und L3 (stetiges $h$) würden es flüssiger machen
- ml/k3lupe (02-die-ableitung.md): animieren ja — Schritte: 1. Ausschnitt breit mit Kurve und Tangente. 2. zehnmal schmaler. 3. nochmals zehnmal schmaler, Kurve und Tangente nicht mehr zu unterscheiden. | Lücke: L4 (Zoom; hier 2D-Kamera), Notbehelf: drei Ausschnitte als Folge von FadeIn
- ml/k3rtaylor1 (02-die-ableitung.md): animieren ja — heute nur ein statisches MathTex ($8+12\cdot0{,}01+\tfrac12\cdot12\cdot0{,}01^2=8{,}1206$), keine Editor-Operation. Ersetzen durch Operation Summation: Summanden $8$; $0{,}12$; $0{,}0006$ wachsen zu $8{,}1206$, daneben der genaue Wert $8{,}120601$. | Lücke: machbar

### Artikel 03
- ml/k3getriebe (03-die-kettenregel.md): animieren ja — Schritte: 1. Drei Zahlenstrahlen mit gleichem Maßstab. 2. Das blaue Stück $\Delta x=0{,}01$ erscheint. 3. Es wird auf das Dreifache gestreckt, orange $\Delta u=0{,}03$ (Scale). 4. Es wird auf das Achtfache gestreckt, rot $\Delta y\approx0{,}24$. | Lücke: machbar
- ml/k3logistisch (03-die-kettenregel.md): animieren ja — Schritte: 1. Achsen, $\sigma$ (Create). 2. Ableitungskurve (Create). 3. Marker bei $0$ ($\sigma'=\tfrac14$) und $2$ (0,1050). 4. Ein Punkt läuft über $\sigma$ (MoveAlongPath), die Tangente steiler und flacher. | Lücke: machbar, mitlaufende Tangente braucht L3

### Artikel 04
- ml/k3schnitt (04-partielle-ableitungen-und-der-gradient.md): animieren ja — Schritte: 1. Höhenlinien $2;4;6;8;10$ nacheinander. 2. Blaue Schnittgerade $x_2=2$ durch $(1,\,2)$, daneben (b) die Schnittkurve $2x_1^2+4$ mit Steigung 4. 3. Rote Gerade $x_1=1$, (c) Schnittkurve $x_2+x_2^2$ mit Steigung 5. | Lücke: machbar
- ml/k3rlinear (04-partielle-ableitungen-und-der-gradient.md): animieren ja — heute nur ein statisches MathTex (Skalarprodukt $4\cdot0{,}01+5\cdot0{,}02$), keine Editor-Operation. Ersetzen durch die Operation Skalarprodukt mit $(4,\,5)\cdot(0{,}01;\ 0{,}02)=0{,}14$, dazu $6+0{,}14=6{,}14$. Pflicht-Rechenbild (Kern des Rechenbeispiels). | Lücke: machbar
### Artikel 05
- ml/k3rrichtung (05-richtungsableitung-und-steilster-anstieg.md): animieren ja, Umbau — heute nur ein statisches MathTex, keine Editor-Operation; siehe V8 (Skalarprodukt $4\cdot0{,}6+5\cdot0{,}8=6{,}4$). | Lücke: machbar
- ml/k3hoehen (05-richtungsableitung-und-steilster-anstieg.md): animieren ja — Schritte: 1. Höhenlinien der runden Schüssel (a) nacheinander (Create). 2. Gradientenpfeile an den Punkten wachsen (GrowFromCenter), alle zeigen vom Mittelpunkt weg. 3. Gestreckte Schüssel (b): Höhenlinien, Pfeile senkrecht zu ihnen. 4. Am Punkt $(1,\,1)$ der steilste Abstieg (blau) und die Richtung zum tiefsten Punkt (gestrichelt), $31^\circ$ dazwischen. | Lücke: machbar

### Artikel 06
- ml/k3rjacobi (06-die-jacobi-matrix.md): animieren ja, Umbau — heute nur ein statisches MathTex (zwei Zeilen Skalarprodukt $2\cdot0{,}1+1\cdot(-0{,}1)=0{,}1$ und $2\cdot0{,}1+4\cdot(-0{,}1)=-0{,}2$), keine Editor-Operation. Ersetzen durch die Operation Skalarprodukt je Zeile (zwei Mal) oder Matrix mal Vektor Zeile für Zeile: Zeile 1 entsteht, Ergebnis $0{,}1$; Zeile 2, Ergebnis $-0{,}2$; dann $\mathbf{g}(2{,}1;\ 5{,}8)$ gegen genau $(2{,}09;\ 5{,}81)$. | Lücke: machbar (Zeile für Zeile); Matrix·Vektor als eine Operation wäre L7

### Artikel 07
- ml/k3wege (07-die-kettenregel-fur-mehrere-variablen.md): animieren ja — Schritte: 1. Knoten $x_1,x_2$, $u_1,u_2$, $F$ erscheinen (FadeIn). 2. Der Weg über $u_1$ (blau) zeichnet sich, Faktoren $2$ und $4$ an den Kanten. 3. Der Weg über $u_2$ (orange), Faktoren $2$ und $3$. 4. Ein Marker (Dot) läuft über beide Wege (MoveAlongPath), am Ziel addieren sich $8$ und $6$ zu $14$. | Lücke: machbar
- ml/k3rwege (07-die-kettenregel-fur-mehrere-variablen.md): animieren ja, Umbau — heute nur ein statisches MathTex, keine Editor-Operation; siehe V12.

### Artikel 08
- ml/k3rresiduum (08-ableiten-nach-vektoren-und-matrizen.md): animieren ja, Umbau — heute nur ein statisches MathTex ($\mathbf{A}^{\top}\mathbf{r}$ komponentenweise), keine Editor-Operation. Ersetzen durch zwei Skalarprodukte: $(1,\,0)\cdot(-3,\,-1)=-3$ und $(2,\,1)\cdot(-3,\,-1)=-7$ (Spalten von $\mathbf{A}$ mit dem Residuum), dann Multiplikation mit $-2$: $(6,\,14)$. Pflicht-Rechenbild. | Lücke: machbar
- ml/k3rrueck (08-ableiten-nach-vektoren-und-matrizen.md): animieren ja, Umbau — heute nur ein statisches MathTex, keine Editor-Operation. Ersetzen durch zwei Skalarprodukte der Spalten von $\mathbf{A}$ mit $\nabla f=(1,\,0,\,-1)$: $(1,\,0,\,3)\cdot(1,\,0,\,-1)=-2$ und $(2,\,-1,\,1)\cdot(1,\,0,\,-1)=1$; passend dazu steht V13 für den Teil nach $\mathbf{A}$. Pflicht-Rechenbild. | Lücke: machbar
### Artikel 09
- ml/k3rtaylor2 (09-die-hesse-matrix-und-die-quadratische-naherung.md): animieren ja, Umbau — heute nur ein statisches MathTex (Doppelsumme $\tfrac12\mathbf{h}^{\top}\mathbf{H}\mathbf{h}$ mit $4\cdot0{,}01^2+2\cdot2\cdot0{,}01\cdot0{,}02+2\cdot0{,}02^2$), keine Editor-Operation. Ersetzen durch die Operation Summation (Doppelsumme als vier Summanden $0{,}0004$; $0{,}0004$; $0{,}0004$; $0{,}0004\ldots$ bzw. die drei zusammengefassten Glieder $0{,}0004+0{,}0008+0{,}0008=0{,}002$), dann $\tfrac12\cdot0{,}002=0{,}001$ und $6+0{,}14+0{,}001=6{,}141$. Pflicht-Rechenbild. | Lücke: machbar
- ml/k3rkruemmung (09-die-hesse-matrix-und-die-quadratische-naherung.md): animieren ja, Umbau — heute nur ein statisches MathTex ($\mathbf{u}^{\top}\mathbf{H}\mathbf{u}$ für $\mathbf{u}=(1,1)/\sqrt2$), keine Editor-Operation. Ersetzen durch Matrix·Vektor Zeile für Zeile, danach Skalarprodukt mit $\mathbf{u}$, Ergebnis $5$ (zwei Schritte, $\mathbf{H}\mathbf{u}=(6,\,4)/\sqrt2$, dann $\mathbf{u}\cdot\mathbf{H}\mathbf{u}=5$). Kann mit V16 zusammengelegt werden (die Zahl $5$ bei $45^\circ$ erscheint dort als Haltepunkt), dann entfällt diese Szene. | Lücke: machbar

### Artikel 10
- ml/k3rvierfaktoren (10-rechengraphen.md): animieren ja, Umbau — heute nur ein statisches MathTex ($2\cdot3\cdot4+1\cdot3\cdot4+1\cdot2\cdot4+1\cdot2\cdot3=24+12+8+6=50$), keine Editor-Operation. Ersetzen durch Summation mit vier Summanden, jedes Produkt aus drei Faktoren entsteht einzeln und wandert in die Summe; der Faktor $1$ (Ableitung des ersetzten Faktors) wird je Summand farbig hervorgehoben. Pflicht-Rechenbild. | Lücke: machbar
- ml/k3graph (10-rechengraphen.md): animieren ja — Schritte: 1. Die drei Eingangsknoten mit $1;\,2;\,3$ erscheinen. 2. Die Additionsknoten $v_1$, $v_2$ mit ihren Pfeilen (Create), die grünen Werte $3$ und $5$ wachsen. 3. Der Multiplikationsknoten, Wert $15$. 4. Die Verzweigung bei $x_2$ wird hervorgehoben (Indicate). | Lücke: machbar
### Artikel 11
- ml/k3rueckwaerts (11-automatische-differentiation.md): animieren ja — Schritte: 1. Der Graph mit den grünen Vorwärtswerten erscheint. 2. $\bar f=1$ (rot) am Ergebnis (FadeIn). 3. $\bar v_2=1\cdot v_1=3$ läuft entgegen der Pfeilrichtung zu $v_2$ (Shift, mit lokaler Ableitung $3$), dann $\bar v_1=5$. 4. $\bar x_3=3$ und $\bar x_1=5$ entstehen. 5. Bei $x_2$ kommen zwei Zahlen $5$ und $3$ an und addieren sich zu $\bar x_2=8$ (Rechenbild Summation $5+3$). | Lücke: machbar
### Artikel 12
- ml/k3vkurve (12-numerische-ableitung-und-gradientenprufung.md): animieren ja — Schritte: 1. Doppelt logarithmische Axes ($h$ von $10^{-15}$ bis $10^{-1}$, Fehler). 2. Die Abschätzungskurven (gestrichelt) erscheinen: rechts die Geraden mit Steigung $1$ (vorwärts) und $2$ (zentral), links die Gerade mit Steigung $-1$. 3. Die gemessenen Punkte (58 Dots) erscheinen von rechts nach links, als würde $h$ kleiner (FadeIn in Gruppen): erst fallen sie, dann steigen sie wieder, links streuen sie. 4. Die tiefsten Punkte bei $h\approx10^{-8}$ und $h\approx3\cdot10^{-6}$ werden hervorgehoben (Indicate). | Lücke: machbar (Gruppen von Dots); ein laufendes $h$ wäre L3

### Artikel 13
- keine vorhandene Abbildung; siehe V25 (k3lupe wiederverwenden).

### Hinweis zu den Rechenbildern
Alle zehn Rechenbilder k3r… des Hefts (k3rtaylor1, k3rlinear, k3rrichtung, k3rjacobi, k3rwege, k3rresiduum, k3rrueck, k3rtaylor2, k3rkruemmung, k3rvierfaktoren) bestehen aus einem einzigen statischen MathTex ohne Editor-Operation. Zehn weitere vorhandene Szenen (k3sekante, k3lupe, k3getriebe, k3logistisch, k3schnitt, k3hoehen, k3wege, k3graph, k3rueckwaerts, k3vkurve) sind Konzeptbilder aus Achsen, Kurven, Pfeilen und Kästen. Die vorhandenen Rechenbilder, die als echte Operation neu gebaut werden sollen, stehen unter den Artikeln 02, 04, 05, 06, 07, 08, 09 und 10 (V8 und V12 sind Umbauten und zählen in der Bilanz nicht als neue Abbildung). In den neuen Szenen V4 (Produkt), V17 und V18 (Skalarprodukt) ist die Pflicht-Rechnung schon enthalten.
