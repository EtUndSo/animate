---
title: Stufe 1: Wie Ladung die Bänder verbiegt
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Der p-n-Übergang
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang
knoten: Kapitel 14: Der p-n-Übergang
order: 4240300
summary: Bisher waren die Bänder meist waagerecht, weil der Halbleiter überall gleich war.
tags: Raumladung, Bandverlauf
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bisher waren die Bänder meist waagerecht, weil der Halbleiter überall gleich war. An Grenzflächen sammelt sich Ladung. Diese Stufe zeigt, wie man im Bänderdiagramm aus einer Ladungsverteilung Feld und Potential abliest.
:::

**Die Idee.** Im homogenen Stück heben sich die Ladungen der Ionen und der beweglichen Träger an jedem Ort auf. Äußere Kräfte oder ein anders dotiertes Nachbargebiet stören diesen Ausgleich: Es entsteht ein örtlicher Überschuss oder Mangel an Trägern, also __Raumladung__, Ladung je Volumen, die nicht ausgeglichen ist. Nach der Poisson-Gleichung aus [Kapitel 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html) ist sie die Quelle eines Feldes. Das Feld gehört zu einem Potential, und das Potential verschiebt die Energie eines Elektrons um $-e\varphi$. Das trifft jeden Zustand am selben Ort gleich: Leitungsband, Valenzband, Donator- und Akzeptorniveau rücken gemeinsam. Die Bandlücke bleibt, die Bänder verbiegen sich.

:::satz Satz 1.1 (Poisson-Gleichung und Bandverbiegung)
<span class="anker" id="satz-1-1"></span>

Hängt alles nur von $x$ ab, gilt mit der Raumladungsdichte $\rho$ für Feld $\mathcal E$ und Potential $\varphi$

<span class="anker" id="gl-1-1"></span>
$$\rho(x)=e\bigl[p(x)+N_\mathrm D^+(x)-n(x)-N_\mathrm A^-(x)\bigr], \tag{1.1}$$

<span class="anker" id="gl-1-2"></span>
$$\frac{\mathrm{d}\mathcal E}{\mathrm{d} x}=\frac{\rho}{\varepsilon_0\varepsilon_\mathrm r},\qquad\mathcal E=-\frac{\mathrm{d}\varphi}{\mathrm{d} x},\qquad\text{also}\quad\frac{\mathrm{d}^2\varphi}{\mathrm{d} x^2}=-\frac{\rho(x)}{\varepsilon_0\varepsilon_\mathrm r}. \tag{1.2}$$

Jedes Niveau $i=\mathrm C,\mathrm V,\mathrm D,\mathrm A$ folgt dem Potential:

<span class="anker" id="gl-1-3"></span>
$$E_i(x)=E_{i,\mathrm{Bulk}}-e\,\varphi(x). \tag{1.3}$$

Für den __Bandverlauf__ $\Phi(x)=-e\varphi(x)+\text{const}$, die Verschiebung der Bänder als Energie, lautet die Poisson-Gleichung

<span class="anker" id="gl-1-4"></span>
$$\frac{\mathrm{d}\Phi}{\mathrm{d} x}=e\,\mathcal E,\qquad\frac{\mathrm{d}^2\Phi}{\mathrm{d} x^2}=\frac{e\,\rho(x)}{\varepsilon_0\varepsilon_\mathrm r}. \tag{1.4}$$
:::

⁠**So liest man das:** $\rho$ in C/m$^3$ ist die Raumladungsdichte aus [Kapitel 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html), $N_\mathrm D^+$ und $N_\mathrm A^-$ sind die Dichten der ionisierten Fremdatome. Fehlen bei $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ alle Elektronen, ist $\rho=eN_\mathrm D=1602\,\mathrm{C/m^3}$. $E_{i,\mathrm{Bulk}}$ ist die Lage im ungestörten Inneren (englisch bulk). $\varphi$ steht in V, $\Phi$ in eV, $\mathcal E$ in V/m. **Kurz gesagt:** Die Neigung der Bänder ist $e$ mal Feld, ihre Krümmung ist $e/\varepsilon$ mal Raumladung. **Gültigkeit:** Das Potential ändert sich über eine Gitterkonstante nur wenig, bei 3 MV/m um 1,6 mV je 0,54 nm. Deshalb gilt an jedem Ort die Bandstruktur aus [Kapitel 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html), nur verschoben.

