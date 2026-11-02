---
title: Stufe 6: Quotient und Wurzel
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Unendliche Reihen
order: 1260800
summary: Eine Majorante muss man erst finden.
tags: Exponentialreihe
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Eine Majorante muss man erst finden. Diese Stufe gibt zwei Tests, die sie selbst finden: Sie prüfen, ob die Glieder schließlich wie eine geometrische Folge fallen, und vergleichen mit ihr.
:::

**Die Idee.** Bei der geometrischen Reihe ist das Verhältnis $|a_{n+1}/a_n|$ genau $q$, die Wurzel $\sqrt[n]{|a_n|}$ ebenfalls. Misst man beide Größen bei einer beliebigen Reihe und findet im Grenzwert ein $\alpha<1$, passt zwischen $\alpha$ und 1 ein festes $q$. Ab einem Index liegt die Reihe dann unter einer geometrischen Reihe mit diesem $q$. Bei $\alpha>1$ wachsen die Glieder. Bei $\alpha=1$ passt kein $q$ dazwischen, der Vergleich hat keinen Halt: Deshalb schweigen beide Tests dort.

:::satz Satz 6.1 (Quotientenkriterium)
<span class="anker" id="satz-6-1"></span>

Sei $\sum_{n=1}^\infty a_n$ eine Reihe mit $a_n\ne0$ für alle $n\ge n_0$. Konvergiert die Folge $\bigl\{\bigl|\frac{a_{n+1}}{a_n}\bigr|\bigr\}_{n\ge n_0}$ mit $\alpha:=\lim_{n\to\infty}\bigl|\frac{a_{n+1}}{a_n}\bigr|$, dann gilt:

<ol class="rm">

<li>

$\sum_{n=1}^\infty a_n$ ist absolut konvergent, wenn $\alpha<1$ ist.

</li>

<li>

$\sum_{n=1}^\infty a_n$ ist divergent, wenn $\alpha>1$ ist.

</li>

</ol>

Für $\alpha=1$ erhält man keine Aussage.
:::

⁠**So liest man das:** $\alpha\ge0$ ist der Faktor, um den die Glieder am Ende von Schritt zu Schritt schrumpfen. Für $a_n=\frac n{2^n}$ ist der Quotient $\frac{n+1}{2n}$, also $\alpha=\frac12$. Die Bedingung $a_n\ne0$ sorgt dafür, dass der Quotient existiert. **Grenzfall $\alpha=1$:** $a_n=\frac1n$ und $a_n=\frac1{n^2}$ haben beide $\alpha=1$, die erste Reihe divergiert, die zweite konvergiert. **Voraussetzung nötig:** $\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ für alle $n$ genügt nicht, wie $\frac1n$ zeigt. Der Grenzwert $\alpha$ selbst muss unter 1 liegen.

:::beweis Vergleich mit der geometrischen Reihe
(i) Sei $\alpha<1$ und $\varepsilon:=\frac{1-\alpha}2>0$. Dann ist $q:=\alpha+\varepsilon<1$. Weil die Quotienten gegen $\alpha$ streben, gibt es $\tilde N_0\ge n_0$ mit $\bigl|\frac{a_{n+1}}{a_n}\bigr|\le q$ für alle $n\ge\tilde N_0$. Schrittweise folgt

$$|a_n|\le q\,|a_{n-1}|\le q^2|a_{n-2}|\le\dots\le q^{n-\tilde N_0}|a_{\tilde N_0}|\qquad\forall\,n\ge\tilde N_0.$$

Die rechte Seite ist $|a_{\tilde N_0}|$ mal einer geometrischen Reihe mit $q<1$, also eine konvergente Majorante. Das Vergleichskriterium ergibt die absolute Konvergenz.

(ii) Sei $\alpha>1$. Wähle $\varepsilon>0$ so klein, dass $\beta:=\alpha-\varepsilon>1$ ist. Für $n\ge\tilde N_0$ gilt $\bigl|\frac{a_{n+1}}{a_n}\bigr|\ge\beta$, also $|a_n|\ge\beta^{n-\tilde N_0}|a_{\tilde N_0}|\to\infty$, denn $a_{\tilde N_0}\ne0$. Die Glieder sind keine Nullfolge, die Reihe divergiert.
:::

**Beispiel: die Exponentialreihe.** Für festes $x\ne0$ sei $a_n=\frac{x^n}{n!}$, $n\ge0$. Dann ist

$$\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\frac{|x|^{n+1}}{(n+1)!}\cdot\frac{n!}{|x|^n}=\frac{|x|}{n+1}\to0.$$

