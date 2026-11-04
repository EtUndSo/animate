---
title: Divergenz, Rotation und Laplace-Operator
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110400
summary: Ein Vektorfeld hat an jedem Punkt eine Jacobi-Matrix mit n 2 Einträgen.
tags: Kreuzprodukt, Determinante, Spur, schiefsymmetrisch, symmetrischen Anteil, schiefsymmetrische Anteil, Divergenz, Quellendichte
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Ein Vektorfeld hat an jedem Punkt eine Jacobi-Matrix mit $n^2$ Einträgen. Dieser Abschnitt baut aus diesen Einträgen Größen mit anschaulicher Bedeutung: wie stark das Feld an einer Stelle auseinanderströmt und wie stark es dort kreist. Das Nabla-Symbol dient dabei als Baustein für weitere Differentialoperatoren.
:::

### Was du dafür brauchst: das Kreuzprodukt

<span class="anker" id="stufe-3-1"></span>

Im Raum gibt es zu zwei Pfeilen, die nicht parallel sind, eine Richtung, die auf beiden senkrecht steht. Das Kreuzprodukt liefert einen Pfeil in diese Richtung.

Das __Kreuzprodukt__ zweier Vektoren $\boldsymbol a,\boldsymbol b\in\mathbb{R}^3$ ist der Vektor

$$\boldsymbol a\times\boldsymbol b=\begin{pmatrix}a_2b_3-a_3b_2\\a_3b_1-a_1b_3\\a_1b_2-a_2b_1\end{pmatrix}.$$

Er steht senkrecht auf $\boldsymbol a$ und auf $\boldsymbol b$. Seine Länge ist $|\boldsymbol a|\,|\boldsymbol b|\sin\alpha$, der Flächeninhalt des Parallelogramms, das $\boldsymbol a$ und $\boldsymbol b$ aufspannen. Seine Richtung folgt der Rechte-Hand-Regel: Zeigt der Daumen der rechten Hand in Richtung $\boldsymbol a$ und der Zeigefinger in Richtung $\boldsymbol b$, zeigt der Mittelfinger in Richtung $\boldsymbol a\times\boldsymbol b$. Vertauscht man die Faktoren, kehrt sich das Vorzeichen um: $\boldsymbol b\times\boldsymbol a=-\boldsymbol a\times\boldsymbol b$. Für die Einheitsvektoren gilt $\hat{\boldsymbol{e}}_1\times\hat{\boldsymbol{e}}_2=\hat{\boldsymbol{e}}_3$, $\hat{\boldsymbol{e}}_2\times\hat{\boldsymbol{e}}_3=\hat{\boldsymbol{e}}_1$ und $\hat{\boldsymbol{e}}_3\times\hat{\boldsymbol{e}}_1=\hat{\boldsymbol{e}}_2$.

⁠**Beispiel:** $(1,2,3)\times(4,5,6)=(2\cdot6-3\cdot5,\;3\cdot4-1\cdot6,\;1\cdot5-2\cdot4)=(-3,\,6,\,-3)$. Zur Kontrolle: $(-3,6,-3)\cdot(1,2,3)=-3+12-9=0$ und $(-3,6,-3)\cdot(4,5,6)=-12+30-18=0$.

⁠**Kurz gesagt:** Das Kreuzprodukt zweier Vektoren im Raum steht senkrecht auf beiden, und seine Länge ist die Fläche des aufgespannten Parallelogramms.

### Was du dafür brauchst: Determinanten

<span class="anker" id="stufe-3-2"></span>

Die Determinante einer $3\times3$-Matrix ist eine Zahl. Mit ihr kann man das Kreuzprodukt kurz aufschreiben und Rauminhalte berechnen.

Die __Determinante__ einer $2\times2$-Matrix ist $\det\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)=ad-bc$. Für eine $3\times3$-Matrix entwickelt man nach der ersten Spalte:

$$\det\begin{pmatrix}m_{11}&m_{12}&m_{13}\\m_{21}&m_{22}&m_{23}\\m_{31}&m_{32}&m_{33}\end{pmatrix} =m_{11}\det\begin{pmatrix}m_{22}&m_{23}\\m_{32}&m_{33}\end{pmatrix} -m_{21}\det\begin{pmatrix}m_{12}&m_{13}\\m_{32}&m_{33}\end{pmatrix} +m_{31}\det\begin{pmatrix}m_{12}&m_{13}\\m_{22}&m_{23}\end{pmatrix}.$$

Jeder Eintrag der ersten Spalte wird mit der Determinante der Matrix multipliziert, die übrig bleibt, wenn man seine Zeile und seine Spalte streicht. Die Vorzeichen wechseln ab: $+,-,+$. Stehen in den Spalten die Vektoren $\boldsymbol a,\boldsymbol b,\boldsymbol c$, schreibt man $\det(\boldsymbol a|\boldsymbol b|\boldsymbol c)$. Ihr Betrag ist der Rauminhalt des schiefen Quaders, den die drei Vektoren aufspannen. Ihr Vorzeichen ist positiv, wenn $\boldsymbol a,\boldsymbol b,\boldsymbol c$ wie Daumen, Zeigefinger und Mittelfinger der rechten Hand liegen.

⁠**Beispiel:**

$$\det\begin{pmatrix}1&0&2\\2&1&0\\0&3&1\end{pmatrix}=1\cdot(1\cdot1-0\cdot3)-2\cdot(0\cdot1-2\cdot3)+0=1+12=13 .$$

⁠**Kurz gesagt:** Die Determinante einer $3\times3$-Matrix entwickelt man nach der ersten Spalte, mit abwechselnden Vorzeichen.

### Was du dafür brauchst: die Spur einer Matrix

<span class="anker" id="stufe-3-3"></span>

Manche Größen hängen nur von der Diagonale einer Matrix ab. Die einfachste ist die Summe der Diagonaleinträge.

Die __Spur__ einer quadratischen Matrix $M\in\mathbb{R}^{n\times n}$ ist die Summe ihrer Diagonaleinträge:

$$\operatorname{Spur}M=M_{11}+M_{22}+\dots+M_{nn}=\sum_{j=1}^nM_{jj}.$$

⁠**Beispiel:** $\operatorname{Spur}\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)=1+4=5$. Die Spur der Jacobi-Matrix $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ des Drehfelds ist $0$.

⁠**Kurz gesagt:** Die Spur ist die Summe der Diagonaleinträge.

### Was du dafür brauchst: schiefsymmetrische Matrizen

<span class="anker" id="stufe-3-4"></span>

Eine symmetrische Matrix bleibt beim Transponieren gleich. Das Gegenstück wechselt dabei ihr Vorzeichen, und jede quadratische Matrix setzt sich aus beiden Sorten zusammen.

Eine quadratische Matrix heißt __schiefsymmetrisch__, wenn $M^T=-M$ gilt, also $M_{jk}=-M_{kj}$ für alle $j,k$. Für $j=k$ folgt $M_{jj}=-M_{jj}$, also stehen auf der Diagonale nur Nullen. Jede quadratische Matrix $M$ ist die Summe eines symmetrischen und eines schiefsymmetrischen Anteils:

$$M=\underbrace{\tfrac12\bigl(M+M^T\bigr)}_{\text{symmetrisch}}+\underbrace{\tfrac12\bigl(M-M^T\bigr)}_{\text{schiefsymmetrisch}} .$$

Man nennt $\frac12(M+M^T)$ den __symmetrischen Anteil__ von $M$. Entsprechend heißt $\frac12(M-M^T)$ der __schiefsymmetrische Anteil__ von $M$. Eine Matrix ist genau dann symmetrisch, wenn ihr schiefsymmetrischer Anteil null ist.

⁠**Beispiel:** $\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}1&1\\1&3\end{smallmatrix}\bigr)+\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$. Die Jacobi-Matrix $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ des Drehfelds ist selbst schiefsymmetrisch.

⁠**Kurz gesagt:** Schiefsymmetrisch heißt: Transponieren wechselt das Vorzeichen. Jede quadratische Matrix ist symmetrischer plus schiefsymmetrischer Anteil.

### Die Divergenz

<span class="anker" id="stufe-3-5"></span>

Strömt ein Feld an einer Stelle auseinander, als ob dort etwas entspringt? Oder läuft es dort zusammen, als ob dort etwas versickert? Eine einzige Zahl pro Punkt soll das messen.

