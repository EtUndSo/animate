---
title: Dotierung – n- und p-Halbleiter
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Halbleiter und Ladungstransport
order: 4050100
summary: Wie man die Ladungsträgerdichte eines Halbleiters gezielt um Größenordnungen einstellt, indem man einzelne Wirtsatome durch Fremdatome ersetzt. Ein Donator (Gruppe V) hat ein Elektron zu viel und wird zum n-Leiter, ein Akzeptor (Gruppe III) eines zu wenig und wird zum p-Leiter. Warum diese Störstellen so leicht ionisieren, erklärt das Wasserstoffmodell – mit einer Ionisierungsenergie von nur $\sim\!45$ meV statt 13,6 eV.
tags: Dotierung, Donator, Akzeptor, n-Typ, p-Typ, Störstelle, Wasserstoffmodell, Ionisierungsenergie
---

:::grafik
Einstiegs-Animation: Ein Silizium-Gitter (jedes Atom vier Bindungen). Links wird ein Atom durch einen __Donator__
(Phosphor, fünf Außenelektronen) ersetzt — vier Elektronen binden, das fünfte umkreist locker den Rumpf und löst
sich bei leichter Erwärmung ins Leitungsband. Rechts ein __Akzeptor__ (Bor, drei Außenelektronen) — eine Bindung
bleibt offen, schnappt sich ein Elektron aus dem Valenzband und lässt dort ein __Loch__ zurück. Daneben ein
Bänderschema: ein Donatorniveau $E_d$ knapp unter $E_L$, ein Akzeptorniveau $E_a$ knapp über $E_V$.
Kernbotschaft: Ein einzelnes Fremdatom liefert gezielt einen beweglichen Ladungsträger.
:::

:::konzept
Reines Silizium ist ein schlechter Leiter: Seine intrinsische Ladungsträgerdichte $n_i \approx 10^{10}\,$cm⁻³ ist
winzig gegenüber den $\sim 10^{22}\,$cm⁻³ Atomen. Für ein Bauelement braucht man aber eine **einstellbare**,
**temperaturstabile** Ladungsträgerdichte. Das erreicht die __Dotierung__: Man ersetzt einzelne Wirtsatome durch
Fremdatome, die gezielt Elektronen oder Löcher beisteuern — und stellt so die Leitfähigkeit über viele
Größenordnungen ein. Das ist der Schritt, der aus dem reinen Kristall erst das Material für Dioden und
Transistoren macht. Verblüffend dabei: Schon winzige thermische Energie genügt, um diese Fremdatome zu
aktivieren — warum, erklärt ein überraschend einfaches Modell.
:::

**Worum es geht:** Wir führen __Donatoren__ (n-Typ) und __Akzeptoren__ (p-Typ) ein, verstehen über das
__Wasserstoffmodell__, *warum* ihre __Störstellen__ so flach (leicht ionisierbar) sind, und grenzen flache von
tiefen Störstellen ab.

## Donator: ein Elektron zu viel (n-Typ)

Ein __Donator__ (von lat. *donare*, geben) ist ein Fremdatom mit **einem Außenelektron mehr** als der Wirt — in
Silizium (Gruppe IV) also ein Element der **Gruppe V**: Phosphor, Arsen, Antimon. Von seinen fünf
Valenzelektronen gehen vier die normalen kovalenten Bindungen mit den Nachbarn ein. Das **fünfte** ist überzählig
und nur sehr schwach an das Atom gebunden.

Schon eine kleine thermische Energie löst dieses fünfte Elektron ab; es wandert ins Leitungsband und ist dort
beweglich. Der Donator „gibt" also ein Elektron ab und bleibt als **positiv geladener** Rumpf zurück. Weil die
zusätzlichen Ladungsträger **Elektronen** (negativ) sind, heißt der Kristall __n-Typ__.

:::grafik
Ausschnitt des Si-Gitters mit einem Phosphor-Atom: vier Bindungen abgesättigt, das fünfte Elektron als lose Wolke
um den P⁺-Rumpf. Ein Pfeil hebt es ins Leitungsband. Beschriftung „Donator → freies Elektron + ortsfester
positiver Rumpf".
:::

## Akzeptor: ein Elektron zu wenig (p-Typ)

