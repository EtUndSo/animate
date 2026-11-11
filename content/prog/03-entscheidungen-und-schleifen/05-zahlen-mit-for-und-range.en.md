---
title: Counting with for and range
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040500
summary: Often it is clear before the first repetition how many there will be: for each day of a week, for each year of a savings plan.
tags: for loop, loop variable
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Often it is clear before the first repetition how many there will be: for each day of a week, for each year of a savings plan. With `while`, you need a counter, a condition and a line that increases the counter for this, and if you forget the last one, the loop runs forever. This section introduces a loop that does the counting itself, and the sequences of numbers it runs through.
:::

### The `for` loop

<span class="anker" id="stufe-4-1"></span>

A loop that works through a fixed sequence of values does not need a condition of its own: it ends when the sequence is over.

**A staircase.** When you climb a staircase, you step onto one stair after another: the same thing happens on each stair, and after the last one, you are done. A name always shows which stair you are currently standing on.

:::definition Definition 4.1 (`for` loop)
<span class="anker" id="satz-4-1"></span>

A __`for` loop__ has the form

`for name in range(n):` ` Block`

Here, for an integer $n$, `range(n)` yields the integers $0, 1, \ldots, n-1$ in order. The loop binds `name` to each of these numbers in turn and executes the block each time; after the last number, execution continues after the block. The name is called the __loop variable__. In general, `in` is followed by an object that yields values one after another; in this section, it is always a `range`.
:::

::::beispiel
The first powers of two:

```python zweierpotenzen.py
# Powers of two with a for loop
for k in range(5):
    print(k, 2 ** k)
print("fertig")
```

```console Linux
$ python3 zweierpotenzen.py
0 1
1 2
2 4
3 8
4 16
fertig
```

With `while`, the same loop needs three more lines: `k = 0` before the loop, the condition `k < 5` and `k = k + 1` at the end of the block. The `for` loop takes care of all three.
::::

⁠**In short:** `for k in range(n):` executes the block for $k=0,1,\ldots,n-1$.

### The sequence of numbers `range`

<span class="anker" id="stufe-4-2"></span>

Not every sequence starts at 0 and goes up in steps of one: amounts from 100 g to 500 g in steps of 100 g, a countdown from 10 downward.

