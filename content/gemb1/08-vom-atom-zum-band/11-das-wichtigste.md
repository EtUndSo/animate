---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Vom Atom zum Band
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band
knoten: Kapitel 8: Vom Atom zum Band
order: 4181100
summary: Warum aus den scharfen Niveaus der Atome breite Energiebänder werden
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Periodizität:** $V(x+a)=V(x)$ erzwingt $\psi_k=\mathrm{e}^{\mathrm{j} kx}u_k(x)$ und $E(k+G)=E(k)$. Alle $N$ Zustände liegen in der ersten Brillouin-Zone.

</li>

<li>

⁠**Zwei Atome:** $\psi=c_1\phi_1+c_2\phi_2$, $E=E_\mathrm s\mp V_\mathrm{ss}$ mit $-V_\mathrm{ss}=\langle1|\hat H|2\rangle$. Gleiches Vorzeichen bindet.

</li>

<li>

⁠**Matrix:** Projektion ergibt ein reguläres Eigenwertproblem mit Hauptdiagonale $E_\mathrm s$, Nebendiagonale $-V_\mathrm{ss}$ und $\det|\boldsymbol H-E\mathbf1|=0$.

</li>

<li>

⁠**Viele Atome:** $E_n=E_\mathrm s-2V_\mathrm{ss}\cos(n\pi/(N+1))$, für große $N$ das Band $E(k)=E_\mathrm s-2V_\mathrm{ss}\cos(ka)$ der Breite $4V_\mathrm{ss}$, $v(k)=(2V_\mathrm{ss}a/\hbar)\sin(ka)$.

</li>

<li>

⁠**Bändermodell:** Jedes Atomniveau wird ein Band mit $N$ Zuständen und $2N$ Plätzen. Dünne oder niedrige Barrieren: breite Bänder, kleine Lücken. Teilweise voll: Metall. Voll: Isolator oder, bei kleiner Lücke, Halbleiter.

</li>

<li>

⁠**Rezept:** $M$ Orbitale in der Zelle, $M$ Bänder. Nachbarmatrizen mal $\mathrm{e}^{\pm\mathrm{j} ka}$, Summe minus $E\cdot\mathbf1$, Determinante null.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Rücken Atome zusammen, überlappen ihre Orbitale, und jedes Niveau spaltet: zwei Atome ergeben zwei Niveaus, $N$ Atome ein Band aus $N$ Zuständen.

</li>

<li>

Die Breite des Bands ist viermal die Kopplung, und die Kopplung fällt exponentiell mit Abstand und Barriere.

</li>

<li>

Bänder aus verschiedenen Niveaus bleiben durch Lücken getrennt, und die Zahl der Elektronen entscheidet dann über Metall, Halbleiter oder Isolator.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Kopplung spaltet Niveaus. Fast alles hier ist die Frage, wie viele gleiche Zustände gekoppelt sind und wie stark.

| Ergebnis | Woher es kommt |
|---|---|
| $E(k+G)=E(k)$ | Verschieben um $a$ ändert nichts Messbares (Stufe [1](was-aus-der-periodizitat-folgt.html#stufe-1)) |
| Bänder und Lücken | Tunneln koppelt Töpfe, Bragg-Reflexion am Rand (Stufe [2](bander-und-lucken.html#stufe-2)) |
| $E_\mathrm s\mp V_\mathrm{ss}$ | Zwei gleiche Zustände, gekoppelt über den Überlapp (Stufe [3](zwei-atome.html#stufe-3)) |
| Drei Diagonalen in $\boldsymbol H$ | Exponentieller Abfall, nur Nachbarn koppeln (Stufe [4](vier-atome-und-die-matrix.html#stufe-4)) |
| Band der Breite $4V_\mathrm{ss}$ | $N$ gekoppelte Zustände, je zwei Nachbarn (Stufe [5](viele-atome.html#stufe-5)) |
| Bändermodell | Überlapp der exponentiellen Ausläufer (Stufe [6](bandbreite-abstand-und-besetzung.html#stufe-6)) |
| Lücke zwischen s- und p-Band | Zwei Niveaus, jedes um seine Kopplung verbreitert (Stufe [7](zwei-orbitale-je-atom.html#stufe-7)) |
| Rezept mit $M\times M$-Matrizen | Periodizität ersetzt Nachbarzellen durch Phasen (Stufe [8](das-rezept.html#stufe-8)) |
