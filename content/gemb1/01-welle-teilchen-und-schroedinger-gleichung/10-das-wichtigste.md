---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung
knoten: Kapitel 1: Welle, Teilchen und Schrödinger-Gleichung
order: 4111000
summary: Was ein Elektron im Material ist und wie man es berechnet
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

Stoffgrößen: $j=\sigma\mathcal E$, Gasmodell $\sigma=e\,n\,\mu$, $\mu=e\tau/m_0$, $v_\mathrm d=-\mu\mathcal E$, $v_\mathrm e=\sqrt{3k_\mathrm BT/m_0}$.

</li>

<li>

Teilchen sind Wellen: $E=\hbar\omega$, $p=h/\lambda=\hbar k$.

</li>

<li>

$|\Psi|^2$ ist die Wahrscheinlichkeitsdichte, $\int|\Psi|^2\,\mathrm{d} x=1$. Wellenfunktionen addieren sich, erst die Summe wird quadriert.

</li>

<li>

$\hat p=(\hbar/\mathrm{j})\,\partial/\partial x$, $\hat E=\mathrm{j}\hbar\,\partial/\partial t$. Zeitabhängig: $\mathrm{j}\hbar\,\partial_t\Psi=\hat H\Psi$, $\hat H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V$.

</li>

<li>

Stationär: $\Psi=\psi(x)\mathrm{e}^{-\mathrm{j} Et/\hbar}$, $\hat H\psi=E\psi$ (Eigenwertgleichung), $|\Psi|^2$ zeitlich fest.

</li>

<li>

Konstantes Potential: ebene Welle $\psi=\mathrm{e}^{\mathrm{j} kx}/\sqrt L$ und $E(k)=\hbar^2k^2/(2m)+V_0=E_\mathrm{kin}+E_\mathrm{pot}$, in 3D die Summe über $k_x,k_y,k_z$.

</li>

<li>

Wellenpaket: $\psi(x)=\int c(k)\mathrm{e}^{\mathrm{j} kx}\mathrm{d} k$, $\Delta x\,\Delta p\ge\hbar/2$.

</li>

<li>

$v=\frac1\hbar\frac{\partial E}{\partial k}$ (Steigung), $m=\bigl(\frac1{\hbar^2}\frac{\partial^2E}{\partial k^2}\bigr)^{-1}$ (Krümmung), $\mathrm{d} k/\mathrm{d} t=F/\hbar$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Elektron ist weder Kugel noch ausgedehnte Ladung: Eine komplexe Wellenfunktion bestimmt, wie wahrscheinlich es an einem Ort auftaucht.

</li>

<li>

Die Wellenfunktion gehorcht der Schrödinger-Gleichung. Bei zeitlich festem Potential ist sie eine Eigenwertgleichung, deren Eigenwerte die erlaubten Energien sind.

</li>

<li>

Bei konstantem Potential sind die Lösungen ebene Wellen mit der Parabel $E(k)$. Aus ihr liest man Impuls $\hbar k$, Geschwindigkeit (Steigung) und Masse (Kehrwert der Krümmung) ab.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Impuls und Energie sind Eigenschaften einer Welle: $p=\hbar k$, $E=\hbar\omega$. Fast alles in diesem Kapitel folgt daraus, sobald man fragt, was die Welle jeweils tut.

| Ergebnis | Woher es kommt |
|---|---|
| Gasmodell scheitert | Es behandelt Elektronen als Kugeln, ihre Wellenlänge ist aber größer als der Atomabstand (Stufe [2](teilchen-und-wellen.html#stufe-2)) |
| Streifen im Doppelspalt | Zeiger addieren sich vor dem Quadrieren (Stufe [3](die-wellenfunktion-und-ihre-deutung.html#stufe-3)) |
| Operatoren $\hat p$ und $\hat E$ | Ableiten liest aus der Welle $k$ und $\omega$ ab (Stufe [4](die-schrodinger-gleichung.html#stufe-4)) |
| Parabel $E(k)$ | Zweimal Ableiten von $\mathrm{e}^{\mathrm{j} kx}$ gibt $-k^2$ (Stufe [5](freies-elektron-ebene-welle-dispersion.html#stufe-5)) |
| Unschärferelation | Eine enge Hülle braucht viele Wellenzahlen (Stufe [6](das-wellenpaket.html#stufe-6)) |
| $v$ aus der Steigung | Die Hülle einer Schwebung läuft mit $\partial\omega/\partial k$ (Stufe [6](das-wellenpaket.html#stufe-6)) |
| $m$ aus der Krümmung | Eine Kraft ändert $k$, die Krümmung übersetzt das in $v$ (Stufe [7](was-die-parabel-verrat.html#stufe-7)) |
