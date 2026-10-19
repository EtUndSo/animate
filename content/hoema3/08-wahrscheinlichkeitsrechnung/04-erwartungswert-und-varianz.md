---
title: Erwartungswert und Varianz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3080400
summary: Von Grund auf – zwei Kennzahlen verdichten eine ganze Verteilung. Der Erwartungswert $E(X)=\int x\,P_X(dx)$ ist der Schwerpunkt (im Mittel angenommener Wert), linear und monoton. Die Varianz $\mathrm{Var}(X)=E((X-\mu)^2)=E(X^2)-E(X)^2$ misst die Streuung, ist quadratisch und bringt die Kovarianz ins Spiel. Die Tschebyschew-Ungleichung macht präzise, wie die Varianz große Abweichungen begrenzt.
tags: Erwartungswert, Varianz, Standardabweichung, Linearität, Kovarianz, Tschebyschew-Ungleichung, Maßintegral, Streuung
---

:::grafik
Einstiegs-Animation: Eine Verteilung (Stäbe bzw. Dichtekurve) auf der Zahlengerade. Der __Erwartungswert__ $E(X)$
erscheint als __Schwerpunkt__ — der Balancepunkt, an dem die „Massenverteilung" der Wahrscheinlichkeit kippfrei
ruht. Dann wird die __Varianz__ sichtbar: zwei Verteilungen mit **demselben** Schwerpunkt, eine schmal
(kleine Streuung), eine breit (große Streuung) — die Varianz misst die mittlere quadratische Entfernung vom
Schwerpunkt. Rechts die __Tschebyschew-Schranke__: ein $\varepsilon$-Band um $\mu$, außerhalb dessen höchstens
$\sigma^2/\varepsilon^2$ der Wahrscheinlichkeit liegen kann. Kernbotschaft: Erwartungswert = Mitte, Varianz =
Breite, und die Varianz begrenzt die Ausreißer.
:::

:::konzept
Eine Verteilung enthält alle Information über eine Zufallsvariable — oft zu viel. Zwei Zahlen fassen das Wesentliche
zusammen: der __Erwartungswert__ $E(X)$ sagt, **wo** die Verteilung liegt (ihr Schwerpunkt, der im Mittel
angenommene Wert), die __Varianz__ $\mathrm{Var}(X)$ sagt, **wie breit** sie ist (wie stark $X$ um den Erwartungswert
streut). Der Erwartungswert ist im Kern ein __Integral__ und damit **linear** — das macht ihn zum bequemsten Werkzeug
der ganzen Stochastik. Die Varianz ist dagegen **quadratisch**, weshalb beim Addieren von Variablen die __Kovarianz__
dazukommt. Und die __Tschebyschew-Ungleichung__ schlägt die Brücke zurück zur Wahrscheinlichkeit: Sie garantiert
allein aus $E$ und $\mathrm{Var}$, dass große Abweichungen selten sind — der Keim des Gesetzes der großen Zahlen.
:::

**Worum es geht:** Wir definieren den __Erwartungswert__ (als Maßintegral, diskret und stetig), seine __Linearität__
und $E(g(X))$, dann die __Varianz__, __Standardabweichung__ und __Kovarianz__, und beweisen die
__Tschebyschew-Ungleichung__.

## Der Erwartungswert

Intuitiv ist $E(X)$ der Wert, den $X$ **im Mittel** annimmt (präzisiert durch das Gesetz der großen Zahlen). Formal
ist er die Mittelung aller Werte bezüglich des Verteilungsmaßes $P_X$, also ein __Maßintegral__
$$E(X)=\int_{\mathbb R}x\,P_X(dx).$$
Für die beiden wichtigen Spezialfälle wird daraus eine Summe bzw. ein Integral (sofern **absolut** konvergent):
$$\text{diskret:}\ \ E(X)=\sum_k x_k\,P(X=x_k),\qquad \text{absolut-stetig:}\ \ E(X)=\int_{\mathbb R}x\,f_X(x)\,dx.$$
Man schreibt oft $\mu_X=E(X)$. Die geometrische Deutung ist der **Schwerpunkt**: Trägt man die Wahrscheinlichkeit als
Masse auf, liegt $E(X)$ genau am Balancepunkt.

