---
title: Overview: Correlation Functions
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260100
summary: How similar are two signals, and how is the energy distributed over frequency?
tags: 
lang: en
---

## What this is about

A radar sends out a pulse and searches the received signal for its echo. A mobile phone searches the noise for a known synchronization sequence. Both ask the same question: *How similar is one signal to another, and at which shift is it most similar?* The answer is given by the correlation function. Its Fourier transform also tells you how the energy of a signal is distributed over the frequencies.



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
Rectangular pulse $\operatorname{rect}(t)$, triangle $\Lambda(t)$, exponential pulse $\varepsilon(t)\mathrm{e}^{-t}$ (the impulse response of the RC circuit with $RC=1$ s) and the sequence $(1,2,1)$. The script `rechnung_kap6.py` recomputes the numbers.
:::
