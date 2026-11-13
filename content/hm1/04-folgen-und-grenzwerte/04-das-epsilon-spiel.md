---
title: Stufe 2: Das Epsilon-Spiel
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240400
summary: „Die Glieder kommen der Null immer näher“ taugt nicht als Definition, denn die Glieder von 1/n kommen auch der Zahl -1 immer näher.
tags: Nullfolge, Epsilon-Schlauch, Limes
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
„Die Glieder kommen der Null immer näher“ taugt nicht als Definition, denn die Glieder von $1/n$ kommen auch der Zahl $-1$ immer näher. Diese Stufe macht aus „beliebig nah“ eine prüfbare Aussage.
:::

**Die Idee.** Das Kriterium ist ein Spiel. *Du* gibst mir eine Toleranz $\varepsilon>0$ vor, so klein du willst. *Ich* nenne dir einen Index $N_0$. Ich gewinne die Runde, wenn *alle* Glieder hinter Platz $N_0$ innerhalb der Toleranz liegen. Eine Folge heißt Nullfolge, wenn ich jede Runde gewinnen kann, egal welche Toleranz du wählst. Die endlich vielen Glieder bis $N_0$ dürfen beliebig weit draußen liegen, mein Index schneidet sie ab.

**An Zahlen.** Gespielt wird mit der Abweichung $d_n=(-1)^n\,3/n$. Für den Abstand zur 0 zählt das Vorzeichen nicht: $|d_n|=3/n$. Die Gewinnbedingung $3/n<\varepsilon$ ist gleichbedeutend mit $n>3/\varepsilon$.

| Runde | Toleranz $\varepsilon$ | Bedingung | Antwort $N_0$ | Glied $N_0$, genau auf dem Rand | erstes Glied drin |
|---|---|---|---|---|---|
| 1 | 0,5 | $n>6$ | 6 | $\vert d_6\vert =0{,}5$ | $\vert d_7\vert =0{,}43$ |
| 2 | 0,25 | $n>12$ | 12 | $\vert d_{12}\vert =0{,}25$ | $\vert d_{13}\vert =0{,}23$ |
| 3 | 0,1 | $n>30$ | 30 | $\vert d_{30}\vert =0{,}1$ | $\vert d_{31}\vert =0{,}097$ |
| 4 | 0,01 | $n>300$ | 300 | $\vert d_{300}\vert =0{,}01$ | $\vert d_{301}\vert =0{,}00997$ |

Hinter dem Glied in der letzten Spalte liegen alle weiteren noch näher an 0, weil $3/n$ fällt. Eine zehnmal kleinere Toleranz verlangt einen zehnmal größeren Index. Weil die natürlichen Zahlen nicht nach oben beschränkt sind, gibt es für jedes $\varepsilon$ eine Zahl oberhalb von $3/\varepsilon$. Ich kann also immer antworten. Eine einzelne Runde beweist noch nichts. Bewiesen ist die Sache erst durch eine Regel für alle Runden: Nimm einen Index oberhalb von $3/\varepsilon$.

:::abbildung hm1/k4spiel 2
Zwei Runden des Spiels mit $d_n$. Der blaue Streifen ist der Epsilon-Schlauch, er reicht von $-\varepsilon$ bis $\varepsilon$. Graue Glieder haben einen Index $n\le N_0$ und dürfen draußen liegen, die blauen liegen alle drin. Halbiert sich $\varepsilon$, verdoppelt sich $N_0$.
:::

:::definition Definition 2.1 (Nullfolge, Epsilon-Kriterium)
<span class="anker" id="satz-2-1"></span>

Eine Folge $\{a_n\}_{n\in\mathbb{N}}$ reeller Zahlen heißt __Nullfolge__, falls

<span class="anker" id="gl-2-1"></span>
$$\forall\,\varepsilon>0\quad\exists\,N_0\in\mathbb{N}\quad\text{so dass}\quad\bigl(\,|a_n|<\varepsilon\quad\forall\,n>N_0\bigr). \tag{2.1}$$

Man schreibt dann $a_n\to0$ für $n\to\infty$ oder $\lim_{n\to\infty}a_n=0$ und sagt: $a_n$ konvergiert gegen null für $n$ gegen unendlich.
:::

