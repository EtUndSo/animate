---
title: Integration über Mengen und das Cavalieri-Prinzip
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020400
summary: Von Grund auf – wie man über eine beliebig geformte, abgeschlossene und beschränkte Menge integriert. Leitbild ist ein Brot aus der Backform. Man stellt die Form in einen Kasten und setzt die Funktion daneben durch null fort; am Rand entsteht dabei eine senkrechte Wand. Der Artikel klärt, wann diese Wand stört und wann nicht (Nullmenge, fette Cantor-Menge, Lebesgue). Dazu das Volumen als Integral der Eins und das Prinzip von Cavalieri, $\mathrm{vol}(K)=\int_0^H s(z)\,dz$ – mit Kegel, Kugel, Napf und Rotationskörpern auf einer Beispiel-Seite.
tags: Integration über Mengen, Fortsetzung durch null, Volumen, Cavalieri-Prinzip, Querschnittsfläche, Rotationskörper, Nullmenge
---

## Anschaulich

Bisher lag das Brot auf einem rechteckigen Brett: Integriert wurde über Quader. Echte Formen sind aber rund, dreieckig
oder kugelförmig.

**Das Leitbild dieses Artikels:** Ein Brot wurde in einer **Backform** gebacken. Die Grundfläche der Form ist eine Menge
$M$ — eine Kreisscheibe, ein Dreieck, irgendetwas. Über jedem Punkt der Form hat das Brot die Höhe $f$, neben der Form ist
nichts.

Der Trick: Man stellt die Form in einen rechteckigen **Brotkasten** $Q$. Im Kasten ist das Brot dann eine Funktion auf
dem ganzen Quader — in der Form die Höhe $f$, daneben die Höhe null. Über Quader können wir integrieren, und das Integral
über die Form ist das Integral über den Kasten.

Der Haken: Ein gebackenes Brot hat **senkrechte Wände**. Am Rand der Form springt die Höhe von $f$ auf null, die neue
Funktion ist dort nicht stetig — und die Stetigkeit war bisher die Grundlage von allem. Bei vernünftigen Formen geht es
trotzdem gut. Bei wild zerfransten Rändern versagt das bisherige Integral, und erst die Lebesgue-Theorie hilft.

Aus derselben Idee entstehen **Volumina**: Ein Körper ist ein Teig der Dichte eins, seine Masse ist sein Volumen. Messen
kann man es so, wie ein Konditor eine Torte in **waagerechte Böden** schneidet: Das Volumen ist das Integral der
Querschnittsflächen. Das ist das __Prinzip von Cavalieri__ — mit ihm fallen Kegel und Kugel in wenigen Zeilen.

:::grafik
Szene: hoema3/integralrechnung-rn/04-backform-im-kasten · Vorlage: gebiet-null-und-cavalieri-3d
Links: ein rundes Brot mit senkrechter Wand in seiner Form $M$, die in einem rechteckigen Kasten $Q$ steht; außerhalb der
Form liegt die Höhe flach auf null, die Stufe am Formrand ist hervorgehoben. Rechts: ein Körper $K$, in dünne waagerechte
Böden der Dicke $h$ zerlegt; jeder Boden in der Höhe $z$ hat die Fläche $s(z)$ und etwa das Volumen $s(z)\,h$, im
Grenzfall dünner Böden wird daraus $\int s(z)\,dz$. Kernaussage: Integrale über Formen sind Integrale über Kästen mit
Wand; Volumina sind Stapel von Querschnitten. (Rot = Brot bzw. Körper, orange = Wand bzw. aktueller Boden, grau = Kasten
und Achsen.)
:::

## Abgeschlossen und beschränkt: welche Formen erlaubt sind

Integriert wird hier über Mengen $M\subseteq\mathbb{R}^n$, die __beschränkt__ und __abgeschlossen__ sind. Beide
Bedingungen haben im Bild einen klaren Sinn.

**Beschränkt** heißt, dass $M$ in eine Kugel um den Ursprung passt: Es gibt eine Zahl $R_M>0$ mit

$$\lvert\vec x\rvert\le R_M \qquad\text{für alle } \vec x\in M.$$

Im Bild: Die Form ist nicht unendlich groß, sie passt in einen Kasten.

**Abgeschlossen** heißt, dass das Komplement $\mathbb{R}^n\setminus M$ offen ist, im Sinne des Artikels
[Skalarfelder, Vektorfelder und die Jacobi-Matrix](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/skalar-und-vektorfelder-differenzierbarkeit.html): Um jeden
Punkt außerhalb von $M$ liegt noch eine kleine Kugel ganz außerhalb von $M$.

Was das bedeutet, zeigt der Rand. Ein Punkt $\vec x\in\mathbb{R}^n$ heißt __Randpunkt__ von $M$, wenn jede Kugel
$B_\varepsilon(\vec x)$ sowohl Punkte von $M$ als auch Punkte außerhalb von $M$ enthält. Die Menge aller Randpunkte ist
der __Rand__ $\partial M$. Eine Menge ist genau dann abgeschlossen, wenn sie ihren ganzen Rand enthält:

$$M \text{ abgeschlossen} \quad\Longleftrightarrow\quad \partial M\subseteq M.$$

:::herleitung
**Von links nach rechts.** Sei $M$ abgeschlossen und $\vec x$ ein Randpunkt. Läge $\vec x$ außerhalb von $M$, gäbe es —
weil das Komplement offen ist — eine Kugel um $\vec x$ ganz außerhalb von $M$. Sie enthielte keinen Punkt von $M$, im
Widerspruch dazu, dass $\vec x$ ein Randpunkt ist. Also liegt $\vec x$ in $M$.

**Von rechts nach links.** Der Rand liege in $M$, und $\vec x$ liege außerhalb von $M$. Dann ist $\vec x$ kein Randpunkt:
Eine Kugel um $\vec x$ enthält nicht beide Sorten von Punkten. Punkte außerhalb von $M$ enthält sie sicher, nämlich
$\vec x$ selbst. Also enthält sie keinen Punkt von $M$ und liegt ganz im Komplement — das Komplement ist offen.
:::

**Im Bild:** Bei einer abgeschlossenen Form gehört der Rand dazu — die Wand des Brots steht auf der Form, nicht daneben.
Beschränkt und abgeschlossen zusammen heißt __kompakt__. Eine stetige Funktion auf einer kompakten Menge ist beschränkt und
nimmt ihr Maximum an: Das Brot ist nirgends unendlich hoch.

:::grafik
Szene: hoema3/integralrechnung-rn/04-rand-und-abschluss · Vorlage: menge-rand-2d
Eine Form $M$ in der Ebene mit hervorgehobenem Rand $\partial M$. Ein Punkt wird mit der Maus bewegt, um ihn liegt eine
kleine Kugel $B_\varepsilon(\vec x)$: Im Inneren liegt sie ganz in $M$, außen ganz daneben, auf dem Rand enthält sie
Punkte beider Sorten. Ein Umschalter wechselt zwischen abgeschlossener Form (Rand durchgezogen, gehört dazu) und offener
Form (Rand gestrichelt, fehlt). Kernaussage: Eine abgeschlossene Form enthält ihren Rand. (Rot = Form, orange = Kugel um
den Punkt, blau = Rand, gestrichelt = fehlender Rand.)
:::

