---
title: Uneigentliche Parameterintegrale und das Majorantenkriterium
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020200
summary: Von Grund auf – warum die bequemen Sätze für Parameterintegrale versagen können, wenn die Kurve bis ins Unendliche reicht (ein Integral kann für jeden Parameter konvergieren und trotzdem springen), und wie ein Deckel sie rettet: eine vom Parameter unabhängige, integrierbare Majorante $\lvert f(\vec x,t)\rvert\le m(t)$ kontrolliert alle Schwänze zugleich und liefert Stetigkeit und Ableiten unter dem Integral – lokal genügt. Mit Beweisen und einer Beispiel-Seite zu Gamma-Funktion, Laplace- und Fourier-Transformation.
tags: uneigentliches Parameterintegral, gleichmäßige Konvergenz, Majorantenkriterium, Gamma-Funktion, Laplace-Transformation, Fourier-Transformation, Lokalisierung
---

## Anschaulich

Im vorigen Artikel lag über einem **festen** Intervall $[a,b]$ eine Kurve, die ein Schieberegler verformt, und die
Fläche darunter war das Parameterintegral. Alles ruhte darauf, dass das Intervall endlich und abgeschlossen ist: Die
ganze Kurve bewegte sich gleichmäßig mit dem Regler.

Jetzt reicht die Kurve **bis ins Unendliche** — oder sie schießt an einem Rand in die Höhe. Die Fläche ist dann ein
Grenzwert: die Fläche bis zu einer Stelle $T$, und $T$ läuft immer weiter hinaus. Der Rest jenseits von $T$, der
__Schwanz__, muss dabei verschwinden.

Hier lauert eine Gefahr. Für manche Reglerstellungen schrumpft der Schwanz nur quälend langsam. Dann kann die Fläche als
Funktion des Reglers **springen** — obwohl sie für jede einzelne Stellung wohldefiniert ist.

**Die Rettung ist ein Deckel:** eine feste Kurve $m(t)$, die über allen Kurven liegt, egal wie der Regler steht, und die
selbst eine endliche Fläche hat. Ihr Schwanz begrenzt alle Schwänze gleichzeitig. Mit diesem __Majorantenkriterium__
kehren Stetigkeit und Ableiten unter dem Integral zurück — es ist das Arbeitspferd hinter Gamma-Funktion, Laplace- und
Fourier-Transformation.

:::grafik
Szene: hoema3/integralrechnung-rn/02-sprung-und-deckel · Vorlage: unstetig-vs-majorante-2d
Links die Kurvenschar $t\mapsto\frac{\sin(tx)}{t}$ für Reglerstellungen nahe $x=0$: Je kleiner $x$, desto langsamer
schwingt die Kurve, und ihre Fläche liegt fast ganz im Schwanz. Darunter die Fläche als Funktion von $x$ mit dem Sprung
von $-\pi/2$ auf $+\pi/2$. Rechts die Rettung: eine Kurvenschar unter einem gemeinsamen Deckel $m(t)$ mit endlicher
Fläche; der Schwanz jenseits von $T$ ist für alle Reglerstellungen zugleich kleiner als der Schwanz des Deckels.
Kernaussage: Ein gemeinsamer Deckel zähmt alle Schwänze auf einmal. (Blau = Kurven, orange = Deckel $m$, rot = Fläche bzw.
Sprung, grau = Grenze $T$.)
:::

## Was ist ein uneigentliches Parameterintegral?

**Die Akteure:** eine offene Menge $U\subseteq\mathbb{R}^n$ für den Parameter, ein offenes Intervall $(a,b)$ mit
$-\infty\le a<b\le\infty$ und eine stetige Funktion

$$f:U\times(a,b)\to\mathbb{R}, \qquad (\vec x,t)\mapsto f(\vec x,t).$$

Für eine feste Reglerstellung $\vec x$ ist das __uneigentliche Integral__ der Grenzwert der Flächen über immer
größeren abgeschlossenen Teilintervallen, falls er existiert:

$$\int_a^b f(\vec x,t)\,dt := \lim_{\alpha\to a,\ \beta\to b}\ \int_\alpha^\beta f(\vec x,t)\,dt.$$

Existiert er für jedes $\vec x\in U$, entsteht wieder ein Parameterintegral, eine skalare Funktion des Parameters:

:::formel Definition
$$g(\vec x) := \int_a^b f(\vec x,t)\,dt, \qquad \vec x\in U.$$
:::

**Im Bild:** Man misst die Fläche zwischen zwei Grenzen $\alpha$ und $\beta$ und schiebt sie nach außen, bis zum Ende des
Intervalls. Was dann noch außerhalb liegt, sind die beiden Schwänze — sie müssen gegen null gehen.

