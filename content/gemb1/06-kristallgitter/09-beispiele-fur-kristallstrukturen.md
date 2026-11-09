---
title: Stufe 7: Beispiele für Kristallstrukturen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallgitter
order: 4160900
summary: Gitter und Basis sind das Werkzeug.
tags: hexagonal dichteste Kugelpackung, kubisch dichteste Kugelpackung, Diamantstruktur, Zinkblendestruktur
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Gitter und Basis sind das Werkzeug. Diese Stufe wendet es auf die Strukturen an, in denen Metalle, Salze und Silizium kristallisieren.
:::

**Die Idee.** Welche Struktur ein Stoff wählt, entscheiden vor allem Atomgröße und Bindungsart ([Teil 5](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung/chemische-bindung.html)). Eine ungerichtete Bindung belohnt jeden weiteren Nachbarn, also wird dicht gepackt. Eine gerichtete Bindung lässt Nachbarn nur in festen Winkeln zu, also bleibt die Struktur offen. Ionen wollen Nachbarn mit Gegenladung.

| Bindung | Richtung | Ladung | Packung |
|---|---|---|---|
| metallisch | ungerichtet | ohne Vorzeichen | sehr dicht, viele Nachbarn |
| ionisch | ungerichtet | mit Vorzeichen | mittel bis groß, die Radien entscheiden |
| kovalent | gerichtet | entfällt | klein, die Bindungen entscheiden |
| Moleküldipol | Vorzugsrichtung | entfällt | Dipolrichtung und Molekülform entscheiden |
| Van der Waals | ungerichtet | ohne Vorzeichen | sehr dicht |

