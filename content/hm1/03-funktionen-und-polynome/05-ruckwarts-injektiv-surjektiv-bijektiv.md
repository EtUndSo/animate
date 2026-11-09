---
title: Stufe 3: Rückwärts: injektiv, surjektiv, bijektiv
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Funktionen und Polynome
order: 1230500
summary: Vorwärts gibt es zu jedem x genau ein y .
tags: injektiv, surjektiv, bijektiv
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Vorwärts gibt es zu jedem $x$ genau ein $y$. Rückwärts fehlt diese Garantie: Die Gleichung $f(x)=y$ kann keine, eine oder viele Lösungen haben. Diese Stufe gibt den drei Fällen Namen.
:::

**Die Idee.** Man zieht in der Höhe $y$ eine Waagerechte durch den Graphen. Jeder Schnittpunkt ist eine Lösung von $f(x)=y$ (Abb. [4](#abb-4)). Bei der Parabel $h$ gibt es zu $y=3$ zwei Lösungen ($x=0$ und $x=4$), zu $y=-2$ keine. Für jedes $y\in\mathcal W(f)$ gibt es nach Definition mindestens eine Lösung, nur kennt man $\mathcal W(f)$ oft nicht.

:::definition Definition 3.1 (Injektiv, surjektiv, bijektiv)
<span class="anker" id="satz-3-1"></span>

Eine Funktion $f:A\to B$ heißt

<ol class="rm">

<li>

__injektiv__, falls für alle $x,y\in A$ gilt: $f(x)=f(y)\Rightarrow x=y$;

</li>

<li>

__surjektiv__, falls es für alle $y\in B$ ein $x\in A$ gibt mit $f(x)=y$;

</li>

<li>

__bijektiv__, falls $f$ injektiv und surjektiv ist.

</li>

</ol>
:::

⁠**So liest man das:** Injektiv heißt: Gleiche Bilder haben gleiche Urbilder, also hat $f(x)=y$ für jedes $y$ höchstens eine Lösung, und die Waagerechte trifft höchstens einmal. Surjektiv heißt $\mathcal W(f)=B$: Mindestens eine Lösung für jedes $y\in B$. Bijektiv heißt: genau eine. **Gültigkeit:** Die Eigenschaften gehören zur Funktion samt $A$ und $B$, nicht zur Formel:

| $f(x)=x^2$ als Abbildung | injektiv | surjektiv |
|---|---|---|
| $\mathbb{R}\to\mathbb{R}$ | nein, $f(2)=f(-2)$ | nein, $y=-1$ hat kein Urbild |
| $\mathbb{R}\to\mathbb{R}_0^+$ | nein | ja |
| $\mathbb{R}_0^+\to\mathbb{R}$ | ja | nein |
| $\mathbb{R}_0^+\to\mathbb{R}_0^+$ | ja | ja |

:::abbildung hm1/k3rueckwaerts 4
Links $h:\mathbb{R}\to[-1,\infty)$: surjektiv, aber nicht injektiv, die Höhe 3 wird zweimal getroffen. Mitte $b:\mathbb{R}_0^+\to\mathbb{R}$: injektiv, aber nicht surjektiv, die Höhe 1,5 wird nie getroffen. Rechts $x^3:\mathbb{R}\to\mathbb{R}$: bijektiv, jede Höhe wird genau einmal getroffen.
:::

:::satz Satz 3.2 (Streng monoton ergibt bijektiv)
<span class="anker" id="satz-3-2"></span>

Eine streng monotone reelle Funktion $f:\mathcal D(f)\to\mathcal W(f)$ ist bijektiv.
:::

:::beweis Streng monoton ergibt bijektiv
Surjektiv ist $f$ nach Definition von $\mathcal W(f)$. Für die Injektivität zeigt man die gleichwertige Kontraposition ([Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)): Aus $x\neq y$ folgt $f(x)\neq f(y)$. Sei $x<y$ (sonst vertausche die Namen). Ist $f$ streng wachsend, gilt $f(x)<f(y)$, ist $f$ streng fallend, gilt $f(x)>f(y)$. In beiden Fällen ist $f(x)\neq f(y)$.
:::

⁠**So liest man das:** Das Ziel ist hier genau $\mathcal W(f)$. **Warum „streng“ nötig ist:** Auf dem waagerechten Stück in Abb. [3](gerade-monoton-beschrankt.html#abb-3) haben viele $x$ dasselbe Bild. **Die Umkehrung gilt nicht:** $f(x)=1/x$ auf $\mathbb{R}\setminus\{0\}$ ist bijektiv auf $\mathbb{R}\setminus\{0\}$, aber nicht monoton, denn $-1<1$ ergibt $f(-1)<f(1)$, und $1<2$ ergibt $f(1)>f(2)$.

::::beispiel [Beispiele]
Nach Satz [2.2](gerade-monoton-beschrankt.html#satz-2-2) und [3.2](#satz-3-2) ist $f(x)=x^n$ bijektiv auf seinen Wertebereich, und zwar ist $\mathcal W(f)=\mathbb{R}_0^+$ für gerades $n$ auf $\mathbb{R}_0^+$ und $\mathcal W(f)=\mathbb{R}$ für ungerades $n$ auf $\mathbb{R}$. Dass wirklich jedes $y$ getroffen wird, folgt wie bei $\sqrt y$ aus der Vollständigkeit der reellen Zahlen ([Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Ohne Monotonie rechnet man direkt: $f:\mathbb{R}\to\mathbb{R}$, $f(x)=2x-5$ ist injektiv, denn $2x-5=2y-5$ ergibt $x=y$, und surjektiv, denn zu $y$ löst $x=(y+5)/2$ die Gleichung.
::::

⁠**Grenzfall:** $f(x)=x$ ist bijektiv, jede Höhe wird genau bei $x=y$ getroffen.

:::frage Kann man jede nicht injektive Funktion injektiv machen?
Ja, durch Verkleinern des Definitionsbereichs. Das ändert die Funktion, und man muss sagen, welches Teilstück man behält: $h$ auf $[2,\infty)$ und $h$ auf $(-\infty,2]$ sind beide injektiv und haben verschiedene Umkehrungen. Genauso entsteht $\sqrt y$ aus $x^2$ auf $\mathbb{R}_0^+$.
:::

:::aufgabe Aufgabe 3 ★★ Wie viele Lösungen?
<span class="anker" id="aufg-3"></span>

(a) Für $g(x)=x^2+6x+5$: Wähle $A$ mit $0\in A$ und $B$ so, dass $g:A\to B$ bijektiv ist, und gib die Lösung von $g(x)=y$ an. (b) Vorhersage ohne Rechnung: Ist $f:\mathbb{Z}\to\mathbb{Z}$, $f(n)=2n$ injektiv? Surjektiv?

:::loesung
(a) $g(x)=(x+3)^2-4$ wächst auf $A=[-3,\infty)$ streng, und $B=[-4,\infty)$. Aus $(x+3)^2=y+4$ und $x+3\ge0$ folgt $x=-3+\sqrt{y+4}$. Probe: $y=5$ ergibt $x=0$. (b) Injektiv ja: $2n=2m\Rightarrow n=m$. Surjektiv nein: $3$ ist ungerade und hat kein Urbild.
:::
:::
