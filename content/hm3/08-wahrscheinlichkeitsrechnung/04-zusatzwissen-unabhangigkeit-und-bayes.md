---
title: Stufe 3: Zusatzwissen, Unabhängigkeit und Bayes
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3180400
summary: Eine Information ändert die Chancen.
tags: bedingte Wahrscheinlichkeit, Multiplikationsregel, stochastisch unabhängig
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Eine Information ändert die Chancen. Diese Stufe rechnet die Änderung aus, sagt, wann sie ausbleibt, und zeigt, wie man von einer Wirkung auf ihre Ursache zurückschließt.
:::

**Die Idee.** Weiß man, dass $B$ eingetreten ist, kommen nur noch die Ausgänge in $B$ in Frage. $B$ wird zum neuen $\Omega$, von $A$ bleibt $A\cap B$, und alle Anteile beziehen sich nun auf $B$.

:::definition Definition 3.1 (Bedingte Wahrscheinlichkeit)
<span class="anker" id="satz-3-1"></span>

Für Ereignisse $A,B$ mit $\mathbb{P}(B)\neq0$ heißt

<span class="anker" id="gl-3-1"></span>
$$\mathbb{P}(A|B):=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)} \tag{3.1}$$

__bedingte Wahrscheinlichkeit__ von $A$ gegeben $B$.
:::

