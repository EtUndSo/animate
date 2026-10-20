---
title: Integration über Mengen und das Cavalieri-Prinzip
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020400
summary: Von Grund auf – wie man eine Funktion über ein beliebig geformtes Gebiet integriert, indem man sie außerhalb durch null fortsetzt. Das Volumen einer Menge ist das Integral der Eins, $\mathrm{vol}(M)=\int_M 1\,dx$, und das Cavalieri-Prinzip berechnet Volumina als Integral der Querschnittsflächen $\mathrm{vol}(K)=\int_0^H A(z)\,dz$ – von Kegel bis Kugel.
tags: Integration über Mengen, Fortsetzung durch null, Volumen, Cavalieri-Prinzip, Querschnittsfläche, Rotationskörper, Nullmenge
---

## Anschaulich

Bisher integrierten wir über **Quader** — aber reale Gebiete sind Kreise, Kugeln, Dreiecke, Zylinder. Wie
integriert man über so etwas?

Der erste Trick: Man bettet das krumme Gebiet $M$ in einen umgebenden Quader ein und setzt die Funktion außerhalb
von $M$ einfach **auf null**. Was außerhalb liegt, trägt dann nichts bei — man integriert bequem über den ganzen
Quader.

Der zweite Gedanke betrifft **Volumina**: Das Volumen einer Menge ist einfach das Integral der konstanten Funktion
$1$ darüber. Und man baut es nach dem __Cavalieri-Prinzip__ aus **Querschnittsflächen** auf — man schneidet den
Körper in dünne Scheiben und stapelt sie.

Mit dieser „Scheiben"-Methode fallen schon Kegel- und Kugelvolumen in wenigen Zeilen.

