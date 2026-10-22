---
title: Die Integralsätze in der Ebene (Green und Gauß)
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030500
summary: Von Grund auf – wie die Arbeit längs eines Zauns mit den Wirbeln im eingezäunten Grundstück zusammenhängt (Satz von Stokes, Greensche Formel) und der Ausfluss durch den Zaun mit den Quellen darin (Satz von Gauß). Leitbild ist ein Grundstück aus Parzellen – die Rundtouren um die Parzellen heben sich im Inneren auf, übrig bleibt der Zaun. Mit regulären Bereichen und Randorientierung, vollständigem Beweis, der koordinatenfreien Deutung von Divergenz und Rotation, der Planimeter-Formel für Flächen und einer Beispiel-Seite.
tags: Satz von Green, Satz von Stokes, Satz von Gauß, Divergenz, Rotation, Randorientierung, Flächenformel, Planimeter
---

## Anschaulich

Ein **Grundstück** mit einem Zaun, darüber weht ein Wind. Im Artikel über Divergenz und Rotation hatten wir an jeder Stelle
zwei Messgeräte aufgestellt: ein kleines **Schaufelrad**, das sich dreht, wenn der Wind wirbelt, und ein kleines
**Kästchen**, aus dem netto Luft herausströmt, wenn es dort eine Quelle gibt. Jetzt fragen wir nach dem Ganzen.

**Das Leitbild dieses Artikels:** Man zerlegt das Grundstück in viele kleine **Parzellen** und fährt um jede eine kleine
Rundtour, immer so, dass die Parzelle links liegt. Jede Tour misst die Wirbel in ihrer Parzelle — Rotation mal Fläche. Legt man
alle Touren zusammen, wird jede Grenze zwischen zwei Parzellen **zweimal** befahren, einmal in jeder Richtung. Diese Beiträge
heben sich weg. Übrig bleibt nur die Tour um den äußeren Zaun.

Das ist der __Satz von Stokes in der Ebene__, in Komponenten die __Greensche Formel__: Die Arbeit des Winds längs des
Zauns ist die Summe aller Wirbel im Grundstück. Mit dem Kästchen statt dem Schaufelrad entsteht der __Satz von Gauß__: Was
durch den Zaun hinausströmt, ist die Summe aller Quellen darin.

Beide Sätze lassen sich auch rückwärts lesen. Eine Fläche ist ein Integral der Eins — und lässt sich deshalb allein durch
Abfahren des Randes messen. Genau das tut ein mechanisches __Planimeter__.

:::grafik
Szene: hoema3/kurvenintegrale/05-parzellen · Vorlage: parzellen-zirkulation-2d
Ein Grundstück $D$ mit Zaun, über ihm ein Windfeld $\vec F$ mit kleinen Schaufelrädern. Das Grundstück zerfällt in ein Gitter
von Parzellen; um jede läuft eine kleine Rundtour gegen den Uhrzeigersinn. Auf den inneren Grenzen leuchten je zwei
entgegengesetzte Pfeile auf und verschwinden, bis nur die Tour um den Zaun übrig ist. Ein Zähler zeigt links die Summe
der Wirbel, rechts die Arbeit längs des Zauns — beide gleich. Kernaussage: Die inneren Grenzen heben sich weg, der Zaun
misst die Wirbel im Inneren. (Blau = Feld, orange = Rundtouren, rot = Zaun, grau = Parzellengitter.)
:::

## Reguläre Bereiche und ihr Rand

**Die Akteure:** Ein __regulärer Bereich__ ist eine beschränkte, abgeschlossene Menge $D\subseteq\mathbb{R}^2$, deren Inneres
— die Menge der inneren Punkte — wegzusammenhängend ist und deren Rand aus endlich vielen geschlossenen regulären Kurven
besteht.

**Im Bild:** ein Grundstück aus einem Stück, eingefasst von einem oder mehreren Zäunen. Ein Teich mitten im Grundstück, der
nicht dazugehört, hat seinen eigenen Zaun — der Rand besteht dann aus zwei Kurven.

**Positiv orientiert** heißt der Rand $\partial D$, wenn alle Randkurven so durchlaufen werden, dass das Innere von $D$ links
liegt. Für die Einheitstangente $\vec\tau$ des Randes bedeutet das: Der um $90^\circ$ nach links gedrehte Vektor

$$\vec\tau^{\,\perp} = (-\tau_2,\ \tau_1)$$

zeigt ins Innere von $D$.

**Im Bild:** Wer am Zaun entlanggeht, hat das Grundstück stets zur linken Hand — am äußeren Zaun läuft man also gegen den
Uhrzeigersinn, um einen Teich herum im Uhrzeigersinn.

:::grafik
Szene: hoema3/kurvenintegrale/05-randorientierung · Vorlage: parzellen-zirkulation-2d
Ein Grundstück mit einem Teich. Auf dem äußeren Zaun läuft ein Pfeil gegen, auf dem Ufer des Teichs im Uhrzeigersinn; an
mehreren Stellen sind die Einheitstangente $\vec\tau$, der nach links gedrehte Vektor (zeigt ins Grundstück) und die äußere
Normale $\vec\nu$ (zeigt aus dem Grundstück hinaus, am Teich also zum Wasser) eingezeichnet. Kernaussage: Positiv orientiert
heißt, das Grundstück liegt links. (Rot = Grundstück, orange = Randpfeile, blau = Normalen, grau = Teich.)
:::

