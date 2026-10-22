---
title: Bindungstypen
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Kristallstruktur
order: 4020400
summary: Das Gitter beschreibt, wie die Atome angeordnet sind – die Bindung erklärt, warum. Vier Mechanismen (ionisch, kovalent, metallisch, van der Waals) führen Atome zur stabilen Edelgaskonfiguration. Besonders wichtig für die Halbleiter: die kovalente $sp^3$-Bindung, die über den Tetraederwinkel $\arccos(-\tfrac13)\approx109{,}47^\circ$ direkt zur Diamantstruktur von Silizium und Germanium führt.
tags: chemische Bindung, ionisch, kovalent, metallisch, van der Waals, sp3-Hybridisierung, Diamantstruktur, Oktettregel
---

:::grafik
Einstiegs-Animation: Vier Felder, in denen je ein Bindungstyp als „Film" abläuft. (1) __ionisch__: ein Elektron
springt von einem Atom zum anderen, zurück bleiben zwei entgegengesetzt geladene Ionen, die sich anziehen. (2)
__kovalent__: zwei Atome teilen sich ein Elektronenpaar in einer überlappenden Wolke. (3) __metallisch__: viele
Atome geben ihr äußeres Elektron ab, es entsteht ein „See" beweglicher Elektronen um positive Rümpfe. (4) __van
der Waals__: zwei neutrale Atome mit kurz aufblitzenden, zueinander passenden Dipolen. Kernbotschaft: Vier
verschiedene Wege, wie Elektronen eine Bindung herstellen.
:::

:::konzept
Die bisherigen Artikel haben **beschrieben**, wie Atome angeordnet sind (Gitter, Zelle, Ebenen). Jetzt kommt das
**Warum**: Warum sitzen die Atome überhaupt an diesen Plätzen und nicht anders? Die Antwort liefert die
__chemische Bindung__. Fast alle Bindungen verfolgen dasselbe Ziel: Jedes Atom möchte die besonders stabile
__Edelgaskonfiguration__ erreichen — eine **volle äußere Schale** (meist 8 Außenelektronen, die __Oktettregel__).
*Wie* die Atome das erreichen, unterscheidet die vier Bindungstypen. Für uns am wichtigsten ist die kovalente
Bindung, denn sie führt direkt zur Kristallstruktur von Silizium — dem Grundmaterial der gesamten Elektronik.
:::

**Worum es geht:** Wir gehen die vier __Bindungstypen__ durch und nennen bei jedem den **konkreten
Elektronen-Mechanismus**. Besonders ausführlich die kovalente Bindung: Wie aus der __$sp^3$-Hybridisierung__ der
Tetraeder und daraus die __Diamantstruktur__ von Si und Ge wird.

## Die gemeinsame Triebkraft: die volle Schale

Ein Atom ist energetisch am stabilsten, wenn seine äußerste Schale voll ist — so wie bei den reaktionsträgen
Edelgasen. Atome mit fast voller oder fast leerer Außenschale „suchen" deshalb nach einem Weg, diese
Konfiguration zu erreichen. Die vier Bindungstypen sind vier verschiedene Lösungen dieses einen Problems:

| Bindung | Wo? | Mechanismus | Elektronen |
|---|---|---|---|
| **ionisch** | Salze (NaCl, LiF) | Coulomb-Anziehung von Ionen | *übertragen* |
| **kovalent** | Halbleiter (Si, Diamant) | geteilte Bindungselektronen | *lokalisiert, geteilt* |
| **metallisch** | Metalle (Au, Cu, Al) | Elektronengas + Ionenrümpfe | *delokalisiert* |
| **van der Waals** | Graphit, $\text{MoS}_2$ | temporäre Dipole | *kein Austausch* |

## Das Bindungspotential: Gleichgewichtsabstand und Wärmeausdehnung

