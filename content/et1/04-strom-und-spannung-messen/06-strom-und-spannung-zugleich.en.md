---
title: Stage 5: Current and voltage at once
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Measuring Current and Voltage
order: 1140600
summary: Anyone who determines a resistance from R=U/I needs both instruments.
tags: 
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Anyone who determines a resistance from $R=U/I$ needs both instruments. One of them then lies in the measuring circuit of the other. This stage compares the two possible circuits.
:::

**The idea.** The voltmeter can be connected before or after the ammeter (Fig. [6](#abb-6)). If it is before the ammeter, the ammeter counts exactly the current through $R$, but the voltmeter measures the voltage across $R$ and the ammeter together. If it is directly across $R$, the voltage is right, but the ammeter also counts the current of the voltmeter.

:::abbildung et1/k4richtig 6
The two measuring circuits. In green the correct reading, in red the reading with the contribution of the other instrument.
:::

:::definition Definition 5.1 (Correct-current and correct-voltage measurement)
<span class="anker" id="satz-5-1"></span>

$U$ and $I$ are the readings; $U_R$ and $I_R$ are the values at the resistor.

Correct current: $I=I_R$, but $U=U_R+U_\mathrm{iA}\neq U_R$. It follows that

<span class="anker" id="gl-5-1"></span>
$$\frac UI=R+R_\mathrm{iA},\qquad f=+\frac{R_\mathrm{iA}}{R}. \tag{5.1}$$

Correct voltage: $U=U_R$, but $I=I_R+I_\mathrm{iV}\neq I_R$. It follows that

<span class="anker" id="gl-5-2"></span>
$$\frac UI=R\parallel R_\mathrm{iV},\qquad f=-\frac{R}{R+R_\mathrm{iV}}. \tag{5.2}$$
:::

⁠**How to read it:** $U_\mathrm{iA}$ is the voltage drop across the ammeter, $I_\mathrm{iV}$ the current through the voltmeter. $f$ is the error of $U/I$ with respect to $R$. It is not possible to read the current and the voltage at a resistor correctly at the same time. If the internal resistances are known, however, the result can be corrected: $R=U/I-R_\mathrm{iA}$ or $1/R=I/U-1/R_\mathrm{iV}$, respectively.

:::herleitung Quotient of the readings
Correct current: $U/I=(I_RR+I_RR_\mathrm{iA})/I_R=R+R_\mathrm{iA}$. Correct voltage: $I/U=(I_R+I_\mathrm{iV})/U_R=1/R+1/R_\mathrm{iV}$, so $U/I=R\parallel R_\mathrm{iV}$ and $f=(R\parallel R_\mathrm{iV})/R-1=-R/(R+R_\mathrm{iV})$.
:::

::::beispiel
The reference model in both circuits:

|  | Reading $U$ | Reading $I$ | $U/I$ and error |
|---|---|---|---|
| correct current | 9.000 V (across $R$: 8.950 V) | 4.972 mA | 1810 $\Omega$, $+0.56\,\%$ |
| correct voltage | 8.950 V | 5.017 mA (through $R$: 4.972 mA) | 1783.9 $\Omega$, $-0.89\,\%$ |

The mathematical correction leads back to 1800 $\Omega$ in both cases.
::::

**Which circuit?** Fig. [7](#abb-7) shows both errors versus $R$. Small resistors are measured with the correct-voltage circuit, because their current far exceeds that of the voltmeter. Large ones are measured with the correct-current circuit, because their voltage far exceeds the drop across the ammeter. The curves cross near 1.4 k$\Omega$ (Exercise [6](#aufg-6)). At 1.8 k$\Omega$, the correct-current circuit is slightly better.

:::abbildung et1/k4fehler 7
Magnitude of the relative error of $U/I$ for $R_\mathrm{iA}=10\,\Omega$ and $R_\mathrm{iV}=200$ k$\Omega$, both axes logarithmic. The dots belong to the reference model.
:::

:::ltspice Both measuring circuits
⁠**Draw:** source `voltage` with 9 V on net `q`. The ammeter is a `res` with 10, the voltmeter a `res` with 200k. Correct current: `RA1` from `q` to `a`, `RX1` = 1.8k from `a` to ground, `RV1` from `q` to ground. Correct voltage: `RA2` from `q` to `b`, `RX2` = 1.8k and `RV2` from `b` to ground.

⁠**Directives:** `.op`

⁠**What you see:** `I(RA1)` = 4.972 mA at `V(q)` = 9 V, so 1810 $\Omega$. `I(RA2)` = 5.017 mA at `V(b)` = 8.950 V, so 1783.9 $\Omega$. Then insert the values from Exercise [5](#aufg-5) and compare.
:::

:::frage Why not measure one after the other, first current, then voltage?
That does not help here. Alone in the circuit, the ammeter again shows 4.972 mA; alone across $R$, the voltmeter shows 9.000 V. The result is 1810 $\Omega$, as in the correct-current circuit: each instrument's own error remains.
:::

**Measuring resistance without an ammeter.** That is why a digital multimeter measures resistance differently. An accurate constant-current source (a current source with a known, fixed current) drives the current $I_\mathrm q$ through $R$, and only the voltage is measured: $R=U/I_\mathrm q\propto U$. The current is a round power of ten, so the display only has to set the decimal point and the prefix (milli, kilo, mega): 1 mA through 1.8 k$\Omega$ gives 1.800 V, displayed as 1.800 k$\Omega$. What remains is the error $R/(R+R_\mathrm{iV})$, at 10 M$\Omega$ therefore 0.018 %. With small resistances, the connecting leads interfere: 0.1 $\Omega$ of lead on 0.5 $\Omega$ is 20 %. The Kelvin measurement therefore separates the paths: two leads carry the current, two more pick off the voltage directly at the component. Almost no current flows through these, so their resistance has no effect.

:::aufgabe Exercise 5 ★★ Which circuit?
<span class="anker" id="aufg-5"></span>

Instruments as in the reference model, ranges suitably chosen, internal resistances unchanged. Calculate $U/I$ and $f$ in both circuits for (a) $R=100\,\Omega$ at 0.9 V and (b) $R=180$ k$\Omega$ at 9 V. (c) Show that both correction formulas return 1800 $\Omega$ from the reference model.

:::loesung
(a) Correct current: $U/I=110\,\Omega$, $f=+10\,\%$. Correct voltage: $U/I=100\,\Omega\parallel200\,\mathrm{k\Omega}=99.95\,\Omega$, $f=-0.05\,\%$.

(b) Correct current: $U/I=180.01$ k$\Omega$, $f=+0.0056\,\%$. Correct voltage: $U/I=180\,\mathrm{k\Omega}\parallel200\,\mathrm{k\Omega}=94.74$ k$\Omega$, $f=-47.4\,\%$: almost as much current flows through the voltmeter as through $R$ (45 µ A versus 50 µ A). So small resistors with correct voltage, large ones with correct current.

(c) $1810\,\Omega-10\,\Omega=1800\,\Omega$ and $1/(1/1783.94\,\Omega-1/200\,\mathrm{k\Omega})=1800\,\Omega$.
:::
:::

:::aufgabe Exercise 6 ★★★ Equal error
<span class="anker" id="aufg-6"></span>

For which $R$ are the two errors equal in magnitude? Calculate the exact value and show that for $R_\mathrm{iA}\ll R\ll R_\mathrm{iV}$ approximately $R\approx\sqrt{R_\mathrm{iA}R_\mathrm{iV}}$ holds.

:::loesung
$R_\mathrm{iA}/R=R/(R+R_\mathrm{iV})$ leads to $R^2-R_\mathrm{iA}R-R_\mathrm{iA}R_\mathrm{iV}=0$ with the positive solution

$$R=\frac{R_\mathrm{iA}}{2}+\sqrt{\frac{R_\mathrm{iA}^2}{4}+R_\mathrm{iA}R_\mathrm{iV}}=1419\,\Omega.$$

For $R\ll R_\mathrm{iV}$, the right-hand side becomes $R/R_\mathrm{iV}$, so $R^2\approx R_\mathrm{iA}R_\mathrm{iV}$ and $R\approx1414\,\Omega$. Both errors are about 0.7 % there.
:::
:::
