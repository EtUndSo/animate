---
title: Der Satz von Gauß im Raum
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050300
summary: Von Grund auf – der Satz von Gauß, $\int_V\operatorname{div}\vec F\,d^3x=\int_{\partial V}\vec F\cdot d\vec S$ mit der äußeren Normale. Leitbild ist ein Gebäude aus Zimmern – in jedem Zimmer entsteht Luft, durch jede Innentür fließt, was das eine Zimmer verlässt, ins nächste, und für das ganze Haus zählen nur die Außenwände. Mit der partiellen Integration im Raum, dem Rand über eine Böschung an der Wand, einem vollständigen Beweis für Normalbereiche, der Divergenz als Quelldichte, dem Gaußschen Gesetz für jede Fläche um eine Punktladung und den Greenschen Formeln. Mit Beispiel-Seite.
tags: Satz von Gauß, Divergenzsatz, partielle Integration, Divergenz, Flussintegral, äußere Normale, Quelldichte, Greensche Formel
---

## Anschaulich

Der Satz von Stokes hat eine Fläche mit ihrem Rand verbunden, über die Rotation. Der Satz von Gauß verbindet einen Körper mit
seiner Oberfläche, über die Divergenz. Er ist eine **Bilanz**: Was im Inneren an Feld entspringt, muss netto durch die
Oberfläche hinaus.

**Das Leitbild dieses Artikels:** ein **Gebäude aus Zimmern**. In jedem Zimmer steht ein Gebläse, das Luft erzeugt oder
absaugt — das sind die Quellen und Senken, gemessen von der Divergenz. Durch jede Innentür fließt, was das eine Zimmer
verlässt, ins Nachbarzimmer; in der Bilanz des ganzen Hauses hebt sich das weg. Übrig bleibt, was durch die Außenwände
strömt.

Ein einzelnes winziges Zimmer verrät die Divergenz an seinem Ort: Ausfluss geteilt durch Volumen. Und umgekehrt: Kennt man den
Ausfluss durch die Außenwände, kennt man die Summe aller Quellen im Haus. Für das elektrische Feld ist das das Gaußsche Gesetz
— der Fluss durch eine geschlossene Hülle misst die Ladung darin, gleichgültig, wie die Hülle geformt ist.

:::grafik
Szene: hoema3/integralsaetze-im-raum/03-gebaeude · Vorlage: gauss-zimmer-3d
Ein Gebäude im Schnitt, in Zimmer unterteilt; in einigen Zimmern Gebläse (Quellen, rote Punkte) und Absaugungen (Senken, blaue
Punkte), Luftpfeile zwischen den Zimmern und durch die Außenwände. Ein Regler blendet die Pfeile durch Innentüren aus, weil sie
sich in der Bilanz paarweise aufheben; zwei Zähler — Summe der Quellen und Fluss durch die Außenwände — zeigen denselben Wert.
Ein zweiter Regler verkleinert die Zimmer, bis eines zu einem Punkt schrumpft; dann zeigt ein dritter Zähler Fluss pro Volumen,
die Divergenz dort. Kernaussage: Die Quellen im Inneren sind der Ausfluss durch die Außenwände. (Rot = Quellen, blau = Senken,
orange = Luftströme, grau = Wände.)
:::

## Partielle Integration im Raum

Der Weg zum Satz beginnt mit der Produktregel. **Die Akteure:** zwei stetig differenzierbare Funktionen
$f,g:\mathbb{R}^n\to\mathbb{R}$, von denen mindestens eine einen kompakten Träger hat — sie ist außerhalb einer Kugel null. Dann
gilt für jede Koordinate $x_k$

$$\int_{\mathbb{R}^n}\frac{\partial f}{\partial x_k}(\vec x)\,g(\vec x)\;d^nx = -\int_{\mathbb{R}^n}f(\vec x)\,\frac{\partial g}{\partial x_k}(\vec x)\;d^nx.$$

:::herleitung
Nach der Produktregel ist

$$\frac{\partial}{\partial x_k}\big(fg\big) = \frac{\partial f}{\partial x_k}\,g+f\,\frac{\partial g}{\partial x_k}.$$

Das Produkt $fg$ ist außerhalb einer Kugel null, weil einer der Faktoren es ist. Nach Fubini integriert man zuerst über $x_k$;
nach dem Hauptsatz gibt das die Werte von $fg$ an den beiden Enden einer langen Strecke, und dort ist $fg$ null. Also ist das
Integral der linken Seite null, und die beiden Terme rechts sind entgegengesetzt gleich.

**Im Bild:** Die Ableitung wandert vom einen Faktor auf den anderen und nimmt ein Minuszeichen mit. Randterme gibt es keine,
weil weit draußen alles null ist — ein Gebäude ohne Außenwände.
:::