**Wie man Abgeschlossenheit erkennt.** Fast alle Formen der Praxis sind durch Ungleichungen mit „$\le$" beschrieben, etwa
die abgeschlossene Kreisscheibe vom Radius $r>0$ um den Ursprung:

$$S_r := \big\{\vec x\in\mathbb{R}^2 \;:\; \lvert\vec x\rvert\le r\big\}.$$

Solche Mengen sind immer abgeschlossen. Sind $g_1,\ldots,g_p:\mathbb{R}^n\to\mathbb{R}$ stetig, so ist

$$M = \big\{\vec x\in\mathbb{R}^n \;:\; g_i(\vec x)\le0 \ \text{ für } i=1,\ldots,p\big\}$$

abgeschlossen.

:::herleitung
Liegt $\vec x$ außerhalb von $M$, so ist mindestens eine der Ungleichungen verletzt, etwa die $i$-te:

$$g_i(\vec x) > 0.$$

Weil $g_i$ stetig ist, gibt es zu $\varepsilon=g_i(\vec x)$ ein $\delta>0$, sodass $g_i$ auf der Kugel $B_\delta(\vec x)$
um weniger als $\varepsilon$ von $g_i(\vec x)$ abweicht — dort bleibt $g_i$ also positiv. Diese Kugel liegt ganz außerhalb
von $M$, das Komplement ist offen.
:::

::::beispiel Welche Formen sind erlaubt?
**(a) Die Kreisscheibe** $S_r$ ist durch eine Ungleichung mit der stetigen Funktion

$$g_1(\vec x) = \lvert\vec x\rvert^2-r^2$$

beschrieben, also abgeschlossen; beschränkt ist sie mit $R_M=r$. Ihr Rand ist die Kreislinie. Erlaubt.

**(b) Das Dreieck**

$$T := \big\{(x,y)\in\mathbb{R}^2 \;:\; 0\le y\le x\le1\big\}$$

besteht aus drei Ungleichungen:

$$-y\le0, \qquad y-x\le0, \qquad x-1\le0.$$

Es ist also abgeschlossen. Für seine Punkte gilt

$$x^2+y^2\le2,$$

also ist es mit $R_M=\sqrt2$ beschränkt. Erlaubt.

**(c) Die offene Kreisscheibe** $B_1(\vec 0)\subseteq\mathbb{R}^2$ aus dem Artikel über
[Skalar- und Vektorfelder](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/skalar-und-vektorfelder-differenzierbarkeit.html) enthält ihren Randpunkt $(1,0)$
nicht: Jede Kugel um ihn enthält für hinreichend kleine $t>0$ den Punkt $(1-t,0)$ der Scheibe und den Punkt $(1+t,0)$
außerhalb. Nicht abgeschlossen.

**(d) Der Streifen** $[0,1]\times\mathbb{R}$ ist durch zwei Ungleichungen beschrieben,

$$-x\le0, \qquad x-1\le0,$$

also abgeschlossen. Beschränkt ist er nicht — er enthält die Punkte $(0,y)$ mit beliebig großem $y$. Kein Kasten fasst
ihn.

**Im Bild:** (a) und (b) sind echte Backformen. Bei (c) fehlt die Linie, auf der die Wand stehen müsste, und (d) ist eine
unendlich lange Rinne.
::::

## Integration über eine Menge: Fortsetzung durch null

**Die Akteure:** eine abgeschlossene, beschränkte Menge $M\subseteq\mathbb{R}^n$ (die Form), eine stetige Funktion
$f:M\to\mathbb{R}$ (die Höhe des Brots) und ein Quader $Q\subseteq\mathbb{R}^n$, der $M$ enthält (der Kasten). Einen
solchen Kasten gibt es immer, etwa den Würfel

$$Q = [-R_M,R_M]\times\cdots\times[-R_M,R_M],$$

denn jede Koordinate eines Punkts ist betragsmäßig höchstens so groß wie sein Betrag, und der ist für Punkte von $M$
höchstens $R_M$.

**Das Zusammenspiel:** *Wie misst man ein Brot in seiner Form?* Man setzt $f$ durch null auf den ganzen Kasten fort und
integriert dort:

:::formel Definition
$$\bar f(\vec x) := \begin{cases} f(\vec x), & \vec x\in M,\\ 0, & \vec x\in Q\setminus M,\end{cases} \qquad\qquad \int_M f(\vec x)\,d^n x := \int_Q \bar f(\vec x)\,d^n x.$$
:::

**So liest man das:** $\bar f$ — gesprochen „$f$ quer" — ist die __Fortsetzung durch null__: auf dem ganzen Kasten
erklärt, auf der Form gleich $f$, daneben null. Das Integral über $M$ ist das Mehrfachintegral dieser Fortsetzung über
den Kasten, sofern es existiert. Eingabe ist die Funktion $f$ auf der Form, Ausgabe eine Zahl. Für die Konstante $1$
heißt die Fortsetzung __Indikatorfunktion__ $\bar 1_M$: Sie ist $1$ auf $M$ und $0$ daneben, zeigt also an, ob ein Punkt
in $M$ liegt.

**Im Bild:** Die Form steht im Kasten, der Platz daneben ist leer. Leerer Platz trägt nichts bei; deshalb ist es gleich,
wie groß der Kasten ist.

:::herleitung
Sind $Q\subseteq\tilde Q$ zwei Kästen um $M$, so ist die Fortsetzung auf $\tilde Q$ außerhalb von $Q$ null. Man rechnet
wie beim kompakten Träger im vorigen Artikel: Jedes Kantenintervall von $\tilde Q$ zerfällt in die Kante von $Q$ und zwei
Zusatzstücke. Auf den Zusatzstücken ist die Fortsetzung null — höchstens bis auf einen Endpunkt, und ein einzelner Punkt
ändert ein Integral nicht. Stetigkeit braucht diese Rechnung nicht. Die Integrale über $Q$ und $\tilde Q$ stimmen
also überein, sobald sie existieren. Zwei beliebige Kästen vergleicht man über einen großen, der beide enthält.
:::

**Die Rechenregeln bleiben.** Linearität und Monotonie aus dem vorigen Artikel gelten auch für Integrale über $M$, sobald
die beteiligten Integrale existieren.

:::herleitung
Die Fortsetzung einer Linearkombination ist die Linearkombination der Fortsetzungen. Ist $f$ auf $M$ überall höchstens so
groß wie $g$, so gilt dasselbe für die Fortsetzungen, denn daneben sind beide null. Die Herleitungen im vorigen Artikel
benutzten nur die Rechenregeln für gewöhnliche Integrale, Schritt für Schritt — nie die Stetigkeit.
:::

**Der Haken: Die Fortsetzung springt.** An einem Randpunkt $\vec x_0$ von $M$, an dem $f$ nicht null ist, ist $\bar f$
unstetig.

