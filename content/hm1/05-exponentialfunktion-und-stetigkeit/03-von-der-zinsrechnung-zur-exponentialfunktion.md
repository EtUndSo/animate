---
title: Stufe 1: Von der Zinsrechnung zur Exponentialfunktion
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
order: 1250300
summary: Potenzen a x gibt es bisher nur für rationale x .
tags: Eulersche Zahl, Funktionalgleichung, kontinuierliche Verzinsung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Potenzen $a^x$ gibt es bisher nur für rationale $x$. Diese Stufe baut eine Funktion, die für jedes reelle $x$ erklärt ist, und zeigt, dass sie sich wie eine Potenz verhält.
:::

**Die Idee.** Ein Kapital $K_0$ wächst jährlich um $p$ Prozent, nach $k$ Jahren ist es $E_k=K_0(1+\frac p{100})^k$. Wird der Zins in $n$ Raten pro Jahr gezahlt ($n=12$: monatlich), gibt es je Termin $p/n$ Prozent, und die gezahlten Zinsen verzinsen sich mit:

<span class="anker" id="gl-1-1"></span>
$$E_k^{(n)}=K_0\Bigl(1+\frac p{n\cdot100}\Bigr)^{n\cdot k}. \tag{1.1}$$

Für $K_0=1000$ Euro, $p=5$, $k=10$ ergibt das $1628{,}89$ Euro jährlich und $1647{,}01$ Euro monatlich. Der Betrag steigt mit $n$, bleibt aber unter $1648{,}73$ Euro. Mit $x=p/100$ steht in der Klammer $(1+\frac xn)^n$. Das ist der Baustein für alles, was in jedem kleinen Schritt um denselben Bruchteil wächst oder schrumpft, etwa die Ladung eines Kondensators, der sich über einen Widerstand entlädt.

:::satz Satz 1.1 (Exponentialfolge)
<span class="anker" id="satz-1-1"></span>

Für festes $x\in\mathbb{R}$ sei $z_n(x):=\bigl(1+\frac xn\bigr)^n$, $n\in\mathbb{N}$. Für $n>|x|$ gilt $z_n(x)>0$. Für $x\ne0$ gilt

<span class="anker" id="gl-1-2"></span>
$$\frac{z_{n+1}(x)}{z_n(x)}>1\qquad\text{für }n>|x|, \tag{1.2}$$

für $x>0$ sogar für alle $n\in\mathbb{N}$. Außerdem ist $\{z_n(x)\}$ beschränkt. Nach dem Monotonie-Lemma ist die Folge für jedes feste $x$ konvergent.
:::

⁠**So liest man das:** $x$ ist ein fester Parameter, $n$ die Zahl der Schritte. Die Bedingung $n>|x|$ sorgt für eine positive Klammer: Für $x=-3$ ist $z_3=0$, aber endlich viele Glieder zählen nie. Für $x=0$ ist $z_n=1$, deshalb $x\ne0$.

:::beweis Monotonie mit Bernoulli, Schranke mit dem Spiegelbild
Sei $x\ne0$ und $n>|x|$, also $1+\frac xn>0$ und $1+\frac x{n+1}>0$ (für $x>0$ gilt das für alle $n$). Setze $A:=\bigl(1+\frac x{n+1}\bigr)\big/\bigl(1+\frac xn\bigr)>0$ und $h:=A-1>-1$. Dann ist

$$h=\frac{\frac x{n+1}-\frac xn}{1+\frac xn}=\frac{-x}{n(n+1)\bigl(1+\frac xn\bigr)}\ne0,$$

und Bernoulli gibt

$$\frac{z_{n+1}(x)}{z_n(x)}=A^{n+1}\Bigl(1+\frac xn\Bigr)>\bigl(1+(n+1)h\bigr)\Bigl(1+\frac xn\Bigr)=1+\frac xn-\frac xn=1.$$

