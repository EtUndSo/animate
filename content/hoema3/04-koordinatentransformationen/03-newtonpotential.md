---
title: Das Newtonpotential und die Poisson-Gleichung
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040300
summary: Von Grund auf – das Potential einer ganzen Ladungs- oder Massenwolke als Summe der Coulomb-Potentiale all ihrer Körnchen, $u(\vec x)=\frac{1}{4\pi}\int\frac{f(\vec y)}{\lvert\vec x-\vec y\rvert}\,d^3y$. Leitbild ist eine Wolke aus winzigen Körnchen, bei kugelsymmetrischen Wolken die Zwiebel aus dem vorigen Artikel. Mit der Existenz trotz Singularität, dem Fernfeld einer Punktladung, Newtons Schalentheorem samt Erdbeschleunigung und Tunnel durch die Erde, dem Gaußschen Gesetz für kugelsymmetrische Wolken und der Poisson-Gleichung $-\Delta u=f$ – nachgerechnet an einer glatten Wolke. Mit Beispiel-Seite.
tags: Newtonpotential, Poisson-Gleichung, Potentialtheorie, Fundamentallösung, Superposition, Schalentheorem, Kugelschale, harmonische Funktion
---

## Anschaulich

Welches Potential erzeugt eine geladene Wolke, ein Planet, eine Raumladungszone im Halbleiter? Für eine einzelne Punktladung
kennt man die Antwort aus dem Artikel über Gradienten: Das Coulomb-Potential fällt mit dem Kehrwert des Abstands. Eine
ausgedehnte Ladung wirkt schwieriger — aber nur auf den ersten Blick.

**Das Leitbild dieses Artikels:** eine **Wolke aus winzigen Körnchen**. Man zerlegt die Ladung in so kleine Stücke, dass
jedes wie eine Punktladung wirkt. Jedes Körnchen erzeugt sein Coulomb-Potential, und weil sich Potentiale einfach addieren,
ist das Potential der Wolke die Summe über alle Körnchen — im Grenzfall ein Integral. Das ist das __Newtonpotential__.

Ein Körnchen sitzt genau an dem Ort, an dem man das Potential wissen will; sein Abstand ist null. Trotzdem bleibt das
Integral endlich, aus demselben Grund wie im vorigen Artikel: Die innersten Zwiebelschalen um diesen Ort sind winzig.

Ist die Wolke kugelsymmetrisch, schält sich die Zwiebel von selbst. Von außen wirkt sie, als säße ihre ganze Ladung im
Mittelpunkt, und in einem Hohlraum spürt man von der Schale darum gar nichts — Newtons __Schalentheorem__. Umgekehrt verrät
das Potential die Wolke: Seine Krümmung an einem Ort ist die Ladungsdichte dort. Das ist die __Poisson-Gleichung__.

:::grafik
Szene: hoema3/koordinatentransformationen/03-koernchenwolke · Vorlage: superposition-3d
Links eine Ladungswolke aus vielen Körnchen, deren Farbe die Dichte zeigt, und ein Messpunkt. Von jedem Körnchen läuft eine
dünne Linie zum Messpunkt, beschriftet mit seinem Beitrag „Ladung durch $4\pi$ mal Abstand"; ein Zähler summiert. Ein Regler
verfeinert die Zerlegung, und die Summe nähert sich dem Integral. Rechts eine kugelsymmetrische Wolke als Zwiebel; liegt der
Messpunkt außen, zieht sie sich im Bild zu einem Punkt im Mittelpunkt mit derselben Ladung zusammen. Kernaussage: Das
Potential der Wolke ist die Summe der Coulomb-Potentiale ihrer Körnchen. (Rot = Körnchen, blau = Messpunkt und Summe,
orange = Beiträge, grau = Achsen.)
:::

## Singuläre Parameterintegrale

Hinter dem Newtonpotential steht eine allgemeine Form. **Die Akteure:** eine Dichte $f:\mathbb{R}^n\to\mathbb{R}$ und ein
__Kern__ $k:\mathbb{R}^n\setminus\{\vec 0\}\to\mathbb{R}$, der am Ursprung eine Singularität hat. Aus ihnen entsteht

$$u(\vec x) = \int_{\mathbb{R}^n}k(\vec x-\vec y)\,f(\vec y)\,d^ny.$$

Das ist ein Parameterintegral wie im Artikel über Parameterintegrale, mit dem Punkt $\vec x$ als Parameter. Neu ist die
Singularität: Bei $\vec y=\vec x$ ist der Kern nicht definiert.

Man versteht solche Integrale wie im vorigen Artikel als eine Art uneigentliches Integral: Man schneidet die Singularität ab —
etwa eine kleine Kugel um $\vec x$ — und lässt den abgeschnittenen Teil gegen null gehen.

**Im Bild:** $\vec x$ ist der Ort, an dem man misst, $\vec y$ der Ort eines Körnchens und $f(\vec y)$ die Ladungsdichte dort. Der
Kern $k(\vec x-\vec y)$ beschreibt, wie das Körnchen über die Entfernung wirkt. Das Integral sammelt alle Körnchen ein.

## Das Newtonpotential

**Die Akteure:** eine stetig differenzierbare Dichte $f:\mathbb{R}^3\to\mathbb{R}$ mit __kompaktem Träger__ — sie ist außerhalb
einer Kugel $K_{R_0}$ vom Radius $R_0$ um den Ursprung null — und als Kern das Coulomb-Potential der Einheitsladung aus dem
vorigen Artikel:

$$g(\vec z) = \frac{1}{4\pi\lvert\vec z\rvert}, \qquad \vec z\neq\vec 0.$$

Der Träger einer Funktion ist die kleinste abgeschlossene Menge, außerhalb der sie null ist; kompakt heißt beschränkt und
abgeschlossen. Das __Newtonpotential__ von $f$ ist

