---
title: Stufe 1: Widerstände zusammenfassen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1150300
summary: Ein Netz aus Widerständen ohne Quelle hat an zwei Klemmen eine Kennlinie durch den Ursprung, also genügt eine Zahl.
tags: Gruppenschaltung, Gesamtwiderstand, Leitwert
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Netz aus Widerständen ohne Quelle hat an zwei Klemmen eine Kennlinie durch den Ursprung, also genügt eine Zahl. Diese Stufe findet sie durch schrittweises Zusammenfassen.
:::

**Die Idee.** Eine __Gruppenschaltung__ besteht aus Reihen- und Parallelgruppen, die ineinanderstecken. Zwei Widerstände liegen in Reihe, wenn an ihrem gemeinsamen Knoten nichts anderes angeschlossen ist. Dann fließt durch beide derselbe Strom, die Ladung kann nirgends abbiegen. Sie liegen parallel, wenn sie an denselben zwei Knoten hängen. Dann liegt an beiden dieselbe Spannung. Jede solche Gruppe ist selbst ein kleines Eintor mit einem Widerstand als Kennlinie. Man ersetzt sie durch diesen Widerstand, und der Rest der Schaltung merkt nichts davon. Das wiederholt man von innen nach außen.

:::abbildung et1/k5gruppe 1
Links ein Last-Netz aus sechs Widerständen. Die drei gestapelten liegen parallel und ergeben 10 $\Omega$, zusammen mit $R_\mathrm{c}$ in Reihe 15 $\Omega$. Rechts das Netz nach diesen zwei Schritten.
:::

:::definition Definition 1.1 (Gesamtwiderstand)
<span class="anker" id="satz-1-1"></span>

Der __Gesamtwiderstand__ $R_\mathrm{AB}$ ist das Verhältnis $U_\mathrm{AB}/I_\mathrm{A}$ eines Eintors ohne Quelle. Für das Netz aus Abb. [1](#abb-1) gilt

<span class="anker" id="gl-1-1"></span>
$$R_\mathrm{AB}=R_\mathrm{a}+R_\mathrm{b}\parallel\bigl(R_\mathrm{c}+R_\mathrm{d}\parallel R_\mathrm{e}\parallel R_\mathrm{f}\bigr) =R_\mathrm{a}+\left[G_\mathrm{b}+\frac{1}{R_\mathrm{c}+\dfrac{1}{G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}}}\right]^{-1}. \tag{1.1}$$
:::

