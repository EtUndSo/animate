---
title: Stufe 5: Das Poincaré-Lemma
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130600
summary: boldsymbol H zeigt, dass rotboldsymbol F =0 nicht immer reicht.
tags: harmonisch, Sterngebiet, geschlitzte Ebene, Lokal
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
$\boldsymbol{H}$ zeigt, dass $\operatorname{rot}\boldsymbol{F}=0$ nicht immer reicht. Diese Stufe zeigt, dass es reicht, wenn das Gebiet von einem Punkt aus überblickt werden kann, und liefert das Potential als Formel.
:::

**Die Idee.** In Stufe [4](wann-nur-start-und-ziel-zahlen.html#stufe-4) war das Potential die Arbeit von einem festen Punkt aus. Auf einer Kugel um den Nullpunkt liegt die Strecke $\boldsymbol{y}(t)=t\boldsymbol{x}$, $0\le t\le1$, immer im Gebiet, und es ist $\dot{\boldsymbol{y}}=\boldsymbol{x}$. Das legt den Ansatz $\varphi(\boldsymbol{x})=\int_0^1\boldsymbol{F}(t\boldsymbol{x})\cdot\boldsymbol{x}\,\mathrm{d} t$ nahe. Ob wirklich $\nabla\varphi=\boldsymbol{F}$ herauskommt, entscheidet die Integrabilitätsbedingung.

:::satz Satz 5.1 (Poincaré auf der Kugel)
<span class="anker" id="satz-5-1"></span>

Sei $\boldsymbol{F}$ stetig differenzierbar auf der Kugel $B_R(0)\subset\mathbb{R}^3$.

<ol class="rm">

<li>

Ist $\operatorname{rot}\boldsymbol{F}=0$, so gilt $\boldsymbol{F}(\boldsymbol{x})=\nabla\Bigl(\int_0^1\boldsymbol{F}(t\boldsymbol{x})\cdot\boldsymbol{x}\,\mathrm{d} t\Bigr)$. $\boldsymbol{F}$ ist also ein Gradientenfeld.

</li>

<li>

Ist $\operatorname{div}\boldsymbol{F}=0$, so gilt $\boldsymbol{F}(\boldsymbol{x})=\operatorname{rot}\Bigl(\int_0^1\boldsymbol{F}(t\boldsymbol{x})\times t\boldsymbol{x}\,\mathrm{d} t\Bigr)$. $\boldsymbol{F}$ ist also ein Rotationsfeld.

</li>

<li>

Ist $\boldsymbol{F}$ zweimal stetig differenzierbar mit $\operatorname{div}\boldsymbol{F}=0$ und $\operatorname{rot}\boldsymbol{F}=0$, so ist $\boldsymbol{F}$ __harmonisch__, das heißt $\Delta\boldsymbol{F}=0$.

</li>

</ol>
:::

:::beweis Poincaré auf der Kugel
⁠**(i)** Den Gradienten zieht man unter das Integral ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)). Für die $k$-te Komponente geben Produkt- und Kettenregel mit $\boldsymbol{y}=t\boldsymbol{x}$

$$\frac{\partial}{\partial x_k}\sum_{j=1}^3F_j(t\boldsymbol{x})\,x_j=\sum_{j=1}^3\frac{\partial F_j}{\partial y_k}(t\boldsymbol{x})\,t\,x_j+F_k(t\boldsymbol{x}).$$

⁠**Hier wird die Integrabilitätsbedingung gebraucht.** In der Summe steht $\partial F_j/\partial y_k$. Für den Hauptsatz bräuchte man die Ableitung von $F_k$ längs der Strecke, und die lautet

$$\frac{\mathrm{d}}{\mathrm{d} t}F_k(t\boldsymbol{x})=\sum_{j=1}^3\frac{\partial F_k}{\partial y_j}(t\boldsymbol{x})\,x_j.$$

Wegen $\operatorname{rot}\boldsymbol{F}=0$ gilt $\partial F_j/\partial y_k=\partial F_k/\partial y_j$ für alle $j,k$, also darf man die Indizes tauschen. Dadurch wird der Integrand zur vollen $t$-Ableitung:

