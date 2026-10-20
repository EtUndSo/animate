---
title: Die OPV-Grundschaltungen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120500
summary: Mit den beiden goldenen Regeln in wenigen Zeilen hergeleitet – der invertierende und nichtinvertierende Verstärker, der Spannungsfolger, der Addierer, der Subtrahierer und der Integrator.
tags: OPV, invertierender Verstärker, nichtinvertierender Verstärker, Spannungsfolger, Addierer, Subtrahierer, Integrator
---

:::konzept
Jetzt zahlt sich die Theorie aus: Mit den beiden goldenen Regeln — **kein Eingangsstrom** und **virtueller
Kurzschluss** — lässt sich jede OPV-Grundschaltung in wenigen Zeilen durchrechnen. Die Verstärkung steckt dabei
nie im OPV selbst, sondern immer im **Verhältnis äußerer Widerstände**. Dieselbe Idee liefert nicht nur
Verstärker, sondern auch Rechenschaltungen, die addieren, subtrahieren oder sogar integrieren — daher der Name
„Operations"-Verstärker.
:::

**Worum es geht:** Wir wenden die goldenen Regeln auf die wichtigsten Standardschaltungen an. Jede folgt demselben
Muster: Knotenregel an der virtuellen Masse, Eingangsströme null, fertig.

## Der invertierende Verstärker

Das Eingangssignal liegt über $R_1$ am invertierenden Eingang, der Rückkopplungswiderstand $R_\text{f}$ führt
vom Ausgang dorthin zurück; der nichtinvertierende Eingang liegt auf Masse.

**Schritt 1** — virtueller Kurzschluss: Weil $U_+ = 0$ (Masse), ist auch $U_- = 0$. Der invertierende Eingang
ist eine __virtuelle Masse__ — er liegt auf null, ohne mit der Masse verbunden zu sein.

**Schritt 2** — Knotenregel am invertierenden Eingang: In den Eingang fließt kein Strom (Regel 1), also muss der
Strom durch $R_1$ vollständig durch $R_\text{f}$ weiterfließen: $I_1 = I_\text{f}$.

**Schritt 3** — beide Ströme über die virtuelle Masse ausdrücken: $I_1 = \dfrac{U_\text{e} - 0}{R_1}$ und
$I_\text{f} = \dfrac{0 - U_\text{a}}{R_\text{f}}$. Gleichsetzen und nach $U_\text{a}$ auflösen liefert

$$U_\text{a} = -\frac{R_\text{f}}{R_1}\,U_\text{e}.$$

- __$U_\text{a}, U_\text{e}$__: __Ausgangs-__ und __Eingangsspannung__.
- __$R_1$__: der __Eingangswiderstand__ (vom Signal zur virtuellen Masse).
- __$R_\text{f}$__: der __Rückkopplungswiderstand__.

Das Minuszeichen zeigt: Die Schaltung **invertiert**. Die Verstärkung $-R_\text{f}/R_1$ ist allein durch das
Widerstandsverhältnis festgelegt — der OPV selbst taucht nicht mehr auf.

:::grafik
Der invertierende Verstärker: Eingangssignal über $R_1$ an den $-$-Eingang, $R_\text{f}$ vom Ausgang zurück zum
$-$-Eingang, $+$-Eingang an Masse. Die virtuelle Masse am $-$-Eingang ist markiert, der Stromweg $I_1 =
I_\text{f}$ eingezeichnet. Formel $U_\text{a} = -R_\text{f}/R_1 \cdot U_\text{e}$.
:::

## Der nichtinvertierende Verstärker

Hier liegt das Signal direkt am nichtinvertierenden Eingang; die Rückkopplung bildet einen Spannungsteiler aus
$R_\text{f}$ und $R_1$ (gegen Masse). Mit $U_- = U_+ = U_\text{e}$ (virtueller Kurzschluss) und dem Teilerverhältnis
ergibt sich

$$U_\text{a} = \left(1 + \frac{R_\text{f}}{R_1}\right) U_\text{e}.$$

