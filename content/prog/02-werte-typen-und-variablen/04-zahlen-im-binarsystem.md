---
title: Zahlen im Binärsystem
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Kapitel 2: Werte, Typen und Variablen
order: 6030400
summary: Rechner speichern Zahlen als Folgen von Nullen und Einsen.
tags: Basis, Binärzahl, Bit, Byte, Hexadezimalzahl, Binärbruch, Verdopplungsverfahren
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Rechner speichern Zahlen als Folgen von Nullen und Einsen. Dieser Abschnitt erklärt das Binärsystem, zeigt, wie man von Hand und mit Python umrechnet, und klärt, welche Brüche sich im Binärsystem mit endlich vielen Stellen schreiben lassen.
:::

### Das Stellenwertsystem

<span class="anker" id="stufe-3-1"></span>

Um zu verstehen, wie ein Rechner Zahlen speichert, muss man zuerst genau sagen, was eine Ziffernfolge wie 4705 eigentlich bedeutet. Dann lässt sich dieselbe Idee auf andere Grundzahlen als 10 übertragen.

**Tausender, Hunderter, Zehner, Einer.** In 4705 steht die 4 für vier Tausender, die 7 für sieben Hunderter, die 0 für keinen Zehner und die 5 für fünf Einer. Jede Stelle ist zehnmal so viel wert wie die rechts neben ihr.

:::definition Definition 3.1 (Stellenwertsystem)
<span class="anker" id="satz-3-1"></span>

Sei $B\ge2$ eine natürliche Zahl, die __Basis__. Im Stellenwertsystem zur Basis $B$ steht eine Folge von Ziffern $z_{n-1}\ldots z_1z_0$ mit $0\le z_i<B$ für die Zahl

$$z_{n-1}B^{n-1}+\dots+z_1B^1+z_0B^0=\sum_{i=0}^{n-1}z_i\,B^i .$$

Die Zahl $B^i$ heißt der Stellenwert der Stelle $i$. Gezählt wird von rechts, beginnend bei $i=0$.
:::

::::beispiel
Im gewohnten Dezimalsystem ist $B=10$: $4705=4\cdot10^3+7\cdot10^2+0\cdot10^1+5\cdot10^0=4000+700+0+5$.
::::

⁠**Kurz gesagt:** In einem Stellenwertsystem ist jede Ziffer mit dem Stellenwert ihrer Position zu multiplizieren, und alles wird addiert.

### Die Binärzahl

<span class="anker" id="stufe-3-2"></span>

Eine Speicherzelle des Rechners unterscheidet nur zwei Zustände, wie ein Lichtschalter: an oder aus. Für Zahlen braucht man deshalb ein Stellenwertsystem mit nur zwei Ziffern.

**Schalter, die verdoppeln.** Man stelle sich eine Reihe von Schaltern vor. Der rechte zählt 1, der nächste 2, dann 4, 8, 16: Jeder zählt doppelt so viel wie sein rechter Nachbar. Die Zahl ist die Summe der Werte aller eingeschalteten Schalter.

:::definition Definition 3.2 (Binärzahl)
<span class="anker" id="satz-3-2"></span>

Eine __Binärzahl__ ist eine Zahl im Stellenwertsystem zur Basis $B=2$. Ihre Ziffern sind 0 und 1.
:::

Eine Binärstelle heißt __Bit__, nach dem englischen *binary digit*. Die Bits einer Zahl bezeichnet das Kapitel mit $b_i$, gezählt von rechts ab $i=0$. Damit man eine Binärzahl nicht mit einer Dezimalzahl verwechselt, schreibt man die Basis als kleine Zahl dahinter: $10011_2$. Der Wert ist

$$b_{n-1}\ldots b_1b_0\,{}_2=\sum_{i=0}^{n-1}b_i\,2^i .$$

