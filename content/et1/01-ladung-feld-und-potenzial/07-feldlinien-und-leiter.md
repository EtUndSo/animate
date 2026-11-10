---
title: Stufe 5: Feldlinien und Leiter
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1110700
summary: Feldlinien zeigen ein ganzes Feld auf einen Blick.
tags: Influenz, Feldlinie, Quellen, Senken, Abschirmung, homogen, Streufeld
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Feldlinien zeigen ein ganzes Feld auf einen Blick. Mit ihnen wird auch klar, was ein Metall mit einem Feld macht.
:::

**Die Idee.** Reiht man die Feldpfeile aneinander, entstehen Linien (Abb. [6](#abb-6)). Sichtbar macht man sie mit länglichen Körnchen in Öl: Das Feld verschiebt in jedem Korn die Ladungen ein wenig, und das Korn dreht sich in Feldrichtung. In Metall wandern die freien Elektronen, bis keine Kraft mehr auf sie wirkt. Diese Verschiebung heißt __Influenz__.

:::satz Satz 5.1 (Feldlinien ruhender Ladungen)
<span class="anker" id="satz-5-1"></span>

Eine __Feldlinie__ ist eine Kurve, deren Tangente in jedem Punkt die Richtung von $\vec E$ hat, ihre Dichte zeigt die Stärke des Felds. Es gilt:

<ol>

<li>

Feldlinien beginnen auf positiven Ladungen (__Quellen__) und enden auf negativen (__Senken__), nie im leeren Raum. Bei einer einzelnen Ladung läuft das andere Ende ins Unendliche.

</li>

<li>

Feldlinien schneiden sich nicht.

</li>

<li>

Auf der Oberfläche eines Leiters stehen sie senkrecht.

</li>

<li>

Im Inneren eines Leiters ist $\vec E=0$. Ein vom Leiter umschlossener ladungsfreier Hohlraum ist feldfrei (__Abschirmung__).

</li>

</ol>
:::

⁠**So liest man das:** Die Regeln 1 und 2 gelten im leeren Raum, die Regeln 3 und 4 sagen, was Metall am Feld ändert. Bei Quellen und Senken fließt nichts, die Wörter meinen Anfang und Ende der Linien. **Gültigkeit:** Alle Regeln setzen ruhende Ladungen voraus, Stufe [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10) zeigt Felder mit geschlossenen Linien.

:::abbildung et1/k1feldlinien 6
Berechnete Feldlinien. Oben: Bei ungleichnamigen Ladungen laufen sie von $+$ nach $-$, bei gleichnamigen weichen sie einander aus. Unten links: Zwischen zwei Platten verlaufen sie parallel und gleich dicht, nur am Rand wölben sie sich nach außen. Unten rechts: Metallrohr im Schnitt zwischen zwei Platten. Links sammeln sich Elektronen, rechts bleiben positive Ladungen zurück, innen ist $E=0$.
:::

:::herleitung Woher die Regeln kommen
⁠**Regel 2.** An einem Schnittpunkt hätte $\vec E$ zwei Richtungen, die Kraft auf eine Probeladung ist aber eindeutig.

⁠**Regel 4, Metall.** Gäbe es im Metall ein Feld, wanderten die freien Elektronen weiter. Ruhe ist erst erreicht, wenn die verschobenen Ladungen das äußere Feld im Inneren genau aufheben. Überschüssige Ladungen sitzen dabei auf der Oberfläche.

⁠**Regel 3.** Ein Feldanteil längs der Oberfläche würde die Elektronen dort entlangschieben. In Ruhe bleibt nur der senkrechte Anteil.

⁠**Regel 4, Hohlraum.** Das äußere Feld endet auf den influenzierten Ladungen der Außenseite. Ohne Ladung im Hohlraum müsste eine Linie dort von Wand zu Wand laufen. Eine Ladung könnte längs dieser Linie Energie gewinnen und durch das feldfreie Metall kostenlos zurückkehren. Das wäre Energie aus dem Nichts, was Stufe [6](arbeit-im-feld.html#stufe-6) ausschließt.
:::

::::beispiel
Im Plattenpaar sitzt die Ladung auf den Innenseiten der Platten, die Linien laufen parallel und gleich dicht von A nach B. Gleiche Dichte heißt: $\vec E$ ist überall gleich, das Feld ist __homogen__. Das gilt, solange $d$ klein gegen die Plattenbreite ist, nur am Rand wölbt sich ein schwächeres __Streufeld__ nach außen. Das Rohr in Abb. [6](#abb-6) zeigt Regel 3 und 4, an seinem Scheitel ist das Feld rund doppelt so stark wie ohne Rohr. Eine geschlossene Metallhülle schützt ihr Inneres, deshalb sitzt man im Auto bei Gewitter sicher.
::::

⁠**Kontrolle:** Regel 1 passt zum Coulomb-Gesetz. Von einer Ladung laufen $N$ Linien gleichmäßig in alle Richtungen und durchstoßen eine Kugel mit der Fläche $4\pi r^2$. Die Dichte $N/(4\pi r^2)$ fällt mit $1/r^2$, daher auch der Faktor $4\pi$ in $k=1/(4\pi\varepsilon_0)$. Umgekehrt ist die Abschirmung nur bei genau dem Exponenten 2 vollkommen. So entstanden die Messungen aus Stufe [3](die-kraft-zwischen-ladungen.html#stufe-3): Man suchte in einer geladenen Hohlkugel nach einem Restfeld.

:::frage Fliegt eine Ladung längs der Feldlinie?
Im Allgemeinen nicht. Die Feldlinie gibt die Richtung der Kraft an, also der Beschleunigung, nicht die der Geschwindigkeit. Nur bei geraden Linien und Start aus der Ruhe stimmen Bahn und Linie überein.
:::

:::aufgabe Aufgabe 5 ★ Abschirmung vorhersagen
<span class="anker" id="aufg-5"></span>

Antworte zuerst nur mit Feldlinien, ohne zu rechnen.

<ol class="al">

<li>

Eine Metallbox ohne eigene Ladung steht im Feld eines geladenen Stabs. Wie groß ist das Feld in der Box? Wo sitzen die influenzierten Ladungen?

</li>

<li>

In die Mitte einer isolierten, neutralen Metallhohlkugel wird eine Ladung $+Q$ gesetzt. Gibt es im Hohlraum ein Feld? Gibt es außerhalb ein Feld?

</li>

</ol>

:::loesung
(a) In der Box ist $E=0$. Die Influenzladungen sitzen außen: dem Stab gegenüber mit entgegengesetztem Vorzeichen, auf der abgewandten Seite mit gleichem. (b) Im Hohlraum gibt es ein Feld, denn von der Ladung gehen Linien aus. Sie enden auf der Innenwand, die sich durch Influenz mit $-Q$ belädt. Die Kugel ist neutral, außen sitzt also $+Q$, und außerhalb herrscht das Feld einer Ladung $+Q$. Abschirmung schützt nur das Innere vor äußeren Feldern.
:::
:::
