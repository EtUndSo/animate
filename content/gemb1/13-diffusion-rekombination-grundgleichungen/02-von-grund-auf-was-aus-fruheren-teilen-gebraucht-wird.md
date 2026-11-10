---
title: Von Grund auf: Was aus früheren Teilen gebraucht wird
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen
knoten: Kapitel 13: Diffusion, Rekombination und Grundgleichungen
order: 4230200
summary: Wie weit zusätzliche Ladungsträger kommen und welche Gleichungen alles zusammenfassen
tags: Mehrheit, Minderheit, Gradient, Divergenz, Laplace-Operator
lang: de
---

⁠**Dichten ([Kapitel 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html) und 11).** Im Gleichgewicht gilt $n=N_\mathrm C\exp(-(E_\mathrm C-E_\mathrm F)/(k_\mathrm BT))$ und $n\,p=n_\mathrm i^2$. Im n-Gebiet ist $n\approx N_\mathrm D$, die Elektronen sind die __Mehrheit__, die Löcher mit $p=n_\mathrm i^2/N_\mathrm D$ die __Minderheit__. Ein Stück Kristall ist neutral, $p+N_\mathrm D^+-n-N_\mathrm A^-=0$.

⁠**Strom ([Kapitel 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)).** Ein Feld $\mathcal E$ treibt die elektrische Stromdichte $j=e\,n\,\mu_\mathrm n\mathcal E$ mit der Beweglichkeit $\mu_\mathrm n=e\tau_\text{scat}/m^*$, und $\sigma=e(n\mu_\mathrm n+p\mu_\mathrm p)$. $\tau_\text{scat}$ ist die mittlere Zeit zwischen zwei Stößen, $l_\mathrm{mfp}$ der Weg dazwischen. Die Verteilung $f(x,k,t)$ folgt der Boltzmann-Gleichung

<span class="anker" id="gl-0-1"></span>
$$\frac{\partial f}{\partial t}+v\,\frac{\partial f}{\partial x}+\frac F\hbar\,\frac{\partial f}{\partial k}=-\frac{f-f^0}{\tau_\text{scat}}. \tag{0.1}$$

Bandkante und Potential hängen über $E_\mathrm C=\text{konst}-e\varphi$ zusammen, $\mathcal E=-\mathrm{d}\varphi/\mathrm{d} x$. Im Gleichgewicht ist $E_\mathrm F$ waagerecht, also $0=\mathrm{d} E_\mathrm F/\mathrm{d} x=e\mathcal E+(k_\mathrm BT/n)\,\mathrm{d} n/\mathrm{d} x$: Feld und Dichtegefälle halten sich die Waage.

⁠**Schreibweise.** Der __Gradient__ $\operatorname{grad}N=\nabla N$ ist der Vektor der drei Ortsableitungen und zeigt zum stärksten Anstieg. Die __Divergenz__ $\operatorname{div}\boldsymbol a=\nabla\cdot\boldsymbol a=\partial a_x/\partial x+\partial a_y/\partial y+\partial a_z/\partial z$ misst, wie viel aus einem kleinen Volumen netto herausströmt. Der __Laplace-Operator__ ist $\Delta=\operatorname{div}\operatorname{grad}=\partial^2/\partial x^2+\partial^2/\partial y^2+\partial^2/\partial z^2$.
