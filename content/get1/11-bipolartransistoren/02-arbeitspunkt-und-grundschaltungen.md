---
title: Arbeitspunkt und Grundschaltungen des Transistors
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110200
summary: Wie man den Transistor mit Basisspannungsteiler und Emitterwiderstand stabil in den aktiven Bereich bringt, warum der Emitterwiderstand den Arbeitspunkt selbst nachregelt und wodurch sich die drei Grundschaltungen unterscheiden.
tags: Arbeitspunkt, Basisspannungsteiler, Emitterwiderstand, Gegenkopplung, Emitterschaltung, Kollektorschaltung, Basisschaltung
---

:::konzept
Damit ein Transistor sauber verstärkt, muss er im **aktiven Bereich** sitzen — und zwar stabil. Dafür stellt man
seinen **Arbeitspunkt** mit ein paar Widerständen ein: Ein Spannungsteiler legt die Basis fest, ein
Emitterwiderstand sorgt dafür, dass der Arbeitspunkt sich **selbst nachregelt**, falls er wegdriften will. Erst
auf diesem stabilen Gleichstrom-Arbeitspunkt „reitet" später das zu verstärkende Signal.
:::

**Worum es geht:** Der Transistor verstärkt nur im aktiven Bereich (voriger Abschnitt). Hier klären wir, wie man
ihn dorthin bringt (__Arbeitspunkteinstellung__), wie der __Emitterwiderstand__ ihn stabil hält und welche drei
__Grundschaltungen__ es gibt.

## Der Arbeitspunkt

Der __Arbeitspunkt__ (AP) legt die Gleichströme und -spannungen fest, um die herum das Signal schwankt — vor
allem den Kollektorstrom $I_\text{C}$ und die Kollektor-Emitter-Spannung $U_\text{CE}$. Für die Schaltung mit
Kollektorwiderstand $R_\text{C}$ und Emitterwiderstand $R_\text{E}$ liefert die Maschenregel die
Gleichstrom-__Arbeitsgerade__:

$$U_\text{CE} = U_\text{B} - I_\text{C}\,(R_\text{C} + R_\text{E}).$$

- __$U_\text{CE}$__: die __Kollektor-Emitter-Spannung__.
- __$U_\text{B}$__: die __Betriebsspannung__ (Versorgung).
- __$I_\text{C}$__: der __Kollektorstrom__.
- __$R_\text{C}, R_\text{E}$__: __Kollektor-__ und __Emitterwiderstand__.

Wie bei der Diode ist der Arbeitspunkt der Schnittpunkt dieser Geraden mit dem Kennlinienfeld. Man legt ihn
üblich **in die Mitte** des aktiven Bereichs, damit das Signal nach oben wie nach unten gleich viel Platz hat,
ohne in Sättigung oder Sperrbereich zu geraten (sonst würde es verzerrt).

:::grafik
Das Ausgangskennlinienfeld $I_\text{C}$–$U_\text{CE}$ mit der eingezeichneten Arbeitsgeraden von $U_\text{B}$
(Spannungsachse) zu $U_\text{B}/(R_\text{C}+R_\text{E})$ (Stromachse). Der Arbeitspunkt sitzt mittig; links/rechts
der Aussteuerbereich für das Signal eingezeichnet.
:::

## Arbeitspunkteinstellung: Spannungsteiler und Emitterwiderstand

Den Arbeitspunkt stellt man mit einem __Basisspannungsteiler__ aus zwei Widerständen $R_1, R_2$ ein, der an der
Basis eine feste Spannung erzeugt. Damit diese Spannung vom schwankenden Basisstrom möglichst unabhängig bleibt,
wählt man den Querstrom durch den Teiler etwa **zehnmal** so groß wie den Basisstrom.

Der eigentliche Trick ist der __Emitterwiderstand__ $R_\text{E}$. Er bewirkt eine __Stromgegenkopplung__, die den
Arbeitspunkt selbsttätig stabilisiert — unverzichtbar, weil die Stromverstärkung $\beta$ von Exemplar zu Exemplar
stark streut und mit der Temperatur wandert. Der Regelmechanismus:

**Schritt 1** — der Kollektorstrom $I_\text{C}$ steigt (etwa weil der Transistor wärmer wird).

**Schritt 2** — damit steigt auch der Spannungsabfall $I_\text{E}\,R_\text{E}$ am Emitterwiderstand, das
Emitterpotenzial hebt sich an.

**Schritt 3** — weil die Basisspannung durch den Teiler **fest** liegt, verkleinert sich dadurch die
Basis-Emitter-Spannung $U_\text{BE}$.

**Schritt 4** — kleinere $U_\text{BE}$ bedeutet weniger Basisstrom und damit weniger Kollektorstrom — der
anfängliche Anstieg wird **zurückgeregelt**. Der Arbeitspunkt hält sich von selbst.

Dieser Selbstregeleffekt kostet etwas Verstärkung (für das Signal wirkt $R_\text{E}$ ebenfalls gegenkoppelnd):
Näherungsweise ist die Spannungsverstärkung dann $v_U \approx -\dfrac{R_\text{C}}{R_\text{E}}$. Will man für
Wechselsignale die volle Verstärkung, überbrückt man $R_\text{E}$ mit einem Kondensator $C_\text{E}$ — dann
bleibt die Gegenkopplung für den Gleich-Arbeitspunkt erhalten, verschwindet aber für das Signal.

:::grafik
Die Emitterschaltung mit Arbeitspunkteinstellung: Betriebsspannung $U_\text{B}$, Basisspannungsteiler
$R_1/R_2$, Kollektorwiderstand $R_\text{C}$, Emitterwiderstand $R_\text{E}$ (optional mit Überbrückungs-
kondensator $C_\text{E}$). Ein roter Regelkreis-Pfeil deutet die Gegenkopplung an: $I_\text{C}\uparrow \to
U_\text{E}\uparrow \to U_\text{BE}\downarrow \to I_\text{C}\downarrow$.
:::

## Die drei Grundschaltungen

Je nachdem, welcher Anschluss dem Ein- und Ausgang **gemeinsam** ist, unterscheidet man drei Grundschaltungen
mit sehr unterschiedlichen Eigenschaften:

| Grundschaltung | gemeinsam | Spannungs­verstärkung | Strom­verstärkung | Eingangs­widerstand | typischer Einsatz |
|---|---|---|---|---|---|
| Emitterschaltung | Emitter | groß (invertiert) | groß | mittel | Universalverstärker |
| Kollektorschaltung | Kollektor | $\approx 1$ | groß | hoch | Impedanzwandler / Puffer |
| Basisschaltung | Basis | groß | $\approx 1$ | niedrig | Hochfrequenz |

Die __Emitterschaltung__ ist der Standard-Spannungsverstärker: große Verstärkung, dafür dreht sie das Signal um
$180^\circ$ (invertierend). Die __Kollektorschaltung__ (auch __Emitterfolger__) verstärkt die Spannung praktisch
nicht ($v_U \approx 1$), hat aber hohen Eingangs- und niedrigen Ausgangswiderstand — ideal als __Impedanzwandler__,
der eine empfindliche Quelle von einer niederohmigen Last entkoppelt. Die __Basisschaltung__ hat einen sehr
kleinen Eingangswiderstand und wird vor allem bei hohen Frequenzen eingesetzt.

:::grafik
Drei kleine Schaltbilder nebeneinander (Emitter-, Kollektor-, Basisschaltung), jeweils mit markiertem Ein- und
Ausgang und dem gemeinsamen Anschluss hervorgehoben. Darunter das Stichwort zur Eigenschaft (invertierend /
Folger / HF).
:::

:::kern
Der __Arbeitspunkt__ (Schnittpunkt der Arbeitsgeraden $U_\text{CE} = U_\text{B} - I_\text{C}(R_\text{C}+R_\text{E})$
mit dem Kennlinienfeld) wird mittig in den aktiven Bereich gelegt. Man stellt ihn mit einem
__Basisspannungsteiler__ ein (Querstrom $\approx 10\times$ Basisstrom) und stabilisiert ihn mit dem
__Emitterwiderstand__ $R_\text{E}$ (Stromgegenkopplung: $I_\text{C}\uparrow \Rightarrow U_\text{BE}\downarrow
\Rightarrow I_\text{C}\downarrow$), notfalls für Signale mit $C_\text{E}$ überbrückt. Drei __Grundschaltungen__:
__Emitterschaltung__ (großer, invertierter Spannungsgewinn), __Kollektorschaltung__ (Emitterfolger,
Impedanzwandler), __Basisschaltung__ (Hochfrequenz).
:::

