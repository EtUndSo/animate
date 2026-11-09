---
title: Stufe 5: Kennlinien bei niedriger und hoher Frequenz
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260700
summary: Kapazität misst man mit einer kleinen Wechselspannung.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Kapazität misst man mit einer kleinen Wechselspannung. Diese Stufe zeigt, dass das Ergebnis davon abhängt, welche Ladungen dem Signal folgen können.
:::

**Die Idee.** Zur Gleichspannung $V_\mathrm G$ kommt ein kleines Signal, hier 10 mV. Die Kapazität ist die Wechselladung je Signalspannung. Drei Sorten Ladung können antworten. Löcher sind Majoritätsträger, gleichen Störungen in $\tau_\varepsilon=0{,}5$ ps aus ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html)) und folgen immer, in Akkumulation an der Grenzfläche, sonst am Zonenrand. Die Elektronen der Inversionsschicht sind Minoritätsträger: Sie müssen thermisch erzeugt werden oder durch Diffusion nachkommen. Interfacezustände müssen Ladungsträger aus den Bändern einfangen. Bei niedriger Frequenz antwortet alles, bei hoher nur die Löcher. In Inversion liegt die Wechselladung dann am Zonenrand, und die Kapazität bleibt klein (Abb. [5](#abb-5)).

:::satz Satz 5.1 (Kapazität bei niedriger und hoher Frequenz)
<span class="anker" id="satz-5-1"></span>

Bei niedriger Frequenz oder quasi-statischer Messung gilt [(4.3)](interfacezustande.html#gl-4-3), in Verarmung also

<span class="anker" id="gl-5-1"></span>
$$C'_\mathrm{nf}=\frac{C'_\mathrm{IS}\bigl(C'_\mathrm{depl}+C'_\mathrm{it}\bigr)}{C'_\mathrm{IS}+C'_\mathrm{depl}+C'_\mathrm{it}}. \tag{5.1}$$

Bei hoher Frequenz folgt nur die Verarmungsladung:

<span class="anker" id="gl-5-2"></span>
$$C'_\mathrm{hf}=\frac{C'_\mathrm{IS}C'_\mathrm{depl}}{C'_\mathrm{IS}+C'_\mathrm{depl}},\qquad C'_\mathrm{depl}=\frac{\varepsilon}{L_\mathrm{depl}},\qquad C'_\mathrm{min}=\frac{C'_\mathrm{IS}}{1+C'_\mathrm{IS}L_\mathrm{depl,max}/\varepsilon}. \tag{5.2}$$
:::

⁠**So liest man das:** Oberhalb von $V_\mathrm{th}$ hält die Inversionsschicht die Zone bei $L_\mathrm{depl,max}$ fest, das ergibt das Plateau $C'_\mathrm{min}$. Zwischen beiden Grenzen folgt mit steigender Frequenz ein immer kleinerer Teil der Elektronen. Beim n-Substrat läuft die Kurve gespiegelt, mit Akkumulation rechts von $V_\mathrm{FB}$ und Inversion links von $V_\mathrm{th}<V_\mathrm{FB}$. **Gültigkeit:** Die Gleichspannung ändert sich so langsam, dass die Inversionsschicht im Gleichgewicht ist.

:::abbildung gemb1/k16kennlinie 5
Kennlinien des Rechenmodells, exakt gerechnet. Oben ohne Interfacezustände: Beide Kurven trennen sich erst in Inversion. Unten mit $D_\mathrm{it}=5\cdot10^{11}/(\mathrm{eV\,cm^2})$, grau zum Vergleich die Kurven von oben: Die Interfacezustände dehnen die Kurven, $V_\mathrm{th}$ rückt nach rechts, und in Verarmung liegt die Kurve niedriger Frequenz um den Beitrag von $C'_\mathrm{it}$ höher.
:::

**Die Zeiten.** Paare entstehen in der Zone mit der Stromdichte $j_\mathrm{gen}=e\,n_\mathrm iL_\mathrm{depl}/(2\tau_\text{rec})$ ([Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html)). Mit $\tau_\text{rec}=1$ µ s und $L_\mathrm{depl,max}$ sind das $1{,}3\cdot10^{-8}\,\mathrm{A/cm^2}$. Ein Signal von $\pm10$ mV verlangt in Inversion je Halbperiode die Ladung $2C'_\mathrm{IS}\cdot10\,\mathrm{mV}=3{,}5\,\mathrm{nC/cm^2}$. Das dauert 0,27 s, die Elektronen folgen also nur unterhalb von rund 2 Hz. Bei 1 MHz liefert die Erzeugung nur das $2\cdot10^{-6}$-Fache des Nötigen. Interfacezustände fangen Löcher in der Zeit $1/(\sigma vp(0))$ ein. Mit dem Einfangquerschnitt $\sigma=10^{-15}\,\mathrm{cm^2}$ und $v=10^{7}$ cm/s sind es 0,16 µ s bei $\varphi_\mathrm s=0{,}1$ V und 0,37 ms bei 0,3 V. Bei 1 MHz folgen sie in fast der ganzen Verarmung nicht.

::::beispiel
Ohne Zustände hat $C'_\mathrm{nf}$ das Minimum 46,2 nF/cm$^2$ bei $\varphi_\mathrm s=0{,}68$ V. Das Plateau ist $C'_\mathrm{min}=42{,}6\,\mathrm{nF/cm^2}$, das 0,247-Fache von $C'_\mathrm{IS}$. Die genaue Rechnung liegt wegen der weichen Zonenkante rund 5 % tiefer. Stärkere Dotierung macht die Zone schmaler und hebt das Plateau: Bei 20 nm Oxid ergeben $N_\mathrm A=10^{15}$, $10^{16}$ und $10^{17}\,\mathrm{cm^{-3}}$ die Werte 11,0, 28,4 und 63,1 nF/cm$^2$.

| $\varphi_\mathrm s$ in V | $-0{,}15$ | 0 | 0,1 | 0,3 | 0,6 | 0,777 | 0,9 |
|---|---|---|---|---|---|---|---|
| $V_\mathrm G$ in V | $-2{,}79$ | $-0{,}96$ | $-0{,}71$ | $-0{,}36$ | 0,07 | 0,32 | 1,07 |
| $C'_\mathrm{nf}/C'_\mathrm{IS}$ | 0,971 | 0,718 | 0,509 | 0,356 | 0,276 | 0,396 | 0,945 |
| $C'_\mathrm{hf}/C'_\mathrm{IS}$ | 0,971 | 0,718 | 0,509 | 0,356 | 0,276 | 0,250 | 0,236 |
| $V_\mathrm G$ in V, mit $D_\mathrm{it}$ | $-2{,}86$ | $-0{,}96$ | $-0{,}66$ | $-0{,}22$ | 0,35 | 0,68 | 1,49 |
| $C'_\mathrm{nf}/C'_\mathrm{IS}$, mit $D_\mathrm{it}$ | 0,971 | 0,750 | 0,600 | 0,504 | 0,458 | 0,528 | 0,946 |
::::

**Die Formeln je Bereich.** Allgemein ist mit $F$ aus [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html) $C'_\mathrm{SC}=e\varepsilon\,|\mathrm{d} F/\mathrm{d}\varphi_\mathrm s|/\sqrt{2e\varepsilon F}$, ausgeschrieben

<span class="anker" id="gl-5-3"></span>
$$C'_\mathrm{SC}=\frac{e\varepsilon\,\bigl|N_\mathrm A\bigl(1-\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}\bigr)-n_{p0}\bigl(1-\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}\bigr)\bigr|}{\sqrt{2e\varepsilon\bigl[N_\mathrm A\bigl(\varphi_\mathrm s+V_\mathrm T\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}-V_\mathrm T\bigr)-n_{p0}\bigl(\varphi_\mathrm s-V_\mathrm T\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}+V_\mathrm T\bigr)\bigr]}}. \tag{5.3}$$

Bei $\varphi_\mathrm s=0$ steht dort 0/0, die Regel von de L'Hospital gibt $C'_\mathrm{FB}$. In jedem Bereich überwiegt ein Term. Im n-Substrat ist $p_{n0}=n_\mathrm i^2/N_\mathrm D$, und $\varphi_\mathrm s$ wechselt das Vorzeichen.

| Bereich | $C'_\mathrm{SC}$, p-Substrat | $C'_\mathrm{SC}$, n-Substrat |
|---|---|---|
| Akkumulation | $\sqrt{\frac{e\varepsilon N_\mathrm A}{2V_\mathrm T}}\,\frac{\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}}{\sqrt{\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}-1}}$ | $\sqrt{\frac{e\varepsilon N_\mathrm D}{2V_\mathrm T}}\,\frac{\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}}{\sqrt{\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}-1}}$ |
| Flachband | $\sqrt{\frac{e\varepsilon}{V_\mathrm T}(n_{p0}+N_\mathrm A)}$ | $\sqrt{\frac{e\varepsilon}{V_\mathrm T}(p_{n0}+N_\mathrm D)}$ |
| Verarmung | $\sqrt{\frac{e\varepsilon N_\mathrm A}{2\varphi_\mathrm s}}$ | $\sqrt{\frac{e\varepsilon N_\mathrm D}{2\vert \varphi_\mathrm s\vert }}$ |
| starke Inversion | $\sqrt{\frac{e\varepsilon}{2}}\,\frac{n_{p0}\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}+N_\mathrm A}{\sqrt{n_{p0}V_\mathrm T(\mathrm{e}^{\varphi_\mathrm s/V_\mathrm T}-1)+\varphi_\mathrm sN_\mathrm A}}$ | $\sqrt{\frac{e\varepsilon}{2}}\,\frac{p_{n0}\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}+N_\mathrm D}{\sqrt{p_{n0}V_\mathrm T(\mathrm{e}^{-\varphi_\mathrm s/V_\mathrm T}-1)+\vert \varphi_\mathrm s\vert N_\mathrm D}}$ |

