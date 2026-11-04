---
title: Normen: die Größe eines Vektors
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6210400
summary: Wie groß ist ein Vektor?
tags: euklidische Norm, Länge, normiert, normieren, Betragssummennorm, Maximumnorm, Norm, Dreiecksungleichung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Wie groß ist ein Vektor? Darauf gibt es mehrere richtige Antworten. Dieser Abschnitt stellt die drei wichtigsten vor, klärt, was sie gemeinsam haben, und zeigt, wozu man sie braucht: um zu messen, wie groß ein Fehler ist.
:::

### Die euklidische Norm

<span class="anker" id="stufe-3-1"></span>

Die naheliegende Größe eines Pfeils ist seine Länge. In der Ebene liefert sie der Satz des Pythagoras: Der Pfeil $(3,\,-4)^{\top}$ ist die Hypotenuse eines rechtwinkligen Dreiecks mit den Katheten $3$ und $4$, also ist er $\sqrt{3^2+4^2}=5$ lang. Im Raum wendet man Pythagoras zweimal an und bekommt die Wurzel aus der Summe der drei Quadrate. Dieselbe Formel benutzt man in jeder Dimension.

:::definition Definition 3.1 (Euklidische Norm)
<span class="anker" id="satz-3-1"></span>

Die __euklidische Norm__ eines Vektors $\mathbf{x}\in\mathbb{R}^d$ ist

<span class="anker" id="gl-3-1"></span>
$$\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}=\sqrt{x_1^2+x_2^2+\dots+x_d^2} . \tag{3.1}$$

Ohne Index meint $\lVert\mathbf{x}\rVert$ in dieser Reihe immer die euklidische Norm.
:::

Man nennt sie auch die __Länge__ des Vektors oder, wegen der Quadrate, die $L_2$-Norm. Ein Vektor der Länge $1$ heißt __normiert__. Teilt man einen Vektor $\mathbf{x}\ne\mathbf{0}$ durch seine Länge, so ist $\mathbf{x}/\lVert\mathbf{x}\rVert$ normiert und zeigt in dieselbe Richtung. Diesen Schritt nennt man __normieren__.

⁠**Rechenbeispiel:** $\lVert(3,\,-4)^{\top}\rVert=\sqrt{9+16}=5$, normiert $(0{,}6,\,-0{,}8)^{\top}$. Im Raum ist $\lVert(1,\,2,\,2)^{\top}\rVert=\sqrt{1+4+4}=3$.

⁠**Kurz gesagt:** Die euklidische Norm ist die Länge des Pfeils, die Wurzel aus der Quadratsumme der Komponenten.

### Die Betragssummennorm

<span class="anker" id="stufe-3-2"></span>

In einer Stadt mit rechtwinkligem Straßennetz kann ein Taxi nicht schräg durch die Häuserblöcke fahren. Um vom Nullpunkt zum Punkt $(3,\,-4)^{\top}$ zu kommen, fährt es $3$ Blöcke in die eine und $4$ Blöcke in die andere Richtung, zusammen $7$ Blöcke. Diese Länge misst die Betragssummennorm.

:::definition Definition 3.2 (Betragssummennorm)
<span class="anker" id="satz-3-2"></span>

Die __Betragssummennorm__ eines Vektors $\mathbf{x}\in\mathbb{R}^d$ ist

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{x}\rVert_1=|x_1|+|x_2|+\dots+|x_d|=\sum_{j=1}^d|x_j| . \tag{3.2}$$
:::

Man nennt sie auch $L_1$-Norm oder, nach dem Straßennetz von Manhattan, Manhattan-Norm.

⁠**Rechenbeispiel:** $\lVert(3,\,-4)^{\top}\rVert_1=3+4=7$ und $\lVert(1,\,2,\,2)^{\top}\rVert_1=5$. Die Betragssummennorm ist hier größer als die euklidische Länge, weil der Umweg über die Straßen länger ist als die Luftlinie.

⁠**Kurz gesagt:** Die Betragssummennorm addiert die Beträge der Komponenten; sie ist der Weg durch ein rechtwinkliges Straßennetz.

### Die Maximumnorm

<span class="anker" id="stufe-3-3"></span>

