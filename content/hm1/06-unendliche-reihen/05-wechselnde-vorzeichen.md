---
title: Stufe 3: Wechselnde Vorzeichen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
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

::::beispiel
$L_N$ lautet $1;\ 0{,}5;\ 0{,}833;\ 0{,}583;\ 0{,}783;\ 0{,}617;\ \dots$ Die Schrittweite $\frac1n$ erfüllt alle Voraussetzungen, die Reihe konvergiert. Ihr Wert ist $\log2=0{,}6931$, das wird hier nicht bewiesen. Genauso wie die geraden Teilsummen steigen, fallen die ungeraden: $S_{2N+1}=S_{2N-1}-(a_{2N}-a_{2N+1})$. Also liegt $S$ zwischen je zwei Nachbarn, und der Fehler ist höchstens das erste weggelassene Glied: $|S-S_N|\le a_{N+1}$. Für $N=100$ ist $L_{100}=0{,}68817$, der Fehler $0{,}00498$ unterbietet $\frac1{101}=0{,}0099$. Hundert Glieder ergeben also nur zwei Stellen.
::::

⁠**Grenzfall:** Für $a_n=q^n$ mit $0<q<1$ entsteht eine geometrische Reihe mit Wert $\frac q{1+q}$, für $q=\frac12$ also $\frac13$.

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

::::formelsammlung
**Leibniz-Kriterium**

$$\sum_{n=1}^\infty(-1)^{n+1}a_n=a_1-a_2+a_3-a_4+\cdots$$

Konvergent, wenn $\{a_n\}_{n=1}^\infty$ monoton fallend ist, $a_n>0$ und $\lim_{n\to\infty}a_n=0$. Hier ist $a_n$ die Schrittweite, das Glied ist $(-1)^{n+1}a_n$. Ohne Monotonie oder ohne Nullfolge kann die Reihe divergieren.

**Gerade und ungerade Teilsummen**

$$S_{2N+2}=S_{2N}+(a_{2N+1}-a_{2N+2})\ge S_{2N},\qquad S_{2N+1}=S_{2N-1}-(a_{2N}-a_{2N+1})$$

Die geraden Teilsummen steigen, die ungeraden fallen; beide streben gegen $S$.

**Fehlerschranke**

$$|S-S_N|\le a_{N+1}$$

Unter den Voraussetzungen des Leibniz-Kriteriums: $S$ liegt zwischen je zwei benachbarten Teilsummen, der Fehler ist höchstens das erste weggelassene Glied.

**Alternierende harmonische Reihe**

$$L_N=\sum_{n=1}^N(-1)^{n+1}\frac1n,\qquad\frac1{2k-1}-\frac1{2k}=\frac1{2k(2k-1)}$$

Konvergent nach Leibniz, ihr Wert ist $\log2=0{,}6931$ (hier ohne Beweis). Je zwei Nachbarn ergeben ein Paar, das wie $\frac1{4k^2}$ schrumpft.
::::

