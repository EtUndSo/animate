---
title: Stufe 8: Hohe Dotierstoffdichten
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
order: 4211000
summary: Alle Formeln setzten getrennte Störstellen und die Boltzmann-Näherung voraus.
tags: Störstellenband, effektive Bandlücke, Bandlückenverengung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Alle Formeln setzten getrennte Störstellen und die Boltzmann-Näherung voraus. Diese Stufe zeigt, was geschieht, wenn die Donatoren so dicht sitzen, dass beides nicht mehr gilt.
:::

**Die Idee.** Die Bahn eines Donatorelektrons hat den Radius $r_\mathrm D=3{,}3$ nm. Rücken die Donatoren näher zusammen, überlappen ihre Wellenfunktionen. Dann geschieht dasselbe wie in [Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html) mit Atomen: Gleiche Niveaus koppeln und spalten auf. Aus dem scharfen Niveau wird ein __Störstellenband__. Es wird mit der Dichte breiter, erreicht das Leitungsband und verschmilzt mit ihm. Die Lücke schrumpft, und $E_\mathrm F$ wandert ins Band.

:::abbildung gemb1/k11hoch 8
Oben: Donatoren (rot) mit ihren Bahnen im Maßstab, Fenster 44 nm breit, gedachte regelmäßige Anordnung. Unten: Zustandsdichte, nicht maßstäblich. Bei $10^{17}\,\mathrm{cm^{-3}}$ ein scharfes Niveau, bei $10^{18}\,\mathrm{cm^{-3}}$ ein Störstellenband, bei $10^{19}\,\mathrm{cm^{-3}}$ verschmilzt es mit dem Leitungsband, die Lücke verkleinert sich auf $E_\mathrm g^\mathrm{eff}$, und $E_\mathrm F$ liegt im Band.
:::

:::definition Definition 8.1 (Bandlückenverengung und Entartung)
<span class="anker" id="satz-8-1"></span>

Die verkleinerte Lücke heißt __effektive Bandlücke__ $E_\mathrm g^\mathrm{eff}<E_\mathrm g$, der Effekt __Bandlückenverengung__ (englisch bandgap narrowing). Liegt $E_\mathrm F$ näher als $3k_\mathrm BT$ am Bandrand oder im Band, ist der Halbleiter entartet.
:::

⁠**So liest man das:** Das Verhältnis von Abstand $d=N_\mathrm D^{-1/3}$ und Radius entscheidet. Nach [Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html) fällt die Kopplung exponentiell mit dem Abstand, hier wie $\mathrm{e}^{-d/r_\mathrm D}$, denn die Abklingkonstante ist $1/r_\mathrm D$. Mit der Kopplung als Bruchteil von $\Delta E_\mathrm D$ ist das Band etwa $4\,\Delta E_\mathrm D\,\mathrm{e}^{-d/r_\mathrm D}$ breit. Das ist eine grobe Schätzung. **Folgen:** Im entarteten Halbleiter gelten [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) und damit $n\,p=n_\mathrm i^2$ nicht mehr. Man muss mit der vollen Fermi-Verteilung rechnen. Die Aktivierungsenergie verschwindet, also friert nichts mehr aus: $n$ bleibt bis $T\to0$ erhalten, der Stoff verhält sich metallisch.

::::beispiel
Mit 18,9 meV für $\Delta E_\mathrm D$ aus Stufe [4](warum-die-bindung-so-schwach-ist.html#stufe-4) ergibt sich:

| $N_\mathrm D$ in cm$^{-3}$ | $10^{17}$ | $10^{18}$ | $10^{19}$ | $10^{20}$ |
|---|---|---|---|---|
| Abstand $d$ in nm | 21,5 | 10,0 | 4,6 | 2,2 |
| $d/r_\mathrm D$ | 6,6 | 3,1 | 1,4 | 0,66 |
| Bandbreite in meV | 0,1 | 3,5 | 18 | 39 |

Bei $10^{19}\,\mathrm{cm^{-3}}$ ist die Breite so groß wie der Abstand zum Leitungsband: Das Band erreicht es, das ist die Größenordnung der Grenze. Die Bahnen berühren sich bei $d=2r_\mathrm D$, also $3{,}6\cdot10^{18}\,\mathrm{cm^{-3}}$.

Schon vorher versagt die Erschöpfung. Für $n=N_\mathrm D$ braucht man $K_1\gg N_\mathrm D$, und $K_1(300\,\mathrm{K})=2{,}5\cdot10^{18}\,\mathrm{cm^{-3}}$. Bei $N_\mathrm D=10^{17}\,\mathrm{cm^{-3}}$ sind 96 % ionisiert, bei $10^{18}\,\mathrm{cm^{-3}}$ rechnerisch nur 76 %.
::::

⁠**Grenzfall:** Bei $N_\mathrm D=N_\mathrm C\mathrm{e}^{-3}=1{,}4\cdot10^{18}\,\mathrm{cm^{-3}}$ ist nach [(6.3)](hohe-und-mittlere-temperaturen.html#gl-6-3) $E_\mathrm C-E_\mathrm F=3k_\mathrm BT$. Darüber darf die Boltzmann-Näherung nicht mehr benutzt werden.

:::frage Wenn das Niveau im Band aufgeht, ist die Dotierung dann nutzlos?
Im Gegenteil: Alle Donatoren liefern ihr Elektron, ohne dass Wärme nötig ist. Nur die Formeln dieses Kapitels gelten nicht mehr, und die Lücke ist kleiner.
:::

:::aufgabe Aufgabe 11 ★★ Wann wird es entartet?
<span class="anker" id="aufg-11"></span>

Silizium mit Phosphor.

<ol class="al">

<li>

Bei welchem $N_\mathrm D$ ist nach [(6.3)](hohe-und-mittlere-temperaturen.html#gl-6-3) bei 300 K $E_\mathrm C-E_\mathrm F=3k_\mathrm BT$? Wie groß ist dort $d/r_\mathrm D$?

</li>

<li>

Wie viele Si-Atome kommen bei $N_\mathrm D=10^{20}\,\mathrm{cm^{-3}}$ auf ein P-Atom? Was ergibt [(6.3)](hohe-und-mittlere-temperaturen.html#gl-6-3) für $E_\mathrm C-E_\mathrm F$, und was bedeutet das Vorzeichen?

</li>

<li>

Vorhersage: Was misst man an dieser Probe für $n$ bei 300 K und bei 4 K?

</li>

</ol>

:::loesung
(a) $N_\mathrm D=N_\mathrm C\mathrm{e}^{-3}=1{,}4\cdot10^{18}\,\mathrm{cm^{-3}}$, $d=8{,}9$ nm, $d/r_\mathrm D=2{,}7$. (b) 500 Si-Atome, das sind 0,2 %. $E_\mathrm C-E_\mathrm F=-33$ meV: $E_\mathrm F$ läge im Band, die Formel gilt dort nicht mehr. (c) In beiden Fällen rund $10^{20}\,\mathrm{cm^{-3}}$: Die Probe friert nicht aus.
:::
:::
