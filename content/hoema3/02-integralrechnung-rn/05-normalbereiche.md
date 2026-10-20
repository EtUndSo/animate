---
title: Integration über Normalbereiche
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020500
summary: Von Grund auf – wie man ein Integral über eine krumme Form praktisch ausrechnet. Leitbild ist ein Brot aus der Backform, das man Scheibe für Scheibe am Stück schneiden kann; die Enden jeder Scheibe wandern mit dem Messer. Solche Formen heißen Normalbereiche. Über sie wird das Integral zu gewöhnlichen Integralen mit wandernden Grenzen. Mit Beweis über gestreckte Scheiben, Flächeninhalt, Abschätzung, Zerlegung krummer Formen, räumlichen Normalbereichen und einer Beispiel-Seite (Linse, Ring, Tetraeder, zwei Zylinder).
tags: Normalbereich, iteriertes Integral, variable Grenzen, Doppelintegral, Dreifachintegral, Fläche, Zerlegung, räumlicher Normalbereich
---

## Anschaulich

Der vorige Artikel hat geklärt, **was** das Integral über eine Form ist: Man stellt sie in einen Kasten und setzt die
Funktion daneben durch null fort. **Wie** man es ausrechnet, blieb offen — bis auf den Kuchen aus der Springform, bei dem
jede Scheibe ein einziges Intervall war.

**Das Leitbild:** Wieder ein Brot aus der Backform, und wieder wird es in Scheiben geschnitten. Bei vielen Formen hat das
eine angenehme Eigenschaft: Jede Scheibe ist **ein Stück ohne Lücke**. Steht das Messer bei $y$, reicht die Scheibe von
der linken Wand bis zur rechten. Rückt das Messer weiter, wandern beide Enden stetig mit. Solche Formen heißen
__Normalbereiche__.

Für sie wird das Integral zu zwei gewöhnlichen Integralen: innen über die Scheibe, mit Grenzen, die von der Stellung des
Messers abhängen; außen über alle Stellungen des Messers. Das ist die Lage der Leibnizregel aus dem ersten Artikel — eine
Fläche zwischen wandernden Grenzen.

Nicht jede Form ist so gutmütig. Beim Ring zerfällt die Scheibe durch die Mitte in zwei Stücke; dann zerlegt man die Form
zuerst in Teile, die gutmütig sind. In drei Dimensionen steht über jedem Punkt der Grundform ein senkrechtes Stäbchen vom
Boden des Brots bis zur Kruste.

:::grafik
Szene: hoema3/integralrechnung-rn/05-scheiben-am-stueck · Vorlage: normalbereich-scan-2d
Eine Backform in der Ebene zwischen einer linken Randkurve $\alpha(y)$ und einer rechten $\beta(y)$ über $[c,d]$. Ein
waagerechtes Messer fährt von $c$ nach $d$; die aktuelle Scheibe reicht von $\alpha(y)$ bis $\beta(y)$, ihre Enden gleiten
an den Wänden entlang. Daneben ein Ring, bei dem das Messer durch die Mitte zwei getrennte Stücke schneidet. Unten der
3D-Fall: über einer Grundform $D$ senkrechte Stäbchen vom Boden $\varphi(x,y)$ bis zur Kruste $\psi(x,y)$. Kernaussage:
In einem Normalbereich ist jede Scheibe ein Stück, dessen Enden mit dem Messer wandern. (Rot = Form, orange = aktuelle
Scheibe bzw. Stäbchen, blau = Randkurven, grau = Achsen.)
:::

## Was ist ein Normalbereich?

**Die Akteure:** ein Intervall $[c,d]$ der Messerstellungen und zwei stetige Randfunktionen
$\alpha,\beta:[c,d]\to\mathbb{R}$ mit $\alpha\le\beta$, die linke und die rechte Wand. Ein __Normalbereich__ ist die Menge
der Punkte zwischen diesen Wänden. Beim zweiten Typ tauschen $x$ und $y$ die Rollen, mit stetigen Randfunktionen
$\gamma,\delta:[a,b]\to\mathbb{R}$ und $\gamma\le\delta$, der unteren und der oberen Wand:

:::formel Definition
$$D = \big\{(x,y)\in\mathbb{R}^2 \;:\; \alpha(y)\le x\le\beta(y),\ c\le y\le d\big\} \qquad\text{(Typ 1)},$$

$$D = \big\{(x,y)\in\mathbb{R}^2 \;:\; \gamma(x)\le y\le\delta(x),\ a\le x\le b\big\} \qquad\text{(Typ 2)}.$$
:::

**So liest man das:** Beim Typ 1 steht das Messer waagerecht. Zu jeder Höhe $y\in[c,d]$ gehört genau ein Intervall von
$x$-Werten, von $\alpha(y)$ bis $\beta(y)$ — eine Scheibe am Stück. Beim Typ 2 steht das Messer senkrecht, und zu jedem
$x\in[a,b]$ gehört das Intervall der $y$-Werte von $\gamma(x)$ bis $\delta(x)$.

Ein Normalbereich heißt __regulär__, wenn seine Randfunktionen sogar stetig differenzierbar sind — die Wände haben dann
überall eine Tangente mit endlicher Steigung. Für das Integral selbst genügt Stetigkeit; wozu man die Regularität
braucht, steht weiter unten.

**Im Bild:** Eine Backform, die man in einer Richtung Scheibe für Scheibe schneiden kann, ohne dass eine Scheibe in Stücke
zerfällt. Die Enden jeder Scheibe liegen auf den beiden Wänden und wandern beim Weiterrücken des Messers ohne Sprünge.

