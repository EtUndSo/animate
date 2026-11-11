---
title: Overview: Sampling and Discrete-Time Systems
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3240100
summary: From the continuous signal to a sequence of numbers: sampling theorem, discrete convolution, DFT, FFT and z-transform
tags: samples
lang: en
---

## What this is about

A computer cannot store a function $s(t)$, only a sequence of numbers. The signal is therefore measured at fixed intervals $T$, and one works with the __samples__ $s(nT)$. Two questions shape this chapter: *Is information lost in the process?* And: *How do you calculate with sequences of numbers the way [Chapters 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) to 3 calculated with functions?*

**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Sampling rate** $f_\mathrm A=1/T=1$ kHz ($T=1$ ms). Test signals: cosine oscillations at 300 Hz and 700 Hz.

</li>

<li>

For sequences, the frequency is normalized to the sampling rate: $f=1$ corresponds to $f_\mathrm A$. With $f_\mathrm A=1$ kHz, $f=0.3$ therefore means 300 Hz.

</li>

<li>

⁠**Recursive system** $g(n)=s(n)+0.6\,g(n-1)$.

</li>

<li>

⁠**DFT example** $s_d=(1,\,2,\,0,\,-1)$.

</li>

</ul>

:::
