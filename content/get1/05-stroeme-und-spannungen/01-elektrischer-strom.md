---
title: Der elektrische Strom
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50100
summary: Von Grund auf – was im Draht fließt, wenn Strom fließt. Leitbild ist ein randvolles Wasserrohr mit einer Wasseruhr: Strom ist, was pro Sekunde durch einen Querschnitt tritt, und weil das Rohr voll ist, genügt ein langsames Wandern für einen kräftigen Strom. Mit Ladung und Ladungsträgern, der Raumladungsdichte am Quader, der Stromstärke als Grenzwert, der technischen Stromrichtung, der Stromdichte als Vektor, der überraschend kleinen Driftgeschwindigkeit, der Frage, warum das Licht trotzdem sofort angeht, und den Bedingungen für einen dauerhaften Strom samt Kontinuität. Mit Beispiel-Seite.
tags: Strom, Ladung, Stromstärke, Ampere, Stromdichte, Driftgeschwindigkeit, technische Stromrichtung
---

## Anschaulich

Strom ist bewegte Ladung. Wer wissen will, wie stark ein Strom ist, stellt sich an eine Stelle des Leiters und zählt, wie viel Ladung pro Sekunde an
ihm vorbeikommt. Mehr steckt im Kern nicht dahinter — alles Weitere ist die Frage, was da wandert, wie schnell und in welche Richtung.

**Das Leitbild dieses Artikels:** **ein randvolles Wasserrohr mit einer Wasseruhr**. Die Wasseruhr sitzt an einer Stelle des Rohrs und misst, wie viel
Wasser pro Sekunde hindurchtritt — das ist die Stromstärke. Weil das Rohr voll ist, kann ein kräftiger Durchfluss entstehen, obwohl jedes einzelne
Wasserteilchen nur langsam wandert. Und drückt man am einen Ende Wasser hinein, tritt es am anderen Ende sofort aus, ohne dass ein Teilchen die ganze
Strecke zurücklegen muss.

Ein Metalldraht ist ein solches volles Rohr, gefüllt mit beweglichen Elektronen. Damit es dauerhaft fließt, braucht es eine Pumpe und einen
geschlossenen Kreislauf — elektrisch eine Quelle und einen geschlossenen Stromkreis. Das Wasserbild ist eine Analogie und an manchen Stellen
schief, etwa beim Vorzeichen der Ladung; wo es nicht trägt, steht es unten dabei.

:::grafik
Szene: get1/stroeme-und-spannungen/01-volles-rohr · Vorlage: rohr-wasseruhr
Ein langes, durchsichtiges Rohr voller Kugeln, links eine Pumpe, das Rohr zum Kreis geschlossen. An einer Stelle eine Wasseruhr mit Zähler. Ein
Regler startet die Pumpe: Alle Kugeln setzen sich gleichzeitig langsam in Bewegung, und der Zähler zählt einen kräftigen Durchfluss. Ein markiertes
Kügelchen kriecht dabei nur ein kurzes Stück, während am anderen Ende sofort Kugeln austreten. Ein zweiter Regler verengt ein Rohrstück: Dort laufen
die Kugeln schneller, der Zähler an der engen Stelle zeigt denselben Durchfluss. Kernaussage: Strom ist Durchfluss durch einen Querschnitt; im vollen
Rohr genügt langsames Wandern für einen großen Strom. (Blau = Kugeln und Strömung, rot = markierte Kugel, orange = Zähler, grau = Rohr und Pumpe.)
:::

## Ladung und Ladungsträger

Was fließt, ist __elektrische Ladung__ $Q$, gemessen in __Coulomb__. Es gibt sie in zwei Sorten, positiv und negativ, und sie ist nicht beliebig fein
teilbar: Jede Ladung ist ein ganzzahliges Vielfaches der __Elementarladung__ $e$, rund $1{,}602\cdot10^{-19}\,\text{C}$. Ein Proton trägt $+e$, ein
Elektron $-e$.

