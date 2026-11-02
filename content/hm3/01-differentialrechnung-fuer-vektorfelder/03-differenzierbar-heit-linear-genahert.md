---
title: Stufe 2: Differenzierbar heißt linear genähert
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110300
summary: Partielle Ableitungen schauen nur in Achsenrichtung.
tags: total differenzierbar, differenzierbar, Tangentialebene, stetig differenzierbar, k-mal stetig differenzierbar
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Partielle Ableitungen schauen nur in Achsenrichtung. Diese Stufe sagt, wann die Jacobi-Matrix eine Abbildung wirklich in allen Richtungen beschreibt.
:::

**Die Idee.** Die Matrix soll die Abbildung nahe einem Punkt ersetzen: $\boldsymbol f(\boldsymbol{x})\approx\boldsymbol f(\boldsymbol{x}_0)+A(\boldsymbol{x}-\boldsymbol{x}_0)$. Dass der Fehler klein wird, genügt nicht, das leistet bei stetigem $\boldsymbol f$ jede Matrix. Der Fehler muss schneller verschwinden als der Abstand $|\boldsymbol{x}-\boldsymbol{x}_0|$, und zwar aus jeder Richtung.

:::definition Definition 2.1 (Totale Differenzierbarkeit)
<span class="anker" id="satz-2-1"></span>

$\boldsymbol f:\mathcal U\to\mathbb{R}^m$ heißt in $\boldsymbol{x}_0\in\mathcal U$ __total differenzierbar__, kurz __differenzierbar__, wenn es eine Matrix $A\in\mathbb{R}^{m\times n}$ gibt mit

<span class="anker" id="gl-2-1"></span>
$$\lim_{\boldsymbol{x}\to\boldsymbol{x}_0}\frac{|\boldsymbol f(\boldsymbol{x})-\boldsymbol f(\boldsymbol{x}_0)-A(\boldsymbol{x}-\boldsymbol{x}_0)|}{|\boldsymbol{x}-\boldsymbol{x}_0|}=0. \tag{2.1}$$
:::

⁠**So liest man das:** Der Zähler ist der Fehler der linearen Näherung, der Bruch setzt ihn ins Verhältnis zum Abstand. Für eine skalare Funktion auf $\mathbb{R}^2$ heißt das: Nahe $\boldsymbol{x}_0$ schmiegt sich ihr Graph an die __Tangentialebene__ $z=f(\boldsymbol{x}_0)+\nabla f(\boldsymbol{x}_0)\cdot(\boldsymbol{x}-\boldsymbol{x}_0)$. **Grenzfall:** Für $n=m=1$ steht dort $\bigl|\frac{f(x)-f(x_0)}{x-x_0}-A\bigr|\to0$, die bekannte Ableitung.

:::satz Satz 2.2 (Die Näherung ist die Jacobi-Matrix)
<span class="anker" id="satz-2-2"></span>

Ist $\boldsymbol f$ in $\boldsymbol{x}_0$ differenzierbar, dann existieren dort alle partiellen Ableitungen, und es gilt $A=D\boldsymbol f(\boldsymbol{x}_0)$.
:::