⁠**So liest man das:** Von links nach rechts steht das Spiel: $\forall\,\varepsilon>0$ ist deine Vorgabe, $\exists\,N_0$ meine Antwort, die Klammer die Gewinnbedingung. Die Reihenfolge entscheidet. Erst steht $\varepsilon$ fest, dann wird $N_0$ gewählt, also darf $N_0$ von $\varepsilon$ abhängen: $N_0=N_0(\varepsilon)$. Nach der Abstandsregel heißt $|a_n|<\varepsilon$ dasselbe wie $-\varepsilon<a_n<\varepsilon$. Dieser Streifen heißt __Epsilon-Schlauch__. In jedem noch so engen Schlauch um 0 liegen alle Glieder bis auf endlich viele. Das Zeichen $\infty$ ist keine Zahl, „$n\to\infty$“ steht für den Zusatz „für alle $n$ oberhalb eines passenden Index“. Das Wort __Limes__ (lateinisch für Grenze) gibt $\lim$ den Namen.

**Die Gauß-Klammer.** Mein $N_0$ muss eine natürliche Zahl sein, $3/\varepsilon$ ist meist keine. Das Werkzeug zum Runden heißt so:

:::definition Definition 2.2 (Gauß-Klammer)
<span class="anker" id="satz-2-2"></span>

Für $x\in\mathbb{R}$ setzt man

$$\begin{aligned} \lfloor x\rfloor&:=\max\{z\in\mathbb{Z}:\ z\le x\}\in\mathbb{Z}&&\text{(abrunden)},\\ \lceil x\rceil&:=\min\{z\in\mathbb{Z}:\ x\le z\}\in\mathbb{Z}&&\text{(aufrunden)}. \end{aligned}$$

Für alle $x\in\mathbb{R}$ gilt

<span class="anker" id="gl-2-2"></span>
$$\lfloor x\rfloor\le x\le\lceil x\rceil,\quad0\le\lceil x\rceil-\lfloor x\rfloor\le1,\quad0\le\lceil x\rceil-x<1,\quad0\le x-\lfloor x\rfloor<1 \tag{2.2}$$

sowie $\lfloor x\rfloor=x=\lceil x\rceil\iff x\in\mathbb{Z}$.
:::

⁠**So liest man das:** $\lfloor3{,}7\rfloor=3$, $\lceil3{,}7\rceil=4$, $\lfloor4\rfloor=\lceil4\rceil=4$. Abrunden geht auf der Zahlengeraden immer nach links, deshalb ist $\lfloor-1{,}2\rfloor=-2$ und $\lceil-1{,}2\rceil=-1$. Die wichtigste Folgerung für dieses Kapitel ist $\lfloor x\rfloor+1>x$: Das gibt zu jedem $x\ge0$ eine natürliche Zahl oberhalb von $x$.

