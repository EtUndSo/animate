---
title: Stufe 1: Von der Zinsrechnung zur Exponentialfunktion
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
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

Für (ii) wird eine Formel gebraucht, die für $b=1$ die geometrische Summe aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) ist: Für $a,b\in\mathbb{R}$, $n\in\mathbb{N}$ gilt

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

**Warum die Schreibweise $\mathrm{e}^x$ passt.** Für $a>0$, $p\in\mathbb{Z}$, $q\in\mathbb{N}$ ist die rationale Potenz $a^{p/q}:=\sqrt[q]{a^p}=(\sqrt[q]a)^p$ mit der Wurzel aus [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html). Für $x=\frac pq$ gibt die Funktionalgleichung (für $p<0$ mit (iv))

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

::::formelsammlung
**Zinseszins**

$$E_k=K_0(1+\frac p{100})^k$$

Kapital $K_0$, $p$ Prozent Zins im Jahr, Betrag nach $k$ Jahren.

**Verzinsung in Raten**

$$E_k^{(n)}=K_0\Bigl(1+\frac p{n\cdot100}\Bigr)^{n\cdot k}$$

$n$ Zinstermine im Jahr mit je $p/n$ Prozent; die gezahlten Zinsen verzinsen sich mit. Mit $x=p/100$ steht in der Klammer $(1+\frac xn)^n$.

**Exponentialfolge**

$$z_n(x):=\bigl(1+\frac xn\bigr)^n,\qquad\frac{z_{n+1}(x)}{z_n(x)}>1\quad\text{für }n>|x|$$

Für festes $x\ne0$, bei $x>0$ für alle $n\in\mathbb{N}$. Für $n>|x|$ ist $z_n(x)>0$; die Folge ist beschränkt und konvergiert nach dem Monotonie-Lemma.

**Schranke**

$$z_n(x)\,z_n(-x)=\Bigl(1-\frac{x^2}{n^2}\Bigr)^n\le1$$

Für $n>|x|$; also $z_n(x)\le b_n:=1/z_n(-x)$, und $b_n$ fällt.

**Exponentialfunktion**

$$\exp:\mathbb{R}\to\mathbb{R},\qquad\exp(x):=\lim_{n\to\infty}\Bigl(1+\frac xn\Bigr)^n$$

Jedes $x$ hat seine eigene Folge; ihr Grenzwert ist der Funktionswert.

**Eulersche Zahl**

$$\mathrm{e}:=\exp(1)=\lim_{n\to\infty}(1+\frac1n)^n\approx2{,}71828$$

Die Konvergenz ist langsam: Hundertmal so viele Schritte machen den Abstand zu $\mathrm{e}$ rund hundertmal kleiner.

**Erste Eigenschaften**

$$\exp(0)=1,\quad\exp(x+y)=\exp(x)\cdot\exp(y),\quad\exp(x)>0,\quad\exp(-x)=1/\exp(x)$$

Für alle $x,y\in\mathbb{R}$; die zweite Gleichung ist die Funktionalgleichung von $\exp$: Aus einer Addition am Eingang wird eine Multiplikation am Ausgang.

**Differenz zweier Potenzen**

$$a^n-b^n=(a-b)\sum_{k=1}^na^{n-k}\,b^{k-1}$$

Für $a,b\in\mathbb{R}$, $n\in\mathbb{N}$; für $b=1$ die geometrische Summe.

**Rationale Potenz**

$$a^{p/q}:=\sqrt[q]{a^p}=(\sqrt[q]a)^p,\qquad\exp(\frac pq)=\sqrt[q]{\mathrm{e}^p}=\mathrm{e}^{p/q}$$

Für $a>0$, $p\in\mathbb{Z}$, $q\in\mathbb{N}$. Für irrationale $x$ definiert man $\mathrm{e}^x:=\exp(x)$, damit gilt $\mathrm{e}^x=\exp(x)$ für alle $x\in\mathbb{R}$.

**Kontinuierliche Verzinsung**

$$E_k^{(\infty)}=K_0\,(\mathrm{e}^{p/100})^k$$

Grenzfall $n\to\infty$ der Verzinsung in Raten; jeder Betrag mit endlich vielen Raten bleibt darunter.
::::