Bevor wir die einzelnen Typen durchgehen, der gemeinsame physikalische Rahmen — er gilt für **jede** Bindung und
erklärt nebenbei, warum sich Materialien beim Erwärmen ausdehnen. Zwischen zwei Bausteinen wirkt stets ein
**Wechselspiel** aus einer **anziehenden** und einer **abstoßenden** Kraft:

- die __anziehende Kraft__ $F_\text{an}$ wirkt weitreichend (je nach Bindungstyp z. B. Coulomb $F_\text{an}\sim
  r^{-2}$ im Ionenkristall oder van der Waals $F_\text{an}\sim r^{-6}$);
- die __abstoßende Kraft__ $F_\text{ab}$ wirkt erst bei **starker Annäherung**, dann aber sehr steil (z. B.
  $\sim r^{-12}$ oder exponentiell). Ihre Ursache ist das __Pauli-Prinzip__: Überlappen die gefüllten Orbitale,
  dürfen die Elektronen nicht in dieselben Zustände, was stark abstößt.

Kraft und Energie hängen über das **Energiegefälle** zusammen — die Kraft ist der negative Gradient der
potentiellen Energie $W(r)$:

$$F = -\frac{\mathrm{d}W}{\mathrm{d}r} \qquad\text{(allgemein }\ \vec F = -\operatorname{grad} W\text{)}.$$

Beide Kräfte zusammen ergeben eine **Potentialkurve** $W(r)$ mit einem **Minimum**. An dessen Stelle, dem
__Gleichgewichts- bzw. Bindungsabstand__ $r_0$, herrscht Kräftegleichgewicht $F_\text{an} = -F_\text{ab}$ (die
Gesamtkraft ist null). Die **Tiefe** des Minimums ist die __Bindungsenergie__ $W_0$ — die Energie, die man
aufbringen muss, um die Atome wieder zu trennen. Hier „sitzen" die Atome also: genau am Abstand $r_0$.

**Warum sich Materialien beim Erwärmen ausdehnen.** Die Atome ruhen nicht im Minimum, sondern **schwingen** um
$r_0$. Nach dem Gleichverteilungssatz trägt jede Schwingung im Mittel die thermische Energie $k_\text{B}T$; im
Energiebild liegt der Zustand also um rund $k_\text{B}T$ **über** dem Minimum, und die Schwingungsamplitude wird
durch die Potentialkurve begrenzt. Diese Kurve ist aber **unsymmetrisch** (die abstoßende Flanke ist viel steiler
als die anziehende). Dadurch verschiebt sich der **zeitliche Mittelwert** des Abstands mit steigender Temperatur
zu **größeren** Werten — das ist die Ursache der __thermischen Ausdehnung__. Wird $k_\text{B}T$ schließlich
vergleichbar mit $W_0$, gewinnt die thermische Bewegung die Oberhand: Das Material **schmilzt** und verdampft
letztlich.

:::grafik
Die Bindungs-Potentialkurve $W(r)$ über dem Atomabstand $r$: von links kommend steil abstoßend (Pauli), dann ein
Minimum bei $r_0$ der Tiefe $W_0$, nach rechts flach anziehend gegen null auslaufend. Eine waagerechte Linie
$k_\text{B}T$ über dem Minimum markiert die thermische Anregung; weil die Kurve unsymmetrisch ist, liegt die
Mitte dieser Linie rechts von $r_0$ — Pfeil „mittlerer Abstand wächst mit $T$ → Wärmeausdehnung". Zusätzlich
gestrichelt die beiden Anteile $F_\text{an}\sim r^{-2}/r^{-6}$ und $F_\text{ab}$ (steil).
:::

## Ionische Bindung: Elektronen wechseln den Besitzer

Bei der __ionischen Bindung__ *gibt* ein Atom Elektronen ab und ein anderes *nimmt* sie auf — ein echter
**Elektronentransfer**. Beide erreichen so die Edelgaskonfiguration und werden zu __Ionen__ entgegengesetzter
Ladung, die sich über die **Coulomb-Kraft** anziehen.

