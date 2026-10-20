---
title: Zusammenschaltung von Widerständen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50600
summary: Von Grund auf – wie man Widerstände hintereinander und nebeneinander zu einem einzigen Ersatzwiderstand zusammenfasst und wie sich Spannung und Strom dabei aufteilen. Leitbild sind die Nagelbretter aus dem Artikel über den Widerstand: Hintereinander addieren sich die Längen und damit die Widerstände, nebeneinander die Breiten und damit die Leitwerte. Mit Schaltungszwang aus den Kirchhoffschen Regeln, Reihen- und Parallelschaltung, Spannungs- und Stromteiler, Widerstandsketten in Digital-Analog- und Flash-Analog-Digital-Wandlern, dem R-2R-Netzwerk, gemischten Schaltungen und dem belasteten Spannungsteiler samt Ersatzquelle. Mit Beispiel-Seite.
tags: Reihenschaltung, Parallelschaltung, Ersatzwiderstand, Spannungsteiler, Stromteiler
---

## Anschaulich

Die Kirchhoffschen Regeln lösen jedes Netz, aber für zwei Grundmuster gibt es Abkürzungen: Widerstände, die hintereinander liegen, und solche, die
nebeneinander liegen. Beide lassen sich durch einen einzigen __Ersatzwiderstand__ ersetzen, der sich nach außen genauso verhält. Aus den beiden Mustern
folgen zwei Regeln, die man in jeder Schaltung braucht: wie sich eine Spannung auf hintereinanderliegende Widerstände aufteilt und wie sich ein Strom
auf nebeneinanderliegende verteilt.

**Das Leitbild dieses Artikels:** **die Nagelbretter aus dem Artikel über den Widerstand.** Ein Widerstand ist dort ein schräges Brett voller Nägel, und
sein Widerstand wächst mit der Länge und sinkt mit der Breite. Legt man zwei Bretter hintereinander, müssen alle Kugeln durch beide, und das Brett ist
im Ganzen länger. Legt man sie nebeneinander zwischen dieselbe obere und untere Kante, verteilen sich die Kugeln, und das Brett ist im Ganzen breiter.

Drei Folgerungen kann man den Brettern direkt ansehen:

- **Hintereinander addieren sich die Widerstände.** Durch jedes Brett laufen pro Sekunde gleich viele Kugeln, und die Höhenunterschiede addieren sich
  — wie die Längen.
- **Nebeneinander addieren sich die Leitwerte.** Jedes Brett hat denselben Höhenunterschied, und die Kugeln pro Sekunde addieren sich — wie die
  Breiten.
- **An der Naht liegt eine Zwischenhöhe.** Zwischen zwei hintereinanderliegenden Brettern liegt die Naht auf einer Höhe, die den Höhenunterschied im
  Verhältnis der Widerstände teilt. Zweigt dort ein drittes Brett ab, laufen Kugeln seitlich weg, und die Naht sinkt ab.

Das Längen-und-Breiten-Bild stimmt genau für gleiche Bretter aus demselben Material; dass die Regeln für beliebige Widerstände gelten, zeigen die
Herleitungen aus den Kirchhoffschen Regeln.

:::grafik
Szene: get1/stroeme-und-spannungen/06-nagelbretter · Vorlage: bretter-reihe-parallel
Zwei Nagelbretter mit Kugeln. Ein Schalter „hintereinander" setzt sie in Laufrichtung aneinander: Ein Zähler an jedem Brett zeigt dieselbe Zahl Kugeln pro
Sekunde, ein Höhenmaßstab daneben zerlegt den Gesamthöhenunterschied in zwei Teile, die zusammen den ganzen ergeben; die Anzeige $R_\text{ges}$ ist die
Summe. Ein Schalter „nebeneinander" stellt die Bretter Seite an Seite zwischen dieselbe obere und untere Kante: Beide haben denselben Höhenunterschied, die
Zähler addieren sich zum Gesamtstrom, die Anzeige $G_\text{ges}$ ist die Summe der Leitwerte. Ein dritter Schalter öffnet an der Naht der
hintereinanderliegenden Bretter einen Seitenausgang: Kugeln fließen ab, die Höhe der Naht sinkt sichtbar. Kernaussage: Hintereinander addieren sich
Widerstände wie Längen, nebeneinander Leitwerte wie Breiten. (Blau = Kugeln, rot = Ersatzgrößen, orange = Seitenausgang und Nahthöhe, grau = Bretter und
Maßstab.)
:::

## Die Reihenschaltung

**Die Akteure:**

- $n$ Widerstände $R_1, \dots, R_n$ in Ohm, hintereinander zwischen zwei Klemmen, ohne Abzweig dazwischen;
- die Spannung $U$ über der ganzen Kette und die Teilspannungen $U_1, \dots, U_n$, alle im VZS zum Strom gezählt;
- die Ströme $I_1, \dots, I_n$ durch die einzelnen Widerstände und der Strom $I$ in die Kette.

**Das Zusammenspiel:** *Welcher einzelne Widerstand verhält sich nach außen wie die ganze Kette?*

Das Skript nennt die Bedingung, die die Verschaltung erzwingt, den __Schaltungszwang__: In der Reihe fließt durch alle Widerstände derselbe Strom.

$$I = I_1 = I_2 = \dots = I_n.$$

:::formel
$$R_\text{ges} = \sum_{\nu=1}^{n} R_\nu = R_1 + R_2 + \dots + R_n.$$
:::

**So liest man das:** Eingabe sind die Einzelwiderstände, Ausgabe der __Ersatzwiderstand__ der Kette. Er ist größer als jeder einzelne. Jeder Widerstand
trägt die Teilspannung $R_\nu\,I$; die Teilspannungen addieren sich zur Gesamtspannung. Bei $n$ gleichen Widerständen $R$ ist der Ersatzwiderstand
$n\,R$.

**Im Bild:** Bretter hintereinander sind ein langes Brett. Seine Länge ist die Summe der Längen, sein Widerstand die Summe der Widerstände.

