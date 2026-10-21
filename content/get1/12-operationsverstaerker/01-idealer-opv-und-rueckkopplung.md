---
title: Der Operationsverstärker – idealer OPV und Rückkopplung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120100
summary: Von Grund auf – was ein Operationsverstärker ist und warum erst die Rückkopplung ihn nützlich macht. Leitbild ist eine überempfindliche Balkenwaage, deren Zeiger ein Motor antreibt. Mit Rauschen, Effektivwert und Signal-Rausch-Verhältnis, den vier Rauschquellen, dem Differenzverstärker samt Transistorschaltung, dem idealen Operationsverstärker, dem Komparator und Flash-Wandler, Gegen- und Mitkopplung mit den goldenen Regeln und der Frage, warum eine Schaltung zur Ruhe kommt, und dem Schmitt-Trigger mit Hysterese. Mit Beispiel-Seite.
tags: Operationsverstärker, OPV, idealer OPV, Differenzverstärker, virtueller Kurzschluss, Gegenkopplung
---

## Anschaulich

Der __Operationsverstärker__, kurz OPV, ist eine integrierte Schaltung aus vielen Transistoren mit zwei Eingängen und einem Ausgang. Je nachdem, wie man ihn
von außen beschaltet, addiert, subtrahiert, integriert oder vergleicht er Spannungen; daher der Name, nach den Rechenoperationen. In ihm stecken Stromspiegel
und Emitterfolger aus den Transistorkapiteln und der Differenzverstärker, den dieser Artikel einführt. Er klärt außerdem, was der OPV ideal tut, wozu man ihn braucht und warum
erst die Rückkopplung aus seiner riesigen Verstärkung eine berechenbare Schaltung macht.

**Das Leitbild dieses Artikels:** **eine überempfindliche Balkenwaage mit Motor.** Auf die beiden Schalen einer Balkenwaage legt man die beiden
Eingangsspannungen. Den Zeiger bewegt nicht der Balken selbst, sondern ein kräftiger Motor, der schon auf die winzigste Neigung mit großem Ausschlag antwortet.
Der Zeiger ist die Ausgangsspannung, und zwei Anschläge begrenzen ihn; das sind die Versorgungsspannungen. Wie jedes Bild ist das eine Analogie; das Gewicht
steht für die Spannung an einem Eingang.

Vier Folgerungen, und eine fünfte zum Schluss:

- **Nur der Unterschied zählt.** Legt man auf beide Schalen dasselbe Zusatzgewicht oder rüttelt am Tisch, neigt sich nichts. Störungen, die beide Eingänge
  gleich treffen, fallen heraus; das ist der Differenzverstärker.
- **Ohne Rückmeldung schlägt sie aus.** Schon ein Sandkorn mehr auf einer Seite treibt den Zeiger an den Anschlag. So arbeitet der Komparator.
- **Mit Rückmeldung hält sie das Gleichgewicht.** Schiebt der Motor ein Gegengewicht auf die sinkende Seite, bis der Balken waagrecht steht, zeigt die Stellung
  des Gegengewichts das Gewicht an, gleich wie kräftig der Motor ist. Nach diesem Prinzip der Kraftkompensation arbeiten Präzisionswaagen; beim OPV heißt es
  Gegenkopplung.
- **Falsch herum zurückgemeldet kippt sie.** Schiebt der Motor das Gewicht auf die Seite, die schon unten ist, kippt die Waage ganz und bleibt liegen, bis ein
  großes Gegengewicht sie zurückzwingt. Das ist die Mitkopplung, und mit ihr der Schmitt-Trigger.

Auch eine ruhig stehende Waage zittert ein klein wenig, weil sich ihre Moleküle bewegen. Dieses Zittern ist dieselbe Erscheinung wie das Rauschen in einer
Schaltung, und mit ihm beginnt das Skript.

| An der Waage | Am Operationsverstärker |
|---|---|
| linke und rechte Schale | nichtinvertierender und invertierender Eingang |
| Unterschied der Gewichte | Differenzspannung $U_D$ |
| Zeiger, vom Motor verstärkt | Ausgangsspannung, $v_D$-mal die Differenz |
| Anschläge des Zeigers | Grenzen der Ausgangsspannung durch die Versorgung |
| gleiches Zusatzgewicht auf beiden Schalen | Gleichtaktspannung, wird unterdrückt |
| Zittern durch die Wärmebewegung | thermisches Rauschen |
| Waage ohne Rückmeldung | Komparator |
| Motor schiebt ein Gegengewicht, bis der Balken waagrecht steht | Gegenkopplung, $U_D$ wird null |
| Motor schiebt Gewicht auf die sinkende Seite | Mitkopplung, Schmitt-Trigger |

:::grafik
Szene: get1/operationsverstaerker/01-balkenwaage · Vorlage: opv-waage
Eine Balkenwaage mit zwei Schalen, beschriftet mit $U_{e+}$ und $U_{e-}$; über dem Balken ein kleiner Motor, der einen langen Zeiger zwischen zwei Anschlägen
bewegt, beschriftet mit der Ausgangsspannung und den Grenzen. Ein Umschalter wählt drei Betriebsarten. Ohne Rückmeldung schlägt der Zeiger schon bei einem
Sandkorn Unterschied bis an den Anschlag. Mit Gegenkopplung verschiebt der Motor zugleich ein Gegengewicht auf der Schale $U_{e-}$, bis der Balken waagrecht steht;
eine Skala am Gegengewicht zeigt den Messwert, und ein Regler für die Motorstärke ändert daran fast nichts. Mit Mitkopplung schiebt er das Gewicht auf die
sinkende Seite, und die Waage kippt ganz. Ein Knopf „Tisch rütteln“ bewegt beide Schalen gleich, und der Zeiger bleibt ruhig. Kernaussage: Nur der Unterschied
zählt, und erst die Rückmeldung entscheidet, ob die Waage misst oder kippt. (Rot = Zeiger und Ausgang, blau = Schalen und Eingänge, orange = Motor und
Rückmeldung, grau = Gestell und Anschläge.)
:::

## Rauschen und Signal-Rausch-Verhältnis

Das Skript beginnt in Abschnitt 12.1 mit einer wichtigen Anwendung: Operationsverstärker helfen, eine Messgröße von Störungen zu trennen. Die wichtigste
Störung ist das __Rauschen__, eine zufällig schwankende Spannung, die man sich aus sehr vielen Sinusschwingungen verschiedener Frequenzen, Amplituden und
Phasen zusammengesetzt denken kann. Ihren Verlauf kann man nicht vorhersagen, nur statistisch beschreiben, als __Zufallsprozess__. Ihr Mittelwert ist null; ein
brauchbares Maß ist der Effektivwert, die Wurzel aus dem Mittelwert des Quadrats, wie im Artikel über Gleichrichtung.

Wie sich das Rauschen auf die Frequenzen verteilt, sagt seine spektrale Dichte $|u_r(f)|^2$, im Skript Rauschspannungsdichte genannt. Sie gibt an, welcher Anteil
des mittleren Quadrats auf jedes Hertz Bandbreite um die Frequenz $f$ entfällt, und hat die Einheit $\text{V}^2/\text{Hz}$; ihre Wurzel $|u_r(f)|$ misst man in
$\text{V}/\sqrt{\text{Hz}}$. Der Effektivwert $U_r$, im Skript $u_{r,\text{eff}}$, ist die Wurzel aus der Summe über alle Frequenzen, Gleichung 12.1:

:::formel Definition
$$U_r = \sqrt{\int_0^\infty |u_r(f)|^2\,df}.$$
:::

**So liest man das:** Eingabe ist die Dichte als Funktion der Frequenz, Ausgabe eine Spannung in Volt. Unter der Wurzel steht die gesamte mittlere
Rauschleistung, bezogen auf einen Widerstand von $1\,\Omega$. Zwei Folgerungen sind wichtig. Rauschen aus verschiedenen Frequenzbändern oder aus voneinander
unabhängigen Quellen addiert sich in den Quadraten, nicht in den Spannungen. Und je schmaler das Band, das eine Schaltung durchlässt, desto weniger Rauschen
kommt durch: Bei konstanter Dichte $d$ über eine Bandbreite $\Delta f$ ist $U_r$ gleich $d\sqrt{\Delta f}$.

Wie stark ein Signal aus dem Rauschen herausragt, misst das __Signal-Rausch-Verhältnis__, englisch signal-to-noise ratio, SNR, das Verhältnis der Leistungen,
mit dem Effektivwert $U_S$ des Signals:

$$\text{SNR} = \frac{U_S^2}{U_r^2}.$$

