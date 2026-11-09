---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4261100
summary: Was einen gebauten Kondensator vom idealen unterscheidet und wie die Kapazität es verrät
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Flachband:** $V_\mathrm{FB}=\Delta\Phi/e-Q'_\mathrm{IS}/C'_\mathrm{IS}-Q'_\mathrm{SS}/C'_\mathrm{IS}$ mit $\Delta\Phi=\Phi_\mathrm M-\Phi_\mathrm{SC}$.

</li>

<li>

⁠**Bilanz:** $V_\mathrm G=V_\mathrm{FB}+\varphi_\mathrm s-Q'_\mathrm{SC}/C'_\mathrm{IS}=\Delta\Phi/e+\varphi_\mathrm s+V_\mathrm{IS}$.

</li>

<li>

⁠**Schwelle:** $V_\mathrm{th}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}+\gamma\sqrt{\varphi_\mathrm{s,SI}}$, Verarmung: $V_\mathrm G=V_\mathrm{FB}+\varphi_\mathrm s+\gamma\sqrt{\varphi_\mathrm s}$.

</li>

<li>

⁠**Interfacezustände:** $C'_\mathrm{it}\approx e^2D_\mathrm{it}$, parallel zu $C'_\mathrm{depl}$ und $C'_\mathrm{inv/acc}$, $\mathrm{d}\varphi_\mathrm s/\mathrm{d} V_\mathrm G=C'_\mathrm{IS}/(C'_\mathrm{IS}+C'_\mathrm{SC}+C'_\mathrm{it})$.

</li>

<li>

⁠**Frequenz:** $C'_\mathrm{hf}=C'_\mathrm{IS}C'_\mathrm{depl}/(C'_\mathrm{IS}+C'_\mathrm{depl})$ mit Plateau bei $L_\mathrm{depl,max}$, $C'_\mathrm{nf}$ steigt in Inversion auf $C'_\mathrm{IS}$.

</li>

<li>

⁠**Tiefenverarmung:** Bei schneller Gleichspannung gilt die Verarmungsformel über $\varphi_\mathrm{s,SI}$ hinaus.

</li>

<li>

⁠**Auswertung:** $L_\mathrm{depl,max}=\varepsilon(1/C'_\mathrm{min}-1/C'_\mathrm{IS})$, $C'_\mathrm{it}=(1/C'_\mathrm{nf}-1/C'_\mathrm{IS})^{-1}-(1/C'_\mathrm{hf}-1/C'_\mathrm{IS})^{-1}$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Austrittsarbeitsdifferenz und feste Ladungen fassen sich zur Flachbandspannung zusammen, und alle Kurven des idealen Kondensators verschieben sich um genau diesen Wert.

</li>

<li>

Interfacezustände ändern ihre Ladung mit der Bandverbiegung, deshalb dehnen sie die Kurven und liegen als Kapazität parallel zum Halbleiter.

</li>

<li>

Die gemessene Kapazität hängt davon ab, welche Ladung dem Signal folgen kann, und genau das macht aus einer Kurve ein Messgerät für Dicke, Dotierung, Ladungen und Zustandsdichte.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Die Spannung am Gate ist eine Ladungsbilanz. Was fest sitzt, verschiebt die Kurve, was sich mit $\varphi_\mathrm s$ ändert, dehnt sie, und was zu langsam ist, fehlt in der Messung.

| Ergebnis | Woher es kommt |
|---|---|
| Bänder ohne Spannung verbogen | $E_\mathrm F$ gleicht sich an, die Ladung fließt durch den Draht (Stufe [1](verschiedene-austrittsarbeiten.html#stufe-1)) |
| $-Q'/C'_\mathrm{IS}$ in $V_\mathrm{FB}$ | Bei Flachband trägt das Gate die ganze Gegenladung (Stufe [2](feste-ladungen-im-isolator.html#stufe-2)) |
| Kurven um $V_\mathrm{FB}$ verschoben | Feste Ladung ändert sich mit $V_\mathrm G$ nicht (Stufe [3](die-reale-bilanz-und-die-verschobene-schwelle.html#stufe-3)) |
| Gedehnte Kurven, $C'_\mathrm{it}=e^2D_\mathrm{it}$ | Zustände wandern mit den Bändern durch $E_\mathrm F$ (Stufe [4](interfacezustande.html#stufe-4)) |
| Plateau bei hoher Frequenz | Die Wechselladung sitzt am Zonenrand (Stufe [5](kennlinien-bei-niedriger-und-hoher-frequenz.html#stufe-5)) |
| Kapazität unter dem Plateau | Elektronen fehlen, die Zone wächst weiter (Stufe [6](tiefenverarmung.html#stufe-6)) |
| Auswertung Schritt für Schritt | Jeder Kurvenabschnitt hängt an einer Größe (Stufe [7](messen-und-auswerten.html#stufe-7)) |
| Bildsensor | Tiefenverarmung hält den Topf leer für Lichtladung (Stufe [8](erganzung-charge-coupled-devices.html#stufe-8)) |
