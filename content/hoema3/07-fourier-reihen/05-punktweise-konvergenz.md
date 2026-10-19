---
title: Punktweise Konvergenz von Fourier-Reihen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3070500
summary: Von Grund auf – das Fourierpolynom ist die Faltung $T_Nf=D_N*f$ mit dem Dirichlet-Kern $D_N(x)=\frac{\sin((N+\frac12)x)}{\sin(x/2)}$. Dieser ist Dirac-artig, aber nicht nichtnegativ (die Lebesgue-Konstante $\int|D_N|\to\infty$), weshalb Stetigkeit allein nicht reicht. Für stückweise stetig differenzierbares $f$ konvergiert $T_Nf(x)\to\frac12(f(x+)+f(x-))$ – an Sprüngen gegen den Mittelwert, bei stetigen Funktionen sogar gleichmäßig.
tags: punktweise Konvergenz, Dirichlet-Kern, Faltung, Lebesgue-Konstante, Sprungstelle, Gibbs-Phänomen, gleichmäßige Konvergenz, Du Bois-Reymond
---

:::grafik
Einstiegs-Animation: Das Fourierpolynom als **Mittelung** — $T_Nf(x)$ entsteht, indem man $f$ mit dem __Dirichlet-Kern__
$D_N$ faltet. $D_N$ ist ein hoher, zentraler Zacken bei $0$ (Dirac-artig), aber mit **Nebenzipfeln, die ins Negative
schwingen** und mit $N$ nicht abklingen. Darunter: Für eine stückweise glatte Funktion mit Sprung konvergieren die
$T_Nf$ in den glatten Bereichen sauber, treffen am Sprung den __Mittelwert__ der beiden Seiten und zeigen dort den
festen __Gibbs-Überschwinger__. Kernbotschaft: Weil $D_N$ oszilliert (nicht nichtnegativ), braucht punktweise
Konvergenz etwas mehr als bloße Stetigkeit.
:::

:::konzept
Die $L^2$-Konvergenz (Artikel 3) macht keine Aussage über einzelne Punkte. Hier klären wir die __punktweise__ Frage:
Gilt $T_Nf(x)\to f(x)$ an einem festen $x$? Der Schlüssel ist, das Fourierpolynom als __Faltung mit dem Dirichlet-Kern__
zu lesen — eine Mittelung wie bei den Dirac-Scharen. Der entscheidende Unterschied: Der Dirichlet-Kern ist zwar
Dirac-artig, aber **nicht nichtnegativ** und nicht gleichmäßig integrierbar. Deshalb reicht bloße Stetigkeit **nicht**
(Fourier irrte sich hier), und man braucht eine Regularitätsbedingung — stückweise stetige Differenzierbarkeit. Dann
konvergiert die Reihe überall, an Sprüngen gegen den **Mittelwert**.
:::

**Worum es geht:** Wir schreiben $T_Nf=D_N*f$ mit dem __Dirichlet-Kern__ (Lemma 7.19), erklären, warum Stetigkeit nicht
genügt (__Lebesgue-Konstante__), und beweisen die __punktweise__ (Satz 7.21) und __gleichmäßige__ (Satz 7.25)
Konvergenz.

## Das Fourierpolynom als Faltung: der Dirichlet-Kern

Setzt man die Koeffizienten $c_k=\frac{1}{2\pi}\int_0^{2\pi}f(y)e^{-iky}dy$ in $T_Nf=\sum_{|k|\le N}c_k e^{ikx}$ ein und
vertauscht Summe und Integral, so ist

$$T_Nf(x)=\frac{1}{2\pi}\int_0^{2\pi}D_N(x-y)\,f(y)\,dy=(D_N*f)(x), \qquad D_N(x):=\sum_{|k|\le N}e^{ikx},$$

mit der **periodischen Faltung** $(f*g)(x)=\frac{1}{2\pi}\int_0^{2\pi}f(x-y)g(y)\,dy$. Das Fourierpolynom ist also die
Faltung von $f$ mit dem __Dirichlet-Kern__ $D_N$ — genau die Dirac-artige Mittelung aus dem letzten Artikel.

**Lemma 7.19.** $D_N$ ist eine **gerade**, $2\pi$-periodische, stetige Funktion mit

$$D_N(x)=\begin{cases}\dfrac{\sin\!\big((N+\frac12)x\big)}{\sin\frac{x}{2}}, & x\in(0,2\pi),\\[2mm] 2N+1, & x=0,\end{cases}$$

