---
title: Komplexe und reelle Fourierpolynome
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3070100
summary: Von Grund auf – jede $2\pi$-periodische Funktion wird in reine Schwingungen $e^{ikx}$ zerlegt. Diese bilden ein Orthonormalsystem, daher ist der Fourier-Koeffizient $c_k=\langle f,\hat e_k\rangle=\frac{1}{2\pi}\int_0^{2\pi}f(x)e^{-ikx}dx$ einfach die Projektion von $f$ auf die $k$-te Schwingung. Über die Eulersche Formel entsteht die reelle Form mit $a_k\cos(kx)+b_k\sin(kx)$, plus Rechenregeln (gerade/ungerade, Verschiebung, Ableitung).
tags: Fourier-Reihe, Fourier-Koeffizient, Fourierpolynom, Orthonormalsystem, trigonometrische Basis, Eulersche Formel, periodische Funktion, Projektion
---

:::grafik
Einstiegs-Animation: Eine $2\pi$-periodische Funktion $f$ (eine wellige Kurve) wird aus **reinen Schwingungen**
$e^{ikx}$ (bzw. $\cos kx$, $\sin kx$) zusammengesetzt — wie ein Klang aus Obertönen. Jede Schwingung $\hat e_k$ ist ein
„Basisvektor"; der __Fourier-Koeffizient__ $c_k=\langle f,\hat e_k\rangle$ misst, **wie viel** von dieser Schwingung in
$f$ steckt (die Projektion). Das Fourierpolynom $T_N f$ addiert die ersten $2N+1$ Schwingungen auf und nähert $f$
immer besser an. Kernbotschaft: Fourier zerlegt eine periodische Funktion in ein Orthonormalsystem von Schwingungen —
Koeffizient = Projektion.
:::

:::konzept
Im Artikel
[Normierter Vektorraum und Konvergenz im quadratischen Mittel](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/normierter-vektorraum-und-quadratisches-mittel.html)
haben wir die Funktionen mit einem __Skalarprodukt__ $\langle f,g\rangle$ ausgestattet — damit tragen sie eine
**Geometrie** mit Längen, Winkeln und Orthogonalität. Die __Fourier-Theorie__ nutzt das aus: Die
Schwingungen $\hat e_k(x)=e^{ikx}$ bilden ein __Orthonormalsystem__ — paarweise senkrecht, jede auf Länge $1$. Eine
periodische Funktion in Fourier zu entwickeln heißt dann genau dasselbe wie einen Vektor in einer Orthonormalbasis zu
zerlegen: Der Koeffizient ist die __Projektion__ $\langle f,\hat e_k\rangle$. Das ist die mathematische Grundlage von
Signalverarbeitung, Spektralanalyse und dem Lösen von Schwingungs- und Wärmeleitungsgleichungen.
:::

**Worum es geht:** Wir definieren die __trigonometrische Basis__ $\hat e_k=e^{ikx}$ (ein Orthonormalsystem), die
__Fourier-Koeffizienten__ $c_k$ und das __Fourierpolynom__, übersetzen in die __reelle Form__ $a_k,b_k$ und sammeln
die wichtigsten __Rechenregeln__.

## Periodizität und die trigonometrische Basis

Eine Funktion $f:\mathbb{R}\to\mathbb{C}$ heißt __periodisch__ mit Periode $T>0$, wenn $f(x+T)=f(x)$ für alle $x$.
Durch Skalierung $\tilde f(x)=f\big(\tfrac{T}{2\pi}x\big)$ kann man stets $T=2\pi$ erreichen — das ist die Periode von
$\sin$, $\cos$ und der __komplex-trigonometrischen Basisfunktionen__

$$\hat e_k(x):=e^{ikx}, \qquad x\in\mathbb{R},\ k\in\mathbb{Z}.$$

**Lemma.** Die $\{\hat e_k\}_{k\in\mathbb{Z}}$ bilden ein __Orthonormalsystem__ bezüglich des Skalarprodukts

$$\langle f,g\rangle=\frac{1}{2\pi}\int_0^{2\pi}f(x)\,\overline{g(x)}\,dx, \qquad\text{d.h.}\qquad \langle\hat e_k,\hat e_\ell\rangle=\delta_{k\ell}\ \ \text{für alle } k,\ell\in\mathbb{Z}.$$

