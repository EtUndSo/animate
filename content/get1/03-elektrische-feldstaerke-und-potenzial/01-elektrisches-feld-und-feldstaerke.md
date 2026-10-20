---
title: Das elektrische Feld und die Feldstärke
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Elektrische Feldstärke und Potenzial
order: 30100
summary: Wie Ladungen sich über Entfernung beeinflussen, warum man dafür das elektrische Feld einführt und wie die Feldstärke als Kraft pro Ladung genau das messbar macht — bis zum homogenen Feld im Plattenkondensator.
tags: elektrisches Feld, Feldstärke, Coulomb, Probeladung, Feldlinien, Plattenkondensator, homogenes Feld
---

:::konzept
Zwei geladene Kugeln ziehen sich an oder stoßen sich ab, ohne sich zu berühren. Wie „weiß" die eine Ladung von
der anderen? Die Antwort der Physik: Jede Ladung verändert den Raum um sich herum — sie baut ein **elektrisches
Feld** auf. Eine zweite Ladung spürt dann nicht die erste direkt, sondern das Feld an ihrem eigenen Ort. Das
Feld ist der unsichtbare Vermittler der Kraft.
:::

**Worum es geht:** Im vorigen Kapitel ging es um Ladung als Baustein. Jetzt klären wir, *wie* Ladungen
aufeinander wirken — und bauen daraus den zentralen Begriff der Elektrostatik auf: die __elektrische
Feldstärke__. Sie ist die Grundlage für Spannung, Kondensator und letztlich jede Schaltung.

## Die Kraft zwischen zwei Ladungen

Alles beginnt mit einer Beobachtung: Zwei __Punktladungen__ $q_1$ und $q_2$ üben eine Kraft aufeinander aus.
Gleichnamige stoßen sich ab, ungleichnamige ziehen sich an. Wie groß diese Kraft ist, beschreibt das
__Coulombsche Gesetz__:

$$F = \frac{1}{4\pi\varepsilon_0} \cdot \frac{q_1 \cdot q_2}{r^2}.$$

Die Bestandteile:

- __$F$__: der Betrag der __Coulombkraft__ zwischen den Ladungen, in Newton.
- __$q_1, q_2$__: die beiden __Ladungen__, in Coulomb.
- __$r$__: der __Abstand__ ihrer Mittelpunkte, in Metern.
- __$\varepsilon_0$__: die __elektrische Feldkonstante__ (auch Permittivität des Vakuums),
  $\varepsilon_0 \approx 8{,}854 \cdot 10^{-12}\,\tfrac{\text{A}\cdot\text{s}}{\text{V}\cdot\text{m}}$ — eine
  Naturkonstante, die festlegt, wie „stark" elektrische Kräfte im Vakuum überhaupt sind.

Zwei Dinge stecken in dieser Formel. Erstens wächst die Kraft mit dem Produkt der Ladungen — doppelte Ladung,
doppelte Kraft. Zweitens fällt sie mit dem **Quadrat** des Abstands: doppelter Abstand bedeutet nur noch ein
Viertel der Kraft. Das ist dasselbe $1/r^2$-Gesetz wie bei der Gravitation, nur viele Größenordnungen stärker.

:::grafik
Zwei Ladungen im Abstand $r$. Oben gleichnamige ($+/+$) mit Kraftpfeilen, die voneinander weg zeigen; unten
ungleichnamige ($+/-$) mit Pfeilen, die aufeinander zu zeigen. Die Pfeillängen an beiden Ladungen gleich (actio
= reactio).
:::

## Vom Kraftgesetz zum Feld: die Feldstärke

Das Coulombsche Gesetz hat einen Schönheitsfehler: Die Kraft hängt immer von **beiden** Ladungen ab. Will man
den Einfluss *einer* Ladung auf ihre Umgebung beschreiben — unabhängig davon, was man später hineinstellt —,
braucht man eine Größe, die nur zur felderzeugenden Ladung gehört. Das leistet die __elektrische Feldstärke__.

Die Idee: Man bringt eine kleine __Probeladung__ $q$ an einen Punkt, misst die Kraft $F$ auf sie und teilt
durch $q$. Was übrig bleibt, ist unabhängig von der Probeladung und beschreibt allein den Zustand des Raumes an
diesem Punkt:

$$\vec{E} = \frac{\vec{F}}{q}.$$

- __$\vec{E}$__: die __elektrische Feldstärke__ am betrachteten Punkt — ein Vektor, der in die Kraftrichtung
  auf eine positive Ladung zeigt.
- __$\vec{F}$__: die __Kraft__ auf die Probeladung an diesem Punkt.
- __$q$__: die __Probeladung__ selbst (gedanklich so klein, dass sie das zu messende Feld nicht stört).

