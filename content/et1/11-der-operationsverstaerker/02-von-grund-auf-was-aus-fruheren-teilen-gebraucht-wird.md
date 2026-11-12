---
title: Von Grund auf: Was aus früheren Teilen gebraucht wird
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1210200
summary: Wie aus einem riesigen, ungenauen Faktor ein Bauteil wird, dessen Verhalten nur noch die Widerstände bestimmen
tags: Spannungsteiler, Steilheit
lang: de
---

Das Kapitel rechnet mit Potenzialen $\varphi$ gegen Masse ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)) und der Knotenregel: Die Ströme in einen Knoten summieren sich zu null ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Zwei Widerstände in Reihe teilen eine Spannung im Verhältnis ihrer Werte (__Spannungsteiler__, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Für den Kondensator gilt $i=C\,\mathrm{d} u/\mathrm{d} t$ ([Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), für die Diode in Durchlassrichtung $I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$ ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)). Ein Bipolartransistor im aktiven Bereich ist eine spannungsgesteuerte Stromquelle: $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, kaum abhängig von $U_\mathrm{CE}$. Um den Arbeitspunkt ist die __Steilheit__ $S=I_\mathrm{C}/U_T$ die Steigung dieser Kurve ([Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)). Die Effektivwerte aus [Kapitel 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html) messen die Stärke einer wechselnden Spannung.

::::formelsammlung
**Strom am Kondensator**

$$i=C\,\mathrm{d} u/\mathrm{d} t$$

Der Strom ist die Kapazität mal der Änderungsgeschwindigkeit der Spannung.

**Diode in Durchlassrichtung**

$$I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$$

$I_\mathrm{S}$ ist der Sättigungssperrstrom, $U_T$ die Temperaturspannung.

**Bipolartransistor im aktiven Bereich**

$$I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$$

Spannungsgesteuerte Stromquelle: $U_\mathrm{BE}$ stellt den Kollektorstrom ein, $U_\mathrm{CE}$ wirkt kaum.

**Steilheit**

$$S=I_\mathrm{C}/U_T$$

Steigung der Kurve $I_\mathrm{C}(U_\mathrm{BE})$ um den Arbeitspunkt.
::::