:::herleitung
**Schritt 1: derselbe Strom.** An den Verbindungspunkten zwischen zwei Widerständen zweigt nichts ab. Die Knotenregel an jedem dieser Punkte sagt: Der
Strom, der hineinfließt, fließt weiter. Das ist der Schaltungszwang.

**Schritt 2: Spannungen addieren sich.** Die Masche aus der Gesamtspannung und allen Teilspannungen ergibt mit der Maschenregel und dem Ohmschen Gesetz:

$$U = U_1 + U_2 + \dots + U_n = R_1\,I + R_2\,I + \dots + R_n\,I = (R_1 + R_2 + \dots + R_n)\,I.$$

**Schritt 3: vergleichen.** Ein einzelner Widerstand $R_\text{ges}$ zwischen denselben Klemmen hätte $U=R_\text{ges}\,I$. Er verhält sich genau dann wie die
Kette, wenn $R_\text{ges}$ die Summe ist.
:::

::::beispiel Drei Widerstände an 12 Volt
Drei Widerstände mit $100\,\Omega$, $220\,\Omega$ und $680\,\Omega$ hängen hintereinander an $12\,\text{V}$:

$$R_\text{ges} = 100\,\Omega + 220\,\Omega + 680\,\Omega = 1000\,\Omega, \qquad I = \frac{12\,\text{V}}{1000\,\Omega} = 12\,\text{mA}.$$

Die Teilspannungen sind Widerstand mal derselbe Strom:

$$U_1 = 1{,}2\,\text{V}, \qquad U_2 = 2{,}64\,\text{V}, \qquad U_3 = 8{,}16\,\text{V},$$

zusammen wieder $12\,\text{V}$. Am größten Widerstand fällt die größte Spannung ab.

**Im Bild:** Drei Bretter von $100$, $220$ und $680$ Längeneinheiten hintereinander: Das längste nimmt den größten Teil der Höhe auf.
::::

## Der Spannungsteiler

Eine Reihe aus zwei Widerständen, deren Mittelpunkt man abgreift, heißt __Spannungsteiler__. Er macht aus einer Spannung eine kleinere. Im Skript
(Bild 5.34) liegen $R_1$ oben und $R_2$ unten an $U$; abgegriffen wird $U_2$ über $R_2$, und am Abgriff fließt kein Strom ab, der Laststrom $I_L$ ist null.

:::formel
$$\frac{U_\nu}{U} = \frac{R_\nu}{\sum_{i=1}^{n} R_i}, \qquad \frac{U_2}{U} = \frac{R_2}{R_1 + R_2}, \qquad \frac{U_1}{U_2} = \frac{R_1}{R_2}.$$
:::

**So liest man das:** Jede Teilspannung ist der Anteil der Gesamtspannung, den ihr Widerstand am Gesamtwiderstand hat; zwei Teilspannungen stehen im
Verhältnis ihrer Widerstände. Eingabe sind die Widerstände und die Gesamtspannung, Ausgabe die Teilspannung. Wichtig, wie das Skript betont: Die Regel
gilt nur für den __unbelasteten__ Spannungsteiler, durch dessen Widerstände derselbe Strom fließt. Was bei Belastung passiert, zeigt der letzte
Abschnitt.

**Im Bild:** Die Naht zwischen zwei hintereinanderliegenden Brettern liegt so hoch, wie es dem Anteil des unteren Bretts an der Gesamtlänge entspricht.

:::herleitung
Durch alle Widerstände fließt derselbe Strom, nach der Reihenschaltung

$$I = \frac{U}{R_1 + R_2 + \dots + R_n}.$$

Die Teilspannung am Widerstand $R_\nu$ ist nach Ohm $R_\nu\,I$; eingesetzt und durch $U$ geteilt folgt die erste Form, mit $n$ gleich $2$ die zweite. Im
Verhältnis zweier Teilspannungen kürzt sich der gemeinsame Strom heraus:

$$\frac{U_1}{U_2} = \frac{R_1\,I}{R_2\,I} = \frac{R_1}{R_2}.$$

Die Voraussetzung steckt im ersten Schritt: Derselbe Strom fließt nur, wenn am Abgriff nichts abfließt.
:::

::::beispiel Von 12 auf rund 3,3 Volt
Ein Messeingang verträgt höchstens $3{,}3\,\text{V}$, die Quelle hat $12\,\text{V}$. Nötig ist ein Teilerverhältnis von

$$\frac{U_2}{U} = \frac{3{,}3\,\text{V}}{12\,\text{V}} = 0{,}275, \qquad \frac{R_1}{R_2} = \frac{1 - 0{,}275}{0{,}275} \approx 2{,}64.$$

Mit Normwerten der E24-Reihe, $R_1$ gleich $27\,\text{k}\Omega$ und $R_2$ gleich $10\,\text{k}\Omega$:

$$U_2 = 12\,\text{V}\cdot\frac{10\,\text{k}\Omega}{27\,\text{k}\Omega + 10\,\text{k}\Omega} \approx 3{,}24\,\text{V}, \qquad \frac{U_1}{U_2} = \frac{27}{10}.$$

Etwas unter der Grenze, wie gewünscht. Der Querstrom durch beide Widerstände ist dabei nur $12\,\text{V}$ durch $37\,\text{k}\Omega$, rund $0{,}32\,\text{mA}$.

**Im Bild:** Ein langes Brett aus zwei Stücken im Längenverhältnis $27$ zu $10$; die Naht liegt bei gut einem Viertel der Höhe.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/06-spannungsteiler · Vorlage: spannungsteiler
Das Schaltbild nach Bild 5.34 des Skripts mit eigenen Werten: oben eine Klemme mit $U=12\,\text{V}$ gegen die untere Schiene, darunter $R_1=27\,\text{k}\Omega$
und $R_2=10\,\text{k}\Omega$ in Reihe; der Strompfeil $I$ in die Kette, $I_1$ und $I_2$ nach unten, am Abgriff ein Pfeil $I_L=0$ zur offenen Ausgangsklemme;
Spannungspfeile $U_1$ über $R_1$ und $U_2$ über $R_2$ nach unten. Ein Potenzialbalken neben der Kette fällt linear ab, an der Naht steht $3{,}24\,\text{V}$.
Regler für $R_1$ und $R_2$ verschieben die Naht. Kernaussage: Ohne Last teilt sich die Spannung im Verhältnis der Widerstände. (Rot = Ströme, blau =
Spannungen und Potenzialbalken, orange = Abgriff, grau = Bauteile.)
:::

