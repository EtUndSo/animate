---
title: Komplexe Zahlen und die komplexe Ebene
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Komplexe Zahlen und Zeiger
order: 10100
summary: Das mathematische Fundament der gesamten Signalverarbeitung – warum man die reellen Zahlen um die imaginäre Einheit erweitert, wie komplexe Zahlen als Punkte und Zeiger in der Ebene leben und warum die Exponentialform das Rechnen mit Schwingungen so einfach macht.
tags: komplexe Zahlen, imaginäre Einheit, komplexe Ebene, Betrag, Phase, Polarform, Eulersche Formel, Zeiger
---

:::konzept
Komplexe Zahlen wirken auf den ersten Blick wie eine mathematische Spielerei — eine „Zahl", deren Quadrat
negativ ist. Für die Elektrotechnik sind sie aber das perfekte Werkzeug, denn eine komplexe Zahl ist zugleich
ein **Pfeil in einer Ebene**, und das Multiplizieren solcher Pfeile bedeutet **Drehen und Strecken**. Genau das
brauchen wir, um Schwingungen und Wechselgrößen zu beschreiben: Aus mühsamer Sinus-Rechnerei wird einfache
Multiplikation. Dieses Kapitel legt dafür das Fundament.
:::

**Worum es geht:** „Mathematische Methoden der Elektrotechnik" beginnt mit dem Werkzeug, auf dem die ganze
Signalverarbeitung aufbaut. Wir führen die __komplexen Zahlen__ ein, verorten sie in der __komplexen Ebene__ und
arbeiten uns zur __Exponentialform__ vor — der Darstellung, die alles Weitere einfach macht.

## Die imaginäre Einheit und die kartesische Form

Die reellen Zahlen haben eine Lücke: Keine von ihnen löst $x^2 = -1$. Man schließt sie, indem man eine neue
Zahl einführt, die __imaginäre Einheit__. In der Mathematik heißt sie $i$, in der Elektrotechnik schreibt man
jedoch $j$, um Verwechslungen mit dem Strom $i$ zu vermeiden. Sie ist definiert durch

$$j^2 = -1.$$

Damit lässt sich jede __komplexe Zahl__ als Summe eines reellen und eines imaginären Anteils schreiben, die
__kartesische Form__:

$$z = a + j\,b.$$

- __$z$__: die __komplexe Zahl__.
- __$a = \operatorname{Re}(z)$__: der __Realteil__ (eine gewöhnliche reelle Zahl).
- __$b = \operatorname{Im}(z)$__: der __Imaginärteil__ (ebenfalls reell — er ist der Faktor **vor** $j$, nicht
  $jb$ selbst).

Gerechnet wird wie mit Klammern gewohnt, nur dass am Ende $j^2$ durch $-1$ ersetzt wird. Die __konjugiert
komplexe Zahl__ $z^* = a - j\,b$ (Imaginärteil mit umgekehrtem Vorzeichen) taucht dabei immer wieder auf — etwa,
weil $z\cdot z^* = a^2 + b^2$ reell ist.

## Die komplexe Ebene

Eine komplexe Zahl hat zwei unabhängige Anteile — also lässt sie sich als Punkt in einer **Ebene** zeichnen,
der __komplexen Ebene__ (auch Gaußsche Ebene). Die waagerechte Achse trägt den Realteil, die senkrechte den
Imaginärteil. Die Zahl $z = a + jb$ ist dann der Punkt mit den Koordinaten $(a, b)$ — oder, noch nützlicher, der
**Pfeil** vom Ursprung zu diesem Punkt.

Diese geometrische Sicht ist der ganze Trick: Addition komplexer Zahlen ist das Aneinanderhängen der Pfeile (wie
bei Vektoren), und die konjugiert komplexe Zahl $z^*$ ist die an der reellen Achse gespiegelte Zahl.

:::grafik
Die komplexe Ebene mit reeller Achse (waagerecht) und imaginärer Achse (senkrecht). Eine Zahl $z = a + jb$ ist
als Punkt $(a,b)$ und als Pfeil vom Ursprung eingezeichnet; gestrichelt die Projektionen auf beide Achsen
($a$, $b$). Zusätzlich die gespiegelte konjugierte Zahl $z^*$.
:::

## Betrag und Phase: die Polarform

Statt durch Real- und Imaginärteil lässt sich derselbe Pfeil auch durch seine **Länge** und seinen **Winkel**
beschreiben — die __Polarform__. Die Länge ist der __Betrag__, der Winkel gegen die reelle Achse die __Phase__
(das Argument):

$$|z| = \sqrt{a^2 + b^2}, \qquad \varphi = \arg(z).$$

- __$|z|$__: der __Betrag__ — der Abstand des Punktes vom Ursprung.
- __$\varphi$__: die __Phase__ — der Winkel des Pfeils gegen die positive reelle Achse.

Zwischen beiden Darstellungen vermitteln Sinus und Kosinus: Aus Betrag und Phase bekommt man die Anteile zurück
über $a = |z|\cos\varphi$ und $b = |z|\sin\varphi$, also

