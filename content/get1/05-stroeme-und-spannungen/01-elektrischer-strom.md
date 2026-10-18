---
title: Der elektrische Strom
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50100
summary: Was im Draht wirklich passiert, wenn Strom fließt — von der Ladung über die Stromstärke bis zur Frage, warum das Licht sofort angeht, obwohl die Elektronen kriechen.
tags: Strom, Ladung, Stromstärke, Ampere, Stromdichte, Driftgeschwindigkeit, technische Stromrichtung
---

:::konzept
Strom ist nichts anderes als **Ladung, die sich bewegt**. Stell dir vor, du stehst an einer Stelle im Draht
und zählst, wie viel Ladung pro Sekunde an dir vorbeikommt. Genau diese Zahl ist die __Stromstärke__. Mehr
steckt im Kern nicht dahinter — alles Weitere ist nur die Frage, *was* da wandert, *wie schnell* und *in
welche Richtung*.
:::

**Worum es geht:** „Strom fließt" ist schnell gesagt, aber was fließt da physikalisch, und wie macht man
daraus eine messbare Größe? Dieser Abschnitt baut den Begriff von unten auf: erst die Ladung, dann ihre
Bewegung, dann die Zahl, die beides zusammenfasst.

## Was fließt da eigentlich: die Ladung

Bevor etwas fließen kann, muss klar sein, *was* fließt. Das ist die __elektrische Ladung__ $Q$, gemessen in
__Coulomb__ (Einheitszeichen C). Ladung gibt es in zwei Sorten, die wir **positiv** und **negativ** nennen.
Gleichnamige Ladungen stoßen sich ab, ungleichnamige ziehen sich an — das ist die Grundkraft, aus der am Ende
jede Spannung und jeder Strom entstehen.

:::grafik
Zwei Kugeln mit $+$ und $-$: bei gleichen Vorzeichen Pfeile voneinander weg (Abstoßung), bei
ungleichen aufeinander zu (Anziehung). Pfeillängen gleich groß, um das Kräftegleichgewicht zu zeigen.
:::

Entscheidend ist, dass Ladung nicht beliebig fein teilbar ist. Sie tritt immer als ganzzahliges Vielfaches
einer kleinsten Portion auf, der __Elementarladung__

$$e \approx 1{,}602 \cdot 10^{-19}\,\text{C}.$$

Ein einzelnes Elektron trägt die Ladung **$-e$**, ein Proton **$+e$**. Dass uns der Strom trotzdem wie eine
glatte, kontinuierliche Größe erscheint, liegt an den gewaltigen Stückzahlen: In einem Alltagsstrom wandern
pro Sekunde Trillionen Elektronen vorbei, da fällt die Körnigkeit der einzelnen Ladungsportionen nicht auf.

In einem Metalldraht sind es die __Leitungselektronen__, die sich bewegen. Die __Atomrümpfe__ — die Atome
ohne ihre abgegebenen Außenelektronen — sitzen fest im __Kristallgitter__, dem regelmäßigen räumlichen Muster,
in dem die Atome angeordnet sind. Einige äußere Elektronen sind aber an kein einzelnes Atom gebunden und
können durch das ganze Metall wandern. Diese frei beweglichen Elektronen sind die __Ladungsträger__, um die es
geht. Wie viele davon pro Volumen zur Verfügung stehen, ist von Material zu Material verschieden und entscheidet
später mit darüber, wie gut ein Stoff leitet.

## Die Stromstärke: Ladung pro Zeit

Damit lässt sich die __Stromstärke__ sauber definieren. Sie ist die Ladungsmenge, die pro Zeit durch einen
Querschnitt des Leiters tritt:

$$I = \frac{\mathrm{d}Q}{\mathrm{d}t}.$$

Bestandteil für Bestandteil:

- __$I$__: die __Stromstärke__, die gesuchte Größe. Einheit __Ampere__ (A), und zwar eine der sieben
  __SI-Basisgrößen__, also nicht aus anderen Größen abgeleitet, sondern selbst Grundbaustein.
- __$Q$__: die __Ladung__, die bereits durch den Querschnitt geflossen ist, in Coulomb.
- __$t$__: die __Zeit__ in Sekunden.
- __$\dfrac{\mathrm{d}Q}{\mathrm{d}t}$__: die __Ableitung__ der Ladung nach der Zeit, also die *Rate*, mit der
  gerade Ladung vorbeiströmt.

