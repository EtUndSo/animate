---
title: Stufe 8: Dipol-Bindungen und reale Materialien
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Chemische Bindung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/chemische-bindung
knoten: Kapitel 5: Chemische Bindung
order: 4151000
summary: In H 2 O und CH 4 haben alle Atome die Edelgaskonfiguration, und doch werden beide bei tiefer Temperatur flüssig und fest.
tags: Dipol, Van-der-Waals-Wechselwirkung, Dipolmoment, Polarisierbarkeit, Hydrathüllen, Wasserstoffbrückenbindung, Londonsche Dispersionswechselwirkung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
In H$_2$O und CH$_4$ haben alle Atome die Edelgaskonfiguration, und doch werden beide bei tiefer Temperatur flüssig und fest. Diese Stufe erklärt die schwachen Kräfte zwischen abgeschlossenen Molekülen und ordnet alle Bindungstypen in reale Materialien ein.
:::

**Die Idee.** Ein neutrales Teilchen kann getrennte Ladungsschwerpunkte haben, einen __Dipol__. Seine negative Seite liegt dem positiven Teil des Nachbarn näher, die Anziehung überwiegt die Abstoßung ein wenig. Kein Elektron wechselt den Besitzer, streng genommen ist das eine Wechselwirkung statt einer Bindung (__Van-der-Waals-Wechselwirkung__ im weiteren Sinn). Weil sich die Beiträge fast aufheben, ist sie schwach und fällt steil mit dem Abstand.

:::abbildung gemb1/k5schwach 8
Oben: Die drei Dipol-Bindungen, $\delta+$ und $\delta-$ sind Teilladungen. Unten: Bindungstypen nach Elektronegativität, waagerecht das Mittel beider Partner, senkrecht ihre Differenz. Grau: Mischformen. Die Grenzen sind fließend.
:::

:::satz Satz 8.1 (Drei Dipol-Bindungen)
<span class="anker" id="satz-8-1"></span>

Für das __Dipolmoment__ $p_\mathrm{el}=q\,d$ (Ladungen $\pm q$ im Abstand $d\ll r$) gilt bei günstiger Ausrichtung

<span class="anker" id="gl-8-1"></span>
$$\begin{aligned} \text{Dipol--Ion:}\quad&E_\mathrm{an}=-\frac{q_\mathrm I\,p_\mathrm{el}}{4\pi\varepsilon_0r^2},&\text{Dipol--Dipol in einer Linie:}\quad&E_\mathrm{an}=-\frac{2\,p_\mathrm{el,1}\,p_\mathrm{el,2}}{4\pi\varepsilon_0r^3},\\ \text{London:}\quad&E_\mathrm{an}\propto-\frac{\alpha_\mathrm{pol,1}\,\alpha_\mathrm{pol,2}}{r^6}. \end{aligned} \tag{8.1}$$
:::

⁠**So liest man das:** $q_\mathrm I$ ist die Ladung eines Ions, Wasser hat $p_\mathrm{el}=6{,}2\cdot10^{-30}$ C m. Die __Polarisierbarkeit__ $\alpha_\mathrm{pol}$ sagt, wie leicht sich die Hülle in einem Feld verschiebt: $p_\mathrm{el}=\alpha_\mathrm{pol}\mathcal E$. **Gültigkeit:** $r$ größer als die Moleküle. Frei rotierende Dipole sind nur zeitweise günstig ausgerichtet, die Bindung wird dann schwächer.

**Die drei Typen.** ⁠**Dipol–Ion:** Wassermoleküle sind gewinkelt, und Sauerstoff zieht die Elektronen stärker an als Wasserstoff. Ihr Dipolmoment ist darum groß und bleibend. In Salzlösungen umgeben sie die Ionen mit der passenden Seite und bilden __Hydrathüllen__. **Dipol–Dipol:** Moleküle mit bleibendem Dipolmoment wie Wasser, Ethanol C$_2$H$_5$OH oder Ether H$_3$C–O–CH$_3$ richten sich aneinander aus. Besonders stark ist das zwischen OH-Gruppen und heißt dort __Wasserstoffbrückenbindung__. **London:** Auch in Methan und Edelgasen entsteht durch die Bewegung der Elektronen jederzeit ein kleiner Dipol. Sein Feld verschiebt die Hülle des Nachbarn und erzeugt dort einen Dipol, beide ziehen sich an. Das ist die __Londonsche Dispersionswechselwirkung__ oder Van-der-Waals-Wechselwirkung im engeren Sinn.

:::herleitung Jeder Schritt kostet Potenzen von $r$
Eine Ladung erzeugt das Potential $\propto1/r$. Ein Dipol ist die Differenz zweier solcher Potentiale im Abstand $d$, also $d$ mal Ableitung: $\propto d/r^2$. Das ergibt die erste Formel. Ein zweiter Dipol spürt wieder nur eine Differenz, also $\propto1/r^3$. Bei London entsteht $p_\mathrm{el,2}=\alpha_\mathrm{pol,2}\mathcal E$ erst durch das Feld $\mathcal E\propto p_\mathrm{el,1}/r^3$ des ersten Dipols, deshalb $E_\mathrm{an}\propto p_\mathrm{el,1}p_\mathrm{el,2}/r^3\propto\alpha_\mathrm{pol,2}\,p_\mathrm{el,1}^2/r^6$. Der schwankende Dipol $p_\mathrm{el,1}$ wächst seinerseits mit $\alpha_\mathrm{pol,1}$.
:::

