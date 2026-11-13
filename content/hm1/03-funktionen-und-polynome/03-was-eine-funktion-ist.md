---
title: Stufe 1: Was eine Funktion ist
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
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

::::formelsammlung
**Funktion**

$$f:\begin{cases}A\longrightarrow B\\ a\longmapsto b=:f(a)\end{cases}$$

Für Mengen $A$, $B$ ($A=B$ ist möglich): Jedes $a\in A$ bekommt ein eindeutiges Bild $b\in B$, $a$ heißt Urbild von $b$. Andere Namen: Abbildung $f:A\to B$. Der Pfeil $\to$ verbindet Mengen, $\mapsto$ verbindet Elemente, $=:$ heißt „wird so genannt“.

**Definitionsbereich und Wertebereich**

$$\mathcal D(f):=A,\quad\mathcal W(f):=\{b\in B:\text{es gibt }a\in A\text{ mit }f(a)=b\}$$

Es gilt $\mathcal W(f)\subset B$; $B$ ist nur ein Vorrat. Für $A,B\subset\mathbb{R}$ heißt $f$ reelle Funktion, geschrieben meist $f:\mathcal D(f)\to\mathbb{R}$.

**Graph**

$$\mathcal G(f):=\{(a,f(a)):a\in A\}$$

Es ist $\mathcal G(f)\subset A\times B$. Eine senkrechte Linie trifft einen Graphen höchstens einmal.

**Gleichheit von Funktionen**

$$f=g:\Leftrightarrow\mathcal G(f)=\mathcal G(g)$$

Gleiche Graphen bedeuten auch gleiche Definitionsbereiche: $\sqrt x$ auf $[0,10]$ und $\sqrt x$ auf $\mathbb{R}_0^+$ haben dieselbe Formel und sind verschiedene Funktionen.
::::

