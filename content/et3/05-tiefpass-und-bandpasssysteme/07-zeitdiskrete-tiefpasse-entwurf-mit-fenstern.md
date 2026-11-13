---
title: Stufe 6: Zeitdiskrete Tiefpässe, Entwurf mit Fenstern
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
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

Der Grund ist derselbe wie bei der Kurzzeit-Fourier-Transformation in [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Das Spektrum des Fensters wird mit dem Ideal gefaltet, und die harten Kanten des Rechtecks erzeugen langsam abklingende Nebenzipfel.

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

::::formelsammlung
**Idealer zeitdiskreter Tiefpass**

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn)$$

$f_\mathrm g$ bezogen auf die Abtastrate; Frequenzgang ist das periodisch wiederholte Rechteck. Nicht kausal: Man multipliziert mit einem Fenster $w(n)$ von $2N+1$ Werten und verschiebt um $N$, so entsteht ein FIR-Filter mit linearer Phase. Rechteckfenster: schärfster Übergang, hohe Nebenzipfel; Hann-Fenster: weicherer Übergang, viel tiefere Sperrung.

**Halbbandfilter**

$$h(n)=0{,}5\operatorname{si}(\pi n/2)$$

Der ideale zeitdiskrete Tiefpass mit $f_\mathrm g=0{,}25$: Alle geraden Koeffizienten außer $h(0)$ sind null, im FIR-Filter entfällt fast die Hälfte der Multiplikationen.
::::

