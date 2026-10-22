---
title: Mehrfachintegrale und der Satz von Fubini
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020300
summary: Von Grund auf – wie man eine Funktion über einen Quader im $\mathbb{R}^n$ integriert. Leitbild ist ein Brot, das man in Scheiben schneidet. Jede Scheibe ist ein Parameterintegral, das Stapeln der Scheiben das äußere Integral. Der Satz von Fubini sichert, dass die Schnittrichtung egal ist; bewiesen wird er über ein wachsendes Eckstück. Dazu ein Gegenbeispiel ohne Stetigkeit, Linearität, Monotonie, die Standardabschätzung, das Integral über $\mathbb{R}^n$ bei kompaktem Träger und eine Beispiel-Seite.
tags: Mehrfachintegral, iteriertes Integral, Satz von Fubini, Volumenintegral, Reihenfolge der Integration, kompakter Träger, Monotonie
---

## Anschaulich

Wie viel Brot steckt in einem Laib?

**Das Leitbild dieses Artikels:** Ein Brot liegt auf einem rechteckigen Schneidebrett. Über jedem Punkt $(x,y)$ des
Bretts hat es die Höhe $f(x,y)$. Gesucht ist sein **Volumen** — und genau das soll das Integral von $f$ über das
Rechteck sein.

Niemand misst ein Brot auf einmal aus. Man schneidet es in **Scheiben**. Stellt man das Messer an die Stelle $y$, zeigt
die Schnittfläche die Kurve $x\mapsto f(x,y)$. Ihre Fläche ist ein Parameterintegral wie im Artikel
[Parameterintegrale und Ableiten unter dem Integral](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/parameterintegrale.html) — das Messer ist der Schieberegler von dort.

Eine dünne Scheibe der Dicke $\Delta y$ hat ungefähr das Volumen „Schnittfläche mal Dicke". Legt man alle Scheiben wieder
zusammen, summiert man diese Volumina; im Grenzfall immer dünnerer Scheiben wird daraus ein Integral über $y$. So
entstehen zwei ineinandergeschachtelte Integrale: innen über $x$ (die Fläche einer Scheibe), außen über $y$ (der Stapel).

Man kann das Brot genauso gut in der anderen Richtung schneiden, mit dem Messer an der Stelle $x$. Es bleibt dasselbe
Brot, also muss dasselbe Volumen herauskommen. Dass die Mathematik das bestätigt, ist der __Satz von Fubini__. Er hat
großen praktischen Wert: Oft ist die eine Schnittrichtung mühsam und die andere fast geschenkt.

In drei Dimensionen trägt das Bild weiter, wenn man $f$ als **Dichte** des Teigs liest — wo Rosinen stecken, ist er
schwerer. Das Integral ist dann die **Masse** des Laibs. Man wiegt erst dünne Stäbchen, dann Scheiben aus Stäbchen, dann
den Stapel aus Scheiben.

:::grafik
Szene: hoema3/integralrechnung-rn/03-brot-in-scheiben · Vorlage: volumen-scheiben-3d
Ein Brot über dem Rechteck $[a,b]\times[c,d]$ mit der Oberseite $z=f(x,y)$. Ein Messer fährt entlang der $y$-Achse; an
jeder Stelle $y$ leuchtet die Schnittfläche unter der Kurve $x\mapsto f(x,y)$ auf, daneben wächst ein Stapel dünner
Scheiben zum ganzen Brot. Ein Umschalter dreht die Schnittrichtung: Das Messer fährt entlang der $x$-Achse, die Scheiben
zeigen $y\mapsto f(x,y)$, und der Stapel ergibt dasselbe Volumen. Kernaussage: Ein Volumen ist ein Stapel von
Scheibenflächen — in jeder Schnittrichtung derselbe. (Rot = Brot bzw. Fläche $f$, orange = aktuelle Scheibe, blau =
gestapelte Scheiben, grau = Brett und Achsen.)
:::

## Zwei Dimensionen: das Brot in Scheiben

**Die Akteure:** ein Rechteck — der zweidimensionale __Quader__ —

$$Q = [a,b]\times[c,d] = \big\{(x,y)\in\mathbb{R}^2 \;:\; a\le x\le b,\ c\le y\le d\big\}\subseteq\mathbb{R}^2$$

mit $a<b$ und $c<d$, das Brett. Dazu eine stetige Funktion $f:Q\to\mathbb{R}$, die Höhe des Brots.

**Das Zusammenspiel:** *Wie viel Brot liegt auf dem Brett?*

**Schritt 1: eine Scheibe.** Hält man $y$ fest, ist $x\mapsto f(x,y)$ eine stetige Kurve über $[a,b]$. Die Fläche
darunter ist die Fläche der Scheibe an der Stelle $y$:

$$s(y) := \int_a^b f(x,y)\,dx, \qquad y\in[c,d].$$

Das ist ein Parameterintegral: $x$ wird weg-integriert, $y$ bleibt als Parameter stehen — die Stellung des Messers.
Eingabe ist eine Zahl $y$, Ausgabe eine Fläche. Als skalare Ergebnisfunktion heißt sie klein, $s$ wie Scheibe.

**Schritt 2: der Stapel.** Die Scheibenfläche ändert sich **ohne Sprünge**, wenn das Messer wandert: $s$ ist stetig auf
$[c,d]$. Deshalb existiert das Integral über den Stapel, das __iterierte Integral__ — „iteriert", weil man ein Integral
auf das Ergebnis eines anderen anwendet:

$$\int_c^d s(y)\,dy = \int_c^d\Big(\int_a^b f(x,y)\,dx\Big)dy.$$

:::herleitung
Das ist der Stetigkeitssatz für Parameterintegrale aus dem Artikel [Parameterintegrale und Ableiten unter dem Integral](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/parameterintegrale.html), mit dem Parameter $y$ im abgeschlossenen
Intervall $[c,d]$. Kurz nachgerechnet: Das Rechteck $Q$ ist kompakt, also beschränkt und abgeschlossen. Darum ist $f$
dort __gleichmäßig stetig__ — zu jedem $\varepsilon>0$ gibt es ein $\delta>0$, das an **allen** Stellen zugleich
funktioniert. Für $y,y_0\in[c,d]$ mit $\lvert y-y_0\rvert<\delta$ gilt also

$$\lvert f(x,y)-f(x,y_0)\rvert<\varepsilon \qquad\text{für alle } x\in[a,b].$$

Dann unterscheiden sich die beiden Scheibenflächen um höchstens

$$\lvert s(y)-s(y_0)\rvert \le \int_a^b\lvert f(x,y)-f(x,y_0)\rvert\,dx \le (b-a)\,\varepsilon.$$

Eine stetige Funktion auf $[c,d]$ ist integrierbar, also existiert das äußere Integral.

**Im Bild:** Rückt das Messer um weniger als $\delta$ weiter, bleibt die neue Schnittkurve überall in einem Band der Höhe
$\varepsilon$ um die alte. Die Schnittfläche ändert sich dann höchstens um Breite mal Bandhöhe.
:::

**Im Bild:** Das innere Integral misst eine Scheibe, das äußere stapelt die Scheiben. Liest man das iterierte Integral
von innen nach außen, schneidet man das Brot erst auf und legt es dann wieder zusammen. Wo $f$ negativ ist, hängt der
Teig gewissermaßen unter dem Brett; dieses Volumen zählt negativ — so wie beim gewöhnlichen Integral eine Fläche unterhalb der Achse.

::::beispiel Der Brotkeil
Auf dem Brett

$$Q = [0,2]\times[0,1]$$

liegt ein keilförmiges Brot mit der Höhe

$$f(x,y) = x+y.$$

**Eine Scheibe.** Steht das Messer bei $y$, zeigt die Schnittfläche die Gerade $x\mapsto x+y$ über $[0,2]$:

$$s(y) = \int_0^2 (x+y)\,dx = \Big[\frac{x^2}{2}+xy\Big]_{x=0}^{x=2} = 2+2y.$$

Zur Probe: Die Scheibe ist ein Trapez mit den Randhöhen $y$ und $2+y$ und der Breite $2$. Ihre Fläche ist Breite mal
mittlere Höhe:

$$2\cdot\frac{y+(2+y)}{2} = 2+2y.$$

**Der Stapel.**

$$\int_0^1 s(y)\,dy = \int_0^1 (2+2y)\,dy = 2+1 = 3.$$