Nahe $\varphi_\mathrm{s,SI}$ rechnet man besser mit der Formel der starken Inversion. **Grenzfall:** In starker Akkumulation und starker Inversion ist $C'_\mathrm{SC}\gg C'_\mathrm{IS}$, also $C'_\mathrm{ges}=C'_\mathrm{IS}/(1+C'_\mathrm{IS}/C'_\mathrm{SC})\approx C'_\mathrm{IS}$.

:::frage In Inversion sind die Elektronen doch da. Warum misst man bei hoher Frequenz nicht $C'_\mathrm{IS}$?
Sie sind da, denn die Gleichspannung war langsam genug, um sie zu erzeugen. Ihre Zahl ändert sich aber nicht im Takt des Signals. Kapazität misst die Änderung. Die Wechselladung muss von Löchern am Zonenrand kommen, und der liegt $L_\mathrm{depl,max}$ hinter dem Isolator. Liefert ein benachbartes n-Gebiet Elektronen seitlich nach, misst man auch bei hoher Frequenz $C'_\mathrm{IS}$.
:::

:::aufgabe Aufgabe 7 ★★ Eine Kennlinie als Wertetabelle
<span class="anker" id="aufg-7"></span>

Ein n-Substrat mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ trägt 40 nm $\mathrm{SiO_2}$ auf 1 mm$^2$. Rechne ohne Interfacezustände bei niedriger Frequenz.

