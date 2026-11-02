---
title: Stufe 7: Krummlinige Koordinaten und der Gradient
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3140900
summary: Bisher ging es um Integrale.
tags: krummliniges Koordinatensystem, Koordinatenlinie, natürliche Koordinatenvektorfelder, Maßfaktor, normierten Koordinatenvektorfelder, orthogonal
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bisher ging es um Integrale. Jetzt geht es um Ableitungen: Wie sieht der Gradient aus, wenn eine Funktion in Polar-, Zylinder- oder Kugelkoordinaten gegeben ist?
:::

**Die Idee.** Der Gradient misst die Änderung je Längeneinheit. Ein Schritt $\mathrm{d} r$ ist so lang, wie er heißt. Ein Schritt $\mathrm{d}\varphi$ ist aber $r\,\mathrm{d}\varphi$ lang. Deshalb muss die Ableitung nach $\varphi$ durch $r$ geteilt werden. Dazu kommt: Die passenden Richtungen, radial und tangential, sind an jedem Ort andere (Abb. [7](#abb-7)).

:::abbildung hm3/k4basis 7
In Polarkoordinaten zeigen die Einheitsvektoren $\hat{\boldsymbol{e}}_r$ (radial) und $\hat{\boldsymbol{e}}_\varphi$ (tangential) an jedem Ort in andere Richtungen, sie stehen aber überall senkrecht aufeinander. Die kartesischen Basisvektoren sind überall dieselben.
:::

Sei $\Phi(u,v,w)=\boldsymbol{x}(u,v,w)=(x(u,v,w),y(u,v,w),z(u,v,w))$ stetig differenzierbar und injektiv auf $\mathcal U\subset\mathbb{R}^3$ mit $\det D\Phi\neq0$. Dann definiert $\Phi$ ein __krummliniges Koordinatensystem__ $(u,v,w)$. Ändert man nur eine Koordinate, durchläuft man eine __Koordinatenlinie__.

:::definition Definition 7.1 (Koordinatenvektorfelder)
<span class="anker" id="satz-7-1"></span>

Die Tangentenvektoren an die Koordinatenlinien

<span class="anker" id="gl-7-1"></span>
$$\boldsymbol a_u:=\frac{\partial\Phi}{\partial u},\quad\boldsymbol a_v:=\frac{\partial\Phi}{\partial v},\quad\boldsymbol a_w:=\frac{\partial\Phi}{\partial w} \tag{7.1}$$

heißen __natürliche Koordinatenvektorfelder__. Mit dem __Maßfaktor__ $h_u:=|\partial\Phi/\partial u|$ heißen

<span class="anker" id="gl-7-2"></span>
$$\hat{\boldsymbol{e}}_u:=\frac1{h_u}\frac{\partial\Phi}{\partial u} \tag{7.2}$$

und entsprechend $\hat{\boldsymbol{e}}_v,\hat{\boldsymbol{e}}_w$ die __normierten Koordinatenvektorfelder__. Bilden $\{\hat{\boldsymbol{e}}_u,\hat{\boldsymbol{e}}_v,\hat{\boldsymbol{e}}_w\}$ in jedem Punkt eine Orthonormalbasis, heißt das Koordinatensystem __orthogonal__.
:::

⁠**So liest man das:** $h_u\,\mathrm{d} u$ ist die wahre Länge eines Schritts $\mathrm{d} u$. Eine Längenkoordinate hat $h=1$, der Winkel $\varphi$ hat $h_\varphi=r$. Anders als kartesische Basisvektoren drehen sich die $\hat{\boldsymbol{e}}$ mit dem Ort mit. In einem orthogonalen System gilt für jedes Vektorfeld $\boldsymbol{F}$

<span class="anker" id="gl-7-3"></span>
$$\boldsymbol{F}=(\boldsymbol{F}\cdot\hat{\boldsymbol{e}}_u)\,\hat{\boldsymbol{e}}_u+(\boldsymbol{F}\cdot\hat{\boldsymbol{e}}_v)\,\hat{\boldsymbol{e}}_v+(\boldsymbol{F}\cdot\hat{\boldsymbol{e}}_w)\,\hat{\boldsymbol{e}}_w=:F_u\,\hat{\boldsymbol{e}}_u+F_v\,\hat{\boldsymbol{e}}_v+F_w\,\hat{\boldsymbol{e}}_w. \tag{7.3}$$

:::satz Satz 7.2 (Gradient in orthogonalen Koordinaten)
<span class="anker" id="satz-7-2"></span>

In einem orthogonalen Koordinatensystem gilt

<span class="anker" id="gl-7-4"></span>
$$\nabla f=\frac1{h_u}\frac{\partial f}{\partial u}\,\hat{\boldsymbol{e}}_u+\frac1{h_v}\frac{\partial f}{\partial v}\,\hat{\boldsymbol{e}}_v+\frac1{h_w}\frac{\partial f}{\partial w}\,\hat{\boldsymbol{e}}_w. \tag{7.4}$$
:::

⁠**So liest man das:** Jede Komponente ist die Ableitung nach einer Koordinate, geteilt durch die Länge des Schritts. Rechts steht $f$ kurz für $f\circ\Phi$. In der Ebene gilt die Formel entsprechend mit zwei Summanden.

:::beweis Gradient
Die Kettenregel gibt $\frac{\partial}{\partial u}f(\Phi(u,v,w))=\nabla f\cdot\frac{\partial\Phi}{\partial u}=h_u\,\nabla f\cdot\hat{\boldsymbol{e}}_u$. Also ist die $u$-Komponente $\nabla f\cdot\hat{\boldsymbol{e}}_u=\frac1{h_u}\frac{\partial f}{\partial u}$, und für $v$ und $w$ gilt dasselbe. Einsetzen in [(7.3)](#gl-7-3) mit $\boldsymbol{F}=\nabla f$ gibt die Behauptung.
:::

**Warum orthogonal nötig ist.** Die schiefen Koordinaten $\Phi(u,v)=(u+v,\,v)$ haben $\hat{\boldsymbol{e}}_u=(1,0)$, $\hat{\boldsymbol{e}}_v=\frac1{\sqrt2}(1,1)$ und $h_v=\sqrt2$. Die Funktion $f=y=v$ hat den Gradienten $(0,1)$, die Formel gäbe aber $\frac1{\sqrt2}\hat{\boldsymbol{e}}_v=(\frac12,\frac12)$. In einer schiefen Basis ist $\boldsymbol{F}\cdot\hat{\boldsymbol{e}}_u$ nicht die Komponente längs $\hat{\boldsymbol{e}}_u$, [(7.3)](#gl-7-3) gilt dort nicht.

**Beispiel: Zylinderkoordinaten.** Für $\Phi(r,\varphi,z)=(r\cos\varphi,r\sin\varphi,z)$ mit $r>0$, $\varphi\in(0,2\pi)$, $z\in\mathbb{R}$ ist

$$\boldsymbol a_r=(\cos\varphi,\sin\varphi,0)^T,\quad\boldsymbol a_\varphi=(-r\sin\varphi,r\cos\varphi,0)^T,\quad\boldsymbol a_z=(0,0,1)^T.$$

Alle Skalarprodukte verschwinden, das System ist orthogonal, mit $h_r=1$, $h_\varphi=r$, $h_z=1$. Also

<span class="anker" id="gl-7-5"></span>
$$\nabla f=\frac{\partial f}{\partial r}\,\hat{\boldsymbol{e}}_r+\frac1r\frac{\partial f}{\partial\varphi}\,\hat{\boldsymbol{e}}_\varphi+\frac{\partial f}{\partial z}\,\hat{\boldsymbol{e}}_z. \tag{7.5}$$

⁠**Kontrolle:** $f=x=r\cos\varphi$ gibt $\cos\varphi\,\hat{\boldsymbol{e}}_r-\sin\varphi\,\hat{\boldsymbol{e}}_\varphi=(1,0,0)$, wie es sein muss.

:::zusatz Maßfaktoren und Volumen
Die Spalten von $D\Phi$ sind $h_u\hat{\boldsymbol{e}}_u$, $h_v\hat{\boldsymbol{e}}_v$, $h_w\hat{\boldsymbol{e}}_w$. In einem orthogonalen System ist deshalb $|\det D\Phi|=h_uh_vh_w$: die Zelle ist ein Quader mit den Kanten $h_u\,\mathrm{d} u$, $h_v\,\mathrm{d} v$, $h_w\,\mathrm{d} w$. So entstehen die Faktoren $1\cdot r\cdot1=r$ und, mit $h_\theta=r$, $h_\varphi=r\sin\theta$, auch $r^2\sin\theta$.
:::

:::frage Warum steht vor $\partial f/\partial\varphi$ der Faktor $1/r$ und nicht $r$?
Die Komponente misst die Änderung je Länge. Bei $r=2$ gehört zu einem Radiant die Bogenlänge 2. Ändert sich $f$ um 6 je Radiant, sind das 3 je Längeneinheit, also $\frac1r\cdot6$.
:::

:::aufgabe Aufgabe 11 ★★ Parabolische Koordinaten
<span class="anker" id="aufg-11"></span>

Für $u>0$ und $v,w\in\mathbb{R}$ sei $\Phi(u,v,w)=\bigl(\frac12(u^2-v^2),\,uv,\,w\bigr)$.

<ol class="al">

<li>

Berechne $\boldsymbol a_u,\boldsymbol a_v,\boldsymbol a_w$ und zeige, dass das System orthogonal ist.

</li>

<li>

Bestimme die Maßfaktoren und schreibe [(7.4)](#gl-7-4) für dieses System auf.

</li>

<li>

Prüfe die Formel an der Funktion $f=y=uv$.

</li>

</ol>

:::loesung
(a) $\boldsymbol a_u=(u,v,0)^T$, $\boldsymbol a_v=(-v,u,0)^T$, $\boldsymbol a_w=(0,0,1)^T$. Es ist $\boldsymbol a_u\cdot\boldsymbol a_v=-uv+uv=0$, und $\boldsymbol a_w$ steht senkrecht auf der $x$-$y$-Ebene, in der die beiden anderen liegen. (b) Mit $h:=\sqrt{u^2+v^2}$ ist $h_u=h_v=h$, $h_w=1$, also $\nabla f=\frac1h\frac{\partial f}{\partial u}\hat{\boldsymbol{e}}_u+\frac1h\frac{\partial f}{\partial v}\hat{\boldsymbol{e}}_v+\frac{\partial f}{\partial w}\hat{\boldsymbol{e}}_w$. (c) Für $f=uv$ ist $\nabla f=\frac vh\hat{\boldsymbol{e}}_u+\frac uh\hat{\boldsymbol{e}}_v=\frac{v}{h^2}(u,v,0)+\frac{u}{h^2}(-v,u,0)=\frac{1}{h^2}(0,\,u^2+v^2,\,0)=(0,1,0)$, also der Gradient von $y$.
:::
:::
