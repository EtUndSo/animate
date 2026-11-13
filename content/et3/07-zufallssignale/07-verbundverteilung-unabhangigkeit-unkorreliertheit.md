---
title: Stufe 6: Verbundverteilung, Unabhängigkeit, Unkorreliertheit
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
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

Das ist die Faltung aus [Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), dort am Beispiel der Würfel. Zwei gleichverteilte Größen ergeben eine Dreieckdichte, drei eine schon fast glockenförmige (Abb. [2](#abb-2)).

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

::::formelsammlung
**Verbundverteilung**

$$P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{und}\ g\le y],\qquad p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$$

Daraus die Einzelverteilungen, $P_{sg}(x,\infty)=P_s(x)$, und die Korrelation $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$.

**Statistisch unabhängig**

$$p_{sg}(x,y)=p_s(x)\,p_g(y)$$

Daraus folgt Unkorreliertheit: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$.

**Unkorreliert**

$$\mu_{sg}=\varphi_{sg}-m_sm_g=0$$

Kein linearer Zusammenhang; daraus folgt keine Unabhängigkeit (Beispiel: $s$ gleichverteilt auf $[-1,1]$ und $g=s^2$).

**Dichte der Summe unabhängiger Größen**

$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)$$

Für $s=f+g$; das Integral gilt allgemein, die Faltung bei Unabhängigkeit. Zwei gleichverteilte Größen ergeben eine Dreieckdichte, drei schon eine fast glockenförmige.
::::

