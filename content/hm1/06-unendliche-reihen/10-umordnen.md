---
title: Stufe 8: Umordnen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Unendliche Reihen
order: 1261000
summary: Eine endliche Summe ändert sich nicht, wenn man die Summanden vertauscht.
tags: Bijektion
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Eine endliche Summe ändert sich nicht, wenn man die Summanden vertauscht. Für Reihen ist das falsch. Diese Stufe zeigt den Mechanismus und sagt, wann Umordnen erlaubt ist.
:::

**Die Idee.** Klammern lässt jedes Glied auf seinem Platz. Umordnen schiebt Glieder nach hinten: Zu jedem Zeitpunkt sind Glieder zurückgehalten, die in der alten Reihenfolge schon dran gewesen wären. Geht die Summe dieser zurückgehaltenen Glieder gegen 0, bleibt der Wert. Bei bedingter Konvergenz muss sie das nicht: Wie bei der harmonischen Reihe können immer kleinere, aber immer mehr Glieder eine feste Summe ergeben.

:::definition Definition 8.1 (Umordnung)
<span class="anker" id="satz-8-1"></span>

Sei $k:\mathbb{N}\to\mathbb{N}$ eine __Bijektion__, also eine Zuordnung, die jede natürliche Zahl genau einmal trifft ([Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)). Dann heißt $\sum_{n=1}^\infty a_{k(n)}$ eine Umordnung von $\sum_{n=1}^\infty a_n$.
:::

::::beispiel
Dieselben Glieder wie bei $L_N$, aber immer zwei positive vor einem negativen:

$$T:\quad1+\frac13-\frac12+\frac15+\frac17-\frac14+\frac19+\frac1{11}-\frac16+\dots$$
::::

