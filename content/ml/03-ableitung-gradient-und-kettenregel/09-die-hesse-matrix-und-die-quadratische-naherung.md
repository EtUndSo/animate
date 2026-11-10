---
title: Die Hesse-Matrix und die quadratische Näherung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Kapitel 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15230900
summary: Der Gradient beschreibt die Neigung des Geländes, aber nicht seine Wölbung.
tags: zweiten partiellen Ableitungen, Hesse-Matrix, gemischte Differenz, zweite Richtungsableitung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Der Gradient beschreibt die Neigung des Geländes, aber nicht seine Wölbung. Die zweiten partiellen Ableitungen sammelt die Hesse-Matrix. Sie ist symmetrisch, und mit ihr wird die lineare Näherung zur quadratischen. Ihre Eigenwerte sagen, wie stark sich das Gelände in verschiedene Richtungen krümmt, und verbinden diesen Abschnitt mit den quadratischen Formen aus [Kapitel 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html).
:::

### Zweite partielle Ableitungen

<span class="anker" id="stufe-8-1"></span>

Die partiellen Ableitungen $\partial_jf$ sind selbst wieder Funktionen von $\mathbf{x}$. Man kann sie noch einmal partiell ableiten, nach derselben oder nach einer anderen Variablen. Das beschreibt, wie sich die Steigung in Richtung $x_j$ ändert, wenn man in Richtung $x_i$ weitergeht.

:::definition Definition 8.1 (Zweite partielle Ableitungen)
<span class="anker" id="satz-8-1"></span>

Die __zweiten partiellen Ableitungen__ von $f:\mathbb{R}^d\to\mathbb{R}$ sind

<span class="anker" id="gl-8-1"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial}{\partial x_i}\Bigl(\frac{\partial f}{\partial x_j}\Bigr), \tag{8.1}$$

erst nach $x_j$, dann nach $x_i$ abgeleitet. Für $i=j$ schreibt man $\partial^2f/\partial x_i^2$. Für $i\ne j$ heißen sie gemischte Ableitungen.
:::

::::beispiel [Rechenbeispiel]
Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ ist $\partial_1f=2x_1x_2$ und $\partial_2f=x_1^2+2x_2$, also

$$\begin{gathered} \frac{\partial^2f}{\partial x_1^2}=\frac{\partial}{\partial x_1}(2x_1x_2)=2x_2,\qquad \frac{\partial^2f}{\partial x_2\,\partial x_1}=\frac{\partial}{\partial x_2}(2x_1x_2)=2x_1,\\ \frac{\partial^2f}{\partial x_1\,\partial x_2}=\frac{\partial}{\partial x_1}(x_1^2+2x_2)=2x_1,\qquad \frac{\partial^2f}{\partial x_2^2}=\frac{\partial}{\partial x_2}(x_1^2+2x_2)=2 . \end{gathered}$$

An der Stelle $(1,\,2)$ sind das $4$, $2$, $2$ und $2$. Die beiden gemischten Ableitungen sind gleich, obwohl sie auf verschiedenen Wegen entstanden sind.
::::

⁠**Kurz gesagt:** Zweite partielle Ableitungen leiten eine partielle Ableitung noch einmal partiell ab; die gemischten beschreiben, wie sich die Steigung in einer Richtung beim Gehen in eine andere Richtung ändert.

### Die Hesse-Matrix

<span class="anker" id="stufe-8-2"></span>

Eine Funktion von $d$ Variablen hat $d^2$ zweite partielle Ableitungen. Wie die ersten Ableitungen im Gradienten fasst man sie in einem Objekt zusammen, hier in einer quadratischen Matrix.

:::definition Definition 8.2 (Hesse-Matrix)
<span class="anker" id="satz-8-2"></span>

Die $d\times d$-Matrix

<span class="anker" id="gl-8-2"></span>
$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\cdots&\dfrac{\partial^2f}{\partial x_1\,\partial x_d}\\ \vdots&&\vdots\\ \dfrac{\partial^2f}{\partial x_d\,\partial x_1}&\cdots&\dfrac{\partial^2f}{\partial x_d^2}\end{pmatrix},\qquad \bigl(\mathbf{H}_f(\mathbf{x})\bigr)_{ij}=\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}), \tag{8.2}$$

