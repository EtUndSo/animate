---
title: Stufe 5: Spin und Pauli-Prinzip
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Atome und Orbitale
order: 4140700
summary: Bisher gab es ein Elektron.
tags: ununterscheidbar, magnetische Spinquantenzahl, antisymmetrisch
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Bisher gab es ein Elektron. Bei mehreren stellt sich eine neue Frage: Warum fallen nicht alle ins 1s-Orbital? Diese Stufe führt die vierte Quantenzahl ein und die Regel, die das verbietet.
:::

**Die Idee.** Elektronen sind __ununterscheidbar__: Man kann sie nicht markieren. Vertauscht man zwei, darf sich nichts Messbares ändern, also bleibt $|\psi|^2$ gleich. Dann kann $\psi$ beim Tausch höchstens das Vorzeichen wechseln, und bei Elektronen wechselt es. Das erzeugt ein Verbot: Eine Funktion, die beim Tausch zweier gleicher Argumente ihr Vorzeichen wechselt, ist gleich ihrem Negativen, also null.

:::definition Definition 5.1 (Spin)
<span class="anker" id="satz-5-1"></span>

Das Elektron hat einen eigenen Drehimpuls $\boldsymbol S$ mit festem Betrag $|\boldsymbol S|=\frac{\sqrt3}{2}\hbar$, den Spin. Seine Komponente in $z$-Richtung ist

<span class="anker" id="gl-5-1"></span>
$$S_z=\hbar\,m_s,\qquad m_s=\pm\tfrac12. \tag{5.1}$$
:::

⁠**So liest man das:** $m_s$ ist die __magnetische Spinquantenzahl__, geschrieben als Pfeil: $\uparrow$ für $+\frac12$, $\downarrow$ für $-\frac12$. Mit $n$, $\ell$, $m_\ell$ und $m_s$ ist der Zustand eines gebundenen Elektrons vollständig beschrieben. Der Spin ist keine Drehung eines Körpers, sondern eine Eigenschaft wie die Ladung, mit zwei Einstellungen.

:::satz Satz 5.2 (Antisymmetrie und Pauli-Prinzip)
<span class="anker" id="satz-5-2"></span>

Für Elektronen gilt beim Vertauschen zweier Elektronen

<span class="anker" id="gl-5-2"></span>
$$\psi(x_1,s_1;x_2,s_2;x_3,s_3;\dots)=-\psi(x_2,s_2;x_1,s_1;x_3,s_3;\dots). \tag{5.2}$$

Daraus folgt: In einem Atom stimmen zwei Elektronen nie in allen vier Quantenzahlen überein. Jedes Orbital fasst höchstens zwei Elektronen, und die haben entgegengesetzten Spin.
:::