__Beispiel 8.28 (Poisson).__ Für $X\sim\text{Poisson}(\lambda)$ ist $E(X)=\lambda$, denn
$$E(X)=\sum_{k=0}^\infty k\,\frac{\lambda^k}{k!}e^{-\lambda}=\lambda\,e^{-\lambda}\sum_{k=1}^\infty\frac{\lambda^{k-1}}{(k-1)!}=\lambda\,e^{-\lambda}e^{\lambda}=\lambda.$$
Der Faktor $k$ hebt den $k=0$-Term weg und verschiebt den Index — die verbleibende Reihe ist wieder $e^\lambda$. Der
Parameter $\lambda$ ist also direkt der Erwartungswert.

__Beispiel 8.29 (Normal).__ Für $X\sim\mathcal N(\mu,\sigma^2)$ ist $E(X)=\mu$. Man schreibt
$x=(x-\mu)+\mu$; das Integral über $(x-\mu)\,e^{-\frac12(\frac{x-\mu}{\sigma})^2}$ verschwindet aus
**Punktsymmetrie** (ungerader Integrand um $\mu$), und übrig bleibt $\mu\cdot\int f_X=\mu$.

## Linearität, Monotonie und E(g(X))

__Lemma 8.30.__ Für Zufallsvariablen $X,Y$ auf einem gemeinsamen Raum und $c\in\mathbb R$:
$$E(X+cY)=E(X)+c\,E(Y)\quad(\text{Linearität}),\qquad X\le Y\Rightarrow E(X)\le E(Y)\quad(\text{Monotonie}).$$
Das sind genau die Eigenschaften eines Integrals — tatsächlich ist $E(X)=\int_\Omega X\,dP$ die Integration von $X$
bezüglich $P$. Im diskreten Fall ($\Omega=\{\omega_1,\dots\}$) liest man es direkt ab: $E(X)=\sum_i
X(\omega_i)P(\omega_i)$, und Linearität/Monotonie folgen sofort. Die Linearität ist **bemerkenswert stark**: Sie gilt
**ohne** jede Unabhängigkeitsannahme über $X$ und $Y$.

__Satz 8.31 (Transformationsformel).__ Für absolut-stetiges $X$ mit Dichte $f_X$ und stetiges $g$:
$$E(g(X))=\int_{\mathbb R}g(x)\,f_X(x)\,dx$$
(diskret entsprechend $E(g(X))=\sum_i g(X(\omega_i))P(\omega_i)$). Der Clou: Man braucht die Dichte von $g(X)$
**nicht** — man integriert $g$ gegen die Dichte von $X$. Das ist das Arbeitspferd für alle abgeleiteten Größen, allen
voran $E(X^2)$.

## Varianz und Standardabweichung

Ein großer Erwartungswert sagt nichts darüber, ob $X$ **nahe** bei $\mu$ liegt. Dafür misst man die mittlere
quadratische Abweichung.

__Definition 8.32.__ Existiert $E(X^2)$, so ist die __Varianz__
$$\mathrm{Var}(X):=E\big((X-E(X))^2\big),\qquad \sigma_X:=\sqrt{\mathrm{Var}(X)}\ \ (\text{Standardabweichung}).$$
Aus der Linearität folgt sofort die meistbenutzte Rechenform (Ausmultiplizieren von $(X-\mu)^2$):
$$\mathrm{Var}(X)=E(X^2)-E(X)^2.$$
Warum **quadratisch**? Die lineare mittlere Abweichung $E(X-\mu)$ ist immer $0$ (positive und negative Abweichungen
heben sich auf). Das Quadrat macht alle Abweichungen positiv und bestraft große stärker — und die Wurzel $\sigma_X$
bringt das Ergebnis zurück in die Einheit von $X$.

