---
title: Uneigentliche Parameterintegrale und das Majorantenkriterium
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020200
summary: Von Grund auf – warum die bequemen Sätze für Parameterintegrale auf unendlichen Intervallen versagen können (ein Integral bis $\infty$ kann unstetig sein, obwohl es überall konvergiert) und wie das Majorantenkriterium sie rettet: eine parameterunabhängige, integrierbare Majorante $|f(x,t)|\le g(t)$ erzwingt gleichmäßige Konvergenz und damit Stetigkeit und Ableiten unter dem Integral – die Grundlage für Gamma-Funktion, Fourier- und Laplace-Transformation.
tags: uneigentliches Parameterintegral, gleichmäßige Konvergenz, Majorantenkriterium, Gamma-Funktion, Laplace-Transformation, Fourier-Transformation, Lokalisierung
---

## Anschaulich

Im vorigen Artikel ruhte alles auf der **Kompaktheit** des Intervalls $[a,b]$ — sie lieferte gleichmäßige
Stetigkeit und erlaubte das Ableiten unter dem Integral.

Läuft das Integral aber bis $\infty$, fällt diese Grundlage weg. Dann kann Erstaunliches passieren: Ein
uneigentliches Parameterintegral kann für **jeden** Parameterwert konvergieren und die Ergebnisfunktion trotzdem
**unstetig** sein — sie springt.

Der Ausweg ist eine zusätzliche Bedingung: eine **vom Parameter unabhängige, integrierbare Majorante**, die den
Integranden für alle Parameter gleichzeitig „deckelt". Sie erzwingt *gleichmäßige* Konvergenz und bringt
Stetigkeit und Ableitbarkeit zurück.

Dieses __Majorantenkriterium__ ist das Arbeitspferd hinter fast allen durch Integrale definierten Funktionen:
Gamma-Funktion, Fourier- und Laplace-Transformation.

:::grafik
Szene: hoema3/integralrechnung-rn/02-sprung-und-deckel · Vorlage: unstetig-vs-majorante-2d
Links die Grenzfunktion von $F(x)=\int_0^\infty\frac{\sin(tx)}{t}\,dt$ mit dem Sprung bei $x=0$ ($-\pi/2\to0\to+\pi/2$),
obwohl der Integrand glatt ist und das Integral überall konvergiert. Rechts die Rettung: eine „Deckel"-Funktion
$g(t)$, die $|f(x,t)|$ für ALLE $x$ gleichzeitig nach oben begrenzt und selbst integrierbar ist — mit ihr kehrt
die Stetigkeit zurück. (Rot = Grenzfunktion/Sprung, orange = Majorante $g$, blau = Integrand-Schar.)
:::

## Das Problem: Konvergenz allein genügt nicht

Betrachten wir $F(x)=\int_a^\infty f(x,t)\,dt$ mit stetigem Integranden. Die angenehmen Sätze aus dem vorigen
Artikel gelten hier **im Allgemeinen nicht** — selbst wenn das Integral für jedes $x$ konvergiert.

**Das klassische Gegenbeispiel.** Für $f(x,t)=\dfrac{\sin(tx)}{t}$ (stetig ergänzt durch $f(x,0)=x$) ist mit
$\int_0^\infty\frac{\sin t}{t}\,dt=\frac{\pi}{2}$ und einer Substitution

$$F(x) = \int_0^\infty \frac{\sin(tx)}{t}\,dt = \begin{cases} +\pi/2, & x>0,\\ \ \ 0, & x=0,\\ -\pi/2, & x<0.\end{cases}$$

Das Integral konvergiert für **jedes** $x$, aber $F$ ist bei $x=0$ **unstetig**.

Woran liegt's? Das Integral konvergiert nicht **absolut**, und für $x\to0$ wird die Konvergenz immer **langsamer**:
Man muss die obere Grenze immer weiter hinausschieben, um nahe am Grenzwert zu sein. Die Konvergenz ist **nicht
gleichmäßig** in $x$ — und genau das zerstört die Stetigkeit.

:::grafik
Szene: hoema3/integralrechnung-rn/02-nicht-gleichmaessig · Vorlage: teilintegrale-konvergenz-2d
Oben die Grenzfunktion $F(x)$ mit dem Sprung bei $x=0$. Unten eine Folge von Teilintegralen $\int_0^T$ für
wachsendes $T$: Für $x$ fern von 0 nähern sie sich schnell dem Plateau, für $x$ nahe 0 „hinken" sie hinterher —
Bild der nicht gleichmäßigen Konvergenz. (Rot = Grenzfunktion, orange = Teilintegrale, grau = Achsen.)
:::

