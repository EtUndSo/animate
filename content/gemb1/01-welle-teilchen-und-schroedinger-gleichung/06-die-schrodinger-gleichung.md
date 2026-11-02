---
title: Stufe 4: Die Schrödinger-Gleichung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
order: 4110600
summary: Die Wellenfunktion sagt, wo das Elektron auftaucht.
tags: Hamilton-Funktion, Operatoren, Hamilton-Operator, Potential, Korrespondenzprinzip, stationär, Separationsansatz, Eigenwertgleichung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Wellenfunktion sagt, wo das Elektron auftaucht. Diese Stufe gibt die Gleichung, die sie festlegt, und trennt Ort und Zeit, wenn sich das Potential nicht ändert.
:::

**Die Idee.** Klassisch gilt $E_\mathrm{kin}+V=E$ mit $E_\mathrm{kin}=\frac12mv^2=p^2/(2m)$, und $V$ ist die potentielle Energie. Die Summe $H=p^2/(2m)+V$ heißt __Hamilton-Funktion__. In der Quantenmechanik werden Messgrößen zu __Operatoren__, also Rechenvorschriften, die aus einer Funktion eine andere machen. Welche Vorschrift zu $p$ und $E$ gehört, liest man an [(3.3)](die-wellenfunktion-und-ihre-deutung.html#gl-3-3) ab: Die Ableitung nach $x$ erzeugt den Faktor $\mathrm{j} k$, die Ableitung nach $t$ den Faktor $-\mathrm{j}\omega$. Mit [(2.1)](teilchen-und-wellen.html#gl-2-1) gehören also

<span class="anker" id="gl-4-1"></span>
$$\hat p=\frac{\hbar}{\mathrm{j}}\frac{\partial}{\partial x},\qquad\hat{\boldsymbol p}=\frac{\hbar}{\mathrm{j}}\nabla\quad\text{mit}\quad\nabla=\boldsymbol e_x\frac{\partial}{\partial x}+\boldsymbol e_y\frac{\partial}{\partial y}+\boldsymbol e_z\frac{\partial}{\partial z},\qquad\hat E=\mathrm{j}\hbar\frac{\partial}{\partial t} \tag{4.1}$$

zu Impuls und Energie, $\hat p$ im Eindimensionalen, $\hat{\boldsymbol p}$ im Raum. Dabei sind $\boldsymbol e_x,\boldsymbol e_y,\boldsymbol e_z$ die Einheitsvektoren, $\nabla$ bildet den Gradienten. Setzt man die Operatoren in die Hamilton-Funktion ein und wendet sie auf $\Psi$ an, entsteht die Bewegungsgleichung der Welle.

:::satz Satz 4.1 (Zeitabhängige Schrödinger-Gleichung)
<span class="anker" id="satz-4-1"></span>

Die Wellenfunktion eines Teilchens der Masse $m$ in der potentiellen Energie $V(x,t)$ gehorcht

<span class="anker" id="gl-4-2"></span>
$$\mathrm{j}\hbar\frac{\partial}{\partial t}\Psi(x,t)=\Bigl(-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x,t)\Bigr)\Psi(x,t). \tag{4.2}$$
:::

⁠**So liest man das:** Die Klammer ist der __Hamilton-Operator__ $\hat H$, der Operator der Gesamtenergie. Der erste Summand ist $\hat p^2/(2m)$, die kinetische Energie. Er misst die Krümmung von $\Psi$: Kurze Wellenlänge heißt starke Krümmung und hohe kinetische Energie. $V$ misst man in J oder eV und nennt es kurz __Potential__, obwohl es eine Energie ist. Für ein Elektron im elektrostatischen Potential $\varphi$ (in Volt) ist $V=-e\varphi$. Kennt man $\Psi$ zur Zeit null, liegt $\Psi$ für alle späteren Zeiten fest. **Gültigkeit:** $v$ weit unter Lichtgeschwindigkeit. Solange $V$ endlich ist, muss die Lösung stetig und stetig differenzierbar sein, denn ein Knick gäbe in der zweiten Ableitung einen unendlichen Wert, dem kein anderer Term gegenübersteht.

