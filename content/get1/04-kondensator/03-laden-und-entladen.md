---
title: Laden und Entladen des Kondensators
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Kondensator
order: 40300
summary: Warum sich ein Kondensator über einen Widerstand nicht sofort auflädt, wie die e-Funktion aus einer einfachen Differentialgleichung entsteht und was die Zeitkonstante τ = RC anschaulich bedeutet.
tags: RC-Glied, Ladevorgang, Entladevorgang, Zeitkonstante, e-Funktion, Differentialgleichung
---

:::konzept
Schließt man einen Kondensator über einen Widerstand an eine Quelle an, springt seine Spannung nicht sofort auf
den Endwert. Er füllt sich wie ein Wassertank durch ein dünnes Rohr: am Anfang strömt viel nach, doch je voller
er wird, desto geringer wird der Zufluss — die Spannung nähert sich dem Endwert immer langsamer an. Dieses
„immer langsamer" ist mathematisch die **e-Funktion**, und wie schnell das Ganze abläuft, steckt in einer
einzigen Größe: der **Zeitkonstante**.
:::

**Worum es geht:** Bisher war der Kondensator statisch. Jetzt kommt die Zeit ins Spiel. Mit einem Widerstand in
Reihe entsteht das __RC-Glied__ — die Grundschaltung hinter Verzögerungen, Filtern und Zeitgliedern. Wir leiten
den zeitlichen Verlauf aus der Maschenregel her und deuten die __Zeitkonstante__ $\tau = RC$.

## Die Schaltung: das RC-Glied

Ein __RC-Glied__ besteht aus einer Quelle mit der Spannung $U_0$, einem __Widerstand__ $R$ und einem
__Kondensator__ $C$ in Reihe. Nach der __Maschenregel__ teilt sich die Quellenspannung auf Widerstand und
Kondensator auf:

$$U_0 = u_R + u_C.$$

Zwei Zusammenhänge verknüpfen die Größen: Am Widerstand gilt $u_R = R\cdot i$, und der Strom ist genau die Rate,
mit der sich die Ladung des Kondensators ändert — also $i = C\,\dfrac{\mathrm{d}u_C}{\mathrm{d}t}$. Setzt man
beides ein, entsteht eine Gleichung, in der die gesuchte Spannung $u_C$ **und** ihre eigene Ableitung vorkommen.

:::grafik
Das RC-Glied: Quelle $U_0$, Schalter, Widerstand $R$ und Kondensator $C$ in einer Masche. Eingezeichnet die
Teilspannungen $u_R$ und $u_C$ sowie der Strom $i$, dazu die Maschengleichung $U_0 = u_R + u_C$.
:::

## Der Ladevorgang

**Schritt 1** — die Maschengleichung mit den Bauteilgesetzen füllen. Mit $u_R = R\,i$ und
$i = C\,\mathrm{d}u_C/\mathrm{d}t$ wird aus $U_0 = u_R + u_C$ die __Differentialgleichung__

$$U_0 = R\,C\,\frac{\mathrm{d}u_C}{\mathrm{d}t} + u_C.$$

**Schritt 2** — eine Gleichung, die eine Funktion zusammen mit ihrer Ableitung enthält, heißt
Differentialgleichung. Ihre Lösung für den anfangs ungeladenen Kondensator ($u_C(0) = 0$) ist die bekannte
Aufladekurve:

$$u_C(t) = U_0 \left(1 - e^{-t/\tau}\right), \qquad \tau = R\,C.$$

- __$u_C(t)$__: die __Kondensatorspannung__ zum Zeitpunkt $t$.
- __$U_0$__: die __Quellenspannung__, also der Endwert, dem sich $u_C$ annähert.
- __$e^{-t/\tau}$__: der __Abkling-Term__, der von $1$ (bei $t=0$) auf $0$ (für große $t$) fällt.
- __$\tau$__: die __Zeitkonstante__ $\tau = RC$ (siehe nächster Abschnitt).

