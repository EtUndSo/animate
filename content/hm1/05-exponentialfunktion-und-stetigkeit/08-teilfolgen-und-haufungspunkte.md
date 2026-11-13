---
title: Stufe 6: Teilfolgen und Häufungspunkte
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250800
summary: Beschränkte Folgen müssen nicht konvergieren.
tags: Teilfolge, Limes superior, Limes inferior, uneigentlicher Häufungspunkt
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Beschränkte Folgen müssen nicht konvergieren. Der Satz vom Maximum braucht aber einen Grenzpunkt. Diese Stufe zeigt: Eine Auswahl der Glieder konvergiert immer.
:::

**Die Idee.** $(-1)^n$ konvergiert nicht, die geraden Glieder aber schon. Halbiert man ein beschränktes Intervall, liegen in mindestens einer Hälfte unendlich viele Glieder. Weiterhalbieren schließt eine Stelle ein, um die sie sich drängen.

:::definition Definition 6.1 (Teilfolge)
<span class="anker" id="satz-6-1"></span>

Sei $\{x_n\}_{n=1}^\infty$ eine Folge reeller Zahlen und $\{n_k\}_{k=1}^\infty$ eine streng monoton wachsende Folge mit $n_k\in\mathbb{N}$. Dann heißt $\{x_{n_k}\}_{k=1}^\infty$, also $x_{n_1},x_{n_2},\dots$, eine __Teilfolge__ von $\{x_n\}$.
:::

:::definition Definition 6.2 (Häufungspunkt)
<span class="anker" id="satz-6-2"></span>

<ol class="rm">

<li>

$x_0\in\mathbb{R}$ heißt Häufungspunkt der Folge $\{x_n\}$, wenn in jeder Umgebung $U_\varepsilon(x_0)$, $\varepsilon>0$, unendlich viele Folgenglieder liegen.

</li>

<li>

Sei $M\subset\mathbb{R}$. $x_0\in\mathbb{R}$ heißt Häufungspunkt der Menge $M$, wenn jede punktierte Umgebung $\dot U_\varepsilon(x_0)$ unendlich viele Elemente von $M$ enthält.

</li>

</ol>
:::

⁠**So liest man das:** $n_k$ wählt aus, die Reihenfolge bleibt, und es ist $n_k\ge k$. Beim Grenzwert liegen *alle bis auf endlich viele* Glieder im Schlauch, beim Häufungspunkt nur *unendlich viele*. Ein Wert muss dabei gar nicht angenommen werden. In (i) zählt ein Wert mehrfach, weil die Glieder Plätze haben, in (ii) zählt jedes Element einmal. Endlich viele Glieder ändern wie beim Grenzwert nichts. Für (ii) reicht schon *ein* Element in jeder punktierten Umgebung: Zu einem Element $m$ nimmt man $\tilde\varepsilon=\frac12|m-x_0|$ und findet ein weiteres, und so fort. Gleichbedeutend: Es gibt eine Folge in $M\setminus\{x_0\}$, die gegen $x_0$ läuft.

::::beispiel [Beispiele]
$q_n=(-1)^n\frac n{n+1}$, also $-\frac12;\ \frac23;\ -\frac34;\ \frac45;\ \dots$, hat die Häufungspunkte $\pm1$, die Menge $\{q_n\}$ ebenso. Auch die Folge $(-1)^n$ hat sie, ihre Wertemenge $\{-1,1\}$ aber nicht: Endliche Mengen haben keinen Häufungspunkt. Die Menge $[0,1]\cap\mathbb{Q}$ hat jeden Punkt von $[0,1]$ als Häufungspunkt, denn jedes Intervall enthält Brüche.
::::

:::satz Satz 6.3 (Häufungspunkte und Teilfolgen)
<span class="anker" id="satz-6-3"></span>

Eine Folge $\{x_n\}$ besitzt genau dann den Häufungspunkt $x_0\in\mathbb{R}$, wenn es eine Teilfolge gibt, die gegen $x_0$ konvergiert.
:::

