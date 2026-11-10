---
title: Stufe 5: Reziproke Gittervektoren in der Ebene und im Raum
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallwachstum-und-reziprokes-gitter
knoten: Kapitel 7: Kristallwachstum und reziprokes Gitter
order: 4170700
summary: Auf der Kette genügt eine Zahl.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Auf der Kette genügt eine Zahl. Im Kristall zeigen die Gittervektoren in drei Richtungen, und eine Welle hat einen Wellenvektor. Diese Stufe findet alle Vektoren, die zum Gitter passen.
:::

**Die Idee.** Die Welle $\mathrm{e}^{\mathrm{j}\boldsymbol G\cdot\boldsymbol r}$ passt zum Gitter, wenn ihre Phase an jedem Gitterpunkt ein Vielfaches von $2\pi$ ist. Das muss man nur für $\boldsymbol a_1$, $\boldsymbol a_2$, $\boldsymbol a_3$ prüfen, der Rest folgt. Also baut man drei Bausteine $\boldsymbol b_1$, $\boldsymbol b_2$, $\boldsymbol b_3$, von denen jeder Phase nur längs „seines“ $\boldsymbol a_i$ sammelt und auf den beiden anderen senkrecht steht.

:::definition Definition 5.1 (Reziprokes Gitter)
<span class="anker" id="satz-5-1"></span>

Das reziproke Gitter eines Bravais-Gitters besteht aus allen Vektoren $\boldsymbol G$ mit

<span class="anker" id="gl-5-1"></span>
$$\mathrm{e}^{\mathrm{j}\boldsymbol G\cdot\boldsymbol R}=1\quad\text{für alle Gittervektoren }\boldsymbol R\text{ aus (0.1)}. \tag{5.1}$$
:::

:::satz Satz 5.2 (Reziproke Gittervektoren)
<span class="anker" id="satz-5-2"></span>

Die Lösungen von [(5.1)](#gl-5-1) sind $\boldsymbol G=h_1\boldsymbol b_1+h_2\boldsymbol b_2+h_3\boldsymbol b_3$ mit ganzen $h_1,h_2,h_3$. Die primitiven Vektoren $\boldsymbol b_j$ erfüllen

<span class="anker" id="gl-5-2"></span>
$$\boldsymbol a_i\cdot\boldsymbol b_j=2\pi\,\delta_{ij}, \tag{5.2}$$

und ihre Lösung ist

<span class="anker" id="gl-5-3"></span>
$$\boldsymbol b_1=2\pi\,\frac{\boldsymbol a_2\times\boldsymbol a_3}{\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3)},\quad \boldsymbol b_2=2\pi\,\frac{\boldsymbol a_3\times\boldsymbol a_1}{\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3)},\quad \boldsymbol b_3=2\pi\,\frac{\boldsymbol a_1\times\boldsymbol a_2}{\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3)}. \tag{5.3}$$
:::

⁠**So liest man das:** $\delta_{ij}$ ist das Kronecker-Delta: 1 für $i=j$, sonst 0. $i$ und $j$ sind Zählindizes. Die $\boldsymbol b_j$ haben die Einheit 1/m, typisch 10 bis 30 nm$^{-1}$. Der Nenner ist überall derselbe, sein Betrag ist $\Omega$, sein Vorzeichen darf negativ sein. Die Zelle aus den $\boldsymbol b_j$ hat den Inhalt $(2\pi)^3/\Omega$. In der Ebene nimmt man für $\boldsymbol a_3$ einen Einheitsvektor senkrecht zur Ebene. **Gültigkeit:** Die $\boldsymbol a_i$ müssen primitive Gittervektoren eines Bravais-Gitters sein. Die Basis geht nicht ein.

:::herleitung Von der Phase zu den Formeln
Mit $\boldsymbol G=\sum_jh_j\boldsymbol b_j$ und $\boldsymbol R=\sum_i\ell_i\boldsymbol a_i$ ist

