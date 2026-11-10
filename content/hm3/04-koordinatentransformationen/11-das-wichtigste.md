---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Koordinatentransformationen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen
knoten: Kapitel 4: Koordinatentransformationen
order: 3141100
summary: Was kostet es, wenn aus einem Kreis ein Rechteck wird?
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

Transformationssatz: $\int_Df(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}=\int_Bf(\Phi(\boldsymbol{x}))\,|\det D\Phi(\boldsymbol{x})|\,\mathrm{d}\boldsymbol{x}$ für bijektives $\Phi:B\to D$ mit $\det D\Phi\neq0$. Ausnahmemengen ohne Volumen stören nicht.

</li>

<li>

Faktoren: Polar und Zylinder $r$, Kugel $r^2\sin\theta$, Rotationskörper $r\,p(z)^2$ mit dem Volumen $\pi\int_a^bp(z)^2\,\mathrm{d} z$. Gauß-Integral: $\int_{-\infty}^\infty\mathrm{e}^{-x^2}\,\mathrm{d} x=\sqrt\pi$.

</li>

<li>

Singularität: $|f|\le c/|\boldsymbol{x}|^\alpha$ mit $\alpha<3$ ist im $\mathbb{R}^3$ integrierbar, und $\int_{B_R(0)}|f|\,\mathrm{d}\boldsymbol{x}\le4\pi cR^{3-\alpha}/(3-\alpha)$.

</li>

<li>

Newtonpotential: $u(\boldsymbol{x})=\frac1{4\pi}\int_{\mathbb{R}^3}\frac{f(\boldsymbol{y})}{|\boldsymbol{x}-\boldsymbol{y}|}\,\mathrm{d}\boldsymbol{y}$ löst $-\Delta u=f$. Schalensatz: außen wie eine Punktquelle, $u=Q/(4\pi a)$, im Hohlraum konstant.

</li>

<li>

Krummlinig: $h_u=|\partial\Phi/\partial u|$, $\hat{\boldsymbol{e}}_u=\frac1{h_u}\partial\Phi/\partial u$, $\nabla f=\sum_u\frac1{h_u}\frac{\partial f}{\partial u}\hat{\boldsymbol{e}}_u$, $\operatorname{div}\boldsymbol{F}=\sum_u\frac1{h_u}\bigl(\frac{\partial F_u}{\partial u}-\boldsymbol{F}\cdot\frac{\partial\hat{\boldsymbol{e}}_u}{\partial u}\bigr)$.

</li>

<li>

Zylinder: $\operatorname{div}\boldsymbol{E}=\frac1r\frac{\partial(rE_r)}{\partial r}+\frac1r\frac{\partial E_\varphi}{\partial\varphi}+\frac{\partial E_z}{\partial z}$ und $\Delta f=\frac{\partial^2f}{\partial r^2}+\frac1r\frac{\partial f}{\partial r}+\frac1{r^2}\frac{\partial^2f}{\partial\varphi^2}+\frac{\partial^2f}{\partial z^2}$.

</li>

<li>

Kugel: $\nabla f=\frac{\partial f}{\partial r}\hat{\boldsymbol{e}}_r+\frac1r\frac{\partial f}{\partial\theta}\hat{\boldsymbol{e}}_\theta+\frac1{r\sin\theta}\frac{\partial f}{\partial\varphi}\hat{\boldsymbol{e}}_\varphi$, für $f=f(r)$ ist $\Delta f=\frac1{r^2}(r^2f')'$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Wechsel der Koordinaten ändert das Volumen jeder kleinen Zelle um den Faktor $|\det D\Phi|$, und genau diesen Preis zahlt man im Integral.

</li>

<li>

Dafür werden Kreis und Kugel zu Quadern, mit den Faktoren $r$ und $r^2\sin\theta$, und das $r^2$ macht sogar Singularitäten wie $1/|\boldsymbol{x}|$ integrierbar.

</li>

<li>

Bei Ableitungen teilt man durch die Maßfaktoren $h_u$ und berücksichtigt, dass sich die Basisvektoren mitdrehen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Im Kleinen ist jede Koordinatenabbildung linear. Die Spalten von $D\Phi$ sagen, wie lang und wie schief eine Koordinatenzelle im Raum liegt.

| Ergebnis | Woher es kommt |
|---|---|
| Faktor $\vert \det D\Phi\vert $ | $\operatorname{vol}(AZ)=\vert \det A\vert \operatorname{vol}(Z)$, auf kleine Zellen angewandt |
| Betrag im Satz | Spiegelung kehrt den Umlaufsinn des Rands um (Stufe [2](der-beweis-in-der-ebene.html#stufe-2)) |
| Faktoren $r$ und $r^2\sin\theta$ | Kanten der Zelle: $\mathrm{d} r$, $r\,\mathrm{d}\varphi$ und $\mathrm{d} r$, $r\,\mathrm{d}\theta$, $r\sin\theta\,\mathrm{d}\varphi$ |
| Gauß-Integral | Faktor $r$ erzeugt eine Stammfunktion |
| Bedingung $\alpha<3$ | Schalenvolumen $4\pi r^2\,\mathrm{d} r$ dämpft $1/r^\alpha$ |
| Schalensatz | $\vert r-a\vert $ im Winkelintegral |
| $1/h_u$ im Gradienten | Kettenregel: Ein Schritt $\mathrm{d} u$ ist $h_u\,\mathrm{d} u$ lang |
| Zusatzterme in $\operatorname{div}$ und $\Delta$ | Produktregel: $\hat{\boldsymbol{e}}_u$ hängt vom Ort ab |
