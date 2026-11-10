---
title: Stufe 4: Die Feldstärke
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1110600
summary: Das Coulomb-Gesetz nennt die Kraft, sagt aber nicht, wie sie durch den leeren Raum gelangt.
tags: Probeladung, elektrische Feldstärke
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Das Coulomb-Gesetz nennt die Kraft, sagt aber nicht, wie sie durch den leeren Raum gelangt. Der Begriff des Felds beantwortet das und trennt die Ursache von der Wirkung.
:::

**Die Idee.** Statt „B zieht A über 3 cm hinweg“ zerlegt man den Vorgang. Erstens: Ladung B verändert den Raum um sich, sie erzeugt ein Feld. Zweitens: Ladung A spürt das Feld an ihrem eigenen Ort und erfährt dort eine Kraft. Warum Ladungen Felder erzeugen, lässt sich nicht auf Einfacheres zurückführen, es ist ein Grundgesetz. Das Bild löst aber drei Probleme. **Ursache und Wirkung werden getrennt:** Das Feld hängt nur von den erzeugenden Ladungen ab und gilt für jede Ladung, die man hineinbringt. **Viele Ladungen werden beherrschbar:** Man addiert ihre Felder einmal und rechnet danach mit einem Vektor je Ort. **Die Wirkung braucht Zeit:** Verschiebt man B, ändert sich die Kraft auf A erst, wenn die Änderung des Felds mit Lichtgeschwindigkeit dort ankommt. Über 3 cm dauert das 100 ps, von der Sonne zur Erde 8,3 Minuten. In der Zwischenzeit steckt die Änderung im Feld, es ist also mehr als eine Rechenhilfe.

:::analogie
Die Erde umgibt ein Schwerefeld: An jedem Ort wirkt auf jede Masse die Kraft $\vec F=m\,\vec g$. Das Feld $\vec g$ ist Kraft je Masse, das elektrische Feld ist Kraft je Ladung. Das Bild endet an zwei Stellen: Massen ziehen sich immer an, und ein Schwerefeld lässt sich nicht abschirmen.
:::

:::definition Definition 4.1 (Elektrische Feldstärke)
<span class="anker" id="satz-4-1"></span>

Bringt man eine kleine __Probeladung__ $Q$ an einen Ort und misst die Kraft $\vec F$ auf sie, ist die __elektrische Feldstärke__ dort

<span class="anker" id="gl-4-1"></span>
$$\vec E:=\lim_{Q\to0}\frac{\vec F}{Q},\qquad\text{also}\quad\vec F=Q\cdot\vec E. \tag{4.1}$$

Die Richtung von $\vec E$ ist die Richtung der Kraft auf eine positive Probeladung. Das elektrische Feld ordnet jedem Ort einen solchen Vektor zu.
:::

⁠**So liest man das:** Die Einheit ist $[E]=\mathrm{N/C}=\mathrm{m\,kg\,A^{-1}\,s^{-3}}=\mathrm{V/m}$, denn $\mathrm V=\mathrm{J/C}=\mathrm{N\,m/C}$. Auf eine negative Ladung wirkt die Kraft entgegen $\vec E$. Typische Werte: im stromdurchflossenen Leiter 0,1 V/m, in der Atmosphäre bei klarem Wetter 100 bis 200 V/m, an der Oberfläche einer Rundfunkantenne 1 bis 1000 V/m, an einer Hochspannungsleitung $10^6$ V/m, in einem Kondensator (Bauteil aus zwei Platten, [Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)) $10^6$ bis $10^8$ V/m. Bei $3\cdot10^6$ V/m schlägt Luft durch, es entsteht ein Funke. **Gültigkeit:** Der Grenzwert $Q\to0$ ist nötig, weil eine große Probeladung die erzeugenden Ladungen verschiebt, etwa die freien Elektronen einer Metallplatte. Gemessen werden soll aber das Feld ohne Probeladung.

:::satz Satz 4.2 (Feld von Punktladungen)
<span class="anker" id="satz-4-2"></span>

Eine Punktladung $Q_0$ erzeugt im Abstand $r$ das Feld

