---
title: Solutions by trying: guess and check, approximation with a tolerance
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6040700
summary: With conditions and loops, a program can solve equations for which it knows no formula: it tries out candidates and checks each one.
tags: Guess and check, exhaustive search, approximation, stepping method
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
With conditions and loops, a program can solve equations for which it knows no formula: it tries out candidates and checks each one. This section shows the simplest way to do this, using the example of the square root, where you can easily check every result, and shows why this way is far too slow for accurate results.
:::

### Guess and check

<span class="anker" id="stufe-6-1"></span>

The task is to find the square root of an integer, say of 49. Even if you know no formula, you can still check any number for whether it gives 49 when multiplied by itself.

**A combination lock.** With a three-digit combination lock, you can try all combinations from 000 to 999 in order. After 1000 tries at the latest, it is open, or you know that no combination fits.

:::definition Definition 6.1 (Guess and check)
<span class="anker" id="satz-6-1"></span>

__Guess and check__, also called __exhaustive search__, goes through the possible solutions in a fixed order and checks each one. It stops as soon as a candidate fits or it is certain that none of the remaining ones can fit.
:::

::::beispiel the integer square root
The candidates are $g=0,1,2,\ldots$. As long as $g^2<a$, $g$ cannot be the square root, and the loop moves on to the next one. It ends at the first $g$ with $g^2\ge a$, and then there are two cases: either $g^2=a$, and then $g$ is the square root, or $g^2>a$, and then $a$ has no integer square root, because all smaller candidates had $g^2<a$, and all larger ones have $g^2>a$ all the more (in the outputs, “Wurzel” is German for “root” and “nach … Schritten” for “after … steps”).

```python wurzel_raten.py
# Integer square root by guess and check: g = 0, 1, 2, ... until g*g is at least a
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

The loop is certain to end, because $g$ grows by 1 in every iteration, and at some point $g^2\ge a$. How long that takes is the weakness of the method: the number of steps is the smallest integer $g$ with $g^2\ge a$, that is, about $\sqrt a$. For $a=10^{12}$, that is a million steps; with every two more digits in $a$, it takes ten times as long.
::::

⁠**In short:** Guess and check is certain to find a solution or to show that there is none, but it needs as many steps as there are candidates.

### Approximation with a tolerance

<span class="anker" id="stufe-6-2"></span>

For $\sqrt2$, guessing fails, because $\sqrt2$ is not an integer, not even a fraction. There is also no `float` whose square is exactly 2; even the built-in value does not satisfy the equation:

```console
>>> import math
>>> math.sqrt(2) ** 2
2.0000000000000004
>>> math.sqrt(2) ** 2 == 2
False
```

A loop that waits for `g * g == 2` would therefore never end.

**A target.** In target shooting, a shot counts as a hit if it lies in the inner ring, not only if it hits the exact center. In the same way, you settle for a number $g$ whose square lies close enough to $a$.

:::definition Definition 6.2 (Approximation with a tolerance)
<span class="anker" id="satz-6-2"></span>

A number $g$ is an __approximation__ of $\sqrt a$ with the tolerance $\varepsilon>0$ if $|g^2-a|<\varepsilon$. The tolerance $\varepsilon$ determines how close “close enough” is; it is a freely chosen number and has nothing to do with the machine epsilon $\varepsilon_{\mathrm M}$.
:::

The simplest method for finding such an approximation is called the __stepping method__ here: you start at $g=0$ and increase $g$ in fixed steps of step size $h$ until $|g^2-a|<\varepsilon$.

::::beispiel
$\sqrt{25}$ with $\varepsilon=0.01$ and step size $h=0.0001$. The loop has a second condition: it also stops when $g^2$ already lies above $a$, because then no further step can hit.

```python wurzel_schritte.py
# Search for the square root in small steps until g*g is close enough to a
a = 25.0                                  # number whose square root is sought
eps = 0.01                                # tolerance for |g*g - a|
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