Konvergiert sogar das Integral über $\lvert f(\vec x,\cdot)\rvert$, heißt das uneigentliche Integral __absolut
konvergent__. Dann können sich positive und negative Flächenstücke nicht gegenseitig „retten".

::::beispiel Ein einfaches uneigentliches Parameterintegral
Für den Parameter $x>0$ ist

$$g(x) = \int_0^\infty e^{-xt}\,dt = \lim_{\beta\to\infty}\Big[-\frac{e^{-xt}}{x}\Big]_{t=0}^{t=\beta} = \lim_{\beta\to\infty}\frac{1-e^{-x\beta}}{x} = \frac1x.$$

Der Schwanz jenseits von $T$ ist hier genau

$$\int_T^\infty e^{-xt}\,dt = \frac{e^{-xT}}{x}.$$

**Im Bild:** Für große $x$ fällt die Kurve steil ab, der Schwanz ist sofort winzig. Für kleine $x$ ist sie fast flach,
und der Schwanz bleibt lange groß — für $x$ gegen null wird die Fläche sogar unendlich.
::::

## Das Problem: Konvergenz allein genügt nicht

Die Sätze des vorigen Artikels gelten für uneigentliche Parameterintegrale **im Allgemeinen nicht** — selbst wenn das
Integral für jedes $\vec x$ konvergiert. Der Grund steckt im Schwanz: Für jede Reglerstellung wird er irgendwann klein,
aber nicht überall **gleich schnell**. Ein fester Abschneidepunkt $T$ reicht dann nicht für alle Stellungen zugleich.

Man sagt: Die Konvergenz ist nicht __gleichmäßig__ im Parameter. **Im Bild:** Einige Kurven „hinken hinterher" — bei
ihnen steckt auch weit draußen noch viel Fläche. Bewegt man den Regler auf solche Stellungen zu, kann die Fläche
springen.

::::beispiel Das Dirichlet-Integral springt
Mit der stetigen Fortsetzung bei $t=0$ sei

$$f(x,t) = \frac{\sin(tx)}{t} \quad (t>0), \qquad f(x,0) := x.$$

Mit dem bekannten __Dirichlet-Integral__ und der Substitution $u=tx$ für $x>0$ ergibt sich ein Sprung:

$$\int_0^\infty\frac{\sin u}{u}\,du = \frac\pi2, \qquad g(x) = \int_0^\infty\frac{\sin(tx)}{t}\,dt = \begin{cases} +\pi/2, & x>0,\\ \ \ 0, & x=0,\\ -\pi/2, & x<0. \end{cases}$$

Für $x<0$ folgt der Wert, weil der Sinus ungerade ist; für $x=0$ ist der Integrand null. Das Integral konvergiert also für
**jedes** $x$, aber $g$ springt bei $0$.

**Warum:** Der Schwanz jenseits von $T$ ist nach derselben Substitution

$$\int_T^\infty\frac{\sin(tx)}{t}\,dt = \int_{Tx}^\infty\frac{\sin u}{u}\,du \qquad (x>0).$$

Für jedes noch so große $T$ kann man $x$ so klein wählen, dass $Tx$ fast null ist — dann steckt fast die ganze Fläche
$\tfrac\pi2$ im Schwanz. Kein fester Abschneidepunkt funktioniert für alle $x$. Einen Deckel gibt es auch nicht: Die
naheliegende Schranke $1/t$ hat unendliche Fläche, das Integral ist nicht einmal absolut konvergent.

**Im Bild:** Die Kurve $\sin(tx)/t$ schwingt mit der Wellenlänge $2\pi/x$. Je kleiner $x$, desto langsamer die
Schwingung und desto weiter muss man gehen, bis sich positive und negative Bögen ausgleichen.

:::herleitung
Der Wert des Dirichlet-Integrals lässt sich selbst mit einem Parameter finden — eine Idee, die über den Stoff hinausgeht
und hier nur skizziert wird. Für $s>0$ sei

$$I(s) = \int_0^\infty e^{-st}\,\frac{\sin t}{t}\,dt.$$

Der Dämpfer liefert für $s$ ab einer festen positiven Schranke eine Majorante, man darf also unter dem Integral ableiten.
Mit der bekannten Laplace-Transformierten des Sinus:

$$I'(s) = -\int_0^\infty e^{-st}\sin t\,dt = -\frac{1}{1+s^2}.$$

Weil $I(s)$ für $s\to\infty$ gegen null geht, ist $I(s)=\tfrac\pi2-\arctan s$. Der letzte Schritt, $s$ gegen null, ist
genau ein heikler Grenzübergang ohne Majorante; man sichert ihn mit einer partiellen Integration ab. Ergebnis:
$\tfrac\pi2$.
:::

