---
title: Stufe 3: Abschirmung und Akkumulation
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Die MOS-Kapazität
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat
knoten: Kapitel 15: Die MOS-Kapazität
order: 4250500
summary: Bei V mathrm G<0 zieht das Gate Löcher an die Grenzfläche.
tags: Debye-Länge, dielektrische Relaxationszeit
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bei $V_\mathrm G<0$ zieht das Gate Löcher an die Grenzfläche. Diese Stufe bestimmt, wie tief das Feld in den Halbleiter eindringt.
:::

**Die Idee.** Das Feld zieht Löcher zur Grenzfläche, ihre Ladung schwächt das Feld dahinter. Die Diffusion wirkt dem Anhäufen entgegen. Im Gleichgewicht heben sich Driftstrom und Diffusionsstrom an jedem Ort auf, und der Überschuss klingt ins Innere ab. Freie Ladungen schirmen also jede Potentialänderung exponentiell ab. Ein Metall tut das auf atomarer Länge, ein Halbleiter wegen seiner wenigen Träger auf vielen Nanometern.

:::satz Satz 3.1 (Debye-Länge)
<span class="anker" id="satz-3-1"></span>

Für eine schwache Störung $\Delta p=p-N_\mathrm A$ mit $|\Delta p|\ll N_\mathrm A$ gilt

<span class="anker" id="gl-3-1"></span>
$$\Delta p(x)=\Delta p(0)\,\mathrm{e}^{-x/L_\mathrm D},\qquad L_\mathrm D=\sqrt{\frac{\varepsilon D_p}{\sigma_p}}=\sqrt{D_p\tau_\varepsilon}=\sqrt{\frac{\varepsilon\,k_\mathrm BT}{e^2N_\mathrm A}}. \tag{3.1}$$
:::