Bei einer Qualitätsprüfung interessiert oft nur die schlimmste Abweichung. Ein Bauteil hat drei Maße, und jedes darf höchstens $0{,}1$ mm vom Sollwert abweichen. Ob das Teil in Ordnung ist, entscheidet allein die größte der drei Abweichungen.

:::definition Definition 3.3 (Maximumnorm)
<span class="anker" id="satz-3-3"></span>

Die __Maximumnorm__ eines Vektors $\mathbf{x}\in\mathbb{R}^d$ ist der größte Betrag einer Komponente:

<span class="anker" id="gl-3-3"></span>
$$\lVert\mathbf{x}\rVert_\infty=\max_{j=1,\dots,d}|x_j| . \tag{3.3}$$
:::

Man nennt sie auch $L_\infty$-Norm. Der Grund für das Unendlichzeichen steht im nächsten Unterabschnitt.

⁠**Rechenbeispiel:** $\lVert(3,\,-4)^{\top}\rVert_\infty=4$ und $\lVert(1,\,2,\,2)^{\top}\rVert_\infty=2$. Sind die Abweichungen eines Bauteils $(0{,}05;\ -0{,}08;\ 0{,}02)$ mm, so ist ihre Maximumnorm $0{,}08$ mm und das Teil in Ordnung.

⁠**Kurz gesagt:** Die Maximumnorm ist der größte Betrag einer Komponente, die schlimmste Einzelabweichung.

### Was eine Norm ausmacht

<span class="anker" id="stufe-3-4"></span>

Die drei Normen messen verschieden, aber sie haben drei Eigenschaften gemeinsam, die man von jedem Größenmaß erwartet. Nur der Nullvektor hat die Größe null. Ein doppelt so langer Vektor ist doppelt so groß. Und ein Umweg ist nie kürzer als der direkte Weg.

:::definition Definition 3.4 (Norm)
<span class="anker" id="satz-3-4"></span>

Eine __Norm__ auf dem $\mathbb{R}^d$ ordnet jedem Vektor $\mathbf{x}$ eine reelle Zahl $\lVert\mathbf{x}\rVert$ zu, sodass für alle $\mathbf{u},\mathbf{v},\mathbf{x}\in\mathbb{R}^d$ und alle Skalare $c$ gilt:

<ol>

<li>

$\lVert\mathbf{x}\rVert\ge0$, und $\lVert\mathbf{x}\rVert=0$ nur für $\mathbf{x}=\mathbf{0}$;

</li>

<li>

$\lVert c\,\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$;

</li>

<li>

$\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ (__Dreiecksungleichung__).

</li>

</ol>
:::

Die Dreiecksungleichung hat ihren Namen von einem Dreieck aus den Pfeilen $\mathbf{u}$, $\mathbf{v}$ und $\mathbf{u}+\mathbf{v}$: Die Seite $\mathbf{u}+\mathbf{v}$ ist nie länger als die beiden anderen zusammen.

**Die $p$-Normen.** Die Betragssummennorm und die euklidische Norm sind zwei Fälle einer ganzen Familie. Für jede Zahl $p\ge1$ ist die __$p$-Norm__

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{x}\rVert_p=\Bigl(\sum_{j=1}^d|x_j|^p\Bigr)^{1/p} . \tag{3.4}$$

Für $p=1$ ist das die Betragssummennorm, für $p=2$ die euklidische Norm. Je größer $p$, desto stärker überwiegt in der Summe die größte Komponente. Für $p\to\infty$ bleibt nur sie übrig; deshalb heißt die Maximumnorm $\lVert\cdot\rVert_\infty$.

