---
title: Stufe 8: Die Kapazität in allen Bereichen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Die MOS-Kapazität
order: 4251000
summary: Die Struktur heißt Kondensator, ihre Kapazität ist aber keine Konstante.
tags: Raumladungskapazität
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Die Struktur heißt Kondensator, ihre Kapazität ist aber keine Konstante. Diese Stufe berechnet sie für alle Bereiche aus der exakten Ladung.
:::

**Die Idee.** Ändert man $V_\mathrm G$ wenig, ändert sich die Ladung um $\mathrm{d} Q'_\mathrm{SC}$. Sie erzeugt im Isolator $\mathrm{d} V_\mathrm{IS}$ und im Halbleiter $\mathrm{d}\varphi_\mathrm s$. Beide Schichten tragen dieselbe Ladungsänderung, das ist eine Reihenschaltung. Im Halbleiter reagieren Ionen am Zonenrand und bewegliche Ladung an der Grenzfläche auf dieselbe Änderung $\mathrm{d}\varphi_\mathrm s$, das ist eine Parallelschaltung. Die Rechnung gilt für langsame Änderungen, sodass alle Ladungen folgen.

:::satz Satz 8.1 (Kapazität des MIS-Kondensators)
<span class="anker" id="satz-8-1"></span>

Mit der __Raumladungskapazität__ $C'_\mathrm{SC}=|\mathrm{d} Q'_\mathrm{SC}/\mathrm{d}\varphi_\mathrm s|$ gilt

