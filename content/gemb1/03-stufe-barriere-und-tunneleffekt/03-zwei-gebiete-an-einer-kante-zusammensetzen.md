---
title: Stufe 1: Zwei Gebiete an einer Kante zusammensetzen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4130300
summary: Bisher war das Potential konstant oder die Wand unendlich hoch.
tags: Stetigkeitsbedingung, Reflexionsamplitude, Transmissionsamplitude
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bisher war das Potential konstant oder die Wand unendlich hoch. Jetzt springt es an einer Stelle um einen endlichen Betrag. Diese Stufe setzt die Wellen links und rechts der Kante zu einer einzigen Wellenfunktion zusammen.
:::

**Die Idee.** Links der Kante ist $V=0$, rechts $V=V_0$. Solche Potentialstufen gibt es an der Grenze eines Festkörpers zum Vakuum und zwischen zwei verschieden dotierten Halbleitern, also Halbleitern mit verschiedenen Fremdatomen. In jedem Gebiet für sich gilt [(0.1)](von-grund-auf-wellen-bei-konstantem-potential-rechnen-in-ev.html#gl-0-1). Die Energie $E$ ist überall dieselbe, denn das Potential hängt nicht von der Zeit ab. Die Kante tauscht nur kinetische gegen potentielle Energie. Rechts bleibt weniger kinetische Energie, also ist $k$ kleiner und die Wellenlänge größer (Abb. [1](#abb-1)).

:::abbildung gemb1/k3stufe 1
Dieselbe Energie $E$ in beiden Gebieten. Mitte: Potentialverlauf mit $V_0=2$ eV. Links und rechts: Parabel $E(k)$ des jeweiligen Gebiets, im Gebiet II um $V_0$ angehoben. Blau: $E=3$ eV trifft beide Parabeln, rechts bei kleinerem $k$. Rot: $E=0{,}5$ eV liegt unter der rechten Parabel.
:::

Klassisch gibt es zwei Fälle. Für $E\le V_0$ kehrt jedes Teilchen um. Für $E>V_0$ läuft jedes weiter, mit der kinetischen Energie $E-V_0$. Experimente bestätigen beides in den Grenzfällen $E\gg V_0$ und $E\ll V_0$. Diese Grenzfälle muss auch die Wellenrechnung liefern. Sie beginnt hier mit $E>V_0$.

:::definition Definition 1.1 (Potentialstufe)
<span class="anker" id="satz-1-1"></span>

Die Potentialstufe der Höhe $V_0$ bei $x=0$ ist

<span class="anker" id="gl-1-1"></span>
$$V(x)=\begin{cases}0&\text{für }x<0\quad\text{(Gebiet I)}\\V_0&\text{für }x\ge0\quad\text{(Gebiet II).}\end{cases} \tag{1.1}$$
:::

:::satz Satz 1.2 (Lösung an der Stufe für $E>V_0$)
<span class="anker" id="satz-1-2"></span>

In beiden Gebieten gilt $\psi''=-k^2\psi$ mit eigener Wellenzahl:

<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \psi_\mathrm I(x)&=A\,\mathrm{e}^{\mathrm{j} k_\mathrm Ix}+B\,\mathrm{e}^{-\mathrm{j} k_\mathrm Ix},&k_\mathrm I&=\frac{\sqrt{2mE}}{\hbar},\\ \psi_\mathrm{II}(x)&=C\,\mathrm{e}^{\mathrm{j} k_\mathrm{II}x}+D\,\mathrm{e}^{-\mathrm{j} k_\mathrm{II}x},&k_\mathrm{II}&=\frac{\sqrt{2m(E-V_0)}}{\hbar}. \end{aligned} \tag{1.2}$$

Aus Gebiet II läuft keine Welle zurück, also ist $D=0$. An der Kante gilt die __Stetigkeitsbedingung__: $\psi$ und seine Ableitung gehen ohne Sprung ineinander über,

<span class="anker" id="gl-1-3"></span>
$$\psi_\mathrm I(0)=\psi_\mathrm{II}(0),\qquad\frac{\mathrm{d}\psi_\mathrm I}{\mathrm{d} x}\bigg|_{0}=\frac{\mathrm{d}\psi_\mathrm{II}}{\mathrm{d} x}\bigg|_{0}. \tag{1.3}$$

Daraus folgen $A+B=C$ und $A-B=(k_\mathrm{II}/k_\mathrm I)\,C$, also

<span class="anker" id="gl-1-4"></span>
$$\frac BA=\frac{k_\mathrm I-k_\mathrm{II}}{k_\mathrm I+k_\mathrm{II}},\qquad\frac CA=\frac{2k_\mathrm I}{k_\mathrm I+k_\mathrm{II}}. \tag{1.4}$$
:::

⁠**So liest man das:** $A$ gehört zur einlaufenden, $B$ zur reflektierten, $C$ zur durchgelassenen Welle. Setzt man $A=1$, heißt $B$ __Reflexionsamplitude__ und $C$ __Transmissionsamplitude__. Die Größe von $A$ legt nur fest, wie viele Elektronen einlaufen. Gezählt: vier Konstanten, $D=0$ und zwei Bedingungen. Es bleibt eine Konstante frei, und nur die Verhältnisse sind bestimmt. Addition und Subtraktion der beiden Gleichungen ergeben die Schreibweise

<span class="anker" id="gl-1-5"></span>
$$\psi_\mathrm I(x)=\frac C2\Bigl[\Bigl(1+\frac{k_\mathrm{II}}{k_\mathrm I}\Bigr)\mathrm{e}^{\mathrm{j} k_\mathrm Ix}+\Bigl(1-\frac{k_\mathrm{II}}{k_\mathrm I}\Bigr)\mathrm{e}^{-\mathrm{j} k_\mathrm Ix}\Bigr],\qquad\psi_\mathrm{II}(x)=C\,\mathrm{e}^{\mathrm{j} k_\mathrm{II}x}. \tag{1.5}$$

⁠**Gültigkeit:** zeitunabhängiges Potential, endliche Stufenhöhe, und die Kante ist viel schmaler als die Wellenlänge.

:::herleitung Warum $\psi$ und $\mathrm{d}\psi/\mathrm{d} x$ stetig sind
Stellt man die Schrödinger-Gleichung um, steht dort $\psi''=\frac{2m}{\hbar^2}\,(V-E)\,\psi$. Integriert man über ein kleines Stück von $-\varepsilon$ bis $+\varepsilon$ um die Kante, folgt

$$\psi'(\varepsilon)-\psi'(-\varepsilon)=\frac{2m}{\hbar^2}\int_{-\varepsilon}^{\varepsilon}(V-E)\,\psi\,\mathrm{d} x.$$

$V$ ist endlich und $\psi$ beschränkt, also geht das Integral für $\varepsilon\to0$ gegen null. Damit ist $\psi'$ stetig. Hätte $\psi$ selbst einen Sprung, wäre $\psi'$ dort unendlich groß. Das erlaubt die Gleichung nicht, und $|\psi|^2$ hätte an der Kante keinen eindeutigen Wert. Einsetzen von [(1.2)](#gl-1-2) mit $D=0$ in [(1.3)](#gl-1-3) ergibt $A+B=C$ und $\mathrm{j} k_\mathrm I(A-B)=\mathrm{j} k_\mathrm{II}C$. Addition liefert $A=\frac C2(1+k_\mathrm{II}/k_\mathrm I)$, Subtraktion $B=\frac C2(1-k_\mathrm{II}/k_\mathrm I)$.
:::

::::beispiel
Für $E=3$ eV und $V_0=2$ eV liefert [(0.3)](von-grund-auf-wellen-bei-konstantem-potential-rechnen-in-ev.html#gl-0-3) $k_\mathrm I=8{,}87\,\mathrm{nm^{-1}}$ und $k_\mathrm{II}=5{,}12\,\mathrm{nm^{-1}}$, also $\lambda_\mathrm I=0{,}708$ nm und $\lambda_\mathrm{II}=1{,}226$ nm. Aus [(1.4)](#gl-1-4) folgen $B/A=0{,}268$ und $C/A=1{,}268$. Probe: $1+0{,}268=1{,}268$.
::::

⁠**Grenzfälle:** Für $V_0\to0$ ist $k_\mathrm{II}=k_\mathrm I$, also $B=0$ und $C=A$: Ohne Stufe wird nichts reflektiert. Für $E\to V_0$ geht $k_\mathrm{II}\to0$ und $B\to A$.

:::frage In der Box aus Teil 2 hatte $\psi$ an der Wand einen Knick. Warum ist das hier verboten?
Die Herleitung setzt ein endliches $V$ voraus. An einer unendlich hohen Wand ist das Integral nicht klein, $\psi'$ darf dort springen. An jeder endlichen Stufe bleibt die Kurve glatt. Ihre Krümmung $\psi''$ darf springen, ihre Steigung nicht.
:::

:::aufgabe Aufgabe 1 ★ Rechnen in eV und nm
<span class="anker" id="aufg-1"></span>

Ein Elektron mit $E=1{,}2$ eV trifft auf eine Stufe mit $V_0=0{,}8$ eV.

<ol class="al">

<li>

Bestätige $2m_0/\hbar^2=26{,}25\,/(\mathrm{eV\,nm^2})$ aus den eV-Werten von $m_0$ und $\hbar$.

</li>

<li>

Berechne $k_\mathrm I$, $k_\mathrm{II}$, $\lambda_\mathrm I$ und $\lambda_\mathrm{II}$.

</li>

<li>

Berechne $B/A$ und $C/A$. Warum kommen dieselben Zahlen heraus wie im Beispiel, obwohl alle Energien andere sind?

</li>

</ol>

:::loesung
(a) $2\cdot5{,}686\cdot10^{-12}\,\mathrm{eV\,s^2/m^2}/(6{,}582\cdot10^{-16}\,\mathrm{eV\,s})^2=2{,}625\cdot10^{19}\,/(\mathrm{eV\,m^2})=26{,}25\,/(\mathrm{eV\,nm^2})$. (b) $k_\mathrm I=5{,}61\,\mathrm{nm^{-1}}$, $k_\mathrm{II}=3{,}24\,\mathrm{nm^{-1}}$, $\lambda_\mathrm I=1{,}12$ nm, $\lambda_\mathrm{II}=1{,}94$ nm. (c) $B/A=(5{,}61-3{,}24)/(5{,}61+3{,}24)=0{,}268$ und $C/A=2\cdot5{,}61/8{,}85=1{,}268$. Beide hängen nur von $k_\mathrm{II}/k_\mathrm I=\sqrt{1-V_0/E}$ ab, und $V_0/E=2/3$ ist in beiden Fällen gleich.
:::
:::

:::aufgabe Aufgabe 2 ★★ Das Gleichungssystem aufstellen
<span class="anker" id="aufg-2"></span>

Das Potential hat zwei Kanten: $V=0$ für $x<0$, $V=V_1$ für $0\le x<L$, $V=V_2$ für $x\ge L$, mit $E>V_2>V_1$.

<ol class="al">

<li>

Schreibe die Schrödinger-Gleichung je Gebiet auf. Wie groß sind die Wellenzahlen bei $E=3$ eV, $V_1=1$ eV, $V_2=2$ eV?

</li>

<li>

Stelle den Ansatz auf. Welche Amplitude ist null, und warum?

</li>

<li>

Schreibe alle Stetigkeitsbedingungen auf. Wie viele Amplituden bleiben nach dem Lösen frei?

</li>

</ol>

:::loesung
(a) Je Gebiet gilt $-\frac{\hbar^2}{2m}\psi''+V\psi=E\psi$ mit $V=0$, $V_1$, $V_2$, also $k=\sqrt{2m(E-V)}/\hbar$: $8{,}87\,\mathrm{nm^{-1}}$, $7{,}25\,\mathrm{nm^{-1}}$, $5{,}12\,\mathrm{nm^{-1}}$. (b) $\psi_\mathrm I=A\mathrm{e}^{\mathrm{j} k_\mathrm Ix}+B\mathrm{e}^{-\mathrm{j} k_\mathrm Ix}$, $\psi_\mathrm{II}=C\mathrm{e}^{\mathrm{j} k_\mathrm{II}x}+D\mathrm{e}^{-\mathrm{j} k_\mathrm{II}x}$, $\psi_\mathrm{III}=F\mathrm{e}^{\mathrm{j} k_\mathrm{III}x}+G\mathrm{e}^{-\mathrm{j} k_\mathrm{III}x}$. $G=0$, denn von rechts läuft keine Welle ein. In Gebiet II sind beide Terme nötig, die rechte Kante reflektiert. (c) $A+B=C+D$; $k_\mathrm I(A-B)=k_\mathrm{II}(C-D)$; $C\mathrm{e}^{\mathrm{j} k_\mathrm{II}L}+D\mathrm{e}^{-\mathrm{j} k_\mathrm{II}L}=F\mathrm{e}^{\mathrm{j} k_\mathrm{III}L}$; $k_\mathrm{II}(C\mathrm{e}^{\mathrm{j} k_\mathrm{II}L}-D\mathrm{e}^{-\mathrm{j} k_\mathrm{II}L})=k_\mathrm{III}F\mathrm{e}^{\mathrm{j} k_\mathrm{III}L}$. Vier Gleichungen für fünf Amplituden: Eine bleibt frei.
:::
:::