**Die Einheitskugel.** Wie eine Norm misst, sieht man an der Menge aller Vektoren der Größe $1$. Sie heißt __Einheitskugel__ der Norm, auch wenn sie keine Kugel sein muss (Abb. [4](#abb-4)). Für die euklidische Norm ist sie in der Ebene der Kreis mit Radius $1$. Für die Betragssummennorm ist sie die Raute $|x_1|+|x_2|=1$: In jedem Quadranten ist das eine Strecke, zum Beispiel $x_1+x_2=1$ für $x_1,x_2\ge0$. Für die Maximumnorm ist sie das Quadrat mit den Ecken $(\pm1,\,\pm1)$, denn dort ist die größere der beiden Komponenten dem Betrag nach genau $1$.

:::abbildung ml/k1einheitskugeln 4
Die Einheitskugeln dreier Normen in der Ebene: die Raute der Betragssummennorm (links, orange), der Kreis der euklidischen Norm (Mitte, blau) und das Quadrat der Maximumnorm (rechts, grün); grau jeweils die beiden anderen zum Vergleich. Alle drei gehen durch die Punkte $(\pm1,\,0)$ und $(0,\,\pm1)$.
:::

⁠**Rechenbeispiel:** Für $\mathbf{x}=(3,\,-4)^{\top}$ ist $\lVert\mathbf{x}\rVert_1=7$, $\lVert\mathbf{x}\rVert_2=5$, $\lVert\mathbf{x}\rVert_3=(27+64)^{1/3}=91^{1/3}\approx4{,}498$, $\lVert\mathbf{x}\rVert_{10}=(3^{10}+4^{10})^{1/10}\approx4{,}022$ und $\lVert\mathbf{x}\rVert_\infty=4$. Mit wachsendem $p$ nähert sich die $p$-Norm der größten Komponente $4$.

Dass die Betragssummennorm die Bedingungen (N1) bis (N3) erfüllt, rechnet man direkt nach: (N1) und (N2) gelten, weil $|x_j|\ge0$ und $|c\,x_j|=|c|\,|x_j|$ ist. (N3) folgt aus der Dreiecksungleichung für Zahlen, $|u_j+v_j|\le|u_j|+|v_j|$, summiert über alle $j$. Für die Maximumnorm geht es ebenso. Für die euklidische Norm ist die Dreiecksungleichung anschaulich klar, weil der direkte Weg zwischen zwei Punkten nie länger ist als ein Umweg über einen dritten Punkt.

⁠**Kurz gesagt:** Eine Norm misst die Größe eines Vektors so, dass nur der Nullvektor die Größe null hat, Vielfache entsprechend wachsen und die Dreiecksungleichung gilt; die $p$-Normen bilden eine Familie, zu der $L_1$, $L_2$ und $L_\infty$ gehören.

:::hintergrund Warum $p\ge1$ sein muss und warum die „Nullnorm“ keine Norm ist
Für $p<1$ verletzt die Formel [(3.4)](#gl-3-4) die Dreiecksungleichung. Mit $p=\tfrac12$ ist $\lVert(1,0)^{\top}\rVert_{1/2}=1$ und $\lVert(0,1)^{\top}\rVert_{1/2}=1$, aber $\lVert(1,1)^{\top}\rVert_{1/2}=(1+1)^2=4>1+1$. Ihre „Einheitskugel“ ist nach innen eingebeult, sie hat die Form eines Sterns.

Oft liest man von einer „$L_0$-Norm“: der Zahl der Komponenten, die nicht null sind. Sie ist ein nützliches Maß dafür, wie viele Merkmale ein Vektor überhaupt benutzt. Eine Norm ist sie trotzdem nicht, denn sie verletzt (N2): Der Vektor $2\mathbf{x}$ hat genauso viele Komponenten ungleich null wie $\mathbf{x}$, nicht doppelt so viele.
:::

:::hintergrund Nicht jede Norm kommt von einem Skalarprodukt
Die euklidische Norm ist aus dem Skalarprodukt gebaut, $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$. Daraus folgt eine Gleichung, die man die Parallelogrammgleichung nennt. Multipliziert man mit den Rechenregeln des Skalarprodukts aus, so ist

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,\qquad \lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,$$

und die Summe beider Zeilen ergibt $\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$: In einem Parallelogramm ist die Quadratsumme der beiden Diagonalen gleich der Quadratsumme der vier Seiten. Jede Norm, die aus einem Skalarprodukt stammt, muss diese Gleichung erfüllen. Die Betragssummennorm tut es nicht: Mit $\mathbf{u}=\mathbf{e}_1$ und $\mathbf{v}=\mathbf{e}_2$ ist links $\lVert(1,1)^{\top}\rVert_1^2+\lVert(1,-1)^{\top}\rVert_1^2=4+4=8$, rechts aber $2+2=4$. Es gibt also kein Skalarprodukt, dessen Länge die Betragssummennorm ist. Winkel, wie sie das Skalarprodukt liefert, kann man mit ihr deshalb nicht messen.
:::

### Der Fehlervektor und seine Größe

<span class="anker" id="stufe-3-5"></span>

Ein Modell liefert Vorhersagen, und irgendwann erfährt man die tatsächlichen Werte. Dann will man wissen, wie gut die Vorhersagen waren. Für jedes Beispiel gibt es eine Abweichung, und diese Abweichungen bilden einen Vektor. Seine Norm ist ein Maß für die Größe des Fehlers insgesamt.

:::definition Definition 3.5 (Fehlervektor)
<span class="anker" id="satz-3-5"></span>

Sind $\hat y_1,\dots,\hat y_N$ die Vorhersagen eines Modells für $N$ Beispiele und $y_1,\dots,y_N$ die tatsächlichen Werte, so heißt der Vektor

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{y}}-\mathbf{y}=(\hat y_1-y_1,\,\dots,\,\hat y_N-y_N)^{\top} \tag{3.5}$$

der __Fehlervektor__. Dabei ist $\hat{\mathbf{y}}=(\hat y_1,\dots,\hat y_N)^{\top}$ der Vektor der Vorhersagen und $\mathbf{y}=(y_1,\dots,y_N)^{\top}$ der Vektor der tatsächlichen Werte.
:::

Welche Norm man auf den Fehlervektor anwendet, ist eine Entscheidung darüber, welche Fehler man am meisten scheut. Das Vorzeichen spielt dabei keine Rolle, denn jede Norm gibt $\mathbf{y}-\hat{\mathbf{y}}$ dieselbe Größe wie $\hat{\mathbf{y}}-\mathbf{y}$.

⁠**Rechenbeispiel:** Die vier Wohnungen wurden verkauft, die tatsächlichen Preise waren $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ Tausend Euro. Zwei Gutachter A und B hatten vorher geschätzt:

$$\hat{\mathbf{y}}_{\mathrm A}=(210,\,120,\,300,\,230)^{\top},\qquad \hat{\mathbf{y}}_{\mathrm B}=(200,\,130,\,290,\,280)^{\top}.$$

Ihre Fehlervektoren sind $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}=(10,\,-10,\,10,\,-10)^{\top}$ und $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}=(0,\,0,\,0,\,40)^{\top}$. Gutachter A liegt immer ein wenig daneben, Gutachter B dreimal genau und einmal weit daneben. Die drei Normen urteilen verschieden (Tabelle [2](#tab-2)).

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die Normen der Fehlervektoren zweier Gutachter, in Tausend Euro.

|  | $\lVert\cdot\rVert_1$ | $\lVert\cdot\rVert_2$ | $\lVert\cdot\rVert_\infty$ |
|---|---|---|---|
| Gutachter A, $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}$ | $40$ | $\sqrt{4\cdot100}=20$ | $10$ |
| Gutachter B, $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}$ | $40$ | $\sqrt{1600}=40$ | $40$ |