::::lernkarten
:::karte begriff Verbundverteilung
Was beschreibt die Verbundverteilung $P_{sg}(x,y)$ zweier Zufallsgrößen $s$ und $g$, und wie erhält man ihre Dichte?
---
Die Wahrscheinlichkeit, dass beide Größen zugleich unter ihren Schwellen liegen: $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{und}\ g\le y]$. Ihre Dichte ist $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$.
--- falsch
Die Wahrscheinlichkeit, dass wenigstens eine der beiden Größen unter ihrer Schwelle liegt: $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{oder}\ g\le y]$. Ihre Dichte ist die Summe der beiden Einzeldichten.
--- falsch
Das Produkt der beiden Verteilungsfunktionen, $P_{sg}(x,y)=P_s(x)\,P_g(y)$, und zwar für beliebige Zufallsgrößen. Ihre Dichte ist deshalb stets das Produkt $p_s(x)\,p_g(y)$ der Einzeldichten.
--- falsch
Die Wahrscheinlichkeit, dass die Summe beider Größen unter der Schwelle $x+y$ liegt: $P_{sg}(x,y)=\mathrm{Prob}[s+g\le x+y]$. Ihre Dichte ist die Faltung der beiden Einzeldichten.
:::
:::karte formel Einzelverteilung und Korrelation aus der Verbundverteilung
Wie erhält man aus der Verbundverteilung zweier Größen die Einzelverteilung von $s$ und die Korrelation $\varphi_{sg}$?
---
Die Einzelverteilung, indem man die andere Schwelle nach unendlich schiebt: $P_{sg}(x,\infty)=P_s(x)$. Die Korrelation als Mittel des Produkts: $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$.
--- falsch
Die Einzelverteilung, indem man die andere Schwelle auf null setzt: $P_{sg}(x,0)=P_s(x)$. Die Korrelation als Produkt der Mittelwerte, $\varphi_{sg}=\int x\,p_s\,\mathrm{d} x\cdot\int y\,p_g\,\mathrm{d} y$, für beliebige Größen.
--- falsch
Die Einzelverteilung, indem man durch die andere teilt: $P_s(x)=P_{sg}(x,y)/P_g(y)$. Die Korrelation als Doppelintegral der Verbunddichte: $\varphi_{sg}=\iint p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$.
--- falsch
Die Einzelverteilung, indem man die andere Schwelle nach minus unendlich schiebt: $P_{sg}(x,-\infty)=P_s(x)$. Die Korrelation als Mittel der Summe: $\varphi_{sg}=\iint(x+y)\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$.
:::
:::karte begriff statistisch unabhängig
Wann nennt man zwei Zufallsgrößen $s$ und $g$ statistisch unabhängig, ausgedrückt durch ihre Dichten?
---
Wenn ihre Verbunddichte das Produkt der Einzeldichten ist: $p_{sg}(x,y)=p_s(x)\,p_g(y)$. Daraus folgt insbesondere, dass sie auch unkorreliert sind.
--- falsch
Wenn ihre Verbunddichte die Summe der Einzeldichten ist: $p_{sg}(x,y)=p_s(x)+p_g(y)$. Daraus folgt insbesondere, dass sich ihre Mittelwerte addieren.
--- falsch
Wenn ihre Kreuzkovarianz verschwindet: $\varphi_{sg}-m_sm_g=0$. Das ist dieselbe Bedingung wie für unkorrelierte Größen; beide Begriffe bedeuten dasselbe.
--- falsch
Wenn ihre Einzeldichten gleich sind: $p_s(x)=p_g(x)$. Dann hat keine der beiden Größen Einfluss darauf, wie die andere verteilt ist.
:::
:::karte begriff unkorreliert
Wann nennt man zwei Zufallsgrößen $s$ und $g$ unkorreliert, und welche Art von Zusammenhang schließt das aus?
---
Wenn ihre Kreuzkovarianz verschwindet: $\mu_{sg}=\varphi_{sg}-m_sm_g=0$, die Korrelation ist also das Produkt der Mittelwerte. Das schließt nur einen linearen Zusammenhang aus.
--- falsch
Wenn ihre Korrelation verschwindet: $\varphi_{sg}=0$, auch wenn beide einen Mittelwert haben. Das schließt jeden Zusammenhang zwischen den beiden Größen aus, auch einen quadratischen.
--- falsch
Wenn ihre Verbunddichte das Produkt der Einzeldichten ist: $p_{sg}(x,y)=p_s(x)\,p_g(y)$. Das schließt jeden Zusammenhang aus, denn die eine Größe verrät nichts über die andere.
--- falsch
Wenn ihre Kreuzkovarianz verschwindet: $\mu_{sg}=\varphi_{sg}-m_sm_g=0$. Das schließt jeden Zusammenhang aus, auch einen quadratischen, denn jeder Zusammenhang verändert die Kovarianz.
:::
:::karte zusammenhang Unabhängig, also unkorreliert
Warum sind statistisch unabhängige Zufallsgrößen immer auch unkorreliert?
---
Weil die Verbunddichte dann ein Produkt ist und das Doppelintegral für $\varphi_{sg}$ in zwei Einzelintegrale zerfällt: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$. Damit ist $\mu_{sg}=0$.
--- falsch
Weil unabhängige Größen stets den Mittelwert null haben und deshalb auch ihre Korrelation $\varphi_{sg}$ null ist. Damit verschwindet die Kreuzkovarianz $\mu_{sg}$ von selbst, ohne weitere Rechnung.
--- falsch
Weil Unabhängigkeit und Unkorreliertheit dasselbe bedeuten: Beide sagen aus, dass die Verbunddichte ein Produkt der Einzeldichten ist. Die Umkehrung gilt deshalb ebenso.
--- falsch
Weil die Verbunddichte dann eine Summe ist und das Doppelintegral für $\varphi_{sg}$ in die Summe der Mittelwerte zerfällt: $\varphi_{sg}=m_s+m_g$. Damit ist $\mu_{sg}=0$.
:::
:::karte zusammenhang Unkorreliert, aber abhängig
Warum sind $s$, gleichverteilt auf $[-1,1]$, und $g=s^2$ unkorreliert, obwohl $g$ durch $s$ vollständig bestimmt ist?
---
Weil $m_s=0$ und $\mathrm E\{sg\}=\mathrm E\{s^3\}=0$ ist, also $\mu_{sg}=0$. Der Zusammenhang ist quadratisch, und eine Korrelation erfasst nur lineare Zusammenhänge: Für positive $s$ steigt $g$, für negative fällt es.
--- falsch
Weil $g=s^2$ nie negativ ist und $s$ ebenso oft positiv wie negativ: Größen mit so verschiedenem Vorzeichenverhalten sind stets statistisch unabhängig und damit natürlich auch unkorreliert.
--- falsch
Weil $m_g=0$ ist, denn die Quadrate gleichverteilter Werte mitteln sich zu null. Damit ist $\mu_{sg}=\varphi_{sg}$, und die Korrelation verschwindet wegen der Symmetrie der Gleichverteilung.
--- falsch
Sie sind gar nicht unkorreliert: Da $g$ durch $s$ vollständig bestimmt ist, gilt $\mathrm E\{sg\}=m_sm_g+1$, und die Kreuzkovarianz ist genau 1, wie bei vollständig gekoppelten Größen.
:::
:::karte formel Dichte der Summe unabhängiger Größen
Welche Verteilungsdichte hat die Summe $s=f+g$ zweier unabhängiger Zufallsgrößen?
---
Die Faltung der Einzeldichten: $p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)$. Man sammelt alle Paare mit $f=u$ und $g=x-u$; bei Unabhängigkeit wird daraus die Faltung.
--- falsch
Das Produkt der Einzeldichten: $p_s(x)=p_f(x)\,p_g(x)$. Die Summe nimmt den Wert $x$ nur an, wenn beide Größen zugleich den Wert $x$ haben, und dafür multipliziert man die Dichten.
--- falsch
Die Summe der Einzeldichten: $p_s(x)=p_f(x)+p_g(x)$. Weil sich die Größen addieren, addieren sich auch ihre Dichten; danach teilt man durch 2, damit die Fläche 1 bleibt.
--- falsch
Die Faltung der Verteilungsfunktionen: $p_s(x)=P_f(x)*P_g(x)$. Man sammelt alle Paare mit $f\le u$ und $g\le x-u$, weil die Summe unter der Schwelle $x$ liegen soll.
:::
:::karte herleitung Dichte der Summe
Wie folgt aus der Verbunddichte, dass die Summe $s=f+g$ zweier unabhängiger Größen die Dichte $p_f(x)*p_g(x)$ hat?
---
Die Summe nimmt den Wert $x$ an, wenn $f=u$ und $g=x-u$ ist, für irgendein $u$, weil sich nur so die beiden Werte zu $x$ ergänzen.
---
Man integriert die Verbunddichte über alle diese Paare, $p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u$, weil sich die Wahrscheinlichkeiten der verschiedenen Möglichkeiten für $u$ addieren.
---
Bei Unabhängigkeit zerfällt die Verbunddichte in das Produkt $p_f(u)\,p_g(x-u)$, weil genau das die Bedingung für statistische Unabhängigkeit ist.
---
Das Integral über $u$ ist dann das Faltungsintegral $p_f(x)*p_g(x)$, weil eine Faltung genau ein solches Produkt mit gespiegeltem, verschobenem Argument integriert.
:::
:::karte zusammenhang Summen gleichverteilter Größen
Welche Form hat die Dichte der Summe von zwei und von drei unabhängigen, gleichverteilten Größen, und warum?
---
Zwei ergeben eine Dreieckdichte, drei schon eine fast glockenförmige, weil jede weitere Summe eine weitere Faltung der Dichten bedeutet. Bei $x=0$ liegt die Summe von drei mit 0,75 nahe an der Gaußkurve gleicher Varianz (0,80).
--- falsch
Zwei ergeben wieder eine Gleichverteilung doppelter Breite, drei eine dreifacher Breite, weil die Summe gleichverteilter Größen gleichverteilt bleibt; nur die Höhe der Dichte sinkt jeweils, damit die Fläche 1 bleibt.
--- falsch
Zwei ergeben eine Dreieckdichte, drei wieder eine Gleichverteilung, weil sich die Ecken des Dreiecks bei der nächsten Faltung abschneiden. Erst sehr viele Summanden ergeben eine Glockenform wie die Gaußkurve.
--- falsch
Zwei ergeben eine Dreieckdichte, drei eine Dichte mit zwei Spitzen, weil die Faltung die Dichte jedes Mal an den Rändern verstärkt. Bei $x=0$ entsteht dabei eine Mulde, die mit jedem Summanden tiefer wird.
:::
::::
