---
title: Stufe 1: Schwingungen als Bausteine
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3170200
summary: Diese Stufe legt die Schwingungen fest, aus denen alles gebaut wird, und misst, wie viel von einer Schwingung in einer Funktion steckt.
tags: periodisch, komplex trigonometrischen Basisfunktionen, Orthonormal, Kronecker-Symbol
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Diese Stufe legt die Schwingungen fest, aus denen alles gebaut wird, und misst, wie viel von einer Schwingung in einer Funktion steckt.
:::

**Die Idee.** Im $\mathbb{R}^3$ liest man den Anteil eines Vektors $\boldsymbol v$ in Richtung eines Einheitsvektors $\hat{\boldsymbol{e}}$ mit dem Skalarprodukt ab: $\boldsymbol v\cdot\hat{\boldsymbol{e}}$. Das klappt, weil die Achsen senkrecht aufeinander stehen: Ein Schritt längs der einen Achse ändert den Anteil längs der anderen nicht. Für Funktionen geht man genauso vor. Aus der Summe über die Komponenten wird ein Integral über die Stellen $x$. Zwei Schwingungen verschiedener Frequenz verhalten sich dann wie senkrechte Achsen: Ihr Produkt pendelt so um null, dass sich die Flächen aufheben (Abb. [1](#abb-1)).

:::abbildung hm3/k7ortho 1
Links: Das Produkt zweier Schwingungen verschiedener Frequenz hat die Fläche null, was über der Achse liegt, gleicht aus, was darunter liegt. Rechts: Das Produkt einer Schwingung mit sich selbst bleibt positiv, sein Mittelwert ist $\frac12$.
:::

**Periodische Funktionen.** Eine Funktion $f:\mathbb{R}\to\mathbb{C}$ heißt __periodisch__ mit Periode $T>0$, wenn $f(x+T)=f(x)$ für alle $x\in\mathbb{R}$ gilt. Jede Periode lässt sich auf $2\pi$ umrechnen: $\tilde f(x)=f\bigl(\frac{T}{2\pi}x\bigr)$ erfüllt $\tilde f(x+2\pi)=f\bigl(\frac{T}{2\pi}x+T\bigr)=\tilde f(x)$. Läuft $x$ von $0$ bis $2\pi$, durchläuft $\tilde f$ genau eine Periode von $f$, ob diese nun $20\,\mathrm{ms}$ oder $3\,\mathrm{s}$ dauert. Deshalb gilt ab jetzt immer $T=2\pi$.

:::definition Definition 1.1 (Bausteine und Skalarprodukt)
<span class="anker" id="satz-1-1"></span>

Die __komplex trigonometrischen Basisfunktionen__ sind $\hat{\boldsymbol{e}}_k(x):=\mathrm{e}^{\mathrm{i}kx}$ für $x\in\mathbb{R}$, $k\in\mathbb{Z}$. Für $2\pi$-periodische, über $[0,2\pi]$ Riemann-integrierbare Funktionen $f,g:\mathbb{R}\to\mathbb{C}$ setzt man

<span class="anker" id="gl-1-1"></span>
$$\langle f,g\rangle:=\frac1{2\pi}\int_0^{2\pi}f(x)\,\overline{g(x)}\,\mathrm{d} x,\qquad\|f\|_2^2:=\langle f,f\rangle=\frac1{2\pi}\int_0^{2\pi}|f(x)|^2\,\mathrm{d} x. \tag{1.1}$$
:::

⁠**So liest man das:** $\hat{\boldsymbol{e}}_k$ ist ein Zeiger, der je Periode $k$-mal um den Einheitskreis läuft, für $k<0$ rückwärts, für $k=0$ steht er still. Sein Realteil ist $\cos kx$, sein Imaginärteil $\sin kx$. Das ist das Skalarprodukt aus [Teil 6](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/konvergenz-von-funktionenfolgen.html) auf $[0,2\pi]$. Der Querstrich ist die Konjugation, er macht $\langle f,f\rangle$ reell und nichtnegativ. $\|f\|_2^2$ ist der Mittelwert von $|f|^2$, also die mittlere Leistung, und $\|f\|_2$ der Effektivwert.

:::satz Satz 1.2 (Orthonormalsystem)
<span class="anker" id="satz-1-2"></span>

Für alle $k,\ell\in\mathbb{Z}$ gilt $\langle\hat{\boldsymbol{e}}_k,\hat{\boldsymbol{e}}_\ell\rangle=\delta_{k\ell}$, wobei $\delta_{k\ell}=1$ für $k=\ell$ und $\delta_{k\ell}=0$ sonst.
:::

:::beweis Orthonormalsystem
Es ist $\hat{\boldsymbol{e}}_k\overline{\hat{\boldsymbol{e}}_\ell}=\mathrm{e}^{\mathrm{i}(k-\ell)x}$. Für $k=\ell$ ist das konstant 1, der Mittelwert also 1. Für $k\neq\ell$ gilt

$$\langle\hat{\boldsymbol{e}}_k,\hat{\boldsymbol{e}}_\ell\rangle=\frac1{2\pi}\Bigl[\frac{\mathrm{e}^{\mathrm{i}(k-\ell)x}}{\mathrm{i}(k-\ell)}\Bigr]_0^{2\pi}=0,$$

weil $\mathrm{e}^{\mathrm{i}(k-\ell)2\pi}=1$ ist.
:::

⁠**So liest man das:** __Orthonormal__ heißt: paarweise senkrecht und jeweils mit Norm 1. Die Zahl $\delta_{k\ell}$ heißt __Kronecker-Symbol__. Die Bausteine verhalten sich also wie die Einheitsvektoren eines Koordinatensystems.

**Beispiel.** Sei $f(x)=3+2\cos x-4\sin2x$. Mit $\cos x=\frac12(\hat{\boldsymbol{e}}_1+\hat{\boldsymbol{e}}_{-1})$ und $\sin2x=\frac1{2\mathrm{i}}(\hat{\boldsymbol{e}}_2-\hat{\boldsymbol{e}}_{-2})$ wird

$$f=3\,\hat{\boldsymbol{e}}_0+\hat{\boldsymbol{e}}_1+\hat{\boldsymbol{e}}_{-1}+2\mathrm{i}\,\hat{\boldsymbol{e}}_2-2\mathrm{i}\,\hat{\boldsymbol{e}}_{-2}.$$

Bildet man $\langle f,\hat{\boldsymbol{e}}_2\rangle$, fallen nach Satz [1.2](#satz-1-2) alle Terme bis auf einen weg, und es bleibt $\langle f,\hat{\boldsymbol{e}}_2\rangle=2\mathrm{i}$. Das Skalarprodukt liest den Anteil also direkt aus $f$ ab. **Grenzfall:** Ein Baustein, der nicht vorkommt, ergibt null: $\langle f,\hat{\boldsymbol{e}}_5\rangle=0$.

:::frage Warum komplex, wenn die Signale reell sind?
Weil sich beim Multiplizieren von $\mathrm{e}^{\mathrm{i}kx}$ die Exponenten addieren und beim Ableiten nur ein Faktor entsteht. Mit Sinus und Cosinus bräuchte man jedes Mal Additionstheoreme. Eine reelle Schwingung ist dann die Summe zweier gegenläufiger Zeiger, wie in $\cos x=\frac12(\hat{\boldsymbol{e}}_1+\hat{\boldsymbol{e}}_{-1})$.
:::

:::aufgabe Aufgabe 1 ★ Bausteine ablesen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Das Signal $h(t)=2\sin(100\pi t)$ hat die Periode $T=0{,}02$. Bestimme $\tilde h(x)=h\bigl(\frac{T}{2\pi}x\bigr)$.

</li>

<li>

Schreibe $f(x)=5-2\sin x+6\cos3x$ mit den $\hat{\boldsymbol{e}}_k$ und lies $\langle f,\hat{\boldsymbol{e}}_{-3}\rangle$, $\langle f,\hat{\boldsymbol{e}}_1\rangle$ und $\langle f,\hat{\boldsymbol{e}}_2\rangle$ ab.

</li>

</ol>

:::loesung
(a) $\tilde h(x)=2\sin\bigl(100\pi\cdot\frac{0{,}02}{2\pi}x\bigr)=2\sin x$. (b) $-2\sin x=\mathrm{i}\,\hat{\boldsymbol{e}}_1-\mathrm{i}\,\hat{\boldsymbol{e}}_{-1}$ und $6\cos3x=3\,\hat{\boldsymbol{e}}_3+3\,\hat{\boldsymbol{e}}_{-3}$, also $f=5\,\hat{\boldsymbol{e}}_0+\mathrm{i}\,\hat{\boldsymbol{e}}_1-\mathrm{i}\,\hat{\boldsymbol{e}}_{-1}+3\,\hat{\boldsymbol{e}}_3+3\,\hat{\boldsymbol{e}}_{-3}$. Damit ist $\langle f,\hat{\boldsymbol{e}}_{-3}\rangle=3$, $\langle f,\hat{\boldsymbol{e}}_1\rangle=\mathrm{i}$ und $\langle f,\hat{\boldsymbol{e}}_2\rangle=0$.
:::
:::