$$\boldsymbol G\cdot\boldsymbol R=h_1\ell_1(\boldsymbol a_1\cdot\boldsymbol b_1)+h_2\ell_2(\boldsymbol a_2\cdot\boldsymbol b_2)+h_3\ell_3(\boldsymbol a_3\cdot\boldsymbol b_3)+\text{Mischterme}.$$

[(5.1)](#gl-5-1) verlangt, dass das für alle $\ell_i$ ein ganzes Vielfaches von $2\pi$ ist. Mit [(5.2)](#gl-5-2) fallen die Mischterme weg, und es bleibt $2\pi(h_1\ell_1+h_2\ell_2+h_3\ell_3)$. Weitere Lösungen gibt es nicht: Für jede Lösung ist $\boldsymbol G\cdot\boldsymbol a_i=2\pi h_i$ mit ganzem $h_i$, und das sind die Koordinaten bezüglich der $\boldsymbol b_j$.

$\boldsymbol a_2\times\boldsymbol a_3$ steht senkrecht auf $\boldsymbol a_2$ und $\boldsymbol a_3$, also ist $\boldsymbol a_2\cdot\boldsymbol b_1=\boldsymbol a_3\cdot\boldsymbol b_1=0$. Der Nenner sorgt für $\boldsymbol a_1\cdot\boldsymbol b_1=2\pi$. Die anderen Formeln entstehen durch zyklisches Vertauschen.
:::

::::beispiel [Beispiele] in der Ebene
(Abb. [5](#abb-5)). Das **Rechteckgitter** hat $\boldsymbol a_1=(a_x,0)$, $\boldsymbol a_2=(0,a_y)$. Daraus folgen $\boldsymbol b_1=2\pi(1/a_x,0)$ und $\boldsymbol b_2=2\pi(0,1/a_y)$. Im Rechenmodell sind das 15,7 und 10,5 nm$^{-1}$: Die lange Kante im Ort wird zur kurzen im $k$-Raum. Das **zentriert rechteckige Gitter** mit denselben Kanten hat $\boldsymbol a_1=(a_x,0)$, $\boldsymbol a_2=\frac12(a_x,a_y)$. Hier gilt

<span class="anker" id="gl-5-4"></span>
$$\boldsymbol b_1=2\pi\Bigl(\frac1{a_x},-\frac1{a_y}\Bigr),\qquad\boldsymbol b_2=2\pi\Bigl(0,\frac2{a_y}\Bigr). \tag{5.4}$$
::::

⁠**Probe:** $\boldsymbol a_1\cdot\boldsymbol b_2=0$, $\boldsymbol a_2\cdot\boldsymbol b_1=\pi-\pi=0$, $\boldsymbol a_2\cdot\boldsymbol b_2=2\pi$. **Grenzfall:** Für $a_y\to\infty$ im Rechteckgitter wird $\boldsymbol b_2$ null: Es bleiben unabhängige Ketten mit $2\pi/a_x$.

:::abbildung gemb1/k7rezi2d 5
Links die Gitter, rechts ihre reziproken Gitter, getönt je eine primitive Zelle. Oben rechteckig, unten zentriert rechteckig. Unten steht $\boldsymbol b_1$ senkrecht auf $\boldsymbol a_2$ und $\boldsymbol b_2$ senkrecht auf $\boldsymbol a_1$.
:::

::::beispiel [Beispiele] im Raum
Bei SC ist $\boldsymbol b_1=(2\pi/a)(1,0,0)$, entsprechend die anderen: wieder SC mit der Kante $2\pi/a$. Für FCC ergeben die Vektoren aus der Tabelle

$$\boldsymbol a_2\times\boldsymbol a_3=\frac{a^2}4(-1,-1,1),\quad\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3)=-\frac{a^3}4,\quad\boldsymbol b_1=\frac{2\pi}a(1,1,-1).$$

Der Betrag $a^3/4$ ist $\Omega$, und $\boldsymbol a_1\cdot\boldsymbol b_1=\frac a2\cdot\frac{2\pi}a\cdot2=2\pi$ stimmt. Alle Ergebnisse:

| Kristallgitter | $\boldsymbol b_1,\boldsymbol b_2,\boldsymbol b_3$ in Einheiten von $2\pi/a$ | reziprokes Gitter |
|---|---|---|
| SC | $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ | SC mit Kante $2\pi/a$ |
| BCC | $(1,1,0)$, $(0,1,1)$, $(1,0,1)$ | FCC mit Würfelkante $4\pi/a$ |
| FCC | $(1,1,-1)$, $(1,-1,1)$, $(-1,1,1)$ | BCC mit Würfelkante $4\pi/a$ |

$\frac{2\pi}a(1,1,-1)$ ist ein BCC-Vektor $\frac{a'}2(1,1,-1)$ mit $a'=4\pi/a$. FCC und BCC tauschen also die Rollen. Der Grund liegt in [(5.2)](#gl-5-2): Die Bedingung ist in $\boldsymbol a$ und $\boldsymbol b$ symmetrisch, also ist das reziproke Gitter des reziproken Gitters wieder das Ausgangsgitter.
::::

:::frage Warum zeigt $\boldsymbol b_1$ nicht einfach in Richtung $\boldsymbol a_1$?
[(5.2)](#gl-5-2) verlangt etwas anderes: $\boldsymbol b_1$ muss senkrecht auf $\boldsymbol a_2$ und $\boldsymbol a_3$ stehen. Nur bei orthogonalen $\boldsymbol a_i$ ist das die Richtung von $\boldsymbol a_1$. Eine Welle längs $\boldsymbol b_1$ hat auf jeder Geraden längs $\boldsymbol a_2$ dieselbe Phase.
:::

:::aufgabe Aufgabe 6 ★★ Das hexagonale Gitter
<span class="anker" id="aufg-6"></span>

Ein hexagonales Gitter hat $\boldsymbol a_1=a(1,0)$, $\boldsymbol a_2=a(\frac12,\frac{\sqrt3}2)$ mit $a=0{,}246$ nm.

<ol class="al">

<li>

Bestimme $\boldsymbol b_1$ und $\boldsymbol b_2$ aus [(5.2)](#gl-5-2).

</li>

<li>

Berechne $|\boldsymbol b_1|$, $|\boldsymbol b_2|$ und den Winkel zwischen ihnen. Welche Art von Gitter ist das? Um welchen Winkel ist $\boldsymbol b_1$ gegen $\boldsymbol a_1$ gedreht?

</li>

<li>

Probe: Das Produkt der Zellflächen im Ort und im $k$-Raum muss $(2\pi)^2$ sein.

</li>

</ol>

:::loesung
(a) Aus $\boldsymbol a_1\cdot\boldsymbol b_2=0$ folgt $b_{2x}=0$. Aus $\boldsymbol a_2\cdot\boldsymbol b_2=2\pi$ folgt $b_{2y}=4\pi/(\sqrt3\,a)$. Ebenso ergibt sich $\boldsymbol b_1=\frac{2\pi}a\bigl(1,-\frac1{\sqrt3}\bigr)=(25{,}54;\,-14{,}75)\,\mathrm{nm^{-1}}$ und $\boldsymbol b_2=(0;\,29{,}49)\,\mathrm{nm^{-1}}$. (b) $|\boldsymbol b_1|=|\boldsymbol b_2|=4\pi/(\sqrt3\,a)=29{,}49\,\mathrm{nm^{-1}}$, Winkel 120°. Das Gitter ist wieder hexagonal, um 30° gedreht. (c) $\Omega=\frac{\sqrt3}2a^2=0{,}0524\,\mathrm{nm^2}$, reziproke Zelle $753{,}3\,\mathrm{nm^{-2}}$, Produkt $39{,}48=(2\pi)^2$.
:::
:::