:::grafik
Szene: hoema3/integralrechnung-rn/02-nicht-gleichmaessig · Vorlage: teilintegrale-konvergenz-2d
Oben die Fläche $g(x)$ mit dem Sprung bei $x=0$. Unten die Flächen bis $T$ für wachsendes $T$: Für $x$ fern von $0$
erreichen sie schnell das Plateau $\pm\pi/2$, für $x$ nahe $0$ hinken sie hinterher. Kernaussage: Ohne gleichmäßige
Konvergenz kann die Grenzfunktion springen. (Rot = Grenzfunktion, orange = Flächen bis $T$, grau = Achsen.)
:::
::::

## Das Majorantenkriterium: ein Deckel für alle Schwänze

Die Rettung ist eine Bedingung, die gleichmäßige Kontrolle über die Schwänze erzwingt: eine integrierbare Schranke, die
**nicht vom Parameter abhängt**. Eine solche Funktion $m:(a,b)\to\mathbb{R}$ heißt __Majorante__ (im Skript $g$); für die
Ableitungen braucht man ebensolche Funktionen $m_k$ (im Skript $G_k$).

:::formel Satz
$$\lvert f(\vec x,t)\rvert\le m(t)\ \text{ auf } U\times(a,b),\ \ \int_a^b m(t)\,dt<\infty \quad\Longrightarrow\quad g \text{ ist stetig auf } U.$$

$$\Big\lvert\frac{\partial f}{\partial x_k}(\vec x,t)\Big\rvert\le m_k(t),\ \ \int_a^b m_k(t)\,dt<\infty \quad\Longrightarrow\quad \frac{\partial g}{\partial x_k}(\vec x) = \int_a^b\frac{\partial f}{\partial x_k}(\vec x,t)\,dt.$$
:::

**So liest man das:** Die erste Zeile verlangt eine einzige Deckelkurve $m$ mit endlicher Fläche, die über allen
Kurven $\lvert f(\vec x,\cdot)\rvert$ liegt — für **alle** Reglerstellungen zugleich. Dann ist das Parameterintegral
stetig, und es existiert auch überall. Die zweite Zeile verlangt zusätzlich, dass $f$ nach den Parametern stetig
differenzierbar ist und auch die Ableitungen solche Deckel haben. Dann ist $g$ stetig differenzierbar, und man darf
unter dem Integral ableiten.

**Im Bild:** Der Schwanz jeder Kurve jenseits von $T$ liegt unter dem Schwanz des Deckels — und der hängt nicht vom Regler
ab. Wird er klein, werden alle Schwänze zugleich klein.

:::herleitung
**Existenz.** Für jedes $\vec x$ konvergiert das Integral über $\lvert f(\vec x,\cdot)\rvert$ nach dem
Vergleichskriterium aus HM1, denn es liegt unter dem Integral über $m$.

**Stetigkeit.** Sei $\vec x_0\in U$ und $\varepsilon>0$. Weil die Fläche unter $m$ endlich ist, gibt es Grenzen
$a<\alpha<\beta<b$, jenseits derer der Deckel nur noch wenig Fläche hat:

$$\int_a^\alpha m(t)\,dt + \int_\beta^b m(t)\,dt < \varepsilon.$$

Für **jedes** $\vec x\in U$ sind die Schwänze dann klein, denn sie liegen unter denen des Deckels. Bezeichnet
$g_{\alpha\beta}(\vec x)$ die Fläche zwischen $\alpha$ und $\beta$, so gilt

$$\big\lvert g(\vec x)-g_{\alpha\beta}(\vec x)\big\rvert \le \int_a^\alpha\lvert f(\vec x,t)\rvert\,dt+\int_\beta^b\lvert f(\vec x,t)\rvert\,dt < \varepsilon.$$

Die mittlere Fläche $g_{\alpha\beta}$ ist ein Parameterintegral über dem **festen, abgeschlossenen** Intervall
$[\alpha,\beta]$, also nach dem vorigen Artikel stetig. Für $\vec x$ nahe genug bei $\vec x_0$ unterscheidet sie sich um
weniger als $\varepsilon$, und mit der Dreiecksungleichung folgt

$$\lvert g(\vec x)-g(\vec x_0)\rvert \le \lvert g(\vec x)-g_{\alpha\beta}(\vec x)\rvert + \lvert g_{\alpha\beta}(\vec x)-g_{\alpha\beta}(\vec x_0)\rvert + \lvert g_{\alpha\beta}(\vec x_0)-g(\vec x_0)\rvert < 3\,\varepsilon.$$