:::beweis Beide Richtungen
„$\Leftarrow$“: Konvergiert $x_{n_k}\to x_0$, liegen in jedem $U_\varepsilon(x_0)$ alle $x_{n_k}$ mit $k>N_0$, das sind unendlich viele Glieder. „$\Rightarrow$“: Wähle $n_1$ mit $x_{n_1}\in U_1(x_0)$. Weil in $U_{1/2}(x_0)$ unendlich viele Glieder liegen, gibt es dort eines mit $n_2>n_1$, und so fort: $n_{k+1}>n_k$ mit $|x_{n_{k+1}}-x_0|<\frac1{k+1}$. Das ergibt $|x_{n_k}-x_0|<\frac1k$, also $x_{n_k}\to x_0$.
:::

⁠**So liest man das:** Häufungspunkte sind genau die Grenzwerte von Teilfolgen. Für $q_n$ läuft $n_k=2k$ gegen $1$ und $n_k=2k-1$ gegen $-1$.

:::definition Definition 6.4 (Limes superior und Limes inferior)
<span class="anker" id="satz-6-4"></span>

Für eine Folge $\{x_n\}$ in $\mathbb{R}$ heißt der größte Häufungspunkt $x^*$ __Limes superior__, der kleinste Häufungspunkt $x_*$ __Limes inferior__:

<span class="anker" id="gl-6-1"></span>
$$\limsup_{n\to\infty}x_n=\varlimsup_{n\to\infty}x_n:=x^*,\qquad\liminf_{n\to\infty}x_n=\varliminf_{n\to\infty}x_n:=x_*. \tag{6.1}$$

Ist die Folge nicht nach oben beschränkt, heißt $x^*=\infty$ __uneigentlicher Häufungspunkt__, ist sie nicht nach unten beschränkt, ebenso $x_*=-\infty$.
:::

:::satz Satz 6.5 (Bolzano-Weierstraß)
<span class="anker" id="satz-6-5"></span>

Eine beschränkte Folge in $\mathbb{R}$ besitzt mindestens einen Häufungspunkt in $\mathbb{R}$, und damit eine konvergente Teilfolge. Es gibt auch einen kleinsten und einen größten Häufungspunkt.
:::

:::beweis Halbieren, das Unendliche behalten
Sei $a\le x_n\le b$ für alle $n$. Eine der Hälften $I_1=[a,\frac{a+b}2]$, $I_2=[\frac{a+b}2,b]$ enthält unendlich viele Folgenglieder. Setze $[a_1,b_1]:=I_1$, falls das für $I_1$ gilt, sonst $I_2$. Fortsetzen ergibt eine Intervallschachtelung, jedes $[a_n,b_n]$ mit unendlich vielen Gliedern, und $b_n-a_n=2^{-n}(b-a)\to0$. Sie enthält genau einen Punkt $x_0$. Jedes $U_\varepsilon(x_0)$ enthält ein ganzes $[a_{n},b_{n}]$, also unendlich viele Glieder. Damit ist $x_0$ Häufungspunkt, und Satz [6.3](#satz-6-3) liefert die Teilfolge.

Größter: Die Hülle $s_n:=\sup\{x_k:k\ge n\}$ aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) fällt und ist beschränkt, also existiert $s:=\lim s_n$. Sei $\varepsilon>0$. Ab einem $N$ ist $s_n<s+\varepsilon$, also liegen dort alle $x_k$ unter $s+\varepsilon$. Zu jedem $n$ gibt es wegen $s_n\ge s$ ein $k\ge n$ mit $x_k>s-\varepsilon$. Also liegen unendlich viele Glieder in $U_\varepsilon(s)$, und $s$ ist Häufungspunkt. Ist $y>s$ und $\varepsilon=\frac12(y-s)$, liegen in $U_\varepsilon(y)$ nur endlich viele Glieder. Also ist $s$ der größte. Für den kleinsten nimmt man die Infima.
:::

⁠**So liest man das:** Mit den uneigentlichen Häufungspunkten sind $\limsup x_n$ und $\liminf x_n$ für jede Folge in $\mathbb{R}\cup\{\pm\infty\}$ erklärt, und stets ist $x_*\le x^*$. Der Beweis zeigt für beschränkte Folgen