Normalbereiche sind abgeschlossen und beschränkt; der vorige Artikel erklärt also, was das Integral über sie ist.

:::herleitung
Für den Typ 1. **Beschränkt:** $\alpha$ und $\beta$ sind auf dem kompakten Intervall $[c,d]$ stetig, also beschränkt. Damit
liegt $D$ im Rechteck aus den $x$ zwischen dem kleinsten Wert von $\alpha$ und dem größten von $\beta$ und den $y$ aus
$[c,d]$.

**Abgeschlossen:** Man setzt $\alpha$ und $\beta$ links von $c$ und rechts von $d$ konstant fort, mit ihren Werten am
Rand; dann sind sie auf ganz $\mathbb{R}$ stetig. $D$ ist durch vier Ungleichungen mit stetigen Funktionen auf
$\mathbb{R}^2$ beschrieben,

$$\alpha(y)-x\le0, \qquad x-\beta(y)\le0, \qquad c-y\le0, \qquad y-d\le0,$$

und solche Mengen sind nach dem vorigen Artikel abgeschlossen. Für den Typ 2 tauschen $x$ und $y$ die Rollen.
:::

::::beispiel Normalbereich oder nicht?
**(a) Die Linse** zwischen Parabel und Gerade,

$$L = \big\{(x,y)\in\mathbb{R}^2 \;:\; x^2\le y\le x,\ 0\le x\le1\big\},$$

ist ein Normalbereich vom Typ 2 mit

$$\gamma(x) = x^2, \qquad \delta(x) = x.$$

Sie ist auch einer vom Typ 1. Bei fester Höhe $y\in[0,1]$ verlangen die Bedingungen nämlich

$$y\le x, \qquad x\le\sqrt y,$$

denn aus $x^2\le y$ folgt für nichtnegative $x$, dass $x$ höchstens $\sqrt y$ ist. Also

$$\alpha(y) = y, \qquad \beta(y) = \sqrt y.$$

Als Typ 2 ist sie regulär. Als Typ 1 ist sie es nicht, denn $\sqrt y$ hat bei $y=0$ eine senkrechte Tangente — ob ein
Bereich regulär beschrieben ist, hängt also von der Schnittrichtung ab.

**(b) Die Kreisscheibe** $S_1$ vom Radius $1$ ist ein Normalbereich vom Typ 1 mit

$$\alpha(y) = -\sqrt{1-y^2}, \qquad \beta(y) = \sqrt{1-y^2}, \qquad y\in[-1,1],$$

und aus Symmetriegründen auch einer vom Typ 2. Im Skript sind die beiden Wände vertauscht notiert; die linke Wand ist die
mit dem Minuszeichen. Regulär ist diese Beschreibung nicht: Die Steigung der Wände wird an den Polen unendlich.

:::herleitung
Die Ableitung der rechten Wand ist

$$\beta'(y) = \frac{-y}{\sqrt{1-y^2}},$$

und für $y\to\pm1$ geht der Nenner gegen null, während der Zähler gegen $\mp1$ geht — die Steigung wächst über alle Grenzen.
:::

**(c) Der Ring**

$$A = \big\{(x,y)\in\mathbb{R}^2 \;:\; 1\le x^2+y^2\le4\big\}$$

ist kein Normalbereich. In der Höhe $y=0$ besteht die Scheibe aus zwei Stücken,

$$\{x \;:\; 1\le x^2\le4\} = [-2,-1]\cup[1,2],$$

also nicht aus einem Intervall; bei $x=0$ ist es genauso. Weder Typ 1 noch Typ 2 passt.

**Im Bild:** Linse und Kreisscheibe lassen sich in beiden Richtungen am Stück schneiden. Beim Ring trennt das Messer durch
die Mitte zwei Stücke ab.
::::

## Das Integral über einen Normalbereich

Für einen Normalbereich $D$ und eine stetige Funktion $f:D\to\mathbb{R}$ existiert das Integral über $D$. Es ist ein
iteriertes Integral mit wandernden inneren Grenzen. Das Volumenelement schreiben wir hier mit den Koordinaten als $d(x,y)$;
das Skript schreibt an dieser Stelle $dx\,dy$.

:::formel Satz
$$\int_D f(x,y)\,d(x,y) = \int_c^d\bigg(\int_{\alpha(y)}^{\beta(y)} f(x,y)\,dx\bigg)dy \qquad\text{(Typ 1)},$$

$$\int_D f(x,y)\,d(x,y) = \int_a^b\bigg(\int_{\gamma(x)}^{\delta(x)} f(x,y)\,dy\bigg)dx \qquad\text{(Typ 2)}.$$
:::

**So liest man das:** Die **inneren** Grenzen hängen von der äußeren Variablen ab — sie sagen, wo die Scheibe an dieser
Stelle beginnt und endet. Die **äußeren** Grenzen sind feste Zahlen, denn am Ende muss eine Zahl herauskommen. Eingabe ist
die Funktion $f$ auf $D$, Ausgabe eine Zahl.

**Im Bild:** Erst misst man eine Scheibe — eine Fläche zwischen wandernden Grenzen, wie bei der Leibnizregel —, dann
stapelt man die Scheiben.