Warum überhaupt eine Ableitung und nicht einfach $Q/t$? Weil der Strom sich im Allgemeinen ständig ändert —
beim Einschalten, bei Wechselstrom, in jeder realen Schaltung. Die Ableitung $\mathrm{d}Q/\mathrm{d}t$ liefert
den Wert **genau in einem Augenblick**, den __Momentanwert__. Fließt der Strom dagegen gleichmäßig, bleibt die
Rate konstant, und man darf die Ableitung durch den einfachen Quotienten $I = Q/t$ ersetzen. Aus der Definition
folgt direkt der Zusammenhang der Einheiten:

$$1\,\text{A} = 1\,\frac{\text{C}}{\text{s}}, \qquad \text{also} \qquad 1\,\text{C} = 1\,\text{A}\cdot\text{s}.$$

Ein __Coulomb__ ist damit keine besonders handliche Portion Ladung, sondern schlicht die Ladung, die bei einem
__Ampere__ in einer Sekunde durch den Querschnitt tritt. Und das Ampere selbst ist über die Elementarladung
festgelegt: Seit der Neudefinition der SI-Einheiten (2019) hat $e$ einen exakt festgelegten Zahlenwert, und ein
Ampere bedeutet, dass in jeder Sekunde eine fest definierte, riesige Zahl von Elementarladungen den Querschnitt
passiert.

**Anders betrachtet.** Trägt man die durchgeflossene Ladung $Q$ über der Zeit $t$ auf, dann ist die
Stromstärke nichts anderes als die **Steigung dieser Kurve**. Ein konstanter Strom ist eine Gerade, ein
ansteigender Strom eine nach oben gekrümmte Kurve. Das ist dasselbe Bild wie in der Mechanik: So wie die
Geschwindigkeit die Steigung der Weg-Zeit-Kurve ist, ist der Strom die Steigung der Ladungs-Zeit-Kurve.

:::grafik
Ein $Q$-$t$-Diagramm. Eine gerade Linie für konstanten Strom, daneben ein Steigungsdreieck, dessen
Verhältnis $\Delta Q / \Delta t$ als $I$ beschriftet ist. Zweite, gekrümmte Kurve für ansteigenden Strom mit
einer Tangente, die zeigt: der Momentanwert ist die Steigung in genau einem Punkt.
:::

Was heißt das konkret? Ein Strom von $I = 2\,\text{A}$ bedeutet, dass pro Sekunde $2\,\text{C}$ an Ladung einen
Querschnitt passieren. In Elektronen umgerechnet:

$$\frac{2\,\text{C}}{1{,}602 \cdot 10^{-19}\,\text{C}} \approx 1{,}25 \cdot 10^{19}\ \text{Elektronen pro Sekunde.}$$

## In welche Richtung? Technische und tatsächliche Stromrichtung

An diesem Punkt stolpern viele. Lange bevor man das Elektron kannte, hatte man schon festgelegt, dass der
Strom außerhalb der Quelle vom __Pluspol__ zum __Minuspol__ fließt. Das nennt man die __technische
Stromrichtung__. Später zeigte sich, dass im Metall die negativ geladenen Elektronen wandern — und die laufen
genau andersherum, vom Minus- zum Pluspol.

Korrigiert hat man die alte Festlegung trotzdem nicht, und das muss man auch nicht.

:::grafik
Ein Stromkreis mit Batterie und Lampe. Ein roter Pfeil außen zeigt die technische Stromrichtung (Plus → Minus),
ein zweiter, blauer Pfeil daneben die tatsächliche Bewegung der Elektronen (Minus → Plus), damit der Gegensatz
sofort sichtbar wird.
:::

**Zwei Sichtweisen, dasselbe Ergebnis.** Eine positive Ladung, die nach rechts wandert, ist für jede Rechnung
dasselbe wie eine negative Ladung, die nach links wandert — in beiden Fällen nimmt die positive Ladung rechts
zu. Deshalb darf man rechnen, als flössen positive Träger in technischer Richtung, obwohl physikalisch
Elektronen entgegengesetzt laufen. Alle Formeln und Vorzeichen der Schaltungsanalyse beziehen sich auf die
__technische Stromrichtung__; die tatsächliche Elektronenbewegung braucht man nur, wenn es um das Innenleben
des Materials geht.

