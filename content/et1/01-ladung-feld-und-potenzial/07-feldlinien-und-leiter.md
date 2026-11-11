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

::::lernkarten
:::karte begriff Feldlinie
Was ist eine Feldlinie?
---
Eine Kurve, deren Tangente in jedem Punkt die Richtung von $\vec E$ hat. Die Dichte der Feldlinien zeigt die Stärke des Felds.
--- falsch
Die Bahn, auf der eine Ladung durch das Feld fliegt. Die Dichte der Feldlinien zeigt, wie viele Ladungen dort unterwegs sind.
--- falsch
Eine Kurve, die in jedem Punkt senkrecht zur Richtung von $\vec E$ verläuft. Die Dichte der Feldlinien zeigt die Stärke des Felds.
--- falsch
Eine Kurve, deren Tangente in jedem Punkt die Richtung von $\vec E$ hat. Die Länge einer Feldlinie zeigt die Stärke des Felds.
:::
:::karte begriff Quellen und Senken
Was sind Quellen und Senken der Feldlinien?
---
Quellen sind die positiven Ladungen, auf denen Feldlinien beginnen, Senken die negativen, auf denen sie enden. Dabei fließt nichts; die Wörter meinen Anfang und Ende der Linien.
--- falsch
Quellen sind die negativen Ladungen, auf denen Feldlinien beginnen, Senken die positiven, auf denen sie enden. Dabei fließt nichts; die Wörter meinen Anfang und Ende der Linien.
--- falsch
Quellen sind Orte, aus denen Ladung ins Feld hinausfließt, Senken Orte, an denen sie wieder abfließt. Die Feldlinien zeigen, wohin die Ladung dabei strömt.
--- falsch
Quellen und Senken sind Punkte im leeren Raum, an denen sich Felder aufheben. Dort beginnen und enden Feldlinien, ohne dass eine Ladung nötig ist.
:::
:::karte begriff Influenz
Was ist Influenz?
---
Die Verschiebung der freien Elektronen in einem Metall durch ein äußeres Feld. Sie wandern, bis keine Kraft mehr auf sie wirkt.
--- falsch
Die Verschiebung der Protonen in einem Metall durch ein äußeres Feld. Sie wandern, bis keine Kraft mehr auf sie wirkt.
--- falsch
Das Aufladen eines Metalls durch Berührung mit einem geladenen Körper. Dabei gehen Elektronen von einem Körper auf den anderen über.
--- falsch
Die Verschiebung der Elektronen in einem Isolator durch ein äußeres Feld. Sie wandern durch den ganzen Körper bis an seine Oberfläche.
:::
:::karte begriff homogenes Feld
Wann heißt ein Feld homogen?
---
Wenn $\vec E$ überall nach Betrag und Richtung gleich ist; die Feldlinien verlaufen parallel und gleich dicht. Zwischen zwei Platten gilt das, solange ihr Abstand klein gegen die Plattenbreite ist.
--- falsch
Wenn $\vec E$ überall dieselbe Richtung hat, der Betrag darf sich längs der Linien ändern. Zwischen zwei Platten gilt das, solange ihr Abstand klein gegen die Plattenbreite ist.
--- falsch
Wenn $\vec E$ überall nach Betrag und Richtung gleich ist; die Feldlinien verlaufen parallel und gleich dicht. Zwischen zwei Platten gilt das, solange ihr Abstand groß gegen die Plattenbreite ist.
--- falsch
Wenn die Feldlinien von einer einzigen Ladung ausgehen und gleichmäßig in alle Richtungen laufen, sodass das Feld in jeder Richtung gleich aussieht.
:::
:::karte begriff Abschirmung
Was versteht man unter Abschirmung?
---
Die Feldfreiheit eines ladungsfreien Hohlraums, den ein Leiter umschließt. Das äußere Feld endet auf den influenzierten Ladungen der Außenseite und dringt nicht ein.
--- falsch
Die Feldfreiheit der Außenseite eines Leiters. Feldlinien erreichen die Oberfläche eines Metalls nicht, sie biegen vorher ab und laufen an ihm vorbei.
--- falsch
Die Feldfreiheit im Inneren jeder Metallhülle, auch wenn im Hohlraum selbst eine Ladung sitzt. Die Hülle hält jedes Feld vom Inneren fern, gleich wo es entsteht.
--- falsch
Die Schwächung eines Felds durch eine Schicht aus Glas oder Gummi. Ihre gebundenen Elektronen halten die Feldlinien fest und lassen sie nicht hindurch.
:::
:::karte zusammenhang Feldlinien schneiden sich nicht
Warum schneiden sich Feldlinien nicht?
---
Weil $\vec E$ an einem Schnittpunkt zwei Richtungen hätte. Die Kraft auf eine Probeladung an diesem Ort ist aber eindeutig.
--- falsch
Weil sich Feldlinien gegenseitig abstoßen, wie zwei gleichnamige Ladungen. Kommen sie sich nahe, weichen sie einander aus.
--- falsch
Weil das Feld an einem Schnittpunkt doppelt so stark wäre. Die Luft würde dort durchschlagen, und die Linien würden enden.
--- falsch
Weil jede Feldlinie zu genau einer Ladung gehört. Linien verschiedener Ladungen bleiben getrennt und überlagern sich nicht.
:::
:::karte zusammenhang Kein Feld im Metall
Warum ist im Inneren eines ruhenden Metallkörpers $\vec E=0$?
---
Weil die freien Elektronen weiterwandern, solange es dort ein Feld gibt. Ruhe herrscht erst, wenn die verschobenen Ladungen das äußere Feld im Inneren genau aufheben.
--- falsch
Weil das Metall die Energie des Felds aufnimmt: Die freien Elektronen wandeln sie in Wärme um, und das Feld klingt im Inneren nach wenigen Atomlagen vollständig ab.
--- falsch
Weil sich im Metall die Protonen verschieben, bis ihr Feld das äußere aufhebt. Die Elektronen bleiben dabei fest an ihren Atomen.
--- falsch
Weil ein schwaches äußeres Feld nicht in das dichte Metall eindringen kann; die Atome stehen dafür zu eng. Ein ausreichend starkes Feld würde das Metall dagegen durchdringen.
:::
:::karte zusammenhang Senkrecht auf Leitern
Warum stehen Feldlinien senkrecht auf der Oberfläche eines Leiters?
---
Weil ein Feldanteil längs der Oberfläche die freien Elektronen dort entlangschieben würde. In Ruhe bleibt nur der senkrechte Anteil.
--- falsch
Weil Feldlinien immer den kürzesten Weg zum Metall nehmen, und der kürzeste Weg zu einer Fläche ist der senkrechte.
--- falsch
Weil die Oberfläche die Feldlinien wie ein Spiegel zurückwirft, sodass hinlaufende und zurücklaufende Linie zusammenfallen.
--- falsch
Weil die Elektronen an der Oberfläche festsitzen. Sie können nur senkrecht zur Oberfläche ausweichen, nicht an ihr entlang, und lenken das Feld so um.
:::
:::karte zusammenhang Bahn und Feldlinie
Warum folgt die Bahn einer Ladung im Allgemeinen nicht der Feldlinie?
---
Weil die Feldlinie die Richtung der Kraft angibt, also der Beschleunigung, nicht die der Geschwindigkeit. Nur bei geraden Linien und Start aus der Ruhe stimmen Bahn und Linie überein.
--- falsch
Weil die Kraft auf eine Ladung senkrecht zur Feldlinie wirkt. Die Bahn biegt deshalb immer quer zur Linie ab; nur eine ruhende Ladung bleibt auf ihrer Linie, weil sie sich gar nicht bewegt.
--- falsch
Weil die Ladung ihr eigenes Feld mitnimmt. Es schiebt die Feldlinie beim Vorbeifliegen von der Bahn weg, sodass Bahn und Linie auseinanderlaufen.
--- falsch
Weil Feldlinien nur positive Ladungen führen. Negative Ladungen weichen den Linien aus und laufen quer zu ihnen, positive folgen ihnen dagegen genau.
:::
:::karte zusammenhang Feldliniendichte
Warum fällt die Dichte der Feldlinien einer Punktladung wie ihr Feld mit $1/r^2$?
---
Weil $N$ Linien gleichmäßig in alle Richtungen laufen und eine Kugel der Fläche $4\pi r^2$ durchstoßen: Ihre Dichte $N/(4\pi r^2)$ fällt mit $1/r^2$. Daher auch der Faktor $4\pi$ in $k=1/(4\pi\varepsilon_0)$.
--- falsch
Weil die $N$ Linien der Ladung in der Ebene einen Kreis mit dem Umfang $2\pi r$ durchstoßen. Ihre Dichte $N/(2\pi r)$ fällt mit $1/r^2$; daher auch der Faktor $2\pi$ in der Konstante $k$ des Coulomb-Gesetzes.
--- falsch
Weil die Feldlinien mit wachsendem Abstand kürzer werden. Ihre Länge fällt mit $1/r^2$, und die Länge einer Linie gibt die Stärke des Felds an ihrem Ort an.
--- falsch
Weil mit wachsendem Abstand immer mehr Linien im leeren Raum enden. Die Zahl der Linien, die übrig bleiben, fällt mit $1/r^2$, und mit ihr die Dichte.
:::
::::
