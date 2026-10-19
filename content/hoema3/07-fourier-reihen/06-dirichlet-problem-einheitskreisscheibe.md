---
title: Das Dirichlet-Problem auf der Einheitskreisscheibe
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3070600
summary: Von Grund auf – Fourier-Reihen lösen eine partielle Differentialgleichung. Gesucht ist eine harmonische Funktion auf der Kreisscheibe mit vorgegebenem Rand ($\Delta u=0$, $u|_{\partial D}=g$). Der Separationsansatz liefert $u(r,\theta)=\sum_k c_k r^{|k|}e^{ik\theta}$ mit den Fourier-Koeffizienten von $g$. Zusammengefasst ist das die Faltung mit dem Poisson-Kern $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ – einer nichtnegativen Dirac-Schar, die die Randwerte annimmt.
tags: Dirichlet-Problem, harmonische Funktion, Laplace-Gleichung, Poisson-Kern, Separationsansatz, Poisson-Integralformel, Maximumprinzip, Mittelwerteigenschaft
---

:::grafik
Einstiegs-Animation: Eine Kreisscheibe $D$, an deren Rand eine Temperatur $g$ vorgegeben ist (eingefärbter Rand). Im
Inneren stellt sich die __harmonische__ Gleichgewichtsverteilung $u$ ein ($\Delta u=0$) — eine glatte Einfärbung ohne
Quellen. Rechts die Konstruktion: Man zerlegt den Rand in Fourier-Moden $e^{ik\theta}$; jede Mode setzt sich mit dem
Dämpfungsfaktor $r^{|k|}$ nach innen fort (hohe Frequenzen klingen schneller ab). Zusammengefasst ist $u$ die Faltung
des Randes mit dem __Poisson-Kern__ $P_r$ — einem **nichtnegativen** Buckel, der für $r\to1$ die Randwerte sauber
„einsammelt". Kernbotschaft: Fourier löst die Laplace-Gleichung auf der Scheibe.
:::

:::konzept
Zum Abschluss zeigt sich die eigentliche Kraft der Fourier-Theorie: Sie **löst eine partielle Differentialgleichung**.
Das __Dirichlet-Problem__ fragt nach einer harmonischen Funktion (Gleichgewicht, z. B. stationäre Temperatur oder ein
elektrostatisches Potential) auf einer Scheibe, deren Randwerte vorgegeben sind. Die Idee ist __Separation__: Jede
Fourier-Mode des Randes lässt sich eindeutig und gedämpft ins Innere fortsetzen. Die Summe ist die Lösung — und sie
bündelt sich zur eleganten __Poisson-Integralformel__. Der auftretende __Poisson-Kern__ ist, anders als der
Dirichlet-Kern, eine **echte** (nichtnegative) Dirac-Schar — deshalb werden die Randwerte sogar für bloß stetige $g$
angenommen.
:::

**Worum es geht:** Wir lösen das __Dirichlet-Problem__ auf der Kreisscheibe per __Fourier-Separation__, bündeln die
Lösung mit dem __Poisson-Kern__ zur Integralformel und begründen Existenz und Eindeutigkeit (__Maximumprinzip__).

## Das Problem und der Separationsansatz

Auf der Einheitskreisscheibe $D=\{(x,y):x^2+y^2<1\}$ und zu stetigen Randwerten $g:\partial D\to\mathbb{R}$ sucht man
die Lösung des __Dirichlet-Problems__

$$\begin{cases}\Delta u=0 & \text{in } D,\\ u=g & \text{auf } \partial D.\end{cases}$$

Man entwickelt die stetige $2\pi$-periodische Randfunktion $\theta\mapsto g(e^{i\theta})$ in eine Fourier-Reihe
$g(e^{i\theta})=\sum_{k\in\mathbb{Z}}c_k e^{ik\theta}$ und sucht $u$ in Polarkoordinaten, $u(re^{i\theta})=v(r,\theta)$.
Die Laplace-Gleichung lautet dort

$$\frac{\partial^2 v}{\partial r^2}+\frac1r\frac{\partial v}{\partial r}+\frac{1}{r^2}\frac{\partial^2 v}{\partial\theta^2}=0, \qquad v(1,\theta)=g(e^{i\theta}).$$

Der __Separationsansatz__ $v_k(r,\theta)=A_k(r)\,e^{ik\theta}$ führt auf die gewöhnliche (Euler-)Differentialgleichung

