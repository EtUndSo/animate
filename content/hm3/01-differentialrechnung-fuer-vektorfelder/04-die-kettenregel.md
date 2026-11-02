---
title: Stufe 3: Die Kettenregel
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110400
summary: Setzt man eine Abbildung in eine andere ein, wie ändert sich das Ergebnis?
tags: Richtungsableitung, Höhenlinie
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Setzt man eine Abbildung in eine andere ein, wie ändert sich das Ergebnis? Die Antwort liefert die Änderung einer Funktion längs einer Kurve und erklärt, wohin der Gradient zeigt.
:::

**Die Idee.** Nahe einem Punkt verhält sich jede differenzierbare Abbildung wie ihre Jacobi-Matrix. Hintereinander ausgeführte lineare Abbildungen ergeben das Matrixprodukt. Also muss die Ableitung der Verkettung das Produkt der Jacobi-Matrizen sein.

:::satz Satz 3.1 (Kettenregel)
<span class="anker" id="satz-3-1"></span>

Sei $f=f(y_1,\dots,y_m)$ eine differenzierbare Funktion und $\boldsymbol{g}=(g_1,\dots,g_m)$ eine differenzierbare Abbildung in $\boldsymbol{x}=(x_1,\dots,x_n)$. Dann ist die Verkettung $(f\circ\boldsymbol{g})(\boldsymbol{x})=f(\boldsymbol{g}(\boldsymbol{x}))$, falls definiert, differenzierbar mit

<span class="anker" id="gl-3-1"></span>
$$\frac{\partial(f\circ\boldsymbol{g})}{\partial x_k}(\boldsymbol{x})=\sum_{j=1}^m\frac{\partial f}{\partial y_j}(\boldsymbol{g}(\boldsymbol{x}))\,\frac{\partial g_j}{\partial x_k}(\boldsymbol{x}). \tag{3.1}$$

Für Abbildungen $\boldsymbol f=(f_1,\dots,f_N)$ gilt entsprechend $\frac{\partial(\boldsymbol f\circ\boldsymbol{g})_i}{\partial x_k}(\boldsymbol{x})=\sum_{j=1}^m\frac{\partial f_i}{\partial y_j}(\boldsymbol{g}(\boldsymbol{x}))\,\frac{\partial g_j}{\partial x_k}(\boldsymbol{x})$, geschrieben als Matrixprodukt:

<span class="anker" id="gl-3-2"></span>
$$D(\boldsymbol f\circ\boldsymbol{g})(\boldsymbol{x})=D\boldsymbol f(\boldsymbol{g}(\boldsymbol{x}))\,D\boldsymbol{g}(\boldsymbol{x}). \tag{3.2}$$
:::

⁠**So liest man das:** Ändert man $x_k$, ändern sich alle Zwischengrößen $y_j=g_j(\boldsymbol{x})$, und jede wirkt über ihren Hebel $\partial f/\partial y_j$ auf $f$. Die Summe läuft über alle Wege $x_k\to y_j\to f$. Das ist genau Zeile mal Spalte. Die Formate passen: $N\times m$ mal $m\times n$ ergibt $N\times n$. Wichtig: $D\boldsymbol f$ wird an der Stelle $\boldsymbol{g}(\boldsymbol{x})$ ausgewertet, nicht an der Stelle $\boldsymbol{x}$.

:::herleitung Fehler durch Fehler
Setze $\boldsymbol{y}=\boldsymbol{g}(\boldsymbol{x})$. Es ist $\boldsymbol{g}(\boldsymbol{x}+\boldsymbol s)-\boldsymbol{y}=D\boldsymbol{g}(\boldsymbol{x})\,\boldsymbol s+\boldsymbol r_1$ und $\boldsymbol f(\boldsymbol{y}+\boldsymbol w)-\boldsymbol f(\boldsymbol{y})=D\boldsymbol f(\boldsymbol{y})\,\boldsymbol w+\boldsymbol r_2$, wobei die Reste $\boldsymbol r_1,\boldsymbol r_2$ schneller verschwinden als $|\boldsymbol s|$ und $|\boldsymbol w|$. Mit $\boldsymbol w=\boldsymbol{g}(\boldsymbol{x}+\boldsymbol s)-\boldsymbol{y}$ folgt

