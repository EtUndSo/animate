---
title: Stufe 3: Drei Quantenzahlen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Atome und Orbitale
order: 4140500
summary: n legt die Energie fest, beschreibt den Zustand aber nicht vollständig.
tags: Knotenflächen, Knotenkugeln, Bahndrehimpulsquantenzahl, magnetische Quantenzahl, Schale, Unterschale
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
$n$ legt die Energie fest, beschreibt den Zustand aber nicht vollständig. Eine stehende Welle im Raum braucht drei Angaben, wie in der 3D-Box. Diese Stufe nennt sie und zählt die Zustände.
:::

**Die Idee.** In der Box zählt je eine Zahl die Halbwellen in einer Richtung. Im Atom heißen die Richtungen $r$, $\theta$ und $\varphi$, und auch hier gehört zu jeder Koordinate eine Bedingung. Um die $z$-Achse läuft die Welle im Kreis: Nach einem Umlauf muss sie zu sich selbst passen, also passen ganze Wellenzüge hinein. Das quantisiert den Drehimpuls um die $z$-Achse. Die Zahl der __Knotenflächen__ durch den Kern (Flächen, auf denen die Welle null ist) legt den Betrag des Drehimpulses fest. Die Zahl der __Knotenkugeln__ um den Kern bleibt für die Richtung $r$.

:::satz Satz 3.1 (Die Quantenzahlen des Elektrons im Coulomb-Potential)
<span class="anker" id="satz-3-1"></span>

Ein Zustand ist durch drei Zahlen festgelegt:

<span class="anker" id="gl-3-1"></span>
$$\begin{aligned} n&=1,2,3,\dots&&\text{Energie }E_n,\\ \ell&=0,1,\dots,n-1&&\text{Betrag des Drehimpulses }|\boldsymbol L|=\hbar\sqrt{\ell(\ell+1)},\\ m_\ell&=-\ell,\dots,+\ell&&\text{Komponente in }z\text{-Richtung }L_z=\hbar\,m_\ell. \end{aligned} \tag{3.1}$$

Zu jedem $n$ gehören $\sum_{\ell=0}^{n-1}(2\ell+1)=n^2$ Zustände derselben Energie.
:::

⁠**So liest man das:** $\ell$ heißt __Bahndrehimpulsquantenzahl__, $m_\ell$ __magnetische Quantenzahl__. Die Einheit des Drehimpulses ist $\hbar=1{,}055\cdot10^{-34}$ J s. Die $z$-Richtung ist im Experiment die Richtung eines äußeren Magnetfelds, an dem sich der Drehimpuls des geladenen Elektrons ausrichtet. Ohne Feld ist sie frei wählbar. Aus historischen Gründen schreibt man statt $\ell=0,1,2,3$ die Buchstaben s, p, d, f, also 3p für $n=3$, $\ell=1$. Alle Zustände mit gleichem $n$ bilden eine __Schale__ (auch Hauptschale), alle mit gleichem $n$ und $\ell$ eine __Unterschale__. **Gültigkeit:** Dass $E$ nur von $n$ abhängt, gilt nur für ein Elektron im reinen $1/r$-Potential.

:::abbildung gemb1/k4zaehlen 3
Alle Zustände bis $n=4$, je Strich einer, Abstände nicht maßstäblich. Alle Striche einer Zeile haben dieselbe Energie. Eine Unterschale hat $2\ell+1$ Striche, eine Schale $n^2$.
:::

:::herleitung Woher die drei Bedingungen kommen
<ol>

<li>

⁠**Umlauf.** Der Winkelanteil trennt weiter in $Y=\Theta(\theta)\,\mathrm{e}^{\mathrm{j} m_\ell\varphi}$. $\varphi$ und $\varphi+2\pi$ sind derselbe Punkt, also muss $\mathrm{e}^{\mathrm{j} m_\ell2\pi}=1$ sein: $m_\ell$ ist ganz. Mit der Bogenlänge $b=r\varphi$ und dem Impulsoperator aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html) ist $\hat p=\frac{\hbar}{\mathrm{j}}\,\partial/\partial b$, also $\hat L_z=r\,\hat p=\frac{\hbar}{\mathrm{j}}\,\partial/\partial\varphi$. Auf $\mathrm{e}^{\mathrm{j} m_\ell\varphi}$ angewandt ergibt das $\hbar m_\ell$.

</li>

<li>