:::grafik
Szene: hoema3/integralrechnung-rn/05-zieharmonika · Vorlage: normalbereich-scan-2d
Ein Normalbereich vom Typ 1 mit Brot der Höhe $f$. Das Messer steht bei $y$, die Scheibe reicht von $\alpha(y)$ bis
$\beta(y)$. Ein Knopf „strecken" zieht jede Scheibe wie eine Ziehharmonika auf die feste Breite $[0,1]$; danach sieht man
über einem festen Intervall eine Kurve, die sich mit $y$ stetig verformt — die Lage aus dem ersten Artikel. Kernaussage:
Gestreckt auf eine feste Breite, wird jede Scheibe zu einem gewöhnlichen Parameterintegral. (Rot = Brot, orange =
aktuelle Scheibe, blau = Wände, grau = Achsen.)
:::

:::herleitung
Für den Typ 1, in vier Schritten.

**Schritt 1: der Kasten.** Mit dem kleinsten Wert $a_0$ von $\alpha$ und dem größten Wert $b_0$ von $\beta$ liegt $D$ im
Rechteck

$$Q = [a_0,b_0]\times[c,d].$$

**Schritt 2: eine Scheibe.** Bei fester Höhe $y\in[c,d]$ ist die Fortsetzung $x\mapsto\bar f(x,y)$ auf
$[\alpha(y),\beta(y)]$ gleich $f$ und daneben null — stückweise stetig mit höchstens zwei Sprüngen, also integrierbar
(HM1). Ihr Integral ist die Scheibenfläche:

$$\int_{a_0}^{b_0}\bar f(x,y)\,dx = \int_{\alpha(y)}^{\beta(y)} f(x,y)\,dx =: s(y).$$

**Schritt 3: Die Scheibenfläche ist stetig.** Man streckt jede Scheibe auf die feste Breite $[0,1]$, mit der Substitution

$$x = \alpha(y)+t\,\big(\beta(y)-\alpha(y)\big), \qquad dx = \big(\beta(y)-\alpha(y)\big)\,dt, \qquad t\in[0,1].$$

Damit wird

$$s(y) = \big(\beta(y)-\alpha(y)\big)\int_0^1 f\Big(\alpha(y)+t\,\big(\beta(y)-\alpha(y)\big),\,y\Big)\,dt.$$

Der Integrand ist eine stetige Funktion von $(t,y)$ auf dem Rechteck $[0,1]\times[c,d]$, denn der eingesetzte Punkt liegt
für jedes $t$ in $D$. Nach dem Stetigkeitssatz für Parameterintegrale (erster Artikel, Parameter im abgeschlossenen
Intervall) ist das Integral stetig in $y$, und der Vorfaktor ist es auch.

**Schritt 4: der Stapel.** Als stetige Funktion ist $s$ auf $[c,d]$ integrierbar. Das Mehrfachintegral integriert zuerst
über $x$, dann über $y$, also

$$\int_D f(x,y)\,d(x,y) = \int_Q\bar f(x,y)\,d(x,y) = \int_c^d s(y)\,dy.$$

**Typ 2.** Mit vertauschten Rollen zeigt dieselbe Rechnung, dass das iterierte Integral „erst über $y$, dann über $x$"
existiert. Dass es dasselbe Integral über $D$ ist, sichert die Aussage des vorigen Artikels: Jede Integrationsreihenfolge
liefert denselben Wert.

**Im Bild:** Gestreckt auf dieselbe Breite, sieht das Messer über einem festen Intervall eine Kurve, die sich mit $y$ ohne
Sprünge verformt — genau die Lage des Stetigkeitssatzes. Die Wand des gebackenen Brots ist dabei kein Hindernis mehr, weil
sie immer an den Enden der Scheibe steht.
:::

::::beispiel Die Linse, in beiden Richtungen
Auf der Linse

$$L = \big\{(x,y)\in\mathbb{R}^2 \;:\; x^2\le y\le x,\ 0\le x\le1\big\}$$

liegt ein Brot der Höhe

$$f(x,y) = x+y.$$

**Als Typ 2** (senkrechte Scheiben von $x^2$ bis $x$):

$$\int_{x^2}^{x}(x+y)\,dy = \Big[xy+\frac{y^2}{2}\Big]_{y=x^2}^{y=x} = \frac32\,x^2-x^3-\frac12\,x^4,$$

$$\int_0^1\Big(\frac32\,x^2-x^3-\frac12\,x^4\Big)dx = \frac12-\frac14-\frac1{10} = \frac{3}{20}.$$

**Als Typ 1** (waagerechte Scheiben von $y$ bis $\sqrt y$):

$$\int_{y}^{\sqrt y}(x+y)\,dx = \Big[\frac{x^2}{2}+xy\Big]_{x=y}^{x=\sqrt y} = \frac{y}{2}+y^{3/2}-\frac32\,y^2,$$

$$\int_0^1\Big(\frac{y}{2}+y^{3/2}-\frac32\,y^2\Big)dy = \frac14+\frac25-\frac12 = \frac{3}{20}.$$

**Im Bild:** Dasselbe Brot, einmal senkrecht und einmal waagerecht geschnitten. Die Scheiben sehen ganz verschieden aus —
die Summe ist dieselbe.
::::

## Flächeninhalt und Abschätzung

Für die Konstante $1$ misst das innere Integral die **Länge** der Scheibe. Der Flächeninhalt ist dann das Integral der
Scheibenlängen:

:::formel
$$\lvert D\rvert = \int_c^d \ell(y)\,dy, \qquad \ell(y) := \beta(y)-\alpha(y).$$
:::

**So liest man das:** $\ell(y)$ ist die Länge der Scheibe in der Höhe $y$, der Abstand der beiden Wände. Beim Typ 2 steht
dort die Länge zwischen unterer und oberer Wand. Das ist das Prinzip von Cavalieri aus dem vorigen Artikel, eine Dimension
tiefer.

