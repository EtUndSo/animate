---
title: Stufe 4: GaAs, direkte und indirekte Lücke
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Bandstrukturen lesen
order: 4190600
summary: In Silizium liegen die beiden Bandkanten bei verschiedenen boldsymbol k .
tags: direkt, indirekt, Phonon
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
In Silizium liegen die beiden Bandkanten bei verschiedenen $\boldsymbol k$. Diese Stufe zeigt mit GaAs den Gegenfall und erklärt, warum dieser Unterschied über die Lichtausbeute entscheidet.
:::

**Die Idee.** Ein Photon trägt viel Energie, aber fast keinen Wellenvektor. Beim Sprung über die Lücke ändert sich $\boldsymbol k$ deshalb kaum, im Diagramm läuft der Sprung senkrecht. Liegen die Bandkanten übereinander, führt er direkt von Kante zu Kante. Liegen sie nebeneinander, fehlt ein Wellenvektor, den das Photon nicht liefern kann. Ein drittes Teilchen muss ihn bringen, und das macht den Vorgang selten.

**GaAs zählen.** Galliumarsenid hat die Zinkblendestruktur: wie Silizium, aber mit Ga auf dem einen und As auf dem anderen FCC-Gitter. Ga hat drei Außenelektronen, As fünf, zusammen acht je Zelle. Die acht Orbitale s und p der beiden Atome ergeben acht Bänder, die acht Elektronen füllen die unteren vier. Dass die Zelle zwei Atome enthält, zeigt auch dieser Schluss: Acht Außenelektronen an einem Atom wären eine Edelgasschale, und Edelgase sind bei Raumtemperatur keine Festkörper.

:::definition Definition 4.1 (Direkte und indirekte Bandlücke)
<span class="anker" id="satz-4-1"></span>

Das Valenzbandmaximum liege bei $\boldsymbol k_\mathrm V$, das Leitungsbandminimum bei $\boldsymbol k_\mathrm C$. Für $\boldsymbol k_\mathrm V=\boldsymbol k_\mathrm C$ heißt die Lücke __direkt__, sonst __indirekt__. GaAs ist direkt, beide Kanten liegen bei $\Gamma$. Silizium ist indirekt, $\boldsymbol k_\mathrm V$ liegt bei $\Gamma$, $\boldsymbol k_\mathrm C$ nahe $X$.
:::

:::abbildung gemb1/k9gaas 4
**Qualitative Skizzen**, nicht maßstäblich und nicht gerechnet, nur Lage der Extrema und Reihenfolge stimmen. Links GaAs: Das Photon führt senkrecht von Kante zu Kante, über der Mulde bei $\Gamma$ liegen Nebentäler bei $L$ und $X$. Rechts Silizium: Das Photon trägt die Energie, ein Phonon den Wellenvektor.
:::

:::satz Satz 4.2 (Übergang mit Licht)
<span class="anker" id="satz-4-2"></span>

Bei Absorption oder Emission eines Photons der Wellenlänge $\lambda$ bleiben Energie und Wellenvektor erhalten. Mit

<span class="anker" id="gl-4-1"></span>
$$E_\mathrm{Ph}=\frac{hc}\lambda,\qquad k_\mathrm{Ph}=\frac{2\pi}\lambda=\frac{E_\mathrm{Ph}}{\hbar c} \tag{4.1}$$

gilt beim Sprung ins Leitungsband $E_\mathrm{nach}-E_\mathrm{vor}=E_\mathrm{Ph}$ und $\boldsymbol k_\mathrm{nach}-\boldsymbol k_\mathrm{vor}=\boldsymbol k_\mathrm{Ph}\approx0$.
:::

⁠**So liest man das:** Bei direkter Lücke ist $E_\mathrm g$ die kleinste Photonenenergie, die ein Elektron hebt. Bei indirekter Lücke muss zusätzlich ein __Phonon__ mitwirken, ein Energiequant der Gitterschwingung. Es liefert den Unterschied $\boldsymbol k_\mathrm C-\boldsymbol k_\mathrm V$, und seine Energie ist mit einigen 10 meV klein gegen $E_\mathrm g$. Das erklärt die schlechte Ausbeute: Elektron, leerer Zustand und Phonon müssen zusammentreffen, das ist viel seltener als der direkte Sprung. In Silizium gibt ein Elektron seine Energie deshalb meist als Wärme ab.

::::beispiel
In GaAs gehört zu $E_\mathrm g=1{,}42$ eV die Wellenlänge $\lambda=873$ nm, nahes Infrarot. Dann ist $k_\mathrm{Ph}=0{,}0072\,\mathrm{nm^{-1}}$, 1545-mal weniger als $2\pi/a=11{,}11\,\mathrm{nm^{-1}}$. In Silizium ist $\lambda=1107$ nm und $k_\mathrm{Ph}=0{,}0057\,\mathrm{nm^{-1}}$, der Abstand der Kanten aber $9{,}83\,\mathrm{nm^{-1}}$, also 1733-mal mehr. Deshalb baut man Leuchtdioden und Laser aus GaAs und verwandten Stoffen.
::::

⁠**Grenzfall:** Rückt $\boldsymbol k_\mathrm C$ nach $\boldsymbol k_\mathrm V$, entfällt das Phonon, und die Lücke wird direkt.

**Täler in GaAs.** Das unterste Tal liegt bei $\Gamma$ und ist kugelförmig, mit der kleinen Masse $m^*=0{,}067\,m_0$. Rund 0,29 eV höher folgt ein Minimum bei $L$, rund 0,48 eV höher eines bei $X$. Knapp über $E_\mathrm C$ ist die Fläche konstanter Energie also eine Kugel um $\Gamma$, erst höher kommen Ellipsoide bei $L$ und dann bei $X$ hinzu. Die Wärmeenergie $k_\mathrm BT=26$ meV ist elfmal kleiner als der erste Abstand: Bei Raumtemperatur bleiben die Elektronen im $\Gamma$-Tal.

:::aufgabe Aufgabe 4 ★★ Licht und Lücke
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Welche Wellenlängen gehören zu GaAs (1,42 eV), InP (1,27 eV) und GaN (3,37 eV)? Welches Material leuchtet im Ultravioletten?

</li>

<li>

Ein Halbleiter wird durchstrahlt. Unterhalb von $\lambda=1{,}77$ µm wird das Licht stark geschwächt. Wie groß ist $E_\mathrm g$?

</li>

<li>

Silizium mit einem Phonon von 60 meV: Welche Photonenenergie entsteht, wenn das Elektron von Kante zu Kante fällt und das Phonon erzeugt wird? Welche braucht die Absorption, wenn es ebenfalls erzeugt wird?

</li>

</ol>

:::loesung
(a) $\lambda=hc/E_\mathrm g$: 873 nm, 976 nm, 368 nm. GaN leuchtet im Ultravioletten. (b) $E_\mathrm g=1240\,\mathrm{eV\,nm}/1770\,\mathrm{nm}=0{,}70$ eV. (c) Beim Fall erhält das Photon $1{,}12\,\mathrm{eV}-0{,}06\,\mathrm{eV}=1{,}06$ eV. Bei Absorption muss das Photon das erzeugte Phonon mitbezahlen: $1{,}18$ eV.
:::
:::
