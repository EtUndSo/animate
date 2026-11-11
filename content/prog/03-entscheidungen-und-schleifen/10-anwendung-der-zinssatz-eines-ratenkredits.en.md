---
title: Application: the interest rate of an installment loan
pfad: Computer Science / Programming / Python / Decisions and Loops
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Chapter 3: Decisions and Loops
order: 6041000
summary: Bisection and Newton's method are not made for square roots but for equations that cannot be solved for the unknown.
tags: remaining balance, annuity formula, effective annual interest rate
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
Bisection and Newton's method are not made for square roots but for equations that cannot be solved for the unknown. This section solves such an equation from everyday life: what interest rate is hidden in a loan that you pay back in equal monthly payments?
:::

:::::vorwissen What you need for this: interest, payments and remaining balance

<span class="anker" id="stufe-9-1"></span>

A car dealership offers a car for €20 000, or alternatively for 60 monthly payments of €400. Together, that is €24 000; the €4000 extra is the interest. What interest rate is hidden in it?

If you take out a loan for the amount $K$, you owe $K$ at first. What still has to be paid back at any given time is called the __remaining balance__ $S$. Every month, interest is added: with the monthly interest rate $r$, written as a decimal number (0.5 % is 0.005), the remaining balance grows to $S\,(1+r)$. Then you pay the monthly payment $R$, and the remaining balance decreases by $R$. With the abbreviation $q=1+r$, the following therefore holds from month to month:

$$S_0=K,\qquad S_{k+1}=S_k\,q-R .$$

The loan is paid off after $n$ months exactly when $S_n=0$.

If you substitute the rule into itself again and again, you get a formula for $S_n$:

$$S_1=Kq-R,\qquad S_2=Kq^2-Rq-R,\qquad\ldots,\qquad S_n=Kq^n-R\,\bigl(q^{n-1}+q^{n-2}+\cdots+q+1\bigr).$$

With the value of the sum in the parentheses, $(q^n-1)/r$ for $r\ne0$, the condition $S_n=0$ gives the __annuity formula__

$$R=\frac{K\,r\,q^n}{q^n-1}=\frac{K\,r}{1-q^{-n}} .$$

It gives the monthly payment for a known interest rate.

:::herleitung The sum in the parentheses
Let $G=1+q+q^2+\cdots+q^{n-1}$. Multiplying by $q$ shifts every term by one place: $qG=q+q^2+\cdots+q^n$. In the difference $qG-G$, all terms cancel except $q^n$ and $1$, so $(q-1)\,G=q^n-1$, and with $q-1=r$

$$G=\frac{q^n-1}{r}\qquad(r\ne0).$$

Substituting this gives $S_n=Kq^n-R\,(q^n-1)/r$. From $S_n=0$, it follows that $R\,(q^n-1)=K\,r\,q^n$, and dividing by $q^n-1$ gives the annuity formula; the second fraction results from dividing the numerator and the denominator by $q^n$.
:::

In the EU, loan offers must state an __effective annual interest rate__. It converts the cost of the loan to one year, with compound interest. Without further costs and with equal monthly payments, it is $(1+r)^{12}-1$: the interest rate that the monthly interest rate $r$ turns into over twelve months with compound interest.

::::beispiel
For the car, $K=20\,000$ euros and $n=60$. At a monthly interest rate of 0.5 %, the payment would be $20\,000\cdot0.005/(1-1.005^{-60})\approx386.66$ euros, that is, less than the €400 required. At 1 %, it would be €444.89, that is, more. The monthly interest rate sought therefore lies between 0.5 % and 1 %.
::::

⁠**In short:** Every month, the remaining balance grows by the interest and decreases by the payment; at the right interest rate, it is exactly zero after the last payment.

:::::

### The interest rate as a zero

<span class="anker" id="stufe-9-2"></span>

