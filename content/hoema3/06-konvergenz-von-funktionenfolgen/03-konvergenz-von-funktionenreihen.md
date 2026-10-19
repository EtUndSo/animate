---
title: Konvergenz von Funktionenreihen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3060300
summary: Von Grund auf – eine Funktionenreihe $\sum_k g_k(x)$ ist die Folge ihrer Partialsummen, also fällt alles über Funktionenfolgen auf sie zurück. Der Weierstraßsche M-Test liefert ein einfaches Kriterium für gleichmäßige Konvergenz ($|g_k|\le M_k$, $\sum M_k<\infty$). Damit sind Potenzreihen innerhalb ihres Konvergenzradius $R$ stetig, gliedweise differenzierbar und sogar beliebig glatt.
tags: Funktionenreihe, Potenzreihe, Weierstraß M-Test, Majorantenkriterium, Konvergenzradius, Cauchy-Hadamard, gliedweise Differentiation, gleichmäßige Konvergenz
---

:::grafik
Einstiegs-Animation: Eine Funktionenreihe $\sum_k g_k(x)$ baut sich auf — Partialsummen $f_0,f_1,f_2,\dots$ legen sich
übereinander und nähern sich der Summenfunktion $f$. Rechts der __Weierstraßsche M-Test__: Jeder Summand $g_k$ liegt
betragsmäßig unter einer Schranke $M_k$ (ein waagrechter Deckel), und solange die Zahlenreihe $\sum M_k$ konvergiert,
spannt sich ein $\varepsilon$-Schlauch um $f$ — die Reihe konvergiert **gleichmäßig**. Beispiel: eine Potenzreihe
$\sum a_k x^k$ innerhalb ihres Konvergenzkreises mit Radius $R$. Kernbotschaft: Eine summierbare Zahlen-Majorante
erzwingt gleichmäßige Konvergenz der Funktionenreihe.
:::

:::konzept
Die wichtigsten Funktionen der Analysis — Exponentialfunktion, Sinus, später die Fourier-Reihen — sind als
**unendliche Reihen** definiert: $f(x)=\sum_{k=0}^\infty g_k(x)$. Damit stellt sich sofort die Frage, in welchem Sinne
so eine Reihe konvergiert und ob die Summenfunktion die guten Eigenschaften (Stetigkeit, Differenzierbarkeit) der
Summanden **erbt**. Der Schlüssel ist einfach: Eine Reihe **ist** die Folge ihrer __Partialsummen__, also greift alles
aus den letzten beiden Artikeln. Es fehlt nur noch ein bequemes Kriterium für gleichmäßige Konvergenz — der
__Weierstraßsche M-Test__ — und dann ist der Weg frei zur gesamten Theorie der Potenz- und Fourier-Reihen.
:::

**Worum es geht:** Wir fassen eine __Funktionenreihe__ als Folge der Partialsummen auf, beweisen den __Weierstraßschen
M-Test__ und wenden ihn auf __Potenzreihen__ an (Stetigkeit und gliedweise Differenzierbarkeit im Konvergenzkreis).

## Funktionenreihen als Partialsummen

Eine __Funktionenreihe__ hat die Form

$$f(x)=\sum_{k=0}^\infty g_k(x), \qquad\text{mit Partialsummen}\qquad f_n(x)=\sum_{k=0}^n g_k(x).$$

Die Reihe konvergiert (punktweise, gleichmäßig, absolut) genau dann, wenn die **Folge der Partialsummen** $f_n$ im
entsprechenden Sinne konvergiert — Funktionenreihen fügen sich also lückenlos in das Konzept der Funktionenfolgen ein,
und alle Vertauschungssätze des letzten Artikels gelten für sie. Zwei zentrale Spezialfälle:

- __Potenzreihen__: $g_k(x)=a_k(x-x_0)^k$ (reell oder komplex),
- __Fourier-Reihen__: $g_k(x)=c_k e^{ikx}$ (das Thema des nächsten Kapitels).

## Der Weierstraßsche M-Test

**Satz 6.9 (Weierstraßscher M-Test).** Sei $g_k:[a,b]\to\mathbb{C}$ eine Funktionenfolge mit

$$|g_k(x)|\le M_k \quad\text{für alle } x\in[a,b], \qquad\text{und}\qquad \sum_{k=0}^\infty M_k<\infty.$$

Dann konvergiert $f_n(x)=\sum_{k=0}^n g_k(x)$ **gleichmäßig** auf $[a,b]$.