Das Skript sagt, das Rauschen lasse sich nicht verhindern, aber man könne das Nutzsignal verstärken und so das SNR verbessern. So allein stimmt das nicht: Ein
Verstärker vergrößert das Signal und das Rauschen, das schon an seinem Eingang liegt, um denselben Faktor, und er fügt eigenes Rauschen hinzu; das Verhältnis
kann dabei nur gleich bleiben oder schlechter werden. Was wirklich hilft, sind drei Dinge. Man verstärkt früh und rauscharm, bevor lange Leitungen und weitere
Stufen ihr eigenes, festes Rauschen hinzufügen, das dann relativ wenig zählt. Man begrenzt die Bandbreite auf das, was das Signal braucht. Und man unterdrückt
Störungen, die auf beiden Leitungen gleich ankommen, mit dem Differenzverstärker des übernächsten Abschnitts.

**Im Bild:** Das Zittern der Waage ist kein einzelnes Schaukeln, sondern ein Gemisch vieler kleiner Bewegungen. Ihre Stärke misst man, indem man die
Bewegungsenergie aller Anteile zusammenzählt.

:::herleitung
**Mittleres Quadrat und Dichte.** Der Effektivwert ist die Wurzel aus dem zeitlichen Mittelwert von $u_r^2$. Die Dichte verteilt dieses mittlere Quadrat auf die
Frequenzen: Ein schmales Band der Breite $df$ um $f$ trägt $|u_r(f)|^2\,df$ bei. Summiert, also integriert, über alle Frequenzen ergibt sich das ganze mittlere
Quadrat und mit der Wurzel die Formel.

**Unabhängige Anteile addieren sich in den Quadraten.** Für zwei Anteile $a(t)$ und $b(t)$ ist das mittlere Quadrat der Summe

$$\overline{(a + b)^2} = \overline{a^2} + 2\,\overline{a\,b} + \overline{b^2}.$$

Sind sie unabhängig und haben beide den Mittelwert null, ist der mittlere Wert des Produkts null, und es bleibt die Summe der mittleren Quadrate.

**Konstante Dichte.** Ist $|u_r(f)|^2$ im Band gleich $d^2$ und außerhalb null, ist das Integral $d^2\,\Delta f$, und $U_r$ ist $d\sqrt{\Delta f}$.

**Verstärken ändert das SNR nicht.** Ein rauschfreier Verstärker mit dem Faktor $v$ macht aus $U_S$ und $U_r$ die Werte $vU_S$ und $vU_r$; im Verhältnis der
Quadrate kürzt sich $v^2$. Rauscht er selbst, kommt im Nenner noch sein Anteil hinzu. Im Bild: Wer nur die langsamen Bewegungen der Waage beachtet, sieht viel
weniger Zittern; wer sie vergrößert betrachtet, sieht das Zittern ebenso vergrößert.
:::

::::beispiel Rauschen in einem Band
Ein Verstärker habe am Eingang eine konstante Rauschdichte und lasse Frequenzen bis $100\,\text{kHz}$ durch:

$$|u_r(f)| = 10\,\frac{\text{nV}}{\sqrt{\text{Hz}}}, \qquad \Delta f = 100\,\text{kHz}.$$

**Der Effektivwert.**

$$U_r = 10\,\frac{\text{nV}}{\sqrt{\text{Hz}}}\cdot\sqrt{10^5\,\text{Hz}} = 3{,}16\,\mu\text{V}.$$

**Ein Signal von $1\,\text{mV}$** ragt heraus mit

$$\text{SNR} = \Big(\frac{1\,\text{mV}}{3{,}16\,\mu\text{V}}\Big)^2 = 10^5.$$

**Schmaleres Band.** Braucht das Signal nur $10\,\text{kHz}$ und begrenzt man das Band darauf, sinkt das Rauschen auf $1\,\mu\text{V}$, und das SNR steigt auf
$10^6$. Ein Zehntel der Bandbreite gibt ein Zehntel der Rauschleistung.

**Im Bild:** Wer nur auf die langsamen Schwankungen der Waage achtet, sieht ein Zehntel der Zitterenergie.
::::

## Vier Quellen des Rauschens

Das Skript nennt vier Arten von Rauschen.

**Thermisches Rauschen.** In jedem Leiter bewegen sich die Ladungsträger durch die Wärme ungeordnet, wie bei der Brownschen Bewegung. Zufällig sammeln sich an
einem Ende eines Widerstands kurz mehr Elektronen als am anderen, und an den Klemmen erscheint eine schwankende Spannung, auch wenn kein Strom fließt. Ihre
Dichte ist nach Gleichung 12.2, mit der Boltzmann-Konstante $k_B$, im Skript $k$, und der absoluten Temperatur $T$:

:::formel Gesetz
$$|u_{r,R}(f)|^2 = 4\,k_B\,T\,R.$$
:::

**So liest man das:** Eingaben sind Temperatur und Widerstand, Ausgabe die Dichte in $\text{V}^2/\text{Hz}$. Proportional zu $T$ und $R$ ist die Dichte; die
Spannung wächst nur mit der Wurzel. Die Frequenz kommt nicht vor: Das thermische Rauschen ist bis zu sehr hohen Frequenzen gleichmäßig verteilt, bei
Raumtemperatur bis in den Terahertzbereich. Ein Widerstand von $1\,\text{k}\Omega$ rauscht mit gut $4\,\text{nV}/\sqrt{\text{Hz}}$. Die Boltzmann-Konstante
verknüpft Temperatur und Energie; $k_BT$ ist das Maß der mittleren Wärmeenergie, die auf jede Bewegungsmöglichkeit eines Teilchens entfällt.

**Im Bild:** Die Waage zittert umso stärker, je wärmer sie ist; ein großer Widerstand ist dabei wie eine besonders weiche, leicht bewegliche Waage.

:::herleitung
Die vollständige Herleitung stammt von Harry Nyquist (1928) und geht über diesen Kurs hinaus; die Idee ist kurz. Ein Widerstand im Wärmegleichgewicht gibt an
einen angeschlossenen, gleich großen Widerstand in jedem Hertz Bandbreite im Mittel die Leistung $k_BT$ ab; das folgt aus der Gleichverteilung der Wärmeenergie
auf die Schwingungen, die zwischen beiden hin- und herlaufen. Nach dem Artikel über Leistungsanpassung erhält eine angepasste Last von einer Quelle mit der
Leerlaufspannung $U$ und dem Innenwiderstand $R$ die Leistung $U^2/(4R)$. Setzt man beides je Hertz gleich, ergibt sich

$$\frac{|u_{r,R}(f)|^2}{4\,R} = k_B\,T, \qquad |u_{r,R}(f)|^2 = 4\,k_B\,T\,R.$$

Im Bild: Zwei gleiche Waagen, die sich über eine Feder gegenseitig anstoßen, tauschen im Mittel gleich viel Zitterenergie aus.
:::

**Weißes Rauschen.** So heißt Rauschen mit konstanter Dichte über alle Frequenzen. Nach Formel (1) wäre seine Gesamtleistung unendlich, wie das Skript
bemerkt; es ist deshalb eine Idealisierung, und weiß ist echtes Rauschen nur in einem begrenzten Band. Anders als die drei übrigen ist es auch keine eigene
Ursache, sondern eine Form des Spektrums: Thermisches Rauschen und Schrotrauschen sind in sehr guter Näherung weiß.

**Schrotrauschen.** Muss ein Strom eine Potentialbarriere überwinden, wie am pn-Übergang einer Diode oder eines Transistors, besteht er aus einzelnen
Ladungsträgern, die unabhängig voneinander hinüberspringen. Ihre Zahl schwankt von Augenblick zu Augenblick, und mit ihr der Strom. Die Dichte dieser
Stromschwankung, die das Skript nicht angibt, ist nach Walter Schottky, mit der Elementarladung $e$ und dem Gleichstrom $I$:

$$|i_r(f)|^2 = 2\,e\,I.$$

**1/f-Rauschen.** Seine Dichte ist umgekehrt proportional zur Frequenz, sie hat also die Form $c/f$ mit einer Konstante $c$. Ursachen sind nach dem Skript etwa
schwankende Umladungen von Zuständen an Oberflächen und Schwankungen der Zahl freier Ladungsträger in Halbleitern. Bei tiefen Frequenzen, je nach Bauteil bis
in den Bereich von $10\,\text{kHz}$, überwiegt es das weiße Rauschen. Jede Dekade trägt gleich viel bei:

$$\int_{f_1}^{10 f_1} \frac{c}{f}\,df = c\,\ln10.$$

**Im Bild:** Thermisches Rauschen ist das Zittern durch die Wärme, Schrotrauschen das Prasseln einzelner Körner, die auf die Schale fallen, und 1/f-Rauschen ein
langsames Kriechen, das man umso stärker spürt, je länger man hinsieht.

