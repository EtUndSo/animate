---
title: Stufe 4: Tunneln durch eine dünne Wand
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4130600
summary: Bisher war das verbotene Gebiet unendlich lang.
tags: Tunnelwahrscheinlichkeit
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher war das verbotene Gebiet unendlich lang. Jetzt endet es nach der Breite $L$. Diese Stufe berechnet, wie viel der abklingenden Welle auf der anderen Seite als laufende Welle herauskommt.
:::

**Die Idee.** In der Barriere klingt $\psi$ ab, ist an der rechten Kante aber nicht null. Dort gilt wieder die Stetigkeitsbedingung: $\psi$ und $\psi'$ müssen in eine Lösung für $V=0$ übergehen, und das ist eine laufende Welle. Das ist der Tunneleffekt. Merklich wird er, wenn $L$ nicht viel größer als $\delta$ ist. Gerechnet wird wie an einer einzelnen Kante, nur zweimal. Die rechte Kante reflektiert einen kleinen Teil zurück, deshalb steckt in der Barriere auch ein ansteigender Anteil (Abb. [4](#abb-4)). Solche Barrieren gibt es an Kontakten zwischen Metall und Halbleiter und an Atomkernen.

:::abbildung gemb1/k3barriere 4
Oben: stationäre Lösung für $E=0{,}5$ eV, $V_0=2$ eV und $L=0{,}4$ nm, mit $A=1$. Links fast die stehende Welle von Stufe [3](die-welle-dringt-in-die-wand-ein.html#stufe-3), in der Barriere der Abfall, rechts eine laufende Welle mit derselben Wellenlänge und der Amplitude 0,14. Unten: Wellenpaket mit mittlerer Energie 1,5 eV an derselben Barriere, numerisch gerechnet. Gezeigt ist $|\psi|^2$ zu Beginn und 17 fs später. Das Elektron ist dann mit 17 % Wahrscheinlichkeit rechts, ein wenig mehr als $T=0{,}16$ bei 1,5 eV, denn das Paket enthält auch höhere Energien.
:::

:::definition Definition 4.1 (Rechteckbarriere)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$V(x)=\begin{cases}0&\text{für }x\le0\quad\text{(Gebiet I)}\\V_0&\text{für }0<x<L\quad\text{(Gebiet II)}\\0&\text{für }x\ge L\quad\text{(Gebiet III).}\end{cases} \tag{4.1}$$
:::

Für $0<E<V_0$ ist $k=\sqrt{2mE}/\hbar$ die Wellenzahl in den Gebieten I und III, $\kappa=\sqrt{2m(V_0-E)}/\hbar$ die Abklingkonstante in Gebiet II. Der Ansatz lautet

<span class="anker" id="gl-4-2"></span>
$$\psi_\mathrm I=A\,\mathrm{e}^{\mathrm{j} kx}+B\,\mathrm{e}^{-\mathrm{j} kx},\qquad\psi_\mathrm{II}=C\,\mathrm{e}^{-\kappa x}+D\,\mathrm{e}^{\kappa x},\qquad\psi_\mathrm{III}=F\,\mathrm{e}^{\mathrm{j} kx}+G\,\mathrm{e}^{-\mathrm{j} kx}. \tag{4.2}$$

Aus Gebiet III läuft nichts zurück, also $G=0$. Die Stetigkeit bei $x=0$ und $x=L$ liefert vier Gleichungen. Das sind fünf Bedingungen für sechs Amplituden, und gesucht ist nur das Verhältnis $F/A$.

:::satz Satz 4.2 (Transmissionskoeffizient der Rechteckbarriere)
<span class="anker" id="satz-4-2"></span>

Für $0<E<V_0$ gilt, wegen $|v_\mathrm{III}|=|v_\mathrm I|$,

<span class="anker" id="gl-4-3"></span>
$$T=\frac{|F|^2\,|v_\mathrm{III}|}{|A|^2\,|v_\mathrm I|}=\Bigl|\frac FA\Bigr|^2=\frac{1}{\cosh^2(\kappa L)+\frac14\bigl(\frac\kappa k-\frac k\kappa\bigr)^2\sinh^2(\kappa L)}=\Bigl[1+\frac{\sinh^2(\kappa L)}{4\frac{E}{V_0}\bigl(1-\frac{E}{V_0}\bigr)}\Bigr]^{-1}. \tag{4.3}$$
:::

⁠**So liest man das:** $\sinh x=\frac12(\mathrm{e}^x-\mathrm{e}^{-x})$ und $\cosh x=\frac12(\mathrm{e}^x+\mathrm{e}^{-x})$ sind die Hyperbelfunktionen, mit $\cosh^2x-\sinh^2x=1$. $\kappa L=L/\delta$ zählt, wie viele Eindringtiefen die Barriere dick ist. Der Nenner $4\frac E{V_0}(1-\frac E{V_0})$ liegt zwischen 0 und 1. $T$ heißt auch __Tunnelwahrscheinlichkeit__. Es gilt wieder $R+T=1$. **Gültigkeit:** rechteckige Barriere, scharfe Kanten, gleiches Potential auf beiden Seiten, dieselbe Masse in allen Gebieten.

:::herleitung Von den Stetigkeitsbedingungen zu $T$
<ol>

<li>

Stetigkeit bei $x=0$: $A+B=C+D$ und $\mathrm{j} k(A-B)=\kappa(D-C)$. Geteilt durch $\mathrm{j} k$: $A-B=\mathrm{j}\frac\kappa k(C-D)$. Addition ergibt

$$A=\tfrac C2\bigl(1+\mathrm{j}\tfrac\kappa k\bigr)+\tfrac D2\bigl(1-\mathrm{j}\tfrac\kappa k\bigr).$$

</li>

<li>

Stetigkeit bei $x=L$ mit $G=0$: $C\mathrm{e}^{-\kappa L}+D\mathrm{e}^{\kappa L}=F\mathrm{e}^{\mathrm{j} kL}$ und $C\mathrm{e}^{-\kappa L}-D\mathrm{e}^{\kappa L}=-\mathrm{j}\frac k\kappa F\mathrm{e}^{\mathrm{j} kL}$. Addition und Subtraktion ergeben

$$C=\tfrac F2\,\mathrm{e}^{(\kappa+\mathrm{j} k)L}\bigl(1-\mathrm{j}\tfrac k\kappa\bigr),\qquad D=\tfrac F2\,\mathrm{e}^{(-\kappa+\mathrm{j} k)L}\bigl(1+\mathrm{j}\tfrac k\kappa\bigr).$$

</li>

<li>

Einsetzen mit $(1+\mathrm{j}\frac\kappa k)(1-\mathrm{j}\frac k\kappa)=2+\mathrm{j} c$ und $c=\frac\kappa k-\frac k\kappa$:

$$A=\tfrac F4\,\mathrm{e}^{\mathrm{j} kL}\bigl[(2+\mathrm{j} c)\mathrm{e}^{\kappa L}+(2-\mathrm{j} c)\mathrm{e}^{-\kappa L}\bigr]=F\,\mathrm{e}^{\mathrm{j} kL}\bigl[\cosh(\kappa L)+\mathrm{j}\tfrac c2\sinh(\kappa L)\bigr].$$

</li>

<li>

Der Betrag zum Quadrat ergibt die erste Form von [(4.3)](#gl-4-3). Für die zweite setzt man $\cosh^2=1+\sinh^2$ ein und benutzt $1+\frac{c^2}4=\frac14(\frac\kappa k+\frac k\kappa)^2=\frac{(k^2+\kappa^2)^2}{4k^2\kappa^2}$. Mit $k^2\propto E$ und $\kappa^2\propto V_0-E$ wird das $\frac{V_0^2}{4E(V_0-E)}$.

</li>

</ol>
:::

::::beispiel
Für $E=0{,}5$ eV und $L=1$ nm ist $\kappa L=6{,}27$, $\sinh^2(\kappa L)=7{,}05\cdot10^{4}$ und $4\frac E{V_0}(1-\frac E{V_0})=0{,}75$. Das ergibt $T=1{,}06\cdot10^{-5}$: Eines von 94 000 Elektronen kommt durch. Mit $L=0{,}4$ nm ist $T=0{,}020$, die Amplitude rechts also $\sqrt T=0{,}14$.
::::

⁠**Grenzfälle:** $L\to0$ ergibt $T=1$, ohne Barriere läuft alles durch. $L\to\infty$ ergibt $T\to0$ wie in Stufe [3](die-welle-dringt-in-die-wand-ein.html#stufe-3). $V_0\to\infty$ bei festem $E$ ergibt ebenfalls $T\to0$.

:::frage Verliert das Elektron beim Tunneln Energie? Die Welle ist rechts doch viel kleiner.
Nein. Rechts ist $V=0$, also ist $k$ dasselbe wie links, die Wellenlänge ändert sich nicht. Die kleine Amplitude bedeutet eine kleine Wahrscheinlichkeit, kein schwächeres Elektron. Wer rechts ankommt, hat die volle Energie $E$. Der Rest der Wahrscheinlichkeit ist reflektiert.
:::

:::aufgabe Aufgabe 7 ★★★ Die Barriere als Matrizenprodukt
<span class="anker" id="aufg-7"></span>

Die vier Stetigkeitsbedingungen lassen sich mit Matrizen sortieren. Lass dafür $G$ zunächst stehen.

<ol class="al">

<li>

Schreibe die Bedingungen als $M_1(A,B)^\top=M_2(C,D)^\top$ und $M_3(C,D)^\top=M_4(F,G)^\top$. Teile in $M_2$ und $M_4$ so, dass in $M_1$ nur $\pm1$ und in $M_3$ nur $\pm\mathrm{e}^{\pm\kappa L}$ stehen.

</li>

<li>

Bestimme $M_1^{-1}$ und $M_3^{-1}$ mit der Formel für die Inverse einer $2\times2$-Matrix.

</li>

<li>

Berechne $M_{\mathrm{I,II}}=M_1^{-1}M_2$ und $M_{\mathrm{II,III}}=M_3^{-1}M_4$.

</li>

<li>

Berechne das Element $M_{11}$ von $M=M_{\mathrm{I,II}}M_{\mathrm{II,III}}$. Zeige, dass mit $G=0$ daraus [(4.3)](#gl-4-3) folgt.

</li>

</ol>

:::loesung
(a) Aus den Gleichungen der Herleitung, aber mit $G\ne0$:

$$M_1=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\ M_2=\begin{pmatrix}1&1\\\mathrm{j}\frac\kappa k&-\mathrm{j}\frac\kappa k\end{pmatrix},\ M_3=\begin{pmatrix}\mathrm{e}^{-\kappa L}&\mathrm{e}^{\kappa L}\\-\mathrm{e}^{-\kappa L}&\mathrm{e}^{\kappa L}\end{pmatrix},\ M_4=\begin{pmatrix}\mathrm{e}^{\mathrm{j} kL}&\mathrm{e}^{-\mathrm{j} kL}\\\mathrm{j}\frac k\kappa\mathrm{e}^{\mathrm{j} kL}&-\mathrm{j}\frac k\kappa\mathrm{e}^{-\mathrm{j} kL}\end{pmatrix}.$$

(b) Die Determinanten sind $-2$ und $2$, also $M_1^{-1}=\frac12M_1$ und $M_3^{-1}=\frac12\begin{pmatrix}\mathrm{e}^{\kappa L}&-\mathrm{e}^{\kappa L}\\\mathrm{e}^{-\kappa L}&\mathrm{e}^{-\kappa L}\end{pmatrix}$.

(c) Ausmultiplizieren ergibt

$$M_{\mathrm{I,II}}=\frac12\begin{pmatrix}1+\mathrm{j}\frac\kappa k&1-\mathrm{j}\frac\kappa k\\1-\mathrm{j}\frac\kappa k&1+\mathrm{j}\frac\kappa k\end{pmatrix},\quad M_{\mathrm{II,III}}=\frac12\begin{pmatrix}(1-\mathrm{j}\frac k\kappa)\mathrm{e}^{(\kappa+\mathrm{j} k)L}&(1+\mathrm{j}\frac k\kappa)\mathrm{e}^{(\kappa-\mathrm{j} k)L}\\(1+\mathrm{j}\frac k\kappa)\mathrm{e}^{(-\kappa+\mathrm{j} k)L}&(1-\mathrm{j}\frac k\kappa)\mathrm{e}^{(-\kappa-\mathrm{j} k)L}\end{pmatrix}.$$

(d) Mit $c=\frac\kappa k-\frac k\kappa$ ist $(1+\mathrm{j}\frac\kappa k)(1-\mathrm{j}\frac k\kappa)=2+\mathrm{j} c$ und $(1-\mathrm{j}\frac\kappa k)(1+\mathrm{j}\frac k\kappa)=2-\mathrm{j} c$, also $M_{11}=\frac14\mathrm{e}^{\mathrm{j} kL}[(2+\mathrm{j} c)\mathrm{e}^{\kappa L}+(2-\mathrm{j} c)\mathrm{e}^{-\kappa L}]=\mathrm{e}^{\mathrm{j} kL}[\cosh(\kappa L)+\mathrm{j}\frac c2\sinh(\kappa L)]$. Mit $G=0$ ist $A=M_{11}F$, also $T=1/|M_{11}|^2=1/(\cosh^2(\kappa L)+\frac{c^2}4\sinh^2(\kappa L))$.
:::
:::

:::aufgabe Aufgabe 8 ★★ Grenzfälle der Formel
<span class="anker" id="aufg-8"></span>

Für $V_0=2$ eV und $E=0{,}5$ eV, wenn nichts anderes steht:

<ol class="al">

<li>

Zeichne $V(x)$ für $L=0{,}2$ nm und skizziere darüber den nach rechts laufenden Anteil von $\psi$ in allen drei Gebieten. Wie groß ist die Wellenlänge links und rechts?

</li>

<li>

Berechne $T$ bei $L=0{,}05$ nm, 0,2 nm und 3 nm.

</li>

<li>

Zeige für $E=V_0/2$: $T=1/\cosh^2(\kappa L)$. Warum verschwindet ein Term?

</li>

<li>

Zeige für $E\to V_0$: $T\to1/(1+mV_0L^2/(2\hbar^2))$. Berechne den Wert für $L=1$ nm.

</li>

</ol>

:::loesung
(a) Links läuft eine Welle mit $\lambda=1{,}73$ nm. In der Barriere fällt die Kurve glatt ab, ohne Knick an den Kanten. Rechts läuft eine Welle mit denselben 1,73 nm und der Amplitude $\sqrt T=0{,}47$. (b) Mit $\kappa=6{,}27\,\mathrm{nm^{-1}}$: $T=0{,}88$ bei 0,05 nm, 0,22 bei 0,2 nm, $1{,}3\cdot10^{-16}$ bei 3 nm. (c) Bei $E=V_0/2$ ist $k=\kappa$, also $\frac\kappa k-\frac k\kappa=0$. Der zweite Term in [(4.3)](#gl-4-3) entfällt: $T=1/\cosh^2(\kappa L)$. (d) Für $E\to V_0$ geht $\kappa L\to0$, also $\sinh^2(\kappa L)\approx\kappa^2L^2=\frac{2m}{\hbar^2}(V_0-E)L^2$. Der Nenner in [(4.3)](#gl-4-3) geht gegen $4\frac{V_0-E}{V_0}$. $V_0-E$ kürzt sich, und der Bruch im Nenner wird $\frac14\cdot26{,}25\cdot2\cdot1=13{,}1$, also $T=0{,}071$. In der Barriere ist $\psi$ dann eine Gerade. Die einlaufende Welle passt dazu schlecht und wird größtenteils reflektiert.
:::
:::
