---
title: Rechnen mit Gleitkommazahlen
pfad: Informatik / Programmieren / Python / Werte, Typen und Variablen
adresse: informatik/programmieren/python/werte-typen-und-variablen
knoten: Kapitel 2: Werte, Typen und Variablen
order: 6030600
summary: Nicht nur das Eintippen, auch jede Rechnung mit float wird gerundet.
tags: Rundungsfehler, Maschinengenauigkeit, absorbiert, Auslöschung, Überlauf
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Nicht nur das Eintippen, auch jede Rechnung mit `float` wird gerundet. Dieser Abschnitt bestimmt, wie groß dieser Fehler höchstens ist, wann er sichtbar wird und was passiert, wenn ein Ergebnis zu groß oder ungültig wird.
:::

### Der Rundungsfehler einer Rechnung

<span class="anker" id="stufe-5-1"></span>

Die Summe zweier `float` hat im Allgemeinen mehr Binärstellen, als ein `float` fassen kann. Python muss das Ergebnis jeder Rechnung wieder in das Format zwängen.

**Exakt rechnen, dann runden.** Man kann sich vorstellen, dass der Prozessor das exakte Ergebnis aus den beiden gespeicherten Werten bildet, mit so vielen Stellen wie nötig, und es danach auf den nächsten `float` rundet.

:::definition Definition 5.1 (Korrekt gerundete Rechnung)
<span class="anker" id="satz-5-1"></span>

Für die Grundrechenarten $+$, $-$, $\cdot$, $/$ und die Quadratwurzel verlangt IEEE 754: Das Ergebnis ist das exakte Ergebnis der gespeicherten Werte, gerundet nach derselben Regel wie beim Speichern, also auf den nächsten `float` und bei Gleichstand zur geraden Mantisse. Der dabei entstehende Unterschied heißt __Rundungsfehler__ der Rechnung.
:::

::::beispiel $0{,}1+0{,}2$
Die gespeicherten Werte sind etwas größer als $0{,}1$ und $0{,}2$. Ihre exakte Summe ist

$$0{,}3000000000000000166533453693773481063544750213623046875 .$$

Sie liegt zwischen zwei benachbarten `float`:

|  |  |
|---|---|
| linker Nachbar, der `float` für `0.3` | $0{,}299999999999999988897769753748434595763683319091796875$ |
| exakte Summe | $0{,}3000000000000000166533453693773481063544750213623046875$ |
| rechter Nachbar, angezeigt als `0.30000000000000004` | $0{,}3000000000000000444089209850062616169452667236328125$ |

Beide Abstände sind genau gleich, $2{,}78\cdot10^{-17}$: ein Gleichstand. Die Regel entscheidet für die gerade Mantisse. Das Mantissenfeld des linken Nachbarn endet auf `3`, also auf das Bit 1, das des rechten auf `4`, also auf das Bit 0. Deshalb ist das Ergebnis der rechte Nachbar, und `0.1 + 0.2` ist nicht der `float`, den Python für `0.3` speichert.
::::

::::beispiel zehnmal $0{,}1$
Bei vielen Rechenschritten wird jedes Zwischenergebnis gerundet, und die Fehler können sich summieren. Mit dem Unterstrich `_` für das letzte Ergebnis ([Kapitel 1, Abschnitt 4.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-4)) und der Pfeiltaste addiert man im interaktiven Modus zehnmal $0{,}1$:

```console
>>> 0.1
0.1
>>> _ + 0.1
0.2
>>> _ + 0.1
0.30000000000000004
>>> _ + 0.1
0.4
>>> _ + 0.1
0.5
>>> _ + 0.1
0.6
>>> _ + 0.1
0.7
>>> _ + 0.1
0.7999999999999999
>>> _ + 0.1
0.8999999999999999
>>> _ + 0.1
0.9999999999999999
>>> 0.1 * 10
1.0
```

Nach zehn Additionen fehlt eine letzte Stelle bis 1. Die Multiplikation `0.1 * 10` ist dagegen ein einziger Rechenschritt, und dessen exaktes Ergebnis liegt so nahe an 1, dass die Rundung genau 1 trifft. Dieselbe Größe, auf zwei Wegen gerechnet, ergibt zwei verschiedene `float`.
::::

⁠**Kurz gesagt:** Jede Rechnung ist exakt gerechnet und dann gerundet; die Fehler einzelner Schritte können sich über viele Schritte summieren.