::::beispiel Ränder positiv durchlaufen
**(a) Die Kreisscheibe** vom Radius $r$: Der Rand läuft gegen den Uhrzeigersinn,

$$\vec\gamma(t) = (r\cos t,\ r\sin t), \qquad \vec\tau = (-\sin t,\ \cos t), \qquad \vec\tau^{\,\perp} = (-\cos t,\ -\sin t).$$

Der gedrehte Vektor zeigt zum Mittelpunkt, also nach innen.

**(b) Der Ring** zwischen den Radien $1$ und $2$ hat zwei Randkurven. Die äußere läuft gegen den Uhrzeigersinn, die innere im
Uhrzeigersinn:

$$\vec\gamma_a(t) = (2\cos t,\ 2\sin t), \qquad \vec\gamma_i(t) = (\cos t,\ -\sin t), \qquad t\in[0,2\pi].$$

Auf dem inneren Kreis ist die Einheitstangente $(-\sin t,\ -\cos t)$, der gedrehte Vektor also $(\cos t,\ -\sin t)$ — er zeigt
vom Ursprung weg, in den Ring hinein.

**(c) Das Einheitsquadrat**: gegen den Uhrzeigersinn, unten nach rechts, rechts hinauf, oben nach links, links hinab — wie die
Rundtour um das Quadrat im Artikel über das Kurvenintegral.

**Im Bild:** In allen drei Fällen hat, wer den Rand abläuft, das Grundstück zur Linken.
::::

## Der Satz von Stokes in der Ebene

**Die Akteure:** ein regulärer Bereich $D$ mit positiv orientiertem Rand und ein Vektorfeld $\vec F$, das auf einer offenen
Umgebung von $D$ stetig differenzierbar ist. Die Rotation ist in der Ebene die Zahl

$$\operatorname{rot}\vec F = \partial_1F_2-\partial_2F_1.$$

:::formel Satz
$$\int_D\operatorname{rot}\vec F\,d(x,y) = \oint_{\partial D}\vec F\cdot d\vec x.$$
:::

**So liest man das:** Links stehen die Wirbel, über das Grundstück summiert — Eingabe ist das Feld, Ausgabe eine Zahl.
Rechts steht die Arbeit des Winds längs aller Randkurven, positiv durchlaufen. In Komponenten, oft auch $P$ und $Q$
genannt, ist das die __Greensche Formel__:

:::formel
$$\int_D\Big(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\Big)\,d(x,y) = \oint_{\partial D}F_1\,dx+F_2\,dy.$$
:::

Dabei ist $F_1\,dx+F_2\,dy$ die Kurzschreibweise für das Skalarprodukt $\vec F\cdot d\vec x$.

**Im Bild:** Die Rundtour um eine winzige Parzelle misst Rotation mal Fläche — so wurde die Rotation im Divergenz-Artikel
gedeutet. Legt man die Parzellen zusammen, heben sich alle inneren Grenzen weg, und der Zaun misst die Summe.

:::herleitung
**Schritt 1: ein Normalbereich.** Sei zuerst $D$ ein regulärer Normalbereich vom ersten Typ, mit stetig differenzierbaren
Wänden $\alpha\le\beta$ über $[c,d]$. Positiv orientiert besteht sein Rand aus vier Stücken: die rechte Wand $(\beta(y),y)$
nach oben, die obere Kante von rechts nach links, die linke Wand $(\alpha(y),y)$ nach unten, die untere Kante von links nach
rechts. Man behandelt die beiden Komponenten getrennt.

**Der Anteil von $F_2$.** Nach dem Satz über Normalbereiche und dem Hauptsatz in $x$:

$$\int_D\frac{\partial F_2}{\partial x}\,d(x,y) = \int_c^d\Big(F_2\big(\beta(y),y\big)-F_2\big(\alpha(y),y\big)\Big)\,dy.$$

Auf dem Rand trägt das Feld $(0,F_2)$ nur auf den Wänden bei, wo man sich nach oben oder unten bewegt — auf der rechten Wand
mit $+F_2$, auf der linken, abwärts durchlaufen, mit $-F_2$. Das ist genau die rechte Seite.

**Der Anteil von $F_1$.** Mit der Abkürzung für die Scheibenfläche

$$S(y) := \int_{\alpha(y)}^{\beta(y)}F_1(x,y)\,dx$$

gibt die Leibnizregel aus dem Artikel über Parameterintegrale

$$\int_{\alpha(y)}^{\beta(y)}\frac{\partial F_1}{\partial y}\,dx = S'(y)-F_1\big(\beta(y),y\big)\,\beta'(y)+F_1\big(\alpha(y),y\big)\,\alpha'(y).$$

Integriert über $y$:

$$\int_D\frac{\partial F_1}{\partial y}\,d(x,y) = S(d)-S(c)-\int_c^d F_1\big(\beta(y),y\big)\,\beta'(y)\,dy+\int_c^d F_1\big(\alpha(y),y\big)\,\alpha'(y)\,dy.$$

Auf dem Rand trägt das Feld $(F_1,0)$ überall bei, wo man sich seitwärts bewegt. Die rechte Wand gibt
$\int F_1(\beta,y)\,\beta'\,dy$, die linke, abwärts, $-\int F_1(\alpha,y)\,\alpha'\,dy$, die obere Kante, nach links,
$-S(d)$, die untere, nach rechts, $+S(c)$. Zusammen ist das genau das Negative des Flächenintegrals.

**Zusammen:**

$$\oint_{\partial D}\vec F\cdot d\vec x = \int_D\frac{\partial F_2}{\partial x}\,d(x,y)-\int_D\frac{\partial F_1}{\partial y}\,d(x,y) = \int_D\operatorname{rot}\vec F\,d(x,y).$$

Hier braucht man, dass die Wände stetig differenzierbar sind — deshalb verlangt der Satz reguläre Bereiche. Für
Normalbereiche vom zweiten Typ geht es mit vertauschten Rollen von $x$ und $y$ genauso.

**Schritt 2: zusammengesetzte Bereiche.** Ein allgemeiner regulärer Bereich
lässt sich in reguläre Normalbereiche zerlegen. Für jedes Teilstück gilt Schritt 1. Summiert man, addieren sich links die
Flächenintegrale zum Integral über $D$. Rechts wird jede innere Schnittlinie zweimal befahren, einmal von jedem
angrenzenden Teilstück aus und in entgegengesetzter Richtung, weil jedes sein Inneres links hat; diese Beiträge heben sich
nach der Regel für die Rückfahrt weg. Übrig bleibt der positiv orientierte Rand von $D$.

**Im Bild:** Schritt 2 ist genau das Parzellenbild: Innere Grenzen werden hin und zurück befahren und zählen nicht.
:::

::::beispiel Drei Proben
**(a) Der Wirbel auf der Kreisscheibe.** Für das Feld

$$\vec F(x,y) = (-y,\ x), \qquad \operatorname{rot}\vec F = 1-(-1) = 2,$$

ist die linke Seite zweimal die Fläche, $2\pi r^2$. Auf dem Rand gegen den Uhrzeigersinn ist der Integrand

$$(-r\sin t)(-r\sin t)+(r\cos t)(r\cos t) = r^2, \qquad \oint_{\partial D}\vec F\cdot d\vec x = 2\pi r^2.$$

**(b) Der Wirbel auf dem Einheitsquadrat.** Die linke Seite ist zweimal die Fläche, also $2$. Genau das hatte die
Rundtour um das Quadrat im Artikel über das Kurvenintegral ergeben — dort als Zufall angekündigt, hier erklärt.

**(c) Ein ungleichmäßiger Wirbel.** Auf dem Einheitsquadrat sei

$$\vec F(x,y) = (0,\ x^2), \qquad \operatorname{rot}\vec F = 2x, \qquad \int_0^1\!\!\int_0^1 2x\,dx\,dy = 1.$$

Auf dem Rand weht der Wind nur nach oben, und nur auf der rechten Kante bei $x=1$ mit der Stärke $1$, wo man nach oben fährt:

$$\oint_{\partial D}\vec F\cdot d\vec x = \int_0^1 1\,dt = 1.$$

**Im Bild:** Bei (c) drehen sich die Schaufelräder rechts schneller als links. Am Zaun merkt man davon nur die rechte Kante,
wo der Wind mitschiebt — und das ist genau die Summe aller Drehungen.
::::

**Ein zweiter Beweis des zweiten Hauptsatzes.** In der Ebene liefert Stokes den zweiten Hauptsatz neu. Ist
$G\subseteq\mathbb{R}^2$ einfach zusammenhängend, so ist jede doppelpunktfreie, geschlossene, reguläre Kurve in $G$ — bis auf
die Orientierung — der Rand eines regulären Bereichs in $G$. Das ist ein Satz der Topologie (Jordanscher Kurvensatz), den wir
hier nicht beweisen. Für ein wirbelfreies Feld ist dann

$$\oint_\gamma\vec F\cdot d\vec x = \pm\int_D\operatorname{rot}\vec F\,d(x,y) = 0.$$

Kurven mit Doppelpunkten zerlegt man in doppelpunktfreie Schleifen.

**Im Bild:** Ohne Säule umschließt jeder Zaun nur Gelände, auf dem kein Schaufelrad sich dreht — also leistet der Wind längs
des Zauns nichts.

::::beispiel Der Ring um die Säule
Die Wendeltreppe

$$\vec W(x,y) = \frac{1}{x^2+y^2}\,(-y,\ x)$$

ist auf dem Ring zwischen den Radien $1$ und $2$ stetig differenzierbar und wirbelfrei. Stokes auf dem Ring, mit dem äußeren
Kreis gegen und dem inneren im Uhrzeigersinn:

$$0 = \int_{\text{Ring}}\operatorname{rot}\vec W\,d(x,y) = \oint_{\text{außen}}\vec W\cdot d\vec x+\oint_{\text{innen, im Uhrzeigersinn}}\vec W\cdot d\vec x = 2\pi+(-2\pi).$$

Gegen den Uhrzeigersinn bringen also beide Kreise dieselbe Arbeit $2\pi$ — dasselbe Ergebnis wie mit der Homotopie im vorigen
Artikel.

Auf der ganzen Kreisscheibe darf man Stokes dagegen **nicht** anwenden: Der Ursprung gehört dazu, und dort ist $\vec W$ gar
nicht erklärt.

**Im Bild:** Der Ring ist das Gelände zwischen zwei Zäunen um die Säule. Weil sich darin kein Schaufelrad dreht, leisten der
äußere und der innere Zaun, gleich herum durchlaufen, dieselbe Arbeit. Der „Wirbel" der Wendeltreppe sitzt ganz in der Säule.
::::

## Der Satz von Gauß in der Ebene

Statt der Arbeit längs des Zauns misst man jetzt, wie viel durch ihn **hinausströmt**. Dazu braucht man die Richtung
senkrecht zum Zaun nach außen.

**Die Akteure:** Für den positiv orientierten Rand mit der Einheitstangente $\vec\tau$ ist das __äußere Einheitsnormalenfeld__
$\vec\nu$ der Vektor, den man um $90^\circ$ nach links drehen muss, um $\vec\tau$ zu erhalten:

:::formel Definition
$$\vec\tau = \vec\nu^{\,\perp}, \qquad \vec\nu^{\,\perp} = (-\nu_2,\ \nu_1), \qquad\text{also}\qquad \vec\nu = (\tau_2,\ -\tau_1).$$
:::

**So liest man das:** $\vec\nu$ ist $\vec\tau$ um $90^\circ$ nach **rechts** gedreht. Weil das Innere links liegt, zeigt
$\vec\nu$ nach außen. Es hat wie $\vec\tau$ die Länge $1$.

Dann gilt für ein stetig differenzierbares Feld auf einer Umgebung von $D$:

:::formel Satz
$$\int_D\operatorname{div}\vec F\,d(x,y) = \oint_{\partial D}\vec F\cdot\vec\nu\,ds.$$
:::

**So liest man das:** Links stehen die Quellen, über das Grundstück summiert. Rechts steht der __Fluss__ durch den Zaun:
der Anteil des Winds senkrecht nach außen, mal gefahrene Strecke, aufsummiert.

**Im Bild:** Jedes Kästchen lässt netto so viel Luft heraus, wie in ihm entsteht. Was ein Kästchen an seiner Grenze an das
Nachbarkästchen abgibt, nimmt dieses auf — diese inneren Flüsse heben sich weg, und übrig bleibt, was durch den Zaun ins
Freie geht.

:::grafik
Szene: hoema3/kurvenintegrale/05-kaestchen-fluss · Vorlage: parzellen-zirkulation-2d
Dasselbe Grundstück, jetzt mit Kästchen statt Schaufelrädern. In jedem Kästchen zeigt eine Zahl die Quelle darin; an jeder
inneren Grenze fließt Luft vom einen ins andere Kästchen, die beiden Pfeile heben sich auf. Am Zaun zeigen Pfeile senkrecht
nach außen, wie viel hinausströmt. Ein Zähler vergleicht die Summe der Quellen mit dem Fluss durch den Zaun. Kernaussage:
Was im Inneren entsteht, muss durch den Rand hinaus. (Blau = Feld, orange = Flusspfeile, rot = Zaun, grau = Kästchen.)
:::

:::herleitung
Man dreht das Feld um $90^\circ$ nach links und wendet Stokes an. Für

$$\vec G = (-F_2,\ F_1)$$

ist nach dem Divergenz-Artikel die Rotation die Divergenz von $\vec F$:

$$\operatorname{rot}\vec G = \partial_1F_1-\partial_2(-F_2) = \operatorname{div}\vec F.$$

Längs des Randes gilt mit $d\vec x=\vec\tau\,ds$:

$$\vec G\cdot\vec\tau = -F_2\,\tau_1+F_1\,\tau_2 = \vec F\cdot(\tau_2,\ -\tau_1) = \vec F\cdot\vec\nu.$$

Stokes für $\vec G$ ergibt also genau den Satz von Gauß. Umgekehrt folgt Stokes ebenso aus Gauß — in der Ebene sind beide
Sätze gleichwertig.
:::

::::beispiel Quellen und Fluss
**(a) Ein Quellfeld auf der Kreisscheibe.** Für das radiale Feld

$$\vec F(x,y) = (x,\ y), \qquad \operatorname{div}\vec F = 2,$$

ist die linke Seite zweimal die Fläche, $2\pi r^2$. Auf dem Rand ist die äußere Normale der Einheitsvektor in Richtung des
Ortes, und

$$\vec\nu = (\cos t,\ \sin t), \qquad \vec F\cdot\vec\nu = r, \qquad \oint_{\partial D}\vec F\cdot\vec\nu\,ds = r\cdot2\pi r = 2\pi r^2.$$

