---
title: Die größte Entropie
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
knoten: Grundlagen 5: Statistik und Information
nachschlagen: ja
order: 15251100
summary: Welche Verteilung ist am wenigsten vorhersagbar, wenn über sie nur wenig feststeht?
tags: differentielle Entropie
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Welche Verteilung ist am wenigsten vorhersagbar, wenn über sie nur wenig feststeht? Dieser Abschnitt beantwortet die Frage zweimal mit der Gibbs-Ungleichung. Ohne weitere Angaben ist es die Gleichverteilung, bei vorgegebener Varianz die Normalverteilung. Das ist der zweite Grund, warum die Normalverteilung so oft vorkommt.
:::

### Die Gleichverteilung hat die größte Entropie

<span class="anker" id="stufe-10-1"></span>

Eine faire Münze ist unvorhersagbarer als eine verbogene, ein fairer Würfel unvorhersagbarer als ein gezinkter. Allgemein gilt:

:::satz Satz 10.1 (Größte Entropie bei $K$ Ergebnissen)
<span class="anker" id="satz-10-1"></span>

Für jede Verteilung $\mathbf{p}$ auf $K$ Ergebnissen ist

<span class="anker" id="gl-10-1"></span>
$$H(\mathbf{p})\le\log_2K , \tag{10.1}$$

und Gleichheit gilt genau dann, wenn $\mathbf{p}$ die Gleichverteilung $\mathbf{u}=(\tfrac1K,\dots,\tfrac1K)^{\top}$ ist.
:::

:::beweis Größte Entropie
Nach [(9.2)](kreuzentropie-und-kl-divergenz.html#gl-9-2) ist $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})=\sum_kp_k\log_2(p_kK)=\sum_kp_k\log_2K-\sum_kp_k\log_2\frac1{p_k}=\log_2K-H(\mathbf{p})$. Nach der Gibbs-Ungleichung ist das nicht negativ und nur für $\mathbf{p}=\mathbf{u}$ null.
:::

::::beispiel [Rechenbeispiel]
Für die Quelle mit $\mathbf{p}=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)^{\top}$ ist $H(\mathbf{p})=1{,}75\le\log_24=2$, und $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})=0{,}25$ bit. Das ist genau die Ersparnis des Codes aus Abb. [14](informationsgehalt-und-entropie.html#abb-14) gegenüber dem Code mit zwei Ziffern je Zeichen. Ein fairer Würfel hat die größtmögliche Entropie $\log_26\approx2{,}585$ bit für sechs Ergebnisse.
::::

⁠**Kurz gesagt:** Unter allen Verteilungen auf $K$ Ergebnissen hat die Gleichverteilung die größte Entropie, $\log_2K$; der Abstand zu ihr ist $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})$.

:::hintergrund Warum gerade die Gleichverteilung
Jede Ungleichheit der Wahrscheinlichkeiten lässt sich ausnutzen: Wer weiß, dass ein Ergebnis häufiger ist, gibt ihm ein kürzeres Codewort und spart im Mittel Binärziffern. Nur bei der Gleichverteilung ist kein Ergebnis häufiger als ein anderes, und kein Code ist im Mittel kürzer als der mit gleich langen Codewörtern. Die Zahl $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})=\log_2K-H(\mathbf{p})$ misst genau, wie viel Vorhersagbarkeit in $\mathbf{p}$ steckt. Daraus folgt eine Regel für den Fall, dass man über eine Verteilung nur wenig weiß: Man wählt unter allen Verteilungen, die zum Wissen passen, die mit der größten Entropie. Sie behauptet nichts, wofür man keinen Grund hat. Ohne jedes Wissen ist das die Gleichverteilung, wie beim gleichförmigen Prior der Laplace-Regel.
:::

### Die Entropie einer Dichte

<span class="anker" id="stufe-10-2"></span>

Für eine stetig verteilte Größe ersetzt man die Summe durch ein Integral und die Wahrscheinlichkeiten durch die Dichte.

:::definition Definition 10.2 (Differentielle Entropie)
<span class="anker" id="satz-10-2"></span>

Die __differentielle Entropie__ einer Dichte $p$ ist

<span class="anker" id="gl-10-2"></span>
$$h(p)=\int p(x)\ln\frac1{p(x)}\,\mathrm{d} x\quad\text{nat}, \tag{10.2}$$

