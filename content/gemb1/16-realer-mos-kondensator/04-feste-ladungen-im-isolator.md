---
title: Stufe 2: Feste Ladungen im Isolator
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260400
summary: Auch bei gleichen Austrittsarbeiten bleiben die Bänder nicht flach, wenn im Isolator Ladung sitzt.
tags: 
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Auch bei gleichen Austrittsarbeiten bleiben die Bänder nicht flach, wenn im Isolator Ladung sitzt. Diese Stufe berechnet, um wie viel sich die Flachbandspannung dadurch verschiebt.
:::

**Die Idee.** Im Oxid bleiben bei der Herstellung Ladungen zurück, die sich nicht bewegen. Die Feldlinien jeder positiven Ladung müssen auf negativer Gegenladung enden, und dafür gibt es zwei Orte: das Gate und den Halbleiter (Abb. [2](#abb-2), links). Der Anteil im Halbleiter bedeutet Bandverbiegung. Legt man negative Spannung ans Gate, übernimmt es immer mehr Gegenladung. Bei $V_\mathrm{FB}$ trägt es alles, Ladung und Feld im Halbleiter verschwinden, und die Bänder sind flach (rechts). Das Feld sitzt dann nur noch zwischen Gate und Isolatorladung.

:::abbildung gemb1/k16ladung 2
Ladung im p-Substrat, Höhen schematisch. Zeile a: nur $\Delta\Phi<0$. Zeile b: positive Oxidladung im Volumen. Zeile c: positive feste Ladung an der Grenzfläche. Links bei $V_\mathrm G=0$, die Summe aller Ladungen ist null. Rechts bei $V_\mathrm G=V_\mathrm{FB}$: Der Halbleiter ist ladungsfrei.
:::

:::definition Definition 2.1 (Feste Ladungen)
<span class="anker" id="satz-2-1"></span>

$Q'_\mathrm{IS}$ ist die Oxidladung, im Volumen des Isolators verteilt und je Fläche gezählt. $Q'_\mathrm{SS}$ ist die ortsfeste Grenzflächenladung, sie sitzt im Isolator direkt an der Grenzfläche zum Halbleiter. Beide hängen nicht von $V_\mathrm G$ ab. Für alle Rechnungen wird $Q'_\mathrm{IS}$ als Flächenladung an derselben Grenzfläche behandelt.
:::

:::satz Satz 2.2 (Flachbandspannung)
<span class="anker" id="satz-2-2"></span>

<span class="anker" id="gl-2-1"></span>
$$V_\mathrm{FB}=\frac{\Delta\Phi}{e}-\frac{Q'_\mathrm{IS}}{C'_\mathrm{IS}}-\frac{Q'_\mathrm{SS}}{C'_\mathrm{IS}},\qquad C'_\mathrm{IS}=\frac{\varepsilon_\mathrm{IS}}{d_\mathrm{IS}}. \tag{2.1}$$

Wirkt nur eine Ladung, gilt für ihren Beitrag $|Q'_\mathrm{IS}|=C'_\mathrm{IS}|V_\mathrm{FB}|$ beziehungsweise $|Q'_\mathrm{SS}|=C'_\mathrm{IS}|V_\mathrm{FB}|$.
:::

⁠**So liest man das:** Positive Ladung senkt $V_\mathrm{FB}$, negative hebt sie. Typische Werte sind 1 bis 10 nC/cm$^2$, entsprechend $10^{10}$ bis $10^{11}$ Elementarladungen je cm$^2$. **Gültigkeit:** Die Ladung sitzt als Fläche an der Grenzfläche.

:::herleitung Plattenkondensator aus Gate und Isolatorladung
Bei $V_\mathrm G=V_\mathrm{FB}$ ist $\varphi_\mathrm s=0$ und $Q'_\mathrm{SC}=0$. Die Neutralität verlangt $Q'_\mathrm M=-Q'_\mathrm{IS}-Q'_\mathrm{SS}$. Im Isolator herrscht das konstante Feld $\mathcal E_\mathrm{IS}=Q'_\mathrm M/\varepsilon_\mathrm{IS}$, also $V_\mathrm{IS}=\mathcal E_\mathrm{IS}d_\mathrm{IS}=-(Q'_\mathrm{IS}+Q'_\mathrm{SS})/C'_\mathrm{IS}$. Einsetzen in [(1.2)](verschiedene-austrittsarbeiten.html#gl-1-2) ergibt [(2.1)](#gl-2-1).
:::

**Lage der Ladung.** Sitzt eine Flächenladung im Abstand $y$ vom Gate, trägt nur die Strecke $y$ das Feld, und ihr Beitrag ist $-(Q'/C'_\mathrm{IS})\,(y/d_\mathrm{IS})$. Direkt am Gate wirkt sie gar nicht, an der Grenzfläche voll. Gleichmäßig im Volumen verteilt liegt ihr Schwerpunkt bei $d_\mathrm{IS}/2$, sie wirkt also halb so stark.

::::beispiel
Das Rechenmodell erhält $Q'_\mathrm{IS}=+8{,}0\,\mathrm{nC/cm^2}$ und $Q'_\mathrm{SS}=+3{,}2\,\mathrm{nC/cm^2}$, das sind $5{,}0\cdot10^{10}$ und $2{,}0\cdot10^{10}$ Elementarladungen je cm$^2$. Eine $(100)$-Fläche trägt $6{,}8\cdot10^{14}$ Atome je cm$^2$, auf rund 10 000 Atome kommt also eine Ladung. Die Beiträge sind $-0{,}046$ V und $-0{,}019$ V, zusammen $-0{,}065$ V. Damit ist

$$V_\mathrm{FB}=-0{,}899\,\mathrm{V}-0{,}065\,\mathrm{V}=-0{,}964\,\mathrm{V}.$$

Gleichmäßig verteilt brächte $Q'_\mathrm{IS}$ nur $-0{,}023$ V.
::::

⁠**Grenzfall:** Der Ladungsbeitrag wächst linear mit $d_\mathrm{IS}$: $-0{,}016$ V bei 5 nm, $-0{,}32$ V bei 100 nm, $-1{,}6$ V bei 500 nm. Dünne Isolatoren sind unempfindlich gegen feste Ladung.

Die drei Beiträge zu $V_\mathrm{FB}$ addieren sich, denn der Isolator ist linear. Die Bandverbiegung bei $V_\mathrm G=0$ addiert sich nicht, denn der Halbleiter ist nichtlinear: Exakt gerechnet sind es 0,501 V nur mit $\Delta\Phi$, 0,020 V nur mit den Ladungen und 0,547 V mit beidem.

:::frage Die Ladung sitzt direkt am Halbleiter. Wie kann ihr Feld dort bei $V_\mathrm{FB}$ verschwinden?
Eine Flächenladung erzeugt nach beiden Seiten ein gleich starkes Feld. Die Gegenladung auf dem Gate erzeugt ebenfalls eines. Im Isolator addieren sich beide, im Halbleiter heben sie sich auf. Genau bei $V_\mathrm{FB}$ ist die Gegenladung so groß, dass das vollständig gelingt.
:::

:::zusatz Woher die Ladungen stammen
An der Grenzfläche bleiben Atome unvollständig oxidiert, das ergibt positive feste Ladung. Im Volumen fängt das Oxid Elektronen oder Löcher ein, und Ionen wie $\mathrm{Na^+}$ wandern bei Wärme durch das Oxid. Sauberkeit und Tempern halten alle Sorten klein.
:::

:::aufgabe Aufgabe 3 ★★ Ladung aus der Verschiebung
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

In einem Kondensator mit 40 nm $\mathrm{SiO_2}$ verschiebt eine Flächenladung an der Grenzfläche $V_\mathrm{FB}$ um $-0{,}60$ V. Berechne $Q'$ mit Vorzeichen und die Elementarladungen je cm$^2$.

</li>

<li>

Wie groß wäre die Verschiebung bei gleicher Ladung in 5 nm $\mathrm{SiO_2}$?

</li>

<li>

Dieselbe Ladung sitzt in 40 nm $\mathrm{SiO_2}$ nun 10 nm von der Grenzfläche entfernt. Wie groß ist die Verschiebung?

</li>

<li>

Auf einer Scheibe misst du $V_\mathrm{FB}=-0{,}31$ V bei 10 nm und $-0{,}46$ V bei 40 nm $\mathrm{SiO_2}$. Trenne $\Delta\Phi$ und $Q'_\mathrm{IS}+Q'_\mathrm{SS}$.

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=86{,}3\,\mathrm{nF/cm^2}$, $Q'=+51{,}8\,\mathrm{nC/cm^2}$, positiv, weil $V_\mathrm{FB}$ sinkt. Das sind $3{,}2\cdot10^{11}$ Elementarladungen je cm$^2$. (b) $C'_\mathrm{IS}$ ist achtmal so groß: $-0{,}075$ V. (c) $y/d_\mathrm{IS}=30/40$, also $-0{,}45$ V. (d) Die Steigung ist $-5{,}0$ mV/nm, der Achsenabschnitt ergibt $\Delta\Phi/e=-0{,}31\,\mathrm{V}+0{,}05\,\mathrm{V}=-0{,}26$ V. $Q'_\mathrm{IS}+Q'_\mathrm{SS}=5{,}0\,\mathrm{mV/nm}\cdot\varepsilon_\mathrm{IS}=+17{,}3\,\mathrm{nC/cm^2}$.
:::
:::