::::lernkarten
:::karte formel Verzinsung in Raten
Welchen Betrag $E_k^{(n)}$ erreicht ein Kapital $K_0$ nach $k$ Jahren bei $p$ Prozent Jahreszins, wenn der Zins in $n$ Raten pro Jahr gezahlt wird?
---
$E_k^{(n)}=K_0\Bigl(1+\frac p{n\cdot100}\Bigr)^{n\cdot k}$: Je Termin gibt es $p/n$ Prozent, es gibt $n\cdot k$ Termine, und die gezahlten Zinsen verzinsen sich mit.
--- falsch
$E_k^{(n)}=K_0\Bigl(1+\frac p{100}\Bigr)^{n\cdot k}$: Je Termin gibt es die vollen $p$ Prozent, es gibt $n\cdot k$ Termine, und die gezahlten Zinsen verzinsen sich mit.
--- falsch
$E_k^{(n)}=K_0\Bigl(1+\frac p{n\cdot100}\Bigr)^{k}$: Je Termin gibt es $p/n$ Prozent; gezählt werden nur die $k$ Jahre, weil die Raten eines Jahres zusammengehören.
--- falsch
$E_k^{(n)}=K_0\Bigl(1+\frac{p\cdot k}{100}\Bigr)$: Die Zinsen werden in jedem Jahr nur auf $K_0$ gezahlt, die Zahl $n$ der Raten ändert deshalb nichts am Betrag.
:::
:::karte formel Exponentialfolge
Was sagt der Satz über die Exponentialfolge $z_n(x)=\bigl(1+\frac xn\bigr)^n$ über Vorzeichen, Monotonie und Konvergenz bei festem $x$?
---
Für $n>|x|$ ist $z_n(x)>0$. Für $x\ne0$ wächst die Folge streng ab $n>|x|$, für $x>0$ sogar ab $n=1$. Sie ist beschränkt und konvergiert deshalb nach dem Monotonie-Lemma.
--- falsch
Für alle $n$ ist $z_n(x)>0$. Für $x\ne0$ fällt die Folge streng, weil die Klammer $1+\frac xn$ gegen 1 schrumpft. Sie ist beschränkt und konvergiert deshalb gegen 1.
--- falsch
Für $n>|x|$ ist $z_n(x)>0$. Für $x\ne0$ wächst die Folge streng ab $n>|x|$, ist aber unbeschränkt, weil die Zahl der Faktoren wächst; sie konvergiert deshalb nicht.
--- falsch
Für $n>|x|$ ist $z_n(x)>0$. Für $x>0$ wächst die Folge streng, für $x<0$ fällt sie streng. Sie ist beschränkt und konvergiert deshalb nach dem Monotonie-Lemma.
:::
:::karte herleitung Monotonie mit Bernoulli
Wie zeigt man mit der Bernoulli-Ungleichung, dass $z_n(x)=\bigl(1+\frac xn\bigr)^n$ für $x\ne0$ und $n>|x|$ streng wächst?
---
Wegen $n>|x|$ sind $1+\frac xn>0$ und $1+\frac x{n+1}>0$; man setzt $A:=\bigl(1+\frac x{n+1}\bigr)\big/\bigl(1+\frac xn\bigr)>0$ und $h:=A-1>-1$, weil $A$ positiv ist.
---
Es ist $h=\frac{-x}{n(n+1)\bigl(1+\frac xn\bigr)}\ne0$, weil der Zähler $\frac x{n+1}-\frac xn$ von $A-1$ für $x\ne0$ nicht null ist.
---
Der Quotient ist $\frac{z_{n+1}(x)}{z_n(x)}=A^{n+1}\Bigl(1+\frac xn\Bigr)$, weil man im Zähler $n+1$ Faktoren $1+\frac x{n+1}$ hat und im Nenner nur $n$ Faktoren $1+\frac xn$.
---
Bernoulli mit $m=n+1\ge2$ gibt $A^{n+1}>1+(n+1)h$, weil $h>-1$ und $h\ne0$ ist.
---
Also $\frac{z_{n+1}(x)}{z_n(x)}>\bigl(1+(n+1)h\bigr)\Bigl(1+\frac xn\Bigr)=1+\frac xn-\frac xn=1$, weil $(n+1)h$ mal $1+\frac xn$ genau $-\frac xn$ ergibt.
:::
:::karte zusammenhang Schranke mit dem Spiegelbild
Warum ist die Exponentialfolge $z_n(x)$ nach oben beschränkt, und welche Rolle spielt dabei das Spiegelbild $z_n(-x)$?
---
Weil $z_n(x)\,z_n(-x)=\Bigl(1-\frac{x^2}{n^2}\Bigr)^n\le1$ ist, gilt $z_n(x)\le b_n:=1/z_n(-x)$. Da $z_n(-x)$ wächst, fällt $b_n$, also $z_n(x)\le b_{n_0}$ für alle $n\ge n_0:=\lfloor|x|\rfloor+1$.
--- falsch
Weil jeder Faktor $1+\frac xn$ höchstens $1+x$ ist, ist das Produkt durch $1+x$ beschränkt; das Spiegelbild $z_n(-x)$ wird dafür gar nicht gebraucht.
--- falsch
Weil $z_n(x)+z_n(-x)=2$ ist, gilt $z_n(x)\le2$: Was die Folge bei $x$ gewinnt, verliert sie bei $-x$. Deshalb ist 2 eine gemeinsame Schranke für alle $x$.
--- falsch
Weil $z_n(x)\,z_n(-x)=\Bigl(1-\frac{x^2}{n^2}\Bigr)^n\le1$ ist, gilt $z_n(x)\le1$ für alle $n$, denn auch das Spiegelbild $z_n(-x)$ ist stets mindestens 1.
:::
:::karte begriff Exponentialfunktion
Wie ist die Exponentialfunktion $\exp(x)$ für jedes reelle $x$ definiert?
---
Als Funktion $\exp:\mathbb{R}\to\mathbb{R}$, $\exp(x):=\lim_{n\to\infty}\Bigl(1+\frac xn\Bigr)^n$: Jedes $x$ hat seine eigene Folge, und deren Grenzwert ist der Funktionswert.
--- falsch
Als Funktion $\exp:\mathbb{R}\to\mathbb{R}$, $\exp(x):=x\cdot\lim_{n\to\infty}\Bigl(1+\frac 1n\Bigr)^{n}$: Man berechnet einmal den Grenzwert $\mathrm{e}$ und multipliziert ihn mit $x$.
--- falsch
Als Funktion $\exp:\mathbb{N}\to\mathbb{R}$, $\exp(n):=\Bigl(1+\frac 1n\Bigr)^n$: Erklärt ist sie nur für natürliche Zahlen, an denen man die Folge direkt auswertet.
--- falsch
Als Funktion $\exp:\mathbb{R}\to\mathbb{R}$, $\exp(x):=\lim_{n\to\infty}\Bigl(1+\frac xn\Bigr)$: Die Klammer läuft für jedes $x$ gegen einen Grenzwert, und dieser ist der Funktionswert.
:::
:::karte begriff Eulersche Zahl
Wie ist die Eulersche Zahl $\mathrm{e}$ über die Exponentialfunktion definiert, und welchen Wert hat sie ungefähr?
---
$\mathrm{e}:=\exp(1)=\lim_{n\to\infty}(1+\frac1n)^n\approx2{,}71828$: der Wert der Exponentialfunktion an der Stelle 1.
--- falsch
$\mathrm{e}:=\exp(0)=\lim_{n\to\infty}(1+\frac0n)^n\approx2{,}71828$: der Wert der Exponentialfunktion an der Stelle 0, also ihr Startwert.
--- falsch
$\mathrm{e}:=\exp(1)\approx2{,}5937$, also $(1+\frac1{10})^{10}$: Schon zehn Schritte liefern den Grenzwert, weitere ändern nichts mehr.
--- falsch
$\mathrm{e}:=\exp(1)=\lim_{n\to\infty}(1+\frac1n)^n=3$: Die Folge wächst und bleibt unter 3, also ist 3 ihr Grenzwert.
:::
:::karte begriff Funktionalgleichung
Was besagt die Funktionalgleichung der Exponentialfunktion, und wie lässt sie sich anschaulich lesen?
---
$\exp(x+y)=\exp(x)\cdot\exp(y)$ für alle $x,y\in\mathbb{R}$: Aus einer Addition am Eingang wird eine Multiplikation am Ausgang; zehn Jahre Verzinsung sind fünf und noch einmal fünf.
--- falsch
$\exp(x\cdot y)=\exp(x)+\exp(y)$ für alle $x,y\in\mathbb{R}$: Aus einer Multiplikation am Eingang wird eine Addition am Ausgang, so wie beim Rechnen mit einem Rechenschieber.
--- falsch
$\exp(x+y)=\exp(x)+\exp(y)$ für alle $x,y\in\mathbb{R}$: Die Funktion ist additiv; zehn Jahre Verzinsung bringen genau doppelt so viel wie fünf Jahre Verzinsung.
--- falsch
$\exp(x+y)=\exp(x)\cdot\exp(y)$, aber nur für $x,y>0$: Für negative Zahlen bricht sie zusammen, weil die Klammer $1+\frac xn$ dann negativ werden kann.
:::
:::karte formel Erste Eigenschaften der Exponentialfunktion
Welche Werte und Vorzeichen hat die Exponentialfunktion nach ihren ersten Eigenschaften, und wie hängen $\exp(x)$ und $\exp(-x)$ zusammen?
---
$\exp(0)=1$, $\exp(x)>0$ für alle $x\in\mathbb{R}$ und $\exp(-x)=1/\exp(x)$; das Letzte folgt aus $1=\exp(x-x)=\exp(x)\exp(-x)$.
--- falsch
$\exp(0)=0$, $\exp(x)>0$ nur für $x>0$ und $\exp(-x)=-\exp(x)$; die Funktion ist also ungerade wie $x^3$.
--- falsch
$\exp(0)=1$, $\exp(x)\ge0$ mit $\exp(x)=0$ für sehr negative $x$, und $\exp(-x)=1/\exp(x)$ nur für $x\ge0$.
--- falsch
$\exp(0)=1$, $\exp(x)>0$ für alle $x\in\mathbb{R}$ und $\exp(-x)=1-\exp(x)$; das folgt aus $\exp(x)+\exp(-x)=\exp(0)=1$.
:::
:::karte herleitung Beweis der Funktionalgleichung
Wie zeigt man $\exp(x+y)=\exp(x)\cdot\exp(y)$ für $x,y\ne0$ mit $a:=1+\frac{x+y}n$ und $b:=(1+\frac xn)(1+\frac yn)$?
---
Es ist $a-b=-\frac{xy}{n^2}$, weil sich beim Ausmultiplizieren von $b$ alles außer dem Glied $\frac{xy}{n^2}$ gegen $a$ weghebt.
---
Nach den Rechenregeln ist $\exp(x+y)-\exp(x)\exp(y)=\lim_{n\to\infty}(a^n-b^n)$, weil $a^n=z_n(x+y)$ und $b^n=z_n(x)\,z_n(y)$ ist.
---
Mit $a^n-b^n=(a-b)\sum_{k=1}^na^{n-k}\,b^{k-1}$ steht im Grenzwert $-\frac{xy}{n^2}\sum_{k=1}^na^{n-k}b^{k-1}$, weil man so den kleinen Faktor $a-b$ abspaltet.
---
Jeder der $n$ Summanden ist betragsmäßig höchstens $D:=\exp(|x|)\exp(|y|)$, weil $|a|,|b|\le c:=(1+\frac{|x|}n)(1+\frac{|y|}n)$ und $c^{\,n-1}\le z_n(|x|)\,z_n(|y|)$ gilt und $z_n(|x|)$ gegen $\exp(|x|)$ wächst.
---
Die Klammer ist damit betragsmäßig höchstens $\frac{|xy|}{n^2}\cdot n\,D=\frac{|xy|D}n$, eine Nullfolge, weil $D$ nicht von $n$ abhängt; also ist die Differenz null.
:::
:::karte formel Differenz zweier Potenzen
Welche Formel zerlegt $a^n-b^n$ in den Faktor $a-b$ und eine Summe, und welcher Spezialfall ist die geometrische Summe?
---
$a^n-b^n=(a-b)\sum_{k=1}^na^{n-k}\,b^{k-1}$ für $a,b\in\mathbb{R}$, $n\in\mathbb{N}$. Für $b=1$ ist das die geometrische Summe; Ausmultiplizieren gibt eine Teleskopsumme.
--- falsch
$a^n-b^n=(a-b)^n$ für $a,b\in\mathbb{R}$, $n\in\mathbb{N}$. Für $b=1$ ist das die geometrische Summe; Ausmultiplizieren mit dem binomischen Satz lässt nur diesen einen Term übrig.
--- falsch
$a^n-b^n=(a-b)\sum_{k=1}^na^{n-k}\,b^{k-1}$, aber nur für $a>b>0$. Für negative Zahlen fehlt die Teleskopsumme, weil sich die Vorzeichen nicht mehr wegheben.
--- falsch
$a^n-b^n=(a-b)\sum_{k=1}^n a^{k}\,b^{k}$ für $a,b\in\mathbb{R}$, $n\in\mathbb{N}$. Für $b=1$ ist das die geometrische Summe; jeder Summand ist ein Produkt gleich hoher Potenzen.
:::
:::karte zusammenhang Schreibweise als Potenz
Warum passt die Schreibweise $\mathrm{e}^x$ für $\exp(x)$, und wie ist sie für irrationale $x$ erklärt?
---
Für $x=\frac pq$ gibt die Funktionalgleichung $\bigl(\exp(x)\bigr)^q=\exp(p)=\mathrm{e}^p$, und wegen $\exp(x)>0$ folgt $\exp(\frac pq)=\sqrt[q]{\mathrm{e}^p}=\mathrm{e}^{p/q}$. Für irrationale $x$ definiert man $\mathrm{e}^x:=\exp(x)$.
--- falsch
Weil $\exp(x)=\mathrm{e}\cdot x$ für alle $x$ gilt, ist $\mathrm{e}^x$ nur eine Kurzschrift für dieses Produkt; für irrationale $x$ rechnet man ebenso mit dem Produkt aus $\mathrm{e}$ und $x$.
--- falsch
Für $x=\frac pq$ gibt die Funktionalgleichung $\exp(\frac pq)=\mathrm{e}^{p/q}$. Für irrationale $x$ ist $\mathrm{e}^x$ dagegen nicht erklärt, weil man keine Wurzel mit irrationalem Index ziehen kann.
--- falsch
Für natürliche $x$ gilt $\exp(x)=\mathrm{e}^x$, für rationale $x$ dagegen nicht, weil Wurzeln nicht zur Funktionalgleichung passen. Für irrationale $x$ definiert man $\mathrm{e}^x:=\exp(x)$.
:::
:::karte begriff kontinuierliche Verzinsung
Was versteht man unter kontinuierlicher Verzinsung, und welchen Betrag $E_k^{(\infty)}$ liefert sie nach $k$ Jahren?
---
Den Grenzfall $n\to\infty$ der Verzinsung in $n$ Raten pro Jahr: $E_k^{(\infty)}=K_0\,(\mathrm{e}^{p/100})^k$. Kein Betrag mit endlich vielen Raten erreicht ihn, denn $z_n(x)$ bleibt unter $\mathrm{e}^x$.
--- falsch
Den Grenzfall $n\to\infty$ der Verzinsung in $n$ Raten pro Jahr; der Betrag wächst dabei über jede Grenze, weil unendlich viele Zinstermine auch unendlich viel Zins bringen.
--- falsch
Die jährliche Verzinsung ohne Zinseszins: $E_k^{(\infty)}=K_0\,(1+\frac{p\,k}{100})$. Der Zins wird stetig auf das Anfangskapital gezahlt und verzinst sich nicht mit.
--- falsch
Den Grenzfall $n\to\infty$ der Verzinsung in $n$ Raten pro Jahr: $E_k^{(\infty)}=K_0\,\mathrm{e}^{k}$. Der Zinssatz $p$ fällt im Grenzfall heraus, weil die Raten beliebig klein werden.
:::
:::karte zusammenhang Grenzwert der Zinsfolge
Warum ist der Grenzwert von $(1+\frac1n)^n$ nicht 1, obwohl die Klammer gegen 1 geht?
---
Die Rechenregeln gelten nur für eine feste Zahl von Faktoren. Hier wächst die Zahl der Faktoren mit, während jeder gegen 1 geht; beide Effekte konkurrieren, der Grenzwert liegt zwischen 2 und 3.
--- falsch
Er ist doch 1: Nach der Produktregel geht ein Produkt aus Faktoren, die alle gegen 1 gehen, gegen $1\cdot1\cdots1=1$; die Werte über 2 entstehen nur durch Rundung beim Rechnen.
--- falsch
Weil die Folge unbeschränkt wächst: Jeder Faktor ist größer als 1, und ein Produkt aus immer mehr Faktoren über 1 übersteigt schließlich jede noch so große Schranke.
--- falsch
Weil die Klammer erst für sehr große $n$ nahe bei 1 liegt; vorher ist sie deutlich größer, und diese ersten Glieder der Folge bestimmen allein den Grenzwert, die späteren kaum noch.
:::
::::
