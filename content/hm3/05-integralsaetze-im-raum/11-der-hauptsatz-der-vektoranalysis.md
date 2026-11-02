---
title: Stufe 10: Der Hauptsatz der Vektoranalysis
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3151100
summary: Gradientenfelder sind wirbelfrei, Rotationsfelder sind quellenfrei.
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Gradientenfelder sind wirbelfrei, Rotationsfelder sind quellenfrei. Diese Stufe zeigt, dass jedes genügend schöne Feld aus genau diesen beiden Sorten besteht.
:::

**Die Idee.** Ein Feld hat zwei Ursachen: Quellen, gemessen durch $\operatorname{div}$, und Wirbel, gemessen durch $\operatorname{rot}$. Man trennt beide, indem man erst den Quellenanteil als Gradient abspaltet. Was übrig bleibt, ist quellenfrei und damit eine Rotation (Abb. [9](#abb-9)).

:::abbildung hm3/k5helmholtz 9
Zerlegung des Felds $\boldsymbol{F}=(x-y,\,x+y,\,0)$ in der Ebene. Es wirbelt spiralförmig nach außen, ist also die Summe aus dem reinen Quellenfeld $\nabla u=(x,y,0)$ und dem reinen Wirbelfeld $\operatorname{rot}\boldsymbol{A}=(-y,x,0)$.
:::

:::satz Satz 10.1 (Helmholtz-Zerlegung)
<span class="anker" id="satz-10-1"></span>

Sei $\boldsymbol{F}:\mathbb{R}^3\to\mathbb{R}^3$ zweimal stetig differenzierbar mit kompaktem Träger. Dann gibt es zweimal stetig differenzierbare $u:\mathbb{R}^3\to\mathbb{R}$ und $\boldsymbol{A}:\mathbb{R}^3\to\mathbb{R}^3$ mit

<span class="anker" id="gl-10-1"></span>
$$\boldsymbol{F}=\nabla u+\nabla\times\boldsymbol{A}. \tag{10.1}$$
:::

:::beweis Quellen abspalten, Rest ist Rotation
⁠**Schritt 1.** $\operatorname{div}\boldsymbol{F}$ ist stetig differenzierbar. Nach Satz [9.1](poisson-gleichung.html#satz-9-1) gibt es also eine zweimal stetig differenzierbare Lösung $u$ von $\Delta u=\operatorname{div}\boldsymbol{F}$, das heißt $\operatorname{div}(\boldsymbol{F}-\nabla u)=0$ auf $\mathbb{R}^3$.

⁠**Schritt 2.** Das Feld $\boldsymbol{F}-\nabla u$ ist also divergenzfrei auf $\mathbb{R}^3$, und der $\mathbb{R}^3$ ist sternförmig. Nach dem Poincaré-Lemma aus [Teil 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html) gibt es ein stetig differenzierbares $\boldsymbol{A}$ mit $\boldsymbol{F}-\nabla u=\operatorname{rot}\boldsymbol{A}$. Die Formel für $\boldsymbol{A}$ aus dem Poincaré-Lemma zeigt mit dem Satz über Parameterintegrale, dass $\boldsymbol{A}$ zweimal stetig differenzierbar ist.
:::

⁠**So liest man das:** $\nabla u$ trägt alle Quellen, $\nabla\times\boldsymbol{A}$ alle Wirbel. Zwei Zusätze:

<ul>

<li>

⁠**Eichung.** Das $\boldsymbol{A}$ ist nicht eindeutig, wie in [Teil 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html). Addiert man $\nabla\psi$ mit $\Delta\psi=-\operatorname{div}\boldsymbol{A}$, ändert sich $\operatorname{rot}\boldsymbol{A}$ nicht, und man erreicht $\operatorname{div}\boldsymbol{A}=0$.

</li>

<li>

⁠**Weniger Voraussetzungen.** Statt des kompakten Trägers genügt das Abklingen $\boldsymbol{F}(\boldsymbol{x})=o(1/|\boldsymbol{x}|^2)$ für $|\boldsymbol{x}|\to\infty$, das sichert die Konvergenz der Integrale.

</li>

</ul>

:::frage Ist die Zerlegung eindeutig?
Nicht ohne Bedingung im Unendlichen. Für eine harmonische Funktion $h$, also $\Delta h=0$, ist $\nabla h$ zugleich Gradient und Rotation. Man kann es von einem Summanden zum anderen schieben. Verlangt man, dass beide Anteile im Unendlichen abklingen, bleibt nur $h=\text{konst}$, und die Zerlegung ist eindeutig.
:::

:::aufgabe Aufgabe 17 ★★ Zerlegen von Hand
<span class="anker" id="aufg-17"></span>

Das Feld $\boldsymbol{F}=(x-y,\,x+y,\,0)$ hat keinen kompakten Träger, die Zerlegung geht hier trotzdem.

<ol class="al">

<li>

Berechne $\operatorname{div}\boldsymbol{F}$ und $\operatorname{rot}\boldsymbol{F}$.

</li>

<li>

Finde $u$ mit $\nabla u=(x,y,0)$ und $\boldsymbol{A}=(0,0,a)$ mit $\operatorname{rot}\boldsymbol{A}=(-y,x,0)$.

</li>

<li>

Zeige mit $h=x^2-y^2$, dass die Zerlegung nicht eindeutig ist.

</li>

</ol>

:::loesung
(a) $\operatorname{div}\boldsymbol{F}=2$, $\operatorname{rot}\boldsymbol{F}=(0,0,2)$. (b) $u=\frac12(x^2+y^2)$. Mit $\boldsymbol{A}=(0,0,a)$ ist $\operatorname{rot}\boldsymbol{A}=(a_y,-a_x,0)$, also $a=-\frac12(x^2+y^2)$. Dann ist $\nabla u+\operatorname{rot}\boldsymbol{A}=(x-y,\,y+x,\,0)$. (c) $\Delta h=2-2=0$, also ist $\nabla h=(2x,-2y,0)$ divergenzfrei und wirbelfrei. Es ist zugleich eine Rotation, weil $\mathbb{R}^3$ die Bedingung von Satz [7.1](wann-ein-feld-eine-rotation-ist.html#satz-7-1) erfüllt. Ersetzt man $u$ durch $u+h$ und zieht $\nabla h$ beim Rotationsanteil ab, entsteht eine andere Zerlegung desselben Felds.
:::
:::
