---
title: Stufe 8: Die Diffusionslänge
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
order: 4231000
summary: Licht erzeugt an der Oberfläche ständig Paare.
tags: Rekombinationsgeschwindigkeit
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Licht erzeugt an der Oberfläche ständig Paare. Sie diffundieren ins Innere und rekombinieren unterwegs. Diese Stufe beantwortet die Frage des Kapitels: Wie weit kommen sie?
:::

**Die Idee.** Zwei Vorgänge laufen gegeneinander. Die Diffusion trägt die Löcher in der Zeit $t$ etwa $\sqrt{D_\mathrm pt}$ weit. Die Rekombination beendet ihren Weg nach der Zeit $\tau_\text{rec}$. Also kommen sie rund $\sqrt{D_\mathrm p\tau_\text{rec}}$ weit. An jedem Ort stellt sich ein Gleichgewicht ein: Was durch Diffusion mehr hineinläuft als herausläuft, rekombiniert dort.

:::abbildung gemb1/k13laenge 8
Links: Licht von links, die Tangente bei $x=0$ trifft die Achse bei $L_\text{diff,p}$. Mitte: dünne Platte der Dicke $d$ mit schneller Rekombination auf der Rückseite. Rechts: Paket nach einem Lichtblitz bei $x=0$ zu drei Zeiten, es wird breiter und verliert an Fläche.
:::

:::satz Satz 8.1 (Gleichzeitige Diffusion und Rekombination)
<span class="anker" id="satz-8-1"></span>

