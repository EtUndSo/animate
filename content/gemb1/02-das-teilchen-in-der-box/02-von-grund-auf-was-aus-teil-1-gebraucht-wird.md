---
title: Von Grund auf: Was aus Kapitel 1 gebraucht wird
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Das Teilchen in der Box
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box
knoten: Kapitel 2: Das Teilchen in der Box
order: 4120200
summary: Warum ein eingesperrtes Elektron nur bestimmte Energien hat
tags: 
lang: de
---

Ein Elektron wird durch seine Wellenfunktion $\psi$ beschrieben. $|\psi(x)|^2\,\mathrm{d} x$ ist die Wahrscheinlichkeit, es im kleinen Stück $\mathrm{d} x$ zu finden, also gilt $\int|\psi|^2\,\mathrm{d} x=1$. $V(x)$ ist die potentielle Energie des Elektrons am Ort $x$, kurz Potential. Hängt $V$ nicht von der Zeit ab, gilt die zeitunabhängige Schrödinger-Gleichung

<span class="anker" id="gl-0-1"></span>
$$-\frac{\hbar^2}{2m}\,\frac{\mathrm{d}^2\psi}{\mathrm{d} x^2}+V(x)\,\psi(x)=E\,\psi(x). \tag{0.1}$$

Der erste Term ist die kinetische Energie. Er misst die Krümmung von $\psi$, gemeint ist hier die zweite Ableitung. Die linke Seite ist $\hat H\psi$ mit dem Hamilton-Operator $\hat H$, und [(0.1)](#gl-0-1) ist eine Eigenwertgleichung: Die Eigenwerte $E$ sind die erlaubten Energien. Für konstantes $V=V_0$ lösen ebene Wellen $\mathrm{e}^{\pm\mathrm{j} kx}$ die Gleichung, mit der Dispersionsrelation $E(k)=\hbar^2k^2/(2m)+V_0$ und $k=2\pi/\lambda$. Aus dieser Kurve folgen der Impuls $p=\hbar k=h/\lambda$ und die Gruppengeschwindigkeit $v=\frac1\hbar\,\partial E/\partial k$. $\mathrm{j}$ ist die imaginäre Einheit.
