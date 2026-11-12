---
title: Stufe 2: Symmetrie nutzen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1150400
summary: Manche Netze enthalten keine Gruppen.
tags: Halbschaltung
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Manche Netze enthalten keine Gruppen. Symmetrie liefert dann Knoten gleichen Potenzials, und durch deren Verbinden entstehen Gruppen.
:::

**Die Idee.** Liegen zwei Knoten auf gleichem Potenzial, ist die Spannung zwischen ihnen null. Ein Draht zwischen ihnen führt deshalb keinen Strom, und es ändert sich nichts, wenn man ihn einbaut. Umgekehrt darf man einen stromlosen Zweig auftrennen. Symmetrie verrät, welche Knoten das sind, ohne dass man etwas ausrechnet.

:::satz Satz 2.1 (Zwei Symmetrieregeln)
<span class="anker" id="satz-2-1"></span>

Für ein Netz aus Widerständen mit den Klemmen A und B gilt:

<ol>

<li>

Geht das Netz durch Spiegeln oder Drehen in sich über und bleiben A und B dabei am Platz, haben Knoten, die aufeinanderfallen, gleiches Potenzial. Man darf sie verbinden. Ein Widerstand zwischen ihnen ist stromlos.

</li>

<li>

Geht das Netz durch Spiegeln in sich über und tauschen A und B dabei die Plätze, liegt jeder Punkt der Spiegelachse auf dem Mittelwert $\frac12(\varphi_\mathrm{A}+\varphi_\mathrm{B})$. Man darf alle verbinden und rechnet nur eine Seite, die __Halbschaltung__:

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{AB}=2\,R_\mathrm{A,Achse}. \tag{2.1}$$

</li>

</ol>
:::

⁠**So liest man das:** $R_\mathrm{A,Achse}$ ist der Widerstand zwischen A und der zu einem Knoten verbundenen Achse. Ein Widerstand, der die Achse quert, zerfällt in zwei halbe Widerstände, seine Mitte liegt auf der Achse. Ein Widerstand längs der Achse hat beide Enden auf demselben Potenzial und ist stromlos. **Gültigkeit:** Die Symmetrie muss auch die Werte erfassen. Ein einziger abweichender Widerstand hebt sie auf.

:::herleitung Die Potenziale folgen aus der Symmetrie
Regel 1: Das gespiegelte Netz hat dieselben Bauteile, dieselben Klemmen und dieselbe Spannung, also dieselben Gleichungen. Diese haben genau eine Lösung. Zwei Knoten, die aufeinanderfallen, müssen deshalb dasselbe Potenzial haben.

