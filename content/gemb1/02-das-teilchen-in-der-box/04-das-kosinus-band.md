---
title: Stufe 2: Das Kosinus-Band
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Das Teilchen in der Box
order: 4120400
summary: Für konstantes Potential lässt sich die diskrete Gleichung von Hand lösen.
tags: Kosinus-Band, Brillouin-Zone, effektive Masse
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Für konstantes Potential lässt sich die diskrete Gleichung von Hand lösen. Diese Stufe zeigt, was das Gitter an der Parabel $E(k)$ ändert.
:::

**Die Idee.** Ist $V_\ell$ überall gleich, sieht jeder Gitterpunkt dieselbe Umgebung. Dann ist die Lösung dieselbe ebene Welle wie im freien Raum, nur an den Punkten abgetastet. Der Nachbar unterscheidet sich von $\psi_\ell$ nur um den Phasenfaktor $\mathrm{e}^{\pm\mathrm{j} ka}$. So fällt $\psi_\ell$ aus der Gleichung heraus, und es bleibt $E(k)$. Das Gitter setzt aber eine Grenze: Schneller, als von Punkt zu Punkt das Vorzeichen zu wechseln, kann eine Welle auf Punkten nicht schwingen.

:::satz Satz 2.1 (Kosinus-Band)
<span class="anker" id="satz-2-1"></span>