:::beweis Die Abweichung $d_n$ ist eine Nullfolge
Sei $\varepsilon>0$ beliebig vorgegeben. Wähle $N_0:=\lfloor3/\varepsilon\rfloor+1\in\mathbb{N}$. Nach [(2.2)](#gl-2-2) ist $N_0>3/\varepsilon$. Für jedes $n>N_0$ folgt $n>3/\varepsilon$ und daraus, weil $n$ und $\varepsilon$ positiv sind, $3/n<\varepsilon$. Also ist $|d_n|<\varepsilon$ für alle $n>N_0$.
:::

**Wie man $N_0$ findet.** Der Beweis nennt die Antwort sofort, gefunden wird sie rückwärts: Man startet bei $|a_n|<\varepsilon$ und löst nach $n$ auf. Für $b_n=2/\sqrt n$ ist $-\varepsilon<b_n$ immer erfüllt, weil $b_n>0$ ist. Es bleibt

$$\frac2{\sqrt n}<\varepsilon\iff\frac4n<\varepsilon^2\iff n>\frac4{\varepsilon^2}.$$

Quadrieren ist hier umkehrbar, weil beide Seiten positiv sind. Mit $N_0:=\lfloor4/\varepsilon^2\rfloor+1$ ist $2/\sqrt n$ also eine Nullfolge, für $\varepsilon=0{,}5$ etwa ist $n>16$ verlangt. Sie dient in Stufe [3](nullfolgen-vergleichen.html#stufe-3) als Vergleich.

**Was keine Nullfolge ist.** Verneint man [(2.1)](#gl-2-1) nach den Regeln aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) ($\forall$ wird $\exists$, $\exists$ wird $\forall$, die letzte Aussage kehrt sich um), ergibt sich

<span class="anker" id="gl-2-3"></span>
$$\{a_n\}\text{ ist keine Nullfolge}\quad\iff\quad\exists\,\varepsilon_0>0\ \ \forall\,N\in\mathbb{N}\ \ \exists\,n_0>N:\ \ |a_{n_0}|\ge\varepsilon_0. \tag{2.3}$$

Du gewinnst also mit einer festen Toleranz $\varepsilon_0$, wenn hinter jedem Index ein Glied draußen liegt. Beispiel: $g_n=\frac12\bigl(1+(-1)^n\bigr)$ lautet $0;\ 1;\ 0;\ 1;\ \dots$ Unendlich viele Glieder sind exakt null, trotzdem ist das keine Nullfolge: Wähle $\varepsilon_0=\frac12$. Zu jedem $N$ ist $n_0=2N$ gerade und größer als $N$, und $g_{n_0}=1\ge\varepsilon_0$. Dabei darf $n_0$ von $N$ abhängen, $\varepsilon_0$ aber nicht.

⁠**Grenzfall:** Die konstante Folge 0 gewinnt jede Runde mit $N_0=1$. Das Kriterium verlangt also kein Annähern, sondern nur das Einhalten der Toleranz. In der Elektrotechnik kehrt diese Prüfung als Einschwingzeit wieder: die Zeit, ab der eine Ausgangsspannung ein Toleranzband um ihren Endwert nicht mehr verlässt.

:::frage Muss ich das kleinste $N_0$ finden?
Nein. Passt ein $N_0$, passt jedes größere, denn die Bedingung betrifft dann weniger Glieder. Für $\varepsilon=0{,}5$ gibt die Regel aus dem Beweis $N_0=7$, das kleinste mögliche ist 6. Beide gewinnen. Deshalb darf man beim Suchen großzügig nach oben abschätzen.
:::

:::frage Warum verlangt die Definition nicht gleich $\varepsilon=0$?
Eine Toleranz 0 verlangte $a_n=0$ ab einem Index. Die Abweichung $d_n$ ist aber nie 0 und hat trotzdem den Grenzwert 0. Grenzwerte handeln davon, dass der Abstand jede positive Zahl unterbietet, nicht davon, dass er verschwindet.
:::

:::aufgabe Aufgabe 2 ★★ Spiele selbst
<span class="anker" id="aufg-2"></span>

Gegeben ist $c_n=\dfrac5{2n+1}$. Finde das kleinste $N_0$ für $\varepsilon=0{,}1$ und für $\varepsilon=0{,}01$. Gib dann eine Regel $N_0(\varepsilon)$ an und beweise damit, dass $\{c_n\}$ eine Nullfolge ist.

:::loesung
$c_n$ fällt, und $c_n<\varepsilon$ ist gleichbedeutend mit $n>\frac12(5/\varepsilon-1)$. Für $\varepsilon=0{,}1$: $n>24{,}5$, also $N_0=24$ ($c_{24}=0{,}102$, $c_{25}=0{,}098$). Für $\varepsilon=0{,}01$: $n>249{,}5$, also $N_0=249$ ($c_{249}=0{,}01002$, $c_{250}=0{,}00998$). Regel: $N_0(\varepsilon):=\lfloor5/(2\varepsilon)\rfloor+1$. Beweis: Sei $\varepsilon>0$. Für $n>N_0$ ist $n>5/(2\varepsilon)$, also $2n+1>2n>5/\varepsilon$, also $0<c_n<\varepsilon$.
:::
:::

:::aufgabe Aufgabe 3 ★★ Richtig oder falsch
<span class="anker" id="aufg-3"></span>

Entscheide und begründe. (a) Liegen in jedem Intervall $(-\varepsilon,\varepsilon)$ unendlich viele Glieder, ist die Folge eine Nullfolge. (b) Die Folge $h_n=\frac1n$ für ungerade $n$, $h_n=2$ für gerade $n$ ist keine Nullfolge; gib $\varepsilon_0$ und $n_0(N)$ an. (c) Vertauscht man in [(2.1)](#gl-2-1) die Reihenfolge zu $\exists\,N_0\ \forall\,\varepsilon>0$, besteht $d_n$ den Test noch.

:::loesung
(a) Falsch. $g_n=0;\ 1;\ 0;\ 1;\ \dots$ hat in jedem Intervall um 0 unendlich viele Glieder und ist keine Nullfolge. Verlangt ist „alle bis auf endlich viele“. (b) Richtig. Wähle $\varepsilon_0=2$ und zu jedem $N$ den Index $n_0=2N$: Er ist gerade und größer als $N$, und $h_{n_0}=2\ge\varepsilon_0$. (c) Falsch. Ein einziges $N_0$ für alle $\varepsilon$ hieße $|d_n|<\varepsilon$ für jedes $\varepsilon>0$, also $d_n=0$ für alle $n>N_0$. Aber $d_n\ne0$. Nur Folgen, die ab einem Index exakt 0 sind, bestehen diesen Test.
:::
:::

::::formelsammlung
**Nullfolge (Epsilon-Kriterium)**

$$\forall\,\varepsilon>0\quad\exists\,N_0\in\mathbb{N}\quad\text{so dass}\quad\bigl(\,|a_n|<\varepsilon\quad\forall\,n>N_0\bigr)$$

Erst steht $\varepsilon$ fest, dann wird $N_0$ gewählt: $N_0=N_0(\varepsilon)$. Passt ein $N_0$, passt jedes größere.

**Schreibweise**

$$a_n\to0\ \text{für}\ n\to\infty,\qquad\lim_{n\to\infty}a_n=0$$

„$a_n$ konvergiert gegen null für $n$ gegen unendlich“; $\infty$ ist keine Zahl, Limes heißt Grenze.

**Epsilon-Schlauch**

$$|a_n|<\varepsilon\iff-\varepsilon<a_n<\varepsilon$$

In jedem noch so engen Schlauch um 0 liegen alle Glieder bis auf endlich viele.

**Gauß-Klammer**

$$\lfloor x\rfloor:=\max\{z\in\mathbb{Z}:\ z\le x\},\qquad\lceil x\rceil:=\min\{z\in\mathbb{Z}:\ x\le z\}$$

Für $x\in\mathbb{R}$: abrunden und aufrunden. Abrunden geht auf der Zahlengeraden immer nach links.

**Eigenschaften der Gauß-Klammer**

$$\lfloor x\rfloor\le x\le\lceil x\rceil,\quad0\le\lceil x\rceil-\lfloor x\rfloor\le1,\quad0\le\lceil x\rceil-x<1,\quad0\le x-\lfloor x\rfloor<1$$

Für alle $x\in\mathbb{R}$; $\lfloor x\rfloor=x=\lceil x\rceil$ genau für $x\in\mathbb{Z}$.

**Natürliche Zahl oberhalb von $x$**

$$\lfloor x\rfloor+1>x$$

Für $x\ge0$ eine natürliche Zahl; daher die Wahl $N_0:=\lfloor3/\varepsilon\rfloor+1$ für $|d_n|=3/n$.

**Keine Nullfolge**

$$\exists\,\varepsilon_0>0\ \ \forall\,N\in\mathbb{N}\ \ \exists\,n_0>N:\ \ |a_{n_0}|\ge\varepsilon_0$$

Verneinung des Epsilon-Kriteriums; $n_0$ darf von $N$ abhängen, $\varepsilon_0$ nicht.
::::

::::lernkarten
:::karte begriff Nullfolge
Wann heißt eine Folge $\{a_n\}_{n\in\mathbb{N}}$ reeller Zahlen eine Nullfolge, mit den Quantoren in der richtigen Reihenfolge?
---
Wenn $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}$, so dass $|a_n|<\varepsilon$ für alle $n>N_0$. Zu jeder Toleranz gibt es also einen Index, ab dem alle Glieder näher als $\varepsilon$ bei 0 liegen; $N_0$ darf von $\varepsilon$ abhängen.
--- falsch
Wenn $\exists\,N_0\in\mathbb{N}\ \forall\,\varepsilon>0$, so dass $|a_n|<\varepsilon$ für alle $n>N_0$. Ein einziger Index gilt also für jede Toleranz; die Glieder ab $N_0$ sind kleiner als jede positive Zahl, und das reicht für die Annäherung.
--- falsch
Wenn $\forall\,\varepsilon>0\ \exists\,n\in\mathbb{N}$ mit $|a_n|<\varepsilon$. Zu jeder Toleranz gibt es also mindestens ein Glied, das näher als $\varepsilon$ bei 0 liegt; die übrigen Glieder dürfen dabei beliebig weit draußen liegen.
--- falsch
Wenn $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}$, so dass $|a_n|<\varepsilon$ für unendlich viele $n>N_0$. In jedem Schlauch um 0 liegen also unendlich viele Glieder; dazwischen dürfen immer wieder Glieder draußen liegen.
:::
:::karte begriff Epsilon-Kriterium
Wie läuft das Epsilon-Kriterium als Spiel zwischen Toleranz und Index ab, und wann gilt es als bestanden?
---
Ein Toleranztest: Zu einer vorgegebenen Toleranz $\varepsilon>0$ nennt man einen Index $N_0$; die Runde ist gewonnen, wenn alle Glieder hinter Platz $N_0$ innerhalb der Toleranz liegen. Bestanden ist er erst, wenn jede Runde gewonnen wird, gleich welches $\varepsilon$.
--- falsch
Ein Toleranztest: Man wählt erst einen Index $N_0$, danach wird die Toleranz $\varepsilon>0$ vorgegeben; die Runde ist gewonnen, wenn das eine Glied $a_{N_0}$ innerhalb der Toleranz liegt. Bestanden ist er, wenn das für ein einziges $\varepsilon$ gelingt.
--- falsch
Ein Toleranztest: Zu einer vorgegebenen Toleranz $\varepsilon>0$ nennt man einen Index $N_0$; die Runde ist gewonnen, wenn alle Glieder bis Platz $N_0$ innerhalb der Toleranz liegen. Bestanden ist er, wenn einige Runden mit kleinem $\varepsilon$ gewonnen sind.
--- falsch
Ein Toleranztest: Zu einer vorgegebenen Toleranz $\varepsilon>0$ nennt man einen Index $N_0$; die Runde ist gewonnen, wenn ab $N_0$ unendlich viele Glieder in der Toleranz liegen. Bestanden ist er, wenn eine Runde mit sehr kleinem $\varepsilon$ gewonnen ist.
:::
:::karte begriff Epsilon-Schlauch
Was ist der Epsilon-Schlauch um 0, und welche Glieder einer Nullfolge müssen darin liegen?
---
Der Streifen $-\varepsilon<a_n<\varepsilon$, nach der Abstandsregel dasselbe wie $|a_n|<\varepsilon$. In jedem noch so engen Schlauch um 0 liegen alle Glieder bis auf endlich viele.
--- falsch
Der Streifen $-\varepsilon\le a_n\le\varepsilon$ einschließlich seiner Ränder. In jedem noch so engen Schlauch um 0 liegen unendlich viele Glieder; außerhalb dürfen ebenfalls unendlich viele liegen.
--- falsch
Der Streifen $0<a_n<\varepsilon$ oberhalb der Null. In jedem noch so engen Schlauch liegen alle Glieder bis auf endlich viele; negative Glieder zählen nicht, weil der Betrag sie nach oben spiegelt.
--- falsch
Der Streifen $-\varepsilon<a_n<\varepsilon$, nach der Abstandsregel dasselbe wie $|a_n|<\varepsilon$. In jedem noch so engen Schlauch um 0 liegen alle Glieder, auch die ersten; sonst ist es keine Nullfolge.
:::
:::karte begriff Limes
Was bedeutet die Schreibweise $\lim_{n\to\infty}a_n=0$, und woher kommen das Wort Limes und die Angabe $n\to\infty$?
---
Sie sagt, dass $\{a_n\}$ eine Nullfolge ist: $a_n$ konvergiert gegen null für $n$ gegen unendlich. Limes ist lateinisch für Grenze; $\infty$ ist keine Zahl, „$n\to\infty$“ steht für „für alle $n$ oberhalb eines passenden Index“.
--- falsch
Sie sagt, dass das Glied mit dem Index $n=\infty$ gleich 0 ist. Limes ist lateinisch für Ende; $\infty$ ist die größte natürliche Zahl, und an diesem letzten Platz nimmt die Folge ihren letzten Wert an.
--- falsch
Sie sagt, dass die Glieder $a_n$ der Null immer näher kommen, ohne sie zu erreichen. Limes ist lateinisch für Grenze; „$n\to\infty$“ heißt, dass $n$ nach unendlich vielen Schritten den Wert $\infty$ annimmt.
--- falsch
Sie sagt, dass unendlich viele Glieder gleich 0 sind. Limes ist lateinisch für Grenze; „$n\to\infty$“ heißt „für unendlich viele $n$“, und die übrigen Glieder dürfen dabei beliebige Werte haben.
:::
:::karte begriff Gauß-Klammer
Wie sind die Gauß-Klammern $\lfloor x\rfloor$ und $\lceil x\rceil$ für $x\in\mathbb{R}$ definiert, und was ergeben sie für $-1{,}2$?
---
$\lfloor x\rfloor:=\max\{z\in\mathbb{Z}:\ z\le x\}$ rundet ab, $\lceil x\rceil:=\min\{z\in\mathbb{Z}:\ x\le z\}$ rundet auf. Abrunden geht auf der Zahlengeraden immer nach links: $\lfloor-1{,}2\rfloor=-2$ und $\lceil-1{,}2\rceil=-1$.
--- falsch
$\lfloor x\rfloor:=\max\{z\in\mathbb{Z}:\ z\le x\}$ rundet ab, $\lceil x\rceil:=\min\{z\in\mathbb{Z}:\ x\le z\}$ rundet auf. Abrunden schneidet die Nachkommastellen ab: $\lfloor-1{,}2\rfloor=-1$ und $\lceil-1{,}2\rceil=-2$.
--- falsch
$\lfloor x\rfloor:=\min\{z\in\mathbb{Z}:\ x\le z\}$ rundet ab, $\lceil x\rceil:=\max\{z\in\mathbb{Z}:\ z\le x\}$ rundet auf. Abrunden geht immer zur Null hin: $\lfloor-1{,}2\rfloor=-1$ und $\lceil-1{,}2\rceil=-2$.
--- falsch
$\lfloor x\rfloor$ ist die nächstgelegene ganze Zahl, $\lceil x\rceil$ die übernächste; gerundet wird kaufmännisch, ab der Ziffer 5 nach oben. So ist $\lfloor-1{,}2\rfloor=-1$ und $\lceil-1{,}2\rceil=-2$.
:::
:::karte formel Eigenschaften der Gauß-Klammer
Welche Ungleichungen gelten für die Gauß-Klammern für alle $x\in\mathbb{R}$, und welche Folgerung liefert eine natürliche Zahl oberhalb von $x$?
---
$\lfloor x\rfloor\le x\le\lceil x\rceil$, $0\le\lceil x\rceil-\lfloor x\rfloor\le1$, $0\le\lceil x\rceil-x<1$, $0\le x-\lfloor x\rfloor<1$; Gleichheit $\lfloor x\rfloor=x=\lceil x\rceil$ genau für $x\in\mathbb{Z}$. Daraus folgt $\lfloor x\rfloor+1>x$, für $x\ge0$ eine natürliche Zahl oberhalb von $x$.
--- falsch
$\lfloor x\rfloor\le x\le\lceil x\rceil$ und $\lceil x\rceil-\lfloor x\rfloor=1$ für alle $x\in\mathbb{R}$, auch für ganze Zahlen. Daraus folgt $\lceil x\rceil>x$ für alle $x$: Zu jedem $x\ge0$ ist also schon $\lceil x\rceil$ eine natürliche Zahl oberhalb von $x$.
--- falsch
$\lceil x\rceil\le x\le\lfloor x\rfloor$, $0\le x-\lceil x\rceil<1$ und $0\le\lfloor x\rfloor-x<1$; Gleichheit genau für $x\in\mathbb{Z}$. Daraus folgt $\lfloor x\rfloor-1>x$, für $x\ge0$ eine natürliche Zahl oberhalb von $x$.
--- falsch
$\lfloor x\rfloor<x<\lceil x\rceil$ für alle $x\in\mathbb{R}$ und $\lceil x\rceil-\lfloor x\rfloor=1$. Daraus folgt $\lfloor x\rfloor+1>x$, aber nur für $x\notin\mathbb{Z}$; für ganze $x$ braucht man $\lfloor x\rfloor+2$, um über $x$ zu kommen.
:::
:::karte herleitung Abweichung ist Nullfolge
Wie beweist man mit einer Regel $N_0(\varepsilon)$, dass die Abweichung $d_n=(-1)^n\,\frac3n$ eine Nullfolge ist?
---
Für den Abstand zur 0 zählt das Vorzeichen nicht, weil $|(-1)^n|=1$ ist: $|d_n|=3/n$, und $3/n<\varepsilon$ ist gleichbedeutend mit $n>3/\varepsilon$.
---
Sei $\varepsilon>0$ beliebig vorgegeben. Wähle $N_0:=\lfloor3/\varepsilon\rfloor+1\in\mathbb{N}$; das ist erlaubt, weil $N_0$ erst nach $\varepsilon$ gewählt wird und von $\varepsilon$ abhängen darf.
---
Es gilt $N_0>3/\varepsilon$, weil $\lfloor x\rfloor+1>x$ für jedes $x\in\mathbb{R}$ gilt.
---
Für jedes $n>N_0$ folgt $n>3/\varepsilon$ und daraus $3/n<\varepsilon$, weil $n$ und $\varepsilon$ positiv sind. Also ist $|d_n|<\varepsilon$ für alle $n>N_0$.
:::
:::karte zusammenhang Index rückwärts finden
Wie findet man zu $b_n=2/\sqrt n$ und einer Toleranz $\varepsilon$ einen passenden Index $N_0$, und warum ist das Quadrieren dabei erlaubt?
---
Rückwärts: Man startet bei $|b_n|<\varepsilon$ und löst nach $n$ auf, $\frac2{\sqrt n}<\varepsilon\iff\frac4n<\varepsilon^2\iff n>\frac4{\varepsilon^2}$. Quadrieren ist umkehrbar, weil beide Seiten positiv sind; also gewinnt $N_0:=\lfloor4/\varepsilon^2\rfloor+1$.
--- falsch
Rückwärts: Man löst $|b_n|<\varepsilon$ nach $n$ auf, $\frac2{\sqrt n}<\varepsilon\iff\frac2n<\varepsilon^2\iff n>\frac2{\varepsilon^2}$. Quadrieren ist immer erlaubt, weil es jede Ungleichung erhält; also gewinnt $N_0:=\lfloor2/\varepsilon^2\rfloor+1$.
--- falsch
Vorwärts: Man rechnet die Glieder $b_1,b_2,\dots$ aus, bis zum ersten Mal eines kleiner als $\varepsilon$ ist, und nimmt dessen Index als $N_0$. Quadrieren braucht man dafür nicht, und die Glieder danach muss man nicht mehr prüfen.
--- falsch
Rückwärts: $\frac2{\sqrt n}<\varepsilon\iff n<\frac4{\varepsilon^2}$, weil sich beim Quadrieren eines Bruchs die Ungleichung umdreht. Also gewinnt jeder Index unterhalb von $4/\varepsilon^2$, etwa $N_0:=\lfloor4/\varepsilon^2\rfloor-1$, sofern er positiv ist.
:::
:::karte formel keine Nullfolge
Wie lautet die Verneinung der Definition der Nullfolge, also die Aussage, dass $\{a_n\}$ keine Nullfolge ist?
---
$\exists\,\varepsilon_0>0\ \forall\,N\in\mathbb{N}\ \exists\,n_0>N:\ |a_{n_0}|\ge\varepsilon_0$. Es gibt eine feste Toleranz, so dass hinter jedem Index noch ein Glied draußen liegt; $n_0$ darf von $N$ abhängen, $\varepsilon_0$ nicht.
--- falsch
$\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}\ \forall\,n>N_0:\ |a_n|\ge\varepsilon$. Zu jeder Toleranz liegen ab einem Index alle Glieder außerhalb des Schlauchs; ein einzelnes Glied draußen hinter jedem Index genügt dafür nicht.
--- falsch
$\exists\,\varepsilon_0>0\ \exists\,N\in\mathbb{N}\ \exists\,n_0>N:\ |a_{n_0}|\ge\varepsilon_0$. Es genügt also ein einziges Glied außerhalb einer Toleranz; $\varepsilon_0$, $N$ und $n_0$ dürfen dabei alle drei frei gewählt werden.
--- falsch
$\exists\,\varepsilon_0>0\ \forall\,N\in\mathbb{N}\ \exists\,n_0>N:\ |a_{n_0}|<\varepsilon_0$. Es gibt eine feste Toleranz, so dass hinter jedem Index noch ein Glied im Schlauch liegt; $n_0$ darf von $N$ abhängen, $\varepsilon_0$ nicht.
:::
:::karte zusammenhang Reihenfolge von Toleranz und Index
Warum darf im Epsilon-Kriterium der Index $N_0$ von $\varepsilon$ abhängen, und was würde aus der Bedingung, wenn man die Reihenfolge zu $\exists\,N_0\ \forall\,\varepsilon>0$ vertauschte?
---
Weil erst $\varepsilon$ feststeht und dann $N_0$ gewählt wird: $N_0=N_0(\varepsilon)$. Vertauscht hieße es: ein einziges $N_0$ für alle $\varepsilon$, also $a_n=0$ für alle $n>N_0$. Die Abweichung $d_n$ bestünde diesen Test nicht, weil $d_n\ne0$ ist.
--- falsch
Weil $N_0$ zuerst gewählt wird und $\varepsilon$ danach zu $N_0$ passen muss. Vertauscht änderte sich nichts, denn beide Reihenfolgen enthalten dieselben Quantoren und verlangen deshalb dasselbe von den Gliedern der Folge.
--- falsch
Weil $N_0$ immer proportional zu $1/\varepsilon$ ist, wie bei $d_n$. Vertauscht hieße es: Für kleinere $\varepsilon$ braucht man kein größeres $N_0$; diesen Test bestehen genau die Folgen, die monoton fallen, auch $d_n$.
--- falsch
Weil erst $\varepsilon$ feststeht und dann $N_0$ gewählt wird. Vertauscht wäre die Bedingung schwächer: Ein fester Index müsste nur zu einer einzigen Toleranz passen, und jede beschränkte Folge bestünde den Test, auch $d_n$.
:::
:::karte zusammenhang unendlich viele Glieder null
Warum ist $g_n=\frac12\bigl(1+(-1)^n\bigr)$ keine Nullfolge, obwohl unendlich viele ihrer Glieder exakt null sind?
---
Verlangt sind alle Glieder ab einem Index, nicht unendlich viele. Mit $\varepsilon_0=\frac12$ ist zu jedem $N$ der Index $n_0=2N$ gerade und größer als $N$, und $g_{n_0}=1\ge\varepsilon_0$: Hinter jedem Index liegt ein Glied draußen.
--- falsch
Weil ebenso unendlich viele Glieder gleich 1 sind und die Einsen in der Überzahl sind: Eine Nullfolge muss bis zu jedem Index mehr Glieder in der Nähe von 0 haben als außerhalb, und das gelingt hier nie.
--- falsch
Sie ist doch eine Nullfolge: In jedem Schlauch $(-\varepsilon,\varepsilon)$ liegen unendlich viele Glieder, nämlich alle mit ungeradem Index, und mehr verlangt das Epsilon-Kriterium nicht, auch nicht für kleine $\varepsilon$.
--- falsch
Weil ihre Glieder nicht monoton fallen: Eine Nullfolge muss der Null von Glied zu Glied näher kommen, und $g_n$ springt immer wieder von 0 auf 1 zurück, auch hinter jedem noch so großen Index.
:::
:::karte zusammenhang kleinster Index
Muss man beim Epsilon-Kriterium das kleinste passende $N_0$ finden, oder genügt irgendein passender Index?
---
Irgendeiner genügt: Passt ein $N_0$, passt jedes größere, weil die Bedingung dann weniger Glieder betrifft. Bei $d_n$ und $\varepsilon=0{,}5$ gibt die Regel $N_0=7$, das kleinste ist 6; beide gewinnen.
--- falsch
Man braucht das kleinste: Ein größeres $N_0$ schneidet Glieder ab, die schon im Schlauch liegen, und verfälscht damit den Test. Bei $d_n$ und $\varepsilon=0{,}5$ gewinnt deshalb nur $N_0=6$, die Regel mit $N_0=7$ ist dort zu grob.
--- falsch
Irgendeiner genügt, solange er nicht über dem kleinsten liegt: Ein kleineres $N_0$ prüft mehr Glieder und ist deshalb sicherer. Bei $d_n$ und $\varepsilon=0{,}5$ gewinnt etwa $N_0=3$, das größere $N_0=7$ dagegen nicht mehr.
--- falsch
Man braucht das kleinste, weil $N_0$ eine Funktion von $\varepsilon$ sein muss und eine Funktion jedem $\varepsilon$ genau einen Wert zuordnet. Bei $d_n$ und $\varepsilon=0{,}5$ ist das $N_0=6$; die Regel $N_0=7$ ist keine Funktion.
:::
:::karte zusammenhang Toleranz null
Warum verlangt die Definition der Nullfolge jede positive Toleranz $\varepsilon>0$, aber nicht die Toleranz $\varepsilon=0$?
---
Eine Toleranz 0 verlangte $a_n=0$ ab einem Index. Die Abweichung $d_n$ ist aber nie 0 und hat trotzdem den Grenzwert 0: Der Abstand soll jede positive Zahl unterbieten, nicht verschwinden.
--- falsch
Weil $\varepsilon=0$ die Bedingung zu schwach machte: Mit der Toleranz 0 bestünde jede beschränkte Folge den Test, denn die Bedingung $|a_n|<0$ ist für keine Folge zu prüfen und deshalb immer erfüllt.
--- falsch
Weil man durch $\varepsilon$ teilen muss, etwa in der Regel $N_0=\lfloor3/\varepsilon\rfloor+1$, und das ist für $\varepsilon=0$ nicht definiert. Inhaltlich verlangte $\varepsilon=0$ dagegen dasselbe wie jede positive Toleranz.
--- falsch
Weil die Toleranz 0 dasselbe verlangte wie alle positiven Toleranzen zusammen, nur umständlicher: Liegt $a_n$ in jedem Schlauch, ist $a_n=0$, und das gilt für jede Nullfolge ab einem Index.
:::
:::karte zusammenhang Annähern genügt nicht
Warum taugt die Aussage „die Glieder kommen der Null immer näher“ nicht als Definition einer Nullfolge?
---
Weil die Glieder von $1/n$ auch der Zahl $-1$ immer näher kommen, ohne gegen $-1$ zu streben. Umgekehrt nähert sich die konstante Folge 0 gar nicht an und ist doch eine Nullfolge: Verlangt ist nur das Einhalten jeder Toleranz.
--- falsch
Weil man „immer näher“ nicht messen kann: Abstände zwischen reellen Zahlen sind erst durch das Epsilon-Kriterium festgelegt, vorher gibt es keinen Betrag, der angibt, wie nah zwei Zahlen einander sind.
--- falsch
Weil sie nur für positive Folgen passt: Folgen mit Vorzeichenwechsel wie $d_n$ springen um die 0 herum und kommen ihr deshalb nicht immer näher, obwohl sie Nullfolgen sind; die Aussage ist also zu eng.
--- falsch
Weil eine Nullfolge die Null irgendwann erreichen muss: „Immer näher“ ließe auch Folgen zu, die die 0 nie treffen, und solche Folgen haben keinen Grenzwert, weil ihr Abstand zur 0 nie verschwindet.
:::
::::