:::formel Definition
$$u(\vec x) = \frac{1}{4\pi}\int_{\mathbb{R}^3}\frac{f(\vec y)}{\lvert\vec x-\vec y\rvert}\,d^3y = \int_{\mathbb{R}^3}g(\vec x-\vec y)\,f(\vec y)\,d^3y.$$
:::

**So liest man das:** Eingabe ist ein Ort $\vec x$, Ausgabe eine Zahl, das Potential dort. Ein Körnchen am Ort $\vec y$ trägt die
Ladung $f(\vec y)\,d^3y$ und damit das Potential dieser Ladung geteilt durch $4\pi$ mal den Abstand bei.

**Im Bild:** Die Körnchenwolke. Nahe Körnchen zählen viel, ferne wenig, und das Potential ist die Summe aller Beiträge.

:::herleitung
**Das Integral existiert für jedes $\vec x$.** Die Dichte ist stetig und außerhalb von $K_{R_0}$ null, also beschränkt; sei $b$
eine Schranke für $\lvert f\rvert$. Man schneidet die Kugel $K_\delta(\vec x)$ vom Radius $\delta$ um $\vec x$ ab. Außerhalb von ihr ist
der Integrand stetig und außerhalb von $K_{R_0}$ null — ein gewöhnliches Integral über eine beschränkte Menge.

In der Kugel ist der Integrand betragsmäßig höchstens

$$\frac{\lvert f(\vec y)\rvert}{4\pi\lvert\vec x-\vec y\rvert} \le \frac{b}{4\pi\lvert\vec x-\vec y\rvert},$$

eine Singularität mit dem Exponenten $1$, nur um $\vec x$ verschoben. Eine Verschiebung hat die Jacobi-Determinante $1$ und
ändert nach dem Transformationssatz kein Integral. Nach dem Satz über singuläre Integranden des vorigen Artikels existiert das
Integral über die Kugel deshalb, sogar absolut. Mit der Rechnung für das Coulomb-Potential dort ist sein Betrag höchstens

$$\int_{K_\delta(\vec x)}\frac{b}{4\pi\lvert\vec x-\vec y\rvert}\,d^3y = \frac{b\,\delta^2}{2}.$$

**Im Bild:** Die Körnchen in der Kugel um den Messort sind nah, aber es sind wenige. Ihre Menge schrumpft mit dem Volumen,
also wie $\delta^3$, ihr Gewicht wächst nur wie $\frac{1}{\delta}$ — zusammen bleibt $\delta^2$.
:::

Man kann das Abschneiden auch so beschreiben: Ersetzt man den Abstand im Nenner durch einen Abstand, der nie unter $\delta$
fällt, etwa durch

$$\max\big(\lvert\vec x-\vec y\rvert,\ \delta\big),$$

sind die Integranden stetig mit kompaktem Träger, und für $\delta\to0$ entsteht $u(\vec x)$. Die Voraussetzungen an $f$ lassen
sich abschwächen; statt eines kompakten Trägers genügt etwa ein ausreichend schnelles Abklingen von $f$ für große $\lvert\vec y\rvert$.

::::beispiel Wie viel die Nachbarschaft beiträgt
Ist die Dichte betragsmäßig höchstens $1$, trägt die Kugel vom Radius $\delta$ um den Messort höchstens $\frac{\delta^2}{2}$ zum
Potential bei:

$$\delta = 0{,}1:\ \ \frac{\delta^2}{2} = 0{,}005, \qquad \delta = 0{,}01:\ \ \frac{\delta^2}{2} = 0{,}000\,05.$$

Zum Vergleich: Eine Kugel vom Radius $1$ mit der Dichte $1$ erzeugt in ihrem Mittelpunkt das Potential $\frac12$ — das ist
dieselbe Rechnung mit dem Radius $1$. Die Kugel vom Radius $0{,}1$ um den Messort liefert davon nur ein Prozent.

**Im Bild:** Das Körnchen genau am Messort ist kein Problem: Es hat das Volumen null, und seine Nachbarn sind zu wenige, um ins
Gewicht zu fallen.
::::

**Von weitem.** Weil $f$ außerhalb von $K_{R_0}$ verschwindet, sind alle Körnchen von einem fernen Messort aus fast gleich weit
entfernt. Mit der Gesamtladung

$$Q = \int_{\mathbb{R}^3}f(\vec y)\,d^3y$$

gilt für jeden Messort außerhalb von $K_{R_0}$

:::formel
$$\Big\lvert u(\vec x)-\frac{Q}{4\pi\lvert\vec x\rvert}\Big\rvert \le \frac{R_0}{\lvert\vec x\rvert-R_0}\cdot\frac{1}{4\pi\lvert\vec x\rvert}\int_{\mathbb{R}^3}\lvert f(\vec y)\rvert\,d^3y.$$
:::

**So liest man das:** Von weitem ist das Potential das einer Punktladung $Q$ im Ursprung. Für eine Dichte ohne negative Werte
ist das Integral von $\lvert f\rvert$ gleich $Q$, und der relative Fehler ist höchstens

$$\frac{R_0}{\lvert\vec x\rvert-R_0}.$$

Insbesondere geht $u(\vec x)$ für $\lvert\vec x\rvert\to\infty$ gegen null.

**Im Bild:** Von weitem verschmilzt die Wolke zu einem Punkt. Je größer der Abstand, desto weniger unterscheiden sich die
Entfernungen der einzelnen Körnchen.

:::herleitung
Nach der Dreiecksungleichung unterscheiden sich die Abstände vom Messort zum Körnchen und zum Ursprung höchstens um
$\lvert\vec y\rvert$, und für Körnchen in $K_{R_0}$ ist der Abstand zum Messort mindestens $\lvert\vec x\rvert-R_0$:

$$\Big\lvert\lvert\vec x\rvert-\lvert\vec x-\vec y\rvert\Big\rvert \le \lvert\vec y\rvert \le R_0, \qquad \lvert\vec x-\vec y\rvert \ge \lvert\vec x\rvert-R_0 > 0.$$