**(b) Die Quelle im Loch.** Das ebene Feld einer Punktquelle

$$\vec E(x,y) = \frac{1}{x^2+y^2}\,(x,\ y)$$

ist außerhalb des Ursprungs quellenfrei:

$$\operatorname{div}\vec E = \frac{(x^2+y^2)-2x^2}{(x^2+y^2)^2}+\frac{(x^2+y^2)-2y^2}{(x^2+y^2)^2} = 0.$$

Durch jeden Kreis vom Radius $R$ um den Ursprung fließt trotzdem gleich viel hinaus: Dort ist $\vec E\cdot\vec\nu=\frac1R$, der
Fluss also $\frac1R\cdot2\pi R=2\pi$. Auf dem Ring zwischen zwei solchen Kreisen sagt Gauß: Was durch den inneren Kreis
hineinfließt, fließt durch den äußeren hinaus.

**Im Bild:** Die Quelle sitzt im Loch, das zum Ring nicht gehört. Im Ring selbst entsteht nichts — jedes Kreisband lässt so
viel hinaus, wie es von innen bekommt.
::::

## Divergenz und Rotation ohne Koordinaten

Die beiden Sätze geben Divergenz und Rotation eine Bedeutung, die von keinem Koordinatensystem abhängt. Der Schlüssel ist ein
einfacher Mittelwertsatz: Für eine in einer Umgebung von $\vec x$ stetige Funktion $f$ ist $f(\vec x)$ der Grenzwert ihrer
Mittelwerte über immer kleinere Kreisscheiben,

$$f(\vec x) = \lim_{r\to0}\frac{1}{\lvert B_r(\vec x)\rvert}\int_{B_r(\vec x)}f(\vec y)\,d^2y.$$

:::herleitung
Die Mittelwerte unterscheiden sich von $f(\vec x)$ nur durch den Mittelwert der Abweichungen. Nach Monotonie und Linearität
ist das höchstens die größte Abweichung auf der Scheibe:

$$\Big\lvert\frac{1}{\lvert B_r(\vec x)\rvert}\int_{B_r(\vec x)}\big(f(\vec y)-f(\vec x)\big)\,d^2y\Big\rvert \le \max_{\lvert\vec y-\vec x\rvert\le r}\lvert f(\vec y)-f(\vec x)\rvert.$$

Weil $f$ stetig ist, geht das für $r\to0$ gegen null.
:::

Wendet man das auf $\operatorname{div}\vec F$ und $\operatorname{rot}\vec F$ an und ersetzt die Flächenintegrale mit Gauß und
Stokes durch Randintegrale, entstehen die __Quellendichte__ und die __Wirbeldichte__:

:::formel
$$\operatorname{div}\vec F(\vec x) = \lim_{R\to0}\frac{1}{\lvert B_R(\vec x)\rvert}\oint_{\partial B_R(\vec x)}\vec F\cdot\vec\nu\,ds, \qquad \operatorname{rot}\vec F(\vec x) = \lim_{R\to0}\frac{1}{\lvert B_R(\vec x)\rvert}\oint_{\partial B_R(\vec x)}\vec F\cdot\vec\tau\,ds.$$
:::

**So liest man das:** Die Divergenz ist der Ausfluss durch einen winzigen Kreis, geteilt durch seine Fläche. Die Rotation ist
die Arbeit längs eines winzigen Kreises, geteilt durch seine Fläche. Beides sind physikalische Messgrößen, die man ohne
Achsen ablesen könnte.

**Im Bild:** Das ist die genaue Fassung der Bilder aus dem Divergenz-Artikel: Das Kästchen wird zum winzigen Kreis, durch den
man den Fluss misst, das Schaufelrad zur winzigen Rundtour, auf der man die Arbeit misst.

:::herleitung
Auf der abgeschlossenen Kreisscheibe vom Radius $R$ um $\vec x$ gibt Gauß

$$\frac{1}{\lvert B_R(\vec x)\rvert}\oint_{\partial B_R(\vec x)}\vec F\cdot\vec\nu\,ds = \frac{1}{\lvert B_R(\vec x)\rvert}\int_{B_R(\vec x)}\operatorname{div}\vec F\,d^2y.$$

Weil $\operatorname{div}\vec F$ stetig ist, strebt die rechte Seite nach dem Mittelwertsatz gegen $\operatorname{div}\vec F(\vec x)$.
Für die Rotation genauso mit Stokes und $\vec F\cdot d\vec x=\vec F\cdot\vec\tau\,ds$.
:::

::::beispiel Kästchen und Schaufelrad am Kreis
Um den Ursprung misst man auf dem Kreis vom Radius $R$ mit

$$\vec\nu = (\cos t,\ \sin t), \qquad \vec\tau = (-\sin t,\ \cos t), \qquad ds = R\,dt.$$

**(a) Die Dehnung** $\vec F(x,y)=(x,0)$ hat die Divergenz $1$ und die Rotation $0$. Auf dem Kreis:

$$\vec F\cdot\vec\nu = R\cos^2t, \qquad \oint\vec F\cdot\vec\nu\,ds = R^2\int_0^{2\pi}\cos^2t\,dt = \pi R^2, \qquad \oint\vec F\cdot\vec\tau\,ds = -R^2\int_0^{2\pi}\cos t\sin t\,dt = 0.$$

Geteilt durch die Fläche $\pi R^2$: Quellendichte $1$, Wirbeldichte $0$.

**(b) Die Scherung** $\vec F(x,y)=(y,0)$ hat die Divergenz $0$ und die Rotation $-1$. Auf dem Kreis:

$$\vec F\cdot\vec\nu = R\sin t\cos t, \qquad \oint\vec F\cdot\vec\nu\,ds = 0, \qquad \vec F\cdot\vec\tau = -R\sin^2t, \qquad \oint\vec F\cdot\vec\tau\,ds = -\pi R^2.$$

Geteilt durch die Fläche: Quellendichte $0$, Wirbeldichte $-1$.

**Im Bild:** Die Dehnung bläst den Kreis auf — es strömt mehr hinaus als hinein —, dreht ihn aber nicht. Die Scherung schiebt
oben nach rechts und unten nach links; das dreht ein Schaufelrad im Uhrzeigersinn, daher das Minuszeichen.
::::

## Flächen messen mit dem Planimeter

Wählt man in der Greenschen Formel ein Feld mit der Rotation $1$, wird die linke Seite zur Fläche. Ein solches Feld ist

$$F_1 = -\frac{y}{2}, \qquad F_2 = \frac{x}{2}, \qquad \frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y} = \frac12+\frac12 = 1.$$

Für einen regulären Bereich, dessen Rand aus einer einzigen geschlossenen regulären Kurve $\vec\gamma:[a,b]\to\mathbb{R}^2$
besteht, folgt die __Planimeter-Formel__:

:::formel
$$\lvert D\rvert = \frac12\int_a^b\Big(\gamma_1(t)\,\dot\gamma_2(t)-\gamma_2(t)\,\dot\gamma_1(t)\Big)\,dt = \frac12\int_a^b\det\big(\vec\gamma(t)\,\big|\,\dot{\vec\gamma}(t)\big)\,dt.$$
:::

**So liest man das:** In der Determinante stehen der Ortsvektor und die Geschwindigkeit als Spalten. Sie ist die Fläche des
Parallelogramms aus beiden, die Hälfte davon die Fläche des schmalen Dreiecks, das der Fahrstrahl vom Ursprung in der Zeit
$dt$ überstreicht.

**Im Bild:** Ein Planimeter fährt mit einem Stift den Rand einer Fläche ab und zeigt danach ihren Inhalt an — ohne je ins
Innere zu schauen. Genau das sagt die Formel: Die Fläche steckt im Rand.

:::grafik
Szene: hoema3/kurvenintegrale/05-planimeter · Vorlage: fahrstrahl-flaeche-2d
Eine geschlossene Randkurve um eine Fläche; ein Punkt fährt sie ab, und der Fahrstrahl vom Ursprung zum Punkt überstreicht
schmale Dreiecke, deren Flächen $\frac12\det(\vec\gamma\,|\,\dot{\vec\gamma})\,dt$ ein Zähler aufsummiert. Liegt der Ursprung
außerhalb, werden manche Dreiecke rückwärts überstrichen und negativ gezählt. Am Ende zeigt der Zähler die Fläche.
Kernaussage: Die Fläche lässt sich allein durch Abfahren des Randes messen. (Rot = Fläche, orange = Fahrstrahl und
Dreiecke, grau = Achsen.)
:::

:::herleitung
Mit diesem Feld ist die linke Seite der Greenschen Formel das Integral der Eins, also die Fläche. Rechts setzt man die
Parametrisierung ein:

$$\oint_{\partial D}F_1\,dx+F_2\,dy = \int_a^b\Big(-\frac{\gamma_2}{2}\,\dot\gamma_1+\frac{\gamma_1}{2}\,\dot\gamma_2\Big)\,dt.$$

Das ist die Hälfte des Integrals von $\gamma_1\dot\gamma_2-\gamma_2\dot\gamma_1$, und das ist die Determinante der Matrix mit
den Spalten $\vec\gamma$ und $\dot{\vec\gamma}$.
:::

::::beispiel Ellipse und Vieleck
**(a) Die Ellipse** mit den Halbachsen $a$ und $b$, gegen den Uhrzeigersinn:

$$\vec\gamma(t) = (a\cos t,\ b\sin t), \qquad \det\big(\vec\gamma\,\big|\,\dot{\vec\gamma}\big) = a\cos t\cdot b\cos t-b\sin t\cdot(-a\sin t) = ab.$$

Die Fläche ist

$$\lvert D\rvert = \frac12\int_0^{2\pi}ab\,dt = \pi ab.$$

Der Umfang der Ellipse ist dagegen erstaunlich schwer: Er führt auf elliptische Integrale, die sich nicht elementar
ausrechnen lassen.

