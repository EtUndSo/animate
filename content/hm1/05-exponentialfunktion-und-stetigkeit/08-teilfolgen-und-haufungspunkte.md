---
title: Stufe 6: Teilfolgen und Häufungspunkte
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
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

Größter: Die Hülle $s_n:=\sup\{x_k:k\ge n\}$ aus [Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) fällt und ist beschränkt, also existiert $s:=\lim s_n$. Sei $\varepsilon>0$. Ab einem $N$ ist $s_n<s+\varepsilon$, also liegen dort alle $x_k$ unter $s+\varepsilon$. Zu jedem $n$ gibt es wegen $s_n\ge s$ ein $k\ge n$ mit $x_k>s-\varepsilon$. Also liegen unendlich viele Glieder in $U_\varepsilon(s)$, und $s$ ist Häufungspunkt. Ist $y>s$ und $\varepsilon=\frac12(y-s)$, liegen in $U_\varepsilon(y)$ nur endlich viele Glieder. Also ist $s$ der größte. Für den kleinsten nimmt man die Infima.
:::

⁠**So liest man das:** Mit den uneigentlichen Häufungspunkten sind $\limsup x_n$ und $\liminf x_n$ für jede Folge in $\mathbb{R}\cup\{\pm\infty\}$ erklärt, und stets ist $x_*\le x^*$. Der Beweis zeigt für beschränkte Folgen

<span class="anker" id="gl-6-2"></span>
$$x^*=\lim_{n\to\infty}\bigl(\sup\{x_k:k\ge n\}\bigr),\qquad x_*=\lim_{n\to\infty}\bigl(\inf\{x_k:k\ge n\}\bigr). \tag{6.2}$$

Mit dem Hüllensatz aus [Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) folgt für $a\in\mathbb{R}$ das Kriterium

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
