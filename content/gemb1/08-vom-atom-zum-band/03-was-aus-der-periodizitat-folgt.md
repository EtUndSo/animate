---
title: Stufe 1: Was aus der Periodizität folgt
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Vom Atom zum Band
order: 4180300
summary: Die Atome eines Kristalls sitzen regelmäßig.
tags: Rumpfion, periodisches Potential, Bloch-Funktion
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die Atome eines Kristalls sitzen regelmäßig. Diese Stufe zeigt, was allein daraus für jede Wellenfunktion folgt, noch ohne die Schrödinger-Gleichung zu lösen.
:::

**Die Idee.** Im Gitter sitzt ein __Rumpfion__, das Atom ohne seine äußeren Elektronen. Es zieht das Elektron an wie der Coulomb-Trichter aus [Teil 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html). Im Kristall reiht sich Trichter an Trichter, nach einer Strecke $a$ wiederholt sich alles. Verschiebt man den Kristall um $a$, ändert sich für das Elektron nichts. Also darf sich nichts Messbares ändern: Die Aufenthaltswahrscheinlichkeit ist bei jedem Atom dieselbe. Von Zelle zu Zelle darf sich $\psi$ nur um einen Phasenfaktor ändern. Daraus folgt die ganze Stufe.

:::definition Definition 1.1 (Periodisches Potential)
<span class="anker" id="satz-1-1"></span>

Ein __periodisches Potential__ erfüllt $V(x+a)=V(x)$, in drei Dimensionen $V(\boldsymbol r+\boldsymbol A)=V(\boldsymbol r)$ für jeden Gittervektor $\boldsymbol A$. Dessen Komponenten sind im einfach kubischen Gitter ganzzahlige Vielfache der Gitterkonstanten $a$.
:::

