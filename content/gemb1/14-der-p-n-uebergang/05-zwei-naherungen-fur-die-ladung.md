---
title: Stufe 3: Zwei Näherungen für die Ladung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der p-n-Übergang
order: 4240500
summary: Die Poisson-Gleichung braucht rho(x) .
tags: Debye-Länge
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die Poisson-Gleichung braucht $\rho(x)$. Aber $\rho$ hängt von $n$ und $p$ ab, und die hängen vom Potential ab. Diese Stufe zeigt, wie man aus diesem Kreis herauskommt.
:::

**Die Idee.** Im Gleichgewicht gilt [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) mit verschobenen Bandkanten, also $n(x)=n_\mathrm{Bulk}\mathrm{e}^{e\varphi/(k_\mathrm BT)}$ und $p(x)=p_\mathrm{Bulk}\mathrm{e}^{-e\varphi/(k_\mathrm BT)}$. Das ergibt mit [(1.1)](wie-ladung-die-bander-verbiegt.html#gl-1-1) und [(1.2)](wie-ladung-die-bander-verbiegt.html#gl-1-2) eine Differentialgleichung für $\varphi$ allein. Sie ist nur numerisch lösbar. Abb. [3](#abb-3) zeigt das Ergebnis für das Rechenmodell. Zwei Bereiche fallen auf. Im Inneren der Zone fällt die Majoritätsdichte um viele Zehnerpotenzen, und $\rho$ ist die volle Ionenladung. Am Rand geht $\rho$ glatt auf null. Für beide Bereiche gibt es eine Näherung von Hand.

:::abbildung gemb1/k14schottky 3
Vollständige Lösung für das Rechenmodell. Oben: Dichten, jede Sorte fällt quer durch die Zone um 13 Zehnerpotenzen. Unten: Raumladung (blau) und Kastenform (rot gestrichelt). Grau: Zone nach der Kastenform.
:::

**Kleine Störung.** Weicht $n$ nur wenig von $n_0=N_\mathrm D$ ab, $|\Delta n|\ll n_0$, zählen nur die Majoritäten. Die Minoritäten sind hier um den Faktor $10^{12}$ seltener und tragen zu $\rho$ nichts bei: $\rho(x)=-e\,\Delta n(x)$ mit $\Delta n=n-n_0$. Das Feld einer Ladung an der Oberfläche zieht die Majoritäten heran oder drückt sie weg. Die Diffusion wirkt entgegen und verhindert, dass das Gefälle zu steil wird. Gleichgewicht herrscht, wenn sich beide aufheben.

:::satz Satz 3.1 (Debye-Länge)
<span class="anker" id="satz-3-1"></span>

Für $|\Delta n|\ll n_0$ klingt eine Störung im n-Halbleiter exponentiell ab:

<span class="anker" id="gl-3-1"></span>
$$\Delta n(x)=\Delta n(0)\,\mathrm{e}^{-x/L_\mathrm{Deb}},\qquad L_\mathrm{Deb}=\sqrt{D_\mathrm n\tau_\varepsilon}=\sqrt{\frac{\varepsilon_0\varepsilon_\mathrm rk_\mathrm BT}{e^2n_0}},\qquad\tau_\varepsilon=\frac{\varepsilon_0\varepsilon_\mathrm r}{\sigma}. \tag{3.1}$$
:::

⁠**So liest man das:** Die __Debye-Länge__ $L_\mathrm{Deb}$ ist die Abschirmlänge: So weit reicht eine kleine Störung in den Kristall. $\tau_\varepsilon$ ist die dielektrische Relaxationszeit aus [Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html), $\sigma=e\,n_0\mu_\mathrm n$ die Leitfähigkeit. Bei $n_0=10^{16}\,\mathrm{cm^{-3}}$ ist $L_\mathrm{Deb}=41$ nm, bei $5\cdot10^{16}\,\mathrm{cm^{-3}}$ sind es 18 nm. Für p-Halbleiter steht $p_0$ statt $n_0$.

:::herleitung Abschirmung
Das Gleichgewicht verlangt $j_\mathrm n=0$ mit $n\approx n_0$ im Driftterm:

<span class="anker" id="gl-3-2"></span>
$$n_0\,e\,\mu_\mathrm n\mathcal E+e\,D_\mathrm n\frac{\mathrm{d}\Delta n}{\mathrm{d} x}=0. \tag{3.2}$$

Ableiten nach $x$ und [(1.2)](wie-ladung-die-bander-verbiegt.html#gl-1-2) mit $\rho=-e\Delta n$ ergeben $D_\mathrm n\,\mathrm{d}^2\Delta n/\mathrm{d} x^2=\sigma\,\Delta n/(\varepsilon_0\varepsilon_\mathrm r)=\Delta n/\tau_\varepsilon$. Die abklingende Lösung ist [(3.1)](#gl-3-1) mit $L_\mathrm{Deb}^2=D_\mathrm n\tau_\varepsilon$. Mit $D_\mathrm n=\mu_\mathrm nk_\mathrm BT/e$ fällt die Beweglichkeit heraus.
:::

**Große Störung.** Liegt das Band um $\Delta E$ höher als im Inneren, sinkt $n$ auf den Anteil $\mathrm{e}^{-\Delta E/(k_\mathrm BT)}$. Schon bei $3k_\mathrm BT$ sind nur noch 5 % da. Da $\Phi_\mathrm{bi}$ rund $30\,k_\mathrm BT$ beträgt, ist fast die ganze Zone leer. Der Übergang zum Neutralgebiet geschieht auf wenigen Debye-Längen.

:::definition Definition 3.2 (Schottky-Näherung)
<span class="anker" id="satz-3-2"></span>

Die Schottky-Näherung besteht aus zwei Annahmen. Erstens ist der Übergang abrupt: $N_\mathrm A$ ist links, $N_\mathrm D$ rechts der Grenze konstant, jenseits null. Zweitens ist die Raumladung ein Kastenprofil. Mit $x_\mathrm p=-L_\mathrm{depl}^\mathrm A$ und $x_\mathrm n=L_\mathrm{depl}^\mathrm D$ und der Grenze bei $x=0$ ist

<span class="anker" id="gl-3-3"></span>
$$\rho(x)=\begin{cases}-e\,N_\mathrm A^-&\text{für }-L_\mathrm{depl}^\mathrm A<x<0,\\ +e\,N_\mathrm D^+&\text{für }0<x<L_\mathrm{depl}^\mathrm D,\\ 0&\text{sonst.}\end{cases} \tag{3.3}$$
:::

⁠**So liest man das:** $L_\mathrm{depl}^\mathrm A$ und $L_\mathrm{depl}^\mathrm D$ sind die Ausdehnungen der Zone in das p- und das n-Gebiet (depletion, Verarmung). Ein Ort ist entweder ganz verarmt oder ganz neutral. **Gültigkeit:** $L_\mathrm{depl}\gg L_\mathrm{Deb}$ auf der jeweiligen Seite.

::::beispiel
Die Rechnung für Abb. [3](#abb-3) zeigt die Grenzen. Am rechten Rand fällt $\rho$ von 90 % auf 10 % zwischen 210 nm und 351 nm, das sind $3{,}4\,L_\mathrm{Deb}$, links ebenfalls $3{,}4\,L_\mathrm{Deb}$. Der Kasten überschätzt die Gesamtladung und das Feld dennoch nur um 3,6 %, denn was er am Rand zu viel zählt, zählt er daneben zu wenig.
::::

⁠**Grenzfall:** Für $n_0\to\infty$ geht $L_\mathrm{Deb}\to0$: Eine dichte Trägerwolke schirmt auf kürzester Strecke ab.

:::frage Warum endet die Raumladung so scharf, obwohl Träger doch diffundieren?
Sie diffundieren, aber jeder Ladungsüberschuss der Mehrheit erzeugt sofort ein Gegenfeld. Bei $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ fließt er in $\tau_\varepsilon=0{,}54$ ps ab, das ist $1{,}9\cdot10^{6}$-mal kürzer als $\tau_\text{rec}$. Deshalb reicht die Störung nur eine Debye-Länge weit, nicht eine Diffusionslänge.
:::

:::aufgabe Aufgabe 3 ★★ Abschirmlängen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Berechne $L_\mathrm{Deb}$ für $n_0=10^{14}$, $10^{16}$ und $10^{18}\,\mathrm{cm^{-3}}$. Wie hängt sie von $n_0$ und $T$ ab?

</li>

<li>

Eine leere Schicht habe die Bandverbiegung $\Phi(s)=e^2N_\mathrm Ds^2/(2\varepsilon)$ im Abstand $s$ vom Rand der Schicht (Stufe [1](wie-ladung-die-bander-verbiegt.html#stufe-1)). Zeige, dass das Band im Abstand $s=\sqrt6\,L_\mathrm{Deb}$ um $3k_\mathrm BT$ gestiegen ist.

</li>

</ol>

:::loesung
(a) 409 nm, 41 nm und 4,1 nm. $L_\mathrm{Deb}\propto\sqrt{T/n_0}$: Hundertfache Dichte ergibt ein Zehntel. (b) $e^2N_\mathrm Ds^2/(2\varepsilon)=3k_\mathrm BT$ ergibt $s^2=6\,\varepsilon k_\mathrm BT/(e^2N_\mathrm D)=6\,L_\mathrm{Deb}^2$. Bei $10^{16}\,\mathrm{cm^{-3}}$ sind das 100 nm.
:::
:::
