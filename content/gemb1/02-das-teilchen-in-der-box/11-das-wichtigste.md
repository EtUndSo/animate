---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Das Teilchen in der Box
order: 4121100
summary: Warum ein eingesperrtes Elektron nur bestimmte Energien hat
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Gitter:** $-t_0(\psi_{\ell+1}-2\psi_\ell+\psi_{\ell-1})+V_\ell\psi_\ell=E\psi_\ell$, $t_0=\hbar^2/(2ma^2)$, als Matrix eine Eigenwertaufgabe.

</li>

<li>

⁠**Kosinus-Band:** $E(k)=2t_0(1-\cos(ka))+V_0$ für $|k|\le\pi/a$, $v(k)=(2t_0a/\hbar)\sin(ka)$, für kleine $k$ die Parabel. Masse aus der Krümmung: $m^*=(\hbar^{-2}\,\partial^2E/\partial k^2)^{-1}$.

</li>

<li>

⁠**Box in 1D:** $k_n=n\pi/L$, $\psi_n=\mathrm{j}\sqrt{2/L}\,\sin(n\pi x/L)$, $E_n=\hbar^2\pi^2n^2/(2mL^2)=h^2n^2/(8mL^2)$, $n\ge1$. Also $E\propto n^2$, $E\propto1/L^2$, $E\propto1/m$, $n-1$ Knoten, $E_1>0$.

</li>

<li>

⁠**Box in 2D und 3D:** $\psi$ ist das Produkt, $E$ die Summe der Richtungen, je Richtung eine Quantenzahl und eine Masse.

</li>

<li>

⁠**Entartung:** Symmetrie macht verschiedene Zustände energiegleich (Quadrat $g=1,2$; Würfel $g=1,3,6$), dazu kommt Zufall. Ungleiche Kanten oder Massen spalten auf.

</li>

<li>

⁠**Ergänzung:** Film, Draht, Punkt: 1, 2, 3 eingesperrte Richtungen. $D(E)=(2/L^d)\,\mathrm{d} Z/\mathrm{d} E\propto E^{-1/2},E^0,E^{1/2}$ für $d=1,2,3$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eingesperrt sind nur stehende Wellen möglich, die an den Wänden null sind. Die Box wählt deshalb aus $E(k)$ die Punkte $k_n=n\pi/L$ aus, und die Energie wird diskret.

</li>

<li>

Je enger die Box und je leichter das Teilchen, desto größer sind die Energien und ihre Abstände: $E_n\propto n^2/(mL^2)$, und selbst der tiefste Zustand hat $E_1>0$.

</li>

<li>

In mehreren Richtungen addieren sich die Energien, und Symmetrie lässt verschiedene Zustände dieselbe Energie haben.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Krümmung kostet Energie. Fast alles in diesem Kapitel folgt aus der Frage, wie stark eine Welle unter den gegebenen Bedingungen gekrümmt sein muss.

| Ergebnis | Woher es kommt |
|---|---|
| Hüpfparameter $t_0\propto1/(ma^2)$ | Krümmung, gemessen zwischen Nachbarpunkten (Stufe [1](die-schrodinger-gleichung-auf-einem-gitter.html#stufe-1)) |
| Band mit Obergrenze $4t_0$ | Stärkste Krümmung: Vorzeichenwechsel von Punkt zu Punkt (Stufe [2](das-kosinus-band.html#stufe-2)) |
| Masse $m^*$ | Krümmung der Kurve $E(k)$ (Stufe [2](das-kosinus-band.html#stufe-2)) |
| Nullpunktsenergie $E_1>0$ | Null an beiden Wänden erzwingt Krümmung (Stufe [3](das-elektron-zwischen-zwei-wanden.html#stufe-3)) |
| $E_n\propto n^2/L^2$ | $n$ Halbwellen auf $L$: Die Krümmung wächst wie $(n/L)^2$ (Stufe [3](das-elektron-zwischen-zwei-wanden.html#stufe-3)) |
| $E$ als Summe der Richtungen | Die Krümmungen in $x$, $y$, $z$ addieren sich (Stufe [4](die-box-in-der-ebene.html#stufe-4) und [6](die-box-im-raum.html#stufe-6)) |
| Entartung | Vertauschte Achsen ergeben dieselbe Gesamtkrümmung (Stufe [5](gleiche-energie-verschiedene-zustande.html#stufe-5)) |
| $D(E)$ | Zahl der Wellen mit gegebener Gesamtkrümmung (Stufe [8](erganzung-zustandsdichten-in-potentialkasten.html#stufe-8)) |
