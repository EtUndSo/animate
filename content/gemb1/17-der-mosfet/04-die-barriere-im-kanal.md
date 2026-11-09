---
title: Stufe 2: Die Barriere im Kanal
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270400
summary: Stufe 1 beschreibt den Kanal als Schicht.
tags: Spitze der Barriere
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Stufe [1](zwei-kontakte-am-mos-kondensator.html#stufe-1) beschreibt den Kanal als Schicht. Diese Stufe zeigt, welche Energien ein Elektron auf dem Weg durch ihn sieht und wie das Gate darauf wirkt.
:::

**Die Idee.** Längs der Oberfläche trifft ein Elektron aus der Source zuerst auf einen p-n-Übergang. Die Diffusionsspannung scheint also die Barriere festzulegen. Das stimmt nur zum Teil, denn über dem p-Gebiet liegt das Gate. Es biegt die Bänder an der Oberfläche um $\varphi_\mathrm s$ nach unten und senkt so die Barriere (Abb. [2](#abb-2), links). Anders als in der Diode liegt keine Spannung zwischen Source und p-Gebiet, die Quasi-Fermi-Niveaus von Elektronen und Löchern trennen sich dort also nicht. Das Leitungsband verschiebt allein die Spannung an der isolierten Elektrode.

:::satz Satz 2.1 (Barriere über dem Kanal)
<span class="anker" id="satz-2-1"></span>

Die Elektronen der Source sehen die Barriere $E_\mathrm b$, und an ihrer Spitze ist die Dichte $n(0)$:

<span class="anker" id="gl-2-1"></span>
$$E_\mathrm b=\Phi_\mathrm{bi}-e\varphi_\mathrm s,\qquad n(0)=N_\mathrm D\exp\Bigl(-\frac{E_\mathrm b}{k_\mathrm BT}\Bigr)=n_{p0}\exp\Bigl(\frac{\varphi_\mathrm s}{V_\mathrm T}\Bigr). \tag{2.1}$$
:::

⁠**So liest man das:** $E_\mathrm b$ zählt von der Bandkante in der Source bis zur Spitze, in eV. $N_\mathrm D$ ist die Dotierung der Source. Die erste Form von $n(0)$ zählt Elektronen von der Source aus mit dem Boltzmann-Faktor, die zweite ist [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2). **Gültigkeit:** Boltzmann-Näherung in der Source, im Rechenmodell liegt $E_\mathrm F$ dort 45 meV unter $E_\mathrm C$, das sind $1{,}7\,k_\mathrm BT$ und damit eine grobe Näherung. Außerdem muss das Gate die Spitze allein bestimmen.

:::herleitung Beide Formen stimmen überein
Aus $\Phi_\mathrm{bi}=k_\mathrm BT\ln(N_\mathrm AN_\mathrm D/n_\mathrm i^2)$ folgt $N_\mathrm D\exp(-\Phi_\mathrm{bi}/(k_\mathrm BT))=n_\mathrm i^2/N_\mathrm A=n_{p0}$. Einsetzen von $E_\mathrm b$ ergibt die zweite Form.
:::

:::abbildung gemb1/k17barriere 2
Leitungsbandkante $E_\mathrm C$ längs der Oberfläche des Rechenmodells, Energien maßstäblich, Profil längs $y$ schematisch. Links $V_\mathrm{DS}=0$: Das Gate senkt die Barriere. Rechts $V_\mathrm{GS}=V_\mathrm{th}$ und $V_\mathrm{DS}=1$ V. Oben die Zustände $E(k_y)$ an der Spitze: Rot die von der Source besetzte Hälfte $k_y>0$, orange die vom Drain besetzte Hälfte $k_y<0$.
:::

**Erst Diffusion, dann Drift.** Am höchsten Punkt, der __Spitze der Barriere__ (englisch top of the barrier), ist $E_\mathrm C$ waagerecht. Dort ist $\mathcal E_y=0$, und es gibt keine Drift. Davor bremst das Feld die Elektronen sogar, es treibt sie nur das Dichtegefälle: Die Source injiziert sie durch Diffusion. Hinter der Spitze fällt $E_\mathrm C$ zum Drain ab, sobald $V_\mathrm{DS}>0$ ist. Aus dem Diffusionsstrom wird ein Driftstrom.

**Warum es ohne Drainspannung keinen Strom gibt.** Der Strom ist die Summe aus Geschwindigkeit mal Besetzung über alle Zustände ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)). An der Spitze laufen Zustände mit $k_y>0$ zum Drain, solche mit $k_y<0$ zur Source. Die ersten füllt die Source, die zweiten der Drain. Bei $V_\mathrm{DS}=0$ sind beide Hälften gleich besetzt, die Summe ist null, obwohl Elektronen da sind. $V_\mathrm{DS}>0$ senkt $E_\mathrm F$ im Drain um $eV_\mathrm{DS}$, die Hälfte mit $k_y<0$ wird schwächer besetzt, und ein Nettostrom bleibt. Bei großem $V_\mathrm{DS}$ injiziert der Drain gar nicht mehr. Dann kann der Strom nicht weiter steigen, solange die Höhe der Barriere gleich bleibt, und im Idealfall bestimmt sie nur das Gate. Dieses Bild ist streng gültig, wenn Elektronen ohne Stoß laufen. Stöße mischen die Hälften teilweise, die Ursache des Stroms bleibt dieselbe: Source und Drain besetzen die Zustände ungleich.

::::beispiel
Im Rechenmodell ist $\Phi_\mathrm{bi}=0{,}910$ eV. Bei $V_\mathrm{GS}=V_\mathrm{FB}$ ist $E_\mathrm b=0{,}91$ eV$=35\,k_\mathrm BT$. Bei $V_\mathrm{GS}=0$ ist $\varphi_\mathrm s=0{,}539$ V, also $E_\mathrm b=0{,}37$ eV und $n(0)=3{,}0\cdot10^{12}\,\mathrm{cm^{-3}}$. Bei $V_\mathrm{GS}=V_\mathrm{th}$ bleiben 0,13 eV$=5{,}1\,k_\mathrm BT$ und $n(0)=N_\mathrm A$. Das Gate senkt die Barriere um 0,78 eV und hebt die Dichte um den Faktor $10^{13}$.
::::

⁠**Grenzfall:** Bei $\varphi_\mathrm s=0$ ist $E_\mathrm b=\Phi_\mathrm{bi}$: Ohne Wirkung des Gates sieht das Elektron den gewöhnlichen p-n-Übergang.

:::frage Wenn das Feld die Elektronen vor der Spitze bremst, wie kommen sie dann hinauf?
Durch ihre Wärmebewegung. Der Anteil mit genug Energie ist $\exp(-E_\mathrm b/(k_\mathrm BT))$, und dieser Anteil dringt gegen das Feld vor, wie in einem p-n-Übergang in Durchlassrichtung. Das Feld hält die Dichte klein, es verbietet den Weg nicht.
:::

:::aufgabe Aufgabe 2 ★★ Source-Übergang und Barriere
<span class="anker" id="aufg-2"></span>

Ein MOSFET hat $N_\mathrm A=10^{16}\,\mathrm{cm^{-3}}$ und $N_\mathrm D=10^{19}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Berechne im Flachbandfall $\Phi_\mathrm{bi}$ und die Breiten der Verarmungszone im p- und im n-Gebiet ([Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html)). In welchem Verhältnis stehen sie, und warum?

</li>

<li>

Wie groß sind $E_\mathrm b$ und $n(0)$ bei $\varphi_\mathrm s=0{,}30$ V und $0{,}72$ V? Um welchen Faktor wächst $n(0)$?

</li>

</ol>

:::loesung
(a) $\Phi_\mathrm{bi}=25{,}85\,\mathrm{meV}\cdot\ln(10^{16}\cdot10^{19}/(8{,}9\cdot10^{9})^2)=0{,}899$ eV. Mit den Formeln aus [Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html) ist die Zone im p-Gebiet 341 nm und im n-Gebiet 0,34 nm breit. Das Verhältnis ist 1000, also $N_\mathrm D/N_\mathrm A$, denn beide Seiten tragen dieselbe Ladung. (b) Bei 0,30 V ist $E_\mathrm b=0{,}599$ eV und $n(0)=8{,}6\cdot10^{8}\,\mathrm{cm^{-3}}$, bei 0,72 V ist $E_\mathrm b=0{,}179$ eV und $n(0)=9{,}8\cdot10^{15}\,\mathrm{cm^{-3}}$. Der Faktor ist $\mathrm{e}^{0{,}42/0{,}02585}=1{,}1\cdot10^{7}$.
:::
:::