## Widerstandsketten in Wandlern

Eine Kette aus vielen Widerständen ist ein Spannungsteiler mit vielen Abgriffen. Das Skript zeigt zwei Anwendungen.

**Digital-Analog-Wandler.** Ein __Digital-Analog-Wandler__ macht aus einer Zahl eine Spannung. Für drei Bit, also die Zahlen $0$ bis $7$, braucht man
acht Spannungsstufen in gleichen Abständen. Die Kette in Bild 5.36 besteht aus $R/2$ unten, sieben gleichen Widerständen $R$ und $R/2$ oben, zusammen
$8\,R$, zwischen der Referenzspannung $U_\text{ref}$ und Masse. Die Abgriffe liegen dann bei

$$U_Z = \Big(Z + \frac{1}{2}\Big)\,\frac{U_\text{ref}}{8}, \qquad Z \in \{0, 1, \dots, 7\}.$$

Die halben Widerstände an den Enden setzen jede Stufe in die Mitte ihres Intervalls: Die Zahl $0$ bekommt nicht $0\,\text{V}$, sondern eine halbe Stufe.
Ein Baum aus Schaltern, gesteuert von den drei Bits, verbindet genau einen Abgriff mit dem Ausgang (Bild 5.37). Dort sitzt ein __Puffer__, ein
Verstärker, der die Spannung übernimmt, ohne selbst Strom zu ziehen — sonst wäre der Teiler belastet.

:::herleitung
Durch die ganze Kette fließt derselbe Strom $U_\text{ref}/(8R)$. Vom unteren Ende bis zum Abgriff $Z$ liegen $R/2$ und $Z$ ganze Widerstände, zusammen
$(Z+\tfrac12)\,R$. Nach der Spannungsteilerregel ist die Spannung dort dieser Anteil an $8R$, mal $U_\text{ref}$.
:::

**Flash-Analog-Digital-Wandler.** Umgekehrt macht ein __Analog-Digital-Wandler__ aus einer Spannung eine Zahl. Der __Flash-Wandler__ in Bild 5.39 nutzt
dieselbe Kette als Satz von __Schwellen__: An jedem Abgriff vergleicht ein __Komparator__ die Eingangsspannung mit der Abgriffspannung und meldet „darüber"
oder „darunter". Je höher die Eingangsspannung, desto mehr Komparatoren melden „darüber", von unten nach oben wie die Quecksilbersäule eines
Thermometers; ein Decoder zählt sie und gibt die Zahl binär aus. Alle Vergleiche laufen gleichzeitig, daher der Name.

Für drei Bit genügen sieben Schwellen, denn acht Zahlen haben sieben Grenzen. Bild 5.39 zeichnet acht Komparatoren an den Abgriffen
$\tfrac{1}{16}\,U_\text{ref}$ bis $\tfrac{15}{16}\,U_\text{ref}$; der oberste meldet dann, dass die Eingangsspannung über dem Messbereich liegt.

::::beispiel Ein 3-Bit-Wandler mit 4 Volt Referenz
Mit $U_\text{ref}$ gleich $4\,\text{V}$ ist eine Stufe ein Achtel davon:

$$\frac{U_\text{ref}}{8} = 0{,}5\,\text{V}, \qquad U_Z = (Z + 0{,}5)\cdot0{,}5\,\text{V}.$$

Die acht Abgriffe liegen bei $0{,}25$, $0{,}75$, $1{,}25$, $1{,}75$, $2{,}25$, $2{,}75$, $3{,}25$ und $3{,}75\,\text{V}$. Die Zahl $5$ wird zu

$$U_5 = 5{,}5\cdot0{,}5\,\text{V} = 2{,}75\,\text{V}.$$

**Als Flash-Wandler** mit denselben Abgriffen als Schwellen: Eine Eingangsspannung von $2{,}9\,\text{V}$ liegt über den sechs unteren Schwellen
($0{,}25$ bis $2{,}75\,\text{V}$), also melden sechs Komparatoren „darüber", und der Decoder gibt $6$ aus, binär $110$. Das ist die nächstliegende Stufe,
denn $2{,}9\,\text{V}$ sind $5{,}8$ Stufen.

**Im Bild:** Eine Kette aus sieben gleich langen Brettstücken mit je einem halben oben und unten; an jeder Naht eine Höhenmarke.
::::

## Die Parallelschaltung

**Die Akteure:**

- $n$ Widerstände zwischen denselben zwei Knoten, mit den Leitwerten $G_\nu$, dem Kehrwert von $R_\nu$, in Siemens;
- die Teilspannungen $U_1, \dots, U_n$ über den einzelnen Widerständen und die Spannung $U$ zwischen den beiden Knoten;
- die Teilströme $I_1, \dots, I_n$ und der Gesamtstrom $I$, der in den oberen Knoten hineinfließt.

**Das Zusammenspiel:** *Welcher einzelne Widerstand nimmt bei derselben Spannung denselben Gesamtstrom auf?*

Der Schaltungszwang ist hier die gemeinsame Spannung:

$$U = U_1 = U_2 = \dots = U_n.$$

:::formel
$$G_\text{ges} = \sum_{\nu=1}^{n} G_\nu = \sum_{\nu=1}^{n} \frac{1}{R_\nu}, \qquad R_\text{ges} = \Big(\sum_{\nu=1}^{n} \frac{1}{R_\nu}\Big)^{-1}.$$
:::

**So liest man das:** Nebeneinander addieren sich die Leitwerte, der Ersatzwiderstand ist der Kehrwert der Summe. Er ist kleiner als der kleinste
Einzelwiderstand: Jeder weitere Zweig ist ein zusätzlicher Weg. Bei $n$ gleichen Widerständen $R$ ist er $R/n$. Für die Parallelschaltung schreibt man
kurz $R_1\parallel R_2$.