Für $V_\ell=V_0$ löst $\psi_\ell=A\,\mathrm{e}^{\mathrm{j} k\ell a}$ die Gleichung [(1.1)](die-schrodinger-gleichung-auf-einem-gitter.html#gl-1-1) mit

<span class="anker" id="gl-2-1"></span>
$$E(k)=2t_0\bigl(1-\cos(ka)\bigr)+V_0,\qquad-\frac\pi a\le k\le\frac\pi a. \tag{2.1}$$
:::

:::herleitung Einsetzen der ebenen Welle
Aus $\psi_\ell=A\,\mathrm{e}^{\mathrm{j} k\ell a}$ folgen $\psi_{\ell+1}=\psi_\ell\,\mathrm{e}^{\mathrm{j} ka}$ und $\psi_{\ell-1}=\psi_\ell\,\mathrm{e}^{-\mathrm{j} ka}$. Einsetzen und Division durch $\psi_\ell$ ergibt

$$-t_0\,\mathrm{e}^{\mathrm{j} ka}+2t_0-t_0\,\mathrm{e}^{-\mathrm{j} ka}+V_0=2t_0-2t_0\,\frac{\mathrm{e}^{\mathrm{j} ka}+\mathrm{e}^{-\mathrm{j} ka}}{2}+V_0=E.$$

Der Bruch ist $\cos(ka)$.
:::

:::abbildung gemb1/k2kosinus 2
Rechenmodell $a=0{,}2$ nm, $V_0=0$. Links: Kosinus-Band (blau) und Parabel des freien Elektrons (gestrichelt). Rechts: Geschwindigkeit $v(k)$ und die Gerade $\hbar k/m$ des freien Elektrons. Getönt ist die erste Brillouin-Zone, außerhalb wiederholt sich die Kurve.
:::

⁠**So liest man das:** Ein Band ist ein zusammenhängender Bereich erlaubter Energien. Das __Kosinus-Band__ reicht von $V_0$ bis $V_0+4t_0$, im Rechenmodell 3,81 eV breit (Abb. [2](#abb-2)). Stärkere Kopplung gibt ein breiteres Band. Die Grenze für $k$ hat diesen Grund: $k$ und $k+2\pi/a$ liefern an allen Punkten dieselben Zahlen, denn $\mathrm{e}^{\mathrm{j}(2\pi/a)\ell a}=\mathrm{e}^{\mathrm{j}2\pi\ell}=1$. Beide sind also dieselbe Welle. Der eindeutige Bereich $-\pi/a\le k\le\pi/a$ heißt erste __Brillouin-Zone__.

⁠**Grenzfälle:** Für $|ka|\ll1$ ist $\cos(ka)\approx1-(ka)^2/2$, also $E(k)\approx t_0a^2k^2+V_0=\hbar^2k^2/(2m)+V_0$. Die freie Parabel kehrt zurück, weil $a^2$ sich gegen $t_0$ kürzt: Für lange Wellen verschwindet das Gitter. Am Rand $k=\pi/a$ ist $\psi_\ell=A(-1)^\ell$. Jeder Punkt hat das Gegenvorzeichen seiner Nachbarn, die Krümmung ist maximal, und $E=V_0+4t_0$.

**Geschwindigkeit.** Aus $v=\frac1\hbar\,\partial E/\partial k$ folgt

<span class="anker" id="gl-2-2"></span>
$$v(k)=\frac{2t_0a}{\hbar}\sin(ka). \tag{2.2}$$

Anders als beim freien Elektron wächst $v$ nicht unbegrenzt. Das Maximum $v_\text{max}=2t_0a/\hbar=5{,}8\cdot10^5$ m/s liegt bei $k=\pi/(2a)$. Am Rand ist $v=0$: $(-1)^\ell$ ist ein stehendes Muster, die Welle läuft nicht mehr.

**Masse aus der Krümmung.** Nach [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html) ist die Masse der Kehrwert der Krümmung von $E(k)$. Für jede andere Kurve als die freie Parabel heißt diese Größe __effektive Masse__: die Masse, mit der ein Elektron im Material auf eine Kraft reagiert.

<span class="anker" id="gl-2-3"></span>
$$m^*=\Bigl(\frac1{\hbar^2}\,\frac{\partial^2E(k)}{\partial k^2}\Bigr)^{-1}. \tag{2.3}$$

Am Boden des Bands [(2.1)](#gl-2-1) ergibt das $m^*=\hbar^2/(2t_0a^2)$: Starke Kopplung krümmt die Kurve stärker, und das Elektron wirkt leichter. Für den Kristall heißt das: Masse ist dort keine feste Zahl, sondern eine Eigenschaft der Kurve $E(k)$. Hängt die Krümmung von der Richtung ab, hängt auch $m^*$ von der Richtung ab. Für $|k|>\pi/(2a)$ wird $m^*$ sogar negativ: Dort sinkt $v$, wenn $k$ wächst. Im Folgenden steht $m$ für die Masse des jeweiligen Elektrons, also $m_0$ im Vakuum und $m^*$ im Kristall.

**Beispiel.** Im Rechenmodell liegt der Zonenrand bei $\pi/a=15{,}7\,\mathrm{nm^{-1}}$. Die Abweichung von der Parabel bleibt unter 1 %, solange $(ka)^2/12<0{,}01$, also $ka<0{,}35$. Das entspricht $E<114$ meV. Deshalb reicht die Parabel für Elektronen nahe dem Bandboden.

:::frage Warum gibt es ein größtes $k$? Eine Welle kann doch beliebig kurz sein.
Im freien Raum stimmt das. Auf dem Gitter existiert die Welle nur an den Punkten. Eine Welle mit $\lambda<2a$ trifft an den Punkten dieselben Werte wie eine längere Welle innerhalb der Zone. Das ist dieselbe Mehrdeutigkeit wie beim Abtasten eines Signals mit zu wenigen Werten je Periode.
:::

:::aufgabe Aufgabe 2 ★★ Ein Band ausmessen
<span class="anker" id="aufg-2"></span>

Ein Gitter hat $a=0{,}3$ nm, $m=m_0$ und $V_0=0$.

<ol class="al">

<li>

Berechne $t_0$, die Bandbreite und den Zonenrand.

</li>

<li>

Berechne $E$ und $v$ bei $k=\pi/(2a)$. Vergleiche mit Parabel und $\hbar k/m$. Woher kommt der Unterschied?

</li>

<li>

Vorhersage: Was geschieht mit Bandbreite, Zonenrand und Masse am Bandboden, wenn $a$ sich verdoppelt und $t_0$ gleich bleibt?

</li>

</ol>

:::loesung
(a) $t_0=0{,}0381\,\mathrm{eV\,nm^2}/(0{,}3\,\mathrm{nm})^2=0{,}423$ eV, Bandbreite $4t_0=1{,}69$ eV, Zonenrand $\pi/a=10{,}5\,\mathrm{nm^{-1}}$. (b) Bei $k=\pi/(2a)=5{,}24\,\mathrm{nm^{-1}}$ ist $E=2t_0=0{,}847$ eV und $v=2t_0a/\hbar=3{,}86\cdot10^5$ m/s, das Maximum. Die Parabel gäbe 1,04 eV, also das 1,23-Fache, und $\hbar k/m=6{,}06\cdot10^5$ m/s. Das Gitter begrenzt die Krümmung, die Kurve biegt ab. (c) Die Bandbreite $4t_0$ bleibt, der Zonenrand halbiert sich, die Masse $\hbar^2/(2t_0a^2)$ sinkt auf ein Viertel. Gleiche Energiebreite auf halbem $k$-Bereich heißt stärkere Krümmung.
:::
:::