**Im Bild:** Vom vorderen zum hinteren Ende des Bretts wachsen die Scheiben gleichmäßig von der Fläche $2$ auf $4$. Im
Mittel haben sie die Fläche $3$, und der Stapel ist $1$ dick — das Volumen ist $3$.
::::

## Der Satz von Fubini: in jeder Richtung dasselbe Brot

Das iterierte Integral hat eine Richtung eingebaut: erst über $x$, dann über $y$. Schneidet man das Brot in der anderen
Richtung, mit dem Messer bei festem $x$, entsteht das iterierte Integral in umgekehrter Reihenfolge. *Kommt wirklich
dasselbe heraus?* Für stetige Funktionen ja:

:::formel Satz
$$\int_c^d\Big(\int_a^b f(x,y)\,dx\Big)dy = \int_a^b\Big(\int_c^d f(x,y)\,dy\Big)dx \qquad \text{für } f:[a,b]\times[c,d]\to\mathbb{R} \text{ stetig}.$$
:::

**So liest man das:** Links stehen Scheiben bei festem $y$, gestapelt längs der $y$-Achse. Rechts stehen Scheiben bei
festem $x$, gestapelt längs der $x$-Achse. Der Satz sagt: Beide Stapel enthalten gleich viel Brot. Das ist
eine elementare Version des Satzes von Fubini; die allgemeine gehört zur Integrationstheorie nach Lebesgue.

**Im Bild — die Beweisidee:** Statt gleich das ganze Brot zu vergleichen, misst man ein **Eckstück** über dem
Teilrechteck $[a,\xi]\times[c,\eta]$, und zwar auf beide Arten. Rückt die Kante $\xi$ ein Stück weiter, kommt bei der
einen Messung eine neue Scheibe hinzu. Bei der anderen wird jede vorhandene Scheibe um einen schmalen Streifen länger.
Beides ist dasselbe Randstück Brot. Die Differenz der beiden Messungen ändert sich also nie — und für das leere Eckstück
am Anfang ist sie null.

:::grafik
Szene: hoema3/integralrechnung-rn/03-eckstueck · Vorlage: volumen-scheiben-3d
Das Brot über $[a,b]\times[c,d]$; hervorgehoben ein Eckstück über $[a,\xi]\times[c,\eta]$. Ein Regler verschiebt die
Kante $\xi$. Linke Hälfte: das Eckstück aus Scheiben bei festem $x$ — beim Verschieben kommt rechts eine neue Scheibe
hinzu. Rechte Hälfte: dasselbe Eckstück aus Scheiben bei festem $y$ — beim Verschieben wird jede Scheibe an ihrem Ende um
einen schmalen Streifen länger. Die neuen Stücke leuchten in beiden Hälften gleich auf; eine Anzeige der Differenz
$h(\xi,\eta)$ bleibt auf $0$. Kernaussage: Beide Messungen wachsen um dasselbe Randstück, also bleiben sie gleich. (Rot =
Eckstück, orange = hinzukommendes Randstück, blau = übriges Brot, grau = Brett und Achsen.)
:::

:::herleitung
Für jede Ecke $(\xi,\eta)\in[a,b]\times[c,d]$ misst man das Eckstück auf beide Arten und bildet die Differenz. Das ergibt
eine Funktion $h:[a,b]\times[c,d]\to\mathbb{R}$:

$$h(\xi,\eta) := \int_a^\xi\Big(\int_c^\eta f(x,y)\,dy\Big)dx - \int_c^\eta\Big(\int_a^\xi f(x,y)\,dx\Big)dy.$$

**Schritt 1: Der erste Term wächst um eine Scheibe.** Der innere Ausdruck ist die Fläche der Scheibe bei festem $x$,
zwischen $c$ und $\eta$:

$$\sigma(x,\eta) := \int_c^\eta f(x,y)\,dy.$$

Als Parameterintegral ist er stetig in $x$. Nach dem Hauptsatz der Differential- und Integralrechnung wächst ein Integral
mit dem Wert seines Integranden an der oberen Grenze:

$$\frac{\partial}{\partial\xi}\int_a^\xi \sigma(x,\eta)\,dx = \sigma(\xi,\eta) = \int_c^\eta f(\xi,y)\,dy.$$

Im Bild: Rückt die Kante $\xi$ vor, kommt die Scheibe an der Stelle $x=\xi$ hinzu.

**Schritt 2: Im zweiten Term wird jede Scheibe länger.** Hier ist $\xi$ die obere Grenze jeder Scheibe bei festem $y$.
Die Ableitung nach $\xi$ liefert wieder der Hauptsatz:

$$\tau(\xi,y) := \int_a^\xi f(x,y)\,dx, \qquad \frac{\partial\tau}{\partial\xi}(\xi,y) = f(\xi,y).$$

$\tau$ ist auf $[a,b]\times[c,d]$ stetig — wie die Funktion $H$ in der Herleitung der Leibnizregel —, und seine
Ableitung $f$ ebenso. Also darf man nach dem Parameter $\xi$ unter dem Integral ableiten (erster Artikel, Parameter im
abgeschlossenen Intervall):

$$\frac{\partial}{\partial\xi}\int_c^\eta \tau(\xi,y)\,dy = \int_c^\eta \frac{\partial\tau}{\partial\xi}(\xi,y)\,dy = \int_c^\eta f(\xi,y)\,dy.$$

Im Bild: Jede Scheibe bei festem $y$ wird an ihrem Ende $x=\xi$ um einen Streifen der Höhe $f(\xi,y)$ länger. Alle
Streifen zusammen ergeben wieder die Scheibe an der Stelle $x=\xi$.

**Schritt 3: Die Differenz bleibt null.** Beide Terme wachsen gleich schnell:

$$\frac{\partial h}{\partial\xi}(\xi,\eta) = 0 \qquad\text{für alle } (\xi,\eta)\in[a,b]\times[c,d].$$

Für festes $\eta$ ist $\xi\mapsto h(\xi,\eta)$ also konstant (Mittelwertsatz). Am linken Rand $\xi=a$ ist das Eckstück
leer, und beide Terme verschwinden:

$$h(a,\eta) = \int_a^a \sigma(x,\eta)\,dx - \int_c^\eta \tau(a,y)\,dy = 0-\int_c^\eta 0\,dy = 0.$$

Also ist $h$ überall null. Für die Ecke $(\xi,\eta)=(b,d)$ ist das die Behauptung.

Ebenso verschwindet die Ableitung nach $\eta$ (dieselbe Rechnung mit vertauschten Rollen), und man könnte auch mit dem
Wert in der Ecke $(a,c)$ schließen. Für die Konstanz genügt aber schon eine der beiden Ableitungen, weil $h$ am ganzen
linken Rand verschwindet.
:::

::::beispiel Das Eckstück des Brotkeils
Für den Brotkeil

$$f(x,y) = x+y \qquad\text{auf}\qquad Q=[0,2]\times[0,1]$$

misst man das Eckstück über $[0,\xi]\times[0,\eta]$ auf beide Arten. Mit Scheiben bei festem $x$:

$$\int_0^\xi\Big(\int_0^\eta (x+y)\,dy\Big)dx = \int_0^\xi\Big(x\eta+\frac{\eta^2}{2}\Big)dx = \frac{\xi^2\eta}{2}+\frac{\xi\eta^2}{2}.$$

Mit Scheiben bei festem $y$:

$$\int_0^\eta\Big(\int_0^\xi (x+y)\,dx\Big)dy = \int_0^\eta\Big(\frac{\xi^2}{2}+\xi y\Big)dy = \frac{\xi^2\eta}{2}+\frac{\xi\eta^2}{2}.$$

Die Differenz $h$ ist also überall null. Beide Messungen wachsen mit $\xi$ gleich schnell, nämlich mit der Fläche der
Randscheibe an der Stelle $x=\xi$:

$$\frac{\partial}{\partial\xi}\Big(\frac{\xi^2\eta}{2}+\frac{\xi\eta^2}{2}\Big) = \xi\eta+\frac{\eta^2}{2} = \int_0^\eta(\xi+y)\,dy.$$

Für das ganze Brot, also die Ecke $(\xi,\eta)=(2,1)$, kommt in beiden Richtungen das Volumen heraus:

$$\frac{4\cdot1}{2}+\frac{2\cdot1}{2} = 3.$$

**Im Bild:** Bei festem $x$ geschnitten, sind die Scheiben Trapeze mit der Fläche

$$\int_0^1(x+y)\,dy = x+\frac12,$$

von $\tfrac12$ vorn bis $\tfrac52$ hinten, im Mittel $\tfrac32$, gestapelt über die Länge $2$. Wieder $3$.
::::

