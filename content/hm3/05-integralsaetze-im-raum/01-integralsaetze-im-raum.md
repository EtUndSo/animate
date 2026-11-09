---
title: Überblick: Integralsätze im Raum
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3150100
summary: Was im Inneren geschieht, lässt sich am Rand ablesen
tags: Satz von Stokes, Satz von Gauß
lang: de
---

## Worum es geht

Der Hauptsatz der Differential- und Integralrechnung sagt: Integriert man eine Ableitung über ein Intervall, zählen am Ende nur die beiden Randpunkte, $\int_a^bf'(t)\,\mathrm{d} t=f(b)-f(a)$. Alles, was dazwischen passiert, hebt sich auf. Dieses Kapitel zeigt, dass dasselbe auf gekrümmten Flächen und in räumlichen Körpern gilt. Der __Satz von Stokes__ führt ein Integral über eine Fläche auf eine Kurve zurück, der __Satz von Gauß__ ein Integral über einen Körper auf seine Oberfläche. Vorher braucht man das Werkzeug, um über gekrümmte Flächen überhaupt zu integrieren.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Die Rechenmodelle für dieses Kapitel
<ul>

<li>

⁠**Kuppel** $K$: der Graph $z=4-x^2-y^2$ über dem Kreis $x^2+y^2\le4$. Sie steht auf der Ebene $z=0$, ihr Rand ist der Kreis mit Radius 2, ihre Spitze liegt bei $z=4$.

</li>

<li>

⁠**Feld** $\boldsymbol{F}(x,y,z)=(-y,\;x,\;2z)$ mit $\operatorname{rot}\boldsymbol{F}=(0,0,2)$ und $\operatorname{div}\boldsymbol{F}=2$. Das Feld dreht um die $z$-Achse und strömt zugleich von der Ebene $z=0$ weg.

</li>

<li>

⁠**Kugel** mit Radius $R=2$ um den Nullpunkt.

</li>

</ul>

Vorausgesetzt werden Kurvenintegrale, Green in der Ebene, $\operatorname{rot}$, $\operatorname{div}$, Kugelkoordinaten und der Transformationssatz ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) bis 4). Vektoren sind fett gesetzt, $\boldsymbol{x}_u=\partial\boldsymbol{x}/\partial u$ ist die Ableitung nach dem Parameter $u$.
:::