Der Strom folgt daraus durch Ableiten und fällt spiegelbildlich ab — am größten im ersten Moment, dann immer
kleiner:

$$i(t) = \frac{U_0}{R}\,e^{-t/\tau}.$$

Das passt zum Wasserbild: Anfangs ist der Kondensator leer, die volle Spannung treibt einen großen Strom. Je
voller er wird, desto kleiner die treibende Differenz $U_0 - u_C$, desto kleiner der Strom — bis gar nichts
mehr nachfließt und der Kondensator „voll" ist.

:::grafik
Zwei Kurven über der Zeit: oben die Spannung $u_C(t)$, die sich von $0$ als e-Funktion an $U_0$ anschmiegt;
unten der Strom $i(t)$, der von $U_0/R$ exponentiell gegen null fällt. Beide mit markierter Zeitkonstante
$\tau$.
:::

## Die Zeitkonstante τ = RC

Die __Zeitkonstante__ bestimmt das Tempo. Setzt man $t = \tau$ ein, ist der Kondensator auf

$$u_C(\tau) = U_0\left(1 - e^{-1}\right) \approx 0{,}63\,U_0$$

geladen — also auf rund **63 %** des Endwerts. Nach $2\tau$ sind es etwa 86 %, nach $5\tau$ über 99 %, sodass
man den Vorgang nach etwa fünf Zeitkonstanten praktisch als abgeschlossen betrachtet.

Dass $RC$ überhaupt eine Zeit ist, bestätigt die __Dimensionskontrolle__:

$$[R]\cdot[C] = \Omega \cdot \text{F} = \frac{\text{V}}{\text{A}} \cdot \frac{\text{A}\cdot\text{s}}{\text{V}} = \text{s}.$$

**Anders betrachtet.** Ein großer Widerstand drosselt den Ladestrom, eine große Kapazität verlangt mehr Ladung
für dieselbe Spannung — beides verlängert die Zeit. Deshalb steht $\tau = RC$: Verdoppelt man $R$ oder $C$,
dauert das Laden doppelt so lange. Mit diesen beiden Bauteilen stellt man gezielt Verzögerungen ein.

## Der Entladevorgang

Trennt man die geladene Schaltung von der Quelle und schließt sie kurz, treibt der Kondensator selbst einen
Strom durch den Widerstand und entlädt sich. Jetzt fehlt die Quelle, die Differentialgleichung lautet
$0 = RC\,\mathrm{d}u_C/\mathrm{d}t + u_C$, und ihre Lösung ist der reine Abfall:

$$u_C(t) = U_0\,e^{-t/\tau}.$$

Nach einer Zeitkonstante ist die Spannung auf $e^{-1} \approx 0{,}37$, also **37 %** ihres Anfangswerts
gesunken — der Spiegelwert zum Laden. Auch hier gilt die Faustregel: Nach etwa $5\tau$ ist der Kondensator
nahezu vollständig entladen.

:::grafik
Die Entladekurve $u_C(t)$: von $U_0$ exponentiell gegen null fallend, mit der Marke bei $t = \tau$ auf Höhe
$0{,}37\,U_0$. Zum Vergleich gestrichelt die Ladekurve, damit der gespiegelte Verlauf sichtbar wird.
:::

:::kern
Im __RC-Glied__ ($R$ und $C$ in Reihe) führt die __Maschenregel__ $U_0 = Ri + u_C$ mit
$i = C\,\mathrm{d}u_C/\mathrm{d}t$ auf eine __Differentialgleichung__. Laden: $u_C(t) = U_0(1 - e^{-t/\tau})$,
Strom $i(t) = \tfrac{U_0}{R}e^{-t/\tau}$. Entladen: $u_C(t) = U_0\,e^{-t/\tau}$. Die __Zeitkonstante__
$\tau = RC$ (Einheit Sekunde) setzt das Tempo: nach $\tau$ 63 % geladen bzw. auf 37 % entladen, nach $5\tau$
praktisch fertig.
:::

