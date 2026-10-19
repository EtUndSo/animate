---
title: Der Satz von Gauß im Raum
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050300
summary: Von Grund auf – der Satz von Gauß (Divergenzsatz) verknüpft das Volumenintegral der Divergenz eines Vektorfelds mit dem Fluss durch die Randfläche, $\int_V \operatorname{div}F\,dx=\int_{\partial V}F\cdot dS=\int_{\partial V}F\cdot n\,d\sigma$ (äußere Normale). Er entsteht aus der partiellen Integration im Raum und liefert die anschauliche Deutung der Divergenz als Quelldichte sowie die Greenschen Formeln.
tags: Satz von Gauß, Divergenzsatz, partielle Integration, Divergenz, Flussintegral, äußere Normale, Quelldichte, Greensche Formel
---

:::grafik
Einstiegs-Animation: Ein Raumbereich $V$ (z. B. eine Kugel), in dessen Innerem ein Vektorfeld $F$ __Quellen__ und
__Senken__ hat — angedeutet durch kleine Pfeile, die auseinanderlaufen ($\operatorname{div}F>0$) oder zusammenlaufen
($\operatorname{div}F<0$). Die gesamte „Quellstärke" im Volumen, $\int_V\operatorname{div}F\,dx$, tritt als
__Nettofluss__ durch die Randfläche $\partial V$ nach außen aus — Pfeile, die die Hülle mit nach außen zeigender
Normale $n$ durchstoßen. Kernbotschaft (Gauß): Was im Inneren an Quellen entsteht, muss durch die Hülle hinaus —
__Volumenintegral der Divergenz = Fluss durch den Rand__.
:::

:::konzept
Der Satz von Stokes hat Fläche und Randkurve über die __Rotation__ verbunden. Der __Satz von Gauß__ (Divergenzsatz)
macht das eine Dimension höher: Er verknüpft ein **Volumen** mit seiner **Randfläche** — über die __Divergenz__. Die
Idee ist eine **Bilanz**: Die Divergenz $\operatorname{div}F$ ist die lokale Quelldichte (wie viel Feld „entspringt"
pro Volumen), und ihr Integral über $V$ muss gleich dem sein, was netto durch die Hülle $\partial V$ hinausströmt. Das
ist der mathematische Kern des Gaußschen Gesetzes der Elektrostatik, der Kontinuitätsgleichung und der gesamten
Potentialtheorie. Werkzeug dahinter ist die __partielle Integration im Raum__.
:::

**Worum es geht:** Wir leiten die __partielle Integration im Raum__ her, lokalisieren sie zum __Satz von Gauß__
$\int_V\operatorname{div}F\,dx=\int_{\partial V}F\cdot dS$, deuten die __Divergenz als Quelldichte__ und gewinnen die
__Greenschen Formeln__.

## Partielle Integration im Raum

Ausgangspunkt ist die partielle Integration im $\mathbb{R}^n$. Für stetig differenzierbare $f,g:\mathbb{R}^n\to
\mathbb{R}$, von denen **mindestens eine kompakten Träger** hat (damit am Rand im Unendlichen nichts übrig bleibt),
gilt komponentenweise

$$\int_{\mathbb{R}^n}\frac{\partial f}{\partial x_k}(x)\,g(x)\,dx = -\int_{\mathbb{R}^n} f(x)\,\frac{\partial g}{\partial x_k}(x)\,dx.$$

Das ist die Produktregel $\partial_k(fg)=(\partial_k f)g+f(\partial_k g)$, integriert — der Term $\int\partial_k(fg)\,
dx$ verschwindet wegen des kompakten Trägers. Auf Vektorfelder angewandt ergibt sich daraus die __partielle Integration
im Raum__ (Satz 5.16): für stetig differenzierbares $E:\mathbb{R}^n\to\mathbb{R}^n$ und $\varphi:\mathbb{R}^n\to
\mathbb{R}$ (eines mit kompaktem Träger)

$$\int_{\mathbb{R}^n}(\operatorname{div}E)(x)\,\varphi(x)\,dx = -\int_{\mathbb{R}^n} E(x)\cdot\nabla\varphi(x)\,dx.$$

Die Ableitung wandert vom Feld $E$ (dort als Divergenz) auf die Testfunktion $\varphi$ (dort als Gradient), mit einem
Vorzeichenwechsel — genau wie im Eindimensionalen.

