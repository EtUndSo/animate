---
title: Stufe 8: Ergänzung: Ionenkristalle und Modifikationen
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Kristallgitter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter
knoten: Kapitel 6: Kristallgitter
order: 4161000
summary: Kochsalz ist nur eine von mehreren Strukturen aus zwei Ionensorten.
tags: Perowskit-Struktur, Fluorit-Struktur, Modifikationen, Phasenumwandlung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Kochsalz ist nur eine von mehreren Strukturen aus zwei Ionensorten. Diese Stufe zeigt, wie das Größenverhältnis der Ionen die Struktur auswählt.
:::

**Die Idee.** Die meist größeren Anionen (negative Ionen) bilden ein Gerüst, die kleineren Kationen (positive Ionen) sitzen in dessen Lücken. Dieses Bild ist stabil, solange das Kation die Anionen ringsum berührt. Ist es zu klein für seine Lücke, sitzt es lose, die Anionen berühren sich und stoßen einander ab. Dann wählt der Kristall eine engere Lücke mit weniger Nachbarn. Das Verhältnis $r_+/r_-$ legt also die Struktur fest (Abb. [8](#abb-8)).

| $r_+/r_-$ | Struktur | Kation in | Nachbarn |
|---|---|---|---|
| 0,155 bis 0,225 | Bornitrid (BN) | Dreieckslücke | 3 |
| 0,225 bis 0,414 | ZnS | Tetraederlücke | 4 |
| 0,414 bis 0,732 | NaCl | Oktaederlücke | 6 |
| 0,732 bis 1,000 | CsCl | Würfellücke | 8 |
| über 1 | dichteste Packung | keine Lücke | 12 |

:::herleitung Die Grenzwerte
An der Grenze berühren sich die Anionen und zugleich Kation und Anionen. Bei der Oktaederlücke liegen vier Anionen im Quadrat um das Kation. Die Quadratdiagonale ist $\sqrt2\cdot2r_-=2r_-+2r_+$, also $r_+/r_-=\sqrt2-1=0{,}414$. Bei der Würfellücke gilt dasselbe längs der Raumdiagonale: $\sqrt3\cdot2r_-=2r_-+2r_+$, also $\sqrt3-1=0{,}732$. Bei der Tetraederlücke ergibt die Geometrie $\sqrt{3/2}-1=0{,}225$, bei der Dreieckslücke $2/\sqrt3-1=0{,}155$.
:::

:::abbildung gemb1/k6luecken 8
Packungsdichte von Kristallen mit gleich vielen Kationen und Anionen, die sich berühren. Zahlen unter den Namen: Nachbarn jedes Ions. An jeder Grenze springt die Struktur auf die nächste Lücke, und $P$ springt nach oben. Bei $r_+/r_-=1$ endet CsCl bei 68 %, dem Wert von BCC. Gleich große Kugeln packen dichtest mit 74 %.
:::

**Die wichtigsten Strukturen.** Im **CsCl-Gitter** bilden die Anionen ein kubisch primitives Gitter, das Kation sitzt in der Raummitte. Beide Sorten haben acht Nachbarn. Das Gitter ist SC mit zweiatomiger Basis, nicht BCC, denn Mitte und Ecke sind verschiedene Ionen. Im **NaCl-Gitter** bilden die Anionen eine kdp-Struktur, die Kationen füllen jede Oktaederlücke. Im **ZnS-Gitter** (Zinkblende) bilden die Anionen ebenfalls kdp, die Kationen füllen jede zweite Tetraederlücke.

Die __Perowskit-Struktur__ ABX$_3$ hat drei Sorten: A-Kationen auf den Würfelecken, X-Anionen (meist O$^{2-}$) auf den Flächenmitten, das B-Kation in der Raummitte. Die Oxidationszahlen von A und B sind II und IV (BaTiO$_3$, SrZrO$_3$, CaSnO$_3$), I und V (KTaO$_3$) oder III und III (LaCrO$_3$, LaMnO$_3$). In der __Fluorit-Struktur__ AX$_2$ bilden die großen Kationen eine kdp-Struktur, die Anionen füllen alle Tetraederlücken. Daher hat das Kation acht Nachbarn und das Anion vier. Stoffe dieser Art wie ZrO$_2$ und CeO$_2$ leiten Strom durch wandernde Sauerstoffionen. Meist baut man dazu Fremdionen wie Ca$^{2+}$ oder Y$^{3+}$ ein. **Grenzfall:** Die Bilanz der Nachbarn muss aufgehen. Vier Kationen mit je acht Nachbarn und acht Anionen mit je vier ergeben $4\cdot8=8\cdot4$.

**Modifikationen.** Ein Stoff kann in mehreren Strukturen auftreten, den __Modifikationen__. Eisen ist unterhalb 912 °C als $\alpha$-Fe krz, darüber als $\gamma$-Fe kfz und ab 1394 °C bis zum Schmelzpunkt als $\delta$-Fe wieder krz. Der Wechsel heißt __Phasenumwandlung__.

:::frage Warum liegt die NaCl-Kurve bei $r_+/r_-=0{,}732$ tiefer als die CsCl-Kurve?
Nahe 0,732 berühren sich in NaCl nur noch Kation und Anion, die Anionen stehen weit auseinander, und viel Raum bleibt leer. CsCl hat dort acht Nachbarn und nutzt den Raum besser. Deshalb springt $P$ dort von 56 % auf 73 %.
:::

:::aufgabe Aufgabe 11 ★★★ Strontiumtitanat
<span class="anker" id="aufg-11"></span>

SrTiO$_3$ ist ein Perowskit mit den Radien $r(\mathrm{Sr}^{2+})=0{,}144$ nm, $r(\mathrm{Ti}^{4+})=0{,}0605$ nm, $r(\mathrm{O}^{2-})=0{,}140$ nm und den Molmassen 87,62, 47,87 und 16,00 g/mol.

<ol class="al">

<li>

Zähle die Ionen in der Zelle. Bestimme die Abstände Sr-O und Ti-O in Einheiten von $a$ und die Nachbarzahlen von Sr und Ti.

</li>

<li>

Berechne $a$ unter der Annahme, dass sich Ti und O berühren, und unter der Annahme, dass sich Sr und O berühren. Gemessen werden 0,3905 nm.

</li>

<li>

Berechne $P$ und $\rho_\mathrm m$ für beide Fälle und für den Messwert.

</li>

</ol>

:::loesung
(a) Sr: $8\cdot\frac18=1$, Ti: 1, O: $6\cdot\frac12=3$. Sr-O $=a/\sqrt2$, denn Sr auf der Ecke und O in der Flächenmitte. Ti-O $=a/2$. Sr hat 12 O-Nachbarn, Ti hat 6. Bilanz: $1\cdot12=3\cdot4$ und $1\cdot6=3\cdot2$. (b) Ti-O: $a=2(0{,}0605+0{,}140)\,\mathrm{nm}=0{,}4010$ nm, 2,7 % zu groß. Sr-O: $a=\sqrt2(0{,}144+0{,}140)\,\mathrm{nm}=0{,}4016$ nm, 2,9 % zu groß. (c) $\frac43\pi(r_\mathrm{Sr}^3+r_\mathrm{Ti}^3+3r_\mathrm O^3)=0{,}0479\,\mathrm{nm^3}$ und $M=183{,}49$ g/mol. Ti-O: $P=74{,}3\,\%$, $\rho_\mathrm m=4{,}73\,\mathrm{g/cm^3}$. Sr-O: $P=74{,}0\,\%$, $\rho_\mathrm m=4{,}70\,\mathrm{g/cm^3}$. Messwert: $P=80{,}5\,\%$, $\rho_\mathrm m=5{,}12\,\mathrm{g/cm^3}$. Der Kristall ist also dichter als harte Kugeln erlauben: Die Ionen dringen ineinander ein.
:::
:::
