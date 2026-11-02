---
title: Überblick: Integralrechnung im $\R^n$
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120100
summary: Wann man Ableitung, Integral und Reihenfolge vertauschen darf
tags: Parameterintegral, Leibnizregel, Mehrfachintegral, Satz von Fubini, Normalbereich
lang: de
---

## Worum es geht

Ein Integral über eine Variable liefert eine Zahl. In der Technik reicht das an zwei Stellen nicht.

Erstens hängt eine Kurve oft von einer Stellgröße ab. Ein Signal klingt je nach Dämpfung schneller oder langsamer ab. Die Fläche unter der Kurve ist dann keine feste Zahl mehr, sondern eine Funktion der Stellgröße, ein __Parameterintegral__. Man möchte wissen, wie empfindlich diese Fläche auf die Stellgröße reagiert, oft ohne das Integral ausrechnen zu können. Darf man dazu unter dem Integralzeichen ableiten? Was ändert sich, wenn auch die Integrationsgrenzen mitwandern (Stichwort __Leibnizregel__) oder das Integral bis ins Unendliche läuft?

Zweitens ist eine Größe oft über eine Fläche oder einen Körper verteilt, etwa eine Ladung in einem Bauteil. Die Gesamtmenge ist ein __Mehrfachintegral__, ein Integral über mehrere Variablen. Man möchte es in gewöhnliche Integrale zerlegen. Spielt es eine Rolle, welche Variable man zuerst abarbeitet (Stichwort __Satz von Fubini__)? Und wie geht man vor, wenn der Bereich kein Rechteck ist, sondern krumme Ränder hat (Stichwort __Normalbereich__)?

**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Die Rechenmodelle für dieses Kapitel
<ul>

<li>

⁠**Abklingkurve** $f(x,t)=\mathrm{e}^{-xt}$. Die Kurve in $t$ fällt umso schneller, je größer die Dämpfung $x\ge0$ ist. Bei $x=1$ und $t=2$ ist $f=\mathrm{e}^{-2}\approx0{,}135$.

</li>

<li>

⁠**Kuppel** $K$: der Körper zwischen der Ebene $z=0$ und dem Graphen von $4-x^2-y^2$. Sie steht auf dem Kreis $x^2+y^2\le4$, ihre Spitze liegt bei $z=4$.

</li>

</ul>

Vorausgesetzt werden partielle Ableitungen und die Kettenregel für mehrere Variablen ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)) sowie die Integralrechnung einer Variablen, die im nächsten Abschnitt wiederholt wird. Fett gesetzt sind Punkte $\boldsymbol{x}=(x_1,\dots,x_n)$. $\hat{\boldsymbol{e}}_k$ ist der Einheitsvektor längs der $k$-ten Achse.
:::