## Das Majorantenkriterium

Die Rettung ist eine Bedingung, die **gleichmäßige** Konvergenz erzwingt: eine integrierbare Schranke, die
**nicht vom Parameter abhängt**. Sei $U\subseteq\mathbb{R}^n$ offen und $f:U\times(a,b)\to\mathbb{R}$ stetig (mit
$-\infty\le a<b\le\infty$).

:::formel Satz
$$|f(x,t)| \le g(t)\ \ \text{für alle } x\in U, \quad \int_a^b g(t)\,dt < \infty \qquad\Longrightarrow\qquad F(x)=\int_a^b f(x,t)\,dt\ \text{ist stetig.}$$
:::

Dabei ist $g:(a,b)\to\mathbb{R}$ die __Majorante__ — eine einzige Funktion **ohne** $x$-Abhängigkeit, die alle
$|f(x,t)|$ gemeinsam nach oben begrenzt und selbst integrierbar ist.

Ist $f$ zusätzlich stetig differenzierbar und gibt es integrierbare Majoranten
$\big|\frac{\partial f}{\partial x_k}(x,t)\big|\le G_k(t)$ mit $\int_a^b G_k<\infty$, so ist $F$ stetig
differenzierbar, und Ableitung und Integral dürfen **vertauscht** werden,
$\frac{\partial F}{\partial x_k}=\int_a^b\frac{\partial f}{\partial x_k}\,dt$.

:::herleitung
Der entscheidende Punkt ist der „ferne Rest" des Integrals. Mit der Majorante schätzt man ihn ab:

$$\left|\int_T^b f(x,t)\,dt\right| \le \int_T^b |f(x,t)|\,dt \le \int_T^b g(t)\,dt.$$

Die rechte Seite hängt **nicht** von $x$ ab und wird für $T\to b$ klein (weil $\int_a^b g<\infty$). Also schrumpft
der Rest für **alle** $x$ gleichzeitig — die Konvergenz ist gleichmäßig. Damit überträgt sich der Satz aus dem
endlichen Fall (Grenzwert und Integral vertauschen), und $F$ ist stetig bzw. differenzierbar. Hinge $g$ von $x$ ab,
wäre nichts gewonnen.
:::

**Lokalisierung.** Oft findet man **keine** Majorante auf ganz $U$, wohl aber nahe jedes Punktes. Da Stetigkeit
und Differenzierbarkeit **lokale** Eigenschaften sind, genügt das: Reicht zu jedem $x_0\in U$ eine Umgebung mit
dort gültiger Majorante, so folgt die Aussage auf ganz $U$.

:::grafik
Szene: hoema3/integralrechnung-rn/02-majorante-deckel · Vorlage: kurvenschar-unter-deckel-2d
Der Integrand $|f(x,t)|$ als Kurvenschar (verschiedene $x$), alle unter einer gemeinsamen Deckel-Kurve $g(t)$ mit
endlicher Fläche. Ein Pfeil zeigt, wie der „Schwanz" rechts von $T$ für alle $x$ gleichzeitig unter der kleinen
Restfläche von $g$ verschwindet → gleichmäßige Konvergenz. (Blau = Integrand-Schar, orange = Majorante, grau = $T$.)
:::

## Anwendungen: Gamma, Laplace, Fourier

Das Kriterium macht die wichtigsten „Integralfunktionen" der Analysis handhabbar.

**Gamma-Funktion.** Sie ist auf $(0,\infty)$ definiert durch

:::formel Definition
$$\Gamma(x) := \int_0^\infty e^{-y}\,y^{x-1}\,dy.$$
:::

Auf jedem kompakten $x$-Bereich in $(0,\infty)$ findet man integrierbare Majoranten für $e^{-y}y^{x-1}$ und seine
$x$-Ableitung $e^{-y}y^{x-1}\ln y$. Daher ist $\Gamma$ stetig differenzierbar, und man darf unter dem Integral
ableiten:

$$\Gamma'(x) = \int_0^\infty e^{-y}\,y^{x-1}\,\ln y\,\,dy.$$

**Laplace-Transformation.** Für stetiges $f:[0,\infty)\to\mathbb{R}$ mit höchstens polynomialem Wachstum ist

