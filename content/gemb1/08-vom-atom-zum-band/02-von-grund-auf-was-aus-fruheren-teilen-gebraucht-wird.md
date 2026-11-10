---
title: Von Grund auf: Was aus früheren Teilen gebraucht wird
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Vom Atom zum Band
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band
knoten: Kapitel 8: Vom Atom zum Band
order: 4180200
summary: Warum aus den scharfen Niveaus der Atome breite Energiebänder werden
tags: 
lang: de
---

⁠**[Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html).** Auf einem Gitter mit dem Punktabstand $a$ lautet die Schrödinger-Gleichung

<span class="anker" id="gl-0-1"></span>
$$-t_0\bigl(\psi_{\ell+1}-2\psi_\ell+\psi_{\ell-1}\bigr)+V_\ell\,\psi_\ell=E\,\psi_\ell,\qquad t_0=\frac{\hbar^2}{2ma^2}. \tag{0.1}$$

Als Matrix ist das $\boldsymbol H\boldsymbol\psi=E\boldsymbol\psi$ mit $2t_0+V_\ell$ auf der Hauptdiagonale und dem Hüpfparameter $-t_0$ daneben. Für $V_\ell=V_0$ löst $\psi_\ell=A\,\mathrm{e}^{\mathrm{j} k\ell a}$ die Gleichung, mit dem Kosinus-Band und der Geschwindigkeit

<span class="anker" id="gl-0-2"></span>
$$E(k)=2t_0\bigl(1-\cos(ka)\bigr)+V_0,\qquad v(k)=\frac1\hbar\,\frac{\partial E(k)}{\partial k}=\frac{2t_0a}{\hbar}\sin(ka),\qquad-\frac\pi a\le k\le\frac\pi a. \tag{0.2}$$

Dieser Bereich ist die erste Brillouin-Zone: $k$ und $k+2\pi/a$ ergeben an allen Punkten dieselben Zahlen.

⁠**[Kapitel 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html).** Im klassisch verbotenen Gebiet ($V>E$) fällt $\psi$ ab wie $\mathrm{e}^{-\kappa x}$ mit $\kappa=\sqrt{2m(V-E)}/\hbar$. Durch eine dünne Wand reicht die Welle hindurch, das ist der Tunneleffekt.

⁠**[Kapitel 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html) und 5.** Ein Orbital ist die Wellenfunktion eines Elektrons im Atom. Das s-Orbital ist kugelsymmetrisch, das p-Orbital hat zwei Keulen mit entgegengesetztem Vorzeichen. Jedes Orbital fasst nach dem Pauli-Prinzip höchstens zwei Elektronen mit entgegengesetztem Spin. Zwei Atome bilden ein bindendes und ein antibindendes Molekülorbital, getrennt durch die Kopplungsenergie $V_\mathrm{ss}$.

⁠**[Kapitel 7](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallwachstum-und-reziprokes-gitter/kristallwachstum-und-reziprokes-gitter.html).** In einer Kette ist $G=h_1\cdot2\pi/a$ mit ganzem $h_1$ ein reziproker Gittervektor. Ohne Potential kehrt deshalb die Parabel als Schar $E=\hbar^2(k+G)^2/(2m)$ wieder. Faltet man sie in die erste Zone, heißt das reduziertes Zonenschema. Wellen auf dem Zonenrand werden an den Netzebenen reflektiert.