Die Verstärkung ist **positiv** (nicht invertierend) und immer **mindestens 1**. Ein großer Vorteil gegenüber der
invertierenden Variante: Das Signal sieht den unendlichen Eingangswiderstand des OPV direkt, der
**Eingangswiderstand** der Schaltung ist also sehr hoch — die Quelle wird kaum belastet.

## Der Spannungsfolger

Setzt man im nichtinvertierenden Verstärker $R_\text{f} = 0$ (und lässt $R_1$ weg), wird die Verstärkung genau 1:

$$U_\text{a} = U_\text{e}.$$

Der __Spannungsfolger__ (Impedanzwandler) verstärkt also nicht, hat aber einen sehr hohen Eingangs- und einen
sehr niedrigen Ausgangswiderstand. Er ist das OPV-Gegenstück zum Emitterfolger: Er **entkoppelt** eine
empfindliche, hochohmige Quelle von einer niederohmigen Last, ohne das Signal zu verändern.

:::grafik
Links der nichtinvertierende Verstärker mit Spannungsteiler $R_\text{f}/R_1$ in der Rückkopplung und Formel
$(1+R_\text{f}/R_1)$. Rechts der Spannungsfolger: Ausgang direkt auf den $-$-Eingang zurückgeführt, $U_\text{a} =
U_\text{e}$, mit dem Hinweis „Impedanzwandler".
:::

## Addierer und Subtrahierer

Weil an der virtuellen Masse die Ströme nach der Knotenregel zusammenlaufen, kann man **mehrere** Eingänge
addieren. Der __Umkehraddierer__ legt mehrere Signale über je einen Widerstand auf die virtuelle Masse; ihre
Ströme summieren sich, und am Ausgang erscheint die negative gewichtete Summe:

$$U_\text{a} = -\left(\frac{R_\text{f}}{R_1}U_1 + \frac{R_\text{f}}{R_2}U_2 + \ldots\right).$$

Sind alle Eingangswiderstände gleich, ist das die reine (invertierte) Summe der Eingangsspannungen. Der
__Subtrahierer__ (Differenzverstärker) nutzt beide Eingänge und bildet bei passend gewählten Widerständen die
**Differenz**:

$$U_\text{a} = \frac{R_\text{f}}{R_1}\,(U_2 - U_1).$$

Damit lassen sich zwei Signale voneinander abziehen — die Grundlage jeder Messverstärker- und Sensorschaltung,
die auf Differenzen reagiert.

:::grafik
Links der Umkehraddierer: drei Eingänge über je einen Widerstand auf die virtuelle Masse, ein gemeinsamer
$R_\text{f}$ zum Ausgang, Formel der gewichteten Summe. Rechts der Subtrahierer mit Signalen an beiden Eingängen
und der Differenzformel.
:::

## Integrator: rechnen mit der Zeit

Ersetzt man den Rückkopplungswiderstand $R_\text{f}$ durch einen __Kondensator__ $C$, entsteht ein __Integrator__.
Der konstante Eingangsstrom $U_\text{e}/R_1$ lädt den Kondensator, und die Ausgangsspannung wächst proportional
zum **Zeitintegral** des Eingangs:

$$U_\text{a} = -\frac{1}{R_1\,C}\int U_\text{e}\,\mathrm{d}t.$$

Analog ergibt ein Kondensator am Eingang einen __Differenzierer__, dessen Ausgang der Ableitung des Eingangs
folgt. So wird der OPV vom reinen Verstärker zum analogen **Rechenbaustein** — er kann summieren, subtrahieren,
integrieren und differenzieren.

:::kern
Mit den goldenen Regeln folgen die Grundschaltungen direkt. __Invertierend:__ $U_\text{a} = -\tfrac{R_\text{f}}{R_1}U_\text{e}$
(virtuelle Masse, $I_1 = I_\text{f}$). __Nichtinvertierend:__ $U_\text{a} = (1 + \tfrac{R_\text{f}}{R_1})U_\text{e}$
(hoher Eingangswiderstand). __Spannungsfolger:__ $U_\text{a} = U_\text{e}$ (Impedanzwandler). __Addierer:__
negative gewichtete Summe; __Subtrahierer:__ Differenz. Mit Kondensator statt $R_\text{f}$ wird der OPV zum
__Integrator__ ($U_\text{a} = -\tfrac{1}{R_1 C}\int U_\text{e}\,\mathrm{d}t$). In jedem Fall legen die äußeren
Widerstände das Verhalten fest.
:::

