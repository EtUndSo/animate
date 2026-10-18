---
title: Der elektrische Strom
fach: Elektrotechnik
thema: Grundlagen
order: 1
summary: Was im Draht wirklich passiert, wenn Strom fließt — von der Ladung über die Stromstärke bis zur Frage, warum das Licht sofort angeht, obwohl die Elektronen kriechen.
tags: Strom, Ladung, Stromstärke, Ampere, Stromdichte, Driftgeschwindigkeit, technische Stromrichtung
---

:::konzept
Strom ist nichts anderes als Ladung, die sich bewegt. Stell dir vor, du stehst an einer Stelle im Draht
und zählst, wie viel Ladung pro Sekunde an dir vorbeikommt. Genau diese Zahl ist die Stromstärke. Je mehr
Ladung pro Zeit vorbeiwandert, desto größer der Strom. Mehr steckt im Kern nicht dahinter — alles Weitere
ist nur die Frage, *was* da wandert, *wie schnell*, und *in welche Richtung*.
:::

## Was fließt da eigentlich? Die Ladung

Bevor etwas fließen kann, muss klar sein, was fließt. Das ist die **elektrische Ladung** $Q$, gemessen in
**Coulomb** (Einheitszeichen C). Ladung gibt es in zwei Sorten, die wir positiv und negativ nennen.
Gleichnamige Ladungen stoßen sich ab, ungleichnamige ziehen sich an — das ist die Grundkraft, aus der am
Ende jede Spannung und jeder Strom entsteht.

Entscheidend ist, dass Ladung nicht beliebig fein teilbar ist. Sie kommt immer als ganzzahliges Vielfaches
einer kleinsten Portion vor, der **Elementarladung**

$$e \approx 1{,}602 \cdot 10^{-19}\,\text{C}.$$

Ein einzelnes Elektron trägt die Ladung $-e$, ein Proton $+e$. Dass uns der Strom trotzdem wie eine glatte,
kontinuierliche Größe erscheint, liegt nur an den gigantischen Stückzahlen: In einem Alltagsstrom wandern
pro Sekunde Trillionen Elektronen vorbei, und bei so vielen fällt die Körnigkeit nicht auf.

In einem Metalldraht sind es die **Leitungselektronen**, die sich bewegen können. Die Atomrümpfe sitzen fest
im Kristallgitter; einige äußere Elektronen aber sind nicht an ein einzelnes Atom gebunden, sondern können
durch das ganze Metall wandern. Diese frei beweglichen Elektronen sind die Ladungsträger, um die es geht.

## Stromstärke: Ladung pro Zeit

Damit lässt sich die **Stromstärke** sauber definieren. Sie ist die Ladungsmenge, die pro Zeit durch einen
Querschnitt des Leiters tritt:

$$I = \frac{\mathrm{d}Q}{\mathrm{d}t}.$$

Fließt der Strom gleichmäßig, vereinfacht sich das zu $I = Q/t$. Die Einheit ist das **Ampere** (A) — und
zwar nicht als abgeleitete Größe, sondern als eine der sieben SI-Basisgrößen. Aus der Definition folgt direkt

$$1\,\text{A} = 1\,\frac{\text{C}}{\text{s}}, \qquad \text{also} \qquad 1\,\text{C} = 1\,\text{A}\cdot\text{s}.$$

Ein Coulomb ist damit keine besonders anschauliche Portion Ladung, sondern einfach die Ladung, die bei einem
Ampere in einer Sekunde durchfließt.

Was heißt das konkret? Ein Strom von $I = 2\,\text{A}$ bedeutet, dass pro Sekunde $2\,\text{C}$ an Ladung einen
Querschnitt passieren. In Elektronen umgerechnet:

$$\frac{2\,\text{C}}{1{,}602 \cdot 10^{-19}\,\text{C}} \approx 1{,}25 \cdot 10^{19} \text{ Elektronen pro Sekunde.}$$

Die Ableitung $\mathrm{d}Q/\mathrm{d}t$ beschreibt den *momentanen* Strom — den Wert genau jetzt. Schwankt der
Strom, ist das die einzig korrekte Beschreibung; $Q/t$ liefert nur den zeitlichen Mittelwert.

> Grafik (Editor): Querschnitt durch einen Draht mit einer gedachten Zählebene; Ladungsträger wandern
> hindurch, daneben die Zählung "Ladung pro Zeit".

## In welche Richtung? Technische und tatsächliche Stromrichtung

Hier gibt es eine Stolperstelle, die jedem einmal begegnet. Lange bevor man das Elektron kannte, hatte man
schon festgelegt, dass der Strom außerhalb der Quelle vom Pluspol zum Minuspol fließt. Das nennt man die
**technische Stromrichtung**. Später stellte sich heraus, dass im Metall die negativ geladenen Elektronen
wandern — und die laufen genau andersherum, vom Minus- zum Pluspol.

