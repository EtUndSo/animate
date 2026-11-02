---
title: Von Grund auf: Was aus den Teilen 4 bis 6 gebraucht wird
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270200
summary: Wie eine einzige Reihe Exponentialfunktion, Sinus und Cosinus enthält und warum Multiplizieren komplexer Zahlen Drehen und Strecken ist
tags: Reihe, Teilsummen, absolut konvergent, stetig
lang: de
---

Eine __Reihe__ $\sum_{n=0}^\infty b_n$ ist der Grenzwert ihrer __Teilsummen__ $s_N=\sum_{n=0}^Nb_n$. Sie heißt __absolut konvergent__, wenn $\sum|b_n|$ konvergiert. Dann konvergiert sie auch selbst, und jede Umordnung hat denselben Wert. Konvergiert eine Reihe, sind ihre Glieder eine Nullfolge, also beschränkt. Vier Werkzeuge tragen dieses Kapitel:

<ul>

<li>

⁠**Geometrische Reihe:** $\sum_{n=0}^\infty q^n=\frac1{1-q}$ für $|q|<1$, Divergenz für $|q|\ge1$.

</li>

<li>

⁠**Majorante:** Aus $|b_n|\le c_n$ und $\sum c_n$ konvergent folgt, dass $\sum b_n$ absolut konvergiert.

</li>

<li>

⁠**Quotienten- und Wurzelkriterium:** Sei $\alpha:=\lim|b_{n+1}/b_n|$ oder $\alpha:=\lim\sqrt[n]{|b_n|}$. Für $\alpha<1$ ist die Reihe absolut konvergent, für $\alpha>1$ divergent, $\alpha=1$ sagt nichts.

</li>

<li>

⁠**Leibniz-Kriterium:** Fallen die $|b_n|$ monoton gegen 0 und wechselt das Vorzeichen, konvergiert die Reihe. Der Fehler einer Teilsumme ist höchstens das erste weggelassene Glied.

</li>

</ul>

Aus [Teil 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html) kommen $\exp(x)=\lim_{n\to\infty}(1+\frac xn)^n$ und $\exp(1)=\mathrm{e}$, außerdem der Begriff __stetig__ (eine kleine Änderung von $x$ ändert $f(x)$ nur wenig) und der Zwischenwertsatz. Sinus, Cosinus und $\pi$ baut dieses Kapitel neu auf.