## Lokalisierung: der Weg zum Rand

Wie bringt man einen **Rand** ins Spiel? Man ersetzt $\varphi$ durch die __Indikatorfunktion__ $\mathbf{1}_V$ eines
Bereichs $V$ ($\mathbf{1}_V(x)=1$ für $x\in V$, sonst $0$). Dann ist formal

$$\int_V\operatorname{div}E(x)\,dx = \int_{\mathbb{R}^3}\operatorname{div}E(x)\,\mathbf{1}_V(x)\,dx.$$

$\mathbf{1}_V$ ist aber am Rand $\partial V$ unstetig — Satz 5.16 ist nicht direkt anwendbar. Der „Gradient" von
$\mathbf{1}_V$ **konzentriert sich am Rand** und zeigt ins Innere; formal $\nabla\mathbf{1}_V\,dx \sim -dS$. Setzt man
das in die partielle Integration ein, geht der Volumenterm $-\int E\cdot\nabla\mathbf{1}_V\,dx$ in ein **Randintegral**
$\int_{\partial V}E\cdot dS$ über. Bei glattem Rand macht man dieses formale Argument streng — und erhält den Satz von
Gauß.

## Der Satz von Gauß

**Satz von Gauß (Divergenzsatz, Satz 5.17).** Sei $V\subset\mathbb{R}^3$ beschränkt und abgeschlossen mit **glattem
Rand** und $F:U\to\mathbb{R}^3$ stetig differenzierbar in einer Umgebung $U$ von $V$. Dann gilt

$$\int_V \operatorname{div}F(x)\,dx = \int_{\partial V} F\cdot dS = \int_{\partial V} F\cdot n\,d\sigma,$$

wobei $\partial V$ durch das **äußere** Einheitsnormalenfeld $n$ orientiert ist ($dS=n\,d\sigma$). Links die
aufsummierte Quellstärke im Inneren, rechts der Nettofluss durch die Hülle — die beiden sind **gleich**.

:::grafik
Links ein Volumen $V$ mit Divergenzfeld (Quellen rot, Senken blau); rechts dieselbe Hülle $\partial V$ mit überall
nach außen zeigender Normale $n$ und den durchstoßenden Flusspfeilen. Beschriftung $\int_V\operatorname{div}F\,dx=
\int_{\partial V}F\cdot n\,d\sigma$; Hinweis „äußere Normale".
:::

## Divergenz als Quelldichte

Der Satz liefert rückwärts die **anschauliche Bedeutung der Divergenz**. Zieht man $V$ auf einen Punkt $x$ zusammen,
folgt

$$\operatorname{div}F(x) = \lim_{V\downarrow x}\frac{1}{\operatorname{vol}(V)}\int_{\partial V}F\cdot n\,d\sigma$$

— die Divergenz ist der **Fluss pro Volumen**, also die lokale Quelldichte. In der Physik ist das die Form des
__Gaußschen Gesetzes__: $\operatorname{div}E=\rho/\varepsilon_0$ bedeutet integriert $\oint_{\partial V}E\cdot dS=
Q_\text{innen}/\varepsilon_0$ — der elektrische Fluss durch eine geschlossene Hülle misst die eingeschlossene Ladung.

**Eigenes Beispiel.** Für das radiale Feld $F(x)=x$ (Ortsvektor) ist $\operatorname{div}F=\partial_x x+\partial_y y+
\partial_z z=3$. Gauß über die Kugel $V=B_R(0)$ gibt links $\int_{B_R}3\,dx=3\cdot\tfrac{4}{3}\pi R^3=4\pi R^3$. Rechts
ist auf $\partial B_R$ die äußere Normale $n=x/R$, also $F\cdot n=x\cdot x/R=R$, und $\int_{\partial B_R}R\,d\sigma=R\cdot
4\pi R^2=4\pi R^3$ — beide Seiten stimmen überein.

## Die Greenschen Formeln

Als Folgerung erhält man die partielle Integration **mit Rand** (Satz 5.18): für stetig differenzierbare $E:U\to
\mathbb{R}^3$, $\varphi:U\to\mathbb{R}$ auf einem glatt berandeten $V$ gilt

$$\int_V E\cdot\nabla\varphi\,dx = \int_{\partial V}\varphi\,E\cdot dS - \int_V (\operatorname{div}E)\,\varphi\,dx.$$

