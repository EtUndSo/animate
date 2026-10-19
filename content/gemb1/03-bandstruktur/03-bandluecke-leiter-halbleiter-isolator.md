---
title: Bandlücke, Leiter, Halbleiter und Isolator
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bandstruktur
order: 4030300
summary: Die Antwort auf die Kernfrage der Festkörperelektronik – warum ein Material Metall, Halbleiter oder Isolator ist. Entscheidend ist die Besetzung der Bänder: Ein vollständig gefülltes Band trägt keinen Strom, ein teilgefülltes schon. Liegt die Fermi-Energie in einer Bandlücke, hängt alles an deren Größe $E_g$ – winzig (Si, $1{,}12$ eV) macht einen Halbleiter, riesig (Diamant, $5{,}47$ eV) einen Isolator.
tags: Bandlücke, Valenzband, Leitungsband, Fermi-Energie, Metall, Halbleiter, Isolator, Besetzung
---

:::grafik
Einstiegs-Animation: Drei Bänderdiagramme nebeneinander, jeweils Energie senkrecht. (1) __Metall__: ein Band ist
nur halb gefüllt (oder zwei Bänder überlappen), die Füll-Linie liegt **mitten im Band**. (2) __Halbleiter__: ein
volles unteres Band, ein leeres oberes, dazwischen eine **schmale** Lücke; einige Elektronen springen bei
Zimmertemperatur thermisch hinüber. (3) __Isolator__: dieselbe Anordnung, aber mit **breiter** Lücke — fast
niemand kommt hinüber. Ein „Wasserpegel" (Fermi-Energie) füllt die Zustände von unten auf. Kernbotschaft: Nicht
die Bänder allein, sondern ihre **Besetzung** und die **Lückengröße** entscheiden über die Leitfähigkeit.
:::

:::konzept
Jetzt kommt die Frage, auf die das ganze Oberthema hinausläuft: **Warum leitet Kupfer den Strom, Silizium ein
bisschen, und Diamant gar nicht?** Alle drei haben Energiebänder — der Unterschied liegt darin, **wie die Bänder
mit Elektronen gefüllt sind** und **wie groß die Lücke** zwischen ihnen ist. Dieser Artikel verbindet die
abstrakte Bandstruktur mit der greifbaren Eigenschaft „Leiter / Halbleiter / Isolator". Die zentrale, fast
paradoxe Einsicht dabei: Ein randvoll gefülltes Band kann **keinen** Strom tragen — obwohl es voller Elektronen
steckt.
:::

**Worum es geht:** Wir klären, wie Elektronen die Bänder füllen (bis zur __Fermi-Energie__), warum ein **volles**
Band stromlos bleibt, und wie daraus die Dreiteilung __Metall__ / __Halbleiter__ / __Isolator__ folgt — mit der
__Bandlücke__ $E_g$ als entscheidender Größe.

## Wie die Bänder gefüllt werden: die Fermi-Energie

Elektronen sind Fermionen und gehorchen dem **Pauli-Prinzip**: Jeder Zustand nimmt höchstens zwei Elektronen auf
(Spin $\uparrow\downarrow$). Man füllt die verfügbaren Zustände deshalb **von unten nach oben** auf, wie Wasser
ein Gefäß füllt. Die höchste bei $T=0$ besetzte Energie heißt __Fermi-Energie__ $E_f$ — die „Wasserlinie" der
Elektronenfüllung.

Die alles entscheidende Frage ist dann: **Wo liegt diese Wasserlinie?**

- **Mitten in einem Band** → es gibt direkt oberhalb freie Zustände.
- **Genau in einer Lücke** → das darunterliegende Band ist voll, das darüber leer.

