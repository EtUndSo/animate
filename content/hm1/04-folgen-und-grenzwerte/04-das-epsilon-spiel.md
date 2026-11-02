---
title: Stufe 2: Das Epsilon-Spiel
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Folgen und Grenzwerte
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

**Was keine Nullfolge ist.** Verneint man [(2.1)](#gl-2-1) nach den Regeln aus [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) ($\forall$ wird $\exists$, $\exists$ wird $\forall$, die letzte Aussage kehrt sich um), ergibt sich

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