:::herleitung
Mit $f=1$ ist das innere Integral im Satz

$$\int_{\alpha(y)}^{\beta(y)} 1\,dx = \beta(y)-\alpha(y) = \ell(y),$$

und das Integral der Eins über $D$ ist nach Definition der Flächeninhalt.
:::

**Die Abschätzung.** Wie für Quader gilt: Der Betrag des Integrals ist höchstens Fläche mal größter Betrag.

$$\Big\lvert\int_D f(x,y)\,d(x,y)\Big\rvert \le \lvert D\rvert\,\sup_{(x,y)\in D}\lvert f(x,y)\rvert.$$

**Im Bild:** Das Brot passt in einen Kasten mit der Grundfläche der Form und der Höhe seines höchsten Punkts — nur hat
dieser Kasten jetzt die Form der Backform.

:::herleitung
Sei $m$ das Maximum von $\lvert f\rvert$ auf $D$; es existiert, weil $D$ kompakt ist. Die Fortsetzung liegt zwischen
zwei Vielfachen der Indikatorfunktion,

$$-m\,\bar 1_D \le \bar f \le m\,\bar 1_D,$$

denn auf $D$ gilt das für $f$, und daneben sind alle drei null. Mit Monotonie und Linearität für Integrale über Mengen
(voriger Artikel) folgt

$$-m\,\lvert D\rvert \le \int_D f(x,y)\,d(x,y) \le m\,\lvert D\rvert.$$
:::

::::beispiel Fläche und Abschätzung an der Linse
**Der Flächeninhalt** der Linse, in beiden Richtungen:

$$\lvert L\rvert = \int_0^1\big(x-x^2\big)\,dx = \frac12-\frac13 = \frac16, \qquad \lvert L\rvert = \int_0^1\big(\sqrt y-y\big)\,dy = \frac23-\frac12 = \frac16.$$

**Die Abschätzung** für die Höhe $x+y$: Auf $L$ ist $y$ höchstens $x$, also die Höhe höchstens $2x$ und damit höchstens
$2$; der Wert $2$ wird in der Ecke $(1,1)$ angenommen. Damit

$$\frac{3}{20} \le \frac16\cdot2 = \frac13.$$

**Im Bild:** Das Brot füllt seinen linsenförmigen Kasten der Höhe $2$ zu knapp der Hälfte, denn

$$\frac{3/20}{1/3} = \frac{9}{20}.$$
::::

## Zusammengesetzte Bereiche

Gängige Formen lassen sich aus **endlich vielen** regulären Normalbereichen $D_1,\ldots,D_N$ zusammensetzen, die sich
höchstens längs ihrer Randkurven überlappen. Dann integriert man stückweise und addiert:

$$\int_D f(x,y)\,d(x,y) = \sum_{j=1}^{N}\int_{D_j} f(x,y)\,d(x,y).$$

Das Ergebnis hängt nicht davon ab, wie man zerlegt.

**Im Bild:** Eine Form, deren Scheiben zerfallen würden, schneidet man zuerst in Stücke, die man am Stück schneiden kann —
und legt die Stücke danach wieder zusammen.

:::herleitung
**Der einfachste Fall.** Zwei Bereiche vom Typ 1 über demselben Intervall $[c,d]$ liegen nebeneinander und teilen sich die
Wand: Die rechte Wand des linken Bereichs ist die linke Wand des rechten. In jeder Höhe $y$ sind ihre Scheiben dann zwei
aneinanderstoßende Intervalle, und das Integral über ihre Vereinigung zerfällt nach HM1 in die Summe:

$$\int_{\alpha_1(y)}^{\beta_2(y)} f\,dx = \int_{\alpha_1(y)}^{\beta_1(y)} f\,dx + \int_{\beta_1(y)}^{\beta_2(y)} f\,dx \qquad\text{mit } \beta_1=\alpha_2.$$

Integriert man über $y$, addieren sich die beiden Integrale.

**Allgemein.** Die Indikatorfunktion von $D$ und die Summe der Indikatorfunktionen der $D_j$ unterscheiden sich nur auf
den Überlappungen, also auf Stücken von Randkurven. Eine solche Kurve ist der Graph einer stetigen Funktion über einem
kompakten Intervall und damit eine Nullmenge: Man teilt das Intervall in $N$ gleiche Stücke, auf denen die Funktion
wegen der gleichmäßigen Stetigkeit um weniger als $\eta>0$ schwankt. Jedes Kurvenstück liegt dann in einem Rechteck der
Breite $2\eta$, und alle Rechtecke zusammen haben höchstens die Fläche $2\eta$ mal die Intervalllänge — beliebig klein.
Funktionen, die sich nur auf einer Nullmenge unterscheiden, haben dasselbe Integral (Lebesgue, voriger Artikel); mit der
Linearität folgt die Summe. Weil jede Zerlegung das Integral über $D$ ergibt, hängt das Ergebnis nicht von ihr ab.
:::

**Wozu regulär?** Für das Integral genügt die Stetigkeit der Wände, wie der Satz zeigt. Glatte Wände braucht man erst, wenn
man über den Rand selbst integriert oder die Grenzen ableitet. Der Beweis des Satzes von Stokes in der Ebene, später im
Skript, benutzt genau das: die Leibnizregel mit den Ableitungen der Randfunktionen. Darum zerlegt man auch Formen wie die
Kreisscheibe, die zwar Normalbereiche sind, aber keine regulären, in reguläre Stücke.

