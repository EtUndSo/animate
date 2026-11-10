---
title: Stufe 1: Warum man Zustände zählt
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung
knoten: Kapitel 10: Zustandsdichte und Fermi-Verteilung
order: 4200300
summary: Die Bandstruktur nennt erlaubte Energien, aber nicht, wie viele Ladungsträger ein Stück Material enthält.
tags: Besetzungswahrscheinlichkeit
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die Bandstruktur nennt erlaubte Energien, aber nicht, wie viele Ladungsträger ein Stück Material enthält. Diese Stufe zerlegt die Frage in zwei Teile und löst den ersten für eine Kette.
:::

**Die Idee.** Die Zahl der Elektronen folgt nicht aus einem einzelnen Zustand. Man muss alle Zustände durchgehen und fragen, ob der Platz besetzt ist. Darin stecken zwei Fragen: Wie viele Plätze gibt es bei jeder Energie? Mit welcher Wahrscheinlichkeit ist ein Platz dieser Energie besetzt? Die erste beantwortet allein die Bandstruktur. Die Plätze zählt man auf der $k$-Achse, denn dort liegen sie gleichmäßig. Auf der Energieachse liegen sie ungleichmäßig (Abb. [1](#abb-1)): Wo die Kurve $E(k)$ flach ist, fallen viele $k$-Werte in dasselbe Energiefenster.

:::analogie
Ein Stadion hat Sitzreihen. Der Bauplan nennt die Sitze je Reihe, die Belegung, wie oft ein Sitz genommen ist. Zuschauer sind Sitze mal Belegung über alle Reihen. Reihen sind Energien, Sitze Plätze. Das Bild endet beim Ort: Ein Platz gehört dem ganzen Kristall.
:::

:::definition Definition 1.1 (Ladungsträgerdichte)
<span class="anker" id="satz-1-1"></span>

In einer Kette der Länge $L$ ist die Dichte der Elektronen

<span class="anker" id="gl-1-1"></span>
$$n=\frac2L\sum_kf\bigl(E(k)\bigr). \tag{1.1}$$

Die Summe läuft über alle erlaubten $k$, die 2 zählt die Spinrichtungen. $f(E)$ ist die __Besetzungswahrscheinlichkeit__: die Wahrscheinlichkeit, dass ein Platz der Energie $E$ besetzt ist.
:::

**Von der Summe zum Integral.** Die erlaubten $k$ liegen im Abstand $\Delta k=2\pi/L$. Im Stück $\mathrm{d} k$ der Achse liegen also $L\,\mathrm{d} k/(2\pi)$ Werte. Ändert sich $f$ von einem Wert zum nächsten kaum, wird die Summe zum Integral, und $L$ fällt heraus: $n=(1/\pi)\int\mathrm{d} k\,f(E(k))$. Da $f$ nur von $E$ abhängt, sortiert man nach Energie um. Zu jeder Energie gehören $+k$ und $-k$, und ins Fenster $\mathrm{d} E$ fällt auf jeder Seite das Stück $\mathrm{d} k=\mathrm{d} E/|\mathrm{d} E/\mathrm{d} k|$.

:::satz Satz 1.2 (Zustandsdichte einer Kette)
<span class="anker" id="satz-1-2"></span>

Mit $\mathrm{d} Z=2\cdot L\,\mathrm{d} k/(2\pi)$ gilt

<span class="anker" id="gl-1-2"></span>
$$n=\int\mathrm{d} E\,D(E)\,f(E),\qquad D(E)=\frac2L\frac{\mathrm{d} Z}{\mathrm{d} E}=\frac2\pi\Bigl|\frac{\mathrm{d} k}{\mathrm{d} E}\Bigr|. \tag{1.2}$$

Für die Parabel $E=V_0+\hbar^2k^2/(2m^*)$ folgt mit $k=\sqrt{2m^*(E-V_0)}/\hbar$

<span class="anker" id="gl-1-3"></span>
$$D(E)=\frac1{\pi\hbar}\sqrt{\frac{2m^*}{E-V_0}}=\frac2h\sqrt{\frac{2m^*}{E-V_0}}\ \propto\ (E-V_0)^{-1/2}. \tag{1.3}$$
:::

⁠**So liest man das:** $D(E)\,\mathrm{d} E$ ist die Zahl der Plätze je Länge im Fenster $\mathrm{d} E$, Einheit $1/(\mathrm{eV\,cm})$. Die erste 2 in [(1.2)](#gl-1-2) ist der Spin, die zweite steckt in $\mathrm{d} Z$ und zählt $\pm k$. $D$ ist also keine neue Physik, sondern dieselbe Zählung, nach Energie statt nach $k$ sortiert. Mit der Geschwindigkeit $v=\hbar^{-1}\mathrm{d} E/\mathrm{d} k$ aus [Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) ist $D=2/(\pi\hbar|v|)$: Wo die Elektronen langsam sind, ist die Kurve flach und die Dichte hoch. **Gültigkeit:** $D$ ist ein Mittelwert über viele Niveaus. Das ist erlaubt, wenn ihr Abstand klein gegen $k_\mathrm BT$ ist. In 1 cm Silizium ist $\Delta k=6{,}3\cdot10^{-7}\,\mathrm{nm^{-1}}$, und zwei Nachbarniveaus bei $E_\mathrm C+k_\mathrm BT$ trennen $4\cdot10^{-8}$ eV, nur $1{,}5\cdot10^{-6}\,k_\mathrm BT$.

:::abbildung gemb1/k10band 1
Links das Kosinus-Band des Rechenmodells, Punkte auf der $k$-Achse: erlaubte Werte, schematisch weit auseinander. Zwei gleich breite Energiefenster schneiden unten ein langes, in der Mitte ein kurzes $k$-Stück aus. Rechts die Zustandsdichte: blau das Kosinus-Band, rot gestrichelt die Parabel. Beide Bandränder sind flach, also ist $D$ dort groß.
:::

::::beispiel
Für die Kette des Rechenmodells ist $E(k)=2t_0(1-\cos(ka))$ ([Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)), und aus [(1.2)](#gl-1-2) folgt

<span class="anker" id="gl-1-4"></span>
$$D(E)=\frac{2}{\pi a\sqrt{E\,(4t_0-E)}},\qquad0<E<4t_0. \tag{1.4}$$

Bei $E=0{,}2$ eV sind das 4,24 Plätze je eV und nm, die Parabel [(1.3)](#gl-1-3) gibt 4,03. Eine Kette mit $10^4$ Atomen ist $L=2{,}5$ µ m lang. Zählt man die $k$-Werte von Hand, liegen im Fenster von 0,19 bis 0,21 eV genau 106, also 212 Plätze, und $L\,D\,\Delta E=212{,}2$. In der Bandmitte $E=1$ eV ist $D=2{,}55$ je eV und nm, die Parabel taugt dort nicht mehr.
::::

⁠**Grenzfall:** Ist jeder Platz besetzt, also $f=1$, ergibt [(1.4)](#gl-1-4) $n=\int_0^{4t_0}D\,\mathrm{d} E=2/a$. Das sind die zwei Plätze je Atom aus [Kapitel 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html).

:::frage Warum liegen die Plätze auf der $k$-Achse gleichmäßig und auf der Energieachse nicht?
Die Randbedingung legt $k$ fest: Eine ganze Zahl von Wellenlängen muss auf $L$ passen, und das ergibt gleiche Schritte $2\pi/L$. Die Energie ist eine gekrümmte Funktion von $k$. Gleiche Schritte auf der einen Achse werden deshalb ungleiche auf der anderen.
:::

:::aufgabe Aufgabe 1 ★ Eine Kette auszählen
<span class="anker" id="aufg-1"></span>

Eine Kette hat 2000 Atome mit $a=0{,}3$ nm und $t_0=0{,}8$ eV.

<ol class="al">

<li>

Berechne $L$, $\Delta k$, die Zahl der Plätze im Band und $m^*$ am unteren Rand.

</li>

<li>

Berechne $D(0{,}3\,\mathrm{eV})$ aus [(1.3)](#gl-1-3) und aus [(1.4)](#gl-1-4). Wie groß ist der Unterschied?

</li>

<li>

Wie viele Plätze liegen zwischen 0,29 und 0,31 eV?

</li>

</ol>

:::loesung
(a) $L=600$ nm, $\Delta k=2\pi/L=0{,}0105\,\mathrm{nm^{-1}}$, 4000 Plätze, $m^*=\hbar^2/(2t_0a^2)=0{,}529\,m_0$. (b) Parabel: $2{,}17$ je eV und nm. Kosinus: $2{,}28$ je eV und nm. Die Parabel liegt 4,8 % zu tief, denn das Band ist schon flacher als sie. (c) $L\,D\,\Delta E=27{,}3$. Das Auszählen ergibt 14 $k$-Werte, also 28 Plätze.
:::
:::