## Wenn die Stetigkeit fehlt

Die Stetigkeit auf dem **abgeschlossenen** Rechteck ist keine Formsache. Wird der Integrand an einer Ecke unbeschränkt,
können die beiden Reihenfolgen verschiedene Werte liefern — obwohl jedes der beiden iterierten Integrale für sich
existiert.

**Im Bild:** In der Ecke stecken dann ein unendlich hoher Berg und eine unendlich tiefe Mulde. Jede Schnittrichtung
verrechnet die beiden anders, und je nach Richtung bleibt mehr Berg oder mehr Mulde übrig. Bei stetigem $f$ kann das
nicht passieren: Auf dem kompakten Rechteck ist $f$ beschränkt, kein Teil des Brots ist unendlich groß.

::::beispiel Berg und Mulde in der Ecke
Auf dem Quadrat ohne die Ecke $(0,0)$ sei

$$f(x,y) = \frac{x^2-y^2}{(x^2+y^2)^2}, \qquad (x,y)\in[0,1]^2\setminus\{(0,0)\}.$$

Unterhalb der Diagonalen, wo $y<x$ ist, ist $f$ positiv, oberhalb negativ. Zur Ecke hin wird $\lvert f\rvert$ beliebig
groß, auf der $x$-Achse etwa ist

$$f(x,0) = \frac{1}{x^2}.$$

**Zuerst über $y$.** Für festes $x\in(0,1]$ ist der Integrand stetig in $y$, und eine Stammfunktion liefert die
Quotientenregel:

$$\frac{\partial}{\partial y}\,\frac{y}{x^2+y^2} = \frac{(x^2+y^2)-2y^2}{(x^2+y^2)^2} = \frac{x^2-y^2}{(x^2+y^2)^2}.$$

Also

$$\int_0^1 f(x,y)\,dy = \Big[\frac{y}{x^2+y^2}\Big]_{y=0}^{y=1} = \frac{1}{1+x^2}, \qquad \int_0^1\frac{dx}{1+x^2} = \arctan 1 = \frac{\pi}{4}.$$

**Zuerst über $x$.** Ebenso ist

$$\frac{\partial}{\partial x}\,\frac{-x}{x^2+y^2} = \frac{-(x^2+y^2)+2x^2}{(x^2+y^2)^2} = \frac{x^2-y^2}{(x^2+y^2)^2},$$

und für festes $y\in(0,1]$ folgt

$$\int_0^1 f(x,y)\,dx = \Big[\frac{-x}{x^2+y^2}\Big]_{x=0}^{x=1} = -\frac{1}{1+y^2}, \qquad \int_0^1\Big(-\frac{1}{1+y^2}\Big)dy = -\frac{\pi}{4}.$$

Beide iterierten Integrale existieren, aber sie sind verschieden:

$$\frac{\pi}{4} \neq -\frac{\pi}{4}.$$

**Woran es liegt.** Schon der Berg allein hat unendliches Volumen. In der Scheibe bei festem $x$ liegt er über
$0\le y\le x$ und hat dort die Fläche

$$\int_0^x f(x,y)\,dy = \Big[\frac{y}{x^2+y^2}\Big]_{y=0}^{y=x} = \frac{x}{2x^2} = \frac{1}{2x}.$$

Gestapelt über $x\in(0,1]$ divergiert das, denn $\int_0^1\frac{dx}{2x}$ ist unendlich. Die Mulde ist das Spiegelbild des
Bergs an der Diagonalen, mit umgekehrtem Vorzeichen,

$$f(y,x) = -f(x,y),$$

und damit ebenso unendlich tief.

**Im Bild:** Jede Scheibe bei festem $x$ enthält mehr Berg als Mulde, ihre Fläche $\frac{1}{1+x^2}$ ist positiv. Jede
Scheibe bei festem $y$ enthält mehr Mulde als Berg. Zwei unendliche Volumina gegeneinander verrechnet ergeben, was die
Schnittrichtung daraus macht — ähnlich wie eine nur bedingt konvergente Reihe beim Umordnen ihren Wert ändern kann.

:::grafik
Szene: hoema3/integralrechnung-rn/03-berg-und-mulde · Vorlage: flaeche-3d-schnitte
Der Graph von $f(x,y)=\frac{x^2-y^2}{(x^2+y^2)^2}$ über $[0,1]^2$, bei großer Höhe abgeschnitten: ein Berg unter der
Diagonalen, eine Mulde darüber, beide schießen zur Ecke $(0,0)$ hin ins Unendliche. Ein Messer bei festem $x$ zeigt eine
Scheibe mit mehr Berg als Mulde (Fläche $\frac{1}{1+x^2}$), ein Messer bei festem $y$ eine mit mehr Mulde (Fläche
$-\frac{1}{1+y^2}$). Kernaussage: Ohne Stetigkeit am Rand können die beiden Schnittrichtungen verschiedene Volumina
liefern. (Rot = Berg, blau = Mulde, orange = Messer und Scheibe, gestrichelt = Diagonale, grau = Achsen.)
:::
::::

**Was man stattdessen braucht.** In der Integrationstheorie nach Lebesgue darf man auch bei unbeschränkten Integranden
und unbeschränkten Gebieten vertauschen, sobald das Volumen von $\lvert f\rvert$ endlich ist. Das heißt __absolute
Integrierbarkeit__ und ist das mehrdimensionale Gegenstück zur absoluten Konvergenz aus dem vorigen Artikel. Berg und
Mulde haben dann je ein endliches Volumen, und keine Schnittrichtung kann das eine gegen das andere ausspielen. Der Beweis
(Satz von Fubini–Tonelli) sprengt den Rahmen dieser Seiten.

:::herleitung
Nur die Beweisidee; die Einzelheiten brauchen die Lebesgue-Theorie. Man zerlegt $f$ in Berg und Mulde, also in
__Positivteil__ und __Negativteil__:

$$f^+ := \max(f,0), \qquad f^- := \max(-f,0), \qquad f = f^+-f^-, \qquad \lvert f\rvert = f^++f^-.$$

**Ohne Mulde keine Auslöschung.** Für die nichtnegative Funktion $f^+$ nimmt man stetige Funktionen auf dem ganzen
Quader, die von unten gegen $f^+$ wachsen — etwa in immer größerer Höhe abgeschnitten und nahe der kritischen Stelle auf
null heruntergeblendet. Für jede von ihnen gilt der elementare Satz. Mit wachsender Abschneidehöhe steigen beide
iterierten Integrale monoton. Dass sie in beiden Reihenfolgen gegen das iterierte Integral von $f^+$ streben, sichert der
Satz von der monotonen Konvergenz. Ergebnis: Für $f^+$ liefern beide Reihenfolgen dasselbe, möglicherweise unendliche
Volumen (Satz von Tonelli). Für $f^-$ gilt dasselbe.

**Mit endlichem Volumen von $\lvert f\rvert$** sind die Volumina von Berg und Mulde endlich und hängen nicht von der
Reihenfolge ab — also auch ihre Differenz nicht, das Integral von $f$. Im Gegenbeispiel sind beide unendlich, und die
Differenz „unendlich minus unendlich" hat keinen festen Wert.
:::

## Die Reihenfolge klug wählen

Weil beide Reihenfolgen dasselbe liefern, darf man sich die **bequemere** aussuchen — und das ist oft der eigentliche
Trick einer Rechnung.

**Im Bild:** In der einen Richtung geschnitten, haben die Scheiben eine Form, deren Fläche man sofort hinschreiben kann; in
der anderen eine sperrige. Das Brot ist dasselbe.

**Faustregel:** Zuerst über die Variable integrieren, zu der der Integrand eine einfache Stammfunktion hat. Ein typisches
Signal: Vor einer Funktion von $xy$ steht als Faktor gerade die innere Ableitung nach einer der Variablen — so wie das
$x$ vor $\cos(xy)$, das beim Ableiten von $\sin(xy)$ nach $y$ entsteht.

::::beispiel Ein Doppelintegral, zwei Wege
Gesucht ist das Integral über das Quadrat $Q=[0,2\pi]^2$ von

$$f(x,y) = x\cos(xy).$$

**(a) Zuerst über $y$.** Für festes $x$ ist der Faktor $x$ die innere Ableitung von $\sin(xy)$ nach $y$:

$$\frac{\partial}{\partial y}\sin(xy) = x\cos(xy).$$

Das innere Integral ist damit geschenkt — auch für $x=0$, wo beide Seiten null sind:

$$\int_0^{2\pi} x\cos(xy)\,dy = \big[\sin(xy)\big]_{y=0}^{y=2\pi} = \sin(2\pi x).$$

Das äußere ebenso:

$$\int_0^{2\pi}\sin(2\pi x)\,dx = \Big[-\frac{\cos(2\pi x)}{2\pi}\Big]_{x=0}^{x=2\pi} = \frac{1-\cos(4\pi^2)}{2\pi} = \frac{\sin^2(2\pi^2)}{\pi}.$$

Der letzte Schritt nutzt die Doppelwinkelformel

$$1-\cos(2\alpha) = 2\sin^2\alpha \qquad\text{mit}\qquad \alpha=2\pi^2.$$

**(b) Zuerst über $x$.** Für festes $y\neq0$ braucht man partielle Integration, mit $x$ als abzuleitendem Faktor:

$$\int_0^{2\pi} x\cos(xy)\,dx = \Big[\frac{x\sin(xy)}{y}\Big]_{x=0}^{x=2\pi} - \int_0^{2\pi}\frac{\sin(xy)}{y}\,dx = \frac{2\pi\sin(2\pi y)}{y} + \frac{\cos(2\pi y)-1}{y^2}.$$

Für $y=0$ ist das innere Integral $2\pi^2$, und der Ausdruck strebt für $y\to0$ gegen denselben Wert — das Zwischenergebnis
ist stetig, wie es sein muss.

Dieses Ergebnis muss man nun über $y$ integrieren, und einzeln haben die beiden Summanden keine elementare Stammfunktion.
Man muss erkennen, dass sie zusammen die Quotientenregel rückwärts sind. Mit

$$\psi(y) = 1-\cos(2\pi y), \qquad \psi'(y) = 2\pi\sin(2\pi y)$$

steht da

