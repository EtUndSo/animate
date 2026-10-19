---
title: Unabhängigkeit von Zufallsvariablen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3080500
summary: Von Grund auf – zwei Zufallsvariablen sind unabhängig, wenn ihre gemeinsame Verteilung faktorisiert, $F_{X,Y}(x,y)=F_X(x)F_Y(y)$ (bzw. Dichte/Wahrscheinlichkeitsfunktion als Produkt). Die Schlüsselfolge: $E(XY)=E(X)E(Y)$, also $\mathrm{Cov}=0$ und $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$. Unabhängig impliziert unkorreliert, aber nicht umgekehrt – ein zentrales Missverständnis, das die zweidimensionale Normalverteilung aufklärt.
tags: Unabhängigkeit, gemeinsame Verteilung, Randdichte, Produkteigenschaft, unkorreliert, Kovarianz, zweidimensionale Normalverteilung, Zufallsvektor
---

:::grafik
Einstiegs-Animation: Zwei Zufallsvariablen $X,Y$ zusammen als Punktwolke in der Ebene (der __Zufallsvektor__
$(X,Y)$). Bei __Unabhängigkeit__ zerfällt die gemeinsame Dichte in ein **Produkt** — das Streubild ist ein
„Rechteck-Muster" ohne Vorzugsrichtung, die __Randdichten__ $f_X,f_Y$ entstehen durch Projektion auf die Achsen.
Rechts der Kontrast: eine gekippte, zigarrenförmige Wolke (Korrelation $\rho\neq0$) — dieselben Randverteilungen,
aber $X$ und $Y$ **abhängig**. Darunter die Kette der Konsequenzen: $F_{X,Y}=F_XF_Y\Rightarrow E(XY)=E(X)E(Y)\Rightarrow
\mathrm{Cov}=0\Rightarrow\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$. Kernbotschaft: Unabhängigkeit heißt
faktorisierende Verteilung — und erst sie macht Varianzen additiv.
:::

:::konzept
Die __Unabhängigkeit von Zufallsvariablen__ überträgt die Unabhängigkeit von Ereignissen auf Zahlen: Das Wissen über
$X$ sagt nichts über $Y$. Mathematisch heißt das, die __gemeinsame Verteilung faktorisiert__ in das Produkt der
Einzelverteilungen. Die eine Konsequenz, auf die alles hinausläuft, ist die __Produkteigenschaft__
$E(XY)=E(X)E(Y)$ — denn daraus folgt sofort $\mathrm{Cov}(X,Y)=0$ und damit die **Additivität der Varianz**
$\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$. Genau diese Additivität ist der Motor der nächsten beiden
Artikel (Gesetz der großen Zahlen, zentraler Grenzwertsatz). Zugleich klärt dieser Artikel ein hartnäckiges
Missverständnis: __unabhängig__ ist strikt stärker als __unkorreliert__.
:::

**Worum es geht:** Wir definieren die __Unabhängigkeit__ über die __gemeinsame Verteilungsfunktion__, zeigen die
__Produkteigenschaft__ $E(XY)=E(X)E(Y)$ und ihre Folgen, trennen __unabhängig__ von __unkorreliert__ (Lemma 8.41) und
behandeln den diskreten (Satz 8.43) und absolut-stetigen Fall (__Randdichten__, Satz 8.45) bis zur
__zweidimensionalen Normalverteilung__.

## Gemeinsame Verteilung und Unabhängigkeit

Für $X,Y$ auf einem gemeinsamen Raum und $x,y\in\mathbb R$ setzt man $A_x=\{X\le x\}$, $B_y=\{Y\le y\}$. Die
__gemeinsame Verteilungsfunktion__ des __Zufallsvektors__ $(X,Y)$ ist
$$F_{X,Y}(x,y)=P(X\le x,\ Y\le y)=P(A_x\cap B_y).$$
$X$ und $Y$ heißen __stochastisch unabhängig__, wenn $A_x$ und $B_y$ für **alle** $x,y$ unabhängige Ereignisse sind,
also
$$F_{X,Y}(x,y)=F_X(x)\,F_Y(y)\qquad\text{für alle }(x,y)\in\mathbb R^2.$$
Die gemeinsame Verteilung ist dann vollständig durch die beiden Einzelverteilungen bestimmt — kein „Zusammenhang"
bleibt übrig.