$$t\,\frac{\mathrm{d}}{\mathrm{d} t}F_k(t\boldsymbol{x})+F_k(t\boldsymbol{x})=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[t\,F_k(t\boldsymbol{x})\bigr],\qquad\int_0^1\frac{\mathrm{d}}{\mathrm{d} t}\bigl[t\,F_k(t\boldsymbol{x})\bigr]\mathrm{d} t=F_k(\boldsymbol{x}).$$

Mit $n$ statt 3 gilt die Rechnung in jeder Dimension.

⁠**(ii)** Setze $\boldsymbol a(\boldsymbol{x})=\boldsymbol{F}(t\boldsymbol{x})$ und $\boldsymbol b(\boldsymbol{x})=t\boldsymbol{x}$. Die Produktregel aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) gibt

$$\operatorname{rot}(\boldsymbol a\times\boldsymbol b)=\boldsymbol a\,\operatorname{div}\boldsymbol b-\boldsymbol b\,\operatorname{div}\boldsymbol a+(\boldsymbol b\cdot\nabla)\boldsymbol a-(\boldsymbol a\cdot\nabla)\boldsymbol b.$$

Es ist $\operatorname{div}\boldsymbol b=3t$ und $\operatorname{div}\boldsymbol a=t\,(\operatorname{div}\boldsymbol{F})(t\boldsymbol{x})=0$, dort geht die Voraussetzung ein. Weiter ist $(\boldsymbol b\cdot\nabla)\boldsymbol a=t^2\frac{\mathrm{d}}{\mathrm{d} t}\boldsymbol{F}(t\boldsymbol{x})$ und $(\boldsymbol a\cdot\nabla)\boldsymbol b=t\,\boldsymbol a$. Zusammen entsteht wieder eine volle Ableitung:

$$2t\,\boldsymbol{F}(t\boldsymbol{x})+t^2\frac{\mathrm{d}}{\mathrm{d} t}\boldsymbol{F}(t\boldsymbol{x})=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[t^2\boldsymbol{F}(t\boldsymbol{x})\bigr],\qquad\int_0^1\frac{\mathrm{d}}{\mathrm{d} t}\bigl[t^2\boldsymbol{F}(t\boldsymbol{x})\bigr]\mathrm{d} t=\boldsymbol{F}(\boldsymbol{x}).$$

⁠**(iii)** Nach (i) ist $\boldsymbol{F}=\nabla\varphi$, also $\Delta\varphi=\operatorname{div}\boldsymbol{F}=0$ und damit $\Delta\boldsymbol{F}=\Delta\nabla\varphi=\nabla\Delta\varphi=0$.
:::

⁠**So liest man das:** Die Formel in (i) ist das Kurvenintegral längs der Strecke vom Nullpunkt nach $\boldsymbol{x}$. **Warum die Bedingung nötig ist:** Für $\boldsymbol V$ ist $\boldsymbol V(t\boldsymbol{x})\cdot\boldsymbol{x}=-tyx+txy=0$. Die Formel liefert $\varphi=0$ und damit nicht $\boldsymbol V$. **Beispiel:** Für $\boldsymbol G$ gibt sie $\int_0^12t(x^2+y^2)\,\mathrm{d} t=x^2+y^2$. Für das konstante Feld $(0,0,2)$ gibt (ii) das Vektorpotential $\int_0^1(0,0,2)\times t\boldsymbol{x}\,\mathrm{d} t=(-y,x,0)$, also das Drehfeld $\boldsymbol V$.