$$r^2A_k''(r)+rA_k'(r)-k^2A_k(r)=0, \qquad A_k(1)=c_k.$$

Ein Potenzansatz liefert die **bei $r=0$ beschränkte** Lösung $A_k(r)=c_k\,r^{|k|}$ (die zweite Lösung $r^{-|k|}$ bzw.
$\ln r$ für $k=0$ ist nahe $r=0$ unbeschränkt und wird verworfen). Also $v_k(r,\theta)=c_k\,r^{|k|}e^{ik\theta}$ — **jede
Mode klingt mit dem Faktor $r^{|k|}$ nach innen ab**, hohe Frequenzen schneller.

## Der Poisson-Kern und die Integralformel

Da Summen harmonischer Funktionen harmonisch sind, ist die Lösungskandidatin $v(r,\theta)=\sum_{k\in\mathbb{Z}}v_k(r,
\theta)$. Setzt man $c_k=\frac{1}{2\pi}\int_0^{2\pi}g(e^{it})e^{-ikt}\,dt$ ein und vertauscht (für $r<1$ gleichmäßige
Konvergenz, M-Test) Summe und Integral, so ist $v$ die **Faltung** von $g$ mit dem __Poisson-Kern__

$$P_r(\theta):=\sum_{k\in\mathbb{Z}}r^{|k|}e^{ik\theta}, \qquad v(r,\theta)=\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta-t)\,g(e^{it})\,dt.$$

Mit der geometrischen Reihe ($z=re^{i\theta}$, $\sum_{k\ge0}z^k+\sum_{k\ge1}\bar z^k$) erhält man die **geschlossene
Form** und damit die __Poisson-Integralformel__:

$$P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}, \qquad v(r,\theta)=\frac{1}{2\pi}\int_0^{2\pi}\frac{1-r^2}{1-2r\cos(\theta-t)+r^2}\,g(e^{it})\,dt.$$

Dass $v$ wirklich harmonisch ist, folgt, weil $P_r$ für $r<1$ harmonisch ist und man Differentiation und Integral
vertauschen darf (der Poisson-Kern und seine Ableitungen sind auf $[0,1-\delta]\times[0,2\pi]$ gleichmäßig beschränkt).

## Warum die Randwerte angenommen werden

Hier zeigt sich der Vorteil gegenüber dem Dirichlet-Kern: $P_r$ ist eine **echte, nichtnegative Dirac-Schar**. Es gilt
$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta)\,d\theta=1$ **und** $P_r(\theta)\ge0$ (der Zähler $1-r^2>0$, der Nenner $>0$),
also ist $P_r$ — anders als $D_N$ — **gleichmäßig absolut integrierbar**; sein Integral konzentriert sich für $r\nearrow
1$ bei $\theta=0$. Daraus folgt (Lemma 7.27): Für stetiges, $2\pi$-periodisches $f$ konvergiert

$$\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta-t)\,f(t)\,dt\xrightarrow{r\nearrow1} f(\theta) \qquad\text{gleichmäßig in }\theta.$$

Die Nichtnegativität ist genau das, was dem Dirichlet-Kern fehlte — deshalb werden die Randwerte sogar für **bloß
stetige** $g$ angenommen. Zusammengefasst:

**Satz 7.28.** Für stetiges $g:\partial D\to\mathbb{R}$ existiert eine **eindeutige** glatte Lösung $u:D\to\mathbb{R}$
der Laplace-Gleichung $\Delta u=0$ in $D$ mit $\lim_{y\to x}u(y)=g(x)$ für alle $x\in\partial D$.

:::grafik
Links der Poisson-Kern $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ für $r=0.3,0.7,0.9$: ein **nichtnegativer** Buckel,
der mit $r\to1$ immer schärfer bei $\theta=0$ konzentriert (Fläche $1$). Rechts die Scheibe: Randwerte $g$, die Moden
$r^{|k|}e^{ik\theta}$ dämpfen nach innen; im Zentrum $u(0)=$ Mittelwert von $g$.
:::

## Eindeutigkeit und das Maximumprinzip

