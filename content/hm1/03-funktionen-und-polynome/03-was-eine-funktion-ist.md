---
title: Stufe 1: Was eine Funktion ist
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Funktionen und Polynome
order: 1230300
summary: Aus der Schule kennt man Funktionen als Formeln.
tags: Abbildung, Bild, Urbild, Definitionsbereich, Wertebereich, Graph, reelle Funktion
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Aus der Schule kennt man Funktionen als Formeln. Das reicht nicht: Ein gemessener Zusammenhang hat keine Formel, und dieselbe Formel kann zu verschiedenen Funktionen gehören. Diese Stufe sagt, was eine Funktion ist.
:::

**Die Idee.** Eine Funktion legt zu jedem zulässigen Eingang genau einen Ausgang fest (Abb. [1](#abb-1)). Sie ist die Liste dieser Paare aus Eingang und Ausgang, die Formel ist nur eine kurze Art, die Liste anzugeben. Zwei Eingänge dürfen sich einen Ausgang teilen, im Rechenmodell ist $h(0)=h(4)=3$. Ein Eingang darf aber nicht zwei Ausgänge haben und nicht ohne Ausgang bleiben. Sonst wäre $f(x)$ keine bestimmte Zahl, und man könnte nicht damit rechnen.

:::abbildung hm1/k3zuordnung 1
Links eine Funktion: Jedes Element von $A$ hat genau einen Pfeil, zwei Pfeile dürfen im selben Bild enden, und in $B$ darf etwas übrig bleiben. Mitte und rechts keine Funktionen: Ein Element hat zwei Bilder, oder eines hat keines.
:::

:::definition Definition 1.1 (Funktion)
<span class="anker" id="satz-1-1"></span>

Seien $A$, $B$ Mengen ($A=B$ ist möglich). Eine Funktion oder __Abbildung__ $f:A\to B$ ist eine Vorschrift, die jedem $a\in A$ ein eindeutiges $b\in B$ zuordnet:

<span class="anker" id="gl-1-1"></span>
$$f:\begin{cases}A\longrightarrow B\\ a\longmapsto b=:f(a).\end{cases} \tag{1.1}$$

$b$ heißt __Bild__ von $a$, $a$ heißt __Urbild__ von $b$. Weiter heißen

<span class="anker" id="gl-1-2"></span>
$$\mathcal D(f):=A,\quad\mathcal W(f):=\{b\in B:\text{es gibt }a\in A\text{ mit }f(a)=b\},\quad\mathcal G(f):=\{(a,f(a)):a\in A\} \tag{1.2}$$

__Definitionsbereich__, __Wertebereich__ und __Graph__ von $f$, es ist $\mathcal G(f)\subset A\times B$. Für $A,B\subset\mathbb{R}$ heißt $f$ __reelle Funktion__. Zwei Funktionen sind gleich, wenn ihre Graphen gleich sind: $f=g:\Leftrightarrow\mathcal G(f)=\mathcal G(g)$.
:::

⁠**So liest man das:** Der Pfeil $\to$ verbindet Mengen, $\mapsto$ verbindet Elemente, und $=:$ heißt „wird so genannt“. $B$ ist nur ein Vorrat, es gilt $\mathcal W(f)\subset B$. Da man $\mathcal W(f)$ oft nicht kennt, schreibt man bei reellen Funktionen meist $f:\mathcal D(f)\to\mathbb{R}$. Gleiche Graphen bedeuten auch gleiche Definitionsbereiche: $\sqrt x$ auf $[0,10]$ und $\sqrt x$ auf $\mathbb{R}_0^+$ haben dieselbe Formel und sind verschiedene Funktionen.

::::beispiel [Beispiele]
Die Parabel erreicht nur $y\ge-1$: Ein Quadrat ist nie negativ, also ist $h(x)=(x-2)^2-1\ge-1$, und jedes $y\ge-1$ wird von $x=2+\sqrt{y+1}$ getroffen. Für die Glocke ist $1+x^2\ge1$, also $0<b(x)\le1$.

| Funktion | $\mathcal D(f)$ | $\mathcal W(f)$ |
|---|---|---|
| linear: $f(x)=ax+b$ mit $a\neq0$ | $\mathbb{R}$ | $\mathbb{R}$ |
| Parabel $h$ | $\mathbb{R}$ | $[-1,\infty)$ |
| Glocke $b$ | $\mathbb{R}$ | $(0,1]$ |
| Wurzel: $f(x)=\sqrt x$ | $\mathbb{R}_0^+$ | $\mathbb{R}_0^+$ |
| Betrag: $f(x)=x$ für $x\ge0$, $f(x)=-x$ für $x<0$ | $\mathbb{R}$ | $\mathbb{R}_0^+$ |
| Länge eines Vektors: $f(\vec x)=\sqrt{x_1^2+\dots+x_n^2}$ | $\mathbb{R}^n$ | $\mathbb{R}_0^+$ |

Der Betrag zeigt: Eine Funktion darf stückweise erklärt sein. Die letzte Zeile zeigt: Eingänge müssen keine Zahlen sein, diese Funktion ist nicht reell.
::::

⁠**Grenzfall:** Für $a=0$ ist $f(x)=b$ konstant, alle Eingänge teilen sich einen Ausgang. Das ist erlaubt, $\mathcal W(f)=\{b\}$.

**Nicht jede Menge von Paaren ist ein Graph.** Der Einheitskreis $\{(x,y)\in\mathbb{R}^2:x^2+y^2=1\}$ enthält $(0,1)$ und $(0,-1)$: Der Eingang $0$ hätte zwei Ausgänge. Im Bild heißt das: Eine senkrechte Linie trifft einen Graphen höchstens einmal (Abb. [2](#abb-2)).

:::abbildung hm1/k3graph 2
Links der Graph der Parabel $h$. Jede Senkrechte trifft ihn genau einmal, der Wertebereich ist auf der $y$-Achse markiert. Rechts der Einheitskreis: Die Senkrechte bei $x=0{,}6$ trifft ihn zweimal, also ist er kein Graph.
:::

:::frage Sind $f(x)=x$ und $g(x)=x^2/x$ nicht dieselbe Funktion?
Für jedes $x\neq0$ liefern sie denselben Wert, das stimmt. Aber $g(0)$ wäre $0/0$ und ist nicht erklärt, also ist $\mathcal D(g)=\mathbb{R}\setminus\{0\}$, und die Graphen unterscheiden sich um den Punkt $(0,0)$. Stufe [9](rationale-funktionen-und-pole.html#stufe-9) nennt das eine Lücke.
:::

:::aufgabe Aufgabe 1 ★ Definitionsbereich, Wertebereich, Graph
<span class="anker" id="aufg-1"></span>

(a) Bestimme den größten möglichen Definitionsbereich in $\mathbb{R}$ und den Wertebereich von $f(x)=\sqrt{9-x^2}$ und $g(x)=|x-1|+2$. (b) Ist $M_1=\{(x,y)\in\mathbb{R}^2:x=y^2\}$ der Graph einer Funktion von $x$? Und $M_2=\{(x,y)\in\mathbb{R}^2:x=y^3\}$?

:::loesung
(a) Es muss $9-x^2\ge0$ sein, also $\mathcal D(f)=[-3,3]$. Größter Wert 3 bei $x=0$, kleinster 0 bei $x=\pm3$: $\mathcal W(f)=[0,3]$. Für $g$ ist $\mathcal D(g)=\mathbb{R}$ und wegen $|x-1|\ge0$ dann $\mathcal W(g)=[2,\infty)$. (b) $M_1$ nicht: $(4,2)$ und $(4,-2)$ liegen darin, und für $x<0$ gibt es kein $y$. $M_2$ ja: Zu jedem $x\in\mathbb{R}$ gibt es genau ein $y=\sqrt[3]{x}$.
:::
:::
