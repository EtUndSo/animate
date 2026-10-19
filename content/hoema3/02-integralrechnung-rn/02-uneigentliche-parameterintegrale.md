---
title: Uneigentliche Parameterintegrale und das Majorantenkriterium
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020200
summary: Von Grund auf – warum die bequemen Sätze für Parameterintegrale auf unendlichen Intervallen versagen können (ein Integral bis $\infty$ kann unstetig sein, obwohl es überall konvergiert) und wie das Majorantenkriterium sie rettet: eine vom Parameter unabhängige, integrierbare Majorante $|f(x,t)|\le g(t)$ erzwingt gleichmäßige Konvergenz und damit Stetigkeit und Ableiten unter dem Integral – die Grundlage für Gamma-Funktion, Fourier- und Laplace-Transformation.
tags: uneigentliches Parameterintegral, gleichmäßige Konvergenz, Majorantenkriterium, Gamma-Funktion, Laplace-Transformation, Fourier-Transformation, Lokalisierung
---

:::grafik
Einstiegs-Animation: Ein Parameterintegral mit **unendlicher** oberer Grenze, $F(x)=\int_0^\infty f(x,t)\,dt$. Für
das Beispiel $f(x,t)=\frac{\sin(tx)}{t}$ wird gezeigt, wie der Integralwert für $x>0$ konstant $\pi/2$, für $x<0$
konstant $-\pi/2$ und bei $x=0$ null ist — die Grenzfunktion macht bei $x=0$ einen **Sprung**, obwohl der
Integrand überall glatt ist und das Integral überall konvergiert. Daneben die Rettung: eine „Deckel"-Funktion
$g(t)$, die $|f(x,t)|$ für **alle** $x$ gleichzeitig nach oben begrenzt und selbst integrierbar ist — mit ihr
kehrt die Stetigkeit zurück. Kernbotschaft: Auf unendlichen Intervallen braucht man eine parameterunabhängige
Majorante.
:::

:::konzept
Im vorigen Artikel ruhte alles auf der **Kompaktheit** des Intervalls $[a,b]$ — sie lieferte gleichmäßige
Stetigkeit und erlaubte das Ableiten unter dem Integral. Läuft das Integral aber bis $\infty$ (oder hat der
Integrand eine Singularität), fällt diese Grundlage weg. Dann kann Erstaunliches passieren: Ein uneigentliches
Parameterintegral kann für **jeden** Parameterwert konvergieren und die Ergebnisfunktion trotzdem **unstetig**
sein. Der Ausweg ist eine zusätzliche Bedingung — eine **vom Parameter unabhängige, integrierbare Majorante** —,
die *gleichmäßige* Konvergenz sichert. Dieses __Majorantenkriterium__ ist das Arbeitspferd hinter fast allen durch
Integrale definierten Funktionen: Gamma-Funktion, Fourier- und Laplace-Transformation.
:::

**Worum es geht:** Wir sehen am Gegenbeispiel, *warum* uneigentliche Parameterintegrale nicht brav sind,
formulieren das __Majorantenkriterium__ (Stetigkeit und Ableiten unter dem Integral), die __Lokalisierung__ und
die wichtigen Anwendungen.

## Das Problem: Konvergenz allein genügt nicht

Betrachten wir ein uneigentliches Parameterintegral $F(x)=\int_a^\infty f(x,t)\,dt$ mit stetigem Integranden. Die
angenehmen Sätze aus dem vorigen Artikel (Stetigkeit, Ableiten unter dem Integral) gelten hier **im Allgemeinen
nicht** — selbst wenn das Integral für jedes $x$ konvergiert.

**Das klassische Gegenbeispiel.** Für $f(x,t)=\dfrac{\sin(tx)}{t}$ (stetig ergänzt durch $f(x,0)=x$) ist mit der
bekannten Formel $\int_0^\infty \frac{\sin t}{t}\,dt = \frac{\pi}{2}$ und einer Substitution

$$F(x) = \int_0^\infty \frac{\sin(tx)}{t}\,dt = \begin{cases} \ \ \pi/2, & x>0,\\ \ \ 0, & x=0,\\ -\pi/2, & x<0.\end{cases}$$

