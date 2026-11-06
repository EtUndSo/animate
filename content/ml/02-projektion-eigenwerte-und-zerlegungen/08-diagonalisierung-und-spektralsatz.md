---
title: Diagonalisierung und Spektralsatz
pfad: Informatik / Machine Learning / Projektion, Eigenwerte und Zerlegungen
order: 6220800
summary: Beschreibt man eine Matrix in einer Basis aus ihren Eigenvektoren, wird sie diagonal: Jede Koordinate wird nur mit ihrem Eigenwert multipliziert, und gekoppelte Rechnungen zerfallen in einzelne.
tags: Basiswechsel, diagonalisierbar, Hauptachsen
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Beschreibt man eine Matrix in einer Basis aus ihren Eigenvektoren, wird sie diagonal: Jede Koordinate wird nur mit ihrem Eigenwert multipliziert, und gekoppelte Rechnungen zerfallen in einzelne. Dieser Abschnitt zeigt, wann das geht, und beweist, dass es bei symmetrischen Matrizen immer geht, sogar mit einer Orthonormalbasis.
:::

### Basiswechsel

<span class="anker" id="stufe-7-1"></span>

Derselbe Pfeil hat in verschiedenen Basen verschiedene Koordinaten. Ebenso hat dieselbe lineare Abbildung in verschiedenen Koordinaten verschiedene Matrizen. Manche Basen machen die Matrix besonders einfach.

Es sei $\mathbf s_1,\dots,\mathbf s_n$ eine Basis des $\mathbb{R}^n$, und $\mathbf{S}$ die Matrix mit diesen Spalten. Sie ist nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.5, invertierbar. Hat $\mathbf{x}$ in dieser Basis die Koordinaten $\mathbf{c}$, so ist $\mathbf{x}=\sum_ic_i\mathbf s_i=\mathbf{S}\mathbf{c}$, also umgekehrt $\mathbf{c}=\mathbf{S}^{-1}\mathbf{x}$. Bildet man $\mathbf{x}$ mit $\mathbf{A}$ ab, so hat das Bild $\mathbf{A}\mathbf{x}$ die Koordinaten $\mathbf{S}^{-1}\mathbf{A}\mathbf{x}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}\,\mathbf{c}$. In den neuen Koordinaten wirkt die Abbildung also durch die Matrix $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$: erst in die alten Koordinaten umrechnen, dann abbilden, dann zurückrechnen.

:::definition Definition 7.1 (Basiswechsel)
<span class="anker" id="satz-7-1"></span>

Ist $\mathbf{S}$ invertierbar, so heißt $\mathbf{B}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ die Matrix von $\mathbf{A}$ in der Basis der Spalten von $\mathbf{S}$. Der Übergang von $\mathbf{A}$ zu $\mathbf{B}$ heißt __Basiswechsel__.
:::

Zwei Matrizen, die so zusammenhängen, nennt man ähnlich. Sie beschreiben dieselbe Abbildung, nur in verschiedenen Koordinaten.

:::satz Satz 7.2 (Was ein Basiswechsel nicht ändert)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}$ und $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ haben dasselbe charakteristische Polynom, also dieselben Eigenwerte, dieselbe Spur und dieselbe Determinante.
:::

:::beweis Basiswechsel
Es ist $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}-\lambda\mathbf{I}=\mathbf{S}^{-1}(\mathbf{A}-\lambda\mathbf{I})\mathbf{S}$. Nach den Rechenregeln aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 14.5, ist die Determinante davon $\det\mathbf{S}^{-1}\cdot\det(\mathbf{A}-\lambda\mathbf{I})\cdot\det\mathbf{S}=\det(\mathbf{A}-\lambda\mathbf{I})$. Spur und Determinante sind nach [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5) aus den Eigenwerten bestimmt.
:::

⁠**Rechenbeispiel:** Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ und die Basis $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 13.3, ist $\mathbf{S}=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ und $\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\bigr)$. Dann ist

$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}4&5\\2&5\end{pmatrix}=\begin{pmatrix}2&0\\2&5\end{pmatrix}.$$

Die Spur ist wieder $7$, die Determinante wieder $10$, und die Eigenwerte stehen jetzt auf der Diagonale einer Dreiecksmatrix: $2$ und $5$.

⁠**Kurz gesagt:** In der Basis der Spalten von $\mathbf{S}$ hat die Abbildung $\mathbf{A}$ die Matrix $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$; Eigenwerte, Spur und Determinante bleiben dabei gleich.

### Diagonalisierung

<span class="anker" id="stufe-7-2"></span>

Die einfachste mögliche Matrix ist eine Diagonalmatrix: Sie multipliziert jede Koordinate mit einer eigenen Zahl, ohne die Koordinaten zu vermischen. Nimmt man als Basis die Eigenvektoren, so wird jeder Basisvektor nur mit seinem Eigenwert multipliziert. In dieser Basis ist die Matrix also diagonal.

:::satz Satz 7.3 (Diagonalisierung)
<span class="anker" id="satz-7-3"></span>

