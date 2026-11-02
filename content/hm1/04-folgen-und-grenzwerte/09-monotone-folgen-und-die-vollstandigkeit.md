---
title: Stufe 7: Monotone Folgen und die Vollständigkeit
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Folgen und Grenzwerte
order: 1240900
summary: Bisher stand der Grenzwert fest, bevor der Nachweis begann.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bisher stand der Grenzwert fest, bevor der Nachweis begann. Die Wurzelfolge besteht aus Brüchen und strebt zu einem Wert, der kein Bruch ist. Diese Stufe zeigt Konvergenz, ohne das Ziel zu kennen, und macht sichtbar, wo die Vollständigkeit aus [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) wirkt.
:::

**Die Idee.** Eine monoton wachsende Folge kann nicht zurück, und eine obere Schranke ist für sie eine Decke. Die tiefste Decke ist das Supremum der Wertemenge. An diese Decke muss die Folge heran: Bliebe sie dauerhaft um $\varepsilon$ darunter, wäre „Supremum minus $\varepsilon$“ eine noch tiefere Decke. Der Beweis steht und fällt damit, dass es die tiefste Decke im Zahlbereich gibt. Das sagt das Vollständigkeitsaxiom.

:::satz Satz 7.1 (Monotonie-Lemma)
<span class="anker" id="satz-7-1"></span>

<ol>

<li>

Eine monoton wachsende Folge $\{a_n\}$, die nach oben beschränkt ist, ist konvergent, und es gilt $\lim_{n\to\infty}a_n=\sup\mathcal W(a_n)\in\mathbb{R}$.

</li>

<li>

Eine monoton fallende Folge $\{b_n\}$, die nach unten beschränkt ist, ist konvergent, und es gilt $\lim_{n\to\infty}b_n=\inf\mathcal W(b_n)\in\mathbb{R}$.

</li>

</ol>
:::

