---
title: Stufe 6: Quotient und Wurzel
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
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

::::beispiel die Exponentialreihe
Für festes $x\ne0$ sei $a_n=\frac{x^n}{n!}$, $n\ge0$. Dann ist

$$\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\frac{|x|^{n+1}}{(n+1)!}\cdot\frac{n!}{|x|^n}=\frac{|x|}{n+1}\to0.$$

Also ist $\alpha=0$, die __Exponentialreihe__ $\sum_{n=0}^\infty\frac{x^n}{n!}$ ist für alle $x\in\mathbb{R}$ absolut konvergent (für $x=0$ bleibt nur das Glied 1). Der Mechanismus zeigt sich bei $x=3$ (Abb. [6](#abb-6)): Die Glieder steigen bis $a_2=a_3=4{,}5$, ab $n=5$ ist der Faktor $\frac3{n+1}\le\frac12$. Von da an bleibt die Folge unter $a_5\,(\frac12)^{n-5}$, und $S_{15}=20{,}0855$. Für $x=1$ ist $S_{10}=2{,}7182818$.

:::abbildung hm1/k6quotient 6
Die Glieder $3^n/n!$ auf logarithmischer Achse. Eine geometrische Folge ist dort eine Gerade, ihre Steigung ist $\log q$. Ab $n_0=5$ liegen die Glieder unter der Geraden mit $q=\frac12$: Das ist die Majorante aus dem Beweis.
:::
::::

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

⁠**So liest man das:** $\sqrt[n]{|a_n|}$ ist der mittlere Schrumpffaktor der ersten $n$ Schritte, denn $|a_n|=\bigl(\sqrt[n]{|a_n|}\bigr)^n$. Für $a_n=(\frac n{3n+1})^n$ ist die Wurzel $\frac n{3n+1}$, also $\alpha=\frac13$. Einzelne Ausreißer im Quotienten stören den Mittelwert nicht. **Grenzfall $\alpha=1$:** $\sqrt[n]{1/n}\to1$ und $\sqrt[n]{1/n^2}\to1$ nach [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html), die eine Reihe divergiert, die andere konvergiert.

:::beweis Direkt unter $q^n$
(i) Mit $\varepsilon:=\frac{1-\alpha}2$ und $q:=\alpha+\varepsilon<1$ gibt es $N_0$ mit $\sqrt[n]{|a_n|}<q$ für $n>N_0$, also $|a_n|<q^n$. Die geometrische Reihe ist eine konvergente Majorante.

(ii) Für $\alpha>1$ ist $\sqrt[n]{|a_n|}>1$ ab einem Index, also $|a_n|>1$. Die Glieder sind keine Nullfolge.
:::

::::beispiel
Für $a_n=\frac{3+2(-1)^n}{2^n}$ lauten die Glieder $\frac12;\ \frac54;\ \frac18;\ \frac5{16};\ \dots$ Der Quotient pendelt zwischen $\frac52$ und $\frac1{10}$ und hat keinen Grenzwert. Das Quotientenkriterium ist nicht anwendbar. Die Wurzel dagegen ist $\frac12\sqrt[n]{3+2(-1)^n}$ mit $1\le\sqrt[n]{3+2(-1)^n}\le\sqrt[n]5\to1$. Das Sandwich-Lemma gibt $\alpha=\frac12$, die Reihe ist absolut konvergent. Mit den Rechenregeln ist ihr Wert $3\cdot1+2\cdot(-\frac13)=\frac73$.
::::

⁠**Faustregel:** Bei Fakultäten kürzt der Quotient, bei Potenzen $(\dots)^n$ beseitigt die Wurzel den Exponenten.

:::zusatz Wenn der Grenzwert nicht existiert
Mit den Hüllen aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) setzt man $\limsup c_n:=\lim_{n\to\infty}\sup\{c_m:m\ge n\}$ und entsprechend $\liminf c_n$ mit dem Infimum. Für absolute Konvergenz genügt $\limsup\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ beziehungsweise $\limsup\sqrt[n]{|a_n|}<1$, die Beweise bleiben gleich. Für Divergenz genügt $\liminf\bigl|\frac{a_{n+1}}{a_n}\bigr|>1$ beziehungsweise $\limsup\sqrt[n]{|a_n|}>1$: Im zweiten Fall ist $|a_n|>1$ für unendlich viele $n$, das reicht schon gegen eine Nullfolge.
:::

:::aufgabe Aufgabe 7 ★★ Quotient oder Wurzel
<span class="anker" id="aufg-7"></span>

Bestimme $\alpha$ und entscheide. Wo $\alpha=1$ ist, nimm einen Vergleich. (a) $\sum\frac{n^3}{3^n}$, (b) $\sum\frac{5^n}{n!}$, (c) $\sum\bigl(\frac n{2n+1}\bigr)^n$, (d) $\sum\frac{2^n}{n^2}$, (e) $\sum\frac1{n^2+1}$.

:::loesung
(a) Quotient $\frac13(\frac{n+1}n)^3\to\frac13$: absolut konvergent. (b) $\frac5{n+1}\to0$: absolut konvergent. (c) Wurzel $\frac n{2n+1}\to\frac12$: absolut konvergent. (d) Quotient $\frac{2n^2}{(n+1)^2}\to2$: divergent. (e) Quotient $\frac{n^2+1}{(n+1)^2+1}\to1$, keine Aussage. Vergleich: $\frac1{n^2+1}\le\frac1{n^2}$, absolut konvergent.
:::
:::

::::formelsammlung
**Quotientenkriterium**

$$\alpha:=\lim_{n\to\infty}\Bigl|\frac{a_{n+1}}{a_n}\Bigr|$$

Für $a_n\ne0$ ab $n_0$, falls der Grenzwert existiert: $\alpha<1$ absolut konvergent, $\alpha>1$ divergent, $\alpha=1$ keine Aussage (etwa $\frac1n$ und $\frac1{n^2}$). Quotienten unter 1 für alle $n$ genügen nicht.

**Exponentialreihe**

$$\sum_{n=0}^\infty\frac{x^n}{n!},\qquad\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\frac{|x|}{n+1}\to0$$

Für alle $x\in\mathbb{R}$ absolut konvergent: Für $x\ne0$ ist $\alpha=0$, für $x=0$ bleibt nur das Glied 1.

**Wurzelkriterium**

$$\alpha:=\lim_{n\to\infty}\sqrt[n]{|a_n|}$$

Falls der Grenzwert existiert: $\alpha<1$ absolut konvergent, $\alpha>1$ divergent, $\alpha=1$ keine Aussage. $\sqrt[n]{|a_n|}$ ist der mittlere Schrumpffaktor, denn $|a_n|=\bigl(\sqrt[n]{|a_n|}\bigr)^n$.

**Limes superior und Limes inferior**

$$\limsup c_n:=\lim_{n\to\infty}\sup\{c_m:m\ge n\}$$

$\liminf c_n$ entsprechend mit dem Infimum. Absolut konvergent schon bei $\limsup\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ oder $\limsup\sqrt[n]{|a_n|}<1$; divergent bei $\liminf\bigl|\frac{a_{n+1}}{a_n}\bigr|>1$ oder $\limsup\sqrt[n]{|a_n|}>1$.
::::

::::lernkarten
:::karte formel Quotientenkriterium
Was sagt das Quotientenkriterium über eine Reihe $\sum a_n$ mit $a_n\ne0$ für alle $n\ge n_0$, wenn der Grenzwert $\alpha:=\lim_{n\to\infty}\bigl|\frac{a_{n+1}}{a_n}\bigr|$ existiert?
---
Für $\alpha<1$ ist die Reihe absolut konvergent, für $\alpha>1$ ist sie divergent. Für $\alpha=1$ erhält man keine Aussage.
--- falsch
Für $\alpha<1$ ist die Reihe absolut konvergent, für $\alpha\ge1$ ist sie divergent, weil die Glieder dann am Ende nicht mehr schrumpfen.
--- falsch
Für $\alpha<1$ ist die Reihe konvergent, aber nicht unbedingt absolut, für $\alpha>1$ ist sie divergent. Für $\alpha=1$ erhält man keine Aussage.
--- falsch
Für $\alpha\le1$ ist die Reihe absolut konvergent, für $\alpha>1$ ist sie divergent, weil die Glieder bei $\alpha=1$ wenigstens nicht wachsen.
:::
:::karte zusammenhang Grenzwert unter eins nötig
Warum genügt es für das Quotientenkriterium nicht, dass $\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ für alle $n$ gilt?
---
Weil die Quotienten trotzdem gegen 1 streben können: Bei $a_n=\frac1n$ ist jeder Quotient kleiner als 1, die Reihe divergiert. Erst ein Grenzwert $\alpha<1$ lässt Platz für ein festes $q<1$.
--- falsch
Es genügt doch: Ist jeder Quotient kleiner als 1, fallen die Beträge der Glieder Schritt für Schritt, und eine Reihe mit fallenden Beträgen konvergiert immer, wie die geometrische Reihe.
--- falsch
Weil die Bedingung nur ab einem Index $n_0$ gelten muss; für alle $n$ verlangt, ist sie zu streng und schließt konvergente Reihen aus.
--- falsch
Weil der Quotient nur Nachbarn vergleicht; man muss zusätzlich zeigen, dass die Glieder positiv sind, dann genügt $\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ für alle $n$.
:::
:::karte zusammenhang keine Aussage bei eins
Warum liefern Quotienten- und Wurzelkriterium für $\alpha=1$ keine Aussage?
---
Weil zwischen $\alpha$ und 1 kein festes $q<1$ mehr passt, der Vergleich mit der geometrischen Reihe hat keinen Halt. Tatsächlich haben $\frac1n$ und $\frac1{n^2}$ beide $\alpha=1$; die erste Reihe divergiert, die zweite konvergiert.
--- falsch
Weil für $\alpha=1$ alle Glieder gleich groß sind; die Reihe divergiert dann zwar, aber die Kriterien sind nur für schrumpfende Glieder formuliert und schweigen deshalb.
--- falsch
Weil die Rechnung bei $\alpha=1$ zu ungenau wird; mit genügend Nachkommastellen von $\alpha$ ließe sich die Frage jedes Mal entscheiden.
--- falsch
Weil $\alpha=1$ nur bei alternierenden Reihen vorkommt, und für sie ist allein das Leibniz-Kriterium zuständig, nicht der Vergleich.
:::
:::karte herleitung Vergleich mit der geometrischen Reihe
Wie zeigt man, dass die Reihe $\sum a_n$ im Quotientenkriterium für $\alpha<1$ absolut konvergiert?
---
Man setzt $\varepsilon:=\frac{1-\alpha}2>0$ und $q:=\alpha+\varepsilon<1$, weil so ein festes $q$ zwischen $\alpha$ und 1 liegt.
---
Es gibt $\tilde N_0\ge n_0$ mit $\bigl|\frac{a_{n+1}}{a_n}\bigr|\le q$ für alle $n\ge\tilde N_0$, weil die Quotienten gegen $\alpha<q$ streben.
---
Schrittweise folgt $|a_n|\le q^{n-\tilde N_0}|a_{\tilde N_0}|$ für alle $n\ge\tilde N_0$, weil jeder Schritt höchstens den Faktor $q$ bringt.
---
Die rechte Seite ist $|a_{\tilde N_0}|$ mal einer geometrischen Reihe mit $q<1$, also eine konvergente Majorante; das Vergleichskriterium ergibt die absolute Konvergenz, weil es nur ab einem Index gelten muss.
:::
:::karte zusammenhang wachsende Glieder
Warum divergiert eine Reihe, wenn im Quotientenkriterium $\alpha>1$ ist?
---
Weil dann ab einem Index $\tilde N_0$ die Abschätzung $\bigl|\frac{a_{n+1}}{a_n}\bigr|\ge\beta>1$ gilt, also $|a_n|\ge\beta^{n-\tilde N_0}|a_{\tilde N_0}|\to\infty$. Die Glieder bilden keine Nullfolge.
--- falsch
Weil dann alle Glieder größer als 1 sind, schon vom ersten an; eine Reihe mit lauter Gliedern über 1 verletzt die notwendige Bedingung für Konvergenz.
--- falsch
Weil die Teilsummen dann pendeln: Ein Quotient über 1 bedeutet, dass die Vorzeichen wechseln, und die Teilsummen springen hin und her.
--- falsch
Weil die Reihe dann die harmonische Reihe als divergente Minorante hat; die Glieder selbst können dabei durchaus eine Nullfolge bilden.
:::
:::karte begriff Exponentialreihe
Was ist die Exponentialreihe, und für welche $x\in\mathbb{R}$ ist sie konvergent?
---
Die Reihe $\sum_{n=0}^\infty\frac{x^n}{n!}$. Für $x\ne0$ strebt ihr Quotient $\frac{|x|}{n+1}$ gegen 0, also ist $\alpha=0$; sie ist für alle $x\in\mathbb{R}$ absolut konvergent.
--- falsch
Die Reihe $\sum_{n=0}^\infty x^n$. Ihr Quotient ist $|x|$, also ist $\alpha=|x|$, und sie ist nur für $|x|<1$ absolut konvergent.
--- falsch
Die Reihe $\sum_{n=0}^\infty\frac{x^n}{n!}$. Ihr Quotient $\frac{|x|}{n+1}$ strebt gegen 0, aber für $|x|>1$ wachsen die Glieder, also konvergiert sie nur für $|x|\le1$.
--- falsch
Die Reihe $\sum_{n=0}^\infty\frac{n!}{x^n}$. Ihr Quotient $\frac{n+1}{|x|}$ wird für große $|x|$ klein, also ist sie für alle $x\ne0$ absolut konvergent.
:::
:::karte zusammenhang Exponentialreihe bei drei
Warum konvergiert die Exponentialreihe auch für $x=3$, obwohl ihre Glieder $\frac{3^n}{n!}$ anfangs steigen?
---
Weil der Faktor $\frac3{n+1}$ ab $n=5$ höchstens $\frac12$ ist: Von da an bleibt die Folge unter $a_5\,(\frac12)^{n-5}$, einer geometrischen Majorante. Für die Konvergenz zählt nur das Verhalten ab einem Index.
--- falsch
Weil die Glieder in Wahrheit von Anfang an fallen: Der Faktor $\frac3{n+1}$ ist schon für $n=0$ kleiner als 1, das Steigen ist eine Täuschung der Zeichnung.
--- falsch
Weil die Glieder bis $a_2=a_3=4{,}5$ steigen und danach konstant bleiben; die Teilsummen schachteln sich dann wie bei Leibniz ein.
--- falsch
Weil die Teilsummen sehr schnell den Wert $S_{15}=20{,}0855$ erreichen und danach nicht mehr wachsen; die Glieder ab $n=16$ sind alle null.
:::
:::karte formel Wurzelkriterium
Was sagt das Wurzelkriterium über eine Reihe $\sum a_n$, wenn der Grenzwert $\alpha:=\lim_{n\to\infty}\sqrt[n]{|a_n|}$ existiert?
---
Für $\alpha<1$ ist die Reihe absolut konvergent, für $\alpha>1$ ist sie divergent. Für $\alpha=1$ erhält man wieder keine Aussage.
--- falsch
Für $\alpha<1$ ist die Reihe absolut konvergent, für $\alpha\ge1$ divergent, weil $|a_n|$ bei $\alpha=1$ gegen 1 strebt und keine Nullfolge ist.
--- falsch
Für $\alpha<1$ ist die Reihe konvergent, aber nur bei positiven Gliedern auch absolut; für $\alpha>1$ ist sie divergent.
--- falsch
Für $\alpha<1$ ist sie absolut konvergent, für $\alpha>1$ divergent; anders als beim Quotienten gibt $\alpha=1$ hier Konvergenz.
:::
:::karte zusammenhang mittlerer Schrumpffaktor
Warum hilft das Wurzelkriterium noch, wenn der Quotient benachbarter Glieder pendelt und keinen Grenzwert hat?
---
Weil $\sqrt[n]{|a_n|}$ der mittlere Schrumpffaktor der ersten $n$ Schritte ist, denn $|a_n|=\bigl(\sqrt[n]{|a_n|}\bigr)^n$. Einzelne Ausreißer im Quotienten stören diesen Mittelwert nicht; bei $a_n=\frac{3+2(-1)^n}{2^n}$ strebt die Wurzel gegen $\frac12$.
--- falsch
Weil die Wurzel stets den kleineren der beiden Werte liefert, zwischen denen der Quotient pendelt; bei $a_n=\frac{3+2(-1)^n}{2^n}$ also $\frac1{10}$, und die Reihe ist absolut konvergent.
--- falsch
Es hilft nicht: Hat der Quotient keinen Grenzwert, hat auch $\sqrt[n]{|a_n|}$ keinen, weil beide Größen dieselbe Information über die Glieder enthalten und gleich reagieren.
--- falsch
Weil die Wurzel das arithmetische Mittel der Quotienten bildet; bei $a_n=\frac{3+2(-1)^n}{2^n}$ also $\frac12\bigl(\frac52+\frac1{10}\bigr)=1{,}3$, und die Reihe divergiert deshalb.
:::
:::karte zusammenhang Faustregel
Wann wählt man eher das Quotientenkriterium und wann eher das Wurzelkriterium?
---
Bei Fakultäten kürzt der Quotient, etwa zu $\frac{|x|}{n+1}$ bei $\frac{x^n}{n!}$. Bei Potenzen $(\dots)^n$ beseitigt die Wurzel den Exponenten, etwa zu $\frac n{3n+1}$ bei $(\frac n{3n+1})^n$.
--- falsch
Bei Fakultäten nimmt man die Wurzel, weil sich $\sqrt[n]{n!}$ kürzen lässt; bei Potenzen $(\dots)^n$ den Quotienten, weil sich der Exponent dann aufhebt.
--- falsch
Den Quotienten nur bei positiven Gliedern, weil er bei Vorzeichenwechseln negativ wird; die Wurzel bei allen Reihen mit wechselnden Vorzeichen.
--- falsch
Den Quotienten bei Reihen, deren Glieder fallen, die Wurzel bei Reihen, deren Glieder steigen; bei Fakultäten und Potenzen helfen beide gleich gut.
:::
:::karte formel Wenn der Grenzwert nicht existiert
Welche Bedingungen mit Limes superior und Limes inferior genügen für Quotienten- und Wurzelkriterium, wenn der Grenzwert $\alpha$ nicht existiert?
---
Für absolute Konvergenz genügt $\limsup\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ beziehungsweise $\limsup\sqrt[n]{|a_n|}<1$. Für Divergenz genügt $\liminf\bigl|\frac{a_{n+1}}{a_n}\bigr|>1$ beziehungsweise $\limsup\sqrt[n]{|a_n|}>1$.
--- falsch
Für absolute Konvergenz genügt $\liminf\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ beziehungsweise $\liminf\sqrt[n]{|a_n|}<1$. Für Divergenz genügt bei beiden Größen ein $\limsup$ über 1.
--- falsch
Für absolute Konvergenz genügt $\limsup\bigl|\frac{a_{n+1}}{a_n}\bigr|<1$ beziehungsweise $\limsup\sqrt[n]{|a_n|}<1$. Für Divergenz genügt $\limsup\bigl|\frac{a_{n+1}}{a_n}\bigr|>1$, bei der Wurzel ebenso.
--- falsch
Ohne Grenzwert gibt es keine Aussage, auch nicht mit Limes superior oder inferior. Dann bleibt nur ein Vergleich, der eine Majorante oder Minorante von Hand findet.
:::
::::