(die geschlossene Form kennen wir aus Lemma 7.8; der Wert bei $0$ folgt mit L'Hospital). Weiter gilt **(i)** $\frac{1}
{2\pi}\int_0^{2\pi}D_N(x)\,dx=1$ und **(ii)** $T_Nf(x)=\frac{1}{2\pi}\int_0^{2\pi}D_N(y)\,f(x\pm y)\,dy$ (die beiden
Vorzeichen folgen aus der Geradheit $D_N(-y)=D_N(y)$ und Substitution).

## Warum Stetigkeit nicht reicht: die Lebesgue-Konstante

Der Dirichlet-Kern hat zwar Eigenschaft (i) wie eine Approximation der Eins und konzentriert sich bei $x=0$ (bzw.
$2\pi k$). **Aber** — und das ist der entscheidende Unterschied zu einer echten Dirac-Schar — er **oszilliert** für
wachsendes $N$ immer stärker und ist **nicht nichtnegativ**. Seine absolute Masse divergiert (Bemerkung 7.20):

$$\int_0^{2\pi}|D_N(x)|\,dx\xrightarrow{N\to\infty}\infty \qquad(\text{die }\textit{Lebesgue-Konstante}).$$

Deshalb lässt sich die punktweise Konvergenz $D_N*f\to f$ für **bloß stetige** $f$ **nicht** zeigen — die positiven und
negativen Zipfel können sich für ungünstige stetige Funktionen aufschaukeln. Es braucht mehr Regularität (etwa eine
__Lipschitz__-Bedingung $|f(x)-f(y)|\le c\,|x-y|$).

:::grafik
Der Dirichlet-Kern $D_N(y)=\frac{\sin((N+\frac12)y)}{\sin(y/2)}$ für wachsendes $N$: zentraler Peak der Höhe $2N+1$,
flankiert von **abwechselnd positiven und negativen** Nebenzipfeln, die nicht abklingen; die Fläche unter $|D_N|$
(Lebesgue-Konstante) wächst $\sim\ln N$. Kontrast zu einem nichtnegativen Dirac-Kern daneben.
:::

## Punktweise Konvergenz gegen den Mittelwert

**Satz 7.21 (Punktweise Konvergenz).** Ist $f$ $2\pi$-periodisch und **stückweise stetig differenzierbar**, so gilt für
**alle** $x\in\mathbb{R}$

$$T_Nf(x)\longrightarrow \frac12\big(f(x+)+f(x-)\big)\qquad(N\to\infty), \qquad f(x\pm)=\lim_{h\downarrow0}f(x\pm h).$$

An **Stetigkeitsstellen** ist das $f(x)$, an **Sprungstellen** der **Mittelwert** der einseitigen Grenzwerte.
„Stückweise stetig differenzierbar" (Bem. 7.22) heißt: Die einseitigen Ableitungen $f'(x\pm)$ existieren überall und
$f'$ ist stückweise stetig.

*Beweisidee.* Mit Lemma 7.19(ii) und (i) schreibt man $T_Nf(x)-\frac12(f(x+)+f(x-))=I_N$ als

$$I_N=\frac{1}{2\pi}\int_0^{2\pi} g(y)\,\sin\!\Big((N+\tfrac12)y\Big)\,dy, \qquad g(y)=\frac{f(x+y)-f(x+)+f(x-y)-f(x-)}{2\sin\frac{y}{2}}.$$

Wegen $2\sin\frac{y}{2}\approx y$ für kleine $y$ existiert $\lim_{y\downarrow0}g(y)=f'(x+)+f'(x-)$ — also ist $g$
stückweise stetig, insbesondere $R$-integrierbar. Mit dem Additionstheorem $\sin((N+\frac12)y)=\cos\frac{y}{2}\sin(Ny)
+\sin\frac{y}{2}\cos(Ny)$ wird $I_N$ zu einer Kombination von Fourier-Koeffizienten zweier stückweise stetiger
Funktionen — und die bilden nach **Bessel/Riemann-Lebesgue** (Satz 7.13) eine **Nullfolge**. Also $I_N\to0$. $\square$

**Beispiel 7.23 (Sägezahn).** Das prototypische Beispiel: In den glatten Bereichen konvergiert die Reihe $\sum\frac
{\sin kx}{k}$ gleichmäßig, an den Sprungstellen punktweise gegen den **Mittelwert** $0$ — genau wie in Artikel 2
beobachtet.

**Historisches (Bem. 7.24).** Fourier behauptete, die Reihe konvergiere für **jede** stetige $2\pi$-periodische
Funktion punktweise gegen $f$. Du Bois-Reymond widerlegte das mit einem **Gegenbeispiel** (eine stetige Funktion mit in
einem Punkt divergierender Fourier-Reihe). Ohne die stückweise stetige Differenzierbarkeit ist der Satz i. A.
**falsch**.

## Gleichmäßige Konvergenz und das Koeffizienten-Kriterium

Dieselben Argumente, gleichmäßig in $x$ geführt, geben:

**Satz 7.25.** Ist $f$ $2\pi$-periodisch, **stetig und stückweise stetig differenzierbar**, so konvergieren die
Fourierpolynome $T_Nf$ **gleichmäßig** gegen $f$ (kein Sprung ⇒ überall der Funktionswert, und der Fehler $I_N(x)\to0$
gleichmäßig).

Oft ist eine Funktion direkt **als** trigonometrische Reihe gegeben (etwa als Lösung einer Differentialgleichung), und
man will Stetigkeit/Differenzierbarkeit **direkt an den Koeffizienten** ablesen. Das leistet der Weierstraßsche M-Test:

**Satz 7.26.** Ist $\sum_{k\in\mathbb{Z}}|c_k|<\infty$, so konvergiert $f(x)=\sum_{k\in\mathbb{Z}}c_k e^{ikx}$
**gleichmäßig** und ist **stetig**. Ist sogar $\sum_{k\in\mathbb{Z}}|k|^m|c_k|<\infty$, so konvergieren die
Ableitungen bis zur Ordnung $m$ gleichmäßig, $f$ ist $m$-mal stetig differenzierbar, und

$$\frac{d^\ell}{dx^\ell}f(x)=\sum_{k\in\mathbb{Z}}(ik)^\ell c_k e^{ikx}\qquad(1\le\ell\le m).$$

Das quantifiziert das Prinzip aus Artikel 2: **Schneller Koeffizientenabfall ⇒ mehr Glattheit.** Fallen die $c_k$ wie
$1/|k|^{m+2}$, so ist $f$ mindestens $m$-mal stetig differenzierbar.

**Stolperstein:** (1) An einer **Sprungstelle** liefert die Reihe den **Mittelwert** $\frac12(f(x+)+f(x-))$, nicht
einen der beiden Werte — und die Konvergenz ist dort **nicht** gleichmäßig (__Gibbs-Phänomen__: ein fester ~9 %-Über-
schwinger, der nicht verschwindet, sondern nur schmaler wird). (2) Der Dirichlet-Kern ist **nicht nichtnegativ**
($\int|D_N|\to\infty$) — daher versagt das einfache Dirac-Argument; der nichtnegative __Fejér-Kern__ (Cesàro-Mittel)
konvergiert für **alle** stetigen $f$ gleichmäßig. (3) Bloße Stetigkeit garantiert **keine** punktweise Konvergenz
(Du Bois-Reymond); man braucht stückweise $C^1$ bzw. ein Koeffizienten-Kriterium.

:::kern
$T_Nf=D_N*f$ mit __Dirichlet-Kern__ $D_N(x)=\sum_{|k|\le N}e^{ikx}=\frac{\sin((N+\frac12)x)}{\sin(x/2)}$ (bei $0$:
$2N+1$), gerade, $\frac1{2\pi}\int_0^{2\pi}D_N=1$, $T_Nf(x)=\frac1{2\pi}\int_0^{2\pi}D_N(y)f(x\pm y)\,dy$ (Lemma 7.19).
$D_N$ Dirac-artig, aber **nicht nichtnegativ**: $\int_0^{2\pi}|D_N|\to\infty$ (__Lebesgue-Konstante__) ⇒ Stetigkeit
reicht **nicht**. __Satz 7.21__: $f$ stückweise stetig diff ⇒ $T_Nf(x)\to\frac12(f(x+)+f(x-))$ (Stetigkeitsstelle:
$f(x)$; Sprung: Mittelwert); Beweis via $I_N=\frac1{2\pi}\int g(y)\sin((N+\frac12)y)\,dy\to0$ (Riemann-Lebesgue).
__Satz 7.25__: $f$ stetig + stückweise $C^1$ ⇒ gleichmäßig. __Satz 7.26__: $\sum|c_k|<\infty$ ⇒ stetig/gleichmäßig;
$\sum|k|^m|c_k|<\infty$ ⇒ $m$-mal stetig diff, $f^{(\ell)}=\sum(ik)^\ell c_k e^{ikx}$. Sprung → __Gibbs__ (~9 %);
Du Bois-Reymond: stetig ⇏ punktweise.
:::

Zum Abschluss des Kapitels wenden wir die Fourier-Theorie auf eine **partielle Differentialgleichung** an: Das
__Dirichlet-Problem__ auf der Einheitskreisscheibe (harmonische Funktion mit vorgegebenem Rand) löst sich durch eine
Fourier-Reihe mit dem __Poisson-Kern__ — das Thema des nächsten Artikels.