__Beispiel 8.33 (Poisson).__ Für $X\sim\text{Poisson}(\lambda)$ ist auch $\mathrm{Var}(X)=\lambda$. Mit dem Trick
$k^2=k(k-1)+k$ zerfällt $E(X^2)$ in zwei verschiebbare Reihen, man erhält $E(X^2)=\lambda^2+\lambda$, also
$\mathrm{Var}(X)=\lambda^2+\lambda-\lambda^2=\lambda$. (Bei Poisson sind Erwartungswert und Varianz gleich — ein
Erkennungsmerkmal.)

__Beispiel 8.34 (Normal).__ Für $X\sim\mathcal N(\mu,\sigma^2)$ ist $\mathrm{Var}(X)=\sigma^2$. Nach Substitution
$y=\frac{x-\mu}{\sigma}$ bleibt $\frac{\sigma^2}{\sqrt{2\pi}}\int y^2 e^{-y^2/2}dy$; mit $y\,e^{-y^2/2}=-\frac{d}{dy}e^{-y^2/2}$
liefert **partielle Integration** gerade wieder das Gauß-Integral, also $\mathrm{Var}(X)=\sigma^2$. Die Parameter
$(\mu,\sigma^2)$ der Normalverteilung sind damit **exakt** Erwartungswert und Varianz.

## Kovarianz: wie Varianzen sich addieren

Weil die Varianz quadratisch ist, verhält sie sich beim Addieren anders als der Erwartungswert.

__Lemma 8.35.__ Für $X,Y$ mit existierenden zweiten Momenten und $c\in\mathbb R$:
$$\mathrm{Var}(cX)=c^2\,\mathrm{Var}(X),\qquad \mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\,\mathrm{Cov}(X,Y),$$
mit der __Kovarianz__ $\mathrm{Cov}(X,Y):=E\big[(X-E(X))(Y-E(Y))\big]$. __Bemerkung 8.36:__ Es gilt die Rechenform
$\mathrm{Cov}(X,Y)=E(XY)-E(X)E(Y)$. Der Faktor $c^2$ (nicht $c$) ist die Signatur des Quadrats, und die Kovarianz ist
der „gemischte Term", der beim Ausmultiplizieren von $((X-\mu_X)+(Y-\mu_Y))^2$ entsteht. Sie misst, ob $X$ und $Y$
**gemeinsam** über oder unter ihrem Mittel liegen; verschwindet sie, addieren sich die Varianzen einfach — das wird
im nächsten Artikel für unabhängige Variablen zentral.

:::grafik
Links der Erwartungswert als Schwerpunkt (Balancepunkt der Wahrscheinlichkeitsmasse); daneben zwei Verteilungen
gleichen Schwerpunkts, schmal vs. breit, mit ihren Varianzen. Rechts die Kovarianz: Punktwolken $(X,Y)$ mit
positiver, null und negativer Kovarianz; Formel $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\mathrm{Cov}(X,Y)$.
:::

## Die Tschebyschew-Ungleichung

Wie stark begrenzt die Varianz die Abweichung vom Erwartungswert? Für $\varepsilon>0$ schätzt man (diskret; stetig
analog) die Varianz nach unten ab, indem man nur die „weit entfernten" Werte behält und dort $(x_i-\mu)^2\ge\varepsilon^2$
ausnutzt:
$$\mathrm{Var}(X)=\sum_i(x_i-\mu)^2P(X=x_i)\ \ge\!\!\sum_{|x_i-\mu|\ge\varepsilon}\!\!(x_i-\mu)^2P(X=x_i)\ \ge\ \varepsilon^2\!\!\sum_{|x_i-\mu|\ge\varepsilon}\!\!P(X=x_i)=\varepsilon^2\,P(|X-\mu|\ge\varepsilon).$$
Nach $P(\cdot)$ aufgelöst ergibt das:

__Satz 8.37 (Tschebyschew-Ungleichung).__ Für $X$ mit $E(X)=\mu$, $\mathrm{Var}(X)=\sigma^2$ und jedes
$\varepsilon>0$:
$$P(|X-\mu|\ge\varepsilon)\le\frac{\sigma^2}{\varepsilon^2}.$$

