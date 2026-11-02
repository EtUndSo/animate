---
title: Stufe 7: Maximum, Minimum, gleichmäßige Stetigkeit
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
order: 1250900
summary: Hat eine stetige Funktion einen größten Wert?
tags: Minimum, Maximum, nicht konstruktiv, gleichmäßig stetig
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Hat eine stetige Funktion einen größten Wert? Reicht eine Eingangstoleranz für alle Stellen? Auf $[a,b]$ ja. Diese Stufe zeigt warum und was geschieht, wenn eine Voraussetzung fehlt.
:::

**Die Idee.** Man nimmt Stellen $x_n$, an denen $f$ dem Supremum immer näher kommt. Eine Teilfolge läuft gegen eine Stelle $x_1$. Die Abgeschlossenheit hält $x_1$ im Intervall, die Stetigkeit nimmt die Werte mit: $f(x_1)$ ist das Supremum.

:::satz Satz 7.1 (Stetig auf [a,b] ist beschränkt)
<span class="anker" id="satz-7-1"></span>

Sei $a<b$ und $f:[a,b]\to\mathbb{R}$ stetig. Dann ist $f$ beschränkt: Es gibt $K>0$ mit $|f(x)|\le K$ für alle $x\in[a,b]$.
:::

:::beweis Indirekt mit Bolzano-Weierstraß
Sei $f$ ohne Einschränkung nach oben unbeschränkt (sonst betrachte $-f$). Dann gibt es zu jedem $n\in\mathbb{N}$ ein $x_n\in[a,b]$ mit $f(x_n)>n$. Die Folge $\{x_n\}$ ist beschränkt, also gibt es eine Teilfolge $x_{n_k}\to\bar x$. Wegen $a\le x_{n_k}\le b$ gilt $\bar x\in[a,b]$. Die Folgenstetigkeit gibt $f(x_{n_k})\to f(\bar x)\in\mathbb{R}$. Konvergente Folgen sind beschränkt, aber $f(x_{n_k})>n_k\ge k$. Widerspruch.
:::

⁠**So liest man das:** Der Graph liegt in einem waagerechten Streifen der Höhe $2K$.

:::satz Satz 7.2 (Weierstraß, Satz vom Maximum)
<span class="anker" id="satz-7-2"></span>

Sei $f:[a,b]\to\mathbb{R}$ stetig. Dann nimmt $f$ das Infimum $m=\inf\mathcal W(f)\in\mathbb{R}$ und das Supremum $M=\sup\mathcal W(f)\in\mathbb{R}$ als Wert an:

<ol class="rm">

<li>

$m\in\mathcal W(f)$: Es gibt $x_0\in[a,b]$ mit $f(x)\ge m=f(x_0)$ für alle $x\in[a,b]$, also ist $\inf\mathcal W(f)$ ein __Minimum__.

</li>

<li>

$M\in\mathcal W(f)$: Es gibt $x_1\in[a,b]$ mit $f(x)\le M=f(x_1)$ für alle $x\in[a,b]$, also ist $\sup\mathcal W(f)$ ein __Maximum__.

</li>

</ol>
:::