Nach der Betragssummennorm sind beide gleich gut: Beide liegen zusammen um $40$ Tausend Euro daneben. Nach der euklidischen Norm ist A doppelt so gut, nach der Maximumnorm viermal so gut. Wer jeden Tausender Abweichung gleich schlimm findet, egal bei welcher Wohnung, misst mit $L_1$. Wer einen großen Ausreißer schlimmer findet als viele kleine Fehler, misst mit $L_2$. Wer nur den schlimmsten Fall fürchtet, misst mit $L_\infty$.

⁠**Kurz gesagt:** Der Fehlervektor sammelt die Abweichungen aller Vorhersagen; seine Norm misst die Größe des Fehlers, und die Wahl der Norm legt fest, welche Fehler besonders zählen.

:::hintergrund Warum die Quadratsumme große Fehler bestraft und kleine fast übersieht
In der euklidischen Norm geht jede Abweichung als Quadrat ein. Eine Abweichung von $0{,}1$ trägt $0{,}01$ bei, eine Abweichung von $10$ aber $100$. Das Quadrat macht kleine Zahlen kleiner und große Zahlen größer. Ein einzelner großer Fehler von $40$ trägt deshalb $1600$ bei, viermal so viel wie vier Fehler von je $10$ zusammen. Die Betragssummennorm dagegen wächst überall gleich schnell: Jede Einheit Abweichung kostet gleich viel, ob sie zu einem kleinen oder einem großen Fehler gehört. Deshalb unterscheidet sie auch deutlich zwischen „genau null“ und „ein wenig daneben“, während die Quadratsumme zwischen den beiden kaum einen Unterschied macht. Welche Eigenschaft man will, hängt von der Aufgabe ab, und genau deshalb gibt es mehrere Normen.
:::