Regel 2: Der Bezugspunkt liege in der Mitte, also $\varphi_\mathrm{A}=+\frac12U$ und $\varphi_\mathrm{B}=-\frac12U$. Das Spiegeln tauscht A und B, wirkt also wie ein Umpolen der Spannung. Umpolen kehrt in einem linearen Netz jedes Potenzial um (Stufe [8](uberlagerung.html#stufe-8)). Für einen Punkt $P$ und sein Spiegelbild $P'$ gilt daher $\varphi(P')=-\varphi(P)$. Ein Punkt auf der Achse ist sein eigenes Spiegelbild, also gilt $\varphi=-\varphi$ und damit $\varphi=0$, der Mittelwert. Beide Hälften sind gleich und liegen in Reihe, das ergibt [(2.1)](#gl-2-1).
:::

:::abbildung et1/k5symmetrie 2
Sieben gleiche Widerstände mit je 14 $\Omega$. Links das Netz mit den Potenzialen bei 16 V an A. Die Spiegelachse läuft durch L und durch die Mitte des Widerstands zwischen E und F, der deshalb in zweimal 7 $\Omega$ zerfällt. Rechts die Halbschaltung.
:::

::::beispiel
In Abb. [2](#abb-2) tauscht das Spiegeln A und B sowie E und F, Regel 2 gilt. In der Halbschaltung liegen zwischen E und der Achse $14\,\Omega\parallel7\,\Omega=4{,}67\,\Omega$. Mit dem Weg von A nach E sind das 18,67 $\Omega$. Parallel zum linken Zweig ergibt das $R_\mathrm{A,Achse}=14\,\Omega\parallel18{,}67\,\Omega=8\,\Omega$, also $R_\mathrm{AB}=16\,\Omega$, wieder die Last aus dem Rechenmodell. **Kontrolle** mit den Potenzialen des Bildes: Von A nach L fließen $8\,\mathrm{V}/14\,\Omega=0{,}571$ A, von A nach E fließen $6\,\mathrm{V}/14\,\Omega=0{,}429$ A. Die Summe ist 1 A, wie $16\,\mathrm{V}/16\,\Omega$ es verlangt.
::::

:::abbildung et1/k5wuerfel 3
Würfel aus zwölf gleichen Widerständen mit Spannung an der Raumdiagonale. Eine Drehung um diese Diagonale führt die drei Nachbarn von A ineinander über, ebenso die drei Nachbarn von B. Nach dem Verbinden entsteht eine Kette aus drei Gruppen.
:::

**Der Widerstandswürfel.** Zwölf Kanten mit je $R=12\,\Omega$, die Klemmen an gegenüberliegenden Ecken (Abb. [3](#abb-3)). Nach Regel 1 liegen die drei Nachbarn von A auf gleichem Potenzial, ebenso die drei Nachbarn von B. Zwischen diesen Dreiergruppen laufen sechs Kanten. Es entsteht eine Kette:

$$R_\mathrm{AB}=\frac R3+\frac R6+\frac R3=\frac56R=10\,\Omega.$$

Bei 5 V fließen 0,5 A. Sie verteilen sich auf drei Kanten mit je 167 mA, dann auf sechs mit je 83 mA, dann wieder auf drei.

:::frage Ist das Verbinden nicht ein Eingriff in die Schaltung?
In die Zeichnung ja, in die Ströme nein. Durch den neuen Draht könnte nur Strom fließen, wenn zwischen seinen Enden Spannung läge. Die liegt nicht an. Deshalb ändert sich kein Strom im übrigen Netz. Das Verfahren gilt nur, solange die Potenziale wirklich gleich sind.
:::

:::aufgabe Aufgabe 2 ★ Stromlos vorhersagen
<span class="anker" id="aufg-2"></span>

Von A führen 10 $\Omega$ zum Knoten C und 30 $\Omega$ zum Knoten D, von C führen 20 $\Omega$ und von D 60 $\Omega$ nach B. Zwischen C und D liegt ein Querwiderstand $R_\mathrm{Q}$ (die Brücke aus [Kapitel 4](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). (a) Zeige, dass C und D gleiches Potenzial haben, auch ohne Symmetrie. (b) Berechne $R_\mathrm{AB}$ für $R_\mathrm{Q}\to\infty$ und für $R_\mathrm{Q}\to0$. (c) Was folgt für $R_\mathrm{Q}=47\,\Omega$?

:::loesung
(a) Ohne Strom durch $R_\mathrm{Q}$ sind beide Zweige Spannungsteiler mit demselben Verhältnis: $\frac{20}{10+20}=\frac{60}{30+60}=\frac23$. C und D liegen dann auf demselben Potenzial, und durch $R_\mathrm{Q}$ fließt wirklich kein Strom. Das ist die eine Lösung des Netzes (der Abgleich aus [Kapitel 4](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)).

(b) $R_\mathrm{Q}\to\infty$: $(10\,\Omega+20\,\Omega)\parallel(30\,\Omega+60\,\Omega)=22{,}5\,\Omega$. $R_\mathrm{Q}\to0$: $10\,\Omega\parallel30\,\Omega+20\,\Omega\parallel60\,\Omega=7{,}5\,\Omega+15\,\Omega=22{,}5\,\Omega$.

(c) Dasselbe: 22,5 $\Omega$. Der Querwiderstand ist stromlos, sein Wert spielt keine Rolle.
:::
:::

:::aufgabe Aufgabe 3 ★★ Würfel über die Flächendiagonale
<span class="anker" id="aufg-3"></span>

Lege die Spannung an zwei Ecken derselben Würfelfläche, die sich diagonal gegenüberliegen, $R=12\,\Omega$. Tipp: Beide Regeln helfen. Welche vier Ecken liegen auf dem Mittelwert? Berechne $R_\mathrm{AB}$.

:::loesung
Die Klemmen seien A und B. C und D sind die zwei Ecken, die Nachbarn von A und von B sind. Über C und D liegen in der anderen Fläche E und F, über A liegt P, über B liegt Q. Spiegelt man an der Ebene, die senkrecht auf der Verbindung AB steht und durch ihre Mitte geht, tauschen A und B die Plätze, ebenso P und Q. C, D, E, F liegen in dieser Ebene, also nach Regel 2 auf dem Mittelwert.

Halbschaltung von A zur Achse: über C und D je $R$, zusammen $\frac R2$. Über P: $R$, dann von P nach E und nach F je $R$, zusammen $R+\frac R2=\frac32R$. Parallel: $\frac R2\parallel\frac32R=\frac38R$. Damit ist $R_\mathrm{AB}=\frac34R=9\,\Omega$.
:::
:::

::::formelsammlung
**Potenziale bei vertauschten Klemmen (Regel 2)**

$$\varphi(P')=-\varphi(P)$$

Das Netz geht durch Spiegeln in sich über, A und B tauschen die Plätze; Bezugspunkt in der Mitte, $\varphi_\mathrm{A}=+\frac12U$ und $\varphi_\mathrm{B}=-\frac12U$. $P'$ ist das Spiegelbild von $P$. Ein Punkt auf der Achse ist sein eigenes Spiegelbild, also $\varphi=0$: Er liegt auf dem Mittelwert $\frac12(\varphi_\mathrm{A}+\varphi_\mathrm{B})$. Bleiben A und B beim Spiegeln oder Drehen am Platz (Regel 1), haben aufeinanderfallende Knoten gleiches Potenzial.

**Halbschaltung**

$$R_\mathrm{AB}=2\,R_\mathrm{A,Achse}$$

$R_\mathrm{A,Achse}$ ist der Widerstand zwischen A und der zu einem Knoten verbundenen Achse. Ein Widerstand, der die Achse quert, zerfällt in zwei halbe; einer längs der Achse ist stromlos. Die Symmetrie muss auch die Werte erfassen.

**Widerstandswürfel über die Raumdiagonale**

$$R_\mathrm{AB}=\frac R3+\frac R6+\frac R3=\frac56R$$

Zwölf gleiche Kanten $R$. Nach Regel 1 liegen die drei Nachbarn von A auf gleichem Potenzial, ebenso die drei Nachbarn von B; es entsteht eine Kette aus drei, sechs und drei parallelen Kanten.
::::

::::lernkarten
:::karte zusammenhang Knoten gleichen Potenzials
Warum darf man zwei Knoten gleichen Potenzials durch einen Draht verbinden, ohne dass sich im Netz etwas ändert?
---
Zwischen ihnen ist die Spannung null. Ein Draht führt nur Strom, wenn zwischen seinen Enden Spannung liegt; er bleibt also stromlos, und kein Strom im übrigen Netz ändert sich. Ebenso darf man einen stromlosen Zweig auftrennen.
--- falsch
Weil ein Draht keinen Widerstand hat und deshalb nie Strom führt, gleich welche Spannung zwischen seinen Enden liegt. Das gilt für beliebige Knoten, nicht nur für solche gleichen Potenzials, und ebenso für das Auftrennen.
--- falsch
Weil sich zwar die Ströme ändern, der Gesamtwiderstand aber gleich bleibt. Das genügt, solange nur $R_\mathrm{AB}$ gesucht ist; die Ströme muss man danach im ursprünglichen Netz neu rechnen.
--- falsch
Weil der Draht die Potenziale der beiden Knoten angleicht: Vorher sind sie verschieden, danach gleich. Das ist erlaubt, weil sich die Spannung an den Klemmen dabei nicht ändert.
:::
:::karte zusammenhang Symmetrieregel 1
Was folgt nach der ersten Symmetrieregel für Knoten, die beim Spiegeln oder Drehen eines Widerstandsnetzes aufeinanderfallen, wenn A und B dabei am Platz bleiben?
---
Sie haben gleiches Potenzial. Man darf sie verbinden, und ein Widerstand zwischen ihnen ist stromlos.
--- falsch
Sie haben entgegengesetzt gleiches Potenzial, $\varphi(P')=-\varphi(P)$. Man darf sie deshalb nicht verbinden.
--- falsch
Sie führen gleiche Ströme, haben aber verschiedene Potenziale. Ein Widerstand zwischen ihnen führt den doppelten Strom.
--- falsch
Sie liegen auf dem Mittelwert $\frac12(\varphi_\mathrm{A}+\varphi_\mathrm{B})$. Man darf sie deshalb mit der Klemme B verbinden.
:::
:::karte zusammenhang Warum Symmetrie gleiche Potenziale liefert
Warum müssen Knoten, die beim Spiegeln eines Netzes aufeinanderfallen, dasselbe Potenzial haben, wenn A und B dabei am Platz bleiben?
---
Das gespiegelte Netz hat dieselben Bauteile, dieselben Klemmen und dieselbe Spannung, also dieselben Gleichungen. Diese haben genau eine Lösung, also müssen aufeinanderfallende Knoten dasselbe Potenzial haben.
--- falsch
Weil gleiche Widerstände immer gleiche Spannungen tragen, gleich wo sie im Netz liegen. Aufeinanderfallende Knoten sind über gleiche Widerstände mit A verbunden und liegen deshalb gleich hoch über dem Potenzial von B.
--- falsch
Weil sich beim Spiegeln alle Ströme umkehren und dadurch die Potenziale ausgleichen. Was vorher höher lag, liegt danach tiefer, im Mittel also auf demselben Wert.
--- falsch
Weil die Gleichungen des Netzes viele Lösungen haben und man die symmetrische auswählen darf. Sie ist nicht die einzige, aber die einfachste zum Rechnen.
:::
:::karte begriff Halbschaltung
Was ist die Halbschaltung eines Widerstandsnetzes, und unter welcher Bedingung darf man mit ihr rechnen?
---
Die eine Hälfte eines Netzes, das durch Spiegeln in sich übergeht, wobei A und B die Plätze tauschen. Die Punkte der Spiegelachse liegen auf dem Mittelwert der Klemmenpotenziale; man verbindet sie und rechnet: $R_\mathrm{AB}=2\,R_\mathrm{A,Achse}$.
--- falsch
Ein Netz, in dem man jeden Widerstand halbiert, um den Strom zu verdoppeln. Das darf man immer, wenn alle Widerstände gleich groß sind, und es gilt dann $R_\mathrm{AB}=\frac12R_\mathrm{A,Achse}$, weil nur die halbe Zahl von Widerständen übrig bleibt.
--- falsch
Die eine Hälfte eines Netzes, das beim Drehen in sich übergeht, wobei A und B am Platz bleiben. Man rechnet nur diese Seite und halbiert: $R_\mathrm{AB}=\frac12R_\mathrm{A,Achse}$.
--- falsch
Die eine Hälfte eines spiegelsymmetrischen Netzes, wobei A und B die Plätze tauschen. Die Achse liegt dabei auf dem Potenzial von B, man verbindet sie mit B, und es gilt $R_\mathrm{AB}=R_\mathrm{A,Achse}$.
:::
:::karte zusammenhang Widerstände an der Spiegelachse
Was geschieht in der Halbschaltung mit einem Widerstand, der die Spiegelachse quert, und mit einem, der längs der Achse liegt?
---
Ein querender Widerstand zerfällt in zwei halbe Widerstände, seine Mitte liegt auf der Achse. Ein Widerstand längs der Achse hat beide Enden auf demselben Potenzial und ist stromlos.
--- falsch
Ein querender Widerstand fällt ganz weg, weil seine Mitte auf der Achse liegt. Ein Widerstand längs der Achse zerfällt in zwei halbe Widerstände, je einer für jede Seite der Halbschaltung.
--- falsch
Ein querender Widerstand bleibt ganz in der Halbschaltung, weil er an der Seite von A beginnt. Ein Widerstand längs der Achse wird doppelt gezählt.
--- falsch
Ein querender Widerstand zerfällt in zwei doppelt so große Widerstände, die parallel liegen. Ein Widerstand längs der Achse führt den halben Strom.
:::
:::karte herleitung Mittelwert auf der Spiegelachse
Leite aus der Linearität her, dass bei einem Netz, dessen Spiegelung A und B vertauscht, jeder Punkt der Spiegelachse auf dem Mittelwert der Klemmenpotenziale liegt.
---
Man legt den Bezugspunkt in die Mitte, also $\varphi_\mathrm{A}=+\frac12U$ und $\varphi_\mathrm{B}=-\frac12U$, weil der Mittelwert dann null ist und nur noch $\varphi=0$ zu zeigen bleibt.
---
Das Spiegeln tauscht A und B und wirkt deshalb wie ein Umpolen der Spannung, weil das gespiegelte Netz dieselben Bauteile hat und nur die Klemmen vertauscht sind.
---
Für einen Punkt $P$ und sein Spiegelbild $P'$ gilt $\varphi(P')=-\varphi(P)$, weil Umpolen in einem linearen Netz jedes Potenzial umkehrt.
---
Ein Punkt auf der Achse ist sein eigenes Spiegelbild, also gilt $\varphi=-\varphi$ und damit $\varphi=0$, weil nur null gleich seinem Negativen ist.
---
Beide Hälften sind gleich und liegen in Reihe, also $R_\mathrm{AB}=2\,R_\mathrm{A,Achse}$, weil der Strom erst durch die eine, dann durch die andere Hälfte fließt.
:::
:::karte zusammenhang Symmetrie und Widerstandswerte
Was hebt die Symmetrie eines Widerstandsnetzes auf, auch wenn seine Zeichnung symmetrisch aussieht?
---
Ein einziger abweichender Widerstandswert. Die Symmetrie muss auch die Werte erfassen, nicht nur die Form der Schaltung.
--- falsch
Nur eine unsymmetrische Form. Die Werte der Widerstände spielen keine Rolle, solange die Zeichnung beim Spiegeln in sich übergeht.
--- falsch
Eine andere Spannung an den Klemmen. Bei jeder Spannung außer der berechneten verschieben sich die Potenziale auf der Achse.
--- falsch
Ein Draht zwischen zwei Knoten gleichen Potenzials. Danach ist das Netz verändert, und die Symmetrieregeln gelten nicht mehr.
:::
:::karte formel Widerstandswürfel
Welchen Widerstand hat ein Würfel aus zwölf gleichen Widerständen $R$ zwischen zwei gegenüberliegenden Ecken (Raumdiagonale), und warum?
---
$R_\mathrm{AB}=\frac R3+\frac R6+\frac R3=\frac56R$. Nach Regel 1 liegen die drei Nachbarn von A auf gleichem Potenzial, ebenso die drei Nachbarn von B; es entsteht eine Kette aus drei, sechs und drei parallelen Kanten.
--- falsch
$R_\mathrm{AB}=\frac R3+\frac R6+\frac R3=\frac56R$. Nach Regel 2 liegen alle sechs übrigen Ecken auf dem Mittelwert der Klemmenpotenziale; man verbindet sie und rechnet nur eine Hälfte des Würfels, also sechs der zwölf Kanten.
--- falsch
$R_\mathrm{AB}=\frac R3+\frac R3=\frac23R$. Nur die drei Kanten an A und die drei an B führen Strom, die sechs mittleren Kanten verbinden Knoten gleichen Potenzials, sind stromlos und dürfen fehlen.
--- falsch
$R_\mathrm{AB}=R$. Der Strom fließt über drei gleichwertige Wege mit je drei Kanten; jeder Weg hat $3R$, und drei solche Wege parallel ergeben ein Drittel davon.
:::
::::