::::beispiel Kreisscheibe und Ring zerlegt
**(a) Die Kreisscheibe in drei reguläre Stücke.** Mit

$$s_0 = \frac{1}{\sqrt2}$$

zerlegt man $S_1$ in ein Band und zwei Kappen:

- das **Band** $D_1$ der Höhen $\lvert y\rvert\le s_0$, als Typ 1 mit den Wänden $\pm\sqrt{1-y^2}$;
- die **obere Kappe** $D_2$, als Typ 2 über $\lvert x\rvert\le s_0$, von der unteren Wand $s_0$ bis zur oberen
  $\sqrt{1-x^2}$;
- die **untere Kappe** $D_3$, ihr Spiegelbild.

Alle Wände sind dort stetig differenzierbar, weil der Ausdruck unter der Wurzel nie in die Nähe von null kommt: Auf diesen Intervallen ist
$1-y^2$ bzw. $1-x^2$ mindestens $\tfrac12$. Mit $y=\sin\theta$ ist

$$\int_{-s_0}^{s_0}\sqrt{1-y^2}\,dy = \int_{-\pi/4}^{\pi/4}\cos^2\theta\,d\theta = \Big[\frac{\theta}{2}+\frac{\sin2\theta}{4}\Big]_{-\pi/4}^{\pi/4} = \frac{\pi}{4}+\frac12.$$

Damit

$$\lvert D_1\rvert = 2\Big(\frac{\pi}{4}+\frac12\Big) = \frac{\pi}{2}+1, \qquad \lvert D_2\rvert = \lvert D_3\rvert = \Big(\frac{\pi}{4}+\frac12\Big)-2s_0^2 = \frac{\pi}{4}-\frac12.$$

Zusammen ergibt das $\pi$ — wie im vorigen Artikel, als die Scheibe noch in einem Stück beschrieben war.

**(b) Der Ring in zwei Hälften.** Die obere Hälfte des Rings $A$ ist ein Normalbereich vom Typ 2 über $[-2,2]$: Die obere
Wand ist $\sqrt{4-x^2}$, die untere $\sqrt{1-x^2}$ für $\lvert x\rvert\le1$ und $0$ sonst. Diese untere Wand ist stetig,
aber nicht differenzierbar — für das Integral genügt das. Mit dem Integral der Halbkreisbögen aus dem vorigen Artikel,

$$\int_{-r}^{r}\sqrt{r^2-x^2}\,dx = \frac{\pi r^2}{2},$$

hat die obere Hälfte die Fläche

$$\int_{-2}^{2}\sqrt{4-x^2}\,dx-\int_{-1}^{1}\sqrt{1-x^2}\,dx = 2\pi-\frac{\pi}{2} = \frac{3\pi}{2}.$$

Die untere Hälfte ist ihr Spiegelbild, der ganze Ring hat also die Fläche $3\pi$ — große Scheibe minus kleine.

**Im Bild:** Bei der Kreisscheibe schneidet man die Pole ab, wo die Wände senkrecht stehen; beim Ring schneidet man ihn
längs durch, damit keine Scheibe mehr zerfällt.

:::grafik
Szene: hoema3/integralrechnung-rn/05-zerlegungen · Vorlage: normalbereich-scan-2d
Links die Kreisscheibe, zerlegt in ein waagerechtes Band (waagerechte Scheiben) und zwei Kappen oben und unten (senkrechte
Scheiben); die Trennlinien bei $y=\pm\frac{1}{\sqrt2}$ gestrichelt. Rechts der Ring, längs der $x$-Achse in zwei Hälften
geschnitten, jede mit senkrechten Scheiben von der inneren zur äußeren Wand. Kernaussage: Wo die Scheiben zerfallen oder die
Wände senkrecht stehen, zerlegt man in gutmütige Stücke. (Rot = Teilbereiche, orange = Scheiben, gestrichelt = Schnitte,
grau = Achsen.)
:::
::::

## Räumliche Normalbereiche

Dasselbe Prinzip trägt in drei Dimensionen. **Die Akteure:** ein ebener Normalbereich $D\subseteq\mathbb{R}^2$, die
Grundform, und zwei stetige Funktionen $\varphi,\psi:D\to\mathbb{R}$ mit $\varphi\le\psi$, der Boden und die Kruste des
Brots. Der __räumliche Normalbereich__ ist alles dazwischen:

$$M = \big\{(x,y,z)\in\mathbb{R}^3 \;:\; (x,y)\in D,\ \varphi(x,y)\le z\le\psi(x,y)\big\}\subseteq\mathbb{R}^3.$$

Für eine stetige Funktion $f:M\to\mathbb{R}$ gilt

:::formel Satz
$$\int_M f(x,y,z)\,d(x,y,z) = \int_D\bigg(\int_{\varphi(x,y)}^{\psi(x,y)} f(x,y,z)\,dz\bigg)d(x,y).$$
:::

**So liest man das:** Zuerst integriert man längs des senkrechten Stäbchens über $(x,y)$, vom Boden bis zur Kruste. Was
herauskommt, ist eine Funktion auf der Grundform, und über diese integriert man wie in der Ebene — $D$ ist selbst ein
Normalbereich und liefert zwei weitere Integrale. Aus einem Dreifachintegral werden drei gewöhnliche.

**Im Bild:** Wie im Artikel über Mehrfachintegrale: erst die Stäbchen wiegen, dann die Scheiben aus Stäbchen, dann den
Laib — nur reichen die Stäbchen jetzt vom gewölbten Boden bis zur gewölbten Kruste.