Diese Gleichung lässt sich nicht aus Tieferem herleiten, ebenso wenig wie die newtonschen Gesetze oder die maxwellschen Gleichungen. Sie ist der erfolgreiche Versuch, die de-Broglie-Beziehung auf bewegte Teilchen anzuwenden. Ihre Gültigkeit stützt sich allein darauf, dass sie alle Beobachtungen widerspruchsfrei beschreibt, andere denkbare Wellengleichungen tun das nicht. Für große Massen und Abmessungen gehen ihre Lösungen in die klassischen Bahnen über (__Korrespondenzprinzip__).

**Stationäre Probleme.** Oft hängt das Potential nicht von der Zeit ab, $V(x,t)\to V(x)$. Solche Probleme heißen __stationär__. Dann lassen sich Ort und Zeit trennen.

:::satz Satz 4.2 (Zeitunabhängige Schrödinger-Gleichung)
<span class="anker" id="satz-4-2"></span>

Für $V=V(x)$ gibt es Lösungen $\Psi(x,t)=\psi(x)\,\mathrm{e}^{-\mathrm{j} Et/\hbar}$, deren Ortsanteil

<span class="anker" id="gl-4-3"></span>
$$\Bigl(-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\Bigr)\psi(x)=E\,\psi(x),\qquad\text{kurz}\quad\hat H\psi=E\,\psi, \tag{4.3}$$

erfüllt. In drei Dimensionen lautet sie, in zwei Dimensionen ohne den $z$-Term,

<span class="anker" id="gl-4-4"></span>
$$\Bigl(-\frac{\hbar^2}{2m}\Bigl(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}\Bigr)+V(\boldsymbol r)\Bigr)\psi(\boldsymbol r)=E\,\psi(\boldsymbol r),\quad\text{kurz}\quad-\frac{\hbar^2}{2m}\nabla^2\psi+V\psi=E\,\psi. \tag{4.4}$$
:::

