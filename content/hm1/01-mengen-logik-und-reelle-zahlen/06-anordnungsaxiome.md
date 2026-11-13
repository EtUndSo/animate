---
title: Stufe 4: Anordnungsaxiome
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
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

⁠**So liest man das:** Eine Ungleichung verträgt jede Addition, aber nur die Multiplikation mit positiven Zahlen. Für $z<0$ dreht sie sich: $x<y\wedge z<0\Rightarrow xz>yz$. Für $z=0$ wird (O4) zu $0<0$, falsch. Gäbe es in einem angeordneten Körper ein $i$ mit $i\cdot i=-1$, wäre nach (d) $-1>0$ und $1>0$, also nach (T2) $0>0$. Deshalb lassen sich die komplexen Zahlen aus [Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html) nicht anordnen. Statt (T1) bis (T3) könnte man gleichwertig (O1) bis (O4) als Axiome nehmen.

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

::::formelsammlung
**Anordnungsaxiome**

$$x>0\wedge y>0\Rightarrow x+y>0,\qquad x>0\wedge y>0\Rightarrow x\cdot y>0$$

(T2) und (T3): Summe und Produkt positiver Zahlen sind positiv. (T1): Jedes $x\in\mathbb K$ erfüllt genau eine der Beziehungen $x>0$, $x=0$, $(-x)>0$. Ein Körper mit einer solchen Relation „$>0$“ heißt total angeordnet.

**Größer und kleiner**

$$x>y:\Leftrightarrow x-y>0,\qquad x<y:\Leftrightarrow y>x,\qquad x\ge y:\Leftrightarrow(x=y\vee x>y)$$

Entsprechend $x\le y$. $x<0$ ist gleichbedeutend mit $(-x)>0$: $x$ ist negativ.

**Trichotomie und Transitivität**

$$x<y\wedge y<z\Rightarrow x<z$$

(O1) Trichotomie: Genau eine der Beziehungen $x<y$, $x=y$, $x>y$ gilt. (O2) Transitivität wie oben.

**Monotonie**

$$x<y\Rightarrow x+z<y+z,\qquad x<y\wedge z>0\Rightarrow xz<yz$$

(O3): Eine Ungleichung verträgt jede Addition. (O4): Multiplizieren nur mit positiven Zahlen.

**Multiplikation mit einer negativen Zahl**

$$x<y\wedge z<0\Rightarrow xz>yz$$

Die Ungleichung dreht sich, denn Mal eine negative Zahl spiegelt die Zahlengerade an der Null. Für $z=0$ wird (O4) zu $0<0$, falsch.

**Spiegeln und Addieren**

$$x<y\Leftrightarrow-y<-x,\qquad x<y\wedge u<v\Rightarrow x+u<y+v$$

Regeln (a) und (b).

**Vorzeichen eines Produkts**

$$xy>0\Leftrightarrow\bigl((x>0\wedge y>0)\vee(x<0\wedge y<0)\bigr)$$

Daraus: Für $x\ne0$ ist $x$ positiv genau dann, wenn $x^{-1}$ positiv ist.

**Quadrate**

$$x\ne0\Rightarrow x\cdot x>0,\qquad1>0$$

Deshalb lässt sich kein Körper anordnen, in dem es ein $i$ mit $i\cdot i=-1$ gibt.

**Quadrieren**

$$x^2\ge y^2\Leftrightarrow x\ge y$$

Nur für $x\ge0$, $y\ge0$; ohne diese Voraussetzung gilt etwa $-3<2$, aber $9>4$.
::::