:::herleitung
**Schrotrauschen, die Idee.** In einer Zeit $\tau$ springen im Mittel $N$ gleich $I\tau/e$ Ladungsträger über die Barriere. Für unabhängige, seltene Ereignisse
ist die Schwankung ihrer Anzahl so groß wie die Wurzel des Mittelwerts, nach der Poisson-Statistik; ihr mittleres Quadrat ist also $N$. Der über $\tau$
gemittelte Strom ist $eN/\tau$, sein Schwankungsquadrat

$$\Big(\frac{e}{\tau}\Big)^2 N = \frac{e\,I}{\tau}.$$

Eine Mittelung über $\tau$ lässt Frequenzen bis etwa $1/(2\tau)$ durch; mit dieser Bandbreite $\Delta f$ ist das gleich $2eI\,\Delta f$, also die Dichte $2eI$.

**1/f-Rauschen.** Die Stammfunktion von $1/f$ ist $\ln f$, und $\ln(10 f_1) - \ln f_1$ ist $\ln 10$, unabhängig von $f_1$. Im Bild: Das Kriechen hat in jeder
Zeitskala, Sekunden, Minuten, Stunden, gleich viel zu bieten.
:::

::::beispiel Rauschen von Widerständen und Strömen
**(a) Thermisches Rauschen bei $300\,\text{K}$** über ein Audioband von $20\,\text{kHz}$:

| $R$ | Dichte | Effektivwert über $20\,\text{kHz}$ |
|---|---|---|
| $1\,\text{k}\Omega$ | $4{,}07\,\text{nV}/\sqrt{\text{Hz}}$ | $0{,}58\,\mu\text{V}$ |
| $100\,\text{k}\Omega$ | $40{,}7\,\text{nV}/\sqrt{\text{Hz}}$ | $5{,}8\,\mu\text{V}$ |
| $1\,\text{M}\Omega$ | $129\,\text{nV}/\sqrt{\text{Hz}}$ | $18{,}2\,\mu\text{V}$ |

Für die erste Zeile:

$$\sqrt{4\cdot1{,}381\cdot10^{-23}\,\frac{\text{J}}{\text{K}}\cdot300\,\text{K}\cdot1\,\text{k}\Omega} = 4{,}07\,\frac{\text{nV}}{\sqrt{\text{Hz}}}.$$

Kühlt man den Widerstand mit flüssigem Stickstoff auf $77\,\text{K}$, sinkt das Rauschen auf die Hälfte, um den Faktor $\sqrt{77/300}$.

**(b) Schrotrauschen** eines Diodenstroms von $1\,\text{mA}$:

$$\sqrt{2\cdot1{,}602\cdot10^{-19}\,\text{C}\cdot1\,\text{mA}} = 17{,}9\,\frac{\text{pA}}{\sqrt{\text{Hz}}}.$$

Über $20\,\text{kHz}$ sind das $2{,}5\,\text{nA}$, ein Vierhunderttausendstel des Stroms.

**(c) 1/f-Rauschen.** Zwischen $1$ und $10\,\text{Hz}$ liegt ebenso viel davon wie zwischen $1$ und $10\,\text{kHz}$, je $c\ln10$; wer lange misst, sammelt immer
mehr davon ein.

**Im Bild:** Ein großer Widerstand ist eine weichere Waage und zittert stärker; ein Strom aus vielen Körnern prasselt kaum hörbar.
::::

## Der Differenzverstärker

Ein __Differenzverstärker__ ist nach Abschnitt 12.2 des Skripts eine Schaltung mit zwei Eingängen, die den Unterschied der beiden Eingangsspannungen $U_{e1}$
und $U_{e2}$ verstärkt; er ist der Grundbestandteil jedes Operationsverstärkers. Jedes Paar von Eingangsspannungen lässt sich in einen gemeinsamen Anteil, die
__Gleichtaktspannung__ $U_{gl}$, und den Unterschied, die __Differenzspannung__ $U_D$, zerlegen:

$$U_{gl} = \frac{U_{e1} + U_{e2}}{2}, \qquad U_D = U_{e1} - U_{e2}.$$

Ein idealer Differenzverstärker antwortet nur auf den Unterschied, nach Gleichung 12.3 mit einem Verstärkungsfaktor $v$, den das Skript mit etwa $10000$ angibt:

:::formel Definition
$$U_A = v\,\big(U_{e1} - U_{e2}\big) = v\,U_D.$$
:::

**So liest man das:** Eingaben sind zwei Spannungen, Ausgabe eine; die Gleichtaktspannung kommt nicht vor. Liegt an beiden Eingängen dieselbe Spannung, ist der
Ausgang null, und wie groß die Eingangsspannungen selbst sind, spielt keine Rolle. Das nutzt man, wie das Skript beschreibt, gegen Störungen: Ein Signal reist
oft auf einer Gleichspannung, die selbst verrauscht ist. Gibt man beiden Eingängen dieselbe Gleichspannung mit ihrem Rauschen und nur einem zusätzlich das
Nutzsignal, steht am Ausgang allein das verstärkte Nutzsignal. Hier verbessert der Verstärker das SNR wirklich, weil er eine Störung entfernt, statt sie
mitzuverstärken.

**Im Bild:** Ein gleiches Zusatzgewicht auf beiden Schalen und ein Rütteln am Tisch neigen den Balken nicht; nur ein Unterschied der Gewichte bewegt ihn.

:::herleitung
Die Zerlegung ist umkehrbar: Addiert man die Hälfte der Differenzspannung zur Gleichtaktspannung oder zieht sie ab, erhält man die beiden Eingänge zurück,

$$U_{e1} = U_{gl} + \frac{U_D}{2}, \qquad U_{e2} = U_{gl} - \frac{U_D}{2}.$$

Jedes Paar von Eingangsspannungen ist also genau ein Paar aus Gleichtakt- und Differenzspannung, und Formel (3) sagt, dass der ideale Verstärker von diesem
Paar nur die zweite Zahl beachtet. Im Bild: Jede Beladung der Waage ist ein gleicher Grundanteil auf beiden Schalen plus ein Unterschied.
:::

::::beispiel Eine Störung, die beide Leitungen trifft
Ein Sensor liefert sein Signal von $1\,\text{mV}$ auf einer Gleichspannung von $2{,}5\,\text{V}$; auf beiden Leitungen liegt zusätzlich dieselbe Störung von
$50\,\text{mV}$:

$$U_{e1} = 2{,}5\,\text{V} + 50\,\text{mV} + 1\,\text{mV}, \qquad U_{e2} = 2{,}5\,\text{V} + 50\,\text{mV}, \qquad v = 10^4.$$

**Zerlegt.** Die Differenzspannung ist $1\,\text{mV}$, die Gleichtaktspannung $2{,}5505\,\text{V}$. Der ideale Differenzverstärker liefert

$$U_A = 10^4\cdot1\,\text{mV} = 10\,\text{V}.$$

Die Störung ist verschwunden, das Signal zehntausendfach verstärkt.

**Zum Vergleich.** Ein Verstärker mit einem einzigen Eingang und derselben Verstärkung würde die $50\,\text{mV}$ Störung zu $500\,\text{V}$ vergrößern wollen und
läge längst am Anschlag.

**Im Bild:** Fünfzig Gramm Sand auf beiden Schalen, ein Gramm mehr auf einer; die Waage zeigt nur das eine Gramm.
::::

Wie man einen Differenzverstärker aus Transistoren baut, zeigt Bild 12.1. Zwei gleiche npn-Transistoren Q1 und Q2 bilden zwei symmetrische Emitterschaltungen,
mit je einem Kollektorwiderstand $R_C$ an $U_{CC}$; ihre Emitter sind verbunden und führen zum Kollektor eines dritten Transistors Q3, dessen Basis an einer
festen Spannung $U_\text{bias}$ liegt. Q3 arbeitet als Stromquelle und hält den Summenstrom $I_{Q3}$ fest, so wie es auch ein Stromspiegel könnte. Die Eingänge
sind die Basen von Q1 und Q2, der Ausgang die Spannung zwischen den Kollektoren, $U_A$ gleich $U_{a1} - U_{a2}$. Die Basisströme vernachlässigt man, wie das
Skript. Bei gleichen Eingängen teilt sich der Strom aus Symmetrie gleich auf, Gleichung 12.4, und $U_A$ ist null. Mit der Steilheit $S$ jedes Transistors, im
vorigen Artikel $g_m$ genannt, ergibt sich für kleine Differenzspannungen:

:::formel
$$I_{Q1} = I_{Q2} = \frac{I_{Q3}}{2}, \qquad U_A = -S\,R_C\,\big(U_{e1} - U_{e2}\big), \qquad S = \frac{I_{Q3}}{2\,U_T}.$$
:::

**So liest man das:** Steigt $U_{e1}$, sinkt $U_A$; $U_{e1}$ ist also der invertierende Eingang und $U_{e2}$ der nichtinvertierende, wie das Skript in
Abschnitt 12.3 sagt. Der Betrag der Verstärkung, $SR_C$, ist $I_{Q1}R_C/U_T$, die Gleichspannung an einem Kollektorwiderstand geteilt durch $U_T$, genau wie bei
der Emitterschaltung im vorigen Artikel.

Das Skript erhält dagegen $-2SR$. Es setzt die ganze Signalspannung an die Basis-Emitter-Strecke von Q1. Weil Q3 aber die Summe beider Ströme festhält, folgt das
gemeinsame Emitterpotenzial dem Signal um die Hälfte: Die eine Hälfte erhöht $U_{BE1}$, die andere senkt $U_{BE2}$. Damit wächst $I_{Q1}$ nur um $Su_{e,s}/2$,
und die Verstärkung ist halb so groß. Auch die Größenordnung $10000$, die das Skript nennt, erreicht eine Stufe mit Widerständen nicht; dafür müssten an $R_C$
rund $260\,\text{V}$ liegen. In echten Operationsverstärkern bilden Stromspiegel die Last, die mit ihrem großen Ausgangswiderstand $r_{CE}$ wirken; so kommt eine
Stufe auf etwa tausend und mehr, und mehrere Stufen hintereinander ergeben die $10^5$ bis $10^6$ des ganzen Operationsverstärkers, wie das Skript sagt.

Warum nur der Unterschied zählt, zeigt die Schaltung selbst: Steigen beide Eingänge um dasselbe, steigt das Emitterpotenzial genauso mit, die beiden
Basis-Emitter-Spannungen bleiben gleich, und kein Strom ändert sich. Und für große Differenzspannungen gilt die Kennlinie

$$I_{Q1} - I_{Q2} = I_{Q3}\,\tanh\frac{U_{e1} - U_{e2}}{2\,U_T}.$$

Linear ist sie nur für Differenzen deutlich unter $2U_T$, etwa bis $10\,\text{mV}$; darüber flacht sie ab, und der Ausgang erreicht höchstens $R_CI_{Q3}$.

**Im Bild:** Der Balken verteilt eine feste Summe: Was die eine Schale nach unten gewinnt, verliert die andere. Hebt man beide Schalen gleich an, bleibt er
waagrecht.

:::herleitung
**Gleichgewicht.** Bei gleichen Eingängen und gleichen Transistoren sind beide Basis-Emitter-Spannungen gleich und damit nach der Transfergleichung beide Ströme;
zusammen ergeben sie $I_{Q3}$.

**Das Signal teilt sich.** Q3 hält die Summe fest, also ändern sich die beiden Ströme gegengleich. Jeder ändert sich um $S$ mal die Änderung seiner
Basis-Emitter-Spannung, also ändern sich auch diese gegengleich. Ihre Differenz ist der Unterschied der Basisspannungen, weil die Emitter verbunden sind:

$$\Delta U_{BE1} - \Delta U_{BE2} = u_{e,s}, \qquad \Delta U_{BE1} = -\Delta U_{BE2} = \frac{u_{e,s}}{2}, \qquad \Delta I_{Q1} = \frac{S\,u_{e,s}}{2}.$$

**Der Ausgang.** Wie im Skript ist an den Kollektoren

$$U_{a1} = U_{CC} - R_C\,\big(I_{Q1} + \Delta I_{Q1}\big), \qquad U_{a2} = U_{CC} - R_C\,\big(I_{Q2} - \Delta I_{Q1}\big),$$

und mit gleichen Ruheströmen ist $U_A$ gleich $-2R_C\Delta I_{Q1}$, also $-SR_Cu_{e,s}$. Bis hierhin stimmt die Rechnung des Skripts; nur $\Delta I_{Q1}$ ist dort
doppelt so groß angesetzt.

**Gleichtakt.** Steigen beide Basen um $\Delta U$, muss der Emitter ebenso steigen, damit die Ströme ihre Summe behalten und gleich bleiben; dann ändert sich
nichts.

**Großsignal.** Nach der Transfergleichung ist das Verhältnis der Ströme die Exponentialfunktion des Unterschieds der Basis-Emitter-Spannungen, und dieser ist
$U_{e1} - U_{e2}$. Mit der Summe $I_{Q3}$:

$$\frac{I_{Q1}}{I_{Q2}} = \exp\frac{U_{e1} - U_{e2}}{U_T}, \qquad I_{Q1} = \frac{I_{Q3}}{1 + \exp\big(-(U_{e1} - U_{e2})/U_T\big)}.$$

Die Differenz der beiden Ströme ist dann $I_{Q3}$ mal $(e^x - 1)/(e^x + 1)$ mit $x$ gleich $(U_{e1} - U_{e2})/U_T$, und das ist $\tanh(x/2)$. Ihre Steigung bei
null ist $I_{Q3}/(2U_T)$, also $S$; das ist wieder das Kleinsignalergebnis. Im Bild: Ein Balken, der weit ausschlägt, legt schließlich das ganze Gewicht auf eine
Seite.
:::

::::beispiel Ein Differenzverstärker aus Transistoren
Die Schaltung von Bild 12.1 mit eigenen Werten:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 10\,\text{k}\Omega, \qquad I_{Q3} = 1\,\text{mA}.$$

**Ruhe.** Jeder Transistor führt $0{,}5\,\text{mA}$, an jedem $R_C$ fallen $5\,\text{V}$ ab, beide Kollektoren liegen bei $7\,\text{V}$, und $U_A$ ist null.

**Kleines Signal.** Die Steilheit ist

$$S = \frac{0{,}5\,\text{mA}}{25{,}85\,\text{mV}} = 19{,}3\,\text{mS}, \qquad A = -S\,R_C = -193.$$

Ein Millivolt an $U_{e1}$ teilt sich auf beide Transistoren auf; $I_{Q1}$ wächst um $9{,}7\,\mu\text{A}$, $I_{Q2}$ sinkt ebenso, und $U_A$ wird
$-193\,\text{mV}$. Die Formel des Skripts gäbe $-387$.

**Große Signale,** nach der Kennlinie und linear gerechnet:

| $U_{e1} - U_{e2}$ | $U_A$ nach Kennlinie | $U_A$ linear |
|---|---|---|
| $10\,\text{mV}$ | $-1{,}91\,\text{V}$ | $-1{,}93\,\text{V}$ |
| $26\,\text{mV}$ | $-4{,}64\,\text{V}$ | $-5{,}03\,\text{V}$ |
| $52\,\text{mV}$ | $-7{,}64\,\text{V}$ | $-10{,}06\,\text{V}$ |
| $100\,\text{mV}$ | $-9{,}59\,\text{V}$ | $-19{,}3\,\text{V}$ |

Bei großen Differenzen nähert sich $U_A$ der Grenze $-R_CI_{Q3}$, $-10\,\text{V}$: Dann fließt fast der ganze Strom durch Q1.

**Mit Stromspiegeln als Last** und einem Ausgangswiderstand von $200\,\text{k}\Omega$ je Transistor käme dieselbe Stufe auf eine Verstärkung um $1900$.

**Im Bild:** Ein Milligramm Unterschied neigt den Balken; bei hundert Milligramm liegt fast alles auf einer Seite.
::::

## Der ideale Operationsverstärker

Dem Differenzverstärker folgen im OPV weitere Verstärkerstufen, und die Vorlesung betrachtet von da an nur noch die äußere Beschaltung, nicht den inneren
Aufbau. Das Schaltsymbol, Bild 12.2 des Skripts, ist ein Dreieck mit zwei Eingängen und einem Ausgang an der Spitze. Der mit Plus bezeichnete Eingang ist der
__nichtinvertierende Eingang__ mit der Spannung $U_{e+}$, der mit Minus der __invertierende Eingang__ mit $U_{e-}$; beide Spannungen zählen gegen Masse. Dazu
kommen die Anschlüsse der Versorgung, $U_{B+}$ und $U_{B-}$, die man in Schaltbildern oft weglässt. Der OPV verstärkt die Differenzspannung zwischen den
Eingängen mit der __Differenzverstärkung__ $v_D$, auch __Leerlaufverstärkung__, weil kein Ausgang zurückgeführt ist:

:::formel Definition
$$U_D = U_{e+} - U_{e-}, \qquad U_A = v_D\,U_D.$$
:::