integriert über alle $x$ mit $p(x)>0$.
:::

Das kleine $h$ soll daran erinnern, dass sie sich anders verhält als die Entropie $H$ einer diskreten Verteilung. Sie misst, wie weit eine Dichte ausgebreitet ist, aber sie kann negativ sein, und sie hängt von der Einheit ab, in der man $x$ misst.

::::beispiel [Rechenbeispiel]
Für die Gleichverteilung auf $[0,\,a]$ ist $p(x)=1/a$ und $h=\int_0^a\frac1a\ln a\,\mathrm{d} x=\ln a$. Für $a=\tfrac18$ ist das $\ln\tfrac18\approx-2{,}079$ nat, in bit $\log_2\tfrac18=-3$: negativ. Misst man dieselbe Größe in Millimetern statt in Metern, so wird aus $[0,\,a]$ das Intervall $[0,\,1000a]$, und $h$ wächst um $\ln1000\approx6{,}91$ nat. Für die Normalverteilung $\mathcal N(\mu,\sigma^2)$ ist $\ln\frac1{p(x)}=\tfrac12\ln(2\pi\sigma^2)+\frac{(x-\mu)^2}{2\sigma^2}$, und der Erwartungswert davon ist

<span class="anker" id="gl-10-3"></span>
$$h\bigl(\mathcal N(\mu,\sigma^2)\bigr)=\tfrac12\ln(2\pi\sigma^2)+\frac{\sigma^2}{2\sigma^2}=\tfrac12\ln(2\pi\mathrm{e}\,\sigma^2) , \tag{10.3}$$

für $\sigma=1$ etwa $1{,}419$ nat.
::::

⁠**Kurz gesagt:** Die differentielle Entropie $h(p)=\int p\ln(1/p)\,\mathrm{d} x$ misst die Ausbreitung einer Dichte; sie kann negativ sein und hängt von der Einheit ab.

:::hintergrund Warum die Entropie einer Dichte anders ist
Man kann eine stetige Größe in Intervalle der Breite $\Delta$ einteilen und die Entropie der so entstehenden diskreten Verteilung berechnen. Das Intervall um $x_j$ hat etwa die Wahrscheinlichkeit $p(x_j)\Delta$, und die Entropie in nat ist etwa

$$\sum_jp(x_j)\Delta\ln\frac1{p(x_j)\Delta}=\sum_jp(x_j)\ln\frac1{p(x_j)}\,\Delta+\ln\frac1\Delta\sum_jp(x_j)\Delta\approx h(p)+\ln\frac1\Delta .$$

Für $\Delta\to0$ wächst sie über alle Grenzen: Eine Größe, die beliebig genau angegeben werden soll, braucht unendlich viele Binärziffern. Die differentielle Entropie ist der Teil, der übrig bleibt, wenn man den für alle Dichten gleichen Summanden $\ln(1/\Delta)$ abzieht. Sie taugt deshalb zum Vergleich zweier Dichten in derselben Einheit, ihr Wert für sich hat keine absolute Bedeutung.
:::

### Die KL-Divergenz für Dichten

<span class="anker" id="stufe-10-3"></span>

Die KL-Divergenz überträgt sich ebenso, und bei ihr verschwinden die Schwierigkeiten der differentiellen Entropie.

:::definition Definition 10.3 (KL-Divergenz zweier Dichten)
<span class="anker" id="satz-10-3"></span>

Für zwei Dichten $p$ und $q$ ist

<span class="anker" id="gl-10-4"></span>
$$D_{\mathrm{KL}}(p\,\|\,q)=\int p(x)\ln\frac{p(x)}{q(x)}\,\mathrm{d} x\quad\text{nat}, \tag{10.4}$$

integriert über alle $x$ mit $p(x)>0$.
:::

Die Gibbs-Ungleichung gilt mit demselben Beweis, die Summen werden zu Integralen: $-D_{\mathrm{KL}}(p\,\|\,q)\le\int p\,(q/p-1)\,\mathrm{d} x=\int q\,\mathrm{d} x-1\le0$. Gleichheit gilt genau dann, wenn $p$ und $q$ übereinstimmen, abgesehen von Stellen, an denen das Integral nichts bemerkt. Die KL-Divergenz hängt nicht von der Einheit ab: Misst man $x$ in einer anderen Einheit, so werden beide Dichten mit demselben Faktor multipliziert, und ihr Verhältnis bleibt gleich.

