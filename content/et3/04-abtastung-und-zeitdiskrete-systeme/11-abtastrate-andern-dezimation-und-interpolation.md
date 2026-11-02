---
title: Stufe 10: Abtastrate ändern, Dezimation und Interpolation
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Abtastung und zeitdiskrete Systeme
order: 3241100
summary: Eine Folge lässt sich nachträglich mit niedrigerer oder höherer Rate darstellen.
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Eine Folge lässt sich nachträglich mit niedrigerer oder höherer Rate darstellen. Für das Spektrum gelten dieselben Regeln wie beim ersten Abtasten.
:::

**Herabtasten um den Faktor $c$.** Man behält nur jeden $c$-ten Wert. Gedanklich erst mit einem Kamm aus Einheitsimpulsen multiplizieren, dann die Nullen weglassen:

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

Die Multiplikation mit dem Kamm erzeugt $c$ Kopien des Spektrums im Abstand $1/c$, das Weglassen der Nullen dehnt die Frequenzachse um $c$:

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

Reicht das Spektrum bis $f_\mathrm g$ (bezogen auf die alte Rate), reicht es nach dem Herabtasten bis $cf_\mathrm g$. Kein Aliasing gibt es nur, wenn $cf_\mathrm g\le\frac12$. Sonst muss vorher ein digitaler Tiefpass das Band begrenzen.

**Hochtasten um den Faktor $c$.** Man fügt zwischen je zwei Werte $c-1$ Nullen ein, $s_\uparrow(n)=s(n/c)$ für durch $c$ teilbare $n$, sonst 0. Das Spektrum wird um $c$ gestaucht, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, und enthält jetzt $c-1$ Spiegelspektren in der Periode. Ein Tiefpass mit der Grenzfrequenz $\frac{1}{2c}$ und der Verstärkung $c$ entfernt sie. Dabei füllt er die Nullen mit interpolierten Werten (die si-Interpolation aus Stufe [3](abtasttheorem-und-ruckgewinnung.html#stufe-3) in diskreter Form), die ursprünglichen Werte bleiben erhalten. Herab- und Hochtasten nacheinander ändern die Rate um einen rationalen Faktor $c_1/c_2$.

:::abbildung et3/k4rate 7
Spektren (Frequenz bezogen auf die jeweilige Rate) beim Ändern der Abtastrate. Herabtasten dehnt das Band, Hochtasten staucht es und erzeugt Spiegelspektren, die ein Interpolationsfilter entfernt.
:::

:::aufgabe Aufgabe 10 ★★ Herabtasten
<span class="anker" id="aufg-10"></span>

Eine Folge hat ein Spektrum bis $f_\mathrm g=0{,}2$.

<ol class="al">

<li>

Darf man sie ohne Vorfilter um $c=2$ herabtasten? Um $c=3$?

</li>

<li>

Was muss vor dem Herabtasten um $c=3$ geschehen, und was verliert man dabei?

</li>

</ol>

:::loesung
(a) $c=2$: Das Band reicht danach bis $0{,}4\le0{,}5$, kein Aliasing. $c=3$: bis $0{,}6>0{,}5$, Aliasing.

(b) Vorher mit einem digitalen Tiefpass auf $\frac{1}{2c}=\frac16\approx0{,}167$ begrenzen. Die Anteile zwischen 0,167 und 0,2 gehen dabei verloren. Das ist der Preis der niedrigeren Rate.
:::
:::
