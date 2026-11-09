---
title: Stufe 7: Das Loch
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Bandstrukturen lesen
order: 4190900
summary: An der Oberkante eines Bands ist die Masse negativ, und ein fast volles Band enthält unvorstellbar viele Elektronen.
tags: Defektelektron, schwere Löcher, leichte Löcher
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
An der Oberkante eines Bands ist die Masse negativ, und ein fast volles Band enthält unvorstellbar viele Elektronen. Diese Stufe ersetzt beide Schwierigkeiten durch ein einziges neues Teilchen.
:::

**Die Idee.** Ein volles Band trägt keinen Strom ([Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html)). Fehlt ein Elektron, fehlt auch dessen Beitrag, und der Rest ergibt einen Strom. Statt $10^{23}$ Elektronen zu verfolgen, verfolgt man den einen leeren Platz. Im Ortsbild: In einer Bindung fehlt ein Elektron, ein Nachbarelektron rückt nach, und die Lücke wandert entgegen.

:::definition Definition 7.1 (Defektelektron oder Loch)
<span class="anker" id="satz-7-1"></span>

Ein unbesetzter Zustand in einem sonst vollen Band wird durch ein Teilchen mit der Ladung $+e$ und positiver effektiver Masse vom gleichen Betrag beschrieben. Es heißt __Defektelektron__ oder Loch. Fehlt das Elektron bei $k_\mathrm e$ nahe der Oberkante, gilt für das Loch

<span class="anker" id="gl-7-1"></span>
$$k_\mathrm h=-k_\mathrm e,\qquad v_\mathrm h=v(k_\mathrm e),\qquad E_\mathrm h=E_\mathrm V-E(k_\mathrm e)=\frac{\hbar^2k_\mathrm h^2}{2m_\mathrm V^*},\qquad F_\mathrm h=+e\mathcal E. \tag{7.1}$$
:::

:::herleitung Aus dem vollen Band
<ol>

<li>

Im vollen Band ist $\sum k=0$ und $\sum v=0$. Ohne das Elektron bei $k_\mathrm e$ bleibt $\sum k=-k_\mathrm e$, der Wellenvektor des Lochs.

</li>

<li>

Die übrigen Elektronen haben $\sum v=-v(k_\mathrm e)$. Auf einer Kette der Länge $L$ tragen sie den Strom $I=(-e/L)(-v(k_\mathrm e))=(+e/L)\,v(k_\mathrm e)$, den Strom einer positiven Ladung mit der Geschwindigkeit $v(k_\mathrm e)$.

</li>

<li>

Im Feld gilt für jedes Elektron $\hbar\,\mathrm{d} k/\mathrm{d} t=-e\mathcal E$, der leere Platz wandert mit. Also ist $\hbar\,\mathrm{d} k_\mathrm h/\mathrm{d} t=+e\mathcal E$.

</li>

<li>

Ein Elektron mit $m^*>0$ hat $\mathrm{d} v/\mathrm{d} t=-(e/m^*)\mathcal E$. An der Oberkante ist $m^*=-m_\mathrm V^*<0$, also $\mathrm{d} v/\mathrm{d} t=+(e/m_\mathrm V^*)\mathcal E$: wie eine positive Ladung mit positiver Masse.

</li>

</ol>
:::

:::abbildung gemb1/k9loch 7
Oben links: Ein volles Band mit 15 Zuständen, symmetrisch um $k=0$. Oben rechts: Das Elektron bei $k_\mathrm e$ fehlt (roter Kreis), das Loch hat $k_\mathrm h=-k_\mathrm e$. Unten: Ortsbild zu drei Zeiten. Das Feld treibt Elektronen nach links, jedes rückt um einen Platz. Der leere Platz wandert nach rechts, in Feldrichtung.
:::