**So liest man das:** Eingabe ist die Differenz der Eingänge, Ausgabe die Ausgangsspannung gegen Masse. Steigt $U_{e+}$, steigt $U_A$; steigt $U_{e-}$, sinkt
$U_A$, daher die Namen. Der __ideale Operationsverstärker__ hat nach dem Skript vier Eigenschaften, jede mit einer Folge:

1. Sein **Eingangswiderstand** ist unendlich; in die Eingänge fließt kein Strom.
2. Seine **Verstärkung** $v_D$ ist unendlich und hängt nicht von der Frequenz ab; mit Gegenkopplung wird $U_D$ deshalb zu null geregelt, wie der Abschnitt über
   Rückkopplung zeigt.
3. Sein **Ausgangswiderstand** ist null; er liefert jeden Strom, den die Schaltung verlangt, und der Ausgangsstrom stellt sich so ein, dass alle Knoten- und
   Maschengleichungen erfüllt sind.
4. Er **rauscht** nicht. Als Differenzverstärker antwortet er außerdem nur auf $U_D$, nicht auf die Gleichtaktspannung.

Ein realer OPV hat eine endliche Verstärkung, typisch $10^5$ bis $10^6$, und seine Ausgangsspannung kann nur zwischen $U_{A,\min}$ und $U_{A,\max}$ liegen,
etwas innerhalb der Versorgung; darüber hinaus geht er in die Sättigung. Dazu kommen nach dem Skript Streuung, Temperaturabhängigkeit und eine Verstärkung, die
zu hohen Frequenzen sinkt, wie der Artikel über den realen OPV zeigt. Wie klein der Bereich ist, in dem ein OPV ohne Rückkopplung linear arbeitet, zeigt die
Grenze der Ausgangsspannung:

$$|U_D| \le \frac{U_{A,\max}}{v_D}.$$

**Im Bild:** Die Schalen sind so leicht zu bewegen, dass das Auflegen nichts kostet; der Motor ist unendlich stark; und der Zeiger lässt sich durch nichts
aufhalten außer durch die Anschläge.

:::herleitung
Im linearen Bereich ist $U_A$ gleich $v_DU_D$, und $|U_A|$ kann höchstens $U_{A,\max}$ sein; geteilt durch $v_D$ folgt die Grenze. Für eine negative Grenze
$U_{A,\min}$ gilt dasselbe mit ihr. Im Bild: Der Motor bringt den Zeiger schon bei einer Neigung an den Anschlag, die man mit bloßem Auge nicht sieht.
:::

::::beispiel Wie klein der lineare Bereich ist
Ein OPV an $\pm15\,\text{V}$, dessen Ausgang bis $\pm13\,\text{V}$ reicht:

| $v_D$ | $10^5$ | $2\cdot10^5$ | $10^6$ |
|---|---|---|---|
| größte lineare $U_D$ | $130\,\mu\text{V}$ | $65\,\mu\text{V}$ | $13\,\mu\text{V}$ |

Zum Beispiel:

$$|U_D| \le \frac{13\,\text{V}}{2\cdot10^5} = 65\,\mu\text{V}.$$

Schon das thermische Rauschen eines Widerstands von $1\,\text{M}\Omega$ über ein Audioband, $18\,\mu\text{V}$, nimmt davon einen merklichen Teil ein. Ohne
Rückkopplung liegt der Ausgang deshalb praktisch immer an einem Anschlag.

**Im Bild:** Ein Hauch auf eine Schale, und der Zeiger schlägt an.
::::

## Der Komparator

Die einfachste Schaltung mit einem OPV ist der __Komparator__, Bild 12.3, ein Vergleicher ohne jede Rückkopplung. Die Spannung $U_1$ liegt am
nichtinvertierenden, $U_2$ am invertierenden Eingang, die Differenzspannung ist $U_1 - U_2$. Weil $v_D$ unendlich ist und der Ausgang begrenzt, liegt der Ausgang
immer an einer der beiden Grenzen:

:::formel
$$U_A = \begin{cases} U_{A,\max}, & U_1 > U_2, \\ U_{A,\min}, & U_1 < U_2. \end{cases}$$
:::

**So liest man das:** Eingaben sind zwei Spannungen, Ausgabe eine von zwei Spannungen, die anzeigt, welche größer ist. Die Kennlinie von Bild 12.4 springt bei
$U_1$ gleich $U_2$. Ideal lägen die Grenzen bei den Versorgungsspannungen; ein realer OPV erreicht nach dem Skript nur $U_{A,\max}$ unter $U_{B+}$ und
$U_{A,\min}$ über $U_{B-}$, weil zwischen dem Ausgang und jedem Versorgungsanschluss Halbleiterbauelemente liegen, an denen eine Spannung abfällt, ähnlich der
Sättigungsspannung eines Transistors. Im Satz des Skripts, für $U_D \ne 0$ stelle sich $U_{B+}$ bzw. $U_{B+}$ ein, ist das zweite $U_{B+}$ ein Druckfehler für
$U_{B-}$.

**Im Bild:** Eine Waage ohne Rückmeldung zeigt nur, welche Schale schwerer ist, und zwar immer mit vollem Ausschlag.

:::herleitung
Nach Formel (5) ist $U_A$ gleich $v_D(U_1 - U_2)$, solange das zwischen den Grenzen liegt. Ist $U_1 - U_2$ größer als $U_{A,\max}/v_D$, verlangte die Formel mehr,
als der Ausgang hergibt, und er bleibt an der oberen Grenze; entsprechend unten. Mit $v_D$ gegen unendlich schrumpft der Bereich dazwischen auf den Punkt
$U_1$ gleich $U_2$. Im Bild: Je stärker der Motor, desto kleiner die Neigung, die schon zum Anschlag reicht.
:::

Eine Anwendung zeigt Bild 12.5 des Skripts, den __Flash-Wandler__, einen schnellen Analog-Digital-Wandler. Ein Spannungsteiler aus gleichen Widerständen an
einer Referenzspannung erzeugt eine Reihe von Schwellen; an jeder liegt der invertierende Eingang eines Komparators, und die Eingangsspannung liegt an allen
nichtinvertierenden Eingängen zugleich. Jeder Komparator, dessen Schwelle die Eingangsspannung übersteigt, meldet eine Eins. Wie viele Einsen es sind, sagt, in
welchem Bereich die Eingangsspannung liegt; man nennt dieses Muster einen Thermometercode, weil die Einsen von unten aufsteigen. Für $n$ Bit braucht man
$2^n$ Bereiche und damit $2^n - 1$ Schwellen und Komparatoren. Weil alle zugleich vergleichen, ist der Wandler sehr schnell, aber teuer an Komparatoren.

::::beispiel Ein Flash-Wandler mit 2 Bit
Vier gleiche Widerstände an $4\,\text{V}$ ergeben Schwellen bei $3$, $2$ und $1\,\text{V}$ für die Komparatoren K1, K2 und K3. Eine Eins steht für $U_{A,\max}$:

| $U_E$ | K1 an $3\,\text{V}$ | K2 an $2\,\text{V}$ | K3 an $1\,\text{V}$ | Einsen | Zahl |
|---|---|---|---|---|---|
| $0{,}4\,\text{V}$ | $0$ | $0$ | $0$ | $0$ | $00$ |
| $1{,}7\,\text{V}$ | $0$ | $0$ | $1$ | $1$ | $01$ |
| $2{,}9\,\text{V}$ | $0$ | $1$ | $1$ | $2$ | $10$ |
| $3{,}6\,\text{V}$ | $1$ | $1$ | $1$ | $3$ | $11$ |

Die Schwellen folgen aus der Spannungsteilerregel, zum Beispiel die oberste:

$$U_{K1} = 4\,\text{V}\cdot\frac{3R}{4R} = 3\,\text{V}.$$

Für $8$ Bit wären es $255$ Komparatoren.

**Im Bild:** Drei Waagen mit verschieden schweren Gegengewichten; wie viele davon kippen, verrät das Gewicht auf ein Viertel genau.
::::

## Rückkopplung: Gegen- und Mitkopplung

Beim Komparator führt nichts vom Ausgang zurück. Abschnitt 12.4 des Skripts untersucht Schaltungen mit einer solchen Verbindung. __Rückkopplung__, englisch
feedback, heißt ein Mechanismus, bei dem ein Teil der Ausgangsgröße direkt oder verändert auf den Eingang zurückgeführt wird; in der Systemtheorie ist der
Begriff zentral. Führt man den Ausgang auf den invertierenden Eingang zurück, wirkt die Rückführung jeder Änderung entgegen, und man spricht von
__Gegenkopplung__, einer negativen oder gegenphasigen Rückführung. Führt man ihn auf den nichtinvertierenden Eingang, verstärkt sie die Änderung: __Mitkopplung__,
positiv oder phasenrichtig. Grob gesagt, so das Skript, dämpft die Gegenkopplung und verstärkt die Mitkopplung.

