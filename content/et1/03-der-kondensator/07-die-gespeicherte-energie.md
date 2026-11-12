---
title: Stufe 6: Die gespeicherte Energie
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130700
summary: Laden kostet Energie, denn jede weitere Ladung muss gegen die schon vorhandene Spannung laufen.
tags: Energiedichte
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Laden kostet Energie, denn jede weitere Ladung muss gegen die schon vorhandene Spannung laufen. Diese Stufe berechnet, wie viel es ist und wo die Energie danach steckt.
:::

**Die Idee.** Spannung ist Energie je Ladung ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Bringt man die kleine Ladung $\Delta q$ von der negativen auf die positive Platte, kostet das $\Delta W=u\,\Delta q$. Die ersten Ladungen kosten fast nichts, weil noch kein Feld da ist. Die letzten kosten den vollen Betrag $U$ je Coulomb. Im Mittel zahlt jede Ladung $U/2$. Das ist die Fläche unter der Geraden $u=q/C$ (Abb. [6](#abb-6) links).

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
Die Kraft auf $\Delta q$ im Feld ist $F=\Delta q\,E$ ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Über den Abstand $\Delta s$ zwischen den Platten kostet das $\Delta W=F\,\Delta s=\Delta q\,E\,\Delta s$. Mit $E\,\Delta s=u$ folgt $\Delta W=\Delta q\,u$, und mit $u=q/C$ ist $\Delta W=\frac qC\,\Delta q$. Die Summe aller Portionen wird für kleine $\Delta q$ zum Integral [(6.1)](#gl-6-1).

Dasselbe Ergebnis liefert die Schaltungsseite. Die Leistung (Energie je Zeit) ist $p=u\,i$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Mit $i=C\,\mathrm{d} u/\mathrm{d} t$ wird $W=\int u\,i\,\mathrm{d} t=C\int_0^Uu\,\mathrm{d} u=\frac12CU^2$.

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

::::formelsammlung
**Energie im Kondensator**

$$W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}=\frac12\,Q\,U=\frac12\,C\,U^2$$

$W$ in J; $q$ Ladung während des Ladens, $Q$ ihr Endwert. Jede weitere Ladung läuft gegen die schon vorhandene Spannung, im Mittel gegen $U/2$; die Spannung geht im Quadrat ein. Gilt für konstantes $C$ ohne Leckstrom.

**Energie aus der Leistung**

$$W=\int u\,i\,\mathrm{d} t=C\int_0^Uu\,\mathrm{d} u=\frac12CU^2$$

Dasselbe Ergebnis von der Schaltungsseite, mit $p=u\,i$ und $i=C\,\mathrm{d} u/\mathrm{d} t$.

**Energie und Energiedichte im Feld**

$$W=\frac12\,\varepsilon\,E^2\cdot A\,d,\qquad w=\frac WV=\frac12\,\varepsilon\,E^2$$

Plattenkondensator mit dem Volumen $V=A\,d$; $w$ in J/m$^3$. Die Energie steckt im Feld zwischen den Platten, im Metall ist $E=0$.

**Kraft zwischen den Platten**

$$F=\frac12QE$$

Jede Platte spürt nur das Feld der anderen, die Hälfte von $E$. Zieht man die Platten eines abgetrennten Kondensators um $\Delta d$ auseinander, verrichtet die Hand $\frac12\varepsilon E^2A\,\Delta d$, genau den Zuwachs der Feldenergie.
::::

::::lernkarten
:::karte formel Energie im Kondensator
Wie viel Energie speichert ein Kondensator mit der Ladung $Q$ und der Spannung $U$, und was setzt die Formel voraus?
---
$W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}=\frac12\,Q\,U=\frac12\,C\,U^2$, gespeichert im Feld zwischen den Platten. Vorausgesetzt sind ein konstantes $C$ und kein Leckstrom.
--- falsch
$W=Q\,U=C\,U^2$, weil jede Ladung die volle Spannung durchläuft; gespeichert im Feld zwischen den Platten. Vorausgesetzt sind ein konstantes $C$ und kein Leckstrom.
--- falsch
$W=\frac12\,C\,U$: Die Energie wächst proportional zur Spannung und steckt in den verschobenen Elektronen auf den Platten. Vorausgesetzt ist ein konstantes $C$.
--- falsch
$W=\frac12\,C\,U^2$, gespeichert im Metall der Platten, in den verschobenen Elektronen. Die Formel gilt auch, wenn $C$ sich mit der Spannung ändert.
:::
:::karte herleitung Energie aus Kraft und Weg
Leite aus der Kraft auf eine kleine Ladung $\Delta q$ im Feld her, dass ein Kondensator die Energie $W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}$ speichert.
---
Die Kraft auf $\Delta q$ im Feld ist $F=\Delta q\,E$, weil die Feldstärke die Kraft je Ladung ist.
---
Über den Abstand $\Delta s$ zwischen den Platten kostet das $\Delta W=F\,\Delta s=\Delta q\,E\,\Delta s$, weil Arbeit Kraft mal Weg in Kraftrichtung ist.
---
Mit $E\,\Delta s=u$ folgt $\Delta W=\Delta q\,u$ und mit $u=q/C$ dann $\Delta W=\frac qC\,\Delta q$, weil die Spannung von der schon getrennten Ladung $q$ abhängt.
---
Für kleine $\Delta q$ wird die Summe aller Portionen zum Integral $W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}$, weil die Fläche unter der Geraden $u=q/C$ ein Dreieck ist.
:::
:::karte zusammenhang Der Faktor ein Halb
Warum speichert ein Kondensator nur $\frac12\,Q\,U$ und nicht $Q\,U$, obwohl Spannung mal Ladung eine Energie ist?
---
Weil die Spannung beim Laden von null an wächst: Die ersten Ladungen kosten fast nichts, die letzten $U$ je Coulomb, im Mittel zahlt jede $U/2$. Nur die Batterie gibt $Q\,U$ ab.
--- falsch
Weil die Hälfte der Ladung beim Laden durch das Dielektrikum verloren geht und nie auf der Gegenplatte ankommt; ohne diesen Verlust speicherte der Kondensator die vollen $Q\,U$.
--- falsch
Weil nur die positive Platte Energie speichert; die negative trägt nichts bei, weil ihre Ladung negativ ist und sich mit der positiven aufhebt. Deshalb zählt nur eine der beiden Platten.
--- falsch
Weil auch die Batterie nur $\frac12\,Q\,U$ abgibt; die andere Hälfte ihrer Energie bleibt in ihr, da sie beim Laden gegen den Kondensator arbeiten muss und dabei Spannung verliert.
:::
:::karte begriff Energiedichte und Feldenergie
Was gibt die Energiedichte $w$ im Feld eines Kondensators an, und wie groß ist sie?
---
Die Energie je Volumen, $w=\frac WV=\frac12\,\varepsilon\,E^2$, in J/m$^3$. Sie sagt, wo die Feldenergie steckt: Jeder Kubikmeter Feld zwischen den Platten enthält $\frac12\varepsilon E^2$.
--- falsch
Die Energie je Plattenfläche, $w=\frac12\,\varepsilon\,E^2$, in J/m$^2$. Sie sagt, wie viel Energie in den Metallplatten selbst steckt, je Quadratmeter Platte.
--- falsch
Die Energie je Volumen, $w=\varepsilon\,E$, in J/m$^3$. Sie wächst linear mit der Feldstärke, weil jede Feldlinie dieselbe Energie trägt, gleich wo sie zwischen den Platten verläuft.
--- falsch
Die Energie je Ladung, $w=W/Q$, in J/C. Sie sagt, wie viel Energie jedes Elektron auf der negativen Platte mitbringt, wenn der Kondensator geladen ist.
:::
:::karte herleitung Vom Bauteil zum Feld
Leite aus $W=\frac12CU^2$ die Energiedichte $w=\frac WV=\frac12\,\varepsilon\,E^2$ im Plattenkondensator her.
---
Einsetzen von $C=\varepsilon A/d$ ist erlaubt, weil die Platten mit dem Dielektrikum einen Plattenkondensator bilden.
---
Einsetzen von $U=E\,d$ ist erlaubt, weil das Feld zwischen den Platten überall gleich ist.
---
Das ergibt $W=\frac12\,\varepsilon\,E^2\cdot A\,d$, weil sich ein $d$ aus dem Nenner von $C$ gegen das Quadrat von $U$ kürzt.
---
Teilen durch das Volumen $V=A\,d$ ergibt $w=\frac WV=\frac12\,\varepsilon\,E^2$, weil die Energiedichte die Energie je Volumen ist.
:::
:::karte zusammenhang Wo die Energie steckt
Wo steckt die Energie eines geladenen Kondensators, und warum nicht im Metall der Platten?
---
Im Feld zwischen den Platten, je Volumen $\frac12\varepsilon E^2$. Im Metall ist $E=0$, und die Elektronen sind dort nur eine Winzigkeit verschoben.
--- falsch
In den verschobenen Elektronen auf den Platten; das Feld zwischen den Platten ist nur ein Rechenhilfsmittel und enthält selbst keine Energie.
--- falsch
Im Dielektrikum als Wärme; das Metall bleibt kalt, weil es Strom leitet und deshalb selbst keine Energie aufnehmen kann.
--- falsch
In der Batterie, die sie nur ausleiht; der Kondensator speichert selbst keine Energie, er hält nur die Spannung fest.
:::
:::karte zusammenhang Platten auseinanderziehen
Was geschieht mit der Feldenergie, wenn man die Platten eines abgetrennten, geladenen Kondensators auseinanderzieht, und woher kommt die Änderung?
---
Sie wächst um $\frac12\varepsilon E^2A\,\Delta d$: $Q$ und $E=Q/(\varepsilon A)$ bleiben, aber das Feld füllt mehr Volumen. Die Energie kommt von der Hand, die gegen die Anziehung $F=\frac12QE$ zieht.
--- falsch
Sie bleibt gleich, weil Ladung und Feldstärke beim Auseinanderziehen gleich bleiben; die Platten ziehen sich nicht an, und die Hand verrichtet deshalb keine Arbeit.
--- falsch
Sie sinkt, weil die Kapazität kleiner wird und nach $W=\frac12\,C\,U^2$ mit $C$ auch die Energie fällt; der Rest fließt als Arbeit in die Hand zurück.
--- falsch
Sie wächst, weil die Hand beim Ziehen Ladung von Platte zu Platte schiebt; die Anziehung zwischen den Platten beträgt dabei $F=Q\,E$.
:::
:::karte zusammenhang Kraft zwischen den Platten
Warum zieht eine geladene Platte die andere nur mit $F=\frac12QE$ an und nicht mit $Q\,E$?
---
Weil jede Platte nur das Feld der anderen Platte spürt, und das ist die Hälfte des Felds $E$ zwischen den Platten.
--- falsch
Weil die Hälfte der Ladung auf der Außenseite der Platte sitzt, wo kein Feld herrscht; nur die Innenseite spürt eine Kraft.
--- falsch
Weil das Dielektrikum die Hälfte des Felds abschirmt; ohne Dielektrikum, also in Luft, wäre die Kraft genau $Q\,E$.
--- falsch
Weil die Kraft beim Auseinanderziehen von $Q\,E$ auf null abnimmt und deshalb im Mittel $\frac12QE$ beträgt.
:::
:::karte zusammenhang Spannung im Quadrat
Warum geht die Spannung im Quadrat in die gespeicherte Energie ein?
---
Doppelte Spannung bedeutet doppelte Ladung, und diese doppelte Ladung läuft gegen die doppelte Spannung. Zusammen ergibt das die vierfache Energie.
--- falsch
Weil sich bei doppelter Spannung der Plattenabstand halbiert, da sich die Platten stärker anziehen, und das Feld zwischen ihnen dadurch viermal so stark wird.
--- falsch
Weil die Energie in beiden Platten getrennt gespeichert wird; jede der beiden Platten trägt dazu einen Faktor $U$ bei.
--- falsch
Weil doppelte Spannung die Ladung auf den Platten vervierfacht; die Energie selbst wächst dagegen nur linear mit der Ladung.
:::
:::karte zusammenhang Kondensator und Batterie
Wofür eignet sich ein Kondensator als Energiespeicher, verglichen mit einer Batterie?
---
Er speichert wenig Energie, eine 9-V-Blockbatterie das Vier-Millionen-Fache eines 100-µF-Kondensators bei 9 V. Dafür gibt er sie sehr schnell ab, etwa im Kamerablitz.
--- falsch
Er speichert mehr Energie als eine Batterie gleicher Größe, gibt sie aber nur langsam wieder ab; deshalb dient er vor allem als Langzeitspeicher, etwa in Uhren.
--- falsch
Er speichert etwa gleich viel Energie wie eine Batterie gleicher Größe, verliert sie aber innerhalb weniger Sekunden durch Selbstentladung.
--- falsch
Er speichert gar keine Energie, sondern nur Ladung; die Energie liefert beim Entladen immer eine Batterie, die an den Kreis angeschlossen ist.
:::
::::