If you plot the payment that belongs to each monthly interest rate according to the annuity formula against the interest rate, and add the required payment of €400 as a horizontal line, the two intersect at the interest rate sought (Fig. [11](#abb-11)).

:::abbildung prog/k3kredit 11
The monthly payment for a loan of €20 000 with 60 payments as a function of the monthly interest rate (blue), and the required payment of €400 (orange). Their intersection is the interest rate hidden in the offer. Without interest, the payment would be $20\,000/60\approx333.33$ euros; with every additional tenth of a percent, it rises.
:::

You can write the intersection as a zero. The simplest way is with the remaining balance after the last payment, viewed as a function of the interest rate:

$$f(r)=S_n=Kq^n-R\,\bigl(q^{n-1}+q^{n-2}+\cdots+q+1\bigr),\qquad q=1+r .$$

If $f(r)>0$, the required payment is not enough at this interest rate, and some debt remains; if $f(r)<0$, you would have paid back too much. At the interest rate sought, $f(r)=0$.

At $r=0$, there is no interest, and $f(0)=K-nR=20\,000-24\,000=-4000$ euros remains, so $f(0)<0$. At the interest rate $r=R/K$, here 2 % per month, the interest on the full debt is exactly as large as the payment: the remaining balance stays at $K$, and $f(R/K)=K>0$. $f$ is continuous, so by the intermediate value theorem there is a zero between 0 and $R/K$. There is also only one. If you divide $f(r)$ by $q^n$, you get $K-R\,\bigl(q^{-1}+q^{-2}+\cdots+q^{-n}\bigr)$. Every term $q^{-k}$ becomes smaller as $r$ grows; so this expression is strictly increasing. Because $q^n$ is positive, $f$ has the same sign as this expression and changes it exactly once. The equation $f(r)=0$ cannot be solved for $r$ with the usual means, because for $n=60$ it is an equation of degree 60 in $q$.

⁠**In short:** The interest rate sought is the only zero of the remaining balance $f(r)$ between 0 and $R/K$.

:::hintergrund Is there a formula after all?
$f(r)=0$ is a polynomial equation of degree $n$ in $q$. For degree 2, you know the quadratic formula from school, and for degrees 3 and 4 there are also formulas that use only the basic arithmetic operations and roots. For degree 5 and higher, there is no such formula that works for all polynomials; this is the Abel–Ruffini theorem. It does not rule out that special equations like this one do have a solution in terms of roots; however, no formula for the interest rate of an arbitrary loan is known. Spreadsheets therefore calculate the interest rate step by step, as this chapter does. Their function for this is called RATE. It starts from a guess, 10 % if none is given, and reports an error if the successive results have not come within 0.0000001 of each other after 20 steps.
:::

### The interest rate by bisection

<span class="anker" id="stufe-9-3"></span>

Bisection needs only the sign of $f$ and the starting interval $[0,R/K]$. Here, $f(\mathit{lo})<0$ as with the square root, so the cases in the loop are the same as there: if the remaining balance at the interest rate at the midpoint is negative, you would have paid back too much at this rate, and the rate sought is higher. The script calculates the value $f(\mathit{mitte})$ without a formula: an inner loop updates the remaining balance month by month according to the rule $S_{k+1}=S_k\,q-R$. The two loops are nested as in subsection [5.3](schleifen-steuern-verschachteln-und-ergebnisse-sammeln.html#stufe-5-3).

```python kredit_bisektion.py
# Interest rate of an installment loan: zero of the remaining balance f(r) by bisection
kredit = 20000.0      # amount borrowed in euros
monate = 60           # term in months
rate = 400.0          # monthly payment in euros
eps = 1e-12           # interval width for the monthly interest rate

lo = 0.0              # f(0) = kredit - monate * rate < 0
hi = rate / kredit    # f(hi) = kredit > 0: the interest uses up the whole payment
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    f = kredit                    # remaining balance at rate mitte, month by month
    for monat in range(monate):
        f = f * (1 + mitte) - rate
    if f < 0:         # paid back too much: the rate is higher than mitte
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
zins = (lo + hi) / 2
print(f"Monatszins: {zins * 100:.4f} %, Schritte: {schritte}")
print(f"effektiver Jahreszins: {((1 + zins) ** 12 - 1) * 100:.2f} %")
```

```console Linux
$ python3 kredit_bisektion.py
Monatszins: 0.6183 %, Schritte: 35
effektiver Jahreszins: 7.68 %
```

Theorem [7.3](die-bisektion.html#satz-7-3) predicts the number of steps: $\lceil\log_2(0.02/10^{-12})\rceil=\lceil34.2\rceil=35$. For this, bisection needs neither the derivative nor a good starting value, only the sign change. The car dealership's offer corresponds to a monthly interest rate of 0.6183 % and an effective annual interest rate of 7.68 %.

⁠**In short:** Bisection reliably finds the monthly interest rate of 0.6183 % in 35 steps.

### The interest rate by Newton's method

<span class="anker" id="stufe-9-4"></span>

For Newton's method, you need the derivative $f'(r)$, and you get it from the same loop as $f$. From $S_{k+1}=S_k\,(1+r)-R$, the product rule $(u\,v)'=u'v+u\,v'$ from school gives

$$S'_0=0,\qquad S'_{k+1}=S'_k\,(1+r)+S_k ,$$

because the loan amount $K$ and the payment $R$ do not depend on the interest rate, and $1+r$ has the derivative 1 with respect to $r$. In words: if the interest rate rises a little, the additional interest on the remaining balance $S_k$ is added every month, and whatever increase the remaining balance already carries is charged interest along with it. At the end, $f'(r)=S'_n$. In the script, the line for the derivative must come before the line for the remaining balance, because it still needs the remaining balance of the previous month.

The script stops as soon as a Newton step changes the interest rate by less than $10^{-12}$, and it has an emergency brake after 1000 steps. It asks for the starting value:

```python kredit_newton.py
# Interest rate of an installment loan: zero of the remaining balance f(r) with Newton's method
kredit = 20000.0      # amount borrowed in euros
monate = 60           # term in months
rate = 400.0          # monthly payment in euros

zins = float(input("Startwert für den Monatszins: "))
schritt = 1.0         # length of the last Newton step, arbitrarily large at first
schritte = 0
while abs(schritt) > 1e-12 and schritte < 1000:
    f = kredit        # remaining balance at this rate, month by month
    f_strich = 0.0    # its derivative with respect to the rate
    for monat in range(monate):
        f_strich = f_strich * (1 + zins) + f    # first, because f still holds the old balance
        f = f * (1 + zins) - rate
    schritt = -f / f_strich
    zins = zins + schritt
    schritte = schritte + 1
print(f"Monatszins: {zins * 100:.4f} %, Schritte: {schritte}")
```

```console Linux
$ python3 kredit_newton.py
Startwert für den Monatszins: 0.01
Monatszins: 0.6183 %, Schritte: 5
$ python3 kredit_newton.py
Startwert für den Monatszins: 0
Monatszins: 0.6183 %, Schritte: 6
$ python3 kredit_newton.py
Startwert für den Monatszins: 1
Monatszins: 0.6183 %, Schritte: 47
```

With a starting value nearby, 1 % per month, Newton needs 5 steps, and from the starting value 0, it needs 6. But if you type `1` for 1 %, you start at 100 % per month, and then it takes 47 steps, more than bisection. The reason is compound interest. Far above the solution, the remaining balance grows almost only through compound interest, roughly like a fixed amount $c$ times $q^n$. For a function $c\,q^n$, $f/f'=c\,q^n/(c\,n\,q^{n-1})=q/n$, so this holds roughly here. Every Newton step therefore lowers $q$ only by about one $n$-th of its value; here, $q$ is multiplied by about $59/60$. From $q=2$ to $q\approx1.006$, that takes $\ln(2/1.006)/\ln(60/59)\approx41$ steps before the fast phase begins.

This leads to the usual division of labor: you narrow down the solution with a safe method or with prior knowledge, for installment loans about 0 % to 2 % per month, and then let Newton fetch the last digits.

⁠**In short:** Started close to the solution, Newton needs 5 steps; far away, it crawls, because $q$ decreases in every step only by about one $n$-th, and it is then slower than bisection.

:::hintergrund How ready-made solvers safeguard Newton's method
The crawling here and the cycle in subsection [8.5](das-newton-verfahren.html#stufe-8-5) have the same cause: far from the zero, the tangent line describes the function poorly, and its step is too short or too long. Ready-made solvers therefore safeguard the method. Two kinds are common.

The first is a safety net made of bisection. Like bisection, the solver keeps an interval with a sign change, and in every step it first tries the Newton step. If this step lands outside the interval or shrinks it too little, the solver takes the midpoint instead. At the new point, it determines the sign of $f$ and uses it to replace an endpoint, as in bisection. This way, every step stays in the interval, a crawling Newton step is replaced by a halving step, and near the zero, where the Newton steps are good, the solver is as fast as Newton.

The second is damping. It also helps where there is no interval, for example when many equations are solved at once. The solver takes the full Newton step $\Delta=-f(g)/f'(g)$ only if $|f|$ is smaller afterward than before; otherwise, it halves the step until it is. This always succeeds as long as $f(g)\ne0$ and $f'(g)\ne0$: for a fraction $\lambda$ of the step, the tangent line gives $f(g+\lambda\Delta)\approx f(g)+\lambda f'(g)\,\Delta=(1-\lambda)\,f(g)$, and for small $\lambda$, the error of this approximation is small compared with $\lambda\,|f(g)|$. So a short step in the direction of the tangent line always decreases $|f|$. Near the zero, the full step is accepted, and the method keeps its speed.
:::

### Exercises for Section [9](#stufe-9)

<span class="anker" id="stufe-9-5"></span>

:::aufgabe Exercise 34 ★★★ Another loan
<span class="anker" id="aufg-34"></span>

A TV costs €1000, or alternatively 24 monthly payments of €45.

<ol class="al">

<li>

Use Theorem [7.3](die-bisektion.html#satz-7-3) to predict how many steps bisection needs with $\varepsilon=10^{-9}$. Then determine the monthly interest rate and the effective annual interest rate with bisection.

</li>

<li>

Determine the monthly interest rate with Newton's method, once from the starting value 0.01 and once from the starting value 1. Estimate the second number of steps beforehand.

</li>

<li>

Also convert the monthly interest rate to a year without compound interest, that is, multiply it by 12, and compare the result with the effective annual interest rate. Why is the effective annual interest rate larger?

</li>

</ol>

:::loesung
(a) The starting interval is $[0,R/K]=[0,\,0.045]$, so $\lceil\log_2(0.045/10^{-9})\rceil=\lceil25.4\rceil=26$. The script is `kredit_bisektion.py` with the new values and `eps = 1e-9`:

```console Linux
$ python3 fernseher_bisektion.py
Monatszins: 0.6251 %, Schritte: 26
effektiver Jahreszins: 7.76 %
```

(b) From the starting value 1, that is, with $q=2$, $q$ decreases in each step by only about one 24th. Down to $q\approx1.006$, that takes about $\ln(2/1.006)/\ln(24/23)\approx16$ steps, plus a few for the last digits. The script `fernseher_newton.py` is `kredit_newton.py` with the new values:

```console Linux
$ python3 fernseher_newton.py
Startwert für den Monatszins: 0.01
Monatszins: 0.6251 %, Schritte: 5
$ python3 fernseher_newton.py
Startwert für den Monatszins: 1
Monatszins: 0.6251 %, Schritte: 22
```

The crawling is shorter than for the car with 60 payments, because here $q$ decreases in each step by one 24th instead of one 60th.

(c) Without compound interest, the result is $12\cdot0.6251\,\%=7.50\,\%$; with compound interest, it is the effective annual interest rate of 7.76 %. The difference arises because the interest of one month becomes part of the remaining balance and itself earns interest in the following months. Multiplied out, $(1+r)^{12}=1+12\,r+66\,r^2+\cdots$; the term $66\,r^2=66\cdot0.006251^2\approx0.0026$ alone accounts for about 0.26 percentage points.
:::
:::

:::aufgabe Exercise 35 ★★ When Newton lands at `nan`
<span class="anker" id="aufg-35"></span>

A home loan of €200 000 is paid back over 30 years, that is, in 360 monthly payments of €1000. Someone has “about 10 percent” in mind and enters the starting value 10 in `kredit_newton.py` with these numbers. What happens, and why does the loop end anyway? Does bisection work with these numbers? Justify your answer with the starting interval and check it by calculation. Then determine the interest rate with Newton's method from a sensible starting value.

:::loesung
The script `baukredit_newton.py` is `kredit_newton.py` with the new values:

```console Linux
$ python3 baukredit_newton.py
Startwert für den Monatszins: 10
Monatszins: nan %, Schritte: 1
```

With $r=10$, that is, 1000 % per month, $q=11$. The inner loop multiplies the remaining balance by 11 a total of 360 times, and $11^{360}\approx10^{375}$ lies far above the largest `float` of about $1.8\cdot10^{308}$. The remaining balance and the derivative become `inf` ([Chapter 2, Section 5.5](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-5)), and $\infty/\infty$ gives `nan` ([Chapter 2, Section 5.6](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-6)). As a result, the step and the new interest rate are `nan`. The loop ends anyway, because every comparison with `nan` except `!=` gives `False`; [Chapter 2, Section 7.3](/wissen/en/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-3) showed this with `nan == nan`. Here it affects the comparison in the condition:

```console
>>> nan = 1e309 - 1e309
>>> abs(nan) > 1e-12
False
```

The condition `abs(schritt) > 1e-12` is therefore false, and the script reports `nan` after one step, without an error message.

Bisection works. Its starting interval is $[0,R/K]=[0,\,0.005]$, and it evaluates $f$ only at midpoints of this interval. There, $q^{360}\le1.005^{360}\approx6.0$, so an overflow is ruled out:

```console Linux
$ python3 baukredit_bisektion.py
Monatszins: 0.3656 %, Schritte: 33
effektiver Jahreszins: 4.48 %
```

The number of steps is $\lceil\log_2(0.005/10^{-12})\rceil=\lceil32.2\rceil=33$. Newton with a sensible starting value, such as the upper limit 0.005, arrives at the same result:

```console Linux
$ python3 baukredit_newton.py
Startwert für den Monatszins: 0.005
Monatszins: 0.3656 %, Schritte: 6
```

As a decimal number, 10 % would be 0.1; the starting value 10, by contrast, means 1000 % per month. A program for other people should check such inputs beforehand, for example with a condition as in Section [2](entscheidungen-if-elif-und-else.html#stufe-2).
:::
:::