Was die Gegenkopplung leistet, zeigt die einfachste Anordnung. Das Eingangssignal $U_E$ liegt am nichtinvertierenden Eingang, und ein Spannungsteiler führt den
Anteil $k$ der Ausgangsspannung, eine Zahl zwischen null und eins, auf den invertierenden Eingang zurück. Mit endlicher Verstärkung $v_D$ gilt dann:

:::formel Satz
$$U_A = \frac{v_D}{1 + k\,v_D}\,U_E \approx \frac{U_E}{k}, \qquad U_D = \frac{U_E}{1 + k\,v_D}.$$
:::

**So liest man das:** Eingaben sind $U_E$, $k$ und $v_D$; Ausgaben die Ausgangs- und die Differenzspannung. Ist $kv_D$ groß gegen eins, wie fast immer bei
$v_D$ um $10^5$, hängt die Verstärkung der ganzen Schaltung, $U_A/U_E$, nur noch von $k$ ab, also von zwei Widerständen; ob $v_D$ nun $10^5$ oder $10^6$ beträgt,
ändert fast nichts. Und die Differenzspannung wird winzig: Der OPV stellt seinen Ausgang so ein, dass seine Eingänge fast dieselbe Spannung haben, und für den
idealen OPV wird $U_D$ genau null. Das ist der Satz des Skripts, bei Gegenkopplung werde $U_D$ zu null geregelt.

Daraus folgen die beiden Regeln, mit denen der nächste Artikel alle Grundschaltungen berechnet, oft die __goldenen Regeln__ genannt. Erstens fließt in die
Eingänge kein Strom; das ist die erste Eigenschaft des idealen OPV und gilt immer. Zweitens liegen bei Gegenkopplung beide Eingänge auf demselben Potenzial, der
__virtuelle Kurzschluss__; liegt einer davon an Masse, heißt der andere __virtuelle Masse__. Virtuell ist der Kurzschluss, weil zwischen den Eingängen kein
Strom fließt: Der OPV erzwingt die Gleichheit, indem er seinen Ausgang nachführt, nicht durch eine Verbindung. Die zweite Regel gilt nur bei Gegenkopplung.

**Im Bild:** Der Motor schiebt das Gegengewicht, bis der Balken waagrecht steht. Wo das Gegengewicht dann sitzt, verrät das Gewicht; ein stärkerer Motor ändert
daran nichts, er stellt nur noch genauer ein.

:::herleitung
**Die Masche am Eingang.** Am nichtinvertierenden Eingang liegt $U_E$, am invertierenden $kU_A$; die Differenzspannung ist also $U_E - kU_A$.

**Einsetzen.** Mit $U_A$ gleich $v_DU_D$:

$$U_A = v_D\,\big(U_E - k\,U_A\big), \qquad U_A\,\big(1 + k\,v_D\big) = v_D\,U_E.$$

Nach $U_A$ aufgelöst ergibt sich der erste Ausdruck, und $U_D$ ist $U_A/v_D$.

**Die Näherung.** Man teilt Zähler und Nenner durch $kv_D$; im Nenner steht dann $1 + 1/(kv_D)$, fast eins. Im Bild: Der Motor kann so stark sein, wie er will,
der Balken kommt dort zur Ruhe, wo das Gegengewicht das Gewicht ausgleicht.
:::

Bleibt eine Frage, die das Skript mit Rechenzyklen beantwortet: Kommt die Schaltung überhaupt zur Ruhe? Formel (7) beschreibt nur den Zustand, in dem sich
nichts mehr ändert. Rechnet man in Zyklen, in denen der OPV jeweils $U_A$ gleich $v_DU_D$ setzt, wächst bei Mitkopplung jede Abweichung, wie das Skript zeigt.
Bei Gegenkopplung aber würde dieselbe Zyklusrechnung jede Abweichung mit $-kv_D$ multiplizieren, also mit Tausenden und wechselndem Vorzeichen, und ebenfalls
aufschwingen. Zur Ruhe kommt eine echte Schaltung, weil ihr Ausgang nicht springen kann. Ein einfaches, für viele OPV gutes Modell ist, dass sich die
Ausgangsspannung umso schneller ändert, je größer $U_D$ ist, mit einer Konstante $\omega_T$, die der Artikel über den realen OPV als Transitkreisfrequenz
einführt:

$$\frac{dU_A}{dt} = \omega_T\,U_D.$$

Mit Gegenkopplung nähert sich der Ausgang dann dem Ruhewert exponentiell, wie die Spannung beim Laden eines Kondensators; mit Mitkopplung entfernt er sich
exponentiell, bis er an einen Anschlag stößt. Mit der Zeitkonstante $\tau$ gleich $1/(k\omega_T)$:

$$\text{Gegenkopplung:} \quad U_A(t) = \frac{U_E}{k} + \Big(U_A(0) - \frac{U_E}{k}\Big)\,e^{-t/\tau}, \qquad \text{Mitkopplung:} \quad \propto e^{+t/\tau}.$$

**Im Bild:** Ein Motor, der das Gegengewicht ruckartig um riesige Strecken versetzte, würde ewig hin- und herschlagen; ein Motor, der umso schneller schiebt, je
schiefer der Balken steht, bringt ihn sanft in die Waagrechte.

:::herleitung
**Gegenkopplung.** Mit $U_D$ gleich $U_E - kU_A$ wird das Modell zu einer linearen Differentialgleichung erster Ordnung. Für die Abweichung $x$ vom Ruhewert,
$x$ gleich $U_A - U_E/k$, lautet sie

$$\frac{dx}{dt} = -k\,\omega_T\,x, \qquad x(t) = x(0)\,e^{-t/\tau}.$$

Das ist dieselbe Gleichung wie beim Entladen eines Kondensators über einen Widerstand; die Abweichung klingt ab.

**Mitkopplung.** Liegt das Signal am invertierenden Eingang und die Rückführung am nichtinvertierenden, ist $U_D$ gleich $kU_A - U_E$, und das Vorzeichen kehrt
sich um: $dx/dt$ ist $+k\omega_Tx$, und jede Abweichung wächst mit $e^{t/\tau}$.

**Die Zyklen.** Setzt man jeweils sofort $U_A$ gleich $v_D(U_E - kU_A)$, wird eine Abweichung $x$ zu $-kv_Dx$; bei $kv_D$ größer als eins wächst ihr Betrag. Im
Bild: Wer bei jedem Blick auf die Waage das Gegengewicht um das Tausendfache der Neigung versetzt, überschießt jedes Mal.
:::

::::beispiel Gegenkopplung in Zahlen
Ein OPV mit Rückführung des Anteils $k$ gleich $0{,}1$, also einer Verstärkung um $10$:

| $v_D$ | $U_A/U_E$ | $U_D$ bei $U_E = 1\,\text{V}$ |
|---|---|---|
| $10^5$ | $9{,}9990$ | $100\,\mu\text{V}$ |
| $10^6$ | $9{,}9999$ | $10\,\mu\text{V}$ |

Zum Beispiel für die erste Zeile:

$$\frac{U_A}{U_E} = \frac{10^5}{1 + 0{,}1\cdot10^5} = 9{,}9990.$$

Eine Verzehnfachung von $v_D$ ändert die Verstärkung um ein Hunderttausendstel.

**Einschwingen.** Mit $\omega_T$ gleich $2\pi\cdot1\,\text{MHz}$, einem typischen Wert:

$$\tau = \frac{1}{0{,}1\cdot2\pi\cdot1\,\text{MHz}} = 1{,}6\,\mu\text{s}.$$

Nach fünf Zeitkonstanten, $8\,\mu\text{s}$, ist der Ruhewert bis auf $0{,}7\,\%$ erreicht. Bei Mitkopplung mit demselben $k$ wächst eine Abweichung von
$1\,\text{mV}$ in $\tau\ln(13\,\text{V}/1\,\text{mV})$, also $15\,\mu\text{s}$, bis an den Anschlag bei $13\,\text{V}$.

**Im Bild:** Ein zehnmal stärkerer Motor rückt das Gegengewicht um ein Hunderttausendstel genauer zurecht.
::::

