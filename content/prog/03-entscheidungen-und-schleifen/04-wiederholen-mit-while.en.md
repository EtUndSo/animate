---
title: Repeating with while
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040400
summary: Many tasks consist of repeating the same step until a goal is reached: calculating until a result is accurate enough, waiting until a cup of tea has cooled down.
tags: loop, while loop, iteration, infinite loop
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Many tasks consist of repeating the same step until a goal is reached: calculating until a result is accurate enough, waiting until a cup of tea has cooled down. In [Chapter 1](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/programme-und-der-python-interpreter.html), you had to press the arrow key for this, pass after pass. This section introduces the statement that does this on its own and shows the two most common reasons why it does not stop.
:::

### The `while` loop

<span class="anker" id="stufe-3-1"></span>

A statement that repeats a block is called a __loop__. The simplest loop repeats its block as long as a condition holds.

**An arrow back.** In a flowchart, such a loop looks like a decision whose yes path leads back up to the diamond (Fig. [4](#abb-4)). After each execution of the block, the question is asked again; only a no leads out of the circle.

:::abbildung prog/k3while 4
Flowchart of the `while` loop from `zaehlen.py`. The condition is checked before each iteration. If it is true, the block runs and the arrow leads back to the diamond; if it is false, execution continues after the loop.
:::

:::definition Definition 3.1 (`while` loop)
<span class="anker" id="satz-3-1"></span>

A __`while` loop__ has the form

`while Bedingung:` ` Block`

Python checks the truth value of the condition. If it is `True`, Python executes the block and then returns to the header line to check the condition again. If it is `False`, execution continues with the first line after the block. A single execution of the block is called an __iteration__. The condition is checked before each iteration; if it is already false the first time, the block does not run even once.
:::

::::beispiel
A counter controls the number of iterations (“Durchlauf” is German for “iteration”):

```python zaehlen.py
# Three iterations, controlled by a counter
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

If you follow the script check by check, you see why `zaehler = 4` appears at the end:

| Check | `zaehler` | `zaehler <= 3` | what happens |
|---|---|---|---|
| 1 | 1 | `True` | iteration 1, then `zaehler` = 2 |
| 2 | 2 | `True` | iteration 2, then `zaehler` = 3 |
| 3 | 3 | `True` | iteration 3, then `zaehler` = 4 |
| 4 | 4 | `False` | loop ends |

Three iterations need four checks: the last check is the one that turns out false.
::::

⁠**In short:** `while Bedingung:` repeats the block as long as the condition is true before the iteration.

### The infinite loop

<span class="anker" id="stufe-3-2"></span>

A `while` loop ends only if its condition becomes false at some point. For that, the block has to change something the condition depends on.

**A program that hangs.** If the block changes nothing about the condition, Python checks the same true condition again and again. From the outside, you often only see that the program does not finish.

:::definition Definition 3.2 (Infinite loop)
<span class="anker" id="satz-3-2"></span>

An __infinite loop__ is a loop whose condition never becomes false. You interrupt a program in an infinite loop with Ctrl+C, that is, by holding down the Control key and pressing C. Python then ends the program with the exception `KeyboardInterrupt` and a traceback ([Chapter 1, Sections 6.3](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-3) and [6.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/fehler-lesen-und-verstehen.html#stufe-6-4)).
:::

::::beispiel
The script is supposed to add $1+2+3$, but the counter is never increased:

```python endlos.py
# Sum 1 + 2 + 3, but the counter is never increased
zaehler = 1
summe = 0
while zaehler <= 3:
    summe = summe + zaehler
print("Summe:", summe)
```

Once started, it outputs nothing. Here, Ctrl+C was pressed after about one second. The Linux terminal shows the keystroke as `^C`:

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

The location line names the line the program was in when the interruption arrived. In these trials, that was always line 5 under Linux and always line 4 under Windows; both lie in the loop, and which one it hits depends on the operating system and on the moment. The last line, `print("Summe:", summe)`, was never reached. The error is fixed with the line `zaehler = zaehler + 1` in the block. In interactive mode, Ctrl+C interrupts a running loop in the same way; afterward, `>>>` appears again and the session continues.
::::

⁠**In short:** If the block changes nothing the condition depends on, the loop runs forever; Ctrl+C interrupts it with `KeyboardInterrupt`.

:::hintergrund How Ctrl+C reaches a running program
The terminal intercepts the key combination, not Python. The operating system then notifies the running program: under Linux with a signal, under Windows with a message of its own to all programs of the console window. CPython has registered a small handler for this. The handler does not interrupt the running calculation immediately; it only sets a flag. The interpreter loop, which processes the bytecode instruction by instruction ([Chapter 1, Section 2.4](/wissen/en/informatik/programmieren/python/programme-und-der-python-interpreter/vom-quelltext-zur-ausfuhrung-compiler-und-interpreter.html#stufe-2-4)), checks this flag at a suitable moment, for example before the next instruction, and then raises the exception `KeyboardInterrupt` in the line that is currently running. That is why Python can be interrupted at any point of a Python program, but not in the middle of a single long-running calculation that takes place entirely in Python's C code: the interruption takes effect only when that calculation is finished.
:::

### The floating-point trap

<span class="anker" id="stufe-3-3"></span>

A loop is supposed to count from 0 to 1 in steps of 0.1. The obvious condition “as long as $x\ne1$” is a trap, and the reason is known from [Chapter 2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/werte-typen-und-variablen.html).

**The 1 is skipped.** So that the trap does not really run forever, the script gets an emergency brake: after 12 iterations, it stops in any case.

```python gleitkomma.py
# Add 0.1 ten times and wait for exactly 1.0, with an emergency brake after 12 iterations
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

After ten additions, `x` is not `1.0` but `0.9999999999999999`; after the eleventh, it is already above 1. The condition `x != 1.0` never became false; without the emergency brake, the loop would run forever.

**With `<` instead of `!=`.** The condition `x < 1.0` does become false at some point, but one iteration too late, because `0.9999999999999999` is also less than 1:

```python gleitkomma_kleiner.py
# With < instead of != the loop ends, but only one iteration too late
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

**The remedy: count with integers.** A loop is safe if it counts an integer and recalculates the `float` from it in every iteration. Integers are exact ([Chapter 2, Section 2.1](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/ganze-zahlen-und-rechenoperatoren.html#stufe-2-1)), and the condition `k < 10` becomes false exactly after the tenth iteration:

```python gleitkomma_zaehler.py
# Remedy: count with integers and recompute the float in every iteration
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

⁠**In short:** Never let a loop wait for a `float` with `!=` or `==`; count with integers and calculate the `float` from the counter.

:::hintergrund Why `x = x + 0.1` misses 1 but `k / 10` hits it
The stored value of `0.1` is slightly greater than 0.1, and every addition is rounded to the nearest `float` ([Chapter 2, Section 5.1](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-1)). These roundings sometimes go up and sometimes down. For `0.1 + 0.2`, the rounding goes up, visible as `0.30000000000000004`. At later steps, it goes down, for example from `0.7` to `0.7999999999999999`. After ten steps, what remains is a sum that lies one smallest step below 1. The errors pile up because every intermediate result carries the errors of all the previous ones along with it.

`k / 10`, on the other hand, is a single calculation with two exact integers. It is rounded only once, to the `float` closest to $k/10$. That is exactly the `float` Python also stores for the notation `0.3` or `1.0`. So with the counter, there is no accumulated error, only the unavoidable representation error of a single number in each iteration.
:::

### Application: how long a cup of tea takes to cool down

<span class="anker" id="stufe-3-4"></span>

A freshly brewed cup of tea is at 90 °C, and the room is at 20 °C. As in [Chapter 2, Section 8.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/module-math-und-sys.html#stufe-8-2), the temperature difference between the tea and the room shrinks approximately like an exponential function. The temperature of the tea is then

$$T(t)=T_\mathrm Z+(T_0-T_\mathrm Z)\,\mathrm{e}^{-t/\tau}$$

with the room temperature $T_\mathrm Z$, the initial temperature $T_0$ and a time constant $\tau$ that depends on the cup, the amount and drafts; here it is 20 min. How long does it take until the tea has cooled down to 60 °C?

For a loop, you divide time into small steps $\Delta t$. Because $\mathrm{e}^{-(t+\Delta t)/\tau}=\mathrm{e}^{-t/\tau}\cdot\mathrm{e}^{-\Delta t/\tau}$, the temperature difference $T-T_\mathrm Z$ is multiplied by the same factor $\mathrm{e}^{-\Delta t/\tau}$ in every step. How many steps it takes to reach 60 °C is not known beforehand; the loop runs as long as the tea is still warmer than that.

```python tee.py
# A cup of tea cools down in a room: when is it down to 60 degrees?
import math
tau = 20.0              # time constant in min
dt = 0.1                # time step in min
zimmer = 20.0           # room temperature in degrees
tee = 90.0              # initial tea temperature in degrees
faktor = math.exp(-dt / tau)
schritte = 0
while tee > 60.0:
    tee = zimmer + (tee - zimmer) * faktor
    schritte = schritte + 1
print("Schritte:", schritte)
print(f"Zeit: {schritte * dt:.1f} min, Temperatur: {tee:.2f} Grad")
print(f"Formel tau * ln(70/40): {tau * math.log(70 / 40):.2f} min")
```

```console Linux
$ python3 tee.py
Schritte: 112
Zeit: 11.2 min, Temperatur: 59.98 Grad
Formel tau * ln(70/40): 11.19 min
```

From $20+70\,\mathrm{e}^{-t/\tau}=60$, it follows that $\mathrm{e}^{-t/\tau}=40/70$ and $t=\tau\ln(70/40)\approx11.19$ min. The loop finds the first time step after which the tea is at most 60 °C: after 111 steps, that is, 11.1 min, it is still just above, and after 112 steps, it is below. Its result therefore lies at most one time step behind the exact value. The script calculates the time as `schritte * dt` from the integer counter, not by repeatedly adding `dt`.

⁠**In short:** `while` is the right loop when you do not know the number of iterations beforehand, only the goal.

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-5"></span>

:::aufgabe Exercise 10 ★ Tracing a loop
<span class="anker" id="aufg-10"></span>

For the following loop, make a table like the one in subsection [3.1](#stufe-3-1): check, value of `n`, condition, what happens. How many times does the block run, and what does `print` output? Check on the computer.

```python
n = 13
halbierungen = 0
while n > 1:
    n = n // 2
    halbierungen = halbierungen + 1
print(halbierungen, n)
```

Compare the number of iterations with the binary representation of 13.

:::loesung
| Check | `n` | `n > 1` | what happens |
|---|---|---|---|
| 1 | 13 | `True` | `n` = 13 // 2 = 6, `halbierungen` = 1 |
| 2 | 6 | `True` | `n` = 3, `halbierungen` = 2 |
| 3 | 3 | `True` | `n` = 1, `halbierungen` = 3 |
| 4 | 1 | `False` | loop ends |

```python ablauf.py
# How many times can 13 be halved as an integer until 1 is left?
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

The block runs three times. $13=1101_2$ has four bits, and `n // 2` removes the last bit each time ([Chapter 2, Section 3.4](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-4)): 1101, 110, 11, 1. After three halvings, only the leading bit is left. In general, the loop runs as many times as $n$ has bits, minus one.
:::
:::

:::aufgabe Exercise 11 ★★ Finding an infinite loop
<span class="anker" id="aufg-11"></span>

The script

```python
t = 0.0
while t != 0.3:
    t = t + 0.1
print("t =", t)
```

is supposed to output `t = 0.3` after three iterations. But it does not stop. Explain why with a calculation in interactive mode, and write a version that ends after exactly three iterations and outputs `t = 0.3`.

:::loesung
```console
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 == 0.3
False
```

After three iterations, `t` is the `float` `0.30000000000000004`, not the `float` for `0.3`. The condition `t != 0.3` stays true, and after that, `t` moves farther and farther away from 0.3. As in subsection [3.3](#stufe-3-3), you count with integers and calculate `t` from the counter:

```python drei_zehntel.py
# Three steps of 0.1, counted with integers: ends for sure and hits 0.3
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

:::aufgabe Exercise 12 ★★ Machine epsilon with a loop
<span class="anker" id="aufg-12"></span>

In [Chapter 2, Section 5.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-2), the machine epsilon $\varepsilon_{\mathrm M}$ was found with the arrow key. Write a loop that starts with `eps = 1.0` and halves `eps` as long as `1.0 + eps / 2` is still different from `1.0`. Compare the result with `sys.float_info.epsilon`. Why is this loop certain to end, although it compares floating-point numbers?

:::loesung
```python epsilon.py
# Machine epsilon: halve eps as long as 1.0 + eps / 2 still differs from 1.0
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

The loop ends at $\varepsilon=2^{-52}=\varepsilon_{\mathrm M}$: then $\varepsilon/2=2^{-53}$, and $1+2^{-53}$ is rounded to the even significand, that is, to 1 ([Chapter 2, Section 5.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-2)). It is certain to end, although it compares floating-point numbers with `!=`, because it does not wait for a particular value. Halving a power of two is exact, so `eps` runs through exactly $2^0,2^{-1},2^{-2},\ldots$, and at the latest when $\varepsilon/2$ is smaller than half the spacing of the `float` values near 1, $1+\varepsilon/2$ can no longer differ from 1.
:::
:::

:::aufgabe Exercise 13 ★★ A drink warms up
<span class="anker" id="aufg-13"></span>

A bottle of juice comes out of the refrigerator at 6 °C into a room at 21 °C. Its temperature is approximately $T(t)=T_\mathrm Z-(T_\mathrm Z-T_0)\,\mathrm{e}^{-t/\tau}$, with the same symbols as for the tea in subsection [3.4](#stufe-3-4). Show that $T_\mathrm{new}=T_\mathrm Z-(T_\mathrm Z-T_\mathrm{old})\,\mathrm{e}^{-\Delta t/\tau}$ holds in every time step. Use it to write a script that, with $\tau=30$ min and $\Delta t=0.1$ min, counts the steps until the bottle has covered 90 % of the way to room temperature, that is, reaches 19.5 °C, and compare with $\tau\ln10$.

:::loesung
From $T(t)=T_\mathrm Z-(T_\mathrm Z-T_0)\,\mathrm{e}^{-t/\tau}$, it follows that $T_\mathrm Z-T(t)=(T_\mathrm Z-T_0)\,\mathrm{e}^{-t/\tau}$, and therefore

$$T(t+\Delta t)=T_\mathrm Z-(T_\mathrm Z-T_0)\,\mathrm{e}^{-t/\tau}\,\mathrm{e}^{-\Delta t/\tau}=T_\mathrm Z-\bigl(T_\mathrm Z-T(t)\bigr)\,\mathrm{e}^{-\Delta t/\tau}.$$

So the distance to room temperature decreases by the same factor in every step, as with the tea.

```python erwaermen.py
# A bottle from the refrigerator warms up in the room: when has it covered 90 % of the way?
import math
tau = 30.0              # time constant in min
dt = 0.1                # time step in min
zimmer = 21.0           # room temperature in degrees
flasche = 6.0           # temperature of the bottle at the start in degrees
faktor = math.exp(-dt / tau)
schritte = 0
while flasche < 19.5:   # 90 % of the way from 6 to 21 degrees
    flasche = zimmer - (zimmer - flasche) * faktor
    schritte = schritte + 1
print(f"Schritte: {schritte}, Zeit: {schritte * dt:.1f} min, Temperatur: {flasche:.2f} Grad")
print(f"Formel tau * ln(10): {tau * math.log(10):.2f} min")
```

```console Linux
$ python3 erwaermen.py
Schritte: 691, Zeit: 69.1 min, Temperatur: 19.50 Grad
Formel tau * ln(10): 69.08 min
```

From $(T_\mathrm Z-T_0)\,\mathrm{e}^{-t/\tau}=0.1\,(T_\mathrm Z-T_0)$, it follows that $t=\tau\ln10\approx69.08$ min. The loop reports the first time step after that, 69.1 min. The displayed temperature 19.50 °C is rounded; it lies just above 19.5 °C.
:::
:::

:::aufgabe Exercise 14 ★ Asking until the input fits
<span class="anker" id="aufg-14"></span>

Write a script `eingabe_personen.py` that asks for the number of people and repeats the question until a number greater than 0 has been entered. Then it should output how much each person pays if everyone splits a bill of €47.50. Test it with the inputs $-5$, $0$ and $3$ one after the other.

:::loesung
The question appears once before the loop and once in the block; the loop runs as long as the last input is invalid.

```python eingabe_personen.py
# Keep asking for the number of people until it is greater than 0
personen = int(input("Anzahl der Personen: "))
while personen <= 0:
    print("Es muss mindestens eine Person sein.")
    personen = int(input("Anzahl der Personen: "))
print(f"Jede Person zahlt {47.50 / personen:.2f} Euro")
```

```console Linux
$ python3 eingabe_personen.py
Anzahl der Personen: -5
Es muss mindestens eine Person sein.
Anzahl der Personen: 0
Es muss mindestens eine Person sein.
Anzahl der Personen: 3
Jede Person zahlt 15.83 Euro
```

If you type a word instead of a number, `int` stops with a `ValueError`; catching it requires exception handling, which this chapter does not cover.
:::
:::
