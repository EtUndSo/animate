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

::::formelsammlung
**Gewichten und transformieren**

$$z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$$

Folge mit $\rho^{-n}$ ($\rho>0$) gewichten und transformieren: $\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$ wird eine Potenzreihe in $z^{-1}$.

**Eigenfunktion jedes LSI-Systems**

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n$$

Weil $z^{n-k}=z^{-k}z^n$; der Eigenwert ist $H(z)$.

**z-Transformation**

$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z$$

Das Kurvenintegral umläuft einen Kreis $|z|=\rho$ im Konvergenzbereich gegen den Uhrzeigersinn. Auf dem Einheitskreis $|z|=1$ ist $S(z)$ das Spektrum $S_\mathrm a(f)$, sofern er im Konvergenzbereich liegt.

**Grundpaare**

$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|$$

Derselbe Ausdruck gehört zu zwei Signalen, erst der Konvergenzbereich entscheidet. Rechtsseitig: außerhalb des Kreises durch den äußersten Pol; linksseitig: innerhalb des Kreises durch den innersten Pol; zweiseitig: ein Ring, für $b^{|n|}$ mit $0<b<1$ der Ring $b<|z|<1/b$.

**Faltung und Verzögerung**

$$g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$$

Eine Verzögerung um $n_0$ Takte wird eine Multiplikation mit $z^{-n_0}$.

**Übertragungsfunktion aus der Differenzengleichung**

$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}$$

Zähler aus dem FIR-Teil, Nenner aus der Rückkopplung.

**Stabilität kausaler LSI-Systeme**

$$\sum|h(n)|<\infty$$

Ein kausales LSI-System ist genau dann stabil, wenn alle Pole von $H(z)$ im Inneren des Einheitskreises liegen: Kausal heißt Konvergenzbereich außerhalb des äußersten Pols, stabil heißt Einheitskreis im Konvergenzbereich.
::::