:::herleitung
Der Randpunkt gehört zu $M$, weil $M$ abgeschlossen ist; dort stimmt $\bar f$ mit $f$ überein und ist nicht null. Jede
noch so kleine Kugel um $\vec x_0$ enthält aber Punkte außerhalb von $M$, an denen $\bar f$ null ist. Beliebig nah an
$\vec x_0$ gibt es also Werte, die um $\lvert f(\vec x_0)\rvert$ vom Wert in $\vec x_0$ abweichen — $\bar f$ ist dort
nicht stetig.
:::

**Im Bild:** Das ist die senkrechte Wand des gebackenen Brots. Nur wo das Brot am Rand von selbst auf null ausläuft, wie
der runde Laib des vorigen Artikels, entsteht keine Wand.

:::grafik
Szene: hoema3/integralrechnung-rn/04-wand · Vorlage: volumen-scheiben-3d
Ein Kuchen der Höhe $1$ in der runden Form $S_1$, die im Kasten $[-1,1]^2$ steht; außerhalb der Form ist die Höhe null, am
Formrand steht eine senkrechte Wand. Ein Messer fährt entlang der $y$-Achse; die Scheibe ist ein Rechteck über dem
Intervall $\lvert x\rvert\le\sqrt{1-y^2}$, dessen Enden mit dem Messer wandern. Daneben die Scheibenfläche
$s(y)=2\sqrt{1-y^2}$ als stetige Kurve. Zum Vergleich der runde Laib ohne Wand. Kernaussage: Die Fortsetzung springt an
der Wand, die Scheibenflächen aber nicht. (Rot = Kuchen, orange = Wand bzw. aktuelle Scheibe, blau = Scheibenfläche, grau
= Kasten.)
:::

**Warum das stört.** Im vorigen Artikel sicherte die Stetigkeit, dass jede Scheibenfläche existiert und sich ohne Sprünge
ändert. Mit einer Wand ist beides nicht mehr selbstverständlich. Ob die iterierten Integrale existieren, hängt jetzt von der
Form ab.

::::beispiel Laib und Springform
**(a) Ohne Wand.** Der runde Laib aus dem vorigen Artikel hat auf der Kreisscheibe $S_1$ die Höhe

$$f(\vec x) = 1-\lvert\vec x\rvert^2.$$

Am Rand ist sie null, er hat also keine Wand. Seine Fortsetzung auf den Kasten $[-1,1]^2$ ist die stetige Funktion

$$\bar f(\vec x) = \max\big(0,\;1-\lvert\vec x\rvert^2\big),$$

und ihr Integral kennen wir schon:

$$\int_{S_1} f(\vec x)\,d^2x = \frac{\pi}{2}.$$

**(b) Mit Wand.** Ein Kuchen aus der Springform hat auf ganz $S_1$ die Höhe $1$. Seine Fortsetzung $\bar 1_{S_1}$ springt
auf der ganzen Kreislinie von $1$ auf $0$. Trotzdem lässt sich das iterierte Integral ausrechnen. Bei festem $y\in[-1,1]$
ist die Höhe $1$ genau auf dem Intervall der $x$ mit

$$\lvert x\rvert\le\sqrt{1-y^2},$$

daneben $0$ — eine Treppe mit zwei Stufen, also integrierbar. Die Scheibenfläche ist die Länge dieses Intervalls:

$$s(y) = \int_{-1}^{1}\bar 1_{S_1}(x,y)\,dx = 2\sqrt{1-y^2}.$$

Sie hängt **stetig** von $y$ ab, obwohl die Fortsetzung springt. Mit der Substitution

$$y=\sin\theta, \qquad dy=\cos\theta\,d\theta, \qquad \sqrt{1-y^2}=\cos\theta \qquad (\theta\in[-\tfrac{\pi}{2},\tfrac{\pi}{2}])$$

folgt

$$\int_{S_1} 1\,d^2x = \int_{-1}^{1}2\sqrt{1-y^2}\,dy = 2\int_{-\pi/2}^{\pi/2}\cos^2\theta\,d\theta = 2\cdot\frac{\pi}{2} = \pi.$$

:::herleitung
Mit der Doppelwinkelformel ist

$$\cos^2\theta = \frac{1+\cos2\theta}{2}, \qquad \int_{-\pi/2}^{\pi/2}\cos^2\theta\,d\theta = \frac{\pi}{2}+\Big[\frac{\sin2\theta}{4}\Big]_{-\pi/2}^{\pi/2} = \frac{\pi}{2}.$$
:::

**Im Bild:** Die Wand steht an den beiden Enden jeder Scheibe. Weil diese Enden beim Weiterrücken des Messers stetig
wandern, ändert sich die Scheibenfläche trotzdem ohne Sprünge.
::::

## Das Volumen einer Menge

Setzt man für $f$ die Konstante $1$ ein, misst das Integral, wie viel Platz die Form einnimmt. Das ist die Definition des
__Volumens__:

:::formel Definition
$$\mathrm{vol}(M) := \int_M 1\,d^n x = \int_Q \bar 1_M(\vec x)\,d^n x.$$
:::

**So liest man das:** Eingabe ist eine abgeschlossene, beschränkte Menge $M\subseteq\mathbb{R}^n$, Ausgabe eine Zahl. In
zwei Dimensionen heißt sie __Flächeninhalt__, in einer __Länge__; man schreibt auch $\lvert M\rvert$.

**Im Bild:** Ein Brot der Höhe $1$ in der Form $M$ hat das Volumen „Grundfläche mal $1$" — das Integral der Eins misst die
Grundfläche. In drei Dimensionen ist es ein Teig der Dichte $1$, dessen Masse sein Volumen ist.

Für Quader passt das zum vorigen Artikel: Das Volumen ist das Produkt der Kantenlängen, $\mathrm{vol}(Q)=\lvert Q\rvert$.

:::herleitung
Für einen Quader kann man ihn selbst als Kasten nehmen. Seine Indikatorfunktion ist dort die Konstante $1$, und deren
Integral ist nach dem vorigen Artikel das Produkt der Kantenlängen.
:::

**Die Kreisscheibe.** Die Kreisscheibe vom Radius $r>0$ hat den Flächeninhalt

$$\mathrm{vol}(S_r) = \pi r^2.$$

:::herleitung
Wie bei der Springform: Im Kasten $[-r,r]^2$ ist die Scheibe bei festem $y\in[-r,r]$ das Intervall der $x$ mit

$$\lvert x\rvert\le\sqrt{r^2-y^2},$$

seine Länge ist $2\sqrt{r^2-y^2}$. Mit der Substitution

$$y = r\sin\theta, \qquad dy = r\cos\theta\,d\theta, \qquad \sqrt{r^2-y^2} = r\cos\theta$$

und dem Integral von $\cos^2$ von dort folgt

$$\mathrm{vol}(S_r) = \int_{-r}^{r}2\sqrt{r^2-y^2}\,dy = 2r^2\int_{-\pi/2}^{\pi/2}\cos^2\theta\,d\theta = 2r^2\cdot\frac{\pi}{2} = \pi r^2.$$
:::

::::beispiel Ein Dreieck, zwei Schnittrichtungen
Das Dreieck

