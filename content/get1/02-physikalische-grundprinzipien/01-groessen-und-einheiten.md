---
title: Physikalische Größen und Einheiten
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Physikalische Grundprinzipien
order: 20100
summary: Von Grund auf – jede physikalische Angabe ist Zahlenwert mal Einheit. Leitbild ist ein Baukasten mit sieben Sorten Grundsteinen, aus denen jede Einheit gebaut ist. Mit den sieben Basisgrößen und ihrer Definition über Naturkonstanten seit 2019, dem Ampere über die Elementarladung, den abgeleiteten Einheiten bis zum Tesla, den Einheitenvorsätzen samt Fallstricken, Geschwindigkeit und Beschleunigung als Ableitungen, Kraft, Gravitationsgesetz, Arbeit als Wegintegral und den Rechenregeln für Einheiten. Mit Beispiel-Seite.
tags: physikalische Größe, Einheit, SI, Basisgrößen, Ampere, Einheitenvorsatz, Größengleichung, Dimensionskontrolle
---

## Anschaulich

Wer sagt „der Widerstand ist 5", hat nichts gesagt: Fünf Ohm, fünf Kiloohm und fünf Megaohm liegen jeweils um den Faktor
tausend auseinander. Eine physikalische Angabe braucht immer zwei Teile, eine Zahl und eine Einheit. Wie teuer ein
Missverständnis werden kann, zeigt die Raumsonde Mars Climate Orbiter: Sie ging 1999 verloren, weil ein Programm Kraftstöße in
Pfund-Kraft mal Sekunde lieferte, während die Navigation Newton mal Sekunde erwartete.