**Im Bild:** Bretter nebeneinander sind ein breites Brett. Seine Breite ist die Summe der Breiten, sein Leitwert die Summe der Leitwerte.

:::herleitung
**Schritt 1: dieselbe Spannung.** Je zwei parallele Widerstände bilden zusammen eine Masche zwischen denselben Knoten. Die Maschenregel sagt: Ihre
Spannungen, gleichsinnig von oben nach unten gezählt, sind gleich. Das ist der Schaltungszwang.

**Schritt 2: Ströme addieren sich.** Die Knotenregel am oberen Knoten und das Ohmsche Gesetz in der Form mit dem Leitwert ergeben:

$$I = I_1 + I_2 + \dots + I_n = G_1\,U + G_2\,U + \dots + G_n\,U = (G_1 + G_2 + \dots + G_n)\,U.$$

**Schritt 3: vergleichen.** Ein einzelner Leitwert $G_\text{ges}$ zwischen denselben Knoten hätte $I=G_\text{ges}\,U$. Er verhält sich wie die
Parallelschaltung, wenn $G_\text{ges}$ die Summe ist; sein Widerstand ist der Kehrwert.

**Kleiner als der kleinste.** Die Summe der Leitwerte ist größer als jeder einzelne Leitwert, also ist ihr Kehrwert kleiner als jeder einzelne
Widerstand.
:::

**Zwei Widerstände.** Für zwei parallele Widerstände wird aus der Kehrwertsumme die Form „Produkt durch Summe" (Bild 5.41 des Skripts):

$$\frac{1}{R_\text{ges}} = \frac{1}{R_1} + \frac{1}{R_2}, \qquad R_\text{ges} = R_1 \parallel R_2 = \frac{R_1\,R_2}{R_1 + R_2}.$$

:::herleitung
Auf den Hauptnenner gebracht ist die Summe der Kehrwerte $\frac{R_2 + R_1}{R_1 R_2}$; ihr Kehrwert ist das Produkt durch die Summe. Der Wert ist kleiner als
$R_1$, denn er ist $R_1$ mal dem Bruch $\frac{R_2}{R_1+R_2}$, und der ist kleiner als eins; ebenso kleiner als $R_2$.
:::

**Gemischte Schaltungen.** Netze aus Reihen und Parallelen fasst man von innen nach außen zusammen. In Bild 5.42 des Skripts liegt $R_1$ parallel zu
einer Reihe aus $R_2$ und $R_3$: Erst wird die Reihe zu $R_2+R_3$, dann die Parallele zu $R_1\parallel(R_2+R_3)$. Das Zusammenfassen ist erlaubt, weil
jede Gruppe sich nach außen wie ihr Ersatzwiderstand verhält.

**Im Bild:** Ein Brett neben zwei hintereinanderliegenden: Zuerst setzt man die beiden zu einem langen zusammen, dann legt man es neben das erste.

::::beispiel Parallel und gemischt
**(a) Zwei Widerstände** mit $1\,\text{k}\Omega$ und $1{,}5\,\text{k}\Omega$ nebeneinander:

$$R_\text{ges} = \frac{1\,\text{k}\Omega\cdot1{,}5\,\text{k}\Omega}{1\,\text{k}\Omega + 1{,}5\,\text{k}\Omega} = 600\,\Omega,$$

kleiner als der kleinere der beiden.

**(b) Drei gleiche** mit je $330\,\Omega$ ergeben ein Drittel:

$$R_\text{ges} = \frac{330\,\Omega}{3} = 110\,\Omega.$$

**(c) Gemischt wie in Bild 5.42:** $R_1$ mit $1\,\text{k}\Omega$ parallel zu einer Reihe aus $R_2$ mit $470\,\Omega$ und $R_3$ mit $1\,\text{k}\Omega$:

$$R_2 + R_3 = 1470\,\Omega, \qquad R_\text{ges} = \frac{1000\,\Omega\cdot1470\,\Omega}{1000\,\Omega + 1470\,\Omega} \approx 595\,\Omega.$$

**Im Bild:** Zwei Bretter nebeneinander sind breiter und leiten besser als jedes für sich; drei gleiche nebeneinander leiten dreimal so gut.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/06-parallel · Vorlage: parallelschaltung
Das Schaltbild nach Bild 5.40 des Skripts: oben eine Klemme mit dem Strompfeil $I$ hinein, darunter drei parallele Widerstände $G_1$, $G_2$, $G_3$ zwischen
einer oberen und einer unteren Schiene, an jedem ein Spannungspfeil $U_\nu$ nach unten und ein Strompfeil $I_\nu$; links der Spannungspfeil $U$ über die
ganze Schaltung. Animierte Ladungen verzweigen sich am oberen Knoten, durch den Zweig mit dem größten Leitwert laufen die meisten; am unteren Knoten
vereinigen sie sich wieder. Ein Zähler zeigt $I$ als Summe der drei Teilströme. Daneben das Ersatzschaltbild mit $G_\text{ges}$. Kernaussage: Nebeneinander
liegt an allen dieselbe Spannung, und die Ströme und Leitwerte addieren sich. (Rot = Ströme, blau = Spannungen, orange = Ersatzleitwert, grau = Schienen und
Bauteile.)
:::

## Der Stromteiler

Wie die Reihenschaltung eine Spannung teilt, teilt die Parallelschaltung einen Strom (Bild 5.44 des Skripts). Weil an allen Zweigen dieselbe Spannung
liegt, bekommt jeder Zweig so viel Strom, wie es seinem Leitwert entspricht:

:::formel
$$\frac{I_\nu}{I} = \frac{G_\nu}{\sum_{i=1}^{n} G_i}, \qquad I_1 = I\,\frac{G_1}{G_1 + G_2} = I\,\frac{R_2}{R_1 + R_2}.$$
:::

**So liest man das:** Der Strom teilt sich im Verhältnis der Leitwerte. Mit Widerständen geschrieben steht bei zwei Zweigen „über Kreuz" der **andere**
Widerstand im Zähler: Durch den kleineren Widerstand fließt der größere Strom. Eingabe sind der Gesamtstrom und die Widerstände, Ausgabe der Teilstrom.

