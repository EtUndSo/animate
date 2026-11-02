---
title: Stufe 4: Die Formen der Orbitale
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Atome und Orbitale
order: 4140600
summary: Quantenzahlen sind Etiketten.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Quantenzahlen sind Etiketten. Diese Stufe zeigt, wie die zugehörigen Wellen im Raum aussehen und warum sie den Zuständen der Box ähneln.
:::

**Die Idee.** Ein Orbital ist ein Produkt: $R$ sagt, wie weit draußen die Welle liegt, $Y$, in welchen Richtungen. Ein s-Orbital hat keine Knotenfläche und ist kugelrund. Ein p-Orbital hat eine Knotenebene durch den Kern und damit zwei Keulen mit entgegengesetztem Vorzeichen. Ein d-Orbital hat zwei Knotenflächen und meist vier Keulen. Jedes Muster entsteht wie in der Box durch Interferenz der Welle mit sich selbst. Deshalb ähneln sich die Bilder: Der Boxzustand $\psi_{1,1,1}$ aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) ist ein Bauch wie 1s. $\psi_{2,1,1}$ hat eine Knotenebene wie $2\mathrm p_x$, und $\psi_{2,1,2}$ hat zwei wie $\mathrm d_{xz}$. Die Wellenphysik ist dieselbe, nur das Potential ist ein anderes.

:::definition Definition 4.1 (Atomorbital)
<span class="anker" id="satz-4-1"></span>