$$T = \big\{(x,y)\in\mathbb{R}^2 \;:\; 0\le y\le x\le1\big\}$$

steht im Kasten $[0,1]^2$.

**Scheiben bei festem $x$:** Zu $T$ gehören die $y$ mit $0\le y\le x$, die Scheibe hat also die Länge $x$:

$$\int_0^1\bar 1_T(x,y)\,dy = x, \qquad \mathrm{vol}(T) = \int_0^1 x\,dx = \frac12.$$

**Scheiben bei festem $y$:** Zu $T$ gehören die $x$ mit $y\le x\le1$, die Länge ist $1-y$:

$$\int_0^1\bar 1_T(x,y)\,dx = 1-y, \qquad \int_0^1(1-y)\,dy = \frac12.$$

**Im Bild:** Ein Brot der Höhe $1$ in einer dreieckigen Form ist ein Prisma: Grundfläche $\tfrac12$ mal Höhe $1$. Beide
Schnittrichtungen geben dasselbe, obwohl die Fortsetzung an den Dreiecksseiten springt — jede Scheibe ist ein Intervall,
dessen Enden stetig wandern.
::::

## Wann die Wand stört — und wann nicht

**Wo die Sprünge sitzen.** Ein Punkt von $M$ heißt __innerer Punkt__, wenn eine ganze Kugel um ihn in $M$ liegt. An
inneren Punkten stimmt $\bar f$ mit der stetigen Funktion $f$ überein, außerhalb von $M$ ist es null — springen kann es
nur auf dem Rand. Ob die Sprünge stören, hängt deshalb davon ab, wie viel Platz der Rand einnimmt.

:::herleitung
Um einen inneren Punkt liegt eine Kugel ganz in $M$; auf ihr ist $\bar f$ gleich $f$, also stetig. Ein Punkt außerhalb
von $M$ hat, weil das Komplement offen ist, eine Kugel ganz außerhalb; auf ihr ist $\bar f$ null. Ein Punkt von $M$, der
kein innerer Punkt ist, hat in jeder Kugel um sich Punkte außerhalb von $M$ — und sich selbst in $M$: Er ist ein
Randpunkt.
:::

**Ein Rand ohne Fläche.** Eine Menge $N\subseteq\mathbb{R}^n$ heißt __Nullmenge__, wenn man sie für jedes $\varepsilon>0$
mit endlich vielen Quadern überdecken kann, deren Volumina zusammen kleiner als $\varepsilon$ sind. Sie nimmt also keinen
Platz ein. Die Kreislinie ist eine Nullmenge, ebenso jede Strecke — und damit der Rand jedes Vielecks.

**Im Bild:** Die Wand eines gebackenen Brots ist hoch, aber im Grundriss nur ein Strich ohne Breite. Die Sprünge der
Fortsetzung sitzen auf diesem Strich und kosten nichts. Genau gesagt: Ist der Rand eine Nullmenge, so stört die Wand nicht
(Integrierbarkeitskriterium von Lebesgue). Für die Formen, mit denen man in der Praxis rechnet — die Normalbereiche —,
zeigt der nächste Artikel direkt, dass die iterierten Integrale existieren.

:::herleitung
**Die Kreislinie.** Man teilt sie in $N$ gleiche Bögen der Länge $2\pi/N$. Jeder Bogen bleibt innerhalb des Abstands
$2\pi/N$ von seinem Anfangspunkt, denn die gerade Sehne ist nie länger als der Bogen. Er liegt also in einem Quadrat der
Seitenlänge $4\pi/N$ um den Anfangspunkt. Die $N$ Quadrate haben zusammen die Fläche

$$N\cdot\Big(\frac{4\pi}{N}\Big)^2 = \frac{16\pi^2}{N},$$

und das wird für großes $N$ kleiner als jedes $\varepsilon$. Eine Strecke der Länge $L$ überdeckt man ebenso mit $N$
Quadraten der Seitenlänge $2L/N$, zusammen mit der Fläche $4L^2/N$. Endlich viele Nullmengen ergeben wieder eine
Nullmenge: Man überdeckt jede mit einem entsprechend kleineren Anteil von $\varepsilon$.

**Warum ein Rand ohne Fläche nicht stört — Beweisidee.** Man überdeckt den Rand mit kleinen Kästchen vom Gesamtvolumen
unter $\varepsilon$. Außerhalb dieser Kästchen ist $\bar f$ stetig und verhält sich wie im vorigen Artikel. In den
Kästchen schwankt $\bar f$ höchstens um $2\max\lvert f\rvert$; zusammen verfälschen sie jede Näherungssumme für das
Volumen höchstens um $2\max\lvert f\rvert\cdot\varepsilon$. Weil $\varepsilon$ beliebig klein ist, legen die Näherungen
das Integral trotzdem eindeutig fest. Die saubere Fassung dieses Arguments gehört in die Integrationstheorie.
:::

**Wenn der Rand Fläche hat.** Es gibt abgeschlossene, beschränkte Formen, deren Rand selbst Platz einnimmt. Dann versagt
das bisherige Integral — schon in einer Dimension.

::::beispiel Eine Form, die nur aus Wand besteht
In einer Dimension ist eine „Form" eine Teilmenge der Achse, der Kasten ist das Intervall $[0,1]$, und die Höhe sei
überall $1$.

**Die Konstruktion.** Man beginnt mit $[0,1]$. Im Schritt $j=1,2,3,\ldots$ entfernt man aus der Mitte jedes der $2^{j-1}$
übrig gebliebenen Intervalle ein offenes Intervall der Länge $4^{-j}$. Was nach allen Schritten übrig bleibt, ist die
__fette Cantor-Menge__ $C\subseteq[0,1]$. Insgesamt wird die Länge

$$\sum_{j=1}^{\infty}2^{j-1}\cdot4^{-j} = \frac12\sum_{j=1}^{\infty}2^{-j} = \frac12$$

entfernt. $C$ ist beschränkt und abgeschlossen: Ihr Komplement in $\mathbb{R}$ besteht nur aus offenen Intervallen, ist
also offen.

**Keine Teilstrecke.** $C$ enthält kein Intervall positiver Länge. Nach dem Schritt $j$ liegt $C$ nämlich in $2^j$
Intervallen, die alle kürzer als $2^{-j}$ sind; ein Intervall in $C$ läge ganz in einem davon. Darum ist jeder Punkt von
$C$ ein Randpunkt.

:::herleitung
Nach $j$ Schritten wurde die Länge $\frac12(1-2^{-j})$ entfernt. Der Rest verteilt sich auf $2^j$ gleich lange
Intervalle, jedes hat also die Länge

$$\frac{1-\frac12(1-2^{-j})}{2^j} = 2^{-j-1}+2^{-2j-1} < 2^{-j}.$$

Das im nächsten Schritt entfernte Stück ist mit $4^{-j-1}$ kürzer als jedes dieser Intervalle und passt hinein. Ein
Intervall, das ganz in $C$ liegt, liegt in einem einzigen Restintervall, ist also für jedes $j$ kürzer als $2^{-j}$ — es
hat die Länge null.
:::