:::herleitung Trennung von Ort und Zeit
Der __Separationsansatz__ ist $\Psi(x,t)=\psi(x)\,g(t)$. Einsetzen in [(4.2)](#gl-4-2) und Teilen durch $\psi\,g$ gibt

$$\mathrm{j}\hbar\,\frac{\mathrm{d} g/\mathrm{d} t}{g(t)}=\frac{\hat H\psi(x)}{\psi(x)}=\text{konst}=E.$$

Links steht nur $t$, rechts nur $x$. Beide können für alle $x$ und $t$ nur gleich sein, wenn sie konstant sind. Die linke Gleichung gibt $g(t)=\mathrm{e}^{-\mathrm{j} Et/\hbar}$, die rechte [(4.3)](#gl-4-3). Der Vergleich mit [(3.3)](die-wellenfunktion-und-ihre-deutung.html#gl-3-3) und $E=\hbar\omega$ zeigt: Die Konstante ist die Energie.
:::

⁠**So liest man das:** [(4.3)](#gl-4-3) ist eine __Eigenwertgleichung__. Meist verändert $\hat H$ eine Funktion in ihrer Form. Die __Eigenfunktionen__ $\psi$ multipliziert er nur mit einer Zahl, dem __Eigenwert__ $E$. Die Eigenfunktionen geben die möglichen __Zustände__, die Eigenwerte deren erlaubte Energien. Der Zeitfaktor dreht $\Psi$ nur als Zeiger und ändert keinen Betrag (Abb. [4](#abb-4)), also bleibt $|\Psi|^2=|\psi|^2$ zeitlich fest. Das gilt nur für eine einzelne Eigenfunktion: In einer Summe zweier Eigenfunktionen mit $E_1\neq E_2$ drehen sich die Zeiger verschieden schnell, und $|\Psi|^2$ schwingt mit $(E_2-E_1)/h$. **Grenzfall:** Eine Verschiebung $V\to V+V_1$ um eine Konstante ändert $\psi$ nicht, erhöht $E$ um $V_1$ und gibt $\Psi$ nur einen zusätzlichen Phasenfaktor. Messbar sind also nur Energieunterschiede.

:::abbildung gemb1/k1stationaer 4
Stationärer Zustand, Beispiel stehende Welle. Links: An festem Ort dreht sich der Zeiger $\Psi$ mit $\omega=E/\hbar$ im Uhrzeigersinn, seine Länge bleibt. Rechts oben: Der Realteil schwingt. Rechts unten: Das Betragsquadrat hängt nicht von der Zeit ab.
:::

**Beispiel.** Bei $E=1$ eV ist $\omega=E/\hbar=1{,}52\cdot10^{15}\,\mathrm{s^{-1}}$, der Zeiger dreht sich in 4,14 fs einmal. Keine Messung an $|\Psi|^2$ sieht diese Drehung.

**Was man damit berechnet.** Aus den Lösungen folgen die Energie der Elektronen und die Zahl der Zustände je Energie, die Aufenthaltswahrscheinlichkeit und damit die Elektronendichte, der Transport, also die Stromdichte, und der Drehimpuls mit seinem magnetischen Moment.

:::analogie
Eine gespannte Saite schwingt nur mit bestimmten Tönen, weil ihre Enden festliegen. Ebenso gibt es nur einzelne Eigenfunktionen mit einzelnen Energien, wenn $V$ den Aufenthaltsbereich einschränkt. Diese __Quantisierung__ ist der Kern der Quantenphysik. Man zählt die erlaubten Werte mit ganz- oder halbzahligen __Quantenzahlen__, je eine für jeden __Freiheitsgrad__ (unabhängige Bewegungsmöglichkeit). Das Bild endet bei der Bedeutung: Die Saite schwingt wirklich, $\Psi$ gibt Wahrscheinlichkeiten.
:::

:::frage In der Elektrotechnik heißt der Zeitfaktor doch $\mathrm{e}^{+\mathrm{j}\omega t}$. Warum steht hier ein Minus?
Das ist Vereinbarung. Zu $+\mathrm{j}\hbar\,\partial/\partial t$ in der Gleichung gehört $\mathrm{e}^{-\mathrm{j} Et/\hbar}$. Ersetzt man überall $\mathrm{j}$ durch $-\mathrm{j}$, ändert sich kein Betragsquadrat und keine Messgröße.
:::

:::aufgabe Aufgabe 4 ★ Eigenfunktion oder nicht?
<span class="anker" id="aufg-4"></span>

Sei $V=0$. Prüfe für $\mathrm{e}^{\mathrm{j} kx}$, $\sin(kx)$ und $x^2$, ob die Funktion Eigenfunktion von $\hat p$ und von $\hat H$ ist, und nenne gegebenenfalls den Eigenwert. Was bedeutet das Ergebnis für $\sin(kx)$?

:::loesung
$\mathrm{e}^{\mathrm{j} kx}$: $\hat p\,\mathrm{e}^{\mathrm{j} kx}=\hbar k\,\mathrm{e}^{\mathrm{j} kx}$ und $\hat H\,\mathrm{e}^{\mathrm{j} kx}=\frac{\hbar^2k^2}{2m}\mathrm{e}^{\mathrm{j} kx}$, Eigenfunktion von beiden. $\sin(kx)$: $\hat p\sin(kx)=(\hbar k/\mathrm{j})\cos(kx)$, keine Eigenfunktion, aber $\hat H\sin(kx)=\frac{\hbar^2k^2}{2m}\sin(kx)$, Eigenfunktion von $\hat H$. $x^2$: $\hat p\,x^2=(2\hbar/\mathrm{j})\,x$ und $\hat H\,x^2=-\hbar^2/m$, keine Eigenfunktion. Deutung: $\sin(kx)$ hat eine feste Energie, aber keinen festen Impuls. Wegen $\sin(kx)=(\mathrm{e}^{\mathrm{j} kx}-\mathrm{e}^{-\mathrm{j} kx})/(2\mathrm{j})$ enthält es $+\hbar k$ und $-\hbar k$ zu gleichen Teilen, eine nach rechts und eine nach links laufende Welle.
:::
:::
