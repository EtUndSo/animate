---
title: Reale Bandstrukturen – direkt und indirekt
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bandstruktur
order: 4030500
summary: Wie echte Bandstrukturen aussehen und warum Galliumarsenid leuchtet, Silizium aber nicht. Entscheidend ist, ob Valenzbandmaximum und Leitungsbandminimum beim selben Wellenvektor liegen (direkte Lücke, GaAs) oder bei verschiedenen (indirekte Lücke, Si). Bei indirekter Lücke braucht ein optischer Übergang zusätzlich ein Phonon – das macht Silizium zu einem schlechten Lichtemitter, aber zum perfekten Elektronikmaterial.
tags: direkte Bandlücke, indirekte Bandlücke, GaAs, Silizium, Graphen, Phonon, Lichtemission, Hochsymmetriepunkte
---

:::grafik
Einstiegs-Animation: Zwei $E(k)$-Diagramme nebeneinander, Energie senkrecht, Wellenvektor waagerecht entlang
eines Wegs durch die Brillouin-Zone. Links __GaAs__: Valenzband-Maximum und Leitungsband-Minimum liegen genau
übereinander (beide bei $\Gamma$) — ein Elektron springt mit einem **senkrechten** Pfeil (reines Photon) über die
Lücke und leuchtet. Rechts __Silizium__: das Leitungsband-Minimum ist seitlich verschoben (nahe $X$) — der Pfeil
muss **schräg** laufen und braucht zusätzlich einen kleinen Ruck (Phonon). Darunter ein Graphen-Ausschnitt mit
zwei Kegeln, die sich in einem Punkt berühren. Kernbotschaft: Die Lage der Bandextrema im $k$-Raum entscheidet,
ob ein Material Licht abgibt.
:::

:::konzept
Die bisherigen Bänder waren einfache Kosinus-Kurven. **Echte** Bandstrukturen sind komplizierter, aber man liest
sie nach demselben Prinzip. Der für die Technik wichtigste Unterschied zwischen Materialien steckt nicht in der
**Größe** der Bandlücke, sondern in ihrer **Lage im $k$-Raum**: Liegen Valenzband-Maximum und
Leitungsband-Minimum beim **gleichen** Wellenvektor (__direkte Lücke__) oder bei **verschiedenen** (__indirekte
Lücke__)? Diese eine Frage entscheidet, ob ein Halbleiter als Leuchtdiode, Laser und Solarzelle taugt — oder
„nur" als hervorragendes Elektronikmaterial wie Silizium. Hier läuft alles aus dem Oberthema zusammen.
:::

**Worum es geht:** Wir lernen, eine reale Bandstruktur entlang der __Hochsymmetriepunkte__ zu lesen, verstehen
den Unterschied zwischen __direkter__ (GaAs) und __indirekter__ (Si) Lücke und *warum* er über Lichtemission
entscheidet, und werfen einen Blick auf den Sonderfall __Graphen__.

## Wie man eine reale Bandstruktur liest

Eine reale Bandstruktur ist eine Funktion $E(\vec k)$ über dem dreidimensionalen $k$-Raum — das kann man nicht
direkt zeichnen. Der Ausweg: Man trägt $E$ nur entlang eines **Wegs** durch die besonders symmetrischen Punkte
der Brillouin-Zone auf, die eigene Namen haben:

- __$\Gamma$__: das Zentrum der Brillouin-Zone ($\vec k = 0$).
- __$X$__: die Mitte einer Zonenrandfläche.
- __$L$__: eine Zonenecke (in der FCC-/Silizium-Zone).

Entlang dieses Wegs ($\Gamma \to X \to L \to \dots$) zeichnet man alle Bänder. Unterhalb der Fermi-Energie liegen
die gefüllten **Valenzbänder**, darüber die leeren **Leitungsbänder**. Die __Bandlücke__ $E_g$ ist der kleinste
senkrechte Abstand zwischen Valenzband-Maximum (VBM) und Leitungsband-Minimum (CBM).