⁠**So liest man das:** $k(n)$ ist die alte Platznummer des Glieds, das jetzt auf Platz $n$ steht. Hier ist $k(1)=1$, $k(2)=3$, $k(3)=2$, $k(4)=5$. Jedes Glied kommt genau einmal vor. Die Teilsummen $T_N$ lauten $1;\ 1{,}333;\ 0{,}833;\ 1{,}033;\ 1{,}176;\ 0{,}926;\ \dots$ und laufen nicht zu $\log2$ (Abb. [9](#abb-9)): $T_{30}=1{,}0152$, $T_{300}=1{,}0372$, $T_{3000}=1{,}0395$.

:::herleitung Der Wert wird anderthalbmal so groß
Sei $S=\lim L_N$. Weil die geraden Teilsummen steigen, ist $S\ge L_2=\frac12>0$. Regel (i) aus Satz [4.1](rechenregeln-und-klammern.html#satz-4-1) gibt $\frac12S$, Nullen dazwischen stören nicht, denn jede Teilsumme kommt dann nur doppelt vor:

$$\begin{aligned} S&=1-\tfrac12+\tfrac13-\tfrac14+\tfrac15-\tfrac16+\tfrac17-\tfrac18+\dots\\ \tfrac12S&=0+\tfrac12+0-\tfrac14+0+\tfrac16+0-\tfrac18+\dots \end{aligned}$$

Regel (ii) addiert gliedweise: $\frac32S=1+0+\frac13-\frac12+\frac15+0+\frac17-\frac14+\dots$ Streicht man die Nullen, bleibt eine Teilfolge der Teilsummen, und das ist genau $T$. Also ist $T=\frac32S\ne S$, mit $S=\log2$ ergibt das $\frac32\log2=1{,}0397$.
:::

:::abbildung hm1/k6umordnung 9
Dieselben Zahlen in zwei Reihenfolgen. $L_N$ (blau) strebt gegen $\log2$, die Umordnung $T_N$ (orange) gegen $\frac32\log2$.
:::

**Der Mechanismus.** Nach $3m$ Gliedern enthält $T$ die positiven Glieder bis $\frac1{4m-1}$ und die negativen bis $\frac1{2m}$. In $L_{4m}$ stehen dieselben positiven Glieder, aber alle negativen bis $\frac1{4m}$. Der Unterschied sind die zurückgehaltenen negativen Glieder:

<span class="anker" id="gl-8-1"></span>
$$T_{3m}=L_{4m}+Z_m,\qquad Z_m:=\frac1{2m+2}+\frac1{2m+4}+\dots+\frac1{4m}. \tag{8.1}$$

$Z_m$ hat $m$ Summanden, jeder mindestens $\frac1{4m}$, also ist $Z_m\ge\frac14$ für alle $m$. Die Zahlen: $Z_1=0{,}25$, $Z_{10}=0{,}3344$, $Z_{100}=0{,}3453$, der Grenzwert ist $\frac12\log2=0{,}3466$. Die einzelnen Glieder schrumpfen, ihre Zahl wächst, die Summe bleibt: Das ist derselbe Mechanismus wie bei den Gruppen der harmonischen Reihe. Bei einer absolut konvergenten Reihe geht das nicht, denn die zurückgehaltenen Glieder liegen alle weit hinten, und jedes Stück dort ist nach dem Cauchy-Kriterium für $\sum|a_n|$ klein.

:::satz Satz 8.2 (Umordnung absolut konvergenter Reihen)
<span class="anker" id="satz-8-2"></span>

Sei $\sum_{n=1}^\infty a_n$ absolut konvergent und $k:\mathbb{N}\to\mathbb{N}$ eine beliebige Bijektion. Dann konvergiert auch $\sum_{n=1}^\infty a_{k(n)}$ und hat denselben Grenzwert.
:::

⁠**So liest man das:** Das „beliebig“ ist wörtlich gemeint. Glieder dürfen beliebig weit nach hinten rücken, wenn nur jedes irgendwann drankommt. **Voraussetzung nötig:** Die Reihe $L_N$ mit ihrer Umordnung $T$ zeigt, dass bloße Konvergenz nicht reicht.

:::beweis Der Unterschied liegt im Rest
Sei $\varepsilon>0$. Das Cauchy-Kriterium für $\sum|a_n|$ gibt ein $N_1$, so dass jede endliche Summe von Beträgen $|a_n|$ mit Indizes $n>N_1$ kleiner als $\varepsilon$ ist. Wähle $P\ge N_1$ so groß, dass $1,\dots,N_1$ unter $k(1),\dots,k(P)$ vorkommen. Für $M\ge P$ heben sich in $\sum_{n=1}^Ma_{k(n)}-\sum_{n=1}^Ma_n$ alle Glieder mit Index bis $N_1$ auf. Übrig bleiben zwei Summen über verschiedene Indizes oberhalb von $N_1$, also ist der Unterschied kleiner als $2\varepsilon$. Er geht gegen 0, beide Reihen haben denselben Grenzwert.
:::

::::beispiel
$\sum_{n=0}^\infty(-\frac12)^n=\frac23$ ist absolut konvergent. Die Umordnung $1+\frac14-\frac12+\frac1{16}+\frac1{64}-\frac18+\dots$ hat nach 3, 6 und 9 Gliedern die Werte $0{,}75$, $0{,}703$ und $0{,}677$ und strebt wieder gegen $\frac23$. Die positiven Glieder ergeben für sich $\frac43$, die negativen $\frac23$. Beide Vorräte sind endlich, und $\frac43-\frac23$ hängt von keiner Reihenfolge ab.
::::

⁠**Grenzfall:** Vertauscht man nur endlich viele Glieder, ändert sich keine Teilsumme ab einem Index, das ist auch bei bedingter Konvergenz erlaubt.

:::frage Ist Umordnen nicht dasselbe wie Klammern setzen?
Nein. Klammern ändert die Reihenfolge nicht, es liest nur seltener ab. Es ist in jeder konvergenten Reihe erlaubt. Umordnen ändert die Reihenfolge und ist nur bei absoluter Konvergenz harmlos.
:::

:::zusatz Jeder Wert ist erreichbar
Bei bedingter Konvergenz divergieren die positiven Glieder für sich und die negativen für sich. Wäre nämlich eine der beiden Summen endlich, wäre es wegen $S_N=(\text{positive})-(\text{negative})$ auch die andere, und die Reihe wäre absolut konvergent. Beide sind also unerschöpfliche Vorräte. Für jedes Ziel $Z$ nimmt man positive Glieder, bis man über $Z$ liegt, dann negative, bis man darunter liegt, und so fort. Weil die Glieder gegen 0 gehen, wird das Überschießen beliebig klein: Jede Zahl ist als Wert einer Umordnung erreichbar (Riemannscher Umordnungssatz).
:::

:::aufgabe Aufgabe 10 ★★★ Die andere Richtung
<span class="anker" id="aufg-10"></span>

Ordne die Glieder von $L_N$ so um, dass auf ein positives Glied zwei negative folgen: $1-\frac12-\frac14+\frac13-\frac16-\frac18+\frac15-\dots$ Fasse in jedem Dreierblock die ersten beiden Glieder zusammen und zeige, dass die Reihe gegen $\frac12\log2$ strebt. Welche Glieder werden hier zurückgehalten? Prüfe mit $3m=30$ Gliedern.

:::loesung
Block $k$ ist $\frac1{2k-1}-\frac1{4k-2}-\frac1{4k}=\frac1{4k-2}-\frac1{4k}=\frac12\bigl(\frac1{2k-1}-\frac1{2k}\bigr)$. Also sind die Teilsummen nach $3m$ Gliedern gleich $\frac12L_{2m}\to\frac12\log2$, die Teilsummen dazwischen weichen davon um Glieder ab, die gegen 0 gehen. Hier werden positive Glieder zurückgehalten: Nach $3m$ Gliedern fehlen gegenüber $L_{4m}$ die $m$ Glieder $\frac1{2m+1},\dots,\frac1{4m-1}$. Probe: $\frac12L_{20}=0{,}3344$, der Grenzwert ist $0{,}3466$.
:::
:::
