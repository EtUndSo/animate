---
title: Stufe 6: Bandbreite, Abstand und Besetzung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Vom Atom zum Band
order: 4180800
summary: Das Band ist 4V ss breit.
tags: Gleichgewichtsabstand, erlaubtes Band, verbotene Band, Bändermodell, Valenzband, Leitungsband
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Das Band ist $4V_\mathrm{ss}$ breit. Diese Stufe fragt, wovon $V_\mathrm{ss}$ abhängt, was aus allen Niveaus eines Atoms wird und welche Rolle die Zahl der Elektronen spielt. Das Ergebnis ist das Bändermodell.
:::

**Die Idee.** $V_\mathrm{ss}$ misst die gemeinsame Fläche zweier Orbitale. Zwischen den Atomen fällt jedes Orbital exponentiell ab. Deshalb hängt die Kopplung sehr stark vom Abstand und von der Tiefe des Niveaus ab. Tief liegende Zustände nahe am Kern, also mit kleiner Quantenzahl $n$, sind klein und fest eingesperrt, sie merken vom Nachbarn fast nichts. Die äußersten Zustände überlappen stark.

:::satz Satz 6.1 (Kopplung und Abstand, Modell)
<span class="anker" id="satz-6-1"></span>

Liegt das Niveau um $\Delta E$ unter dem Potential zwischen den Atomen, gilt näherungsweise

<span class="anker" id="gl-6-1"></span>
$$V_\mathrm{ss}(r)\approx V_\mathrm{ss}(r_0)\,\mathrm{e}^{-\kappa(r-r_0)},\qquad\kappa=\frac{\sqrt{2m\,\Delta E}}{\hbar}. \tag{6.1}$$
:::

⁠**So liest man das:** Der __Gleichgewichtsabstand__ $r_0$ ist der Abstand, den die Atome im Kristall einnehmen. Der Faktor kommt aus [Teil 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html): Zwischen den Atomen ist $\phi_1\propto\mathrm{e}^{-\kappa x}$ und $\phi_2\propto\mathrm{e}^{-\kappa(r-x)}$, ihr Produkt also $\mathrm{e}^{-\kappa r}$. Kurz gesagt: Dünne oder niedrige Barriere, starker Überlapp, breites Band. Dicke oder hohe Barriere, schwacher Überlapp, flaches Band. **Kontrolle:** Wasserstoff mit $\Delta E=13{,}6$ eV ergibt $\kappa=18{,}9\,\mathrm{nm^{-1}}=1/r_1$, genau den Abfall des 1s-Orbitals aus [Teil 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html).

**Beispiel.** Mit $\Delta E=5$ eV ist $\kappa=11{,}5\,\mathrm{nm^{-1}}$. Drückt man die Kette um 1 % zusammen, also um 2,5 pm, wächst $V_\mathrm{ss}$ um 2,9 %, und das Band wird 2,06 eV breit. Das nutzt man in Transistoren: Im Kanal, dem Gebiet, durch das der Strom fließt, wird das Gitter verspannt. Bei 90 nm Strukturgröße brachte Druck-Verspannung rund 30 % mehr Strom. Real ändert der Druck auch die Form der Bänder, das Bild ist vereinfacht. Ein kernnahes Niveau bei $-40$ eV hat dagegen $\kappa=32{,}4\,\mathrm{nm^{-1}}$. Seine Kopplung ist um den Faktor $\mathrm{e}^{-(32{,}4-11{,}5)\cdot0{,}25}=0{,}005$ kleiner, sein Band nur rund 10 meV breit.