<span class="anker" id="gl-6-2"></span>
$$x^*=\lim_{n\to\infty}\bigl(\sup\{x_k:k\ge n\}\bigr),\qquad x_*=\lim_{n\to\infty}\bigl(\inf\{x_k:k\ge n\}\bigr). \tag{6.2}$$

Mit dem Hüllensatz aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) folgt für $a\in\mathbb{R}$ das Kriterium

<span class="anker" id="gl-6-3"></span>
$$\lim_{n\to\infty}x_n=a\quad\Longleftrightarrow\quad\limsup_{n\to\infty}x_n=\liminf_{n\to\infty}x_n=a. \tag{6.3}$$

Eine konvergente Folge hat also nur einen Häufungspunkt, und eine beschränkte Folge mit genau einem Häufungspunkt konvergiert. **Voraussetzung nötig:** $x_n=n$ ist unbeschränkt und hat in $\mathbb{R}$ keinen Häufungspunkt, nur $x^*=\infty$. **Grenzfall:** Für $r_n=n$ bei geradem, $r_n=\frac1n$ bei ungeradem $n$ ist $x_*=0$, $x^*=\infty$.

:::abbildung hm1/k5haeufung 6
Links $q_n$: Die Glieder mit geraden Indizes (blau) laufen gegen $x^*=1$, die mit ungeraden (orange) gegen $x_*=-1$. Rechts das Halbieren aus dem Beweis: Es bleibt die linke Hälfte, solange sie unendlich viele Glieder enthält.
:::

:::aufgabe Aufgabe 6 ★★ Häufungspunkte finden
<span class="anker" id="aufg-6"></span>

Sei $t_n=(n\bmod3)+\frac1n$, wobei $n\bmod3$ der Rest beim Teilen durch 3 ist. (a) Schreibe $t_1,\dots,t_6$ auf. (b) Gib alle Häufungspunkte mit je einer Teilfolge an. (c) Bestimme $\limsup t_n$ und $\liminf t_n$. Konvergiert die Folge? (d) Hat $\{t_n\}$ als Menge dieselben Häufungspunkte?

