---
title: Gleitkommazahlen: der Typ `float`
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6030500
summary: Messwerte reichen von Pikofarad bis Megaohm und haben Nachkommastellen.
tags: Gleitkommazahl, Mantisse, Exponent, Exponentenfeld, Mantissenfeld, Darstellungsfehler
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Messwerte reichen von Pikofarad bis Megaohm und haben Nachkommastellen. Dieser Abschnitt zeigt, wie Python solche Zahlen in 64 Bit speichert, und warum dabei schon beim Eintippen von `0.1` ein kleiner Fehler entsteht.
:::

### Die Gleitkommadarstellung

<span class="anker" id="stufe-4-1"></span>

Ein Kondensator hat $2{,}2\cdot10^{-12}\,\mathrm F$, ein Widerstand $4{,}7\cdot10^{6}\,\Omega$. Dazwischen liegen 18 Zehnerpotenzen. Wollte man beide Werte mit einer festen Zahl von Stellen vor und hinter dem Komma speichern, bräuchte man Dutzende Ziffern, von denen fast alle null wären.

**Wissenschaftliche Schreibweise.** Die Technik löst das mit der wissenschaftlichen Schreibweise: einige gültige Ziffern und eine Zehnerpotenz, die sagt, wo das Komma steht. $4{,}7\cdot10^{6}$ und $2{,}2\cdot10^{-12}$ brauchen beide nur zwei Ziffern und einen Exponenten. Das Komma „gleitet“ mit dem Exponenten an die richtige Stelle. Rechner machen dasselbe, nur im Binärsystem und mit einer festen Zahl von Binärstellen.

:::definition Definition 4.1 (Gleitkommazahl)
<span class="anker" id="satz-4-1"></span>

Eine __Gleitkommazahl__ mit $p$ Binärstellen ist eine Zahl der Form $\pm\,m\cdot2^E$.

Darin ist die __Mantisse__ $m$ eine Binärzahl mit $p$ Stellen und genau einer Stelle vor dem Komma, die 1 ist: $m=1{,}\ldots{}_2$, also $1\le m<2$.

Der __Exponent__ $E$ ist eine ganze Zahl aus einem festen Bereich.
:::

::::beispiel ein Spielzeugformat
Mit nur $p=3$ Stellen gibt es vier Mantissen: $1{,}00_2=1$, $1{,}01_2=1{,}25$, $1{,}10_2=1{,}5$ und $1{,}11_2=1{,}75$. Lässt man die Exponenten $E=-1,0,1,2$ zu, entstehen 16 positive Zahlen:

| $E$ | $m=1$ | $m=1{,}25$ | $m=1{,}5$ | $m=1{,}75$ | Abstand |
|---|---|---|---|---|---|
| $-1$ | $0{,}5$ | $0{,}625$ | $0{,}75$ | $0{,}875$ | $0{,}125$ |
| $0$ | $1$ | $1{,}25$ | $1{,}5$ | $1{,}75$ | $0{,}25$ |
| $1$ | $2$ | $2{,}5$ | $3$ | $3{,}5$ | $0{,}5$ |
| $2$ | $4$ | $5$ | $6$ | $7$ | $1$ |