:::hintergrund Summen genauer bilden: die kompensierte Summation
Beim Addieren eines kleinen Werts zu einer großen Zwischensumme gehen die hinteren Stellen des kleinen Werts verloren. Der Mathematiker William Kahan schlug 1965 vor, diesen verlorenen Rest bei jedem Schritt auszurechnen und in einer zweiten Zahl, der Korrektur, aufzusammeln: Man berechnet die neue Summe, zieht davon die alte Summe ab und vergleicht mit dem Wert, den man addieren wollte. Der Unterschied ist genau das, was die Rundung verschluckt hat. Arnold Neumaier verbesserte das Verfahren 1974 für den Fall, dass ein Summand größer ist als die bisherige Summe.

Python benutzt dieses Verfahren: Die eingebaute Funktion `sum`, die viele Werte auf einmal addiert, arbeitet seit Python 3.12 mit Neumaiers Korrektur und liefert für zehnmal $0{,}1$ genau `1.0`. Wer den Rundungsfehler beim Summieren sehen will, muss deshalb wie oben Schritt für Schritt addieren. Ältere Lehrtexte, die den Fehler mit `sum` zeigen, gelten für Python bis 3.11.
:::

### Die Maschinengenauigkeit

<span class="anker" id="stufe-5-2"></span>

Wie groß kann ein Rundungsfehler höchstens werden? Das hängt vom Abstand benachbarter `float` ab, und den kann man an einer Stelle besonders leicht ablesen: bei 1.

**Der erste Schritt hinter der 1.** $1=1{,}000\ldots0_2\cdot2^0$ hat das Mantissenfeld 0. Der nächstgrößere `float` hat im Mantissenfeld eine 1 an der letzten, der 52. Stelle. Er ist um $2^{-52}$ größer.

:::definition Definition 5.2 (Maschinengenauigkeit)
<span class="anker" id="satz-5-2"></span>

Die __Maschinengenauigkeit__ $\varepsilon_{\mathrm M}$ ist der Abstand von 1 zum nächstgrößeren `float`:

$$\varepsilon_{\mathrm M}=2^{-52}\approx2{,}22\cdot10^{-16}.$$
:::

:::satz Satz 5.3 (Größe des Rundungsfehlers)
<span class="anker" id="satz-5-3"></span>

Liegt eine Zahl $x\ne0$ im Bereich der gewöhnlichen `float`, unterscheidet sich der gerundete Wert $\tilde x$ von $x$ höchstens um

$$|\tilde x-x|\le\frac{\varepsilon_{\mathrm M}}{2}\,|x|=2^{-53}\,|x|\approx1{,}11\cdot10^{-16}\,|x| .$$

Ein `float` hat also etwa 16 gültige Dezimalstellen.
:::

:::beweis halber Abstand
Sei $2^E\le|x|<2^{E+1}$. In diesem Bereich haben alle `float` den Exponenten $E$, und ihre Mantissen unterscheiden sich in Schritten von $2^{-52}$. Benachbarte `float` haben dort also den Abstand $2^{-52}\cdot2^E$. Beim Runden auf den nächsten ist der Fehler höchstens der halbe Abstand: $|\tilde x-x|\le2^{-53}\cdot2^E\le2^{-53}\,|x|$, weil $2^E\le|x|$.
:::

::::beispiel
Addiert man zu 1 den Wert $2^{-52}$, entsteht der Nachbar von 1. Addiert man nur die Hälfte, $2^{-53}$, liegt das exakte Ergebnis genau in der Mitte zwischen 1 und dem Nachbarn, und die Rundung zur geraden Mantisse liefert wieder 1:

```console
>>> 1.0 + 2 ** -52
1.0000000000000002
>>> 1.0 + 2 ** -53
1.0
>>> 2 ** -52
2.220446049250313e-16
```

Der Abstand wächst mit der Zahl. Bei $10^{16}$ ist er schon 2: $10^{16}$ liegt zwischen $2^{53}$ und $2^{54}$, also ist der Abstand $2^{-52}\cdot2^{53}=2$. Die Zahl $10^{16}+1$ kann es als `float` nicht geben:

```console
>>> 1e16 + 1
1e+16
>>> 1e16 + 2
1.0000000000000002e+16
>>> 2 ** 53 + 1.0
9007199254740992.0
```

Die letzte Zeile zeigt eine Folge davon: Alle ganzen Zahlen bis $2^{53}=9\,007\,199\,254\,740\,992$ sind als `float` exakt, darüber nicht mehr jede.
::::