*Nachrechnen:* $\langle\hat e_k,\hat e_\ell\rangle=\frac{1}{2\pi}\int_0^{2\pi}e^{i(k-\ell)x}\,dx$ ist $1$ für $k=\ell$
und $0$ sonst (das Integral einer vollen Schwingung verschwindet). Das ist das Herzstück: ein **orthonormales**
Schwingungssystem.

## Fourier-Koeffizienten und Fourierpolynom

Sei $f:\mathbb{R}\to\mathbb{C}$ $2\pi$-periodisch und über $[0,2\pi]$ $R$-integrierbar. Die __Fourier-Koeffizienten__
sind die Projektionen auf die Basis,

$$c_k=\langle f,\hat e_k\rangle=\frac{1}{2\pi}\int_0^{2\pi}f(x)\,e^{-ikx}\,dx, \qquad k\in\mathbb{Z},$$

und das __$N$-te Fourierpolynom__ ist die abgeschnittene Entwicklung

$$T_N f=\sum_{|k|\le N}c_k\,\hat e_k=\sum_{|k|\le N}\langle f,\hat e_k\rangle\,\hat e_k.$$

Wegen der Periodizität darf man über **jede** volle Periode integrieren: $c_k=\frac{1}{2\pi}
\int_\alpha^{2\pi+\alpha}f(x)e^{-ikx}\,dx$ für beliebiges $\alpha$; eine häufige Konvention ist $\alpha=-\pi$ (Integration
über $[-\pi,\pi]$). Die __formale Fourierreihe__ ist der Grenzfall $N\to\infty$,

$$Tf=\sum_{k\in\mathbb{Z}}c_k\,\hat e_k=\sum_{k\in\mathbb{Z}}\langle f,\hat e_k\rangle\,\hat e_k.$$

(„Formal", weil über die Konvergenz noch nichts gesagt ist — das klären die folgenden Artikel.)

## Die reelle Form: $\cos$ und $\sin$

Mit der __Eulerschen Formel__ $e^{-ikx}=\cos(kx)-i\sin(kx)$ geht die komplexe in die reelle Darstellung über. Man setzt

$$a_k=\frac{1}{\pi}\int_0^{2\pi}f(x)\cos(kx)\,dx, \qquad b_k=\frac{1}{\pi}\int_0^{2\pi}f(x)\sin(kx)\,dx.$$

Dann ist $a_{-k}=a_k$, $b_{-k}=-b_k$ (insbesondere $b_0=0$), und die Koeffizienten hängen über

$$c_k=\tfrac12(a_k-ib_k), \qquad c_{-k}=\tfrac12(a_k+ib_k)\qquad(k\in\mathbb{N}_0)$$

zusammen. Damit schreibt sich das Fourierpolynom reell als

$$T_N f(x)=\frac{a_0}{2}+\sum_{k=1}^{N}\big(a_k\cos(kx)+b_k\sin(kx)\big).$$

Dass hier mit $\frac1\pi$ (statt $\frac{1}{2\pi}$) normiert wird, liegt daran, dass auch $\{\cos(kx),
\sin(kx)\}$ ein Orthonormalsystem bezüglich des reellen Skalarprodukts bilden: $\frac1\pi\int_0^{2\pi}\cos(kx)\cos(\ell
x)\,dx=\frac1\pi\int_0^{2\pi}\sin(kx)\sin(\ell x)\,dx=\delta_{k\ell}$ und $\frac1\pi\int_0^{2\pi}\sin(kx)\cos(\ell x)\,
dx=0$. Der Term $\frac{a_0}{2}$ ist der **Mittelwert** von $f$ über eine Periode.

:::grafik
Links die ersten Basisfunktionen $\cos(kx),\sin(kx)$ ($k=0,1,2,\dots$) als übereinandergelegte Schwingungen, mit dem
Hinweis auf ihre Orthonormalität ($\frac1\pi\int\cos\cos=\delta_{k\ell}$). Rechts eine Zielfunktion $f$ und ihre
Fourierpolynome $T_1,T_3,T_5$, die sich schrittweise anschmiegen; $\frac{a_0}{2}$ als Mittelwertlinie markiert.
:::

## Rechenregeln

Die Koeffizientenzuordnung ist **linear** ($f+\lambda g$ hat $c_k+\lambda d_k$). Weiter gilt für $2\pi$-periodisches,
$R$-integrierbares $f$ mit $c_k=\tfrac12(a_k-ib_k)$:

- **(i) Reellwertig:** Ist $f$ reell, so sind $a_k,b_k$ reell und $c_{-k}=\overline{c_k}$.
- **(ii) Gerade:** Ist $f$ gerade ($f(x)=f(-x)$), so ist $b_k=0$ für alle $k$ — es bleibt eine reine **Kosinusreihe**.
- **(iii) Ungerade:** Ist $f$ ungerade ($f(x)=-f(-x)$), so ist $a_k=0$ für alle $k$ — eine reine **Sinusreihe**.
- **(iv) Verschiebung:** $\tilde f(x)=f(x+\tau)$ hat die Koeffizienten $\tilde c_k=e^{i\tau k}c_k$.
- **(v) Ableitung:** Ist $f$ stetig differenzierbar, so hat $f'$ die Koeffizienten $ik\,c_k$ (Differenzieren $=$ Mal
  $ik$ im Spektrum).