Die Ladungen, die sich bewegen können, heißen __Ladungsträger__. In Metallen sind es die __Leitungselektronen__: Die Atome sitzen als positive
__Atomrümpfe__ fest in einem regelmäßigen Gitter, dem __Kristallgitter__, und jedes gibt eines oder mehrere Außenelektronen ab, die sich frei durch das
ganze Metall bewegen. In Salzlösungen und Batterien wandern __Ionen__, geladene Atome oder Moleküle; in Halbleitern zusätzlich __Löcher__, fehlende
Elektronen, die sich wie positive Ladungen verhalten (Kapitel 10).

**Im Bild:** Die Leitungselektronen sind das Wasser im Rohr, das Gitter der Atomrümpfe ist das Rohr selbst. Anders als beim Wasser ist das Rohr hier
positiv geladen und gleicht die Ladung des Wassers genau aus: Ein Draht ist im Ganzen neutral, auch wenn Strom fließt.

## Bewegte Ladung: die Raumladungsdichte

Um den Strom zu berechnen, betrachtet das Skript einen kleinen Quader mit den Kantenlängen $\Delta x$, $\Delta y$ und $\Delta z$, also dem Volumen
$\Delta V$, in dem die bewegliche Ladung $\Delta Q$ steckt. Wie dicht sie verteilt ist, misst die __Raumladungsdichte__:

$$\rho = \frac{\Delta Q}{\Delta V}, \qquad \Delta V = \Delta x\,\Delta y\,\Delta z.$$

Das Skript nennt sie $q$; hier heißt sie nach DIN $\rho$. Bewegt sich die Ladung mit der Geschwindigkeit $v_z$ in $z$-Richtung, tritt in der Zeit $\Delta t$
durch die Seitenfläche $\Delta x\,\Delta y$ die Ladung

$$\frac{\Delta Q}{\Delta t} = \rho\,v_z\,\Delta x\,\Delta y$$

pro Zeit hindurch.

**So liest man das:** Der Durchfluss ist Dichte mal Geschwindigkeit mal Fläche. Mehr Ladung pro Volumen, schnellere Bewegung oder ein größerer
Querschnitt — jedes davon vergrößert, was pro Sekunde durchtritt.

**Im Bild:** Durch die Wasseruhr tritt pro Sekunde das Wasser aus einer Säule, deren Grundfläche der Querschnitt ist und deren Länge die Strecke, die
das Wasser in einer Sekunde zurücklegt.

:::herleitung
In der Zeit $\Delta t$ legt jede Ladung die Strecke $v_z\,\Delta t$ zurück. Durch die Seitenfläche treten also genau die Ladungen, die höchstens so weit
von ihr entfernt waren: alle in einer Säule mit der Grundfläche $\Delta x\,\Delta y$ und der Länge $v_z\,\Delta t$. Ihre Ladung ist Dichte mal Volumen:

$$\Delta Q = \rho\cdot\Delta x\,\Delta y\,v_z\,\Delta t.$$

Geteilt durch $\Delta t$ folgt die Formel.
:::

:::grafik
Szene: get1/stroeme-und-spannungen/01-ladungssaeule · Vorlage: quader-durchfluss
Ein Quader mit den Kanten $\Delta x$, $\Delta y$, $\Delta z$, gefüllt mit Ladungen, die sich mit $v_z$ in $z$-Richtung bewegen; die Seitenfläche $\Delta x\,\Delta y$ ist
hervorgehoben. Ein Zeitregler läuft von $0$ bis $\Delta t$: Vor der Fläche färbt sich eine Säule der Länge $v_z\,\Delta t$, deren Ladungen in dieser Zeit die
Fläche passieren; ein Zähler zeigt $\rho\,\Delta x\,\Delta y\,v_z\,\Delta t$. Regler für $\rho$ und $v_z$ verlängern bzw. verdichten die Säule. Kernaussage: Pro
Zeit tritt die Ladung einer Säule aus Querschnitt mal Geschwindigkeit durch die Fläche. (Blau = Ladungen, rot = durchtretende Säule, orange = Zähler,
grau = Quaderkanten.)
:::

::::beispiel Wie viel bewegliche Ladung steckt in Kupfer?
Kupfer hat die Dichte $8{,}96\,\frac{\text{g}}{\text{cm}^3}$ und die molare Masse $63{,}55\,\frac{\text{g}}{\text{mol}}$, und jedes Atom gibt ein
Leitungselektron ab. Mit der Avogadro-Konstante aus dem Artikel über Einheiten ist die Zahl der Leitungselektronen pro Volumen