**Ableiten.** Wie im vorigen Artikel schreibt man den Differenzenquotienten mit dem Mittelwertsatz als Integral über die
Ableitung an Zwischenstellen. In den Schwänzen schätzt man ihn durch den Deckel $m_k$ ab — unabhängig vom Schritt —, auf
dem mittleren Stück $[\alpha,\beta]$ geht der Beweis des vorigen Artikels wörtlich durch. Die Stetigkeit der Ableitung
folgt aus dem ersten Teil, angewandt auf $\partial f/\partial x_k$ mit dem Deckel $m_k$.

**Im Bild:** Der Deckel schneidet das unendliche Problem in zwei Stücke: ein endliches Mittelstück, auf dem der vorige
Artikel gilt, und zwei Schwänze, die für alle Reglerstellungen zugleich vernachlässigbar sind. Hinge $m$ vom Regler ab,
wäre nichts gewonnen.
:::

**Lokal genügt.** Oft findet man keinen Deckel für den **ganzen** Parameterbereich, wohl aber für jede kleine Umgebung
eines Punktes. Das reicht: Gibt es zu jedem $\vec x_0\in U$ eine offene Umgebung $V\subseteq U$ mit einem Deckel, der auf
$V\times(a,b)$ gilt, so ist $g$ auf ganz $U$ stetig (bzw. stetig differenzierbar).

:::herleitung
Stetigkeit und Differenzierbarkeit in $\vec x_0$ hängen nur von den Werten von $g$ in einer beliebig kleinen Umgebung
von $\vec x_0$ ab. Wendet man den Satz auf die offene Menge $V$ statt auf $U$ an, erhält man beides in $\vec x_0$. Da
$\vec x_0$ beliebig war, gilt es überall.
:::

::::beispiel Ein Deckel, der nur lokal passt
Für das Parameterintegral mit dem Integranden $e^{-xt}$ auf $(0,\infty)$ gibt es **keinen** Deckel für alle $x$ zugleich: Für $x$ gegen null
nähert sich die Kurve der Konstanten $1$, und jede Schranke darüber hätte unendliche Fläche. Für alle $x\ge x_0/2$ mit
einem festen $x_0>0$ passt aber

$$e^{-xt} \le e^{-x_0t/2} =: m(t), \qquad \int_0^\infty m(t)\,dt = \frac{2}{x_0}.$$

Auch die Ableitung nach $x$ hat dort einen Deckel:

$$\Big\lvert\frac{\partial}{\partial x}\,e^{-xt}\Big\rvert = t\,e^{-xt} \le t\,e^{-x_0t/2} =: m_1(t), \qquad \int_0^\infty m_1(t)\,dt = \frac{4}{x_0^2}.$$

Lokal genügt das, also darf man unter dem Integral ableiten — passend zur direkten Rechnung:

$$g'(x) = -\int_0^\infty t\,e^{-xt}\,dt = -\frac{1}{x^2} = \frac{d}{dx}\,\frac1x.$$

Wiederholtes Ableiten liefert ebenso eine schöne Formel, bei $x=1$ die Fakultät:

$$\int_0^\infty t^k\,e^{-xt}\,dt = \frac{k!}{x^{k+1}}, \qquad \int_0^\infty t^k\,e^{-t}\,dt = k!.$$

:::herleitung
Jede weitere Ableitung holt einen Faktor $-t$ ins Integral, und $t^k e^{-x_0t/2}$ ist ein Deckel mit endlicher Fläche.
Die $k$-te Ableitung von $\frac1x$ ist $(-1)^k\,k!/x^{k+1}$; das Gleichsetzen mit $(-1)^k\int_0^\infty t^ke^{-xt}\,dt$
ergibt die Formel.
:::

**Im Bild:** Der Deckel $e^{-x_0t/2}$ liegt über allen Kurven, deren Regler mindestens auf $x_0/2$ steht. Nahe null
gibt es keinen gemeinsamen Deckel — aber für jeden einzelnen Punkt reicht ein Deckel, der zu dessen Nachbarschaft passt.
::::

:::grafik
Szene: hoema3/integralrechnung-rn/02-majorante-deckel · Vorlage: kurvenschar-unter-deckel-2d
Die Kurven $\lvert f(\vec x,t)\rvert$ für verschiedene Reglerstellungen, alle unter einer gemeinsamen Deckelkurve $m(t)$
mit endlicher Fläche. Ein Regler für $T$ zeigt, wie der Schwanz rechts von $T$ für alle Kurven zugleich unter der kleinen
Restfläche des Deckels verschwindet. Kernaussage: Ein Deckel, der nicht vom Regler abhängt, erzwingt gleichmäßige
Kontrolle. (Blau = Kurven, orange = Deckel, grau = Grenze $T$.)
:::

