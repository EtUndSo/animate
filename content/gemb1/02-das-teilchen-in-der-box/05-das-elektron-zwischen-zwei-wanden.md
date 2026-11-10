---
title: Stufe 3: Das Elektron zwischen zwei Wänden
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Das Teilchen in der Box
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box
knoten: Kapitel 2: Das Teilchen in der Box
order: 4120500
summary: Bisher konnte das Elektron überall hin.
tags: Randbedingung, Quantenzahl, Quantisierung, Knoten, Nullpunktsenergie, Korrespondenzprinzip, Delokalisierung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bisher konnte das Elektron überall hin. Jetzt sperren zwei Wände es ein. Diese Stufe zeigt, warum dann nur noch bestimmte Energien erlaubt sind.
:::

**Die Idee.** Klassisch fliegt ein Teilchen kräftefrei zwischen den Wänden hin und her, wird elastisch reflektiert, ist überall gleich oft anzutreffen und darf jede Energie haben. Quantenmechanisch laufen zwei ebene Wellen $\mathrm{e}^{\mathrm{j} kx}$ und $\mathrm{e}^{-\mathrm{j} kx}$ gegeneinander und bilden eine stehende Welle. Sie muss an beiden Wänden null sein. Zwischen zwei feste Enden passen nur ganze Vielfache der halben Wellenlänge: $L=n\lambda/2$. Damit ist $k$ festgelegt, und die Dispersion macht daraus die Energie. Das Einsperren wählt aus der Parabel einzelne Punkte aus (Abb. [3](#abb-3)).

:::analogie
Eine Gitarrensaite ist an beiden Enden eingespannt und schwingt nur im Grundton und in Obertönen. Die Länge bestimmt die Töne, genau wie $L$ die Energien. Das Bild endet bei der Reihenfolge: Bei der Saite ist die Frequenz proportional zu $k$, die Obertöne liegen gleichmäßig. Beim Elektron ist die Energie proportional zu $k^2$. Außerdem ist die Auslenkung der Saite messbar, $\psi$ selbst nicht.
:::

**Das Modell.** Im Inneren ($0<x<L$) ist $V=0$, außerhalb geht $V\to\infty$. Dort lässt sich [(0.1)](von-grund-auf-was-aus-teil-1-gebraucht-wird.html#gl-0-1) nur mit $\psi=0$ erfüllen, das Elektron existiert in den Wänden nicht. Weil $\psi$ stetig ist, folgt die __Randbedingung__ $\psi(0)=\psi(L)=0$.

:::satz Satz 3.1 (Box in einer Dimension)
<span class="anker" id="satz-3-1"></span>

Die erlaubten Wellenzahlen, Wellenfunktionen und Energien sind, für $n=1,2,3,\dots$,

<span class="anker" id="gl-3-1"></span>
$$k_n=n\frac\pi L,\qquad\psi_n(x)=\mathrm{j}\sqrt{\frac2L}\,\sin\Bigl(n\frac\pi Lx\Bigr),\qquad E_n=\frac{\hbar^2\pi^2}{2mL^2}\,n^2=\frac{h^2}{8mL^2}\,n^2. \tag{3.1}$$

Liegt der Boden der Box bei $V_0$, kommt $V_0$ zu $E_n$ hinzu.
:::

:::herleitung Von der Randbedingung zur Energie
<ol>

<li>

Innen gilt $\psi''=-k^2\psi$ mit $k^2=2mE/\hbar^2$. Ansatz: $\psi(x)=A\,\mathrm{e}^{\mathrm{j} kx}+B\,\mathrm{e}^{-\mathrm{j} kx}$. Gleichwertig ist die Form mit Sinus und Kosinus.

</li>

<li>

$\psi(0)=A+B=0$ ergibt $B=-A$, also $\psi(x)=2\mathrm{j} A\sin(kx)$. Der Kosinus fällt weg, weil er bei $x=0$ nicht null ist.

</li>

<li>

$\psi(L)=2\mathrm{j} A\sin(kL)=0$ verlangt für $A\neq0$ die Bedingung $kL=n\pi$.

</li>

<li>

Normierung mit $q=n\pi x/L$:

$$\int_0^L|\psi_n|^2\,\mathrm{d} x=4|A|^2\,\frac L{n\pi}\int_0^{n\pi}\sin^2q\;\mathrm{d} q=4|A|^2\,\frac L{n\pi}\Bigl[\frac q2-\frac{\sin2q}4\Bigr]_0^{n\pi}=2|A|^2L\overset!=1.$$

Also ist $A=\sqrt{1/(2L)}$.

</li>

<li>

$E_n=\hbar^2k_n^2/(2m)$ ergibt die Energie. Mit $\hbar=h/(2\pi)$ folgt die zweite Form.

</li>

</ol>
:::

:::abbildung gemb1/k2box 3
Rechenmodell $L=2$ nm. Oben links: Niveaus $E_1=94$ meV, $E_2=376$ meV, $E_3=846$ meV (rot), darauf die Wellenfunktionen (blau, Höhe willkürlich). Oben rechts: Die Box wählt aus der Parabel die Punkte $k_n$. Unten: $L|\psi_n|^2$ über $x/L$; gestrichelt der klassische Wert. Bei $n=30$ sind die Berge nicht mehr zu trennen.
:::

⁠**So liest man das:** $n$ ist die __Quantenzahl__, sie zählt die Zustände. Dass nur einzelne Energien erlaubt sind, heißt __Quantisierung__. $n=0$ ergäbe $\psi\equiv0$, also kein Teilchen. Negative $n$ ändern nur das Vorzeichen und sind kein neuer Zustand. Der Faktor $\mathrm{j}$ ist eine Phase: $|\psi_n|^2$ ändert sich nicht, $\sqrt{2/L}\,\sin(n\pi x/L)$ ist dieselbe Lösung. $\psi_n$ hat im Inneren $n-1$ Nullstellen, die __Knoten__.

Der tiefste Zustand heißt Grundzustand, seine Energie $E_1>0$ __Nullpunktsenergie__: Ein eingesperrtes Teilchen ruht nie. Der Grund ist die Krümmung: Eine Funktion, die an beiden Wänden null und dazwischen nicht null ist, muss gekrümmt sein, und Krümmung ist kinetische Energie. Drei Abhängigkeiten sind zu merken. Aus $E_n\propto n^2$ folgt der Abstand $E_{n+1}-E_n=(2n+1)E_1$, die Niveaus rücken nach oben auseinander. Aus $E_n\propto1/L^2$ folgt: Halbe Box, vierfache Energie. Aus $E_n\propto1/m$ folgt: Leichte Teilchen zeigen die Quantisierung stärker.

::::beispiel
Im Rechenmodell ist $E_1=0{,}376\,\mathrm{eV\,nm^2}/(2\,\mathrm{nm})^2=94$ meV, $E_2=4E_1=376$ meV, $E_3=9E_1=846$ meV. Dieselbe Formel gibt für $L=50$ nm nur 0,15 meV, für $L=0{,}2$ nm, also Atomgröße, schon 9,4 eV.
::::

⁠**Grenzfälle:** Für $L\to\infty$ gehen alle Abstände gegen null, das Spektrum wird kontinuierlich wie beim freien Elektron. Für $n\to\infty$ schwingt $|\psi_n|^2$ so schnell, dass kein Messgerät die Berge trennt. Es bleibt der Mittelwert $1/L$, genau die klassische Gleichverteilung. Diese Übereinstimmung heißt __Korrespondenzprinzip__.

:::frage $\psi_n$ hat an der Wand einen Knick. Muss $\psi$ nicht glatt sein?
Ein Knick bedeutet dort eine unendliche zweite Ableitung. Im Inneren wäre das unmöglich, denn in [(0.1)](von-grund-auf-was-aus-teil-1-gebraucht-wird.html#gl-0-1) steht sonst nichts Unendliches, was sie ausgleicht. An der unendlich hohen Wand ist $V$ selbst unendlich, und nur dort ist der Knick erlaubt.
:::

:::zusatz Nullpunktsenergie und chemische Bindung
Dass die Grundzustandsenergie mit der Größe des Aufenthaltsbereichs sinkt, gilt für jede Form des Potentials. Teilen sich zwei Atome ein Elektron, wird sein Bereich größer als ein einzelnes Atom, und die Nullpunktsenergie sinkt (__Delokalisierung__). Dieser Gewinn trägt merklich zur Festigkeit der Bindung bei.
:::

:::aufgabe Aufgabe 3 ★ Zwei Boxen vergleichen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Berechne $E_1$, $E_2$ und $E_3$ für $L=1$ nm.

</li>

<li>

Box A hat $L_\mathrm A=6$ nm, Box B hat $L_\mathrm B=2$ nm. Um welchen Faktor liegt $E_n$ in B höher? Um welchen Faktor ist das Maximum von $|\psi_n|$ größer? Skizziere beide Boxen mit den ersten drei Niveaus und $\psi_n$.

</li>

<li>

Vorhersage: Wie entwickelt sich der relative Abstand $(E_{n+1}-E_n)/E_n$ für große $n$?

</li>

</ol>

:::loesung
(a) $E_1=0{,}376$ eV, $E_2=1{,}50$ eV, $E_3=3{,}38$ eV. (b) $E_n\propto1/L^2$ gibt den Faktor 9. Das Maximum $\sqrt{2/L}$ wächst um $\sqrt3=1{,}73$, weil dieselbe Wahrscheinlichkeit 1 auf ein Drittel der Länge passen muss. In Einheiten von $E_1$ der Box A liegen die Niveaus von A bei 1, 4, 9, die von B bei 9, 36, 81. (c) $(E_{n+1}-E_n)/E_n=(2n+1)/n^2$ fällt: 3 bei $n=1$, 0,21 bei $n=10$, 0,02 bei $n=100$. Für große $n$ wirkt das Spektrum kontinuierlich.
:::
:::

:::aufgabe Aufgabe 4 ★★ Wo sitzt das Elektron?
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Zeige für das linke Viertel der Box: $P=\int_0^{L/4}|\psi_n|^2\,\mathrm{d} x=\frac14-\frac{\sin(n\pi/2)}{2n\pi}$.

</li>

<li>

Berechne $P$ für $n=1,2,3,31$.

</li>

<li>

Was sagt die klassische Rechnung? Was bedeutet das Ergebnis für große $n$?

</li>

</ol>

:::loesung
(a) $\sin^2u=\frac12(1-\cos2u)$ ergibt $\int_0^{L/4}\frac2L\sin^2(n\pi x/L)\,\mathrm{d} x=\bigl[\frac xL-\frac{\sin(2n\pi x/L)}{2n\pi}\bigr]_0^{L/4}$. (b) $n=1$: 0,091, $n=2$: 0,250, $n=3$: 0,303, $n=31$: 0,255. (c) Klassisch ist $P=\frac14$. Der Korrekturterm fällt wie $1/n$. Bei $n=1$ hält der Wellenberg das Elektron von der Wand fern, für große $n$ gilt die klassische Gleichverteilung.
:::
:::

:::aufgabe Aufgabe 5 ★★★ Die Box auf dem Gitter
<span class="anker" id="aufg-5"></span>

Die Box wird mit $N$ inneren Punkten diskretisiert, also $L=(N+1)a$ und $\psi_0=\psi_{N+1}=0$, mit $V_\ell=0$.

<ol class="al">

<li>

Schreibe für $N=3$ die Matrix hin und berechne die drei Eigenwerte in Einheiten von $t_0$.

</li>

<li>

Zeige: $\psi_\ell=\sin(n\pi\ell/(N+1))$ erfüllt [(1.1)](die-schrodinger-gleichung-auf-einem-gitter.html#gl-1-1) und die Ränder, und es gilt $E_n=2t_0\bigl(1-\cos(n\pi/(N+1))\bigr)$. Das sind genau die Punkte $k_n=n\pi/L$ auf dem Kosinus-Band.

</li>

<li>

Vergleiche im Rechenmodell ($N=9$) die Werte $E_1$, $E_2$, $E_3$ mit [(3.1)](#gl-3-1). Warum wird die Abweichung mit $n$ größer?

</li>

</ol>

:::loesung
(a) Die Matrix hat die Diagonale $2t_0$ und die Nebendiagonalen $-t_0$. Aus $\det(\boldsymbol H-E\mathbf 1)=0$ folgt $(2-\varepsilon)\bigl((2-\varepsilon)^2-2\bigr)=0$ mit $\varepsilon=E/t_0$, also $\varepsilon=2-\sqrt2$, $2$, $2+\sqrt2=0{,}586$, $2$, $3{,}414$. (b) Die Summe $\sin(u+v)+\sin(u-v)=2\sin u\cos v$ mit $u=n\pi\ell/(N+1)$ und $v=n\pi/(N+1)$ ergibt $\psi_{\ell+1}+\psi_{\ell-1}=2\cos v\;\psi_\ell$, also $E=2t_0(1-\cos v)$. Die Ränder stimmen, denn $\sin0=\sin(n\pi)=0$. Mit $L=(N+1)a$ ist $v=k_na$. (c) Gitter: 93,3, 363,9 und 785,4 meV. Formel [(3.1)](#gl-3-1): 94,0, 376,1 und 846,2 meV. Die Abweichung ist $-0{,}8$ %, $-3{,}2$ % und $-7{,}2$ %: Mit wachsendem $n$ wächst $k_na$, die Welle spürt das Gitter.
:::
:::
