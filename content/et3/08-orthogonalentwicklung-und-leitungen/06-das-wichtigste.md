---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Orthogonalentwicklung und Leitungen
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Kapitel 8: Orthogonalentwicklung und Leitungen
order: 3280600
summary: Zwei Zusatzthemen: Signale als Vektoren, Wellen auf elektrischen Leitungen
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Bei orthonormalen Basisfunktionen ist der beste Koeffizient einer Funktion ihre Korrelation mit der Basisfunktion, und die Energie ist die Summe der Koeffizientenquadrate.

</li>

<li>

Auf einer Leitung ist jede Spannung eine Überlagerung einer hinlaufenden und einer rücklaufenden Welle. Die Leitung ist durch die Ausbreitungskonstante $\gamma$ und den Wellenwiderstand $Z$ beschrieben.

</li>

<li>

Wird die Leitung mit ihrem Wellenwiderstand abgeschlossen, verschwindet die rücklaufende Welle. Bei einer verlustlosen Leitung laufen alle Frequenzen gleich schnell, Signale kommen unverzerrt an.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Orthonormal: $\int s_is_j\mathrm{d} t=\delta_{ij}$; beste Koeffizienten $b_i=\int fs_i\mathrm{d} t$; $E_r=E_f-\sum b_i^2$; vollständig: $E_f=\sum b_i^2$.

</li>

<li>

Leitungsgleichungen: $\partial_su=-(R'+L'\partial_t)i$, $\partial_si=-(G'+C'\partial_t)u$.

</li>

<li>

Zeiger (mit $\omega=2\pi f$): $\underline U=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$; $\gamma=\sqrt{(R'+\mathrm{j}\omega L')(G'+\mathrm{j}\omega C')}=\alpha+\mathrm{j}\beta$; $Z=\sqrt{\frac{R'+\mathrm{j}\omega L'}{G'+\mathrm{j}\omega C'}}$.

</li>

<li>

Abschluss mit $Z$: keine Reflexion; $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$.

</li>

<li>

Verlustlos: $Z=\sqrt{L'/C'}$, $v=1/\sqrt{L'C'}$, $u=u_\mathrm{hin}(s-vt)+u_\mathrm{rück}(s+vt)$.

</li>

</ul>
:::
