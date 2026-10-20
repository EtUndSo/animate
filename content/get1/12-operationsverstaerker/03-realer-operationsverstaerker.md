---
title: Der reale Operationsverstärker
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120700
summary: Wo die idealen Annahmen an ihre Grenzen stoßen – endliche Verstärkung und Bandbreite, die Slew Rate als Tempolimit, Offsetspannung und Eingangsströme als Fehlerquellen und die Gleichtaktunterdrückung.
tags: realer OPV, Verstärkungs-Bandbreite-Produkt, Transitfrequenz, Slew Rate, Offsetspannung, Eingangsruhestrom, CMRR
---

:::konzept
Der ideale OPV ist eine hervorragende Näherung — aber echte Bauteile sind nicht perfekt. Ihre Verstärkung ist
groß, aber **endlich**; sie sind schnell, aber nicht **unendlich** schnell; und kleine fertigungsbedingte
Unsymmetrien erzeugen winzige Fehlerspannungen und -ströme. Wer weiß, *wo* diese Grenzen liegen, erkennt auch,
*wann* die goldenen Regeln noch gelten und wann man genauer hinschauen muss.
:::

**Worum es geht:** Alle bisherigen Formeln galten für den idealen OPV. Dieser Abschluss zeigt die wichtigsten
**realen Grenzen** — und schließt damit das Kapitel und den gesamten Grundkurs zur Schaltungsanalyse ab.

## Endliche Verstärkung und Bandbreite

Die __Leerlaufverstärkung__ $V_0$ ist nicht unendlich, sondern endlich (typisch $10^3$ bis $10^5$) und zudem
**frequenzabhängig**: Zu höheren Frequenzen hin nimmt sie ab. Beschrieben wird das durch das
__Verstärkungs-Bandbreite-Produkt__ (engl. *Gain-Bandwidth Product*, GBW): Das Produkt aus eingestellter
Verstärkung $V$ und zugehöriger Grenzfrequenz $f_\text{g}$ ist konstant und gleich der __Transitfrequenz__
$f_\text{T}$:

$$V \cdot f_\text{g} = f_\text{T}.$$

- __$V$__: die (durch Gegenkopplung) eingestellte __Verstärkung__.
- __$f_\text{g}$__: die __Grenzfrequenz__, bis zu der die Schaltung diese Verstärkung hält.
- __$f_\text{T}$__: die __Transitfrequenz__ — die Frequenz, bei der die Leerlaufverstärkung auf 1 gesunken ist.

Daraus folgt ein grundlegender **Kompromiss**: Je höher man die Verstärkung wählt, desto **kleiner** wird die
nutzbare Bandbreite. Ein OPV mit $f_\text{T} = 1\,\text{MHz}$ liefert bei hundertfacher Verstärkung nur noch
$10\,\text{kHz}$ Bandbreite. Mehr Verstärkung gibt es also nicht umsonst — sie kostet Geschwindigkeit.

:::grafik
Ein doppeltlogarithmisches Diagramm Verstärkung über Frequenz: die fallende Leerlaufverstärkungs-Gerade von
$V_0$ bis zur Transitfrequenz $f_\text{T}$ (bei Verstärkung 1). Zwei waagerechte Linien für zwei eingestellte
Verstärkungen, deren Knick jeweils die zugehörige Grenzfrequenz markiert — höhere Verstärkung, kleinere
Bandbreite.
:::

## Slew Rate: das Tempolimit des Ausgangs

Selbst innerhalb der Bandbreite kann der Ausgang seiner Sollspannung nur mit einer **maximalen
Geschwindigkeit** folgen. Diese größtmögliche Änderungsrate der Ausgangsspannung heißt __Slew Rate__
$S = \left|\dfrac{\mathrm{d}U_\text{a}}{\mathrm{d}t}\right|_\text{max}$, angegeben in $\text{V}/\mu\text{s}$.