:::loesung
(a) $2;\ 2{,}5;\ 0{,}333;\ 1{,}25;\ 2{,}2;\ 0{,}167$. (b) Häufungspunkte 0, 1, 2 mit $n_k=3k$, $n_k=3k+1$, $n_k=3k+2$. Weitere gibt es nicht, denn jedes Glied liegt für großes $n$ nahe einem der drei Werte. (c) $\limsup t_n=2$, $\liminf t_n=0$. Keine Konvergenz nach [(6.3)](#gl-6-3). (d) Ja. Die Werte $t_n$ sind paarweise verschieden, also liegen in jeder punktierten Umgebung von 0, 1 und 2 unendlich viele Elemente der Menge.
:::
:::

::::formelsammlung
**Teilfolge**

$$\{x_{n_k}\}_{k=1}^\infty,\qquad n_k\in\mathbb{N}\ \text{streng monoton wachsend}$$

Die Reihenfolge bleibt, und $n_k\ge k$.

**Häufungspunkt**

$$x_{n_k}\to x_0$$

$x_0$ ist genau dann Häufungspunkt von $\{x_n\}$, wenn eine Teilfolge gegen $x_0$ konvergiert, also wenn in jeder Umgebung $U_\varepsilon(x_0)$ unendlich viele Folgenglieder liegen. Bei einer Menge $M$: Jede punktierte Umgebung $\dot U_\varepsilon(x_0)$ enthält unendlich viele Elemente von $M$.

**Limes superior und Limes inferior**

$$\limsup_{n\to\infty}x_n=\varlimsup_{n\to\infty}x_n:=x^*,\qquad\liminf_{n\to\infty}x_n=\varliminf_{n\to\infty}x_n:=x_*$$

Größter bzw. kleinster Häufungspunkt; stets $x_*\le x^*$. Nicht nach oben beschränkt: $x^*=\infty$, nicht nach unten beschränkt: $x_*=-\infty$ (uneigentliche Häufungspunkte).

**Bolzano-Weierstraß**

$$b_n-a_n=2^{-n}(b-a)\to0$$

Eine beschränkte Folge in $\mathbb{R}$ hat mindestens einen Häufungspunkt in $\mathbb{R}$ und damit eine konvergente Teilfolge, dazu einen kleinsten und einen größten. Beweis: Halbieren, die Hälfte mit unendlich vielen Gliedern behalten.

**Hüllen**

$$x^*=\lim_{n\to\infty}\bigl(\sup\{x_k:k\ge n\}\bigr),\qquad x_*=\lim_{n\to\infty}\bigl(\inf\{x_k:k\ge n\}\bigr)$$

Für beschränkte Folgen.

**Kriterium für Konvergenz**

$$\lim_{n\to\infty}x_n=a\quad\Longleftrightarrow\quad\limsup_{n\to\infty}x_n=\liminf_{n\to\infty}x_n=a$$

Für $a\in\mathbb{R}$: Eine konvergente Folge hat nur einen Häufungspunkt, eine beschränkte Folge mit genau einem Häufungspunkt konvergiert.
::::

::::lernkarten
:::karte begriff Teilfolge
Wie entsteht eine Teilfolge $\{x_{n_k}\}$ einer Folge $\{x_n\}$, und welche Bedingung müssen die Indizes $n_k$ erfüllen?
---
Man wählt mit einer streng monoton wachsenden Folge $\{n_k\}$ natürlicher Zahlen Glieder aus: $x_{n_1},x_{n_2},\dots$. Die Reihenfolge bleibt erhalten, und es ist $n_k\ge k$.
--- falsch
Man wählt beliebige Glieder in beliebiger Reihenfolge aus, auch mehrfach: $x_{n_1},x_{n_2},\dots$ mit irgendwelchen $n_k\in\mathbb{N}$; die Reihenfolge darf sich dabei ändern.
--- falsch
Man wählt endlich viele Glieder aus, etwa $x_1,\dots,x_{10}$: Die Teilfolge ist ein Anfangsstück der Folge, und die Indizes $n_k=k$ laufen bis zu einer festen Grenze.
--- falsch
Man wählt mit einer monoton wachsenden Folge $\{n_k\}$ Glieder aus, wobei $n_k=n_{k+1}$ erlaubt ist; ein Glied darf also mehrfach hintereinander vorkommen.
:::
:::karte begriff Häufungspunkt
Wann heißt $x_0\in\mathbb{R}$ Häufungspunkt einer Folge $\{x_n\}$, und worin unterscheidet sich das vom Grenzwert?
---
Wenn in jeder Umgebung $U_\varepsilon(x_0)$, $\varepsilon>0$, unendlich viele Folgenglieder liegen. Beim Grenzwert sind es dort alle bis auf endlich viele; angenommen werden muss $x_0$ nicht.
--- falsch
Wenn mindestens ein Folgenglied gleich $x_0$ ist. Beim Grenzwert müssen alle Glieder ab einem Index gleich $x_0$ sein, beim Häufungspunkt genügt ein einziges Glied mit diesem Wert.
--- falsch
Wenn in einer Umgebung $U_\varepsilon(x_0)$ unendlich viele Folgenglieder liegen. Beim Grenzwert gilt das für jede Umgebung, beim Häufungspunkt genügt dagegen eine einzige feste Umgebung.
--- falsch
Wenn in jeder Umgebung $U_\varepsilon(x_0)$ alle bis auf endlich viele Folgenglieder liegen. Das ist dasselbe wie beim Grenzwert; die beiden Wörter bezeichnen denselben Begriff.
:::
:::karte zusammenhang Häufungspunkt einer Menge
Wie ist der Häufungspunkt einer Menge $M\subset\mathbb{R}$ erklärt, und worin unterscheidet er sich vom Häufungspunkt einer Folge?
---
$x_0$ ist Häufungspunkt von $M$, wenn jede punktierte Umgebung $\dot U_\varepsilon(x_0)$ unendlich viele Elemente von $M$ enthält. In der Folge zählt ein Wert mehrfach, in der Menge nur einmal: $(-1)^n$ hat die Häufungspunkte $\pm1$, die Menge $\{-1,1\}$ keinen.
--- falsch
$x_0$ ist Häufungspunkt von $M$, wenn jede Umgebung $U_\varepsilon(x_0)$ ein Element von $M$ enthält, wobei $x_0$ selbst mitzählt. Damit ist jedes Element ein Häufungspunkt, und $\{-1,1\}$ hat dieselben Häufungspunkte $\pm1$ wie die Folge $(-1)^n$.
--- falsch
$x_0$ ist Häufungspunkt von $M$, wenn jede punktierte Umgebung $\dot U_\varepsilon(x_0)$ unendlich viele Elemente von $M$ enthält. Ein Unterschied zur Folge besteht nicht: Die Folge $(-1)^n$ und die Menge $\{-1,1\}$ haben beide die Häufungspunkte $\pm1$.
--- falsch
$x_0$ ist Häufungspunkt von $M$, wenn $x_0$ das Supremum oder das Infimum von $M$ ist. Bei der Folge zählt dagegen jeder Wert, der unendlich oft vorkommt; so haben $(-1)^n$ und $\{-1,1\}$ beide die Häufungspunkte $\pm1$.
:::
:::karte formel Häufungspunkte und Teilfolgen
Wie hängen die Häufungspunkte einer Folge mit ihren Teilfolgen zusammen?
---
Eine Folge $\{x_n\}$ besitzt genau dann den Häufungspunkt $x_0\in\mathbb{R}$, wenn es eine Teilfolge gibt, die gegen $x_0$ konvergiert: Häufungspunkte sind genau die Grenzwerte von Teilfolgen.
--- falsch
Jeder Häufungspunkt ist Grenzwert der ganzen Folge, und Teilfolgen haben dieselben Häufungspunkte wie die Folge; man braucht sie nur, um Häufungspunkte schneller zu finden.
--- falsch
Ist $x_0$ Grenzwert einer Teilfolge, dann ist $x_0$ Häufungspunkt; umgekehrt muss es zu einem Häufungspunkt aber keine Teilfolge geben, die gegen ihn konvergiert.
--- falsch
Eine Folge hat genau dann den Häufungspunkt $x_0$, wenn alle ihre Teilfolgen gegen $x_0$ konvergieren: Häufungspunkte sind die gemeinsamen Grenzwerte aller Teilfolgen.
:::
:::karte herleitung Teilfolge zu einem Häufungspunkt
Wie konstruiert man zu einem Häufungspunkt $x_0$ einer Folge eine Teilfolge, die gegen $x_0$ konvergiert?
---
Man wählt $n_1$ mit $x_{n_1}\in U_1(x_0)$, weil in jeder Umgebung von $x_0$ Folgenglieder liegen.
---
In $U_{1/2}(x_0)$ liegen unendlich viele Glieder, also gibt es dort eines mit $n_2>n_1$, weil nur endlich viele Indizes höchstens $n_1$ sind.
---
So fährt man fort: $n_{k+1}>n_k$ mit $|x_{n_{k+1}}-x_0|<\frac1{k+1}$, weil jede Umgebung $U_{1/(k+1)}(x_0)$ unendlich viele Glieder enthält.
---
Das ergibt $|x_{n_k}-x_0|<\frac1k$, also $x_{n_k}\to x_0$, weil $\frac1k$ eine Nullfolge ist.
:::
:::karte begriff Limes superior und Limes inferior
Was bezeichnen Limes superior und Limes inferior einer Folge $\{x_n\}$ in $\mathbb{R}$?
---
Der Limes superior $\limsup_{n\to\infty}x_n:=x^*$ ist der größte Häufungspunkt, der Limes inferior $\liminf_{n\to\infty}x_n:=x_*$ der kleinste. Stets ist $x_*\le x^*$.
--- falsch
Der Limes superior ist das größte Folgenglied, der Limes inferior das kleinste; beide werden also von der Folge angenommen. Stets ist $\liminf x_n\le\limsup x_n$.
--- falsch
Der Limes superior ist das Supremum $\sup\{x_n:n\in\mathbb{N}\}$ der Wertemenge, der Limes inferior ihr Infimum. Stets ist $\liminf x_n\le\limsup x_n$.
--- falsch
Der Limes superior ist der Grenzwert der Glieder mit geraden Indizes, der Limes inferior der Grenzwert der Glieder mit ungeraden Indizes. Beide gibt es für jede Folge.
:::
:::karte begriff uneigentlicher Häufungspunkt
Was ist ein uneigentlicher Häufungspunkt, und welchen Limes superior hat die unbeschränkte Folge $x_n=n$?
---
Ist eine Folge nicht nach oben beschränkt, setzt man $x^*=\infty$, einen uneigentlichen Häufungspunkt; nicht nach unten beschränkt entsprechend $x_*=-\infty$. $x_n=n$ hat in $\mathbb{R}$ keinen Häufungspunkt, nur $x^*=\infty$.
--- falsch
Ein Häufungspunkt, der von der Folge nicht angenommen wird, etwa $1$ bei $q_n=(-1)^n\frac n{n+1}$. $x_n=n$ hat dagegen gar keinen Limes superior, weil sie keinen Häufungspunkt in $\mathbb{R}$ besitzt.
--- falsch
Ein Häufungspunkt, in dessen Umgebungen nur endlich viele Glieder liegen. $x_n=n$ hat jede natürliche Zahl als uneigentlichen Häufungspunkt, ihr Limes superior ist deshalb nicht erklärt.
--- falsch
Ein Häufungspunkt, der auf dem Rand eines Intervalls liegt, etwa $1$ für Folgen in $[0,1]$. $x_n=n$ hat in $\mathbb{R}$ keinen Häufungspunkt und deshalb auch keinen Limes superior, auch keinen uneigentlichen.
:::
:::karte formel Bolzano-Weierstraß
Was garantiert der Satz von Bolzano-Weierstraß für eine beschränkte Folge in $\mathbb{R}$?
---
Sie besitzt mindestens einen Häufungspunkt in $\mathbb{R}$ und damit eine konvergente Teilfolge. Es gibt auch einen kleinsten und einen größten Häufungspunkt.
--- falsch
Sie konvergiert: Eine beschränkte Folge kann nicht ewig zwischen den Schranken hin- und herspringen und besitzt deshalb einen Grenzwert in $\mathbb{R}$.
--- falsch
Sie besitzt mindestens einen Häufungspunkt in $\mathbb{R}$, aber nicht unbedingt eine konvergente Teilfolge, weil die Glieder um den Häufungspunkt herum springen dürfen.
--- falsch
Sie besitzt genau einen Häufungspunkt in $\mathbb{R}$ und damit eine konvergente Teilfolge; mehrere Häufungspunkte hat nur eine unbeschränkte Folge.
:::
:::karte herleitung Halbieren, das Unendliche behalten
Wie findet man für eine beschränkte Folge mit $a\le x_n\le b$ durch Halbieren einen Häufungspunkt?
---
Eine der Hälften $[a,\frac{a+b}2]$, $[\frac{a+b}2,b]$ enthält unendlich viele Folgenglieder, weil sonst insgesamt nur endlich viele Glieder da wären.
---
Man behält eine solche Hälfte und halbiert weiter, weil man so eine Intervallschachtelung mit unendlich vielen Gliedern in jedem $[a_n,b_n]$ und $b_n-a_n=2^{-n}(b-a)\to0$ erhält.
---
Die Schachtelung enthält genau einen Punkt $x_0$, weil geschachtelte Intervalle mit Längen gegen 0 genau eine gemeinsame Zahl haben.
---
Jedes $U_\varepsilon(x_0)$ enthält ein ganzes $[a_n,b_n]$ und damit unendlich viele Glieder, weil die Längen gegen 0 gehen und $x_0$ in jedem $[a_n,b_n]$ liegt; also ist $x_0$ Häufungspunkt.
---
Der Satz über Häufungspunkte und Teilfolgen liefert eine konvergente Teilfolge, weil Häufungspunkte genau die Grenzwerte von Teilfolgen sind.
:::
:::karte formel Hüllenformel
Wie lassen sich Limes superior und Limes inferior einer beschränkten Folge über Suprema und Infima der Endstücke berechnen?
---
$x^*=\lim_{n\to\infty}\bigl(\sup\{x_k:k\ge n\}\bigr)$ und $x_*=\lim_{n\to\infty}\bigl(\inf\{x_k:k\ge n\}\bigr)$: Die obere Hülle fällt gegen den größten Häufungspunkt, die untere wächst gegen den kleinsten.
--- falsch
$x^*=\sup\{x_k:k\in\mathbb{N}\}$ und $x_*=\inf\{x_k:k\in\mathbb{N}\}$: Supremum und Infimum aller Glieder sind schon der größte und der kleinste Häufungspunkt, ohne Grenzübergang.
--- falsch
$x^*=\lim_{n\to\infty}\bigl(\inf\{x_k:k\ge n\}\bigr)$ und $x_*=\lim_{n\to\infty}\bigl(\sup\{x_k:k\ge n\}\bigr)$: Die untere Hülle wächst gegen den größten Häufungspunkt, die obere fällt gegen den kleinsten.
--- falsch
$x^*=\lim_{n\to\infty}\bigl(\sup\{x_k:k\ge n\}\bigr)$ und $x_*=\lim_{n\to\infty}\bigl(\inf\{x_k:k\ge n\}\bigr)$, aber nur für monotone Folgen; sonst existieren diese Grenzwerte nicht.
:::
:::karte formel Kriterium für Konvergenz
Woran erkennt man mit Limes superior und Limes inferior, ob eine Folge gegen eine Zahl $a\in\mathbb{R}$ konvergiert?
---
$\lim_{n\to\infty}x_n=a\Longleftrightarrow\limsup_{n\to\infty}x_n=\liminf_{n\to\infty}x_n=a$. Eine konvergente Folge hat also nur einen Häufungspunkt, und eine beschränkte Folge mit genau einem Häufungspunkt konvergiert.
--- falsch
$\lim_{n\to\infty}x_n=a\Longleftrightarrow\limsup_{n\to\infty}x_n=a$. Es genügt der größte Häufungspunkt; der kleinste spielt für die Konvergenz keine Rolle, weil er ohnehin unter dem größten liegt.
--- falsch
$\lim_{n\to\infty}x_n=a\Longleftrightarrow\limsup_{n\to\infty}x_n+\liminf_{n\to\infty}x_n=2a$. Die Folge konvergiert gegen den Mittelwert der beiden, auch wenn sie verschieden sind.
--- falsch
$\lim_{n\to\infty}x_n=a\Longleftrightarrow\limsup_{n\to\infty}x_n=\liminf_{n\to\infty}x_n=a$. Jede Folge mit genau einem Häufungspunkt in $\mathbb{R}$ konvergiert, auch eine unbeschränkte, weil nur Häufungspunkte zählen.
:::
:::karte zusammenhang Voraussetzung beschränkt
Warum braucht der Satz von Bolzano-Weierstraß die Beschränktheit der Folge?
---
$x_n=n$ ist unbeschränkt und hat in $\mathbb{R}$ keinen Häufungspunkt, also keine konvergente Teilfolge. Im Beweis fehlt das Startintervall $[a,b]$, das alle Glieder enthält.
--- falsch
Er braucht sie nicht: Auch unbeschränkte Folgen haben stets einen Häufungspunkt in $\mathbb{R}$; die Beschränktheit macht nur den Beweis durch Halbieren kürzer und übersichtlicher.
--- falsch
Weil unbeschränkte Folgen nicht monoton sein können; ohne Monotonie greift das Monotonie-Lemma nicht, und auf diesem Lemma beruht der Beweis durch Halbieren.
--- falsch
Weil eine unbeschränkte Folge unendlich viele Häufungspunkte hat; dann gibt es keinen kleinsten und keinen größten, der Satz verlangt aber beide.
:::
::::
