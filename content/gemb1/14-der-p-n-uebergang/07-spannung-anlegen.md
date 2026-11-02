---
title: Stufe 5: Spannung anlegen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der p-n-Übergang
order: 4240700
summary: Bisher lag keine äußere Spannung an.
tags: Durchlassrichtung, Sperrrichtung
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Bisher lag keine äußere Spannung an. Diese Stufe legt eine an. Sie zeigt, wie sich die Barriere verschiebt und warum eine einzige Fermi-Energie nicht mehr reicht.
:::

**Die Idee.** $U_\mathrm{pn}$ ist das Potential des p-Gebiets gegenüber dem n-Gebiet. Die Neutralgebiete leiten gut, die Zone enthält kaum Träger. Sie wirken wie kleine Widerstände in Reihe mit einem sehr großen: Fast die ganze Spannung fällt an der Zone ab. Das n-Gebiet bleibe fest. Bei __Durchlassrichtung__, $U_\mathrm{pn}>0$, sinkt die Energie der Elektronen im p-Gebiet um $eU_\mathrm{pn}$, die Barriere schrumpft. Bei __Sperrrichtung__, $U_\mathrm{pn}<0$, wächst sie (Abb. [5](#abb-5)).

Über die Zone laufen zwei gegenläufige Elektronenströme. **Diffusion:** Elektronen aus dem n-Gebiet müssen die Barriere hinauf. Ihr Anteil folgt dem Boltzmann-Faktor der Barrierenhöhe und ändert sich exponentiell mit ihr. **Drift:** Minoritätselektronen vom Rand im p-Gebiet fallen die Barriere hinab. Ihre Zahl hängt von der Höhe fast nicht ab. Ohne Spannung sind beide gleich. Bei Durchlass überwiegt die Diffusion, bei Sperrung bleibt nur die kleine Drift. Für Löcher gilt dasselbe in Gegenrichtung.

:::abbildung gemb1/k14spannung 5
Bänder bei $U_\mathrm{pn}=+0{,}4$ V, 0 und $-0{,}4$ V, n-Gebiet festgehalten, Schottky-Näherung. Orange: Barriere für Elektronen in eV. Grau: Zone. Blau und rot: Fermi-Energien der Elektronen und der Löcher, ihr Abstand ist $e|U_\mathrm{pn}|$. Bei Durchlass liegt $E_\mathrm{Fp}$ unter $E_\mathrm{Fn}$, bei Sperrung darüber.
:::

**Zwei Quasi-Fermi-Niveaus.** Eine Spannung ist eine Differenz von Fermi-Energien, also kann $E_\mathrm F$ nicht mehr überall gleich sein. Dafür hat [Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html) das Quasi-Fermi-Niveau eingeführt, das örtliche Fermi-Niveau außerhalb des Gleichgewichts. Hier reicht eines nicht mehr, denn Elektronen und Löcher sind nicht miteinander im Gleichgewicht. Unter sich sind sie es: Streuung stellt die Verteilung in jedem Band in rund 0,2 ps ein ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)), Rekombination braucht 1 µ s, das $5\cdot10^{6}$-fache. Jede Sorte bekommt deshalb ihr eigenes Niveau.

:::definition Definition 5.1 (Quasi-Fermi-Niveaus der beiden Sorten)
<span class="anker" id="satz-5-1"></span>

$E_\mathrm{Fn}(x)$ für Elektronen und $E_\mathrm{Fp}(x)$ für Löcher sind durch die wirklichen Dichten festgelegt:

<span class="anker" id="gl-5-1"></span>
$$n(x)=N_\mathrm C\exp\Bigl(-\frac{E_\mathrm C(x)-E_\mathrm{Fn}(x)}{k_\mathrm BT}\Bigr),\qquad p(x)=N_\mathrm V\exp\Bigl(-\frac{E_\mathrm{Fp}(x)-E_\mathrm V(x)}{k_\mathrm BT}\Bigr). \tag{5.1}$$

Daraus folgt $n\,p=n_\mathrm i^2\exp\bigl((E_\mathrm{Fn}-E_\mathrm{Fp})/(k_\mathrm BT)\bigr)$. Der Strom jeder Sorte ist $j_\mathrm n=\mu_\mathrm n\,n\,\mathrm{d} E_\mathrm{Fn}/\mathrm{d} x$ und $j_\mathrm p=\mu_\mathrm p\,p\,\mathrm{d} E_\mathrm{Fp}/\mathrm{d} x$.
:::

