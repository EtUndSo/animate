---
title: Stufe 2: Gerade, monoton, beschränkt
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230400
summary: Die Definition sagt, was eine Funktion ist, aber nicht, wie sie aussieht.
tags: gerade, ungerade, monoton wachsend, streng monoton wachsend, monoton fallend, streng monoton fallend, beschränkt
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die Definition sagt, was eine Funktion ist, aber nicht, wie sie aussieht. Drei Eigenschaften sparen Rechnung: Symmetrie halbiert die Arbeit, Monotonie ordnet die Werte, Beschränktheit begrenzt sie.
:::

**Die Idee.** Hängt $f(x)$ nur vom Abstand zur Null ab, sind die Werte links ein Spiegelbild der Werte rechts (Abb. [3](#abb-3)). Wächst $f$ mit $x$, folgt aus $x<y$ schon etwas über die Werte, ohne sie zu rechnen. Bleibt $f$ unter einer festen Zahl, kann nichts über alle Grenzen wachsen.

:::definition Definition 2.1 (Symmetrie, Monotonie, Beschränktheit)
<span class="anker" id="satz-2-1"></span>

Sei $f$ eine reelle Funktion. Enthält $\mathcal D(f)$ mit $x$ auch $-x$, so heißt $f$ __gerade__, falls $f(x)=f(-x)$ für alle $x\in\mathcal D(f)$, und __ungerade__, falls $f(x)=-f(-x)$ für alle $x\in\mathcal D(f)$. Weiter heißt $f$, jeweils für alle $x,y\in\mathcal D(f)$,

<ol class="rm">

<li>

__monoton wachsend__, falls aus $x<y$ folgt $f(x)\le f(y)$;

</li>

<li>

__streng monoton wachsend__, falls aus $x<y$ folgt $f(x)<f(y)$;

</li>

<li>

__monoton fallend__, falls aus $x<y$ folgt $f(x)\ge f(y)$;

</li>

<li>

__streng monoton fallend__, falls aus $x<y$ folgt $f(x)>f(y)$.

</li>

</ol>

$f$ heißt nach oben (unten) __beschränkt__, wenn es eine Zahl $K$ gibt mit $f(x)\le K$ ($f(x)\ge K$) für alle $x\in\mathcal D(f)$, also wenn die Menge $\mathcal W(f)$ nach oben (unten) beschränkt ist. Gilt beides, heißt $f$ beschränkt.
:::

⁠**So liest man das:** Gerade heißt: Der Graph geht durch Spiegeln an der $y$-Achse in sich über. Ungerade heißt: Er geht durch Punktspiegelung am Ursprung in sich über. Die Namen kommen von den Potenzen: $(-x)^{2n}=x^{2n}$ und $(-x)^{2n+1}=-x^{2n+1}$. Es genügt daher, die Werte auf $\mathcal D(f)\cap\mathbb{R}_0^+$ zu kennen, den Rest liefert die Spiegelung. Fallend und wachsend hängen zusammen: $f$ ist genau dann (streng) monoton fallend, wenn $-f$ (streng) monoton wachsend ist, denn Multiplikation mit $-1$ dreht die Ungleichung um.

:::abbildung hm1/k3eigenschaften 3
Links die gerade Glocke $b$: Die Werte bei $\pm1{,}5$ sind gleich. Mitte die ungerade Funktion $x^3-3x$: Die Werte bei $\pm1{,}5$ sind entgegengesetzt, $\mp1{,}125$. Rechts eine monoton wachsende Funktion mit waagerechtem Stück: Sie ist nicht streng monoton.
:::

:::satz Satz 2.2 (Potenzen sind monoton)
<span class="anker" id="satz-2-2"></span>

Sei $n\in\mathbb{N}$. Für ungerades $n$ ist $f(x)=x^n$ auf $\mathbb{R}$ streng monoton wachsend, für gerades $n$ auf $\mathbb{R}_0^+$.
:::

:::beweis Potenzen
⁠**Fall $0\le x<y$, jedes $n$:** Induktion über $n$. Für $n=1$ steht es da. Aus $x^n<y^n$ folgt $x^{n+1}=x\cdot x^n\le y\cdot x^n<y\cdot y^n=y^{n+1}$. Der erste Schritt benutzt $x<y$ und $x^n\ge0$, der zweite $y>0$. Das erledigt gerades $n$. **Fall $x<y\le0$, $n$ ungerade:** Es ist $0\le-y<-x$, nach dem ersten Fall $(-y)^n<(-x)^n$, und weil $n$ ungerade ist, $-y^n<-x^n$, also $x^n<y^n$. **Fall $x<0<y$, $n$ ungerade:** $x^n<0<y^n$.
:::

⁠**So liest man das:** $n$ ist die feste Potenz. **Warum „auf $\mathbb{R}_0^+$“ nötig ist:** Für gerades $n$ ist $f$ auf ganz $\mathbb{R}$ nicht monoton, es ist $-2<-1$, aber $(-2)^2>(-1)^2$.

::::beispiel [Beispiele]
$h$ ist nach unten durch $-1$ beschränkt, nach oben nicht. Die Glocke ist beschränkt und auf $\mathbb{R}_0^+$ streng fallend: Aus $0\le x<y$ folgt $1+x^2<1+y^2$, also $b(x)>b(y)$. Summe und Produkt beschränkter Funktionen sind wieder beschränkt: Aus $|f|\le K$ und $|g|\le L$ folgt $|f+g|\le K+L$ und $|f\cdot g|\le K\,L$.
::::

⁠**Grenzfälle:** Eine konstante Funktion ist monoton wachsend und fallend zugleich, aber nicht streng. $f(x)=0$ ist gerade und ungerade zugleich.

:::frage Ist eine Funktion, die nicht gerade ist, automatisch ungerade?
Bei Zahlen stimmt das, bei Funktionen nicht: $f(x)=x^2+x$ hat $f(1)=2$ und $f(-1)=0$: weder gleich noch entgegengesetzt. Die meisten Funktionen sind beides nicht.
:::

:::aufgabe Aufgabe 2 ★★ Symmetrie und Schranken
<span class="anker" id="aufg-2"></span>

(a) Gerade, ungerade oder keins: $f_1(x)=x^4-3x^2$, $f_2(x)=x^3+x$, $f_3(x)=x^2+x$, $f_4(x)=x\,|x|$? (b) Zeige: Das Produkt zweier ungerader Funktionen ist gerade. (c) Bestimme für $v(x)=3/(2+x^2)$ Schranken und den Wertebereich, und zeige, dass $v$ auf $\mathbb{R}_0^+$ streng monoton fällt.

:::loesung
(a) $f_1(-x)=f_1(x)$: gerade. $f_2(-x)=-x^3-x=-f_2(x)$: ungerade. $f_3(1)=2$, $f_3(-1)=0$: keins. $f_4(-x)=-x\,|x|=-f_4(x)$: ungerade. (b) Mit $f(-x)=-f(x)$ und $g(-x)=-g(x)$ ist $(f\cdot g)(-x)=(-f(x))(-g(x))=(f\cdot g)(x)$. (c) Wegen $2+x^2\ge2$ ist $0<v(x)\le\frac32$. Jedes $y\in(0,\frac32]$ wird von $x=\sqrt{3/y-2}$ getroffen, also $\mathcal W(v)=(0,\frac32]$. Für $0\le x<y$ wächst der Nenner, der Bruch fällt.
:::
:::
