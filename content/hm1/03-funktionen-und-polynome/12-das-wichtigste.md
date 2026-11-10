---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1231200
summary: Wann sich eine Gleichung rückwärts lösen lässt und warum jede Nullstelle einen Faktor abspaltet
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine Funktion ist eine Zuordnung, die jedem Element ihres Definitionsbereichs (der Menge der zulässigen Eingänge) genau ein Bild gibt. Eine Formel ist nur eine Art, sie anzugeben.

</li>

<li>

Die Gleichung $f(x)=y$ hat für jedes $y$ genau eine Lösung, wenn $f$ bijektiv ist, also kein $y$ doppelt und keines gar nicht getroffen wird. Dann gibt es die Umkehrfunktion $f^{-1}$, und ihr Graph (das Bild der Zuordnung in der Ebene) ist der an $y=x$ gespiegelte Graph von $f$.

</li>

<li>

Ein Polynom ist durch seine Koeffizienten (die festen Zahlen vor den Potenzen) bestimmt. Teilt man es durch $x-x_0$, bleibt der Rest $P(x_0)$. Deshalb spaltet jede Nullstelle einen Linearfaktor ab, und ein Polynom vom Grad $n$ hat höchstens $n$ Nullstellen.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Funktion $f:A\to B$: jedem $a\in A$ genau ein Bild. $\mathcal D(f)=A$, $\mathcal W(f)\subset B$, $\mathcal G(f)=\{(a,f(a))\}$.

</li>

<li>

Gerade: $f(x)=f(-x)$, ungerade: $f(x)=-f(-x)$. Streng wachsend: $x<y\Rightarrow f(x)<f(y)$. Beschränkt: $|f|\le K$.

</li>

<li>

Injektiv: höchstens, surjektiv: mindestens, bijektiv: genau eine Lösung von $f(x)=y$. Streng monoton ergibt bijektiv auf $\mathcal W(f)$.

</li>

<li>

$(g\circ f)(x)=g(f(x))$. Injektiv: Es gibt $g$ mit $g(f(x))=x$. Surjektiv: Es gibt $g$ mit $f(g(y))=y$. Bijektiv: Genau ein $g=f^{-1}$ kann beides.

</li>

<li>

$f(x)=y\Leftrightarrow x=f^{-1}(y)$. Graph: Spiegelung an $y=x$. $f^{-1}(y)\neq1/f(y)$. Monotonie vererbt sich.

</li>

<li>

Polynom $\sum_{i=0}^na_ix^i$, $a_n\neq0$. Gleich für alle $x$ $\Leftrightarrow$ gleiche Koeffizienten.

</li>

<li>

Division: $P_n=S_{n-m}Q_m+T_k$ mit $k<m$ oder $T_k=0$.

</li>

<li>

Horner: $c_n=a_n$, $c_i=c_{i+1}x_0+a_i$; $c_0=P_n(x_0)$; $P_n(x)=(x-x_0)Q_{n-1}(x)+c_0$.

</li>

<li>

$P_n(x_0)=0\Leftrightarrow$ Faktor $x-x_0$; höchstens $n$ Nullstellen. $m$-fach: $(x-x_0)^mQ_{n-m}$, $Q_{n-m}(x_0)\neq0$; $m$ ungerade kreuzt, gerade berührt.

</li>

<li>

Pol: Nenner null, Zähler nach Kürzen nicht. Lücke: Faktor kürzt sich weg. Für große $|x|$ gilt $R\approx S$.

</li>

</ul>
:::

**Ausblick auf [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html).** „Über jede Grenze wachsen“ und „sich annähern“ sind hier Beschreibungen geblieben. [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) macht daraus den Grenzwert, zunächst für Folgen.

**Ein Prinzip hinter allen Ergebnissen.** Eine Funktion gibt zu jedem $x$ genau ein $y$. Fast alles in diesem Kapitel stellt die umgekehrte Frage: Wie viele $x$ gehören zu einem gegebenen $y$?

| Ergebnis | Woher es kommt |
|---|---|
| Funktion, Graph, Wertebereich | Genau ein Ausgang je Eingang; die erreichten $y$ bilden den Wertebereich (Stufe [1](was-eine-funktion-ist.html#stufe-1)) |
| gerade, ungerade, monoton, beschränkt | Die Eigenschaften sagen, wie sich $f(x)$ mit $x$ ändert, ohne jeden Wert zu rechnen (Stufe [2](gerade-monoton-beschrankt.html#stufe-2)) |
| injektiv, surjektiv, bijektiv | Höchstens, mindestens oder genau eine Lösung von $f(x)=y$ (Stufe [3](ruckwarts-injektiv-surjektiv-bijektiv.html#stufe-3)) |
| Umkehrfunktion, Wurzel | Genau eine Lösung für jedes $y$: Diese Lösung ist selbst eine Funktion von $y$ (Stufe [4](verknupfen-und-umkehren.html#stufe-4)) |
| Koeffizientenvergleich | Gleiche Funktion heißt gleiche Koeffizienten, nahe $x=0$ wird jeder einzeln sichtbar (Stufe [5](polynome-und-koeffizienten.html#stufe-5)) |
| Division mit Rest | Die höchste Potenz wird abgezogen, der Grad sinkt (Stufe [6](division-mit-rest.html#stufe-6)) |
| Horner-Schema | Ausklammern von $x$ spart Multiplikationen und liefert nebenbei den Quotienten (Stufe [7](das-horner-schema.html#stufe-7)) |
| Linearfaktor, Vielfachheit | Der Rest der Division durch $x-x_0$ ist der Wert $P(x_0)$ (Stufe [8](jede-nullstelle-spaltet-einen-linearfaktor-ab.html#stufe-8)) |
| Pol, Lücke, Asymptote | Teilen durch fast null macht $\vert R\vert $ groß; für große $\vert x\vert $ bleibt der Polynomteil (Stufe [9](rationale-funktionen-und-pole.html#stufe-9)) |