**Beispiel LiF:** Lithium ($1s^2\,2s^1$) hat ein einzelnes Außenelektron, Fluor ($1s^2\,2s^2\,2p^5$) hat genau
ein freies Plätzchen in der $2p$-Schale.

- Li gibt sein $2s$-Elektron ab → $\text{Li}^+$ (Konfiguration wie Helium).
- F nimmt es auf → $\text{F}^-$ (Konfiguration wie Neon).

Die so entstandenen Ionen ordnen sich zur **Steinsalz-Struktur**: zwei ineinandergestellte FCC-Gitter aus
$\text{Li}^+$ und $\text{F}^-$. Die Bindung entsteht allein durch die elektrostatische Anziehung — ganz ohne
geteilte Elektronen.

:::grafik
LiF-Entstehung: links die Schalenbilder von Li ($2s^1$) und F ($2p^5$); ein Pfeil zeigt das wandernde Elektron.
Rechts die zwei entstandenen Ionen $\text{Li}^+$ und $\text{F}^-$ mit „+/−" und einem Coulomb-Anziehungspfeil,
darunter das Steinsalz-Gitter (zwei verschachtelte FCC).
:::

## Kovalente Bindung: Elektronen werden geteilt

Bei der __kovalenten Bindung__ werden Elektronen nicht übertragen, sondern **geteilt**: Zwei Atome legen
Elektronen in einem überlappenden Orbital zusammen, und **jedes** zählt die geteilten Elektronen zu seiner
Schale. So erreichen beide die Oktettregel. Entscheidend: Die Bindungselektronen sind **lokalisiert** — sie
sitzen fest zwischen den Partnern. Genau deshalb sind kovalente Kristalle typischerweise **Halbleiter oder
Isolatoren**: Es gibt keine frei beweglichen Ladungen wie im Metall.

### sp³-Hybridisierung und die Diamantstruktur

Das für die Elektronik wichtigste Beispiel ist Silizium (und sein Vorbild Kohlenstoff als Diamant). Kohlenstoff
hat die Konfiguration $1s^2\,2s^2\,2p^2$ — eigentlich nur zwei halbbesetzte $p$-Orbitale, also „wollte" er nur
zwei Bindungen machen. Beobachtet werden aber **vier** gleichwertige Bindungen. Der Grund ist die
__$sp^3$-Hybridisierung__:

1. **Promotion:** Ein $2s$-Elektron wird in das freie $2p$-Orbital angehoben — jetzt sind vier Orbitale je
   einfach besetzt.
2. **Mischung:** Die Orbitale $2s, 2p_x, 2p_y, 2p_z$ mischen zu **vier gleichwertigen** $sp^3$-Hybridorbitalen
   (Hybridisierung = quantenmechanisches „Vermischen" von Atomorbitalen zu neuen Bindungsorbitalen).

Wie richten sich diese vier Elektronenwolken aus? Sie stoßen sich gegenseitig ab (Coulomb) und gehen daher auf
**maximalen Abstand** — das ergibt ein **Tetraeder**. Der Winkel zwischen zwei Bindungen ist dann exakt

$$\theta = \arccos\!\left(-\tfrac13\right) \approx 109{,}47^\circ.$$

:::grafik
Ein zentrales Atom mit vier $sp^3$-Keulen, die in die Ecken eines Tetraeders zeigen; der Bindungswinkel
$109{,}47^\circ$ ist zwischen zwei Keulen eingezeichnet. Daneben der Hinweis „maximaler Abstand durch
Coulomb-Abstoßung → Tetraeder".
:::

Setzt man diese Tetraeder lückenlos periodisch fort, entsteht die __Diamantstruktur__: **zwei ineinander
geschobene FCC-Gitter**, versetzt um ein Viertel der Raumdiagonale:

$$\vec d = \tfrac{a}{4}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}.$$

