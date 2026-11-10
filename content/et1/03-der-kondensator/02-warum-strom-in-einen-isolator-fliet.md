---
title: Stufe 1: Warum Strom in einen Isolator fließt
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130200
summary: Die Platten berühren sich nicht.
tags: 
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die Platten berühren sich nicht. Trotzdem zeigt ein Messgerät in der Zuleitung Strom. Diese Stufe klärt, welche Ladung sich dabei wohin bewegt.
:::

**Die Idee.** Das ungeladene Plattenpaar wird über Drähte an die Batterie gelegt (Abb. [1](#abb-1)). Im ersten Moment liegen beide Platten auf demselben Potenzial, die Batteriepole aber 9 V auseinander. Das Potenzialgefälle liegt also längs der Drähte. Dort herrscht ein Feld, und es schiebt die freien Elektronen im Metall. Im Draht an Platte A laufen sie von der Platte weg zum Pluspol, im Draht an Platte B vom Minuspol auf die Platte. A verliert Elektronen und wird positiv, B gewinnt Elektronen und wird negativ. Kein Elektron überquert die Lücke: Jedes Elektron, das auf B ankommt, stammt aus dem Draht davor, nicht von A.

Mit jeder verschobenen Ladung wächst zwischen den Platten das Feld und damit die Spannung. Die Platten rücken im Potenzial an ihre Pole heran, das Gefälle längs der Drähte schrumpft, der Strom nimmt ab. Bei 9 V zwischen den Platten liegt jede Platte auf dem Potenzial ihres Pols. Längs der Drähte bleibt kein Gefälle, auf die Elektronen wirkt keine Kraft mehr, und der Strom endet.

:::abbildung et1/k3aufbau 1
Links: das Plattenpaar beim Laden. Elektronen laufen von Platte A zum Pluspol, ebenso viele vom Minuspol auf Platte B. Der Strom $i$ zählt in Richtung positiver Ladung, also gegen die Elektronen, und ist in beiden Zuleitungen gleich. Durch den Isolator läuft keine Ladung, dort steht das Feld $E$. Rechts: das Schaltzeichen mit Zählpfeilen.
:::

:::definition Definition 1.1 (Kondensator)
<span class="anker" id="satz-1-1"></span>

Ein Kondensator besteht aus zwei Elektroden, die ein Dielektrikum trennt. Seine Ladung $Q$ ist die Ladung der positiven Elektrode, die andere trägt $-Q$. Strom durch den Kondensator heißt: An einem Anschluss fließt ein Strom hinein, am anderen im selben Moment derselbe Strom heraus.
:::

⁠**So liest man das:** Geladen heißt: Ladung ist getrennt, nicht hinzugefügt. Die Gesamtladung bleibt null. Jede Feldlinie, die auf A beginnt, endet auf B ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Typisch sind Ladungen von Nanocoulomb bis Millicoulomb. **Gültigkeit:** Das Dielektrikum gilt als idealer Isolator, Stufe [5](bauformen-und-selbstentladung.html#stufe-5) nennt die Abweichung.

:::herleitung Warum an beiden Anschlüssen derselbe Strom fließt
Angenommen, es fließt mehr hinein als heraus. Dann sammelt sich im Bauteil eine Nettoladung $Q_\mathrm{n}$, und das ganze Bauteil hebt sich im Potenzial gegen seine Umgebung. Wie stark, zeigt eine Kugel von der Größe eines Gehäuses, $r=1$ cm: Nach [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) hat sie das Potenzial $\varphi=k\,Q_\mathrm{n}/r$, und schon 1 µC ergäbe 900 kV. Das Feld dieser Ladung bremst den Zufluss, lange bevor ein messbarer Unterschied entsteht. Also bleibt $Q_\mathrm{n}$ praktisch null, und die Knotenregel aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) gilt für das Bauteil als Ganzes.
:::

:::analogie
Im Rohr eines Wasserkreises sitzt quer eine Gummihaut. Die Pumpe drückt Wasser dagegen, die Haut dehnt sich. Auf beiden Seiten bewegt sich Wasser, durch die Haut geht keines. Ihr Gegendruck wächst mit der Dehnung, und wenn er den Pumpendruck erreicht, steht das Wasser. Das Bild endet bei der Energie: Die Haut speichert sie im Gummi, der Kondensator im Feld zwischen den Platten (Stufe [6](die-gespeicherte-energie.html#stufe-6)).
:::

::::beispiel
Ein Messgerät in der Zuleitung zu A zeigt 0,1 s lang konstant 0,9 mA. Dann sind $Q=I\,t=90\,\mu\text{C}$ verschoben, das sind $5{,}6\cdot10^{14}$ Elektronen. Sie haben A verlassen, ebenso viele sind auf B angekommen. Ein Messgerät in der Zuleitung zu B zeigt dieselben 0,9 mA.
::::

⁠**Grenzfall:** Liegen die Platten schon auf den Potenzialen der Pole, ist das Gefälle längs der Drähte null und damit auch der Strom. Ein auf 9 V geladener Kondensator zieht aus einer 9-V-Batterie keinen Strom.

:::frage Fließt der Strom nun durch den Kondensator oder nicht?
Durch die Zuleitungen ja, durch die Lücke nein. Von außen sieht man nur die Anschlüsse: Am einen geht Strom hinein, am anderen kommt derselbe Strom heraus. Für die Schaltung sieht das aus wie ein durchgehender Strom, deshalb die kurze Redeweise. Er dauert aber nur, solange sich die Ladung ändert.
:::

:::frage Warum bleibt die Ladung sitzen, wenn man die Batterie abklemmt?
Die Elektronen auf B werden von A angezogen, aber der Isolator lässt sie nicht durch, und die Drahtenden sind offen. Ein Weg entsteht erst, wenn ein Leiter die Anschlüsse verbindet (Stufe [10](entladen-und-zeitkonstante.html#stufe-10)).
:::

:::aufgabe Aufgabe 1 ★ Was die Messgeräte zeigen
<span class="anker" id="aufg-1"></span>

In der Zuleitung zu Platte A eines Kondensators zeigt ein Messgerät 2 s lang konstant 0,45 mA.

<ol class="al">

<li>

Wie viel Ladung ist verschoben, und wie viele Elektronen sind das?

</li>

<li>

Was zeigt ein Messgerät in der Zuleitung zu Platte B? Wie groß ist danach die Gesamtladung des Kondensators?

</li>

<li>

Wie viele Elektronen haben den Isolator durchquert?

</li>

</ol>

:::loesung
(a) $Q=I\,t=0{,}45\,\mathrm{mA}\cdot2\,\mathrm{s}=900\,\mu\text{C}$, also $N=Q/e=5{,}6\cdot10^{15}$ Elektronen.

(b) Ebenfalls 0,45 mA: Was bei A hineinfließt, fließt bei B heraus. Die Gesamtladung bleibt null, A trägt $+900\,\mu\text{C}$, B trägt $-900\,\mu\text{C}$.

(c) Keines. Die Elektronen auf B kommen aus dem Draht, die Elektronen von A sind in den Draht gelaufen.
:::
:::