Für Vektorfelder wird daraus die __partielle Integration im Raum__. Ist $\vec G:\mathbb{R}^n\to\mathbb{R}^n$ ein stetig
differenzierbares Vektorfeld, $\psi:\mathbb{R}^n\to\mathbb{R}$ eine stetig differenzierbare Funktion, und hat eines von beiden einen
kompakten Träger, so gilt

:::formel Satz
$$\int_{\mathbb{R}^n}\big(\operatorname{div}\vec G\big)(\vec x)\,\psi(\vec x)\;d^nx = -\int_{\mathbb{R}^n}\vec G(\vec x)\cdot\nabla\psi(\vec x)\;d^nx.$$
:::

**So liest man das:** Die Ableitung wandert vom Feld, wo sie als Divergenz steht, auf die Funktion, wo sie als Gradient steht,
mit einem Minuszeichen.

**Im Bild:** Eine Gewichtung $\psi$ der Zimmer. Die gewichtete Summe der Quellen ist das, was entlang des Gefälles der
Gewichtung abfließt.

:::herleitung
Nach der Produktregel für Divergenzen aus dem Artikel über Rechenregeln ist

$$\operatorname{div}\big(\psi\,\vec G\big) = \nabla\psi\cdot\vec G+\psi\,\operatorname{div}\vec G.$$

Das Feld $\psi\vec G$ hat einen kompakten Träger. Seine Divergenz ist die Summe der Ableitungen $\partial_k(\psi G_k)$, und jede davon
hat nach der Rechnung oben das Integral null. Also ist das Integral der rechten Seite null.
:::

::::beispiel Gewichtete Quellen in der Kugel
Das Ortsvektorfeld $\vec G=\vec x$ hat überall die Divergenz $3$. Als Gewichtung dient die glatte Wolke aus dem Artikel über das
Newtonpotential, mit kompaktem Träger:

$$\psi(\vec x) = \big(1-\lvert\vec x\rvert^2\big)^2 \quad\text{für } \lvert\vec x\rvert\le1, \qquad \psi = 0 \quad\text{sonst}.$$

In Kugelkoordinaten ist die linke Seite

$$\int_{K_1}3\,\big(1-r^2\big)^2\;d^3x = 12\pi\int_0^1\big(1-r^2\big)^2r^2\;dr = 12\pi\cdot\frac{8}{105} = \frac{32\pi}{35}.$$

Rechts braucht man den Gradienten der Gewichtung und sein Skalarprodukt mit dem Feld:

$$\nabla\psi = -4\big(1-r^2\big)\,\vec x, \qquad \vec x\cdot\nabla\psi = -4\big(1-r^2\big)\,r^2.$$

Damit ist

$$-\int_{K_1}\vec x\cdot\nabla\psi\;d^3x = 16\pi\int_0^1\big(1-r^2\big)r^4\;dr = 16\pi\Big(\frac15-\frac17\Big) = \frac{32\pi}{35}.$$

**Im Bild:** Die Gewichtung fällt vom Mittelpunkt nach außen ab. Was das radiale Feld entlang dieses Gefälles nach außen trägt,
ist genau die gewichtete Summe der Quellen.
::::

## Ein Rand kommt ins Spiel

Bisher gab es keinen Rand. Um ihn einzuführen, beschränkt man das Integral auf einen Körper $V\subseteq\mathbb{R}^3$ mit Hilfe der
__Indikatorfunktion__ $\mathbf 1_V$, die auf $V$ gleich $1$ und außerhalb gleich $0$ ist:

$$\int_V\operatorname{div}\vec G\;d^3x = \int_{\mathbb{R}^3}\operatorname{div}\vec G\;\mathbf 1_V\;d^3x.$$

Die Indikatorfunktion springt aber am Rand $\partial V$ und ist nicht stetig; den Satz darf man mit ihr nicht anwenden. Ihr
„Gradient" ist überall null, nur am Rand nicht — dort konzentriert er sich und zeigt ins Innere. Formal schreibt man

$$\nabla\mathbf 1_V\,d^3x \sim -\,d\vec S,$$

mit $d\vec S=\vec n\,d\sigma$ und der äußeren Normale $\vec n$. Setzt man das ein, wird aus dem Volumenintegral ein Integral über
die Oberfläche.

**Im Bild:** Die Gewichtung ist im Haus $1$ und draußen $0$. Ihr ganzes Gefälle steckt in den Außenwänden, und genau dort wird
das Feld nach außen getragen.

:::herleitung
**Mit einer Böschung** wird das formale Argument greifbar, wie im Artikel über Integration über Mengen. Man ersetzt die Wand
durch eine Böschung der Breite $\delta$: eine Funktion $\psi_\delta$, die im Inneren $1$ ist, außerhalb von $V$ null, und in einer
dünnen Schicht innen an der Wand gleichmäßig von $1$ auf $0$ abfällt. In dieser Schicht ist ihr Gradient ungefähr