Genau diese Struktur haben **Silizium** (Kantenlänge $a = 0{,}543\,$nm) und **Germanium** ($a = 0{,}566\,$nm) —
weshalb die tetraedrische $sp^3$-Bindung *das* Grundmotiv der Halbleiterelektronik ist. (Im Sinne des Artikels
[Gitter, Basis und Einheitszelle](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/kristallstruktur/gitter-basis-einheitszelle.html):
Die Diamantstruktur ist ein **FCC-Bravaisgitter mit zweiatomiger Basis** an $(0,0,0)$ und $\vec d$.)

:::grafik
Die Diamantstruktur: ein FCC-Würfel, in dem vier der Tetraederlücken mit einem zweiten Atom besetzt sind;
eingezeichnet der Versatz $\vec d = \tfrac{a}{4}(1,1,1)$ zwischen den beiden FCC-Teilgittern und die tetraedrische
Bindung eines Atoms an seine vier Nachbarn.
:::

**sp²-Hybridisierung → Graphen.** Mischt man nur $2s$ mit **zwei** $p$-Orbitalen, entstehen drei
$sp^2$-Hybridorbitale in einer Ebene (Winkel $120^\circ$); das übrige $p$-Orbital steht senkrecht. Die Abstoßung
führt hier zur **Waben-Struktur** — das ist Graphen.

## Metallische Bindung: der See aus Elektronen

Bei Metallen ist das äußerste Elektron nur **schwach** gebunden. Der konkrete quantenmechanische Grund ist die
__Abschirmung__: Die inneren, gefüllten Orbitale schirmen das Kern-Potential ab, sodass das äußere Elektron statt
des tiefen ein **flacheres, abgeschirmtes** Potential „sieht". Ein flacheres, räumlich engeres Potential
entspricht einem Teilchen in einer **kürzeren Box** — und dort steigt die Grundzustandsenergie, denn (aus dem
Artikel [Teilchen in der Box (1D)](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/quantenmechanik/teilchen-in-der-box-1d.html))

$$E_n = \frac{\hbar^2 \pi^2 n^2}{2 m L^2} \propto \frac{1}{L^2}.$$

Höhere Energie heißt: Das Atom lässt sich **leichter ionisieren**. Das äußere Elektron löst sich und wird Teil
eines gemeinsamen __Elektronengases__ — delokalisierter, frei beweglicher Elektronen. Zurück bleiben **positive
Atomrümpfe**, die vom negativen Elektronengas zusammengehalten werden. Die freie Beweglichkeit dieses Gases ist
zugleich die Erklärung für die hohe elektrische Leitfähigkeit der Metalle.

:::grafik
Links das tiefe, ungeschirmte Kern-Potential (Elektron sitzt tief), rechts das flachere, abgeschirmte Potential
(Elektron sitzt höher, „kürzere Box"). Ein Pfeil „leichter ionisierbar" führt zum Bild des Elektronengases:
positive Rümpfe im Gitter, umspült von beweglichen Elektronen.
:::

## Van-der-Waals-Bindung: kurz aufblitzende Dipole

Die __van-der-Waals-Wechselwirkung__ ist streng genommen keine Bindung: Es gibt **keinen** Elektronentransfer und
kein geteiltes Paar. Stattdessen entstehen durch zufällige Ladungsfluktuationen **temporäre Dipole**, deren
elektrostatische Anziehung die Bausteine zusammenhält. Diese Anziehung ist **sehr schwach** und extrem
**kurzreichweitig**:

$$V_{\text{vdW}} \sim \frac{1}{r^6}.$$

Der steile Abfall mit $1/r^6$ bedeutet: Schon bei geringfügig größerem Abstand ist praktisch keine Anziehung mehr
da. Beispiele: Die einzelnen Graphen-Ebenen im **Graphit** werden nur durch van-der-Waals-Kräfte zusammengehalten
— deshalb lässt sich ein Bleistift „abblättern". Ebenso die Schichten von $\text{MoS}_2$, dessen leichte
Verschiebbarkeit es zum Trockenschmierstoff macht.

:::grafik
Zwei neutrale Atome, bei denen momentane Ladungsverschiebungen zueinander passende „+/−"-Dipole bilden (schwacher
Anziehungspfeil). Daneben die Kurve $V \sim 1/r^6$, die steil gegen null fällt, und ein Graphit-Stapel aus
Ebenen, zwischen denen „vdW" steht.
:::

