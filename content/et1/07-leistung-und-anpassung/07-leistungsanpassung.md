---
title: Stufe 6: Leistungsanpassung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Leistung, Anpassung und Wirkungsgrad
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Kapitel 7: Leistung, Anpassung und Wirkungsgrad
order: 1170700
summary: Die Tabelle zeigt ein Maximum von P L .
tags: Kurzschlussleistung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Tabelle zeigt ein Maximum von $P_\mathrm{L}$. Diese Stufe findet es und erklärt, warum es genau bei $R_\mathrm{L}=R_\mathrm{i}$ liegt.
:::

**Die Idee.** Zwei Einflüsse arbeiten gegeneinander. Bei kleinem $R_\mathrm{L}$ kommen viele Coulomb, aber fast ihre ganze Energie bleibt in $R_\mathrm{i}$. Bei großem $R_\mathrm{L}$ gibt jedes Coulomb fast alles in der Last ab, aber es kommen wenige. Die Gerade $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ aus [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) macht das sichtbar: $P_\mathrm{L}=U_\mathrm{L}I$ ist die Fläche des Rechtecks unter ihr (Abb. [7](#abb-7)). Am größten ist es, wenn seine Ecke in der Mitte der Geraden liegt, bei halbem Strom und halber Spannung. Dann fällt an $R_\mathrm{i}$ und $R_\mathrm{L}$ dieselbe Spannung bei demselben Strom ab, also sind beide Widerstände gleich.

:::abbildung et1/k7rechteck 7
Quellengerade der Batterie mit drei Arbeitspunkten. Blau: $P_\mathrm{L}$, Rechteck aus $I$ und $U_\mathrm{L}$. Rot: $P_\mathrm{v}$, Rechteck aus $I$ und $U_\mathrm{Ri}$. Beide zusammen sind $P_\mathrm{q}=U_\mathrm{q}I$. Die mittlere Ecke ergibt das größte blaue Rechteck.
:::

:::satz Satz 6.1 (Leistungsanpassung)
<span class="anker" id="satz-6-1"></span>

Mit $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$ ist die Leistung an der Last

<span class="anker" id="gl-6-1"></span>
$$P_\mathrm{L}(R_\mathrm{L})=\left(\frac{U_\mathrm{q}}{R_\mathrm{i}+R_\mathrm{L}}\right)^{\!2}R_\mathrm{L}=U_\mathrm{q}^2\,\frac{R_\mathrm{L}}{\bigl(R_\mathrm{i}(1+R_\mathrm{L}/R_\mathrm{i})\bigr)^2}=P_\mathrm{KS}\,\frac{\alpha}{(1+\alpha)^2}, \tag{6.1}$$

mit $\alpha=R_\mathrm{L}/R_\mathrm{i}$ und $P_\mathrm{KS}=U_\mathrm{q}^2/R_\mathrm{i}$. Sie ist am größten für

<span class="anker" id="gl-6-2"></span>
$$R_\mathrm{L}=R_\mathrm{i},\qquad P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{KS}}{4},\qquad I=\frac{I_\mathrm{KS}}{2},\qquad U_\mathrm{L}=\frac{U_\mathrm{q}}{2}. \tag{6.2}$$
:::

⁠**So liest man das:** $P_\mathrm{KS}=U_\mathrm{q}I_\mathrm{KS}$ ist die __Kurzschlussleistung__, die Leistung der Quelle bei $R_\mathrm{L}=0$. Sie landet ganz in $R_\mathrm{i}$, und mehr als ein Viertel davon erreicht keine Last. **Gültigkeit:** Die Quelle steht fest, nur $R_\mathrm{L}$ wird gewählt. Bei einer Ersatzquelle steht $U_\mathrm{LL}$ für $U_\mathrm{q}$.

:::herleitung Das Maximum, auf drei Wegen
Nach der Quotientenregel, $\bigl(f/g\bigr)'=(f'g-f\,g')/g^2$, mit $f=\alpha$ und $g=(1+\alpha)^2$ ist

$$\frac{\mathrm{d} P_\mathrm{L}}{\mathrm{d}\alpha}=P_\mathrm{KS}\,\frac{(1+\alpha)^2-2\alpha(1+\alpha)}{(1+\alpha)^4}=P_\mathrm{KS}\,\frac{1-\alpha}{(1+\alpha)^3}.$$

Die Ableitung ist null bei $\alpha=1$, davor positiv, danach negativ. Das ist das Maximum.

Ohne Ableitung: Mit $x=I/I_\mathrm{KS}$ ist $P_\mathrm{L}=P_\mathrm{KS}\,x(1-x)$. Diese Parabel hat die Nullstellen 0 und 1, ihr Maximum $\frac14$ liegt also bei $x=\frac12$.

Als Mechanismus: Ein Stromzuwachs $\mathrm{d} I$ bringt $U_\mathrm{q}\mathrm{d} I$ aus der Quelle, die Verluste wachsen um $2R_\mathrm{i}I\,\mathrm{d} I$. Bei $I=I_\mathrm{KS}/2$ frisst der Verlust den Zuwachs: 9 V gegen $2\cdot2\,\Omega\cdot2{,}25\,\mathrm{A}=9$ V.
:::

::::beispiel
Für $R_\mathrm{L}=2\,\Omega$ sind $I=2{,}25$ A, $U_\mathrm{L}=4{,}5$ V und $P_\mathrm{L}=10{,}125$ W, das ist ein Viertel von $P_\mathrm{KS}=40{,}5$ W. Die Lasten 0,5 $\Omega$ und 8 $\Omega$ ergeben beide 6,48 W. Allgemein liefern $\alpha$ und $1/\alpha$ dieselbe Leistung, denn sie tauschen $x$ und $1-x$.
::::

⁠**Grenzfälle:** Für $\alpha\to0$ ist der Strom fest und $P_\mathrm{L}\approx P_\mathrm{KS}\,\alpha$. Für $\alpha\to\infty$ ist die Spannung fest und $P_\mathrm{L}\approx P_\mathrm{KS}/\alpha$.

:::ltspice Parabel und Gerade
⁠**Zeichnen:** `voltage` mit 9 von `q` nach Masse, `res` mit 2 von `q` nach `a`. Als Last eine Stromquelle `current` namens `I1` von `a` nach Masse.

⁠**Direktiven:** `.dc I1 0 4.5 0.01` und `.meas dc Pmax MAX V(a)*I(I1)`

⁠**Was du siehst:** Trage `V(a)*I(I1)` auf: eine Parabel mit dem Maximum 10,125 W bei 2,25 A. `V(a)/9` ist der Wirkungsgrad, eine fallende Gerade, die dort 0,5 erreicht. Bei 3,6 A und 0,9 A stehen je 6,48 W. Für Aufgabe [6](#aufg-6) trägst du 12 und 4 ein und lässt bis 3 A laufen: 9 W bei 1,5 A, je 8 W bei 1 A und 2 A.
:::

:::frage Ich habe eine feste Last. Soll ich die Quelle so wählen, dass $R_\mathrm{i}=R_\mathrm{L}$ ist?
Nein. Der Satz gilt für eine feste Quelle und eine wählbare Last. Ist die Last fest und $R_\mathrm{i}$ wählbar, ist $R_\mathrm{i}=0$ am besten, denn $U_\mathrm{q}^2R_\mathrm{L}/(R_\mathrm{i}+R_\mathrm{L})^2$ fällt mit $R_\mathrm{i}$. Die 16-$\Omega$-Last bekommt mit $R_\mathrm{i}=2\,\Omega$ dann 4 W, mit $R_\mathrm{i}=0$ dagegen 5,06 W.
:::

:::aufgabe Aufgabe 6 ★★ Lautsprecher am Verstärker
<span class="anker" id="aufg-6"></span>

Ein Verstärkerausgang wirkt wie $U_\mathrm{q}=12$ V und $R_\mathrm{i}=4\,\Omega$. (a) Welcher Lautsprecher holt die größte Leistung heraus, und wie groß ist sie? (b) Was ergibt 8 $\Omega$? Vergleiche Leistung und Wirkungsgrad. (c) Welche zweite Last liefert dieselbe Leistung wie 8 $\Omega$? (d) ★★★ Beweise mit [(6.1)](#gl-6-1), dass $\alpha$ und $1/\alpha$ stets dieselbe Leistung ergeben.

:::loesung
(a) $R_\mathrm{L}=4\,\Omega$, $P_\mathrm{L,max}=144\,\mathrm{V^2}/16\,\Omega=9$ W bei $\eta=50$ %. (b) $I=1$ A, $P_\mathrm{L}=8$ W, $\eta=\frac23$. Es gehen nur 11 % Leistung verloren, und die Verluste sinken von 9 W auf 4 W. (c) $\alpha=2$ gehört zu $\alpha=\frac12$, also $R_\mathrm{L}=2\,\Omega$: 8 W, aber nur $\eta=\frac13$.

(d) $\dfrac{1/\alpha}{(1+1/\alpha)^2}=\dfrac{1/\alpha}{(\alpha+1)^2/\alpha^2}=\dfrac{\alpha}{(1+\alpha)^2}$.
:::
:::

::::formelsammlung
**Leistung an der Last**

$$P_\mathrm{L}(R_\mathrm{L})=\left(\frac{U_\mathrm{q}}{R_\mathrm{i}+R_\mathrm{L}}\right)^{\!2}R_\mathrm{L}=U_\mathrm{q}^2\,\frac{R_\mathrm{L}}{\bigl(R_\mathrm{i}(1+R_\mathrm{L}/R_\mathrm{i})\bigr)^2}=P_\mathrm{KS}\,\frac{\alpha}{(1+\alpha)^2}$$

$\alpha=R_\mathrm{L}/R_\mathrm{i}$. Die Quelle steht fest, nur $R_\mathrm{L}$ wird gewählt. $\alpha$ und $1/\alpha$ liefern dieselbe Leistung. Grenzfälle: Für $\alpha\to0$ ist der Strom fest und $P_\mathrm{L}\approx P_\mathrm{KS}\,\alpha$, für $\alpha\to\infty$ ist die Spannung fest und $P_\mathrm{L}\approx P_\mathrm{KS}/\alpha$.

**Kurzschlussleistung**

$$P_\mathrm{KS}=U_\mathrm{q}I_\mathrm{KS},\qquad P_\mathrm{KS}=U_\mathrm{q}^2/R_\mathrm{i}$$

Leistung der Quelle bei $R_\mathrm{L}=0$; sie landet ganz in $R_\mathrm{i}$.

**Leistungsanpassung**

$$R_\mathrm{L}=R_\mathrm{i},\qquad P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{KS}}{4},\qquad I=\frac{I_\mathrm{KS}}{2},\qquad U_\mathrm{L}=\frac{U_\mathrm{q}}{2}$$

Größte Leistung, die eine feste Quelle an eine wählbare Last abgibt. Bei einer Ersatzquelle steht $U_\mathrm{LL}$ für $U_\mathrm{q}$. Ist dagegen die Last fest und $R_\mathrm{i}$ wählbar, ist $R_\mathrm{i}=0$ am besten.

**Ableitung der Lastleistung**

$$\frac{\mathrm{d} P_\mathrm{L}}{\mathrm{d}\alpha}=P_\mathrm{KS}\,\frac{1-\alpha}{(1+\alpha)^3}$$

Null bei $\alpha=1$, davor positiv, danach negativ: Dort liegt das Maximum.

**Lastleistung über dem Strom**

$$P_\mathrm{L}=P_\mathrm{KS}\,x(1-x)$$

$x=I/I_\mathrm{KS}$. Parabel mit den Nullstellen 0 und 1, Maximum $\frac14$ bei $x=\frac12$.

**Gleiche Leistung für Kehrwerte**

$$\dfrac{1/\alpha}{(1+1/\alpha)^2}=\dfrac{\alpha}{(1+\alpha)^2}$$

Die Lasten $\alpha$ und $1/\alpha$ vertauschen $x$ und $1-x$; an der Batterie ergeben 0,5 $\Omega$ und 8 $\Omega$ beide 6,48 W.
::::

::::lernkarten
:::karte begriff Leistungsanpassung
Was versteht man unter Leistungsanpassung einer Last an eine Quelle mit Innenwiderstand $R_\mathrm{i}$?
---
Die Wahl der Last $R_\mathrm{L}=R_\mathrm{i}$, bei der eine feste Quelle die größte Leistung an die Last abgibt. Dann teilt sich die Energie jeder Ladung zu gleichen Teilen auf Quelle und Last.
--- falsch
Die Wahl der Quelle mit $R_\mathrm{i}=R_\mathrm{L}$ zu einer festen Last, bei der diese die größte Leistung erhält. Dann gibt die Quelle ihre gesamte Energie ohne Verlust an die Last ab.
--- falsch
Die Wahl einer sehr großen Last $R_\mathrm{L}\gg R_\mathrm{i}$, bei der die Quelle die größte Leistung abgibt, weil dann fast die ganze Quellenspannung an der Last liegt.
--- falsch
Die Wahl der Last $R_\mathrm{L}=R_\mathrm{i}$, bei der der Wirkungsgrad am größten ist. Dann geht nur ein kleiner Teil der Energie jeder Ladung in der Quelle verloren.
:::
:::karte begriff Kurzschlussleistung
Was ist die Kurzschlussleistung einer Quelle mit Innenwiderstand, und wo wird sie umgesetzt?
---
Die Leistung der Quelle bei $R_\mathrm{L}=0$, $P_\mathrm{KS}=U_\mathrm{q}I_\mathrm{KS}$, also $P_\mathrm{KS}=U_\mathrm{q}^2/R_\mathrm{i}$. Sie landet ganz in $R_\mathrm{i}$; keine Last kann mehr als ein Viertel davon erhalten.
--- falsch
Die größte Leistung, die eine Last an der Quelle erhalten kann, $P_\mathrm{KS}=U_\mathrm{q}I_\mathrm{KS}$. Sie wird im Kurzschluss vollständig im Kurzschlussbügel umgesetzt.
--- falsch
Die Leistung der Quelle bei offenen Klemmen, $P_\mathrm{KS}=U_\mathrm{q}^2/R_\mathrm{i}$. Sie wird nirgends umgesetzt, weil im Leerlauf kein Strom fließt und nur Spannung anliegt.
--- falsch
Die Leistung der Quelle bei $R_\mathrm{L}=0$, $P_\mathrm{KS}=U_\mathrm{q}I_\mathrm{KS}/2$. Sie teilt sich zu gleichen Teilen auf den Innenwiderstand und den Kurzschlussbügel auf.
:::
:::karte formel Leistung an der Last
Wie hängt die Leistung an der Last von $R_\mathrm{L}$ und vom Verhältnis $\alpha=R_\mathrm{L}/R_\mathrm{i}$ ab, wenn die Quelle fest ist?
---
$P_\mathrm{L}(R_\mathrm{L})=\left(\frac{U_\mathrm{q}}{R_\mathrm{i}+R_\mathrm{L}}\right)^{\!2}R_\mathrm{L}$, normiert $P_\mathrm{KS}\,\frac{\alpha}{(1+\alpha)^2}$ mit $P_\mathrm{KS}=U_\mathrm{q}^2/R_\mathrm{i}$. Der Strom ist $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$.
--- falsch
$P_\mathrm{L}(R_\mathrm{L})=\frac{U_\mathrm{q}^2}{R_\mathrm{i}+R_\mathrm{L}}$, normiert $P_\mathrm{KS}\,\frac{1}{1+\alpha}$. Die Leistung an der Last fällt deshalb mit wachsendem $R_\mathrm{L}$ stetig ab.
--- falsch
$P_\mathrm{L}(R_\mathrm{L})=\left(\frac{U_\mathrm{q}}{R_\mathrm{i}+R_\mathrm{L}}\right)^{\!2}R_\mathrm{i}$, normiert $P_\mathrm{KS}\,\frac{1}{(1+\alpha)^2}$. Die Leistung an der Last ist im Kurzschluss am größten.
--- falsch
$P_\mathrm{L}(R_\mathrm{L})=\frac{U_\mathrm{q}^2}{R_\mathrm{L}}$, normiert $P_\mathrm{KS}/\alpha$. Sie hängt nicht vom Innenwiderstand ab, weil an der Last stets die volle Quellenspannung liegt.
:::
:::karte formel Werte bei Leistungsanpassung
Welche Werte haben Lastleistung, Strom und Lastspannung, wenn eine feste Quelle mit der Last $R_\mathrm{L}=R_\mathrm{i}$ betrieben wird?
---
$P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{KS}}{4}$, $I=\frac{I_\mathrm{KS}}{2}$ und $U_\mathrm{L}=\frac{U_\mathrm{q}}{2}$. Bei einer Ersatzquelle steht $U_\mathrm{LL}$ für $U_\mathrm{q}$.
--- falsch
$P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{2\,R_\mathrm{i}}=\frac{P_\mathrm{KS}}{2}$, $I=\frac{I_\mathrm{KS}}{2}$ und $U_\mathrm{L}=\frac{U_\mathrm{q}}{2}$. Die Hälfte der Kurzschlussleistung erreicht die Last.
--- falsch
$P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{KS}}{4}$, $I=I_\mathrm{KS}$ und $U_\mathrm{L}=\frac{U_\mathrm{q}}{4}$. Es fließt der volle Kurzschlussstrom, weil die Last klein ist.
--- falsch
$P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{R_\mathrm{i}}=P_\mathrm{KS}$, $I=I_\mathrm{KS}$ und $U_\mathrm{L}=U_\mathrm{q}$. Bei Anpassung kommt die ganze Kurzschlussleistung an der Last an.
:::
:::karte zusammenhang Zwei gegenläufige Einflüsse
Warum hat die Leistung an der Last ein Maximum, statt mit wachsendem $R_\mathrm{L}$ ständig zu steigen oder zu fallen?
---
Zwei Einflüsse arbeiten gegeneinander: Bei kleinem $R_\mathrm{L}$ kommen viele Coulomb, aber ihre Energie bleibt fast ganz in $R_\mathrm{i}$. Bei großem $R_\mathrm{L}$ gibt jedes fast alles in der Last ab, aber es kommen wenige.
--- falsch
Weil der Innenwiderstand mit dem Strom wächst. Bei kleinem $R_\mathrm{L}$ wird die Quelle heiß, $R_\mathrm{i}$ steigt und begrenzt den Strom; bei großem $R_\mathrm{L}$ bleibt sie kalt und liefert weniger.
--- falsch
Weil die Quelle bei einem bestimmten Strom ihre Nennleistung erreicht. Darüber regelt sie die Spannung herunter, darunter gibt sie ihre volle Leistung gar nicht erst ab, weil die Last zu wenig verlangt.
--- falsch
Weil die Lastspannung mit $R_\mathrm{L}$ zuerst steigt und dann wieder fällt. Bei kleinem und bei großem $R_\mathrm{L}$ liegt an der Last fast keine Spannung, dazwischen die volle.
:::
:::karte zusammenhang Rechteck unter der Quellengeraden
Warum liegt das Maximum der Lastleistung genau bei halbem Kurzschlussstrom und halber Quellenspannung?
---
$P_\mathrm{L}=U_\mathrm{L}I$ ist die Fläche des Rechtecks unter der Geraden $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$. Sie ist am größten, wenn seine Ecke in der Mitte der Geraden liegt; dann sind $R_\mathrm{i}$ und $R_\mathrm{L}$ gleich.
--- falsch
Weil Strom und Spannung an der Last in jedem Arbeitspunkt gleich groß sind, wenn man sie auf $I_\mathrm{KS}$ und $U_\mathrm{q}$ bezieht. Ihr Produkt ist deshalb in der Mitte am größten.
--- falsch
Weil die Quelle dort einen Wirkungsgrad von 100 % erreicht. Bei halbem Strom fällt am Innenwiderstand keine Spannung mehr ab, und die ganze Leistung geht an die Last.
--- falsch
$P_\mathrm{L}=U_\mathrm{L}I$ ist die Fläche des Rechtecks unter der Geraden $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$. Am größten ist sie am Rand, im Kurzschluss, weil dort der Strom und damit die Breite des Rechtecks am größten ist.
:::
:::karte zusammenhang Zuwachs und Verlust
Warum steigt die Lastleistung nicht weiter, wenn man den Strom über den halben Kurzschlussstrom hinaus erhöht?
---
Ein Stromzuwachs $\mathrm{d} I$ bringt $U_\mathrm{q}\mathrm{d} I$ aus der Quelle, die Verluste in $R_\mathrm{i}$ wachsen um $2R_\mathrm{i}I\,\mathrm{d} I$. Bei $I=I_\mathrm{KS}/2$ frisst der Verlust den Zuwachs, darüber übersteigt er ihn.
--- falsch
Weil die Quelle oberhalb des halben Kurzschlussstroms keine zusätzliche Leistung mehr abgibt. Ihre Leistung $P_\mathrm{q}$ bleibt ab dort konstant, während die Verluste weiter wachsen.
--- falsch
Ein Stromzuwachs $\mathrm{d} I$ bringt $U_\mathrm{q}\mathrm{d} I$ aus der Quelle, die Verluste wachsen nur um $R_\mathrm{i}I\,\mathrm{d} I$. Erst bei $I=I_\mathrm{KS}$ frisst der Verlust den Zuwachs, vorher steigt die Leistung.
--- falsch
Weil oberhalb des halben Kurzschlussstroms die Spannung an der Last negativ wird. Die Last gibt dann Energie an die Quelle zurück, statt welche aufzunehmen.
:::
:::karte zusammenhang Gleiche Leistung für zwei Lasten
Warum liefern die Lasten mit $\alpha$ und $1/\alpha$ an derselben Quelle dieselbe Leistung, etwa 0,5 $\Omega$ und 8 $\Omega$ an der Batterie mit 2 $\Omega$?
---
Weil sie den Strombruchteil $x=I/I_\mathrm{KS}$ und $1-x$ vertauschen, und $P_\mathrm{L}=P_\mathrm{KS}\,x(1-x)$ ändert sich dabei nicht. An der Batterie ergeben beide 6,48 W.
--- falsch
Weil beide Lasten gleich weit vom Innenwiderstand entfernt sind: Der Unterschied zu $R_\mathrm{i}$ ist bei 0,5 $\Omega$ und 8 $\Omega$ derselbe. An der Batterie ergeben beide 6,48 W.
--- falsch
Weil bei beiden Lasten derselbe Strom fließt: Die Quelle liefert unabhängig von der Last stets den halben Kurzschlussstrom. An der Batterie ergeben beide 6,48 W.
--- falsch
Weil bei beiden derselbe Wirkungsgrad vorliegt: Die Energie jeder Ladung teilt sich gleich auf Quelle und Last auf. An der Batterie ergeben beide 6,48 W.
:::
:::karte zusammenhang Feste Last, wählbare Quelle
Welcher Innenwiderstand liefert einer festen Last die größte Leistung, wenn man die Quelle frei wählen kann?
---
$R_\mathrm{i}=0$, denn $U_\mathrm{q}^2R_\mathrm{L}/(R_\mathrm{i}+R_\mathrm{L})^2$ fällt mit $R_\mathrm{i}$. Die Leistungsanpassung gilt nur für eine feste Quelle und eine wählbare Last; die 16-$\Omega$-Last bekommt mit $R_\mathrm{i}=0$ dann 5,06 W statt 4 W.
--- falsch
$R_\mathrm{i}=R_\mathrm{L}$, denn die Leistungsanpassung gilt in beide Richtungen: Ob man die Last an die Quelle oder die Quelle an die Last anpasst, das Maximum liegt immer bei gleichen Widerständen.
--- falsch
Ein möglichst großer Innenwiderstand, denn er begrenzt den Strom und schützt so die Last. Die Leistung an der Last ändert sich dabei kaum, weil sie im Wesentlichen nur von $U_\mathrm{q}$ abhängt.
--- falsch
$R_\mathrm{i}=R_\mathrm{L}/2$, denn dann liegen zwei Drittel der Quellenspannung an der Last. Die 16-$\Omega$-Last bekommt so mehr als mit $R_\mathrm{i}=0$, weil dort der Strom zu groß würde.
:::
:::karte formel Grenzfälle sehr kleiner und sehr großer Last
Wie verhält sich die Lastleistung an einer festen Quelle, wenn die Last sehr klein oder sehr groß gegen den Innenwiderstand ist?
---
Für $\alpha\to0$ ist der Strom fest und $P_\mathrm{L}\approx P_\mathrm{KS}\,\alpha$. Für $\alpha\to\infty$ ist die Spannung fest und $P_\mathrm{L}\approx P_\mathrm{KS}/\alpha$.
--- falsch
Für $\alpha\to0$ ist die Spannung fest und $P_\mathrm{L}\approx P_\mathrm{KS}/\alpha$. Für $\alpha\to\infty$ ist der Strom fest und $P_\mathrm{L}\approx P_\mathrm{KS}\,\alpha$.
--- falsch
Für $\alpha\to0$ und für $\alpha\to\infty$ geht $P_\mathrm{L}\approx P_\mathrm{KS}$, weil in beiden Fällen jeweils die ganze Leistung der Quelle an der Last ankommt.
--- falsch
Für $\alpha\to0$ ist der Strom fest und $P_\mathrm{L}\approx P_\mathrm{KS}\,\alpha^2$. Für $\alpha\to\infty$ ist die Spannung fest und $P_\mathrm{L}\approx P_\mathrm{KS}/\alpha^2$.
:::
:::karte herleitung Maximum über die Ableitung
Leite aus $P_\mathrm{L}=P_\mathrm{KS}\,\frac{\alpha}{(1+\alpha)^2}$ mit der Ableitung nach $\alpha$ her, dass die Lastleistung bei $R_\mathrm{L}=R_\mathrm{i}$ am größten ist.
---
Nach der Quotientenregel $\bigl(f/g\bigr)'=(f'g-f\,g')/g^2$ mit $f=\alpha$ und $g=(1+\alpha)^2$ ist $\frac{\mathrm{d} P_\mathrm{L}}{\mathrm{d}\alpha}=P_\mathrm{KS}\,\frac{(1+\alpha)^2-2\alpha(1+\alpha)}{(1+\alpha)^4}$, weil $f'=1$ und $g'=2(1+\alpha)$ sind.
---
Kürzen durch $(1+\alpha)$ ergibt $P_\mathrm{KS}\,\frac{1-\alpha}{(1+\alpha)^3}$, weil im Zähler $(1+\alpha)-2\alpha=1-\alpha$ übrig bleibt.
---
Die Ableitung ist null bei $\alpha=1$, weil dort der Zähler $1-\alpha$ verschwindet.
---
Davor ist sie positiv, danach negativ, weil der Nenner stets positiv ist; also ist $\alpha=1$, das heißt $R_\mathrm{L}=R_\mathrm{i}$, ein Maximum.
---
Eingesetzt folgt $P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{KS}}{4}$, weil $\frac{\alpha}{(1+\alpha)^2}$ bei $\alpha=1$ den Wert $\frac14$ hat.
:::
:::karte herleitung Maximum ohne Ableitung
Zeige ohne Ableitung, mit dem Strombruchteil $x=I/I_\mathrm{KS}$, dass die Lastleistung beim halben Kurzschlussstrom ihr Maximum $P_\mathrm{KS}/4$ hat.
---
Auf der Geraden $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ ist die Lastspannung der Bruchteil $1-x$ von $U_\mathrm{q}$, weil $R_\mathrm{i}I$ zu $U_\mathrm{q}$ im selben Verhältnis steht wie $I$ zu $I_\mathrm{KS}$.
---
Damit ist $P_\mathrm{L}=U_\mathrm{L}I=P_\mathrm{KS}\,x(1-x)$, weil $U_\mathrm{L}I$ der Bruchteil $(1-x)\,x$ von $U_\mathrm{q}I_\mathrm{KS}$ ist.
---
Diese Parabel hat die Nullstellen 0 und 1, weil bei $x=0$ kein Strom fließt und bei $x=1$ keine Spannung an der Last liegt.
---
Ihr Scheitel liegt in der Mitte zwischen den Nullstellen, also bei $x=\frac12$, weil die Parabel symmetrisch ist; dort hat $x(1-x)$ den Wert $\frac14$.
---
Also ist $P_\mathrm{L,max}=P_\mathrm{KS}/4$ bei $I=\frac{I_\mathrm{KS}}{2}$, weil $x=\frac12$ den halben Kurzschlussstrom bedeutet.
:::
::::
