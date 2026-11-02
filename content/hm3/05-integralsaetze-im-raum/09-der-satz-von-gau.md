---
title: Stufe 8: Der Satz von Gauß
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3150900
summary: Die Divergenz misst die Quellstärke in einem Punkt.
tags: kompakten Träger, Indikatorfunktion
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Die Divergenz misst die Quellstärke in einem Punkt. Diese Stufe zeigt, dass die Summe aller Quellen in einem Körper gleich dem ist, was durch die Oberfläche hinausfließt.
:::

**Die Idee.** Zerlege den Körper in kleine Würfel (Abb. [7](#abb-7)). Der Abfluss aus einem Würfel ist fast $\operatorname{div}\boldsymbol{F}$ mal Volumen. Summiert man alle Würfel, zählt jede Innenwand zweimal mit entgegengesetzter Normale: Was aus dem einen Würfel herausfließt, fließt in den Nachbarn hinein. Übrig bleibt nur der Fluss durch die Außenhaut. Das ist derselbe Mechanismus wie bei Stokes, eine Dimension höher.

:::abbildung hm3/k5zellen3 7
Schnitt durch einen zerlegten Körper. Der Fluss durch eine Innenwand wird für beide Nachbarzellen mit entgegengesetztem Vorzeichen gezählt und hebt sich auf. Nur die Pfeile durch die Außenhaut bleiben.
:::

**Der Weg über partielle Integration.** Für stetig differenzierbare $f,g:\mathbb{R}^n\to\mathbb{R}$, von denen mindestens eine __kompakten Träger__ hat, also außerhalb einer beschränkten Menge null ist, gilt

<span class="anker" id="gl-8-1"></span>
$$\int_{\mathbb{R}^n}\frac{\partial f}{\partial x_k}\,g\;\mathrm{d}\boldsymbol{x}=-\int_{\mathbb{R}^n}f\,\frac{\partial g}{\partial x_k}\;\mathrm{d}\boldsymbol{x}. \tag{8.1}$$

Das ist die eindimensionale partielle Integration in der Variablen $x_k$. Die Randterme fallen weg, weil das Produkt $fg$ weit draußen null ist. Summiert man über $k$, entsteht die Regel für Vektorfelder.

:::satz Satz 8.1 (Partielle Integration im Raum)
<span class="anker" id="satz-8-1"></span>

Sind $\boldsymbol{E}:\mathbb{R}^n\to\mathbb{R}^n$ und $\varphi:\mathbb{R}^n\to\mathbb{R}$ stetig differenzierbar und hat eine davon kompakten Träger, dann gilt

<span class="anker" id="gl-8-2"></span>
$$\int_{\mathbb{R}^n}(\operatorname{div}\boldsymbol{E})\,\varphi\;\mathrm{d}\boldsymbol{x}=-\int_{\mathbb{R}^n}\boldsymbol{E}\cdot\nabla\varphi\;\mathrm{d}\boldsymbol{x}. \tag{8.2}$$
:::

Setzt man formal $\varphi=\mathbf 1_V$, die __Indikatorfunktion__ von $V$ ($1$ in $V$, $0$ außerhalb), steht links $\int_V\operatorname{div}\boldsymbol{E}\,\mathrm{d}\boldsymbol{x}$. Satz [8.1](#satz-8-1) ist hier nicht anwendbar, denn $\mathbf 1_V$ springt am Rand. Der Gradient von $\mathbf 1_V$ sitzt aber genau auf dem Rand und zeigt nach innen: formal $\nabla\mathbf 1_V\,\mathrm{d}\boldsymbol{x}\sim-\mathrm{d}\boldsymbol{S}$. Damit wird die rechte Seite zu $\int_{\partial V}\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}$.

:::satz Satz 8.2 (Gauß)
<span class="anker" id="satz-8-2"></span>

Sei $V\subset\mathbb{R}^3$ beschränkt und abgeschlossen mit glattem Rand und $\boldsymbol{F}$ stetig differenzierbar in einer Umgebung von $V$. Dann gilt

<span class="anker" id="gl-8-3"></span>
$$\int_V\operatorname{div}\boldsymbol{F}\;\mathrm{d}\boldsymbol{x}=\int_{\partial V}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}, \tag{8.3}$$

wobei $\partial V$ durch die äußere Normale orientiert ist, $\mathrm{d}\boldsymbol{S}=\boldsymbol{n}\,\mathrm{d}\sigma$.
:::

:::herleitung Gauß für den Quader
Sei $V=[a_1,b_1]\times[a_2,b_2]\times[a_3,b_3]$. Für die dritte Komponente gibt der Hauptsatz in $z$

$$\int_V\frac{\partial F_3}{\partial z}\,\mathrm{d}\boldsymbol{x}=\int\!\!\int\bigl(F_3(x,y,b_3)-F_3(x,y,a_3)\bigr)\mathrm{d} x\,\mathrm{d} y.$$

Auf dem Deckel ist $\boldsymbol{n}=\hat{\boldsymbol{e}}_3$, also $\boldsymbol{F}\cdot\boldsymbol{n}=F_3$. Auf dem Boden ist $\boldsymbol{n}=-\hat{\boldsymbol{e}}_3$, also $\boldsymbol{F}\cdot\boldsymbol{n}=-F_3$. Die rechte Seite ist der Fluss durch Deckel und Boden. Die Seitenflächen tragen zu $F_3$ nichts bei. Dasselbe für $F_1$ und $F_2$, die Summe ist [(8.3)](#gl-8-3). Allgemeine Körper setzt man aus solchen Stücken zusammen, darauf beruht das Bild der Zellen. Für glatte Ränder ist der strenge Beweis länger.
:::

⁠**So liest man das:** Links steht die Summe aller Quellen im Körper, rechts der gesamte Abfluss durch die Oberfläche. Das ist eine Bilanz. Gibt es keine Quellen ($\operatorname{div}\boldsymbol{F}=0$), fließt netto nichts hinaus: Was hineinfließt, muss wieder heraus.

**Beispiel: Kuppelkörper.** Sei $V$ der Körper zwischen Kuppel und Boden. Sein Volumen ist $\int_0^{2\pi}\!\int_0^2(4-r^2)\,r\,\mathrm{d} r\,\mathrm{d}\varphi=8\pi$. Mit $\operatorname{div}\boldsymbol{F}=2$ ist die linke Seite $16\pi$. Auf der rechten Seite ist der Fluss durch die Kuppel $16\pi$ (Stufe [4](orientierung-und-flussintegral.html#stufe-4)). Auf dem Boden ist $\boldsymbol{n}=(0,0,-1)$ und $\boldsymbol{F}\cdot\boldsymbol{n}=-2z=0$. Beide Seiten stimmen.

**Kontrolle an der Kugel.** Für $\boldsymbol{F}=\boldsymbol{x}$ und $R=2$ ist $\operatorname{div}\boldsymbol{F}=3$, die linke Seite also $3\cdot\frac43\pi\cdot8=32\pi$. Auf der Kugel ist $\boldsymbol{n}=\boldsymbol{x}/2$ und $\boldsymbol{F}\cdot\boldsymbol{n}=2$, die rechte Seite also $2\cdot16\pi=32\pi$.

:::satz Satz 8.3 (Partielle Integration mit Rand)
<span class="anker" id="satz-8-3"></span>

Sei $V$ wie in Satz [8.2](#satz-8-2), und seien $\boldsymbol{E}$ und $\varphi$ stetig differenzierbar in einer Umgebung von $V$. Dann gilt

<span class="anker" id="gl-8-4"></span>
$$\int_V\boldsymbol{E}\cdot\nabla\varphi\;\mathrm{d}\boldsymbol{x}=\int_{\partial V}\varphi\,\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}-\int_V(\operatorname{div}\boldsymbol{E})\,\varphi\;\mathrm{d}\boldsymbol{x}. \tag{8.4}$$
:::

:::beweis Partielle Integration mit Rand
Die Produktregel gibt $\operatorname{div}(\varphi\boldsymbol{E})=\nabla\varphi\cdot\boldsymbol{E}+\varphi\,\operatorname{div}\boldsymbol{E}$. Integriert man über $V$ und wendet links Gauß auf $\varphi\boldsymbol{E}$ an, steht die Formel da.
:::

:::frage Mein Körper hat eine offene Seite. Kann ich Gauß trotzdem nehmen?
Ja, und das ist der wichtigste Trick dieser Stufe. Soll der Fluss durch eine offene Fläche berechnet werden, schließt man sie mit einem Deckel, wendet Gauß an und zieht den Fluss durch den Deckel ab. Ist $\operatorname{div}\boldsymbol{F}=0$, ist der Fluss durch die Fläche gleich dem Fluss durch den Deckel. So wird aus einem schwierigen ein einfaches Integral.
:::

:::zusatz Gauß in der Elektrotechnik
Mit $\operatorname{div}\boldsymbol D=\rho$ ist Gauß das Gaußsche Gesetz: Der Fluss von $\boldsymbol D$ durch eine geschlossene Fläche ist die eingeschlossene Ladung. Das Beispiel [(7.1)](wann-ein-feld-eine-rotation-ist.html#gl-7-1) zeigt es für die Punktladung, jede Kugel liefert denselben Fluss $Q$.
:::

:::aufgabe Aufgabe 11 ★★ Greensche Formeln
<span class="anker" id="aufg-11"></span>

Seien $f,g$ zweimal stetig differenzierbar in einer Umgebung von $V$ und $\partial f/\partial\boldsymbol{n}:=\nabla f\cdot\boldsymbol{n}$.

<ol class="al">

<li>

Zeige $\int_Vg\,\Delta f\,\mathrm{d}\boldsymbol{x}=\int_{\partial V}g\,\frac{\partial f}{\partial\boldsymbol{n}}\,\mathrm{d}\sigma-\int_V\nabla g\cdot\nabla f\,\mathrm{d}\boldsymbol{x}$. Tipp: Satz [8.3](#satz-8-3) mit $\boldsymbol{E}=\nabla f$.

</li>

<li>

Folgere $\int_V(f\Delta g-g\Delta f)\,\mathrm{d}\boldsymbol{x}=\int_{\partial V}\bigl(f\frac{\partial g}{\partial\boldsymbol{n}}-g\frac{\partial f}{\partial\boldsymbol{n}}\bigr)\mathrm{d}\sigma$.

</li>

</ol>

:::loesung
(a) Satz [8.3](#satz-8-3) mit $\boldsymbol{E}=\nabla f$, $\varphi=g$ gibt $\int_V\nabla f\cdot\nabla g=\int_{\partial V}g\,\nabla f\cdot\boldsymbol{n}\,\mathrm{d}\sigma-\int_Vg\,\Delta f$. Umstellen liefert die Formel. (b) Schreibe (a) noch einmal mit vertauschten $f,g$ und ziehe beide Gleichungen voneinander ab. Der Term $\int\nabla f\cdot\nabla g$ ist symmetrisch und fällt weg.
:::
:::

:::aufgabe Aufgabe 12 ★★ Halbschale
<span class="anker" id="aufg-12"></span>

Sei $G=\{1<|\boldsymbol{x}|<2,\;z>0\}$ und $\boldsymbol{F}=(|\boldsymbol{x}|^2-1)\,\boldsymbol{x}$. Berechne $\int_G\operatorname{div}\boldsymbol{F}\,\mathrm{d}\boldsymbol{x}$ mit Gauß und zur Kontrolle direkt in Kugelkoordinaten.

:::loesung
⁠**Mit Gauß:** Der Rand besteht aus drei Stücken. Auf $|\boldsymbol{x}|=2$ ist $\boldsymbol{F}=3\boldsymbol{x}$, $\boldsymbol{n}=\boldsymbol{x}/2$, also $\boldsymbol{F}\cdot\boldsymbol{n}=6$, und die Halbkugel hat die Fläche $8\pi$: Beitrag $48\pi$. Auf $|\boldsymbol{x}|=1$ ist $\boldsymbol{F}=0$. Auf dem Boden $z=0$ ist $\boldsymbol{n}=(0,0,-1)$, also $\boldsymbol{F}\cdot\boldsymbol{n}=-(|\boldsymbol{x}|^2-1)\,z=0$. Summe: $48\pi$. **Direkt:** $\operatorname{div}\boldsymbol{F}=\nabla(\rho^2-1)\cdot\boldsymbol{x}+3(\rho^2-1)=5\rho^2-3$. Damit $2\pi\int_1^2(5\rho^2-3)\rho^2\,\mathrm{d}\rho=2\pi[\rho^5-\rho^3]_1^2=48\pi$.
:::
:::

:::aufgabe Aufgabe 13 ★★★ Kugelkappe mit Deckel
<span class="anker" id="aufg-13"></span>

Sei $K$ der Teil der Kugel $|\boldsymbol{x}|=2$ mit $z\ge1$, $\boldsymbol{n}$ nach außen, und $\boldsymbol{F}=(y\,\mathrm{e}^z,\;x\sin z,\;3)$. Berechne $\int_K\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$. Tipp: $\operatorname{div}\boldsymbol{F}$ berechnen und mit der Scheibe in der Ebene $z=1$ schließen.

:::loesung
$\operatorname{div}\boldsymbol{F}=0+0+0=0$. Die Kappe und die Scheibe $D=\{z=1,\;x^2+y^2\le3\}$ schließen einen Körper ein. Nach Gauß ist der Gesamtfluss nach außen null. Auf $D$ zeigt die äußere Normale nach unten, also ist $\int_K\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=\int_D\boldsymbol{F}\cdot\hat{\boldsymbol{e}}_3\,\mathrm{d}\sigma=3\cdot3\pi=9\pi$.
:::
:::

:::aufgabe Aufgabe 14 ★★ Eine Aussage, zwei Wege
<span class="anker" id="aufg-14"></span>

Sei $\boldsymbol{F}$ zweimal stetig differenzierbar auf $\mathbb{R}^3$. Zeige $\int_{\partial B_R(0)}\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=0$

<ol class="al">

<li>

mit Gauß,

</li>

<li>

mit Stokes, indem du die Kugel in zwei Hälften zerlegst.

</li>

</ol>

:::loesung
(a) $\operatorname{div}\operatorname{rot}\boldsymbol{F}=0$, also ist das Volumenintegral null. (b) Beide Halbkugeln haben den Äquator als Rand, aber mit entgegengesetztem Umlauf. Nach Stokes heben sich beide Kurvenintegrale auf.
:::
:::

:::aufgabe Aufgabe 15 ★★★ Ableiten nach dem Radius
<span class="anker" id="aufg-15"></span>

Sei $f$ stetig und $I(r)=\int_{B_r(\boldsymbol{x}_0)}f\,\mathrm{d}\boldsymbol{x}$. Zeige $I'(r)=\int_{\partial B_r(\boldsymbol{x}_0)}f\,\mathrm{d}\sigma$. Tipp: Schreibe $I$ in Kugelkoordinaten um $\boldsymbol{x}_0$ als Integral $\int_0^r\dots\mathrm{d}\rho$. Was bedeutet die Formel anschaulich?

:::loesung
In Kugelkoordinaten um $\boldsymbol{x}_0$ ist $I(r)=\int_0^r\Bigl(\int_{\partial B_\rho(\boldsymbol{x}_0)}f\,\mathrm{d}\sigma\Bigr)\mathrm{d}\rho$, denn $\mathrm{d}\boldsymbol{x}=\rho^2\sin\theta\,\mathrm{d}\rho\,\mathrm{d}\theta\,\mathrm{d}\varphi$ und $\rho^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi=\mathrm{d}\sigma$. Der innere Ausdruck ist stetig in $\rho$, der Hauptsatz gibt die Behauptung. Anschaulich: Wächst der Radius um $\mathrm{d} r$, kommt eine dünne Schale mit Volumen $\mathrm{d}\sigma\,\mathrm{d} r$ dazu.
:::
:::