*Beweis (elementar, über das Cauchy-Kriterium).* Für $m<n$ ist

$$\sup_{x\in[a,b]}|f_m(x)-f_n(x)|=\sup_{x\in[a,b]}\Big|\sum_{k=m+1}^n g_k(x)\Big|\le\sum_{k=m+1}^n M_k\le\sum_{k=m+1}^\infty M_k\xrightarrow{m\to\infty}0,$$

denn der Reihenrest einer **konvergenten** Zahlenreihe $\sum M_k$ geht gegen null. Nach dem Cauchy-Kriterium (Lemma
6.3) konvergiert $(f_n)$ gleichmäßig. $\square$ Der Trick: Man drückt die **funktionale** Konvergenz durch eine
**summierbare Zahlenreihe** $\sum M_k$ nieder — eine Majorante, die nicht mehr von $x$ abhängt. Daraus folgt mit Satz
6.4 sofort, dass die Summe einer solchen Reihe stetiger Funktionen wieder **stetig** ist.

**Eigenes Beispiel.** Die Reihe $\sum_{k=1}^\infty\frac{\sin(kx)}{k^2}$ konvergiert auf ganz $\mathbb{R}$ gleichmäßig:
Es ist $\big|\frac{\sin(kx)}{k^2}\big|\le\frac{1}{k^2}=:M_k$, und $\sum\frac1{k^2}=\frac{\pi^2}{6}<\infty$. Die
Summenfunktion ist daher stetig — obwohl man sie nicht elementar hinschreiben kann.

## Potenzreihen: Konvergenzradius

Für eine Potenzreihe $\sum_{k=0}^\infty a_k(x-x_0)^k$ ist der __Konvergenzradius__

$$R:=\sup\Big\{\,|y|:\ \sum_{k=0}^\infty a_k y^k \text{ konvergiert}\,\Big\} = \sup\Big\{\,r>0:\ \sum_{k=0}^\infty |a_k|\,r^k \text{ konvergiert}\,\Big\},$$

mit der Formel von __Cauchy–Hadamard__ $R=1/\limsup_{k\to\infty}\sqrt[k]{|a_k|}$. Die Reihe konvergiert für $|x-x_0|<R$
**absolut** und divergiert für $|x-x_0|>R$; am Rand $|x-x_0|=R$ ist eine gesonderte Prüfung nötig. Der Name
„Konvergenz**radius**" stammt vom komplexen Fall $f(z)=\sum c_k(z-z_0)^k$: Dort konvergiert die Reihe im
__Konvergenzkreis__ $B_R(z_0)=\{z\in\mathbb{C}:|z-z_0|<R\}$ und divergiert außerhalb.

## Stetigkeit und gliedweise Differenzierbarkeit

**Satz 6.10.** Habe $\sum a_k(x-x_0)^k$ den Konvergenzradius $R>0$, und sei $0<r<R$. Dann konvergiert die
Partialsummenfolge **gleichmäßig** für alle $x$ mit $|x-x_0|\le r$, und folglich ist die Potenzreihe eine **stetige**
Funktion in $|x-x_0|<R$.

*Beweis (M-Test).* Für $|x-x_0|\le r$ ist $|g_k(x)|=|a_k(x-x_0)^k|\le|a_k|r^k=:M_k$, und $(M_k)$ ist nach Definition
von $R$ (wegen $r<R$) **summierbar**. Also greift der Weierstraßsche M-Test: gleichmäßige Konvergenz auf $|x-x_0|\le
r$, und als gleichmäßiger Limes stetiger Polynome ist die Summe dort stetig. Da $r$ beliebig nahe an $R$ heranreicht,
ist die Potenzreihe im **ganzen** offenen Kreis $|x-x_0|<R$ stetig. $\square$

**Gliedweise Differentiation.** Die formale Ableitung $\sum_{k=1}^\infty k\,a_k(x-x_0)^{k-1}$ hat **denselben**
Konvergenzradius $R$ (denn $\sqrt[k]{k}\to1$ ändert den $\limsup$ nicht). Nach Satz 6.8 (gliedweise Differentiation bei
gleichmäßiger Konvergenz der Ableitungen) ist die Potenzreihe in $|x-x_0|<R$ stetig differenzierbar mit

$$f'(x)=\frac{d}{dx}\sum_{k=0}^\infty a_k(x-x_0)^k=\sum_{k=1}^\infty k\,a_k(x-x_0)^{k-1}.$$