:::grafik
Ein Band als „Gefäß", in das Elektronen von unten eingefüllt werden; die Füllhöhe ist die Fermi-Energie $E_f$
(waagerechte „Wasserlinie"). Zwei Fälle angedeutet: Wasserlinie mitten im Band vs. Wasserlinie an einer
Bandkante (Lücke darüber).
:::

## Warum ein volles Band keinen Strom trägt

Das ist der Schlüssel — und zunächst überraschend. Ein Strom bedeutet, dass sich die Elektronen im Mittel in
**eine** Richtung bewegen, also mehr Elektronen mit Impuls $+k$ als mit $-k$ vorhanden sind. In einem **vollen**
Band ist aber **jeder** Zustand besetzt: zu jedem Elektron mit $+k$ gibt es eines mit $-k$. Ihre Beiträge zur
Geschwindigkeit heben sich **exakt auf** — der Netto-Strom ist null.

Legt man ein elektrisches Feld an, möchte es die Elektronen beschleunigen, also ihren $k$-Wert verschieben. Dafür
müssten sie in **freie** Zustände wechseln. In einem vollen Band gibt es aber keine freien Zustände (das nächste
freie liegt erst jenseits der Lücke). Das Feld „greift ins Leere" — es kann nichts bewegen.

$$\text{volles Band} \;\Rightarrow\; \text{kein freier Zustand in Reichweite} \;\Rightarrow\; j = 0.$$

:::grafik
Ein voll besetztes Kosinus-Band: zu jedem besetzten Zustand bei $+k$ ist der Partner bei $-k$ markiert, mit
entgegengesetzten Geschwindigkeitspfeilen, die sich aufheben. Ein angelegtes Feld (Pfeil) findet keinen freien
Zustand → „kein Strom".
:::

## Metall: das teilgefüllte Band

Ganz anders, wenn die Fermi-Energie **mitten in einem Band** liegt (teilgefülltes Band, oder zwei überlappende
Bänder). Dann sitzen direkt oberhalb der besetzten Zustände **leere** Zustände. Schon ein kleines Feld kann die
Elektronen an der Wasserlinie dorthin verschieben — es entsteht ein Überschuss in eine Richtung, also **Strom**.
Das ist ein __Metall__: Es leitet immer, auch bei $T=0$ ([OpenStax](https://openstax.org/books/university-physics-volume-3/pages/9-5-band-theory-of-solids)).

:::grafik
Ein halb gefülltes Band mit der Fermi-Linie in der Mitte; direkt darüber leere Zustände. Ein Feldpfeil verschiebt
die Besetzung leicht nach $+k$ → Überschuss an $+k$-Elektronen → Netto-Strom. Beschriftung „teilgefüllt = Metall".
:::

## Halbleiter und Isolator: alles hängt an der Lücke

Liegt die Fermi-Energie dagegen in einer __Bandlücke__, dann ist das untere Band — das __Valenzband__ — bei $T=0$
**voll** und trägt keinen Strom, und das obere — das __Leitungsband__ — ist **leer**. Bei $T=0$ ist so ein
Material ein perfekter Nichtleiter. Was es bei Zimmertemperatur unterscheidet, ist allein die **Größe** der Lücke
$E_g$ (der Abstand zwischen Valenzband-Oberkante und Leitungsband-Unterkante):

- **Kleine Lücke (Halbleiter):** Die thermische Energie bei Raumtemperatur ($\sim 0{,}025$ eV) reicht aus, um
  **einige** Elektronen über eine schmale Lücke ins Leitungsband zu heben. Dort sind sie beweglich → das Material
  leitet **schwach** und nimmt mit steigender Temperatur zu. Beispiel: Silizium, $E_g = 1{,}12$ eV.
- **Große Lücke (Isolator):** Bei breiter Lücke schafft es praktisch **kein** Elektron hinüber → kein Strom.
  Beispiel: Diamant, $E_g \approx 5{,}47$ eV.

Der Übergang ist **fließend** — es gibt keine scharfe Grenze zwischen Halbleiter und Isolator, nur eine immer
kleiner werdende Zahl thermisch angeregter Ladungsträger ([Penn State](https://courses.ems.psu.edu/matse81/book/export/html/2228)).

:::grafik
Halbleiter vs. Isolator nebeneinander: beide mit vollem Valenzband und leerem Leitungsband, aber links eine
schmale Lücke $E_g$ (ein paar Elektronen mit Pfeil „thermisch angeregt" im Leitungsband, Löcher zurück im
Valenzband) und rechts eine breite Lücke (keine Anregung). $E_g$ jeweils als Doppelpfeil bemaßt.
:::

**Warum leitet ein Halbleiter nicht wie ein Metall, obwohl er voller Elektronen ist?** Weil diese Elektronen im
**vollen** Valenzband sitzen und erst die Lücke überspringen müssen, bevor sie beweglich werden. Genau dieser
„Sprung über die Lücke" ist das Prinzip, das Dioden, Transistoren und Solarzellen steuerbar macht.

## Warum die Lücke bei C → Si → Ge → Sn schrumpft

Die Elementhalbleiter der IV. Hauptgruppe (Kohlenstoff, Silizium, Germanium, Zinn) haben **alle** dieselbe
Valenzkonfiguration (vier Außenelektronen, $sp^3$) und dieselbe Diamantstruktur — ihr Valenzband ist jeweils
voll. Trotzdem sinkt die Bandlücke dramatisch, wenn man in der Gruppe nach unten geht:

| Element | $E_g$ (Raumtemp.) | Typ |
|---|---|---|
| C (Diamant) | $5{,}47$ eV | Isolator (Weitband) |
| Si | $1{,}12$ eV | Halbleiter |
| Ge | $0{,}67$ eV | Halbleiter |
| $\alpha$-Sn | $\approx 0$ eV | Halbmetall |

**Der Mechanismus:** Je weiter oben in der Gruppe, desto **kleiner** die Atome und desto **kürzer/fester** die
Bindung — das bindet die Elektronen stärker und hält die Lücke groß. Nach unten werden die Atome größer, die
Bindung schwächer, die Bänder breiter (stärkerer Überlapp aus dem vorigen Artikel), und die Lücke schrumpft, bis
sie bei grauem Zinn praktisch verschwindet.

:::grafik
Vier Bänderdiagramme nebeneinander (C, Si, Ge, α-Sn) mit von links nach rechts schrumpfender Lücke $E_g$ (5,47 →
1,12 → 0,67 → ~0 eV). Darunter ein Pfeil „größere Atome, schwächere Bindung, breitere Bänder → kleinere Lücke".
:::

:::kern
Ob ein Material __Metall__, __Halbleiter__ oder __Isolator__ ist, entscheidet die **Besetzung** der Bänder plus
die **Lückengröße**. Elektronen füllen die Zustände bis zur __Fermi-Energie__ $E_f$. **Volles Band → kein Strom**
(zu jedem $+k$ ein $-k$, und kein freier Zustand zum Beschleunigen). **Teilgefülltes Band → Metall** (freie
Zustände an $E_f$). Liegt $E_f$ in der Lücke, ist das __Valenzband__ voll, das __Leitungsband__ leer; dann
entscheidet $E_g$: **klein → Halbleiter** (thermische Anregung, z. B. Si $1{,}12$ eV), **groß → Isolator** (z. B.
Diamant $5{,}47$ eV), Übergang fließend. In der IV. Hauptgruppe schrumpft $E_g$ von C ($5{,}47$) über Si/Ge bis
$\alpha$-Sn ($\approx 0$), weil die Atome größer, die Bindung schwächer und die Bänder breiter werden.
:::

Wir wissen jetzt, **ob** ein Material leitet. Offen ist, **wie gut** — wie schnell und „schwer" die wenigen
Ladungsträger im Leitungsband sind, die es über die Lücke geschafft haben. Das steckt in der Krümmung der Bänder
und führt zum Begriff der __effektiven Masse__ (und zum Gegenstück des Elektrons, dem __Loch__) — dem Thema des
nächsten Artikels.

:::quiz
F: Was ist die Fermi-Energie, und warum füllt man die Bänder „von unten" auf?
A: Elektronen sind Fermionen und gehorchen dem Pauli-Prinzip — jeder Zustand nimmt höchstens zwei auf. Man belegt daher die niedrigsten Zustände zuerst, wie Wasser ein Gefäß; die höchste bei $T=0$ besetzte Energie ist die Fermi-Energie $E_f$ (die „Wasserlinie").
F: Warum entscheidet die Lage der Fermi-Energie über das Verhalten des Materials?
A: Liegt $E_f$ mitten in einem Band, gibt es direkt darüber freie Zustände (leitfähig). Liegt sie in einer Lücke, ist das untere Band voll und das obere leer — dann hängt alles an der Lückengröße.
F: Warum trägt ein vollständig gefülltes Band keinen Strom, obwohl es voller Elektronen ist?
A: In einem vollen Band ist zu jedem Elektron mit Impuls $+k$ auch der Partner mit $-k$ besetzt; ihre Geschwindigkeiten heben sich exakt auf. Für einen Netto-Strom bräuchte man ein Ungleichgewicht, das nur durch freie Zustände entstehen könnte — die es im vollen Band nicht gibt.
F: Warum kann ein elektrisches Feld in einem vollen Band nichts bewegen?
A: Das Feld will die Elektronen beschleunigen, also ihren $k$-Wert verschieben — dafür bräuchten sie freie Zustände, in die sie wechseln können. Im vollen Band liegt der nächste freie Zustand erst jenseits der Lücke, das Feld „greift ins Leere".
F: Warum leitet ein Metall immer, sogar bei $T=0$?
A: Bei einem Metall liegt $E_f$ mitten in einem Band, direkt oberhalb der besetzten Zustände sind leere. Schon ein kleines Feld verschiebt die Besetzung dorthin und erzeugt einen Überschuss in eine Richtung — Strom, ohne dass thermische Anregung nötig wäre.
F: Was unterscheidet einen Halbleiter von einem Isolator physikalisch?
A: Beide haben bei $T=0$ ein volles Valenzband und ein leeres Leitungsband; der Unterschied ist nur die Größe der Bandlücke $E_g$. Bei kleiner Lücke (Halbleiter) heben thermische Fluktuationen einige Elektronen hinüber, bei großer (Isolator) praktisch keine.
F: Warum nimmt die Leitfähigkeit eines Halbleiters mit der Temperatur zu?
A: Höhere Temperatur bedeutet mehr thermische Energie, sodass mehr Elektronen über die Lücke ins Leitungsband gelangen und dort beweglich werden. Mehr Ladungsträger heißt höhere Leitfähigkeit — anders als beim Metall, wo sie eher sinkt.
F: Warum ist die Grenze zwischen Halbleiter und Isolator fließend?
A: Die Zahl thermisch angeregter Ladungsträger nimmt mit wachsender Lücke stetig (exponentiell) ab, ohne einen scharfen Sprung. „Halbleiter" und „Isolator" sind daher nur Bereiche auf einer kontinuierlichen Skala der Lückengröße.
F: Warum leitet ein Halbleiter nicht wie ein Metall, obwohl er voller Elektronen ist?
A: Seine Elektronen sitzen im vollen Valenzband und müssen erst die Lücke überspringen, bevor sie in freie Leitungsbandzustände gelangen und beweglich werden. Genau dieser steuerbare „Sprung über die Lücke" macht Dioden, Transistoren und Solarzellen möglich.
F: Warum schrumpft die Bandlücke in der IV. Hauptgruppe von C über Si, Ge bis α-Sn?
A: Nach unten werden die Atome größer und die Bindungen schwächer, sodass die Wellenfunktionen stärker überlappen und die Bänder breiter werden. Breitere Bänder rücken enger zusammen, die Lücke schrumpft von 5,47 eV (Diamant) bis fast 0 (graues Zinn).
:::