**Im Bild:** Zwei Bretter nebeneinander: Das breitere bekommt die meisten Kugeln.

:::herleitung
Die gemeinsame Spannung folgt aus dem Gesamtstrom und dem Ersatzleitwert; jeder Zweig führt nach Ohm seinen Leitwert mal diese Spannung:

$$U = \frac{I}{G_\text{ges}}, \qquad I_\nu = G_\nu\,U = I\,\frac{G_\nu}{G_\text{ges}}.$$

Für zwei Zweige schreibt man die Leitwerte als Kehrwerte und erweitert mit $R_1 R_2$:

$$\frac{G_1}{G_1 + G_2} = \frac{1/R_1}{1/R_1 + 1/R_2} = \frac{R_2}{R_2 + R_1}.$$
:::

::::beispiel Teilströme und ein Messbereich
**(a) Zwei Zweige.** $30\,\text{mA}$ fließen in eine Parallelschaltung aus $1\,\text{k}\Omega$ und $2\,\text{k}\Omega$:

$$I_1 = 30\,\text{mA}\cdot\frac{2\,\text{k}\Omega}{3\,\text{k}\Omega} = 20\,\text{mA}, \qquad I_2 = 30\,\text{mA}\cdot\frac{1\,\text{k}\Omega}{3\,\text{k}\Omega} = 10\,\text{mA}.$$

Der halb so große Widerstand führt den doppelten Strom.

**(b) Ein Nebenwiderstand.** Ein Messwerk mit $100\,\Omega$ Innenwiderstand zeigt bei $1\,\text{mA}$ Vollausschlag. Damit es bis $100\,\text{mA}$ misst,
legt man einen __Nebenwiderstand__ $R_\text{N}$ parallel, der den Rest übernimmt. Nach dem Stromteiler muss bei $100\,\text{mA}$ gerade $1\,\text{mA}$ durch
das Messwerk fließen:

$$1\,\text{mA} = 100\,\text{mA}\cdot\frac{R_\text{N}}{R_\text{N} + 100\,\Omega}, \qquad R_\text{N} = \frac{100\,\Omega\cdot1\,\text{mA}}{100\,\text{mA} - 1\,\text{mA}} \approx 1{,}01\,\Omega.$$

Wie solche Messgeräte genau gebaut werden, zeigt Kapitel 6.

**Im Bild:** Neben das schmale Brett des Messwerks legt man ein sehr breites; fast alle Kugeln nehmen den breiten Weg.
::::

**Ein Stromteiler als Wandler.** Der strombasierte Digital-Analog-Wandler in Bild 5.45 und 5.47 des Skripts nutzt ein __R-2R-Netzwerk__: Zwischen
aufeinanderfolgenden Knoten liegt jeweils ein Widerstand $R$, von jedem Knoten führt ein Zweig mit $2R$ zu einem Umschalter, und am Ende sitzt ein
Abschluss. Die Knoten sind von $6$ an der Referenzspannung bis $1$ nummeriert; im Text des Skripts steht versehentlich „Knoten 6 bis 5". Jeder Umschalter
legt seinen Zweig entweder an Masse oder an die Ausgangsleitung, die eine äußere Schaltung ebenfalls auf dem Potenzial der Masse hält. Die Zweigströme
hängen deshalb nicht von den Schalterstellungen ab — sie halbieren sich von Knoten zu Knoten:

$$I_\text{aus} = I_0\,\Big(b_5 + \frac{b_4}{2} + \frac{b_3}{4} + \frac{b_2}{8} + \frac{b_1}{16} + \frac{b_0}{32}\Big), \qquad I_0 = \frac{U_\text{ref}}{2R}.$$

Dabei sind $b_5$ bis $b_0$ die Bits der Zahl, $1$ für „Zweig auf den Ausgang", $0$ für „Zweig an Masse"; $b_5$ ist das höchstwertige Bit am Knoten $6$.

**Im Bild:** An jeder Naht der Kette zweigt ein Brett doppelter Länge ab; jede Naht liegt halb so hoch wie die vorige, und jedes abzweigende Brett führt
halb so viele Kugeln.

:::herleitung
**Von rechts aufrollen.** Hinter Knoten $1$ liegen ein Längswiderstand $R$ und der Abschluss $R$ in Reihe, zusammen $2R$; parallel dazu der Zweig $2R$
des Knotens. Von Knoten $2$ aus gesehen liegt dahinter also der Längswiderstand $R$ und dann

$$2R \parallel 2R = R.$$

Der Längswiderstand und dieses $R$ bilden zusammen wieder $2R$, parallel zum Zweig $2R$ von Knoten $2$, und so fort: An jedem Knoten sieht man nach rechts,
einschließlich seines eigenen Zweigs, den Widerstand $R$.

**Halbierung.** Zwischen zwei Nachbarknoten liegen deshalb der Längswiderstand $R$ und dahinter der Widerstand $R$ nach Masse, ein Spannungsteiler $1$ zu
$1$: Jeder Knoten hat das halbe Potenzial seines linken Nachbarn. Der Zweig $2R$ an einem Knoten mit dem Potenzial $\varphi$ führt den Strom $\varphi/(2R)$,
an Knoten $6$ also $U_\text{ref}/(2R)$, dann die Hälfte, ein Viertel und so weiter.

**Summe.** Die Ausgangsleitung sammelt die Ströme der Zweige, deren Schalter auf ihr stehen. Weil beide Schalterstellungen auf Massepotenzial liegen,
ändert ein Umschalten keinen Strom im Netzwerk, nur sein Ziel.
:::

::::beispiel Ein 6-Bit-Wandler mit R-2R-Netzwerk
Mit $U_\text{ref}$ gleich $5\,\text{V}$ und $R$ gleich $10\,\text{k}\Omega$ ist der Strom im Zweig des höchstwertigen Bits

$$I_0 = \frac{5\,\text{V}}{2\cdot10\,\text{k}\Omega} = 0{,}25\,\text{mA}.$$