<ol class="al">

<li>

Berechne $C'_\mathrm{IS}$, $\varphi_\mathrm{s,WI}$ und $\varphi_\mathrm{s,SI}$.

</li>

<li>

Berechne $C$ in pF bei $\varphi_\mathrm s=+0{,}2$ V, 0, $-0{,}1$, $-0{,}3$, $-0{,}5$ V und $\varphi_\mathrm{s,SI}$.

</li>

<li>

Wie groß ist das Plateau bei hoher Frequenz in pF? Skizziere beide Kurven über $V_\mathrm G$ für $V_\mathrm{FB}=0$.

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=86{,}3\,\mathrm{nF/cm^2}$, also 863 pF. $\varphi_\mathrm{s,WI}=-0{,}360$ V, $\varphi_\mathrm{s,SI}=-0{,}720$ V. (b) $+0{,}2$ V ist Akkumulation mit $C'_\mathrm{SC}=8587\,\mathrm{nF/cm^2}$: 855 pF. Bei 0 ist $C'_\mathrm{FB}=253{,}4\,\mathrm{nF/cm^2}$: 644 pF. $-0{,}1$ V: 443 pF, $-0{,}3$ V: 327 pF, $-0{,}5$ V: 277 pF. Bei $\varphi_\mathrm{s,SI}$ ist $C'_\mathrm{SC}=2C'_\mathrm{depl}=67{,}9\,\mathrm{nF/cm^2}$: 380 pF. (c) $L_\mathrm{depl,max}=305$ nm, Plateau 244 pF. Die Akkumulation liegt rechts, die Inversion links.
:::
:::
