---
title: Stufe 2: Langsame Elektronen, sofortiger Strom
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
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
Aus $F=m_\mathrm e\,a$ und $F=e\,E$ ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)) folgt die Beschleunigung $a=e\,E/m_\mathrm e$. Ein Flug beginnt beim gerichteten Anteil null, also $v(t)=a\,t$ und $v_\mathrm{max}=a\,T$. Der Sägezahn hat den Mittelwert $v_\mathrm{max}/2=e\,E\,T/(2\,m_\mathrm e)$. Die Geschwindigkeit wächst nicht weiter an, denn jeder Stoß setzt sie zurück.
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

:::frage Teil 1 sagt: Im Metall ist $\vec E=0$. Warum gibt es im Draht ein Feld, und wie folgt es den Kurven?
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