**Von der Kugel zum Sterngebiet.** Die Beweise brauchen nur, dass die Strecke vom Mittelpunkt zu jedem $\boldsymbol{x}$ im Gebiet liegt (Abb. [5](#abb-5)). Durch Verschieben gelten sie für jede Kugel $B_R(\boldsymbol{x}_0)$ und darüber hinaus für folgende Gebiete.

:::abbildung hm3/k3stern 5
Links ein Sterngebiet: Von $\boldsymbol{x}_0$ aus liegt jede Strecke im Gebiet. Rechts ein Ring: Zu jedem möglichen Zentrum gibt es Punkte hinter dem Loch.
:::

:::definition Definition 5.2 (Sterngebiet)
<span class="anker" id="satz-5-2"></span>

Eine offene Menge $\mathcal G\subset\mathbb{R}^n$, $n\ge2$, heißt __Sterngebiet__, wenn es einen Punkt $\boldsymbol{x}_0\in\mathcal G$ gibt, das Sternzentrum, so dass die gerade Strecke von $\boldsymbol{x}_0$ zu jedem Punkt von $\mathcal G$ ganz in $\mathcal G$ verläuft.
:::

Kugeln, Quader und alle anderen konvexen Mengen sind Sterngebiete, sogar mit jedem Punkt als Zentrum. Die __geschlitzte Ebene__ $\mathbb{R}^2\setminus\{(x,0):x\le0\}$ ist eines, zum Beispiel mit dem Zentrum $(1,0)$. Die Ebene ohne Nullpunkt ist keines.

:::satz Satz 5.3 (Poincaré-Lemma)
<span class="anker" id="satz-5-3"></span>

Für stetig differenzierbare Vektorfelder auf Sterngebieten $\mathcal G\subset\mathbb{R}^3$ gilt

$$\boldsymbol{F}\text{ ist Gradientenfeld}\iff\operatorname{rot}\boldsymbol{F}=0,\qquad\boldsymbol{F}\text{ ist Rotationsfeld}\iff\operatorname{div}\boldsymbol{F}=0.$$
:::

Die Richtungen „$\Rightarrow$“ sind $\operatorname{rot}\nabla=0$ und $\operatorname{div}\operatorname{rot}=0$ aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html). Die Richtungen „$\Leftarrow$“ liefert Satz [5.1](#satz-5-1) mit $\boldsymbol{x}-\boldsymbol{x}_0$ statt $\boldsymbol{x}$. Das Skalarpotential gelingt auf Sterngebieten in jeder Dimension $n\ge2$, wenn die Integrabilitätsbedingungen gelten.

:::frage Heißt das, $\boldsymbol{H}$ hat gar kein Potential?
Nicht auf ganz $\mathbb{R}^2\setminus\{0\}$, wohl aber lokal: Jeder Punkt des Gebiets liegt in einer kleinen Kreisscheibe ohne den Nullpunkt, und dort greift das Poincaré-Lemma. __Lokal__ heißt hier: in einer kleinen Umgebung jedes Punkts. Die lokalen Potentiale passen nur nicht zu einem einzigen zusammen.
:::

:::aufgabe Aufgabe 5 ★ Potentiale aus der Formel
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Bestimme aus $\varphi(\boldsymbol{x})=\int_0^1\boldsymbol{F}(t\boldsymbol{x})\cdot\boldsymbol{x}\,\mathrm{d} t$ ein Potential von $\boldsymbol{F}(x,y)=(3x^2y,\,x^3)$.

</li>

<li>

Zeige, dass $\boldsymbol{F}(x,y,z)=(2y,0,0)$ ein Rotationsfeld ist, berechne das Vektorpotential aus Satz [5.1](#satz-5-1)(ii) und mache die Probe.

</li>

</ol>

:::loesung
(a) $\boldsymbol{F}(t\boldsymbol{x})\cdot\boldsymbol{x}=3t^3x^3y+t^3x^3y=4t^3x^3y$, also $\varphi=x^3y$. Probe: $\nabla\varphi=(3x^2y,x^3)$. (b) $\operatorname{div}\boldsymbol{F}=\partial_x(2y)=0$. $\boldsymbol{F}(t\boldsymbol{x})\times t\boldsymbol{x}=t^2(0,-2yz,2y^2)$, das Integral gibt $\boldsymbol{A}=\frac13(0,-2yz,2y^2)$. Probe: $\operatorname{rot}\boldsymbol{A}=(\frac43y+\frac23y,\,0,\,0)=(2y,0,0)$.
:::
:::
