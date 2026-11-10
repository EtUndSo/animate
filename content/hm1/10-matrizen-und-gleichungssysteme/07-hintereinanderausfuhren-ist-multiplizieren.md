---
title: Stufe 5: Hintereinanderausführen ist Multiplizieren
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
adresse: elektrotechnik/1-semester/hohere-mathematik-1/matrizen-und-lineare-gleichungssysteme
knoten: Kapitel 10: Matrizen und lineare Gleichungssysteme
order: 1300700
summary: Lineare Abbildungen lassen sich addieren und hintereinander ausführen.
tags: Matrizenprodukt, assoziativ, distributiv, Ring, Algebra, Nullteiler
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Lineare Abbildungen lassen sich addieren und hintereinander ausführen. Diese Stufe fragt, was dabei mit den Matrizen geschieht. Die Addition ist harmlos, das Hintereinanderausführen erzwingt eine neue Multiplikation.
:::

**Summen.** Für $L,M:V\to W$ linear und feste $\alpha,\beta\in\mathbb K$ ist

<span class="anker" id="gl-5-1"></span>
$$F:=\alpha L+\beta M:V\to W,\quad v\mapsto\alpha L(v)+\beta M(v) \tag{5.1}$$

wieder linear, denn $F(\lambda v_1+v_2)=\alpha L(\lambda v_1+v_2)+\beta M(\lambda v_1+v_2)=\lambda F(v_1)+F(v_2)$. Haben $L,M$ bezüglich $\mathcal B,\mathcal C$ die Matrizen $A=(a_{ij})$, $B=(b_{ij})$, so gehört zu $F$ die Matrix $C=(c_{ij})$ mit

<span class="anker" id="gl-5-2"></span>
$$c_{ij}=\alpha a_{ij}+\beta b_{ij}, \tag{5.2}$$

denn $F(v_j)=\alpha\sum_ia_{ij}w_i+\beta\sum_ib_{ij}w_i=\sum_i(\alpha a_{ij}+\beta b_{ij})w_i$, und die Koordinaten sind eindeutig. Das definiert Eintrag für Eintrag

$$A+B:=(a_{ij}+b_{ij}),\qquad\alpha\cdot A:=(\alpha a_{ij})$$

und macht $\mathbb K^{m\times n}$ zu einem Vektorraum. Null ist die Nullmatrix, das Negative $-A=(-a_{ij})$. Eine Basis bilden die $E_{ij}$ mit einer 1 in Zeile $i$, Spalte $j$ und sonst Nullen, denn $A=\sum_{i,j}a_{ij}E_{ij}$. Also ist $\dim\mathbb K^{m\times n}=m\cdot n$. Beispiel: $2D-S=\bigl(\begin{smallmatrix}-1&-3\\2&-1\end{smallmatrix}\bigr)$ schickt $(1,1)$ auf $2(-1,1)-(2,1)=(-4,1)$. Vorsicht: Über dem Körper $\mathbb{R}$ statt $\mathbb{C}$ hat $\mathbb{C}^{m\times n}$ die Dimension $2mn$.

**Die Idee beim Hintereinanderausführen.** Sind $L,M$ linear, ist auch $F=M\circ L$ linear: $F(\lambda v_1+v_2)=M(\lambda Lv_1+Lv_2)=\lambda M(Lv_1)+M(Lv_2)$. Welche Matrix gehört dazu? Die $j$-te Spalte ist das Bild von $e_j$. Nun ist $L(e_j)$ die $j$-te Spalte der rechten Matrix, und $M$ wirkt darauf wie immer: Die $j$-te Spalte des Produkts ist *linke Matrix mal $j$-te Spalte der rechten*.

:::satz Satz 5.1 (Matrizenprodukt)
<span class="anker" id="satz-5-1"></span>