:::herleitung
**$M$ ist abgeschlossen und beschränkt.** Beschränkt, weil $D$ beschränkt ist und $\varphi,\psi$ auf dem kompakten $D$
beschränkt sind. Abgeschlossen: Liegt ein Punkt außerhalb, so liegt entweder $(x,y)$ außerhalb von $D$ — dann auch eine
ganze Kugel um ihn, weil $D$ abgeschlossen ist —, oder $z$ liegt über der Kruste oder unter dem Boden. Dann bleibt das
wegen der Stetigkeit von $\varphi$ und $\psi$ in einer kleinen Kugel so.

**Das Stäbchen-Integral ist stetig.** Mit der Streckung

$$z = \varphi(x,y)+t\,\big(\psi(x,y)-\varphi(x,y)\big), \qquad t\in[0,1],$$

wird das innere Integral zu

$$w(x,y) := \int_{\varphi(x,y)}^{\psi(x,y)} f\,dz = (\psi-\varphi)\int_0^1 f\big(x,y,\varphi+t\,(\psi-\varphi)\big)\,dt.$$

Der Integrand ist auf der kompakten Menge $D\times[0,1]$ stetig, also gleichmäßig stetig; dasselbe Argument wie beim
Stetigkeitssatz des ersten Artikels zeigt, dass $w$ auf $D$ stetig ist.

**Der Rest.** Über den Normalbereich $D$ lässt sich $w$ nach dem ebenen Satz integrieren. Dass das Ergebnis das Integral
über $M$ ist, sichert wie beim Typ 2 die Aussage des vorigen Artikels, dass jede Integrationsreihenfolge denselben Wert
liefert. Das Skript verlangt den Boden echt unter der Kruste; für die Formel genügt, dass er nicht darüber liegt — im
Beispiel des Skripts berühren sich beide sogar am Rand.
:::

::::beispiel Das Tetraeder
Das Tetraeder

$$T = \big\{(x,y,z)\in\mathbb{R}^3 \;:\; x,y,z\ge0,\ x+y+z\le1\big\}$$

ist ein räumlicher Normalbereich über dem Dreieck

$$D = \big\{(x,y)\in\mathbb{R}^2 \;:\; 0\le y\le 1-x,\ 0\le x\le1\big\},$$

mit dem Boden $0$ und der schrägen Kruste

$$\psi(x,y) = 1-x-y.$$

**Stäbchen** (die Höhe der Kruste):

$$\int_0^{1-x-y}1\,dz = 1-x-y.$$

**Scheiben** bei festem $x$:

$$\int_0^{1-x}(1-x-y)\,dy = \Big[(1-x)\,y-\frac{y^2}{2}\Big]_{y=0}^{y=1-x} = \frac{(1-x)^2}{2}.$$

**Der Laib:**

$$\mathrm{vol}(T) = \int_0^1\frac{(1-x)^2}{2}\,dx = \frac16.$$

**Zur Probe mit Cavalieri:** In der Höhe $z$ ist der Querschnitt das Dreieck der $x,y\ge0$ mit Summe höchstens $1-z$, mit
der Fläche $\frac12(1-z)^2$; das Integral über $z\in[0,1]$ gibt wieder $\frac16$. Auch die Pyramidenformel passt:
Grundfläche $\frac12$ mal Höhe $1$, durch $3$.

**Im Bild:** Ein Brot mit dreieckiger Grundform und schräger Kruste. Jedes Stäbchen reicht vom Brett bis zur Kruste, und
die Kruste senkt sich zur Spitze hin ab.
::::

**Schicht um Schicht.** Ist auch die Grundform $D$ ein Normalbereich, etwa vom Typ 2, so wird das Integral über $M$ zu drei
geschachtelten gewöhnlichen Integralen: innen über $z$ mit Grenzen, die von $x$ und $y$ abhängen; in der Mitte über $y$ mit
Grenzen, die von $x$ abhängen; außen über $x$ mit festen Grenzen. Der Begriff lässt sich ebenso auf beliebige Dimensionen
übertragen: Die letzte Koordinate liegt zwischen zwei stetigen Funktionen über einem Normalbereich der Dimension darunter.

::::beispiel Zwei Zylinder im Oktanten
Das Beispiel des Skripts: Zwei Zylinder vom Radius $1$ kreuzen sich rechtwinklig, der eine um die $z$-Achse, der andere
um die $y$-Achse,

$$Z_1 = \big\{x^2+y^2\le1\big\}, \qquad Z_2 = \big\{x^2+z^2\le1\big\},$$

und man nimmt den Teil im __Oktanten__ $O$ der Punkte mit drei nichtnegativen Koordinaten:

$$M = Z_1\cap Z_2\cap O.$$

**Die Beschreibung.** Bei festem $(x,y)$ verlangen $Z_2$ und $O$, dass $z$ zwischen $0$ und $\sqrt{1-x^2}$ liegt; die
Kruste hängt nur von $x$ ab. Die Grundform ergibt sich aus $Z_1$ und $O$:

$$D = \big\{(x,y)\in\mathbb{R}^2 \;:\; 0\le y\le\sqrt{1-x^2},\ 0\le x\le1\big\},$$

eine Viertelkreisscheibe, selbst ein Normalbereich vom Typ 2. Also

$$I = \int_M f\,d(x,y,z) = \int_0^1\bigg(\int_0^{\sqrt{1-x^2}}\bigg(\int_0^{\sqrt{1-x^2}} f(x,y,z)\,dz\bigg)dy\bigg)dx.$$

