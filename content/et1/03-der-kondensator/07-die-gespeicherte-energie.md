---
title: Stufe 6: Die gespeicherte Energie
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Kondensator
order: 1130700
summary: Laden kostet Energie, denn jede weitere Ladung muss gegen die schon vorhandene Spannung laufen.
tags: Energiedichte
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Laden kostet Energie, denn jede weitere Ladung muss gegen die schon vorhandene Spannung laufen. Diese Stufe berechnet, wie viel es ist und wo die Energie danach steckt.
:::

**Die Idee.** Spannung ist Energie je Ladung ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Bringt man die kleine Ladung $\Delta q$ von der negativen auf die positive Platte, kostet das $\Delta W=u\,\Delta q$. Die ersten Ladungen kosten fast nichts, weil noch kein Feld da ist. Die letzten kosten den vollen Betrag $U$ je Coulomb. Im Mittel zahlt jede Ladung $U/2$. Das ist die Fläche unter der Geraden $u=q/C$ (Abb. [6](#abb-6) links).

:::satz Satz 6.1 (Energie im Kondensator)
<span class="anker" id="satz-6-1"></span>

Ein Kondensator mit der Ladung $Q$ und der Spannung $U$ speichert

<span class="anker" id="gl-6-1"></span>
$$W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}=\frac12\,Q\,U=\frac12\,C\,U^2. \tag{6.1}$$

Sie steckt im Feld zwischen den Platten. Beim Plattenkondensator gilt mit dem Volumen $V=A\,d$

<span class="anker" id="gl-6-2"></span>
$$W=\frac12\,\varepsilon\,E^2\cdot A\,d,\qquad w=\frac WV=\frac12\,\varepsilon\,E^2. \tag{6.2}$$

Dabei ist $w$ die __Energiedichte__, die Energie je Volumen.
:::

⁠**So liest man das:** $W$ in J, $C$ in F, $U$ in V, $w$ in J/m$^3$. Die Spannung geht im Quadrat ein: Doppelte Spannung bedeutet doppelte Ladung, und die läuft gegen die doppelte Spannung. $q$ ist die Ladung während des Ladens, $Q$ ihr Endwert. **Gültigkeit:** $C$ konstant, kein Leckstrom.

:::herleitung Energie aus Kraft und Weg
Die Kraft auf $\Delta q$ im Feld ist $F=\Delta q\,E$ ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Über den Abstand $\Delta s$ zwischen den Platten kostet das $\Delta W=F\,\Delta s=\Delta q\,E\,\Delta s$. Mit $E\,\Delta s=u$ folgt $\Delta W=\Delta q\,u$, und mit $u=q/C$ ist $\Delta W=\frac qC\,\Delta q$. Die Summe aller Portionen wird für kleine $\Delta q$ zum Integral [(6.1)](#gl-6-1).

Dasselbe Ergebnis liefert die Schaltungsseite. Die Leistung (Energie je Zeit) ist $p=u\,i$ ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Mit $i=C\,\mathrm{d} u/\mathrm{d} t$ wird $W=\int u\,i\,\mathrm{d} t=C\int_0^Uu\,\mathrm{d} u=\frac12CU^2$.

⁠**Vom Bauteil zum Feld:** Einsetzen von $C=\varepsilon A/d$ und $U=E\,d$ in [(6.1)](#gl-6-1) ergibt [(6.2)](#gl-6-2).
:::

:::abbildung et1/k3energie 6
Links: Sechs Portionen zu je 150 µC. Jede Portion kostet $u\,\Delta q$, ihre Spannung ist die in der Mitte der Portion. Die Fläche aller Balken ist die Fläche des Dreiecks unter $u=q/C$, also $W=\frac12QU=4{,}05$ mJ. Rechts: Die Energie steckt im Raum zwischen den Platten, je Volumen $w=\frac12\varepsilon E^2$. Im Metall ist $E=0$.
:::

**Wo die Energie steckt.** Das Metall kann sie nicht enthalten, denn dort ist $E=0$ und die Elektronen sind nur eine Winzigkeit verschoben (Stufe [2](die-kapazitat.html#stufe-2)). Gleichung [(6.2)](#gl-6-2) sagt: Jeder Kubikmeter Feld enthält $\frac12\varepsilon E^2$. Dass das mehr ist als eine Rechenweise, zeigt ein Versuch. Man trennt die Batterie ab und zieht die Platten auseinander. $Q$ bleibt, also auch $E=Q/(\varepsilon A)$. Das Feld füllt aber mehr Volumen, die Feldenergie wächst um $\frac12\varepsilon E^2A\,\Delta d$. Die Energie kommt von der Hand, die gegen die Anziehung der Platten zieht. Jede Platte spürt nur das Feld der anderen, das ist die Hälfte von $E$, also $F=\frac12QE$. Die Arbeit ist $F\,\Delta d=\frac12QE\,\Delta d=\frac12\varepsilon E^2A\,\Delta d$, genau der Zuwachs. Dass Feldenergie unabhängig von Ladungen existiert, zeigt das Licht: Es trägt Energie durch den leeren Raum.

::::beispiel
Der Kondensator des RC-Kreises speichert bei 9 V $W=\frac12\cdot100\,\mu\text{F}\cdot(9\,\mathrm{V})^2=4{,}05$ mJ, das Plattenpaar nur 1,20 nJ. Dort ist $w=\frac12\varepsilon_0(3\,\mathrm{kV/m})^2=3{,}98\cdot10^{-5}$ J/m$^3$, mal $V=3\cdot10^{-5}\,\mathrm{m^3}$ ergibt dieselben 1,20 nJ. Ein Supercap mit 100 F speichert bei 2,7 V immerhin 365 J, eine 9-V-Blockbatterie mit 0,5 Ah aber 16 kJ, das Vier-Millionen-Fache des 100-µF-Kondensators. Kondensatoren speichern wenig Energie, geben sie aber sehr schnell ab, etwa im Kamerablitz.
::::

⁠**Grenzfall:** Für $U\to0$ geht $W\to0$, ohne Feld keine Energie. **Kontrolle:** $\mathrm{F\cdot V^2}=\frac{\mathrm{C}}{\mathrm V}\cdot\mathrm{V^2}=\mathrm{C\,V}=\mathrm J$.

:::frage Warum nicht $W=Q\,U$? Spannung mal Ladung ist doch Energie.
$Q\,U$ stimmt, wenn die ganze Ladung die volle Spannung durchläuft. Beim Laden ist $U$ aber der Endwert, die Spannung wächst von null an. Die Batterie gibt tatsächlich $Q\,U$ ab, denn durch sie läuft jede Ladung bei voller Spannung. Der Kondensator erhält nur die Hälfte. Wohin der Rest geht, klärt Aufgabe [11](aufladen-uber-einen-widerstand.html#aufg-11).
:::

:::aufgabe Aufgabe 7 ★★★ Platten auseinanderziehen
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Ein Kondensator mit 470 µF liegt an 12 V, dann an 24 V. Wie groß ist jeweils $W$?

</li>

<li>

Das Plattenpaar wird auf 9 V geladen und abgetrennt. Dann wird $d$ auf 6 mm verdoppelt. Wie groß sind $C$, $U$, $E$ und $W$? Prüfe den Zuwachs von $W$ mit $F\,\Delta d$.

</li>

<li>

Dasselbe, aber die Batterie bleibt angeschlossen. Nun sinkt $W$, obwohl die Hand Arbeit verrichtet. Wohin geht die Energie? Die mechanische Arbeit beträgt hier 0,60 nJ.

</li>

</ol>

:::loesung
(a) $W=\frac12\cdot470\,\mu\text{F}\cdot(12\,\mathrm{V})^2=33{,}8$ mJ, bei 24 V das Vierfache, 135 mJ.

(b) $Q=266$ pC bleibt. $C=14{,}8$ pF, $U=Q/C=18$ V, $E=U/d=3$ kV/m wie zuvor. $W=\frac12QU=2{,}39$ nJ, der Zuwachs beträgt 1,20 nJ. Die Kraft ist $F=\frac12QE=0{,}398\,\mu\text{N}$, und $F\,\Delta d=0{,}398\,\mu\text{N}\cdot3\,\mathrm{mm}=1{,}20$ nJ. Beides stimmt überein.

(c) $U=9$ V bleibt. $C=14{,}8$ pF, $Q=133$ pC, $E=1{,}5$ kV/m, $W=0{,}60$ nJ. Das Feld verliert 0,60 nJ. Dazu kommen 0,60 nJ von der Hand. Beides fließt in die Batterie, denn 133 pC laufen bei 9 V zurück: $133\,\mathrm{pC}\cdot9\,\mathrm{V}=1{,}20$ nJ. Die Batterie wird ein wenig geladen.
:::
:::