Stationär, ohne Feld und hinter der Erzeugungszone wird [(6.9)](die-grundgleichungen-der-halbleiter.html#gl-6-9) zu

<span class="anker" id="gl-8-1"></span>
$$\frac{\Delta p_\mathrm n}{\tau_\text{rec}}=D_\mathrm p\,\frac{\partial^2\Delta p_\mathrm n}{\partial x^2}. \tag{8.1}$$

In einer langen Probe ist die Lösung

<span class="anker" id="gl-8-2"></span>
$$\Delta p_\mathrm n(x)=\Delta p_\mathrm n(x=0)\,\exp\Bigl(-\frac x{L_\text{diff,p}}\Bigr),\qquad L_\text{diff,p}=\sqrt{D_\mathrm p\,\tau_\text{rec}}. \tag{8.2}$$
:::

⁠**So liest man das:** $L_\text{diff,p}$ ist die Diffusionslänge der Löcher als Minderheit im n-Gebiet. Auf dieser Länge sinkt der Überschuss auf 36,8 %, und sie ist die mittlere Tiefe, die ein Träger erreicht. In Silizium und Germanium erreicht sie bis zu 1 cm, meist ist sie viel kleiner. Für Elektronen im p-Gebiet gilt $L_\text{diff,n}=\sqrt{D_\mathrm n\tau_\text{rec}}$. **Gültigkeit:** schwache Injektion, stationär ($\partial\Delta p_\mathrm n/\partial t=0$), Generation nur in der Oberflächenschicht (dahinter $R_\mathrm p-G_\mathrm p=\Delta p_\mathrm n/\tau_\text{rec}$) und $\mathcal E=0$. Das Feld darf man weglassen, wenn $\mathcal E\,L_\text{diff,p}\ll k_\mathrm BT/e$ ist (Aufgabe [7](die-grundgleichungen-der-halbleiter.html#aufg-7)), und die Mehrheit hält die Probe neutral (Stufe [7](erganzung-raumladungen-und-relaxation.html#stufe-7)).

:::herleitung Lösen und einsetzen
Der Ansatz $\mathrm{e}^{\kappa x}$ gibt $\kappa=\pm1/L_\text{diff,p}$, die allgemeine Lösung mit $L=L_\text{diff,p}$ ist $C_1\mathrm{e}^{-x/L}+C_2\mathrm{e}^{+x/L}$. Weit im Innern muss der Überschuss verschwinden, also ist $C_2=0$, und $C_1$ ist der Wert bei $x=0$. Probe: $\partial^2/\partial x^2$ gibt den Faktor $1/L^2=1/(D_\mathrm p\tau_\text{rec})$, und [(8.1)](#gl-8-1) stimmt.
:::

**Beispiel.** Die Probe hat $L_\text{diff,p}=33$ µ m. Bei 164 µ m sind noch 0,7 % übrig. Mit $\Delta p_\mathrm n(0)=10^{13}\,\mathrm{cm^{-3}}$ fließt an der Oberfläche $\mathcal J_\mathrm p(0)=D_\mathrm p\Delta p_\mathrm n(0)/L_\text{diff,p}=3{,}3\cdot10^{16}\,\mathrm{cm^{-2}\,s^{-1}}$, das sind 5,3 mA/cm$^2$. **Kontrolle:** Alles, was eintritt, muss rekombinieren: $\int_0^\infty\Delta p_\mathrm n\,\mathrm{d} x/\tau_\text{rec}=\Delta p_\mathrm n(0)\,L_\text{diff,p}/\tau_\text{rec}$ ergibt wegen $L_\text{diff,p}^2=D_\mathrm p\tau_\text{rec}$ denselben Wert. **Grenzfälle:** Für $\tau_\text{rec}\to\infty$ wird das Profil flach, für $\tau_\text{rec}\to0$ bleiben die Träger an der Oberfläche.

**Dünne Platte.** Rekombiniert auf der Rückseite einer Platte alles sofort, gilt $\Delta p_\mathrm n(d)=0$. Die Gleichung [(8.1)](#gl-8-1) bleibt, und mit festem Wert bei $x=0$ ist

<span class="anker" id="gl-8-3"></span>
$$\Delta p_\mathrm n(x)=\Delta p_\mathrm n(x=0)\,\frac{\sinh\bigl((d-x)/L_\text{diff,p}\bigr)}{\sinh\bigl(d/L_\text{diff,p}\bigr)}. \tag{8.3}$$

Für $d\ll L_\text{diff,p}$ wird daraus die Gerade $\Delta p_\mathrm n(0)(1-x/d)$: Fast niemand rekombiniert unterwegs. Für $d\gg L_\text{diff,p}$ erscheint wieder [(8.2)](#gl-8-2).

**Lichtblitz.** Ein kurzer Blitz erzeuge bei $x=0$ in einer dünnen Platte $G_0$ Paare je Fläche, $G(t=0)=\delta(x)\,G_0$, danach $G=0$, die Oberflächen rekombinieren kaum. Nun ist $\partial\Delta p_\mathrm n/\partial t\ne0$, und mit $\mathcal E=0$ bleibt

<span class="anker" id="gl-8-4"></span>
$$\frac{\partial\Delta p_\mathrm n}{\partial t}=-\frac{\Delta p_\mathrm n}{\tau_\text{rec}}+D_\mathrm p\frac{\partial^2\Delta p_\mathrm n}{\partial x^2},\qquad\Delta p_\mathrm n(x,t)=\frac{G_0}{\sqrt{4\pi D_\mathrm pt}}\exp\Bigl(-\frac{x^2}{4D_\mathrm pt}-\frac t{\tau_\text{rec}}\Bigr). \tag{8.4}$$

Das ist die Gauß-Kurve aus Stufe [3](erganzung-diffusion-aus-unendlicher-und-endlicher-quelle.html#stufe-3) mal dem Zerfallsgesetz. Nach 100 ns ist sie $\sqrt{2D_\mathrm pt}=15$ µ m breit, und 90 % der Paare leben noch.

:::frage Ist die Diffusionslänge der Weg eines einzelnen Trägers?
Nein, seine Tiefe. Der Zickzackweg in der Zeit $\tau_\text{rec}$ ist rund $v_\text{th}\tau_\text{rec}=20$ cm lang. Wegen der ständigen Richtungswechsel bleibt davon nur eine Verschiebung von rund $L_\text{diff,p}=33$ µ m.
:::

:::aufgabe Aufgabe 9 ★★★ Dicke und dünne Probe
<span class="anker" id="aufg-9"></span>

Löcher im n-Gebiet haben $D_\mathrm p=12\,\mathrm{cm^2/s}$ und $\tau_\text{rec}=10$ µ s. Die Vorderseite wird beleuchtet, das Licht wird nur dort absorbiert, $\Delta p_\mathrm n(0)=5\cdot10^{12}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Dicke Probe: Berechne $L_\text{diff,p}$, die Tiefe mit noch 1 % sowie $\mathcal J_\mathrm p(0)$ und $j_\mathrm p(0)$. Gold senkt $\tau_\text{rec}$ um den Faktor 100. Was wird aus $L_\text{diff,p}$ und, bei gleichem Zufluss, aus $\Delta p_\mathrm n(0)$?

</li>

<li>

Dünne Probe, $d=67$ µ m, auf der Rückseite rekombiniert alles sofort: Nenne Differentialgleichung, Art und Randbedingungen. Bestimme die Konstanten der allgemeinen Lösung und zeige [(8.3)](#gl-8-3).

</li>

<li>

Zeige $\mathcal J_\mathrm p(d)/\mathcal J_\mathrm p(0)=1/\cosh(d/L_\text{diff,p})$. Wie viel Prozent erreichen die Rückseite? Welches $d/L_\text{diff,p}$ ist für 90 % höchstens erlaubt?

</li>

<li>

Vernachlässige die Rekombination im Innern und löse neu. Wie groß ist nun das Verhältnis?

</li>

</ol>

:::loesung
(a) $L_\text{diff,p}=110$ µ m, 1 % bei $L\ln100=504$ µ m, $\mathcal J_\mathrm p(0)=D_\mathrm p\Delta p_\mathrm n(0)/L=5{,}5\cdot10^{15}\,\mathrm{cm^{-2}\,s^{-1}}$, $j_\mathrm p(0)=0{,}88$ mA/cm$^2$. Mit Gold ist $L=11$ µ m und $\Delta p_\mathrm n(0)=\mathcal J_\mathrm p(0)L/D_\mathrm p=5\cdot10^{11}\,\mathrm{cm^{-3}}$. (b) $D_\mathrm p\,\mathrm{d}^2\Delta p_\mathrm n/\mathrm{d} x^2=\Delta p_\mathrm n/\tau_\text{rec}$, lineare homogene gewöhnliche Differentialgleichung zweiter Ordnung, $\Delta p_\mathrm n(0)=\Delta_0$, $\Delta p_\mathrm n(d)=0$. Aus $C_1+C_2=\Delta_0$ und $C_1\mathrm{e}^{-d/L}+C_2\mathrm{e}^{d/L}=0$ folgt $C_1=\Delta_0\mathrm{e}^{d/L}/(2\sinh(d/L))$, $C_2=\Delta_0-C_1$, also [(8.3)](#gl-8-3). (c) $\mathcal J_\mathrm p(x)=(D_\mathrm p\Delta_0/L)\cosh((d-x)/L)/\sinh(d/L)$ gibt das Verhältnis $1/\cosh(d/L)$. Mit $d/L=0{,}61$ sind das 84 %. 90 % verlangen $\cosh(d/L)\le1{,}11$, also $d/L\le0{,}47$. (d) $\Delta p_\mathrm n=\Delta_0(1-x/d)$, $\mathcal J_\mathrm p=D_\mathrm p\Delta_0/d$ überall, Verhältnis 1.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Rekombination an der Oberfläche
<span class="anker" id="aufg-10"></span>

Eine dicke p-Probe wird überall gleich beleuchtet, $G_\mathrm n=10^{18}\,\mathrm{cm^{-3}\,s^{-1}}$, mit $\tau_\text{rec}=2$ µ s und $D_\mathrm n=30\,\mathrm{cm^2/s}$. Die Oberfläche bei $x=0$ nimmt Elektronen mit der __Rekombinationsgeschwindigkeit__ $S_\mathrm n=10^4$ cm/s auf: $D_\mathrm n\,\partial\Delta n_\mathrm p/\partial x|_{x=0}=S_\mathrm n\Delta n_\mathrm p(0)$.

<ol class="al">

<li>

Stelle die stationäre Differentialgleichung auf und löse sie. Welche Bedingung gilt für $x\to\infty$?

</li>

<li>

Berechne $L_\text{diff,n}$, $\Delta n_\mathrm p(\infty)$ und $\Delta n_\mathrm p(0)$. Was ergibt sich für $S_\mathrm n\to0$ und $S_\mathrm n\to\infty$?

</li>

</ol>

:::loesung
(a) $D_\mathrm n\,\mathrm{d}^2\Delta n_\mathrm p/\mathrm{d} x^2-\Delta n_\mathrm p/\tau_\text{rec}+G_\mathrm n=0$, im Innern $\Delta n_\mathrm p(\infty)=G_\mathrm n\tau_\text{rec}$. Mit $\Delta n_\mathrm p=G_\mathrm n\tau_\text{rec}+C\mathrm{e}^{-x/L}$ gibt der Rand $-D_\mathrm nC/L=S_\mathrm n(G_\mathrm n\tau_\text{rec}+C)$, also $C=-G_\mathrm n\tau_\text{rec}\,S_\mathrm n/(S_\mathrm n+D_\mathrm n/L)$. (b) $L_\text{diff,n}=77$ µ m, $D_\mathrm n/L=3{,}9\cdot10^{3}$ cm/s, $\Delta n_\mathrm p(\infty)=2\cdot10^{12}\,\mathrm{cm^{-3}}$, $\Delta n_\mathrm p(0)=5{,}6\cdot10^{11}\,\mathrm{cm^{-3}}$. $S_\mathrm n\to0$: überall $G_\mathrm n\tau_\text{rec}$. $S_\mathrm n\to\infty$: $\Delta n_\mathrm p(0)=0$.
:::
:::