Also ist $\alpha=0$, die __Exponentialreihe__ $\sum_{n=0}^\infty\frac{x^n}{n!}$ ist für alle $x\in\mathbb{R}$ absolut konvergent (für $x=0$ bleibt nur das Glied 1). Der Mechanismus zeigt sich bei $x=3$ (Abb. [6](#abb-6)): Die Glieder steigen bis $a_2=a_3=4{,}5$, ab $n=5$ ist der Faktor $\frac3{n+1}\le\frac12$. Von da an bleibt die Folge unter $a_5\,(\frac12)^{n-5}$, und $S_{15}=20{,}0855$. Für $x=1$ ist $S_{10}=2{,}7182818$.

:::abbildung hm1/k6quotient 6
Die Glieder $3^n/n!$ auf logarithmischer Achse. Eine geometrische Folge ist dort eine Gerade, ihre Steigung ist $\log q$. Ab $n_0=5$ liegen die Glieder unter der Geraden mit $q=\frac12$: Das ist die Majorante aus dem Beweis.
:::

:::satz Satz 6.2 (Wurzelkriterium)
<span class="anker" id="satz-6-2"></span>

Sei $\sum_{n=1}^\infty a_n$ eine Reihe, für die $\alpha:=\lim_{n\to\infty}\sqrt[n]{|a_n|}$ existiert. Dann gilt:

<ol class="rm">

<li>

$\sum_{n=1}^\infty a_n$ ist absolut konvergent, falls $\alpha<1$.

</li>

<li>

$\sum_{n=1}^\infty a_n$ ist divergent, falls $\alpha>1$.

</li>

</ol>

Für $\alpha=1$ erhält man wieder keine Aussage.
:::

⁠**So liest man das:** $\sqrt[n]{|a_n|}$ ist der mittlere Schrumpffaktor der ersten $n$ Schritte, denn $|a_n|=\bigl(\sqrt[n]{|a_n|}\bigr)^n$. Für $a_n=(\frac n{3n+1})^n$ ist die Wurzel $\frac n{3n+1}$, also $\alpha=\frac13$. Einzelne Ausreißer im Quotienten stören den Mittelwert nicht. **Grenzfall $\alpha=1$:** $\sqrt[n]{1/n}\to1$ und $\sqrt[n]{1/n^2}\to1$ nach [Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html), die eine Reihe divergiert, die andere konvergiert.

:::beweis Direkt unter $q^n$
(i) Mit $\varepsilon:=\frac{1-\alpha}2$ und $q:=\alpha+\varepsilon<1$ gibt es $N_0$ mit $\sqrt[n]{|a_n|}<q$ für $n>N_0$, also $|a_n|<q^n$. Die geometrische Reihe ist eine konvergente Majorante.

(ii) Für $\alpha>1$ ist $\sqrt[n]{|a_n|}>1$ ab einem Index, also $|a_n|>1$. Die Glieder sind keine Nullfolge.
:::

**Beispiel.** Für $a_n=\frac{3+2(-1)^n}{2^n}$ lauten die Glieder $\frac12;\ \frac54;\ \frac18;\ \frac5{16};\ \dots$ Der Quotient pendelt zwischen $\frac52$ und $\frac1{10}$ und hat keinen Grenzwert. Das Quotientenkriterium ist nicht anwendbar. Die Wurzel dagegen ist $\frac12\sqrt[n]{3+2(-1)^n}$ mit $1\le\sqrt[n]{3+2(-1)^n}\le\sqrt[n]5\to1$. Das Sandwich-Lemma gibt $\alpha=\frac12$, die Reihe ist absolut konvergent. Mit den Rechenregeln ist ihr Wert $3\cdot1+2\cdot(-\frac13)=\frac73$. **Faustregel:** Bei Fakultäten kürzt der Quotient, bei Potenzen $(\dots)^n$ beseitigt die Wurzel den Exponenten.

:::zusatz Wenn der Grenzwert nicht existiert
Mit den Hüllen aus [Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) setzt man $\limsup c_n:=\lim_{n\to\infty}\sup\{c_m:m\ge n\}$ und entsprechend $\liminf c_n$ mit dem Infimum. Für absolute Konvergenz genügt $\limsup\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ beziehungsweise $\limsup\sqrt[n]{|a_n|}<1$, die Beweise bleiben gleich. Für Divergenz genügt $\liminf\bigl|\frac{a_{n+1}}{a_n}\bigr|>1$ beziehungsweise $\limsup\sqrt[n]{|a_n|}>1$: Im zweiten Fall ist $|a_n|>1$ für unendlich viele $n$, das reicht schon gegen eine Nullfolge.
:::

:::aufgabe Aufgabe 7 ★★ Quotient oder Wurzel
<span class="anker" id="aufg-7"></span>

Bestimme $\alpha$ und entscheide. Wo $\alpha=1$ ist, nimm einen Vergleich. (a) $\sum\frac{n^3}{3^n}$, (b) $\sum\frac{5^n}{n!}$, (c) $\sum\bigl(\frac n{2n+1}\bigr)^n$, (d) $\sum\frac{2^n}{n^2}$, (e) $\sum\frac1{n^2+1}$.

:::loesung
(a) Quotient $\frac13(\frac{n+1}n)^3\to\frac13$: absolut konvergent. (b) $\frac5{n+1}\to0$: absolut konvergent. (c) Wurzel $\frac n{2n+1}\to\frac12$: absolut konvergent. (d) Quotient $\frac{2n^2}{(n+1)^2}\to2$: divergent. (e) Quotient $\frac{n^2+1}{(n+1)^2+1}\to1$, keine Aussage. Vergleich: $\frac1{n^2+1}\le\frac1{n^2}$, absolut konvergent.
:::
:::