$$n = \frac{8{,}96\,\text{g}/\text{cm}^3}{63{,}55\,\text{g}/\text{mol}}\cdot6{,}022\cdot10^{23}\,\frac{1}{\text{mol}} \approx 8{,}49\cdot10^{22}\,\frac{1}{\text{cm}^3} = 8{,}49\cdot10^{28}\,\frac{1}{\text{m}^3}.$$

Ihre Raumladungsdichte:

$$\rho = -n\,e \approx -8{,}49\cdot10^{28}\,\frac{1}{\text{m}^3}\cdot1{,}602\cdot10^{-19}\,\text{C} \approx -1{,}36\cdot10^{10}\,\frac{\text{C}}{\text{m}^3}.$$

Das sind über $13\,000$ Coulomb in jedem Kubikzentimeter — ausgeglichen durch ebenso viel positive Ladung der Atomrümpfe. Wandern die Elektronen nur
$0{,}1\,\frac{\text{mm}}{\text{s}}$ durch einen Querschnitt von $1\,\text{mm}^2$, sind das schon

$$1{,}36\cdot10^{10}\,\frac{\text{C}}{\text{m}^3}\cdot10^{-4}\,\frac{\text{m}}{\text{s}}\cdot10^{-6}\,\text{m}^2 \approx 1{,}36\,\frac{\text{C}}{\text{s}}.$$

**Im Bild:** Das Rohr ist bis zum Rand voll. Schon ein Kriechen von einem Zehntel Millimeter pro Sekunde schiebt mehr als ein Coulomb pro Sekunde durch
die Wasseruhr.
::::

## Die Stromstärke

Lässt man das Zeitintervall gegen null gehen, erhält man den Durchfluss in einem Augenblick, die __Stromstärke__:

:::formel Definition
$$I := \lim_{\Delta t\to0}\frac{\Delta Q}{\Delta t} = \frac{dQ}{dt}, \qquad [I] = \frac{\text{C}}{\text{s}} = \text{A}.$$
:::

**So liest man das:** Die Stromstärke ist die Ladung, die pro Zeit durch einen Querschnitt tritt, im Augenblick betrachtet. Ihre Einheit, das
__Ampere__, ist eine der sieben Basiseinheiten, und das Coulomb ist daraus abgeleitet, eine Amperesekunde. Ändert sich der Strom mit der Zeit, schreibt
man nach DIN kleine Buchstaben, $i(t)$ als Ableitung der Ladung $q(t)$; das Skript schreibt durchweg groß. Bei konstantem Strom ist die Ableitung
ein einfacher Quotient:

$$Q = I\cdot t.$$

**Im Bild:** Die Anzeige der Wasseruhr — nicht die Wassermenge, die insgesamt durchgeflossen ist, sondern wie schnell sie gerade zunimmt. Trägt man
die durchgeflossene Ladung über der Zeit auf, ist der Strom die Steigung der Kurve, so wie die Geschwindigkeit die Steigung des Wegs.

:::herleitung
**Der Grenzwert** ist die Ableitung der durchgeflossenen Ladung nach der Zeit, wie im Artikel über Einheiten die Geschwindigkeit die Ableitung des Wegs.

**Konstanter Strom.** Ist die Ableitung konstant, ist die durchgeflossene Ladung eine lineare Funktion der Zeit; ab dem Start bei null ist sie
Steigung mal Zeit. Allgemein ist sie das Integral des Stroms.
:::

::::beispiel Elektronen pro Sekunde
**(a) Ein Strom von $2\,\text{A}$** bringt in jeder Sekunde $2\,\text{C}$ durch den Querschnitt, getragen von

$$\frac{2\,\text{C}}{1{,}602\cdot10^{-19}\,\text{C}} \approx 1{,}25\cdot10^{19}$$

Elektronen pro Sekunde.

**(b) Eine Stunde lang** sind das $2\,\text{A}$ mal $3600\,\text{s}$, also $7200\,\text{C}$ — in der Einheit der Akkus $2\,\text{Ah}$.

