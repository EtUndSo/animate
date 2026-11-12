---
title: Stufe 4: Das Zweitor im Betrieb
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1160600
summary: Im Betrieb ist kein Tor offen.
tags: Rückwirkung, rückwirkungsfrei
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Im Betrieb ist kein Tor offen. Diese Stufe zeigt, wie die Last über den Parameter $Z_{12}$ auf den Eingang zurückwirkt und was das Zweitor für die Last ist.
:::

**Die Idee.** Die Last entnimmt Tor 2 einen Strom, also ist $I_2\neq0$. Über die Quelle $Z_{12}I_2$ erscheint dieser Strom als Spannung am Eingang. Im T-Zweitor ist das greifbar: Ein Teil des Stroms, der sonst durch $R_\mathrm{b}$ flösse, weicht über $R_\mathrm{c}$ zur Last aus. An $R_\mathrm{b}$ fällt weniger ab, $U_1$ sinkt, und der Eingang wirkt niederohmiger. Diese Wirkung des Ausgangs auf den Eingang heißt __Rückwirkung__.

:::satz Satz 4.1 (Eingangswiderstand und Ausgangsseite)
<span class="anker" id="satz-4-1"></span>

Mit der Last $Z_\mathrm{L}$ an Tor 2 gilt $U_2=-Z_\mathrm{L}I_2$ und

<span class="anker" id="gl-4-1"></span>
$$I_2=-\frac{Z_{21}}{Z_{22}+Z_\mathrm{L}}\,I_1,\qquad Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}. \tag{4.1}$$

Die Grenzfälle sind der Leerlauf- und der Kurzschlusseingangswiderstand:

<span class="anker" id="gl-4-2"></span>
$$Z_{1,\mathrm{LL}}=Z_{11},\qquad Z_{1,\mathrm{KS}}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}}. \tag{4.2}$$

Speist eine Quelle $U_\mathrm{q}$, $R_\mathrm{q}$ Tor 1, wirkt Tor 2 als Ersatzspannungsquelle ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) mit

<span class="anker" id="gl-4-3"></span>
$$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q},\qquad R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}. \tag{4.3}$$
:::