$$\nabla\psi_\delta \approx -\frac{1}{\delta}\,\vec n,$$

denn auf der Strecke $\delta$ fällt sie quer zur Wand um $1$. Die partielle Integration gibt

$$\int_{\mathbb{R}^3}\operatorname{div}\vec G\;\psi_\delta\;d^3x = -\int_{\mathbb{R}^3}\vec G\cdot\nabla\psi_\delta\;d^3x \approx \frac{1}{\delta}\int_{\text{Schicht}}\vec G\cdot\vec n\;d^3x.$$

Die Schicht hat über jedem Flächenstück $d\sigma$ das Volumen $\delta\,d\sigma$. Für $\delta\to0$ strebt die linke Seite gegen das
Integral der Divergenz über $V$, die rechte gegen das Integral von $\vec G\cdot\vec n$ über den Rand. Streng wird das mit einem glatten
Rand; einen vollständigen Beweis auf anderem Weg gibt der nächste Abschnitt.
:::

:::grafik
Szene: hoema3/integralsaetze-im-raum/03-boeschung · Vorlage: indikator-boeschung-2d
Ein Schnitt durch einen Körper: links die Indikatorfunktion als Plateau der Höhe $1$ mit senkrechter Wand, rechts eine Böschung,
die in einer Schicht der Breite $\delta$ abfällt. In der Schicht sind Gradientenpfeile eingezeichnet, die ins Innere zeigen und mit
kleinerem $\delta$ länger werden. Ein Regler verkleinert $\delta$; ein Zähler zeigt das Integral von $-\vec G\cdot\nabla\psi_\delta$ und
nähert sich dem Fluss durch die Wand. Kernaussage: Das Gefälle der Indikatorfunktion sitzt am Rand und zeigt nach innen. (Blau =
Plateau und Böschung, rot = Gradientenpfeile, orange = Feld, grau = Achsen.)
:::

## Der Satz von Gauß

**Die Akteure:** ein beschränkter, abgeschlossener Körper $V\subseteq\mathbb{R}^3$ mit glattem Rand $\partial V$ und ein Vektorfeld
$\vec F:U\to\mathbb{R}^3$, das auf einer offenen Menge $U\subseteq\mathbb{R}^3$ um $V$ stetig differenzierbar ist. Der Rand wird durch
die **äußere** Normale $\vec n$ orientiert. Dann gilt

:::formel Satz
$$\int_V\operatorname{div}\vec F\;d^3x = \int_{\partial V}\vec F\cdot d\vec S, \qquad d\vec S = \vec n\,d\sigma.$$
:::

**So liest man das:** Links die Summe aller Quellen im Inneren, rechts der Nettofluss durch die Oberfläche, Ausfluss positiv,
Einfluss negativ. Beide Seiten sind Zahlen.

**Im Bild:** Das Gebäude. Jedes Zimmer bilanziert seine Gebläse gegen den Luftstrom durch seine Wände; durch jede Innentür zählt
der Strom einmal als Ausfluss und einmal als Einfluss. In der Summe bleiben nur die Außenwände.

:::herleitung
**Schritt 1: ein Normalbereich in $z$-Richtung.** Sei $V$ ein Normalbereich wie im Artikel über Normalbereiche: Über einem
regulären Bereich $D$ der $xy$-Ebene liegt er zwischen einem Boden und einem Deckel, Graphen stetig differenzierbarer
Funktionen $\alpha\le\beta$:

$$V = \big\{(x,y,z)\in\mathbb{R}^3 : (x,y)\in D,\ \alpha(x,y)\le z\le\beta(x,y)\big\}.$$

Für die dritte Komponente gibt Fubini, innen über $z$ mit dem Hauptsatz,

$$\int_V\frac{\partial F_3}{\partial z}\;d^3x = \int_D\Big(F_3\big(x,y,\beta(x,y)\big)-F_3\big(x,y,\alpha(x,y)\big)\Big)\;d(x,y).$$

**Schritt 2: dieselbe Zahl als Fluss.** Der Rand von $V$ besteht aus Deckel, Boden und einer senkrechten Seitenwand über dem Rand
von $D$. Auf der Seitenwand ist die äußere Normale waagerecht, ihre dritte Komponente null. Den Deckel parametrisiert man als
Graph; nach dem vorigen Artikel ist das Kreuzprodukt $(-\partial_x\beta,-\partial_y\beta,1)$ und zeigt nach oben, also nach außen.
Am Boden zeigt die äußere Normale nach unten, das Kreuzprodukt kommt mit Minuszeichen. Für das Feld $(0,0,F_3)$ ergibt die
Rechenformel für Flüsse

