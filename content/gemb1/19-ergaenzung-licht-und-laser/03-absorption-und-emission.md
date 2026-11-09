---
title: Stufe 1: Absorption und Emission
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Ergänzung: Licht und Laser
order: 4290300
summary: Die Lösungen der zeitunabhängigen Schrödinger-Gleichung ändern sich nie.
tags: Photoabsorption, Photoemission, Photolumineszenz, Mehrphotonenabsorption, strahlungslosen Übergang, Absorptionskante
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die Lösungen der zeitunabhängigen Schrödinger-Gleichung ändern sich nie. Danach bliebe ein Elektron ewig auf seinem Niveau. Diese Stufe zeigt, wie es das Niveau wechselt und welche Energie Licht dafür mitbringen muss.
:::

**Die Idee.** Im thermischen Gleichgewicht, also nach langer Zeit in Kontakt mit der Umgebung, sitzt ein Elektron im Grundzustand, sobald der Abstand zum nächsten Niveau groß gegen $k_\mathrm BT$ ist. Überschüssige Energie ist dann längst abgeflossen. Auf ein höheres Niveau kommt es nur, wenn ihm die fehlende Energie zugeführt wird, zum Beispiel durch ein Photon. Das Photon verschwindet, das Elektron steigt (Abb. [1](#abb-1)). Beim umgekehrten Sprung entsteht ein Photon. Weil ein Photon unteilbar ist, muss seine ganze Energie zum Abstand der Niveaus passen.

:::abbildung gemb1/k19uebergaenge 1
Übergänge im Rechenmodell, Höhen maßstäblich. Links Absorption: von $E_1$ nach $E_2$, von $E_1$ nach $E_3$ und in zwei Schritten über $E_2$. Rechts Emission: dieselben Sprünge abwärts, dazu ein Sprung ohne Photon, bei dem die Energie als Wärme ins Gitter geht.
:::

:::definition Definition 1.1 (Absorption und Emission)
<span class="anker" id="satz-1-1"></span>

Bei der __Photoabsorption__ nimmt ein Elektron ein Photon auf und wechselt vom Niveau $E_1$ auf das höhere Niveau $E_2$. Bei der __Photoemission__ wechselt es von $E_2$ nach $E_1$ und gibt ein Photon ab. In beiden Fällen gilt

<span class="anker" id="gl-1-1"></span>
$$\hbar\omega_{21}=E_2-E_1,\qquad\lambda_{21}=\frac{hc}{E_2-E_1}. \tag{1.1}$$
:::

⁠**So liest man das:** $E_2-E_1$ ist der Abstand der Niveaus, typisch 0,1 bis 10 eV. $\omega_{21}$ ist die Kreisfrequenz des passenden Lichts in 1/s, der Index nennt zuerst das obere Niveau. Mit Photoemission ist hier die Abgabe von Licht gemeint, nicht das Herauslösen von Elektronen aus einer Oberfläche, das denselben Namen trägt. Wurde das Elektron vorher durch Licht angehoben, heißt das Leuchten __Photolumineszenz__. Solche Übergänge sind die Grundlage aller optoelektronischen Bauelemente. **Gültigkeit:** [(1.1)](#gl-1-1) ist notwendig, reicht aber nicht. Das Ausgangsniveau muss besetzt und das Zielniveau frei sein (Pauli-Prinzip, [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)). Außerdem müssen im Atom der Drehimpuls ([Teil 4](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale/atome-und-orbitale.html)) und im Kristall der Wellenvektor ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)) passen.

**Weitere Wege.** [(1.1)](#gl-1-1) gilt für jeden Einzelschritt. Ein Elektron kann also in Stufen steigen: Ein Photon $\hbar\omega_{21}$ hebt es auf $E_2$, ein zweites $\hbar\omega_{32}$ auf $E_3$, zusammen $\hbar\omega_{21}+\hbar\omega_{32}=E_3-E_1$. Strahlt man beide Frequenzen gleichzeitig ein, heißt das __Mehrphotonenabsorption__. Nach unten gibt es auch einen Weg ohne Licht: Beim __strahlungslosen Übergang__ geht die Energie als Phononen ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)) an das Kristallgitter und wird zu Wärme.

:::herleitung Warum genau diese Frequenz
Während des Übergangs ist das Elektron in einer Überlagerung beider Zustände, jeder mit dem Zeitfaktor $\mathrm{e}^{-\mathrm{j} Et/\hbar}$ aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html). Im Betragsquadrat entsteht ein Mischterm:

$$|\Psi|^2=|c_1\psi_1|^2+|c_2\psi_2|^2+2\operatorname{Re}\bigl(c_1^*c_2\,\psi_1^*\psi_2\,\mathrm{e}^{-\mathrm{j}(E_2-E_1)t/\hbar}\bigr).$$

Die Ladungswolke schwingt also mit $\omega_{21}=(E_2-E_1)/\hbar$. Das elektrische Feld des Lichts verrichtet nur dann über viele Schwingungen Arbeit an ihr, wenn es im selben Takt schwingt. Bei jeder anderen Frequenz mittelt sich seine Wirkung weg.
:::

::::beispiel
Im Rechenmodell gehört $\hbar\omega_{21}=1{,}80$ eV zu 689 nm (rot), $\hbar\omega_{31}=2{,}40$ eV zu 517 nm (grün) und $\hbar\omega_{32}=0{,}60$ eV zu 2067 nm (Infrarot). Aus dem Grundzustand absorbiert das Atom rotes und grünes Licht. Licht von 2067 nm geht hindurch, obwohl es zu einem Abstand passt, denn $E_2$ ist unbesetzt.
::::

⁠**Grenzfall:** Für $E_2-E_1\to0$ wächst $\lambda_{21}$ über alle Grenzen.

**Vom Niveau zum Band.** Ein Atom hat scharfe Linien. Im Kristall findet dagegen jedes Photon mit $\hbar\omega\ge E_\mathrm g$ ein besetztes und ein freies Niveau im passenden Abstand. Der Absorptionskoeffizient $\alpha_\mathrm P$ aus [Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html) steigt deshalb an einer steilen __Absorptionskante__, und ihre Lage verrät $E_\mathrm g$. In GaAs liegt sie bei 873 nm. Silizium absorbiert unterhalb von 1107 nm, aber schwach, weil ein Phonon mitwirken muss ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)). **Grenzfall:** Für $\hbar\omega<E_\mathrm g$ gibt es kein passendes Paar, und der Kristall ist durchsichtig.

:::frage Ein Photon hat mehr Energie, als der Abstand verlangt. Wird nur der passende Teil geschluckt?
Nein, ein Photon ist unteilbar. Ein Atom lässt es durch, wenn kein Niveau passt. Im Halbleiter gibt es höher im Band ein passendes Niveau: Das Elektron landet über der Kante und gibt den Überschuss $\hbar\omega-E_\mathrm g$ danach in kleinen Schritten als Wärme ans Gitter ab.
:::

:::aufgabe Aufgabe 1 ★ Niveaus und Farben
<span class="anker" id="aufg-1"></span>

Ein Atom hat die Niveaus $E_1=0$, $E_2=2{,}00$ eV und $E_3=2{,}75$ eV, das Elektron sitzt auf $E_1$.

<ol class="al">

<li>

Berechne Photonenenergie und Wellenlänge aller drei Übergänge. Welche sind sichtbar?

</li>

<li>

Nur Licht von 1653 nm fällt ein. Was geschieht? Was ändert zusätzliches Licht von 620 nm?

</li>

</ol>

:::loesung
(a) $E_2-E_1=2{,}00$ eV gibt 620 nm (orangerot), $E_3-E_1=2{,}75$ eV gibt 451 nm (blau), $E_3-E_2=0{,}75$ eV gibt 1653 nm (Infrarot). Die ersten beiden sind sichtbar. (b) Allein passiert nichts: 1653 nm passt zu $E_3-E_2$, aber $E_2$ ist leer. Mit 620 nm hebt das rote Licht Elektronen auf $E_2$, und von dort hebt das Infrarot sie auf $E_3$: $2{,}00+0{,}75=2{,}75$ eV.
:::
:::

:::aufgabe Aufgabe 2 ★★ Bandlücke aus der Absorptionskante
<span class="anker" id="aufg-2"></span>

Eine schwach dotierte Probe wird bei fester Intensität mit verschiedenen Wellenlängen durchstrahlt. Bis herab zu 775 nm kommt fast alles hindurch, darunter wird das Licht stark geschwächt.

<ol class="al">

<li>

Wie groß ist $E_\mathrm g$? Warum ändert man die Wellenlänge und nicht die Intensität?

</li>

<li>

Was geschieht mit 1300 nm und mit 650 nm? Für 650 nm sei $\alpha_\mathrm P=10^{4}\,\mathrm{cm^{-1}}$. Wie viel ist nach 5 µ m übrig?

</li>

<li>

Vorhersage: Bei starker n-Dotierung liegt $E_\mathrm F$ über $E_\mathrm C$. Wohin wandert die Kante?

</li>

</ol>

:::loesung
(a) $E_\mathrm g=1240\,\mathrm{eV\,nm}/775\,\mathrm{nm}=1{,}60$ eV. Die Kante hängt an der Energie jedes einzelnen Photons, also an $\lambda$. Mehr Photonen je Sekunde machen $\hbar\omega$ nicht größer. (b) 1300 nm sind 0,95 eV, weniger als die Lücke, das Licht geht durch. 650 nm sind 1,91 eV und werden absorbiert. Nach 5 µ m ist $\mathrm{e}^{-5}=0{,}7$ % übrig. (c) Die untersten Zustände des Leitungsbands sind besetzt, das Ziel ist dort nicht frei. Die Kante wandert zu größerer Energie und kürzerer Wellenlänge. Deshalb misst man an schwach dotierten Proben.
:::
:::