Damit ist

$$\Big\lvert\frac{1}{\lvert\vec x-\vec y\rvert}-\frac{1}{\lvert\vec x\rvert}\Big\rvert = \frac{\big\lvert\lvert\vec x\rvert-\lvert\vec x-\vec y\rvert\big\rvert}{\lvert\vec x\rvert\,\lvert\vec x-\vec y\rvert} \le \frac{R_0}{\lvert\vec x\rvert\,(\lvert\vec x\rvert-R_0)}.$$

Die Differenz, um die es geht, ist ein Integral über diese Klammer:

$$u(\vec x)-\frac{Q}{4\pi\lvert\vec x\rvert} = \frac{1}{4\pi}\int_{K_{R_0}}f(\vec y)\Big(\frac{1}{\lvert\vec x-\vec y\rvert}-\frac{1}{\lvert\vec x\rvert}\Big)\,d^3y.$$

Schätzt man die Klammer ab und zieht den Betrag von $f$ ins Integral, folgt die Formel. Die rechte Seite und $\frac{Q}{4\pi\lvert\vec x\rvert}$
gehen für großes $\lvert\vec x\rvert$ gegen null, also auch $u(\vec x)$.
:::

::::beispiel Zwei Kügelchen von weitem
Zwei kleine, gleichmäßig geladene Kügelchen mit der Ladung $1$ sitzen bei $(0,0,1)$ und $(0,0,-1)$. Von außen wirkt jedes wie
eine Punktladung in seinem Mittelpunkt — das zeigt der Abschnitt über kugelsymmetrische Wolken —, und die Potentiale beider
addieren sich. Die Gesamtladung ist $2$. Auf der $z$-Achse und senkrecht dazu, jeweils im Abstand $10$ vom Ursprung, ist

$$u(0,0,10) = \frac{1}{4\pi}\Big(\frac19+\frac1{11}\Big)\approx\frac{0{,}2020}{4\pi}, \qquad u(10,0,0) = \frac{1}{4\pi}\cdot\frac{2}{\sqrt{101}}\approx\frac{0{,}1990}{4\pi}.$$

Die Punktladung $2$ im Ursprung gäbe in beiden Fällen $\frac{0{,}2}{4\pi}$. Der Fehler ist rund ein Prozent bzw. ein halbes Prozent —
weit unter der Schranke der Abschätzung, mit $R_0$ knapp über $1$:

$$\frac{R_0}{\lvert\vec x\rvert-R_0}\approx\frac19\approx11\,\%.$$

**Im Bild:** Aus zehn Einheiten Abstand sehen die beiden Kügelchen fast wie eines aus. Längs ihrer Verbindungslinie ist der
Unterschied am größten, weil dort ein Kügelchen deutlich näher liegt als das andere.
::::

## Kugelsymmetrische Wolken

**Die Akteure:** eine __kugelsymmetrische__ Dichte, die nur vom Abstand zum Ursprung abhängt, mit einem stückweise stetigen
Profil $\rho:[0,\infty)\to\mathbb{R}$, das oberhalb von $R_0$ null ist:

$$f(\vec y) = \rho\big(\lvert\vec y\rvert\big).$$

Stückweise stetig heißt: Das Profil darf an endlich vielen Stellen springen, etwa am Rand einer gleichmäßig geladenen Kugel.
Solche Dichten sind nicht stetig differenzierbar, ihr Newtonpotential ist aber wie oben erklärt.

**Das Potential hängt nur vom Abstand ab.** Dreht man eine kugelsymmetrische Wolke um den Ursprung, ändert sie sich nicht —
also auch ihr Potential nicht. Es gibt deshalb ein __Profil__ $h$ des Potentials mit

$$u(\vec x) = h\big(\lvert\vec x\rvert\big).$$

:::herleitung
Sei $A$ eine Drehung, eine orthogonale Matrix mit der Determinante $1$. Sie ändert keine Längen. Substituiert man im
Newtonpotential $\vec y=A\vec w$, ist der Betrag der Jacobi-Determinante $1$, und nach dem Transformationssatz

$$u(A\vec x) = \frac{1}{4\pi}\int\frac{\rho(\lvert A\vec w\rvert)}{\lvert A\vec x-A\vec w\rvert}\,d^3w = \frac{1}{4\pi}\int\frac{\rho(\lvert\vec w\rvert)}{\lvert\vec x-\vec w\rvert}\,d^3w = u(\vec x).$$

Zwei Punkte mit gleichem Abstand vom Ursprung gehen durch eine Drehung ineinander über; also hat $u$ dort denselben Wert.
:::

Das Profil lässt sich ausrechnen. Für jeden Abstand $a>0$ des Messorts gilt

:::formel Satz
$$h(a) = \frac1a\int_0^a\rho(r)\,r^2\,dr+\int_a^{\infty}\rho(r)\,r\,dr.$$
:::

**So liest man das:** Der erste Term ist das Potential der Ladung innerhalb des Radius $a$, als säße sie im Mittelpunkt. Diese
innere Ladung ist

$$q(a) = 4\pi\int_0^a\rho(r)\,r^2\,dr,$$

denn eine dünne Schale vom Radius $r$ hat das Volumen $4\pi r^2\,dr$; der erste Term ist genau $\frac{q(a)}{4\pi a}$. Der zweite Term
sammelt die Schalen außerhalb, und jede von ihnen trägt einen festen Betrag bei, gleichgültig, wo innen man steht.

**Im Bild:** Die Zwiebel. Steht man im Abstand $a$ vom Mittelpunkt, wirken alle Schalen innerhalb so, als säße ihre ganze
Ladung im Mittelpunkt. Jede Schale außerhalb hebt das Potential nur um einen festen Betrag an — wie ein Sockel, auf dem man
steht, ohne geschoben zu werden.

:::herleitung
**Schritt 1: der Messort auf der Achse.** Wegen der Drehsymmetrie darf man den Messort auf die $z$-Achse legen:

$$\vec x = (0,\ 0,\ a).$$

Den Quellpunkt $\vec y$ beschreibt man in Kugelkoordinaten mit dem Abstand $r$, dem Polarwinkel $\theta$ und dem Azimut $\varphi$.
Der Winkel zwischen $\vec x$ und $\vec y$ ist dann $\theta$, und der Kosinussatz gibt

$$\lvert\vec x-\vec y\rvert = \sqrt{a^2+r^2-2ar\cos\theta}.$$

**Schritt 2: Kugelkoordinaten.** Mit dem Volumenelement $r^2\sin\theta\,dr\,d\theta\,d\varphi$ des vorigen Artikels — das Integral
über $\varphi$ gibt $2\pi$ — ist

$$u(\vec x) = \frac{1}{4\pi}\cdot2\pi\int_0^\infty\rho(r)\,r^2\Big(\int_0^\pi\frac{\sin\theta\,d\theta}{\sqrt{a^2+r^2-2ar\cos\theta}}\Big)\,dr.$$

**Schritt 3: das Winkelintegral.** Mit der Substitution $s=\cos\theta$ wird $\sin\theta\,d\theta$ zu $-ds$, und

$$\int_{-1}^{1}\frac{ds}{\sqrt{a^2+r^2-2ars}} = \Big[-\frac{1}{ar}\sqrt{a^2+r^2-2ars}\,\Big]_{-1}^{1} = \frac{(a+r)-\lvert a-r\rvert}{ar} = \frac{2}{\max(a,r)}.$$

Die Wurzeln an den Grenzen sind $a+r$ und $\lvert a-r\rvert$. Liegt die Schale innen, ist $\max(a,r)$ gleich $a$, liegt sie außen,
gleich $r$.

**Schritt 4: zusammensetzen.** Teilt man das Integral über $r$ bei $a$, entsteht

$$u(\vec x) = \frac12\int_0^\infty\rho(r)\,r^2\cdot\frac{2}{\max(a,r)}\,dr = \frac1a\int_0^a\rho(r)\,r^2\,dr+\int_a^\infty\rho(r)\,r\,dr.$$

**Im Bild:** Das Winkelintegral ist das Potential einer einzelnen dünnen Schale. Von außen gesehen ist es das einer
Punktladung im Mittelpunkt, von innen gesehen eine Konstante.
:::

**Newtons Schalentheorem.** Zwei Folgerungen machen die Formel berühmt. Außerhalb der Wolke verschwindet der zweite Term, und
in einem ladungsfreien Hohlraum — einer Kugel vom Radius $R_1$, in der das Profil null ist — verschwindet der erste:

$$h(a) = \frac{Q}{4\pi a} \quad\text{für } a\ge R_0, \qquad h(a) = \int_{R_1}^{\infty}\rho(r)\,r\,dr \quad\text{für } a\le R_1.$$

Von außen wirkt die Wolke also genau wie eine Punktladung $Q$ in ihrem Mittelpunkt. Im Hohlraum ist das Potential konstant, und
das Feld, sein negativer Gradient, ist null.

:::herleitung
Für $a\ge R_0$ ist das Profil oberhalb von $a$ null, und das erste Integral ist die ganze Ladung geteilt durch $4\pi$, denn in
Kugelkoordinaten ist

$$Q = \int_{\mathbb{R}^3}\rho(\lvert\vec y\rvert)\,d^3y = 4\pi\int_0^\infty\rho(r)\,r^2\,dr.$$

Für $a\le R_1$ ist das Profil unterhalb von $a$ null, das erste Integral verschwindet, und im zweiten trägt erst der Bereich ab
$R_1$ bei — ein Wert, der nicht von $a$ abhängt.

**Im Bild,** nach Newtons eigener Überlegung: Von einem Punkt im Hohlraum aus schneidet ein schmaler Doppelkegel zwei Stücke
aus einer dünnen Schale, in entgegengesetzten Richtungen. Das ferne Stück ist größer — seine Fläche wächst mit dem Quadrat des
Abstands —, zieht aber schwächer, denn die Kraft fällt mit dem Quadrat des Abstands. Beides gleicht sich genau aus.
:::

:::grafik
Szene: hoema3/koordinatentransformationen/03-zwiebel-schalentheorem · Vorlage: schalen-schnitt-2d
Ein Schnitt durch eine kugelsymmetrische Wolke mit farbigen Schalen und ein Messpunkt im Abstand $a$ vom Mittelpunkt, mit der
Maus verschiebbar. Die Schalen innerhalb des Kreises vom Radius $a$ ziehen sich im Bild zu einer Punktladung $q(a)$ im
Mittelpunkt zusammen; die äußeren werden blass und tragen als Sockel einen festen Betrag bei. Daneben das Profil $h$ als Kurve
mit dem aktuellen Wert. Im Hohlraum einer Schale zeigt ein Doppelkegel die zwei herausgeschnittenen Stücke mit ihren Flächen
und Kräften, die sich aufheben. Kernaussage: Innen zählt die eingeschlossene Ladung, außen nur ein Sockel. (Rot = innere
Ladung, grau = äußere Schalen, blau = Messpunkt und Profil, orange = Doppelkegel.)
:::

::::beispiel Die gleichmäßig geladene Kugelschale
Eine Kugelschale zwischen den Radien $R_1$ und $R_2$, mit $0\le R_1<R_2$, mit der konstanten Dichte
$\rho$ — das Profil ist $\rho$ zwischen den beiden Radien und null sonst:

$$S = \big\{\vec y\in\mathbb{R}^3 : R_1\le\lvert\vec y\rvert\le R_2\big\}, \qquad u(\vec x) = \frac{\rho}{4\pi}\int_S\frac{d^3y}{\lvert\vec x-\vec y\rvert}.$$

**(a) Außen**, für $a\ge R_2$: Nur der erste Term bleibt,