::::beispiel [Rechenbeispiel]
Es sei $p$ die Dichte von $\mathcal N(0,1)$ und $q$ die von $\mathcal N(1,\,2^2)$. Mit [(4.1)](die-likelihood.html#gl-4-1) ist

$$\ln\frac{p(x)}{q(x)}=\ln2-\frac{x^2}2+\frac{(x-1)^2}8 .$$

Unter $p$ ist $\mathbb{E}[x^2]=1$ und $\mathbb{E}[(x-1)^2]=\operatorname{Var}(x)+(\mathbb{E}[x]-1)^2=1+1=2$. Also ist

$$D_{\mathrm{KL}}(p\,\|\,q)=\ln2-\frac12+\frac28\approx0{,}693-0{,}5+0{,}25=0{,}443\ \text{nat}.$$

Abb. [21](#abb-21) zeigt das als Fläche: Die KL-Divergenz ist die Fläche unter $p\ln(p/q)$. Wo $q$ größer ist als $p$, ist der Integrand negativ, aber die positive Fläche überwiegt. In der anderen Richtung ist $D_{\mathrm{KL}}(q\,\|\,p)\approx1{,}307$ nat (Aufgabe [44](#aufg-44)).

:::abbildung ml/k5klflaeche 21
(a) Zwei Normalverteilungen. (b) Der Integrand der KL-Divergenz. Blau die Fläche, wo $p>q$ ist, zwischen $x\approx-1{,}85$ und $x\approx1{,}18$; rot die negative Fläche, wo $q$ größer ist. Die blaue Fläche überwiegt, und die gesamte Fläche ist $0{,}443$.
:::
::::

⁠**Kurz gesagt:** Die KL-Divergenz zweier Dichten ist die Fläche unter $p\ln(p/q)$; sie ist nie negativ, nur für gleiche Dichten null und hängt nicht von der Einheit ab.

### Die Normalverteilung hat bei fester Varianz die größte Entropie

<span class="anker" id="stufe-10-4"></span>

Weiß man von einem Rauschen nur, wie groß seine Leistung ist, also seine Varianz, welche Verteilung soll man dann annehmen? Nach dem Hintergrund-Kasten in Unterabschnitt [10.1](#stufe-10-1) die mit der größten Entropie. Der folgende Satz sagt, welche das ist.

:::satz Satz 10.4 (Größte Entropie bei fester Varianz)
<span class="anker" id="satz-10-4"></span>

Für jede Dichte $p$ mit der Varianz $\sigma^2$ ist

<span class="anker" id="gl-10-5"></span>
$$h(p)\le\tfrac12\ln(2\pi\mathrm{e}\,\sigma^2) , \tag{10.5}$$

und Gleichheit gilt genau dann, wenn $p$ eine Normalverteilung ist.
:::

:::beweis Größte Entropie bei fester Varianz
Es sei $\mu$ der Erwartungswert von $p$ und $q$ die Dichte von $\mathcal N(\mu,\sigma^2)$. Es ist $\ln\frac1{q(x)}=\tfrac12\ln(2\pi\sigma^2)+\frac{(x-\mu)^2}{2\sigma^2}$, und weil $p$ die Varianz $\sigma^2$ hat, ist

$$\int p(x)\ln\frac1{q(x)}\,\mathrm{d} x=\tfrac12\ln(2\pi\sigma^2)+\frac{\sigma^2}{2\sigma^2}=\tfrac12\ln(2\pi\mathrm{e}\,\sigma^2)=h(q) .$$

Nach der Gibbs-Ungleichung für Dichten ist

$$0\le D_{\mathrm{KL}}(p\,\|\,q)=\int p\ln\frac pq\,\mathrm{d} x=-h(p)+\int p\ln\frac1q\,\mathrm{d} x=-h(p)+h(q),$$

also $h(p)\le h(q)$, mit Gleichheit genau dann, wenn $p=q$ ist.
:::

Der Beweis zeigt den Mechanismus. Der Logarithmus einer Normalverteilungsdichte ist eine quadratische Funktion von $x$. Mittelt man ihn mit irgendeiner Dichte $p$, so kommt es nur auf deren Erwartungswert und Varianz an. Unter allen Dichten mit derselben Varianz hat deshalb $\int p\ln(1/q)$ denselben Wert, und die Gibbs-Ungleichung sortiert sie nach ihrem Abstand zur Normalverteilung.

::::beispiel [Rechenbeispiel]
Die Gleichverteilung auf $[-a,\,a]$ hat nach [Grundlagen 4, Abschnitt 8.4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-4), die Varianz $(2a)^2/12=a^2/3$. Mit $a=\sqrt3\,\sigma$ hat sie also die Varianz $\sigma^2$ und die differentielle Entropie $\ln(2a)=\ln\sigma+\ln(2\sqrt3)\approx\ln\sigma+1{,}242$. Die Normalverteilung mit derselben Varianz hat $\tfrac12\ln(2\pi\mathrm{e})+\ln\sigma\approx\ln\sigma+1{,}419$, also $0{,}176$ nat mehr. Genau so groß ist die KL-Divergenz der Gleichverteilung zur Normalverteilung.
::::

⁠**Kurz gesagt:** Unter allen Verteilungen mit derselben Varianz hat die Normalverteilung die größte differentielle Entropie, $\tfrac12\ln(2\pi\mathrm{e}\,\sigma^2)$.

:::hintergrund Der zweite Grund für normalverteiltes Rauschen
[Grundlagen 4, Abschnitt 13.4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-4), hat erklärt, warum Rauschen so oft normalverteilt ist: Es ist die Summe vieler kleiner, unabhängiger Beiträge, und der zentrale Grenzwertsatz macht daraus eine Normalverteilung. Der Satz dieses Unterabschnitts gibt einen zweiten, davon unabhängigen Grund für die Annahme. Kennt man von einem Rauschen nur seine Leistung, also seine Varianz, so ist die Normalverteilung diejenige Verteilung, die darüber hinaus am wenigsten festlegt. Jede andere Verteilung derselben Varianz hätte eine kleinere Entropie, enthielte also eine zusätzliche Struktur, für die man keinen Grund hat. Der erste Grund beschreibt, wie das Rauschen entsteht, der zweite, was man vernünftigerweise annimmt, wenn man das nicht weiß. Beide führen auf dieselbe Verteilung.
:::

:::aufgabe Aufgabe 42 ★ Wie weit von der Gleichverteilung?
<span class="anker" id="aufg-42"></span>

<ol class="al">

<li>

Welche größte Entropie hat eine Verteilung auf acht Ergebnissen?

</li>

<li>

Berechne für $\mathbf{p}=(0{,}4;\ 0{,}3;\ 0{,}2;\ 0{,}1)^{\top}$ die Entropie und $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})$ in bit.

</li>

</ol>

:::loesung
(a) $\log_28=3$ bit, erreicht von der Gleichverteilung.

(b) $H(\mathbf{p})=0{,}4\log_2\tfrac1{0{,}4}+0{,}3\log_2\tfrac1{0{,}3}+0{,}2\log_2\tfrac1{0{,}2}+0{,}1\log_2\tfrac1{0{,}1}\approx0{,}529+0{,}521+0{,}464+0{,}332=1{,}846$ bit und $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})=2-1{,}846=0{,}154$ bit.
:::
:::