:::beweis Teilfolge wählen, Wert mitnehmen
Nach Satz [7.1](#satz-7-1) ist $\mathcal W(f)$ beschränkt und nicht leer, das Vollständigkeitsaxiom gibt $M\in\mathbb{R}$. Da $M-\frac1n$ keine obere Schranke ist, gibt es $x_n\in[a,b]$ mit $M-\frac1n<f(x_n)\le M$, also $f(x_n)\to M$. Bolzano-Weierstraß gibt eine Teilfolge $x_{n_k}\to x_1$, und $x_1\in[a,b]$ wie oben. Die Folgenstetigkeit gibt $f(x_1)=\lim_{k\to\infty}f(x_{n_k})=M$. Für $m$ wendet man das auf $-f$ an.
:::

⁠**So liest man das:** Ein Supremum muss kein Funktionswert sein, hier ist es einer. Wo, sagt der Beweis nicht: Er ist __nicht konstruktiv__. **Beispiele:** Die wachsende Prüffunktion hat auf $[0,1]$ das Minimum $k(0)=1$ und das Maximum $k(1)=3{,}718$. Die Kurve $i(x)=x\,\mathrm{e}^{-x}$ auf $[0,2]$ (so verläuft der Strom eines kritisch gedämpften Schwingkreises) hat das Minimum $i(0)=0$ und das Maximum $i(1)=\frac{1}{\mathrm{e}}=0{,}3679$. Das zeigt Satz [2.1](wachstum-logarithmus-allgemeine-potenz.html#satz-2-1) (i): Aus $\mathrm{e}^{x-1}\ge x$ folgt $x\,\mathrm{e}^{-x}\le\mathrm{e}^{-1}$. **Grenzfall:** Für konstantes $f$ ist $m=M$.

**Jede Voraussetzung wird gebraucht (Abb. [7](#abb-7)).**

| Was fehlt | Gegenbeispiel | Was im Beweis bricht |
|---|---|---|
| abgeschlossen | $1/x$ auf $(0,1]$: unbeschränkt. $x$ auf $[0,1)$: beschränkt, Supremum 1 kein Wert | Der Grenzpunkt $\bar x=0$ bzw. $1$ liegt nicht im Intervall |
| beschränktes Intervall | $\mathrm{e}^x$ auf $[0,\infty)$: unbeschränkt, kein Maximum | $\{x_n\}$ läuft weg, Bolzano-Weierstraß greift nicht |
| stetig | $f(x)=\frac1{x-1}$, $f(1)=0$ auf $[0,2]$: unbeschränkt. $v(x)=x$ für $x<1$, $v(1)=0$ auf $[0,1]$: beschränkt, Supremum 1 kein Wert | Der Wert $f(\bar x)$ folgt den $f(x_{n_k})$ nicht |

:::abbildung hm1/k5maximum 7
Links wächst $1/x$ auf $(0,1]$ ohne Grenze, die 0 fehlt. Mitte: $v$ springt bei 1 nach unten, das Supremum 1 wird nicht erreicht. Rechts steigt $\mathrm{e}^x$ auf $[0,\infty)$ immer weiter.
:::

**Eine Eingangstoleranz für alle Stellen.** In Stufe [4](stetigkeit-und-epsilon-delta.html#stufe-4) hing $\delta_0$ von $x_0$ ab. Bei $1/x$ auf $(0,1]$ muss man das: Für $\varepsilon=1$ ist die größte Antwort $\delta_0=\frac16$ bei $x_0=\frac12$, aber nur $\frac1{20}$ bei $x_0=\frac14$. Allgemein ist sie $\frac{\varepsilon x_0^2}{1+\varepsilon x_0}$, und das schrumpft mit $x_0$ gegen 0. Keine Antwort gewinnt überall.

:::definition Definition 7.3 (Gleichmäßige Stetigkeit)
<span class="anker" id="satz-7-3"></span>

Sei $f:M\to\mathbb{R}$, $M\subset\mathbb{R}$. Dann heißt $f$ auf $M$ __gleichmäßig stetig__, wenn es zu jedem $\varepsilon>0$ ein $\delta_0=\delta_0(\varepsilon)>0$ gibt, so dass für alle $x,y\in M$ gilt:

<span class="anker" id="gl-7-1"></span>
$$|x-y|<\delta_0\quad\Longrightarrow\quad|f(x)-f(y)|<\varepsilon. \tag{7.1}$$
:::

⁠**So liest man das:** Im Unterschied zum $\varepsilon$-$\delta$-Kriterium darf $\delta_0$ nicht von $x$ oder $y$ abhängen. Hält man $y=x_0$ fest, entsteht [(4.1)](stetigkeit-und-epsilon-delta.html#gl-4-1): Gleichmäßig stetig auf $(a,b)$ ergibt stetig in jedem Punkt. Die Umkehrung gilt nicht, wie $1/x$ auf $(0,1]$ zeigt: Für $x=\frac1n$, $y=\frac1{n+1}$ ist $|x-y|=\frac1{n(n+1)}\to0$, aber $|f(x)-f(y)|=1$. **Beispiel:** $x^2$ auf $[0,3]$: Es ist $|x^2-y^2|=|x-y|\,|x+y|\le6\,|x-y|$, also gewinnt $\delta_0=\varepsilon/6$ überall. Auf ganz $\mathbb{R}$ fehlt die Schranke für $|x+y|$.

:::satz Satz 7.4 (Stetig auf [a,b] ist gleichmäßig stetig)
<span class="anker" id="satz-7-4"></span>

Sei $f:[a,b]\to\mathbb{R}$ stetig. Dann ist $f$ auf $[a,b]$ gleichmäßig stetig.
:::

:::beweis Wieder Teilfolge und Stetigkeit
Wäre $f$ nicht gleichmäßig stetig, gäbe es $\varepsilon_1>0$ und zu jedem $n$ Stellen $x_n,y_n\in[a,b]$ mit $|x_n-y_n|<\frac1n$ und $|f(x_n)-f(y_n)|\ge\varepsilon_1$. Bolzano-Weierstraß gibt eine Teilfolge $x_{n_k}\to\bar x\in[a,b]$. Wegen $y_{n_k}=(y_{n_k}-x_{n_k})+x_{n_k}$ läuft auch $y_{n_k}\to\bar x$. Die Folgenstetigkeit gibt $f(x_{n_k})\to f(\bar x)$ und $f(y_{n_k})\to f(\bar x)$, also $|f(x_{n_k})-f(y_{n_k})|\to0$. Das widerspricht $\ge\varepsilon_1$.
:::

⁠**So liest man das:** Auf $[a,b]$ reicht eine Eingangstoleranz für alle Stellen. Auf $(0,1]$ fehlt der Grenzpunkt 0, deshalb scheitert $1/x$.

:::aufgabe Aufgabe 7 ★★ Satz anwendbar?
<span class="anker" id="aufg-7"></span>

Entscheide jeweils, ob der Satz vom Maximum gilt. Gib Maximum und Minimum an oder begründe, warum eines fehlt. (a) $x^2$ auf $[-1,2]$. (b) $x^2$ auf $(-1,1)$. (c) $\mathrm{e}^{-x}$ auf $[0,\infty)$. (d) $H$ auf $[-1,1]$. (e) Bestimme das Minimum von $x-\log x$ auf $[\frac12,2]$ mit Satz [2.3](wachstum-logarithmus-allgemeine-potenz.html#satz-2-3) (iv).

:::loesung
(a) Gilt: Maximum 4 bei 2, Minimum 0 bei 0. (b) Nicht abgeschlossen: Minimum 0, Supremum 1 wird nicht angenommen. (c) Unbeschränktes Intervall: Maximum 1 bei 0, Infimum 0 wird nicht angenommen. (d) Nicht stetig. Hier existieren trotzdem Maximum 1 und Minimum 0: Der Satz ist hinreichend, nicht notwendig. (e) Aus $\log x\le x-1$ folgt $x-\log x\ge1$, Gleichheit bei $x=1$: Das Minimum ist 1.
:::
:::