$$h(a) = \frac{\rho}{a}\int_{R_1}^{R_2}r^2\,dr = \rho\,\frac{R_2^3-R_1^3}{3a} = \frac{Q}{4\pi a}, \qquad Q = \rho\cdot\frac43\pi\big(R_2^3-R_1^3\big).$$

**(b) Im Hohlraum**, für $a\le R_1$: Nur der zweite Term bleibt, und er hängt nicht von $a$ ab:

$$h(a) = \rho\int_{R_1}^{R_2}r\,dr = \rho\,\frac{R_2^2-R_1^2}{2}.$$

**(c) In der Schale selbst**, für $R_1<a<R_2$, tragen beide Terme bei:

$$h(a) = \frac{\rho}{a}\int_{R_1}^{a}r^2\,dr+\rho\int_a^{R_2}r\,dr = \rho\Big(\frac{R_2^2}{2}-\frac{a^2}{6}-\frac{R_1^3}{3a}\Big).$$

An den Rändern passen die Stücke zusammen: Am inneren Rand gibt (c) den Wert aus (b), am äußeren den aus (a). Für die Schale
zwischen den Radien $1$ und $2$ mit der Dichte $1$ ist

$$h(0{,}5) = 1{,}5, \qquad h(1{,}5)\approx1{,}40, \qquad h(3) = \frac79\approx0{,}78.$$

**(d) Die Vollkugel** vom Radius $R$ ist der Fall ohne Hohlraum, $R_1=0$. Außen gilt (a) mit der Ladung

$$Q = \rho\cdot\frac43\pi R^3,$$

innen gibt (c)

$$h(a) = \rho\Big(\frac{R^2}{2}-\frac{a^2}{6}\Big).$$

Im Mittelpunkt ist das Potential $\frac{\rho R^2}{2}$, anderthalbmal so groß wie an der Oberfläche. Von außen kann man nicht
unterscheiden, ob die Ladung gleichmäßig über die Kugel verteilt oder im Mittelpunkt gebündelt ist.

**Im Bild:** Bei (a) wirkt die ganze Zwiebel wie ein Punkt, bei (b) ist sie nur ein Sockel, bei (c) zählt der innere Teil als
Punkt und der äußere als Sockel.
::::

**Das Feld einer kugelsymmetrischen Wolke.** Nach dem Artikel über Gradienten ist der Gradient einer Funktion des Abstands das
Profil abgeleitet mal der Einheitsvektor $\vec e_r$, der vom Ursprung weg zeigt. Das Feld $\vec E=-\nabla u$ ist deshalb

:::formel
$$\vec E(\vec x) = \frac{q(a)}{4\pi a^2}\,\vec e_r, \qquad a = \lvert\vec x\rvert>0.$$
:::

**So liest man das:** Im Abstand $a$ wirkt nur die eingeschlossene Ladung $q(a)$, und zwar wie eine Punktladung im
Mittelpunkt. Die äußeren Schalen tragen zum Feld nichts bei. Das ist das __Gaußsche Gesetz__ für kugelsymmetrische Wolken.

**Im Bild:** Die Sockel der äußeren Schalen heben das Potential nur an; geschoben wird man allein von der Zwiebel unter den
eigenen Füßen.

:::herleitung
Man leitet das Profil nach $a$ ab — den ersten Term mit der Produktregel, beide Integrale mit dem Hauptsatz:

$$h'(a) = -\frac{1}{a^2}\int_0^a\rho(r)\,r^2\,dr+\frac1a\,\rho(a)\,a^2-\rho(a)\,a = -\frac{q(a)}{4\pi a^2}.$$

Die beiden Terme mit $\rho(a)$ heben sich weg. An einer Sprungstelle des Profils gilt dasselbe für die Ableitung von links und
von rechts, mit dem jeweiligen Grenzwert des Profils; das Profil $h$ ist also auch dort stetig differenzierbar. Mit dem
Gradienten aus dem Artikel über Gradienten folgt

$$\vec E = -\nabla u = -h'(a)\,\vec e_r = \frac{q(a)}{4\pi a^2}\,\vec e_r.$$
:::

::::beispiel Die Erde: Gewicht, Inneres und ein Tunnel
In der Gravitation ist das Potential einer Massendichte $-4\pi G$ mal ihr Newtonpotential, mit der Gravitationskonstante $G$.
Die Beschleunigung zeigt deshalb zum Mittelpunkt und hat den Betrag $G$ mal der eingeschlossenen Masse durch $a^2$.

**(a) An der Oberfläche** wirkt die ganze Masse $M$ der Erde wie ein Punkt im Mittelpunkt:

$$g = \frac{GM}{R^2} = \frac{6{,}674\cdot10^{-11}\,\frac{\mathrm{m}^3}{\mathrm{kg\,s^2}}\cdot5{,}972\cdot10^{24}\,\mathrm{kg}}{\big(6{,}371\cdot10^{6}\,\mathrm{m}\big)^2}\approx9{,}82\,\frac{\mathrm{m}}{\mathrm{s}^2}.$$

**(b) Im Inneren** einer gleichmäßig dichten Erde ist die eingeschlossene Masse $M\frac{a^3}{R^3}$, also

$$g(a) = \frac{GM}{R^3}\,a.$$

Auf halbem Weg zum Mittelpunkt ist die Beschleunigung nur halb so groß, rund $4{,}9\,\frac{\mathrm{m}}{\mathrm{s}^2}$. Die echte Erde hat
einen dichteren Kern; das gleichmäßige Modell ist eine Vereinfachung.

**(c) Ein Tunnel durch den Mittelpunkt.** Nach (b) ist die Beschleunigung proportional zum Abstand und zeigt zum Mittelpunkt —
die Gleichung einer harmonischen Schwingung mit der Kreisfrequenz

$$\omega = \sqrt{\frac{GM}{R^3}}\approx1{,}24\cdot10^{-3}\,\frac1{\mathrm{s}}.$$

