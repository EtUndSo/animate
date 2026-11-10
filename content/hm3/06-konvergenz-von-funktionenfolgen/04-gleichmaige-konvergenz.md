---
title: Stufe 2: Gleichmäßige Konvergenz
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen
knoten: Kapitel 6: Konvergenz von Funktionenfolgen
order: 3160400
summary: Diese Stufe verlangt ein gemeinsames Tempo für alle Stellen und zeigt, wie man das prüft, auch ohne die Grenzfunktion zu kennen.
tags: Gleichmäßige Konvergenz
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Diese Stufe verlangt ein gemeinsames Tempo für alle Stellen und zeigt, wie man das prüft, auch ohne die Grenzfunktion zu kennen.
:::

**Die Idee.** Lege um die Grenzfunktion einen Schlauch, der um $\varepsilon$ nach oben und unten reicht. Verlangt wird: Ab einem Index liegt die ganze Kurve im Schlauch, nicht nur jeder Punkt für sich irgendwann (Abb. [2](#abb-2)). Dazu fasst man die Abweichungen aller Stellen in einer Zahl zusammen, der größten.

:::abbildung hm3/k6schlauch 2
Der Schlauch $|y|<0{,}2$ um die Grenzfunktion null. Links liegt der Rippel $w_{12}$ ganz darin. Rechts ragt die Entladekurve $u_{16}$ bei $x=0$ hinaus, und das bleibt für jedes $n$ so.
:::

:::definition Definition 2.1 (Gleichmäßige Konvergenz)
<span class="anker" id="satz-2-1"></span>

Seien $(f_n)_{n\in\mathbb{N}}$ und $f$ beschränkte Funktionen auf $[a,b]$. __Gleichmäßige Konvergenz__ der Folge gegen $f$ heißt

<span class="anker" id="gl-2-1"></span>
$$\lim_{n\to\infty}\;\sup_{x\in[a,b]}|f_n(x)-f(x)|=0. \tag{2.1}$$
:::

⁠**So liest man das:** $d_n:=\sup_{x\in[a,b]}|f_n(x)-f(x)|$ ist je $n$ eine einzige Zahl, die Abweichung an der schlechtesten Stelle. Gleichmäßig heißt $d_n\to0$. Ausgeschrieben: Zu jedem $\varepsilon>0$ gibt es ein $N$, das für alle $x$ zugleich passt. Bei punktweiser Konvergenz wird dagegen erst $x$ gewählt und dann $N$. Wegen $|f_n(x)-f(x)|\le d_n$ folgt aus gleichmäßiger Konvergenz die punktweise. Die Umkehrung ist falsch.

**So prüft man es.**

<ol class="rm">

<li>

Bestimme die punktweise Grenzfunktion $f$. Nur sie kommt als gleichmäßiger Grenzwert infrage.

</li>

<li>

Berechne $d_n$ über Randwerte und Nullstellen der Ableitung von $f_n-f$, oder finde eine Schranke für $|f_n(x)-f(x)|$, die nicht von $x$ abhängt und gegen null strebt.

</li>

<li>

Für das Gegenteil reicht eine Stelle $x_n$ mit $|f_n(x_n)-f(x_n)|\ge c>0$ für alle $n$.

</li>

</ol>

::::beispiel [Beispiele]
⁠**Rippel:** Es ist $f=0$ und $|w_n(x)|\le1/n$, also $d_n=1/n\to0$. Das ist gleichmäßig. **Entladekurven:** Mit $x_n=1/n$ ist $|u_n(x_n)-f(x_n)|=\mathrm{e}^{-1}$, also nicht gleichmäßig. Genauer gilt $d_n=\sup_{0<x\le1}\mathrm{e}^{-nx}=1$. Dieser Wert wird nicht angenommen, denn bei $x=0$ ist die Abweichung null. Deshalb steht in [(2.1)](#gl-2-1) ein Supremum und kein Maximum. **Beulen:** Mit $x_n=1/n$ ist $b_n(x_n)=n/\mathrm{e}\to\infty$, also nicht gleichmäßig.
::::

⁠**Grenzfall:** Auf $[\delta,1]$ mit festem $\delta>0$ konvergieren die Entladekurven gleichmäßig gegen 0, denn dort ist $d_n=\mathrm{e}^{-n\delta}\to0$. Für $\delta=0{,}1$ gilt $d_n<0{,}01$ ab $n=47$, passend zu Stufe [1](punktweise-konvergenz.html#stufe-1). Das Hindernis sitzt allein bei $x=0$. Je kleiner $\delta$, desto langsamer die Konvergenz.

**Ohne die Grenzfunktion.** Oft kennt man $f$ nicht. Bei Zahlenfolgen hilft dann die Cauchy-Bedingung. Für Funktionen gilt sie genauso, wenn der Betrag durch die größte Abweichung ersetzt wird.

:::satz Satz 2.2 (Cauchy-Kriterium)
<span class="anker" id="satz-2-2"></span>

Eine Folge beschränkter Funktionen $(f_n)_{n\in\mathbb{N}}$ auf $[a,b]$ konvergiert genau dann gleichmäßig, wenn

<span class="anker" id="gl-2-2"></span>
$$\sup_{x\in[a,b]}|f_m(x)-f_n(x)|\to0\quad\text{für }m,n\to\infty. \tag{2.2}$$
:::

:::beweis Cauchy-Kriterium
⁠**Notwendig.** Sei $f$ der gleichmäßige Grenzwert. Die Dreiecksungleichung gibt an jeder Stelle

$$|f_m(x)-f_n(x)|\le|f_m(x)-f(x)|+|f_n(x)-f(x)|\le d_m+d_n.$$

Die rechte Seite hängt nicht von $x$ ab und strebt gegen null.

⁠**Hinreichend, Schritt 1.** Für festes $x$ ist $|f_m(x)-f_n(x)|$ höchstens so groß wie das Supremum in [(2.2)](#gl-2-2). Also ist $(f_n(x))_{n\in\mathbb{N}}$ eine Cauchy-Folge von Zahlen. Weil $\mathbb{R}$ und $\mathbb{C}$ vollständig sind, hat sie einen Grenzwert, und diesen nennen wir $f(x)$. Damit gilt $f_n\to f$ punktweise.

⁠**Schritt 2.** Sei $\varepsilon>0$. Nach [(2.2)](#gl-2-2) gibt es ein $N$ mit $|f_m(x)-f_n(x)|<\varepsilon$ für alle $m\ge n\ge N$ und alle $x$. Halte $n$ und $x$ fest und lasse $m\to\infty$. Aus der punktweisen Konvergenz folgt

$$|f(x)-f_n(x)|=\lim_{m\to\infty}|f_m(x)-f_n(x)|\le\varepsilon\quad\text{für alle }n\ge N,\ x\in[a,b].$$

Im Grenzwert wird aus $<$ ein $\le$. Das $N$ hängt nicht von $x$ ab, also ist $d_n\le\varepsilon$ für $n\ge N$. Außerdem ist $|f(x)|\le|f_N(x)|+\varepsilon$, die Grenzfunktion ist also beschränkt.
:::

⁠**So liest man das:** Das Kriterium vergleicht die Glieder nur untereinander, $f$ kommt darin nicht vor. Für die Entladekurven ist mit $y=\mathrm{e}^{-nx}$ die Differenz $u_n(x)-u_{2n}(x)=y-y^2$. Ihr Maximum $\frac14$ liegt bei $y=\frac12$, für jedes $n$. Die Bedingung [(2.2)](#gl-2-2) ist verletzt, und das zeigt ohne Kenntnis von $f$: keine gleichmäßige Konvergenz.

:::frage Reicht es, wenn benachbarte Glieder einander nahe kommen?
Nein. Für die Entladekurven ist mit $t=\mathrm{e}^{-x}$ die Differenz $u_n-u_{n+1}=t^n(1-t)$, und ihr Maximum ist kleiner als $1/(n+1)$. Benachbarte Kurven rücken also zusammen, und trotzdem konvergiert die Folge nicht gleichmäßig. In [(2.2)](#gl-2-2) müssen $m$ und $n$ unabhängig voneinander groß werden.
:::

:::aufgabe Aufgabe 2 ★★ Drei Beulen
<span class="anker" id="aufg-2"></span>

Untersuche auf $[0,1]$ auf punktweise und gleichmäßige Konvergenz.

<ol class="al">

<li>

$f_n(x)=nx/(1+n^2x^2)$. Was geschieht auf $[\delta,1]$ mit $\delta>0$?

</li>

<li>

$f_n(x)=x/(1+nx^2)$. Ab welchem $n$ gilt $d_n<0{,}01$?

</li>

<li>

$f_n(x)=n\,x\,(1-x)^n$.

</li>

</ol>

:::loesung
(a) $f_n(0)=0$, und für $x>0$ ist $|f_n(x)|\le nx/(n^2x^2)=1/(nx)\to0$. Also $f=0$. Aus $f_n'(x)=n(1-n^2x^2)/(1+n^2x^2)^2$ folgt die Spitze bei $x=1/n$ mit $f_n(1/n)=\frac12$. Damit ist $d_n=\frac12$, die Konvergenz ist nicht gleichmäßig. Auf $[\delta,1]$ gilt $|f_n(x)|\le1/(n\delta)\to0$, dort ist sie gleichmäßig. (b) $f=0$. Aus $f_n'(x)=(1-nx^2)/(1+nx^2)^2$ folgt die Spitze bei $x=1/\sqrt n$ mit dem Wert $1/(2\sqrt n)=d_n\to0$. Die Konvergenz ist gleichmäßig, die Spitze sinkt. $d_n<0{,}01$ heißt $\sqrt n>50$, also $n\ge2501$. (c) Bei $x=0$ und $x=1$ ist $f_n=0$, für $0<x<1$ gewinnt $(1-x)^n$ gegen $n$. Also $f=0$. Aus $f_n'(x)=n(1-x)^{n-1}(1-(n+1)x)$ folgt die Spitze bei $x=1/(n+1)$ mit $d_n=(n/(n+1))^{n+1}\to\mathrm{e}^{-1}\approx0{,}368$. Die Konvergenz ist nicht gleichmäßig.
:::
:::
