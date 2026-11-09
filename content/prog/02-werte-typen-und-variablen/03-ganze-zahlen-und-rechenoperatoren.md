---
title: Ganze Zahlen und Rechenoperatoren
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
knoten: Python 2: Werte, Typen und Variablen
order: 6030300
summary: Ganze Zahlen sind der einfachste Zahlentyp von Python.
tags: Operator, Operanden, Ganzzahldivision, Rest, Rangfolge
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ganze Zahlen sind der einfachste Zahlentyp von Python. Dieser Abschnitt zeigt, wie groß sie werden können, welche Rechenoperatoren Python kennt und wie es ganzzahlig teilt, auch bei negativen Zahlen.
:::

### Der Typ `int`

<span class="anker" id="stufe-2-1"></span>

Stückzahlen, Zählerstände, Abtastnummern, Adressen: Vieles in der Technik ist ganzzahlig. Dort will man exakt rechnen, ohne jede Rundung, auch wenn die Zahlen sehr groß werden.

**Ziffern, so viele wie nötig.** Auf Papier schreibt man eine ganze Zahl mit so vielen Ziffern, wie sie braucht. Eine dreistellige Zahl braucht drei Ziffern, eine dreißigstellige dreißig. Genau so geht Python mit ganzen Zahlen um.

:::definition Definition 2.1 (Der Typ `int`)
<span class="anker" id="satz-2-1"></span>

Der Typ `int` umfasst die ganzen Zahlen $\ldots,-2,-1,0,1,2,\ldots$ Ein Objekt vom Typ `int` hat keine feste Größe: Es wird so groß, wie die Zahl es verlangt, und ist nur durch den Arbeitsspeicher begrenzt. Addieren, Subtrahieren und Multiplizieren zweier `int` liefert immer das exakte Ergebnis als `int`.
:::

Man schreibt einen `int` als Folge von Ziffern ohne Punkt, negative Zahlen mit einem Minus davor. Lange Zahlen darf man mit Unterstrichen gliedern: `1_000_000` ist dieselbe Zahl wie `1000000`.

::::beispiel
$2^{100}$ hat 31 Stellen und wird exakt ausgerechnet. Auch eine Rechnung, bei der eine kleine Zahl zwischen zwei riesigen steht, geht nicht verloren:

```console
>>> 2 ** 100
1267650600228229401496703205376
>>> 10 ** 20 + 1 - 10 ** 20
1
>>> 1_000_000 * 1_000_000
1000000000000
```
::::

⁠**Kurz gesagt:** Ein `int` ist eine ganze Zahl beliebiger Größe; Python rechnet mit ihr exakt.

:::hintergrund Warum ein `int` in Python nie überläuft
Ein Prozessor rechnet mit ganzen Zahlen fester Größe. Eine übliche Größe reicht bis $18\,446\,744\,073\,709\,551\,615$; was darüber hinausgeht, schneidet der Maschinenbefehl ab, und das Ergebnis ist falsch. Die ganzzahligen Typen der Sprache C haben solche festen Grenzen.

CPython speichert einen `int` deshalb nicht als eine einzige Maschinenzahl, sondern wie eine Zahl auf Papier: als Folge von Ziffern. Nur ist die Basis nicht 10, sondern $2^{30}=1\,073\,741\,824$. Jede „Ziffer“ ist eine Zahl von 0 bis $2^{30}-1$ und belegt ein eigenes Speicherwort; das Vorzeichen steht getrennt davor. Wird eine Zahl größer, hängt CPython weitere Ziffern an. Gerechnet wird wie beim schriftlichen Rechnen in der Schule: Ziffer für Ziffer mit Übertrag, jeder Schritt mit gewöhnlichen Maschinenbefehlen. Der Preis ist Zeit: Eine Addition großer Zahlen braucht viele Maschinenbefehle statt eines einzigen.
:::