::::lernkarten
:::karte begriff Funktion und Abbildung
Was ist eine Funktion oder Abbildung $f:A\to B$ von einer Menge $A$ in eine Menge $B$?
---
Eine Vorschrift, die jedem $a\in A$ ein eindeutiges $b\in B$ zuordnet, geschrieben $b=:f(a)$. Kein Element von $A$ hat zwei Bilder oder keines; zwei Elemente dürfen sich ein Bild teilen.
--- falsch
Eine Vorschrift, die jedem $b\in B$ genau ein $a\in A$ zuordnet, geschrieben $a=:f(b)$. Jedes Element von $B$ wird also getroffen, und zwei Elemente von $B$ dürfen sich ein $a$ teilen.
--- falsch
Eine Rechenformel in $x$, mit der man zu jedem Eingang den Ausgang ausrechnen kann. Ein gemessener Zusammenhang ohne Formel ist keine Funktion, dieselbe Formel ergibt immer dieselbe Funktion.
--- falsch
Eine Vorschrift, die jedem $a\in A$ mindestens ein $b\in B$ zuordnet. Ein Element von $A$ darf auch mehrere Bilder haben, solange keines ohne Bild bleibt, wie beim Einheitskreis.
:::
:::karte begriff Bild und Urbild
Was bezeichnen bei einer Funktion $f:A\to B$ mit $f(a)=b$ die Wörter Bild und Urbild?
---
$b$ heißt Bild von $a$, und $a$ heißt Urbild von $b$. Jedes $a\in A$ hat genau ein Bild; ein $b\in B$ kann dagegen mehrere Urbilder haben oder gar keines.
--- falsch
$a$ heißt Bild von $b$, und $b$ heißt Urbild von $a$, weil $b$ zuerst da ist und $a$ daraus berechnet wird. Jedes $b\in B$ hat deshalb genau ein Bild in $A$.
--- falsch
$b$ heißt Bild von $a$, und $a$ heißt Urbild von $b$. Wie jedes $a\in A$ genau ein Bild hat, hat auch jedes $b\in B$ genau ein Urbild, sonst wäre $f$ keine Funktion.
--- falsch
Das Bild ist der Graph von $f$, also die Kurve in der Ebene, und das Urbild ist die Formel, aus der man die Kurve zeichnet. Beide gehören zur ganzen Funktion, nicht zu einem $a$.
:::
:::karte begriff Definitionsbereich
Was ist der Definitionsbereich $\mathcal D(f)$ einer Funktion $f:A\to B$, und gehört er zur Funktion dazu?
---
Die Menge $A$ der zulässigen Eingänge, $\mathcal D(f):=A$. Er gehört zur Funktion: $\sqrt x$ auf $[0,10]$ und $\sqrt x$ auf $\mathbb{R}_0^+$ haben dieselbe Formel und sind verschiedene Funktionen.
--- falsch
Die Menge $B$, in der die Bilder liegen dürfen, $\mathcal D(f):=B$. Er ist nur ein Vorrat und gehört nicht zur Funktion: $\sqrt x$ auf $[0,10]$ und auf $\mathbb{R}_0^+$ ist dieselbe Funktion.
--- falsch
Die Menge aller $x\in\mathbb{R}$, in die man die Formel von $f$ einsetzen kann. Er ergibt sich immer aus der Formel und muss nicht eigens angegeben werden; $\sqrt x$ hat stets $\mathbb{R}_0^+$.
--- falsch
Die Menge der tatsächlich erreichten Werte, $\mathcal D(f):=\{f(a):a\in A\}$. Er gehört zur Funktion, ist immer eine Teilmenge von $B$ und für $\sqrt x$ gleich $\mathbb{R}_0^+$.
:::
:::karte begriff Wertebereich
Was ist der Wertebereich $\mathcal W(f)$ einer Funktion $f:A\to B$, und wie hängt er mit der Menge $B$ zusammen?
---
Die Menge der tatsächlich erreichten Bilder, $\mathcal W(f):=\{b\in B:\text{es gibt }a\in A\text{ mit }f(a)=b\}$. Es gilt $\mathcal W(f)\subset B$; $B$ ist nur ein Vorrat.
--- falsch
Die Menge $B$ selbst, also $\mathcal W(f):=B$. Jedes Element von $B$ wird von $f$ getroffen, denn sonst hätte man $B$ von vornherein kleiner wählen müssen.
--- falsch
Die Menge aller Eingänge, für die $f$ einen Wert liefert, $\mathcal W(f):=\{a\in A:f(a)\in B\}$. Es gilt $\mathcal W(f)\subset A$; meist ist es ganz $A$.
--- falsch
Die Menge aller reellen Zahlen, die als Ausgang denkbar sind, bei reellen Funktionen also stets $\mathbb{R}$. Man schreibt deshalb $f:\mathcal D(f)\to\mathbb{R}$, und $\mathcal W(f)=\mathbb{R}$ ist der Normalfall.
:::
:::karte begriff Graph
Welche Menge ist der Graph $\mathcal G(f)$ einer Funktion $f:A\to B$, und in welcher Menge liegt er?
---
Die Menge aller Paare aus Eingang und zugehörigem Ausgang, $\mathcal G(f):=\{(a,f(a)):a\in A\}$. Er ist eine Teilmenge des kartesischen Produkts, $\mathcal G(f)\subset A\times B$.
--- falsch
Die Menge aller Paare $(a,b)$ mit $a\in A$ und $b\in B$, also $\mathcal G(f):=A\times B$. Er ist das ganze kartesische Produkt, aus dem $f$ dann einzelne Punkte auswählt.
--- falsch
Die Menge aller Paare $(f(a),a)$ mit $a\in A$, zuerst der Ausgang, dann der Eingang. Er ist eine Teilmenge von $B\times A$ und wird mit dem Ausgang auf der waagerechten Achse gezeichnet.
--- falsch
Die gezeichnete Kurve von $f$ in der Ebene. Er liegt immer in $\mathbb{R}^2$, auch wenn $A$ und $B$ keine Zahlen enthalten, und ist keine Menge, sondern ein Bild der Formel.
:::
:::karte begriff reelle Funktion
Wann heißt eine Funktion $f:A\to B$ eine reelle Funktion, und wie schreibt man sie meist?
---
Wenn $A,B\subset\mathbb{R}$ gilt, Eingänge und Ausgänge also reelle Zahlen sind. Da man $\mathcal W(f)$ oft nicht kennt, schreibt man meist $f:\mathcal D(f)\to\mathbb{R}$.
--- falsch
Wenn ihre Ausgänge reelle Zahlen sind, also $B\subset\mathbb{R}$; die Eingänge dürfen beliebig sein. So ist die Länge eines Vektors eine reelle Funktion auf $\mathbb{R}^n$.
--- falsch
Wenn sie sich durch eine Formel mit reellen Zahlen angeben lässt. Eine gemessene Kennlinie ohne Formel ist keine reelle Funktion; man schreibt sie als $f:\mathbb{R}\to\mathbb{R}$.
--- falsch
Wenn $A,B\subset\mathbb{R}$ gilt und $f$ jeden Wert in $\mathbb{R}$ erreicht. Deshalb schreibt man $f:\mathcal D(f)\to\mathbb{R}$, denn bei reellen Funktionen ist stets $\mathcal W(f)=\mathbb{R}$.
:::
:::karte formel Gleichheit von Funktionen
Wann sind zwei Funktionen $f$ und $g$ gleich, und warum gehört dabei der Definitionsbereich dazu?
---
$f=g:\Leftrightarrow\mathcal G(f)=\mathcal G(g)$. Gleiche Graphen bedeuten auch gleiche Definitionsbereiche; $\sqrt x$ auf $[0,10]$ und auf $\mathbb{R}_0^+$ haben dieselbe Formel und sind verschieden.
--- falsch
$f=g:\Leftrightarrow$ $f$ und $g$ haben dieselbe Formel. Der Definitionsbereich gehört nicht dazu; $\sqrt x$ auf $[0,10]$ und auf $\mathbb{R}_0^+$ ist dieselbe Funktion, nur verschieden weit gezeichnet.
--- falsch
$f=g:\Leftrightarrow f(x)=g(x)$ für jedes $x$, an dem beide erklärt sind. Deshalb sind $f(x)=x$ und $g(x)=x^2/x$ gleich; einzelne fehlende Stellen spielen keine Rolle.
--- falsch
$f=g:\Leftrightarrow\mathcal W(f)=\mathcal W(g)$. Funktionen mit demselben Wertebereich sind gleich, etwa $\sqrt x$ auf $\mathbb{R}_0^+$ und der Betrag auf $\mathbb{R}$, die beide genau die Werte in $\mathbb{R}_0^+$ annehmen.
:::
:::karte zusammenhang derselbe Wert, verschiedene Funktionen
Warum sind $f(x)=x$ und $g(x)=x^2/x$ verschiedene Funktionen, obwohl sie für jedes $x\neq0$ denselben Wert liefern?
---
Weil $g(0)$ den Ausdruck $0/0$ ergäbe, der nicht erklärt ist: $\mathcal D(g)=\mathbb{R}\setminus\{0\}$. Die Graphen unterscheiden sich um den Punkt $(0,0)$, und gleich sind Funktionen nur bei gleichen Graphen.
--- falsch
Weil $g(0)=0/0=1$ ist, während $f(0)=0$ gilt. Beide Funktionen sind auf ganz $\mathbb{R}$ erklärt, unterscheiden sich aber im Wert an der Stelle $0$ und haben deshalb verschiedene Graphen.
--- falsch
Weil ihre Formeln verschieden aussehen: Funktionen sind genau dann gleich, wenn ihre Formeln Zeichen für Zeichen übereinstimmen, auch wenn sie überall dieselben Werte liefern.
--- falsch
Sie sind gar nicht verschieden: Da $x^2/x=x$ durch Kürzen folgt, ist $g$ dieselbe Funktion wie $f$, auch an der Stelle $0$, wo man einfach den gekürzten Ausdruck einsetzt.
:::
:::karte zusammenhang senkrechte Linie
Warum ist der Einheitskreis $\{(x,y)\in\mathbb{R}^2:x^2+y^2=1\}$ nicht der Graph einer Funktion von $x$?
---
Weil er $(0,1)$ und $(0,-1)$ enthält: Der Eingang $0$ hätte zwei Ausgänge. Im Bild heißt das: Eine senkrechte Linie trifft einen Graphen höchstens einmal, den Kreis trifft sie zweimal.
--- falsch
Weil er geschlossen ist: Ein Graph muss nach links und rechts ohne Ende weiterlaufen. Eine waagerechte Linie trifft einen Graphen höchstens einmal, den Kreis trifft sie zweimal.
--- falsch
Weil er $(1,0)$ und $(-1,0)$ enthält: Zwei Eingänge haben denselben Ausgang $0$. Das ist bei einem Graphen verboten, denn jeder Ausgang darf nur zu einem Eingang gehören.
--- falsch
Weil man ihn nicht nach $y$ auflösen kann: Ein Graph ist nur eine Menge, die eine Formel $y=f(x)$ besitzt. Lässt sich keine Formel angeben, ist eine Menge von Paaren nie ein Graph.
:::
:::karte zusammenhang Wertebereich der Parabel
Warum ist der Wertebereich der Parabel $h(x)=(x-2)^2-1$ genau $[-1,\infty)$ und keine kleinere Menge?
---
Weil beides gilt: Ein Quadrat ist nie negativ, also $h(x)=(x-2)^2-1\ge-1$; und jedes $y\ge-1$ wird von $x=2+\sqrt{y+1}$ getroffen. Die Schranke allein zeigt nur, dass alle Werte in $[-1,\infty)$ liegen.
--- falsch
Weil ein Quadrat nie negativ ist, also $h(x)\ge-1$ gilt. Mehr ist nicht zu zeigen: Eine Parabel nimmt oberhalb ihres tiefsten Punkts jeden Wert an, das folgt bereits aus der Schranke.
--- falsch
Weil $h$ bei $x=2$ den Wert $-1$ hat und bei $x=0$ und $x=4$ den Wert $3$. Aus diesen drei Werten folgt schon, dass jeder Wert zwischen $-1$ und $\infty$ vorkommt.
--- falsch
Weil der Wertebereich einer reellen Funktion immer das Ziel $\mathbb{R}$ ist, abzüglich der Werte unter dem tiefsten Punkt. Den tiefsten Punkt $(2\,|\,{-1})$ liest man an der Scheitelform ab.
:::
:::karte zusammenhang konstante Funktion
Ist eine konstante Funktion $f(x)=b$ eine Funktion, obwohl alle Eingänge denselben Ausgang haben?
---
Ja. Verboten ist nur, dass ein Eingang zwei Ausgänge oder keinen hat; mehrere Eingänge dürfen sich einen Ausgang teilen. Ihr Wertebereich ist $\mathcal W(f)=\{b\}$.
--- falsch
Nein. Eine Funktion muss verschiedenen Eingängen verschiedene Ausgänge geben, sonst könnte man aus dem Ausgang den Eingang nicht mehr zurückgewinnen.
--- falsch
Ja, aber nur, wenn $b\neq0$ ist: Für $b=0$ hätte jeder Eingang den Ausgang null, und eine Zuordnung zu null gilt als fehlender Ausgang. Ihr Wertebereich wäre dann leer.
--- falsch
Nein. Ihr Graph ist eine waagerechte Gerade, und eine waagerechte Linie darf einen Graphen höchstens einmal treffen; die Gerade trifft sie aber überall.
:::
:::karte zusammenhang Eingänge ohne Zahlen
Warum ist die Länge eines Vektors $f(\vec x)=\sqrt{x_1^2+\dots+x_n^2}$ eine Funktion, aber keine reelle Funktion?
---
Weil sie jedem $\vec x\in\mathbb{R}^n$ genau einen Wert in $\mathbb{R}_0^+$ zuordnet, ihre Eingänge aber keine Zahlen sind. Reell heißt eine Funktion nur, wenn $A,B\subset\mathbb{R}$ gilt.
--- falsch
Weil ihr Wertebereich nur $\mathbb{R}_0^+$ ist und nicht ganz $\mathbb{R}$. Eine reelle Funktion muss jede reelle Zahl als Wert annehmen können, auch die negativen Zahlen.
--- falsch
Weil die Wurzel nicht für alle Eingänge erklärt ist: Für manche $\vec x$ ist $x_1^2+\dots+x_n^2$ negativ, dort hat $f$ keinen Wert, und das schließt reell aus.
--- falsch
Weil sie stückweise erklärt ist, je nach Vorzeichen der Einträge. Stückweise erklärte Vorschriften wie der Betrag sind zwar Funktionen, aber keine reellen Funktionen.
:::
::::