**Marks on the number line.** On the number line, you set a first mark at the start and then further marks at a fixed spacing until you reach or pass the stop mark. The stop mark itself is not included (Fig. [5](#abb-5)).

:::abbildung prog/k3range 5
The sequence `range(2, 11, 3)`: it begins at the start 2, continues in steps of 3 and stops before the stop 11. The next mark would be 11 itself; the stop never belongs to the sequence.
:::

:::definition Definition 4.2 (`range`)
<span class="anker" id="satz-4-2"></span>

`range` exists with one, two or three integer arguments: `range(stop)`, `range(start, stop)` and `range(start, stop, schritt)` (`schritt` is German for “step”). If `start` is missing, it is 0; if `schritt` is missing, it is 1. The sequence consists of the numbers $\mathtt{start}$, $\mathtt{start}+\mathtt{schritt}$, $\mathtt{start}+2\cdot\mathtt{schritt}$, …, as long as they are less than `stop` for a positive step and greater than `stop` for a negative step. `stop` itself never belongs to it. If `start` is already not before `stop`, the sequence is empty. `len` returns the number of elements; for a positive step, it is

$$\mathtt{len}=\max\Bigl(0,\Bigl\lceil\frac{\mathtt{stop}-\mathtt{start}}{\mathtt{schritt}}\Bigr\rceil\Bigr).$$
:::

::::beispiel
The addition `end=" "` in `print`, passed by name, writes a space at the end instead of a line break. This way, each sequence stands on one line, and `print()` without values ends the line (“leer” is German for “empty”):

```python range_folgen.py
# Which numbers does range yield? Each line shows one sequence, end=" " keeps it on one line.
for i in range(5):
    print(i, end=" ")
print()
for i in range(2, 6):
    print(i, end=" ")
print()
for i in range(2, 10, 3):
    print(i, end=" ")
print()
for i in range(10, 0, -3):
    print(i, end=" ")
print()
for i in range(5, 5):
    print(i, end=" ")
print("(leer)")
```

```console Linux
$ python3 range_folgen.py
0 1 2 3 4
2 3 4 5
2 5 8
10 7 4 1
(leer)
```

In interactive mode, Python shows a `range` only with its bounds; `len` returns the number of elements. Only integers are allowed, and the step must not be 0:

```console
>>> range(5)
range(0, 5)
>>> len(range(2, 10, 3))
3
>>> len(range(0, 100, 7))
15
>>> range(0.5)
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    range(0.5)
    ~~~~~^^^^^
TypeError: 'float' object cannot be interpreted as an integer
>>> range(1, 10, 0)
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    range(1, 10, 0)
    ~~~~~^^^^^^^^^^
ValueError: range() arg 3 must not be zero
```

`len(range(0, 100, 7))` is $\lceil100/7\rceil=\lceil14.29\rceil=15$: the numbers 0, 7, 14, …, 98.

A price table for 100 g to 500 g of cheese at €18.90 per kilogram needs 501 as the stop so that 500 is still included:

```python preis_tabelle.py
# Price of different amounts of cheese at 18.90 euros per kg
kilopreis = 18.90
for gramm in range(100, 501, 100):
    print(f"{gramm} g kosten {kilopreis * gramm / 1000:5.2f} Euro")
```

```console Linux
$ python3 preis_tabelle.py
100 g kosten  1.89 Euro
200 g kosten  3.78 Euro
300 g kosten  5.67 Euro
400 g kosten  7.56 Euro
500 g kosten  9.45 Euro
```

The most common error with `range` is exactly this one: `range(1, 10)` yields 1 to 9, not 1 to 10.
::::

⁠**In short:** `range(start, stop, schritt)` counts from `start` in steps up to just before `stop`; the stop is never included.

:::hintergrund Why the stop does not belong to the sequence
A range that includes the lower bound and excludes the upper one has two convenient properties. First, its length is the difference of the bounds: `range(a, b)` has exactly $b-a$ elements, and `range(n)` has exactly $n$. Second, two such ranges join without a gap and without overlap: `range(0, 5)` and `range(5, 10)` together give exactly `range(0, 10)`, and the common bound 5 occurs exactly once. In 1982, the computer scientist Edsger Dijkstra explained why, for this reason, sequences should best start at 0 and be described by $0\le i<n$: if the lower bound were excluded, a range that starts at the smallest natural number 0 would have to be written with the bound $-1$, that is, with a number outside the natural numbers. Python follows this choice for `range` and wherever ranges occur.
:::

:::hintergrund What a `range` stores in memory
A `range` does not store its numbers. It stores only three numbers, start, stop and step, and calculates each element only when the loop needs it, as $\mathtt{start}+k\cdot\mathtt{schritt}$. That is why `range(10 ** 15)` needs no more memory than `range(5)`, and `len` calculates the number of elements with the formula instead of counting:

```console
>>> len(range(10 ** 15))
1000000000000000
```
:::

### Floating-point steps via an integer counter

<span class="anker" id="stufe-4-3"></span>

A stopwatch is supposed to display the times 0 s, 0.1 s, …, 1 s. But `range` accepts only integers.

The solution is the same as for the floating-point trap in subsection [3.3](wiederholen-mit-while.html#stufe-3-3): the loop counts with an integer $k$, and you recalculate the time in every iteration as $t_k=k\cdot\Delta t$, here as `k / 10`. The following script puts both ways side by side, repeated adding and the calculation from the counter:

```python zeitachse.py
# Times 0 s, 0.1 s, ..., 1 s: once added up, once from the integer counter
t = 0.0
for k in range(11):
    print(k, t, k / 10)
    t = t + 0.1
```

```console Linux
$ python3 zeitachse.py
0 0.0 0.0
1 0.1 0.1
2 0.2 0.2
3 0.30000000000000004 0.3
4 0.4 0.4
5 0.5 0.5
6 0.6 0.6
7 0.7 0.7
8 0.7999999999999999 0.8
9 0.8999999999999999 0.9
10 0.9999999999999999 1.0
```

The middle column accumulates the rounding errors; the right one hits each time as exactly as a `float` can represent it at all. [Chapter 2, Section 5](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5) made the same observation in an exercise with interactive mode; with the loop, you see all the times at once.

⁠**In short:** For steps with floating-point numbers, `range` counts with integers, and you calculate the value from the counter.

### `for` or `while`?

<span class="anker" id="stufe-4-4"></span>

Both loops repeat a block. Which one you choose depends on what you know before the first iteration.

|  | `for k in range(…)` | `while Bedingung` |
|---|---|---|
| when suitable | number of iterations is known beforehand | goal is known, number of iterations is not |
| how it ends | after the last value of the sequence | when the condition is false |
| danger | no infinite loop possible | infinite if the block does not change the condition |
| example | price table for 5 amounts | tea cooling down to 60 °C |

One difference often comes as a surprise: if you bind the loop variable to a different value inside a `for` loop, this has no effect on the next iteration, because the loop binds the name anew to the next value from the `range` each time.

```python schleifenvariable.py
# Changing the loop variable inside the loop does not change the sequence
for i in range(3):
    print("Anfang des Durchlaufs:", i)
    i = 100
    print("nach i = 100:", i)
```

```console Linux
$ python3 schleifenvariable.py
Anfang des Durchlaufs: 0
nach i = 100: 100
Anfang des Durchlaufs: 1
nach i = 100: 100
Anfang des Durchlaufs: 2
nach i = 100: 100
```

The assignment `i = 100` only changes what the name is bound to in the current iteration; the `range` still yields 1 and then 2.

⁠**In short:** `for` when the sequence of values is known beforehand; `while` when only the goal is known.

### Exercises for Section [4](#stufe-4)

<span class="anker" id="stufe-4-5"></span>

:::aufgabe Exercise 15 ★ Predicting sequences
<span class="anker" id="aufg-15"></span>

For each `range`, write down the numbers it yields and how many there are. Check the count with `len` and the numbers with a loop as in `range_folgen.py`. (a) `range(4)`, (b) `range(1, 4)`, (c) `range(0, 10, 2)`, (d) `range(10, 0, -2)`, (e) `range(3, 3)`, (f) `range(0, 1, 5)`, (g) `range(-3, 3)`.

:::loesung
(a) 0, 1, 2, 3: four numbers. (b) 1, 2, 3: three. (c) 0, 2, 4, 6, 8: five. (d) 10, 8, 6, 4, 2: five; the 0 is the stop and is not included. (e) empty. (f) only the 0: one number, because $0+5$ already lies above the stop. (g) $-3$ to 2: six numbers.

```console
>>> len(range(4))
4
>>> len(range(1, 4))
3
>>> len(range(0, 10, 2))
5
>>> len(range(10, 0, -2))
5
>>> len(range(3, 3))
0
>>> len(range(0, 1, 5))
1
>>> len(range(-3, 3))
6
```

For positive steps, the formula from subsection [4.2](#stufe-4-2) confirms every count, for example (f): $\lceil(1-0)/5\rceil=\lceil0.2\rceil=1$.
:::
:::

:::aufgabe Exercise 16 ★★ A travel time table
<span class="anker" id="aufg-16"></span>

Write a script that outputs the travel time in hours with two decimal places for an average speed of 75 km/h and the distances 100 km, 200 km, …, 1000 km, one line per distance. Which arguments does `range` need?

:::loesung
The stop has to lie above 1000 so that 1000 is still included: `range(100, 1001, 100)`.

```python fahrzeit_tabelle.py
# Travel time at an average of 75 km/h for 100 km to 1000 km
tempo = 75.0
for km in range(100, 1001, 100):
    print(f"{km:4d} km   {km / tempo:5.2f} h")
```

```console Linux
$ python3 fahrzeit_tabelle.py
 100 km    1.33 h
 200 km    2.67 h
 300 km    4.00 h
 400 km    5.33 h
 500 km    6.67 h
 600 km    8.00 h
 700 km    9.33 h
 800 km   10.67 h
 900 km   12.00 h
1000 km   13.33 h
```

The format specifier `4d` keeps the distances right-aligned in four places, and `5.2f` keeps the times in five characters with two decimal places, so that the columns line up ([Chapter 2, Section 10.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/zeichenketten-eingabe-und-ausgabe.html#stufe-10-2)).
:::
:::

:::aufgabe Exercise 17 ★★ One minute of video
<span class="anker" id="aufg-17"></span>

A video shows 60 frames per second; frame number $k$ begins at time $t_k=k/60$ s. Calculate $t_{3600}$, which should be exactly 60 s, in three ways: (a) with a loop that adds `1 / 60` to `t` 3600 times, (b) as `3600 * (1 / 60)`, (c) as `3600 / 60`. Which ways hit 60.0 exactly? Explain the difference with the number of roundings.

:::loesung
```python video.py
# One minute of video at 60 frames per second: the time after the last frame, calculated in three ways
t = 0.0
for k in range(3600):
    t = t + 1 / 60
print("aufaddiert:      ", t)
print("3600 * (1 / 60): ", 3600 * (1 / 60))
print("3600 / 60:       ", 3600 / 60)
```

```console Linux
$ python3 video.py
aufaddiert:       59.999999999997875
3600 * (1 / 60):  60.0
3600 / 60:        60.0
```

(a) misses 60: in each of the 3600 additions, the result is rounded, and the errors accumulate to about $2\cdot10^{-12}$. (b) contains two roundings, one when forming `1 / 60` and one when multiplying. Here they cancel out in such a way that exactly 60.0 results; this is not guaranteed: `49 * (1 / 49)`, for example, gives `0.9999999999999999`. (c) is a single, exact calculation. The safest way is therefore to calculate each time as `k / 60`: one rounding per value, never accumulated.
:::
:::

:::aufgabe Exercise 18 ★★ Rewriting loops
<span class="anker" id="aufg-18"></span>

<ol class="al">

<li>

Rewrite `zaehlen.py` from subsection [3.1](wiederholen-mit-while.html#stufe-3-1) with a `for` loop. What does your version output as the last value of the counter, and why does it differ from the `while` version?

</li>

<li>

Rewrite the loop `for i in range(10, 0, -3):` with `print(i)` in the block as a `while` loop.

</li>

</ol>

:::loesung
(a)

```python zaehlen_for.py
# zaehlen.py with a for loop
for zaehler in range(1, 4):
    print("Durchlauf", zaehler)
print("fertig, zaehler =", zaehler)
```

```console Linux
$ python3 zaehlen_for.py
Durchlauf 1
Durchlauf 2
Durchlauf 3
fertig, zaehler = 3
```

The `for` loop binds `zaehler` last to 3, the last value from the `range`, and does not increase it any further. The `while` version increases the counter at the end of every iteration, including the last one, and ends only when the check fails with the value 4.

(b) Start before the loop, the condition “still above the stop”, the step at the end of the block:

```python countdown_while.py
# for i in range(10, 0, -3): print(i)  as a while loop
i = 10
while i > 0:
    print(i)
    i = i - 3
```

```console Linux
$ python3 countdown_while.py
10
7
4
1
```

With a negative step, the condition is `i > 0`, not `i < 0`: the sequence continues as long as it lies above the stop.
:::
:::
