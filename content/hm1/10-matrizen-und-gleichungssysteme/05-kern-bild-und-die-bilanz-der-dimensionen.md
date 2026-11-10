---
title: Stufe 3: Kern, Bild und die Bilanz der Dimensionen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
adresse: elektrotechnik/1-semester/hohere-mathematik-1/matrizen-und-lineare-gleichungssysteme
knoten: Kapitel 10: Matrizen und lineare Gleichungssysteme
order: 1300500
summary: Die Presse P schickt verschiedene Vektoren auf dasselbe Ziel.
tags: Bild, Urbild, Kern
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die Presse $P$ schickt verschiedene Vektoren auf dasselbe Ziel. Diese Stufe misst, wie viel dabei verloren geht, und zeigt: Verlust und Ertrag ergeben zusammen immer die Dimension des Startraums.
:::

**Die Idee.** $P$ hat die Spalten $(1,2)$ und $(2,4)$. Beide liegen auf derselben Geraden, also landet jedes $Px$ auf dieser Geraden. Die Ebene wird flachgedrückt, und zwar längs der Richtung $(-2,1)$, denn $P\cdot(-2,1)=0$. Jede Parallele zu dieser Richtung fällt auf einen einzigen Punkt (Abb. [3](#abb-3)): $P(1,1)=P(3,0)=P(-1,2)=(3,6)$. Eine Dimension geht als Richtung verloren, eine bleibt als Bild. Was im Kern verschwindet, fehlt im Bild.

:::abbildung hm1/k10kern 3
Die Presse $P$. Links die rote Gerade, die auf 0 geht (der Kern), und zwei Parallelen. Jede Parallele fällt auf einen Punkt der Bildgeraden rechts: Die drei blauen Punkte gehen alle auf $(3,6)$.
:::

:::satz Satz 3.1 (Bilder und Urbilder von Unterräumen)
<span class="anker" id="satz-3-1"></span>

Sei $L:V\to W$ linear.

<ol class="al">

<li>

Ist $U\subset V$ ein Unterraum, so ist das __Bild__ $L(U):=\{Lu:u\in U\}$ ein Unterraum von $W$.

</li>

<li>

Ist $Z\subset W$ ein Unterraum, so ist das __Urbild__ $L^{-1}(Z):=\{v\in V:Lv\in Z\}$ ein Unterraum von $V$.

</li>

</ol>
:::

:::beweis Bilder und Urbilder
Geprüft werden die drei Eigenschaften eines Unterraums. Ein Schritt erledigt (U2) und (U3) zugleich, wenn man $\alpha_1x_1+\alpha_2x_2$ betrachtet.

(a) Wegen $0_V\in U$ ist $0_W=L(0_V)\in L(U)$. Sind $Lu_1,Lu_2\in L(U)$, so ist $\alpha_1Lu_1+\alpha_2Lu_2=L(\alpha_1u_1+\alpha_2u_2)$ nach (L1), (L2), und $\alpha_1u_1+\alpha_2u_2\in U$. Das Ergebnis liegt also in $L(U)$.

(b) Wegen $L(0_V)=0_W\in Z$ ist $0_V\in L^{-1}(Z)$. Sind $v_1,v_2\in L^{-1}(Z)$, so ist $L(\alpha_1v_1+\alpha_2v_2)=\alpha_1Lv_1+\alpha_2Lv_2\in Z$, weil $Z$ ein Unterraum ist.
:::

⁠**So liest man das:** Die Schreibweise $L^{-1}(Z)$ ist eine Menge und setzt nicht voraus, dass $L$ umkehrbar ist. Beispiel: Für $P$ und $Z=\{0\}$ ist das Urbild die rote Gerade.

:::definition Definition 3.2 (Kern und Bild)
<span class="anker" id="satz-3-2"></span>

Für $L:V\to W$ linear heißt $\ker L:=L^{-1}(\{0_W\})=\{v\in V:Lv=0_W\}$ der __Kern__ von $L$ (englisch *kernel*) und $\operatorname{im}L:=L(V)=\{Lv:v\in V\}\subset W$ das __Bild__ von $L$ (englisch *image*).
:::

⁠**So liest man das:** Nach Satz [3.1](#satz-3-1) sind $\ker L\subset V$ und $\operatorname{im}L\subset W$ Unterräume, insbesondere $0_V\in\ker L$ und $0_W\in\operatorname{im}L$. Für eine Matrix ist $\operatorname{im}A$ der Aufspann der Spalten, das zeigt [(2.1)](die-spalten-sind-die-bilder.html#gl-2-1). Für $P$: $\ker P=\operatorname{span}\{(-2,1)\}$, $\operatorname{im}P=\operatorname{span}\{(1,2)\}$.

:::satz Satz 3.3 (Injektiv und surjektiv)
<span class="anker" id="satz-3-3"></span>

Für $L:V\to W$ linear gilt: (a) $L$ injektiv $\iff\ker L=\{0_V\}$; (b) $L$ surjektiv $\iff\operatorname{im}L=W$.
:::

:::beweis Injektiv und surjektiv
(b) ist die Definition von surjektiv. (a): Nach Satz [1.2](lineare-abbildungen.html#satz-1-2) (a) gilt $Lv=L\tilde v\iff L(v-\tilde v)=0_W\iff v-\tilde v\in\ker L$. Ist $\ker L=\{0_V\}$, folgt daraus $v=\tilde v$. Ist umgekehrt $L$ injektiv und $Lu=0_W=L0_V$, folgt $u=0_V$.
:::

⁠**So liest man das:** Bei allgemeinen Funktionen muss man alle Paare $v,\tilde v$ prüfen. Bei linearen genügt der eine Punkt 0, weil zwei Vektoren genau dann dasselbe Bild haben, wenn ihre Differenz im Kern liegt.

:::satz Satz 3.4 (Dimensionssatz)
<span class="anker" id="satz-3-4"></span>

Sei $V$ endlichdimensional und $L:V\to W$ linear. Dann gilt

<span class="anker" id="gl-3-1"></span>
$$\dim V=\dim(\ker L)+\dim(\operatorname{im}L). \tag{3.1}$$
:::

:::beweis Dimensionssatz
Wähle eine Basis $u_1,\dots,u_k$ von $\ker L$ und ergänze sie durch $v_1,\dots,v_r$ zu einer Basis von $V$ (Basisergänzung). Dann ist $\dim V=k+r$. Es bleibt zu zeigen, dass $Lv_1,\dots,Lv_r$ eine Basis von $\operatorname{im}L$ sind.

⁠*Sie spannen auf:* Jedes $v\in V$ ist $\sum_i\alpha_iu_i+\sum_j\beta_jv_j$. Wegen $Lu_i=0$ ist $Lv=\sum_j\beta_jLv_j$.

⁠*Sie sind unabhängig:* Aus $\sum_j\beta_jLv_j=0$ folgt $L(\sum_j\beta_jv_j)=0$, also $\sum_j\beta_jv_j\in\ker L$. Damit ist $\sum_j\beta_jv_j=\sum_i\gamma_iu_i$. Das ist eine Nullkombination der Basis von $V$, also sind alle $\beta_j$ und $\gamma_i$ gleich null.
:::

⁠**So liest man das:** Die Gleichung ist eine Bilanz. Jede Richtung einer passend gewählten Basis von $V$ tut genau eines: Entweder verschwindet sie ($u_i$), oder sie liefert eine neue Richtung im Bild ($v_j$). Es gibt keinen dritten Ausgang. Für $P$: $2=1+1$. Für die flache Matrix $Q$: Der Kern ist $\operatorname{span}\{(-2,1,0)\}$, das Bild $\operatorname{span}\{(1,2,3),(1,3,4)\}$, also $3=1+2$. **Grenzfälle:** Für die Nullabbildung ist $\ker L=V$ und $\operatorname{im}L=\{0\}$. Für $\operatorname{Id}$ ist es umgekehrt. Aus [(3.1)](#gl-3-1) folgt $\dim(\operatorname{im}L)\le\dim V$: Eine lineare Abbildung kann keine Dimension erzeugen.

:::analogie
Das Bild ist der Schatten eines Körpers auf einer Wand, der Kern die Richtung des Lichts. Punkte auf einem gemeinsamen Lichtstrahl fallen auf denselben Schattenpunkt. Wie viele Dimensionen der Strahl schluckt, so viele fehlen dem Schatten. Das Bild stimmt nur für Projektionen: Eine lineare Abbildung kann zusätzlich drehen und strecken, und ihr Bild muss nicht in $V$ liegen.
:::

:::satz Satz 3.5 (Folgerungen aus dem Dimensionssatz)
<span class="anker" id="satz-3-5"></span>

Seien $V,W$ endlichdimensional und $L:V\to W$ linear. Dann gilt:

<ol class="al">

<li>

$L$ injektiv $\iff\dim V=\dim(\operatorname{im}L)\le\dim W$;

</li>

<li>

$L$ surjektiv $\iff\dim V=\dim(\ker L)+\dim W$;

</li>

<li>

$L$ bijektiv $\iff\bigl(\dim V=\dim W$ und $\ker L=\{0_V\}\bigr)$.

</li>

</ol>
:::

:::beweis Folgerungen
(a) Nach Satz [3.3](#satz-3-3) ist $L$ genau dann injektiv, wenn $\dim\ker L=0$ ist. Nach [(3.1)](#gl-3-1) heißt das $\dim V=\dim(\operatorname{im}L)$. Die Schranke $\dim W$ gilt, weil $\operatorname{im}L\subset W$ ein Unterraum ist.

(b) $L$ surjektiv $\iff\operatorname{im}L=W\iff\dim(\operatorname{im}L)=\dim W$, denn ein Unterraum voller Dimension ist $W$ selbst (eine Basis von ihm hat $\dim W$ unabhängige Vektoren, ein weiterer unabhängiger Vektor aus $W$ wäre einer zu viel). Einsetzen in [(3.1)](#gl-3-1) gibt die Behauptung.

(c) Bijektiv heißt injektiv und surjektiv, also $\ker L=\{0_V\}$ nach (a) und $\dim V=0+\dim W$ nach (b). Umgekehrt folgen aus den beiden Bedingungen (a) und (b).
:::

⁠**So liest man das:** Gilt $\dim V>\dim W$, kann $L$ nie injektiv sein, und bei $\dim V<\dim W$ nie surjektiv. Bei $\dim V=\dim W$ sind injektiv, surjektiv und bijektiv dasselbe. **Warum endlich nötig ist:** Auf dem Raum aller Polynome ist $p(x)\mapsto x\,p(x)$ injektiv, aber nicht surjektiv, denn das Polynom 1 wird nie getroffen.

:::frage Ist $V$ also aus Kern und Bild zusammengesetzt?
Nein. [(3.1)](#gl-3-1) ist eine Gleichung zwischen Zahlen, nicht zwischen Mengen. Der Kern liegt in $V$, das Bild in $W$. Selbst für $V=W$ passen sie nicht immer zusammen: Bei der Matrix $N$ aus Stufe [5](hintereinanderausfuhren-ist-multiplizieren.html#stufe-5) sind Kern und Bild dieselbe Gerade.
:::

:::aufgabe Aufgabe 3 ★★ Kern und Bild bestimmen
<span class="anker" id="aufg-3"></span>

Bestimme Kern und Bild, prüfe [(3.1)](#gl-3-1) und entscheide, ob die Abbildung injektiv oder surjektiv ist: (a) $K_1=\begin{pmatrix}1&-1&2\\2&-2&4\end{pmatrix}$; (b) $K_2=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}$.

:::loesung
(a) Die zweite Zeile ist das Doppelte der ersten, also bleibt $x_1-x_2+2x_3=0$. Damit ist $\ker K_1=\operatorname{span}\{(1,1,0),(-2,0,1)\}$. Alle Spalten sind Vielfache von $(1,2)$, also $\operatorname{im}K_1=\operatorname{span}\{(1,2)\}$. Bilanz: $3=2+1$. Weder injektiv noch surjektiv. (b) $K_2x=(x_1,x_2,x_1+x_2)=0$ erzwingt $x=0$, also $\ker K_2=\{0\}$. $\operatorname{im}K_2=\operatorname{span}\{(1,0,1),(0,1,1)\}=\{y:y_3=y_1+y_2\}$. Bilanz: $2=0+2$. Injektiv, nicht surjektiv: $(0,0,1)$ wird nicht getroffen.
:::
:::

:::aufgabe Aufgabe 4 ★★ Vorhersagen ohne Rechnen
<span class="anker" id="aufg-4"></span>

Sei $L$ linear. Was lässt sich sagen? (a) $L:\mathbb{R}^5\to\mathbb{R}^3$: Wie groß ist $\dim\ker L$ mindestens? (b) $L:\mathbb{R}^3\to\mathbb{R}^5$: Kann $L$ surjektiv sein? (c) $L:\mathbb{R}^4\to\mathbb{R}^4$ ist injektiv: Ist $L$ surjektiv? (d) $L:\mathbb{R}^7\to\mathbb{R}^4$ mit $\dim\ker L=3$: Ist $L$ surjektiv?

:::loesung
(a) $\dim\ker L=5-\dim\operatorname{im}L\ge5-3=2$. (b) Nein: $\dim\operatorname{im}L\le3<5$. (c) Ja: $\ker L=\{0\}$ gibt $\dim\operatorname{im}L=4$, und das ist ganz $\mathbb{R}^4$. (d) Ja: $\dim\operatorname{im}L=7-3=4=\dim\mathbb{R}^4$.
:::
:::
