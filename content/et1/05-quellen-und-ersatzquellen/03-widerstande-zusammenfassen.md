---
title: Stufe 1: Widerstände zusammenfassen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Quellen und Ersatzquellen
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