Man stellt sich das Feld als Geschwindigkeit einer Strömung vor und um einen Punkt ein kleines gedachtes Kästchen (Abb. [12](#abb-12)). Fließt mehr hinaus als hinein, entspringt im Kästchen etwas. Durch die zwei Wände senkrecht zur $x_j$-Achse fließt nur die Komponente $E_j$. Hinaus fließt mehr als hinein, wenn $E_j$ an der einen Wand größer ist als an der gegenüberliegenden, wenn also $E_j$ in Richtung $x_j$ wächst. Es kommt also auf die Ableitungen $\partial E_j/\partial x_j$ an, die Diagonale der Jacobi-Matrix.

:::abbildung hm3/k1quelle 12
Links strömt aus dem gestrichelten Kästchen mehr hinaus als hinein. In der Mitte tritt an der einen Wand aus, was an der gegenüberliegenden eintritt. Rechts strömt es seitlich hinaus und oben und unten hinein, die Bilanz ist null.
:::

:::definition Definition 3.1 (Divergenz)
<span class="anker" id="satz-3-1"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $\boldsymbol{E}=(E_1,\dots,E_n)^T$ ein differenzierbares Vektorfeld auf $\mathcal U$. Die __Divergenz__ von $\boldsymbol{E}$ ist

<span class="anker" id="gl-3-1"></span>
$$\operatorname{div}\boldsymbol{E}:=\nabla\cdot\boldsymbol{E}=\sum_{j=1}^n\frac{\partial E_j}{\partial x_j}. \tag{3.1}$$
:::

⁠**So liest man das:** Die Divergenz macht aus einem Vektorfeld eine skalare Funktion. Die Schreibweise $\nabla\cdot\boldsymbol{E}$ ist das formale Skalarprodukt von Nabla mit $\boldsymbol{E}$: Eintrag $j$ von $\nabla$ leitet die Komponente $E_j$ ab, und alles wird addiert. Die Divergenz ist die Spur der Jacobi-Matrix: $\operatorname{div}\boldsymbol{E}=\operatorname{Spur}D\boldsymbol{E}$. Sie ist ein Maß für die örtliche __Quellendichte__ des Felds. Einen Punkt mit $\operatorname{div}\boldsymbol{E}>0$ nennt man eine __Quelle__. Einen Punkt mit $\operatorname{div}\boldsymbol{E}<0$ nennt man eine __Senke__.

⁠**Beispiele:** Für $\boldsymbol{E}=(2x,4y)$ ist $\operatorname{div}\boldsymbol{E}=2+4=6$. Das Drehfeld hat $\operatorname{div}(-y,x)=0+0=0$. Das Strahlfeld in $\mathbb{R}^n$ hat $\operatorname{div}\boldsymbol{x}=1+1+\dots+1=n$. Die drei Felder in Abb. [12](#abb-12) haben $\operatorname{div}(x,y)=2$, $\operatorname{div}(1,0)=0$ und $\operatorname{div}(x,-y)=1-1=0$.

:::hintergrund Warum gerade diese Summe misst, wie viel entspringt
Man denke sich $\boldsymbol{E}$ als Geschwindigkeit einer Flüssigkeit im Raum. Durch eine kleine ebene Wand mit dem Flächeninhalt $A$, die senkrecht zur $x_j$-Achse steht, tritt pro Zeit ungefähr das Volumen $A\,E_j$ hindurch: Nur die Komponente senkrecht zur Wand trägt etwas über sie hinweg, die beiden anderen schieben parallel zu ihr. Diese Menge pro Zeit nennt man den *Fluss* durch die Wand.

Nun ein Würfel mit der Kantenlänge $a$ und dem Mittelpunkt $\boldsymbol{x}$. Seine beiden Wände senkrecht zur $x_j$-Achse haben die Mittelpunkte $\boldsymbol{x}\pm\frac a2\hat{\boldsymbol{e}}_j$ und den Inhalt $a^2$. Hinaus fließt durch die vordere Wand etwa $a^2E_j(\boldsymbol{x}+\frac a2\hat{\boldsymbol{e}}_j)$, durch die hintere hinein etwa $a^2E_j(\boldsymbol{x}-\frac a2\hat{\boldsymbol{e}}_j)$. Netto verlässt den Würfel durch dieses Wandpaar also

$$a^2\Bigl(E_j\bigl(\boldsymbol{x}+\tfrac a2\hat{\boldsymbol{e}}_j\bigr)-E_j\bigl(\boldsymbol{x}-\tfrac a2\hat{\boldsymbol{e}}_j\bigr)\Bigr)\approx a^2\cdot a\,\frac{\partial E_j}{\partial x_j}(\boldsymbol{x})=a^3\,\frac{\partial E_j}{\partial x_j}(\boldsymbol{x}).$$

Die drei Wandpaare zusammen geben $a^3\operatorname{div}\boldsymbol{E}(\boldsymbol{x})$. Teilt man durch das Volumen $a^3$, bleibt die Divergenz. Für ein stetig differenzierbares Feld werden alle Näherungen beim Verkleinern des Würfels exakt: Die Divergenz ist der Grenzwert von „Fluss aus dem Würfel durch Volumen des Würfels“ für $a\to0$. Darum heißt sie Quellendichte: Sie gibt an, wie viel pro Volumen und Zeit entsteht. In der Ebene tritt ein Quadrat an die Stelle des Würfels und sein Flächeninhalt an die Stelle des Volumens. Die Ableitungen $\partial E_j/\partial x_k$ mit $j\neq k$ kommen nicht vor: Sie beschreiben, wie sich das Feld parallel zu einer Wand ändert, und das schiebt nichts durch die Wand.
:::

⁠**Kurz gesagt:** Die Divergenz ist die Summe der Ableitungen jeder Komponente nach ihrer eigenen Richtung. Sie misst, wie viel ein Feld an einer Stelle pro Volumen auseinanderströmt.

### Die Divergenz eines Gradientenfelds

<span class="anker" id="stufe-3-6"></span>

Was ergibt die Divergenz, wenn das Feld der Gradient einer skalaren Funktion ist? Dann treffen zwei Ableitungen aufeinander.

Ist $\boldsymbol{E}=\nabla\varphi$ mit einer zweimal differenzierbaren Funktion $\varphi$, dann ist $E_j=\partial\varphi/\partial x_j$, und die Divergenz wird

$$\operatorname{div}\boldsymbol{E}=\sum_{j=1}^n\frac{\partial}{\partial x_j}\Bigl(\frac{\partial\varphi}{\partial x_j}\Bigr)=\sum_{j=1}^n\frac{\partial^2\varphi}{\partial x_j^2}.$$

Es tritt also die Summe der zweiten partiellen Ableitungen nach jeweils derselben Variablen auf.

⁠**Beispiel:** Für die Schale $\varphi=x^2+2y^2$ ist $\nabla\varphi=(2x,4y)$ und $\operatorname{div}\nabla\varphi=2+4=6$. Ebenso ist $\frac{\partial^2\varphi}{\partial x^2}+\frac{\partial^2\varphi}{\partial y^2}=2+4=6$.

⁠**Kurz gesagt:** Die Divergenz eines Gradientenfelds ist die Summe der reinen zweiten Ableitungen des Skalarpotentials.

### Der Laplace-Operator

<span class="anker" id="stufe-3-7"></span>

Die Summe aus dem letzten Unterabschnitt kommt in der Physik so oft vor, dass sie einen eigenen Namen bekommt. Sie vergleicht, wie sich eine Funktion an einem Punkt zu ihrer Umgebung verhält.

:::definition Definition 3.2 (Laplace-Operator)
<span class="anker" id="satz-3-2"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $\varphi\colon\mathcal U\to\mathbb{R}$ zweimal differenzierbar. Dann ist

<span class="anker" id="gl-3-2"></span>
$$\Delta\varphi:=\sum_{j=1}^n\frac{\partial^2\varphi}{\partial x_j^2}. \tag{3.2}$$

Das Zeichen $\Delta$ heißt __Laplace-Operator__.
:::

⁠**So liest man das:** Nach dem letzten Unterabschnitt gilt

$$\Delta\varphi=\operatorname{div}(\nabla\varphi),\qquad\text{formal also}\qquad\Delta=\nabla\cdot\nabla .$$

Deshalb schreibt man in den Natur- und Ingenieurwissenschaften oft $\nabla^2$ statt $\Delta$. Der Laplace-Operator braucht zweite Ableitungen, er ist ein Differentialoperator zweiter Ordnung. Er wirkt nach der Definition auf skalare Funktionen. Auf ein Vektorfeld $\boldsymbol{F}=(F_1,\dots,F_n)^T$ wendet man ihn Komponente für Komponente an:

$$\Delta\boldsymbol{F}=(\Delta F_1,\dots,\Delta F_n)^T .$$

⁠**Beispiele:** $\Delta(x^2+2y^2)=2+4=6$, $\Delta(x^2+y^2)=4$ und $\Delta(x^2-y^2)=2-2=0$. Für das Vektorfeld $\boldsymbol{F}=(x^2,\;xy,\;z^3)$ ist $\Delta\boldsymbol{F}=(2,\;0,\;6z)^T$.

:::hintergrund Was der Laplace-Operator misst: Abweichung vom Mittelwert der Nachbarn
In einer Variablen gilt nach der Taylorformel $\varphi(x\pm a)=\varphi(x)\pm a\,\varphi'(x)+\frac{a^2}2\varphi''(x)+\dots$, wobei die Punkte für Glieder stehen, die schneller als $a^2$ klein werden. Addiert man beide Gleichungen, heben sich die ersten Ableitungen weg:

$$\frac{\varphi(x+a)+\varphi(x-a)}2-\varphi(x)\approx\frac{a^2}{2}\,\varphi''(x).$$

Die zweite Ableitung misst also, um wie viel der Mittelwert der beiden Nachbarn über dem Wert in der Mitte liegt. In $n$ Variablen macht man dasselbe in jeder Achsenrichtung und mittelt über alle $2n$ Nachbarn $\boldsymbol{x}\pm a\,\hat{\boldsymbol{e}}_j$:

$$\frac1{2n}\sum_{j=1}^n\bigl(\varphi(\boldsymbol{x}+a\hat{\boldsymbol{e}}_j)+\varphi(\boldsymbol{x}-a\hat{\boldsymbol{e}}_j)\bigr)-\varphi(\boldsymbol{x})\approx\frac{a^2}{2n}\,\Delta\varphi(\boldsymbol{x}).$$

Ist $\Delta\varphi(\boldsymbol{x})>0$, liegt $\varphi$ in $\boldsymbol{x}$ unter dem Mittel der Umgebung, wie am Boden einer Mulde. Ist $\Delta\varphi(\boldsymbol{x})<0$, liegt $\varphi$ darüber, wie auf einer Kuppe. Für zweimal stetig differenzierbares $\varphi$ gilt dieselbe Aussage auch für den Mittelwert über eine ganze kleine Kugelfläche um $\boldsymbol{x}$. Darum taucht $\Delta$ überall dort auf, wo sich etwas mit seiner Umgebung ausgleicht: Wärme fließt von warmen zu kalten Nachbarn, bis jeder Punkt den Mittelwert seiner Umgebung annimmt.
:::

⁠**Kurz gesagt:** Der Laplace-Operator ist die Summe der reinen zweiten Ableitungen, also die Divergenz des Gradienten.

### Harmonische Funktionen

<span class="anker" id="stufe-3-8"></span>

Besonders wichtig sind Funktionen, für die der Laplace-Operator überall null ist. Sie beschreiben zum Beispiel das elektrische Potential in einem Bereich ohne Ladungen.

:::definition Definition 3.3 (Harmonische Funktion)
<span class="anker" id="satz-3-3"></span>

Eine zweimal differenzierbare Funktion $u$ auf einer offenen Menge heißt __harmonisch__, wenn dort $\Delta u=0$ gilt.
:::

Wegen $\Delta u=\operatorname{div}\nabla u$ heißt das: Das Gradientenfeld einer harmonischen Funktion hat nirgends eine Quelle oder eine Senke.

⁠**Beispiel:** $u(x,y)=x^2-y^2$ ist harmonisch, denn $\Delta u=2-2=0$. Die Funktion $x^2+y^2$ ist es nicht, denn $\Delta(x^2+y^2)=4$.

:::hintergrund Harmonisch heißt: keine Mulden und keine Kuppen
Nach dem Hintergrund zum Laplace-Operator misst $\Delta u(\boldsymbol{x})$, um wie viel der Mittelwert der Nachbarn über dem Wert in $\boldsymbol{x}$ liegt. Bei einer harmonischen Funktion ist diese Abweichung in führender Ordnung null: Sie liegt in jedem Punkt auf dem Mittelwert ihrer nächsten Umgebung. Die Sattelfläche $x^2-y^2$ zeigt, wie das aussieht: Längs der $x$-Achse steigt sie nach beiden Seiten, längs der $y$-Achse fällt sie nach beiden Seiten, und im Mittel der vier Nachbarn $(\pm a,0)$, $(0,\pm a)$ ergibt sich genau der Wert $0$ der Mitte. Ein elektrisches Potential in einem Bereich ohne Ladungen verhält sich so.
:::

⁠**Kurz gesagt:** Harmonisch heißt $\Delta u=0$: Der Gradient hat keine Quellen und Senken.

### Die Produktregel der Divergenz

<span class="anker" id="stufe-3-9"></span>

Viele Felder sind das Produkt aus einer skalaren Funktion und einem einfachen Feld, etwa $\frac{f(r)}r\,\boldsymbol{x}$. Die Divergenz eines solchen Produkts lässt sich aus den Teilen berechnen.

:::satz Satz 3.4 (Produktregel der Divergenz)
<span class="anker" id="satz-3-4"></span>

Für eine differenzierbare Funktion $\varphi$ und ein differenzierbares Vektorfeld $\boldsymbol{F}$ auf einer offenen Menge des $\mathbb{R}^n$ gilt

$$\operatorname{div}(\varphi\boldsymbol{F})=\nabla\varphi\cdot\boldsymbol{F}+\varphi\,\operatorname{div}\boldsymbol{F} .$$
:::

:::beweis Produktregel einer Variablen in jedem Summanden
Komponente $j$ von $\varphi\boldsymbol{F}$ ist $\varphi F_j$. Mit der gewöhnlichen Produktregel ist

$$\operatorname{div}(\varphi\boldsymbol{F})=\sum_{j=1}^n\frac{\partial(\varphi F_j)}{\partial x_j}=\sum_{j=1}^n\frac{\partial\varphi}{\partial x_j}F_j+\varphi\sum_{j=1}^n\frac{\partial F_j}{\partial x_j}=\nabla\varphi\cdot\boldsymbol{F}+\varphi\,\operatorname{div}\boldsymbol{F} .$$
:::

⁠**Beispiel:** $\varphi=x$ und $\boldsymbol{F}=(y,\,x)$ in der Ebene. Direkt: $\operatorname{div}(xy,\;x^2)=y+0=y$. Mit der Regel: $\nabla x\cdot\boldsymbol{F}=(1,0)\cdot(y,x)=y$ und $x\,\operatorname{div}(y,x)=x\cdot0=0$, zusammen $y$.

⁠**Kurz gesagt:** Die Divergenz eines Produkts ist „Gradient des Skalars mal Feld“ plus „Skalar mal Divergenz des Felds“.

### Die Divergenz radialsymmetrischer Felder

<span class="anker" id="stufe-3-10"></span>

Wie stark strömt ein radialsymmetrisches Feld $f(r)\,\hat{\boldsymbol{e}}_r$ auseinander? Zwei Dinge spielen mit: Die Pfeile können nach außen länger werden, und radiale Pfeile laufen schon bei gleicher Länge auseinander, weil die Kugelflächen nach außen größer werden.

:::satz Satz 3.5 (Divergenz radialsymmetrischer Felder)
<span class="anker" id="satz-3-5"></span>

Sei $f\colon(0,\infty)\to\mathbb{R}$ stetig differenzierbar und $\boldsymbol{E}(\boldsymbol{x})=f(r)\,\hat{\boldsymbol{e}}_r$ mit $r=|\boldsymbol{x}|$. Dann gilt auf $\mathbb{R}^n\setminus\{0\}$

<span class="anker" id="gl-3-3"></span>
$$\operatorname{div}\boldsymbol{E}=f'(r)+(n-1)\,\frac{f(r)}{r}. \tag{3.3}$$
:::

:::beweis Skalar mal Strahlfeld
Man schreibt das Feld als Produkt einer skalaren Funktion mit dem Strahlfeld:

$$\boldsymbol{E}(\boldsymbol{x})=\frac{f(r)}{r}\,\boldsymbol{x},\qquad\text{also}\qquad\varphi(\boldsymbol{x})=\frac{f(r)}{r},\quad\boldsymbol{F}(\boldsymbol{x})=\boldsymbol{x} .$$

Die Produktregel (Satz [3.4](#satz-3-4)) braucht drei Bausteine.

<ol class="rm">

<li>

$\operatorname{div}\boldsymbol{F}=\operatorname{div}\boldsymbol{x}=n$, denn jede der $n$ Ableitungen $\partial x_j/\partial x_j$ ist $1$.

</li>

<li>

$\varphi$ ist radialsymmetrisch mit dem Profil $f(r)/r$. Nach [(2.2)](radialsymmetrische-funktionen-und-felder.html#gl-2-2) und der Quotientenregel ist

$$\nabla\varphi=\frac{\mathrm{d}}{\mathrm{d} r}\Bigl(\frac{f(r)}{r}\Bigr)\hat{\boldsymbol{e}}_r=\frac{f'(r)\,r-f(r)}{r^2}\,\hat{\boldsymbol{e}}_r .$$

</li>

<li>

Wegen $\hat{\boldsymbol{e}}_r\cdot\boldsymbol{x}=\frac{\boldsymbol{x}\cdot\boldsymbol{x}}{r}=\frac{r^2}r=r$ ist $\nabla\varphi\cdot\boldsymbol{F}=\dfrac{f'(r)\,r-f(r)}{r^2}\cdot r=\dfrac{f'(r)\,r-f(r)}{r}$.

</li>

</ol>

Zusammen:

$$\operatorname{div}\boldsymbol{E}=\frac{f'(r)\,r-f(r)}{r}+n\,\frac{f(r)}{r}=f'(r)+(n-1)\,\frac{f(r)}{r}.$$
:::

⁠**So liest man das:** Der Summand $f'$ zählt, wie stark die Pfeillänge nach außen zunimmt. Der Summand $(n-1)f/r$ zählt, dass radiale Pfeile schon bei gleicher Länge auseinanderlaufen. **Kontrolle:** Für das Strahlfeld $\boldsymbol{E}=\boldsymbol{x}$ ist $f(r)=r$, und [(3.3)](#gl-3-3) gibt $1+(n-1)=n$, wie direkt berechnet. Für $n=1$ bleibt nur $f'$, denn auf einer Geraden können Pfeile nicht zur Seite auseinanderlaufen.

⁠**Kurz gesagt:** Die Divergenz von $f(r)\,\hat{\boldsymbol{e}}_r$ ist $f'(r)+(n-1)f(r)/r$: Wachstum der Pfeile plus Auseinanderlaufen.

### Das Coulomb-Potential ist harmonisch

<span class="anker" id="stufe-3-11"></span>

Das Feld einer Punktladung zeigt nach außen. Hat es außerhalb der Ladung Quellen? Die Formel aus dem letzten Unterabschnitt beantwortet das sofort.

Für das Coulomb-Potential $u=\frac{Q}{4\pi r}$ auf $\mathbb{R}^3\setminus\{0\}$ ist nach Unterabschnitt [2.6](radialsymmetrische-funktionen-und-felder.html#stufe-2-6)

$$\boldsymbol{E}(\boldsymbol{x})=-\nabla u(\boldsymbol{x})=\frac{Q}{4\pi r^2}\,\hat{\boldsymbol{e}}_r .$$

Mit $n=3$ und $f(r)=\frac{Q}{4\pi r^2}$, also $f'(r)=-\frac{Q}{2\pi r^3}$, liefert [(3.3)](#gl-3-3)

$$-\Delta u=\operatorname{div}\boldsymbol{E}=-\frac{Q}{2\pi r^3}+2\cdot\frac{Q}{4\pi r^3}=0\qquad\text{in }\mathbb{R}^3\setminus\{0\}.$$

Das Coulomb-Potential ist also harmonisch, und sein Feld hat außerhalb des Nullpunkts keine Quellen. Allgemein ist [(3.3)](#gl-3-3) genau dann null, wenn $f'=-(n-1)f/r$ gilt, also für $f(r)=c\,r^{-(n-1)}$ mit einer Konstanten $c$. In drei Dimensionen ist demnach genau der Abfall mit $1/r^2$ quellenfrei.

:::hintergrund Das Feld strömt sichtbar nach außen. Warum ist die Divergenz trotzdem null?
Weil die Divergenz eine örtliche Bilanz ist. Man denke sich wieder eine Strömung und betrachte eine Kugelfläche mit dem Radius $r$ um den Nullpunkt. Das Feld steht überall senkrecht auf ihr und hat dort die feste Länge $\frac{Q}{4\pi r^2}$. Durch die ganze Kugelfläche mit dem Inhalt $4\pi r^2$ tritt also pro Zeit die Menge $4\pi r^2\cdot\frac{Q}{4\pi r^2}=Q$ nach außen, für jeden Radius dieselbe. Was durch die innere von zwei Kugelflächen hinausfließt, kommt also vollständig durch die äußere wieder heraus: Zwischen ihnen entsteht nichts und verschwindet nichts. Die Pfeile werden nach außen kürzer, verteilen sich aber auf eine größere Fläche, und beides hebt sich genau auf, weil der Flächeninhalt mit $r^2$ wächst und das Feld mit $1/r^2$ fällt. In $n$ Dimensionen wächst der Inhalt einer Kugelfläche mit $r^{n-1}$, deshalb ist dort $r^{-(n-1)}$ der quellenfreie Abfall. Die Quelle des Felds sitzt im Nullpunkt, und der gehört nicht zum betrachteten Bereich.
:::

⁠**Kurz gesagt:** Außerhalb der Ladung ist $\Delta\frac{Q}{4\pi r}=0$. In drei Dimensionen ist genau das $1/r^2$-Feld quellenfrei.

### Die Rotation im Raum

<span class="anker" id="stufe-3-12"></span>

Die Divergenz benutzt nur die Diagonale der Jacobi-Matrix. Die Einträge daneben tragen eine andere Information: ob das Feld an einer Stelle kreist, wie Wasser in einem Strudel.

Man betrachtet ein kleines Quadrat in der $x_1$-$x_2$-Ebene. Ist $E_2$ an der rechten Kante größer als an der linken, schiebt das Feld die rechte Kante stärker nach oben als die linke: Das Quadrat wird gegen den Uhrzeigersinn gedreht. Dasselbe bewirkt ein $E_1$, das an der oberen Kante kleiner ist als an der unteren. Die Neigung, um die $x_3$-Achse zu drehen, ist also $\partial E_2/\partial x_1-\partial E_1/\partial x_2$. Für die beiden anderen Achsen gilt dasselbe mit vertauschten Indizes.

:::definition Definition 3.6 (Rotation im Raum)
<span class="anker" id="satz-3-6"></span>

Sei $\mathcal U\subset\mathbb{R}^3$ offen und $\boldsymbol{E}=(E_1,E_2,E_3)$ ein differenzierbares Vektorfeld auf $\mathcal U$. Die __Rotation__ von $\boldsymbol{E}$ ist

<span class="anker" id="gl-3-4"></span>
$$\operatorname{rot}\boldsymbol{E}:=\nabla\times\boldsymbol{E}=\begin{pmatrix}\dfrac{\partial E_3}{\partial x_2}-\dfrac{\partial E_2}{\partial x_3}\\[8pt]\dfrac{\partial E_1}{\partial x_3}-\dfrac{\partial E_3}{\partial x_1}\\[8pt]\dfrac{\partial E_2}{\partial x_1}-\dfrac{\partial E_1}{\partial x_2}\end{pmatrix}. \tag{3.4}$$

Die englische Bezeichnung für $\operatorname{rot}\boldsymbol{E}$ ist $\operatorname{curl}\boldsymbol{E}$.
:::

⁠**So liest man das:** Die Schreibweise $\nabla\times\boldsymbol{E}$ ist das formale Kreuzprodukt von Nabla mit $\boldsymbol{E}$: Man setzt in die Formel des Kreuzprodukts $a_j=\partial/\partial x_j$ und $b_k=E_k$ ein. Die Rotation macht aus einem Vektorfeld wieder ein Vektorfeld, sie ist ein Differentialoperator erster Ordnung. Die Komponente $i$ ist ein Maß für die örtliche __Wirbeldichte__ des Felds um die $x_i$-Achse.

⁠**Beispiel 1:** Für $\boldsymbol{E}=(0,\,0,\,xy)$ ist $\operatorname{rot}\boldsymbol{E}=(x-0,\;0-y,\;0-0)=(x,\,-y,\,0)$.

⁠**Beispiel 2:** Eine starre Drehung um die $x_3$-Achse mit der Winkelgeschwindigkeit $\Omega$ hat das Geschwindigkeitsfeld $\boldsymbol{E}=\Omega\,(-x_2,\,x_1,\,0)$. Ihre Rotation ist $\operatorname{rot}\boldsymbol{E}=(0-0,\;0-0,\;\Omega+\Omega)=(0,0,2\Omega)$: Sie zeigt längs der Drehachse und ist doppelt so lang wie die Winkelgeschwindigkeit.

:::hintergrund Warum die Rotation die Wirbeldichte ist: Umlauf um ein kleines Quadrat
Man denke sich $\boldsymbol{E}$ als Strömung und lege in die $x_1$-$x_2$-Ebene ein kleines Quadrat mit der Seitenlänge $a$ und der linken unteren Ecke $\boldsymbol{x}$. Man umläuft es gegen den Uhrzeigersinn und addiert für jede Kante „Komponente des Felds längs der Kante mal Kantenlänge“, mit Minuszeichen, wo die Kante gegen eine Achse läuft. Diese Summe misst, wie stark die Strömung um das Quadrat herumschiebt; man nennt sie die *Zirkulation*. Nimmt man das Feld auf jeder Kante an einer Ecke, ergibt sich

$$\begin{aligned} &a\,E_1(\boldsymbol{x})+a\,E_2(\boldsymbol{x}+a\hat{\boldsymbol{e}}_1)-a\,E_1(\boldsymbol{x}+a\hat{\boldsymbol{e}}_2)-a\,E_2(\boldsymbol{x})\\ &\qquad=a^2\Bigl(\frac{E_2(\boldsymbol{x}+a\hat{\boldsymbol{e}}_1)-E_2(\boldsymbol{x})}{a}-\frac{E_1(\boldsymbol{x}+a\hat{\boldsymbol{e}}_2)-E_1(\boldsymbol{x})}{a}\Bigr). \end{aligned}$$

Teilt man durch den Flächeninhalt $a^2$ und lässt $a\to0$ gehen, werden die Brüche zu partiellen Ableitungen, und es bleibt $\partial E_2/\partial x_1-\partial E_1/\partial x_2$, die dritte Komponente von $\operatorname{rot}\boldsymbol{E}$. Für ein stetig differenzierbares Feld wird die Näherung dabei exakt. Die Rotation ist also „Umlauf pro Fläche“, und die Komponente $i$ gehört zu einem kleinen Quadrat senkrecht zur $x_i$-Achse. Ein Feld kann gleichmäßig in eine Richtung strömen und trotzdem Rotation haben, wenn es auf der einen Seite des Quadrats schneller ist als auf der anderen. Bei der starren Drehung dreht sich jedes kleine Flüssigkeitsteilchen mit $\Omega$ um sich selbst, und die Rotation ist $2\Omega$: Allgemein ist die halbe Rotation die Winkelgeschwindigkeit, mit der sich ein winziges Teilchen der Strömung um sich selbst dreht.
:::

:::analogie
Halte ein winziges Schaufelrad in die Strömung. Dreht es sich, wirbelt das Feld an dieser Stelle, und $\operatorname{rot}\boldsymbol{E}$ zeigt längs der Drehachse: Krümmt man die Finger der rechten Hand in Drehrichtung des Rads, zeigt der Daumen in Richtung von $\operatorname{rot}\boldsymbol{E}$. Das Bild stimmt nur, solange das Rad sehr klein ist, und es sagt nichts über Quellen.
:::

:::hintergrund Gibt es die Rotation auch für Felder mit mehr als drei Komponenten?
Hängt ein Feld $\boldsymbol{E}(\boldsymbol{x},t)$ zusätzlich von der Zeit ab, stellt sich die Frage gar nicht: Das Feld hat vier Eingänge, aber nur drei Ausgänge. Die Rotation leitet nur nach $x_1,x_2,x_3$ ab, die Zeit $t$ bleibt dabei fest. Für zwei Vektoren mit $n\ge4$ Komponenten gibt es das Kreuzprodukt in dieser Form nicht, denn senkrecht zu beiden steht dort mehr als eine Richtung. Was bleibt, sind die Zahlen $a_jb_k-a_kb_j$ für jedes Paar $j<k$, je eine pro Koordinatenebene, zusammen $n(n-1)/2$ Stück. Nur für $n=3$ sind das drei, und deshalb passen sie dort in einen Vektor.
:::

⁠**Kurz gesagt:** Die Rotation $\nabla\times\boldsymbol{E}$ ist ein Vektorfeld; ihre Komponente $i$ misst, wie stark das Feld um die $x_i$-Achse kreist.

### Levi-Civita-Symbole

<span class="anker" id="stufe-3-13"></span>

Die drei Komponenten des Kreuzprodukts und der Rotation folgen einem Muster: Jede Komponente $i$ benutzt die beiden anderen Indizes, einmal mit Plus, einmal mit Minus. Ein Symbol, das nur dieses Vorzeichen festhält, fasst alle drei Komponenten in einer Formel zusammen.

Man stellt die Zahlen $1,2,3$ im Kreis auf. Liest man drei verschiedene Indizes in Pfeilrichtung $1\to2\to3\to1$, gibt es ein Plus, gegen die Pfeilrichtung ein Minus. Kommt ein Index doppelt vor, gibt es null.

:::definition Definition 3.7 (Levi-Civita-Symbole)
<span class="anker" id="satz-3-7"></span>

Mit den Einheitsvektoren $\hat{\boldsymbol{e}}_1,\hat{\boldsymbol{e}}_2,\hat{\boldsymbol{e}}_3$ des $\mathbb{R}^3$ heißen die Zahlen

<span class="anker" id="gl-3-5"></span>
$$\varepsilon_{ijk}=\hat{\boldsymbol{e}}_i\cdot(\hat{\boldsymbol{e}}_j\times\hat{\boldsymbol{e}}_k)\in\{-1,0,1\},\qquad i,j,k\in\{1,2,3\}, \tag{3.5}$$

die __Levi-Civita-Symbole__.
:::

⁠**So liest man das:** Es ist $\varepsilon_{123}=\hat{\boldsymbol{e}}_1\cdot\hat{\boldsymbol{e}}_1=1$. Zyklisches Vertauschen ändert nichts: $\varepsilon_{123}=\varepsilon_{231}=\varepsilon_{312}=1$. Das Vertauschen zweier Indizes wechselt das Vorzeichen: $\varepsilon_{213}=\varepsilon_{132}=\varepsilon_{321}=-1$. Kommt ein Index doppelt vor, ist $\varepsilon_{ijk}=0$, denn dann ist $\hat{\boldsymbol{e}}_j\times\hat{\boldsymbol{e}}_k$ null oder steht senkrecht auf $\hat{\boldsymbol{e}}_i$. Damit gilt für das Kreuzprodukt und die Rotation

<span class="anker" id="gl-3-6"></span>
$$(\boldsymbol a\times\boldsymbol b)_i=\sum_{j,k=1}^3\varepsilon_{ijk}\,a_jb_k,\qquad(\operatorname{rot}\boldsymbol{F})_i=\sum_{j,k=1}^3\varepsilon_{ijk}\,\frac{\partial F_k}{\partial x_j}. \tag{3.6}$$

⁠**Beispiel:** Für $i=1$ sind in der Summe nur $(j,k)=(2,3)$ mit $\varepsilon_{123}=1$ und $(j,k)=(3,2)$ mit $\varepsilon_{132}=-1$ von null verschieden. Es bleibt $(\operatorname{rot}\boldsymbol{F})_1=\partial F_3/\partial x_2-\partial F_2/\partial x_3$, die erste Zeile von [(3.4)](#gl-3-4).

:::hintergrund Warum ein Vorzeichen genügt, um das Kreuzprodukt zu beschreiben
$\varepsilon_{ijk}$ ist die Determinante $\det(\hat{\boldsymbol{e}}_i|\hat{\boldsymbol{e}}_j|\hat{\boldsymbol{e}}_k)$, also der orientierte Rauminhalt des Würfels aus drei Einheitsvektoren. Er ist $\pm1$, wenn die drei verschieden sind, mit Plus genau dann, wenn sie wie die Finger der rechten Hand liegen, und $0$, wenn zwei gleich sind. Das Kreuzprodukt ist in jedem Faktor linear: $\boldsymbol a\times\boldsymbol b=\sum_{j,k}a_jb_k\,(\hat{\boldsymbol{e}}_j\times\hat{\boldsymbol{e}}_k)$. Es genügt also, die Kreuzprodukte der Einheitsvektoren zu kennen, und deren Komponente $i$ ist genau $\varepsilon_{ijk}$. Die ganze Rechenregel des Kreuzprodukts steckt damit in den $27$ Zahlen $\varepsilon_{ijk}$, von denen nur sechs nicht null sind.
:::

⁠**Kurz gesagt:** $\varepsilon_{ijk}$ ist $+1$ für $1,2,3$ in zyklischer Reihenfolge, $-1$ dagegen und $0$ bei doppeltem Index. Damit schreibt man Kreuzprodukt und Rotation als eine Summe.

### Die Rotation als Determinante

<span class="anker" id="stufe-3-14"></span>

Die Formel [(3.4)](#gl-3-4) muss man sich nicht Zeile für Zeile merken. Eine Determinante mit Einheitsvektoren und Ableitungsbefehlen erzeugt sie.

Als Merkregel dient

<span class="anker" id="gl-3-7"></span>
$$\operatorname{rot}\boldsymbol{F}=\det\begin{pmatrix}\hat{\boldsymbol{e}}_1&\dfrac{\partial}{\partial x_1}&F_1\\[6pt]\hat{\boldsymbol{e}}_2&\dfrac{\partial}{\partial x_2}&F_2\\[6pt]\hat{\boldsymbol{e}}_3&\dfrac{\partial}{\partial x_3}&F_3\end{pmatrix}. \tag{3.7}$$

Diese „Determinante“ ist keine Zahl, sondern eine Rechenvorschrift. Man entwickelt formal nach der ersten Spalte, wie in Unterabschnitt [3.2](#stufe-3-2), und lässt jeden Ableitungsbefehl auf das $F$ wirken, das im selben Produkt steht.

⁠**Beispiel:** Für das Drehfeld $\boldsymbol{F}=(-y,\,x,\,0)$ im Raum:

$$\operatorname{rot}\boldsymbol{F}=\hat{\boldsymbol{e}}_1\Bigl(\frac{\partial0}{\partial y}-\frac{\partial x}{\partial z}\Bigr)-\hat{\boldsymbol{e}}_2\Bigl(\frac{\partial0}{\partial x}-\frac{\partial(-y)}{\partial z}\Bigr)+\hat{\boldsymbol{e}}_3\Bigl(\frac{\partial x}{\partial x}-\frac{\partial(-y)}{\partial y}\Bigr)=(0,\,0,\,2).$$

⁠**Kurz gesagt:** Die Rotation ist eine formale Determinante aus Einheitsvektoren, Ableitungsbefehlen und Komponenten, entwickelt nach der ersten Spalte.

### Die Rotation in der Ebene

<span class="anker" id="stufe-3-15"></span>

Ein ebenes Feld kann nur um eine einzige Achse kreisen, die senkrecht auf der Ebene steht. Deshalb genügt in der Ebene eine Zahl.

Betrachtet man im Raum ein Feld der Form $\boldsymbol{E}=(E_1,E_2,0)$, das nicht von $x_3$ abhängt, dann sind in [(3.4)](#gl-3-4) alle Ableitungen nach $x_3$ und alle Ableitungen von $E_3$ null. Es bleibt

$$\operatorname{rot}\boldsymbol{E}=\Bigl(0,\;0,\;\frac{\partial E_2}{\partial x_1}-\frac{\partial E_1}{\partial x_2}\Bigr)^T .$$

Ein solches Feld kann man mit dem ebenen Feld $(E_1,E_2)$ gleichsetzen. Das legt die folgende Definition nahe.

:::definition Definition 3.8 (Rotation in der Ebene)
<span class="anker" id="satz-3-8"></span>

Sei $\mathcal U\subset\mathbb{R}^2$ offen und $\boldsymbol{E}=(E_1,E_2)$ ein differenzierbares Vektorfeld auf $\mathcal U$. Die __Rotation in der Ebene__ von $\boldsymbol{E}$ ist die skalare Funktion

<span class="anker" id="gl-3-8"></span>
$$\operatorname{rot}\boldsymbol{E}=\frac{\partial E_2}{\partial x_1}-\frac{\partial E_1}{\partial x_2}. \tag{3.8}$$
:::

In der Ebene sind Divergenz und Rotation also beide skalare Funktionen. Ein positiver Wert heißt: Das Feld kreist dort gegen den Uhrzeigersinn.

⁠**Beispiele:** Das Drehfeld hat $\operatorname{rot}(-y,x)=1-(-1)=2$. Das Strahlfeld hat $\operatorname{rot}(x,y)=0-0=0$. Das *Scherfeld* $\boldsymbol G=(y,0)$ hat $\operatorname{rot}\boldsymbol G=0-1=-1$, obwohl alle seine Pfeile parallel nach rechts oder links zeigen (Abb. [13](#abb-13)): Die obere Kante eines kleinen Quadrats wird nach rechts gezogen, die untere nach links, und das dreht das Quadrat im Uhrzeigersinn. Das Gradientenfeld $(2x,4y)$ hat $\operatorname{rot}(2x,4y)=0-0=0$.

:::abbildung hm3/k1wirbel 13
Dreht man das Strahlfeld $\boldsymbol{F}=(x,y)$ um einen rechten Winkel, wird aus der Quelle ein Wirbel: $\boldsymbol{F}^\perp$ ist das Drehfeld. Rechts das Scherfeld $\boldsymbol G=(y,0)$: Alle Pfeile laufen parallel, trotzdem ist die Rotation nicht null, weil die obere Kante eines Quadrats nach rechts und die untere nach links gezogen wird.
:::

:::hintergrund Kreisende Feldlinien und Rotation sind zweierlei
Die Rotation ist eine örtliche Größe, wie die Divergenz. Das Scherfeld $(y,0)$ hat gerade Feldlinien und trotzdem überall $\operatorname{rot}=-1$. Umgekehrt kann ein Feld auf Kreisen umlaufen und trotzdem $\operatorname{rot}=0$ haben, wenn es nach außen gerade richtig schwächer wird. Ein Beispiel ist $\boldsymbol{H}(x,y)=\dfrac{(-y,\,x)}{x^2+y^2}$ auf $\mathbb{R}^2\setminus\{0\}$. Seine Feldlinien sind Kreise um den Nullpunkt, aber es ist

$$\frac{\partial}{\partial x}\Bigl(\frac{x}{x^2+y^2}\Bigr)=\frac{y^2-x^2}{(x^2+y^2)^2},\qquad\frac{\partial}{\partial y}\Bigl(\frac{-y}{x^2+y^2}\Bigr)=\frac{y^2-x^2}{(x^2+y^2)^2},$$

und die Differenz, also $\operatorname{rot}\boldsymbol{H}$, ist null. Ein kleines Schaufelrad, das auf einem Kreis um den Nullpunkt mitschwimmt, wird auf seiner Innenseite schneller angeströmt als auf seiner Außenseite. Das dreht es im Uhrzeigersinn um sich selbst, und genau so viel, wie der Umlauf auf dem gekrümmten Weg es gegen den Uhrzeigersinn dreht.
:::

⁠**Kurz gesagt:** In der Ebene ist die Rotation die Zahl $\partial E_2/\partial x_1-\partial E_1/\partial x_2$, die dritte Komponente der räumlichen Rotation.

### Drehen um einen rechten Winkel vertauscht Divergenz und Rotation

<span class="anker" id="stufe-3-16"></span>

In Abb. [13](#abb-13) wird aus dem Strahlfeld, einer Quelle, durch Drehen jedes Pfeils das Drehfeld, ein Wirbel. Das ist ein allgemeines Gesetz der Ebene.

Dreht man jeden Pfeil eines Felds $\boldsymbol{F}=(F_1,F_2)$ um $\pi/2$ gegen den Uhrzeigersinn, entsteht das Feld

$$\boldsymbol{F}^\perp=(-F_2,\;F_1).$$

Was vorher senkrecht durch eine Kante eines kleinen Quadrats strömte, strömt danach längs dieser Kante. Aus Hinaus- und Hineinströmen wird Herumströmen, und umgekehrt.

:::satz Satz 3.9 (Divergenz und Rotation unter Drehung)
<span class="anker" id="satz-3-9"></span>

Für ein differenzierbares Vektorfeld $\boldsymbol{F}=(F_1,F_2)$ in der Ebene gilt

<span class="anker" id="gl-3-9"></span>
$$\operatorname{div}\boldsymbol{F}=\operatorname{rot}\boldsymbol{F}^\perp,\qquad\operatorname{div}\boldsymbol{F}^\perp=-\operatorname{rot}\boldsymbol{F} . \tag{3.9}$$
:::

:::beweis Einsetzen
Mit $\boldsymbol{F}^\perp=(-F_2,F_1)$ ist

$$\operatorname{rot}\boldsymbol{F}^\perp=\frac{\partial F_1}{\partial x_1}-\frac{\partial(-F_2)}{\partial x_2}=\frac{\partial F_1}{\partial x_1}+\frac{\partial F_2}{\partial x_2}=\operatorname{div}\boldsymbol{F},\qquad \operatorname{div}\boldsymbol{F}^\perp=\frac{\partial(-F_2)}{\partial x_1}+\frac{\partial F_1}{\partial x_2}=-\operatorname{rot}\boldsymbol{F} .$$
:::

⁠**Beispiel:** Das Strahlfeld $\boldsymbol{F}=(x,y)$ hat $\operatorname{div}\boldsymbol{F}=2$ und $\operatorname{rot}\boldsymbol{F}=0$. Sein gedrehtes Feld $\boldsymbol{F}^\perp=(-y,x)$ ist das Drehfeld mit $\operatorname{rot}\boldsymbol{F}^\perp=2$ und $\operatorname{div}\boldsymbol{F}^\perp=0$, wie [(3.9)](#gl-3-9) verlangt.

⁠**Kurz gesagt:** In der Ebene werden Divergenz und Rotation durch Drehen der Pfeile um einen rechten Winkel ineinander überführt.

### Eine Rotation für jede Dimension

<span class="anker" id="stufe-3-17"></span>

Die Rotation wurde im Raum und in der Ebene getrennt erklärt. In beiden Fällen besteht sie aus Differenzen $\partial F_k/\partial x_j-\partial F_j/\partial x_k$. Diese Differenzen gibt es in jeder Dimension, und man sammelt sie in einer Matrix.

:::definition Definition 3.10 (Wirbelmatrix)
<span class="anker" id="satz-3-10"></span>

Für ein differenzierbares Vektorfeld $\boldsymbol{F}=(F_1,\dots,F_n)$ auf einer offenen Menge des $\mathbb{R}^n$ sei

<span class="anker" id="gl-3-10"></span>
$$\omega_{jk}=\frac12\Bigl(\frac{\partial F_k}{\partial x_j}-\frac{\partial F_j}{\partial x_k}\Bigr),\qquad1\le j,k\le n. \tag{3.10}$$

Die Matrix $(\omega_{jk})_{jk}$ heißt in diesem Kapitel die __Wirbelmatrix__ von $\boldsymbol{F}$.
:::

⁠**So liest man das:** Vertauscht man $j$ und $k$, wechselt das Vorzeichen: Die Matrix ist schiefsymmetrisch. Der Eintrag $\partial F_k/\partial x_j$ steht in der Jacobi-Matrix an der Stelle $(k,j)$, also in ihrer Transponierten an der Stelle $(j,k)$. Deshalb ist $(\omega_{jk})$ der schiefsymmetrische Anteil der transponierten Jacobi-Matrix: $(\omega_{jk})=\frac12\bigl((D\boldsymbol{F})^T-D\boldsymbol{F}\bigr)$. Für $n=3$ und $n=2$ erhält man die Rotation zurück:

<span class="anker" id="gl-3-11"></span>
$$(\operatorname{rot}\boldsymbol{F})_i=\sum_{j,k=1}^3\varepsilon_{ijk}\,\omega_{jk}\quad(n=3),\qquad\operatorname{rot}\boldsymbol{F}=\sum_{j,k=1}^2\varepsilon_{jk}\,\omega_{jk}\quad(n=2). \tag{3.11}$$

Dabei sind $\varepsilon_{12}=1$, $\varepsilon_{21}=-1$ und $\varepsilon_{11}=\varepsilon_{22}=0$ die Levi-Civita-Symbole der Ebene. Für $i=3$ etwa bleiben $\omega_{12}-\omega_{21}=2\omega_{12}=\partial F_2/\partial x_1-\partial F_1/\partial x_2$; das ist die dritte Zeile von [(3.4)](#gl-3-4). Die Wirbelmatrix hat $n(n-1)/2$ Einträge oberhalb der Diagonale, die übrigen folgen aus der Schiefsymmetrie. Nur für $n=3$ sind das drei und passen in einen Vektor.

⁠**Beispiel:** Für das Drehfeld $(-y,x)$ ist $\omega_{12}=\frac12(1-(-1))=1$ und $\omega_{21}=-1$, also $\operatorname{rot}=\varepsilon_{12}\omega_{12}+\varepsilon_{21}\omega_{21}=1+1=2$.

⁠**Kurz gesagt:** Die Wirbelmatrix ist der schiefsymmetrische Anteil der transponierten Jacobi-Matrix. In drei und zwei Dimensionen enthält sie genau die Rotation.

### Die Integrabilitätsbedingungen

<span class="anker" id="stufe-3-18"></span>

Nach Satz [1.15](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#satz-1-15) hat ein Gradientenfeld eine symmetrische Jacobi-Matrix. Eine symmetrische Matrix hat keinen schiefsymmetrischen Anteil. Also verschwindet bei einem Gradientenfeld die Wirbelmatrix, und mit ihr die Rotation.

:::satz Satz 3.11 (Integrabilitätsbedingungen)
<span class="anker" id="satz-3-11"></span>

Sei $\boldsymbol{F}=\nabla\varphi$ ein Gradientenfeld mit einem zweimal stetig differenzierbaren Skalarpotential $\varphi$.

<ol class="rm">

<li>

Dann gelten die __Integrabilitätsbedingungen__

<span class="anker" id="gl-3-12"></span>
$$\frac{\partial F_k}{\partial x_j}=\frac{\partial F_j}{\partial x_k}\qquad\text{für alle }1\le j,k\le n, \tag{3.12}$$

also $\omega_{jk}=0$ für alle $j,k$.

</li>

<li>

Für $n=2$ und $n=3$ ist das Feld __rotationsfrei__: $\operatorname{rot}\nabla\varphi=0$.

</li>

</ol>
:::

:::beweis Lemma von Schwarz
(i) Es ist $F_k=\partial\varphi/\partial x_k$, und nach dem Lemma von Schwarz gilt

$$\frac{\partial F_k}{\partial x_j}=\frac{\partial^2\varphi}{\partial x_j\,\partial x_k}=\frac{\partial^2\varphi}{\partial x_k\,\partial x_j}=\frac{\partial F_j}{\partial x_k}.$$

(ii) Nach (i) sind alle $\omega_{jk}=0$, und nach [(3.11)](#gl-3-11) ist dann auch die Rotation null. Für die erste Komponente im Raum ausgeschrieben: $(\operatorname{rot}\nabla\varphi)_1=\frac{\partial^2\varphi}{\partial x_2\,\partial x_3}-\frac{\partial^2\varphi}{\partial x_3\,\partial x_2}=0$.
:::

Die Bedingung $\operatorname{rot}\boldsymbol{F}=0$ ist also *notwendig* dafür, dass ein stetig differenzierbares Feld ein Gradientenfeld ist. Der Name kommt daher, dass man ein Gradientenfeld zu seinem Potential „integrieren“ kann; die Bedingungen sagen, wann das überhaupt in Frage kommt.

⁠**Beispiel:** Für $\boldsymbol{F}=(y+2xz,\;x+z^2,\;x^2+2yz)$ im Raum sind die drei Bedingungen $\partial F_2/\partial x=1=\partial F_1/\partial y$, $\partial F_3/\partial x=2x=\partial F_1/\partial z$ und $\partial F_3/\partial y=2z=\partial F_2/\partial z$ erfüllt, also $\operatorname{rot}\boldsymbol{F}=0$. Für das Feld $(y,\;2x,\;z)$ ist dagegen $\partial F_2/\partial x=2$, aber $\partial F_1/\partial y=1$; es kann kein Gradientenfeld sein.

:::hintergrund Woher die Bedingung kommt, anschaulich und in $n$ Dimensionen
Rechnerisch aus der Vertauschbarkeit zweiter Ableitungen, siehe den Beweis. Anschaulich: Man läuft um ein kleines Rechteck mit den Seiten $a$ und $b$ in der Ebene, die von der $x_j$- und der $x_k$-Achse aufgespannt wird (Abb. [14](#abb-14)). Ist $\boldsymbol{F}=\nabla\varphi$, ändert sich das Potential längs einer kurzen Kante nach [(1.7)](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#gl-1-7) um ungefähr „Feldkomponente längs der Kante mal Kantenlänge“. Die vier Änderungen ergeben zusammen etwa $ab\,(\partial F_k/\partial x_j-\partial F_j/\partial x_k)$. Das muss null sein, denn ein geschlossener Weg führt zum selben Potentialwert zurück. Die Bedingung ist also ein Rundweg-Test im Kleinen: Ein Feld, das um ein winziges Rechteck herum etwas aufsammelt, kann keine Höhenkarte haben.

:::abbildung hm3/k1rechteck 14
Rundweg um ein kleines Rechteck mit den Ecken $P_0$, $P_1=P_0+a\,\hat{\boldsymbol{e}}_j$, $P_2=P_0+a\,\hat{\boldsymbol{e}}_j+b\,\hat{\boldsymbol{e}}_k$ und $P_3=P_0+b\,\hat{\boldsymbol{e}}_k$. An den Kanten stehen die Änderungen des Potentials. Ihre Summe ist $b\,\bigl(F_k(P_1)-F_k(P_0)\bigr)-a\,\bigl(F_j(P_3)-F_j(P_0)\bigr)$, also etwa $ab\,\bigl(\partial F_k/\partial x_j-\partial F_j/\partial x_k\bigr)$.
:::

Jedes Paar von Achsen spannt eine solche Ebene auf. Das ergibt $n(n-1)/2$ verschiedene Bedingungen: keine für $n=1$, eine für $n=2$, drei für $n=3$, nämlich die drei Komponenten von $\operatorname{rot}\boldsymbol{F}$, und sechs für $n=4$.
:::

⁠**Kurz gesagt:** Gradientenfelder erfüllen $\partial F_k/\partial x_j=\partial F_j/\partial x_k$; in Ebene und Raum heißt das $\operatorname{rot}\boldsymbol{F}=0$.

### Notwendig, aber nicht hinreichend

<span class="anker" id="stufe-3-19"></span>

Folgt umgekehrt aus $\operatorname{rot}\boldsymbol{F}=0$, dass $\boldsymbol{F}$ ein Gradientenfeld ist? Das ist eine Kernfrage der Vektoranalysis. Die Antwort lautet im Allgemeinen nein, und ein Beispiel zeigt, woran es liegt.

Das Feld $\boldsymbol{H}(x,y)=\dfrac{(-y,\,x)}{x^2+y^2}$ auf $\mathbb{R}^2\setminus\{0\}$ ist stetig differenzierbar. Es ist rotationsfrei, denn nach der Quotientenregel ist

$$\frac{\partial H_2}{\partial x}=\frac{\partial}{\partial x}\Bigl(\frac{x}{x^2+y^2}\Bigr)=\frac{y^2-x^2}{(x^2+y^2)^2},\qquad \frac{\partial H_1}{\partial y}=\frac{\partial}{\partial y}\Bigl(\frac{-y}{x^2+y^2}\Bigr)=\frac{y^2-x^2}{(x^2+y^2)^2},$$

und die Differenz, also $\operatorname{rot}\boldsymbol{H}$, ist null. Angenommen, es wäre $\boldsymbol{H}=\nabla\varphi$ auf $\mathbb{R}^2\setminus\{0\}$. Dann gäbe [(1.10)](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#gl-1-10) längs des Kreises $\gamma(t)=(\cos t,\sin t)$

$$\frac{\mathrm{d}}{\mathrm{d} t}\,\varphi\bigl(\gamma(t)\bigr)=\boldsymbol{H}\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)=(-\sin t,\cos t)\cdot(-\sin t,\cos t)=\sin^2t+\cos^2t=1 .$$

Nach einem Umlauf, von $t=0$ bis $t=2\pi$, wäre $\varphi$ um $2\pi$ gewachsen, obwohl man wieder am selben Punkt $(1,0)$ steht. Das ist unmöglich. Also hat $\boldsymbol{H}$ kein Skalarpotential auf $\mathbb{R}^2\setminus\{0\}$, obwohl $\operatorname{rot}\boldsymbol{H}=0$ ist.

Ob die Bedingung $\operatorname{rot}\boldsymbol{F}=0$ für ein Skalarpotential ausreicht, hängt also nicht nur vom Feld ab, sondern auch von der Menge, auf der es erklärt ist. Hier hat die Menge ein Loch, um das der Kreis herumläuft.

:::hintergrund Was im Beispiel schiefgeht: ein Potential, das nicht zusammenpasst
Für einen Punkt $(x,y)\neq(0,0)$ sei $\theta$ der Winkel, den der Pfeil vom Nullpunkt zu diesem Punkt mit der positiven $x$-Achse bildet, gegen den Uhrzeigersinn gemessen. Auf der rechten Halbebene $x>0$ ist $\theta=\arctan(y/x)$, und Ableiten gibt $\nabla\theta=\frac{(-y,\,x)}{x^2+y^2}=\boldsymbol{H}$. Örtlich ist $\boldsymbol{H}$ also durchaus ein Gradientenfeld, mit dem Winkel als Potential. Läuft man aber einmal um den Nullpunkt, wächst der Winkel um $2\pi$ und passt am Ende nicht mehr zum Anfangswert. Auf einer Menge, in der man den Nullpunkt nicht umrunden kann, etwa auf der rechten Halbebene, gibt es das Potential; auf $\mathbb{R}^2\setminus\{0\}$ gibt es keines. Die Rotationsfreiheit prüft nur kleine Rundwege, wie im Hintergrund zu den Integrabilitätsbedingungen. Ein großer Rundweg um ein Loch wird von ihr nicht erfasst.
:::

⁠**Kurz gesagt:** $\operatorname{rot}\boldsymbol{F}=0$ ist notwendig für ein Skalarpotential, aber nicht hinreichend: Auf einer Menge mit Loch kann ein rotationsfreies Feld ohne Potential sein.

### Ein Skalarpotential ausrechnen

<span class="anker" id="stufe-3-20"></span>

Sind die Integrabilitätsbedingungen erfüllt, sucht man das Potential. Man integriert Komponente für Komponente und prüft am Ende durch Ableiten.

Der Grund, warum das geht: Aus $\partial\varphi/\partial x=F_1$ ist $\varphi$ bis auf einen Summanden bestimmt, der nicht von $x$ abhängt, denn nur dessen Ableitung nach $x$ ist null. Die nächste Komponente legt diesen Summanden bis auf einen Teil fest, der weder von $x$ noch von $y$ abhängt, und so weiter.

⁠**Beispiel:** $\boldsymbol{F}=(y+2xz,\;x+z^2,\;x^2+2yz)$ aus dem letzten Unterabschnitt erfüllt die Integrabilitätsbedingungen.

<ol class="rm">

<li>

Aus $\partial\varphi/\partial x=y+2xz$ folgt $\varphi=xy+x^2z+c(y,z)$ mit einer noch unbekannten Funktion $c$ von $y$ und $z$.

</li>

<li>

Ableiten nach $y$ gibt $x+\partial c/\partial y$. Das muss $F_2=x+z^2$ sein, also $\partial c/\partial y=z^2$ und $c=yz^2+d(z)$.

</li>

<li>

Ableiten nach $z$ gibt $x^2+2yz+d'(z)$. Das muss $F_3=x^2+2yz$ sein, also $d'(z)=0$ und $d$ konstant.

</li>

</ol>

Ergebnis: $\varphi=xy+x^2z+yz^2+\text{konst}$. Kontrolle: $\nabla\varphi=(y+2xz,\;x+z^2,\;x^2+2yz)$.

⁠**Kurz gesagt:** Ein Skalarpotential findet man, indem man die erste Komponente integriert und die unbekannte Restfunktion mit den übrigen Komponenten festlegt.

### Aufgaben

<span class="anker" id="stufe-3-21"></span>

:::aufgabe Aufgabe 9 ★ Divergenz und Rotation rechnen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Berechne $\operatorname{div}\boldsymbol{F}$ und $\operatorname{rot}\boldsymbol{F}$ für $\boldsymbol{F}(x,y,z)=(x^2y,\;yz,\;xz^2)$, allgemein und im Punkt $(1,2,-1)$.

</li>

<li>

Berechne die Jacobi-Matrix von $\boldsymbol{F}$ aus (a) im Punkt $(1,2,-1)$, ihre Spur und die Wirbelmatrix. Lies $\operatorname{div}\boldsymbol{F}$ und $\operatorname{rot}\boldsymbol{F}$ daraus ab.

</li>

<li>

Berechne für $\boldsymbol G(x,y)=(x^2y,\;xy^2)$ die Größen $\operatorname{div}\boldsymbol G$, $\operatorname{rot}\boldsymbol G$, $\operatorname{div}\boldsymbol G^\perp$ und $\operatorname{rot}\boldsymbol G^\perp$ und prüfe [(3.9)](#gl-3-9).

</li>

</ol>

:::loesung
(a) $\operatorname{div}\boldsymbol{F}=\frac{\partial(x^2y)}{\partial x}+\frac{\partial(yz)}{\partial y}+\frac{\partial(xz^2)}{\partial z}=2xy+z+2xz$, im Punkt $(1,2,-1)$ also $4-1-2=1$. Nach [(3.4)](#gl-3-4)

$$\operatorname{rot}\boldsymbol{F}=\Bigl(\frac{\partial(xz^2)}{\partial y}-\frac{\partial(yz)}{\partial z},\;\frac{\partial(x^2y)}{\partial z}-\frac{\partial(xz^2)}{\partial x},\;\frac{\partial(yz)}{\partial x}-\frac{\partial(x^2y)}{\partial y}\Bigr)=(-y,\;-z^2,\;-x^2),$$

im Punkt $(1,2,-1)$ also $(-2,-1,-1)$.

(b) Zeile für Zeile abgeleitet:

$$D\boldsymbol{F}=\begin{pmatrix}2xy&x^2&0\\0&z&y\\z^2&0&2xz\end{pmatrix},\qquad D\boldsymbol{F}(1,2,-1)=\begin{pmatrix}4&1&0\\0&-1&2\\1&0&-2\end{pmatrix},\qquad\operatorname{Spur}=4-1-2=1=\operatorname{div}\boldsymbol{F} .$$

Die Wirbelmatrix ist

$$(\omega_{jk})=\tfrac12\bigl((D\boldsymbol{F})^T-D\boldsymbol{F}\bigr)=\begin{pmatrix}0&-1/2&1/2\\1/2&0&-1\\-1/2&1&0\end{pmatrix}.$$

Nach [(3.11)](#gl-3-11) ist $(\operatorname{rot}\boldsymbol{F})_1=\omega_{23}-\omega_{32}=-1-1=-2$, $(\operatorname{rot}\boldsymbol{F})_2=\omega_{31}-\omega_{13}=-\tfrac12-\tfrac12=-1$ und $(\operatorname{rot}\boldsymbol{F})_3=\omega_{12}-\omega_{21}=-\tfrac12-\tfrac12=-1$, wie in (a).

(c) $\operatorname{div}\boldsymbol G=2xy+2xy=4xy$ und $\operatorname{rot}\boldsymbol G=\frac{\partial(xy^2)}{\partial x}-\frac{\partial(x^2y)}{\partial y}=y^2-x^2$. Mit $\boldsymbol G^\perp=(-xy^2,\;x^2y)$ ist $\operatorname{div}\boldsymbol G^\perp=-y^2+x^2=-\operatorname{rot}\boldsymbol G$ und $\operatorname{rot}\boldsymbol G^\perp=2xy-(-2xy)=4xy=\operatorname{div}\boldsymbol G$, wie [(3.9)](#gl-3-9) verlangt.
:::
:::

:::aufgabe Aufgabe 10 ★★ Radialsymmetrische harmonische Funktionen
<span class="anker" id="aufg-10"></span>

Sei $u(\boldsymbol{x})=v(r)$ auf $\mathbb{R}^n\setminus\{0\}$ mit einer zweimal stetig differenzierbaren Funktion $v$.

<ol class="al">

<li>

Zeige $\Delta u=v''(r)+\frac{n-1}{r}\,v'(r)$. Tipp: [(2.2)](radialsymmetrische-funktionen-und-felder.html#gl-2-2) und [(3.3)](#gl-3-3).

</li>

<li>

Bestimme alle radialsymmetrischen harmonischen Funktionen auf $\mathbb{R}^4\setminus\{0\}$. Tipp: Multipliziere die Gleichung mit $r^3$ und erkenne eine Ableitung.

</li>

<li>

Zeige, dass $\ln r$ auf $\mathbb{R}^2\setminus\{0\}$ harmonisch ist.

</li>

<li>

Zeige $\Delta(fg)=f\,\Delta g+g\,\Delta f+2\,\nabla f\cdot\nabla g$ für zweimal differenzierbare Funktionen $f,g$ und berechne damit $\Delta(x\,r^{-3})$ auf $\mathbb{R}^3\setminus\{0\}$.

</li>

</ol>

:::loesung
(a) Nach [(2.2)](radialsymmetrische-funktionen-und-felder.html#gl-2-2) ist $\nabla u=v'(r)\,\hat{\boldsymbol{e}}_r$, ein radialsymmetrisches Feld mit dem Profil $f=v'$. Mit [(3.3)](#gl-3-3) folgt $\Delta u=\operatorname{div}\nabla u=v''(r)+\frac{n-1}{r}\,v'(r)$.

(b) Für $n=4$ lautet $\Delta u=0$: $v''+\frac3rv'=0$. Multipliziert mit $r^3$ steht $r^3v''+3r^2v'=(r^3v')'=0$ da. Also ist $r^3v'$ gleich einer Konstanten $C$, damit $v'=C/r^3$ und $v=-\frac{C}{2r^2}+c_2$. Mit $c_1=-C/2$ ist $v=c_1/r^2+c_2$, und $c_1,c_2$ sind beliebige Konstanten. Alle radialsymmetrischen harmonischen Funktionen auf $\mathbb{R}^4\setminus\{0\}$ sind also $c_1/r^2+c_2$.

(c) Für $n=2$ und $v=\ln r$ ist $v'=1/r$ und $v''=-1/r^2$, also $\Delta u=-\frac1{r^2}+\frac1r\cdot\frac1r=0$.

(d) Es ist $\nabla(fg)=f\,\nabla g+g\,\nabla f$. Mit der Produktregel der Divergenz (Satz [3.4](#satz-3-4)) ist $\operatorname{div}(f\nabla g)=\nabla f\cdot\nabla g+f\,\Delta g$ und $\operatorname{div}(g\nabla f)=\nabla g\cdot\nabla f+g\,\Delta f$. Addiert: $\Delta(fg)=f\,\Delta g+g\,\Delta f+2\,\nabla f\cdot\nabla g$. Für $f=x$ und $g=r^{-3}$ in $\mathbb{R}^3$ ist $\Delta f=0$. Aus (a) mit $n=3$ und $v=r^{-3}$, $v'=-3r^{-4}$, $v''=12r^{-5}$, folgt $\Delta g=12r^{-5}-6r^{-5}=6r^{-5}$. Außerdem ist $\nabla f\cdot\nabla g=(1,0,0)\cdot(-3r^{-4}\,\hat{\boldsymbol{e}}_r)=-3x\,r^{-5}$. Zusammen: $\Delta(x\,r^{-3})=6x\,r^{-5}+0-6x\,r^{-5}=0$. Die Funktion ist harmonisch, obwohl sie nicht radialsymmetrisch ist.
:::
:::

:::aufgabe Aufgabe 11 ★★ Potential suchen
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Für welche Zahlen $\lambda\in\mathbb{R}$ hat $\boldsymbol{F}=(2xy+z^2,\;\lambda x^2+z,\;2xz+y)$ auf $\mathbb{R}^3$ ein Skalarpotential? Gib es an.

</li>

<li>

Hat $\boldsymbol G=(yz,\;xz^2,\;xy)$ ein Skalarpotential?

</li>

<li>

Für welche $\lambda\in\mathbb{R}$ hat $\boldsymbol{E}(x,y)=\dfrac{(\lambda y,\;x)}{(x+y)^2}$ auf der Halbebene $x+y>0$ ein Skalarpotential? Gib es an. Tipp: Ist die Bedingung erfüllt, findest du das Potential wie in Unterabschnitt [3.20](#stufe-3-20).

</li>

</ol>

:::loesung
(a) Die Bedingung $\partial F_2/\partial x=\partial F_1/\partial y$ lautet $2\lambda x=2x$ und verlangt $\lambda=1$. Die beiden anderen stimmen für jedes $\lambda$: $\partial F_3/\partial x=2z=\partial F_1/\partial z$ und $\partial F_3/\partial y=1=\partial F_2/\partial z$. Für $\lambda\neq1$ gibt es also kein Skalarpotential. Für $\lambda=1$: Aus $\partial\varphi/\partial x=2xy+z^2$ folgt $\varphi=x^2y+xz^2+c(y,z)$. Ableiten nach $y$: $x^2+\partial c/\partial y=x^2+z$, also $c=yz+d(z)$. Ableiten nach $z$: $2xz+y+d'(z)=2xz+y$, also $d$ konstant. Ergebnis: $\varphi=x^2y+xz^2+yz+\text{konst}$.

(b) Nein: $\partial G_2/\partial z=2xz$, aber $\partial G_3/\partial y=x$. Das stimmt nicht überall überein, also ist [(3.12)](#gl-3-12) verletzt.

(c) $\dfrac{\partial E_1}{\partial y}=\lambda\,\dfrac{(x+y)^2-2y(x+y)}{(x+y)^4}=\lambda\,\dfrac{x-y}{(x+y)^3}$ und $\dfrac{\partial E_2}{\partial x}=\dfrac{(x+y)^2-2x(x+y)}{(x+y)^4}=\dfrac{y-x}{(x+y)^3}$. Gleichheit für alle Punkte verlangt $\lambda=-1$. Dann gibt $\partial\varphi/\partial x=-y/(x+y)^2$ die Funktion $\varphi=\frac{y}{x+y}+c(y)$, und $\partial\varphi/\partial y=\frac{(x+y)-y}{(x+y)^2}+c'(y)=\frac{x}{(x+y)^2}+c'(y)$ verlangt $c'=0$. Ergebnis: $\varphi=\frac{y}{x+y}+\text{konst}$.
:::
:::