**Beispiel.** Für $f(x)=\cos^2 x$ nutzt man $\cos^2 x=\tfrac12+\tfrac12\cos(2x)$ und **liest die Koeffizienten
direkt ab**: $\frac{a_0}{2}=\tfrac12$ (also $a_0=1$), $a_2=\tfrac12$, alle übrigen $a_k,b_k=0$; komplex $c_0=\tfrac12$,
$c_2=c_{-2}=\tfrac14$. Da $f$ gerade ist, verschwinden erwartungsgemäß alle $b_k$ (Regel ii). Kein Integral nötig — die
Orthonormalität garantiert die Eindeutigkeit der Zerlegung.

**Stolperstein:** (1) Normierung: komplex $\frac{1}{2\pi}$, reell $\frac1\pi$ (und der Sonderfaktor $\frac{a_0}{2}$) —
das ist kein Widerspruch, sondern folgt aus der jeweiligen Orthonormalität. (2) $c_k$ läuft über **alle** $k\in
\mathbb{Z}$ (auch negative), $a_k,b_k$ nur über $k\ge0$. (3) „Formale" Reihe heißt: Gleichheit $f=Tf$ ist noch
**nicht** behauptet — in welchem Sinn sie gilt, ist Thema der nächsten Artikel.

:::kern
__Trigonometrische Basis__ $\hat e_k(x)=e^{ikx}$, $k\in\mathbb{Z}$, ist ein __Orthonormalsystem__ bzgl. $\langle f,g
\rangle=\frac{1}{2\pi}\int_0^{2\pi}f\bar g\,dx$ ($\langle\hat e_k,\hat e_\ell\rangle=\delta_{k\ell}$).
__Fourier-Koeffizient__ (Projektion) $c_k=\langle f,\hat e_k\rangle=\frac{1}{2\pi}\int_0^{2\pi}f(x)e^{-ikx}\,dx$;
__Fourierpolynom__ $T_N f=\sum_{|k|\le N}c_k\hat e_k$, formale Reihe $Tf=\sum_{k\in\mathbb{Z}}c_k\hat e_k$ (Integration
über jede Periode möglich). __Reelle Form__: $a_k=\frac1\pi\int_0^{2\pi}f\cos(kx)$, $b_k=\frac1\pi\int_0^
{2\pi}f\sin(kx)$; $c_k=\tfrac12(a_k-ib_k)$, $c_{-k}=\tfrac12(a_k+ib_k)$; $T_N f=\frac{a_0}{2}+\sum_{k=1}^N(a_k\cos kx+
b_k\sin kx)$ (auch $\{\cos,\sin\}$ ONS mit $\frac1\pi$). __Regeln__: linear; $f$ reell $\Rightarrow c_{-k}
=\overline{c_k}$; $f$ gerade $\Rightarrow b_k=0$ (Kosinusreihe); $f$ ungerade $\Rightarrow a_k=0$ (Sinusreihe);
Verschiebung $f(x+\tau)\to e^{i\tau k}c_k$; Ableitung $f'\to ik\,c_k$.
:::

Als Nächstes rechnen wir zwei klassische Fourier-Reihen **zu Fuß** aus — den Sägezahn und eine weitere Standardfunktion
— und sehen dabei, wie die Koeffizienten konkret entstehen und was am Sprung passiert. Das ist das Thema des nächsten
Artikels.

