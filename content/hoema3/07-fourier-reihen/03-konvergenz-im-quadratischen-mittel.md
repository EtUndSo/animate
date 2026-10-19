---
title: Konvergenz von Fourier-Reihen im quadratischen Mittel
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3070300
summary: Von Grund auf – das Fourierpolynom $T_Nf$ ist die orthogonale Projektion von $f$ auf die trigonometrischen Polynome vom Grad $\le N$, also die beste $L^2$-Approximation. Daraus folgen der Satz von Pythagoras, die Besselsche Ungleichung $\sum|c_k|^2\le\|f\|_2^2$ und – weil das trigonometrische System vollständig ist – die Konvergenz im quadratischen Mittel $T_Nf\to f$ mit der Parseval-Gleichung $\|f\|_2^2=\sum_{k}|c_k|^2$. Anwendung: $\sum 1/k^2=\pi^2/6$.
tags: L2-Konvergenz, orthogonale Projektion, Bestapproximation, Besselsche Ungleichung, Parseval-Gleichung, Pythagoras, Riemann-Lebesgue, Basel-Problem
---

:::grafik
Einstiegs-Animation: Der Funktionenraum als „Raum" dargestellt, darin eine endlichdimensionale Ebene $V_N$ (die
trigonometrischen Polynome vom Grad $\le N$). Eine Funktion $f$ schwebt darüber; ihr nächster Punkt in $V_N$ ist der
__Lotfußpunkt__ $T_Nf$ — die **orthogonale Projektion**. Der Fehler $f-T_Nf$ steht **senkrecht** auf $V_N$, und das
Dreieck $f,\,T_Nf,\,$ ein beliebiges $S_N$ erfüllt __Pythagoras__. Wächst $N$, füllt $V_N$ den Raum immer mehr aus und
$T_Nf\to f$. Kernbotschaft: Fourier = orthogonale Projektion = beste Approximation im quadratischen Mittel.
:::

:::konzept
Die Beispiele im letzten Artikel waren Handarbeit. Jetzt kommt der __abstrakte Zugang__, der alles auf einmal erklärt —
und der sich auf jedes Orthonormalsystem überträgt (Legendre-, Tschebyschew-Polynome usw.). Die Idee ist reine
**lineare Algebra im Funktionenraum**: Das Fourierpolynom $T_Nf$ ist die __orthogonale Projektion__ von $f$ auf den
Unterraum der trigonometrischen Polynome — und eine Projektion liefert immer den **nächstgelegenen** Punkt. Daraus
fallen die drei Grundpfeiler: __Pythagoras__, die __Besselsche Ungleichung__ (die „Energie" der Koeffizienten ist
beschränkt) und — weil das trigonometrische System **vollständig** ist — die __Parseval-Gleichung__ und die
$L^2$-Konvergenz jeder Fourier-Reihe.
:::

**Worum es geht:** Wir verstehen $T_Nf$ als __Projektion__ (Bestapproximation), beweisen __Pythagoras__ und
__Bessel__ (Lemma 7.11), und erhalten die $L^2$-__Konvergenz__ mit der __Parseval-Gleichung__ (Satz 7.13).

## Fourierpolynome als Projektion

Sei $V_N=\{\text{komplex-trigonometrische Polynome vom Grad}\le N\}$. Das ist ein komplexer Vektorraum der Dimension
$2N+1$ (identifizierbar mit $\mathbb{C}^{2N+1}$); seine Elemente sind $S_N=\sum_{|k|\le N}\gamma_k\hat e_k$. Wegen der
Orthonormalität der $\hat e_k$ berechnet sich die $L^2$-Norm wie die euklidische Norm des Koeffizientenvektors:

$$\|S_N\|_2^2=\sum_{|k|\le N}|\gamma_k|^2.$$

In $\mathbb{R}^n$ ist die Bestapproximation eines Vektors $v$ in einem Unterraum $V_m$ mit Orthonormalbasis
$\{\hat e_1,\dots,\hat e_m\}$ gerade die Projektion $v_0=\sum_k(v\cdot\hat e_k)\hat e_k$ (Bemerkung 7.10). Genau das
imitieren wir mit dem $L^2$-Skalarprodukt: Der __Projektionsoperator__

$$T_N:\ f\longmapsto T_Nf=\sum_{|k|\le N}\langle f,\hat e_k\rangle\,\hat e_k\in V_N$$

bildet $f$ auf ihr nächstes trigonometrisches Polynom ab.

