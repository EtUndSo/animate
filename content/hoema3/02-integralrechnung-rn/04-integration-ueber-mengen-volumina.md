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