Ein __Akzeptor__ (von lat. *accipere*, annehmen) ist das Gegenstück: ein Fremdatom mit **einem Außenelektron
weniger**, also aus der **Gruppe III** (Bor, Aluminium, Gallium). Ihm fehlt ein Elektron, um alle vier Bindungen
zu schließen. Diese offene Bindung „schnappt" sich ein Elektron aus dem Valenzband. Der Akzeptor wird dadurch
**negativ geladen** und hinterlässt im Valenzband ein **Loch** — den beweglichen, positiven Ladungsträger. Weil
die Ladungsträger hier **Löcher** (positiv) sind, heißt der Kristall __p-Typ__.

:::grafik
Si-Gitter mit einem Bor-Atom: drei Bindungen abgesättigt, eine offen. Ein Elektron aus einer Nachbarbindung
füllt sie auf (B⁻), und die Lücke (Loch, +) wandert ins Valenzband. Beschriftung „Akzeptor → freies Loch +
ortsfester negativer Rumpf".
:::

Im Bänderschema sitzt der Donator als Niveau $E_d$ **knapp unterhalb** der Leitungsbandkante $E_L$ (das überzählige
Elektron ist fast schon frei), der Akzeptor als Niveau $E_a$ **knapp oberhalb** der Valenzbandkante $E_V$.

:::grafik
Bänderschema mit Leitungsband (oben) und Valenzband (unten); ein Donatorniveau $E_d$ dicht unter $E_L$ (kurzer
Abstand, Pfeil nach oben ins Leitungsband) und ein Akzeptorniveau $E_a$ dicht über $E_V$ (Pfeil, der ein Elektron
aus dem Valenzband aufnimmt, Loch zurücklässt).
:::

## Warum ist das überzählige Elektron so schwach gebunden?

Hier kommt die elegante Idee. Das fünfte Donator-Elektron umkreist den einfach positiven Donatorrumpf — das ist
**genau die Situation des Wasserstoffatoms**, nur eben eingebettet in den Siliziumkristall. Man übernimmt daher
die Wasserstoff-Ionisierungsenergie (die Rydberg-Energie $13{,}6\,$eV) und passt sie an zwei Kristall-Effekte an:

$$E_{\text{ion}} = 13{,}6\,\text{eV} \cdot \frac{m^\star/m_0}{\varepsilon_r^2}.$$

- __$m^\star$__: Statt der freien Elektronenmasse zählt die **effektive Masse** im Kristall (für Silizium
  $m^\star \approx 0{,}19\,m_0$) — das Elektron ist „leichter".
- __$\varepsilon_r$__: Die **relative Permittivität** des Kristalls ($\varepsilon_r = 11{,}7$ für Silizium)
  schwächt das anziehende Coulomb-Feld des Rumpfs stark ab, weil der polarisierbare Kristall dazwischenliegt. Und
  $\varepsilon_r$ geht sogar **quadratisch** ein.

Beide Effekte senken die Bindung drastisch — von $13{,}6\,$eV auf nur noch

$$E_{\text{ion}} \sim 20\text{–}50\,\text{meV}.$$

:::grafik
Links das Wasserstoffatom (Elektron umkreist Proton, $13{,}6\,$eV). Rechts dasselbe im Si-Kristall: ein viel
größerer Orbit (effektiver Bohr-Radius $\sim 1{,}8\,$nm, über viele Gitteratome), mit den Ersetzungen
$m_0\to m^\star$ und $\varepsilon_0\to\varepsilon_r\varepsilon_0$, Ergebnis $\sim 45\,$meV.
:::

