---
title: Schleifen steuern, verschachteln und Ergebnisse sammeln
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
knoten: Python 3: Entscheidungen und Schleifen
order: 6040600
summary: Eine Schleife muss nicht jeden Durchlauf vollständig ausführen und nicht immer bis zum Ende laufen.
tags: verschachtelt, Akkumulator
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Eine Schleife muss nicht jeden Durchlauf vollständig ausführen und nicht immer bis zum Ende laufen. Dieser Abschnitt zeigt, wie man eine Schleife vorzeitig verlässt oder einen Durchlauf überspringt, wie man Schleifen ineinander setzt und wie man in einer Schleife ein Ergebnis aufsammelt, etwa eine Summe.
:::

### Abbrechen mit `break`

<span class="anker" id="stufe-5-1"></span>

Eine Suche soll aufhören, sobald sie etwas gefunden hat. Die Bedingung der Schleife kann das oft nicht ausdrücken, weil der Fund erst mitten im Block feststeht.

**Wer den Schlüssel gefunden hat, sucht nicht weiter.** Wer Schubladen der Reihe nach nach einem Schlüssel durchsucht, öffnet nach dem Fund keine weitere mehr, auch wenn noch Schubladen übrig sind.

:::definition Definition 5.1 (`break`)
<span class="anker" id="satz-5-1"></span>

Die Anweisung `break` im Block einer Schleife beendet diese Schleife sofort. Der Rest des Blocks wird übersprungen, ebenso alle weiteren Durchläufe, und das Programm geht mit der ersten Zeile nach der Schleife weiter.
:::

**Beispiel: der kleinste Teiler.** Eine ganze Zahl $n\ge2$ ist eine Primzahl, wenn sie außer 1 und sich selbst keinen Teiler hat. Das Skript probiert die möglichen Teiler $t=2,3,\ldots$ der Reihe nach durch; beim ersten, der $n$ ohne Rest teilt, bricht es ab. Der Name `teiler` ist anfangs an `None` gebunden, das heißt hier „noch keiner gefunden“ ([Programmieren, Python 2, Abschnitt 7.6](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-6)).

```python kleinster_teiler.py
# Den kleinsten Teiler einer ganzen Zahl n ab 2 suchen; ohne Teiler ist n eine Primzahl
n = int(input("Ganze Zahl ab 2: "))
teiler = None
t = 2
while t * t <= n:
    if n % t == 0:
        teiler = t
        break
    t = t + 1
if teiler is None:
    print(n, "ist eine Primzahl")
else:
    print(n, "=", teiler, "*", n // teiler)
```

```console Linux
$ python3 kleinster_teiler.py
Ganze Zahl ab 2: 91
91 = 7 * 13
$ python3 kleinster_teiler.py
Ganze Zahl ab 2: 97
97 ist eine Primzahl
```

Die Bedingung `t * t <= n` begrenzt die Suche auf Teiler bis $\sqrt n$. Das genügt: Ist $n=t\cdot s$ mit $t\le s$, dann ist $t\cdot t\le t\cdot s=n$. Jede zusammengesetzte Zahl hat also einen Teiler, der höchstens $\sqrt n$ ist. Bei 97 prüft das Skript nur $t=2$ bis 9 statt 2 bis 96.

⁠**Kurz gesagt:** `break` beendet eine Schleife sofort, typisch nach einem Fund.

:::hintergrund `else` an einer Schleife: der Fall „kein `break`“
Auch eine Schleife darf einen `else`-Block haben, so weit eingerückt wie ihre Kopfzeile. Er läuft, wenn die Schleife regulär endet, also bei `while` weil die Bedingung falsch wurde und bei `for` nach dem letzten Wert, aber nicht, wenn `break` sie beendet hat. Damit braucht die Suche nach dem kleinsten Teiler keinen eigenen Namen für „gefunden“:

```python teiler_else.py
# Dieselbe Suche mit else an der Schleife: der else-Block läuft nur, wenn kein break kam
n = int(input("Ganze Zahl ab 2: "))
t = 2
while t * t <= n:
    if n % t == 0:
        print(n, "=", t, "*", n // t)
        break
    t = t + 1
else:
    print(n, "ist eine Primzahl")
```

```console Linux
$ python3 teiler_else.py
Ganze Zahl ab 2: 91
91 = 7 * 13
$ python3 teiler_else.py
Ganze Zahl ab 2: 97
97 ist eine Primzahl
```

Das Wort `else` führt hier leicht in die Irre, denn es hat nichts mit der Bedingung der Schleife zu tun. Man liest es am besten als „kein `break`“: Der Block läuft, wenn die Suche nichts gefunden hat. Viele Programmierer kennen diese Form nicht; ein Name wie `teiler` mit dem Startwert `None` ist für die meisten Leser verständlicher.
:::

### Überspringen mit `continue`

<span class="anker" id="stufe-5-2"></span>

Manchmal soll eine Schleife einzelne Werte auslassen, aber danach weiterlaufen, etwa einen defekten Messkanal.

**Ein Gerät mit Defektaufkleber.** Wer eine Reihe von Messgeräten prüft, übergeht ein Gerät mit Defektaufkleber und macht mit dem nächsten weiter. Die Prüfung der Reihe hört dabei nicht auf, nur dieses eine Gerät fällt aus.

:::definition Definition 5.2 (`continue`)
<span class="anker" id="satz-5-2"></span>

Die Anweisung `continue` im Block einer Schleife beendet nur den laufenden Durchlauf. Der Rest des Blocks wird übersprungen. Eine `for`-Schleife macht mit dem nächsten Wert weiter, eine `while`-Schleife mit der nächsten Prüfung ihrer Bedingung.
:::

**Beispiel.** Von acht Kanälen ist Kanal 3 defekt:

```python kanaele.py
# Messkanäle 0 bis 7 abfragen; Kanal 3 ist defekt und wird übersprungen
for kanal in range(8):
    if kanal == 3:
        continue
    print("messe Kanal", kanal)
print("fertig")
```

```console Linux
$ python3 kanaele.py
messe Kanal 0
messe Kanal 1
messe Kanal 2
messe Kanal 4
messe Kanal 5
messe Kanal 6
messe Kanal 7
fertig
```

Dasselbe ließe sich mit `if kanal != 3:` und dem eingerückten `print` schreiben. `continue` lohnt sich, wenn ein Durchlauf viele Zeilen hat und mehrere Gründe, ihn auszulassen: Jeder Grund bekommt eine kurze Prüfung am Anfang, und der eigentliche Block muss nicht immer tiefer eingerückt werden.

⁠**Kurz gesagt:** `continue` überspringt den Rest des laufenden Durchlaufs, die Schleife läuft weiter.

### Verschachtelte Schleifen

<span class="anker" id="stufe-5-3"></span>

Für jede Zahl prüfen, ob sie eine Primzahl ist; für jedes Paar zweier Widerstände den Gesamtwiderstand ausrechnen: Solche Aufgaben brauchen eine Wiederholung in der Wiederholung.

**Wie bei einer Uhr.** Der Minutenzeiger läuft einmal ganz herum, dann rückt der Stundenzeiger eine Stunde weiter, und der Minutenzeiger beginnt von vorn. Zwei ineinandergesetzte Schleifen arbeiten genauso. Mit einer äußeren Schleife über drei Zeilen und einer inneren über vier Spalten entsteht diese Reihenfolge der Durchläufe des inneren Blocks:

|  | Spalte 0 | Spalte 1 | Spalte 2 | Spalte 3 |
|---|---|---|---|---|
| Zeile 0 | 1 | 2 | 3 | 4 |
| Zeile 1 | 5 | 6 | 7 | 8 |
| Zeile 2 | 9 | 10 | 11 | 12 |

:::definition Definition 5.3 (Verschachtelte Schleife)
<span class="anker" id="satz-5-3"></span>