Die Eindeutigkeit folgt aus dem __Maximumprinzip__: **Harmonische Funktionen nehmen Maximum und Minimum am Rand an.**
Die Differenz zweier Lösungen mit gleichen Randwerten ist dann harmonisch mit Randwert $0$, also überall $0$ — die
Lösungen stimmen überein. *Beweis des Prinzips:* Nähme $u$ ihr Maximum im Inneren an (mit Abstand $\delta>0$ zum
Randmaximum), so hätte $\tilde u(x)=u(x)+\frac{\delta}{2}|x|^2$ ebenfalls ein inneres Maximum bei $x_0\in D$ — dort wäre
aber $\operatorname{spur}D^2\tilde u(x_0)=\Delta u(x_0)+2\delta=2\delta>0$, im Widerspruch zum notwendigen Kriterium
$\operatorname{spur}D^2\tilde u(x_0)\le0$ an einem Maximum. Analog für das Minimum.

**Eigene Deutung (Mittelwerteigenschaft).** Im Zentrum $r=0$ ist $P_0\equiv1$, also

$$u(0)=\frac{1}{2\pi}\int_0^{2\pi}g(e^{it})\,dt$$

— der Wert im Mittelpunkt ist der **Mittelwert der Randwerte**. Das ist die berühmte __Mittelwerteigenschaft__
harmonischer Funktionen (und zugleich der Grund fürs Maximumprinzip: ein Mittelwert kann die Umgebung nicht
übertreffen). Physikalisch: Die stationäre Temperatur im Scheibenmittelpunkt ist das Mittel der Randtemperatur.

**Stolperstein:** (1) __Poisson-Kern vs. Dirichlet-Kern__: $P_r$ gewichtet die Koeffizienten mit **$r^{|k|}$**
(exponentiell gedämpft, nichtnegativ → gute Approximation der Eins); $D_N$ **schneidet** die Reihe hart ab (oszilliert,
nicht nichtnegativ → nur mit Zusatzregularität brauchbar). (2) Die zweite ODE-Lösung $r^{-|k|}$/$\ln r$ wird nur wegen
der **Beschränktheit** bei $r=0$ verworfen — auf einem Kreisring müsste man sie behalten. (3) „Randwerte angenommen"
heißt als **Limes** $\lim_{y\to x}u(y)=g(x)$ — $u$ ist im Inneren glatt, der Randwert ist der stetige Übergang.

:::kern
__Dirichlet-Problem__ auf $D$: $\Delta u=0$, $u|_{\partial D}=g$. __Separation__ $v_k=A_k(r)e^{ik\theta}$ → Euler-ODE
$r^2A_k''+rA_k'-k^2A_k=0$, beschränkte Lösung $A_k=c_k r^{|k|}$ ⇒ $u(r,\theta)=\sum_{k\in\mathbb{Z}}c_k r^{|k|}e^{ik
\theta}$ (Fourier-Koeffizienten $c_k$ von $g$; Mode klingt mit $r^{|k|}$ ab). __Poisson-Kern__ $P_r(\theta)=\sum_k
r^{|k|}e^{ik\theta}=\frac{1-r^2}{1-2r\cos\theta+r^2}$; __Poisson-Integralformel__ $u(r,\theta)=\frac1{2\pi}\int_0^{2\pi}
P_r(\theta-t)g(e^{it})\,dt$. $P_r\ge0$, $\frac1{2\pi}\int P_r=1$ → **nichtnegative Dirac-Schar** ⇒ Randwerte angenommen
(Lemma 7.27, $r\nearrow1$ gleichmäßig). __Satz 7.28__: eindeutige glatte Lösung; Eindeutigkeit via __Maximumprinzip__
(harmonisch ⇒ Max/Min am Rand). __Mittelwerteigenschaft__ $u(0)=\frac1{2\pi}\int g$. Gegensatz: $P_r$ (Dämpfung
$r^{|k|}$, nichtnegativ) vs. $D_N$ (Abschneiden, oszillierend).
:::

Damit schließt das Fourier-Kapitel: von der Zerlegung in Schwingungen über $L^2$- und punktweise Konvergenz bis zur
Lösung der Laplace-Gleichung. Das letzte Kapitel wechselt zur __Wahrscheinlichkeitsrechnung__ — Wahrscheinlichkeits-
räume, Zufallsvariablen und die Grenzwertsätze. Das ist der Start des nächsten Kapitels.