⁠**So liest man das:** Im Gleichgewicht ist $E_\mathrm{Fn}=E_\mathrm{Fp}=E_\mathrm F$ und $n\,p=n_\mathrm i^2$. Die Stromformeln folgen wie [(2.1)](der-ubergang-im-gleichgewicht.html#gl-2-1), denn die Rechnung benutzte nur die Dichte einer Sorte. Das Niveau einer Sorte ist flach, wo sie viele Träger hat: Dort reicht für jeden Strom ein kleines Gefälle. Ein Beispiel ohne Spannung ist Licht: Es hebt Elektronen aus dem Valenz- ins Leitungsband, und beide Niveaus trennen sich. Bei schwacher Injektion ([Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html)) bleiben die Minoritäten viel seltener als die Majoritäten. Dann behält das Niveau der Majoritäten seine Lage, nur das der Minoritäten wandert. Bei starker Injektion erreicht die Minoritätsdichte die Majoritätsdichte, und beide Niveaus bewegen sich.

:::satz Satz 5.2 (Übergang mit Spannung)
<span class="anker" id="satz-5-2"></span>

$E_\mathrm{Fn}$ kommt flach aus dem n-Gebiet, $E_\mathrm{Fp}$ flach aus dem p-Gebiet. In der Zone gilt deshalb

<span class="anker" id="gl-5-2"></span>
$$E_\mathrm{Fn}-E_\mathrm{Fp}=eU_\mathrm{pn},\qquad\Phi_\mathrm{bi}\to\Phi_\mathrm{bi}-eU_\mathrm{pn}. \tag{5.2}$$

Die Weiten [(4.3)](feld-potential-und-weite-der-zone.html#gl-4-3) bleiben gültig, wenn dort $\Phi_\mathrm{bi}-eU_\mathrm{pn}$ statt $\Phi_\mathrm{bi}$ steht.
:::

⁠**Gültigkeit:** $U_\mathrm{pn}<U_\mathrm d$, schwache Injektion, kleiner Strom, sonst fällt auch in den Neutralgebieten Spannung ab. Die zweite Gleichung liest man in Abb. [5](#abb-5) ab: Der Abstand von Bandkante zu Niveau bleibt in beiden Neutralgebieten gleich, also verschiebt sich die p-Seite samt Bändern um $-eU_\mathrm{pn}$.

**Beispiel.** Mit $U_\mathrm d=0{,}762$ V folgt:

| $U_\mathrm{pn}$ | $+0{,}4$ V | 0 | $-0{,}4$ V | $-5$ V |
|---|---|---|---|---|
| Barriere $\Phi_\mathrm{bi}-eU_\mathrm{pn}$ | 0,362 eV | 0,762 eV | 1,162 eV | 5,762 eV |
| $L_\mathrm{depl}$ | 237 nm | 344 nm | 425 nm | 946 nm |
| $\vert \mathcal E_\mathrm{max}\vert $ | 3,06 MV/m | 4,43 MV/m | 5,47 MV/m | 12,2 MV/m |

Der Boltzmann-Faktor der Barriere ist bei +0,4 V $5{,}2\cdot10^{6}$-mal größer als bei 0 V. **Grenzfälle:** Für $U_\mathrm{pn}\to U_\mathrm d$ werden die Bänder flach, $L_\mathrm{depl}\to0$ und $E_\mathrm{Fn}-E_\mathrm{Fp}=\Phi_\mathrm{bi}$, genau wie bei den getrennten Stücken in Abb. [2](der-ubergang-im-gleichgewicht.html#abb-2). Für große Sperrspannung ist $L_\mathrm{depl}\propto\sqrt{|U_\mathrm{pn}|}$.

:::frage Pluspol am p-Gebiet: Warum liegt $E_\mathrm{Fp}$ dann *unten*?
Weil die Achse die Energie von Elektronen zeigt. Positives Potential bedeutet $-e\varphi<0$. Das p-Gebiet rutscht im Bild mit allen Niveaus nach unten, genau dadurch sinkt die Barriere. Bei Sperrung rutscht es nach oben.
:::

:::aufgabe Aufgabe 6 ★★ Zone unter Spannung
<span class="anker" id="aufg-6"></span>

Rechenmodell.

<ol class="al">

<li>

Berechne $L_\mathrm{depl}^\mathrm A$, $L_\mathrm{depl}^\mathrm D$ und $|\mathcal E_\mathrm{max}|$ für $U_\mathrm{pn}=+0{,}5$ V, $-2$ V und $-20$ V.

</li>

<li>

Bei welchem $U_\mathrm{pn}$ ist die Zone doppelt so breit wie bei 0 V?

</li>

<li>

Welche Spannung macht die Bänder flach? Was gilt dann für $E_\mathrm{Fn}$ und $E_\mathrm{Fp}$?

</li>

<li>

Zeichne das Bänderdiagramm für $U_\mathrm{pn}<0$ mit $E_\mathrm{Fn}$, $E_\mathrm{Fp}$ und der Barriere.

</li>

</ol>

:::loesung
(a) $+0{,}5$ V: 33,6 nm, 168 nm, 2,60 MV/m. $-2$ V: 109 nm, 546 nm, 8,44 MV/m. $-20$ V: 299 nm, 1496 nm, 23,1 MV/m. (b) $L_\mathrm{depl}\propto\sqrt{U_\mathrm d-U_\mathrm{pn}}$. Doppelt so breit heißt $U_\mathrm d-U_\mathrm{pn}=4U_\mathrm d$, also $U_\mathrm{pn}=-3U_\mathrm d=-2{,}29$ V. (c) $U_\mathrm{pn}=U_\mathrm d=0{,}762$ V. Dann ist $E_\mathrm{Fn}-E_\mathrm{Fp}=\Phi_\mathrm{bi}$ wie bei den getrennten Stücken. (d) Wie Abb. [5](#abb-5) rechts: $E_\mathrm{Fp}$ liegt um $e|U_\mathrm{pn}|$ über $E_\mathrm{Fn}$, die Barriere ist $\Phi_\mathrm{bi}+e|U_\mathrm{pn}|$.
:::
:::

:::aufgabe Aufgabe 7 ★★ Beleuchtetes Silizium
<span class="anker" id="aufg-7"></span>

Ein n-Stück mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ wird beleuchtet, das Licht erzeugt gleichmäßig $\Delta n=\Delta p$ zusätzlich.

<ol class="al">

<li>

Berechne für $\Delta n=10^{13}\,\mathrm{cm^{-3}}$ die Abstände $E_\mathrm C-E_\mathrm{Fn}$ und $E_\mathrm{Fp}-E_\mathrm V$ sowie $E_\mathrm{Fn}-E_\mathrm{Fp}$.

</li>

<li>

Dasselbe für $\Delta n=10^{17}\,\mathrm{cm^{-3}}$.

</li>

<li>

Welches Niveau bewegt sich jeweils, und um wie viel? Welcher Fall ist schwache, welcher starke Injektion?

</li>

</ol>

:::loesung
Im Dunkeln ist $E_\mathrm C-E_\mathrm F=205{,}4$ meV und $E_\mathrm F-E_\mathrm V=914{,}6$ meV. (a) $n=1{,}001\cdot10^{16}\,\mathrm{cm^{-3}}$, $p=10^{13}\,\mathrm{cm^{-3}}$: $E_\mathrm C-E_\mathrm{Fn}=205{,}4$ meV, $E_\mathrm{Fp}-E_\mathrm V=372{,}8$ meV, $E_\mathrm{Fn}-E_\mathrm{Fp}=541{,}9$ meV. (b) $n=1{,}1\cdot10^{17}\,\mathrm{cm^{-3}}$, $p=10^{17}\,\mathrm{cm^{-3}}$: 143,4 meV, 134,7 meV, 841,9 meV. (c) Im ersten Fall ändert sich $E_\mathrm{Fn}$ nur um 0,03 meV, $E_\mathrm{Fp}$ rückt um 542 meV nach unten: schwache Injektion. Im zweiten Fall ist $p>N_\mathrm D$: starke Injektion, $E_\mathrm{Fn}$ steigt um 62 meV, $E_\mathrm{Fp}$ sinkt um 780 meV.
:::
:::
