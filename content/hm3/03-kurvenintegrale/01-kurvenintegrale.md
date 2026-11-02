---
title: Überblick: Kurvenintegrale
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130100
summary: Wann zählen nur Start und Ziel, und wann der ganze Weg?
tags: 
lang: de
---

## Worum es geht

Ein Feld wirkt an jedem Ort anders, und ein Teilchen läuft auf einem krummen Weg hindurch. Die Frage dieses Kapitels lautet: *Wie viel Arbeit leistet das Feld längs dieses Wegs, und wann kommt es dabei nur auf Start und Ziel an, nicht auf den Weg dazwischen?* Die Antwort spart viel Rechnung. Sie sagt auch, warum man in der Elektrotechnik von der Spannung zwischen zwei Punkten sprechen darf. Zum Schluss geht es darum, was ein Lauf um den Rand einer ebenen Fläche über ihr Inneres verrät.

**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Zwei Wege** von $A=(1,0)$ nach $B=(0,1)$: der Viertelkreis $\kappa(t)=(\cos t,\sin t)$, $0\le t\le\pi/2$, und die Strecke $\eta(t)=(1-t,\,t)$, $0\le t\le1$.

</li>

<li>

⁠**Drei Felder** in der Ebene: das Drehfeld $\boldsymbol V(x,y)=(-y,\,x)$, das Gradientenfeld $\boldsymbol G(x,y)=(2x,\,2y)=\nabla(x^2+y^2)$ und $\boldsymbol{H}(x,y)=\frac{1}{x^2+y^2}(-y,\,x)$, das im Nullpunkt nicht definiert ist.

</li>

</ul>

Vorausgesetzt werden Gradient, Divergenz, Rotation und die Integrabilitätsbedingungen ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)) sowie Ableiten unter dem Integral, die Leibnizregel und Normalbereiche ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)). In der Ebene ist $\operatorname{rot}\boldsymbol{F}=\partial_xF_2-\partial_yF_1$ eine Zahl.
:::
