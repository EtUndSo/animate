---
title: Stufe 2: Die Leitungsgleichungen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Orthogonalentwicklung und Leitungen
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Kapitel 8: Orthogonalentwicklung und Leitungen
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

::::formelsammlung
**Leitungsbeläge**

$$R'\mathrm{d} s,\qquad L'\mathrm{d} s,\qquad C'\mathrm{d} s,\qquad G'\mathrm{d} s$$

Längswiderstand, Längsinduktivität, Querkapazität und Querleitwert eines kurzen Stücks der Länge $\mathrm{d} s$ einer gleichförmigen Leitung; die Leitungsbeläge $R'$, $L'$, $C'$, $G'$ sind die Werte je Meter.

**Leitungsgleichungen**

$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u$$

Für eine gleichförmige Leitung, aus Maschen- und Knotenregel an einem Stück der Länge $\mathrm{d} s$. Die Spannung fällt, weil Strom durch die Längselemente fließt; der Strom nimmt ab, weil er über die Querelemente abfließt.
::::

::::lernkarten
:::karte zusammenhang Leitung als ideale Verbindung
Wann darf man eine Leitung nicht mehr als ideale Verbindung behandeln, und warum?
---
Wenn sie gegenüber der Wellenlänge nicht mehr kurz ist. Dann braucht ein Signal merklich Zeit, um sie zu durchlaufen; Spannung und Strom hängen auch vom Ort ab.
--- falsch
Wenn ihr Widerstand größer ist als der Lastwiderstand. Dann fällt der größte Teil der Spannung auf der Leitung selbst ab, und am Ende kommt fast nichts mehr an.
--- falsch
Wenn sie aus mehr als zwei Leitern besteht. Dann beeinflussen sich die Leiter gegenseitig, und man muss jeden einzelnen Leiter als eigene Quelle behandeln.
--- falsch
Wenn die Frequenz unter einer Grenzfrequenz liegt. Dann wirken die Kapazitäten zwischen den Leitern als Kurzschluss, und das Signal wird vollständig abgeleitet.
:::
:::karte begriff Leitungsbeläge
Was versteht man unter den Leitungsbelägen $R'$, $L'$, $C'$, $G'$, mit denen man eine gleichförmige Leitung beschreibt?
---
Widerstand, Induktivität, Kapazität und Leitwert der Leitung je Meter Länge. Ein kurzes Stück der Länge $\mathrm{d} s$ hat dann $R'\mathrm{d} s$, $L'\mathrm{d} s$, $C'\mathrm{d} s$ und $G'\mathrm{d} s$.
--- falsch
Widerstand, Induktivität, Kapazität und Leitwert der ganzen Leitung von Anfang bis Ende. Jedes kurze Stück hat dieselben Werte, weil die Leitung gleichförmig ist.
--- falsch
Die Bauteile, die man am Anfang und am Ende einer Leitung anschließt, um sie anzupassen. Sie werden je nach Länge der Leitung passend ausgewählt.
--- falsch
Widerstand, Induktivität, Kapazität und Leitwert je Sekunde Laufzeit. Sie geben an, wie stark ein Signal in jeder Sekunde auf der Leitung verändert wird.
:::
:::karte zusammenhang Längs- und Querelemente
Welche Elemente liegen im Ersatzschaltbild eines kurzen Leitungsstücks in Längsrichtung und welche quer zwischen den Leitern, und warum?
---
Längs liegen $R'\mathrm{d} s$ und $L'\mathrm{d} s$, weil der Strom durch Hin- und Rückleiter fließt. Quer liegen $C'\mathrm{d} s$ und $G'\mathrm{d} s$, weil sie Kapazität und Leitwert zwischen den beiden Leitern beschreiben.
--- falsch
Längs liegen $R'\mathrm{d} s$ und $C'\mathrm{d} s$, weil beide den Stromfluss entlang des Leiters behindern. Quer liegen $L'\mathrm{d} s$ und $G'\mathrm{d} s$, weil sie das Magnetfeld zwischen den Leitern beschreiben.
--- falsch
Längs liegen alle vier Elemente hintereinander, weil der Strom jedes Element des Leitungsstücks nacheinander durchfließen muss, bevor er das Ende des Stücks erreicht.
--- falsch
Längs liegen $G'\mathrm{d} s$ und $C'\mathrm{d} s$, weil sie zum Leiter selbst gehören. Quer liegen $R'\mathrm{d} s$ und $L'\mathrm{d} s$, weil sie die Verluste zwischen Hin- und Rückleiter beschreiben.
:::
:::karte formel Leitungsgleichungen
Wie lauten die Leitungsgleichungen, die Spannung $u(s,t)$ und Strom $i(s,t)$ auf einer gleichförmigen Leitung verknüpfen?
---
$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i$ und $\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u$. Sie gelten für beliebige Zeitverläufe und koppeln $u$ und $i$ in Ort und Zeit.
--- falsch
$\frac{\partial u}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)i$ und $\frac{\partial i}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)u$. Sie gelten für beliebige Zeitverläufe und koppeln $u$ und $i$ in Ort und Zeit.
--- falsch
$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i$ und $\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u$. Sie gelten nur für sinusförmige Signale, nicht für beliebige Zeitverläufe.
--- falsch
$\frac{\partial u}{\partial t}=-\Bigl(R'+L'\frac{\partial}{\partial s}\Bigr)i$ und $\frac{\partial i}{\partial t}=-\Bigl(G'+C'\frac{\partial}{\partial s}\Bigr)u$. Sie gelten für beliebige Zeitverläufe und koppeln $u$ und $i$ in Ort und Zeit.
:::
:::karte herleitung Leitungsgleichungen aus Maschen- und Knotenregel
Wie gewinnt man aus dem Ersatzschaltbild eines Leitungsstücks der Länge $\mathrm{d} s$ die beiden Leitungsgleichungen?
---
Die Maschenregel über das Stück liefert $u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$, weil die Spannung am Anfang gleich den Spannungen an den Längselementen plus der Spannung am Ende ist.
---
Daraus wird $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$, weil $u$ auf beiden Seiten steht und sich weghebt.
---
Die Knotenregel liefert $i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$, weil vom Strom $i$ ein Teil durch $G'\mathrm{d} s$ und $C'\mathrm{d} s$ zwischen den Leitern abfließt.
---
Man teilt beide Gleichungen durch $\mathrm{d} s$ und erhält die Leitungsgleichungen, weil $\mathrm{d} s$ in jedem Glied als Faktor steht. Dass in der Knotenregel strenggenommen die Spannung am Ende des Stücks steht, ändert nur Glieder zweiter Ordnung in $\mathrm{d} s$.
:::
:::karte zusammenhang Spannung fällt, Strom nimmt ab
Warum fällt die Spannung entlang einer Leitung, und warum nimmt der Strom entlang der Leitung ab?
---
Die Spannung fällt, weil Strom durch die Längselemente $R'$ und $L'$ fließt. Der Strom nimmt ab, weil ein Teil über die Querelemente $G'$ und $C'$ zwischen den Leitern abfließt.
--- falsch
Die Spannung fällt, weil ein Teil über die Querelemente $G'$ und $C'$ abfließt. Der Strom nimmt ab, weil er in den Längselementen $R'$ und $L'$ abgebremst und verbraucht wird.
--- falsch
Die Spannung fällt, weil sich die Leitung wie ein Kondensator auflädt. Der Strom nimmt ab, weil die Ladung am Ende der Leitung nicht weiterfließen kann und sich staut.
--- falsch
Beides liegt allein am Widerstandsbelag $R'$: Er setzt Leistung in Wärme um, sodass Spannung und Strom zum Ende hin im gleichen Verhältnis kleiner werden.
:::
::::