Alle diese Ergebnisse gelten für den **idealen** OPV. In der Praxis setzen endliche Verstärkung, begrenzte
Bandbreite und kleine Fehlerspannungen dem Ganzen Grenzen — das ist das Thema des letzten Abschnitts.

:::quiz
F: Warum steckt die Verstärkung einer OPV-Schaltung in den äußeren Widerständen, nicht im OPV?
A: Die Gegenkopplung zwingt die Eingangsdifferenz auf null, sodass die gigantische Leerlaufverstärkung herausfällt. Übrig bleibt allein das Verhältnis der Rückkopplungs- und Eingangswiderstände.
F: Was bedeutet „virtuelle Masse" beim invertierenden Verstärker?
A: Weil der +-Eingang auf Masse liegt, zwingt der virtuelle Kurzschluss auch den −-Eingang auf 0 V — ohne ihn leitend mit Masse zu verbinden. Er liegt auf null Potenzial, aber es fließt kein Strom direkt zur Masse.
F: Warum ist beim invertierenden Verstärker $I_1=I_f$?
A: In den OPV-Eingang fließt kein Strom (Regel 1), also muss der gesamte Strom durch $R_1$ über $R_f$ weiterlaufen. Dieser Knotenstrombilanz an der virtuellen Masse entspringt die Verstärkungsformel.
F: Warum hat der nichtinvertierende Verstärker einen sehr hohen Eingangswiderstand?
A: Das Signal liegt direkt am +-Eingang, und dort fließt (Regel 1) kein Strom hinein. Die Quelle sieht also praktisch den unendlichen Eingangswiderstand des OPV und wird kaum belastet.
F: Warum ist die Verstärkung des nichtinvertierenden Verstärkers immer mindestens 1?
A: Sie ist $1+R_f/R_1$, und der Bruch ist nie negativ. Selbst bei $R_f=0$ bleibt der Faktor 1 — die Schaltung kann nicht abschwächen.
F: Wie entsteht aus dem nichtinvertierenden Verstärker der Spannungsfolger?
A: Man setzt $R_f=0$ und lässt $R_1$ weg, dann wird $1+R_f/R_1=1$ und $U_a=U_e$. Der Ausgang folgt dem Eingang exakt.
F: Wozu dient der Spannungsfolger, wenn er doch nicht verstärkt?
A: Als Impedanzwandler: hoher Eingangs-, niedriger Ausgangswiderstand. Er entkoppelt eine empfindliche, hochohmige Quelle von einer niederohmigen Last, ohne das Signal zu verändern.
F: Warum kann man an der virtuellen Masse mehrere Signale addieren?
A: Jeder Eingang speist über seinen Widerstand einen Strom in den gemeinsamen Knoten, und nach der Knotenregel summieren sich diese Ströme. Der Rückkopplungswiderstand wandelt die Summe in die (negative, gewichtete) Ausgangsspannung.
F: Warum ist ein Addierer am invertierenden Eingang besonders einfach, aber ein Subtrahierer aufwendiger?
A: Am invertierenden Eingang laufen alle Ströme an der virtuellen Masse zusammen und addieren sich direkt. Für eine Differenz muss man zusätzlich den nichtinvertierenden Eingang und die Widerstände passend wählen, damit sich die Gewichte sauber subtrahieren.
F: Wieso bildet ein Kondensator statt $R_f$ einen Integrator?
A: Der konstante Eingangsstrom $U_e/R_1$ lädt den Kondensator, und seine Spannung wächst proportional zur aufgenommenen Ladung — also zum Zeitintegral des Eingangs. Daraus folgt $U_a=-\tfrac{1}{R_1 C}\int U_e\,\mathrm{d}t$.
:::