The loop stops at the first $g$ whose square lies above $25-0.01=24.99$; that is $g=4.999$. The output shows `4.999000000001688` (“Näherung” is German for “approximation”), because $g$ arose from almost 50 000 additions, each of which was rounded, as with the floating-point trap in subsection [3.3](wiederholen-mit-while.html#stufe-3-3).
::::

⁠**In short:** With floating-point numbers, you do not look for an exact solution but for one that meets a tolerance.

### Step size and tolerance

<span class="anker" id="stufe-6-3"></span>

The stepping method has two knobs to turn, $h$ and $\varepsilon$, and they are linked.

**A narrow ditch.** The values of $g$ that meet the tolerance form a narrow range around $\sqrt a$, like a ditch across a path. If you take large steps, you can step over the ditch without ever falling in.

How wide is the range? From $g^2-a=(g-\sqrt a)(g+\sqrt a)$ and $g+\sqrt a\approx2\sqrt a$ near the solution, it follows that $|g^2-a|<\varepsilon$ means roughly $|g-\sqrt a|<\varepsilon/(2\sqrt a)$. So the range is about $\varepsilon/\sqrt a$ wide, for $a=25$ and $\varepsilon=0.01$ from 4.999 to 5.001.

::::beispiel a step that is too large
With $h=0.003$, the candidates lie at …, 4.998, 5.001, …. The square of the first is 24.980, that of the second 25.010; both lie outside the tolerance (“übersprungen” is German for “skipped”):

```console Linux
$ python3 wurzel_schritte.py
Schrittweite h = 0.003
übersprungen: g = 5.0010000000000785 nach 1667 Schritten
```

Without the second condition `g * g <= a`, the loop would run on forever here, further and further away from the solution.
::::

**The cost.** So the step size may be at most as large as the range, $h\lesssim\varepsilon/\sqrt a$, and then the method needs about $\sqrt a/h\gtrsim a/\varepsilon$ steps. For $\sqrt{25}$ with $\varepsilon=0.01$, that is a few thousand to tens of thousands, which takes a fraction of a second. For $\sqrt2$ to twelve digits, $\varepsilon=10^{-12}$, it is about $2\cdot10^{12}$ steps. On a typical computer, a Python loop manages roughly ten million simple iterations per second; that gives $2\cdot10^5$ s, more than two days. Section [7](die-bisektion.html#stufe-7) shows how to reach twelve digits in 41 steps.

⁠**In short:** The step size must be smaller than the range the tolerance allows, and that is why the number of steps grows with $a/\varepsilon$.

:::hintergrund Why a tolerance is necessary, even for the best floating-point number
Between 1 and 2, adjacent `float` values lie at a spacing of $\varepsilon_{\mathrm M}=2^{-52}$ ([Chapter 2, Section 5.2](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-2)). $\sqrt2$ lies between two of them, `1.414213562373095` and `1.4142135623730951`. Their squares, rounded to the nearest `float`, are `1.9999999999999996` and `2.0000000000000004`; neither of the two values is 2. For every other `float`, the square lies even further away. So the equation $g^2=2$ has no solution among the `float` values, and the smallest achievable deviation is $4.44\cdot10^{-16}$. Every loop that searches for a square root therefore needs a tolerance, and this tolerance must be larger than the deviation that can be achieved with `float` at all.
:::

### Exercises for Section [6](#stufe-6)

<span class="anker" id="stufe-6-4"></span>

:::aufgabe Exercise 24 ★★ The integer cube root
<span class="anker" id="aufg-24"></span>

Write a script `kubikwurzel.py` that uses guess and check to find the integer cube root of an integer $k$, that is, an integer $g$ with $g^3=k$, or reports that there is none. Negative numbers should work, too. Hint: search for the root of $|k|$ and then give it the sign of $k$. Test it with 27, $-8$ and 10.

:::loesung
```python kubikwurzel.py
# Integer cube root by guess and check, also for negative numbers
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

For negative $k$, $(-g)^3=-g^3$; so the root of $|k|$ with the opposite sign is the one sought. For 10, the search ends at $g=3$ with $27>10$, and no smaller candidate fit.
:::
:::

:::aufgabe Exercise 25 ★★ The step size for $\sqrt{10}$
<span class="anker" id="aufg-25"></span>

Change `wurzel_schritte.py` so that it searches for $\sqrt{10}$ with $\varepsilon=0.01$. Try the step sizes 0.001, 0.003, 0.004 and 0.005. Which ones meet the tolerance, and how many steps do they need? Estimate the width of the admissible range for $g$ beforehand and use it to explain the results.

:::loesung
The admissible $g$ lie between $\sqrt{9.99}\approx3.16070$ and $\sqrt{10.01}\approx3.16386$; the range is about 0.0032 wide, as the estimate $\varepsilon/\sqrt{10}=0.0032$ says. Step sizes up to this width are certain to hit it, larger ones only with luck.

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

With $h=0.004$, the candidates jump from 3.160 to 3.164; the first lies just below the range, the second just above it. With $h=0.005$ likewise, from 3.160 to 3.165. The script `schritte10.py` is `wurzel_schritte.py` with `a = 10.0`.
:::
:::

:::aufgabe Exercise 26 ★ How long guessing takes
<span class="anker" id="aufg-26"></span>

How many steps does `wurzel_raten.py` need for $a=10^{14}$ and for $a=10^{20}$? Roughly how long does that take at ten million iterations per second? Measure it for $a=10^{14}$ if you have the patience.

:::loesung
`wurzel_raten.py` needs about $\sqrt a$ steps: ten million for $a=10^{14}$, ten billion for $a=10^{20}$. At ten million iterations per second, that is one second and 1000 s, respectively, the latter about a quarter of an hour. On the computer used to test this chapter, $a=10^{14}$ took just over a second (between 1.1 s and 1.6 s, depending on the system). Every two additional digits in $a$ multiply the time by ten.
:::
:::