Induktiv folgt: **Potenzreihen sind in ihrem Konvergenzkreis beliebig oft differenzierbar** (glatt). Das ist der tiefe
Grund, warum $e^x=\sum\frac{x^k}{k!}$, $\sin x$, $\cos x$ so gutartig sind.

**Eigene Beispiele.** (1) Die geometrische Reihe $\sum_{k=0}^\infty x^k=\frac{1}{1-x}$ hat $R=1$ (gleichmäßig nur auf
$|x|\le r<1$, **nicht** auf ganz $(-1,1)$ — bei $x\to1$ wächst die Summe über alle Grenzen). (2) Die Exponentialreihe
$\sum_{k=0}^\infty\frac{x^k}{k!}$ hat $R=\infty$ (wegen $\sqrt[k]{1/k!}\to0$) — sie konvergiert auf jedem beschränkten
Intervall gleichmäßig und definiert die glatte Funktion $e^x$.

:::grafik
Links der M-Test an $\sum\sin(kx)/k^2$: die Summanden unter den Deckeln $1/k^2$, die Zahlenreihe $\sum1/k^2=\pi^2/6$
konvergiert. Rechts eine Potenzreihe mit Konvergenzkreis Radius $R$: gleichmäßige Konvergenz auf jeder abgeschlossenen
Scheibe $|x-x_0|\le r<R$ (grün), Divergenz außerhalb (rot), Rand $|x-x_0|=R$ als „Einzelfallprüfung" markiert.
:::

**Stolperstein:** (1) Die gleichmäßige Konvergenz einer Potenzreihe gilt nur auf **kompakten** Teilscheiben $|x-x_0|\le
r<R$ — am offenen Rand $r\to R$ kann sie verloren gehen (geometrische Reihe). (2) Der M-Test ist **hinreichend, nicht
notwendig**: Reihen können gleichmäßig konvergieren, ohne eine summierbare Majorante zu haben (z. B. bedingt
konvergente Fälle). (3) Gliedweise Differentiation braucht die gleichmäßige Konvergenz der **abgeleiteten** Reihe —
bei Potenzreihen automatisch erfüllt (gleicher Radius $R$), bei Fourier-Reihen aber **nicht** selbstverständlich.

:::kern
Eine __Funktionenreihe__ $f(x)=\sum_{k=0}^\infty g_k(x)$ ist die Folge ihrer __Partialsummen__ $f_n=\sum_{k=0}^n g_k$;
alle Konvergenz- und Vertauschungssätze gelten. __Weierstraßscher M-Test__ (Satz 6.9): $|g_k(x)|\le M_k\ \forall x$ und
$\sum M_k<\infty$ ⇒ $\sum g_k$ **gleichmäßig** konvergent (Beweis: $\sup|\sum_{k=m+1}^n g_k|\le\sum_{k=m+1}^\infty M_k
\to0$). __Potenzreihe__ $\sum a_k(x-x_0)^k$: Konvergenzradius $R=\sup\{r>0:\sum|a_k|r^k<\infty\}=1/\limsup_k\sqrt[k]
{|a_k|}$ (Cauchy–Hadamard); konvergiert absolut für $|x-x_0|<R$, divergiert für $>R$, Rand gesondert. Satz 6.10: auf
jeder Scheibe $|x-x_0|\le r<R$ gleichmäßig ⇒ **stetig** in $|x-x_0|<R$; formale Ableitung $\sum k\,a_k(x-x_0)^{k-1}$ hat
**denselben** $R$ ⇒ gliedweise differenzierbar, induktiv **beliebig glatt**. Beispiele: $\sum\sin(kx)/k^2$ (M-Test,
$R$ n/a), geom. Reihe $R=1$, $e^x=\sum x^k/k!$ ($R=\infty$).
:::

Als Nächstes betten wir die stetigen Funktionen in einen __normierten Vektorraum__ ein (Supremumsnorm und $L^2$-Norm)
und lernen die __Konvergenz im quadratischen Mittel__ — den Konvergenzbegriff, in dem Fourier-Reihen am natürlichsten
leben. Das ist das Thema des nächsten Artikels.