Hat $\mathbf{A}\in\mathbb{R}^{n\times n}$ $n$ linear unabhängige Eigenvektoren $\mathbf s_1,\dots,\mathbf s_n$ zu den Eigenwerten $\lambda_1,\dots,\lambda_n$, und ist $\mathbf{S}$ die Matrix mit diesen Spalten, so ist

<span class="anker" id="gl-7-1"></span>
$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad\text{also}\qquad \mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1} . \tag{7.1}$$

Umgekehrt: Lässt sich $\mathbf{A}$ so schreiben, so sind die Spalten von $\mathbf{S}$ Eigenvektoren.
:::

:::beweis Diagonalisierung
Nach [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 9.2, ist Spalte $i$ von $\mathbf{A}\mathbf{S}$ das Produkt $\mathbf{A}\mathbf s_i=\lambda_i\mathbf s_i$, und Spalte $i$ von $\mathbf{S}\boldsymbol{\Lambda}$ ist ebenfalls $\lambda_i\mathbf s_i$. Also ist $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$. Die Spalten von $\mathbf{S}$ sind unabhängig, also ist $\mathbf{S}$ invertierbar, und Multiplikation mit $\mathbf{S}^{-1}$ von links ergibt [(7.1)](#gl-7-1). Liest man dieselbe Gleichung $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$ rückwärts, folgt die Umkehrung.
:::

Eine Matrix, die sich so schreiben lässt, heißt __diagonalisierbar__. Nach dem Satz in Abschnitt [6.8](eigenwerte-und-eigenvektoren.html#stufe-6-8) ist das zum Beispiel immer der Fall, wenn alle $n$ Eigenwerte verschieden sind. Nicht diagonalisierbar ist die Scherung, denn ihr fehlt ein Eigenvektor. Auch die Drehung um $90^\circ$ ist nicht mit reellen Zahlen diagonalisierbar, nur mit komplexen. Beide sind trotzdem invertierbar: Invertierbar und diagonalisierbar sind zwei verschiedene Eigenschaften.

⁠**Rechenbeispiel:** Für $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ mit den Eigenvektoren $(1,\,1)^{\top}$ und $(1,\,-2)^{\top}$ ist

$$\mathbf{S}=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix},\qquad \mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix}\begin{pmatrix}5&2\\5&-4\end{pmatrix}=\begin{pmatrix}5&0\\0&2\end{pmatrix}.$$

⁠**Kurz gesagt:** Eine Matrix mit $n$ unabhängigen Eigenvektoren ist in deren Basis diagonal: $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$.

### Entkoppeln: Potenzen und Folgen

<span class="anker" id="stufe-7-3"></span>

Wozu das gut ist, zeigt eine Matrix, die immer wieder angewandt wird. Zwei Orte A und B tauschen jedes Jahr Einwohner aus: $20\,\%$ der Einwohner von A ziehen nach B, $30\,\%$ der Einwohner von B ziehen nach A, alle anderen bleiben. Sind $\mathbf{x}_k$ die Einwohnerzahlen im Jahr $k$, so ist

$$\mathbf{x}_{k+1}=\mathbf M\mathbf{x}_k\qquad\text{mit}\qquad \mathbf M=\begin{pmatrix}0{,}8&0{,}3\\0{,}2&0{,}7\end{pmatrix}.$$

Die beiden Einwohnerzahlen sind gekoppelt: Jede neue Zahl hängt von beiden alten ab. Nach $k$ Jahren ist $\mathbf{x}_k=\mathbf M^k\mathbf{x}_0$. Die Potenz $\mathbf M^k$ direkt auszurechnen ist mühsam und zeigt nicht, was auf lange Sicht passiert. In der Eigenbasis ist es einfach.

:::satz Satz 7.4 (Potenzen und Folgen in der Eigenbasis)
<span class="anker" id="satz-7-4"></span>

Ist $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$, so ist $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$ mit $\boldsymbol{\Lambda}^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k)$. Für die Folge $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$ gilt

<span class="anker" id="gl-7-2"></span>
$$\mathbf{x}_k=\sum_{i=1}^nc_i\,\lambda_i^k\,\mathbf s_i\qquad\text{mit}\qquad \mathbf{c}=\mathbf{S}^{-1}\mathbf{x}_0 . \tag{7.2}$$
:::

:::beweis Potenzen
$\mathbf{A}^2=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\mathbf{S}\boldsymbol{\Lambda}^2\mathbf{S}^{-1}$, weil $\mathbf{S}^{-1}\mathbf{S}=\mathbf{I}$ in der Mitte wegfällt; ebenso für jede Potenz. Zerlegt man $\mathbf{x}_0=\sum_ic_i\mathbf s_i$ in Eigenvektoren, so multipliziert jede Anwendung von $\mathbf{A}$ jeden Anteil nur mit seinem Eigenwert.
:::

In den Koordinaten $\mathbf{c}$ der Eigenbasis ist jeder Schritt die Multiplikation jeder Koordinate mit ihrer eigenen Zahl: $c_i\mapsto\lambda_ic_i$. Aus einer gekoppelten Rechnung mit $n$ Unbekannten werden $n$ getrennte Rechnungen mit je einer Unbekannten. Diese Koordinaten sind entkoppelt. Auf lange Sicht überwiegt der Anteil mit dem betragsgrößten Eigenwert.

