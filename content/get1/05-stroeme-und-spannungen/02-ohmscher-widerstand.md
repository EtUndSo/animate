---
title: Der ohmsche Widerstand und das Ohmsche Gesetz
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50200
summary: Warum ein Leiter dem Strom überhaupt etwas entgegensetzt, wie das Ohmsche Gesetz Spannung, Strom und Widerstand verknüpft, woran der Widerstand baulich liegt und wo die schöne Geradlinigkeit endet.
tags: ohmscher Widerstand, Ohmsches Gesetz, spezifischer Widerstand, Leitwert, Kennlinie, Temperaturabhängigkeit
---

:::konzept
Wir wissen schon: Eine Spannung treibt Ladungen an, es fließt ein Strom. Aber wie viel Strom? Das hängt davon
ab, wie stark sich der Leiter dagegen sperrt — das ist der **Widerstand**. Je größer er ist, desto weniger
Strom bei gegebener Spannung. Das Bild dazu ist ein Wasserrohr: Ein enges, langes Rohr lässt bei gleichem Druck
weniger Wasser durch als ein kurzes, weites. Der Zusammenhang zwischen Druck (Spannung), Durchfluss (Strom) und
Enge (Widerstand) ist das **Ohmsche Gesetz**.
:::

**Worum es geht:** Im Strom-Artikel ging es darum, *was* fließt. Jetzt kommt das Gesetz, das festlegt, *wie
viel* fließt. Wir verknüpfen Spannung, Strom und __Widerstand__, klären, woran der Widerstand baulich liegt,
und schauen, wo der einfache lineare Zusammenhang gilt — und wo nicht.

## Das Ohmsche Gesetz

Für viele Leiter — vor allem Metalle bei konstanter Temperatur — ist der Strom der angelegten Spannung direkt
proportional. Das Verhältnis aus beiden ist eine feste Materialgröße, der __elektrische Widerstand__:

$$R = \frac{U}{I} \qquad\Longleftrightarrow\qquad U = R \cdot I.$$

- __$R$__: der __Widerstand__, Einheit __Ohm__ ($\Omega$).
- __$U$__: die am Bauteil anliegende __Spannung__, in Volt.
- __$I$__: der hindurchfließende __Strom__, in Ampere.

Aus der Definition folgt die Einheit $1\,\Omega = 1\,\tfrac{\text{V}}{\text{A}}$: Ein Ohm ist der Widerstand,
durch den bei einem Volt gerade ein Ampere fließt. Den Kehrwert nennt man __Leitwert__ $G = \tfrac{1}{R}$ mit
der Einheit __Siemens__ ($1\,\text{S} = 1\,\Omega^{-1}$) — er sagt, wie *gut* statt wie *schlecht* ein Bauteil
leitet.

**Anders betrachtet.** Das Ohmsche Gesetz lässt sich aus drei Blickwinkeln lesen, je nachdem, was man sucht:
$U = R\,I$ (welche Spannung fällt ab?), $I = U/R$ (welcher Strom fließt?) und $R = U/I$ (welchen Widerstand hat
das Bauteil?). Es ist dieselbe Beziehung, nur nach verschiedenen Größen aufgelöst.

:::grafik
Ein Widerstand im Stromkreis: Spannungsquelle $U$, durch den Widerstand fließt der Strom $I$. Daneben das
Wasserbild — ein enges Rohr, durch das bei gegebenem Druck nur ein dünner Strahl passt. Beschriftung
$U = R\cdot I$.
:::

## Woran der Widerstand liegt: R = ρ·l/A

Der Widerstand eines Drahtes ist keine Zauberzahl, sondern folgt aus Material und Form:

$$R = \rho \cdot \frac{l}{A}.$$

- __$R$__: der __Widerstand__ des Leiterstücks.
- __$\rho$__: der __spezifische Widerstand__ (Materialkonstante), in $\Omega\cdot\text{mm}^2/\text{m}$ — groß für
  schlechte Leiter, klein für gute wie Kupfer oder Silber.
- __$l$__: die __Länge__ des Leiters in Stromrichtung.
- __$A$__: die __Querschnittsfläche__ des Leiters.

Zwei anschauliche Aussagen stecken darin. Ein **längerer** Leiter hat mehr Widerstand, weil die Ladungsträger
auf ihrem Weg öfter mit dem Gitter zusammenstoßen — $l$ steht im Zähler. Ein **dickerer** Leiter hat weniger
Widerstand, weil sich der Strom auf mehr Fläche verteilt — $A$ steht im Nenner. Das ist exakt das Rohrbild:
lang und dünn sperrt, kurz und dick lässt durch.