⁠**So liest man das:** $L_\mathrm D$ ist die __Debye-Länge__ oder Abschirmlänge. $\sigma_p=eN_\mathrm A\mu_p$ ist die Leitfähigkeit, $D_p$ die Diffusionskonstante, $\tau_\varepsilon=\varepsilon/\sigma_p$ die __dielektrische Relaxationszeit__, in der ein Leiter eine Ladungsstörung ausgleicht. Für ein n-Substrat steht $N_\mathrm D$ statt $N_\mathrm A$. **Gültigkeit:** Nach [(2.3)](wie-sich-die-gatespannung-aufteilt.html#gl-2-3) ist $\Delta p(0)\approx-N_\mathrm A\varphi_\mathrm s/V_\mathrm T$, also verlangt die Formel $|\varphi_\mathrm s|\ll V_\mathrm T$. Das gilt für schwache Akkumulation ebenso wie für schwache Verarmung ($\Delta p<0$).

:::herleitung Aus der Löcherbilanz und der Poisson-Gleichung
Die Kontinuitätsgleichung mit Drift und Diffusion ([Kapitel 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html)) lautet

$$\frac{\partial p}{\partial t}=-\frac{\partial p}{\partial x}\mu_p\mathcal E-p\mu_p\frac{\partial\mathcal E}{\partial x}+D_p\frac{\partial^2p}{\partial x^2}+G_p-R_p.$$

Stationär ist $\partial p/\partial t=0$. Ohne Licht ist $G_p=R_p$. Mit $p=N_\mathrm A+\Delta p$ ist der erste Term rechts ein Produkt zweier kleiner Größen und fällt weg, im zweiten ist $p\approx N_\mathrm A$. Mit $\partial\mathcal E/\partial x=e\Delta p/\varepsilon$ aus [(0.3)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-3) bleibt

$$\frac{\sigma_p\,\Delta p}{\varepsilon}=D_p\frac{\partial^2\Delta p}{\partial x^2}.$$

Die abklingende Lösung ist [(3.1)](#gl-3-1). Die Einstein-Beziehung $D_p=\mu_pk_\mathrm BT/e$ liefert die letzte Form.
:::

:::abbildung gemb1/k15debye 3
Links: Überschuss im Rechenmodell. Die Tangente bei $x=0$ trifft die Achse bei $L_\mathrm D=23{,}6$ nm, dort ist noch der Anteil $1/\mathrm{e}$ übrig. Rechts: $L_\mathrm D$ in Silizium bei 300 K, rot das Rechenmodell.
:::

Integriert man die Überschussladung, folgt $|Q'_\mathrm{SC}|=e\,|\Delta p(0)|\,L_\mathrm D$, also

<span class="anker" id="gl-3-2"></span>
$$\Delta p(0)=\frac{Q'_\mathrm{SC}}{eL_\mathrm D},\qquad C'=\frac{|Q'_\mathrm{SC}|}{|\varphi_\mathrm s|}=\frac{\varepsilon}{L_\mathrm D}. \tag{3.2}$$

Die Randschicht wirkt wie ein Plattenkondensator der Dicke $L_\mathrm D$ in Reihe zum Isolator. Deshalb ist die Kapazität etwas kleiner als die des Isolators allein.

::::beispiel
Das Rechenmodell hat $L_\mathrm D=23{,}6$ nm. Nach 109 nm ist die Störung auf 1 % gefallen. Die Ladung $Q'_\mathrm{SC}=1\,\mathrm{nC/cm^2}$ ergibt $\Delta p(0)=2{,}6\cdot10^{15}\,\mathrm{cm^{-3}}$, das sind 8,8 % von $N_\mathrm A$, und $\varphi_\mathrm s=-2{,}3$ mV. In Silizium ist $L_\mathrm D=409$ nm, 41 nm und 4,1 nm für $N=10^{14}$, $10^{16}$ und $10^{18}\,\mathrm{cm^{-3}}$.
::::

⁠**Grenzfall:** Für $L_\mathrm D\to0$ wird die Halbleiterplatte zum Metall.

**Starke Akkumulation.** Bei $|\Delta p|\gtrsim N_\mathrm A$ ist die Leitfähigkeit nicht mehr konstant, und die Differentialgleichung wird nichtlinear. Nach [(2.3)](wie-sich-die-gatespannung-aufteilt.html#gl-2-3) wächst $p(0)$ um den Faktor 10 je 60 mV. Die Ladung drängt sich in eine Schicht dünner als $L_\mathrm D$, die Bänder biegen an der Grenzfläche scharf nach oben, und die Grenzschicht verhält sich quasi metallisch. Bei $\varphi_\mathrm s=-0{,}166$ V erreicht $E_\mathrm V$ im Rechenmodell $E_\mathrm F$, die Oberfläche ist entartet ([Kapitel 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html)). Deshalb bleibt $|\varphi_\mathrm s|$ klein, und fast die ganze Spannung liegt am Isolator:

<span class="anker" id="gl-3-3"></span>
$$V_\mathrm G=-\frac{Q'_\mathrm{SC}}{C'_\mathrm{IS}}+\varphi_\mathrm s\approx-\frac{Q'_\mathrm{SC}}{C'_\mathrm{IS}}. \tag{3.3}$$

Im Bänderdiagramm streben Elektronen im Leitungsband zu tiefer Energie, Löcher im Valenzband nach oben. Deshalb sammeln sich Löcher dort, wo die Bänder nach oben biegen. Die Struktur ähnelt einem Plattenkondensator aus Metall, Isolator und Metall. Bei $\varphi_\mathrm s=-0{,}15$ V, knapp vor dem Ende der Boltzmann-Näherung, ist $p(0)=9{,}9\cdot10^{18}\,\mathrm{cm^{-3}}$, die Ladung 289 nC/cm$^2$ und $V_\mathrm G=-1{,}82$ V. Am Halbleiter liegen nur 8 % der Spannung, die Schicht ist rund 2 nm dick. Für ein n-Substrat gilt dasselbe bei $V_\mathrm G>0$ mit Elektronen und Bändern, die nach unten biegen.

:::frage Warum kommt die Beweglichkeit in der Debye-Länge nicht vor?
Sie steckt in Drift und in Diffusion, und beide sind ihr proportional. Im Gleichgewicht zählt nur das Verhältnis der beiden Ströme, und da kürzt sie sich. Die Beweglichkeit bestimmt, wie schnell die Schicht entsteht, nicht wie sie am Ende aussieht.
:::

:::aufgabe Aufgabe 3 ★ Eindringtiefe abschätzen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Berechne $L_\mathrm D$ für $N_\mathrm A=10^{15}$ und $10^{17}\,\mathrm{cm^{-3}}$.

</li>

<li>

Ein Substrat mit $N_\mathrm A=10^{17}\,\mathrm{cm^{-3}}$ trägt $Q'_\mathrm{SC}=0{,}5\,\mathrm{nC/cm^2}$. Berechne $\Delta p(0)$ und $\varphi_\mathrm s$. Ist die Formel anwendbar?

</li>

<li>

Um wie viel Prozent liegt die Reihenschaltung aus $\varepsilon/L_\mathrm D$ und 50 nm $\mathrm{SiO_2}$ unter dem Wert des Isolators allein?

</li>

</ol>

:::loesung
(a) 129 nm und 12,9 nm. (b) $\Delta p(0)=Q'_\mathrm{SC}/(eL_\mathrm D)=2{,}4\cdot10^{15}\,\mathrm{cm^{-3}}$, das sind 2,4 % von $N_\mathrm A$, also ist die Formel anwendbar. $\varphi_\mathrm s=-V_\mathrm T\,\Delta p(0)/N_\mathrm A=-0{,}62$ mV. (c) $\varepsilon/L_\mathrm D=801$ nF/cm$^2$, $C'_\mathrm{IS}=69{,}1$ nF/cm$^2$, Reihenschaltung 63,6 nF/cm$^2$, also 7,9 % weniger.
:::
:::