Zur Schranke: Für $n>|x|$ ist auch $z_n(-x)>0$ und wachsend, also ist $b_n:=1/z_n(-x)$ positiv und fallend. Wegen $0<1-\frac{x^2}{n^2}<1$ gilt

$$\frac{z_n(x)}{b_n}=z_n(x)\,z_n(-x)=\Bigl(1-\frac{x^2}{n^2}\Bigr)^n\le1.$$

Mit $n_0:=\lfloor|x|\rfloor+1$ folgt $z_n(x)\le b_n\le b_{n_0}$ für alle $n\ge n_0$. Davor stehen nur endlich viele Glieder.
:::

:::definition Definition 1.2 (Exponentialfunktion, Eulersche Zahl)
<span class="anker" id="satz-1-2"></span>

Die Funktion

<span class="anker" id="gl-1-3"></span>
$$\exp:\mathbb{R}\to\mathbb{R},\qquad\exp(x):=\lim_{n\to\infty}\Bigl(1+\frac xn\Bigr)^n \tag{1.3}$$

heißt Exponentialfunktion, und $\mathrm{e}:=\exp(1)=\lim_{n\to\infty}(1+\frac1n)^n\approx2{,}71828$ heißt __Eulersche Zahl__.
:::

⁠**So liest man das:** Jedes $x$ hat seine eigene Folge, ihr Grenzwert ist der Funktionswert. Die Konvergenz ist langsam, $z_{10}(1)=2{,}5937$, $z_{1000}(1)=2{,}7169$: Hundertmal so viele Schritte machen den Abstand zu $\mathrm{e}$ rund hundertmal kleiner. **Grenzfall:** $n=1$ ergibt die Gerade $z_1(x)=1+x$ (Abb. [1](#abb-1)).

:::abbildung hm1/k5zins 1
Links steigt $z_n(1)$ gegen $\mathrm{e}$. Rechts $z_1$, $z_2$, $z_5$ und die Grenzfunktion $\mathrm{e}^x$: Für $x\ne0$ liegt jede Kurve unter der nächsten.
:::

:::satz Satz 1.3 (Erste Eigenschaften der Exponentialfunktion)
<span class="anker" id="satz-1-3"></span>

Für alle $x,y\in\mathbb{R}$ gilt: (i) $\exp(0)=1$, (ii) $\exp(x+y)=\exp(x)\cdot\exp(y)$ (__Funktionalgleichung__ von $\exp$), (iii) $\exp(x)>0$, (iv) $\exp(-x)=1/\exp(x)$.
:::

⁠**So liest man das:** Aus einer Addition am Eingang wird eine Multiplikation am Ausgang: Zehn Jahre Verzinsung sind fünf Jahre und noch einmal fünf.

Für (ii) wird eine Formel gebraucht, die für $b=1$ die geometrische Summe aus [Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) ist: Für $a,b\in\mathbb{R}$, $n\in\mathbb{N}$ gilt

<span class="anker" id="gl-1-4"></span>
$$a^n-b^n=(a-b)\sum_{k=1}^na^{n-k}\,b^{k-1}. \tag{1.4}$$

Ausmultiplizieren gibt nämlich die Teleskopsumme $\sum_{k=1}^n\bigl(a^{n+1-k}b^{k-1}-a^{n-k}b^k\bigr)=a^n-b^n$.

:::beweis Erste Eigenschaften
(i) $z_n(0)=1$. (iii) Für $n>|x|$ ist $z_n(x)>0$, und die Folge wächst, also ist der Grenzwert positiv. (iv) folgt aus (i) und (ii): $1=\exp(x-x)=\exp(x)\exp(-x)$.

(ii) Sei $x,y\ne0$ (sonst gilt die Gleichung wegen (i)). Setze $a:=1+\frac{x+y}n$ und $b:=(1+\frac xn)(1+\frac yn)$, also $a-b=-\frac{xy}{n^2}$. Nach den Rechenregeln und [(1.4)](#gl-1-4) ist

$$\exp(x+y)-\exp(x)\exp(y)=\lim_{n\to\infty}(a^n-b^n)=\lim_{n\to\infty}\Bigl[-\frac{xy}{n^2}\sum_{k=1}^na^{n-k}b^{k-1}\Bigr].$$

Die Dreiecksungleichung gibt $|a|\le c$ und $|b|\le c$ für $c:=(1+\frac{|x|}n)(1+\frac{|y|}n)\ge1$. Jeder der $n$ Summanden ist also betragsmäßig höchstens

$$c^{\,n-1}\le\Bigl(1+\frac{|x|}n\Bigr)^n\Bigl(1+\frac{|y|}n\Bigr)^n=z_n(|x|)\,z_n(|y|)\le\exp(|x|)\exp(|y|)=:D,$$

denn $z_n(|x|)$ wächst gegen $\exp(|x|)$. Die Schranke $D$ hängt nicht von $n$ ab. Die Klammer ist damit betragsmäßig höchstens $\frac{|xy|}{n^2}\cdot n\,D=\frac{|xy|D}n$, und das ist eine Nullfolge.
:::

**Warum die Schreibweise $\mathrm{e}^x$ passt.** Für $a>0$, $p\in\mathbb{Z}$, $q\in\mathbb{N}$ ist die rationale Potenz $a^{p/q}:=\sqrt[q]{a^p}=(\sqrt[q]a)^p$ mit der Wurzel aus [Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html). Für $x=\frac pq$ gibt die Funktionalgleichung (für $p<0$ mit (iv))

$$\bigl(\exp(x)\bigr)^q=\exp(qx)=\exp(p)=\bigl(\exp(1)\bigr)^p=\mathrm{e}^p.$$

Weil $\exp(x)>0$ ist, folgt $\exp(\frac pq)=\sqrt[q]{\mathrm{e}^p}=\mathrm{e}^{p/q}$. Für irrationale $x$ definiert man $\mathrm{e}^x:=\exp(x)$, damit gilt $\mathrm{e}^x=\exp(x)$ für alle $x\in\mathbb{R}$. Zum Beispiel ist $\mathrm{e}^{1/2}=\sqrt\mathrm{e}=1{,}6487$ und $\mathrm{e}^{-1}=0{,}3679$. Für [(1.1)](#gl-1-1) folgt mit $n\to\infty$ die __kontinuierliche Verzinsung__ $E_k^{(\infty)}=K_0\,(\mathrm{e}^{p/100})^k$.

:::frage Die Klammer in $(1+\frac1n)^n$ geht gegen 1. Warum ist der Grenzwert nicht 1?
Die Rechenregeln gelten für eine feste Zahl von Faktoren. Hier wächst die Zahl der Faktoren mit, während jeder Faktor gegen 1 geht. Beide Effekte konkurrieren, das Ergebnis liegt zwischen 2 und 3.
:::

:::aufgabe Aufgabe 1 ★ Zinsen
<span class="anker" id="aufg-1"></span>

$K_0=2000$ Euro, $p=3$, $k=20$. (a) Berechne $E_k$, $E_k^{(12)}$ und $E_k^{(\infty)}$. (b) Sage vorher: Bringt tägliche Zahlung ($n=365$) mehr als $E_k^{(\infty)}$? (c) Berechne $z_4(2)$ und $z_{50}(2)$ und vergleiche mit $\mathrm{e}^2$.

:::loesung
(a) $E_{20}=2000\cdot1{,}03^{20}=3612{,}22$ Euro, $E_{20}^{(12)}=2000\,(1+\frac{0{,}03}{12})^{240}=3641{,}51$ Euro, $E_{20}^{(\infty)}=2000\,\mathrm{e}^{0{,}6}=3644{,}24$ Euro. (b) Nein, $z_n(x)$ bleibt unter $\mathrm{e}^x$: $n=365$ ergibt $3644{,}15$ Euro. (c) $z_4(2)=1{,}5^4=5{,}0625$, $z_{50}(2)=1{,}04^{50}=7{,}1067$, $\mathrm{e}^2=7{,}3891$.
:::
:::
