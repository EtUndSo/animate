---
title: Überblick: Mengen, Logik und reelle Zahlen
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210100
summary: Was man über die Zahlen voraussetzen muss und warum die Wurzel aus 2 kein Bruch ist
tags: Menge, Aussage, Axiom, Körper, Anordnung, Vollständigkeit, vollständige Induktion, Betrag
lang: de
---

## Worum es geht

Aus der Schule kennt man Regeln wie $(-1)\cdot(-1)=1$ oder „durch null darf man nicht teilen“. Warum gelten sie? Gewohnheit als Begründung trägt nicht weit: Bei den komplexen Zahlen ([Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)) fällt die Regel „Quadrate sind nicht negativ“, und alle Grenzwerte ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)) hängen an einer Eigenschaft der Zahlen, die in der Schule nie genannt wird. Man sieht sie an einer einzigen Zahl: Die Diagonale eines Quadrats mit Seitenlänge 1 hat die Länge $\sqrt2$, und kein Bruch hat diesen Wert. Die Frage dieses Kapitels lautet: *Was genau muss man über die Zahlen voraussetzen, damit alle Rechenregeln beweisbar werden, und was unterscheidet die reellen Zahlen von den Brüchen?*

Die Antwort braucht zwei Werkzeuge und eine kurze Liste von Annahmen. Eine __Menge__ fasst Objekte zusammen, eine __Aussage__ ist ein Satz, der wahr oder falsch ist. Ein __Axiom__ ist eine Grundannahme, die man festlegt und nicht beweist. Drei Gruppen von Axiomen genügen: Ein __Körper__ ist eine Menge, in der Plus und Mal nach den bekannten Regeln funktionieren. Die __Anordnung__ legt fest, welche Zahlen positiv sind. Die __Vollständigkeit__ sagt, dass die Zahlengerade keine Lücken hat. Dazu kommen die __vollständige Induktion__, das Beweisverfahren für Aussagen über alle natürlichen Zahlen, und der __Betrag__, der Abstand einer Zahl von der Null.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Mengen:** $G=\{1,2,\dots,12\}$, darin $A=\{1,2,3,4,6,12\}$ (Teiler von 12) und $B=\{2,3,5,7,11\}$ (Primzahlen).

</li>

<li>

⁠**Aussage:** $\mathcal E(n):=(n\ge7\Rightarrow n>5)$ für natürliche Zahlen $n$.

</li>

<li>

⁠**Lückenmenge:** $D=\{x\in\mathbb{Q}:x>0,\ x^2<2\}$, die positiven Brüche mit Quadrat unter 2.

</li>

<li>

⁠**Zahlen für Ungleichungen:** $x=-3$, $y=5$ für den Betrag; $x=2$, $y=8$ für die Mittelwerte; die Listen $\vec x=(3,4)$, $\vec y=(1,2)$ für Cauchy-Schwarz.

</li>

</ul>
:::