Das ist einfach Gauß, angewandt auf das Produktfeld $\varphi E$ (denn $\operatorname{div}(\varphi E)=\nabla\varphi\cdot
E+\varphi\operatorname{div}E$). Mit der Spezialwahl $E=\nabla u$ (also $\operatorname{div}E=\Delta u$) wird daraus die
__erste Greensche Formel__

$$\int_V \nabla u\cdot\nabla\varphi\,dx = \int_{\partial V}\varphi\,\frac{\partial u}{\partial n}\,d\sigma - \int_V \varphi\,\Delta u\,dx,$$

wobei $\tfrac{\partial u}{\partial n}=\nabla u\cdot n$ die Normalableitung ist. Vertauscht man $u$ und $\varphi$ und
subtrahiert, heben sich die symmetrischen Gradiententerme weg und man bekommt die __zweite Greensche Formel__
$\int_V(\varphi\Delta u-u\Delta\varphi)\,dx=\int_{\partial V}\big(\varphi\tfrac{\partial u}{\partial n}-u\tfrac{\partial
\varphi}{\partial n}\big)\,d\sigma$ — das Arbeitspferd der Potentialtheorie.

**Stolperstein:** (1) **Äußere** Normale — $n$ zeigt aus $V$ hinaus; mit innerer Normale kehrt sich das Vorzeichen um.
(2) Der Rand muss **glatt** (bzw. stückweise glatt) sein; Ecken/Kanten eines Quaders behandelt man flächenweise.
(3) $\operatorname{div}F$ ist eine **Skalar**funktion (Volumenintegral), $F\cdot n$ eine Skalargröße auf der Fläche —
auf beiden Seiten steht am Ende eine Zahl, kein Vektor.

:::kern
__Partielle Integration im Raum__ (Satz 5.16): $\int_{\mathbb{R}^n}(\operatorname{div}E)\varphi\,dx=-\int_{\mathbb{R}^n}
E\cdot\nabla\varphi\,dx$ (eines mit kompaktem Träger; aus Produktregel). __Satz von Gauß__ (Satz 5.17): für glatt
berandetes $V\subset\mathbb{R}^3$ und $C^1$-Feld $F$ gilt $\int_V\operatorname{div}F\,dx=\int_{\partial V}F\cdot dS=
\int_{\partial V}F\cdot n\,d\sigma$ mit **äußerer** Normale ($dS=n\,d\sigma$): Quellstärke im Volumen = Nettofluss durch
die Hülle. Daraus __Divergenz als Quelldichte__ $\operatorname{div}F(x)=\lim_{V\downarrow x}\frac{1}{\operatorname{vol}
V}\int_{\partial V}F\cdot n\,d\sigma$ (physik. Gaußsches Gesetz $\oint E\cdot dS=Q/\varepsilon_0$). __Partielle
Integration mit Rand__ (Satz 5.18): $\int_V E\cdot\nabla\varphi\,dx=\int_{\partial V}\varphi\,E\cdot dS-\int_V
(\operatorname{div}E)\varphi\,dx$; mit $E=\nabla u$ die __erste Greensche Formel__ $\int_V\nabla u\cdot\nabla\varphi\,dx
=\int_{\partial V}\varphi\,\partial_n u\,d\sigma-\int_V\varphi\,\Delta u\,dx$ (und daraus die zweite). Beispiel $F=x$:
$\operatorname{div}F=3$, beide Seiten $=4\pi R^3$ über $B_R$.
:::

Gauß und Stokes sind die beiden räumlichen Integralsätze. Zum Abschluss des Kapitels wenden wir sie auf die
__Poisson-Gleichung__ an (das Newtonpotential als Greensche Funktion) und beweisen den __Hauptsatz der
Vektoranalysis__ (Helmholtz-Zerlegung) — das Thema des nächsten Artikels.