Der Kehrwert von $\rho$ ist die __Leitfähigkeit__ $\kappa = 1/\rho$; damit schreibt sich dasselbe als
$R = \tfrac{l}{\kappa A}$. Mikroskopisch ist der Widerstand die Folge der **Stöße** der driftenden Elektronen
mit den schwingenden Atomrümpfen — bei jedem Stoß geben sie Bewegungsenergie ab, die als Wärme im Leiter
erscheint.

:::grafik
Zwei Leiterstücke im Vergleich: oben lang und dünn (viele eingezeichnete Stöße der Elektronen am Gitter, hoher
Widerstand), unten kurz und dick (wenige Stöße, breiter Querschnitt, niedriger Widerstand). Formel $R=\rho\,l/A$
mit markiertem $l$ und $A$.
:::

## Kennlinie: lineare und nichtlineare Zweipole

Trägt man den Strom $I$ über der Spannung $U$ auf, erhält man die __Kennlinie__ eines Bauteils (eines
__Zweipols__, also eines Bauteils mit zwei Anschlüssen). Beim idealen ohmschen Widerstand ist sie eine
**Gerade durch den Ursprung** — doppelte Spannung, doppelter Strom. Ihre Steigung ist gerade der Leitwert
$G = I/U$, ihre Umkehrung der Widerstand. Solche Bauteile heißen __lineare Zweipole__.

Doch das Ohmsche Gesetz ist kein Naturgesetz für alle Stoffe, sondern die Beschreibung eines **Spezialfalls**.
Viele Bauteile sind __nichtlinear__: Bei ihnen ist $R = U/I$ nicht konstant, die Kennlinie krümmt sich. Eine
Glühlampe bekommt bei mehr Strom einen höheren Widerstand (der Draht wird heiß), eine __Diode__ sperrt in eine
Richtung fast ganz und leitet in die andere erst ab einer Schwellspannung. Für solche Bauteile rechnet man mit
der Kennlinie selbst statt mit einem festen $R$.

:::grafik
Ein $U$-$I$-Diagramm mit drei Kennlinien: eine Gerade durch den Ursprung (ohmscher Widerstand, Steigung $=G$),
eine nach oben abknickende Kurve (Glühlampe) und eine Diodenkennlinie (lange flach, dann steil ansteigend).
Beschriftung „linear" bzw. „nichtlinear".
:::

## Temperaturabhängigkeit

Auch ein „ohmscher" Widerstand ist nur bei **konstanter Temperatur** wirklich konstant. Erwärmt sich ein
Metall, schwingen seine Atomrümpfe heftiger, die driftenden Elektronen stoßen häufiger — der Widerstand
**steigt**. Näherungsweise linear beschreibt das

$$R(\vartheta) = R_0\,\bigl(1 + \alpha \cdot \Delta\vartheta\bigr).$$

- __$R_0$__: der __Widerstand__ bei der Bezugstemperatur (meist $20\,^\circ\text{C}$).
- __$\alpha$__: der __Temperaturkoeffizient__ des Materials (für Metalle positiv).
- __$\Delta\vartheta$__: die __Temperaturänderung__ gegenüber der Bezugstemperatur.

Das erklärt die abknickende Kennlinie der Glühlampe: Mit steigendem Strom wird der Draht heißer, $R$ wächst,
und der Strom steigt langsamer als die Spannung. Bei manchen Materialien (Halbleitern) ist $\alpha$ sogar
negativ — dort sinkt der Widerstand mit der Temperatur.

:::kern
Das __Ohmsche Gesetz__ $U = R\,I$ verknüpft Spannung, Strom und __Widerstand__ ($1\,\Omega = 1\,\text{V}/\text{A}$);
der Kehrwert ist der __Leitwert__ $G = 1/R$ in Siemens. Baulich gilt $R = \rho\,l/A$: lang und dünn sperrt, kurz
und dick leitet, bestimmt vom __spezifischen Widerstand__ $\rho$ des Materials. In der __Kennlinie__ ist ein
__linearer (ohmscher) Zweipol__ eine Ursprungsgerade; __nichtlineare__ Bauteile (Diode, Glühlampe) krümmen sie.
Und weil Stöße am Gitter den Widerstand verursachen, steigt er bei Metallen mit der Temperatur:
$R(\vartheta) = R_0(1 + \alpha\,\Delta\vartheta)$.
:::

Mit Strom, Spannung und Widerstand sind die drei Grundgrößen beisammen. Bevor man ganze Netzwerke berechnet,
braucht man aber eine saubere Vorzeichen-Vereinbarung — die __Zählpfeile__.