**Die Untersumme ist null.** Bei jeder Zerlegung von $[0,1]$ enthält jedes Teilintervall einen Punkt außerhalb von $C$,
und dort ist die Fortsetzung null. Jede Untersumme ist $0$.

**Die Obersumme ist mindestens $\tfrac12$.** Ein Teilintervall ohne Punkt von $C$ liegt ganz in einem einzigen entfernten
Intervall. Solche Teilintervalle haben zusammen höchstens die entfernte Länge $\tfrac12$. Die übrigen treffen $C$, dort
ist das Supremum $1$, und sie haben zusammen mindestens die Länge $\tfrac12$. Jede Obersumme ist also mindestens
$\tfrac12$.

Ober- und Untersummen kommen sich nie näher als $\tfrac12$ — die Fortsetzung ist nicht Riemann-integrierbar. Die
Lebesgue-Theorie misst der Menge dagegen die Länge zu, die übrig blieb:

$$\int_C 1\,dx = 1-\frac12 = \frac12.$$

**Im Bild:** Eine Backform mit unendlich vielen, immer feineren Rillen. Die Form besteht nur aus Wand, und diese Wand hat
zusammen die Länge $\tfrac12$. In zwei Dimensionen wird daraus ein Kamm mit unendlich vielen Zinken, die Menge
$C\times[0,1]$.

:::grafik
Szene: hoema3/integralrechnung-rn/04-fette-cantor-menge · Vorlage: intervall-zerlegung-1d
Das Intervall $[0,1]$; Schritt für Schritt verschwinden offene Mittelstücke der Längen $\frac14$, zweimal $\frac1{16}$,
viermal $\frac1{64}$ und so fort. Übrig bleibt ein immer feinerer Staub, dessen Restlänge sich $\frac12$ nähert. Darüber
eine Zerlegung mit Ober- und Untersumme: Die Untersumme bleibt $0$, die Obersumme nie unter $\frac12$. Kernaussage: Eine
Form, die nur aus Rand besteht, sprengt das Riemann-Integral. (Rot = Menge $C$, grau = entfernte Stücke, orange = Ober-
und Untersumme.)
:::
::::

**Was die Lebesgue-Theorie leistet.** Für **jede** abgeschlossene, beschränkte Menge $M$ und jedes stetige $f$ liefert die
Integrationstheorie nach Lebesgue einen eindeutigen Wert für das Integral über $M$. Wo ein iteriertes Integral existiert —
in welcher Reihenfolge auch immer —, stimmt es mit diesem Wert überein. Die Begründung sprengt den Rahmen dieser Seiten;
die Idee ist anschaulich.

:::herleitung
Nur die Beweisidee. Man ersetzt die senkrechte Wand durch eine **Böschung**. Dazu setzt man $f$ zuerst zu einer stetigen
Funktion $\hat f$ auf dem ganzen Kasten fort — das geht immer (Fortsetzungssatz von Tietze). Dann multipliziert man mit
einem Faktor, der auf $M$ gleich $1$ ist und in einem schmalen Saum um $M$ linear auf null abfällt:

$$f_\ell(\vec x) := \hat f(\vec x)\cdot\max\big(0,\;1-\ell\,\mathrm{dist}(\vec x,M)\big), \qquad \ell\in\mathbb{N}.$$

Dabei ist $\mathrm{dist}(\vec x,M)$ der kleinste Abstand von $\vec x$ zu einem Punkt von $M$. Jedes $f_\ell$ ist stetig,
sein Integral kennt man also aus dem vorigen Artikel. Mit wachsendem $\ell$ wird der Saum schmaler.

An jeder Stelle streben die $f_\ell$ gegen $\bar f$: Auf $M$ ist der Faktor $1$. Außerhalb von $M$ ist der Abstand
positiv — weil $M$ abgeschlossen ist —, sodass der Faktor ab einem $\ell$ null ist. Einen gemeinsamen Deckel liefert das
Maximum von $\lvert\hat f\rvert$ auf dem Kasten. Der Satz von der majorisierten Konvergenz, das Gegenstück zum
Majorantenkriterium im vorletzten Artikel, sichert dann, dass die Integrale konvergieren und der Grenzwert nicht von der
gewählten Böschung abhängt. Er ist das Integral über $M$.

Die Fortsetzung ist beschränkt und lebt auf einem beschränkten Kasten, ist also absolut integrierbar. Nach dem Satz von
Fubini–Tonelli aus dem vorigen Artikel liefert deshalb jede Integrationsreihenfolge denselben Wert.
:::

::::beispiel Die Wand abschrägen
Für den Kuchen aus der Springform — Höhe $1$ auf der Einheitskreisscheibe $S_1$ — ersetzt man die Wand durch Böschungen:

$$f_\ell(\vec x) = \max\big(0,\;1-\ell\,\mathrm{dist}(\vec x,S_1)\big), \qquad \ell\in\mathbb{N}.$$

Den Abstand zur Scheibe kann man direkt angeben:

$$\mathrm{dist}(\vec x,S_1) = \max\big(0,\;\lvert\vec x\rvert-1\big).$$

:::herleitung
Für einen Punkt der Scheibe ist der Abstand null. Für einen Punkt $\vec x$ mit $\lvert\vec x\rvert>1$ und jeden Punkt
$\vec y\in S_1$ gilt nach der Dreiecksungleichung

$$\lvert\vec x-\vec y\rvert \ge \lvert\vec x\rvert-\lvert\vec y\rvert \ge \lvert\vec x\rvert-1,$$

und der Randpunkt $\vec x/\lvert\vec x\rvert$ hat genau diesen Abstand.
:::

Also ist $f_\ell$ auf $S_1$ gleich $1$, fällt zwischen den Radien $1$ und $1+\frac1\ell$ linear auf $0$ und ist danach
null. Es liegt zwischen den Indikatorfunktionen zweier Kreisscheiben:

$$\bar 1_{S_1} \le f_\ell \le \bar 1_{S_{1+1/\ell}}.$$

Mit der Monotonie und der Formel für die Kreisscheibe folgt im Kasten $[-2,2]^2$

$$\pi \le \int_{[-2,2]^2} f_\ell(\vec x)\,d^2x \le \pi\Big(1+\frac1\ell\Big)^2.$$

Für wachsendes $\ell$ streben die Integrale der stetigen Böschungen also gegen $\pi$ — genau den Wert, den das iterierte
Integral für den Kuchen mit Wand lieferte.

**Im Bild:** Je steiler die Böschung, desto näher liegt das Volumen am Kuchen mit senkrechter Wand. Die Böschung fügt
höchstens einen Ring hinzu, dessen Fläche gegen null geht:

$$\pi\Big(1+\frac1\ell\Big)^2-\pi = \pi\Big(\frac2\ell+\frac1{\ell^2}\Big).$$
::::

**Wie man in der Praxis rechnet.** Die Fortsetzung durch null klärt, **was** das Integral über eine Form ist. Zum
Ausrechnen nutzt man Formen mit glattem Rand: Man zerlegt $M$ in __Normalbereiche__, über die man Scheibe für Scheibe mit
wandernden Grenzen integriert (nächster Artikel), oder man wechselt in passende Koordinaten, etwa Polarkoordinaten
(Transformationssatz, später).

