---
title: Stufe 6: Das Wellenpaket
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
order: 4110800
summary: Eine ebene Welle ist überall zugleich, ein Elektron hat aber einen Aufenthaltsbereich.
tags: Wellenpaket, kanonisch konjugierte, Phasengeschwindigkeit, Gruppengeschwindigkeit
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Eine ebene Welle ist überall zugleich, ein Elektron hat aber einen Aufenthaltsbereich. Diese Stufe baut ein Paket aus ebenen Wellen und zeigt, was das kostet und wie schnell es läuft.
:::

**Die Idee.** Die Schrödinger-Gleichung ist linear, eine Summe von Lösungen ist wieder eine Lösung. Überlagert man viele ebene Wellen mit leicht verschiedenen Wellenzahlen, stimmen ihre Phasen nur an einer Stelle überein. Dort verstärken sie sich, überall sonst löschen sie sich aus. So entsteht ein __Wellenpaket__ (Abb. [6](#abb-6)). Je enger das Paket sein soll, desto mehr Wellenzahlen braucht es: Der Ort wird schärfer, der Impuls unschärfer. Die Hülle wandert mit einer anderen Geschwindigkeit als die Wellenberge in ihr.

:::satz Satz 6.1 (Gaußsches Wellenpaket)
<span class="anker" id="satz-6-1"></span>

Mit der Gewichtsfunktion $c(k)=c_0\,\mathrm{e}^{-(k-k_0)^2/(2/w)^2}$ um die Wellenzahl $k_0$ ist

<span class="anker" id="gl-6-1"></span>
$$\psi(x)=\int_{-\infty}^{\infty}c(k)\,\mathrm{e}^{\mathrm{j} kx}\,\mathrm{d} k=\Bigl(\frac2{\pi w^2}\Bigr)^{1/4}\mathrm{e}^{-x^2/w^2}\,\mathrm{e}^{\mathrm{j} k_0x}. \tag{6.1}$$
:::

⁠**So liest man das:** $\mathrm{e}^{\mathrm{j} k_0x}$ ist die Trägerwelle, $\mathrm{e}^{-x^2/w^2}$ die Hülle mit dem Breitenmaß $w$. Die Konstante $c_0$ ist so gewählt, dass $\psi$ normiert ist. Das Paket ist ein amplitudenmoduliertes Signal im Ort. Als Breiten nimmt man die Standardabweichungen (mittlere Abweichungen vom Mittelwert) von $|\psi|^2$ und $|c|^2$: $\Delta x=w/2$ und $\Delta k=1/w$.

:::herleitung Das Gaußintegral
Mit $q=k-k_0$ ist $\psi(x)=c_0\,\mathrm{e}^{\mathrm{j} k_0x}\int\mathrm{e}^{-w^2q^2/4+\mathrm{j} qx}\,\mathrm{d} q$. Quadratisch ergänzen gibt den Exponenten $-\frac{w^2}4\bigl(q-2\mathrm{j} x/w^2\bigr)^2-x^2/w^2$, das Gaußintegral den Faktor $2\sqrt\pi/w$. Aus $\int|\psi|^2\,\mathrm{d} x=1$ folgt der Vorfaktor in [(6.1)](#gl-6-1).
:::

:::abbildung gemb1/k1paket 6
Oben und Mitte: Realteil von $\psi$ mit Hülle (rot) und zugehörige Gewichtsfunktion für $k_0=5{,}12$/nm. Das schmalere Paket braucht mehr Wellenzahlen. Unten: Paket mit $w=2$ nm bei $t=0$ und $t=6$ fs, exakt gerechnet. Die Hülle läuft mit $v_\mathrm g$ um 3,6 nm, ein Wellenberg (roter Punkt) mit $v_\mathrm{ph}$ um 1,8 nm.
:::

:::satz Satz 6.2 (Heisenbergsche Unschärferelation)
<span class="anker" id="satz-6-2"></span>

Ort und Impuls eines Teilchens lassen sich nicht zugleich beliebig genau festlegen. Für die Standardabweichungen gilt

<span class="anker" id="gl-6-2"></span>
$$\Delta x\,\Delta p\ge\frac\hbar2. \tag{6.2}$$
:::

⁠**So liest man das:** Mit $p=\hbar k$ gibt das Gaußpaket genau $\Delta x\,\Delta p=\hbar/2$, es ist das schärfste mögliche Paket. Für Überschläge rechnet man mit $\Delta x\,\Delta p\approx\hbar$. Dasselbe gilt für andere __kanonisch konjugierte__ Größen, also Paare, die wie $x$ und $k$ über ein Integral der Form [(6.1)](#gl-6-1) zusammenhängen, etwa Energie und Zeit mit $\Delta E\,\Delta t\approx\hbar$.

**Grenzfälle.** Für $w\to0$ geht $c(k)\to c_0$: Alle Wellenzahlen tragen gleich bei, $\psi(0)\to\infty$ und $\psi(x\neq0)\to0$. Das ist die Deltafunktion $\delta(x)$, die außer bei $x=0$ überall null ist und die Fläche 1 hat: $\int\mathrm{e}^{\mathrm{j} kx}\,\mathrm{d} k=2\pi\,\delta(x)$. Für $w\to\infty$ wird die Hülle flach, und bis auf den Vorfaktor bleibt die ebene Welle $\mathrm{e}^{\mathrm{j} k_0x}$.

:::satz Satz 6.3 (Phasen- und Gruppengeschwindigkeit)
<span class="anker" id="satz-6-3"></span>

Ein Wellenberg läuft mit der __Phasengeschwindigkeit__ $v_\mathrm{ph}$, die Hülle mit der __Gruppengeschwindigkeit__ $v_\mathrm g$:

<span class="anker" id="gl-6-3"></span>
$$v_\mathrm{ph}=\frac\omega k=\frac1\hbar\frac{E(k)}k,\qquad v_\mathrm g=\frac{\partial\omega}{\partial k}=\frac1\hbar\frac{\partial E(k)}{\partial k}. \tag{6.3}$$

Für die Parabel mit $V_0=0$ ist $v_\mathrm g=\hbar k/m=p/m=v$ die klassische Teilchengeschwindigkeit und $v_\mathrm{ph}=\hbar k/(2m)=v/2$.
:::

:::herleitung Schwebung
Zwei Wellen mit $k_0\pm\Delta k$ und $\omega_0\pm\Delta\omega$ ergeben $2\cos(\Delta k\,x-\Delta\omega\,t)\cos(k_0x-\omega_0t)$. Der zweite Faktor ist der Träger, er läuft mit $\omega_0/k_0$. Der erste ist die Hülle, sie läuft mit $\Delta\omega/\Delta k$, für kleine $\Delta k$ also mit $\partial\omega/\partial k$. Einsetzen von $\omega=E/\hbar$ gibt [(6.3)](#gl-6-3).
:::

⁠**So liest man das:** Das Maximum des Pakets ist der markante Punkt, mit dem sich das Elektron bewegt, deshalb ist $v_\mathrm g$ seine Geschwindigkeit. $v_\mathrm{ph}$ hat keine messbare Bedeutung: Sie ändert sich mit dem Energienullpunkt, $v_\mathrm g$ nicht, denn die Ableitung sieht die Konstante $V_0$ nicht. Für $V_0=0$ laufen die Wellenberge langsamer als die Hülle, sie tauchen vorn auf und verschwinden hinten.

::::beispiel
Ein Probe-Elektron mit $v_\mathrm g=5{,}93\cdot10^{5}$ m/s sitze im Paket mit $w=2$ nm. Dann ist $\Delta x=1$ nm, $\Delta k=5\cdot10^{8}\,\mathrm{m^{-1}}$, rund 10 % von $k_0$. Die Wellenzahlen des Pakets haben verschiedene Gruppengeschwindigkeiten, sie streuen um $\Delta v=\hbar\Delta k/m_0=5{,}8\cdot10^{4}$ m/s. Deshalb läuft das Paket auseinander: Nach $t=\Delta x/\Delta v=1{,}7\cdot10^{-14}$ s ist die Streuung so groß wie die Breite selbst.
::::

:::frage Ist die Unschärfe ein Messfehler, den bessere Geräte beseitigen?
Nein. Ein Zustand mit kleinem $\Delta x$ enthält viele Wellenzahlen, er hat gar keinen scharfen Impuls. Das gilt für jede Welle: Auch ein kurzer Spannungspuls hat ein breites Spektrum.
:::

:::aufgabe Aufgabe 7 ★★ Ein Paket vermessen
<span class="anker" id="aufg-7"></span>

Das Probe-Elektron stecke in einem Gaußpaket mit $w=6$ nm und $V_0=0$.

<ol class="al">

<li>

Berechne $\Delta x$, $\Delta k$ und $\Delta p$. Wie viele Wellenlängen passen in $2\Delta x$?

</li>

<li>

Berechne $\Delta v$, die Zeit $t=\Delta x/\Delta v$ und den Flugweg in dieser Zeit.

</li>

<li>

Grenzfall: Wie ändert sich $t$, wenn $w$ zehnmal größer ist?

</li>

<li>

Was ändert sich an $v_\mathrm g$ und $v_\mathrm{ph}$, wenn das Elektron auf $V_0=2$ eV sitzt? Rechne beide aus.

</li>

</ol>

:::loesung
(a) $\Delta x=3$ nm, $\Delta k=1/w=1{,}67\cdot10^{8}\,\mathrm{m^{-1}}$, $\Delta p=\hbar\Delta k=1{,}76\cdot10^{-26}$ kg m/s. In $2\Delta x=6$ nm passen 4,9 Wellenlängen von 1,23 nm. (b) $\Delta v=\Delta p/m_0=1{,}93\cdot10^{4}$ m/s, $t=1{,}55\cdot10^{-13}$ s, Flugweg $v_\mathrm g\,t=92$ nm. (c) $\Delta x$ wächst und $\Delta v$ sinkt je zehnfach, $t$ wird hundertmal größer: $1{,}55\cdot10^{-11}$ s. (d) $v_\mathrm g$ bleibt $5{,}93\cdot10^{5}$ m/s, denn die Ableitung sieht $V_0$ nicht. $v_\mathrm{ph}=E/(\hbar k)$ steigt von $3{,}0\cdot10^{5}$ m/s auf $8{,}9\cdot10^{5}$ m/s, obwohl sich physikalisch nichts geändert hat.
:::
:::
