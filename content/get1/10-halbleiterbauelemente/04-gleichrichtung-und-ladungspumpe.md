---
title: Gleichrichtung und Ladungspumpe
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100600
summary: Die wichtigste Anwendung der Diode – aus Wechselspannung Gleichspannung machen. Vom Einweggleichrichter über die Graetz-Brücke und die Glättung mit Kondensator bis zur Ladungspumpe, die die Spannung sogar anhebt.
tags: Gleichrichter, Einweggleichrichter, Brückengleichrichter, Graetz, Glättung, Brummspannung, Ladungspumpe
---

:::konzept
Aus der Steckdose kommt Wechselspannung, die meisten Geräte brauchen aber Gleichspannung. Genau das leistet die
Diode als Ventil: Eine einzelne Diode schneidet die negativen Halbwellen weg, vier Dioden in einer Brücke
klappen sie sogar nach oben, und ein Kondensator glättet das Ergebnis zu nahezu glatter Gleichspannung. Mit
einer geschickten Anordnung aus Dioden und Kondensatoren lässt sich die Spannung dabei sogar **vervielfachen**.
:::

**Worum es geht:** Hier zahlt sich die Einseitigkeit der Diode aus. Wir bauen die __Gleichrichtung__ in Stufen
auf — Einweg, Brücke, Glättung — und schauen zum Schluss auf die __Ladungspumpe__, die Spannung nicht nur
gleichrichtet, sondern anhebt.

## Der Einweggleichrichter

Die einfachste Schaltung ist eine **einzige Diode** in Reihe mit dem Verbraucher. Sie lässt nur die Halbwellen
durch, in denen sie in Durchlassrichtung gepolt ist — die positiven. Die negativen Halbwellen werden gesperrt
und fehlen am Ausgang.

Das Ergebnis ist ein pulsierender Gleichstrom: richtig „gleich" ist er nicht, denn die Hälfte der Zeit liegt
gar keine Spannung an. Immerhin fließt der Strom nur noch in **eine** Richtung. Nachteil: Die halbe Energie
bleibt ungenutzt, und die Lücken sind groß.

:::grafik
Links die Schaltung: Wechselspannungsquelle, eine Diode, Lastwiderstand. Rechts zwei übereinanderliegende
Kurven: die sinusförmige Eingangsspannung und darunter die Ausgangsspannung, bei der nur die positiven Halbwellen
übrig bleiben (negative abgeschnitten).
:::

## Der Brückengleichrichter (Graetz-Schaltung)

Deutlich besser ist die __Graetz-Brücke__ aus **vier Dioden**. Sie ist so verschaltet, dass der Strom in beiden
Halbwellen denselben Weg durch den Verbraucher nimmt — in der positiven Halbwelle leiten zwei der Dioden, in der
negativen die anderen beiden, und zwar immer so, dass am Ausgang die Spannung **immer gleich gepolt** ist.

Damit werden **beide** Halbwellen genutzt (Zweiweggleichrichtung): Die negative wird nach oben „geklappt". Der
Ausgang pulsiert jetzt mit der doppelten Netzfrequenz (bei $50\,\text{Hz}$ Netz also $100\,\text{Hz}$), die
Lücken sind viel kleiner, und es geht keine Halbwelle verloren. Ein Preis: In jeder Halbwelle liegen zwei Dioden
im Strompfad, es fallen also zwei Schleusenspannungen ab.

:::grafik
Die Graetz-Brücke: vier Dioden als Raute zwischen Wechselspannungsquelle und Last, mit farbig markiertem
Strompfad für die positive (zwei leitende Dioden) und die negative Halbwelle (die anderen beiden). Daneben die
Ausgangskurve, bei der alle Halbwellen positiv sind.
:::

## Glättung mit dem Ladekondensator

