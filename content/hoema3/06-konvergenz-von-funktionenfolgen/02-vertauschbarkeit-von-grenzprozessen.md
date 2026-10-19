---
title: Vertauschbarkeit von Grenzprozessen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3060200
summary: Von Grund auf – warum gleichmäßige Konvergenz das stärkere Werkzeug ist. Der gleichmäßige Limes stetiger Funktionen ist wieder stetig, und man darf Grenzwert und Integral vertauschen, $\lim_n\int f_n=\int\lim_n f_n$. Bei der Differentiation genügt gleichmäßige Konvergenz der $f_n$ allein nicht – es müssen die Ableitungen $f_n'$ gleichmäßig konvergieren, dann ist $f'=\lim_n f_n'$.
tags: gleichmäßige Konvergenz, Stetigkeit, Vertauschung, Grenzwert und Integral, gliedweise Differentiation, Grenzprozesse, Hauptsatz
---

:::grafik
Einstiegs-Animation: Das Leitmotiv „darf man die Reihenfolge tauschen?". Drei Paare von Operationen: $\lim$ gegen
__Stetigkeit__ (Grenzübergang in $x$), $\lim$ gegen __Integral__ ($\int$), $\lim$ gegen __Ableitung__ ($\tfrac{d}{dx}$).
Bei gleichmäßiger Konvergenz schließt sich jedes Diagramm (beide Wege führen zum selben Ergebnis) — für Stetigkeit und
Integral genügt $f_n\to f$ gleichmäßig, für die Ableitung muss zusätzlich $f_n'$ gleichmäßig konvergieren. Als Warnung
blinkt ein „Wanderhöcker" $g_n$ auf, dessen Fläche $1$ bleibt, obwohl $g_n\to0$ punktweise — hier **scheitert** die
Vertauschung. Kernbotschaft: Gleichmäßige Konvergenz macht Grenzprozesse vertauschbar.
:::

:::konzept
Im letzten Artikel haben wir gesehen: Der punktweise Limes stetiger Funktionen kann **unstetig** sein ($x^n$). Das ist
ein Symptom eines allgemeinen Problems — bei **punktweiser** Konvergenz darf man den Grenzwert $\lim_n$ im Allgemeinen
**nicht** mit anderen Grenzprozessen (Grenzübergang in $x$, Integration, Differentiation) **vertauschen**. Die
__gleichmäßige Konvergenz__ repariert das: Sie ist genau die Zusatzbedingung, unter der diese Vertauschungen erlaubt
sind. Das ist der Grund, warum sie das Arbeitspferd der Analysis ist — und die Voraussetzung dafür, dass man Potenz-
und Fourier-Reihen **gliedweise** integrieren und (unter Zusatzbedingung) differenzieren darf.
:::

**Worum es geht:** Drei Vertauschungssätze — gleichmäßiger Limes erhält __Stetigkeit__ (Satz 6.4), vertauscht mit dem
__Integral__ (Satz 6.6) und — bei gleichmäßiger Konvergenz der Ableitungen — mit der __Differentiation__ (Satz 6.8).

## Stetigkeit bleibt erhalten

**Satz 6.4.** Ist $(f_n)$ eine Folge **stetiger** Funktionen auf $[a,b]$ mit $f_n\to f$ **gleichmäßig**, so ist die
Grenzfunktion $f:[a,b]\to\mathbb{C}$ stetig.

*Beweis ($\varepsilon/3$-Argument).* Sei $\varepsilon>0$. Wegen gleichmäßiger Konvergenz gibt es ein $n_0$ mit
$|f(x)-f_{n_0}(x)|<\varepsilon/3$ für **alle** $x$. Da $f_{n_0}$ stetig ist, gibt es ein $\delta>0$ mit $|f_{n_0}(x)-
f_{n_0}(y)|<\varepsilon/3$, sobald $|x-y|<\delta$. Dann folgt für $|x-y|<\delta$