::::lernkarten
:::karte zusammenhang Knotenregel
Warum summieren sich nach der Knotenregel die Ströme in einen Knoten zu null?
---
Ein Knoten speichert keine Ladung. Was in ihn hineinfließt, muss deshalb im selben Augenblick wieder herausfließen.
--- falsch
Weil sich der Strom an jedem Knoten gleichmäßig auf alle Zweige verteilt und sich die Anteile dabei gegenseitig aufheben.
--- falsch
Weil jeder Knoten über die Masse mit allen anderen verbunden ist; überschüssige Ladung fließt sofort zur Masse ab.
--- falsch
Sie summieren sich nur im Mittel zu null; ein Knoten kann kurzzeitig Ladung sammeln, wie ein kleiner Kondensator.
:::
:::karte zusammenhang Spannungsteiler
Warum teilen zwei Widerstände in Reihe als Spannungsteiler eine Spannung im Verhältnis ihrer Werte auf?
---
Durch beide fließt derselbe Strom, weil kein Abzweig dazwischen liegt. Nach dem ohmschen Gesetz fällt deshalb am größeren Widerstand der größere Teil der Spannung ab.
--- falsch
Die Spannung verteilt sich in einer Reihe immer gleichmäßig auf alle Bauteile; erst eine Last am Abgriff verschiebt sie im Verhältnis der Werte; ohne Last zählt der Wert nicht.
--- falsch
Durch den größeren Widerstand fließt weniger Strom, deshalb fällt an ihm der kleinere Teil ab; die Teilung folgt dem umgekehrten Verhältnis.
--- falsch
Der kleinere Widerstand lässt mehr Strom durch und bekommt deshalb mehr Spannung; der Strom teilt sich in einer Reihe wie die Leitwerte.
:::
:::karte formel Strom am Kondensator
Wie hängt der Strom durch einen Kondensator mit der Spannung an ihm zusammen?
---
$i=C\,\mathrm{d} u/\mathrm{d} t$: Der Strom ist die Kapazität mal der Änderungsgeschwindigkeit der Spannung. Bei konstanter Spannung fließt kein Strom.
--- falsch
$i=C\,u$: Der Strom ist proportional zur Spannung selbst; der Kondensator wirkt wie ein Widerstand mit dem Leitwert $C$, auch bei Gleichspannung.
--- falsch
$i=\frac{1}{C}\,\mathrm{d} u/\mathrm{d} t$: Je größer die Kapazität, desto kleiner ist der Strom bei derselben Änderungsgeschwindigkeit der Spannung.
--- falsch
$i=C\,\mathrm{d} u/\mathrm{d} t$, aber nur solange der Kondensator leer ist; ein geladener Kondensator führt bei keiner Spannungsänderung mehr Strom.
:::
:::karte formel Diode in Durchlassrichtung
Wie hängt der Strom einer Diode in Durchlassrichtung von ihrer Spannung ab?
---
$I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$ mit dem Sättigungssperrstrom $I_\mathrm{S}$ und der Temperaturspannung $U_T$: Der Strom wächst exponentiell mit der Spannung.
--- falsch
$I=I_\mathrm{S}\,U/U_T$ mit dem Sättigungssperrstrom $I_\mathrm{S}$ und der Temperaturspannung $U_T$: Der Strom wächst linear mit der Spannung.
--- falsch
$I=I_\mathrm{S}\,\mathrm{e}^{-U/U_T}$ mit dem Sättigungssperrstrom $I_\mathrm{S}$: Der Strom fällt mit wachsender Spannung, bis er $I_\mathrm{S}$ erreicht.
--- falsch
$I=I_\mathrm{S}\,\mathrm{e}^{U/U_T}$, aber nur in Sperrrichtung; in Durchlassrichtung ist der Strom einfach $U/R$ mit dem Bahnwiderstand der Diode, der den Strom allein begrenzt.
:::
:::karte zusammenhang Transistor als spannungsgesteuerte Stromquelle
Warum kann man einen Bipolartransistor im aktiven Bereich als spannungsgesteuerte Stromquelle ansehen?
---
Sein Kollektorstrom $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ wird von der Spannung $U_\mathrm{BE}$ festgelegt und hängt kaum von $U_\mathrm{CE}$ ab. Eine Spannung stellt also einen Strom ein.
--- falsch
Sein Kollektorstrom hängt nur von $U_\mathrm{CE}$ ab und kaum von $U_\mathrm{BE}$; die Spannung zwischen Kollektor und Emitter stellt also den Strom ein.
--- falsch
Er liefert an seinem Kollektor eine feste Spannung, die der Basisstrom einstellt; welcher Strom dann fließt, bestimmt allein die angeschlossene Last.
--- falsch
Sein Kollektorstrom ist fest, egal welche Spannungen anliegen; der Transistor liefert immer den Sättigungssperrstrom $I_\mathrm{S}$, die Spannung schaltet ihn nur ein.
:::
:::karte zusammenhang Steilheit
Warum ist die Steilheit eines Bipolartransistors im Arbeitspunkt $S=I_\mathrm{C}/U_T$ und damit umso größer, je mehr Strom fließt?
---
Sie ist die Steigung der Kurve $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$, und die Ableitung einer e-Funktion ist der Funktionswert geteilt durch $U_T$.
--- falsch
Sie ist der Kehrwert des Kollektorwiderstands; mit mehr Strom fällt an ihm mehr Spannung ab, und der Kehrwert wächst entsprechend mit.
--- falsch
Sie ist das Verhältnis $I_\mathrm{C}/I_\mathrm{B}$; mit mehr Strom leitet die Basis besser, und diese Stromverstärkung steigt mit $I_\mathrm{C}$ an.
--- falsch
Sie ist die Steigung von $I_\mathrm{C}$ über $U_\mathrm{CE}$; je mehr Strom fließt, desto steiler wird die Ausgangskennlinie im aktiven Bereich.
:::
::::
