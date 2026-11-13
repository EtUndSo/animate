---
title: Stufe 4: Der Grenzwert
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
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

⁠**So liest man das:** Nach der Abstandsregel bedeutet $|a_n-a|<\varepsilon$, dass $a_n$ im offenen Intervall $(a-\varepsilon,a+\varepsilon)$ liegt, dem Epsilon-Schlauch um $a$. Er ist $2\varepsilon$ breit. Bis auf endlich viele Glieder liegen alle darin. Direkte Nachweise von [(4.1)](#gl-4-1) heißen __Epsilontik__. Dieselbe Technik trägt später Cauchy-Folgen (Stufe [8](cauchy-folgen-und-die-axiome.html#stufe-8)) und die Stetigkeit ([Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)). Nullfolgen sind der Sonderfall $a=0$.

:::abbildung hm1/k4schlauch 5
Der Epsilon-Schlauch um $a=2$ mit $\varepsilon=0{,}5$ und den Gliedern der Pendelfolge. Das Glied $a_6=2{,}5$ liegt genau auf dem Rand und damit nicht im offenen Intervall, $a_7=1{,}571$ liegt drin. Ab $N_0=6$ bleiben alle Glieder im Schlauch, die grauen bis $n=6$ zählen nicht.
:::

::::beispiel
Für die Pendelfolge ist $a_n-2=d_n$, und das ist nach Stufe [2](das-epsilon-spiel.html#stufe-2) eine Nullfolge. Also gilt $\lim a_n=2$, mit denselben Antworten wie im Spiel. Für die Summenfolge ist $2-s_n=(\frac12)^n$, eine geometrische Folge, also gilt $\lim s_n=2$.
::::

⁠**Grenzfall:** Die konstante Folge $a_n=c$ hat den Grenzwert $c$ mit $N_0=1$ für jede Toleranz.

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

::::formelsammlung
**Konvergent mit Grenzwert $a$**

$$\forall\,\varepsilon>0\quad\exists\,N_0\in\mathbb{N},\quad\text{so dass}\quad|a_n-a|<\varepsilon\quad\forall\,n>N_0$$

Für $a\in\mathbb{R}$; gleichbedeutend: $\{a_n-a\}$ ist eine Nullfolge. Geschrieben $\lim_{n\to\infty}a_n=a$ oder $a_n\to a$ für $n\to\infty$.

**Epsilon-Schlauch um $a$**

$$a-\varepsilon<a_n<a+\varepsilon$$

Das offene Intervall $(a-\varepsilon,a+\varepsilon)$, $2\varepsilon$ breit; bis auf endlich viele liegen alle Glieder darin.

**Trick der Epsilontik**

$$|a_n-a|\le y_n$$

Mit einer bekannten positiven Nullfolge $y_n$, etwa $\frac Cn$ oder $\frac C{\sqrt n}$; nach $n$ aufgelöst wird nur $y_n<\varepsilon$.

**Konvergente Folgen sind beschränkt**

$$|a_n|\le M+|a|$$

Der Grenzwert ist eindeutig bestimmt, und $\{a_n\}$ ist beschränkt ($M$ beschränkt die Nullfolge $\{a_n-a\}$). Die Umkehrung gilt nicht: $(-1)^n$.
::::

::::lernkarten
:::karte begriff konvergent und Grenzwert
Wann heißt eine Folge $\{a_n\}$ konvergent mit Grenzwert $a\in\mathbb{R}$, formuliert mit dem Epsilon-Kriterium?
---
Wenn $\{a_n-a\}$ eine Nullfolge ist, also $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}$, so dass $|a_n-a|<\varepsilon$ für alle $n>N_0$. Man schreibt $\lim_{n\to\infty}a_n=a$ oder $a_n\to a$ für $n\to\infty$.
--- falsch
Wenn $\exists\,N_0\in\mathbb{N}\ \forall\,\varepsilon>0$ mit $|a_n-a|<\varepsilon$ für alle $n>N_0$. Ein einziger Index gilt also für jede Toleranz zugleich. Man schreibt $\lim_{n\to\infty}a_n=a$ oder $a_n\to a$.
--- falsch
Wenn $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}$ mit $|a_n|-|a|<\varepsilon$ für alle $n>N_0$; es genügt also, dass die Beträge der Glieder höchstens um $\varepsilon$ über $|a|$ liegen. Man schreibt $\lim_{n\to\infty}a_n=a$.
--- falsch
Wenn $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}$ mit $|a_{n+1}-a_n|<\varepsilon$ für alle $n>N_0$; benachbarte Glieder rücken also beliebig eng zusammen, und $a$ ist der Wert, auf den sie dabei zulaufen.
:::
:::karte zusammenhang Konvergenz
Warum lässt sich die Konvergenz einer Folge gegen $a$ auf das Spiel mit Nullfolgen zurückführen?
---
Weil für die Annäherung an $a$ nur der Abstand $|a_n-a|$ zählt: Zieht man von jedem Glied $a$ ab, landet man beim Nullfolgen-Spiel. Eine konvergente Folge ist eine um $a$ verschobene Nullfolge, ihr Schlauch liegt um $a$.
--- falsch
Weil jede konvergente Folge ab einem Index nur noch Glieder gleich $a$ hat: Zieht man $a$ ab, bleibt ab dort die konstante Folge 0, also eine Nullfolge. Die Glieder davor dürfen beliebig sein, sie zählen nicht.
--- falsch
Weil man jede Folge durch ihren Grenzwert teilen kann: $\{a_n/a\}$ strebt gegen 1, und $\{a_n/a-1\}$ ist dann eine Nullfolge. Das gelingt für jedes $a\in\mathbb{R}$, auch für $a=0$, weil man dort mit 1 rechnet.
--- falsch
Weil Konvergenz gegen $a$ dasselbe ist wie $|a_n|\to|a|$: Man vergleicht nur die Beträge, und $\{|a_n|-|a|\}$ ist genau dann eine Nullfolge, wenn die Folge gegen $a$ konvergiert, gleich welches Vorzeichen $a$ hat.
:::
:::karte zusammenhang Schlauch um den Grenzwert
In welchem Intervall liegen die Glieder einer gegen $a$ konvergenten Folge ab $N_0$, und wie breit ist dieser Epsilon-Schlauch?
---
Nach der Abstandsregel heißt $|a_n-a|<\varepsilon$, dass $a_n$ im offenen Intervall $(a-\varepsilon,a+\varepsilon)$ liegt; der Schlauch um $a$ ist $2\varepsilon$ breit. Bis auf endlich viele liegen alle Glieder darin; ein Glied genau auf dem Rand liegt nicht darin.
--- falsch
Im abgeschlossenen Intervall $[a-\varepsilon,a+\varepsilon]$, das $\varepsilon$ breit ist; ein Glied genau auf dem Rand liegt also mit darin. Bis auf endlich viele Glieder liegen alle in diesem Schlauch, auch die mit kleinem Index.
--- falsch
Im offenen Intervall $(a,a+\varepsilon)$ oberhalb von $a$, das $\varepsilon$ breit ist; Glieder unterhalb von $a$ zählen nicht, weil sich eine konvergente Folge ihrem Grenzwert immer von oben nähert, wie die Pendelfolge.
--- falsch
Im offenen Intervall $(a-\varepsilon,a+\varepsilon)$, das $2\varepsilon$ breit ist; darin liegen ab $N_0$ unendlich viele Glieder, die übrigen dürfen sich bis ans Ende der Folge immer wieder außerhalb aufhalten.
:::
:::karte begriff Epsilontik
Was nennt man Epsilontik, und welchen Wert muss man dafür schon vorher kennen?
---
Direkte Nachweise der Konvergenz über die Definition: zu jedem $\varepsilon>0$ ein $N_0$ angeben, so dass $|a_n-a|<\varepsilon$ für alle $n>N_0$. Dafür muss der Grenzwert $a$ vorher bekannt sein.
--- falsch
Das Abschätzen von Folgengliedern mit Taschenrechner und Tabelle, bis eines kleiner als $\varepsilon$ ist. Den Grenzwert muss man dafür nicht kennen, er ergibt sich am Ende aus der Tabelle.
--- falsch
Direkte Nachweise der Konvergenz über die Definition, aber nur für Nullfolgen: Für Folgen mit Grenzwert $a\ne0$ braucht man andere Methoden, weil dort kein $\varepsilon$ vorkommt.
--- falsch
Das Rechnen mit unendlich kleinen Zahlen $\varepsilon$, die kleiner als jede positive Zahl und trotzdem nicht null sind. Den Grenzwert erhält man, indem man am Ende $\varepsilon=0$ setzt.
:::
:::karte zusammenhang Trick der Epsilontik
Was tut man in der Epsilontik, wenn sich $|a_n-a|<\varepsilon$ nicht bequem nach $n$ auflösen lässt, etwa bei $f_n=\frac{2n^2+3}{n^2+n}$?
---
Man schätzt den Abstand durch eine bekannte positive Nullfolge ab, $|a_n-a|\le y_n$, und löst nur $y_n<\varepsilon$ nach $n$ auf. Bei $f_n$ ist $|f_n-2|=\frac{2n-3}{n^2+n}\le\frac2n$ für $n\ge2$, also gewinnt $N_0:=\lfloor2/\varepsilon\rfloor+1$.
--- falsch
Man schätzt den Abstand nach unten ab, $|a_n-a|\ge y_n$ mit einer Nullfolge $y_n$, und löst $y_n<\varepsilon$ nach $n$ auf. Bei $f_n$ ist $|f_n-2|\ge\frac1n$ für alle $n$, also gewinnt $N_0:=\lfloor1/\varepsilon\rfloor+1$.
--- falsch
Man setzt einige große $n$ ein und liest ab, ab wann $|a_n-a|<\varepsilon$ gilt. Bei $f_n$ ist $|f_{10}-2|=0{,}1545$, also gewinnt für $\varepsilon=0{,}2$ der Index $N_0=10$, und damit ist die Konvergenz für jedes $\varepsilon$ gezeigt.
--- falsch
Man ersetzt $a_n$ durch den Grenzwert und rechnet mit $a$ weiter, weil beide für große $n$ gleich sind. Bei $f_n$ ist dann $|f_n-2|=0$ für große $n$, und jedes $N_0$ gewinnt, ohne dass man nach $n$ auflösen muss.
:::
:::karte formel Eigenschaften konvergenter Folgen
Welche zwei Eigenschaften hat jede konvergente Folge $\{a_n\}$ mit Grenzwert $a$, und gilt die zweite auch umgekehrt?
---
Der Grenzwert ist eindeutig bestimmt, und $\{a_n\}$ ist beschränkt. Umgekehrt gilt das nicht: $(-1)^n$ ist beschränkt und konvergiert nicht.
--- falsch
Der Grenzwert ist eindeutig bestimmt, und $\{a_n\}$ ist beschränkt. Umgekehrt gilt das auch: Jede beschränkte Folge konvergiert, weil sie den Streifen nicht verlassen kann.
--- falsch
Der Grenzwert ist eindeutig bestimmt, und $\{a_n\}$ ist monoton. Umgekehrt gilt das nicht: $(-1)^n$ wechselt die Richtung, ist beschränkt und konvergiert trotzdem nicht.
--- falsch
Eine Folge kann mehrere Grenzwerte haben, etwa $-1$ und $1$ bei $(-1)^n$, und $\{a_n\}$ ist beschränkt. Umgekehrt hat jede beschränkte Folge mindestens einen Grenzwert.
:::
:::karte herleitung Eindeutigkeit und Beschränktheit
Wie zeigt man, dass eine konvergente Folge $\{a_n\}$ nur einen Grenzwert hat und beschränkt ist?
---
Gelte $a_n\to a$ und $a_n\to\tilde a$. Dann ist auch $(a_n-a)-(a_n-\tilde a)=\tilde a-a$ eine Nullfolge, weil die Differenz zweier Nullfolgen eine Nullfolge ist.
---
Diese Differenz hängt nicht von $n$ ab. Eine konstante Nullfolge ist 0, weil sie sonst an $\varepsilon=|\tilde a-a|$ scheitert; also ist $\tilde a=a$.
---
Für die Schranke schreibt man $|a_n|=|a_n-a+a|\le|a_n-a|+|a|$, weil der Betrag einer Summe nach der Dreiecksungleichung höchstens die Summe der Beträge ist.
---
Die Nullfolge $\{a_n-a\}$ ist durch ein $M$ beschränkt, weil jede Nullfolge beschränkt ist; also ist $|a_n|\le M+|a|$ für alle $n$.
:::
:::karte zusammenhang beschränkt, aber nicht konvergent
Folgt aus der Beschränktheit einer Folge ihre Konvergenz, und was lässt sich über unbeschränkte Folgen sagen?
---
Nein: $(-1)^n$ ist beschränkt und konvergiert nicht. Umgekehrt kann eine unbeschränkte Folge nicht konvergieren, weil jede konvergente Folge beschränkt ist.
--- falsch
Ja: Eine beschränkte Folge liegt in einem Streifen und muss sich darin irgendwo häufen; dieser Wert ist ihr Grenzwert. Unbeschränkte Folgen konvergieren nie.
--- falsch
Nein: $(-1)^n$ ist beschränkt und konvergiert nicht. Unbeschränkte Folgen können dagegen konvergieren, wenn sie nur nach oben unbeschränkt sind und nach unten eine Schranke haben.
--- falsch
Ja, sofern die Folge zusätzlich nur endlich viele verschiedene Werte annimmt. Unbeschränkte Folgen konvergieren gegen $\infty$ oder $-\infty$ und haben damit ebenfalls einen Grenzwert.
:::
:::karte zusammenhang Anfang der Folge
Ändert sich der Grenzwert einer Folge, wenn man ihre ersten tausend Glieder ändert?
---
Nein. Die Bedingung betrifft nur Glieder hinter $N_0$, und $N_0$ darf man über 1000 legen. Der Grenzwert ist eine Eigenschaft des Endes der Folge; Aussagen über einzelne Glieder oder über die ersten paar sagen nichts über ihn.
--- falsch
Ja, im Allgemeinen schon: Der Grenzwert ist ein Mittelwert über alle Glieder, und tausend geänderte Glieder verschieben diesen Mittelwert, wenn auch für große $n$ nur ein wenig und nie ganz unmerklich.
--- falsch
Nur wenn die Folge monoton ist: Dann bestimmen die ersten Glieder die Richtung, und eine Änderung am Anfang kann eine wachsende Folge in eine fallende verwandeln, die dann einen anderen Grenzwert hat.
--- falsch
Ja, denn der Index $N_0$ muss für jede Toleranz der kleinstmögliche sein; ändert man die ersten tausend Glieder, ändern sich diese kleinsten Indizes, und mit ihnen ändert sich auch der Grenzwert der Folge.
:::
:::karte zusammenhang Pendelfolge und Summenfolge
Warum konvergieren die Pendelfolge $a_n=2+d_n$ und die Summenfolge $s_n$ beide gegen 2?
---
Bei der Pendelfolge ist $a_n-2=d_n$, und $d_n$ ist eine Nullfolge; also gilt $\lim a_n=2$ mit denselben Indizes wie im Spiel. Bei der Summenfolge ist $2-s_n=(\frac12)^n$ eine geometrische Folge mit $|q|<1$, also gilt $\lim s_n=2$.
--- falsch
Weil beide beschränkt sind und die 2 jeweils ungefähr in der Mitte ihres Streifens liegt: Eine beschränkte Folge konvergiert gegen die Mitte zwischen ihrer kleinsten oberen und ihrer größten unteren Schranke.
--- falsch
Bei der Pendelfolge ist $a_n-2=d_n$ eine Nullfolge, also gilt $\lim a_n=2$. Die Summenfolge konvergiert dagegen nicht, weil sie streng monoton wächst und eine wachsende Folge nie zur Ruhe kommt.
--- falsch
Weil beide Folgen den Wert 2 nach endlich vielen Schritten exakt erreichen und danach dort bleiben; der Grenzwert ist der Wert, bei dem eine Folge zur Ruhe kommt, und das geschieht hier bei 2.
:::
::::