__Beispiel 8.39.__ Auf $\Omega=[0,1]^2$ mit $P(M)=$ Flächeninhalt sei $X(\omega)=g(s)$, $Y(\omega)=h(t)$ für
$\omega=(s,t)$ — jede Variable hängt nur von **einer** Koordinate ab. Dann ist $\{X\le x\}$ ein vertikaler Streifen,
$\{Y\le y\}$ ein horizontaler; solche Streifen sind unabhängig, also sind $X,Y$ unabhängig. Hier ist $P$ gerade das
Lebesgue-Maß $ds\,dt$, und weil $X$ nur von $s$ abhängt, ist $E(X)=\int_0^1 g(s)\,ds$ (die $t$-Integration ist
redundant), analog $E(Y)=\int_0^1 h(t)\,dt$.

## Die Produkteigenschaft und ihre Folgen

Im Beispiel rechnet man direkt
$$E(XY)=\int_0^1\!\!\int_0^1 g(s)h(t)\,ds\,dt=\Big(\int_0^1 g\,ds\Big)\Big(\int_0^1 h\,dt\Big)=E(X)E(Y),$$
weil das Doppelintegral eines Produkts getrennter Funktionen in ein Produkt zerfällt. Das ist kein Zufall des
Beispiels:

__Für unabhängige $X,Y$ gilt immer__
$$E(XY)=E(X)\,E(Y).$$
Im Allgemeinen hat der Erwartungswert **keine** Produkteigenschaft — sie ist eine Spezialität der Unabhängigkeit.
Daraus folgt sofort mit $\mathrm{Cov}(X,Y)=E(XY)-E(X)E(Y)$:
$$\mathrm{Cov}(X,Y)=0\quad\Longrightarrow\quad \mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$$
(nach Lemma 8.35). Die **Additivität der Varianz** unter Unabhängigkeit ist der Grund, warum das Mittel vieler
unabhängiger Messungen eine kleine Streuung hat — der Keim des Gesetzes der großen Zahlen.

## Unabhängig ist mehr als unkorreliert

__Definition 8.40.__ $X,Y$ mit $\mathrm{Cov}(X,Y)=0$ heißen __unkorreliert__.

__Lemma 8.41.__ Unabhängigkeit $\Rightarrow$ Unkorreliertheit, aber **nicht** umgekehrt. Unkorreliertheit erfasst nur
den **linearen** Zusammenhang (verschwindende Kovarianz); Unabhängigkeit verbietet **jeden** Zusammenhang.

__Beispiel 8.42 (unkorreliert, aber abhängig).__ Auf dem Laplace-Raum $\Omega=\{1,2,3\}$ sei $X(1)=-1$, $X(2)=0$,
$X(3)=1$ und $Y(1)=0$, $Y(2)=1$, $Y(3)=0$. Dann ist $XY\equiv0$, also $E(XY)=0$; außerdem $E(X)=0$, somit
$\mathrm{Cov}(X,Y)=0$ — **unkorreliert**. Aber $P(X\le-1,Y\le0)=\tfrac13$, während $P(X\le-1)P(Y\le0)=\tfrac13\cdot\tfrac23=\tfrac29$,
also $F_{X,Y}(-1,0)\neq F_X(-1)F_Y(0)$ — **nicht unabhängig**. ($Y=1$ erzwingt $X=0$: ein klarer, aber nicht-linearer
Zusammenhang.)

## Der diskrete Fall

