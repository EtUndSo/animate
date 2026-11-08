---
title: Wie gut ist ein Schätzer?
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
knoten: Grundlagen 5: Statistik und Information
nachschlagen: ja
order: 15250300
summary: Ein Schätzer trifft den wahren Parameter fast nie genau.
tags: Verzerrung, erwartungstreu, Standardfehler, mittlere quadratische Fehler, konsistent
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Schätzer trifft den wahren Parameter fast nie genau. Dieser Abschnitt misst, wie weit er im Mittel danebenliegt, zerlegt diesen Fehler in einen systematischen und einen zufälligen Anteil und fragt, ob der Schätzer mit mehr Daten besser wird.
:::

### Verzerrung und Erwartungstreue

<span class="anker" id="stufe-2-1"></span>

Abb. [4](#abb-4) zeigt das Bild, an dem sich die Güte eines Schätzers ablesen lässt. Jeder Punkt ist der Schätzwert aus einem gedachten Datensatz, die Mitte der Scheibe ist der wahre Parameter. Zwei Dinge können schiefgehen. Die Punkte können um eine Stelle neben der Mitte liegen; dann irrt der Schätzer systematisch, auch im Mittel über viele Datensätze. Und die Punkte können weit streuen; dann liegt der einzelne Schätzwert oft weit daneben, selbst wenn der Mittelwert stimmt. Dieser Unterabschnitt misst das Erste, der nächste das Zweite.

:::abbildung ml/k5zielscheibe 4
Schätzwerte aus acht gedachten Datensätzen (blau) und der wahre Parameter (rotes Kreuz in der Mitte). Bei (a) und (b) liegt der Schwerpunkt der Punkte in der Mitte: Der Schätzer ist unverzerrt. Bei (c) und (d) ist der Schwerpunkt um $(0{,}5;\ 0{,}35)$ verschoben: Der Schätzer irrt systematisch. Bei (b) und (d) streuen die Punkte $4$-mal so weit wie bei (a) und (c). Die Scheibe ist zweidimensional, damit man die Punkte unterscheiden kann; ein einzelner Parameter entspricht einer Linie durch die Mitte.
:::

:::definition Definition 2.1 (Verzerrung, Erwartungstreue)
<span class="anker" id="satz-2-1"></span>

Die __Verzerrung__ (englisch *bias*) eines Schätzers $\hat\theta$ für $\theta$ ist

<span class="anker" id="gl-2-1"></span>
$$\operatorname{Bias}(\hat\theta)=\mathbb{E}[\hat\theta]-\theta . \tag{2.1}$$

Der Schätzer heißt __erwartungstreu__ oder unverzerrt, wenn seine Verzerrung für jeden Wert des Parameters null ist.
:::

Der Erwartungswert ist der über die Stichprobenverteilung, bei festem wahrem $\theta$. Ein erwartungstreuer Schätzer liegt also im Mittel über alle gedachten Datensätze genau richtig. Dass er für *jeden* Wert des Parameters stimmen muss, ist wesentlich: Ein Schätzer, der nur zufällig beim wahren Wert richtig liegt, nützt nichts, denn den wahren Wert kennt man nicht.

:::warnung Zwei Bedeutungen von „bias“
Englische Texte nennen auch den Achsenabschnitt $b$ einer affinen Vorschrift $\mathbf{w}^{\top}\mathbf{x}+b$ aus [Grundlagen 1, Abschnitt 8.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-5), „bias“. Das hat mit der Verzerrung eines Schätzers nichts zu tun. Dieses Kapitel sagt deshalb immer „Verzerrung“ und schreibt $\operatorname{Bias}(\hat\theta)$ nur als Formelzeichen.
:::

⁠**Rechenbeispiel:** Der Mittelwert $\bar X$ ist für jede Verteilung mit Erwartungswert $\mu$ ein erwartungstreuer Schätzer für $\mu$, denn nach der Linearität aus [Grundlagen 4, Abschnitt 7.3](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-3), ist

$$\mathbb{E}[\bar X]=\frac1N\sum_{i=1}^N\mathbb{E}[X_i]=\frac1N\cdot N\mu=\mu .$$

Für Münzwürfe ist $\bar X=N_1/N$, also ist auch der Anteil der Köpfe erwartungstreu. Im Beispiel des vorigen Unterabschnitts war $\mathbb{E}[\bar X]=2=\mu$. Der erste Wurf $X_1$ ist ebenfalls erwartungstreu, denn $\mathbb{E}[X_1]=\mu$. Die feste Zahl $0{,}5$ hat die Verzerrung $0{,}5-\theta$; sie ist nur für $\theta=0{,}5$ null, der Schätzer ist also nicht erwartungstreu.

⁠**Kurz gesagt:** Die Verzerrung ist der systematische Fehler $\mathbb{E}[\hat\theta]-\theta$; ein erwartungstreuer Schätzer liegt im Mittel über alle Datensätze richtig.

### Varianz und Standardfehler eines Schätzers

<span class="anker" id="stufe-2-2"></span>

Erwartungstreue sagt nichts darüber, wie weit ein einzelner Schätzwert danebenliegen kann. Bild (b) in Abb. [4](#abb-4) ist erwartungstreu, aber die einzelnen Treffer sind schlecht. Das Maß für die Streuung ist die Varianz aus [Grundlagen 4, Abschnitt 7.4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-4), angewandt auf den Schätzer.

:::definition Definition 2.2 (Varianz und Standardfehler eines Schätzers)
<span class="anker" id="satz-2-2"></span>

Die Varianz $\operatorname{Var}(\hat\theta)$ eines Schätzers ist die Varianz seiner Stichprobenverteilung. Ihre Wurzel heißt __Standardfehler__:

<span class="anker" id="gl-2-2"></span>
$$\operatorname{SE}(\hat\theta)=\sqrt{\operatorname{Var}(\hat\theta)} . \tag{2.2}$$
:::

Für den Mittelwert ist das der Standardfehler $\sigma/\sqrt N$ aus [Grundlagen 4, Abschnitt 13.1](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-1); die Abkürzung SE kommt vom englischen *standard error*. Der Standardfehler hat dieselbe Einheit wie der Parameter und gibt an, wie weit ein Schätzwert typischerweise vom Erwartungswert des Schätzers entfernt liegt.

⁠**Rechenbeispiel:** Für den Anteil der Köpfe $N_1/N$ ist $N_1$ binomialverteilt, also eine Summe von $N$ unabhängigen Bernoulli-Größen mit der Varianz $\theta(1-\theta)$ nach [Grundlagen 4, Abschnitt 8.1](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-1). Mit [Grundlagen 4, Abschnitt 13.1](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-1), ist

$$\operatorname{Var}\Bigl(\frac{N_1}N\Bigr)=\frac{\theta(1-\theta)}N,\qquad \operatorname{SE}\Bigl(\frac{N_1}N\Bigr)=\sqrt{\frac{\theta(1-\theta)}N} .$$

Wäre bei der verbogenen Münze $\theta=0{,}7$, so wäre der Standardfehler bei $N=10$ gleich $\sqrt{0{,}21/10}\approx0{,}145$: Der Anteil der Köpfe aus zehn Würfen liegt typischerweise um $0{,}15$ neben $\theta$. Der erste Wurf $X_1$ dagegen hat die Varianz $\theta(1-\theta)=0{,}21$, gleichgültig, wie viele Würfe man macht.

⁠**Kurz gesagt:** Die Varianz eines Schätzers misst, wie stark er von Datensatz zu Datensatz schwankt; ihre Wurzel ist der Standardfehler.

:::hintergrund Den Standardfehler selbst schätzen
Der Standardfehler $\sqrt{\theta(1-\theta)/N}$ enthält den unbekannten Parameter. In der Praxis setzt man den Schätzwert ein und erhält einen geschätzten Standardfehler, bei sieben Köpfen in zehn Würfen also $\sqrt{0{,}7\cdot0{,}3/10}\approx0{,}145$. Mit dem zentralen Grenzwertsatz aus [Grundlagen 4, Abschnitt 13.4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-4), ist der Anteil der Köpfe bei großem $N$ näherungsweise normalverteilt. Deshalb liegt das Intervall „Schätzwert $\pm\,2$ Standardfehler“ in etwa $95\,\%$ der gedachten Wiederholungen so, dass es den wahren Parameter enthält. Man nennt es ein Konfidenzintervall. In der frequentistischen Sicht ist dabei das Intervall zufällig und der Parameter fest: Die $95\,\%$ beschreiben das Verfahren über viele Datensätze, nicht die Wahrscheinlichkeit, dass $\theta$ in einem bestimmten, schon berechneten Intervall liegt. Für zehn Würfe ist die Normalnäherung noch grob.
:::

### Der mittlere quadratische Fehler

<span class="anker" id="stufe-2-3"></span>

Verzerrung und Varianz beschreiben zwei Arten danebenzuliegen. Für den Vergleich zweier Schätzer möchte man eine einzige Zahl, die beide erfasst: den mittleren Abstand der Schätzwerte vom wahren Parameter, gemessen im Quadrat.

:::definition Definition 2.3 (Mittlerer quadratischer Fehler)
<span class="anker" id="satz-2-3"></span>

Der __mittlere quadratische Fehler__ eines Schätzers $\hat\theta$ für $\theta$ ist

<span class="anker" id="gl-2-3"></span>
$$\operatorname{MSE}(\hat\theta)=\mathbb{E}\bigl[(\hat\theta-\theta)^2\bigr] . \tag{2.3}$$
:::

Die Abkürzung MSE kommt vom englischen *mean squared error*. Der Erwartungswert ist wieder der über die Stichprobenverteilung bei festem $\theta$.

:::satz Satz 2.4 (Zerlegung des mittleren quadratischen Fehlers)
<span class="anker" id="satz-2-4"></span>

Für jeden Schätzer gilt

<span class="anker" id="gl-2-4"></span>
$$\operatorname{MSE}(\hat\theta)=\operatorname{Bias}(\hat\theta)^2+\operatorname{Var}(\hat\theta) . \tag{2.4}$$
:::

:::beweis Zerlegung
Es sei $Y=\hat\theta-\theta$. Nach der Verschiebungsformel aus [Grundlagen 4, Abschnitt 7.5](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-5), ist $\mathbb{E}[Y^2]=\operatorname{Var}(Y)+\mathbb{E}[Y]^2$. Links steht $\operatorname{MSE}(\hat\theta)$. Rechts ist $\mathbb{E}[Y]=\mathbb{E}[\hat\theta]-\theta=\operatorname{Bias}(\hat\theta)$, und $\operatorname{Var}(Y)=\operatorname{Var}(\hat\theta)$, denn das Abziehen der festen Zahl $\theta$ verschiebt die Verteilung nur und ändert nach [Grundlagen 4, Abschnitt 7.6](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-6), die Varianz nicht.
:::

Bei einem erwartungstreuen Schätzer ist der mittlere quadratische Fehler einfach die Varianz. Ein verzerrter Schätzer kann trotzdem den kleineren mittleren quadratischen Fehler haben, wenn er dafür weniger streut.

⁠**Rechenbeispiel:** Im Beispiel aus Unterabschnitt [1.4](schatzen-aus-einer-stichprobe.html#stufe-1-4) mit $\mu=2$ und $N=2$ hat $\bar X$ die Verzerrung $0$ und die Varianz $\tfrac13$, also $\operatorname{MSE}(\bar X)=\tfrac13\approx0{,}333$. Der geschrumpfte Schätzer $0{,}9\,\bar X$ hat den Erwartungswert $0{,}9\cdot2=1{,}8$, also die Verzerrung $-0{,}2$, und nach [Grundlagen 4, Abschnitt 7.6](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-6), die Varianz $0{,}81\cdot\tfrac13=0{,}27$. Sein mittlerer quadratischer Fehler ist $0{,}04+0{,}27=0{,}31$, kleiner als der von $\bar X$. Abb. [5](#abb-5) rechnet ihn zur Probe direkt über die Stichprobenverteilung aus. Der Vorteil hängt aber vom unbekannten $\mu$ ab: Läge $\mu$ bei $10$, mit derselben Streuung, so hätte $0{,}9\,\bar X$ die Verzerrung $-1$ und den mittleren quadratischen Fehler $1+0{,}27=1{,}27$, viel mehr als $\bar X$.

:::abbildung ml/k5rmse 5
Der mittlere quadratische Fehler des Schätzers $0{,}9\,\bar X$ für $\mu=2$ als Summe über die fünf Werte der Stichprobenverteilung aus Abb. [2](schatzen-aus-einer-stichprobe.html#abb-2) (b), und seine Zerlegung in die quadrierte Verzerrung und die Varianz.
:::

⁠**Kurz gesagt:** Der mittlere quadratische Fehler ist die quadrierte Verzerrung plus die Varianz; ein leicht verzerrter Schätzer, der weniger streut, kann insgesamt genauer sein.

:::hintergrund Warum sich Verzerrung und Streuung einfach addieren
Schreibt man den Fehler als Summe $\hat\theta-\theta=(\hat\theta-\mathbb{E}[\hat\theta])+(\mathbb{E}[\hat\theta]-\theta)$, so ist der erste Teil die zufällige Schwankung und der zweite die feste Verzerrung. Beim Quadrieren entsteht ein Mischglied $2\,(\hat\theta-\mathbb{E}[\hat\theta])\,(\mathbb{E}[\hat\theta]-\theta)$. Sein Erwartungswert ist null, weil die Schwankung um den eigenen Erwartungswert im Mittel verschwindet und die Verzerrung eine feste Zahl ist, die man vor den Erwartungswert ziehen darf. Das ist derselbe Grund, aus dem sich in [Grundlagen 1, Abschnitt 4.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-3), die Abweichungen vom Mittelwert zu null summieren. In der Sprache von [Grundlagen 4, Abschnitt 10.4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/kovarianz-und-korrelation.html#stufe-10-4), wo die Kovarianz wie ein Skalarprodukt rechnet, steht die Schwankung senkrecht auf jeder festen Zahl, und das Quadrat der Summe zerfällt nach Pythagoras in zwei Quadrate. Weil beide nie negativ sind, kann man den Fehler nur verkleinern, indem man an der Verzerrung oder an der Streuung spart, und oft erkauft man das eine mit dem anderen.
:::

### Konsistenz

<span class="anker" id="stufe-2-4"></span>

Mehr Daten sollten eine Schätzung besser machen. Beim Mittelwert ist das so, beim ersten Wurf $X_1$ nicht: Er wirft alle weiteren Werte weg. Die folgende Eigenschaft hält fest, dass ein Schätzer mit wachsender Datenmenge beliebig genau wird. Weil der Schätzer jetzt von der Zahl $N$ der Werte abhängt, schreibt man $\hat\theta_N$.

:::definition Definition 2.5 (Konsistenz)
<span class="anker" id="satz-2-5"></span>

Ein Schätzer $\hat\theta_N$ heißt __konsistent__, wenn für jedes $\varepsilon>0$ gilt

<span class="anker" id="gl-2-5"></span>
$$P\bigl(|\hat\theta_N-\theta|\ge\varepsilon\bigr)\longrightarrow0\qquad\text{für }N\to\infty . \tag{2.5}$$
:::

Wie klein man die Toleranz $\varepsilon$ auch wählt, mit genug Daten liegt der Schätzwert mit einer Wahrscheinlichkeit beliebig nahe bei $1$ näher als $\varepsilon$ am wahren Parameter. Das ist dieselbe Form wie das Gesetz der großen Zahlen aus [Grundlagen 4, Abschnitt 13.3](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-3).

:::satz Satz 2.6 (Konsistenz aus dem mittleren quadratischen Fehler)
<span class="anker" id="satz-2-6"></span>

Geht $\operatorname{MSE}(\hat\theta_N)$ für $N\to\infty$ gegen null, also Verzerrung und Varianz zugleich, so ist $\hat\theta_N$ konsistent. Genauer gilt für jedes $\varepsilon>0$

<span class="anker" id="gl-2-6"></span>
$$P\bigl(|\hat\theta_N-\theta|\ge\varepsilon\bigr)\le\frac{\operatorname{MSE}(\hat\theta_N)}{\varepsilon^2} . \tag{2.6}$$
:::

:::beweis Konsistenz
Wie beim Beweis der Tschebyschow-Ungleichung in [Grundlagen 4, Abschnitt 13.2](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-2): Es sei $A$ das Ereignis $|\hat\theta_N-\theta|\ge\varepsilon$. Dann ist $(\hat\theta_N-\theta)^2\ge\varepsilon^2\,\mathbb 1_A$ für jedes Ergebnis, und der Erwartungswert beider Seiten ergibt $\operatorname{MSE}(\hat\theta_N)\ge\varepsilon^2\,P(A)$.
:::

⁠**Rechenbeispiel:** Der Mittelwert hat $\operatorname{MSE}(\bar X_N)=\sigma^2/N$, und das geht gegen null: $\bar X_N$ ist konsistent. Für die Münze mit $\theta=0{,}7$ und $N=100$ Würfen sagt [(2.6)](#gl-2-6), dass der Anteil der Köpfe höchstens mit der Wahrscheinlichkeit $0{,}0021/0{,}01=0{,}21$ um $0{,}1$ oder mehr danebenliegt. Der Schätzer $X_1$ dagegen ist zwar erwartungstreu, aber nicht konsistent. Im Beispiel mit den Werten $1$, $2$, $3$ ist $P(|X_1-2|\ge1)=\tfrac23$, gleichgültig, wie groß $N$ ist. Umgekehrt ist der Schätzer $\bar X_N+1/N$ verzerrt, denn seine Verzerrung ist $1/N$, aber konsistent, denn sein mittlerer quadratischer Fehler $1/N^2+\sigma^2/N$ geht gegen null.

⁠**Kurz gesagt:** Ein konsistenter Schätzer trifft mit genug Daten beliebig genau; Erwartungstreue und Konsistenz sind verschiedene Eigenschaften, und keine folgt aus der anderen.

:::aufgabe Aufgabe 3 ★ Zwei Schätzer für eine Münze
<span class="anker" id="aufg-3"></span>

Für $N=10$ Würfe vergleicht man $\hat\theta_1=N_1/N$ und $\hat\theta_2=(N_1+1)/(N+2)$.

<ol class="al">

<li>

Zeige $\operatorname{Bias}(\hat\theta_2)=\dfrac{1-2\theta}{N+2}$ und $\operatorname{Var}(\hat\theta_2)=\dfrac{N\theta(1-\theta)}{(N+2)^2}$.

</li>

<li>

Berechne die mittleren quadratischen Fehler beider Schätzer für $\theta=0{,}5$, $\theta=0{,}7$ und $\theta=0{,}95$. Welcher ist jeweils besser?

</li>

<li>

Ist $\hat\theta_2$ konsistent?

</li>

</ol>

:::loesung
(a) Mit $\mathbb{E}[N_1]=N\theta$ ist $\mathbb{E}[\hat\theta_2]=\frac{N\theta+1}{N+2}$, also $\operatorname{Bias}(\hat\theta_2)=\frac{N\theta+1-(N+2)\theta}{N+2}=\frac{1-2\theta}{N+2}$. Mit $\operatorname{Var}(N_1)=N\theta(1-\theta)$ und [Grundlagen 4, Abschnitt 7.6](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-6), ist $\operatorname{Var}(\hat\theta_2)=\frac{N\theta(1-\theta)}{(N+2)^2}$.

(b) $\hat\theta_1$ ist erwartungstreu, also $\operatorname{MSE}(\hat\theta_1)=\theta(1-\theta)/10$. Für $\hat\theta_2$ addiert man das Quadrat der Verzerrung zur Varianz:

<ul>

<li>

$\theta=0{,}5$: $\operatorname{MSE}(\hat\theta_1)=0{,}025$; $\hat\theta_2$ hat die Verzerrung $0$ und die Varianz $2{,}5/144\approx0{,}0174$. $\hat\theta_2$ ist besser.

</li>

<li>

$\theta=0{,}7$: $\operatorname{MSE}(\hat\theta_1)=0{,}021$; $\hat\theta_2$ hat die Verzerrung $-0{,}4/12\approx-0{,}0333$ und die Varianz $2{,}1/144\approx0{,}0146$, zusammen $0{,}00111+0{,}01458\approx0{,}0157$. $\hat\theta_2$ ist besser.

</li>

<li>

$\theta=0{,}95$: $\operatorname{MSE}(\hat\theta_1)=0{,}00475$; $\hat\theta_2$ hat die Verzerrung $-0{,}9/12=-0{,}075$ und die Varianz $0{,}475/144\approx0{,}0033$, zusammen $0{,}005625+0{,}0033\approx0{,}0089$. Hier ist $\hat\theta_1$ besser.

</li>

</ul>

$\hat\theta_2$ zieht jeden Schätzwert zur Mitte $\tfrac12$ hin. Das senkt die Varianz und kostet in der Nähe der Mitte wenig Verzerrung. Am Rand wird die Verzerrung groß, und dort verliert er.

(c) Ja. Die Verzerrung $(1-2\theta)/(N+2)$ und die Varianz $N\theta(1-\theta)/(N+2)^2\le\theta(1-\theta)/N$ gehen beide gegen null, also auch der mittlere quadratische Fehler, und nach dem Satz in Unterabschnitt [2.4](#stufe-2-4) ist $\hat\theta_2$ konsistent.
:::
:::

:::aufgabe Aufgabe 4 ★★ Den größten Wert schätzen
<span class="anker" id="aufg-4"></span>

Im Beispiel aus Unterabschnitt [1.4](schatzen-aus-einer-stichprobe.html#stufe-1-4) (Werte $1$, $2$, $3$, $N=2$) soll der größte mögliche Wert $3$ geschätzt werden, und zwar mit dem größten beobachteten Wert $M=\max(X_1,X_2)$.

<ol class="al">

<li>

Bestimme die Stichprobenverteilung von $M$ mit Tabelle [1](schatzen-aus-einer-stichprobe.html#tab-1).

</li>

<li>

Berechne Verzerrung, Varianz und mittleren quadratischen Fehler. Warum muss die Verzerrung negativ sein?

</li>

</ol>

:::loesung
(a) Aus Tabelle [1](schatzen-aus-einer-stichprobe.html#tab-1): $M=1$ nur für $(1,1)$, $M=2$ für $(1,2)$, $(2,1)$, $(2,2)$, $M=3$ für die übrigen fünf. Also $P(M=1)=\tfrac19$, $P(M=2)=\tfrac39$, $P(M=3)=\tfrac59$.

(b) $\mathbb{E}[M]=\tfrac{1+6+15}9=\tfrac{22}9\approx2{,}444$, die Verzerrung ist $\tfrac{22}9-3=-\tfrac59\approx-0{,}556$. Mit $\mathbb{E}[M^2]=\tfrac{1+12+45}9=\tfrac{58}9$ ist $\operatorname{Var}(M)=\tfrac{58}9-\tfrac{484}{81}=\tfrac{38}{81}\approx0{,}469$, und $\operatorname{MSE}(M)=\tfrac{25}{81}+\tfrac{38}{81}=\tfrac{63}{81}=\tfrac79\approx0{,}778$. Zur Probe direkt: $\mathbb{E}[(M-3)^2]=\tfrac{4\cdot1+1\cdot3+0\cdot5}9=\tfrac79$. Die Verzerrung muss negativ sein, weil der größte beobachtete Wert nie größer als der größte mögliche Wert ist, aber manchmal kleiner; im Mittel liegt er also darunter.
:::
:::

:::aufgabe Aufgabe 5 ★★ Zwei Messgeräte
<span class="anker" id="aufg-5"></span>

Eine Spannung $\mu$ wird mit zwei Geräten je einmal gemessen. Die Messwerte $X_A$ und $X_B$ sind unabhängig, erwartungstreu und haben die Varianzen $\sigma_A^2=4\,\mathrm{mV}^2$ und $\sigma_B^2=1\,\mathrm{mV}^2$.

<ol class="al">

<li>

Zeige, dass $\hat\mu=w\,X_A+(1-w)\,X_B$ für jede Zahl $w$ erwartungstreu ist.

</li>

<li>

Bestimme $w$ so, dass die Varianz von $\hat\mu$ am kleinsten ist. Tipp: Die Varianz ist eine nach oben geöffnete Parabel in $w$; ihr Scheitel liegt dort, wo die Ableitung null ist.

</li>

<li>

Vergleiche den Standardfehler mit dem von $X_B$ allein und mit dem des einfachen Mittelwerts $w=\tfrac12$.

</li>

</ol>

:::loesung
(a) Nach der Linearität ist $\mathbb{E}[\hat\mu]=w\mu+(1-w)\mu=\mu$, für jedes $w$.

(b) Wegen der Unabhängigkeit ist $\operatorname{Var}(\hat\mu)=w^2\cdot4+(1-w)^2\cdot1$ in $\mathrm{mV}^2$. Die Ableitung nach $w$ ist $8w-2(1-w)=10w-2$; sie ist null bei $w=0{,}2$. Das ungenauere Gerät A bekommt also nur das Gewicht $0{,}2$. Allgemein ist $w=\sigma_B^2/(\sigma_A^2+\sigma_B^2)$: Jedes Gerät wird mit dem Kehrwert seiner Varianz gewichtet.

(c) Bei $w=0{,}2$ ist $\operatorname{Var}(\hat\mu)=0{,}04\cdot4+0{,}64=0{,}8\,\mathrm{mV}^2$, der Standardfehler also $0{,}894\,\mathrm{mV}$. Gerät B allein hat $1\,\mathrm{mV}$, der einfache Mittelwert hat $\operatorname{Var}=0{,}25\cdot4+0{,}25=1{,}25\,\mathrm{mV}^2$, also $1{,}118\,\mathrm{mV}$. Der einfache Mittelwert ist schlechter als Gerät B allein; erst die richtige Gewichtung macht die zweite Messung nützlich.
:::
:::

:::aufgabe Aufgabe 6 ★★★ Wie viele Würfe?
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Zeige mit [(2.6)](#gl-2-6), dass für den Anteil der Köpfe bei jedem $\theta$ gilt: $P(|N_1/N-\theta|\ge\varepsilon)\le1/(4N\varepsilon^2)$. Benutze, dass $\theta(1-\theta)$ höchstens $\tfrac14$ ist.

</li>

<li>

Wie viele Würfe garantieren nach dieser Schranke, dass der Anteil mit mindestens $95\,\%$ Wahrscheinlichkeit um weniger als $0{,}05$ danebenliegt?

</li>

<li>

Wie viele Würfe genügen nach dem zentralen Grenzwertsatz im ungünstigsten Fall $\theta=\tfrac12$? Woher kommt der große Unterschied?

</li>

</ol>

:::loesung
(a) Der mittlere quadratische Fehler ist $\theta(1-\theta)/N\le\tfrac1{4N}$, und [(2.6)](#gl-2-6) ergibt $P(|N_1/N-\theta|\ge\varepsilon)\le\frac1{4N\varepsilon^2}$.

(b) Verlangt ist $\frac1{4N\cdot0{,}05^2}\le0{,}05$, also $N\ge\frac1{4\cdot0{,}0025\cdot0{,}05}=2000$.

(c) Nach dem zentralen Grenzwertsatz ist $N_1/N$ näherungsweise normalverteilt mit dem Standardfehler $\sqrt{0{,}25/N}$. Die Abweichung ist mit $95\,\%$ Wahrscheinlichkeit kleiner als $1{,}96$ Standardfehler, verlangt ist also $1{,}96\cdot0{,}5/\sqrt N\le0{,}05$, das heißt $\sqrt N\ge19{,}6$ und $N\ge385$. Die Schranke aus (a) gilt für jede Verteilung und nutzt nur die Varianz; sie ist deshalb grob, wie die Tschebyschow-Ungleichung in [Grundlagen 4, Abschnitt 13.2](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-2).
:::
:::
