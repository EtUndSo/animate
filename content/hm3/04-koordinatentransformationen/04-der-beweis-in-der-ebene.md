---
title: Stufe 2: Der Beweis in der Ebene
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3140400
summary: Die Herleitung aus Stufe 1 ist eine Näherung mit kleinen Zellen.
tags: 
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die Herleitung aus Stufe [1](der-transformationssatz.html#stufe-1) ist eine Näherung mit kleinen Zellen. In der Ebene lässt sich die Formel exakt beweisen: Beide Seiten werden zum selben Kurvenintegral über den Rand.
:::

**Die Idee.** Green in der Ebene ([Teil 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html)) verwandelt ein Integral über einen Bereich in ein Randintegral. Das Randintegral über $\partial D$ lässt sich mit der Kettenregel nach $\partial B$ zurückholen, denn $\Phi$ bildet Rand auf Rand ab (Abb. [2](#abb-2)). Green verwandelt es dort zurück in ein Integral über $B$. Die Determinante entsteht dabei von selbst.

:::abbildung hm3/k4rand 2
Links der Rand von $B$, positiv durchlaufen: Das Innere liegt links. Bei $\det D\Phi>0$ bleibt es links. Bei $\det D\Phi<0$ liegt es rechts, der Rand wird rückwärts durchlaufen. Das zeigen auch die beiden kleinen Pfeile: Ihr Drehsinn kehrt sich um.
:::

**Zusatzannahmen.** Sie vereinfachen nur den Beweis, der Satz gilt auch ohne sie. Es sei $f$ stetig differenzierbar in einem Sterngebiet $\mathcal U\supset D$ ([Teil 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html)), $\Phi$ zweimal stetig differenzierbar, $\partial B$ die Spur (Bildmenge) einer geschlossenen regulären Kurve $\gamma:[a,b]\to\mathbb{R}^2$, positiv durchlaufen. Weil $\det D\Phi$ stetig und nie null ist, hat die Determinante auf $B$ ein festes Vorzeichen. Zuerst sei $\det D\Phi>0$. In der Ebene ist $\operatorname{rot}\boldsymbol{F}=\partial F_2/\partial y_1-\partial F_1/\partial y_2$.

:::beweis Transformationssatz in der Ebene
⁠**Schritt 1: ein Feld mit $\operatorname{rot}\boldsymbol{F}=f$.** Lege den Nullpunkt in ein Sternzentrum von $\mathcal U$ und setze

$$g(\boldsymbol{y})=\int_0^1t\,f(t\boldsymbol{y})\,\mathrm{d} t,\qquad\boldsymbol{F}(\boldsymbol{y})=g(\boldsymbol{y})\,(-y_2,\;y_1).$$

Dann ist $\operatorname{rot}\boldsymbol{F}=2g+\boldsymbol{y}\cdot\nabla g$. Ableiten unter dem Integral und partielle Integration in $t$ geben

$$\boldsymbol{y}\cdot\nabla g(\boldsymbol{y})=\int_0^1t^2\,\frac{\mathrm{d}}{\mathrm{d} t}f(t\boldsymbol{y})\,\mathrm{d} t=f(\boldsymbol{y})-2g(\boldsymbol{y}),$$

also $\operatorname{rot}\boldsymbol{F}=f$ auf $\mathcal U$.

⁠**Schritt 2: Green auf $D$.**

$$\int_Df(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}=\int_D\operatorname{rot}\boldsymbol{F}(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}=\int_{\partial D}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{y}.$$

⁠**Schritt 3: Rand zurückholen.** Der Rand $\partial D=\partial(\Phi(B))$ wird von $\Phi\circ\gamma$ durchlaufen, und wegen $\det D\Phi>0$ bleibt der Umlaufsinn positiv. Mit der Kettenregel $\frac{\mathrm{d}}{\mathrm{d} t}\Phi_j(\gamma(t))=\nabla\Phi_j(\gamma(t))\cdot\dot\gamma(t)$ für $j=1,2$ folgt

$$\begin{aligned} \int_{\partial D}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{y}&=\int_a^b\boldsymbol{F}(\Phi(\gamma(t)))\cdot\frac{\mathrm{d}}{\mathrm{d} t}(\Phi\circ\gamma)(t)\,\mathrm{d} t\\ &=\int_a^b\sum_{j=1,2}\bigl[F_j(\Phi(\gamma(t)))\,\nabla\Phi_j(\gamma(t))\bigr]\cdot\dot\gamma(t)\,\mathrm{d} t=\sum_{j=1,2}\int_{\partial B}\bigl[F_j(\Phi(\boldsymbol{x}))\,\nabla\Phi_j(\boldsymbol{x})\bigr]\cdot\mathrm{d}\boldsymbol{x}. \end{aligned}$$

Der letzte Schritt ist die Definition des Kurvenintegrals.

⁠**Schritt 4: Green auf $B$.** Die Felder $(F_j\circ\Phi)\,\nabla\Phi_j$ sind stetig differenzierbar, weil $\Phi$ zweimal stetig differenzierbar ist. Also ist die Summe gleich

$$\sum_{j=1,2}\int_B\Bigl[\frac{\partial}{\partial x_1}\Bigl((F_j\circ\Phi)\frac{\partial\Phi_j}{\partial x_2}\Bigr)-\frac{\partial}{\partial x_2}\Bigl((F_j\circ\Phi)\frac{\partial\Phi_j}{\partial x_1}\Bigr)\Bigr]\mathrm{d}\boldsymbol{x}.$$

⁠**Schritt 5: Ableiten.** Die Produktregel liefert zwei Terme mit zweiten Ableitungen von $\Phi_j$. Sie heben sich nach Schwarz ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)) auf. Für den Rest gibt die Kettenregel $\frac{\partial}{\partial x_m}(F_j\circ\Phi)=\sum_k\bigl(\frac{\partial F_j}{\partial y_k}\circ\Phi\bigr)\frac{\partial\Phi_k}{\partial x_m}$, also

$$\sum_{j,k}\int_B\Bigl(\frac{\partial F_j}{\partial y_k}\circ\Phi\Bigr)\Bigl(\frac{\partial\Phi_j}{\partial x_2}\frac{\partial\Phi_k}{\partial x_1}-\frac{\partial\Phi_j}{\partial x_1}\frac{\partial\Phi_k}{\partial x_2}\Bigr)\mathrm{d}\boldsymbol{x}.$$

⁠**Schritt 6: Determinante erkennen.** Für $j=k$ ist die zweite Klammer null. Für $j=2$, $k=1$ ist sie $\det D\Phi$, für $j=1$, $k=2$ ist sie $-\det D\Phi$. Es bleibt

$$\int_B(\operatorname{rot}\boldsymbol{F})(\Phi(\boldsymbol{x}))\,\det D\Phi(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}=\int_Bf(\Phi(\boldsymbol{x}))\,|\det D\Phi(\boldsymbol{x})|\,\mathrm{d}\boldsymbol{x}.$$
:::

**Der Fall $\det D\Phi<0$.** Dann durchläuft $\Phi\circ\gamma$ den Rand rückwärts, und das Randintegral in Schritt 3 wechselt das Vorzeichen. Am Ende steht $-\int_Bf(\Phi)\det D\Phi\,\mathrm{d}\boldsymbol{x}$, und $-\det D\Phi=|\det D\Phi|$. Der Betrag gleicht also genau den umgekehrten Umlaufsinn aus. **Kontrolle:** Für $f=1$ und lineares $\Phi(\boldsymbol{x})=A\boldsymbol{x}$ sagt der Satz $\operatorname{vol}(D)=|\det A|\operatorname{vol}(B)$, im Einklang mit [(0.1)](von-grund-auf-determinante-und-volumen.html#gl-0-1).

:::frage Warum entsteht beim Zurückholen eine Determinante?
Die Rotation ist eine Differenz zweier gemischter Ableitungen, sie wechselt beim Vertauschen der beiden Richtungen das Vorzeichen. Dasselbe tut die Determinante. Die Kettenregel überträgt diese Eigenschaft auf die Ableitungen von $\Phi$, und aus den vier Einträgen von $D\Phi$ lässt sich nur eine solche Größe bilden.
:::

:::aufgabe Aufgabe 3 ★★ Den Beweis nachrechnen
<span class="anker" id="aufg-3"></span>

Sei $B=[0,1]^2$ mit positiv durchlaufenem Rand und $\boldsymbol{F}(\boldsymbol{y})=(0,y_1)$, also $\operatorname{rot}\boldsymbol{F}=1$.

<ol class="al">

<li>

Sei $\Phi(x_1,x_2)=(2x_1+x_2,\,x_2)$. Berechne $\int\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{y}$ längs $\Phi\circ\gamma$ Seite für Seite und vergleiche mit $\det D\Phi$.

</li>

<li>

Wiederhole das für $\Phi(x_1,x_2)=(x_2,x_1)$. Was sagt das Vorzeichen?

</li>

</ol>

:::loesung
Die Seiten von $\partial B$ sind $(t,0)$, $(1,t)$, $(1-t,1)$, $(0,1-t)$ für $t\in[0,1]$, und längs der Bildkurve ist $\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{y}=y_1\,\mathrm{d} y_2$. (a) Bildkurven: $(2t,0)$, $(2+t,t)$, $(3-2t,1)$, $(1-t,1-t)$. Die vier Integrale sind $0$, $\int_0^1(2+t)\,\mathrm{d} t=\frac52$, $0$ und $-\int_0^1(1-t)\,\mathrm{d} t=-\frac12$. Die Summe 2 ist die Fläche des Bilds, und $\det D\Phi=2$. (b) Bildkurven: $(0,t)$, $(t,1)$, $(1,1-t)$, $(1-t,0)$. Die Integrale sind $0$, $0$, $-1$, $0$, die Summe ist $-1$, und $\det D\Phi=-1$. Das Bild ist wieder das Einheitsquadrat, sein Rand wird aber rückwärts durchlaufen. Das Randintegral gibt deshalb minus die Fläche.
:::
:::
