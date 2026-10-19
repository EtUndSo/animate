---
title: Integration über Mengen und das Cavalieri-Prinzip
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020400
summary: Von Grund auf – wie man eine Funktion über ein beliebig geformtes Gebiet (nicht nur über Quader) integriert, indem man sie außerhalb durch null fortsetzt. Das Volumen einer Menge ist das Integral der Eins, $\mathrm{vol}(M)=\int_M 1\,dx$, und das Cavalieri-Prinzip berechnet Volumina als Integral der Querschnittsflächen $\mathrm{vol}(K)=\int_0^H A(z)\,dz$ – von Kegel bis Kugel.
tags: Integration über Mengen, Fortsetzung durch null, Volumen, Cavalieri-Prinzip, Querschnittsfläche, Rotationskörper, Nullmenge
---

:::grafik
Einstiegs-Animation: Ein krummes Gebiet $M$ (z. B. eine Kreisscheibe) in einen Quader $Q$ eingebettet; die
Funktion $f$ wird außerhalb von $M$ auf **null** gesetzt (die Fläche „fällt dort auf den Boden"), und man
integriert über den ganzen Quader. Daneben das Cavalieri-Bild: Ein Körper $K$ wird in dünne waagerechte
**Scheiben** der Dicke $h$ geschnitten; jede hat die Querschnittsfläche $A(z)$, und ihr Volumen $A(z)\,h$ wird
aufgestapelt. Im Grenzwert $h\to0$ wird daraus $\mathrm{vol}(K)=\int_0^H A(z)\,dz$. Kernbotschaft: Über beliebige
Gebiete integriert man durch „Auffüllen mit null", und Volumina baut man aus Querschnittsflächen.
:::

:::konzept
Bisher integrierten wir über **Quader** — aber reale Gebiete sind Kreise, Kugeln, Dreiecke, Zylinder. Zwei Ideen
machen das handhabbar. Erstens: Man setzt die Funktion außerhalb des Gebiets einfach **auf null fort** und
integriert über einen umgebenden Quader — was außerhalb liegt, trägt dann nichts bei. Zweitens, für Volumina: Das
**Volumen** einer Menge ist nichts anderes als das Integral der konstanten Funktion $1$ darüber, und man kann es
nach dem __Cavalieri-Prinzip__ aus den **Querschnittsflächen** aufbauen — die klassische „Scheiben"-Methode, mit
der schon Kegel- und Kugelvolumen fallen.
:::

**Worum es geht:** Wir erklären die __Integration über eine Menge__ (Fortsetzung durch null), definieren das
__Volumen__ $\mathrm{vol}(M)=\int_M 1\,dx$ und leiten das __Cavalieri-Prinzip__ her, mit dem wir Kegel- und
Kugelvolumen berechnen.

## Integration über ein beliebiges Gebiet

Sei $M\subset\mathbb{R}^n$ abgeschlossen und beschränkt und $f:M\to\mathbb{R}$ stetig. Um $f$ zu integrieren,
führt man den Fall auf einen umgebenden Quader $Q\supset M$ zurück, indem man $f$ **durch null fortsetzt**:

$$\bar f(x) = \begin{cases} f(x), & x\in M,\\ 0, & x\in Q\setminus M,\end{cases} \qquad \int_M f(x)\,dx := \int_Q \bar f(x)\,dx.$$

Anschaulich: Außerhalb von $M$ „liegt die Funktion flach am Boden", trägt also nichts zum Integral bei; der Quader
ist nur ein bequemer Rahmen. **Stolperstein:** Die fortgesetzte Funktion $\bar f$ ist am Rand von $M$ im
Allgemeinen **nicht stetig** (sie springt dort auf null). Dass das Integral trotzdem wohldefiniert ist, sichert
für abgeschlossene, beschränkte $M$ die (hier nicht vertiefte) **Lebesgue-Integrationstheorie** — der Rand ist
eine „Nullmenge" und verdirbt nichts. Für die **praktische** Berechnung nutzt man ohnehin andere Werkzeuge:
Koordinatentransformationen (Kapitel 4) oder die Zerlegung in __Normalbereiche__ (nächster Artikel), über die man
„scheibchenweise" integriert.

## Das Volumen einer Menge

Setzt man speziell $f\equiv 1$, so misst das Integral schlicht, wie „groß" das Gebiet ist — das ist die Definition
des **Volumens** (in 2D: des Flächeninhalts):

$$\mathrm{vol}(M) = \int_M 1\,dx.$$

Das verallgemeinert die vertraute Idee „Fläche = Integral über 1" auf beliebige Dimension. Für einen Quader
$Q=[a_1,b_1]\times\cdots\times[a_n,b_n]$ kommt erwartungsgemäß $\mathrm{vol}(Q)=(b_1-a_1)\cdots(b_n-a_n)$ heraus.

## Das Cavalieri-Prinzip

Für Körper im $\mathbb{R}^3$ gibt es eine besonders anschauliche Methode. Ein Körper $K$ sei als Stapel von
**Querschnitten** gegeben,

$$K = \{(x,y,z)\in\mathbb{R}^3 : (x,y)\in D(z),\ 0\le z\le H\},$$

wobei die Schnittfläche $D(z)\subset\mathbb{R}^2$ den Flächeninhalt $A(z)=|D(z)|$ hat (stetig in $z$). Man nähert
das Volumen durch dünne Scheiben der Dicke $h=H/N$: Jede Scheibe bei Höhe $z_k$ hat näherungsweise das Volumen
$A(z_k)\,h$, also

$$\mathrm{vol}(K) \approx h\sum_{k=1}^{N} A(z_k).$$

Das ist eine **Riemann-Summe** für $A(z)$ — im Grenzwert $h\to 0$ (unabhängig von der Wahl der Zwischenstellen
$z_k$) wird daraus das __Cavalieri-Prinzip__:

$$\boxed{\ \mathrm{vol}(K) = \int_0^H A(z)\,dz.\ }$$

In Worten: **Das Volumen ist das Integral der Querschnittsflächen.** Zwei Körper mit in jeder Höhe gleicher
Querschnittsfläche haben dasselbe Volumen — ganz gleich, wie „schief" sie aussehen (das ist die ursprüngliche
Aussage Cavalieris).

