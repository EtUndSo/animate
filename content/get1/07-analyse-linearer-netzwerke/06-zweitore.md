---
title: Zweitore und ihre Parameter
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70600
summary: Wie man ein Bauteil mit Eingang und Ausgang als Black Box beschreibt, die nur Eingangs- und Ausgangsgrößen verknüpft – und warum es dafür vier gleichwertige Formen gibt, jede mit ihrem natürlichen Einsatzgebiet.
tags: Zweitor, Vierpol, Widerstandsform, Leitwertform, Hybridparameter, Kettenparameter
---

:::konzept
Viele Bauteile haben einen **Eingang** und einen **Ausgang** — ein Verstärker, ein Filter, ein Transistor, ein
Übertrager. Statt ihr Innenleben zu analysieren, behandelt man sie als Black Box mit zwei Anschlusspaaren
(Toren) und beschreibt nur, wie die Spannungen und Ströme am Eingang mit denen am Ausgang zusammenhängen. Das
ist ein **Zweitor**, und sein Verhalten steckt vollständig in vier Zahlen — einer 2×2-Matrix.
:::

**Worum es geht:** Das __Zweitor__ (auch __Vierpol__) ist die allgemeinste Beschreibung eines linearen
Übertragungsglieds. Wir klären, welche vier Größen es verknüpft, und lernen die vier gebräuchlichen
__Parameterformen__ kennen — die alle dasselbe Zweitor beschreiben, aber je nach Situation unterschiedlich
praktisch sind.

## Was ist ein Zweitor?

Ein __Zweitor__ hat vier Anschlüsse, die zu zwei Toren zusammengefasst sind: dem __Eingangstor__ mit der
Spannung $U_1$ und dem Strom $I_1$, und dem __Ausgangstor__ mit $U_2$ und $I_2$. Weil das Innere linear ist,
sind diese vier Größen durch **zwei** lineare Gleichungen verknüpft. Man darf also zwei davon frei wählen (die
„Ursachen") und die anderen beiden daraus berechnen (die „Wirkungen").

Welche zwei man zu unabhängigen Variablen macht, ist Geschmackssache — und genau diese Wahl führt auf die
verschiedenen Parameterformen.

:::grafik
Eine Box mit der Beschriftung „Zweitor". Links das Eingangstor mit Spannungspfeil $U_1$ und Strompfeil $I_1$
(hinein), rechts das Ausgangstor mit $U_2$ und $I_2$. Darunter „4 Größen, 2 Gleichungen".
:::

## Widerstandsform (Z-Parameter)

Wählt man die beiden **Ströme** als unabhängig, drückt man die Spannungen durch sie aus — die
__Widerstandsform__:

$$U_1 = Z_{11} I_1 + Z_{12} I_2, \qquad U_2 = Z_{21} I_1 + Z_{22} I_2.$$

Alle vier __Z-Parameter__ sind __Widerstände__ (Impedanzen). Man misst sie im **Leerlauf** des jeweils anderen
Tors (Strom null), weshalb sie auch Leerlauf-Impedanzparameter heißen. $Z_{11}$ ist zum Beispiel der
Eingangswiderstand bei offenem Ausgang. Diese Form ist natürlich, wenn man Zweitore **in Reihe** schaltet — dann
addieren sich die Z-Matrizen.

## Leitwertform (Y-Parameter)

Spiegelbildlich: Wählt man die beiden **Spannungen** als unabhängig, bekommt man die __Leitwertform__:

$$I_1 = Y_{11} U_1 + Y_{12} U_2, \qquad I_2 = Y_{21} U_1 + Y_{22} U_2.$$

Die __Y-Parameter__ sind __Leitwerte__ (Admittanzen), gemessen im **Kurzschluss** des anderen Tors (Spannung
null). Diese Form passt, wenn man Zweitore **parallel** schaltet — dann addieren sich die Y-Matrizen. Z- und
Y-Matrix beschreiben dasselbe Zweitor und sind zueinander **invers**.

:::grafik
Zwei kleine Messskizzen: links die Z-Bestimmung mit offenem zweiten Tor (Leerlauf, $I=0$), rechts die
Y-Bestimmung mit kurzgeschlossenem zweiten Tor ($U=0$). Beschriftung „Z: Leerlauf-Widerstände" und „Y:
Kurzschluss-Leitwerte".
:::

## Hybrid- und Kettenform

Zwei weitere Kombinationen sind besonders nützlich:

Die __Hybridform__ (__H-Parameter__) mischt die Größen: Eingangsstrom und Ausgangsspannung sind unabhängig.

$$U_1 = h_{11} I_1 + h_{12} U_2, \qquad I_2 = h_{21} I_1 + h_{22} U_2.$$

Hier ist $h_{11}$ ein Widerstand, $h_{22}$ ein Leitwert, und $h_{12}, h_{21}$ sind dimensionslos — daher
„hybrid". Das ist die klassische Form für den **Transistor**, wo $h_{21}$ gerade die Stromverstärkung ist.

Die __Kettenform__ (__A-__ oder __ABCD-Parameter__) drückt die Eingangsgrößen durch die Ausgangsgrößen aus:

$$U_1 = A_{11} U_2 + A_{12}\,(-I_2), \qquad I_1 = A_{21} U_2 + A_{22}\,(-I_2).$$

Ihr großer Vorteil: Schaltet man Zweitore **hintereinander** (in Kette), so ist die Gesamt-Kettenmatrix einfach
das **Produkt** der einzelnen Matrizen. Eine Reihe von Übertragungsgliedern rechnet man damit durch bloße
Matrizenmultiplikation durch.