$$\boldsymbol f(\boldsymbol{g}(\boldsymbol{x}+\boldsymbol s))-\boldsymbol f(\boldsymbol{y})=D\boldsymbol f(\boldsymbol{y})\,D\boldsymbol{g}(\boldsymbol{x})\,\boldsymbol s+D\boldsymbol f(\boldsymbol{y})\,\boldsymbol r_1+\boldsymbol r_2.$$

Beide Reste verschwinden schneller als $|\boldsymbol s|$, weil $|\boldsymbol w|$ für kleine $\boldsymbol s$ höchstens ein festes Vielfaches von $|\boldsymbol s|$ ist. Nach Satz [2.2](differenzierbar-heit-linear-genahert.html#satz-2-2) ist die Matrix vor $\boldsymbol s$ die Jacobi-Matrix der Verkettung.
:::

**Der wichtigste Fall: längs einer Kurve.** Für eine differenzierbare Funktion $u$ auf $\mathcal U\subset\mathbb{R}^n$ und eine differenzierbare Kurve $\gamma:[a,b]\to\mathcal U$ gibt [(3.1)](#gl-3-1) das Skalarprodukt

<span class="anker" id="gl-3-3"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}\,u(\gamma(t))=\nabla u(\gamma(t))\cdot\dot\gamma(t). \tag{3.3}$$

Für die Schale längs $\gamma(t)=(\cos t,\sin t)$ ist $\nabla\varphi\cdot\dot\gamma=2\cos t\,(-\sin t)+4\sin t\cos t=2\sin t\cos t$. Direkt: $\varphi(\gamma(t))=1+\sin^2t$ hat dieselbe Ableitung. **Grenzfall:** Für $n=1$ und $\gamma(t)=t$ bleibt $u'(t)$. Die Differenzierbarkeit von $u$ ist nötig: Für $f$ aus Aufgabe [3](differenzierbar-heit-linear-genahert.html#aufg-3) und $\gamma(t)=(t,t)$ ist $f(\gamma(t))=t/2$ mit der Ableitung $\frac12$, die rechte Seite von [(3.3)](#gl-3-3) ist bei $t=0$ aber null.

**Wohin der Gradient zeigt.** Die __Richtungsableitung__ von $u$ in Richtung eines Einheitsvektors $\boldsymbol v$ ist die Ableitung längs der Geraden $\gamma(t)=\boldsymbol{x}+t\boldsymbol v$. Nach [(3.3)](#gl-3-3) ist sie

<span class="anker" id="gl-3-4"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}\,u(\boldsymbol{x}+t\boldsymbol v)\Big|_{t=0}=\nabla u(\boldsymbol{x})\cdot\boldsymbol v=|\nabla u(\boldsymbol{x})|\cos\alpha, \tag{3.4}$$

wobei $\alpha$ der Winkel zwischen $\nabla u$ und $\boldsymbol v$ ist. Am größten wird das für $\alpha=0$: *Der Gradient zeigt in die Richtung des steilsten Anstiegs, und $|\nabla u|$ ist diese Steigung.* Läuft eine Kurve auf einer __Höhenlinie__, also einer Linie mit konstantem $u$, ist die linke Seite von [(3.3)](#gl-3-3) null: *Der Gradient steht senkrecht auf den Höhenlinien* (Abb. [3](#abb-3)).

:::abbildung hm3/k1gradient 3
Höhenlinien der Schale $\varphi=x^2+2y^2$ mit Gradientenpfeilen auf der Linie $\varphi=3$. Im Punkt $(1,1)$ ist $\nabla\varphi=(2,4)$, gezeichnet in verkleinertem Maßstab. Die Kurve $\gamma$ schneidet die Höhenlinien, und [(3.3)](#gl-3-3) sagt, wie schnell $\varphi$ dabei wächst.
:::

:::frage Der Berg ist dreidimensional. Warum zeigt der Gradient dann in der Ebene?
Der Gradient von $\varphi(x,y)$ hat zwei Komponenten, er lebt im Eingangsraum, also in der $x$-$y$-Ebene. Er ist die Richtung, in die du auf der Landkarte gehen musst, nicht ein Pfeil auf dem Hang. Deshalb steht er in der Karte senkrecht auf den Höhenlinien.
:::

:::aufgabe Aufgabe 4 ★ Richtung und Kurve
<span class="anker" id="aufg-4"></span>

Sei $u(x,y)=x^2y-y^2$.

<ol class="al">

<li>

Berechne die Richtungsableitung in $(2,1)$ in Richtung $\boldsymbol v=\frac15(3,4)$. In welcher Richtung steigt $u$ dort am stärksten, wie groß ist diese Steigung, und in welche Richtung bleibt $u$ gleich?

</li>

<li>

Berechne $\frac{\mathrm{d}}{\mathrm{d} t}u(\gamma(t))$ für $\gamma(t)=(t^2,t)$ mit [(3.3)](#gl-3-3) und zur Kontrolle durch Einsetzen.

</li>

<li>

Gib die Tangentialebene an den Graphen von $u$ über dem Punkt $(2,1)$ an.

</li>

</ol>

:::loesung
(a) $\nabla u=(2xy,\;x^2-2y)$, also $\nabla u(2,1)=(4,2)$. Die Richtungsableitung ist $\frac15(12+8)=4$. Am stärksten steigt $u$ in Richtung $(4,2)/|(4,2)|=(2,1)/\sqrt5$, die Steigung ist $|(4,2)|=2\sqrt5\approx4{,}47$. Gleich bleibt $u$ senkrecht dazu, in Richtung $\pm(-1,2)/\sqrt5$. (b) $\nabla u(\gamma)=(2t^3,\;t^4-2t)$ und $\dot\gamma=(2t,1)$ geben $4t^4+t^4-2t=5t^4-2t$. Einsetzen: $u(\gamma(t))=t^5-t^2$ hat dieselbe Ableitung. (c) $u(2,1)=3$, also $z=3+4(x-2)+2(y-1)=4x+2y-7$.
:::
:::

:::aufgabe Aufgabe 5 ★★ Kettenregel als Matrixprodukt
<span class="anker" id="aufg-5"></span>

Sei $\boldsymbol{g}(s,t)=(s+t,\;st)$ und $\boldsymbol f(y_1,y_2)=(y_1y_2,\;y_1^2)$. Berechne $D(\boldsymbol f\circ\boldsymbol{g})(1,1)$ mit [(3.2)](#gl-3-2) und zur Kontrolle direkt.

:::loesung
$\boldsymbol{g}(1,1)=(2,1)$. Es ist $D\boldsymbol f(y)=\begin{pmatrix}y_2&y_1\\2y_1&0\end{pmatrix}$ und $D\boldsymbol{g}(s,t)=\begin{pmatrix}1&1\\t&s\end{pmatrix}$, also

$$D(\boldsymbol f\circ\boldsymbol{g})(1,1)=\begin{pmatrix}1&2\\4&0\end{pmatrix}\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}3&3\\4&4\end{pmatrix}.$$

Direkt: $\boldsymbol f\circ\boldsymbol{g}=((s+t)st,\;(s+t)^2)$ hat die Ableitungen $(2st+t^2,\;s^2+2st)$ und $(2(s+t),\;2(s+t))$, bei $(1,1)$ also dieselbe Matrix.
:::
:::