⁠**So liest man das:** Das Loch ist ein Rechenbild, kein eigenes Stück Materie, aber eine exakte Umformung derselben Summe. Seine positive Ladung ist handfest: Volles Band und Rumpfionen wären zusammen neutral, ohne ein Elektron bleibt $+e$. Im Feld läuft es mit $\mathcal E$, das Elektron gegen $\mathcal E$. Seine Energie zählt von $E_\mathrm V$ nach unten, im Zustand kleinster Energie besetzen Löcher die höchsten Zustände des Bands. **Gültigkeit:** fast volles Band. Mit mehr leeren Zuständen gibt es mehr Löcher, und das Band leitet besser. Eine feste Masse haben sie, solange [(5.3)](die-effektive-masse-im-kristall.html#gl-5-3) gilt.

**Zwei Sorten.** An der Valenzbandkante von Silizium treffen sich zwei Bänder mit verschiedener Krümmung (Stufe [3](silizium.html#stufe-3)). Das flachere ergibt __schwere Löcher__ mit $m_\mathrm{hh}^*=0{,}49\,m_0$, das stärker gekrümmte __leichte Löcher__ mit $m_\mathrm{lh}^*=0{,}16\,m_0$.

::::beispiel
Ein Valenzband habe die Form der Kette im Rechenmodell, $E=E_\mathrm V-2V_\mathrm{ss}(1-\cos(ka))$ mit $m_\mathrm V^*=1{,}22\,m_0$. Das Feld $\mathcal E=10^6$ V/m beschleunigt das Loch mit $e\mathcal E/m_\mathrm V^*=1{,}4\cdot10^{17}\,\mathrm{m/s^2}$ in Feldrichtung.
::::

⁠**Grenzfall:** Ein Band mit einem einzigen Elektron und eines mit einem einzigen Loch sind Spiegelbilder, und halb gefüllt sind beide Beschreibungen gleich gut.

:::aufgabe Aufgabe 8 ★★ Einem Loch folgen
<span class="anker" id="aufg-8"></span>

Ein Valenzband ist $E=E_\mathrm V-2V(1-\cos(ka))$ mit $V=0{,}4$ eV und $a=0{,}3$ nm. Das Elektron bei $k_\mathrm e=+2\,\mathrm{nm^{-1}}$ fehlt.

<ol class="al">

<li>

Berechne $m_\mathrm V^*$ und $E_\mathrm h$ exakt und aus der Parabel.

</li>

<li>

Gib $k_\mathrm h$ und $v_\mathrm h$ an. In welche Richtung bewegt sich das Loch?

</li>

<li>

Ein Feld $\mathcal E=+10^6$ V/m wirkt für 1 ps. Wie ändern sich $k_\mathrm e$ und $k_\mathrm h$?

</li>

<li>

Vorhersage: Elektronen im Leitungsband und Löcher im Valenzband liegen im selben Feld. Laufen sie in dieselbe Richtung? Fließen ihre Ströme in dieselbe Richtung?

</li>

</ol>

:::loesung
(a) $m_\mathrm V^*=\hbar^2/(2Va^2)=1{,}06\,m_0$. Exakt $E_\mathrm h=2V(1-\cos0{,}6)=0{,}140$ eV, Parabel $0{,}144$ eV. (b) $k_\mathrm h=-2\,\mathrm{nm^{-1}}$, $v_\mathrm h=-(2Va/\hbar)\sin0{,}6=-2{,}06\cdot10^5$ m/s. Das Loch läuft nach links, passend zu $k_\mathrm h<0$ bei positiver Masse. (c) $\Delta k_\mathrm e=-e\mathcal Et/\hbar=-1{,}52\,\mathrm{nm^{-1}}$, also $k_\mathrm e=0{,}48\,\mathrm{nm^{-1}}$ und $k_\mathrm h=-0{,}48\,\mathrm{nm^{-1}}$. Das Feld bremst das nach links laufende Loch. (d) Sie laufen entgegengesetzt, die Ströme fließen in dieselbe Richtung, denn auch die Ladungen sind entgegengesetzt.
:::
:::
