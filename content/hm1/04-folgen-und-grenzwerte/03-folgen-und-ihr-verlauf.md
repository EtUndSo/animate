---
title: Stufe 1: Folgen und ihr Verlauf
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240300
summary: Ein Grenzwert braucht etwas, das sich einem Wert nähert.
tags: Zahlenfolge, Folgenglieder, Index, Wertemenge, monoton wachsend, streng monoton wachsend, monoton fallend, streng monoton fallend
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Grenzwert braucht etwas, das sich einem Wert nähert. Diese Stufe legt fest, was eine Folge ist, und beschreibt ihren Verlauf mit den Begriffen aus [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html).
:::

**Die Idee.** Eine Folge ist eine nummerierte Liste ohne Ende: Jeder Platz $n$ bekommt genau eine Zahl. Eine Zuordnung, die jedem Eingang genau einen Wert gibt, ist eine Funktion ([Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)), hier mit natürlichen Zahlen als Eingang. Deshalb besteht ihr Graph aus einzelnen Punkten, zwischen den Plätzen gibt es nichts (Abb. [1](#abb-1)).

:::definition Definition 1.1 (Folge)
<span class="anker" id="satz-1-1"></span>

Eine __Zahlenfolge__ ist eine auf $\mathbb{N}$ (oder auf $\mathbb{N}_0$ oder einer unendlichen Teilmenge von $\mathbb{N}_0$) definierte reellwertige Funktion

$$f:\ \mathbb{N}\to\mathbb{R},\qquad n\mapsto f(n)=:f_n.$$

Man schreibt $\{f_n\}_{n\in\mathbb{N}}$, $\{f_n\}_{n=1}^\infty$ oder kurz $\{f_n\}$. Die Zahlen $f_n$ heißen __Folgenglieder__.
:::

⁠**So liest man das:** $n$ ist der __Index__, die Platznummer. $f_n$ ist die Zahl auf diesem Platz. Die Menge aller vorkommenden Zahlen heißt __Wertemenge__ $\mathcal W(f_n):=\{f_n:n\in\mathbb{N}\}$.

:::frage Ist $\{f_n\}$ nicht dasselbe wie die Wertemenge?
Nein. Die Klammer meint hier die Liste mit ihrer Reihenfolge. Die Folge $(-1)^n$ hat unendlich viele Glieder, ihre Wertemenge nur die zwei Elemente $-1$ und $1$.
:::

:::definition Definition 1.2 (Monotone und beschränkte Folgen)
<span class="anker" id="satz-1-2"></span>

Eine Folge heißt monoton wachsend, nach unten beschränkt und so weiter, wenn die zugehörige Funktion $f$ diese Eigenschaft hat. Für Folgen bedeutet das:

<ul>

<li>

__monoton wachsend__: $a_n\le a_{n+1}$ für alle $n$; __streng monoton wachsend__: $a_n<a_{n+1}$; __monoton fallend__: $a_n\ge a_{n+1}$; __streng monoton fallend__: $a_n>a_{n+1}$;

</li>

<li>

__nach oben beschränkt__: $a_n\le S$ für alle $n$ mit einem festen $S\in\mathbb{R}$; __nach unten beschränkt__: $R\le a_n$ für alle $n$ mit einem festen $R\in\mathbb{R}$; __beschränkt__: beides zugleich, also $|a_n|\le M$ für alle $n$ mit einem festen $M$.

</li>

</ul>
:::

⁠**So liest man das:** Für Funktionen verlangt Monotonie den Vergleich beliebiger Stellen $x<y$. Auf $\mathbb{N}$ genügt der Vergleich von Nachbarn, weil man von $n$ in Einerschritten zu jedem größeren $m$ kommt. Beschränkt heißt: Der Graph liegt in einem waagerechten Streifen. Die Pendelfolge ist beschränkt ($-1\le a_n\le3{,}5$), aber nicht monoton. Die Summenfolge ist streng monoton wachsend und durch 2 beschränkt. Die Folge $n^2$ ist streng monoton wachsend und unbeschränkt.

:::abbildung hm1/k4folgen 1
Oben die ersten Glieder der Pendelfolge und der Summenfolge als Punkte über dem Index, gestrichelt der Wert 2. Unten dieselben Glieder auf der Zahlengeraden: Der Index ist nicht mehr zu sehen, aber die Häufung bei 2.
:::

**Die geometrische Summe.** Viele Folgen entstehen durch Aufsummieren, darunter die Summenfolge.

:::satz Satz 1.3 (Geometrische Summe)
<span class="anker" id="satz-1-3"></span>

Für $q\in\mathbb{R}$ heißt die Folge $s_n:=\sum_{k=0}^nq^k=1+q+q^2+\dots+q^n$, $n\in\mathbb{N}_0$, __geometrische Summe__. Es gilt

<span class="anker" id="gl-1-1"></span>
$$s_n=\begin{cases}\dfrac{1-q^{n+1}}{1-q},&q\ne1,\\[2mm]n+1,&q=1.\end{cases} \tag{1.1}$$
:::

⁠**So liest man das:** $q$ ist das Verhältnis benachbarter Summanden, der Summand mit $k=0$ ist immer 1. Es gibt $n+1$ Summanden. Die Formel ersetzt $n+1$ Additionen durch eine Division.

:::beweis Teleskopsumme
Für $q=1$ stehen $n+1$ Einsen da. Für $q\ne1$ multipliziert man mit $1-q$:

$$(1-q)\,s_n=\sum_{k=0}^n\bigl(q^k-q^{k+1}\bigr)=(1-q)+(q-q^2)+\dots+(q^n-q^{n+1})=1-q^{n+1}.$$

Jede Potenz $q,\dots,q^n$ kommt einmal mit Plus und einmal mit Minus vor, nur der Anfang 1 und das Ende $q^{n+1}$ bleiben (eine __Teleskopsumme__). Teilen durch $1-q\ne0$ ergibt [(1.1)](#gl-1-1).
:::

⁠**Verlauf.** Für $q>0$ ist $s_{n+1}=s_n+q^{n+1}>s_n$: Die Folge wächst streng monoton. Für $q\ge1$ ist jeder Summand mindestens 1, also $s_n\ge n+1$, und die Folge ist unbeschränkt. Für $0<q<1$ ist $q^{n+1}>0$, also $0<s_n<\frac1{1-q}$, und die Folge ist beschränkt.

::::beispiel
Für $q=\frac12$ ergibt [(1.1)](#gl-1-1) die Summenfolge in geschlossener Form: $s_n=2\bigl(1-(\frac12)^{n+1}\bigr)=2-(\frac12)^n$, zum Beispiel $s_{10}=2047/1024=1{,}99902$. Der Rest $2-s_n=(\frac12)^n$ halbiert sich in jedem Schritt.
::::

⁠**Grenzfälle:** Für $q=0$ ist $s_n=1$. Für $q$ nahe 1 geht die Formel in $n+1$ über: $q=1{,}001$ und $n=9$ ergeben $10{,}05$ statt 10.

:::aufgabe Aufgabe 1 ★ Geometrische Summen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $s_5$ für $q=\frac34$ als Bruch und vergleiche mit der Schranke $\frac1{1-q}$.

</li>

<li>

Schreibe für $q=-\frac12$ die Glieder $s_0$ bis $s_5$ auf. Ist die Folge monoton? Ist sie beschränkt?

</li>

<li>

Sage vorher, was für $q=-1$ passiert, und prüfe es mit [(1.1)](#gl-1-1).

</li>

</ol>

:::loesung
(a) $s_5=\dfrac{1-(3/4)^6}{1/4}=4\bigl(1-\frac{729}{4096}\bigr)=\frac{3367}{1024}=3{,}288$, unter der Schranke $\frac1{1-q}=4$. (b) $s_0,\dots,s_5=1;\ \frac12;\ \frac34;\ \frac58;\ \frac{11}{16};\ \frac{21}{32}$. Die Folge springt auf und ab, sie ist nicht monoton. Beschränkt ist sie: Aus [(1.1)](#gl-1-1) folgt $s_n=\frac23\bigl(1-(-\frac12)^{n+1}\bigr)$, also $\frac12\le s_n\le1$. (c) Die Summanden $+1$ und $-1$ heben sich paarweise auf: $s_n=1$ für gerade $n$, $s_n=0$ für ungerade $n$. Die Formel gibt $s_n=\frac12\bigl(1-(-1)^{n+1}\bigr)$, dasselbe.
:::
:::

::::formelsammlung
**Zahlenfolge**

$$f:\ \mathbb{N}\to\mathbb{R},\qquad n\mapsto f(n)=:f_n$$

Auch auf $\mathbb{N}_0$ oder einer unendlichen Teilmenge von $\mathbb{N}_0$ definiert. Geschrieben $\{f_n\}_{n\in\mathbb{N}}$, $\{f_n\}_{n=1}^\infty$ oder kurz $\{f_n\}$; $n$ ist der Index, die $f_n$ sind die Folgenglieder.

**Wertemenge**

$$\mathcal W(f_n):=\{f_n:n\in\mathbb{N}\}$$

Die Menge der vorkommenden Zahlen, ohne Reihenfolge; nicht dasselbe wie die Folge.

**Monoton wachsend und monoton fallend**

$$a_n\le a_{n+1},\qquad a_n\ge a_{n+1}$$

Jeweils für alle $n$. Auf $\mathbb{N}$ genügt der Vergleich von Nachbarn, weil man in Einerschritten zu jedem größeren Index kommt.

**Streng monoton wachsend und streng monoton fallend**

$$a_n<a_{n+1},\qquad a_n>a_{n+1}$$

Jeweils für alle $n$; gleiche Nachbarglieder sind ausgeschlossen.

**Nach oben beschränkt, nach unten beschränkt, beschränkt**

$$a_n\le S,\qquad R\le a_n,\qquad|a_n|\le M$$

Jeweils für alle $n$ mit festen $S,R,M\in\mathbb{R}$; beschränkt heißt beides zugleich. Der Graph liegt dann in einem waagerechten Streifen.

**Geometrische Summe**

$$s_n=\begin{cases}\dfrac{1-q^{n+1}}{1-q},&q\ne1,\\[2mm]n+1,&q=1.\end{cases}$$

Für $s_n:=\sum_{k=0}^nq^k=1+q+q^2+\dots+q^n$, $q\in\mathbb{R}$, $n\in\mathbb{N}_0$; es gibt $n+1$ Summanden. Herleitung als Teleskopsumme über $(1-q)\,s_n=1-q^{n+1}$.

**Verlauf der geometrischen Summe**

$$s_{n+1}=s_n+q^{n+1}>s_n\ \ (q>0),\qquad0<s_n<\frac1{1-q}\ \ (0<q<1)$$

Für $q>0$ streng monoton wachsend; für $q\ge1$ ist $s_n\ge n+1$, also unbeschränkt, für $0<q<1$ beschränkt.

**Summenfolge**

$$s_n=2\bigl(1-(\frac12)^{n+1}\bigr)=2-(\frac12)^n$$

Die geometrische Summe für $q=\frac12$; der Rest $2-s_n=(\frac12)^n$ halbiert sich in jedem Schritt.
::::

::::lernkarten
:::karte begriff Folge und Zahlenfolge
Was ist eine Zahlenfolge, als Funktion betrachtet, und auf welchen Mengen darf sie definiert sein?
---
Eine reellwertige Funktion $f:\ \mathbb{N}\to\mathbb{R}$, $n\mapsto f(n)=:f_n$, definiert auf $\mathbb{N}$, auf $\mathbb{N}_0$ oder auf einer unendlichen Teilmenge von $\mathbb{N}_0$. Man schreibt $\{f_n\}_{n\in\mathbb{N}}$ oder kurz $\{f_n\}$.
--- falsch
Eine reellwertige Funktion $f:\mathbb{R}\to\mathbb{R}$, deren Werte man nur an den Stellen $n\in\mathbb{N}$ abliest; zwischen diesen Stellen verläuft ihr Graph als durchgehende Kurve. Man schreibt $\{f_n\}$.
--- falsch
Eine endliche, nummerierte Liste reeller Zahlen $f_1,\dots,f_N$, in der jeder Platz genau eine Zahl bekommt; definiert auf $\{1,\dots,N\}$. Man schreibt $\{f_n\}_{n=1}^N$ oder kurz $\{f_n\}$.
--- falsch
Die Menge $\{f_n:n\in\mathbb{N}\}$ der vorkommenden Zahlen, ohne Reihenfolge, definiert auf $\mathbb{N}$ oder $\mathbb{N}_0$; jede Zahl zählt nur einmal, auch wenn sie mehrfach vorkommt. Man schreibt $\{f_n\}$.
:::
:::karte begriff Folgenglieder und Index
Was bezeichnen bei einer Folge $\{f_n\}$ der Index $n$ und die Folgenglieder $f_n$?
---
Der Index $n$ ist die Platznummer in der Liste, $f_n$ die Zahl auf diesem Platz. Die Zahlen $f_n$ heißen Folgenglieder.
--- falsch
Der Index $n$ ist die Zahl auf einem Platz, $f_n$ die zugehörige Platznummer. Die Platznummern $f_n$ heißen Folgenglieder.
--- falsch
Der Index $n$ gibt an, wie viele Glieder die Folge insgesamt hat; die Folgenglieder $f_n$ sind die verschiedenen Zahlen, die vorkommen.
--- falsch
Der Index $n$ ist die Platznummer; die Folgenglieder sind die Paare $(n,f_n)$ aus Platz und Zahl, also die Punkte des Graphen.
:::
:::karte begriff Wertemenge
Was ist die Wertemenge einer Folge $\{f_n\}$, und warum ist sie nicht dasselbe wie die Folge selbst?
---
Die Menge aller vorkommenden Zahlen, $\mathcal W(f_n):=\{f_n:n\in\mathbb{N}\}$. Die Folge ist dagegen die Liste mit Reihenfolge: $(-1)^n$ hat unendlich viele Glieder, ihre Wertemenge nur die Elemente $-1$ und $1$.
--- falsch
Die Menge der Indizes, an denen die Folge nicht verschwindet, $\mathcal W(f_n):=\{n\in\mathbb{N}:f_n\ne0\}$. Bei $(-1)^n$ ist das ganz $\mathbb{N}$, sie ist also so groß wie die Folge selbst und doch keine Liste.
--- falsch
Die Menge aller vorkommenden Zahlen, $\mathcal W(f_n):=\{f_n:n\in\mathbb{N}\}$. Sie ist dasselbe wie die Folge, denn die Schreibweise $\{f_n\}$ meint genau diese Menge, ohne Reihenfolge und Wiederholungen.
--- falsch
Das Intervall zwischen dem kleinsten und dem größten Glied. Für $(-1)^n$ ist das $[-1,1]$; die Folge selbst enthält dagegen nur die beiden Zahlen $-1$ und $1$, aber diese unendlich oft.
:::
:::karte zusammenhang Monotonie, monoton wachsend und monoton fallend
Warum genügt es bei einer Folge, benachbarte Glieder zu vergleichen, um ihre Monotonie zu zeigen, also dass sie monoton wachsend oder monoton fallend ist?
---
Weil man auf $\mathbb{N}$ von $n$ in Einerschritten zu jedem größeren $m$ kommt: Aus $a_n\le a_{n+1}$ für alle $n$ folgt $a_n\le a_m$ für alle $n<m$, ebenso bei $\ge$. Bei Funktionen muss man beliebige Stellen $x<y$ vergleichen.
--- falsch
Weil die Definition für Folgen nur Nachbarn betrifft: Weiter voneinander entfernte Glieder dürfen in der falschen Reihenfolge stehen, etwa $a_1>a_3$ bei einer monoton wachsenden Folge, solange alle Nachbarn passen.
--- falsch
Weil zwischen zwei Plätzen nur endlich viele Glieder liegen und man deshalb alle Paare ausprobieren kann; bei Funktionen auf $\mathbb{R}$ ist das nicht möglich, dort genügt umgekehrt der Vergleich benachbarter Stellen.
--- falsch
Weil benachbarte Glieder einer Folge immer den kleinsten Abstand voneinander haben: Ist dieser Abstand positiv, sind alle anderen Abstände größer und damit ebenfalls positiv, die Folge wächst also überall.
:::
:::karte zusammenhang streng monoton wachsend und streng monoton fallend
Was unterscheidet bei Folgen streng monoton wachsend und streng monoton fallend von der einfachen Monotonie, gemessen an benachbarten Gliedern?
---
Streng verlangt echte Ungleichungen, $a_n<a_{n+1}$ bzw. $a_n>a_{n+1}$ für alle $n$; gleiche Nachbarglieder sind verboten. Die einfache Monotonie erlaubt sie: $a_n\le a_{n+1}$ bzw. $a_n\ge a_{n+1}$.
--- falsch
Streng verlangt, dass die Folge unbeschränkt ist: Eine streng monoton wachsende Folge wächst über jede Schranke, eine streng monoton fallende sinkt unter jede; sonst heißt sie nur monoton.
--- falsch
Streng verlangt die Ungleichung nur für Nachbarn, $a_n<a_{n+1}$; die einfache Monotonie verlangt dagegen $a_n\le a_m$ für alle $n<m$ und ist deshalb die stärkere der beiden Bedingungen.
--- falsch
Streng verlangt gleich große Schritte, $a_{n+1}-a_n=d$ mit festem $d>0$ bzw. $d<0$; bei der einfachen Monotonie dürfen die Schritte verschieden groß sein und auch einmal null.
:::
:::karte zusammenhang nach oben beschränkt, nach unten beschränkt und beschränkt
Was bedeutet es für eine Folge, nach oben beschränkt, nach unten beschränkt und beschränkt zu sein, und wie sieht das am Graphen aus?
---
Nach oben beschränkt: $a_n\le S$ für alle $n$ mit festem $S\in\mathbb{R}$; nach unten beschränkt: $R\le a_n$ für alle $n$ mit festem $R\in\mathbb{R}$. Beschränkt heißt beides, also $|a_n|\le M$ mit festem $M$: Der Graph liegt in einem waagerechten Streifen.
--- falsch
Nach oben beschränkt: Zu jedem $n$ gibt es ein $S$ mit $a_n\le S$; nach unten beschränkt entsprechend mit $R\le a_n$. Beschränkt heißt beides; das trifft auf jede Folge zu, weil jedes Glied selbst eine solche Zahl ist.
--- falsch
Nach oben beschränkt: $a_n\le S$ für alle $n$ mit festem $S$; nach unten beschränkt: $R\le a_n$. Beschränkt heißt, dass eines von beiden gilt, also $a_n\le M$ oder $a_n\ge-M$: Der Graph liegt auf einer Seite einer Waagerechten.
--- falsch
Nach oben beschränkt: Die Indizes $n$ sind durch ein festes $S$ begrenzt; nach unten beschränkt: durch ein festes $R$. Beschränkt heißt beides: Die Folge hat nur endlich viele Glieder, ihr Graph liegt in einem senkrechten Streifen.
:::
:::karte zusammenhang beschränkt, aber nicht monoton
Kann eine Folge beschränkt sein, ohne monoton zu sein, und kann sie streng monoton wachsend sein, ohne beschränkt zu sein?
---
Ja, beides kommt vor: Die Pendelfolge ist beschränkt, $-1\le a_n\le3{,}5$, aber nicht monoton; $n^2$ ist streng monoton wachsend und unbeschränkt. Die Summenfolge hat beide Eigenschaften.
--- falsch
Nein. Jede beschränkte Folge ist ab einem Index monoton, weil sie im Streifen nicht ewig auf und ab springen kann; und jede streng monoton wachsende Folge ist beschränkt.
--- falsch
Nur das Erste: Die Pendelfolge ist beschränkt und nicht monoton. Streng monoton wachsende Folgen sind dagegen immer beschränkt, weil ihr erstes Glied sie nach unten begrenzt.
--- falsch
Nur das Zweite: $n^2$ ist streng monoton wachsend und unbeschränkt. Eine beschränkte Folge ist dagegen immer monoton, wie die Summenfolge, die nur wächst und unter 2 bleibt.
:::
:::karte zusammenhang Graph einer Folge
Warum besteht der Graph einer Folge aus einzelnen Punkten und nicht aus einer durchgehenden Kurve?
---
Weil eine Folge eine Funktion mit natürlichen Zahlen als Eingang ist: Jeder Platz $n$ bekommt genau eine Zahl, und zwischen den Plätzen gibt es nichts, was einen Wert bekommen könnte.
--- falsch
Weil man nur endlich viele Glieder zeichnen kann; die Folge selbst hat auch zwischen den Plätzen Werte, die man erhält, wenn man benachbarte Punkte geradlinig verbindet.
--- falsch
Weil die Glieder einer Folge springen dürfen: Ein durchgehender Graph ist nur bei monotonen Folgen möglich, bei denen man benachbarte Glieder ohne Sprung verbinden kann.
--- falsch
Weil eine Folge keine Funktion ist, sondern eine Menge von Zahlen; ihr Graph zeigt deshalb nur, welche Zahlen vorkommen, nicht aber, an welchem Platz sie stehen.
:::
:::karte formel geometrische Summe
Wie lautet die geschlossene Form der geometrischen Summe $s_n=\sum_{k=0}^nq^k$, und welche Fälle muss man unterscheiden?
---
$s_n=\frac{1-q^{n+1}}{1-q}$ für $q\ne1$ und $s_n=n+1$ für $q=1$. Es gibt $n+1$ Summanden, der mit $k=0$ ist immer 1.
--- falsch
$s_n=\frac{1-q^{n}}{1-q}$ für $q\ne1$ und $s_n=n$ für $q=1$. Es gibt $n$ Summanden, der erste davon ist $q$.
--- falsch
$s_n=\frac{1-q^{n+1}}{1-q}$ für alle $q\in\mathbb{R}$; für $q=1$ kürzt man den Bruch und erhält ebenfalls $n+1$, ohne Sonderfall.
--- falsch
$s_n=\frac{q^{n+1}-1}{1-q}$ für $q\ne1$ und $s_n=n+1$ für $q=1$. Es gibt $n+1$ Summanden, der mit $k=0$ ist immer 1.
:::
:::karte herleitung Teleskopsumme
Wie leitet man die geschlossene Form der geometrischen Summe $s_n=\sum_{k=0}^nq^k$ her, und was bleibt dabei von der Teleskopsumme übrig?
---
Für $q=1$ stehen $n+1$ Einsen da, also $s_n=n+1$, weil $1^k=1$ für jedes $k$ gilt.
---
Für $q\ne1$ multipliziert man mit $1-q$, weil dann jeder Summand $q^k$ zu $q^k-q^{k+1}$ wird: $(1-q)\,s_n=\sum_{k=0}^n\bigl(q^k-q^{k+1}\bigr)$.
---
Ausgeschrieben steht $(1-q)+(q-q^2)+\dots+(q^n-q^{n+1})$; die Potenzen $q,\dots,q^n$ heben sich weg, weil jede einmal mit Plus und einmal mit Minus vorkommt.
---
Übrig bleiben nur der Anfang 1 und das Ende $q^{n+1}$, also $(1-q)\,s_n=1-q^{n+1}$, weil eine Teleskopsumme nur ihr erstes und ihr letztes Glied behält.
---
Teilen durch $1-q$ ergibt $s_n=\frac{1-q^{n+1}}{1-q}$, weil $1-q\ne0$ für $q\ne1$ gilt.
:::
:::karte zusammenhang Verlauf der geometrischen Summe
Für welche $q>0$ ist die geometrische Summe beschränkt, für welche unbeschränkt, und woran liegt das?
---
Für $q>0$ wächst sie streng monoton, weil $s_{n+1}=s_n+q^{n+1}>s_n$. Für $q\ge1$ ist jeder Summand mindestens 1, also $s_n\ge n+1$: unbeschränkt. Für $0<q<1$ ist $q^{n+1}>0$, also $0<s_n<\frac1{1-q}$: beschränkt.
--- falsch
Für alle $q>0$ ist sie unbeschränkt, weil sie streng monoton wächst, $s_{n+1}=s_n+q^{n+1}>s_n$: Eine Summe aus lauter positiven Summanden übersteigt mit jedem Schritt mehr und schließlich jede Schranke.
--- falsch
Beschränkt ist sie für $q>1$, weil dann $1-q^{n+1}$ und $1-q$ beide negativ sind und sich der Bruch auf $\frac1{q-1}$ einpendelt. Für $0<q\le1$ wächst sie ohne Grenze, weil die Summanden zu langsam schrumpfen.
--- falsch
Für $q>0$ wächst sie streng monoton. Für $q\ge1$ ist sie unbeschränkt; für $0<q<1$ ist sie durch 1 beschränkt, weil jeder Summand $q^k$ kleiner als 1 ist und die Summe deshalb unter 1 bleibt.
:::
:::karte formel Summenfolge
Welche geschlossene Form hat die Summenfolge $s_n=\sum_{k=0}^n(\frac12)^k$, und wie verhält sich ihr Rest bis 2?
---
$s_n=2\bigl(1-(\frac12)^{n+1}\bigr)=2-(\frac12)^n$. Der Rest $2-s_n=(\frac12)^n$ halbiert sich in jedem Schritt; die 2 wird nie erreicht.
--- falsch
$s_n=2\bigl(1-(\frac12)^{n}\bigr)=2-2(\frac12)^n$. Der Rest $2-s_n$ halbiert sich in jedem Schritt; ab $n=10$ ist die 2 exakt erreicht.
--- falsch
$s_n=2-\frac1n$. Der Rest $2-s_n=\frac1n$ schrumpft in jedem Schritt um denselben Betrag; die 2 wird nie erreicht, weil $\frac1n$ nie null ist.
--- falsch
$s_n=2\bigl(1+(\frac12)^{n+1}\bigr)=2+(\frac12)^n$. Der Abstand $s_n-2=(\frac12)^n$ halbiert sich in jedem Schritt; die Folge nähert sich der 2 von oben.
:::
::::
