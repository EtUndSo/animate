---
title: Stufe 4: Stetigkeit und Epsilon-Delta
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250600
summary: Der Grenzwert schaut an f(x 0) vorbei.
tags: stetig, rechtsseitig stetig, linksseitig stetig, stetig ergänzbar, stetige Ergänzung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Der Grenzwert schaut an $f(x_0)$ vorbei. Stetigkeit verlangt, dass beide übereinstimmen. Das Epsilon-Delta-Kriterium macht daraus einen Toleranztest ohne Folgen.
:::

**Die Idee.** Der Funktionswert soll das sein, was man von nahebei erwartet. Das ist die Aussage „kleine Änderung am Eingang, kleine Änderung am Ausgang“. Die drei Beispiele aus Abb. [3](grenzwerte-von-funktionen.html#abb-3) scheitern daran auf verschiedene Weise.

:::definition Definition 4.1 (Stetigkeit)
<span class="anker" id="satz-4-1"></span>

Sei $f:(a,b)\to\mathbb{R}$, $x_0\in(a,b)$. Dann heißt

<ol class="rm">

<li>

$f$ in $x_0$ __stetig__, falls $\lim\limits_{x\to x_0}f(x)=f(x_0)$,

</li>

<li>

$f$ in $x_0$ __rechtsseitig stetig__, falls $\lim\limits_{x\searrow x_0}f(x)=f(x_0)$,

</li>

<li>

$f$ in $x_0$ __linksseitig stetig__, falls $\lim\limits_{x\nearrow x_0}f(x)=f(x_0)$,

</li>

<li>

$f$ auf $(a,b)$ stetig, falls $f$ in jedem Punkt von $(a,b)$ stetig ist.

</li>

</ol>

$f:[a,b]\to\mathbb{R}$ heißt auf $[a,b]$ stetig, wenn $f$ auf $(a,b)$ stetig ist, in $a$ rechtsseitig und in $b$ linksseitig stetig; entsprechend für $[a,b)$ und $(a,b]$.
:::

⁠**So liest man das:** (i) enthält drei Forderungen: $f(x_0)$ ist erklärt, der Grenzwert existiert, beide sind gleich. Polynome sind nach [(3.3)](grenzwerte-von-funktionen.html#gl-3-3) überall stetig. $H$ ist bei 0 rechtsseitig stetig, nicht aber linksseitig: $\lim_{x\nearrow0}H(x)=0\ne1=H(0)$. **Grenzfall:** Konstante Funktionen sind überall stetig, jede Änderung am Ausgang ist 0.

:::satz Satz 4.2 ($\varepsilon$-$\delta$-Kriterium für Stetigkeit)
<span class="anker" id="satz-4-2"></span>

Sei $f:(a,b)\to\mathbb{R}$, $x_0\in(a,b)$. Dann ist $f$ genau dann in $x_0$ stetig, wenn gilt

<span class="anker" id="gl-4-1"></span>
$$\forall\,\varepsilon>0\ \ \exists\,\delta_0>0:\quad|f(x)-f(x_0)|<\varepsilon\quad\forall\,x\in(x_0-\delta_0,x_0+\delta_0). \tag{4.1}$$

Gleichbedeutend: $\forall\,\varepsilon>0\ \exists\,\delta_0>0$ mit $\bigl(x\in U_{\delta_0}(x_0)\Rightarrow f(x)\in U_\varepsilon(f(x_0))\bigr)$.
:::

⁠**So liest man das:** Es ist das Spiel aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html). Du gibst eine Toleranz $\varepsilon$ für den Ausgang vor, ich nenne $\delta_0$ für den Eingang. Ich gewinne, wenn alle Eingänge näher als $\delta_0$ an $x_0$ einen Ausgang näher als $\varepsilon$ an $f(x_0)$ erzeugen. $\delta_0=\delta_0(\varepsilon,x_0)$ darf von $\varepsilon$ und $x_0$ abhängen und muss so klein sein, dass $(x_0-\delta_0,x_0+\delta_0)\subset(a,b)$ gilt. Geometrisch bleibt das Graphenstück über dem $\delta_0$-Streifen im $\varepsilon$-Streifen (Abb. [4](#abb-4)).

:::beweis Beide Richtungen
„$\Leftarrow$“: Es gelte [(4.1)](#gl-4-1), und $\{x_n\}$ erfülle [(3.1)](grenzwerte-von-funktionen.html#gl-3-1). Sei $\varepsilon>0$ und $\delta_0$ wie in [(4.1)](#gl-4-1). Wegen $x_n\to x_0$ gibt es $N_0$ mit $|x_n-x_0|<\delta_0$ für alle $n>N_0$, also $|f(x_n)-f(x_0)|<\varepsilon$ für diese $n$. Das heißt $f(x_n)\to f(x_0)$.

„$\Rightarrow$“ indirekt: Gilt [(4.1)](#gl-4-1) nicht, gibt es $\varepsilon_1>0$ und zu jedem $\delta_0=\frac1n$ ein $x_n$ mit $|x_n-x_0|<\frac1n$ und $|f(x_n)-f(x_0)|\ge\varepsilon_1$. Dann ist $x_n\ne x_0$ und $x_n\to x_0$, aber $f(x_n)$ läuft nicht gegen $f(x_0)$.
:::

::::beispiel
$f(x)=x^2$ bei $x_0=2$. Es ist $|x^2-4|=|x-2|\,|x+2|$. Um den zweiten Faktor zu begrenzen, verlangt man zuerst $|x-2|<1$, dann ist $|x+2|<5$. Also ist $\delta_0:=\min\{1,\varepsilon/5\}$ eine Antwort: Für $|x-2|<\delta_0$ ist $|x^2-4|<5\,\delta_0\le\varepsilon$. Für $\varepsilon=0{,}5$ ist $\delta_0=0{,}1$, und tatsächlich liegt $x^2$ für $x\in(1{,}9;\ 2{,}1)$ zwischen $3{,}61$ und $4{,}41$. An einer Stelle $x_0>0$ gibt derselbe Weg $\delta_0=\min\{1,\varepsilon/(2x_0+1)\}$: Je steiler der Graph, desto kleiner $\delta_0$.
::::

⁠**Grenzfall:** Für $f(x)=|x|$ gewinnt bei $x_0=0$ die Antwort $\delta_0=\varepsilon$.

:::abbildung hm1/k5epsdelta 4
$x^2$ bei $x_0=2$, $\varepsilon=0{,}5$: Über dem Streifen $(1{,}9;\ 2{,}1)$ bleibt der Graph im Streifen $(3{,}5;\ 4{,}5)$. $\delta_0=0{,}1$ ist nicht die größte Antwort, aber sie gewinnt.
:::

:::analogie
„Stetig heißt: Den Graphen zeichnen, ohne abzusetzen.“ Das Bild passt auf Intervallen. Es stimmt nicht mehr, sobald der Definitionsbereich Lücken hat: $1/x$ auf $\mathbb{R}\setminus\{0\}$ ist in jedem Punkt stetig, der Graph hat trotzdem zwei Äste.
:::

:::definition Definition 4.3 (Stetige Ergänzung)
<span class="anker" id="satz-4-3"></span>

Sei $f:\dot U_\eta(x_0)\to\mathbb{R}$ in ganz $\dot U_\eta(x_0)$ stetig, und es existiere $y_0:=\lim_{x\to x_0}f(x)\in\mathbb{R}$. Dann heißt $f$ in $x_0$ __stetig ergänzbar__. Die Funktion

$$\tilde f(x):=\begin{cases}f(x),&x\in\dot U_\eta(x_0),\\y_0,&x=x_0\end{cases}$$

heißt __stetige Ergänzung__ (oder Fortsetzung) von $f$ auf $U_\eta(x_0)$.
:::

⁠**So liest man das:** Man füllt die Stelle mit dem einzigen Wert, der den Graphen schließt.

::::beispiel [Beispiele]
$L$ wird mit $\tilde L(2)=4$ zur Geraden $x+2$. $h(x)=\frac{\mathrm{e}^x-1}x$ hat bei 0 keinen Wert, wird aber mit $\tilde h(0)=1$ nach [(3.5)](grenzwerte-von-funktionen.html#gl-3-5) stetig. **Nicht ergänzbar:** $H$ hat bei 0 keinen Grenzwert, $|1/x|$ wächst ohne Grenze.
::::

:::aufgabe Aufgabe 4 ★★ Toleranzspiel
<span class="anker" id="aufg-4"></span>

Sei $f(x)=\sqrt x$, $x_0=4$. (a) Zeige $|\sqrt x-2|\le\frac12|x-4|$ für $x\ge0$. (b) Gib $\delta_0(\varepsilon)$ an. (c) Wie groß ist es für $\varepsilon=0{,}1$, und wie groß wäre das größte mögliche $\delta_0$?

:::loesung
(a) $|\sqrt x-2|=\frac{|x-4|}{\sqrt x+2}\le\frac12|x-4|$. (b) $\delta_0=\min\{2\varepsilon,4\}$; die 4 hält $x$ im Definitionsbereich $x>0$. (c) $\delta_0=0{,}2$. Am größten: $\sqrt x\in(1{,}9;\ 2{,}1)$ heißt $x\in(3{,}61;\ 4{,}41)$, also $\delta_0=\min\{0{,}39;\ 0{,}41\}=0{,}39$.
:::
:::

::::formelsammlung
**Stetigkeit**

$$\lim\limits_{x\to x_0}f(x)=f(x_0)$$

Für $f:(a,b)\to\mathbb{R}$, $x_0\in(a,b)$: $f(x_0)$ ist erklärt, der Grenzwert existiert, beide sind gleich. Auf $(a,b)$ stetig: in jedem Punkt stetig.

**Einseitige Stetigkeit**

$$\lim\limits_{x\searrow x_0}f(x)=f(x_0),\qquad\lim\limits_{x\nearrow x_0}f(x)=f(x_0)$$

Rechtsseitig bzw. linksseitig stetig. Auf $[a,b]$ stetig: auf $(a,b)$ stetig, in $a$ rechtsseitig und in $b$ linksseitig stetig.

**Epsilon-Delta-Kriterium**

$$\forall\,\varepsilon>0\ \ \exists\,\delta_0>0:\quad|f(x)-f(x_0)|<\varepsilon\quad\forall\,x\in(x_0-\delta_0,x_0+\delta_0)$$

Gleichwertig zur Stetigkeit in $x_0$. $\delta_0=\delta_0(\varepsilon,x_0)$ darf von $\varepsilon$ und $x_0$ abhängen und muss $(x_0-\delta_0,x_0+\delta_0)\subset(a,b)$ erfüllen.

**Mit Umgebungen**

$$\forall\,\varepsilon>0\ \exists\,\delta_0>0\ \text{mit}\ \bigl(x\in U_{\delta_0}(x_0)\Rightarrow f(x)\in U_\varepsilon(f(x_0))\bigr)$$

Dieselbe Aussage in der Sprache der Umgebungen.

**Eingangstoleranz für die Parabel**

$$\delta_0:=\min\{1,\varepsilon/5\}$$

Für $f(x)=x^2$ bei $x_0=2$; an einer Stelle $x_0>0$ allgemein $\delta_0=\min\{1,\varepsilon/(2x_0+1)\}$: Je steiler der Graph, desto kleiner $\delta_0$.

**Stetige Ergänzung**

$$\tilde f(x):=\begin{cases}f(x),&x\in\dot U_\eta(x_0),\\y_0,&x=x_0\end{cases}$$

Für $f$ stetig in ganz $\dot U_\eta(x_0)$, falls $y_0:=\lim_{x\to x_0}f(x)\in\mathbb{R}$ existiert; dann heißt $f$ in $x_0$ stetig ergänzbar.
::::

::::lernkarten
:::karte begriff stetig
Wann heißt eine Funktion $f:(a,b)\to\mathbb{R}$ in einer Stelle $x_0\in(a,b)$ stetig, und wann auf ganz $(a,b)$?
---
In $x_0$ stetig, falls $\lim\limits_{x\to x_0}f(x)=f(x_0)$ ist: Der Funktionswert ist das, was man von nahebei erwartet. Auf $(a,b)$ stetig, falls $f$ in jedem Punkt von $(a,b)$ stetig ist.
--- falsch
In $x_0$ stetig, falls $\lim\limits_{x\to x_0}f(x)$ existiert, gleich welchen Wert $f(x_0)$ hat. Auf $(a,b)$ stetig, falls $f$ in jedem Punkt von $(a,b)$ einen solchen Grenzwert besitzt.
--- falsch
In $x_0$ stetig, falls $f(x_0)$ erklärt ist: Jede Funktion ist an den Stellen stetig, an denen sie einen Wert hat. Auf $(a,b)$ stetig, falls $f$ dort überall erklärt ist.
--- falsch
In $x_0$ stetig, falls $\lim\limits_{x\to x_0}f(x)=f(x_0)$ ist. Auf $(a,b)$ stetig, falls $f$ in einem Punkt stetig ist, denn Stetigkeit überträgt sich von dort auf das ganze Intervall.
:::
:::karte zusammenhang Stetigkeit
Welche drei Forderungen stecken in der Stetigkeit von $f$ in $x_0$, und warum sind Polynome überall stetig?
---
$f(x_0)$ ist erklärt, der Grenzwert $\lim_{x\to x_0}f(x)$ existiert, und beide sind gleich. Polynome erfüllen das überall, weil ihr Grenzwert durch Einsetzen entsteht: $\lim_{x\to x_0}P_n(x)=P_n(x_0)$.
--- falsch
$f$ ist bei $x_0$ erklärt, beschränkt und monoton. Polynome erfüllen das überall, weil sie nur endlich viele Nullstellen haben und dazwischen nicht springen können.
--- falsch
Der linksseitige Grenzwert existiert, der rechtsseitige existiert, und beide sind gleich; $f(x_0)$ selbst spielt keine Rolle. Polynome erfüllen das, weil ihr Grenzwert durch Einsetzen entsteht.
--- falsch
$f(x_0)$ ist erklärt, der Grenzwert existiert, und beide sind gleich. Polynome sind aber nur zwischen ihren Nullstellen stetig, weil der Graph an einer Nullstelle die Achse kreuzt.
:::
:::karte begriff rechtsseitig stetig und linksseitig stetig
Wann heißt $f$ in $x_0$ rechtsseitig stetig und wann linksseitig stetig, und welche davon gilt für den Schalter $H$ bei 0?
---
Rechtsseitig stetig, falls $\lim\limits_{x\searrow x_0}f(x)=f(x_0)$; linksseitig stetig, falls $\lim\limits_{x\nearrow x_0}f(x)=f(x_0)$. $H$ ist bei 0 rechtsseitig stetig, nicht linksseitig: $\lim_{x\nearrow0}H(x)=0\ne1=H(0)$.
--- falsch
Rechtsseitig stetig, falls $\lim\limits_{x\searrow x_0}f(x)$ existiert; linksseitig stetig, falls $\lim\limits_{x\nearrow x_0}f(x)$ existiert. $H$ ist bei 0 deshalb beidseitig stetig, weil beide einseitigen Grenzwerte existieren.
--- falsch
Rechtsseitig stetig, falls $\lim\limits_{x\nearrow x_0}f(x)=f(x_0)$; linksseitig stetig, falls $\lim\limits_{x\searrow x_0}f(x)=f(x_0)$. $H$ ist bei 0 linksseitig stetig, nicht rechtsseitig, denn $H(0)=1$ ist der Wert rechts.
--- falsch
Rechtsseitig stetig, falls $\lim\limits_{x\searrow x_0}f(x)=f(x_0)$; linksseitig stetig, falls $\lim\limits_{x\nearrow x_0}f(x)=f(x_0)$. $H$ ist bei 0 weder rechtsseitig noch linksseitig stetig, weil $H$ dort springt.
:::
:::karte zusammenhang stetig auf einem abgeschlossenen Intervall
Was bedeutet es, dass $f:[a,b]\to\mathbb{R}$ auf dem abgeschlossenen Intervall $[a,b]$ stetig ist, und warum genügt an den Rändern einseitige Stetigkeit?
---
$f$ ist auf $(a,b)$ stetig, in $a$ rechtsseitig und in $b$ linksseitig stetig. An den Rändern reicht das, weil $f$ links von $a$ und rechts von $b$ nicht erklärt ist; es gibt dort nur Testfolgen von innen.
--- falsch
$f$ ist auf $(a,b)$ stetig; an den Rändern $a$ und $b$ wird nichts verlangt, weil sich dort keine Testfolge von beiden Seiten bilden lässt und ein Grenzwert deshalb gar nicht gebildet werden kann.
--- falsch
$f$ ist auf $(a,b)$ stetig, in $a$ linksseitig und in $b$ rechtsseitig stetig. An den Rändern genügt das, weil man von außen an das Intervall herankommt und die Werte dort fortsetzt.
--- falsch
$f$ ist in $a$ und $b$ beidseitig stetig und dazwischen überall. An den Rändern genügt einseitige Stetigkeit nicht, weil der Grenzwert immer Testfolgen von beiden Seiten verlangt.
:::
:::karte formel Epsilon-Delta-Kriterium
Wie lautet das Epsilon-Delta-Kriterium für die Stetigkeit von $f:(a,b)\to\mathbb{R}$ in $x_0$, mit den Quantoren in der richtigen Reihenfolge?
---
$\forall\,\varepsilon>0\ \ \exists\,\delta_0>0:\quad|f(x)-f(x_0)|<\varepsilon\quad\forall\,x\in(x_0-\delta_0,x_0+\delta_0)$. Erst steht $\varepsilon$ fest, dann wird $\delta_0$ gewählt; das ist gleichwertig zur Stetigkeit in $x_0$.
--- falsch
$\exists\,\delta_0>0\ \ \forall\,\varepsilon>0:\quad|f(x)-f(x_0)|<\varepsilon\quad\forall\,x\in(x_0-\delta_0,x_0+\delta_0)$. Ein einziges $\delta_0$ muss für jede Toleranz $\varepsilon$ passen; das ist gleichwertig zur Stetigkeit.
--- falsch
$\forall\,\delta_0>0\ \ \exists\,\varepsilon>0:\quad|f(x)-f(x_0)|<\varepsilon\quad\forall\,x\in(x_0-\delta_0,x_0+\delta_0)$. Zu jeder Eingangstoleranz gibt es eine Ausgangstoleranz; das ist gleichwertig zur Stetigkeit.
--- falsch
$\forall\,\varepsilon>0\ \ \exists\,\delta_0>0$ und ein $x$ mit $|x-x_0|<\delta_0$ und $|f(x)-f(x_0)|<\varepsilon$. Zu jeder Toleranz gibt es also eine nahe Stelle mit nahem Wert; das ist gleichwertig zur Stetigkeit.
:::
:::karte zusammenhang Toleranzspiel
Wie läuft das Toleranzspiel des Epsilon-Delta-Kriteriums ab, und wovon darf die Eingangstoleranz $\delta_0$ abhängen?
---
Der Gegner gibt eine Ausgangstoleranz $\varepsilon$ vor, man antwortet mit $\delta_0$ und gewinnt, wenn alle $x$ näher als $\delta_0$ an $x_0$ einen Wert näher als $\varepsilon$ an $f(x_0)$ liefern. $\delta_0=\delta_0(\varepsilon,x_0)$ darf von $\varepsilon$ und $x_0$ abhängen.
--- falsch
Man gibt zuerst $\delta_0$ vor, der Gegner antwortet mit $\varepsilon$ und gewinnt, wenn er ein $x$ nahe $x_0$ mit weit entferntem Wert findet. $\delta_0$ darf deshalb nicht von $\varepsilon$ abhängen, sondern nur von der Stelle $x_0$.
--- falsch
Der Gegner gibt $\varepsilon$ vor, man antwortet mit $\delta_0$ und gewinnt, wenn ein einziges $x$ näher als $\delta_0$ an $x_0$ einen Wert näher als $\varepsilon$ an $f(x_0)$ liefert. $\delta_0$ darf von $\varepsilon$ und von $x_0$ abhängen.
--- falsch
Der Gegner gibt $\varepsilon$ vor, man antwortet mit $\delta_0$ und gewinnt, wenn alle $x$ näher als $\delta_0$ an $x_0$ passende Werte liefern. $\delta_0$ muss aber für alle Stellen $x_0$ dasselbe sein und darf nur von $\varepsilon$ abhängen.
:::
:::karte herleitung Epsilon-Delta und Testfolgen
Wie zeigt man, dass das Epsilon-Delta-Kriterium in $x_0$ gleichwertig zur Stetigkeit über Testfolgen ist, in beiden Richtungen?
---
„$\Leftarrow$“: Zu $\varepsilon>0$ nimmt man $\delta_0$ aus dem Kriterium; für eine Testfolge gibt es $N_0$ mit $|x_n-x_0|<\delta_0$ für alle $n>N_0$, weil $x_n$ gegen $x_0$ konvergiert.
---
Für diese $n$ gilt $|f(x_n)-f(x_0)|<\varepsilon$, weil $x_n$ im $\delta_0$-Streifen um $x_0$ liegt; also gilt $f(x_n)\to f(x_0)$.
---
„$\Rightarrow$“ indirekt: Gilt das Kriterium nicht, gibt es $\varepsilon_1>0$ und zu jedem $\delta_0=\frac1n$ ein $x_n$ mit $|x_n-x_0|<\frac1n$ und $|f(x_n)-f(x_0)|\ge\varepsilon_1$, weil genau das die Verneinung des Kriteriums sagt.
---
Dann ist $x_n\ne x_0$, weil $|f(x_n)-f(x_0)|\ge\varepsilon_1>0$ ist, und $x_n\to x_0$; aber $f(x_n)$ läuft nicht gegen $f(x_0)$, ein Widerspruch zur Stetigkeit, weil der Abstand nie unter $\varepsilon_1$ fällt.
:::
:::karte zusammenhang Eingangstoleranz für die Parabel
Wie findet man für $f(x)=x^2$ bei $x_0=2$ zu jedem $\varepsilon$ ein passendes $\delta_0$, und warum wird es an steileren Stellen kleiner?
---
$|x^2-4|=|x-2|\,|x+2|$; man verlangt zuerst $|x-2|<1$, dann ist $|x+2|<5$, und $\delta_0:=\min\{1,\varepsilon/5\}$ gewinnt. An $x_0>0$ gibt derselbe Weg $\delta_0=\min\{1,\varepsilon/(2x_0+1)\}$: Je steiler der Graph, desto kleiner $\delta_0$.
--- falsch
$|x^2-4|=|x-2|^2$; also gewinnt $\delta_0:=\sqrt\varepsilon$ an jeder Stelle. Die Steilheit spielt keine Rolle, weil $\delta_0$ nur von $\varepsilon$ abhängt und nicht von der Stelle $x_0$, an der man prüft.
--- falsch
$|x^2-4|=|x-2|\,|x+2|$; man wählt $\delta_0:=\varepsilon/4$, weil $|x+2|$ bei $x=2$ genau 4 ist. Je steiler der Graph, desto größer darf $\delta_0$ sein, weil der Graph den Streifen dann schneller verlässt.
--- falsch
$|x^2-4|=|x-2|\,|x+2|$; man verlangt $|x-2|<1$, dann ist $|x+2|<5$, und $\delta_0:=5\varepsilon$ gewinnt. An steileren Stellen wird $\delta_0$ größer, weil dort der Faktor $2x_0+1$ wächst.
:::
:::karte zusammenhang Zeichnen ohne Absetzen
Warum stimmt das Bild „Stetig heißt: den Graphen zeichnen, ohne abzusetzen“ nicht mehr, wenn der Definitionsbereich Lücken hat?
---
$1/x$ auf $\mathbb{R}\setminus\{0\}$ ist in jedem Punkt stetig, der Graph hat trotzdem zwei Äste. Stetigkeit wird an jeder Stelle einzeln geprüft; das Bild vom Zeichnen passt nur auf Intervallen.
--- falsch
Es stimmt auch dann: $1/x$ auf $\mathbb{R}\setminus\{0\}$ ist nicht stetig, weil man beim Zeichnen bei 0 absetzen muss; eine Lücke im Definitionsbereich ist selbst eine Unstetigkeitsstelle.
--- falsch
Es stimmt nie, auch nicht auf Intervallen: Jede stetige Funktion hat Stellen, an denen man absetzen muss, weil Stetigkeit nur Grenzwerte betrifft und nicht den Graphen.
--- falsch
Weil eine Lücke im Definitionsbereich die Funktion an allen Stellen unstetig macht: $1/x$ auf $\mathbb{R}\setminus\{0\}$ ist in keinem Punkt stetig, obwohl ihre beiden Äste glatt aussehen.
:::
:::karte begriff stetig ergänzbar und stetige Ergänzung
Wann heißt eine Funktion $f$ in einer Stelle $x_0$ stetig ergänzbar, und wie sieht ihre stetige Ergänzung aus?
---
Wenn $f$ in ganz $\dot U_\eta(x_0)$ stetig ist und $y_0:=\lim_{x\to x_0}f(x)\in\mathbb{R}$ existiert. Die stetige Ergänzung $\tilde f$ stimmt auf $\dot U_\eta(x_0)$ mit $f$ überein und hat in $x_0$ den Wert $y_0$.
--- falsch
Wenn $f$ in $x_0$ einen Wert hat, den man ändern darf. Die stetige Ergänzung $\tilde f$ ersetzt $f(x_0)$ durch den Mittelwert der einseitigen Grenzwerte, auch wenn diese verschieden sind.
--- falsch
Wenn $f$ in ganz $\dot U_\eta(x_0)$ stetig ist, gleich ob in $x_0$ ein Grenzwert existiert. Die stetige Ergänzung $\tilde f$ hat in $x_0$ den Wert 0 und stimmt sonst mit $f$ überein.
--- falsch
Wenn $f$ in ganz $\dot U_\eta(x_0)$ stetig ist und $|f(x)|$ bei $x_0$ ohne Grenze wächst. Die stetige Ergänzung $\tilde f$ setzt dann in $x_0$ den Wert $\infty$ ein und schließt so den Graphen.
:::
:::karte zusammenhang Ergänzen einer Lücke
Warum lassen sich die Lücke $L$ bei 2 und $h(x)=\frac{\mathrm{e}^x-1}x$ bei 0 stetig ergänzen, der Kehrwert $|1/x|$ bei 0 aber nicht?
---
$L$ hat bei 2 den Grenzwert 4, mit $\tilde L(2)=4$ wird $L$ zur Geraden $x+2$; $h$ hat bei 0 den Grenzwert 1, also $\tilde h(0)=1$. $|1/x|$ wächst bei 0 ohne Grenze, es gibt keinen Grenzwert $y_0\in\mathbb{R}$.
--- falsch
Weil $L$ und $h$ rationale Funktionen sind und sich rationale Funktionen überall stetig ergänzen lassen; $|1/x|$ enthält dagegen einen Betrag und ist deshalb keine rationale Funktion.
--- falsch
Weil bei $L$ und $h$ Zähler und Nenner an der Stelle null sind und $\frac00$ als 1 gilt; bei $|1/x|$ ist nur der Nenner null, und $\frac10$ lässt sich auf keinen Wert festlegen.
--- falsch
Weil $L$ und $h$ nahe der Stelle beschränkt sind und $|1/x|$ nicht. Jede beschränkte Funktion lässt sich an einer fehlenden Stelle stetig ergänzen, notfalls durch den Wert 0.
:::
::::
