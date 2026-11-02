---
title: Stufe 3: Wechselnde Vorzeichen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Unendliche Reihen
order: 1260500
summary: Die harmonische Reihe divergiert, weil jede Stufe nach oben führt.
tags: alternierende Reihe
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die harmonische Reihe divergiert, weil jede Stufe nach oben führt. Diese Stufe zeigt, was geschieht, wenn die Stufen abwechselnd nach oben und unten führen.
:::

**Die Idee.** Bei wechselnden Vorzeichen nimmt jeder Schritt einen Teil des vorigen zurück, aber nie alles, weil die Schritte schrumpfen. Deshalb fallen die Teilsummen mit ungeradem Index, die mit geradem steigen. Beide Folgen schachteln das Ziel ein, und ihr Abstand ist gerade das nächste Glied, das gegen 0 geht (Abb. [3](#abb-3)).

:::satz Satz 3.1 (Leibniz-Kriterium)
<span class="anker" id="satz-3-1"></span>

Sei $\{a_n\}_{n=1}^\infty$ monoton fallend, $a_n>0$ und $\lim_{n\to\infty}a_n=0$. Dann ist die __alternierende Reihe__ (das Vorzeichen wechselt von Glied zu Glied)

<span class="anker" id="gl-3-1"></span>
$$\sum_{n=1}^\infty(-1)^{n+1}a_n=a_1-a_2+a_3-a_4+\cdots \tag{3.1}$$

konvergent.
:::

⁠**So liest man das:** Hier ist $a_n>0$ die Schrittweite, nicht das Glied. Das Glied ist $(-1)^{n+1}a_n$, für $n=1$ positiv. Bei $L_N$ ist $a_4=\frac14$ und das vierte Glied $-\frac14$. **Voraussetzungen nötig:** Ohne Nullfolge scheitert die notwendige Bedingung, etwa bei $\sum(-1)^{n+1}\frac n{n+1}$. Ohne Monotonie geht es auch schief: Sei $a_n=\frac1n$ für ungerades und $a_n=\frac1{n^2}$ für gerades $n$. Die positiven Schritte summieren sich wie die harmonische Reihe auf, die negativen bleiben beschränkt (Stufe [5](absolute-konvergenz-und-vergleich.html#stufe-5)), also divergiert die Reihe.

:::beweis Zwei monotone Teilfolgen
Sei $S_N=\sum_{n=1}^N(-1)^{n+1}a_n$. Die Folge $\{S_{2N}\}$ ist nach oben beschränkt, denn wegen der Monotonie ist jede Klammer höchstens 0:

$$S_{2N}=a_1+(-a_2+a_3)+(-a_4+a_5)+\dots+(-a_{2N-2}+a_{2N-1})-a_{2N}\le a_1.$$

Sie ist monoton wachsend, denn $S_{2N+2}=S_{2N}+(a_{2N+1}-a_{2N+2})\ge S_{2N}$. Das Monotonie-Lemma gibt $S:=\lim S_{2N}$. Weiter ist $S_{2N+1}=S_{2N}+a_{2N+1}\to S+0=S$. Gerade und ungerade Teilsummen liegen also ab einem Index im Schlauch um $S$, damit gilt $S_N\to S$.
:::

:::abbildung hm1/k6leibniz 3
Die Teilsummen $L_N$. Die ungeraden fallen, die geraden steigen, der Grenzwert $S$ liegt immer dazwischen. Der Abstand zweier Nachbarn ist das nächste Glied.
:::

**Beispiel.** $L_N$ lautet $1;\ 0{,}5;\ 0{,}833;\ 0{,}583;\ 0{,}783;\ 0{,}617;\ \dots$ Die Schrittweite $\frac1n$ erfüllt alle Voraussetzungen, die Reihe konvergiert. Ihr Wert ist $\log2=0{,}6931$, das wird hier nicht bewiesen. Genauso wie die geraden Teilsummen steigen, fallen die ungeraden: $S_{2N+1}=S_{2N-1}-(a_{2N}-a_{2N+1})$. Also liegt $S$ zwischen je zwei Nachbarn, und der Fehler ist höchstens das erste weggelassene Glied: $|S-S_N|\le a_{N+1}$. Für $N=100$ ist $L_{100}=0{,}68817$, der Fehler $0{,}00498$ unterbietet $\frac1{101}=0{,}0099$. Hundert Glieder ergeben also nur zwei Stellen. **Grenzfall:** Für $a_n=q^n$ mit $0<q<1$ entsteht eine geometrische Reihe mit Wert $\frac q{1+q}$, für $q=\frac12$ also $\frac13$.

:::frage Warum rettet das Vorzeichen die harmonische Reihe?
Fasst man je zwei Nachbarn zusammen, bleibt $\frac1{2k-1}-\frac1{2k}=\frac1{2k(2k-1)}$. Die Paare schrumpfen also wie $\frac1{4k^2}$ und nicht wie $\frac1k$. Das Vorzeichen macht aus langsam fallenden Gliedern schnell fallende Paare.
:::

:::aufgabe Aufgabe 3 ★★ Einschachteln
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Zeige, dass $\sum(-1)^{n+1}\frac1{\sqrt n}$ konvergiert. Wie viele Glieder garantieren einen Fehler unter $0{,}01$?

</li>

<li>

Berechne für $\sum(-1)^{n+1}\frac1{n^2}$ die Teilsummen $S_4$ und $S_5$. Zwischen welchen Zahlen liegt der Wert?

</li>

</ol>

:::loesung
(a) $\frac1{\sqrt n}$ ist positiv und fällt monoton gegen 0, Leibniz greift. Der Fehler ist höchstens $\frac1{\sqrt{N+1}}<0{,}01$, also $N+1>10^4$. Das erfüllt $N=10000$. (b) $S_4=1-\frac14+\frac19-\frac1{16}=\frac{115}{144}=0{,}7986$ und $S_5=S_4+\frac1{25}=0{,}8386$. Der Wert liegt zwischen beiden.
:::
:::