## Pythagoras, Bestapproximation und Bessel

**Lemma 7.11.** Für $2\pi$-periodisches, über $[0,2\pi]$ $R$-integrierbares $f$, alle $N$ und beliebiges $S_N\in V_N$:

$$\text{(i)}\quad \|f-S_N\|_2^2=\|f-T_Nf\|_2^2+\|T_Nf-S_N\|_2^2 \qquad(\text{Pythagoras}),$$
$$\text{(ii)}\quad \|f-S_N\|_2^2\ge\|f-T_Nf\|_2^2 \qquad(L^2\text{-Bestapproximation}),$$
$$\text{(iii)}\quad \|f-T_Nf\|_2^2=\|f\|_2^2-\|T_Nf\|_2^2, \qquad \text{(iv)}\quad \|T_Nf\|_2^2\le\|f\|_2^2 \quad(\text{Bessel}).$$

*Beweis.* Der Kern ist die **Orthogonalität des Fehlers**: Da $T_Nf-S_N\in V_N$ und $\langle f-T_Nf,\hat e_k\rangle=0$
für alle $|k|\le N$ (die Projektion zieht genau die Komponenten in $V_N$ ab), ist $\langle f-T_Nf,\ T_Nf-S_N\rangle=0$.
Mit Pythagoras ($\|a+b\|^2=\|a\|^2+\|b\|^2$ bei $\langle a,b\rangle=0$) folgt (i), und da der zweite Summand $\ge0$ ist,
(ii) — $T_Nf$ ist die beste Approximation. Mit $S_N=0$ folgen (iii) und (iv). $\square$

**Besselsche Ungleichung** (Bemerkung 7.12) konkret: $\sum_{|k|\le N}|c_k|^2\le\frac{1}{2\pi}\int_0^{2\pi}|f(x)|^2\,dx$.
Da die linke Seite in $N$ wächst und beschränkt bleibt, bilden die Fourier-Koeffizienten eine **Nullfolge**
($\lim_{|k|\to\infty}\int_0^{2\pi}f(x)e^{ikx}\,dx=0$ — das __Riemann-Lebesgue-Lemma__): Je höher die Frequenz, desto
weniger steckt davon in einer integrierbaren Funktion.

:::grafik
Links die Projektion: $f$, die Ebene $V_N$, der Lotfußpunkt $T_Nf$, der Fehlervektor $f-T_Nf\perp V_N$, ein beliebiges
$S_N\in V_N$ weiter weg; das rechtwinklige Dreieck illustriert Pythagoras (i). Rechts die Bessel-Bilanz als Balken:
$\|f\|_2^2$ (ganzer Balken) teilt sich in $\|T_Nf\|_2^2=\sum_{|k|\le N}|c_k|^2$ (erfasst) und $\|f-T_Nf\|_2^2$ (Rest),
der mit $N$ schrumpft.
:::

## $L^2$-Konvergenz und die Parseval-Gleichung

Das trigonometrische System ist **vollständig** — es lässt keinen Rest übrig:

**Satz 7.13 (Konvergenz im quadratischen Mittel).** Für $2\pi$-periodisches, über $[0,2\pi]$ $R$-integrierbares $f$
konvergiert die Fourier-Reihe im quadratischen Mittel, $T_Nf\to f$, und es gilt die __Parseval-Identität__

$$\frac{1}{2\pi}\int_0^{2\pi}|f(x)|^2\,dx=\sum_{n\in\mathbb{Z}}|c_n|^2.$$

Nach Lemma 7.11 (iii) ist $T_Nf\to f$ im quadratischen Mittel **gleichbedeutend** mit $\|T_Nf\|_2^2=\sum_{|k|\le N}
|c_k|^2\to\|f\|_2^2$ — aus der Bessel-**Ungleichung** wird im Limes die Parseval-**Gleichung**. Man zeigt das zunächst
für **Treppenfunktionen** (schon eine einzelne Stufe genügt) und überträgt es durch deren Dichtheit auf alle
$R$-integrierbaren Funktionen. Physikalisch ist Parseval die __Energieerhaltung__: Die „Gesamtenergie" $\|f\|_2^2$ im
Zeitbereich ist gleich der Summe der Energien $|c_n|^2$ der einzelnen Frequenzen (Spektrum). In reeller Form lautet sie

$$\frac{1}{\pi}\int_0^{2\pi}|f(x)|^2\,dx=\frac{a_0^2}{2}+\sum_{k=1}^\infty\big(a_k^2+b_k^2\big).$$