⁠**Rechenbeispiel:** $\mathbf M$ hat die Spur $1{,}5$ und die Determinante $0{,}56-0{,}06=0{,}5$, also die Eigenwerte $1$ und $0{,}5$. Eigenvektoren sind $\mathbf s_1=(3,\,2)^{\top}$ zum Eigenwert $1$, denn $\mathbf M\mathbf s_1=(2{,}4+0{,}6;\ 0{,}6+1{,}4)^{\top}=\mathbf s_1$, und $\mathbf s_2=(1,\,-1)^{\top}$ zum Eigenwert $0{,}5$. Wohnen anfangs $1000$ Menschen in A und niemand in B, so ist $\mathbf{x}_0=(1000,\,0)^{\top}=200\,\mathbf s_1+400\,\mathbf s_2$ und nach [(7.2)](#gl-7-2)

$$\mathbf{x}_k=200\begin{pmatrix}3\\2\end{pmatrix}+400\cdot0{,}5^k\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}600+400\cdot0{,}5^k\\400-400\cdot0{,}5^k\end{pmatrix}.$$

Nach einem Jahr sind es $(800,\,200)^{\top}$, nach zwei Jahren $(700,\,300)^{\top}$, und auf lange Sicht stellt sich $(600,\,400)^{\top}$ ein. Der Anteil zum Eigenwert $0{,}5$ halbiert sich jedes Jahr, der Anteil zum Eigenwert $1$ bleibt.

⁠**Kurz gesagt:** In der Eigenbasis wird jede Potenz der Matrix zu Potenzen der Eigenwerte; gekoppelte Folgen zerfallen in getrennte Folgen, eine je Eigenvektor.

:::hintergrund Dasselbe Prinzip wie bei LTI-Systemen und der Fourier-Transformation
Im Zeitbereich ist ein LTI-System eine Faltung: Jeder Ausgangswert hängt von allen Eingangswerten ab, alles ist gekoppelt. Zerlegt man das Eingangssignal in Exponentialfunktionen $\mathrm e^{pt}$, wird jede nur mit ihrem Eigenwert $H(p)$ multipliziert, und die Kopplung ist verschwunden. Die Laplace- und die Fourier-Transformation leisten für Signale, was der Basiswechsel $\mathbf{S}^{-1}$ für Vektoren leistet: Sie rechnen in die Koordinaten der Eigenfunktionen um.

Für abgetastete Signale ist die Entsprechung sogar wörtlich eine Diagonalisierung. Eine zyklische Faltung $y_k=\sum_lh_{(k-l)\bmod n}\,x_l$ ist eine Matrix, deren erste Spalte die Impulsantwort $(h_0,\dots,h_{n-1})^{\top}$ ist und deren übrige Spalten deren zyklische Verschiebungen sind. Ihre Eigenvektoren sind die abgetasteten komplexen Schwingungen $\mathbf f_m=\bigl(1,\ \mathrm e^{\mathrm j2\pi m/n},\ \mathrm e^{\mathrm j2\pi\cdot2m/n},\dots\bigr)^{\top}$, und der Eigenwert zu $\mathbf f_m$ ist der Wert $H[m]=\sum_qh_q\,\mathrm e^{-\mathrm j2\pi mq/n}$ der diskreten Fourier-Transformation der Impulsantwort. Die Matrix der diskreten Fourier-Transformation ist also, bis auf den Faktor $1/n$, das $\mathbf{S}^{-1}$, das jede zyklische Faltung diagonalisiert, und zwar für alle Impulsantworten zugleich. Beispiel mit $n=3$ und $h=(1;\,0{,}5;\,0)$: Die Matrix $\Bigl(\begin{smallmatrix}1&0&0{,}5\\0{,}5&1&0\\0&0{,}5&1\end{smallmatrix}\Bigr)$ bildet $\mathbf f_0=(1,1,1)^{\top}$ auf $1{,}5\,\mathbf f_0$ ab, und $1{,}5=H[0]=h_0+h_1+h_2$.
:::

### Symmetrische Matrizen haben reelle Eigenwerte

<span class="anker" id="stufe-7-4"></span>