<span class="anker" id="gl-8-1"></span>
$$\frac1{C'_\mathrm{ges}}=\frac1{C'_\mathrm{IS}}+\frac1{C'_\mathrm{SC}(\varphi_\mathrm s)},\qquad C'_\mathrm{SC}=C'_\mathrm{depl}+C'_\mathrm{inv/acc},\qquad C'_\mathrm{ges}=\frac{\bigl(C'_\mathrm{depl}+C'_\mathrm{inv/acc}\bigr)C'_\mathrm{IS}}{C'_\mathrm{depl}+C'_\mathrm{inv/acc}+C'_\mathrm{IS}}. \tag{8.1}$$
:::

:::herleitung Kapazitiver Spannungsteiler
$Q'_\mathrm{SC}$ fällt überall mit steigendem $\varphi_\mathrm s$, also ist $\mathrm{d} Q'_\mathrm{SC}=-C'_\mathrm{SC}\,\mathrm{d}\varphi_\mathrm s$. Aus [(2.2)](wie-sich-die-gatespannung-aufteilt.html#gl-2-2) folgt $\mathrm{d} V_\mathrm G=\mathrm{d}\varphi_\mathrm s\,(1+C'_\mathrm{SC}/C'_\mathrm{IS})$, und daraus

$$\frac{\mathrm{d}\varphi_\mathrm s}{\mathrm{d} V_\mathrm G}=\frac{C'_\mathrm{IS}}{C'_\mathrm{IS}+C'_\mathrm{SC}},\qquad C'_\mathrm{ges}=\Bigl|\frac{\mathrm{d} Q'_\mathrm{SC}}{\mathrm{d} V_\mathrm G}\Bigr|=C'_\mathrm{SC}\,\frac{\mathrm{d}\varphi_\mathrm s}{\mathrm{d} V_\mathrm G}=\frac{C'_\mathrm{SC}C'_\mathrm{IS}}{C'_\mathrm{SC}+C'_\mathrm{IS}}.$$

Die Ladung im Halbleiter ist die Summe aus Ionen und beweglicher Ladung, also addieren sich ihre Ableitungen.
:::

:::satz Satz 8.2 (Exakte Ladung, p-Substrat)
<span class="anker" id="satz-8-2"></span>

<span class="anker" id="gl-8-2"></span>
$$Q'_\mathrm{SC}=\mp\sqrt{2e\varepsilon\,F(\varphi_\mathrm s)},\qquad F=N_\mathrm A\bigl(V_\mathrm T\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}+\varphi_\mathrm s-V_\mathrm T\bigr)+n_{p0}\bigl(V_\mathrm T\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}-\varphi_\mathrm s-V_\mathrm T\bigr). \tag{8.2}$$

Das obere Vorzeichen gilt für $\varphi_\mathrm s>0$, das untere für $\varphi_\mathrm s<0$.
:::

:::herleitung Poisson-Gleichung einmal integrieren
Die Dichten folgen dem Potential wie in [(2.3)](wie-sich-die-gatespannung-aufteilt.html#gl-2-3), also ist $\rho(\varphi)=e\bigl[N_\mathrm A(\mathrm{e}^{-\varphi/V_\mathrm T}-1)-n_{p0}(\mathrm{e}^{\varphi/V_\mathrm T}-1)\bigr]$. Multipliziert man $\mathrm{d}^2\varphi/\mathrm{d} x^2=-\rho/\varepsilon$ mit $2\,\mathrm{d}\varphi/\mathrm{d} x$, steht links die Ableitung von $(\mathrm{d}\varphi/\mathrm{d} x)^2$. Integration von $x\to\infty$, wo Feld und Potential null sind, ergibt

$$\Bigl(\frac{\mathrm{d}\varphi}{\mathrm{d} x}\Bigr)^2=-\frac2\varepsilon\int_0^\varphi\rho(u)\,\mathrm{d} u=\frac{2e}{\varepsilon}F(\varphi).$$

Nach dem gaußschen Satz ist $|Q'_\mathrm{SC}|=\varepsilon\,|\mathcal E(0)|$. Für kleine $\varphi_\mathrm s$ gibt die Reihe von $\mathrm{e}^{\mp u}$ bis $u^2/2$ den Wert $F\approx(N_\mathrm A+n_{p0})\varphi_\mathrm s^2/(2V_\mathrm T)$.
:::

| Bereich | $Q'_\mathrm{SC}$ | $C'_\mathrm{SC}$ |
|---|---|---|
| Akkumulation, $-\varphi_\mathrm s\gg V_\mathrm T$ | $+\sqrt{2e\varepsilon N_\mathrm AV_\mathrm T\bigl(\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}-1\bigr)}$ | $C'_\mathrm{acc}\approx\vert Q'_\mathrm{SC}\vert /(2V_\mathrm T)$, groß |
| Flachband, $\varphi_\mathrm s=0$ | $Q'_\mathrm{SC}=0$ | $C'_\mathrm{FB}=\sqrt{\frac{e\varepsilon}{V_\mathrm T}(n_{p0}+N_\mathrm A)}\approx\frac{\varepsilon}{L_\mathrm D}$ |
| Verarmung, schwache Inversion | $-\sqrt{2e\varepsilon N_\mathrm A\varphi_\mathrm s}$ | $C'_\mathrm{depl}=\sqrt{\frac{e\varepsilon N_\mathrm A}{2\varphi_\mathrm s}}=\frac{\varepsilon}{L_\mathrm{depl}}$ |
| starke Inversion, $\varphi_\mathrm s>\varphi_\mathrm{s,SI}$ | $-\sqrt{2e\varepsilon\bigl[n_{p0}V_\mathrm T(\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}-1)+N_\mathrm A\varphi_\mathrm s\bigr]}$ | $C'_\mathrm{inv}\approx\vert Q'_\mathrm{SC}\vert /(2V_\mathrm T)$, groß |

⁠**So liest man das:** Eine Spannungsänderung schiebt in Verarmung nur den Zonenrand, die Zone wirkt wie ein Plattenkondensator der Dicke $L_\mathrm{depl}$. Das ist die Ableitung von $Q'_\mathrm{depl}=-eN_\mathrm AL_\mathrm{depl}$ nach $\varphi_\mathrm s$. Exponentiell wachsende Ladung gibt $\mathrm{d}|Q'|/\mathrm{d}\varphi_\mathrm s=|Q'|/(2V_\mathrm T)$. In Akkumulation und starker Inversion ist deshalb $C'_\mathrm{SC}\gg C'_\mathrm{IS}$ und $C'_\mathrm{ges}\approx C'_\mathrm{IS}$: ein regulärer Plattenkondensator. In Verarmung ist $C'_\mathrm{ges}=C'_\mathrm{depl}C'_\mathrm{IS}/(C'_\mathrm{depl}+C'_\mathrm{IS})$, die Kapazität sinkt, weil die Zone wächst (Abb. [8](#abb-8)).

:::abbildung gemb1/k15kapazitaet 8
Links: Ersatzschaltbild, $C'_\mathrm{IS}$ in Reihe zur Parallelschaltung im Halbleiter. Rechts: Kapazität des Rechenmodells, blau exakt aus [(8.2)](#gl-8-2), gestrichelt nur Verarmung. Beide Enden nähern sich $C'_\mathrm{IS}$.
:::

**Beispiel.** Die Tabelle zeigt das Rechenmodell mit $C'_\mathrm{IS}=172{,}7\,\mathrm{nF/cm^2}$. Das Minimum liegt mit 46,2 nF/cm$^2$ bei $\varphi_\mathrm s=0{,}68$ V.

| $\varphi_\mathrm s$ in V | $-0{,}15$ | 0 | 0,1 | 0,3 | 0,6 | 0,777 | 0,9 |
|---|---|---|---|---|---|---|---|
| $\vert Q'_\mathrm{SC}\vert $ in nC/cm$^2$ | 288,9 | 0 | 27,3 | 52,3 | 75,6 | 88,0 | 196 |
| $C'_\mathrm{SC}$ in nF/cm$^2$ | 5688 | 438,9 | 178,8 | 95,3 | 65,9 | 113,2 | 2956 |
| $C'_\mathrm{ges}/C'_\mathrm{IS}$ | 0,971 | 0,718 | 0,509 | 0,356 | 0,276 | 0,396 | 0,945 |

⁠**Grenzfälle:** Die Kastenformel gibt bei 0,3 V den Wert 54,7 statt 52,3 nC/cm$^2$. Genauer steht in Verarmung $\varphi_\mathrm s-V_\mathrm T$ unter der Wurzel, das ist die weiche Kante aus Abb. [4](verarmung.html#abb-4). Bei $\varphi_\mathrm{s,SI}$ ist $n_{p0}\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}=N_\mathrm A$. Dann ist $F=N_\mathrm A\varphi_\mathrm s$, die Kastenformel stimmt wieder, und $C'_\mathrm{SC}=2C'_\mathrm{depl}$: Elektronen und Ionen tragen gleich viel bei.

**Grenze durch die Zustandsdichte.** Liegt $E_\mathrm F$ an der Grenzfläche im Band, gilt die Boltzmann-Näherung nicht mehr, und die Zahl freier Zustände bestimmt $C'_\mathrm{inv}$. Hebt man $\varphi_\mathrm s$ um $\mathrm{d}\varphi_\mathrm s$, sinken alle Niveaus um $e\,\mathrm{d}\varphi_\mathrm s$, und nur Zustände direkt an $E_\mathrm F$ werden neu besetzt, denn $\partial f/\partial E$ wirkt wie eine Deltafunktion. Mit [(7.2)](die-inversionsschicht-als-quantentopf.html#gl-7-2) ergibt das

<span class="anker" id="gl-8-3"></span>
$$C'_\mathrm{inv}\approx e^2D_\mathrm s(E_\mathrm F). \tag{8.3}$$

Mit dreidimensionaler Zustandsdichte wächst das wie $\sqrt{E_\mathrm F-E_\mathrm{C,0}}$, im Subband ist es konstant. Mit $D_\mathrm s=1{,}59\cdot10^{14}/(\mathrm{eV\,cm^2})$ sind es 25,4 µ F/cm$^2$, das 147-Fache von $C'_\mathrm{IS}$, also $C'_\mathrm{ges}=0{,}993\,C'_\mathrm{IS}$. Erst bei 2 nm Oxid wird die Abweichung mit 6 % merklich.

:::frage Warum ist die Kapazität bei Akkumulation und starker Inversion gleich, obwohl verschiedene Ladungsträger beteiligt sind?
Der Isolator merkt nur, dass an seiner Unterseite eine dünne leitende Schicht jede Ladungsänderung übernimmt. Der Plattenabstand ist beide Male $d_\mathrm{IS}$.
:::

:::aufgabe Aufgabe 10 ★★ Kapazität berechnen
<span class="anker" id="aufg-10"></span>

Gegeben sind $N_\mathrm A=10^{16}\,\mathrm{cm^{-3}}$ und $d_\mathrm{IS}=30$ nm $\mathrm{SiO_2}$.

<ol class="al">

<li>

Berechne $C'_\mathrm{IS}$, $C'_\mathrm{FB}$ und $C'_\mathrm{ges}$ im Flachbandfall.

</li>

<li>

Berechne $C'_\mathrm{depl}$ und $C'_\mathrm{ges}$ bei $\varphi_\mathrm s=0{,}2$ und 0,5 V. Wie groß ist jeweils $L_\mathrm{depl}$?

</li>

<li>

Berechne mit [(8.2)](#gl-8-2) die Ladung bei $\varphi_\mathrm s=-0{,}15$ und $+0{,}8$ V und schätze $C'_\mathrm{SC}$ mit $|Q'|/(2V_\mathrm T)$. Wie nah kommt $C'_\mathrm{ges}$ an $C'_\mathrm{IS}$?

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=115{,}1\,\mathrm{nF/cm^2}$, $L_\mathrm D=40{,}9$ nm, $C'_\mathrm{FB}=253{,}4\,\mathrm{nF/cm^2}$, $C'_\mathrm{ges}=79{,}1\,\mathrm{nF/cm^2}$, das 0,69-Fache. (b) 0,2 V: $L_\mathrm{depl}=161$ nm, $C'_\mathrm{depl}=64{,}4\,\mathrm{nF/cm^2}$, $C'_\mathrm{ges}=41{,}3\,\mathrm{nF/cm^2}$. 0,5 V: 254 nm, $40{,}7\,\mathrm{nF/cm^2}$, $30{,}1\,\mathrm{nF/cm^2}$. (c) $-0{,}15$ V: $|Q'|=166{,}8\,\mathrm{nC/cm^2}$, $C'_\mathrm{SC}\approx3226\,\mathrm{nF/cm^2}$, $C'_\mathrm{ges}=0{,}966\,C'_\mathrm{IS}$. $+0{,}8$ V: $|Q'|=66{,}6\,\mathrm{nC/cm^2}$, $C'_\mathrm{SC}\approx1287\,\mathrm{nF/cm^2}$, $C'_\mathrm{ges}\approx0{,}918\,C'_\mathrm{IS}$. Die letzte Schätzung ist zu groß, denn bei 0,8 V tragen die Ionen noch einen Teil der Ladung, exakt sind es 566 nF/cm$^2$ und das 0,83-Fache.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Grenzfälle aus einer Formel
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Zeige aus [(8.2)](#gl-8-2), dass für $V_\mathrm T\ll\varphi_\mathrm s<\varphi_\mathrm{s,WI}$ der Ausdruck $Q'_\mathrm{SC}=-\sqrt{2e\varepsilon N_\mathrm A(\varphi_\mathrm s-V_\mathrm T)}$ folgt. Welche Terme fallen weg, und warum?

</li>

<li>

Zeige $C'_\mathrm{FB}=\varepsilon/L_\mathrm D$ für $N_\mathrm A\gg n_{p0}$.

</li>

<li>

Zeige, dass $C'_\mathrm{SC}=2C'_\mathrm{depl}$ bei $\varphi_\mathrm{s,SI}$ gilt.

</li>

</ol>

:::loesung
(a) Für $\varphi_\mathrm s\gg V_\mathrm T$ ist $V_\mathrm T\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}\ll V_\mathrm T$, das fällt weg. Der Term mit $n_{p0}$ ist klein, denn unter $\varphi_\mathrm{s,WI}$ gilt $n_{p0}\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}<n_\mathrm i\ll N_\mathrm A$. Es bleibt $F=N_\mathrm A(\varphi_\mathrm s-V_\mathrm T)$. (b) Mit $F\approx N_\mathrm A\varphi_\mathrm s^2/(2V_\mathrm T)$ ist $|Q'|=\sqrt{e\varepsilon N_\mathrm A/V_\mathrm T}\,|\varphi_\mathrm s|$, die Steigung ist $C'_\mathrm{FB}$. Unter der Wurzel steht $e\varepsilon N_\mathrm A/V_\mathrm T=\varepsilon^2\cdot e^2N_\mathrm A/(\varepsilon k_\mathrm BT)=\varepsilon^2/L_\mathrm D^2$. (c) Bei $\varphi_\mathrm{s,SI}$ ist $n_{p0}\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}=N_\mathrm A$. Mit $\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}\approx0$ und $n_{p0}\ll N_\mathrm A$ sind $F=N_\mathrm A\varphi_\mathrm s$ und $\mathrm{d} F/\mathrm{d}\varphi_\mathrm s=2N_\mathrm A$. Wegen $C'_\mathrm{SC}=e\varepsilon(\mathrm{d} F/\mathrm{d}\varphi_\mathrm s)/\sqrt{2e\varepsilon F}$ folgt $C'_\mathrm{SC}=2\sqrt{e\varepsilon N_\mathrm A/(2\varphi_\mathrm s)}=2C'_\mathrm{depl}$.
:::
:::
