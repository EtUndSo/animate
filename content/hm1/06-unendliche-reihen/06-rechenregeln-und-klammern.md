---
title: Stufe 4: Rechenregeln und Klammern
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
order: 1260600
summary: Endliche Summen darf man gliedweise addieren, mit einer Zahl multiplizieren und beliebig klammern.
tags: Index-Folge
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Endliche Summen darf man gliedweise addieren, mit einer Zahl multiplizieren und beliebig klammern. Diese Stufe zeigt, was davon für Reihen bleibt und warum Klammern nur in einer Richtung erlaubt ist.
:::

**Die Idee.** Die Teilsummen sind Folgen, also gelten deren Rechenregeln. Klammern heißt: Man liest die Treppenhöhe nicht nach jeder Stufe ab, sondern nur nach ganzen Blöcken. Die neuen Teilsummen sind eine Teilfolge der alten, und eine Teilfolge einer konvergenten Folge hat denselben Grenzwert.

:::satz Satz 4.1 (Rechenregeln für Reihen)
<span class="anker" id="satz-4-1"></span>

Seien $\sum_{n=1}^\infty a_n$ und $\sum_{n=1}^\infty b_n$ konvergente Reihen mit Grenzwerten $a$ und $b$. Dann gilt:

<ol class="rm">

<li>

Für jedes $c\in\mathbb{R}$ ist $\sum_{n=1}^\infty(c\cdot a_n)=c\cdot a$.

</li>

<li>

$\sum_{n=1}^\infty(a_n+b_n)=a+b$. Summen konvergenter Reihen sind also konvergent.

</li>

<li>

Sei $\{n_k\}_{k\in\mathbb{N}}\subset\mathbb{N}$ eine __Index-Folge__ mit $1=n_1<n_2<\dots$ und $A_k:=a_{n_k}+\dots+a_{(n_{k+1}-1)}$. Dann konvergiert auch $\sum_{k=1}^\infty A_k$, und es gilt $\sum_{k=1}^\infty A_k=\sum_{n=1}^\infty a_n=a$.

</li>

</ol>
:::

⁠**So liest man das:** In (iii) ist $n_k$ der Startindex von Block $k$, und $A_k$ ist die Summe dieses Blocks. Für $n_k=2k-1$ sind die Starts $1,3,5,\dots$, und $A_2=a_3+a_4$. Teil (iii) sagt: In konvergenten Reihen darf man Klammern setzen, ohne den Grenzwert zu ändern.

:::beweis Rechenregeln für Folgen, Teilfolge
(i), (ii): Für die Teilsummen ist $\sum_{n=1}^Nca_n=c\sum_{n=1}^Na_n$ und $\sum_{n=1}^N(a_n+b_n)=\sum_{n=1}^Na_n+\sum_{n=1}^Nb_n$. Die Rechenregeln für Folgen ergeben die Behauptung.

(iii): Sei $\tilde S_M:=\sum_{k=1}^MA_k$. Wegen $n_1=1$ ist

$$\tilde S_M=(a_1+\dots+a_{n_2-1})+\dots+(a_{n_M}+\dots+a_{n_{M+1}-1})=S_{n_{M+1}-1}.$$

Weil $n_{M+1}-1$ streng wächst, ist $\{\tilde S_M\}$ eine Teilfolge von $\{S_N\}$ und hat denselben Grenzwert.
:::