:::hintergrund Eine Grenze gibt es doch: 4300 Dezimalstellen bei der Umwandlung in Text
Rechnen kann Python mit beliebig großen `int`. Für die Anzeige muss es die Zahl aber in Dezimalziffern umwandeln, und das ist bei riesigen Zahlen viel aufwendiger als jede Addition: Der Aufwand wächst deutlich schneller als die Zahl der Stellen. Ein Angreifer könnte einem Server, der Zahlen aus Texten liest, eine Zahl mit Millionen Stellen schicken und ihn damit lange beschäftigen. Seit Python 3.11 verweigert Python deshalb Umwandlungen mit mehr als 4300 Dezimalstellen. Die Lücke ist unter der Kennung CVE-2020-10735 öffentlich beschrieben.

```console
>>> 10 ** 5000
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    10 ** 5000
    ~~~^^~~~~~
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
```

Ausgerechnet ist die Zahl; nur die Anzeige scheitert. Die Meldung nennt den Weg, die Grenze zu verschieben. Umwandlungen in Systeme mit einer Zweierpotenz als Basis sind ausgenommen, weil sie schnell gehen.
:::

### Operator und Operand

<span class="anker" id="stufe-2-2"></span>

Python 1 hat die Zeichen `+ - * / **` Rechenzeichen genannt ([Programmieren, Python 1, Abschnitt 4.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4)). Python kennt weitere solche Zeichen, und es gibt einen allgemeinen Namen für sie.

**Eine kleine Maschine.** Ein Rechenzeichen nimmt Werte entgegen und gibt einen neuen Wert heraus, wie eine kleine Maschine mit Eingängen und einem Ausgang.

:::definition Definition 2.2 (Operator und Operand)
<span class="anker" id="satz-2-2"></span>

Ein __Operator__ ist ein Zeichen, das aus Werten einen neuen Wert berechnet.

Die Werte, auf die ein Operator wirkt, heißen seine __Operanden__.
:::

Ein Operator mit zwei Operanden heißt zweistellig, einer mit nur einem Operanden einstellig. In `7 - 2` ist das Minus zweistellig, in `-7` einstellig: Es macht aus 7 die Zahl $-7$.

Python hat sieben arithmetische Operatoren:

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `+` | Addition | `7 + 2` ergibt `9` |
| `-` | Subtraktion; einstellig: Vorzeichen | `7 - 2` ergibt `5` |
| `*` | Multiplikation | `7 * 2` ergibt `14` |
| `/` | Division | `7 / 2` ergibt `3.5` |
| `//` | Ganzzahldivision | `7 // 2` ergibt `3` |
| `%` | Rest | `7 % 2` ergibt `1` |
| `**` | Potenz | `7 ** 2` ergibt `49` |

**Welchen Typ das Ergebnis hat.** Sind beide Operanden ein `int`, ist auch das Ergebnis ein `int`, mit einer Ausnahme: Die Division `/` liefert immer einen `float`. Ist mindestens ein Operand ein `float`, verwandelt Python den anderen ebenfalls in einen `float`, und das Ergebnis ist ein `float`:

```console
>>> 7 + 2
9
>>> 7 + 0.5
7.5
>>> 2 * 3.0
6.0
```

⁠**Kurz gesagt:** Ein Operator berechnet aus seinen Operanden einen neuen Wert; ist ein Operand ein `float`, ist es auch das Ergebnis.

### Die Division

<span class="anker" id="stufe-2-3"></span>

Spannung durch Widerstand, Strecke durch Zeit: Die gewöhnliche Division braucht man ständig, und sie soll das Ergebnis liefern, das man aus der Mathematik kennt.

:::definition Definition 2.3 (Division)
<span class="anker" id="satz-2-3"></span>

Der Operator `/` teilt den linken Operanden durch den rechten. Das Ergebnis ist immer ein `float`, auch wenn beide Operanden ein `int` sind und die Division aufgeht.
:::

::::beispiel
Das erklärt die Beobachtung aus Python 1, dass `12 / 4` die Antwort `3.0` liefert:

```console
>>> 7 / 2
3.5
>>> 12 / 4
3.0
>>> 1 / 3
0.3333333333333333
>>> 7 / 0
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    7 / 0
    ~~^~~
ZeroDivisionError: division by zero
```

Durch null teilen geht nicht; Python meldet einen `ZeroDivisionError`. Teilt man einen `float` durch null, lautet die Beschreibung in Python 3.13 `float division by zero`, ab Python 3.14 wie bei ganzen Zahlen `division by zero`.
::::

⁠**Kurz gesagt:** `/` teilt wie in der Mathematik und liefert immer einen `float`.

:::hintergrund Warum `/` auch bei ganzen Zahlen einen `float` liefert
In den alten Versionen 2.x der Sprache Python ergab `7 / 2` die ganze Zahl 3, wie in C: Bei zwei ganzen Zahlen wurde ganzzahlig geteilt, bei Gleitkommazahlen gewöhnlich. Das Ergebnis hing also davon ab, welchen Typ die Werte gerade hatten, und nicht davon, was der Programmierer meinte. Eine Rechnung wie „Summe der Messwerte durch ihre Anzahl“ lieferte mit Messwerten `4.0` und `5.0` den Wert 4,5, mit denselben Messwerten als `4` und `5` still den Wert 4. Weil man in Python nirgends festlegt, welchen Typ ein Wert haben muss, gerieten ganze Zahlen leicht in solche Rechnungen.

Mit Python 3.0 (2008) wurde die Bedeutung deshalb getrennt: `/` teilt immer wie in der Mathematik, und wer ganzzahlig teilen will, schreibt dafür einen eigenen Operator. Ein Ausdruck bedeutet seitdem dasselbe, egal ob ganze Zahlen oder Gleitkommazahlen in ihn hineinkommen.
:::

### Ganzzahldivision und Rest

<span class="anker" id="stufe-2-4"></span>

125 Minuten sind 2 Stunden und 5 Minuten. Für solche Rechnungen braucht man zwei Zahlen: wie oft 60 ganz in 125 passt, und was übrig bleibt.