__Bemerkung 8.38.__ Interessant ist sie für **große** Abweichungen: Mit $\varepsilon\to\infty$ fällt die
Wahrscheinlichkeit großer Abweichungen quadratisch. Für $\varepsilon\le\sigma$ liefert sie nichts Neues (die
Schranke ist $\ge1$, und $P\le1$ gilt ohnehin); der Grenzfall $\varepsilon=\sigma$ markiert genau die
Standardabweichung. Die Stärke der Ungleichung ist ihre **Universalität**: Sie gilt für **jede** Verteilung, nur mit
$\mu$ und $\sigma^2$ — ganz ohne Kenntnis der Form.

**Stolperstein:** (1) Erwartungswert und Varianz existieren **nur**, wenn Summe/Integral **absolut** konvergieren —
es gibt Verteilungen ohne $E(X)$ (z. B. Cauchy). (2) __Linearität von $E$__ gilt **immer**, auch für abhängige
$X,Y$ — $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$ hingegen **nur** bei $\mathrm{Cov}=0$. (3) $E(g(X))\neq
g(E(X))$ im Allgemeinen (z. B. $E(X^2)\neq E(X)^2$ — genau die Differenz ist die Varianz). (4) Tschebyschew ist
**grob** (universell, aber nicht scharf) — für konkrete Verteilungen gibt es oft viel bessere Schranken.

:::kern
__Erwartungswert__ $E(X)=\int_{\mathbb R}x\,P_X(dx)$ (Maßintegral) — diskret $\sum_k x_k P(X=x_k)$, stetig $\int
x f_X\,dx$ (absolut konvergent); Schwerpunkt, $\mu_X$. Beispiele: Poisson $E=\lambda$, Normal $E=\mu$. __Lemma
8.30__: $E$ linear ($E(X+cY)=E(X)+cE(Y)$, immer!) und monoton. __Satz 8.31__: $E(g(X))=\int g(x)f_X(x)\,dx$ (Dichte
von $g(X)$ unnötig). __Varianz__ (Def. 8.32): $\mathrm{Var}(X)=E((X-\mu)^2)=E(X^2)-E(X)^2$, $\sigma_X=\sqrt{\mathrm{Var}}$;
quadratisch (lineare mittlere Abweichung $=0$). Poisson $\mathrm{Var}=\lambda$, Normal $\mathrm{Var}=\sigma^2$.
__Lemma 8.35__: $\mathrm{Var}(cX)=c^2\mathrm{Var}(X)$, $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\mathrm{Cov}(X,Y)$,
$\mathrm{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]=E(XY)-E(X)E(Y)$. __Tschebyschew__ (Satz 8.37):
$P(|X-\mu|\ge\varepsilon)\le\sigma^2/\varepsilon^2$ — universell, für große $\varepsilon$ quadratischer Abfall.
:::

Die Tschebyschew-Ungleichung sagt schon jetzt: Kleine Varianz ⇒ $X$ bleibt nahe bei $\mu$. Für **Summen** vieler
Variablen braucht man aber, wie sich Varianzen addieren — und das ist nur unter __Unabhängigkeit__ einfach. Wann
Zufallsvariablen unabhängig sind und warum dann $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$ gilt, ist das Thema
des nächsten Artikels.