:::quiz
F: Warum darf man sich bei der Fourier-Theorie ohne Einschränkung auf die Periode $2\pi$ beschränken?
A: Jede $T$-periodische Funktion lässt sich durch die Skalierung $\tilde f(x)=f(\tfrac{T}{2\pi}x)$ auf Periode $2\pi$ umrechnen. Die $2\pi$-Periode ist zudem die natürliche von $\sin$, $\cos$ und $e^{ikx}$, sodass die Formeln am einfachsten werden.
F: Was bedeutet es, dass die Schwingungen $\hat e_k=e^{ikx}$ ein Orthonormalsystem bilden, und warum ist das zentral?
A: Bezüglich $\langle f,g\rangle=\frac{1}{2\pi}\int_0^{2\pi}f\bar g$ gilt $\langle\hat e_k,\hat e_\ell\rangle=\delta_{k\ell}$ — verschiedene Schwingungen sind „senkrecht", jede hat Länge $1$. Das macht die Fourier-Entwicklung zur Zerlegung eines Vektors in einer Orthonormalbasis, bei der jeder Koeffizient unabhängig bestimmbar ist.
F: Warum ist der Fourier-Koeffizient $c_k=\langle f,\hat e_k\rangle$ eine „Projektion"?
A: Wie in der linearen Algebra die Komponente eines Vektors längs eines Basisvektors das Skalarprodukt mit ihm ist, misst $c_k=\langle f,\hat e_k\rangle$ den Anteil der Schwingung $\hat e_k$ in $f$. Dank Orthonormalität stören sich die Projektionen gegenseitig nicht.
F: Warum verschwindet im Nachweis der Orthonormalität $\frac{1}{2\pi}\int_0^{2\pi}e^{i(k-\ell)x}dx$ für $k\ne\ell$?
A: Für $k\ne\ell$ ist $e^{i(k-\ell)x}$ eine ganze Anzahl voller Schwingungen über $[0,2\pi]$; über eine volle Periode mitteln sich Real- und Imaginärteil zu null. Nur für $k=\ell$ ist der Integrand konstant $1$ und das Integral gibt $1$.
F: Warum darf man die Fourier-Koeffizienten über jede beliebige volle Periode integrieren?
A: Der Integrand $f(x)e^{-ikx}$ ist selbst $2\pi$-periodisch (Produkt zweier $2\pi$-periodischer Faktoren). Das Integral über ein Intervall der Länge $2\pi$ hängt daher nicht von der Lage des Intervalls ab — oft wählt man $[-\pi,\pi]$.
F: Wieso wird die reelle Form mit $\frac{1}{\pi}$ normiert, die komplexe aber mit $\frac{1}{2\pi}$?
A: Auch $\{\cos(kx),\sin(kx)\}$ bilden ein Orthonormalsystem, aber bezüglich $\frac{1}{\pi}\int_0^{2\pi}$ statt $\frac{1}{2\pi}\int_0^{2\pi}$. Der Faktor $\frac1\pi$ ist gerade der, der $\cos$ und $\sin$ auf Norm $1$ bringt — kein Widerspruch, sondern verschiedene Normierung verschiedener Basen.
F: Was bedeutet der Term $\frac{a_0}{2}$ in der reellen Fourierreihe anschaulich?
A: Er ist der Mittelwert von $f$ über eine Periode (der Anteil der „nullten Schwingung", einer Konstanten). Alle $\cos$- und $\sin$-Terme haben Mittelwert null, also trägt nur $\frac{a_0}{2}$ zum Gleichanteil bei.
F: Warum ist eine gerade Funktion eine reine Kosinusreihe, eine ungerade eine reine Sinusreihe?
A: $\cos$ ist gerade, $\sin$ ungerade. Eine gerade Funktion hat keinen ungeraden Anteil, also $b_k=0$ (nur Kosinus); eine ungerade keinen geraden Anteil, also $a_k=0$ (nur Sinus). Die Integrale der jeweils „falschen" Symmetrie verschwinden.
F: Was bedeutet die Ableitungsregel $f'\to ik\,c_k$ für das Spektrum?
A: Differenzieren im Ortsraum entspricht Multiplikation mit $ik$ im Spektrum. Hohe Frequenzen werden dadurch verstärkt — das erklärt, warum Ableiten die Konvergenz der Fourier-Reihe verschlechtert und glatte Funktionen schnell abfallende Koeffizienten haben.
F: Warum kann man die Fourier-Koeffizienten von $\cos^2 x$ ohne jedes Integral ablesen?
A: Mit $\cos^2 x=\tfrac12+\tfrac12\cos(2x)$ steht die Funktion bereits als Linearkombination von Basisschwingungen da. Da die Zerlegung in das Orthonormalsystem eindeutig ist, sind das genau die Fourier-Koeffizienten ($a_0=1$, $a_2=\tfrac12$, sonst null).
:::