### Der Effektivwert

<span class="anker" id="stufe-3-6"></span>

Die euklidische Norm wächst mit der Zahl der Komponenten. Bewertet man einen Gutachter an vier Wohnungen und einen anderen an vierhundert, so hat der zweite einen viel längeren Fehlervektor, auch wenn er pro Wohnung genauso gut schätzt. Will man Fehler pro Beispiel vergleichen, muss man die Zahl der Komponenten herausrechnen.

:::definition Definition 3.6 (Effektivwert)
<span class="anker" id="satz-3-6"></span>

Der __Effektivwert__ eines Vektors $\mathbf{x}\in\mathbb{R}^n$ ist

<span class="anker" id="gl-3-6"></span>
$$\operatorname{rms}(\mathbf{x})=\frac{\lVert\mathbf{x}\rVert}{\sqrt n}=\sqrt{\frac1n\sum_{i=1}^nx_i^2} . \tag{3.6}$$
:::

Die Abkürzung rms steht für *root mean square*: die Wurzel aus dem Mittelwert der Quadrate. Der Effektivwert ist ein typischer Betrag einer Komponente. Haben alle Komponenten denselben Betrag $a$, ist der Effektivwert genau $a$.

Aus der Elektrotechnik kennt man den Namen: Der Effektivwert einer Wechselspannung ist die Wurzel aus dem zeitlichen Mittel ihres Quadrats. Für ein abgetastetes Signal ist [(3.6)](#gl-3-6) dieselbe Rechnung mit Abtastwerten statt eines Integrals. Tastet man einen Sinus über genau eine Periode an $n\ge3$ gleichmäßig verteilten Stellen ab, kommt sogar exakt der Effektivwert $1/\sqrt2$ des Sinus heraus.

⁠**Rechenbeispiel:** Die Fehlervektoren der Gutachter aus dem vorigen Unterabschnitt haben die Effektivwerte $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y})=20/\sqrt4=10$ und $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y})=40/\sqrt4=20$ Tausend Euro: A liegt typischerweise um $10$ Tausend Euro daneben. Der Sinus mit den Abtastwerten $(0,\,1,\,0,\,-1)^{\top}$ hat $\operatorname{rms}=\sqrt{2/4}=1/\sqrt2\approx0{,}707$.

⁠**Kurz gesagt:** Der Effektivwert $\lVert\mathbf{x}\rVert/\sqrt n$ ist der typische Betrag einer Komponente und macht Vektoren verschiedener Länge vergleichbar.

:::hintergrund Wie viele Komponenten können groß sein?
Der Effektivwert begrenzt, wie viele Komponenten einen großen Betrag haben können. Haben $k$ der $n$ Komponenten einen Betrag von mindestens $a>0$, so tragen allein diese $k$ Komponenten mindestens $k\,a^2$ zur Quadratsumme bei. Die ganze Quadratsumme ist $n\operatorname{rms}(\mathbf{x})^2$, also ist $k\,a^2\le n\operatorname{rms}(\mathbf{x})^2$ oder

$$\frac kn\le\Bigl(\frac{\operatorname{rms}(\mathbf{x})}{a}\Bigr)^2 .$$

Höchstens der Anteil $(\operatorname{rms}/a)^2$ der Komponenten kann also mindestens $a$ groß sein. Höchstens ein Viertel der Komponenten kann das Doppelte des Effektivwerts erreichen, höchstens ein Prozent das Zehnfache. Beim Gutachter B mit $\operatorname{rms}=20$ können höchstens $(20/30)^2=4/9\approx44$ % der Fehler $30$ oder mehr betragen; tatsächlich ist es einer von vier, also $25$ %. Diese Abschätzung heißt Tschebyscheff-Ungleichung.
:::

:::aufgabe Aufgabe 7 ★ Normen rechnen
<span class="anker" id="aufg-7"></span>

Es sei $\mathbf{x}=(2,\,-1,\,0,\,2)^{\top}$.

<ol class="al">

<li>

Berechne $\lVert\mathbf{x}\rVert_1$, $\lVert\mathbf{x}\rVert_2$, $\lVert\mathbf{x}\rVert_3$ und $\lVert\mathbf{x}\rVert_\infty$ sowie den normierten Vektor $\mathbf{x}/\lVert\mathbf{x}\rVert$.

