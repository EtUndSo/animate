---
title: Stufe 2: Ladung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1110400
summary: Diese Stufe klärt die erste Frage: Was ist Ladung, wie entsteht ein geladener Körper, und was bleibt dabei erhalten?
tags: Elektronenmangel, Elektronenüberschuss, Elementarladung, Ladungserhaltung, Leiter, Isolator
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Diese Stufe klärt die erste Frage: Was ist Ladung, wie entsteht ein geladener Körper, und was bleibt dabei erhalten?
:::

**Die Idee.** Reibungselektrizität, der Blitz als Entladung getrennter Ladungen durch die Luft und der Magnetismus lassen sich nicht aus der Mechanik erklären. Reibt man einen Glasstab mit einem Seidentuch und einen Hartgummistab mit einem Fell, ziehen sich die Stäbe an, zwei Hartgummistäbe stoßen sich ab (Abb. [3](#abb-3)). Beim Reiben entsteht nichts Neues, Elektronen wechseln den Körper. Verschiedene Stoffe binden ihre äußeren Elektronen unterschiedlich fest. An den Berührstellen gehen Elektronen zu dem Stoff über, der sie stärker bindet, und das Reiben schafft viele solche Stellen. Ein Körper mit __Elektronenmangel__ ist positiv geladen, einer mit __Elektronenüberschuss__ negativ.

:::abbildung et1/k1reibung 3
Oben: Reiben trennt Ladung. Elektronen ($\mathrm{e}^-$) gehen vom Glas auf die Seide und vom Fell auf den Gummi. Unten: Ungleichnamig geladene Stäbe ziehen sich an, gleichnamig geladene stoßen sich ab.
:::

:::definition Definition 2.1 (Ladung)
<span class="anker" id="satz-2-1"></span>

Ein Körper mit $N_\mathrm{p}$ Protonen und $N_\mathrm{e}$ Elektronen trägt die Ladung

<span class="anker" id="gl-2-1"></span>
$$Q=(N_\mathrm{p}-N_\mathrm{e})\,e,\qquad e=1{,}602\cdot10^{-19}\,\mathrm{C},\qquad[Q]=\mathrm C=\mathrm{A\,s}. \tag{2.1}$$

Die __Elementarladung__ $e$ ist die kleinste frei vorkommende Ladung. Ein Elektron trägt $-e$, ein Proton $+e$. In einem abgeschlossenen System bleibt die Summe aller Ladungen konstant (__Ladungserhaltung__).
:::

⁠**So liest man das:** Ladung kommt nur in Vielfachen von $e$ vor, ein Coulomb sind $6{,}24\cdot10^{18}$ Elementarladungen. Geriebene Stäbe tragen um 10 nC. **Gültigkeit:** Die Stufung merkt man nur bei einzelnen Teilchen, schon 1 nC sind sechs Milliarden Elektronen. In Schaltungen behandelt man Ladung deshalb als stetige Größe.

:::herleitung Warum Reiben die Gesamtladung nicht ändert
Zwei Körper tragen zusammen $Q_1+Q_2=\bigl[(N_\mathrm{p1}+N_\mathrm{p2})-(N_\mathrm{e1}+N_\mathrm{e2})\bigr]e$. Geht ein Elektron von 1 nach 2, wird $N_\mathrm{e1}$ um eins kleiner und $N_\mathrm{e2}$ um eins größer, die Klammer bleibt gleich. Die durch Reiben „erzeugten“ Ladungen ergeben zusammen immer null.
:::

Die Namen sind älter als das Elektron. DuFay unterschied 1733 glasige und harzige Elektrizität, Franklin nannte um 1750 die eine positiv, die andere negativ. Das griechische Wort für Bernstein, *elektron*, gab dem Gebiet den Namen.

**Leiter und Isolatoren.** In einem __Leiter__ wie Metall kann je Atom mindestens ein Elektron durch den ganzen Körper wandern. In einem __Isolator__ wie Glas oder Gummi bleiben die Elektronen an ihren Atomen. Deshalb bleibt Ladung auf einem Isolator, wo sie entstanden ist, während sie sich auf Metall sofort verteilt.

::::beispiel
Kugel A ($+10$ nC) fehlen $N=Q/e=6{,}24\cdot10^{10}$ Elektronen. Eine Kunststoffkugel von 1 g enthält rund $3{,}2\cdot10^{23}$ Elektronen, es fehlt also nur eines von $5\cdot10^{12}$.
::::

⁠**Grenzfall:** Für $N_\mathrm{p}=N_\mathrm{e}$ ist $Q=0$. Ein neutraler Körper enthält nicht wenig Ladung, sondern gleich viel von beiden Vorzeichen.

:::frage Warum heißt ausgerechnet der Mangel an Elektronen positiv?
Weil die Vorzeichen vergeben wurden, bevor man Elektronen kannte. Franklin nannte geriebenes Glas positiv, erst viel später zeigte sich, dass es dabei Elektronen verliert. Die Festlegung blieb, also trägt das Elektron negative Ladung. Physikalisch ist daran nichts besonders.
:::

:::aufgabe Aufgabe 2 ★ Ladungen zählen
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Ein Glasstab trägt nach dem Reiben $+8$ nC. Wie viele Elektronen hat er abgegeben? Welche Ladung trägt das Tuch, wenn vorher beide neutral waren?

</li>

<li>

Zwei gleiche Metallkugeln tragen $+8$ nC und $-2$ nC. Sie berühren sich und werden getrennt. Welche Ladung trägt jede? Wie viele Elektronen sind übergegangen, und in welche Richtung?

</li>

</ol>

:::loesung
(a) $N=8\cdot10^{-9}\,\mathrm{C}/(1{,}602\cdot10^{-19}\,\mathrm{C})=4{,}99\cdot10^{10}$ Elektronen. Das Tuch hat sie aufgenommen und trägt $-8$ nC. (b) Die Gesamtladung $+6$ nC bleibt erhalten und verteilt sich auf gleiche Kugeln gleichmäßig: je $+3$ nC. Die negative Kugel gibt also $5\cdot10^{-9}\,\mathrm{C}/e=3{,}12\cdot10^{10}$ Elektronen an die positive ab.
:::
:::

::::lernkarten
:::karte begriff Ladung
Was ist die elektrische Ladung $Q$ eines Körpers?
---
Die Eigenschaft der Protonen und Elektronen, elektrische Kräfte auszuüben und zu spüren. Ein Körper mit $N_\mathrm{p}$ Protonen und $N_\mathrm{e}$ Elektronen trägt $Q=(N_\mathrm{p}-N_\mathrm{e})\,e$, Einheit Coulomb, $\mathrm C=\mathrm{A\,s}$.
--- falsch
Die Eigenschaft der Protonen und Elektronen, elektrische Kräfte auszuüben und zu spüren. Ein Körper mit $N_\mathrm{p}$ Protonen und $N_\mathrm{e}$ Elektronen trägt $Q=(N_\mathrm{p}+N_\mathrm{e})\,e$, Einheit Coulomb, $\mathrm C=\mathrm{A\,s}$.
--- falsch
Die Eigenschaft der Protonen und Elektronen, elektrische Kräfte auszuüben und zu spüren. Ein Körper mit $N_\mathrm{p}$ Protonen und $N_\mathrm{e}$ Elektronen trägt $Q=(N_\mathrm{e}-N_\mathrm{p})\,e$, Einheit Coulomb, $\mathrm C=\mathrm{A\,s}$.
--- falsch
Die Menge der Elektronen in einem Körper, ausgedrückt in Coulomb. Ein Körper mit $N_\mathrm{e}$ Elektronen trägt $Q=N_\mathrm{e}\,e$, gleich wie viele Protonen er enthält; $\mathrm C=\mathrm{A\,s}$.
:::
:::karte begriff Elementarladung
Was ist die Elementarladung $e$?
---
Die kleinste frei vorkommende Ladung, $e=1{,}602\cdot10^{-19}\,\mathrm{C}$. Ein Proton trägt $+e$, ein Elektron $-e$; Ladung kommt nur in Vielfachen von $e$ vor.
--- falsch
Die kleinste frei vorkommende Ladung, $e=1{,}602\cdot10^{-19}\,\mathrm{C}$. Ein Elektron trägt $+e$, ein Proton $-e$; Ladung kommt nur in Vielfachen von $e$ vor.
--- falsch
Die kleinste Ladung, die ein Messgerät noch auflösen kann, $e=1{,}602\cdot10^{-19}\,\mathrm{C}$. Darunter ist Ladung stetig verteilt und beliebig teilbar.
--- falsch
Die größte Ladung, die ein geriebener Körper tragen kann, rund 10 nC. Mehr Ladung kann er nicht halten, der Überschuss entlädt sich sofort.
:::
:::karte begriff Ladungserhaltung
Was besagt die Ladungserhaltung?
---
In einem abgeschlossenen System bleibt die Summe aller Ladungen konstant. Ladung entsteht nicht neu, sie wird nur zwischen Körpern verschoben.
--- falsch
In einem abgeschlossenen System bleibt die Zahl der Elektronen auf jedem einzelnen Körper konstant. Ladung kann den Körper nicht wechseln.
--- falsch
In einem abgeschlossenen System bleibt nur die positive Ladung konstant. Negative Ladung entsteht beim Reiben neu und vergeht beim Entladen.
--- falsch
Die Ladung eines Körpers bleibt erhalten, solange er ein Isolator ist. Auf einem Leiter geht sie verloren, weil sie sich sofort verteilt.
:::
:::karte zusammenhang Reibungselektrizität
Warum ist ein Glasstab nach dem Reiben mit einem Seidentuch positiv geladen?
---
Weil die Seide äußere Elektronen stärker bindet als das Glas. An den vielen Berührstellen gehen Elektronen vom Glas zur Seide; dem Glas fehlen dann Elektronen, die Seide trägt die gleich große negative Ladung.
--- falsch
Weil die Reibungswärme im Glas neue positive Ladung erzeugt. Die Seide bleibt dabei neutral, weil sie sich beim Reiben weniger stark erwärmt als das Glas und deshalb keine Ladung bildet.
--- falsch
Weil das Glas Protonen stärker bindet als die Seide. An den vielen Berührstellen gehen Protonen von der Seide zum Glas über; das Glas hat danach einen Überschuss an Protonen.
--- falsch
Weil das Glas äußere Elektronen stärker bindet als die Seide. An den vielen Berührstellen gehen Elektronen von der Seide zum Glas über, und dieser Überschuss an Elektronen macht das Glas positiv, die Seide negativ.
:::
:::karte herleitung Reiben ändert die Gesamtladung nicht
Zeige mit $Q=(N_\mathrm{p}-N_\mathrm{e})\,e$, dass Reiben die Gesamtladung zweier Körper nicht ändert.
---
Zusammen tragen die Körper $Q_1+Q_2=\bigl[(N_\mathrm{p1}+N_\mathrm{p2})-(N_\mathrm{e1}+N_\mathrm{e2})\bigr]e$, weil sich die Ladungen beider Körper addieren.
---
Beim Reiben wechseln nur Elektronen den Körper, weil die Protonen fest im Kern sitzen. $N_\mathrm{p1}$ und $N_\mathrm{p2}$ bleiben gleich.
---
Geht ein Elektron von 1 nach 2, wird $N_\mathrm{e1}$ um eins kleiner und $N_\mathrm{e2}$ um eins größer, weil das Elektron nur den Körper wechselt.
---
Die Summe $N_\mathrm{e1}+N_\mathrm{e2}$ und damit die Klammer bleibt gleich, weil sich die Änderungen um eins aufheben. Die durch Reiben „erzeugten“ Ladungen ergeben zusammen null.
:::
:::karte begriff Leiter und Isolator
Was unterscheidet einen Leiter von einem Isolator?
---
In einem Leiter wie Metall kann je Atom mindestens ein Elektron durch den ganzen Körper wandern. In einem Isolator wie Glas oder Gummi bleiben die Elektronen an ihren Atomen.
--- falsch
In einem Leiter wie Metall wandern die Protonen durch den ganzen Körper. In einem Isolator wie Glas oder Gummi sitzen sie fest in den Kernen ihrer Atome.
--- falsch
Ein Leiter wie Metall enthält Elektronen, ein Isolator wie Glas oder Gummi enthält keine. Deshalb lässt sich ein Isolator auch durch Reiben nicht aufladen, ein Leiter dagegen schon.
--- falsch
In einem Leiter wie Metall bleiben die Elektronen an ihren Atomen. In einem Isolator wie Glas oder Gummi kann je Atom ein Elektron durch den ganzen Körper wandern.
:::
:::karte zusammenhang Ladung als stetige Größe
Warum darf man Ladung in Schaltungen als stetige Größe behandeln, obwohl sie nur in Vielfachen von $e$ vorkommt?
---
Weil $e$ winzig ist: Schon 1 nC sind sechs Milliarden Elektronen, ein Coulomb sind $6{,}24\cdot10^{18}$ Elementarladungen. Die Stufung merkt man nur bei einzelnen Teilchen.
--- falsch
Weil sich die Elektronen beim Wandern durch Metall in kleinere Teilladungen aufspalten. Dadurch wird die Stufung in Schaltungen beliebig fein und verschwindet.
--- falsch
Weil in Schaltungen Protonen und Elektronen zugleich fließen. Ihre Stufen sind gegeneinander versetzt und füllen sich gegenseitig zu einer stetigen Größe auf.
--- falsch
Weil die Elementarladung in Metall viel kleiner ist als im Vakuum. In Drähten fällt die Stufung deshalb nicht mehr ins Gewicht, im Vakuum dagegen schon.
:::
:::karte zusammenhang Vorzeichen der Ladung
Woran liegt es, dass ausgerechnet ein Mangel an Elektronen positiv heißt?
---
An der Geschichte: Franklin nannte geriebenes Glas positiv, bevor man Elektronen kannte. Dass das Glas dabei Elektronen verliert, zeigte sich erst später; die Festlegung blieb.
--- falsch
An der Physik: Protonen wirken stärker als Elektronen. Überwiegen sie, zeigt das Plus diese größere Wirkung an, unabhängig von jeder Festlegung.
--- falsch
An einer Festlegung nach der Entdeckung des Elektrons: Man wollte, dass die Bewegungsrichtung der Elektronen in Rechnungen positiv zählt, und benannte die Vorzeichen danach.
--- falsch
An der Masse: Das Proton ist 1836-mal schwerer als das Elektron. Der schwerere Baustein bekam das Plus, der leichtere das Minus.
:::
::::