Das Integral konvergiert für **jedes** $x$, aber $F$ ist bei $x=0$ **unstetig** — es springt. Woran liegt's? Das
Integral konvergiert nicht **absolut**, und für $x\to 0$ wird die Konvergenz immer **langsamer**: Man muss die
obere Grenze immer weiter hinausschieben, um nahe am Grenzwert zu sein. Die Konvergenz ist **nicht gleichmäßig**
in $x$ — und genau das zerstört die Stetigkeit.

:::grafik
Oben die Grenzfunktion $F(x)$ mit dem Sprung bei $x=0$ ($-\pi/2 \to 0 \to +\pi/2$). Unten eine Folge von
Teilintegralen $\int_0^T$ für wachsendes $T$: Für $x$ fern von 0 nähern sie sich schnell dem Plateau, für $x$ nahe
0 „hinken" sie hinterher — Bild der *nicht gleichmäßigen* Konvergenz.
:::

## Das Majorantenkriterium

Die Rettung ist eine Bedingung, die **gleichmäßige** Konvergenz erzwingt: eine integrierbare Schranke, die
**nicht vom Parameter abhängt**. Sei $U\subset\mathbb{R}^n$ offen und $f:U\times(a,b)\to\mathbb{R}$ stetig (mit
$-\infty\le a<b\le\infty$).

- **Stetigkeit:** Gibt es eine uneigentlich integrierbare __Majorante__ $g:(a,b)\to\mathbb{R}$ mit

$$|f(x,t)| \le g(t) \quad\text{für alle } x\in U, \qquad \int_a^b g(t)\,dt < \infty,$$

  so ist $F(x)=\int_a^b f(x,t)\,dt$ **stetig** auf $U$.
- **Ableiten unter dem Integral:** Ist $f$ zusätzlich stetig differenzierbar und gibt es für jede Ableitung
  integrierbare Majoranten $\big|\frac{\partial f}{\partial x_k}(x,t)\big| \le G_k(t)$ mit $\int_a^b G_k < \infty$,
  so ist $F$ stetig differenzierbar, und Ableitung und Integral dürfen **vertauscht** werden:
  $\frac{\partial F}{\partial x_k}(x)=\int_a^b \frac{\partial f}{\partial x_k}(x,t)\,dt$.

**Der Kern:** Die Majorante „deckelt" den Integranden für alle $x$ **gleichzeitig**. Dadurch wird der
unendlich ferne „Rest" $\int_T^b$ gleichmäßig in $x$ klein — die Konvergenz ist gleichmäßig, und die Sätze aus
dem endlichen Fall übertragen sich. Entscheidend ist, dass $g$ **nicht** von $x$ abhängt (sonst wäre nichts
gewonnen).

:::grafik
Der Integrand $|f(x,t)|$ als Kurvenschar (verschiedene $x$), alle unter einer gemeinsamen Deckel-Kurve $g(t)$ mit
endlicher Fläche. Ein Pfeil zeigt, wie der „Schwanz" rechts von $T$ für alle $x$ gleichzeitig unter der kleinen
Restfläche von $g$ verschwindet → gleichmäßige Konvergenz. Daneben die Folgerung
$\frac{\partial}{\partial x}\int=\int\frac{\partial}{\partial x}$.
:::

**Lokalisierung.** Oft findet man **keine** Majorante auf ganz $U$, wohl aber in der Nähe jedes Punktes. Da
Stetigkeit und Differenzierbarkeit **lokale** Eigenschaften sind, genügt das: Reicht es, zu jedem $x_0\in U$ eine
offene Umgebung $V(x_0)\subset U$ mit einer dort gültigen Majorante zu finden, so folgt die Aussage auf ganz $U$.

## Anwendungen: Gamma, Laplace, Fourier

Das Kriterium macht die wichtigsten „Integralfunktionen" der Analysis handhabbar.

**Gamma-Funktion.** $\displaystyle \Gamma(x) := \int_0^\infty e^{-y}\,y^{x-1}\,dy$ ist auf $(0,\infty)$ stetig
differenzierbar, und man darf unter dem Integral ableiten:

$$\Gamma'(x) = \int_0^\infty e^{-y}\,y^{x-1}\,\ln y\,\,dy.$$

