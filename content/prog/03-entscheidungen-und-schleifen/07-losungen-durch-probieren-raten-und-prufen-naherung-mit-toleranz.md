---
title: Lösungen durch Probieren: Raten und Prüfen, Näherung mit Toleranz
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Kapitel 3: Entscheidungen und Schleifen
order: 6040700
summary: Mit Bedingungen und Schleifen kann ein Programm Gleichungen lösen, für die es keine Lösungsformel kennt: Es probiert Kandidaten durch und prüft jeden.
tags: Raten und Prüfen, erschöpfende Suche, Näherung, Schrittverfahren
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Mit Bedingungen und Schleifen kann ein Programm Gleichungen lösen, für die es keine Lösungsformel kennt: Es probiert Kandidaten durch und prüft jeden. Dieser Abschnitt zeigt den einfachsten Weg dazu am Beispiel der Quadratwurzel, bei der man jedes Ergebnis leicht kontrollieren kann, und zeigt, warum er für genaue Ergebnisse viel zu langsam ist.
:::

### Raten und Prüfen

<span class="anker" id="stufe-6-1"></span>

Gesucht ist die Wurzel einer ganzen Zahl, etwa von 49. Wer keine Formel kennt, kann trotzdem jede Zahl daraufhin prüfen, ob sie mit sich selbst multipliziert 49 ergibt.

**Ein Zahlenschloss.** Bei einem Zahlenschloss mit drei Ziffern kann man alle Kombinationen von 000 bis 999 der Reihe nach probieren. Spätestens nach 1000 Versuchen ist es offen, oder man weiß, dass keine Kombination passt.

:::definition Definition 6.1 (Raten und Prüfen)
<span class="anker" id="satz-6-1"></span>

__Raten und Prüfen__, auch __erschöpfende Suche__ genannt, geht die möglichen Lösungen in einer festen Reihenfolge durch und prüft jede. Es hört auf, sobald ein Kandidat passt oder feststeht, dass keiner der übrigen mehr passen kann.
:::

::::beispiel die ganzzahlige Wurzel
Die Kandidaten sind $g=0,1,2,\ldots$. Solange $g^2<a$ ist, kann $g$ nicht die Wurzel sein, und die Schleife geht zum nächsten. Sie endet beim ersten $g$ mit $g^2\ge a$, und dann gibt es zwei Fälle: Entweder ist $g^2=a$, dann ist $g$ die Wurzel, oder $g^2>a$, dann hat $a$ keine ganzzahlige Wurzel, denn alle kleineren Kandidaten hatten $g^2<a$, und alle größeren haben erst recht $g^2>a$.

```python wurzel_raten.py
# Ganzzahlige Quadratwurzel durch Raten und Prüfen: g = 0, 1, 2, ... bis g*g mindestens a ist
a = int(input("Ganze Zahl a ab 0: "))
g = 0
while g * g < a:
    g = g + 1
if g * g == a:
    print("Wurzel:", g, "nach", g, "Schritten")
else:
    print(a, "hat keine ganzzahlige Wurzel, geprüft bis", g)
```

```console Linux
$ python3 wurzel_raten.py
Ganze Zahl a ab 0: 49
Wurzel: 7 nach 7 Schritten
$ python3 wurzel_raten.py
Ganze Zahl a ab 0: 50
50 hat keine ganzzahlige Wurzel, geprüft bis 8
```

Die Schleife endet sicher, denn $g$ wächst in jedem Durchlauf um 1, und irgendwann ist $g^2\ge a$. Wie lange das dauert, ist die Schwäche des Verfahrens: Die Zahl der Schritte ist die kleinste ganze Zahl $g$ mit $g^2\ge a$, also etwa $\sqrt a$. Für $a=10^{12}$ sind das eine Million Schritte; mit jeden zwei Stellen mehr in $a$ wird es zehnmal so lange.
::::