Mit stabilem Arbeitspunkt im aktiven Bereich kann der Transistor seine eigentliche Aufgabe erfüllen: ein kleines
Signal **verstärken**. Wie das quantitativ funktioniert, zeigt der letzte Abschnitt.

:::quiz
F: Warum muss man den Arbeitspunkt eines Verstärkertransistors überhaupt einstellen?
A: Der Transistor verstärkt linear nur im aktiven Bereich. Der Arbeitspunkt legt die Ruhe-Gleichgrößen fest, um die das Signal schwankt, damit es weder in Sättigung noch in den Sperrbereich gerät.
F: Warum legt man den Arbeitspunkt mittig in den aktiven Bereich?
A: Damit das Signal nach oben und unten gleich viel Aussteuerraum hat. Sitzt der AP zu nah an einer Grenze, wird eine Halbwelle in Sättigung oder Sperrbereich abgeschnitten und das Signal verzerrt.
F: Wozu dient der Basisspannungsteiler?
A: Er erzeugt an der Basis eine feste, definierte Spannung und legt so den Arbeitspunkt fest. Ein fester Basispunkt ist Voraussetzung dafür, dass der Emitterwiderstand überhaupt gegenkoppeln kann.
F: Warum wählt man den Querstrom durch den Teiler etwa zehnmal so groß wie den Basisstrom?
A: Dann belastet der schwankende Basisstrom den Teiler kaum, und die Basisspannung bleibt nahezu konstant. So ist der Arbeitspunkt unabhängig von den Streuungen des Transistors.
F: Wie stabilisiert der Emitterwiderstand den Arbeitspunkt?
A: Durch Stromgegenkopplung: Steigt $I_C$, steigt der Abfall $I_E R_E$, das Emitterpotenzial hebt sich, und bei fester Basisspannung sinkt $U_{BE}$ — das drosselt $I_C$ wieder. Der Arbeitspunkt regelt sich selbst nach.
F: Warum ist diese Selbststabilisierung überhaupt nötig?
A: Die Stromverstärkung $\beta$ streut stark von Exemplar zu Exemplar und wandert mit der Temperatur. Ohne Gegenkopplung würde der Arbeitspunkt wegdriften; $R_E$ fängt das automatisch ab.
F: Warum kostet der Emitterwiderstand Verstärkung, und wie umgeht man das?
A: $R_E$ koppelt auch für das Signal gegen, sodass $v_U\approx-R_C/R_E$ sinkt. Überbrückt man $R_E$ mit einem Kondensator $C_E$, bleibt die Gegenkopplung für den Gleich-Arbeitspunkt erhalten, verschwindet aber für das Wechselsignal.
F: Wonach unterscheidet man die drei Grundschaltungen?
A: Danach, welcher Anschluss Ein- und Ausgang gemeinsam ist — Emitter, Kollektor oder Basis. Diese Wahl bestimmt Spannungs- und Stromverstärkung sowie Ein- und Ausgangswiderstand.
F: Warum eignet sich die Kollektorschaltung als Impedanzwandler, obwohl sie die Spannung nicht verstärkt?
A: Sie hat hohen Eingangs- und niedrigen Ausgangswiderstand bei $v_U\approx1$. Damit entkoppelt sie eine empfindliche, hochohmige Quelle von einer niederohmigen Last, ohne die Spannung zu verändern.
F: Warum invertiert die Emitterschaltung das Signal?
A: Steigt die Basisspannung, steigt $I_C$, und der größere Abfall an $R_C$ senkt die Kollektorspannung. Ein steigender Eingang führt also zu einem fallenden Ausgang — eine Phasendrehung um 180°.
:::