## Anwendung: das Basel-Problem

Jetzt lösen wir das im letzten Artikel offen gebliebene $C$ — und bekommen eine berühmte Summe geschenkt. Für den
**Sägezahn** $f(x)=\frac{\pi-x}{2}=\sum_{k\ge1}\frac{\sin kx}{k}$ sind die komplexen Koeffizienten $c_k=\frac{1}{2ik}$
($k\ge1$), $c_{-k}=-\frac{1}{2ik}$, $c_0=0$, also $|c_k|^2=\frac{1}{4k^2}$ für $k\neq0$. Die linke Seite der
Parseval-Gleichung ist

$$\frac{1}{2\pi}\int_0^{2\pi}\Big(\frac{\pi-x}{2}\Big)^2dx=\frac{1}{8\pi}\int_0^{2\pi}(\pi-x)^2\,dx=\frac{1}{8\pi}\cdot\frac{2\pi^3}{3}=\frac{\pi^2}{12}.$$

Parseval gibt also $\frac{\pi^2}{12}=\sum_{k\neq0}\frac{1}{4k^2}=\frac12\sum_{k=1}^\infty\frac{1}{k^2}$, und damit das
berühmte __Basel-Problem__

$$\sum_{k=1}^\infty\frac{1}{k^2}=\frac{\pi^2}{6}.$$

Daraus folgt auch die Konstante aus Lemma 7.9: $C=\sum_{k=1}^\infty\frac{(-1)^{k+1}}{k^2}=\frac{\pi^2}{12}$ (die
alternierende Variante).

**Stolperstein:** (1) $L^2$-Konvergenz ist **nicht** punktweise Konvergenz — $T_Nf$ kann an einzelnen Punkten (Sprüngen)
danebenliegen, obwohl $\|f-T_Nf\|_2\to0$ (die Integralnorm verzeiht Einzelpunkte). (2) __Bessel__ gilt für **jedes**
Orthonormalsystem (Ungleichung); __Parseval__ (Gleichheit) nur, wenn das System **vollständig** ist — beim
trigonometrischen System ist das der Fall. (3) Normierung beachten: komplex $\frac{1}{2\pi}$, reell $\frac1\pi$ (und der
Sonderterm $\frac{a_0^2}{2}$).

:::kern
$V_N$ (trig. Polynome Grad $\le N$, dim $2N+1$); $\|S_N\|_2^2=\sum_{|k|\le N}|\gamma_k|^2$. __Projektionsoperator__
$T_Nf=\sum_{|k|\le N}\langle f,\hat e_k\rangle\hat e_k$ = __Bestapproximation__ in $V_N$. __Lemma 7.11__ (Fehler
$f-T_Nf\perp V_N$): (i) Pythagoras $\|f-S_N\|^2=\|f-T_Nf\|^2+\|T_Nf-S_N\|^2$; (ii) $T_Nf$ minimiert $\|f-S_N\|_2$;
(iii) $\|f-T_Nf\|^2=\|f\|^2-\|T_Nf\|^2$; (iv) __Bessel__ $\sum_{|k|\le N}|c_k|^2\le\|f\|_2^2$ ⇒ $c_k$ Nullfolge
(__Riemann-Lebesgue__). __Satz 7.13__: trig. System vollständig ⇒ $T_Nf\to f$ im quadratischen Mittel + __Parseval__
$\frac{1}{2\pi}\int_0^{2\pi}|f|^2dx=\sum_{n\in\mathbb{Z}}|c_n|^2$ (reell $\frac1\pi\int|f|^2=\frac{a_0^2}{2}+\sum(a_k^2
+b_k^2)$), „Energieerhaltung". Anwendung (Sägezahn): $|c_k|^2=\frac1{4k^2}$, LHS $=\frac{\pi^2}{12}$ ⇒ $\sum\frac1{k^2}
=\frac{\pi^2}{6}$ (Basel), $C=\frac{\pi^2}{12}$. $L^2$-Konvergenz $\neq$ punktweise.
:::

Die $L^2$-Konvergenz gilt für **jede** integrierbare Funktion — sagt aber nichts über einzelne Punkte. Für die
__punktweise__ Konvergenz brauchen wir ein feineres Werkzeug, den __Dirichlet-Kern__, und als Vorbereitung die
__Dirac-Scharen__ und die $\delta$-Distribution — die Themen der nächsten Artikel.