**(b) Ein Vieleck** mit den Ecken $\vec p_1,\ldots,\vec p_N$, gegen den Uhrzeigersinn: Auf jeder Kante ist die Determinante
konstant, und die Formel wird zur __Schnürsenkelformel__

$$\lvert D\rvert = \frac12\sum_{k=1}^{N}\det\big(\vec p_k\,\big|\,\vec p_{k+1}\big), \qquad \vec p_{N+1} := \vec p_1.$$

:::herleitung
Auf der Kante von $\vec p_k$ nach $\vec p_{k+1}$ fährt man mit

$$\vec\gamma(t) = \vec p_k+t\,(\vec p_{k+1}-\vec p_k), \qquad \dot{\vec\gamma}(t) = \vec p_{k+1}-\vec p_k, \qquad t\in[0,1].$$

Weil die Determinante linear in jeder Spalte ist und zwei gleiche Spalten null geben, ist sie längs der Kante konstant:

$$\det\big(\vec\gamma(t)\,\big|\,\dot{\vec\gamma}(t)\big) = \det\big(\vec p_k\,\big|\,\vec p_{k+1}-\vec p_k\big) = \det\big(\vec p_k\,\big|\,\vec p_{k+1}\big).$$
:::

Für das Viereck mit den Ecken $(0,0)$, $(3,0)$, $(3,2)$, $(1,3)$ sind die Determinanten der Reihe nach $0$, $6$, $7$ und
$0$:

$$\lvert D\rvert = \frac12\,(0+6+7+0) = \frac{13}{2}.$$

Zur Probe zerlegt man das Viereck längs der Diagonale vom Ursprung nach $(3,2)$ in zwei Dreiecke mit den Flächen $3$ und
$\tfrac72$.

**Im Bild:** Der Fahrstrahl vom Ursprung überstreicht auf jeder Kante ein Dreieck. Wo er rückwärts streicht, zählt das
Dreieck negativ — und am Ende bleibt genau die umfahrene Fläche.
::::

## Bedeutung und Ausblick

Die Integralsätze verbinden das Innere eines Gebiets mit seinem Rand: Wirbel im Inneren zeigen sich als Arbeit längs des
Randes, Quellen im Inneren als Fluss durch den Rand. Damit ist das ebene Bild aus dem Divergenz-Artikel vollständig — Divergenz
und Rotation sind die Dichten von Fluss und Arbeit. In der Elektrotechnik sind das die Grundformen der Maxwell-Gleichungen in
Integralform; ihre räumlichen Fassungen folgen in den Artikeln
[Der Satz von Stokes im Raum](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/satz-von-stokes-im-raum.html)
und [Der Satz von Gauß im Raum](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/satz-von-gauss-im-raum.html).

Zunächst hilft der Satz von Stokes an unerwarteter Stelle. Mit ihm beweist der Artikel
[Der Transformationssatz und Polarkoordinaten](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen/transformationssatz-und-polarkoordinaten.html)
den __Transformationssatz__ in der Ebene — die Regel, wie sich Flächenintegrale beim Wechsel der Koordinaten ändern, etwa zu
Polarkoordinaten. Die Planimeter-Formel deutet schon an, warum dabei eine Determinante auftaucht.

:::kern
- Ein __regulärer Bereich__ ist beschränkt, abgeschlossen, mit zusammenhängendem Inneren; sein Rand besteht aus endlich vielen geschlossenen regulären Kurven.
- **Positiv orientiert**: Wer den Rand abläuft, hat das Innere links — außen gegen, um Löcher herum im Uhrzeigersinn.
- __Satz von Stokes__ in der Ebene: $\int_D\operatorname{rot}\vec F\,d(x,y)=\oint_{\partial D}\vec F\cdot d\vec x$ — der Zaun misst die Wirbel.
- Beweis: für Normalbereiche mit Hauptsatz und Leibnizregel, sonst zerlegen — innere Grenzen werden hin und zurück befahren.
- In Komponenten ist das die __Greensche Formel__; der Wirbel $(-y,x)$ bringt deshalb längs jedes Randes die doppelte Fläche.
- __Äußere Normale__ $\vec\nu$: die Tangente um $90^\circ$ nach rechts gedreht.
- __Satz von Gauß__ in der Ebene: $\int_D\operatorname{div}\vec F\,d(x,y)=\oint_{\partial D}\vec F\cdot\vec\nu\,ds$ — gleichwertig zu Stokes.
- Divergenz und Rotation sind die Grenzwerte von Fluss bzw. Arbeit pro Fläche an winzigen Kreisen — ohne Koordinaten.
- __Planimeter-Formel__: Die Fläche ist das halbe Integral von $\det(\vec\gamma\,|\,\dot{\vec\gamma})$ längs des Randes.
:::