:::grafik
Szene: get1/operationsverstaerker/01-gegenkopplung · Vorlage: opv-regelkreis
Links ein OPV mit $U_E$ am nichtinvertierenden Eingang und einem Spannungsteiler, der den Anteil $k = 0{,}1$ des Ausgangs auf den invertierenden Eingang
zurückführt; ein Umschalter vertauscht die Eingänge und macht daraus Mitkopplung. Rechts über der Zeit $U_A(t)$ nach einem Sprung von $U_E$ auf $1\,\text{V}$: bei
Gegenkopplung das exponentielle Einschwingen auf $10\,\text{V}$ mit $\tau = 1{,}6\,\mu\text{s}$, bei Mitkopplung das exponentielle Weglaufen bis zum Anschlag.
Ein dritter Modus zeigt die Zyklusrechnung mit sprunghaftem $U_A = v_D U_D$, deren Werte mit wechselndem Vorzeichen immer größer werden. Ein Regler für $v_D$ von
$10^3$ bis $10^6$ ändert den Endwert bei Gegenkopplung kaum. Kernaussage: Gegenkopplung bringt den Ausgang auf $U_E/k$, unabhängig von $v_D$, weil er sich nur
endlich schnell ändert. (Rot = Ausgang, blau = Eingang, orange = Rückführung, grau = Achsen, gestrichelt = Ruhewert.)
:::

## Der Schmitt-Trigger

Das Skript untersucht die Mitkopplung am __invertierenden Schmitt-Trigger__, Bild 12.6. Die Eingangsspannung $U_E$ liegt am invertierenden Eingang. Vom Ausgang
führt $R_2$ zum nichtinvertierenden Eingang und von dort $R_1$ nach Masse; am nichtinvertierenden Eingang liegt also der Anteil $k$ gleich $R_1/(R_1 + R_2)$ der
Ausgangsspannung, die Spannung $U_{R1}$ des Skripts, und die Differenzspannung ist $kU_A - U_E$.

Das Skript geht in drei Schritten vor. Bei $U_E$ gleich null fließt kein Strom, und $U_A$ gleich null ist ein Zustand ohne Änderung. Er ist aber, wie die
Mitkopplung im vorigen Abschnitt zeigt, instabil: Die kleinste Abweichung, etwa durch Rauschen, wächst, und in Wirklichkeit bleibt der Ausgang dort nicht stehen.
Wäre die Ausgangsspannung unbegrenzt, wüchse sie bei jedem $U_E$ ungleich null ohne Ende, und der Strom durch $R_1$ und $R_2$ würde die Bauteile zerstören. Mit
begrenztem Ausgang aber bleibt er an einem Anschlag, an $U_{A,\max}$ oder an $U_{A,\min}$, und dort hält ihn die Mitkopplung fest. Er wechselt erst, wenn $U_D$
das Vorzeichen wechselt, und das geschieht bei zwei verschiedenen Eingangsspannungen, der oberen Schwelle $U_{S,o}$ und der unteren $U_{S,u}$:

:::formel
$$U_{S,o} = k\,U_{A,\max}, \qquad U_{S,u} = k\,U_{A,\min}, \qquad k = \frac{R_1}{R_1 + R_2}.$$
:::

**So liest man das:** Eingaben sind die Grenzen des Ausgangs und die beiden Widerstände, Ausgaben die beiden Schaltschwellen; im Skript heißen sie
$U_{R1,\max}$ und $U_{R1,\min}$. Steigt die Eingangsspannung, springt der Ausgang erst bei $U_{S,o}$ nach unten; fällt sie, springt er erst bei $U_{S,u}$ zurück
nach oben. Dazwischen hängt der Ausgang von der Vorgeschichte ab, wie das Skript sagt; die Schaltung hat zwei stabile Zustände und merkt sich, in welchem sie
ist. Diese Eigenschaft heißt __Hysterese__, ihre Breite ist $k(U_{A,\max} - U_{A,\min})$. Nützlich ist das bei langsamen, verrauschten Signalen: Solange das
Rauschen kleiner ist als die Hysterese, schaltet der Ausgang bei jedem Durchgang genau einmal; ein einfacher Komparator schaltete dagegen an seiner einzigen
Schwelle so oft hin und her, wie das Rauschen sie überquert.

**Im Bild:** Hat der Motor das Gewicht auf die sinkende Seite geschoben, liegt die Waage fest; erst ein Gegengewicht, das auch das verschobene Gewicht
übertrifft, kippt sie zurück, und dann liegt sie auf der anderen Seite ebenso fest.

:::herleitung
**Der obere Zustand.** Bei $U_A$ gleich $U_{A,\max}$ ist $U_D$ gleich $kU_{A,\max} - U_E$. Positiv bleibt das, und damit der Ausgang oben, solange $U_E$ unter
$kU_{A,\max}$ liegt. Überschreitet $U_E$ diesen Wert, wird $U_D$ negativ, und der Ausgang läuft nach unten.

**Der untere Zustand.** Bei $U_A$ gleich $U_{A,\min}$ ist $U_D$ gleich $kU_{A,\min} - U_E$; negativ bleibt das, solange $U_E$ über $kU_{A,\min}$ liegt.
Unterschreitet $U_E$ diesen Wert, läuft der Ausgang nach oben.

**Der Sprung.** Sobald $U_D$ das Vorzeichen gewechselt hat, verstärkt die Mitkopplung den Wechsel: Mit fallendem $U_A$ sinkt auch $kU_A$, und $U_D$ wird noch
negativer. Der Ausgang springt deshalb ganz zum anderen Anschlag. Im Bild: Kippt der Balken einmal, schiebt der Motor das Gewicht hinterher, und er kippt
durch.
:::

::::beispiel Ein Schmitt-Trigger für ein verrauschtes Signal
Ein OPV, dessen Ausgang bis $\pm13\,\text{V}$ reicht, mit

$$R_1 = 10\,\text{k}\Omega, \qquad R_2 = 47\,\text{k}\Omega, \qquad k = \frac{10\,\text{k}\Omega}{57\,\text{k}\Omega} = 0{,}175.$$

**Die Schwellen.**

$$U_{S,o} = 0{,}175\cdot13\,\text{V} = 2{,}28\,\text{V}, \qquad U_{S,u} = -2{,}28\,\text{V}.$$

Die Hysterese ist $4{,}56\,\text{V}$ breit.

**Ein verrauschtes Signal.** Die Eingangsspannung steigt langsam von $-5$ auf $+5\,\text{V}$ und fällt wieder; ihr ist ein Rauschen von höchstens
$\pm0{,}5\,\text{V}$ überlagert. Beim Anstieg springt der Ausgang einmal, sobald die Spannung $2{,}28\,\text{V}$ erreicht, von $+13$ auf $-13\,\text{V}$. Um
zurückzuspringen, müsste das Rauschen die Spannung um mehr als $4{,}56\,\text{V}$ senken, also nie; erst beim Abstieg unter $-2{,}28\,\text{V}$ springt er
zurück. Ein Komparator mit einer einzigen Schwelle bei null hätte dagegen bei jedem Nulldurchgang so oft gezappelt, wie das Rauschen die Null kreuzt.

**Im Bild:** Eine Waage, die erst bei einem halben Kilo Unterschied umkippt, lässt sich von einem zitternden Tisch nicht hin- und herwerfen.
::::

:::grafik
Szene: get1/operationsverstaerker/01-schmitt-trigger · Vorlage: hysterese
Oben links die Schaltung von Bild 12.6 mit $U_E$ am invertierenden Eingang, $R_2 = 47\,\text{k}\Omega$ vom Ausgang zum nichtinvertierenden Eingang und
$R_1 = 10\,\text{k}\Omega$ nach Masse, mit den Zählpfeilen von $U_E$, $U_D$ und $U_A$. Oben rechts die Hystereseschleife $U_A$ über $U_E$: oben bei
$+13\,\text{V}$ bis $2{,}28\,\text{V}$, senkrechter Sprung nach $-13\,\text{V}$, unten zurück bis $-2{,}28\,\text{V}$ und senkrechter Sprung nach oben, mit
Pfeilen für die Laufrichtung. Unten über der Zeit ein langsames, verrauschtes Signal mit den beiden Schwellen als gestrichelte Linien, darunter der saubere
Ausgang des Schmitt-Triggers und zum Vergleich der zappelnde Ausgang eines Komparators mit einer Schwelle. Ein Regler für $R_2$ verändert die Breite der
Hysterese. Kernaussage: Mitkopplung macht aus einem Vergleicher einen Schalter mit Gedächtnis, der Rauschen ignoriert. (Rot = Ausgang und Schleife, blau =
Eingangssignal, orange = Schwellen und Rückführung, grau = Achsen, gestrichelt = Schwellen.)
:::

## Bedeutung und Ausblick

