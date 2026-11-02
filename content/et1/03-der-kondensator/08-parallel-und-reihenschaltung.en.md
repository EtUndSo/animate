---
title: Stage 7: Parallel and series connection
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1130800
summary: Several capacitors can be treated like one.
tags: island
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
Several capacitors can be treated like one. The only question is which quantity the circuit makes the same for all of them.
:::

**The idea.** ⁠**Parallel:** All upper plates hang on one wire, all lower plates on another. A wire without current has the same potential everywhere, so the same voltage is across all the capacitors. The circuit acts like an enlarged plate, and the charges add. **Series:** The lower plate of $C_1$ and the upper plate of $C_2$, together with their connecting wire, form an __island__: a piece of conductor reached only through insulators (Fig. [7](#abb-7)). Charge can neither get in nor out there. If the island was uncharged, its sum stays zero: if the upper plate with $+Q$ attracts $-Q$ on the island, the missing counterpart must go as $+Q$ onto the next plate. So all carry the same charge, and the voltages add. The circuit acts like an enlarged separation.

:::abbildung et1/k3schaltungen 7
$C_1=100\,\mu\text{F}$ and $C_2=50\,\mu\text{F}$ at 9 V. Parallel: the same voltage; the charges add up to 1350 µC. In series: the same charge of 300 µC, because the island with the dashed outline stays neutral. The smaller capacitor gets the larger voltage.
:::

:::satz Theorem 7.1 (Total capacitance)
<span class="anker" id="satz-7-1"></span>

For $n$ capacitors connected in parallel (left) and $n$ initially uncharged capacitors connected in series (right),

<span class="anker" id="gl-7-1"></span>
$$C_\mathrm{G}=\sum_{i=1}^nC_i,\qquad\qquad\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}. \tag{7.1}$$

For two capacitors in series, $C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2}$, and the voltage divides according to $U_1=U_\mathrm{G}\,\dfrac{C_2}{C_1+C_2}$.
:::

:::herleitung Total capacitance
⁠**Parallel.** Constraint of the circuit: $U_i=U_\mathrm{G}$ for all $i$. Individual charge: $Q_i=C_iU_i=C_iU_\mathrm{G}$. Total charge: $Q_\mathrm{G}=\sum Q_i=U_\mathrm{G}\sum C_i$. With $C_\mathrm{G}=Q_\mathrm{G}/U_\mathrm{G}$ the left formula follows.

⁠**Series.** Constraint of the circuit: $Q_i=Q_\mathrm{G}$ for all $i$. Total voltage: $U_\mathrm{G}=\sum U_i$. Partial voltage: $U_i=Q_i/C_i=Q_\mathrm{G}/C_i$. So $U_\mathrm{G}=Q_\mathrm{G}\sum 1/C_i$, and with $U_\mathrm{G}=Q_\mathrm{G}/C_\mathrm{G}$ the right formula follows. For the divider: $U_1=Q_\mathrm{G}/C_1=U_\mathrm{G}\,C_\mathrm{G}/C_1=U_\mathrm{G}\,C_2/(C_1+C_2)$.
:::

⁠**How to read it:** $C_\mathrm{G}$ is the capacitance of a single capacitor that shows the same behavior at the two outer terminals. In parallel, $C_\mathrm{G}$ becomes larger than every individual value, in series smaller than the smallest. **Validity:** The right formula needs uncharged islands at the start. Otherwise the old island charge is conserved, and $Q_i=Q_\mathrm{G}$ holds only for the added charge.

**Example.** Parallel: $C_\mathrm{G}=150\,\mu\text{F}$, $Q_1=900\,\mu\text{C}$, $Q_2=450\,\mu\text{C}$. In series: $1/C_\mathrm{G}=1/(100\,\mu\text{F})+1/(50\,\mu\text{F})$, so $C_\mathrm{G}=33.3\,\mu\text{F}$. At 9 V, $Q=300\,\mu\text{C}$, $U_1=3$ V and $U_2=6$ V.

⁠**Limiting cases:** For $C_2\to\infty$, in series $C_\mathrm{G}\to C_1$: a huge capacitor behaves like a wire. For $C_2\to0$, in series $C_\mathrm{G}\to0$: the gap interrupts; in parallel, $C_1$ remains.

:::frage Why are the formulas exactly the reverse of those for resistors?
For resistors, $u=R\,i$: in series the voltages add at the same current, so $R$ adds. For the capacitor, $u=\frac1C\,q$: in series the voltages add at the same charge, so $1/C$ adds. **In short:** For the capacitor, $1/C$ plays the role of $R$.
:::

:::aufgabe Exercise 8 ★★ A mixed network
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Two capacitors of 10 µF and 20 µF are in parallel, with 60 µF in series with them, the whole across 9 V. Calculate $C_\mathrm{G}$, the total charge, all voltages and all individual charges.

</li>

<li>

Two identical capacitors with 100 µF and 16 V maximum voltage are in series. What capacitance and what maximum voltage does the chain have?

</li>

</ol>

:::loesung
(a) Parallel: $10+20=30\,\mu\text{F}$. In series with 60 µF: $C_\mathrm{G}=\frac{30\cdot60}{30+60}\,\mu\text{F}=20\,\mu\text{F}$. $Q=20\,\mu\text{F}\cdot9\,\mathrm{V}=180\,\mu\text{C}$. Across the 60 µF capacitor: $180\,\mu\text{C}/60\,\mu\text{F}=3$ V. Across the parallel block: $180\,\mu\text{C}/30\,\mu\text{F}=6$ V, together 9 V. The charge divides: $10\,\mu\text{F}\cdot6\,\mathrm{V}=60\,\mu\text{C}$ and $20\,\mu\text{F}\cdot6\,\mathrm{V}=120\,\mu\text{C}$.

(b) $C_\mathrm{G}=50\,\mu\text{F}$. With identical capacitors the voltage divides equally, so 16 V each and 32 V together.
:::
:::