:::grafik
Ein schematisches Bänderdiagramm über der Achse $\Gamma$–$X$–$L$: mehrere Valenzbänder unten, Leitungsbänder oben,
dazwischen die Lücke. VBM und CBM sind als Punkte markiert, $E_g$ als senkrechter Abstand. Beschriftung der
Hochsymmetriepunkte.
:::

## Direkte Lücke: GaAs leuchtet

Bei __Galliumarsenid (GaAs)__ liegen VBM und CBM **beim selben** Wellenvektor — beide im Zentrum $\Gamma$. Die
Lücke beträgt $E_g = 1{,}42$ eV. Weil kein Wellenvektor-Unterschied zu überbrücken ist, kann ein Elektron allein
durch **Absorption oder Emission eines Photons** über die Lücke springen.

Der Grund, *warum* das so effizient geht: Ein Photon trägt viel Energie, aber fast **keinen** Impuls. Schätzt man
den Photonimpuls $p_\gamma = E/c$ für $E \approx 1{,}4$ eV ab, ist er rund **tausendmal kleiner** als die Breite
des Kristallimpulses $\sim \hbar\pi/a$ über die Brillouin-Zone. Im $E(k)$-Diagramm ist ein optischer Übergang
daher praktisch **senkrecht** (kein Versatz in $k$). Bei direkter Lücke passt das perfekt zum Abstand VBM→CBM →
Lichtabsorption und -emission sind **effizient** (interne Quanteneffizienz nahe 1). Deshalb macht man LEDs, Laser
und hocheffiziente Solarzellen aus GaAs und verwandten III-V-Halbleitern. Bei $1{,}42$ eV liegt die Emission bei
etwa $870$ nm (nahes Infrarot) ([halbleiter.org](https://www.halbleiter.org/en/optoelectronics-photonics/fundamentals-optoelectronics/)).

:::grafik
GaAs-Bänder nahe $\Gamma$: VBM und CBM genau übereinander. Ein senkrechter Pfeil (Photon $h\nu = E_g$) verbindet
sie ohne $k$-Versatz. Daneben eine kleine Abschätzung „$p_\gamma = E/c \ll \hbar\pi/a$ → Übergang senkrecht".
:::

## Indirekte Lücke: warum Silizium (fast) nicht leuchtet

Bei __Silizium__ liegt das VBM bei $\Gamma$, das CBM aber **seitlich verschoben** nahe $X$ (entlang
$\Gamma$–$X$). Beide liegen also bei **verschiedenen** Wellenvektoren; $E_g = 1{,}12$ eV. Jetzt entsteht ein
Problem: Für den Sprung übers Band muss nicht nur die Energie $E_g$, sondern auch ein **Wellenvektor-Unterschied**
überbrückt werden. Ein Photon kann die Energie liefern, aber nicht den Impuls (es ist ja praktisch senkrecht).

Der Ausweg ist ein drittes Teilchen: ein __Phonon__ (ein Quant der Gitterschwingung), das den fehlenden Impuls
beisteuert. Ein optischer Übergang in Silizium ist damit ein **Dreier-Prozess** (Elektron + Photon + Phonon), der
viel unwahrscheinlicher ist als der direkte Zweier-Prozess. Konkret: Die interne Quanteneffizienz liegt bei
Silizium um $\sim 10^{-6}$, bei GaAs nahe $1$ — ein Unterschied von sechs Größenordnungen
([halbleiter.org](https://www.halbleiter.org/en/optoelectronics-photonics/fundamentals-optoelectronics/)). Darum
gibt es keine Silizium-LEDs. Für **Elektronik** ist dieselbe indirekte Lücke dagegen kein Nachteil — und Silizium
ist aus anderen Gründen (Oxid, Verfügbarkeit) das dominierende Material.

:::grafik
Si-Bänder entlang $\Gamma$–$X$: VBM bei $\Gamma$, CBM seitlich nahe $X$. Ein Übergang braucht einen schrägen Pfeil
= senkrechtes Photon (Energie) **plus** waagerechten Ruck (Phonon, Impuls). Beschriftung „Dreier-Prozess →
unwahrscheinlich → kein Lichtemitter".
:::

**Der Kernunterschied in einem Satz:** Nicht die Größe der Lücke, sondern ob VBM und CBM beim **gleichen** $k$
liegen, entscheidet über die Lichtausbeute.

## Sonderfall Graphen: die Lücke ist null

__Graphen__ (eine einzelne Kohlenstoff-Ebene) ist ein lehrreicher Grenzfall. Sein gefülltes $\pi$-Band und sein
leeres $\pi^\star$-Band **berühren** sich an den Zonenecken (den __Dirac-Punkten__ $K$): Die Bandlücke ist exakt
**null**. In der Umgebung dieser Punkte ist die Dispersion nicht parabolisch, sondern **linear** (kegelförmig) —
$E \propto |\vec k|$. Graphen ist damit ein __Halbmetall__ (Nullgap-Halbleiter); die linearen Bänder machen die
Ladungsträger extrem beweglich (sie verhalten sich wie masselose Teilchen).

:::grafik
Zwei Kegel, die sich mit ihren Spitzen in einem Punkt berühren (Dirac-Punkt $K$): unten das $\pi$-Band, oben das
$\pi^\star$-Band, lineare Flanken $E\propto|\vec k|$. Beschriftung „Bandlücke = 0, lineare Dispersion".
:::

## Systematik der Verbindungshalbleiter

Bei den III-V-Verbindungshalbleitern lässt sich die Bandlücke über die Materialwahl breit einstellen — von
Infrarot bis Ultraviolett. Dabei zeigt sich die schon bekannte Faustregel **kleine Lücke ↔ kleine effektive
Masse** (steilere Bänder):

| Material | $E_g$ (eV) | $m^\star/m_0$ |
|---|---|---|
| GaN | 3,37 | — |
| GaAs | 1,42 | 0,067 |
| InP | 1,27 | 0,077 |
| InAs | 0,355 | 0,023 |
| InSb | 0,17 | 0,014 |

InSb mit nur $0{,}17$ eV hat extrem leichte, schnelle Elektronen ($m^\star = 0{,}014\,m_0$); großlückige
Materialien wie GaN (Leistungselektronik, blaue/UV-LEDs) haben entsprechend trägere Ladungsträger.

:::grafik
Ein „Spektrum-Balken" von kleiner zu großer Bandlücke mit eingeordneten Materialien (InSb, InAs, InP, GaAs, GaN)
und der zugeordneten Emissionswellenlänge (Infrarot → sichtbar → UV); darunter die Tendenz „kleine Lücke →
kleine $m^\star$ → schnelle Ladungsträger".
:::

:::kern
Reale Bandstrukturen liest man als $E(k)$ entlang der __Hochsymmetriepunkte__ ($\Gamma$, $X$, $L$). Entscheidend
ist die **Lage** der Extrema: __Direkte Lücke__ (GaAs, VBM & CBM bei $\Gamma$, $1{,}42$ eV) → Elektron springt
mit reinem **Photon** über die Lücke (Photonimpuls $\approx 0$, Übergang senkrecht) → effiziente Lichtemission →
LED/Laser/Solarzelle. __Indirekte Lücke__ (Si, VBM bei $\Gamma$, CBM nahe $X$, $1{,}12$ eV) → zusätzlich
__Phonon__ für den Impulsausgleich nötig → Dreier-Prozess → schlechter Lichtemitter ($\eta\sim10^{-6}$ vs. $\sim1$
bei GaAs), aber top für Elektronik. __Graphen__: $\pi$/$\pi^\star$ berühren sich an den __Dirac-Punkten__ ($E_g=0$,
lineare Dispersion, Halbmetall). Systematik: kleine Lücke ↔ kleine effektive Masse.
:::

Damit ist das Oberthema **Bandstruktur** komplett: Wir können aus $E(k)$ Leitfähigkeitstyp, Bandlücke,
effektive Masse, Ladungsträger-Geschwindigkeit und Lichtausbeute ablesen. Als Nächstes zählen wir, **wie viele**
Zustände es pro Energie gibt (die __Zustandsdichte__) und **wie** sie bei einer gegebenen Temperatur besetzt sind
(die __Fermi-Verteilung__) — die Grundlage, um die Ladungsträgerdichte in Halbleitern wirklich auszurechnen.

:::quiz
F: Warum trägt man eine reale Bandstruktur nur entlang eines Wegs durch die Hochsymmetriepunkte auf?
A: $E(\vec k)$ lebt im dreidimensionalen $k$-Raum und lässt sich nicht direkt zeichnen. Man beschränkt sich auf einen Weg durch die besonders symmetrischen Punkte ($\Gamma$, $X$, $L$), weil dort die Bandextrema und die wesentlichen Merkmale liegen.
F: Was ist der entscheidende Unterschied zwischen direkter und indirekter Bandlücke?
A: Bei direkter Lücke liegen Valenzbandmaximum und Leitungsbandminimum beim selben Wellenvektor, bei indirekter bei verschiedenen. Nicht die Größe der Lücke, sondern diese Lage im $k$-Raum entscheidet über die Lichtausbeute.
F: Warum kann ein Elektron in GaAs allein mit einem Photon über die Lücke springen?
A: VBM und CBM liegen beide bei $\Gamma$, es muss also kein Wellenvektor-Unterschied überbrückt werden. Ein Photon liefert die nötige Energie, und da sein Impuls fast null ist, passt der senkrechte Übergang perfekt.
F: Warum ist ein optischer Übergang im $E(k)$-Diagramm praktisch senkrecht?
A: Ein Photon der Energie ~1,4 eV hat einen Impuls $p_\gamma=E/c$, der rund tausendmal kleiner ist als die Breite des Kristallimpulses über die Brillouin-Zone. Es kann also kaum $k$ ändern — der Übergang verläuft fast ohne horizontalen Versatz.
F: Warum ist Silizium ein schlechter Lichtemitter?
A: Sein CBM liegt seitlich (nahe $X$), das VBM bei $\Gamma$ — der Sprung erfordert neben der Energie auch einen Wellenvektor-Unterschied. Den liefert ein Photon nicht; es braucht zusätzlich ein Phonon, also einen unwahrscheinlichen Dreier-Prozess.
F: Welche Rolle spielt das Phonon beim Übergang in einem indirekten Halbleiter?
A: Das Phonon (ein Quant der Gitterschwingung) steuert den fehlenden Impuls (Wellenvektor-Unterschied) bei, den das Photon nicht liefern kann. Dadurch wird der Übergang zum Dreier-Prozess (Elektron + Photon + Phonon) und ist viel seltener.
F: Wie groß ist der Effizienzunterschied zwischen GaAs und Si, und warum ist Si trotzdem dominierend?
A: Die interne Quanteneffizienz liegt bei GaAs nahe 1, bei Si um $10^{-6}$ — sechs Größenordnungen. Für Elektronik ist die indirekte Lücke aber kein Nachteil, und Si gewinnt durch sein hervorragendes Oxid und die Verfügbarkeit.
F: Was macht Graphen zu einem Sonderfall?
A: Sein gefülltes $\pi$- und sein leeres $\pi^\star$-Band berühren sich an den Dirac-Punkten, die Bandlücke ist exakt null (Halbmetall). In deren Umgebung ist die Dispersion linear statt parabolisch, sodass sich die Ladungsträger wie masselose Teilchen verhalten.
F: Warum sind die Ladungsträger in Graphen besonders beweglich?
A: Die lineare Dispersion $E\propto|\vec k|$ entspricht keiner gewöhnlichen parabolischen Masse — die Elektronen verhalten sich wie masselose, extrem schnelle Teilchen. Das führt zu sehr hoher Beweglichkeit.
F: Welche Faustregel verbindet Bandlücke und effektive Masse bei den III-V-Halbleitern?
A: Kleine Lücke geht mit kleiner effektiver Masse (steileren Bändern) einher. InSb mit nur 0,17 eV hat extrem leichte, schnelle Elektronen ($m^\star=0{,}014\,m_0$), großlückige wie GaN entsprechend trägere Ladungsträger.
:::
