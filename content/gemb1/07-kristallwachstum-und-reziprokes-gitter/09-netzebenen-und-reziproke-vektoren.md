---
title: Stufe 7: Netzebenen und reziproke Vektoren
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
order: 4170900
summary: Teil 6 benennt Ebenen über Kehrwerte.
tags: Bragg-Gleichung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
[Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html) benennt Ebenen über Kehrwerte. Der Name „reziprok“ ist kein Zufall. Diese Stufe zeigt: Jede Schar von Netzebenen gehört zu genau einem reziproken Gittervektor.
:::

**Die Idee.** Die Welle $\mathrm{e}^{\mathrm{j}\boldsymbol G\cdot\boldsymbol r}$ hat ebene Wellenfronten senkrecht zu $\boldsymbol G$ im Abstand $2\pi/|\boldsymbol G|$. Weil sie zum Gitter passt, ist ihre Phase an jedem Gitterpunkt ein Vielfaches von $2\pi$. Alle Gitterpunkte liegen also auf Wellenfronten, und diese Fronten sind Netzebenen (Abb. [7](#abb-7)).

:::satz Satz 7.1 (Netzebenen und reziproke Vektoren)
<span class="anker" id="satz-7-1"></span>

$h_1,h_2,h_3$ seien teilerfremd, und $(h_1h_2h_3)$ sei die Ebenenschar mit den Achsenabschnitten $\boldsymbol a_1/h_1$, $\boldsymbol a_2/h_2$, $\boldsymbol a_3/h_3$. Dann steht $\boldsymbol G=h_1\boldsymbol b_1+h_2\boldsymbol b_2+h_3\boldsymbol b_3$ senkrecht auf der Schar, und für den Abstand benachbarter Ebenen gilt

<span class="anker" id="gl-7-1"></span>
$$d=\frac{2\pi}{|\boldsymbol G|}. \tag{7.1}$$
:::

⁠**So liest man das:** Das sind die Millerschen Indizes aus [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html) mit $h_1=h$, $h_2=k$, $h_3=l$. Sie tragen hier Nummern, weil $k$ die Wellenzahl ist. Jeder Punkt des reziproken Gitters steht für eine Ebenenschar: Seine Richtung ist die Normale, seine Länge $2\pi/d$. **Gültigkeit:** Die Indizes beziehen sich auf primitive Gittervektoren. Ist $h_i=0$, ist die Ebene parallel zu $\boldsymbol a_i$, und man rechnet mit den übrigen Achsen.

:::herleitung Senkrecht und Abstand
Die Vektoren $\boldsymbol a_1/h_1-\boldsymbol a_2/h_2$ und $\boldsymbol a_1/h_1-\boldsymbol a_3/h_3$ liegen in der Ebene durch die drei Achsenabschnitte. Mit [(5.2)](reziproke-gittervektoren-in-der-ebene-und-im-raum.html#gl-5-2) ist

$$\boldsymbol G\cdot\Bigl(\frac{\boldsymbol a_1}{h_1}-\frac{\boldsymbol a_2}{h_2}\Bigr)=2\pi-2\pi=0,$$

ebenso für den zweiten Vektor. Also ist $\boldsymbol G$ die Normale. Die Parallelebene durch den Ursprung ist die Nachbarebene. Ihr Abstand ist die Projektion von $\boldsymbol a_1/h_1$ auf die Normale:

$$d=\frac{\boldsymbol a_1}{h_1}\cdot\frac{\boldsymbol G}{|\boldsymbol G|}=\frac{2\pi}{|\boldsymbol G|}.$$
:::

:::abbildung gemb1/k7ebenen 7
Rechteckgitter mit $a_x=0{,}40$ nm, $a_y=0{,}60$ nm. Links die Scharen $(1\,1)$ und $(2\,1)$ mit ihrem Abstand $d$, rechts die zugehörigen Vektoren im reziproken Gitter. Jeder Pfeil steht senkrecht auf seiner Schar, und der engeren Schar gehört der längere Pfeil.
:::

::::beispiel
Im Rechteckgitter ist für $(1\,1)$ der Vektor $\boldsymbol G=(15{,}7;\,10{,}5)\,\mathrm{nm^{-1}}$, $|\boldsymbol G|=18{,}9\,\mathrm{nm^{-1}}$, also $d=0{,}333$ nm. Für $(2\,1)$ ist $|\boldsymbol G|=33{,}1\,\mathrm{nm^{-1}}$ und $d=0{,}190$ nm.
::::

⁠**Grenzfall:** Für $(1\,0)$ ist $\boldsymbol G=\boldsymbol b_1$ und $d=a_x$, wie es sein muss.

**Kubisch.** Im SC-Gitter ist $\boldsymbol G=(2\pi/a)(h_1,h_2,h_3)$, und aus [(7.1)](#gl-7-1) folgt $d=a/\sqrt{h_1^2+h_2^2+h_3^2}$, die Formel aus [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html). Auch die Regel aus [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html), dass $[hkl]$ nur im kubischen System senkrecht auf $(hkl)$ steht, wird klar: Die Normale ist immer $\boldsymbol G=\sum h_i\boldsymbol b_i$. Mit $[hkl]$ stimmt sie nur überein, wenn alle $\boldsymbol b_i$ dasselbe Vielfache ihres $\boldsymbol a_i$ sind, und das verlangt gleich lange, orthogonale Achsen.

**Zonenrand und Reflexion.** Eine Welle trifft unter dem Winkel $\theta$ zur Ebene auf parallele Netzebenen im Abstand $d$. Jede Ebene reflektiert einen kleinen Teil. Die Teilwelle von der nächsttieferen Ebene läuft $2d\sin\theta$ weiter. Verstärkung gibt es nur, wenn dieser Umweg ein Vielfaches der Wellenlänge ist:

<span class="anker" id="gl-7-2"></span>
$$2d\sin\theta=\nu\lambda,\qquad\nu=1,2,\dots \tag{7.2}$$

Das ist die __Bragg-Gleichung__ mit der Ordnung $\nu$. Der Zonenrand [(6.1)](die-brillouin-zone.html#gl-6-1) sagt dasselbe für $\nu=1$: Seine linke Seite ist $|\boldsymbol k|\sin\theta=(2\pi/\lambda)\sin\theta$, seine rechte $|\boldsymbol G|/2=\pi/d$. Wellenvektoren auf dem Zonenrand gehören also genau zu den Wellen, die Netzebenen reflektieren. Hin- und rücklaufende Welle bilden dort eine stehende Welle. Das erklärt, warum in [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) die Geschwindigkeit bei $k=\pi/a$ null ist. **Zahlenprobe:** Röntgenlicht mit $\lambda=0{,}1541$ nm trifft $(111)$-Ebenen von Silizium ($d=0{,}3136$ nm) unter $\theta=14{,}2^\circ$. Dann ist $|\boldsymbol k|\sin\theta=10{,}02\,\mathrm{nm^{-1}}$, genau der Abstand der Sechseckflächen aus Stufe [6](die-brillouin-zone.html#stufe-6).

:::frage Teil 6 sagt $d_{hkl}=a/\sqrt{h^2+k^2+l^2}$. Gilt das auch in Silizium?
Nur für Scharen, zu denen es ein $\boldsymbol G$ gibt. [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html) zählt bei FCC längs der Würfelkanten $\boldsymbol e_i$, nicht längs der $\boldsymbol a_i$. Das reziproke Gitter von FCC enthält $(2\pi/a)(h,k,l)$ aber nur, wenn alle drei Zahlen gerade oder alle ungerade sind. $(111)$ gehört dazu: $d=a/\sqrt3=0{,}3136$ nm. Für $(100)$ ist der kürzeste Vektor $(200)$, also $d=a/2=0{,}272$ nm. Das sind die Zwischenebenen aus [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html).
:::

:::aufgabe Aufgabe 9 ★★ Ebenen im orthorhombischen Gitter
<span class="anker" id="aufg-9"></span>

Ein Gitter hat $\boldsymbol a_1=(0{,}30;\,0;\,0)$, $\boldsymbol a_2=(0;\,0{,}40;\,0)$, $\boldsymbol a_3=(0;\,0;\,0{,}50)$ in nm.

<ol class="al">

<li>

Gib die $\boldsymbol b_j$ an. Berechne $|\boldsymbol G|$ und $d$ für $(100)$, $(110)$ und $(111)$.

</li>

<li>

Zeige, dass $\boldsymbol G$ von $(111)$ senkrecht auf $\boldsymbol a_1-\boldsymbol a_2$ steht.

</li>

<li>

Welchen Winkel schließt $\boldsymbol G$ von $(111)$ mit der Richtung $[111]$ ein? Warum nicht null?

</li>

</ol>

:::loesung
(a) Orthogonale Achsen ergeben $\boldsymbol b_1=(20{,}94;0;0)$, $\boldsymbol b_2=(0;15{,}71;0)$, $\boldsymbol b_3=(0;0;12{,}57)\,\mathrm{nm^{-1}}$. $(100)$: $|\boldsymbol G|=20{,}94\,\mathrm{nm^{-1}}$, $d=0{,}300$ nm. $(110)$: $26{,}18\,\mathrm{nm^{-1}}$, $d=0{,}240$ nm. $(111)$: $29{,}04\,\mathrm{nm^{-1}}$, $d=0{,}216$ nm. (b) $\boldsymbol G\cdot(\boldsymbol a_1-\boldsymbol a_2)=2\pi-2\pi=0$. (c) $\cos\phi=\boldsymbol G\cdot(\boldsymbol a_1+\boldsymbol a_2+\boldsymbol a_3)/(|\boldsymbol G|\,|\boldsymbol a_1+\boldsymbol a_2+\boldsymbol a_3|)$ ergibt $\phi=23{,}4^\circ$. Die Achsen sind verschieden lang, also wiegt die kurze Achse in $\boldsymbol G$ stärker und in $[111]$ schwächer.
:::
:::
