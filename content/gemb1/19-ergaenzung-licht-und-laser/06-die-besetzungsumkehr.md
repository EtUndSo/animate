---
title: Stufe 4: Die Besetzungsumkehr
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Ergänzung: Licht und Laser
order: 4290600
summary: Im selben Stoff kann ein Photon geschluckt oder verdoppelt werden.
tags: Inversion
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Im selben Stoff kann ein Photon geschluckt oder verdoppelt werden. Diese Stufe zeigt, was gewinnt, und warum ein Stoff im Gleichgewicht Licht nie verstärkt.
:::

**Die Idee.** Licht passender Frequenz läuft durch viele Atome. Trifft es ein Elektron auf $E_1$, verschwindet ein Photon. Trifft es eines auf $E_2$, kommt eines hinzu. Beide Treffer sind je Elektron gleich wahrscheinlich (Stufe [3](spontane-und-stimulierte-emission.html#stufe-3)), also entscheidet die Mehrheit. Sitzen oben mehr Elektronen als unten, wächst das Licht lawinenartig (Abb. [4](#abb-4)). Die spontane Emission fehlt in dieser Bilanz: Ihre Photonen fliegen in alle Richtungen und tragen zum Strahl fast nichts bei.

:::abbildung gemb1/k19umkehr 4
Links: Im Gleichgewicht sitzen unten mehr Elektronen als oben, das Licht wird schwächer. Mitte: Bei Besetzungsumkehr wird es stärker (Punktzahlen schematisch). Rechts: Besetzung von $E_2$, wenn man mit Licht derselben Energie pumpt. Die Kurve nähert sich $\frac12$ von unten.
:::

:::satz Satz 4.1 (Licht im Stoff)
<span class="anker" id="satz-4-1"></span>

Läuft passendes Licht in $x$-Richtung durch einen Stoff mit $N_1$ und $N_2$ Elektronen je Volumen auf den beiden Niveaus, gilt

<span class="anker" id="gl-4-1"></span>
$$\frac{\mathrm{d} j_\mathrm{Ph}}{\mathrm{d} x}=A_\mathrm{Ph}(N_2-N_1)\,j_\mathrm{Ph},\quad j_\mathrm{Ph}(x)=j_\mathrm{Ph}(0)\,\mathrm{e}^{-\alpha_\mathrm Px},\quad\alpha_\mathrm P=A_\mathrm{Ph}(N_1-N_2). \tag{4.1}$$
:::

⁠**So liest man das:** Eine Schicht der Dicke $\mathrm{d} x$ und der Fläche 1 enthält $N_1\mathrm{d} x$ Elektronen unten und $N_2\mathrm{d} x$ oben. Mit [(3.2)](spontane-und-stimulierte-emission.html#gl-3-2) verschwinden je Zeit $A_\mathrm{Ph}j_\mathrm{Ph}N_1\mathrm{d} x$ Photonen, und $A_\mathrm{Ph}j_\mathrm{Ph}N_2\mathrm{d} x$ kommen hinzu. $\alpha_\mathrm P$ ist der Absorptionskoeffizient aus [Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html). Für $\alpha_\mathrm P>0$ wird das Licht schwächer, für $\alpha_\mathrm P<0$ stärker, dann ist der Stoff ein Verstärker. **Gültigkeit:** Das Licht darf $N_1$ und $N_2$ längs des Wegs nicht merklich verschieben.

:::satz Satz 4.2 (Besetzung im Gleichgewicht)
<span class="anker" id="satz-4-2"></span>

Im thermischen Gleichgewicht gilt für $E_2>E_1$ bei jeder Temperatur

<span class="anker" id="gl-4-2"></span>
$$f(E_2)<f(E_1),\qquad\frac{N_2}{N_1}=\mathrm{e}^{-(E_2-E_1)/(k_\mathrm BT)}<1. \tag{4.2}$$
:::

:::herleitung Besetzung und Nettorate
$f$ fällt mit $E$, das liefert die Ungleichung. Aus der Fermi-Verteilung folgt $f/(1-f)=\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}$. Mit $f_i=f(E_i)$ hat „oben besetzt, unten frei“ die Wahrscheinlichkeit $f_2(1-f_1)$ und „unten besetzt, oben frei“ die Wahrscheinlichkeit $f_1(1-f_2)$. Ihr Verhältnis ist

$$\frac{f_2(1-f_1)}{f_1(1-f_2)}=\mathrm{e}^{-(E_2-E_1)/(k_\mathrm BT)},$$

denn $E_\mathrm F$ kürzt sich. Teilt sich in jedem Atom ein Elektron zwei Niveaus, sind das die Häufigkeiten $N_2$ und $N_1$. In Bändern besetzen die Elektronen die Niveaus unabhängig. Stimulierte Emission braucht die erste Anordnung, Absorption die zweite, und ihre Differenz ist $f_2(1-f_1)-f_1(1-f_2)=f_2-f_1$. Auch dort entscheidet, welches Niveau stärker besetzt ist.
:::

:::definition Definition 4.3 (Besetzungsumkehr)
<span class="anker" id="satz-4-3"></span>

Ein System zeigt Besetzungsumkehr, auch __Inversion__ genannt, wenn ein höheres Niveau stärker besetzt ist als ein tieferes: $N_2>N_1$, in Bändern $f(E_2)>f(E_1)$. Dieser Ungleichgewichtszustand hält nur, solange von außen Energie zugeführt wird. Diese Zufuhr heißt Pumpen.
:::

Das Pumpen muss laufend ersetzen, was nach unten fällt, je Volumen und Zeit mindestens $N_2/\tau_{21}$ Elektronen. Die Inversion der MOS-Struktur ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html)) meint etwas anderes: Dort kehrt sich an der Oberfläche die Trägersorte um.