::::lernkarten
:::karte begriff Anordnung
Was legt die Anordnung eines Körpers fest, und wie erklärt man damit „$x$ größer als $y$“?
---
Sie legt fest, welche Zahlen positiv sind ($x>0$). Damit setzt man $x>y:\Leftrightarrow x-y>0$, $x<y:\Leftrightarrow y>x$ und $x\ge y:\Leftrightarrow(x=y\vee x>y)$.
--- falsch
Sie legt die Reihenfolge fest, in der man die Zahlen aufzählt. „$x$ größer als $y$“ heißt dann, dass $x$ in dieser Aufzählung später kommt als $y$.
--- falsch
Sie legt fest, welche Zahlen positiv sind ($x>0$). Damit setzt man $x>y:\Leftrightarrow x\cdot y>0$, also beide Zahlen positiv oder beide negativ.
--- falsch
Sie legt fest, welche Zahlen ganzzahlig sind. „$x$ größer als $y$“ heißt, dass man von $y$ durch wiederholtes Addieren von 1 zu $x$ gelangt.
:::
:::karte begriff total angeordnet
Wann heißt ein Körper $\mathbb K$ mit einer Relation „$>0$“ total angeordnet?
---
Wenn (T1) jedes $x\in\mathbb K$ genau eine der Beziehungen $x>0$, $x=0$, $(-x)>0$ erfüllt, (T2) $x>0\wedge y>0\Rightarrow x+y>0$ und (T3) $x>0\wedge y>0\Rightarrow x\cdot y>0$ gilt.
--- falsch
Wenn (T1) jedes $x\in\mathbb K$ mindestens eine der Beziehungen $x>0$, $x=0$, $(-x)>0$ erfüllt, (T2) $x>0\wedge y>0\Rightarrow x+y>0$ und (T3) $x>0\wedge y>0\Rightarrow x\cdot y>0$ gilt.
--- falsch
Wenn (T1) jedes $x\in\mathbb K$ genau eine der Beziehungen $x>0$, $x=0$, $(-x)>0$ erfüllt, (T2) $x>0\wedge y>0\Rightarrow x+y>0$ und (T3) $x>0\wedge y<0\Rightarrow x\cdot y>0$ gilt.
--- falsch
Wenn sich je zwei Elemente $x,y\in\mathbb K$ vergleichen lassen, also $x>y$ oder $y>x$ gilt; Summen und Produkte positiver Zahlen dürfen dabei auch negativ sein.
:::
:::karte begriff Trichotomie
Was besagt die Trichotomie (O1) für zwei Elemente $x$, $y$ eines total angeordneten Körpers?
---
Dass genau eine der Beziehungen $x<y$, $x=y$, $x>y$ gilt. Sie folgt aus (T1), angewandt auf $x-y$.
--- falsch
Dass mindestens eine der Beziehungen $x<y$, $x=y$, $x>y$ gilt; es können auch zwei zugleich gelten, etwa $x<y$ und $x>y$.
--- falsch
Dass aus $x<y$ und $y<z$ stets $x<z$ folgt. Sie ist ein eigenes Axiom und lässt sich aus (T1) bis (T3) nicht herleiten.
--- falsch
Dass genau eine der Beziehungen $x<0$, $x=0$, $x>0$ gilt; über zwei verschiedene Elemente $x$, $y$ sagt sie nichts.
:::
:::karte formel Monotonie
Welche Rechenoperationen verträgt eine Ungleichung $x<y$ nach (O3) und (O4)?
---
Jede Addition: $x<y\Rightarrow x+z<y+z$. Die Multiplikation nur mit positiven Zahlen: $x<y\wedge z>0\Rightarrow xz<yz$.
--- falsch
Jede Addition: $x<y\Rightarrow x+z<y+z$. Ebenso jede Multiplikation, $x<y\Rightarrow xz<yz$ für alle $z$, weil Mal nur wiederholtes Plus ist.
--- falsch
Die Addition nur mit positiven Zahlen: $x<y\wedge z>0\Rightarrow x+z<y+z$. Die Multiplikation dagegen mit jeder Zahl $z\ne0$: $xz<yz$.
--- falsch
Jede Addition: $x<y\Rightarrow x+z<y+z$. Die Multiplikation nur mit negativen Zahlen: $x<y\wedge z<0\Rightarrow xz<yz$.
:::
:::karte zusammenhang Ungleichung dreht sich
Warum dreht sich eine Ungleichung, wenn man sie mit einer negativen Zahl multipliziert?
---
Weil Mal eine negative Zahl die Zahlengerade an der Null spiegelt: Aus $x<y$ und $z<0$ folgt $xz>yz$. Rechnerisch ist $-z>0$, nach (O4) $-xz<-yz$ und nach (a) $yz<xz$.
--- falsch
Weil die Multiplikation mit einer negativen Zahl die Zahlengerade staucht: Große Zahlen werden stärker verkleinert als kleine, bis sie mit ihnen die Plätze tauschen.
--- falsch
Weil eine negative Zahl kein Inverses hat: Man kann die Multiplikation nicht rückgängig machen, und dadurch geht die ursprüngliche Reihenfolge verloren.
--- falsch
Weil beide Seiten negativ werden und für negative Zahlen die Ordnung umgekehrt gilt: $-5>-2$, weil 5 größer als 2 ist und das Minus die Größe nicht ändert.
:::
:::karte formel Vorzeichenregel
Wann ist ein Produkt $xy$ in einem total angeordneten Körper positiv?
---
Genau dann, wenn beide Faktoren positiv oder beide negativ sind: $xy>0\Leftrightarrow\bigl((x>0\wedge y>0)\vee(x<0\wedge y<0)\bigr)$.
--- falsch
Genau dann, wenn mindestens einer der beiden Faktoren positiv ist: $xy>0\Leftrightarrow(x>0\vee y>0)$.
--- falsch
Genau dann, wenn beide Faktoren positiv sind: $xy>0\Leftrightarrow(x>0\wedge y>0)$; ein Produkt negativer Zahlen ist negativ.
--- falsch
Genau dann, wenn die Faktoren verschiedene Vorzeichen haben: $xy>0\Leftrightarrow\bigl((x>0\wedge y<0)\vee(x<0\wedge y>0)\bigr)$.
:::
:::karte formel Quadrate
Was gilt in einem total angeordneten Körper für das Quadrat $x\cdot x$ einer Zahl $x\ne0$, und was folgt daraus für die $1$?
---
$x\ne0\Rightarrow x\cdot x>0$, denn $x$ ist positiv oder negativ, und in beiden Fällen ist das Produkt nach der Vorzeichenregel positiv. Mit $x=1$ folgt $1>0$.
--- falsch
$x\ne0\Rightarrow x\cdot x>0$ gilt nur für positive $x$; für negative $x$ ist auch $x\cdot x$ negativ. Ob $1>0$ gilt, ist deshalb eine eigene Festlegung.
--- falsch
$x\cdot x\ge x$ für alle $x\ne0$, weil Quadrieren eine Zahl vergrößert. Mit $x=1$ folgt nur $1\ge1$; über das Vorzeichen der $1$ sagt das nichts aus.
--- falsch
$x\ne0\Rightarrow x\cdot x>0$ ist ein eigenes Axiom neben (T1) bis (T3). Dass $1>0$ gilt, folgt daraus nicht, sondern aus dem Körperaxiom (NNE).
:::
:::karte herleitung Quadrate sind positiv
Wie folgt aus den Anordnungsaxiomen, dass $x\cdot x>0$ für jedes $x\ne0$ und insbesondere $1>0$ gilt?
---
Für $x\ne0$ ist nach (T1) $x>0$ oder $(-x)>0$, weil von den drei Beziehungen genau eine gilt und $x=0$ ausgeschlossen ist.
---
Ist $x>0$, dann ist $x\cdot x>0$, weil nach (T3) das Produkt positiver Zahlen positiv ist.
---
Ist $(-x)>0$, dann ist $(-x)(-x)>0$ nach (T3), und das ist $x\cdot x$, weil im Körper $(-x)(-y)=xy$ gilt.
---
Mit $x=1\ne0$ folgt $1>0$, weil $1\ne0$ nach (NNE) gilt und $1\cdot1=1$ ist.
:::
:::karte zusammenhang komplexe Zahlen nicht anordenbar
Warum lässt sich kein Körper anordnen, in dem es ein $i$ mit $i\cdot i=-1$ gibt?
---
Weil nach der Regel für Quadrate dann $-1=i\cdot i>0$ wäre und zugleich $1>0$. Nach (T2) folgte $0>0$, ein Widerspruch zu (T1).
--- falsch
Weil $i$ weder positiv noch negativ ist, sondern null: Aus $i\cdot i=-1$ folgt $i=0$, und die Null darf kein Quadrat $-1$ haben.
--- falsch
Weil $i$ keine Dezimaldarstellung hat und sich deshalb nicht auf der Zahlengeraden einzeichnen lässt; die Anordnung braucht eine Lage auf der Geraden.
--- falsch
Weil $i\cdot i=-1$ die Körperaxiome verletzt: $-1$ hätte dann zwei Wurzeln, und das widerspricht der Eindeutigkeit der Inversen.
:::
:::karte formel Quadrieren
Unter welcher Voraussetzung darf man eine Ungleichung quadrieren?
---
Nur wenn beide Seiten nicht negativ sind: Für $x\ge0$, $y\ge0$ gilt $x^2\ge y^2\Leftrightarrow x\ge y$. Ohne die Voraussetzung: $-3<2$, aber $9>4$.
--- falsch
Immer: Für alle $x$, $y$ gilt $x^2\ge y^2\Leftrightarrow x\ge y$, weil Quadrieren wie die Multiplikation mit einer positiven Zahl wirkt.
--- falsch
Nur wenn beide Seiten negativ sind: Für $x<0$, $y<0$ gilt $x^2\ge y^2\Leftrightarrow x\ge y$; positive Seiten muss man vorher spiegeln.
--- falsch
Nur wenn beide Seiten nicht negativ sind; dann dreht sich die Ungleichung aber um: Für $x\ge0$, $y\ge0$ gilt $x^2\ge y^2\Leftrightarrow x\le y$.
:::
:::karte zusammenhang Inverses positiv
Warum ist für $x\ne0$ die Zahl $x$ genau dann positiv, wenn ihr Inverses $x^{-1}$ positiv ist?
---
Weil $x\cdot x^{-1}=1>0$ ist und ein positives Produkt nach der Vorzeichenregel zwei Faktoren mit gleichem Vorzeichen hat.
--- falsch
Weil $x^{-1}=-x$ ist und die Spiegelung an der Null das Vorzeichen zweimal umkehrt, wenn man zweimal invertiert.
--- falsch
Weil $x\cdot x^{-1}=0$ ist und die Null weder positiv noch negativ ist; deshalb müssen beide Faktoren dasselbe Vorzeichen tragen.
--- falsch
Weil das Inverse eine Zahl nur kleiner macht, sie aber nie über die Null schiebt; der Abstand zur Null schrumpft, das Vorzeichen bleibt.
:::
:::karte zusammenhang Ungleichung mit Bruch
Wie löst man die Ungleichung $\frac1x>2$, und warum braucht man dabei eine Fallunterscheidung?
---
Weil nur die Multiplikation mit positiven Zahlen die Ungleichung erhält. Für $x>0$ gibt Multiplikation mit $x$: $1>2x$, also $0<x<\frac12$. Für $x<0$ ist $\frac1x$ negativ, es gibt keine Lösung.
--- falsch
Man multipliziert ohne Fallunterscheidung mit $x$ und erhält $1>2x$, also alle $x<\frac12$ mit $x\ne0$. Eine Fallunterscheidung braucht man nur bei Gleichungen, nicht bei Ungleichungen.
--- falsch
Weil man durch $x$ nur teilen darf, wenn $x$ ganzzahlig ist. Für ganzzahlige $x$ gibt es keine Lösung, für alle anderen $x$ gilt die Ungleichung genau für $x<\frac12$.
--- falsch
Weil nur die Multiplikation mit positiven Zahlen die Ungleichung erhält. Für $x>0$ gibt das $0<x<\frac12$; für $x<0$ dreht sie sich zu $1<2x$, also kommen alle $x>\frac12$ hinzu.
:::
::::
