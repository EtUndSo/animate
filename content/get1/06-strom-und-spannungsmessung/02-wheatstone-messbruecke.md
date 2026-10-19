---
title: Die Wheatstonesche Messbrücke
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Strom- und Spannungsmessung
order: 60200
summary: Wie man mit zwei Spannungsteilern und einem Nullabgleich einen unbekannten Widerstand sehr genau bestimmt – und warum die Messung gerade dann besonders zuverlässig ist, wenn das Messgerät nichts mehr anzeigt.
tags: Wheatstone, Messbrücke, Abgleichbedingung, Nullmethode, Widerstandsmessung
---

:::konzept
Die genaueste Art, einen Widerstand zu messen, ist nicht, einen Zeiger abzulesen, sondern ihn mit einem
bekannten Widerstand zu **vergleichen** — so wie eine Balkenwaage eine Masse nicht „abliest", sondern mit
Gewichten ins Gleichgewicht bringt. Die **Wheatstonesche Messbrücke** macht genau das: Zwei Spannungsteiler
liegen nebeneinander, dazwischen ein empfindliches Messgerät. Man verstellt einen Widerstand, bis das Gerät
**null** anzeigt — dann teilen beide Teiler im gleichen Verhältnis, und der unbekannte Widerstand ist bestimmt.
:::

**Worum es geht:** Mit einem normalen Messgerät begrenzen Innenwiderstand und Skalengenauigkeit die Präzision.
Die __Messbrücke__ umgeht das mit einem Trick — der __Nullmethode__. Wir sehen ihren Aufbau, leiten die
__Abgleichbedingung__ her und verstehen, warum sie so genau ist.

## Aufbau: zwei Spannungsteiler nebeneinander

Die Brücke besteht aus vier Widerständen $R_1, R_2, R_3, R_4$, die als zwei __Spannungsteiler__ an derselben
Quelle $U$ liegen. Der linke Teiler ($R_1$ über $R_2$) hat einen Mittelabgriff — nennen wir ihn Punkt A —, der
rechte ($R_3$ über $R_4$) den Punkt B. Zwischen A und B, in der __Brückendiagonalen__, sitzt ein empfindliches
Strommessgerät (ein __Galvanometer__).

Jeder Teiler legt an seinem Mittelpunkt ein Potenzial fest. Nach der Spannungsteilerregel ist (gemessen gegen
denselben Bezugspunkt)

$$U_\text{A} = U \cdot \frac{R_2}{R_1 + R_2}, \qquad U_\text{B} = U \cdot \frac{R_4}{R_3 + R_4}.$$

Das Galvanometer in der Diagonalen misst die Differenz dieser beiden Potenziale — und genau die bringt man zum
Verschwinden.

:::grafik
Die klassische Brücke als Raute: oben die Quelle $U$, links der Teiler $R_1/R_2$ mit Mittelpunkt A, rechts
$R_3/R_4$ mit Mittelpunkt B, und in der waagerechten Diagonalen zwischen A und B das Galvanometer (Kreis mit „G").
:::

## Die Abgleichbedingung

Die Brücke heißt __abgeglichen__, wenn durch die Diagonale **kein Strom** fließt. Das ist genau dann der Fall,
wenn die beiden Mittelpunkte auf **demselben Potenzial** liegen, also $U_\text{A} = U_\text{B}$. Setzt man die
beiden Teilerausdrücke gleich,

$$\frac{R_2}{R_1 + R_2} = \frac{R_4}{R_3 + R_4},$$

und multipliziert über Kreuz, fällt die Quellenspannung $U$ heraus und es bleibt die __Abgleichbedingung__:

$$\frac{R_1}{R_2} = \frac{R_3}{R_4} \qquad\Longleftrightarrow\qquad R_1 \cdot R_4 = R_2 \cdot R_3.$$

- __$R_1, R_2, R_3, R_4$__: die vier __Brückenwiderstände__.

Ist einer davon der gesuchte Widerstand — nennen wir ihn $R_x = R_1$ — und sind die drei anderen bekannt (einer
davon einstellbar), so liest man ihn direkt aus der abgeglichenen Brücke ab:

$$R_x = R_2 \cdot \frac{R_3}{R_4}.$$

Man verstellt also einen bekannten Widerstand so lange, bis das Galvanometer null zeigt, und rechnet $R_x$ aus
dem erreichten Verhältnis aus.

:::grafik
Zwei Zustände nebeneinander: links die unabgeglichene Brücke (Galvanometer-Zeiger schlägt aus, $U_\text{A} \ne
U_\text{B}$), rechts die abgeglichene (Zeiger auf null, $U_\text{A} = U_\text{B}$), darunter die Bedingung
$R_1/R_2 = R_3/R_4$.
:::

## Warum so genau: die Nullmethode

Der eigentliche Clou ist, **was** am Ende gemessen wird — nämlich nichts. Im Abgleich fließt durch das
Galvanometer kein Strom, und das hat zwei schöne Folgen.

Erstens fällt die __Quellenspannung__ $U$ aus der Bedingung heraus (sie kürzt sich beim Gleichsetzen). Die
Messung ist also **unabhängig** davon, wie stabil oder genau bekannt die Speisespannung ist — Schwankungen der
Quelle stören nicht.

Zweitens spielt der __Innenwiderstand__ des Galvanometers keine Rolle: Wo kein Strom fließt, fällt an ihm auch
keine Spannung ab, egal wie groß er ist. Man muss das Messgerät also nicht kalibrieren, sondern nur erkennen,
**ob** Strom fließt oder nicht. Deshalb ist eine solche __Nullmethode__ immer genauer als das Ablesen eines
Ausschlags: Sie verlangt dem Messgerät nur eine einzige, einfache Entscheidung ab — null oder nicht null — und
hängt sonst allein vom Verhältnis gut bekannter Widerstände ab.

:::grafik
Eine Nahaufnahme der Diagonalen im Abgleich: durch das Galvanometer der Strom $I = 0$, daneben zwei Notizen
„Quellenspannung $U$ kürzt sich heraus" und „Innenwiderstand des Messgeräts egal (kein Strom, kein
Spannungsabfall)".
:::

:::kern
Die __Wheatstonesche Messbrücke__ ist ein Vergleich zweier __Spannungsteiler__ an einer gemeinsamen Quelle mit
einem Galvanometer in der Diagonalen. Sie ist __abgeglichen__, wenn dort kein Strom fließt, also beide
Mittelpunkte gleiches Potenzial haben — die __Abgleichbedingung__ $R_1/R_2 = R_3/R_4$ bzw. $R_1 R_4 = R_2 R_3$.
Damit ist $R_x = R_2\,R_3/R_4$. Weil im Abgleich kein Strom durch das Messgerät fließt, fallen __Quellenspannung__
und __Innenwiderstand__ des Galvanometers heraus — diese __Nullmethode__ macht die Messung besonders genau.
:::

Damit ist die Messtechnik des Grundkurses abgedeckt. Das nächste Kapitel widmet sich den systematischen
Verfahren, mit denen man auch verzweigte Netzwerke elegant löst: Quellenumwandlung, Ersatzquellen,
Superposition und Leistungsanpassung.