Verlangt ein großes, schnelles Signal einen steileren Anstieg, als die Slew Rate erlaubt, kann der Ausgang nicht
mehr folgen: Aus einer steilen Flanke wird eine schräge Rampe, und ein Sinus wird zum Dreieck verzerrt. Während
die Bandbreite vor allem **kleine** Signale begrenzt, ist die Slew Rate die Grenze für **große, schnelle**
Signale — beide zusammen bestimmen, wie schnell ein OPV wirklich ist.

:::grafik
Ein idealer rechteckiger Sollsprung am Ausgang und darüber die tatsächliche Antwort: eine schräge Rampe mit der
Steigung = Slew Rate, die der Sollspannung hinterherhinkt. Beschriftung $S = \mathrm{d}U_\text{a}/\mathrm{d}t$ in
$\text{V}/\mu\text{s}$.
:::

## Offsetspannung und Eingangsströme

Durch unvermeidliche Fertigungsunsymmetrien zwischen den beiden Eingängen ist der Ausgang nicht exakt null, wenn
beide Eingänge auf gleichem Potenzial liegen. Die __Offsetspannung__ $U_\text{os}$ ist die kleine
Eingangsspannung (einige Millivolt oder weniger), die man anlegen müsste, um den Ausgang exakt auf null zu
bringen. Sie wird — wie jedes Eingangssignal — mitverstärkt und erscheint als konstanter Fehler am Ausgang.

Zweitens ist der Eingangswiderstand nicht wirklich unendlich: In die Eingänge fließen kleine __Eingangsruheströme__
(Bias-Ströme, im Bereich von Nano- bis Mikroampere). An den äußeren Widerständen erzeugen sie zusätzliche
Fehlerspannungen. Beide Effekte sind bei grober Signalverarbeitung vernachlässigbar, bei Präzisionsmessungen
aber entscheidend — dort wählt man speziell abgeglichene OPV.

:::grafik
Ein gegengekoppelter OPV mit eingezeichneter kleiner Offsetspannungsquelle $U_\text{os}$ in Reihe zum Eingang und
zwei kleinen Strompfeilen $I_\text{B}$ in die Eingänge. Daneben die Folge: ein konstanter Fehler am Ausgang,
obwohl das Eingangssignal null ist.
:::

## Weitere reale Grenzen

