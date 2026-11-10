---
title: Stufe 5: Die Exponentialreihe, reell und komplex
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
adresse: elektrotechnik/1-semester/hohere-mathematik-1/potenzreihen-und-eulersche-formel
knoten: Kapitel 7: Potenzreihen und Eulersche Formel
order: 1270700
summary: Aus Kapitel 5 ist exp der Grenzwert einer Folge.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Aus [Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html) ist $\exp$ der Grenzwert einer Folge. Diese Stufe macht daraus eine Potenzreihe, setzt komplexe Zahlen ein und beweist die Funktionalgleichung.
:::

**Die Idee.** Multipliziert man $(1+\frac xn)^n$ mit der binomischen Formel aus, ist das $k$-te Glied $\frac{x^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}$. Der zweite Bruch geht für festes $k$ gegen 1, für $n=1000$ und $k=2;3;4$ ist er $0{,}999;\ 0{,}997;\ 0{,}994$. Im Grenzwert bleibt $\sum x^k/k!$. Die Reihe ist der schnellere Weg zur selben Zahl (Abb. [5](#abb-5)) und enthält nur Rechenschritte, die auch in $\mathbb{C}$ erlaubt sind.

:::abbildung hm1/k7zweiwege 5
Zwei Wege zu $\mathrm{e}$. Die Teilsummen $s_k=\sum_{j=0}^k\frac1{j!}$ (blau) irren bei $k=8$ nur noch um $3\cdot10^{-6}$. Die Folge $(1+\frac1k)^k$ (orange) irrt bei $k=1000$ noch um $1{,}4\cdot10^{-3}$.
:::

:::satz Satz 5.1 (Exponentialreihe)
<span class="anker" id="satz-5-1"></span>

Die Potenzreihe $\sum_{k=0}^\infty\frac{x^k}{k!}$ hat den Konvergenzradius $R=\infty$, und für alle $x\in\mathbb{R}$ gilt

<span class="anker" id="gl-5-1"></span>
$$\exp(x)=\lim_{n\to\infty}\Bigl(1+\frac xn\Bigr)^n=\sum_{k=0}^\infty\frac{x^k}{k!}. \tag{5.1}$$
:::

:::beweis Abstand von Folge und Teilsumme
Radius: $|a_{k+1}/a_k|=\frac1{k+1}\to0$. Sei $S(x)$ der Wert der Reihe. Es genügt, $A_n:=\bigl|\sum_{k=0}^n\frac{x^k}{k!}-(1+\frac xn)^n\bigr|\to0$ zu zeigen. Mit [(4.3)](reihen-multiplizieren.html#gl-4-3) ist

$$A_n=\Bigl|\sum_{k=0}^n\frac{x^k}{k!}\Bigl(1-\frac{n!}{(n-k)!\,n^k}\Bigr)\Bigr|.$$

Für $k=0$ und $k=1$ ist die Klammer null. Für $k\ge2$ ist $\frac{n!}{(n-k)!\,n^k}=\prod_{\ell=1}^{k-1}(1-\frac\ell n)$, denn der Faktor $\ell=0$ ist 1. Für $u,v\in[0,1]$ gilt $(1-u)(1-v)=1-u-v+uv\ge1-u-v$. Mit Induktion ergibt das

$$\prod_{\ell=1}^{k-1}\Bigl(1-\frac\ell n\Bigr)\ge1-\frac1n\sum_{\ell=1}^{k-1}\ell=1-\frac{k(k-1)}{2n}.$$

Das Produkt ist außerdem höchstens 1. Also liegt die Klammer zwischen 0 und $\frac{k(k-1)}{2n}$, und mit $\frac{k(k-1)}{k!}=\frac1{(k-2)!}$ folgt

$$A_n\le\sum_{k=2}^n\frac{|x|^k}{k!}\cdot\frac{k(k-1)}{2n}=\frac{x^2}{2n}\sum_{k=2}^n\frac{|x|^{k-2}}{(k-2)!}\le\frac{x^2}{2n}\,S(|x|)\to0.$$
:::

**Der Schritt zu den komplexen Zahlen.** $a_n\to a$ bedeutet in $\mathbb{C}$: $|a_n-a|\to0$, und $|a_n-a|$ ist reell. Wegen $\max\{|\operatorname{Re} w|,|\operatorname{Im} w|\}\le|w|\le|\operatorname{Re} w|+|\operatorname{Im} w|$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)) konvergiert eine komplexe Folge genau dann, wenn Real- und Imaginärteil konvergieren. Damit erbt $\mathbb{C}$ die Vollständigkeit von $\mathbb{R}$, und aus absoluter Konvergenz folgt Konvergenz. Die Sätze der Stufen [1](der-konvergenzkreis.html#stufe-1) und [2](den-radius-ausrechnen.html#stufe-2) rechnen nur mit Beträgen. Sie gelten wörtlich für $z\in\mathbb{C}$, und der Konvergenzbereich ist eine Kreisscheibe $|z|<R$.

:::definition Definition 5.2 (Komplexe Exponentialfunktion)
<span class="anker" id="satz-5-2"></span>

Die Funktion $\exp:\mathbb{C}\to\mathbb{C}$, $z\mapsto\sum_{n=0}^\infty\frac{z^n}{n!}$ heißt komplexe Exponentialfunktion, man schreibt auch $\mathrm{e}^z$. Wegen $R=\infty$ ist sie für alle $z\in\mathbb{C}$ absolut konvergent.
:::

:::satz Satz 5.3 (Eigenschaften von $\exp$)
<span class="anker" id="satz-5-3"></span>

<ol class="al">

<li>

$\exp(z_1+z_2)=\exp(z_1)\exp(z_2)$ für alle $z_1,z_2\in\mathbb{C}$ (Funktionalgleichung),

</li>

<li>

$|\exp(\mathrm{i}\varphi)|=1$ für alle $\varphi\in\mathbb{R}$,

</li>

<li>

$\overline{\exp(\mathrm{i}\varphi)}=\exp(-\mathrm{i}\varphi)$ für alle $\varphi\in\mathbb{R}$.

</li>

</ol>
:::

⁠**So liest man das:** (a) macht aus einer Summe ein Produkt, auch für komplexe Zahlen. (b) sagt: Rein imaginäre Argumente führen auf den Einheitskreis. **Gültigkeit:** In (b) und (c) muss $\varphi$ reell sein. Für $\varphi=\mathrm{i}$ ist $|\exp(\mathrm{i}\cdot\mathrm{i})|=\mathrm{e}^{-1}\approx0{,}368$.

:::beweis Cauchy-Produkt plus Binomialformel
(a) Beide Reihen sind absolut konvergent. Satz [4.2](reihen-multiplizieren.html#satz-4-2) für $x=1$ mit $a_n=z_1^n/n!$ und $b_m=z_2^m/m!$ gibt

$$c_k=\sum_{\ell=0}^k\frac{z_1^\ell}{\ell!}\cdot\frac{z_2^{k-\ell}}{(k-\ell)!}=\frac1{k!}\sum_{\ell=0}^k\binom k\ell z_1^\ell z_2^{k-\ell}=\frac{(z_1+z_2)^k}{k!}.$$

Also ist $\exp(z_1)\exp(z_2)=\sum_kc_k=\exp(z_1+z_2)$. Hier zeigt sich der Mechanismus: Die Fakultäten der Reihe sind genau die, die der Binomialkoeffizient braucht.

(c) Konjugieren darf in Summen und Produkte hinein ([Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)) und wegen $|\overline w|=|w|$ auch in Grenzwerte. Also ist $\overline{\sum(\mathrm{i}\varphi)^n/n!}=\sum(\overline{\mathrm{i}\varphi})^n/n!=\sum(-\mathrm{i}\varphi)^n/n!$, denn $\overline{\mathrm{i}}=-\mathrm{i}$ und $\overline\varphi=\varphi$.

(b) Mit $|w|^2=w\overline w$, (c) und (a): $|\exp(\mathrm{i}\varphi)|^2=\exp(\mathrm{i}\varphi)\exp(-\mathrm{i}\varphi)=\exp(0)=1$.
:::

::::beispiel
$\exp(\mathrm{i})=1+\mathrm{i}-\frac12-\frac{\mathrm{i}}6+\frac1{24}+\frac{\mathrm{i}}{120}-\dots$ Bis $n=5$ ist das $0{,}5417+0{,}8417\,\mathrm{i}$, bis $n=7$ schon $0{,}5403+0{,}8415\,\mathrm{i}$, mit dem Betrag 1. Mit (a) ist $\exp(1+\mathrm{i})=\mathrm{e}\cdot\exp(\mathrm{i})\approx1{,}4687+2{,}2874\,\mathrm{i}$.
::::

⁠**Grenzfall:** $z_2=-z_1$ gibt $\exp(z)\exp(-z)=\exp(0)=1$. Also ist $\exp(z)$ nie null.

:::frage Was bedeutet „$\mathrm{e}$ hoch $\mathrm{i}$“? Man kann doch nicht $\mathrm{i}$-mal mit sich selbst multiplizieren.
Richtig, als wiederholte Multiplikation hat das keinen Sinn. $\mathrm{e}^z$ ist eine Schreibweise für die Reihe $\exp(z)$. Sie passt, weil die Funktionalgleichung die Potenzregel $\mathrm{e}^{z+w}=\mathrm{e}^z\mathrm{e}^w$ fortsetzt.
:::

:::aufgabe Aufgabe 5 ★★ Exponentialfunktion rechnen
<span class="anker" id="aufg-5"></span>

(a) Berechne $s_6=\sum_{k=0}^6\frac{2^k}{k!}$ als Bruch und vergleiche mit $\mathrm{e}^2\approx7{,}38906$ und mit $(1+\frac2{100})^{100}$. Welche Näherung ist besser? (b) Zeige $\exp(-z)=1/\exp(z)$ für alle $z\in\mathbb{C}$. (c) Zeige $\overline{\exp(z)}=\exp(\overline z)$ für alle $z\in\mathbb{C}$.

:::loesung
(a) $s_6=1+2+2+\frac43+\frac23+\frac4{15}+\frac4{45}=\frac{331}{45}=7{,}3556$, Fehler $0{,}034$. $(1{,}02)^{100}=7{,}2446$, Fehler $0{,}144$. Sieben Glieder schlagen hundert Faktoren. (b) Nach der Funktionalgleichung ist $\exp(z)\exp(-z)=\exp(0)=1$. Durch $\exp(z)\ne0$ teilen. (c) Konjugieren darf in Summen, Produkte und Grenzwerte hinein: $\overline{\sum z^n/n!}=\sum\overline z^{\,n}/n!=\exp(\overline z)$.
:::
:::
