---
title: Stufe 8: Umordnen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
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

Sei $k:\mathbb{N}\to\mathbb{N}$ eine __Bijektion__, also eine Zuordnung, die jede natürliche Zahl genau einmal trifft ([Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)). Dann heißt $\sum_{n=1}^\infty a_{k(n)}$ eine Umordnung von $\sum_{n=1}^\infty a_n$.
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

::::formelsammlung
**Umordnung**

$$\sum_{n=1}^\infty a_{k(n)}$$

Mit einer Bijektion $k:\mathbb{N}\to\mathbb{N}$, die jede natürliche Zahl genau einmal trifft; $k(n)$ ist die alte Platznummer des Glieds auf Platz $n$.

**Anderthalbfacher Wert**

$$T=\frac32S,\qquad\frac32\log2=1{,}0397$$

$T=1+\frac13-\frac12+\frac15+\frac17-\frac14+\dots$ enthält die Glieder von $L_N$, immer zwei positive vor einem negativen; $S=\lim L_N=\log2$.

**Zurückgehaltene Glieder**

$$T_{3m}=L_{4m}+Z_m,\qquad Z_m:=\frac1{2m+2}+\frac1{2m+4}+\dots+\frac1{4m}$$

$Z_m$ hat $m$ Summanden, jeder mindestens $\frac1{4m}$, also $Z_m\ge\frac14$; der Grenzwert ist $\frac12\log2$.

**Umordnung absolut konvergenter Reihen**

$$\sum_{n=1}^\infty a_{k(n)}=\sum_{n=1}^\infty a_n$$

Für absolut konvergentes $\sum a_n$ und jede Bijektion $k:\mathbb{N}\to\mathbb{N}$; die Umordnung konvergiert. Bei bedingter Konvergenz ist jede Zahl als Wert einer Umordnung erreichbar (Riemannscher Umordnungssatz).

**Ein positives, zwei negative Glieder**

$$\frac1{2k-1}-\frac1{4k-2}-\frac1{4k}=\frac12\bigl(\frac1{2k-1}-\frac1{2k}\bigr)$$

Umordnung von $L_N$ in Dreierblöcken: Die Teilsummen nach $3m$ Gliedern sind $\frac12L_{2m}$, der Wert ist $\frac12\log2$.
::::

