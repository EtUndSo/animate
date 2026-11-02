---
title: Overview: Lowpass and Bandpass Systems
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3250100
summary: Distortionless transmission, ideal lowpass, complex envelope and group delay
tags: 
lang: en
---

## What this is about

Almost every transmission is meant to deliver a signal as unchanged as possible, but only within a certain frequency range: a lowpass passes the low frequencies, a bandpass passes a band around a carrier frequency. This chapter asks: *What exactly does “unchanged” mean, what does a sharply limited band cost, and how do you calculate with signals that ride on a high-frequency carrier?*



**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The reference model for this chapter
<ul>

<li>

⁠**RC lowpass** with $RC=1$ s as in Parts 1 to 3.

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

The script `rechnung_kap5.py` recomputes the numbers and curves. $\operatorname{si}(x)=\sin(x)/x$ as in [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).
:::