__Satz 8.43.__ Diskrete $X,Y$ mit Werten $\{x_k\}$, $\{y_\ell\}$ sind genau dann unabhängig, wenn
$$P(X=x_k,\ Y=y_\ell)=P(X=x_k)\,P(Y=y_\ell)\qquad\text{für alle }k,\ell.$$
Dann zerfällt auch der Erwartungswert des Produkts: $E(XY)=\sum_{k,\ell}x_k y_\ell\,P(X=x_k,Y=y_\ell)=\big(\sum_k
x_k P(X=x_k)\big)\big(\sum_\ell y_\ell P(Y=y_\ell)\big)=E(X)E(Y)$ — die Produkteigenschaft folgt hier aus dem
Faktorisieren der Doppelsumme.

## Der absolut-stetige Fall und Randdichten

__Definition 8.44.__ Ein Zufallsvektor $(X,Y)$ heißt __absolut-stetig__ mit __gemeinsamer Dichte__ $f_{X,Y}\ge0$,
wenn $F_{X,Y}(x,y)=\int_{-\infty}^x\int_{-\infty}^y f_{X,Y}(s,t)\,ds\,dt$, mit Normierung $\int_{\mathbb R^2}
f_{X,Y}=1$.

__Satz 8.45.__ Besitzt $(X,Y)$ die Dichte $f_{X,Y}$, so gilt:
$$\text{(i) Randdichten}\quad f_X(x)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dy,\quad f_Y(y)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dx;$$
$$\text{(ii)}\quad X,Y\ \text{unabhängig}\ \Longleftrightarrow\ f_{X,Y}(x,y)=f_X(x)\,f_Y(y)\ \text{für alle }x,y.$$
Teil (i) ist „Ausintegrieren" der jeweils anderen Variablen (man vergisst $Y$, indem man über alle $y$
aufsummiert); Teil (ii) ist die Faktorisierung auf Ebene der Dichten. __Bemerkung 8.46:__ Sind $X,Y$ unabhängig mit
Dichten $f_X,f_Y$, so hat $(X,Y)$ die Produktdichte $f_Xf_Y$; abhängige absolut-stetige $X,Y$ müssen dagegen gar
keine gemeinsame Dichte besitzen. Und wieder: $E(XY)=\int\!\int xy\,f_{X,Y}\,dx\,dy=E(X)E(Y)$ bei Unabhängigkeit.

:::grafik
Links eine gemeinsame Dichte $f_{X,Y}(x,y)$ als Fläche über der Ebene; die Randdichten entstehen durch „Zusammen-
schieben" (Integrieren) entlang einer Achse. Rechts der Unabhängigkeitstest: zerfällt $f_{X,Y}$ in $f_X(x)\cdot
f_Y(y)$? Daneben zwei 2D-Normaldichten: $\rho=0$ (runde Glocke, unabhängig) vs. $\rho\neq0$ (gekippte Ellipse,
abhängig).
:::

## Beispiel: die zweidimensionale Normalverteilung

__Beispiel 8.47.__ Sind $X,Y\sim\mathcal N(0,1)$ unabhängig, so ist die gemeinsame Dichte das Produkt
$$f_{X,Y}(x,y)=\frac{1}{2\pi}\exp\!\Big(-\frac{x^2+y^2}{2}\Big)$$
— eine rotationssymmetrische „Glocke" über der Ebene (die Standard-2D-Normalverteilung).

__Beispiel 8.48 (korrelierter Fall).__ Für $0\le\rho<1$ sei
$$f_{X,Y}(x,y)=\frac{1}{2\pi\sqrt{1-\rho^2}}\exp\!\Big(-\frac{x^2-2\rho xy+y^2}{2(1-\rho^2)}\Big).$$
Durch **quadratische Ergänzung** und Substitution berechnet man die Randdichten zu $f_X(x)=\frac{1}{\sqrt{2\pi}}
e^{-x^2/2}$ und ebenso $f_Y$ — beide Komponenten sind also für **jedes** $\rho$ standard-normalverteilt. Trotzdem sind
$X$ und $Y$ **nur für $\rho=0$** unabhängig: Nur dann faktorisiert $f_{X,Y}=f_Xf_Y$ (der Mischterm $-2\rho xy$
verschwindet). Dieses Beispiel zeigt eindrücklich, dass gleiche Randverteilungen völlig verschiedene Abhängigkeits-
strukturen zulassen — und bei der Normalverteilung fällt „unkorreliert" ($\rho=0$) ausnahmsweise mit „unabhängig"
zusammen.