$$F(x) = (\mathcal{L}f)(x) = \int_0^\infty f(t)\,e^{-xt}\,dt$$

auf $(0,\infty)$ beliebig oft differenzierbar, mit $F^{(k)}(x)=\int_0^\infty(-t)^k f(t)\,e^{-xt}\,dt$.

:::herleitung
Der Dämpfer $e^{-xt}$ sorgt nur für $x>0$ für Integrierbarkeit; nahe $x=0$ gibt es keine Majorante auf ganz
$(0,\infty)$. Also arbeitet man **lokal**: Für $x\ge x_0/2$ ist

$$|f(t)\,e^{-xt}| \le c\,e^{-x_0 t/4} =: g(t),$$

und dieses $g$ ist integrierbar. Mit der Lokalisierung folgt die Glätte auf ganz $(0,\infty)$; die Faktoren
$(-t)^k$ der höheren Ableitungen werden durch dasselbe Argument beherrscht.
:::

**Fourier-Transformation.** $\hat f(\xi)=\frac{1}{\sqrt{2\pi}}\int_\mathbb{R} f(x)\,e^{-i\xi x}\,dx$ ist für
absolut integrierbares $f$ stetig und beschränkt. Ist zusätzlich $x^\ell f(x)$ absolut integrierbar, so ist
$\hat f$ entsprechend oft differenzierbar — jede Ableitung „holt" einen Faktor $-ix$ ins Integral. Das ist der
Grund für die Faustregel **„schneller Abfall im Ortsraum ⟺ Glätte im Frequenzraum"**.

:::grafik
Szene: hoema3/integralrechnung-rn/02-anwendungen · Vorlage: gamma-laplace-fourier-kacheln
Drei Mini-Kacheln: Gamma-Funktion $\Gamma(x)$ als glatte Kurve auf $(0,\infty)$; Laplace-Transformation als Block
$f(t)\mapsto F(x)$ mit dem Dämpfer $e^{-xt}$; Fourier als Ortsraum↔Frequenzraum-Paar. Gemeinsame Beschriftung
„alle wohldefiniert & glatt dank Majorantenkriterium". (Rot = Ergebnisfunktion, blau = Eingabe, grau = Achsen.)
:::

## Bedeutung und Ausblick

Das Majorantenkriterium ist der Grund, warum man mit Gamma-Funktion, Laplace- und Fourier-Transformation
überhaupt rechnen darf wie mit „normalen" Funktionen — es sichert Stetigkeit und das Ableiten unter dem Integral
trotz unendlichem Bereich.

Bisher integrierten wir über **ein** Intervall (mit einem Parameter). Jetzt gehen wir zu echten
**mehrdimensionalen** Integralen über: Wie integriert man über einen Quader im $\mathbb{R}^n$, und darf man die
Integrationen nacheinander in beliebiger Reihenfolge ausführen? Das beantwortet der __Satz von Fubini__ im
nächsten Artikel.

:::kern
- Auf unendlichen Intervallen versagen die Sätze aus §2.1 im Allgemeinen: $F(x)=\int_a^\infty f(x,t)\,dt$ kann überall konvergieren und doch **unstetig** sein (klassisch $\int_0^\infty\frac{\sin(tx)}{t}\,dt=\tfrac{\pi}{2}\operatorname{sgn}x$, Sprung bei $0$ — Konvergenz nicht gleichmäßig).
- Das __Majorantenkriterium__ rettet die Lage: eine **parameterunabhängige**, integrierbare __Majorante__ $|f(x,t)|\le g(t)$, $\int g<\infty$, macht $F$ stetig.
- Mechanismus: der ferne Rest wird durch $\int_T^b g$ abgeschätzt, unabhängig von $x$ → gleichmäßige Konvergenz.
- Mit Majoranten $|\partial f/\partial x_k|\le G_k$ ist $F$ auch stetig differenzierbar (Ableitung/Integral vertauschbar). Weil die Eigenschaften **lokal** sind, genügt eine Majorante je Umgebung (__Lokalisierung__).
- Anwendungen: __Gamma-Funktion__ $\Gamma(x)=\int_0^\infty e^{-y}y^{x-1}dy$ ($\Gamma'=\int e^{-y}y^{x-1}\ln y\,dy$), __Laplace-__ (lokale Majorante $e^{-x_0t/4}$) und __Fourier-Transformation__.
:::

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
