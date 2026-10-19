---
title: Die kubischen Bravaisgitter
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Kristallstruktur
order: 4020200
summary: Die drei würfelbasierten Gitter – einfach kubisch, raumzentriert und flächenzentriert – und die zwei Kennzahlen, mit denen man sie vergleicht: die Koordinationszahl (6, 8, 12) und die Packungsdichte ($\tfrac{\pi}{6}$, $\tfrac{\sqrt3\pi}{8}$, $\tfrac{\pi}{3\sqrt2}$). Plus die häufigste Falle: Warum die „naiven" Würfelvektoren BCC und FCC gar nicht beschreiben.
tags: kubische Gitter, einfach kubisch, BCC, FCC, Koordinationszahl, Packungsdichte, primitive Gittervektoren, Wigner-Seitz-Zelle
---

:::grafik
Einstiegs-Animation: Drei Würfel nebeneinander, die sich langsam drehen. Links __einfach kubisch__ (Atome nur
auf den 8 Ecken), Mitte __raumzentriert__ (zusätzlich ein Atom in der Würfelmitte), rechts __flächenzentriert__
(zusätzlich je ein Atom auf den 6 Flächenmitten). Von einem herausgehobenen Atom leuchten jeweils seine nächsten
Nachbarn auf — 6, dann 8, dann 12. Darunter füllt sich ein Balken „Packungsdichte": 52 %, 68 %, 74 %.
Kernbotschaft: Je mehr Zusatzatome, desto mehr nächste Nachbarn und desto dichter die Packung.
:::

:::konzept
Im vorigen Artikel haben wir gelernt, *wie* man ein periodisches Gitter beschreibt. Jetzt schauen wir die für die
Halbleitertechnik wichtigsten konkreten Fälle an: die drei __kubischen__ Bravaisgitter. Sie sind nicht nur die
anschaulichsten (ein Würfel als Grundform), sondern auch die wichtigsten — Silizium und Germanium kristallisieren
in der **Diamantstruktur**, die auf dem flächenzentrierten kubischen Gitter aufbaut. Um die drei Gitter zu
vergleichen, brauchen wir zwei Kennzahlen (__Koordinationszahl__ und __Packungsdichte__). Und wir klären eine
Falle, in die fast jeder einmal tappt: Die „offensichtlichen" Würfelkantenvektoren beschreiben zwei der drei
Gitter **falsch**.
:::

**Worum es geht:** Wir stellen die drei kubischen Gitter __SC__, __BCC__ und __FCC__ vor, definieren
__Koordinationszahl__ und __Packungsdichte__, rechnen letztere für jedes Gitter aus, und leiten her, warum die
primitiven Gittervektoren von BCC und FCC **nicht** die simplen Würfelkanten sein können.

## Zwei Kennzahlen, um Gitter zu vergleichen

Denkt man sich die Atome als harte, sich berührende Kugeln, lassen sich zwei Zahlen ablesen, die ein Gitter
charakterisieren:

- __Koordinationszahl__ (anschaulich: wie viele unmittelbare Nachbarn hat ein Atom) — die Zahl der **nächsten**
  Nachbarn. Sie misst, wie „umringt" und damit wie stabil gebunden ein Atom sitzt.
- __Packungsdichte__ (engl. *atomic packing factor*, APF) — der **Volumenanteil**, den die harten Kugeln
  ausfüllen. Sie misst, wie effizient der Raum genutzt wird.

Beide hängen zusammen: Mehr nächste Nachbarn bedeuten in der Regel eine dichtere Packung und eine energetisch
günstigere, stabilere Struktur. Genau diesen Trend sehen wir gleich bei SC → BCC → FCC.

## Einfach kubisch (SC)

