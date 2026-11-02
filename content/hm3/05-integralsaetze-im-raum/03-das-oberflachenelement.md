---
title: Stufe 2: Das Oberflächenelement
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3150300
summary: Beim Biegen ändern sich Flächen.
tags: metrischen Koeffizienten, metrische Tensor, Oberflächenelement, stückweise reguläre Fläche
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Beim Biegen ändern sich Flächen. Diese Stufe bestimmt den Faktor, mit dem das Rechteck $\mathrm{d} u\,\mathrm{d} v$ groß wird, und definiert damit das Oberflächenintegral.
:::

**Die Idee.** Das kleine Rechteck mit den Kanten $\mathrm{d} u$ und $\mathrm{d} v$ im Blatt wird auf der Fläche fast zu einem Parallelogramm mit den Kanten $\boldsymbol{x}_u\,\mathrm{d} u$ und $\boldsymbol{x}_v\,\mathrm{d} v$ (Abb. [2](#abb-2)). Dessen Fläche ist der Betrag des Kreuzprodukts. Der Faktor hängt also vom Ort ab, an steilen Stellen ist er größer. Das ist dieselbe Idee wie die Funktionaldeterminante im Transformationssatz, nur dass hier zwei Dimensionen im Raum liegen und die Determinante nicht direkt passt.

:::abbildung hm3/k5element 2
Das Rechteck $\mathrm{d} u\,\mathrm{d} v$ im Parameterbereich wird zum Parallelogramm mit den Kanten $\boldsymbol{x}_u\,\mathrm{d} u$ und $\boldsymbol{x}_v\,\mathrm{d} v$. Seine Fläche ist $\mathrm{d}\sigma=|\boldsymbol{x}_u\times\boldsymbol{x}_v|\,\mathrm{d} u\,\mathrm{d} v$. Im Modellpunkt $(1,0,3)$ der Kuppel ist der Faktor $\sqrt5\approx2{,}24$ je Fläche im Grundriss.
:::

:::definition Definition 2.1 (Metrik)
<span class="anker" id="satz-2-1"></span>

Für ein reguläres Flächenstück heißen $E=|\boldsymbol{x}_u|^2$, $F=\boldsymbol{x}_u\cdot\boldsymbol{x}_v$, $G=|\boldsymbol{x}_v|^2$ die __metrischen Koeffizienten__, die Matrix $\boldsymbol{g}=\begin{pmatrix}E&F\\F&G\end{pmatrix}$ der __metrische Tensor__, und

<span class="anker" id="gl-2-1"></span>
$$\mathrm{d}\sigma=\sqrt{\det\boldsymbol{g}}\;\mathrm{d} u\,\mathrm{d} v=\sqrt{EG-F^2}\;\mathrm{d} u\,\mathrm{d} v \tag{2.1}$$

das __Oberflächenelement__.
:::

Das $F$ in $\boldsymbol{g}$ ist eine Zahl und hat nichts mit dem Vektorfeld $\boldsymbol{F}$ zu tun. Die Bezeichnung ist fest eingeführt, Verwechslungen vermeidet man durch die Fettschrift.

:::satz Satz 2.2 (Oberflächenelement und Parameterwechsel)
<span class="anker" id="satz-2-2"></span>

Es gilt $\sqrt{EG-F^2}=|\boldsymbol{x}_u\times\boldsymbol{x}_v|$. Sind $\boldsymbol{x}$ und $\boldsymbol{y}=\boldsymbol{x}\circ\psi$ zwei reguläre Parametrisierungen derselben Fläche mit Tensoren $\boldsymbol{g}$ und $\boldsymbol{g}'$, so gilt

<span class="anker" id="gl-2-2"></span>
$$\boldsymbol{g}'=D\psi^T\,\boldsymbol{g}(\psi)\,D\psi,\qquad\sqrt{\det\boldsymbol{g}'}=\sqrt{\det(\boldsymbol{g}\circ\psi)}\;|\det D\psi|. \tag{2.2}$$
:::

:::beweis Oberflächenelement und Parameterwechsel
Die Identität von Lagrange lautet $|\boldsymbol a\times\boldsymbol b|^2=|\boldsymbol a|^2|\boldsymbol b|^2-(\boldsymbol a\cdot\boldsymbol b)^2$. Mit $\boldsymbol a=\boldsymbol{x}_u$, $\boldsymbol b=\boldsymbol{x}_v$ steht rechts $EG-F^2$.

Fasst man $\boldsymbol{x}_u,\boldsymbol{x}_v$ als Spalten der $3\times2$-Matrix $D\boldsymbol{x}$ auf, ist $\boldsymbol{g}=D\boldsymbol{x}^TD\boldsymbol{x}$, denn die Einträge dieses Produkts sind die Skalarprodukte der Spalten. Die Kettenregel liefert $D\boldsymbol{y}=(D\boldsymbol{x}\circ\psi)\,D\psi$, also

$$\boldsymbol{g}'=D\boldsymbol{y}^TD\boldsymbol{y}=D\psi^T(D\boldsymbol{x}\circ\psi)^T(D\boldsymbol{x}\circ\psi)\,D\psi=D\psi^T\,\boldsymbol{g}(\psi)\,D\psi.$$

Die Determinante des Produkts gibt $\det\boldsymbol{g}'=(\det D\psi)^2\det(\boldsymbol{g}\circ\psi)$. Daraus folgt mit der Wurzel die zweite Formel.
:::

:::definition Definition 2.3 (Oberflächenintegral und Flächeninhalt)
<span class="anker" id="satz-2-3"></span>

Sei $f$ stetig in einer Umgebung von $\mathcal F=\Phi(B)$. Dann ist

<span class="anker" id="gl-2-3"></span>
$$\int_{\mathcal F}f\,\mathrm{d}\sigma:=\int_Bf(\boldsymbol{x}(u,v))\sqrt{\det\boldsymbol{g}(u,v)}\;\mathrm{d} u\,\mathrm{d} v,\qquad\mathcal A(\mathcal F)=\int_B\sqrt{EG-F^2}\;\mathrm{d} u\,\mathrm{d} v. \tag{2.3}$$
:::

⁠**So liest man das:** Das Integral summiert $f$ über die Fläche, jeder Punkt zählt mit dem wahren Flächenanteil. Für $f=1$ steht dort der Inhalt. Das Ergebnis hängt nicht von der Parametrisierung ab: In [(2.2)](#gl-2-2) ist $|\det D\psi|$ genau der Faktor des Transformationssatzes, er kürzt sich beim Wechsel der Variablen heraus.

:::definition Definition 2.4 (Stückweise reguläre Fläche)
<span class="anker" id="satz-2-4"></span>

Eine __stückweise reguläre Fläche__ besteht aus endlich vielen regulären Flächenstücken $\mathcal F_k$, die sich höchstens an den Rändern überlappen. Man setzt $\int_{\mathcal F}f\,\mathrm{d}\sigma:=\sum_k\int_{\mathcal F_k}f\,\mathrm{d}\sigma$.
:::

Das braucht man für geschlossene Flächen. Eine Kugeloberfläche oder ein Würfel lassen sich nicht als ein einziges injektives Flächenstück schreiben, wohl aber aus mehreren zusammensetzen.

**Beispiel: die Kuppel.** Mit [(1.3)](flachen-beschreiben.html#gl-1-3) ist $E=1+4r^2$, $F=0$, $G=r^2$, also $\sqrt{EG-F^2}=r\sqrt{1+4r^2}$. Der Inhalt ist

$$\mathcal A(K)=\int_0^{2\pi}\!\!\int_0^2r\sqrt{1+4r^2}\;\mathrm{d} r\,\mathrm{d}\varphi=2\pi\Bigl[\tfrac1{12}(1+4r^2)^{3/2}\Bigr]_0^2=\frac\pi6\bigl(17\sqrt{17}-1\bigr)\approx36{,}2.$$

Die Kuppel ist fast dreimal so groß wie der Kreis $4\pi\approx12{,}6$, über dem sie steht. **Grenzfall:** Für eine flache Kuppel $z=0$ fehlt das $4r^2$ unter der Wurzel, und es bleibt $\int\!\!\int r\,\mathrm{d} r\,\mathrm{d}\varphi=4\pi$.

:::frage Warum darf ich nicht einfach $\mathrm{d} x\,\mathrm{d} y$ schreiben, wenn die Fläche ein Graph ist?
Weil $\mathrm{d} x\,\mathrm{d} y$ den Schatten der Fläche misst, nicht die Fläche. Eine steile Stelle wirft einen kleinen Schatten, ist aber groß. Der Korrekturfaktor ist $\sqrt{1+|\nabla H|^2}$ (Stufe [3](drei-standardfalle.html#stufe-3)). Das ist die häufigste Fehlerquelle: $\mathrm{d}\sigma$ vergessen und über den Grundriss integrieren.
:::
