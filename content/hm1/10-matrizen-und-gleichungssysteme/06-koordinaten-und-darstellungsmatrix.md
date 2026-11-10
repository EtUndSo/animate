---
title: Stufe 4: Koordinaten und Darstellungsmatrix
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
adresse: elektrotechnik/1-semester/hohere-mathematik-1/matrizen-und-lineare-gleichungssysteme
knoten: Kapitel 10: Matrizen und lineare Gleichungssysteme
order: 1300600
summary: Bisher galt die Matrix nur für Zahlenräume mit Standardbasis.
tags: Koordinatenabbildung, Koordinatenvektor, Darstellungsmatrix
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher galt die Matrix nur für Zahlenräume mit Standardbasis. Polynome sind keine Zahlenspalten, und eine Spiegelung an einer schrägen Geraden hat passendere Richtungen als $e_1,e_2$. Diese Stufe zeigt: Jede Basis macht aus einem Vektorraum einen Zahlenraum, und die Matrix hängt von dieser Wahl ab.
:::

**Die Idee.** Eine Basis ist ein Koordinatensystem. Sie ersetzt jeden Vektor durch die Liste seiner Koeffizienten, und diese Übersetzung verliert nichts. Rechnet man in Listen, ist $L$ wieder eine Matrix (Abb. [4](#abb-4)).

:::definition Definition 4.1 (Koordinatenabbildung)
<span class="anker" id="satz-4-1"></span>

Sei $\mathcal B=(v_1,\dots,v_n)$ eine Basis von $V$. Die Abbildung

$$\Phi_{\mathcal B}:\mathbb K^n\to V,\qquad(x_1,\dots,x_n)\mapsto\sum_{j=1}^nx_jv_j$$

heißt __Koordinatenabbildung__. Das $x$ mit $\Phi_{\mathcal B}(x)=v$ heißt __Koordinatenvektor__ $v_{\mathcal B}$ von $v$.
:::

$\Phi_{\mathcal B}$ ist linear, das rechnet man direkt nach. Der Kern ist $\{0\}$: Aus $\sum_jx_jv_j=0$ folgt $x=0$, weil die $v_j$ unabhängig sind. Wegen $\dim V=\dim\mathbb K^n=n$ ist $\Phi_{\mathcal B}$ nach Satz [3.5](kern-bild-und-die-bilanz-der-dimensionen.html#satz-3-5) (c) bijektiv. Für die Polynome $\mathcal P_2$ mit $\mathcal B=(1,x,x^2)$ ist der Koordinatenvektor von $3+4x+5x^2$ die Liste $(3,4,5)$.

:::satz Satz 4.2 (Umkehrabbildung)
<span class="anker" id="satz-4-2"></span>

Ist $L:V\to W$ linear und bijektiv, so ist $L^{-1}:W\to V$ wieder linear, also $L^{-1}\in\operatorname{Lin}(W,V)$.
:::

:::beweis Umkehrabbildung
Seien $w,\tilde w\in W$ und $\alpha\in\mathbb K$. Setze $v:=L^{-1}w$ und $\tilde v:=L^{-1}\tilde w$, also $Lv=w$ und $L\tilde v=\tilde w$. Dann ist $L(v+\tilde v)=w+\tilde w$. Wendet man $L^{-1}$ an, steht da $v+\tilde v=L^{-1}(w+\tilde w)$, das ist (L1). Ebenso folgt aus $L(\alpha v)=\alpha w$ die Gleichung $\alpha v=L^{-1}(\alpha w)$, das ist (L2).
:::

⁠**So liest man das:** Insbesondere ist $\Phi_{\mathcal B}^{-1}:V\to\mathbb K^n$, $v\mapsto v_{\mathcal B}$ linear: Koordinaten einer Summe sind die Summe der Koordinaten. **Warum bijektiv nötig ist:** $P$ hat keine Umkehrabbildung, $(3,6)$ hat unendlich viele Urbilder.

:::satz Satz 4.3 (Eine Abbildung ist durch die Bilder einer Basis festgelegt)
<span class="anker" id="satz-4-3"></span>

Sei $\mathcal B=(v_1,\dots,v_n)$ eine Basis von $V$.

<ol class="rm">

<li>

Eine lineare Abbildung $L:V\to W$ ist auf ganz $V$ durch die Werte $L(v_1),\dots,L(v_n)$ festgelegt.

</li>

<li>

Zu je $n$ Vektoren $y_1,\dots,y_n\in W$ gibt es genau eine lineare Abbildung $L:V\to W$ mit

<span class="anker" id="gl-4-1"></span>
$$L(v_j)=y_j\quad\text{für alle }j=1,\dots,n. \tag{4.1}$$

</li>

</ol>
:::

:::beweis Festlegung durch Basisbilder
(i) Jedes $v$ hat eine eindeutige Darstellung $v=\sum_j\alpha_jv_j$, und $L(v)=\sum_j\alpha_jL(v_j)$ nach Satz [1.2](lineare-abbildungen.html#satz-1-2) (b).

(ii) *Existenz:* Setze $L(v):=\sum_j\alpha_jy_j$ für $v=\sum_j\alpha_jv_j$. Das ist wohldefiniert, weil die $\alpha_j$ eindeutig sind. Für $\tilde v=\sum_j\tilde\alpha_jv_j$ hat $\lambda v+\tilde v$ die Koeffizienten $\lambda\alpha_j+\tilde\alpha_j$, also ist $L(\lambda v+\tilde v)=\lambda L(v)+L(\tilde v)$. Außerdem hat $v_j$ die Koeffizienten $0,\dots,1,\dots,0$, also gilt [(4.1)](#gl-4-1).

⁠*Eindeutigkeit:* Erfüllt auch $\tilde L$ die Gleichung [(4.1)](#gl-4-1), so ist $(L-\tilde L)(v_j)=0$ für alle $j$. Wegen der Linearität folgt $(L-\tilde L)(v)=\sum_j\alpha_j(L-\tilde L)(v_j)=0$ für alle $v$, also $L=\tilde L$.
:::

⁠**So liest man das:** Die Bilder einer Basis dürfen beliebig vorgegeben werden, und damit ist alles bestimmt. **Warum Basis nötig ist:** Sind die $v_j$ abhängig, etwa $v_2=2v_1$, darf man $y_1,y_2$ nicht frei wählen, denn es muss $y_2=2y_1$ gelten. Spannen sie nicht auf, ist $L$ außerhalb des Aufspanns nicht festgelegt.

:::definition Definition 4.4 (Darstellungsmatrix)
<span class="anker" id="satz-4-4"></span>

Sei zusätzlich $\mathcal C=(w_1,\dots,w_m)$ eine Basis von $W$. Schreibt man die Bilder in dieser Basis,

<span class="anker" id="gl-4-2"></span>
$$L(v_j)=\sum_{i=1}^m\ell_{ij}w_i,\qquad j=1,\dots,n, \tag{4.2}$$

so heißt $\mathcal L=\mathcal L_L^{\mathcal B,\mathcal C}:=(\ell_{ij})\in\mathbb K^{m\times n}$ die __Darstellungsmatrix__ von $L$ bezüglich $\mathcal B$ und $\mathcal C$.
:::

⁠**So liest man das:** Die $j$-te Spalte ist der Koordinatenvektor von $L(v_j)$. Die Regel aus Stufe [2](die-spalten-sind-die-bilder.html#stufe-2) bleibt also bestehen. Die $m\cdot n$ Zahlen $\ell_{ij}$ legen $L$ nach Satz [4.3](#satz-4-3) fest, und umgekehrt legt $L$ sie fest. In diesem Sinn identifiziert man $L$ mit $\mathcal L$, aber nur bei festen Basen.

:::satz Satz 4.5 (Bilder in Koordinaten)
<span class="anker" id="satz-4-5"></span>

Für $v\in V$ mit $v_{\mathcal B}=x$ und $w\in W$ mit $w_{\mathcal C}=y$ gilt

<span class="anker" id="gl-4-3"></span>
$$L(v)=w\iff y=\mathcal L\,x\iff y_i=\sum_{j=1}^n\ell_{ij}x_j\quad(i=1,\dots,m). \tag{4.3}$$
:::

:::beweis Bilder in Koordinaten
Es ist $L(v)=L(\sum_jx_jv_j)=\sum_jx_jL(v_j)=\sum_jx_j\sum_i\ell_{ij}w_i=\sum_i\bigl(\sum_j\ell_{ij}x_j\bigr)w_i$. Also hat $L(v)$ die Koordinaten $\sum_j\ell_{ij}x_j$. Weil die Koordinaten von $w$ eindeutig sind, folgen beide Richtungen.
:::

⁠**So liest man das:** [(4.2)](#gl-4-2) ist eine Gleichung in $W$ und läuft über den ersten Index, [(4.3)](#gl-4-3) sind Gleichungen in $\mathbb K$ und laufen über den zweiten. Abb. [4](#abb-4) zeigt den Zusammenhang: $\mathcal L=\Phi_{\mathcal C}^{-1}\circ L\circ\Phi_{\mathcal B}$. Wegen $v\in\ker L\iff v_{\mathcal B}\in\ker\mathcal L$ lassen sich Kern und Bild von $L$ in Koordinaten ausrechnen.

:::abbildung hm1/k10schema 4
Oben die Abbildung zwischen den Vektorräumen, unten dieselbe Abbildung als Matrix. Die senkrechten Pfeile übersetzen zwischen Vektoren und Koordinaten und lassen sich umkehren.
:::

::::beispiel Ableiten
Sei $\mathcal D:\mathcal P_2\to\mathcal P_1$ die Ableitung aus der Schule, $\mathcal D(a_0+a_1x+a_2x^2)=a_1+2a_2x$. Sie ist linear. Mit $\mathcal B=(1,x,x^2)$ und $\mathcal C=(1,x)$ sind die Bilder $\mathcal D(1)=0$, $\mathcal D(x)=1$, $\mathcal D(x^2)=2x$, also

$$\mathcal L=\begin{pmatrix}0&1&0\\0&0&2\end{pmatrix},\qquad\mathcal L\begin{pmatrix}3\\4\\5\end{pmatrix}=\begin{pmatrix}4\\10\end{pmatrix}.$$

Das heißt $(3+4x+5x^2)'=4+10x$. Der Kern besteht aus den konstanten Polynomen, und es ist $3=1+2$.
::::

::::beispiel Spiegelung
Sei $L:\mathbb{R}^2\to\mathbb{R}^2$ die Spiegelung an der Geraden $G=\operatorname{span}\{v\}$ mit $\|v\|=1$. Die Orthogonalprojektion ([Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html)) auf $G$ ist $\operatorname{Proj}_G(a)=\langle a,v\rangle v$. Von $a$ zum Lotfußpunkt führt $b=\operatorname{Proj}_G(a)-a$, das Spiegelbild liegt doppelt so weit: $L(a)=a+2b=2\langle a,v\rangle v-a$. Daraus ergeben sich $L(e_1)=2v_1v-e_1$ und $L(e_2)=2v_2v-e_2$, also

<span class="anker" id="gl-4-4"></span>
$$\mathcal L_L^{\mathcal E,\mathcal E}=\begin{pmatrix}2v_1^2-1&2v_1v_2\\2v_1v_2&2v_2^2-1\end{pmatrix},\qquad\text{für }v=\bigl(\tfrac35,\tfrac45\bigr):\quad R:=\frac1{25}\begin{pmatrix}-7&24\\24&7\end{pmatrix}, \tag{4.4}$$

wobei $\mathcal E=(e_1,e_2)$. Für $a=(2,1)$ ist $\langle a,v\rangle=2$, $\operatorname{Proj}_G(a)=(1{,}2;\ 1{,}6)$, $b=(-0{,}8;\ 0{,}6)$ und $L(a)=(0{,}4;\ 2{,}2)$ (Abb. [5](#abb-5)). Jetzt dieselbe Abbildung in der Basis $\tilde{\mathcal B}=(v,u)$ mit $u=(-v_2,v_1)$, im Beispiel $u=(-\frac45,\frac35)$. Ihre Vektoren stehen senkrecht aufeinander und haben die Länge 1. Die Formel gibt $L(v)=2v-v=v$ und $L(u)=-u$, also

$$\mathcal L_L^{\tilde{\mathcal B},\tilde{\mathcal B}}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

Die Abbildung ist dieselbe, die Matrix eine andere: Die Matrix hängt von den gewählten Basen ab. Eine gute Basis macht sie übersichtlich.

:::abbildung hm1/k10spiegel 5
Links die Spiegelung von $a=(2,1)$ an $G$ über den Lotfußpunkt $\operatorname{Proj}_G(a)$. Der Pfeil $b$ wird zweimal angetragen. Rechts die Basis aus $v$ und $u$: $v$ bleibt, $u$ kehrt sich um. Daher die übersichtliche Matrix.
:::
::::

:::frage Wenn die Matrix von den Basen abhängt, was bleibt dann gleich?
Alles, was man ohne Basis sagen kann: die Abbildung selbst, $\dim\ker L$, $\dim\operatorname{im}L$, injektiv, surjektiv. Beide Spiegelungsmatrizen oben haben deshalb den Kern $\{0\}$. Die Einträge dagegen sagen nur etwas zusammen mit den Basen.
:::

:::aufgabe Aufgabe 5 ★★ Darstellungsmatrix wechselt mit der Basis
<span class="anker" id="aufg-5"></span>

Sei $\mathcal D:\mathcal P_3\to\mathcal P_2$ die Ableitung.

<ol class="al">

<li>

Bestimme die Darstellungsmatrix für $\mathcal B=(1,x,x^2,x^3)$ und $\mathcal C=(1,x,x^2)$. Berechne damit die Ableitung von $p=1-2x+3x^3$.

</li>

<li>

Bestimme Kern, Bild und prüfe [(3.1)](kern-bild-und-die-bilanz-der-dimensionen.html#gl-3-1).

</li>

<li>

Wiederhole (a) mit $\tilde{\mathcal C}=(1,\ 1+x,\ 1+x+x^2)$. Welche Einträge ändern sich? Was bleibt gleich?

</li>

</ol>

:::loesung
(a) $\mathcal D(1)=0$, $\mathcal D(x)=1$, $\mathcal D(x^2)=2x$, $\mathcal D(x^3)=3x^2$ ergibt $\mathcal L=\begin{pmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\end{pmatrix}$. Mit $p_{\mathcal B}=(1,-2,0,3)$ folgt $\mathcal L\,p_{\mathcal B}=(-2,0,9)$, also $p'=-2+9x^2$. (b) $\ker\mathcal D=\operatorname{span}\{1\}$, $\operatorname{im}\mathcal D=\mathcal P_2$, $4=1+3$. (c) Die Bilder lauten $0$, $1$, $2x=-2\cdot1+2(1+x)$, $3x^2=-3(1+x)+3(1+x+x^2)$, also $\tilde{\mathcal L}=\begin{pmatrix}0&1&-2&0\\0&0&2&-3\\0&0&0&3\end{pmatrix}$. Jetzt ist $\tilde{\mathcal L}\,p_{\mathcal B}=(-2,-9,9)$, und $-2-9(1+x)+9(1+x+x^2)=-2+9x^2$ ist dieselbe Ableitung. Die Einträge ändern sich, der Rang 3 bleibt.
:::
:::