## Anwendungen: Gamma, Laplace, Fourier

Mit dem Kriterium werden die wichtigsten durch Integrale definierten Funktionen der Analysis handhabbar.

**Die Gamma-Funktion** ist für $x>0$ definiert durch

:::formel Definition
$$\Gamma(x) := \int_0^\infty e^{-y}\,y^{x-1}\,dy.$$
:::

Sie ist auf $(0,\infty)$ stetig differenzierbar, und man darf unter dem Integral ableiten:

$$\Gamma'(x) = \int_0^\infty e^{-y}\,y^{x-1}\,\ln y\,dy.$$

**Im Bild:** Hier ist das Integral an **beiden** Enden uneigentlich. Bei $y$ gegen null schießt die Kurve $y^{x-1}$ für
$x<1$ in die Höhe, bei $y$ gegen unendlich wird sie vom Dämpfer $e^{-y}$ gezähmt. Für jedes Ende braucht der Deckel einen
eigenen Teil.

:::herleitung
Sei $[c,d]$ mit $0<c<d$ ein Parameterbereich. Für $y\le1$ ist $y^{x-1}$ am größten, wenn der Exponent am kleinsten ist,
für $y\ge1$, wenn er am größten ist. Ein Deckel für alle $x\in[c,d]$ ist deshalb

$$m(y) = \begin{cases} y^{c-1}, & 0<y\le1,\\ e^{-y}\,y^{d-1}, & y\ge1. \end{cases}$$

Er hat endliche Fläche: Am linken Ende ist der Exponent $c-1$ größer als $-1$, am rechten dämpft $e^{-y}$ jede Potenz.
Die Ableitung nach $x$ bringt den Faktor $\ln y$; mit ihm bleibt die Fläche endlich, denn $\lvert\ln y\rvert$ wächst bei
null langsamer als jede Potenz $y^{-c/2}$ und bei unendlich langsamer als jede Potenz von $y$. Jeder Punkt aus
$(0,\infty)$ liegt im Inneren eines solchen Bereichs — lokal genügt.
:::

::::beispiel Die Gamma-Funktion setzt die Fakultät fort
Partielle Integration verschiebt den Parameter um eins:

$$\Gamma(x+1) = \int_0^\infty e^{-y}\,y^{x}\,dy = \Big[-e^{-y}\,y^{x}\Big]_0^\infty + x\int_0^\infty e^{-y}\,y^{x-1}\,dy = x\,\Gamma(x).$$

Der Randterm ist null, denn bei $y=0$ verschwindet $y^x$ und bei unendlich gewinnt $e^{-y}$. Mit dem Startwert

$$\Gamma(1) = \int_0^\infty e^{-y}\,dy = 1$$

folgt Schritt für Schritt die Fakultät, und dazwischen füllt $\Gamma$ die Lücken glatt aus:

$$\Gamma(2) = 1, \qquad \Gamma(3) = 2, \qquad \Gamma(n+1) = n!.$$

**Im Bild:** Das passt zur Formel aus dem Beispiel mit dem lokalen Deckel: Das Integral über $t^ke^{-t}$ ist $k!$, und das
ist genau $\Gamma(k+1)$.
::::

**Die Laplace-Transformation.** Sei $f:[0,\infty)\to\mathbb{R}$ stetig mit höchstens polynomialem Wachstum, das heißt
mit Konstanten $C$ und $p$:

$$\lvert f(t)\rvert \le C\,(1+t^p) \qquad\text{für alle } t\ge0.$$

Dann ist die __Laplace-Transformierte__ auf $(0,\infty)$ wohldefiniert und beliebig oft differenzierbar, und jede Ableitung
holt einen Faktor $-t$ ins Integral:

$$(\mathcal Lf)(x) := \int_0^\infty f(t)\,e^{-xt}\,dt, \qquad \frac{d^k}{dx^k}(\mathcal Lf)(x) = \int_0^\infty(-t)^k f(t)\,e^{-xt}\,dt.$$

**Im Bild:** Der Dämpfer $e^{-xt}$ drückt jede polynomial wachsende Kurve irgendwann unter jeden Deckel — aber nur, wenn
$x>0$ ist. Deshalb arbeitet man lokal.

:::herleitung
Sei $x_0>0$. Für alle $x>x_0/2$ ist der Dämpfer mindestens so stark wie $e^{-x_0t/2}$. Davon spaltet man die Hälfte ab,
um das polynomiale Wachstum zu bändigen: Die Funktion $(1+t^p)\,t^k\,e^{-x_0t/4}$ ist beschränkt, etwa durch eine Zahl
$c$, weil jede Potenz gegen die Exponentialfunktion verliert. Also gilt