## Das Prinzip von Cavalieri: Volumen aus Querschnitten

**Die Akteure:** eine Höhe $H>0$ und für jede Höhe $z\in[0,H]$ ein __Querschnitt__ — eine abgeschlossene Menge
$D(z)\subseteq\mathbb{R}^2$, alle in einem gemeinsamen Rechteck $Q_2\subseteq\mathbb{R}^2$. Daraus entsteht der Körper

$$K = \big\{(x,y,z)\in\mathbb{R}^3 \;:\; (x,y)\in D(z),\ 0\le z\le H\big\}\subseteq\mathbb{R}^3.$$

Die Fläche des Querschnitts in der Höhe $z$ sei eine stetige Funktion von $z$:

$$s(z) := \mathrm{vol}\big(D(z)\big), \qquad z\in[0,H].$$

Üblich ist auch $A(z)$; als skalare Ergebnisfunktion heißt sie hier klein, $s$ wie Scheibe — wie die Scheibenfläche
im vorigen Artikel.

**Das Zusammenspiel:** *Wie viel Teig steckt in der Torte?*

:::formel Satz
$$\mathrm{vol}(K) = \int_0^H s(z)\,dz.$$
:::

**So liest man das:** Eingabe ist die Flächenfunktion $s$ — eine Zahl für jede Höhe —, Ausgabe das Volumen. Das Volumen
ist das Integral der Querschnittsflächen. Statt $[0,H]$ darf das Höhenintervall jedes Intervall $[z_0,z_1]$ sein; die
Herleitung ändert sich dabei nicht.

**Im Bild:** Der Konditor schneidet die Torte in dünne waagerechte Böden. Ein Boden der Dicke $h$ in der Höhe $z$ hat
ungefähr das Volumen $s(z)\,h$, und die Torte ist der Stapel aller Böden — wie das Brot im vorigen Artikel, nur waagerecht
geschnitten.

:::grafik
Szene: hoema3/integralrechnung-rn/04-tortenboeden · Vorlage: gleiche-querschnitte-3d
Ein Körper $K$ über dem Höhenintervall $[0,H]$, in $N$ waagerechte Schichten der Dicke $h$ zerlegt. In jeder Schicht steht
ein flacher Zylinder mit der Grundfläche $D(z_k)$; ein Regler erhöht $N$, die Zylinderstapel schmiegen sich an den Körper,
und die Summe $h\sum s(z_k)$ nähert sich $\int_0^H s(z)\,dz$. Daneben zwei Münzstapel, einer gerade, einer schräg
geschoben, mit gleichem Volumen. Kernaussage: Ein Volumen ist ein Stapel von Querschnittsflächen. (Rot = Körper, orange =
aktuelle Schicht, blau = Flächenfunktion $s$, grau = Achsen.)
:::

:::herleitung
**Die Scheibchen-Summe.** Man teilt die Höhe in $N\in\mathbb{N}$ Schichten der Dicke

$$h = \frac{H}{N}$$

und wählt in jeder Schicht eine Höhe $z_k$:

$$(k-1)\,h\le z_k\le k\,h, \qquad k=1,\ldots,N.$$

Die $k$-te Schicht ist ungefähr ein flacher Zylinder mit der Grundfläche $D(z_k)$ und der Höhe $h$:

$$\mathrm{vol}(K) \approx h\sum_{k=1}^{N} s(z_k).$$

Das ist eine __Riemann-Summe__ der stetigen Funktion $s$. Für $h\to0$ strebt sie nach der Theorie des Riemann-Integrals
gegen $\int_0^H s(z)\,dz$, gleich wie man die $z_k$ wählt.

**Exakt aus der Definition.** Man stellt $K$ in den Kasten $Q_2\times[0,H]$. Ein Punkt in der Höhe $z$ liegt genau dann in
$K$, wenn $(x,y)$ in $D(z)$ liegt:

$$\bar 1_K(x,y,z) = \bar 1_{D(z)}(x,y).$$

Das Mehrfachintegral integriert zuerst über $x$ und $y$, zuletzt über $z$. Die beiden inneren Integrationen messen also
genau die Fläche des Querschnitts:

$$\int_{Q_2}\bar 1_{D(z)}(x,y)\,d^2x = \mathrm{vol}\big(D(z)\big) = s(z).$$

Das äußere Integral stapelt die Querschnitte:

$$\mathrm{vol}(K) = \int_0^H s(z)\,dz.$$

**Im Bild:** Nimmt man $z$ als letzte Variable, schneidet die Definition des Mehrfachintegrals die Torte schon in Böden. Die
Scheibchen-Summe ist nur die Riemann-Summe des äußersten Integrals.
:::

::::beispiel Die Eiswaffel
Ein Kegel mit Grundradius $R$ und Höhe $H$ wird auf die Spitze gestellt: Spitze im Ursprung, Grundkreis oben
in der Höhe $H$.

**Der Querschnitt.** In der Höhe $z$ ist er eine Kreisscheibe. Ihr Radius wächst nach dem Strahlensatz linear von $0$ an
der Spitze bis $R$ am oberen Rand:

$$r(z) = \frac{zR}{H}, \qquad s(z) = \pi\,r(z)^2 = \pi\,\frac{R^2}{H^2}\,z^2.$$

**Der Stapel.**

$$\mathrm{vol}(K) = \int_0^H \pi\,\frac{R^2}{H^2}\,z^2\,dz = \pi\,\frac{R^2}{H^2}\cdot\frac{H^3}{3} = \frac{\pi}{3}\,R^2H.$$

**In Zahlen:** Eine Eiswaffel mit

$$R = 3\,\text{cm}, \qquad H = 12\,\text{cm}$$

fasst

$$\frac{\pi}{3}\cdot9\cdot12\,\text{cm}^3 = 36\pi\,\text{cm}^3 \approx 113\,\text{cm}^3.$$

**Im Bild:** Ein Zylinder mit derselben Grundfläche und Höhe hat das Volumen $\pi R^2H$. Der Kegel ist genau ein Drittel
davon, weil seine Böden nach unten quadratisch schrumpfen — im Mittel ist $z^2$ auf $[0,H]$ ein Drittel von $H^2$.
::::

**Gleiche Querschnitte, gleiches Volumen.** Daraus folgt die ursprüngliche Aussage Cavalieris aus dem 17. Jahrhundert:
Haben zwei Körper in **jeder** Höhe Querschnitte mit gleichem Flächeninhalt, so haben sie dasselbe Volumen — gleich, wie
die Querschnitte geformt oder gegeneinander verschoben sind.

:::herleitung
Beide Volumina sind nach dem Satz das Integral derselben Flächenfunktion $s$ über dasselbe Höhenintervall.
:::

**Im Bild:** Ein Stapel Münzen hat dasselbe Volumen, ob er gerade steht oder schräg geschoben ist.