$$|f(x)-f(y)|\le\underbrace{|f(x)-f_{n_0}(x)|}_{<\varepsilon/3}+\underbrace{|f_{n_0}(x)-f_{n_0}(y)|}_{<\varepsilon/3}+\underbrace{|f_{n_0}(y)-f(y)|}_{<\varepsilon/3}<\varepsilon.$$

Also ist $f$ stetig. $\square$ In Worten (Bemerkung 6.5): **Gleichmäßig konvergente Folgen stetiger Funktionen
konvergieren gegen eine stetige Funktion.** Dass hier die **Gleichmäßigkeit** zählt, zeigt der Kontrast zu $x^n$ (nur
punktweise, Grenzfunktion unstetig).

## Grenzwert und Integral vertauschen

**Satz 6.6.** Ist $(f_n)$ eine Folge stetiger Funktionen mit $f_n\to f$ **gleichmäßig** auf $[a,b]$, so gilt

$$\lim_{n\to\infty}\int_a^b f_n(x)\,dx = \int_a^b f(x)\,dx = \int_a^b \Big(\lim_{n\to\infty}f_n(x)\Big)\,dx.$$

*Beweis.* Der denkbar einfachste: Für $n\ge N(\varepsilon)$ ist

$$\left|\int_a^b f\,dx-\int_a^b f_n\,dx\right|\le\int_a^b|f(x)-f_n(x)|\,dx\le(b-a)\,\sup_{x\in[a,b]}|f(x)-f_n(x)|=(b-a)\,\|f-f_n\|_\infty\to0.$$

Der ganze Fehler wird durch die Supremumsnorm kontrolliert, mal der Intervalllänge. (Die Voraussetzungen sind
keineswegs optimal — es gibt stärkere Vertauschungssätze, etwa den von Lebesgue — aber dieser genügt für stetige
Funktionen und ist elementar.) **Bemerkung 6.7:** Für komplexwertige $f(x)=u(x)+iv(x)$ ist $\int_a^b f\,dx=\int_a^b u\,
dx+i\int_a^b v\,dx$ und ebenso $f'(x)=u'(x)+iv'(x)$ — alles läuft komponentenweise in Real- und Imaginärteil.

**Warnung (Wanderhöcker).** Ohne gleichmäßige Konvergenz kann die Vertauschung scheitern: Die Höcker $g_n$ mit
$g_n(x)=n$ auf $[0,\tfrac1n]$ und $0$ sonst konvergieren punktweise gegen $0$, aber $\int_0^1 g_n\,dx=1$ für alle $n$ —
also $\lim_n\int g_n=1\neq0=\int\lim_n g_n$. Die „Masse" wandert ins Unendliche statt zu verschwinden.

:::grafik
Oben: gleichmäßige Konvergenz, der $\varepsilon$-Schlauch um $f$; die Flächen unter $f_n$ und $f$ unterscheiden sich um
höchstens $(b-a)\varepsilon$. Unten: der Wanderhöcker $g_n$ (schmaler, höher werdender Rechteckpuls mit konstanter
Fläche $1$), der punktweise gegen $0$ geht, dessen Integral aber $1$ bleibt — Vertauschung verboten.
:::

## Differentiation: die Ableitungen müssen gleichmäßig konvergieren

Bei der Ableitung ist mehr Vorsicht nötig. Es genügt **nicht**, dass $f_n$ gleichmäßig konvergiert — es müssen die
**Ableitungen** $f_n'$ gleichmäßig konvergieren.