⁠**So liest man das:** $Z_\mathrm{L}$ ist die Last, hier ein Widerstand. Das Minuszeichen in $U_2=-Z_\mathrm{L}I_2$ steht, weil $I_2$ in das Zweitor zeigt und damit gegen den Strom durch die Last. Der Bruch in [(4.1)](#gl-4-1) ist der Betrag, um den die Last den Eingangswiderstand ändert. Ist $Z_{12}=0$, ist er null: Der Eingang merkt nichts von der Last, das Zweitor heißt __rückwirkungsfrei__. **Gültigkeit:** Das Zweitor muss linear sein, die Formeln für die Ersatzquelle setzen eine lineare Quelle voraus.

:::herleitung Eingangswiderstand und Ausgangsseite
Rechte Masche: $U_2=Z_{21}I_1+Z_{22}I_2=-Z_\mathrm{L}I_2$, nach $I_2$ umgestellt ergibt sich der erste Teil von [(4.1)](#gl-4-1). Eingesetzt in die linke Masche $U_1=Z_{11}I_1+Z_{12}I_2$ und durch $I_1$ geteilt folgt $Z_1$. Für $Z_\mathrm{L}\to\infty$ fällt der Bruch weg, für $Z_\mathrm{L}=0$ folgt $Z_{1,\mathrm{KS}}$ mit $I_2=-Z_{21}I_1/Z_{22}$.

Für [(4.3)](#gl-4-3) ersetzt man die Last. Die Quelle gibt $U_1=U_\mathrm{q}-R_\mathrm{q}I_1$ vor. Bei $I_2=0$ ist $I_1=U_\mathrm{q}/(Z_{11}+R_\mathrm{q})$ und $U_\mathrm{i}=Z_{21}I_1$. Mit $U_\mathrm{q}=0$ ist Tor 1 durch $R_\mathrm{q}$ abgeschlossen, und $R_\mathrm{i}$ ist $Z_1$ mit vertauschten Indizes.
:::

:::abbildung et1/k6betrieb 5
Ersatzschaltbild des T-Zweitors mit Quelle und Last. Es fließen $I_1=250$ mA und $I_2=-50$ mA. Die Rückwirkung beträgt $Z_{12}I_2=-1$ V, die Vorwärtsquelle liefert $Z_{21}I_1=5$ V. Der Eingang zeigt 31 $\Omega$ statt 35 $\Omega$.
:::

::::beispiel
Für das T-Zweitor ist $Z_{1,\mathrm{LL}}=35\,\Omega$ und $Z_{1,\mathrm{KS}}=35\,\Omega-400\,\Omega^2/40\,\Omega=25\,\Omega$, das ist $R_\mathrm{a}+R_\mathrm{b}\parallel R_\mathrm{c}$. Mit $R_\mathrm{L}=60\,\Omega$ wird

$$Z_1=35\,\Omega-\frac{400\,\Omega^2}{100\,\Omega}=31\,\Omega,\quad I_1=\frac{9\,\mathrm{V}}{5\,\Omega+31\,\Omega}=250\,\mathrm{mA},\quad I_2=-\frac{20}{100}\,I_1=-50\,\mathrm{mA}.$$

Am Eingang ist $U_1=9\,\mathrm{V}-5\,\Omega\cdot250\,\mathrm{mA}=7{,}75$ V, am Ausgang $U_2=60\,\Omega\cdot50\,\mathrm{mA}=3$ V. In $R_\mathrm{b}$ fließen $I_1+I_2=200$ mA statt 250 mA, das senkt $U_1$ um genau 1 V (Abb. [5](#abb-5)). Von der Last aus gesehen: $U_\mathrm{i}=\frac{20}{40}\cdot9\,\mathrm{V}=4{,}5$ V, $R_\mathrm{i}=40\,\Omega-400\,\Omega^2/40\,\Omega=30\,\Omega$. Dann ist $I=4{,}5\,\mathrm{V}/90\,\Omega=50$ mA, derselbe Strom. Die Ersatzquelle aus [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) steckt also in den vier Zahlen.
::::

⁠**Grenzfälle:** $R_\mathrm{L}\to\infty$ ergibt $Z_1\to35\,\Omega$, $R_\mathrm{L}\to0$ ergibt $25\,\Omega$. Jede Last liegt dazwischen.

:::frage Die Last hängt nur an Tor 2. Woher weiß der Eingang von ihr?
Von den gemeinsamen Bauteilen. Im T-Zweitor führen beide Tore durch $R_\mathrm{b}$, sein Spannungsabfall hängt von $I_1+I_2$ ab. Allgemein ist $Z_{12}$ das Maß für diese Kopplung. Eine Signalübertragung zurück braucht es nicht, die Spannungen stellen sich im Netzwerk gemeinsam ein.
:::

:::ltspice T-Zweitor im Betrieb
⁠**Zeichnen:** Quelle `voltage` mit `9` von `q` nach Masse, `res` mit `5` von `q` nach `1`, `Ra` mit `15` von `1` nach `m`, `Rb` mit `20` von `m` nach Masse, `Rc` mit `20` von `m` nach `2`, `RL` mit `{RL}` von `2` nach Masse.

⁠**Direktiven:** `.param RL=60`, `.op`, `.meas op Uein FIND V(1)`, `.meas op Iein FIND I(Ra)`, `.meas op Zein PARAM Uein/Iein`, `.meas op Uaus FIND V(2)`.

⁠**Was du siehst:** $\mathtt{V(1)}=7{,}75$ V, $\mathtt{I(Ra)}=250$ mA, `Zein` $=31\,\Omega$, $\mathtt{V(2)}=3$ V. Mit `RL=1m` wird `Zein` 25,0 $\Omega$, mit `RL=1G` 35,0 $\Omega$ und $\mathtt{V(2)}=4{,}5$ V, die Spannung $U_\mathrm{i}$. Setze `RL=10` und prüfe Aufgabe [4](#aufg-4)(a) und (c).
:::

:::aufgabe Aufgabe 4 ★★ Die Last am T-Zweitor
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Wie groß ist $Z_1$ für $R_\mathrm{L}=10\,\Omega$?

</li>

<li>

Bei welcher Last zeigt der Eingang $Z_1=30\,\Omega$?

</li>

<li>

Berechne für $R_\mathrm{L}=10\,\Omega$ mit Quelle die Ströme $I_1$, $I_2$ und $U_2$. Prüfe den Laststrom mit der Ersatzquelle.

</li>

</ol>

:::loesung
(a) $Z_1=35\,\Omega-400\,\Omega^2/50\,\Omega=27\,\Omega$. (b) $400\,\Omega^2/(40\,\Omega+R_\mathrm{L})=5\,\Omega$, also $R_\mathrm{L}=40\,\Omega$. (c) $I_1=9\,\mathrm{V}/32\,\Omega=281{,}25$ mA, $I_2=-\frac{20}{50}I_1=-112{,}5$ mA, $U_2=1{,}125$ V. Die Ersatzquelle ergibt $4{,}5\,\mathrm{V}/(30\,\Omega+10\,\Omega)=112{,}5$ mA.
:::
:::

::::formelsammlung
**Last an Tor 2**

$$U_2=-Z_\mathrm{L}I_2$$

Das Minus steht, weil $I_2$ in das Zweitor zeigt und damit gegen den Strom durch die Last.

**Eingangswiderstand bei Last**

$$I_2=-\frac{Z_{21}}{Z_{22}+Z_\mathrm{L}}\,I_1,\qquad Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}$$

Der Bruch ist der Betrag, um den die Last den Eingangswiderstand ändert (Rückwirkung über $Z_{12}$). Ist $Z_{12}=0$, ist er null: Das Zweitor ist rückwirkungsfrei. Das Zweitor muss linear sein.

**Leerlauf- und Kurzschlusseingangswiderstand**

$$Z_{1,\mathrm{LL}}=Z_{11},\qquad Z_{1,\mathrm{KS}}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}}$$

Grenzfälle $Z_\mathrm{L}\to\infty$ und $Z_\mathrm{L}=0$; der Eingangswiderstand liegt für jede Last dazwischen.

**Ausgang als Ersatzspannungsquelle**

$$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q},\qquad R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}$$

Eine lineare Quelle $U_\mathrm{q}$, $R_\mathrm{q}$ speist Tor 1. $R_\mathrm{i}$ ist der Eingangswiderstand mit vertauschten Indizes, Tor 1 durch $R_\mathrm{q}$ abgeschlossen.
::::

::::lernkarten
:::karte begriff Rückwirkung
Was bezeichnet man bei einem Zweitor als Rückwirkung, und über welchen Parameter der Z-Form kommt sie zustande?
---
Die Wirkung des Ausgangs auf den Eingang. Entnimmt die Last Tor 2 einen Strom $I_2$, erscheint er über die Quelle $Z_{12}I_2$ als Spannung am Eingang.
--- falsch
Die Wirkung des Eingangs auf den Ausgang. Ein Strom $I_1$ erscheint über die Quelle $Z_{21}I_1$ als Spannung am Ausgang und treibt dort den Laststrom.
--- falsch
Den Strom, den die Last an die Quelle zurückschickt. Er fließt über die Masseleitung zum Eingang zurück und wird dabei durch $Z_{22}$ begrenzt.
--- falsch
Die Wirkung des Ausgangs auf den Eingang. Sie kommt über $Z_{11}$ zustande, weil die Last den Eingangsleerlaufwiderstand selbst verändert.
:::
:::karte formel Last an Tor 2
Welche Gleichung beschreibt die Last $Z_\mathrm{L}$ an Tor 2, und warum steht darin ein Minus?
---
$U_2=-Z_\mathrm{L}I_2$. Das Minus steht, weil $I_2$ in das Zweitor zeigt und damit gegen den Strom durch die Last.
--- falsch
$U_2=Z_\mathrm{L}I_2$. Ein Minus ist hier nicht nötig, weil Spannung und Strom an einer Last immer dieselbe Richtung haben.
--- falsch
$U_2=Z_\mathrm{L}I_2-U_1$. Das Minus steht, weil an der Last nur ankommt, was am Eingang nicht schon abgefallen ist.
--- falsch
$U_2=-Z_\mathrm{L}I_2$. Das Minus steht, weil die Spannung an der Last der Torspannung $U_2$ entgegengerichtet ist.
:::
:::karte formel Eingangswiderstand bei Last
Wie groß ist der Eingangswiderstand $Z_1$ eines linearen Zweitors, an dessen Tor 2 die Last $Z_\mathrm{L}$ hängt?
---
$Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}$. Der Bruch ist der Betrag, um den die Last den Eingangswiderstand ändert; bei $Z_{12}=0$ ist er null.
--- falsch
$Z_1=Z_{11}+Z_\mathrm{L}$. Die Last liegt über das Zweitor in Reihe zum Eingangsleerlaufwiderstand, deshalb addieren sich die beiden Widerstände einfach.
--- falsch
$Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{11}+Z_\mathrm{L}}$. Der Bruch ist der Betrag, um den die Last den Eingangswiderstand ändert; bei $Z_{12}=0$ ist er null.
--- falsch
$Z_1=\frac{U_1}{I_1}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}$. Der Bruch ist die auf den Eingang umgerechnete Last; er bleibt auch bei $Z_{12}=0$ bestehen.
:::
:::karte formel Leerlauf- und Kurzschlusseingangswiderstand
Zwischen welchen Grenzwerten liegt der Eingangswiderstand $Z_1$ eines Zweitors für jede Last, und wie lauten sie?
---
Zwischen $Z_{1,\mathrm{LL}}=Z_{11}$ im Leerlauf, $Z_\mathrm{L}\to\infty$, und $Z_{1,\mathrm{KS}}=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}}$ im Kurzschluss, $Z_\mathrm{L}=0$. Beim T-Zweitor sind das 35 $\Omega$ und 25 $\Omega$.
--- falsch
Zwischen $Z_{11}$ für $Z_\mathrm{L}=0$ und $Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}}$ für $Z_\mathrm{L}\to\infty$. Beim T-Zweitor sind das 35 $\Omega$ im Kurzschluss und 25 $\Omega$ im Leerlauf.
--- falsch
Zwischen null für $Z_\mathrm{L}=0$ und $Z_{11}$ für $Z_\mathrm{L}\to\infty$, weil ein Kurzschluss am Ausgang auch den Eingang kurzschließt. Beim T-Zweitor sind das 0 und 35 $\Omega$.
--- falsch
Zwischen $Z_{11}$ im Leerlauf und $Z_{11}+Z_{22}$ im Kurzschluss, weil die Last den Ausgangsleerlaufwiderstand zum Eingang hinzufügt. Beim T-Zweitor sind das 35 und 75 $\Omega$.
:::
:::karte begriff rückwirkungsfrei
Wann heißt ein Zweitor rückwirkungsfrei, und was merkt sein Eingang dann von der Last?
---
Wenn $Z_{12}=0$ ist. Dann ist der Bruch im Eingangswiderstand null, der Eingangswiderstand ist für jede Last $Z_{11}$, und der Eingang merkt nichts von der Last.
--- falsch
Wenn $Z_{11}=Z_{22}$ ist. Dann sehen Eingang und Ausgang denselben Widerstand, und keine der beiden Seiten kann auf die andere zurückwirken.
--- falsch
Wenn $Z_{12}=Z_{21}$ ist. Dann wirkt das Zweitor in beide Richtungen gleich stark, und die Wirkungen der Last auf den Eingang heben sich gegenseitig auf.
--- falsch
Wenn die Last sehr groß ist. Dann fließt kaum Ausgangsstrom, und der Eingang merkt nichts von der Last, gleich welche Parameter das Zweitor hat.
:::
:::karte zusammenhang Rückwirkung im T-Zweitor
Warum sinkt der Eingangswiderstand des T-Zweitors, wenn man an Tor 2 eine Last anschließt?
---
Ein Teil des Stroms, der sonst durch $R_\mathrm{b}$ flösse, weicht über $R_\mathrm{c}$ zur Last aus. An $R_\mathrm{b}$ fällt weniger ab, $U_1$ sinkt, und der Eingang wirkt niederohmiger.
--- falsch
Weil die Last über das Zweitor parallel zum Eingang liegt und so den Widerstand zwischen den Klemmen 1 und 1$'$ unmittelbar verkleinert.
--- falsch
Er sinkt nicht, sondern steigt: Die Last liegt in Reihe hinter $R_\mathrm{c}$, und der Strom muss nun zusätzlich durch einen weiteren Widerstand fließen, die Last selbst.
--- falsch
Weil durch $R_\mathrm{b}$ nun mehr Strom fließt als vorher. Der größere Strom bei gleicher Spannung bedeutet einen kleineren Widerstand am Eingang.
:::
:::karte formel Ausgang als Ersatzspannungsquelle
Welche Ersatzspannungsquelle sieht die Last an Tor 2, wenn eine lineare Quelle $U_\mathrm{q}$, $R_\mathrm{q}$ Tor 1 speist?
---
$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q}$ und $R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}$. Beim T-Zweitor mit 9 V und 5 $\Omega$ sind das 4,5 V und 30 $\Omega$.
--- falsch
$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}}\,U_\mathrm{q}$ und $R_\mathrm{i}=Z_{22}$, weil der Quellwiderstand bei offenem Tor 2 keinen Einfluss hat. Beim T-Zweitor sind das 5,14 V und 40 $\Omega$.
--- falsch
$U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q}$ und $R_\mathrm{i}=Z_{22}+R_\mathrm{q}$, weil der Quellwiderstand in Reihe zum Ausgangsleerlaufwiderstand liegt. Beim T-Zweitor sind das 4,5 V und 45 $\Omega$.
--- falsch
$U_\mathrm{i}=U_\mathrm{q}$ und $R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}$, weil im Leerlauf die volle Quellenspannung am Ausgang ankommt. Beim T-Zweitor sind das 9 V und 30 $\Omega$.
:::
:::karte herleitung Eingangswiderstand bei Last
Leite aus den Gleichungen der Z-Form und der Lastgleichung $U_2=-Z_\mathrm{L}I_2$ den Eingangswiderstand $Z_1$ her.
---
Die rechte Masche gibt $U_2=Z_{21}I_1+Z_{22}I_2=-Z_\mathrm{L}I_2$, weil die Last an Tor 2 dieselbe Spannung $U_2$ trägt.
---
Nach $I_2$ umgestellt folgt $I_2=-\frac{Z_{21}}{Z_{22}+Z_\mathrm{L}}\,I_1$, weil man alle Glieder mit $I_2$ auf eine Seite bringt und durch $Z_{22}+Z_\mathrm{L}$ teilt.
---
Eingesetzt in die linke Masche $U_1=Z_{11}I_1+Z_{12}I_2$ ist $U_1$ ein Vielfaches von $I_1$ allein, weil $I_2$ nun durch $I_1$ ausgedrückt ist.
---
Durch $I_1$ geteilt folgt $Z_1=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}$, weil der Eingangswiderstand der Quotient aus $U_1$ und $I_1$ ist.
---
Für $Z_\mathrm{L}\to\infty$ fällt der Bruch weg, für $Z_\mathrm{L}=0$ folgt $Z_{1,\mathrm{KS}}$, weil der Nenner dann unendlich groß bzw. gleich $Z_{22}$ wird.
:::
:::karte herleitung Ersatzquelle am Ausgang
Leite aus der Z-Form her, welche Ersatzspannungsquelle mit $U_\mathrm{i}$ und $R_\mathrm{i}$ die Last an Tor 2 sieht, wenn eine Quelle $U_\mathrm{q}$, $R_\mathrm{q}$ Tor 1 speist.
---
Die Quelle gibt $U_1=U_\mathrm{q}-R_\mathrm{q}I_1$ vor, weil an ihrem Innenwiderstand die Spannung $R_\mathrm{q}I_1$ abfällt.
---
Für die Leerlaufspannung ist Tor 2 offen, also $I_2=0$ und $U_1=Z_{11}I_1$; daraus folgt $I_1=U_\mathrm{q}/(Z_{11}+R_\mathrm{q})$, weil Quelle und Eingang denselben Strom führen.
---
Es ist $U_\mathrm{i}=Z_{21}I_1$, also $U_\mathrm{i}=\frac{Z_{21}}{Z_{11}+R_\mathrm{q}}\,U_\mathrm{q}$, weil bei $I_2=0$ in der zweiten Gleichung nur der Anteil von $I_1$ bleibt.
---
Für $R_\mathrm{i}$ setzt man $U_\mathrm{q}=0$; dann ist Tor 1 durch $R_\mathrm{q}$ abgeschlossen, weil von der Quelle nur ihr Innenwiderstand übrig bleibt.
---
$R_\mathrm{i}$ ist nun $Z_1$ mit vertauschten Indizes und $R_\mathrm{q}$ als Last, also $R_\mathrm{i}=Z_{22}-\frac{Z_{12}Z_{21}}{Z_{11}+R_\mathrm{q}}$, weil man jetzt von Tor 2 aus auf ein an Tor 1 belastetes Zweitor blickt.
:::
::::
