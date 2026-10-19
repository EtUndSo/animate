---
title: Normierter Vektorraum und Konvergenz im quadratischen Mittel
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3060400
summary: Von Grund auf – Funktionen werden zu Vektoren, und Konvergenz wird zum Abstand in einer Norm. Die Supremumsnorm $\|f\|_{\sup}=\sup_x|f(x)|$ macht $C^0([a,b])$ zu einem vollständigen Raum (Banachraum); gleichmäßige Konvergenz ist genau Konvergenz darin. Für Fourier-Reihen passt besser die $L^2$-Norm $\|f\|_2^2=\frac{1}{b-a}\int_a^b|f|^2$ aus einem Skalarprodukt – die Konvergenz im quadratischen Mittel, der Hilbertraum $L^2$.
tags: Supremumsnorm, normierter Vektorraum, Banachraum, Skalarprodukt, L2-Norm, Konvergenz im quadratischen Mittel, Cauchy-Schwarz, Hilbertraum
---

:::grafik
Einstiegs-Animation: Zwei „Messlatten" für den Abstand zweier Funktionen $f,g$. Links die __Supremumsnorm__
$\|f-g\|_{\sup}$ — der **größte** senkrechte Abstand irgendwo (ein einzelner Ausreißer dominiert). Rechts die
__$L^2$-Norm__ $\|f-g\|_2$ — die **Wurzel aus der mittleren quadratischen** Abweichung, also die „Fläche unter
$(f-g)^2$" (ein schmaler Ausreißer zählt kaum). Ein hoher, hauchdünner Zacken macht den Unterschied sichtbar:
$\|\cdot\|_{\sup}$ ist riesig, $\|\cdot\|_2$ winzig. Kernbotschaft: Funktionen sind Vektoren, und es gibt
**verschiedene Normen** — Supremum (gleichmäßig) und quadratisches Mittel ($L^2$).
:::

:::konzept
Bisher war Konvergenz eine Eigenschaft „von Hand". Jetzt heben wir sie auf die richtige Abstraktionsebene:
**Funktionen bilden einen Vektorraum**, und eine __Norm__ darauf misst „Länge" und „Abstand". Dann ist Konvergenz
einfach $\|f_n-f\|\to0$ — wie bei Zahlenfolgen, nur mit Funktionen. Zwei Normen sind zentral: Die __Supremumsnorm__
fasst die **gleichmäßige** Konvergenz (ideal für Potenzreihen). Für Fourier-Reihen und allgemeinere (auch
unstetige) Funktionen ist sie aber zu streng — dort passt die __$L^2$-Norm__ aus einem **Skalarprodukt**, die der
Funktionenwelt eine Geometrie mit Winkeln, Orthogonalität und Pythagoras gibt. Das ist die Bühne, auf der die
Fourier-Theorie im nächsten Kapitel spielt.
:::

**Worum es geht:** Wir machen die stetigen Funktionen mit der __Supremumsnorm__ zu einem vollständigen Raum
(Banachraum) und führen das __Skalarprodukt__, die __$L^2$-Norm__ und die __Konvergenz im quadratischen Mittel__ ein.

## Die Supremumsnorm und der Raum $C^0$

Für beschränkte Funktionen $f:[a,b]\to\mathbb{C}$ definiert man die __Supremumsnorm__

$$\|f\|_{\sup}:=\sup_{x\in[a,b]}|f(x)|.$$

Sie erfüllt die Normaxiome: $\|f\|_{\sup}\ge0$ mit $\|f\|_{\sup}=0\Leftrightarrow f\equiv0$; $\|\lambda f\|_{\sup}=
|\lambda|\,\|f\|_{\sup}$ für Skalare $\lambda\in\mathbb{C}$; und die Dreiecksungleichung $\|f+g\|_{\sup}\le\|f\|_{\sup}
+\|g\|_{\sup}$. Damit bilden die stetigen Funktionen einen **normierten Vektorraum**, und die gleichmäßige Konvergenz
schreibt sich kompakt als Cauchy-Bedingung

$$\|f_m-f_n\|_{\sup}\to0\quad\text{für } m,n\to\infty.$$

Da jede gleichmäßig konvergente Folge stetiger Funktionen einen stetigen Limes **im Raum** besitzt (Satz 6.4), ist der
Raum **vollständig**:

**Satz 6.11.** Die stetigen Funktionen $C^0([a,b];\mathbb{C})=\{f:[a,b]\to\mathbb{C}\ \text{stetig}\}$ bilden mit der
Supremumsnorm einen **vollständigen** normierten Vektorraum (einen __Banachraum__); man schreibt $\|f\|_{C^0}\equiv
\|f\|_{\sup}$. Ebenso sind die Räume $C^k([a,b])$ der $k$-mal stetig differenzierbaren Funktionen mit der Norm
$\|f\|_{C^k}:=\sup_{x\in[a,b]}\sum_{i=0}^k|f^{(i)}(x)|$ vollständig.

„Vollständig" heißt: Jede Cauchy-Folge hat einen Grenzwert **im Raum selbst** — man fällt beim Grenzübergang nicht
aus den stetigen Funktionen heraus. Das ist die funktionale Entsprechung der Vollständigkeit von $\mathbb{R}$.

## Konvergenz im quadratischen Mittel

Für die Approximation durch **orthogonale Funktionensysteme** (Fourier-, Legendre-Polynome) ist die gleichmäßige
Konvergenz zu streng — schon stückweise stetige Funktionen mit Sprüngen lassen sich nicht gleichmäßig durch stetige
Summen approximieren. Der passende Begriff ist die __Konvergenz im quadratischen Mittel__ (Definition 6.12): Für
$R$-integrierbare $f_n,f:[a,b]\to\mathbb{C}$ gilt $f_n\to f$ im quadratischen Mittel, wenn

$$\lim_{n\to\infty}\int_a^b|f_n(x)-f(x)|^2\,dx=0.$$

Der Raum $\mathcal{R}([a,b];\mathbb{C})$ der $R$-integrierbaren Funktionen enthält insbesondere alle stetigen und
stückweise stetigen Funktionen (und mit $f$ auch $|f|^2$). Der Zusammenhang zur gleichmäßigen Konvergenz
(Bemerkung 6.13): **Gleichmäßige Konvergenz impliziert Konvergenz im quadratischen Mittel** (auf dem endlichen
Intervall) — aber **nicht umgekehrt**.

## Das Skalarprodukt und die $L^2$-Norm

Die quadratische-Mittel-Geometrie kommt von einem **Skalarprodukt**. Für $f,g\in\mathcal{R}([a,b];\mathbb{C})$ setzt
man das (hermitesche) Skalarprodukt und die zugehörige Norm

$$\langle f,g\rangle:=\frac{1}{b-a}\int_a^b f(x)\,\overline{g(x)}\,dx, \qquad \|f\|_2^2:=\langle f,f\rangle=\frac{1}{b-a}\int_a^b|f(x)|^2\,dx.$$

Die Normierung mit der Intervalllänge $\frac{1}{b-a}$ ist für Konvergenzfragen unerheblich (auf unbeschränkten
Gebieten lässt man sie weg). Es gelten (Lemma 6.15) die **Dreiecksungleichung** $\|f+g\|_2\le\|f\|_2+\|g\|_2$ und die
__Cauchy–Schwarz-Ungleichung__

$$|\langle f,g\rangle|\le\|f\|_2\,\|g\|_2.$$

Für stückweise stetige $f_n,f$ ist Konvergenz im quadratischen Mittel genau $\|f_n-f\|_2\to0$; man nennt sie daher
auch __$L^2$-Konvergenz__. Sie lässt sich mit der **Integration vertauschen** (Lemma 6.16): $f_n\to f$ im
quadratischen Mittel $\Rightarrow\lim_n\int_a^b f_n\,dx=\int_a^b f\,dx$, denn mit Cauchy–Schwarz ist

$$\left|\int_a^b f_n\,dx-\int_a^b f\,dx\right|\le\int_a^b|f_n-f|\,dx\le(b-a)^{1/2}\Big(\int_a^b|f_n-f|^2\,dx\Big)^{1/2}\to0.$$

:::grafik
Links die Normaxiome als „Länge"-Eigenschaften (Skalierung, Dreiecksungleichung) im Funktionenraum. Rechts das
Skalarprodukt $\langle f,g\rangle=\frac{1}{b-a}\int f\bar g$ mit Cauchy–Schwarz $|\langle f,g\rangle|\le\|f\|_2\|g\|_2$
als „Winkel"-Ungleichung; angedeutet die Orthogonalität $\langle e^{ikx},e^{ilx}\rangle=\delta_{kl}$ des
Fourier-Systems.
:::

## Warum $L^2$ schwächer ist — und der Hilbertraum

**Eigenes Beispiel (Zacken).** Betrachte auf $[0,1]$ die Spitzen $f_n(x)=n$ für $x\in[0,\tfrac1{n^3}]$ und $0$ sonst.
Dann ist $\|f_n\|_{\sup}=n\to\infty$ (keine gleichmäßige Konvergenz, nicht einmal beschränkt), aber

