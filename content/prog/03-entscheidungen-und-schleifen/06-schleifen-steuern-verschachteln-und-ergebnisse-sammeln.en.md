---
title: Controlling loops, nesting them and collecting results
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040600
summary: A loop does not have to execute every iteration completely, and it does not always have to run to the end.
tags: nested, accumulator
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
A loop does not have to execute every iteration completely, and it does not always have to run to the end. This section shows how to leave a loop early or skip an iteration, how to put loops inside one another and how to collect a result in a loop, for example a sum.
:::

### Breaking out with `break`

<span class="anker" id="stufe-5-1"></span>

A search is supposed to stop as soon as it has found something. The condition of the loop often cannot express this, because whether something has been found is only settled in the middle of the block.

**Once you have found the key, you stop searching.** If you search drawers one after another for a key, you do not open another one after finding it, even if there are drawers left.

:::definition Definition 5.1 (`break`)
<span class="anker" id="satz-5-1"></span>

The statement `break` in the block of a loop ends this loop immediately. The rest of the block is skipped, as are all further iterations, and the program continues with the first line after the loop.
:::

::::beispiel the smallest divisor
An integer $n\ge2$ is a prime number if it has no divisor apart from 1 and itself. The script tries the possible divisors $t=2,3,\ldots$ one after another; at the first one that divides $n$ without a remainder, it breaks off. The name `teiler` (German for “divisor”) is bound to `None` at first, which here means “none found yet” ([Chapter 2, Section 7.6](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-6)).

```python kleinster_teiler.py
# Find the smallest divisor of an integer n from 2 on; without a divisor, n is a prime
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

The condition `t * t <= n` limits the search to divisors up to $\sqrt n$. That is enough: if $n=t\cdot s$ with $t\le s$, then $t\cdot t\le t\cdot s=n$. So every composite number has a divisor that is at most $\sqrt n$. For 97, the script checks only $t=2$ to 9 instead of 2 to 96.
::::

⁠**In short:** `break` ends a loop immediately, typically after a find.

:::hintergrund `else` on a loop: the case “no `break`”
A loop may also have an `else` block, indented as far as its header line. It runs when the loop ends regularly, that is, for `while` because the condition became false and for `for` after the last value, but not when `break` has ended it. With it, the search for the smallest divisor needs no name of its own for “found”:

```python teiler_else.py
# The same search with else on the loop: the else block runs only if no break came
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

The word `else` is easily misleading here, because it has nothing to do with the condition of the loop. It is best read as “no `break`”: the block runs if the search has found nothing. Many programmers do not know this form; a name like `teiler` with the starting value `None` is easier to understand for most readers.
:::

### Skipping with `continue`

<span class="anker" id="stufe-5-2"></span>

Sometimes a loop is supposed to leave out individual values but keep running afterward, for example a hotel room where nobody wants to be disturbed.

**A “Do not disturb” sign.** When you clean the rooms along a hotel hallway, you pass over a room with this sign and continue with the next one. The round does not stop; only this one room is left out.

:::definition Definition 5.2 (`continue`)
<span class="anker" id="satz-5-2"></span>

The statement `continue` in the block of a loop ends only the current iteration. The rest of the block is skipped. A `for` loop continues with the next value, a `while` loop with the next check of its condition.
:::

::::beispiel
Of eight rooms, room 3 has the sign on its door (“reinige Zimmer” is German for “cleaning room”):

```python zimmer.py
# Clean hotel rooms 1 to 8; room 3 has "Do not disturb" on it, so it is skipped
for zimmer in range(1, 9):
    if zimmer == 3:
        continue
    print("reinige Zimmer", zimmer)
print("fertig")
```

```console Linux
$ python3 zimmer.py
reinige Zimmer 1
reinige Zimmer 2
reinige Zimmer 4
reinige Zimmer 5
reinige Zimmer 6
reinige Zimmer 7
reinige Zimmer 8
fertig
```

The same could be written with `if zimmer != 3:` and the indented `print`. `continue` pays off when an iteration has many lines and several reasons to leave it out: each reason gets a short check at the beginning, and the actual block does not have to be indented ever more deeply.
::::

⁠**In short:** `continue` skips the rest of the current iteration; the loop keeps running.

### Nested loops

<span class="anker" id="stufe-5-3"></span>

Checking for each number whether it is a prime number; calculating the average for each pair of two speeds: tasks like these need a repetition within the repetition.

**As with a clock.** The minute hand goes all the way around once, then the hour hand moves on by one hour, and the minute hand starts over. Two loops placed inside each other work in exactly the same way. With an outer loop over three rows and an inner loop over four columns, the iterations of the inner block come in this order:

|  | Column 0 | Column 1 | Column 2 | Column 3 |
|---|---|---|---|---|
| Row 0 | 1 | 2 | 3 | 4 |
| Row 1 | 5 | 6 | 7 | 8 |
| Row 2 | 9 | 10 | 11 | 12 |

:::definition Definition 5.3 (Nested loop)
<span class="anker" id="satz-5-3"></span>

If one loop stands in the block of another, the two are called __nested__. The loop in the block is called the inner loop, the other one the outer loop. In each iteration of the outer loop, the inner loop runs completely. If the outer loop has $m$ iterations and the inner one $n$ each time, the block of the inner loop runs $m\cdot n$ times. `break` and `continue` act only on the innermost loop whose block contains them.
:::

::::beispiel all prime numbers up to 30
The outer loop goes through the numbers $n$; the inner one searches for a divisor as in subsection [5.1](#stufe-5-1). The `break` leaves only the inner loop; the outer one continues with the next $n$.

```python primzahlen.py
# All primes up to 30: for each number n, try out the possible divisors t
for n in range(2, 31):
    ist_prim = True
    t = 2
    while t * t <= n:
        if n % t == 0:
            ist_prim = False
            break             # leaves only the inner loop
        t = t + 1
    if ist_prim:
        print(n, end=" ")
print()
```

```console Linux
$ python3 primzahlen.py
2 3 5 7 11 13 17 19 23 29
```
::::

::::beispiel two speeds for an average of 30 km/h
If you drive a route at speed $v_1$ there and at speed $v_2$ back, your average speed is $2v_1v_2/(v_1+v_2)$ ([Chapter 1, Section 6.5](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-5)). The task is to find two speeds from the series 10 km/h, 20 km/h, …, 90 km/h that give an average of exactly 30 km/h. For the average, it does not matter which of the two speeds applies on the way there and which on the way back. The inner loop therefore starts at `v1`, so that each pair occurs only once. The result is a `float`, so the script compares with `math.isclose`:

```python schnitt_suche.py
# Find two speeds from 10, 20, ..., 90 km/h whose average there and back is 30 km/h
import math
for v1 in range(10, 100, 10):
    for v2 in range(v1, 100, 10):            # v2 >= v1: each pair only once
        schnitt = 2 * v1 * v2 / (v1 + v2)
        if math.isclose(schnitt, 30):
            print(v1, "km/h und", v2, "km/h ergeben im Schnitt", schnitt, "km/h")
```

```console Linux
$ python3 schnitt_suche.py
20 km/h und 60 km/h ergeben im Schnitt 30.0 km/h
30 km/h und 30 km/h ergeben im Schnitt 30.0 km/h
```

Here, the number of inner iterations depends on the outer value: nine for $v_1=10$ km/h, eight for 20 km/h, and so on down to one for 90 km/h, 45 pairs in total instead of $9\cdot9=81$.
::::

⁠**In short:** In nested loops, the inner loop runs all the way through in each iteration of the outer one; `break` leaves only the inner loop.

### The accumulator pattern

<span class="anker" id="stufe-5-4"></span>

A loop is supposed to do more than output something: it should deliver a result from all its iterations, such as a sum, a count or a product.

**The memory key.** On a calculator, you first clear the memory and then press the M+ key after each value. At the end, the memory holds the sum of all the values. A loop does the same, except that the memory is called `summe` here.

:::definition Definition 5.4 (Accumulator)
<span class="anker" id="satz-5-4"></span>

An __accumulator__ is a name that is bound to a starting value before a loop and combined with the new value in every iteration, for example with `summe = summe + wert`. After the loop, it is bound to the result. The starting value is the result for the case in which the loop does not have a single iteration: 0 for a sum and a count, 1 for a product.
:::

::::beispiel a sum
The sum of the squares $1^2+2^2+\cdots+5^2$, with the intermediate result after each iteration:

```python quadratsumme.py
# Accumulator: the sum of the squares 1*1 + 2*2 + ... + 5*5
summe = 0                       # starting value: the empty sum
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

The loop calculates exactly the sum that mathematics writes with the summation sign (Fig. [6](#abb-6)). The summation index $i$ below the $\Sigma$ is the loop variable; the limits 1 and 5 are the bounds of `range(1, 6)`, with the stop one higher.

:::abbildung prog/k3rquadrate 6
The sum of the squares from 1 to 5 step by step, just as the loop in `quadratsumme.py` forms it: each term is one iteration.
:::
::::

::::beispiel a count
A counter is an accumulator to which 1 is added in every matching iteration:

```python zaehler.py
# Accumulator as a counter: how many numbers from 1 to 100 are divisible by 3 or by 7?
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

To check by hand: 33 of the numbers are divisible by 3 and 14 by 7; 4 are divisible by both, that is, by 21, and were counted twice; $33+14-4=43$.
::::

::::beispiel a product
In how many ways can five people line up in a row? There are 5 options for the first place, 4 for the second, and so on, $5\cdot4\cdot3\cdot2\cdot1$ in total. The starting value of a product is 1:

```python reihenfolgen.py
# Accumulator for a product: in how many ways can 5 people line up in a row?
anzahl = 1                      # starting value: the empty product
for k in range(1, 6):
    anzahl = anzahl * k
print("Reihenfolgen:", anzahl)
```

```console Linux
$ python3 reihenfolgen.py
Reihenfolgen: 120
```
::::

⁠**In short:** An accumulator starts before the loop with 0 (sum, count) or 1 (product) and takes in one value in every iteration.

:::hintergrund Why the empty sum is 0 and the empty product is 1
The starting value is chosen so that it does not change the result: $0+x=x$ and $1\cdot x=x$. That is why the result after one iteration is exactly the first value, and it is also correct if the loop does not run at all, for example with `range(1, 1)`. For the same reason, mathematics agrees that a sum without terms is 0 and a product without factors is 1; this is also where $0!=1$ and $x^0=1$ come from. If you choose a different starting value, for example 1 for a sum, every result is off by exactly this value, and you often notice it only late.
:::

### Application: mean and maximum

<span class="anker" id="stufe-5-5"></span>

Two evaluations you need all the time are accumulators: the mean of several numbers and the largest value of a series.

**The mean.** The mean of $n$ numbers $x_1,\ldots,x_n$ is their sum divided by $n$, $\bar x=\frac1n\sum_{k=1}^nx_k$. The script first asks for the number of values and then for each value, here the daily highs of four days in degrees Celsius; an accumulator collects the sum:

```python mittelwert.py
# Mean of several numbers that you type in one after the other
anzahl = int(input("Anzahl der Werte: "))
summe = 0.0
for k in range(anzahl):
    wert = float(input(f"Wert {k + 1}: "))
    summe = summe + wert
print(f"Mittelwert: {summe / anzahl:.2f}")
```

```console Linux
$ python3 mittelwert.py
Anzahl der Werte: 4
Wert 1: 18.4
Wert 2: 21.2
Wert 3: 19.7
Wert 4: 20.7
Mittelwert: 20.00
```

Fig. [7](#abb-7) shows the same calculation with the summation sign.

:::abbildung prog/k3rmittel 7
The mean of the four temperatures from `mittelwert.py` step by step: the loop forms the sum; the division by the count follows after the loop.
:::

**The maximum.** A rectangular flower bed along a house wall is to be enclosed with 40 m of fence; the wall forms the fourth side. If the two sides that lead away from the wall are each $x$ long, $40-2x$ remains for the side opposite the wall, and the area is

$$A=x\,(40-2x).$$

For which $x$ is it largest? An accumulator for the maximum remembers the largest value so far and replaces it as soon as a larger one comes along; a second name remembers where it occurred. The starting value is `0`, which every real area exceeds:

```python zaun.py
# A bed along the house wall with 40 m of fence: at which width x is the area largest?
zaun = 40            # length of the fence in m
beste_x = None
beste_a = 0
for x in range(1, 20):
    a = x * (zaun - 2 * x)               # area in square meters
    if a > beste_a:
        beste_a = a
        beste_x = x
print(f"größte Fläche {beste_a} Quadratmeter bei x = {beste_x} m")
```

```console Linux
$ python3 zaun.py
größte Fläche 200 Quadratmeter bei x = 10 m
```

The maximum lies at $x=10$ m and is 200 m$^2$; the bed is then twice as long as it is deep. However, the loop has found the maximum only among the 19 integer lengths it checked. That there is no larger value between two grid points either is shown only by a calculation: $A(x)$ is a downward-opening parabola with the zeros 0 and 20, and its vertex lies exactly in the middle between them, at $x=10$.

⁠**In short:** The mean is a sum accumulator divided by the count; the maximum is an accumulator that is replaced only by a larger value.

### Exercises for Section [5](#stufe-5)

<span class="anker" id="stufe-5-6"></span>

:::aufgabe Exercise 19 ★ Predicting `break` and `continue`
<span class="anker" id="aufg-19"></span>

What do the two loops output? Predict first, then check.

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

The first loop outputs 0 to 3 and ends at $k=4$, before the `print` runs. The second skips the multiples of 3, that is, 0, 3, 6 and 9, and otherwise runs to the end.
:::
:::

:::aufgabe Exercise 20 ★★ A trap with `continue`
<span class="anker" id="aufg-20"></span>

The following script is supposed to output the numbers 0 to 7 except 3, but after the 2 it stops outputting anything and does not end. Explain why, and fix the error without rewriting the loop as a `for` loop.

```python
k = 0
while k < 8:
    if k == 3:
        continue
    print(k)
    k = k + 1
```

:::loesung
At $k=3$, `continue` jumps back to the condition before `k = k + 1` runs. `k` stays 3, the condition stays true, and `continue` comes again and again: an infinite loop that outputs nothing more. The counter also has to advance on the path through `continue`:

```python continue_behoben.py
# The numbers 0 to 7 without the 3: the counter must advance before continue
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

A `for` loop does not have this trap, because it fetches the next value itself.
:::
:::

:::aufgabe Exercise 21 ★★ Prime numbers up to 100
<span class="anker" id="aufg-21"></span>

Change `primzahlen.py` so that it outputs all prime numbers up to 100 and reports two numbers at the end: how many prime numbers it found, and how many times in total the remainder `n % t` was calculated. Roughly how many times would it be without the bound `t * t <= n`, if you checked every $t$ from 2 to $n-1$?

:::loesung
Two counters are added: one for the prime numbers found, one for each remainder calculated.

```python primzahlen_100.py
# All prime numbers up to 100, plus two counters: primes found and remainders calculated
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

Without the bound and without `break`, with every $t$ from 2 to $n-1$, there would be $\sum_{n=2}^{100}(n-2)=0+1+\cdots+98=4851$ remainders, that is, about twenty times as many. Without the bound but with `break`, there are 1133: the prime numbers themselves then cost the most, because for them no early divisor ends the search.
:::
:::

:::aufgabe Exercise 22 ★ Sum and product
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

Calculate $1+2+\cdots+100$ with a loop and compare with the formula $n(n+1)/2$.

</li>

<li>

Calculate $1\cdot2\cdot3\cdots20$. Why is the result exact, although it has 19 digits?

</li>

</ol>

:::loesung
```python summe_produkt.py
# Sum 1 + 2 + ... + 100 and product 1 * 2 * ... * 20 with accumulators
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

(a) Both ways give 5050. (b) The product is exact, because all factors are integers and `int` can have any number of digits ([Chapter 2, Section 2.1](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/ganze-zahlen-und-rechenoperatoren.html#stufe-2-1)). With `float`, the result would no longer be guaranteed to be exact above $2^{53}$.
:::
:::

:::aufgabe Exercise 23 ★★★ A juice spritzer with less sugar
<span class="anker" id="aufg-23"></span>

Apple juice contains about 10 g of sugar per 100 ml. If you mix $s$ glasses of juice with $w$ glasses of water, the spritzer contains $10\,\mathrm g\cdot s/(s+w)$ of sugar per 100 ml. You take 1 to 10 glasses of each, and the spritzer should come as close as possible to 6.6 g per 100 ml. Write a script with two nested loops, the outer one over $w$ and the inner one over $s$, and an accumulator for the smallest deviation $|\text{sugar}-6.6\,\mathrm g|$ that outputs the best pair and its sugar content. Why are there several equally good pairs, and which one does your script find?

:::loesung
The outer loop goes through $w$, the inner one through $s$; the accumulator remembers the smallest deviation and the pair that belongs to it. It starts with `None` so that the first pair is certain to be taken over:

```python schorle.py
# Spritzer of w glasses of water and s glasses of juice (1 to 10 each): sugar close to 6.6 g per 100 ml
beste_abw = None
for w in range(1, 11):
    for s in range(1, 11):
        zucker = 10 * s / (w + s)        # juice has about 10 g of sugar per 100 ml
        abw = abs(zucker - 6.6)
        if beste_abw is None or abw < beste_abw:
            beste_abw = abw
            beste_w = w
            beste_s = s
            beste_zucker = zucker
print(f"Wasser {beste_w}, Saft {beste_s}: {beste_zucker:.3f} g je 100 ml, Abweichung {beste_abw:.3f} g")
```

```console Linux
$ python3 schorle.py
Wasser 1, Saft 2: 6.667 g je 100 ml, Abweichung 0.067 g
```

The sugar content depends only on the ratio $s/w$. The pairs with 2 and 4, 3 and 6, 4 and 8, and 5 and 10 glasses of water and juice have the same ratio 2 and the same sugar content. Because the accumulator is replaced only for a strictly smaller deviation (`<`, not `<=`), the pair found first remains: 1 glass of water and 2 glasses of juice. In practice, you choose the pair by the amount you need: three glasses of spritzer for one thirsty person, fifteen for a large pitcher.
:::
:::