$$\int_{\partial V}F_3\,n_3\;d\sigma = \int_D F_3\big(x,y,\beta\big)\;d(x,y)-\int_D F_3\big(x,y,\alpha\big)\;d(x,y)+0,$$

dasselbe wie in Schritt 1.

**Schritt 3: alle Richtungen.** Ist $V$ auch in $x$- und in $y$-Richtung ein Normalbereich — Kugeln und Quader sind es —, gilt
dasselbe für $F_1$ und $F_2$. Die Summe der drei Gleichungen ist der Satz.

**Schritt 4: zusammensetzen.** Einen allgemeineren Körper zerlegt man in solche Stücke. Eine Schnittfläche zwischen zwei Stücken
gehört zu beiden, mit entgegengesetzten äußeren Normalen; ihre Flüsse heben sich weg. Dass sich jeder Körper mit glattem Rand so
zerlegen lässt, ist ein technischer Punkt, den wir hier nicht ausführen.

**Im Bild:** Schritt 1 und 2 sind Säulen von Zimmern übereinander: Was durch die Decken strömt, hebt sich auf, übrig bleiben
Dach und Keller. Schritt 4 sind die Innentüren zwischen verschiedenen Gebäudeteilen.
:::

::::beispiel Quellen gegen Ausfluss
**(a) Das Ortsvektorfeld** über der Kugel vom Radius $R$: Die Divergenz ist $3$, die Normalkomponente auf der Kugel $R$:

$$\int_{K_R}3\;d^3x = 3\cdot\frac43\pi R^3 = 4\pi R^3, \qquad \int_{\partial K_R}\vec x\cdot d\vec S = R\cdot4\pi R^2 = 4\pi R^3.$$

**(b) Ein Feld im Einheitswürfel** $[0,1]^3$:

$$\vec F(x,y,z) = \big(x^2,\ y^2,\ z^2\big), \qquad \operatorname{div}\vec F = 2\,(x+y+z).$$

Die Quellen summieren sich zu

$$\int_{[0,1]^3}2\,(x+y+z)\;d^3x = 2\cdot3\cdot\frac12 = 3.$$

Zum Fluss trägt jede der drei Seiten bei, auf der die betreffende Koordinate $1$ ist, die Fläche $1$; auf den drei Seiten durch
den Ursprung ist die Normalkomponente null. Zusammen wieder $3$.

**Im Bild:** Bei (b) wachsen die Gebläse zur Ecke $(1,1,1)$ hin, und die Luft verlässt den Würfel nur durch die drei Seiten,
die dieser Ecke anliegen.
::::

## Divergenz als Quelldichte

Lässt man den Körper auf einen Punkt schrumpfen, gibt der Satz die anschauliche Bedeutung der Divergenz: **Fluss pro Volumen.**
Für die Kugeln $K_\delta(\vec x)$ vom Radius $\delta$ um einen Punkt $\vec x$ ist

:::formel
$$\operatorname{div}\vec F(\vec x) = \lim_{\delta\to0}\frac{1}{\mathrm{vol}\big(K_\delta(\vec x)\big)}\int_{\partial K_\delta(\vec x)}\vec F\cdot d\vec S.$$
:::

**So liest man das:** Die Divergenz an einem Punkt ist der Ausfluss aus einer winzigen Kugel um ihn, geteilt durch ihr Volumen.
Das ist die räumliche Fassung der koordinatenfreien Divergenz aus dem Artikel über die
[Integralsätze in der Ebene](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/integralsaetze-in-der-ebene.html).

**Im Bild:** Ein einziges winziges Zimmer. Sein Ausfluss pro Volumen ist die Leistung des Gebläses darin.

:::herleitung
Nach Gauß ist der Ausfluss das Integral der Divergenz über die Kugel. Geteilt durch das Volumen ist das ein Mittelwert, und er
unterscheidet sich vom Wert im Mittelpunkt höchstens um die größte Abweichung auf der Kugel:

$$\Big\lvert\frac{1}{\mathrm{vol}}\int_{K_\delta(\vec x)}\operatorname{div}\vec F\;d^3y-\operatorname{div}\vec F(\vec x)\Big\rvert \le \max_{\vec y\in K_\delta(\vec x)}\big\lvert\operatorname{div}\vec F(\vec y)-\operatorname{div}\vec F(\vec x)\big\rvert.$$

Weil die Divergenz stetig ist, geht die rechte Seite für $\delta\to0$ gegen null.
:::

In der Physik ist das die Form des __Gaußschen Gesetzes__. Die Maxwell-Gleichung für das elektrische Feld, mit der
Ladungsdichte $\rho$ und der Feldkonstante $\varepsilon_0$,

