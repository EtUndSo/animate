---
title: Stufe 1: Die Schrödinger-Gleichung auf einem Gitter
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Das Teilchen in der Box
order: 4120300
summary: Für ein beliebiges Potential V(x) gibt es keine Lösung als Formel.
tags: Diskretisierung, Hüpfparameter, Hamilton-Matrix
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Für ein beliebiges Potential $V(x)$ gibt es keine Lösung als Formel. Diese Stufe macht aus der Differentialgleichung eine Matrixgleichung, die ein Rechner löst.
:::

**Die Idee.** Ein Rechner kennt keine Funktionen, nur Listen von Zahlen. Also ersetzt man $\psi(x)$ durch die Werte auf Gitterpunkten $x_\ell=\ell a$ mit dem Abstand $a$ (Abb. [1](#abb-1)). Das heißt __Diskretisierung__. Die zweite Ableitung misst, wie stark sich die Steigung ändert. Zwischen zwei Nachbarpunkten ist die Steigung fast die der Sekante. Die Krümmung am Punkt $\ell$ ist also die Differenz aus rechter und linker Sekantensteigung, geteilt durch $a$. Sie hängt nur von $\psi_\ell$ und den beiden Nachbarn ab. Das ist der ganze Mechanismus: Die kinetische Energie koppelt jeden Punkt an seine Nachbarn.

:::abbildung gemb1/k2gitter 1
Links: Die Funktion $\psi(x)$ wird nur noch an Punkten im Abstand $a$ gespeichert. Rechts: Drei Nachbarpunkte. Die zweite Ableitung am Punkt $\ell$ ist die Differenz der beiden Sekantensteigungen, geteilt durch $a$.
:::

:::satz Satz 1.1 (Diskrete Schrödinger-Gleichung)
<span class="anker" id="satz-1-1"></span>

Auf dem Gitter mit $\psi_\ell=\psi(x_\ell)$ und $V_\ell=V(x_\ell)$ gilt

<span class="anker" id="gl-1-1"></span>
$$-t_0\bigl(\psi_{\ell+1}-2\psi_\ell+\psi_{\ell-1}\bigr)+V_\ell\,\psi_\ell=E\,\psi_\ell,\qquad t_0=\frac{\hbar^2}{2ma^2}. \tag{1.1}$$
:::

⁠**So liest man das:** $\psi_\ell$ ist die komplexe Amplitude am Punkt $\ell$. $t_0$ heißt __Hüpfparameter__: eine Energie, die angibt, wie stark zwei Nachbarpunkte gekoppelt sind. Mit der Zeit hat das Symbol nichts zu tun. Im Rechenmodell ist $t_0=0{,}0381\,\mathrm{eV\,nm^2}/(0{,}2\,\mathrm{nm})^2=0{,}953$ eV. Kleineres $a$ oder kleinere Masse vergrößern $t_0$. **Gültigkeit:** $\psi$ muss sich von Punkt zu Punkt wenig ändern, also $ka\ll1$ für die Wellenzahl $k$ der Lösung. Der relative Fehler der zweiten Ableitung beträgt $(ka)^2/12$.

:::herleitung Von der Krümmung zur Gleichung
Rechts vom Punkt $\ell$ ist die Steigung $(\psi_{\ell+1}-\psi_\ell)/a$, links davon $(\psi_\ell-\psi_{\ell-1})/a$. Die zweite Ableitung ist die Änderung der Steigung je Länge:

$$\frac{\mathrm{d}^2\psi}{\mathrm{d} x^2}\bigg|_\ell\approx\frac1a\Bigl(\frac{\psi_{\ell+1}-\psi_\ell}{a}-\frac{\psi_\ell-\psi_{\ell-1}}{a}\Bigr)=\frac{\psi_{\ell+1}-2\psi_\ell+\psi_{\ell-1}}{a^2}.$$

Einsetzen in [(0.1)](von-grund-auf-was-aus-teil-1-gebraucht-wird.html#gl-0-1) ergibt [(1.1)](#gl-1-1): Der Faktor vor der Klammer ist $-\hbar^2/(2ma^2)=-t_0$.
:::

**Die Matrix.** [(1.1)](#gl-1-1) gilt an jedem Punkt. $N$ Punkte ergeben $N$ Gleichungen, zusammen $\boldsymbol H\boldsymbol\psi=E\boldsymbol\psi$:

<span class="anker" id="gl-1-2"></span>
$$\begin{pmatrix} \ddots&\ddots\\ \ddots&2t_0+V_{\ell-1}&-t_0&0\\ &-t_0&2t_0+V_\ell&-t_0\\ &0&-t_0&2t_0+V_{\ell+1}&\ddots\\ &&&\ddots&\ddots \end{pmatrix} \begin{pmatrix}\vdots\\\psi_{\ell-1}\\\psi_\ell\\\psi_{\ell+1}\\\vdots\end{pmatrix} =E\begin{pmatrix}\vdots\\\psi_{\ell-1}\\\psi_\ell\\\psi_{\ell+1}\\\vdots\end{pmatrix}. \tag{1.2}$$

$\boldsymbol H$ heißt __Hamilton-Matrix__. Auf der Hauptdiagonale steht $2t_0+V_\ell$, direkt daneben $-t_0$, sonst überall null. Der Operator $\hat H$ ist zur Tabelle geworden. Gesucht sind die Vektoren, die $\boldsymbol H$ nur um den Faktor $E$ streckt: Das ist die Eigenwertaufgabe der linearen Algebra. $N$ Punkte liefern $N$ Energien, zu jeder einen Vektor mit den Amplituden. Ein Rechner schafft das für Tausende Punkte und für jedes $V_\ell$.

**Beispiel.** Prüfe die Näherung an $\psi(x)=\sin(\pi x/L)$ mit $L=2$ nm an der Stelle $x=1$ nm. Exakt ist $\psi''=-(\pi/L)^2=-2{,}467\,\mathrm{nm^{-2}}$. Mit $a=0{,}2$ nm und $\psi_{\ell\pm1}=\cos(0{,}1\,\pi)=0{,}951$ ergibt die Differenz $-2{,}447\,\mathrm{nm^{-2}}$. Die Abweichung von 0,82 % ist genau $(ka)^2/12$ mit $ka=0{,}314$. **Grenzfall:** Für $a\to0$ wächst $t_0$ wie $1/a^2$, die Klammer in [(1.1)](#gl-1-1) schrumpft wie $a^2$. Das Produkt bleibt endlich, und [(0.1)](von-grund-auf-was-aus-teil-1-gebraucht-wird.html#gl-0-1) kehrt zurück.

Das Gitter ist mehr als ein Rechentrick: In einem Kristall sitzen die Atome an regelmäßigen Plätzen, und ein Elektron wechselt von Atom zu Atom. [(1.1)](#gl-1-1) ist das einfachste Modell davon, vereinfacht in den Werten von $t_0$ und $V_\ell$.

:::frage Warum steht $2t_0$ auf der Diagonale, obwohl dort gar kein Potential sitzt?
Der Term gehört zur kinetischen Energie. Die Krümmung vergleicht $\psi_\ell$ mit den Nachbarn, und dafür braucht man $\psi_\ell$ selbst. Nur die Summe der drei Einträge einer Zeile zählt: Für ein konstantes $\psi$ heben sich $2t_0$, $-t_0$ und $-t_0$ auf, die kinetische Energie ist null.
:::

:::aufgabe Aufgabe 1 ★ Ein Gitter aufstellen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $t_0$ für $a=0{,}25$ nm und $m=m_0$. Was wird aus $t_0$, wenn $a$ sich halbiert? Was bei $m=0{,}2\,m_0$?

</li>

<li>

Vier Gitterpunkte, $t_0=0{,}6$ eV, $V_\ell=(0;\;0{,}5;\;0;\;0)$ eV, und links und rechts der Punkte ist $\psi=0$. Schreibe die Hamilton-Matrix hin.

</li>

<li>

Grenzfall: Zeige, dass $\psi_\ell=c\,\ell+d$ die Klammer in [(1.1)](#gl-1-1) null macht. Was bedeutet das?

</li>

</ol>

:::loesung
(a) $t_0=0{,}0381\,\mathrm{eV\,nm^2}/(0{,}25\,\mathrm{nm})^2=0{,}61$ eV. Halbes $a$ ergibt das Vierfache, 2,44 eV. Mit $m=0{,}2\,m_0$ ist $t_0$ fünfmal so groß, 3,05 eV. (b) Mit $2t_0=1{,}2$ eV:

$$\boldsymbol H=\begin{pmatrix}1{,}2&-0{,}6&0&0\\-0{,}6&1{,}7&-0{,}6&0\\0&-0{,}6&1{,}2&-0{,}6\\0&0&-0{,}6&1{,}2\end{pmatrix}\,\mathrm{eV}.$$

(c) $c(\ell+1)+d-2(c\ell+d)+c(\ell-1)+d=0$. Eine Gerade hat keine Krümmung, sie trägt keine kinetische Energie.
:::
:::
