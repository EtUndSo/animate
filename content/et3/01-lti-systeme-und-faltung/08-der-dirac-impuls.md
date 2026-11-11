---
title: Stufe 7: Der Dirac-Impuls
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210800
summary: Der Dirac-Impuls ist das Grenzobjekt aus Stufe 4.
tags: Distribution, ideales Laufzeitglied, verallgemeinerte Differentiation
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Der Dirac-Impuls ist das Grenzobjekt aus Stufe [4](das-faltungsintegral.html#stufe-4). Er ist keine gewöhnliche Funktion. Alle seine Eigenschaften folgen daraus, dass er nur über seine Fläche wirkt.
:::

**Was $\delta$ ist und was nicht.** Die Rechtecke $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ werden für $T_0\to0$ immer schmaler und höher, ihre Fläche bleibt 1 (Abb. [8](#abb-8)). Einen Grenzwert im Sinne gewöhnlicher Funktionen gibt es nicht: Eine Funktion, die überall außer in einem Punkt null ist, hat die Fläche null, egal welchen Wert sie in diesem Punkt hat. $\delta(t)$ ist deshalb eine __Distribution__: ein Objekt, das nur durch seine Wirkung unter einem Integral festgelegt ist, nämlich durch [(4.1)](das-faltungsintegral.html#gl-4-1). Gezeichnet wird es als Pfeil, dessen Höhe das Gewicht (die Fläche) angibt.

:::abbildung et3/k1dirac 8
Links: Rechtecke der Fläche 1, immer schmaler und höher. Rechts: das Symbol des Grenzobjekts. Die Pfeilhöhe ist das Gewicht, nicht der Funktionswert.
:::

:::satz Satz 7.1 (Eigenschaften des Dirac-Impulses)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{Gewicht:} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{Sieb:} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{Fläche:} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{Dehnung:} && \delta(bt)=\frac{1}{|b|}\,\delta(t)\quad(b\neq0),\qquad \delta(-t)=\delta(t),\\ &\text{Verschiebung:} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{Integral:} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**So liest man das:** Das Produkt $s(t)\,\delta(t-T)$ kann nur an der Stelle $T$ etwas bewirken, also zählt nur $s(T)$. Ein gestauchter Impuls $\delta(bt)$ ist zwar genauso „unendlich hoch“, hat aber nur noch die Fläche $1/|b|$. Ein System mit $h(t)=\delta(t-t_0)$ verzögert jedes Signal um $t_0$, es heißt __ideales Laufzeitglied__. Und weil der Sprung das laufende Integral des Stoßes ist, darf man Funktionen mit Sprungstellen ableiten: Ein Sprung der Höhe $A$ wird zu $A\,\delta$. Das heißt __verallgemeinerte Differentiation__. Vorsicht: Viele Operationen, etwa das Quadrieren $\delta^2$, sind für Dirac-Impulse nicht definiert.

:::herleitung Dehnung und Sieb-Produkt
⁠**Dehnung.** Für $b>0$ mit $\vartheta=b\tau$:

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

Für $b<0$ kehrt die Substitution die Integrationsrichtung um, es kommt $-\frac1b=\frac{1}{|b|}$ heraus. Also wirkt $\delta(bt)$ wie $\frac1{|b|}\delta(t)$. Mit $b=-1$ folgt die Symmetrie $\delta(-t)=\delta(t)$.

⁠**Sieb-Produkt.** Faltet man $s(t)\delta(t)$ mit einem beliebigen $g(t)$, ergibt die Siebeigenschaft

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

Beide wirken auf jedes $g$ gleich, also $s(t)\delta(t)=s(0)\delta(t)$. Mit Verschiebung folgt $s(t)\delta(t-T)=s(T)\delta(t-T)$.

⁠**Integral.** $\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$, und $\varepsilon(t-\tau)=1$ genau für $\tau\le t$.
:::

:::frage $\delta(0)$ ist doch unendlich. Dann ist $\delta(2t)$ dasselbe wie $\delta(t)$, oder?
Nein. „Unendlich hoch“ beschreibt $\delta$ nicht, denn alle Funktionswerte außer bei $0$ sind gleich, und der Wert bei $0$ ist keine Zahl. Was $\delta$ ausmacht, ist seine Fläche. Staucht man das Rechteck der Fläche 1 auf die halbe Breite und lässt die Höhe gleich, halbiert sich die Fläche. Deshalb ist $\delta(2t)=\frac12\delta(t)$.
:::

:::aufgabe Aufgabe 8 ★ Rechnen mit $\delta$
<span class="anker" id="aufg-8"></span>

Berechne: (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$, (b) $\mathrm{e}^{-t}\,\delta(t-1)$, (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$, (d) $\delta(t)*\delta(t-3)$, (e) $\operatorname{rect}(t)*\delta(t-1)$, (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$.

:::loesung
(a) $\mathrm{e}^{-2}=0{,}135$. (b) $\mathrm{e}^{-1}\,\delta(t-1)$. (c) $\tfrac12$. (d) $\delta(t-3)$. (e) $\operatorname{rect}(t-1)$. (f) $3\,\delta(t-1)$.
:::
:::

::::kurzfassung
Der Dirac-Impuls ist keine gewöhnliche Funktion. Alle seine Eigenschaften folgen daraus, dass er nur über seine Fläche wirkt.

Die Rechtecke $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ werden für $T_0\to0$ immer schmaler und höher, ihre Fläche bleibt 1. Einen Grenzwert im Sinne gewöhnlicher Funktionen gibt es nicht, denn eine Funktion, die überall außer in einem Punkt null ist, hat die Fläche null. $\delta(t)$ ist deshalb eine __Distribution__: ein Objekt, das nur durch seine Wirkung unter einem Integral festgelegt ist. Man zeichnet es als Pfeil, dessen Höhe das Gewicht angibt, also die Fläche. Die wichtigsten Regeln sind das Sieb-Produkt und die Dehnung:

$$s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\qquad \delta(bt)=\frac{1}{|b|}\,\delta(t).$$

Dazu kommen $\delta(-t)=\delta(t)$ und $\delta(t-t_0)*s(t)=s(t-t_0)$. Ein System mit $h(t)=\delta(t-t_0)$ verzögert also jedes Signal um $t_0$; es heißt __ideales Laufzeitglied__. Aus $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t)$ folgt: Ein Sprung der Höhe $A$ wird beim Ableiten zu $A\,\delta$. Dieses Ableiten über Sprungstellen hinweg heißt __verallgemeinerte Differentiation__.

Der Grund für die Dehnung: Staucht man das Rechteck der Fläche 1 auf die halbe Breite und lässt die Höhe gleich, halbiert sich die Fläche. Das Produkt $s(t)\,\delta(t-T)$ kann nur an der Stelle $T$ etwas bewirken, also zählt nur $s(T)$.

Falle: „Unendlich hoch“ beschreibt $\delta$ nicht. Deshalb ist $\delta(2t)$ nicht dasselbe wie $\delta(t)$, sondern $\frac12\delta(t)$. Manche Operationen, etwa das Quadrieren $\delta^2$, sind gar nicht definiert.
::::

::::formelsammlung
**Rechtecke der Fläche 1**

$$\frac{1}{T_0}\operatorname{rect}(t/T_0)$$

Für $T_0\to0$ immer schmaler und höher, Fläche stets 1. Einen gewöhnlichen Grenzwert gibt es nicht; $\delta(t)$ ist eine Distribution, festgelegt durch $s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$.

**Gewicht**

$$[a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t)$$

$a$, $a_1$, $a_2$ Konstanten. Gezeichnet als Pfeil, dessen Höhe das Gewicht (die Fläche) angibt.

**Siebeigenschaft**

$$\int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T)$$

Das Produkt mit $\delta(t-T)$ wirkt nur an der Stelle $T$; es zählt nur $s(T)$.

**Fläche**

$$\int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a$$

$a$ konstant.

**Dehnung**

$$\delta(bt)=\frac{1}{|b|}\,\delta(t),\qquad \delta(-t)=\delta(t)$$

$b$ reell, $b\ne0$. Der gestauchte Impuls hat nur noch die Fläche $1/|b|$.

**Verschiebung**

$$\delta(t-t_0)*s(t)=s(t-t_0)$$

Ein System mit $h(t)=\delta(t-t_0)$ verzögert jedes Signal um $t_0$: ideales Laufzeitglied.

**Sprung als Integral des Dirac-Impulses**

$$\varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t)$$

Verallgemeinerte Differentiation: Ein Sprung der Höhe $A$ wird beim Ableiten zu $A\,\delta$. Nicht definiert sind viele Operationen, etwa $\delta^2$.
::::
