---
title: Stufe 3: Vom Wellenpaket zur Verteilungsfunktion
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Strom im Halbleiter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter
knoten: Kapitel 12: Strom im Halbleiter
order: 4220500
summary: (1.1) braucht die Besetzung außerhalb des Gleichgewichts.
tags: semiklassische Betrachtung, Diffusionsterm
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
[(1.1)](strom-aus-besetzten-zustanden.html#gl-1-1) braucht die Besetzung außerhalb des Gleichgewichts. Diese Stufe führt die Größe ein, die sie beschreibt, und findet ihre Bewegungsgleichung für den Fall ohne Stöße.
:::

**Die Idee.** Ein klassisches Teilchen ist durch Ort $x$ und Geschwindigkeit $v$ oder Impuls $p=mv$ bestimmt. Die Unschärferelation verbietet, $x$ und $p$ zugleich scharf festzulegen. Interessieren die mikroskopischen Einzelheiten nicht, darf man das Wellenpaket trotzdem als Punkt in der $x$-$k$-Ebene behandeln (__semiklassische Betrachtung__). Viele Elektronen bilden dort eine Wolke. Ohne Stöße wandert jeder Punkt auf seiner Bahn und nimmt seine Besetzung mit.

:::definition Definition 3.1 (Verteilungsfunktion)
<span class="anker" id="satz-3-1"></span>

Die Verteilungsfunktion $f(x,k,t)$ ist die Wahrscheinlichkeit, ein Teilchen mit der Wellenzahl $k$, also der Geschwindigkeit $v(k)$, zur Zeit $t$ am Ort $x$ anzutreffen. In einer Dimension gilt

<span class="anker" id="gl-3-1"></span>
$$n(x,t)=\frac1\pi\int\mathrm{d} k\;f(x,k,t),\qquad j(x,t)=-\frac e\pi\int\mathrm{d} k\;v(k)\,f(x,k,t). \tag{3.1}$$
:::

⁠**So liest man das:** $f$ ist die Besetzung aus [(1.1)](strom-aus-besetzten-zustanden.html#gl-1-1), zusätzlich abhängig von Ort und Zeit. Der Vorfaktor $1/\pi$ folgt aus $\sum_k\to2\cdot L/(2\pi)\int\mathrm{d} k$ und der Teilung durch $L$.

:::abbildung gemb1/k12phasenraum 3
Links: Wellenpaket mit Hülle und dasselbe Paket als Kästchen in der $x$-$k$-Ebene. Rechts: Ohne Stöße wandert das Kästchen längs der Bahn. Bei $(x,k)$ sitzt zur Zeit $t$, was zur Zeit $t-\mathrm{d} t$ bei $(x-v\,\mathrm{d} t,\,k-F\,\mathrm{d} t/\hbar)$ saß.
:::

:::satz Satz 3.2 (Boltzmann-Gleichung ohne Stöße)
<span class="anker" id="satz-3-2"></span>

Ohne Stöße bleibt $f$ längs jeder Bahn konstant, $\mathrm{d} f/\mathrm{d} t=0$, also

<span class="anker" id="gl-3-2"></span>
$$\frac{\partial f}{\partial t}+v\,\frac{\partial f}{\partial x}+\frac F\hbar\,\frac{\partial f}{\partial k}=0. \tag{3.2}$$
:::

⁠**So liest man das:** Der erste Term ist die Änderung am festen Punkt $(x,k)$. Im zweiten tragen Teilchen ihre Besetzung durch den Ort. Weil das Dichteunterschiede ausgleicht, heißt er __Diffusionsterm__. Im dritten schiebt die Kraft die Besetzung durch $k$, das ist [(1.2)](strom-aus-besetzten-zustanden.html#gl-1-2). In drei Dimensionen wird daraus $\partial_tf+\boldsymbol v\cdot\nabla_{\boldsymbol r}f+\hbar^{-1}\boldsymbol F\cdot\nabla_{\boldsymbol k}f=0$.

:::herleitung Von der Bahn zur Gleichung
Ein Punkt, der zur Zeit $t$ bei $(x,k)$ ist, war zur Zeit $t-\mathrm{d} t$ bei $(x-v\,\mathrm{d} t,\;k-F\,\mathrm{d} t/\hbar)$ und hat seine Besetzung mitgebracht:

$$f(x,k,t)=f\bigl(x-v\,\mathrm{d} t,\;k-\tfrac F\hbar\,\mathrm{d} t,\;t-\mathrm{d} t\bigr),\qquad\text{also}\quad\mathrm{d} f=0.$$

Die Fläche des Kästchens bleibt dabei gleich, denn $v$ hängt nicht von $x$ ab und $F$ nicht von $k$ (Satz von Liouville). Die Kettenregel gibt

$$\frac{\mathrm{d}}{\mathrm{d} t}f(x,k,t)=\frac{\partial f}{\partial t}+\frac{\partial f}{\partial x}\frac{\mathrm{d} x}{\mathrm{d} t}+\frac{\partial f}{\partial k}\frac{\mathrm{d} k}{\mathrm{d} t}=0.$$

Einsetzen von $\mathrm{d} x/\mathrm{d} t=v$ und $\hbar\,\mathrm{d} k/\mathrm{d} t=\mathrm{d} p/\mathrm{d} t=F$ ergibt [(3.2)](#gl-3-2).
:::

⁠**Gültigkeit:** Das Paket muss schmal sein gegen die Breite von $f$ in $k$ und klein gegen die Strecke, auf der sich Potential und Dichte ändern. In Silizium ist bei 300 K die thermische Geschwindigkeit $v_\text{th}=\sqrt{3k_\mathrm BT/m_\mathrm n^*}=2{,}3\cdot10^5$ m/s (wie $v_\mathrm e$ aus [Kapitel 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html), mit $m^*$ statt $m_0$) und damit $k_\text{th}=m_\mathrm n^*v_\text{th}/\hbar=0{,}51\,\mathrm{nm^{-1}}$. Ein Paket mit $\Delta x=10$ nm hat $\Delta k=0{,}05\,\mathrm{nm^{-1}}$, 10 % davon. Für Gebiete über 100 nm reicht das. Weit darunter braucht man die Quantenmechanik mit Greenschen Funktionen $G^r(x,x',E)$.

::::beispiel
Zwei Grenzfälle lösen [(3.2)](#gl-3-2) sofort. In homogener Probe ist $f(k,t)=f(k-Ft/\hbar,0)$: die starre Verschiebung aus Stufe [1](strom-aus-besetzten-zustanden.html#stufe-1). Ohne Kraft ist $f(x,k,t)=f(x-v(k)t,k,0)$: Jede Gruppe läuft weiter, bei $v_\text{th}$ in 1 ps um 230 nm.
::::

:::frage Legt $f(x,k,t)$ nicht doch Ort und Wellenzahl zugleich fest?
Nein. Ein Kästchen mit $\Delta x\,\Delta k\approx\frac12$ enthält rund einen Platz. Gemeint ist immer ein Mittel über Kästchen mit vielen Plätzen, und für den Strom genügt das.
:::

:::aufgabe Aufgabe 3 ★★ Die Gleichung prüfen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Zeige durch Einsetzen, dass $f=g(x-v\,t)\,h(k)$ für $F=0$ und festes $v$ die Gleichung [(3.2)](#gl-3-2) löst. Wie weit läuft $g$ bei $v=2\cdot10^5$ m/s in 1 ps?

</li>

<li>

Zeige dasselbe für $f=h(k-Ft/\hbar)$ in homogener Probe. Wie weit rutscht $h$ bei $F=1{,}6\cdot10^{-15}$ N in 1 ps?

</li>

<li>

Vorhersage: Was bleibt von [(3.2)](#gl-3-2) im Gleichgewicht einer homogenen Probe ohne Kraft übrig?

</li>

</ol>

:::loesung
(a) $\partial_tf=-v\,g'\,h$ und $v\,\partial_xf=+v\,g'\,h$, die Summe ist null. $g$ läuft $v\,t=200$ nm weit. (b) $\partial_tf=-(F/\hbar)h'$ und $(F/\hbar)\partial_kf=+(F/\hbar)h'$. Die Verschiebung ist $Ft/\hbar=0{,}015\,\mathrm{nm^{-1}}$. (c) Nichts: $\partial_xf=0$, ohne Kraft fehlt der dritte Term, und im Gleichgewicht ist $\partial_tf=0$.
:::
:::