⁠**So liest man das:** $R$ ist ein Widerstand in $\Omega$, $G=1/R$ sein __Leitwert__ in Siemens (S). In Reihe addiert man Widerstände, parallel addiert man Leitwerte. In der zweiten Form steht deshalb jede Parallelgruppe als Summe von Leitwerten. Die eckige Klammer mit dem Exponenten $-1$ kehrt das Ergebnis wieder um. **Gültigkeit:** Das Verfahren braucht echte Gruppen. Hängt an einem Zwischenknoten ein dritter Zweig, liegen die zwei Nachbarn nicht mehr in Reihe (Stufe [2](symmetrie-nutzen.html#stufe-2) und [3](stern-und-dreieck.html#stufe-3)).

::::beispiel
Mit den Werten aus Abb. [1](#abb-1): $G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}=50+33{,}3+16{,}7$ mS $=100$ mS, das sind 10 $\Omega$. Dazu in Reihe $R_\mathrm{c}$: 15 $\Omega$. Parallel zu $R_\mathrm{b}$: $30\,\Omega\parallel15\,\Omega=10\,\Omega$. Dazu in Reihe $R_\mathrm{a}$: $R_\mathrm{AB}=16\,\Omega$. Die Rückrechnung liefert die Ströme: Bei 8 V an A und B fließen 0,5 A. An $R_\mathrm{a}$ fallen 3 V ab, es bleiben 5 V für den Rest. Durch $R_\mathrm{b}$ fließen $5\,\mathrm{V}/30\,\Omega=166{,}7$ mA, durch $R_\mathrm{c}$ fließen $5\,\mathrm{V}/15\,\Omega=333{,}3$ mA. Die Summe ist 500 mA.
::::

⁠**Grenzfall:** Für $R_\mathrm{b}\to0$ wird [(1.1)](#gl-1-1) zu $R_\mathrm{AB}=R_\mathrm{a}=6\,\Omega$. Der Kurzschluss überbrückt alles dahinter, die Ladung nimmt den Draht.

:::frage Darf ich die Schritte in beliebiger Reihenfolge machen?
Nein. Eine Gruppe entsteht oft erst, wenn die innere Gruppe zusammengefasst ist: $R_\mathrm{c}$ und $R_\mathrm{b}$ liegen im Ausgangsbild nicht parallel, weil zwischen ihnen die drei gestapelten Widerstände hängen. Deshalb arbeitet man von der klemmenfernsten Gruppe zu den Klemmen.
:::

:::aufgabe Aufgabe 1 ★ Das Last-Netz verändern
<span class="anker" id="aufg-1"></span>

Gehe vom Netz aus Abb. [1](#abb-1) aus. Welches $R_\mathrm{AB}$ ergibt sich, wenn (a) $R_\mathrm{b}$ durch einen Leitungsbruch wegfällt, (b) $R_\mathrm{c}$ kurzgeschlossen wird, (c) $R_\mathrm{d}$ kurzgeschlossen wird, (d) $R_\mathrm{f}$ wegfällt? Sage vor dem Rechnen voraus, welche der vier Änderungen am wenigsten bewirkt.

:::loesung
Vorhersage: Am wenigsten bewirkt (d), denn $R_\mathrm{f}$ ist der größte Widerstand seiner Parallelgruppe und führt den kleinsten Strom.

(a) $R_\mathrm{AB}=6\,\Omega+15\,\Omega=21\,\Omega$. (b) $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel10\,\Omega=13{,}5\,\Omega$. (c) Die ganze Parallelgruppe ist überbrückt: $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel5\,\Omega=10{,}29\,\Omega$. (d) $20\,\Omega\parallel30\,\Omega=12\,\Omega$, also $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel17\,\Omega=16{,}85\,\Omega$.
:::
:::

::::formelsammlung
**Gesamtwiderstand**

$$R_\mathrm{AB}=\frac{U_\mathrm{AB}}{I_\mathrm{A}}$$

Verhältnis von Klemmenspannung und Klemmenstrom eines Eintors ohne Quelle. Ohne Quelle geht die Kennlinie durch den Ursprung, eine Zahl reicht.

**Leitwert**

$$G=1/R$$

$G$ in Siemens (S), $R$ in $\Omega$. In Reihe addiert man Widerstände (gleicher Strom), parallel addiert man Leitwerte (gleiche Spannung).

**Gesamtwiderstand des Last-Netzes**

$$R_\mathrm{AB}=R_\mathrm{a}+R_\mathrm{b}\parallel\bigl(R_\mathrm{c}+R_\mathrm{d}\parallel R_\mathrm{e}\parallel R_\mathrm{f}\bigr)=R_\mathrm{a}+\left[G_\mathrm{b}+\frac{1}{R_\mathrm{c}+\dfrac{1}{G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}}}\right]^{-1}$$

Netz aus sechs Widerständen: $R_\mathrm{d}$, $R_\mathrm{e}$, $R_\mathrm{f}$ parallel, dazu $R_\mathrm{c}$ in Reihe, das Ganze parallel zu $R_\mathrm{b}$, davor $R_\mathrm{a}$. In der zweiten Form steht jede Parallelgruppe als Summe von Leitwerten, die Klammer mit dem Exponenten $-1$ kehrt um. Man fasst von der klemmenfernsten Gruppe zu den Klemmen zusammen. Gilt nur für echte Gruppen: Hängt an einem Zwischenknoten ein dritter Zweig, liegen die Nachbarn nicht in Reihe. Für $R_\mathrm{b}\to0$ wird $R_\mathrm{AB}=R_\mathrm{a}$.
::::

::::lernkarten
:::karte begriff Gruppenschaltung
Woraus besteht eine Gruppenschaltung von Widerständen, und wie bestimmt man ihren Widerstand an den Klemmen?
---
Aus Reihen- und Parallelgruppen, die ineinanderstecken. Jede Gruppe ist ein kleines Eintor mit einem Widerstand als Kennlinie; man ersetzt sie durch diesen Widerstand und wiederholt das von innen nach außen.
--- falsch
Aus Widerständen, die alle parallel zwischen denselben zwei Knoten liegen. Man addiert ihre Widerstände in beliebiger Reihenfolge und erhält so den Widerstand zwischen den Klemmen in einem einzigen Schritt.
--- falsch
Aus Widerständen, die nach gleichen Werten sortiert sind. Man fasst jeweils die gleichen zusammen, gleich wo sie im Netz liegen, und addiert die Ergebnisse der einzelnen Gruppen.
--- falsch
Aus Reihen- und Parallelgruppen, die ineinanderstecken. Man fasst sie von den Klemmen aus nach innen zusammen, weil die Gruppen an den Klemmen den meisten Strom führen.
:::
:::karte zusammenhang Reihenschaltung
Woran erkennt man, dass zwei Widerstände in Reihe liegen, und warum fließt dann durch beide derselbe Strom?
---
An ihrem gemeinsamen Knoten ist nichts anderes angeschlossen. Die Ladung kann dort nirgends abbiegen, deshalb fließt durch beide derselbe Strom.
--- falsch
Sie sind in der Zeichnung hintereinander auf einer Linie gezeichnet. Derselbe Strom folgt daraus, dass beide denselben Widerstandswert haben.
--- falsch
Sie hängen an denselben zwei Knoten. Dann liegt an beiden dieselbe Spannung, und nach dem ohmschen Gesetz fließt durch beide derselbe Strom.
--- falsch
An ihrem gemeinsamen Knoten hängt noch ein dritter Zweig. Dieser Zweig gleicht die Ströme aus, sodass durch beide derselbe Strom fließt.
:::
:::karte zusammenhang Parallelschaltung
Woran erkennt man, dass zwei Widerstände parallel liegen, und was haben sie dann gemeinsam?
---
Sie hängen an denselben zwei Knoten. Dann liegt an beiden dieselbe Spannung, und man fasst sie zusammen, indem man ihre Leitwerte addiert.
--- falsch
An ihrem gemeinsamen Knoten ist nichts anderes angeschlossen. Dann liegt an beiden dieselbe Spannung, und man addiert ihre Widerstände.
--- falsch
Sie hängen an denselben zwei Knoten. Dann fließt durch beide derselbe Strom, und man fasst sie zusammen, indem man ihre Widerstände addiert.
--- falsch
Sie sind in der Zeichnung nebeneinander und gleich lang gezeichnet. Dann fließt durch beide derselbe Strom, und man addiert ihre Leitwerte.
:::
:::karte begriff Leitwert
Was ist der Leitwert eines Widerstands, und wofür ist er beim Zusammenfassen von Widerständen nützlich?
---
Der Kehrwert des Widerstands, $G=1/R$, in Siemens (S). Parallel addiert man Leitwerte, so wie man in Reihe Widerstände addiert.
--- falsch
Der Kehrwert des Widerstands, $G=1/R$, in Siemens (S). In Reihe addiert man Leitwerte, parallel addiert man dagegen Widerstände.
--- falsch
Der Widerstand je Meter Leitung, in $\Omega$/m. Man braucht ihn, um die Drähte zwischen den Gruppen beim Zusammenfassen mitzuzählen.
--- falsch
Das Produkt aus Widerstand und Strom, in Volt. Parallel addiert man Leitwerte, weil an allen Zweigen dieselbe Spannung liegt.
:::
:::karte begriff Gesamtwiderstand
Was gibt der Gesamtwiderstand $R_\mathrm{AB}$ eines Eintors ohne Quelle an, und warum reicht für ein solches Eintor diese eine Zahl?
---
Das Verhältnis $U_\mathrm{AB}/I_\mathrm{A}$ an den Klemmen. Ohne Quelle geht die Kennlinie durch den Ursprung, also legt eine einzige Zahl sie fest.
--- falsch
Die Summe aller Widerstände im Netz, gleich wie sie verschaltet sind. Sie reicht, weil jeder Widerstand vom ganzen Klemmenstrom durchflossen wird.
--- falsch
Das Verhältnis $U_\mathrm{AB}/I_\mathrm{A}$, das sich mit dem Strom ändert. Eine Zahl reicht nur für einen bestimmten Strom, die Kennlinie ist eine Kurve.
--- falsch
Den größten Widerstand im Netz, weil er den Strom begrenzt. Die übrigen Widerstände sind daneben vernachlässigbar, also reicht eine Zahl.
:::
:::karte formel Gesamtwiderstand mit Leitwerten
Wie schreibt man den Gesamtwiderstand $R_\mathrm{AB}=R_\mathrm{a}+R_\mathrm{b}\parallel\bigl(R_\mathrm{c}+R_\mathrm{d}\parallel R_\mathrm{e}\parallel R_\mathrm{f}\bigr)$ mit Leitwerten, und warum sieht die Form so aus?
---
$R_\mathrm{AB}=R_\mathrm{a}+\left[G_\mathrm{b}+\frac{1}{R_\mathrm{c}+\dfrac{1}{G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}}}\right]^{-1}$. Jede Parallelgruppe steht als Summe von Leitwerten, der Exponent $-1$ kehrt das Ergebnis wieder um.
--- falsch
$R_\mathrm{AB}=R_\mathrm{a}+\left[G_\mathrm{b}+R_\mathrm{c}+G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}\right]^{-1}$. Alle Glieder hinter $R_\mathrm{a}$ stehen in einer Summe; die eckige Klammer kehrt das Ergebnis einmal um, das genügt für jede Tiefe.
--- falsch
$R_\mathrm{AB}=\left[G_\mathrm{a}+G_\mathrm{b}+G_\mathrm{c}+G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}\right]^{-1}$. In der Leitwertform addiert man alle Leitwerte, gleich ob sie in Reihe oder parallel liegen, und kehrt am Ende um.
--- falsch
$R_\mathrm{AB}=R_\mathrm{a}+G_\mathrm{b}+R_\mathrm{c}+G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}$. Leitwerte und Widerstände darf man mischen, solange jede Gruppe in ihrer eigenen Form steht.
:::
:::karte zusammenhang Reihenfolge beim Zusammenfassen
Warum darf man beim Zusammenfassen einer Gruppenschaltung die Schritte nicht in beliebiger Reihenfolge machen?
---
Eine Gruppe entsteht oft erst, wenn die innere zusammengefasst ist: Im Last-Netz liegen $R_\mathrm{c}$ und $R_\mathrm{b}$ anfangs nicht parallel, weil dazwischen die drei gestapelten Widerstände hängen. Man arbeitet daher von der klemmenfernsten Gruppe zu den Klemmen.
--- falsch
Weil sich das Ergebnis mit der Reihenfolge ändert: Wer an den Klemmen beginnt, erhält einen größeren Widerstand als wer innen beginnt. Deshalb ist eine Reihenfolge fest vorgeschrieben, damit alle, die dasselbe Netz rechnen, dasselbe Ergebnis erhalten.
--- falsch
Weil man sonst die Leitwerte falsch addiert: Man muss zuerst alle Reihengruppen und danach alle Parallelgruppen zusammenfassen, gleich wo sie im Netz liegen.
--- falsch
Weil man an den Klemmen beginnen muss: Dort fließt der ganze Strom, und nur so kennt man ihn, bevor man ihn auf die inneren Gruppen verteilt und weiter nach innen rechnet.
:::
:::karte zusammenhang Kurzschluss im Last-Netz
Was wird aus dem Gesamtwiderstand des Last-Netzes, wenn $R_\mathrm{b}\to0$ geht, und warum?
---
$R_\mathrm{AB}=R_\mathrm{a}=6\,\Omega$. Der Kurzschluss überbrückt alles dahinter, die Ladung nimmt den Draht.
--- falsch
$R_\mathrm{AB}=0$, weil ein Kurzschluss irgendwo im Netz jeden Widerstand zwischen den Klemmen auf null bringt.
--- falsch
Er bleibt 16 $\Omega$, weil ein Widerstand von null Ohm keinen Beitrag liefert und deshalb nichts ändert.
--- falsch
$R_\mathrm{AB}=R_\mathrm{a}+R_\mathrm{c}$, weil nur die Parallelgruppe überbrückt wird und $R_\mathrm{c}$ weiter in Reihe liegt.
:::
:::karte zusammenhang Grenze des Zusammenfassens
Wann reicht das schrittweise Zusammenfassen von Reihen- und Parallelgruppen nicht mehr aus?
---
Wenn es keine echten Gruppen gibt: Hängt an einem Zwischenknoten ein dritter Zweig, liegen die zwei Nachbarn nicht mehr in Reihe, und die Regeln für Reihe und Parallel greifen nicht.
--- falsch
Wenn die Widerstände verschieden groß sind: Nur gleiche Widerstände lassen sich zu Reihen- oder Parallelgruppen zusammenfassen, verschiedene muss man einzeln rechnen.
--- falsch
Wenn ein Widerstand kurzgeschlossen ist: Ein Draht im Netz zerstört jede Gruppe, und man muss das Netz ohne ihn neu zeichnen, bevor man weiterrechnen kann.
--- falsch
Wenn zwei Widerstände an denselben zwei Knoten hängen, weil dann nicht klar ist, ob sie in Reihe oder parallel liegen, und sich die Regeln für Reihe und Parallel widersprechen.
:::
::::
