---
title: Stufe 3: Die Kraft zwischen Ladungen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
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

::::formelsammlung
**Coulomb-Gesetz**

$$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}$$

Betrag der Kraft zwischen zwei punktförmigen, ruhenden Ladungen im Abstand $r$, im Vakuum (in Luft nur 0,06 % kleiner). Gleichnamige Ladungen stoßen sich ab, ungleichnamige ziehen sich an. $\varepsilon_0=8{,}854\cdot10^{-12}$ A s/(V m) ist die elektrische Feldkonstante.

**Coulomb-Kraft als Vektor**

$$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}$$

Kraft auf A, Ladungen mit Vorzeichen; $\vec r$ zeigt von B nach A, $\vec r/r$ hat die Länge 1. Für $Q_\mathrm{A}Q_\mathrm{B}>0$ zeigt $\vec F_\mathrm{A}$ von B weg. Beide Ladungen spüren gleich große, entgegengesetzte Kräfte; mehrere Ladungen wirken unabhängig, ihre Kräfte addieren sich als Vektoren.

**Kraftmessung mit dem Pendel**

$$\tan\alpha=F/(m\,g)$$

Ausschlag $\alpha$ einer Kugel der Masse $m$ am Faden, wenn die elektrische Kraft $F$ waagerecht wirkt.
::::