heißt die __Hesse-Matrix__ von $f$ an der Stelle $\mathbf{x}$.
:::

Die Matrix ist nach dem Mathematiker Otto Hesse benannt; manche Bücher schreiben $\nabla^2f$. Ihre Spalte $j$ ist der Gradient der Funktion $\partial_jf$. Sie ist damit eng mit der Jacobi-Matrix des Gradienten verwandt, der vektorwertigen Funktion $\mathbf{x}\mapsto\nabla f(\mathbf{x})$: Deren Eintrag $(i,j)$ ist $\partial(\partial_if)/\partial x_j$, die Ableitung in der anderen Reihenfolge. Der nächste Unterabschnitt zeigt, dass beide Reihenfolgen fast immer dasselbe ergeben; dann ist die Hesse-Matrix die Jacobi-Matrix des Gradienten.

::::beispiel [Rechenbeispiel]
Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ ist nach dem vorigen Unterabschnitt

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}2x_2&2x_1\\2x_1&2\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}4&2\\2&2\end{pmatrix}.$$

Für eine quadratische Funktion $f(\mathbf{x})=\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ mit symmetrischem $\mathbf{A}$ ist nach Abschnitt [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) $\nabla f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ und damit $\mathbf{H}_f=\mathbf{A}$ an jeder Stelle. Für die Schüssel $x_1^2+4x_2^2$ aus Abschnitt [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) ist $\mathbf{A}=\operatorname{diag}(2;\,8)$.
::::

⁠**Kurz gesagt:** Die Hesse-Matrix sammelt alle zweiten partiellen Ableitungen; bei einer quadratischen Funktion $\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ ist sie überall $\mathbf{A}$.

### Der Satz von Schwarz

<span class="anker" id="stufe-8-3"></span>

Im Rechenbeispiel waren die beiden gemischten Ableitungen gleich. Das ist kein Zufall, sondern gilt für alle Funktionen, deren zweite Ableitungen keine Sprünge haben.

:::satz Satz 8.3 (Satz von Schwarz)
<span class="anker" id="satz-8-3"></span>

Existieren alle zweiten partiellen Ableitungen von $f$ in der Nähe von $\mathbf{x}$ und sind sie an der Stelle $\mathbf{x}$ stetig, so gilt dort

<span class="anker" id="gl-8-3"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial^2f}{\partial x_j\,\partial x_i} \tag{8.3}$$

für alle $i,j$. Die Hesse-Matrix ist dann symmetrisch.
:::

Den Grund sieht man an einer Rechnung, in der die Reihenfolge gar nicht vorkommt. Man verschiebt sich von $\mathbf{x}$ um $h$ in Richtung $x_1$ und um $k$ in Richtung $x_2$ und bildet die __gemischte Differenz__

$$\Delta(h,k)=f(x_1+h,\,x_2+k)-f(x_1+h,\,x_2)-f(x_1,\,x_2+k)+f(x_1,\,x_2).$$

Fasst man den ersten mit dem dritten und den zweiten mit dem vierten Summanden zusammen, so ist $\Delta$ die Änderung der Differenz $f(x_1+h,\cdot)-f(x_1,\cdot)$ beim Schritt $k$ in Richtung $x_2$: Wie ändert sich der Anstieg in Richtung $x_1$, wenn man in Richtung $x_2$ geht? Teilt man durch $hk$, so nähert sich das für kleine $h$ und $k$ der Ableitung erst nach $x_1$, dann nach $x_2$. Fasst man stattdessen die ersten beiden und die letzten beiden Summanden zusammen, liest man dieselbe Zahl als Änderung des Anstiegs in Richtung $x_2$ beim Schritt in Richtung $x_1$, und der Quotient nähert sich der Ableitung in der anderen Reihenfolge. Beide Grenzwerte gehören zu derselben Zahl $\Delta/(hk)$. Die Stetigkeit sorgt dafür, dass es auf die Reihenfolge der beiden Grenzübergänge nicht ankommt.

::::beispiel [Rechenbeispiel]
Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ mit $h=k=0{,}1$ ist