Die Zahl $45$, binär $101101$, schaltet die Zweige mit den Gewichten $1$, $\tfrac14$, $\tfrac18$ und $\tfrac1{32}$ auf den Ausgang:

$$I_\text{aus} = 0{,}25\,\text{mA}\cdot\Big(1 + \frac14 + \frac18 + \frac1{32}\Big) = 0{,}25\,\text{mA}\cdot\frac{45}{32} \approx 0{,}352\,\text{mA}.$$

Jede Zahl ergibt so ein Vielfaches von $\frac{I_0}{32}$, rund $7{,}8\,\mu\text{A}$.

**Im Bild:** Sechs abzweigende Bretter mit $1$, $\tfrac12$, $\tfrac14$ … der Kugeln; die Zahl bestimmt, welche davon in den Sammelkanal münden.
::::

## Der belastete Spannungsteiler

Ein Spannungsteiler, aus dem niemand Strom entnimmt, kommt in Wirklichkeit kaum vor: Die geteilte Spannung soll ja eine weitere Stufe versorgen, und die
zieht Strom. Im Skript (Bild 5.43) liegt dazu ein __Lastwiderstand__ $R_L$ parallel zu $R_2$.

**Die Akteure:** die Teilerwiderstände $R_1$ und $R_2$, der Lastwiderstand $R_L$, die Spannung $U$ am Teiler, die Ausgangsspannung $U_2$ und der Laststrom
$I_L$.

**Das Zusammenspiel:** *Wie stark sinkt die Ausgangsspannung, wenn die Last Strom zieht?*

:::formel
$$\frac{U_2}{U} = \frac{R_2 \parallel R_L}{R_1 + R_2 \parallel R_L}, \qquad \frac{U_2}{U} = \frac{R_2\,R_L}{R_1\,(R_2 + R_L) + R_2\,R_L},$$

$$I_L = \frac{U_2}{R_L} = U\,\frac{R_2}{R_1\,(R_2 + R_L) + R_2\,R_L}.$$
:::

**So liest man das:** Die Last liegt parallel zum unteren Widerstand und macht ihn kleiner; der Teiler teilt jetzt zwischen $R_1$ und $R_2\parallel R_L$.
Je kleiner $R_L$, desto tiefer sinkt $U_2$. Ohne Last, für $R_L$ gegen unendlich, wird daraus der unbelastete Teiler. Im Skript fehlt in der Formel für
$I_L$ der Faktor $U$; ohne ihn hätte der Strom die Einheit eines Leitwerts.

**Im Bild:** An der Naht zwischen den beiden Brettern zweigt ein drittes ab. Kugeln laufen seitlich weg; damit oben mehr nachkommen, braucht das obere Brett
mehr Gefälle, und die Naht sinkt.

:::herleitung
**Zusammenfassen.** $R_2$ und $R_L$ liegen zwischen denselben Knoten, also parallel, mit dem Ersatzwiderstand $R_2\parallel R_L$. Mit $R_1$ bildet er
einen unbelasteten Teiler, und die Spannungsteilerregel gibt den ersten Ausdruck.

**Ausmultiplizieren.** Mit $R_2\parallel R_L$ als $\frac{R_2R_L}{R_2+R_L}$ und Erweitern mit $R_2+R_L$:

$$\frac{U_2}{U} = \frac{\frac{R_2R_L}{R_2+R_L}}{R_1 + \frac{R_2R_L}{R_2+R_L}} = \frac{R_2R_L}{R_1(R_2+R_L) + R_2R_L}.$$

**Laststrom.** Ohm an $R_L$ und $U_2$ aus der vorigen Zeile; $R_L$ kürzt sich.

**Last gleich $R_2$.** Dann ist $R_2\parallel R_L$ die Hälfte von $R_2$, und es folgt wie im Skript

$$\frac{U_2}{U} = \frac{R_2/2}{R_1 + R_2/2} = \frac{R_2}{2R_1 + R_2}.$$
:::

**Der Teiler als Quelle.** Die Formel lässt sich so umstellen, dass man auf einen Blick sieht, wie stark die Last stört. Mit der Leerlaufspannung
$U_{2,0}$, der Ausgangsspannung ohne Last:

$$U_2 = U_{2,0}\,\frac{R_L}{R_L + R_1 \parallel R_2}, \qquad U_{2,0} = U\,\frac{R_2}{R_1 + R_2}.$$

Der belastete Teiler verhält sich wie eine Quelle mit der Spannung $U_{2,0}$ und dem __Innenwiderstand__ $R_1\parallel R_2$, an die die Last angeschlossen
ist. Der relative Spannungsverlust ist

$$\frac{U_{2,0} - U_2}{U_{2,0}} = \frac{R_1 \parallel R_2}{R_L + R_1 \parallel R_2}.$$

Soll er unter einem Prozent bleiben, muss $R_L$ mindestens das 99-fache von $R_1\parallel R_2$ sein. Dieses Bild einer __Ersatzspannungsquelle__ baut
Kapitel 7 aus.

:::herleitung
Ausgangspunkt ist der ausmultiplizierte Bruch. Der Nenner wird nach $R_L$ sortiert und $R_1+R_2$ ausgeklammert:

$$R_1(R_2+R_L) + R_2R_L = R_1R_2 + (R_1+R_2)\,R_L = (R_1+R_2)\Big(R_L + \frac{R_1R_2}{R_1+R_2}\Big).$$

Der Bruch zerfällt damit in den unbelasteten Teiler mal einen zweiten Teiler aus $R_L$ und $R_1\parallel R_2$:

$$\frac{U_2}{U} = \frac{R_2}{R_1+R_2}\cdot\frac{R_L}{R_L + R_1\parallel R_2}.$$

Der relative Verlust ist eins minus der zweite Faktor.
:::

**Welcher Fehler?** Das Skript misst die Wirkung der Last am Verhältnis $U_2/U_1$ der beiden Teilspannungen und nennt dessen Abweichung vom unbelasteten Wert
$F$. Bei $R_L$ gleich dem Zehnfachen von $R_2$ und $R_1$ gleich $R_2$ sind das $9{,}1\,\%$. Die Ausgangsspannung $U_2$ selbst sinkt dabei weniger, nur um
$4{,}8\,\%$, denn wenn $U_2$ sinkt, steigt $U_1$ — das Verhältnis ändert sich doppelt.