::::beispiel
Ein Na$^+$ im Abstand 0,23 nm von einem Wassermolekül gewinnt 1,05 eV, zwei Wassermoleküle in einer Linie bei 0,28 nm gewinnen 0,19 eV. Für gleiche Atome gilt bei London $E_\mathrm{an}=-\frac34\Delta E_\mathrm{IE}\,(\alpha_\mathrm{pol}/(4\pi\varepsilon_0))^2/r^6$. Argon mit 0,00164 nm$^3$, 15,76 eV und $r_0=0{,}38$ nm ergibt 10,6 meV, gemessen sind 10,4 meV. Das liegt unter $k_\mathrm BT$ bei 300 K, darum ist Argon gasförmig. Dipol-Bindungen reichen von 0,4 eV bei Wasserstoffbrücken bis 0,01 eV bei London.
::::

⁠**Grenzfall:** Verdoppelt man $r$, sinkt die Energie auf $\frac14$, $\frac18$ oder $\frac1{64}$. London wirkt also kaum über die nächsten Nachbarn hinaus.

**Bindungstypen in realen Materialien.** Die drei starken Typen sind Grenzfälle mit jedem Übergang dazwischen. Abb. [8](#abb-8) ordnet sie: Große Differenz der Elektronegativität führt zu ionischer Bindung, kleine Differenz bei niedrigem Mittel zu metallischer, bei hohem Mittel zu kovalenter Bindung. In vielen Werkstoffen wirken mehrere Typen:

| Werkstoff | innerhalb | dazwischen, Folge |
|---|---|---|
| Keramik: Oxide, Isolatorporzellan, Ferroelektrika (schaltbar polarisiert), Ferrite (magnetische Oxide) | ionisch, kovalent | keine Schichten: hart |
| Minerale: Glimmer, Talk (Schichten), Asbest (Fäden) | ionisch, kovalent | Van der Waals, wenig ionisch: leicht trennbar |
| Graphit | kovalent | Van der Waals, sehr schwach metallisch: schmiert |
| Dichalkogenide MoS$_2$, WS$_2$ | kovalent | Van der Waals: Trockenschmierstoff |
| Organische Polymere (Kettenmoleküle) | kovalent | Van der Waals: Ketten gleiten |

Vom kovalenten über den ionischen und metallischen zum Van-der-Waals-Zustand fallen Bindungsenergie, Härte, Schmelzpunkt und elastische Steifigkeit, und der thermische Ausdehnungskoeffizient steigt (Stufe [1](die-energiekurve-der-bindung.html#stufe-1)). Das hilft bei der Wahl von Werkstoffen, etwa für Durchführungen durch Glas oder Keramik, wo sich beide Partner gleich ausdehnen müssen. Die Eigenschaften hängen aber auch von der Anordnung der Atome ab.

:::aufgabe Aufgabe 10 ★★ Dipole rechnen
<span class="anker" id="aufg-10"></span>

Ammoniak hat $p_\mathrm{el}=4{,}9\cdot10^{-30}$ C m.

<ol class="al">

<li>

Welche Energie gewinnt ein K$^+$ im Abstand 0,30 nm? Welche zwei NH$_3$ in einer Linie bei 0,34 nm?

</li>

<li>

Ne, Ar, Kr, Xe sieden bei 27, 87, 120 und 165 K. Erkläre den Gang ohne Rechnung.

</li>

<li>

Vorhersage: Warum siedet Wasser (373 K) viel höher als Methan (112 K)?

</li>

</ol>

:::loesung
(a) $p_\mathrm{el}=0{,}0306\,e\cdot$nm. K$^+$: $1{,}44\,\mathrm{eV\,nm}\cdot0{,}0306\,\mathrm{nm}/(0{,}30\,\mathrm{nm})^2=0{,}49$ eV. Zwei NH$_3$: $2\cdot1{,}44\cdot0{,}0306^2/0{,}34^3=0{,}069$ eV. (b) Die Hüllen werden größer und lockerer, die Polarisierbarkeit und damit die London-Anziehung steigt. (c) Wasser hat ein bleibendes Dipolmoment und Wasserstoffbrücken, Methan nur London-Anziehung.
:::
:::

:::aufgabe Aufgabe 11 ★ Bindungen erkennen
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Nenne die vier Bindungstypen mit je einem Beispiel. Welche hat eine ausgezeichnete Richtung?

</li>

<li>

Ordne zu: MgO, Kupfer, Silizium, festes Argon, GaAs, Polyethylen. Wo liegen Mischformen vor?

</li>

<li>

Ein Kupferstift (17 ppm/K) von 10 mm Länge steckt in Glas (3,3 ppm/K). Um wie viel unterscheiden sich die Längen bei 300 K Erwärmung? Wie viel bleibt mit einer Legierung von 5 ppm/K?

</li>

</ol>

:::loesung
(a) Ionisch (NaCl), kovalent (Silizium), metallisch (Kupfer), Van der Waals (zwischen Graphitschichten). Eine ausgezeichnete Richtung hat die kovalente Bindung. (b) MgO: ionisch mit kovalentem Anteil. Kupfer: metallisch. Silizium: kovalent. Festes Argon: London. GaAs: kovalent mit ionischem Anteil. Polyethylen: kovalent in der Kette, Van der Waals zwischen den Ketten. (c) $(17-3{,}3)\cdot10^{-6}\,\mathrm{K^{-1}}\cdot300\,\mathrm{K}\cdot10\,\mathrm{mm}=41$ µ m. Mit 5 ppm/K bleiben 5 µ m.
:::
:::
