---
title: Von Grund auf: Was aus Teil 15 gebraucht wird
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260200
summary: Was einen gebauten Kondensator vom idealen unterscheidet und wie die Kapazität es verrät
tags: 
lang: de
---

⁠**Energien.** Die Austrittsarbeit ist $\Phi=E_\mathrm{vac}-E_\mathrm F$. Für den Halbleiter gilt

<span class="anker" id="gl-0-1"></span>
$$\Phi_\mathrm{SC}=\chi_\mathrm{SC}+\frac{E_\mathrm g}{2}+\bigl(E_\mathrm{Fi,\infty}-E_\mathrm F\bigr). \tag{0.1}$$

Die Klammer ist im p-Gebiet positiv und im n-Gebiet negativ, ihr Betrag ist $k_\mathrm BT\ln(N/n_\mathrm i)$. Das Vakuumniveau $E_\mathrm{vac}$ folgt dem Potential und läuft stetig durch die ganze Struktur. Liegt am Gate die Spannung $V_\mathrm G$ gegen das Substrat, ist $E_\mathrm F-E_\mathrm{F,M}=eV_\mathrm G$.

⁠**Ideale Bilanz.** Die Gatespannung teilt sich auf: $V_\mathrm G=V_\mathrm{IS}+\varphi_\mathrm s$ mit $V_\mathrm{IS}=-Q'_\mathrm{SC}/C'_\mathrm{IS}$ und $C'_\mathrm{IS}=\varepsilon_\mathrm{IS}/d_\mathrm{IS}$. In Verarmung ist $Q'_\mathrm{SC}=-eN_\mathrm AL_\mathrm{depl}=-\sqrt{2\varepsilon eN_\mathrm A\varphi_\mathrm s}$, also $V_\mathrm G=\varphi_\mathrm s+\gamma\sqrt{\varphi_\mathrm s}$ mit $\gamma=\sqrt{2\varepsilon eN_\mathrm A}/C'_\mathrm{IS}$. Starke Inversion beginnt bei $\varphi_\mathrm{s,SI}=2\varphi_\mathrm{s,WI}=2V_\mathrm T\ln(N_\mathrm A/n_\mathrm i)$.

⁠**Kapazität.** Isolator und Halbleiter liegen in Reihe, $1/C'_\mathrm{ges}=1/C'_\mathrm{IS}+1/C'_\mathrm{SC}$ mit $C'_\mathrm{SC}=|\mathrm{d} Q'_\mathrm{SC}/\mathrm{d}\varphi_\mathrm s|$. In Verarmung ist $C'_\mathrm{SC}=C'_\mathrm{depl}=\varepsilon/L_\mathrm{depl}$.
