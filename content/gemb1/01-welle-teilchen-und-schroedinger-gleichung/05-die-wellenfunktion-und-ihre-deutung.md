---
title: Stufe 3: Die Wellenfunktion und ihre Deutung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
order: 4110500
summary: Das Elektron kommt als Punkt an, das Muster ist das einer Welle.
tags: Wellenfunktion, Wahrscheinlichkeitsdichte, Normierung, Elektronendichte, Interferenzterm, monochromatische Welle
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Das Elektron kommt als Punkt an, das Muster ist das einer Welle. Diese Stufe sagt, was die Welle bedeutet und was sie über den Ort vorhersagt.
:::

**Die Idee.** Zu jedem Elektron gehört eine komplexe Funktion von Ort und Zeit. Sie beschreibt Schwingung und Ausbreitung wie bei einer elektromagnetischen Welle, lässt sich aber anders als das elektrische Feld nicht messen. Messbar ist nur, wie häufig Elektronen an einem Ort auftauchen, und das legt ihr Betragsquadrat fest, das Gegenstück zur Intensität. Die Zeiger aus beiden Spalten addieren sich, erst die Summe wird quadriert (Abb. [3](#abb-3)). Das ist der Mechanismus der Streifen: Zwei Wege können sich auslöschen, zwei Häufigkeiten nicht.

:::definition Definition 3.1 (Wellenfunktion)
<span class="anker" id="satz-3-1"></span>

Der Zustand eines Elektrons wird durch die komplexe __Wellenfunktion__ $\Psi(x,t)$ beschrieben. Ihr Betragsquadrat $|\Psi|^2=\Psi^*\Psi$ ist die __Wahrscheinlichkeitsdichte__: $|\Psi(x,t)|^2\,\mathrm{d} x$ ist die Wahrscheinlichkeit, das Elektron zur Zeit $t$ zwischen $x$ und $x+\mathrm{d} x$ zu finden. Weil es irgendwo sein muss, gilt die __Normierung__

<span class="anker" id="gl-3-1"></span>
$$\int_{-\infty}^{\infty}|\Psi(x,t)|^2\,\mathrm{d} x=1. \tag{3.1}$$

Im Raum tritt $\Psi(\boldsymbol r,t)$ mit dem Ortsvektor $\boldsymbol r$ an die Stelle, das Volumenelement $\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z$ an die von $\mathrm{d} x$.
:::

⁠**So liest man das:** $|\Psi|^2$ hat die Einheit 1/m, im Raum 1/m$^3$. Wahrscheinlichkeit heißt Häufigkeit in vielen gleichen Versuchen, ein einzelner Versuch liefert genau einen Punkt. Bei $N$ Elektronen im selben Zustand ist $n(x)=N\,|\Psi(x,t)|^2$ die __Elektronendichte__. Das Betragsquadrat passt, weil Messwerte reell und Häufigkeiten nie negativ sind. Multipliziert man $\Psi$ mit $\mathrm{e}^{\mathrm{j}\gamma}$, ändert sich kein Betragsquadrat: Die Phase allein ist nicht messbar. **Gültigkeit:** Die Normierung verlangt ein endliches Integral.

:::satz Satz 3.2 (Überlagerung)
<span class="anker" id="satz-3-2"></span>

Kann das Elektron auf zwei Wegen zum selben Ort gelangen, addieren sich die Wellenfunktionen, und es gilt

<span class="anker" id="gl-3-2"></span>
$$|\Psi_1+\Psi_2|^2=|\Psi_1|^2+|\Psi_2|^2+2\,\operatorname{Re}\bigl(\Psi_1^*\Psi_2\bigr). \tag{3.2}$$
:::

⁠**So liest man das:** Der letzte Summand ist der __Interferenzterm__, er entsteht beim Ausmultiplizieren von $(\Psi_1+\Psi_2)^*(\Psi_1+\Psi_2)$. Für gleich lange Zeiger mit dem Winkel $\delta$ ist $|\Psi|^2=2|\Psi_1|^2(1+\cos\delta)$. Das schwankt zwischen null und dem Vierfachen von $|\Psi_1|^2$. Teilchen ohne Welle ergäben überall das Zweifache.

:::abbildung gemb1/k1zeiger 3
Oben: Betragsquadrat auf dem Schirm in der Nähe der Mitte. Unten: Die Zeiger $\Psi_1$ und $\Psi_2$ an den Stellen A, B und C. Der Wegunterschied dreht sie um $\delta=2\pi y/y_\mathrm S$ gegeneinander. Bei A addieren sie sich, bei C löschen sie sich aus. Gestrichelt: die Summe der Betragsquadrate ohne Interferenz.
:::

::::beispiel
Die einfachste Wellenfunktion hat genau eine Wellenzahl (__monochromatische Welle__):

<span class="anker" id="gl-3-3"></span>
$$\Psi(x,t)=C\,\mathrm{e}^{\mathrm{j}(kx-\omega t)},\qquad\text{im Raum}\quad\Psi(\boldsymbol r,t)=C\,\mathrm{e}^{\mathrm{j}(\boldsymbol k\cdot\boldsymbol r-\omega t)}. \tag{3.3}$$

Hier ist $|\Psi|^2=|C|^2$ überall und jederzeit gleich. Über die ganze Achse divergiert [(3.1)](#gl-3-1), man normiert deshalb auf ein großes Intervall der Länge $L$: $L\,|C|^2=1$ gibt $C=1/\sqrt L$. Für $L=10$ nm ist $C=10^{4}\,\mathrm{m^{-1/2}}$, und in einem Stück von 2 nm liegt das Elektron mit der Wahrscheinlichkeit 0,2.
::::

⁠**Grenzfall:** Für $L\to\infty$ geht $C\to0$. Eine Welle mit exakt einer Wellenlänge ist unendlich ausgedehnt und sagt nichts über den Ort.

:::frage Liegt dann ein Fünftel des Elektrons in diesem Stück von 2 nm?
Nein. Jeder Nachweis findet ein ganzes Elektron mit der Ladung $-e$. Die Zahl 0,2 sagt: Von vielen gleichen Versuchen endet ein Fünftel dort. Die Welle ist keine verschmierte Ladung, sie regelt die Häufigkeit.
:::

:::aufgabe Aufgabe 3 ★★ Normieren und Wahrscheinlichkeiten
<span class="anker" id="aufg-3"></span>

Zu einem festen Zeitpunkt sei $\Psi(x)=C\,\mathrm{e}^{-|x|/w}$ mit $w=1$ nm und $C>0$.

<ol class="al">

<li>

Bestimme $C$ aus [(3.1)](#gl-3-1) mit Zahlenwert und Einheit.

</li>

<li>

Wie wahrscheinlich liegt das Elektron zwischen $-w$ und $w$? Wie wahrscheinlich außerhalb von $\pm2w$?

</li>

<li>

Doppelspalt: Ein Spalt wird so verengt, dass dort nur die halbe Amplitude ankommt, $|\Psi_2|=|\Psi_1|/2$. Wie groß sind das hellste und das dunkelste $|\Psi|^2$ in Vielfachen von $|\Psi_1|^2$? Was ergäbe sich ohne Interferenz?

</li>

</ol>

:::loesung
(a) $\int|\Psi|^2\,\mathrm{d} x=2C^2\int_0^\infty\mathrm{e}^{-2x/w}\,\mathrm{d} x=C^2w=1$, also $C=1/\sqrt w=3{,}16\cdot10^{4}\,\mathrm{m^{-1/2}}$. (b) $2C^2\int_0^w\mathrm{e}^{-2x/w}\,\mathrm{d} x=1-\mathrm{e}^{-2}=0{,}865$. Außerhalb von $\pm2w$: $\mathrm{e}^{-4}=0{,}018$. (c) Hellste Stelle $(1+\frac12)^2=2{,}25$, dunkelste $(1-\frac12)^2=0{,}25$, ohne Interferenz überall $1+\frac14=1{,}25$. Die dunklen Streifen werden nicht mehr schwarz, weil sich ungleiche Zeiger nicht ganz auslöschen.
:::
:::
