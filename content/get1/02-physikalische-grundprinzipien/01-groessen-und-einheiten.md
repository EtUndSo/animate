---
title: Physikalische Größen und Einheiten
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Physikalische Grundprinzipien
order: 20100
summary: Warum jede physikalische Aussage aus Zahlenwert und Einheit besteht, woher die sieben Basisgrößen kommen und wie man mit Einheiten rechnet — das Werkzeug, auf dem die ganze Elektrotechnik aufbaut.
tags: physikalische Größe, Einheit, SI, Basisgrößen, Ampere, Einheitenvorsatz, Größengleichung, Dimensionskontrolle
---

:::konzept
„Der Widerstand ist 5." — fünf was? Ohne Einheit ist eine physikalische Angabe wertlos. Jede Größe in der
Elektrotechnik besteht aus zwei Teilen: einer **Zahl** und einer **Einheit**, die sagt, worauf sich die Zahl
bezieht. Dieser Abschnitt klärt, wie dieses System aufgebaut ist — es ist das Werkzeug, mit dem alles Weitere
gemessen und gerechnet wird.
:::

**Worum es geht:** Bevor man Ströme, Spannungen und Felder berechnet, braucht man eine saubere Sprache für
Messwerte. Diese Sprache ist das __Internationale Einheitensystem__ (SI, von französisch *Système
international d'unités*). Wir bauen sie von der einzelnen Größe über die sieben Grundpfeiler bis zum Rechnen
mit Einheiten auf.

## Was ist eine physikalische Größe?

Eine __physikalische Größe__ ist alles, was sich messen lässt — eine Länge, eine Zeit, ein Strom. Ihr Wert ist
immer das Produkt aus einem __Zahlenwert__ und einer __Einheit__:

$$G = \{G\} \cdot [G].$$

Die einzelnen Bestandteile:

- __$G$__: die __physikalische Größe__ selbst, zum Beispiel ein Strom $I$ oder eine Länge $l$.
- __$\{G\}$__: der __Zahlenwert__ — die reine Maßzahl, also *wie viele* Einheiten es sind.
- __$[G]$__: die __Einheit__ — das Bezugsmaß, *in welcher Einheit* gemessen wurde.

Ein Beispiel: Bei $I = 5\,\text{A}$ ist der Zahlenwert $\{I\} = 5$ und die Einheit $[I] = \text{A}$ (Ampere).
Beide gehören untrennbar zusammen. Lässt man die Einheit weg, ist die Aussage sinnlos; ändert man die Einheit,
muss sich der Zahlenwert anpassen — dieselbe Länge ist $1\,\text{m}$ **oder** $100\,\text{cm}$, das Produkt aus
Zahl und Einheit bleibt gleich.

**Anders betrachtet.** Man kann die Einheit wie eine Währung sehen: „5 Euro" und „500 Cent" sind derselbe
Betrag, nur in unterschiedlicher Stückelung ausgedrückt. Rechnet man den Zahlenwert um, muss man die Einheit
gegenläufig anpassen, damit der Wert erhalten bleibt.

:::grafik
Die „Anatomie" einer Größe: der Ausdruck $I = 5\,\text{A}$, darunter zwei Klammern, die auf die $5$
(Beschriftung „Zahlenwert") und auf das $\text{A}$ (Beschriftung „Einheit") zeigen.
:::

## Die sieben Basisgrößen

Nicht jede Einheit lässt sich auf eine andere zurückführen. Das SI legt sieben __Basisgrößen__ fest, aus denen
sich alle übrigen zusammensetzen lassen. Sie sind der Werkzeugkasten, aus dem der Rest gebaut wird:

| Basisgröße | Formelzeichen | Basiseinheit | Einheitenzeichen |
|---|---|---|---|
| Länge | $l$ | Meter | $\text{m}$ |
| Masse | $m$ | Kilogramm | $\text{kg}$ |
| Zeit | $t$ | Sekunde | $\text{s}$ |
| elektrische Stromstärke | $I$ | Ampere | $\text{A}$ |
| thermodynamische Temperatur | $T$ | Kelvin | $\text{K}$ |
| Stoffmenge | $n$ | Mol | $\text{mol}$ |
| Lichtstärke | $I_\text{v}$ | Candela | $\text{cd}$ |

Für die Elektrotechnik ist entscheidend, dass die __elektrische Stromstärke__ mit dem __Ampere__ zu diesen
sieben Grundpfeilern gehört — sie wird also **nicht** aus mechanischen Größen abgeleitet, sondern ist selbst
eine Basisgröße.

Seit der grundlegenden Reform des SI am **20. Mai 2019** sind alle sieben Einheiten über feste Zahlenwerte von
__Naturkonstanten__ definiert, statt über Prototypen oder Versuchsanordnungen. Das __Ampere__ hängt seitdem
direkt an der __Elementarladung__

$$e = 1{,}602176634 \cdot 10^{-19}\,\text{C},$$

deren Zahlenwert per Definition **exakt** festgelegt wurde. Ein Ampere bedeutet damit anschaulich: pro Sekunde
tritt eine ganz bestimmte, feste Anzahl von Elementarladungen durch den Querschnitt. Der Vorteil dieser
Definition über eine Naturkonstante ist, dass sie überall im Universum reproduzierbar ist und nicht von einem
aufbewahrten Gegenstand abhängt ([2019 revision of the SI](https://en.wikipedia.org/wiki/2019_revision_of_the_SI)).

## Abgeleitete Größen

Alle anderen Größen heißen __abgeleitete Größen__, weil sie sich durch Multiplikation und Division aus den
Basisgrößen zusammensetzen. Ihre Einheiten ergeben sich nach genau derselben Rechnung aus den Basiseinheiten.
Drei Beispiele, die in der Elektrotechnik ständig auftauchen:

- __Geschwindigkeit__ $v = \dfrac{s}{t}$, also Weg pro Zeit, mit der Einheit $\dfrac{\text{m}}{\text{s}}$.
- __elektrische Ladung__ $Q = I \cdot t$, also Strom mal Zeit, mit der Einheit $\text{A}\cdot\text{s}$. Diese
  Kombination bekommt einen eigenen Namen, das __Coulomb__: $1\,\text{C} = 1\,\text{A}\cdot\text{s}$.
- __Kraft__ $F = m \cdot a$, mit der Einheit $\text{kg}\cdot\dfrac{\text{m}}{\text{s}^2}$. Auch sie erhält
  einen eigenen Namen, das __Newton__: $1\,\text{N} = 1\,\text{kg}\cdot\dfrac{\text{m}}{\text{s}^2}$.

Dass manche abgeleiteten Einheiten einen eigenen Namen tragen (Coulomb, Newton, später Volt, Ohm, Watt), ist
reine Bequemlichkeit — dahinter steht immer nur eine Kombination der sieben Basiseinheiten. Man kann jede
dieser Einheiten bei Bedarf wieder in Meter, Kilogramm, Sekunden und Ampere zerlegen.

:::grafik
Ein Baumdiagramm: oben die vier mechanisch-elektrischen Basiseinheiten $\text{m}$, $\text{kg}$, $\text{s}$,
$\text{A}$; darunter abzweigend, wie sich daraus $\text{m}/\text{s}$ (Geschwindigkeit), $\text{A}\cdot\text{s}$
(Ladung) und $\text{kg}\,\text{m}/\text{s}^2$ (Kraft) zusammensetzen. Pfeile von den Bausteinen zur abgeleiteten
Größe.
:::

## Einheitenvorsätze: der Umgang mit großen und kleinen Zahlen

In der Elektrotechnik treten Werte über viele Größenordnungen auf — von Picofarad bei Kondensatoren bis zu
Megawatt im Kraftwerk. Damit man nicht mit unübersichtlichen Zehnerpotenzen hantiert, stellt man der Einheit
einen __Einheitenvorsatz__ voran, der für einen festen Faktor steht:

| Vorsatz | Zeichen | Faktor | | Vorsatz | Zeichen | Faktor |
|---|---|---|---|---|---|---|
| Giga | $\text{G}$ | $10^{9}$ | | Milli | $\text{m}$ | $10^{-3}$ |
| Mega | $\text{M}$ | $10^{6}$ | | Mikro | $\mu$ | $10^{-6}$ |
| Kilo | $\text{k}$ | $10^{3}$ | | Nano | $\text{n}$ | $10^{-9}$ |
| — | — | $10^{0}$ | | Piko | $\text{p}$ | $10^{-12}$ |

So wird aus $0{,}000\,001\,5\,\text{F}$ handlich $1{,}5\,\mu\text{F}$ und aus $4700\,\Omega$ einfach
$4{,}7\,\text{k}\Omega$. Der Vorsatz verschiebt nur das Komma, am physikalischen Wert ändert sich nichts.

:::grafik
Ein waagerechter Zahlenstrahl der Zehnerpotenzen von $10^{-12}$ (Piko) bis $10^{9}$ (Giga), an den passenden
Stellen beschriftet mit p, n, µ, m, k, M, G. Zwei Beispielmarkierungen: $1{,}5\,\mu\text{F}$ und
$4{,}7\,\text{k}\Omega$.
:::

## Rechnen mit Einheiten

Der vielleicht nützlichste Punkt für die Praxis: __Einheiten rechnen mit__. Multipliziert, dividiert und kürzt
man sie wie ganz normale Faktoren. Eine Gleichung, in der sowohl Zahlenwerte als auch Einheiten stehen, heißt
__Größengleichung__ — und sie ist nur dann richtig, wenn auf beiden Seiten dieselbe Einheit herauskommt.

Ein Beispiel, die durch einen Leiter geflossene Ladung aus Strom und Zeit:

$$Q = I \cdot t = 2\,\text{A} \cdot 3\,\text{s} = 6\,\text{A}\cdot\text{s} = 6\,\text{C}.$$

Hier wurde nicht nur $2 \cdot 3 = 6$ gerechnet, sondern auch $\text{A} \cdot \text{s} = \text{A}\cdot\text{s}$,
und diese Einheit trägt den Namen Coulomb. Die Einheit entsteht also automatisch aus der Rechnung mit.

**Die Dimensionskontrolle als Sicherheitsnetz.** Genau daraus folgt ein mächtiger Trick, um Rechenfehler zu
finden: die __Einheitenkontrolle__ (auch __Dimensionskontrolle__). Man setzt am Ende einer Rechnung nur die
Einheiten ein und prüft, ob die erwartete Einheit herauskommt. Stimmt sie nicht, steckt irgendwo ein Fehler —
noch bevor man eine einzige Zahl eingesetzt hat.

Rechnet man etwa eine Spannung aus und erhält als Einheit $\text{A}\cdot\Omega$, ist das ein gutes Zeichen,
denn $1\,\text{A}\cdot\Omega = 1\,\text{V}$. Käme stattdessen $\text{A}/\Omega$ heraus, wüsste man sofort: in
der Herleitung ist etwas verrutscht.

**Anders betrachtet.** Die Einheiten sind wie eine zweite, unabhängige Buchführung, die parallel zur Rechnung
mit den Zahlen läuft. Solange beide Bücher am Ende zusammenpassen, kann die Rechnung zwar immer noch einen
Zahlenfehler enthalten — aber ein falscher *Ansatz* fällt fast immer durch eine nicht passende Einheit auf.

:::grafik
Eine Beispielrechnung, in der nur mit Einheiten gearbeitet wird: $\text{V} = \text{A}\cdot\Omega$, daneben
durchgestrichen der Fehlversuch $\text{A}/\Omega$ mit einem roten Kreuz — das Bild macht klar, wie die
Einheitenkontrolle einen falschen Ansatz entlarvt.
:::

:::kern
Jede __physikalische Größe__ ist $G = \{G\}\cdot[G]$, also __Zahlenwert__ mal __Einheit__ — beides gehört
untrennbar zusammen. Das SI ruht auf sieben __Basisgrößen__; für die Elektrotechnik ist die __Stromstärke__
(Einheit __Ampere__) darunter, seit 2019 über die __Elementarladung__ $e$ exakt definiert. Alle anderen
Größen sind __abgeleitet__, ihre Einheiten ergeben sich durch dieselbe Multiplikation und Division. Mit
__Einheitenvorsätzen__ (p, n, µ, m, k, M, G) bleiben die Zahlen handlich. Und weil Einheiten mitrechnen, prüft
die __Dimensionskontrolle__ jede Herleitung auf Plausibilität.
:::

Damit steht das Messwerkzeug. Im nächsten Schritt geht es um die erste große physikalische Erscheinung der
Elektrotechnik: die __elektrische Ladung__ und das __elektrische Feld__, das sie umgibt.

:::quiz
F: Warum ist eine physikalische Angabe ohne Einheit wertlos?
A: Der Zahlenwert sagt nur, *wie viele* einer Bezugsgröße vorliegen, aber nicht *wovon*. Erst die Einheit legt das Bezugsmaß fest — „5" allein kann Ampere, Meter oder Sekunden bedeuten und ist damit nicht interpretierbar.
F: Warum ändert sich der Zahlenwert, wenn man die Einheit wechselt, der physikalische Wert aber nicht?
A: Die Größe ist das Produkt $G=\{G\}\cdot[G]$; bleibt $G$ konstant, müssen sich Zahlenwert und Einheit gegenläufig anpassen. Wie bei „5 Euro = 500 Cent" beschreiben $1\,$m und $100\,$cm denselben Wert in anderer Stückelung.
F: Warum braucht das SI überhaupt Basisgrößen, statt alle Einheiten gleichberechtigt zu behandeln?
A: Man muss irgendwo anfangen: Sieben nicht aufeinander zurückführbare Größen bilden den Grundstock, aus dem sich alle anderen durch Multiplikation und Division aufbauen lassen. So braucht man nur sieben Festlegungen statt unendlich vieler.
F: Warum ist es für die Elektrotechnik bedeutsam, dass die Stromstärke eine Basisgröße ist?
A: Das Ampere wird nicht aus mechanischen Größen abgeleitet, sondern ist selbst ein Grundpfeiler. Die elektrischen Größen stehen damit gleichberechtigt neben Länge, Masse und Zeit und bilden das Fundament, auf dem Ladung, Spannung usw. aufbauen.
F: Welchen Vorteil bringt es, Einheiten über Naturkonstanten statt über Prototypen zu definieren?
A: Eine Naturkonstante wie die Elementarladung ist überall im Universum gleich und jederzeit reproduzierbar. Die Definition hängt dann nicht mehr von einem einzelnen aufbewahrten Gegenstand ab, der beschädigt werden oder sich verändern könnte.
F: Was bedeutet es anschaulich, dass das Ampere seit 2019 an der Elementarladung hängt?
A: Der Zahlenwert von $e$ ist per Definition exakt festgelegt, sodass ein Ampere einer ganz bestimmten, festen Anzahl Elementarladungen pro Sekunde durch den Querschnitt entspricht. Der Strom ist damit direkt auf das Abzählen von Ladungen zurückgeführt.
F: Warum tragen manche abgeleiteten Einheiten eigene Namen wie Coulomb oder Newton?
A: Das ist reine Bequemlichkeit für häufig gebrauchte Kombinationen; dahinter steckt immer nur ein Produkt der Basiseinheiten (z. B. $1\,$C$=1\,$A·s). Bei Bedarf lässt sich jede dieser Einheiten wieder in m, kg, s und A zerlegen.
F: Wozu dienen Einheitenvorsätze, und ändern sie den physikalischen Wert?
A: Sie ersetzen unübersichtliche Zehnerpotenzen durch einen festen Faktor (etwa k für $10^3$), sodass die Zahlen handlich bleiben. Der Vorsatz verschiebt nur das Komma — am physikalischen Wert ändert sich nichts.
F: Warum rechnen Einheiten in einer Größengleichung einfach mit?
A: Multipliziert und dividiert man Größen, werden ihre Einheiten wie normale Faktoren mitgeführt und gekürzt. Dadurch entsteht die Einheit des Ergebnisses automatisch aus der Rechnung, z. B. $A\cdot s=C$.
F: Wie funktioniert die Dimensionskontrolle als Sicherheitsnetz?
A: Man setzt am Ende einer Herleitung nur die Einheiten ein und prüft, ob die erwartete Einheit herauskommt. Stimmt sie nicht (etwa $A/\Omega$ statt $V=A\cdot\Omega$), steckt ein Fehler im Ansatz — und das zeigt sich, noch bevor man eine Zahl einsetzt.
:::