## Der mikroskopische Blick: warum das Licht sofort angeht

Man würde erwarten, dass die Elektronen schnell durch den Draht wandern. Das Gegenteil ist der Fall: Sie
bewegen sich **sehr langsam** vorwärts. Zur Einordnung muss man zwei Geschwindigkeiten auseinanderhalten.
Zufällig, durch die Wärme, zittern die Elektronen mit mehreren Hundert Kilometern pro Sekunde kreuz und quer —
aber dieses Gewusel hebt sich im Mittel auf und transportiert nichts. Legt man eine Spannung an, bekommt die
ungeordnete Bewegung nur eine winzige gemeinsame Vorzugsrichtung. Diese mittlere Netto-Geschwindigkeit in
Stromrichtung heißt __Driftgeschwindigkeit__ $v_\text{d}$ und liegt bei Alltagsströmen bei Bruchteilen eines
Millimeters pro Sekunde — langsamer als eine kriechende Schnecke.

:::grafik
Ein Ausschnitt des Drahts mit vielen Elektronen. Dünne, wirre Zickzack-Linien zeigen die thermische Bewegung;
darüber ein einzelner, langer, langsamer Pfeil nach rechts für die gemeinsame Drift. Kernaussage des Bildes:
viel Gezappel, kaum Netto-Weg.
:::

Diesen überraschend kleinen Wert liefert der folgende Zusammenhang, der die makroskopische Stromstärke mit dem
mikroskopischen Geschehen verbindet:

$$I = n \cdot A \cdot e \cdot v_\text{d}.$$

Jeder Faktor einzeln:

- __$n$__: die __Ladungsträgerdichte__, also die Zahl der frei beweglichen Elektronen pro Volumen (Einheit
  $1/\text{m}^3$). In Kupfer ist sie gewaltig, rund $n \approx 10^{29}\,\text{m}^{-3}$.
- __$A$__: die __Querschnittsfläche__ des Drahtes, durch die der Strom tritt (in $\text{m}^2$).
- __$e$__: die __Elementarladung__, die jedes Elektron beisteuert.
- __$v_\text{d}$__: die __Driftgeschwindigkeit__ der Träger (in $\text{m}/\text{s}$).

Woher dieses Produkt kommt, sieht man am besten, wenn man es in zwei Schritten aufbaut.

**Schritt 1** — welche Ladungsträger schaffen es in einer Sekunde durch den Querschnitt? Alle, die nicht weiter
als eine Wegstrecke $v_\text{d}\cdot t$ entfernt sind, denn genau so weit kommt ein Träger in der Zeit $t$.
Diese Träger füllen ein gedachtes Stück Draht mit der Querschnittsfläche $A$ und der Länge $v_\text{d}\cdot t$,
also mit dem Volumen $V = A \cdot v_\text{d} \cdot t$.

**Schritt 2** — wie viel Ladung sitzt in diesem Volumen? Die Trägerdichte $n$ sagt, wie viele Träger pro
Volumen da sind; mal dem Volumen ergibt das ihre Anzahl $N = n \cdot V$. Jeder trägt die Ladung $e$, also ist
die durchgetretene Ladung $Q = e \cdot N = e \cdot n \cdot A \cdot v_\text{d} \cdot t$. Teilt man das durch die
Zeit, fällt $t$ heraus, und übrig bleibt genau

$$I = \frac{Q}{t} = n \cdot A \cdot e \cdot v_\text{d}.$$

Die eigentliche Pointe steckt in den Größenordnungen. Weil $n$ in einem Metall astronomisch groß ist (in Kupfer
rund $10^{29}$ Träger pro Kubikmeter), muss jeder einzelne Träger nur winzig langsam wandern, um in Summe einen
kräftigen Strom zu tragen. Stellt man die Gleichung nach $v_\text{d}$ um und setzt für einen typischen Draht
($I = 1\,\text{A}$, Querschnitt $1{,}5\,\text{mm}^2$) ein, erhält man

$$v_\text{d} = \frac{I}{n \cdot A \cdot e} \approx 0{,}04\,\frac{\text{mm}}{\text{s}}.$$

