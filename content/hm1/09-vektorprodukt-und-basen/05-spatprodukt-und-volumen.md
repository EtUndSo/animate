---
title: Stufe 3: Spatprodukt und Volumen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektorprodukt und Basen
order: 1290500
summary: Das Vektorprodukt misst Flächen.
tags: Spatprodukt, Parallelepiped, Spat, Einheitswürfel
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Das Vektorprodukt misst Flächen. Für das Volumen eines schiefen Quaders fehlt die Höhe, und die liefert das Skalarprodukt.
:::

**Die Idee.** Volumen ist Grundfläche mal Höhe. Der Vektor $\vec b\times\vec c$ steht senkrecht auf der Grundfläche und hat ihren Inhalt als Länge. Das Skalarprodukt mit $\vec a$ multipliziert diese Länge mit dem Anteil von $\vec a$ längs der Senkrechten, und dieser Anteil ist die Höhe. Beide Faktoren stecken in einem Ausdruck (Abb. [3](#abb-3)).

:::definition Definition 3.1 (Spatprodukt)
<span class="anker" id="satz-3-1"></span>

Für $\vec a,\vec b,\vec c\in\mathbb{R}^3$ heißt $\operatorname{spat}(\vec a,\vec b,\vec c):=\langle\vec a,\vec b\times\vec c\rangle\in\mathbb{R}$ das __Spatprodukt__.
:::

:::satz Satz 3.2 (Volumen des Parallelepipeds)
<span class="anker" id="satz-3-2"></span>

Das von $\vec a,\vec b,\vec c\in\mathbb{R}^3$ aufgespannte __Parallelepiped__ (auch __Spat__)

$$P:=\bigl\{\alpha\vec a+\beta\vec b+\gamma\vec c:\ \alpha,\beta,\gamma\in[0,1]\bigr\}$$

hat das Volumen $\operatorname{Vol}(P)=|\operatorname{spat}(\vec a,\vec b,\vec c)|=|\langle\vec a,\vec b\times\vec c\rangle|$.
:::

⁠**So liest man das:** $P$ ist der schiefe Quader mit den Kanten $\vec a,\vec b,\vec c$, die Zahlen $\alpha,\beta,\gamma$ wandern durch alle seine Punkte. Der Betrag steht da, weil das Spatprodukt negativ sein kann. **Beispiel:** $\vec a=\vec e_1$, $\vec b=\vec e_2$, $\vec c=\vec e_3$ gibt den __Einheitswürfel__ $[0,1]^3$ mit Volumen 1. Im Modell ist $\operatorname{spat}(\vec k,\vec u,\vec v)=\langle(1,0,2),(2,-4,2)\rangle=6$.

:::beweis Grundfläche mal Höhe
Es ist $\operatorname{Vol}(P)=F\cdot h$. Sind $\vec b,\vec c$ abhängig, ist $P$ flach und $\vec b\times\vec c=\vec0$, beide Seiten sind 0. Sonst sei $\vec n:=\vec b\times\vec c\ne\vec0$. Nach (E3) ist die Grundfläche $F=\|\vec n\|$. Die Höhe ist die Länge der Projektion von $\vec a$ auf die Senkrechte zur Grundfläche, nach (E2) also auf $\operatorname{span}\{\vec n\}$:

$$\operatorname{Proj}_{\vec n}(\vec a)=\frac{\langle\vec a,\vec n\rangle}{\|\vec n\|^2}\,\vec n,\qquad h=\|\operatorname{Proj}_{\vec n}(\vec a)\|=\frac{|\langle\vec a,\vec n\rangle|}{\|\vec n\|}.$$

Also ist $F\cdot h=|\langle\vec a,\vec b\times\vec c\rangle|$. Im Modell: $F=\sqrt{24}$, $h=6/\sqrt{24}=1{,}225$.
:::

:::abbildung hm1/k9spat 3
Das Parallelepiped mit der Grundfläche aus $\vec u,\vec v$ und der dritten Kante $\vec k$. Die Projektion von $\vec k$ auf $\vec u\times\vec v$ ist $(\frac12,-1,\frac12)$. Ihre Länge $h=1{,}225$ ist die Höhe, das Volumen ist $\sqrt{24}\cdot1{,}225=6$. Der Pfeil $\vec u\times\vec v$ ist verkürzt gezeichnet.
:::

:::satz Satz 3.3 (Vorzeichen und Abhängigkeit)
<span class="anker" id="satz-3-3"></span>

Für $\vec a,\vec b,\vec c\in\mathbb{R}^3$ gilt:

<ol class="rm">

<li>

$\operatorname{spat}(\vec a,\vec b,\vec c)=\operatorname{spat}(\vec b,\vec c,\vec a)=\operatorname{spat}(\vec c,\vec a,\vec b)=\langle\vec c,\vec a\times\vec b\rangle$; Vertauschen zweier Vektoren kehrt das Vorzeichen um.

</li>

<li>

$(\vec a,\vec b,\vec c)$ ist ein Rechtssystem $\iff\operatorname{spat}(\vec a,\vec b,\vec c)>0$.

</li>

<li>

$\vec a,\vec b,\vec c$ sind linear unabhängig $\iff\operatorname{Vol}(P)\ne0\iff\operatorname{spat}(\vec a,\vec b,\vec c)\ne0$.

</li>

</ol>
:::

⁠**So liest man das:** (i) sagt, dass jede Seite des Spats Grundfläche sein darf. (ii) gibt die Orientierung: Rechte Hand oder linke. (iii) ist ein Test: Drei Vektoren sind genau dann abhängig, wenn der Körper flach ist. Im Modell ist $\operatorname{spat}(\vec w,\vec u,\vec v)=8-4-4=0$, passend zu $\vec w=2\vec u-\vec v$.

:::beweis Ausschreiben und projizieren
(i): Es gilt $\operatorname{spat}(\vec a,\vec b,\vec c)=a_1b_2c_3+a_2b_3c_1+a_3b_1c_2-a_1b_3c_2-a_2b_1c_3-a_3b_2c_1$. Zyklisches Weiterschieben von $\vec a,\vec b,\vec c$ vertauscht nur die Summanden. Das Vorzeichen beim Tauschen kommt aus Satz [2.1](rechenregeln-und-geometrie-im-raum.html#satz-2-1) (ii).

(ii): Es ist $\operatorname{Proj}_{\vec a\times\vec b}(\vec c)=\frac{\langle\vec c,\vec a\times\vec b\rangle}{\|\vec a\times\vec b\|^2}(\vec a\times\vec b)$. Der Faktor ist genau dann positiv, wenn $\vec c$ auf derselben Seite der Ebene von $\vec a,\vec b$ liegt wie $\vec a\times\vec b$, und $(\vec a,\vec b,\vec a\times\vec b)$ ist nach (E4) ein Rechtssystem.

(iii): Sind die Vektoren abhängig, ist nach (i) ohne Einschränkung $\vec a=\beta\vec b+\gamma\vec c$, also $\langle\vec a,\vec b\times\vec c\rangle=0$ nach (E2). Die Umkehrung folgt in Stufe [6](die-dimension.html#stufe-6).
:::

:::frage Hängt das Volumen davon ab, welche Seite ich als Grundfläche nehme?
Nein, das sagt (i). Im Modell gibt die Grundfläche aus $\vec u,\vec v$ die Werte $F=\sqrt{24}$, $h=1{,}225$. Die Grundfläche aus $\vec v,\vec k$ gibt mit $\vec v\times\vec k=(2,2,-1)$ die Werte $F=3$, $h=2$. Beide Male ist das Produkt 6.
:::

:::aufgabe Aufgabe 4 ★★ Spat
<span class="anker" id="aufg-4"></span>

Sei $\vec a=(1,1,0)$, $\vec b=(0,1,1)$, $\vec c_t=(1,0,t)$. (a) Berechne $\operatorname{spat}(\vec a,\vec b,\vec c_t)$ allgemein und das Volumen für $t=2$. (b) Für welches $t$ sind die Vektoren abhängig? Gib dort die Abhängigkeit an. (c) Für welche $t$ ist $(\vec a,\vec b,\vec c_t)$ ein Rechtssystem? Was gilt für $(\vec b,\vec a,\vec c_2)$?

:::loesung
(a) $\vec b\times\vec c_t=(t,1,-1)$, also $\operatorname{spat}=t+1$. Für $t=2$ ist das Volumen 3. (b) $t=-1$: $\vec c_{-1}=(1,0,-1)=\vec a-\vec b$. (c) Für $t>-1$. Tauschen kehrt das Vorzeichen um: $\operatorname{spat}(\vec b,\vec a,\vec c_2)=-3$, das ist ein Linkssystem.
:::
:::