::::lernkarten
:::karte formel Idealer zeitdiskreter Tiefpass
Welche Impulsantwort hat der ideale zeitdiskrete Tiefpass mit der auf die Abtastrate bezogenen Grenzfrequenz $f_\mathrm g$?
---
$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn)$; sein Frequenzgang ist das periodisch wiederholte Rechteck. Auch er ist nicht kausal, weil $h(n)$ für negative $n$ nicht verschwindet.
--- falsch
$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn)$ für $n\ge0$ und null sonst; sein Frequenzgang ist ein einzelnes Rechteck. Er ist kausal, weil eine Folge erst bei $n=0$ beginnt.
--- falsch
$h(n)$ ist eine Folge von Einsen für $|n|\le f_\mathrm g$ und null sonst; sein Frequenzgang ist das periodisch wiederholte Rechteck. Er ist nicht kausal, weil die Einsen symmetrisch um $n=0$ liegen.
--- falsch
$h(n)=\delta(n)-2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn)$; sein Frequenzgang ist das periodisch wiederholte Rechteck. Er ist kausal, weil der Einheitsimpuls bei $n=0$ den Anfang festlegt.
:::
:::karte zusammenhang Entwurf mit Fenstern
Wie entwirft man aus dem idealen zeitdiskreten Tiefpass ein kausales FIR-Filter mit linearer Phase?
---
Man multipliziert $h(n)$ mit einem Fenster $w(n)$ von $2N+1$ Werten und verschiebt das Ergebnis um $N$. So entsteht ein FIR-Filter mit linearer Phase, genau wie beim kausalen analogen Tiefpass.
--- falsch
Man schneidet alle Werte mit $n<0$ ab und behält den Rest unverändert. So entsteht ein FIR-Filter mit linearer Phase, weil die übrigen Koeffizienten weiterhin symmetrisch zueinander liegen.
--- falsch
Man faltet $h(n)$ mit einem Fenster $w(n)$ von $2N+1$ Werten und verschiebt um $N$. So entsteht ein IIR-Filter mit linearer Phase, weil die Faltung die Impulsantwort unendlich verlängert.
--- falsch
Man multipliziert $h(n)$ mit einem Fenster $w(n)$ von $2N+1$ Werten, verschiebt aber nicht. So entsteht schon ein kausales FIR-Filter, weil das Fenster alle Werte außerhalb von $|n|\le N$ entfernt.
:::
:::karte zusammenhang Rechteckfenster und Hann-Fenster
Worin unterscheiden sich FIR-Tiefpässe, die mit dem Rechteckfenster bzw. mit dem Hann-Fenster entworfen sind?
---
Das Rechteckfenster gibt den schärfsten Übergang, aber hohe Nebenzipfel und damit eine schwache Sperrung. Das Hann-Fenster gibt einen weicheren Übergang, dafür eine viel tiefere Sperrung und einen glatteren Durchlass.
--- falsch
Das Rechteckfenster gibt den weichsten Übergang und die tiefste Sperrung, weil es alle Koeffizienten unverändert lässt; das Hann-Fenster gibt eine steilere Flanke, aber höhere Nebenzipfel im Sperrbereich.
--- falsch
Beide Fenster ergeben bei gleicher Länge denselben Betragsfrequenzgang, weil die Grenzfrequenz allein von $h(n)$ bestimmt wird; sie unterscheiden sich nur in der Verzögerung um $N$ Takte, die beim Hann-Fenster größer ist.
--- falsch
Das Rechteckfenster gibt die tiefere Sperrung, weil es mehr Koeffizienten voll gewichtet; das Hann-Fenster gibt einen schärferen Übergang, dafür schwankt sein Durchlass um etwa $\pm0{,}5$ dB.
:::
:::karte zusammenhang Nebenzipfel durch das Fenster
Warum erzeugt das Rechteckfenster beim Entwurf eines FIR-Tiefpasses so hohe Nebenzipfel im Sperrbereich?
---
Das Spektrum des Fensters wird mit dem idealen Frequenzgang gefaltet. Die harten Kanten des Rechtecks erzeugen langsam abklingende Nebenzipfel, die sich in den Sperrbereich übertragen, wie bei der Kurzzeit-Fourier-Transformation.
--- falsch
Das Spektrum des Fensters wird mit dem idealen Frequenzgang multipliziert. Weil das Rechteck auch im Spektrum ein Rechteck ist, bleibt der Sperrbereich offen, sobald das Fenster kürzer als die gesamte Impulsantwort ist.
--- falsch
Weil das Rechteckfenster die Koeffizienten am Rand zu stark abschwächt: Dadurch fehlen die hohen Frequenzen, die den Sperrbereich auslöschen würden, und die Nebenzipfel bleiben dort stehen.
--- falsch
Weil die Abtastung die Kanten des idealen Frequenzgangs periodisch wiederholt: Die Nebenzipfel sind die Spiegelspektren der Kante und hängen deshalb nicht vom gewählten Fenster ab.
:::
:::karte zusammenhang Halbbandfilter
Was fällt an den Koeffizienten des idealen zeitdiskreten Tiefpasses mit $f_\mathrm g=0{,}25$ auf, und warum spart das bei einem FIR-Filter Rechenarbeit?
---
Mit $h(n)=0{,}5\operatorname{si}(\pi n/2)$ sind alle geraden Koeffizienten außer $h(0)$ null, weil $\sin(\pi n/2)=0$ für gerade $n$ ist. Im FIR-Filter entfallen diese Multiplikationen, fast die Hälfte.
--- falsch
Mit $h(n)=0{,}5\operatorname{si}(\pi n/2)$ sind alle ungeraden Koeffizienten null, weil der Sinus bei ungeraden Vielfachen von $\pi/2$ verschwindet. Im FIR-Filter entfällt so jede zweite Multiplikation.
--- falsch
Alle Koeffizienten sind gleich groß, nämlich 0,5, weil die Grenzfrequenz genau ein Viertel der Abtastrate ist. Das Filter wird damit zum gleitenden Mittelwert und braucht nur eine Multiplikation.
--- falsch
Die Koeffizienten wechseln von Wert zu Wert ihr Vorzeichen, weil $f_\mathrm g=0{,}25$ genau in der Mitte des Bandes liegt. Man spart Rechenarbeit, weil man nur die Beträge speichern muss.
:::
::::