::::lernkarten
:::karte begriff alternierende Reihe
Was ist eine alternierende Reihe, und wie schreibt man sie mit positiven Schrittweiten $a_n$?
---
Eine Reihe, deren Vorzeichen von Glied zu Glied wechselt: $\sum_{n=1}^\infty(-1)^{n+1}a_n=a_1-a_2+a_3-a_4+\cdots$ mit $a_n>0$. Hier ist $a_n$ die Schrittweite, das Glied ist $(-1)^{n+1}a_n$.
--- falsch
Eine Reihe, deren Glieder abwechselnd größer und kleiner werden, etwa $a_1<a_2>a_3<a_4>\cdots$. Auf die Vorzeichen kommt es dabei nicht an, die Glieder dürfen alle positiv sein.
--- falsch
Eine Reihe, deren Vorzeichen nach jedem zweiten Glied wechselt: $a_1+a_2-a_3-a_4+\cdots$ mit $a_n>0$. Die Glieder kommen also paarweise mit gleichem Vorzeichen.
--- falsch
Eine Reihe mit unendlich vielen positiven und unendlich vielen negativen Gliedern in beliebiger Reihenfolge, etwa $a_1+a_2-a_3+a_4+a_5-\cdots$ mit $a_n>0$.
:::
:::karte formel Leibniz-Kriterium
Welche Voraussetzungen an die Schrittweiten $a_n$ verlangt das Leibniz-Kriterium, damit die alternierende Reihe $\sum(-1)^{n+1}a_n$ konvergiert?
---
$\{a_n\}_{n=1}^\infty$ ist monoton fallend, $a_n>0$ und $\lim_{n\to\infty}a_n=0$. Dann ist $\sum_{n=1}^\infty(-1)^{n+1}a_n$ konvergent; ohne Monotonie oder ohne Nullfolge kann sie divergieren.
--- falsch
$a_n>0$ und $\lim_{n\to\infty}a_n=0$. Monotonie braucht man nicht, weil die wechselnden Vorzeichen jede Unregelmäßigkeit der Schrittweiten ausgleichen.
--- falsch
$\{a_n\}_{n=1}^\infty$ ist monoton fallend und $a_n>0$. Dass die Schrittweiten gegen 0 gehen, muss man nicht eigens fordern, weil es aus der Monotonie von selbst folgt.
--- falsch
$\{a_n\}_{n=1}^\infty$ ist monoton fallend, $a_n>0$ und $\lim_{n\to\infty}a_n=0$. Dann konvergiert sogar $\sum a_n$ ohne Vorzeichen, weil die Schrittweiten fallen.
:::
:::karte zusammenhang Monotonie nötig
Was passiert beim Leibniz-Kriterium, wenn die Schrittweiten $a_n>0$ zwar gegen 0 gehen, aber nicht monoton fallen?
---
Dann kann die Reihe divergieren: Ist $a_n=\frac1n$ für ungerades und $a_n=\frac1{n^2}$ für gerades $n$, wachsen die positiven Schritte wie die harmonische Reihe, die negativen bleiben beschränkt.
--- falsch
Dann konvergiert die Reihe trotzdem, nur langsamer: Die Monotonie braucht man allein für die Fehlerschranke $|S-S_N|\le a_{N+1}$, nicht für die Konvergenz selbst.
--- falsch
Dann konvergiert die Reihe trotzdem, weil wechselnde Vorzeichen bei einer Nullfolge immer genügen; die Monotonie macht nur den Beweis mit den geraden und ungeraden Teilsummen bequemer.
--- falsch
Dann divergiert die Reihe in jedem Fall, weil ohne Monotonie die notwendige Bedingung verletzt ist: Die Glieder bilden dann keine Nullfolge mehr.
:::
:::karte herleitung Zwei monotone Teilfolgen
Wie zeigt man mit den geraden und den ungeraden Teilsummen, dass die alternierende Reihe unter den Voraussetzungen des Leibniz-Kriteriums konvergiert?
---
$S_{2N}=a_1+(-a_2+a_3)+(-a_4+a_5)+\dots+(-a_{2N-2}+a_{2N-1})-a_{2N}\le a_1$, weil wegen der Monotonie jede Klammer höchstens 0 ist und $-a_{2N}<0$ gilt.
---
$S_{2N+2}=S_{2N}+(a_{2N+1}-a_{2N+2})\ge S_{2N}$, weil die Schrittweiten fallen; die geraden Teilsummen wachsen also monoton.
---
Das Monotonie-Lemma gibt $S:=\lim S_{2N}$, weil $\{S_{2N}\}$ monoton wächst und nach oben beschränkt ist.
---
$S_{2N+1}=S_{2N}+a_{2N+1}\to S+0=S$, weil die Schrittweiten eine Nullfolge bilden.
---
Gerade und ungerade Teilsummen liegen ab einem Index im Schlauch um $S$, also gilt $S_N\to S$, weil jedes $N$ gerade oder ungerade ist.
:::
:::karte formel Fehlerschranke
Wie genau ist eine Teilsumme $S_N$ einer Reihe, die das Leibniz-Kriterium erfüllt, und warum gilt diese Schranke?
---
$|S-S_N|\le a_{N+1}$: Der Fehler ist höchstens das erste weggelassene Glied. Denn die ungeraden Teilsummen fallen, die geraden steigen, und $S$ liegt zwischen je zwei Nachbarn.
--- falsch
$|S-S_N|\ge a_{N+1}$: Der Fehler ist mindestens das erste weggelassene Glied. Denn alle weiteren Glieder kommen noch hinzu und vergrößern den Abstand zum Grenzwert $S$ immer weiter.
--- falsch
$|S-S_N|\le\frac1N$: Der Fehler fällt bei jeder solchen Reihe wie $\frac1N$. Denn die Schrittweiten fallen monoton und deshalb mindestens so schnell wie bei $L_N$.
--- falsch
$|S-S_N|\le\frac12a_{N+1}$: Der Fehler ist höchstens das halbe nächste Glied. Denn $S$ liegt immer genau in der Mitte zwischen zwei benachbarten Teilsummen.
:::
:::karte zusammenhang Vorzeichen rettet die harmonische Reihe
Warum konvergiert die alternierende harmonische Reihe, obwohl die harmonische Reihe aus denselben Beträgen divergiert?
---
Weil je zwei Nachbarn zusammen $\frac1{2k-1}-\frac1{2k}=\frac1{2k(2k-1)}$ ergeben. Die Paare schrumpfen also wie $\frac1{4k^2}$ und nicht wie $\frac1k$: Das Vorzeichen macht aus langsam fallenden Gliedern schnell fallende Paare.
--- falsch
Weil sich je zwei Nachbarn für großes $k$ praktisch aufheben, $\frac1{2k-1}-\frac1{2k}\approx0$. Übrig bleibt im Wesentlichen das erste Glied 1, und das ist dann auch der Wert der Reihe.
--- falsch
Weil die Glieder mit Vorzeichen schneller gegen 0 gehen als ohne: $\bigl|(-1)^{n+1}\frac1n\bigr|$ fällt wie $\frac1{n^2}$, und das reicht wie bei der Quadratreihe für die Konvergenz.
--- falsch
Weil die negativen Glieder für sich ebenso divergieren wie die positiven, und zwei divergente Teile mit entgegengesetztem Vorzeichen ergeben zusammen stets eine konvergente Reihe.
:::
::::