Seien $\mathcal B=(v_1,\dots,v_n)$, $\mathcal C=(w_1,\dots,w_m)$, $\mathcal G=(z_1,\dots,z_\ell)$ Basen von $V,W,Z$. Die linearen Abbildungen $L:V\to W$ und $M:W\to Z$ mögen die Matrizen $\mathcal L=(a_{ij})\in\mathbb K^{m\times n}$ und $\mathcal M=(b_{ki})\in\mathbb K^{\ell\times m}$ haben. Dann hat $F=M\circ L$ die Matrix $\mathcal F=(c_{kj})\in\mathbb K^{\ell\times n}$ mit

<span class="anker" id="gl-5-3"></span>
$$c_{kj}=\sum_{i=1}^mb_{ki}a_{ij},\qquad k=1,\dots,\ell,\ j=1,\dots,n. \tag{5.3}$$

Man definiert das __Matrizenprodukt__ $\mathcal M\cdot\mathcal L:=\mathcal F$.
:::

:::beweis Matrizenprodukt
Für festes $j$ rechnet man mit der Definition von $\mathcal L$, der Linearität von $M$ und der Definition von $\mathcal M$:

$$F(v_j)=M\Bigl(\sum_{i=1}^ma_{ij}w_i\Bigr)=\sum_{i=1}^ma_{ij}M(w_i)=\sum_{i=1}^ma_{ij}\sum_{k=1}^\ell b_{ki}z_k=\sum_{k=1}^\ell\Bigl[\sum_{i=1}^mb_{ki}a_{ij}\Bigr]z_k.$$