Korrigiert hat man die alte Festlegung nie, und das ist auch nicht nötig. Eine positive Ladung, die nach
rechts wandert, ist für jede Rechnung dasselbe wie eine negative Ladung, die nach links wandert. Alle Formeln
und Vorzeichen in der Schaltungsanalyse beziehen sich auf die technische Richtung. Die tatsächliche
Elektronenbewegung muss man nur kennen, wenn es um das Innenleben des Materials geht.

## Der mikroskopische Blick: warum das Licht sofort angeht

Jetzt wird es interessant. Man könnte meinen, die Elektronen rasen durch den Draht. Tatsächlich ist das
Gegenteil der Fall: Sie **kriechen**. Die mittlere Geschwindigkeit, mit der sie sich netto vorwärtsbewegen,
heißt **Driftgeschwindigkeit** $v_\text{d}$ und liegt bei Alltagsströmen im Bereich von Bruchteilen eines
Millimeters pro Sekunde.

Woran das liegt, zeigt der Zusammenhang

$$I = n \cdot A \cdot e \cdot v_\text{d},$$

mit der Ladungsträgerdichte $n$ (Zahl der freien Elektronen pro Volumen), der Querschnittsfläche $A$ und der
Elementarladung $e$. In Kupfer ist $n$ gewaltig — rund $10^{29}$ Elektronen pro Kubikmeter. Wenn so unfassbar
viele Träger gemeinsam beitragen, muss jeder einzelne nur sehr langsam wandern, um in Summe einen kräftigen
Strom zu ergeben. Stellt man die Gleichung nach $v_\text{d}$ um, landet man für einen normalen Draht tatsächlich
bei Werten um einige Hundertstel Millimeter pro Sekunde.

Das wirft sofort eine Frage auf: Wenn die Elektronen so langsam sind, warum leuchtet die Lampe dann im selben
Moment, in dem ich den Schalter drücke? Weil nicht ein einzelnes Elektron von der Quelle zur Lampe reisen muss.
Der Draht ist bereits *überall* voll mit Ladungsträgern. Drückt man am einen Ende, setzt sich die ganze
Kette praktisch gleichzeitig in Bewegung — das treibende elektrische Feld breitet sich im Leiter nahezu mit
Lichtgeschwindigkeit aus. Dasselbe Bild liefert ein randvoll mit Wasser gefülltes Rohr: Drückst du vorne
Wasser hinein, tritt hinten sofort welches aus, obwohl kein einzelnes Wassermolekül in dieser kurzen Zeit die
ganze Strecke zurücklegt. (Das Wasserbild ist eine Analogie und darf nicht überstrapaziert werden — Ladung ist
kein Wasser —, aber für diesen einen Punkt trifft es den Kern.)

## Stromdichte: Strom pro Fläche

Die Stromstärke sagt, *wie viel* Ladung pro Zeit fließt, aber nicht, *wie eng gedrängt*. Dafür gibt es die
**Stromdichte**. Verteilt sich der Strom $I$ gleichmäßig über die Querschnittsfläche $A$, ist sie

$$J = \frac{I}{A}, \qquad [J] = \frac{\text{A}}{\text{m}^2}.$$

In der Praxis rechnet man oft in $\text{A}/\text{mm}^2$, weil Drahtquerschnitte in Quadratmillimetern angegeben
werden. Die Stromdichte ist deshalb so wichtig, weil sie über die Erwärmung entscheidet: Zwingt man denselben
Strom durch einen dünneren Draht, steigt die Stromdichte, und der Draht wird heißer. Genau daran bemisst sich,
wie viel Strom eine Leitung dauerhaft tragen darf, ohne Schaden zu nehmen.

:::kern
Strom ist bewegte Ladung. Die Stromstärke $I = \mathrm{d}Q/\mathrm{d}t$ zählt die Ladung pro Zeit; ihre Einheit
Ampere ist eine SI-Basisgröße, und es gilt $1\,\text{C} = 1\,\text{A}\cdot\text{s}$. Als technische Stromrichtung
gilt der Weg von Plus nach Minus. Die Ladungsträger driften überraschend langsam, der Effekt breitet sich aber
fast mit Lichtgeschwindigkeit aus. Die Stromdichte $J = I/A$ beschreibt, wie dicht gedrängt der Strom fließt.
:::

Damit ist geklärt, *was* fließt. Die nächste Frage ist, *was es antreibt*: die Spannung. Und aus dem
Zusammenspiel von Strom und Spannung ergibt sich dann der wichtigste Zusammenhang der Schaltungsanalyse, das
Ohmsche Gesetz.
