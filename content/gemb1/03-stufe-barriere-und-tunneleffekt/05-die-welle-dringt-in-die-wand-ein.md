---
title: Stufe 3: Die Welle dringt in die Wand ein
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4130500
summary: Das Elektron hat zu wenig Energie für die Kante, klassisch endet es dort.
tags: evaneszente Welle, Abklingkonstanten, Eindringtiefe
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Das Elektron hat zu wenig Energie für die Kante, klassisch endet es dort. Hier zeigt sich, was die Welle tut und wie weit sie in das verbotene Gebiet reicht.
:::

**Die Idee.** Für $E<V_0$ dreht sich in [(0.1)](von-grund-auf-wellen-bei-konstantem-potential-rechnen-in-ev.html#gl-0-1) das Vorzeichen: Rechts gilt $\psi''=+\kappa^2\psi$ mit $\kappa^2=2m(V_0-E)/\hbar^2>0$. Die Krümmung zeigt jetzt von der Achse weg, die Kurve schwingt nicht mehr. Lösungen sind $\mathrm{e}^{-\kappa x}$ und $\mathrm{e}^{+\kappa x}$. Die zweite wächst ohne Grenze und scheidet aus. Rechnerisch wird $k_\mathrm{II}$ imaginär, und aus der Schwingung $\mathrm{e}^{\mathrm{j} k_\mathrm{II}x}$ wird der Abfall $\mathrm{e}^{-\kappa x}$.

Warum endet die Welle nicht an der Kante? Dafür müssten dort $\psi$ und $\psi'$ beide null sein, denn beide sind stetig. Dann wäre aber auch links $\psi\equiv0$: Die Differentialgleichung zweiter Ordnung hat mit diesen Anfangswerten nur die Nulllösung. Die Stetigkeit erzwingt also das Eindringen. Die abklingende Lösung heißt __evaneszente Welle__. Trotz des Namens läuft sie nicht.

:::satz Satz 3.1 (Eindringen in die Stufe für $E<V_0$)
<span class="anker" id="satz-3-1"></span>

Es ist $k_\mathrm{II}=\mathrm{j}\kappa$ mit der __Abklingkonstanten__ $\kappa=\sqrt{2m(V_0-E)}/\hbar$, und

<span class="anker" id="gl-3-1"></span>
$$\psi_\mathrm{II}(x)=C\,\mathrm{e}^{-\kappa x}\propto\exp\Bigl(-\sqrt{\frac{2m(V_0-E)}{\hbar^2}}\;x\Bigr)=\mathrm{e}^{-x/\delta},\qquad\delta=\frac1\kappa=\sqrt{\frac{\hbar^2}{2m(V_0-E)}}. \tag{3.1}$$

Mit $k_\mathrm{II}=\mathrm{j}\kappa$ in [(1.5)](zwei-gebiete-an-einer-kante-zusammensetzen.html#gl-1-5) und [(1.4)](zwei-gebiete-an-einer-kante-zusammensetzen.html#gl-1-4) folgt

<span class="anker" id="gl-3-2"></span>
$$\psi_\mathrm I(x)=\frac C2\Bigl[\Bigl(1+\mathrm{j}\frac{\kappa}{k_\mathrm I}\Bigr)\mathrm{e}^{\mathrm{j} k_\mathrm Ix}+\Bigl(1-\mathrm{j}\frac{\kappa}{k_\mathrm I}\Bigr)\mathrm{e}^{-\mathrm{j} k_\mathrm Ix}\Bigr],\qquad\frac BA=\frac{k_\mathrm I-\mathrm{j}\kappa}{k_\mathrm I+\mathrm{j}\kappa},\qquad R=1,\qquad T=0. \tag{3.2}$$
:::

⁠**So liest man das:** $\kappa$ in 1/nm misst, wie schnell die Welle abfällt. Die __Eindringtiefe__ $\delta$ ist die Strecke, auf der die Amplitude auf $1/\mathrm{e}$ fällt. $|\psi|^2$ fällt mit $\mathrm{e}^{-2x/\delta}$, doppelt so schnell. Mit [(0.3)](von-grund-auf-wellen-bei-konstantem-potential-rechnen-in-ev.html#gl-0-3) ist $\delta=0{,}195\,\mathrm{nm}/\sqrt{(V_0-E)/\mathrm{eV}}$. Sie wächst, wenn $V_0-E$ klein wird, und sinkt mit der Masse wie $1/\sqrt m$. **Gültigkeit:** $E<V_0$, und das Gebiet II reicht bis $x\to\infty$.

:::abbildung gemb1/k3unten 3
Wellenfunktion an der Kante mit $V_0=2$ eV für $A=1$ (grau: verbotenes Gebiet). Links die stehende Welle, rechts der exponentielle Abfall. Bei $x=\delta$ ist die Amplitude auf $1/\mathrm{e}=37$ % gefallen. Je näher $E$ an $V_0$ liegt, desto weiter reicht die Welle, und die Kurve läuft an der Kante flacher in die Wand.
:::

:::herleitung $R=1$ und $T=0$
In $B/A$ sind Zähler und Nenner zueinander konjugiert komplex, also gleich groß: $|B/A|=1$. Die Reflexion ist elastisch, $|v|$ ist für beide Wellen gleich, und aus [(2.3)](reflexion-trotz-genugender-energie.html#gl-2-3) wird $R=|B/A|^2=1$. Rechts gibt es keine laufende Welle und kein reelles $k$, also keine Geschwindigkeit und keinen Teilchenstrom: $T=0$.

$B/A$ ist also eine reine Phase, $B/A=\mathrm{e}^{-2\mathrm{j}\varphi}$ mit $\tan\varphi=\kappa/k_\mathrm I$. Damit wird $\psi_\mathrm I=2A\,\mathrm{e}^{-\mathrm{j}\varphi}\cos(k_\mathrm Ix+\varphi)$, eine stehende Welle. Aus [(1.4)](zwei-gebiete-an-einer-kante-zusammensetzen.html#gl-1-4) folgt

<span class="anker" id="gl-3-3"></span>
$$\Bigl|\frac CA\Bigr|^2=\frac{4k_\mathrm I^2}{k_\mathrm I^2+\kappa^2}=\frac{4E}{V_0}. \tag{3.3}$$
:::

**Beispiel.** Für $E=0{,}5$ eV und $V_0=2$ eV ist $\kappa=6{,}27\,\mathrm{nm^{-1}}$ und $\delta=0{,}159$ nm, weniger als ein Atomabstand. In 1 nm Tiefe ist die Amplitude auf $\mathrm{e}^{-6{,}27}=0{,}0019$ gefallen. Bei $E=1{,}5$ eV ist $\delta=0{,}276$ nm, bei $E=1{,}9$ eV schon 0,617 nm. Die Phase ist $\varphi=60^\circ$, und $|C/A|^2=1$. Für ein Proton (1837-fache Masse) schrumpft $\delta$ um den Faktor 42,9 auf 3,7 pm. **Grenzfälle:** Für $E\to V_0$ geht $\delta\to\infty$. Für $V_0\to\infty$ geht $\delta\to0$ und nach [(3.3)](#gl-3-3) $\psi(0)\to0$. Das ist die Randbedingung der Box aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html).

$R=1$ stimmt mit der klassischen Erwartung überein. Neu ist: Die Reflexion findet nicht genau an der Kante statt, sondern erstreckt sich ein Stück in die Wand hinein, und das Elektron hat dort eine klassisch unmögliche Aufenthaltswahrscheinlichkeit.

:::frage Im verbotenen Gebiet wäre die kinetische Energie negativ. Wie kann das Elektron dort sein?
Der Satz $E=E_\mathrm{kin}+V$ mit scharfen Werten gilt für Teilchen mit Bahn, nicht für die Welle. $\psi$ ist dort nicht null, also gibt es eine Aufenthaltswahrscheinlichkeit. Um das Elektron dort nachzuweisen, muss man es aber auf die Breite $\delta$ eingrenzen. Eine so stark gekrümmte Wellenfunktion hat rund $\hbar^2/(2m\delta^2)$ kinetische Energie, und das ist gerade $V_0-E$. Die Messung liefert also die fehlende Energie. Negative kinetische Energie wird nie gemessen.
:::

:::aufgabe Aufgabe 5 ★ Eindringtiefen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Berechne $\delta$ für $V_0-E=0{,}25$ eV, 1 eV und 4 eV. Welches Gesetz liest du ab?

</li>

<li>

In welcher Tiefe ist $|\psi|^2$ in diesen Fällen auf 1 % gefallen?

</li>

<li>

Vorhersage: Ein Proton trifft mit $V_0-E=1$ eV auf die Kante. Wie groß ist $\delta$, und was bedeutet das für schwere Teilchen?

</li>

</ol>

:::loesung
(a) $\delta=0{,}195\,\mathrm{nm}/\sqrt{(V_0-E)/\mathrm{eV}}$: 0,390 nm, 0,195 nm, 0,098 nm. Vierfache Energiedifferenz halbiert $\delta$. (b) $\mathrm{e}^{-2x/\delta}=0{,}01$ ergibt $x=\frac\delta2\ln100=2{,}30\,\delta$: 0,90 nm, 0,45 nm, 0,22 nm. (c) $\delta$ sinkt mit $1/\sqrt m$, also um den Faktor 42,9 auf 4,6 pm. Schwere Teilchen dringen kaum ein, und klassisches Verhalten wird genauer.
:::
:::

:::aufgabe Aufgabe 6 ★★ Von der Stufe zur harten Wand
<span class="anker" id="aufg-6"></span>

Ein Elektron hat $E=0{,}5$ eV. Berechne für $V_0=2$ eV, 20 eV und 200 eV die Größen $|C/A|^2$, $\delta$ und $\varphi$. Was geschieht für $V_0\to\infty$ mit $\psi(0)$ und mit der Phase? Vergleiche mit der stehenden Welle in der Box aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html).

:::loesung
Es ist $|C/A|^2=4E/V_0$, $\delta=0{,}195\,\mathrm{nm}/\sqrt{(V_0-E)/\mathrm{eV}}$ und $\tan\varphi=\kappa/k_\mathrm I=\sqrt{(V_0-E)/E}$. Das ergibt für 2 eV: 1; 0,159 nm; $60{,}0^\circ$. Für 20 eV: 0,1; 0,044 nm; $80{,}9^\circ$. Für 200 eV: 0,01; 0,014 nm; $87{,}1^\circ$. Für $V_0\to\infty$ gehen $|C/A|\to0$ und $\varphi\to90^\circ$. Dann wird $\psi_\mathrm I\propto\cos(k_\mathrm Ix+90^\circ)=-\sin(k_\mathrm Ix)$, ein Sinus mit Knoten an der Wand: die stehende Welle der Box.
:::
:::