Die Matrix $\mathcal F$ ist durch $F(v_j)=\sum_kc_{kj}z_k$ erklärt. Weil $(z_1,\dots,z_\ell)$ eine Basis ist, sind die Koeffizienten eindeutig, also gilt [(5.3)](#gl-5-3).
:::

⁠**So liest man das:** $c_{kj}$ ist „Zeile $k$ der linken mal Spalte $j$ der rechten Matrix“, für $\mathbb K=\mathbb{R}$ also $\langle\mathcal M_{k\bullet}^T,\mathcal L_{\bullet j}\rangle$. Deshalb sieht die Formel so aus: Das Produkt ist keine freie Vereinbarung, sondern das Hintereinanderausführen in Zahlen. [(5.3)](#gl-5-3) erklärt es für alle Matrizen passender Formate:

$$\underbrace{\mathcal M}_{\ell\times m}\cdot\underbrace{\mathcal L}_{m\times n}=\underbrace{\mathcal F}_{\ell\times n}.$$

Die Spaltenzahl links muss die Zeilenzahl rechts sein, denn die Abbildung $L$ muss dort enden, wo $M$ beginnt. Rechts vom Produkt steht das zuerst ausgeführte $L$: $\mathcal M\cdot\mathcal L$ heißt „$M$ nach $L$“. Im Schema von Abb. [4](koordinaten-und-darstellungsmatrix.html#abb-4) ist $\mathcal M\cdot\mathcal L=(\Phi_{\mathcal G}^{-1}\circ M\circ\Phi_{\mathcal C})\circ(\Phi_{\mathcal C}^{-1}\circ L\circ\Phi_{\mathcal B})=\Phi_{\mathcal G}^{-1}\circ F\circ\Phi_{\mathcal B}$, weil sich $\Phi_{\mathcal C}\circ\Phi_{\mathcal C}^{-1}=\operatorname{Id}$ heraushebt.

::::beispiel
Erst drehen, dann scheren, und umgekehrt (Abb. [6](#abb-6)):

$$SD=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}1&-1\\1&0\end{pmatrix},\qquad DS=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.$$

Probe mit der Ecke $(1,1)$: $S(D(1,1))=S(-1,1)=(0,1)$ und $D(S(1,1))=D(2,1)=(-1,2)$. Die erste Spalte von $SD$ ist $S\cdot(0,1)=(1,1)$, also $S$ mal erste Spalte von $D$.

:::abbildung hm1/k10produkt 6
Oben erst $D$, dann $S$, unten erst $S$, dann $D$. Das Einheitsquadrat landet an verschiedenen Stellen: Die Reihenfolge zählt, also $SD\ne DS$. Rot und grün sind wieder die Spalten.
:::
::::

:::satz Satz 5.2 (Rechenregeln für Matrizen)
<span class="anker" id="satz-5-2"></span>

Für Matrizen $X_1,X_2,X_3$ passender Formate gilt: (i) $X_1(X_2X_3)=(X_1X_2)X_3$ (__assoziativ__); (ii) $X_1(X_2+X_3)=X_1X_2+X_1X_3$ und (iii) $(X_1+X_2)X_3=X_1X_3+X_2X_3$ (__distributiv__). Für $A\in\mathbb K^{n\times n}$ ist $E_nA=AE_n=A$.
:::

:::beweis Rechenregeln
Sei $L_i:x\mapsto X_ix$. Nach Satz [5.1](#satz-5-1) gehört ein Produkt zu $L_i\circ L_k$. (i) Beide Seiten gehören zu $x\mapsto L_1(L_2(L_3(x)))$. (ii) Das ist die Linearität von $L_1$: $X_1((X_2+X_3)x)=X_1(X_2x+X_3x)=X_1X_2x+X_1X_3x$. (iii) gilt nach Definition der Summe: $(X_1+X_2)(X_3x)=X_1(X_3x)+X_2(X_3x)$. Zuletzt: $E_n$ gehört zu $\operatorname{Id}$, also $E_nA$ zu $\operatorname{Id}\circ L_A=L_A$ und $AE_n$ zu $L_A\circ\operatorname{Id}=L_A$.
:::

⁠**So liest man das:** Klammern setzen und ausmultiplizieren geht wie bei Zahlen, nur die Reihenfolge der Faktoren muss bleiben. Beispiel: $(S+E_2)D=SD+D=\bigl(\begin{smallmatrix}1&-2\\2&0\end{smallmatrix}\bigr)$.

**Was im Vergleich zu Zahlen fehlt.** $(\mathbb{R}^{n\times n},+,\cdot)$ erfüllt die Körperaxiome aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) mit zwei Ausnahmen: Die Multiplikation ist nicht kommutativ, und es gibt nicht zu jedem $A\ne0$ ein Inverses. Eine solche Struktur heißt __Ring__ mit Einselement $E_n$. Weil sie auch ein Vektorraum ist, heißt sie __Algebra__. Für $n\ge2$ gilt:

<ol class="rm">

<li>

Im Allgemeinen ist $AB\ne BA$, siehe $SD$ und $DS$.

</li>

<li>

Es gibt __Nullteiler__: Matrizen $A,B\ne0$ mit $AB=0$. Für $N=\bigl(\begin{smallmatrix}1&-1\\1&-1\end{smallmatrix}\bigr)$ ist $N^2=N\cdot N=0$. Der Mechanismus: $\operatorname{im}N=\operatorname{span}\{(1,1)\}$ und $N(1,1)=0$. Der erste Schritt schickt alles in den Kern des zweiten.

</li>

<li>

Viele $A\ne0$ haben keine Inverse: Aus $NX=E_2$ folgte $N=N\cdot NX=0\cdot X=0$.

</li>

</ol>

:::frage Darf ich wie bei Zahlen kürzen, also aus $AX_1=AX_2$ auf $X_1=X_2$ schließen?
Nur für $\ker A=\{0\}$. Der Mechanismus: $A(X_1-X_2)=0$ sagt nur, dass die Spalten von $X_1-X_2$ im Kern von $A$ liegen. Beispiel: Es ist $N\cdot N=0=N\cdot0$, aber $N\ne0$.
:::

:::aufgabe Aufgabe 6 ★ Produkte
<span class="anker" id="aufg-6"></span>

Sei $T=\begin{pmatrix}1&0&2\\3&1&0\end{pmatrix}$ und $Y=\begin{pmatrix}2&-1\\1&3\\0&4\end{pmatrix}$. (a) Berechne $TY$ und $YT$. Warum sind die Formate verschieden? (b) Sage ohne Rechnung die Matrizen $D^2$, $D^4$ und $S^n$ aus der Geometrie vorher und prüfe $D^2$, $S^2$ durch Rechnen.

:::loesung
(a) $TY=\begin{pmatrix}2&7\\7&0\end{pmatrix}$ und $YT=\begin{pmatrix}-1&-1&4\\10&3&2\\12&4&0\end{pmatrix}$. $TY$ führt von $\mathbb{R}^2$ über $\mathbb{R}^3$ nach $\mathbb{R}^2$, $YT$ von $\mathbb{R}^3$ über $\mathbb{R}^2$ nach $\mathbb{R}^3$. (b) Zwei Vierteldrehungen sind eine halbe Drehung: $D^2=-E_2$. Vier sind eine volle: $D^4=E_2$. Jede Scherung schiebt die Höhe 1 um 1 weiter: $S^n=\bigl(\begin{smallmatrix}1&n\\0&1\end{smallmatrix}\bigr)$, also $S^2=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$.
:::
:::

:::aufgabe Aufgabe 7 ★★ Nullteiler verstehen
<span class="anker" id="aufg-7"></span>

Sei $\tilde N=\begin{pmatrix}2&-4\\1&-2\end{pmatrix}$. (a) Bestimme $\ker\tilde N$ und $\operatorname{im}\tilde N$ und sage $\tilde N^2$ vorher. (b) Finde $X\ne0$ mit $\tilde NX=0$ und $X\tilde N\ne0$. Tipp: Die Spalten von $X$ müssen im Kern liegen.

:::loesung
(a) $2x_1-4x_2=0$ gibt $\ker\tilde N=\operatorname{span}\{(2,1)\}$. Die Spalten sind $(2,1)$ und $-2(2,1)$, also $\operatorname{im}\tilde N=\operatorname{span}\{(2,1)\}$. Das Bild liegt im Kern, also ist $\tilde N^2=0$. (b) Zum Beispiel $X=\begin{pmatrix}2&0\\1&0\end{pmatrix}$. Dann ist $\tilde NX=0$ und $X\tilde N=\begin{pmatrix}4&-8\\2&-4\end{pmatrix}\ne0$.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Zwei Spiegelungen
<span class="anker" id="aufg-8"></span>

Sei $R$ aus [(4.4)](koordinaten-und-darstellungsmatrix.html#gl-4-4) und $R_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ die Spiegelung an der $x_1$-Achse. Berechne $RR_1$ und $R_1R$. Zeige, dass beide Drehungen sind (Aufgabe [2](die-spalten-sind-die-bilder.html#aufg-2)), und bestimme mit $\cos\vartheta=\frac35$, $\sin\vartheta=\frac45$ den Drehwinkel durch den Winkel $\vartheta$ von $G$. Prüfe auch $R^2=E_2$ und erkläre dieses Ergebnis ohne Rechnung.

:::loesung
$RR_1=\dfrac1{25}\begin{pmatrix}-7&-24\\24&-7\end{pmatrix}$ und $R_1R=\dfrac1{25}\begin{pmatrix}-7&24\\-24&-7\end{pmatrix}$. Beide haben die Form der Drehmatrix: Nach den Additionstheoremen ([Kapitel 7](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/potenzreihen-und-eulersche-formel/potenzreihen-und-eulersche-formel.html)) ist $\cos2\vartheta=2\cos^2\vartheta-1=-\frac7{25}$ und $\sin2\vartheta=2\sin\vartheta\cos\vartheta=\frac{24}{25}$. Also dreht $RR_1$ um $2\vartheta$ und $R_1R$ um $-2\vartheta$. Zwei Spiegelungen ergeben eine Drehung um den doppelten Winkel zwischen den Achsen, die Reihenfolge bestimmt den Drehsinn. $R^2=E_2$, weil zweimal Spiegeln jeden Punkt an seinen Ort zurückbringt.
:::
:::