$$\operatorname{div}\vec E = \frac{\rho}{\varepsilon_0},$$

heißt integriert: Der elektrische Fluss durch eine geschlossene Hülle ist die eingeschlossene Ladung durch $\varepsilon_0$.

$$\int_{\partial V}\vec E\cdot d\vec S = \frac{1}{\varepsilon_0}\int_V\rho\;d^3x = \frac{Q_{\text{innen}}}{\varepsilon_0}.$$

:::herleitung
Man setzt die Maxwell-Gleichung in die linke Seite des Satzes von Gauß ein. Das Integral der Ladungsdichte über $V$ ist die
Ladung in $V$.
:::

::::beispiel Ein kleiner Würfel misst die Divergenz
Das Feld

$$\vec F(x,y,z) = \big(x^2,\ y,\ 0\big), \qquad \operatorname{div}\vec F = 2x+1,$$

hat am Punkt $(1,0,0)$ die Divergenz $3$. Statt einer Kugel nimmt man einen Würfel der Kantenlänge $h$ um diesen Punkt. Durch die
beiden Seiten senkrecht zur $x$-Achse fließt netto

$$\Big(\big(1+\tfrac h2\big)^2-\big(1-\tfrac h2\big)^2\Big)\,h^2 = 2h\cdot h^2,$$

durch die beiden Seiten senkrecht zur $y$-Achse $h\cdot h^2$, durch die übrigen nichts. Zusammen $3h^3$, geteilt durch das Volumen
$h^3$ genau $3$ — hier schon für jede Kantenlänge, weil das Feld so einfach ist.

**Im Bild:** Das winzige Zimmer am Punkt $(1,0,0)$ bläst in $x$-Richtung doppelt so stark aus, wie es ansaugt, und in
$y$-Richtung gleichmäßig — das gibt die Gebläseleistung $3$ pro Volumen.
::::

**Jede Hülle um eine Punktladung.** Für das Coulomb-Feld der Ladung $Q$ aus dem vorigen Artikel ist der Fluss durch jede
geschlossene, glatte Fläche, die den Ursprung umschließt, gleich $Q$ — und durch jede, die ihn nicht umschließt, null. Der Satz
von Gauß ist auf den Ursprung selbst nicht anwendbar, weil das Feld dort nicht definiert ist; man schneidet ihn heraus.

:::herleitung
**Ohne den Ursprung.** Liegt der Ursprung nicht in $V$, ist das Feld auf einer Umgebung von $V$ stetig differenzierbar und
quellenfrei; nach Gauß ist der Fluss null.

**Mit dem Ursprung im Inneren.** Man schneidet eine kleine Kugel $K_\delta$ um den Ursprung heraus, die ganz im Inneren von $V$
liegt. Auf dem Rest ist das Feld quellenfrei, und sein Rand besteht aus $\partial V$ und der kleinen Kugeloberfläche. Deren äußere
Normale — vom Rest aus gesehen — zeigt zum Ursprung hin. Nach Gauß ist deshalb

$$\int_{\partial V}\vec E\cdot d\vec S-\int_{\partial K_\delta}\vec E\cdot d\vec S = 0,$$

mit der Kugeloberfläche nach außen orientiert. Ihr Fluss ist nach dem vorigen Artikel $Q$.

**Im Bild:** Ein Gebäude mit einem Kamin in der Mitte, aus dem die Ladung strömt. Ohne Gebläse in den Zimmern kommt durch die
Außenwände genau heraus, was der Kamin liefert — gleichgültig, wie das Haus gebaut ist.
:::

::::beispiel Eine Punktladung in Würfel und Kugel
**(a) Im Würfel** $[-1,1]^3$ mit der Ladung $Q$ im Mittelpunkt: Nach dem Gesetz ist der Fluss $Q$, aus Symmetrie durch jede der
sechs Seiten $\frac Q6$. Auf der Deckelseite in der Höhe $1$ ist die Normalkomponente

$$E_3(x,y,1) = \frac{Q}{4\pi}\,\frac{1}{\big(x^2+y^2+1\big)^{3/2}},$$

und direkt gerechnet ist ihr Fluss

$$\frac{Q}{4\pi}\int_{-1}^1\int_{-1}^1\frac{dx\,dy}{\big(x^2+y^2+1\big)^{3/2}} = \frac Q6.$$

Der Wert des Doppelintegrals ist $\frac{2\pi}{3}$ — das folgt aus der Symmetrie, und eine numerische Rechnung bestätigt es.

**(b) Neben der Ladung,** in der Kugel vom Radius $1$ um $(0,0,3)$: Der Ursprung liegt außerhalb, der Fluss ist null. Was auf der
der Ladung zugewandten Seite einströmt, strömt auf der abgewandten wieder hinaus.