$$\lvert t^k f(t)\,e^{-xt}\rvert \le C\,(1+t^p)\,t^k\,e^{-x_0t/2} \le C\,c\,e^{-x_0t/4} =: m_k(t),$$

und dieser Deckel hat die endliche Fläche $4Cc/x_0$. Das Kriterium mit Lokalisierung gibt die Behauptung für jede
Ordnung $k$.
:::

::::beispiel Laplace-Transformierte der Potenzen
Für die konstante Funktion $1$ ist die Laplace-Transformierte die Fläche aus dem ersten Beispiel:

$$(\mathcal L1)(x) = \int_0^\infty e^{-xt}\,dt = \frac1x.$$

Die Ableitungsregel liefert daraus ohne neue Rechnung die Transformierten aller Potenzen:

$$(\mathcal L\,t^k)(x) = (-1)^k\,\frac{d^k}{dx^k}\,\frac1x = \frac{k!}{x^{k+1}}.$$

Für die erste Potenz an der Stelle $2$ etwa ist das $\tfrac14$, passend zur direkten partiellen Integration.

**Im Bild:** Ein Faktor $t$ im Ortsbereich wird zu einer Ableitung (mit Minuszeichen) im Bildbereich — so übersetzt die
Laplace-Transformation Multiplikation in Differentiation.
::::

**Die Fourier-Transformation.** Für eine absolut integrierbare Funktion $f:\mathbb{R}\to\mathbb{C}$ ist ihre
__Fourier-Transformierte__

$$\hat f(\xi) := \frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}} f(x)\,e^{-\mathrm i\xi x}\,dx, \qquad \xi\in\mathbb{R},$$

stetig und beschränkt. Sind zusätzlich für $0\le\ell\le k$ die Funktionen $x^\ell f(x)$ absolut integrierbar, so ist $\hat f$
$k$-mal stetig differenzierbar, und die $\ell$-te Ableitung ist die Fourier-Transformierte von $(-\mathrm ix)^\ell f(x)$.

**Im Bild:** Hier gibt es sogar einen **globalen** Deckel: Der Faktor $e^{-\mathrm i\xi x}$ hat immer den Betrag $1$ und
dreht die Kurve nur in der komplexen Ebene, ohne sie größer zu machen. Daraus folgt die Faustregel **„schneller Abfall im
Ortsraum ⟺ Glätte im Frequenzraum"**.

:::herleitung
Komplexwertige Integranden behandelt man über Real- und Imaginärteil. Der Integrand und seine Ableitungen nach $\xi$ haben
vom Parameter unabhängige Beträge:

$$\big\lvert f(x)\,e^{-\mathrm i\xi x}\big\rvert = \lvert f(x)\rvert, \qquad \Big\lvert\frac{\partial^\ell}{\partial\xi^\ell}\big(f(x)\,e^{-\mathrm i\xi x}\big)\Big\rvert = \lvert x\rvert^\ell\,\lvert f(x)\rvert.$$

Das sind Deckel mit endlicher Fläche nach Voraussetzung; das Kriterium gibt Stetigkeit und die Ableitungsformel.
Beschränkt ist $\hat f$, weil der Betrag des Integrals höchstens das Integral des Betrags ist:

$$\lvert\hat f(\xi)\rvert \le \frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}\lvert f(x)\rvert\,dx.$$
:::

::::beispiel Die Fourier-Transformierte eines Zeltes mit Spitze
Für die beidseitig abfallende Funktion

$$f(x) = e^{-\lvert x\rvert}$$

heben sich Sinusanteile wegen der Symmetrie weg, und es bleibt ein Kosinusintegral:

$$\hat f(\xi) = \frac{2}{\sqrt{2\pi}}\int_0^\infty e^{-x}\cos(\xi x)\,dx = \sqrt{\frac2\pi}\;\frac{1}{1+\xi^2}.$$

Das Ergebnis ist stetig und beschränkt, mit dem größten Wert bei $\xi=0$:

$$\hat f(0) = \sqrt{\frac2\pi} = \frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{-\lvert x\rvert}\,dx.$$

Weil $x^\ell e^{-\lvert x\rvert}$ für jedes $\ell$ absolut integrierbar ist, ist $\hat f$ beliebig oft differenzierbar.

**Im Bild:** $f$ fällt exponentiell ab, also ist $\hat f$ glatt. Umgekehrt hat $f$ bei $0$ einen Knick — und $\hat f$ fällt
deshalb nur langsam ab, wie $1/\xi^2$. Glätte und Abfall tauschen bei der Fourier-Transformation die Rollen.
::::

