---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Die MOS-Kapazität
order: 4251100
summary: Wie eine Spannung am Gate die Oberfläche eines Halbleiters umdreht
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Ideal:** $\Phi_\mathrm M=\Phi_\mathrm{SC}=\chi_\mathrm{SC}+E_\mathrm g/2+(E_\mathrm{Fi,\infty}-E_\mathrm F)$, keine Ladungen, kein Strom, $V_\mathrm{FB}=0$.

</li>

<li>

⁠**Bilanz:** $V_\mathrm G=\varphi_\mathrm s-Q'_\mathrm{SC}/C'_\mathrm{IS}$, $e\varphi_\mathrm s=E_\mathrm{C,\infty}-E_\mathrm{C,0}$, $p(0)=N_\mathrm A\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}$, $n(0)=n_{p0}\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}$.

</li>

<li>

⁠**Abschirmung:** $L_\mathrm D=\sqrt{\varepsilon k_\mathrm BT/(e^2N_\mathrm A)}$.

</li>

<li>

⁠**Verarmung:** $L_\mathrm{depl}=\sqrt{2\varepsilon\varphi_\mathrm s/(eN_\mathrm A)}$, $Q'_\mathrm{SC}=-\sqrt{2\varepsilon eN_\mathrm A\varphi_\mathrm s}$.

</li>

<li>

⁠**Inversion:** $\varphi_\mathrm{s,WI}=V_\mathrm T\ln(N_\mathrm A/n_\mathrm i)$, $\varphi_\mathrm{s,SI}=2\varphi_\mathrm{s,WI}$, $V_\mathrm{th}=\varphi_\mathrm{s,SI}+\gamma\sqrt{\varphi_\mathrm{s,SI}}$, $\gamma=\sqrt{2\varepsilon eN_\mathrm A}/C'_\mathrm{IS}$.

</li>

<li>

⁠**Kapazität:** $1/C'_\mathrm{ges}=1/C'_\mathrm{IS}+1/C'_\mathrm{SC}$. Akkumulation und starke Inversion: $C'_\mathrm{ges}\approx C'_\mathrm{IS}$. Verarmung: $C'_\mathrm{SC}=\varepsilon/L_\mathrm{depl}$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Die Gatespannung teilt sich auf den Isolator und die Bandverbiegung $\varphi_\mathrm s$ auf, und $\varphi_\mathrm s$ verschiebt die Bänder gegen das waagerechte $E_\mathrm F$, sodass sich die Dichten an der Grenzfläche um den Faktor 10 je 60 mV ändern.

</li>

<li>

Bei $V_\mathrm G<0$ sammeln sich Löcher in einer dünnen Schicht, bei kleinem $V_\mathrm G>0$ bleibt eine wachsende Zone aus Ionen zurück, und ab $\varphi_\mathrm{s,SI}=2V_\mathrm T\ln(N_\mathrm A/n_\mathrm i)$ übernehmen Elektronen die Ladung.

</li>

<li>

Deshalb ist die Kapazität gleich $C'_\mathrm{IS}$, solange die Ladung direkt am Isolator sitzt, und kleiner, solange sie sich am Rand der Verarmungszone ändert.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Das Gate verlangt eine Gegenladung. Der Halbleiter liefert sie in der Form, die gerade am wenigsten Bandverbiegung kostet: bewegliche Ladung direkt am Isolator, wenn es sie gibt, sonst feste Ionen in der Tiefe.

| Ergebnis | Woher es kommt |
|---|---|
| Flachband ohne Spannung | Gleiche Austrittsarbeit, keine Ladung (Stufe [1](drei-stoffe-auf-einer-energieskala.html#stufe-1)) |
| Faktor 10 je 60 mV | $E_\mathrm F$ waagerecht, Boltzmann-Faktor folgt der Bandkante (Stufe [2](wie-sich-die-gatespannung-aufteilt.html#stufe-2)) |
| $L_\mathrm D\propto1/\sqrt N$ | Drift gegen Diffusion, wenige Träger schirmen schlecht (Stufe [3](abschirmung-und-akkumulation.html#stufe-3)) |
| $L_\mathrm{depl}\propto\sqrt{\varphi_\mathrm s}$ | Feste Ionendichte, Ladung und Abstand wachsen zugleich (Stufe [4](verarmung.html#stufe-4)) |
| $\varphi_\mathrm{s,SI}=2\varphi_\mathrm{s,WI}$ | Abstand $E_\mathrm{Fi}$ zu $E_\mathrm F$ abbauen und spiegeln (Stufe [5](inversion.html#stufe-5)) |
| $V_\mathrm{th}$ | Bandverbiegung plus Ionenladung über dem Isolator (Stufe [6](die-schwellspannung.html#stufe-6)) |
| Stufen in $D_\mathrm s$ | Der enge Topf quantisiert die Bewegung (Stufe [7](die-inversionsschicht-als-quantentopf.html#stufe-7)) |
| $C'_\mathrm{ges}\approx C'_\mathrm{IS}$ | Bewegliche Ladung sitzt direkt am Isolator (Stufe [8](die-kapazitat-in-allen-bereichen.html#stufe-8)) |