:::quiz
F: Was fragt das Dirichlet-Problem anschaulich, und was heißt „harmonisch"?
A: Gesucht ist die Gleichgewichtsverteilung im Inneren einer Scheibe (z. B. stationäre Temperatur), wenn am Rand feste Werte $g$ vorgegeben sind. „Harmonisch" ($\Delta u=0$) bedeutet quellenfrei — die Funktion gleicht sich überall glatt aus, ohne Maxima oder Minima im Inneren zu erzeugen.
F: Was ist die Grundidee des Separationsansatzes $v_k=A_k(r)e^{ik\theta}$?
A: Man zerlegt die Randfunktion in Fourier-Moden $e^{ik\theta}$ und sucht für jede getrennt die radiale Fortsetzung $A_k(r)$ ins Innere. Die Laplace-Gleichung entkoppelt dann in eine gewöhnliche ODE pro Mode, die man einzeln lösen kann.
F: Warum wird von den beiden ODE-Lösungen nur $A_k(r)=c_k r^{|k|}$ behalten?
A: Die zweite Lösung ($r^{-|k|}$ bzw. $\ln r$ für $k=0$) wird bei $r=0$ unbeschränkt. Da $u$ auf der ganzen Scheibe (inklusive Zentrum) glatt sein soll, ist nur die bei $r=0$ beschränkte Lösung $r^{|k|}$ zulässig.
F: Was bedeutet der Dämpfungsfaktor $r^{|k|}$ anschaulich?
A: Jede Rand-Mode klingt nach innen ab, und hohe Frequenzen (großes $|k|$) klingen schneller ab, da $r^{|k|}$ für $r<1$ mit $|k|$ rasch gegen null geht. Feine Randdetails dringen also kaum ins Innere — das Feld wird zur Mitte hin immer glatter.
F: Wie entsteht aus der Modensumme die Poisson-Integralformel?
A: Man setzt die Koeffizienten $c_k=\frac{1}{2\pi}\int g\,e^{-ikt}dt$ in $\sum_k c_k r^{|k|}e^{ik\theta}$ ein und vertauscht (gleichmäßige Konvergenz für $r<1$) Summe und Integral. Die verbleibende Summe $\sum_k r^{|k|}e^{ik(\theta-t)}$ ist der Poisson-Kern, also wird $u$ die Faltung von $g$ mit $P_r$.
F: Welche Eigenschaft des Poisson-Kerns macht ihn dem Dirichlet-Kern überlegen?
A: $P_r$ ist nichtnegativ und erfüllt $\frac{1}{2\pi}\int P_r=1$ — eine echte Dirac-Schar. Der Dirichlet-Kern oszillierte dagegen ins Negative (divergierende Lebesgue-Konstante); die Nichtnegativität von $P_r$ sichert die Approximation der Randwerte.
F: Warum werden die Randwerte sogar für bloß stetiges $g$ angenommen?
A: Weil $P_r$ eine nichtnegative, gleichmäßig absolut integrierbare Dirac-Schar ist, konzentriert sich ihre Masse für $r\nearrow1$ bei $\theta=0$. Die Faltung $P_r*g$ konvergiert dann gleichmäßig gegen $g$ — bloße Stetigkeit genügt, anders als beim Dirichlet-Kern.
F: Was besagt die Mittelwerteigenschaft, und wie folgt sie aus der Lösung?
A: Im Zentrum ist $P_0\equiv1$, also $u(0)=\frac{1}{2\pi}\int_0^{2\pi}g(e^{it})\,dt$ — der Wert im Mittelpunkt ist das Mittel der Randwerte. Allgemein ist jeder Wert einer harmonischen Funktion der Mittelwert über jeden umgebenden Kreis.
F: Wie sichert das Maximumprinzip die Eindeutigkeit der Lösung?
A: Harmonische Funktionen nehmen Maximum und Minimum am Rand an. Die Differenz zweier Lösungen mit gleichem Rand ist harmonisch mit Randwert null, liegt also zwischen null und null — sie ist überall null, die Lösungen stimmen überein.
F: Warum kann eine harmonische Funktion kein echtes Maximum im Inneren haben (Beweisidee)?
A: Nähme $u$ innen ein Maximum an, hätte die leicht gestörte Funktion $\tilde u=u+\frac\delta2|x|^2$ dort auch ein Maximum, wo die Spur der Hesse-Matrix $\le0$ sein müsste. Aber $\operatorname{spur}D^2\tilde u=\Delta u+2\delta=2\delta>0$ — ein Widerspruch, also liegt das Maximum am Rand.
:::