**Satz 6.8.** Sei $(f_n)$ eine Folge **stetig differenzierbarer** Funktionen mit $f_n\to f$ **punktweise** auf $[a,b]$
und $(f_n')$ **gleichmäßig** konvergent. Dann ist $f$ stetig differenzierbar und

$$f'(x)=\lim_{n\to\infty}f_n'(x).$$

*Beweis.* Nach dem Hauptsatz ist $f_n(x)=f_n(a)+\int_a^x f_n'(y)\,dy$. Mit der Dreiecksungleichung und der Monotonie des
Integrals folgt

$$\sup_{x\in[a,b]}|f_n(x)-f_m(x)|\le|f_n(a)-f_m(a)|+\int_a^b|f_n'(y)-f_m'(y)|\,dy,$$

und die rechte Seite geht wegen der punktweisen Konvergenz der $f_n(a)$ und der gleichmäßigen Konvergenz der $f_n'$
(mit Satz 6.6) für $m,n\to\infty$ gegen null — also konvergiert $f_n$ sogar **gleichmäßig** gegen $f$. Der
Grenzübergang in der Hauptsatz-Formel liefert $f(x)=f(a)+\int_a^x f^*(y)\,dy$, wobei $f^*$ der (nach Satz 6.4 stetige)
gleichmäßige Limes der $f_n'$ ist. Nach dem **ersten Hauptsatz** ist $f$ stetig differenzierbar mit $f'=f^*=\lim_n f_n'$.
$\square$

**Warum die Zusatzbedingung?** Das Gegenbeispiel aus dem letzten Artikel: $f_n(x)=\frac{\sin(nx)}{n}\to0$ **gleichmäßig**,
aber $f_n'(x)=\cos(nx)$ konvergiert **nirgends** (außer in Einzelpunkten). Hier ist zwar $(\lim f_n)'=0$, aber $\lim
f_n'$ existiert nicht — die Vertauschung $\frac{d}{dx}\lim=\lim\frac{d}{dx}$ ist unmöglich. Genau diese Falle schließt
die Forderung „$f_n'$ gleichmäßig konvergent" aus.

**Stolperstein:** (1) Für **Stetigkeit und Integration** genügt $f_n\to f$ gleichmäßig; für **Differentiation** braucht
man die gleichmäßige Konvergenz der **Ableitungen** (die der $f_n$ selbst darf dann sogar nur punktweise sein). (2) Die
Sätze geben **hinreichende**, nicht notwendige Bedingungen — manchmal vertauscht es auch ohne (etwa $\int_0^1 x^n\,dx=
\frac1{n+1}\to0=\int_0^1 0\,dx$ trotz fehlender Gleichmäßigkeit). (3) Punktweise Konvergenz allein garantiert **keine**
dieser Vertauschungen (Wanderhöcker).

:::kern
__Gleichmäßige Konvergenz erlaubt das Vertauschen von Grenzprozessen.__ **Stetigkeit** (Satz 6.4): $f_n$ stetig,
$f_n\to f$ gleichmäßig ⇒ $f$ stetig ($\varepsilon/3$-Beweis). **Integration** (Satz 6.6): dann $\lim_n\int_a^b f_n\,dx=
\int_a^b f\,dx$, denn $|\int f-\int f_n|\le(b-a)\|f-f_n\|_\infty\to0$. **Komplex** (Bem 6.7): Integral/Ableitung
komponentenweise $u+iv$. **Differentiation** (Satz 6.8): $f_n$ stetig diff, $f_n\to f$ **punktweise** UND $f_n'$
**gleichmäßig** ⇒ $f$ stetig diff mit $f'=\lim_n f_n'$ (Beweis über $f_n(x)=f_n(a)+\int_a^x f_n'$ + Hauptsatz). Bei der
Ableitung reicht gleichmäßige Konvergenz der $f_n$ **nicht** ($\frac{\sin nx}{n}\to0$ glm., aber $\cos(nx)$ divergiert).
Gegenbeispiel ohne Gleichmäßigkeit: Wanderhöcker $g_n$, $\int g_n=1\neq0$.
:::

Diese Vertauschungssätze gelten gleich für **Reihen**, wenn man sie auf die Partialsummen anwendet. Der nächste Artikel
überträgt die Konvergenzbegriffe auf __Funktionenreihen__ und liefert mit dem __Weierstraßschen M-Test__ ein handliches
Kriterium für gleichmäßige Konvergenz.
