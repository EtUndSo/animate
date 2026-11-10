---
title: Stufe 11: Die z-Transformation
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3241200
summary: Wie die Laplace-Transformation die Fourier-Transformation erweitert (Kapitel 2), so erweitert die z-Transformation die Fourier-Transformation zeitdiskreter Signale: erst exponentiell gewichten, dann transformieren.
tags: Einheitskreis
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Wie die Laplace-Transformation die Fourier-Transformation erweitert ([Kapitel 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)), so erweitert die z-Transformation die Fourier-Transformation zeitdiskreter Signale: erst exponentiell gewichten, dann transformieren.
:::

**Die Idee.** Man multipliziert die Folge mit $\rho^{-n}$ ($\rho>0$) und transformiert: $\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$. Mit $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$ wird daraus eine Potenzreihe in $z^{-1}$. Gleichwertig: $z^n$ ist eine Eigenfunktion jedes LSI-Systems, denn $z^{n-k}=z^{-k}z^n$, und der Eigenwert ist $H(z)$:

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n.$$

:::satz Satz 11.1 (z-Transformation)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z, \tag{11.1}$$

wobei das Kurvenintegral einen Kreis $|z|=\rho$ im Konvergenzbereich gegen den Uhrzeigersinn umläuft.
:::

⁠**So liest man das:** Auf dem Kreis $|z|=\rho$ steht eine Periode des Spektrums der gewichteten Folge $s(n)\rho^{-n}$. Auf dem __Einheitskreis__ $|z|=1$ ist $S(z)$ das gewöhnliche Spektrum $S_\mathrm a(f)$, sofern er im Konvergenzbereich liegt. Die Ebene der Laplace-Transformation wird so auf die z-Ebene abgebildet: Die imaginäre Achse wird zum Einheitskreis, die linke Halbebene zu seinem Inneren.

**Grundpaare und Konvergenzbereich.** Mit der geometrischen Reihe:

<span class="anker" id="gl-11-2"></span>
$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|. \tag{11.2}$$

Wie bei Laplace gehört derselbe Ausdruck zu zwei Signalen, erst der Konvergenzbereich entscheidet. Bei rechtsseitigen Folgen liegt er außerhalb des Kreises durch den äußersten Pol, bei linksseitigen innerhalb des Kreises durch den innersten Pol, bei zweiseitigen ist er ein Ring. Für $b^{|n|}$ mit $0<b<1$ ist das der Ring $b<|z|<1/b$.

**Rechenregeln.** Faltung wird Produkt: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. Verzögerung um $n_0$ Takte wird Multiplikation mit $z^{-n_0}$. Damit wird aus der Differenzengleichung [(5.2)](zeitdiskrete-signale-und-die-diskrete-faltung.html#gl-5-2)

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

Für das System aus Aufgabe [6](ein-rekursives-system.html#aufg-6) ist $H(z)=\frac{1+0{,}5z^{-1}}{1-0{,}6z^{-1}}$: Nullstelle bei $z=-0{,}5$, Pol bei $z=0{,}6$.

:::satz Satz 11.2 (Stabilität)
<span class="anker" id="satz-11-2"></span>

Ein kausales LSI-System ist genau dann stabil, wenn alle Pole von $H(z)$ im Inneren des Einheitskreises liegen.
:::

⁠**Warum:** Kausal heißt Konvergenzbereich außerhalb des äußersten Pols. Stabil heißt $\sum|h(n)|<\infty$, dann konvergiert $H(z)$ auf dem Einheitskreis, er gehört also zum Konvergenzbereich. Beides zusammen geht nur, wenn der äußerste Pol innerhalb des Einheitskreises liegt. Für das rekursive System mit $H(z)=\frac{1}{1-bz^{-1}}$ heißt das wieder $|b|<1$.

::::beispiel
$s(n)=0{,}5^n\cos(\pi n/3)\,\varepsilon(n)$. Mit $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$ und [(11.2)](#gl-11-2) für $b=0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$:

$$S(z)=\frac12\Bigl[\frac{1}{1-0{,}5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0{,}5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0{,}25z^{-1}}{1-0{,}5z^{-1}+0{,}25z^{-2}},\qquad|z|>0{,}5.$$

Pole bei $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0{,}25\pm0{,}433\mathrm{j}$, Nullstellen bei $z=0$ und $z=0{,}25$ (Abb. [8](#abb-8)). Der Betrag der Pole gibt das Abklingen je Takt an (0,5), ihr Winkel die Schwingung ($\pi/3$ je Takt, also sechs Takte je Periode).

:::abbildung et3/k4zebene 8
z-Ebene des Beispiels: Pole (Kreuze) bei $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$, Nullstellen (Kreise) bei 0 und 0,25. Der Konvergenzbereich (blau) liegt außerhalb des Kreises durch die Pole und enthält den Einheitskreis. Als Impulsantwort gelesen, beschreibt die Folge ein kausales und stabiles System.
:::
::::

:::aufgabe Aufgabe 11 ★★ z-Transformation anwenden
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Bestätige den Zähler und Nenner von $S(z)$ im Beispiel, indem du die beiden Brüche auf den Hauptnenner bringst.

</li>

<li>

Existiert das Spektrum $S_\mathrm a(f)$ des Beispielsignals? Begründe mit dem Konvergenzbereich.

</li>

</ol>

:::loesung
(a) Hauptnenner $(1-az^{-1})(1-a^*z^{-1})=1-(a+a^*)z^{-1}+|a|^2z^{-2}$ mit $a=0{,}5\mathrm{e}^{\mathrm{j}\pi/3}$: $a+a^*=2\cdot0{,}25=0{,}5$, $|a|^2=0{,}25$. Zähler $\frac12[2-(a+a^*)z^{-1}]=1-0{,}25z^{-1}$.

(b) Ja. Der Konvergenzbereich $|z|>0{,}5$ enthält den Einheitskreis.
:::
:::

:::aufgabe Aufgabe 12 ★★ Kausal oder stabil
<span class="anker" id="aufg-12"></span>

$H(z)=\dfrac{1}{1-2z^{-1}}$.

<ol class="al">

<li>

Welche Impulsantwort gehört zum Konvergenzbereich $|z|>2$, welche zu $|z|<2$?

</li>

<li>

Welche der beiden ist stabil, welche kausal? Gibt es eine, die beides ist?

</li>

</ol>

:::loesung
(a) $|z|>2$: $h(n)=2^n\varepsilon(n)$. $|z|<2$: $h(n)=-2^n\varepsilon(-n-1)$, also $-\frac12,-\frac14,\dots$ für $n=-1,-2,\dots$

(b) Die erste ist kausal, aber instabil (wächst). Die zweite ist stabil ($\sum_{n\le-1}2^n=1$), aber antikausal. Beides zugleich geht nicht: Der Pol bei $z=2$ liegt außerhalb des Einheitskreises, und dann kann der Konvergenzbereich nicht zugleich außerhalb des Pols liegen und den Einheitskreis enthalten.
:::
:::