$$\frac{\psi'(y)}{y}-\frac{\psi(y)}{y^2} = \frac{d}{dy}\,\frac{\psi(y)}{y}.$$

Nach l'Hospital strebt $\psi(y)/y$ für $y\to0$ gegen $\psi'(0)$, also gegen null. Damit

$$\int_0^{2\pi}\Big(\frac{2\pi\sin(2\pi y)}{y}+\frac{\cos(2\pi y)-1}{y^2}\Big)dy = \frac{\psi(2\pi)}{2\pi}-\lim_{y\to0}\frac{\psi(y)}{y} = \frac{1-\cos(4\pi^2)}{2\pi}.$$

Dasselbe Ergebnis, wie Fubini es verspricht — aber mit deutlich mehr Arbeit.

**Im Bild:** Bei festem $x$ geschnitten, zeigt jede Scheibe eine Kosinuswelle, deren Fläche man sofort hinschreibt. Bei
festem $y$ geschnitten, ist die Welle mit $x$ verstärkt — eine sperrige Form, deren Fläche erst die partielle
Integration liefert.
::::

**Produkte zerfallen.** Ist der Integrand ein Produkt aus einer Funktion von $x$ allein und einer von $y$ allein, mit
stetigen $u:[a,b]\to\mathbb{R}$ und $v:[c,d]\to\mathbb{R}$, so zerfällt das Doppelintegral in zwei gewöhnliche
Integrale:

$$\int_c^d\Big(\int_a^b u(x)\,v(y)\,dx\Big)dy = \Big(\int_a^b u(x)\,dx\Big)\Big(\int_c^d v(y)\,dy\Big).$$

**Im Bild:** Jede Scheibe zeigt dieselbe Kurve $u$, nur mit dem Faktor $v(y)$ gestreckt. Ihre Fläche ist $v(y)$ mal die
Fläche unter $u$, und der Stapel summiert die Streckfaktoren.

:::herleitung
Für die Integration über $x$ ist $v(y)$ eine Konstante und darf vor das innere Integral (Linearität):

$$\int_a^b u(x)\,v(y)\,dx = v(y)\int_a^b u(x)\,dx.$$

Das verbleibende Integral über $u$ hängt nicht von $y$ ab. Im äußeren Integral ist es deshalb ein konstanter Faktor und
darf ebenso vor das Integral:

$$\int_c^d v(y)\Big(\int_a^b u(x)\,dx\Big)dy = \Big(\int_a^b u(x)\,dx\Big)\int_c^d v(y)\,dy.$$
:::

::::beispiel Ein Brot mit Sinusbogen
Auf dem Brett

$$Q = [0,\pi]\times[0,2]$$

liegt ein Brot, dessen Querschnitt ein Sinusbogen ist, der nach hinten höher wird:

$$f(x,y) = (1+y)\sin x.$$

Das ist ein Produkt aus einer Funktion von $x$ allein und einer von $y$ allein:

$$u(x) = \sin x, \qquad v(y) = 1+y.$$

Also zerfällt das Integral:

$$\int_0^2\Big(\int_0^\pi (1+y)\sin x\,dx\Big)dy = \Big(\int_0^\pi\sin x\,dx\Big)\Big(\int_0^2(1+y)\,dy\Big) = 2\cdot4 = 8.$$

Zur Probe Scheibe für Scheibe: Bei festem $y$ hat die Scheibe die Fläche $2(1+y)$, und

$$\int_0^2 2(1+y)\,dy = 2\cdot(2+2) = 8.$$

**Im Bild:** Am vorderen Rand des Bretts ist der Bogen $1$ hoch und die Scheibe hat die Fläche $2$; am hinteren ist er $3$
hoch, mit der Fläche $6$. Alle Scheiben sind derselbe Bogen, nur gestreckt.
::::

## Beliebige Dimension: das Mehrfachintegral

**Die Akteure:** eine Dimension $n\in\mathbb{N}$ und ein $n$-dimensionaler __Quader__

$$Q = [a_1,b_1]\times\cdots\times[a_n,b_n] = \big\{\vec x=(x_1,\ldots,x_n)\in\mathbb{R}^n \;:\; a_k\le x_k\le b_k \ \text{ für } k=1,\ldots,n\big\}\subseteq\mathbb{R}^n$$

mit $a_k<b_k$. In einer Dimension ist $Q$ ein Intervall, in zwei ein Rechteck, in drei ein Klotz. Dazu eine stetige
Funktion $f:Q\to\mathbb{R}$. Das __Volumen__ des Quaders ist das Produkt seiner Kantenlängen — in zwei Dimensionen der
Flächeninhalt, in einer die Länge:

$$\lvert Q\rvert := (b_1-a_1)\cdots(b_n-a_n).$$

Man integriert nacheinander nach jeder Variablen, von innen nach außen. Das definiert das __Mehrfachintegral__ von $f$
über $Q$:

:::formel Definition
$$\int_Q f(\vec x)\,d^n x := \int_{a_n}^{b_n}\bigg(\cdots\int_{a_2}^{b_2}\bigg(\int_{a_1}^{b_1} f(x_1,\ldots,x_n)\,dx_1\bigg)dx_2\cdots\bigg)dx_n.$$
:::

**So liest man das:** Das innerste Integral behandelt $x_2,\ldots,x_n$ als feste Parameter und integriert $x_1$ weg;
übrig bleibt eine Funktion von $(x_2,\ldots,x_n)$. Das nächste Integral integriert $x_2$ weg, und so fort, bis nach $n$
Schritten eine Zahl dasteht. Eingabe ist die Funktion $f$ auf $Q$, Ausgabe eine Zahl. Für $n=2$ ist das genau das
iterierte Integral der vorigen Abschnitte.

Das Zeichen $d^n x$ ist kein Vektor, sondern das $n$-dimensionale __Volumenelement__ — das Volumen eines winzigen
Klötzchens mit den Kanten $dx_1,\ldots,dx_n$. Deshalb trägt es keinen Pfeil, anders als das Wegelement $d\vec x$ der
[Kurvenintegrale](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegral-und-orientierung.html).

**Im Bild,** mit $f$ als Dichte des Teigs in drei Dimensionen: Das innerste Integral wiegt ein dünnes Stäbchen in
$x_1$-Richtung, genauer: Es gibt seine Masse pro Querschnittsfläche an. Das mittlere wiegt eine Scheibe aus
nebeneinanderliegenden Stäbchen, das äußere den Stapel aus Scheiben — den ganzen Laib.

:::grafik
Szene: hoema3/integralrechnung-rn/03-staebchen-scheibe-laib · Vorlage: quader-dichte-3d
Ein Klotz $Q=[a_1,b_1]\times[a_2,b_2]\times[a_3,b_3]$, eingefärbt nach der Dichte $f$. Drei Stufen nacheinander: Ein
dünnes Stäbchen in $x_1$-Richtung leuchtet auf, seine Masse pro Querschnittsfläche erscheint als Zahl; die Stäbchen bei
festem $x_3$ fügen sich zu einer Scheibe; die Scheiben stapeln sich zum Klotz. Ein Umschalter wählt eine andere der sechs
Reihenfolgen, die Gesamtmasse bleibt gleich. Kernaussage: Ein Mehrfachintegral ist ein Stapel von Stapeln — in jeder
Reihenfolge. (Blau = Dichte, orange = aktuelles Stäbchen bzw. aktuelle Scheibe, rot = Ergebnis, grau = Achsen.)
:::

**Warum es existiert.** Jedes Zwischenergebnis ist wieder eine **stetige** Funktion der restlichen Variablen. Deshalb kann
man jeden Schritt ausführen — wegen dieses schrittweisen Aufbaus genügte es oben, den Fall zweier Dimensionen zu
verstehen.

:::herleitung
Man zeigt es für den ersten Schritt; die weiteren gehen genauso, mit einem Quader der nächstkleineren Dimension. Sei

$$Q' := [a_2,b_2]\times\cdots\times[a_n,b_n]\subseteq\mathbb{R}^{n-1}$$

der Quader der restlichen Variablen. Für einen Punkt $\vec p\in Q'$ mit den Koordinaten $p_2,\ldots,p_n$ schreibt man kurz
$(x_1,\vec p)$ für den Punkt $(x_1,p_2,\ldots,p_n)\in Q$ und setzt

$$s_1(\vec p) := \int_{a_1}^{b_1} f(x_1,\vec p)\,dx_1.$$

Der Quader $Q$ ist kompakt, also ist $f$ dort gleichmäßig stetig: Zu $\varepsilon>0$ gibt es ein $\delta>0$, sodass sich
die Funktionswerte an zwei Punkten mit einem Abstand kleiner als $\delta$ um weniger als $\varepsilon$ unterscheiden. Für
$\vec p,\vec p_0\in Q'$ mit $\lvert\vec p-\vec p_0\rvert<\delta$ haben die Punkte $(x_1,\vec p)$ und $(x_1,\vec p_0)$
genau den Abstand $\lvert\vec p-\vec p_0\rvert$, also

$$\lvert s_1(\vec p)-s_1(\vec p_0)\rvert \le \int_{a_1}^{b_1}\lvert f(x_1,\vec p)-f(x_1,\vec p_0)\rvert\,dx_1 \le (b_1-a_1)\,\varepsilon.$$

So ist $s_1$ stetig auf dem kompakten Quader $Q'$. Dasselbe Argument, angewandt auf $s_1$, liefert eine stetige Funktion
$s_2$ auf $[a_3,b_3]\times\cdots\times[a_n,b_n]$. Nach $n-1$ Schritten bleibt eine stetige Funktion von $x_n$ auf
$[a_n,b_n]$, und deren Integral existiert.

**Im Bild:** Benachbarte Stäbchen sind fast gleich schwer, benachbarte Scheiben ebenso — nirgends springt das Gewicht.
:::

::::beispiel Ein Laib mit ungleichmäßiger Dichte
Der Klotz

$$Q = [0,1]\times[0,2]\times[0,3]\subseteq\mathbb{R}^3$$

habe die Dichte

$$f(\vec x) = x_1+x_2+x_3.$$

**Stäbchen** in $x_1$-Richtung:

$$s_1(x_2,x_3) = \int_0^1 (x_1+x_2+x_3)\,dx_1 = \frac12+x_2+x_3.$$

**Scheiben** bei festem $x_3$:

$$s_2(x_3) = \int_0^2\Big(\frac12+x_2+x_3\Big)dx_2 = 1+2+2x_3 = 3+2x_3.$$

**Der Stapel:**

$$\int_Q f(\vec x)\,d^3x = \int_0^3 (3+2x_3)\,dx_3 = 9+9 = 18.$$

**Im Bild:** Der Klotz hat das Volumen $\lvert Q\rvert=6$. Zur Probe: Eine linear wachsende Dichte ist im Mittel so groß
wie im Mittelpunkt $(\tfrac12,1,\tfrac32)$, weil sich die Abweichungen nach oben und unten symmetrisch ausgleichen — dort
ist sie $3$. Volumen mal mittlere Dichte ergibt wieder $18$.
::::

**Die Reihenfolge ist auch hier frei.** Die Definition integriert in der Reihenfolge $x_1,x_2,\ldots,x_n$. Jede andere der
$n!$ möglichen Reihenfolgen liefert denselben Wert — das ist der Satz von Fubini in beliebiger Dimension. Erst deshalb
verdient das Mehrfachintegral seinen Namen ohne Angabe einer Reihenfolge.

**Im Bild:** Ob man den Laib zuerst in Stäbchen längs der einen oder der anderen Kante zerlegt und in welcher Richtung man
die Scheiben stapelt — die Masse ist dieselbe.

:::herleitung
Jede Reihenfolge entsteht aus jeder anderen durch wiederholtes Vertauschen **benachbarter** Integrationen, so wie man eine
Liste durch Nachbartausch sortieren kann. Es genügt also zu zeigen, dass ein solcher Tausch nichts ändert.

Angenommen, an den Positionen $j$ und $j+1$ der Reihenfolge stehen die Variablen $x_k$ und $x_l$. Die ersten $j-1$
Integrationen liefern, wie in der Herleitung der Existenz, eine stetige Funktion $s_{j-1}$ der noch nicht integrierten
Variablen. Hält man alle davon außer $x_k$ und $x_l$ fest, ist $s_{j-1}$ eine stetige Funktion von $(x_k,x_l)$ auf dem
Rechteck $[a_k,b_k]\times[a_l,b_l]$. Für sie ist der zweidimensionale Satz von Fubini zuständig:

$$\int_{a_l}^{b_l}\Big(\int_{a_k}^{b_k} s_{j-1}\,dx_k\Big)dx_l = \int_{a_k}^{b_k}\Big(\int_{a_l}^{b_l} s_{j-1}\,dx_l\Big)dx_k.$$

Für jede Wahl der festgehaltenen Variablen kommt also dasselbe heraus, und die restlichen Integrationen verarbeiten
dieselbe Funktion.

**Im Bild:** Zwei aufeinanderfolgende Schnittrichtungen zu tauschen heißt, in jeder Schicht des Laibs ein
zweidimensionales Brot einmal anders herum zu schneiden — und dort gilt der Satz schon.
:::

::::beispiel Derselbe Laib, anders zerlegt
Für den Klotz von eben,

$$Q=[0,1]\times[0,2]\times[0,3], \qquad f(\vec x) = x_1+x_2+x_3,$$

integriert man jetzt zuerst über $x_3$, dann über $x_1$, zuletzt über $x_2$. Stäbchen in $x_3$-Richtung:

$$\int_0^3 (x_1+x_2+x_3)\,dx_3 = 3x_1+3x_2+\frac92.$$

Scheiben bei festem $x_2$:

$$\int_0^1\Big(3x_1+3x_2+\frac92\Big)dx_1 = \frac32+3x_2+\frac92 = 6+3x_2.$$

Der Stapel längs $x_2$:

$$\int_0^2 (6+3x_2)\,dx_2 = 12+6 = 18.$$

**Im Bild:** Diesmal stehen die Stäbchen senkrecht und sind $3$ lang, und die Scheiben liegen quer zur $x_2$-Kante. Die
Masse bleibt $18$.
::::

**Andere Schreibweisen.** Statt $d^n x$ schreibt man auch $dx_1\cdots dx_n$, $d(x_1,\ldots,x_n)$ oder kurz $dx$. In den Natur- und Ingenieurwissenschaften heißt der dreidimensionale Fall __Volumenintegral__:

$$\iiint_Q f(x,y,z)\,dx\,dy\,dz = \iiint_Q f\,dV.$$

Das Volumenelement $dV$ ist das Volumen eines winzigen Klötzchens mit den Kanten $dx$, $dy$ und $dz$. Ein Beispiel aus der
Elektrotechnik: Die Gesamtladung in einem Gebiet ist das Volumenintegral der Ladungsdichte $\rho$.

## Rechenregeln: linear, monoton, abschätzbar

Mit dem Mehrfachintegral rechnet man wie mit dem gewöhnlichen Integral. Für stetige $f,g:Q\to\mathbb{R}$ und
Zahlen $\lambda,\mu\in\mathbb{R}$ gilt:

:::formel Lemma
$$\int_Q\big(\lambda f(\vec x)+\mu g(\vec x)\big)\,d^n x = \lambda\int_Q f(\vec x)\,d^n x+\mu\int_Q g(\vec x)\,d^n x,$$

$$f\le g \ \text{ in } Q \quad\Longrightarrow\quad \int_Q f(\vec x)\,d^n x \le \int_Q g(\vec x)\,d^n x,$$

$$\Big\lvert\int_Q f(\vec x)\,d^n x\Big\rvert \le \lvert Q\rvert\,\sup_{\vec x\in Q}\lvert f(\vec x)\rvert.$$
:::

**So liest man das:** Die erste Zeile ist die __Linearität__ — Summen und konstante Faktoren darf man aus dem Integral
ziehen. Die zweite ist die __Monotonie__ — die größere Funktion hat das größere Integral. Die dritte ist die
__Standardabschätzung__: Der Betrag des Integrals ist höchstens das Volumen des Quaders mal den größten Funktionsbetrag.
Das __Supremum__, die kleinste obere Schranke, ist hier sogar ein Maximum, weil die stetige Funktion $\lvert f\rvert$ auf
dem kompakten Quader ihr Maximum annimmt.

**Im Bild:** Stapelt man zwei Brote aufeinander, addieren sich ihre Höhen und damit die Volumina; ein doppelt so hohes Brot
hat das doppelte Volumen. Ein Brot, das überall niedriger ist als ein zweites, hat weniger Volumen. Und jedes Brot passt in
einen **Brotkasten** mit der Grundfläche des Bretts und der Höhe seines höchsten Punkts.

:::grafik
Szene: hoema3/integralrechnung-rn/03-brotkasten · Vorlage: volumen-scheiben-3d
Ein Brot über dem Rechteck $Q$ mit der Höhe $f$, darüber ein durchsichtiger Kasten mit derselben Grundfläche und der Höhe
$\max_Q\lvert f\rvert$. Ein Regler verformt das Brot; das Brotvolumen und das Kastenvolumen $\lvert Q\rvert\max_Q\lvert
f\rvert$ werden als Balken verglichen — der Brotbalken bleibt immer kürzer. Hat das Brot Mulden unter dem Brett, reicht der
Kasten ebenso weit nach unten. Kernaussage: Das Integral ist höchstens Grundfläche mal größter Betrag. (Rot = Brot, grau
gestrichelt = Brotkasten, orange = Vergleichsbalken.)
:::

:::herleitung
**Linearität.** Jede einzelne Integration ist linear. Schon die innerste liefert

$$\int_{a_1}^{b_1}\big(\lambda f+\mu g\big)\,dx_1 = \lambda\int_{a_1}^{b_1} f\,dx_1+\mu\int_{a_1}^{b_1} g\,dx_1,$$

also dieselbe Kombination der beiden Zwischenergebnisse. Die nächste Integration übernimmt sie wieder, und so fort durch
alle $n$ Schritte.

**Monotonie.** Aus $f\le g$ folgt für die innerste Integration an jeder Stelle $(x_2,\ldots,x_n)$

$$\int_{a_1}^{b_1} f\,dx_1 \le \int_{a_1}^{b_1} g\,dx_1.$$

Die Ungleichung zwischen den Zwischenergebnissen bleibt in jedem weiteren Schritt erhalten.

**Integral einer Konstanten.** Für die konstante Funktion mit dem Wert $\kappa\in\mathbb{R}$ liefert jede Integration den
Faktor einer Kantenlänge:

$$\int_Q \kappa\,d^n x = \kappa\,(b_1-a_1)\cdots(b_n-a_n) = \kappa\,\lvert Q\rvert.$$

**Standardabschätzung.** Sei $m$ das Maximum von $\lvert f\rvert$ auf $Q$. Es gilt

$$-\lvert f\rvert \le f \le \lvert f\rvert \qquad\text{und}\qquad \lvert f\rvert\le m.$$

Mit Monotonie, Linearität und dem Integral der Konstanten $m$ folgt

$$\Big\lvert\int_Q f\,d^n x\Big\rvert \le \int_Q\lvert f\rvert\,d^n x \le \int_Q m\,d^n x = m\,\lvert Q\rvert.$$

**Im Bild:** Der Brotkasten ist die konstante Funktion $m$. Er umschließt das Brot, also enthält er mindestens so viel
Volumen — und das Volumen eines Kastens ist Grundfläche mal Höhe.
:::

::::beispiel Rechenregeln am Brotkeil
**(a) Linearität.** Der Brotkeil auf $Q=[0,2]\times[0,1]$ mit der Höhe $x+y$ ist die Summe zweier einfacher Keile: Der
eine steigt nur in $x$-Richtung, der andere nur in $y$-Richtung.

$$\int_Q x\,d^2x = \int_0^1\Big(\int_0^2 x\,dx\Big)dy = 2, \qquad \int_Q y\,d^2x = \int_0^1\Big(\int_0^2 y\,dx\Big)dy = \int_0^1 2y\,dy = 1.$$

Zusammen ergibt das $3$, wie bei der Rechnung Scheibe für Scheibe.

**(b) Standardabschätzung.** Auf $Q$ liegt die Höhe zwischen $0$ und $3$, das Maximum in der Ecke $(2,1)$. Mit
$\lvert Q\rvert=2$:

$$3 \le 2\cdot3 = 6.$$

Der Keil füllt genau die Hälfte seines Brotkastens.

**(c) Mit Vorzeichen.** Für die Höhe $x-y$ auf demselben $Q$ liegt über dem Bereich $y>x$ eine Mulde. Mit Linearität und
den Werten aus (a):

$$\int_Q (x-y)\,d^2x = 2-1 = 1.$$

Das Volumen von $\lvert x-y\rvert$ zählt die Mulde positiv mit. Für festes $y\in[0,1]$:

$$\int_0^2\lvert x-y\rvert\,dx = \int_0^y(y-x)\,dx+\int_y^2(x-y)\,dx = \frac{y^2}{2}+\frac{(2-y)^2}{2},$$

$$\int_Q\lvert x-y\rvert\,d^2x = \int_0^1\Big(\frac{y^2}{2}+\frac{(2-y)^2}{2}\Big)dy = \frac16+\frac76 = \frac43.$$

Das Maximum von $\lvert x-y\rvert$ ist $2$, in der Ecke $(2,0)$. Die Kette aus der Herleitung lautet also

$$1 \le \frac43 \le 2\cdot2 = 4.$$

**Im Bild:** Bei (c) frisst die Mulde einen Teil des Bergs auf. Das Integral selbst ist deshalb kleiner als das Volumen von
$\lvert x-y\rvert$, das beide positiv zählt.
::::

## Über den ganzen $\mathbb{R}^n$: kompakter Träger

Bisher lag das Brot auf einem Brett. Jetzt soll man über den ganzen $\mathbb{R}^n$ integrieren — im Bild liegt das Brot auf
einem **unendlich großen Tisch**. Das geht ohne neue Theorie, solange die Funktion außerhalb eines beschränkten Bereichs
verschwindet.

**Die Akteure:** eine stetige Funktion $f:\mathbb{R}^n\to\mathbb{R}$. Man sagt, $f$ hat __kompakten Träger__, wenn sie
außerhalb einer Kugel um den Ursprung null ist. Dann integriert man über einen Quader, außerhalb dessen $f$ verschwindet:

:::formel Definition
$$\exists\,R>0: \quad f(\vec x)=0 \ \text{ für alle } \vec x\in\mathbb{R}^n \text{ mit } \lvert\vec x\rvert>R,$$

$$\int_{\mathbb{R}^n} f(\vec x)\,d^n x := \int_Q f(\vec x)\,d^n x \qquad\text{für einen Quader } Q\subseteq\mathbb{R}^n \text{ mit } f=0 \text{ außerhalb von } Q.$$
:::

**So liest man das:** Die erste Zeile ist die Bedingung — außerhalb der Kugel vom Radius $R$ um den Ursprung ist $f$ null.
Der __Träger__ einer Funktion ist der Bereich, auf dem sie „lebt": die Menge der Punkte mit $f(\vec x)\neq0$ samt ihren
Randpunkten. Er liegt hier in der abgeschlossenen Kugel vom Radius $R$, ist also beschränkt und abgeschlossen — das heißt
__kompakt__, daher der Name. Die zweite Zeile führt das Integral über den ganzen Raum auf ein Integral über einen Quader
zurück.

**Im Bild:** Auf dem unendlichen Tisch liegt das Brot nur in einem beschränkten Bereich, sonst ist die Höhe null. Man
stülpt irgendeinen Brotkasten darüber, der das ganze Brot enthält, und misst dessen Inhalt.

:::grafik
Szene: hoema3/integralrechnung-rn/03-kompakter-traeger · Vorlage: buckel-im-quader-2d
Ein runder Laib auf einer unendlichen Tischebene; außerhalb des Kreises vom Radius $R$ ist die Höhe null. Darüber zwei
verschieden große Kästen, die beide den Laib enthalten. Das gemessene Volumen ist bei beiden gleich, weil der größere nur
leeren Tisch dazunimmt. Gestrichelt der Kreis vom Radius $R$ und das Quadrat $[-R,R]^2$ als Standard-Kasten. Kernaussage:
Bei kompaktem Träger ist das Integral über den ganzen Raum das Integral über irgendeinen Kasten, der den Träger enthält.
(Rot = $f$, grau = Tisch und Kästen, gestrichelt = Kreis und Standard-Kasten.)
:::

Damit die Definition sinnvoll ist, muss es einen solchen Quader geben, und das Ergebnis darf nicht davon abhängen, welchen
man nimmt. Beides gilt:

:::herleitung
**Es gibt einen passenden Quader.** Man nimmt den Würfel mit der Kantenlänge $2R$ um den Ursprung:

$$Q_R := [-R,R]\times\cdots\times[-R,R]\subseteq\mathbb{R}^n.$$

Liegt $\vec x$ außerhalb, so ist mindestens eine Koordinate betragsmäßig größer als $R$, etwa die $k$-te. Dann ist auch

$$\lvert\vec x\rvert \ge \lvert x_k\rvert > R,$$

also ist $f(\vec x)$ null.

**Vergrößern ändert nichts.** Seien $Q\subseteq\tilde Q$ zwei Quader mit den Kanten $[a_k,b_k]$ bzw.
$[\tilde a_k,\tilde b_k]$, und $f$ sei außerhalb von $Q$ null. Für die innerste Integration zerlegt man das größere
Intervall in drei Stücke:

$$\int_{\tilde a_1}^{\tilde b_1} f\,dx_1 = \int_{\tilde a_1}^{a_1} f\,dx_1+\int_{a_1}^{b_1} f\,dx_1+\int_{b_1}^{\tilde b_1} f\,dx_1.$$

Auf den äußeren Stücken ist $f$ null: Dort liegt der Punkt außerhalb von $Q$ oder auf dessen Rand, und am Rand ist die
stetige Funktion $f$ ebenfalls null. Es bleibt das Integral über $[a_1,b_1]$. Liegen die übrigen Koordinaten
$(x_2,\ldots,x_n)$ außerhalb von $[a_2,b_2]\times\cdots\times[a_n,b_n]$, liegt sogar die ganze Linie außerhalb von $Q$,
und das Zwischenergebnis ist null. In jedem weiteren Schritt wiederholt sich dasselbe: Die zusätzlichen Stücke tragen
nichts bei. Also

$$\int_{\tilde Q} f(\vec x)\,d^n x = \int_Q f(\vec x)\,d^n x.$$

**Jeder passende Quader gibt dasselbe.** Sind $Q_1$ und $Q_2$ zwei Quader, außerhalb derer $f$ verschwindet, so wählt man
einen großen Quader $\tilde Q$, der beide enthält. Zweimal „Vergrößern ändert nichts" ergibt

$$\int_{Q_1} f\,d^n x = \int_{\tilde Q} f\,d^n x = \int_{Q_2} f\,d^n x.$$

**Im Bild:** Ein größerer Brotkasten enthält nur zusätzliche Luft, und Luft trägt zum Volumen des Brots nichts bei.
:::

::::beispiel Ein runder Laib auf dem Tisch
Auf dem Tisch $\mathbb{R}^2$ liegt ein runder Laib mit der Höhe

$$f(\vec x) = \max\big(0,\;1-\lvert\vec x\rvert^2\big) = \max\big(0,\;1-x^2-y^2\big).$$

$f$ ist stetig und für $\lvert\vec x\rvert>1$ null: ein kompakter Träger mit $R=1$, nämlich die abgeschlossene
Einheitskreisscheibe. Als Brotkasten dient das Quadrat $Q=[-1,1]^2$.

**Eine Scheibe.** Bei festem $y\in[-1,1]$ ist der Integrand nur zwischen $-w$ und $w$ positiv, mit der halben
Scheibenbreite

$$w = \sqrt{1-y^2}.$$

Dort ist er gleich $w^2-x^2$, also

$$\int_{-1}^{1} f(x,y)\,dx = \int_{-w}^{w}(w^2-x^2)\,dx = 2w^3-\frac23\,w^3 = \frac43\,(1-y^2)^{3/2}.$$

**Der Stapel.** Man substituiert

$$y=\sin\theta, \qquad dy=\cos\theta\,d\theta, \qquad 1-y^2=\cos^2\theta \qquad (\theta\in[-\tfrac{\pi}{2},\tfrac{\pi}{2}]).$$

Weil $\cos\theta$ dort nicht negativ ist, wird $(1-y^2)^{3/2}$ zu $\cos^3\theta$, und

$$\int_{\mathbb{R}^2} f(\vec x)\,d^2x = \frac43\int_{-1}^{1}(1-y^2)^{3/2}\,dy = \frac43\int_{-\pi/2}^{\pi/2}\cos^4\theta\,d\theta = \frac43\cdot\frac{3\pi}{8} = \frac{\pi}{2}.$$

:::herleitung
Das Integral von $\cos^4$ zerlegt man mit der Doppelwinkelformel

$$\cos^2\alpha = \frac{1+\cos2\alpha}{2},$$

zweimal angewandt:

$$\cos^4\theta = \Big(\frac{1+\cos2\theta}{2}\Big)^2 = \frac{1+2\cos2\theta+\cos^22\theta}{4} = \frac38+\frac{\cos2\theta}{2}+\frac{\cos4\theta}{8}.$$

Über $[-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ integriert, verschwinden beide Kosinus-Terme, denn ihre Stammfunktionen
$\sin2\theta$ und $\sin4\theta$ sind an beiden Grenzen null. Es bleibt

$$\int_{-\pi/2}^{\pi/2}\cos^4\theta\,d\theta = \frac38\cdot\pi = \frac{3\pi}{8}.$$
:::

**Ein größerer Kasten.** Nimmt man stattdessen $\tilde Q=[-2,2]\times[-3,5]$, ändert sich nichts. Für $\lvert y\rvert\le1$
ist die Scheibe dieselbe wie oben, für $\lvert y\rvert>1$ ist sie leer, und auf den zusätzlichen Stücken des Stapels liegt
kein Brot. Wieder ergibt sich $\frac{\pi}{2}$.

**Im Bild:** Der Laib ist ein Paraboloid der Höhe $1$ über der Einheitskreisscheibe. Sein Volumen $\frac{\pi}{2}$ ist genau
die Hälfte des umschließenden Zylinders, der das Volumen $\pi$ hat. Der Träger ist rund, der Kasten eckig — das stört
nicht, weil der Kasten nur leeren Tisch dazunimmt.
::::

**Wie geht es weiter?** Viele wichtige Funktionen haben keinen kompakten Träger — etwa die Glockenkurve
$e^{-\lvert\vec x\rvert^2}$, die nirgends ganz null wird. Es liegt nahe, sie als Grenzwert von Funktionen mit kompaktem
Träger zu behandeln. Wann das möglich ist, klärt erst die __Lebesgue-Integration__; sie sprengt den Rahmen dieser Seiten.

## Bedeutung und Ausblick

Mit dem iterierten Integral führt man jedes Integral über einen Quader auf $n$ gewöhnliche Integrale zurück —
Scheibe für Scheibe, Stäbchen für Stäbchen. Der Satz von Fubini erlaubt, die Schnittrichtung frei zu wählen, und das ist
in der Praxis oft der entscheidende Rechentrick. Massen, Ladungen, Schwerpunkte und Trägheitsmomente sind solche
Mehrfachintegrale, später in der Stochastik auch Wahrscheinlichkeiten für mehrere Zufallsgrößen.

Bisher lag das Brot auf einem rechteckigen Brett, und auch der runde Laib ging nur auf, weil seine Höhe am Rand stetig auf
null fiel. Reale Gebiete sind Kreisscheiben, Kugeln und Dreiecke — und eine Funktion, die man über eine Kreisscheibe
integrieren will, ist am Rand meist **nicht** null. Setzt man sie außerhalb durch null fort, entsteht ein Sprung, und die
Stetigkeit, auf der hier alles ruhte, ist dahin. Wie man trotzdem über allgemeine Mengen integriert und Volumina
berechnet, zeigt der nächste Artikel. Das Scheiben-Prinzip dieses Artikels wird dort als __Prinzip von Cavalieri__ zum
Werkzeug für Volumina.

:::kern
- Das __iterierte Integral__ integriert nacheinander nach jeder Variablen: innen eine Scheibe messen, außen die Scheiben stapeln.
- Es existiert, weil jedes Zwischenergebnis wieder **stetig** ist — gleichmäßige Stetigkeit auf dem kompakten Quader.
- __Satz von Fubini__: Für stetiges $f$ auf einem Quader ist die Reihenfolge egal — in jeder Schnittrichtung dasselbe Brot.
- Beweis: Ein Eckstück wächst in beiden Messungen um dieselbe Randscheibe, also bleibt die Differenz $h$ null.
- Ohne Stetigkeit kann es scheitern: Berg und Mulde mit unendlichem Volumen in einer Ecke geben je nach Reihenfolge $\pm\frac{\pi}{4}$.
- Die Reihenfolge klug wählen: zuerst die Variable mit der einfachen Stammfunktion.
- Produkte $u(x)\,v(y)$ zerfallen in zwei gewöhnliche Integrale — jede Scheibe ist dieselbe Kurve, nur gestreckt.
- Das __Mehrfachintegral__ $\int_Q f(\vec x)\,d^n x$ ist **linear** und **monoton**; das Volumenelement ist kein Vektor und trägt keinen Pfeil.
- __Standardabschätzung__: $\lvert\int_Q f\,d^n x\rvert\le\lvert Q\rvert\,\sup_Q\lvert f\rvert$ — das Brot passt in seinen Brotkasten.
- Bei __kompaktem Träger__ ist das Integral über $\mathbb{R}^n$ das Integral über irgendeinen Quader, der den Träger enthält.
- Für Funktionen ohne kompakten Träger braucht man Grenzwerte und letztlich das Lebesgue-Integral.
:::

:::quiz
F: Was misst das innere, was das äußere Integral im iterierten Integral $\int_c^d\big(\int_a^b f(x,y)\,dx\big)dy$?
A: Das innere Integral misst bei festem $y$ die Fläche $s(y)$ einer Scheibe — die Schnittfläche unter der Kurve $x\mapsto f(x,y)$, ein Parameterintegral mit dem Messer als Regler. Das äußere stapelt die Scheiben längs der $y$-Achse: Scheibenfläche mal Dicke, aufsummiert. Zusammen ergibt das das Volumen des Brots über dem Rechteck.
F: Warum existiert das iterierte Integral für stetiges $f$?
A: Die Scheibenfläche $s(y)$ ist stetig: Auf dem kompakten Rechteck ist $f$ gleichmäßig stetig, also ändert sich die Schnittkurve bei kleinem Weiterrücken des Messers überall nur wenig, und $\lvert s(y)-s(y_0)\rvert\le(b-a)\varepsilon$. Eine stetige Funktion auf $[c,d]$ ist integrierbar. In $n$ Dimensionen wiederholt sich das Argument in jedem Schritt.
F: Was besagt der Satz von Fubini, und unter welcher Voraussetzung gilt er hier?
A: Für eine **stetige** Funktion auf einem Quader liefern alle Integrationsreihenfolgen denselben Wert, in zwei Dimensionen $\int_c^d\int_a^b f\,dx\,dy=\int_a^b\int_c^d f\,dy\,dx$. Im Bild: In jeder Schnittrichtung ist es dasselbe Brot. Beim Brotkeil $x+y$ auf $[0,2]\times[0,1]$ ergeben beide Richtungen das Volumen $3$.
F: Wie funktioniert der Beweis mit der Hilfsfunktion $h(\xi,\eta)$?
A: $h$ ist die Differenz der beiden Messungen des Eckstücks über $[a,\xi]\times[c,\eta]$. Rückt $\xi$ vor, wächst die erste Messung nach dem Hauptsatz um die Randscheibe $\int_c^\eta f(\xi,y)\,dy$; in der zweiten wird jede Scheibe um $f(\xi,y)$ länger, und Ableiten unter dem Integral gibt dieselbe Randscheibe. Also ist $\partial h/\partial\xi=0$, $h$ ist in $\xi$ konstant, und am Rand $\xi=a$ ist $h=0$.
F: Warum liefern die beiden Reihenfolgen für $\frac{x^2-y^2}{(x^2+y^2)^2}$ auf $[0,1]^2$ verschiedene Werte, obwohl beide existieren?
A: Zuerst über $y$ ergibt sich $\frac{\pi}{4}$, zuerst über $x$ dagegen $-\frac{\pi}{4}$. Die Funktion ist in der Ecke $(0,0)$ unbeschränkt, also nicht stetig auf dem abgeschlossenen Quadrat — der Satz greift nicht. Dort stecken ein Berg und eine Mulde mit je unendlichem Volumen (die Scheibenfläche des Bergs ist $\frac{1}{2x}$), und jede Schnittrichtung verrechnet sie anders. Sicher vertauschen darf man erst bei absoluter Integrierbarkeit.
F: Wie berechnet man $\int_0^{2\pi}\!\int_0^{2\pi}x\cos(xy)\,dx\,dy$ am geschicktesten, und warum?
A: Zuerst über $y$: Der Faktor $x$ ist genau die innere Ableitung von $\sin(xy)$ nach $y$, also gibt das innere Integral sofort $\sin(2\pi x)$ und das äußere $\frac{1-\cos(4\pi^2)}{2\pi}=\frac{\sin^2(2\pi^2)}{\pi}$. Zuerst über $x$ braucht man partielle Integration und muss danach die Quotientenregel rückwärts erkennen — dasselbe Ergebnis, viel mehr Arbeit.
F: Warum zerfällt das Integral eines Produkts $u(x)\,v(y)$ über ein Rechteck in zwei gewöhnliche Integrale?
A: Bei der Integration über $x$ ist $v(y)$ eine Konstante und darf vor das Integral; übrig bleibt das feste Integral über $u$, das im äußeren Integral ebenfalls vor das Integral darf. Im Bild zeigt jede Scheibe dieselbe Kurve $u$, nur mit $v(y)$ gestreckt. Beim Sinusbogen-Brot $(1+y)\sin x$ auf $[0,\pi]\times[0,2]$ gibt das $2\cdot4=8$.
F: Warum ist auch in $n$ Dimensionen jede der $n!$ Reihenfolgen erlaubt?
A: Jede Reihenfolge entsteht aus jeder anderen durch Vertauschen benachbarter Integrationen. Bei einem solchen Tausch integriert man eine stetige Funktion zweier Variablen über ein Rechteck — dort gilt der zweidimensionale Satz —, und alle übrigen Integrationen bleiben unverändert. Beim Klotz mit der Dichte $x_1+x_2+x_3$ ergeben zwei verschiedene Reihenfolgen beide die Masse $18$.
F: Woher kommt die Standardabschätzung $\lvert\int_Q f\,d^n x\rvert\le\lvert Q\rvert\sup_Q\lvert f\rvert$, und was bedeutet sie im Bild?
A: Aus $-\lvert f\rvert\le f\le\lvert f\rvert$ und $\lvert f\rvert\le m$ (das Maximum von $\lvert f\rvert$) folgt mit Monotonie und Linearität $\lvert\int f\rvert\le\int\lvert f\rvert\le m\lvert Q\rvert$, denn eine Konstante $\kappa$ integriert sich zu $\kappa\lvert Q\rvert$. Im Bild: Das Brot passt in einen Brotkasten mit der Grundfläche des Bretts und der Höhe des höchsten Punkts.
F: Was heißt „kompakter Träger", und warum hängt $\int_{\mathbb{R}^n}f\,d^n x$ nicht vom gewählten Quader ab?
A: $f$ ist außerhalb einer Kugel vom Radius $R$ null; der Träger liegt dann in einer beschränkten, abgeschlossenen Menge. Vergrößert man einen Quader, außerhalb dessen $f$ verschwindet, kommen nur Stücke mit $f=0$ hinzu; zwei passende Quader vergleicht man über einen großen, der beide enthält. Beim runden Laib $\max(0,1-\lvert\vec x\rvert^2)$ geben $[-1,1]^2$ und jeder größere Kasten das Volumen $\frac{\pi}{2}$.
:::