::::lernkarten
:::karte zusammenhang Idee der z-Transformation
Wie entsteht die z-Transformation aus der Fourier-Transformation zeitdiskreter Signale, und welche Rolle spielt dabei $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$?
---
Man gewichtet die Folge erst mit $\rho^{-n}$ ($\rho>0$) und transformiert dann: $\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$. Mit $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$ wird daraus eine Potenzreihe in $z^{-1}$, so wie die Laplace-Transformation die Fourier-Transformation erweitert.
--- falsch
Man ersetzt die Frequenz $f$ durch die komplexe Zahl $z$ und lässt die Folge ungewichtet. Mit $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$ wird die Summe dann zu einem Integral über die z-Ebene, so wie bei der Laplace-Transformation, die ebenfalls ohne Gewichtung auskommt.
--- falsch
Man gewichtet die Folge mit $\rho^{n}$ und transformiert, damit wachsende Folgen noch stärker wachsen. Mit $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$ wird daraus eine Potenzreihe in $z$, deren Koeffizienten die Spektralwerte der Folge sind.
--- falsch
Man tastet das Spektrum $S_\mathrm a(f)$ an den Stellen $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$ ab. Die z-Transformation ist also eine DFT mit komplexen Frequenzen, die nur endlich viele Werte liefert und deshalb im Rechner leicht auszuwerten ist.
:::
:::karte formel Eigenfunktion jedes LSI-Systems
Warum ist $z^n$ eine Eigenfunktion jedes LSI-Systems, und was ist der Eigenwert?
---
Weil $z^{n-k}=z^{-k}z^n$ ist: $z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n$. Der Eigenwert ist $H(z)$, die z-Transformierte der Impulsantwort.
--- falsch
Weil die Faltung mit $z^n$ jede Impulsantwort in $z^n$ verwandelt: $z^n*h(n)=z^n$ für jedes $h$. Der Eigenwert ist deshalb stets 1, unabhängig vom System und von $z$.
--- falsch
Weil $z^{n-k}=z^n-z^k$ ist: $z^n*h(n)=z^n\sum_kh(k)-\sum_kh(k)z^k$. Der Eigenwert ist die Summe $\sum_kh(k)$ der Impulsantwort, der zweite Term verschwindet bei kausalen Systemen.
--- falsch
Weil $z^{n-k}=z^{-k}z^n$ ist: $z^n*h(n)=H(z)\,z^n$. Der Eigenwert ist aber der Wert $h(n)$ der Impulsantwort zum selben Zeitpunkt, weil die Faltung Takt für Takt wirkt.
:::
:::karte formel z-Transformation
Wie lauten die z-Transformation einer Folge $s(n)$ und ihre Rücktransformation?
---
$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n}$ und $s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z$, wobei das Kurvenintegral einen Kreis $|z|=\rho$ im Konvergenzbereich gegen den Uhrzeigersinn umläuft.
--- falsch
$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n}$ und $s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{-n}\,\mathrm{d} z$, wobei das Kurvenintegral stets den Einheitskreis umläuft, unabhängig davon, wo der Konvergenzbereich liegt.
--- falsch
$S(z)=\sum_{n=0}^{\infty}s(n)\,z^{-n}$ und $s(n)=\int_{-1/2}^{1/2}S(z)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f$, wobei man über eine Periode des Spektrums integriert; linksseitige Folgen haben keine z-Transformierte.
--- falsch
$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n}$ und $s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z$, wobei das Kurvenintegral einen Kreis außerhalb des Konvergenzbereichs umläuft, damit es die Pole einschließt.
:::
:::karte begriff Einheitskreis
Was ist der Einheitskreis in der z-Ebene, und welche Bedeutung hat $S(z)$ auf ihm?
---
Der Kreis $|z|=1$, auf dem die Gewichtung $\rho^{-n}$ entfällt. Dort ist $S(z)$ das gewöhnliche Spektrum $S_\mathrm a(f)$, sofern er im Konvergenzbereich liegt; er ist das Bild der imaginären Achse der Laplace-Ebene.
--- falsch
Der Kreis $|z|=1$, auf dem alle Pole eines Systems liegen. Dort ist $S(z)$ unendlich groß, deshalb gehört er nie zum Konvergenzbereich; er ist das Bild der linken Halbebene der Laplace-Ebene.
--- falsch
Der Kreis $|z|=2\pi$, auf dem eine volle Umdrehung der Frequenz entspricht. Dort ist $S(z)$ das Spektrum $S_\mathrm a(f)$, und zwar unabhängig vom Konvergenzbereich, weil er genau eine Periode enthält.
--- falsch
Der Kreis $|z|=1$, auf dem die Gewichtung $\rho^{-n}$ entfällt. Dort ist $S(z)$ die Impulsantwort $h(n)$ der Folge, sofern er im Konvergenzbereich liegt; er ist das Bild der reellen Achse der Laplace-Ebene.
:::
:::karte zusammenhang Laplace-Ebene und z-Ebene
Worauf werden die imaginäre Achse und die linke Halbebene der Laplace-Ebene in der z-Ebene abgebildet?
---
Die imaginäre Achse wird zum Einheitskreis $|z|=1$, die linke Halbebene zu seinem Inneren. Der Einheitskreis übernimmt damit die Rolle der imaginären Achse: Auf ihm steht das Spektrum.
--- falsch
Die imaginäre Achse wird zur reellen Achse der z-Ebene, die linke Halbebene zur linken Halbebene. Die z-Ebene ist nur eine gedrehte Laplace-Ebene, ihre Bereiche entsprechen einander unmittelbar.
--- falsch
Die imaginäre Achse wird zum Einheitskreis, die linke Halbebene zu seinem Äußeren. Deshalb müssen die Pole eines kausalen, stabilen Systems außerhalb des Einheitskreises liegen.
--- falsch
Die imaginäre Achse wird zum Nullpunkt $z=0$, die linke Halbebene zum Einheitskreis. Alle Frequenzen fallen so in einem Punkt zusammen, deshalb ist das Spektrum einer Folge periodisch.
:::
:::karte formel Grundpaare der z-Transformation
Welche Folgen gehören zum Ausdruck $\frac{z}{z-b}$, und wovon hängt ab, welche gemeint ist?
---
$\varepsilon(n)\,b^n$ für $|z|>|b|$ und $-\varepsilon(-n-1)\,b^n$ für $|z|<|b|$. Derselbe Ausdruck gehört zu zwei Signalen; erst der Konvergenzbereich entscheidet, wie bei der Laplace-Transformation.
--- falsch
Nur $\varepsilon(n)\,b^n$. Der Ausdruck legt die Folge eindeutig fest, der Konvergenzbereich $|z|>|b|$ folgt aus ihm und muss deshalb nicht eigens angegeben werden.
--- falsch
$\varepsilon(n)\,b^n$ für $|z|<|b|$ und $-\varepsilon(-n-1)\,b^n$ für $|z|>|b|$. Derselbe Ausdruck gehört zu zwei Signalen; erst der Konvergenzbereich entscheidet, wie bei der Laplace-Transformation.
--- falsch
$\varepsilon(n)\,b^n$ und $\varepsilon(-n)\,b^{-n}$, je nach Vorzeichen von $b$. Für positives $b$ ist die Folge rechtsseitig, für negatives linksseitig; der Konvergenzbereich spielt dabei keine Rolle.
:::
:::karte zusammenhang Konvergenzbereich und Seite der Folge
Wo liegt der Konvergenzbereich der z-Transformierten bei rechtsseitigen, linksseitigen und zweiseitigen Folgen?
---
Bei rechtsseitigen Folgen außerhalb des Kreises durch den äußersten Pol, bei linksseitigen innerhalb des Kreises durch den innersten Pol, bei zweiseitigen in einem Ring. Für $b^{|n|}$ mit $0<b<1$ ist das der Ring $b<|z|<1/b$.
--- falsch
Bei rechtsseitigen Folgen innerhalb des Kreises durch den innersten Pol, bei linksseitigen außerhalb des Kreises durch den äußersten Pol, bei zweiseitigen in einem Ring. Für $b^{|n|}$ mit $0<b<1$ ist das der Ring $b<|z|<1/b$.
--- falsch
Bei allen Folgen auf dem Einheitskreis und in seiner Nähe, weil dort die Fourier-Transformation existiert. Für $b^{|n|}$ mit $0<b<1$ ist das der Ring $b<|z|<1/b$, der den Einheitskreis enthält.
--- falsch
Bei rechtsseitigen Folgen außerhalb des Kreises durch den äußersten Pol, bei linksseitigen innerhalb des Kreises durch den innersten Pol. Zweiseitige Folgen haben keine z-Transformierte, weil beide Bedingungen zugleich gelten müssten.
:::
:::karte formel Faltung und Verzögerung im z-Bereich
Was wird bei der z-Transformation aus einer Faltung und was aus einer Verzögerung um $n_0$ Takte?
---
Die Faltung wird ein Produkt: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. Die Verzögerung um $n_0$ Takte wird eine Multiplikation mit $z^{-n_0}$. Damit lässt sich jede Differenzengleichung in eine Übertragungsfunktion $H(z)$ umschreiben.
--- falsch
Die Faltung wird ein Produkt: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. Die Verzögerung um $n_0$ Takte wird eine Multiplikation mit $z^{n_0}$, denn eine spätere Folge hat eine größere Potenz von $z$ und rückt so im Bildbereich nach oben.
--- falsch
Die Faltung wird eine Summe: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)+H(z)$. Die Verzögerung um $n_0$ Takte wird eine Multiplikation mit $z^{-n_0}$, wie bei jeder linearen Transformation.
--- falsch
Die Faltung bleibt eine Faltung, nun der z-Transformierten: $G(z)=S(z)*H(z)$. Die Verzögerung um $n_0$ Takte wird eine Verschiebung in der z-Ebene, $S(z-n_0)$.
:::
:::karte herleitung Übertragungsfunktion aus der Differenzengleichung
Wie gewinnt man aus der Differenzengleichung $g(n)=\sum_{q=0}^{Q}a_q\,s(n-q)+\sum_{p=1}^{P}b_p\,g(n-p)$ die Übertragungsfunktion $H(z)=\frac{G(z)}{S(z)}$?
---
Man transformiert beide Seiten, weil die z-Transformation linear ist und jede Summe gliedweise transformiert werden kann.
---
Jedes verzögerte Glied $s(n-q)$ wird zu $S(z)$ mal $z^{-q}$ und jedes $g(n-p)$ zu $G(z)$ mal $z^{-p}$, weil eine Verzögerung um $n_0$ Takte eine Multiplikation mit $z^{-n_0}$ ist.
---
Man bringt alle Glieder mit $G(z)$ auf die linke Seite, weil man nach dem Ausgang auflösen will: $G(z)\bigl[1-\sum_pb_pz^{-p}\bigr]=S(z)\sum_qa_qz^{-q}$.
---
Man teilt durch $S(z)$ und durch die Klammer, weil $H(z)$ das Verhältnis von Ausgang zu Eingang ist: $H(z)=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}$.
:::
:::karte zusammenhang Stabilität kausaler Systeme
Warum ist ein kausales LSI-System genau dann stabil, wenn alle Pole von $H(z)$ im Inneren des Einheitskreises liegen?
---
Kausal heißt: Der Konvergenzbereich liegt außerhalb des äußersten Pols. Stabil heißt $\sum|h(n)|<\infty$; dann konvergiert $H(z)$ auf dem Einheitskreis, er gehört also zum Konvergenzbereich. Beides zusammen geht nur, wenn der äußerste Pol innerhalb des Einheitskreises liegt.
--- falsch
Weil Pole im Inneren des Einheitskreises einen Betrag kleiner 1 haben und deshalb die Impulsantwort begrenzen. Liegt ein Pol außerhalb, ist das System instabil, ganz gleich, wo der Konvergenzbereich liegt und ob das System kausal ist oder nicht.
--- falsch
Kausal heißt: Der Konvergenzbereich liegt innerhalb des innersten Pols. Stabil heißt, dass er den Nullpunkt $z=0$ enthält, weil dort die Summe der Impulsantwort steht. Beides zusammen geht nur, wenn alle Pole im Inneren des Einheitskreises liegen.
--- falsch
Weil der Einheitskreis die Grenze zwischen kausalen und nichtkausalen Systemen bildet. Pole innerhalb gehören zu kausalen Anteilen, Pole außerhalb zu nichtkausalen, und nur kausale Systeme können überhaupt stabil sein.
:::
:::karte zusammenhang Kausal oder stabil
Welche Impulsantworten gehören zu $H(z)=\dfrac{1}{1-2z^{-1}}$, und kann eine davon zugleich kausal und stabil sein?
---
Für $|z|>2$ gehört $h(n)=2^n\varepsilon(n)$ dazu, kausal, aber instabil; für $|z|<2$ gehört $h(n)=-2^n\varepsilon(-n-1)$ dazu, stabil, aber antikausal. Beides zugleich geht nicht, weil der Pol bei $z=2$ außerhalb des Einheitskreises liegt.
--- falsch
Für $|z|>2$ gehört $h(n)=2^n\varepsilon(n)$ dazu, kausal und stabil, weil die Folge erst bei $n=0$ beginnt; für $|z|<2$ gehört $h(n)=-2^n\varepsilon(-n-1)$ dazu, die weder kausal noch stabil ist.
--- falsch
Es gibt nur eine Impulsantwort, $h(n)=2^n\varepsilon(n)$, weil der Ausdruck die Folge eindeutig bestimmt. Sie ist kausal und wird durch den Pol bei $z=2$ stabil gehalten, weil er auf der reellen Achse liegt.
--- falsch
Für $|z|>2$ gehört $h(n)=2^{-n}\varepsilon(n)$ dazu, kausal und stabil; für $|z|<2$ gehört $h(n)=-2^{-n}\varepsilon(-n-1)$ dazu, antikausal und instabil. Das erste System erfüllt also beide Bedingungen zugleich.
:::
:::karte zusammenhang Pole deuten
Was verraten Betrag und Winkel der Pole $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$ der z-Transformierten von $s(n)=0{,}5^n\cos(\pi n/3)\,\varepsilon(n)$ über die Folge?
---
Der Betrag 0,5 gibt das Abklingen je Takt an: Jeder Takt multipliziert die Einhüllende mit 0,5. Der Winkel $\pi/3$ gibt die Schwingung an: $\pi/3$ je Takt, also sechs Takte je Periode.
--- falsch
Der Betrag 0,5 gibt die Amplitude der Schwingung an, die konstant bleibt. Der Winkel $\pi/3$ gibt die Phasenverschiebung gegenüber dem Kosinus an, also einen Versatz um ein Sechstel der Periode.
--- falsch
Der Betrag 0,5 gibt die Frequenz an, also eine Schwingung mit der halben Abtastrate. Der Winkel $\pi/3$ gibt das Abklingen an: Jeder Takt dreht die Folge um $60^\circ$ weiter zur Null hin.
--- falsch
Der Betrag 0,5 gibt das Abklingen je Takt an. Der Winkel $\pi/3$ gibt die Schwingung an: $\pi/3$ je Takt, also drei Takte je Periode, weil der Kosinus schon nach dem Winkel $\pi$ wiederkehrt.
:::
:::karte zusammenhang Spektrum aus der z-Transformierten
Woran erkennt man an der z-Transformierten, ob das Spektrum $S_\mathrm a(f)$ einer Folge existiert, etwa beim Konvergenzbereich $|z|>0{,}5$?
---
Das Spektrum existiert, wenn der Einheitskreis im Konvergenzbereich liegt; dann ist $S(z)$ auf ihm das Spektrum $S_\mathrm a(f)$. Der Bereich $|z|>0{,}5$ enthält den Einheitskreis, das Spektrum existiert also.
--- falsch
Das Spektrum existiert, wenn der Nullpunkt $z=0$ im Konvergenzbereich liegt. Der Bereich $|z|>0{,}5$ enthält ihn nicht, das Spektrum existiert also nicht, obwohl die Folge abklingt.
--- falsch
Das Spektrum existiert immer, wenn die z-Transformierte existiert, weil beide dieselbe Summe sind. Der Konvergenzbereich spielt dafür keine Rolle, er betrifft nur die Rücktransformation.
--- falsch
Das Spektrum existiert, wenn alle Nullstellen auf dem Einheitskreis liegen. Im Beispiel liegen sie bei 0 und 0,25, das Spektrum existiert also nur näherungsweise für tiefe Frequenzen.
:::
::::