**Im Bild:** Die Wasseruhr dreht sich gleichmäßig; was in einer Stunde durchgeflossen ist, ist Anzeige mal Zeit.
::::

## Die Stromrichtung

Die __technische Stromrichtung__ wurde festgelegt, bevor man das Elektron kannte: Außerhalb der Quelle fließt der Strom vom Plus- zum Minuspol, als
wanderten positive Ladungen. In Metallen bewegen sich aber Elektronen, und die laufen genau andersherum, vom Minus- zum Pluspol.

Für den Strom macht das keinen Unterschied. Eine negative Ladung, die nach links wandert, verschiebt Ladung genauso wie eine positive, die nach rechts
wandert. Formal steckt das im Vorzeichen: Bei Elektronen ist die Raumladungsdichte negativ, und Dichte mal Geschwindigkeit ergibt einen positiven
Durchfluss gegen ihre Bewegungsrichtung. Alle Formeln der Schaltungstechnik beziehen sich auf die technische Stromrichtung; die tatsächliche Bewegung
der Elektronen braucht man nur, wenn es um das Innere des Materials geht.

**Im Bild:** Hier hinkt das Wasserbild. Das „Wasser" im Draht ist negativ geladen; die Wasseruhr zählt Elektronen, die nach links strömen, als
positiven Strom nach rechts.

:::grafik
Szene: get1/stroeme-und-spannungen/01-stromrichtungen · Vorlage: stromkreis-richtungen
Ein Stromkreis aus einer Batterie und einer Lampe. Außen am Leiter ein roter Pfeil in technischer Stromrichtung, vom Pluspol durch die Lampe zum
Minuspol; im Leiter kleine Elektronen, die langsam in Gegenrichtung wandern, mit blauen Pfeilen. Ein Umschalter zeigt dasselbe einmal mit gedachten
positiven Ladungen in technischer Richtung: Der Zähler für die Ladung rechts eines Querschnitts zeigt in beiden Fällen dieselbe Zunahme. Kernaussage:
Positive Ladung nach rechts und negative nach links sind derselbe Strom. (Rot = technische Stromrichtung, blau = Elektronen, orange = Zähler, grau =
Batterie und Lampe.)
:::

:::herleitung
Eine positive Ladung $+e$ wandert durch einen Querschnitt nach rechts: Rechts davon wächst die Ladung um $+e$. Eine negative Ladung $-e$ wandert nach
links: Rechts davon fehlt jetzt $-e$, die Ladung dort wächst also ebenfalls um $+e$. Beide Vorgänge ändern die Ladungsverteilung gleich, sie sind
derselbe Strom. In der Formel des Quaders sind bei Elektronen Dichte und Geschwindigkeit in $z$-Richtung beide negativ, ihr Produkt positiv.
:::

## Die Stromdichte

Die Stromstärke sagt, wie viel Ladung pro Zeit durch einen Querschnitt tritt, aber nicht, wie dicht gedrängt sie fließt. Das misst die __Stromdichte__,
Strom pro Fläche. Im Quader des Skripts, eindimensional in Flussrichtung und als Vektor:

:::formel Definition
$$J_z = \frac{I}{\Delta x\,\Delta y} = \rho\,v_z, \qquad \vec J = \rho\,\vec v.$$
:::

**So liest man das:** Die Stromdichte zeigt in die Richtung, in die positive Ladung strömt; ihr Betrag ist Strom pro Fläche, in Ampere pro
Quadratmeter, in der Praxis meist pro Quadratmillimeter. Bei Elektronen ist die Dichte negativ, also zeigt $\vec J$ ihrer Bewegung entgegen — in die
technische Stromrichtung. Das Skript schreibt die Stromdichte klein, $\vec j$; im Kasten steht dort im Zähler versehentlich ein $l$ statt des Stroms $I$.

Verteilt sich der Strom gleichmäßig und senkrecht über einen Querschnitt $A$, ist die Stromdichte einfach $\frac IA$. Ist er ungleich verteilt, ist der
Strom die Summe über kleine Flächenstücke $d\vec A$, jedes mit seiner Normalen als Richtung:

$$I = \int_A\vec J\cdot d\vec A.$$