::::lernkarten
:::karte formel Coulomb-Gesetz
Wie groß ist die Kraft zwischen zwei Ladungen $Q_\mathrm{A}$ und $Q_\mathrm{B}$ im Abstand $r$?
---
$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r^2}$ mit $k=\frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}$. Gilt für ruhende Punktladungen im Vakuum; in Luft ist die Kraft nur um 0,06 % kleiner.
--- falsch
$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r}$ mit $k=\frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}$. Gilt für ruhende Punktladungen im Vakuum; in Luft ist die Kraft nur um 0,06 % kleiner.
--- falsch
$F=k\,\frac{|Q_\mathrm{A}+Q_\mathrm{B}|}{r^2}$ mit $k=\frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}$. Gilt für ruhende Punktladungen im Vakuum; in Luft ist die Kraft nur um 0,06 % kleiner.
--- falsch
$F=k\,\frac{|Q_\mathrm{A}\,Q_\mathrm{B}|}{r^2}$ mit $k=\frac{1}{4\pi\varepsilon_0}=8{,}99\cdot10^{9}\,\frac{\mathrm{N\,m^2}}{\mathrm{C^2}}$. Gilt für ruhende Körper jeder Größe; $r$ ist der kleinste Abstand ihrer Oberflächen.
:::
:::karte formel Coulomb-Gesetz als Vektor
Wie lautet die Coulomb-Kraft auf Ladung A als Vektor, und woran erkennt man darin Anziehung oder Abstoßung?
---
$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}$, $\vec r$ zeigt von B nach A. Gleichnamig ist $Q_\mathrm{A}Q_\mathrm{B}>0$, die Kraft zeigt von B weg: Abstoßung. Ungleichnamig zeigt sie zu B hin: Anziehung.
--- falsch
$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}$, $\vec r$ zeigt von A nach B. Gleichnamig ist $Q_\mathrm{A}Q_\mathrm{B}>0$, die Kraft zeigt zu B hin: Anziehung. Ungleichnamig zeigt sie von B weg: Abstoßung.
--- falsch
$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}$, $\vec r$ zeigt von B nach A. Es entscheidet der Betrag von $\vec r/r$: Ist er größer als 1, stoßen sich die Ladungen ab, ist er kleiner, ziehen sie sich an.
--- falsch
$\vec F_\mathrm{A}=k\,\frac{Q_\mathrm{A}\,Q_\mathrm{B}}{r^2}\cdot\frac{\vec r}{r}$, $\vec r$ zeigt von B nach A. Es entscheidet allein das Vorzeichen von $Q_\mathrm{A}$: Ist A positiv, wird A abgestoßen, ist A negativ, angezogen.
:::
:::karte begriff Punktladung
Was versteht man unter einer Punktladung, wie sie das Coulomb-Gesetz voraussetzt?
---
Ein geladener Körper, der klein gegen den Abstand $r$ zu den anderen Ladungen ist. Für ruhende Punktladungen gilt das Coulomb-Gesetz.
--- falsch
Eine Ladung von genau einer Elementarladung, also ein einzelnes Elektron oder Proton. Nur für sie gilt das Coulomb-Gesetz.
--- falsch
Ein geladener Körper, der an einem festen Punkt gehalten wird, sodass ihn die Kraft der anderen Ladungen nicht verschieben kann.
--- falsch
Ein geladener Körper beliebiger Größe, dessen Ladung sich in dem Punkt seiner Oberfläche sammelt, der der anderen Ladung am nächsten liegt.
:::
:::karte begriff Überlagerung
Wie bestimmt man nach dem Prinzip der Überlagerung die Kraft auf eine Ladung, wenn mehrere andere Ladungen auf sie wirken?
---
Mehrere Ladungen wirken unabhängig voneinander: Die Kraft auf eine Ladung ist die Vektorsumme der Kräfte, die jede andere Ladung allein auf sie ausüben würde.
--- falsch
Mehrere Ladungen wirken unabhängig voneinander: Die Kraft auf eine Ladung ist die Summe der Beträge der Einzelkräfte, gleich in welche Richtung diese zeigen.
--- falsch
Mehrere Ladungen verdecken einander: Auf eine Ladung wirkt nur die Kraft der nächstgelegenen Ladung, die weiter entfernten tragen nichts bei.
--- falsch
Mehrere Ladungen verstärken einander: Die Kraft auf eine Ladung wächst mit dem Produkt aller anderen Ladungen, nicht mit der Summe ihrer Einzelkräfte.
:::
:::karte zusammenhang Gleiche Kraft auf beide
Kugel B trägt doppelt so viel Ladung wie Kugel A. Warum spüren beide trotzdem eine gleich große Kraft?
---
Weil beide Ladungen gleichberechtigt in $F=k\,|Q_\mathrm{A}Q_\mathrm{B}|/r^2$ eingehen: ein Produkt, ein Abstand, also ein Betrag für beide, in entgegengesetzter Richtung. Die leichtere Kugel wird nur stärker beschleunigt.
--- falsch
Weil sich die Ladungen beim Annähern angleichen: B gibt die Hälfte seines Überschusses an A ab, bis beide Kugeln gleich viel Ladung tragen und deshalb gleich große Kräfte spüren, auch ohne sich zu berühren.
--- falsch
Weil die Kraft nur vom Abstand abhängt: Beide Kugeln sind gleich weit voneinander entfernt, die Ladungen bestimmen nur, ob sie sich anziehen oder abstoßen, nicht wie stark.
--- falsch
Weil die Gravitation den Unterschied ausgleicht: Sie zieht die schwächer geladene Kugel A zusätzlich zu B hin, bis die Kraft auf A genauso groß ist wie die auf B.
:::
:::karte zusammenhang Abstand und Ladung
Was passiert mit der Coulomb-Kraft, wenn man den Abstand verdoppelt, und was, wenn man eine der beiden Ladungen verdoppelt?
---
Doppelter Abstand ergibt ein Viertel der Kraft, weil sie mit $1/r^2$ fällt. Doppelte Ladung ergibt die doppelte Kraft, weil sie proportional zu jeder der beiden Ladungen wächst.
--- falsch
Doppelter Abstand ergibt die halbe Kraft, weil sie mit $1/r$ fällt. Doppelte Ladung ergibt die doppelte Kraft, weil sie proportional zu jeder der beiden Ladungen wächst.
--- falsch
Doppelter Abstand ergibt ein Viertel der Kraft, weil sie mit $1/r^2$ fällt. Doppelte Ladung ergibt die vierfache Kraft, weil die beiden Ladungen als Produkt eingehen.
--- falsch
Doppelter Abstand ergibt ein Viertel der Kraft, weil sie mit $1/r^2$ fällt. Doppelte Ladung ändert nichts, solange die andere Ladung gleich bleibt.
:::
:::karte zusammenhang Gravitation vernachlässigbar
Zwei Kugeln von je 1 g tragen $+10$ nC und $-20$ nC und sind 3 cm voneinander entfernt. Warum darf man die Gravitation zwischen ihnen vernachlässigen?
---
Weil sie verschwindend klein ist: Die elektrische Kraft beträgt 2,0 mN, die Gravitation nur $7{,}4\cdot10^{-14}$ N, also $2{,}7\cdot10^{10}$-mal weniger. Dabei fehlt bei Kugel A nur eines von $5\cdot10^{12}$ Elektronen.
--- falsch
Weil Gravitation nur zwischen ungeladenen Körpern wirkt. Sobald eine der Kugeln geladen ist, verschwindet die Anziehung ihrer Massen, und es bleibt allein die elektrische Kraft.
--- falsch
Weil Gravitation und elektrische Kraft hier in entgegengesetzte Richtungen zeigen. Sie heben sich gegenseitig auf, deshalb darf man beide Kräfte zugleich weglassen.
--- falsch
Weil die Gravitation mit $1/r^3$ fällt und bei 3 cm Abstand schon fast null ist. Die elektrische Kraft fällt dagegen nur mit $1/r^2$ und bleibt deshalb übrig.
:::
:::karte zusammenhang Exponent 2 gemessen
Warum gilt der Exponent 2 im Coulomb-Gesetz als gesichert?
---
Weil Messungen ihn immer genauer bestätigt haben: Setzt man $F\sim1/r^{2\pm\delta}$ an, sank die Grenze für $\delta$ von 0,02 bei Cavendish auf $3\cdot10^{-16}$ im Jahr 1971.
--- falsch
Weil er aus $F=m\,a$ folgt, wenn man in der Mechanik die Masse durch die Ladung ersetzt. Messungen sind dafür nicht nötig, der Exponent ergibt sich aus der Rechnung.
--- falsch
Weil Ladungen eine besondere Form von Masse sind. Deshalb muss für sie derselbe Exponent gelten wie im Gravitationsgesetz, das ihn schon vorgibt.
--- falsch
Weil er um 1750 so festgelegt wurde, damit die Einheit Coulomb einfach wird. Er ist eine Vereinbarung wie die Namen positiv und negativ, kein Messergebnis.
:::
::::
