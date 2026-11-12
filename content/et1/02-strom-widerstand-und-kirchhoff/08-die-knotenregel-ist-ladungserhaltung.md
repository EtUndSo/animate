---
title: Stufe 7: Die Knotenregel ist Ladungserhaltung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1120800
summary: Die erste Gleichungsart: Was verlangt die Erhaltung der Ladung an einem Knoten?
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Die erste Gleichungsart: Was verlangt die Erhaltung der Ladung an einem Knoten?
:::

**Die Idee.** Ein Knoten ist ein Stück Draht. Fließt mehr hinein als heraus, sammelt sich auf ihm Ladung, und sein Potenzial steigt. Dadurch sinkt die Spannung an den zuführenden Widerständen, und sie steigt an den abführenden. Der Zufluss nimmt ab, der Abfluss nimmt zu, bis beide gleich sind. Diese Selbstregelung läuft in Nanosekunden ab. Sie ist der Mechanismus hinter der Regel: Der Knoten stellt sich auf genau das Potenzial ein, bei dem nichts hängen bleibt.

:::satz Satz 7.1 (Knotenregel, erstes kirchhoffsches Gesetz)
<span class="anker" id="satz-7-1"></span>

Die Summe aller Ströme, die in einen Knoten hineinfließen, ist in jedem Zeitpunkt null. Gleichwertig ist die Summe der zufließenden Ströme gleich der Summe der abfließenden:

<span class="anker" id="gl-7-1"></span>
$$\sum_{\nu=1}^{N}I_\nu=0\quad\text{(alle Pfeile zum Knoten)},\qquad\sum I_\mathrm{zu}=\sum I_\mathrm{ab}. \tag{7.1}$$

Für ein Netz mit $k$ Knoten sind $k-1$ dieser Gleichungen unabhängig.
:::

⁠**So liest man das:** Die Pfeile sind frei wählbar. Zeigen alle zum Knoten, muss mindestens einer der Ströme negativ sein, oder alle sind null. Bei gemischten Pfeilen zählen zufließende positiv, abfließende negativ. **Gültigkeit:** Der Knoten darf keine nennenswerte Ladung speichern. Das gilt, solange sich die Ströme langsam gegen die Ausgleichszeit ändern. Die Herleitung gibt dafür eine Zahl.

:::abbildung et1/k2knoten 8
Links: Knoten mit zwei zufließenden und drei abfließenden Strömen, Summe je 7 mA. Rechts: Die Regel gilt auch für eine Hülle um einen Teil des Netzes, hier um $K_2$, $K_3$ und $R_\mathrm e$. Der Strom in $R_\mathrm e$ bleibt innen und zählt nicht.
:::

:::herleitung Knotenregel aus der Ladungserhaltung
Für die Ladung $Q_\mathrm K$ auf dem Knoten gilt $\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$, denn Ladung entsteht und verschwindet nicht. Wie klein $Q_\mathrm K$ bleibt, zeigt eine Abschätzung mit [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html): Eine Metallkugel mit 1 cm Radius hat das Potenzial $\varphi=k_\mathrm C\,Q/r$ mit der Coulomb-Konstante $k_\mathrm C=8{,}99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$. Für 9 V reichen $Q=10$ pC. Ein Überschuss von 3 mA liefert das in 3,3 ns. Deshalb ist $\mathrm{d} Q_\mathrm K/\mathrm{d} t$ gegen die Ströme vernachlässigbar, und es bleibt $\sum I_\nu=0$.
:::

**Warum eine Gleichung überflüssig ist.** Jeder Zweig verbindet zwei Knoten. Sein Strom tritt deshalb in genau zwei Knotengleichungen auf, einmal mit $+$ (zufließend) und einmal mit $-$ (abfließend). Addiert man alle $k$ Gleichungen, heben sich alle Ströme auf. Eine Gleichung folgt also aus den übrigen, und jede Auswahl von $k-1$ Gleichungen ist unabhängig.