**Vielfache auf dem Zahlenstrahl.** Man markiert auf dem Zahlenstrahl alle Vielfachen des Teilers, etwa alle Vielfachen von 2. Jede ganze Zahl $a$ liegt dann entweder auf einem Vielfachen oder zwischen zweien. Das nächste Vielfache links von $a$ (oder $a$ selbst) ist $q\cdot2$; der Abstand von dort bis $a$ ist der Rest (Abb. [2](#abb-2)). Für $a=7$ ist das Vielfache $6=3\cdot2$ und der Rest 1. Für $a=-7$ ist das nächste Vielfache links $-8=(-4)\cdot2$, nicht $-6$, und der Rest ist wieder 1.

:::abbildung prog/k2rest 2
Ganzzahldivision durch 2 auf dem Zahlenstrahl. Zu jeder Zahl $a$ gehört das nächste Vielfache von 2 links von ihr, $q\cdot2$; der Abstand bis $a$ ist der Rest. Für $a=7$ ist $q=3$, für $a=-7$ ist $q=-4$. In beiden Fällen ist der Rest 1.
:::

:::definition Definition 2.4 (Ganzzahldivision und Rest)
<span class="anker" id="satz-2-4"></span>

Für ganze Zahlen $a$ und $b\ne0$ ist `a // b` die größte ganze Zahl, die nicht größer ist als $a/b$. Das ist der Quotient, nach unten gerundet, also in Richtung $-\infty$.

Der Rest ist `a % b` $=a-(a\,/\!/\,b)\cdot b$.
:::

Der Operator `//` heißt __Ganzzahldivision__, der Operator `%` liefert den __Rest__. Aus der Definition folgen zwei Regeln, die man sich merken sollte.

:::satz Satz 2.5 (Ganzzahldivision und Rest)
<span class="anker" id="satz-2-5"></span>

Für alle ganzen Zahlen $a$ und $b\ne0$ gilt

<span class="anker" id="gl-2-1"></span>
$$a = (a\,/\!/\,b)\cdot b + a\,\%\,b . \tag{2.1}$$

Für $b>0$ liegt der Rest im Bereich $0\le a\,\%\,b<b$, für $b<0$ im Bereich $b<a\,\%\,b\le0$. Der Rest hat also immer das Vorzeichen von $b$ oder ist null.
:::

:::beweis aus der Definition
[(2.1)](#gl-2-1) ist die Definition des Rests, nach $a$ aufgelöst. Sei $b>0$ und $q=a\,/\!/\,b$. Weil $q$ die größte ganze Zahl mit $q\le a/b$ ist, gilt $q\le a/b<q+1$. Multipliziert man mit $b>0$, folgt $qb\le a<qb+b$, also $0\le a-qb<b$, und $a-qb$ ist der Rest. Für $b<0$ dreht die Multiplikation beide Ungleichungen um: $qb\ge a>qb+b$, also $0\ge a-qb>b$.
:::

::::beispiel
Zuerst positive Zahlen, dann negative:

```console
>>> 125 // 60
2
>>> 125 % 60
5
>>> -7 // 2
-4
>>> -7 % 2
1
>>> 7 // -2
-4
>>> 7 % -2
-1
```

Die Probe mit [(2.1)](#gl-2-1): $2\cdot60+5=125$, $(-4)\cdot2+1=-7$ und $(-4)\cdot(-2)+(-1)=7$. Bei $-7\,/\!/\,2$ ist $-7/2=-3{,}5$, und die größte ganze Zahl, die nicht größer ist, ist $-4$, nicht $-3$.
::::

Die eingebaute Funktion `divmod` liefert beide Ergebnisse auf einmal, zuerst den Quotienten, dann den Rest. Beide Operatoren funktionieren auch mit Gleitkommazahlen:

```console
>>> divmod(125, 60)
(2, 5)
>>> divmod(-7, 2)
(-4, 1)
>>> 7.5 // 2
3.0
>>> 7.5 % 2
1.5
```

⁠**Kurz gesagt:** `//` rundet den Quotienten nach unten, Richtung $-\infty$; `%` ist der Rest dazu und hat das Vorzeichen des rechten Operanden.

:::hintergrund Warum Python Richtung $-\infty$ rundet und nicht Richtung null
In C rundet die ganzzahlige Division Richtung null: Dort ist $-7/2=-3$, und damit die Gleichung [(2.1)](#gl-2-1) gilt, muss der Rest $-1$ sein. Python rundet nach unten, weil dann der Rest für $b>0$ immer zwischen 0 und $b-1$ liegt, egal welches Vorzeichen $a$ hat. Das ist genau die Eigenschaft, die man bei allem braucht, was sich periodisch wiederholt:

<ul>

<li>

⁠**Uhrzeit:** Zählt eine Uhr Sekunden seit einem Bezugszeitpunkt, ist `t % 86400` die Sekunde des Tages, auch für Zeitpunkte vor dem Bezugszeitpunkt, also für negative $t$. Eine Sekunde vor Mitternacht ist `-1 % 86400`, das ergibt 86399, also 23:59:59.

</li>

<li>

⁠**Winkel:** Eine Phase von $-90^\circ$ ist dieselbe wie $270^\circ$. `-90 % 360` ergibt 270, jeder Winkel landet im Bereich von $0^\circ$ bis unter $360^\circ$.

</li>

</ul>

Hat man sich für diesen Rest entschieden, liegt der Quotient fest: Nach [(2.1)](#gl-2-1) ist $q=(a-r)/b$, und das ist der abgerundete Quotient. In der Zahlentheorie ist dieselbe Wahl üblich. Dass C anders rechnet, hat vermutlich geschichtliche Gründe: Die Rechenwerke der damaligen Prozessoren teilten Richtung null, und seit 1999 schreibt die Norm der Sprache C diese Rundung fest vor.
:::

### Die Potenz

<span class="anker" id="stufe-2-5"></span>

Zehnerpotenzen für Einheitenvorsätze, Zweierpotenzen für Speichergrößen, Quadrate für Leistungen: Potenzen kommen in fast jeder technischen Rechnung vor. Python 1 hat `**` mit positiven ganzen Exponenten benutzt und `2 ** 0.5` für die Wurzel. Für den Typ des Ergebnisses, für negative Exponenten und für Minuszeichen in der Nähe gelten eigene Regeln.

:::definition Definition 2.6 (Potenz)
<span class="anker" id="satz-2-6"></span>

`a ** b` ist $a$ hoch $b$. Sind $a$ und $b$ ein `int` und ist $b\ge0$, ist das Ergebnis ein `int`; ist $b$ ein negativer `int`, ist es ein `float`. Ist einer der Operanden ein `float`, ist das Ergebnis ebenfalls ein `float`; nur eine negative Basis mit einem nicht ganzzahligen Exponenten liefert etwas anderes. Außerdem gilt:

<ul>

<li>

`**` bindet stärker als ein Minuszeichen links davon: `-2 ** 2` ist $-(2^2)=-4$.

</li>

<li>

Mehrere `**` wertet Python von rechts nach links aus: `2 ** 3 ** 2` ist $2^{(3^2)}=2^9=512$.

</li>

</ul>
:::

::::beispiel
Negative Exponenten, Minuszeichen und Potenztürme:

```console
>>> 2 ** -1
0.5
>>> 10 ** -3
0.001
>>> -2 ** 2
-4
>>> (-2) ** 2
4
>>> 2 ** 3 ** 2
512
>>> (2 ** 3) ** 2
64
>>> 0 ** 0
1
```

`0 ** 0` ist in Python festgelegt als 1, wie in den meisten Programmiersprachen.
::::

⁠**Kurz gesagt:** `**` bindet stärker als ein Minus davor und wird von rechts nach links ausgewertet; ein negativer Exponent liefert einen `float`.

:::hintergrund Warum Python die Potenz so liest wie die Mathematik
Beide Regeln stammen aus der mathematischen Schreibweise. $-2^2$ bedeutet dort $-(2^2)=-4$; wer $(-2)^2$ meint, setzt Klammern. Ein Potenzturm $a^{b^c}$ bedeutet $a^{(b^c)}$, weil die andere Lesart keinen Turm braucht: $(a^b)^c=a^{b\cdot c}$ schreibt man einfacher mit einem einzigen Exponenten. Python übernimmt beides, damit Formeln aus dem Lehrbuch ohne Umdenken in den Quelltext wandern können. Ein Minus *rechts* vom Operator gehört dagegen zum Exponenten: `2 ** -1` ist $2^{-1}=0{,}5$.
:::

### Die Rangfolge

<span class="anker" id="stufe-2-6"></span>

Ein Ausdruck wie `2 + 3 * 4 ** 2 // 5` enthält vier Operatoren. Python braucht eine feste Regel, in welcher Reihenfolge es sie anwendet.

:::definition Definition 2.7 (Rangfolge)
<span class="anker" id="satz-2-7"></span>

Die __Rangfolge__ der Operatoren legt fest, welcher Operator in einem Ausdruck ohne Klammern zuerst ausgeführt wird. Für die arithmetischen Operatoren gilt, vom stärksten zum schwächsten:

| Rang | Operatoren | bei gleichem Rang |
|---|---|---|
| 1 | `**` | von rechts nach links |
| 2 | einstelliges `+` und `-` |  |
| 3 | `*` `/` `//` `%` | von links nach rechts |
| 4 | zweistelliges `+` und `-` | von links nach rechts |

Klammern gehen allem vor.
:::

::::beispiel
`2 + 3 * 4 ** 2 // 5` wertet Python so aus: zuerst die Potenz $4^2=16$, dann von links nach rechts $3\cdot16=48$ und $48\,/\!/\,5=9$, zuletzt $2+9=11$. Bei `12 / 3 / 2` haben beide Operatoren denselben Rang, also gilt $(12/3)/2=2$:

```console
>>> 2 + 3 * 4 ** 2 // 5
11
>>> 100 - 7 % 3 * 2
98
>>> 12 / 3 / 2
2.0
>>> -3 ** 2
-9
```

In der zweiten Zeile ist $7\,\%\,3=1$, dann $1\cdot2=2$, zuletzt $100-2=98$.
::::

⁠**Kurz gesagt:** Potenz vor Vorzeichen vor Punktrechnung (`* / // %`) vor Strichrechnung; Klammern gehen vor, und im Zweifel setzt man sie.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-7"></span>

:::aufgabe Aufgabe 4 ★ Ergebnisse vorhersagen
<span class="anker" id="aufg-4"></span>

Schreibe für jeden Ausdruck Wert und Typ auf. Prüfe danach am Rechner.

<ol class="al">

<li>

`7 / 2` (b) `7 // 2` (c) `-7 // 2` (d) `-7 % 3` (e) `7 % -3`

</li>

<li>

⁠**(f)** `2 ** -1` (g) `-2 ** 2` (h) `2 ** 3 ** 2` (i) `6 / 2` (j) `7.5 // 2`

</li>

</ol>

:::loesung
```console
>>> 7 / 2
3.5
>>> 7 // 2
3
>>> -7 // 2
-4
>>> -7 % 3
2
>>> 7 % -3
-2
>>> 2 ** -1
0.5
>>> -2 ** 2
-4
>>> 2 ** 3 ** 2
512
>>> 6 / 2
3.0
>>> 7.5 // 2
3.0
```

Typen: (a), (f), (i), (j) sind `float`, alle anderen `int`. Begründungen: `/` liefert immer `float`, auch bei `6 / 2`. $-7/2=-3{,}5$, nach unten gerundet $-4$. $-7\,/\!/\,3=-3$, also $-7\,\%\,3=-7-(-3)\cdot3=2$; der Rest hat das Vorzeichen von $3$. $7\,/\!/\,(-3)=-3$, also $7\,\%\,(-3)=7-(-3)(-3)=-2$, mit dem Vorzeichen von $-3$. Ein negativer Exponent liefert einen `float`. `**` bindet stärker als das Minus davor und gruppiert von rechts: $-(2^2)$ und $2^{(3^2)}$. `7.5 // 2` rundet $3{,}75$ nach unten zu 3; weil ein Operand ein `float` ist, ist es auch das Ergebnis.
:::
:::

:::aufgabe Aufgabe 5 ★★ Die Gleichung für Quotient und Rest prüfen
<span class="anker" id="aufg-5"></span>

Bestimme für die Paare $(a,b)=(17,5)$, $(-17,5)$, $(17,-5)$ und $(-17,-5)$ von Hand $a\,/\!/\,b$ und $a\,\%\,b$. Prüfe für jedes Paar die Gleichung [(2.1)](#gl-2-1) und die Vorzeichenregel aus Satz [2.5](#satz-2-5). Vergleiche danach mit `divmod`.

:::loesung
Der Quotient ist $a/b$, nach unten gerundet; der Rest folgt aus $r=a-q\cdot b$:

| $a$ | $b$ | $a/b$ | $q=a\,/\!/\,b$ | $r=a\,\%\,b$ | Probe $q\cdot b+r$ |
|---|---|---|---|---|---|
| 17 | 5 | $3{,}4$ | 3 | 2 | $15+2=17$ |
| $-17$ | 5 | $-3{,}4$ | $-4$ | 3 | $-20+3=-17$ |
| 17 | $-5$ | $-3{,}4$ | $-4$ | $-3$ | $20-3=17$ |
| $-17$ | $-5$ | $3{,}4$ | 3 | $-2$ | $-15-2=-17$ |

Vorzeichenregel: Für $b=5$ liegen die Reste 2 und 3 in $0\le r<5$, für $b=-5$ die Reste $-3$ und $-2$ in $-5<r\le0$. Mit `divmod`:

```console
>>> divmod(17, 5)
(3, 2)
>>> divmod(-17, 5)
(-4, 3)
>>> divmod(17, -5)
(-4, -3)
>>> divmod(-17, -5)
(3, -2)
```

Auffällig ist $-17\,/\!/\,5=-4$ und nicht $-3$: Python rundet Richtung $-\infty$. In C wäre es $-3$ mit dem Rest $-2$.
:::
:::

:::aufgabe Aufgabe 6 ★★ Sekunden in Tage, Stunden, Minuten
<span class="anker" id="aufg-6"></span>

Eine Messung läuft $100\,000$ s.

<ol class="al">

<li>

Zerlege die Dauer mit `//` und `%` in Tage, Stunden, Minuten und Sekunden.

</li>

<li>

Rechne dasselbe mit `divmod`, Schritt für Schritt im interaktiven Modus.

</li>

<li>

Ein Zeitstempel zählt Sekunden ab Mitternacht eines Bezugstags. Welche Uhrzeit gehört zu $t=-3600$ s? Beantworte die Frage mit einem einzigen Ausdruck.

</li>

</ol>

:::loesung
(a) Ein Tag hat $86\,400\,\mathrm s$, eine Stunde $3600\,\mathrm s$. Zuerst die ganzen Tage, dann mit dem Rest weiter:

```console
>>> 100000 // 86400
1
>>> 100000 % 86400
13600
>>> 13600 // 3600
3
>>> 13600 % 3600
2800
>>> 2800 // 60
46
>>> 2800 % 60
40
```

Ergebnis: 1 Tag, 3 Stunden, 46 Minuten, 40 Sekunden. Probe: $86\,400+3\cdot3600+46\cdot60+40=100\,000$.

(b) `divmod` liefert beide Teile auf einmal:

```console
>>> divmod(100000, 86400)
(1, 13600)
>>> divmod(13600, 3600)
(3, 2800)
>>> divmod(2800, 60)
(46, 40)
```

(c) Die Sekunde des Tages ist der Rest bei der Division durch $86\,400$:

```console
>>> -3600 % 86400
82800
>>> 82800 // 3600
23
```

$82\,800\,\mathrm s=23\,\mathrm h$, die Uhrzeit ist also 23:00:00 am Vortag. Das klappt nur, weil `%` für einen positiven Teiler immer einen Rest zwischen 0 und $86\,399$ liefert, auch für negative $t$.
:::
:::

:::aufgabe Aufgabe 7 ★ Phasenwinkel in den Bereich von $0^\circ$ bis $360^\circ$
<span class="anker" id="aufg-7"></span>

Ein Programm berechnet Phasenwinkel in Grad, die außerhalb von $0^\circ$ bis $360^\circ$ liegen können. Bringe $-90^\circ$, $450^\circ$, $-450^\circ$ und $720^\circ$ mit einem Operator in diesen Bereich. Welches Ergebnis hättest du für $-90^\circ$ bekommen, wenn `%` wie in C rechnen würde?

:::loesung
Der Rest bei der Division durch 360 liegt immer im Bereich von 0 bis 359:

```console
>>> -90 % 360
270
>>> 450 % 360
90
>>> -450 % 360
270
>>> 720 % 360
0
```

Würde `%` wie in C Richtung null runden, wäre der Quotient von $-90/360=-0{,}25$ die Zahl 0 und der Rest $-90-0\cdot360=-90$. Der Winkel bliebe negativ, und man bräuchte eine zusätzliche Fallunterscheidung.
:::
:::