::::beispiel Schief geschoben und der Napf
**(a) Der schiefe Kegel.** Man verschiebt die Böden der Eiswaffel waagerecht, den Boden in der Höhe $z$ um den Vektor
$\tfrac{z}{H}\,\vec c$ mit einem festen $\vec c\in\mathbb{R}^2$. So entsteht ein schiefer Kegel, dessen Spitze nicht mehr
unter der Mitte des Grundkreises liegt. Eine Verschiebung ändert keine Fläche: Jede Scheibe des Bodens rutscht nur ein
Stück und behält ihre Länge, und das Integral über die Scheiben verschiebt sich mit. Also behält der Kegel sein Volumen:

$$\mathrm{vol} = \frac{\pi}{3}\,R^2H.$$

**(b) Der Napf.** In den Höhen zwischen $0$ und $R$ vergleicht man zwei Körper:

- die **Halbkugel** vom Radius $R$ über der Ebene $z=0$. Ihr Boden in der Höhe $z$ ist nach Pythagoras eine Kreisscheibe
  vom Radius $\sqrt{R^2-z^2}$;
- den **Napf**: einen Zylinder vom Radius $R$ und der Höhe $R$, aus dem ein auf der Spitze stehender Kegel mit der Spitze
  im Ursprung herausgebohrt ist. Sein Boden in der Höhe $z$ ist ein Ring zwischen den Radien $z$ und $R$.

Beide Böden haben dieselbe Fläche:

$$\pi\big(\sqrt{R^2-z^2}\big)^2 = \pi R^2-\pi z^2.$$

Die Ringfläche ist dabei die große Scheibe minus die kleine; der gemeinsame Randkreis hat keine Fläche. Nach Cavalieri
sind die Volumina gleich:

$$\mathrm{vol}(\text{Halbkugel}) = \pi R^2\cdot R-\frac{\pi}{3}\,R^2\cdot R = \frac23\,\pi R^3.$$

**Im Bild:** Halbkugel und Napf sind in jeder Höhe gleich „dick", also gleich schwer. Dass die Kugel zwei Drittel ihres
umschließenden Zylinders füllt, wusste schon Archimedes; mit Cavalieri wird daraus eine Zeile.

:::grafik
Szene: hoema3/integralrechnung-rn/04-napf · Vorlage: gleiche-querschnitte-3d
Links eine Halbkugel vom Radius $R$, rechts ein Zylinder gleicher Höhe mit herausgebohrtem Kegel (Spitze unten). Eine
waagerechte Ebene in der Höhe $z$ fährt auf und ab; sie schneidet links eine Kreisscheibe vom Radius $\sqrt{R^2-z^2}$,
rechts einen Ring zwischen $z$ und $R$, beide mit der Flächenanzeige $\pi(R^2-z^2)$. Kernaussage: Gleiche Querschnitte in
jeder Höhe bedeuten gleiches Volumen. (Rot = Körper, orange = Schnittfläche, grau = Achse, gestrichelt = Kegel im
Zylinder.)
:::
::::

**Rotationskörper.** Dreht man eine Kurve um die $z$-Achse, entsteht ein __Rotationskörper__. **Die Akteure:** eine
stetige Profilfunktion $r:[0,H]\to[0,\infty)$, die in jeder Höhe den Abstand der Oberfläche von der Achse angibt, und der
Körper

$$K = \big\{(x,y,z)\in\mathbb{R}^3 \;:\; x^2+y^2\le r(z)^2,\ 0\le z\le H\big\}\subseteq\mathbb{R}^3.$$

Seine Querschnitte sind Kreisscheiben vom Radius $r(z)$, und Cavalieri liefert

$$\mathrm{vol}(K) = \pi\int_0^H r(z)^2\,dz.$$

**Im Bild:** Eine Drehbank formt das Profil; jeder waagerechte Schnitt durch das Werkstück ist eine Kreisscheibe.

:::herleitung
In der Höhe $z$ ist der Querschnitt die Kreisscheibe vom Radius $r(z)$ um die Achse. Nach der Formel für die Kreisscheibe
hat sie die Fläche

$$s(z) = \pi\,r(z)^2,$$

und die ist stetig in $z$, weil $r$ stetig ist. Wo $r(z)$ null ist, besteht der Querschnitt aus einem Punkt mit der Fläche
null, passend zur Formel. Cavalieri ergibt die Behauptung — ebenso für jedes andere Höhenintervall.
:::

::::beispiel Kugel und runder Laib als Rotationskörper
**(a) Die Kugel** vom Radius $R$ um den Ursprung ist ein Rotationskörper über dem Höhenintervall $[-R,R]$. Nach Pythagoras
hat sie in der Höhe $z$ den Radius

$$r(z) = \sqrt{R^2-z^2}.$$

Also

$$\mathrm{vol} = \pi\int_{-R}^{R}(R^2-z^2)\,dz = \pi\Big[R^2z-\frac{z^3}{3}\Big]_{z=-R}^{z=R} = \pi\Big(2R^3-\frac23\,R^3\Big) = \frac43\,\pi R^3.$$

Das ist das Doppelte der Halbkugel aus dem Napf-Vergleich.

**(b) Der runde Laib** aus dem vorigen Artikel ist der Körper unter der Fläche

$$z = 1-x^2-y^2$$

über der Ebene $z=0$. Er ist ein Rotationskörper über $[0,1]$: In der Höhe $z$ gehören die Punkte mit

$$x^2+y^2\le1-z$$

dazu. Also

$$r(z)^2 = 1-z, \qquad \mathrm{vol} = \pi\int_0^1(1-z)\,dz = \frac{\pi}{2}.$$

Im vorigen Artikel kam dasselbe Volumen aus senkrechten Scheiben.

**Im Bild:** Dasselbe Brot, einmal senkrecht und einmal waagerecht geschnitten — und beide Male dasselbe Volumen.
::::

## Bedeutung und Ausblick

Mit der Fortsetzung durch null ist das Integral über jede abgeschlossene, beschränkte Form erklärt. Die Wand am Rand ist
harmlos, solange der Rand keine Fläche hat; für zerfranste Ränder braucht man die Lebesgue-Theorie. Das Volumen ist das
Integral der Eins, und Cavalieri baut es aus Querschnitten auf. Das ist die Grundlage für Masse, Ladung und Schwerpunkt
realer Körper.

Cavalieri schneidet in **einer** Richtung und setzt voraus, dass man die Querschnittsflächen schon kennt. Der nächste
Artikel macht daraus ein allgemeines Rechenverfahren: In einem __Normalbereich__ ist jede Scheibe ein Intervall, dessen
Enden mit dem Messer wandern. Man integriert mit variablen Grenzen, und die Leibnizregel garantiert, dass sich die
Scheibenflächen ohne Sprünge ändern.

