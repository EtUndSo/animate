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

::::formelsammlung
**Ladung der beiden Elektroden**

$$Q+(-Q)=0$$

$Q$ ist die Ladung der positiven Elektrode, die andere trägt $-Q$: Laden trennt Ladung, es fügt keine hinzu. An beiden Anschlüssen fließt im selben Moment derselbe Strom, durch die Lücke läuft keine Ladung.

**Verschobene Ladung bei konstantem Strom**

$$Q=I\,t,\qquad N=Q/e$$

$I$ Strom in einer Zuleitung, $t$ Dauer; $N$ Zahl der Elektronen, die die eine Platte verlassen. Ebenso viele kommen auf der anderen an, aus dem Draht davor.

**Potenzial einer Nettoladung**

$$\varphi=k\,Q_\mathrm{n}/r$$

Kugel vom Radius $r$ mit der Nettoladung $Q_\mathrm{n}$; bei $r=1$ cm ergäbe 1 µC schon 900 kV. Deshalb bleibt die Nettoladung eines Bauteils praktisch null, und die Knotenregel gilt für das Bauteil als Ganzes.
::::

::::lernkarten
:::karte begriff Kondensator, Elektrode und Dielektrikum
Woraus besteht ein Kondensator, und wie heißen seine Teile?
---
Aus zwei Elektroden, die ein Dielektrikum trennt: Jede der beiden Platten ist eine Elektrode, der Isolator dazwischen heißt Dielektrikum.
--- falsch
Aus zwei Dielektrika, die eine Elektrode trennt: Jede der beiden Platten ist ein Dielektrikum, der leitende Kern dazwischen heißt Elektrode.
--- falsch
Aus zwei Elektroden aus Isolierstoff, zwischen denen ein leitendes Dielektrikum liegt, durch das der Strom von Platte zu Platte fließt.
--- falsch
Aus einer einzigen Elektrode, die ein Dielektrikum ringsum umhüllt: Die Elektrode speichert die Ladung, das Dielektrikum hält sie dort fest.
:::
:::karte begriff Ladung eines Kondensators
Was meint man mit der Ladung $Q$ eines geladenen Kondensators, und wie groß ist seine Gesamtladung?
---
$Q$ ist die Ladung der positiven Elektrode, die andere trägt $-Q$. Geladen heißt: Ladung ist getrennt, nicht hinzugefügt; die Gesamtladung bleibt null.
--- falsch
$Q$ ist die Summe der Ladungen beider Elektroden. Geladen heißt: Die Batterie hat Ladung hinzugefügt; die Gesamtladung des Bauteils ist deshalb $Q$.
--- falsch
$Q$ ist die Ladung jeder der beiden Elektroden, beide tragen $+Q$. Die Gesamtladung ist $2Q$, die Batterie hat sie aus ihrem Vorrat abgegeben.
--- falsch
$Q$ ist die Ladung, die durch den Isolator von einer Elektrode zur anderen gewandert ist. Die Gesamtladung bleibt null, weil sie nur die Seite wechselt.
:::
:::karte zusammenhang Strom durch den Kondensator
Was geschieht an den Anschlüssen und in der Lücke, wenn man sagt, durch einen Kondensator fließe Strom?
---
An einem Anschluss fließt Strom hinein, am anderen im selben Moment derselbe Strom heraus. Durch die Lücke läuft keine Ladung, und der Strom dauert nur, solange sich die Ladung ändert.
--- falsch
Elektronen springen durch das Dielektrikum von Platte zu Platte, deshalb kommt am anderen Anschluss derselbe Strom heraus, und zwar so lange, wie die Batterie angeschlossen bleibt.
--- falsch
An einem Anschluss fließt Strom hinein; am anderen fließt erst dann Strom heraus, wenn die erste Platte voll ist. Bis dahin bleibt der zweite Anschluss ganz stromlos.
--- falsch
An beiden Anschlüssen fließt Strom in den Kondensator hinein. Die Ladung sammelt sich auf beiden Platten, bis der Kondensator voll ist; die Lücke dazwischen bleibt leer.
:::
:::karte zusammenhang Ladestrom trotz Lücke
Warum fließt Strom in den Zuleitungen, sobald man einen ungeladenen Kondensator an eine Batterie anschließt, obwohl sich die Platten nicht berühren?
---
Im ersten Moment liegen beide Platten auf demselben Potenzial, die Pole nicht. Das Gefälle liegt längs der Drähte; ihr Feld schiebt Elektronen von der einen Platte zum Pluspol und vom Minuspol auf die andere.
--- falsch
Die Batterie drückt Elektronen durch das Dielektrikum, das im ersten Moment noch leitet. Erst die getrennte Ladung macht es wieder zum Isolator, dann endet der Strom in den Zuleitungen.
--- falsch
Die Batterie gibt aus ihrem Vorrat neue Ladung ab, die sich auf beiden Platten sammelt; deshalb fließt in beiden Drähten Strom zum Kondensator hin, bis die Platten voll sind.
--- falsch
Zwischen den Platten herrscht von Anfang an das volle Feld der Batterie. Es zieht die Elektronen über die Drähte auf beide Platten, bis diese so viel Ladung tragen, wie auf ihre Fläche überhaupt hineinpasst.
:::
:::karte zusammenhang Ende des Ladestroms
Warum hört der Ladestrom von selbst auf, wenn die Spannung zwischen den Platten die Spannung der Batterie erreicht?
---
Jede verschobene Ladung verstärkt das Feld zwischen den Platten und verkleinert das Gefälle längs der Drähte. Am Ende liegt jede Platte auf dem Potenzial ihres Pols; die Kraft auf die Elektronen ist null.
--- falsch
Weil die Platten dann voll sind: Jede Platte fasst nur eine feste Menge Ladung, und weitere Elektronen finden auf ihr keinen Platz mehr, gleich wie stark die Batterie drückt.
--- falsch
Weil die Batterie dann leer ist: Sie hat ihre gesamte Ladung an den Kondensator abgegeben und kann deshalb keinen weiteren Strom mehr durch die Drähte treiben.
--- falsch
Weil sich die Drähte durch den Strom erwärmen und ihr Widerstand dabei so stark steigt, dass der Strom schließlich auf null sinkt, genau in dem Moment, in dem die Spannung am Kondensator die der Batterie erreicht.
:::
:::karte herleitung Gleicher Strom an beiden Anschlüssen
Begründe, ausgehend von der Annahme, es fließe mehr Strom hinein als heraus, dass an beiden Anschlüssen eines Kondensators derselbe Strom fließt.
---
Flösse mehr hinein als heraus, sammelte sich im Bauteil eine Nettoladung $Q_\mathrm{n}$, weil die Differenz der beiden Ströme im Bauteil bliebe.
---
Das ganze Bauteil höbe sich dadurch im Potenzial gegen seine Umgebung, weil Ladung ein Potenzial erzeugt: Eine Kugel mit $r=1$ cm hat $\varphi=k\,Q_\mathrm{n}/r$, schon 1 µC ergäbe 900 kV.
---
Das Feld dieser Nettoladung bremst den Zufluss, lange bevor ein messbarer Unterschied entsteht, weil schon winzige Ladungen riesige Potenziale erzeugen.
---
Also bleibt $Q_\mathrm{n}$ praktisch null, und die Knotenregel gilt für das Bauteil als Ganzes, weil sich Zufluss und Abfluss ohne Stau angleichen.
:::
:::karte zusammenhang Ladung nach dem Abklemmen
Warum bleibt die Ladung auf den Platten sitzen, wenn man die Batterie abklemmt?
---
Die Elektronen der negativen Platte werden von der positiven angezogen, aber der Isolator lässt sie nicht durch, und die Drahtenden sind offen. Erst ein Leiter zwischen den Anschlüssen schafft einen Weg.
--- falsch
Weil mit dem Abklemmen die Anziehung zwischen den Platten verschwindet: Ohne Batterie wirkt auf die Ladungen keine Kraft mehr, die sie von ihrer Platte wegbewegen könnte.
--- falsch
Weil die Elektronen fest an die Atome der Platte gebunden werden, sobald sie dort ankommen; auch über einen Draht zwischen den Anschlüssen können sie die Platte nicht mehr verlassen, sie bleiben dort gebunden.
--- falsch
Weil beide Platten gleichnamig geladen sind und sich gegenseitig abstoßen; diese Abstoßung drückt jede Ladung fest auf ihre eigene Platte, solange die Drahtenden offen sind.
:::
:::karte zusammenhang Geladener Kondensator an gleicher Spannung
Was geschieht, wenn man einen auf 9 V geladenen Kondensator mit gleicher Polung an eine 9-V-Batterie anschließt?
---
Nichts: Die Platten liegen schon auf den Potenzialen der Pole, längs der Drähte gibt es kein Gefälle, also fließt kein Strom.
--- falsch
Es fließt kurz Strom, bis der Kondensator 18 V trägt, weil sich die Spannungen von Batterie und Kondensator addieren.
--- falsch
Es fließt derselbe Ladestrom wie bei einem leeren Kondensator, weil die Batterie ihre Spannung unabhängig vom Zustand der Platten anlegt.
--- falsch
Es fließt ein dauernder Strom, weil der volle Kondensator nun wie ein Draht wirkt und die Batterie kurzschließt.
:::
::::