⁠**Kurz gesagt:** Raten und Prüfen findet sicher eine Lösung oder zeigt, dass es keine gibt, braucht aber so viele Schritte, wie es Kandidaten gibt.

### Die Näherung mit Toleranz

<span class="anker" id="stufe-6-2"></span>

Für $\sqrt2$ versagt das Raten, denn $\sqrt2$ ist keine ganze Zahl, nicht einmal ein Bruch. Es gibt auch keinen `float`, dessen Quadrat genau 2 ist; selbst der eingebaute Wert erfüllt die Gleichung nicht:

```console
>>> import math
>>> math.sqrt(2) ** 2
2.0000000000000004
>>> math.sqrt(2) ** 2 == 2
False
```

Eine Schleife, die auf `g * g == 2` wartet, würde deshalb nie enden.

**Eine Zielscheibe.** Beim Zielschießen zählt ein Treffer, wenn er im inneren Ring liegt, nicht erst, wenn er genau die Mitte trifft. Genauso gibt man sich mit einer Zahl $g$ zufrieden, deren Quadrat nahe genug an $a$ liegt.

:::definition Definition 6.2 (Näherung mit Toleranz)
<span class="anker" id="satz-6-2"></span>

Eine Zahl $g$ ist eine __Näherung__ von $\sqrt a$ mit der Toleranz $\varepsilon>0$, wenn $|g^2-a|<\varepsilon$ ist. Die Toleranz $\varepsilon$ legt fest, wie genau „nahe genug“ ist; sie ist eine frei gewählte Zahl und hat nichts mit der Maschinengenauigkeit $\varepsilon_{\mathrm M}$ zu tun.
:::

Das einfachste Verfahren, eine solche Näherung zu finden, heißt hier __Schrittverfahren__: Man beginnt bei $g=0$ und erhöht $g$ in festen Schritten der Schrittweite $h$, bis $|g^2-a|<\varepsilon$ ist.

::::beispiel
$\sqrt{25}$ mit $\varepsilon=0{,}01$ und der Schrittweite $h=0{,}0001$. Die Schleife hat eine zweite Bedingung: Sie hört auch auf, wenn $g^2$ schon über $a$ liegt, denn dann kann kein weiterer Schritt mehr treffen.

```python wurzel_schritte.py
# Quadratwurzel in kleinen Schritten suchen, bis g*g nahe genug an a liegt
a = 25.0                                  # Zahl, deren Wurzel gesucht ist
eps = 0.01                                # Toleranz für |g*g - a|
h = float(input("Schrittweite h = "))
g = 0.0
schritte = 0
while abs(g * g - a) >= eps and g * g <= a:
    g = g + h
    schritte = schritte + 1
if abs(g * g - a) < eps:
    print("Näherung:", g, "nach", schritte, "Schritten")
else:
    print("übersprungen: g =", g, "nach", schritte, "Schritten")
```

```console Linux
$ python3 wurzel_schritte.py
Schrittweite h = 0.0001
Näherung: 4.999000000001688 nach 49990 Schritten
```