::::beispiel Ein Teiler unter Last
Ein Teiler aus zwei gleichen Widerständen von $4{,}7\,\text{k}\Omega$ an $10\,\text{V}$ liefert ohne Last $5\,\text{V}$. Sein Innenwiderstand ist

$$R_1 \parallel R_2 = 2{,}35\,\text{k}\Omega, \qquad U_2 = 5\,\text{V}\cdot\frac{R_L}{R_L + 2{,}35\,\text{k}\Omega}.$$

Für drei Lasten:

| $R_L$ | $U_2$ | Verlust von $U_2$ | $F$ des Skripts | $I_L$ |
|---|---|---|---|---|
| $47\,\text{k}\Omega$ | $4{,}76\,\text{V}$ | $4{,}8\,\%$ | $9{,}1\,\%$ | $0{,}10\,\text{mA}$ |
| $4{,}7\,\text{k}\Omega$ | $3{,}33\,\text{V}$ | $33\,\%$ | $50\,\%$ | $0{,}71\,\text{mA}$ |
| $470\,\Omega$ | $0{,}83\,\text{V}$ | $83\,\%$ | $91\,\%$ | $1{,}77\,\text{mA}$ |

Die erste Zeile mit der vollen Formel nachgerechnet:

$$\frac{U_2}{U} = \frac{4{,}7\cdot47}{4{,}7\cdot(4{,}7+47) + 4{,}7\cdot47} = \frac{220{,}9}{463{,}9} \approx 0{,}476, \qquad U_2 \approx 4{,}76\,\text{V}.$$

Nur die Last mit dem Zehnfachen von $R_2$ lässt die Spannung halbwegs stehen. Wer genauer sein will, nimmt kleinere Teilerwiderstände (mit mehr Querstrom)
oder einen Puffer wie im Digital-Analog-Wandler.

**Im Bild:** Ein dünnes Seitenbrett lässt die Naht kaum sinken, ein breites zieht so viele Kugeln ab, dass sie fast auf den Boden fällt.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/06-belasteter-teiler · Vorlage: teiler-mit-last
Das Schaltbild nach Bild 5.43 des Skripts: $U=10\,\text{V}$, $R_1=R_2=4{,}7\,\text{k}\Omega$, am Abgriff ein Lastwiderstand $R_L$ parallel zu $R_2$, mit den
Strompfeilen $I$, $I_1$, $I_2$, $I_L$ und den Spannungspfeilen $U_1$, $U_2$. Ein logarithmischer Regler für $R_L$ von $100\,\Omega$ bis $1\,\text{M}\Omega$; ein
Spannungsmesser zeigt $U_2$, daneben eine Kurve $U_2$ über $R_L$, die von fast null auf $5\,\text{V}$ ansteigt, mit markiertem Knick bei
$R_L=R_1\parallel R_2$. Ein Umschalter blendet die Ersatzquelle ein: $U_{2,0}=5\,\text{V}$ mit Innenwiderstand $2{,}35\,\text{k}\Omega$, an der dieselbe Last
dieselbe Spannung erzeugt. Kernaussage: Eine Last senkt die Teilerspannung wie eine Quelle mit Innenwiderstand $R_1\parallel R_2$. (Rot = Ströme, blau =
Spannungen und Kurve, orange = Last und Ersatzquelle, grau = Bauteile.)
:::

## Bedeutung und Ausblick

Mit Reihen- und Parallelschaltung, Spannungs- und Stromteiler lassen sich viele Netze ohne großes Gleichungssystem berechnen: von innen nach außen
zusammenfassen, bis ein Widerstand übrig ist, dann mit Gesamtstrom und Teilerregeln wieder nach innen. Das Skript fasst Kapitel 5 so zusammen: Strom
ist bewegte Ladung, das Material bestimmt die Leitfähigkeit, ein Leiterstück hat den Widerstand $\frac{l}{\sigma A}$ mit $U=R\,I$, an Knoten und in
Maschen gelten die Kirchhoffschen Regeln, und hintereinander addieren sich Widerstände, nebeneinander Leitwerte.

Kapitel 6 wendet das sofort an: Ein Strommesser wird mit einem Nebenwiderstand erweitert, ein Spannungsmesser mit einem Vorwiderstand, und die
__Wheatstonesche Messbrücke__ vergleicht zwei Spannungsteiler. Kapitel 7 behandelt Netze, die sich nicht in Reihen und Parallelen zerlegen lassen, etwa
mit der Stern-Dreieck-Umwandlung, und baut das Bild des Teilers als Quelle mit Innenwiderstand zu den Ersatzquellen aus. Die Widerstandsketten der
Wandler begegnen einem in jedem Mikrocontroller wieder.

:::kern
- __Schaltungszwang__: In Reihe fließt überall derselbe Strom, parallel liegt überall dieselbe Spannung.
- __Reihenschaltung__: Die Widerstände addieren sich, $R_\text{ges}=\sum R_\nu$, größer als jeder einzelne.
- __Parallelschaltung__: Die Leitwerte addieren sich, $G_\text{ges}=\sum G_\nu$; der Ersatzwiderstand ist kleiner als der kleinste.
- Zwei parallele Widerstände: Produkt durch Summe, $R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$.
- __Spannungsteiler__: $\frac{U_\nu}{U}=\frac{R_\nu}{\sum R_i}$, gültig nur ohne Last.
- __Stromteiler__: Der Strom teilt sich wie die Leitwerte; bei zwei Zweigen steht der andere Widerstand im Zähler.
- Widerstandsketten liefern die Stufen von Digital-Analog- und Flash-Analog-Digital-Wandlern; das R-2R-Netzwerk halbiert den Strom von Knoten zu Knoten.
- __Belasteter Teiler__: Die Last liegt parallel zu $R_2$ und senkt $U_2$; der Teiler wirkt wie eine Quelle mit dem Innenwiderstand $R_1\parallel R_2$.
- Im Skript fehlt in der Formel für den Laststrom der Faktor $U$; sein Fehlermaß $F$ bezieht sich auf $U_2/U_1$, nicht auf $U_2$.
:::