⁠**Pole.** Die Gleichung für $Y$ in [(1.3)](der-kern-als-kasten-ohne-wande.html#gl-1-3) hat nur dann auch auf der $z$-Achse, bei $\theta=0$ und $\theta=\pi$, endliche Lösungen, wenn $C=\ell(\ell+1)$ ist, mit ganzem $\ell\ge|m_\ell|$. Probe: $Y=1$ gibt $C=0$, und $Y=\cos\theta$ gibt $C=2$. Die Klammer dort ist die Krümmung auf der Kugelfläche. Sie liefert die Bewegungsenergie der Drehung, $|\boldsymbol L|^2/(2m_0r^2)$, also ist $|\boldsymbol L|^2=\hbar^2\ell(\ell+1)$.

</li>

<li>

⁠**Radius.** Mit diesem $C$ wirkt in der Radialgleichung zusätzlich die Energie $\hbar^2\ell(\ell+1)/(2m_0r^2)$. Drehimpuls drängt das Elektron also vom Kern weg. Wie in der Box hat der $n$-te Zustand $n-1$ Knoten, $\ell$ davon sind Knotenflächen, $n-\ell-1\ge0$ Knotenkugeln. Daraus folgt $\ell\le n-1$.

</li>

</ol>
:::

::::beispiel
Für $n=2$ gibt es $\ell=0$ mit $m_\ell=0$ und $\ell=1$ mit $m_\ell=-1,0,+1$, zusammen vier Zustände mit $E_2=-3{,}40$ eV. Sie sind entartet ([Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)). Dass die Energie nicht von $m_\ell$ abhängt, folgt aus der Kugelsymmetrie: Keine Richtung ist ausgezeichnet. Dass sie auch nicht von $\ell$ abhängt, ist eine Besonderheit des $1/r$-Potentials. Für $\ell=1$ ist $|\boldsymbol L|=\sqrt2\,\hbar=1{,}49\cdot10^{-34}$ J s.
::::

⁠**Grenzfälle:** Für $\ell=0$ ist $|\boldsymbol L|=0$. Dieser Zustand hat keine Entsprechung auf einer klassischen Kreisbahn. Für großes $\ell$ nähert sich das größte $L_z$ dem Betrag: $\ell/\sqrt{\ell(\ell+1)}$ ist 0,707 für $\ell=1$ und 0,995 für $\ell=100$.

:::frage Warum ist $|\boldsymbol L|$ nicht $\hbar\ell$? Warum zeigt der Drehimpuls nie genau in $z$-Richtung?
Zeigte $\boldsymbol L$ genau in $z$-Richtung, läge die Bewegung genau in der Ebene $z=0$. Die Welle wäre dann in einer Schicht der Dicke null eingesperrt, und das kostet nach [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) unendlich viel Energie. Deshalb bleibt immer ein Rest senkrecht zu $z$, und $|\boldsymbol L|$ ist größer als das größte $L_z=\hbar\ell$.
:::

:::aufgabe Aufgabe 4 ★★ Zustände zählen
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Welche Angaben $(n,\ell,m_\ell)$ sind erlaubt? $(3,2,-2)$, $(2,2,0)$, $(4,0,1)$, $(4,3,-3)$, $(1,0,0)$, $(3,-1,0)$. Begründe jedes Verbot.

</li>

<li>

Liste alle Unterschalen zu $n=3$ mit ihrer Zahl von Zuständen auf.

</li>

<li>

Berechne $|\boldsymbol L|$ für $\ell=2$ in J s. Welche Winkel kann $\boldsymbol L$ mit der $z$-Achse bilden?

</li>

<li>

Zeige, dass $Y=3\cos^2\theta-1$ die Gleichung in [(1.3)](der-kern-als-kasten-ohne-wande.html#gl-1-3) mit $C=6$ löst. Welches $\ell$ ist das?

</li>

</ol>

:::loesung
(a) Erlaubt: $(3,2,-2)$, $(4,3,-3)$, $(1,0,0)$. Verboten: $(2,2,0)$, denn $\ell\le n-1$. $(4,0,1)$, denn $|m_\ell|\le\ell$. $(3,-1,0)$, denn $\ell\ge0$. (b) 3s mit einem Zustand, 3p mit drei, 3d mit fünf, zusammen $9=3^2$. (c) $|\boldsymbol L|=\sqrt6\,\hbar=2{,}58\cdot10^{-34}$ J s. Aus $\cos\alpha=m_\ell/\sqrt6$ folgen $\alpha=35{,}3^\circ$, $65{,}9^\circ$, $90^\circ$, $114{,}1^\circ$, $144{,}7^\circ$. (d) $\partial_\theta Y=-6\cos\theta\sin\theta$. Dann ist $\frac{1}{\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta Y)=6\sin^2\theta-12\cos^2\theta=6-18\cos^2\theta=-6\,Y$. $Y$ hängt nicht von $\varphi$ ab, also ist $C=6=2\cdot3$ und $\ell=2$.
:::
:::