Vier Hundertstel Millimeter pro Sekunde — ein einzelnes Elektron bräuchte für einen Meter Draht also fast einen
halben Tag.

**Stolperstein: Wenn die Elektronen so langsam sind, warum leuchtet die Lampe dann sofort, wenn ich den
Schalter drücke?** Weil kein einzelnes Elektron von der Quelle bis zur Lampe reisen muss. Der Draht ist bereits
**überall** voll mit Ladungsträgern. Drückt man am einen Ende, setzt sich die ganze Kette praktisch
gleichzeitig in Bewegung — das treibende elektrische Feld breitet sich im Leiter **nahezu mit
Lichtgeschwindigkeit** aus.

Das gleiche Bild liefert ein randvoll mit Wasser gefülltes Rohr: Drückst du vorne Wasser hinein, tritt hinten
sofort welches aus, obwohl kein einzelnes Wassermolekül in dieser kurzen Zeit die ganze Strecke zurücklegt.
(Das Wasserbild ist eine *Analogie* und darf nicht überstrapaziert werden — Ladung ist kein Wasser —, aber für
genau diesen Punkt trifft es den Kern.)

## Die Stromdichte: Strom pro Fläche

Die Stromstärke sagt, *wie viel* Ladung pro Zeit fließt, aber nicht, *wie dicht gedrängt*. Dafür gibt es die
__Stromdichte__. Verteilt sich der Strom $I$ gleichmäßig über die Querschnittsfläche $A$, ist sie

$$J = \frac{I}{A}, \qquad [J] = \frac{\text{A}}{\text{m}^2}.$$

- __$J$__: die __Stromdichte__, ein Maß dafür, wie viel Strom sich durch jede Flächeneinheit zwängt.
- __$I$__: die __Stromstärke__ durch die Fläche.
- __$A$__: die durchströmte __Querschnittsfläche__.

In der Praxis rechnet man oft in $\text{A}/\text{mm}^2$, weil Drahtquerschnitte in Quadratmillimetern
angegeben werden.

:::grafik
Zwei Drähte mit demselben Strom, einer dick, einer dünn. Im dünnen Draht drängen sich die Stromlinien enger —
höhere Stromdichte —, angedeutet durch eine wärmere Einfärbung, um die stärkere Erwärmung sichtbar zu machen.
:::

Genau genommen ist die __Stromdichte__ mehr als eine Zahl: Sie ist ein __Vektor__ $\vec{J}$, der in jedem Punkt
in die Richtung zeigt, in die dort gerade Ladung strömt, und dessen Betrag angibt, wie dicht der Fluss ist. Der
einfache Quotient $J = I/A$ ist der Spezialfall eines Drahtes, in dem der Strom überall gleich stark und
parallel fließt. In verzweigten Leitern oder im Inneren von Körpern ändert die Strömung Richtung und Dichte von
Ort zu Ort — dann braucht man das __Vektorfeld__. Es ist der erste Schritt von der Schaltungsgröße Strom hin zur
Feldbeschreibung, mit der sich später beschreiben lässt, *wie* sich der Strom im Material verteilt.

:::kern
Strom ist bewegte Ladung. Die __Stromstärke__ $I = \dfrac{\mathrm{d}Q}{\mathrm{d}t}$ zählt die Ladung pro Zeit;
ihre Einheit __Ampere__ ist eine SI-Basisgröße, und es gilt $1\,\text{C} = 1\,\text{A}\cdot\text{s}$. Als
__technische Stromrichtung__ gilt der Weg von Plus nach Minus. Die __Ladungsträger__ driften überraschend
langsam ($I = n\,A\,e\,v_\text{d}$), der Effekt breitet sich aber fast mit Lichtgeschwindigkeit aus. Die
__Stromdichte__ $J = \dfrac{I}{A}$ beschreibt, wie dicht gedrängt der Strom fließt, und entscheidet über die
Erwärmung.
:::

Damit ist geklärt, *was* fließt. Die nächste Frage ist, *was es antreibt*: die __Spannung__. Aus dem
Zusammenspiel von Strom und Spannung ergibt sich dann der wichtigste Zusammenhang der Schaltungsanalyse, das
__Ohmsche Gesetz__.