Die Schleife hält beim ersten $g$, dessen Quadrat über $25-0{,}01=24{,}99$ liegt; das ist $g=4{,}999$. Angezeigt wird `4.999000000001688`, weil $g$ durch fast 50 000 Additionen entstanden ist, von denen jede gerundet wurde, wie bei der Gleitkomma-Falle in Unterabschnitt [3.3](wiederholen-mit-while.html#stufe-3-3).
::::

⁠**Kurz gesagt:** Mit Gleitkommazahlen sucht man keine exakte Lösung, sondern eine, die eine Toleranz einhält.

### Schrittweite und Toleranz

<span class="anker" id="stufe-6-3"></span>

Das Schrittverfahren hat zwei Stellschrauben, $h$ und $\varepsilon$, und sie hängen zusammen.

**Ein schmaler Graben.** Die Werte von $g$, die die Toleranz einhalten, bilden einen schmalen Bereich um $\sqrt a$, wie einen Graben auf einem Weg. Wer mit großen Schritten geht, kann über den Graben hinwegtreten, ohne je hineinzufallen.

Wie breit ist der Bereich? Aus $g^2-a=(g-\sqrt a)(g+\sqrt a)$ und $g+\sqrt a\approx2\sqrt a$ in der Nähe der Lösung folgt: $|g^2-a|<\varepsilon$ heißt ungefähr $|g-\sqrt a|<\varepsilon/(2\sqrt a)$. Der Bereich ist also etwa $\varepsilon/\sqrt a$ breit, für $a=25$ und $\varepsilon=0{,}01$ von 4,999 bis 5,001.

::::beispiel ein zu großer Schritt
Mit $h=0{,}003$ liegen die Kandidaten bei …, 4,998, 5,001, …. Das Quadrat des ersten ist 24,980, das des zweiten 25,010; beide liegen außerhalb der Toleranz:

```console Linux
$ python3 wurzel_schritte.py
Schrittweite h = 0.003
übersprungen: g = 5.0010000000000785 nach 1667 Schritten
```

Ohne die zweite Bedingung `g * g <= a` liefe die Schleife hier endlos weiter, immer weiter von der Lösung weg.
::::

**Die Kosten.** Die Schrittweite darf also höchstens so groß sein wie der Bereich, $h\lesssim\varepsilon/\sqrt a$, und dann braucht das Verfahren etwa $\sqrt a/h\gtrsim a/\varepsilon$ Schritte. Für $\sqrt{25}$ mit $\varepsilon=0{,}01$ sind das einige Tausend bis Zehntausende, das geht in Sekundenbruchteilen. Für $\sqrt2$ auf zwölf Stellen, $\varepsilon=10^{-12}$, sind es etwa $2\cdot10^{12}$ Schritte. Eine Python-Schleife schafft auf einem üblichen Rechner grob zehn Millionen einfache Durchläufe in der Sekunde; das ergibt $2\cdot10^5$ s, mehr als zwei Tage. Wie man in 41 Schritten auf zwölf Stellen kommt, zeigt Abschnitt [7](die-bisektion.html#stufe-7).

⁠**Kurz gesagt:** Die Schrittweite muss kleiner sein als der Bereich, den die Toleranz zulässt, und deshalb wächst die Schrittzahl mit $a/\varepsilon$.

:::hintergrund Warum eine Toleranz nötig ist, auch für die beste Gleitkommazahl
Zwischen 1 und 2 liegen benachbarte `float` im Abstand $\varepsilon_{\mathrm M}=2^{-52}$ ([Kapitel 2, Abschnitt 5.2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-2)). $\sqrt2$ liegt zwischen zwei von ihnen, `1.414213562373095` und `1.4142135623730951`. Ihre Quadrate sind, gerundet auf den nächsten `float`, `1.9999999999999996` und `2.0000000000000004`; keiner der beiden Werte ist 2. Für jeden anderen `float` liegt das Quadrat noch weiter weg. Die Gleichung $g^2=2$ hat unter den `float` also keine Lösung, und die kleinste erreichbare Abweichung ist $4{,}44\cdot10^{-16}$. Jede Schleife, die eine Wurzel sucht, braucht deshalb eine Toleranz, und diese muss größer sein als die Abweichung, die mit `float` überhaupt erreichbar ist.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-4"></span>

:::aufgabe Aufgabe 24 ★★ Die ganzzahlige Kubikwurzel
<span class="anker" id="aufg-24"></span>

Schreibe ein Skript `kubikwurzel.py`, das zu einer ganzen Zahl $k$ durch Raten und Prüfen die ganzzahlige Kubikwurzel sucht, also ein ganzes $g$ mit $g^3=k$, oder meldet, dass es keine gibt. Auch negative Zahlen sollen gehen. Tipp: Suche die Wurzel von $|k|$ und gib ihr danach das Vorzeichen von $k$. Teste mit 27, $-8$ und 10.

:::loesung
```python kubikwurzel.py
# Ganzzahlige Kubikwurzel durch Raten und Prüfen, auch für negative Zahlen
k = int(input("Ganze Zahl k: "))
g = 0
while g ** 3 < abs(k):
    g = g + 1
if g ** 3 == abs(k):
    if k < 0:
        g = -g
    print("Kubikwurzel:", g)
else:
    print(k, "hat keine ganzzahlige Kubikwurzel")
```

```console Linux
$ python3 kubikwurzel.py
Ganze Zahl k: 27
Kubikwurzel: 3
$ python3 kubikwurzel.py
Ganze Zahl k: -8
Kubikwurzel: -2
$ python3 kubikwurzel.py
Ganze Zahl k: 10
10 hat keine ganzzahlige Kubikwurzel
```

Für negative $k$ ist $(-g)^3=-g^3$; die Wurzel von $|k|$ mit umgekehrtem Vorzeichen ist also die gesuchte. Bei 10 endet die Suche bei $g=3$ mit $27>10$, und kein kleinerer Kandidat hatte gepasst.
:::
:::

:::aufgabe Aufgabe 25 ★★ Die Schrittweite für $\sqrt{10}$
<span class="anker" id="aufg-25"></span>

Ändere `wurzel_schritte.py` so, dass es $\sqrt{10}$ mit $\varepsilon=0{,}01$ sucht. Probiere die Schrittweiten 0,001, 0,003, 0,004 und 0,005. Welche treffen die Toleranz, wie viele Schritte brauchen sie? Schätze vorher die Breite des zulässigen Bereichs für $g$ ab und erkläre damit die Ergebnisse.

:::loesung
Die zulässigen $g$ liegen zwischen $\sqrt{9{,}99}\approx3{,}16070$ und $\sqrt{10{,}01}\approx3{,}16386$; der Bereich ist etwa 0,0032 breit, wie die Abschätzung $\varepsilon/\sqrt{10}=0{,}0032$ sagt. Schrittweiten bis zu dieser Breite treffen sicher, größere nur mit Glück.

```console Linux
$ python3 schritte10.py
Schrittweite h = 0.001
Näherung: 3.160999999999763 nach 3161 Schritten
$ python3 schritte10.py
Schrittweite h = 0.003
Näherung: 3.162000000000009 nach 1054 Schritten
$ python3 schritte10.py
Schrittweite h = 0.004
übersprungen: g = 3.1640000000000024 nach 791 Schritten
$ python3 schritte10.py
Schrittweite h = 0.005
übersprungen: g = 3.1649999999999547 nach 633 Schritten
```

Mit $h=0{,}004$ springen die Kandidaten von 3,160 auf 3,164; der erste liegt knapp unter, der zweite knapp über dem Bereich. Mit $h=0{,}005$ ebenso, von 3,160 auf 3,165. Das Skript `schritte10.py` ist `wurzel_schritte.py` mit `a = 10.0`.
:::
:::

:::aufgabe Aufgabe 26 ★ Wie lange das Raten dauert
<span class="anker" id="aufg-26"></span>

Wie viele Schritte braucht `wurzel_raten.py` für $a=10^{14}$ und für $a=10^{20}$? Wie lange dauert das ungefähr bei zehn Millionen Durchläufen je Sekunde? Miss für $a=10^{14}$ nach, wenn du Geduld hast.

:::loesung
`wurzel_raten.py` braucht etwa $\sqrt a$ Schritte: für $a=10^{14}$ zehn Millionen, für $a=10^{20}$ zehn Milliarden. Bei zehn Millionen Durchläufen je Sekunde ist das eine Sekunde beziehungsweise 1000 s, also etwa eine Viertelstunde. Auf dem Rechner, mit dem dieses Kapitel geprüft wurde, brauchte $a=10^{14}$ gut eine Sekunde (zwischen 1,1 s und 1,6 s, je nach System). Je zwei Stellen mehr in $a$ verzehnfachen die Zeit.
:::
:::