$$\Delta=f(1{,}1;\ 2{,}1)-f(1{,}1;\ 2)-f(1;\ 2{,}1)+f(1,2)=6{,}951-6{,}42-6{,}51+6=0{,}021,$$

also $\Delta/(hk)=2{,}1$, nahe bei der gemischten Ableitung $2x_1=2$. Die Abweichung kommt daher, dass $2x_1$ zwischen $x_1=1$ und $x_1=1{,}1$ nicht konstant ist.
::::

⁠**Kurz gesagt:** Bei stetigen zweiten Ableitungen ist die Reihenfolge des Ableitens gleichgültig, und die Hesse-Matrix ist symmetrisch.

:::hintergrund Wenn die zweiten Ableitungen nicht stetig sind
Ohne Stetigkeit kann der Satz falsch sein. Das klassische Gegenbeispiel ist $f(x_1,x_2)=x_1x_2\,\frac{x_1^2-x_2^2}{x_1^2+x_2^2}$ mit $f(0,0)=0$. Rechnet man die ersten partiellen Ableitungen auf den Achsen aus, so ergibt sich $\partial_1f(0,x_2)=-x_2$ und $\partial_2f(x_1,0)=x_1$. Leitet man die erste nach $x_2$ ab, erhält man im Nullpunkt $-1$; leitet man die zweite nach $x_1$ ab, erhält man $+1$. Die gemischten Ableitungen im Nullpunkt sind also verschieden, weil die zweiten Ableitungen dort springen. Bei den Funktionen dieses Kapitels ohne Knick tritt das nicht auf; sie sind aus Polynomen, e-Funktionen und Grundrechenarten gebaut und haben überall, wo sie erklärt sind, stetige Ableitungen beliebiger Ordnung.
:::

### Die quadratische Näherung

<span class="anker" id="stufe-8-4"></span>

In einer Variablen wurde die Tangente in Abschnitt [1.5](die-ableitung.html#stufe-1-5) durch eine Parabel verbessert. Bei mehreren Variablen tritt an die Stelle der Tangentialebene eine gewölbte Fläche, deren Wölbung die Hesse-Matrix beschreibt.

:::satz Satz 8.4 (Quadratische Näherung)
<span class="anker" id="satz-8-4"></span>

Hat $f$ in der Nähe von $\mathbf{x}$ stetige zweite partielle Ableitungen, so gilt

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x}+\mathbf{h})=f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{h}+r_2(\mathbf{h})\qquad\text{mit}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{r_2(\mathbf{h})}{\lVert\mathbf{h}\rVert^2}=0 . \tag{8.4}$$
:::

:::herleitung Die quadratische Näherung entlang einer Geraden
Man schränkt $f$ auf die Gerade durch $\mathbf{x}$ in Richtung $\mathbf{h}$ ein: $\phi(t)=f(\mathbf{x}+t\,\mathbf{h})$. Das ist eine Funktion einer Variablen. Nach [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4) ist $\phi'(t)=\nabla f(\mathbf{x}+t\mathbf{h})^{\top}\mathbf{h}=\sum_jh_j\,\partial_jf(\mathbf{x}+t\mathbf{h})$. Jeden Summanden leitet man noch einmal mit [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4) ab, diesmal für die Funktion $\partial_jf$:

$$\phi''(t)=\sum_{j=1}^dh_j\sum_{i=1}^d\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}+t\mathbf{h})\,h_i=\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x}+t\mathbf{h})\,\mathbf{h} .$$