Der Operationsverstärker ist ein Differenzverstärker mit sehr großer Verstärkung. Für sich allein taugt er nur zum Vergleichen, weil schon Mikrovolt den Ausgang
an einen Anschlag treiben. Seine Stärke zeigt er erst mit Rückkopplung: Mit Gegenkopplung bestimmen wenige Widerstände genau, was die Schaltung tut, und die
riesige Verstärkung sorgt nur noch dafür, dass es genau gelingt. Mit Mitkopplung entstehen Schalter mit Hysterese und, mit Kondensatoren, Schwingschaltungen.
Rauschen setzt dabei die Grenze dessen, was man messen kann; der Differenzverstärker am Eingang hält wenigstens die Störungen fern, die beide Leitungen gleich
treffen.

Der nächste Artikel berechnet mit den beiden goldenen Regeln die Grundschaltungen: den invertierenden und den nichtinvertierenden Verstärker, den
Spannungsfolger, Addierer, Subtrahierer und Integrator. Der Artikel danach nimmt die Idealisierung zurück, mit endlicher Verstärkung, begrenzter Bandbreite und
Geschwindigkeit, Offsetfehlern und der Gleichtaktunterdrückung realer Bauteile.

:::kern
- Rauschen beschreibt man statistisch; sein Effektivwert ist $U_r=\sqrt{\int_0^\infty|u_r(f)|^2df}$.
- Unabhängige Rauschanteile addieren sich in den Quadraten; ein schmaleres Band lässt weniger durch.
- Thermisches Rauschen eines Widerstands: $|u_{r,R}|^2=4k_BTR$, weiß bis zu sehr hohen Frequenzen.
- Verstärken allein verbessert das SNR nicht; es hilft, früh und rauscharm zu verstärken, das Band zu begrenzen und Gleichtaktstörungen zu unterdrücken.
- Der Differenzverstärker antwortet nur auf $U_{e1}-U_{e2}$; die Gleichtaktspannung fällt heraus.
- Mit Stromquelle am Emitter ist die Verstärkung des Transistorpaars $-SR_C$, nicht $-2SR$, und linear nur für wenige Millivolt.
- Idealer OPV: kein Eingangsstrom, unendliche Verstärkung, Ausgangswiderstand null, kein Rauschen.
- Ohne Rückkopplung arbeitet ein OPV nur für Mikrovolt an $U_D$ linear; deshalb ist er dann ein Komparator.
- Gegenkopplung: Die Verstärkung wird $v_D/(1+kv_D)\approx1/k$, und $U_D$ geht gegen null.
- Goldene Regeln: kein Eingangsstrom; bei Gegenkopplung virtueller Kurzschluss zwischen den Eingängen.
- Zur Ruhe kommt die Gegenkopplung, weil der Ausgang sich nur endlich schnell ändert; Mitkopplung läuft an einen Anschlag.
- Schmitt-Trigger: Schwellen bei $kU_{A,\max}$ und $kU_{A,\min}$, dazwischen Hysterese und Gedächtnis.
:::

:::quiz
F: Was ist der Effektivwert eines Rauschens, und warum addieren sich Rauschanteile in den Quadraten?
A: Die Wurzel aus dem mittleren Quadrat, nach Gleichung 12.1 die Wurzel aus dem Integral der Dichte $|u_r(f)|^2$ über alle Frequenzen. Für unabhängige Anteile mit Mittelwert null ist der Mittelwert ihres Produkts null, deshalb bleibt im mittleren Quadrat der Summe nur die Summe der mittleren Quadrate; bei $10\,\text{nV}/\sqrt{\text{Hz}}$ über $100\,\text{kHz}$ sind es $3{,}16\,\mu\text{V}$.
F: Wie groß ist das thermische Rauschen eines Widerstands, und wovon hängt es ab?
A: Seine Dichte ist $4k_BTR$, proportional zu Temperatur und Widerstand und unabhängig von der Frequenz. Ein Widerstand von $1\,\text{k}\Omega$ rauscht bei $300\,\text{K}$ mit $4{,}07\,\text{nV}/\sqrt{\text{Hz}}$, über $20\,\text{kHz}$ mit $0{,}58\,\mu\text{V}$; die Idee der Herleitung ist, dass er an eine angepasste Last je Hertz die Leistung $k_BT$ abgibt.
F: Verbessert ein Verstärker das Signal-Rausch-Verhältnis?
A: Allein nicht: Er vergrößert Signal und Eingangsrauschen um denselben Faktor und fügt eigenes Rauschen hinzu. Das SNR verbessert man, indem man früh und rauscharm verstärkt, bevor weitere Rauschquellen kommen, das Band auf das Nötige begrenzt und mit einem Differenzverstärker Störungen entfernt, die beide Leitungen gleich treffen.
F: Was ist weißes Rauschen, und was unterscheidet Schrotrauschen und 1/f-Rauschen?
A: Weißes Rauschen hat eine konstante Dichte, als Idealisierung mit unendlicher Gesamtleistung; es ist eine Form des Spektrums, keine eigene Ursache. Schrotrauschen entsteht, weil ein Strom über eine Barriere aus einzelnen Ladungsträgern besteht, mit der Dichte $2eI$; 1/f-Rauschen wächst zu tiefen Frequenzen und trägt in jeder Dekade gleich viel bei.
F: Wie unterdrückt der Differenzverstärker aus Bild 12.1 Gleichtaktstörungen, und wie groß ist seine Verstärkung?
A: Q3 hält die Summe der Ströme fest; steigen beide Eingänge gleich, steigt das Emitterpotenzial mit, und kein Strom ändert sich. Für eine Differenz teilt sich das Signal auf beide Basis-Emitter-Strecken auf, $\Delta I_{Q1}=Su_{e,s}/2$, und die Verstärkung ist $-SR_C$, nicht $-2SR$ wie im Skript; mit $1\,\text{mA}$ und $10\,\text{k}\Omega$ sind es $-193$.
F: Welche vier Eigenschaften hat der ideale OPV, und wie klein ist der lineare Bereich eines realen OPV ohne Rückkopplung?
A: Unendlicher Eingangswiderstand, also kein Eingangsstrom; unendliche, frequenzunabhängige Verstärkung; Ausgangswiderstand null; kein Rauschen. Real ist $|U_D|$ nur bis $U_{A,\max}/v_D$ linear, bei $13\,\text{V}$ und $v_D=2\cdot10^5$ bis $65\,\mu\text{V}$, sodass der Ausgang ohne Rückkopplung praktisch immer an einem Anschlag liegt.
F: Wie arbeitet ein Flash-Wandler?
A: Ein Spannungsteiler erzeugt Schwellen an den invertierenden Eingängen mehrerer Komparatoren, die Eingangsspannung liegt an allen nichtinvertierenden. Jeder Komparator unter der Eingangsspannung meldet eins; die Zahl der Einsen ist der Wert. Mit Schwellen bei $1$, $2$ und $3\,\text{V}$ ergeben $1{,}7\,\text{V}$ die Zahl $01$; für $n$ Bit braucht man $2^n-1$ Komparatoren.
F: Was bewirkt Gegenkopplung, und woher kommen die goldenen Regeln?
A: Mit dem zurückgeführten Anteil $k$ ist $U_A=v_DU_E/(1+kv_D)\approx U_E/k$ und $U_D=U_E/(1+kv_D)$; die Verstärkung hängt nur noch von Widerständen ab, und $U_D$ wird winzig, bei $v_D$ unendlich null. Daraus folgen die Regeln: kein Eingangsstrom und, nur bei Gegenkopplung, der virtuelle Kurzschluss zwischen den Eingängen.
F: Warum kommt eine gegengekoppelte Schaltung zur Ruhe, und warum ist die Zyklusrechnung des Skripts dafür kein Beweis?
A: Ändert sich der Ausgang mit $dU_A/dt=\omega_TU_D$, nähert er sich bei Gegenkopplung dem Ruhewert exponentiell mit $\tau=1/(k\omega_T)$, bei $k=0{,}1$ und $1\,\text{MHz}$ mit $1{,}6\,\mu\text{s}$; bei Mitkopplung läuft er exponentiell weg. Eine Rechnung in sprunghaften Zyklen würde auch bei Gegenkopplung jede Abweichung mit $-kv_D$ vervielfachen und aufschwingen.
F: Wie entsteht die Hysterese des Schmitt-Triggers?
A: Die Rückführung auf den nichtinvertierenden Eingang hält den Ausgang an einem Anschlag fest; er wechselt erst, wenn $U_E$ die Schwelle $kU_{A,\max}$ übersteigt oder $kU_{A,\min}$ unterschreitet. Mit $10\,\text{k}\Omega$, $47\,\text{k}\Omega$ und $\pm13\,\text{V}$ liegen die Schwellen bei $\pm2{,}28\,\text{V}$; ein Rauschen von $\pm0{,}5\,\text{V}$ kann den Ausgang deshalb nicht hin- und herwerfen.
:::