**Das Leitbild dieses Artikels:** ein **Baukasten**. Das internationale Einheitensystem, kurz __SI__ (französisch *Système
international d'unités*), hat sieben Sorten Grundsteine: Meter, Kilogramm, Sekunde, Ampere, Kelvin, Mol und Candela. Jede andere
Einheit ist ein Bauwerk aus diesen Steinen. Das Newton etwa besteht aus einem Kilogramm-Stein und einem Meter-Stein im Zähler und
zwei Sekunden-Steinen im Nenner.

Eine Größe anzugeben heißt dann: sagen, welches Bauwerk gemeint ist, und zählen, wie viele davon. Daraus folgen die Regeln dieses
Kapitels fast von selbst. Addieren kann man nur gleiche Bauwerke — drei Meter und zwei Sekunden ergeben keine Summe.
Multiplizieren setzt Bauwerke zu neuen zusammen. Steht derselbe Stein oben und unten, fällt er heraus. Und eine Gleichung stimmt
nur, wenn auf beiden Seiten dasselbe Bauwerk steht.

:::grafik
Szene: get1/physikalische-grundprinzipien/01-baukasten · Vorlage: einheiten-baukasten
Oben eine Leiste mit sieben farbigen Grundsteinen, beschriftet m, kg, s, A, K, mol, cd. Darunter entstehen nacheinander Bauwerke:
das Newton aus kg und m über zwei s, das Joule aus Newton und m, das Volt aus Joule über A und s. Ein Regler multipliziert Volt mit
Ampere; die beiden A-Steine oben und unten leuchten auf, verschwinden, und übrig bleibt das Watt. Kernaussage: Jede Einheit ist
ein Bauwerk aus sieben Sorten Grundsteinen, und beim Rechnen werden die Steine mitgezählt. (Blau = Grundsteine, rot = das gerade
gebaute Bauwerk, orange = Zusammensetzen und Kürzen, grau = Leiste und Rahmen.)
:::

## Was ist eine physikalische Größe?

Eine __physikalische Größe__ ist eine messbare Eigenschaft eines Körpers, eines Vorgangs oder eines Zustands — eine Länge, eine
Zeit, ein Strom. Messbar heißt: Man vergleicht mit einem festgelegten Maß und erhält eine Zahl, und zwar __objektiv__, also
unabhängig davon, wer misst. Ein Thermometer zeigt im Wohnzimmer $21\,\text{°C}$, gleichgültig, wer abliest. Die Hand sagt nur
„warm" oder „kühl", und das hängt davon ab, wo sie vorher war.

Einige Größen mit ihren üblichen Formelzeichen:

| Gebiet | Größen und Formelzeichen |
|---|---|
| Mechanik | Weg, Länge, Radius $s$, $l$, $r$; Geschwindigkeit $\vec v$; Beschleunigung $\vec a$; Masse $m$; Kraft $\vec F$; Arbeit $W$ |
| Elektrizitätslehre | Ladung $Q$; Spannung $U$; Strom $I$; Widerstand $R$; elektrische Feldstärke $\vec E$ |
| Wärmelehre | Temperatur $T$; Wärmemenge $Q$; Entropie $S$ |

Vektorielle Größen tragen einen Pfeil; ihre Beträge schreibt man ohne, etwa $v$ oder $F$.

Eine Größe ist immer das Produkt aus einem __Zahlenwert__ und einer __Einheit__:

:::formel Definition
$$G = \{G\}\cdot[G].$$
:::

**So liest man das:** $G$ ist die Größe, $\{G\}$ ihr Zahlenwert — eine reine Zahl ohne Einheit — und $[G]$ ihre Einheit. Bei einem
Strom von zwei Ampere ist

$$I = 2\,\text{A}, \qquad \{I\} = 2, \qquad [I] = \text{A}.$$

**Im Bild:** Die Einheit ist das Bauwerk, der Zahlenwert sagt, wie viele Bauwerke es sind. Weder das eine noch das andere allein
beschreibt die Größe.

:::grafik
Szene: get1/physikalische-grundprinzipien/01-zahlenwert-mal-einheit · Vorlage: massstab-umrechnen
Ein Stab von $0{,}25\,\text{m}$ Länge, darunter drei Maßstäbe: einer in Metern, einer in Zentimetern, einer in Millimetern. Ein
Regler wechselt die Einheit; die Teilstriche werden feiner, der Zähler für den Zahlenwert springt von $0{,}25$ auf $25$ und $250$,
während der Stab selbst unverändert bleibt. Darüber die Zerlegung $G=\{G\}\cdot[G]$ mit Klammern um Zahlenwert und Einheit.
Kernaussage: Kleinere Einheit, größerer Zahlenwert — die Größe bleibt dieselbe. (Rot = der Stab, die Größe, blau = Maßstäbe,
orange = Zahlenwert-Zähler, grau = Teilstriche.)
:::

**Formelzeichen und Einheitenzeichen.** Formelzeichen für Größen werden kursiv gesetzt, Einheitenzeichen aufrecht. Das ist mehr
als Typografie, denn dieselben Buchstaben kommen in beiden Rollen vor: $m$ ist die Masse, $\text{m}$ das Meter, $s$ der Weg, $\text{s}$
die Sekunde, $W$ die Energie und $\text{W}$ das Watt. Ein Zeichen kann sogar in verschiedenen Gebieten verschiedene Größen
bezeichnen — $Q$ steht in der Elektrizitätslehre für die Ladung, in der Wärmelehre für die Wärmemenge. Dann entscheidet der
Zusammenhang.

**Einheit wechseln.** Dieselbe Größe lässt sich in verschiedenen Einheiten derselben Art angeben. Schreibt man sie einmal mit dem
Zahlenwert $\{G\}_1$ in der Einheit $[G]_1$ und einmal mit $\{G\}_2$ in $[G]_2$, dann ändert sich der Zahlenwert gegenläufig zur
Einheit:

$$\{G\}_2 = \{G\}_1\cdot\frac{[G]_1}{[G]_2}.$$

**Im Bild:** Baut man mit kleineren Bauwerken, braucht man entsprechend mehr davon — die Größe selbst bleibt dieselbe.

:::herleitung
Beide Schreibweisen beschreiben dieselbe Größe:

$$G = \{G\}_1\cdot[G]_1 = \{G\}_2\cdot[G]_2.$$

Man teilt durch $[G]_2$. Der Quotient zweier Einheiten derselben Art ist eine reine Zahl, der __Umrechnungsfaktor__ — etwa
$\frac{\text{m}}{\text{cm}}$, das ist $100$, weil ein Meter hundert Zentimeter lang ist.
:::

::::beispiel Ein Wert, drei Schreibweisen
**(a) Eine Länge.** Mit den Umrechnungsfaktoren 100 für Meter in Zentimeter und 1000 für Meter in Millimeter:

$$0{,}25\,\text{m} = 0{,}25\cdot100\,\text{cm} = 25\,\text{cm} = 250\,\text{mm}.$$

**(b) Ein Strom.** Ein Ampere sind tausend Milliampere:

$$I = 0{,}02\,\text{A} = 20\,\text{mA}, \qquad \{I\} = 0{,}02 \ \text{in A}, \qquad \{I\} = 20 \ \text{in mA}.$$

**(c) Eine Zeit.** Eine Stunde hat 60 Minuten, eine Minute 60 Sekunden:

$$1{,}5\,\text{h} = 1{,}5\cdot60\,\text{min} = 90\,\text{min} = 90\cdot60\,\text{s} = 5400\,\text{s}.$$

**Im Bild:** Je kleiner das Bauwerk, desto größer die Zahl davor. Das Produkt aus beiden — die Größe — ändert sich nie.
::::

## Die sieben Basisgrößen

Das SI teilt die Größen in zwei Klassen, __Basisgrößen__ und __abgeleitete Größen__. Basisgrößen lassen sich nicht durch andere
Basisgrößen ausdrücken; sie sind die Grundsteine des Baukastens. Das SI legt sieben davon fest:

| Basisgröße | Formelzeichen | Einheit | Einheitenzeichen |
|---|---|---|---|
| Länge, Weg, Radius | $l$, $s$, $r$ | Meter | $\text{m}$ |
| Masse | $m$ | Kilogramm | $\text{kg}$ |
| Zeit | $t$ | Sekunde | $\text{s}$ |
| elektrische Stromstärke | $I$ | Ampere | $\text{A}$ |
| absolute Temperatur | $T$ | Kelvin | $\text{K}$ |
| Lichtstärke | $I_\text{v}$ | Candela | $\text{cd}$ |
| Stoffmenge | $n$ | Mol | $\text{mol}$ |

**Im Bild:** Sieben Sorten Steine, und keine lässt sich aus den anderen bauen. Mehr braucht man nicht, um jede Einheit der Physik
zusammenzusetzen.

**Warum ein elektrischer Grundstein?** Man könnte die Ladung auch rein mechanisch festlegen, über die Kraft zwischen zwei
Ladungen. Das tut das ältere Gaußsche Einheitensystem; dort erhält die Ladungseinheit gebrochene Exponenten von Gramm und
Zentimeter. Das SI nimmt stattdessen die Stromstärke als eigenen Grundstein. Elektrische Einheiten werden dadurch handlich, und
der Preis dafür ist eine Naturkonstante, die später im Coulomb-Gesetz auftaucht, die elektrische Feldkonstante.

:::herleitung
Im Gaußschen System lautet das Coulomb-Gesetz für zwei gleiche Ladungen $Q$ im Abstand $r$ ohne jede Konstante: Kraft gleich
Ladungsquadrat durch Abstandsquadrat. Die Ladungseinheit muss dann die Einheitengleichung

$$[Q]^2 = [F]\cdot[r]^2 = \frac{\text{g}\,\text{cm}}{\text{s}^2}\cdot\text{cm}^2, \qquad [Q] = \text{g}^{1/2}\,\text{cm}^{3/2}\,\text{s}^{-1}$$

erfüllen — mit halbzahligen Exponenten. Im SI steht im Coulomb-Gesetz zusätzlich die Feldkonstante, deren Einheit die Ampere-Steine
aufnimmt.
:::

**Die Definitionen entwickeln sich weiter.** Wie man die Grundsteine festlegt, folgt dem Stand der Messtechnik. Der letzte große
Schritt war die Reform vom 20. Mai 2019: Seitdem ist jede Basiseinheit über den exakt festgelegten Zahlenwert einer Naturkonstante
definiert. Vorher war das Kilogramm die Masse eines Metallzylinders in einem Tresor bei Paris, des Urkilogramms.

| Naturkonstante | festgelegter Wert | legt fest |
|---|---|---|
| Frequenz des Cäsium-Übergangs $\Delta\nu_{\text{Cs}}$ | $9\,192\,631\,770\,\text{Hz}$ | Sekunde |
| Lichtgeschwindigkeit $c$ | $299\,792\,458\,\text{m}/\text{s}$ | Meter |
| Planck-Konstante $h$ | $6{,}626\,070\,15\cdot10^{-34}\,\text{J}\,\text{s}$ | Kilogramm |
| Elementarladung $e$ | $1{,}602\,176\,634\cdot10^{-19}\,\text{C}$ | Ampere |
| Boltzmann-Konstante $k$ | $1{,}380\,649\cdot10^{-23}\,\text{J}/\text{K}$ | Kelvin |
| Avogadro-Konstante $N_\text{A}$ | $6{,}022\,140\,76\cdot10^{23}\,\text{mol}^{-1}$ | Mol |
| Photometrisches Strahlungsäquivalent $K_\text{cd}$ | $683\,\text{lm}/\text{W}$ | Candela |

Das Lumen in der letzten Zeile ist die Einheit des Lichtstroms, das Hertz eine Schwingung pro Sekunde.

**Im Bild:** Die Grundsteine werden nicht mehr nach einem Musterstein im Tresor gegossen, sondern nach einer Bauanleitung, die
jedes Labor der Welt nachbauen kann.

**Das Ampere.** Für die Elektrotechnik zählt vor allem die Elementarladung, die Ladung eines Protons; ein Elektron trägt ihr
Negatives. Ihr Wert ist exakt festgelegt, und mit der Einheit Coulomb, Ampere mal Sekunde, folgt die Definition des Ampere:

:::formel Definition
$$e = 1{,}602\,176\,634\cdot10^{-19}\,\text{C}, \qquad 1\,\text{C} = 1\,\text{A}\,\text{s}.$$
:::

**So liest man das:** Ein Strom von einem Ampere transportiert in jeder Sekunde die Ladung $1\,\text{C}$ durch den Leiterquerschnitt,
und das sind

$$\frac{1\,\text{C}}{e} = \frac{1}{1{,}602\,176\,634\cdot10^{-19}} \approx 6{,}241\,509\cdot10^{18}$$

Elementarladungen.

**Im Bild:** Der Ampere-Stein wird abgezählt: so und so viele Elementarladungen pro Sekunde.

:::herleitung
Ein Strom $I$ transportiert in der Zeit $t$ die Ladung $I\cdot t$; bei einem Ampere und einer Sekunde ist das ein Coulomb. Die Zahl
der Elementarladungen ist diese Ladung geteilt durch die Ladung einer einzelnen:

$$N = \frac{1\,\text{A}\cdot1\,\text{s}}{1{,}602\,176\,634\cdot10^{-19}\,\text{A}\,\text{s}} = \frac{1}{1{,}602\,176\,634\cdot10^{-19}}.$$

Die Einheiten kürzen sich, übrig bleibt eine reine Anzahl. Weil der Zahlenwert von $e$ exakt festgelegt ist, ist auch diese Anzahl
exakt.
:::

::::beispiel Elektronen zählen
**(a) Ein kleiner Strom.** Durch eine Leuchtdiode fließt $1\,\text{mA}$ eine Sekunde lang. Die transportierte Ladung und die Zahl der
Elektronen:

$$Q = 10^{-3}\,\text{A}\cdot1\,\text{s} = 10^{-3}\,\text{C}, \qquad N = \frac{10^{-3}\,\text{C}}{1{,}602\cdot10^{-19}\,\text{C}} \approx 6{,}24\cdot10^{15}.$$

**(b) Ein Handy-Akku.** Die Angabe $3000\,\text{mAh}$ ist eine Ladung: Strom mal Zeit. Mit einer Stunde gleich $3600\,\text{s}$:

$$Q = 3\,\text{A}\cdot3600\,\text{s} = 10\,800\,\text{C}, \qquad N = \frac{10\,800\,\text{C}}{1{,}602\cdot10^{-19}\,\text{C}} \approx 6{,}74\cdot10^{22}.$$

**Im Bild:** Hinter jedem Ampere steckt eine unvorstellbar große, aber abzählbare Zahl von Elementarladungen. Die Einheiten zeigen
in beiden Rechnungen, dass am Ende eine reine Anzahl steht: Coulomb durch Coulomb.
::::

## Abgeleitete Größen

Alle übrigen Größen sind __abgeleitet__: Sie entstehen aus den Basisgrößen durch Multiplizieren, Dividieren und Potenzieren, und
ihre Einheiten sind Produkte von Potenzen der Basiseinheiten. Viele dieser Einheiten tragen einen eigenen Namen. Die wichtigsten
für die Elektrotechnik:

| Größe | Zeichen | Einheit | in Basiseinheiten | in anderen SI-Einheiten |
|---|---|---|---|---|
| Kraft | $F$ | Newton, $\text{N}$ | $\text{kg}\,\text{m}\,\text{s}^{-2}$ | — |
| Energie, Arbeit | $W$ | Joule, $\text{J}$ | $\text{kg}\,\text{m}^2\,\text{s}^{-2}$ | $\text{N}\,\text{m}$, $\text{W}\,\text{s}$ |
| Leistung | $P$ | Watt, $\text{W}$ | $\text{kg}\,\text{m}^2\,\text{s}^{-3}$ | $\text{J}/\text{s}$, $\text{V}\,\text{A}$ |
| Druck | $p$ | Pascal, $\text{Pa}$ | $\text{kg}\,\text{m}^{-1}\,\text{s}^{-2}$ | $\text{N}/\text{m}^2$ |
| Ladung | $Q$ | Coulomb, $\text{C}$ | $\text{A}\,\text{s}$ | — |
| Spannung | $U$ | Volt, $\text{V}$ | $\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-1}$ | $\text{J}/\text{C}$, $\text{W}/\text{A}$ |
| Widerstand | $R$ | Ohm, $\Omega$ | $\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-2}$ | $\text{V}/\text{A}$ |
| Kapazität | $C$ | Farad, $\text{F}$ | $\text{A}^2\,\text{s}^4\,\text{kg}^{-1}\,\text{m}^{-2}$ | $\text{A}\,\text{s}/\text{V}$ |
| Induktivität | $L$ | Henry, $\text{H}$ | $\text{kg}\,\text{m}^2\,\text{s}^{-2}\,\text{A}^{-2}$ | $\text{V}\,\text{s}/\text{A}$ |
| magnetischer Fluss | $\Phi$ | Weber, $\text{Wb}$ | $\text{kg}\,\text{m}^2\,\text{s}^{-2}\,\text{A}^{-1}$ | $\text{V}\,\text{s}$ |
| magnetische Flussdichte | $B$ | Tesla, $\text{T}$ | $\text{kg}\,\text{s}^{-2}\,\text{A}^{-1}$ | $\text{V}\,\text{s}/\text{m}^2$ |