**Im Bild:** Bei (a) verteilt sich der Kamin gleichmäßig auf sechs Außenwände. Bei (b) steht das Haus neben dem Kamin, und der
Luftstrom zieht nur hindurch.
::::

## Partielle Integration mit Rand und die Greenschen Formeln

Als Folgerung aus dem Satz von Gauß erhält man die partielle Integration auf einem Körper mit Rand. **Die Akteure:** $V$ wie im
Satz von Gauß, ein Vektorfeld $\vec G:U\to\mathbb{R}^3$ und eine Funktion $\psi:U\to\mathbb{R}$, beide stetig differenzierbar auf
einer offenen Menge $U\subseteq\mathbb{R}^3$ um $V$. Dann gilt

:::formel Satz
$$\int_V\vec G\cdot\nabla\psi\;d^3x = \int_{\partial V}\psi\,\vec G\cdot d\vec S-\int_V\big(\operatorname{div}\vec G\big)\,\psi\;d^3x.$$
:::

**So liest man das:** Dieselbe Regel wie ohne Rand, nur dass jetzt ein Randterm auftritt — das, was die Gewichtung $\psi$ an der
Oberfläche noch hat.

**Im Bild:** Jetzt hat das Gebäude Außenwände. Die gewichtete Bilanz der Zimmer bekommt einen zusätzlichen Posten: den
gewichteten Strom durch die Außenwände.

:::herleitung
Man wendet den Satz von Gauß auf das Feld $\psi\vec G$ an und benutzt die Produktregel für die Divergenz:

$$\int_V\Big(\nabla\psi\cdot\vec G+\psi\,\operatorname{div}\vec G\Big)\;d^3x = \int_{\partial V}\psi\,\vec G\cdot d\vec S.$$

Den zweiten Term bringt man auf die andere Seite.
:::

**Die Greenschen Formeln** sind der Spezialfall eines Gradientenfelds. Für zweimal stetig differenzierbare Funktionen $u$ und $\psi$
auf $U$ sei

$$\frac{\partial u}{\partial n} = \nabla u\cdot\vec n$$

die __Normalableitung__ am Rand, die Steigung von $u$ senkrecht zur Oberfläche nach außen. Dann gelten die __erste__ und die
__zweite Greensche Formel__:

$$\int_V\nabla u\cdot\nabla\psi\;d^3x = \int_{\partial V}\psi\,\frac{\partial u}{\partial n}\;d\sigma-\int_V\psi\,\Delta u\;d^3x,$$

$$\int_V\big(\psi\,\Delta u-u\,\Delta\psi\big)\;d^3x = \int_{\partial V}\Big(\psi\,\frac{\partial u}{\partial n}-u\,\frac{\partial\psi}{\partial n}\Big)\;d\sigma.$$

Der Beweis der Poisson-Gleichung im nächsten Artikel benutzt die partielle Integration mit Rand auf dieselbe Weise.

:::herleitung
**Die erste Formel.** Man setzt in die partielle Integration mit Rand das Gradientenfeld $\vec G=\nabla u$ ein. Seine Divergenz ist
$\Delta u$, und am Rand ist $\nabla u\cdot\vec n$ die Normalableitung.

**Die zweite Formel.** Man schreibt die erste noch einmal mit vertauschten Rollen von $u$ und $\psi$ und zieht ab. Der Term
$\nabla u\cdot\nabla\psi$ ist in beiden gleich und fällt heraus; übrig bleibt die zweite Formel.

**Im Bild:** Die erste Formel wiegt die Strömung entlang des Gefälles von $u$ mit $\psi$; die zweite ist symmetrisch in beiden
Funktionen — was im Inneren nicht passt, steht als Fluss an den Außenwänden.
:::

::::beispiel Green an der Kugel nachgerechnet
Auf der Einheitskugel sei

$$u(\vec x) = \lvert\vec x\rvert^2 = r^2, \qquad \Delta u = 6, \qquad \frac{\partial u}{\partial n} = 2r = 2 \ \text{ auf der Kugel}.$$

**(a) Erste Formel mit der Gewichtung $1$:** Links steht null, denn $\nabla1=\vec 0$. Rechts:

$$\int_{\partial K_1}2\;d\sigma-\int_{K_1}6\;d^3x = 2\cdot4\pi-6\cdot\frac{4\pi}{3} = 0.$$

**(b) Erste Formel mit der Gewichtung $u$ selbst:** Links ist $\lvert\nabla u\rvert^2=4r^2$, also

$$\int_{K_1}4r^2\;d^3x = 4\cdot\frac{4\pi}{5} = \frac{16\pi}{5}, \qquad \int_{\partial K_1}1\cdot2\;d\sigma-\int_{K_1}r^2\cdot6\;d^3x = 8\pi-\frac{24\pi}{5} = \frac{16\pi}{5}.$$

