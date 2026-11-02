---
title: Stufe 7: Wann ein Feld eine Rotation ist
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3150800
summary: Aus Teil 3 weißt du, wann ein Feld ein Gradient ist.
tags: Rotationsfeld, Vektorpotential
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Aus [Teil 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html) weißt du, wann ein Feld ein Gradient ist. Die entsprechende Frage für Rotationen führt auf eine andere Art von Loch im Gebiet.
:::

**Die Idee.** Ein Feld $\boldsymbol{F}$ heißt __Rotationsfeld__, wenn $\boldsymbol{F}=\operatorname{rot}\boldsymbol{A}$ für ein __Vektorpotential__ $\boldsymbol{A}$ gilt. Dann ist zwingend $\operatorname{div}\boldsymbol{F}=0$, denn $\operatorname{div}\operatorname{rot}=0$. Die Umkehrung gilt nicht überall. Beim Gradienten stört ein Loch, um das eine geschlossene *Kurve* läuft. Bei der Rotation stört ein Loch, das von einer geschlossenen *Fläche* eingeschlossen wird (Abb. [6](#abb-6)).

:::abbildung hm3/k5loecher 6
Links: Fehlt der Nullpunkt, lässt sich jede geschlossene Kurve zusammenziehen, aber die Kugelfläche um das Loch nicht. Rechts: Fehlt die $z$-Achse, lässt sich der Kreis um die Achse nicht zusammenziehen, jede Fläche aber schon. Die eine Sorte Loch verhindert Rotationsfelder, die andere Gradientenfelder.
:::

**Beispiel 1: die Punktladung.** Auf $\mathcal U=\mathbb{R}^3\setminus\{0\}$ sei

<span class="anker" id="gl-7-1"></span>
$$\boldsymbol{E}(\boldsymbol{x})=\frac{Q}{4\pi r^2}\,\hat{\boldsymbol{e}}_r. \tag{7.1}$$

Dieses Gebiet ist einfach zusammenhängend, jede geschlossene Kurve lässt sich am Nullpunkt vorbei zusammenziehen. Wegen $\operatorname{rot}\boldsymbol{E}=0$ ist $\boldsymbol{E}$ ein Gradient, und zwar $\boldsymbol{E}=-\nabla\phi$ mit $\phi=Q/(4\pi r)$. Außerdem ist $\operatorname{div}\boldsymbol{E}=0$ auf $\mathcal U$. Ist $\boldsymbol{E}$ also auch eine Rotation? Der Fluss durch die Kugel $S_R$ mit Radius $R$ ist

$$\int_{S_R}\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=\frac{Q}{4\pi R^2}\int_{S_R}\mathrm{d}\sigma=Q\neq0.$$

Wäre $\boldsymbol{E}=\operatorname{rot}\boldsymbol{A}$, zerlegt man $S_R$ in obere und untere Halbkugel. Beide haben den Äquator $\Gamma_R$ als Rand, aber mit entgegengesetztem Umlauf. Nach Stokes ergäbe das

$$\int_{S_R}\operatorname{rot}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{S}=\int_{\Gamma_R}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{x}+\int_{-\Gamma_R}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{x}=0,$$

ein Widerspruch. Also ist $\boldsymbol{E}$ keine Rotation.

**Beispiel 2: der stromdurchflossene Draht.** Auf $\mathcal U=\mathbb{R}^3\setminus\{x^2+y^2=0\}$, also ohne die $z$-Achse, sei

<span class="anker" id="gl-7-2"></span>
$$\boldsymbol{H}(x,y,z)=\frac{1}{x^2+y^2}\begin{pmatrix}-y\\x\\0\end{pmatrix}. \tag{7.2}$$

Hier ist $\operatorname{rot}\boldsymbol{H}=0$, aber $\boldsymbol{H}$ ist nicht konservativ, das Integral um die Achse ist $2\pi$. Das Gebiet ist eben nicht einfach zusammenhängend. Zugleich gilt $\operatorname{div}\boldsymbol{H}=0$, und $\boldsymbol{H}$ ist tatsächlich eine Rotation: $\boldsymbol{H}=\operatorname{rot}\boldsymbol{A}$ mit $\boldsymbol{A}=-\ln\sqrt{x^2+y^2}\;\hat{\boldsymbol{e}}_3$.

:::satz Satz 7.1 (Hinreichende Bedingung für Rotationsfelder)
<span class="anker" id="satz-7-1"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ ein Gebiet, in dem jede geschlossene stückweise reguläre Fläche $\mathcal F\subset\mathcal U$ Rand eines regulären Bereichs $V\subset\mathcal U$ ist, und $\boldsymbol{F}$ stetig differenzierbar auf $\mathcal U$. Dann gilt

<span class="anker" id="gl-7-3"></span>
$$\boldsymbol{F}\text{ ist Rotationsfeld in }\mathcal U\iff\operatorname{div}\boldsymbol{F}=0\text{ in }\mathcal U. \tag{7.3}$$
:::

Der Satz wird hier ohne Beweis benutzt. Die Tabelle stellt beide Fragen gegenüber.

|  | Gradientenfeld $\boldsymbol{F}=\nabla\varphi$ | Rotationsfeld $\boldsymbol{F}=\operatorname{rot}\boldsymbol{A}$ |
|---|---|---|
| notwendig | $\operatorname{rot}\boldsymbol{F}=0$ | $\operatorname{div}\boldsymbol{F}=0$ |
| hinreichend, wenn | jede geschlossene Kurve zusammenziehbar | jede geschlossene Fläche berandet einen Körper im Gebiet |
| störendes Loch | Achse (Beispiel 2) | Punkt (Beispiel 1) |
| Test am Loch | $\oint\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}\neq0$ | $\oint\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}\neq0$ |

:::frage Beispiel 1 hat doch $\operatorname{div}\boldsymbol{E}=0$ und den Fluss $Q$. Widerspricht das nicht Gauß?
Nein, denn die Kugel enthält den Nullpunkt, und dort ist $\boldsymbol{E}$ nicht definiert. Gauß darf man auf die Kugel nicht anwenden. Physikalisch sitzt die Quelle genau im herausgenommenen Punkt, Stufe [9](poisson-gleichung.html#stufe-9) macht das exakt.
:::

:::aufgabe Aufgabe 10 ★★ Vektorpotential finden
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Warum ist $\boldsymbol{F}=(x,y,z)$ auf $\mathbb{R}^3$ keine Rotation?

</li>

<li>

Zeige, dass $\boldsymbol{F}=(y,z,x)$ eine Rotation ist, und finde ein Vektorpotential der Form $\boldsymbol{A}=(0,a,b)$.

</li>

</ol>

:::loesung
(a) $\operatorname{div}\boldsymbol{F}=3\neq0$, aber jede Rotation ist divergenzfrei. (b) $\operatorname{div}\boldsymbol{F}=0$ und $\mathbb{R}^3$ erfüllt die Bedingung von Satz [7.1](#satz-7-1). Mit $\boldsymbol{A}=(0,a,b)$ ist $\operatorname{rot}\boldsymbol{A}=(b_y-a_z,\;-b_x,\;a_x)$. Aus $a_x=x$ folgt $a=x^2/2$. Aus $-b_x=z$ folgt $b=-xz+c(y,z)$. Die erste Gleichung gibt dann $c_y=y$, also $c=y^2/2$. Ergebnis: $\boldsymbol{A}=(0,\;x^2/2,\;y^2/2-xz)$. Die Probe bestätigt $\operatorname{rot}\boldsymbol{A}=(y,z,x)$.
:::
:::
