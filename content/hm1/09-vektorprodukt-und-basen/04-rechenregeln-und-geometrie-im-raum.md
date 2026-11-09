---
title: Stufe 2: Rechenregeln und Geometrie im Raum
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektorprodukt und Basen
order: 1290400
summary: Teil 8 setzt in der Hesseschen Normalform den Normalenvektor voraus.
tags: Normalenvektor, Graßmannsche Entwicklungssatz, Jacobi-Identität, Schnittgerade
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
[Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) setzt in der Hesseschen Normalform den Normalenvektor voraus. Ist die Ebene durch zwei Richtungen gegeben, liefert ihn das Vektorprodukt. Dieselbe Idee gibt die Richtung der Schnittgeraden zweier Ebenen.
:::

**Die Idee.** Beide Aufgaben suchen einen Vektor senkrecht zu zwei bekannten Richtungen. Der __Normalenvektor__ einer Ebene steht senkrecht auf den beiden Richtungen, die sie aufspannen. Die Schnittgerade liegt in beiden Ebenen, ihre Richtung steht also senkrecht auf beiden Normalenvektoren. Vorher braucht man die Rechenregeln.

:::satz Satz 2.1 (Rechenregeln)
<span class="anker" id="satz-2-1"></span>

Für $\vec u,\vec v\in\mathbb{R}^3$ gilt:

<ol class="rm">

<li>

$\vec u$ und $\vec v$ sind linear abhängig $\iff\vec u\times\vec v=\vec0$. Gleichbedeutend: linear unabhängig $\iff\vec u\times\vec v\ne\vec0$.

</li>

<li>

$\vec u\times\vec v=-(\vec v\times\vec u)$.

</li>

</ol>
:::

⁠**So liest man das:** (ii) sagt, dass die Reihenfolge zählt: Vertauschen dreht den Pfeil um, passend zur rechten Hand. (i) ist ein Test auf Unabhängigkeit. Im Modell ist $\vec u\times\vec v\ne\vec0$, also sind $\vec u,\vec v$ unabhängig.

