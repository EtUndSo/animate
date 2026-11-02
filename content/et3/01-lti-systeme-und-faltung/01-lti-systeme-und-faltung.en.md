---
title: Overview: Signals, LTI Systems and Convolution
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / LTI Systems and Convolution
order: 3210100
summary: Why the response to a single impulse describes the whole system
tags: 
lang: en
---

## What this is about

A system takes in one signal and puts out another: an RC circuit smooths a voltage, a loudspeaker cabinet colors a sound, a measuring amplifier delays and amplifies. The question of this chapter is: *What do you need to know about a system to compute its output for any input signal?*

For the large class of linear, time-invariant systems (LTI systems), the answer is surprisingly short: the response to a single, infinitely short impulse. The tool that turns this one response into every other one is convolution.



**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The reference model for this chapter
<ul>

<li>

⁠**RC low-pass** with $T=RC=1$ s (for example $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Times in s, voltages in V, so all calculations are dimensionless.

</li>

<li>

⁠**Rectangular pulse** of height $a=1$ V and duration $T_0=1$ s, starting at $t=0$.

</li>

</ul>

The script `rechnung_kap1.py` recomputes the numbers and curves.
:::
