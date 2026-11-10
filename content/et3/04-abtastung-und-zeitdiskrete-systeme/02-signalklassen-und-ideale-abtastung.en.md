---
title: Stage 1: Signal classes and ideal sampling
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3240200
summary: What kinds of signals are there, and how is sampling described mathematically?
tags: analog, discrete-time, digital, ideal sampler
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
What kinds of signals are there, and how is sampling described mathematically?
:::

**Four classes.** Time and amplitude can each be continuous or discrete. An __analog__ signal is continuous in both. A __discrete-time__ signal has values only at the times $nT$, but these with arbitrary precision. A __digital__ signal is in addition stepped in amplitude (quantized), because a computer can represent only finitely many numbers. This chapter deals with the discretization of time. The quantization of the amplitude is a separate topic.

**From the real to the ideal sampler.** In every clock cycle, a real sampler closes a switch for the short time $T_0$:

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

If $T_0$ is made shorter and shorter, only the values $s(nT)$ remain. Mathematically, the rectangle is replaced by a Dirac impulse. This is the __ideal sampler__:

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

The sampled signal is a train of Dirac impulses, each with a sample as its weight. The second step is the sifting property $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$. In this form, sampled signals can be treated with all the tools for continuous signals.