Ein Kristall der Länge $L$ ist also eine große Box wie in [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html), deren Boden mit der Periode $a$ gewellt ist. Als Modell ersetzt man jeden Trichter durch einen Topf mit endlich hohen Wänden wie in [Teil 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html) und erhält das Kammpotential (Abb. [1](#abb-1) oben). Die Form der Töpfe ändert die Zahlen, nicht die Aussagen.

:::satz Satz 1.2 (Bloch-Funktion)
<span class="anker" id="satz-1-2"></span>

In einem periodischen Potential lassen sich alle Lösungen so wählen, dass gilt

<span class="anker" id="gl-1-1"></span>
$$\psi_k(x+a)=\mathrm{e}^{\mathrm{j} ka}\,\psi_k(x)\qquad\Longleftrightarrow\qquad\psi_k(x)=\mathrm{e}^{\mathrm{j} kx}\,u_k(x)\quad\text{mit}\quad u_k(x+a)=u_k(x). \tag{1.1}$$
:::

:::herleitung Vom Verschieben zum Phasenfaktor
<ol>

<li>

Ersetzt man $x$ durch $x+a$, bleiben $\mathrm{d}^2/\mathrm{d} x^2$ und $V$ gleich. Ist $\psi(x)$ eine Lösung zur Energie $E$, dann auch $\psi(x+a)$.

</li>

<li>

Gehört zu $E$ nur eine Lösung, ist $\psi(x+a)=\gamma\,\psi(x)$. Gibt es mehrere, kann man sie so kombinieren, dass das gilt.

</li>

<li>

Wäre $|\gamma|\neq1$, wüchse die Welle über viele Zellen ohne Grenze. Also ist $\gamma=\mathrm{e}^{\mathrm{j} ka}$.

</li>

<li>

Für $u(x)=\mathrm{e}^{-\mathrm{j} kx}\psi(x)$ folgt $u(x+a)=\mathrm{e}^{-\mathrm{j} kx}\mathrm{e}^{-\mathrm{j} ka}\mathrm{e}^{\mathrm{j} ka}\psi(x)=u(x)$.

</li>

</ol>
:::

:::abbildung gemb1/k8bloch 1
Kammpotential mit $b=0{,}4$ nm, also $a=1{,}4$ nm, und der tiefste Zustand mit $k=2\pi/(8a)$. Mitte: Realteil von $\psi$ (blau) und die ebene Welle $\pm\cos(kx)$ (orange). Unten: Die Dichte $|\psi|^2$ hat die Periode $a$, in jeder Zelle sitzt gleich viel.
:::

⁠**So liest man das:** Eine solche Lösung heißt __Bloch-Funktion__: eine ebene Welle $\mathrm{e}^{\mathrm{j} kx}$, moduliert mit einer Funktion $u_k$, die in jeder Zelle gleich aussieht. $k$ in 1/nm ist die neue Quantenzahl des Kristalls. **Gültigkeit:** fehlerfreier Kristall, dessen Ränder keine Rolle spielen.

Drei Folgen:

<ol>

<li>

⁠**Die Dichte ist periodisch.** Es gilt $|\psi_k|^2=|u_k|^2$. Das Elektron gehört dem ganzen Kristall.

</li>

<li>

⁠**$E(k)$ ist periodisch:** $E(k+G)=E(k)$, in drei Dimensionen $E(\boldsymbol k+\boldsymbol G)=E(\boldsymbol k)$. Denn $\mathrm{e}^{\mathrm{j} Ga}=1$, der Faktor in [(1.1)](#gl-1-1) ist für $k$ und $k+G$ derselbe. Alle Zustände liegen also in der ersten Brillouin-Zone.

</li>

<li>

⁠**Es gibt so viele $k$ wie Zellen.** Bei $N$ Zellen und der Bedingung $\psi(x+Na)=\psi(x)$ aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) ist $\mathrm{e}^{\mathrm{j} kNa}=1$, also $k_n=n\cdot2\pi/(Na)$ mit ganzem $n$. Die Zone der Breite $2\pi/a$ enthält genau $N$ dieser Werte.

</li>

</ol>

**Beispiel.** In der Atomkette mit $a=0{,}25$ nm liegt der Zonenrand bei $\pi/a=12{,}6\,\mathrm{nm^{-1}}$. Eine 1 µm lange Kette hat $N=4000$ Zellen, die $k$ liegen im Abstand $2\pi/L=0{,}0063\,\mathrm{nm^{-1}}$. Bei $k=\pi/(2a)$ ist $\mathrm{e}^{\mathrm{j} ka}=\mathrm{j}$: Nach vier Atomen stimmt die Phase wieder. **Grenzfall:** Für konstantes $V$ ist $u_k$ konstant, und die ebene Welle aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html) kehrt zurück.

:::frage Das Elektron sitzt doch bei einem Atom. Warum sollte es sich auf alle verteilen?
Ein Zustand fester Energie ändert seine Dichte nicht, und im periodischen Potential ist kein Atom ausgezeichnet. Ein Elektron, das gerade bei einem Atom sitzt, ist ein Wellenpaket aus vielen $k$. Es hat keine scharfe Energie und läuft weiter.
:::

:::aufgabe Aufgabe 1 ★ Phasen und Zustände zählen
<span class="anker" id="aufg-1"></span>

Eine Kette hat $a=0{,}4$ nm.

<ol class="al">

<li>

Berechne Zonenrand und Zonenbreite.

</li>

<li>

Liegt $k=12\,\mathrm{nm^{-1}}$ in der ersten Zone? Welches $k$ innerhalb der Zone beschreibt denselben Zustand?

</li>

<li>

Wie viele verschiedene $k$ erlaubt eine Kette aus 500 Atomen, und wie groß ist ihr Abstand?

</li>

<li>

Vorhersage: Eine Welle hat $k=\pi/a$. Wie unterscheiden sich $\psi(x)$, $\psi(x+a)$ und $\psi(x+2a)$?

</li>

</ol>

:::loesung
(a) Zonenrand $\pi/a=7{,}85\,\mathrm{nm^{-1}}$, Zonenbreite $2\pi/a=15{,}7\,\mathrm{nm^{-1}}$. (b) Nein, $12>7{,}85$. Mit $G=-2\pi/a$ ist $k=12-15{,}71=-3{,}71\,\mathrm{nm^{-1}}$, derselbe Faktor $\mathrm{e}^{\mathrm{j} ka}$. (c) 500 Werte im Abstand $2\pi/(500\cdot0{,}4\,\mathrm{nm})=0{,}0314\,\mathrm{nm^{-1}}$. (d) $\mathrm{e}^{\mathrm{j}\pi}=-1$: $\psi(x+a)=-\psi(x)$ und $\psi(x+2a)=\psi(x)$.
:::
:::