Ein Körper, ohne Reibung fallen gelassen, kommt nach einer halben Schwingung auf der anderen Seite an:

$$\frac{\pi}{\omega}\approx2530\,\mathrm{s}\approx42\,\mathrm{min}.$$

**Im Bild:** Auf dem Weg nach innen bleiben immer mehr Schalen über dem Körper zurück. Sie ziehen nicht, und die Zwiebel unter
ihm wird kleiner — deshalb nimmt die Beschleunigung zum Mittelpunkt hin ab.
::::

## Die Poisson-Gleichung

**Die Akteure:** wie oben eine stetig differenzierbare Dichte $f$ mit kompaktem Träger und ihr Newtonpotential $u$. Dann ist $u$
zweimal stetig differenzierbar, und es gilt

:::formel Satz
$$-\Delta u = f \quad\text{in } \mathbb{R}^3, \qquad u(\vec x)\to0 \quad\text{für } \lvert\vec x\rvert\to\infty.$$
:::

**So liest man das:** $\Delta$ ist der Laplace-Operator aus dem Artikel
[Divergenz, Rotation und Laplace-Operator](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/divergenz-rotation-laplace.html),
die Divergenz des Gradienten. Weil das Feld der
negative Gradient ist, sagt die Gleichung: Die Quelldichte des Felds $\vec E=-\nabla u$ ist die Ladungsdichte. Die Bedingung im
Unendlichen legt die Lösung fest; ohne sie könnte man etwa eine Konstante addieren.

In der Elektrostatik ist das Potential einer Ladungsdichte $f$ das Newtonpotential geteilt durch die Feldkonstante
$\varepsilon_0$; die Gleichung lautet dann mit $\frac{f}{\varepsilon_0}$ auf der rechten Seite. In der Gravitation ist es $-4\pi G$ mal
das Newtonpotential der Massendichte. Physiker fassen den Satz kurz so zusammen: Minus der Laplace-Operator des Kerns $g$
ist eine Punktquelle der Stärke $1$ im Ursprung, die Dirac-Distribution, die der Artikel
[Dirac-Scharen und die δ-Distribution](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/fourier-reihen/dirac-scharen-und-delta-distribution.html)
genauer erklärt.

**Im Bild:** Wo Körnchen sitzen, ist das Potential eine Kuppe — höher als der Durchschnitt seiner Umgebung. Nach dem Artikel
über Divergenz und Rotation misst der Laplace-Operator genau diesen Unterschied, und je dichter die Körnchen, desto stärker die Kuppe.

:::herleitung
**Für kugelsymmetrische Wolken vollständig.** Nach dem Artikel über Divergenz und Rotation hat ein radiales Feld mit dem
Profil $v$ die Divergenz

$$\operatorname{div}\big(v(a)\,\vec e_r\big) = v'(a)+\frac{2}{a}\,v(a) = \frac{1}{a^2}\big(a^2v(a)\big)'.$$

Mit dem Feld aus der Formel oben, also dem Profil $\frac{q(a)}{4\pi a^2}$, und weil die Ableitung von $q$ nach dem Hauptsatz
$4\pi\rho(a)\,a^2$ ist, folgt an jeder Stetigkeitsstelle des Profils

$$-\Delta u = \operatorname{div}\vec E = \frac{1}{a^2}\Big(\frac{q(a)}{4\pi}\Big)' = \frac{1}{a^2}\,\rho(a)\,a^2 = \rho(a) = f(\vec x).$$

**Im allgemeinen Fall** folgt hier nur die Beweisidee, in drei Schritten:

- **Glatt.** Mit $\vec y=\vec x-\vec z$ steht $\vec x$ nur noch in der Dichte: $u$ ist das Integral von $g(\vec z)\,f(\vec x-\vec z)$ über $\vec z$.
  Ableitungen nach $\vec x$ fallen auf $f$; weil $g$ integrierbar ist und die Ableitungen von $f$ beschränkt sind, darf man nach
  dem Artikel über uneigentliche Parameterintegrale unter dem Integral ableiten. So ist $u$ stetig differenzierbar.
- **Fluss.** Das Feld $\vec E=-\nabla u$ ist die Überlagerung der Coulomb-Felder aller Körnchen. Durch die Oberfläche einer Kugel
  fließt aus dem Feld eines Körnchens seine Ladung heraus, wenn es innen sitzt — auf einer Kugel um das Körnchen ist der
  Betrag des Felds Ladung durch $4\pi$ mal Radiusquadrat, die Oberfläche $4\pi$ mal Radiusquadrat —, und nichts, wenn es außen
  sitzt. Der Fluss von $\vec E$ durch die Kugeloberfläche ist also die Ladung in der Kugel — das Gaußsche Gesetz.
- **Dichte.** Teilt man durch das Volumen der Kugel und lässt sie auf $\vec x$ schrumpfen, wird links die Divergenz von $\vec E$ —
  die Quelldichte, wie in der Ebene im Artikel über die
  [Integralsätze in der Ebene](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/integralsaetze-in-der-ebene.html) —,
  rechts $f(\vec x)$.

Was fehlt, sind die Flussrechnung im Raum, die der
[Satz von Gauß im Raum](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/satz-von-gauss-im-raum.html)
liefert, und der
Nachweis, dass $u$ sogar zweimal stetig differenzierbar ist. Dafür braucht man feinere Abschätzungen; hier kommt die
Voraussetzung ins Spiel, dass $f$ stetig differenzierbar ist.
:::

:::grafik
Szene: hoema3/koordinatentransformationen/03-fluss-aus-kugel · Vorlage: fluss-kugel-3d
Eine kleine Kugel um einen Messort in einer Körnchenwolke; aus ihrer Oberfläche treten Feldpfeile aus. Körnchen innerhalb der
Kugel leuchten auf, und ein Zähler zeigt ihre Ladung; ein zweiter Zähler zeigt den Fluss durch die Oberfläche — beide sind
gleich. Ein Körnchen außerhalb wird markiert: Sein Feld tritt auf einer Seite ein und auf der anderen aus, sein Beitrag zum
Fluss ist null. Ein Regler schrumpft die Kugel; der Quotient aus Fluss und Volumen nähert sich der Dichte am Messort.
Kernaussage: Was aus einer kleinen Kugel herausfließt, ist die Ladung darin — daraus wird die Poisson-Gleichung. (Rot =
Körnchen innen, grau = Körnchen außen, blau = Kugel und Feldpfeile, orange = Zähler.)
:::

