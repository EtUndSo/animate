---
title: Stufe 2: Der ideale Tiefpass
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250300
summary: Der ideale Tiefpass lässt alle Frequenzen bis f mathrm g unverändert durch und sperrt alle darüber.
tags: Signaldauer
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Der ideale Tiefpass lässt alle Frequenzen bis $f_\mathrm g$ unverändert durch und sperrt alle darüber. Diese Stufe zeigt, was dieses scharfe Abschneiden im Zeitbereich bedeutet.
:::

:::satz Satz 2.1 (Idealer Tiefpass)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**So liest man das:** Die Impulsantwort reicht in beide Richtungen ins Unendliche. Der ideale Tiefpass ist also *nicht kausal*: Er müsste auf einen Stoß schon antworten, bevor er kommt. Er ist ein mathematisches Grenzobjekt, das man nur annähern kann (Stufen [4](kausale-naherung.html#stufe-4), [6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6)).

**Dauer und Bandbreite.** Als __Signaldauer__ $t_m$ einer Impulsantwort nimmt man die Breite eines Rechtecks mit derselben Höhe $h_{\max}$ und derselben Fläche:

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

Beim idealen Tiefpass ist $H(0)=1$ und $h_{\max}=2f_\mathrm g$, also $t_m=\frac{1}{2f_\mathrm g}$ und $f_\mathrm g\cdot t_m=\frac12$. Allgemein gilt für Tiefpässe $f_\mathrm g\cdot t_m=\text{konst.}$: Doppelte Bandbreite heißt halbe Antwortdauer. Das ist der Ähnlichkeitssatz aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).

**Überschwingen.** Das Verhältnis des betragsgrößten Nebenmaximums $a_1$ zum Hauptmaximum $a_0$ ist bei der si-Funktion

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21{,}7\,\%,$$

unabhängig von $f_\mathrm g$ (das erste Nebenminimum von $\operatorname{si}(\pi u)$ liegt bei $u=1{,}43$ mit $-0{,}217$). Eine Änderung von $f_\mathrm g$ staucht die Kurve nur, sie ändert nicht ihre Form.

:::aufgabe Aufgabe 2 ★ Idealer Tiefpass für Sprache
<span class="anker" id="aufg-2"></span>

Ein idealer Tiefpass mit $f_\mathrm g=4$ kHz. Wie groß sind die Signaldauer der Impulsantwort und das Überschwingen? Was ändert sich bei $f_\mathrm g=8$ kHz?

:::loesung
$t_m=\frac{1}{2f_\mathrm g}=125$ µ s, Überschwingen 21,7 %. Bei 8 kHz halbiert sich die Signaldauer auf 62,5 µ s. Das Überschwingen bleibt 21,7 %, weil die Impulsantwort nur gestaucht wird.
:::
:::