Das Skript nennt die Flussdichte magnetische Induktion und schreibt den Fluss als $\phi$. Auch hier gilt die Regel von oben: Das
kursive $C$ der Kapazität ist eine Größe, das aufrechte $\text{C}$ des Coulomb eine Einheit.

**Im Bild:** Jede Zeile ist ein Bauwerk. Die eigenen Namen — Newton, Volt, Ohm — sind Spitznamen für häufig gebaute Bauwerke;
dahinter stehen immer nur Grundsteine mit Exponenten.

**Woher die Einheiten kommen.** Jede Zeile folgt aus der Gleichung, die die Größe festlegt: Die Einheit einer Größe ist die Einheit
der rechten Seite ihrer Definitionsgleichung. Die meisten dieser Gleichungen kommen erst in späteren Kapiteln; für die Einheit
genügt schon ihre Form.

:::herleitung
Schritt für Schritt, jeweils mit der festlegenden Gleichung in Worten:

- **Kraft** ist Masse mal Beschleunigung, weiter unten im Artikel: Kilogramm mal Meter pro Sekundenquadrat.
- **Arbeit** ist Kraft mal Weg, also $\text{N}\,\text{m}$ und damit $\text{kg}\,\text{m}^2\,\text{s}^{-2}$. **Leistung** ist Arbeit pro Zeit, ein Sekunden-Stein mehr im Nenner.
- **Druck** ist Kraft pro Fläche, also Newton durch Quadratmeter.
- **Ladung** ist Strom mal Zeit, also $\text{A}\,\text{s}$.
- **Spannung** ist Energie pro Ladung (Kapitel 3), also Joule durch Amperesekunde: $\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-1}$. Weil Leistung Spannung mal Strom ist, ist das Volt auch Watt pro Ampere.
- **Widerstand** ist Spannung pro Strom (Kapitel 5): ein Ampere-Stein mehr im Nenner.
- **Kapazität** ist Ladung pro Spannung (Kapitel 4). Das Volt im Nenner bringt seine Steine mit umgekehrten Exponenten mit: $\text{A}\,\text{s}$ mal $\text{kg}^{-1}\,\text{m}^{-2}\,\text{s}^{3}\,\text{A}$ ergibt $\text{A}^2\,\text{s}^4\,\text{kg}^{-1}\,\text{m}^{-2}$.
- **Induktivität** verknüpft die Spannung mit der Änderung des Stroms: Spannung gleich Induktivität mal Stromänderung pro Zeit. Also Volt mal Sekunde durch Ampere.
- **Magnetischer Fluss**: Die induzierte Spannung ist seine Änderung pro Zeit, also Volt mal Sekunde. **Flussdichte** ist Fluss pro Fläche.

Die Einheiten rechnet man dabei wie Faktoren aus, genau wie im Abschnitt über das Rechnen mit Einheiten.
:::

::::beispiel Das Ohm in Grundsteinen
**(a) Zerlegen.** Über die Kette der festlegenden Gleichungen — Volt gleich Joule pro Coulomb, Joule gleich Newton mal Meter,
Newton gleich Kilogramm mal Meter pro Sekundenquadrat:

$$1\,\Omega = 1\,\frac{\text{V}}{\text{A}} = 1\,\frac{\text{J}}{\text{A}^2\,\text{s}} = 1\,\frac{\text{N}\,\text{m}}{\text{A}^2\,\text{s}} = 1\,\frac{\text{kg}\,\text{m}^2}{\text{s}^3\,\text{A}^2}.$$

**(b) Ohm mal Farad.** Volt und Ampere kürzen sich, übrig bleibt die Sekunde:

$$1\,\Omega\cdot1\,\text{F} = 1\,\frac{\text{V}}{\text{A}}\cdot\frac{\text{A}\,\text{s}}{\text{V}} = 1\,\text{s}.$$

Das Produkt aus Widerstand und Kapazität ist eine Zeit — die Zeitkonstante, mit der sich ein Kondensator über einen Widerstand
lädt (Kapitel 4).

**(c) Die Kilowattstunde.** Leistung mal Zeit ist Energie:

$$1\,\text{kWh} = 1000\,\text{W}\cdot3600\,\text{s} = 3{,}6\cdot10^{6}\,\text{W}\,\text{s} = 3{,}6\,\text{MJ}.$$

**Im Bild:** Bei (b) stehen Volt- und Ampere-Steine einmal oben und einmal unten und fallen heraus; übrig bleibt ein einzelner
Sekunden-Stein. Bei (c) ist die Kilowattstunde auf der Stromrechnung ein Joule-Bauwerk in großer Packung.
::::

## Einheitenvorsätze

Größen der Elektrotechnik überspannen viele Größenordnungen, vom Pikofarad in einer Schaltung bis zum Gigawatt im Kraftwerk.
Statt Zehnerpotenzen mitzuschleppen, stellt man der Einheit einen __Einheitenvorsatz__ voran. Er skaliert den Zahlenwert mit einer
Zehnerpotenz mit ganzzahligem Exponenten. Dafür gelten vier Regeln:

- Vorsätze für Teile einer Einheit schreibt man klein, etwa Milli für ein Tausendstel; Vorsätze für Vielfache groß, etwa Mega für
  eine Million. Aus historischen Gründen weichen Deka ($\text{da}$), Hekto ($\text{h}$) und Kilo ($\text{k}$) davon ab.
- Vor einer Einheit steht immer nur **ein** Vorsatz: Nanofarad, nicht „Millimikrofarad".
- Vorsatz und Einheit bilden **ein** Zeichen, Klammern braucht man nicht. Eine Potenz gilt deshalb für beide zusammen:
  $\text{km}^2$ ist das Quadrat eines Kilometers.
- Beim Kilogramm steckt der Vorsatz schon im Namen. Vorsätze hängen deshalb am Gramm: Milligramm, nicht „Mikrokilogramm".

| Vorsatz | Zeichen | Faktor | in Worten |
|---|---|---|---|
| Dezi | $\text{d}$ | $10^{-1}$ | Zehntel |
| Zenti | $\text{c}$ | $10^{-2}$ | Hundertstel |
| Milli | $\text{m}$ | $10^{-3}$ | Tausendstel |
| Mikro | $\mu$ | $10^{-6}$ | Millionstel |
| Nano | $\text{n}$ | $10^{-9}$ | Milliardstel |
| Piko | $\text{p}$ | $10^{-12}$ | Billionstel |
| Femto | $\text{f}$ | $10^{-15}$ | Billiardstel |
| Atto | $\text{a}$ | $10^{-18}$ | Trillionstel |

| Vorsatz | Zeichen | Faktor | in Worten |
|---|---|---|---|
| Deka | $\text{da}$ | $10^{1}$ | Zehn |
| Hekto | $\text{h}$ | $10^{2}$ | Hundert |
| Kilo | $\text{k}$ | $10^{3}$ | Tausend |
| Mega | $\text{M}$ | $10^{6}$ | Million |
| Giga | $\text{G}$ | $10^{9}$ | Milliarde |
| Tera | $\text{T}$ | $10^{12}$ | Billion |
| Peta | $\text{P}$ | $10^{15}$ | Billiarde |
| Exa | $\text{E}$ | $10^{18}$ | Trillion |

Das SI kennt noch weitere Vorsätze bis $10^{30}$ und $10^{-30}$, zuletzt 2022 ergänzt; in der Elektrotechnik kommen sie kaum vor.

**Im Bild:** Vorsätze sind Packungsgrößen. Ein Kiloohm ist der Tausenderpack Ohm, ein Mikrofarad ein Millionstel Farad. An der
Menge ändert die Verpackung nichts.