:::herleitung Vom Potential zum Bandverlauf
[(1.2)](#gl-1-2) ist die eindimensionale Form der Poisson-Gleichung aus [Kapitel 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html). Ein Elektron hat im Potential $\varphi$ die zusätzliche Energie $-e\varphi$ ([Kapitel 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html)), das ergibt [(1.3)](#gl-1-3). Mit $-e$ multipliziert wird aus [(1.2)](#gl-1-2) die Gleichung [(1.4)](#gl-1-4).
:::

**Ladung je Fläche.** Trägt eine Kondensatorplatte aus Halbleiter die Ladung $Q=C\,U$ auf der Fläche $A$, sitzt diese Ladung nicht auf der Oberfläche, sondern in einer Schicht darunter. Die Flächenladung ist die Summe über die Tiefe:

<span class="anker" id="gl-1-5"></span>
$$Q'=\frac{Q}{A}=\int_0^\infty\rho(x)\,\mathrm{d} x. \tag{1.5}$$

::::beispiel
In Abb. [1](#abb-1) fehlen die Elektronen in einer Schicht von $d=200$ nm Dicke, dort stehen nur Donatoren mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$. Die Gegenladung $-Q'$ sitzt dünn auf der Oberfläche bei $x=0$, rechts der Schicht ist alles neutral. Aus [(1.5)](#gl-1-5) folgt $Q'=eN_\mathrm Dd=3{,}2\cdot10^{-4}\,\mathrm{C/m^2}$, das sind $2\cdot10^{11}$ Ladungen je cm$^2$. Das Feld fällt nach [(1.2)](#gl-1-2) linear von $Q'/\varepsilon=3{,}09$ MV/m auf null. Die Bandkante steigt als Parabel um $eQ'd/(2\varepsilon)=0{,}309$ eV, das sind $12\,k_\mathrm BT$. Wenige hundert Nanometer Raumladung verbiegen die Bänder also um einen großen Teil der Bandlücke.
::::

⁠**Grenzfälle:** Ist $\rho=0$, sind die Bänder gerade: mit Feld schräg wie in [Kapitel 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html), ohne Feld waagerecht.

:::abbildung gemb1/k14baender 1
Vorgegebene Ladung und ihre Folgen. Oben: positive Schicht der Dicke 200 nm, $\rho=1{,}6\cdot10^{3}\,\mathrm{C/m^3}$, dazu die Gegenladung $-Q'$ auf der Oberfläche. Mitte: Das Feld steigt linear bis null. Unten: Die Bandkanten folgen als Parabel, beide um dieselben 0,31 eV. Wo $\rho=0$ und $\mathcal E=0$ ist, sind sie waagerecht.
:::

:::frage Warum steigt ein Loch im Bänderdiagramm nach oben?
Die Achse zeigt die Energie eines Elektrons. Das Feld in Abb. [1](#abb-1) zeigt nach links. Es schiebt das Elektron nach rechts, bergab, und das positive Loch nach links, im Bild bergauf. Ein Loch verliert Energie, wenn es nach oben steigt, denn dabei sinkt ein Elektron von oben auf seinen Platz.
:::

:::aufgabe Aufgabe 1 ★ Eine Schicht und eine Parabel
<span class="anker" id="aufg-1"></span>

In Silizium ist eine Schicht von $d=150$ nm von Elektronen entleert, die Donatoren haben $N_\mathrm D=3\cdot10^{16}\,\mathrm{cm^{-3}}$. Die Gegenladung sitzt dünn bei $x=0$, rechts von $x=d$ ist alles feldfrei.

<ol class="al">

<li>

Berechne $Q'$, das Feld bei $x=0$ und die Bandverbiegung in eV und in $k_\mathrm BT$.

</li>

<li>

Um welchen Faktor wächst die Bandverbiegung, wenn $d$ sich verdoppelt? Was fällt im Vergleich mit $E_\mathrm g$ auf?

</li>

<li>

Eine Bandkante verläuft als $E_\mathrm C(x)=E_0+a\,x^2$ mit $a=2\,\mathrm{eV/\mu\text{}m^2}$. Welches Vorzeichen und welche Größe hat $\rho$? Wohin zeigt das Feld bei $x>0$, und wohin läuft dort ein Elektron?

</li>

</ol>

:::loesung
(a) $Q'=eN_\mathrm Dd=7{,}2\cdot10^{-4}\,\mathrm{C/m^2}$, $|\mathcal E(0)|=Q'/\varepsilon=6{,}96$ MV/m, Bandverbiegung $e^2N_\mathrm Dd^2/(2\varepsilon)=0{,}522$ eV $=20{,}2\,k_\mathrm BT$. (b) Sie wächst mit $d^2$, also vierfach auf 2,09 eV, mehr als $E_\mathrm g$. So weit kommt es nicht: Erreicht die Verbiegung die Lücke, treten bewegliche Träger auf. (c) $\mathrm{d}^2\Phi/\mathrm{d} x^2=2a=4\,\mathrm{eV/\mu\text{}m^2}=e\rho/\varepsilon$ ergibt $\rho=+414\,\mathrm{C/m^3}$, also $2{,}6\cdot10^{15}$ Elementarladungen je cm$^3$. Aus $\mathrm{d} E_\mathrm C/\mathrm{d} x=e\mathcal E=2ax$ folgt $\mathcal E>0$: Das Feld zeigt nach rechts, das Elektron läuft nach links zum Minimum bei $x=0$.
:::
:::