**Dichteste Kugelpackungen.** Gleich große Kugeln liegen in einer Ebene am dichtesten hexagonal: Jede hat sechs Nachbarn (Lage A). Darauf gibt es zwei Sorten von Mulden, B und C, und die nächste Lage kann nur eine Sorte füllen, sagen wir B (Abb. [7](#abb-7)). Für die dritte Lage gibt es zwei Wege:

<ul>

<li>

⁠**ABAB…:** Sie liegt über A. Das ist die __hexagonal dichteste Kugelpackung__ (hdp), etwa Mg, Co, Zn, Ti, Zr, Cd.

</li>

<li>

⁠**ABCABC…:** Sie liegt über C, erst die vierte wieder über A. Das ist die __kubisch dichteste Kugelpackung__ (kdp), etwa Al, Cu, Au, Pt, Ag, Pb. Sie ist das FCC-Gitter: Die Lagen sind seine $(111)$-Ebenen.

</li>

</ul>

Beide haben die Koordinationszahl 12 (sechs in der Lage, je drei darüber und darunter) und $P=74{,}0\,\%$, denn jede Lage ist gleich dicht und der Lagenabstand ist in beiden $h=\sqrt{2/3}\,d$, mit dem Nachbarabstand $d$. Die hexagonale Packung ist kein Bravais-Gitter, denn A- und B-Plätze sehen ihre Nachbarn gedreht. Sie ist ein hexagonales Gitter mit zwei Atomen je Zelle. Mit $a=d$ und $c=2h$ ist $c/a=\sqrt{8/3}=1{,}633$ der Idealwert. Mg liegt mit 1,624 nahe daran, Zn mit 1,856 deutlich darüber: Das Kugelmodell gilt nicht für jedes Metall. Die dritte verbreitete Struktur der Metalle ist BCC mit $P=68\,\%$, etwa Fe, Cr, K, Na, Mo, W.

:::abbildung gemb1/k6struktur 7
Oben links: eine dichte Lage mit den beiden Muldensorten. Oben Mitte und rechts: Stapelfolgen in schematischer Seitenansicht. Unten links die Diamantstruktur: Zwei FCC-Gitter (blau, grün), um $\boldsymbol d$ verschoben, jedes Atom hat vier Nachbarn. Unten rechts die Kochsalzstruktur: Zwei FCC-Gitter, um eine halbe Kante verschoben, jedes Ion hat sechs Nachbarn der anderen Sorte.
:::

**Kochsalzstruktur.** NaCl ist FCC mit einer Basis aus zwei Ionen: Cl$^-$ bei $\boldsymbol d_1=0$, Na$^+$ bei $\boldsymbol d_2=(a/2,0,0)$. Der Würfel enthält je vier Ionen: $8\cdot\frac18+6\cdot\frac12=4$ Cl$^-$ und $12\cdot\frac14+1=4$ Na$^+$. Jedes Ion hat sechs Gegenionen im Abstand $a/2=0{,}282$ nm. Dieselbe Struktur haben LiF, KCl und KI. Die Coulomb-Anziehung hält das Gitter zusammen, denn die nächsten Nachbarn jedes Ions sind Gegenladungen.

:::definition Definition 7.1 (Diamantstruktur)
<span class="anker" id="satz-7-1"></span>

Die __Diamantstruktur__ ist FCC mit einer zweiatomigen Basis:

<span class="anker" id="gl-7-1"></span>
$$\boldsymbol d_1=0,\qquad \boldsymbol d_2=\boldsymbol d=\frac a4\,(1,1,1). \tag{7.1}$$

Sie besteht aus zwei FCC-Gittern, die um ein Viertel der Raumdiagonale gegeneinander verschoben sind. C, Si und Ge kristallisieren so. Besetzen zwei Atomsorten die beiden Gitter, heißt sie __Zinkblendestruktur__, etwa ZnS, GaAs und InSb.
:::

⁠**So liest man das:** Der Würfel enthält $4+4=8$ Atome. Die Basis liegt auf einer Raumdiagonale, und jedes Atom hat vier Nachbarn im Abstand $\sqrt3\,a/4$ an den Ecken eines Tetraeders. Das ist die Form der vier sp$^3$-Bindungen mit dem Winkel 109,47° ([Teil 5](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung/chemische-bindung.html)), so wie die drei sp$^2$-Bindungen in der Ebene die Wabe aus Stufe [2](bravais-gitter-in-einer-und-zwei-dimensionen.html#stufe-2) ergeben. Die gerichtete Bindung erzwingt die offene Struktur: Mit $r_\mathrm{at}=\sqrt3\,a/8$ füllen gleiche Kugeln nur $P=8\cdot\frac43\pi r_\mathrm{at}^3/a^3=\sqrt3\,\pi/16=34\,\%$, weniger als die Hälfte von FCC. Zwischen ionischer und kovalenter Bindung gibt es einen stetigen Übergang: ZnS, GaAs und InSb haben auch ionischen Charakter, weil die beiden Sorten verschieden stark an den Elektronen ziehen.

::::beispiel
GaAs hat $a=0{,}5653$ nm, der Abstand von Ga zu As ist $\sqrt3\,a/4=0{,}2448$ nm, und [(5.2)](koordinationszahl-und-packungsdichte.html#gl-5-2) ergibt mit vier Ga und vier As $\rho_\mathrm m=5{,}32\,\mathrm{g/cm^3}$.
::::

⁠**Grenzfall:** Sind beide Atomsorten gleich, wird aus Zinkblende Diamant. Rückt $\boldsymbol d$ auf $\frac a2(1,1,1)$, entsteht aus zwei FCC-Gittern kein Tetraeder mehr, sondern die Kochsalzstruktur, denn $\frac a2(1,1,1)$ und $\frac a2(1,0,0)$ unterscheiden sich um einen Gittervektor.

:::frage Alle Atome in Silizium sind gleich und haben vier Nachbarn. Warum ist die Struktur kein Bravais-Gitter?
Weil die Nachbarn in verschiedenen Richtungen liegen. Ein Atom von Basisplatz 1 hat einen Nachbarn bei $+\boldsymbol d$, ein Atom von Basisplatz 2 bei $-\boldsymbol d$. Die beiden Tetraeder sind gegeneinander umgekehrt. Verschiebt man den Kristall um $\boldsymbol d$, landen die Atome von Platz 2 in leeren Bereichen, wie bei der Wabe.
:::

:::aufgabe Aufgabe 10 ★★ Silizium
<span class="anker" id="aufg-10"></span>

Silizium hat $a=0{,}5431$ nm.

<ol class="al">

<li>

Berechne die Atomdichte, den Bindungsabstand und das Volumen je Atom.

</li>

<li>

Berechne $\rho_\mathrm m$. Gemessen werden 2,33 g/cm$^3$.

</li>

<li>

Wie viele Atome je cm$^2$ liegen auf einer $(100)$-Fläche eines der beiden FCC-Gitter, wie viele auf einer $(111)$-Fläche? Welche ist dichter belegt?

</li>

</ol>

:::loesung
(a) $8/a^3=4{,}99\cdot10^{22}\,\mathrm{cm^{-3}}$. Bindungsabstand $\sqrt3\,a/4=0{,}2352$ nm. Volumen je Atom $a^3/8=0{,}0200\,\mathrm{nm^3}$. (b) $\rho_\mathrm m=8\cdot28{,}09\,\mathrm{g/mol}/(N_\mathrm{Av}\,a^3)=2{,}329\,\mathrm{g/cm^3}$. (c) $(100)$: Die Würfelfläche enthält $4\cdot\frac14+1=2$ Atome auf $a^2$, also $6{,}78\cdot10^{14}\,\mathrm{cm^{-2}}$. $(111)$: Die Atome bilden ein hexagonales Gitter mit dem Abstand $a/\sqrt2$, die Zelle hat $\frac{\sqrt3}4a^2$, also $4/(\sqrt3\,a^2)=7{,}83\cdot10^{14}\,\mathrm{cm^{-2}}$. Die $(111)$-Fläche ist 15 % dichter belegt.
:::
:::
