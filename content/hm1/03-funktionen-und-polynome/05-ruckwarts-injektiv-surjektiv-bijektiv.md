---
title: Stufe 3: Rückwärts: injektiv, surjektiv, bijektiv
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
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
Surjektiv ist $f$ nach Definition von $\mathcal W(f)$. Für die Injektivität zeigt man die gleichwertige Kontraposition ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)): Aus $x\neq y$ folgt $f(x)\neq f(y)$. Sei $x<y$ (sonst vertausche die Namen). Ist $f$ streng wachsend, gilt $f(x)<f(y)$, ist $f$ streng fallend, gilt $f(x)>f(y)$. In beiden Fällen ist $f(x)\neq f(y)$.
:::

⁠**So liest man das:** Das Ziel ist hier genau $\mathcal W(f)$. **Warum „streng“ nötig ist:** Auf dem waagerechten Stück in Abb. [3](gerade-monoton-beschrankt.html#abb-3) haben viele $x$ dasselbe Bild. **Die Umkehrung gilt nicht:** $f(x)=1/x$ auf $\mathbb{R}\setminus\{0\}$ ist bijektiv auf $\mathbb{R}\setminus\{0\}$, aber nicht monoton, denn $-1<1$ ergibt $f(-1)<f(1)$, und $1<2$ ergibt $f(1)>f(2)$.

::::beispiel [Beispiele]
Nach Satz [2.2](gerade-monoton-beschrankt.html#satz-2-2) und [3.2](#satz-3-2) ist $f(x)=x^n$ bijektiv auf seinen Wertebereich, und zwar ist $\mathcal W(f)=\mathbb{R}_0^+$ für gerades $n$ auf $\mathbb{R}_0^+$ und $\mathcal W(f)=\mathbb{R}$ für ungerades $n$ auf $\mathbb{R}$. Dass wirklich jedes $y$ getroffen wird, folgt wie bei $\sqrt y$ aus der Vollständigkeit der reellen Zahlen ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Ohne Monotonie rechnet man direkt: $f:\mathbb{R}\to\mathbb{R}$, $f(x)=2x-5$ ist injektiv, denn $2x-5=2y-5$ ergibt $x=y$, und surjektiv, denn zu $y$ löst $x=(y+5)/2$ die Gleichung.
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

::::formelsammlung
**Injektiv**

$$f(x)=f(y)\Rightarrow x=y$$

Für alle $x,y\in A$: Die Gleichung $f(x)=y$ hat für jedes $y$ höchstens eine Lösung, jede Waagerechte trifft den Graphen höchstens einmal.

**Surjektiv**

$$\mathcal W(f)=B$$

Für alle $y\in B$ gibt es ein $x\in A$ mit $f(x)=y$: mindestens eine Lösung. Bijektiv heißt injektiv und surjektiv: genau eine Lösung für jedes $y\in B$. Die Eigenschaften gehören zur Funktion samt $A$ und $B$, nicht zur Formel.

**Streng monoton ergibt bijektiv**

$$f:\mathcal D(f)\to\mathcal W(f)$$

Eine streng monotone reelle Funktion ist als Abbildung auf ihren Wertebereich bijektiv; so ist $x^n$ bijektiv auf $\mathcal W(f)=\mathbb{R}_0^+$ (gerades $n$, auf $\mathbb{R}_0^+$) bzw. auf $\mathcal W(f)=\mathbb{R}$ (ungerades $n$, auf $\mathbb{R}$). Die Umkehrung gilt nicht: $f(x)=1/x$ auf $\mathbb{R}\setminus\{0\}$ ist bijektiv, aber nicht monoton.
::::

::::lernkarten
:::karte begriff injektiv
Wann heißt eine Funktion $f:A\to B$ injektiv, und was bedeutet das für die Gleichung $f(x)=y$?
---
Wenn für alle $x,y\in A$ gilt: $f(x)=f(y)\Rightarrow x=y$; gleiche Bilder haben gleiche Urbilder. Dann hat $f(x)=y$ für jedes $y$ höchstens eine Lösung, jede Waagerechte trifft den Graphen höchstens einmal.
--- falsch
Wenn für alle $x,y\in A$ gilt: $x=y\Rightarrow f(x)=f(y)$; gleiche Urbilder haben gleiche Bilder. Dann hat $f(x)=y$ für jedes $y$ genau eine Lösung, jede Waagerechte trifft den Graphen genau einmal.
--- falsch
Wenn es für alle $y\in B$ ein $x\in A$ gibt mit $f(x)=y$. Dann hat $f(x)=y$ für jedes $y\in B$ mindestens eine Lösung, jede Waagerechte in der Höhe $y\in B$ trifft den Graphen.
--- falsch
Wenn für alle $x,y\in A$ gilt: $f(x)=f(y)\Rightarrow x=y$. Dann hat $f(x)=y$ für jedes $y\in B$ genau eine Lösung, denn jedes Bild hat genau ein Urbild, und jede Waagerechte trifft genau einmal.
:::
:::karte begriff surjektiv
Wann heißt eine Funktion $f:A\to B$ surjektiv, und wie drückt man das mit dem Wertebereich aus?
---
Wenn es für alle $y\in B$ ein $x\in A$ gibt mit $f(x)=y$, also $\mathcal W(f)=B$. Dann hat $f(x)=y$ für jedes $y\in B$ mindestens eine Lösung; mehrere Lösungen sind erlaubt.
--- falsch
Wenn es für alle $x\in A$ ein $y\in B$ gibt mit $f(x)=y$, also $\mathcal D(f)=A$. Das gilt für jede Funktion; surjektiv betont nur, dass kein Eingang ohne Bild bleibt.
--- falsch
Wenn es für alle $y\in B$ genau ein $x\in A$ gibt mit $f(x)=y$, also $\mathcal W(f)=B$ und keine doppelten Bilder. Dann hat $f(x)=y$ genau eine Lösung.
--- falsch
Wenn $\mathcal W(f)\subset B$ gilt, die Bilder also im Ziel liegen. Dann hat $f(x)=y$ für jedes $y\in B$ höchstens eine Lösung, weil kein Bild außerhalb von $B$ liegt.
:::
:::karte begriff bijektiv
Wann heißt eine Funktion $f:A\to B$ bijektiv, und wie viele Lösungen hat dann die Gleichung $f(x)=y$?
---
Wenn $f$ injektiv und surjektiv ist. Dann hat $f(x)=y$ für jedes $y\in B$ genau eine Lösung: mindestens eine wegen surjektiv, höchstens eine wegen injektiv.
--- falsch
Wenn $f$ injektiv oder surjektiv ist. Dann hat $f(x)=y$ für jedes $y\in B$ mindestens eine Lösung; welche der beiden Eigenschaften vorliegt, entscheidet über die Zahl der Lösungen.
--- falsch
Wenn $f(x)=y$ für jedes $y\in B$ zwei Lösungen hat, wie bei der Parabel $h$, die jede Höhe über ihrem tiefsten Punkt zweimal trifft. Daher kommt die Vorsilbe „bi“.
--- falsch
Wenn $f$ injektiv und surjektiv ist. Dann hat $f(x)=y$ für jedes $y\in\mathbb{R}$ genau eine Lösung, unabhängig davon, welches Ziel $B$ man für $f$ gewählt hat.
:::
:::karte zusammenhang Waagerechte durch den Graphen
Wie liest man an einer Waagerechten durch den Graphen ab, wie viele Lösungen die Gleichung $f(x)=y$ hat?
---
Man zieht die Waagerechte in der Höhe $y$; jeder Schnittpunkt mit dem Graphen ist eine Lösung. Bei der Parabel $h$ gibt es zu $y=3$ zwei Lösungen, $x=0$ und $x=4$, zu $y=-2$ keine.
--- falsch
Man zieht eine Senkrechte an der Stelle $x$; jeder Schnittpunkt ist eine Lösung. Trifft sie den Graphen zweimal, hat $f(x)=y$ zwei Lösungen, trifft sie ihn nicht, keine.
--- falsch
Man zieht die Waagerechte in der Höhe $y$; nur ein Schnittpunkt zählt als Lösung, weitere Schnittpunkte sind Spiegelbilder. Bei der Parabel $h$ ist $x=4$ die Lösung zu $y=3$.
--- falsch
Man zieht die Waagerechte in der Höhe $y$; jeder Schnittpunkt mit dem Graphen ist eine Lösung. Für jedes $y$ gibt es mindestens einen, weil eine Waagerechte jeden Graphen irgendwo trifft.
:::
:::karte zusammenhang Funktion samt A und B
Warum kann man nicht sagen, ob $f(x)=x^2$ injektiv oder surjektiv ist, ohne die Mengen $A$ und $B$ zu kennen?
---
Weil die Eigenschaften zur Funktion samt $A$ und $B$ gehören, nicht zur Formel: $\mathbb{R}\to\mathbb{R}$ weder noch, $\mathbb{R}\to\mathbb{R}_0^+$ surjektiv, $\mathbb{R}_0^+\to\mathbb{R}$ injektiv, $\mathbb{R}_0^+\to\mathbb{R}_0^+$ bijektiv.
--- falsch
Weil $x^2$ an manchen Stellen injektiv ist und an anderen nicht; man muss jeden Punkt einzeln prüfen. Die Mengen $A$ und $B$ sagen, an welchen Punkten man prüfen soll.
--- falsch
Doch, das kann man: $x^2$ ist als Formel nie injektiv, weil $f(2)=f(-2)$ gilt, und nie surjektiv, weil $y=-1$ kein Urbild hat. Die Mengen $A$ und $B$ ändern daran nichts.
--- falsch
Weil die Eigenschaften zur Funktion samt $A$ und $B$ gehören: Als $\mathbb{R}\to\mathbb{R}$ ist $x^2$ surjektiv, als $\mathbb{R}_0^+\to\mathbb{R}_0^+$ injektiv, aber bijektiv ist $x^2$ bei keiner Wahl von $A$ und $B$.
:::
:::karte formel Streng monoton ergibt bijektiv
Welche Aussage macht der Satz „Streng monoton ergibt bijektiv“, und auf welches Ziel bezieht er sich?
---
Eine streng monotone reelle Funktion $f:\mathcal D(f)\to\mathcal W(f)$ ist bijektiv. Das Ziel ist genau der Wertebereich, damit sie surjektiv ist; die Umkehrung gilt nicht.
--- falsch
Eine monoton wachsende oder fallende reelle Funktion $f:\mathcal D(f)\to\mathbb{R}$ ist bijektiv. Das Ziel ist ganz $\mathbb{R}$, und die Umkehrung gilt ebenfalls: Jede bijektive Funktion ist monoton.
--- falsch
Eine streng monotone reelle Funktion $f:\mathcal D(f)\to\mathbb{R}$ ist bijektiv, weil sie wegen der strengen Monotonie jede reelle Zahl genau einmal erreicht. Das Ziel ist ganz $\mathbb{R}$.
--- falsch
Eine bijektive reelle Funktion $f:\mathcal D(f)\to\mathcal W(f)$ ist streng monoton. Das Ziel ist der Wertebereich, und die Umkehrung, von streng monoton auf bijektiv, gilt nicht.
:::
:::karte herleitung Streng monoton ergibt bijektiv
Wie zeigt man, dass eine streng monotone reelle Funktion $f:\mathcal D(f)\to\mathcal W(f)$ bijektiv ist?
---
$f$ ist surjektiv, weil das Ziel genau $\mathcal W(f)$ ist und jedes Element des Wertebereichs nach Definition ein Urbild hat.
---
Für die Injektivität zeigt man die gleichwertige Kontraposition: Aus $x\neq y$ folgt $f(x)\neq f(y)$; das genügt, weil eine Implikation und ihre Kontraposition gleichwertig sind.
---
Sei $x<y$; das ist keine Einschränkung, weil man sonst die Namen vertauscht.
---
Ist $f$ streng wachsend, gilt $f(x)<f(y)$, ist $f$ streng fallend, gilt $f(x)>f(y)$; in beiden Fällen ist $f(x)\neq f(y)$, weil eine strenge Ungleichung die Gleichheit ausschließt.
:::
:::karte zusammenhang warum streng nötig ist
Warum genügt im Satz „Streng monoton ergibt bijektiv“ eine bloß monotone Funktion nicht?
---
Weil eine monotone Funktion waagerechte Stücke haben darf: Dort haben viele $x$ dasselbe Bild, und $f$ ist nicht injektiv. Erst „streng“ schließt gleiche Werte an verschiedenen Stellen aus.
--- falsch
Weil eine monotone Funktion Sprünge haben darf: Dann werden manche Werte übersprungen, und $f$ ist nicht surjektiv auf $\mathcal W(f)$. Erst „streng“ schließt solche Sprünge aus.
--- falsch
Weil eine monotone Funktion nach oben beschränkt sein kann: Dann erreicht sie nicht jede Höhe, und $f$ ist nicht surjektiv. Erst „streng“ sorgt dafür, dass sie über alle Grenzen wächst.
--- falsch
Weil eine monotone Funktion zwischendurch die Richtung wechseln darf, erst wachsen und dann fallen. Dann wird eine Höhe zweimal getroffen; „streng“ verbietet den Richtungswechsel.
:::
:::karte zusammenhang Umkehrung gilt nicht
Warum folgt aus „bijektiv“ nicht „streng monoton“, und welches Beispiel zeigt das?
---
Weil eine bijektive Funktion die Richtung wechseln darf: $f(x)=1/x$ auf $\mathbb{R}\setminus\{0\}$ ist bijektiv auf $\mathbb{R}\setminus\{0\}$, aber $-1<1$ ergibt $f(-1)<f(1)$ und $1<2$ ergibt $f(1)>f(2)$.
--- falsch
Doch, das folgt: Eine bijektive Funktion trifft jede Höhe genau einmal und kann deshalb nie umkehren. $f(x)=1/x$ ist streng fallend auf ganz $\mathbb{R}\setminus\{0\}$, wie die Werte zeigen.
--- falsch
Weil bijektiv nur über die Zahl der Lösungen spricht: $f(x)=x^2$ auf $\mathbb{R}$ ist bijektiv auf $\mathbb{R}_0^+$, aber nicht monoton, denn $-2<-1$ ergibt $f(-2)>f(-1)$.
--- falsch
Weil Monotonie nur auf Intervallen erklärt ist: $f(x)=1/x$ auf $\mathbb{R}\setminus\{0\}$ ist bijektiv, aber auf einer Menge mit Lücke kann man gar nicht von monoton sprechen.
:::
:::karte zusammenhang injektiv machen
Wie macht man eine nicht injektive Funktion wie die Parabel $h$ injektiv, und was muss man dabei angeben?
---
Man verkleinert den Definitionsbereich. Das ändert die Funktion, und man muss sagen, welches Teilstück man behält: $h$ auf $[2,\infty)$ und $h$ auf $(-\infty,2]$ sind beide injektiv, mit verschiedenen Umkehrungen.
--- falsch
Man verkleinert das Ziel $B$ auf den Wertebereich. Dadurch verschwinden die doppelt getroffenen Höhen, und die Funktion bleibt dieselbe; ein Teilstück des Definitionsbereichs muss man nicht auswählen.
--- falsch
Man verkleinert den Definitionsbereich. Welches Teilstück man behält, ist gleichgültig: $h$ auf $[2,\infty)$ und $h$ auf $(-\infty,2]$ haben dieselbe Umkehrung, weil die Formel gleich bleibt.
--- falsch
Gar nicht: Ob eine Funktion injektiv ist, liegt an ihrer Formel. Eine Parabel trifft jede Höhe über dem tiefsten Punkt zweimal, egal auf welcher Menge man sie betrachtet.
:::
:::karte zusammenhang bijektiv ohne Monotonie
Wie zeigt man ohne Monotonie, dass $f:\mathbb{R}\to\mathbb{R}$, $f(x)=2x-5$ injektiv und surjektiv ist?
---
Man rechnet direkt: Aus $2x-5=2y-5$ folgt $x=y$, also injektiv; zu jedem $y$ löst $x=(y+5)/2$ die Gleichung $f(x)=y$, also surjektiv.
--- falsch
Man setzt zwei Werte ein: $f(0)=-5$ und $f(1)=-3$ sind verschieden, also ist $f$ injektiv; und weil $f$ negative und positive Werte annimmt, ist $f$ surjektiv.
--- falsch
Man rechnet direkt: Aus $x=y$ folgt $2x-5=2y-5$, also injektiv; und weil zu jedem $x$ ein Wert $f(x)$ existiert, trifft $f$ jede reelle Zahl, also surjektiv.
--- falsch
Man rechnet direkt: Aus $2x-5=2y-5$ folgt $x=y$, also injektiv; surjektiv ist $f$ nicht, weil $f(x)=0$ keine ganzzahlige Lösung hat und $\mathbb{R}$ nicht ganz getroffen wird.
:::
:::karte formel Potenzen bijektiv
Auf welchen Mengen ist $f(x)=x^n$ bijektiv auf ihren Wertebereich, und welcher Wertebereich ergibt sich dabei?
---
Für gerades $n$ auf $\mathbb{R}_0^+$ mit $\mathcal W(f)=\mathbb{R}_0^+$, für ungerades $n$ auf $\mathbb{R}$ mit $\mathcal W(f)=\mathbb{R}$. Dass jedes $y$ getroffen wird, folgt aus der Vollständigkeit der reellen Zahlen.
--- falsch
Für jedes $n$ auf $\mathbb{R}$ mit $\mathcal W(f)=\mathbb{R}$, weil jede reelle Zahl eine $n$-te Potenz ist. Dass jedes $y$ getroffen wird, folgt aus der strengen Monotonie allein.
--- falsch
Für gerades $n$ auf $\mathbb{R}$ mit $\mathcal W(f)=\mathbb{R}_0^+$, für ungerades $n$ auf $\mathbb{R}_0^+$ mit $\mathcal W(f)=\mathbb{R}$. Dass jedes $y$ getroffen wird, folgt aus der Vollständigkeit der reellen Zahlen.
--- falsch
Für gerades $n$ auf $\mathbb{R}_0^+$ mit $\mathcal W(f)=\mathbb{R}_0^+$, für ungerades $n$ auf $\mathbb{R}$ mit $\mathcal W(f)=\mathbb{R}$. Dass jedes $y$ getroffen wird, folgt schon für Brüche, ohne die Vollständigkeit.
:::
::::
