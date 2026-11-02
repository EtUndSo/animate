---
title: Stufe 4: Wann nur Start und Ziel zählen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130500
summary: Zwei Wege mit gleichem Start und Ziel liefern im Allgemeinen verschiedene Werte.
tags: Gebiet, wegzusammenhängend, wegunabhängig, konservativ
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Zwei Wege mit gleichem Start und Ziel liefern im Allgemeinen verschiedene Werte. Diese Stufe zeigt, bei welchen Feldern der Weg keine Rolle spielt.
:::

**Die Idee.** Das Rechenmodell zeigt beide Fälle (Abb. [4](#abb-4)). Von $A$ nach $B$ ergibt $\boldsymbol V$ auf dem Viertelkreis $\pi/2$. Auf der Strecke ist $\boldsymbol V(\eta(t))\cdot\dot\eta(t)=(-t,1-t)\cdot(-1,1)=1$, das Integral also 1. Der Weg zählt. Für $\boldsymbol G=\nabla(x^2+y^2)$ ergibt der Kreis null, und auf der Strecke ist $\boldsymbol G(\eta(t))\cdot\dot\eta(t)=4t-2$, das Integral wieder null. Der Grund: $x^2+y^2$ hat in $A$ und $B$ denselben Wert. Bei einem Gradientenfeld summieren die Beiträge $\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ die Änderung einer Funktion auf, wie im Hauptsatz $\int_a^bf'(t)\,\mathrm{d} t=f(b)-f(a)$.

:::abbildung hm3/k3wege 4
Dieselben zwei Wege von $A$ nach $B$ in zwei Feldern. Links hängt das Integral vom Weg ab, rechts nicht.
:::

:::definition Definition 4.1 (Gebiet, konservatives Feld)
<span class="anker" id="satz-4-1"></span>

Ein __Gebiet__ $\mathcal G\subset\mathbb{R}^n$ ist eine offene Menge, in der sich je zwei Punkte durch eine reguläre Kurve verbinden lassen, die ganz in $\mathcal G$ verläuft ($\mathcal G$ ist __wegzusammenhängend__). Sei $\boldsymbol{F}:\mathcal G\to\mathbb{R}^n$ stetig. Das Kurvenintegral heißt __wegunabhängig__, wenn $\int_{\gamma_1}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\gamma_2}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ für alle regulär parametrisierten Kurven in $\mathcal G$ mit gleichem Anfangs- und Endpunkt gilt. Ein solches Feld heißt __konservativ__.
:::

:::satz Satz 4.2 (Rundwege)
<span class="anker" id="satz-4-2"></span>

$\boldsymbol{F}$ ist auf dem Gebiet $\mathcal G$ genau dann konservativ, wenn $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=0$ für alle regulär parametrisierten geschlossenen Kurven in $\mathcal G$ gilt.
:::

:::beweis Rundwege
Haben $\gamma_1,\gamma_2$ gleiche Endpunkte, ist $\gamma_1\oplus\gamma_2^-$ geschlossen, und ihr Integral ist $\int_{\gamma_1}-\int_{\gamma_2}$. Sind Rundwege null, sind beide Integrale gleich. Umgekehrt zerlegt man eine geschlossene Kurve in zwei Stücke $\gamma_1$ von $P$ nach $Q$ und $\gamma_2$ von $Q$ nach $P$. Dann haben $\gamma_1$ und $\gamma_2^-$ gleiche Endpunkte, also ist $\int_{\gamma_1}=\int_{\gamma_2^-}=-\int_{\gamma_2}$.
:::

Der Name kommt von der Energie: Auf einem Rundweg gewinnt ein Teilchen im konservativen Feld nichts und verliert nichts.

:::satz Satz 4.3 (Erster Hauptsatz für Kurvenintegrale)
<span class="anker" id="satz-4-3"></span>

Sei $\mathcal G\subset\mathbb{R}^n$ ein Gebiet.

<ol class="rm">

<li>

Ist $\varphi:\mathcal G\to\mathbb{R}$ stetig differenzierbar und $\boldsymbol{F}=\nabla\varphi$, dann gilt für jede regulär parametrisierte Kurve $\gamma$ in $\mathcal G$ von $\boldsymbol{x}_0$ nach $\boldsymbol{x}_1$

<span class="anker" id="gl-4-1"></span>
$$\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\varphi(\boldsymbol{x}_1)-\varphi(\boldsymbol{x}_0). \tag{4.1}$$

</li>

<li>

Ist $\boldsymbol{F}:\mathcal G\to\mathbb{R}^n$ stetig, dann gilt: $\boldsymbol{F}$ ist konservativ $\iff$ $\boldsymbol{F}$ ist ein Gradientenfeld.

</li>

</ol>
:::

:::beweis Erster Hauptsatz
⁠**(i)** Die Kettenregel gibt $\frac{\mathrm{d}}{\mathrm{d} t}\varphi(\gamma(t))=\nabla\varphi(\gamma(t))\cdot\dot\gamma(t)=\boldsymbol{F}(\gamma(t))\cdot\dot\gamma(t)$. Der Hauptsatz der Differential- und Integralrechnung gibt $\int_a^b\frac{\mathrm{d}}{\mathrm{d} t}\varphi(\gamma(t))\,\mathrm{d} t=\varphi(\gamma(b))-\varphi(\gamma(a))$. Bei Knicken heben sich die Zwischenwerte auf.

⁠**(ii)** „$\Leftarrow$“ folgt aus (i), denn rechts in [(4.1)](#gl-4-1) stehen nur die Endpunkte. „$\Rightarrow$“: Fixiere $\boldsymbol{x}_0\in\mathcal G$, verbinde es mit jedem $\boldsymbol{x}\in\mathcal G$ durch eine reguläre Kurve $\Gamma(\boldsymbol{x})$ und setze

$$\varphi(\boldsymbol{x}):=\int_{\Gamma(\boldsymbol{x})}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{y}.$$

Wegen der Wegunabhängigkeit hängt $\varphi$ nicht von der Wahl der Kurve ab. Weil $\mathcal G$ offen ist, liegt für kleines $\delta\neq0$ die Strecke von $\boldsymbol{x}$ nach $\boldsymbol{x}+\delta\hat{\boldsymbol{e}}_k$ in $\mathcal G$. Zum Punkt $\boldsymbol{x}+\delta\hat{\boldsymbol{e}}_k$ darf man über $\boldsymbol{x}$ laufen, also bleibt nur diese Strecke übrig:

$$\varphi(\boldsymbol{x}+\delta\hat{\boldsymbol{e}}_k)-\varphi(\boldsymbol{x})=\int_{[\boldsymbol{x},\,\boldsymbol{x}+\delta\hat{\boldsymbol{e}}_k]}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{y}=\int_0^\delta F_k(\boldsymbol{x}+t\hat{\boldsymbol{e}}_k)\,\mathrm{d} t.$$

Nach dem Mittelwertsatz der Integralrechnung gibt es ein $t^*$ zwischen $0$ und $\delta$ mit

$$\frac1\delta\bigl(\varphi(\boldsymbol{x}+\delta\hat{\boldsymbol{e}}_k)-\varphi(\boldsymbol{x})\bigr)=\frac1\delta\int_0^\delta F_k(\boldsymbol{x}+t\hat{\boldsymbol{e}}_k)\,\mathrm{d} t=F_k(\boldsymbol{x}+t^*\hat{\boldsymbol{e}}_k).$$

Für $\delta\to0$ folgt mit der Stetigkeit von $\boldsymbol{F}$, dass $\partial\varphi/\partial x_k(\boldsymbol{x})=F_k(\boldsymbol{x})$. Da $k$ und $\boldsymbol{x}$ beliebig sind, ist $\nabla\varphi=\boldsymbol{F}$.
:::

⁠**So liest man das:** (i) ist der Hauptsatz in mehreren Variablen. (ii) baut das Potential als angesammelte Arbeit von einem festen Punkt aus, wie $\int_a^xf$ in einer Variablen. Konservativ, Gradientenfeld und Rundwege null sind also drei Namen für dieselbe Sache.

**In der Physik.** Elektrostatische Felder sind konservativ. Deshalb hat jedes Punktepaar eine Spannung, die nicht vom Weg abhängt. Das elektrische Wirbelfeld, das ein sich ändernder Magnetfluss erzeugt, ist nicht konservativ: Ein Umlauf um den Fluss ergibt nicht null, sondern die Induktionsspannung.

**Notwendig, aber nicht hinreichend.** Für $n=2,3$ und stetig differenzierbares $\boldsymbol{F}$ gilt: Ist $\boldsymbol{F}$ konservativ, dann ist $\boldsymbol{F}=\nabla\varphi$ und nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) $\operatorname{rot}\boldsymbol{F}=0$. Passend dazu ist $\operatorname{rot}\boldsymbol V=2\neq0$. Die Umkehrung ist falsch. Auf $\mathcal G=\mathbb{R}^2\setminus\{0\}$ gibt die Quotientenregel

$$\frac{\partial H_2}{\partial x}=\frac{y^2-x^2}{(x^2+y^2)^2}=\frac{\partial H_1}{\partial y},\quad\text{also}\quad\operatorname{rot}\boldsymbol{H}=0.$$

Für den gegen den Uhrzeigersinn durchlaufenen Kreis $K_R$ mit Radius $R>0$, $\gamma(t)=R(\cos t,\sin t)$, ist aber $\boldsymbol{H}(\gamma)\cdot\dot\gamma=\frac1R(-\sin t,\cos t)\cdot R(-\sin t,\cos t)=1$, also

<span class="anker" id="gl-4-2"></span>
$$\int_{K_R}\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{x}=\int_0^{2\pi}1\,\mathrm{d} t=2\pi\neq0. \tag{4.2}$$

Nach Satz [4.2](#satz-4-2) ist $\boldsymbol{H}$ nicht konservativ und damit kein Gradientenfeld. Der Wert hängt nicht von $R$ ab.

:::frage $\operatorname{rot}\boldsymbol{H}=0$ sagt doch, dass das Feld nirgends wirbelt. Woher kommen dann die $2\pi$?
Richtig ist: In jedem Punkt von $\mathcal G$ ist die Rotation null. Aber der Kreis läuft um den Nullpunkt, und dort ist $\boldsymbol{H}$ gar nicht definiert. Die Rechnung $\operatorname{rot}\boldsymbol{H}=0$ sagt über diese Stelle nichts.
:::

:::aufgabe Aufgabe 4 ★★ Wann ist dieses Feld konservativ?
<span class="anker" id="aufg-4"></span>

Seien $a,b\in\mathbb{R}$ und $\boldsymbol{F}(x,y)=\dfrac{a}{(x^2+y^2)^2}\,(x,y)+b\,\boldsymbol{H}(x,y)$ auf $\mathbb{R}^2\setminus\{0\}$.

<ol class="al">

<li>

Berechne das Integral über den Kreis mit Radius 2 gegen den Uhrzeigersinn.

</li>

<li>

Für welche $a,b$ ist $\boldsymbol{F}$ konservativ? Gib dann ein Potential an.

</li>

<li>

Berechne für diesen Fall das Integral von $(1,0)$ nach $(0,2)$.

</li>

</ol>

:::loesung
(a) Der erste Summand steht auf dem Kreis senkrecht zum Weg und liefert null. Der zweite liefert nach [(4.2)](#gl-4-2) den Wert $2\pi b$. (b) Für $b\neq0$ ist der Umlauf nicht null, also ist $\boldsymbol{F}$ nicht konservativ. Für $b=0$ ist $\boldsymbol{F}=\nabla\varphi$ mit $\varphi=-\frac{a}{2(x^2+y^2)}$. $a$ ist beliebig. (c) $\varphi(0,2)-\varphi(1,0)=-\frac a8+\frac a2=\frac{3a}{8}$.
:::
:::