Zwei weitere Punkte runden das Bild ab. Die __Aussteuergrenzen__: Der Ausgang kann die
__Versorgungsspannung__ nicht ganz erreichen — die maximale Ausgangsspannung bleibt je nach Typ etwas unterhalb
der Versorgungsschienen (spezielle „Rail-to-Rail"-OPV kommen besonders nah heran). Und die
__Gleichtaktunterdrückung__ (CMRR, *Common-Mode Rejection Ratio*): Idealerweise verstärkt der OPV nur die
Differenz und ignoriert ein gemeinsames Eingangsniveau völlig. Real ist die Gleichtaktverstärkung klein, aber
nicht null; das Verhältnis von Differenz- zu Gleichtaktverstärkung (das CMRR, typisch $10^3$ bis $10^5$) gibt
an, wie gut der OPV diese Störungen unterdrückt.

:::kern
Der __reale OPV__ weicht in mehreren Punkten vom Ideal ab: Die __Leerlaufverstärkung__ ist endlich und
frequenzabhängig — das __Verstärkungs-Bandbreite-Produkt__ $V\cdot f_\text{g} = f_\text{T}$ erzwingt den
Kompromiss „mehr Verstärkung = weniger Bandbreite". Die __Slew Rate__ begrenzt große, schnelle Signale
(Verzerrung). __Offsetspannung__ und __Eingangsruheströme__ erzeugen konstante Ausgangsfehler. Dazu kommen
__Aussteuergrenzen__ (Ausgang erreicht die Versorgung nicht ganz) und endliche __Gleichtaktunterdrückung__
(CMRR). Für die meisten Rechnungen bleibt der ideale OPV eine gute Näherung — die Grenzen zeigen, wann man genauer
rechnen muss.
:::

Damit ist der Operationsverstärker — und mit ihm der gesamte Grundkurs „Grundgebiete der Elektrotechnik 1 —
Einführung in die Schaltungsanalyse" — abgeschlossen: von der Ladung über Felder, Kondensator und Netzwerke bis
zu Diode, Transistor und Operationsverstärker.

:::quiz
F: Was besagt das Verstärkungs-Bandbreite-Produkt?
A: Das Produkt aus eingestellter Verstärkung und zugehöriger Grenzfrequenz ist konstant und gleich der Transitfrequenz $f_T$ ($V\cdot f_g=f_T$). Verstärkung und nutzbare Bandbreite sind damit fest gegeneinander gekoppelt.
F: Warum sinkt bei höherer Verstärkung die nutzbare Bandbreite?
A: Weil $V\cdot f_g$ konstant bleibt: Wählt man $V$ größer, muss $f_g$ im selben Maß kleiner werden. Ein OPV mit $f_T=1\,$MHz liefert bei 100-facher Verstärkung nur noch 10 kHz Bandbreite.
F: Was ist die Transitfrequenz $f_T$?
A: Die Frequenz, bei der die Leerlaufverstärkung auf 1 abgesunken ist. Oberhalb davon kann der OPV nicht mehr verstärken; sie ist die obere Schranke für das Verstärkungs-Bandbreite-Produkt.
F: Was begrenzt die Slew Rate, und wobei macht sie sich bemerkbar?
A: Sie ist die maximale Änderungsrate der Ausgangsspannung ($V/\mu s$). Verlangt ein großes, schnelles Signal einen steileren Anstieg, kann der Ausgang nicht folgen — aus steilen Flanken werden Rampen, ein Sinus wird zum Dreieck.
F: Worin unterscheiden sich Bandbreite und Slew Rate als Tempogrenzen?
A: Die Bandbreite begrenzt vor allem kleine Signale (frequenzabhängige Verstärkung), die Slew Rate große, schnelle Signale (maximale Anstiegsgeschwindigkeit). Erst beide zusammen bestimmen, wie schnell ein OPV wirklich ist.
F: Was ist die Offsetspannung, und woher kommt sie?
A: Die kleine Eingangsspannung, die man anlegen müsste, damit der Ausgang bei gleichen Eingängen exakt null wird. Sie entsteht durch unvermeidliche Fertigungsunsymmetrien zwischen den beiden Eingängen.
F: Warum ist die Offsetspannung mehr als eine Winzigkeit?
A: Sie wird wie jedes Eingangssignal mit der Schaltungsverstärkung multipliziert und erscheint als konstanter Fehler am Ausgang. Bei hoher Verstärkung oder Präzisionsmessung kann dieser Fehler erheblich werden.
F: Welche Idealannahme verletzen die Eingangsruheströme?
A: Die Annahme eines unendlichen Eingangswiderstands (goldene Regel: kein Eingangsstrom). Real fließen kleine Bias-Ströme in die Eingänge, die an den äußeren Widerständen zusätzliche Fehlerspannungen erzeugen.
F: Warum erreicht der Ausgang die Versorgungsspannung nicht ganz?
A: Die internen Endstufen haben einen Restspannungsabfall, sodass die maximale Ausgangsspannung etwas unter den Versorgungsschienen bleibt. Spezielle „Rail-to-Rail"-OPV kommen besonders nah heran, aber nie exakt dran.
F: Was beschreibt die Gleichtaktunterdrückung (CMRR)?
A: Das Verhältnis von Differenz- zu Gleichtaktverstärkung — wie gut der OPV ein gemeinsames Eingangsniveau ignoriert und nur die Differenz verstärkt. Ideal wäre es unendlich; real liegt es bei $10^3$ bis $10^5$, sodass Gleichtaktstörungen stark, aber nicht vollständig unterdrückt werden.
:::
