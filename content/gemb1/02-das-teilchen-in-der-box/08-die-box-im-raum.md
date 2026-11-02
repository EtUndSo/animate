---
title: Stufe 6: Die Box im Raum
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Das Teilchen in der Box
order: 4120800
summary: In einem Nanokristall ist das Elektron in allen drei Richtungen eingesperrt.
tags: Quantenzustand, Spin, Pauli-Prinzip, künstliches Atom
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
In einem Nanokristall ist das Elektron in allen drei Richtungen eingesperrt. Diese Stufe überträgt das Rezept auf den Raum und zählt die Zustände im Würfel.
:::

**Die Idee.** Der Mechanismus bleibt, es kommt ein Faktor hinzu. Ohne Wände ist $\psi\propto\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol r}=\mathrm{e}^{\mathrm{j}(k_xx+k_yy+k_zz)}$ mit dem Wellenvektor $\boldsymbol k=(k_x,k_y,k_z)$, und die Dispersion lautet

<span class="anker" id="gl-6-1"></span>
$$E(\boldsymbol k)=\frac{\hbar^2|\boldsymbol k|^2}{2m}+V_0=\frac{\hbar^2k_x^2}{2m}+\frac{\hbar^2k_y^2}{2m}+\frac{\hbar^2k_z^2}{2m}+V_0. \tag{6.1}$$

Flächen gleicher Energie sind Kugeln um $\boldsymbol k=0$. Die Wände erlauben $k_x=n_x\pi/L_x$, $k_y=n_y\pi/L_y$, $k_z=n_z\pi/L_z$.

:::satz Satz 6.1 (Quaderförmige Box)
<span class="anker" id="satz-6-1"></span>

Für $V=V_0$ im Quader mit den Kanten $L_x$, $L_y$, $L_z$ und $V\to\infty$ außerhalb gilt

<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
$$\begin{aligned} \psi_{n_x,n_y,n_z}(\boldsymbol r)&=\sqrt{\frac2{L_x}}\sin\Bigl(n_x\frac\pi{L_x}x\Bigr)\sqrt{\frac2{L_y}}\sin\Bigl(n_y\frac\pi{L_y}y\Bigr)\sqrt{\frac2{L_z}}\sin\Bigl(n_z\frac\pi{L_z}z\Bigr),\\ E_{n_x,n_y,n_z}&=\frac{\hbar^2\pi^2}{2m_xL_x^2}\,n_x^2+\frac{\hbar^2\pi^2}{2m_yL_y^2}\,n_y^2+\frac{\hbar^2\pi^2}{2m_zL_z^2}\,n_z^2+V_0. \end{aligned} \tag{6.2|6.3}$$

Für gleiche Massen und $V_0=0$ ist $E=\frac{h^2}{8m}\bigl(n_x^2/L_x^2+n_y^2/L_y^2+n_z^2/L_z^2\bigr)$.
:::

⁠**So liest man das:** Eine Kombination $(n_x,n_y,n_z)$ heißt __Quantenzustand__. Grundzustand ist $(1,1,1)$. Keine Quantenzahl darf null sein, sonst verschwindet das ganze Produkt. **Rechenrezept** für ungleiche Kanten und Massen: Schreibe $m_i=\alpha_im_0$ und $L_i=\beta_iL$. Dann ist

<span class="anker" id="gl-6-4"></span>
$$E_{n_x,n_y,n_z}=E_0\Bigl(\frac{n_x^2}{\alpha_x\beta_x^2}+\frac{n_y^2}{\alpha_y\beta_y^2}+\frac{n_z^2}{\alpha_z\beta_z^2}\Bigr)+V_0,\qquad E_0=\frac{\hbar^2\pi^2}{2m_0L^2}=\frac{0{,}376\,\mathrm{eV\,nm^2}}{L^2}. \tag{6.4}$$

:::abbildung gemb1/k2knoten 6
Würfelbox. Für $\psi$ bleibt im Raum keine Achse übrig, deshalb steht die Farbe für den Wert: rot positiv, blau negativ, kräftig für großen Betrag. Grün sind die Knotenflächen. Sie liegen in der Mitte, quer zur Achse mit der höheren Quantenzahl.
:::