:::beweis Komponenten vergleichen
(ii): Vertauschen von $\vec u$ und $\vec v$ in [(1.1)](das-vektorprodukt.html#gl-1-1) kehrt jede Komponente um.

(i) „$\Rightarrow$“: Bei Abhängigkeit gibt es nach [Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) ein $\lambda$ mit $\vec u=\lambda\vec v$ oder ein $\mu$ mit $\vec v=\mu\vec u$. Im ersten Fall ist die erste Komponente $\lambda v_2v_3-\lambda v_3v_2=0$, die anderen ebenso. Der zweite Fall folgt mit (ii).

„$\Leftarrow$“: Sei $\vec u\times\vec v=\vec0$. Für $\vec v=\vec0$ sind die Vektoren abhängig. Sei also $\vec v\ne\vec0$, zum Beispiel $v_3\ne0$ (die anderen Fälle gehen gleich). Die erste Komponente gibt $u_2=\frac{u_3}{v_3}v_2$, die zweite $u_1=\frac{u_3}{v_3}v_1$, und $u_3=\frac{u_3}{v_3}v_3$ gilt immer. Mit $\lambda:=u_3/v_3$ ist $\vec u=\lambda\vec v$.
:::

:::satz Satz 2.2 (Weitere Rechenregeln)
<span class="anker" id="satz-2-2"></span>

Für alle $\vec u,\vec v,\vec w\in\mathbb{R}^3$ gelten der __Graßmannsche Entwicklungssatz__ und die __Jacobi-Identität__:

<span class="anker" id="gl-2-1"></span>
<span class="anker" id="gl-2-2"></span>
$$\begin{aligned} \vec u\times(\vec v\times\vec w)&=\langle\vec u,\vec w\rangle\,\vec v-\langle\vec u,\vec v\rangle\,\vec w,\\ \vec u\times(\vec v\times\vec w)+\vec v\times(\vec w\times\vec u)+\vec w\times(\vec u\times\vec v)&=\vec0. \end{aligned} \tag{2.1|2.2}$$
:::

⁠**So liest man das:** In [(2.2)](#gl-2-2) werden die Argumente zyklisch vertauscht. Klammern dürfen nicht weggelassen werden: Es gilt $\vec e_1\times(\vec e_1\times\vec e_2)=-\vec e_2$, aber $(\vec e_1\times\vec e_1)\times\vec e_2=\vec0$. **Beweisidee:** Beide Seiten von [(2.1)](#gl-2-1) sind in jedem Eingang linear, also reicht es, Einheitsvektoren einzusetzen. Die Probe $\langle\vec z,\vec u\rangle=0$ für die rechte Seite $\vec z$ passt: $\langle\vec u,\vec w\rangle\langle\vec v,\vec u\rangle-\langle\vec u,\vec v\rangle\langle\vec w,\vec u\rangle=0$. [(2.2)](#gl-2-2) folgt aus [(2.1)](#gl-2-1): Dreimal eingesetzt, heben sich die sechs Summanden paarweise auf.

**Lorentz-Kraft.** Auf einen geraden Leiter der Länge $\ell$ im Magnetfeld $\vec B$ wirkt beim Strom $\vec I$ die Kraft $\vec F=\ell\,\vec I\times\vec B$, quer zu Strom und Feld (Daumen, Zeigefinger, Mittelfinger).

**Ebene: von der Parameterform zum Normalenvektor.** Gegeben ist $E=\{\vec w+\alpha_1\vec v_1+\alpha_2\vec v_2:\alpha_1,\alpha_2\in\mathbb{R}\}$ mit linear unabhängigen $\vec v_1,\vec v_2$. Gesucht ist die Hessesche Normalform $E=\{\vec u\in\mathbb{R}^3:\langle\vec u,\vec n\rangle=\beta\}$ mit $\|\vec n\|=1$, $\beta\ge0$. Nach (E2) und Satz [2.1](#satz-2-1) (i) ist

<span class="anker" id="gl-2-3"></span>
$$\vec n=\pm\frac{\vec v_1\times\vec v_2}{\|\vec v_1\times\vec v_2\|},\qquad\beta:=\langle\vec w,\vec n\rangle\ge0, \tag{2.3}$$

und das Vorzeichen wird so gewählt, dass $\beta\ge0$ ist.

::::beispiel
$\vec w=(3,0,0)$, $\vec v_1=(1,0,-1)$, $\vec v_2=(-1,2,0)$ geben $\vec v_1\times\vec v_2=(2,1,2)$ mit Länge 3, also $\vec n=\frac13(2,1,2)$ und $\beta=2$. Das ist die Ebene $H$ aus [Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html).
::::

⁠**Grenzfall:** Für $\vec v_2=-2\vec v_1$ ist der Nenner 0, die Menge ist nur eine Gerade.

**Gerade als Schnitt zweier Ebenen.** Gegeben sind $E_j=\{\vec u:\langle\vec u,\vec n^{(j)}\rangle=\beta_j\}$, $j=1,2$, in Hessescher Normalform mit linear unabhängigen $\vec n^{(1)},\vec n^{(2)}$. Gesucht ist die __Schnittgerade__ $G=\{\vec w+\alpha\vec v:\alpha\in\mathbb{R}\}=E_1\cap E_2$ (Abb. [2](#abb-2)). Die Richtung muss senkrecht auf beiden Normalenvektoren stehen, also setzt man $\vec v:=\vec n^{(1)}\times\vec n^{(2)}$. Für den Aufpunkt macht man den Ansatz $\vec w=\gamma_1\vec n^{(1)}+\gamma_2\vec n^{(2)}$, den Punkt von $G$ in der Ebene der beiden Normalen. Einsetzen in die beiden Ebenengleichungen gibt mit $c:=\langle\vec n^{(1)},\vec n^{(2)}\rangle$ wegen $\|\vec n^{(j)}\|=1$

<span class="anker" id="gl-2-4"></span>
$$\gamma_1+c\,\gamma_2=\beta_1,\qquad c\,\gamma_1+\gamma_2=\beta_2,\qquad\text{also}\quad\gamma_1=\frac{\beta_1-c\beta_2}{1-c^2},\quad\gamma_2=\frac{\beta_2-c\beta_1}{1-c^2}. \tag{2.4}$$

Der Nenner ist nach [(1.2)](das-vektorprodukt.html#gl-1-2) gleich $\|\vec v\|^2\ne0$. $G$ ist der ganze Schnitt: Für $\vec x\in E_1\cap E_2$ steht $\vec x-\vec w$ senkrecht auf beiden Normalen, liegt also nach Satz [4.6](orthonormalsysteme-und-projektion.html#satz-4-6) in $\operatorname{span}\{\vec v\}$.

::::beispiel
$H$ mit $\beta_1=2$ und die waagerechte Ebene $x_3=1$, also $\vec n^{(2)}=\vec e_3$, $\beta_2=1$. Dann ist $c=\frac23$, $\gamma_1=\frac{12}5$, $\gamma_2=-\frac35$ und $\vec w=(\frac85,\frac45,1)$, $\vec v=\frac13(1,-2,0)$.
::::

⁠**Grenzfall:** Parallele Ebenen haben abhängige Normalen, $\vec v=\vec0$: Es gibt keine Schnittrichtung.

:::abbildung hm1/k9ebenen 2
Die Ebenen $H$ (schräg) und $x_3=1$ (waagerecht) schneiden sich in der Geraden $G$. Die Richtung $\vec v=\vec n^{(1)}\times\vec n^{(2)}$ steht senkrecht auf beiden Normalenvektoren.
:::

**Dreiecksfläche.** Das Dreieck $A=(1,0,1)$, $B=(3,1,1)$, $C=(1,1,3)$ hat die Kantenvektoren $\overrightarrow{AB}=\vec u$, $\overrightarrow{AC}=\vec v$ des Modells. Es ist das halbe Parallelogramm, also ist seine Fläche $\frac12\|\vec u\times\vec v\|=\sqrt6=2{,}449$.

:::frage Warum steht in [(2.3)](#gl-2-3) ein $\pm$?
Eine Ebene hat zwei Seiten, also zwei Einheitsnormalen. Das Vektorprodukt wählt nach der rechten Hand eine davon, Tauschen von $\vec v_1,\vec v_2$ wählt die andere. Die Forderung $\beta\ge0$ entscheidet: $\vec n$ zeigt vom Ursprung zur Ebene.
:::

:::aufgabe Aufgabe 2 ★★ Ebene aus drei Punkten
<span class="anker" id="aufg-2"></span>

Eine Ebene geht durch $A=(3,0,0)$, $B=(0,-6,0)$, $C=(0,0,3)$. (a) Bestimme $\overrightarrow{AB}\times\overrightarrow{AC}$ und die Fläche des Dreiecks. (b) Bestimme die Hessesche Normalform. Welches Vorzeichen gilt in [(2.3)](#gl-2-3)? (c) Wie weit ist die Ebene vom Ursprung entfernt?

:::loesung
(a) $\overrightarrow{AB}=(-3,-6,0)$, $\overrightarrow{AC}=(-3,0,3)$, Produkt $(-18,9,-18)$ mit Länge 27. Die Dreiecksfläche ist $13{,}5$. (b) $\frac{(-18,9,-18)}{27}=-\frac13(2,-1,2)$. Mit diesem Vorzeichen wäre $\langle\vec w,\vec n\rangle=-2<0$. Also gilt in [(2.3)](#gl-2-3) das Minuszeichen: $\vec n=\frac13(2,-1,2)$, $\beta=\langle(3,0,0),\vec n\rangle=2$. Die Ebene ist $2x_1-x_2+2x_3=6$. Probe mit $B$ und $C$: $6$ und $6$. (c) Der Abstand ist $\beta=2$.
:::
:::

:::aufgabe Aufgabe 3 ★★ Schnittgerade und Graßmann
<span class="anker" id="aufg-3"></span>

(a) Bestimme die Schnittgerade von $x_1+2x_2+2x_3=6$ und $x_1=1$ nach [(2.4)](#gl-2-4). (b) Prüfe [(2.1)](#gl-2-1) für $\vec p=(1,1,0)$, $\vec q=(0,1,1)$, $\vec r=(1,0,1)$ und vergleiche mit $(\vec p\times\vec q)\times\vec r$.

:::loesung
(a) $\vec n^{(1)}=\frac13(1,2,2)$, $\beta_1=2$, $\vec n^{(2)}=\vec e_1$, $\beta_2=1$, $c=\frac13$, $1-c^2=\frac89$. Das gibt $\gamma_1=\frac{15}8$, $\gamma_2=\frac38$, $\vec w=(1,\frac54,\frac54)$ und $\vec v=\frac13(1,2,2)\times\vec e_1=\frac23(0,1,-1)$. Also $G=\{(1,\frac54,\frac54)+\alpha(0,1,-1)\}$. Probe: $x_1=1$ und $1+2(\frac54+\alpha)+2(\frac54-\alpha)=6$. (b) $\vec q\times\vec r=(1,1,-1)$, $\vec p\times(\vec q\times\vec r)=(-1,1,0)$. Rechte Seite: $\langle\vec p,\vec r\rangle\vec q-\langle\vec p,\vec q\rangle\vec r=\vec q-\vec r=(-1,1,0)$. Dagegen ist $(\vec p\times\vec q)\times\vec r=(1,-1,1)\times(1,0,1)=(-1,0,1)$, also ein anderer Vektor.
:::
:::