Auf dem Zahlenstrahl liegen sie nicht gleichmäßig (Abb. [6](#abb-6)). Zwischen 1 und 2 haben Nachbarn den Abstand $0{,}25$, zwischen 4 und 8 den Abstand 1: Mit jeder Zweierpotenz verdoppelt sich der Abstand. Eine Zahl wie $6{,}5$ kommt in diesem Format nicht vor; wer sie speichern will, muss sie auf eine der Nachbarzahlen 6 oder 7 runden.

:::abbildung prog/k2zahlenstrahl 6
Die 16 positiven Zahlen eines Gleitkommaformats mit drei Binärstellen und den Exponenten $-1$ bis $2$. In jedem Bereich von einer Zweierpotenz zur nächsten liegen gleich viele Zahlen, vier Stück; deshalb verdoppelt sich ihr Abstand mit jeder Zweierpotenz. Zwischen 0 und $0{,}5$ liegt keine Zahl des Formats.
:::
::::

⁠**Kurz gesagt:** Eine Gleitkommazahl ist Mantisse mal Zweierpotenz; mit fester Stellenzahl wächst der Abstand benachbarter Zahlen mit ihrem Betrag.

:::hintergrund Warum wachsende Abstände genau das Richtige sind
Der Abstand benachbarter Zahlen wächst im gleichen Verhältnis wie die Zahlen selbst. Der *relative* Abstand, also Abstand geteilt durch Betrag, bleibt deshalb ungefähr gleich: Im Spielzeugformat liegt er zwischen $\frac17$ und $\frac14$, egal ob man bei $0{,}5$ oder bei 6 schaut: von $0{,}5$ zum Nachbarn sind es $0{,}125$, ein Viertel von $0{,}5$, und von $3{,}5$ zum Nachbarn 4 sind es $0{,}5$, ein Siebtel von $3{,}5$. So arbeitet auch ein Messgerät mit automatischer Bereichswahl: Es zeigt immer etwa gleich viele gültige Ziffern, bei $4{,}700\,\mathrm{k\Omega}$ ebenso wie bei $1{,}000\,\mathrm{pF}$. Ein fester Abstand wäre für kleine Werte zu grob und für große unnötig fein. Gleitkommazahlen verteilen ihre Genauigkeit so, dass jede Zahl ungefähr gleich viele gültige Stellen hat.
:::

### Der Typ `float`

<span class="anker" id="stufe-4-2"></span>

Das Spielzeugformat hat nur 16 Zahlen. Ein Rechner braucht ein Format mit viel mehr Stellen und einem viel größeren Exponentenbereich, und alle Rechner sollten dasselbe Format benutzen, damit Programme überall dieselben Ergebnisse liefern.

**Ein Wort aus 64 Bit.** Python speichert jede Gleitkommazahl in genau 64 Bit, also 8 Byte. Diese 64 Bit sind in drei Felder geteilt: ein Bit für das Vorzeichen, 11 Bit für den Exponenten, 52 Bit für die Mantisse (Abb. [7](#abb-7)).

:::definition Definition 4.2 (Der Typ `float`)
<span class="anker" id="satz-4-2"></span>

Ein Objekt vom Typ `float` speichert eine Gleitkommazahl im Format *binary64* der Norm IEEE 754. Die Mantisse hat $p=53$ Binärstellen, der Exponent liegt im Bereich $-1022\le E\le1023$. Die Zahl belegt 64 Bit, aufgeteilt in drei Felder:

<ul>

<li>

1 Bit Vorzeichen $s$: $s=0$ für positive, $s=1$ für negative Zahlen;

</li>

<li>

11 Bit Exponentenfeld $c$;

</li>

<li>

52 Bit Mantissenfeld $t$.

</li>

</ul>
:::

Die Norm IEEE 754 legt fest, wie Rechner Gleitkommazahlen speichern und mit ihnen rechnen; fast alle Prozessoren seit den 1980er-Jahren halten sich an sie. Der Name *binary64* sagt: Basis 2, 64 Bit. Man nennt das Format auch „doppelte Genauigkeit“.

:::abbildung prog/k2bitfelder 7
Die 64 Bit eines `float`, oben für die Zahl $6{,}5$, unten für die Zahl, die Python beim Eintippen von `0.1` speichert. Links das Vorzeichenbit (Bit 63), dann 11 Bit Exponentenfeld, rechts 52 Bit Mantissenfeld (Bit 51 bis 0).
:::

⁠**Kurz gesagt:** Ein `float` ist eine Gleitkommazahl mit 53 Binärstellen Mantisse, gespeichert in 64 Bit: Vorzeichen, Exponentenfeld, Mantissenfeld.

:::hintergrund Woher die Norm kommt
Bis in die 1980er-Jahre rechnete fast jeder Rechnerhersteller anders: mit anderen Stellenzahlen, anderen Rundungsregeln, anderen Antworten auf Überläufe. Dasselbe Programm lieferte auf zwei Maschinen verschiedene Ergebnisse, und numerische Software ließ sich kaum übertragen. Ein Ausschuss der IEEE, eines Verbands von Elektroingenieuren, erarbeitete deshalb eine gemeinsame Norm; sie erschien 1985 als IEEE 754. Maßgeblich daran beteiligt war der Mathematiker William Kahan aus Berkeley, der dafür 1989 den Turing-Preis erhielt. Die Norm wurde 2008 und 2019 überarbeitet; die Fassung von 2019 gilt heute.
:::

### Das Exponentenfeld

<span class="anker" id="stufe-4-3"></span>

Der Exponent kann negativ sein, von $-1022$ bis $1023$. Die 11 Bit des Exponentenfelds sind aber eine gewöhnliche Binärzahl ohne Vorzeichen, von 0 bis $2^{11}-1=2047$.

**Ein verschobener Nullpunkt.** Man verschiebt den Nullpunkt, so wie bei einer Temperaturskala: Statt des Exponenten selbst speichert man den Exponenten plus 1023. Aus dem kleinsten Exponenten $-1022$ wird so die 1, aus dem Exponenten 0 die 1023.

:::definition Definition 4.3 (Exponentenfeld)
<span class="anker" id="satz-4-3"></span>

Das __Exponentenfeld__ $c$ eines `float` speichert den um 1023 verschobenen Exponenten:

$$c=E+1023,\qquad E=c-1023 .$$

Gewöhnliche Zahlen haben $1\le c\le2046$. Die Werte $c=0$ und $c=2047$ sind für besondere Fälle reserviert.
:::

Die Zahl 1023 heißt die Verschiebung des Exponenten.

::::beispiel
In Abb. [7](#abb-7) hat $6{,}5$ das Exponentenfeld $10000000001_2=1025$, also $E=1025-1023=2$. Tatsächlich ist $6{,}5=1{,}625\cdot2^2$. Die untere Zeile hat $c=01111111011_2=\mathtt{3fb}_{16}=1019$, also $E=-4$.
::::

⁠**Kurz gesagt:** Das Exponentenfeld speichert $E+1023$; so kommt es ohne Vorzeichen aus.

:::hintergrund Warum der Exponent verschoben gespeichert wird
Die Felder stehen in der Reihenfolge Vorzeichen, Exponent, Mantisse, und der Exponent ist verschoben, also nie negativ. Zusammen hat das eine praktische Folge: Liest man die 64 Bit zweier positiver `float` als gewöhnliche ganze Zahlen ohne Vorzeichen, ist die größere ganze Zahl auch der größere `float`. Ein größerer Exponent ergibt ein größeres Exponentenfeld und damit ein größeres Bitmuster, und bei gleichem Exponenten entscheidet die Mantisse. Ein Rechner kann Gleitkommazahlen deshalb mit denselben schnellen Befehlen vergleichen und sortieren wie ganze Zahlen; nur das Vorzeichen braucht eine eigene Behandlung. Mit einem Exponenten in einer Darstellung mit Vorzeichen ginge das nicht.
:::

### Das Mantissenfeld

<span class="anker" id="stufe-4-4"></span>

Die Mantisse hat 53 Binärstellen, für sie stehen aber nur 52 Bit zur Verfügung.

**Die erste Ziffer ist immer 1.** Nach der Definition der Gleitkommazahl steht vor dem Komma der Mantisse immer eine 1. Was immer gleich ist, muss man nicht speichern. Das Mantissenfeld enthält deshalb nur die 52 Stellen nach dem Komma.

:::definition Definition 4.4 (Mantissenfeld)
<span class="anker" id="satz-4-4"></span>

Das __Mantissenfeld__ $t$ eines `float` enthält die 52 Binärstellen der Mantisse nach dem Komma. Liest man sie als ganze Zahl $t$, ist die Mantisse

$$m=1+\frac{t}{2^{52}} .$$
:::

Die 1 vor dem Komma heißt das verborgene Bit, weil sie nicht im Speicher steht. Mit Exponentenfeld und Mantissenfeld zusammen ist der Wert eines `float` mit $1\le c\le2046$

<span class="anker" id="gl-4-1"></span>
$$x=(-1)^s\cdot\Bigl(1+\frac{t}{2^{52}}\Bigr)\cdot2^{\,c-1023}. \tag{4.1}$$

::::beispiel
Für $6{,}5$ beginnt das Mantissenfeld in Abb. [7](#abb-7) mit $101$, danach folgen nur Nullen. Die Mantisse ist also $m=1{,}101_2=1+\frac12+\frac18=1{,}625$, und mit $E=2$ und $s=0$ ergibt sich $x=1{,}625\cdot4=6{,}5$.
::::

⁠**Kurz gesagt:** Das Mantissenfeld speichert die 52 Stellen hinter dem Komma; die führende 1 ergänzt man beim Lesen.

### Einen `float` in seine Felder zerlegen

<span class="anker" id="stufe-4-5"></span>

Um zu sehen, was Python tatsächlich gespeichert hat, braucht man die drei Felder. Abb. [7](#abb-7) ist mühsam zu lesen; Python liefert dieselbe Information kürzer.

**Die Methode `hex`.** Jeder `float` hat eine Methode `hex`. Sie schreibt die Zahl als Mantisse mal Zweierpotenz, die Mantisse hexadezimal:

```console
>>> (6.5).hex()
'0x1.a000000000000p+2'
>>> (-0.75).hex()
'-0x1.8000000000000p-1'
```

So liest man die Zeichenkette:

<ul>

<li>

ein Minus am Anfang, falls $s=1$ ist;

</li>

<li>

`0x1.` ist das verborgene Bit, eine 1 vor dem Komma, hier hexadezimal geschrieben;

</li>

<li>

die 13 Hexadezimalziffern danach sind das Mantissenfeld $t$, je Ziffer vier Bits, zusammen 52 Bit;

</li>

<li>

hinter `p` steht der Exponent $E$ als Dezimalzahl, also nicht das Feld $c$, sondern $c-1023$.

</li>

</ul>

::::beispiel
Bei $6{,}5$ ist das Mantissenfeld $\mathtt{a000000000000}_{16}$, die Ziffer $\mathtt a=1010_2$ und dahinter nur Nullen: $m=1{,}1010_2=1{,}625$. Mit $E=2$ folgt $6{,}5$, wie in Abb. [7](#abb-7). Bei $-0{,}75$ ist $s=1$, $\mathtt{8}=1000_2$, also $m=1{,}1_2=1{,}5$, und $E=-1$: $x=-1{,}5\cdot\frac12=-0{,}75$.
::::

⁠**Kurz gesagt:** `hex` zeigt einen `float` als $\pm$`0x1.`*Mantissenfeld*`p`*Exponent*.

### Der Darstellungsfehler

<span class="anker" id="stufe-4-6"></span>

$0{,}1$ hat im Binärsystem unendlich viele Stellen (Unterabschnitt [3.7](zahlen-im-binarsystem.html#stufe-3-7)). Ein `float` hat aber nur 53. Was speichert Python, wenn man `0.1` eintippt?

**Der nächste Nachbar.** Liegt eine Zahl zwischen zwei darstellbaren Zahlen, wie $6{,}5$ in Abb. [6](#abb-6), muss Python eine von beiden nehmen. Es nimmt die nähere.

:::definition Definition 4.5 (Rundung und Darstellungsfehler)
<span class="anker" id="satz-4-5"></span>

Ist eine Zahl $x$ nicht als `float` darstellbar, speichert Python den `float`, der $x$ am nächsten liegt. Liegt $x$ genau in der Mitte zwischen zwei `float`, nimmt Python den, dessen letztes Mantissenbit 0 ist. Die Differenz zwischen dem gespeicherten Wert und $x$ heißt __Darstellungsfehler__.
:::

Die Regel für die Mitte heißt „Runden zur geraden Mantisse“. Im Spielzeugformat liegt $6{,}5$ genau zwischen $6=1{,}10_2\cdot2^2$ und $7=1{,}11_2\cdot2^2$; gerundet wird auf 6, weil dessen letztes Mantissenbit 0 ist.

**Von Hand: die Felder von $0{,}1$ vorhersagen.** Aus dem Verdopplungsverfahren ist

$$0{,}1=0{,}0001\,1001\,1001\,1001\ldots{}_2=1{,}1001\,1001\,1001\ldots{}_2\cdot2^{-4}.$$

Das Komma ist vier Stellen nach rechts gerückt, also $E=-4$. Nach dem Komma der Mantisse wiederholt sich $1001$, hexadezimal die Ziffer `9`. Von den unendlich vielen Stellen passen 52 ins Mantissenfeld, das sind 13 Hexadezimalziffern: $\mathtt{9999999999999}$. Die erste Stelle, die nicht mehr hineinpasst, ist eine 1, und dahinter folgen weitere Einsen. Der abgeschnittene Rest ist also mehr als eine halbe letzte Stelle, und die nächste darstellbare Zahl liegt oben: Die letzte Ziffer wird aufgerundet, aus `9` wird `a`. Die Vorhersage lautet `0x1.999999999999ap-4`.

**Fertig: was Python gespeichert hat.** Die Methode `hex` bestätigt die Vorhersage. Die Methode `as_integer_ratio` aus Unterabschnitt [1.4](objekte-und-typen.html#stufe-1-4) liefert den gespeicherten Wert als gekürzten Bruch:

```console
>>> (0.1).hex()
'0x1.999999999999ap-4'
>>> (0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)
>>> 2 ** 55
36028797018963968
```

Der Nenner ist $2^{55}$. Gespeichert ist also nicht $\frac1{10}$, sondern $\frac{3602879701896397}{2^{55}}$. Dasselbe Ergebnis liefert Gleichung [(4.1)](#gl-4-1) aus den Feldern (Abb. [8](#abb-8)): $s=0$, $c=1019$, und das Mantissenfeld ist $\mathtt{999999999999a}_{16}=2702159776422298$.

:::abbildung prog/k2rfloat 8
Der Wert, den Python für `0.1` speichert, aus den drei Feldern berechnet: Vorzeichen $s=0$, Exponentenfeld $c=1019$, Mantissenfeld $t=\mathtt{999999999999a}_{16}$; $2^{52}=4503599627370496$, $2^{55}=36028797018963968$.
:::

**Den gespeicherten Wert genau ausschreiben.** Ein Bruch mit dem Nenner $2^{55}$ hat einen endlichen Dezimalbruch, denn $\frac{1}{2^{55}}=\frac{5^{55}}{10^{55}}$. Multipliziert man den Zähler mit $5^{55}$, stehen die Dezimalstellen da. Mit `int` ist das eine exakte Rechnung:

```console
>>> 3602879701896397 * 5 ** 55
1000000000000000055511151231257827021181583404541015625
```

Komma 55 Stellen von rechts gesetzt:

$$\mathtt{0.1}\ \text{gespeichert}=0{,}1000000000000000055511151231257827021181583404541015625 .$$

Der Darstellungsfehler ist also etwa $5{,}55\cdot10^{-18}$, relativ zu $0{,}1$ etwa $5{,}55\cdot10^{-17}$.

**Vergleich.** Von Hand und fertig stimmen überein: Das Verdopplungsverfahren liefert das Muster $1001$, die Rundung macht aus der letzten Ziffer ein `a`, und Python zeigt genau diese Felder.

⁠**Kurz gesagt:** Python speichert den nächstgelegenen `float`; für `0.1` ist das $\frac{3602879701896397}{2^{55}}$, um etwa $5{,}6\cdot10^{-18}$ zu groß.

:::hintergrund Ein Darstellungsfehler mit Folgen: das Flugabwehrsystem in Dhahran
Am 25. Februar 1991 verfehlte ein Patriot-Flugabwehrsystem in Dhahran (Saudi-Arabien) eine anfliegende Rakete; beim Einschlag starben 28 Soldaten. Der US-Rechnungshof fand bei seiner Untersuchung die Ursache in der Zeitrechnung. Das System zählte die Zeit in Zehntelsekunden als ganze Zahl und rechnete sie in Sekunden um, indem es mit $0{,}1$ multiplizierte. Diese $0{,}1$ stand in einem Register mit 24 Bit, also mit noch weniger Stellen als ein `float`, und war deshalb um etwa $9{,}5\cdot10^{-8}$ zu klein. Nach über 100 Stunden Dauerbetrieb, also nach mehr als 3,6 Millionen Zehntelsekunden, war daraus eine Zeitabweichung von $0{,}34\,\mathrm s$ geworden. Die Untersuchung beziffert die Folge: Der Bereich, in dem das System die Rakete erwartete, lag 687 Meter neben ihr. Schaden richtete der Fehler an, weil zwei Programmteile die Zeit verschieden genau umrechneten; so hoben sich die Fehler beim Abziehen zweier Zeitpunkte nicht mehr auf.

Zwei Dinge lehrt der Fall: Ein winziger Darstellungsfehler wird durch Multiplikation mit einer großen Zahl groß. Und das System rechnete nicht mit Gleitkommazahlen nach IEEE 754, sondern mit einer festen Zahl von Stellen. Das Problem steckt nicht in einem bestimmten Format, sondern darin, dass $\frac1{10}$ in *keinem* Binärformat exakt ist.
:::

### Die kürzeste Darstellung

<span class="anker" id="stufe-4-7"></span>

Wenn Python $0{,}1000000000000000055511\ldots$ gespeichert hat, warum zeigt der interaktive Modus dann `0.1` an? Und warum zeigt er bei `0.1 + 0.2` plötzlich 17 Stellen?

**Ein Etikett, das eindeutig sein muss.** Zwischen zwei benachbarten `float` liegen unendlich viele Dezimalzahlen. Alle, die näher am gespeicherten Wert liegen als an seinen Nachbarn, führen beim Eintippen zu genau diesem `float`. Python sucht unter ihnen die mit den wenigsten Stellen aus und zeigt sie als Etikett an.

:::definition Definition 4.6 (Kürzeste Darstellung)
<span class="anker" id="satz-4-6"></span>

Der interaktive Modus und `print` zeigen einen `float` als die kürzeste Dezimalzahl, die beim Eintippen genau diesen `float` ergibt.
:::

Angezeigt ist also nicht der gespeicherte Wert, sondern ein eindeutiges Kennzeichen für ihn. Tippt man die angezeigte Zahl wieder ein, erhält man genau denselben `float`.

::::beispiel
Für den gespeicherten Wert von `0.1` ist die kürzeste solche Dezimalzahl $0{,}1$ selbst; deshalb erscheint `0.1`. Bei `0.1 + 0.2` ist das anders:

```console
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.3
0.3
>>> (0.1 + 0.2).hex()
'0x1.3333333333334p-2'
>>> (0.3).hex()
'0x1.3333333333333p-2'
```

Die Summe ist ein anderer `float` als der, den Python für `0.3` speichert: Die Mantissenfelder unterscheiden sich in der letzten Stelle, die beiden Zahlen sind Nachbarn. Das Etikett `0.3` ist schon vergeben, also braucht die Summe ein längeres, und das kürzeste, das zu ihr und zu keinem Nachbarn passt, hat 17 Stellen.
::::

⁠**Kurz gesagt:** Angezeigt wird die kürzeste Dezimalzahl, die denselben `float` ergibt; angezeigt ist nicht gleich gespeichert.

:::hintergrund Wie viele Stellen nötig sind, und was vor Python 3.1 angezeigt wurde
Für das Format binary64 gelten zwei feste Zahlen. Jede Dezimalzahl mit höchstens 15 gültigen Stellen übersteht den Weg in einen `float` und, auf 15 Stellen gerundet, zurück unverändert. Und 17 gültige Stellen genügen immer, um einen `float` eindeutig zu kennzeichnen. Bis Python 3.0 rundete der interaktive Modus deshalb jede Anzeige auf 17 gültige Stellen und schrieb für `0.1` die Zahl `0.10000000000000001`. Seit Python 3.1 sucht ein Verfahren, das auf den Mathematiker David Gay zurückgeht, die kürzeste passende Zahl. Am gespeicherten Wert hat sich dadurch nichts geändert, nur an seinem Etikett. Gerade deshalb fällt der Darstellungsfehler heute erst auf, wenn eine Rechnung von dem Wert wegführt, den man eingetippt hat.
:::

### Aufgaben zu Abschnitt [4](#stufe-4)

<span class="anker" id="stufe-4-8"></span>

:::aufgabe Aufgabe 13 ★ Felder lesen
<span class="anker" id="aufg-13"></span>

Bestimme mit `hex` Vorzeichen, Exponent $E$, Exponentenfeld $c$ und Mantisse $m$ von `1.0`, `3.0`, `-0.5` und `0.75`. Rechne aus den Feldern den Wert mit Gleichung [(4.1)](#gl-4-1) zurück.

:::loesung
```console
>>> (1.0).hex()
'0x1.0000000000000p+0'
>>> (3.0).hex()
'0x1.8000000000000p+1'
>>> (-0.5).hex()
'-0x1.0000000000000p-1'
>>> (0.75).hex()
'0x1.8000000000000p-1'
```

| Zahl | $s$ | $E$ | $c=E+1023$ | $m$ |
|---|---|---|---|---|
| $1{,}0$ | 0 | 0 | 1023 | $1{,}0$ |
| $3{,}0$ | 0 | 1 | 1024 | $1{,}1_2=1{,}5$ |
| $-0{,}5$ | 1 | $-1$ | 1022 | $1{,}0$ |
| $0{,}75$ | 0 | $-1$ | 1022 | $1{,}1_2=1{,}5$ |

Die Ziffer `8` ist $1000_2$; sie steht für die erste Stelle nach dem Komma, also $\frac12$. Zurückgerechnet mit [(4.1)](#gl-4-1): $1\cdot2^0=1$, $1{,}5\cdot2^1=3$, $-1\cdot2^{-1}=-0{,}5$, $1{,}5\cdot2^{-1}=0{,}75$. Alle vier Zahlen sind exakt, denn ihre Mantissen haben nur eine Stelle nach dem Komma.
:::
:::

:::aufgabe Aufgabe 14 ★★ $0{,}2$ und $0{,}3$ vorhersagen
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

$0{,}2=2\cdot0{,}1$. Sage ohne Rechner vorher, was `(0.2).hex()` anzeigt.

</li>

<li>

Sage mit deinen Binärstellen aus Aufgabe [12](zahlen-im-binarsystem.html#aufg-12) vorher, was `(0.3).hex()` anzeigt. Wird die letzte Hexadezimalziffer auf- oder abgerundet? Begründe mit der ersten Stelle, die nicht mehr ins Mantissenfeld passt.

</li>

<li>

Prüfe beide Vorhersagen am Rechner.

</li>

</ol>

:::loesung
(a) Verdoppeln erhöht nur den Exponenten um 1; die Mantisse bleibt. Die Rundung ist dieselbe, weil dieselben Binärstellen abgeschnitten werden. Vorhersage:

`0x1.999999999999ap-3`

(b) Aus Aufgabe [12](zahlen-im-binarsystem.html#aufg-12): $0{,}3=0{,}01\,0011\,0011\ldots{}_2=1{,}0011\,0011\ldots{}_2\cdot2^{-2}$. Nach dem Komma der Mantisse wiederholt sich $0011$, hexadezimal `3`. Die 13 Hexadezimalziffern sind `3333333333333`. Die erste Stelle, die nicht mehr hineinpasst, beginnt eine neue Gruppe $0011$, ist also 0: Der abgeschnittene Rest ist kleiner als eine halbe letzte Stelle, und es wird abgerundet. Vorhersage: `0x1.3333333333333p-2`.

(c)

```console
>>> (0.2).hex()
'0x1.999999999999ap-3'
>>> (0.3).hex()
'0x1.3333333333333p-2'
```

Beide Vorhersagen stimmen. Der gespeicherte Wert von `0.3` ist also etwas *kleiner* als $0{,}3$, der von `0.1` und `0.2` etwas größer. Auch das erklärt, warum `0.1 + 0.2` nicht beim `float` für `0.3` landet.
:::
:::

:::aufgabe Aufgabe 15 ★★ Welche Zahlen sind exakt?
<span class="anker" id="aufg-15"></span>

Entscheide für jede Zahl, ob Python sie exakt speichert: $0{,}5$; $0{,}25$; $0{,}2$; $1024{,}0$; $1{,}1$. Prüfe mit `as_integer_ratio`: Woran erkennst du an der Antwort, ob die Zahl exakt gespeichert wurde?

:::loesung
```console
>>> (0.5).as_integer_ratio()
(1, 2)
>>> (0.25).as_integer_ratio()
(1, 4)
>>> (0.2).as_integer_ratio()
(3602879701896397, 18014398509481984)
>>> (1024.0).as_integer_ratio()
(1024, 1)
>>> (1.1).as_integer_ratio()
(2476979795053773, 2251799813685248)
```

`as_integer_ratio` liefert den gespeicherten Wert als gekürzten Bruch. Ist dieser Bruch die gemeinte Zahl, wurde sie exakt gespeichert: $\frac12$, $\frac14$ und $\frac{1024}1$ stimmen. Bei $0{,}2=\frac15$ und $1{,}1=\frac{11}{10}$ steht dagegen ein riesiger Bruch mit einer Zweierpotenz im Nenner ($2^{54}$ und $2^{51}$), also ein anderer Wert. Der Nenner eines gespeicherten `float` ist immer eine Zweierpotenz; genau die Zahlen mit einem solchen gekürzten Nenner, die außerdem in 53 Stellen passen, sind exakt.
:::
:::

:::aufgabe Aufgabe 16 ★★★ Große ganze Zahlen als `float`
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

$10^{22}=2^{22}\cdot5^{22}$. Zeige mit Python, dass $5^{22}<2^{53}$ ist, und folgere, dass `1e22` exakt gespeichert wird.

</li>

<li>

Warum gilt das für $10^{23}$ nicht?

</li>

<li>

Prüfe mit `int(1e22)` und `int(1e23)`. Die Funktion `int` macht dabei aus dem gespeicherten `float` die ganze Zahl, die er tatsächlich darstellt.

</li>

</ol>

:::loesung
(a) und (b):

```console
>>> 5 ** 22
2384185791015625
>>> 2 ** 53
9007199254740992
>>> 5 ** 23
11920928955078125
```

$10^{22}=5^{22}\cdot2^{22}$. Der Faktor $2^{22}$ geht in den Exponenten. Die Mantisse muss also die ganze Zahl $5^{22}$ darstellen, und die ist kleiner als $2^{53}$, passt also in 53 Binärstellen. Damit ist `1e22` exakt. Bei $10^{23}=5^{23}\cdot2^{23}$ ist $5^{23}>2^{53}$, und weil $5^{23}$ ungerade ist, lässt sich auch kein Faktor 2 in den Exponenten schieben: Die Zahl bräuchte 54 Binärstellen und wird gerundet.

(c)

```console
>>> int(1e22)
10000000000000000000000
>>> int(1e23)
99999999999999991611392
```

`1e23` ist als `float` um $8\,388\,608=2^{23}$ kleiner als $10^{23}$. Das ist die Hälfte des Abstands benachbarter `float` bei dieser Größe, und `int` zeigt es als exakte ganze Zahl.
:::
:::
