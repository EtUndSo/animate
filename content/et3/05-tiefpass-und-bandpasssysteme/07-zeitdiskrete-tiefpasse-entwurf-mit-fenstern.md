---
title: Stufe 6: Zeitdiskrete Tiefpässe, Entwurf mit Fenstern
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250700
summary: Wie entwirft man einen digitalen Tiefpass?
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Wie entwirft man einen digitalen Tiefpass? Genau wie den kausalen analogen: idealen Tiefpass nehmen, verzögern, mit einem Fenster abschneiden.
:::

Der ideale zeitdiskrete Tiefpass hat den periodisch wiederholten Rechteck-Frequenzgang und die Impulsantwort

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

im Rechenmodell ($f_\mathrm g=0{,}2$) also $h(0)=0{,}4$, $h(\pm1)=0{,}303$, $h(\pm2)=0{,}094$, $h(\pm3)=-0{,}062$. Auch er ist nicht kausal. Man multipliziert ihn mit einem Fenster $w(n)$ von $2N+1$ Werten, verschiebt um $N$ und erhält ein FIR-Filter mit linearer Phase. Das Fenster bestimmt das Ergebnis (Abb. [4](#abb-4)):

<ul>

<li>

⁠**Rechteckfenster:** schärfster Übergang, aber hohe Nebenzipfel. Im Rechenmodell ($N=10$) erreicht der Sperrbereich ab $f=0{,}3$ noch $-26{,}6$ dB, der Durchlass schwankt um etwa $\pm0{,}5$ dB.

</li>

<li>

⁠**Hann-Fenster:** weicherer Übergang, aber viel tiefere Sperrung: ab $f=0{,}3$ höchstens $-45{,}9$ dB, Durchlass auf $0{,}05$ dB glatt.

</li>

</ul>

Der Grund ist derselbe wie bei der Kurzzeit-Fourier-Transformation in [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Das Spektrum des Fensters wird mit dem Ideal gefaltet, und die harten Kanten des Rechtecks erzeugen langsam abklingende Nebenzipfel.

:::abbildung et3/k5fenster 4
Betragsfrequenzgang zweier FIR-Tiefpässe mit $f_\mathrm g=0{,}2$ und 21 Koeffizienten. Rechteckfenster: steile Flanke, ab $f=0{,}3$ Sperrung nur bis $-26{,}6$ dB. Hann-Fenster: flachere Flanke, ab $f=0{,}3$ höchstens $-45{,}9$ dB.
:::

:::aufgabe Aufgabe 6 ★ Halbbandfilter
<span class="anker" id="aufg-6"></span>

Berechne die Koeffizienten $h(0)$ bis $h(3)$ des idealen zeitdiskreten Tiefpasses mit $f_\mathrm g=0{,}25$. Was fällt auf, und warum spart das bei einem FIR-Filter Rechenarbeit?

:::loesung
$h(n)=0{,}5\operatorname{si}(\pi n/2)$: $h(0)=0{,}5$, $h(\pm1)=\frac1\pi=0{,}318$, $h(\pm2)=0$, $h(\pm3)=-\frac{1}{3\pi}=-0{,}106$. Alle geraden Koeffizienten außer $h(0)$ sind null, weil $\sin(\pi n/2)=0$ für gerade $n$. Im FIR-Filter entfallen diese Multiplikationen, fast die Hälfte.
:::
:::