::::beispiel
Alle Strompfeile im Netz zeigen in Richtung des tatsächlichen Stroms: von $K_1$ durch die Widerstände nach unten, $I_\mathrm e$ von $K_2$ nach $K_3$, $I_0$ durch die Quelle von $K_4$ nach $K_1$. Die Knotengleichungen lauten

$$\begin{aligned} K_1:&\quad +I_0-I_\mathrm a-I_\mathrm c=0, & K_2:&\quad +I_\mathrm a-I_\mathrm b-I_\mathrm e=0,\\ K_3:&\quad +I_\mathrm c-I_\mathrm d+I_\mathrm e=0, & K_4:&\quad -I_0+I_\mathrm b+I_\mathrm d=0. \end{aligned}$$

Die Summe der ersten drei ist $I_0-I_\mathrm b-I_\mathrm d=0$, die vierte Gleichung mit umgekehrtem Vorzeichen. Addiert man nur $K_2$ und $K_3$, fällt $I_\mathrm e$ heraus, und es bleibt die Hülle aus Abb. [8](#abb-8): $I_\mathrm a+I_\mathrm c=I_\mathrm b+I_\mathrm d$. **Kontrolle:** An einem Punkt mit nur zwei Zweigen folgt $I_1=I_2$. Durch hintereinanderliegende Bauteile fließt derselbe Strom.
::::

:::frage Gilt die Regel auch, wenn an einem Knoten ein Kondensator hängt?
Ja. Der Strom zur Platte ist ein Zweigstrom wie jeder andere, die Ladung sammelt sich nicht auf dem Knoten, sondern auf der Platte. [Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html) behandelt das.
:::

:::aufgabe Aufgabe 7 ★★ Knotenregel anwenden
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Vier Strompfeile zeigen zum Knoten: $I_1=5$ mA, $I_2=-2$ mA, $I_3=-1$ mA. Wie groß ist $I_4$, und in welche Richtung fließt er wirklich?

</li>

<li>

Zeige aus den Knotengleichungen des Netzes $I_0=I_\mathrm b+I_\mathrm d$. Welche Hülle gehört dazu?

</li>

<li>

Vorhersage: Ein Überschuss von nur 1 µ A bliebe 1 s lang auf der Kugel aus der Herleitung. Welches Potenzial hätte sie? Warum geschieht das nicht?

</li>

</ol>

:::loesung
(a) $5-2-1+I_4=0$, also $I_4=-2$ mA: Es fließen 2 mA aus dem Knoten heraus.

(b) Addition von $K_1$, $K_2$, $K_3$ gibt $I_0-I_\mathrm b-I_\mathrm d=0$. Das ist die Hülle um $K_1$, $K_2$, $K_3$ oder, gleichwertig, die Gleichung von $K_4$. Mit Zahlen: $4=1+3$.

(c) $Q=1\,\mu\text{C}$ ergibt $\varphi=k_\mathrm C\,Q/r=0{,}9$ MV. Lange bevor dieser Wert erreicht wäre, treibt das steigende Potenzial den Überschuss ab. Das ist die Selbstregelung.
:::
:::

::::formelsammlung
**Knotenregel (erstes kirchhoffsches Gesetz)**

$$\sum_{\nu=1}^{N}I_\nu=0\quad\text{(alle Pfeile zum Knoten)},\qquad\sum I_\mathrm{zu}=\sum I_\mathrm{ab}$$

Gilt in jedem Zeitpunkt, solange der Knoten keine nennenswerte Ladung speichert, und auch für eine Hülle um einen Teil des Netzes. Für ein Netz mit $k$ Knoten sind $k-1$ dieser Gleichungen unabhängig.

**Ladung auf dem Knoten**

$$\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$$

Ladungserhaltung: Was mehr zu- als abfließt, sammelt sich auf dem Knoten und verschiebt sein Potenzial, bis Zu- und Abfluss gleich sind. Schon winzige Ladungen genügen dafür, deshalb bleibt $\sum I_\nu=0$.
::::

::::lernkarten
:::karte formel Knotenregel
Was besagt die Knotenregel, das erste kirchhoffsche Gesetz, über die Ströme an einem Knoten?
---
$\sum_{\nu=1}^{N}I_\nu=0$, wenn alle Pfeile zum Knoten zeigen, oder $\sum I_\mathrm{zu}=\sum I_\mathrm{ab}$; in jedem Zeitpunkt, solange der Knoten keine nennenswerte Ladung speichert.
--- falsch
$\sum_{\nu=1}^{N}I_\nu=0$, wenn alle Pfeile zum Knoten zeigen. Das heißt: Jeder einzelne Strom an einem Knoten ist null, sonst wäre die Summe nicht null.
--- falsch
$\sum I_\mathrm{zu}=\sum I_\mathrm{ab}$, aber nur im Mittel über längere Zeit. In jedem einzelnen Zeitpunkt kann ein Knoten beliebig viel Ladung aufnehmen und später wieder abgeben.
--- falsch
Die Summe der Spannungen aller Zweige an einem Knoten ist null, $\sum U=0$. Der Strom teilt sich dabei im Verhältnis der Widerstände auf.
:::
:::karte zusammenhang Knotenregel und Ladungserhaltung
Warum ist die Knotenregel eine Folge der Ladungserhaltung?
---
Weil für die Ladung auf dem Knoten $\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$ gilt: Ladung entsteht und verschwindet nicht. Der Knoten speichert fast nichts, also bleibt $\sum I_\nu=0$.
--- falsch
Weil an einem Knoten Energie weder entsteht noch verschwindet: Die Spannungen aller Zweige ergeben zusammen null, und daraus folgen die Ströme.
--- falsch
Weil die Ladungsträger am Knoten gleichmäßig verteilt werden: Jeder abgehende Zweig erhält gleich viel Ladung, gleich welchen Widerstand er hat und wie lang er ist.
--- falsch
Weil ein Knoten beliebig viel Ladung speichern kann: Was mehr hineinfließt, sammelt sich dort an, ohne sein Potenzial zu ändern.
:::
:::karte herleitung Knotenregel aus der Ladungserhaltung
Leite aus der Ladungserhaltung her, dass an einem Knoten $\sum I_\nu=0$ gilt, und begründe, warum die Ladung auf dem Knoten vernachlässigbar bleibt.
---
Für die Ladung $Q_\mathrm K$ auf dem Knoten gilt $\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$, weil Ladung weder entsteht noch verschwindet; die zufließenden Ströme ändern nur $Q_\mathrm K$.
---
Schätzt man den Knoten als Metallkugel mit 1 cm Radius ab, hat er das Potenzial $\varphi=k_\mathrm C\,Q/r$. Für 9 V reichen $Q=10$ pC, weil die Coulomb-Konstante $k_\mathrm C$ sehr groß ist.
---
Ein Überschuss von 3 mA liefert diese Ladung schon in 3,3 ns, weil der Strom die Ladung je Zeit ist.
---
Deshalb ist $\mathrm{d} Q_\mathrm K/\mathrm{d} t$ gegen die Ströme vernachlässigbar und es bleibt $\sum I_\nu=0$, weil schon winzige Ladungen das Potenzial des Knotens so verschieben, dass der Überschuss abfließt.
:::
:::karte zusammenhang Selbstregelung am Knoten
Was passiert, wenn in einen Knoten kurzzeitig mehr Strom hinein- als herausfließt?
---
Auf ihm sammelt sich Ladung, sein Potenzial steigt. Dadurch sinkt die Spannung an den zuführenden Widerständen und steigt an den abführenden, bis Zu- und Abfluss gleich sind.
--- falsch
Die überschüssige Ladung sammelt sich dauerhaft auf dem Knoten an. Sein Potenzial bleibt dabei trotzdem gleich, weil ein Knoten ein ideales Stück Draht ist.
--- falsch
Der Überschuss fließt in die Masse ab. Dafür braucht jeder Knoten eine eigene Verbindung zur Masse, sonst gilt die Knotenregel dort nicht.
--- falsch
Die Elektronen stauen sich vor dem Knoten und werden langsamer. Dadurch sinkt der Strom in den zuführenden Zweigen, während das Potenzial des Knotens dabei unverändert bleibt.
:::
:::karte zusammenhang Eine Knotengleichung zu viel
Warum sind in einem Netz mit $k$ Knoten nur $k-1$ Knotengleichungen unabhängig?
---
Weil jeder Zweigstrom in genau zwei Knotengleichungen steht, einmal mit $+$, einmal mit $-$. Addiert man alle $k$ Gleichungen, bleibt null: Eine folgt aus den übrigen.
--- falsch
Weil ein Knoten immer an der Quelle liegt. An ihm gilt die Knotenregel nicht, denn die Quelle bringt dort ständig zusätzliche Ladung in das Netz hinein.
--- falsch
Weil ein Knoten die Masse ist. An der Masse fließt Strom aus dem Netz ab, deshalb gilt dort keine Knotengleichung.
--- falsch
Weil jeder Zweigstrom in allen Knotengleichungen vorkommt. Eine Gleichung ist deshalb die Summe aller anderen, gleich welche man weglässt.
:::
:::karte zusammenhang Hülle um einen Netzteil
Gilt die Knotenregel auch für eine Hülle um einen Teil des Netzes, und warum?
---
Ja: Sie ist die Summe der Knotengleichungen aller Knoten in der Hülle. Ströme in Zweigen ganz innerhalb der Hülle treten dabei mit $+$ und $-$ auf und fallen heraus.
--- falsch
Nein: Die Regel gilt nur für einen einzelnen Punkt. In einer Hülle können die Widerstände Ladung speichern, deshalb geht die Summe nicht auf.
--- falsch
Ja, aber nur, wenn in der Hülle kein Widerstand liegt. Ein Widerstand in der Hülle verbraucht Strom, und die Summe wäre nicht mehr null.
--- falsch
Ja: Die Ströme aller Zweige in der Hülle ergeben zusammen null, auch die der inneren Zweige. Man muss deshalb jeden Zweig mitzählen, der irgendwo in der Hülle liegt.
:::
:::karte zusammenhang Gleicher Strom in Reihe
Warum fließt durch hintereinanderliegende Bauteile derselbe Strom?
---
Weil an ihrem Verbindungspunkt nur zwei Zweige zusammentreffen: Die Knotenregel ergibt dort $I_1=I_2$.
--- falsch
Weil die Quelle jedem Bauteil gleich viel Strom zuteilt, gleich ob es in Reihe oder parallel liegt.
--- falsch
Weil hintereinanderliegende Bauteile denselben Widerstand haben müssen; sonst wären auch die Ströme verschieden.
--- falsch
Weil der Strom im ersten Bauteil verbraucht und im zweiten im selben Maß wieder erzeugt wird.
:::
:::karte zusammenhang Kondensator am Knoten
Gilt die Knotenregel auch, wenn an einem Knoten ein Kondensator hängt?
---
Ja: Der Strom zur Platte ist ein Zweigstrom wie jeder andere. Die Ladung sammelt sich nicht auf dem Knoten, sondern auf der Platte.
--- falsch
Nein: Ein Kondensator speichert Ladung, deshalb ist die Summe der Ströme am Knoten nicht null, solange er geladen oder entladen wird.
--- falsch
Nur wenn sich die Spannung am Kondensator nicht ändert: Sonst sammelt sich seine Ladung auf dem Knoten an.
--- falsch
Ja, aber nur, wenn man den Kondensatorstrom weglässt: Er fließt in keinem Zweig, sondern endet auf der Platte.
:::
::::