**Im Bild:** An einer engen Stelle des Rohrs drängt sich derselbe Durchfluss auf weniger Fläche — die Strömung ist dort dichter.

:::herleitung
**Die Dichte am Quader.** Der Strom durch die Seitenfläche ist nach dem Abschnitt über die Raumladungsdichte $\rho\,v_z\,\Delta x\,\Delta y$; durch die
Fläche geteilt, bleibt $\rho\,v_z$. Bewegt sich die Ladung in eine beliebige Richtung, gilt das für jede Komponente, und die Komponenten bilden den
Vektor $\rho\,\vec v$.

**Das Integral.** Durch ein kleines Flächenstück trägt nur die Komponente von $\vec J$ senkrecht zur Fläche Ladung hindurch; ein Anteil parallel zur
Fläche streift an ihr entlang. Der Vektor $d\vec A$ steht senkrecht auf dem Stück und ist so lang, wie das Stück groß ist; das Skalarprodukt
$\vec J\cdot d\vec A$ ist deshalb genau der Strom durch das Stück, und die Summe über alle Stücke ist der Strom durch die ganze Fläche.
:::

::::beispiel Stromdichten im Alltag
**(a) Hausinstallation.** Eine Leitung mit $1{,}5\,\text{mm}^2$ Kupferquerschnitt, abgesichert mit $16\,\text{A}$, und eine mit $2{,}5\,\text{mm}^2$:

$$J = \frac{16\,\text{A}}{1{,}5\,\text{mm}^2} \approx 10{,}7\,\frac{\text{A}}{\text{mm}^2}, \qquad J = \frac{16\,\text{A}}{2{,}5\,\text{mm}^2} = 6{,}4\,\frac{\text{A}}{\text{mm}^2}.$$

**(b) Ein dünner Litzendraht** von $0{,}14\,\text{mm}^2$ mit $1\,\text{A}$:

$$J = \frac{1\,\text{A}}{0{,}14\,\text{mm}^2} \approx 7{,}1\,\frac{\text{A}}{\text{mm}^2}.$$

Beide Leiter sind ähnlich stark belastet, obwohl die Ströme sich um den Faktor $16$ unterscheiden. Wie stark sich ein Leiter erwärmt, hängt an der
Stromdichte, nicht am Strom allein (Kapitel 7).

**Im Bild:** Ein dickes Rohr mit großem Durchfluss und ein dünnes mit kleinem können gleich „voll" strömen.
::::

## Wie schnell wandern die Elektronen?

Aus der Stromdichte folgt, wie schnell die Ladungsträger im Mittel vorankommen. Mit der Trägerdichte $n$ und dem Betrag $n\,e$ der Raumladungsdichte
ist für einen Draht mit dem Querschnitt $A$ die __Driftgeschwindigkeit__

:::formel
$$v_\text{D} = \frac{I}{n\,e\,A}.$$
:::

**So liest man das:** Die Driftgeschwindigkeit ist die mittlere Geschwindigkeit der Träger längs des Leiters. Weil $n$ in Metallen riesig ist, ist sie
winzig — Bruchteile eines Millimeters pro Sekunde.

**Im Bild:** In einem randvollen, weiten Rohr genügt ein Kriechen für einen kräftigen Durchfluss.

:::herleitung
Bei gleichmäßiger Verteilung ist der Betrag der Stromdichte einerseits Strom durch Fläche, andererseits Betrag der Raumladungsdichte mal Geschwindigkeit:

$$\frac{I}{A} = n\,e\,v_\text{D}.$$

Nach der Geschwindigkeit aufgelöst steht die Formel da.
:::

Langsam sind die Elektronen dabei keineswegs. Ihre ungeordnete Bewegung ist sehr schnell — in Kupfer über tausend Kilometer pro Sekunde, eine Folge der
Quantenmechanik —, aber sie hebt sich im Mittel auf und transportiert nichts. Der Strom ist nur die winzige gemeinsame Vorzugsrichtung, die das Feld
dieser Bewegung aufprägt; wie das geschieht, zeigt der nächste Artikel.

