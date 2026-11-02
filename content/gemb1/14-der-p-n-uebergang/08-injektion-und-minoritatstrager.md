---
title: Stufe 6: Injektion und Minoritätsträger
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der p-n-Übergang
order: 4240800
summary: Die Barriere ist gesunken.
tags: Shockley-Näherung, Gesetz des Übergangs
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Barriere ist gesunken. Diese Stufe bestimmt, wie viele Träger dadurch am Rand der Zone ankommen und wie sie sich im Neutralgebiet dahinter verteilen.
:::

**Die Idee.** Elektronen, die bei Durchlass über die Barriere kommen, landen am linken Rand der Zone im p-Gebiet. Dort sind sie Minoritätsträger: Sie wurden injiziert ([Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html)). Am rechten Rand kommen ebenso Löcher im n-Gebiet an. Ein Feld gibt es dort kaum, die Träger diffundieren und rekombinieren mit den Majoritäten. So klingt ihr Überschuss auf einer Diffusionslänge ab. Alles hängt an den Dichten am Zonenrand. Die __Shockley-Näherung__ macht das rechenbar:

| Annahme | Bedeutung | Im Rechenmodell |
|---|---|---|
| 1. Schwache Injektion | $p_\mathrm n\ll n_\mathrm{n0}$, $n_\mathrm p\ll p_\mathrm{p0}$, Niveaus in der Zone flach | bis rund 0,66 V |
| 2. Störstellenerschöpfung | $n_\mathrm{n0}\approx N_\mathrm D^+$, $p_\mathrm{p0}\approx N_\mathrm A^-$ | 300 K, flache Störstellen |
| 3. Boltzmann-Statistik | $f(E)\approx\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}$ | Abstand $5{,}9$ und $7{,}9\,k_\mathrm BT$ |
| 4. Nur Drift und Diffusion | kein Tunneln durch die Zone | Zone hunderte nm |
| 5. Lange Gebiete | p-Gebiet $\gg L_\text{diff,n}$, n-Gebiet $\gg L_\text{diff,p}$ | über 250 µ m dick |
| 6. Verlustfreie Zone | keine Generation und Rekombination, $j_\mathrm n$, $j_\mathrm p$ dort konstant | 96-mal dünner als $L_\text{diff,p}$ |
| 7. Abrupte Zone | Schottky-Näherung, $L_\mathrm{depl}\gg L_\mathrm{Deb}$ | Stufe [3](zwei-naherungen-fur-die-ladung.html#stufe-3) |

:::satz Satz 6.1 (Randdichten und Minoritätsprofile)
<span class="anker" id="satz-6-1"></span>

Am Rand der Zone gilt das __Gesetz des Übergangs__

<span class="anker" id="gl-6-1"></span>
$$n_\mathrm p(-L_\mathrm{depl}^\mathrm A)=n_\mathrm{p0}\,\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)},\qquad p_\mathrm n(L_\mathrm{depl}^\mathrm D)=p_\mathrm{n0}\,\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}. \tag{6.1}$$

Die Überschüsse $\Delta n_\mathrm p=n_\mathrm p-n_\mathrm{p0}$ und $\Delta p_\mathrm n=p_\mathrm n-p_\mathrm{n0}$ klingen in den Neutralgebieten ab:

<span class="anker" id="gl-6-2"></span>
$$\Delta n_\mathrm p(x)=n_\mathrm{p0}\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr)\mathrm{e}^{(x+L_\mathrm{depl}^\mathrm A)/L_\text{diff,n}},\quad x\le-L_\mathrm{depl}^\mathrm A, \tag{6.2}$$

<span class="anker" id="gl-6-3"></span>
$$\Delta p_\mathrm n(x)=p_\mathrm{n0}\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr)\mathrm{e}^{-(x-L_\mathrm{depl}^\mathrm D)/L_\text{diff,p}},\quad x\ge L_\mathrm{depl}^\mathrm D. \tag{6.3}$$
:::

⁠**So liest man das:** $n_\mathrm p(x)$ und $p_\mathrm n(x)$ sind die Minoritätsdichten ([Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html)). Je $k_\mathrm BT/e=25{,}85$ mV wächst die Randdichte um den Faktor 2,718. **Gültigkeit:** die Annahmen der Tabelle.

:::herleitung Gesetz des Übergangs
<ol>

<li>

$E_\mathrm{Fn}$ bleibt in der Zone flach. Nach [(5.1)](spannung-anlegen.html#gl-5-1) ist $\mathrm{d} E_\mathrm{Fn}/\mathrm{d} x=j_\mathrm n/(\mu_\mathrm nn)$. Bei $U_\mathrm{pn}=0{,}6$ V ist am Rand $n=1{,}9\cdot10^{13}\,\mathrm{cm^{-3}}$ und $j_\mathrm n=15$ mA/cm$^2$. Selbst dieser kleinste Wert von $n$ ergäbe über die ganze Zone nur 0,18 meV, weit unter $k_\mathrm BT$.

</li>

<li>

Am linken Rand ist $E_\mathrm{Fp}$ noch die Fermi-Energie des p-Gebiets, also $n_\mathrm{p0}=N_\mathrm C\exp\bigl(-(E_\mathrm C-E_\mathrm{Fp})/(k_\mathrm BT)\bigr)$.

</li>

<li>

Dort gilt aber $n_\mathrm p=N_\mathrm C\exp\bigl(-(E_\mathrm C-E_\mathrm{Fn})/(k_\mathrm BT)\bigr)$. Einfügen von $\pm E_\mathrm{Fp}$ im Exponenten ergibt

<span class="anker" id="gl-6-4"></span>
$$n_\mathrm p=N_\mathrm C\mathrm{e}^{-(E_\mathrm C-E_\mathrm{Fp})/(k_\mathrm BT)}\,\mathrm{e}^{(E_\mathrm{Fn}-E_\mathrm{Fp})/(k_\mathrm BT)}=n_\mathrm{p0}\,\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}. \tag{6.4}$$