Beim __einfach kubischen__ Gitter (*simple cubic*, SC) sitzen Atome nur auf den **8 Würfelecken**. Da jede Ecke
zu 8 angrenzenden Würfeln gehört, trägt sie nur $1/8$ zum Würfel bei — macht $8 \cdot \tfrac18 = 1$ Atom pro
Zelle. Ein Atom hat **6** nächste Nachbarn (oben, unten, links, rechts, vorn, hinten), also Koordinationszahl 6
([KSU](https://faculty.ksu.edu.sa/sites/default/files/Lecture_8_Important_Crystal_Structures.pdf)).

Hier sind die primitiven Gittervektoren tatsächlich die Würfelkanten:

$$\vec a_1 = \begin{pmatrix} a \\ 0 \\ 0 \end{pmatrix}, \quad \vec a_2 = \begin{pmatrix} 0 \\ a \\ 0 \end{pmatrix}, \quad \vec a_3 = \begin{pmatrix} 0 \\ 0 \\ a \end{pmatrix}.$$

Die Packungsdichte: Entlang der Kante berühren sich die Kugeln, also $a = 2r$. Ein Atom (Volumen
$\tfrac43\pi r^3$) steckt im Würfel $a^3$:

$$\text{APF}_{\text{SC}} = \frac{\tfrac43\pi r^3}{a^3} = \frac{\tfrac43\pi r^3}{(2r)^3} = \frac{\pi}{6} \approx 0{,}52.$$

Nur 52 % des Raums sind gefüllt — das ist wenig, die Struktur ist **instabil** und in der Natur selten. Praktisch
das einzige Element mit SC-Struktur ist **Polonium**. Die Wigner-Seitz-Zelle ist hier schlicht ein Würfel.

:::grafik
Ein SC-Würfel mit Atomen auf den Ecken; ein herausgehobenes Atom mit seinen 6 nächsten Nachbarn (Pfeile in
$\pm x, \pm y, \pm z$). Daneben der Kugel-Kontakt entlang der Kante mit der Beschriftung $a = 2r$ und das Ergebnis
$\text{APF} = \pi/6$.
:::

## Kubisch-raumzentriert (BCC)

Beim __raumzentrierten__ Gitter (*body-centered cubic*, BCC) kommt zu den 8 Ecken **ein Atom im Würfelzentrum**
hinzu. Pro Zelle also $8\cdot\tfrac18 + 1 = 2$ Atome. Das Zentralatom „sieht" alle 8 Ecken gleich weit — die
Koordinationszahl ist **8** ([KSU](https://faculty.ksu.edu.sa/sites/default/files/Lecture_8_Important_Crystal_Structures.pdf)).
Beispiele: Natrium, $\alpha$-Eisen, Wolfram, Chrom, Kalium.

Jetzt berühren sich die Kugeln entlang der **Raumdiagonale** (Länge $\sqrt3\,a$), auf der vier Radien liegen:
$\sqrt3\,a = 4r$. Mit 2 Atomen pro Zelle:

$$\text{APF}_{\text{BCC}} = \frac{2\cdot\tfrac43\pi r^3}{a^3} = \frac{\sqrt3\,\pi}{8} \approx 0{,}68.$$

Deutlich dichter als SC. Die Wigner-Seitz-Zelle ist ein **abgestumpftes Oktaeder**.

:::grafik
Ein BCC-Würfel mit Eck- und Zentralatom; die Raumdiagonale ist eingezeichnet mit den vier aufgereihten Radien
und der Bedingung $\sqrt3\,a = 4r$. Daneben das Ergebnis $\text{APF} = \sqrt3\pi/8 \approx 0{,}68$.
:::

**Die Falle — warum nicht die Würfelkanten?** Es liegt nahe, für BCC dieselben Vektoren $(a,0,0)$, $(0,a,0)$,
$(0,0,a)$ zu nehmen. Das ist **falsch**: Diese Vektoren erzeugen durch ganzzahlige Kombination nur die **Ecken** —
das Zentralatom wird **nie** getroffen. Sie beschreiben also nur das SC-Eckgitter und verfehlen die halbe
Struktur. Korrekt sind Vektoren, die von einer Ecke zu den Zentralatomen der Nachbarwürfel zeigen (halbe
Raumdiagonalen):

$$\vec a_1 = \tfrac{a}{2}\begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}, \quad \vec a_2 = \tfrac{a}{2}\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}, \quad \vec a_3 = \tfrac{a}{2}\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}.$$

Der Grund ist der Kern aus dem vorigen Artikel: Die **primitive** Zelle muss **genau einen** Gitterpunkt
enthalten. Der Würfel mit Eck- **und** Zentralatom enthält aber zwei — er ist die __konventionelle__ (symmetrisch
schöne), **nicht** die primitive Zelle.

:::grafik
Links die durchgestrichenen „naiven" Vektoren $(a,0,0)$ etc., die nur das Eckgitter erzeugen (Zentralatom rot als
„verfehlt" markiert). Rechts die korrekten halben Raumdiagonalen $\tfrac{a}{2}(1,1,-1)$ etc., die von einer Ecke
zu Zentralatomen zeigen und so jeden Gitterpunkt treffen.
:::

## Kubisch-flächenzentriert (FCC)

Beim __flächenzentrierten__ Gitter (*face-centered cubic*, FCC) sitzt zu den 8 Ecken **je ein Atom auf den 6
Flächenmitten**. Jede Flächenmitte gehört zu 2 Würfeln, trägt also $\tfrac12$ bei: $8\cdot\tfrac18 + 6\cdot\tfrac12
= 4$ Atome pro Zelle. Die Koordinationszahl ist **12** — der höchstmögliche Wert für gleich große Kugeln
([KSU](https://faculty.ksu.edu.sa/sites/default/files/Lecture_8_Important_Crystal_Structures.pdf)). Beispiele:
Aluminium, Kupfer, Gold, Silber.

Hier berühren sich die Kugeln entlang der **Flächendiagonale** (Länge $\sqrt2\,a$), auf der vier Radien liegen:
$\sqrt2\,a = 4r$. Mit 4 Atomen pro Zelle:

$$\text{APF}_{\text{FCC}} = \frac{4\cdot\tfrac43\pi r^3}{a^3} = \frac{\pi}{3\sqrt2} \approx 0{,}74.$$

Das ist die **dichteste** mögliche Packung gleich großer Kugeln überhaupt. Die primitiven Vektoren zeigen von
einer Ecke zu den benachbarten Flächenmitten (auch hier **nicht** die Würfelkanten):

$$\vec a_1 = \tfrac{a}{2}\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \vec a_2 = \tfrac{a}{2}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \quad \vec a_3 = \tfrac{a}{2}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}.$$

Die Wigner-Seitz-Zelle ist ein **Rhombendodekaeder** (12 rautenförmige Flächen — passend zu den 12 Nachbarn).

:::grafik
Ein FCC-Würfel mit Eck- und Flächenatomen; die Flächendiagonale mit vier aufgereihten Radien und der Bedingung
$\sqrt2\,a = 4r$. Daneben das Ergebnis $\text{APF} = \pi/(3\sqrt2) \approx 0{,}74$ und die primitiven Vektoren
Ecke → Flächenmitte.
:::

## Der Trend auf einen Blick

Die drei Gitter bilden eine klare Reihe — mehr Zentrierung bedeutet mehr Nachbarn, dichtere Packung und (meist)
höhere Stabilität:

| Gitter | Atome/Zelle | Koordinationszahl | Packungsdichte | WS-Zelle | Beispiele |
|---|---|---|---|---|---|
| SC | 1 | 6 | $\pi/6 \approx 0{,}52$ | Würfel | Polonium |
| BCC | 2 | 8 | $\sqrt3\pi/8 \approx 0{,}68$ | abgest. Oktaeder | Na, $\alpha$-Fe, W |
| FCC | 4 | 12 | $\pi/(3\sqrt2) \approx 0{,}74$ | Rhombendodekaeder | Al, Cu, Au, Ag |

:::grafik
Balkendiagramm Koordinationszahl (6 / 8 / 12) und daneben Packungsdichte (52 % / 68 % / 74 %) für SC / BCC / FCC,
mit einem Pfeil „mehr Zentrierung → dichter → stabiler".
:::

:::kern
Die drei __kubischen__ Gitter unterscheiden sich durch Zusatzatome: __SC__ (nur Ecken, 1 Atom/Zelle,
Koordinationszahl 6, $\text{APF}=\pi/6\approx0{,}52$), __BCC__ (+ Zentrum, 2 Atome, KZ 8,
$\sqrt3\pi/8\approx0{,}68$), __FCC__ (+ Flächen, 4 Atome, KZ 12, $\pi/(3\sqrt2)\approx0{,}74$ = dichteste
Packung). __Packungsdichte__ = Kugel-Volumenanteil, aus dem Kontaktabstand: SC $a=2r$, BCC $\sqrt3a=4r$, FCC
$\sqrt2a=4r$. **Falle:** Die Würfelkanten $(a,0,0)$ etc. sind nur für SC primitiv; bei BCC/FCC erzeugen sie nur
die Ecken und verfehlen Zentral-/Flächenatome — korrekt sind halbe Raum- bzw. Flächendiagonalen
($\tfrac{a}{2}(1,1,-1)$ bzw. $\tfrac{a}{2}(1,1,0)$). Der Würfel mit Zusatzatomen ist die __konventionelle__, nicht
die primitive Zelle.
:::

Wir können Gitter jetzt benennen und vergleichen. Als Nächstes brauchen wir eine Sprache für die **Ebenen und
Richtungen** in einem Kristall — denn Spaltflächen, Ätzflächen und Transportrichtungen sind physikalisch
ausgezeichnet. Das leisten die __Millerindizes__, das Thema des nächsten Artikels.

:::quiz
F: Was misst die Koordinationszahl, und was die Packungsdichte?
A: Die Koordinationszahl ist die Zahl der nächsten Nachbarn eines Atoms (wie „umringt" es sitzt), die Packungsdichte der Volumenanteil, den die als harte Kugeln gedachten Atome ausfüllen (wie effizient der Raum genutzt wird). Beide steigen zusammen von SC über BCC zu FCC.
F: Warum trägt ein Eckatom nur 1/8 zur Würfelzelle bei?
A: Jede Würfelecke wird von 8 angrenzenden Würfeln geteilt, sodass nur ein Achtel des Eckatoms in eine einzelne Zelle fällt. Bei 8 Ecken ergibt das $8\cdot\tfrac18=1$ Atom pro SC-Zelle.
F: Wie kommt beim SC-Gitter die Beziehung $a=2r$ zustande?
A: Die Atome berühren sich entlang der Würfelkante, auf der genau zwei Radien liegen (je einer der beiden Eckatome). Daher ist die Kantenlänge $a=2r$, woraus $\text{APF}=\pi/6\approx0{,}52$ folgt.
F: Warum ist das SC-Gitter in der Natur so selten?
A: Mit nur 52 % Raumfüllung und Koordinationszahl 6 ist es energetisch ungünstig und instabil — die Atome „verschenken" viel Platz. Praktisch nur Polonium kristallisiert einfach kubisch.
F: Warum berühren sich die Kugeln bei BCC entlang der Raumdiagonale und nicht der Kante?
A: Das Zentralatom liegt der Ecke am nächsten, und die Verbindungslinie Ecke–Zentrum–gegenüberliegende Ecke ist die Raumdiagonale. Dort liegen vier Radien, also $\sqrt3\,a=4r$ — entlang der Kante berühren sich die Eckatome dagegen nicht.
F: Warum beschreiben die Würfelkantenvektoren $(a,0,0)$ usw. das BCC-Gitter falsch?
A: Ganzzahlige Kombinationen dieser Vektoren treffen nur die Ecken, nie das Zentralatom — die halbe Struktur wird verfehlt. Die primitive Zelle muss genau einen Gitterpunkt enthalten; korrekt sind die halben Raumdiagonalen $\tfrac a2(1,1,-1)$ usw., die von einer Ecke zu den Zentralatomen zeigen.
F: Was ist der Unterschied zwischen konventioneller und primitiver Zelle bei BCC/FCC?
A: Der symmetrisch schöne Würfel mit Eck- und Zusatzatomen ist die konventionelle Zelle, enthält aber mehr als einen Gitterpunkt (BCC 2, FCC 4). Die primitive Zelle enthält genau einen und wird von den halben Diagonalen aufgespannt — kleiner, aber weniger anschaulich.
F: Warum hat FCC mit Koordinationszahl 12 die dichteste Packung gleich großer Kugeln?
A: Zwölf nächste Nachbarn ist das Maximum, das sich mit gleich großen Kugeln erreichen lässt; die Kugeln berühren sich entlang der Flächendiagonale ($\sqrt2\,a=4r$). Das ergibt $\text{APF}=\pi/(3\sqrt2)\approx0{,}74$ — die dichtestmögliche Kugelpackung.
F: Warum hat die Wigner-Seitz-Zelle des FCC-Gitters zwölf Flächen?
A: Jede Fläche der WS-Zelle entsteht als Mittelsenkrechte zu einem nächsten Nachbarn; FCC hat 12 nächste Nachbarn, also 12 Flächen — das Rhombendodekaeder. Die Zahl der WS-Flächen spiegelt direkt die Koordinationszahl.
F: Welcher allgemeine Trend verbindet SC → BCC → FCC?
A: Mit zunehmender Zentrierung steigen Koordinationszahl (6→8→12) und Packungsdichte (52 %→68 %→74 %). Mehr nächste Nachbarn bedeuten in der Regel eine dichtere, energetisch günstigere und stabilere Struktur.
:::
