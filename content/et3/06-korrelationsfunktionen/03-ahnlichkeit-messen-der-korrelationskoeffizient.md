---
title: Stufe 2: Ähnlichkeit messen, der Korrelationskoeffizient
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260300
summary: Wie misst man mit einer Zahl, wie ähnlich zwei Signale sind?
tags: Korrelationskoeffizienten, orthogonal
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Wie misst man mit einer Zahl, wie ähnlich zwei Signale sind? Man misst, wie groß ihre Differenz ist.
:::

**Die Idee.** Die Energie der Differenz $\Delta(t)=s(t)-g(t)$ ist klein, wenn die Signale ähnlich sind. Ausmultipliziert:

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

Der Unterschied steckt also allein im Integral des Produkts. Damit die Größe der Signale nicht mitzählt, normiert man beide auf die Energie 1. Dann ist $E_\Delta=2-2\operatorname{Re}\,p_{sg}$ mit dem __Korrelationskoeffizienten__

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**So liest man das:** $|p_{sg}|\le1$ (Cauchy-Schwarz-Ungleichung). $p=1$ heißt $s=a\,g$ mit $a>0$: gleiche Form. $p=-1$ heißt $s=-a\,g$: gleiche Form, umgekehrtes Vorzeichen. $p=0$ heißt $\int s^*g\,\mathrm{d} t=0$, die Signale sind __orthogonal__, wie die Harmonischen einer Fourier-Reihe in [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html). Beispiel: $\operatorname{rect}(t)$ und $\Lambda(t)$ haben $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0{,}75$, $E_{\operatorname{rect}}=1$, $E_\Lambda=\frac23$, also $p=0{,}919$.

:::aufgabe Aufgabe 2 ★★ Korrelationskoeffizienten
<span class="anker" id="aufg-2"></span>

Berechne $p$ für (a) $\operatorname{rect}(t)$ und $\operatorname{rect}(t-0{,}5)$, (b) $\operatorname{rect}(t)$ und $\Lambda(t)$ (Ergebnis oben), (c) $\operatorname{rect}(t)$ und $\operatorname{sgn}(t)\operatorname{rect}(t)$.

:::loesung
(a) Die Rechtecke überlappen auf der Länge 0,5, also $\int=0{,}5$, beide Energien 1: $p=0{,}5$. (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0{,}75$, $E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$: $p=\frac{0{,}75}{\sqrt{2/3}}=0{,}919$. Sehr ähnliche Formen. (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$: $p=0$, die Signale sind orthogonal, obwohl sie auf der rechten Hälfte gleich sind.
:::
:::