::::beispiel Eine glatte Wolke zum Nachrechnen
Die Dichte

$$f(\vec y) = \big(1-\lvert\vec y\rvert^2\big)^2 \quad\text{für } \lvert\vec y\rvert\le1, \qquad f(\vec y) = 0 \quad\text{sonst},$$

ist stetig differenzierbar mit kompaktem Träger: Am Rand der Einheitskugel sind sie und ihr Gradient null. Sie erfüllt alle
Voraussetzungen des Satzes. Ihr Profil ist $(1-r^2)^2$, und die eingeschlossene Ladung ist für $a\le1$

$$\frac{q(a)}{4\pi} = \int_0^a\big(1-r^2\big)^2r^2\,dr = \frac{a^3}{3}-\frac{2a^5}{5}+\frac{a^7}{7}, \qquad \frac{Q}{4\pi} = \frac13-\frac25+\frac17 = \frac{8}{105}.$$

Die Formel für kugelsymmetrische Wolken gibt das Potential

$$h(a) = \frac16-\frac{a^2}{6}+\frac{a^4}{10}-\frac{a^6}{42} \quad\text{für } a\le1, \qquad h(a) = \frac{8}{105\,a} \quad\text{für } a\ge1.$$

**Die Probe.** Bei $a=1$ geben beide Stücke $\frac{8}{105}$, und auch die ersten beiden Ableitungen stimmen dort überein — $u$ ist
zweimal stetig differenzierbar. Innen ist nach der radialen Formel für die Divergenz

$$-\Delta u = \frac{1}{a^2}\Big(\frac{a^3}{3}-\frac{2a^5}{5}+\frac{a^7}{7}\Big)' = 1-2a^2+a^4 = \big(1-a^2\big)^2,$$

genau die Dichte, und außen ist $\frac{8}{105\,a}$ harmonisch. Für großes $a$ geht das Potential gegen null; im Mittelpunkt und
am Rand ist es

$$h(0) = \frac16\approx0{,}167, \qquad h(1) = \frac{8}{105}\approx0{,}076.$$

**Im Bild:** Die Wolke ist in der Mitte am dichtesten, und dort ist die Kuppe des Potentials am stärksten gekrümmt. Am Rand
läuft die Dichte sanft aus, und die Kuppe geht ohne Knick in den Abfall einer Punktladung über.
::::

## Bedeutung und Ausblick

Das Newtonpotential beantwortet die Grundfrage der Elektrostatik und der Gravitation: Welches Potential erzeugt eine gegebene
Ladung? Die Antwort ist die Überlagerung der Coulomb-Potentiale, und sie löst die Poisson-Gleichung. In der Elektrotechnik
steckt das in jeder Feldberechnung — bei Raumladungszonen in Halbleitern, bei geladenen Elektroden und bei der Frage, warum das
Feld in einer gleichmäßig geladenen Kugelschale verschwindet.

Für kugelsymmetrische Wolken reichte das radiale Profil. Wie der Laplace-Operator in Kugel- und Zylinderkoordinaten allgemein
aussieht, zeigt der nächste Artikel über krummlinige Koordinaten. Mit den Integralsätzen im Raum wird die Flussrechnung hinter
dem Gaußschen Gesetz zum Beweis, im Artikel
[Poisson-Gleichung und Hauptsatz der Vektoranalysis](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/poisson-gleichung-und-hauptsatz-der-vektoranalysis.html).

:::kern
- Ein __singuläres Parameterintegral__ $\int k(\vec x-\vec y)\,f(\vec y)\,d^ny$ versteht man, indem man die Singularität ausschneidet und den Schnitt schrumpfen lässt.
- Das __Newtonpotential__ $u(\vec x)=\frac{1}{4\pi}\int\frac{f(\vec y)}{\lvert\vec x-\vec y\rvert}\,d^3y$ ist die Summe der Coulomb-Potentiale aller Körnchen.
- Es existiert trotz der Singularität: Die Körnchen nahe dem Messort sind zu wenige, ihr Beitrag ist höchstens Schranke mal halbes Radiusquadrat.
- Von weitem wirkt jede Wolke wie eine Punktladung $Q$; das Potential geht im Unendlichen gegen null.
- Kugelsymmetrisch: Die innere Ladung wirkt wie eine Punktladung im Mittelpunkt, jede äußere Schale ist nur ein Sockel.
- __Schalentheorem__: von außen wie eine Punktladung, im Hohlraum konstantes Potential und kein Feld.
- __Gaußsches Gesetz__ für kugelsymmetrische Wolken: $\vec E=\frac{q(a)}{4\pi a^2}\,\vec e_r$ mit der eingeschlossenen Ladung $q(a)$.
- __Poisson-Gleichung__: $-\Delta u=f$, und im Unendlichen verschwindet das Potential — die Quelldichte des Felds ist die Ladungsdichte.
- Beweisidee: Was aus einer kleinen Kugel herausfließt, ist die Ladung darin; für kugelsymmetrische Wolken ist die Rechnung vollständig.
:::

