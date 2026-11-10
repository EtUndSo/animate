---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung
knoten: Kapitel 11: Eigenhalbleiter und Dotierung
order: 4211100
summary: Wie viele Ladungsträger ein Halbleiter hat und wie man ihre Zahl festlegt
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Eigenhalbleiter:** $n=p=n_\mathrm i=\sqrt{N_\mathrm CN_\mathrm V}\,\mathrm{e}^{-E_\mathrm g/(2k_\mathrm BT)}$, $E_\mathrm{Fi}=E_\mathrm V+\frac12E_\mathrm g+\frac34k_\mathrm BT\ln(m_\mathrm V^*/m_\mathrm C^*)$.

</li>

<li>

⁠**Dotierung:** $E_\mathrm D$ knapp unter $E_\mathrm C$, $E_\mathrm A$ knapp über $E_\mathrm V$, $\Delta E\approx13{,}6\,\mathrm{eV}\,(m^*/m_0)/\varepsilon_\mathrm r^2$.

</li>

<li>

⁠**Besetzung:** $N_\mathrm D^+=N_\mathrm D/(1+2\mathrm{e}^{(E_\mathrm F-E_\mathrm D)/(k_\mathrm BT)})$, $N_\mathrm A^-=N_\mathrm A/(1+g_\mathrm A\mathrm{e}^{(E_\mathrm A-E_\mathrm F)/(k_\mathrm BT)})$, in Si $g_\mathrm A=4$.

</li>

<li>

⁠**Neutralität:** $p+N_\mathrm D^+-n-N_\mathrm A^-=0$ legt $E_\mathrm F$ fest, $n\,p=n_\mathrm i^2$ bleibt gültig.

</li>

<li>

⁠**Ionisiert:** $n=\frac12N_\mathrm D+\sqrt{\frac14N_\mathrm D^2+n_\mathrm i^2}$, $E_\mathrm F=E_\mathrm{Fi}+k_\mathrm BT\operatorname{arcsinh}(N_\mathrm D/(2n_\mathrm i))$. Erschöpfung: $n=N_\mathrm D$, $E_\mathrm F=E_\mathrm C-k_\mathrm BT\ln(N_\mathrm C/N_\mathrm D)$.

</li>

<li>

⁠**Reserve:** $n=\sqrt{N_\mathrm DN_\mathrm C/2}\;\mathrm{e}^{-\Delta E_\mathrm D/(2k_\mathrm BT)}$, $E_\mathrm F=E_\mathrm C-\frac12\Delta E_\mathrm D+\frac12k_\mathrm BT\ln(N_\mathrm D/(2N_\mathrm C))$. p-Typ: $p=\sqrt{N_\mathrm AN_\mathrm V/g_\mathrm A}\;\mathrm{e}^{-\Delta E_\mathrm A/(2k_\mathrm BT)}$.

</li>

<li>

⁠**Hohe Dichte:** Ab rund $10^{19}\,\mathrm{cm^{-3}}$ Störstellenband, $E_\mathrm g^\mathrm{eff}<E_\mathrm g$, Entartung.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Im reinen Kristall entstehen Elektronen und Löcher nur paarweise, deshalb liegt $E_\mathrm F$ nahe der Bandmitte, und $n_\mathrm i$ wächst mit $\mathrm{e}^{-E_\mathrm g/(2k_\mathrm BT)}$ steil mit der Temperatur.

</li>

<li>

Fremdatome binden ihr überzähliges Elektron oder Loch nur mit rund $k_\mathrm BT$, weil effektive Masse und Abschirmung das Wasserstoffatom um einen Faktor von mehreren Hundert schwächen, und legen so Art und Zahl der Träger fest.

</li>

<li>

Die Neutralität bestimmt dann $E_\mathrm F$ und ergibt drei Bereiche: Bei tiefen Temperaturen frieren die Elektronen auf den Donatoren aus, dazwischen ist $n=N_\mathrm D$ konstant, und bei hohen Temperaturen überholt die Eigenleitung die Dotierung.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** $E_\mathrm F$ stellt sich so ein, dass die Ladung aufgeht. Alles Weitere ist die Frage, welche Quelle die Elektronen liefert und was sie kostet.

| Ergebnis | Woher es kommt |
|---|---|
| $E_\mathrm{Fi}$ nahe der Bandmitte | Elektronen und Löcher entstehen paarweise (Stufe [2](der-reine-kristall.html#stufe-2)) |
| Halbe Energie in den Exponenten | Zwei Teilchen teilen sich die Energie (Stufe [2](der-reine-kristall.html#stufe-2) und [7](tiefe-temperaturen-und-die-lage-von.html#stufe-7)) |
| Wenige Fremdatome genügen | Das Elektron kostet nur $\Delta E_\mathrm D$ statt $E_\mathrm g/2$ (Stufe [3](fremdatome-im-gitter.html#stufe-3)) |
| $\Delta E$ von nur rund 45 meV | Masse $m^*$ und Abschirmung $\varepsilon_\mathrm r$ im Wasserstoffmodell (Stufe [4](warum-die-bindung-so-schwach-ist.html#stufe-4)) |
| Plateau, darüber Eigenleitung | Donatoren sind leer, Paare erst heiß stark genug (Stufe [6](hohe-und-mittlere-temperaturen.html#stufe-6)) |
| Ausfrieren bei tiefen $T$ | Die Wärme reicht nicht mehr für $\Delta E_\mathrm D$ (Stufe [7](tiefe-temperaturen-und-die-lage-von.html#stufe-7)) |
| Störstellenband und Entartung | Überlappende Bahnen koppeln wie Atome im Kristall (Stufe [8](hohe-dotierstoffdichten.html#stufe-8)) |
