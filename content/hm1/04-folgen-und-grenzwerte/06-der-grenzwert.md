---
title: Stufe 4: Der Grenzwert
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Folgen und Grenzwerte
order: 1240600
summary: Die Pendelfolge strebt nicht gegen 0, sondern gegen 2.
tags: konvergent, Grenzwert, Epsilontik
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Pendelfolge strebt nicht gegen 0, sondern gegen 2. Diese Stufe verschiebt das Spiel zu einem beliebigen Wert $a$ und zeigt, dass eine Folge höchstens einen Grenzwert hat.
:::

**Die Idee.** Für eine Annäherung an $a$ zählt der Abstand $|a_n-a|$. Zieht man von jedem Glied $a$ ab, landet man beim Spiel aus Stufe [2](das-epsilon-spiel.html#stufe-2). Eine konvergente Folge ist also eine um $a$ verschobene Nullfolge. Der Schlauch liegt jetzt um $a$ (Abb. [5](#abb-5)).

:::definition Definition 4.1 (Konvergent mit Grenzwert, Epsilon-Kriterium)
<span class="anker" id="satz-4-1"></span>

Die Folge $\{a_n\}_{n=1}^\infty$ heißt __konvergent__ mit __Grenzwert__ $a\in\mathbb{R}$, wenn $\{a_n-a\}_{n=1}^\infty$ eine Nullfolge ist, das heißt

<span class="anker" id="gl-4-1"></span>
$$\forall\,\varepsilon>0\quad\exists\,N_0\in\mathbb{N},\quad\text{so dass}\quad|a_n-a|<\varepsilon\quad\forall\,n>N_0. \tag{4.1}$$

Man schreibt $\lim_{n\to\infty}a_n=a$ oder $a_n\to a$ für $n\to\infty$.
:::

⁠**So liest man das:** Nach der Abstandsregel bedeutet $|a_n-a|<\varepsilon$, dass $a_n$ im offenen Intervall $(a-\varepsilon,a+\varepsilon)$ liegt, dem Epsilon-Schlauch um $a$. Er ist $2\varepsilon$ breit. Bis auf endlich viele Glieder liegen alle darin. Direkte Nachweise von [(4.1)](#gl-4-1) heißen __Epsilontik__. Dieselbe Technik trägt später Cauchy-Folgen (Stufe [8](cauchy-folgen-und-die-axiome.html#stufe-8)) und die Stetigkeit ([Teil 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)). Nullfolgen sind der Sonderfall $a=0$.

:::abbildung hm1/k4schlauch 5
Der Epsilon-Schlauch um $a=2$ mit $\varepsilon=0{,}5$ und den Gliedern der Pendelfolge. Das Glied $a_6=2{,}5$ liegt genau auf dem Rand und damit nicht im offenen Intervall, $a_7=1{,}571$ liegt drin. Ab $N_0=6$ bleiben alle Glieder im Schlauch, die grauen bis $n=6$ zählen nicht.
:::

**Beispiel.** Für die Pendelfolge ist $a_n-2=d_n$, und das ist nach Stufe [2](das-epsilon-spiel.html#stufe-2) eine Nullfolge. Also gilt $\lim a_n=2$, mit denselben Antworten wie im Spiel. Für die Summenfolge ist $2-s_n=(\frac12)^n$, eine geometrische Folge, also gilt $\lim s_n=2$. **Grenzfall:** Die konstante Folge $a_n=c$ hat den Grenzwert $c$ mit $N_0=1$ für jede Toleranz.

**Der Trick der Epsilontik.** Oft lässt sich $|a_n-a|<\varepsilon$ nicht bequem nach $n$ auflösen. Man sucht dann eine bekannte positive Nullfolge $y_n$ mit $|a_n-a|\le y_n$, etwa $y_n=\frac Cn$ oder $\frac C{\sqrt n}$. Nach $n$ aufgelöst wird nur $y_n<\varepsilon$. Gefragt ist ein $N_0$, nicht das kleinste. Beispiel: $f_n=\dfrac{2n^2+3}{n^2+n}$ hat den Grenzwert 2, denn für $n\ge2$ ist

$$|f_n-2|=\Bigl|\frac{3-2n}{n^2+n}\Bigr|=\frac{2n-3}{n^2+n}\le\frac{2n}{n^2}=\frac2n.$$

Sei $\varepsilon>0$. Wähle $N_0:=\lfloor2/\varepsilon\rfloor+1$. Für $n>N_0$ ist $n\ge2$ und $n>2/\varepsilon$, also $|f_n-2|\le\frac2n<\varepsilon$. Für $n=10$ ist $|f_{10}-2|=0{,}1545\le0{,}2$.

:::satz Satz 4.2 (Eigenschaften konvergenter Folgen)
<span class="anker" id="satz-4-2"></span>

Sei $\{a_n\}$ konvergent mit Grenzwert $a$. Dann gilt: (i) Der Grenzwert ist eindeutig bestimmt. (ii) $\{a_n\}$ ist beschränkt.
:::

⁠**So liest man das:** (i) rechtfertigt das Wort „der“ Grenzwert. (ii) gilt nicht umgekehrt: $(-1)^n$ ist beschränkt und konvergiert nicht (Stufe [6](einklemmen-und-divergenz.html#stufe-6)). Eine unbeschränkte Folge kann dagegen nicht konvergieren.

:::beweis Eindeutigkeit und Beschränktheit
(i) Es gelte $a_n\to a$ und $a_n\to\tilde a$. Dann sind $\{a_n-a\}$ und $\{a_n-\tilde a\}$ Nullfolgen, nach Satz [3.2](nullfolgen-vergleichen.html#satz-3-2) (i) auch ihre Differenz $(a_n-a)-(a_n-\tilde a)=\tilde a-a$. Diese Differenz hängt nicht von $n$ ab. Eine konstante Nullfolge ist 0, sonst scheitert sie an $\varepsilon=|\tilde a-a|$. Also ist $\tilde a=a$.

(ii) Mit der Dreiecksungleichung ist $|a_n|=|a_n-a+a|\le|a_n-a|+|a|$. Die Nullfolge $\{a_n-a\}$ ist nach Satz [3.2](nullfolgen-vergleichen.html#satz-3-2) (iii) durch ein $M$ beschränkt, also ist $|a_n|\le M+|a|$ für alle $n$.
:::

:::frage Ändert sich der Grenzwert, wenn ich die ersten tausend Glieder ändere?
Nein. Die Bedingung betrifft nur Glieder hinter $N_0$, und $N_0$ darf man über 1000 legen. Der Grenzwert ist eine Eigenschaft des Endes der Folge. Aussagen über einzelne Glieder oder über „die ersten paar“ sagen nichts über ihn.
:::

:::aufgabe Aufgabe 6 ★★ Epsilontik
<span class="anker" id="aufg-6"></span>

Zeige mit [(4.1)](#gl-4-1), dass $h_n=\dfrac{3n-1}{n+2}$ gegen 3 konvergiert. Rechne $|h_n-3|$ exakt aus, finde das kleinste $N_0$ für $\varepsilon=0{,}1$ und für $\varepsilon=0{,}001$, und gib eine Regel $N_0(\varepsilon)$ an. Welches $N_0$ liefert für $\varepsilon=0{,}1$ die gröbere Abschätzung $|h_n-3|\le7/n$?

:::loesung
$h_n-3=\dfrac{3n-1-3n-6}{n+2}=\dfrac{-7}{n+2}$, also $|h_n-3|=\dfrac7{n+2}$. Das ist kleiner als $\varepsilon$ genau für $n>7/\varepsilon-2$. Für $\varepsilon=0{,}1$: $n>68$, $N_0=68$. Für $\varepsilon=0{,}001$: $n>6998$, $N_0=6998$. Regel: $N_0(\varepsilon):=\lfloor7/\varepsilon\rfloor+1$, denn für $n>N_0$ ist $n+2>n>7/\varepsilon$. Die gröbere Abschätzung $7/(n+2)\le7/n$ gibt für $\varepsilon=0{,}1$ das Ergebnis $N_0=70$. Das ist nicht das kleinste, gewinnt aber auch.
:::
:::