:::quiz
F: Was ist die Grundidee des Newtonpotentials?
A: Superposition: Man zerlegt die Ladung in winzige Körnchen mit der Ladung $f(\vec y)\,d^3y$. Jedes trägt sein Coulomb-Potential, Ladung durch $4\pi$ mal Abstand, bei, und die Summe — im Grenzfall das Integral $\frac{1}{4\pi}\int\frac{f(\vec y)}{\lvert\vec x-\vec y\rvert}\,d^3y$ — ist das Potential der Wolke.
F: Warum existiert das Newtonpotential, obwohl ein Körnchen am Messort den Abstand null hat?
A: In einer kleinen Kugel um den Messort ist der Integrand höchstens $\frac{b}{4\pi\lvert\vec x-\vec y\rvert}$, eine Singularität mit dem Exponenten $1$, und nach dem Satz über singuläre Integranden integrierbar. Der Beitrag dieser Kugel ist höchstens $\frac{b\delta^2}{2}$: Die nahen Körnchen haben zwar viel Gewicht, aber es sind zu wenige — bei der Dichte $1$ und dem Radius $0{,}1$ höchstens $0{,}005$.
F: Wie sieht eine Wolke von weitem aus, und warum geht ihr Potential im Unendlichen gegen null?
A: Wie eine Punktladung $Q$ im Ursprung: Der Unterschied zu $\frac{Q}{4\pi\lvert\vec x\rvert}$ ist höchstens $\frac{R_0}{\lvert\vec x\rvert-R_0}$ mal $\frac{1}{4\pi\lvert\vec x\rvert}\int\lvert f\rvert$, weil sich die Abstände der Körnchen nach der Dreiecksungleichung höchstens um $R_0$ unterscheiden. Bei zwei Kügelchen im Abstand $10$ ist der Fehler etwa ein Prozent, die Schranke $11$ Prozent.
F: Warum hängt das Potential einer kugelsymmetrischen Wolke nur vom Abstand ab?
A: Eine Drehung ändert weder die Wolke noch Abstände. Substituiert man $\vec y=A\vec w$ mit der Drehmatrix $A$, ist der Betrag der Jacobi-Determinante $1$, und der Transformationssatz gibt $u(A\vec x)=u(\vec x)$. Punkte mit gleichem Abstand gehen durch Drehungen ineinander über.
F: Was besagt die Formel für das Potential kugelsymmetrischer Wolken, und wie entsteht sie?
A: $h(a)=\frac1a\int_0^a\rho\,r^2\,dr+\int_a^\infty\rho\,r\,dr$: Die Ladung innerhalb des Radius $a$ wirkt wie eine Punktladung im Mittelpunkt, jede äußere Schale ist ein fester Sockel. Man legt den Messort auf die $z$-Achse, nimmt Kugelkoordinaten und den Kosinussatz; das Winkelintegral gibt mit $s=\cos\theta$ den Wert $\frac{2}{\max(a,r)}$.
F: Was besagt Newtons Schalentheorem, und was ergibt sich für die gleichmäßig geladene Kugelschale?
A: Von außen wirkt eine kugelsymmetrische Wolke wie eine Punktladung $Q$ im Mittelpunkt, in einem Hohlraum ist das Potential konstant und das Feld null. Für die Schale mit der Dichte $\rho$ ist außen $h(a)=\rho\frac{R_2^3-R_1^3}{3a}=\frac{Q}{4\pi a}$ und im Hohlraum $\rho\frac{R_2^2-R_1^2}{2}$. Von außen kann man nicht unterscheiden, ob die Ladung verteilt oder im Mittelpunkt gebündelt ist.
F: Wie groß ist das Feld einer kugelsymmetrischen Wolke, und warum tragen die äußeren Schalen nichts bei?
A: $\vec E=\frac{q(a)}{4\pi a^2}\vec e_r$ mit der eingeschlossenen Ladung $q(a)$ — das Gaußsche Gesetz. Leitet man das Profil ab, heben sich die beiden Terme mit $\rho(a)$ weg; die äußeren Schalen liefern nur einen Sockel, dessen Gradient null ist. Newton sah es geometrisch: Die Flächen der Schalenstücke wachsen mit dem Abstandsquadrat, die Kräfte fallen damit.
F: Was folgt aus dem Schalentheorem für die Erde?
A: An der Oberfläche wirkt die ganze Masse wie ein Punkt: $g=\frac{GM}{R^2}\approx9{,}82\,\frac{\mathrm{m}}{\mathrm{s}^2}$. Im Inneren einer gleichmäßig dichten Erde ist die eingeschlossene Masse proportional zu $a^3$, die Beschleunigung also proportional zu $a$ — auf halbem Weg rund $4{,}9\,\frac{\mathrm{m}}{\mathrm{s}^2}$. Ein Körper in einem Tunnel durch den Mittelpunkt schwingt harmonisch und ist nach etwa $42$ Minuten auf der anderen Seite.
F: Was besagt die Poisson-Gleichung, und wie beweist man sie?
A: $-\Delta u=f$ mit $u\to0$ im Unendlichen: Die Quelldichte des Felds $-\nabla u$ ist die Ladungsdichte, und wo Ladung sitzt, ist das Potential eine Kuppe. Für kugelsymmetrische Wolken folgt das aus der radialen Divergenz $\frac{1}{a^2}(a^2v)'$ des Felds mit dem Profil $v=\frac{q(a)}{4\pi a^2}$. Allgemein ist die Idee das Gaußsche Gesetz: Was aus einer kleinen Kugel herausfließt, ist die Ladung darin; die Einzelheiten liefern der Satz von Gauß im Raum und feinere Abschätzungen.
F: Wie prüft man den Satz an der glatten Wolke $(1-\lvert\vec y\rvert^2)^2$?
A: Die eingeschlossene Ladung ist $4\pi(\frac{a^3}{3}-\frac{2a^5}{5}+\frac{a^7}{7})$, das Potential innen $\frac16-\frac{a^2}{6}+\frac{a^4}{10}-\frac{a^6}{42}$ und außen $\frac{8}{105a}$. Bei $a=1$ passen Wert und zwei Ableitungen zusammen, innen ergibt $\frac{1}{a^2}(\frac{q}{4\pi})'$ genau $(1-a^2)^2$, außen ist das Potential harmonisch und geht gegen null.
:::