Pulsierende Gleichspannung ist noch keine saubere Gleichspannung. Schaltet man einen __Ladekondensator__
parallel zum Verbraucher, füllt er die Täler zwischen den Spitzen: In den Spitzen lädt er sich auf, in den
Lücken speist er den Verbraucher weiter. Übrig bleibt eine fast glatte Spannung mit einer kleinen
sägezahnförmigen Restwelligkeit, der __Brummspannung__ $U_\text{br}$.

Ihre Größe schätzt man über die Kondensatorentladung zwischen zwei Spitzen ab:

$$U_\text{br} \approx \frac{I}{f \cdot C}.$$

- __$U_\text{br}$__: die __Brummspannung__ (Restwelligkeit).
- __$I$__: der entnommene __Laststrom__.
- __$f$__: die __Pulsfrequenz__ ($100\,\text{Hz}$ bei Zweiweggleichrichtung am $50$-Hz-Netz).
- __$C$__: die __Kapazität__ des Ladekondensators.

Je größer $C$ und je höher die Pulsfrequenz, desto glatter die Spannung — ein weiterer Vorteil der Brücke, die
mit $100\,\text{Hz}$ doppelt so oft nachlädt wie der Einweggleichrichter. Der geglättete Scheitelwert liegt
nahe bei $\hat{U} = U_\text{eff}\cdot\sqrt{2}$ abzüglich der Diodenspannungen.

:::grafik
Die geglättete Ausgangsspannung: die pulsierende Kurve der Brücke, darüber die durch den Kondensator geglättete,
fast waagerechte Linie mit kleiner Sägezahn-Welligkeit. Die Brummspannung $U_\text{br}$ als Höhe des Sägezahns
beschriftet, dazu der Ladekondensator parallel zur Last im Schaltbild.
:::

## Die Ladungspumpe

Dioden und Kondensatoren können Spannung nicht nur gleichrichten, sondern auch **anheben** — in einer
__Ladungspumpe__. Die Grundidee des __Spannungsverdopplers__: In der einen Halbwelle lädt sich ein Kondensator
über eine Diode auf den Scheitelwert $\hat{U}$ auf. In der nächsten Halbwelle wird er in Reihe zur Quelle
geschaltet, sodass sich seine Spannung zur Quellenspannung addiert, und lädt über eine zweite Diode einen
Ausgangskondensator auf nahezu $2\hat{U}$.

So entsteht aus der Wechselspannung eine Gleichspannung mit fast dem doppelten Scheitelwert — ganz ohne
Transformator. Schaltet man mehrere solcher Stufen hintereinander (Kaskade), lässt sich die Spannung
vervielfachen; das Prinzip steckt in Hochspannungserzeugern und in vielen integrierten Schaltungen, die intern
eine höhere Spannung brauchen, als von außen anliegt.

:::grafik
Ein Spannungsverdoppler: Quelle, zwei Dioden und zwei Kondensatoren. Zwei Teilbilder zeigen die beiden
Halbwellen — in der ersten lädt sich der erste Kondensator auf $\hat{U}$, in der zweiten addiert er sich zur
Quelle und lädt den Ausgangskondensator auf $\approx 2\hat{U}$.
:::

:::kern
Die Diode macht aus Wechsel- Gleichspannung. Der __Einweggleichrichter__ (eine Diode) nutzt nur die positiven
Halbwellen; die __Graetz-Brücke__ (vier Dioden) nutzt beide und liefert eine mit doppelter Netzfrequenz
pulsierende, immer positive Spannung. Ein paralleler __Ladekondensator__ glättet sie bis auf die
__Brummspannung__ $U_\text{br} \approx I/(f\,C)$. Eine __Ladungspumpe__ aus Dioden und Kondensatoren hebt die
Spannung sogar an (Spannungsverdoppler $\approx 2\hat{U}$, kaskadierbar).
:::

Mit der Diode ist das erste, einfachste Halbleiterbauelement verstanden. Fügt man eine dritte Zone hinzu,
entsteht ein Bauteil, das Ströme nicht nur schaltet, sondern **verstärkt** — der __Bipolartransistor__.
