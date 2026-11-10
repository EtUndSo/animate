---
title: Überblick: Vektoren und Skalarprodukt
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektoren und Skalarprodukt
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt
knoten: Kapitel 8: Vektoren und Skalarprodukt
order: 1280100
summary: Warum Pfeile, Zahlenspalten und Polynome denselben Regeln folgen und wie Länge und Winkel dazukommen
tags: Vektor, Vektorraum, Linearkombination, Unterraum, Lineare Unabhängigkeit, Skalarprodukt, Norm, Orthogonalprojektion
lang: de
---

## Worum es geht

Eine Kraft, eine Spalte aus Messwerten und ein Polynom haben wenig gemeinsam. Trotzdem rechnet man mit allen dreien gleich: Zwei davon lassen sich addieren, eines lässt sich mit einer Zahl strecken. Die Frage lautet: *Was genügt, damit überall dieselben Regeln gelten, und woher kommen Länge und Winkel, wenn es nichts mehr zu zeichnen gibt?*

Die Antwort führt über acht Begriffe. Alles, was man addieren und strecken kann, heißt __Vektor__, die Menge solcher Objekte __Vektorraum__. Eine __Linearkombination__ ist eine Summe gestreckter Vektoren. Ein __Unterraum__ ist ein Teil des Vektorraums, den keine Linearkombination verlässt. __Lineare Unabhängigkeit__ heißt: Keiner der Vektoren lässt sich aus den anderen bauen. Das __Skalarprodukt__ macht aus zwei Vektoren eine Zahl. Aus ihm folgen die __Norm__, also die Länge, und die __Orthogonalprojektion__, die einen Vektor in einen Teil längs einer Richtung und einen Rest senkrecht dazu zerlegt.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Zwei Pfeile in der Ebene:** $\vec a=(3,1)$ und $\vec b=(1,2)$. Sie schließen genau $45^\circ$ ein.

</li>

<li>

⁠**Drei Vektoren im Raum:** $\vec c=(2,1,0)$, $\vec d=(0,1,2)$ und $\vec f=(4,1,-2)$. Keiner ist ein Vielfaches eines anderen, und doch ist $\vec f=2\vec c-\vec d$.

</li>

<li>

⁠**Drei Polynome:** $p(x)=x^2-1$, $q(x)=x+1$, $r(x)=x^2+x$. Es gilt $p+q=r$.

</li>

<li>

⁠**Eine Ebene und ein Punkt im Raum:** $H$: $2x_1+x_2+2x_3=6$ und $P=(3,3,3)$. Der nächste Punkt von $H$ ist $(1,2,1)$, der Abstand 3.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap8.py` nach.
:::
