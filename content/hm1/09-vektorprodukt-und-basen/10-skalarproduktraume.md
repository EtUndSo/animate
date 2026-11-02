---
title: Stufe 8: Skalarprodukträume
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektorprodukt und Basen
order: 1291000
summary: Länge, Winkel und Projektion hängen bisher am mathbb R n .
tags: Skalarproduktraum, Prä-Hilbert-Raum, Skalarprodukt, hermitesch, semilinear, Hilbertraum
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Länge, Winkel und Projektion hängen bisher am $\mathbb{R}^n$. Die Beweise benutzen aber nur drei Regeln des Skalarprodukts. Wer sie anderswo erfüllt, bekommt die ganze Geometrie geschenkt: für Polynome, für $\mathbb{C}^n$ und für Signale.
:::

**Die Idee.** Polynome lassen sich nicht zeichnen, aber man kann ihnen ein Skalarprodukt geben. Dann haben sie Längen, stehen senkrecht aufeinander, und Gram-Schmidt läuft wörtlich (Abb. [8](#abb-8)). Im Komplexen braucht das Skalarprodukt eine Konjugation, sonst hätte ein Vektor $\ne\vec0$ die Länge 0.

:::definition Definition 8.1 (Skalarproduktraum)
<span class="anker" id="satz-8-1"></span>

Sei $V$ ein Vektorraum über $\mathbb K=\mathbb{R}$ oder $\mathbb{C}$. $V$ heißt __Skalarproduktraum__ oder __Prä-Hilbert-Raum__, wenn es eine Abbildung $\langle\cdot,\cdot\rangle:V\times V\to\mathbb K$, $(\vec v,\vec w)\mapsto\langle\vec v,\vec w\rangle$ (__Skalarprodukt__) gibt, sodass für alle $\alpha,\beta\in\mathbb K$ und $\vec u,\vec v,\vec w\in V$ gilt:

<ul>

<li>

⁠**(S1)** $\langle\alpha\vec u+\beta\vec v,\vec w\rangle=\alpha\langle\vec u,\vec w\rangle+\beta\langle\vec v,\vec w\rangle$ (Linearität im ersten Eingang),

</li>

<li>

⁠**(S2)** $\langle\vec u,\vec v\rangle=\langle\vec v,\vec u\rangle$ falls $\mathbb K=\mathbb{R}$ (symmetrisch), $\langle\vec u,\vec v\rangle=\overline{\langle\vec v,\vec u\rangle}$ falls $\mathbb K=\mathbb{C}$ (__hermitesch__),

</li>

<li>

⁠**(S3)** $\langle\vec u,\vec u\rangle>0$ für $\vec u\ne\vec0$ (Positivität).

</li>

</ul>
:::

⁠**So liest man das:** Aus (S1) folgt $\langle\vec0,\vec0\rangle=0$, mit (S3) also $\langle\vec u,\vec u\rangle=0\iff\vec u=\vec0$. Für $\mathbb K=\mathbb{C}$ gibt (S2) mit $\vec v=\vec u$, dass $\langle\vec u,\vec u\rangle$ reell ist, sonst hätte (S3) keinen Sinn. Im zweiten Eingang folgt aus (S1) und (S2) nur noch $\langle\vec u,\alpha\vec v+\beta\vec w\rangle=\overline\alpha\langle\vec u,\vec v\rangle+\overline\beta\langle\vec u,\vec w\rangle$, man sagt __semilinear__. Für $\mathbb K=\mathbb{R}$ ändert sich nichts gegenüber [Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html). Ist $V$ zusätzlich vollständig (jede Cauchy-Folge konvergiert), heißt $V$ __Hilbertraum__.

:::satz Satz 8.2 (Norm im Skalarproduktraum)
<span class="anker" id="satz-8-2"></span>

In jedem Skalarproduktraum ist $\|\vec v\|:=\sqrt{\langle\vec v,\vec v\rangle}$ eine Norm. Die Eigenschaften (N) aus [Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html), die Cauchy-Schwarz-Ungleichung und die Dreiecksungleichung für den Abstand $\|\vec x-\vec y\|$ gelten wie dort.
:::

⁠**Beweisidee:** [Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) benutzt nur Linearität, Symmetrie und $\|\text{Rest}\|^2\ge0$. Für $\mathbb K=\mathbb{C}$ steht in Cauchy-Schwarz der Betrag $|\langle\vec x,\vec y\rangle|$. Damit übertragen sich die Stufen [4](orthonormalsysteme-und-projektion.html#stufe-4) und [7](orthonormalbasis-und-gram-schmidt.html#stufe-7) auf jeden Skalarproduktraum, im Komplexen mit $|t_i-\langle\vec p,\vec v_i\rangle|^2$ in [(4.3)](orthonormalsysteme-und-projektion.html#gl-4-3).

**Polynome.** Auf dem Vektorraum $\mathcal P=\{p:\mathbb{R}\to\mathbb{R}\mid p\text{ ist Polynom}\}$ über $\mathbb{R}$ setzt man für $p(x)=\sum_{i=0}^n\alpha_ix^i$, $q(x)=\sum_{j=0}^m\beta_jx^j$

<span class="anker" id="gl-8-1"></span>
$$\langle p,q\rangle:=\int_{-1}^1p(x)q(x)\,\mathrm{d} x=\sum_{i=0}^n\sum_{j=0}^m\alpha_i\beta_j\int_{-1}^1x^{i+j}\,\mathrm{d} x. \tag{8.1}$$

Das ist ein Skalarprodukt: (S1) ist die Linearität des Integrals, (S2) gilt wegen $pq=qp$. (S3): $p^2\ge0$ ist stetig und für $p\ne0$ höchstens an endlich vielen Stellen null, also ist das Integral positiv. **Beispiel ([Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html)):** Für $p(x)=x^2-1$, $q(x)=x+1$ ist $\langle p,q\rangle=\int_{-1}^1(x^3+x^2-x-1)\mathrm{d} x=-\frac43$ und $\|q\|^2=\frac83$.

Gram-Schmidt für $1,x,x^2$: $\|1\|^2=2$ gibt $c_0=\frac1{\sqrt2}$. Wegen $\langle x,1\rangle=0$ bleibt $x$, und $\|x\|^2=\frac23$ gibt $c_1=\sqrt{3/2}\,x$. Für $x^2$ ist $\langle x^2,c_1\rangle=0$ und $\langle x^2,c_0\rangle c_0=\frac13$, also $d_2=x^2-\frac13$, $\|d_2\|^2=\frac8{45}$, $c_2=\sqrt{45/8}\,(x^2-\frac13)$. Das ist eine ONB des Raums der Polynome vom Grad höchstens 2. Die Fourier-Reihe ist derselbe Gedanke für Signale: Sinus und Cosinus bilden, passend normiert, eine Orthonormalbasis (mit unendlich vielen Elementen), und die Fourier-Koeffizienten sind Skalarprodukte wie in [(7.1)](orthonormalbasis-und-gram-schmidt.html#gl-7-1).

:::abbildung hm1/k9poly 8
Links: $\langle1,x\rangle=\int_{-1}^1x\,\mathrm{d} x=0$, die Flächen über und unter der Achse heben sich auf. Die Funktionen $1$ und $x$ stehen senkrecht, ohne dass ein Winkel zu sehen ist. Rechts die ONB $c_0,c_1,c_2$ aus Gram-Schmidt.
:::

**Das Skalarprodukt in $\mathbb{C}^n$.** Für $\vec u,\vec v\in\mathbb{C}^n$ setzt man

<span class="anker" id="gl-8-2"></span>
$$\langle\vec u,\vec v\rangle:=\sum_{i=1}^nu_i\,\overline{v_i}. \tag{8.2}$$

(S1) gilt, denn die $u_i$ stehen ohne Konjugation. (S2): $\overline{\langle\vec v,\vec u\rangle}=\overline{\sum_iv_i\overline{u_i}}=\sum_i\overline{v_i}\,u_i=\langle\vec u,\vec v\rangle$. (S3): $\langle\vec u,\vec u\rangle=\sum_i|u_i|^2>0$ für $\vec u\ne\vec0$. **Warum die Konjugation nötig ist:** Ohne sie hätte $(1,\mathrm{i})\ne\vec0$ den Wert $1+\mathrm{i}^2=0$, und (S3) wäre verletzt. Mit ihr ist $\|(1,\mathrm{i})\|^2=2$.

**Projektion über $\mathbb{C}$.** Die Formeln [(4.5)](orthonormalsysteme-und-projektion.html#gl-4-5) und [(7.2)](orthonormalbasis-und-gram-schmidt.html#gl-7-2) gelten unverändert, auch die Prüfung $[\vec p-\operatorname{Proj}_U(\vec p)]\perp\vec u$ für alle $\vec u\in U$. Die Beweise brauchen nur die Linearität im ersten Eingang, und die gilt auch für $\mathbb K=\mathbb{C}$. Die Reihenfolge $\langle\vec p,\vec v_i\rangle$ im Koeffizienten ist aber wichtig (Aufgabe [10](#aufg-10)). Manche Bücher fordern die Linearität statt (S1) im zweiten Eingang, dann ist der erste semilinear, und in [(4.5)](orthonormalsysteme-und-projektion.html#gl-4-5) und [(7.2)](orthonormalbasis-und-gram-schmidt.html#gl-7-2) müssen die Eingänge getauscht werden.

:::frage Ist ein Polynom jetzt ein Pfeil?
Nein. Die Analogie reicht genau so weit wie die Regeln: Alles, was aus (S1) bis (S3) folgt, gilt auch für Polynome. Einen Pfeil zeichnen kann man nicht, und $\langle p,q\rangle=0$ heißt nur, dass das Integral verschwindet.
:::

:::aufgabe Aufgabe 9 ★★★ Beste Näherung durch Polynome
<span class="anker" id="aufg-9"></span>

(a) Entwickle $p(x)=x^2-1$ nach der ONB $c_0,c_1,c_2$. (b) Bestimme die Projektion von $x^3$ auf den Raum der Polynome vom Grad höchstens 2. (c) Wie groß ist $\|x^3-\operatorname{Proj}(x^3)\|$? Warum ist dieses Polynom unter allen vom Grad $\le2$ das beste?

:::loesung
(a) $\langle p,c_0\rangle=-\frac4{3\sqrt2}=-0{,}943$, $\langle p,c_1\rangle=0$, $\langle p,c_2\rangle=\sqrt{8/45}=0{,}422$. Probe: $-\frac4{3\sqrt2}\cdot\frac1{\sqrt2}+\sqrt{\frac8{45}}\sqrt{\frac{45}8}(x^2-\frac13)=x^2-1$. (b) $\langle x^3,c_0\rangle=\langle x^3,c_2\rangle=0$, denn dort steht eine ungerade Funktion unter dem Integral. Es bleibt $\langle x^3,c_1\rangle c_1=\frac32\cdot\frac25x=\frac35x$. (c) $\|x^3-\frac35x\|^2=\frac27-\frac6{25}=\frac8{175}$, also $0{,}214$. Nach Satz [4.4](orthonormalsysteme-und-projektion.html#satz-4-4) (b), der in jedem Skalarproduktraum gilt, ist die Projektion der nächste Punkt: $\frac35x$ nähert $x^3$ im Sinn dieses Abstands am besten.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Reihenfolge im Komplexen
<span class="anker" id="aufg-10"></span>

Sei $\vec v=\frac1{\sqrt2}(1,\mathrm{i})\in\mathbb{C}^2$, $\vec p=(0,1)$, $U=\operatorname{span}\{\vec v\}$. (a) Prüfe $\|\vec v\|=1$. (b) Berechne $\operatorname{Proj}_U(\vec p)=\langle\vec p,\vec v\rangle\vec v$ und zeige, dass der Rest senkrecht auf $\vec v$ steht. (c) Was passiert mit dem vertauschten Koeffizienten $\langle\vec v,\vec p\rangle\vec v$? (d) Zeige $\langle\vec u,\alpha\vec v\rangle=\overline\alpha\langle\vec u,\vec v\rangle$ aus (S1) und (S2).

:::loesung
(a) $\|\vec v\|^2=\frac12(1+|\mathrm{i}|^2)=1$. (b) $\langle\vec p,\vec v\rangle=1\cdot\overline{\mathrm{i}}/\sqrt2=-\mathrm{i}/\sqrt2$, also $\operatorname{Proj}_U(\vec p)=(-\frac{\mathrm{i}}2,\frac12)$. Der Rest ist $(\frac{\mathrm{i}}2,\frac12)$, und $\langle\text{Rest},\vec v\rangle=\frac1{\sqrt2}(\frac{\mathrm{i}}2-\frac{\mathrm{i}}2)=0$. (c) $\langle\vec v,\vec p\rangle=\mathrm{i}/\sqrt2$ gibt $(\frac{\mathrm{i}}2,-\frac12)$, der Rest $(-\frac{\mathrm{i}}2,\frac32)$ hat mit $\vec v$ das Skalarprodukt $-\sqrt2\,\mathrm{i}\ne0$. Die Formel versagt. (d) $\langle\vec u,\alpha\vec v\rangle\overset{(S2)}{=}\overline{\langle\alpha\vec v,\vec u\rangle}\overset{(S1)}{=}\overline{\alpha\langle\vec v,\vec u\rangle}=\overline\alpha\,\overline{\langle\vec v,\vec u\rangle}\overset{(S2)}{=}\overline\alpha\langle\vec u,\vec v\rangle$.
:::
:::
