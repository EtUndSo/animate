---
title: Stufe 1: Verschiedene Austrittsarbeiten
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260300
summary: Aluminium und p-Silizium haben nicht dieselbe Austrittsarbeit.
tags: 
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Aluminium und p-Silizium haben nicht dieselbe Austrittsarbeit. Diese Stufe zeigt, warum die Bänder deshalb schon ohne Spannung verbogen sind und welche Spannung sie wieder flach macht.
:::

**Die Idee.** Vor dem Kontakt liegt $E_\mathrm F$ im Aluminium 0,90 eV höher als im Silizium (Abb. [1](#abb-1), links). Verbindet man Gate und Rückseite mit einem Draht, fließen Elektronen vom Metall durch den Draht ins Substrat, bis $E_\mathrm F$ überall gleich hoch liegt. Durch den Isolator kommen sie nicht. Das Gate bleibt positiv geladen zurück. An der Rückseite rekombinieren die Elektronen mit Löchern. Das zieht Löcher von der Grenzfläche ab, und dort bleibt eine Verarmungszone aus Akzeptorionen. Zwischen beiden Ladungen herrscht ein Feld wie im geladenen Kondensator. Es verbiegt die Bänder, ohne dass eine Spannung von außen anliegt.

:::abbildung gemb1/k16austritt 1
Rechenmodell ohne Ladungen im Isolator, Energien maßstäblich. Links: Vor dem Kontakt ist $E_\mathrm{vac}$ gemeinsam. Rechts: Nach dem Kontakt bei $V_\mathrm G=0$ ist $E_\mathrm F$ gemeinsam (rot), $E_\mathrm{vac}$ fällt zum Metall um 0,90 eV. Das teilt sich auf den Isolator ($eV_\mathrm{IS,0}$) und die orange Verarmungszone ($e\varphi_\mathrm{s0}$) auf.
:::

:::definition Definition 1.1 (Austrittsarbeitsdifferenz)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
$$\Delta\Phi=\Phi_\mathrm M-\Phi_\mathrm{SC}=\Phi_\mathrm M-\Bigl(\chi_\mathrm{SC}+\frac{E_\mathrm g}{2}+\bigl(E_\mathrm{Fi,\infty}-E_\mathrm F\bigr)\Bigr). \tag{1.1}$$
:::

⁠**So liest man das:** $\Delta\Phi$ ist eine Energie in eV, typisch zwischen $-1$ und $+1$ eV. $\Phi_\mathrm M$ legt das Metall fest, $\chi_\mathrm{SC}$ und $E_\mathrm g$ der Halbleiter, die Klammer $E_\mathrm{Fi,\infty}-E_\mathrm F$ die Dotierung. Der Isolator kommt nicht vor: $\Delta\Phi$ hängt nicht von seinen Eigenschaften ab.

:::satz Satz 1.2 (Bilanz mit Austrittsarbeitsdifferenz)
<span class="anker" id="satz-1-2"></span>

Ohne Ladungen im Isolator gilt

<span class="anker" id="gl-1-2"></span>
$$V_\mathrm G=\frac{\Delta\Phi}{e}+V_\mathrm{IS}+\varphi_\mathrm s,\qquad V_\mathrm{FB}=\frac{\Delta\Phi}{e},\qquad-\frac{\Delta\Phi}{e}=V_\mathrm{IS,0}+\varphi_\mathrm{s0}. \tag{1.2}$$
:::

⁠**So liest man das:** $V_\mathrm{FB}$ ist die Flachbandspannung in V. $V_\mathrm{IS,0}$ und $\varphi_\mathrm{s0}$ sind die Werte bei $V_\mathrm G=0$. Die letzte Gleichung sagt: Ohne äußere Spannung liegt $-\Delta\Phi/e$ innen. **Gültigkeit:** kein Strom durch den Isolator, Gleichgewicht.

:::herleitung Das Vakuumniveau einmal durch die Struktur
Tief im Substrat liegt $E_\mathrm{vac}$ bei $E_\mathrm F+\Phi_\mathrm{SC}$. Bis zur Grenzfläche sinkt es um $e\varphi_\mathrm s$, über dem Isolator um $eV_\mathrm{IS}$. Am Gate muss es bei $E_\mathrm{F,M}+\Phi_\mathrm M$ ankommen:

$$E_\mathrm F+\Phi_\mathrm{SC}-e\varphi_\mathrm s-eV_\mathrm{IS}=E_\mathrm{F,M}+\Phi_\mathrm M.$$

Mit $E_\mathrm F-E_\mathrm{F,M}=eV_\mathrm G$ folgt die Bilanz. Bei $V_\mathrm G=\Delta\Phi/e$ erfüllen $\varphi_\mathrm s=0$ und $V_\mathrm{IS}=0$ die Gleichung: keine Ladung, flache Bänder.
:::

Das Vorzeichen von $V_\mathrm{FB}$ verrät den Zustand bei $V_\mathrm G=0$, denn $V_\mathrm{FB}$ macht ihn rückgängig. Ein p-Substrat in Akkumulation hat nach oben gebogene Bänder, flach werden sie mit positiver Gatespannung. Akkumulation bedeutet also $V_\mathrm{FB}>0$ im p-Substrat und $V_\mathrm{FB}<0$ im n-Substrat, Verarmung oder Inversion bedeutet $V_\mathrm{FB}<0$ im p-Substrat und $V_\mathrm{FB}>0$ im n-Substrat.

::::beispiel
Im Rechenmodell ist $\Delta\Phi=4{,}10\,\mathrm{eV}-5{,}00\,\mathrm{eV}=-0{,}90$ eV, genauer $-0{,}899$ eV. Bei $V_\mathrm G=0$ liegen 0,899 V innen. Mit der Ladung der Verarmung gilt $0{,}899\,\mathrm{V}=\varphi_\mathrm{s0}+\gamma\sqrt{\varphi_\mathrm{s0}}$, also $\sqrt{\varphi_\mathrm{s0}}=-\gamma/2+\sqrt{\gamma^2/4+0{,}899\,\mathrm{V}}$. Das ergibt $\varphi_\mathrm{s0}=0{,}493$ V und $V_\mathrm{IS,0}=0{,}406$ V, also 55 % im Halbleiter. Die Zone ist 146 nm breit, die Ladung beträgt $Q'_\mathrm{SC}=-70{,}1\,\mathrm{nC/cm^2}$. Wegen $\varphi_\mathrm{s0}>\varphi_\mathrm{s,WI}$ ist die Oberfläche schon schwach invertiert. Die exakte Ladung aus [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html) ergibt 0,50 V.
::::

⁠**Grenzfälle:** $\Delta\Phi=0$ gibt den idealen Kondensator. Je dünner der Isolator, desto mehr liegt im Halbleiter: 94 % bei 2 nm, 3 % bei 200 nm. Ein Metall mit $\Phi_\mathrm M=5{,}15$ eV ergäbe $V_\mathrm{FB}=+0{,}15$ V und Akkumulation ohne Spannung.

:::frage Innen liegen 0,9 V. Kann ich die mit einem Voltmeter zwischen Gate und Substrat messen?
Nein. Ein Voltmeter misst die Differenz der Fermi-Niveaus an seinen Klemmen, und die ist null. Die 0,9 V sind der Abfall des elektrostatischen Potentials im Inneren. Er gleicht den Unterschied der Austrittsarbeiten gerade aus, deshalb fließt kein Strom.
:::

:::aufgabe Aufgabe 1 ★ Flachbandspannung vorhersagen
<span class="anker" id="aufg-1"></span>

Ein Gate hat $\Phi_\mathrm M=4{,}70$ eV, im Isolator sitzt keine Ladung.

<ol class="al">

<li>

Berechne $\Delta\Phi$ und $V_\mathrm{FB}$ auf p-Silizium mit $N_\mathrm A=10^{17}\,\mathrm{cm^{-3}}$ und auf n-Silizium mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$.

</li>

<li>

Welcher Zustand liegt jeweils bei $V_\mathrm G=0$ vor?

</li>

<li>

Bei welchem $N_\mathrm A$ wäre dieses Metall für p-Silizium ideal?

</li>

</ol>

:::loesung
(a) p-Silizium: $E_\mathrm{Fi,\infty}-E_\mathrm F=0{,}420$ eV, $\Phi_\mathrm{SC}=5{,}03$ eV, $\Delta\Phi=-0{,}33$ eV, $V_\mathrm{FB}=-0{,}33$ V. n-Silizium: Die Klammer ist $-0{,}360$ eV, $\Phi_\mathrm{SC}=4{,}25$ eV, $V_\mathrm{FB}=+0{,}45$ V. (b) Beide Male Verarmung oder Inversion. (c) $\Delta\Phi=0$ verlangt $E_\mathrm{Fi,\infty}-E_\mathrm F=0{,}09$ eV, also $N_\mathrm A=n_\mathrm i\,\mathrm{e}^{0{,}09/0{,}02585}=2{,}9\cdot10^{11}\,\mathrm{cm^{-3}}$.
:::
:::

:::aufgabe Aufgabe 2 ★★ Die Differenz teilt sich auf
<span class="anker" id="aufg-2"></span>

Ein n-Substrat mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ trägt 20 nm $\mathrm{SiO_2}$ und ein Gate mit $\Phi_\mathrm M=4{,}80$ eV. Die Fläche ist 1 mm$^2$, der Isolator ist frei von Ladungen.

<ol class="al">

<li>

Berechne $\Phi_\mathrm{SC}$, $\Delta\Phi$ und $V_\mathrm{FB}$.

</li>

<li>

Stelle die Bilanz bei $V_\mathrm G=0$ auf. Beachte, dass beim n-Substrat in Verarmung $\varphi_\mathrm s<0$ und $Q'_\mathrm{SC}=+\sqrt{2\varepsilon eN_\mathrm D|\varphi_\mathrm s|}$ ist. Berechne $\varphi_\mathrm{s0}$, $V_\mathrm{IS,0}$ und $L_\mathrm{depl}$.

</li>

<li>

Liegt noch Verarmung vor? Wie groß ist die Kapazität $C$ in pF?

</li>

</ol>

:::loesung
(a) $\Phi_\mathrm{SC}=4{,}25$ eV, $\Delta\Phi=+0{,}55$ eV, $V_\mathrm{FB}=+0{,}55$ V. (b) $0=0{,}55\,\mathrm{V}+V_\mathrm{IS,0}+\varphi_\mathrm{s0}$ mit $V_\mathrm{IS,0}=-\gamma\sqrt{|\varphi_\mathrm{s0}|}$ und $\gamma=0{,}334\,\sqrt{\mathrm V}$. Das ergibt $\sqrt{|\varphi_\mathrm{s0}|}=-0{,}167+\sqrt{0{,}0278+0{,}55}=0{,}593$, also $\varphi_\mathrm{s0}=-0{,}352$ V, $V_\mathrm{IS,0}=-0{,}198$ V, $L_\mathrm{depl}=213$ nm. (c) Wegen $|\varphi_\mathrm{s0}|<0{,}360$ V liegt knapp Verarmung vor. Mit $C'_\mathrm{depl}=48{,}6\,\mathrm{nF/cm^2}$ ist $C=379$ pF.
:::
:::
