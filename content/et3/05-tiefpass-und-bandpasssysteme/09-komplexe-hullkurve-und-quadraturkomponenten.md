---
title: Stufe 8: Komplexe Hüllkurve und Quadraturkomponenten
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3250900
summary: Was für Systeme gilt, gilt auch für Signale: Ein Bandpasssignal ist ein Tiefpasssignal auf einem Träger.
tags: komplexe Hüllkurve, komplexer Träger, Quadraturkomponenten, Einhüllende
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Was für Systeme gilt, gilt auch für Signale: Ein Bandpasssignal ist ein Tiefpasssignal auf einem Träger. Diese Stufe zeigt die verschiedenen Arten, das hinzuschreiben.
:::

Die Rücktransformation von [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) ergibt mit der Modulationsregel $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$, also wegen $z+z^*=2\operatorname{Re} z$:

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ heißt __komplexe Hüllkurve__, $\mathrm{e}^{\mathrm{j}2\pi f_0t}$ __komplexer Träger__. Ihr halbes Produkt ist die analytische Komponente aus [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$, also $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

:::satz Satz 8.1 (Quadraturdarstellung)
<span class="anker" id="satz-8-1"></span>

Mit $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ und der Hilbert-Transformierten $\hat s=s*\frac{1}{\pi t}$:

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**So liest man das:** $s_{Tr}$ und $s_{Ti}$ heißen __Quadraturkomponenten__: Die eine moduliert den Kosinus, die andere den Sinus des Trägers. $|s_T|$ ist die __Einhüllende__, die man auf einem Oszilloskop als „Umriss“ des Signals sieht, und $\varphi_T$ die Phasenabweichung des Trägers. Ist die Hüllkurve reell (symmetrischer Fall), ist $s(t)=s_T(t)\cos(2\pi f_0t)$: ein amplitudenmodulierter Kosinus.

:::herleitung Quadraturkomponenten
[(8.2)](#gl-8-2): $\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$. Für [(8.3)](#gl-8-3): $2s_+=s+\mathrm{j}\hat s$ ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), also

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe Aufgabe 8 ★★ Komplexe Hüllkurven bestimmen
<span class="anker" id="aufg-8"></span>

Bestimme $s_T$, $s_{Tr}$, $s_{Ti}$ und $|s_T|$ bezüglich $f_0=10$ Hz für (a) $s(t)=\bigl[1+0{,}5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$, (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0{,}3)$, (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$. Prüfe (c) mit [(8.2)](#gl-8-2).

:::loesung
(a) $s_T=1+0{,}5\cos(2\pi t)$, reell: $s_{Tr}=s_T$, $s_{Ti}=0$, $|s_T|=1+0{,}5\cos(2\pi t)$ zwischen 0,5 und 1,5. Ein amplitudenmodulierter Kosinus.

(b) $s_T=\mathrm{e}^{\mathrm{j}0{,}3}$: $s_{Tr}=\cos0{,}3=0{,}955$, $s_{Ti}=\sin0{,}3=0{,}296$, $|s_T|=1$. Die Hüllkurve ist konstant, nur die Phase ist um 0,3 verschoben.

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$, also $s_T=-\mathrm{j}$: $s_{Tr}=0$, $s_{Ti}=-1$, $|s_T|=1$. Probe: $0\cdot\cos-(-1)\sin=\sin$.
:::
:::

::::formelsammlung
**Komplexe Hüllkurve**

$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$$

$s_T(t)$ komplexe Hüllkurve, $\mathrm{e}^{\mathrm{j}2\pi f_0t}$ komplexer Träger. Folgt aus dem äquivalenten Tiefpass mit der Modulationsregel und $z+z^*=2\operatorname{Re} z$.

**Hüllkurve und analytische Komponente**

$$s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t},\qquad s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$$

Das halbe Produkt aus komplexer Hüllkurve und komplexem Träger ist die analytische Komponente.

**Analytische Komponente und Hilbert-Transformierte**

$$2s_+=s+\mathrm{j}\hat s,\qquad\hat s=s*\frac{1}{\pi t}$$

$\hat s$ Hilbert-Transformierte von $s$.

**Quadraturdarstellung**

$$s(t)=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t)$$

Mit $s_T=s_{Tr}+\mathrm{j} s_{Ti}$. Die Quadraturkomponenten $s_{Tr}$ und $s_{Ti}$ modulieren Kosinus und Sinus des Trägers.

**Quadraturkomponenten**

$$s_{Tr}(t)=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t)$$

Real- und Imaginärteil von $s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)$.

**Einhüllende und Phasenabweichung**

$$s(t)=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}$$

