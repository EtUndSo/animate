---
title: Key points so far
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6041100
summary: Conditions, if, while and for, roots and zeros by guessing, halving and tangents
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

Comparisons return `bool`; `a <= x <= b` checks a range. Strings are compared character by character according to the numbers of their characters, `"10" < "9"`.

</li>

<li>

`not`, `and`, `or` with the precedence `not` before `and` before `or`. `and` and `or` use short-circuit evaluation and return one of their operands.

</li>

<li>

Of the values known so far, `False`, `None`, every zero and `""` count as false, all others as true.

</li>

<li>

`if`, `elif`, `else`: the block of the first true condition runs. A block is recognized by its indentation; four spaces are usual.

</li>

<li>

`while Bedingung:` repeats as long as the condition is true before the iteration; if the block changes nothing about it, the loop runs forever, and Ctrl+C interrupts it with `KeyboardInterrupt`. Never wait for a `float` with `!=`.

</li>

<li>

`for k in range(start, stop, schritt):` runs through integers up to just before `stop`; you calculate floating-point steps from the counter.

</li>

<li>

`break` ends the innermost loop, `continue` the current iteration. An accumulator starts with 0 (sum, count) or 1 (product).

</li>

<li>

Guess and check: about $\sqrt a$ steps. Stepping method with a tolerance: about $a/\varepsilon$ steps; steps that are too large jump over the solution.

</li>

<li>

Bisection: sign change, halve the interval, $\lceil\log_2(L/\varepsilon)\rceil$ steps for the initial width $L$, one bit per step.

</li>

<li>

Newton: $g\leftarrow g-f(g)/f'(g)$, Heron's recipe for the square root; $d_{n+1}=d_n^2/(2g_n)$, the digits double, but only near the solution and with $f'\ne0$.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

A program takes different paths depending on the data by checking the truth value of a condition and, depending on it, executing an indented block once (`if`) or again and again (`while`, `for`).

</li>

<li>

The square root of 2 is the zero of $x^2-2$; bisection halves an interval with a sign change and needs 41 steps for twelve digits, while Newton's method follows the tangent line, squaring the error as it goes, and needs only 5.

</li>

<li>

Because floating-point numbers are rounded, every such method ends not at equality but at a tolerance, and the tolerance must fit the size of the numbers, otherwise the loop runs forever.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from two ideas: every decision and every repetition depends on a truth value, and every approximation method is a loop that shrinks a range of uncertainty until it lies below a tolerance. How fast that goes depends on how much a single step learns about the solution.

| Result | Where it comes from |
|---|---|
| `1 < x < 10` means the same as in mathematics | a chained comparison becomes `and` (Section [1](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1)) |
| `n != 0 and 10 / n > 1` is safe | short-circuit evaluation: the right side only if needed (Section [1](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1)) |
| `eingabe or "Standard"` | `or` returns the deciding operand (Section [1](bedingungen-vergleiche-und-logische-operatoren.html#stufe-1)) |
| Indentation is mandatory | it replaces the braces around a block (Section [2](entscheidungen-if-elif-und-else.html#stufe-2)) |
| `while x != 1.0` does not end | rounding errors accumulate, $1.0$ is skipped (Section [3](wiederholen-mit-while.html#stufe-3)) |
| `range(n)` has exactly $n$ numbers | the stop is not included (Section [4](zahlen-mit-for-und-range.html#stufe-4)) |
| A sum starts at 0, a product at 1 | empty sum and empty product (Section [5](schleifen-steuern-verschachteln-und-ergebnisse-sammeln.html#stufe-5)) |
| Guessing and stepping are slow | one step rules out only one candidate or a piece $h$ (Section [6](losungen-durch-probieren-raten-und-prufen-naherung-mit-toleranz.html#stufe-6)) |
| Bisection: 41 steps for $\sqrt2$ | one step halves the range, one bit per step (Section [7](die-bisektion.html#stufe-7)) |
| Newton: 5 steps for $\sqrt2$ | the tangent line has a quadratic error (Section [8](das-newton-verfahren.html#stufe-8)) |
| Newton crawls from a starting rate far away | there $f/f'\approx q/n$, so $q$ decreases per step only by about one $n$-th (Section [9](anwendung-der-zinssatz-eines-ratenkredits.html#stufe-9)) |