**(c) Zweite Formel mit der Gewichtung $1$:** Beide Seiten sind $8\pi$:

$$\int_{K_1}\big(1\cdot6-r^2\cdot0\big)\;d^3x = 8\pi, \qquad \int_{\partial K_1}\big(1\cdot2-1\cdot0\big)\;d\sigma = 8\pi.$$

**Im Bild:** Das Feld $\nabla u=2\vec x$ ist der radiale Luftstrom aus dem ersten Beispiel, doppelt so stark. Bei (a) ist die Quellstärke
$6$ pro Volumen genau der Ausfluss $2$ pro Wandfläche, über die ganze Kugel gerechnet.
::::

## Bedeutung und Ausblick

Der Satz von Gauß ist die Integralform jeder Bilanzgleichung. In der Elektrostatik misst der Fluss durch eine Hülle die
eingeschlossene Ladung; in der Strömungslehre ist der Ausfluss aus einem Volumen die Summe der Quellen; und die
__Kontinuitätsgleichung__ der Ladung — die zeitliche Änderung der Ladungsdichte plus die Divergenz der Stromdichte ist null —
sagt integriert: Die Ladung in einem Volumen nimmt genau um den Strom ab, der durch seine Oberfläche hinausfließt.

Mit Gauß und Stokes sind die beiden räumlichen Integralsätze beisammen. Der nächste Artikel setzt sie ein: Er beweist
mit der partiellen Integration mit Rand, dass das Newtonpotential die Poisson-Gleichung löst, und zerlegt jedes Vektorfeld in
ein Gradienten- und ein Rotationsfeld — den Hauptsatz der Vektoranalysis.

:::kern
- __Partielle Integration im Raum__: Ohne Rand wandert die Ableitung mit Minuszeichen vom Feld auf die Gewichtung — ein Faktor braucht kompakten Träger.
- Der Rand kommt über die Indikatorfunktion ins Spiel: Ihr Gefälle sitzt an der Wand und zeigt nach innen, formal $\nabla\mathbf 1_V\,d^3x\sim-d\vec S$.
- __Satz von Gauß__: $\int_V\operatorname{div}\vec F\,d^3x=\int_{\partial V}\vec F\cdot d\vec S$ mit der äußeren Normale — Quellen gleich Ausfluss.
- Beweis für Normalbereiche: Fubini und Hauptsatz geben Deckel minus Boden; die Seitenwände tragen nichts bei; Schnittflächen heben sich weg.
- __Divergenz als Quelldichte__: Ausfluss aus einer winzigen Kugel geteilt durch ihr Volumen.
- __Gaußsches Gesetz__: Der Fluss des elektrischen Felds durch eine Hülle ist die eingeschlossene Ladung durch $\varepsilon_0$.
- Für eine Punktladung ist der Fluss durch jede umschließende Hülle derselbe; man schneidet die Ladung mit einer kleinen Kugel heraus.
- __Partielle Integration mit Rand__: Es kommt der Randterm $\int_{\partial V}\psi\,\vec G\cdot d\vec S$ hinzu.
- __Greensche Formeln__: mit $\vec G=\nabla u$ die erste, durch Vertauschen und Abziehen die symmetrische zweite.
:::