:::kern
- Über eine abgeschlossene, beschränkte Form $M\subseteq\mathbb{R}^n$ integriert man, indem man $f$ **durch null** auf einen umgebenden Kasten fortsetzt.
- Der Kasten ist beliebig: Leerer Platz trägt nichts bei.
- Die Fortsetzung $\bar f$ springt am Rand, wo $f$ nicht null ist — die senkrechte Wand des gebackenen Brots.
- **Abgeschlossen** heißt: Der Rand gehört zur Form; Mengen aus Ungleichungen mit „kleiner gleich" sind abgeschlossen.
- Hat der Rand keine Fläche, ist er also eine __Nullmenge__ wie die Kreislinie, so stört die Wand nicht.
- Eine Form, die nur aus Wand besteht (fette Cantor-Menge), sprengt das Riemann-Integral; die Lebesgue-Theorie liefert trotzdem einen Wert.
- Das __Volumen__ ist das Integral der Eins: $\mathrm{vol}(M)=\int_M 1\,d^n x$.
- __Cavalieri__: Das Volumen ist das Integral der Querschnittsflächen, $\mathrm{vol}(K)=\int_0^H s(z)\,dz$.
- Gleiche Querschnittsflächen in jeder Höhe bedeuten gleiches Volumen.
- Rotationskörper: $\mathrm{vol}(K)=\pi\int_0^H r(z)^2\,dz$.
- Kegel und Kugel fallen so in zwei Zeilen: ein Drittel des Zylinders bzw. $\frac43\pi R^3$.
:::

:::quiz
F: Wie integriert man eine stetige Funktion über eine abgeschlossene, beschränkte Menge $M$, und warum ist die Wahl des Kastens egal?
A: Man stellt $M$ in einen Quader $Q$ und setzt $f$ durch null fort: $\bar f=f$ auf $M$, $\bar f=0$ daneben; dann ist $\int_M f:=\int_Q\bar f$. Ein größerer Kasten fügt nur Stücke hinzu, auf denen $\bar f$ null ist — sie tragen nichts bei. Im Bild ist das leerer Platz im Brotkasten.
F: Was bedeuten „beschränkt" und „abgeschlossen" für eine Form $M\subseteq\mathbb{R}^n$, und wozu braucht man beides?
A: Beschränkt: $M$ liegt in einer Kugel, passt also in einen Kasten. Abgeschlossen: Das Komplement ist offen, gleichwertig enthält $M$ seinen ganzen Rand. Zusammen heißt das kompakt; dann ist das stetige $f$ beschränkt. Für die Böschung der Lebesgue-Idee braucht man außerdem, dass Punkte außerhalb von $M$ einen positiven Abstand zu $M$ haben — das liefert die Abgeschlossenheit.
F: Warum ist die Fortsetzung durch null am Rand im Allgemeinen unstetig?
A: Ein Randpunkt $\vec x_0$ gehört zu $M$, dort ist $\bar f(\vec x_0)=f(\vec x_0)$. Ist das nicht null, enthält trotzdem jede Kugel um $\vec x_0$ Punkte außerhalb von $M$ mit $\bar f=0$ — ein Sprung. Im Bild ist das die senkrechte Wand eines gebackenen Brots. Nur wenn $f$ am Rand null ist, wie beim runden Laib, gibt es keine Wand.
F: Warum lässt sich der Kuchen aus der Springform trotz Wand Scheibe für Scheibe integrieren?
A: Bei festem $y$ ist die Höhe $1$ genau auf dem Intervall $\lvert x\rvert\le\sqrt{1-y^2}$, also ist die Scheibenfläche $s(y)=2\sqrt{1-y^2}$. Sie hängt stetig von $y$ ab, weil die Enden der Scheibe stetig wandern. Das iterierte Integral ergibt $\pi$, den Flächeninhalt der Einheitskreisscheibe.
F: Was ist eine Nullmenge, und warum ist die Kreislinie eine?
A: Eine Menge, die sich für jedes $\varepsilon>0$ mit endlich vielen Quadern vom Gesamtvolumen unter $\varepsilon$ überdecken lässt. Teilt man die Kreislinie in $N$ Bögen, liegt jeder in einem Quadrat der Seitenlänge $4\pi/N$; zusammen ergibt das $16\pi^2/N$, was gegen null geht. Im Bild hat die Wand im Grundriss keine Fläche, ihre Sprünge kosten nichts.
F: Warum versagt das Riemann-Integral bei der fetten Cantor-Menge?
A: Sie enthält kein Intervall, also hat jedes Teilintervall einer Zerlegung einen Punkt mit Fortsetzung $0$ — jede Untersumme ist $0$. Die Teilintervalle, die die Menge treffen, haben zusammen mindestens die Länge $\tfrac12$, weil insgesamt nur die Länge $\tfrac12$ entfernt wurde — jede Obersumme ist mindestens $\tfrac12$. Die Form besteht nur aus Wand; Lebesgue misst ihr die Länge $\tfrac12$ zu.
F: Wie liefert die Lebesgue-Theorie trotzdem ein Integral über jede abgeschlossene, beschränkte Menge?
A: Man ersetzt die Wand durch eine Böschung: stetige Funktionen $f_\ell$, die in einem Saum der Breite $1/\ell$ um $M$ auf null abfallen. Sie streben an jeder Stelle gegen $\bar f$, weil Punkte außerhalb von $M$ einen positiven Abstand haben, und ein gemeinsamer Deckel ist das Maximum des Betrags. Die majorisierte Konvergenz sichert den Grenzwert der Integrale. Bei der Kreisscheibe liegen die Integrale zwischen $\pi$ und $\pi(1+1/\ell)^2$, der Grenzwert ist $\pi$.
F: Wie hängt $\mathrm{vol}(M)=\int_M 1\,d^n x$ mit dem Brot-Bild zusammen, und was ergibt sich für Quader, Kreisscheibe und Dreieck?
A: Ein Brot der Höhe $1$ in der Form $M$ hat das Volumen „Grundfläche mal $1$" — das Integral der Eins misst die Grundfläche, in drei Dimensionen die Masse eines Teigs der Dichte $1$. Für einen Quader ergibt sich das Produkt der Kantenlängen, für die Kreisscheibe vom Radius $r$ der Flächeninhalt $\pi r^2$, für das Dreieck $0\le y\le x\le1$ in beiden Schnittrichtungen $\tfrac12$.
F: Was besagt das Prinzip von Cavalieri, und warum folgt es direkt aus der Definition des Mehrfachintegrals?
A: $\mathrm{vol}(K)=\int_0^H s(z)\,dz$ mit der Querschnittsfläche $s(z)$. Das Mehrfachintegral integriert zuerst über $x$ und $y$ und zuletzt über $z$; die inneren Integrale messen also genau die Querschnittsfläche, das äußere stapelt die Böden. Die Scheibchen-Summe $h\sum s(z_k)$ ist die Riemann-Summe dazu.
F: Wie ergeben sich Kegel- und Kugelvolumen mit Cavalieri, und was zeigt der Napf?
A: Kegel auf der Spitze: Der Radius in der Höhe $z$ ist $zR/H$ (Strahlensatz), also $s(z)=\pi R^2z^2/H^2$ und $\mathrm{vol}=\frac{\pi}{3}R^2H$. Kugel: Radius $\sqrt{R^2-z^2}$ (Pythagoras), also $\frac43\pi R^3$. Der Napf, ein Zylinder ohne Kegel, hat in jeder Höhe denselben Querschnitt $\pi(R^2-z^2)$ wie die Halbkugel, also dasselbe Volumen $\frac23\pi R^3$.
:::
