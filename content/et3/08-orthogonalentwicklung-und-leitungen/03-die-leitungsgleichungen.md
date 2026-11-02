---
title: Stufe 2: Die Leitungsgleichungen
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Orthogonalentwicklung und Leitungen
order: 3280300
summary: Bisher waren Leitungen ideale Verbindungen.
tags: Leitungsbelägen
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Bisher waren Leitungen ideale Verbindungen. Ist eine Leitung lang gegenüber der Wellenlänge, braucht ein Signal merklich Zeit, um sie zu durchlaufen. Diese Stufe stellt die Gleichungen auf, die das beschreiben.
:::

**Die Idee.** Man zerlegt die Leitung in kurze Stücke der Länge $\mathrm{d} s$. Jedes Stück hat einen Längswiderstand und eine Längsinduktivität (die Hin- und Rückleiter), dazu eine Querkapazität und einen Querleitwert (zwischen den Leitern). Bei einer gleichförmigen Leitung sind diese Größen proportional zur Länge: $R'\mathrm{d} s$, $L'\mathrm{d} s$, $C'\mathrm{d} s$, $G'\mathrm{d} s$ mit den __Leitungsbelägen__ $R'$, $L'$, $C'$, $G'$ (Werte je Meter, Abb. [1](#abb-1)).

:::abbildung et3/k8element 1
Ersatzschaltbild eines kurzen Leitungsstücks der Länge $\mathrm{d} s$ mit den Leitungsbelägen $R'$, $L'$, $G'$, $C'$.
:::

:::satz Satz 2.1 (Leitungsgleichungen)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung Leitungsgleichungen
Maschenregel über das Stück: $u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$, also $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$. Knotenregel: Vom Strom $i$ fließt ein Teil durch $G'\mathrm{d} s$ und $C'\mathrm{d} s$ ab, $i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$. Durch $\mathrm{d} s$ teilen. (In der Knotenregel steht strenggenommen die Spannung am Ende des Stücks, der Unterschied ist von zweiter Ordnung in $\mathrm{d} s$.)
:::

⁠**So liest man das:** Die Spannung fällt entlang der Leitung, weil Strom durch die Längselemente fließt. Der Strom nimmt ab, weil er über die Querelemente zwischen den Leitern abfließt. Die beiden Gleichungen koppeln $u$ und $i$ in Ort und Zeit.