Damit ist das Kapitel zum Kondensator abgeschlossen. Als Nächstes verlässt die Elektrostatik die Ruhe: Es geht
um __bewegte__ Ladungen — den Strom in Leitern, den ohmschen Widerstand und die Gesetze ganzer Netzwerke.

:::quiz
F: Warum springt die Kondensatorspannung beim Einschalten nicht sofort auf den Endwert?
A: Der Widerstand begrenzt den Ladestrom, und eine Spannungsänderung am Kondensator erfordert erst, dass Ladung hinüberfließt. Wie ein Tank durch ein dünnes Rohr füllt er sich allmählich, nicht schlagartig.
F: Wie entsteht aus der Maschenregel eine Differentialgleichung?
A: In $U_0=u_R+u_C$ setzt man $u_R=Ri$ und $i=C\,\mathrm{d}u_C/\mathrm{d}t$ ein. Dann steht die gesuchte Spannung $u_C$ zusammen mit ihrer eigenen Ableitung in einer Gleichung — genau das Kennzeichen einer Differentialgleichung.
F: Warum beschreibt gerade eine e-Funktion den Verlauf?
A: Die Änderungsrate ist proportional zum noch verbleibenden Abstand zum Endwert ($\dot u_C\propto U_0-u_C$). Eine Größe, deren Änderung proportional zu sich selbst (bzw. zum Rest) ist, wächst oder fällt exponentiell.
F: Warum ist der Ladestrom im ersten Moment am größten und fällt dann ab?
A: Anfangs ist der Kondensator leer, die volle Differenz $U_0-u_C=U_0$ treibt den Strom. Je voller er wird, desto kleiner diese treibende Differenz und damit der Strom — bis nichts mehr nachfließt.
F: Was bedeutet die Zeitkonstante $\tau$ anschaulich?
A: Sie ist das charakteristische Tempo des Vorgangs: Nach $\tau$ ist der Kondensator auf rund 63 % geladen (bzw. auf 37 % entladen). Nach etwa $5\tau$ gilt der Vorgang als praktisch abgeschlossen.
F: Warum verlängern sowohl ein größerer Widerstand als auch eine größere Kapazität die Ladezeit?
A: Ein großer Widerstand drosselt den Ladestrom, eine große Kapazität verlangt mehr Ladung für dieselbe Spannung. Beides zusammen steckt im Produkt $\tau=RC$ — Verdopplung von $R$ oder $C$ verdoppelt die Zeit.
F: Wie zeigt die Dimensionskontrolle, dass $RC$ wirklich eine Zeit ist?
A: $\Omega\cdot$F$=\tfrac{V}{A}\cdot\tfrac{A\cdot s}{V}=s$ — Volt und Ampere kürzen sich heraus, übrig bleibt die Sekunde. Das bestätigt $\tau=RC$ als Zeitkonstante.
F: Warum ist der Entladeverlauf das Spiegelbild des Ladevorgangs?
A: Ohne Quelle lautet die Gleichung $0=RC\,\dot u_C+u_C$, deren Lösung der reine Abfall $u_C=U_0 e^{-t/\tau}$ ist. Nach $\tau$ sind noch 37 % übrig — genau der Komplementärwert zu den 63 % beim Laden.
F: Warum fließt beim Entladen der Strom, obwohl keine Quelle angeschlossen ist?
A: Der geladene Kondensator ist selbst die Spannungsquelle: Seine gespeicherte Ladung treibt einen Strom durch den Widerstand, bis er sich entladen hat. Die Energie stammt aus dem zuvor aufgebauten Feld.
F: Warum betrachtet man den Vorgang nach etwa $5\tau$ als abgeschlossen?
A: Nach $5\tau$ ist $e^{-5}\approx0{,}0067$, also unter 1 % Restabweichung vom Endwert. Dieser Rest ist für praktische Zwecke vernachlässigbar, daher die Faustregel „nach $5\tau$ fertig".
:::
