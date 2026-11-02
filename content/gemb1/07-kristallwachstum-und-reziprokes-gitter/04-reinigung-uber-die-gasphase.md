---
title: Stufe 2: Reinigung über die Gasphase
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
order: 4170400
summary: Rohsilizium ist ein Feststoff voller Fremdatome.
tags: Trichlorsilan, polykristallines Silizium
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Rohsilizium ist ein Feststoff voller Fremdatome. Diese Stufe zeigt, wie der Faktor $10^9$ gelingt: über eine Flüssigkeit, die sich destillieren lässt.
:::

**Die Idee.** Aus einem Feststoff bekommt man Fremdatome kaum heraus, sie sitzen fest zwischen den Siliziumatomen. Also verwandelt man das Silizium in eine leicht flüchtige Flüssigkeit, das __Trichlorsilan__, SiHCl$_3$, reinigt sie und holt das Silizium danach wieder heraus. Der Trick: Auch jedes Fremdatom bildet eine Chlorverbindung, und jede hat ihre eigene Siedetemperatur. Am Ende steht __polykristallines Silizium__ (Polysilizium): hochrein, aber aus vielen kleinen Kristalliten.

**Schritt 1: Trichlorsilan bilden.** Gemahlenes Rohsilizium reagiert in einem Reaktor bei rund 300 °C mit Chlorwasserstoff:

<span class="anker" id="gl-2-1"></span>
$$\mathrm{Si}+3\,\mathrm{HCl}\;\longrightarrow\;\mathrm{SiHCl_3}+\mathrm{H_2}. \tag{2.1}$$

Die Fremdatome werden dabei zu Chloriden. Ein Staubfilter hält Feststoffe zurück. Beim Abkühlen kondensieren die Chloride, der Wasserstoff bleibt gasförmig und wird abgeführt.

**Schritt 2: Destillieren.** Erhitzt man ein Flüssigkeitsgemisch, verdampft bevorzugt der Stoff mit der tieferen Siedetemperatur. Verflüssigt man den Dampf und wiederholt das in vielen Stufen, trennen sich die Stoffe. Das heißt fraktionierte Destillation. SiHCl$_3$ siedet bei 31,8 °C (Abb. [2](#abb-2)). Bis zu den nächsten schwerer siedenden Chloriden sind es über 40 K, bis BCl$_3$ knapp 20 K. Das reicht für eine sehr genaue Trennung.

:::abbildung gemb1/k7siede 2
Links: Siedetemperaturen bei Normaldruck. Rot das Trichlorsilan, blau die Chloride der Fremdatome. Rechts: Abscheidung im Reaktor. Strom heizt den dünnen Siliziumstab, nur an seiner heißen Oberfläche zerfällt das Gas.
:::

**Schritt 3: Silizium abscheiden.** Das reine SiHCl$_3$ strömt mit Wasserstoff in eine Quarzglocke. Darin heizt elektrischer Strom einen dünnen Siliziumstab auf 1000 bis 1150 °C. Nur an dieser heißen Oberfläche zerfällt das Gas, also nur am Stab:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
$$\begin{aligned} \mathrm{SiHCl_3}+\mathrm{H_2}&\;\longrightarrow\;\mathrm{Si}+3\,\mathrm{HCl},\\ 2\,\mathrm{SiHCl_3}&\;\longrightarrow\;\mathrm{Si}+\mathrm{SiCl_4}+2\,\mathrm{HCl},\\ 4\,\mathrm{SiHCl_3}&\;\longrightarrow\;\mathrm{Si}+3\,\mathrm{SiCl_4}+2\,\mathrm{H_2}. \end{aligned} \tag{2.2|2.3|2.4}$$

Der Stab wird dicker. Weil das Silizium nur Gas und den eigenen Stab berührt, nimmt es keine neuen Fremdatome auf. Das Verfahren wurde 1954 von Siemens patentiert, die Weltproduktion liegt über 20 000 t im Jahr.

⁠**So liest man das:** [(2.2)](#gl-2-2) ist die Umkehrung von [(2.1)](#gl-2-1). Die Temperatur entscheidet die Richtung: Bei 300 °C entsteht SiHCl$_3$, über 1000 °C zerfällt es. Nach [(2.2)](#gl-2-2) wird jedes SiHCl$_3$ zu Silizium, nach [(2.3)](#gl-2-3) jedes zweite, nach [(2.4)](#gl-2-4) jedes vierte, der Rest bleibt als SiCl$_4$ zurück. Der zugeführte Wasserstoff begünstigt [(2.2)](#gl-2-2). Das Ergebnis ist polykristallin, weil das Gas die Atome an vielen Stellen zugleich absetzt: Viele Keime wachsen nebeneinander, jeder mit eigener Gitterrichtung.

**Beispiel.** Ein Stab mit 150 mm Durchmesser und 2 m Länge enthält 82 kg Silizium. Nach [(2.2)](#gl-2-2) allein sind dafür 397 kg SiHCl$_3$ nötig. **Grenzfall:** Ohne Wasserstoff bleibt [(2.2)](#gl-2-2) aus, und höchstens die Hälfte des Siliziums landet im Stab.

:::frage Warum destilliert man nicht gleich das Silizium?
Silizium siedet erst weit über 3000 °C. Dort gibt jeder Behälter selbst Fremdatome ab. Der Umweg über SiHCl$_3$ verschiebt die Trennung auf rund 30 °C, wo sie sauber gelingt.
:::

:::aufgabe Aufgabe 2 ★★ Destillieren und Abscheiden
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Ein Gemisch aller Stoffe aus Abb. [2](#abb-2) wird auf 50 °C gehalten. Was verdampft, was bleibt flüssig? Wie trennst du danach SiHCl$_3$ von dem, was mitverdampft ist?

</li>

<li>

Bei welchem Stoff ist die Trennung am schwierigsten? SiCl$_4$ siedet bei 57 °C. Ist es leichter oder schwerer abzutrennen?

</li>

<li>

100 mol SiHCl$_3$ reagieren: 60 mol nach [(2.2)](#gl-2-2), 30 mol nach [(2.3)](#gl-2-3), 10 mol nach [(2.4)](#gl-2-4). Wie viel Silizium und SiCl$_4$ entstehen? Prüfe die Siliziumbilanz.

</li>

</ol>

:::loesung
(a) Bei 50 °C verdampfen BCl$_3$ und SiHCl$_3$, alle anderen bleiben flüssig. Der Dampf wird kondensiert und erneut destilliert, nun bei rund 20 °C: SiHCl$_3$ bleibt flüssig, BCl$_3$ geht weg. (b) Am schwierigsten ist BCl$_3$ mit 19,8 K Abstand. SiCl$_4$ liegt 25,2 K darüber, also etwas leichter als BCl$_3$, aber schwerer als CCl$_4$ und PCl$_3$ mit 44,2 K. (c) Silizium: $60+30/2+10/4=77{,}5$ mol. SiCl$_4$: $30/2+3\cdot10/4=22{,}5$ mol. Summe 100 mol, die Bilanz stimmt.
:::
:::
