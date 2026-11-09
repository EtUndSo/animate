---
title: Stufe 4: Anordnungsaxiome
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
order: 1210600
summary: Die Körperaxiome sagen nichts über „größer“.
tags: total angeordnet, Trichotomie
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Körperaxiome sagen nichts über „größer“. Welche Annahmen stecken hinter dem Rechnen mit Ungleichungen?
:::

**Die Idee.** Reelle Zahlen liegen der Größe nach auf einer Geraden. Man muss nur festlegen, welche Zahlen positiv sind. Dann ist „$x$ größer als $y$“ dasselbe wie „$x-y$ ist positiv“. Die Multiplikation mit einer negativen Zahl spiegelt die Gerade an der Null, deshalb dreht sich die Reihenfolge (Abb. [4](#abb-4)).

:::definition Definition 4.1 (Total angeordneter Körper)
<span class="anker" id="satz-4-1"></span>

Ein Körper $\mathbb K$ mit einer Relation „$>0$“ heißt __total angeordnet__, wenn gilt:

<ul>

<li>

⁠**(T1)** Jedes $x\in\mathbb K$ erfüllt genau eine der Beziehungen $x>0$, $x=0$, $(-x)>0$.

</li>

<li>

⁠**(T2)** $x>0\wedge y>0\Rightarrow x+y>0$.

</li>

<li>

⁠**(T3)** $x>0\wedge y>0\Rightarrow x\cdot y>0$.

</li>

</ul>

Man setzt $x>y:\Leftrightarrow x-y>0$, $x<y:\Leftrightarrow y>x$ und $x\ge y:\Leftrightarrow(x=y\vee x>y)$, entsprechend $x\le y$.
:::

⁠**So liest man das:** $x>0$ heißt „$x$ ist positiv“. (T2) und (T3): Summe und Produkt positiver Zahlen sind positiv. $x<0$ ist gleichbedeutend mit $(-x)>0$: $x$ ist negativ.

:::satz Satz 4.2 (Rechnen mit Ungleichungen)
<span class="anker" id="satz-4-2"></span>

In einem total angeordneten Körper gilt für alle $x,y,z,u,v$:

|  |  |
|---|---|
| (O1) __Trichotomie__ | genau eine der Beziehungen $x<y$, $x=y$, $x>y$ gilt |
| (O2) Transitivität | $x<y\wedge y<z\Rightarrow x<z$ |
| (O3) Monotonie der Addition | $x<y\Rightarrow x+z<y+z$ |
| (O4) Monotonie der Multiplikation | $x<y\wedge z>0\Rightarrow xz<yz$ |
| (a) Spiegeln | $x<y\Leftrightarrow-y<-x$ |
| (b) Addieren | $x<y\wedge u<v\Rightarrow x+u<y+v$ |
| (c) Vorzeichen | $xy>0\Leftrightarrow\bigl((x>0\wedge y>0)\vee(x<0\wedge y<0)\bigr)$ |
| (d) Quadrate | $x\ne0\Rightarrow x\cdot x>0$; insbesondere $1>0$ |
| (e) Quadrieren | für $x\ge0$, $y\ge0$: $x^2\ge y^2\Leftrightarrow x\ge y$ |
:::

⁠**So liest man das:** Eine Ungleichung verträgt jede Addition, aber nur die Multiplikation mit positiven Zahlen. Für $z<0$ dreht sie sich: $x<y\wedge z<0\Rightarrow xz>yz$. Für $z=0$ wird (O4) zu $0<0$, falsch. Gäbe es in einem angeordneten Körper ein $i$ mit $i\cdot i=-1$, wäre nach (d) $-1>0$ und $1>0$, also nach (T2) $0>0$. Deshalb lassen sich die komplexen Zahlen aus [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html) nicht anordnen. Statt (T1) bis (T3) könnte man gleichwertig (O1) bis (O4) als Axiome nehmen.

:::frage Darf ich eine Ungleichung quadrieren?
Nur, wenn beide Seiten nicht negativ sind, das ist (e). Ohne diese Voraussetzung: $-3<2$, aber $9>4$. Quadrieren spiegelt den negativen Teil der Geraden in den positiven, wie Mal $-1$ in Abb. [4](#abb-4).
:::

:::abbildung hm1/k1spiegel 4
Rechenmodell $x=-3<y=2$. Mal 2 streckt die Gerade von der Null weg, die Reihenfolge bleibt. Mal $-1$ spiegelt an der Null, die Reihenfolge dreht sich: $3>-2$.
:::

:::beweis Ordnungsregeln aus (T1) bis (T3)
(O1): (T1) für $x-y$. (O2): $(y-x)+(z-y)=z-x$ ist nach (T2) positiv. (O3): $(y+z)-(x+z)=y-x$. (O4): $(y-x)z>0$ nach (T3), mit (AM) also $yz-xz>0$. (a): $(-x)-(-y)=y-x$. (b): $x+u<y+u$ und $u+y<v+y$ nach (O3), dann (O2).

(c) „$\Leftarrow$“: Für $x,y>0$ ist das (T3). Für $x,y<0$ ist $(-x)(-y)>0$, und $(-x)(-y)=xy$. „$\Rightarrow$“ indirekt: Es sei $xy>0$, aber das Paar $(x,y)$ gehöre nicht zu den beiden Fällen rechts. Dann bleiben vier Fälle. Bei $x=0$ oder $y=0$ ist $xy=0$, gegen (T1). Bei $x<0<y$ folgt aus (O4) $xy<0\cdot y=0$, gegen $xy>0$. Bei $y<0<x$ ebenso. (d): Für $x\ne0$ ist $x>0$ oder $x<0$, nach (c) ist $x\cdot x>0$. Mit $x=1\ne0$ folgt $1>0$.

(e) „$\Leftarrow$“: Für $x=y$ ist nichts zu zeigen. Aus $x>y\ge0$ folgt $x\cdot x>y\cdot x\ge y\cdot y$ nach (O4) mit $z=x$ und $z=y$. „$\Rightarrow$“ als Kontraposition: Aus $0\le x<y$ folgt ebenso $x\cdot x\le x\cdot y<y\cdot y$.
:::

::::beispiel
Für $x\ne0$ ist $x$ positiv genau dann, wenn $x^{-1}$ positiv ist, denn $x\cdot x^{-1}=1>0$ und (c). Daher: Löse $\frac1x>2$. Für $x>0$ darf man mit $x$ multiplizieren: $1>2x$, also $0<x<\frac12$. Für $x<0$ ist die linke Seite negativ, es gibt keine Lösung.
::::

⁠**Grenzfall:** Bei $x=\frac12$ steht $2>2$, falsch, die Grenze gehört nicht dazu.

:::aufgabe Aufgabe 5 ★★ Ungleichungen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Zeige $x<y\wedge z<0\Rightarrow xz>yz$ aus (O4) und (a).

</li>

<li>

Für welche reellen $x\ne1$ gilt $\frac3{x-1}>1$? Unterscheide zwei Fälle.

</li>

</ol>

:::loesung
(a) Aus $z<0$ folgt $-z>0$, nach (O4) $-xz<-yz$, nach (a) $yz<xz$. (b) Fall $x>1$: Multiplikation mit $x-1>0$ gibt $3>x-1$, also $1<x<4$. Fall $x<1$: Die linke Seite ist negativ, keine Lösung. Ergebnis: $1<x<4$.
:::
:::