**Stolperstein:** (1) __Unabhängig $\neq$ unkorreliert__: Unabhängigkeit ⇒ $\mathrm{Cov}=0$, aber $\mathrm{Cov}=0$
erfasst nur linearen Zusammenhang (Beispiel 8.42). (2) Die Produkteigenschaft $E(XY)=E(X)E(Y)$ gilt **nur** bei
Unabhängigkeit (bzw. Unkorreliertheit) — nicht allgemein; die Linearität $E(X+Y)=E(X)+E(Y)$ gilt dagegen immer. (3)
$\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$ braucht nur $\mathrm{Cov}=0$, also schon Unkorreliertheit. (4) Gleiche
Randverteilungen legen die gemeinsame Verteilung **nicht** fest (die 2D-Normalverteilung mit beliebigem $\rho$).

:::kern
__Unabhängigkeit__: $F_{X,Y}(x,y)=F_X(x)F_Y(y)$ für alle $x,y$ (gemeinsame Verteilungsfunktion faktorisiert). Folge:
__Produkteigenschaft__ $E(XY)=E(X)E(Y)$ ⇒ $\mathrm{Cov}(X,Y)=0$ ⇒ $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$
(Lemma 8.35). __Unkorreliert__ (Def. 8.40): $\mathrm{Cov}=0$; __Lemma 8.41__: unabhängig ⇒ unkorreliert, **nicht**
umgekehrt (Beispiel 8.42: $X\in\{-1,0,1\}$, $Y$ Indikator — $\mathrm{Cov}=0$, aber abhängig). __Diskret__ (Satz
8.43): $P(X=x_k,Y=y_\ell)=P(X=x_k)P(Y=y_\ell)$. __Absolut-stetig__ (Def. 8.44, Satz 8.45): gemeinsame Dichte
$f_{X,Y}$, __Randdichten__ $f_X=\int f_{X,Y}\,dy$, $f_Y=\int f_{X,Y}\,dx$; unabhängig ⟺ $f_{X,Y}=f_Xf_Y$.
__2D-Normal__: $\rho=0$ Produktdichte (unabhängig), $\rho\neq0$ gekippte Ellipse (abhängig, aber Ränder weiter
$\mathcal N(0,1)$); bei Normalverteilung unkorreliert = unabhängig.
:::

Die Additivität der Varianz unter Unabhängigkeit ist der Schlüssel zum nächsten Satz: Mittelt man viele unabhängige
Variablen, schrumpft die Streuung des Mittelwerts — und der Durchschnitt nähert sich dem Erwartungswert. Das ist das
__Gesetz der großen Zahlen__, das Thema des nächsten Artikels.