:::quiz
F: Warum addieren sich Widerstände in Reihe?
A: An den Verbindungspunkten zweigt nichts ab, also fließt nach der Knotenregel durch alle derselbe Strom. Nach der Maschenregel addieren sich die Teilspannungen, mit Ohm ist das $(R_1+\dots+R_n)\,I$; ein Ersatzwiderstand verhält sich genauso, wenn er die Summe ist. Bei $100$, $220$ und $680\,\Omega$ an $12\,\text{V}$ fließen $12\,\text{mA}$, und am größten Widerstand fallen $8{,}16\,\text{V}$ ab.
F: Unter welcher Voraussetzung gilt die Spannungsteilerregel, und warum?
A: Nur wenn am Abgriff kein Strom abfließt. Dann fließt durch alle Widerstände derselbe Strom $\frac{U}{\sum R_i}$, und jede Teilspannung ist ihr Anteil $\frac{R_\nu}{\sum R_i}$ an $U$. Zieht eine Last Strom, ist die Voraussetzung verletzt.
F: Wie teilt man $12\,\text{V}$ auf rund $3{,}3\,\text{V}$ mit Normwerten?
A: Nötig ist ein Verhältnis $\frac{R_1}{R_2}$ von etwa $2{,}64$. Mit $27\,\text{k}\Omega$ und $10\,\text{k}\Omega$ aus der E24-Reihe ergibt sich $12\,\text{V}\cdot\frac{10}{37}\approx3{,}24\,\text{V}$, etwas unter der Grenze, bei rund $0{,}32\,\text{mA}$ Querstrom.
F: Warum sitzen in der Widerstandskette des 3-Bit-Digital-Analog-Wandlers halbe Widerstände an den Enden?
A: Die Kette aus $R/2$, sieben mal $R$ und $R/2$ hat zusammen $8R$; der Abgriff $Z$ liegt bei $(Z+\frac12)\,\frac{U_\text{ref}}{8}$, also in der Mitte jeder Stufe. Bei $4\,\text{V}$ Referenz sind das $0{,}25$ bis $3{,}75\,\text{V}$, die Zahl $5$ wird zu $2{,}75\,\text{V}$. Ein Puffer am Ausgang verhindert, dass die Last den Teiler verfälscht.
F: Wie arbeitet ein Flash-Analog-Digital-Wandler, und wie viele Komparatoren braucht er für drei Bit?
A: An jedem Abgriff der Kette vergleicht ein Komparator die Eingangsspannung mit der Schwelle; je höher die Spannung, desto mehr melden „darüber", und ein Decoder zählt sie. Acht Zahlen haben sieben Grenzen, also genügen sieben Komparatoren; Bild 5.39 zeigt acht, der oberste meldet die Bereichsüberschreitung. Bei $4\,\text{V}$ Referenz ergibt $2{,}9\,\text{V}$ die Zahl $6$.
F: Warum ist der Ersatzwiderstand einer Parallelschaltung kleiner als der kleinste Einzelwiderstand?
A: An allen Zweigen liegt dieselbe Spannung, und nach der Knotenregel addieren sich die Ströme: Die Leitwerte addieren sich. Die Summe ist größer als jeder einzelne Leitwert, ihr Kehrwert also kleiner als jeder einzelne Widerstand. $1\,\text{k}\Omega$ parallel zu $1{,}5\,\text{k}\Omega$ ergibt $600\,\Omega$.
F: Warum steht beim Stromteiler mit zwei Zweigen der andere Widerstand im Zähler?
A: Der Strom teilt sich wie die Leitwerte, $I_1=I\,\frac{G_1}{G_1+G_2}$; mit Widerständen geschrieben und mit $R_1R_2$ erweitert wird daraus $I\,\frac{R_2}{R_1+R_2}$. Durch den kleineren Widerstand fließt der größere Strom: Von $30\,\text{mA}$ nimmt $1\,\text{k}\Omega$ neben $2\,\text{k}\Omega$ $20\,\text{mA}$.
F: Warum halbieren sich im R-2R-Netzwerk die Ströme von Knoten zu Knoten?
A: Von hinten aufgerollt sieht man an jedem Knoten nach rechts, einschließlich seines $2R$-Zweigs, den Widerstand $R$, denn $2R\parallel2R$ ist $R$. Zwischen zwei Knoten bilden der Längswiderstand $R$ und dieses $R$ einen Teiler $1$ zu $1$: Jeder Knoten hat das halbe Potenzial, jeder Zweig den halben Strom. Weil beide Schalterstellungen auf Massepotenzial liegen, ändern die Schalter nichts an den Strömen.
F: Was passiert beim belasteten Spannungsteiler, und wie sieht man es auf einen Blick?
A: Die Last liegt parallel zu $R_2$ und verkleinert den unteren Teilerwiderstand; $U_2$ sinkt. Umgestellt ist $U_2=U_{2,0}\,\frac{R_L}{R_L+R_1\parallel R_2}$: Der Teiler verhält sich wie eine Quelle mit der Leerlaufspannung $U_{2,0}$ und dem Innenwiderstand $R_1\parallel R_2$. Bei $2\times4{,}7\,\text{k}\Omega$ an $10\,\text{V}$ sinkt $U_2$ mit $47\,\text{k}\Omega$ Last von $5$ auf $4{,}76\,\text{V}$.
F: Welche zwei Ungenauigkeiten hat das Skript beim belasteten Teiler?
A: In der Formel für den Laststrom fehlt der Faktor $U$; richtig ist $I_L=U\,\frac{R_2}{R_1(R_2+R_L)+R_2R_L}$, sonst hätte der Strom die Einheit eines Leitwerts. Und sein Fehlermaß $F$ misst die Abweichung des Verhältnisses $U_2/U_1$; die Ausgangsspannung selbst sinkt weniger, bei $R_L$ gleich $10\,R_2$ um $4{,}8\,\%$ statt $9{,}1\,\%$.
:::