$$\|f_n\|_2^2=\int_0^1|f_n|^2\,dx=n^2\cdot\frac{1}{n^3}=\frac1n\to0.$$

Im quadratischen Mittel konvergiert $f_n\to0$, gleichmäßig überhaupt nicht — die $L^2$-Norm „sieht" den schmalen
hohen Zacken fast nicht. Genau diese Toleranz gegenüber Ausreißern macht $L^2$ für sprungbehaftete Funktionen
geeignet.

**Vorsicht (Bemerkung 6.14).** $\|\cdot\|_2$ ist auf $\mathcal{R}([a,b];\mathbb{C})$ **streng genommen keine Norm**:
$\|f\|_2=0$ erzwingt nicht $f\equiv0$ — jede Funktion, die nur an endlich vielen Punkten $\neq0$ ist, hat $\|f\|_2=0$.
Es ist also nur eine **Halbnorm**. Vervollständigt man den Raum bezüglich $\|\cdot\|_2$ und identifiziert Funktionen,
die sich nur auf einer **Nullmenge** (fast überall gleich) unterscheiden, erhält man den Raum der quadratisch
**Lebesgue**-integrierbaren Funktionen — den vollständigen __Hilbertraum__ $L^2((a,b);\mathbb{C})$. „Hilbert" (nicht
nur Banach), weil die Norm aus einem **Skalarprodukt** stammt — das gibt Orthogonalität und Projektionen, die
Grundlage der Fourier-Zerlegung.

**Stolperstein:** (1) Zwei verschiedene Normen = zwei verschiedene Konvergenzbegriffe: gleichmäßig ($\|\cdot\|_{\sup}$)
ist **stärker** als $L^2$ (auf endlichem Intervall), nicht umgekehrt. (2) $\|\cdot\|_2$ ist auf $R$-integrierbaren
Funktionen nur eine **Halbnorm**; erst das Identifizieren fast-überall-gleicher Funktionen macht $L^2$ zu einem echten
normierten (sogar vollständigen) Raum. (3) Der Normierungsfaktor $\frac{1}{b-a}$ ist Konvention und ändert an der
Konvergenz nichts.

:::kern
Funktionen = Vektoren, Konvergenz = $\|f_n-f\|\to0$. __Supremumsnorm__ $\|f\|_{\sup}=\sup_x|f(x)|$ (Normaxiome);
gleichmäßige Konvergenz $\Leftrightarrow\|f_m-f_n\|_{\sup}\to0$. **Satz 6.11:** $C^0([a,b];\mathbb{C})$ mit
$\|\cdot\|_{\sup}$ ist **vollständig** (__Banachraum__), ebenso $C^k$ mit $\|f\|_{C^k}=\sup_x\sum_{i=0}^k|f^{(i)}(x)|$.
__Konvergenz im quadratischen Mittel__ (Def 6.12): $\int_a^b|f_n-f|^2\,dx\to0$; aus __Skalarprodukt__ $\langle f,g
\rangle=\frac{1}{b-a}\int_a^b f\bar g\,dx$ und $\|f\|_2^2=\langle f,f\rangle=\frac{1}{b-a}\int_a^b|f|^2\,dx$. Lemma
6.15: Dreieck + __Cauchy–Schwarz__ $|\langle f,g\rangle|\le\|f\|_2\|g\|_2$; $L^2$-Konvergenz $=\|f_n-f\|_2\to0$. Lemma
6.16: $L^2$-Konvergenz $\Rightarrow\lim\int f_n=\int f$. **Gleichmäßig ⇒ $L^2$**, nicht umgekehrt (Zacken $f_n=n$ auf
$[0,n^{-3}]$: $\|f_n\|_{\sup}=n$, $\|f_n\|_2^2=1/n\to0$). $\|\cdot\|_2$ nur **Halbnorm** (Bem 6.14); Vervollständigung
= __Hilbertraum__ $L^2$ (fast-überall-Identifikation, Lebesgue).
:::

Damit ist Kapitel 6 abgeschlossen: Wir haben punktweise, gleichmäßige und $L^2$-Konvergenz, die zugehörigen Räume und
ihre Vertauschungsregeln. Auf dieser Bühne entfaltet sich nun die __Fourier-Theorie__ — die Zerlegung periodischer
Funktionen in das orthogonale System $e^{ikx}$, das Thema des nächsten Kapitels.
