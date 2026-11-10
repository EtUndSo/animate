---
title: Stufe 5: Viele Atome
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Vom Atom zum Band
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band
knoten: Kapitel 8: Vom Atom zum Band
order: 4180700
summary: Ein Kristall hat nicht vier Atome, sondern unvorstellbar viele.
tags: Einhüllende, quasikontinuierlich
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ein Kristall hat nicht vier Atome, sondern unvorstellbar viele. Diese Stufe zeigt, was für große $N$ aus den Niveaus wird und wie man ohne riesige Matrix rechnet.
:::

**Die Idee.** In [(4.4)](vier-atome-und-die-matrix.html#gl-4-4) bleiben alle Energien zwischen $E_\mathrm s-2V_\mathrm{ss}$ und $E_\mathrm s+2V_\mathrm{ss}$. Mehr Atome ergeben keine breitere Aufspaltung, sondern dichtere Niveaus im selben Bereich, denn jedes Atom hat nur zwei Nachbarn (Abb. [5](#abb-5)). Für große $N$ zählen die Enden nicht mehr, und es gilt Stufe [1](was-aus-der-periodizitat-folgt.html#stufe-1): Die Koeffizienten unterscheiden sich von Atom zu Atom nur um den Faktor $\mathrm{e}^{\mathrm{j} ka}$. So schrumpft die Riesenmatrix auf eine einzige Gleichung.

:::satz Satz 5.1 (Tight-Binding-Band)
<span class="anker" id="satz-5-1"></span>

Für $\hat H=-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2}{\mathrm{d} x^2}+\sum_\ell V(x-\ell a)$ und $N\to\infty$ sind die Lösungen

<span class="anker" id="gl-5-1"></span>
$$\psi_k(x)=\frac1{\sqrt N}\sum_{\ell=1}^N\mathrm{e}^{\mathrm{j} k\ell a}\,\phi(x-\ell a),\qquad\text{kurz}\quad|\psi_k\rangle=\frac1{\sqrt N}\sum_{\ell=1}^N\mathrm{e}^{\mathrm{j} k\ell a}\,|\ell\rangle, \tag{5.1}$$

mit dem Band

<span class="anker" id="gl-5-2"></span>
$$E(k)=E_\mathrm s-2V_\mathrm{ss}\cos(ka),\qquad-\frac\pi a\le k\le\frac\pi a. \tag{5.2}$$
:::

:::herleitung Eine Zeile der Matrix
Die Zeile $\ell$ von $\boldsymbol H\boldsymbol c=E\boldsymbol c$ lautet mit $c_\ell=\mathrm{e}^{\mathrm{j} k\ell a}$

$$-V_\mathrm{ss}\,\mathrm{e}^{\mathrm{j} k(\ell+1)a}+E_\mathrm s\,\mathrm{e}^{\mathrm{j} k\ell a}-V_\mathrm{ss}\,\mathrm{e}^{\mathrm{j} k(\ell-1)a}=E\,\mathrm{e}^{\mathrm{j} k\ell a}.$$

Division durch $\mathrm{e}^{\mathrm{j} k\ell a}$ ergibt eine Regel, die für jedes $\ell$ gleich ist:

$$E(k)=\langle\ell|\hat H|\ell+1\rangle\,\mathrm{e}^{\mathrm{j} ka}+\langle\ell|\hat H|\ell\rangle+\langle\ell|\hat H|\ell-1\rangle\,\mathrm{e}^{-\mathrm{j} ka}=-V_\mathrm{ss}\,\mathrm{e}^{-\mathrm{j} ka}+E_\mathrm s-V_\mathrm{ss}\,\mathrm{e}^{\mathrm{j} ka}.$$