**Warum das Licht trotzdem sofort angeht.** Kein Elektron muss vom Schalter zur Lampe reisen. Der Draht ist überall voller Leitungselektronen. Schließt
man den Kreis, breitet sich das antreibende Feld mit einem großen Bruchteil der Lichtgeschwindigkeit aus — in einem Kabel typisch etwa zwei Dritteln
davon —, und die Elektronen setzen sich überall praktisch gleichzeitig in Bewegung. Wie schnell genau, hängt von der Leitung ab und folgt aus der Theorie
elektromagnetischer Wellen.

**Im Bild:** Drückt man am einen Ende Wasser in das volle Rohr, tritt am anderen sofort Wasser aus — nicht dasselbe, das man hineingedrückt hat.

::::beispiel Kriechende Elektronen
Ein Kupferdraht mit $1{,}5\,\text{mm}^2$ Querschnitt führt $1\,\text{A}$. Mit der Trägerdichte von Kupfer:

$$v_\text{D} = \frac{1\,\text{A}}{8{,}49\cdot10^{28}\,\text{m}^{-3}\cdot1{,}602\cdot10^{-19}\,\text{C}\cdot1{,}5\cdot10^{-6}\,\text{m}^2} \approx 4{,}9\cdot10^{-5}\,\frac{\text{m}}{\text{s}}.$$

Knapp fünf Hundertstel Millimeter pro Sekunde. Für einen Meter Draht bräuchte ein Elektron

$$\frac{1\,\text{m}}{4{,}9\cdot10^{-5}\,\text{m}/\text{s}} \approx 2{,}0\cdot10^{4}\,\text{s},$$

gut fünfeinhalb Stunden. Das Signal, mit etwa $2\cdot10^{8}\,\frac{\text{m}}{\text{s}}$, braucht für denselben Meter fünf Nanosekunden.

**Im Bild:** Die einzelne Kugel im Rohr kommt kaum voran, der Schub am anderen Ende ist sofort da.
::::

## Wann fließt ein Strom?

Das Skript nennt zwei Bedingungen für einen dauerhaften Strom: Es muss eine __Ladungsquelle__ geben, die die Ladungen antreibt, etwa eine Batterie oder
ein Netzteil, und der __Stromkreis__ muss geschlossen sein. Ein Strom, der sich zeitlich nicht ändert, heißt __stationär__. In einem stationären Strom
fließt durch jeden Querschnitt eines unverzweigten Leiters derselbe Strom, die __Kontinuität__:

$$I_1 = I_2 \quad\text{für zwei Querschnitte desselben unverzweigten Leiters}.$$

**So liest man das:** Ladung kann sich nirgends anhäufen, solange sich nichts ändert. An einer engen Stelle sind deshalb Stromdichte und
Driftgeschwindigkeit größer, der Strom aber derselbe.

**Im Bild:** Wasser lässt sich nicht zusammendrücken. Was in ein Rohrstück hineinfließt, muss hinten wieder hinaus; schließt man ein Ventil, steht der
ganze Kreislauf.

:::herleitung
**Kontinuität.** Zwischen zwei Querschnitten ändert sich die Ladung nur, wenn hinein ein anderer Strom fließt als hinaus; ihre Änderungsrate ist die
Differenz der beiden Ströme. Nach dem Ladungserhaltungssatz kann Ladung dabei weder entstehen noch verschwinden. In einem stationären Zustand ändert
sich nichts, also ist die Differenz null.

**Geschlossener Kreis.** Wäre der Kreis offen, sammelte sich Ladung an der Unterbrechung an, wie auf den Platten eines Kondensators. Ihr Feld wüchse,
bis es dem antreibenden Feld die Waage hält, und der Strom käme zum Erliegen — kein dauerhafter Strom ohne geschlossenen Kreis.
:::

::::beispiel Eine enge Stelle
Ein Strom von $1\,\text{A}$ fließt durch einen Kupferdraht von $1{,}5\,\text{mm}^2$, der an einer Stelle auf $0{,}25\,\text{mm}^2$ verjüngt ist. Der Strom ist
überall $1\,\text{A}$, Stromdichte und Driftgeschwindigkeit aber nicht:

| Querschnitt | Stromdichte | Driftgeschwindigkeit |
|---|---|---|
| $1{,}5\,\text{mm}^2$ | $0{,}67\,\frac{\text{A}}{\text{mm}^2}$ | $0{,}049\,\frac{\text{mm}}{\text{s}}$ |
| $0{,}25\,\text{mm}^2$ | $4{,}0\,\frac{\text{A}}{\text{mm}^2}$ | $0{,}29\,\frac{\text{mm}}{\text{s}}$ |

An der engen Stelle müssen die Elektronen sechsmal so schnell wandern, damit pro Sekunde dieselbe Ladung durchkommt.

**Im Bild:** In der Engstelle des Rohrs strömt das Wasser schneller, die Wasseruhr zeigt dort aber denselben Durchfluss.
::::

## Bedeutung und Ausblick

Die Stromstärke ist die Grundgröße jeder Schaltung, und das Ampere ist eine Basiseinheit des SI. Die Stromdichte entscheidet, wie stark sich ein Leiter
erwärmt — sie bestimmt Leitungsquerschnitte und Sicherungen — und im Inneren von Halbleitern, wie die Bauelemente arbeiten. Aus der Kontinuität wird
später in diesem Kapitel die Knotenregel von Kirchhoff: An einer Verzweigung teilt sich der Strom, und die Summe bleibt erhalten.

Der nächste Artikel fragt, was die Elektronen antreibt und was sie bremst: das Feld im Leiter und die Stöße mit dem Gitter. Daraus entstehen der
Widerstand und das Ohmsche Gesetz.

:::kern
- Strom ist bewegte Ladung; __Ladungsträger__ sind in Metallen Leitungselektronen, in Lösungen Ionen, in Halbleitern auch Löcher.
- Die __Raumladungsdichte__ ist $\rho=\frac{\Delta Q}{\Delta V}$; der Durchfluss durch eine Fläche ist Dichte mal Geschwindigkeit mal Fläche.
- __Stromstärke__: $I=\frac{dQ}{dt}$, Einheit Ampere; bei konstantem Strom ist die Ladung Strom mal Zeit.
- Die __technische Stromrichtung__ zählt positive Ladung von Plus nach Minus; Elektronen laufen entgegen, mit demselben Ergebnis.
- __Stromdichte__: $\vec J=\rho\,\vec v$, Strom pro Fläche; bei Elektronen zeigt sie gegen ihre Bewegung.
- Die __Driftgeschwindigkeit__ $v_\text{D}=\frac{I}{neA}$ ist in Metallen winzig, Bruchteile eines Millimeters pro Sekunde.
- Das Licht geht trotzdem sofort an: Das antreibende Feld breitet sich fast mit Lichtgeschwindigkeit aus.
- Dauerhafter Strom braucht eine Quelle und einen geschlossenen Kreis; durch jeden Querschnitt eines unverzweigten Leiters fließt derselbe Strom.
:::