:::grafik
Ein Körper $K$, in Scheiben der Dicke $h$ zerlegt; eine Scheibe bei $z_k$ mit Querschnitt $D(z_k)$ und Fläche
$A(z_k)$ hervorgehoben, Volumen $\approx A(z_k)h$. Danebenstehend die Riemann-Summe $h\sum A(z_k)$ und ihr
Grenzwert $\int_0^H A(z)\,dz$. Rechts zwei verschieden „schiefe" Körper mit gleichen Querschnittsflächen und
gleichem Volumen (Cavalieri).
:::

**Beispiel Kegel.** Ein Kegel mit Grundradius $R$ und Höhe $H$, auf die Spitze gestellt, hat in Höhe $z$ einen
Kreis vom Radius $\tfrac{zR}{H}$, also $A(z)=\pi\big(\tfrac{zR}{H}\big)^2 = \pi\tfrac{R^2}{H^2}z^2$. Integrieren:

$$\mathrm{vol} = \int_0^H \pi\frac{R^2}{H^2}z^2\,dz = \pi\frac{R^2}{H^2}\cdot\frac{H^3}{3} = \frac{\pi}{3}R^2 H.$$

**Beispiel Kugel** (eigenes Beispiel). Eine Kugel vom Radius $R$ hat in Höhe $z\in[-R,R]$ einen Kreis vom Radius
$\sqrt{R^2-z^2}$, also $A(z)=\pi(R^2-z^2)$. Damit

$$\mathrm{vol} = \int_{-R}^{R}\pi(R^2-z^2)\,dz = \pi\Big[R^2 z - \tfrac{z^3}{3}\Big]_{-R}^{R} = \pi\Big(2R^3 - \tfrac{2R^3}{3}\Big) = \frac{4}{3}\pi R^3.$$

Beide klassischen Formeln fallen mit dem Cavalieri-Prinzip in zwei Zeilen heraus.

:::grafik
Links der auf die Spitze gestellte Kegel mit Kreisquerschnitt vom Radius $zR/H$ in Höhe $z$; rechts die Kugel mit
Kreisquerschnitt vom Radius $\sqrt{R^2-z^2}$. Darunter je die Flächenfunktion $A(z)$ und das Ergebnis
$\tfrac{\pi}{3}R^2H$ bzw. $\tfrac{4}{3}\pi R^3$.
:::

:::kern
Über ein abgeschlossenes, beschränktes Gebiet $M\subset\mathbb{R}^n$ integriert man eine stetige Funktion, indem
man sie außerhalb durch **null fortsetzt** und über einen umgebenden Quader integriert: $\int_M f:=\int_Q \bar f$
(wohldefiniert via Lebesgue; der Rand ist eine Nullmenge; praktisch rechnet man mit Normalbereichen/Transformation).
Das __Volumen__ ist $\mathrm{vol}(M)=\int_M 1\,dx$. Das __Cavalieri-Prinzip__ baut Volumina aus Querschnittsflächen:
für $K$ mit Schnittfläche $A(z)$ ist $\mathrm{vol}(K)=\int_0^H A(z)\,dz$ (Grenzwert der Scheiben-Riemann-Summe
$h\sum A(z_k)$). Damit sofort: Kegel $\tfrac{\pi}{3}R^2H$ (mit $A(z)=\pi(zR/H)^2$) und Kugel $\tfrac{4}{3}\pi R^3$
(mit $A(z)=\pi(R^2-z^2)$).
:::

