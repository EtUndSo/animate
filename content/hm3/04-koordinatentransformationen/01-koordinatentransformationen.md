---
title: Überblick: Koordinatentransformationen
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Koordinatentransformationen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen
knoten: Kapitel 4: Koordinatentransformationen
order: 3140100
summary: Was kostet es, wenn aus einem Kreis ein Rechteck wird?
tags: Koordinatentransformation
lang: de
---

## Worum es geht

Ein Kreis ist in den Koordinaten $x$ und $y$ unbequem: Die Grenzen des einen Integrals hängen von der anderen Variablen ab. Beschreibt man denselben Kreis durch Abstand und Winkel, läuft jede Variable durch ihr eigenes festes Intervall. Ein solcher Wechsel heißt __Koordinatentransformation__. Dieses Kapitel fragt, was er kostet und wann er erlaubt ist.

Der Nutzen ist groß. Das Volumen eines Rotationskörpers, das Potential einer geladenen Kugel, das Feld um einen Draht: All das wird erst in passenden Koordinaten rechenbar. Zum Schluss steht dieselbe Frage für Ableitungen: Wie sehen Gradient und Divergenz aus, wenn eine Funktion nicht in $x,y,z$ gegeben ist, sondern in Abstand und Winkeln?

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Die Rechenmodelle für dieses Kapitel
<ul>

<li>

⁠**Scheibe**: der Kreis $x^2+y^2\le4$ in der Ebene.

</li>

<li>

⁠**Kuppelkörper**: der Körper über der Scheibe, unten begrenzt durch $z=0$, oben durch $z=4-x^2-y^2$.

</li>

<li>

⁠**Kugel** mit Radius $R=2$ um den Nullpunkt.

</li>

</ul>

Vorausgesetzt werden Jacobi-Matrix, Gradient, Divergenz und Rotation ([Kapitel 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)), Mehrfachintegrale ([Kapitel 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)), Kurvenintegrale und Green in der Ebene ([Kapitel 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html)). Vektoren sind fett gesetzt.
:::
