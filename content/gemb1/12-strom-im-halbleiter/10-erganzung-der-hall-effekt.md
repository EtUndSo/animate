---
title: Stufe 8: Ergänzung: Der Hall-Effekt
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Strom im Halbleiter
order: 4221000
summary: Aus sigma allein lassen sich n und mu nicht trennen, und das Vorzeichen der Träger bleibt unbekannt.
tags: Hall-Spannung, Lorentz-Kraft, Hall-Koeffizient, Hall-Winkel
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Aus $\sigma$ allein lassen sich $n$ und $\mu$ nicht trennen, und das Vorzeichen der Träger bleibt unbekannt. Ein Magnetfeld liefert die fehlende Messung.
:::

**Die Idee.** Das Magnetfeld lenkt bewegte Ladungen seitlich ab. Sie sammeln sich am Rand, und ihr Feld wächst, bis es die Ablenkung aufhebt. Zwischen den Rändern liegt dann die __Hall-Spannung__ (Abb. [8](#abb-8)). Elektronen und Löcher werden an denselben Rand gedrückt, denn Ladung und Laufrichtung sind beide entgegengesetzt. Sie laden ihn aber verschieden auf, also verrät das Vorzeichen die Trägersorte.

:::satz Satz 8.1 (Hall-Spannung bei einer Trägersorte)
<span class="anker" id="satz-8-1"></span>

Eine Platte der Dicke $d$ und Breite $w$ führt den Strom $I$ in $x$-Richtung, $B$ zeigt in $z$-Richtung. Mit der __Lorentz-Kraft__ $\boldsymbol F_\mathrm L=q\,\boldsymbol v_\mathrm d\times\boldsymbol B$ gilt

<span class="anker" id="gl-8-1"></span>
$$\mathcal E_\mathrm H=R_\mathrm H\,\frac{IB}{w\,d},\qquad U_\mathrm H=w\,\mathcal E_\mathrm H=R_\mathrm H\,\frac{IB}d, \tag{8.1}$$

<span class="anker" id="gl-8-2"></span>
$$R_\mathrm H=-\frac1{ne}\quad\text{(Elektronen)},\qquad R_\mathrm H=+\frac1{pe}\quad\text{(Löcher)}. \tag{8.2}$$
:::

⁠**So liest man das:** $R_\mathrm H$ ist der __Hall-Koeffizient__ in m$^3$/C, eine Stoffgröße. $\mathcal E_\mathrm H$ ist die $y$-Komponente des Feldes, $U_\mathrm H$ die Spannung vom Rand bei $-w/2$ zum Rand bei $+w/2$. **Gültigkeit:** eine Trägersorte, $\mu B\ll1$, Abgriff in der Mitte zwischen den Stromkontakten.

:::herleitung Kräftegleichgewicht
Es ist $I_x=-e\,n\,v_{\mathrm d,x}\,w\,d$. Mit $\boldsymbol B=(0,0,B_z)$ ist $F_{\mathrm L,x}=F_{\mathrm L,z}=0$ und $F_{\mathrm L,y}=e\,v_{\mathrm d,x}B_z$. Im stationären Zustand gleicht die Kraft $-e\mathcal E_\mathrm H$ die Lorentz-Kraft aus, also $\mathcal E_\mathrm H=v_{\mathrm d,x}B_z=-IB/(n\,e\,w\,d)$. Für Löcher ist $q=+e$ und $I_x=+e\,p\,v_{\mathrm d,x}\,w\,d$, daher das andere Vorzeichen.
:::

:::abbildung gemb1/k12hall 8
Links: Elektronenleitende Platte von oben, $B$ zeigt aus der Bildebene. Die Lorentz-Kraft drückt die Elektronen nach unten, das Feld $\mathcal E_\mathrm H$ der Randladungen gleicht sie aus. Rechts: $|R_\mathrm H|$ von Silizium mit $N=10^{16}\,\mathrm{cm^{-3}}$ und $b=3{,}1$. Bei $1000/T=1{,}53$ wechselt der p-Typ das Vorzeichen.
:::

:::satz Satz 8.2 (Beide Trägersorten)
<span class="anker" id="satz-8-2"></span>

Sind Elektronen und Löcher beteiligt, gilt

<span class="anker" id="gl-8-3"></span>
$$R_\mathrm H=\frac1e\,\frac{p\,\mu_\mathrm p^2-n\,\mu_\mathrm n^2}{(p\,\mu_\mathrm p+n\,\mu_\mathrm n)^2}, \tag{8.3}$$

in Eigenleitung $R_\mathrm H=\dfrac1{n_\mathrm ie}\dfrac{1-b}{1+b}$ mit $b=\mu_\mathrm n/\mu_\mathrm p>1$, in Erschöpfung $R_\mathrm H=-1/(N_\mathrm De)$ oder $R_\mathrm H=+1/(N_\mathrm Ae)$.
:::

⁠**So liest man das:** Quer fließt insgesamt nichts, $j_y=0$, und jede Sorte zählt mit $\mu^2$: einmal als Geschwindigkeit, einmal als Reaktion auf das Querfeld. In Eigenleitung gewinnen die schnelleren Elektronen, $R_\mathrm H<0$. Beim n-Typ bleibt $R_\mathrm H$ daher negativ. Beim p-Typ liegt zwischen Erschöpfung und Eigenleitung ein Nulldurchgang bei $p\,\mu_\mathrm p^2=n\,\mu_\mathrm n^2$. Messungen an InSb, mit kleiner Lücke und großem $b$, zeigen das deutlich. Dort gilt oberhalb von rund $4\cdot10^{16}\,\mathrm{cm^{-3}}$ die Boltzmann-Näherung nicht mehr, weil $N_\mathrm C$ so klein ist.

**Hall-Winkel und Strombahnen.** Das Hall-Feld überlagert sich dem Längsfeld $\mathcal E_\mathrm a=j_x/(n\,\mu_\mathrm n\,e)$. Strom und Gesamtfeld sind nicht mehr parallel, ihr Winkel ist der __Hall-Winkel__:

<span class="anker" id="gl-8-4"></span>
$$\tan\Theta_\mathrm H=\frac{\mathcal E_\mathrm H}{\mathcal E_\mathrm a}=-\mu_\mathrm nB. \tag{8.4}$$

Er ist überall in der Platte gleich, unabhängig von Form und Kontakten, und misst $\mu$ direkt. An den Stromkontakten schließen die Metallflächen das Hall-Feld kurz: Die Lorentz-Kraft bleibt dort unkompensiert, es entsteht ein Stromanteil $j_y$, und die Strombahnen laufen schräg. Zwischen den Kontakten ist $j_y=0$.

**Beispiel.** Eine Platte aus dem Material der Probe mit $d=0{,}5$ mm, $w=5$ mm, $I=1$ mA und $B=0{,}5$ T hat $R_\mathrm H=-6{,}24\cdot10^{-4}\,\mathrm{m^3/C}$, $U_\mathrm H=-0{,}62$ mV und wegen $\mu_\mathrm nB=0{,}06$ den Hall-Winkel $3{,}4^\circ$. Kupfer gäbe nur $-0{,}074$ nV, denn $U_\mathrm H\propto1/n$. Aus $|R_\mathrm H|$ folgt die Dichte, mit $\sigma$ die Beweglichkeit: $\mu=|R_\mathrm H|\,\sigma$. **Grenzfall:** Für $B=0$ ist $U_\mathrm H=0$.

:::aufgabe Aufgabe 9 ★★ Eine Probe vermessen
<span class="anker" id="aufg-9"></span>

Eine Siliziumplatte hat $d=0{,}4$ mm, $w=4$ mm, die Längskontakte liegen 12 mm auseinander. Bei $I=2$ mA und $B=0{,}8$ T misst du $U_\mathrm H=+1{,}2$ mV und die Längsspannung 0,12 V.

<ol class="al">

<li>

Welche Trägersorte liegt vor? Berechne $R_\mathrm H$, die Dichte, $\sigma$, $\rho$, die Beweglichkeit und $\Theta_\mathrm H$.

</li>

<li>

Zeige für einen p-Halbleiter, dass $R_\mathrm H=0$ bei $n_\mathrm i=N_\mathrm A/(b-1/b)$ liegt. Wie groß sind dort $n_\mathrm i$, $p$ und $n$ für $N_\mathrm A=2\cdot10^{15}\,\mathrm{cm^{-3}}$ und $b=2$?

</li>

<li>

Vorhersage: Warum kann ein n-Halbleiter mit $b>1$ keinen Nulldurchgang haben?

</li>

</ol>

:::loesung
(a) Positives $U_\mathrm H$: Löcher. $R_\mathrm H=U_\mathrm Hd/(IB)=3{,}0\cdot10^{-4}\,\mathrm{m^3/C}$, $p=1/(eR_\mathrm H)=2{,}08\cdot10^{16}\,\mathrm{cm^{-3}}$, $\sigma=(I/U)\,L/(w\,d)=125$ S/m, $\rho=0{,}80\,\Omega$ cm, $\mu_\mathrm p=R_\mathrm H\sigma=375\,\mathrm{cm^2/(V\,s)}$, $\tan\Theta_\mathrm H=\mu_\mathrm pB=0{,}030$, also $1{,}7^\circ$. (b) $R_\mathrm H=0$ verlangt $p=b^2n$. Mit $pn=n_\mathrm i^2$ ist $p=b\,n_\mathrm i$, $n=n_\mathrm i/b$, und $p-n=N_\mathrm A$ gibt die Formel. Zahlen: $n_\mathrm i=1{,}33\cdot10^{15}$, $p=2{,}67\cdot10^{15}$, $n=6{,}7\cdot10^{14}\,\mathrm{cm^{-3}}$. (c) Der Zähler von [(8.3)](#gl-8-3) wäre null nur bei $p=b^2n>n$. Beim n-Typ ist aber stets $n\ge p$.
:::
:::
