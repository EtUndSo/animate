---
title: Stufe 6: Ein rekursives System
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240700
summary: Am einfachsten IIR-System sieht man, wie Rückkopplung eine unendlich lange Impulsantwort erzeugt und wann das System stabil ist.
tags: kausal, stabil
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Am einfachsten IIR-System sieht man, wie Rückkopplung eine unendlich lange Impulsantwort erzeugt und wann das System stabil ist.
:::

Das System $g(n)=s(n)+b\,g(n-1)$ addiert zum Eingang den mit $b$ gewichteten letzten Ausgang. Für $s=\delta$ und Ruhe vor $n=0$:

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

Der Stoß läuft in der Rückkopplung immer wieder herum und wird jedes Mal mit $b$ multipliziert. Das System ist __kausal__ ($h(n)=0$ für $n<0$). Es ist __stabil__, wenn $\sum_n|h(n)|<\infty$ (das diskrete Gegenstück zu [Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)), hier also genau für $|b|<1$, mit $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Antwort auf eine Rechteckfolge.** Eingang $s(n)=\varepsilon(n)-\varepsilon(n-M)$ ($M$ Einsen). Mit der Faltungssumme und der geometrischen Summenformel $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$:

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

Im Rechenmodell ($b=0{,}6$, $M=4$): $g=1;\ 1{,}6;\ 1{,}96;\ 2{,}176$, danach $1{,}306;\ 0{,}783;\ 0{,}470;\dots$, jeder Wert das 0,6-Fache des vorigen (Abb. [5](#abb-5)). Das ist das diskrete Gegenstück zur Rechteckantwort des RC-Glieds in [Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html).

:::abbildung et3/k4rek 5
Das rekursive System mit $b=0{,}6$. Links die Impulsantwort. Rechts die Antwort auf vier Einsen: Sie steigt bis 2,176 an und klingt danach mit dem Faktor 0,6 je Takt ab.
:::

:::aufgabe Aufgabe 5 ★★ Das rekursive System untersuchen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Bestätige die ersten fünf Werte von $g(n)$ im Rechenmodell direkt mit der Rekursion.

</li>

<li>

Gegen welchen Wert strebt der Ausgang bei einer unendlich langen Folge von Einsen ($M\to\infty$)? Vergleiche mit $\sum_nh(n)$.

</li>

<li>

Wie sieht $h(n)$ für $b=-0{,}6$ und für $b=1{,}1$ aus? Welches System ist stabil?

</li>

</ol>

:::loesung
(a) $g(0)=1$, $g(1)=1+0{,}6=1{,}6$, $g(2)=1+0{,}96=1{,}96$, $g(3)=1+1{,}176=2{,}176$, $g(4)=0+0{,}6\cdot2{,}176=1{,}306$.

(b) $\frac{1}{1-b}=2{,}5$. Das ist $\sum_nh(n)=\sum0{,}6^n=2{,}5$: Bei konstantem Eingang 1 summiert die Faltung alle Werte der Impulsantwort. Es ist auch $H_\mathrm a(0)=2{,}5$.

(c) $b=-0{,}6$: $1;\ -0{,}6;\ 0{,}36;\ -0{,}216;\dots$, wechselndes Vorzeichen, abklingend, stabil. $b=1{,}1$: $1;\ 1{,}1;\ 1{,}21;\dots$, wachsend, instabil.
:::
:::

:::aufgabe Aufgabe 6 ★★ System erster Ordnung
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0{,}5\,s(n-1)+0{,}6\,g(n-1)$ (Abb. [4](zeitdiskrete-signale-und-die-diskrete-faltung.html#abb-4) mit $a_0=1$, $a_1=0{,}5$, $b_1=0{,}6$).

<ol class="al">

<li>

Berechne $h(0)$ bis $h(3)$ mit der Rekursion.

</li>

<li>

Zeige, dass $h(n)=\frac{11}{6}\,0{,}6^n\varepsilon(n)-\frac56\delta(n)$ ist.

</li>

</ol>

:::loesung
(a) $h(0)=1$, $h(1)=0{,}5+0{,}6\cdot1=1{,}1$, $h(2)=0{,}6\cdot1{,}1=0{,}66$, $h(3)=0{,}396$.

(b) Die Formel gibt $h(0)=\frac{11}{6}-\frac56=1$ und $h(1)=\frac{11}{6}\cdot0{,}6=1{,}1$. Ab $n=2$ ist der Eingang null, die Rekursion lautet $h(n)=0{,}6\,h(n-1)$, und die Formel erfüllt sie, weil $\frac{11}{6}0{,}6^n=0{,}6\cdot\frac{11}{6}0{,}6^{n-1}$. (Mit der z-Transformation folgt die Formel aus der Zerlegung $H(z)=-\frac56+\frac{11/6}{1-0{,}6z^{-1}}$.)
:::
:::