::::lernkarten
:::karte begriff Umordnung
Was ist eine Umordnung einer Reihe $\sum_{n=1}^\infty a_n$, und was gibt dabei $k(n)$ an?
---
Die Reihe $\sum_{n=1}^\infty a_{k(n)}$ mit einer Bijektion $k:\mathbb{N}\to\mathbb{N}$, also dieselben Glieder in anderer Reihenfolge. $k(n)$ ist die alte Platznummer des Glieds, das jetzt auf Platz $n$ steht.
--- falsch
Die Reihe $\sum_{n=1}^\infty a_{k(n)}$ mit einer beliebigen Abbildung $k:\mathbb{N}\to\mathbb{N}$, bei der Glieder auch mehrfach vorkommen oder fehlen dürfen. $k(n)$ ist die alte Platznummer des Glieds auf Platz $n$.
--- falsch
Die Reihe $\sum_{n=1}^\infty a_{k(n)}$ mit einer Bijektion $k:\mathbb{N}\to\mathbb{N}$, also dieselben Glieder in anderer Reihenfolge. $k(n)$ ist die neue Platznummer des Glieds, das vorher auf Platz $n$ stand.
--- falsch
Die Reihe, die durch Setzen von Klammern entsteht: Die Glieder bleiben in ihrer Reihenfolge und werden zu Blöcken zusammengefasst. $k(n)$ ist der Startindex von Block $n$.
:::
:::karte zusammenhang Bijektion
Warum muss die Zuordnung $k:\mathbb{N}\to\mathbb{N}$ einer Umordnung eine Bijektion sein?
---
Weil eine Bijektion jede natürliche Zahl genau einmal trifft: So kommt jedes Glied der alten Reihe genau einmal vor, keines fehlt und keines doppelt.
--- falsch
Weil eine Bijektion die Reihenfolge der Glieder erhält; nur so bleibt der Wert der Reihe bei jeder Umordnung gleich, auch bei bedingter Konvergenz und bei beliebig weiten Verschiebungen.
--- falsch
Weil eine Bijektion jede Zahl höchstens einmal trifft; ob alle Glieder vorkommen, ist für den Wert unerheblich, solange keines doppelt steht.
--- falsch
Weil eine Bijektion nur endlich viele Glieder verschiebt; so ändert sich ab einem Index keine Teilsumme, und der Wert bleibt erhalten.
:::
:::karte formel anderthalbfacher Wert
Welchen Wert hat die Umordnung $T=1+\frac13-\frac12+\frac15+\frac17-\frac14+\dots$ der alternierenden harmonischen Reihe, in der immer zwei positive Glieder vor einem negativen stehen?
---
$T=\frac32S$ mit $S=\lim L_N=\log2$, also $\frac32\log2=1{,}0397$. Dieselben Glieder ergeben in dieser Reihenfolge einen anderen Wert.
--- falsch
$T=S=\log2$, weil dieselben Glieder vorkommen und die Reihenfolge in einer konvergenten Reihe den Wert nicht ändert.
--- falsch
$T=2S=2\log2$, weil die positiven Glieder doppelt so oft kommen wie die negativen und deshalb doppelt so viel beitragen.
--- falsch
$T$ divergiert, weil die positiven Glieder doppelt so schnell kommen und deshalb wie die harmonische Reihe über alle Grenzen wachsen.
:::
:::karte herleitung Der Wert wird anderthalbmal so groß
Wie zeigt man mit den Rechenregeln für Reihen, dass die Umordnung $T$ der alternierenden harmonischen Reihe den Wert $\frac32S$ hat?
---
Regel (i) gibt $\frac12S=0+\frac12+0-\frac14+0+\frac16+0-\frac18+\dots$, weil Nullen dazwischen nicht stören: Jede Teilsumme kommt dann nur doppelt vor.
---
Regel (ii) addiert $S$ und $\frac12S$ gliedweise zu $\frac32S=1+0+\frac13-\frac12+\frac15+0+\frac17-\frac14+\dots$, weil beide Reihen konvergieren.
---
Streicht man die Nullen, bleibt eine Teilfolge der Teilsummen, und das ist genau $T$, weil die übrigen Glieder schon in der Reihenfolge von $T$ stehen.
---
Also ist $T=\frac32S\ne S$, weil $S\ge L_2=\frac12>0$ ist; mit $S=\log2$ folgt $\frac32\log2=1{,}0397$.
:::
:::karte zusammenhang zurückgehaltene Glieder
Woran liegt es, dass die Umordnung $T$ nicht gegen $\log2$ strebt, obwohl jedes Glied von $L_N$ genau einmal vorkommt?
---
An den zurückgehaltenen negativen Gliedern: $T_{3m}=L_{4m}+Z_m$ mit $Z_m:=\frac1{2m+2}+\frac1{2m+4}+\dots+\frac1{4m}$. Dabei ist $Z_m\ge\frac14$, der Grenzwert ist $\frac12\log2$: Immer kleinere, aber immer mehr Glieder tragen eine feste Summe.
--- falsch
An den zurückgehaltenen negativen Gliedern: Ihre Summe $Z_m$ geht zwar gegen 0, aber so langsam, dass $T$ numerisch über $\log2$ zu liegen scheint; im Grenzwert ist $T=\log2$.
--- falsch
Daran, dass in $T$ doch Glieder fehlen: Die negativen Glieder $-\frac1{4m}$ kommen nie an die Reihe, deshalb ist der Wert größer als $\log2$, und zwar um die Summe der fehlenden Glieder.
--- falsch
An einem Rundungseffekt: $T$ strebt doch gegen $\log2$, nur so langsam, dass selbst $T_{3000}=1{,}0395$ den Grenzwert noch nicht zeigt; erst viel später fällt $T_N$ wieder ab.
:::
:::karte formel Umordnung absolut konvergenter Reihen
Was garantiert der Satz über die Umordnung absolut konvergenter Reihen, und welche Bijektionen sind dabei erlaubt?
---
Ist $\sum_{n=1}^\infty a_n$ absolut konvergent, so konvergiert jede Umordnung $\sum_{n=1}^\infty a_{k(n)}$ mit einer beliebigen Bijektion $k:\mathbb{N}\to\mathbb{N}$ und hat denselben Grenzwert. Glieder dürfen beliebig weit nach hinten rücken.
--- falsch
Ist $\sum_{n=1}^\infty a_n$ konvergent, so konvergiert jede Umordnung mit einer beliebigen Bijektion und hat denselben Grenzwert; absolute Konvergenz braucht man nur für schnellere Konvergenz.
--- falsch
Ist $\sum_{n=1}^\infty a_n$ absolut konvergent, so konvergiert jede Umordnung, ihr Grenzwert kann sich aber ändern; erhalten bleibt nur, dass sie wieder absolut konvergiert.
--- falsch
Ist $\sum_{n=1}^\infty a_n$ absolut konvergent, so behalten nur Umordnungen, die endlich viele Glieder vertauschen, den Grenzwert; „beliebig“ meint beliebige endliche Vertauschungen.
:::
:::karte herleitung Der Unterschied liegt im Rest
Wie zeigt man, dass jede Umordnung einer absolut konvergenten Reihe denselben Grenzwert hat?
---
Zu $\varepsilon>0$ gibt das Cauchy-Kriterium für $\sum|a_n|$ ein $N_1$, so dass jede endliche Summe von Beträgen $|a_n|$ mit Indizes $n>N_1$ kleiner als $\varepsilon$ ist, weil $\sum|a_n|$ konvergiert.
---
Man wählt $P\ge N_1$ so groß, dass $1,\dots,N_1$ unter $k(1),\dots,k(P)$ vorkommen, weil die Bijektion $k$ jede natürliche Zahl trifft.
---
Für $M\ge P$ heben sich in $\sum_{n=1}^Ma_{k(n)}-\sum_{n=1}^Ma_n$ alle Glieder mit Index bis $N_1$ auf, weil beide Summen sie genau einmal enthalten.
---
Übrig bleiben zwei Summen über verschiedene Indizes oberhalb von $N_1$, also ist der Unterschied kleiner als $2\varepsilon$, weil jede der beiden Summen betragsmäßig unter $\varepsilon$ liegt.
---
Der Unterschied geht also gegen 0, und beide Reihen haben denselben Grenzwert, weil $\sum_{n=1}^Ma_n$ konvergiert.
:::
:::karte zusammenhang Umordnen und Klammern
Worin unterscheidet sich das Umordnen einer Reihe vom Setzen von Klammern, und wann ist jedes von beiden erlaubt?
---
Klammern ändert die Reihenfolge nicht, es liest nur seltener ab, und ist in jeder konvergenten Reihe erlaubt. Umordnen ändert die Reihenfolge und ist nur bei absoluter Konvergenz harmlos.
--- falsch
Klammern ändert die Reihenfolge nicht und ist in jeder Reihe erlaubt, auch in einer divergenten. Umordnen ist dagegen nur bei bedingter Konvergenz harmlos, bei absoluter ändert es den Wert.
--- falsch
Klammern ändert die Reihenfolge, Umordnen nur die Zusammenfassung zu Blöcken. Klammern ist deshalb nur bei absoluter Konvergenz erlaubt, Umordnen in jeder konvergenten Reihe.
--- falsch
Es gibt keinen wesentlichen Unterschied: Beides fasst dieselben Glieder anders zusammen, beides ist in jeder konvergenten Reihe erlaubt und ändert den Wert nie.
:::
:::karte zusammenhang jeder Wert ist erreichbar
Warum lässt sich eine bedingt konvergente Reihe so umordnen, dass sie gegen eine beliebig vorgegebene Zahl $Z$ strebt?
---
Weil ihre positiven und negativen Glieder für sich divergieren: Man nimmt positive, bis man über $Z$ liegt, dann negative, bis man darunter liegt, und so fort. Weil die Glieder gegen 0 gehen, schrumpft das Überschießen.
--- falsch
Weil ihre positiven und ihre negativen Glieder für sich konvergieren; man kann deshalb die beiden Summen beliebig gewichten und so jede vorgegebene Zahl als gewichtete Differenz der beiden Vorräte erzeugen.
--- falsch
Weil eine bedingt konvergente Reihe nur endlich viele negative Glieder hat; schiebt man diese passend nach vorn oder nach hinten, lässt sich jeder Wert einstellen.
--- falsch
Weil man beim Umordnen Glieder weglassen darf, solange unendlich viele übrig bleiben; durch geschicktes Weglassen positiver oder negativer Glieder erreicht man dann jede vorgegebene Zahl.
:::
:::karte zusammenhang endliche Vorräte
Warum ändert keine Umordnung den Wert der Reihe $\sum_{n=0}^\infty(-\frac12)^n=\frac23$?
---
Weil die Reihe absolut konvergiert: Die positiven Glieder ergeben für sich $\frac43$, die negativen $\frac23$; $\frac43-\frac23$ hängt von keiner Reihenfolge ab.
--- falsch
Weil die Glieder geometrisch fallen: Bei geometrisch fallenden Gliedern ist die Reihenfolge egal, bei allen anderen Reihen ändert Umordnen den Wert, auch bei absoluter Konvergenz.
--- falsch
Weil positive und negative Glieder einander abwechseln; jede Umordnung, die dieses Muster erhält, lässt den Wert gleich, alle anderen ändern ihn.
--- falsch
Weil die positiven Glieder für sich $\frac43$ und die negativen $\frac23$ ergeben; beide Vorräte sind endlich, also ergibt jede Umordnung $\frac43+\frac23=2$.
:::
:::karte zusammenhang endlich viele Vertauschungen
Was passiert mit dem Wert einer bedingt konvergenten Reihe, wenn man nur endlich viele Glieder vertauscht?
---
Nichts: Ab einem Index ändert sich keine Teilsumme mehr, deshalb bleibt der Grenzwert gleich. Das ist auch bei bedingter Konvergenz erlaubt.
--- falsch
Der Wert kann sich ändern, weil bei bedingter Konvergenz schon eine einzelne Vertauschung alle späteren Teilsummen dauerhaft um ein Stück verschiebt.
--- falsch
Die Reihe wird divergent, weil die Vertauschung das Vorzeichenmuster stört, auf dem ihre Konvergenz beruht.
--- falsch
Nichts, aber nur, wenn die vertauschten Glieder dasselbe Vorzeichen haben; sonst ändert sich der Wert um ihre Differenz.
:::
::::
