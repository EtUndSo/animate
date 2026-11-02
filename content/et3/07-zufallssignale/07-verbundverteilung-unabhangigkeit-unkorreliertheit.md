---
title: Stufe 6: Verbundverteilung, Unabhängigkeit, Unkorreliertheit
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Zufallssignale
order: 3270700
summary: Zwei Zufallsgrößen zugleich: Wann hängen sie zusammen, und was folgt daraus für ihre Summe?
tags: Verbundverteilung, statistisch unabhängig, unkorreliert
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Zwei Zufallsgrößen zugleich: Wann hängen sie zusammen, und was folgt daraus für ihre Summe?
:::

Die __Verbundverteilung__ zweier Größen ist $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{und}\ g\le y]$, ihre Dichte $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$. Daraus folgen die Einzelverteilungen ($P_{sg}(x,\infty)=P_s(x)$) und die Korrelation $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$. Bei verbunden stationären Prozessen hängt alles nur von der Zeitverschiebung $\tau$ zwischen $s(t)$ und $g(t+\tau)$ ab.

:::definition Definition 6.1 (Unabhängig, unkorreliert)
<span class="anker" id="satz-6-1"></span>

$s$ und $g$ heißen __statistisch unabhängig__, wenn $p_{sg}(x,y)=p_s(x)\,p_g(y)$. Sie heißen __unkorreliert__, wenn $\mu_{sg}=\varphi_{sg}-m_sm_g=0$.
:::

Aus Unabhängigkeit folgt Unkorreliertheit: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$. Umgekehrt nicht: Unkorreliert heißt nur, dass kein *linearer* Zusammenhang besteht (Aufgabe [5](#aufg-5)).

**Die Summe zweier unabhängiger Größen.** Die Summe $s=f+g$ nimmt den Wert $x$ an, wenn $f=u$ und $g=x-u$, für irgendein $u$:

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{unabhängig}). \tag{6.1}$$

Das ist die Faltung aus [Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), dort am Beispiel der Würfel. Zwei gleichverteilte Größen ergeben eine Dreieckdichte, drei eine schon fast glockenförmige (Abb. [2](#abb-2)).

:::abbildung et3/k7summen 2
Verteilungsdichten von Summen unabhängiger, auf $[-\frac12,\frac12]$ gleichverteilter Zufallsgrößen. Schon die Summe von drei liegt nahe an der Gaußkurve mit derselben Varianz (bei $x=0$: 0,75 gegen 0,80).
:::

:::aufgabe Aufgabe 5 ★★ Unkorreliert, aber abhängig
<span class="anker" id="aufg-5"></span>

$s$ ist gleichverteilt auf $[-1,1]$ und $g=s^2$. Zeige, dass $s$ und $g$ unkorreliert sind, obwohl $g$ durch $s$ vollständig bestimmt ist.

:::loesung
$m_s=0$ und $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$, also $\mu_{sg}=0-0\cdot m_g=0$: unkorreliert. Trotzdem legt $s$ den Wert von $g$ fest. Der Zusammenhang ist quadratisch, und eine Korrelation erfasst nur lineare Zusammenhänge: Für positive $s$ steigt $g$ mit $s$, für negative fällt es, im Mittel heben sich beide Tendenzen auf.
:::
:::