</li>

<li>

Prüfe $\lVert\mathbf{x}\rVert_\infty\le\lVert\mathbf{x}\rVert_2\le\lVert\mathbf{x}\rVert_1$. Begründe, warum diese Reihenfolge für jeden Vektor gilt.

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{x}\rVert_1=2+1+0+2=5$, $\lVert\mathbf{x}\rVert_2=\sqrt{4+1+0+4}=3$, $\lVert\mathbf{x}\rVert_3=(8+1+0+8)^{1/3}=17^{1/3}\approx2{,}571$ und $\lVert\mathbf{x}\rVert_\infty=2$. Normiert ist $\mathbf{x}/3=(\tfrac23,\,-\tfrac13,\,0,\,\tfrac23)^{\top}$ mit der Länge $\sqrt{(4+1+4)/9}=1$.

(b) Es ist $2\le3\le5$, auch $\lVert\mathbf{x}\rVert_3$ liegt mit $2{,}571$ dazwischen. Allgemein: Ist $|x_k|$ die größte Komponente, so ist $\lVert\mathbf{x}\rVert_\infty^2=x_k^2\le\sum_jx_j^2=\lVert\mathbf{x}\rVert_2^2$, denn die Summe enthält $x_k^2$ und lauter nicht negative weitere Summanden. Und $\lVert\mathbf{x}\rVert_1^2=\bigl(\sum_j|x_j|\bigr)^2=\sum_jx_j^2+\sum_{j\ne l}|x_j|\,|x_l|\ge\lVert\mathbf{x}\rVert_2^2$, weil die gemischten Produkte nicht negativ sind. Anschaulich: Die Luftlinie ist nie länger als der Weg durch das Straßennetz und nie kürzer als die längste Einzelstrecke.
:::
:::

:::aufgabe Aufgabe 8 ★★ Wie gut schätzt die Maklerin?
<span class="anker" id="aufg-8"></span>

Die Maklerin aus Unterabschnitt [2.2](das-skalarprodukt.html#stufe-2-2) hatte die Vorhersagen $\hat{\mathbf{y}}=(188,\,126,\,286,\,232)^{\top}$, die tatsächlichen Preise waren $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ Tausend Euro.

<ol class="al">

<li>

Berechne den Fehlervektor, seine drei Normen und seinen Effektivwert. Bei welcher Wohnung liegt sie am weitesten daneben?

</li>

<li>

Was fällt an den Vorzeichen auf? Die Maklerin addiert ab sofort zu jeder Vorhersage $7$ Tausend Euro. Berechne den neuen Fehlervektor und seine Normen. Ist sie nach allen drei Normen besser geworden?

</li>

</ol>

:::loesung
(a) Der Fehlervektor ist $\hat{\mathbf{y}}-\mathbf{y}=(188-200,\ 126-130,\ 286-290,\ 232-240)^{\top}=(-12,\,-4,\,-4,\,-8)^{\top}$. Seine Normen: $\lVert\cdot\rVert_1=28$, $\lVert\cdot\rVert_2=\sqrt{144+16+16+64}=\sqrt{240}\approx15{,}49$, $\lVert\cdot\rVert_\infty=12$, Effektivwert $\sqrt{240}/2\approx7{,}75$ Tausend Euro. Am weitesten daneben liegt sie bei Wohnung 1, um $12$ Tausend Euro.

(b) Alle Fehler sind negativ: Die Maklerin schätzt durchweg zu niedrig, ihr Fehler hat einen Gleichanteil. Mit $7$ Tausend Euro Zuschlag wird der Fehlervektor zu $(-5,\,3,\,3,\,-1)^{\top}$ mit $\lVert\cdot\rVert_1=12$, $\lVert\cdot\rVert_2=\sqrt{25+9+9+1}=\sqrt{44}\approx6{,}63$, $\lVert\cdot\rVert_\infty=5$ und dem Effektivwert $\sqrt{44}/2\approx3{,}32$. Sie ist nach allen drei Normen besser geworden. Der Zuschlag $7$ ist genau der Mittelwert der Fehlerbeträge, $(12+4+4+8)/4=7$: Er zieht den Gleichanteil des Fehlers ab und lässt nur den Wechselanteil übrig.
:::
:::