:::quiz
F: Was ist die Grundidee des Satzes von Gauß im Bild des Gebäudes?
A: Eine Bilanz: Jedes Zimmer bilanziert seine Gebläse gegen den Luftstrom durch seine Wände. Durch jede Innentür zählt der Strom einmal als Aus- und einmal als Einfluss, in der Summe hebt er sich weg; übrig bleibt der Strom durch die Außenwände. Deshalb ist das Integral der Divergenz über den Körper der Fluss durch seine Oberfläche.
F: Warum gilt die partielle Integration im Ganzraum, und wozu braucht sie einen kompakten Träger?
A: Nach der Produktregel ist $\partial_k(fg)=(\partial_kf)g+f\,\partial_kg$. Integriert man zuerst über $x_k$, gibt der Hauptsatz die Werte von $fg$ an den Enden einer langen Strecke — die sind null, weil einer der Faktoren außerhalb einer Kugel verschwindet. Für Vektorfelder folgt mit $\operatorname{div}(\psi\vec G)=\nabla\psi\cdot\vec G+\psi\operatorname{div}\vec G$ die Formel $\int(\operatorname{div}\vec G)\psi=-\int\vec G\cdot\nabla\psi$; am Ortsvektorfeld mit der Gewichtung $(1-r^2)^2$ geben beide Seiten $\frac{32\pi}{35}$.
F: Wie bringt die Indikatorfunktion den Rand ins Spiel, und was macht die Böschung daraus?
A: $\mathbf 1_V$ springt am Rand und ist nicht stetig; ihr Gefälle sitzt ganz an der Wand und zeigt nach innen, formal $\nabla\mathbf 1_V\,d^3x\sim-d\vec S$. Ersetzt man die Wand durch eine Böschung der Breite $\delta$, ist dort der Gradient etwa $-\frac1\delta\vec n$, und $-\int\vec G\cdot\nabla\psi_\delta$ wird für $\delta\to0$ zum Fluss $\int\vec G\cdot\vec n\,d\sigma$.
F: Wie beweist man den Satz von Gauß für einen Normalbereich?
A: Für die dritte Komponente geben Fubini und der Hauptsatz das Integral von $F_3$ am Deckel minus am Boden. Dieselbe Zahl ist der Fluss von $(0,0,F_3)$: Auf der Seitenwand ist die Normale waagerecht, am Deckel zeigt das Kreuzprodukt der Graphen-Parametrisierung nach oben, am Boden kommt es mit Minuszeichen. Mit allen drei Richtungen folgt der Satz; allgemeine Körper zerlegt man, und die Schnittflächen heben sich weg.
F: Warum muss die Normale im Satz von Gauß die äußere sein?
A: Die rechte Seite zählt den Ausfluss positiv; nur so entspricht sie der Summe der Quellen. Mit der inneren Normale wechselt jeder Fluss das Vorzeichen, und der Satz gilt nur noch mit Minuszeichen — im Normalbereich-Beweis ist die äußere Normale genau die, die am Deckel nach oben und am Boden nach unten zeigt.
F: Was ergeben beide Seiten des Satzes für das Ortsvektorfeld in der Kugel und für $(x^2,y^2,z^2)$ im Einheitswürfel?
A: Für $\vec x$ ist die Divergenz $3$, das Integral über die Kugel $4\pi R^3$; auf der Kugel ist die Normalkomponente $R$, der Fluss $R\cdot4\pi R^2$, also auch $4\pi R^3$. Für $(x^2,y^2,z^2)$ ist die Divergenz $2(x+y+z)$ mit dem Integral $3$, und der Fluss kommt mit je $1$ aus den drei Seiten an der Ecke $(1,1,1)$.
F: Warum ist die Divergenz die Quelldichte, und wie zeigt das ein kleiner Würfel?
A: Nach Gauß ist der Ausfluss aus einer winzigen Kugel das Integral der Divergenz, geteilt durch das Volumen ein Mittelwert, der wegen der Stetigkeit gegen den Wert im Mittelpunkt strebt. Für $(x^2,y,0)$ am Punkt $(1,0,0)$ fließen aus einem Würfel der Kante $h$ netto $2h\cdot h^2$ in $x$- und $h\cdot h^2$ in $y$-Richtung, zusammen $3h^3$ — Fluss pro Volumen $3$, die Divergenz $2x+1$ dort.
F: Wie folgt das Gaußsche Gesetz der Elektrostatik aus dem Satz?
A: Mit der Maxwell-Gleichung $\operatorname{div}\vec E=\frac{\rho}{\varepsilon_0}$ ist die linke Seite des Satzes das Integral der Ladungsdichte durch $\varepsilon_0$, also die eingeschlossene Ladung durch $\varepsilon_0$. Der Fluss durch eine geschlossene Hülle misst die Ladung darin.
F: Warum ist der Fluss einer Punktladung durch jede umschließende Hülle $Q$, und was ergibt sich für Würfel und Kugel daneben?
A: Man schneidet eine kleine Kugel um die Ladung heraus; auf dem Rest ist das Feld quellenfrei, also ist der Fluss durch die Hülle gleich dem durch die kleine Kugel, nämlich $Q$. Im Würfel $[-1,1]^3$ fließt aus Symmetrie durch jede Seite $\frac Q6$. Durch eine Kugel, die die Ladung nicht enthält, ist der Fluss null — was einströmt, strömt wieder hinaus.
F: Wie entstehen die partielle Integration mit Rand und die Greenschen Formeln, und wie prüft man sie an $u=r^2$?
A: Gauß auf $\psi\vec G$ mit der Produktregel gibt $\int_V\vec G\cdot\nabla\psi=\int_{\partial V}\psi\,\vec G\cdot d\vec S-\int_V(\operatorname{div}\vec G)\psi$; mit $\vec G=\nabla u$ die erste Greensche Formel, durch Vertauschen und Abziehen die zweite. Auf der Einheitskugel ist $\Delta(r^2)=6$ und die Normalableitung $2$: Mit der Gewichtung $1$ heben sich $8\pi$ und $8\pi$ auf, mit der Gewichtung $u$ geben beide Seiten $\frac{16\pi}{5}$.
:::