**Laplace-Transformation.** Für stetiges $f:[0,\infty)\to\mathbb{R}$ mit höchstens polynomialem Wachstum ist

$$F(x) = (\mathcal{L}f)(x) = \int_0^\infty f(t)\,e^{-xt}\,dt$$

auf $(0,\infty)$ beliebig oft differenzierbar, mit $F^{(k)}(x)=\int_0^\infty (-t)^k f(t)\,e^{-xt}\,dt$. Die
Majorante baut man lokal: Für $x\ge x_0/2$ ist $|f(t)e^{-xt}|\le c\,e^{-x_0 t/4}=:g(t)$ integrierbar — mit der
Lokalisierung folgt die Glätte auf ganz $(0,\infty)$.

**Fourier-Transformation.** $\hat f(\xi)=\frac{1}{\sqrt{2\pi}}\int_\mathbb{R} f(x)\,e^{-i\xi x}\,dx$ ist für
absolut integrierbares $f$ stetig und beschränkt; ist zusätzlich $x^\ell f(x)$ absolut integrierbar, so ist
$\hat f$ entsprechend oft differenzierbar (die Ableitung „holt" jeweils einen Faktor $-ix$ ins Integral). Das ist
der Grund für die Faustregel „schneller Abfall im Ortsraum ⟺ Glätte im Frequenzraum".

:::grafik
Drei Mini-Kacheln: Gamma-Funktion $\Gamma(x)$ als glatte Kurve auf $(0,\infty)$; Laplace-Transformation als
Block $f(t)\mapsto F(x)$ mit dem „Dämpfer" $e^{-xt}$; Fourier als Ortsraum↔Frequenzraum-Paar. Gemeinsame
Beschriftung „alle wohldefiniert & glatt dank Majorantenkriterium".
:::

:::kern
Auf unendlichen Intervallen versagen die Sätze aus §2.1 im Allgemeinen: Ein uneigentliches Parameterintegral
$F(x)=\int_a^\infty f(x,t)\,dt$ kann überall konvergieren und doch **unstetig** sein (klassisch
$\int_0^\infty\frac{\sin(tx)}{t}\,dt=\tfrac{\pi}{2}\operatorname{sgn}x$, Sprung bei $0$ — Konvergenz nicht
gleichmäßig). Das __Majorantenkriterium__ rettet die Lage: Gibt es eine **parameterunabhängige**, integrierbare
__Majorante__ $|f(x,t)|\le g(t)$, $\int g<\infty$, so ist $F$ stetig; mit Majoranten $|\partial f/\partial x_k|\le
G_k$ auch stetig differenzierbar und Ableitung/Integral vertauschbar. Weil Stetigkeit/Differenzierbarkeit
**lokal** sind, genügt eine Majorante je Umgebung (__Lokalisierung__). Anwendungen: __Gamma-Funktion__
$\Gamma(x)=\int_0^\infty e^{-y}y^{x-1}dy$ ($\Gamma'=\int e^{-y}y^{x-1}\ln y\,dy$), __Laplace-__ und
__Fourier-Transformation__ sind damit wohldefiniert und glatt.
:::

Bisher integrierten wir über **ein** Intervall (mit einem Parameter). Jetzt gehen wir zu echten
**mehrdimensionalen** Integralen über: Wie integriert man eine Funktion über einen Quader im $\mathbb{R}^n$, und
darf man die Integrationen nacheinander in beliebiger Reihenfolge ausführen? Das beantwortet der __Satz von
Fubini__ im nächsten Artikel.

:::quiz
F: Warum versagen die bequemen Sätze aus §2.1 (Stetigkeit, Ableiten unter dem Integral) auf einem unendlichen Intervall?
A: Ihr Beweis beruhte auf der **Kompaktheit** von $[a,b]$, die gleichmäßige Stetigkeit lieferte. Auf $(a,\infty)$ fehlt diese Kompaktheit, also auch die gleichmäßige Kontrolle über den fernen Teil des Integrals — die Vertauschung von Grenzwert und Integral ist dann nicht mehr garantiert.
F: Beim Beispiel $\int_0^\infty\frac{\sin(tx)}{t}\,dt$: Wie kann $F$ bei $x=0$ springen, obwohl das Integral für jedes $x$ konvergiert?
A: Das Integral konvergiert nur **bedingt** (nicht absolut), und nahe $x=0$ wird die Konvergenz immer langsamer — man muss die obere Grenze immer weiter hinausschieben. Die Konvergenz ist also **nicht gleichmäßig** in $x$, und genau das erlaubt den Sprung von $-\pi/2$ über $0$ auf $+\pi/2$.
F: Was heißt „gleichmäßige Konvergenz in $x$" bei einem uneigentlichen Parameterintegral anschaulich?
A: Dass der ferne Rest $\int_T^\infty f(x,t)\,dt$ für **alle** $x$ gleichzeitig klein wird, sobald $T$ groß genug ist — mit einem von $x$ unabhängigen Maß. Kein Parameterwert darf „hinterherhinken" wie bei $x\to0$ oben.
F: Was besagt das Majorantenkriterium, und warum muss die Majorante vom Parameter unabhängig sein?
A: Gibt es ein integrierbares $g(t)$ mit $|f(x,t)|\le g(t)$ für **alle** $x$ und $\int g<\infty$, so ist $F$ stetig. Entscheidend ist die $x$-Unabhängigkeit: nur dann deckelt $g$ den Rest für alle Parameter zugleich — eine $x$-abhängige Schranke brächte keine gleichmäßige Kontrolle.
F: Durch welchen Mechanismus erzwingt die Majorante die gleichmäßige Konvergenz?
A: Der Schwanz wird abgeschätzt durch $\big|\int_T^\infty f(x,t)\,dt\big|\le\int_T^\infty g(t)\,dt$. Die rechte Seite hängt **nicht** von $x$ ab und wird für große $T$ klein — also schrumpft der Rest für alle $x$ gleichmäßig.
F: Welche Zusatzbedingung erlaubt das Ableiten unter dem uneigentlichen Integral?
A: Man braucht integrierbare Majoranten für die **Ableitungen**: $|\partial f/\partial x_k(x,t)|\le G_k(t)$ mit $\int G_k<\infty$. Dann ist $F$ stetig differenzierbar und $\partial_{x_k}F=\int\partial_{x_k}f\,dt$.
F: Was besagt die Lokalisierung, und warum genügt eine Majorante nur je Umgebung?
A: Stetigkeit und Differenzierbarkeit sind **lokale** Eigenschaften — sie hängen nur vom Verhalten in einer kleinen Umgebung jedes Punktes ab. Findet man zu jedem $x_0$ eine Umgebung mit gültiger Majorante, folgt die Aussage auf ganz $U$; eine globale Majorante ist unnötig.
F: Warum braucht die Laplace-Transformation $\int_0^\infty f(t)e^{-xt}\,dt$ gerade die Lokalisierung?
A: Der Dämpfer $e^{-xt}$ sorgt nur für $x>0$ für Integrierbarkeit; nahe $x=0$ gibt es keine integrierbare Schranke auf ganz $(0,\infty)$. Für $x\ge x_0/2$ aber gilt lokal $|f(t)e^{-xt}|\le c\,e^{-x_0 t/4}$ — mit Lokalisierung folgt die Glätte auf dem ganzen Bereich.
F: Warum darf man die Gamma-Funktion unter dem Integral ableiten, und wie lautet $\Gamma'(x)$?
A: Auf jedem kompakten $x$-Bereich in $(0,\infty)$ findet man integrierbare Majoranten für $e^{-y}y^{x-1}$ und seine $x$-Ableitung $e^{-y}y^{x-1}\ln y$. Also $\Gamma'(x)=\int_0^\infty e^{-y}y^{x-1}\ln y\,dy$.
F: Warum gilt die Faustregel „schneller Abfall im Ortsraum ⟺ Glätte im Frequenzraum" bei der Fourier-Transformation?
A: Jede Ableitung von $\hat f$ nach $\xi$ „holt" einen Faktor $-ix$ in das Integral. Ist $x^\ell f(x)$ absolut integrierbar (also fällt $f$ schnell genug ab), liefert die Majorante die $\ell$-fache Differenzierbarkeit von $\hat f$ — mehr Abfall im Ortsraum bedeutet mehr Glätte im Frequenzraum.
:::