**Für die Funktion** $x^2+y^2+z^2$, mit der Abkürzung

$$w = \sqrt{1-x^2}, \qquad w^2 = 1-x^2:$$

Innen, über $z$:

$$\int_0^w\big(x^2+y^2+z^2\big)\,dz = \big(x^2+y^2\big)\,w+\frac{w^3}{3}.$$

In der Mitte, über $y$:

$$\int_0^w\Big(\big(x^2+y^2\big)\,w+\frac{w^3}{3}\Big)dy = x^2w^2+\frac{w^4}{3}+\frac{w^4}{3} = x^2\big(1-x^2\big)+\frac23\big(1-x^2\big)^2.$$

Außen, über $x$:

$$I = \int_0^1\Big(x^2-x^4+\frac23\big(1-2x^2+x^4\big)\Big)dx = \frac13-\frac15+\frac23\cdot\frac{8}{15} = \frac{2}{15}+\frac{16}{45} = \frac{22}{45}.$$

**Das Volumen** — die Funktion $1$ — ist noch einfacher:

$$\mathrm{vol}(M) = \int_0^1\bigg(\int_0^{w}w\,dy\bigg)dx = \int_0^1\big(1-x^2\big)\,dx = \frac23.$$

**Im Bild:** Schneidet man bei festem $x$, ist der Querschnitt ein Quadrat: $y$ und $z$ laufen beide von $0$ bis
$\sqrt{1-x^2}$. Seine Fläche ist $1-x^2$ — Cavalieri längs der $x$-Achse gibt sofort $\frac23$. Der ganze
Durchdringungskörper beider Zylinder besteht aus acht solchen Stücken und hat das Volumen $\frac{16}{3}$.

:::grafik
Szene: hoema3/integralrechnung-rn/05-zwei-zylinder · Vorlage: tetraeder-schichtung-3d
Zwei Zylinder vom Radius $1$, rechtwinklig gekreuzt; hervorgehoben ihr gemeinsamer Teil im Oktanten. Ein Regler
verschiebt eine Schnittebene bei festem $x$: Der Querschnitt ist ein Quadrat der Seitenlänge $\sqrt{1-x^2}$. Darunter die
Grundform, eine Viertelkreisscheibe, mit einem Stäbchen vom Boden $0$ bis zur Kruste $\sqrt{1-x^2}$. Kernaussage: Der
Körper ist ein räumlicher Normalbereich über einer Viertelkreisscheibe. (Rot = Körper, orange = Stäbchen bzw. Querschnitt,
blau = Zylinderflächen, grau = Achsen.)
:::
::::

## Bedeutung und Ausblick

Mit Normalbereichen rechnet man die allermeisten Flächen- und Volumenintegrale der Praxis aus: Massen, Ladungen,
Schwerpunkte und Trägheitsmomente realer Körper. Neue Theorie braucht man dafür nicht — nur gewöhnliche Integrale aus HM1
mit sauber gewählten Grenzen. Wie beim Satz von Fubini lohnt es sich, die Schnittrichtung klug zu wählen: Sie entscheidet,
wie einfach die Grenzen und die Stammfunktionen werden.

Bei Kreisen, Kugeln und Zylindern werden die Grenzen allerdings schnell unhandlich, voller Wurzeln. Dafür gibt es später
den __Transformationssatz__, der solche Formen in Polar-, Zylinder- oder Kugelkoordinaten zu Quadern macht. Zunächst aber
geht es um das Integrieren **längs von Wegen**, die __Kurvenintegrale__. Die glatten Randkurven regulärer Normalbereiche
kehren dort als Wege wieder, über die man integriert.

:::kern
- Ein __Normalbereich__ ist eine Form, die man Scheibe für Scheibe am Stück schneiden kann; die Enden jeder Scheibe liegen auf zwei stetigen Wänden.
- Typ 1: waagerechte Scheiben von $\alpha(y)$ bis $\beta(y)$; Typ 2: senkrechte Scheiben von $\gamma(x)$ bis $\delta(x)$.
- Das Integral wird zum iterierten Integral mit **wandernden inneren** und **festen äußeren** Grenzen.
- Beweisidee: Jede Scheibe wird auf die Breite $[0,1]$ gestreckt — dann ist sie ein gewöhnliches Parameterintegral und ändert sich stetig.
- Flächeninhalt: das Integral der Scheibenlängen, $\lvert D\rvert=\int_c^d\big(\beta(y)-\alpha(y)\big)\,dy$.
- Abschätzung: Der Betrag des Integrals ist höchstens Fläche mal größter Betrag.
- Krumme Formen wie den Ring zerlegt man in Normalbereiche und addiert; die Überlappungen sind Nullmengen.
- __Regulär__ heißt: stetig differenzierbare Wände; die Kreisscheibe zerlegt man dafür in Band und Kappen.
- __Räumlicher Normalbereich__: Stäbchen vom Boden $\varphi$ bis zur Kruste $\psi$ über einer ebenen Grundform — drei geschachtelte Integrale.
:::