</li>

<li>

Im feldfreien Neutralgebiet gilt die Diffusionsgleichung aus [Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html), $D_\mathrm n\,\mathrm{d}^2\Delta n_\mathrm p/\mathrm{d} x^2=\Delta n_\mathrm p/\tau_{\text{rec},\mathrm n}$. Die Lösung, die für $x\to-\infty$ verschwindet, ist [(6.2)](#gl-6-2) mit dem Randwert. Für Löcher gilt dasselbe gespiegelt.

</li>

</ol>
:::

:::abbildung gemb1/k14injektion 6
Links Durchlass mit +0,5 V, rechts Sperrung mit $-0{,}2$ V, Maßstab µ m, die Zone ist nur noch die senkrechte Linie. Oben: Quasi-Fermi-Niveaus. In der Zone liegen sie flach, in den Neutralgebieten nähert sich das der Minoritäten dem der Majoritäten an. Unten: Dichten, punktiert die Gleichgewichtswerte. Bei Durchlass steigen die Minoritäten am Rand um den Faktor $2{,}5\cdot10^{8}$, bei Sperrung fallen sie fast auf null.
:::

**Beispiel.** Bei $U_\mathrm{pn}=0{,}5$ V ist $\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}=2{,}5\cdot10^{8}$. Am Rand ist $n_\mathrm p=4{,}0\cdot10^{11}\,\mathrm{cm^{-3}}$ und $p_\mathrm n=2{,}0\cdot10^{12}\,\mathrm{cm^{-3}}$ (Abb. [6](#abb-6)). Das sind $8\cdot10^{-6}$ von $N_\mathrm A$ und $2\cdot10^{-4}$ von $N_\mathrm D$, die Injektion ist schwach. $p_\mathrm n=0{,}1\,N_\mathrm D$ wird bei 0,66 V erreicht. **Grenzfälle:** Bei $U_\mathrm{pn}=0$ verschwindet der Überschuss. Für $U_\mathrm{pn}\ll-k_\mathrm BT/e$ ist die Randdichte praktisch null, der Überschuss ist $-n_\mathrm{p0}$ und $-p_\mathrm{n0}$: Die Zone saugt Minoritäten ab.

:::frage Elektronen laufen in das p-Gebiet. Lädt es sich dadurch nicht auf?
Nein. Jeder Elektronenüberschuss zieht in weniger als 1 ps, der Zeit $\tau_\varepsilon$, gleich viele Löcher heran, also ist $\Delta p\approx\Delta n$. Das Neutralgebiet bleibt neutral. Für die Majoritäten ist dieser Zuwachs winzig ($8\cdot10^{-6}$ von $N_\mathrm A$), für die Minoritäten ist er alles. Deshalb zählt man nur die Minoritäten.
:::

:::aufgabe Aufgabe 8 ★★ Am Rand der Zone
<span class="anker" id="aufg-8"></span>

Rechenmodell, $U_\mathrm{pn}=0{,}55$ V.

<ol class="al">

<li>

Berechne die Randdichten $n_\mathrm p$ und $p_\mathrm n$. Ist die Injektion schwach?

</li>

<li>

Bei welcher Spannung erreicht $n_\mathrm p$ am Rand 10 % von $N_\mathrm A$?

</li>

<li>

In welchem Abstand vom Rand sind beide Überschüsse auf 1 % gefallen? Wie dick müssen die Gebiete sein?

</li>

</ol>

:::loesung
(a) $\mathrm{e}^{0{,}55/0{,}02585}=1{,}74\cdot10^{9}$, $n_\mathrm p=2{,}7\cdot10^{12}\,\mathrm{cm^{-3}}$, $p_\mathrm n=1{,}4\cdot10^{13}\,\mathrm{cm^{-3}}$. Das sind $5{,}5\cdot10^{-5}$ von $N_\mathrm A$ und $1{,}4\cdot10^{-3}$ von $N_\mathrm D$: schwach. (b) $U_\mathrm{pn}=k_\mathrm BT/e\cdot\ln(0{,}1N_\mathrm A/n_\mathrm{p0})=0{,}744$ V. Die Löcher erreichen ihre Grenze schon bei 0,66 V. (c) Abfall auf 1 % nach $\ln100=4{,}6$ Diffusionslängen: 225 µ m für Elektronen, 152 µ m für Löcher. Die Gebiete sollten also dicker als rund 250 µ m sein.
:::
:::