:::grafik
Szene: get1/physikalische-grundprinzipien/01-vorsaetze · Vorlage: zehnerpotenz-skala
Ein waagerechter Zahlenstrahl der Zehnerpotenzen von $10^{-18}$ bis $10^{18}$, in Dreierschritten mit a, f, p, n, µ, m, k, M, G, T,
P, E beschriftet, dazwischen kleiner d, c, da, h. Typische Bauteilwerte springen an ihre Stelle: $100\,\text{pF}$, $2{,}2\,\mu\text{F}$,
$4{,}7\,\text{k}\Omega$, $1\,\text{GW}$ für ein Kraftwerk. Ein Regler verschiebt einen Wert und zeigt, wie sich Vorsatz und Zahlenwert
gemeinsam ändern. Kernaussage: Ein Vorsatz ist eine Zehnerpotenz, die man in die Einheit verpackt. (Blau = Skala, rot = der
gewählte Wert, orange = Vorsatz und Zahlenwert, grau = Teilstriche.)
:::

**Vorsicht bei Potenzen.** Weil Vorsatz und Einheit zusammengehören, wird beim Potenzieren auch der Vorsatz potenziert:

$$1\,\text{km}^2 = \big(10^{3}\,\text{m}\big)^2 = 10^{6}\,\text{m}^2.$$

:::herleitung
$\text{km}^2$ bedeutet $(\text{km})^2$, und ein Kilometer sind $10^3$ Meter. Nach den Potenzgesetzen quadriert man Zahl und Einheit
einzeln:

$$\big(10^{3}\,\text{m}\big)^2 = 10^{3\cdot2}\,\text{m}^2 = 10^{6}\,\text{m}^2.$$

Läse man den Vorsatz nur einmal, käme $10^3\,\text{m}^2$ heraus — tausendmal zu wenig: Ein Quadrat von einem Kilometer
Seitenlänge enthält eine Million Quadrate von einem Meter.
:::

::::beispiel Vorsätze richtig lesen
**(a) Bauteilwerte.** Mit dem passenden Vorsatz werden die Zahlen handlich:

$$4700\,\Omega = 4{,}7\,\text{k}\Omega, \qquad 0{,}000\,002\,2\,\text{F} = 2{,}2\,\mu\text{F}, \qquad 1\cdot10^{-10}\,\text{F} = 100\,\text{pF}.$$

**(b) Potenzen.** Der Vorsatz wird mitpotenziert:

$$1\,\text{cm}^3 = \big(10^{-2}\,\text{m}\big)^3 = 10^{-6}\,\text{m}^3, \qquad 1\,\text{dm}^3 = 10^{-3}\,\text{m}^3 = 1\,\text{Liter}.$$

**(c) Das Kilogramm.** Der Vorsatz hängt am Gramm:

$$1\,\text{mg} = 10^{-3}\,\text{g} = 10^{-6}\,\text{kg}.$$

**(d) Ein Leerzeichen macht den Unterschied.** $\text{ms}$ ist eine Millisekunde, $\text{m}\,\text{s}$ dagegen Meter mal Sekunde. Ebenso
ist $\text{mN}$ ein Millinewton, $\text{m}\,\text{N}$ ein Newtonmeter.

**Im Bild:** Bei (b) steckt in einem Würfel von einem Zentimeter Kantenlänge nicht ein Hundertstel, sondern ein Millionstel des
Meterwürfels — hundert mal hundert mal hundert kleine Würfel füllen den großen.
::::

## Physikalische Gleichungen: Geschwindigkeit und Beschleunigung

Physikalische Gleichungen beschreiben gesetzmäßige Zusammenhänge zwischen Größen. Das Skript nennt als erstes Beispiel das
Ohmsche Gesetz, Spannung gleich Widerstand mal Strom:

$$U = R\cdot I.$$

Eine solche Gleichung heißt __Größengleichung__: Sie verknüpft die Größen selbst, jeweils Zahlenwert mal Einheit, und gilt deshalb
unabhängig davon, in welchen Einheiten man die Werte angibt. Solche Gesetzmäßigkeiten zu finden ist Aufgabe der Physik. Die
Ingenieurwissenschaften wenden sie an — in Bauelementen, Schaltungen, Kraftwerken und Fahrzeugen.

**Im Bild:** In einer Größengleichung stehen links und rechts dieselben Bauwerke. Beim Ohmschen Gesetz ist Ohm mal Ampere wieder
Volt, weil das Ohm Volt pro Ampere ist.

Das Skript übt den Umgang mit Größengleichungen an der Bewegung eines Körpers. Dabei tauchen zum ersten Mal Ableitung und Integral
als physikalische Werkzeuge auf.

**Geschwindigkeit als Steigung.** Ein Körper bewegt sich längs einer Strecke; $s(t)$ ist der Weg, den er bis zur Zeit $t$
zurückgelegt hat. Eingabe ist die Zeit, Ausgabe der Weg. Bewegt er sich gleichförmig, ist der Graph von $s$ über $t$ eine Gerade,
und die Geschwindigkeit ist ihre Steigung, Wegstück durch Zeitstück:

$$v = \frac{\Delta s}{\Delta t}.$$

Bei einer beschleunigten Bewegung ist der Graph gekrümmt. Dann hängt der Quotient davon ab, wie lang man das Zeitstück wählt, und
gibt nur die mittlere Geschwindigkeit in diesem Zeitstück. Die Geschwindigkeit in einem Augenblick erhält man, indem man das
Zeitstück gegen null schrumpfen lässt — aus der Sekante durch zwei Punkte des Graphen wird die Tangente in einem Punkt:

:::formel Definition
$$v(t) = \lim_{\Delta t\to0}\frac{\Delta s}{\Delta t} = \frac{ds}{dt}, \qquad a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}.$$
:::

**So liest man das:** Die Geschwindigkeit ist die Ableitung des Wegs nach der Zeit, die Steigung des $s$-$t$-Graphen im jeweiligen
Augenblick. Die __Beschleunigung__ ist die Ableitung der Geschwindigkeit, also die zweite Ableitung des Wegs. Konstante Steigung
im $s$-$t$-Graphen heißt konstante Geschwindigkeit.

**Im Bild:** Ableiten teilt durch einen Zeit-Stein. Aus Meter wird Meter pro Sekunde, daraus Meter pro Sekundenquadrat.

:::herleitung
**Die Einheiten.** Der Differenzenquotient ist ein Weg durch eine Zeit, also Meter durch Sekunde. Der Grenzübergang ändert die
Zahlen, nicht die Einheit. Für die Beschleunigung teilt man noch einmal durch eine Zeit:

$$[v] = \frac{\text{m}}{\text{s}}, \qquad [a] = \frac{\text{m}/\text{s}}{\text{s}} = \frac{\text{m}}{\text{s}^2}.$$

**Konstante Steigung.** Eine Gerade hat überall dieselbe Steigung, und die Ableitung einer linearen Funktion ist konstant. Umgekehrt
ist eine Funktion mit überall gleicher Ableitung linear — der Graph ist eine Gerade.
:::

::::beispiel Sekante und Tangente
Ein Körper startet aus der Ruhe und legt den Weg

$$s(t) = 0{,}5\,\frac{\text{m}}{\text{s}^2}\cdot t^2$$

zurück. Bei $t=4\,\text{s}$ ist er $8\,\text{m}$ weit gekommen. Die mittlere Geschwindigkeit in den ersten vier Sekunden ist
$\frac{8\,\text{m}}{4\,\text{s}}$, also $2\,\frac{\text{m}}{\text{s}}$.

Lässt man das Zeitstück ab $t=4\,\text{s}$ schrumpfen, nähert sich der Differenzenquotient einem festen Wert:

| $\Delta t$ | $s(4\,\text{s}+\Delta t)$ | $\frac{\Delta s}{\Delta t}$ |
|---|---|---|
| $1\,\text{s}$ | $12{,}5\,\text{m}$ | $4{,}5\,\frac{\text{m}}{\text{s}}$ |
| $0{,}1\,\text{s}$ | $8{,}405\,\text{m}$ | $4{,}05\,\frac{\text{m}}{\text{s}}$ |
| $0{,}01\,\text{s}$ | $8{,}040\,05\,\text{m}$ | $4{,}005\,\frac{\text{m}}{\text{s}}$ |

Die Ableitung gibt den Grenzwert direkt, dazu die konstante Beschleunigung:

$$v(t) = 1\,\frac{\text{m}}{\text{s}^2}\cdot t, \qquad v(4\,\text{s}) = 4\,\frac{\text{m}}{\text{s}}, \qquad a = 1\,\frac{\text{m}}{\text{s}^2}.$$

**Im Bild:** Die Sekante vom Start bis $t=4\,\text{s}$ ist nur halb so steil wie die Tangente dort — der Körper wird ja immer
schneller, im Mittel war er langsamer als am Ende.
::::

**Rückwärts: integrieren.** Kennt man die Geschwindigkeit, erhält man den Weg durch Integration, und aus der Beschleunigung die
Geschwindigkeit:

$$s(t_1) = s(t_0)+\int_{t_0}^{t_1}v(t)\;dt, \qquad v(t) = v(t_0)+\int_{t_0}^{t}a(\tau)\;d\tau.$$

Der Weg folgt aus der Beschleunigung also durch zweifache Integration. Das Skript schreibt das ohne die Anfangswerte; ohne sie
legt die Integration den Weg aber nur bis auf eine Konstante fest. In der zweiten Formel heißt die Integrationsvariable $\tau$, weil
$t$ schon die obere Grenze ist.

**So liest man das:** Der zurückgelegte Weg ist die Fläche unter dem $v$-$t$-Graphen.

**Im Bild:** Integrieren über die Zeit setzt einen Sekunden-Stein dazu: Meter pro Sekunde mal Sekunde ergibt Meter.

:::herleitung
Nach dem Hauptsatz der Differential- und Integralrechnung ist das Integral einer Ableitung die Differenz der Funktionswerte an den
Grenzen. Weil $v$ die Ableitung von $s$ ist,

$$\int_{t_0}^{t_1}v(t)\;dt = \int_{t_0}^{t_1}\frac{ds}{dt}\;dt = s(t_1)-s(t_0).$$

Genauso für $v$ und $a$. Das Integral ist der Grenzwert von Summen aus Geschwindigkeit mal kleinem Zeitstück, also von kleinen
Wegstücken — anschaulich Streifen unter dem Graphen.
:::

**Gleichmäßig beschleunigt.** Ist die Beschleunigung $a$ konstant, ergeben die beiden Integrationen mit dem Anfangsort $s_0$ und der
Anfangsgeschwindigkeit $v_0$ zur Zeit $t_0$:

:::formel
$$v(t) = v_0+a\,(t-t_0), \qquad s(t) = s_0+v_0\,(t-t_0)+\frac12\,a\,(t-t_0)^2.$$
:::

**So liest man das:** Die Geschwindigkeit wächst linear mit der Zeit, der Ort quadratisch. Das Skript schreibt das Ergebnis als
$\Delta s$; gemeint ist der Ort $s(t_1)$, denn der Anfangsort $s_0$ ist schon enthalten. Der zurückgelegte Weg ist $s(t_1)-s_0$.

**Im Bild:** Im $v$-$t$-Graphen ist die Geschwindigkeit eine Gerade. Die Fläche darunter besteht aus einem Rechteck der Höhe $v_0$
und einem Dreieck darauf, das halb so groß ist wie das Rechteck um es herum — daher der Faktor $\frac12$.

:::herleitung
Mit konstanter Beschleunigung ist das erste Integral sofort ausgerechnet:

$$v(t) = v_0+\int_{t_0}^{t}a\;d\tau = v_0+a\,(t-t_0).$$

Eingesetzt in das zweite, mit $\tau$ als Integrationsvariable:

$$s(t) = s_0+\int_{t_0}^{t}\big(v_0+a\,(\tau-t_0)\big)\;d\tau = s_0+v_0\,(t-t_0)+a\,\frac{(t-t_0)^2}{2}.$$

Das letzte Integral ist das Dreieck: Grundseite $t-t_0$, Höhe $a\,(t-t_0)$, Fläche die Hälfte des Produkts.
:::

:::grafik
Szene: get1/physikalische-grundprinzipien/01-steigung-und-flaeche · Vorlage: weg-zeit-geschwindigkeit
Links der Weg-Zeit-Graph einer gleichmäßig beschleunigten Bewegung, eine nach oben gekrümmte Parabel. Durch zwei Punkte eine
Sekante; ein Regler verkleinert den Abstand der Punkte, bis die Sekante in die Tangente übergeht, und ein Zähler zeigt dabei den
Differenzenquotienten. Rechts der Geschwindigkeit-Zeit-Graph derselben Bewegung, eine schräge Gerade; die Fläche darunter ist in
ein Rechteck der Höhe $v_0$ und ein Dreieck geteilt, und ein Zähler zeigt die Fläche als zurückgelegten Weg. Kernaussage:
Geschwindigkeit ist die Steigung des Wegs, Weg die Fläche unter der Geschwindigkeit. (Blau = Graphen, rot = Tangente und Fläche,
orange = Sekante und Zähler, grau = Achsen, gestrichelt = Rechteck um das Dreieck.)
:::

::::beispiel Straßenbahn und Stein
**(a) Eine Straßenbahn** fährt aus dem Stand an und hat nach $10\,\text{s}$ die Geschwindigkeit $36\,\frac{\text{km}}{\text{h}}$. Ein
Kilometer pro Stunde sind $\frac{1000\,\text{m}}{3600\,\text{s}}$, also

$$36\,\frac{\text{km}}{\text{h}} = 10\,\frac{\text{m}}{\text{s}}, \qquad a = \frac{10\,\text{m}/\text{s}}{10\,\text{s}} = 1\,\frac{\text{m}}{\text{s}^2}.$$

Der Anfahrweg, mit Start bei null und ohne Anfangsgeschwindigkeit:

$$s = \frac12\cdot1\,\frac{\text{m}}{\text{s}^2}\cdot(10\,\text{s})^2 = 50\,\text{m}.$$

**(b) Ein Stein** fällt aus der Ruhe zwei Sekunden lang, ohne Luftwiderstand, mit der Fallbeschleunigung $9{,}81\,\frac{\text{m}}{\text{s}^2}$:

$$v = 9{,}81\,\frac{\text{m}}{\text{s}^2}\cdot2\,\text{s} \approx 19{,}6\,\frac{\text{m}}{\text{s}}, \qquad s = \frac12\cdot9{,}81\,\frac{\text{m}}{\text{s}^2}\cdot(2\,\text{s})^2 \approx 19{,}6\,\text{m}.$$

Die Geschwindigkeit ist gut $70\,\frac{\text{km}}{\text{h}}$.

**Im Bild:** In beiden Rechnungen kürzen sich die Sekunden-Steine: Meter pro Sekundenquadrat mal Sekundenquadrat ist Meter. Dass
Geschwindigkeit und Weg beim Stein dieselbe Zahl haben, ist Zufall der zwei Sekunden — die Einheiten sind verschieden.
::::

## Kraft und Arbeit

**Kraft.** Eine __Kraft__ ist eine Einwirkung, die einen festgehaltenen Körper verformt oder einen beweglichen beschleunigt. Nach
Newton ist sie Masse mal Beschleunigung; sie zeigt in die Richtung der Beschleunigung:

:::formel Definition
$$\vec F = m\cdot\vec a, \qquad [F] = \text{kg}\,\frac{\text{m}}{\text{s}^2} = \text{N}.$$
:::

**So liest man das:** Eingabe sind die Masse, ein Skalar in Kilogramm, und die Beschleunigung, ein Vektor in Meter pro
Sekundenquadrat. Heraus kommt die Kraft, ein Vektor in Newton; ihr Betrag ist $F$. Ein Newton beschleunigt ein Kilogramm um einen
Meter pro Sekundenquadrat. Das Skript schreibt die Beträge, $F=m\cdot a$.

**Im Bild:** Das Newton-Bauwerk ist genau das: ein Kilogramm-Stein, ein Meter-Stein und zwei Sekunden-Steine im Nenner.

**Das Gravitationsgesetz.** Zwei Massen $m$ und $M$ im Abstand $r$ ziehen sich mit der Kraft

:::formel Gesetz
$$F = \gamma\,\frac{m\cdot M}{r^2}$$
:::

an. Dabei ist $\gamma$ die __Gravitationskonstante__, eine Naturkonstante:

$$\gamma = 6{,}674\,30\cdot10^{-11}\,\frac{\text{m}^3}{\text{kg}\,\text{s}^2}.$$

Das Gesetz lässt sich nicht aus Einfacherem herleiten. Newton hat es aus Beobachtungen der Planetenbahnen gewonnen, und Messungen
bestätigen es bis heute. Die Einheit der Konstante folgt aber aus der Gleichung.

**Im Bild:** Die Konstante ist genau das Bauwerk, das links und rechts gleich macht: Kilogramm mal Kilogramm durch Meterquadrat soll
Newton ergeben.

:::herleitung
Man löst nach der Konstante auf und setzt die Einheiten ein:

$$\gamma = \frac{F\,r^2}{m\,M}, \qquad [\gamma] = \frac{\text{N}\,\text{m}^2}{\text{kg}^2} = \frac{\text{kg}\,\text{m}\,\text{s}^{-2}\,\text{m}^2}{\text{kg}^2} = \frac{\text{m}^3}{\text{kg}\,\text{s}^2}.$$
:::

::::beispiel Wie schwer ist ein Kilogramm?
Auf ein Kilogramm an der Erdoberfläche wirkt die Anziehung der Erde, mit ihrer Masse und ihrem mittleren Radius

$$M = 5{,}972\cdot10^{24}\,\text{kg}, \qquad r = 6{,}371\cdot10^{6}\,\text{m}.$$

