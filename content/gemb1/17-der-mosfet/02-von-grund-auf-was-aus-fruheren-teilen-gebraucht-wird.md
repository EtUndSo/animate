---
title: Von Grund auf: Was aus früheren Teilen gebraucht wird
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270200
summary: Wie eine isolierte Elektrode den Strom zwischen zwei Kontakten steuert
tags: 
lang: de
---

⁠**MOS-Kondensator ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html) und 16).** Eine Spannung $V_\mathrm G$ zwischen Gate und Substrat teilt sich auf Isolator und Halbleiter auf:

<span class="anker" id="gl-0-1"></span>
$$V_\mathrm G=V_\mathrm{FB}+\varphi_\mathrm s-\frac{Q'_\mathrm{SC}}{C'_\mathrm{IS}},\qquad C'_\mathrm{IS}=\frac{\varepsilon_\mathrm{IS}}{d_\mathrm{IS}},\qquad V_\mathrm{FB}=\frac{\Phi_\mathrm M-\Phi_\mathrm{SC}}{e}-\frac{Q'_\mathrm{IS}+Q'_\mathrm{SS}}{C'_\mathrm{IS}}. \tag{0.1}$$

$V_\mathrm{FB}$ ist die Flachbandspannung, $\varphi_\mathrm s$ das Oberflächenpotential, $Q'_\mathrm{SC}$ die Flächenladung im Halbleiter. Ein Strich kennzeichnet Größen je Fläche. In Verarmung und schwacher Inversion ist $Q'_\mathrm{SC}=-\sqrt{2\varepsilon eN_\mathrm A\varphi_\mathrm s}$ mit der Zonenweite $L_\mathrm{depl}=\sqrt{2\varepsilon\varphi_\mathrm s/(eN_\mathrm A)}$. An der Grenzfläche gilt

<span class="anker" id="gl-0-2"></span>
$$n(0)=n_{p0}\exp\Bigl(\frac{\varphi_\mathrm s}{V_\mathrm T}\Bigr),\qquad\varphi_\mathrm{s,WI}=V_\mathrm T\ln\frac{N_\mathrm A}{n_\mathrm i},\qquad\varphi_\mathrm{s,SI}=2\varphi_\mathrm{s,WI}. \tag{0.2}$$

Im Rechenmodell ist $\varphi_\mathrm{s,WI}=0{,}389$ V und $\varphi_\mathrm{s,SI}=0{,}777$ V. Oberhalb der Schwellspannung $V_\mathrm{th}$ liefert fast nur noch die Inversionsladung $Q'_\mathrm{inv}\approx-C'_\mathrm{IS}(V_\mathrm G-V_\mathrm{th})$ die zusätzliche Ladung.

⁠**p-n-Übergang ([Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html)).** Ein Elektron sieht zwischen n- und p-Gebiet die Barriere $\Phi_\mathrm{bi}=k_\mathrm BT\ln(N_\mathrm AN_\mathrm D/n_\mathrm i^2)$. Eine Spannung $U_\mathrm{pn}$ senkt sie um $eU_\mathrm{pn}$, und es gilt $j=j_\mathrm s\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr)$.

⁠**Transport ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html) und 13).** Die Driftstromdichte ist $j=e\,n\,\mu\,\mathcal E$, die Diffusionsstromdichte der Elektronen $j=eD_\mathrm n\,\mathrm{d} n/\mathrm{d} y$, und es gilt $D_\mathrm n=\mu_\mathrm n\,k_\mathrm BT/e$.