## Dichteste Kugelpackungen: hcp und fcc

Denkt man Atome als harte Kugeln, gibt es zwei Wege, sie **maximal dicht** zu stapeln (beide mit
Koordinationszahl 12). Sie unterscheiden sich nur in der **Stapelreihenfolge** der dichtgepackten Ebenen:

- **hexagonal dichteste Packung (hcp):** Folge **ABAB…** — die dritte Lage liegt genau über der ersten.
- **kubisch dichteste Packung (= FCC):** Folge **ABCABC…** — erst die vierte Lage liegt wieder über der ersten.

Beide füllen denselben Volumenanteil ($\approx 0{,}74$); der Unterschied liegt allein darin, *wo* die jeweils
nächste Lage einrastet.

:::grafik
Zwei Stapel dichtgepackter Kugelebenen nebeneinander: links hcp mit Markierung ABAB (dritte Lage über der
ersten), rechts fcc mit ABCABC (versetzte dritte Lage). Gleiche Packungsdichte, verschiedene Stapelung.
:::

:::kern
Das Gitter beschreibt, die __Bindung__ erklärt die Anordnung; gemeinsames Ziel ist die __Edelgaskonfiguration__
(Oktettregel). Jede Bindung ist ein Wechselspiel aus Anziehung ($F_\text{an}$) und Pauli-Abstoßung
($F_\text{ab}$); die Potentialkurve $W(r)$ (mit $F=-\mathrm{d}W/\mathrm{d}r$) hat ihr Minimum beim
__Bindungsabstand__ $r_0$ ($F_\text{an}=-F_\text{ab}$), die Tiefe ist die __Bindungsenergie__ $W_0$. Die
**Unsymmetrie** der Kurve + thermische Schwingung ($\sim k_\text{B}T$) erklärt die __Wärmeausdehnung__. **Ionisch:** Elektronen**transfer** → Coulomb-Anziehung von Ionen (LiF → Steinsalz, 2×FCC).
**Kovalent:** geteilte, **lokalisierte** Elektronen (Halbleiter/Isolator); __$sp^3$-Hybridisierung__ → Tetraeder
($\arccos(-\tfrac13)\approx109{,}47^\circ$) → __Diamantstruktur__ = 2 FCC versetzt um $\vec d=\tfrac{a}{4}(1,1,1)$
(Si $a=0{,}543\,$nm, Ge $0{,}566\,$nm); $sp^2$ → Graphen-Wabe. **Metallisch:** Abschirmung → leichtere Ionisation
→ delokalisiertes __Elektronengas__ + positive Rümpfe → leitfähig. **Van der Waals:** kein Transfer, temporäre
Dipole, $V\sim1/r^6$ (Graphit-Ebenen, $\text{MoS}_2$). Dichteste Packungen: **hcp (ABAB)** und **fcc (ABCABC)**,
beide KZ 12, APF $\approx0{,}74$.
:::

Wir wissen jetzt, *warum* Silizium in der Diamantstruktur kristallisiert. Für ein Bauelement braucht man es aber
als **defektfreien Einkristall** höchster Reinheit. Wie man aus billigem Quarzsand einen solchen Kristall zieht,
zeigt der nächste Artikel über das __Kristallwachstum__.