:::quiz
F: Was zählt die Stromstärke anschaulich, und warum ist sie als Grenzwert definiert?
A: Sie zählt, wie viel Ladung pro Zeit durch einen Querschnitt tritt, wie die Anzeige einer Wasseruhr. Weil sich der Strom im Allgemeinen ändert, nimmt man den Grenzwert $\frac{dQ}{dt}$, den Wert im Augenblick; im Ladung-Zeit-Diagramm ist er die Steigung. Nur bei konstantem Strom ist die Ladung einfach Strom mal Zeit.
F: Wie hängen Raumladungsdichte, Geschwindigkeit und Durchfluss am Quader zusammen?
A: In der Zeit $\Delta t$ treten durch die Seitenfläche alle Ladungen einer Säule der Länge $v_z\Delta t$, also $\rho\,\Delta x\,\Delta y\,v_z\,\Delta t$. Der Durchfluss ist deshalb $\rho\,v_z\,\Delta x\,\Delta y$ — Dichte mal Geschwindigkeit mal Fläche.
F: Warum ist ein Kupferdraht neutral, obwohl jeder Kubikzentimeter über $13\,000\,\text{C}$ bewegliche Ladung enthält?
A: Jedes Kupferatom gibt ein Leitungselektron ab und bleibt als positiver Atomrumpf im Gitter zurück. Die Raumladungsdichte der Elektronen von etwa $-1{,}36\cdot10^{10}\,\frac{\text{C}}{\text{m}^3}$ wird von den Rümpfen genau ausgeglichen. Wandern die Elektronen, bleibt der Draht neutral — es fließt nur Ladung hindurch.
F: Wie viele Elektronen tragen einen Strom von $2\,\text{A}$, und was bedeuten $2\,\text{Ah}$?
A: Zwei Coulomb pro Sekunde, geteilt durch die Elementarladung, sind rund $1{,}25\cdot10^{19}$ Elektronen pro Sekunde. $2\,\text{Ah}$ sind die Ladung, die $2\,\text{A}$ in einer Stunde transportieren, also $7200\,\text{C}$.
F: Warum darf man mit der technischen Stromrichtung rechnen, obwohl Elektronen andersherum laufen?
A: Eine negative Ladung, die nach links wandert, ändert die Ladungsverteilung genauso wie eine positive nach rechts: Rechts wächst die Ladung in beiden Fällen um $+e$. In der Formel sind bei Elektronen Dichte und Geschwindigkeit beide negativ, ihr Produkt positiv. Deshalb gelten alle Formeln mit der Richtung von Plus nach Minus.
F: Was ist die Stromdichte, und in welche Richtung zeigt sie bei Elektronen?
A: Strom pro Fläche, als Vektor $\vec J=\rho\vec v$; bei gleichmäßiger Verteilung $\frac IA$, allgemein ist der Strom das Integral von $\vec J$ über die Fläche. Bei Elektronen ist $\rho$ negativ, $\vec J$ zeigt also ihrer Bewegung entgegen, in die technische Stromrichtung. Eine Leitung von $1{,}5\,\text{mm}^2$ mit $16\,\text{A}$ hat etwa $10{,}7\,\frac{\text{A}}{\text{mm}^2}$.
F: Wie schnell driften die Elektronen bei $1\,\text{A}$ in einem Kupferdraht von $1{,}5\,\text{mm}^2$, und warum so langsam?
A: Aus $\frac IA=n\,e\,v_\text{D}$ folgt $v_\text{D}=\frac{I}{neA}\approx4{,}9\cdot10^{-5}\,\frac{\text{m}}{\text{s}}$, knapp fünf Hundertstel Millimeter pro Sekunde; für einen Meter bräuchte ein Elektron über fünf Stunden. So langsam, weil die Trägerdichte von rund $8{,}5\cdot10^{28}\,\text{m}^{-3}$ riesig ist: Sehr viele Träger teilen sich den Strom.
F: Warum leuchtet die Lampe sofort, obwohl die Elektronen so langsam kriechen?
A: Kein Elektron muss vom Schalter zur Lampe reisen; der Draht ist überall voller Leitungselektronen. Das antreibende Feld breitet sich mit einem großen Bruchteil der Lichtgeschwindigkeit aus, in Kabeln etwa zwei Drittel davon, und setzt alle praktisch gleichzeitig in Bewegung — ein Meter dauert etwa fünf Nanosekunden. Wie bei einem vollen Wasserrohr tritt am Ende sofort etwas aus.
F: Welche Bedingungen braucht ein dauerhafter Strom, und warum fließt durch jeden Querschnitt eines unverzweigten Leiters derselbe Strom?
A: Eine Quelle, die die Ladungen antreibt, und einen geschlossenen Kreis; bei einer Unterbrechung sammelte sich Ladung an, deren Feld den Strom stoppt. Zwischen zwei Querschnitten ändert sich die Ladung um die Differenz der Ströme; im stationären Zustand ändert sich nichts, also sind die Ströme gleich — die Kontinuität, ein Fall der Ladungserhaltung.
F: Was ändert sich an einer engen Stelle eines Leiters, und was bleibt gleich?
A: Der Strom bleibt derselbe, denn Ladung häuft sich nicht an. Stromdichte und Driftgeschwindigkeit wachsen mit dem Kehrwert des Querschnitts: Verjüngt sich ein Draht mit $1\,\text{A}$ von $1{,}5$ auf $0{,}25\,\text{mm}^2$, steigt die Stromdichte von $0{,}67$ auf $4\,\frac{\text{A}}{\text{mm}^2}$, und die Elektronen wandern sechsmal so schnell.
:::