**Der Würfel.** Für $L_x=L_y=L_z=L$ und gleiche Massen ist $E=E_0(n_x^2+n_y^2+n_z^2)+V_0$. Alle Vertauschungen der drei Achsen führen den Würfel in sich über. Die Symmetrie allein ergibt: Drei gleiche Quantenzahlen haben $g=1$, zwei gleiche $g=3$, drei verschiedene $g=6$. Hinzu kommt zufällige Entartung: $3^2+3^2+3^2=27=5^2+1^2+1^2$, also $g=4$. Ungleiche Kanten brechen die Symmetrie und heben die Entartung auf. Der Grundzustand ist punktsymmetrisch zur Würfelmitte. Die drei ersten angeregten Zustände in Abb. [6](#abb-6) haben dieselbe Form, in drei Richtungen gelegt.

| Typ | $(1,1,1)$ | $(2,1,1)$ | $(2,2,1)$ | $(3,1,1)$ | $(2,2,2)$ |
|---|---|---|---|---|---|
| $E/E_0$ | 3 | 6 | 9 | 11 | 12 |
| $g$ | 1 | 3 | 3 | 3 | 1 |
| $E$ in meV bei $L=2$ nm | 282 | 564 | 846 | 1034 | 1128 |

**Viele Elektronen.** Jeder Zustand fasst höchstens zwei Elektronen, die sich im __Spin__ unterscheiden, einer inneren Eigenschaft des Elektrons mit genau zwei Werten. Diese Regel heißt __Pauli-Prinzip__. Elektronen füllen die Box deshalb von unten. Der Würfel füllt sich schalenweise wie ein Atom: nach 2, 8, 14, 20 und 22 Elektronen ist jeweils ein Niveau voll. Ein Objekt, das in allen drei Richtungen quantisiert ist, heißt deshalb auch __künstliches Atom__. **Grenzfall:** Für $L_z\to\infty$ bleibt die rechteckige Box aus Stufe [4](die-box-in-der-ebene.html#stufe-4) mit einer freien Richtung.

:::frage Warum liegt der Grundzustand bei $3\,E_0$ und nicht bei $E_0$? Wäre $(1,0,0)$ nicht tiefer?
$(1,0,0)$ gibt es nicht. Der Faktor mit $n_y=0$ ist überall null, also auch das Produkt: Es wäre gar kein Teilchen da. In jeder eingesperrten Richtung muss die Welle mindestens eine Halbwelle bilden, und jede Richtung kostet mindestens $E_0$.
:::

:::aufgabe Aufgabe 8 ★★ Ein künstliches Atom
<span class="anker" id="aufg-8"></span>

Ein Elektron sitzt in einer Würfelbox mit $L=1$ nm, $m=m_0$.

<ol class="al">

<li>

Gib die vier tiefsten Niveaus in eV mit Entartungsgrad an.

</li>

<li>

Wie viele Elektronen fassen diese vier Niveaus? Wie viele positive Elementarladungen braucht das Objekt, um neutral zu sein?

</li>

<li>

Welche Gesamtenergie haben 8 Elektronen im tiefsten Gesamtzustand? Abstoßung zwischen Elektronen bleibt außer Acht.

</li>

</ol>

:::loesung
(a) Mit $E_0=0{,}376$ eV: 1,13 eV ($g=1$), 2,26 eV ($g=3$), 3,38 eV ($g=3$), 4,14 eV ($g=3$). (b) $1+3+3+3=10$ Zustände, also 20 Elektronen und 20 positive Elementarladungen. (c) Zwei Elektronen bei $3\,E_0$, sechs bei $6\,E_0$: $2\cdot3+6\cdot6=42\,E_0=15{,}8$ eV.
:::
:::

:::aufgabe Aufgabe 9 ★★★ Kanten und Massen ungleich
<span class="anker" id="aufg-9"></span>

Für eine Box gilt $L_x=L_y=3L_z$, $m_x=m_y=m_0/2$, $m_z=m_0$ und $E_{1,1,1}=260$ meV.

<ol class="al">

<li>

Stelle mit [(6.4)](#gl-6-4) eine Formel auf, mit $L=L_x$.

</li>

<li>

Berechne die Kantenlängen.

</li>

<li>

Bestimme die fünf tiefsten Niveaus mit Entartung. Wann kommt zum ersten Mal $n_z=2$ vor?

</li>

</ol>

:::loesung
(a) Mit $\alpha_x=\alpha_y=\frac12$, $\alpha_z=1$, $\beta_x=\beta_y=1$, $\beta_z=\frac13$ ist $E=E_0(2n_x^2+2n_y^2+9n_z^2)$. (b) $E_{1,1,1}=13\,E_0$ gibt $E_0=20$ meV, also $L_x=L_y=\sqrt{0{,}376\,\mathrm{eV\,nm^2}/20\,\mathrm{meV}}=4{,}34$ nm und $L_z=1{,}45$ nm. (c) $(1,1,1)$: 260 meV, $g=1$. $(2,1,1)$ und $(1,2,1)$: 380 meV, $g=2$. $(2,2,1)$: 500 meV, $g=1$. $(3,1,1)$ und $(1,3,1)$: 580 meV, $g=2$. $(3,2,1)$ und $(2,3,1)$: 700 meV, $g=2$. Erst bei 800 meV kommt $(1,1,2)$: $L_z$ ist kurz, die Stufe in $z$ teuer.
:::
:::
