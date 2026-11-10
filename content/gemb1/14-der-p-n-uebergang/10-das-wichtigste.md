---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Der p-n-Übergang
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang
knoten: Kapitel 14: Der p-n-Übergang
order: 4241000
summary: Wie aus zwei dotierten Gebieten ein Ventil für Strom wird
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Bänder:** $E_i(x)=E_{i,\mathrm{Bulk}}-e\varphi(x)$, $\mathrm{d}^2\Phi/\mathrm{d} x^2=e\rho/(\varepsilon_0\varepsilon_\mathrm r)$.

</li>

<li>

⁠**Gleichgewicht:** $E_\mathrm F$ konstant, $\Phi_\mathrm{bi}=eU_\mathrm d=k_\mathrm BT\ln\bigl(N_\mathrm AN_\mathrm D/n_\mathrm i^2\bigr)=k_\mathrm BT\ln(n_\mathrm{n0}/n_\mathrm{p0})$.

</li>

<li>

⁠**Näherungen:** $L_\mathrm{Deb}=\sqrt{\varepsilon_0\varepsilon_\mathrm rk_\mathrm BT/(e^2n_0)}$. Schottky-Kasten für $L_\mathrm{depl}\gg L_\mathrm{Deb}$.

</li>

<li>

⁠**Zone:** $L_\mathrm{depl}^\mathrm AN_\mathrm A=L_\mathrm{depl}^\mathrm DN_\mathrm D$, $L_\mathrm{depl}=\sqrt{\frac{2\varepsilon U_\mathrm d}{e}\frac{N_\mathrm A+N_\mathrm D}{N_\mathrm AN_\mathrm D}}$, $|\mathcal E_\mathrm{max}|=2U_\mathrm d/L_\mathrm{depl}$.

</li>

<li>

⁠**Spannung:** $\Phi_\mathrm{bi}\to\Phi_\mathrm{bi}-eU_\mathrm{pn}$, $E_\mathrm{Fn}-E_\mathrm{Fp}=eU_\mathrm{pn}$, $n\,p=n_\mathrm i^2\mathrm{e}^{(E_\mathrm{Fn}-E_\mathrm{Fp})/(k_\mathrm BT)}$.

</li>

<li>

⁠**Injektion:** $\Delta n_\mathrm p=n_\mathrm{p0}\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr)$ am Rand, Abklingen auf $L_\text{diff,n}$.

</li>

<li>

⁠**Kennlinie:** $j=j_\mathrm s\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr)$, $j_\mathrm s=eD_\mathrm pp_\mathrm{n0}/L_\text{diff,p}+eD_\mathrm nn_\mathrm{p0}/L_\text{diff,n}=e\sqrt{D_\mathrm p/\tau_{\text{rec},\mathrm p}}\,n_\mathrm i^2/N_\mathrm D+e\sqrt{D_\mathrm n/\tau_{\text{rec},\mathrm n}}\,n_\mathrm i^2/N_\mathrm A$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

An der Grenze diffundieren Träger in das jeweils andere Gebiet und lassen feste Ionen zurück, deren Feld die Bänder um $\Phi_\mathrm{bi}$ verbiegt, bis die Fermi-Energie überall gleich ist und Drift die Diffusion aufhebt.

</li>

<li>

Eine Spannung verschiebt die Barriere und trennt die Quasi-Fermi-Niveaus um $eU_\mathrm{pn}$, dadurch ändert sich die Minoritätsdichte am Zonenrand um den Faktor $\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}$.

</li>

<li>

Der Strom ist die Diffusion dieser Minoritäten: Bei Durchlass wächst er je 60 mV um den Faktor 10, bei Sperrung bleibt nur der kleine, spannungsunabhängige Strom $-j_\mathrm s$ der thermisch erzeugten Minoritäten.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Die Dichte jeder Sorte folgt dem Boltzmann-Faktor des Abstands zwischen Bandkante und ihrem Fermi-Niveau, und die Poisson-Gleichung macht aus der Ladung die Bandverbiegung. Alles Weitere ist die Frage, wo welches Niveau liegt.

| Ergebnis | Woher es kommt |
|---|---|
| Bänder verbiegen sich, Lücke bleibt | Das Potential verschiebt alle Zustände am Ort gleich (Stufe [1](wie-ladung-die-bander-verbiegt.html#stufe-1)) |
| $\Phi_\mathrm{bi}=k_\mathrm BT\ln(N_\mathrm AN_\mathrm D/n_\mathrm i^2)$ | Das Dichteverhältnis passt zum Boltzmann-Faktor (Stufe [2](der-ubergang-im-gleichgewicht.html#stufe-2)) |
| Kastenprofil, zwei Parabeln | Die Dichte fällt über wenige $k_\mathrm BT$ (Stufe [3](zwei-naherungen-fur-die-ladung.html#stufe-3) und [4](feld-potential-und-weite-der-zone.html#stufe-4)) |
| $E_\mathrm{Fn}-E_\mathrm{Fp}=eU_\mathrm{pn}$ | Jede Sorte ist unter sich schneller im Gleichgewicht (Stufe [5](spannung-anlegen.html#stufe-5)) |
| Randdichte $n_\mathrm{p0}\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}$ | $E_\mathrm{Fn}$ läuft flach durch die Zone (Stufe [6](injektion-und-minoritatstrager.html#stufe-6)) |
| $I=I_\mathrm S(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1)$ | Der Strom ist die Steigung des Profils am Rand (Stufe [7](die-diodenkennlinie.html#stufe-7)) |
