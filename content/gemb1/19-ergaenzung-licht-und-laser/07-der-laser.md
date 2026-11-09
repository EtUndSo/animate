---
title: Stufe 5: Der Laser
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Ergänzung: Licht und Laser
order: 4290700
summary: Licht derselben Energie stellt die Umkehr nicht her.
tags: Drei-Niveau-Laser, laseraktiv, Maser, Resonator, Halbleiterlaser
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Licht derselben Energie stellt die Umkehr nicht her. Diese Stufe pumpt über ein drittes Niveau, zeigt die beiden Möglichkeiten dafür und macht aus dem Verstärker einen Laser.
:::

**Die Idee.** Man pumpt mit Licht der größeren Energie $\hbar\omega_{31}=E_3-E_1$. Es passt weder zu $E_2-E_1$ noch zu $E_3-E_2$ und stimuliert keinen der Sprünge, auf denen verstärkt werden soll. Nach oben geht es also auf einem Weg, nach unten auf einem anderen. Zwischen $E_3$ und $E_1$ selbst gilt [(4.3)](die-besetzungsumkehr.html#gl-4-3): Dort kommt es höchstens zum Gleichstand. Verstärkt wird deshalb auf einer der beiden anderen Stufen (Abb. [5](#abb-5)).

:::definition Definition 5.1 (Drei-Niveau-Laser)
<span class="anker" id="satz-5-1"></span>

Das Absorbieren von $\hbar\omega_{31}$ heißt beim __Drei-Niveau-Laser__ Pumpen. Der Übergang, der das Licht verstärkt, heißt __laseraktiv__.

<ul>

<li>

⁠**Variante 1, $E_3\to E_2$ laseraktiv.** Eingestrahltes Licht $\hbar\omega_{32}<\hbar\omega_{31}$ stimuliert den Sprung, dabei entsteht ein Photon $\hbar\omega_{32}$. Das Elektron muss von $E_2$ schneller nach $E_1$ fallen, als von oben neue ankommen, oft strahlungslos. Sonst bleibt $E_2$ besetzt, das Ziel ist nicht frei, und die stimulierte Emission erlischt.

</li>

<li>

⁠**Variante 2, $E_2\to E_1$ laseraktiv.** Das Elektron geht sehr schnell und spontan von $E_3$ nach $E_2$, die Energie kann strahlungslos abfließen. Eingestrahltes Licht $\hbar\omega_{21}$ stimuliert dann den Sprung nach $E_1$.

</li>

</ul>
:::

:::abbildung gemb1/k19laser 5
Oben: die zwei Möglichkeiten des Drei-Niveau-Lasers. Grün das Pumpen, rot der Übergang, der Licht verstärkt, gestrichelt der schnelle Sprung ohne Licht. Unten links: Stab zwischen zwei Spiegeln, von denen einer einen kleinen Teil des Lichts durchlässt. Unten rechts: Besetzung von $E_2$ über der Rate $r$, mit der je Elektron gepumpt wird. Zwei Niveaus bleiben unter $\frac12$, drei Niveaus nach Variante 2 überschreiten es bei $r\tau_{21}=1$.
:::

:::satz Satz 5.2 (Bedingungen für die Umkehr)
<span class="anker" id="satz-5-2"></span>

Mit der Pumprate $r_\mathrm P$ je Elektron auf $E_1$ gilt stationär ohne verstärktes Licht

<span class="anker" id="gl-5-1"></span>
$$\text{Variante 1: }\frac{N_2}{N_3}=\frac{\tau_{21}}{\tau_{32}},\qquad\text{Variante 2: }\frac{N_2}{N_1}=r_\mathrm P\tau_{21}. \tag{5.1}$$

Umkehr verlangt also in Variante 1 $\tau_{21}<\tau_{32}$ und in Variante 2 $r_\mathrm P>1/\tau_{21}$.
:::

:::herleitung Zwei Bilanzen
⁠**Variante 1.** $E_2$ erhält $N_3/\tau_{32}$ und verliert $N_2/\tau_{21}$, stationär sind beide gleich. Läuft die Verstärkung, kommt der stimulierte Zufluss hinzu, und $E_2$ muss auch diesen abführen.

⁠**Variante 2.** Wegen des schnellen Sprungs bleibt $E_3$ fast leer, jedes gepumpte Elektron landet auf $E_2$. Der Zufluss $r_\mathrm PN_1$ ist gleich dem Abfluss $N_2/\tau_{21}$. Mit $N_1+N_2=N$ folgt

$$\frac{N_2}N=\frac{r_\mathrm P\tau_{21}}{1+r_\mathrm P\tau_{21}},\qquad N_2-N_1=N\,\frac{r_\mathrm P\tau_{21}-1}{r_\mathrm P\tau_{21}+1}.$$

Gegenüber [(4.3)](die-besetzungsumkehr.html#gl-4-3) fehlt die 2 im Nenner, denn das Pumplicht holt von $E_2$ niemanden zurück.
:::

⁠**So liest man das:** $r_\mathrm P$ ist die Rate aus [(3.2)](spontane-und-stimulierte-emission.html#gl-3-2) für das Pumplicht, in 1/s. In Variante 1 ist $E_2$ von Anfang an leer, wenige Elektronen auf $E_3$ genügen. In Variante 2 ist das untere Niveau der volle Grundzustand, mehr als die Hälfte aller Elektronen muss hinauf. Das verlangt starkes Pumpen und ein langlebiges, metastabiles $E_2$. Welcher Sprung laseraktiv ist, hängt von den Atomen ab. **Gültigkeit:** Variante 2 setzt $r_\mathrm P\tau_{32}\ll1$ voraus.

::::beispiel
Im Rechenmodell mit Variante 2 beginnt die Umkehr bei $r_\mathrm P=1000\,\mathrm{s^{-1}}$. Bei $r_\mathrm P=3000\,\mathrm{s^{-1}}$ ist $N_2=\frac34N$ und $N_1=\frac14N$, also $\alpha_\mathrm P=-A_\mathrm{Ph}N/2=-0{,}15\,\mathrm{cm^{-1}}$. Der Stab verstärkt um den Faktor $\mathrm{e}^{1{,}5}=4{,}48$. Auf $E_3$ sitzt nur der Anteil $N_3/N_1=r_\mathrm P\tau_{32}=3\cdot10^{-5}$. Vom gepumpten Photon gehen mindestens $0{,}60/2{,}40=25$ % als Wärme verloren.
::::

⁠**Grenzfall:** Für $r_\mathrm P\to\infty$ geht $N_2\to N$, nicht $N/2$ wie bei zwei Niveaus.

**Vom Verstärker zum Laser.** Das Wort kürzt *light amplification by stimulated emission of radiation* ab. Im Mikrowellenbereich heißt das Gerät __Maser__, das M steht für *microwave*. Für eine Lichtquelle stellt man den Stab zwischen zwei Spiegel, das ist der __Resonator__. Spontan entstandene Photonen längs der Achse laufen immer wieder durch den Stab und werden verstärkt, alle anderen gehen verloren. Ein Spiegel lässt einen kleinen Teil durch, das ist der Strahl. Weil alle Photonen Kopien sind, hat er eine Farbe, eine Richtung und eine Phase.

**Halbleiterlaser.** Der __Halbleiterlaser__ pumpt mit Strom statt mit Licht. Am p-n-Übergang in Durchlassrichtung ([Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html)) strömen Elektronen und Löcher in dieselbe dünne Zone. Dort ist der untere Teil des Leitungsbands besetzt und der obere Teil des Valenzbands leer, das ist Besetzungsumkehr. Fällt ein Elektron ins Loch, entsteht bei direkter Lücke ein Photon mit $\hbar\omega\ge E_\mathrm g$ ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)). Ohne Spiegel überwiegt die spontane Emission, das Bauelement ist dann eine Leuchtdiode.

:::zusatz Die Bedingung in der Diode
Mit den Quasi-Fermi-Niveaus aus [Teil 14](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang/der-p-n-uebergang.html) gilt $E_\mathrm{Fn}-E_\mathrm{Fp}=eU_\mathrm{pn}$. Liegt $E_2$ im Leitungs- und $E_1$ im Valenzband, wird $f(E_2)>f(E_1)$ zu $E_2-E_\mathrm{Fn}<E_1-E_\mathrm{Fp}$, also

<span class="anker" id="gl-5-2"></span>
$$E_\mathrm{Fn}-E_\mathrm{Fp}>\hbar\omega\ge E_\mathrm g. \tag{5.2}$$
:::

**Typische Laser.** Rubin und Erbium arbeiten nach Variante 2. Die Übrigen nutzen ein viertes Niveau: Der Sprung endet über dem Grundzustand auf einem Niveau, das schnell leer läuft wie $E_2$ in Variante 1. Der CO$_2$-Laser nutzt statt Elektronenniveaus Schwingungen des Moleküls.

| Stoff | $\lambda$ in µ m | Leistung in W | Anwendung |
|---|---|---|---|
| Helium-Neon$^*$ (Gas) | 0,63; 1,15; 3,39 | 0,01 bis 0,1 | Lichtzeiger, Längenmessung, Kurzstreckenübertragung |
| CO$_2$ (Gas) | 9,6; 10,6 | 1 bis 1000, selten $10^{6}$ | Materialbearbeitung |
| Nd$^{3+}$ in YAG | 1,064; 1,32 | bis 1000 | Nachrichten- und Messtechnik |
| Nd$^{3+}$ in Glas | 1,06 | bis 1000 | Messtechnik |
| Rubin (Cr$^{3+}$ in Al$_2$O$_3$) | 0,69 | 1 bis 10 | Messtechnik |
| Erbium in Glas | 1,55 | $10^{-3}$ | Glasfaserverstärker |

$^*$Heute weitgehend durch Halbleiterlaser ersetzt. Nd ist Neodym, YAG Yttrium-Aluminium-Granat.

:::frage Woher kommt das erste Photon, wenn gar kein Licht eingestrahlt wird?
Aus der spontanen Emission. Die wenigen Photonen, die zufällig längs der Achse fliegen, wachsen bei Umkehr exponentiell, bis die stimulierte Emission $N_2-N_1$ so weit abbaut, dass Gewinn und Verlust je Umlauf gleich sind.
:::

:::aufgabe Aufgabe 6 ★★★ Ein Verstärker mit drei Niveaus
<span class="anker" id="aufg-6"></span>

Benutze das Rechenmodell mit Variante 2.

<ol class="al">

<li>

Ab welchem $r_\mathrm P$ herrscht Umkehr? Welche Pumpleistung je cm$^3$ braucht man dort ($N_1=N/2$)?

</li>

<li>

Berechne für $r_\mathrm P=3000\,\mathrm{s^{-1}}$ die Pumpleistung und den Faktor, um den der Stab verstärkt.

</li>

<li>

Ein anderer Stoff arbeitet nach Variante 1, mit $\tau_{32}=5$ µ s und $\tau_{21}=50$ µ s. Was geschieht?

</li>

</ol>

:::loesung
(a) $r_\mathrm P=1/\tau_{21}=1000\,\mathrm{s^{-1}}$. Je cm$^3$ und Sekunde werden $r_\mathrm PN_1=5\cdot10^{21}$ Elektronen gepumpt, jedes mit 2,40 eV. Das sind 1,9 kW/cm$^3$. (b) $N_1=N/4$ ergibt $3000\,\mathrm{s^{-1}}\cdot2{,}5\cdot10^{18}\,\mathrm{cm^{-3}}\cdot2{,}40\,\mathrm{eV}=2{,}9$ kW/cm$^3$. Mit $N_2-N_1=N/2$ ist $\alpha_\mathrm P=-0{,}15\,\mathrm{cm^{-1}}$, der Stab verstärkt um $\mathrm{e}^{1{,}5}=4{,}48$. (c) Nach [(5.1)](#gl-5-1) ist $N_2/N_3=50/5=10$. Elektronen stauen sich auf $E_2$, das Ziel ist besetzt, und es gibt keine Umkehr.
:::
:::

:::aufgabe Aufgabe 7 ★★ Eine Laserdiode
<span class="anker" id="aufg-7"></span>

Verstärkung verlangt [(5.2)](#gl-5-2) mit $E_\mathrm{Fn}-E_\mathrm{Fp}=eU_\mathrm{pn}$. Der Stoff sei GaAs, $E_\mathrm g=1{,}42$ eV.

<ol class="al">

<li>

Welche Spannung ist mindestens nötig, welche Wellenlänge entsteht?

</li>

<li>

Die Diode nimmt 30 mA bei 1,6 V auf. Jedes Paar aus Elektron und Loch liefert höchstens ein Photon. Wie groß sind Lichtleistung und Wirkungsgrad höchstens?

</li>

<li>

Warum scheitert derselbe Aufbau mit Silizium?

</li>

</ol>

:::loesung
(a) Mehr als 1,42 V, die Wellenlänge ist $1240\,\mathrm{eV\,nm}/1{,}42\,\mathrm{eV}=873$ nm. (b) $I/e=1{,}87\cdot10^{17}$ Paare je Sekunde mit je 1,42 eV ergeben $30\,\mathrm{mA}\cdot1{,}42\,\mathrm{V}=42{,}6$ mW. Aufgenommen werden 48 mW, also höchstens $1{,}42/1{,}6=89$ %. (c) Die Lücke ist indirekt ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)). Ein Phonon muss mitwirken, das ist selten, und die Energie geht vorher strahlungslos verloren ([Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html)).
:::
:::