:::quiz
F: Was ist ein Normalbereich, und was bedeuten Typ 1 und Typ 2 im Bild der Backform?
A: Eine Form, bei der eine Koordinate zwischen zwei stetigen Randfunktionen der anderen liegt. Typ 1: Zu jeder Höhe $y\in[c,d]$ reicht die waagerechte Scheibe von $\alpha(y)$ bis $\beta(y)$; Typ 2: Zu jedem $x\in[a,b]$ reicht die senkrechte Scheibe von $\gamma(x)$ bis $\delta(x)$. Im Bild lässt sich das Brot in einer Richtung Scheibe für Scheibe am Stück schneiden, und die Enden der Scheiben wandern stetig an den Wänden entlang.
F: Warum ist der Ring $1\le x^2+y^2\le4$ kein Normalbereich, und wie integriert man trotzdem über ihn?
A: In der Höhe $y=0$ zerfällt die Scheibe in die zwei Intervalle $[-2,-1]$ und $[1,2]$, bei $x=0$ ebenso — keine Scheibe am Stück. Man schneidet den Ring längs der $x$-Achse in zwei Hälften; jede ist ein Normalbereich vom Typ 2 mit der oberen Wand $\sqrt{4-x^2}$ und der unteren $\sqrt{1-x^2}$ bzw. $0$. Jede Hälfte hat die Fläche $\frac{3\pi}{2}$, der Ring also $3\pi$.
F: Warum dürfen die inneren Grenzen von der äußeren Variablen abhängen, die äußeren aber nicht?
A: Das innere Integral misst eine Scheibe bei fester Stellung des Messers; wo die Scheibe beginnt und endet, hängt von dieser Stellung ab. Das äußere Integral stapelt alle Scheiben und muss eine Zahl ergeben, also stehen dort feste Grenzen.
F: Warum ist die Scheibenfläche $s(y)=\int_{\alpha(y)}^{\beta(y)}f(x,y)\,dx$ stetig in $y$, obwohl die Fortsetzung durch null an den Wänden springt?
A: Man streckt jede Scheibe auf die feste Breite $[0,1]$: Mit $x=\alpha(y)+t(\beta(y)-\alpha(y))$ wird $s(y)$ zum Vorfaktor $\beta(y)-\alpha(y)$ mal einem Integral über $t\in[0,1]$ mit stetigem Integranden. Das ist ein gewöhnliches Parameterintegral, also stetig. Die Wand stört nicht, weil sie immer an den Enden der Scheibe steht.
F: Was zeigt die Rechnung an der Linse $x^2\le y\le x$ mit der Höhe $x+y$?
A: Als Typ 2 (senkrechte Scheiben von $x^2$ bis $x$) und als Typ 1 (waagerechte Scheiben von $y$ bis $\sqrt y$) ergibt sich beide Male $\frac{3}{20}$. Die Scheiben sehen ganz verschieden aus, die Summe ist dieselbe — jede Integrationsreihenfolge liefert denselben Wert.
F: Wie berechnet man den Flächeninhalt eines Normalbereichs, und was ergibt sich für die Linse?
A: Mit $f=1$ misst das innere Integral die Scheibenlänge $\ell(y)=\beta(y)-\alpha(y)$, die Fläche ist das Integral dieser Längen — Cavalieri eine Dimension tiefer. Für die Linse: $\int_0^1(x-x^2)\,dx=\frac16$ und ebenso $\int_0^1(\sqrt y-y)\,dy=\frac16$.
F: Woher kommt die Abschätzung $\lvert\int_D f\rvert\le\lvert D\rvert\sup_D\lvert f\rvert$?
A: Mit dem Maximum $m$ von $\lvert f\rvert$ liegt die Fortsetzung zwischen $-m\bar 1_D$ und $m\bar 1_D$; Monotonie und Linearität geben $-m\lvert D\rvert\le\int_D f\le m\lvert D\rvert$. Im Bild passt das Brot in einen Kasten von der Form der Backform und der Höhe des höchsten Punkts. An der Linse: $\frac{3}{20}\le\frac16\cdot2=\frac13$.
F: Warum ist das Integral über eine zerlegte Form die Summe der Teilintegrale, unabhängig von der Zerlegung?
A: Im einfachsten Fall teilen sich zwei Bereiche eine Wand; in jeder Höhe stoßen ihre Scheiben aneinander, und das 1D-Integral zerfällt in die Summe. Allgemein unterscheiden sich die Indikatorfunktionen nur auf den Überlappungen, also auf Randkurven — Nullmengen, die nichts beitragen. Weil jede Zerlegung das Integral über die ganze Form ergibt, hängt das Ergebnis nicht von ihr ab.
F: Was heißt „regulär", warum ist die übliche Beschreibung der Kreisscheibe es nicht, und wie hilft man sich?
A: Regulär heißt, dass die Wände stetig differenzierbar sind. Die Wände $\pm\sqrt{1-y^2}$ der Kreisscheibe haben an den Polen $y=\pm1$ unendliche Steigung. Man schneidet die Pole ab: ein Band $\lvert y\rvert\le\frac{1}{\sqrt2}$ mit waagerechten Scheiben und zwei Kappen mit senkrechten Scheiben, alle regulär; zusammen wieder die Fläche $\pi$. Gebraucht wird die Regularität später, etwa beim Satz von Stokes in der Ebene.
F: Wie berechnet man ein Integral über einen räumlichen Normalbereich, etwa über den Teil zweier gekreuzter Zylinder im Oktanten?
A: Zuerst längs des senkrechten Stäbchens vom Boden $\varphi$ bis zur Kruste $\psi$, dann über die ebene Grundform. Beim Skript-Beispiel liegt $z$ zwischen $0$ und $\sqrt{1-x^2}$ über der Viertelkreisscheibe $0\le y\le\sqrt{1-x^2}$, $0\le x\le1$. Für $x^2+y^2+z^2$ ergibt sich $\frac{22}{45}$, das Volumen ist $\frac23$, denn der Querschnitt bei festem $x$ ist ein Quadrat der Fläche $1-x^2$.
:::