:::quiz
F: Warum ist der Erwartungswert anschaulich der „Schwerpunkt" der Verteilung?
A: $E(X)=\int x\,P_X(dx)$ gewichtet jeden Wert mit seiner Wahrscheinlichkeit — genau wie ein Massenschwerpunkt jede Position mit ihrer Masse gewichtet. Trägt man die Wahrscheinlichkeit als Masse auf, ist $E(X)$ der Punkt, an dem die Verteilung kippfrei balanciert.
F: Warum muss man für die Existenz von $E(X)$ absolute Konvergenz fordern?
A: Nur bei absoluter Konvergenz ist der Wert der Summe/des Integrals unabhängig von der Summationsreihenfolge und wohldefiniert. Sonst (z. B. bei der Cauchy-Verteilung) existiert kein sinnvoller Mittelwert — der Erwartungswert ist dann nicht definiert.
F: Warum ist die Linearität des Erwartungswerts so bemerkenswert stark?
A: $E(X+cY)=E(X)+cE(Y)$ gilt **ohne** jede Annahme über die Abhängigkeit von $X$ und $Y$. Das liegt daran, dass $E$ im Kern ein Integral ist und Integration immer linear ist — man darf Erwartungswerte von Summen immer gliedweise zerlegen.
F: Was besagt die Transformationsformel $E(g(X))=\int g(x)f_X(x)\,dx$, und warum ist sie praktisch?
A: Sie berechnet den Erwartungswert von $g(X)$, ohne die Verteilung von $g(X)$ selbst zu kennen — man integriert einfach $g$ gegen die Dichte von $X$. Das erspart die oft schwierige Bestimmung der Dichte der transformierten Variablen, etwa bei $E(X^2)$.
F: Warum misst man Streuung über das Quadrat und nicht über die einfache Abweichung $X-\mu$?
A: Die mittlere einfache Abweichung $E(X-\mu)$ ist immer null, weil sich positive und negative Abweichungen aufheben. Das Quadrat macht alle Abweichungen positiv und gewichtet große stärker; die Wurzel (Standardabweichung) bringt das Maß zurück in die Einheit von $X$.
F: Wie folgt die Rechenform $\mathrm{Var}(X)=E(X^2)-E(X)^2$ aus der Definition?
A: Man multipliziert $(X-\mu)^2=X^2-2\mu X+\mu^2$ aus und wendet die Linearität an: $E(X^2)-2\mu E(X)+\mu^2=E(X^2)-2\mu^2+\mu^2=E(X^2)-\mu^2$. Die Varianz ist also „mittleres Quadrat minus Quadrat des Mittels".
F: Warum ist bei der Poisson-Verteilung $E(X)=\mathrm{Var}(X)=\lambda$ ein Erkennungsmerkmal?
A: Beide Kennzahlen sind gleich dem einzigen Parameter $\lambda$. Beobachtet man an Daten näherungsweise gleiche empirische Mittel und Varianz, ist das ein starker Hinweis auf eine Poisson-Verteilung — Abweichungen deuten auf Über- oder Unterdispersion.
F: Warum skaliert die Varianz mit $c^2$ statt mit $c$, und wozu dient die Kovarianz?
A: Weil die Varianz eine quadratische Größe ist: $\mathrm{Var}(cX)=E((cX-c\mu)^2)=c^2 E((X-\mu)^2)$. Beim Addieren entsteht ein gemischter Term, die Kovarianz $\mathrm{Cov}(X,Y)$; sie misst das gemeinsame Abweichen und sorgt dafür, dass sich Varianzen nur bei $\mathrm{Cov}=0$ einfach addieren.
F: Wie kommt die Tschebyschew-Ungleichung zustande?
A: Man schätzt die Varianz nach unten ab, indem man in $\sum(x_i-\mu)^2 P$ nur die Terme mit $|x_i-\mu|\ge\varepsilon$ behält und dort $(x_i-\mu)^2\ge\varepsilon^2$ setzt: $\mathrm{Var}(X)\ge\varepsilon^2 P(|X-\mu|\ge\varepsilon)$. Auflösen nach der Wahrscheinlichkeit gibt $P(|X-\mu|\ge\varepsilon)\le\sigma^2/\varepsilon^2$.
F: Was ist die Stärke und was die Schwäche der Tschebyschew-Ungleichung?
A: Stärke: Sie gilt universell für jede Verteilung, allein aus $\mu$ und $\sigma^2$, ohne deren Form zu kennen. Schwäche: Sie ist dadurch grob — für $\varepsilon\le\sigma$ liefert sie nichts (Schranke $\ge1$), und für konkrete Verteilungen gibt es meist viel schärfere Abschätzungen.
:::