⁠**So liest man das:** Bei den Vierer-Würfeln sei $C$ „Summe mindestens 6“ und $B$ „erster Würfel mindestens 3“. $C$ hat 6 Elemente, 5 davon liegen in $B$. Also ist $\mathbb{P}(B|C)=\frac56$, während $\mathbb{P}(B)=\frac12$ ist. Umgestellt gibt [(3.1)](#gl-3-1) die __Multiplikationsregel__ $\mathbb{P}(A\cap B)=\mathbb{P}(A|B)\,\mathbb{P}(B)$. **Grenzfall:** $\mathbb{P}(A|\Omega)=\mathbb{P}(A)$, die Information „irgendetwas ist passiert“ ändert nichts.

**Unabhängigkeit.** Ändert $B$ nichts an den Chancen von $A$, gilt $\mathbb{P}(A|B)=\mathbb{P}(A)$. Mit [(3.1)](#gl-3-1) wird daraus eine symmetrische Form, die auch für $\mathbb{P}(B)=0$ sinnvoll ist.

:::definition Definition 3.2 (Stochastische Unabhängigkeit)
<span class="anker" id="satz-3-2"></span>

Zwei Ereignisse $A,B$ heißen __stochastisch unabhängig__, wenn $\mathbb{P}(A\cap B)=\mathbb{P}(A)\,\mathbb{P}(B)$ gilt.
:::

Dann ist $A$ auch von $B^c$ unabhängig. Denn $A$ zerfällt disjunkt in $A\cap B$ und $A\cap B^c$, also ist

$$\mathbb{P}(A\cap B^c)=\mathbb{P}(A)-\mathbb{P}(A)\,\mathbb{P}(B)=\mathbb{P}(A)\,\mathbb{P}(B^c).$$

::::beispiel
$A$ „Summe 5“ und $B$ „erster Würfel mindestens 3“ aus Abb. [1](ereignisse-und-wahrscheinlichkeit.html#abb-1) sind unabhängig, denn $\frac2{16}=\frac14\cdot\frac12$. Zu jedem Wert des ersten Würfels führt nämlich genau einer von vier Werten des zweiten zur Summe 5. $C$ und $B$ von oben sind dagegen abhängig.
::::

::::beispiel ein Zufallspunkt
Ein Punkt falle zufällig in $\Omega=[0,1]^2$, und $\mathbb{P}(M)$ sei der Flächeninhalt von $M$. Sei $A=\{(x,y):x\le\frac14\}$ und $B=[\frac18,\frac58]\times[\frac12,1]$. Dann ist $\mathbb{P}(A)=\mathbb{P}(B)=\frac14$ und $\mathbb{P}(A\cap B)=\frac18\cdot\frac12=\frac1{16}$: unabhängig. $A$ nimmt von der Breite von $B$ denselben Anteil ein wie von der Breite von $\Omega$. Senkrecht lässt sich $B$ deshalb verschieben, ohne dass sich das ändert. Waagerecht nicht: $B'=[0,\frac12]\times[\frac12,1]$ gibt $\mathbb{P}(A\cap B')=\frac18\neq\frac1{16}$.
::::

:::definition Definition 3.3 (Unabhängigkeit vieler Ereignisse)
<span class="anker" id="satz-3-3"></span>

Sei $I$ eine beliebige Indexmenge. Die Ereignisse $A_i$, $i\in I$, heißen unabhängig, wenn für jede endliche Auswahl $i_1,\dots,i_m\in I$ gilt: $\mathbb{P}(A_{i_1}\cap\dots\cap A_{i_m})=\mathbb{P}(A_{i_1})\cdots\mathbb{P}(A_{i_m})$.
:::

Es genügt nicht, das für Paare zu prüfen. Sei $A_1$ „erster Würfel gerade“, $A_2$ „zweiter Würfel gerade“, $A_3$ „Summe gerade“. Jedes hat die Wahrscheinlichkeit $\frac12$, je zwei schneiden sich mit $\frac14$. Aber $\mathbb{P}(A_1\cap A_2\cap A_3)=\frac14\neq\frac18$, denn die ersten beiden legen das dritte fest.

:::satz Satz 3.4 (Gesetz der totalen Wahrscheinlichkeit)
<span class="anker" id="satz-3-4"></span>

Seien $A_1,A_2,\dots$ endlich oder abzählbar viele paarweise disjunkte Ereignisse mit Vereinigung $\Omega$. Dann gilt für jedes Ereignis $B$

<span class="anker" id="gl-3-2"></span>
$$\mathbb{P}(B)=\sum_i\mathbb{P}(B\cap A_i)=\sum_i\mathbb{P}(B|A_i)\,\mathbb{P}(A_i), \tag{3.2}$$

wobei die rechte Summe nur über die $A_i$ mit $\mathbb{P}(A_i)>0$ läuft.
:::

:::beweis Totale Wahrscheinlichkeit
$B$ ist die disjunkte Vereinigung der $B\cap A_i$, das gibt mit der $\sigma$-Additivität die erste Gleichung. Für $\mathbb{P}(A_i)>0$ ist $\mathbb{P}(B\cap A_i)=\mathbb{P}(B|A_i)\,\mathbb{P}(A_i)$, für $\mathbb{P}(A_i)=0$ folgt $\mathbb{P}(B\cap A_i)=0$ aus der Monotonie.
:::

::::beispiel
Ein Lager stammt zu $\frac12$, $\frac13$, $\frac16$ von drei Lieferanten mit den Ausschussquoten $\frac1{10}$, $\frac15$, $\frac3{10}$. Für $B$ „Teil defekt“ gibt [(3.2)](#gl-3-2) $\mathbb{P}(B)=\frac1{20}+\frac1{15}+\frac1{20}=\frac16$ (Abb. [3](#abb-3)). **Abzählbar viele Fälle:** Eine Nachricht bestehe mit $\mathbb{P}(Z=n)=2^{-n}$ aus $n\in\mathbb{N}$ Blöcken und komme dann mit $3^{-n}$ fehlerfrei an. Die Ereignisse $\{Z=n\}$ zerlegen $\Omega$, also ist $\mathbb{P}(\text{fehlerfrei})=\sum_{n=1}^\infty6^{-n}=\frac15$.

:::abbildung hm3/k8mosaik 3
Das Lager als Quadrat: Spaltenbreiten $\mathbb{P}(A_i)$, blaue Höhen $\mathbb{P}(B|A_i)$. Die blaue Gesamtfläche ist $\mathbb{P}(B)$, ihr Anteil in Spalte $k$ ist $\mathbb{P}(A_k|B)$.
:::
::::

:::satz Satz 3.5 (Formel von Bayes)
<span class="anker" id="satz-3-5"></span>

Für Ereignisse $A,B$ mit $\mathbb{P}(A),\mathbb{P}(B)>0$ gilt

<span class="anker" id="gl-3-3"></span>
$$\mathbb{P}(A|B)=\frac{\mathbb{P}(B|A)\,\mathbb{P}(A)}{\mathbb{P}(B)}. \tag{3.3}$$

Unter den Voraussetzungen von Satz [3.4](#satz-3-4) gilt für $\mathbb{P}(B)>0$ und $\mathbb{P}(A_k)>0$

<span class="anker" id="gl-3-4"></span>
$$\mathbb{P}(A_k|B)=\frac{\mathbb{P}(B|A_k)\,\mathbb{P}(A_k)}{\sum_i\mathbb{P}(B|A_i)\,\mathbb{P}(A_i)}. \tag{3.4}$$
:::

:::beweis Bayes
Die Multiplikationsregel liefert $\mathbb{P}(A|B)\,\mathbb{P}(B)=\mathbb{P}(A\cap B)=\mathbb{P}(B|A)\,\mathbb{P}(A)$. Für [(3.4)](#gl-3-4) ersetzt man $\mathbb{P}(B)$ durch [(3.2)](#gl-3-2).
:::

⁠**So liest man das:** Bekannt ist, wie oft die Ursache $A_k$ die Wirkung $B$ erzeugt, gesucht der Rückschluss. Im Lager stammt ein defektes Teil mit $\frac{1/20}{1/6}=\frac3{10}$ vom dritten Lieferanten, obwohl der nur $\frac16$ liefert.

:::frage Sind disjunkte Ereignisse unabhängig?
Im Gegenteil. Für $\mathbb{P}(A),\mathbb{P}(B)>0$ ist dann $\mathbb{P}(A\cap B)=0\neq\mathbb{P}(A)\,\mathbb{P}(B)$: Tritt $A$ ein, ist $B$ ausgeschlossen.
:::

:::aufgabe Aufgabe 4 ★ Ziehen ohne Zurücklegen
<span class="anker" id="aufg-4"></span>

Eine Urne enthält 5 rote und 3 blaue Kugeln. Drei werden nacheinander ohne Zurücklegen gezogen. Berechne die Wahrscheinlichkeit, dass (a) alle rot sind, (b) die zweite rot ist, (c) die erste und die dritte dieselbe Farbe haben. (d) Sind „erste rot“ und „zweite rot“ unabhängig?

:::loesung
(a) $\frac58\cdot\frac47\cdot\frac36=\frac5{28}$ nach der Multiplikationsregel. (b) Zerlegen nach der ersten Kugel: $\frac58\cdot\frac47+\frac38\cdot\frac57=\frac58$, wie für die erste Kugel: Vor dem Hinsehen sind alle Plätze gleichwertig. (c) Darum verhalten sich der erste und dritte Zug wie zwei Züge nacheinander: $\frac{5\cdot4+3\cdot2}{8\cdot7}=\frac{13}{28}$. (d) Nein: $\frac58\cdot\frac47=\frac5{14}\neq\frac58\cdot\frac58$.
:::
:::

:::aufgabe Aufgabe 5 ★★ Das Prüfgerät
<span class="anker" id="aufg-5"></span>

2 % aller Teile sind defekt. Ein Prüfgerät schlägt bei defekten Teilen mit 95 % an, bei guten mit 3 %. Es schlägt an. Wie wahrscheinlich ist das Teil defekt? Warum ist der Wert so klein?

:::loesung
$\mathbb{P}(\text{Alarm})=0{,}02\cdot0{,}95+0{,}98\cdot0{,}03=0{,}0484$, also $\mathbb{P}(\text{defekt}|\text{Alarm})=0{,}019/0{,}0484\approx0{,}393$. Gute Teile sind 49-mal häufiger, darum sind Fehlalarme häufiger als echte Treffer.
:::
:::