**Zwei Niveaus reichen nicht.** Pumpt man mit Licht der Energie $\hbar\omega_{21}$, holt dieses Licht mit derselben Rate Elektronen wieder herunter. Mit $N_1=N-N_2$ gilt

<span class="anker" id="gl-4-3"></span>
$$\frac{\mathrm{d} N_2}{\mathrm{d} t}=r_\mathrm{st}(N_1-N_2)-\frac{N_2}{\tau_{21}},\qquad\text{stationär:}\quad\frac{N_2}N=\frac{r_\mathrm{st}\tau_{21}}{1+2r_\mathrm{st}\tau_{21}}<\frac12. \tag{4.3}$$

Rückt $N_2$ an $N_1$ heran, gleichen sich Absorption und stimulierte Emission aus, und das Licht treibt nichts mehr nach oben. Starkes Licht macht den Stoff durchsichtig, aber nie zum Verstärker.

::::beispiel
Im Stab mit allen Elektronen unten ist $\alpha_\mathrm P=A_\mathrm{Ph}N=0{,}30\,\mathrm{cm^{-1}}$, nach 10 cm kommen noch 5 % an. Mit $N_2-N_1=0{,}2\,N$ wäre $\alpha_\mathrm P=-0{,}06\,\mathrm{cm^{-1}}$, und das Licht würde um den Faktor 1,82 stärker. Im Gleichgewicht ist bei 300 K $N_2/N_1=\mathrm{e}^{-69{,}6}=5{,}8\cdot10^{-31}$, selbst bei 6000 K, der Temperatur der Sonnenoberfläche, nur 0,031. Ein Mikrowellenübergang bei 10 GHz hat 41 µ eV und bei 300 K $N_2/N_1=0{,}9984$: fast gleich, aber unter 1. [(4.3)](#gl-4-3) ergibt für $r_\mathrm{st}\tau_{21}=1$, 10 und 100 die Werte 0,333, 0,476 und 0,498.
::::

⁠**Grenzfälle:** Für $T\to0$ und $r_\mathrm{st}\to0$ sitzt alles unten. Für $T\to\infty$ und $r_\mathrm{st}\to\infty$ wird $N_2=N_1$, also $\alpha_\mathrm P\to0$.

:::frage Kann man die Umkehr nicht durch starkes Heizen erreichen?
Nein. Nach [(4.2)](#gl-4-2) nähert sich $N_2/N_1$ mit wachsendem $T$ dem Wert 1 von unten. Die Elektronen müssen auf einem anderen Weg nach oben kommen, als sie herunterfallen.
:::

:::aufgabe Aufgabe 5 ★★★ Durchsichtig durch Licht
<span class="anker" id="aufg-5"></span>

Zwei Niveaus wie im Rechenmodell, $\tau_{21}=1$ ms, das Licht ist überall gleich stark.

<ol class="al">

<li>

Zeige aus [(4.1)](#gl-4-1) und [(4.3)](#gl-4-3): $\alpha_\mathrm P=A_\mathrm{Ph}N/(1+2r_\mathrm{st}\tau_{21})$.

</li>

<li>

Berechne $\alpha_\mathrm P$ und den Anteil des Lichts, der 1 cm durchquert, für $r_\mathrm{st}\tau_{21}=0$, 1 und 10.

</li>

<li>

Bei welcher Intensität $\hbar\omega_{21}\,j_\mathrm{Ph}$ ist $\alpha_\mathrm P$ auf die Hälfte gesunken?

</li>

</ol>

:::loesung
(a) Aus [(4.3)](#gl-4-3) folgt $N_1-N_2=N-2N_2=N/(1+2r_\mathrm{st}\tau_{21})$, dann [(4.1)](#gl-4-1) einsetzen. (b) Mit $A_\mathrm{Ph}N=0{,}30\,\mathrm{cm^{-1}}$ ist $\alpha_\mathrm P=0{,}300$, 0,100 und 0,014 cm$^{-1}$. Durch 1 cm kommen 74,1 %, 90,5 % und 98,6 %. $\alpha_\mathrm P$ bleibt positiv. (c) Die Hälfte verlangt $r_\mathrm{st}\tau_{21}=\frac12$, also $j_\mathrm{Ph}=1/(2A_\mathrm{Ph}\tau_{21})=1{,}67\cdot10^{22}\,\mathrm{cm^{-2}\,s^{-1}}$. Das sind 4,8 kW/cm$^2$.
:::
:::
