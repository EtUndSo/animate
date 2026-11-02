---
title: Stufe 6: Punkte, Ebenen und Richtungen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallgitter
order: 4160800
summary: Kristalle spalten längs bestimmter Ebenen, und Ätzmittel greifen sie je nach Ebene verschieden schnell an.
tags: Netzebenen, Bragg-Gleichung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Kristalle spalten längs bestimmter Ebenen, und Ätzmittel greifen sie je nach Ebene verschieden schnell an. Diese Stufe gibt Orten, Ebenen und Richtungen Namen und rechnet mit ihnen.
:::

**Die Idee.** Eine Ebene schneidet die drei Achsen in drei Punkten. Man könnte diese Abschnitte nennen. Eine Ebene parallel zu einer Achse hätte dann aber den Abschnitt $\infty$. Nimmt man die Kehrwerte, wird aus $\infty$ eine 0, und die drei Zahlen sind die Faktoren in der Gleichung der Ebene. Im kubischen Kristall bilden sie zugleich den Pfeil senkrecht auf der Ebene (Abb. [6](#abb-6)).

**Punkte.** Man nimmt das kristalleigene System: Die Kantenvektoren $\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3$ der Elementarzelle haben die Längen $a$, $b$, $c$. Bei BCC und FCC sind das die Würfelkanten, nicht die primitiven Vektoren. Der Ursprung liegt meist in der unteren, hinteren, linken Ecke. Ein Punkt $\xi_1\boldsymbol e_1+\xi_2\boldsymbol e_2+\xi_3\boldsymbol e_3$ wird $\xi_1\,\xi_2\,\xi_3$ oder $((\xi_1\,\xi_2\,\xi_3))$ geschrieben. Die Zellmitte ist $\frac12\,\frac12\,\frac12$, die Mitte der Fläche mit $\xi_2=0$ ist $\frac12\,0\,\frac12$.

:::definition Definition 6.1 (Millersche Indizes)
<span class="anker" id="satz-6-1"></span>

__Netzebenen__ sind parallele Ebenen in regelmäßigem Abstand, die durch gleiche Gitterpunkte gehen. Ihre Indizes $(hkl)$ entstehen in vier Schritten:

<ol>

<li>

Bestimme die Schnittpunkte der Ebene mit den drei Achsen in Einheiten von $a$, $b$, $c$. Eine Ebene durch den Ursprung verschiebt man vorher parallel. Parallel zu einer Achse heißt Schnittpunkt $\infty$.

</li>

<li>

Kürze gemeinsame Faktoren.

</li>

<li>

Bilde die Kehrwerte.

</li>

<li>

Multipliziere mit dem kleinsten gemeinsamen Vielfachen der Nenner. Es entstehen drei ganze, teilerfremde Zahlen.

</li>

</ol>

Ein negativer Wert erhält einen Querstrich: $\bar1$. $(hkl)$ bezeichnet eine bestimmte Ebenenschar, $\{hkl\}$ alle symmetrisch gleichwertigen.
:::

⁠**So liest man das:** $h$, $k$, $l$ sind hier ganze Zahlen, nicht Planck-Konstante und Wellenzahl. Die Schar enthält alle Ebenen

<span class="anker" id="gl-6-1"></span>
$$h\,\xi_1+k\,\xi_2+l\,\xi_3=g,\qquad g\ \text{ganz}. \tag{6.1}$$

Die Ebene $g=1$ schneidet die Achsen bei $1/h$, $1/k$, $1/l$. Daher kommen die Kehrwerte. Im kubischen Kristall sind die sechs Würfelflächen gleichwertig: $\{100\}$ steht für $(100)$, $(010)$, $(001)$, $(\bar100)$, $(0\bar10)$, $(00\bar1)$.

:::abbildung gemb1/k6miller 6
Ebenen in der Würfelzelle, Ursprung in der hinteren unteren Ecke. Rot die Richtung mit denselben Indizes. (200) schneidet die $x$-Achse bei $\frac12$, (102) hat die Schnittpunkte $1,\infty,\frac12$, (210) die Schnittpunkte $1,2,\infty$.
:::

**Beispiel.** Die Schnittpunkte $4,2,3$ ergeben die Kehrwerte $\frac14,\frac12,\frac13$ und mal 12 die Ebene $(364)$. Aus $2,\infty,1$ wird $\frac12,0,1$, also $(102)$. Aus $1,-2,\infty$ wird $(2\bar10)$. Aus $2,4,2$ wird nach dem Kürzen $1,2,1$, also $(212)$. Die Schreibweise $(200)$ durchbricht die Regel „teilerfremd“ mit Absicht. Sie meint die Ebene mit dem Schnittpunkt $\frac12$, also eine Schar mit gleicher Stellung wie $(100)$ und halbem Abstand. Im SC-Gitter liegen auf den Zwischenebenen keine Atome, im FCC-Gitter dagegen schon.

:::definition Definition 6.2 (Richtungen)
<span class="anker" id="satz-6-2"></span>

Die Richtung eines Vektors $\boldsymbol r=u\,\boldsymbol e_1+v\,\boldsymbol e_2+w\,\boldsymbol e_3$ wird mit dem kleinsten ganzzahligen Tripel in eckigen Klammern geschrieben: $[uvw]$. $\langle uvw\rangle$ bezeichnet alle gleichwertigen Richtungen.
:::

⁠**So liest man das:** $[111]$ ist eine Raumdiagonale, $[110]$ eine Flächendiagonale, $[\bar100]$ die negative $a$-Achse. Der Vektor zum Punkt $\frac12\,\frac12\,1$ ist die Richtung $[112]$. Es gilt also: runde Klammern für Ebenen, eckige für Richtungen, geschweifte und spitze für alle gleichwertigen, doppelte runde oder keine für Punkte.

:::satz Satz 6.3 (Kubischer Kristall)
<span class="anker" id="satz-6-3"></span>

Die Richtung $[hkl]$ steht senkrecht auf der Ebene $(hkl)$. Der Abstand benachbarter Ebenen einer Schar und der Winkel zwischen zwei Ebenen sind

<span class="anker" id="gl-6-2"></span>
$$d_{hkl}=\frac{a}{\sqrt{h^2+k^2+l^2}},\qquad \cos\phi=\frac{h_1h_2+k_1k_2+l_1l_2}{\sqrt{h_1^2+k_1^2+l_1^2}\,\sqrt{h_2^2+k_2^2+l_2^2}}. \tag{6.2}$$
:::

:::herleitung Normale und Abstand
Im kubischen Kristall ist $\xi_i=x_i/a$ mit kartesischen $x_i$. Aus [(6.1)](#gl-6-1) wird $h\,x_1+k\,x_2+l\,x_3=g\,a$. Das ist die Ebene mit dem Normalenvektor $(h,k,l)$ im Abstand $g\,a/\sqrt{h^2+k^2+l^2}$ vom Ursprung. Der Schritt von $g$ zu $g+1$ ergibt $d_{hkl}$. Der Winkel zweier Ebenen ist der Winkel ihrer Normalen.

Anders ist es, wenn die Achsen schief oder verschieden lang sind: Die Normale der Ebene $(101)$ im tetragonalen Kristall ist $(1/a,0,1/c)$, die Richtung $[101]$ aber $(a,0,c)$. Bei $c=1{,}5\,a$ schließen beide 22,6° ein.
:::

**Anwendung.** Bestimmte Laugen ätzen Silizium auf $\{111\}$-Flächen sehr langsam. In einer $(100)$-Scheibe entstehen so Gräben mit Flanken aus $\{111\}$-Ebenen. Der Winkel folgt aus [(6.2)](#gl-6-2): $\cos\phi=1/\sqrt3$, also $\phi=54{,}7°$. Der Kristall selbst legt die Form bis in den Nanometerbereich fest. **Grenzfall:** $(hkl)$ und $(\bar h\bar k\bar l)$ sind dieselbe Schar, denn in [(6.1)](#gl-6-1) ändert sich nur das Vorzeichen von $g$, und [(6.2)](#gl-6-2) gibt denselben Abstand.

:::frage Warum nimmt man bei BCC und FCC nicht die primitiven Vektoren als Achsen?
Dann wären die Achsen schief, und der Satz oben fiele weg. Die Indizes beschreiben die Geometrie des Würfels. Ob auf einer Ebene Atome liegen, sagt erst die Besetzung: Bei BCC liegen die $(100)$-Netzebenen wegen der Zellmitten im Abstand $a/2$.
:::

:::aufgabe Aufgabe 7 ★ Ebenen benennen
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Bestimme $(hkl)$ für die Schnittpunkte $2,3,6$ und $3,3,1$ und $-1,2,\frac12$ und $2,-2,1$.

</li>

<li>

Eine Ebene geht durch die Punkte $1\,1\,0$, $1\,0\,1$ und $0\,1\,1$. Welche Indizes hat sie, und welches $g$ in [(6.1)](#gl-6-1)?

</li>

<li>

Eine Ebene enthält den Ursprung, $1\,1\,0$ und $0\,0\,1$. Verschiebe sie und bestimme $(hkl)$.

</li>

</ol>

:::loesung
(a) $2,3,6$: Kehrwerte $\frac12,\frac13,\frac16$, mal 6: $(321)$. $\ 3,3,1$: $\frac13,\frac13,1$, mal 3: $(113)$. $\ -1,2,\frac12$: $-1,\frac12,2$, mal 2: $(\bar214)$. $\ 2,-2,1$: $\frac12,-\frac12,1$, mal 2: $(1\bar12)$. (b) Alle drei Punkte erfüllen $\xi_1+\xi_2+\xi_3=2$. Das ist $(111)$ mit $g=2$, die Schnittpunkte sind $2,2,2$. (c) Die Ebene erfüllt $\xi_1-\xi_2=0$, sie ist parallel zur dritten Achse. Verschoben auf $\xi_1-\xi_2=1$ hat sie die Schnittpunkte $1,-1,\infty$, also $(1\bar10)$.
:::
:::

:::aufgabe Aufgabe 8 ★★ Richtungen im Würfel
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Welchen Punkt der Würfelzelle erreichst du vom Ursprung aus längs $[210]$ am Zellrand? Längs $[112]$?

</li>

<li>

Wie heißt die Richtung von $1\,0\,0$ nach $0\,1\,1$?

</li>

<li>

Zeige, dass die Richtung $[1\bar10]$ in der Ebene $(111)$ liegt.

</li>

<li>

Berechne die Winkel zwischen $(100)$ und $(110)$ sowie zwischen $(111)$ und $(1\bar11)$.

</li>

</ol>

:::loesung
(a) $[210]$ trifft den Rand bei $1\,\frac12\,0$, $[112]$ bei $\frac12\,\frac12\,1$. (b) Der Vektor ist $(-1,1,1)$, also $[\bar111]$. (c) $[1\bar10]$ steht senkrecht auf der Normalen $[111]$, denn $1\cdot1-1\cdot1+0\cdot1=0$. Also liegt die Richtung in der Ebene. (d) $\cos\phi=1/\sqrt2$ ergibt 45°. $\cos\phi=(1-1+1)/3=\frac13$ ergibt 70,5°.
:::
:::

:::aufgabe Aufgabe 9 ★★★ Netzebenenabstände
<span class="anker" id="aufg-9"></span>

Polonium ist SC mit $a=0{,}335$ nm. Röntgenwellen mit $\lambda=0{,}0709$ nm werden an Netzebenen verstärkt reflektiert, wenn der Umweg $2d_{hkl}\sin\theta$ der Welle von der tieferen Ebene ein Vielfaches von $\lambda$ ist: $2d_{hkl}\sin\theta=q\lambda$ mit der Ordnung $q=1,2,\dots$ (__Bragg-Gleichung__). So misst man Gitterkonstanten.

<ol class="al">

<li>

Berechne $d_{100}$, $d_{110}$ und $d_{111}$ und die Winkel $\theta$ der ersten Ordnung. In welcher Reihenfolge erscheinen sie?

</li>

<li>

Unter welchem Winkel liegt die zweite Ordnung an $(100)$? Warum bezeichnet man sie als $(200)$-Reflex, obwohl die Zwischenebenen im SC-Gitter leer sind?

</li>

</ol>

:::loesung
(a) $d_{100}=0{,}335$ nm, $d_{110}=0{,}237$ nm, $d_{111}=0{,}193$ nm. Aus $\sin\theta=\lambda/(2d)$ folgen $\theta=6{,}07°$, 8,61° und 10,56°. Großer Abstand heißt kleiner Winkel. (b) $\sin\theta=2\lambda/(2a)=0{,}212$, also $\theta=12{,}2°$. $2a\sin\theta=2\lambda$ lässt sich als $2(a/2)\sin\theta=\lambda$ lesen, wie die erste Ordnung an Ebenen im Abstand $a/2$. Der Reflex entsteht aber an den vorhandenen $(100)$-Ebenen.
:::
:::