Steht eine Schleife im Block einer anderen, heißen die beiden __verschachtelt__. Die Schleife im Block heißt die innere, die andere die äußere. Bei jedem Durchlauf der äußeren Schleife läuft die innere vollständig. Hat die äußere $m$ Durchläufe und die innere jeweils $n$, läuft der Block der inneren Schleife $m\cdot n$-mal. `break` und `continue` wirken nur auf die innerste Schleife, deren Block sie enthält.
:::

**Beispiel: alle Primzahlen bis 30.** Die äußere Schleife geht die Zahlen $n$ durch, die innere sucht wie in Unterabschnitt [5.1](#stufe-5-1) einen Teiler. Das `break` verlässt nur die innere Schleife; die äußere macht mit dem nächsten $n$ weiter.

```python primzahlen.py
# Alle Primzahlen bis 30: für jede Zahl n die möglichen Teiler t durchprobieren
for n in range(2, 31):
    ist_prim = True
    t = 2
    while t * t <= n:
        if n % t == 0:
            ist_prim = False
            break             # verlässt nur die innere Schleife
        t = t + 1
    if ist_prim:
        print(n, end=" ")
print()
```

```console Linux
$ python3 primzahlen.py
2 3 5 7 11 13 17 19 23 29
```

**Beispiel: zwei Widerstände für 150 $\Omega$.** Gesucht sind zwei Widerstände aus der Reihe 100 $\Omega$, 200 $\Omega$, …, 900 $\Omega$, die parallel geschaltet $R_1R_2/(R_1+R_2)=150$ $\Omega$ ergeben. Die innere Schleife beginnt bei `r1`, damit jedes Paar nur einmal vorkommt. Das Ergebnis ist ein `float`, deshalb vergleicht das Skript mit `math.isclose`:

```python parallel_suche.py
# Zwei Widerstände aus 100, 200, ..., 900 Ohm suchen, die parallel 150 Ohm ergeben
import math
for r1 in range(100, 1000, 100):
    for r2 in range(r1, 1000, 100):          # r2 >= r1: jedes Paar nur einmal
        r_par = r1 * r2 / (r1 + r2)
        if math.isclose(r_par, 150):
            print(r1, "Ohm parallel", r2, "Ohm ergibt", r_par, "Ohm")
```

```console Linux
$ python3 parallel_suche.py
200 Ohm parallel 600 Ohm ergibt 150.0 Ohm
300 Ohm parallel 300 Ohm ergibt 150.0 Ohm
```

Hier hängt die Zahl der inneren Durchläufe vom äußeren Wert ab: neun für $R_1=100$ $\Omega$, acht für 200 $\Omega$, und so fort bis einer für 900 $\Omega$, zusammen 45 Paare statt $9\cdot9=81$.

⁠**Kurz gesagt:** In verschachtelten Schleifen läuft die innere bei jedem Durchlauf der äußeren ganz durch; `break` verlässt nur die innere.

### Das Akkumulator-Muster

<span class="anker" id="stufe-5-4"></span>

Eine Schleife soll nicht nur etwas ausgeben, sondern ein Ergebnis aus allen Durchläufen liefern: eine Summe, eine Anzahl, ein Produkt.

**Die Speichertaste.** Auf einem Taschenrechner löscht man zuerst den Speicher und drückt dann nach jedem Wert die Taste M+. Am Ende steht im Speicher die Summe aller Werte. Eine Schleife macht es genauso, nur heißt der Speicher hier `summe`.

:::definition Definition 5.4 (Akkumulator)
<span class="anker" id="satz-5-4"></span>

Ein __Akkumulator__ ist ein Name, der vor einer Schleife an einen Startwert gebunden wird und in jedem Durchlauf mit dem neuen Wert verrechnet wird, zum Beispiel mit `summe = summe + wert`. Nach der Schleife ist er an das Ergebnis gebunden. Der Startwert ist das Ergebnis für den Fall, dass die Schleife keinen einzigen Durchlauf hat: 0 für eine Summe und eine Anzahl, 1 für ein Produkt.
:::

**Beispiel: eine Summe.** Die Summe der Quadrate $1^2+2^2+\cdots+5^2$, mit dem Zwischenstand nach jedem Durchlauf:

```python quadratsumme.py
# Akkumulator: die Summe der Quadrate 1*1 + 2*2 + ... + 5*5
summe = 0                       # Startwert: die leere Summe
for i in range(1, 6):
    summe = summe + i * i
    print("i =", i, "  Summe bis hier:", summe)
print("Ergebnis:", summe)
```

```console Linux
$ python3 quadratsumme.py
i = 1   Summe bis hier: 1
i = 2   Summe bis hier: 5
i = 3   Summe bis hier: 14
i = 4   Summe bis hier: 30
i = 5   Summe bis hier: 55
Ergebnis: 55
```

Die Schleife rechnet genau die Summe aus, die man in der Mathematik mit dem Summenzeichen schreibt (Abb. [6](#abb-6)). Der Laufindex $i$ unter dem $\Sigma$ ist die Schleifenvariable, die Grenzen 1 und 5 sind die Grenzen von `range(1, 6)`, mit dem Stopp eins höher.

:::abbildung prog/k3rquadrate 6
Die Summe der Quadrate von 1 bis 5 Schritt für Schritt, so wie die Schleife in `quadratsumme.py` sie bildet: Jeder Summand ist ein Durchlauf.
:::

**Beispiel: eine Anzahl.** Ein Zähler ist ein Akkumulator, zu dem in jedem passenden Durchlauf 1 addiert wird:

```python zaehler.py
# Akkumulator als Zähler: Wie viele Zahlen von 1 bis 100 sind durch 3 oder durch 7 teilbar?
anzahl = 0
for n in range(1, 101):
    if n % 3 == 0 or n % 7 == 0:
        anzahl = anzahl + 1
print("Anzahl:", anzahl)
```

```console Linux
$ python3 zaehler.py
Anzahl: 43
```

Zur Kontrolle von Hand: Durch 3 teilbar sind 33 der Zahlen, durch 7 teilbar 14, durch beide, also durch 21, sind 4 teilbar und doppelt gezählt; $33+14-4=43$.

**Beispiel: ein Produkt.** Auf wie viele Arten lassen sich fünf Messgeräte nacheinander anschließen? Für das erste gibt es 5 Möglichkeiten, für das zweite noch 4, und so weiter, zusammen $5\cdot4\cdot3\cdot2\cdot1$. Der Startwert eines Produkts ist 1:

```python reihenfolgen.py
# Akkumulator für ein Produkt: Auf wie viele Arten lassen sich 5 Messgeräte nacheinander anschließen?
anzahl = 1                      # Startwert: das leere Produkt
for k in range(1, 6):
    anzahl = anzahl * k
print("Reihenfolgen:", anzahl)
```

```console Linux
$ python3 reihenfolgen.py
Reihenfolgen: 120
```

⁠**Kurz gesagt:** Ein Akkumulator startet vor der Schleife mit 0 (Summe, Anzahl) oder 1 (Produkt) und nimmt in jedem Durchlauf einen Wert auf.

:::hintergrund Warum die leere Summe 0 und das leere Produkt 1 ist
Der Startwert ist so gewählt, dass er das Ergebnis nicht verändert: $0+x=x$ und $1\cdot x=x$. Deshalb ist das Ergebnis nach einem Durchlauf genau der erste Wert, und es stimmt auch, wenn die Schleife gar nicht läuft, etwa bei `range(1, 1)`. Die Mathematik vereinbart aus demselben Grund, dass eine Summe ohne Summanden 0 und ein Produkt ohne Faktoren 1 ist; daher kommt auch $0!=1$ und $x^0=1$. Wählt man einen anderen Startwert, etwa 1 für eine Summe, ist jedes Ergebnis um genau diesen Wert falsch, und man merkt es oft erst spät.
:::

### Anwendung: Mittelwert und Maximum

<span class="anker" id="stufe-5-5"></span>

Zwei Auswertungen, die man am Messplatz ständig braucht, sind Akkumulatoren: der Mittelwert mehrerer Messungen und der größte Wert einer Messreihe.

**Der Mittelwert.** Der Mittelwert von $n$ Messwerten $U_1,\ldots,U_n$ ist ihre Summe geteilt durch $n$, $\bar U=\frac1n\sum_{k=1}^nU_k$. Das Skript fragt zuerst nach der Anzahl und dann nach jedem Wert; ein Akkumulator sammelt die Summe:

```python mittelwert.py
# Mittelwert mehrerer Messwerte, die man nacheinander eintippt
anzahl = int(input("Anzahl der Messwerte: "))
summe = 0.0
for k in range(anzahl):
    wert = float(input(f"Messwert {k + 1} in V: "))
    summe = summe + wert
print(f"Mittelwert: {summe / anzahl:.3f} V")
```

```console Linux
$ python3 mittelwert.py
Anzahl der Messwerte: 4
Messwert 1 in V: 4.98
Messwert 2 in V: 5.02
Messwert 3 in V: 5.01
Messwert 4 in V: 4.99
Mittelwert: 5.000 V
```

Abb. [7](#abb-7) zeigt dieselbe Rechnung mit dem Summenzeichen.

:::abbildung prog/k3rmittel 7
Der Mittelwert der vier Messwerte aus `mittelwert.py` Schritt für Schritt: Die Schleife bildet die Summe, die Division durch die Anzahl folgt nach der Schleife.
:::

**Das Maximum.** Eine Quelle mit der Leerlaufspannung $U_0$ und dem Innenwiderstand $R_\mathrm i$ treibt durch einen Lastwiderstand $R$ den Strom $I=U_0/(R+R_\mathrm i)$. Im Lastwiderstand wird die Leistung

$$P=I^2R=\frac{U_0^2\,R}{(R+R_\mathrm i)^2}$$

umgesetzt. Bei welchem $R$ ist sie am größten? Ein Akkumulator für das Maximum merkt sich den bisher größten Wert und ersetzt ihn, sobald ein größerer kommt; ein zweiter Name merkt sich, wo er auftrat. Als Startwert dient `0.0`, den jede echte Leistung übertrifft:

```python anpassung.py
# Leistungsanpassung: Bei welchem Lastwiderstand gibt eine Quelle die größte Leistung ab?
u0 = 10.0            # Leerlaufspannung der Quelle in V
r_i = 50.0           # Innenwiderstand der Quelle in Ohm
beste_r = None
beste_p = 0.0
for r in range(10, 201, 10):
    p = u0 ** 2 * r / (r + r_i) ** 2     # Leistung im Lastwiderstand in W
    if p > beste_p:
        beste_p = p
        beste_r = r
print(f"größte Leistung {beste_p:.3f} W bei R = {beste_r} Ohm")
```

```console Linux
$ python3 anpassung.py
größte Leistung 0.500 W bei R = 50 Ohm
```

Das Maximum liegt bei $R=R_\mathrm i=50$ $\Omega$ und beträgt $U_0^2/(4R_\mathrm i)=0{,}5$ W. Das ist die Leistungsanpassung aus der Elektrotechnik: Eine Quelle gibt die größte Leistung ab, wenn der Lastwiderstand gleich ihrem Innenwiderstand ist. Die Schleife hat das Maximum nur unter den 20 geprüften Widerständen gefunden; dass es zwischen zwei Rasterpunkten kein größeres gibt, zeigt erst die Rechnung.

⁠**Kurz gesagt:** Der Mittelwert ist ein Summen-Akkumulator geteilt durch die Anzahl, das Maximum ein Akkumulator, der nur bei einem größeren Wert ersetzt wird.

### Aufgaben zu Abschnitt [5](#stufe-5)

<span class="anker" id="stufe-5-6"></span>

:::aufgabe Aufgabe 19 ★ `break` und `continue` vorhersagen
<span class="anker" id="aufg-19"></span>

Was geben die beiden Schleifen aus? Erst vorhersagen, dann prüfen.

```python
for k in range(10):
    if k == 4:
        break
    print(k, end=" ")
print()
for k in range(10):
    if k % 3 == 0:
        continue
    print(k, end=" ")
print()
```

:::loesung
```console Linux
$ python3 break_continue.py
0 1 2 3
1 2 4 5 7 8
```

Die erste Schleife gibt 0 bis 3 aus und endet bei $k=4$, bevor das `print` läuft. Die zweite überspringt die Vielfachen von 3, also 0, 3, 6 und 9, und läuft sonst bis zum Ende.
:::
:::

:::aufgabe Aufgabe 20 ★★ Eine Falle mit `continue`
<span class="anker" id="aufg-20"></span>

Das folgende Skript soll die Zahlen 0 bis 7 außer 3 ausgeben, hört aber nach der 2 auf, etwas auszugeben, und endet nicht. Erkläre, warum, und behebe den Fehler, ohne die Schleife in eine `for`-Schleife umzuschreiben.

```python
k = 0
while k < 8:
    if k == 3:
        continue
    print(k)
    k = k + 1
```

:::loesung
Bei $k=3$ springt `continue` zurück zur Bedingung, bevor `k = k + 1` läuft. `k` bleibt 3, die Bedingung bleibt wahr, und `continue` kommt immer wieder: eine Endlosschleife, die nichts mehr ausgibt. Der Zähler muss auch auf dem Weg über `continue` weiterrücken:

```python continue_behoben.py
# Die Zahlen 0 bis 7 ohne die 3: vor continue muss der Zähler weiterrücken
k = 0
while k < 8:
    if k == 3:
        k = k + 1
        continue
    print(k, end=" ")
    k = k + 1
print()
```

```console Linux
$ python3 continue_behoben.py
0 1 2 4 5 6 7
```

Bei einer `for`-Schleife gibt es diese Falle nicht, weil sie den nächsten Wert selbst holt.
:::
:::

:::aufgabe Aufgabe 21 ★★ Primzahlen bis 100
<span class="anker" id="aufg-21"></span>

Ändere `primzahlen.py` so, dass es alle Primzahlen bis 100 ausgibt und am Ende zwei Zahlen meldet: wie viele Primzahlen es gefunden hat, und wie oft insgesamt der Rest `n % t` berechnet wurde. Wie oft wäre es ohne die Grenze `t * t <= n` ungefähr, wenn man jedes $t$ von 2 bis $n-1$ prüft?

:::loesung
Zwei Zähler kommen dazu: einer für die gefundenen Primzahlen, einer für jeden berechneten Rest.

```python primzahlen_100.py
# Alle Primzahlen bis 100, dazu zwei Zähler: gefundene Primzahlen und berechnete Reste
anzahl = 0
reste = 0
for n in range(2, 101):
    ist_prim = True
    t = 2
    while t * t <= n:
        reste = reste + 1
        if n % t == 0:
            ist_prim = False
            break
        t = t + 1
    if ist_prim:
        anzahl = anzahl + 1
        print(n, end=" ")
print()
print("Primzahlen:", anzahl, " berechnete Reste:", reste)
```

```console Linux
$ python3 primzahlen_100.py
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
Primzahlen: 25  berechnete Reste: 236
```

Ohne die Grenze und ohne `break`, mit jedem $t$ von 2 bis $n-1$, wären es $\sum_{n=2}^{100}(n-2)=0+1+\cdots+98=4851$ Reste, also etwa zwanzigmal so viele. Ohne die Grenze, aber mit `break` sind es 1133: Die Primzahlen selbst kosten dann am meisten, weil für sie kein früher Teiler die Suche beendet.
:::
:::

:::aufgabe Aufgabe 22 ★ Summe und Produkt
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

Berechne mit einer Schleife $1+2+\cdots+100$ und vergleiche mit der Formel $n(n+1)/2$.

</li>

<li>

Berechne $1\cdot2\cdot3\cdots20$. Warum ist das Ergebnis exakt, obwohl es 19 Stellen hat?

</li>

</ol>

:::loesung
```python summe_produkt.py
# Summe 1 + 2 + ... + 100 und Produkt 1 * 2 * ... * 20 mit Akkumulatoren
summe = 0
for i in range(1, 101):
    summe = summe + i
print("Summe:", summe, " Formel:", 100 * 101 // 2)
produkt = 1
for i in range(1, 21):
    produkt = produkt * i
print("Produkt:", produkt)
```

```console Linux
$ python3 summe_produkt.py
Summe: 5050  Formel: 5050
Produkt: 2432902008176640000
```

(a) Beide Wege liefern 5050. (b) Das Produkt ist exakt, weil alle Faktoren ganze Zahlen sind und `int` beliebig viele Stellen hat ([Programmieren, Python 2, Abschnitt 2.1](/wissen/informatik/programmieren/python/werte-typen-und-variablen/ganze-zahlen-und-rechenoperatoren.html#stufe-2-1)). Mit `float` wäre das Ergebnis über $2^{53}$ nicht mehr garantiert exakt.
:::
:::

:::aufgabe Aufgabe 23 ★★★ Ein Spannungsteiler für 3,3 V
<span class="anker" id="aufg-23"></span>

Aus 5 V sollen mit einem Spannungsteiler etwa 3,3 V werden, $U_2=5\,\mathrm V\cdot R_2/(R_1+R_2)$. Zur Verfügung stehen Widerstände von 1 $\mathrm{k\Omega}$ bis 10 $\mathrm{k\Omega}$ in Schritten von 1 $\mathrm{k\Omega}$. Schreibe ein Skript mit zwei verschachtelten Schleifen und einem Akkumulator für die kleinste Abweichung $|U_2-3{,}3\,\mathrm V|$, das das beste Paar und seine Spannung ausgibt. Warum gibt es mehrere gleich gute Paare, und welches findet dein Skript?

:::loesung
Die äußere Schleife geht $R_1$ durch, die innere $R_2$; der Akkumulator merkt sich die kleinste Abweichung und das Paar dazu. Er beginnt mit `None`, damit das erste Paar sicher übernommen wird:

```python spannungsteiler.py
# Spannungsteiler 5 V -> etwa 3.3 V aus Widerständen von 1 kOhm bis 10 kOhm
beste_abw = None
for r1 in range(1, 11):
    for r2 in range(1, 11):
        u2 = 5 * r2 / (r1 + r2)
        abw = abs(u2 - 3.3)
        if beste_abw is None or abw < beste_abw:
            beste_abw = abw
            beste_r1 = r1
            beste_r2 = r2
            beste_u2 = u2
print(f"R1 = {beste_r1} kOhm, R2 = {beste_r2} kOhm, U2 = {beste_u2:.3f} V, Abweichung {beste_abw:.3f} V")
```

```console Linux
$ python3 spannungsteiler.py
R1 = 1 kOhm, R2 = 2 kOhm, U2 = 3.333 V, Abweichung 0.033 V
```

$U_2$ hängt nur vom Verhältnis $R_2/R_1$ ab. Die Paare (2 k$\Omega$, 4 k$\Omega$), (3, 6), (4, 8) und (5, 10) haben dasselbe Verhältnis 2 und dieselbe Spannung. Weil der Akkumulator nur bei einer echt kleineren Abweichung ersetzt wird (`<`, nicht `<=`), bleibt das zuerst gefundene Paar stehen, (1 k$\Omega$, 2 k$\Omega$). In der Praxis wählt man eher das Paar mit den größten Werten, (5 k$\Omega$, 10 k$\Omega$): Es zieht nur 0,33 mA statt 1,67 mA aus der Quelle.
:::
:::