:::grafik
Szene: hoema3/integralrechnung-rn/02-anwendungen · Vorlage: gamma-laplace-fourier-kacheln
Drei Kacheln: die Gamma-Funktion $\Gamma(x)$ als glatte Kurve auf $(0,\infty)$ durch die Punkte $(n+1,n!)$; die
Laplace-Transformation als Block $f(t)\mapsto(\mathcal Lf)(x)$ mit dem Dämpfer $e^{-xt}$ und lokalem Deckel; die
Fourier-Transformation als Paar $e^{-\lvert x\rvert}\leftrightarrow\sqrt{2/\pi}/(1+\xi^2)$. Gemeinsame Beschriftung „glatt
dank Deckel". (Rot = Ergebnisfunktion, blau = Eingabe, orange = Deckel, grau = Achsen.)
:::

## Bedeutung und Ausblick

Das Majorantenkriterium ist der Grund, warum man mit Gamma-Funktion, Laplace- und Fourier-Transformation rechnen darf
wie mit gewöhnlichen Funktionen: Es sichert Stetigkeit und das Ableiten unter dem Integral, obwohl der Bereich unendlich
ist. Im Lebesgue-Integral, das über diesen Kurs hinausgeht, heißt dasselbe Prinzip __Satz von der majorisierten
Konvergenz__ — ein Deckel mit endlicher Fläche erlaubt dort ganz allgemein, Grenzwert und Integral zu vertauschen.

Bisher integrierten wir über **ein** Intervall, mit einem Parameter. Jetzt geht es zu echten **mehrdimensionalen**
Integralen: Wie integriert man über einen Quader im $\mathbb{R}^n$, und darf man die Integrationen in beliebiger
Reihenfolge ausführen? Das beantwortet der __Satz von Fubini__ im nächsten Artikel.

:::kern
- Ein __uneigentliches Parameterintegral__ $g(\vec x)=\int_a^b f(\vec x,t)\,dt$ ist der Grenzwert der Flächen über wachsenden Teilintervallen; die __Schwänze__ müssen verschwinden.
- Konvergenz für jeden Parameter genügt **nicht**: Beim Dirichlet-Integral $\int_0^\infty\frac{\sin(tx)}{t}\,dt$ springt $g$ bei $0$ von $-\pi/2$ auf $+\pi/2$, weil der Schwanz für kleine $x$ beliebig langsam schrumpft.
- __Majorantenkriterium__: Ein vom Parameter unabhängiger Deckel $\lvert f(\vec x,t)\rvert\le m(t)$ mit endlicher Fläche macht $g$ stetig.
- Mechanismus: Deckel zerlegt in ein endliches Mittelstück (voriger Artikel) und Schwänze, die für alle Parameter zugleich klein sind.
- Deckel $m_k$ für die Ableitungen $\partial f/\partial x_k$ erlauben das Ableiten unter dem Integral.
- __Lokal genügt__: Ein Deckel je Umgebung reicht, weil Stetigkeit und Differenzierbarkeit lokale Eigenschaften sind.
- Die __Gamma-Funktion__ ist stetig differenzierbar (Deckel an beiden Enden); partielle Integration gibt $\Gamma(n+1)=n!$.
- __Laplace__: Jede Ableitung holt einen Faktor $-t$ ins Integral; $(\mathcal L\,t^k)(x)=k!/x^{k+1}$.
- __Fourier__: globaler Deckel $\lvert f\rvert$; schneller Abfall von $f$ ergibt Glätte von $\hat f$ und umgekehrt.
:::