**Ohne Konvergenz ist das falsch.** Die Reihe $\sum_{n=1}^\infty(-1)^{n+1}=1-1+1-1+\dots$ divergiert, denn ihre Glieder sind keine Nullfolge. Klammert man $(1-1)+(1-1)+\dots$, sind alle $A_k=0$, die neue Reihe konvergiert gegen 0. Klammert man $1+(-1+1)+(-1+1)+\dots$, konvergiert die neue Reihe gegen 1. Der Mechanismus: Die Teilsummen pendeln zwischen 1 und 0, jede Klammerung liest eine andere Teilfolge ab (Abb. [4](#abb-4)). Klammern *setzen* ist also nur in konvergenten Reihen erlaubt, und Klammern *weglassen* geht nie von selbst: Aus der Konvergenz von $\sum A_k$ folgt nichts über $\sum a_n$.

:::abbildung hm1/k6klammern 4
Die Teilsummen von $1-1+1-1+\dots$ pendeln. Die linke Klammerung liest nur die geraden ab, die rechte nur die ungeraden. Zwei Teilfolgen, zwei Grenzwerte, die Reihe selbst hat keinen.
:::

::::beispiel
Regeln (i) und (ii): $\sum_{n=0}^\infty\bigl(3(\frac12)^n-2(\frac13)^n\bigr)=3\cdot2-2\cdot\frac32=3$. Regel (iii): Die Reihe $L_N$ konvergiert, also darf man Paare bilden: $(1-\frac12)+(\frac13-\frac14)+\dots=\frac12+\frac1{12}+\frac1{30}+\dots$ Die Teilsummen sind $L_2,L_4,L_6,\dots$, der Wert bleibt $\log2$.
::::

⁠**Grenzfall:** Für $n_k=k$ enthält jeder Block ein Glied, und (iii) sagt nichts Neues.

:::aufgabe Aufgabe 4 ★ Gliedweise rechnen
<span class="anker" id="aufg-4"></span>

(a) Berechne $\sum_{n=0}^\infty\frac{2^n+3^n}{6^n}$. (b) Die Reihe $\sum_{n=1}^\infty\bigl(\frac1n-\frac1{n+1}\bigr)$ konvergiert (Aufgabe [1](eine-reihe-ist-eine-folge.html#aufg-1)), obwohl beide Teile divergieren. Warum widerspricht das Regel (ii) nicht?

:::loesung
(a) $\frac{2^n+3^n}{6^n}=(\frac13)^n+(\frac12)^n$, also ergibt Regel (ii) mit [(1.3)](eine-reihe-ist-eine-folge.html#gl-1-3) den Wert $\frac32+2=\frac72$. (b) Regel (ii) setzt die Konvergenz beider Teile voraus. Aus der Konvergenz der Summe folgt nichts über die Teile.
:::
:::

:::aufgabe Aufgabe 5 ★★ Zwei Klammerungen, zwei Werte
<span class="anker" id="aufg-5"></span>

Für $b_n=(-1)^{n+1}\bigl(1+\frac1n\bigr)$, also $2-\frac32+\frac43-\frac54+\dots$: Sage vorher, ob die Reihe konvergiert. Klammere dann ab dem ersten Glied zu Paaren und anschließend ab dem zweiten Glied. Drücke beide Ergebnisse durch $S=\lim L_N$ aus. Wie groß ist ihr Unterschied, und woher kommt er?

:::loesung
Wegen $|b_n|>1$ sind die Glieder keine Nullfolge, die Reihe divergiert. Paare ab dem ersten Glied: $\bigl(1+\frac1{2k-1}\bigr)-\bigl(1+\frac1{2k}\bigr)=\frac1{2k-1}-\frac1{2k}$, die Teilsummen sind $L_{2k}$, der Wert ist $S$. Paare ab dem zweiten Glied: $2-\sum_{k=1}^\infty\bigl(\frac1{2k}-\frac1{2k+1}\bigr)=2-(1-S)=1+S$. Der Unterschied ist 1. Es gilt $b_n=(-1)^{n+1}+(-1)^{n+1}\frac1n$, die Teilsummen sind also $L_N$ plus die pendelnde Folge $1;\,0;\,1;\,0;\,\dots$ Jede Klammerung wählt einen der beiden Werte dieser Folge.
:::
:::

::::formelsammlung
**Vielfache und Summen**

$$\sum_{n=1}^\infty(c\cdot a_n)=c\cdot a,\qquad\sum_{n=1}^\infty(a_n+b_n)=a+b$$

Für konvergente Reihen mit Grenzwerten $a$ und $b$ und jedes $c\in\mathbb{R}$. Aus der Konvergenz von $\sum(a_n+b_n)$ folgt nichts über die Teile.

**Klammern setzen**

$$A_k:=a_{n_k}+\dots+a_{(n_{k+1}-1)},\qquad\sum_{k=1}^\infty A_k=\sum_{n=1}^\infty a_n=a$$

Für eine konvergente Reihe und eine Index-Folge $\{n_k\}_{k\in\mathbb{N}}\subset\mathbb{N}$ mit $1=n_1<n_2<\dots$; $n_k$ ist der Startindex von Block $k$. Klammern weglassen geht nicht von selbst.

**Teilsummen der geklammerten Reihe**

$$\tilde S_M=S_{n_{M+1}-1}$$

Mit $\tilde S_M:=\sum_{k=1}^MA_k$; das ist eine Teilfolge der Teilsummen $S_N$, also mit demselben Grenzwert.
::::

::::lernkarten
:::karte formel Rechenregeln für Reihen
Welche Rechenregeln gelten für konvergente Reihen mit den Grenzwerten $a$ und $b$ beim Multiplizieren mit einer Zahl und beim gliedweisen Addieren?
---
Für jedes $c\in\mathbb{R}$ ist $\sum_{n=1}^\infty(c\cdot a_n)=c\cdot a$, und es gilt $\sum_{n=1}^\infty(a_n+b_n)=a+b$. Summen konvergenter Reihen sind also konvergent; das folgt aus den Rechenregeln für Folgen.
--- falsch
Für jedes $c\in\mathbb{R}$ ist $\sum_{n=1}^\infty(c\cdot a_n)=c\cdot a$, und es gilt $\sum_{n=1}^\infty(a_n\cdot b_n)=a\cdot b$. Konvergente Reihen darf man also gliedweise addieren und auch gliedweise multiplizieren.
--- falsch
$\sum_{n=1}^\infty(c\cdot a_n)=c\cdot a$ gilt nur für $c>0$, weil ein negativer Faktor alle Vorzeichen umkehrt; die Regel $\sum_{n=1}^\infty(a_n+b_n)=a+b$ gilt dagegen ohne jede Einschränkung.
--- falsch
Für jedes $c\in\mathbb{R}$ ist $\sum_{n=1}^\infty(c\cdot a_n)=c\cdot a$, und $\sum_{n=1}^\infty(a_n+b_n)=a+b$ gilt schon dann, wenn nur die Summe konvergiert; die einzelnen Reihen dürfen divergieren.
:::
:::karte zusammenhang Voraussetzung der Summenregel
Warum widerspricht die Konvergenz von $\sum_{n=1}^\infty\bigl(\frac1n-\frac1{n+1}\bigr)$ nicht der Regel für Summen von Reihen, obwohl beide Teilreihen divergieren?
---
Weil die Regel die Konvergenz beider Teile voraussetzt und nur in dieser Richtung schließt. Aus der Konvergenz der Summe folgt nichts über die Teile.
--- falsch
Weil sich die beiden divergenten Teilreihen gegenseitig aufheben; die Regel gilt auch mit unendlichen Werten, wenn man $\infty-\infty$ passend als Zahl festlegt.
--- falsch
Weil die Regel nur für Reihen mit positiven Gliedern gilt; hier hat der zweite Teil negative Glieder, sie ist also nicht anwendbar.
--- falsch
Weil die Teilreihen doch konvergieren, nur sehr langsam; der Wert 1 der Reihe ist dann die Differenz ihrer beiden endlichen Grenzwerte.
:::
:::karte begriff Index-Folge
Was ist beim Setzen von Klammern in einer Reihe die Index-Folge $\{n_k\}_{k\in\mathbb{N}}$, und welche Bedingungen muss sie erfüllen?
---
Eine Folge natürlicher Zahlen mit $1=n_1<n_2<\dots$; $n_k$ ist der Startindex von Block $k$. Die Blocksumme ist dann $A_k:=a_{n_k}+\dots+a_{(n_{k+1}-1)}$.
--- falsch
Eine Folge natürlicher Zahlen mit $1=n_1<n_2<\dots$; $n_k$ ist die Länge von Block $k$, also die Zahl der Glieder, die in der $k$-ten Klammer zusammengefasst werden.
--- falsch
Eine Bijektion $\mathbb{N}\to\mathbb{N}$, die festlegt, in welcher Reihenfolge die Glieder addiert werden; $n_k$ ist die Nummer des Glieds, das an der Stelle $k$ steht.
--- falsch
Eine Folge natürlicher Zahlen mit $1=n_1\le n_2\le\dots$; gleiche Indizes sind erlaubt, der Block ist dann leer und seine Summe $A_k=0$.
:::
:::karte formel Klammern setzen
Was sagt die Regel über das Setzen von Klammern in einer konvergenten Reihe $\sum_{n=1}^\infty a_n=a$ mit den Blocksummen $A_k$?
---
Auch $\sum_{k=1}^\infty A_k$ konvergiert, und es gilt $\sum_{k=1}^\infty A_k=\sum_{n=1}^\infty a_n=a$. In konvergenten Reihen darf man also Klammern setzen, ohne den Grenzwert zu ändern.
--- falsch
$\sum_{k=1}^\infty A_k$ konvergiert ebenfalls, hat aber im Allgemeinen einen anderen Grenzwert als $\sum_{n=1}^\infty a_n$, weil die Blöcke die Glieder anders zusammenfassen.
--- falsch
$\sum_{k=1}^\infty A_k=a$ gilt in jeder Reihe, auch in einer divergenten, weil Klammern in endlichen Summen nichts ändert und jede Teilsumme eine endliche Summe ist.
--- falsch
$\sum_{k=1}^\infty A_k=a$ gilt, und umgekehrt folgt aus der Konvergenz jeder geklammerten Reihe die Konvergenz von $\sum_{n=1}^\infty a_n$ mit demselben Grenzwert.
:::
:::karte herleitung Klammern als Teilfolge
Wie zeigt man, dass das Setzen von Klammern den Grenzwert einer konvergenten Reihe nicht ändert?
---
Für $\tilde S_M:=\sum_{k=1}^MA_k$ gilt $\tilde S_M=S_{n_{M+1}-1}$, weil die Blöcke wegen $n_1=1$ lückenlos die Glieder $a_1$ bis $a_{n_{M+1}-1}$ umfassen.
---
Die Indizes $n_{M+1}-1$ wachsen streng mit $M$, weil die $n_k$ streng wachsen; also ist $\{\tilde S_M\}$ eine Teilfolge von $\{S_N\}$.
---
Eine Teilfolge einer konvergenten Folge hat denselben Grenzwert, weil streng wachsende Indizes $n_k\ge k$ erfüllen und ihre Glieder deshalb ab einem Index im Schlauch liegen; also gilt $\tilde S_M\to a$.
:::
:::karte zusammenhang Klammern ohne Konvergenz
Was passiert, wenn man in der divergenten Reihe $1-1+1-1+\dots$ auf zwei Arten Klammern setzt, und woran liegt das?
---
$(1-1)+(1-1)+\dots$ konvergiert gegen 0, $1+(-1+1)+(-1+1)+\dots$ gegen 1. Die Teilsummen pendeln zwischen 1 und 0, jede Klammerung liest eine andere Teilfolge ab.
--- falsch
Beide Klammerungen ergeben 0, weil sich jedes Paar $1-1$ aufhebt. Die Reihe hat also in Wahrheit den Wert 0, die Klammern machen ihn nur sichtbar.
--- falsch
Beide Klammerungen ergeben $\frac12$, den Mittelwert der pendelnden Teilsummen. Klammern macht aus einer pendelnden Reihe stets ihren Mittelwert.
--- falsch
Beide geklammerten Reihen bleiben divergent wie die ursprüngliche, weil Klammern die Konvergenz einer Reihe weder erzeugen noch zerstören kann.
:::
:::karte zusammenhang Zwei Klammerungen, zwei Werte
Was ergeben bei $b_n=(-1)^{n+1}\bigl(1+\frac1n\bigr)$ die Paarklammerungen ab dem ersten und ab dem zweiten Glied, und woher kommt ihr Unterschied?
---
Ab dem ersten Glied $S=\lim L_N$, ab dem zweiten $1+S$. Die Teilsummen sind $L_N$ plus die pendelnde Folge $1;\,0;\,1;\,0;\,\dots$, jede Klammerung wählt einen ihrer Werte.
--- falsch
Beide Klammerungen ergeben $S=\lim L_N$, weil man in jedem Fall dieselben Glieder zu Paaren zusammenfasst und Klammern einen Grenzwert nie ändert.
--- falsch
Ab dem ersten Glied $S$, ab dem zweiten $2+S$. Der Unterschied ist das erste Glied 2, das bei der zweiten Klammerung allein vor allen Klammern steht und nicht ausgeglichen wird.
--- falsch
Ab dem ersten Glied $1+S$, ab dem zweiten $S$. Die Reihe selbst konvergiert, weil $1+\frac1n$ fällt und die Vorzeichen wechseln, nur langsamer als $L_N$.
:::
::::
