---
title: Kovarianz und Korrelation
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15241100
summary: Zwei Größen schwanken oft gemeinsam: Größere Wohnungen haben mehr Zimmer, an Sonnentagen wird mehr Rad gefahren.
tags: Kovarianz, unkorreliert, Korrelationskoeffizient, empirische Kovarianz, empirische Korrelationskoeffizient, Zufallsprozess
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Zwei Größen schwanken oft gemeinsam: Größere Wohnungen haben mehr Zimmer, an Sonnentagen wird mehr Rad gefahren. Dieser Abschnitt misst das mit einer Zahl, der Kovarianz, und mit ihrer einheitenlosen Form, dem Korrelationskoeffizienten. Er zeigt, dass die Kovarianz wie ein Skalarprodukt rechnet, warum sich deshalb die Varianzen unabhängiger Größen addieren, und warum eine Kovarianz von null noch keine Unabhängigkeit bedeutet. Am Ende stehen Kovarianz und Korrelation eines Datensatzes.
:::

### Die Kovarianz

<span class="anker" id="stufe-10-1"></span>

Liegt $X$ über seinem Erwartungswert, wenn auch $Y$ über seinem liegt, so ist das Produkt der beiden Abweichungen positiv; liegt das eine darüber und das andere darunter, ist es negativ. Mittelt man dieses Produkt, so sagt das Vorzeichen, welcher Fall überwiegt, und der Betrag, wie stark.

:::definition Definition 10.1 (Kovarianz)
<span class="anker" id="satz-10-1"></span>

Für Zufallsvariablen $X$ und $Y$ mit den Erwartungswerten $\mu_X$ und $\mu_Y$ heißt

<span class="anker" id="gl-10-1"></span>
$$\operatorname{Cov}(X,Y)=\mathbb{E}\bigl[(X-\mu_X)(Y-\mu_Y)\bigr] \tag{10.1}$$

die __Kovarianz__ von $X$ und $Y$.
:::

Wie bei der Varianz gibt es eine Verschiebungsformel: Ausmultiplizieren und die Linearität ergeben

<span class="anker" id="gl-10-2"></span>
$$\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\,\mathbb{E}[Y]. \tag{10.2}$$