Die Einheit folgt direkt aus der Definition: Kraft durch Ladung, also $\tfrac{\text{N}}{\text{C}}$. Weil sich
das später als gleichwertig zu $\tfrac{\text{V}}{\text{m}}$ herausstellt (Volt pro Meter), ist das die in der
Elektrotechnik übliche Schreibweise ([Elektronik-Kompendium](https://www.elektronik-kompendium.de/sites/formeln/elektrische-feldstaerke)).

**Warum durch die Probeladung teilen?** Weil die Kraft nach Coulomb proportional zur Probeladung ist: doppelte
Probeladung, doppelte Kraft. Der Quotient $F/q$ kürzt diese Abhängigkeit genau heraus — übrig bleibt eine
Eigenschaft des Raumes, nicht des Testkörpers. Man kann das Feld also einmal bestimmen und danach für *jede*
beliebige Ladung sofort die Kraft angeben über $\vec{F} = q\cdot\vec{E}$.

**Anders betrachtet.** Das Feld ist wie eine Landkarte von Strömungen in einem Fluss: An jedem Punkt ist
eingetragen, in welche Richtung und wie stark es zieht. Setzt man ein Boot (die Probeladung) hinein, folgt die
Kraft darauf aus der Strömung am jeweiligen Ort — die Karte selbst gilt aber schon, bevor irgendein Boot da ist.

:::grafik
Eine große Ladung $Q$ und an einem Punkt daneben eine kleine Probeladung $q$. Eingezeichnet der Kraftpfeil
$\vec{F}$ auf $q$ und, halb transparent darunter, der Feldstärkepfeil $\vec{E}$ in gleicher Richtung — mit dem
Hinweis $\vec{E} = \vec{F}/q$.
:::

## Feldlinien und das Feld einer Punktladung

Ein Feld ist unsichtbar, lässt sich aber durch __Feldlinien__ anschaulich machen. Vereinbarung: Feldlinien
zeigen in Richtung der Kraft auf eine **positive** Probeladung, starten bei positiven und enden bei negativen
Ladungen, und wo sie dichter liegen, ist das Feld stärker.

Für eine einzelne Punktladung $Q$ ergibt sich die Feldstärke, indem man die Coulombkraft durch die Probeladung
teilt:

$$E = \frac{1}{4\pi\varepsilon_0} \cdot \frac{Q}{r^2}.$$

Die Feldlinien laufen hier radial nach außen (bei $+Q$) oder nach innen (bei $-Q$), wie die Stacheln eines
Igels. Dass das Feld mit $1/r^2$ schwächer wird, sieht man direkt an den Linien: Weiter außen verteilen sie
sich auf eine größere Fläche, liegen also dünner — das Feld nimmt ab.

:::grafik
Links eine positive Punktladung mit radial nach außen zeigenden Feldlinien, rechts eine negative mit nach
innen zeigenden. An beiden erkennbar: außen größerer Linienabstand = schwächeres Feld.
:::

## Das homogene Feld im Plattenkondensator

In der Praxis ist ein Feld besonders wichtig, bei dem die Feldstärke überall gleich groß und gleich gerichtet
ist — ein __homogenes Feld__. Es entsteht zwischen zwei parallelen, entgegengesetzt geladenen Platten, dem
__Plattenkondensator__. Zwischen den Platten verlaufen die Feldlinien als gleichmäßige, parallele Geraden von
der positiven zur negativen Platte.

Hier hängt die Feldstärke besonders einfach mit der angelegten __Spannung__ $U$ und dem Plattenabstand $d$
zusammen:

$$E = \frac{U}{d}.$$

- __$E$__: die __Feldstärke__ im Plattenzwischenraum (konstant, daher reicht ein Zahlenwert).
- __$U$__: die __Spannung__ zwischen den Platten, in Volt.
- __$d$__: der __Plattenabstand__, in Metern.

An dieser Beziehung liest man die Einheit $\tfrac{\text{V}}{\text{m}}$ unmittelbar ab — genau die Einheit, die
oben schon als gleichwertig zu $\tfrac{\text{N}}{\text{C}}$ angekündigt wurde. Praktisch heißt das: Je kleiner
der Abstand bei gleicher Spannung, desto stärker das Feld. Deshalb erreichen schon kleine Spannungen in einem
engen Spalt sehr hohe Feldstärken — der Grund, warum Luft bei genügend kleinem Abstand durchschlägt (ein Funke).

:::grafik
Ein Plattenkondensator: zwei waagerechte Platten, oben $+$, unten $-$, dazwischen gleichmäßig dichte, parallele
senkrechte Feldlinien. Beschriftung des Abstands $d$ und der Spannung $U$, dazu die Relation $E = U/d$. Am Rand
leicht nach außen gebogene Linien (Randfeld) als ehrlicher Hinweis, dass „homogen" eine Idealisierung des
Innenraums ist.
:::

:::kern
Ladungen wirken über das __elektrische Feld__ aufeinander. Die Kraft zweier Punktladungen folgt dem
__Coulombschen Gesetz__ $F = \tfrac{1}{4\pi\varepsilon_0}\tfrac{q_1 q_2}{r^2}$ (mit $1/r^2$-Abstandsgesetz).
Die __Feldstärke__ $\vec{E} = \vec{F}/q$ beschreibt das Feld unabhängig von der Probeladung; aus ihr folgt
jederzeit die Kraft $\vec{F} = q\vec{E}$. Einheit: $\tfrac{\text{N}}{\text{C}} = \tfrac{\text{V}}{\text{m}}$.
Im __Plattenkondensator__ ist das Feld __homogen__ und besonders einfach: $E = U/d$.
:::

Bisher ging es um die Kraft. Als Nächstes die Energie: Was kostet es, eine Ladung im Feld zu verschieben? Daraus
entstehen die Begriffe __Arbeit__, __Potenzial__ und schließlich die __Spannung__.

:::quiz
F: Warum führt man überhaupt den Begriff „Feld" ein, statt nur mit der Coulombkraft zu rechnen?
A: Die Coulombkraft hängt immer von beiden Ladungen ab. Das Feld beschreibt den Einfluss *einer* Ladung auf den Raum unabhängig davon, was man später hineinstellt — der unsichtbare Vermittler, den eine zweite Ladung an ihrem Ort spürt.
F: Warum fällt die Coulombkraft mit $1/r^2$ und nicht etwa mit $1/r$?
A: Das Feld einer Punktladung verteilt sich gleichmäßig auf Kugelschalen, deren Fläche mit $r^2$ wächst. Dieselbe „Menge Feld" auf immer größerer Fläche bedeutet eine Abnahme proportional zu $1/r^2$.
F: Was bedeutet die elektrische Feldkonstante $\varepsilon_0$ physikalisch?
A: Sie legt fest, wie stark elektrische Kräfte im Vakuum überhaupt sind — ein Umrechnungsfaktor zwischen Ladung/Abstand und Kraft. Ihr fester Zahlenwert eicht das Coulombsche Gesetz an die beobachtete Natur.
F: Warum teilt man bei der Definition der Feldstärke durch die Probeladung?
A: Die Kraft ist proportional zur Probeladung, also kürzt der Quotient $F/q$ diese Abhängigkeit genau heraus. Übrig bleibt eine Eigenschaft des Raumes allein, die man einmal bestimmt und danach für jede Ladung über $\vec F=q\vec E$ nutzt.
F: Warum muss die Probeladung gedanklich „klein" sein?
A: Eine reale Ladung erzeugt selbst ein Feld und würde die Quellladungen verschieben oder das zu messende Feld verzerren. Nur eine beliebig kleine Probeladung tastet das Feld ab, ohne es zu stören.
F: Warum ist $\vec E$ ein Vektor, und wie ist seine Richtung festgelegt?
A: Die Kraft hat eine Richtung, und da $\vec E=\vec F/q$ ist, erbt das Feld diese Richtung. Per Konvention zeigt $\vec E$ in die Kraftrichtung auf eine *positive* Ladung.
F: Woran erkennt man an Feldlinien, wo das Feld stärker ist?
A: An der Liniendichte: Wo die Feldlinien enger beieinanderliegen, ist das Feld stärker. Bei einer Punktladung laufen sie nach außen auseinander, liegen dünner und zeigen so die $1/r^2$-Abnahme.
F: Warum starten Feldlinien bei positiven und enden bei negativen Ladungen?
A: Sie folgen der Kraftrichtung auf eine positive Probeladung, die von positiven Ladungen weg- und zu negativen hingezogen wird. Daraus ergibt sich die Konvention Quelle (+) → Senke (−).
F: Warum ist das Feld im Plattenkondensator homogen, am Rand aber nicht?
A: Zwischen großen, parallelen Platten verlaufen die Feldlinien gleichmäßig und parallel, Betrag und Richtung sind überall gleich. Am Rand „quellen" sie nach außen (Randfeld), weshalb „homogen" streng nur für den Innenraum als Idealisierung gilt.
F: Warum erzeugt eine kleine Spannung in einem engen Spalt ein sehr starkes Feld?
A: Wegen $E=U/d$ wächst die Feldstärke, je kleiner der Abstand bei gleicher Spannung. In sehr engen Spalten werden dadurch so hohe Feldstärken erreicht, dass selbst Luft durchschlägt (Funke).
:::