Die Kraft pro Kilogramm, also die Beschleunigung, die die Erde jedem Körper gibt:

$$\frac{F}{m} = \gamma\,\frac{M}{r^2} = 6{,}674\cdot10^{-11}\,\frac{\text{m}^3}{\text{kg}\,\text{s}^2}\cdot\frac{5{,}972\cdot10^{24}\,\text{kg}}{\big(6{,}371\cdot10^{6}\,\text{m}\big)^2} \approx 9{,}82\,\frac{\text{m}}{\text{s}^2}.$$

Ein Kilogramm wiegt also rund $9{,}8\,\text{N}$. Das ist fast genau die Fallbeschleunigung $g\approx9{,}81\,\frac{\text{m}}{\text{s}^2}$; den
kleinen Rest machen vor allem die Erddrehung und die abgeplattete Form der Erde aus.

**Im Bild:** Die Einheiten gehen glatt auf: Kilogramm kürzt sich gegen Kilogramm, Meter hoch drei durch Meterquadrat lässt ein
Meter übrig — heraus kommt eine Beschleunigung.
::::

**Arbeit.** Wird ein Körper unter der Wirkung einer Kraft verschoben, wird an ihm __Arbeit__ verrichtet: Energie wird auf
mechanischem Weg übertragen. Im einfachsten Fall wirkt die Kraft genau in Richtung der Verschiebung um das Wegstück $\Delta s$:

$$\Delta W = F\cdot\Delta s.$$

Arbeit ist Kraft mal Weg, die Einheit ist das Newtonmeter, gleich dem Joule. Schließen die Kraft und die Verschiebung
$\Delta\vec s$ den Winkel $\alpha$ ein, zählt nur der Anteil der Kraft in Bewegungsrichtung:

$$\Delta W = \vec F\cdot\Delta\vec s = F\cdot\Delta s\cdot\cos\alpha.$$

**So liest man das:** Das Skalarprodukt nimmt zwei Vektoren und gibt eine Zahl aus. Für einen Winkel über $90^\circ$ wirkt die Kraft
gegen die Bewegung, und die Arbeit ist negativ. Das Skript setzt das Skalarprodukt in Betragsstriche; damit ginge dieses Vorzeichen
verloren — richtig ist die Formel ohne Betrag.

**Im Bild:** Wer einen Koffer waagerecht trägt, verrichtet an ihm im Sinn der Physik keine Arbeit: Die Haltekraft zeigt nach oben,
die Bewegung zur Seite, und der Kosinus von $90^\circ$ ist null.

:::herleitung
Man zerlegt die Verschiebung in einen Anteil längs der Kraft und einen senkrecht dazu. Der Anteil längs der Kraft hat die Länge
$\Delta s\cdot\cos\alpha$, wie im rechtwinkligen Dreieck aus Verschiebung und ihren beiden Anteilen. Längs der Kraft gilt die
einfache Formel; senkrecht dazu hat die Kraft keinen Anteil und verrichtet nichts:

$$\Delta W = F\cdot\Delta s\cos\alpha+0.$$

Das ist genau das Skalarprodukt zweier Vektoren: Betrag mal Betrag mal Kosinus des eingeschlossenen Winkels.
:::

:::grafik
Szene: get1/physikalische-grundprinzipien/01-arbeit-und-winkel · Vorlage: kraft-weg-winkel
Ein Körper auf einer Ebene, ein Kraftpfeil $\vec F$ schräg nach oben und ein Verschiebungspfeil $\Delta\vec s$ waagerecht, dazwischen
der Winkel $\alpha$. Gestrichelt die Zerlegung der Verschiebung in den Anteil längs der Kraft und den Anteil senkrecht dazu. Ein
Regler dreht die Kraft von $0^\circ$ über $90^\circ$ bis $180^\circ$; ein Zähler zeigt $F\,\Delta s\cos\alpha$, das von positiv über null
ins Negative wandert. Kernaussage: Arbeit verrichtet nur der Kraftanteil längs des Wegs. (Rot = Verschiebung, blau = Kraft, orange =
Winkel und Zähler, gestrichelt = Zerlegung, grau = Ebene.)
:::

**Das Wegintegral.** Ändert sich die Kraft längs des Wegs oder ist der Weg gekrümmt, zerlegt man ihn in kleine Stücke $d\vec s$, auf
denen die Kraft praktisch konstant ist, und summiert ihre Arbeiten. Im Grenzfall immer kleinerer Stücke wird daraus das
__Wegintegral__, auch __Linienintegral__, längs des Wegs vom Startpunkt $P_1$ zum Zielpunkt $P_2$:

:::formel Definition
$$W = \int_{P_1}^{P_2}\vec F\cdot d\vec s.$$
:::

**So liest man das:** Eingabe ist ein Weg samt der Kraft in jedem seiner Punkte, Ausgabe eine Zahl, die Arbeit in Joule. An jedem
Wegstück zählt nur der Kraftanteil längs des Wegs.

**Im Bild:** Newton-Bauwerk mal Meter-Stein ergibt Joule, Stück für Stück aufaddiert. Im Schwerefeld zählen nur die Wegstücke nach
oben oder unten; waagerechte Stücke tragen nichts bei.

:::herleitung
Auf jedem der kleinen Wegstücke $\Delta\vec s_i$ wirkt näherungsweise eine feste Kraft $\vec F_i$, und die Arbeit dort ist nach der
Formel oben ihr Skalarprodukt. Die Summe über alle Stücke

$$W \approx \sum_i\vec F_i\cdot\Delta\vec s_i$$

wird umso genauer, je kleiner die Stücke sind. Ihr Grenzwert für immer feinere Zerlegungen ist das Wegintegral — so, wie das
gewöhnliche Integral der Grenzwert von Streifensummen ist.
:::

::::beispiel Eine Kiste auf der Rampe
Eine Kiste der Masse $2\,\text{kg}$ rutscht eine Rampe hinab: $5\,\text{m}$ lang, $3\,\text{m}$ Höhenunterschied, also $4\,\text{m}$
waagerecht. Mit der Fallbeschleunigung $9{,}81\,\frac{\text{m}}{\text{s}^2}$ ist die Gewichtskraft

$$F = 2\,\text{kg}\cdot9{,}81\,\frac{\text{m}}{\text{s}^2} = 19{,}62\,\text{N},$$

senkrecht nach unten. Zwischen ihr und der Rampe liegt der Winkel, dessen Kosinus Höhe durch Länge ist:

$$\cos\alpha = \frac{3\,\text{m}}{5\,\text{m}} = 0{,}6, \qquad W = 19{,}62\,\text{N}\cdot5\,\text{m}\cdot0{,}6 \approx 58{,}9\,\text{J}.$$

**Stückweise, wie im Skript:** Zerlegt man den Weg in $4\,\text{m}$ waagerecht und $3\,\text{m}$ senkrecht, trägt das waagerechte Stück
nichts bei und das senkrechte alles:

$$W = 19{,}62\,\text{N}\cdot4\,\text{m}\cdot\cos90^\circ+19{,}62\,\text{N}\cdot3\,\text{m}\cdot\cos0^\circ \approx 58{,}9\,\text{J}.$$

Schiebt man die Kiste wieder hinauf, verrichtet die Schwerkraft die Arbeit $-58{,}9\,\text{J}$: Kraft und Bewegung schließen dann
einen stumpfen Winkel ein.

**Im Bild:** Für die Arbeit der Schwerkraft zählt nur der Höhenunterschied, nicht die Form des Wegs. Die Einheit stimmt: Newton mal
Meter ist Joule.
::::

## Rechnen mit Einheiten

Aus der Definition Zahlenwert mal Einheit folgen alle Regeln für das Rechnen mit Einheiten: Zahlenwerte und Einheiten werden
getrennt behandelt, und die Einheiten verhalten sich wie Faktoren.

**Addieren nur bei gleicher Einheit.** Zwei Größen lassen sich nur addieren, wenn sie dieselbe Einheit haben; das Ergebnis hat
wieder diese Einheit:

$$G_1+G_2 = \big(\{G_1\}+\{G_2\}\big)\cdot[G] \qquad\text{für } [G_1] = [G_2] = [G].$$

Muss man scheinbar verschiedene Einheiten addieren, steckt fast immer ein Rechenfehler dahinter — deshalb eignen sich die Einheiten
gut zur Kontrolle. Verschiedene Vorsätze sind dagegen kein Hindernis: Sie ändern nicht die Einheit, sie skalieren nur den
Zahlenwert. Man muss sie aber als Faktor mitnehmen.

**Im Bild:** Nur gleiche Bauwerke lassen sich zusammenzählen. Drei Meter und zwei Sekunden sind zwei verschiedene Haufen.

:::herleitung
Bei gleicher Einheit klammert man sie nach dem Distributivgesetz aus:

$$\{G_1\}\cdot[G]+\{G_2\}\cdot[G] = \big(\{G_1\}+\{G_2\}\big)\cdot[G].$$

