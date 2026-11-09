---
title: Stufe 3: Die Kraft zwischen Ladungen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Ladung, Feld und Potenzial
order: 1110500
summary: Geladene Körper üben Kräfte aufeinander aus.
tags: elektrische Feldkonstante, Punktladungen, Überlagerung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Geladene Körper üben Kräfte aufeinander aus. Diese Stufe macht aus „ziehen sich an“ ein Gesetz mit Zahlen.
:::

**Die Idee.** Man hängt eine geladene Kugel an einen Faden und stellt eine zweite, entgegengesetzt geladene daneben (Abb. [4](#abb-4)). Die Anziehung zieht die Kugel aus der Senkrechten, die Schwerkraft zurück, der Ausschlag verrät die Kraft: $\tan\alpha=F/(m\,g)$. Verändert man Ladungen und Abstand, zeigt sich: Die Kraft wächst proportional zu jeder der beiden Ladungen und fällt mit dem Quadrat des Abstands. Dieselbe Form hat das Gravitationsgesetz [(1.2)](groen-kraft-und-arbeit.html#gl-1-2), mit Ladungen statt Massen.

:::abbildung et1/k1pendel 4
Links: Kugel A am Faden neben Kugel B, Kräfte maßstäblich. Gewichtskraft $m\,g=9{,}81$ mN, elektrische Kraft $F=2{,}0$ mN und Fadenkraft $F_0=10{,}0$ mN heben sich auf, $\alpha=11{,}5^\circ$. Rechts: Coulomb-Kraft im Rechenmodell. Doppelter Abstand ergibt ein Viertel der Kraft.
:::

:::satz Satz 3.1 (Coulomb-Gesetz)
<span class="anker" id="satz-3-1"></span>

Zwei punktförmige, ruhende Ladungen im Abstand $r$ üben aufeinander Kräfte vom Betrag

<span class="anker" id="gl-3-1"></span>
$$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}} \tag{3.1}$$

aus. Als Vektor lautet die Kraft auf A, wobei $\vec r$ von B nach A zeigt,

<span class="anker" id="gl-3-2"></span>
$$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}. \tag{3.2}$$
:::

⁠**So liest man das:** $Q_\mathrm{A}$, $Q_\mathrm{B}$ sind die Ladungen in C, in [(3.2)](#gl-3-2) mit Vorzeichen, $r$ der Abstand in m. Der Vektor $\vec r/r$ hat die Länge 1 und gibt nur die Richtung an. $\varepsilon_0=8{,}854\cdot10^{-12}$ A s/(V m) heißt __elektrische Feldkonstante__. Bei gleichnamigen Ladungen ist $Q_\mathrm{A}Q_\mathrm{B}>0$, $\vec F_\mathrm{A}$ zeigt von B weg: Abstoßung. Bei ungleichnamigen zeigt es zu B hin: Anziehung. **Gültigkeit:** Die Körper müssen klein gegen $r$ sein (__Punktladungen__) und ruhen. Das Gesetz gilt im Vakuum, in Luft ist die Kraft nur um 0,06 % kleiner. Mehrere Ladungen wirken unabhängig, ihre Kräfte addieren sich als Vektoren (__Überlagerung__).

:::herleitung Vom Experiment zum Gesetz
Das Gesetz ist ein Messergebnis. Die Versuchsreihen ergeben einzeln $F\sim Q_\mathrm{A}$, $F\sim Q_\mathrm{B}$, $F\sim1/r^2$ und $\vec F\parallel\vec r$, zusammen $F\sim Q_\mathrm{A}Q_\mathrm{B}/r^2$, der Faktor ist $k$. Setzt man $F\sim1/r^{2\pm\delta}$ an, sank die Grenze für $\delta$ von 0,02 bei Cavendish (18. Jahrhundert) über $5\cdot10^{-5}$ bei Maxwell (19. Jahrhundert) auf $10^{-13}$ (Bartlett und andere, 1970) und $3\cdot10^{-16}$ (Williams und andere, 1971).
:::

::::beispiel
Im Rechenmodell ist

$$F=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}\cdot\frac{10\cdot10^{-9}\,\mathrm{C}\cdot20\cdot10^{-9}\,\mathrm{C}}{(0{,}03\,\mathrm{m})^2}=2{,}0\,\mathrm{mN}.$$

Die Gewichtskraft der Kugel A ist 9,81 mN, also $\tan\alpha=0{,}204$ und $\alpha=11{,}5^\circ$. Diesen Ausschlag erzeugt das Fehlen eines Elektrons unter $5\cdot10^{12}$. Die Gravitation zwischen zwei 1-g-Kugeln im selben Abstand beträgt nur $7{,}4\cdot10^{-14}$ N, sie ist um den Faktor $2{,}7\cdot10^{10}$ kleiner und darf entfallen. Zwischen zwei Elektronen ist die elektrische Kraft sogar $4{,}2\cdot10^{42}$-mal größer.
::::

⁠**Grenzfälle:** Für $r\to\infty$ geht $F\to0$. Für $Q_\mathrm{A}=0$ ist $F=0$. Doppelter Abstand ergibt 0,5 mN, doppelte Ladung $Q_\mathrm{A}$ ergibt 4,0 mN.

:::frage Kugel B trägt doppelt so viel Ladung wie Kugel A. Spürt A deshalb die größere Kraft?
Nein, beide spüren dieselben 2,0 mN in entgegengesetzter Richtung, denn in [(3.1)](#gl-3-1) gehen beide Ladungen gleichberechtigt ein. Verschieden sein kann die Wirkung: Die leichtere Kugel wird stärker beschleunigt.
:::

:::aufgabe Aufgabe 3 ★★ Coulomb-Kraft
<span class="anker" id="aufg-3"></span>

Zwei kleine Metallkugeln tragen $+2$ nC und $+5$ nC im Abstand 2 cm.

<ol class="al">

<li>

Wie groß ist die Kraft, und wohin zeigt sie auf jede Kugel?

</li>

<li>

Was ergibt sich beim dreifachen Abstand? Antworte erst ohne Taschenrechner.

</li>

<li>

Die gleich großen Kugeln berühren sich kurz und werden wieder auf 2 cm gebracht. Welche Kraft wirkt nun? Warum ist sie nicht gleich geblieben, obwohl die Gesamtladung es ist?

</li>

</ol>

:::loesung
(a) $F=k\cdot2\,\mathrm{nC}\cdot5\,\mathrm{nC}/(2\,\mathrm{cm})^2=225$ µ N. Gleichnamig: Jede Kugel wird von der anderen weggedrückt. (b) Dreifacher Abstand ergibt ein Neuntel: 25 µ N.

(c) Jede Kugel trägt nun $+3{,}5$ nC, also $F=k\,(3{,}5\,\mathrm{nC})^2/(2\,\mathrm{cm})^2=275$ µ N. Die Kraft hängt vom Produkt der Ladungen ab, nicht von der Summe: $3{,}5\cdot3{,}5=12{,}25$ gegen $2\cdot5=10$.
:::
:::