:::beweis Die Spalten von $A$
Setze in [(2.1)](#gl-2-1) $\boldsymbol{x}=\boldsymbol{x}_0+t\,\hat{\boldsymbol{e}}_k$ mit dem Einheitsvektor $\hat{\boldsymbol{e}}_k$ der $x_k$-Achse und lasse $t\to0$ gehen. Dann ist $|\boldsymbol{x}-\boldsymbol{x}_0|=|t|$, und [(2.1)](#gl-2-1) sagt $\frac1t\bigl(\boldsymbol f(\boldsymbol{x}_0+t\,\hat{\boldsymbol{e}}_k)-\boldsymbol f(\boldsymbol{x}_0)\bigr)\to A\,\hat{\boldsymbol{e}}_k$. Der Grenzwert links ist die partielle Ableitung nach $x_k$, und $A\,\hat{\boldsymbol{e}}_k$ ist Spalte $k$ von $A$.
:::

**Beispiel.** Für die Schale gilt um $(1,1)$ exakt $\varphi(1+s_1,1+s_2)=3+2s_1+4s_2+s_1^2+2s_2^2$. Mit $A=(2\;\;4)$ bleibt der Fehler $s_1^2+2s_2^2\le2|\boldsymbol s|^2$. Der Bruch ist höchstens $2|\boldsymbol s|$ und geht gegen null.

**Gegenbeispiel.** Die Umkehrung von Satz [2.2](#satz-2-2) ist falsch. Sei $f(x,y)=\dfrac{xy}{x^2+y^2}$ für $(x,y)\neq(0,0)$ und $f(0,0)=0$. Auf beiden Achsen ist $f=0$, also sind beide partiellen Ableitungen im Nullpunkt null, und als Näherung käme nur $A=0$ in Frage. Auf der Diagonale ist aber $f(t,t)=\frac12$, so nah man dem Nullpunkt auch kommt (Abb. [2](#abb-2)). $f$ ist dort nicht einmal stetig. Die partiellen Ableitungen sehen diesen Sprung nicht, weil er neben den Achsen liegt.

:::abbildung hm3/k1schraeg 2
Links: $f=xy/(x^2+y^2)$ ist auf jedem Strahl durch den Nullpunkt konstant, die Zahlen sind die Werte auf den Strahlen. Rechts: Längs der Achse ist $f=0$, längs der Diagonale springt $f$ im Nullpunkt von $\frac12$ auf $0$.
:::

:::satz Satz 2.3 (Hinreichende Bedingung)
<span class="anker" id="satz-2-3"></span>

Sind alle partiellen Ableitungen von $\boldsymbol f$ auf $\mathcal U$ stetig, dann ist $\boldsymbol f$ auf $\mathcal U$ differenzierbar. Man nennt $\boldsymbol f$ dann __stetig differenzierbar__.
:::

⁠**Idee des Beweises:** Man geht von $\boldsymbol{x}_0$ nach $\boldsymbol{x}$ in Schritten parallel zu den Achsen. Auf jedem Stück ist jede Komponente eine Funktion einer Variablen, der Mittelwertsatz gibt ihre Änderung als partielle Ableitung an einer Zwischenstelle mal Schrittlänge. Wegen der Stetigkeit weicht diese Ableitung nur wenig vom Wert in $\boldsymbol{x}_0$ ab. Die Stetigkeit verbindet so die Achsen mit allen übrigen Richtungen.

:::definition Definition 2.4 ($C^k$)
<span class="anker" id="satz-2-4"></span>

$\boldsymbol f$ heißt __$k$-mal stetig differenzierbar__, wenn alle partiellen Ableitungen der Ordnung $\le k$ stetig sind, die Abbildung selbst als Ordnung 0 eingeschlossen. Der Raum dieser Abbildungen heißt $C^k(\mathcal U;\mathbb{R}^m)$.
:::

:::satz Satz 2.5 (Lemma von Schwarz)
<span class="anker" id="satz-2-5"></span>

Für $k\ge2$ dürfen bei $C^k$-Abbildungen alle partiellen Ableitungen der Ordnung $\le k$ beliebig vertauscht werden, zum Beispiel $\dfrac{\partial^2f}{\partial x\,\partial y}=\dfrac{\partial^2f}{\partial y\,\partial x}$.
:::

Die Stetigkeit ist nötig: Für $f=xy(x^2-y^2)/(x^2+y^2)$ mit $f(0,0)=0$ haben die beiden gemischten Ableitungen im Nullpunkt die Werte $1$ und $-1$.

Damit gilt die Kette: stetig differenzierbar $\Rightarrow$ differenzierbar $\Rightarrow$ alle partiellen Ableitungen existieren. Beide Pfeile lassen sich nicht umkehren. Das Gegenbeispiel oben zeigt es für den zweiten, Aufgabe [2](#aufg-2) für den ersten.

:::frage Muss ich immer den Grenzwert [(2.1)](#gl-2-1) rechnen?
Nein. Besteht $\boldsymbol f$ aus Polynomen, $\mathrm{e}$-Funktion, Sinus und ähnlichen Bausteinen, sind die partiellen Ableitungen stetig, und Satz [2.3](#satz-2-3) erledigt alles. Den Grenzwert braucht man an Sonderstellen, an denen die Formel abschnittsweise definiert ist oder ein Nenner null wird.
:::

:::aufgabe Aufgabe 2 ★★ Differenzierbar nach Definition
<span class="anker" id="aufg-2"></span>

Sei $f(x,y)=5+3x-2y+\rho^2\cos(1/\rho^2)$ mit $\rho^2=x^2+y^2$ für $(x,y)\neq(0,0)$ und $f(0,0)=5$.

<ol class="al">

<li>

Zeige mit [(2.1)](#gl-2-1), dass $f$ im Nullpunkt differenzierbar ist, und gib $A$ an.

</li>

<li>

Zeige, dass $\partial f/\partial x$ im Nullpunkt nicht stetig ist. Betrachte dazu die Punkte $(x,0)$ mit $1/x^2=2\pi m+\frac\pi2$, $m\in\mathbb{N}$. Warum hilft Satz [2.3](#satz-2-3) hier nicht?

</li>

</ol>

:::loesung
(a) Es ist $f(x,y)-5-(3x-2y)=\rho^2\cos(1/\rho^2)$, und $|\boldsymbol{x}|=\rho$. Der Bruch aus [(2.1)](#gl-2-1) ist höchstens $\rho^2/\rho=\rho\to0$. Also ist $A=(3\;\;{-2})$. (b) Für $(x,y)\neq(0,0)$ ist $\partial f/\partial x=3+2x\cos(1/\rho^2)+\frac{2x}{\rho^2}\sin(1/\rho^2)$. An den Punkten $(x,0)$ mit $x>0$, $1/x^2=2\pi m+\frac\pi2$ ist $\cos(1/\rho^2)=0$ und $\sin(1/\rho^2)=1$, also $\partial f/\partial x=3+2/x$. Das wächst für $m\to\infty$ über alle Grenzen, während die Punkte gegen $0$ gehen. Satz [2.3](#satz-2-3) ist nur hinreichend: Seine Voraussetzung fehlt hier, die Aussage gilt trotzdem.
:::
:::

:::aufgabe Aufgabe 3 ★★ Stetig, aber nicht differenzierbar
<span class="anker" id="aufg-3"></span>

Sei $f(x,y)=x^2y/(x^2+y^2)$ für $(x,y)\neq(0,0)$ und $f(0,0)=0$. Zeige: $f$ ist im Nullpunkt stetig, beide partiellen Ableitungen existieren dort, aber $f$ ist dort nicht differenzierbar. Tipp: Welche Matrix käme als $A$ in Frage? Prüfe den Bruch aus [(2.1)](#gl-2-1) längs $(t,t)$.

:::loesung
Stetig: Wegen $x^2\le x^2+y^2$ ist $|f(x,y)|\le|y|\to0$. Partielle Ableitungen: $f(x,0)=0$ und $f(0,y)=0$, also sind beide null, und nur $A=0$ kommt in Frage. Längs $(t,t)$ mit $t>0$ ist $f(t,t)=t/2$ und $|(t,t)|=\sqrt2\,t$. Der Bruch ist $\frac{t/2}{\sqrt2\,t}=\frac1{2\sqrt2}$ und geht nicht gegen null.
:::
:::