Bei verschiedenen Einheiten gibt es keinen gemeinsamen Faktor zum Ausklammern; die Summe lässt sich nicht als eine Zahl mal eine
Einheit schreiben. Unterscheiden sich nur die Vorsätze, rechnet man erst einen Wert in die Einheit des anderen um.
:::

**Multiplizieren geht immer.** Bei Produkten und Quotienten werden Zahlenwerte und Einheiten jeweils miteinander multipliziert; in
Brüchen kürzen sich Einheiten wie Zahlen. Zusammenhänge zwischen Einheiten darf man dabei nutzen, etwa Volt mal Ampere gleich
Watt, und fasst das Ergebnis meist zu einer passenden Einheit zusammen:

$$G_1\cdot G_2 = \big(\{G_1\}\cdot\{G_2\}\big)\cdot\big([G_1]\cdot[G_2]\big).$$

Vorsätze werden dabei als Zehnerpotenzen mitmultipliziert:

$$\text{k}\cdot\text{k} = 10^{3}\cdot10^{3} = \text{M}, \qquad \text{m}\cdot\mu = 10^{-3}\cdot10^{-6} = \text{n}, \qquad \mu\cdot\text{M} = 10^{-6}\cdot10^{6} = 1.$$

**Im Bild:** Beim Multiplizieren stellt man Bauwerke zusammen und zählt die Steine; gleiche Steine oben und unten fallen heraus.
Packungsgrößen multiplizieren sich mit.

:::herleitung
Ein Produkt von Größen ist ein Produkt von Faktoren. Nach dem Kommutativ- und dem Assoziativgesetz darf man sie beliebig ordnen:

$$\{G_1\}\cdot[G_1]\cdot\{G_2\}\cdot[G_2] = \big(\{G_1\}\cdot\{G_2\}\big)\cdot\big([G_1]\cdot[G_2]\big).$$

Ein Vorsatz ist selbst ein Faktor, eine Zehnerpotenz, und für Zehnerpotenzen addieren sich beim Multiplizieren die Exponenten.
:::

::::beispiel Einheiten, die mitrechnen
**(a) Addieren mit Vorsätzen.** Zwei Ströme in einem Knoten, erst in dieselbe Einheit gebracht:

$$250\,\text{mA}+1{,}2\,\text{A} = 0{,}25\,\text{A}+1{,}2\,\text{A} = 1{,}45\,\text{A}.$$

Wer stattdessen die Zahlen addiert, erhält $251{,}2$ — weder in Milliampere noch in Ampere richtig.

**(b) Multiplizieren.** Ein Lämpchen an $12\,\text{V}$ mit $0{,}5\,\text{A}$ und ein Drehmoment, geteilt durch einen Hebelarm:

$$12\,\text{V}\cdot0{,}5\,\text{A} = 6\,\text{V}\,\text{A} = 6\,\text{W}, \qquad \frac{1\,\text{N}\,\text{m}}{4\,\text{m}} = 0{,}25\,\text{N}.$$

**(c) Vorsätze im Produkt.** Ein Strom von $3\,\text{mA}$ durch $2\,\text{k}\Omega$ — Kilo mal Milli ist eins:

$$2\,\text{k}\Omega\cdot3\,\text{mA} = 6\cdot10^{3}\cdot10^{-3}\,\Omega\,\text{A} = 6\,\text{V}.$$

**Im Bild:** Bei (c) heben sich die beiden Packungsgrößen genau auf, und Ohm mal Ampere ergibt das Volt-Bauwerk.
::::

**Umrechnen.** Jede Einheit lässt sich in Basiseinheiten zerlegen, und oft gibt es mehrere gleichwertige Schreibweisen: Das Newton
ist Kilogramm mal Meter pro Sekundenquadrat, aber auch Joule pro Meter. Manchmal braucht man beim Umrechnen einen Zahlenfaktor,
etwa zwischen Stunden und Sekunden:

$$1\,\frac{\text{km}}{\text{h}} = 1\,\frac{\text{km}}{\text{h}}\cdot\frac{1000\,\text{m}}{1\,\text{km}}\cdot\frac{1\,\text{h}}{3600\,\text{s}} = \frac{1}{3{,}6}\,\frac{\text{m}}{\text{s}}.$$

**Im Bild:** Man tauscht Steine gegen gleichwertige Steine: einen Kilometer-Stein gegen tausend Meter-Steine.

:::herleitung
Jeder Umrechnungsbruch wie $\frac{1000\,\text{m}}{1\,\text{km}}$ ist eine Eins, denn Zähler und Nenner beschreiben dieselbe Länge.
Mit Eins zu multiplizieren ändert die Größe nicht; die Brüche sind nur so gewählt, dass sich die alten Einheiten herauskürzen.
:::

**Gleiche Steine, verschiedene Größen.** Zwei Einheiten mit derselben Zerlegung in Basiseinheiten können verschiedene Größen
bezeichnen. Hertz und Becquerel sind beide $\text{s}^{-1}$, aber das eine misst eine Frequenz, das andere die Zerfälle pro Sekunde eines
radioaktiven Stoffs. Das Newtonmeter ist die Einheit der Energie und die des Drehmoments. Umgekehrt heißt dieselbe Einheit je nach
Gebiet verschieden: Energie misst man in Wattsekunden in der Elektrotechnik, in Newtonmetern in der Mechanik und in Joule in der
Wärmelehre. Maßgeblich ist immer die Größe, zu der die Einheit gehört — einen Widerstand gibt man in Ohm an, nicht in Volt pro
Ampere.

**Im Bild:** Zwei gleich gebaute Häuser können eine Schule und ein Museum sein; erst die Nutzung sagt, was sie sind.

**Die Dimensionskontrolle.** Weil die Einheiten mitrechnen, prüft man jede hergeleitete Formel, bevor man Zahlen einsetzt. Man setzt
nur die Einheiten ein und schaut, ob links und rechts dasselbe herauskommt. Stimmt das nicht, ist der Ansatz falsch. Stimmt es,
kann trotzdem noch ein reiner Zahlenfaktor fehlen: Die Kontrolle findet falsche Ansätze, aber keine falschen Faktoren.

**Im Bild:** Eine zweite Buchführung, die neben der Rechnung mit Zahlen herläuft. Passen die Bauwerke links und rechts nicht
zusammen, ist irgendwo ein Stein verloren gegangen.

::::beispiel Ein Fehler, den die Einheiten verraten
**(a) Ein falscher Ansatz.** Jemand schreibt für den Anfahrweg aus dem Stand „Weg gleich halbe Beschleunigung mal Zeit". Die
Einheiten der rechten Seite:

$$\frac{\text{m}}{\text{s}^2}\cdot\text{s} = \frac{\text{m}}{\text{s}},$$

eine Geschwindigkeit, kein Weg — der Ansatz ist falsch. Mit dem Quadrat der Zeit stimmt es:

$$\frac{\text{m}}{\text{s}^2}\cdot\text{s}^2 = \text{m}.$$

**(b) Ein Widerstand.** Soll der Widerstand aus Spannung und Strom folgen, passt nur der Quotient: Volt durch Ampere ist Ohm, Volt
mal Ampere dagegen Watt.

**(c) Was die Kontrolle nicht findet.** „Weg gleich Beschleunigung mal Zeitquadrat" hat die richtige Einheit, ist aber doppelt so
groß wie richtig: Bei der Straßenbahn kämen $100\,\text{m}$ statt $50\,\text{m}$ heraus.

**Im Bild:** Bei (a) fehlt ein Sekunden-Stein im Nenner der Rechnung, und das Bauwerk wird zum falschen. Bei (c) stimmt das Bauwerk,
nur die Anzahl nicht — dafür ist die Kontrolle blind.
::::

## Bedeutung und Ausblick

Größen und Einheiten sind das Handwerkszeug für alles Weitere. In der Elektrotechnik rechnet man ständig mit Vorsätzen — Kiloohm,
Mikrofarad, Milliampere —, und jede Formel der folgenden Kapitel lässt sich mit der Dimensionskontrolle prüfen. Dass Ohm mal Farad
eine Sekunde ist, wird beim Laden eines Kondensators zur Zeitkonstante; dass Volt mal Ampere ein Watt ist, ist die elektrische
Leistung.

Auch Kraft und Arbeit kehren gleich wieder. Das nächste Kapitel beschreibt mit dem elektrischen Feld die Kraft auf eine Ladung, und
die Arbeit, die dieses Feld an einer Ladung verrichtet, führt auf das Potenzial und die Spannung — wieder als Wegintegral.

