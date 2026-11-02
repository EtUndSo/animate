---
title: Stufe 6: Leistungsanpassung
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170700
summary: Die Tabelle zeigt ein Maximum von P L .
tags: Kurzschlussleistung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Tabelle zeigt ein Maximum von $P_\mathrm{L}$. Diese Stufe findet es und erklärt, warum es genau bei $R_\mathrm{L}=R_\mathrm{i}$ liegt.
:::

**Die Idee.** Zwei Einflüsse arbeiten gegeneinander. Bei kleinem $R_\mathrm{L}$ kommen viele Coulomb, aber fast ihre ganze Energie bleibt in $R_\mathrm{i}$. Bei großem $R_\mathrm{L}$ gibt jedes Coulomb fast alles in der Last ab, aber es kommen wenige. Die Gerade $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ aus [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) macht das sichtbar: $P_\mathrm{L}=U_\mathrm{L}I$ ist die Fläche des Rechtecks unter ihr (Abb. [7](#abb-7)). Am größten ist es, wenn seine Ecke in der Mitte der Geraden liegt, bei halbem Strom und halber Spannung. Dann fällt an $R_\mathrm{i}$ und $R_\mathrm{L}$ dieselbe Spannung bei demselben Strom ab, also sind beide Widerstände gleich.

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

**Beispiel.** Für $R_\mathrm{L}=2\,\Omega$ sind $I=2{,}25$ A, $U_\mathrm{L}=4{,}5$ V und $P_\mathrm{L}=10{,}125$ W, das ist ein Viertel von $P_\mathrm{KS}=40{,}5$ W. Die Lasten 0,5 $\Omega$ und 8 $\Omega$ ergeben beide 6,48 W. Allgemein liefern $\alpha$ und $1/\alpha$ dieselbe Leistung, denn sie tauschen $x$ und $1-x$. **Grenzfälle:** Für $\alpha\to0$ ist der Strom fest und $P_\mathrm{L}\approx P_\mathrm{KS}\,\alpha$. Für $\alpha\to\infty$ ist die Spannung fest und $P_\mathrm{L}\approx P_\mathrm{KS}/\alpha$.

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