Das Cavalieri-Prinzip zerlegt einen Körper in Scheiben senkrecht zu **einer** Achse. Systematisch verallgemeinert
wird das durch die __Normalbereiche__: Gebiete, bei denen eine Koordinate zwischen zwei Funktionen der anderen
eingeschlossen ist. Über sie integriert man direkt per iteriertem Integral mit variablen Grenzen — das Thema des
nächsten Artikels.

:::quiz
F: Wie integriert man eine Funktion über ein krummes Gebiet $M$, und warum funktioniert die „Fortsetzung durch null"?
A: Man bettet $M$ in einen Quader $Q$ ein und setzt $f$ außerhalb $M$ auf $0$ ($\bar f$), dann $\int_M f:=\int_Q\bar f$. Weil $\bar f$ außerhalb $M$ verschwindet, trägt der Bereich $Q\setminus M$ nichts bei — der Quader ist nur ein bequemer Rahmen.
F: Warum ist die fortgesetzte Funktion $\bar f$ am Rand von $M$ im Allgemeinen unstetig, und warum stört das nicht?
A: Am Rand springt $\bar f$ vom Funktionswert auf $0$. Der Rand eines (gutartigen) Gebiets ist jedoch eine **Nullmenge** — er hat Volumen $0$ und trägt zum Integral nichts bei; die Lebesgue-Theorie sichert dadurch die Wohldefiniertheit.
F: Warum ist $\mathrm{vol}(M)=\int_M 1\,dx$ eine sinnvolle Definition des Volumens?
A: Integriert man die konstante Funktion $1$, summiert man gerade „Einheitsvolumen pro Punkt" über $M$ — das misst, wie groß $M$ ist. Das verallgemeinert die vertraute Idee „Fläche $=\int 1$" auf jede Dimension (beim Quader kommt das Produkt der Kantenlängen heraus).
F: Was besagt das Cavalieri-Prinzip, und wie entsteht das Integral $\int_0^H A(z)\,dz$ aus Scheiben?
A: Das Volumen ist das Integral der Querschnittsflächen: $\mathrm{vol}(K)=\int_0^H A(z)\,dz$. Man zerlegt den Körper in dünne Scheiben der Dicke $h$ mit Volumen $\approx A(z_k)h$; die Summe $h\sum A(z_k)$ ist eine Riemann-Summe, die für $h\to0$ gegen das Integral strebt.
F: Was ist die ursprüngliche (geometrische) Aussage Cavalieris?
A: Zwei Körper, die in **jeder** Höhe dieselbe Querschnittsfläche haben, besitzen dasselbe Volumen — ganz gleich, wie „schief" oder verschoben sie aussehen. Nur die Flächenfunktion $A(z)$ zählt, nicht die Form der Scheiben.
F: Warum ist beim Kegel $A(z)=\pi(zR/H)^2$, und wie folgt daraus $\frac{\pi}{3}R^2H$?
A: Auf die Spitze gestellt wächst der Radius linear mit der Höhe, $r(z)=zR/H$, also $A(z)=\pi r(z)^2=\pi\frac{R^2}{H^2}z^2$. Integration liefert $\int_0^H$ von $z^2$ gleich $H^3/3$, also $\mathrm{vol}=\pi\frac{R^2}{H^2}\cdot\frac{H^3}{3}=\frac{\pi}{3}R^2H$.
F: Warum hat der Kugelquerschnitt in Höhe $z$ die Fläche $A(z)=\pi(R^2-z^2)$?
A: Der Schnitt einer Kugel vom Radius $R$ in Höhe $z$ ist ein Kreis; sein Radius ist nach Pythagoras $\sqrt{R^2-z^2}$. Also $A(z)=\pi(\sqrt{R^2-z^2})^2=\pi(R^2-z^2)$ — null an den Polen ($z=\pm R$), maximal am Äquator.
F: Inwiefern ist das Cavalieri-Prinzip nur ein Spezialfall des Satzes von Fubini?
A: Das Volumenintegral $\int_K 1\,dV$ ist ein Dreifachintegral. Integriert man nach Fubini zuerst über den Querschnitt $(x,y)\in D(z)$, erhält man $\int_{D(z)}1\,dx\,dy=A(z)$, und das äußere Integral über $z$ ergibt $\int_0^H A(z)\,dz$ — genau Cavalieri.
F: Warum rechnet man in der Praxis selten direkt mit der „Fortsetzung durch null"?
A: Die unstetige Fortsetzung ist zum konkreten Ausrechnen unhandlich. Praktisch zerlegt man das Gebiet in **Normalbereiche** (variable Integrationsgrenzen) oder nutzt **Koordinatentransformationen** — beides vermeidet den springenden Rand.
F: Welche Rolle spielt die Stetigkeit der Querschnittsfläche $A(z)$ für das Cavalieri-Integral?
A: Sie sichert, dass $A$ Riemann-integrierbar ist, sodass die Scheiben-Riemann-Summe $h\sum A(z_k)$ unabhängig von den Zwischenstellen gegen $\int_0^H A(z)\,dz$ konvergiert. Ohne eine solche Regularität wäre der Grenzwert nicht garantiert.
:::