:::kern
- Jede __physikalische Größe__ ist $G=\{G\}\cdot[G]$, Zahlenwert mal Einheit; Formelzeichen kursiv, Einheitenzeichen aufrecht.
- Beim Wechsel der Einheit ändert sich der Zahlenwert gegenläufig; die Größe bleibt dieselbe.
- Das SI hat sieben __Basisgrößen__ — Länge, Masse, Zeit, Stromstärke, Temperatur, Lichtstärke, Stoffmenge —, seit 2019 über feste Naturkonstanten definiert.
- Das __Ampere__ hängt an der exakt festgelegten Elementarladung: Ein Ampere sind rund $6{,}24\cdot10^{18}$ Elementarladungen pro Sekunde.
- __Abgeleitete Einheiten__ sind Produkte von Potenzen der Basiseinheiten; Namen wie Volt oder Ohm sind Abkürzungen dafür.
- __Einheitenvorsätze__ skalieren mit Zehnerpotenzen; nur einer pro Einheit, und beim Potenzieren wird er mitpotenziert: $1\,\text{km}^2=10^6\,\text{m}^2$.
- Die Geschwindigkeit ist die Ableitung des Wegs, $v=\frac{ds}{dt}$, die Beschleunigung die der Geschwindigkeit; der Weg ist die Fläche unter dem $v$-$t$-Graphen.
- Bei konstanter Beschleunigung ist $s=s_0+v_0\,(t-t_0)+\frac12a\,(t-t_0)^2$.
- __Kraft__ ist Masse mal Beschleunigung, Einheit Newton; das __Gravitationsgesetz__ $F=\gamma\frac{mM}{r^2}$ ist ein Naturgesetz.
- __Arbeit__ ist Kraft mal Weg in Kraftrichtung, $\Delta W=F\,\Delta s\cos\alpha$, allgemein das Wegintegral der Kraft.
- Addieren nur bei gleicher Einheit, Multiplizieren immer; Vorsätze werden als Zehnerpotenzen mitgenommen.
- Die __Dimensionskontrolle__ findet falsche Ansätze, aber keine falschen Zahlenfaktoren.
:::

:::quiz
F: Warum gehören Zahlenwert und Einheit untrennbar zusammen, und was passiert beim Wechsel der Einheit?
A: Eine Größe ist das Produkt $G=\{G\}\cdot[G]$; die Zahl allein sagt nur, wie viele Einheiten es sind, aber nicht welche. Wechselt man zu einer kleineren Einheit, wächst der Zahlenwert um den Umrechnungsfaktor, und die Größe bleibt gleich: $0{,}25\,\text{m}$ sind $25\,\text{cm}$ oder $250\,\text{mm}$, eineinhalb Stunden sind $5400\,\text{s}$.
F: Was unterscheidet Basisgrößen von abgeleiteten Größen, und warum hat das SI einen elektrischen Grundstein?
A: Basisgrößen lassen sich nicht durch andere Basisgrößen ausdrücken; das SI hat sieben: Länge, Masse, Zeit, Stromstärke, Temperatur, Lichtstärke und Stoffmenge. Alle anderen sind abgeleitet, ihre Einheiten Produkte von Potenzen der Basiseinheiten. Die Stromstärke als eigene Basisgröße macht die elektrischen Einheiten handlich; im älteren Gaußschen System, das die Ladung mechanisch festlegt, bekommt die Ladungseinheit gebrochene Exponenten.
F: Wie ist das Ampere seit 2019 festgelegt, und wie viele Elektronen fließen bei $1\,\text{mA}$ in einer Sekunde?
A: Die Elementarladung hat den exakt festgelegten Wert $1{,}602\,176\,634\cdot10^{-19}\,\text{C}$, und ein Coulomb ist eine Amperesekunde. Ein Ampere transportiert also pro Sekunde $\frac{1\,\text{C}}{e}\approx6{,}24\cdot10^{18}$ Elementarladungen. Bei $1\,\text{mA}$ sind es in einer Sekunde rund $6{,}24\cdot10^{15}$ Elektronen; ein Akku mit $3000\,\text{mAh}$ speichert $10\,800\,\text{C}$.
F: Wie kommt man auf die Basiseinheiten des Ohm, und welche Einheit hat Ohm mal Farad?
A: Über die festlegenden Gleichungen: Ohm ist Volt pro Ampere, Volt ist Joule pro Coulomb, Joule ist Newton mal Meter, Newton ist Kilogramm mal Meter pro Sekundenquadrat — zusammen $\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-2}$. Ohm mal Farad ist Volt pro Ampere mal Amperesekunde pro Volt, also eine Sekunde: die Zeitkonstante beim Laden eines Kondensators.
F: Welche Regeln gelten für Einheitenvorsätze, und warum ist ein Quadratkilometer eine Million Quadratmeter?
A: Vorsätze skalieren mit ganzzahligen Zehnerpotenzen, klein für Teile, groß für Vielfache, mit den Ausnahmen da, h und k; vor einer Einheit steht nur einer, beim Kilogramm hängen sie am Gramm. Vorsatz und Einheit bilden ein Zeichen, also wird beim Potenzieren der Vorsatz mitpotenziert: $(10^3\,\text{m})^2=10^6\,\text{m}^2$, und ein Kubikzentimeter ist $10^{-6}\,\text{m}^3$.
F: Warum ist die Geschwindigkeit die Ableitung des Wegs, und was zeigt die Bewegung $s(t)=0{,}5\,\frac{\text{m}}{\text{s}^2}\,t^2$ bei $t=4\,\text{s}$?
A: Der Quotient aus Wegstück und Zeitstück ist die Steigung einer Sekante, also eine mittlere Geschwindigkeit; lässt man das Zeitstück schrumpfen, wird daraus die Tangente, die Geschwindigkeit im Augenblick. Bei der Beispielbewegung geben die Zeitstücke $1\,\text{s}$, $0{,}1\,\text{s}$ und $0{,}01\,\text{s}$ die Quotienten $4{,}5$, $4{,}05$ und $4{,}005\,\frac{\text{m}}{\text{s}}$, der Grenzwert ist $4\,\frac{\text{m}}{\text{s}}$ — doppelt so viel wie die mittlere Geschwindigkeit der ersten vier Sekunden.
F: Woher kommt der Faktor $\frac12$ bei der gleichmäßig beschleunigten Bewegung, und was ergibt sie für die Straßenbahn?
A: Man integriert die linear wachsende Geschwindigkeit $v_0+a\,(t-t_0)$; die Fläche unter dem $v$-$t$-Graphen ist ein Rechteck plus ein Dreieck, und das Dreieck ist halb so groß wie das Rechteck um es herum. Die Straßenbahn erreicht $36\,\frac{\text{km}}{\text{h}}$, also $10\,\frac{\text{m}}{\text{s}}$, in $10\,\text{s}$: Beschleunigung $1\,\frac{\text{m}}{\text{s}^2}$, Anfahrweg $\frac12\cdot1\,\frac{\text{m}}{\text{s}^2}\cdot(10\,\text{s})^2=50\,\text{m}$.
F: Was sagt das Gravitationsgesetz, welche Einheit hat die Gravitationskonstante, und was ergibt es an der Erdoberfläche?
A: Zwei Massen ziehen sich mit $F=\gamma\frac{mM}{r^2}$ an; das ist ein Naturgesetz aus Beobachtungen, keine Herleitung. Aufgelöst nach der Konstante folgt ihre Einheit $\frac{\text{N}\,\text{m}^2}{\text{kg}^2}=\frac{\text{m}^3}{\text{kg}\,\text{s}^2}$. Mit Erdmasse und Erdradius ergibt $\gamma\frac{M}{r^2}$ rund $9{,}82\,\frac{\text{m}}{\text{s}^2}$ — ein Kilogramm wiegt etwa $9{,}8\,\text{N}$.
F: Warum zählt bei der Arbeit nur der Kraftanteil in Wegrichtung, und was ergibt die Kiste auf der Rampe?
A: Zerlegt man die Verschiebung in einen Anteil längs der Kraft und einen senkrecht dazu, verrichtet die Kraft nur längs ihrer Richtung Arbeit: $\Delta W=F\,\Delta s\cos\alpha$, das Skalarprodukt, das auch negativ sein kann. Die $2$-kg-Kiste auf der Rampe von $5\,\text{m}$ Länge und $3\,\text{m}$ Höhe: $19{,}62\,\text{N}\cdot5\,\text{m}\cdot0{,}6\approx58{,}9\,\text{J}$ — dasselbe wie $19{,}62\,\text{N}\cdot3\,\text{m}$, weil das waagerechte Stück nichts beiträgt.
F: Welche Regeln gelten für Addition und Multiplikation von Größen, und was leistet die Dimensionskontrolle?
A: Addieren geht nur bei gleicher Einheit, Vorsätze rechnet man vorher um: $250\,\text{mA}+1{,}2\,\text{A}=1{,}45\,\text{A}$. Multiplizieren geht immer, Zahlen und Einheiten getrennt, Vorsätze als Zehnerpotenzen: $2\,\text{k}\Omega\cdot3\,\text{mA}=6\,\text{V}$. Die Dimensionskontrolle setzt nur Einheiten ein: „Weg gleich halbe Beschleunigung mal Zeit" ergibt Meter pro Sekunde und ist falsch; einen fehlenden Faktor zwei findet sie dagegen nicht.
:::