:::abbildung gemb1/k8abstand 6
Links: Modell [(6.1)](#gl-6-1) für Niveaus bei $-5$ eV und $-1$ eV mit den Kopplungen 0,5 eV und 0,75 eV bei $r_0=0{,}25$ nm. Mit sinkendem Abstand $r$ wird aus jedem Niveau ein Band, bei kleinem $r$ überlappen beide. Das kernnahe Niveau liegt in Wirklichkeit tiefer. Rechts: Besetzung bei $T=0$, Blau bedeutet voll, Weiß leer.
:::

:::definition Definition 6.2 (Bändermodell)
<span class="anker" id="satz-6-2"></span>

In einem Kristall aus $N$ Atomen spaltet jedes Niveau des Einzelatoms in ein Band aus $N$ Zuständen auf. Weil $N$ riesig ist, ist es quasikontinuierlich und heißt __erlaubtes Band__. Zwischen zwei erlaubten Bändern gibt es keine Zustände, das ist das __verbotene Band__ oder die Bandlücke. Erlaubte Bänder können sich überlappen, dann fehlt das verbotene Band dazwischen. Dieses __Bändermodell__ erweitert das Atommodell auf den Kristall.
:::

**Besetzung.** Auch im Kristall gilt das Pauli-Prinzip. Im Atom kennzeichnen $n$, $l$, $m_l$ den Zustand, im Band die Bandnummer und $k$. Jeder Zustand fasst zwei Elektronen, ein Band also $2N$, je zwei Plätze pro Rumpfion. Das gilt für jedes Band und auch in drei Dimensionen: Ein einfach kubischer Würfel der Kante $L$ hat $(L/a)^3=N$ Zustände in der ersten Zone. Daraus folgen die drei Fälle in Abb. [6](#abb-6):

<ul>

<li>

⁠**Metall:** Ein Band ist nur teilweise gefüllt. Direkt über den besetzten Zuständen sind freie, die Elektronen können sich bewegen, die Leitfähigkeit ist hoch.

</li>

<li>

⁠**Isolator:** Ein Band ist voll, das nächste leer und weit entfernt.

</li>

<li>

⁠**Halbleiter:** Bei $T=0$ ist das oberste gefüllte Band, das __Valenzband__, voll. Das leere __Leitungsband__ darüber liegt so nah, dass bei Raumtemperatur Wärme einige Elektronen hinüberhebt. Das ergibt eine gewisse Leitfähigkeit.

</li>

</ul>

Der Abstand heißt $E_\mathrm g=E_\mathrm C-E_\mathrm V$, mit der Oberkante $E_\mathrm V$ des Valenzbands und der Unterkante $E_\mathrm C$ des Leitungsbands.

:::frage Warum leitet ein volles Band nicht? Die Elektronen darin haben doch Geschwindigkeiten.
Nach [(5.3)](viele-atome.html#gl-5-3) gehört zu jedem $k$ ein Zustand $-k$ mit $v(-k)=-v(k)$, in einem vollen Band heben sich alle Geschwindigkeiten auf. Ein Feld müsste Elektronen in andere Zustände schieben, und alle sind belegt.
:::

:::aufgabe Aufgabe 7 ★★ Verspannen
<span class="anker" id="aufg-7"></span>

Ein Band hat bei $r_0=a=0{,}30$ nm die Kopplung $V_\mathrm{ss}=0{,}6$ eV, und es ist $\kappa=9\,\mathrm{nm^{-1}}$.

<ol class="al">

<li>

Berechne Bandbreite und $v_\text{max}$ ohne Verspannung.

</li>

<li>

Wie ändern sich beide bei 2 % Stauchung und bei 2 % Dehnung? Warum ändert sich $v_\text{max}$ weniger als $V_\mathrm{ss}$?

</li>

<li>

Wie breit ist das Band bei doppeltem Abstand? Was bleibt für $r\to\infty$?

</li>

</ol>

:::loesung
(a) Breite $4V_\mathrm{ss}=2{,}40$ eV, $v_\text{max}=5{,}47\cdot10^5$ m/s. (b) Stauchung: $V_\mathrm{ss}=0{,}633$ eV, 2,53 eV, $5{,}66\cdot10^5$ m/s. Dehnung: $V_\mathrm{ss}=0{,}569$ eV, 2,27 eV, $5{,}29\cdot10^5$ m/s. $V_\mathrm{ss}$ ändert sich um 5,5 %, $v_\text{max}$ um 3,4 %, denn in $V_\mathrm{ss}a$ wirkt $a$ gegenläufig. (c) $\mathrm{e}^{-9\cdot0{,}3}=0{,}067$, Breite 0,16 eV. Für $r\to\infty$ bleibt das scharfe Atomniveau.
:::
:::
