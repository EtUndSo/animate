---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4131000
summary: Was eine Elektronenwelle an einer endlich hohen Wand tut
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

Stückweise konstantes Potential: in jedem Gebiet $k=\sqrt{2m(E-V)}/\hbar$. Für Elektronen $2m_0/\hbar^2=26{,}25/(\mathrm{eV\,nm^2})$.

</li>

<li>

An jeder endlichen Kante sind $\psi$ und $\mathrm{d}\psi/\mathrm{d} x$ stetig.

</li>

<li>

Potentialstufe, $E>V_0$: $R=\bigl(\frac{k_\mathrm I-k_\mathrm{II}}{k_\mathrm I+k_\mathrm{II}}\bigr)^2$, $T=\frac{4k_\mathrm Ik_\mathrm{II}}{(k_\mathrm I+k_\mathrm{II})^2}$, $R+T=1$. Der Teilchenstrom $\mathcal J_\mathrm e=|\psi|^2v$ zählt, nicht die Dichte.

</li>

<li>

Potentialstufe, $E<V_0$: $k_\mathrm{II}=\mathrm{j}\kappa$, $\psi\propto\mathrm{e}^{-x/\delta}$, $\delta=1/\kappa=\sqrt{\hbar^2/(2m(V_0-E))}$, $R=1$, $T=0$.

</li>

<li>

Barriere, $E<V_0$: $T=\bigl[1+\frac{\sinh^2(\kappa L)}{4(E/V_0)(1-E/V_0)}\bigr]^{-1}$. Für $\kappa L\gg1$: $T\approx16\frac E{V_0}(1-\frac E{V_0})\mathrm{e}^{-2\kappa L}$.

</li>

<li>

Barriere, $E>V_0$: $\sinh$ wird $\sin$ mit $k_\mathrm{II}$, $T=1$ bei $k_\mathrm{II}L=n\pi$.

</li>

<li>

Box mit endlichen Wänden: Energien tiefer als bei unendlich hohen Wänden, Eindringen wächst mit $E_n$, endlich viele gebundene Zustände.

</li>

<li>

Die scharfe Kante gilt nur, wenn ihr Anstieg nicht viel breiter ist als die Wellenlänge.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

An einer Kante muss die Welle in Wert und Steigung glatt bleiben. Deshalb läuft für $E>V_0$ immer ein Teil zurück, und für $E<V_0$ endet die Welle nicht, sondern klingt mit der Eindringtiefe $\delta$ ab.

</li>

<li>

Ist die Wand dünn, liegt am anderen Ende noch Amplitude an, und dort beginnt eine laufende Welle derselben Energie. Der Anteil, der durchkommt, fällt mit $\mathrm{e}^{-2\kappa L}$.

</li>

<li>

In einer Box mit endlichen Wänden ragen die Wellen in die Wände. Die Energien sinken, und hohe Niveaus sind am wenigsten gefangen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** In jedem Gebiet legt $E-V$ die Form der Welle fest: Schwingung für $E>V$, Exponentialfunktion für $E<V$. An den Kanten müssen diese Stücke glatt ineinander übergehen. Alles Übrige folgt daraus.

| Ergebnis | Woher es kommt |
|---|---|
| Reflexion für $E>V_0$ | Eine Welle allein passt nicht zugleich in Wert und Steigung (Stufe [2](reflexion-trotz-genugender-energie.html#stufe-2)) |
| $T\to0$ für $E\to V_0$ | $k_\mathrm{II}\to0$: Rechts bleibt keine passende Steigung (Stufe [2](reflexion-trotz-genugender-energie.html#stufe-2)) |
| Evaneszente Welle | $E<V$ macht $k$ imaginär, und ein Ende an der Kante ist verboten (Stufe [3](die-welle-dringt-in-die-wand-ein.html#stufe-3)) |
| $R=1$ für $E<V_0$ | Die abklingende Funktion trägt keinen Teilchenstrom (Stufe [3](die-welle-dringt-in-die-wand-ein.html#stufe-3)) |
| Tunneleffekt | Am Barrierenende ist $\psi\ne0$, dort startet eine laufende Welle (Stufe [4](tunneln-durch-eine-dunne-wand.html#stufe-4)) |
| $T\propto\mathrm{e}^{-2\kappa L}$ | Die Amplitude fällt um $\mathrm{e}^{-\kappa L}$, $T$ zählt das Quadrat (Stufe [5](die-dicke-barriere.html#stufe-5)) |
| $T=1$ über der Barriere | Die Reflexionen beider Kanten löschen sich aus (Stufe [5](die-dicke-barriere.html#stufe-5)) |
| Tiefere Energien in der Box | Die Welle ragt in die Wände und wird länger (Stufe [6](die-box-mit-endlich-hohen-wanden.html#stufe-6)) |
| Keine Reflexion beim Ball | Der Anstieg ist viel breiter als die Wellenlänge (Stufe [7](erganzung-scharfe-stufen-und-nachweise.html#stufe-7)) |
