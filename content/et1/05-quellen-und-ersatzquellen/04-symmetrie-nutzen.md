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
