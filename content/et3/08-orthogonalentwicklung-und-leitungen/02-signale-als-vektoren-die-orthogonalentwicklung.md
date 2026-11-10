---
title: Stufe 1: Signale als Vektoren, die Orthogonalentwicklung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Orthogonalentwicklung und Leitungen
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Kapitel 8: Orthogonalentwicklung und Leitungen
order: 3280200
summary: Die Fourier-Reihe zerlegt ein Signal nach Schwingungen.
tags: orthogonal, orthonormal, verallgemeinerte Parseval-Theorem
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die Fourier-Reihe zerlegt ein Signal nach Schwingungen. Dasselbe geht mit jedem System orthogonaler Funktionen. Diese Stufe zeigt, wie man die Koeffizienten findet und warum sie die beste Näherung liefern.
:::

**Die Idee.** Ein Vektor im Raum hat die Komponenten $b_i=\vec f\cdot\vec e_i$ bezüglich senkrechter Einheitsvektoren $\vec e_i$. Für Signale auf einem Intervall $[0,T]$ spielt das Integral $\int_0^Tf(t)g(t)\mathrm{d} t$ die Rolle des Skalarprodukts. Zwei Signale heißen __orthogonal__, wenn es null ist ([Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). Ein System von $M$ Funktionen $s_i(t)$ heißt __orthonormal__, wenn

<span class="anker" id="gl-1-1"></span>
$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}. \tag{1.1}$$

Man nähert ein Energiesignal $f(t)$ durch $\sum_{i=0}^{M-1}b_is_i(t)$, und es bleibt ein Rest $r(t)=f(t)-\sum b_is_i(t)$.

:::satz Satz 1.1 (Orthogonalentwicklung)
<span class="anker" id="satz-1-1"></span>

Die Energie des Rests $E_r=\int_0^Tr^2\mathrm{d} t$ ist am kleinsten für

<span class="anker" id="gl-1-2"></span>
$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t. \tag{1.2}$$

Dann gilt $E_r=E_f-\sum_ib_i^2$. Wird $E_r\to0$ mit wachsendem $M$ (vollständiges System), gilt das __verallgemeinerte Parseval-Theorem__ $E_f=\sum_ib_i^2$.
:::

:::herleitung Koeffizienten und Restenergie
$E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$. Ableiten nach $b_j$ und null setzen:

$$\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0\quad\Longrightarrow\quad\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t=b_j.$$

Die Orthonormalität lässt aus der Summe nur $i=j$ übrig. Setzt man diese $b_i$ ein und multipliziert aus, heben sich die gemischten Glieder wieder wegen der Orthonormalität weg: $E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$.
:::

⁠**So liest man das:** Jeder Koeffizient wird für sich bestimmt, unabhängig von den anderen. Nimmt man eine Basisfunktion hinzu, ändern sich die bisherigen Koeffizienten nicht. Das ist der Vorteil orthogonaler Systeme, genau wie bei der Fourier-Reihe ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). $b_i$ ist die Kreuzkorrelation $\varphi^E_{fs_i}(0)$. Deshalb kann man die Koeffizienten mit einer Bank von Korrelationsfiltern $h_i(t)=s_i(T-t)$ messen, deren Ausgänge man bei $t=T$ abtastet ([Kapitel 7](/wissen/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)).

::::beispiel
$f(t)=t^2$ auf $[0,1]$, $E_f=\frac15$. Mit $s_0=1$ und $s_1=\sqrt3(2t-1)$:

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0{,}289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

Die Näherung ist $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$, die beste Gerade im Sinne der Energie. Die Restenergie ist $\frac15-\frac7{36}=\frac{1}{180}=0{,}0056$, also 2,8 % von $E_f$. Mit $s_2=\sqrt5(6t^2-6t+1)$ kommt $b_2=\frac{\sqrt5}{30}=0{,}075$ dazu, und der Rest wird null, weil $t^2$ selbst ein Polynom zweiten Grades ist.
::::

:::aufgabe Aufgabe 1 ★ Orthonormal prüfen
<span class="anker" id="aufg-1"></span>

Zeige, dass $s_0=1$ und $s_1=\sqrt3(2t-1)$ auf $[0,1]$ orthonormal sind. Warum braucht $s_1$ den Faktor $\sqrt3$?

:::loesung
$\int_0^11\cdot\sqrt3(2t-1)\mathrm{d} t=\sqrt3\,[t^2-t]_0^1=0$: orthogonal. $\int_0^11^2\mathrm{d} t=1$. $\int_0^13(2t-1)^2\mathrm{d} t=3\cdot\bigl[\frac{(2t-1)^3}{6}\bigr]_0^1=3\cdot\frac{1+1}{6}=1$. Ohne den Faktor wäre die Energie von $2t-1$ nur $\frac13$. Der Faktor $\sqrt3$ normiert sie auf 1, sonst wäre $b_1=\int fs_1\mathrm{d} t$ nicht der richtige Koeffizient.
:::
:::

:::aufgabe Aufgabe 2 ★★ Beste Näherung
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Rechne $b_1$ für $f(t)=t^2$ nach und bestätige die Näherung $t-\frac16$.

</li>

<li>

Prüfe $E_r=\frac{1}{180}$, indem du $\int_0^1\bigl(t^2-t+\frac16\bigr)^2\mathrm{d} t$ direkt berechnest.

</li>

<li>

Bestimme die Koeffizienten von $f(t)=\sqrt2\cos(2\pi t)$ bezüglich $s_0$ und $s_1$. Was bedeutet das Ergebnis?

</li>

</ol>

:::loesung
(a) $\int_0^1t^2(2t-1)\mathrm{d} t=\frac24-\frac13=\frac16$, also $b_1=\frac{\sqrt3}{6}$. Näherung: $\frac13+\frac{\sqrt3}{6}\cdot\sqrt3(2t-1)=\frac13+t-\frac12=t-\frac16$.

(b) $\int_0^1\bigl(t^2-t+\tfrac16\bigr)^2\mathrm{d} t=\int_0^1\bigl(t^4-2t^3+\tfrac43t^2-\tfrac13t+\tfrac1{36}\bigr)\mathrm{d} t=\tfrac15-\tfrac12+\tfrac49-\tfrac16+\tfrac1{36}=\tfrac{1}{180}$.

(c) $b_0=\sqrt2\int_0^1\cos(2\pi t)\mathrm{d} t=0$ und $b_1=\sqrt6\int_0^1(2t-1)\cos(2\pi t)\mathrm{d} t=0$ (der Kosinus ist symmetrisch um $t=\frac12$, $2t-1$ antisymmetrisch). Beide Koeffizienten sind null: Die Funktion ist zu beiden Basisfunktionen orthogonal, die Näherung ist null, und der ganze Signalinhalt bleibt im Rest. Eine Basis taugt nur für Signale, die ihren Funktionen ähneln.
:::
:::