Bei symmetrischen Matrizen ist vieles besonders einfach. Das Erste: Ihre Eigenwerte sind immer reell. Eine symmetrische Matrix dreht also keine Ebene in sich, wie es die Drehungen in Abschnitt [6.6](eigenwerte-und-eigenvektoren.html#stufe-6-6) tun.

:::satz Satz 7.5 (Reelle Eigenwerte)
<span class="anker" id="satz-7-5"></span>

Jeder Eigenwert einer reellen symmetrischen Matrix ist reell.
:::

:::beweis Reelle Eigenwerte
Es sei $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ mit $\mathbf{v}\ne\mathbf{0}$, wobei $\lambda$ und $\mathbf{v}$ zunächst komplex sein dürfen. Konjugiert man beide Seiten, so bleibt $\mathbf{A}$ unverändert, weil es reell ist: $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$. Man berechnet die Zahl $(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}$ auf zwei Arten. Einmal mit $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=\lambda\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Einmal mit $\mathbf{A}=\mathbf{A}^{\top}$ und $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=(\mathbf{A}^{\top}\mathbf{v}^*)^{\top}\mathbf{v}=(\mathbf{A}\mathbf{v}^*)^{\top}\mathbf{v}=\lambda^*\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Also ist $(\lambda-\lambda^*)\,(\mathbf{v}^*)^{\top}\mathbf{v}=0$. Nach Abschnitt [6.1](eigenwerte-und-eigenvektoren.html#stufe-6-1) ist $(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0$, also $\lambda=\lambda^*$, und $\lambda$ ist reell.
:::

Zu einem reellen Eigenwert gibt es dann auch reelle Eigenvektoren, denn $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ ist ein reelles Gleichungssystem.

⁠**Rechenbeispiel:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ hat das charakteristische Polynom $\lambda^2-7\lambda+6$ mit der Diskriminante $49-24=25>0$ und den reellen Eigenwerten $6$ und $1$. Für eine beliebige symmetrische $2\times2$-Matrix $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$ ist die Diskriminante $(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ge0$; die Eigenwerte sind also immer reell, wie der Satz sagt.

⁠**Kurz gesagt:** Eine symmetrische Matrix hat nur reelle Eigenwerte und reelle Eigenvektoren.

### Eigenvektoren symmetrischer Matrizen stehen senkrecht

<span class="anker" id="stufe-7-5"></span>

Die Eigenvektoren von $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ standen schräg zueinander. Bei symmetrischen Matrizen kann das nicht passieren.

:::satz Satz 7.6 (Orthogonale Eigenvektoren)
<span class="anker" id="satz-7-6"></span>

Eigenvektoren einer symmetrischen Matrix zu verschiedenen Eigenwerten stehen senkrecht aufeinander.
:::

:::beweis Orthogonale Eigenvektoren
Es sei $\mathbf{A}\mathbf{v}_1=\lambda_1\mathbf{v}_1$ und $\mathbf{A}\mathbf{v}_2=\lambda_2\mathbf{v}_2$ mit $\lambda_1\ne\lambda_2$. Man berechnet $\mathbf{v}_1^{\top}\mathbf{A}\mathbf{v}_2$ auf zwei Arten: als $\mathbf{v}_1^{\top}(\lambda_2\mathbf{v}_2)=\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2$, und mit $\mathbf{A}^{\top}=\mathbf{A}$ als $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\lambda_1\,\mathbf{v}_1^{\top}\mathbf{v}_2$. Also ist $(\lambda_1-\lambda_2)\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$, und wegen $\lambda_1\ne\lambda_2$ ist $\mathbf{v}_1^{\top}\mathbf{v}_2=0$.
:::

⁠**Rechenbeispiel:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ hat zum Eigenwert $6$ den Eigenvektor $(2,\,1)^{\top}$, denn $(10+2,\ 4+2)^{\top}=6\,(2,\,1)^{\top}$, und zum Eigenwert $1$ den Eigenvektor $(1,\,-2)^{\top}$, denn $(5-4,\ 2-4)^{\top}=(1,\,-2)^{\top}$. Ihr Skalarprodukt ist $2-2=0$ (Abb. [19](#abb-19)).

:::abbildung ml/k2rsenkrecht 19
Das Skalarprodukt der Eigenvektoren $(2,1)^{\top}$ zum Eigenwert $6$ und $(1,-2)^{\top}$ zum Eigenwert $1$ der symmetrischen Matrix $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$: Sie stehen senkrecht aufeinander.
:::

⁠**Kurz gesagt:** Bei einer symmetrischen Matrix stehen Eigenvektoren zu verschiedenen Eigenwerten senkrecht aufeinander.

:::hintergrund Warum gerade die Symmetrie die Eigenrichtungen senkrecht stellt
Der Beweis benutzt die Symmetrie an genau einer Stelle: $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\mathbf{v}_1^{\top}(\mathbf{A}\mathbf{v}_2)$. Für eine symmetrische Matrix gilt diese Gleichung für alle Vektoren; man darf $\mathbf{A}$ im Skalarprodukt von einer Seite auf die andere schieben. Das Skalarprodukt misst, wie viel von $\mathbf{v}_2$ in Richtung $\mathbf{v}_1$ zeigt. Streckt $\mathbf{A}$ die eine Richtung um $\lambda_1$ und die andere um $\lambda_2$, so wird dieser Anteil links mit $\lambda_1$, rechts mit $\lambda_2$ multipliziert. Beide Seiten können nur gleich sein, wenn es nichts zu multiplizieren gibt, wenn der Anteil also null ist. Bei einer nicht symmetrischen Matrix gilt die Verschiebe-Regel nicht, und schräge Eigenrichtungen sind möglich.

Daraus folgt eine zweite, wichtige Eigenschaft. Ist $\mathbf{q}$ ein Eigenvektor und steht $\mathbf{z}$ senkrecht auf $\mathbf{q}$, so steht auch $\mathbf{A}\mathbf{z}$ senkrecht auf $\mathbf{q}$: $(\mathbf{A}\mathbf{z})^{\top}\mathbf{q}=\mathbf{z}^{\top}\mathbf{A}\mathbf{q}=\lambda\,\mathbf{z}^{\top}\mathbf{q}=0$. Eine symmetrische Matrix bildet das orthogonale Komplement eines Eigenvektors also in sich selbst ab. Dort kann man den nächsten Eigenvektor suchen, und so weiter. Genau so funktioniert der Beweis im nächsten Unterabschnitt.
:::

### Der Spektralsatz

<span class="anker" id="stufe-7-6"></span>

Die beiden vorigen Sätze lassen vermuten, dass jede symmetrische Matrix in einer Orthonormalbasis aus Eigenvektoren diagonal ist. Das stimmt auch dann, wenn Eigenwerte mehrfach vorkommen. Die Menge der Eigenwerte einer Matrix nennt man ihr Spektrum, daher der Name des Satzes.

:::satz Satz 7.7 (Spektralsatz)
<span class="anker" id="satz-7-7"></span>

Zu jeder symmetrischen Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ gibt es eine Orthonormalbasis $\mathbf{q}_1,\dots,\mathbf{q}_n$ aus Eigenvektoren mit reellen Eigenwerten $\lambda_1,\dots,\lambda_n$. Mit der orthogonalen Matrix $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ und $\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ ist

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}=\sum_{i=1}^n\lambda_i\,\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{7.3}$$
:::

:::beweis Spektralsatz
Man geht schrittweise vor. Nach Abschnitt [6.3](eigenwerte-und-eigenvektoren.html#stufe-6-3) hat $\mathbf{A}$ mindestens einen Eigenwert $\lambda_1$, nach Abschnitt [7.4](#stufe-7-4) ist er reell und hat einen reellen Eigenvektor, normiert $\mathbf{q}_1$. Man ergänzt $\mathbf{q}_1$ zu einer Orthonormalbasis des $\mathbb{R}^n$, etwa mit dem Gram-Schmidt-Verfahren angewandt auf $\mathbf{q}_1,\mathbf{e}_1,\dots,\mathbf{e}_n$, wobei man die Vektoren mit $\tilde{\mathbf{q}}=\mathbf{0}$ überspringt. Die übrigen Basisvektoren bilden die Spalten einer Matrix $\mathbf{W}\in\mathbb{R}^{n\times(n-1)}$, und $\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1&\mathbf{W}\end{pmatrix}$ ist orthogonal. Dann ist

$$\mathbf{Q}_1^{\top}\mathbf{A}\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{q}_1^{\top}\mathbf{A}\mathbf{W}\\\mathbf{W}^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{W}^{\top}\mathbf{A}\mathbf{W}\end{pmatrix}=\begin{pmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{B}\end{pmatrix}$$

mit der symmetrischen $(n-1)\times(n-1)$-Matrix $\mathbf{B}=\mathbf{W}^{\top}\mathbf{A}\mathbf{W}$. Die Nullen entstehen, weil $\mathbf{A}\mathbf{q}_1=\lambda_1\mathbf{q}_1$ senkrecht auf den Spalten von $\mathbf{W}$ steht, und oben rechts ebenso, weil $\mathbf{A}$ symmetrisch ist. Für $\mathbf{B}$ wiederholt man dasselbe, bis eine $1\times1$-Matrix übrig bleibt. Hat man so für $\mathbf{B}$ eine orthogonale Matrix $\mathbf{Q}_B$ gefunden, mit der $\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B$ diagonal ist, so ist $\mathbf{Q}=\mathbf{Q}_1\bigl(\begin{smallmatrix}1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B\end{smallmatrix}\bigr)$ als Produkt orthogonaler Matrizen orthogonal, und $\mathbf{Q}^{\top}\mathbf{A}\mathbf{Q}=\bigl(\begin{smallmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B\end{smallmatrix}\bigr)=\boldsymbol{\Lambda}$ ist diagonal. Weil $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ ist, folgt $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. Die Summenform folgt aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 9.5, denn $\mathbf{Q}\boldsymbol{\Lambda}$ hat die Spalten $\lambda_i\mathbf{q}_i$.
:::

Jeder Summand $\mathbf{q}_i\mathbf{q}_i^{\top}$ ist nach Abschnitt [2.3](projektion-auf-eine-gerade.html#stufe-2-3) die Projektion auf die Gerade in Richtung $\mathbf{q}_i$. Eine symmetrische Matrix ist also eine Summe von Projektionen auf senkrechte Achsen, jede mit ihrem Eigenwert gewichtet. Bei einem mehrfachen Eigenwert ist die Wahl der $\mathbf{q}_i$ in seinem Eigenraum frei: Jede Orthonormalbasis des Eigenraums ist recht. Auch das Vorzeichen jedes $\mathbf{q}_i$ ist frei. Manche Bücher sortieren die Eigenwerte absteigend, andere nicht.

⁠**Rechenbeispiel:** Für $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ sind $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ und $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$ die normierten Eigenvektoren zu $6$ und $1$. Dann ist

$$6\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}+1\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\frac15\begin{pmatrix}25&10\\10&10\end{pmatrix}=\begin{pmatrix}5&2\\2&2\end{pmatrix}.$$

⁠**Kurz gesagt:** Jede symmetrische Matrix ist $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$: in einem passend gedrehten Achsenkreuz diagonal, eine gewichtete Summe von Projektionen auf senkrechte Achsen.

:::hintergrund Wo symmetrische Matrizen herkommen
Symmetrische Matrizen entstehen überall, wo eine Matrix paarweise Beziehungen beschreibt, die nicht von der Reihenfolge abhängen. Die Gram-Matrizen $\mathbf{X}^{\top}\mathbf{X}$ und $\mathbf{X}\mathbf{X}^{\top}$ aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 10, enthalten Skalarprodukte, und $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$. Die Matrix einer quadratischen Form darf man nach Abschnitt [5.2](quadratische-formen.html#stufe-5-2) immer symmetrisch wählen. Die Induktivitätsmatrix gekoppelter Spulen ist symmetrisch, weil die Gegeninduktivität von Spule 1 auf Spule 2 dieselbe ist wie umgekehrt. Für alle diese Matrizen garantiert der Spektralsatz reelle Eigenwerte und senkrechte Eigenrichtungen.
:::

### Hauptachsen

<span class="anker" id="stufe-7-7"></span>

In Abschnitt [5.3](quadratische-formen.html#stufe-5-3) war die Form einer quadratischen Form leicht zu erkennen, solange ihre Matrix diagonal war. Der Spektralsatz macht jede symmetrische Matrix diagonal, wenn man die Koordinaten passend dreht. Damit verschwinden die gemischten Glieder.

:::satz Satz 7.8 (Hauptachsen einer quadratischen Form)
<span class="anker" id="satz-7-8"></span>

Ist $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ und sind $c_i=\mathbf{q}_i^{\top}\mathbf{x}$ die Koordinaten von $\mathbf{x}$ in der Eigenbasis, so ist

<span class="anker" id="gl-7-4"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_1c_1^2+\lambda_2c_2^2+\dots+\lambda_nc_n^2 . \tag{7.4}$$
:::

:::beweis Hauptachsen
Mit $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ ist $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}\mathbf{x}=\mathbf{c}^{\top}\boldsymbol{\Lambda}\mathbf{c}=\sum_i\lambda_ic_i^2$.
:::

Die Richtungen der Eigenvektoren heißen deshalb die __Hauptachsen__ der quadratischen Form. Sind alle Eigenwerte positiv, so ist die Höhenlinie $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=1$ eine Ellipse, im $\mathbb{R}^3$ ein Ellipsoid. Ihre Achsen liegen in den Richtungen $\mathbf{q}_i$, und die Halbachse in Richtung $\mathbf{q}_i$ hat die Länge $1/\sqrt{\lambda_i}$, denn für $\mathbf{x}=t\,\mathbf{q}_i$ ist $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_it^2=1$ genau bei $t=\pm1/\sqrt{\lambda_i}$. Ein großer Eigenwert gehört zu einer steilen Richtung und einer kurzen Halbachse.

:::abbildung ml/k2ellipse 20
Die Höhenlinien $5x_1^2+4x_1x_2+2x_2^2=1$ (blau) und $=\tfrac14$ (hellblau) sind Ellipsen. Ihre Achsen (grau) liegen in den Richtungen der Eigenvektoren $\mathbf{q}_1=(2,1)^{\top}/\sqrt5$ zum Eigenwert $6$ und $\mathbf{q}_2=(1,-2)^{\top}/\sqrt5$ zum Eigenwert $1$. Die Halbachsen der äußeren Ellipse sind $1/\sqrt6\approx0{,}41$ (rot) und $1/\sqrt1=1$ (grün): In Richtung des großen Eigenwerts steigt die Form am steilsten, die Ellipse ist dort am schmalsten.
:::

⁠**Rechenbeispiel:** Für $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$ sind die Koordinaten in der Eigenbasis $c_1=(2x_1+x_2)/\sqrt5$ und $c_2=(x_1-2x_2)/\sqrt5$, und

$$5x_1^2+4x_1x_2+2x_2^2=6\,c_1^2+c_2^2=\tfrac65(2x_1+x_2)^2+\tfrac15(x_1-2x_2)^2 .$$

Ausmultipliziert ergibt die rechte Seite $\tfrac15\bigl(24x_1^2+24x_1x_2+6x_2^2+x_1^2-4x_1x_2+4x_2^2\bigr)=5x_1^2+4x_1x_2+2x_2^2$. Die Höhenlinie $f=1$ ist die Ellipse in Abb. [20](#abb-20), mit den Halbachsen $1/\sqrt6\approx0{,}408$ und $1$.

⁠**Kurz gesagt:** In der Eigenbasis wird jede quadratische Form zur Summe $\sum_i\lambda_ic_i^2$ ohne gemischte Glieder; die Eigenvektoren sind die Hauptachsen ihrer Ellipsen, die Halbachsen sind $1/\sqrt{\lambda_i}$.

:::hintergrund Zwei Arten, Quadrate zu ergänzen
Dieselbe Form ließ sich in Abschnitt [5.4](quadratische-formen.html#stufe-5-4) auch als $5(x_1+0{,}4x_2)^2+1{,}2x_2^2$ schreiben. Die Faktoren $5$ und $1{,}2$ dort sind andere Zahlen als die Eigenwerte $6$ und $1$ hier. Beide Zerlegungen sind richtig, aber die neuen Koordinaten sind verschieden: Beim quadratischen Ergänzen sind $x_1+0{,}4x_2$ und $x_2$ schräge Koordinaten, beim Spektralsatz sind $c_1,c_2$ Koordinaten in einem gedrehten rechtwinkligen Achsenkreuz. Nur die zweite Zerlegung zeigt die Achsen der Ellipse. Gemeinsam ist beiden etwas anderes: Die Zahl der positiven, negativen und verschwindenden Faktoren ist dieselbe. Das gilt für jede Zerlegung einer quadratischen Form in eine Summe von Quadraten unabhängiger Koordinaten; der Satz heißt Trägheitssatz von Sylvester. Deshalb führen das Ergänzen und die Eigenwerte immer zum selben Urteil über Schüssel, Rinne oder Sattel.
:::

:::aufgabe Aufgabe 21 ★ Diagonalisieren
<span class="anker" id="aufg-21"></span>

Es sei $\mathbf{A}=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$ aus Aufgabe [17](eigenwerte-und-eigenvektoren.html#aufg-17).

<ol class="al">

<li>

Gib $\mathbf{S}$ und $\boldsymbol{\Lambda}$ mit $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ an und prüfe die Gleichung.

</li>

<li>

Berechne $\mathbf{A}^3$ einmal direkt und einmal als $\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}$.

</li>

</ol>

:::loesung
(a) Aus Aufgabe [17](eigenwerte-und-eigenvektoren.html#aufg-17): Eigenwerte $4$ und $1$ mit den Eigenvektoren $(1,\,1)^{\top}$ und $(2,\,-1)^{\top}$. Also

$$\mathbf{S}=\begin{pmatrix}1&2\\1&-1\end{pmatrix},\qquad \boldsymbol{\Lambda}=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}1&2\\1&-1\end{pmatrix},$$

denn $\det\mathbf{S}=-3$. Probe: $\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}4&2\\4&-1\end{smallmatrix}\bigr)\cdot\tfrac13\bigl(\begin{smallmatrix}1&2\\1&-1\end{smallmatrix}\bigr)=\tfrac13\bigl(\begin{smallmatrix}6&6\\3&9\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$.

(b) Direkt: $\mathbf{A}^2=\bigl(\begin{smallmatrix}6&10\\5&11\end{smallmatrix}\bigr)$ und $\mathbf{A}^3=\mathbf{A}^2\mathbf{A}=\bigl(\begin{smallmatrix}12+10&12+30\\10+11&10+33\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}22&42\\21&43\end{smallmatrix}\bigr)$. Über die Eigenbasis: $\boldsymbol{\Lambda}^3=\operatorname{diag}(64;\,1)$, $\mathbf{S}\boldsymbol{\Lambda}^3=\bigl(\begin{smallmatrix}64&2\\64&-1\end{smallmatrix}\bigr)$ und

$$\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}=\frac13\begin{pmatrix}64+2&128-2\\64-1&128+1\end{pmatrix}=\begin{pmatrix}22&42\\21&43\end{pmatrix}.$$

Bei großen Potenzen ist der zweite Weg viel kürzer: Nur die Eigenwerte werden potenziert.
:::
:::

:::aufgabe Aufgabe 22 ★★ Eine Folge entkoppeln
<span class="anker" id="aufg-22"></span>

Die Fibonacci-Zahlen $0,1,1,2,3,5,\dots$ erfüllen $F_{k+2}=F_{k+1}+F_k$. Mit $\mathbf{x}_k=(F_{k+1},\,F_k)^{\top}$ ist $\mathbf{x}_{k+1}=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\mathbf{x}_k$.

<ol class="al">

<li>

Bestimme die Eigenwerte und Eigenvektoren der Matrix.

</li>

<li>

Leite mit [(7.2)](#gl-7-2) eine Formel für $F_k$ her und prüfe sie für $k=5$.

</li>

<li>

Wie verhält sich $F_{k+1}/F_k$ für große $k$, und warum?

</li>

</ol>

:::loesung
(a) $p(\lambda)=\lambda^2-\lambda-1$ mit den Nullstellen $\varphi=\tfrac{1+\sqrt5}2\approx1{,}618$ und $\psi=\tfrac{1-\sqrt5}2\approx-0{,}618$. Die erste Zeile von $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ lautet $(1-\lambda)v_1+v_2=0$; die zweite, $v_1-\lambda v_2=0$, ist wegen $p(\lambda)=0$ dazu gleichwertig. Eigenvektoren sind $\mathbf s_1=(\varphi,\,1)^{\top}$ und $\mathbf s_2=(\psi,\,1)^{\top}$.

(b) $\mathbf{x}_0=(F_1,\,F_0)^{\top}=(1,\,0)^{\top}=c_1\mathbf s_1+c_2\mathbf s_2$ verlangt $c_1+c_2=0$ und $c_1\varphi+c_2\psi=1$, also $c_1=1/(\varphi-\psi)=1/\sqrt5$ und $c_2=-1/\sqrt5$. Nach [(7.2)](#gl-7-2) ist $\mathbf{x}_k=\tfrac1{\sqrt5}(\varphi^k\mathbf s_1-\psi^k\mathbf s_2)$; die zweite Komponente ist

$$F_k=\frac{\varphi^k-\psi^k}{\sqrt5} .$$

Für $k=5$: $\varphi^5=\tfrac{11+5\sqrt5}2$ und $\psi^5=\tfrac{11-5\sqrt5}2$, also $F_5=\tfrac{5\sqrt5}{\sqrt5}=5$. Numerisch: $\varphi^5\approx11{,}090$, $\psi^5\approx-0{,}090$, $(11{,}090+0{,}090)/2{,}236\approx5{,}000$.

(c) Wegen $|\psi|<1$ geht $\psi^k$ gegen null, und $F_{k+1}/F_k$ geht gegen $\varphi\approx1{,}618$, den goldenen Schnitt. Der Anteil zum betragsgrößten Eigenwert setzt sich durch, wie in Abschnitt [7.3](#stufe-7-3); jeder weitere Schritt multipliziert ihn mit $\varphi$.
:::
:::

:::aufgabe Aufgabe 23 ★★ Spektralzerlegung
<span class="anker" id="aufg-23"></span>

<ol class="al">

<li>

Schreibe $\mathbf{A}=\bigl(\begin{smallmatrix}3&4\\4&-3\end{smallmatrix}\bigr)$ als $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ und als Summe $\lambda_1\mathbf{q}_1\mathbf{q}_1^{\top}+\lambda_2\mathbf{q}_2\mathbf{q}_2^{\top}$.

</li>

<li>

Bestimme die Hauptachsen der Form $3x_1^2+8x_1x_2-3x_2^2$ und schreibe sie als $\lambda_1c_1^2+\lambda_2c_2^2$. Welche Grundform aus Abschnitt [5.3](quadratische-formen.html#stufe-5-3) liegt vor?

</li>

<li>

Die Matrix $\Bigl(\begin{smallmatrix}2&0&0\\0&3&1\\0&1&3\end{smallmatrix}\Bigr)$ hat den Eigenwert $2$ doppelt. Gib eine Orthonormalbasis aus Eigenvektoren an. Ist sie eindeutig?

</li>

</ol>

:::loesung
(a) Spur $0$, Determinante $-9-16=-25$, also $\lambda^2-25=0$ und $\lambda=\pm5$. Zu $5$: $\bigl(\begin{smallmatrix}-2&4\\4&-8\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$. Zu $-5$: $\bigl(\begin{smallmatrix}8&4\\4&2\end{smallmatrix}\bigr)$, $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$. Mit $\mathbf{Q}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr)$ und $\boldsymbol{\Lambda}=\operatorname{diag}(5;\,-5)$ ist $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$, und

$$5\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}-5\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\begin{pmatrix}3&4\\4&-3\end{pmatrix}.$$

(b) Die Form hat genau diese Matrix. Mit $c_1=(2x_1+x_2)/\sqrt5$ und $c_2=(x_1-2x_2)/\sqrt5$ ist

$$3x_1^2+8x_1x_2-3x_2^2=5c_1^2-5c_2^2=(2x_1+x_2)^2-(x_1-2x_2)^2 ,$$

ausmultipliziert $4x_1^2+4x_1x_2+x_2^2-x_1^2+4x_1x_2-4x_2^2$. Die Hauptachsen zeigen in die Richtungen $(2,\,1)^{\top}$ und $(1,\,-2)^{\top}$. Ein Eigenwert positiv, einer negativ: ein Sattel, dessen Achsen gegen die Koordinatenachsen gedreht sind.

(c) $\mathbf{e}_1$ ist ein Eigenvektor zu $2$. Der untere Block $\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ hat die Eigenwerte $4$ mit $(1,\,1)^{\top}$ und $2$ mit $(1,\,-1)^{\top}$. Eine Orthonormalbasis aus Eigenvektoren ist also

$$\mathbf{e}_1,\qquad \tfrac1{\sqrt2}(0,\,1,\,-1)^{\top}\quad\text{zu }2,\qquad \tfrac1{\sqrt2}(0,\,1,\,1)^{\top}\quad\text{zu }4 .$$

Sie ist nicht eindeutig. Der Eigenraum zu $2$ ist die Ebene, die $\mathbf{e}_1$ und $(0,\,1,\,-1)^{\top}$ aufspannen, und jede Orthonormalbasis dieser Ebene ist recht, etwa $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1+\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$ und $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1-\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$. Eindeutig bis auf das Vorzeichen ist nur der Eigenvektor zum einfachen Eigenwert $4$.
:::
:::