⁠**So liest man das:** $\mathcal W(a_n)=\{a_n:n\in\mathbb{N}\}$ ist die Wertemenge aus Stufe [1](folgen-und-ihr-verlauf.html#stufe-1). Der Satz gibt Konvergenz, ohne dass der Grenzwert vorher in einer Formel bekannt sein muss. **Voraussetzungen nötig:** Ohne Schranke wächst $n^2$ ohne Grenze, ohne Monotonie pendelt $(-1)^n$. **Grenzfall:** Die konstante Folge $c$ ist monoton in beide Richtungen, ihr Supremum und Infimum sind $c$.

:::beweis Monotonie-Lemma
(I) Die Wertemenge $M:=\mathcal W(a_n)\subset\mathbb{R}$ ist nicht leer und nach oben beschränkt. Nach dem Vollständigkeitsaxiom existiert $a:=\sup M\in\mathbb{R}$. Sei $\varepsilon>0$. Dann ist $a-\varepsilon$ keine obere Schranke von $M$, denn $a$ ist die kleinste. Also gibt es ein $N_0$ mit $a-\varepsilon<a_{N_0}\le a$. Wegen der Monotonie gilt für alle $n>N_0$

$$a-\varepsilon<a_{N_0}\le a_n\le a,\quad\text{also}\quad|a_n-a|<\varepsilon.$$

(II) Die Folge $a_n:=-b_n$ ist monoton wachsend und nach oben beschränkt, mit $\sup\mathcal W(a_n)=-\inf\mathcal W(b_n)$. Nach (I) konvergiert sie, die Rechenregeln übertragen das auf $b_n$.
:::

:::abbildung hm1/k4monoton 8
Links die Summenfolge unter der Decke $\sup\mathcal W(s_n)=2$. Der rote Streifen hat die Breite $\varepsilon=0{,}1$. Ab $N_0=3$ bleiben alle Glieder darin. Rechts die Wurzelfolge: Sie fällt, ist nach unten beschränkt und strebt gegen $\sqrt2$. Innerhalb der rationalen Zahlen gibt es dort kein Ziel.
:::

**Beispiel: die Wurzelfolge.** Alle Glieder $x_1=2$, $x_{n+1}=\frac12(x_n+2/x_n)$ sind positiv und rational, denn Brüche bleiben bei den Grundrechenarten Brüche. Ausmultiplizieren zeigt zwei Dinge:

$$x_{n+1}^2-2=\tfrac14\Bigl(x_n-\frac2{x_n}\Bigr)^2\ge0,\qquad x_n-x_{n+1}=\frac{x_n^2-2}{2x_n}\ge0.$$

Die erste Gleichung sagt mit $x_1^2=4$, dass $x_n^2\ge2$ für alle $n$ gilt, die zweite sagt damit: Die Folge fällt monoton. Nach unten ist sie durch 1 beschränkt, denn $x_n^2\ge2$ erzwingt $x_n\ge1$. Das Monotonie-Lemma liefert in $\mathbb{R}$ einen Grenzwert $x\ge1$. Ihn berechnet man, indem man in der Vorschrift auf beiden Seiten zum Grenzwert übergeht (Rechenregeln, $\{x_{n+1}\}$ hat denselben Grenzwert wie $\{x_n\}$):

$$x=\tfrac12\Bigl(x+\frac2x\Bigr)\quad\Longrightarrow\quad x^2=2\quad\Longrightarrow\quad x=\sqrt2.$$

Zahlen: $x_3=1{,}4167$, $x_4=1{,}414216$, $x_5=1{,}4142135624$. Der Fehler von $x_5$ liegt unter $2\cdot10^{-12}$. Das Heron-Verfahren ist ein gängiger Weg, Wurzeln in digitalen Rechenwerken zu bestimmen.

**Warum das in $\mathbb{Q}$ scheitert.** Alle Voraussetzungen des Monotonie-Lemmas prüft man innerhalb von $\mathbb{Q}$: Die $x_n$ sind Brüche, sie fallen, und die Schranke 1 ist ein Bruch. Trotzdem gibt es in $\mathbb{Q}$ keinen Grenzwert: Jeder Grenzwert müsste die Gleichung $x^2=2$ erfüllen, und kein Bruch tut das ([Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Der Beweis des Lemmas bricht genau an einer Stelle: Die Menge $\{x_n\}$ hat in $\mathbb{Q}$ kein Infimum. Zu jeder rationalen unteren Schranke gibt es eine größere. Die Folge läuft auf eine Lücke zu. Deshalb steht in der Definition der Konvergenz $a\in\mathbb{R}$ und deshalb ist die Vollständigkeit keine Formalie: *In $\mathbb{R}$ hat jede monotone beschränkte Folge ein Ziel, in $\mathbb{Q}$ nicht.*

:::frage Ein Rechner kennt nur Brüche. Wozu braucht man die Lücken in $\mathbb{Q}$ geschlossen?
Für einen Zahlenwert genügt ein Bruch: $x_5$ trifft $\sqrt2$ auf 11 Nachkommastellen. Aussagen wie „diese Folge hat einen Grenzwert“ brauchen dagegen $\mathbb{R}$. Stetigkeit ([Teil 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)) und Reihen ([Teil 6](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen/unendliche-reihen.html)) beruhen darauf, dass der Grenzwert existiert, auch wenn ihn niemand als Bruch hinschreiben kann.
:::

:::aufgabe Aufgabe 9 ★★ Wurzelkette
<span class="anker" id="aufg-9"></span>

Gegeben ist $y_1=1$, $y_{n+1}=\sqrt{2y_n+3}$. (a) Berechne $y_2,y_3,y_4$. (b) Zeige durch Induktion $0<y_n<3$ und $y_n<y_{n+1}$. (c) Warum konvergiert die Folge? (d) Berechne den Grenzwert. Warum scheidet $-1$ aus?

:::loesung
(a) $y_2=\sqrt5=2{,}2361$, $y_3=2{,}7335$, $y_4=2{,}9098$. (b) $y_1=1$ liegt in $(0,3)$. Aus $0<y_n<3$ folgt $3<2y_n+3<9$, also $0<y_{n+1}<3$. Weiter ist $y_{n+1}^2-y_n^2=2y_n+3-y_n^2=(3-y_n)(1+y_n)>0$, und weil beide positiv sind, ist $y_{n+1}>y_n$. (c) Die Folge ist monoton wachsend und beschränkt, das Monotonie-Lemma greift. (d) Grenzübergang in $y_{n+1}^2=2y_n+3$ gibt $y^2=2y+3$, also $(y-3)(y+1)=0$. Wegen $y_n\ge1$ ist $y\ge1$, also $y=3$.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Heron für 3
<span class="anker" id="aufg-10"></span>

Gegeben ist $w_1=2$, $w_{n+1}=\frac12(w_n+3/w_n)$. (a) Berechne $w_2,w_3$ als Brüche. (b) Zeige wie im Beispiel: $w_n^2\ge3$, und die Folge fällt monoton. (c) Bestimme ihren Grenzwert in $\mathbb{R}$. (d) Eine Bekannte behauptet: „Die Folge fällt und ist beschränkt, also konvergiert sie auch in $\mathbb{Q}$.“ Was ist falsch, wenn du weißt, dass $\sqrt3$ irrational ist?

:::loesung
(a) $w_2=\frac12(2+\frac32)=\frac74$, $w_3=\frac12(\frac74+\frac{12}7)=\frac{97}{56}=1{,}7321$. (b) $w_{n+1}^2-3=\frac14(w_n-3/w_n)^2\ge0$ und $w_1^2=4\ge3$, also $w_n^2\ge3$. Damit ist $w_n-w_{n+1}=\frac{w_n^2-3}{2w_n}\ge0$. (c) Die Folge ist durch 1 nach unten beschränkt, also konvergiert sie in $\mathbb{R}$ gegen ein $w\ge1$. Der Grenzübergang gibt $w=\frac12(w+3/w)$, also $w^2=3$ und $w=\sqrt3$. (d) Das Monotonie-Lemma braucht ein Infimum im Zahlbereich, und das fehlt in $\mathbb{Q}$. Ein rationaler Grenzwert müsste $w^2=3$ erfüllen. Das schließt die Irrationalität von $\sqrt3$ aus.
:::
:::
