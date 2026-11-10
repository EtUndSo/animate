---
title: Overview: Lowpass and Bandpass Systems
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3250100
summary: Distortionless transmission, ideal lowpass, complex envelope and group delay
tags: 
lang: en
---

## What this is about

Almost every transmission is meant to deliver a signal as unchanged as possible, but only within a certain frequency range: a lowpass passes the low frequencies, a bandpass passes a band around a carrier frequency. This chapter asks: *What exactly does “unchanged” mean, what does a sharply limited band cost, and how do you calculate with signals that ride on a high-frequency carrier?*



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**RC lowpass** with $RC=1$ s as in [Chapters 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) to 3.

</li>

<li>

⁠**Ideal lowpass** with $f_\mathrm g=1$ Hz (also 2 Hz for comparison).

</li>

<li>

⁠**Ideal bandpass** with the center frequency $f_0=10$ Hz and the bandwidth $\Delta f=2$ Hz.

</li>

<li>

⁠**Discrete-time lowpass** with $f_\mathrm g=0.2$ (normalized to the sampling rate) and 21 coefficients.

</li>

</ul>

The script `rechnung_kap5.py` recomputes the numbers and curves. $\operatorname{si}(x)=\sin(x)/x$ as in [Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).
:::