Die Kovarianz ist symmetrisch, $\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X)$, und es ist $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$. Sie hat das Produkt der Einheiten von $X$ und $Y$. Unter linearer Umrechnung gilt $\operatorname{Cov}(aX+b,\,cY+d)=ac\,\operatorname{Cov}(X,Y)$, denn Verschiebungen fallen in den Abweichungen heraus. Sind $X$ und $Y$ unabhängig, so ist nach Unterabschnitt [9.5](mehrere-zufallsvariablen.html#stufe-9-5) $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$, also $\operatorname{Cov}(X,Y)=0$. Zufallsvariablen mit Kovarianz null heißen __unkorreliert__.

::::beispiel [Rechenbeispiel]
Für Sonne $S$ und Rad $R$ ist $\mathbb{E}[S]=\mathbb{E}[R]=0{,}4$, und $\mathbb{E}[SR]$ ist die Summe von $s\,r\,P(S=s,R=r)$ über die vier Zellen (Abb. [12](#abb-12)). Die Kovarianz ist $0{,}3-0{,}16=0{,}14>0$: Sonne und Radfahren treten häufiger gemeinsam auf, als es bei Unabhängigkeit der Fall wäre.

:::abbildung ml/k4rkovarianz 12
Die Kovarianz von Sonne und Radfahren: Nur die Zelle, in der beide Größen $1$ sind, trägt zu $\mathbb{E}[SR]$ bei.
:::
::::

⁠**Kurz gesagt:** Die Kovarianz ist der Erwartungswert des Produkts der beiden Abweichungen; positiv, wenn die Größen gemeinsam steigen, negativ, wenn die eine fällt, wenn die andere steigt, und null bei unabhängigen Größen.

### Die Varianz einer Summe

<span class="anker" id="stufe-10-2"></span>

Zwei Störquellen addieren sich in einer Schaltung. Wie stark schwankt die Summe? Die Erwartungswerte addieren sich immer. Bei den Varianzen kommt es darauf an, wie die Störungen zusammenhängen: Schwanken sie im Gleichtakt, verstärken sie sich; schwanken sie gegeneinander, heben sie sich teilweise auf.

:::satz Satz 10.2 (Varianz einer Summe)
<span class="anker" id="satz-10-2"></span>

Für Zufallsvariablen $X$ und $Y$ ist

<span class="anker" id="gl-10-3"></span>
$$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\,\operatorname{Cov}(X,Y). \tag{10.3}$$

Für $X_1,\dots,X_n$ ist $\operatorname{Var}\bigl(\sum_iX_i\bigr)=\sum_i\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)$. Sind die Zufallsvariablen paarweise unkorreliert, insbesondere wenn sie unabhängig sind, so addieren sich die Varianzen:

<span class="anker" id="gl-10-4"></span>
$$\operatorname{Var}(X_1+\dots+X_n)=\operatorname{Var}(X_1)+\dots+\operatorname{Var}(X_n). \tag{10.4}$$
:::

:::beweis Varianz einer Summe
Mit den Abweichungen $\tilde X=X-\mu_X$ und $\tilde Y=Y-\mu_Y$ ist die Abweichung der Summe $\tilde X+\tilde Y$, also $\operatorname{Var}(X+Y)=\mathbb{E}[(\tilde X+\tilde Y)^2]=\mathbb{E}[\tilde X^2]+2\,\mathbb{E}[\tilde X\tilde Y]+\mathbb{E}[\tilde Y^2]$. Bei $n$ Summanden ist das Quadrat der Summe die Summe aller Produkte $\tilde X_i\tilde X_j$; die mit $i=j$ ergeben die Varianzen, jedes Paar $i\ne j$ kommt zweimal vor.
:::

Die Standardabweichungen addieren sich dagegen nicht. Für unabhängige Größen ist $\sigma_{X+Y}=\sqrt{\sigma_X^2+\sigma_Y^2}$, kleiner als $\sigma_X+\sigma_Y$.

::::beispiel [Rechenbeispiel 1]
Zwei unabhängige Rauschquellen mit den Standardabweichungen $3\,\mathrm{mV}$ und $4\,\mathrm{mV}$ ergeben zusammen die Varianz $9+16=25\,\mathrm{mV}^2$, also $\sigma=5\,\mathrm{mV}$ und nicht $7\,\mathrm{mV}$. Die Augensumme zweier Würfel hat die Varianz $2\cdot\tfrac{35}{12}=\tfrac{35}6\approx5{,}83$ und die Standardabweichung $2{,}415$, nicht $2\cdot1{,}708$.
::::

::::beispiel [Rechenbeispiel 2] die Binomialverteilung
$X\sim\mathrm{Bin}(n,\theta)$ ist die Summe von $n$ unabhängigen Bernoulli-Variablen mit der Varianz $\theta(1-\theta)$. Nach [(10.4)](#gl-10-4) ist

<span class="anker" id="gl-10-5"></span>
$$\operatorname{Var}(X)=n\,\theta\,(1-\theta). \tag{10.5}$$

Für die $10$ Teile bei $5\,\%$ Ausschuss ist $\operatorname{Var}(X)=10\cdot0{,}05\cdot0{,}95=0{,}475$ und $\sigma\approx0{,}689$; für die drei Münzwürfe ist $\operatorname{Var}=3\cdot\tfrac14=0{,}75$, wie in Unterabschnitt [7.4](erwartungswert-und-varianz.html#stufe-7-4).
::::

⁠**Kurz gesagt:** Die Varianz einer Summe ist die Summe der Varianzen plus zweimal jede Kovarianz; bei unabhängigen Größen addieren sich die Varianzen, nicht die Standardabweichungen.

:::hintergrund Warum sich Varianzen addieren und Standardabweichungen nicht
Die Rechnung im Beweis ist die Rechnung für die Länge einer Vektorsumme: $\lVert\mathbf{a}+\mathbf{b}\rVert^2=\lVert\mathbf{a}\rVert^2+2\,\mathbf{a}^{\top}\mathbf{b}+\lVert\mathbf{b}\rVert^2$. Die Rolle des Skalarprodukts spielt die Kovarianz, die Rolle der Länge die Standardabweichung (Unterabschnitt [10.4](#stufe-10-4)). Unkorrelierte Größen entsprechen senkrechten Vektoren, und [(10.4)](#gl-10-4) ist der Satz des Pythagoras: Die Längen addieren sich nicht, ihre Quadrate schon. Zwei unabhängige Rauschquellen mit $3$ und $4\,\mathrm{mV}$ sind wie zwei senkrechte Katheten; die Summe ist die Hypotenuse mit $5\,\mathrm{mV}$. In der Elektrotechnik heißt das: Die Leistungen unabhängiger Rauschquellen addieren sich, ihre Effektivwerte addieren sich nur „quadratisch“. Dass sich die Varianzen unabhängiger Summanden addieren, wurde 1853 von Irénée-Jules Bienaymé ausgesprochen. Diese Eigenschaft ist der Hauptgrund, warum man Streuung mit Quadraten misst und nicht etwa mit dem mittleren Betrag der Abweichung: Für den mittleren Betrag gibt es keine solche Additionsregel.
:::

### Der Korrelationskoeffizient

<span class="anker" id="stufe-10-3"></span>

Die Kovarianz hat eine Einheit, und ihr Betrag hängt von den Einheiten ab: In Millimetern statt Metern gemessen wird sie tausendmal so groß. Um die Stärke eines Zusammenhangs zu vergleichen, misst man beide Größen in ihren eigenen Standardabweichungen, also standardisiert.

:::definition Definition 10.3 (Korrelationskoeffizient)
<span class="anker" id="satz-10-3"></span>

Für Zufallsvariablen mit $\sigma_X>0$ und $\sigma_Y>0$ heißt

<span class="anker" id="gl-10-6"></span>
$$\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\,\sigma_Y} \tag{10.6}$$

der __Korrelationskoeffizient__ von $X$ und $Y$. Er ist die Kovarianz der standardisierten Größen $Z_X=(X-\mu_X)/\sigma_X$ und $Z_Y=(Y-\mu_Y)/\sigma_Y$.
:::

:::satz Satz 10.4 (Wertebereich des Korrelationskoeffizienten)
<span class="anker" id="satz-10-4"></span>

Es ist $-1\le\rho_{XY}\le1$. Der Betrag ist genau dann $1$, wenn $Y=aX+b$ mit Wahrscheinlichkeit $1$ gilt, mit $a>0$ für $\rho=1$ und $a<0$ für $\rho=-1$.
:::

:::beweis Wertebereich
Mit $\rho=\rho_{XY}=\operatorname{Cov}(Z_X,Z_Y)$ und $\operatorname{Var}(Z_X)=\operatorname{Var}(Z_Y)=1$ ist nach [(10.3)](#gl-10-3) und den Rechenregeln der Kovarianz

$$0\le\operatorname{Var}(Z_Y-\rho Z_X)=\operatorname{Var}(Z_Y)-2\rho\,\operatorname{Cov}(Z_X,Z_Y)+\rho^2\operatorname{Var}(Z_X)=1-2\rho^2+\rho^2=1-\rho^2 .$$

Also ist $\rho^2\le1$. Gleichheit gilt genau dann, wenn $Z_Y-\rho Z_X$ die Varianz $0$ hat, also mit Wahrscheinlichkeit $1$ konstant ist; wegen der Erwartungswerte ist die Konstante $0$, und $Z_Y=\rho Z_X$ ist eine lineare Beziehung.
:::

Der Korrelationskoeffizient misst also, wie gut sich $Y$ durch eine Gerade in $X$ beschreiben lässt. Abb. [13](#abb-13) zeigt Punktwolken mit verschiedenen Korrelationskoeffizienten. Bei $\rho=0{,}9$ liegen die Punkte nahe einer steigenden Geraden, bei $\rho=0$ ist keine Richtung bevorzugt.

:::abbildung ml/k4streu 13
Je $40$ Punkte $(x,y)$, waagrecht $x$, senkrecht $y$. (a) bis (d): Punktwolken mit den empirischen Korrelationskoeffizienten $-0{,}90$; $0{,}00$; $0{,}50$ und $0{,}90$, berechnet wie in Unterabschnitt [10.6](#stufe-10-6). (e) und (f): Der Korrelationskoeffizient ist $0$, obwohl $y$ von $x$ abhängt. In (e) ist $y=x^2$, in (f) ist $y=x$ oder $y=-x$ mit zufälligem Vorzeichen.
:::

::::beispiel [Rechenbeispiel]
Für Sonne und Rad ist $\operatorname{Var}(S)=\operatorname{Var}(R)=0{,}4\cdot0{,}6=0{,}24$, also $\rho=0{,}14/0{,}24\approx0{,}583$. Rechnet man eine Größe in andere Einheiten um, ändert sich $\rho$ nicht: Mit $\operatorname{Cov}(aX+b,\,cY+d)=ac\,\operatorname{Cov}(X,Y)$ und $\sigma_{aX+b}=|a|\sigma_X$ kürzt sich $ac$ bis auf das Vorzeichen heraus.
::::

⁠**Kurz gesagt:** Der Korrelationskoeffizient ist die Kovarianz der standardisierten Größen; er liegt zwischen $-1$ und $1$ und misst, wie gut eine Gerade den Zusammenhang beschreibt.

### Die Kovarianz als Skalarprodukt

<span class="anker" id="stufe-10-4"></span>

Die Rechenregeln der Kovarianz sind die eines Skalarprodukts aus [Grundlagen 1, Abschnitt 2.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-1). Sie ist symmetrisch und in jedem Argument linear: $\operatorname{Cov}(aX+bY,\,V)=a\,\operatorname{Cov}(X,V)+b\,\operatorname{Cov}(Y,V)$, eine direkte Folge der Linearität des Erwartungswerts. Und $\operatorname{Cov}(X,X)=\operatorname{Var}(X)\ge0$. Das legt eine geometrische Sprache nahe, in der Zufallsvariablen mit Erwartungswert $0$ wie Vektoren behandelt werden.

| Vektoren (Grundlagen 1) | Zufallsvariablen mit Erwartungswert $0$ |
|---|---|
| Skalarprodukt $\mathbf{a}^{\top}\mathbf{b}$ | Kovarianz $\operatorname{Cov}(X,Y)=\mathbb{E}[XY]$ |
| Länge $\lVert\mathbf{a}\rVert$ | Standardabweichung $\sigma_X$ |
| Kosinus des Winkels | Korrelationskoeffizient $\rho_{XY}$ |
| senkrecht | unkorreliert |
| Cauchy-Schwarz $\vert \mathbf{a}^{\top}\mathbf{b}\vert \le\lVert\mathbf{a}\rVert\,\lVert\mathbf{b}\rVert$ | $\vert \operatorname{Cov}(X,Y)\vert \le\sigma_X\sigma_Y$, also $\vert \rho\vert \le1$ |
| Pythagoras für senkrechte Vektoren | $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)$ für unkorrelierte |

Für einen Datensatz wird das wörtlich. [Grundlagen 1, Abschnitt 5.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-4), hat den Korrelationskoeffizienten zweier Merkmale als Kosinus des Winkels zwischen ihren zentrierten Merkmalsvektoren eingeführt. Das ist genau $\rho$ für die empirische Verteilung: Für zwei Merkmalsvektoren $\mathbf{a}$ und $\mathbf{b}$ mit den zentrierten Vektoren $\tilde{\mathbf{a}}$ und $\tilde{\mathbf{b}}$ ist die Kovarianz der empirischen Verteilung $\tfrac1N\tilde{\mathbf{a}}^{\top}\tilde{\mathbf{b}}$, ein Skalarprodukt der zentrierten Vektoren, und die Standardabweichungen sind $\tfrac1{\sqrt N}\lVert\tilde{\mathbf{a}}\rVert$ und $\tfrac1{\sqrt N}\lVert\tilde{\mathbf{b}}\rVert$. Der Faktor $\tfrac1N$ kürzt sich im Quotienten heraus (Unterabschnitt [10.6](#stufe-10-6)).

::::beispiel [Rechenbeispiel]
Für die Rauschquellen mit $3$ und $4\,\mathrm{mV}$ aus Unterabschnitt [10.2](#stufe-10-2) sei nun $\rho=0{,}5$, etwa weil beide von derselben Versorgungsspannung gestört werden. Das entspricht zwei Vektoren der Längen $3$ und $4$ im Winkel von $60^\circ$. Die Summe hat die Varianz $9+16+2\cdot0{,}5\cdot3\cdot4=37$, also $\sigma\approx6{,}08\,\mathrm{mV}$, mehr als die $5\,\mathrm{mV}$ unkorrelierter Quellen.
::::

⁠**Kurz gesagt:** Die Kovarianz rechnet wie ein Skalarprodukt; die Standardabweichung ist die Länge, der Korrelationskoeffizient der Kosinus des Winkels, und unkorreliert heißt senkrecht.

### Unkorreliert heißt nicht unabhängig

<span class="anker" id="stufe-10-5"></span>

Unabhängige Größen sind unkorreliert. Die Umkehrung liegt nahe, ist aber falsch. Die Kovarianz misst nur, wie gut eine Gerade den Zusammenhang beschreibt; ein Zusammenhang, der keiner Geraden folgt, kann ihr ganz entgehen.

:::satz Satz 10.5 (Unabhängig und unkorreliert)
<span class="anker" id="satz-10-5"></span>

Unabhängige Zufallsvariablen sind unkorreliert. Unkorrelierte Zufallsvariablen können abhängig sein. Ist die Kovarianz nicht null, so sind die Zufallsvariablen abhängig.
:::

Der erste Teil steht in Unterabschnitt [10.1](#stufe-10-1), der dritte ist seine Umkehrung ins Gegenteil. Für den zweiten genügt ein Beispiel.

::::beispiel [Rechenbeispiel 1]
$X$ sei gleich wahrscheinlich $-1$, $0$ oder $1$, und $Y=X^2$. Dann ist $\mathbb{E}[X]=0$ und $\mathbb{E}[XY]=\mathbb{E}[X^3]=\tfrac13\,(-1+0+1)=0$, also $\operatorname{Cov}(X,Y)=0$. Aber $Y$ ist durch $X$ vollständig bestimmt: $P(Y=0\mid X=0)=1$, während $P(Y=0)=\tfrac13$ ist. Abb. [13](#abb-13) (e) zeigt dasselbe für viele Werte: Die Punkte liegen auf einer Parabel, und eine Gerade durch sie hätte die Steigung $0$, weil der linke und der rechte Ast sich aufheben.
::::

::::beispiel [Rechenbeispiel 2]
$X\sim\mathcal N(0,1)$, und $V$ sei unabhängig davon $+1$ oder $-1$ mit je der Wahrscheinlichkeit $\tfrac12$. Dann ist $Y=VX$ ebenfalls standardnormalverteilt, weil die Normalverteilung symmetrisch um $0$ ist. Es ist $\operatorname{Cov}(X,Y)=\mathbb{E}[VX^2]=\mathbb{E}[V]\,\mathbb{E}[X^2]=0\cdot1=0$. Trotzdem ist $|Y|=|X|$ immer: Kennt man $X$, so bleiben für $Y$ nur zwei Werte. Abb. [13](#abb-13) (f) zeigt das als Kreuz aus zwei Geraden.
::::

⁠**Kurz gesagt:** Aus unabhängig folgt unkorreliert, aber nicht umgekehrt; die Kovarianz sieht nur den linearen Anteil eines Zusammenhangs.

### Kovarianz und Korrelation eines Datensatzes

<span class="anker" id="stufe-10-6"></span>

Hat man statt einer Verteilung nur Daten, so rechnet man mit der empirischen Verteilung aus Unterabschnitt [7.7](erwartungswert-und-varianz.html#stufe-7-7): Jeder Datenpunkt bekommt die Wahrscheinlichkeit $1/N$.

:::definition Definition 10.6 (Empirische Kovarianz und Korrelation)
<span class="anker" id="satz-10-6"></span>

Zwei Merkmale seien an $N$ Datenpunkten gemessen, mit den Werten $a_i$ und $b_i$, den Merkmalsvektoren $\mathbf{a},\mathbf{b}\in\mathbb{R}^N$, den Mittelwerten $\bar a$ und $\bar b$ und den zentrierten Vektoren $\tilde{\mathbf{a}}$ und $\tilde{\mathbf{b}}$ mit den Komponenten $a_i-\bar a$ und $b_i-\bar b$. Dann heißt

<span class="anker" id="gl-10-7"></span>
$$\operatorname{cov}(\mathbf{a},\mathbf{b})=\frac1N\sum_{i=1}^N(a_i-\bar a)(b_i-\bar b)=\frac1N\,\tilde{\mathbf{a}}^{\top}\tilde{\mathbf{b}} \tag{10.7}$$

die __empirische Kovarianz__ und

<span class="anker" id="gl-10-8"></span>
$$\operatorname{corr}(\mathbf{a},\mathbf{b})=\frac{\operatorname{cov}(\mathbf{a},\mathbf{b})}{\operatorname{std}(\mathbf{a})\,\operatorname{std}(\mathbf{b})} \tag{10.8}$$

der __empirische Korrelationskoeffizient__.
:::

Das ist die Kovarianz der empirischen Verteilung; sie ist durch $N$ geteilt wie die Standardabweichung in [Grundlagen 1, Abschnitt 4.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-4). Mit $\mathbf{b}=\mathbf{a}$ ist $\operatorname{cov}(\mathbf{a},\mathbf{a})=\operatorname{std}(\mathbf{a})^2$. Kleingeschrieben unterscheiden $\operatorname{cov}$ und $\operatorname{corr}$ die Zahlen eines Datensatzes von den Größen $\operatorname{Cov}$ und $\rho$ einer Verteilung; wie in Unterabschnitt [7.7](erwartungswert-und-varianz.html#stufe-7-7) hängen sie davon ab, welche Daten zufällig gezogen wurden.

::::beispiel [Rechenbeispiel]
Drei Datenpunkte $(a_i,b_i)$, nämlich $(1,2)$, $(2,1)$ und $(3,3)$, haben die Mittelwerte $\bar a=\bar b=2$ und die zentrierten Vektoren $\tilde{\mathbf{a}}=(-1,\,0,\,1)^{\top}$ und $\tilde{\mathbf{b}}=(0,\,-1,\,1)^{\top}$. Abb. [14](#abb-14) rechnet $\operatorname{cov}(\mathbf{a},\mathbf{b})=\tfrac13$ und $\operatorname{std}(\mathbf{a})^2=\operatorname{std}(\mathbf{b})^2=\tfrac23$, also $\operatorname{corr}(\mathbf{a},\mathbf{b})=\frac{1/3}{2/3}=0{,}5$.

:::abbildung ml/k4rdaten 14
Empirische Kovarianz und Varianz der drei Datenpunkte: Skalarprodukte der zentrierten Vektoren, geteilt durch $N=3$. Für $\mathbf{b}$ ergibt sich ebenso $\tfrac23$.
:::
::::

⁠**Kurz gesagt:** Kovarianz und Korrelation eines Datensatzes sind die der empirischen Verteilung: das Skalarprodukt der zentrierten Vektoren durch $N$, und dessen Kosinus.

:::hintergrund Zufallsprozesse: Kovarianzen innerhalb eines Signals
Ein Rauschsignal ist eine Folge von Zufallsvariablen $X_1,X_2,\dots$, eine für jeden Abtastzeitpunkt; man nennt eine solche Folge einen __Zufallsprozess__. Aus Signale und Systeme kennt man seine Autokorrelation. Für einen Prozess mit Erwartungswert $0$ ist sie die Kovarianz $\mathbb{E}[X_nX_{n+k}]$ zweier Werte im Abstand $k$; hängt sie nur vom Abstand $k$ ab und nicht vom Zeitpunkt $n$, heißt der Prozess (schwach) stationär. Bei $k=0$ ist sie die Varianz, also die Leistung. Weißes Rauschen hat $\mathbb{E}[X_nX_{n+k}]=0$ für $k\ne0$: Seine Abtastwerte sind unkorreliert, und deshalb ist sein Leistungsdichtespektrum flach. Die meisten Signale sind nicht weiß; ihre Abtastwerte sind korreliert, und eine Folge von Abtastwerten ist dann keine i.i.d. Stichprobe im Sinn von Unterabschnitt [9.6](mehrere-zufallsvariablen.html#stufe-9-6).
:::

:::aufgabe Aufgabe 29 ★ Kovarianz aus einer Tabelle
<span class="anker" id="aufg-29"></span>

Zwei Zufallsvariablen $X,Y\in\{0,1\}$ haben $P(0,0)=0{,}4$, $P(0,1)=0{,}1$, $P(1,0)=0{,}1$ und $P(1,1)=0{,}4$.

<ol class="al">

<li>

Berechne $\mathbb{E}[X]$, $\mathbb{E}[Y]$, $\mathbb{E}[XY]$ und $\operatorname{Cov}(X,Y)$.

</li>

<li>

Berechne den Korrelationskoeffizienten.

</li>

</ol>

:::loesung
(a) $\mathbb{E}[X]=0{,}1+0{,}4=0{,}5$, ebenso $\mathbb{E}[Y]=0{,}5$; $\mathbb{E}[XY]=P(1,1)=0{,}4$; $\operatorname{Cov}(X,Y)=0{,}4-0{,}25=0{,}15$.

(b) $\operatorname{Var}(X)=\operatorname{Var}(Y)=0{,}5\cdot0{,}5=0{,}25$, also $\rho=0{,}15/0{,}25=0{,}6$.
:::
:::

:::aufgabe Aufgabe 30 ★★ Die Differenzmessung
<span class="anker" id="aufg-30"></span>

Zwei Sensoren messen dieselbe Größe; ihr Rauschen $X$ und $Y$ hat die Standardabweichungen $2\,\mathrm{mV}$ und $3\,\mathrm{mV}$ und den Korrelationskoeffizienten $\rho$.

<ol class="al">

<li>

Berechne $\operatorname{Var}(X+Y)$ und $\operatorname{Var}(X-Y)$ für $\rho=0{,}5$.

</li>

<li>

Wie verhält sich $\operatorname{Var}(X-Y)$ für $\rho\to1$? Warum misst man deshalb oft die Differenz zweier Signale, die dieselbe Störung abbekommen?

</li>

<li>

Für welches $\rho$ ist $\operatorname{Var}(X-Y)$ am kleinsten, und welchen Wert hat es dann?

</li>

</ol>

:::loesung
(a) $\operatorname{Cov}(X,Y)=0{,}5\cdot2\cdot3=3\,\mathrm{mV}^2$. $\operatorname{Var}(X+Y)=4+9+6=19\,\mathrm{mV}^2$ und $\operatorname{Var}(X-Y)=4+9-6=7\,\mathrm{mV}^2$.

(b) $\operatorname{Var}(X-Y)=13-12\rho$ geht für $\rho\to1$ gegen $1\,\mathrm{mV}^2$. Je stärker die Störungen gemeinsam schwanken, desto mehr heben sie sich in der Differenz auf. Ein Differenzverstärker nutzt das: Eine Störung, die beide Leitungen gleich trifft, erscheint in der Differenz nicht. Wären die beiden Störungen auch gleich groß, so würden sie sich bei $\rho=1$ ganz aufheben.

(c) $13-12\rho$ ist am kleinsten bei $\rho=1$, mit dem Wert $1\,\mathrm{mV}^2=(\sigma_Y-\sigma_X)^2$.
:::
:::

:::aufgabe Aufgabe 31 ★★ Die Wohnungen
<span class="anker" id="aufg-31"></span>

Die vier Wohnungen aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) haben die Flächen $(60,\,40,\,90,\,70)$ und die Zimmerzahlen $(2,\,1,\,4,\,3)$.

<ol class="al">

<li>

Berechne die empirische Kovarianz von Fläche und Zimmerzahl und den empirischen Korrelationskoeffizienten.

</li>

<li>

Wie ändern sich beide, wenn die Fläche in $\mathrm{dm}^2$ statt in $\mathrm m^2$ angegeben wird?

</li>

</ol>

:::loesung
(a) Die Mittelwerte sind $65\,\mathrm m^2$ und $2{,}5$ Zimmer. Die zentrierten Flächen sind $-5$, $-25$, $25$, $5$, die zentrierten Zimmerzahlen $-0{,}5$, $-1{,}5$, $1{,}5$, $0{,}5$. Also ist $\operatorname{cov}=\tfrac14\,(2{,}5+37{,}5+37{,}5+2{,}5)=20\,\mathrm m^2$. Mit $\operatorname{std}^2=325\,\mathrm m^4$ für die Flächen und $1{,}25$ für die Zimmer ist $\operatorname{corr}=20/\sqrt{325\cdot1{,}25}\approx0{,}992$: Fläche und Zimmerzahl hängen in diesen Daten fast linear zusammen.

(b) In $\mathrm{dm}^2$ sind alle Flächen und Abweichungen hundertmal so groß: Die Kovarianz wird $2\,000$, der Korrelationskoeffizient bleibt $0{,}992$.
:::
:::

:::aufgabe Aufgabe 32 ★★★ Symmetrie macht unkorreliert
<span class="anker" id="aufg-32"></span>

<ol class="al">

<li>

Es sei $X$ symmetrisch um $0$ verteilt, das heißt $X$ und $-X$ haben dieselbe Verteilung, und $\mathbb{E}[X^4]$ sei endlich. Zeige $\operatorname{Cov}(X,X^2)=0$.

</li>

<li>

Gib ein Beispiel für zwei abhängige Zufallsvariablen mit Kovarianz null, bei denen keine eine Funktion der anderen ist.

</li>

</ol>

:::loesung
(a) Weil $X$ und $-X$ dieselbe Verteilung haben, ist $\mathbb{E}[X]=\mathbb{E}[-X]=-\mathbb{E}[X]$, also $\mathbb{E}[X]=0$, und ebenso $\mathbb{E}[X^3]=0$. Damit ist $\operatorname{Cov}(X,X^2)=\mathbb{E}[X^3]-\mathbb{E}[X]\,\mathbb{E}[X^2]=0$. Die Endlichkeit von $\mathbb{E}[X^4]$ sichert, dass alle vorkommenden Erwartungswerte existieren.

(b) Die Punkte in Abb. [13](#abb-13) (f): $Y=VX$ mit einem zufälligen Vorzeichen $V$. Kennt man $X$, so ist $Y$ nicht festgelegt, denn es bleiben $\pm X$; kennt man $Y$, so ist $X$ ebenso wenig festgelegt. Ein Beispiel mit endlich vielen Werten: $(X,Y)$ sei gleich wahrscheinlich einer der Punkte $(1,0)$, $(-1,0)$, $(0,1)$, $(0,-1)$. Dann ist $\mathbb{E}[X]=\mathbb{E}[Y]=\mathbb{E}[XY]=0$, also $\operatorname{Cov}=0$; aber aus $X=1$ folgt $Y=0$, während $P(Y=0)=\tfrac12$ ist.
:::
:::