Die quadratische Näherung [(1.6)](die-ableitung.html#gl-1-6) von $\phi$ an der Stelle $0$, ausgewertet bei $t=1$, lautet $\phi(1)\approx\phi(0)+\phi'(0)+\tfrac12\phi''(0)$, und das ist [(8.4)](#gl-8-4). Dass der Fehler schneller als $\lVert\mathbf{h}\rVert^2$ verschwindet, folgt aus der Stetigkeit der zweiten Ableitungen.
:::

Das neue Glied $\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$ ist eine quadratische Form im Sinn von [Kapitel 2, Abschnitt 5.1](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1), mit der Hesse-Matrix als Matrix. Die Funktion sieht in der Nähe von $\mathbf{x}$ also aus wie eine Ebene plus eine quadratische Form.

::::beispiel [Rechenbeispiel]
Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ und $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$ wie in Abschnitt [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4) ist

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(4\cdot0{,}01^2+2\cdot2\cdot0{,}01\cdot0{,}02+2\cdot0{,}02^2\bigr)=\tfrac12\,(0{,}0004+0{,}0008+0{,}0008)=0{,}001$$

(Abb. [15](#abb-15)). Die quadratische Näherung ist $6+0{,}14+0{,}001=6{,}141$, der genaue Wert $6{,}141002$. Der Fehler sank von $0{,}001002$ auf $0{,}000002$. Der Rest ist das Glied dritter Ordnung: In $x_1^2x_2$ steckt der Summand $h_1^2h_2=0{,}0001\cdot0{,}02=0{,}000002$, den keine quadratische Näherung erfasst.

:::abbildung ml/k3rtaylor2 15
Das Krümmungsglied der quadratischen Näherung als Doppelsumme; die beiden gemischten Summanden $h_1\cdot2\cdot h_2$ und $h_2\cdot2\cdot h_1$ sind zum mittleren Glied zusammengefasst.
:::
::::

⁠**Kurz gesagt:** Nahe bei $\mathbf{x}$ ist $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{h}$: Ebene plus quadratische Form.

### Die Krümmung in einer Richtung

<span class="anker" id="stufe-8-5"></span>

Wie stark ist das Gelände gewölbt, wenn man von $\mathbf{x}$ aus in Richtung $\mathbf{u}$ geht? Die Herleitung des vorigen Unterabschnitts hat die Antwort schon gegeben: Die zweite Ableitung von $\phi(t)=f(\mathbf{x}+t\mathbf{u})$ an der Stelle $0$ ist $\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{u}$.

:::definition Definition 8.5 (Krümmung in einer Richtung)
<span class="anker" id="satz-8-5"></span>

Für einen Vektor $\mathbf{u}$ der Länge $1$ heißt

<span class="anker" id="gl-8-5"></span>
$$\frac{\mathrm{d}^2}{\mathrm{d} t^2}f(\mathbf{x}+t\,\mathbf{u})\Big|_{t=0}=\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u} \tag{8.5}$$

die __zweite Richtungsableitung__ von $f$ an der Stelle $\mathbf{x}$ in Richtung $\mathbf{u}$. Sie misst die Krümmung der Schnittkurve in dieser Richtung.
:::

Mit den Ergebnissen aus [Kapitel 2](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) lässt sich sofort sagen, wie groß diese Krümmung höchstens und mindestens ist. Die Hesse-Matrix ist symmetrisch und hat nach dem Spektralsatz aus [Kapitel 2, Abschnitt 7.6](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-6), reelle Eigenwerte und senkrecht aufeinander stehende Eigenvektoren.

:::satz Satz 8.6 (Krümmung und Eigenwerte)
<span class="anker" id="satz-8-6"></span>

Es seien $\lambda_{\min}$ und $\lambda_{\max}$ der kleinste und der größte Eigenwert der symmetrischen Hesse-Matrix $\mathbf{H}_f(\mathbf{x})$. Dann gilt für jede Richtung $\mathbf{u}$ mit $\lVert\mathbf{u}\rVert=1$

<span class="anker" id="gl-8-6"></span>
$$\lambda_{\min}\le\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u}\le\lambda_{\max}. \tag{8.6}$$

In Richtung eines Eigenvektors ist die Krümmung genau der zugehörige Eigenwert. Ist $\mathbf{H}_f(\mathbf{x})$ positiv definit, so ist die Krümmung in jeder Richtung positiv; ist sie indefinit, so krümmt sich das Gelände in manche Richtungen nach oben und in andere nach unten.
:::

Die Ungleichung ist die Aussage über den größten und kleinsten Wert einer quadratischen Form auf dem Einheitskreis aus [Kapitel 2, Abschnitt 8.5](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-5). Für einen Eigenvektor $\mathbf{u}$ zum Eigenwert $\lambda$ ist $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\lambda\,\mathbf{u}^{\top}\mathbf{u}=\lambda$. Die Begriffe positiv definit und indefinit stammen aus [Kapitel 2, Abschnitt 8](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8); dort war die Form einer quadratischen Form an ihren Eigenwerten abzulesen, als Schüssel, Rinne oder Sattel. Über die quadratische Näherung [(8.4)](#gl-8-4) überträgt sich das auf das Gelände in der Nähe von $\mathbf{x}$: Die Höhenlinien des Krümmungsglieds sind bei positiv definiter Hesse-Matrix Ellipsen, deren Hauptachsen nach [Kapitel 2, Abschnitt 7.7](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-7), in Richtung der Eigenvektoren liegen und in der Richtung starker Krümmung kurz sind.

::::beispiel [Rechenbeispiel 1]
Für die Schüssel $f(\mathbf{x})=x_1^2+4x_2^2$ ist $\mathbf{H}_f=\operatorname{diag}(2;\,8)$ mit den Eigenwerten $2$ und $8$. In Richtung $x_1$ ist die Krümmung $2$, in Richtung $x_2$ ist sie $8$, und in Richtung $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$ ist sie $\tfrac12(2+8)=5$. Das erklärt die gestreckten Höhenlinien aus Abschnitt [4.4](richtungsableitung-und-steilster-anstieg.html#stufe-4-4): In Richtung $x_2$ krümmt sich die Schüssel viermal so stark, ihre Wände sind dort steiler, und die Ellipsen sind in dieser Richtung schmal.
::::

::::beispiel [Rechenbeispiel 2]
Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ ist $\mathbf{H}_f=\bigl(\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\bigr)$. Spur $6$ und Determinante $4$ ergeben nach [Kapitel 2, Abschnitt 6.5](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5), die Eigenwerte $3\pm\sqrt5$, also etwa $5{,}236$ und $0{,}764$. Beide sind positiv, die Hesse-Matrix ist positiv definit: In der Nähe von $(1,\,2)$ krümmt sich das Gelände in jeder Richtung nach oben. In Richtung $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$ ist die Krümmung

$$\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\tfrac12\,(4+2+2+2)=5,$$

und sie liegt zwischen $0{,}764$ und $5{,}236$ (Abb. [16](#abb-16)).

:::abbildung ml/k3rkruemmung 16
Die Krümmung von $f(\mathbf{x})=x_1^2x_2+x_2^2$ an der Stelle $(1,\,2)$ in Richtung der Winkelhalbierenden; der Faktor $\tfrac12$ kommt von $u_iu_j=\tfrac12$.
:::
::::

⁠**Kurz gesagt:** Die Krümmung in Richtung $\mathbf{u}$ ist $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$; sie liegt zwischen dem kleinsten und dem größten Eigenwert der Hesse-Matrix, und deren Vorzeichen entscheiden, ob sich das Gelände wie eine Schüssel oder wie ein Sattel krümmt.

:::hintergrund Hesse-Matrix mal Vektor, ohne die Hesse-Matrix
Bei vielen Variablen ist die Hesse-Matrix riesig: Bei einer Million Variablen hat sie $10^{12}$ Einträge. Oft braucht man aber nur ihr Produkt mit einem Vektor $\mathbf{v}$. Das bekommt man, ohne die Matrix aufzustellen. Die Zahl $\nabla f(\mathbf{x})^{\top}\mathbf{v}=\sum_jv_j\,\partial_jf(\mathbf{x})$ ist eine Funktion von $\mathbf{x}$, und ihr Gradient hat die Komponenten $\sum_jv_j\,\partial^2f/\partial x_i\partial x_j$, also ist $\nabla_{\mathbf{x}}\bigl(\nabla f(\mathbf{x})^{\top}\mathbf{v}\bigr)=\mathbf{H}_f(\mathbf{x})\,\mathbf{v}$. Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ und $\mathbf{v}=(1,\,1)^{\top}$ ist $\nabla f^{\top}\mathbf{v}=2x_1x_2+x_1^2+2x_2$ mit dem Gradienten $(2x_2+2x_1,\ 2x_1+2)^{\top}$, an der Stelle $(1,\,2)$ also $(6,\,4)^{\top}$, und das ist $\mathbf{H}_f\mathbf{v}=(4+2,\ 2+2)^{\top}$. Man berechnet also zwei Gradienten statt einer Matrix mit $d^2$ Einträgen.
:::

:::aufgabe Aufgabe 28 ★ Hesse-Matrizen
<span class="anker" id="aufg-28"></span>

Berechne die Hesse-Matrix an der angegebenen Stelle und prüfe die Symmetrie.

<ol class="al">

<li>

$f(\mathbf{x})=x_1^3+x_1x_2^2$ an der Stelle $(1,\,2)$;

</li>

<li>

$f(\mathbf{x})=\mathrm{e}^{x_1+2x_2}$ an der Stelle $(0,\,0)$. Welchen Rang hat die Matrix?

</li>

<li>

$f(\mathbf{x})=x_1x_2x_3$ an der Stelle $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3x_1^2+x_2^2$ und $\partial_2f=2x_1x_2$, also

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}6x_1&2x_2\\2x_2&2x_1\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}6&4\\4&2\end{pmatrix};$$

die gemischten Ableitungen $\partial_2(3x_1^2+x_2^2)=2x_2$ und $\partial_1(2x_1x_2)=2x_2$ sind gleich.

(b) Mit $f=\mathrm{e}^{x_1+2x_2}$ ist $\partial_1f=f$ und $\partial_2f=2f$, also $\mathbf{H}_f=f\cdot\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ und im Nullpunkt $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$. Die zweite Zeile ist das Doppelte der ersten; der Rang ist $1$, die Eigenwerte sind $5$ und $0$. Das passt: $f$ hängt nur von $x_1+2x_2$ ab und ist entlang der Richtung $(2,\,-1)^{\top}$ konstant, dort also nicht gekrümmt.

(c) $\partial_1f=x_2x_3$, $\partial_2f=x_1x_3$, $\partial_3f=x_1x_2$, also

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}0&x_3&x_2\\x_3&0&x_1\\x_2&x_1&0\end{pmatrix},\qquad \mathbf{H}_f(1,2,3)=\begin{pmatrix}0&3&2\\3&0&1\\2&1&0\end{pmatrix}.$$
:::
:::

:::aufgabe Aufgabe 29 ★★ Quadratische Näherung
<span class="anker" id="aufg-29"></span>

Es sei $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ wie in Aufgabe [10](partielle-ableitungen-und-der-gradient.html#aufg-10).

<ol class="al">

<li>

Berechne $\mathbf{H}_f(2,0)$.

</li>

<li>

Berechne mit der quadratischen Näherung an der Stelle $(2,\,0)$ einen Näherungswert für $f(2{,}1;\ -0{,}05)$ und vergleiche ihn mit der linearen Näherung aus Aufgabe [10](partielle-ableitungen-und-der-gradient.html#aufg-10) und dem genauen Wert.

</li>

</ol>

:::loesung
(a) $\partial_1^2f=0$, $\partial_1\partial_2f=\mathrm{e}^{x_2}$, $\partial_2^2f=x_1\mathrm{e}^{x_2}$, also $\mathbf{H}_f(2,0)=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$.

(b) Mit $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$ ist

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(0+2\cdot1\cdot0{,}1\cdot(-0{,}05)+2\cdot0{,}05^2\bigr)=\tfrac12\,(-0{,}01+0{,}005)=-0{,}0025 .$$

Die quadratische Näherung ist $2+0-0{,}0025=1{,}9975$, die lineare war $2{,}0$, der genaue Wert ist $1{,}997582$. Der Fehler sinkt von $0{,}0024$ auf $0{,}00008$. Das gemischte Glied $-0{,}005$ ist die Wechselwirkung aus Aufgabe [10](partielle-ableitungen-und-der-gradient.html#aufg-10).
:::
:::

:::aufgabe Aufgabe 30 ★★ Krümmungen einer schiefen Schüssel
<span class="anker" id="aufg-30"></span>

Es sei $f(\mathbf{x})=x_1^2+4x_2^2+x_1x_2$.

<ol class="al">

<li>

Schreibe $f$ als $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ und gib $\mathbf{H}$ an.

</li>

<li>

Berechne die Eigenwerte von $\mathbf{H}$ und die Krümmungen in die Richtungen $\mathbf{e}_1$, $\mathbf{e}_2$ und $(1,\,-1)^{\top}/\sqrt2$. Prüfe [(8.6)](#gl-8-6).

</li>

<li>

In welche Richtung ist die Krümmung am größten? Gib einen Eigenvektor an.

</li>

</ol>

:::loesung
(a) $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ mit $\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&8\end{smallmatrix}\bigr)$ ergibt $\tfrac12\,(2x_1^2+2x_1x_2+8x_2^2)=x_1^2+x_1x_2+4x_2^2$. Das ist auch die Hesse-Matrix von $f$.

(b) Spur $10$, Determinante $16-1=15$, also $\lambda^2-10\lambda+15=0$ und $\lambda=5\pm\sqrt{10}$, etwa $8{,}162$ und $1{,}838$. Die Krümmungen sind $\mathbf{e}_1^{\top}\mathbf{H}\mathbf{e}_1=2$, $\mathbf{e}_2^{\top}\mathbf{H}\mathbf{e}_2=8$ und für $\mathbf{u}=(1,\,-1)^{\top}/\sqrt2$: $\tfrac12\,(2-1-1+8)=4$. Alle drei liegen zwischen $1{,}838$ und $8{,}162$.

(c) Am größten ist die Krümmung in Richtung eines Eigenvektors zu $\lambda=5+\sqrt{10}$. Aus der ersten Zeile von $(\mathbf{H}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ folgt $(2-\lambda)v_1+v_2=0$, also $\mathbf{v}=(1;\ 3+\sqrt{10})^{\top}\approx(1;\ 6{,}162)^{\top}$, normiert etwa $(0{,}160;\ 0{,}987)^{\top}$. Das ist fast die $x_2$-Richtung, durch das gemischte Glied $x_1x_2$ ein wenig gedreht.
:::
:::

:::aufgabe Aufgabe 31 ★★★ Verschiedene gemischte Ableitungen
<span class="anker" id="aufg-31"></span>

Es sei $f(x_1,x_2)=x_1x_2\,\dfrac{x_1^2-x_2^2}{x_1^2+x_2^2}$ für $\mathbf{x}\ne\mathbf{0}$ und $f(0,0)=0$.

<ol class="al">

<li>

Zeige mit dem Differenzenquotienten $\partial_1f(0,x_2)=-x_2$ für $x_2\ne0$ und $\partial_1f(0,0)=0$. Berechne ebenso $\partial_2f(x_1,0)$.

</li>

<li>

Folgere, dass die beiden gemischten Ableitungen im Nullpunkt $-1$ und $+1$ sind. Welche Voraussetzung des Satzes von Schwarz ist verletzt?

</li>

</ol>

:::loesung
(a) Auf der Achse $x_1=0$ ist $f=0$. Für $x_2\ne0$ ist

$$\partial_1f(0,x_2)=\lim_{h\to0}\frac{f(h,x_2)-0}{h}=\lim_{h\to0}x_2\,\frac{h^2-x_2^2}{h^2+x_2^2}=x_2\cdot\frac{-x_2^2}{x_2^2}=-x_2 .$$

Im Nullpunkt ist $f(h,0)=0$, also $\partial_1f(0,0)=0$; die Formel $-x_2$ gilt also auch für $x_2=0$. Ebenso ist $\partial_2f(x_1,0)=\lim_k x_1\frac{x_1^2-k^2}{x_1^2+k^2}=x_1$.

(b) Erst nach $x_1$, dann nach $x_2$ abgeleitet: $\frac{\partial}{\partial x_2}(-x_2)=-1$. Erst nach $x_2$, dann nach $x_1$: $\frac{\partial}{\partial x_1}(x_1)=+1$. Die gemischten Ableitungen im Nullpunkt sind verschieden. Verletzt ist die Stetigkeit der zweiten Ableitungen im Nullpunkt: Außerhalb des Nullpunkts ist die gemischte Ableitung auf der $x_2$-Achse überall $-1$ und auf der $x_1$-Achse überall $+1$. Sie springt also im Nullpunkt, und die beiden Reihenfolgen des Ableitens nähern sich ihm von verschiedenen Seiten.
:::
:::
