---
title: Wiederholen mit while
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
knoten: Python 3: Entscheidungen und Schleifen
order: 6040400
summary: Viele Aufgaben bestehen darin, denselben Schritt so lange zu wiederholen, bis ein Ziel erreicht ist: so lange rechnen, bis ein Ergebnis genau genug ist, so lange warten, bis eine Spannung gesunken ist.
tags: Schleife, while-Schleife, Durchlauf, Endlosschleife
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Viele Aufgaben bestehen darin, denselben Schritt so lange zu wiederholen, bis ein Ziel erreicht ist: so lange rechnen, bis ein Ergebnis genau genug ist, so lange warten, bis eine Spannung gesunken ist. In Python 1 musste man dafür die Pfeiltaste drücken, Durchgang für Durchgang. Dieser Abschnitt führt die Anweisung ein, die das selbst erledigt, und zeigt die zwei häufigsten Gründe, warum sie nicht aufhört.
:::

### Die `while`-Schleife

<span class="anker" id="stufe-3-1"></span>

Eine Anweisung, die einen Block wiederholt, heißt __Schleife__. Die einfachste Schleife wiederholt ihren Block, solange eine Bedingung gilt.

**Ein Pfeil zurück.** Im Flussdiagramm sieht eine solche Schleife aus wie eine Entscheidung, deren Ja-Weg wieder nach oben zur Raute führt (Abb. [4](#abb-4)). Nach jeder Ausführung des Blocks wird die Frage neu gestellt; erst ein Nein führt aus dem Kreis heraus.

:::abbildung prog/k3while 4
Flussdiagramm der `while`-Schleife aus `zaehlen.py`. Vor jedem Durchlauf wird die Bedingung geprüft. Ist sie wahr, läuft der Block, und der Pfeil führt zurück zur Raute; ist sie falsch, geht es nach der Schleife weiter.
:::

:::definition Definition 3.1 (`while`-Schleife)
<span class="anker" id="satz-3-1"></span>

Eine __`while`-Schleife__ hat die Form

`while Bedingung:` ` Block`

Python prüft den Wahrheitswert der Bedingung. Ist er `True`, führt es den Block aus und kehrt danach zur Kopfzeile zurück, um die Bedingung erneut zu prüfen. Ist er `False`, geht es mit der ersten Zeile nach dem Block weiter. Eine einzelne Ausführung des Blocks heißt __Durchlauf__. Die Bedingung wird vor jedem Durchlauf geprüft; ist sie schon beim ersten Mal falsch, läuft der Block kein einziges Mal.
:::

**Beispiel.** Ein Zähler steuert die Zahl der Durchläufe:

```python zaehlen.py
# Drei Durchläufe, gesteuert von einem Zähler
zaehler = 1
while zaehler <= 3:
    print("Durchlauf", zaehler)
    zaehler = zaehler + 1
print("fertig, zaehler =", zaehler)
```

```console Linux
$ python3 zaehlen.py
Durchlauf 1
Durchlauf 2
Durchlauf 3
fertig, zaehler = 4
```

Verfolgt man das Skript Prüfung für Prüfung, sieht man, warum am Ende `zaehler = 4` dasteht:

| Prüfung | `zaehler` | `zaehler <= 3` | was passiert |
|---|---|---|---|
| 1 | 1 | `True` | Durchlauf 1, danach `zaehler` = 2 |
| 2 | 2 | `True` | Durchlauf 2, danach `zaehler` = 3 |
| 3 | 3 | `True` | Durchlauf 3, danach `zaehler` = 4 |
| 4 | 4 | `False` | Schleife endet |

Drei Durchläufe brauchen vier Prüfungen: Die letzte Prüfung ist die, die falsch ausfällt.

⁠**Kurz gesagt:** `while Bedingung:` wiederholt den Block, solange die Bedingung vor dem Durchlauf wahr ist.

### Die Endlosschleife

<span class="anker" id="stufe-3-2"></span>

Eine `while`-Schleife endet nur, wenn ihre Bedingung irgendwann falsch wird. Dazu muss der Block etwas verändern, wovon die Bedingung abhängt.

**Ein Programm, das hängt.** Ändert der Block nichts an der Bedingung, prüft Python immer wieder dieselbe wahre Bedingung. Von außen sieht man oft nur, dass das Programm nicht fertig wird.

:::definition Definition 3.2 (Endlosschleife)
<span class="anker" id="satz-3-2"></span>

Eine __Endlosschleife__ ist eine Schleife, deren Bedingung nie falsch wird. Ein Programm in einer Endlosschleife bricht man mit Strg+C ab, also mit gedrückter Steuerungstaste und der Taste C. Python beendet das Programm dann mit der Ausnahme `KeyboardInterrupt` und einem Traceback ([Programmieren, Python 1, Abschnitte 6.3](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-3) und [6.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-4)).
:::

**Beispiel.** Das Skript soll $1+2+3$ addieren, aber der Zähler wird nie erhöht:

```python endlos.py
# Summe 1 + 2 + 3, aber der Zähler wird nie erhöht
zaehler = 1
summe = 0
while zaehler <= 3:
    summe = summe + zaehler
print("Summe:", summe)
```

Gestartet, gibt es nichts aus. Nach etwa einer Sekunde ist hier Strg+C gedrückt worden. Das Linux-Terminal zeigt den Tastendruck als `^C`:

```console Linux
$ python3 endlos.py
^CTraceback (most recent call last):
  File "/home/student/python-kurs/endlos.py", line 5, in <module>
    summe = summe + zaehler
    ^^^^^
KeyboardInterrupt
```

```console Windows (PowerShell)
PS> py endlos.py
Traceback (most recent call last):
  File "C:\Users\student\python-kurs\endlos.py", line 4, in <module>
    while zaehler <= 3:
          ^^^^^^^^^^^^
KeyboardInterrupt
```

Die Ortszeile nennt die Zeile, in der das Programm gerade war, als die Unterbrechung ankam. In diesen Versuchen war das unter Linux stets Zeile 5 und unter Windows stets Zeile 4; beide liegen in der Schleife, und welche es trifft, hängt vom Betriebssystem und vom Zeitpunkt ab. Die letzte Zeile, `print("Summe:", summe)`, wurde nie erreicht. Behoben ist der Fehler mit der Zeile `zaehler = zaehler + 1` im Block. Im interaktiven Modus bricht Strg+C ebenso eine laufende Schleife ab; danach erscheint wieder `>>>`, und die Sitzung geht weiter.

⁠**Kurz gesagt:** Ändert der Block nichts, wovon die Bedingung abhängt, läuft die Schleife endlos; Strg+C bricht sie mit `KeyboardInterrupt` ab.

:::hintergrund Wie Strg+C ein laufendes Programm erreicht
Die Tastenkombination fängt das Terminal ab, nicht Python. Das Betriebssystem benachrichtigt daraufhin das laufende Programm, unter Linux mit einem Signal, unter Windows über eine eigene Meldung an alle Programme des Konsolenfensters. CPython hat dafür eine kleine Routine angemeldet. Sie unterbricht die laufende Rechnung nicht sofort, sondern setzt nur eine Merkmarke. Die Interpreterschleife, die den Bytecode Befehl für Befehl abarbeitet ([Programmieren, Python 1, Abschnitt 2.4](/wissen/informatik/programmieren/python/programme-und-der-python-interpreter/vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)), sieht bei passender Gelegenheit nach dieser Marke, etwa vor dem nächsten Befehl, und löst dann in der gerade laufenden Zeile die Ausnahme `KeyboardInterrupt` aus. Deshalb kann Python an jeder Stelle eines Python-Programms unterbrochen werden, aber nicht mitten in einer einzelnen, lange dauernden Rechnung, die vollständig im C-Code von Python abläuft: Die Unterbrechung wirkt erst, wenn diese fertig ist.
:::

### Die Gleitkomma-Falle

<span class="anker" id="stufe-3-3"></span>

Eine Schleife soll in Schritten von 0,1 von 0 bis 1 zählen. Die naheliegende Bedingung „solange $x\ne1$“ ist eine Falle, und der Grund ist aus Python 2 bekannt.

**Die 1 wird übersprungen.** Damit die Falle nicht wirklich endlos läuft, bekommt das Skript eine Notbremse: Nach 12 Durchläufen ist in jedem Fall Schluss.

```python gleitkomma.py
# Zehnmal 0.1 addieren und auf genau 1.0 warten, mit einer Notbremse nach 12 Durchläufen
x = 0.0
durchlauf = 0
while x != 1.0 and durchlauf < 12:
    x = x + 0.1
    durchlauf = durchlauf + 1
    print(durchlauf, x)
```

```console Linux
$ python3 gleitkomma.py
1 0.1
2 0.2
3 0.30000000000000004
4 0.4
5 0.5
6 0.6
7 0.7
8 0.7999999999999999
9 0.8999999999999999
10 0.9999999999999999
11 1.0999999999999999
12 1.2
```

Nach zehn Additionen ist `x` nicht `1.0`, sondern `0.9999999999999999`; nach der elften ist es schon darüber. Die Bedingung `x != 1.0` ist nie falsch geworden, ohne Notbremse liefe die Schleife endlos.

**Mit `<` statt `!=`.** Die Bedingung `x < 1.0` wird zwar irgendwann falsch, aber einen Durchlauf zu spät, denn auch `0.9999999999999999` ist kleiner als 1:

```python gleitkomma_kleiner.py
# Mit < statt != endet die Schleife, aber erst einen Durchlauf zu spät
x = 0.0
durchlauf = 0
while x < 1.0:
    x = x + 0.1
    durchlauf = durchlauf + 1
print(durchlauf, x)
```

```console Linux
$ python3 gleitkomma_kleiner.py
11 1.0999999999999999
```

**Die Abhilfe: ganzzahlig zählen.** Sicher ist eine Schleife, die eine ganze Zahl zählt und den `float` in jedem Durchlauf neu aus ihr berechnet. Ganze Zahlen sind exakt ([Programmieren, Python 2, Abschnitt 2.1](/wissen/informatik/programmieren/python/werte-typen-und-variablen/ganze-zahlen-und-rechenoperatoren.html#stufe-2-1)), und die Bedingung `k < 10` wird genau nach dem zehnten Durchlauf falsch:

```python gleitkomma_zaehler.py
# Abhilfe: ganzzahlig zählen und den float in jedem Durchlauf neu ausrechnen
k = 0
while k < 10:
    k = k + 1
    x = k / 10
print(k, x)
```

```console Linux
$ python3 gleitkomma_zaehler.py
10 1.0
```

⁠**Kurz gesagt:** Eine Schleife nie mit `!=` oder `==` auf einen `float` warten lassen; ganzzahlig zählen und den `float` daraus berechnen.

:::hintergrund Warum `x = x + 0.1` die 1 nicht trifft, `k / 10` aber schon
Der gespeicherte Wert von `0.1` ist etwas größer als 0,1, und jede Addition wird auf den nächsten `float` gerundet ([Programmieren, Python 2, Abschnitt 5.1](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1)). Diese Rundungen fallen mal nach oben, mal nach unten aus. Bei `0.1 + 0.2` fällt sie nach oben, sichtbar als `0.30000000000000004`. Bei späteren Schritten fällt sie nach unten, etwa von `0.7` zu `0.7999999999999999`. Nach zehn Schritten bleibt eine Summe, die eine kleinste Stufe unter 1 liegt. Die Fehler häufen sich, weil jedes Zwischenergebnis den Fehler aller vorigen mitbringt.

`k / 10` ist dagegen eine einzige Rechnung mit zwei exakten ganzen Zahlen. Sie wird nur einmal gerundet, auf den `float`, der $k/10$ am nächsten liegt. Das ist genau der `float`, den Python auch für die Schreibweise `0.3` oder `1.0` speichert. Mit dem Zähler gibt es also keinen aufgehäuften Fehler, sondern in jedem Durchlauf nur den unvermeidlichen Darstellungsfehler einer einzelnen Zahl.
:::

### Anwendung: Wie lange sich ein Kondensator entlädt

<span class="anker" id="stufe-3-4"></span>

Ein Kondensator mit der Anfangsspannung $U_0$ entlädt sich über einen Widerstand. Seine Spannung fällt nach $u(t)=U_0\,\mathrm{e}^{-t/\tau}$ mit der Zeitkonstanten $\tau=RC$. Wie lange dauert es, bis nur noch 1 % übrig ist?

Für eine Schleife zerlegt man die Zeit in kleine Schritte $\Delta t$. Wegen $\mathrm{e}^{-(t+\Delta t)/\tau}=\mathrm{e}^{-t/\tau}\cdot\mathrm{e}^{-\Delta t/\tau}$ wird die Spannung in jedem Schritt mit demselben Faktor $\mathrm{e}^{-\Delta t/\tau}$ multipliziert. Wie viele Schritte es bis 1 % braucht, weiß man vorher nicht; die Schleife läuft, solange die Spannung noch darüber liegt.

```python rc_entladung.py
# Ein Kondensator entlädt sich über einen Widerstand: Wann ist nur noch 1 % der Spannung übrig?
import math
tau = 1e-3              # Zeitkonstante R*C in s, z. B. 1 kOhm und 1 µF
dt = 1e-4               # Zeitschritt in s
u = 5.0                 # Anfangsspannung in V
faktor = math.exp(-dt / tau)
schritte = 0
while u > 0.05:
    u = u * faktor
    schritte = schritte + 1
print("Schritte:", schritte)
print(f"Zeit: {schritte * dt * 1000:.1f} ms, Spannung: {u:.4f} V")
print(f"Formel tau * ln(100): {tau * math.log(100) * 1000:.3f} ms")
```

```console Linux
$ python3 rc_entladung.py
Schritte: 47
Zeit: 4.7 ms, Spannung: 0.0455 V
Formel tau * ln(100): 4.605 ms
```

Aus $U_0\,\mathrm{e}^{-t/\tau}=0{,}01\,U_0$ folgt $t=\tau\ln100\approx4{,}605$ ms. Die Schleife findet den ersten Zeitschritt, nach dem die Spannung unter 1 % liegt: Nach 46 Schritten, also 4,6 ms, ist sie noch knapp darüber, nach 47 Schritten darunter. Ihr Ergebnis liegt deshalb höchstens einen Zeitschritt hinter dem exakten Wert. Die Zeit rechnet das Skript als `schritte * dt` aus dem ganzzahligen Zähler, nicht durch fortgesetztes Addieren von `dt`.

⁠**Kurz gesagt:** `while` ist die richtige Schleife, wenn man die Zahl der Durchläufe vorher nicht kennt, sondern nur das Ziel.

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-5"></span>

:::aufgabe Aufgabe 10 ★ Eine Schleife verfolgen
<span class="anker" id="aufg-10"></span>

Lege für die folgende Schleife eine Tabelle an wie in Unterabschnitt [3.1](#stufe-3-1): Prüfung, Wert von `n`, Bedingung, was passiert. Wie oft läuft der Block, und was gibt `print` aus? Prüfe am Rechner.

```python
n = 13
halbierungen = 0
while n > 1:
    n = n // 2
    halbierungen = halbierungen + 1
print(halbierungen, n)
```

Vergleiche die Zahl der Durchläufe mit der Binärdarstellung von 13.

:::loesung
| Prüfung | `n` | `n > 1` | was passiert |
|---|---|---|---|
| 1 | 13 | `True` | `n` = 13 // 2 = 6, `halbierungen` = 1 |
| 2 | 6 | `True` | `n` = 3, `halbierungen` = 2 |
| 3 | 3 | `True` | `n` = 1, `halbierungen` = 3 |
| 4 | 1 | `False` | Schleife endet |

```python ablauf.py
# Wie oft lässt sich 13 ganzzahlig halbieren, bis 1 übrig bleibt?
n = 13
halbierungen = 0
while n > 1:
    n = n // 2
    halbierungen = halbierungen + 1
print(halbierungen, n)
```

```console Linux
$ python3 ablauf.py
3 1
```

Der Block läuft dreimal. $13=1101_2$ hat vier Bit, und `n // 2` streicht jedes Mal das letzte Bit ([Programmieren, Python 2, Abschnitt 3.4](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-4)): 1101, 110, 11, 1. Nach drei Halbierungen ist nur das führende Bit übrig. Allgemein läuft die Schleife so oft, wie $n$ Bit hat, weniger eins.
:::
:::

:::aufgabe Aufgabe 11 ★★ Eine Endlosschleife finden
<span class="anker" id="aufg-11"></span>

Das Skript

```python
t = 0.0
while t != 0.3:
    t = t + 0.1
print("t =", t)
```

soll nach drei Durchläufen `t = 0.3` ausgeben. Es hört aber nicht auf. Erkläre mit einer Rechnung im interaktiven Modus, warum, und schreibe eine Fassung, die nach genau drei Durchläufen endet und `t = 0.3` ausgibt.

:::loesung
```console
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 == 0.3
False
```

Nach drei Durchläufen ist `t` der `float` `0.30000000000000004`, nicht der `float` für `0.3`. Die Bedingung `t != 0.3` bleibt wahr, und danach entfernt sich `t` immer weiter von 0,3. Wie in Unterabschnitt [3.3](#stufe-3-3) zählt man ganzzahlig und rechnet `t` aus dem Zähler:

```python drei_zehntel.py
# Drei Schritte von 0.1, ganzzahlig gezählt: endet sicher und trifft 0.3
k = 0
while k < 3:
    k = k + 1
    t = k / 10
print("t =", t)
```

```console Linux
$ python3 drei_zehntel.py
t = 0.3
```
:::
:::

:::aufgabe Aufgabe 12 ★★ Die Maschinengenauigkeit mit einer Schleife
<span class="anker" id="aufg-12"></span>

In [Programmieren, Python 2, Abschnitt 5.2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-2) wurde die Maschinengenauigkeit $\varepsilon_{\mathrm M}$ mit der Pfeiltaste gesucht. Schreibe eine Schleife, die mit `eps = 1.0` beginnt und `eps` so lange halbiert, wie `1.0 + eps / 2` noch von `1.0` verschieden ist. Vergleiche das Ergebnis mit `sys.float_info.epsilon`. Warum endet diese Schleife sicher, obwohl sie Gleitkommazahlen vergleicht?

:::loesung
```python epsilon.py
# Die Maschinengenauigkeit: eps halbieren, solange 1.0 + eps / 2 noch von 1.0 verschieden ist
import sys
eps = 1.0
halbierungen = 0
while 1.0 + eps / 2 != 1.0:
    eps = eps / 2
    halbierungen = halbierungen + 1
print(eps, "nach", halbierungen, "Halbierungen")
print("sys.float_info.epsilon:", sys.float_info.epsilon)
```

```console Linux
$ python3 epsilon.py
2.220446049250313e-16 nach 52 Halbierungen
sys.float_info.epsilon: 2.220446049250313e-16
```

Die Schleife endet bei $\varepsilon=2^{-52}=\varepsilon_{\mathrm M}$: Dann ist $\varepsilon/2=2^{-53}$, und $1+2^{-53}$ wird zur geraden Mantisse gerundet, also zu 1 ([Programmieren, Python 2, Abschnitt 5.2](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-2)). Sie endet sicher, obwohl sie Gleitkommazahlen mit `!=` vergleicht, weil sie nicht auf einen bestimmten Wert wartet. Das Halbieren einer Zweierpotenz ist exakt, `eps` durchläuft also genau $2^0,2^{-1},2^{-2},\ldots$, und spätestens wenn $\varepsilon/2$ kleiner als der halbe Abstand der `float` bei 1 ist, kann $1+\varepsilon/2$ nicht mehr von 1 verschieden sein.
:::
:::

:::aufgabe Aufgabe 13 ★★ Einen Kondensator aufladen
<span class="anker" id="aufg-13"></span>

Ein Kondensator wird über einen Widerstand an 5 V geladen und beginnt bei 0 V. Seine Spannung ist $u(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr)$. Zeige, dass in jedem Zeitschritt $u_\mathrm{neu}=U_0-(U_0-u_\mathrm{alt})\,\mathrm{e}^{-\Delta t/\tau}$ gilt. Schreibe damit ein Skript, das mit $\tau=1$ ms und $\Delta t=0{,}1$ ms die Schritte zählt, bis 90 % von $U_0$ erreicht sind, und vergleiche mit $\tau\ln10$.

:::loesung
Aus $u(t)=U_0(1-\mathrm{e}^{-t/\tau})$ folgt $U_0-u(t)=U_0\mathrm{e}^{-t/\tau}$, und damit

$$u(t+\Delta t)=U_0-U_0\,\mathrm{e}^{-(t+\Delta t)/\tau}=U_0-U_0\,\mathrm{e}^{-t/\tau}\,\mathrm{e}^{-\Delta t/\tau}=U_0-\bigl(U_0-u(t)\bigr)\,\mathrm{e}^{-\Delta t/\tau}.$$

Der Abstand zur Endspannung nimmt also in jedem Schritt um denselben Faktor ab, wie beim Entladen.

```python aufladen.py
# Kondensator über einen Widerstand an 5 V laden: Wann sind 90 % erreicht?
import math
tau = 1e-3              # Zeitkonstante in s
dt = 1e-4               # Zeitschritt in s
u0 = 5.0                # Ladespannung in V
u = 0.0                 # Anfangsspannung in V
faktor = math.exp(-dt / tau)
schritte = 0
while u < 0.9 * u0:
    u = u0 - (u0 - u) * faktor
    schritte = schritte + 1
print(f"Schritte: {schritte}, Zeit: {schritte * dt * 1000:.1f} ms, Spannung: {u:.4f} V")
print(f"Formel tau * ln(10): {tau * math.log(10) * 1000:.3f} ms")
```

```console Linux
$ python3 aufladen.py
Schritte: 24, Zeit: 2.4 ms, Spannung: 4.5464 V
Formel tau * ln(10): 2.303 ms
```

Aus $1-\mathrm{e}^{-t/\tau}=0{,}9$ folgt $t=\tau\ln10\approx2{,}303$ ms. Die Schleife meldet den ersten Zeitschritt danach, 2,4 ms.
:::
:::

:::aufgabe Aufgabe 14 ★ So lange fragen, bis die Eingabe passt
<span class="anker" id="aufg-14"></span>

Schreibe ein Skript `eingabe_r.py`, das nach einem Widerstand in Ohm fragt und die Frage so lange wiederholt, bis eine Zahl größer als 0 eingegeben ist. Dann soll es den Strom bei 5 V ausgeben. Teste mit den Eingaben $-5$, $0$ und $470$ nacheinander.

:::loesung
Die Frage steht einmal vor der Schleife und einmal im Block; die Schleife läuft, solange die letzte Eingabe ungültig ist.

```python eingabe_r.py
# So lange nach dem Widerstand fragen, bis er größer als 0 ist
r = float(input("Widerstand in Ohm: "))
while r <= 0:
    print("Der Widerstand muss größer als 0 sein.")
    r = float(input("Widerstand in Ohm: "))
print(f"Strom bei 5 V: {5 / r * 1000:.2f} mA")
```

```console Linux
$ python3 eingabe_r.py
Widerstand in Ohm: -5
Der Widerstand muss größer als 0 sein.
Widerstand in Ohm: 0
Der Widerstand muss größer als 0 sein.
Widerstand in Ohm: 470
Strom bei 5 V: 10.64 mA
```

Tippt man statt einer Zahl ein Wort, bricht `float` mit `ValueError` ab; das abzufangen erfordert eine Ausnahmebehandlung, die dieses Kapitel nicht behandelt.
:::
:::