:::quiz
F: Was ist die gemeinsame Triebkraft hinter allen vier Bindungstypen?
A: Jedes Atom strebt die besonders stabile Edelgaskonfiguration an — eine volle äußere Schale (Oktettregel). Die vier Bindungstypen sind nur verschiedene Wege, dieses eine Ziel über die Außenelektronen zu erreichen.
F: Woher kommt die abstoßende Kraft, die jede Bindung bei kleinem Abstand begrenzt?
A: Aus dem Pauli-Prinzip: Überlappen die gefüllten Orbitale zweier Atome, dürfen die Elektronen nicht dieselben Zustände einnehmen, was sehr steil abstößt. Zusammen mit der weitreichenden Anziehung entsteht so eine Potentialkurve mit Minimum.
F: Was bedeuten Bindungsabstand $r_0$ und Bindungsenergie $W_0$ in der Potentialkurve?
A: $r_0$ ist die Lage des Minimums, wo sich Anziehung und Abstoßung aufheben ($F=-dW/dr=0$) — dort sitzen die Atome. $W_0$ ist die Tiefe des Minimums, also die Energie, die man aufbringen muss, um die Atome wieder zu trennen.
F: Warum dehnen sich Materialien beim Erwärmen aus?
A: Die Atome schwingen um $r_0$ mit einer thermischen Energie $\sim k_\text BT$, und die Potentialkurve ist unsymmetrisch (abstoßende Flanke steiler als anziehende). Dadurch verschiebt sich der zeitliche Mittelwert des Abstands mit steigender Temperatur zu größeren Werten.
F: Wie unterscheiden sich ionische und kovalente Bindung im Umgang mit Elektronen?
A: Bei der ionischen Bindung werden Elektronen vollständig übertragen, es entstehen entgegengesetzt geladene Ionen, die sich über Coulomb anziehen. Bei der kovalenten Bindung werden Elektronen geteilt — ein lokalisiertes Bindungspaar sitzt fest zwischen den Partnern, die es beide zu ihrer Schale zählen.
F: Warum sind kovalente Kristalle typischerweise Halbleiter oder Isolatoren?
A: Weil die Bindungselektronen lokalisiert sind — sie sitzen fest zwischen den Atomen und sind nicht frei beweglich. Es gibt kein Elektronengas wie im Metall, daher fehlen bei tiefer Temperatur freie Ladungsträger für den Stromtransport.
F: Wie entsteht aus der $sp^3$-Hybridisierung der Tetraederwinkel von 109,47°?
A: Die vier gleichwertigen $sp^3$-Hybridorbitale stoßen sich gegenseitig ab und gehen auf maximalen Abstand — das ergibt eine tetraedrische Anordnung. Der Winkel zwischen zwei Bindungen ist dann exakt $\arccos(-\tfrac13)\approx109{,}47^\circ$.
F: Wie hängt die $sp^3$-Bindung mit der Diamantstruktur von Silizium zusammen?
A: Setzt man die Tetraeder lückenlos periodisch fort, entstehen zwei um $\vec d=\tfrac a4(1,1,1)$ versetzte FCC-Gitter — die Diamantstruktur. Silizium und Germanium kristallisieren genau so (ein FCC-Bravaisgitter mit zweiatomiger Basis).
F: Warum lässt sich das äußere Elektron eines Metallatoms so leicht ablösen?
A: Die inneren gefüllten Orbitale schirmen das Kernpotential ab, sodass das Außenelektron ein flacheres, engeres Potential „sieht" — wie ein Teilchen in kürzerer Box, wo $E\propto1/L^2$ steigt. Die höhere Energie bedeutet leichtere Ionisierung; die abgelösten Elektronen bilden das delokalisierte Elektronengas.
F: Warum ist die van-der-Waals-Wechselwirkung so schwach und kurzreichweitig, und was folgt daraus praktisch?
A: Sie beruht nur auf zufälligen, temporären Dipolen ohne Elektronentransfer, und ihr Potential fällt steil wie $1/r^6$ ab. Daher hält sie z. B. die Graphen-Ebenen im Graphit nur lose zusammen — weshalb sich ein Bleistift abblättern lässt und $\text{MoS}_2$ als Trockenschmierstoff taugt.
:::
