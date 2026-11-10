---
title: Stufe 2: Die Kapazität
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130300
summary: Wie viel Ladung hält eine bestimmte Spannung auf den Platten?
tags: 
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Wie viel Ladung hält eine bestimmte Spannung auf den Platten? Die Antwort ist eine einzige Zahl je Bauteil.
:::

**Die Idee.** Verdoppelt man die Ladung auf beiden Platten, trägt jede Ladung ihr Feld doppelt bei. Nach der Überlagerung aus [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) verdoppelt sich das Feld an jedem Ort, seine Form bleibt gleich (Abb. [2](#abb-2) links). Die Spannung ist das Integral des Felds von Platte zu Platte, also verdoppelt sie sich auch. $Q$ und $U$ sind deshalb proportional. Ihr Verhältnis hängt nicht davon ab, wie viel Ladung gerade da ist, sondern nur von Form, Abstand und Stoff.

:::definition Definition 2.1 (Kapazität)
<span class="anker" id="satz-2-1"></span>

Die Kapazität eines Kondensators ist das Verhältnis von Ladung und Spannung:

<span class="anker" id="gl-2-1"></span>
$$C=\frac{Q}{U},\qquad Q=C\,U,\qquad[C]=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F\ \text{(Farad)}. \tag{2.1}$$
:::

⁠**So liest man das:** $Q$ ist die Ladung der positiven Platte in C (Coulomb), $U$ die Spannung zwischen den Platten in V, $C$ die Kapazität in F. Bei 1 F hält ein Volt ein Coulomb. Das ist sehr viel. Übliche Werte liegen bei fF, pF, nF und µF, Elektrolytkondensatoren reichen bis in den mF-Bereich. Die Formelzeichen nicht verwechseln: Kursiv ist $C$ die Kapazität, aufrecht ist C das Coulomb. **Gültigkeit:** [(2.1)](#gl-2-1) setzt voraus, dass der Stoff zwischen den Platten sich mit dem Feld nicht ändert. Keramik mit sehr großem $\varepsilon_\mathrm{r}$ (Stufe [4](plattenkondensator-und-dielektrikum.html#stufe-4)) verliert bei hoher Spannung merklich an Kapazität.

:::abbildung et1/k3qu 2
Links: Doppelte Ladung ergibt doppelt so dichte Feldlinien und damit die doppelte Spannung. Rechts: Die Ladung wächst proportional zur Spannung, die Steigung der Geraden ist die Kapazität. Die Punkte gehören zu 9 V.
:::

::::beispiel
Das Plattenpaar hat $C=29{,}5$ pF (Stufe [4](plattenkondensator-und-dielektrikum.html#stufe-4)). Bei 9 V trägt es $Q=29{,}5\,\mathrm{pF}\cdot9\,\mathrm{V}=266$ pC, das sind $1{,}66\cdot10^{9}$ Elektronen. Eine 1 mm dicke Kupferplatte dieser Fläche enthält $8{,}5\cdot10^{23}$ freie Elektronen. Es wandert also nur eines von $5\cdot10^{14}$, und diese sitzen auf der Innenseite der Platte. Das Metall bleibt praktisch unverändert. Der Kondensator des RC-Kreises trägt bei 9 V $Q=900\,\mu\text{C}$, 3,4 Millionen Mal mehr.
::::

⁠**Grenzfall:** Für $U=0$ ist $Q=0$: Ohne Spannung ist nichts getrennt. Bei gleicher Ladung zeigt der kleinere Kondensator die größere Spannung.

:::frage Kapazität klingt nach Fassungsvermögen. Ist ein Kondensator irgendwann voll?
Nicht im Sinn eines Eimers. Mehr Spannung bringt immer mehr Ladung, $C$ bleibt dabei gleich. Die Grenze setzt das Dielektrikum: Über einer bestimmten Feldstärke schlägt es durch. Voll heißt in diesem Kapitel nur: Die Spannung hat die der Quelle erreicht.
:::

:::aufgabe Aufgabe 2 ★ Ladung und Spannung
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Ein Kondensator mit 470 nF liegt an 12 V. Wie groß ist seine Ladung?

</li>

<li>

Bei welcher Spannung trägt er 1 µC?

</li>

<li>

Die Spannung wird halbiert. Was geschieht mit $Q$ und mit $C$?

</li>

<li>

Zwei Kondensatoren mit 10 µF und 1 µF tragen je 50 µC. Welche Spannungen liegen an ihnen?

</li>

</ol>

:::loesung
(a) $Q=470\,\mathrm{nF}\cdot12\,\mathrm{V}=5{,}64\,\mu\text{C}$.

(b) $U=Q/C=1\,\mu\text{C}/470\,\mathrm{nF}=2{,}13$ V.

(c) $Q$ halbiert sich auf 2,82 µC. $C$ bleibt gleich, denn es hängt nur vom Bauteil ab.

(d) $U=Q/C$: 5 V am 10-µF-Kondensator, 50 V am 1-µF-Kondensator. Dieselbe Ladung erzeugt am kleineren die größere Spannung.
:::
:::
