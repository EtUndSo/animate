---
title: Stufe 1: Der Kern als Kasten ohne Wände
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Atome und Orbitale
order: 4140300
summary: In der Box saß das Elektron zwischen vorgegebenen Wänden.
tags: Wasserstoffatom, Zentralpotential, Radialanteil, Winkelanteil, reduzierte Masse
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
In der Box saß das Elektron zwischen vorgegebenen Wänden. Im Atom gibt es keine Wände, nur die Anziehung des Kerns. Diese Stufe stellt die Schrödinger-Gleichung für diese Anziehung auf und zeigt, warum auch hier nur bestimmte Energien erlaubt sind.
:::

**Die Idee.** Das kleinste Atom ist das __Wasserstoffatom__: ein Proton, ein Elektron, also keine Abstoßung zwischen Elektronen. Das Proton zieht das Elektron an, und die potentielle Energie sinkt zum Kern hin immer tiefer. Im Schnitt sieht das wie ein Trichter aus (Abb. [1](#abb-1)). Hat das Elektron eine Energie $E<0$, endet das erlaubte Gebiet am Rand des Trichters: Weiter außen ist $V>E$, das Gebiet ist klassisch verboten, und die Welle klingt dort ab ([Teil 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html)). Die Welle ist also eingesperrt und interferiert mit sich selbst. Wie in der Box bleiben nur Muster übrig, die zu sich selbst passen. Diese gebundenen Zustände haben diskrete Energien. Für $E>0$ gibt es keinen Rand mehr, das Elektron ist frei, und jede Energie ist möglich.

:::abbildung gemb1/k4coulomb 1
Potentielle Energie $V$ eines Elektrons im Schnitt durch das Proton. Die roten Linien sind die drei tiefsten erlaubten Energien. Sie enden dort, wo $V=E$ gilt. Jenseits dieser Punkte ist das Gebiet für die jeweilige Energie klassisch verboten. Oberhalb von $E=0$ liegen die freien Zustände.
:::

:::definition Definition 1.1 (Coulomb-Potential)
<span class="anker" id="satz-1-1"></span>

Die potentielle Energie eines Elektrons im Abstand $r$ vom Wasserstoffkern ist

<span class="anker" id="gl-1-1"></span>
$$V(r)=-\frac{e^2}{4\pi\varepsilon_0\,r}. \tag{1.1}$$

Ein Potential, das nur von $r$ abhängt, heißt __Zentralpotential__.
:::

⁠**So liest man das:** $V$ ist wie in [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html) bis 3 eine Energie in J oder eV, nicht das elektrische Potential in Volt. Sie ist das Produkt aus dem Potential des Protons und der Elektronenladung $-e$. $r$ ist der Abstand in m, typisch 0,1 nm. Der Nullpunkt liegt bei $r\to\infty$. Das Minuszeichen sagt: Beim Annähern sinkt die Energie, das ist Anziehung. Bei $r=0{,}1$ nm ist $V=-1{,}44\,\mathrm{eV\,nm}/0{,}1\,\mathrm{nm}=-14{,}4$ eV.

:::satz Satz 1.2 (Schrödinger-Gleichung im Zentralpotential)
<span class="anker" id="satz-1-2"></span>

In Kugelkoordinaten lautet die zeitunabhängige Schrödinger-Gleichung für $\psi(r,\theta,\varphi)$

<span class="anker" id="gl-1-2"></span>
$$-\frac{\hbar^2}{2\mu}\,\frac{1}{r^2\sin\theta}\Bigl[\sin\theta\,\frac{\partial}{\partial r}\Bigl(r^2\frac{\partial\psi}{\partial r}\Bigr)+\frac{\partial}{\partial\theta}\Bigl(\sin\theta\,\frac{\partial\psi}{\partial\theta}\Bigr)+\frac{1}{\sin\theta}\frac{\partial^2\psi}{\partial\varphi^2}\Bigr]+V(r)\,\psi=E\,\psi. \tag{1.2}$$

Der Separationsansatz $\psi(r,\theta,\varphi)=R(r)\,Y(\theta,\varphi)$ trennt sie in eine Gleichung für den __Radialanteil__ $R$ und eine für den __Winkelanteil__ $Y$.
:::

⁠**So liest man das:** Die Klammer mit ihrem Vorfaktor ist $\partial_x^2+\partial_y^2+\partial_z^2$, umgerechnet mit der Kettenregel auf [(0.1)](von-grund-auf-atom-kugelkoordinaten-und-drehimpuls.html#gl-0-1). Der erste Summand misst die Krümmung der Welle entlang $r$, die beiden anderen ihre Krümmung auf der Kugelfläche. $\mu=m_0m_\mathrm p/(m_0+m_\mathrm p)$ ist die __reduzierte Masse__, denn Kern und Elektron bewegen sich um ihren gemeinsamen Schwerpunkt. Mit der Protonenmasse $m_\mathrm p$ ist $\mu=0{,}99946\,m_0$. Die Abweichung von 0,05 % spielt für die Zahlen dieses Kapitels keine Rolle, deshalb steht ab hier $m_0$. **Gültigkeit:** ein Elektron, punktförmiger Kern, kein äußeres Feld. Die typische Geschwindigkeit liegt bei 0,7 % der Lichtgeschwindigkeit, die nichtrelativistische Gleichung reicht also.

:::herleitung Warum der Ansatz trennt
In kartesischen Koordinaten steckt $V$ wegen $r=\sqrt{x^2+y^2+z^2}$ in allen drei Variablen, der Produktansatz der Box trennt nicht. In Kugelkoordinaten hängt $V$ nur von $r$ ab. Einsetzen von $\psi=RY$ und Multiplizieren mit $-2\mu r^2/(\hbar^2RY)$ ergibt

<span class="anker" id="gl-1-3"></span>
$$\frac1R\frac{\mathrm{d}}{\mathrm{d} r}\Bigl(r^2\frac{\mathrm{d} R}{\mathrm{d} r}\Bigr)+\frac{2\mu r^2}{\hbar^2}\bigl(E-V(r)\bigr)=C=-\frac1Y\Bigl[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\Bigl(\sin\theta\frac{\partial Y}{\partial\theta}\Bigr)+\frac{1}{\sin^2\theta}\frac{\partial^2Y}{\partial\varphi^2}\Bigr]. \tag{1.3}$$

Links steht nur $r$, rechts stehen nur die Winkel. Beide Seiten sind also gleich einer Konstanten $C$. Rechts kommt $V$ nicht vor: Der Winkelanteil ist für jedes Zentralpotential derselbe, nur $R$ kennt die Form von $V(r)$.
:::

::::beispiel
Das erlaubte Gebiet endet bei $V(r)=E$, also beim Umkehrradius $r_\mathrm U=e^2/(4\pi\varepsilon_0|E|)$. Für $E=-3{,}4$ eV ist $r_\mathrm U=1{,}44\,\mathrm{eV\,nm}/3{,}4\,\mathrm{eV}=0{,}42$ nm. Im Abstand 0,0529 nm beträgt das Feld des Protons $\mathcal E=e/(4\pi\varepsilon_0r^2)=5{,}1\cdot10^{11}$ V/m, das 170 000-fache der Durchschlagsfeldstärke von Luft. Felder aus Schaltungen stören ein Atom deshalb kaum.
::::

⁠**Grenzfälle:** Für $r\to\infty$ geht $V\to0$, und es bleibt das freie Teilchen aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html). Mit der Kernladung $Ze$ statt $e$ wird $V=-Ze^2/(4\pi\varepsilon_0r)$: Der Trichter wird tiefer, seine Form bleibt.

:::frage Rollt das Elektron wie eine Kugel im Trichter?
Nein. Das Bild zeigt Energie über dem Ort, keine Höhe im Raum, und nur einen Schnitt: $V$ hängt in allen Richtungen gleich von $r$ ab. Das Elektron hat keine Bahn. Es ist eine stehende Welle, die zugleich im ganzen erlaubten Gebiet existiert. Eine rote Linie ist eine Energie, kein Weg.
:::

:::aufgabe Aufgabe 1 ★ Der Trichter in Zahlen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $V$ bei $r=0{,}25$ nm und bei $r=1$ nm in eV.

</li>

<li>

Bis zu welchem Abstand reicht das klassisch erlaubte Gebiet für $E=-1$ eV?

</li>

<li>

Das Ion He$^+$ hat zwei Protonen und ein Elektron. Wie groß ist $V$ dort bei 0,25 nm?

</li>

<li>

Vorhersage: Wie ändert sich der Umkehrradius in He$^+$ bei gleicher Energie $E$? Was sagt das über den Trichter?

</li>

</ol>

:::loesung
(a) $V(0{,}25\,\mathrm{nm})=-1{,}44\,\mathrm{eV\,nm}/0{,}25\,\mathrm{nm}=-5{,}76$ eV, $V(1\,\mathrm{nm})=-1{,}44$ eV. (b) $r_\mathrm U=1{,}44\,\mathrm{eV\,nm}/1\,\mathrm{eV}=1{,}44$ nm. (c) Die doppelte Ladung verdoppelt $V$: $-11{,}52$ eV. (d) $r_\mathrm U=Ze^2/(4\pi\varepsilon_0|E|)$ verdoppelt sich. Der Trichter ist an jeder Stelle doppelt so tief, also reicht er bei gleicher Energie doppelt so weit.
:::
:::
