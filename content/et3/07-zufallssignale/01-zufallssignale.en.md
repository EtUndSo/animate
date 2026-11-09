---
title: Overview: Random Signals
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270100
summary: Mean values, distributions, power spectral density, noise in systems and the optimal receiver
tags: 
lang: en
---

## What this is about

The noise of a resistor, speech, a data stream: such signals cannot be predicted. Their exact waveform is unknown, but their *average properties* are known: how large they typically are, how fast they change, which frequencies they contain. This chapter shows how to describe such random signals, what an LTI system does to them and how to detect a known signal in noise most reliably.



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Uniformly distributed random numbers** between $-\frac12$ and $\frac12$ (variance $\frac{1}{12}$), also as discrete-time white noise.

</li>

<li>

⁠**Resistor** $R=1\,\mathrm{k\Omega}$ at 290 K, bandwidth 20 kHz (audio).

</li>

<li>

⁠**Recursive system** $g(n)=s(n)+0.6\,g(n-1)$ from [Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html).

</li>

</ul>

The script `rechnung_kap7.py` recomputes the numbers, in part checking them with simulated random numbers.
:::