Der entscheidende Vergleich: Die thermische Energie bei Raumtemperatur ist $k_B T \approx 25\,$meV — also **in
derselben Größenordnung** wie $E_{\text{ion}}$. Deshalb sind diese __flachen Störstellen__ (Niveau nur knapp neben
der Bandkante) bei Raumtemperatur **nahezu vollständig ionisiert**: Praktisch jedes Donatoratom hat sein Elektron
schon abgegeben. Gemessene Ionisierungsenergien in Silizium (von der nächsten Bandkante): Phosphor $\approx 45\,$meV,
Arsen $54\,$meV, Antimon $39\,$meV (Donatoren); Bor $45\,$meV, Aluminium $67\,$meV (Akzeptoren)
([NCBI/PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5519722/), [arXiv](https://arxiv.org/pdf/cond-mat/0309139)).

:::grafik
Ein Energiebalken: links $13{,}6\,$eV (H-Atom), rechts stark zusammengeschrumpft $\sim 45\,$meV (Donator in Si),
und direkt daneben die Marke $k_B T = 25\,$meV (300 K). Hervorgehoben: beide fast gleich → „bei Raumtemperatur
ionisiert".
:::

## Flache und tiefe Störstellen

Nicht jedes Fremdatom ist so brav. Man unterscheidet:

- __Flache Störstellen__ ($E_{\text{ion}} \sim$ einige $10\,$meV, Niveau nahe einer Bandkante): die
  „Nutz-Dotierung" (P, As, Sb, B, Al) — bei Raumtemperatur ionisiert, liefert kontrollierte Ladungsträger.
- __Tiefe Störstellen__ (Niveau nahe der **Bandmitte**, z. B. Gold, Eisen, Chrom): ionisieren kaum, liefern also
  kaum Ladungsträger. Schlimmer noch — sie wirken als **Rekombinationszentren**: Sie fangen Elektronen und Löcher
  ein und vernichten sie, was in den meisten Bauelementen unerwünscht ist (gezielt nutzt man sie nur, um die
  Schaltgeschwindigkeit zu erhöhen).

Wie viel Fremdatome man überhaupt einbauen kann, begrenzt die temperaturabhängige **Löslichkeit** des Dotierstoffs
im Wirtskristall.

:::grafik
Bänderschema mit zwei Störstellentypen: ein flaches Niveau dicht unter $E_L$ (Pfeil leicht ins Band, „liefert
Ladungsträger") und ein tiefes Niveau in Bandmitte, das ein Elektron und ein Loch einfängt und zusammenführt
(„Rekombinationszentrum").
:::

**Warum nicht einfach reines Silizium erhitzen, um Ladungsträger zu bekommen?** Weil die intrinsische Dichte
$n_i$ (1) winzig und (2) extrem temperaturempfindlich ist ($\propto e^{-E_g/2k_BT}$) — ein Bauelement bräuchte
dann exakte Temperaturkontrolle und bliebe schlecht leitend. Dotierung liefert dagegen eine **feste, einstellbare**
Dichte, die über einen weiten Temperaturbereich konstant ist (nächster Artikel).

:::kern
__Dotierung__ stellt die Ladungsträgerdichte gezielt ein, indem Wirtsatome durch Fremdatome ersetzt werden. Ein
__Donator__ (Gruppe V: P, As, Sb) hat ein Elektron zu viel → gibt es ins Leitungsband ab, bleibt positiv, macht
den __n-Typ__; Niveau $E_d$ knapp unter $E_L$. Ein __Akzeptor__ (Gruppe III: B, Al, Ga) hat eines zu wenig →
nimmt ein Valenzband-Elektron auf, bleibt negativ, hinterlässt ein Loch, macht den __p-Typ__; Niveau $E_a$ knapp
über $E_V$. Das __Wasserstoffmodell__ erklärt die kleine Ionisierungsenergie $E_{\text{ion}}=13{,}6\,\text{eV}\cdot
(m^\star/m_0)/\varepsilon_r^2 \sim 20\text{–}50\,$meV (Si: $m^\star\approx0{,}19\,m_0$, $\varepsilon_r=11{,}7$) —
vergleichbar mit $k_BT\approx25\,$meV, daher bei Raumtemperatur **ionisiert**. __Flache__ Störstellen (nahe
Bandkante) sind die Nutzdotierung; __tiefe__ (Bandmitte, z. B. Au) wirken als Rekombinationszentren.
:::

Wir können jetzt Elektronen oder Löcher gezielt einbauen. Als Nächstes schauen wir, wie sich die
Ladungsträgerdichte und das __Fermi-Niveau__ eines dotierten Halbleiters mit der **Temperatur** verhalten — mit
den drei charakteristischen Bereichen Freeze-out, Sättigung und Eigenleitung.

:::quiz
F: Warum reicht die intrinsische Leitung nicht, warum braucht ein Bauelement Dotierung?
A: $n_i\approx10^{10}\,$cm⁻³ ist winzig und zudem extrem temperaturempfindlich ($\propto e^{-E_g/2k_BT}$). Ein Bauelement braucht aber eine fest einstellbare, über einen weiten Temperaturbereich stabile Ladungsträgerdichte — genau das liefert die Dotierung.
F: Warum macht ein Gruppe-V-Atom einen n-Leiter?
A: Es bringt fünf Valenzelektronen mit, vier davon sättigen die kovalenten Bindungen zum Silizium ab. Das fünfte ist überzählig und schwach gebunden, löst sich leicht ins Leitungsband und wird zum zusätzlichen (negativen) Ladungsträger.
F: Warum bleibt der ionisierte Donator ortsfest positiv, trägt also nicht zum Strom bei?
A: Er gibt sein überzähliges Elektron ab, der Atomrumpf ist aber fest ins Gitter eingebaut und kann nicht wandern. Beweglich ist nur das abgegebene Elektron; der positive Rumpf bleibt als ortsfeste Raumladung zurück.
F: Wieso erzeugt ein Akzeptor einen positiven beweglichen Ladungsträger, obwohl er selbst negativ wird?
A: Die offene vierte Bindung fängt ein Elektron aus dem Valenzband ein — der Akzeptor wird dadurch negativ. Das herausgerissene Elektron hinterlässt im Valenzband ein Loch, und dieses Loch ist der bewegliche, positive Ladungsträger.
F: Warum liegt das Donatorniveau $E_d$ knapp *unter* $E_L$ und das Akzeptorniveau $E_a$ knapp *über* $E_V$?
A: Das überzählige Donatorelektron ist nur schwach gebunden, es fehlt ihm also fast nichts mehr zum Leitungsband — daher $E_d$ dicht unter $E_L$. Der Akzeptor braucht umgekehrt nur wenig Energie, um ein Valenzbandelektron aufzunehmen, deshalb liegt $E_a$ dicht über $E_V$.
F: Warum darf man das Donatorelektron wie ein Wasserstoffatom behandeln?
A: Ein einzelnes Elektron umkreist einen einfach positiven Rumpf — genau die Geometrie des Wasserstoffatoms. Nur ist es in den Kristall eingebettet, sodass man die Rydberg-Energie mit effektiver Masse und Permittivität an die Kristallumgebung anpasst.
F: Warum ist die Ionisierungsenergie im Kristall nur ~45 meV statt 13,6 eV?
A: Die effektive Masse $m^\star\approx0{,}19\,m_0$ macht das Elektron „leichter", und die Permittivität $\varepsilon_r=11{,}7$ schirmt das anziehende Coulomb-Feld des Rumpfs ab — letztere sogar quadratisch. Beide Faktoren im Zähler/Nenner drücken $E_\text{ion}$ um rund drei Größenordnungen herunter.
F: Warum sind flache Störstellen bei Raumtemperatur praktisch vollständig ionisiert?
A: Ihre Ionisierungsenergie (~einige 10 meV) liegt in derselben Größenordnung wie die thermische Energie $k_BT\approx25\,$meV. Die thermische Bewegung reicht damit aus, nahezu jedem Donator/Akzeptor seinen Ladungsträger zu entreißen.
F: Was unterscheidet tiefe von flachen Störstellen, und warum sind tiefe meist unerwünscht?
A: Tiefe Störstellen sitzen nahe der Bandmitte, zu weit von jeder Bandkante, um mit $k_BT$ ionisiert zu werden — sie liefern kaum Ladungsträger. Schlimmer: sie fangen Elektronen und Löcher ein und vernichten sie als Rekombinationszentren.
F: Warum nutzt man gezielt doch manchmal tiefe Störstellen (z. B. Gold)?
A: Ihre Wirkung als Rekombinationszentrum vernichtet überschüssige Ladungsträger schnell. Das verkürzt die Ladungsträgerlebensdauer und erhöht damit die Schaltgeschwindigkeit eines Bauelements — in Fällen, wo es auf Tempo statt auf lange Lebensdauer ankommt.
:::
