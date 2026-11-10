---
title: Stufe 6: Hohe und mittlere Temperaturen
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung
knoten: Kapitel 11: Eigenhalbleiter und Dotierung
order: 4210800
summary: Die Neutralität hat keine geschlossene Lösung.
tags: Eigenleitung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Neutralität hat keine geschlossene Lösung. Diese Stufe zeigt die drei Bereiche der exakten Kurve und löst die Gleichung für den Fall, dass alle Donatoren ionisiert sind.
:::

**Die Idee.** Abb. [6](#abb-6) zeigt die numerische Lösung. Bei hohen Temperaturen übertrifft die Paarbildung die feste Zahl der Donatoren, das Stück verhält sich wie ein reiner Kristall: Das ist die __Eigenleitung__, Bereich I. Bei mittleren Temperaturen sind alle Donatoren ionisiert, und Paare sind noch selten: $n$ bleibt stehen. Das ist die Störstellenerschöpfung, Bereich II, auch Sättigungsbereich genannt. Bei tiefen Temperaturen hält ein Teil der Donatoren sein Elektron fest, das ist die Störstellenreserve, Bereich III. In den Bereichen I und II liegt $E_\mathrm F$ weit unter $E_\mathrm D$, also $N_\mathrm D^+=N_\mathrm D$. Dann gibt es nur noch $n$ und $p$ mit zwei Gleichungen, und die Rechnung ist geschlossen möglich.

:::abbildung gemb1/k11bereiche 6
Silizium mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ und $\Delta E_\mathrm D=45$ meV, numerische Lösung von $p+N_\mathrm D^+-n=0$. Oben: $n$ über $1000/T$ mit den Bereichen I (rot), II (grün), III (blau); gestrichelt $n_\mathrm i$ und, orange, die Gerade des Bereichs III. Unten: $E_\mathrm F$ auf derselben Achse. Die Grenzen liegen bei 719 K und 95 K.
:::

:::satz Satz 6.1 (Voll ionisierte Donatoren)
<span class="anker" id="satz-6-1"></span>

Aus $n-p=N_\mathrm D$ und $n\,p=n_\mathrm i^2$ folgt

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
$$\begin{aligned} n&=\frac{N_\mathrm D}2+\sqrt{\frac{N_\mathrm D^2}4+n_\mathrm i^2},\qquad p=\frac{n_\mathrm i^2}n, \\ E_\mathrm F&=\underbrace{\frac12(E_\mathrm V+E_\mathrm C)+\frac34k_\mathrm BT\ln\frac{m_\mathrm V^*}{m_\mathrm C^*}}_{E_\mathrm{Fi}}+\underbrace{k_\mathrm BT\,\operatorname{arcsinh}\frac{N_\mathrm D}{2n_\mathrm i}}_{\text{Beitrag der Donatoren}}. \end{aligned} \tag{6.1|6.2}$$

Für p-Typ stehen $N_\mathrm A$ statt $N_\mathrm D$ und $p$ statt $n$, und im Argument steht $-N_\mathrm A$: $E_\mathrm F$ liegt unter $E_\mathrm{Fi}$.
:::

:::herleitung Quadratische Gleichung für $\exp(-E_\mathrm F/(k_\mathrm BT))$
Mit [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) lautet die Neutralität $N_\mathrm V\mathrm{e}^{-(E_\mathrm F-E_\mathrm V)/(k_\mathrm BT)}+N_\mathrm D-N_\mathrm C\mathrm{e}^{-(E_\mathrm C-E_\mathrm F)/(k_\mathrm BT)}=0$. Multipliziert man mit $\frac1{N_\mathrm V}\mathrm{e}^{-(E_\mathrm V+E_\mathrm F)/(k_\mathrm BT)}$, entsteht für $u=\mathrm{e}^{-E_\mathrm F/(k_\mathrm BT)}$

$$u^2+\frac{N_\mathrm D}{N_\mathrm V}\,\mathrm{e}^{-E_\mathrm V/(k_\mathrm BT)}\,u-\frac{N_\mathrm C}{N_\mathrm V}\,\mathrm{e}^{-(E_\mathrm C+E_\mathrm V)/(k_\mathrm BT)}=0.$$

Mit $-2c$ als Faktor bei $u$ und $-d^2$ als letztem Glied ist $u=c\pm\sqrt{c^2+d^2}$, und nur das Plus ist positiv. Mit $\ln(c+\sqrt{c^2+d^2})=\ln d+\operatorname{arcsinh}(c/d)$ folgt $-E_\mathrm F/(k_\mathrm BT)=\ln d+\operatorname{arcsinh}(c/d)$. Es ist $c/d=-N_\mathrm D/(2n_\mathrm i)$ und $-k_\mathrm BT\ln d=\frac12(E_\mathrm C+E_\mathrm V)+\frac12k_\mathrm BT\ln(N_\mathrm V/N_\mathrm C)$. Das ist [(6.2)](#gl-6-2).

⁠**Kürzer:** Aus [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) und [(2.1)](der-reine-kristall.html#gl-2-1) folgt $n=n_\mathrm i\mathrm{e}^{x}$ und $p=n_\mathrm i\mathrm{e}^{-x}$ mit $x=(E_\mathrm F-E_\mathrm{Fi})/(k_\mathrm BT)$. Dann ist $n-p=2n_\mathrm i\sinh x=N_\mathrm D$. Für $n$ selbst ergibt $p=n_\mathrm i^2/n$ die Gleichung $n^2-N_\mathrm Dn-n_\mathrm i^2=0$.
:::

**Die beiden Grenzfälle.** Für $N_\mathrm D\ll2n_\mathrm i$ ist $\operatorname{arcsinh}y\approx y$ klein. Das ist die Eigenleitung: $n\approx p\approx n_\mathrm i$ und $E_\mathrm F\approx E_\mathrm{Fi}$, mit der Steigung $-E_\mathrm g/(2k_\mathrm B)$ wie in [(2.3)](der-reine-kristall.html#gl-2-3). Für $N_\mathrm D\gg2n_\mathrm i$ ist $\operatorname{arcsinh}y\approx\ln(2y)$. Das ist die Erschöpfung:

<span class="anker" id="gl-6-3"></span>
$$n=N_\mathrm D,\qquad p=\frac{n_\mathrm i^2}{N_\mathrm D}\propto\mathrm{e}^{-E_\mathrm g/(k_\mathrm BT)},\qquad E_\mathrm F=E_\mathrm{Fi}+k_\mathrm BT\ln\frac{N_\mathrm D}{n_\mathrm i}=E_\mathrm C-k_\mathrm BT\ln\frac{N_\mathrm C}{N_\mathrm D}. \tag{6.3}$$

Für Akzeptoren gilt entsprechend $p=N_\mathrm A$, $n=n_\mathrm i^2/N_\mathrm A$ und $E_\mathrm F=E_\mathrm V+k_\mathrm BT\ln(N_\mathrm V/N_\mathrm A)$.

⁠**So liest man das:** Die Mehrheit hängt nicht von $T$ ab, deshalb arbeiten Bauelemente in diesem Bereich. Die Minderheit folgt $n_\mathrm i^2$ und hängt stark von $T$ ab. Auf der logarithmischen Achse liegt $p$ so weit unter $n_\mathrm i$, wie $n$ darüber liegt. $E_\mathrm F$ sinkt mit steigendem $T$: Der Ausläufer von $f$ wird breiter und die Zahl $N_\mathrm C$ größer, also muss $E_\mathrm F$ vom Band abrücken, damit $n$ gleich bleibt. **Gültigkeit:** $E_\mathrm D-E_\mathrm F>3k_\mathrm BT$ und thermisches Gleichgewicht.

::::beispiel
Bei 300 K ist $n=10^{16}\,\mathrm{cm^{-3}}$, $p=7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$ und $E_\mathrm C-E_\mathrm F=205$ meV. $E_\mathrm F$ liegt 360 meV über $E_\mathrm{Fi}$, beide Abstände ergeben zusammen rund die 566 meV von $E_\mathrm C$ bis $E_\mathrm{Fi}$. Bei 310 K wächst $p$ um den Faktor 4,5, $n$ gar nicht. Bei 719 K ist $n_\mathrm i=N_\mathrm D$, dort sind $n=1{,}62\,N_\mathrm D$ und $p=0{,}62\,N_\mathrm D$, bei 800 K schon $n=3{,}5\cdot10^{16}\,\mathrm{cm^{-3}}$.
::::

:::frage Gilt $n\,p=n_\mathrm i^2$ immer? Was ändert die Dotierung daran?
Die Dotierung ändert nichts: Sie verschiebt $n$ und $p$ gegenläufig, das Produkt bleibt. Es gilt aber nur im thermischen Gleichgewicht. Licht passender Wellenlänge oder eine angelegte Spannung bringen zusätzliche Paare oder entfernen sie, dann ist $n\,p\ne n_\mathrm i^2$. Außerdem setzt es die Boltzmann-Näherung voraus.
:::

:::aufgabe Aufgabe 7 ★ Erschöpfung prüfen
<span class="anker" id="aufg-7"></span>

Si mit Phosphor, $N_\mathrm D=2\cdot10^{17}\,\mathrm{cm^{-3}}$, $T=250$ K.

<ol class="al">

<li>

Berechne $N_\mathrm C$, $n_\mathrm i$ und $E_\mathrm C-E_\mathrm F$ nach [(6.3)](#gl-6-3).

</li>

<li>

Wie viel Prozent der Donatoren sind damit ionisiert? Rechne mit diesem $n$ einmal neu.

</li>

<li>

Wie groß ist $p$? Vorhersage: Rückt $E_\mathrm F$ bei 400 K zur Bandkante oder weg? Prüfe es.

</li>

</ol>

:::loesung
(a) $N_\mathrm C=2{,}14\cdot10^{19}\,\mathrm{cm^{-3}}$, $n_\mathrm i=8{,}9\cdot10^{7}\,\mathrm{cm^{-3}}$, $k_\mathrm BT=21{,}54$ meV, $E_\mathrm C-E_\mathrm F=100{,}7$ meV. (b) $E_\mathrm D-E_\mathrm F=55{,}7$ meV $=2{,}59\,k_\mathrm BT$, also 87 % ionisiert. Mit $n=0{,}87\,N_\mathrm D$ folgen 103,7 meV und 88 %. Numerisch: $n=1{,}77\cdot10^{17}\,\mathrm{cm^{-3}}$, 103,4 meV. (c) $p=n_\mathrm i^2/n=0{,}045\,\mathrm{cm^{-3}}$, praktisch kein Loch. $E_\mathrm F$ rückt ab: Bei 400 K ist $E_\mathrm C-E_\mathrm F=185$ meV.
:::
:::

:::aufgabe Aufgabe 8 ★★ Dotierung gegen Eigenleitung
<span class="anker" id="aufg-8"></span>

Germanium (Tabelle aus Stufe [2](der-reine-kristall.html#stufe-2)) mit $N_\mathrm A=10^{15}\,\mathrm{cm^{-3}}$ bei 400 K, alle Akzeptoren ionisiert.

<ol class="al">

<li>

Berechne $n_\mathrm i$, $p$ und $n$. Prüfe die Neutralität.

</li>

<li>

Wie groß wäre der Fehler mit $p=N_\mathrm A$?

</li>

<li>

Wo liegt $E_\mathrm F$ relativ zu $E_\mathrm{Fi}$?

</li>

<li>

Welches $N_\mathrm A$ ergibt bei dieser Temperatur $p=2n$?

</li>

</ol>

:::loesung
(a) $n_\mathrm i=7{,}3\cdot10^{14}\,\mathrm{cm^{-3}}$, $p=\frac12N_\mathrm A+\sqrt{\frac14N_\mathrm A^2+n_\mathrm i^2}=1{,}39\cdot10^{15}\,\mathrm{cm^{-3}}$, $n=n_\mathrm i^2/p=3{,}9\cdot10^{14}\,\mathrm{cm^{-3}}$. Probe: $p-n=10^{15}\,\mathrm{cm^{-3}}$. (b) 28 % zu wenig. (c) $E_\mathrm F-E_\mathrm{Fi}=-34{,}47\,\mathrm{meV}\cdot\operatorname{arcsinh}0{,}684=-22{,}0$ meV. (d) Mit $p=\sqrt2\,n_\mathrm i$ und $n=n_\mathrm i/\sqrt2$ ist $N_\mathrm A=p-n=5{,}2\cdot10^{14}\,\mathrm{cm^{-3}}$.
:::
:::