Ein Atomorbital ist ein gebundener Zustand im Zentralpotential des Atoms, also eine Lösung $\psi_{n\ell m_\ell}(r,\theta,\varphi)=R_{n\ell}(r)\,Y_{\ell m_\ell}(\theta,\varphi)$ von [(1.2)](der-kern-als-kasten-ohne-wande.html#gl-1-2), festgelegt durch die drei Quantenzahlen. In der reellen Form der folgenden Tabelle hat es $\ell$ Knotenflächen durch den Kern und $n-\ell-1$ Knotenkugeln, zusammen $n-1$ Knoten.
:::

| $\ell$ | $m_\ell=0$ | $m_\ell=\pm1$ | $m_\ell=\pm2$ | $m_\ell=\pm3$ |
|---|---|---|---|---|
| 0 | s: 1 |  |  |  |
| 1 | $\mathrm p_z$: $z/r$ | $\mathrm p_x$: $x/r$, $\mathrm p_y$: $y/r$ |  |  |
| 2 | $\mathrm d_{z^2}$: $(3z^2-r^2)/r^2$ | $\mathrm d_{xz}$: $xz/r^2$, $\mathrm d_{yz}$: $yz/r^2$ | $\mathrm d_{xy}$: $xy/r^2$, $\mathrm d_{x^2-y^2}$: $(x^2-y^2)/r^2$ |  |
| 3 | $\mathrm f_{z^3}$ | $\mathrm f_{xz^2}$, $\mathrm f_{yz^2}$ | $\mathrm f_{xyz}$, $\mathrm f_{z(x^2-y^2)}$ | $\mathrm f_{x(x^2-3y^2)}$, $\mathrm f_{y(3x^2-y^2)}$ |

⁠**So liest man das:** Die Tabelle nennt die Orbitale, bei s, p und d mit dem Winkelanteil bis auf einen Faktor. Mit [(0.1)](von-grund-auf-atom-kugelkoordinaten-und-drehimpuls.html#gl-0-1) ist etwa $z/r=\cos\theta$. Die Knotenflächen sind die Nullstellen dieser Ausdrücke: $z=0$ bei $\mathrm p_z$, die Ebenen $x=0$ und $z=0$ bei $\mathrm d_{xz}$, zwei Kegel bei $\mathrm d_{z^2}$. Das Vorzeichen der Keulen ist die Phase der Welle.

:::abbildung gemb1/k4formen 4
Winkelanteil der s-, p- und d-Orbitale im Schnitt durch den Kern. Der Abstand der Linie vom Ursprung ist der Betrag von $Y$ in dieser Richtung. Blau: positives Vorzeichen, rot: negatives. Zwischen den Keulen liegen die Knotenflächen.
:::

**Warum $x$ und $y$ statt $m_\ell=\pm1$.** Zu $m_\ell=\pm1$ gehören die komplexen Faktoren $\mathrm{e}^{\pm\mathrm{j}\varphi}$. Beide Zustände haben dieselbe Energie, also ist auch jede Summe davon eine Lösung (Entartung, [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)). Summe und Differenz liefern $\cos\varphi$ und $\sin\varphi$, also reelle Keulen entlang $x$ und $y$. Diese haben dafür kein festes $L_z$ mehr. Dasselbe gilt für alle d- und f-Orbitale mit $m_\ell\ne0$.

**Was $Y$ bedeutet.** Dem Winkelanteil allein kommt keine physikalische Bedeutung zu. Erst das Produkt $\psi=RY$ beschreibt das Elektron, und erst $|\psi|^2$ ist die Aufenthaltsdichte. Die wesentliche Aussage steckt aber schon in $Y$: In bestimmten Richtungen ist die Aufenthaltswahrscheinlichkeit groß, auf den Knotenflächen geht sie gegen null.

**Beispiel.** Für $n=2$ gilt bis auf die Normierung

<span class="anker" id="gl-4-1"></span>
$$\psi_{2\mathrm s}\propto\Bigl(1-\frac{r}{2r_1}\Bigr)\mathrm{e}^{-r/(2r_1)},\qquad\psi_{2\mathrm p_z}\propto z\,\mathrm{e}^{-r/(2r_1)}. \tag{4.1}$$

2s hat eine Knotenkugel bei $r=2r_1=0{,}106$ nm. $2\mathrm p_z$ hat die Knotenebene $z=0$ und seine größte Amplitude auf der $z$-Achse bei $|z|=2r_1$. Beide klingen außen doppelt so langsam ab wie 1s. **Grenzfälle:** Am Kern ist nur ein s-Orbital ungleich null, denn für $\ell\ge1$ geht $R$ wie $r^\ell$ gegen null. Weit außen klingt jedes Orbital wie im verbotenen Gebiet aus [Teil 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html) mit $\mathrm{e}^{-\kappa r}$ ab, mit $\kappa=\sqrt{2m_0|E_n|}/\hbar=1/(n\,r_1)$.

:::frage Ein p-Orbital hat eine Knotenebene. Wie kommt das Elektron von einer Keule in die andere, wenn es diese Ebene nie betritt?
Die Frage setzt eine Bahn voraus, und die gibt es nicht. Der Zustand ist eine stehende Welle, die zugleich in beiden Keulen existiert. Nichts wandert durch die Knotenebene, das Elektron wechselt nicht hinüber.
:::

:::aufgabe Aufgabe 5 ★ Knoten zählen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Wie viele Knotenflächen und Knotenkugeln haben 3p, 4d, 4f und 5s?

</li>

<li>

Welches dieser Orbitale hat am Kern eine Aufenthaltsdichte ungleich null?

</li>

<li>

Welcher Boxzustand $\psi_{n_x,n_y,n_z}$ entspricht in der Form $2\mathrm p_y$? Welcher $\mathrm d_{xy}$?

</li>

</ol>

:::loesung
(a) 3p: 1 Fläche, 1 Kugel. 4d: 2 Flächen, 1 Kugel. 4f: 3 Flächen, keine Kugel. 5s: keine Fläche, 4 Kugeln. (b) Nur 5s, denn nur für $\ell=0$ ist die Welle am Kern ungleich null. (c) $2\mathrm p_y$ entspricht $\psi_{1,2,1}$ (Knotenebene senkrecht zu $y$). $\mathrm d_{xy}$ entspricht $\psi_{2,2,1}$ (Knotenebenen senkrecht zu $x$ und zu $y$).
:::
:::

:::aufgabe Aufgabe 6 ★★★ Der Zustand 2s
<span class="anker" id="aufg-6"></span>

Nimm $\psi=(1-r/(2r_1))\,\mathrm{e}^{-r/(2r_1)}$ aus [(4.1)](#gl-4-1).

<ol class="al">

<li>

Setze $\psi$ in die Gleichung aus der Herleitung von Stufe [2](das-wasserstoffatom.html#stufe-2) ein, also $-\frac{\hbar^2}{2m_0}(\psi''+\frac2r\psi')+V\psi=E\psi$. Zeige $E=E_1/4$. Tipp: $e^2/(4\pi\varepsilon_0)=\hbar^2/(m_0r_1)$.

</li>

<li>

Prüfe die Abklingkonstante $\kappa=\sqrt{2m_0|E_2|}/\hbar$ aus [Teil 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html) gegen den Exponenten von $\psi$.

</li>

</ol>

:::loesung
(a) Mit $a=r_1$ ist $\psi'=(-\frac1a+\frac{r}{4a^2})\mathrm{e}^{-r/(2a)}$, $\psi''=(\frac{3}{4a^2}-\frac{r}{8a^3})\mathrm{e}^{-r/(2a)}$, also $\psi''+\frac2r\psi'=(\frac{5}{4a^2}-\frac{2}{a\,r}-\frac{r}{8a^3})\mathrm{e}^{-r/(2a)}$. Mit $V=-\hbar^2/(m_0a\,r)$ ist $V\psi=(-\frac{\hbar^2}{m_0a\,r}+\frac{\hbar^2}{2m_0a^2})\mathrm{e}^{-r/(2a)}$. Die Summe ergibt, geteilt durch $\hbar^2/(2m_0)$ und durch $\mathrm{e}^{-r/(2a)}$,

$$-\frac{5}{4a^2}+\frac{2}{a\,r}+\frac{r}{8a^3}-\frac{2}{a\,r}+\frac{1}{a^2}=-\frac{1}{4a^2}\Bigl(1-\frac{r}{2a}\Bigr).$$

Die $1/r$-Terme heben sich auf, und es bleibt ein Vielfaches von $\psi$: $E=-\hbar^2/(8m_0a^2)=E_1/4=-3{,}40$ eV. (b) $\kappa=\sqrt{2m_0\cdot\hbar^2/(8m_0r_1^2)}/\hbar=1/(2r_1)$, genau der Faktor im Exponenten.
:::
:::