:::aufgabe Aufgabe 43 ★★ Differentielle Entropien
<span class="anker" id="aufg-43"></span>

<ol class="al">

<li>

Berechne $h$ für die Gleichverteilung auf $[0,\,2]$ in nat und in bit.

</li>

<li>

Berechne $h$ für $\mathcal N(0;\ 0{,}1^2)$. Warum ist das Ergebnis negativ, und warum ist das kein Widerspruch?

</li>

<li>

Um wie viel ändert sich $h$, wenn man eine Größe mit $c>0$ multipliziert? Begründe mit der Gleichverteilung und mit [(10.3)](#gl-10-3).

</li>

</ol>

:::loesung
(a) $h=\ln2\approx0{,}693$ nat, in bit $\log_22=1$.

(b) $h=\tfrac12\ln(2\pi\mathrm{e}\cdot0{,}01)\approx\tfrac12\ln0{,}1708\approx-0{,}884$ nat. Die Dichte ist schmal und an der Spitze etwa $4$ hoch; $\ln(1/p)$ ist dort negativ, und die differentielle Entropie misst nur die Ausbreitung relativ zur Einheit. Das ist kein Widerspruch, denn nur die Entropie diskreter Verteilungen ist nie negativ: Der Satz in Unterabschnitt [8.2](informationsgehalt-und-entropie.html#stufe-8-2) benutzt $p_k\le1$, und Dichtewerte können größer als $1$ sein.

(c) Mit $c$ multipliziert wird aus der Gleichverteilung auf $[0,\,a]$ die auf $[0,\,ca]$, und $h$ wird zu $\ln(ca)=\ln a+\ln c$. Bei der Normalverteilung wird $\sigma^2$ zu $c^2\sigma^2$, und $\tfrac12\ln(2\pi\mathrm{e} c^2\sigma^2)=\tfrac12\ln(2\pi\mathrm{e}\sigma^2)+\ln c$. In beiden Fällen kommt $\ln c$ hinzu.
:::
:::

:::aufgabe Aufgabe 44 ★★ Die andere Richtung
<span class="anker" id="aufg-44"></span>

Es seien $p$ und $q$ wie im Rechenbeispiel in Unterabschnitt [10.3](#stufe-10-3).

<ol class="al">

<li>

Berechne $D_{\mathrm{KL}}(q\,\|\,p)$. Unter $q$ ist $\mathbb{E}[x^2]=\operatorname{Var}(x)+\mathbb{E}[x]^2$.

</li>

<li>

Erkläre an Abb. [21](#abb-21) (a), warum diese Richtung so viel größer ist.

</li>

</ol>

:::loesung
(a) $\ln\frac{q(x)}{p(x)}=-\ln2+\frac{x^2}2-\frac{(x-1)^2}8$. Unter $q$ ist $\mathbb{E}[x^2]=4+1=5$ und $\mathbb{E}[(x-1)^2]=\operatorname{Var}(x)=4$. Also ist $D_{\mathrm{KL}}(q\,\|\,p)=-\ln2+\tfrac52-\tfrac48\approx-0{,}693+2{,}5-0{,}5=1{,}307$ nat.

(b) $q$ ist breit und gibt den Stellen weit rechts und links viel Gewicht, wo $p$ fast null ist. Wer $p$ erwartet und $q$ erlebt, wird oft von Werten überrascht, die $p$ für sehr selten hält. Umgekehrt erlebt man unter $p$ nur Werte nahe null, die auch $q$ für recht plausibel hält.
:::
:::

:::aufgabe Aufgabe 45 ★★★ Gleichverteilung gegen Normalverteilung
<span class="anker" id="aufg-45"></span>

Es sei $p$ die Gleichverteilung auf $[-\sqrt3\,\sigma,\,\sqrt3\,\sigma]$ und $q$ die Dichte von $\mathcal N(0,\sigma^2)$.

<ol class="al">

<li>

Berechne $D_{\mathrm{KL}}(p\,\|\,q)$ direkt aus [(10.4)](#gl-10-4) und prüfe, dass es $h(q)-h(p)$ ist.

</li>

<li>

Warum hängt das Ergebnis nicht von $\sigma$ ab?

</li>

</ol>

:::loesung
(a) Auf $[-\sqrt3\,\sigma,\sqrt3\,\sigma]$ ist $p=1/(2\sqrt3\,\sigma)$ und $\ln\frac1q=\tfrac12\ln(2\pi\sigma^2)+\frac{x^2}{2\sigma^2}$. Mit $\mathbb{E}_p[x^2]=\sigma^2$ ist

$$\begin{aligned} D_{\mathrm{KL}}(p\,\|\,q)&=\int p\ln p\,\mathrm{d} x+\int p\ln\frac1q\,\mathrm{d} x=-\ln(2\sqrt3\,\sigma)+\tfrac12\ln(2\pi\sigma^2)+\tfrac12\\ &=\tfrac12\ln(2\pi)+\tfrac12-\ln(2\sqrt3)\approx0{,}176 . \end{aligned}$$

Das ist $h(q)-h(p)=\tfrac12\ln(2\pi\mathrm{e}\,\sigma^2)-\ln(2\sqrt3\,\sigma)$.

(b) $\sigma$ hebt sich heraus. Das passt zum Unterabschnitt [10.3](#stufe-10-3): Die KL-Divergenz hängt nicht von der Einheit ab, und eine andere Wahl von $\sigma$ ist nur eine andere Einheit für $x$.
:::
:::
