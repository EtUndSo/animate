---
title: Stufe 5: Divergenz und Laplace-Operator
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110600
summary: Der Gradient macht aus einer Funktion ein Feld.
tags: Divergenz, Quellendichte, Senke, Laplace-Operator, harmonisch
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Der Gradient macht aus einer Funktion ein Feld. Diese Stufe geht den umgekehrten Weg: Aus einem Feld wird eine Funktion, die angibt, wie stark das Feld an jeder Stelle auseinanderströmt.
:::

**Die Idee.** Stell dir $\boldsymbol{E}$ als Strömung vor und einen kleinen Würfel mit Kante $a$ um den Punkt $\boldsymbol{x}$. Durch die zwei Wände senkrecht zur $x_j$-Achse zählt nur $E_j$. Es fließt netto etwa $a^2\bigl(E_j(\boldsymbol{x}+\frac a2\hat{\boldsymbol{e}}_j)-E_j(\boldsymbol{x}-\frac a2\hat{\boldsymbol{e}}_j)\bigr)\approx a^3\,\partial E_j/\partial x_j$ hinaus. Summiert über alle Wandpaare ergibt das $a^3\sum_j\partial E_j/\partial x_j$ (Abb. [5](#abb-5)). Es kommt also nur auf die Diagonale der Jacobi-Matrix an.

:::abbildung hm3/k1quelle 5
Links strömt aus dem gestrichelten Kästchen mehr hinaus als hinein. In der Mitte tritt an der einen Wand aus, was an der gegenüberliegenden eintritt. Rechts strömt es seitlich hinaus und oben und unten hinein, die Bilanz ist null.
:::

:::definition Definition 5.1 (Divergenz)
<span class="anker" id="satz-5-1"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $\boldsymbol{E}=(E_1,\dots,E_n)^T$ ein differenzierbares Vektorfeld auf $\mathcal U$. Die __Divergenz__ von $\boldsymbol{E}$ ist

<span class="anker" id="gl-5-1"></span>
$$\operatorname{div}\boldsymbol{E}:=\nabla\cdot\boldsymbol{E}=\sum_{j=1}^n\frac{\partial E_j}{\partial x_j}. \tag{5.1}$$
:::

⁠**So liest man das:** Das Ergebnis ist eine Funktion, kein Feld. Sie ist ein Maß für die lokale __Quellendichte__ von $\boldsymbol{E}$: Positiv heißt Quelle, negativ heißt __Senke__. $\nabla\cdot\boldsymbol{E}$ ist das formale Skalarprodukt von Nabla mit $\boldsymbol{E}$, und $\operatorname{div}\boldsymbol{E}$ ist die Spur der Jacobi-Matrix $D\boldsymbol{E}$. **Beispiele:** $\operatorname{div}(2x,4y)=6$, das Drehfeld hat $\operatorname{div}(-y,x)=0$, das Strahlfeld hat $\operatorname{div}\boldsymbol{x}=n$.

:::definition Definition 5.2 (Laplace-Operator)
<span class="anker" id="satz-5-2"></span>

Für eine zweimal differenzierbare Funktion $\varphi:\mathcal U\to\mathbb{R}$ ist

<span class="anker" id="gl-5-2"></span>
$$\Delta\varphi:=\sum_{j=1}^n\frac{\partial^2\varphi}{\partial x_j^2}. \tag{5.2}$$

$\Delta$ heißt __Laplace-Operator__. Auf ein Vektorfeld wirkt er komponentenweise: $\Delta\boldsymbol{F}=(\Delta F_1,\dots,\Delta F_n)^T$.
:::

⁠**So liest man das:** Für ein Gradientenfeld $\boldsymbol{E}=\nabla\varphi$ ist $\operatorname{div}\boldsymbol{E}=\sum_j\partial^2\varphi/\partial x_j^2$. Also gilt $\Delta\varphi=\operatorname{div}(\nabla\varphi)$, formal $\Delta=\nabla\cdot\nabla$. In den Ingenieurwissenschaften schreibt man deshalb oft $\nabla^2$. $\Delta$ ist ein Differentialoperator zweiter Ordnung. Er vergleicht den Wert in einem Punkt mit dem Mittel der Umgebung, in einer Dimension ist $\frac12(\varphi(x+a)+\varphi(x-a))-\varphi(x)\approx\frac{a^2}2\varphi''(x)$. Eine Funktion mit $\Delta u=0$ heißt __harmonisch__: Ihr Gradientenfeld hat keine Quellen und Senken.

:::satz Satz 5.3 (Produktregel der Divergenz)
<span class="anker" id="satz-5-3"></span>

$\operatorname{div}(\varphi\boldsymbol{F})=\nabla\varphi\cdot\boldsymbol{F}+\varphi\,\operatorname{div}\boldsymbol{F}$.
:::

:::beweis Produktregel
$\sum_j\partial_{x_j}(\varphi F_j)=\sum_j(\partial_{x_j}\varphi)F_j+\varphi\sum_j\partial_{x_j}F_j$. Hier steht $\partial_{x_j}$ kurz für $\partial/\partial x_j$.
:::

:::satz Satz 5.4 (Divergenz radialsymmetrischer Felder)
<span class="anker" id="satz-5-4"></span>

Für $\boldsymbol{E}(\boldsymbol{x})=f(r)\,\hat{\boldsymbol{e}}_r$ mit glattem $f:(0,\infty)\to\mathbb{R}$ gilt auf $\mathbb{R}^n\setminus\{0\}$

<span class="anker" id="gl-5-3"></span>
$$\operatorname{div}\boldsymbol{E}=f'(r)+(n-1)\frac{f(r)}{r}. \tag{5.3}$$
:::

:::beweis Skalar mal Strahlfeld
Schreibe $\boldsymbol{E}=\frac{f(r)}{r}\boldsymbol{x}$ und nimm Satz [5.3](#satz-5-3) mit $\varphi=f(r)/r$ und $\boldsymbol{F}=\boldsymbol{x}$. Es ist $\operatorname{div}\boldsymbol{x}=n$. Nach [(4.3)](radiale-funktionen-und-felder.html#gl-4-3) und der Quotientenregel ist $\nabla\varphi=\frac{f'(r)\,r-f(r)}{r^2}\,\hat{\boldsymbol{e}}_r$. Wegen $\hat{\boldsymbol{e}}_r\cdot\boldsymbol{x}=r$ folgt

$$\operatorname{div}\boldsymbol{E}=\frac{f'(r)\,r-f(r)}{r}+n\,\frac{f(r)}{r}=f'(r)+(n-1)\frac{f(r)}{r}.$$
:::

⁠**So liest man das:** $f'$ zählt, wie die Pfeillänge nach außen zunimmt. $(n-1)f/r$ zählt, dass radiale Pfeile schon bei gleicher Länge auseinanderlaufen. **Kontrolle:** Für $\boldsymbol{E}=\boldsymbol{x}$ ist $f=r$, und [(5.3)](#gl-5-3) gibt $1+(n-1)=n$. Für $n=1$ bleibt nur $f'$, denn auf einer Geraden gibt es kein Auseinanderlaufen zur Seite.

**Beispiel: Punktladung.** Für $u=Q/(4\pi r)$ und $\boldsymbol{E}=-\nabla u=\frac{Q}{4\pi r^2}\hat{\boldsymbol{e}}_r$ gibt [(5.3)](#gl-5-3) mit $n=3$

<span class="anker" id="gl-5-4"></span>
$$-\Delta u=\operatorname{div}\boldsymbol{E}=-\frac{Q}{2\pi r^3}+2\cdot\frac{Q}{4\pi r^3}=0\quad\text{in }\mathbb{R}^3\setminus\{0\}. \tag{5.4}$$

Das Potential der Punktladung ist harmonisch. Allgemein verschwindet [(5.3)](#gl-5-3) für $f\propto r^{-(n-1)}$. In drei Dimensionen ist also genau der Abfall mit $1/r^2$ quellenfrei.

:::frage Das Feld der Punktladung strömt sichtbar nach außen. Warum ist die Divergenz null?
Die Divergenz ist eine lokale Bilanz. Die Pfeile laufen auseinander, werden aber nach außen kürzer, und in [(5.3)](#gl-5-3) heben sich beide Anteile genau auf. Die Quelle des Felds sitzt im Nullpunkt, und dieser Punkt gehört nicht zum Definitionsbereich.
:::

:::aufgabe Aufgabe 7 ★★ Radiale harmonische Funktionen
<span class="anker" id="aufg-7"></span>

Sei $u(\boldsymbol{x})=v(r)$ auf $\mathbb{R}^n\setminus\{0\}$ mit zweimal stetig differenzierbarem $v$.

<ol class="al">

<li>

Zeige $\Delta u=v''(r)+\frac{n-1}{r}\,v'(r)$. Tipp: [(4.3)](radiale-funktionen-und-felder.html#gl-4-3) und [(5.3)](#gl-5-3).

</li>

<li>

Bestimme alle radialsymmetrischen harmonischen Funktionen in $\mathbb{R}^4\setminus\{0\}$. Tipp: Multipliziere die Gleichung mit $r^3$ und erkenne eine Ableitung.

</li>

<li>

Zeige, dass $\ln r$ in $\mathbb{R}^2\setminus\{0\}$ harmonisch ist.

</li>

<li>

Zeige $\Delta(fg)=f\Delta g+g\Delta f+2\nabla f\cdot\nabla g$ und berechne damit $\Delta(x\,r^{-3})$ in $\mathbb{R}^3\setminus\{0\}$.

</li>

</ol>

:::loesung
(a) $\nabla u=v'(r)\,\hat{\boldsymbol{e}}_r$. Mit $f=v'$ in [(5.3)](#gl-5-3) folgt $\Delta u=\operatorname{div}\nabla u=v''+\frac{n-1}{r}v'$. (b) Für $n=4$: $v''+\frac3rv'=0$. Multipliziert mit $r^3$ steht $(r^3v')'=0$ da, also $v'=c/r^3$ und $v=c_1/r^2+c_2$ mit Konstanten $c_1,c_2$. (c) Für $n=2$ und $v=\ln r$: $-\frac1{r^2}+\frac1r\cdot\frac1r=0$. (d) $\nabla(fg)=f\nabla g+g\nabla f$. Mit Satz [5.3](#satz-5-3) ist $\operatorname{div}(f\nabla g)=\nabla f\cdot\nabla g+f\Delta g$, und ebenso für den zweiten Summanden. Für $f=x$, $g=r^{-3}$ ist $\Delta f=0$. Aus (a) mit $n=3$ folgt $\Delta g=12\,r^{-5}-6\,r^{-5}=6\,r^{-5}$. Außerdem ist $\nabla f\cdot\nabla g=(1,0,0)\cdot(-3r^{-4}\hat{\boldsymbol{e}}_r)=-3x\,r^{-5}$. Zusammen: $\Delta(x\,r^{-3})=6x\,r^{-5}-6x\,r^{-5}=0$. Die Funktion ist harmonisch, obwohl sie nicht radialsymmetrisch ist.
:::
:::