<span class="anker" id="gl-4-2"></span>
$$\vec E=k\,\frac{Q_0}{r^2}\cdot\frac{\vec r}{r},\qquad E=k\,\frac{|Q_0|}{r^2}, \tag{4.2}$$

wobei $\vec r$ von der Ladung zum Ort zeigt. Mehrere Ladungen erzeugen zusammen die Summe ihrer Felder: $\vec E=\sum_i\vec E_i$.
:::

:::herleitung Feld einer Punktladung
Eine Probeladung $Q$ erfährt nach [(3.2)](die-kraft-zwischen-ladungen.html#gl-3-2) die Kraft $\vec F=k\,Q\,Q_0/r^2\cdot\vec r/r$. Division durch $Q$ lässt $Q$ verschwinden, das Ergebnis hängt nur noch von $Q_0$ und dem Ort ab. Die Summenregel folgt aus der Überlagerung der Kräfte.
:::

:::abbildung et1/k1feldpfeile 5
Feldvektoren um eine positive und eine negative Punktladung. Das Feld zeigt von der positiven Ladung weg und zur negativen hin. Die Pfeillänge ist proportional zu $1/r^2$.
:::

::::beispiel
Kugel B ($-20$ nC) erzeugt am Ort von Kugel A das Feld $E=k\cdot20\,\mathrm{nC}/(3\,\mathrm{cm})^2=2{,}0\cdot10^5$ V/m, es zeigt auf B zu. Die Kraft auf A ist $F=10\,\mathrm{nC}\cdot2{,}0\cdot10^5\,\mathrm{V/m}=2{,}0$ mN wie in Stufe [3](die-kraft-zwischen-ladungen.html#stufe-3). Umgekehrt erzeugt A am Ort von B nur $1{,}0\cdot10^5$ V/m, trifft dort aber auf die doppelte Ladung: wieder 2,0 mN.
::::

⁠**Kurz gesagt:** Die Kraft auf eine Ladung ist ihre Ladung mal das Feld an ihrem Ort.

⁠**Grenzfälle:** Für $r\to\infty$ geht $E\to0$. Für $r\to0$ würde $E$ unbegrenzt wachsen, das zeigt die Grenze des Modells Punktladung.

:::frage Spürt eine Ladung auch ihr eigenes Feld?
In $\vec F=Q\vec E$ steht nur das Feld der *anderen* Ladungen. Eine ruhende Ladung übt auf sich selbst keine Kraft aus.
:::

:::aufgabe Aufgabe 4 ★★ Zwei Ladungen, ein feldfreier Punkt
<span class="anker" id="aufg-4"></span>

Auf der $x$-Achse liegen $Q_1=+4$ nC bei $x=0$ und $Q_2=+1$ nC bei $x=6$ cm.

<ol class="al">

<li>

Berechne Betrag und Richtung des Felds bei $x=3$ cm. Welche Kraft erfährt dort ein Elektron?

</li>

<li>

Wo zwischen den Ladungen ist $E=0$?

</li>

<li>

Grenzfall: Wohin wandert dieser Punkt für $Q_2\to0$? Passt das zum Feld einer einzelnen Ladung?

</li>

</ol>

:::loesung
(a) $E_1=k\cdot4\,\mathrm{nC}/(3\,\mathrm{cm})^2=40{,}0$ kV/m nach rechts, $E_2=k\cdot1\,\mathrm{nC}/(3\,\mathrm{cm})^2=9{,}99$ kV/m nach links, zusammen $E=30{,}0$ kV/m nach rechts. Elektron: $F=e\,E=4{,}8\cdot10^{-15}$ N nach links.

(b) $E=0$ verlangt $Q_1/x^2=Q_2/(a-x)^2$ mit $a=6$ cm. Daraus $2/x=1/(a-x)$, also $x=\frac23a=4$ cm. (c) Allgemein ist $x=a/(1+\sqrt{Q_2/Q_1})$. Für $Q_2\to0$ geht $x\to a$: Der Punkt wandert an den Ort von $Q_2$ und verschwindet: Eine einzelne Ladung hat keinen feldfreien Punkt.
:::
:::
