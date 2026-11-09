---
title: Stufe 8: Polardarstellung, Drehen und Strecken
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1271000
summary: Diese Stufe löst die Ankündigung aus Teil 2 ein: Jede komplexe Zahl ist Länge mal Richtung, und Multiplizieren heißt Drehen und Strecken.
tags: Einheitskreislinie, Argument, orientierte Winkel, Definitheit, Zeiger
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Diese Stufe löst die Ankündigung aus [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html) ein: Jede komplexe Zahl ist Länge mal Richtung, und Multiplizieren heißt Drehen und Strecken.
:::

**Die Idee.** Jedes $z\ne0$ liegt auf genau einem Strahl vom Nullpunkt und hat einen Abstand $|z|$ von ihm. Teilt man durch $|z|$, landet man auf dem Einheitskreis, also bei einem $\mathrm{e}^{\mathrm{i}\varphi}$. Multipliziert man zwei solche Zahlen, addieren sich die Exponenten wegen der Funktionalgleichung, und die Längen multiplizieren sich. Die Multiplikation mit $w$ dreht also die ganze Ebene um den Winkel von $w$ und streckt sie um $|w|$. Das Dreieck $(0,1,z_2)$ in Abb. [8](#abb-8) geht in das ähnliche Dreieck $(0,z_1,z_1z_2)$ über.

:::abbildung hm1/k7dreh 8
Links dreht $z_1$ das Dreieck $(0,1,z_2)$ um $\varphi_1$ und streckt es um $\sqrt{10}$. Rechts der Kehrwert: Der Betrag wird zu $1/|z_2|$, das ist $z_2/|z_2|^2$ auf demselben Strahl. Das Spiegeln an der reellen Achse ergibt $1/z_2=0{,}2-0{,}4\mathrm{i}$.
:::

:::satz Satz 8.1 (Einheitskreis und Polardarstellung)
<span class="anker" id="satz-8-1"></span>

<ol class="rm">

<li>

Zu jedem $z$ mit $|z|=1$ gibt es genau ein $\varphi\in[0,2\pi)$ mit $z=\mathrm{e}^{\mathrm{i}\varphi}$. Also ist $\{\mathrm{e}^{\mathrm{i}\varphi}:\varphi\in\mathbb{R}\}=\{z\in\mathbb{C}:|z|=1\}=:S^1$, die __Einheitskreislinie__.

</li>

<li>

Jedes $z=x+\mathrm{i}y\ne0$ besitzt die Darstellung

<span class="anker" id="gl-8-1"></span>
$$z=|z|\,\mathrm{e}^{\mathrm{i}\varphi}=|z|\,(\cos\varphi+\mathrm{i}\sin\varphi) \tag{8.1}$$

mit eindeutigem $\varphi\in[0,2\pi)$. Es heißt __Argument__ von $z$, geschrieben $\varphi=\arg(z)$, und ist der __orientierte Winkel__ von $(1,0)$ nach $(x,y)$, gegen den Uhrzeigersinn gezählt.

</li>

</ol>
:::

⁠**So liest man das:** $|z|$ ist die Länge, $\varphi$ die Richtung im Bogenmaß ($360^\circ$ sind $2\pi$). Aus [(8.1)](#gl-8-1) folgt

<span class="anker" id="gl-8-2"></span>
$$\cos\varphi=\frac x{|z|},\qquad\sin\varphi=\frac y{|z|}. \tag{8.2}$$

Das sind Ankathete und Gegenkathete durch Hypotenuse: Die Reihen sind die Funktionen aus der Schule. **Gültigkeit:** $z=0$ hat keinen Winkel. Manche Bücher wählen $\varphi\in(-\pi,\pi]$.

:::beweis Auf den Einheitskreis zurückführen
(i), Idee: Sei $z=x+\mathrm{i}y$ mit $x^2+y^2=1$. Der Cosinus läuft auf $[0,\pi]$ stetig und monoton von 1 nach $-1$ und trifft $x$ genau einmal in einem $\varphi_0$. Dann ist $\sin\varphi_0=\pm y$, und die Wahl von $\varphi_0$ oder $2\pi-\varphi_0$ passt das Vorzeichen an.

(ii): $w:=z/|z|$ hat den Betrag 1, also ist $w=\mathrm{e}^{\mathrm{i}\varphi}$ mit eindeutigem $\varphi$, und $z=|z|\,w$. Die zweite Form ist [(6.1)](die-eulersche-formel.html#gl-6-1).
:::

::::beispiel Umrechnen
Aus [(8.2)](#gl-8-2) folgt $\tan\varphi=y/x$ für $x\ne0$. Die Taste $\arctan$ liefert Werte in $(-\frac\pi2,\frac\pi2)$, den Quadranten bestimmt man selbst. Für $z_1=3+\mathrm{i}$ ist $|z_1|=\sqrt{10}$ und $\varphi_1=\arctan\frac13\approx0{,}3218$ ($18{,}43^\circ$). Für $z_2=1+2\mathrm{i}$ ist $\varphi_2=\arctan2\approx1{,}1071$ ($63{,}43^\circ$). Für $-1-\mathrm{i}$ gibt $\arctan1=\frac\pi4$ den falschen Quadranten, richtig ist $\varphi=\frac\pi4+\pi=\frac54\pi$ und $|z|=\sqrt2$.
::::

:::satz Satz 8.2 (Multiplikation in Polardarstellung)
<span class="anker" id="satz-8-2"></span>

Für $z=|z|\,\mathrm{e}^{\mathrm{i}\varphi}$ und $w=|w|\,\mathrm{e}^{\mathrm{i}\psi}$ gilt

<span class="anker" id="gl-8-3"></span>
$$z\cdot w=|z|\,|w|\,\mathrm{e}^{\mathrm{i}(\varphi+\psi)},\qquad\overline{z\cdot w}=|z|\,|w|\,\mathrm{e}^{-\mathrm{i}(\varphi+\psi)},\qquad\frac1z=\frac1{|z|}\,\mathrm{e}^{-\mathrm{i}\varphi}. \tag{8.3}$$

Außerdem ist $\arg(zw)=\varphi+\psi$, falls $\varphi+\psi<2\pi$, sonst $\arg(zw)=\varphi+\psi-2\pi$.
:::

⁠**So liest man das:** Beträge multiplizieren, Winkel addieren. $w=\mathrm{i}=\mathrm{e}^{\mathrm{i}\pi/2}$ ist die Vierteldrehung aus [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html), und $\mathrm{i}^2=-1$ heißt: zweimal $90^\circ$ sind $180^\circ$. Es folgt $z^n=|z|^n\mathrm{e}^{\mathrm{i}n\varphi}$. Konjugieren kehrt den Winkel um. Der Beweis ist [(8.1)](#gl-8-1) und die Funktionalgleichung, bei $1/z$ die Probe $z\cdot\frac1{|z|}\mathrm{e}^{-\mathrm{i}\varphi}=1$.

::::beispiel
$z_1z_2=\sqrt{10}\sqrt5\,\mathrm{e}^{\mathrm{i}(0{,}3218+1{,}1071)}=\sqrt{50}\,\mathrm{e}^{1{,}4289\,\mathrm{i}}$, und $\sqrt{50}\cos1{,}4289=1$, $\sqrt{50}\sin1{,}4289=7$. Das ist $1+7\mathrm{i}$ aus [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Potenzen werden kurz: $(1+\mathrm{i})^8=(\sqrt2)^8\,\mathrm{e}^{8\mathrm{i}\pi/4}=16\,\mathrm{e}^{2\pi\mathrm{i}}=16$.
::::

:::satz Satz 8.3 (Rechenregeln in $\mathbb{C}$, Zusammenfassung)
<span class="anker" id="satz-8-3"></span>

Für alle $z,w\in\mathbb{C}$ gilt: (a) $\overline{z+w}=\overline z+\overline w$, (b) $\overline{z\cdot w}=\overline z\cdot\overline w$, (c) $|z|\ge0$ und ($|z|=0\Leftrightarrow z=0$), die __Definitheit__ des Betrags, (d) $|z+w|\le|z|+|w|$ (Dreiecksungleichung), (e) $|z\cdot w|=|z|\cdot|w|$, (f) $z\cdot\overline z=|z|^2$, (g) $\max\{|\operatorname{Re} z|,|\operatorname{Im} z|\}\le|z|\le|\operatorname{Re} z|+|\operatorname{Im} z|$, (h) $\frac1z=\overline z\cdot\frac1{|z|^2}$ für $z\ne0$.
:::

⁠**So liest man das:** Die Beweise stehen in [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Neu ist die Polarform: (b), (e), (f), (h) folgen aus [(8.3)](#gl-8-3), (g) aus $\operatorname{Re} z=|z|\cos\varphi$ und $|\cos\varphi|\le1$. Regel (h) zerlegt den Kehrwert in Abb. [8](#abb-8): $z/|z|^2$ spiegelt $z$ am Einheitskreis (der Betrag wird zum Kehrwert), die Konjugation spiegelt an der reellen Achse.

**Wo es gebraucht wird.** Eine Wechselspannung $u(t)=\hat U\cos(\omega t+\varphi_0)$ ist der Realteil von $\hat U\mathrm{e}^{\mathrm{i}\varphi_0}\cdot\mathrm{e}^{\mathrm{i}\omega t}$: Ein __Zeiger__ der Länge $\hat U$ läuft mit der Kreisfrequenz $\omega$ um den Nullpunkt, und die Spannung ist sein Schatten auf der reellen Achse. Der feste Faktor $\hat U\mathrm{e}^{\mathrm{i}\varphi_0}$ enthält Amplitude und Phase in einer Zahl. Die Elektrotechnik schreibt dafür $\mathrm{j}$ statt $\mathrm{i}$.

:::frage Gibt es für die Summe $z+w$ auch eine kurze Polarformel?
Nein. Addieren ist in der Normalform kurz, Multiplizieren in der Polarform. Deshalb wechselt man je nach Rechenart die Darstellung.
:::

:::aufgabe Aufgabe 8 ★★ Polarform üben
<span class="anker" id="aufg-8"></span>

(a) Bringe $-2+2\mathrm{i}$, $-\sqrt3-\mathrm{i}$ und $3\mathrm{i}$ auf Polarform. (b) Berechne $(1+\mathrm{i})^{10}$ und $(1+\sqrt3\,\mathrm{i})^6$. (c) Sei $z=2\,\mathrm{e}^{\mathrm{i}\pi/3}$. Sage Betrag und Winkel von $\mathrm{i}z$, $\overline z$ und $1/z$ vorher und rechne alle drei in die Normalform um.

:::loesung
(a) $-2+2\mathrm{i}=2\sqrt2\,\mathrm{e}^{3\mathrm{i}\pi/4}$. $-\sqrt3-\mathrm{i}=2\,\mathrm{e}^{7\mathrm{i}\pi/6}$ (dritter Quadrant, $\arctan\frac1{\sqrt3}=\frac\pi6$). $3\mathrm{i}=3\,\mathrm{e}^{\mathrm{i}\pi/2}$. (b) $(1+\mathrm{i})^{10}=(\sqrt2)^{10}\mathrm{e}^{10\mathrm{i}\pi/4}=32\,\mathrm{e}^{\mathrm{i}\pi/2}=32\mathrm{i}$, denn $\frac{10\pi}4=2\pi+\frac\pi2$. $(1+\sqrt3\,\mathrm{i})^6=(2\,\mathrm{e}^{\mathrm{i}\pi/3})^6=64\,\mathrm{e}^{2\pi\mathrm{i}}=64$. (c) $\mathrm{i}z$: Betrag 2, Winkel $\frac\pi3+\frac\pi2=\frac56\pi$, also $\mathrm{i}z=-\sqrt3+\mathrm{i}$. $\overline z$: Betrag 2, Winkel $-\frac\pi3$, also $\overline z=1-\sqrt3\,\mathrm{i}$. $1/z$: Betrag $\frac12$, Winkel $-\frac\pi3$, also $\frac14-\frac{\sqrt3}4\mathrm{i}$. Dabei ist $z=1+\sqrt3\,\mathrm{i}$.
:::
:::

:::aufgabe Aufgabe 9 ★★★ Zwei Schwingungen addieren
<span class="anker" id="aufg-9"></span>

(a) Zeige für reelle $a,b$: $a\cos t+b\sin t=\operatorname{Re}\bigl((a-\mathrm{i}b)\,\mathrm{e}^{\mathrm{i}t}\bigr)$. (b) Schreibe $3\cos t+4\sin t$ als $C\cos(t+\varphi_0)$ mit $C>0$. (c) Bei welchem $t\in[0,2\pi)$ ist das Maximum? Prüfe das Ergebnis bei $t=0$.

:::loesung
(a) $(a-\mathrm{i}b)(\cos t+\mathrm{i}\sin t)=(a\cos t+b\sin t)+\mathrm{i}(a\sin t-b\cos t)$. Der Realteil ist die Behauptung. (b) $3-4\mathrm{i}$ hat den Betrag 5 und den Winkel $\varphi_0=-\arctan\frac43=-0{,}9273$ ($-53{,}13^\circ$). Also ist $3\cos t+4\sin t=\operatorname{Re}(5\,\mathrm{e}^{\mathrm{i}\varphi_0}\mathrm{e}^{\mathrm{i}t})=5\cos(t+\varphi_0)$. (c) Das Maximum 5 liegt bei $t+\varphi_0=0$, also $t=0{,}9273$. Probe bei $t=0$: $5\cos(-0{,}9273)=3$.
:::
:::
