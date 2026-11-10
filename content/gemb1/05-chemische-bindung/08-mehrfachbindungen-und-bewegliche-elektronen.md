---
title: Stufe 6: Mehrfachbindungen und bewegliche Elektronen
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Chemische Bindung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung
knoten: Kapitel 5: Chemische Bindung
order: 4150800
summary: Nicht immer mischen alle drei p-Orbitale mit.
tags: konjugiert, delokalisiert, Graphen, Kohlenstoff-Nanoröhrchen
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Nicht immer mischen alle drei p-Orbitale mit. Diese Stufe zeigt, was die übrigen leisten: Sie bilden Mehrfachbindungen, und in manchen Stoffen verteilen sich ihre Elektronen über viele Atome.
:::

**Die Idee.** Mischt man 2s nur mit zwei oder einem p-Orbital, entstehen drei oder zwei Hybride, die das Gerüst aus $\sigma$-Bindungen tragen. Die ungemischten p-Orbitale stehen senkrecht dazu und überlappen seitlich mit denen des Nachbarn zu $\pi$-Bindungen. Eine Doppelbindung ist eine $\sigma$- plus eine $\pi$-Bindung, eine Dreifachbindung eine $\sigma$- plus zwei $\pi$-Bindungen.

| Typ | Hybride | $w^2$ | Winkel | p übrig | Beispiele |
|---|---|---|---|---|---|
| sp$^3$ | 4 | 3 | $109{,}47^\circ$ | 0 | Methan CH$_4$, Ethan C$_2$H$_6$, Diamant, Silizium |
| sp$^2$ | 3 | 2 | $120^\circ$ | 1 | Ethen C$_2$H$_4$, Benzol C$_6$H$_6$, Graphen |
| sp | 2 | 1 | $180^\circ$ | 2 | Ethin C$_2$H$_2$ |

:::abbildung gemb1/k5doppel 6
Oben: Hybride sp und sp$^2$ (blau), ungemischte p-Orbitale (grau, bei sp$^2$ senkrecht zur Zeichenebene). Unten links: Doppelbindung im Ethen von der Seite, die p-Orbitale überlappen über und unter der Achse. Mitte: Benzolring, der gestrichelte Kreis steht für die $\pi$-Elektronen. Rechts: Ausschnitt aus Graphen.
:::

:::satz Satz 6.1 (Hybride sp$^2$ und sp)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
$$\mathrm{sp}^2:\quad\phi_\mathrm{h1}=\frac{\phi_\mathrm s+\sqrt2\,\phi_x}{\sqrt3},\quad\phi_{\mathrm h2,3}=\frac{\phi_\mathrm s}{\sqrt3}-\frac{\phi_x}{\sqrt6}\pm\frac{\phi_y}{\sqrt2},\qquad\qquad\mathrm{sp}:\quad\phi_\mathrm{h1,2}=\frac{\phi_\mathrm s\pm\phi_z}{\sqrt2}. \tag{6.1}$$
:::

