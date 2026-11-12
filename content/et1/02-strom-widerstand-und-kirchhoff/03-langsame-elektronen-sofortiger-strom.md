---
title: Stufe 2: Langsame Elektronen, sofortiger Strom
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1120300
summary: Stufe 1 braucht eine Geschwindigkeit v .
tags: Kristallgitter, Beweglichkeit, mittlere freie Weglänge
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Stufe [1](strom-ist-bewegte-ladung.html#stufe-1) braucht eine Geschwindigkeit $v$. Diese Stufe zeigt, warum sie konstant und winzig ist, und löst den Widerspruch zur Lampe, die sofort leuchtet.
:::

**Die Idee.** In einem Metall ist je Atom mindestens ein Elektron nicht mehr an sein Atom gebunden. Die zurückbleibenden positiven Ionen bilden ein regelmäßiges __Kristallgitter__. Liegt eine Spannung an, herrscht im Draht ein Feld. Es beschleunigt jedes freie Elektron gegen die Feldrichtung. Nach kurzer Zeit wird das Elektron gestreut und gibt die gewonnene gerichtete Geschwindigkeit an das Gitter ab, dann beginnt es von vorn (Abb. [2](#abb-2)). Im Mittel bleibt eine konstante Geschwindigkeit: Die Stöße nehmen genau so viel, wie das Feld gibt.

:::abbildung et1/k2drift 2
Links: Bahn eines Elektrons im Gitter (schematisch, nicht maßstäblich). Rechts: Modell für den gerichteten Anteil der Geschwindigkeit. Er wächst im Feld bis $v_\mathrm{max}$ und fällt beim Stoß auf null. Sein Mittelwert ist die Driftgeschwindigkeit $v_\mathrm D=v_\mathrm{max}/2$.
:::

:::satz Satz 2.1 (Driftgeschwindigkeit)
<span class="anker" id="satz-2-1"></span>

Dauert jeder Flug zwischen zwei Stößen die Zeit $T$, so ist

<span class="anker" id="gl-2-1"></span>
$$|\vec v_\mathrm{max}|=\frac{e\,|\vec E|}{m_\mathrm e}\,T,\qquad\vec v_\mathrm D=-\mu\,\vec E,\qquad\mu=\frac{e\,T}{2\,m_\mathrm e}. \tag{2.1}$$

Mit Stufe [1](strom-ist-bewegte-ladung.html#stufe-1) folgt aus dem Strom $v_\mathrm D=j/(n\,e)=I/(n\,e\,A)$.
:::

⁠**So liest man das:** $\vec v_\mathrm D$ ist die Driftgeschwindigkeit in m/s. Das Minuszeichen sagt: Elektronen sind negativ, sie laufen gegen $\vec E$. $\mu$ ist die __Beweglichkeit__, die Driftgeschwindigkeit je Feldstärke, in $\mathrm{m^2/(V\,s)}$. Sie ist eine Materialkonstante, im Kupfer $4{,}3\cdot10^{-3}\,\mathrm{m^2/(V\,s)}$. $T$ ist die Flugzeit, im Kupfer rund 49 fs. Das Elektron legt in dieser Zeit im Mittel die __mittlere freie Weglänge__ $\lambda$ zurück. **Gültigkeit:** [(2.1)](#gl-2-1) ist ein Modell. Es zählt nur den vom Feld erzeugten Anteil der Geschwindigkeit. Daneben fliegen die Elektronen ungeordnet in alle Richtungen, mit rund 1600 km/s. Diese Bewegung hebt sich im Mittel auf, trägt keinen Strom und bleibt bei den Stößen erhalten.

:::herleitung Vom Feld zur Drift
Aus $F=m_\mathrm e\,a$ und $F=e\,E$ ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)) folgt die Beschleunigung $a=e\,E/m_\mathrm e$. Ein Flug beginnt beim gerichteten Anteil null, also $v(t)=a\,t$ und $v_\mathrm{max}=a\,T$. Der Sägezahn hat den Mittelwert $v_\mathrm{max}/2=e\,E\,T/(2\,m_\mathrm e)$. Die Geschwindigkeit wächst nicht weiter an, denn jeder Stoß setzt sie zurück.
:::

::::beispiel
Im Draht ist $v_\mathrm D=j/(n\,e)=6\cdot10^3\,\mathrm{A/m^2}/(1{,}36\cdot10^{10}\,\mathrm{C/m^3})=4{,}4\cdot10^{-7}$ m/s, also 0,44 µ m/s. Für einen Meter bräuchte ein Elektron 26 Tage. Das Feld im Draht ist $E=v_\mathrm D/\mu=0{,}10$ mV/m. Die Drift ist so klein, weil der Draht so viele Ladungsträger enthält: 6800 C je Meter müssen nur 3 mC je Sekunde liefern.
::::

⁠**Kurz gesagt:** Die Driftgeschwindigkeit ist der Strom geteilt durch die freie Ladung je Meter. **Grenzfälle:** Ohne Feld ist $v_\mathrm D=0$. Doppelter Strom ergibt doppelte Drift. Viele Stöße ($T\to0$) ergeben $\mu\to0$: Das Material leitet nicht.

**Warum der Strom trotzdem sofort da ist.** Zwei Dinge wandern im Draht, und sie dürfen nicht verwechselt werden. Die Elektronen driften langsam. Das Feld dagegen breitet sich beim Schließen des Schalters als elektromagnetische Welle längs des Drahts aus, in Kabeln mit rund $2\cdot10^8$ m/s. Die Elektronen sitzen schon überall im Draht. Jedes beginnt zu driften, sobald die Feldfront es erreicht (Abb. [3](#abb-3)). Nach wenigen solchen Laufzeiten fließt im ganzen Kreis der stationäre Strom. Die Energie reist mit dem Feld, nicht mit den Elektronen. Für einen Meter braucht die Front 5 ns. In diesen 5 ns driftet ein Elektron 2,2 fm, das ist rund 100 000-mal weniger als der Abstand zweier Kupferatome. Die beiden Geschwindigkeiten unterscheiden sich um den Faktor $4{,}5\cdot10^{14}$.

:::abbildung et1/k2sofort 3
Ein Meter Draht in drei Momenten nach dem Schließen des Schalters links. Die Feldfront durchläuft ihn in 5 ns. Hinter der Front driften alle Elektronen, davor ruhen sie im Mittel. Die Elektronen selbst sind in dieser Zeit praktisch nicht vorangekommen.
:::

:::analogie
Eine Fahrradkette ist überall voller Glieder. Tritt man vorn, bewegt sie sich hinten im selben Moment, obwohl jedes Glied nur langsam läuft. Die Analogie endet beim Mechanismus: Kettenglieder drücken einander mechanisch, die Wirkung läuft mit Schallgeschwindigkeit durch das Metall. Im Draht läuft ein Feld, und seine Geschwindigkeit liegt nahe der Lichtgeschwindigkeit.
:::

:::frage Kapitel 1 sagt: Im Metall ist $\vec E=0$. Warum gibt es im Draht ein Feld, und wie folgt es den Kurven?
$\vec E=0$ gilt nur im Ruhezustand, wenn alle Ladungen zur Ruhe gekommen sind. Die Quelle lässt das nicht zu: Sie führt an einem Ende Elektronen ab und am anderen zu, der Ruhezustand wird nie erreicht. Es bleibt ein kleines Feld, hier 0,10 mV/m. An Biegungen sammeln sich winzige Ladungen auf der Drahtoberfläche. Ihr Feld lenkt $\vec E$ überall in Drahtrichtung, sonst liefen die Elektronen gegen die Wand, und die Ladung dort würde weiter wachsen.
:::

:::zusatz Wie schnell Elektronen wirklich sind
Die ungeordnete Bewegung ist $3{,}6\cdot10^{12}$-mal schneller als die Drift im Draht. Sie ist eine Folge der Quantenmechanik und bleibt selbst nahe dem absoluten Nullpunkt erhalten. Die Flugzeiten streuen, und mit gestreuten Zeiten fällt der Faktor $\frac12$ in $\mu$ weg, wenn $T$ die mittlere Flugzeit ist. Dann ist $T=25$ fs, und die freie Weglänge $\lambda$ beträgt rund 39 nm, etwa 150 Atomabstände. Das Bild „Stoß mit jedem Atom“ ist also zu grob: Ein vollkommenes, ruhendes Gitter streut Elektronen gar nicht. Sie stoßen an Gitterschwingungen, Fremdatomen und Fehlstellen.
:::

:::aufgabe Aufgabe 2 ★★ Drift und Laufzeit
<span class="anker" id="aufg-2"></span>

Das Kabel aus Aufgabe [1](strom-ist-bewegte-ladung.html#aufg-1) ist aus Kupfer und 30 m lang.

<ol class="al">

<li>

Berechne $v_\mathrm D$ und das Feld $E=\rho\,j$ im Kabel.

</li>

<li>

Wie lange bräuchte ein Elektron für die 30 m, wie lange die Feldfront?

</li>

<li>

Vorhersage: Wie ändert sich $v_\mathrm D$, wenn der Querschnitt bei gleichem Strom doppelt so groß wird?

</li>

</ol>

:::loesung
(a) $j=1{,}07\cdot10^7\,\mathrm{A/m^2}$, $v_\mathrm D=j/(n\,e)=0{,}78$ mm/s. $E=\rho\,j=0{,}18$ V/m.

(b) Elektron: $30\,\mathrm{m}/0{,}78\,\mathrm{mm/s}=3{,}8\cdot10^4$ s $=10{,}6$ h. Feldfront: $30\,\mathrm{m}/(2\cdot10^8\,\mathrm{m/s})=150$ ns.

(c) Sie halbiert sich: Doppelt so viele Ladungsträger je Meter teilen sich denselben Strom, $v_\mathrm D=I/(n\,e\,A)$.
:::
:::

::::formelsammlung
**Höchste gerichtete Geschwindigkeit**

$$|\vec v_\mathrm{max}|=\frac{e\,|\vec E|}{m_\mathrm e}\,T$$

Am Ende eines Flugs der Dauer $T$ zwischen zwei Stößen, Beschleunigung $a=e\,E/m_\mathrm e$. Jeder Stoß setzt den gerichteten Anteil wieder auf null.

**Driftgeschwindigkeit und Beweglichkeit**

$$\vec v_\mathrm D=-\mu\,\vec E,\qquad\mu=\frac{e\,T}{2\,m_\mathrm e}$$

$\vec v_\mathrm D$ ist der Mittelwert des Sägezahns, $v_\mathrm D=v_\mathrm{max}/2$; Elektronen laufen gegen $\vec E$. $\mu$ Beweglichkeit in $\mathrm{m^2/(V\,s)}$, eine Materialkonstante. Das Modell zählt nur den vom Feld erzeugten Anteil der Geschwindigkeit; die ungeordnete Bewegung trägt keinen Strom.

**Driftgeschwindigkeit aus dem Strom**

$$v_\mathrm D=j/(n\,e)=I/(n\,e\,A)$$

$n$ Dichte der freien Elektronen, $A$ Querschnitt: der Strom geteilt durch die freie Ladung je Meter. Die Drift ist winzig, weil der Draht sehr viele Ladungsträger enthält; der Strom ist trotzdem sofort da, weil sich das Feld mit rund $2\cdot10^8$ m/s ausbreitet.
::::

::::lernkarten
:::karte begriff Kristallgitter
Was ist das Kristallgitter eines Metalls, in dem sich die freien Elektronen bewegen?
---
Die regelmäßige Anordnung der positiven Ionen, die zurückbleiben, weil je Atom mindestens ein Elektron nicht mehr gebunden ist.
--- falsch
Die regelmäßige Anordnung der freien Elektronen, die zwischen den neutralen Atomen fest auf ihren Plätzen sitzen und dort nur schwingen.
--- falsch
Ein Netz aus feinen Kanälen im Metall, durch das die freien Elektronen fließen, ohne je an Atome zu stoßen.
--- falsch
Die regelmäßige Anordnung der neutralen Atome, deren Elektronen alle fest an ihr eigenes Atom gebunden bleiben.
:::
:::karte begriff Driftgeschwindigkeit
Was versteht man unter der Driftgeschwindigkeit der Elektronen in einem Draht?
---
Die mittlere Geschwindigkeit längs des Leiters, die das Feld den Elektronen zwischen den Stößen gibt. Sie ist dem Feld proportional, $\vec v_\mathrm D=-\mu\,\vec E$.
--- falsch
Die Geschwindigkeit, mit der sich das Feld beim Einschalten längs des Drahts ausbreitet. Sie liegt nahe der Lichtgeschwindigkeit.
--- falsch
Die ungeordnete Geschwindigkeit, mit der die Elektronen in alle Richtungen fliegen. Sie beträgt rund 1600 km/s und trägt den Strom.
--- falsch
Die größte Geschwindigkeit, die ein Elektron kurz vor einem Stoß erreicht. Sie wächst mit jedem weiteren Flug immer weiter an, solange das Feld im Draht wirkt.
:::
:::karte begriff Beweglichkeit
Was gibt die Beweglichkeit $\mu$ der Elektronen in einem Metall an, und wovon hängt sie im Stoßmodell ab?
---
Die Driftgeschwindigkeit je Feldstärke, in $\mathrm{m^2/(V\,s)}$; eine Materialkonstante. Im Modell ist $\mu=\frac{e\,T}{2\,m_\mathrm e}$, sie wächst mit der Flugzeit $T$ zwischen zwei Stößen.
--- falsch
Die Driftgeschwindigkeit je Feldstärke, in $\mathrm{m^2/(V\,s)}$; eine Materialkonstante. Im Modell ist $\mu=\frac{2\,m_\mathrm e}{e\,T}$, sie sinkt mit der Flugzeit $T$ zwischen zwei aufeinanderfolgenden Stößen.
--- falsch
Die Zahl der freien Elektronen je Volumen, in $\mathrm{m^{-3}}$; eine Materialkonstante. Je mehr Elektronen im Metall frei sind, desto größer ist sie.
--- falsch
Die ungeordnete Geschwindigkeit der Elektronen, in m/s. Sie hängt von der angelegten Spannung ab und ist deshalb keine Materialkonstante.
:::
:::karte begriff mittlere freie Weglänge
Was ist die mittlere freie Weglänge eines Elektrons in einem Metall?
---
Der Weg, den ein Elektron im Mittel zwischen zwei Stößen zurücklegt, also während einer Flugzeit. Er ist viel länger als der Abstand zweier Atome.
--- falsch
Der Abstand zweier benachbarter Atome im Kristallgitter, weil ein Elektron im Metall an jedem Atom stößt, an dem es vorbeikommt.
--- falsch
Der Weg, den ein Elektron je Sekunde längs des Drahts driftet, also seine Driftgeschwindigkeit mal einer Sekunde. Er ist deshalb dem Strom proportional.
--- falsch
Der Weg, den die Feldfront beim Einschalten zurücklegt, bevor ein Elektron zu driften beginnt. Er ist so lang wie der ganze Draht.
:::
:::karte formel Driftgeschwindigkeit im Stoßmodell
Welche Driftgeschwindigkeit ergibt das Stoßmodell, wenn jeder Flug zwischen zwei Stößen die Zeit $T$ dauert?
---
$\vec v_\mathrm D=-\mu\,\vec E$ mit $\mu=\frac{e\,T}{2\,m_\mathrm e}$. Das Minuszeichen sagt: Elektronen laufen gegen $\vec E$.
--- falsch
$\vec v_\mathrm D=\mu\,\vec E$ mit $\mu=\frac{e\,T}{2\,m_\mathrm e}$. Elektronen laufen also in Richtung von $\vec E$ wie jede Ladung.
--- falsch
$\vec v_\mathrm D=-\mu\,\vec E$ mit $\mu=\frac{e\,T}{m_\mathrm e}$. Das ist die Geschwindigkeit kurz vor dem Stoß, die über den Flug gleich bleibt.
--- falsch
$\vec v_\mathrm D=-\frac{e\,\vec E}{m_\mathrm e}\,t$. Die Geschwindigkeit wächst mit der Zeit $t$ immer weiter, solange das Feld anliegt.
:::
:::karte formel Drift aus dem Strom
Wie berechnet man die Driftgeschwindigkeit aus dem Strom $I$ in einem Draht mit dem Querschnitt $A$ und der Elektronendichte $n$?
---
$v_\mathrm D=j/(n\,e)=I/(n\,e\,A)$: Man teilt den Strom durch die freie Ladung je Meter Draht, $n\,e\,A$. Doppelter Strom ergibt doppelte Drift.
--- falsch
$v_\mathrm D=I\,n\,e/A$: Je mehr freie Elektronen der Draht enthält, desto schneller laufen sie bei gleichem Strom.
--- falsch
$v_\mathrm D=I/(n\,e)$: Der Querschnitt spielt keine Rolle, weil der Strom in jedem Draht gleich schnell fließt.
--- falsch
$v_\mathrm D=I\,A/(n\,e)$: Ein dickerer Draht führt denselben Strom mit schnelleren Elektronen, weil sie mehr Platz haben.
:::
:::karte herleitung Vom Feld zur Drift
Leite aus $F=e\,E$ und dem Stoßmodell her, dass die Driftgeschwindigkeit $v_\mathrm D=e\,E\,T/(2\,m_\mathrm e)$ beträgt.
---
Aus $F=m_\mathrm e\,a$ und $F=e\,E$ folgt die Beschleunigung $a=e\,E/m_\mathrm e$, weil zwischen zwei Stößen nur die Feldkraft das Elektron beschleunigt.
---
Ein Flug beginnt beim gerichteten Anteil null, also $v(t)=a\,t$ und $v_\mathrm{max}=a\,T$, weil der vorige Stoß die gewonnene gerichtete Geschwindigkeit an das Gitter abgegeben hat.
---
Der gerichtete Anteil wächst in jedem Flug gleichmäßig von 0 bis $v_\mathrm{max}$ und fällt dann auf null, weil die Beschleunigung konstant ist; er bildet einen Sägezahn.
---
Der Sägezahn hat den Mittelwert $v_\mathrm{max}/2=e\,E\,T/(2\,m_\mathrm e)$, weil eine gleichmäßig wachsende Größe im Mittel den halben Endwert hat. Er wächst nicht weiter an, weil jeder Stoß ihn zurücksetzt.
:::
:::karte zusammenhang Konstante Drift
Warum wird ein Elektron im Draht nicht immer schneller, obwohl das Feld es ständig beschleunigt?
---
Weil es nach kurzer Zeit gestreut wird und die gewonnene gerichtete Geschwindigkeit an das Gitter abgibt. Die Stöße nehmen im Mittel genau so viel, wie das Feld gibt.
--- falsch
Weil das Feld im Draht nur beim Einschalten wirkt. Danach rollen die Elektronen ohne Antrieb mit der einmal erreichten Geschwindigkeit weiter.
--- falsch
Weil die Elektronen schon nach kurzer Zeit eine Grenzgeschwindigkeit nahe der Lichtgeschwindigkeit erreichen. Schneller als die Feldfront können sie im Draht nicht werden.
--- falsch
Weil sich die Elektronen gegenseitig abstoßen. Die Kraft der vorderen Elektronen bremst jedes folgende genau auf die Driftgeschwindigkeit ab.
:::
:::karte zusammenhang Kleine Drift
Woran liegt es, dass die Elektronen in einem Kupferdraht mit $0{,}5\,\mathrm{mm^2}$ bei 3 mA nur mit 0,44 µ m/s driften?
---
An der riesigen Zahl freier Ladungsträger: Ein Meter Draht enthält 6800 C freie Ladung, für 3 mA müssen davon nur 3 mC je Sekunde vorbeikommen.
--- falsch
An den vielen Stößen: Jedes Elektron prallt an jedem einzelnen Atom ab und kommt deshalb kaum voran, gleich wie viele Elektronen im Draht frei sind.
--- falsch
An der großen Masse der Elektronen: Sie sind so schwer, dass das schwache Feld im Draht sie zwischen den Stößen kaum beschleunigen kann.
--- falsch
An der Isolation des Drahts: Sie hält die Elektronen zurück, damit sie nicht aus dem Draht austreten, und bremst sie dabei ab.
:::
:::karte zusammenhang Strom ist sofort da
Warum leuchtet eine Lampe sofort beim Einschalten, obwohl die Elektronen im Draht nur langsam driften?
---
Weil nicht die Elektronen vom Schalter zur Lampe laufen, sondern das Feld, mit rund $2\cdot10^8$ m/s. Die Elektronen sitzen schon überall und driften los, sobald die Feldfront sie erreicht.
--- falsch
Weil beim Einschalten einzelne Elektronen sehr schnell vom Schalter zur Lampe fliegen und sie zum Leuchten bringen. Erst wenn sie angekommen sind, stellt sich die langsame Drift ein.
--- falsch
Weil die ungeordnete Bewegung der Elektronen mit rund 1600 km/s die Energie zur Lampe trägt. Die langsame Drift spielt für das Leuchten keine Rolle.
--- falsch
Weil jedes Elektron mechanisch gegen das nächste drückt wie die Glieder einer Kette. Die Wirkung läuft so mit Schallgeschwindigkeit durch das Metall.
:::
:::karte zusammenhang Feld im Draht
Warum gibt es im stromdurchflossenen Draht ein Feld, obwohl im Metall in Ruhe $\vec E=0$ gilt?
---
Weil die Quelle keinen Ruhezustand zulässt: Sie führt an einem Ende Elektronen ab und am anderen zu. Ladungen an Biegungen lenken das kleine Restfeld in Drahtrichtung.
--- falsch
Weil das Feld der Quelle durch die Isolation in den Draht dringt. In einem blanken Metall ohne Isolation wäre $\vec E=0$ auch dann, wenn Strom fließt.
--- falsch
Weil die Elektronen beim Driften ein eigenes Feld erzeugen, das mit ihrer Geschwindigkeit wächst. Ruhende Elektronen erzeugen dagegen kein Feld, dann ist $\vec E=0$.
--- falsch
Weil die Quelle so stark ist, dass sie die Abschirmung des Metalls überwindet. Eine schwache Quelle erzeugt im Draht weder Feld noch Strom.
:::
::::