:::grafik
Szene: hoema3/integralrechnung-rn/04-fortsetzung-und-scheiben · Vorlage: gebiet-null-und-cavalieri-3d
Links ein krummes Gebiet $M$ (Kreisscheibe) in einem Quader $Q$; die Funktion $f$ wird außerhalb $M$ auf null
gesetzt (fällt „auf den Boden"). Rechts das Cavalieri-Bild: ein Körper $K$ in dünne waagerechte Scheiben der
Dicke $h$ zerlegt, jede mit Querschnittsfläche $A(z)$ und Volumen $A(z)\,h$; im Grenzwert $h\to0$ wird daraus
$\int_0^H A(z)\,dz$. (Rot = $f$ bzw. Körper, orange = eine Scheibe, grau = Quader.)
:::

## Integration über ein beliebiges Gebiet

Sei $M\subset\mathbb{R}^n$ abgeschlossen und beschränkt und $f:M\to\mathbb{R}$ stetig. Man führt den Fall auf
einen umgebenden Quader $Q\supset M$ zurück, indem man $f$ **durch null fortsetzt**:

:::formel Definition
$$\bar f(x) = \begin{cases} f(x), & x\in M,\\ 0, & x\in Q\setminus M,\end{cases} \qquad \int_M f(x)\,dx := \int_Q \bar f(x)\,dx.$$
:::

Dabei ist $\bar f$ die auf den ganzen Quader fortgesetzte Funktion. Außerhalb von $M$ „liegt sie flach am Boden",
trägt also nichts bei; der Quader ist nur ein bequemer Rahmen.

**Stolperstein:** Die fortgesetzte Funktion $\bar f$ ist am Rand von $M$ im Allgemeinen **nicht stetig** — sie
springt dort auf null. Dass das Integral trotzdem wohldefiniert ist, sichert für abgeschlossene, beschränkte $M$
die (hier nicht vertiefte) **Lebesgue-Theorie**: Der Rand ist eine „Nullmenge" (Volumen $0$) und verdirbt nichts.

Für die **praktische** Berechnung nutzt man ohnehin andere Werkzeuge: Koordinatentransformationen (Kapitel 4) oder
die Zerlegung in __Normalbereiche__ (nächster Artikel).

## Das Volumen einer Menge

Setzt man speziell $f\equiv1$, misst das Integral schlicht, wie „groß" das Gebiet ist — das ist die Definition des
**Volumens** (in 2D: des Flächeninhalts):

$$\mathrm{vol}(M) = \int_M 1\,dx.$$

Das verallgemeinert die vertraute Idee „Fläche = Integral über 1" auf jede Dimension. Für einen Quader kommt
erwartungsgemäß $\mathrm{vol}(Q)=(b_1-a_1)\cdots(b_n-a_n)$ heraus.

## Das Cavalieri-Prinzip

Für Körper im $\mathbb{R}^3$ gibt es eine besonders anschauliche Methode. Ein Körper $K$ sei als Stapel von
**Querschnitten** gegeben: In Höhe $z$ (mit $0\le z\le H$) ist der Schnitt eine Fläche $D(z)\subset\mathbb{R}^2$
mit Flächeninhalt $A(z)=|D(z)|$ (stetig in $z$). Dann gilt:

:::formel Satz
$$\mathrm{vol}(K) = \int_0^H A(z)\,dz.$$
:::

Eingabe ist die Flächenfunktion $A(z)$ (eine Zahl pro Höhe), Ausgabe das Volumen (eine Zahl). In Worten: **Das
Volumen ist das Integral der Querschnittsflächen.**

:::herleitung
Man nähert das Volumen durch dünne Scheiben der Dicke $h=H/N$. Jede Scheibe bei Höhe $z_k$ hat näherungsweise das
Volumen $A(z_k)\,h$, also

$$\mathrm{vol}(K) \approx h\sum_{k=1}^{N} A(z_k).$$

Das ist eine **Riemann-Summe** für die Funktion $A$. Weil $A$ stetig (und damit Riemann-integrierbar) ist,
konvergiert sie für $h\to0$ unabhängig von der Wahl der Zwischenstellen $z_k$ gegen $\int_0^H A(z)\,dz$.
:::

:::herleitung
Cavalieri ist zugleich ein **Spezialfall von Fubini**. Das Volumen ist das Dreifachintegral $\int_K 1\,dV$.
Integriert man nach Fubini zuerst über den Querschnitt $(x,y)\in D(z)$, so ist das innere Integral gerade die
Fläche,

$$\int_{D(z)} 1\,dx\,dy = A(z),$$

und das äußere Integral über $z$ liefert $\int_0^H A(z)\,dz$.
:::

Daraus folgt die ursprüngliche Aussage Cavalieris: Zwei Körper mit in **jeder** Höhe gleicher Querschnittsfläche
haben dasselbe Volumen — ganz gleich, wie „schief" sie aussehen.

:::grafik
Szene: hoema3/integralrechnung-rn/04-cavalieri-schief · Vorlage: gleiche-querschnitte-3d
Zwei verschieden „schiefe" Körper mit in jeder Höhe gleicher Querschnittsfläche $A(z)$ und damit gleichem Volumen;
daneben die Scheibenzerlegung mit Riemann-Summe $h\sum A(z_k)\to\int_0^H A(z)\,dz$. (Rot = Körper, orange = eine
Scheibe, grau = Höhenachse $z$.)
:::

## Beispiele: Kegel und Kugel

**Kegel.** Ein Kegel mit Grundradius $R$ und Höhe $H$, auf die Spitze gestellt, hat in Höhe $z$ einen Kreis vom
Radius $zR/H$, also $A(z)=\pi\big(\tfrac{zR}{H}\big)^2=\pi\tfrac{R^2}{H^2}z^2$. Integrieren:

$$\mathrm{vol} = \int_0^H \pi\frac{R^2}{H^2}z^2\,dz = \pi\frac{R^2}{H^2}\cdot\frac{H^3}{3} = \frac{\pi}{3}R^2 H.$$

**Kugel.** Eine Kugel vom Radius $R$ hat in Höhe $z\in[-R,R]$ einen Kreis vom Radius $\sqrt{R^2-z^2}$ (Pythagoras),
also $A(z)=\pi(R^2-z^2)$. Damit

$$\mathrm{vol} = \int_{-R}^{R}\pi(R^2-z^2)\,dz = \pi\Big[R^2 z-\tfrac{z^3}{3}\Big]_{-R}^{R} = \pi\Big(2R^3-\tfrac{2R^3}{3}\Big) = \frac{4}{3}\pi R^3.$$

Beide klassischen Formeln fallen mit dem Cavalieri-Prinzip in zwei Zeilen heraus.

:::grafik
Szene: hoema3/integralrechnung-rn/04-kegel-kugel · Vorlage: rotationskoerper-querschnitt-3d
Links der auf die Spitze gestellte Kegel mit Kreisquerschnitt vom Radius $zR/H$ in Höhe $z$; rechts die Kugel mit
Kreisquerschnitt vom Radius $\sqrt{R^2-z^2}$. Darunter je die Flächenfunktion $A(z)$ und das Ergebnis
$\tfrac{\pi}{3}R^2H$ bzw. $\tfrac{4}{3}\pi R^3$. (Rot = Körper, orange = Querschnittskreis, grau = Achse.)
:::

## Bedeutung und Ausblick

Mit der Fortsetzung durch null ist das Integral über jedes vernünftige Gebiet erklärt, und mit Cavalieri rechnet
man Volumina bequem aus Querschnitten — die Grundlage für Masse, Ladung oder Schwerpunkt eines Körpers.

Das Cavalieri-Prinzip zerlegt einen Körper in Scheiben senkrecht zu **einer** Achse. Systematisch verallgemeinert
wird das durch die __Normalbereiche__: Gebiete, bei denen eine Koordinate zwischen zwei Funktionen der anderen
eingeschlossen ist. Über sie integriert man direkt per iteriertem Integral mit variablen Grenzen — das Thema des
nächsten Artikels.

:::kern
- Über ein abgeschlossenes, beschränktes Gebiet $M\subset\mathbb{R}^n$ integriert man eine stetige Funktion durch **Fortsetzung mit null**: $\int_M f:=\int_Q\bar f$ (wohldefiniert via Lebesgue; der Rand ist eine Nullmenge; praktisch rechnet man mit Normalbereichen/Transformation).
- Das __Volumen__ ist $\mathrm{vol}(M)=\int_M 1\,dx$ (Quader: Produkt der Kantenlängen).
- Das __Cavalieri-Prinzip__ baut Volumina aus Querschnittsflächen: $\mathrm{vol}(K)=\int_0^H A(z)\,dz$ (Grenzwert der Scheiben-Riemann-Summe $h\sum A(z_k)$; zugleich Fubini-Spezialfall).
- Zwei Körper mit in jeder Höhe gleicher Querschnittsfläche haben dasselbe Volumen (ursprüngliche Aussage Cavalieris).
- Sofort: Kegel $\tfrac{\pi}{3}R^2H$ (mit $A(z)=\pi(zR/H)^2$) und Kugel $\tfrac{4}{3}\pi R^3$ (mit $A(z)=\pi(R^2-z^2)$).
:::

:::quiz
F: Wie integriert man eine Funktion über ein krummes Gebiet $M$, und warum funktioniert die „Fortsetzung durch null"?
A: Man bettet $M$ in einen Quader $Q$ ein und setzt $f$ außerhalb $M$ auf $0$ ($\bar f$), dann $\int_M f:=\int_Q\bar f$. Weil $\bar f$ außerhalb $M$ verschwindet, trägt der Bereich $Q\setminus M$ nichts bei — der Quader ist nur ein bequemer Rahmen.
F: Warum ist die fortgesetzte Funktion $\bar f$ am Rand von $M$ im Allgemeinen unstetig, und warum stört das nicht?
A: Am Rand springt $\bar f$ vom Funktionswert auf $0$. Der Rand eines gutartigen Gebiets ist jedoch eine **Nullmenge** — er hat Volumen $0$ und trägt zum Integral nichts bei; die Lebesgue-Theorie sichert dadurch die Wohldefiniertheit.
F: Warum ist $\mathrm{vol}(M)=\int_M 1\,dx$ eine sinnvolle Definition des Volumens?
A: Integriert man die konstante Funktion $1$, summiert man gerade „Einheitsvolumen pro Punkt" über $M$ — das misst, wie groß $M$ ist. Das verallgemeinert „Fläche $=\int 1$" auf jede Dimension (beim Quader kommt das Produkt der Kantenlängen heraus).
F: Was besagt das Cavalieri-Prinzip, und wie entsteht das Integral $\int_0^H A(z)\,dz$ aus Scheiben?
A: Das Volumen ist das Integral der Querschnittsflächen: $\mathrm{vol}(K)=\int_0^H A(z)\,dz$. Man zerlegt den Körper in dünne Scheiben der Dicke $h$ mit Volumen $\approx A(z_k)h$; die Summe $h\sum A(z_k)$ ist eine Riemann-Summe, die für $h\to0$ gegen das Integral strebt.
F: Was ist die ursprüngliche (geometrische) Aussage Cavalieris?
A: Zwei Körper, die in **jeder** Höhe dieselbe Querschnittsfläche haben, besitzen dasselbe Volumen — ganz gleich, wie „schief" oder verschoben sie aussehen. Nur die Flächenfunktion $A(z)$ zählt, nicht die Form der Scheiben.
F: Warum ist beim Kegel $A(z)=\pi(zR/H)^2$, und wie folgt daraus $\frac{\pi}{3}R^2H$?
A: Auf die Spitze gestellt wächst der Radius linear mit der Höhe, $r(z)=zR/H$, also $A(z)=\pi r(z)^2=\pi\frac{R^2}{H^2}z^2$. Integration liefert $\int_0^H z^2\,dz=H^3/3$, also $\mathrm{vol}=\pi\frac{R^2}{H^2}\cdot\frac{H^3}{3}=\frac{\pi}{3}R^2H$.
F: Warum hat der Kugelquerschnitt in Höhe $z$ die Fläche $A(z)=\pi(R^2-z^2)$?
A: Der Schnitt einer Kugel vom Radius $R$ in Höhe $z$ ist ein Kreis; sein Radius ist nach Pythagoras $\sqrt{R^2-z^2}$. Also $A(z)=\pi(\sqrt{R^2-z^2})^2=\pi(R^2-z^2)$ — null an den Polen ($z=\pm R$), maximal am Äquator.
F: Inwiefern ist das Cavalieri-Prinzip nur ein Spezialfall des Satzes von Fubini?
A: Das Volumenintegral $\int_K 1\,dV$ ist ein Dreifachintegral. Integriert man nach Fubini zuerst über den Querschnitt $(x,y)\in D(z)$, erhält man $\int_{D(z)}1\,dx\,dy=A(z)$, und das äußere Integral über $z$ ergibt $\int_0^H A(z)\,dz$ — genau Cavalieri.
F: Warum rechnet man in der Praxis selten direkt mit der „Fortsetzung durch null"?
A: Die unstetige Fortsetzung ist zum konkreten Ausrechnen unhandlich. Praktisch zerlegt man das Gebiet in **Normalbereiche** (variable Integrationsgrenzen) oder nutzt **Koordinatentransformationen** — beides vermeidet den springenden Rand.
F: Welche Rolle spielt die Stetigkeit der Querschnittsfläche $A(z)$ für das Cavalieri-Integral?
A: Sie sichert, dass $A$ Riemann-integrierbar ist, sodass die Scheiben-Riemann-Summe $h\sum A(z_k)$ unabhängig von den Zwischenstellen gegen $\int_0^H A(z)\,dz$ konvergiert. Ohne eine solche Regularität wäre der Grenzwert nicht garantiert.
:::