$|s_T|$ Einhüllende, der „Umriss“ des Signals auf dem Oszilloskop; $\varphi_T$ Phasenabweichung des Trägers.

**Reelle Hüllkurve**

$$s(t)=s_T(t)\cos(2\pi f_0t)$$

Symmetrischer Fall, $s_{Ti}=0$: ein amplitudenmodulierter Kosinus.
::::

::::lernkarten
:::karte begriff komplexe Hüllkurve
Was ist die komplexe Hüllkurve $s_T(t)$ eines Bandpasssignals $s(t)$ bezüglich der Trägerfrequenz $f_0$?
---
Das Tiefpasssignal $s_T(t)$, aus dem das Bandpasssignal durch $s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$ entsteht. Es ist für Signale das Gegenstück zum äquivalenten Tiefpass und darf komplex sein.
--- falsch
Der Betrag $|s(t)|$ des Bandpasssignals, also der Umriss, den man auf einem Oszilloskop sieht. Er ist immer reell und positiv und enthält keine Information über die Phase des Trägers.
--- falsch
Das Signal $s(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}$, also das Bandpasssignal, mit dem komplexen Träger multipliziert. Es liegt bei der doppelten Trägerfrequenz und ist deshalb selbst wieder ein Bandpasssignal.
--- falsch
Das Tiefpasssignal $s_T(t)$, aus dem das Bandpasssignal durch $s(t)=s_T(t)+\cos(2\pi f_0t)$ entsteht. Der Träger wird also zur Hüllkurve addiert und nicht mit ihr multipliziert.
:::
:::karte begriff komplexer Träger
Was bezeichnet man in der Darstellung $s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$ als komplexen Träger, und wie hängt er mit der analytischen Komponente zusammen?
---
Der komplexe Träger ist der Faktor $\mathrm{e}^{\mathrm{j}2\pi f_0t}$. Das halbe Produkt aus komplexer Hüllkurve und komplexem Träger ist die analytische Komponente: $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$, also $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.
--- falsch
Der komplexe Träger ist der Faktor $\mathrm{e}^{\mathrm{j}2\pi f_0t}$. Das Produkt aus komplexer Hüllkurve und komplexem Träger ist schon das Bandpasssignal selbst, $s(t)=s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$, ganz ohne Realteil; die analytische Komponente braucht man dafür nicht.
--- falsch
Der komplexe Träger ist der Realteil $\cos(2\pi f_0t)$ des Faktors $\mathrm{e}^{\mathrm{j}2\pi f_0t}$. Die analytische Komponente ist die Hilbert-Transformierte dieses Kosinus, also der Sinus $\sin(2\pi f_0t)$ des Trägers.
--- falsch
Der komplexe Träger ist die komplexe Hüllkurve selbst, wenn ihr Spektrum bei $f_0$ liegt. Die analytische Komponente ist dann das Doppelte davon, $s_+(t)=2s_T(t)$, ganz ohne einen eigenen Trägerfaktor.
:::
:::karte formel Quadraturdarstellung
Wie schreibt man ein Bandpasssignal mit Real- und Imaginärteil seiner komplexen Hüllkurve $s_T=s_{Tr}+\mathrm{j} s_{Ti}$?
---
$s(t)=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t)$: Der Realteil der Hüllkurve moduliert den Kosinus, der Imaginärteil mit negativem Vorzeichen den Sinus des Trägers.
--- falsch
$s(t)=s_{Tr}(t)\cos(2\pi f_0t)+s_{Ti}(t)\sin(2\pi f_0t)$: Realteil und Imaginärteil der Hüllkurve modulieren Kosinus und Sinus mit gleichem Vorzeichen, weil der Realteil eines Produkts eine Summe ist.
--- falsch
$s(t)=s_{Tr}(t)\cos(2\pi f_0t)$: Nur der Realteil der Hüllkurve geht in das Signal ein; der Imaginärteil fällt bei der Bildung des Realteils vollständig weg, ganz gleich, wie groß er ist.
--- falsch
$s(t)=\sqrt{s_{Tr}^2+s_{Ti}^2}\,\sin(2\pi f_0t)$: Beide Komponenten werden zum Betrag zusammengefasst, der dann den Sinus des Trägers moduliert; die Phase geht dabei verloren.
:::
:::karte begriff Quadraturkomponenten
Was sind die Quadraturkomponenten eines Bandpasssignals, und wie berechnet man sie aus $s$ und seiner Hilbert-Transformierten $\hat s$?
---
Real- und Imaginärteil der komplexen Hüllkurve; der eine moduliert den Kosinus, der andere den Sinus des Trägers. Es gilt $s_{Tr}(t)=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t)$ und $s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t)$.
--- falsch
Betrag und Phase der komplexen Hüllkurve; der Betrag moduliert die Amplitude, die Phase den Nulldurchgang des Trägers. Man berechnet den Betrag als Summe $s+\hat s$ und die Phase als Quotient aus $\hat s$ und $s$, ganz ohne Kosinus und Sinus des Trägers.
--- falsch
Real- und Imaginärteil der komplexen Hüllkurve, berechnet als $s_{Tr}(t)=s(t)\cos(2\pi f_0t)$ und $s_{Ti}(t)=\hat s(t)\sin(2\pi f_0t)$; jede der beiden Komponenten braucht also nur eines der beiden Signale $s$ und $\hat s$.
--- falsch
Die beiden Seitenbänder des Bandpasssignals oberhalb und unterhalb von $f_0$: Das obere ist $s_{Tr}$, das untere $s_{Ti}$. Man gewinnt sie aus $s$ und $\hat s$ als Summe $s+\hat s$ und Differenz $s-\hat s$, jeweils mit dem Faktor $\frac12$.
:::
:::karte begriff Einhüllende
Was ist die Einhüllende eines Bandpasssignals, und wie berechnet man sie aus den Quadraturkomponenten?
---
Die Einhüllende ist der Betrag $|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}$ der komplexen Hüllkurve, der „Umriss“ des Signals auf dem Oszilloskop. Mit der Phasenabweichung $\varphi_T$ gilt $s(t)=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr)$.
--- falsch
Die Einhüllende ist der Realteil $s_{Tr}$ der komplexen Hüllkurve, also der Anteil, der den Kosinus des Trägers moduliert. Mit ihr gilt $s(t)=s_{Tr}(t)\cos(2\pi f_0t)$ für jedes beliebige Bandpasssignal.
--- falsch
Die Einhüllende ist die Summe $s_{Tr}+s_{Ti}$ der beiden Quadraturkomponenten, also der Umriss des Signals auf dem Oszilloskop. Sie wird negativ, sobald eine der beiden Komponenten stärker negativ ist als die andere positiv.
--- falsch
Die Einhüllende ist der Betrag $|s(t)|$ des Bandpasssignals selbst, gebildet Punkt für Punkt. Sie folgt jeder einzelnen Schwingung des Trägers und hat deshalb dieselbe Frequenz $f_0$ wie das Signal.
:::
:::karte zusammenhang Reelle Hüllkurve
Was folgt für ein Bandpasssignal, wenn seine komplexe Hüllkurve reell ist?
---
Dann ist $s_{Ti}=0$ und $s(t)=s_T(t)\cos(2\pi f_0t)$: Das Signal ist ein amplitudenmodulierter Kosinus. Die Hüllkurve verändert nur die Amplitude des Kosinus.
--- falsch
Dann ist $s_{Tr}=0$, und das Signal ist ein amplitudenmodulierter Sinus: Der Realteil der Hüllkurve moduliert immer den Sinus des Trägers, nicht den Kosinus.
--- falsch
Dann ist das Bandpasssignal ein reiner Kosinus mit konstanter Amplitude: Eine reelle Hüllkurve enthält keine Information, weil diese nur im Imaginärteil steckt.
--- falsch
Dann ist $s(t)=s_T(t)$: Bei reeller Hüllkurve braucht man keinen Träger mehr, weil das Bandpasssignal selbst schon ein Tiefpasssignal ist.
:::
:::karte zusammenhang Hüllkurve eines Sinus
Welche komplexe Hüllkurve hat das Signal $s(t)=\sin(2\pi f_0t)$ bezüglich $f_0$, und warum?
---
$s_T=-\mathrm{j}$, also $s_{Tr}=0$, $s_{Ti}=-1$ und $|s_T|=1$, weil $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$ ist: Die Hüllkurve ist konstant und rein imaginär. Probe mit der Quadraturdarstellung: $0\cdot\cos-(-1)\sin=\sin$.
--- falsch
$s_T=\mathrm{j}$, also $s_{Tr}=0$ und $s_{Ti}=1$, weil der Sinus der Imaginärteil von $\mathrm{e}^{\mathrm{j} x}$ ist und der Imaginärteil der Hüllkurve den Sinus mit positivem Vorzeichen moduliert.
--- falsch
$s_T=1$, also $s_{Tr}=1$ und $s_{Ti}=0$, weil ein Sinus nur ein verschobener Kosinus ist und eine Verschiebung des Trägers die komplexe Hüllkurve nicht ändert.
--- falsch
$s_T=\sin(2\pi f_0t)$ selbst, weil ein Signal ohne Modulation seine eigene Hüllkurve ist; die Quadraturkomponenten sind dann beide halb so groß wie das Signal.
:::
:::karte herleitung Komplexe Hüllkurve aus dem äquivalenten Tiefpass
Wie folgt aus $H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0)$ die Darstellung $h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$?
---
Man transformiert beide Summanden zurück, weil die Modulationsregel eine Verschiebung im Spektrum in eine Multiplikation mit dem komplexen Träger übersetzt.
---
Der zweite Summand ist das Konjugierte des ersten, weil er aus dem gespiegelten und konjugierten Band entsteht; so ergibt sich $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$.
---
Mit $z+z^*=2\operatorname{Re} z$ wird daraus $h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$, weil sich die Faktoren $\frac12$ und 2 aufheben.
---
Für Signale gilt dasselbe, $s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$, weil man ein Bandpasssignal genauso zerlegt wie die Impulsantwort eines Bandpasses.
:::
:::karte herleitung Quadraturkomponenten aus der Hilbert-Transformierten
Wie folgen aus $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$ und $2s_+=s+\mathrm{j}\hat s$ die Formeln für $s_{Tr}$ und $s_{Ti}$?
---
Man setzt $2s_+=s+\mathrm{j}\hat s$ ein, weil die analytische Komponente so aus dem Signal und seiner Hilbert-Transformierten gebildet wird.
---
Man zerlegt den Faktor $\mathrm{e}^{-\mathrm{j}2\pi f_0t}$ nach Euler in Kosinus minus $\mathrm{j}$ mal Sinus (Argument $2\pi f_0t$), weil man Real- und Imaginärteil trennen will; damit ist $s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)$.
---
Ausmultiplizieren gibt $(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin)$, weil das Produkt der beiden imaginären Anteile reell wird und man reelle und imaginäre Produkte sammelt.
---
Der Realteil ist $s_{Tr}$, der Imaginärteil $s_{Ti}$, weil $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ so definiert ist.
:::
::::
