---
title: Stufe 6: Der Satz von Stokes
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Integralsätze im Raum
adresse: elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum
knoten: Kapitel 5: Integralsätze im Raum
order: 3150700
summary: Die Rotation misst die Wirbelstärke in einem Punkt.
tags: Rechtsschraube, Zirkulation
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Rotation misst die Wirbelstärke in einem Punkt. Diese Stufe zeigt, wie sich viele kleine Wirbel über eine Fläche zur Zirkulation am Rand summieren.
:::

**Die Idee.** Zerlege die Fläche in kleine Zellen und laufe um jede einmal herum (Abb. [4](#abb-4)). Das Kurvenintegral um eine Zelle ist fast $\operatorname{rot}\boldsymbol{F}\cdot\boldsymbol{n}$ mal Zellfläche, das ist der Inhalt von Green im Kleinen. Summiert man alle Zellen, wird jede Innenkante zweimal durchlaufen, einmal von jeder Nachbarzelle und in entgegengesetzter Richtung. Diese Beiträge heben sich auf. Übrig bleibt der äußere Rand. Die Form der Fläche spielt dabei keine Rolle, nur ihr Rand.

:::abbildung hm3/k5zellen 4
Links die Zellen mit ihrem Umlaufsinn. Auf jeder Innenkante laufen zwei Pfeile gegeneinander, ihre Beiträge heben sich auf. Rechts das Ergebnis: Nur der Umlauf um den Rand bleibt.
:::

:::satz Satz 6.1 (Stokes im Raum)
<span class="anker" id="satz-6-1"></span>

Sei $\mathcal F$ ein orientiertes reguläres Flächenstück mit Normalenfeld $\boldsymbol{n}$ und $\boldsymbol{F}$ stetig differenzierbar in einer Umgebung von $\mathcal F$. Dann gilt

<span class="anker" id="gl-6-1"></span>
$$\int_{\mathcal F}\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=\int_{\partial\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}, \tag{6.1}$$

wobei $\partial\mathcal F$ so durchlaufen wird, dass der Umlauf mit $\boldsymbol{n}$ eine __Rechtsschraube__ bildet: Zeigt der Daumen der rechten Hand in Richtung $\boldsymbol{n}$, zeigen die Finger in Laufrichtung.
:::

⁠**So liest man das:** Links steht die summierte Wirbelstärke quer durch die Fläche, rechts die __Zirkulation__, also die Arbeit des Felds auf einer Runde um den Rand. Ist $\Phi:B\to\mathbb{R}^3$ orientierungstreu und läuft $\partial B$ positiv, also gegen den Uhrzeigersinn, so durchläuft das Bild $\Phi\circ\gamma$ den Rand in der richtigen Richtung. Eine Kurve hat zwei Laufrichtungen, die Fläche zwei Seiten, die Rechtsschraube koppelt beide (Abb. [5](#abb-5)).

:::abbildung hm3/k5kuppel 5
Kuppel und Bodenscheibe haben denselben Rand. Mit $\boldsymbol{n}$ nach oben läuft der Rand von oben gesehen gegen den Uhrzeigersinn. Deshalb haben beide Flächen dasselbe Integral von $\operatorname{rot}\boldsymbol{F}$, im Modell $8\pi$.
:::

:::beweis Zurückführen auf Green in der Ebene (für zweimal stetig differenzierbares $\Phi$)
Sei $\Phi:B\to\mathbb{R}^3$ orientierungstreu. Setze auf $B$ das ebene Feld

$$P(u,v):=\boldsymbol{F}(\Phi)\cdot\Phi_u,\qquad Q(u,v):=\boldsymbol{F}(\Phi)\cdot\Phi_v.$$

⁠**Schritt 1.** Mit der Kettenregel ist $Q_u=(D\boldsymbol{F}\,\Phi_u)\cdot\Phi_v+\boldsymbol{F}\cdot\Phi_{vu}$ und $P_v=(D\boldsymbol{F}\,\Phi_v)\cdot\Phi_u+\boldsymbol{F}\cdot\Phi_{uv}$. Die zweiten Ableitungen sind nach Schwarz gleich und fallen in der Differenz weg:

$$Q_u-P_v=(D\boldsymbol{F}\,\Phi_u)\cdot\Phi_v-(D\boldsymbol{F}\,\Phi_v)\cdot\Phi_u=\Phi_v\cdot\bigl((D\boldsymbol{F}-D\boldsymbol{F}^T)\,\Phi_u\bigr).$$

⁠**Schritt 2.** Die Matrix $D\boldsymbol{F}-D\boldsymbol{F}^T$ ist schiefsymmetrisch, und es gilt $(D\boldsymbol{F}-D\boldsymbol{F}^T)\boldsymbol w=\operatorname{rot}\boldsymbol{F}\times\boldsymbol w$. Das Spatprodukt lässt sich zyklisch tauschen:

$$Q_u-P_v=\Phi_v\cdot(\operatorname{rot}\boldsymbol{F}\times\Phi_u)=\operatorname{rot}\boldsymbol{F}(\Phi)\cdot(\Phi_u\times\Phi_v).$$

⁠**Schritt 3.** Mit [(4.2)](orientierung-und-flussintegral.html#gl-4-2) und Green in der Ebene folgt

$$\int_{\mathcal F}\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=\int_B(Q_u-P_v)\,\mathrm{d} u\,\mathrm{d} v=\int_{\partial B}P\,\mathrm{d} u+Q\,\mathrm{d} v.$$

⁠**Schritt 4.** Die Kettenregel gibt $\mathrm{d}\boldsymbol{x}=\Phi_u\,\mathrm{d} u+\Phi_v\,\mathrm{d} v$, also $P\,\mathrm{d} u+Q\,\mathrm{d} v=\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$. Damit steht rechts das Kurvenintegral über $\partial\mathcal F$.
:::

::::beispiel Kuppel
Für $\boldsymbol{F}=(-y,x,2z)$ ist $\operatorname{rot}\boldsymbol{F}=(0,0,2)$. Mit [(1.3)](flachen-beschreiben.html#gl-1-3) ist $\operatorname{rot}\boldsymbol{F}\cdot(\Phi_r\times\Phi_\varphi)=2r$, das Flächenintegral also $\int_0^{2\pi}\!\int_0^22r\,\mathrm{d} r\,\mathrm{d}\varphi=8\pi$. Der Rand $\gamma(t)=(2\cos t,2\sin t,0)$ läuft von oben gesehen gegen den Uhrzeigersinn, passt also zu $\boldsymbol{n}$ nach oben. Es ist $\boldsymbol{F}(\gamma)\cdot\dot\gamma=4\sin^2t+4\cos^2t=4$, das Randintegral also $2\pi\cdot4=8\pi$. Beide Seiten stimmen.
::::

**Der wichtigste Trick.** Das Ergebnis hängt nur vom Rand ab. Hat man ein hässliches $\int_{\mathcal F}\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$, gibt es zwei Auswege: das Randintegral rechnen oder die Fläche durch eine einfachere mit demselben Rand ersetzen, etwa die Bodenscheibe. Dort ist $\boldsymbol{n}=(0,0,1)$, und der Integrand vereinfacht sich oft stark. Komponenten, die auf dem Rand verschwinden, spielen gar keine Rolle.

:::frage Woran erkenne ich, dass Stokes gemeint ist?
Am Ausdruck $\operatorname{rot}\boldsymbol{F}$ unter einem Flächenintegral, oder an einem Kurvenintegral über eine geschlossene Kurve mit unbequemer Parametrisierung. Ein Feld mit langen Exponential- oder Sinusausdrücken ist fast immer ein Signal: Direkt rechnen soll man nicht.
:::

:::zusatz Stokes in der Elektrotechnik
Das Durchflutungsgesetz $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{x}=I$ und das Induktionsgesetz $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{x}=-\mathrm{d}\Phi/\mathrm{d} t$ sind Stokes angewandt auf $\operatorname{rot}\boldsymbol{H}=\boldsymbol J$ und $\operatorname{rot}\boldsymbol{E}=-\partial_t\boldsymbol B$. Dass die Fläche beliebig gewählt werden darf, ist genau die Unabhängigkeit vom Flächeninneren.
:::

:::aufgabe Aufgabe 8 ★★ Hässliches Feld, einfacher Rand
<span class="anker" id="aufg-8"></span>

Sei $S$ der Graph $z=1-x^2-y^2$, $z\ge0$, mit $\boldsymbol{n}$ nach oben, und $\boldsymbol{F}=\bigl(z\,\mathrm{e}^{y^2}-y,\;\;x+z\sin(xy),\;\;\mathrm{e}^{xy}\bigr)$. Berechne $\int_S\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$. Welche Komponenten von $\boldsymbol{F}$ spielen auf dem Rand eine Rolle?

:::loesung
Der Rand ist der Einheitskreis in $z=0$, von oben gesehen gegen den Uhrzeigersinn: $\gamma(t)=(\cos t,\sin t,0)$. Dort ist $z=0$, also $\boldsymbol{F}=(-y,\;x,\;\mathrm{e}^{xy})$. Die dritte Komponente spielt keine Rolle, weil $\dot\gamma$ keine $z$-Komponente hat. Damit ist $\boldsymbol{F}\cdot\dot\gamma=\sin^2t+\cos^2t=1$ und $\int_S\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=2\pi$.
:::
:::

:::aufgabe Aufgabe 9 ★★★ Elliptischer Rand
<span class="anker" id="aufg-9"></span>

Sei $S$ die Fläche $4x^2+y^2=4z$, $0\le z\le1$, mit $\boldsymbol{n}$ nach oben, und $\boldsymbol{F}=\bigl(-y\,z^2,\;x\,z^3,\;x^5y^4+z^7\bigr)$. Berechne $\int_S\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$. Tipp: Der Rand liegt in der Ebene $z=1$. Benutze dort Green für $-y\,\mathrm{d} x+x\,\mathrm{d} y$.

:::loesung
Bei $z=1$ ist der Rand die Ellipse $x^2+y^2/4=1$ mit den Halbachsen 1 und 2. Dort ist $\boldsymbol{F}=(-y,x,\dots)$, und die dritte Komponente spielt wieder keine Rolle. Green in der Ebene gibt $\oint-y\,\mathrm{d} x+x\,\mathrm{d} y=2\cdot\text{Fläche}=2\cdot2\pi=4\pi$. Die Richtung passt, denn $\boldsymbol{n}$ zeigt nach oben und der Rand läuft dann von oben gesehen gegen den Uhrzeigersinn. Ergebnis: $4\pi$.
:::
:::
