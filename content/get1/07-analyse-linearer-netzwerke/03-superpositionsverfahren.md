---
title: Das Superpositionsverfahren
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70700
summary: Wie man ein Netzwerk mit mehreren Quellen löst, indem man jede Quelle einzeln wirken lässt und die Teilwirkungen addiert – warum das dank Linearität erlaubt ist und warum es bei der Leistung nicht funktioniert.
tags: Superposition, Überlagerungssatz, lineare Netzwerke, mehrere Quellen, Teilströme, Leistung
---

:::konzept
Wenn in einer Schaltung mehrere Quellen gleichzeitig treiben, kann die Rechnung schnell unübersichtlich werden.
Das **Superpositionsverfahren** teilt das Problem auf: Man lässt jede Quelle **einzeln** wirken, während die
anderen abgeschaltet sind, berechnet jedes Mal den Beitrag, und addiert am Ende alle Beiträge. So wie mehrere
Personen, die einen Wagen aus verschiedenen Richtungen anschieben — man bestimmt die Wirkung jedes Schubs für
sich und setzt sie zusammen.
:::

**Worum es geht:** Für Netze mit mehreren Quellen gibt es neben Kirchhoff und Ersatzquellen ein drittes
Werkzeug — den __Überlagerungssatz__. Er zerlegt das Netz in einfache Teilprobleme mit je einer Quelle. Wir
sehen das Rezept, den Grund dahinter und eine wichtige Grenze.

## Der Überlagerungssatz

In einem **linearen** Netzwerk mit mehreren unabhängigen Quellen gilt: Der Strom in einem Zweig (oder die
Spannung an einem Bauteil) ist die **Summe** der Beiträge, die jede Quelle **allein** erzeugen würde.

Statt alle Quellen auf einmal zu behandeln, rechnet man also mehrere einfache Schaltungen mit je einer Quelle
und legt die Ergebnisse übereinander — daher der Name __Superposition__ (Überlagerung).

## Das Rezept in Schritten

**Schritt 1** — eine Quelle auswählen, alle anderen __deaktivieren__. Deaktivieren heißt wie bei den
Ersatzquellen: jede ideale __Spannungsquelle__ durch einen **Kurzschluss** ersetzen, jede ideale
__Stromquelle__ durch eine **Unterbrechung**. Hat eine Quelle einen Innenwiderstand, bleibt dieser im Netz
stehen.

**Schritt 2** — das jetzt einfache Netz (nur eine Quelle, sonst reine Widerstände) mit Reihen-, Parallel- und
Teilerregeln lösen und den gesuchten __Teilstrom__ bzw. die __Teilspannung__ notieren.

**Schritt 3** — Schritt 1 und 2 für **jede** Quelle wiederholen, immer mit derselben Zählpfeilrichtung für die
gesuchte Größe.

**Schritt 4** — alle Teilwirkungen **algebraisch addieren** (mit Vorzeichen, je nach Richtung):

$$I = I_1 + I_2 + \ldots, \qquad U = U_1 + U_2 + \ldots$$

- __$I, U$__: der gesuchte __Gesamtstrom__ bzw. die __Gesamtspannung__.
- __$I_k, U_k$__: der __Teilbeitrag__ der $k$-ten Quelle (alle anderen deaktiviert).

:::grafik
Oben das Originalnetz mit zwei Quellen. Darunter zwei Teilbilder: links wirkt nur Quelle 1 (Quelle 2 als
Kurzschluss/Unterbrechung), rechts nur Quelle 2 (Quelle 1 deaktiviert), jeweils mit dem Teilstrom $I_1$ bzw.
$I_2$. Ein Pluszeichen führt zum Gesamtstrom $I = I_1 + I_2$.
:::

## Warum es funktioniert: die Linearität

Der ganze Satz steht und fällt mit der __Linearität__. In einem linearen Netz hängt jede Wirkung (Strom,
Spannung) **proportional** von den Ursachen (den Quellen) ab, und mehrere Ursachen überlagern sich additiv —
genau die beiden Eigenschaften, die man zum Zerlegen und Wiederzusammensetzen braucht. Verdoppelt man eine
Quelle, verdoppelt sich ihr Beitrag; schaltet man eine zweite hinzu, addiert sich deren Beitrag unabhängig
dazu.

Sobald ein **nichtlineares** Bauteil im Spiel ist (eine Diode, ein nicht konstanter Widerstand), gilt das nicht
mehr — dann darf man die Quellen nicht mehr getrennt behandeln. Das Verfahren ist also ausdrücklich ein Werkzeug
für **lineare** Netze.

## Vorsicht: nicht bei der Leistung

Eine häufige Falle: Man darf **Leistungen nicht überlagern**. Die Leistung hängt **quadratisch** von Strom bzw.
Spannung ab,

$$P = I^2 \cdot R = \frac{U^2}{R},$$

und quadratische Größen sind nicht additiv: $(I_1 + I_2)^2 \ne I_1^2 + I_2^2$. Der richtige Weg ist deshalb,
**zuerst** die Gesamtströme bzw. -spannungen durch Superposition zu bestimmen und **erst danach** daraus die
Leistung zu berechnen. Superposition gilt nur für die linearen Größen Strom und Spannung, nicht für die
nichtlineare Leistung.

:::grafik
Eine Warntafel: durchgestrichen „$P = P_1 + P_2$" (rotes Kreuz), daneben richtig „erst $I = I_1 + I_2$, dann
$P = I^2 R$". Darunter kurz der Grund: $(I_1+I_2)^2 \ne I_1^2 + I_2^2$.
:::

:::kern
Im __linearen__ Netz ist jeder Strom/jede Spannung die Summe der Beiträge der einzelnen Quellen
(__Überlagerungssatz__). Rezept: jede Quelle einzeln wirken lassen, die anderen __deaktivieren__ (Spannungsquelle
→ Kurzschluss, Stromquelle → offen), die Teilgrößen berechnen und **algebraisch addieren**
($I = I_1 + I_2 + \ldots$). Grund ist die __Linearität__ (proportional + additiv); bei nichtlinearen Bauteilen
gilt es nicht. Und: __Leistung__ darf man nicht überlagern (sie ist quadratisch) — erst Ströme/Spannungen
summieren, dann $P = I^2 R$.
:::

Neben diesen allgemeinen Verfahren helfen bei bestimmten Strukturen gezielte Umformungen. Eine besonders
nützliche ist die __Stern-Dreieck-Transformation__, mit der sich sonst unauflösbare Widerstandsgruppen doch
zusammenfassen lassen.
