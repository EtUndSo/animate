---
title: Stufe 10: Quadraturschaltung und Bandpass-Abtastung
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3251100
summary: Wie gewinnt man die Quadraturkomponenten technisch?
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Wie gewinnt man die Quadraturkomponenten technisch? Und wie viele Abtastwerte braucht ein Bandpasssignal?
:::

**Quadraturschaltung.** Multipliziert man ein Bandpasssignal mit $\cos(2\pi f_0t)$ und filtert mit einem Tiefpass, bleibt $\frac12s_{Tr}$. Mit $-\sin(2\pi f_0t)$ bleibt $\frac12s_{Ti}$. Der Grund ist trigonometrisch:

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{bei }2f_0,\text{ vom Tiefpass entfernt}},$$

und ebenso $-s\sin=\frac12s_{Ti}+(\text{Anteile bei }2f_0)$. Voraussetzung ist, dass das Band unterhalb von $2f_0$ endet. Im Tiefpassbereich filtert man dann mit vier Tiefpässen ($h_{Tr}$, $\pm h_{Ti}$) nach [(9.1)](bandpasssignal-durch-bandpasssystem.html#gl-9-1). Am Ausgang moduliert man nach [(8.2)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-2) wieder auf den Träger, oder man bildet die Einhüllende $\sqrt{g_{Tr}^2+g_{Ti}^2}$ (Abb. [6](#abb-6)).

:::abbildung et3/k5quadratur 6
Quadraturdemodulator: Er gewinnt aus einem Bandpasssignal die beiden Quadraturkomponenten, also die komplexe Hüllkurve.
:::

**Abtasttheorem für Bandpasssignale.** Ein Bandpasssignal der Bandbreite $\Delta f$ hat, bezogen auf die Mittenfrequenz, Quadraturkomponenten, die Tiefpasssignale bis $\Delta f/2$ sind. Jede lässt sich mit $1/T=\Delta f$ abtasten:

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

Insgesamt braucht man $2\Delta f$ Werte je Sekunde, so viele wie für ein Tiefpasssignal der Grenzfrequenz $\Delta f$. Es kommt also auf die Bandbreite an, nicht auf die höchste Frequenz.

:::aufgabe Aufgabe 9 ★★ Ein Funksignal abtasten
<span class="anker" id="aufg-9"></span>

Ein Signal belegt das Band von 10,0 bis 10,2 MHz.

<ol class="al">

<li>

Welche Abtastrate bräuchte man nach dem gewöhnlichen Abtasttheorem?

</li>

<li>

Wie viele Abtastwerte je Sekunde genügen mit der Quadraturschaltung insgesamt, und mit welcher Rate wird jeder Zweig abgetastet?

</li>

</ol>

:::loesung
(a) Mindestens $2\cdot10{,}2=20{,}4$ MHz.

(b) $\Delta f=0{,}2$ MHz. Jeder Zweig wird mit 0,2 MHz abgetastet ($T=5$ µ s), zusammen 0,4 MHz, rund fünfzigmal weniger.
:::
:::