**Die Beobachtung aus [Kapitel 1](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html).** Das Heron-Rezept endete bei `1.414213562373095`, der fertige Weg `2 ** 0.5` lieferte `1.4142135623730951` ([Kapitel 1, Abschnitt 4.5](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/der-interaktive-modus.html#stufe-4-5)). Zwischen 1 und 2 haben benachbarte `float` genau den Abstand $\varepsilon_{\mathrm M}$, und so weit liegen die beiden Ergebnisse auseinander:

```console
>>> 1.4142135623730951 - 1.414213562373095
2.220446049250313e-16
```

Die beiden Wege landen also auf benachbarten `float`, eine kleinste Stufe voneinander entfernt. Jeder Durchgang des Rezepts rundet mehrmals, und die Rundungsfehler lassen es eine Stufe neben dem `float` zur Ruhe kommen, der $\sqrt2$ am nächsten liegt.

⁠**Kurz gesagt:** $\varepsilon_{\mathrm M}=2^{-52}$ ist der Abstand von 1 zum nächsten `float`; jede Rundung ändert eine Zahl um höchstens den Bruchteil $\varepsilon_{\mathrm M}/2$ ihres Betrags.

### Die Absorption

<span class="anker" id="stufe-5-3"></span>

In der Mathematik ist $(a+b)-a=b$. Mit `float` kann dabei etwas ganz anderes herauskommen, wenn $a$ und $b$ sehr verschieden groß sind.

**Ein Sandkorn auf einer Waage für Lastwagen.** Legt man ein Sandkorn auf eine Waage, die in Schritten von 10 kg anzeigt, ändert sich die Anzeige nicht. Das Sandkorn ist da, aber die Waage kann es nicht darstellen.

:::definition Definition 5.4 (Absorption)
<span class="anker" id="satz-5-4"></span>

Ist $|b|$ kleiner als der halbe Abstand der `float` in der Nähe von $a$, dann ergibt $a+b$ wieder $a$: Der kleine Summand geht vollständig verloren. Man sagt, er wird __absorbiert__.
:::

::::beispiel
Bei $10^{16}$ ist der Abstand 2, und 1 ist genau der halbe Abstand. Der Gleichstand wird zur geraden Mantisse gerundet, und das ist $10^{16}$ selbst:

```console
>>> 1e16 + 1 - 1e16
0.0
>>> 1e16 - 1e16 + 1
1.0
```

Dieselben drei Zahlen, in anderer Reihenfolge verknüpft, liefern verschiedene Ergebnisse. Mit `float` gilt das Assoziativgesetz der Addition also nicht: Es kommt darauf an, was man zuerst rechnet. Wer viele kleine Werte zu einem großen addiert, sollte die kleinen zuerst zusammenzählen.
::::

⁠**Kurz gesagt:** Ein Summand, der kleiner ist als der halbe Abstand der `float` beim anderen Summanden, verschwindet beim Addieren.

### Die Auslöschung

<span class="anker" id="stufe-5-4"></span>

Zieht man zwei fast gleiche Zahlen voneinander ab, um eine kleine Differenz zu bekommen, kann das Ergebnis viel ungenauer sein als die beiden Zahlen. So wiegt man einen Brief schlecht, indem man sich einmal mit und einmal ohne ihn auf die Personenwaage stellt: Zwei große, leicht ungenaue Anzeigen ergeben einen kleinen, sehr ungenauen Unterschied.

**Die vorderen Ziffern heben sich auf.** $1{,}0000000000000011$ minus $1$: Die vorderen 15 Nachkommastellen sind gleich und verschwinden. Übrig bleiben nur die hintersten Stellen, und genau in denen steckt der Rundungsfehler der Eingabe.

:::definition Definition 5.5 (Auslöschung)
<span class="anker" id="satz-5-5"></span>

__Auslöschung__ heißt der Verlust gültiger Stellen beim Subtrahieren zweier fast gleicher Zahlen, die schon mit Rundungsfehlern behaftet sind. Die Subtraktion selbst ist dabei oft exakt; die vorhandenen Fehler werden aber relativ zum kleinen Ergebnis groß.
:::

::::beispiel
$1+10^{-15}$ wird beim Speichern auf ein Vielfaches von $2^{-52}$ gerundet. Zieht man 1 wieder ab, sieht man genau diese Rundung:

```console
>>> (1 + 1e-15) - 1
1.1102230246251565e-15
```

Das Ergebnis müsste $10^{-15}$ sein, ist aber um 11 % zu groß. Der Fehler beim Speichern von $1+10^{-15}$ war winzig, relativ zu 1 etwa $10^{-16}$. Relativ zum Ergebnis $10^{-15}$ ist derselbe Fehler aber riesig. Von den 16 gültigen Stellen ist nach dem Abziehen nur noch eine richtig.
::::

⁠**Kurz gesagt:** Beim Abziehen fast gleicher, gerundeter Zahlen bleiben nur die fehlerhaften hinteren Stellen übrig.

### Der Überlauf: `inf`

<span class="anker" id="stufe-5-5"></span>

Das Exponentenfeld hat 11 Bit, der größte Exponent ist 1023. Was passiert, wenn ein Ergebnis größer wird als der größte `float`?

**Ein Wert für „zu groß“.** IEEE 754 hat dafür einen eigenen Wert reserviert: unendlich. Er steht mit dem Exponentenfeld $c=2047$ und dem Mantissenfeld 0 im Speicher.

:::definition Definition 5.6 (Überlauf und `inf`)
<span class="anker" id="satz-5-6"></span>

Der größte `float` ist $(2-2^{-52})\cdot2^{1023}\approx1{,}797\cdot10^{308}$. Ist das gerundete Ergebnis einer Rechnung größer, spricht man vom __Überlauf__, und das Ergebnis ist der besondere Wert `inf` (unendlich), bei negativen Ergebnissen `-inf`.
:::

::::beispiel
Auch eine zu große Zahl im Quelltext wird zu `inf`. Mit `inf` rechnet Python weiter wie mit $\infty$:

```console
>>> 1e308 * 10
inf
>>> 1e309
inf
>>> -1e309
-inf
>>> 1e309 + 1
inf
>>> 1 / 1e309
0.0
```

Die Potenz `**` verhält sich anders: Sie meldet bei einem Überlauf die Ausnahme `OverflowError`, statt `inf` zu liefern. Die Beschreibung stammt vom Betriebssystem und lautet unter Windows `(34, 'Result too large')`, unter Linux `(34, 'Numerical result out of range')`:

```console
>>> 2.0 ** 1024
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    2.0 ** 1024
    ~~~~^^~~~~~
OverflowError: (34, 'Numerical result out of range')
```
::::

⁠**Kurz gesagt:** Ergebnisse über $1{,}797\cdot10^{308}$ werden zu `inf`; mit `inf` rechnet Python wie mit $\infty$ weiter, nur `**` meldet einen `OverflowError`.

:::hintergrund Am anderen Ende: was mit sehr kleinen Zahlen passiert
Der kleinste gewöhnliche `float` ist $2^{-1022}\approx2{,}2\cdot10^{-308}$. Darunter wäre ohne Vorkehrung sofort Schluss, und zwischen 0 und $2^{-1022}$ klaffte eine Lücke wie zwischen 0 und $0{,}5$ in Abb. [6](gleitkommazahlen-der-typ-float.html#abb-6). IEEE 754 füllt diese Lücke mit dem Exponentenfeld $c=0$: Dann fehlt die führende 1 der Mantisse, und die Zahlen liegen in gleichen Abständen von $2^{-1074}$ bis hinunter zur 0. Sie haben weniger gültige Stellen, je näher sie der 0 kommen; dafür sinkt ein Ergebnis allmählich gegen 0, statt plötzlich auf 0 zu fallen. Der kleinste positive `float` ist $2^{-1074}\approx4{,}9\cdot10^{-324}$, und Python zeigt ihn als `5e-324`. Ein Ergebnis, das höchstens halb so groß ist, wird zu 0: `1e-300 * 1e-300` ergibt `0.0`. Auch die Null selbst hat das Exponentenfeld $c=0$, mit Mantissenfeld 0, und es gibt sie mit beiden Vorzeichen, `0.0` und `-0.0`; beim Vergleichen gelten beide als gleich.
:::

### Das ungültige Ergebnis: `nan`

<span class="anker" id="stufe-5-6"></span>

Was ist $\infty-\infty$? Darauf gibt es keine sinnvolle Zahl als Antwort. Trotzdem soll eine lange Rechnung an dieser Stelle nicht einfach stehen bleiben.

**Ein Platzhalter für „keine Zahl“.** IEEE 754 reserviert dafür einen zweiten besonderen Wert: Exponentenfeld $c=2047$ und ein Mantissenfeld ungleich 0.

:::definition Definition 5.7 (`nan`)
<span class="anker" id="satz-5-7"></span>

`nan` (englisch *not a number*, keine Zahl) ist der `float`, den eine Rechnung ohne sinnvolles Ergebnis liefert, etwa $\infty-\infty$ oder $0\cdot\infty$. Fast jede Rechnung mit `nan` ergibt wieder `nan`.
:::

::::beispiel
Zwei Rechnungen ohne sinnvolles Ergebnis, dann eine, die das `nan` weiterreicht:

```console
>>> 1e309 - 1e309
nan
>>> 0 * 1e309
nan
>>> 1e309 - 1e309 + 1
nan
```

Ein `nan` am Ende einer langen Rechnung zeigt an, dass irgendwo unterwegs etwas Ungültiges passiert ist, auch wenn man nicht mehr sieht, wo.
::::

⁠**Kurz gesagt:** `nan` ist das Ergebnis ungültiger Rechnungen und steckt jede weitere Rechnung an.

:::hintergrund Warum es `inf` und `nan` gibt, und warum Python bei der Division durch null trotzdem abbricht
Ohne besondere Werte müsste ein Rechner bei jedem Überlauf und jeder ungültigen Operation das Programm anhalten. Bei einer Simulation, die eine Million Werte berechnet, wäre das oft die schlechteste Lösung: Ein einziger ungültiger Wert würde alle anderen mitreißen. IEEE 754 lässt die Rechnung deshalb mit `inf` oder `nan` weiterlaufen, und das Programm kann am Ende prüfen, welche Ergebnisse brauchbar sind. Nach der Norm wäre auch $1/0$ einfach $\infty$ und $0/0$ einfach `nan`.

Python weicht hier ab: Für `/`, `//` und `%` durch null meldet es immer einen `ZeroDivisionError`, auch bei `float`. Das hat einen praktischen Vorteil: Eine Division durch null ist in einem gewöhnlichen Programm meist ein Fehler, und die Ausnahme zeigt mit ihrem Traceback sofort, wo er steckt; ein stilles `inf` würde ihn erst viele Zeilen später sichtbar machen.
:::

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-7"></span>

:::aufgabe Aufgabe 17 ★★ Die Maschinengenauigkeit selbst finden
<span class="anker" id="aufg-17"></span>

Suche im interaktiven Modus die kleinste Zweierpotenz $2^{-k}$, für die `1.0 + 2 ** -k` nicht mehr `1.0` ergibt. Beginne bei $k=50$ und erhöhe $k$ mit der Pfeiltaste schrittweise. Erkläre, warum gerade bei diesem $k$ die Grenze liegt, und warum bei $k=53$ das Ergebnis `1.0` ist, obwohl $2^{-53}$ nicht 0 ist.

:::loesung
```console
>>> 1.0 + 2 ** -50
1.0000000000000009
>>> 1.0 + 2 ** -51
1.0000000000000004
>>> 1.0 + 2 ** -52
1.0000000000000002
>>> 1.0 + 2 ** -53
1.0
```

Die kleinste Zweierpotenz, die 1 noch verändert, ist $2^{-52}$, also $k=52$. Sie ist genau der Abstand von 1 zum nächsten `float`, die Maschinengenauigkeit. Bei $k=53$ liegt $1+2^{-53}$ exakt in der Mitte zwischen 1 und $1+2^{-52}$. Bei Gleichstand wird zur geraden Mantisse gerundet, und das Mantissenfeld von 1 ist 0, also gerade. Deshalb kommt 1 heraus, obwohl $2^{-53}\ne0$ ist. Jede noch kleinere Zweierpotenz liegt erst recht näher an 1.
:::
:::

:::aufgabe Aufgabe 18 ★★ Eine Zeitachse aufbauen
<span class="anker" id="aufg-18"></span>

Eine Stoppuhr-App soll alle $0{,}1$ s die Zeit anzeigen, also die Zeitpunkte $t_k=k\cdot0{,}1\,\mathrm{s}$ erzeugen. Weg A addiert immer wieder `0.1` zum letzten Zeitpunkt, Weg B rechnet `k * 0.1` direkt aus.

<ol class="al">

<li>

Rechne mit beiden Wegen $t_3$ und $t_8$ aus (Weg A mit `_ + 0.1` im interaktiven Modus).

</li>

<li>

Welcher Weg ist genauer, und warum? Wie viele Rundungen stecken in $t_k$ bei Weg A, wie viele bei Weg B?

</li>

</ol>

:::loesung
(a) Weg A im interaktiven Modus, Weg B direkt:

```console
>>> 0.1
0.1
>>> _ + 0.1
0.2
>>> _ + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
0.7999999999999999
>>> 8 * 0.1
0.8
```

Für $t_3$ liefern beide Wege denselben `float`, für $t_8$ nicht: Weg A ergibt $0{,}7999999999999999\,\mathrm s$, Weg B $0{,}8\,\mathrm s$. Die lange Summe in einer Zeile rechnet von links nach rechts genau wie das wiederholte `_ + 0.1`.

(b) Weg B ist genauer. In $t_k$ von Weg A stecken der Darstellungsfehler von `0.1` und $k-1$ gerundete Additionen; die Fehler können sich summieren und wachsen mit $k$. Bei Weg B sind es der Darstellungsfehler und eine einzige Rundung, der Fehler bleibt relativ immer unter etwa $2\varepsilon_{\mathrm M}$. Gute Programme berechnen Zeitpunkte deshalb aus der Schrittnummer, nicht durch Aufsummieren.
:::
:::

:::aufgabe Aufgabe 19 ★ Absorption oder Auslöschung?
<span class="anker" id="aufg-19"></span>

Sage für jeden Ausdruck das Ergebnis vorher und ordne es einem der beiden Effekte zu. Prüfe dann am Rechner.

<ol class="al">

<li>

`1e20 + 1000 - 1e20`

</li>

<li>

`(1 + 1e-10) - 1`

</li>

<li>

`1e20 - 1e20 + 1000`

</li>

<li>

`(2 ** 53 + 1.0) - 2 ** 53`

</li>

</ol>

:::loesung
```console
>>> 1e20 + 1000 - 1e20
0.0
>>> (1 + 1e-10) - 1
1.000000082740371e-10
>>> 1e20 - 1e20 + 1000
1000.0
>>> (2 ** 53 + 1.0) - 2 ** 53
0.0
```

(a) Absorption: Bei $10^{20}$ ist der Abstand der `float` $2^{-52}\cdot2^{66}=16384$, denn $2^{66}\le10^{20}<2^{67}$. 1000 ist weniger als der halbe Abstand und geht verloren. (b) Auslöschung: $1+10^{-10}$ wird beim Speichern um bis zu $1{,}1\cdot10^{-16}$ verfälscht; nach dem Abziehen der 1 ist das ein relativer Fehler von etwa $8\cdot10^{-8}$ am Ergebnis $10^{-10}$, nur noch sieben richtige Stellen. (c) Kein Effekt: Zuerst wird exakt 0 gerechnet, dann 1000 addiert. (d) Absorption: $2^{53}+1$ liegt genau in der Mitte zwischen $2^{53}$ und $2^{53}+2$ und wird zur geraden Mantisse, also zu $2^{53}$, gerundet.
:::
:::

:::aufgabe Aufgabe 20 ★ Grenzfälle
<span class="anker" id="aufg-20"></span>

Sage vorher, was Python anzeigt: (a) `1e308 + 1e308`, (b) `-1e309 * 2`, (c) `1e309 * 0`, (d) `1e-320 / 1e10`, (e) `1.0 / 0`. Ordne jedes Ergebnis einem Unterabschnitt dieses Abschnitts zu.

:::loesung
```console
>>> 1e308 + 1e308
inf
>>> -1e309 * 2
-inf
>>> 1e309 * 0
nan
>>> 1e-320 / 1e10
0.0
>>> 1.0 / 0
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    1.0 / 0
    ~~~~^~~
ZeroDivisionError: division by zero
```

(a) Überlauf, Unterabschnitt [5.5](#stufe-5-5): $2\cdot10^{308}$ ist größer als der größte `float`. (b) Rechnen mit `-inf`, ebenfalls Unterabschnitt [5.5](#stufe-5-5). (c) $\infty\cdot0$ hat keine sinnvolle Antwort: `nan`, Unterabschnitt [5.6](#stufe-5-6). (d) $10^{-330}$ liegt unter dem kleinsten positiven `float` $4{,}9\cdot10^{-324}$ und wird zu 0, Hintergrund in Unterabschnitt [5.5](#stufe-5-5). (e) Python meldet bei der Division durch null eine Ausnahme statt `inf`, Hintergrund in Unterabschnitt [5.6](#stufe-5-6); unter Python 3.13 lautet die Beschreibung `float division by zero`.
:::
:::
