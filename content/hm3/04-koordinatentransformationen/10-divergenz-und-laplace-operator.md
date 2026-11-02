---
title: Stufe 8: Divergenz und Laplace-Operator
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3141000
summary: Beim Gradienten genügt es, durch die Längen zu teilen.
tags: dyadische Produkt, Spur
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Beim Gradienten genügt es, durch die Längen zu teilen. Bei der Divergenz kommt etwas hinzu: Die Basisvektoren selbst ändern sich von Ort zu Ort. Diese Stufe zeigt, welche Zusatzterme das erzeugt.
:::

**Die Idee.** Das ebene Feld $\hat{\boldsymbol{e}}_r$ hat überall die radiale Komponente 1, sie ändert sich also nicht. Trotzdem laufen seine Pfeile auseinander (Abb. [8](#abb-8)), und tatsächlich ist $\operatorname{div}\hat{\boldsymbol{e}}_r=1/r\neq0$. Die Komponenten allein reichen also nicht, auch die Drehung der Basis zählt.

:::abbildung hm3/k4drehung 8
Links: Das Feld $\hat{\boldsymbol{e}}_r$ hat überall die Länge 1, und doch laufen die Pfeile auseinander. Rechts: Wächst $\varphi$ um $\Delta\varphi$, ändert sich $\hat{\boldsymbol{e}}_r$ fast um $\Delta\varphi\,\hat{\boldsymbol{e}}_\varphi$. Daraus wird $\partial\hat{\boldsymbol{e}}_r/\partial\varphi=\hat{\boldsymbol{e}}_\varphi$.
:::

**Die Jacobi-Matrix.** Die Zeilen von $D\boldsymbol{F}$ sind die Gradienten der kartesischen Komponenten von $\boldsymbol{F}$. Wendet man [(7.4)](krummlinige-koordinaten-und-der-gradient.html#gl-7-4) auf jede Zeile an, entsteht

<span class="anker" id="gl-8-1"></span>
$$D\boldsymbol{F}=\frac1{h_u}\frac{\partial\boldsymbol{F}}{\partial u}\otimes\hat{\boldsymbol{e}}_u+\frac1{h_v}\frac{\partial\boldsymbol{F}}{\partial v}\otimes\hat{\boldsymbol{e}}_v+\frac1{h_w}\frac{\partial\boldsymbol{F}}{\partial w}\otimes\hat{\boldsymbol{e}}_w. \tag{8.1}$$

Dabei ist $\boldsymbol a\otimes\boldsymbol b$ das __dyadische Produkt__, die Matrix mit den Einträgen $(\boldsymbol a\otimes\boldsymbol b)_{ij}=a_ib_j$. In der Basis $\hat{\boldsymbol{e}}_u,\hat{\boldsymbol{e}}_v,\hat{\boldsymbol{e}}_w$ hat $D\boldsymbol{F}$ die Diagonalelemente

<span class="anker" id="gl-8-2"></span>
$$(D\boldsymbol{F})_{uu}=\frac1{h_u}\Bigl(\frac{\partial\boldsymbol{F}}{\partial u}\cdot\hat{\boldsymbol{e}}_u\Bigr),\quad(D\boldsymbol{F})_{vv}=\frac1{h_v}\Bigl(\frac{\partial\boldsymbol{F}}{\partial v}\cdot\hat{\boldsymbol{e}}_v\Bigr),\quad(D\boldsymbol{F})_{ww}=\frac1{h_w}\Bigl(\frac{\partial\boldsymbol{F}}{\partial w}\cdot\hat{\boldsymbol{e}}_w\Bigr). \tag{8.2}$$

Die __Spur__, die Summe der Diagonalelemente, hängt nicht von der Orthonormalbasis ab, und $\operatorname{div}\boldsymbol{F}=\operatorname{spur}(D\boldsymbol{F})$. Also ist

<span class="anker" id="gl-8-3"></span>
$$\operatorname{div}\boldsymbol{F}=\frac1{h_u}\Bigl(\frac{\partial\boldsymbol{F}}{\partial u}\cdot\hat{\boldsymbol{e}}_u\Bigr)+\frac1{h_v}\Bigl(\frac{\partial\boldsymbol{F}}{\partial v}\cdot\hat{\boldsymbol{e}}_v\Bigr)+\frac1{h_w}\Bigl(\frac{\partial\boldsymbol{F}}{\partial w}\cdot\hat{\boldsymbol{e}}_w\Bigr). \tag{8.3}$$

**Der Zusatzterm.** Aus $F_u=\boldsymbol{F}\cdot\hat{\boldsymbol{e}}_u$ folgt mit der Produktregel, und analog für $v$ und $w$,

<span class="anker" id="gl-8-4"></span>
$$\frac1{h_u}\Bigl(\frac{\partial\boldsymbol{F}}{\partial u}\cdot\hat{\boldsymbol{e}}_u\Bigr)=\frac1{h_u}\Bigl(\frac{\partial F_u}{\partial u}-\boldsymbol{F}\cdot\frac{\partial\hat{\boldsymbol{e}}_u}{\partial u}\Bigr). \tag{8.4}$$

Der letzte Term ist die Drehung der Basis. Kartesisch fehlt er, denn dort sind die Basisvektoren konstant. Die Ableitungen von $\hat{\boldsymbol{e}}_u$ lassen sich als Linearkombinationen von $\hat{\boldsymbol{e}}_u,\hat{\boldsymbol{e}}_v,\hat{\boldsymbol{e}}_w$ schreiben, meist mit veränderlichen Koeffizienten. In orthogonalen Koordinaten fällt dabei der Koeffizient von $\hat{\boldsymbol{e}}_u$ immer weg: Aus $|\hat{\boldsymbol{e}}_u|^2=1$ folgt $\hat{\boldsymbol{e}}_u\cdot\partial\hat{\boldsymbol{e}}_u/\partial u=0$. So ist $\partial\hat{\boldsymbol{e}}_u/\partial u$ eine Linearkombination von $\hat{\boldsymbol{e}}_v$ und $\hat{\boldsymbol{e}}_w$.

**Beispiel: Zylinderkoordinaten.** Sei $\boldsymbol{E}=E_r\hat{\boldsymbol{e}}_r+E_\varphi\hat{\boldsymbol{e}}_\varphi+E_z\hat{\boldsymbol{e}}_z$. Aus $\hat{\boldsymbol{e}}_r=(\cos\varphi,\sin\varphi,0)$, $\hat{\boldsymbol{e}}_\varphi=(-\sin\varphi,\cos\varphi,0)$, $\hat{\boldsymbol{e}}_z=(0,0,1)$ folgt

<span class="anker" id="gl-8-5"></span>
$$\frac{\partial\hat{\boldsymbol{e}}_r}{\partial\varphi}=\hat{\boldsymbol{e}}_\varphi,\qquad\frac{\partial\hat{\boldsymbol{e}}_\varphi}{\partial\varphi}=-\hat{\boldsymbol{e}}_r, \tag{8.5}$$

und alle übrigen Ableitungen, etwa $\partial\hat{\boldsymbol{e}}_z/\partial\varphi$, $\partial\hat{\boldsymbol{e}}_z/\partial r$, $\partial\hat{\boldsymbol{e}}_\varphi/\partial z$, $\partial\hat{\boldsymbol{e}}_r/\partial z$, sind null. Einsetzen in [(8.4)](#gl-8-4) mit $h_r=h_z=1$, $h_\varphi=r$: Der $\varphi$-Summand gibt $\frac1r\bigl(\frac{\partial E_\varphi}{\partial\varphi}+\boldsymbol{E}\cdot\hat{\boldsymbol{e}}_r\bigr)$, die anderen beiden bleiben unverändert. Also

<span class="anker" id="gl-8-6"></span>
$$\operatorname{div}\boldsymbol{E}=\frac{\partial E_r}{\partial r}+\frac1r\frac{\partial E_\varphi}{\partial\varphi}+\frac1rE_r+\frac{\partial E_z}{\partial z}=\frac1r\Bigl(\frac{\partial}{\partial r}(rE_r)+\frac{\partial E_\varphi}{\partial\varphi}\Bigr)+\frac{\partial E_z}{\partial z}. \tag{8.6}$$

Mit $E_r=1$ und $E_\varphi=E_z=0$ ist das die Zahl $1/r$ aus der Idee. Setzt man $\boldsymbol{E}=\nabla f$ aus [(7.5)](krummlinige-koordinaten-und-der-gradient.html#gl-7-5) ein, folgt der Laplace-Operator in Zylinderkoordinaten:

<span class="anker" id="gl-8-7"></span>
$$\Delta f=\operatorname{div}\nabla f=\frac{\partial^2f}{\partial r^2}+\frac1r\frac{\partial f}{\partial r}+\frac1{r^2}\frac{\partial^2f}{\partial\varphi^2}+\frac{\partial^2f}{\partial z^2}. \tag{8.7}$$

⁠**Kontrolle:** $f=x^2+y^2=r^2$ gibt $2+2=4$, wie kartesisch. $f=x^2-y^2=r^2\cos2\varphi$ gibt $2\cos2\varphi+2\cos2\varphi-4\cos2\varphi=0$, ebenfalls wie kartesisch.

:::frage Warum steht in $\Delta f$ ein Term mit $\partial f/\partial r$, also eine erste Ableitung?
Weil sich die Basis dreht. Er stammt aus dem Zusatzterm $\frac1rE_r$ der Divergenz. Kartesisch gibt es nur zweite Ableitungen. Für $f=\ln r$ hebt er die zweite Ableitung genau auf: $-1/r^2+1/r^2=0$. Solche Potentiale treten um einen geladenen Draht auf.
:::

:::aufgabe Aufgabe 12 ★★★ Kugelkoordinaten
<span class="anker" id="aufg-12"></span>

Sei $\Phi(r,\theta,\varphi)$ wie in [(4.3)](zylinder-und-kugelkoordinaten.html#gl-4-3) mit $r>0$, $\theta\in(0,\pi)$, $\varphi\in(0,2\pi)$.

<ol class="al">

<li>

Zeige, dass das System orthogonal ist, mit $h_r=1$, $h_\theta=r$, $h_\varphi=r\sin\theta$. Gib $\nabla f$ an.

</li>

<li>

Prüfe $\frac{\partial\hat{\boldsymbol{e}}_r}{\partial\theta}=\hat{\boldsymbol{e}}_\theta$, $\frac{\partial\hat{\boldsymbol{e}}_\theta}{\partial\theta}=-\hat{\boldsymbol{e}}_r$, $\frac{\partial\hat{\boldsymbol{e}}_r}{\partial\varphi}=\sin\theta\,\hat{\boldsymbol{e}}_\varphi$, $\frac{\partial\hat{\boldsymbol{e}}_\theta}{\partial\varphi}=\cos\theta\,\hat{\boldsymbol{e}}_\varphi$, $\frac{\partial\hat{\boldsymbol{e}}_\varphi}{\partial\varphi}=-\sin\theta\,\hat{\boldsymbol{e}}_r-\cos\theta\,\hat{\boldsymbol{e}}_\theta$.

</li>

<li>

Berechne $\operatorname{div}\boldsymbol{F}$ und daraus $\Delta f$.

</li>

<li>

Wie lautet $\Delta f$ für $f=f(r)$? Prüfe $\Delta(1/r)=0$ für $r>0$.

</li>

</ol>

:::loesung
(a) Ableiten gibt $\boldsymbol a_r=\hat{\boldsymbol{e}}_r$, $\boldsymbol a_\theta=r\,\hat{\boldsymbol{e}}_\theta$, $\boldsymbol a_\varphi=r\sin\theta\,\hat{\boldsymbol{e}}_\varphi$ mit

$$\hat{\boldsymbol{e}}_r=\begin{pmatrix}\sin\theta\cos\varphi\\\sin\theta\sin\varphi\\\cos\theta\end{pmatrix},\quad\hat{\boldsymbol{e}}_\theta=\begin{pmatrix}\cos\theta\cos\varphi\\\cos\theta\sin\varphi\\-\sin\theta\end{pmatrix},\quad\hat{\boldsymbol{e}}_\varphi=\begin{pmatrix}-\sin\varphi\\\cos\varphi\\0\end{pmatrix}.$$

Das sind Einheitsvektoren, und ihre drei Skalarprodukte verschwinden. Nach [(7.4)](krummlinige-koordinaten-und-der-gradient.html#gl-7-4) ist $\nabla f=\frac{\partial f}{\partial r}\hat{\boldsymbol{e}}_r+\frac1r\frac{\partial f}{\partial\theta}\hat{\boldsymbol{e}}_\theta+\frac1{r\sin\theta}\frac{\partial f}{\partial\varphi}\hat{\boldsymbol{e}}_\varphi$.

(b) Direktes Ableiten dieser drei Vektoren. Für die letzte Formel: $\sin\theta\,\hat{\boldsymbol{e}}_r+\cos\theta\,\hat{\boldsymbol{e}}_\theta=(\cos\varphi,\sin\varphi,0)=-\partial\hat{\boldsymbol{e}}_\varphi/\partial\varphi$.

(c) Nach [(8.4)](#gl-8-4) sind die drei Summanden $\frac{\partial F_r}{\partial r}$, dann $\frac1r\bigl(\frac{\partial F_\theta}{\partial\theta}+F_r\bigr)$ und $\frac1{r\sin\theta}\bigl(\frac{\partial F_\varphi}{\partial\varphi}+\sin\theta\,F_r+\cos\theta\,F_\theta\bigr)$. Zusammen:

$$\operatorname{div}\boldsymbol{F}=\frac1{r^2}\frac{\partial}{\partial r}(r^2F_r)+\frac1{r\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,F_\theta)+\frac1{r\sin\theta}\frac{\partial F_\varphi}{\partial\varphi}.$$

Mit $\boldsymbol{F}=\nabla f$ folgt

$$\Delta f=\frac1{r^2}\frac{\partial}{\partial r}\Bigl(r^2\frac{\partial f}{\partial r}\Bigr)+\frac1{r^2\sin\theta}\frac{\partial}{\partial\theta}\Bigl(\sin\theta\frac{\partial f}{\partial\theta}\Bigr)+\frac1{r^2\sin^2\theta}\frac{\partial^2f}{\partial\varphi^2}.$$

(d) Für $f=f(r)$ bleibt $\Delta f=\frac1{r^2}(r^2f')'$. Für $f=1/r$ ist $r^2f'=-1$ konstant, also $\Delta f=0$.
:::
:::