⁠**So liest man das:** $x_i$ steht für den Ort des Elektrons $i$, $s_i$ für seinen Spin, also $\uparrow$ oder $\downarrow$. Das kursive $s_i$ ist nicht das aufrechte s der Orbitale. Eine Wellenfunktion mit [(5.2)](#gl-5-2) heißt __antisymmetrisch__. **Gültigkeit:** für alle Elektronen. Das Minuszeichen ist eine Erfahrungstatsache.

:::herleitung Vom Vertauschen zum Verbot
<ol>

<li>

Messbar ist nur das Betragsquadrat, also gilt $|\psi(x_1,s_1;x_2,s_2;x_3,\dots)|^2=|\psi(x_2,s_2;x_1,s_1;x_3,\dots)|^2$.

</li>

<li>

Der Tausch multipliziert $\psi$ daher mit einem Faktor vom Betrag 1. Zweimal getauscht ist alles wie vorher, also ist der Faktor $\pm1$: $\psi(x_1,s_1;x_2,s_2;\dots)=\pm\psi(x_2,s_2;x_1,s_1;\dots)$. Für Elektronen gilt das Minus.

</li>

<li>

Für trennbaren Ort und Spin gilt $\psi(x_1,s_1;\dots)=\Phi(x_1,x_2,x_3,\dots)\,\chi(s_1,s_2,s_3,\dots)$.

</li>

<li>

⁠**Gleicher Ort,** $x_1=x_2$: Es gilt $\Phi(x_1,x_1,x_3,\dots)\,\chi(s_1,s_2,s_3,\dots)=-\Phi(x_1,x_1,x_3,\dots)\,\chi(s_2,s_1,s_3,\dots)$. Ist auch $s_1=s_2$, steht rechts das Negative der linken Seite:

$$\Phi(x_1,x_1,x_3,\dots)\,\chi(s_1,s_1,s_3,\dots)=-\Phi(x_1,x_1,x_3,\dots)\,\chi(s_1,s_1,s_3,\dots)=0.$$

Also verlangt $x_1=x_2$, dass $s_1\ne s_2$ ist.

</li>

<li>

⁠**Gleicher Spin,** $s_1=s_2$: Hier folgt $\Phi(x_1,x_2,x_3,\dots)\,\chi(s_1,s_1,s_3,\dots)=-\Phi(x_2,x_1,x_3,\dots)\,\chi(s_1,s_1,s_3,\dots)$. $\Phi$ selbst ist antisymmetrisch und damit bei $x_1=x_2$ null. Also verlangt $s_1=s_2$, dass $x_1\ne x_2$ ist.

</li>

<li>

⁠**Gleicher Zustand.** Zwei Elektronen mit gleichem Spin in den Orbitalen $u$ und $v$ haben $\Phi=\frac{1}{\sqrt2}[\psi_u(x_1)\psi_v(x_2)-\psi_v(x_1)\psi_u(x_2)]$. Für $u=v$ ist das null, dieser Zustand existiert nicht. Mit entgegengesetztem Spin geht es: Dann ist $\chi$ antisymmetrisch und $\Phi$ symmetrisch. Ein drittes Elektron hätte mit einem der beiden denselben Spin und wird verboten.

</li>

</ol>
:::

:::abbildung gemb1/k4austausch 5
Zwei Elektronen in der Box der Breite $L$, in den Zuständen $n=1$ und $n=2$. Das erste sitzt bei $x_1=0{,}3\,L$ (gestrichelt), aufgetragen ist die Dichte für das zweite. Links: gleicher Spin, $\Phi$ antisymmetrisch. Die beiden meiden sich. Rechts: Spins antiparallel mit antisymmetrischem $\chi$, $\Phi$ symmetrisch. Beide dürfen am selben Ort sein.
:::

**Beispiel.** Aus zwei Elektronen je Orbital und $2\ell+1$ Orbitalen je Unterschale folgt die Kapazität einer Schale:

<span class="anker" id="gl-5-3"></span>
$$\sum_{\ell=0}^{n-1}2\,(2\ell+1)=2n^2. \tag{5.3}$$

Das sind 2, 8, 18 und 32 Plätze für $n=1$ bis 4. Wie stark das Verbot wirkt, zeigen zehn Elektronen in einer Box mit $L=1$ nm, deren tiefster Zustand bei 0,376 eV liegt: Wären alle im untersten Zustand, ergäbe das 3,76 eV. Mit je zwei Elektronen pro Zustand sind es $2(1+4+9+16+25)\cdot0{,}376\,\mathrm{eV}=41{,}4$ eV. **Grenzfall:** Überlappen sich $\psi_u$ und $\psi_v$ nicht, etwa in zwei weit entfernten Atomen, fällt in $|\Phi|^2$ der gemischte Term weg. Dann ergeben Plus- und Minuszeichen dieselbe Dichte, und das Verbot wirkt nicht mehr.

:::frage Ist das Pauli-Prinzip eine abstoßende Kraft zwischen Elektronen?
Nein. In [(1.2)](der-kern-als-kasten-ohne-wande.html#gl-1-2) kommt kein zusätzlicher Term vor. Das Prinzip streicht Lösungen: Bestimmte Wellenfunktionen gibt es nicht. Es gilt deshalb auch für ungeladene Teilchen wie Neutronen. Die Folgen sehen aber aus wie eine Kraft, denn die übrigen Zustände haben mehr Energie.
:::

:::aufgabe Aufgabe 7 ★ Plätze vergeben
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Schreibe die vier Quantenzahlen aller acht Plätze der Schale $n=2$ auf.

</li>

<li>

Wie viele Elektronen fasst die Schale $n=5$?

</li>

<li>

Dürfen zwei Elektronen desselben Atoms die Werte $(3,1,0,+\frac12)$ und $(3,1,1,+\frac12)$ haben? Und zweimal $(3,1,0,+\frac12)$?

</li>

</ol>

:::loesung
(a) $(2,0,0,\pm\frac12)$, $(2,1,-1,\pm\frac12)$, $(2,1,0,\pm\frac12)$, $(2,1,1,\pm\frac12)$. (b) $2\cdot5^2=50$. (c) Das erste Paar ist erlaubt, denn $m_\ell$ unterscheidet sich. Zweimal dieselben vier Zahlen sind verboten.
:::
:::

:::aufgabe Aufgabe 8 ★★ Zwei Elektronen in der Box
<span class="anker" id="aufg-8"></span>

Nimm $\Phi(x_1,x_2)=\frac{1}{\sqrt2}[\psi_1(x_1)\psi_2(x_2)-\psi_2(x_1)\psi_1(x_2)]$ mit $\psi_n(x)=\sqrt{2/L}\,\sin(n\pi x/L)$.

<ol class="al">

<li>

Zeige $\Phi(x_2,x_1)=-\Phi(x_1,x_2)$ und $\Phi(x,x)=0$.

</li>

<li>

Berechne $L^2|\Phi|^2$ für $x_1=0{,}25\,L$, $x_2=0{,}75\,L$ und für $x_1=x_2=0{,}5\,L$.

</li>

<li>

Vorhersage: Wie sähe ein Siliziumatom aus, wenn für Elektronen das Pluszeichen gälte?

</li>

</ol>

:::loesung
(a) Der Tausch vertauscht die beiden Produkte in der Klammer, das dreht das Vorzeichen. Für $x_1=x_2$ sind beide Produkte gleich. (b) Bei $x_1=0{,}25\,L$, $x_2=0{,}75\,L$ ist $\psi_1=\sqrt{1/L}$ an beiden Stellen und $\psi_2=\pm\sqrt{2/L}$. Damit ist $\Phi=-2/L$ und $L^2|\Phi|^2=4$. Für $x_1=x_2$ ist $L^2|\Phi|^2=0$. (c) Alle 14 Elektronen lägen im 1s-Orbital. Es gäbe keine Schalen und keine Periodizität.
:::
:::
