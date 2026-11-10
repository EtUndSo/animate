---
title: Stufe 1: Vom Quarz zum Rohsilizium
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallwachstum-und-reziprokes-gitter
knoten: Kapitel 7: Kristallwachstum und reziprokes Gitter
order: 4170300
summary: Silizium kommt in der Natur nur an Sauerstoff gebunden vor.
tags: Metallurgisches Silizium
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Silizium kommt in der Natur nur an Sauerstoff gebunden vor. Diese Stufe trennt die beiden und zeigt, was das kostet und was es noch nicht leistet.
:::

**Die Idee.** Ausgangsstoff ist Quarz oder Quarzsand, SiO$_2$. Die Bindung zwischen Silizium und Sauerstoff ist so fest, dass man dem Sauerstoff einen besseren Partner anbieten muss, und dazu sehr viel Wärme. Beides liefert ein elektrischer Ofen: Ein Lichtbogen, also eine stromführende Gasentladung, brennt in einem Gemenge aus Quarz und Koks, fast reinem Kohlenstoff. Der Kohlenstoff nimmt dem Silizium den Sauerstoff weg und verlässt den Ofen als Gas. Weil das Gas entweicht, kann die Reaktion nicht zurücklaufen. Unten sammelt sich flüssiges Silizium (Abb. [1](#abb-1)).

:::definition Definition 1.1 (Metallurgisches Silizium)
<span class="anker" id="satz-1-1"></span>

__Metallurgisches Silizium__ (Rohsilizium) entsteht nach der Gesamtreaktion

<span class="anker" id="gl-1-1"></span>
$$\mathrm{SiO_2}+2\,\mathrm C\;\longrightarrow\;\mathrm{Si}+2\,\mathrm{CO}. \tag{1.1}$$

Der Energieaufwand beträgt 12,5 bis 14 MWh je 1000 kg Silizium. Das Produkt enthält noch 2 bis 4 % Fremdatome.
:::

⁠**So liest man das:** Eine Reaktionsgleichung zählt Teilchen. Ein Mol SiO$_2$ (60,09 g) und zwei Mol Kohlenstoff (24,02 g) ergeben 28,09 g Silizium und 56,02 g Kohlenmonoxid, beide Seiten also 84,11 g. 1000 kg Silizium verlangen 2139 kg Quarz und 855 kg Kohlenstoff und liefern 1994 kg CO.

**Was im Ofen geschieht.** [(1.1)](#gl-1-1) ist nur die Bilanz. Wirklich laufen je nach Temperatur vier Teilreaktionen ab:

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} \mathrm{SiO_2}+\mathrm C&\;\longrightarrow\;\mathrm{SiO}+\mathrm{CO}&&\text{bei 1700 bis 1900\,°C},\\ \mathrm{SiO}+2\,\mathrm C&\;\longrightarrow\;\mathrm{SiC}+\mathrm{CO}&&\text{bei 1500 bis 1700\,°C},\\ \mathrm{SiO_2}+\mathrm{SiC}&\;\longrightarrow\;\mathrm{Si}+\mathrm{SiO}+\mathrm{CO}&&\text{über 2000\,°C},\\ \mathrm{SiO}+\mathrm{CO}&\;\longrightarrow\;\mathrm{SiO_2}+\mathrm C&&\text{unter 1500\,°C}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$

:::abbildung gemb1/k7ofen 1
Schema des Lichtbogenofens. Am Lichtbogen unten ist es am heißesten. Gase (blau) steigen in kühlere Zonen, Festes (rot) sinkt in heißere. Rechts die Reaktion jeder Zone.
:::

Der Mechanismus ist ein Kreislauf. SiO ist ein Gas und steigt vom Lichtbogen auf. In kühleren Schichten fängt der Kohlenstoff es ein [(1.3)](#gl-1-3), oder es zerfällt wieder [(1.5)](#gl-1-5). Beides ergibt Feststoffe, die mit dem Gemenge nach unten sinken. Im heißesten Bereich entsteht aus SiC und SiO$_2$ das Silizium [(1.4)](#gl-1-4). So geht kaum Silizium als Gas verloren. **Grenzfall:** Wäre der Ofen überall unter 1500 °C, liefe nur [(1.5)](#gl-1-5), und kein Silizium entstünde.

::::beispiel
13 MWh je 1000 kg sind 46,8 MJ/kg, also 13,6 eV je Siliziumatom. Eine chemische Bindung trägt einige eV. Hier sind je Atom mehrere Bindungen zum Sauerstoff zu lösen, und der Ofen verliert zusätzlich Wärme.
::::

**Warum das nicht reicht.** Für genau festgelegte Halbleitereigenschaften sind Einkristallinität und chemische Reinheit unverzichtbar, etwa für die Beweglichkeit (wie leicht Ladungsträger im Feld driften) und die Lebensdauer (wie lange ein beweglicher Ladungsträger besteht, bis er eingefangen wird). Der Mechanismus: Ein Gitterfehler oder Fremdatom stört die Periodizität, Elektronen werden dort gestreut oder festgehalten. Gitterfehler und Fremdatomgehalt müssen deshalb genau kontrolliert werden. Rohsilizium muss um den Faktor $10^9$ reiner werden. Aus 3 % werden $3\cdot10^{-11}$, ein Fremdatom auf $3\cdot10^{10}$ Siliziumatome. Das sind noch $1{,}5\cdot10^{12}$ Fremdatome je cm$^3$, im Mittel 0,87 µm oder 1600 Gitterkonstanten voneinander entfernt.

:::frage Warum entsteht CO und nicht das stabilere CO$_2$?
Bei niedrigen Temperaturen wäre CO$_2$ bevorzugt. Über rund 1000 °C reagiert CO$_2$ aber mit Kohlenstoff zu CO, und Kohlenstoff liegt im Ofen überall vor. Deshalb braucht jedes Siliziumatom zwei Kohlenstoffatome.
:::

:::aufgabe Aufgabe 1 ★ Bilanz eines Ofens
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Ein Ofen soll 250 kg Silizium liefern. Wie viel Quarz und Kohlenstoff braucht er, wie viel CO entsteht?

</li>

<li>

Zeige, dass die Summe der vier Teilreaktionen die Gesamtreaktion [(1.1)](#gl-1-1) ergibt. Welche Stoffe heben sich weg?

</li>

<li>

Ein Ofen nimmt dauerhaft 20 MW auf und braucht 13 MWh je 1000 kg. Wie viel Silizium liefert er am Tag?

</li>

</ol>

:::loesung
(a) 250 kg sind 8,90 kmol. Also 535 kg Quarz, 214 kg Kohlenstoff, 499 kg CO. (b) Links stehen $2\,\mathrm{SiO_2}+3\,\mathrm C+2\,\mathrm{SiO}+\mathrm{SiC}+\mathrm{CO}$, rechts $2\,\mathrm{SiO}+3\,\mathrm{CO}+\mathrm{SiC}+\mathrm{Si}+\mathrm{SiO_2}+\mathrm C$. SiO und SiC heben sich ganz weg, je eines von SiO$_2$, C und CO ebenfalls. Es bleibt $\mathrm{SiO_2}+2\,\mathrm C\to\mathrm{Si}+2\,\mathrm{CO}$. (c) $20\,\mathrm{MW}\cdot24\,\mathrm{h}=480$ MWh, geteilt durch 13 MWh je 1000 kg ergibt 36,9 t am Tag.
:::
:::
