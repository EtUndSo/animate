---
title: Stufe 7: Intervallschachtelung und Wurzeln
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210900
summary: Das Axiom garantiert Grenzen.
tags: Intervall, nicht negativen Zahlen, Wurzel
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Das Axiom garantiert Grenzen. Diese Stufe macht daraus ein Bauverfahren und beweist damit, dass $x^2=2$ in $\mathbb{R}$ genau eine positive Lösung hat.
:::

**Die Idee.** Man fängt die gesuchte Zahl zwischen zwei Brüchen ein und halbiert das Intervall immer wieder, bis es beliebig klein ist (Abb. [7](#abb-7)). Jedes Intervall liegt im vorigen. Die Vollständigkeit garantiert, dass es einen Punkt gibt, der in allen liegt. In $\mathbb{Q}$ kann dieser Punkt fehlen. Ein __Intervall__ ist $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$, die __nicht negativen Zahlen__ sind $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ge0\}$.

:::satz Satz 7.1 (Intervallschachtelung)
<span class="anker" id="satz-7-1"></span>

Für Zahlen $a_n,b_n\in\mathbb{R}$, $n\in\mathbb{N}$, gelte $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$ und

<span class="anker" id="gl-7-1"></span>
$$\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon. \tag{7.1}$$

Dann gibt es genau ein $x\in\mathbb{R}$ mit $a_n\le x\le b_n$ für alle $n\in\mathbb{N}$.
:::

⁠**So liest man das:** $\varepsilon$ (griechisch Epsilon) ist eine beliebig kleine positive Zahl. [(7.1)](#gl-7-1) heißt: Die Intervalle $[a_n,b_n]$ werden kleiner als jede vorgegebene Länge. **Warum die Voraussetzungen:** Ohne [(7.1)](#gl-7-1) ist $x$ nicht eindeutig: Für $a_n=-\frac1n$, $b_n=1+\frac1n$ liegt ganz $[0,1]$ in allen Intervallen. In $\mathbb{Q}$ gilt der Satz nicht: Die Brüche $a_n,b_n$ aus Abb. [7](#abb-7) erfüllen alle Bedingungen, aber kein Bruch liegt in allen Intervallen.

:::beweis Intervallschachtelung
⁠*Existenz.* Für beliebige $n,k$ sei $m$ die größere der beiden Zahlen. Dann $a_n\le a_m\le b_m\le b_k$. Also ist jedes $b_k$ obere Schranke von $A:=\{a_n:n\in\mathbb{N}\}$. Nach Satz [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (i) existiert $x:=\sup A$. Es ist $a_n\le x$, weil $x$ obere Schranke ist, und $x\le b_k$, weil $x$ die kleinste ist.

⁠*Eindeutigkeit.* Lägen $x<\tilde x$ in allen Intervallen, wäre $b_n-a_n\ge\tilde x-x=:\varepsilon>0$ für alle $n$, gegen [(7.1)](#gl-7-1).
:::

:::abbildung hm1/k1schachtelung 7
Halbieren für $x^2=2$: Ist das Quadrat der Mitte kleiner als 2, wird sie die neue linke Grenze, sonst die neue rechte. Die Länge ist $b_n-a_n=2^{1-n}$.
:::

:::satz Satz 7.2 (Wurzel)
<span class="anker" id="satz-7-2"></span>

Zu jedem $y\in\mathbb{R}_0^+$ gibt es genau ein $x\in\mathbb{R}_0^+$ mit $x^2=y$. Man schreibt $x=\sqrt y$ („__Wurzel__ aus $y$“). Für $x,y\ge0$ gilt $\sqrt{xy}=\sqrt x\sqrt y$.
:::

⁠**So liest man das:** Die Wurzel ist die nicht negative Lösung, $\sqrt{4}=2$ und nicht $-2$. Die Gleichung $z^2=2$ hat zwei Lösungen: $\sqrt2$ und $-\sqrt2$, denn $(-1)(-1)=1$. Die Produktregel braucht $x,y\ge0$: $\sqrt{(-1)(-1)}=1$, aber $\sqrt{-1}$ gibt es in $\mathbb{R}$ nicht. **Grenzfall** $y=0$: Die einzige Lösung ist $x=0$.

:::beweis Existenz für $y=2$, Eindeutigkeit, Produktregel
Man startet mit $a_1=1$, $b_1=2$ und halbiert wie in Abb. [7](#abb-7). Alle $a_n$, $b_n$ sind Brüche, also ist nach Satz [6.1](das-vollstandigkeitsaxiom.html#satz-6-1) nie $a_n^2=2$ oder $b_n^2=2$. Das gibt $a_n^2<2<b_n^2$ und $b_n-a_n=2^{1-n}\le\frac1n$ wegen $2^{n-1}\ge n$ (Aufgabe [10](elementare-ungleichungen.html#aufg-10)). Nach Satz [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (vi) gilt [(7.1)](#gl-7-1), also gibt es $x$ mit $a_n\le x\le b_n$ für alle $n$.

Warum $x^2=2$: Aus $a_n\le x\le b_n$ folgt nach Satz [4.2](anordnungsaxiome.html#satz-4-2) (e) $a_n^2\le x^2\le b_n^2$. Auch 2 liegt in $[a_n^2,b_n^2]$. Dieses Intervall hat die Länge $(b_n-a_n)(b_n+a_n)\le4\cdot\frac1n$. Der Abstand von $x^2$ und 2 ist also kleiner als jede positive Zahl und damit null. Für andere $y>0$ startet man mit $[0,y+1]$; trifft eine Mitte $m$ genau $m^2=y$, ist $x=m$. Für $y=0$ ist $x=0$. *Eindeutigkeit:* Aus $u>v\ge0$ folgt $u^2>v^2$, zwei verschiedene nicht negative Zahlen haben verschiedene Quadrate.

⁠*Produktregel:* $\sqrt x\sqrt y\ge0$ und $(\sqrt x\sqrt y)^2=xy$ (M1, M2), und die nicht negative Lösung ist eindeutig.
:::

::::beispiel
Nach sechs Schritten ist $1{,}40625\le\sqrt2\le1{,}4375$, Breite $2^{-5}=0{,}03125$. Dezimalzahlen sind dieselbe Idee mit zehn statt zwei Teilen: Jede Ziffer schränkt das Intervall auf ein Zehntel ein. Deshalb hat jede reelle Zahl eine Darstellung [(0.1)](von-grund-auf-zahlbereiche-und-dezimalzahlen.html#gl-0-1).
::::

:::frage Es reicht doch, $\sqrt2$ vom Taschenrechner abzulesen. Wozu der Aufwand?
Für jeden Zahlenwert reicht das. Der Rechner zeigt aber einen Bruch, $1{,}414213562$, dessen Quadrat nicht 2 ist. Die Frage hier lautet: Gibt es überhaupt eine Zahl mit Quadrat genau 2? In $\mathbb{Q}$ nein, in $\mathbb{R}$ ja, und dieser Unterschied trägt später Grenzwerte und Stetigkeit.
:::

:::aufgabe Aufgabe 8 ★★★ Die Wurzel aus 3
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Führe drei Halbierungsschritte für $x^2=3$ aus, Start $[1,2]$. Wie breit ist das Ergebnis?

</li>

<li>

Beweise $\sqrt3\notin\mathbb{Q}$. Hinweis: Eine Zahl, die nicht durch 3 teilbar ist, hat die Form $3k\pm1$.

</li>

<li>

An welcher Stelle scheitert derselbe Beweis für $\sqrt4$?

</li>

</ol>

:::loesung
(a) Mitte $1{,}5$: $2{,}25<3$, also $[1{,}5;\,2]$. Mitte $1{,}75$: $3{,}0625>3$, also $[1{,}5;\,1{,}75]$. Mitte $1{,}625$: $2{,}640625<3$, also $[1{,}625;\,1{,}75]$. Breite $\frac18=0{,}125$. (b) Annahme: $\sqrt3=\frac pq$, $p,q\in\mathbb{N}$, nicht beide durch 3 teilbar. Dann $p^2=3q^2$. Wäre $p=3k\pm1$, dann $p^2=3(3k^2\pm2k)+1$, nicht durch 3 teilbar. Also $p=3k$, damit $q^2=3k^2$, und ebenso ist $q$ durch 3 teilbar. Widerspruch. (c) Aus $p^2=4q^2$ folgt $p=2k$ und $k^2=q^2$. Das sagt nichts über die Teilbarkeit von $q$: $\sqrt4=\frac21$.
:::
:::

::::formelsammlung
**Intervall und nicht negative Zahlen**

$$[a,b]:=\{x\in\mathbb{R}:a\le x\le b\},\qquad\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ge0\}$$

Die Grenzen $a$ und $b$ gehören zum Intervall, die Null gehört zu $\mathbb{R}_0^+$.

**Intervallschachtelung**

$$a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1,\qquad\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon$$

Für $a_n,b_n\in\mathbb{R}$: Dann gibt es genau ein $x\in\mathbb{R}$ mit $a_n\le x\le b_n$ für alle $n\in\mathbb{N}$. Ohne die Längenbedingung ist $x$ nicht eindeutig; in $\mathbb{Q}$ gilt der Satz nicht.

**Halbierungsverfahren**

$$b_n-a_n=2^{1-n}$$

Für $x^2=2$ mit $a_1=1$, $b_1=2$: Ist das Quadrat der Mitte kleiner als 2, wird sie die neue linke Grenze, sonst die neue rechte.

**Wurzel**

$$x=\sqrt y\quad\Longleftrightarrow\quad x\in\mathbb{R}_0^+\ \text{und}\ x^2=y$$

Zu jedem $y\in\mathbb{R}_0^+$ gibt es genau ein solches $x$. Die Wurzel ist die nicht negative Lösung; $z^2=2$ hat die zwei Lösungen $\sqrt2$ und $-\sqrt2$.

**Produktregel der Wurzel**

$$\sqrt{xy}=\sqrt x\sqrt y$$

Für $x,y\ge0$.
::::

::::lernkarten
:::karte begriff Intervall
Wie ist das Intervall $[a,b]$ als Menge reeller Zahlen definiert?
---
Als Menge aller reellen Zahlen zwischen $a$ und $b$ einschließlich der Grenzen: $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$.
--- falsch
Als Menge aller reellen Zahlen zwischen $a$ und $b$ ohne die Grenzen: $[a,b]:=\{x\in\mathbb{R}:a<x<b\}$.
--- falsch
Als Menge aller ganzen Zahlen zwischen $a$ und $b$ einschließlich der Grenzen: $[a,b]:=\{x\in\mathbb{Z}:a\le x\le b\}$.
--- falsch
Als Paar der beiden Grenzen $a$ und $b$; die Zahlen dazwischen gehören nicht dazu, nur die beiden Endpunkte selbst.
:::
:::karte begriff nicht negative Zahlen
Welche Zahlen bilden die Menge $\mathbb{R}_0^+$ der nicht negativen Zahlen?
---
Alle reellen Zahlen, die größer oder gleich null sind: $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ge0\}$. Die Null gehört dazu.
--- falsch
Alle reellen Zahlen, die echt größer als null sind: $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x>0\}$. Die Null gehört nicht dazu.
--- falsch
Alle natürlichen Zahlen und die Null: $\mathbb{R}_0^+:=\mathbb{N}\cup\{0\}$. Brüche und Wurzeln gehören nicht dazu.
--- falsch
Alle reellen Zahlen außer der Null: $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ne0\}$. Der Index 0 zeigt an, dass die Null fehlt.
:::
:::karte formel Intervallschachtelung
Was besagt der Satz über die Intervallschachtelung, und welche Voraussetzungen hat er?
---
Gilt $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$ und $\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon$, dann gibt es genau ein $x\in\mathbb{R}$ mit $a_n\le x\le b_n$ für alle $n\in\mathbb{N}$.
--- falsch
Gilt $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$, dann gibt es genau ein $x\in\mathbb{R}$ mit $a_n\le x\le b_n$ für alle $n\in\mathbb{N}$; wie schnell die Intervalle schrumpfen, spielt dafür keine Rolle.
--- falsch
Gilt $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$ und $\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon$, dann gibt es genau ein $x\in\mathbb{Q}$ mit $a_n\le x\le b_n$ für alle $n\in\mathbb{N}$.
--- falsch
Gilt $\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon$, dann gibt es genau ein $x$ mit $a_n\le x\le b_n$ für alle $n$; ob die Intervalle ineinander liegen, ist dafür gleichgültig.
:::
:::karte zusammenhang Längenbedingung
Warum braucht die Intervallschachtelung die Bedingung, dass die Längen $b_n-a_n$ kleiner als jedes $\varepsilon>0$ werden?
---
Weil sonst der gemeinsame Punkt nicht eindeutig ist: Für $a_n=-\frac1n$, $b_n=1+\frac1n$ liegt ganz $[0,1]$ in allen Intervallen.
--- falsch
Weil sonst kein gemeinsamer Punkt existiert: Intervalle, die nicht beliebig klein werden, haben nie einen Punkt, der in allen von ihnen liegt.
--- falsch
Weil sonst die Intervalle nicht ineinander lägen: Erst die Längenbedingung sorgt dafür, dass jedes Intervall im vorigen enthalten ist.
--- falsch
Weil sonst der gemeinsame Punkt kein Bruch wäre: Erst die Längenbedingung sichert, dass der Punkt in $\mathbb{Q}$ liegt und nicht nur in $\mathbb{R}$.
:::
:::karte zusammenhang Intervallschachtelung in den Brüchen
Warum gilt der Satz über die Intervallschachtelung nicht in $\mathbb{Q}$?
---
Weil die Existenz des gemeinsamen Punkts auf der Vollständigkeit beruht. Die Brüche $a_n$, $b_n$ aus dem Halbieren für $x^2=2$ erfüllen alle Bedingungen, aber kein Bruch liegt in allen Intervallen.
--- falsch
Weil in $\mathbb{Q}$ die Intervalle nicht beliebig klein werden können: Zwischen zwei Brüchen bleibt immer ein Mindestabstand, der vom Nenner abhängt und nicht unterschritten wird.
--- falsch
Er gilt in $\mathbb{Q}$ genauso, weil alle Grenzen $a_n$, $b_n$ Brüche sind und der gemeinsame Punkt deshalb ebenfalls ein Bruch sein muss; der Satz gilt in jedem Körper.
--- falsch
Weil in $\mathbb{Q}$ die Eindeutigkeit fehlt: Es liegen dort immer zwei verschiedene Brüche in allen Intervallen, nie genau einer, weil zwischen zwei Brüchen ein weiterer liegt.
:::
:::karte herleitung Intervallschachtelung
Wie beweist man Existenz und Eindeutigkeit des Punkts $x$ in einer Intervallschachtelung?
---
Für beliebige $n,k$ sei $m$ die größere der beiden Zahlen; dann gilt $a_n\le a_m\le b_m\le b_k$, weil die $a_n$ wachsen und die $b_n$ fallen. Also ist jedes $b_k$ obere Schranke von $A:=\{a_n:n\in\mathbb{N}\}$.
---
Es existiert $x:=\sup A$, weil in $\mathbb{R}$ jede nach oben beschränkte, nicht leere Menge ein Supremum hat.
---
Es ist $a_n\le x$, weil $x$ obere Schranke von $A$ ist, und $x\le b_k$, weil $x$ die kleinste obere Schranke ist.
---
Lägen $x<\tilde x$ in allen Intervallen, wäre $b_n-a_n\ge\tilde x-x>0$ für alle $n$; das ist unmöglich, weil die Längen kleiner als jedes $\varepsilon>0$ werden.
:::
:::karte begriff Wurzel
Was ist die Wurzel $\sqrt y$ einer Zahl $y\in\mathbb{R}_0^+$?
---
Die eindeutige Zahl $x\in\mathbb{R}_0^+$ mit $x^2=y$. Die Wurzel ist also nie negativ: $\sqrt{4}=2$ und nicht $-2$.
--- falsch
Jede Zahl $x\in\mathbb{R}$ mit $x^2=y$. Die Wurzel hat deshalb zwei Werte: $\sqrt{4}=2$ und ebenso $\sqrt{4}=-2$.
--- falsch
Die eindeutige Zahl $x\in\mathbb{R}_0^+$ mit $2x=y$. Die Wurzel ist also die Hälfte und nie negativ: $\sqrt{4}=2$.
--- falsch
Die eindeutige Zahl $x\in\mathbb{Q}$ mit $x^2=y$. Deshalb gibt es Wurzeln nur aus Quadratzahlen wie $4$ oder $\frac94$.
:::
:::karte zusammenhang zwei Lösungen
Warum hat die Gleichung $z^2=2$ zwei reelle Lösungen, obwohl $\sqrt2$ nur eine Zahl bezeichnet?
---
Weil auch $-\sqrt2$ das Quadrat 2 hat, denn $(-1)(-1)=1$. Die Wurzel ist nur die nicht negative Lösung; die Lösungen sind $\sqrt2$ und $-\sqrt2$.
--- falsch
Weil $\sqrt2$ zwei verschiedene Dezimaldarstellungen hat, eine endende und eine nicht endende; jede von ihnen ergibt eine eigene Lösung.
--- falsch
Weil $z^2=2$ eine Lösung in $\mathbb{Q}$ und eine in $\mathbb{R}$ hat; die rationale Lösung ist der Bruch $1{,}414$, die reelle ist $\sqrt2$.
--- falsch
Weil die Wurzel selbst zwei Werte hat, $+\sqrt2$ und $-\sqrt2$; deshalb schreibt man auch $\sqrt2=\pm1{,}414\ldots$
:::
:::karte formel Produktregel der Wurzel
Für welche Zahlen gilt $\sqrt{xy}=\sqrt x\sqrt y$, und warum?
---
Für $x,y\ge0$: $\sqrt x\sqrt y$ ist nicht negativ und hat das Quadrat $xy$, und die nicht negative Lösung ist eindeutig. Für $x=y=-1$ scheitert sie: $\sqrt{(-1)(-1)}=1$, aber $\sqrt{-1}$ gibt es in $\mathbb{R}$ nicht.
--- falsch
Für alle $x,y\in\mathbb{R}$, weil Wurzelziehen und Multiplizieren vertauschbar sind; so ist $\sqrt{(-1)(-1)}=\sqrt{-1}\sqrt{-1}=1$, und die Regel bleibt auch für negative Zahlen gültig.
--- falsch
Nur für $x,y\in\mathbb{Q}$, weil die Regel aus dem Kürzen von Brüchen folgt; für irrationale Zahlen wie $\sqrt2\sqrt3$ gilt sie nicht, weil man dort nicht kürzen kann.
--- falsch
Für $x,y\ge0$; außerdem gilt entsprechend $\sqrt{x+y}=\sqrt x+\sqrt y$, weil die Wurzel mit Summen genauso verträglich ist wie mit Produkten, etwa bei $\sqrt{9+16}$.
:::
:::karte zusammenhang Halbierungsverfahren
Wie engt das Halbierungsverfahren für $x^2=2$ die Zahl $\sqrt2$ ein, und wie schnell schrumpfen die Intervalle?
---
Man startet mit $[1,2]$; ist das Quadrat der Mitte kleiner als 2, wird sie neue linke Grenze, sonst neue rechte. Die Länge ist $b_n-a_n=2^{1-n}$, nach sechs Schritten gilt $1{,}40625\le\sqrt2\le1{,}4375$.
--- falsch
Man startet mit $[1,2]$; ist das Quadrat der Mitte kleiner als 2, wird sie neue rechte Grenze, sonst neue linke. Die Länge ist $b_n-a_n=2^{1-n}$, sodass das Intervall nach jedem Schritt halb so lang ist.
--- falsch
Man startet mit $[1,2]$ und verkürzt das Intervall in jedem Schritt um $\frac1{10}$. Die Länge ist $b_n-a_n=1-\frac n{10}$, nach zehn Schritten ist $\sqrt2$ deshalb exakt bestimmt.
--- falsch
Man startet mit $[1,2]$; ist die Mitte selbst kleiner als 2, wird sie neue linke Grenze, sonst neue rechte. Die Länge ist $b_n-a_n=\frac1n$, nach sechs Schritten also $\frac16$.
:::
:::karte herleitung Existenz der Wurzel aus 2
Wie zeigt man mit dem Halbierungsverfahren, dass es ein $x\in\mathbb{R}$ mit $x^2=2$ gibt?
---
Halbieren ab $a_1=1$, $b_1=2$ liefert Brüche mit $a_n^2<2<b_n^2$, weil kein Bruch das Quadrat 2 hat und deshalb nie $a_n^2=2$ oder $b_n^2=2$ gilt.
---
Wegen $b_n-a_n=2^{1-n}\le\frac1n$ und Eudoxus werden die Längen kleiner als jedes $\varepsilon>0$; die Intervallschachtelung liefert $x$ mit $a_n\le x\le b_n$ für alle $n$, weil $\mathbb{R}$ vollständig ist.
---
Aus $a_n\le x\le b_n$ folgt $a_n^2\le x^2\le b_n^2$, weil man Ungleichungen zwischen nicht negativen Zahlen quadrieren darf.
---
Auch 2 liegt in $[a_n^2,b_n^2]$, und dieses Intervall hat die Länge $(b_n-a_n)(b_n+a_n)\le4\cdot\frac1n$, weil $b_n+a_n\le4$ ist.
---
Der Abstand von $x^2$ und 2 ist also kleiner als jede positive Zahl und damit null, weil es sonst nach Eudoxus ein $n$ gäbe, für das $4\cdot\frac1n$ kleiner als dieser Abstand ist.
:::
:::karte zusammenhang Dezimaldarstellung reeller Zahlen
Warum hat jede reelle Zahl eine Dezimaldarstellung?
---
Weil Dezimalziffern eine Intervallschachtelung mit zehn statt zwei Teilen sind: Jede Ziffer schränkt das Intervall auf ein Zehntel ein, und die Schachtelung trifft genau eine Zahl.
--- falsch
Weil die reellen Zahlen als Dezimalzahlen festgelegt sind; das Vollständigkeitsaxiom verlangt das ausdrücklich, und Zahlen ohne Darstellung sind keine reellen Zahlen.
--- falsch
Weil jede reelle Zahl ein Bruch ist und man jeden Bruch durch schriftliches Teilen in eine endende oder periodische Dezimalzahl umwandeln kann.
--- falsch
Weil man jede Zahl in einen Taschenrechner eingeben kann; der Rechner zeigt dann ihre vollständige Dezimaldarstellung mit allen Ziffern an.
:::
:::karte zusammenhang Anzeige des Taschenrechners
Warum beantwortet die Anzeige $1{,}414213562$ eines Taschenrechners nicht die Frage, ob es eine Zahl mit Quadrat genau 2 gibt?
---
Weil die Anzeige ein Bruch ist, dessen Quadrat nicht genau 2 ist. Ob es eine solche Zahl gibt, entscheidet die Vollständigkeit: in $\mathbb{Q}$ nicht, in $\mathbb{R}$ ja.
--- falsch
Weil der Rechner zu wenige Stellen zeigt; mit zwanzig Stellen wäre die Anzeige genau $\sqrt2$, und ihr Quadrat wäre dann auch genau gleich 2.
--- falsch
Weil der Rechner mit Brüchen gar nicht rechnen kann; sein Ergebnis ist deshalb immer eine irrationale Zahl, deren Quadrat genau 2 ist.
--- falsch
Die Anzeige beantwortet die Frage durchaus: Ihr Quadrat ist genau 2, also gibt es eine solche Zahl schon unter den Brüchen in $\mathbb{Q}$.
:::
::::
