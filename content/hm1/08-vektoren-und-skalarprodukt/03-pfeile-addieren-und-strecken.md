---
title: Stufe 1: Pfeile addieren und strecken
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektoren und Skalarprodukt
order: 1280300
summary: Eine Kraft hat Stärke und Richtung, eine einzelne Zahl reicht dafür nicht.
tags: Ursprung, Ortsvektor, Komponente, Nullvektor, Einheitsvektor, Gerade, Richtungsvektor, Parameterdarstellung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Eine Kraft hat Stärke und Richtung, eine einzelne Zahl reicht dafür nicht. Diese Stufe stellt Pfeile durch Zahlen dar und rechnet mit ihnen.
:::

**Die Idee.** Man wählt einen festen Punkt $O$, den __Ursprung__. Zu jedem Punkt $P$ gehört genau ein Pfeil von $O$ nach $P$, sein __Ortsvektor__ $\vec u=\overrightarrow{OP}$. Deshalb behandelt man Punkt und Pfeil als dasselbe Objekt (man *identifiziert* sie). Aus dem Bild ergeben sich zwei Rechenarten (Abb. [1](#abb-1)).

⁠*Addieren* heißt hintereinanderhängen: Erst geht man $\vec a$, dann vom Endpunkt aus $\vec b$. Die Schritte nach rechts addieren sich, ebenso die Schritte nach oben. Also addiert man Stelle für Stelle. Die Reihenfolge spielt keine Rolle, denn beide Wege enden an derselben Ecke eines Parallelogramms. *Strecken* heißt: Die Länge wird $\alpha$-mal so groß, die Richtung bleibt, für $\alpha<0$ kehrt sie sich um. Nach dem Strahlensatz wachsen dabei beide Katheten des Steigungsdreiecks mit demselben Faktor, also wird jede Stelle mit $\alpha$ multipliziert.

:::abbildung hm1/k8pfeile 1
Links die Addition: $\vec a$ und $\vec b$ spannen ein Parallelogramm auf, seine Diagonale ist $\vec a+\vec b=(4,3)$. Beide Wege enden am selben Punkt. Rechts die Streckung: $2\vec a=(6,2)$ liegt auf derselben Geraden wie $\vec a$, und $-\vec b=(-1,-2)$ zeigt entgegengesetzt zu $\vec b$.
:::

:::definition Definition 1.1 (Rechnen im $\mathbb{R}^n$)
<span class="anker" id="satz-1-1"></span>

Die Elemente von $\mathbb{R}^n$ schreibt man als Spalten. Für $\alpha\in\mathbb{R}$ setzt man

<span class="anker" id="gl-1-1"></span>
$$\vec x=\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix},\ \ \vec y=\begin{pmatrix}y_1\\\vdots\\y_n\end{pmatrix}:\qquad\vec x+\vec y:=\begin{pmatrix}x_1+y_1\\\vdots\\x_n+y_n\end{pmatrix},\qquad\alpha\cdot\vec x:=\begin{pmatrix}\alpha x_1\\\vdots\\\alpha x_n\end{pmatrix}. \tag{1.1}$$
:::

⁠**So liest man das:** $x_j$ heißt die $j$-te __Komponente__. Der __Nullvektor__ $\vec0=\overrightarrow{OO}$ hat nur Nullen, also die Länge null und keine bestimmte Richtung. Der Vektor $-\vec x$ hat die Komponenten $-x_j$, und $\vec u-\vec v:=\vec u+(-\vec v)$ ist der Pfeil von der Spitze von $\vec v$ zur Spitze von $\vec u$. Der $j$-te __Einheitsvektor__ $\vec e_j$ hat an Stelle $j$ eine 1 und sonst Nullen. Im Fließtext steht eine Spalte platzsparend liegend, $\vec a=(3,1)$ meint die Spalte. Im Raum gilt dasselbe: $\vec c+\vec d=(2,2,2)$ und $2\vec c-\vec d=(4,1,-2)=\vec f$. **Grenzfälle:** $\alpha=0$ gibt $\vec0$, $\alpha=1$ lässt den Pfeil unverändert. In der Elektrotechnik addieren sich Kräfte und Feldstärken genau so.

:::frage In Abb. [1](#abb-1) beginnt $\vec b$ einmal in $O$ und einmal an der Spitze von $\vec a$. Sind das zwei Vektoren?
Nein, ein Vektor. Er ist durch seine Komponenten festgelegt, also durch die Verschiebung, nicht durch den Startpunkt. Der Ortsvektor ist der Vertreter, der in $O$ beginnt.
:::

**Gerade und Strecke.** Von einem Punkt aus läuft man in Vielfachen einer festen Richtung (Abb. [2](#abb-2)).

:::definition Definition 1.2 (Gerade und Strecke)
<span class="anker" id="satz-1-2"></span>

<ol class="al">

<li>

Für $\vec p,\vec v\in\mathbb{R}^n$ mit $\vec v\ne\vec0$ heißt

<span class="anker" id="gl-1-2"></span>
$$G=\{\vec w\in\mathbb{R}^n:\ \vec w=\vec p+t\cdot\vec v\ \text{ für ein }t\in\mathbb{R}\} \tag{1.2}$$

__Gerade__ durch den Punkt $P$ (mit $\vec p=\overrightarrow{OP}$) mit __Richtungsvektor__ $\vec v$. Die Gleichung $\vec w=\vec p+t\vec v$ ($t\in\mathbb{R}$) heißt __Parameterdarstellung__ von $G$.

</li>

<li>

Für $\vec p=\overrightarrow{OP}$, $\vec q=\overrightarrow{OQ}\in\mathbb{R}^n$ heißt

<span class="anker" id="gl-1-3"></span>
$$\overline{PQ}=\{\vec w\in\mathbb{R}^n:\ \vec w=\vec p+t(\vec q-\vec p)\ \text{ für ein }t\in[0,1]\} \tag{1.3}$$

die __Strecke__ von $P$ nach $Q$.

</li>

</ol>
:::

⁠**So liest man das:** Der __Parameter__ $t$ zählt die Schritte, $\vec p$ ist der Start, $\vec v$ der Schritt. Für $\vec p=(0,2)$, $\vec v=\vec a$ gibt $t=1$ den Punkt $(3,3)$, $t=-1$ den Punkt $(-3,1)$. Bei der Strecke ist $\vec q-\vec p$ der Pfeil von $P$ nach $Q$. Für $t=0$ ist man in $P$, für $t=1$ in $Q$, für $t=\frac12$ im Mittelpunkt $\frac12(\vec p+\vec q)$, bei $P=(1,1)$ und $Q=(5,3)$ also in $(3,2)$. **Voraussetzung nötig:** Für $\vec v=\vec0$ bliebe von der Geraden nur der Punkt $P$.

:::abbildung hm1/k8gerade 2
Links die Gerade durch $(0,2)$ mit Richtung $\vec a$: Jeder Wert von $t$ gibt einen Punkt. Rechts die Strecke von $P=(1,1)$ nach $Q=(5,3)$: Nur $t\in[0,1]$ ist erlaubt.
:::

::::beispiel
Wo schneiden sich $g$: $\vec p+t\vec a$ mit $\vec p=(0,2)$ und $h$: $(1,-1)+s\,\vec b$? Gleichsetzen liefert je Komponente eine Gleichung: $3t=1+s$ und $2+t=-1+2s$. Aus der ersten folgt $s=3t-1$, die zweite gibt $t=1$, also $s=2$. Der Schnittpunkt ist $(3,3)$. In $\mathbb{R}^2$ gibt es drei Möglichkeiten: genau einen Schnittpunkt, keinen (die Geraden sind parallel) oder die Geraden sind gleich. In $\mathbb{R}^3$ kommt eine vierte dazu: Die Geraden sind nicht parallel und treffen sich trotzdem nicht. Sie heißen dann __windschief__.
::::

:::aufgabe Aufgabe 1 ★★ Pfeile, Strecken, Lagen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $2\vec a-3\vec b$ und $-\vec a+\frac12\vec b$.

</li>

<li>

Für $P=(1,-1,2)$ und $Q=(4,5,8)$: Bestimme den Mittelpunkt und die beiden Drittelpunkte von $\overline{PQ}$.

</li>

<li>

Bestimme die Lage von $g$: $(0,2)+t(3,1)$ zu $(4,2)+s(1,1)$, zu $(1,0)+s(6,2)$ und zu $(3,3)+s(-6,-2)$.

</li>

<li>

Zeige, dass $(1,0,0)+t(1,1,0)$ und $(0,0,2)+s(0,1,1)$ windschief sind.

</li>

</ol>

:::loesung
(a) $2\vec a-3\vec b=(6,2)-(3,6)=(3,-4)$ und $-\vec a+\frac12\vec b=(-3+\frac12,\ -1+1)=(-\frac52,0)$. (b) $\vec q-\vec p=(3,6,6)$. Mittelpunkt ($t=\frac12$): $(\frac52,2,5)$. Drittelpunkte ($t=\frac13,\frac23$): $(2,1,4)$ und $(3,3,6)$. (c) Erste Gerade: $3t=4+s$ und $2+t=2+s$ geben $s=t=2$, Schnittpunkt $(6,4)$. Zweite: $(6,2)=2\vec a$ ist parallel, und $(1,0)$ liegt nicht auf $g$, denn $3t=1$ gibt $t=\frac13$, aber $2+\frac13\ne0$. Kein Schnittpunkt. Dritte: $(-6,-2)=-2\vec a$, und $(3,3)$ liegt auf $g$ ($t=1$), die Geraden sind gleich. (d) Die Richtungen sind nicht parallel. Gleichsetzen gibt $1+t=0$, $t=s$, $0=2+s$. Die ersten beiden Gleichungen erzwingen $t=s=-1$, dann steht in der dritten $0=1$.
:::
:::
