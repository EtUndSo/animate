---
title: Von Grund auf: Wellen bei konstantem Potential, Rechnen in eV
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4130200
summary: Was eine Elektronenwelle an einer endlich hohen Wand tut
tags: elastische Reflexion, klassisch verbotenes Gebiet
lang: de
---

Ein Elektron hat die Gesamtenergie $E$. In einem Gebiet mit konstanter potentieller Energie $V$ lautet die zeitunabhängige Schrödinger-Gleichung aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html) nach Umstellen

<span class="anker" id="gl-0-1"></span>
$$\frac{\mathrm{d}^2\psi}{\mathrm{d} x^2}=-k^2\,\psi\qquad\text{mit}\qquad k^2=\frac{2m(E-V)}{\hbar^2}. \tag{0.1}$$

$V$ ist in diesem Kapitel immer eine Energie in eV, keine Spannung. Für $E>V$ ist $k$ reell, und die allgemeine Lösung ist $\psi(x)=A\,\mathrm{e}^{\mathrm{j} kx}+B\,\mathrm{e}^{-\mathrm{j} kx}$. Mit dem Zeitfaktor aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html), $\mathrm{e}^{-\mathrm{j}\omega t}$ mit $\omega=E/\hbar$, wird daraus

<span class="anker" id="gl-0-2"></span>
$$\Psi(x,t)=A\,\mathrm{e}^{\mathrm{j}(kx-\omega t)}+B\,\mathrm{e}^{-\mathrm{j}(kx+\omega t)}. \tag{0.2}$$

Der erste Term wandert in positive $x$-Richtung, der zweite in negative. Läuft die Welle nur in eine Richtung, ist $A=0$ oder $B=0$. Wird sie irgendwo reflektiert, sind beide Amplituden von null verschieden. Bleibt die Energie dabei gleich, heißt das __elastische Reflexion__. Dann bleiben auch $k$ und $\omega$ gleich, und einlaufende und reflektierte Welle überlagern sich zu einer stehenden Welle mit ortsfesten Knoten und Bäuchen. Bei vollständiger Reflexion ist $|A|=|B|$. Die Box aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) ist dafür das Beispiel.

Klassisch gilt $E=E_\mathrm{kin}+V$ mit $E_\mathrm{kin}\ge0$. Ein Gebiet mit $E<V$ heißt deshalb __klassisch verbotenes Gebiet__: Dort wäre die kinetische Energie negativ.

**Rechnen in eV und nm.** Energien stehen hier in Elektronenvolt ([Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html)), Längen in nm. In eV ausgedrückt ist $\hbar=6{,}582\cdot10^{-16}\,\mathrm{eV\,s}$ und $m_0=5{,}686\cdot10^{-12}\,\mathrm{eV\,s^2/m^2}$, das entspricht $m_0c^2=5{,}11\cdot10^{5}$ eV mit der Lichtgeschwindigkeit $c$. Damit kürzt eine Zahl alle Rechnungen ab:

<span class="anker" id="gl-0-3"></span>
$$\frac{2m_0}{\hbar^2}=\frac{1}{0{,}0381\,\mathrm{eV\,nm^2}}=26{,}25\,\mathrm{\frac{1}{eV\,nm^2}},\quad k=5{,}123\,\mathrm{\frac1{nm}}\cdot\sqrt{\frac{E-V}{\mathrm{eV}}},\quad\lambda=\frac{2\pi}{k}=\frac{1{,}226\,\mathrm{nm}}{\sqrt{(E-V)/\mathrm{eV}}}. \tag{0.3}$$

Bei 1 eV kinetischer Energie ist $\lambda=1{,}226$ nm. Das ist die Größenordnung dünner Schichten, deshalb zählt die Wellennatur in Bauelementen.