:::quiz
F: Was bedeutet Unabhängigkeit zweier Zufallsvariablen über ihre gemeinsame Verteilungsfunktion?
A: $F_{X,Y}(x,y)=F_X(x)F_Y(y)$ für alle $x,y$ — die gemeinsame Verteilung ist vollständig das Produkt der beiden Einzelverteilungen. Das Wissen über $X$ ändert die Verteilung von $Y$ nicht, es bleibt kein Zusammenhang übrig.
F: Warum folgt aus Unabhängigkeit die Produkteigenschaft $E(XY)=E(X)E(Y)$?
A: Weil die gemeinsame Verteilung (Wahrscheinlichkeitsfunktion bzw. Dichte) faktorisiert, zerfällt die Doppelsumme bzw. das Doppelintegral $\sum_{k,\ell}x_ky_\ell P(X=x_k)P(Y=y_\ell)$ bzw. $\int\!\int xy f_X f_Y$ in ein Produkt zweier getrennter Summen/Integrale — genau $E(X)E(Y)$.
F: Warum ist die Varianz unter Unabhängigkeit additiv, und welche Annahme reicht dafür wirklich aus?
A: Aus $E(XY)=E(X)E(Y)$ folgt $\mathrm{Cov}(X,Y)=0$, und $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\mathrm{Cov}$ reduziert sich auf die Summe. Tatsächlich genügt dafür schon $\mathrm{Cov}=0$, also Unkorreliertheit — Unabhängigkeit ist hinreichend, aber mehr als nötig.
F: Worin unterscheidet sich „unkorreliert" von „unabhängig"?
A: Unkorreliert heißt nur $\mathrm{Cov}=0$, erfasst also ausschließlich den **linearen** Zusammenhang. Unabhängig verlangt das Faktorisieren der ganzen Verteilung und schließt **jeden** (auch nicht-linearen) Zusammenhang aus — deshalb ist unabhängig strikt stärker.
F: Wie zeigt Beispiel 8.42, dass unkorreliert nicht unabhängig bedeutet?
A: Dort ist $XY\equiv0$ und $E(X)=0$, also $\mathrm{Cov}=0$ (unkorreliert). Aber $Y=1$ erzwingt $X=0$ — ein klarer Zusammenhang; entsprechend faktorisiert die gemeinsame Verteilung nicht ($F_{X,Y}\neq F_XF_Y$). Der Zusammenhang ist nicht-linear, daher für die Kovarianz unsichtbar.
F: Was ist eine Randdichte, und wie gewinnt man sie aus der gemeinsamen Dichte?
A: Die Randdichte $f_X(x)=\int f_{X,Y}(x,y)\,dy$ ist die Dichte von $X$ allein, gewonnen durch „Ausintegrieren" von $Y$ über alle Werte. Man vergisst also die Information über $Y$ und behält die reine $X$-Verteilung.
F: Wie prüft man im absolut-stetigen Fall die Unabhängigkeit?
A: Man bildet die Randdichten $f_X,f_Y$ und testet, ob $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ für alle $x,y$ gilt (Satz 8.45(ii)). Faktorisiert die gemeinsame Dichte in das Produkt der Randdichten, sind $X,Y$ unabhängig, sonst nicht.
F: Warum legen gleiche Randverteilungen die gemeinsame Verteilung nicht fest?
A: Die Ränder sagen nur, wie sich jede Variable einzeln verhält, nicht wie sie zusammenhängen. Die 2D-Normalverteilung zeigt es: Für jedes $\rho\in[0,1)$ sind beide Ränder $\mathcal N(0,1)$, aber die Abhängigkeitsstruktur (die Verkippung der Wolke) ist völlig verschieden.
F: Wann sind die Komponenten einer zweidimensionalen Normalverteilung unabhängig?
A: Genau dann, wenn der Korrelationsparameter $\rho=0$ ist — nur dann verschwindet der Mischterm $-2\rho xy$ und die Dichte faktorisiert in $f_X(x)f_Y(y)$. Für $\rho\neq0$ bleiben die Ränder normal, aber $X$ und $Y$ sind abhängig.
F: Warum ist bei der Normalverteilung „unkorreliert" gleichbedeutend mit „unabhängig", obwohl das allgemein nicht gilt?
A: Bei gemeinsam normalverteilten $X,Y$ steckt die gesamte Abhängigkeit im einzigen Parameter $\rho$ (der Kovarianz). Ist $\rho=0$, verschwindet nicht nur der lineare Zusammenhang, sondern die Dichte faktorisiert vollständig — deshalb fallen hier die beiden Begriffe ausnahmsweise zusammen.
:::