:::quiz
F: Was ist ein regulärer Bereich, und was heißt positiv orientierter Rand?
A: Eine beschränkte, abgeschlossene Menge der Ebene mit wegzusammenhängendem Inneren, deren Rand aus endlich vielen geschlossenen regulären Kurven besteht. Positiv orientiert heißt: Alle Randkurven werden so durchlaufen, dass das Innere links liegt — die um $90^\circ$ nach links gedrehte Tangente zeigt hinein. Beim Ring läuft daher der äußere Kreis gegen, der innere im Uhrzeigersinn.
F: Was besagt der Satz von Stokes in der Ebene, und was bedeutet er im Parzellenbild?
A: $\int_D\operatorname{rot}\vec F\,d(x,y)=\oint_{\partial D}\vec F\cdot d\vec x$. Die Rundtour um eine winzige Parzelle misst Rotation mal Fläche; legt man alle Parzellen zusammen, wird jede innere Grenze zweimal in entgegengesetzter Richtung befahren und hebt sich weg. Übrig bleibt die Arbeit längs des Zauns.
F: Wie beweist man Stokes für einen Normalbereich vom ersten Typ?
A: Den Anteil von $F_2$ liefert der Hauptsatz in $x$: $\int_D\partial_xF_2=\int_c^d(F_2(\beta,y)-F_2(\alpha,y))\,dy$, und das tragen die beiden Wände bei. Den Anteil von $F_1$ liefert die Leibnizregel mit den Ableitungen $\alpha'$, $\beta'$ der Wände; er ist das Negative des Randintegrals von $(F_1,0)$. Dafür braucht man stetig differenzierbare Wände — reguläre Bereiche.
F: Warum genügt es, Stokes für Normalbereiche zu beweisen?
A: Ein regulärer Bereich lässt sich in reguläre Normalbereiche zerlegen. Die Flächenintegrale addieren sich, und jede innere Schnittlinie wird von den beiden angrenzenden Stücken in entgegengesetzter Richtung befahren, weil jedes sein Inneres links hat. Diese Beiträge heben sich weg, übrig bleibt der Rand von $D$.
F: Was ergeben die Proben mit $(-y,x)$ und $(0,x^2)$?
A: Der Wirbel $(-y,x)$ hat die Rotation $2$; auf der Kreisscheibe sind beide Seiten $2\pi r^2$, auf dem Einheitsquadrat $2$ — das erklärt die Quadrat-Rundtour aus dem Kurvenintegral-Artikel. Für $(0,x^2)$ auf dem Quadrat ist die Rotation $2x$ mit Integral $1$, und am Rand schiebt der Wind nur auf der rechten Kante, ebenfalls mit Arbeit $1$.
F: Warum bringen bei der Wendeltreppe der innere und der äußere Kreis dieselbe Arbeit, und warum darf man Stokes nicht auf die ganze Kreisscheibe anwenden?
A: Auf dem Ring ist $\vec W$ stetig differenzierbar und wirbelfrei; Stokes gibt $0=\oint_{\text{außen}}+\oint_{\text{innen, im Uhrzeigersinn}}$, also bringen beide Kreise gegen den Uhrzeigersinn $2\pi$. Auf der Kreisscheibe läge der Ursprung im Bereich, wo $\vec W$ nicht erklärt ist — die Voraussetzung fehlt.
F: Wie folgt der Satz von Gauß aus dem Satz von Stokes?
A: Man dreht das Feld nach links, $\vec G=(-F_2,F_1)$. Dann ist $\operatorname{rot}\vec G=\operatorname{div}\vec F$, und längs des Randes ist $\vec G\cdot\vec\tau=\vec F\cdot\vec\nu$ mit der äußeren Normalen $\vec\nu=(\tau_2,-\tau_1)$. Stokes für $\vec G$ ist Gauß für $\vec F$.
F: Was zeigt das Feld $\frac{(x,y)}{x^2+y^2}$ über den Satz von Gauß?
A: Es ist außerhalb des Ursprungs quellenfrei, und durch jeden Kreis um den Ursprung fließt der Fluss $2\pi$. Auf dem Ring zwischen zwei Kreisen sagt Gauß: Was innen hineinfließt, fließt außen hinaus. Die Quelle sitzt im Loch, das zum Ring nicht gehört.
F: Wie lassen sich Divergenz und Rotation ohne Koordinaten erklären?
A: Als Grenzwerte: $\operatorname{div}\vec F(\vec x)$ ist der Fluss durch einen winzigen Kreis um $\vec x$ geteilt durch seine Fläche, $\operatorname{rot}\vec F(\vec x)$ die Arbeit längs des Kreises geteilt durch die Fläche. Das folgt aus Gauß bzw. Stokes und dem Mittelwertsatz für stetige Funktionen. Für die Scherung $(y,0)$ etwa ergibt sich Quellendichte $0$ und Wirbeldichte $-1$.
F: Wie berechnet man mit der Planimeter-Formel die Fläche einer Ellipse und eines Vielecks?
A: Mit dem Feld $(-\frac y2,\frac x2)$, dessen Rotation $1$ ist, wird die Fläche zu $\frac12\int\det(\vec\gamma\,|\,\dot{\vec\gamma})\,dt$. Für die Ellipse $(a\cos t,b\sin t)$ ist die Determinante $ab$, die Fläche $\pi ab$. Beim Vieleck ist die Determinante auf jeder Kante konstant, und es entsteht die Schnürsenkelformel $\frac12\sum\det(\vec p_k\,|\,\vec p_{k+1})$.
:::
