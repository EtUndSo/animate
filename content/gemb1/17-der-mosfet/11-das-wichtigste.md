---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4271100
summary: Wie eine isolierte Elektrode den Strom zwischen zwei Kontakten steuert
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Aufbau:** Zwei n$^+$-Gebiete im p-Substrat, dazwischen ein MOS-Kondensator. Strom in $y$, Länge $L$, Weite $W$.

</li>

<li>

⁠**Barriere:** $E_\mathrm b=\Phi_\mathrm{bi}-e\varphi_\mathrm s$. Das Gate senkt sie, Injektion durch Diffusion bis zur Spitze, dahinter Drift.

</li>

<li>

⁠**Gradual Channel:** $Q'_\mathrm{inv}(y)=-C'_\mathrm{IS}(V_\mathrm{GS}-V_\mathrm{th}-V(y))$, $K=\mu_\mathrm n(\varepsilon_\mathrm{IS}/d_\mathrm{IS})(W/L)$.

</li>

<li>

⁠**Kennlinien:** ungesättigt $I_\mathrm D=K[(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}-\frac12V_\mathrm{DS}^2]$, ohmsch $I_\mathrm D\approx K(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}$, Sättigung $I_\mathrm D=\frac K2(V_\mathrm{GS}-V_\mathrm{th})^2$ ab $V_\mathrm{DS,sat}=V_\mathrm{GS}-V_\mathrm{th}$.

</li>

<li>

⁠**Schwelle:** $V_\mathrm{th}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}+\gamma\sqrt{\varphi_\mathrm{s,SI}+V_\mathrm{SB}}$.

</li>

<li>

⁠**Aus-Zustand:** $I_\mathrm D\propto\exp(\varphi_\mathrm s/V_\mathrm T)$, $S=V_\mathrm T\ln(10)(C'_\mathrm{IS}+C'_\mathrm{depl})/C'_\mathrm{IS}\ge60$ mV/Dekade.

</li>

<li>

⁠**Typen:** n- oder p-Kanal, Anreicherung ($V_\mathrm{th}$ sperrt bei $V_\mathrm{GS}=0$) oder Verarmung (leitet bei $V_\mathrm{GS}=0$).

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Das isolierte Gate senkt die Barriere zwischen Source und Kanal und legt über den Plattenkondensator fest, wie viel Ladung an jeder Stelle im Kanal sitzt, und der Strom ist diese Ladung mal Beweglichkeit mal Feld.

</li>

<li>

Weil die Ladung zum Drain hin abnimmt, wächst der Strom mit $V_\mathrm{DS}$ immer langsamer und bleibt ab der Abschnürung bei $V_\mathrm{DS,sat}=V_\mathrm{GS}-V_\mathrm{th}$ konstant, nämlich $\frac K2(V_\mathrm{GS}-V_\mathrm{th})^2$.

</li>

<li>

Unter $V_\mathrm{th}$ bleibt ein Diffusionsstrom, der exponentiell mit der Barriere fällt, und weil das Gate die Oberfläche nur über einen kapazitiven Teiler erreicht, braucht eine Dekade mindestens 60 mV.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Das Gate legt fest, wie viele Elektronen zwischen Source und Drain sitzen, ohne dass es selbst Strom führt. Jedes Ergebnis fragt nur, wie viel Ladung dort ist und was sie bewegt.

| Ergebnis | Woher es kommt |
|---|---|
| Sperren ohne Gatespannung | Zwei gegeneinander liegende p-n-Übergänge (Stufe [1](zwei-kontakte-am-mos-kondensator.html#stufe-1)) |
| Kein Strom bei $V_\mathrm{DS}=0$ | Source und Drain besetzen $\pm k_y$ gleich (Stufe [2](die-barriere-im-kanal.html#stufe-2)) |
| Parabel in $V_\mathrm{DS}$ | Ladung sinkt längs des Kanals, Strom bleibt gleich (Stufe [3](gradual-channel-approximation.html#stufe-3)) |
| $I_\mathrm D$ konstant in Sättigung | Am Drain abgeschnürt, nur noch die Source liefert (Stufe [4](ausgangskennlinien.html#stufe-4)) |
| Lage von $V_\mathrm{th}$ | Materialausgleich, Bandverbiegung, Ionenladung (Stufe [5](transferkennlinie-und-schwellspannung.html#stufe-5)) |
| $S\ge60$ mV/Dekade | Boltzmann-Verteilung der Source, kapazitiver Teiler (Stufe [6](der-aus-zustand.html#stufe-6)) |
| Vier Typen | Sorte der Träger und Dotierung der Oberfläche (Stufe [7](vier-typen-von-mosfets.html#stufe-7)) |
| Inverter | Transistor und Widerstand als Spannungsteiler (Stufe [8](erganzung-grundschaltungen.html#stufe-8)) |