⁠**So liest man das:** sp$^2$-Hybride zeigen in die Ecken eines Dreiecks in der $xy$-Ebene, $\phi_z$ steht senkrecht darauf. sp-Hybride zeigen entgegengesetzt, $\phi_x$ und $\phi_y$ bleiben übrig. Die Winkel folgen aus [(5.2)](hybridisierung-im-tetraeder.html#gl-5-2). In Ethen bindet jedes C-Atom über seine sp$^2$-Hybride zwei H-Atome und das andere C-Atom, die senkrechten, einfach besetzten p-Orbitale bilden die $\pi$-Bindung. Ethin ist gerade und hat zwei $\pi$-Bindungen. **Gültigkeit:** wie in Stufe [5](hybridisierung-im-tetraeder.html#stufe-5).

::::beispiel
Bindungen zwischen zwei C-Atomen werden kürzer und fester: Einfachbindung 0,154 nm und 3,6 eV, Doppelbindung 0,134 nm und 6,4 eV, Dreifachbindung 0,120 nm und 8,7 eV. Die erste $\pi$-Bindung bringt 2,8 eV, die zweite 2,3 eV. Beide bleiben unter der $\sigma$-Bindung.
::::

⁠**Grenzfall:** Für $w\to0$ hat [(5.2)](hybridisierung-im-tetraeder.html#gl-5-2) keine Lösung: Aus s allein lassen sich keine zwei orthogonalen Orbitale bilden.

**Delokalisierte Bindungen.** Moleküle, in denen sich Doppel- und Einfachbindungen abwechseln, heißen __konjugiert__. Im Benzol sind alle Bindungen des Sechsrings gleich. Jedes C-Atom trägt ein senkrechtes p-Orbital, das mit beiden Nachbarn gleich überlappt. Die $\pi$-Orbitale erstrecken sich darum über den ganzen Ring, die Bindung ist __delokalisiert__, anders als die lokalisierten $\sigma$-Bindungen. Entlang solcher Systeme gelingt Elektronentransport recht leicht. Ebenen aus sp$^2$-hybridisierten C-Atomen heißen __Graphen__, sie bilden die Schichten des Graphits. In Richtung der Schichten leitet Graphit um mehr als vier Größenordnungen besser als senkrecht dazu. __Kohlenstoff-Nanoröhrchen__, nahtlos aufgewickelte Graphenstreifen, tragen Stromdichten zwei bis drei Größenordnungen über denen von Kupfer.

:::frage Diamant und Graphen sind beide reiner Kohlenstoff. Warum isoliert das eine, und das andere leitet?
In Diamant stecken alle vier Außenelektronen in lokalisierten $\sigma$-Bindungen. In Graphen sitzen drei in $\sigma$-Bindungen, das vierte in einem $\pi$-System, das die ganze Schicht umfasst. Die Bindungsart entscheidet, nicht das Element.
:::

:::aufgabe Aufgabe 7 ★ Bindungen zählen
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Gib für SiH$_4$, PH$_3$ und H$_2$S die Zahl der $\sigma$-Bindungen und der freien Paare an.

</li>

<li>

Gib für Ethan, Ethen und Ethin die Hybridisierung und die Zahl der $\sigma$- und $\pi$-Bindungen an.

</li>

<li>

Vorhersage: Lässt sich eine Doppelbindung leichter um ihre Achse verdrehen oder eine Einfachbindung? Begründe mit den p-Orbitalen.

</li>

</ol>

:::loesung
(a) SiH$_4$: 4 $\sigma$, 0 Paare, Tetraeder. PH$_3$: 3 $\sigma$, 1 Paar, Pyramide. H$_2$S: 2 $\sigma$, 2 Paare, gewinkelt. (b) Ethan: sp$^3$, 7 $\sigma$, 0 $\pi$. Ethen: sp$^2$, 5 $\sigma$, 1 $\pi$. Ethin: sp, 3 $\sigma$, 2 $\pi$. (c) Die Einfachbindung. Eine $\sigma$-Bindung ist rund um die Achse symmetrisch. Bei der Doppelbindung stünden die p-Orbitale nach einer Vierteldrehung senkrecht zueinander, die $\pi$-Bindung wäre gelöst. Das kostet 2,8 eV.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Elektronen auf dem Ring
<span class="anker" id="aufg-8"></span>

Die sechs $\pi$-Elektronen des Benzols bewegen sich im Modell frei auf einem Ring mit dem Umfang $L=6\cdot0{,}140$ nm.

<ol class="al">

<li>

Die Welle $\mathrm{e}^{\mathrm{j} kx}$ muss nach einem Umlauf zu sich selbst passen. Zeige $E_m=h^2m^2/(2m_0L^2)$ mit $m=0,\pm1,\pm2,\dots$

</li>

<li>

Besetze die Zustände mit sechs Elektronen. Welches ist der höchste besetzte, welches der tiefste leere Zustand?

</li>

<li>

Berechne Energie und Wellenlänge des Photons, das ein Elektron dazwischen hebt. Gemessen werden 204 nm.

</li>

</ol>

:::loesung
(a) $\mathrm{e}^{\mathrm{j} kL}=1$ verlangt $k=2\pi m/L$. Mit $E=\hbar^2k^2/(2m_0)$ folgt $E_m=h^2m^2/(2m_0L^2)$. (b) $L=0{,}840$ nm, $E_1=2{,}13$ eV, $E_2=8{,}53$ eV. $m=0$ fasst zwei Elektronen, $m=\pm1$ vier. Höchster besetzter Zustand $m=\pm1$, tiefster leerer $m=\pm2$. (c) $\Delta E=6{,}40$ eV, $\lambda=hc/\Delta E=194$ nm, 5 % neben dem Messwert.
:::
:::