::::beispiel
$10011_2$ hat die Bits $b_4=1$, $b_3=0$, $b_2=0$, $b_1=1$, $b_0=1$. Die Rechnung steht Schritt für Schritt in Abb. [3](#abb-3): Die Zahl ist 19.

:::abbildung prog/k2rbinaer 3
Der Wert der Binärzahl $10011_2$: jedes Bit mal seinem Stellenwert, dann addieren.
:::
::::

In Python schreibt man eine Binärzahl mit dem Präfix `0b`. Der interaktive Modus zeigt sie als Dezimalzahl an, denn das Objekt ist ein gewöhnlicher `int`:

```console
>>> 0b10011
19
>>> type(0b10011)
<class 'int'>
```

Die Methode `bit_length` eines `int` sagt, wie viele Bits die Zahl ohne führende Nullen braucht:

```console
>>> (19).bit_length()
5
```

⁠**Kurz gesagt:** Eine Binärzahl hat nur die Ziffern 0 und 1, die Bits; jedes Bit zählt $2^i$.

### Das Byte

<span class="anker" id="stufe-3-3"></span>

Ein einzelnes Bit kann nur zwei Werte unterscheiden. Speicher und Datenübertragung arbeiten deshalb mit Gruppen von Bits fester Größe.

:::definition Definition 3.3 (Byte)
<span class="anker" id="satz-3-3"></span>

Ein __Byte__ ist eine Gruppe von 8 Bit.
:::

Mit $n$ Bit lassen sich $2^n$ verschiedene Muster bilden, denn jedes Bit verdoppelt die Zahl der Möglichkeiten. Ein Byte hat also $2^8=256$ Muster und kann die ganzen Zahlen von 0 bis 255 darstellen. Speichergrößen zählt man in Byte: Eine Zahl aus 64 Bit belegt 8 Byte.

::::beispiel
Die größte Zahl in einem Byte hat alle acht Bits gesetzt. Ihr Wert ist die Summe aller acht Stellenwerte (Abb. [4](#abb-4)):

:::abbildung prog/k2rbyte 4
Der größte Wert eines Bytes: Alle acht Bits sind 1, die Stellenwerte $2^0$ bis $2^7$ werden addiert. Das Ergebnis ist $255=2^8-1$.
:::
::::

Das Ergebnis ist um eins kleiner als der nächste Stellenwert $2^8=256$. Das gilt für jede Zahl aus lauter Einsen: $n$ Einsen ergeben $2^n-1$, so wie im Dezimalsystem $999=10^3-1$ ist.

⁠**Kurz gesagt:** Ein Byte sind 8 Bit; es kann 256 verschiedene Werte annehmen, die Zahlen 0 bis 255.

### Ins Binärsystem umrechnen: erst von Hand, dann fertig

<span class="anker" id="stufe-3-4"></span>

Abb. [3](#abb-3) rechnet von binär nach dezimal. Für die Gegenrichtung gibt es ein Verfahren, das nur Ganzzahldivision und Rest braucht.

**Die Idee.** Teilt man eine ganze Zahl $n\ge0$ durch 2, ist der Rest das letzte Bit $b_0$: Alle anderen Stellenwerte $2,4,8,\ldots$ sind gerade, nur $b_0\cdot1$ kann einen ungeraden Anteil liefern. Der Quotient $n\,/\!/\,2$ enthält die übrigen Bits, um eine Stelle nach rechts gerückt. Teilt man ihn wieder durch 2, ist der Rest $b_1$, und so weiter, bis der Quotient 0 ist.

**Von Hand.** Die Reste, von unten nach oben gelesen, sind die Bits. Im interaktiven Modus erledigt `divmod` jeden Schritt:

```console
>>> divmod(19, 2)
(9, 1)
>>> divmod(9, 2)
(4, 1)
>>> divmod(4, 2)
(2, 0)
>>> divmod(2, 2)
(1, 0)
>>> divmod(1, 2)
(0, 1)
```

| $n$ | $n\,/\!/\,2$ | $n\,\%\,2$ | Bit |
|---|---|---|---|
| 19 | 9 | 1 | $b_0$ |
| 9 | 4 | 1 | $b_1$ |
| 4 | 2 | 0 | $b_2$ |
| 2 | 1 | 0 | $b_3$ |
| 1 | 0 | 1 | $b_4$ |

Von unten gelesen: $b_4b_3b_2b_1b_0=10011$, also $19=10011_2$.

**Fertig.** Python bringt die Umwandlung mit. Die Funktion `bin` liefert die Binärdarstellung als Zeichenkette mit dem Präfix `0b`; die Funktion `format` mit der Angabe `"b"` liefert sie ohne Präfix, mit `"08b"` auf acht Stellen mit führenden Nullen aufgefüllt. Für den Rückweg nimmt die Funktion `int` eine Zeichenkette und die Basis:

```console
>>> bin(19)
'0b10011'
>>> format(19, "b")
'10011'
>>> format(19, "08b")
'00010011'
>>> int("10011", 2)
19
>>> bin(-19)
'-0b10011'
```

Negative Zahlen schreibt Python mit einem Minus vor dem Präfix, so wie man sie auch im Dezimalsystem schreibt.

**Vergleich.** Von Hand und fertig stehen dieselben Bits da: $10011$. Der fertige Weg ist kürzer und macht keine Lesefehler beim Umdrehen der Reste; den Weg von Hand braucht man, um zu verstehen, warum die Reste die Bits sind.

⁠**Kurz gesagt:** Fortgesetzte Division durch 2 liefert die Bits als Reste, das letzte Bit zuerst; fertig erledigen das `bin` und `format`.

### Die Hexadezimalzahl

<span class="anker" id="stufe-3-5"></span>

Bitfolgen werden schnell lang und unübersichtlich: $0011111111111011$ liest niemand fehlerfrei vor. Man braucht eine kürzere Schreibweise, aus der man die Bits trotzdem sofort ablesen kann.

**Vier Bits sind eine Ziffer.** Vier Bits haben $2^4=16$ Muster. Gibt man jedem dieser 16 Muster ein eigenes Zeichen, kann man jede Bitfolge in Vierergruppen zerlegen und jede Gruppe durch ein Zeichen ersetzen.

:::definition Definition 3.4 (Hexadezimalzahl)
<span class="anker" id="satz-3-4"></span>

Eine __Hexadezimalzahl__ ist eine Zahl im Stellenwertsystem zur Basis $B=16$. Die Ziffern sind `0` bis `9` und `a` bis `f` für die Werte 10 bis 15.
:::

Weil $16=2^4$ ist, steht jede Hexadezimalziffer für genau vier Bits:

| `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` |
|---|---|---|---|---|---|---|---|
| `8` | `9` | `a` | `b` | `c` | `d` | `e` | `f` |
| 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

Ein Byte sind also genau zwei Hexadezimalziffern.

::::beispiel
$255=1111\,1111_2$ ist hexadezimal $\mathtt{ff}_{16}$, denn $15\cdot16+15=255$. Die lange Bitfolge vom Anfang zerlegt man von rechts in Vierergruppen: $0011\;1111\;1111\;1011_2=\mathtt{3ffb}_{16}$. In Python schreibt man Hexadezimalzahlen mit dem Präfix `0x`; `hex` wandelt um, `int` mit der Basis 16 wandelt zurück:

```console
>>> 0xff
255
>>> hex(255)
'0xff'
>>> int("3ffb", 16)
16379
>>> bin(0x3ffb)
'0b11111111111011'
```

Bei `bin` fehlen die beiden führenden Nullen der ersten Vierergruppe; Python lässt führende Nullen weg.
::::

⁠**Kurz gesagt:** Hexadezimal ist die Basis 16; jede Ziffer steht für vier Bits, ein Byte für zwei Ziffern.

### Binärbrüche

<span class="anker" id="stufe-3-6"></span>

Preise, Gewichte und Temperaturen haben Nachkommastellen. Auch sie muss ein Rechner mit Nullen und Einsen schreiben können.

**Stellen rechts vom Komma.** Im Dezimalsystem bedeuten die Stellen rechts vom Komma Zehntel, Hundertstel, Tausendstel. Im Binärsystem halbiert sich der Stellenwert von Stelle zu Stelle: Halbe, Viertel, Achtel, Sechzehntel.

:::definition Definition 3.5 (Binärbruch)
<span class="anker" id="satz-3-5"></span>

Ein __Binärbruch__ ist eine Zahl mit Stellen rechts vom Komma im Binärsystem. Die Stelle $k$ rechts vom Komma hat den Stellenwert $2^{-k}$:

$$0{,}b_{-1}b_{-2}\ldots b_{-m}\,{}_2=\sum_{k=1}^{m}b_{-k}\,2^{-k} .$$
:::

::::beispiel
$0{,}101_2=1\cdot\tfrac12+0\cdot\tfrac14+1\cdot\tfrac18=\tfrac58=0{,}625$ und $0{,}011_2=\tfrac14+\tfrac18=\tfrac38=0{,}375$.
::::

Nicht jeder Bruch hat einen endlichen Binärbruch. Im Dezimalsystem ist das vertraut: $\frac14=0{,}25$ endet, $\frac13=0{,}333\ldots$ nicht. Welche Zahlen im Binärsystem enden, sagt der folgende Satz.

:::satz Satz 3.6 (Endliche Binärbrüche)
<span class="anker" id="satz-3-6"></span>

Eine Zahl $x$ lässt sich genau dann als Binärbruch mit endlich vielen Stellen schreiben, wenn es eine ganze Zahl $p\ge0$ gibt, sodass $x\cdot2^p$ eine ganze Zahl ist.
:::

:::beweis Komma verschieben
Multiplizieren mit $2^p$ verschiebt im Binärsystem das Komma um $p$ Stellen nach rechts, so wie Multiplizieren mit $10^p$ im Dezimalsystem.

Hat $x$ höchstens $p$ Stellen rechts vom Komma, steht nach dem Verschieben keine Stelle mehr rechts vom Komma, und $x\cdot2^p$ ist ganz.

Ist umgekehrt $x\cdot2^p=n$ ganz, hat $n$ eine endliche Binärdarstellung. Verschiebt man darin das Komma um $p$ Stellen nach links, erhält man $x=n\cdot2^{-p}$ mit höchstens $p$ Stellen rechts vom Komma.
:::

**Anwendung auf $\frac38$ und $\frac1{10}$.** $\frac38\cdot2^3=3$ ist ganz, also endet der Binärbruch, und zwar nach drei Stellen. Für $\frac1{10}$ ist $\frac1{10}\cdot2^p=\frac{2^{p}}{10}=\frac{2^{p-1}}{5}$. Eine Zweierpotenz ist aber nie durch 5 teilbar, denn ihre einzigen Primfaktoren sind Zweien. Für kein $p$ ist das ganz: *$0{,}1$ hat im Binärsystem unendlich viele Stellen.* Dasselbe gilt für jeden gekürzten Bruch, in dessen Nenner ein anderer Primfaktor als 2 steckt, etwa $0{,}2=\frac15$ und $0{,}3=\frac3{10}$.

⁠**Kurz gesagt:** Ein Binärbruch endet genau dann, wenn der gekürzte Nenner eine Zweierpotenz ist; $0{,}1$ endet nicht.

### Das Verdopplungsverfahren

<span class="anker" id="stufe-3-7"></span>

Wie sehen die unendlich vielen Binärstellen von $0{,}1$ aus? Für die Stellen rechts vom Komma gibt es ein Verfahren, das dem Teilen durch 2 bei ganzen Zahlen entspricht.

**Die Idee.** Multipliziert man einen Binärbruch $0{,}b_{-1}b_{-2}b_{-3}\ldots{}_2$ mit 2, rückt das Komma eine Stelle nach rechts: Es entsteht $b_{-1}{,}b_{-2}b_{-3}\ldots{}_2$. Vor dem Komma steht jetzt die erste Stelle $b_{-1}$, also 0 oder 1, und dahinter der Rest. Mit dem Rest wiederholt man das.

:::definition Definition 3.7 (Verdopplungsverfahren)
<span class="anker" id="satz-3-7"></span>

Für $0\le x<1$ bestimmt das __Verdopplungsverfahren__ die Binärstellen von $x$: Man verdoppelt $x$. Der ganzzahlige Teil des Ergebnisses, 0 oder 1, ist die nächste Stelle; mit dem Anteil rechts vom Komma macht man weiter. Das Verfahren endet, wenn dieser Anteil 0 ist.
:::

::::beispiel [Beispiel 1] $0{,}625$
$2\cdot0{,}625=1{,}25$, Stelle 1, weiter mit $0{,}25$. $2\cdot0{,}25=0{,}5$, Stelle 0. $2\cdot0{,}5=1{,}0$, Stelle 1, Rest 0, fertig: $0{,}625=0{,}101_2$, wie im letzten Unterabschnitt.
::::

::::beispiel [Beispiel 2] $0{,}1$
Damit sich keine Rundung einschleicht, rechnet man mit dem Bruch $\frac{z}{10}$ und verdoppelt nur den ganzzahligen Zähler $z$. Ist $2z\ge10$, ist die Stelle 1 und man zieht 10 ab; sonst ist die Stelle 0:

| Schritt | Bruch | verdoppelt | Stelle |
|---|---|---|---|
| 1 | $1/10$ | $2/10$ | 0 |
| 2 | $2/10$ | $4/10$ | 0 |
| 3 | $4/10$ | $8/10$ | 0 |
| 4 | $8/10$ | $16/10=1+6/10$ | 1 |
| 5 | $6/10$ | $12/10=1+2/10$ | 1 |
| 6 | $2/10$ | $4/10$ | 0 |
| 7 | $4/10$ | $8/10$ | 0 |
| 8 | $8/10$ | $16/10=1+6/10$ | 1 |
| 9 | $6/10$ | $12/10=1+2/10$ | 1 |

In Schritt 6 steht derselbe Bruch $2/10$ wie in Schritt 2. Von da an wiederholt sich alles, und die Stellen $0011$ kehren endlos wieder:

$$0{,}1=0{,}0\,0011\,0011\,0011\ldots{}_2 .$$

Wie nahe man $0{,}1$ mit den ersten Stellen kommt, zeigt die Summe der Stellenwerte. Die Einsen kommen paarweise: an den Stellen 4 und 5, dann 8 und 9, dann 12 und 13 und so weiter. Ein Paar an den Stellen $4k$ und $4k+1$ ist $2^{-4k}+2^{-(4k+1)}=3\cdot2^{-(4k+1)}$ wert. Die ersten vier Paare, also die ersten 17 Stellen, ergeben (Abb. [5](#abb-5))

:::abbildung prog/k2rnull 5
Die ersten vier Paare von Einsen im Binärbruch von $0{,}1$, als Summe ihrer Stellenwerte. Nach 17 Stellen fehlt noch etwa $1{,}5\cdot10^{-6}$ bis $0{,}1$, und mit jeder weiteren Gruppe von vier Stellen schrumpft der Rest auf ein Sechzehntel.
:::
::::

Die Summe kommt $0{,}1$ immer näher, erreicht es aber mit keiner endlichen Zahl von Stellen. Der Fehler nach den 17 Stellen ist $0{,}1-\frac{13107}{131072}=\frac{1}{655360}=0{,}1\cdot2^{-16}$: Hinter Stelle 17 steht wieder dasselbe Muster wie in $0{,}1$ selbst, nur um 16 Stellen nach rechts gerückt.

⁠**Kurz gesagt:** Verdoppeln schiebt die nächste Binärstelle vor das Komma; für $0{,}1$ ergibt das die unendliche Folge $0{,}0\,0011\,0011\ldots{}_2$.

:::hintergrund Warum sich die Stellen wiederholen müssen
Im Verfahren für $0{,}1$ steht nach jedem Schritt ein Bruch $\frac{z}{10}$ mit einem Zähler $z$ von 0 bis 9. Es gibt also nur zehn mögliche Zustände. Spätestens nach zehn Schritten muss einer davon zum zweiten Mal auftreten, und weil jeder Schritt nur vom aktuellen Bruch abhängt, wiederholt sich von da an alles. Dasselbe Argument zeigt, dass jeder Bruch $\frac{z}{q}$ in jedem Stellenwertsystem entweder endet oder periodisch wird, mit einer Periode von weniger als $q$ Stellen. Im Dezimalsystem kennt man das von $\frac17=0{,}\overline{142857}$.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-8"></span>

:::aufgabe Aufgabe 8 ★ Binär nach dezimal und zurück
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Berechne den Wert von $101101_2$ und von $1000000_2$ von Hand. Prüfe mit `0b`.

</li>

<li>

Rechne 2026 von Hand mit fortgesetzter Division ins Binärsystem um. Prüfe mit `bin`.

</li>

<li>

Wie viele Bits braucht 2026? Prüfe mit der Methode `bit_length`.

</li>

</ol>

:::loesung
(a) $101101_2=32+8+4+1=45$ und $1000000_2=2^6=64$.

(b) Fortgesetzte Division durch 2, Reste von unten nach oben:

| $n$ | $n\,/\!/\,2$ | $n\,\%\,2$ | $n$ | $n\,/\!/\,2$ | $n\,\%\,2$ |
|---|---|---|---|---|---|
| 2026 | 1013 | 0 | 31 | 15 | 1 |
| 1013 | 506 | 1 | 15 | 7 | 1 |
| 506 | 253 | 0 | 7 | 3 | 1 |
| 253 | 126 | 1 | 3 | 1 | 1 |
| 126 | 63 | 0 | 1 | 0 | 1 |
| 63 | 31 | 1 |  |  |  |

Von unten gelesen: $2026=11111101010_2$.

(c) Elf Bits. Alles zusammen geprüft:

```console
>>> 0b101101
45
>>> 0b1000000
64
>>> bin(2026)
'0b11111101010'
>>> (2026).bit_length()
11
```

Probe: $2^{10}=1024\le2026<2048=2^{11}$, also braucht 2026 elf Stellen.
:::
:::

:::aufgabe Aufgabe 9 ★ Hexadezimal lesen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Schreibe $\mathtt{c8}_{16}$ und $\mathtt{3fb}_{16}$ als Bitfolgen und als Dezimalzahlen.

</li>

<li>

Wie viele Hexadezimalziffern braucht eine Zahl aus 64 Bit?

</li>

<li>

Prüfe (a) mit `int` und `bin`.

</li>

</ol>

:::loesung
(a) Jede Hexadezimalziffer ergibt vier Bits: $\mathtt{c8}_{16}=1100\,1000_2=12\cdot16+8=200$ und $\mathtt{3fb}_{16}=0011\,1111\,1011_2=3\cdot256+15\cdot16+11=1019$. Das ist das Exponentenfeld von $0{,}1$ aus Abb. [7](gleitkommazahlen-der-typ-float.html#abb-7).

(b) $64/4=16$ Hexadezimalziffern.

(c)

```console
>>> int("c8", 16)
200
>>> bin(0xc8)
'0b11001000'
>>> int("3fb", 16)
1019
>>> bin(0x3fb)
'0b1111111011'
```

Bei $\mathtt{3fb}$ lässt `bin` die beiden führenden Nullen weg.
:::
:::

:::aufgabe Aufgabe 10 ★★ Endlich oder nicht?
<span class="anker" id="aufg-10"></span>

Entscheide mit Satz [3.6](#satz-3-6), welche Zahlen einen endlichen Binärbruch haben, und gib ihn gegebenenfalls an: $0{,}75$; $0{,}2$; $0{,}375$; $\frac13$; $0{,}05$; $12{,}5$.

:::loesung
Nach Satz [3.6](#satz-3-6) kommt es darauf an, ob der gekürzte Nenner eine Zweierpotenz ist:

<ul>

<li>

$0{,}75=\frac34$, Nenner $4=2^2$: endlich, $0{,}11_2$.

</li>

<li>

$0{,}2=\frac15$: Nenner 5, nicht endlich.

</li>

<li>

$0{,}375=\frac38$, Nenner $2^3$: endlich, $0{,}011_2$.

</li>

<li>

$\frac13$: Nenner 3, nicht endlich.

</li>

<li>

$0{,}05=\frac1{20}$, Nenner $20=4\cdot5$ enthält 5: nicht endlich.

</li>

<li>

$12{,}5=\frac{25}2$: endlich, $12{,}5=8+4+\frac12=1100{,}1_2$.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 11 ★★ Wie fein wiegt eine Küchenwaage?
<span class="anker" id="aufg-11"></span>

Eine digitale Küchenwaage speichert jedes Gewicht als ganze Zahl aus 12 Bit. Der Bereich von 0 bis $5\,\mathrm{kg}$ wird dabei in gleich breite Stufen geteilt, eine Stufe für jedes Bitmuster.

<ol class="al">

<li>

Wie viele Stufen gibt es, und welche Zahl speichert die Waage höchstens?

</li>

<li>

Wie breit ist eine Stufe in Gramm? Rechne mit Python.

</li>

<li>

Ist die Stufenbreite in Kilogramm ein endlicher Binärbruch? Begründe mit Satz [3.6](#satz-3-6).

</li>

</ol>

:::loesung
(a) 12 Bit haben $2^{12}=4096$ Muster, also 4096 Stufen. Die größte Zahl ist $4095=2^{12}-1$, zwölf Einsen.

(b)

```console
>>> 2 ** 12
4096
>>> 5 / 4096 * 1000
1.220703125
```

Eine Stufe ist $1{,}220703125\,\mathrm g$ breit: Gewichte, die weniger als eine Stufe auseinanderliegen, kann diese Waage nicht sicher unterscheiden.

(c) $\frac5{4096}\cdot2^{12}=5$ ist ganz, also ist die Stufenbreite ein endlicher Binärbruch: $\frac{5}{4096}=101_2\cdot2^{-12}=0{,}000000000101_2$. Deshalb zeigt Python auch keine Rundungsstellen: Das Ergebnis ist exakt, denn auch $1{,}220703125=\frac{625}{512}$ hat einen Nenner, der eine Zweierpotenz ist.
:::
:::

:::aufgabe Aufgabe 12 ★★ $0{,}3$ von Hand
<span class="anker" id="aufg-12"></span>

Bestimme mit dem Verdopplungsverfahren die ersten zwölf Binärstellen von $0{,}3$. Rechne wie im Beispiel mit Brüchen $\frac{z}{10}$. Ab welchem Schritt wiederholt sich das Muster, und wie lang ist die Periode?

:::loesung
Man verdoppelt den Zähler von $\frac{z}{10}$; ab 10 ist die Stelle 1, und 10 wird abgezogen:

| Schritt | Bruch | verdoppelt | Stelle | Schritt | Bruch | verdoppelt | Stelle |
|---|---|---|---|---|---|---|---|
| 1 | $3/10$ | $6/10$ | 0 | 7 | $2/10$ | $4/10$ | 0 |
| 2 | $6/10$ | $1+2/10$ | 1 | 8 | $4/10$ | $8/10$ | 0 |
| 3 | $2/10$ | $4/10$ | 0 | 9 | $8/10$ | $1+6/10$ | 1 |
| 4 | $4/10$ | $8/10$ | 0 | 10 | $6/10$ | $1+2/10$ | 1 |
| 5 | $8/10$ | $1+6/10$ | 1 | 11 | $2/10$ | $4/10$ | 0 |
| 6 | $6/10$ | $1+2/10$ | 1 | 12 | $4/10$ | $8/10$ | 0 |

Die ersten zwölf Stellen: $0{,}3=0{,}010011001100\ldots{}_2$. In Schritt 7 steht wieder $\frac2{10}$ wie in Schritt 3; von dort an wiederholt sich alles. Die Periode beginnt also bei Schritt 3 und hat die Länge 4: $0{,}01\,0011\,0011\ldots{}_2$. Es ist dieselbe Periode $0011$ wie bei $0{,}1$, nur an anderer Stelle, denn $0{,}3=0{,}2+0{,}1$ und beide haben die Zählerfolge $2,4,8,6$.
:::
:::