$$z = |z|\,(\cos\varphi + j\sin\varphi).$$

**Stolperstein: die Phase richtig bestimmen.** Man ist versucht, einfach $\varphi = \arctan(b/a)$ zu rechnen —
aber der Arkustangens liefert nur Winkel zwischen $-\tfrac{\pi}{2}$ und $+\tfrac{\pi}{2}$, deckt also nur die
rechte Halbebene ab. Liegt $z$ links (negativer Realteil), muss man $\pi$ addieren. Sicherer ist, den
**Quadranten** aus den Vorzeichen von $a$ und $b$ mitzudenken (die Funktion $\operatorname{atan2}(b,a)$ macht
genau das automatisch).

:::grafik
Derselbe Pfeil $z$ in der komplexen Ebene, nun mit eingezeichnetem Betrag $|z|$ (Länge) und Phase $\varphi$
(Winkel zur reellen Achse, als Bogen). Das rechtwinklige Dreieck mit Katheten $a = |z|\cos\varphi$ und
$b = |z|\sin\varphi$ ist hervorgehoben.
:::

## Die Eulersche Formel und die Exponentialform

Jetzt kommt die Brücke, die alles verbindet. Die __Eulersche Formel__ besagt

$$e^{\,j\varphi} = \cos\varphi + j\sin\varphi.$$

Der Ausdruck $e^{j\varphi}$ ist also genau der Pfeil der Länge 1 unter dem Winkel $\varphi$ — ein Punkt auf dem
**Einheitskreis**. Setzt man das in die Polarform ein, erhält man die kompakte __Exponentialform__:

$$z = |z|\,e^{\,j\varphi}.$$

- __$|z|$__: der __Betrag__ (die Länge des Pfeils).
- __$e^{\,j\varphi}$__: der __Einheitszeiger__ unter dem Winkel $\varphi$ (Drehung).

Eine komplexe Zahl ist damit vollständig durch „wie lang" ($|z|$) und „wie gedreht" ($\varphi$) beschrieben.
Genau diese Form macht das Rechnen mit Schwingungen später so leicht.

:::grafik
Der Einheitskreis in der komplexen Ebene; auf ihm der Zeiger $e^{j\varphi}$ unter dem Winkel $\varphi$, mit den
Projektionen $\cos\varphi$ (reelle Achse) und $\sin\varphi$ (imaginäre Achse) — eine Illustration der Eulerschen
Formel.
:::

## Warum die Exponentialform so praktisch ist

Der Lohn zeigt sich beim Multiplizieren. In der Exponentialform multipliziert man zwei komplexe Zahlen, indem man
ihre **Beträge multipliziert** und ihre **Winkel addiert**:

$$z_1 \cdot z_2 = |z_1|\,|z_2|\;e^{\,j(\varphi_1 + \varphi_2)}.$$

In kartesischer Form wäre dasselbe eine mühsame Ausmultipliziererei mit $j^2 = -1$. Geometrisch heißt das:
Multiplikation ist **Strecken und Drehen**. Insbesondere ist das Multiplizieren mit $e^{j\varphi}$ eine reine
**Drehung** um den Winkel $\varphi$ — ohne die Länge zu ändern. Diese Eigenschaft ist der Grund, warum
Schwingungen und Drehungen in der komplexen Schreibweise so natürlich werden.

:::grafik
Zwei Zeiger $z_1$ und $z_2$ und ihr Produkt in der komplexen Ebene: Die Längen multiplizieren sich, die Winkel
addieren sich ($\varphi_1 + \varphi_2$). Daneben separat die reine Drehung: Multiplikation mit $e^{j\varphi}$
dreht einen Zeiger, ohne ihn zu strecken.
:::

:::kern
Die __imaginäre Einheit__ $j$ (ET-Schreibweise) erfüllt $j^2 = -1$; eine __komplexe Zahl__ $z = a + jb$ hat
__Realteil__ $a$ und __Imaginärteil__ $b$ und lebt als Punkt/Pfeil in der __komplexen Ebene__. In der
__Polarform__ ist sie durch __Betrag__ $|z| = \sqrt{a^2+b^2}$ und __Phase__ $\varphi$ beschrieben (Vorsicht beim
Arkustangens: Quadrant beachten). Die __Eulersche Formel__ $e^{j\varphi} = \cos\varphi + j\sin\varphi$ führt auf
die __Exponentialform__ $z = |z|e^{j\varphi}$. Ihr großer Vorteil: Multiplizieren = __Beträge mal, Winkel plus__,
und $e^{j\varphi}$ ist eine reine Drehung.
:::

Ein Zeiger, der sich mit der Zeit dreht — das ist der Schritt von der ruhenden komplexen Zahl zur **Schwingung**.
Damit beschreibt man Sinussignale als rotierende Zeiger (__Phasoren__), das Thema des nächsten Abschnitts.
