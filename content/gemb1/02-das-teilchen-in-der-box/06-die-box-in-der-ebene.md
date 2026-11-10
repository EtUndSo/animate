---
title: Stufe 4: Die Box in der Ebene
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Das Teilchen in der Box
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box
knoten: Kapitel 2: Das Teilchen in der Box
order: 4120600
summary: Ein Elektron auf einer Fläche bewegt sich in zwei Richtungen zugleich.
tags: Anisotropie, Isotropie
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Ein Elektron auf einer Fläche bewegt sich in zwei Richtungen zugleich. Diese Stufe führt das auf zwei bekannte Probleme in einer Richtung zurück.
:::

**Die Idee.** Ein rechteckiges Potential koppelt $x$ und $y$ nicht: Was in $x$ geschieht, ändert nichts an der Bewegung in $y$. Dann zerfällt das Problem. Die Wellenfunktion wird ein Produkt, die kinetischen Energien addieren sich. Ohne Wände ist die Lösung eine ebene Welle, aus der Parabel wird eine Schale. Mit Wänden bleibt von der Schale nur ein Muster einzelner Punkte (Abb. [4](#abb-4)).

**Ohne Wände.** Die Schrödinger-Gleichung in zwei Dimensionen und ihre Lösung lauten

<span class="anker" id="gl-4-1"></span>
$$-\frac{\hbar^2}{2m}\Bigl(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}\Bigr)\psi+V_0\,\psi=E\,\psi,\quad\psi\propto\mathrm{e}^{\mathrm{j}(k_xx+k_yy)},\quad E(k_x,k_y)=\frac{\hbar^2k_x^2}{2m}+\frac{\hbar^2k_y^2}{2m}+V_0. \tag{4.1}$$

:::satz Satz 4.1 (Rechteckige Box)
<span class="anker" id="satz-4-1"></span>

Für $V=V_0$ in $0<x<L_x$, $0<y<L_y$ und $V\to\infty$ außerhalb gilt, mit $n_x,n_y=1,2,3,\dots$,

<span class="anker" id="gl-4-2"></span>
<span class="anker" id="gl-4-3"></span>
$$\begin{aligned} \psi_{n_x,n_y}(x,y)&=\sqrt{\frac2{L_x}}\sin\Bigl(n_x\frac\pi{L_x}x\Bigr)\cdot\sqrt{\frac2{L_y}}\sin\Bigl(n_y\frac\pi{L_y}y\Bigr),\\ E_{n_x,n_y}&=\frac{\hbar^2\pi^2}{2m_xL_x^2}\,n_x^2+\frac{\hbar^2\pi^2}{2m_yL_y^2}\,n_y^2+V_0. \end{aligned} \tag{4.2|4.3}$$

Für $m_x=m_y=m$ und $V_0=0$ ist $E_{n_x,n_y}=\frac{h^2}{8m}\bigl(n_x^2/L_x^2+n_y^2/L_y^2\bigr)$.
:::

:::herleitung Der Produktansatz
Mit $\psi=\phi(x)\,\chi(y)$ ergibt [(4.1)](#gl-4-1) nach Division durch $\phi\chi$

$$-\frac{\hbar^2}{2m}\frac{\phi''(x)}{\phi(x)}-\frac{\hbar^2}{2m}\frac{\chi''(y)}{\chi(y)}+V_0=E.$$

Der erste Bruch hängt nur von $x$ ab, der zweite nur von $y$. Ihre Summe ist konstant, also ist jeder für sich konstant: $E_x$ und $E_y$ mit $E=E_x+E_y+V_0$. Es bleiben zwei Boxen aus Stufe [3](das-elektron-zwischen-zwei-wanden.html#stufe-3), mit $\phi(0)=\phi(L_x)=0$ und $\chi(0)=\chi(L_y)=0$. Daraus folgen $k_x=n_x\pi/L_x$ und $k_y=n_y\pi/L_y$. Anschaulich: Die Wahrscheinlichkeiten unabhängiger Vorgänge multiplizieren sich, also ist $|\psi|^2=|\phi|^2|\chi|^2$.
:::

:::abbildung gemb1/k2schach 4
Links: Vorzeichen und Höhenlinien von $\psi_{n_x,n_y}$ in der quadratischen Box, gestrichelt die Knotenlinien. Rechts: Dispersion als Schale. Eine quadratische Box lässt nur einzelne Punkte zu (rot), ihre Fußpunkte bilden ein Gitter in der $k_x$-$k_y$-Ebene.
:::

⁠**So liest man das:** Je Richtung gibt es eine Quantenzahl. $\psi_{n_x,n_y}$ hat $n_x-1$ Knotenlinien quer zur $x$-Achse und $n_y-1$ quer zur $y$-Achse, so entsteht das Schachbrett in Abb. [4](#abb-4). Die Massen $m_x$ und $m_y$ kommen aus der Krümmung von $E(k)$ in der jeweiligen Richtung [(2.3)](das-kosinus-band.html#gl-2-3). Sind sie verschieden, spricht man von __Anisotropie__, sind sie gleich, von __Isotropie__. **Gültigkeit:** rechteckige Form, unendlich hohe Wände, Massen längs der Kanten.

::::beispiel
Eine Box mit $L_x=3$ nm und $L_y=2$ nm hat für $m=m_0$ die Energie $E_{1,1}=0{,}376\,\mathrm{eV\,nm^2}\,(1/9+1/4)\,\mathrm{nm^{-2}}=136$ meV, dazu $E_{2,1}=261$ meV, $E_{1,2}=418$ meV und $E_{2,2}=543$ meV. Eine Stufe in der kurzen Richtung kostet mehr.
::::

⁠**Grenzfall:** Für $L_y\to\infty$ ist das Elektron in $y$ frei, $E$ wird in dieser Richtung wieder kontinuierlich.

:::frage Warum ein Produkt und keine Summe?
Eine Summe $\phi(x)+\chi(y)$ wäre an der Wand $x=0$ gleich $\chi(y)$, also nicht null. Ein Produkt ist null, sobald ein Faktor null ist. So erfüllt es alle vier Wände zugleich. Summen tauchen dafür bei der Energie auf, weil die Krümmungen in $x$ und $y$ sich addieren.
:::

:::zusatz Wellenmuster sichtbar gemacht
Stehende Wellen in Rechteck und Kreis erinnern an die Schwingungen eingespannter Membranen. Elektronendichten direkt abzubilden, gelingt selten. Eine Ausnahme: Mit der Spitze eines Rastertunnelmikroskops schiebt man Eisenatome auf einer Kupferoberfläche zu einem Ring aus 48 Atomen mit rund 15 nm Durchmesser. Oberflächenelektronen des Kupfers werden an den Atomen gestreut und bleiben im Ring gefangen. Das Bild zeigt konzentrische Wellen, wie sie die Schrödinger-Gleichung für einen Kreis ergibt. Die Wände dieser Box sind endlich hoch.
:::

:::aufgabe Aufgabe 6 ★★ Die fünf tiefsten Energien
<span class="anker" id="aufg-6"></span>

Eine Box hat $L_x=4$ nm, $L_y=2$ nm, $m=m_0$.

<ol class="al">

<li>

Schreibe die Energie als $E_0(n_x^2+4n_y^2)$ und gib $E_0$ an.

</li>

<li>

Bestimme die fünf tiefsten Energien mit ihren Quantenzahlen. Prüfe auch $n_x=4$. Was fällt auf?

</li>

<li>

Wie viele Knotenlinien hat $\psi_{3,2}$? Skizziere die Vorzeichen.

</li>

</ol>

:::loesung
(a) $E_0=0{,}376\,\mathrm{eV\,nm^2}/16\,\mathrm{nm^2}=23{,}5$ meV. (b) $(1,1)$: $5\,E_0=118$ meV. $(2,1)$: $8\,E_0=188$ meV. $(3,1)$: $13\,E_0=306$ meV. $(1,2)$: $17\,E_0=400$ meV. $(2,2)$ und $(4,1)$: $20\,E_0=470$ meV. Zwei verschiedene Zustände haben dieselbe Energie. (c) $2+1=3$ Knotenlinien, sechs Felder mit wechselndem Vorzeichen, das linke untere positiv.
:::
:::