:::quiz
F: Was ist ein uneigentliches Parameterintegral, und was ist sein Schwanz?
A: Für jeden Parameter $\vec x$ ist $g(\vec x)=\int_a^b f(\vec x,t)\,dt$ der Grenzwert der Flächen über immer größeren Teilintervallen $[\alpha,\beta]$. Der Schwanz ist das, was jenseits einer Grenze $T$ noch an Fläche liegt — er muss für $T\to b$ verschwinden. Bei $\int_0^\infty e^{-xt}\,dt$ ist er genau $e^{-xT}/x$.
F: Warum versagen die Sätze des vorigen Artikels bei unendlichen Intervallen?
A: Ihr Beweis beruhte auf einem festen, abgeschlossenen Intervall, auf dem die Kurve gleichmäßig mit dem Regler mitgeht. Bei einem unendlichen Bereich können die Schwänze für verschiedene Reglerstellungen verschieden schnell verschwinden; ein fester Abschneidepunkt reicht dann nicht für alle zugleich.
F: Wie kann $\int_0^\infty\frac{\sin(tx)}{t}\,dt$ bei $x=0$ springen, obwohl es für jedes $x$ konvergiert?
A: Nach der Substitution $u=tx$ ist der Schwanz jenseits von $T$ gleich $\int_{Tx}^\infty\frac{\sin u}{u}\,du$. Für jedes $T$ kann man $x$ so klein wählen, dass fast die ganze Fläche $\pi/2$ im Schwanz steckt. Die Konvergenz ist nicht gleichmäßig, und $g$ springt von $-\pi/2$ über $0$ auf $+\pi/2$.
F: Warum gibt es beim Dirichlet-Integral keinen Deckel?
A: Die naheliegende Schranke $\lvert\sin(tx)/t\rvert\le1/t$ hat unendliche Fläche, und das Integral ist nicht einmal absolut konvergent. Seine Konvergenz lebt davon, dass sich positive und negative Bögen gegenseitig ausgleichen — und das dauert für kleine $x$ beliebig lange.
F: Was besagt das Majorantenkriterium, und warum muss der Deckel vom Parameter unabhängig sein?
A: Gibt es eine Funktion $m(t)$ mit endlicher Fläche und $\lvert f(\vec x,t)\rvert\le m(t)$ für alle $\vec x$, so ist $g$ stetig; mit solchen Deckeln für die Ableitungen darf man unter dem Integral ableiten. Nur ein parameterunabhängiger Deckel begrenzt alle Schwänze zugleich — hinge er vom Regler ab, wäre nichts gewonnen.
F: Wie läuft der Beweis der Stetigkeit mit dem Deckel?
A: Man wählt Grenzen $\alpha,\beta$, jenseits derer der Deckel weniger als $\varepsilon$ Fläche hat; dann sind die Schwänze aller Kurven kleiner als $\varepsilon$. Das Mittelstück über $[\alpha,\beta]$ ist ein Parameterintegral über einem festen Intervall und nach dem vorigen Artikel stetig. Die Dreiecksungleichung setzt beides zu $\lvert g(\vec x)-g(\vec x_0)\rvert<3\varepsilon$ zusammen.
F: Was bedeutet „lokal genügt", und wie sieht das bei $\int_0^\infty e^{-xt}\,dt$ aus?
A: Stetigkeit und Differenzierbarkeit hängen nur von einer kleinen Umgebung jedes Punktes ab, also reicht dort ein Deckel. Für alle $x$ zugleich gibt es keinen, weil die Kurven für $x\to0$ gegen $1$ gehen. Für $x\ge x_0/2$ passt aber $e^{-x_0t/2}$, und damit folgt $g'(x)=-1/x^2$.
F: Wie zeigt man $\Gamma(n+1)=n!$, und warum ist $\Gamma$ differenzierbar?
A: Partielle Integration gibt $\Gamma(x+1)=x\,\Gamma(x)$, und $\Gamma(1)=1$; daraus folgt die Fakultät. Differenzierbar ist $\Gamma$, weil man auf jedem Bereich $[c,d]\subseteq(0,\infty)$ einen Deckel findet — $y^{c-1}$ nahe null, $e^{-y}y^{d-1}$ für große $y$ —, auch mit dem Faktor $\ln y$ der Ableitung.
F: Wie gewinnt man die Laplace-Transformierten $(\mathcal L\,t^k)(x)=k!/x^{k+1}$ ohne neue Integration?
A: Man kennt $(\mathcal L1)(x)=\int_0^\infty e^{-xt}\,dt=1/x$. Jede Ableitung nach $x$ holt einen Faktor $-t$ ins Integral — erlaubt dank des lokalen Deckels. Also ist $(\mathcal L\,t^k)(x)=(-1)^k\frac{d^k}{dx^k}\frac1x=\frac{k!}{x^{k+1}}$.
F: Warum gilt bei der Fourier-Transformation „schneller Abfall ⟺ Glätte", etwa bei $e^{-\lvert x\rvert}$?
A: Der Faktor $e^{-\mathrm i\xi x}$ hat den Betrag $1$, also ist $\lvert f\rvert$ ein globaler Deckel, und jede Ableitung nach $\xi$ bringt einen Faktor $-\mathrm ix$. Fällt $f$ so schnell ab, dass $x^\ell f$ integrierbar ist, ist $\hat f$ $\ell$-mal differenzierbar. Bei $e^{-\lvert x\rvert}$ ist $\hat f=\sqrt{2/\pi}/(1+\xi^2)$ glatt, fällt aber nur langsam ab, weil $f$ bei $0$ einen Knick hat.
:::