:::quiz
F: Warum lässt sich die ganze Theorie der Funktionenfolgen direkt auf Funktionenreihen übertragen?
A: Eine Reihe $\sum_k g_k$ ist definitionsgemäß die Folge ihrer Partialsummen $f_n=\sum_{k=0}^n g_k$. Jede Aussage über Konvergenz und Vertauschbarkeit von Funktionenfolgen gilt daher unverändert für die Partialsummen — Reihen sind ein Spezialfall, kein neues Konzept.
F: Was ist die Grundidee des Weierstraßschen M-Tests?
A: Man schätzt jeden Summanden durch eine von $x$ unabhängige Zahl ab, $|g_k(x)|\le M_k$, und verlangt, dass die reine Zahlenreihe $\sum M_k$ konvergiert. Diese summierbare Majorante erzwingt dann die gleichmäßige Konvergenz der Funktionenreihe.
F: Wieso folgt aus einer konvergenten Zahlen-Majorante die gleichmäßige Konvergenz der Funktionenreihe?
A: Der Supremumsabstand zweier Partialsummen ist $\sup_x|\sum_{k=m+1}^n g_k(x)|\le\sum_{k=m+1}^\infty M_k$. Da der Reihenrest einer konvergenten Zahlenreihe gegen null geht, erfüllt die Partialsummenfolge das Cauchy-Kriterium gleichmäßig.
F: Warum ist es so nützlich, die funktionale Konvergenz auf eine Zahlenreihe zurückzuführen?
A: Die Schranke $M_k$ hängt nicht mehr von $x$ ab, also kontrolliert eine einzige Zahlenreihe das Verhalten an allen Stellen gleichzeitig. Damit wird ein schwer greifbares gleichmäßiges Konvergenzproblem zu einer gewöhnlichen Reihenkonvergenz-Frage.
F: Was bedeutet der Konvergenzradius $R$ einer Potenzreihe, und was passiert bei $|x-x_0|=R$?
A: Für $|x-x_0|<R$ konvergiert die Reihe absolut, für $|x-x_0|>R$ divergiert sie. Genau am Rand $|x-x_0|=R$ ist keine allgemeine Aussage möglich — dort muss man jeden Fall einzeln prüfen.
F: Warum gilt die gleichmäßige Konvergenz einer Potenzreihe nur auf abgeschlossenen Teilscheiben $|x-x_0|\le r<R$ und nicht auf dem ganzen offenen Kreis?
A: Der M-Test braucht als Majorante $|a_k|r^k$ mit festem $r<R$; nur dann ist $\sum|a_k|r^k$ summierbar. Lässt man $r\to R$, kann die Konvergenz ungleichmäßig werden — die geometrische Reihe etwa wächst bei $x\to1$ über alle Grenzen.
F: Warum ist eine Potenzreihe in ihrem Konvergenzkreis sogar beliebig oft differenzierbar?
A: Die gliedweise abgeleitete Reihe hat denselben Konvergenzradius $R$ (da $\sqrt[k]{k}\to1$), konvergiert also wieder gleichmäßig auf Teilscheiben. Satz 6.8 erlaubt dann gliedweises Ableiten; dieses Argument lässt sich induktiv wiederholen, also ist $f$ glatt.
F: Warum ändert der Faktor $k$ beim Ableiten den Konvergenzradius nicht?
A: Cauchy–Hadamard gibt $R=1/\limsup\sqrt[k]{|a_k|}$. Beim Ableiten tritt der Faktor $k$ auf, aber $\sqrt[k]{k}\to1$, sodass sich der $\limsup$ und damit $R$ nicht ändert — die abgeleitete Reihe konvergiert im selben Kreis.
F: Warum ist der M-Test ein hinreichendes, aber kein notwendiges Kriterium?
A: Er garantiert gleichmäßige Konvergenz nur, wenn eine summierbare Majorante existiert. Es gibt aber gleichmäßig konvergente Reihen ohne solche Majorante (etwa bedingt konvergente Fälle), bei denen der M-Test einfach nicht greift, obwohl die Konvergenz vorliegt.
F: Warum ist die gliedweise Differenzierbarkeit bei Fourier-Reihen — anders als bei Potenzreihen — nicht selbstverständlich?
A: Bei Potenzreihen hat die abgeleitete Reihe automatisch denselben Radius und konvergiert gleichmäßig. Die Ableitung einer Fourier-Reihe bringt dagegen Faktoren $k$ in die Koeffizienten, die die Konvergenz zerstören können — gleichmäßige Konvergenz der abgeleiteten Reihe muss hier eigens geprüft werden.
:::