Mit $\mathrm{e}^{\mathrm{j} ka}+\mathrm{e}^{-\mathrm{j} ka}=2\cos(ka)$ folgt [(5.2)](#gl-5-2). $1/\sqrt N$ normiert: $\langle\psi_k|\psi_k\rangle=\frac1N\sum_\ell1=1$.
:::

:::abbildung gemb1/k8leiter 5
Oben links: Niveaus für $N$ Atome mit $E_\mathrm s=-5$ eV und $V_\mathrm{ss}=0{,}5$ eV. Oben rechts: Band [(5.2)](#gl-5-2) mit den 20 Zuständen der Kette. Unten: Realteil von $\psi_k$, gestrichelt die Einhüllende. Am Boden sind alle Nachbarn gleichphasig, oben gegenphasig.
:::

⁠**So liest man das:** $\mathrm{e}^{\mathrm{j} k\ell a}$ ist die __Einhüllende__, eine ebene Welle, abgetastet an den Atomen. $\phi(x-\ell a)$ ist die Wellenfunktion am Gitterplatz $\ell$. Das Band hat die Mitte $E_\mathrm s$ und die Breite $4V_\mathrm{ss}$. [(5.2)](#gl-5-2) hat die Form von [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2): $V_\mathrm{ss}$ entspricht $t_0$, und $E_\mathrm s$ entspricht $2t_0+V_0$. Nur stammt $t_0$ aus dem Punktabstand, $V_\mathrm{ss}$ aus dem Überlapp. Die Geschwindigkeit ist

<span class="anker" id="gl-5-3"></span>
$$v(k)=\frac1\hbar\frac{\partial E(k)}{\partial k}=\frac{2V_\mathrm{ss}a}{\hbar}\sin(ka). \tag{5.3}$$

⁠**Mechanismus:** Bei $k=0$ haben alle Nachbarn gleiches Vorzeichen, jedes Paar ist bindend, $E=E_\mathrm s-2V_\mathrm{ss}$. Bei $k=\pi/a$ wechselt das Vorzeichen von Atom zu Atom, jedes Paar ist antibindend, $E=E_\mathrm s+2V_\mathrm{ss}$. Das Band ist die Aufspaltung aus Stufe [3](zwei-atome.html#stufe-3), fortgesetzt für jedes Paar. Bei $k=\pi/(2a)$ ist $E=E_\mathrm s$, und $v$ ist am größten. **Gültigkeit:** gleiche Atome, ein Orbital je Atom, nur direkte Nachbarn, $N$ groß.

::::beispiel
Im Rechenmodell reicht das Band von $-6$ bis $-4$ eV, und $v_\text{max}=2V_\mathrm{ss}a/\hbar=3{,}8\cdot10^5$ m/s. Für $N=20$ sind die äußersten Niveaus $-5{,}989$ und $-4{,}011$ eV, schon 98,9 % der Breite, und sie liegen in der Bandmitte 149 meV auseinander. Bei 1 µm Länge sind es 0,79 meV, bei 1 mm nur 0,79 µeV, weit unter der Wärmeenergie von 26 meV. Solche Niveaus heißen __quasikontinuierlich__. **Kontrolle am Kammpotential:** Aus zwei Töpfen kennt man $V_\mathrm{ss}=14{,}8$ meV bei $b=0{,}4$ nm. Das sagt $4V_\mathrm{ss}=59$ meV voraus, genau die Bandbreite aus Stufe [2](bander-und-lucken.html#stufe-2). Bei $b=0{,}2$ nm sind es 37,1 meV und 149 meV. Die Form weicht dort stärker vom Kosinus ab (14 % statt 6,5 % der Bandbreite), weil auch übernächste Nachbarn zählen.
::::

⁠**Grenzfall:** Für $|ka|\ll1$ ist $E\approx E_\mathrm s-2V_\mathrm{ss}+V_\mathrm{ss}a^2k^2$, das Band beginnt als Parabel.

:::frage Mit festen Enden gibt es nur $k>0$, im Band läuft $k$ von $-\pi/a$ bis $\pi/a$. Wo ist die andere Hälfte?
Die Zustände einer Kette mit festen Enden sind stehende Wellen, jede eine Überlagerung von $+k$ und $-k$. Bei periodischen Rändern gibt es laufende Wellen mit doppeltem Abstand der $k$, dafür beide Vorzeichen. Beide Male sind es $N$ Zustände.
:::

:::aufgabe Aufgabe 5 ★★ Dreißig Atome
<span class="anker" id="aufg-5"></span>

Eine Kette hat $N=30$, $E_\mathrm s=-4$ eV, $V_\mathrm{ss}=0{,}8$ eV und $a=0{,}3$ nm.

<ol class="al">

<li>

Berechne $E_1$, $E_{15}$, $E_{16}$ und $E_{30}$. Wie viel fehlt zur Breite des unendlichen Bands?

</li>

<li>

Berechne $E_2-E_1$ und $E_{16}-E_{15}$. Warum liegen die Niveaus am Bandrand dichter?

</li>

<li>

Bei welcher Länge ist der Abstand in der Mitte etwa 1 meV?

</li>

<li>

Wie groß ist $v_\text{max}$? Wo im Band ist $v=0$?

</li>

</ol>

:::loesung
(a) Mit $N+1=31$: $E_1=-5{,}592$, $E_{15}=-4{,}081$, $E_{16}=-3{,}919$, $E_{30}=-2{,}408$ eV. Die Spanne ist 3,184 eV, es fehlen 0,016 eV. (b) 24,5 meV und 162 meV. Gleiche $\Delta k$, und das Band ist am Rand flach. (c) In der Mitte ist $\Delta E\approx2V_\mathrm{ss}\pi/(N+1)$, also $N+1\approx5030$, Länge 1,5 µm. (d) $v_\text{max}=2V_\mathrm{ss}a/\hbar=7{,}3\cdot10^5$ m/s bei $k=\pi/(2a)$. $v=0$ gilt bei $k=0$ und am Zonenrand.
:::
:::

:::aufgabe Aufgabe 6 ★★★ Ein Ring aus sechs Atomen
<span class="anker" id="aufg-6"></span>

Sechs Atome bilden einen Ring: Auch Atom 6 und Atom 1 sind Nachbarn. Das ist der periodische Rand. Es gilt $E_\mathrm s=-5$ eV und $V_\mathrm{ss}=0{,}5$ eV.

<ol class="al">

<li>

Welche Einträge von $\boldsymbol H$ kommen gegenüber der Kette hinzu?

</li>

<li>

Zeige, dass $c_\ell=\mathrm{e}^{\mathrm{j} k\ell a}$ mit $k=n\cdot2\pi/(6a)$ die Gleichung löst, und berechne alle sechs Energien.

</li>

<li>

Welche Niveaus sind entartet, und warum? Vergleiche mit der offenen Kette aus sechs Atomen.

</li>

</ol>

:::loesung
(a) $H_{16}=H_{61}=-V_\mathrm{ss}$. (b) Jede Zeile lautet wie in Stufe [5](#stufe-5), auch Zeile 1 und 6, weil $\mathrm{e}^{\mathrm{j} k6a}=1$ ist. Für $n=-2,\dots,3$ ist $ka=n\pi/3$ und $E=E_\mathrm s-2V_\mathrm{ss}\cos(n\pi/3)$: $-6$; $-5{,}5$; $-5{,}5$; $-4{,}5$; $-4{,}5$; $-4$ eV. (c) $+k$ und $-k$ sind entartet, eine Welle läuft links herum, die andere rechts herum. Die offene Kette hat sechs verschiedene Werte von $-5{,}901$ bis $-4{,}099$ eV.
:::
:::