:::quiz
F: Was ist die physikalische Grundidee hinter dem Satz von Gauß, in einem Satz?
A: Es ist eine Bilanz: Was im Inneren eines Volumens an Feld „entspringt" (die aufsummierte Quelldichte), muss netto durch die Hülle nach außen strömen. Deshalb ist das Volumenintegral der Divergenz gleich dem Fluss durch die Randfläche.
F: Woher stammt das Minuszeichen in der partiellen Integration $\int(\operatorname{div}E)\varphi=-\int E\cdot\nabla\varphi$?
A: Es kommt aus der Produktregel $\partial_k(fg)=(\partial_k f)g+f(\partial_k g)$: Integriert man diese, verschwindet $\int\partial_k(fg)$ wegen des kompakten Trägers, und die beiden übrigen Terme stehen mit umgekehrtem Vorzeichen gegenüber — die Ableitung wandert mit Vorzeichenwechsel auf den anderen Faktor.
F: Wozu braucht man bei der randlosen partiellen Integration, dass eine Funktion kompakten Träger hat?
A: Damit beim Integrieren der Produktregel über den ganzen Raum kein „Randterm im Unendlichen" übrig bleibt. Der kompakte Träger sorgt dafür, dass $fg$ außerhalb eines beschränkten Gebiets null ist und $\int\partial_k(fg)\,dx=0$ gilt.
F: Wie entsteht aus der randlosen Formel ein Randintegral — wie bringt man den Rand überhaupt ins Spiel?
A: Man setzt für die Testfunktion die Indikatorfunktion $\mathbf 1_V$ des Bereichs ein. Ihr „Gradient" konzentriert sich am Rand $\partial V$ und zeigt nach innen ($\nabla\mathbf 1_V\,dx\sim -dS$), sodass der Volumenterm $-\int E\cdot\nabla\mathbf 1_V$ in das Flächenintegral $\int_{\partial V}E\cdot dS$ übergeht.
F: Warum muss die Normale im Satz von Gauß die äußere sein, und was passiert bei der inneren?
A: Die äußere Normale zählt das, was aus $V$ hinausströmt, positiv — das entspricht der Quellbilanz. Wählt man die innere Normale, dreht sich das Vorzeichen jedes Flusses um und die Gleichung stimmt nur noch mit einem Minuszeichen.
F: Wie liefert der Satz von Gauß die anschauliche Deutung der Divergenz als Quelldichte?
A: Zieht man $V$ auf einen Punkt zusammen, wird $\operatorname{div}F(x)=\lim_{V\downarrow x}\frac{1}{\operatorname{vol}V}\int_{\partial V}F\cdot n\,d\sigma$ — also Fluss pro Volumen. Die Divergenz an einem Punkt misst damit, wie stark das Feld dort lokal „quillt" oder „versickert".
F: Wie wird das physikalische Gaußsche Gesetz $\oint E\cdot dS=Q_{\text{innen}}/\varepsilon_0$ zum Spezialfall des Divergenzsatzes?
A: Setzt man $\operatorname{div}E=\rho/\varepsilon_0$ in den Satz von Gauß ein, wird das Volumenintegral $\int_V\rho/\varepsilon_0\,dx=Q_{\text{innen}}/\varepsilon_0$, und die rechte Seite ist genau der Fluss $\oint_{\partial V}E\cdot dS$. Der elektrische Fluss durch eine Hülle misst also die eingeschlossene Ladung.
F: Warum ergeben beim Feld $F(x)=x$ über der Kugel $B_R$ beide Seiten $4\pi R^3$?
A: Links ist $\operatorname{div}F=3$, also $\int_{B_R}3\,dx=3\cdot\frac43\pi R^3=4\pi R^3$. Rechts ist auf der Sphäre $n=x/R$, also $F\cdot n=|x|^2/R=R$, und $\int_{\partial B_R}R\,d\sigma=R\cdot4\pi R^2=4\pi R^3$ — die Quellbilanz geht exakt auf.
F: Wie gewinnt man die Greenschen Formeln aus dem Satz von Gauß?
A: Man wendet Gauß auf das Produktfeld $\varphi E$ an ($\operatorname{div}(\varphi E)=\nabla\varphi\cdot E+\varphi\operatorname{div}E$) und erhält die partielle Integration mit Rand. Mit der Spezialwahl $E=\nabla u$ (also $\operatorname{div}E=\Delta u$) folgt daraus direkt die erste Greensche Formel.
F: Warum fallen beim Übergang zur zweiten Greenschen Formel die Gradiententerme weg?
A: Man schreibt die erste Greensche Formel einmal mit $(u,\varphi)$ und einmal vertauscht mit $(\varphi,u)$ und subtrahiert. Der Term $\int\nabla u\cdot\nabla\varphi$ ist symmetrisch und tritt in beiden gleich auf, hebt sich also heraus — übrig bleibt die symmetrische Beziehung zwischen $\varphi\Delta u-u\Delta\varphi$ und den Normalableitungen am Rand.
:::