| Form | unabhängig | Parameter sind | natürlich bei |
|---|---|---|---|
| Widerstandsform (Z) | $I_1, I_2$ | Widerstände (Leerlauf) | Reihenschaltung |
| Leitwertform (Y) | $U_1, U_2$ | Leitwerte (Kurzschluss) | Parallelschaltung |
| Hybridform (H) | $I_1, U_2$ | gemischt | Transistoren |
| Kettenform (A) | $U_2, I_2$ | gemischt | Kettenschaltung |

:::grafik
Zwei hintereinandergeschaltete Zweitor-Boxen (Ausgang des ersten = Eingang des zweiten) mit der Notiz
„Gesamt-Kettenmatrix $= A^{(1)} \cdot A^{(2)}$" — die Kettenform macht die Reihenfolge zur
Matrizenmultiplikation.
:::

## Alle Formen sind gleichwertig

Alle vier Parametersätze beschreiben **dasselbe** Zweitor und lassen sich ineinander umrechnen. Man wählt immer
die Form, die zur Aufgabe passt: Z für in Reihe liegende, Y für parallele, H für Transistorschaltungen, A für
Ketten. Die eigentliche Information — wie das Bauteil Eingang und Ausgang verknüpft — ist in jeder Form dieselbe,
nur anders verpackt.

:::kern
Ein __Zweitor__ (Vierpol) verknüpft Eingangstor ($U_1, I_1$) und Ausgangstor ($U_2, I_2$) über zwei lineare
Gleichungen, also eine 2×2-Matrix. Je nachdem, welche zwei Größen unabhängig sind, ergeben sich vier
gleichwertige Formen: __Widerstandsform__ Z (Leerlauf-Widerstände, Reihenschaltung), __Leitwertform__ Y
(Kurzschluss-Leitwerte, Parallelschaltung, invers zu Z), __Hybridform__ H (gemischt, Transistoren) und
__Kettenform__ A (gemischt, Kettenschaltung → Matrizen multiplizieren). Alle beschreiben dasselbe Zweitor und
sind umrechenbar.
:::

Damit ist die Werkzeugkiste der Netzwerkanalyse komplett. Die nächsten Kapitel systematisieren das Lösen großer
Netze zu festen Rechenschemata: dem __Maschenstromverfahren__ und dem __Knotenpotentialverfahren__.

:::quiz
F: Was beschreibt ein Zweitor, und was lässt es bewusst weg?
A: Es beschreibt nur, wie die Spannungen und Ströme am Eingangstor mit denen am Ausgangstor zusammenhängen — als Black Box. Das innere Schaltungsdetail bleibt unberücksichtigt; es zählt allein das Klemmenverhalten.
F: Warum genügen zwei Gleichungen (eine 2×2-Matrix), um ein lineares Zweitor zu beschreiben?
A: Es gibt vier Torgrößen ($U_1,I_1,U_2,I_2$), und weil das Innere linear ist, verknüpfen sie zwei lineare Gleichungen. Damit darf man zwei frei wählen und die anderen beiden daraus berechnen.
F: Wodurch unterscheiden sich die vier Parameterformen überhaupt?
A: Durch die Wahl, welche zwei Torgrößen man als unabhängig (die „Ursachen") ansetzt. Jede Wahl führt auf eine andere, aber gleichwertige Matrixdarstellung desselben Zweitors.
F: Warum misst man Z-Parameter im Leerlauf und Y-Parameter im Kurzschluss?
A: Bei den Z-Parametern sind die Ströme unabhängig, also setzt man den jeweils anderen Strom null — das ist Leerlauf. Bei den Y-Parametern sind die Spannungen unabhängig, man setzt die andere null — das ist Kurzschluss.
F: In welchem Verhältnis stehen Z- und Y-Matrix zueinander?
A: Sie beschreiben dasselbe Zweitor und sind zueinander invers. Die eine entsteht aus der anderen durch Matrixinversion.
F: Warum ist die Z-Form natürlich für Reihen-, die Y-Form für Parallelschaltung?
A: Bei Reihenschaltung addieren sich die Tornspannungen bei gleichen Strömen, sodass sich die Z-Matrizen addieren; bei Parallelschaltung addieren sich die Ströme bei gleichen Spannungen, sodass sich die Y-Matrizen addieren. Jede Form passt zur Verschaltung, bei der sich ihre Matrizen einfach summieren.
F: Warum heißen die H-Parameter „hybrid"?
A: Weil sie gemischte unabhängige Größen (Eingangsstrom und Ausgangsspannung) verwenden, sind ihre Parameter unterschiedlicher Art: $h_{11}$ ein Widerstand, $h_{22}$ ein Leitwert, $h_{12},h_{21}$ dimensionslos. Diese Mischung gibt der Form ihren Namen.
F: Warum ist die Hybridform die klassische Wahl für Transistoren?
A: Beim Transistor sind Eingangsstrom und Ausgangsspannung die natürlichen Steuergrößen, und $h_{21}$ ist gerade die Stromverstärkung. Die H-Parameter bilden das Verstärkerverhalten damit direkt ab.
F: Welchen entscheidenden Vorteil hat die Kettenform bei hintereinandergeschalteten Zweitoren?
A: Die Gesamt-Kettenmatrix ist einfach das Produkt der Einzelmatrizen. Eine Reihe von Übertragungsgliedern rechnet man dadurch durch bloße Matrizenmultiplikation durch.
F: Enthält jede Parameterform dieselbe Information über das Zweitor?
A: Ja — alle vier beschreiben exakt dasselbe Zweitor und lassen sich ineinander umrechnen. Sie verpacken die Verknüpfung von Ein- und Ausgang nur unterschiedlich; man wählt die zur Aufgabe passende Form.
:::
