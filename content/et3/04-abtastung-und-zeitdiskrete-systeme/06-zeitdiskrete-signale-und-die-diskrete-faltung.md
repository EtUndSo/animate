---
title: Stufe 5: Zeitdiskrete Signale und die diskrete Faltung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240600
summary: Ab jetzt rechnet man nur noch mit den Zahlenfolgen s(n) .
tags: diskrete Faltung, Einheitsimpuls, verschiebungsinvariant, LSI-System, Impulsantwort, Differenz, Akkumulation, FIR-Filter
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ab jetzt rechnet man nur noch mit den Zahlenfolgen $s(n)$. Diese Stufe überträgt Faltung, Elementarsignale und LTI-Systeme auf Folgen.
:::

**Faltung der Abtastwerte.** Sind Eingang $s$ und Impulsantwort $h$ eines Systems Tiefpasssignale und wird mit der Nyquist-Rate abgetastet, lässt sich jedes als si-Reihe [(3.3)](abtasttheorem-und-ruckgewinnung.html#gl-3-3) schreiben. Weil $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ist ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), folgt für die Abtastwerte des Ausgangs allein

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

Normiert auf $T=1$ ist das die __diskrete Faltung__:

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**Elementarfolgen.**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

Der __Einheitsimpuls__ $\delta(n)$ ist eine gewöhnliche Folge, keine Distribution: Er hat bei $n=0$ den Wert 1. Er ist das Einselement der diskreten Faltung, $s(n)*\delta(n)=s(n)$. Ein Rechteck aus $2M+1$ Einsen um $n=0$ ist $\varepsilon(n+M)-\varepsilon(n-M-1)$.

**Linear und verschiebungsinvariant.** Ein zeitdiskretes System heißt linear, wenn der Überlagerungssatz gilt, und __verschiebungsinvariant__, wenn $\operatorname{Tr}\{s(n-m)\}=g(n-m)$ für jede ganze Zahl $m$. Zusammen heißt es __LSI-System__. Mit der __Impulsantwort__ $h(n)=\operatorname{Tr}\{\delta(n)\}$ folgt wie in [Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html):

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

Hier braucht man keinen Grenzübergang: Eine Folge *ist* schon eine Summe gewichteter, verschobener Einheitsimpulse.

**Differenz und Summe.** Das Gegenstück zur Ableitung ist die __Differenz__ $g(n)=s(n)-s(n-1)$, also $h(n)=\delta(n)-\delta(n-1)$. Das Gegenstück zum Integral ist die __Akkumulation__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$. Beide heben sich auf: $[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$.

**Differenzengleichungen, FIR und IIR.** Statt Differentialgleichungen beschreiben Differenzengleichungen zeitdiskrete Systeme:

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{FIR-Teil}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{IIR-Teil}}. \tag{5.2}$$

Der Ausgang ist eine gewichtete Summe vergangener Eingangs- und Ausgangswerte. Hängt er nur von Eingangswerten ab ($b_p=0$), ist die Impulsantwort nach $Q+1$ Werten zu Ende: ein __FIR-Filter__ (finite impulse response). Mit Rückkopplung ($b_p\neq0$) kann die Impulsantwort unendlich lang sein: ein __IIR-Filter__ (infinite impulse response). Gebaut wird beides aus Verzögerungsgliedern (Speicher für einen Takt), Multiplizierern und Addierern (Abb. [4](#abb-4)).

:::abbildung et3/k4block 4
System erster Ordnung $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$. Das Kästchen $T$ speichert einen Wert für einen Takt. Links der nichtrekursive Teil, rechts die Rückkopplung des Ausgangs.
:::

:::aufgabe Aufgabe 4 ★ Diskrete Faltung von Hand
<span class="anker" id="aufg-4"></span>

Falte $s=(1,1,1)$ mit $h=(1,2)$, beide beginnend bei $n=0$. Wie lang ist das Ergebnis, und warum?

:::loesung
$g(0)=1$, $g(1)=1\cdot2+1\cdot1=3$, $g(2)=3$, $g(3)=1\cdot2=2$: $(1,3,3,2)$. Länge $3+2-1=4$: Der letzte von null verschiedene Wert entsteht, wenn der letzte Wert von $h$ auf den letzten Wert von $s$ trifft.
:::
:::
