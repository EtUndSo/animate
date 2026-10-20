---
title: Zählpfeile und Vorzeichen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50300
summary: Von Grund auf – warum jede Spannung und jeder Strom erst mit einer Richtung vollständig ist und was ein negatives Ergebnis bedeutet. Leitbild ist das Multimeter mit rotem und schwarzem Kabel: Ein Zählpfeil ist die Vorschrift, wie man das Messgerät anschließt, und das Vorzeichen der Anzeige sagt, wie es in Wirklichkeit steht. Mit Spannungspfeil und Doppelindex, Strompfeil, Verbraucher- und Erzeugerzählpfeilsystem, der Leistung als Auskunft über Geben und Nehmen, dem Ohmschen Gesetz in beiden Systemen, Quelle und Verbraucher im Verbund, einer Batterie, die geladen wird, und Größen, die ständig die Richtung wechseln. Mit Beispiel-Seite.
tags: Zählpfeil, Verbraucherpfeilsystem, Erzeugerpfeilsystem, Vorzeichen, Leistung, Netzwerkanalyse
---

## Anschaulich

„Die Spannung beträgt $12\,\text{V}$" ist eine unvollständige Angabe. Zwischen welchen beiden Punkten, und welcher davon liegt höher? „Es fließen
$10\,\text{mA}$" ebenso: in welche Richtung? Spannung und Strom haben eine Richtung, und erst mit ihr ist eine Zahl vollständig. Diese Richtung
legt man in der Elektrotechnik mit __Zählpfeilen__ fest.

**Das Leitbild dieses Artikels:** **das Multimeter mit rotem und schwarzem Kabel**. Ein Spannungsmesser zeigt das Potenzial an der roten Messspitze
minus das an der schwarzen. Hält man Rot an den Pluspol einer $9$-V-Batterie und Schwarz an den Minuspol, zeigt er $+9\,\text{V}$; vertauscht man die
Kabel, zeigt er $-9\,\text{V}$. Falsch ist keine der beiden Messungen — das Vorzeichen sagt nur, welche Spitze am höheren Potenzial liegt. Ein
Strommesser, in eine Leitung eingesetzt, zeigt den Strom positiv an, der am roten Anschluss hineinfließt und am schwarzen hinaus; andersherum
eingesetzt, zeigt er dieselbe Zahl mit Minus.

Ein Zählpfeil ist genau so eine Anschlussvorschrift. Wer einen Pfeil in ein Schaltbild zeichnet, sagt damit: „So würde ich das Messgerät anschließen."
Der Wert der Größe ist das, was das Gerät dann anzeigen würde, samt Vorzeichen.

Drei Folgerungen kann man dem Multimeter direkt ansehen:

- **Ein Minus ist eine Auskunft, kein Fehler.** $-9\,\text{V}$ heißt: Die schwarze Spitze, das Pfeilende, liegt höher.
- **Die Richtung darf man frei wählen.** Wie man das Gerät auch anschließt, die Batterie bleibt dieselbe; es ändert sich nur das Vorzeichen.
- **Bei zwei Geräten zählt, wie sie zueinander stehen.** Misst man Spannung und Strom an einem Bauteil und multipliziert die Anzeigen, hängt es von
  der gegenseitigen Lage der Kabel ab, ob das Produkt die Leistung zählt, die das Bauteil aufnimmt, oder die, die es abgibt. Daraus entstehen die
  beiden __Zählpfeilsysteme__.

:::grafik
Szene: get1/stroeme-und-spannungen/03-multimeter · Vorlage: messgeraet-anschluss
Links eine $9$-V-Batterie mit Plus- und Minuspol, daneben ein Spannungsmesser mit rotem und schwarzem Kabel. Ein Schalter „Kabel tauschen" vertauscht
die Messspitzen: Die Anzeige springt zwischen $+9{,}00\,\text{V}$ und $-9{,}00\,\text{V}$, und im Schaltbild darunter dreht sich der Spannungspfeil mit, er
zeigt stets von der roten zur schwarzen Spitze. Rechts ein Stromkreis aus Batterie und Widerstand mit eingesetztem Strommesser; ein zweiter Schalter
dreht ihn um, die Anzeige wechselt zwischen $+6{,}00\,\text{mA}$ und $-6{,}00\,\text{mA}$, der Strompfeil zeigt stets vom roten zum schwarzen Anschluss. Kleine
Punkte für positive Ladungen laufen dabei unverändert im Kreis. Kernaussage: Der Zählpfeil ist die Anschlussvorschrift des Messgeräts; das Vorzeichen
sagt, ob die Wirklichkeit mit ihm übereinstimmt. (Rot = Zählpfeile und rotes Kabel, blau = Stromkreis und Ladungen, orange = Anzeige, grau = Gehäuse
und schwarzes Kabel.)
:::

## Der Spannungspfeil

Nach dem Artikel über das Potenzial ist die Spannung zwischen zwei Punkten die Differenz ihrer Potenziale, und die Reihenfolge der Punkte zählt. Im
Schaltbild steht dafür der __Spannungspfeil__ vom ersten zum zweiten Punkt:

:::formel Definition
$$U_{12} := \varphi_1 - \varphi_2, \qquad U_{21} = -U_{12}.$$
:::

**So liest man das:** $\varphi_1$ und $\varphi_2$ sind die Potenziale der Punkte $1$ und $2$ in Volt, $U_{12}$ ist die Spannung längs des Pfeils von
$1$ nach $2$, eine Zahl mit Vorzeichen. Positiv ist sie, wenn der Pfeil vom höheren zum niedrigeren Potenzial zeigt, von Plus nach Minus. Dreht man den
Pfeil um, wechselt nur das Vorzeichen. Der __Doppelindex__ nennt Anfangs- und Endpunkt; das Skript schreibt zum Beispiel $U_{11'}$ für die Spannung
von der Klemme $1$ zur Klemme $1'$. Statt des Pfeils markieren manche Schaltbilder, vor allem englischsprachige, den Pfeilanfang mit $+$ und das
Pfeilende mit $-$; das sagt dasselbe.

**Im Bild:** Der Pfeil ist das Messgerät: rote Spitze am Pfeilanfang, schwarze an der Pfeilspitze. Die Spannung ist, was es anzeigt.

:::herleitung
**Umdrehen.** Nach der Definition mit vertauschten Punkten:

$$U_{21} = \varphi_2 - \varphi_1 = -(\varphi_1 - \varphi_2) = -U_{12}.$$

**Aneinanderhängen.** Für einen dritten Punkt $3$ heben sich in der Summe zweier Spannungen die Potenziale des mittleren Punkts weg:

$$U_{12} + U_{23} = (\varphi_1 - \varphi_2) + (\varphi_2 - \varphi_3) = \varphi_1 - \varphi_3 = U_{13}.$$

Hintereinandergehängte Spannungspfeile addieren sich also zum Pfeil vom ersten bis zum letzten Punkt — unabhängig davon, was zwischen den Punkten
liegt. Das ist die Wegunabhängigkeit aus dem Artikel über das Potenzial.

**Bezugspunkt.** Ändert man den Bezugspunkt, verschieben sich alle Potenziale um dieselbe Konstante, die in der Differenz herausfällt. Spannungen
hängen deshalb nicht davon ab, wo die __Masse__ liegt, der Punkt mit dem Potenzial $0\,\text{V}$.
:::

Ein Spannungspfeil darf zwischen zwei beliebigen Punkten stehen, auch zwischen zwei Klemmen, zwischen denen kein Bauteil liegt. Wo man ihn im Bild
zeichnet, ob links oder rechts eines Bauteils, ist gleich; es zählen nur sein Anfangs- und sein Endpunkt. Das Skript zeigt das in Bild 5.18: An einem
Widerstand zwischen $+12\,\text{V}$ und $0\,\text{V}$ ergibt der Pfeil von Plus nach Masse $+12\,\text{V}$, der umgekehrte $-12\,\text{V}$.

::::beispiel Was der Spannungsmesser zeigt
In einer Schaltung haben drei Punkte die Potenziale

$$\varphi_\text{A} = 9\,\text{V}, \qquad \varphi_\text{B} = 3{,}6\,\text{V}, \qquad \varphi_\text{C} = 0\,\text{V};$$

C ist die Masse. Die Spannungen längs verschiedener Pfeile:

$$U_\text{AB} = 9\,\text{V} - 3{,}6\,\text{V} = 5{,}4\,\text{V}, \qquad U_\text{BA} = -5{,}4\,\text{V}, \qquad U_\text{BC} = 3{,}6\,\text{V}.$$

Rot an A und Schwarz an B zeigt $5{,}4\,\text{V}$; vertauscht $-5{,}4\,\text{V}$. Aneinandergehängt:

$$U_\text{AB} + U_\text{BC} = 5{,}4\,\text{V} + 3{,}6\,\text{V} = 9\,\text{V} = U_\text{AC}.$$

Legt man die Masse nach B, werden die Potenziale $5{,}4\,\text{V}$, $0\,\text{V}$ und $-3{,}6\,\text{V}$ — alle Spannungen bleiben dieselben.

**Im Bild:** Das Messgerät weiß nichts von der Masse. Es vergleicht nur seine beiden Spitzen.
::::

## Der Strompfeil

Ein __Strompfeil__ sitzt auf einer Leitung und legt fest, in welcher Richtung durch den Querschnitt gezählt wird. Nach dem Artikel über den Strom ist
die Stromstärke die Ladung, die pro Zeit durch einen Querschnitt tritt; der Pfeil sagt, welche Seite „vorn" ist:

:::formel Definition
$$I := \frac{dQ}{dt}, \qquad I_\text{Gegenpfeil} = -I.$$
:::

**So liest man das:** $dQ$ ist die Ladung, die in der kurzen Zeit $dt$ in Pfeilrichtung durch den Querschnitt tritt; Ladung, die gegen den Pfeil
tritt, zählt negativ. Positiv ist $I$ deshalb, wenn positive Ladung in Pfeilrichtung strömt — oder, gleichwertig, negative Ladung gegen sie. Ein
Pfeil in Gegenrichtung zählt denselben Vorgang mit umgekehrtem Vorzeichen.

**Im Bild:** Der Pfeil ist der Strommesser: Strom in Pfeilrichtung tritt am roten Anschluss ein. Dreht man das Gerät um, dreht sich der Pfeil mit, und
die Anzeige wechselt das Vorzeichen.

:::herleitung
**Gegenpfeil.** Zählt man in Gegenrichtung, ist jede Ladung, die vorher in Pfeilrichtung durchtrat, jetzt eine, die gegen den Pfeil durchtritt, und
umgekehrt. Jede gezählte Ladung wechselt also ihr Vorzeichen, damit auch ihre zeitliche Änderung:

$$dQ_\text{Gegenpfeil} = -dQ, \qquad I_\text{Gegenpfeil} = \frac{-dQ}{dt} = -I.$$

**Negative Träger.** Ein Elektron, das gegen den Pfeil wandert, nimmt die Ladung $-e$ von der Vorderseite weg; auf der Vorderseite wächst die Ladung um
$+e$ — wie bei einer positiven Ladung, die in Pfeilrichtung wandert (Artikel über den Strom). Beides zählt positiv.
:::

In Bild 5.18 des Skripts strömen positive Ladungen vom Pluspol durch den Widerstand zum Minuspol: Ein Pfeil in dieser Richtung ergibt $+10\,\text{mA}$,
der Gegenpfeil $-10\,\text{mA}$. Das Skript hebt noch hervor: Der tatsächliche __Elektronenfluss__ ist der technischen Stromrichtung entgegengesetzt.
Ein positiver Strom in Pfeilrichtung heißt in einem Metall also, dass die Elektronen gegen den Pfeil wandern.

::::beispiel Ein Strom, zwei Pfeile
Eine $9$-V-Batterie speist einen Widerstand von $1{,}5\,\text{k}\Omega$. Positive Ladungen strömen außen vom Plus- zum Minuspol, mit dem Ohmschen Gesetz

$$I = \frac{U}{R} = \frac{9\,\text{V}}{1500\,\Omega} = 6\,\text{mA}.$$

Ein Strompfeil in dieser Richtung zählt $+6\,\text{mA}$, ein Pfeil auf derselben Leitung in Gegenrichtung $-6\,\text{mA}$. In Wirklichkeit tragen
Elektronen den Strom, und zwar gegen die technische Richtung, pro Sekunde

$$\frac{6\cdot10^{-3}\,\text{A}}{1{,}602\cdot10^{-19}\,\text{C}} \approx 3{,}7\cdot10^{16}$$

Stück.

**Im Bild:** Zwei Strommesser auf derselben Leitung, einer verkehrt herum eingesetzt: Sie zeigen $+6\,\text{mA}$ und $-6\,\text{mA}$ und messen doch denselben
Strom.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/03-pfeile-schaltbild · Vorlage: zaehlpfeil-umschalten
Ein Stromkreis wie in Bild 5.18 des Skripts, mit eigenen Werten: links eine Spannungsquelle, oben die Leitung auf $+9\,\text{V}$ (rot), unten die Masse
mit $0\,\text{V}$ (blau, Massesymbol), rechts ein Widerstand mit $1{,}5\,\text{k}\Omega$. Oben zwei Klemmen beschriftet „Pluspol (höheres Potenzial)" und
„Minuspol (niedrigeres Potenzial)". Ein Spannungspfeil zwischen den Klemmen lässt sich per Klick umdrehen: von oben nach unten $U=+9\,\text{V}$, von
unten nach oben $U=-9\,\text{V}$. Darunter derselbe Kreis mit einem gebogenen Pfeil „positive Ladungen" im Uhrzeigersinn und einem umdrehbaren Strompfeil
auf der oberen Leitung: in Laufrichtung $I=+6\,\text{mA}$, dagegen $I=-6\,\text{mA}$; kleine Elektronen laufen sichtbar gegen den gebogenen Pfeil.
Kernaussage: Ein umgedrehter Pfeil ändert nur das Vorzeichen, nicht die Physik. (Rot = Zählpfeile, blau = Leitungen und Ladungen, orange = Anzeigen,
grau = Bauteile und Massesymbol.)
:::

## Zwei Pfeile an einem Zweipol

An einem __Zweipol__, einem Bauteil mit zwei Klemmen (Artikel über den Widerstand), braucht man beide Pfeile: die Spannung zwischen den Klemmen und
den Strom durch den Zweipol. Für ihre gegenseitige Lage gibt es genau zwei Möglichkeiten, und beide haben Namen.

**Die Akteure:**

- der Zweipol mit den Klemmen $1$ und $1'$;
- die Spannung $U_{11'}$, Pfeil von $1$ nach $1'$, in Volt;
- der Strom $I$ an der Klemme $1$, in Ampere, Pfeil entweder in den Zweipol hinein oder aus ihm heraus.

**Das Zusammenspiel:** *Zeigt der Strompfeil durch den Zweipol in dieselbe Richtung wie der Spannungspfeil oder in die Gegenrichtung?*

- Im __Verbraucherzählpfeilsystem__ (VZS) zeigt der Strompfeil an der Klemme $1$ in den Zweipol hinein. Durch den Zweipol hindurch läuft er dann von
  $1$ nach $1'$, in dieselbe Richtung wie der Spannungspfeil.
- Im __Erzeuger-__ oder __Generatorzählpfeilsystem__ (GZS) zeigt der Strompfeil an der Klemme $1$ aus dem Zweipol heraus. Durch den Zweipol läuft er von
  $1'$ nach $1$, dem Spannungspfeil entgegen.

Das Skript zeigt das VZS an einem Widerstand (Bild 5.20) und das GZS an einer Spannungsquelle (Bild 5.19). In der Norm für Richtungsregeln, DIN 5489,
heißen die beiden auch Verbraucher- und Erzeugerpfeilsystem.

**Im Bild:** Zwei Messgeräte am Zweipol. Im VZS zählt der Strommesser den Strom positiv, der an der Klemme mit der roten Spannungsspitze in den Zweipol
hineinfließt; im GZS den Strom, der dort herauskommt.

**Eine Vereinbarung, kein Gesetz.** Welches System man an welchem Zweipol nimmt, ist frei; das Skript nennt es eine unverbindliche Vereinbarung. Jede
Wahl beschreibt dieselbe Physik, nur fallen die Vorzeichen anders aus, und Spannungen und Ströme können negativ werden. Praktisch wählt man die Systeme
so, dass im Normalfall positive Werte herauskommen: Verbraucher im VZS, Quellen im GZS.

**Warum diese Zuordnung passt.** Durch einen Widerstand fließt der technische Strom vom höheren zum niedrigeren Potenzial — die Ladungen „fallen"
durch ihn hindurch, wie die Kugeln über das Nagelbrett im Artikel über den Widerstand. Strom und Spannung zeigen dort also in Wirklichkeit in dieselbe
Richtung, und im VZS sind beide positiv. Das meint der Satz des Skripts, die technische Stromflussrichtung entspreche der des VZS; er gilt für
Verbraucher. In einer Quelle dagegen fließt der technische Strom im Inneren vom Minus- zum Pluspol, gegen das Potenzialgefälle: Die Quelle hebt die
Ladungen mit einer nicht elektrischen Kraft auf das höhere Potenzial, chemisch in einer Batterie, magnetisch in einem Generator. Strom und Spannung
zeigen dort in Wirklichkeit gegeneinander, und im GZS sind beide positiv.

:::herleitung
**Im Widerstand.** Nach dem Ohmschen Gesetz in Punktform ist die Stromdichte $\sigma\vec E$ mit positivem $\sigma$; sie zeigt also in Feldrichtung. Das
Feld zeigt vom höheren zum niedrigeren Potenzial, denn längs des Felds ist das Wegintegral und damit die Spannung positiv. Der Strom fließt deshalb von
Plus nach Minus, in die Richtung des Spannungspfeils von Plus nach Minus.

**In der Quelle.** Im geschlossenen Kreis fließt durch die Quelle derselbe Strom wie durch den Verbraucher, denn Ladung häuft sich nirgends an. Außen
fließt er von Plus nach Minus, im Inneren der Quelle muss er also von Minus nach Plus fließen — gegen das elektrische Feld. Allein mit dem Feld ginge
das nicht, denn es triebe die Ladungen zurück. Eine zusätzliche, nicht elektrische Kraft muss sie hinaufschieben.
:::

:::grafik
Szene: get1/stroeme-und-spannungen/03-vzs-gzs · Vorlage: zweipol-pfeilsysteme
Zwei Schaltbilder nebeneinander nach Bild 5.19 und 5.20 des Skripts. Links eine Spannungsquelle mit den Klemmen $1$ oben und $1'$ unten, der
Quellenspannung $U_\text{q}$ als Pfeil nach unten neben der Quelle, dem Spannungspfeil $U_{11'}$ von $1$ nach $1'$ und dem Strompfeil $I_\text{q}$, der an
der Klemme $1$ aus der Quelle herauszeigt: GZS, die Pfeile laufen durch den Zweipol gegeneinander. Rechts ein Widerstand $R$ mit dem Strompfeil $I$ in die
Klemme $1$ hinein, $U_R$ nach unten neben $R$ und $U_{11'}$ von $1$ nach $1'$: VZS, die Pfeile laufen gleichsinnig. Ein Schalter blendet über beide
Bilder die zwei Messgeräte ein (rote und schwarze Kabel passend zu den Pfeilen); kleine Punkte für positive Ladungen fallen im Widerstand von oben nach
unten und werden in der Quelle von unten nach oben gehoben. Kernaussage: Verbraucher im VZS und Quellen im GZS ergeben positive Werte. (Rot =
Zählpfeile, blau = Ladungen und Leitungen, orange = Hubwirkung der Quelle, grau = Bauteile und Messgeräte.)
:::

## Warum die Leistung verrät, wer gibt und wer nimmt

Der eigentliche Zweck der beiden Systeme ist die Leistung. Mit beiden Pfeilen an einem Zweipol ist das Produkt der beiden Werte eine Leistung, und das
gewählte System legt fest, welche:

:::formel Satz
$$P_\text{auf} = U_{11'}\,I \quad\text{(VZS)}, \qquad P_\text{ab} = U_{11'}\,I \quad\text{(GZS)}.$$
:::

**So liest man das:** Eingabe sind die beiden Werte mit ihren Vorzeichen, Ausgabe eine Leistung in Watt, ebenfalls mit Vorzeichen. Im VZS ist das
Produkt die __aufgenommene Leistung__: Positiv heißt, der Zweipol nimmt wirklich Energie auf; negativ, er gibt sie ab. Im GZS ist es die __abgegebene
Leistung__, mit umgekehrter Deutung. Für denselben Zweipol ist die abgegebene Leistung die negative aufgenommene:

$$P_\text{ab} = -P_\text{auf}.$$

**Im Bild:** Ein Leistungsmesser multipliziert die Anzeigen des Spannungs- und des Strommessers. Wie im VZS angeschlossen, zeigt er positiv, wenn der
Zweipol Energie schluckt; wie im GZS angeschlossen, wenn er Energie liefert.

:::herleitung
**VZS.** In der kurzen Zeit $dt$ tritt die Ladung $I\,dt$ an der Klemme $1$ in den Zweipol ein und an der Klemme $1'$ wieder aus, denn im Zweipol
häuft sich keine Ladung an. Nach dem Artikel über das Potenzial hat eine Ladung $Q$ am Ort mit dem Potenzial $\varphi$ die Energie $Q\,\varphi$. Die
eintretende Ladung bringt also $I\,dt\,\varphi_1$ mit, die austretende nimmt $I\,dt\,\varphi_{1'}$ mit, und der Unterschied bleibt im Zweipol:

$$dW_\text{auf} = I\,dt\,(\varphi_1 - \varphi_{1'}) = U_{11'}\,I\,dt, \qquad P_\text{auf} = \frac{dW_\text{auf}}{dt} = U_{11'}\,I.$$

**GZS.** Jetzt zählt $I$ die Ladung, die an der Klemme $1$ herauskommt. Sie tritt bei $1'$ ein und bei $1$ aus und nimmt dabei den Unterschied
$I\,dt\,(\varphi_1 - \varphi_{1'})$ aus dem Zweipol mit; das ist die abgegebene Energie, und pro Zeit $U_{11'}\,I$.

**Negative Werte.** Wechselt man das System, kehrt sich nur der Strompfeil um, der Strom wechselt das Vorzeichen und mit ihm das Produkt. Daher ist die
abgegebene Leistung die negative aufgenommene. Ist $I$ negativ, fließt die Ladung in Wirklichkeit andersherum, und die Energie auch.
:::

::::beispiel Wer nimmt, wer gibt?
**(a) VZS.** Ein Widerstand mit $330\,\Omega$ liegt an $5\,\text{V}$; Strom- und Spannungspfeil sind gleichsinnig gezeichnet:

$$I = \frac{5\,\text{V}}{330\,\Omega} \approx 15{,}2\,\text{mA}, \qquad P_\text{auf} = 5\,\text{V}\cdot15{,}2\,\text{mA} \approx 75{,}8\,\text{mW}.$$

Positiv: Der Widerstand nimmt $75{,}8\,\text{mW}$ auf und wird warm.

**(b) Derselbe Widerstand im GZS.** Der Strompfeil zeigt jetzt an der Klemme $1$ heraus. Der Strom ist derselbe, gezählt wird er negativ:

$$I = -15{,}2\,\text{mA}, \qquad P_\text{ab} = 5\,\text{V}\cdot(-15{,}2\,\text{mA}) \approx -75{,}8\,\text{mW}.$$

Eine negative abgegebene Leistung von $75{,}8\,\text{mW}$ ist eine aufgenommene von $75{,}8\,\text{mW}$ — dieselbe Physik.

**Im Bild:** Derselbe Leistungsmesser, einmal umgedreht angeschlossen: Die Anzeige wechselt das Vorzeichen, der Widerstand wird gleich warm.
::::

**Die Vorzeichen auf einen Blick.** Trägt man den Betriebspunkt eines Zweipols im VZS in das Diagramm Strom über Spannung ein, verrät der Quadrant die
Rolle. Im ersten und dritten Quadranten haben Spannung und Strom dasselbe Vorzeichen, das Produkt ist positiv: Der Zweipol nimmt Energie auf. Im zweiten
und vierten Quadranten gibt er Energie ab. Die Kennlinie eines Widerstands im VZS läuft nur durch den ersten und dritten Quadranten — ein Widerstand
kann Energie nur aufnehmen, er ist __passiv__. Eine Quelle kann auch im zweiten oder vierten Quadranten arbeiten.

**Im Bild:** Wo der Leistungsmesser positiv zeigt, liegt der Betriebspunkt im ersten oder dritten Quadranten.

:::grafik
Szene: get1/stroeme-und-spannungen/03-quadranten · Vorlage: iu-quadranten
Ein Diagramm $I$ über $U$, alle Größen im VZS gezählt. Der erste und dritte Quadrant sind hellrot hinterlegt und mit „nimmt auf" beschriftet, der zweite
und vierte hellblau mit „gibt ab". Eine Ursprungsgerade für einen Widerstand läuft nur durch die roten Quadranten. Eine senkrechte Gerade bei
$U=9\,\text{V}$ steht für eine ideale Spannungsquelle; ein Betriebspunkt darauf lässt sich verschieben: unterhalb der Achse (Strom fließt am Pluspol
heraus) liegt er im vierten Quadranten, die Quelle gibt ab; oberhalb (Strom wird hineingedrückt) im ersten, die Quelle wird geladen. Ein
Leistungsbalken zeigt $P_\text{auf}=U\,I$ mit Vorzeichen. Kernaussage: Im VZS verrät der Quadrant, ob ein Zweipol gibt oder nimmt. (Rot = aufnehmende
Quadranten und Widerstandskennlinie, blau = abgebende Quadranten, orange = Betriebspunkt und Leistungsbalken, grau = Achsen.)
:::

**Das Ohmsche Gesetz in beiden Systemen.** Das Ohmsche Gesetz aus dem vorigen Artikel wurde für einen Strom von Plus nach Minus und einen Spannungspfeil
von Plus nach Minus hergeleitet — stillschweigend im VZS. Im GZS bekommt es ein Minus:

:::formel
$$U = R\,I \quad\text{(VZS)}, \qquad U = -R\,I \quad\text{(GZS)}.$$
:::

**So liest man das:** Eingabe ist der gezählte Strom, Ausgabe die gezählte Spannung. Der Widerstand $R$ ist positiv; das Minus im GZS kommt allein vom
umgedrehten Strompfeil. Für den Leitwert gilt entsprechend:

$$I = G\,U \quad\text{(VZS)}, \qquad I = -G\,U \quad\text{(GZS)}.$$

Wer das Ohmsche Gesetz ohne Blick auf die Pfeile anwendet, macht genau hier die meisten Vorzeichenfehler.

**Im Bild:** An einem Widerstand zeigen zwei Messgeräte, die wie im GZS angeschlossen sind, stets entgegengesetzte Vorzeichen.

:::herleitung
**VZS.** Im Artikel über den Widerstand ist der Strom durch das Leiterstück von der Plus- zur Minusseite gezählt und die Spannung ebenfalls von Plus nach
Minus; das ist das VZS, und es gilt $U=R\,I$.

**GZS.** Der GZS-Strompfeil zeigt durch den Zweipol in Gegenrichtung, er zählt denselben Strom mit umgekehrtem Vorzeichen:

$$I_\text{GZS} = -I_\text{VZS}, \qquad U = R\,I_\text{VZS} = -R\,I_\text{GZS}.$$

**Leistung.** Im GZS ist die abgegebene Leistung des Widerstands dann $U\,I$ mit $I$ gleich $-\frac{U}{R}$, also $-\frac{U^2}{R}$ — immer höchstens null,
wie es sich für einen passiven Zweipol gehört.
:::

::::beispiel Ohm mit umgedrehtem Pfeil
An einem Widerstand mit $2{,}2\,\text{k}\Omega$ misst man $4{,}4\,\text{V}$; der Strompfeil ist im GZS gezeichnet. Dann ist

$$I = -\frac{U}{R} = -\frac{4{,}4\,\text{V}}{2200\,\Omega} = -2\,\text{mA}, \qquad P_\text{ab} = 4{,}4\,\text{V}\cdot(-2\,\text{mA}) = -8{,}8\,\text{mW}.$$

Der Widerstand nimmt also $8{,}8\,\text{mW}$ auf. Hätte man fälschlich $U=R\,I$ benutzt, käme $+2\,\text{mA}$ heraus und eine abgegebene Leistung von
$+8{,}8\,\text{mW}$ — ein Widerstand, der Energie liefert, den es nicht gibt.

**Im Bild:** Der Strommesser steckt verkehrt herum in der Leitung. Seine $-2\,\text{mA}$ sind richtig; falsch wäre nur, das Minus zu übersehen.
::::

## Quelle und Verbraucher im Verbund

Schließt man eine ideale Spannungsquelle und einen Widerstand an dieselben Klemmen $1$ und $1'$ an, wie in Bild 5.21 des Skripts, wählt man für jedes
Bauteil sein passendes System: die Quelle im GZS mit dem Strom $I_\text{q}$, den Widerstand im VZS mit dem Strom $I$. Dann sind beide Ströme positiv, und Spannung und
Strom sind an beiden Bauteilen dieselben:

$$U_{11'} = U_\text{q} = U_R, \qquad I_\text{q} = I.$$

Die Leistung, die die Quelle abgibt, ist deshalb genau die, die der Widerstand aufnimmt:

$$P_\text{ab,q} = U_{11'}\,I_\text{q} = U_{11'}\,I = P_\text{auf,R}.$$

**Im Bild:** Zwei Leistungsmesser, einer an der Quelle im GZS, einer am Widerstand im VZS. Beide zeigen dieselbe positive Zahl: Was die Quelle hergibt,
kommt im Widerstand an.

:::herleitung
**Dieselbe Spannung.** Beide Bauteile liegen zwischen denselben Klemmen, und eine Spannung hängt nur von den Potenzialen ihrer Endpunkte ab. Die
Pfeile $U_\text{q}$, $U_{11'}$ und $U_R$ zeigen alle von oben nach unten, also sind sie gleich.

**Derselbe Strom.** Der Strom, den die Quelle an der Klemme $1$ abgibt, kann sich nirgends verzweigen oder anhäufen; er fließt vollständig in den
Widerstand hinein (Kontinuität). Der GZS-Pfeil der Quelle und der VZS-Pfeil des Widerstands zeigen dabei auf der Leitung in dieselbe Richtung, also ist
$I_\text{q}$ gleich $I$.

**Die Bilanz.** Gleiche Spannung mal gleicher Strom ergibt gleiche Leistung — die Energieerhaltung in der Sprache der Zählpfeile.
:::

::::beispiel Batterie und Widerstand
Eine $9$-V-Batterie, als ideale Quelle betrachtet, speist einen Widerstand von $1{,}5\,\text{k}\Omega$. Mit der Quelle im GZS und dem Widerstand im VZS:

$$I_\text{q} = I = \frac{9\,\text{V}}{1500\,\Omega} = 6\,\text{mA}, \qquad P_\text{ab,q} = P_\text{auf,R} = 9\,\text{V}\cdot6\,\text{mA} = 54\,\text{mW}.$$

Eine $9$-V-Batterie speichert etwa $500\,\text{mAh}$, also rund $4{,}5\,\text{Wh}$. Bei $54\,\text{mW}$ reicht das für

$$\frac{4{,}5\,\text{Wh}}{0{,}054\,\text{W}} \approx 83\,\text{h},$$

dasselbe wie $500\,\text{mAh}$ geteilt durch $6\,\text{mA}$.

**Im Bild:** Beide Messgerätepaare zeigen nur positive Werte, weil jedes Bauteil in seinem passenden System gezählt wird.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/03-verbund · Vorlage: quelle-verbraucher
Das Schaltbild nach Bild 5.21 des Skripts mit eigenen Werten: links eine Quelle mit $U_\text{q}=9\,\text{V}$ (Pfeil nach unten), oben die Klemme $1$,
unten $1'$, rechts ein Widerstand $R=1{,}5\,\text{k}\Omega$ mit $U_R$ nach unten. Auf der oberen Leitung $I_\text{q}$ aus der Quelle heraus und $I$ in den
Widerstand hinein, beide nach rechts; dazwischen $U_{11'}$ von $1$ nach $1'$. Ein breiter oranger Pfeil zeigt den Energiefluss von der Quelle zum
Widerstand, beschriftet mit $54\,\text{mW}$; zwei Leistungsmesser zeigen $P_\text{ab,q}$ und $P_\text{auf,R}$, beide $+54\,\text{mW}$. Kernaussage: Mit dem
passenden System pro Bauteil sind alle Werte positiv, und die abgegebene Leistung der Quelle ist die aufgenommene des Verbrauchers. (Rot = Zählpfeile,
blau = Leitungen, orange = Energiefluss, grau = Bauteile und Messgeräte.)
:::

## Die Rolle bestimmt das Vorzeichen

Ein Schaltzeichen sagt nicht, ob ein Zweipol gibt oder nimmt; das sagt erst das Vorzeichen der Leistung. Eine Batterie, die geladen wird, nimmt Energie
auf, obwohl sie als Quelle gezeichnet ist. Ein Elektromotor, der beim Bremsen als Generator arbeitet, gibt Energie ab, obwohl man ihn als Verbraucher
zeichnen würde. Zeichnet man die Pfeile nach der erwarteten Rolle und kommt eine negative Leistung heraus, spielt der Zweipol in Wirklichkeit gerade die
andere Rolle.

Für die Rechnung ist das kein Problem. Man legt alle Pfeile vorher fest, rechnet mit ihnen zu Ende und deutet erst das Ergebnis: Ein negativer Strom
fließt gegen seinen Pfeil, eine negative Spannung zeigt vom niedrigeren zum höheren Potenzial, eine negative aufgenommene Leistung ist eine abgegebene.
Die Pfeile während der Rechnung umzudrehen, weil ein Wert negativ geworden ist, ist dagegen ein typischer Fehler: Die Gleichungen, die mit den alten
Pfeilen aufgestellt wurden, passen dann nicht mehr.

**Im Bild:** Das Multimeter bleibt angeschlossen, wie es ist. Man liest die Anzeige samt Vorzeichen ab und denkt dann nach, was sie bedeutet.

::::beispiel Die Autobatterie wird geladen
Bei laufendem Motor liefert die Lichtmaschine $14{,}2\,\text{V}$ an die Batterie und drückt $20\,\text{A}$ in deren Pluspol hinein. Die Batterie ist wie
eine Quelle im GZS gezeichnet, ihr Strompfeil zeigt also am Pluspol heraus:

$$I = -20\,\text{A}, \qquad P_\text{ab} = 14{,}2\,\text{V}\cdot(-20\,\text{A}) = -284\,\text{W}.$$

Die Batterie gibt $-284\,\text{W}$ ab, sie nimmt also $284\,\text{W}$ auf — sie wird geladen. Im VZS gezählt, mit dem Strompfeil in den Pluspol hinein,
wäre derselbe Betriebspunkt $I=+20\,\text{A}$ mit einer aufgenommenen Leistung von $+284\,\text{W}$, im ersten Quadranten.

Beim Anlassen, solange der Motor noch steht, versorgt die Batterie den Anlasser, und der Strom kehrt sich um: Er kommt am Pluspol heraus, im GZS positiv,
und die Batterie gibt Leistung ab.

**Im Bild:** Der Strommesser an der Batterie zeigt beim Laden $-20\,\text{A}$: Der Strom läuft am roten Anschluss hinaus statt hinein. Dieselbe Batterie ist
mal Verbraucher, mal Quelle.
::::

## Wenn die Richtung ständig wechselt

Bei Größen, die sich mit der Zeit ändern, ist der Zählpfeil unverzichtbar. Nach DIN schreibt man ihre Momentanwerte klein, $u(t)$ und $i(t)$. Eine
__Wechselspannung__ kehrt ihre Richtung in jeder Periode zweimal um; der Pfeil bleibt, wo er ist, und das Vorzeichen von $u(t)$ sagt in jedem Augenblick,
wie es gerade steht. Ohne festen Pfeil hätte der Satz „die Spannung ist jetzt positiv" keinen Sinn.

Am Widerstand im VZS gilt das Ohmsche Gesetz in jedem Augenblick. Für die aufgenommene Leistung folgt daraus:

$$p(t) = u(t)\,i(t) = R\,i(t)^2 \ge 0.$$

**So liest man das:** Spannung und Strom wechseln ihr Vorzeichen gemeinsam, das Produkt wird nie negativ. Ein Widerstand nimmt in jedem Augenblick
Energie auf, gleich in welche Richtung der Strom gerade fließt.

**Im Bild:** Das Multimeter zeigt im Wechsel Plus und Minus, der Leistungsmesser am Widerstand nur Plus.

:::herleitung
**Ohm im Augenblick.** Die Drift der Elektronen stellt sich nach dem Artikel über den Widerstand in Femtosekunden ein, nach rund
$2\cdot10^{-14}\,\text{s}$. Eine Spannung, die sich in Millisekunden ändert, ist für die Elektronen in jedem Moment praktisch konstant; deshalb gilt das
Ohmsche Gesetz für die Momentanwerte:

$$u(t) = R\,i(t).$$

**Die Leistung.** Die Herleitung der aufgenommenen Leistung gilt für jedes kurze Zeitstück $dt$ und damit auch für Momentanwerte. Mit dem Ohmschen
Gesetz eingesetzt:

$$p(t) = u(t)\,i(t) = R\,i(t)\cdot i(t) = R\,i(t)^2.$$

Ein Quadrat ist nie negativ, und $R$ ist positiv.
:::

::::beispiel Wechselspannung am Widerstand
Eine Wechselspannung mit dem Scheitelwert $10\,\text{V}$ und $50\,\text{Hz}$ liegt an $100\,\Omega$:

$$u(t) = 10\,\text{V}\cdot\sin(2\pi\cdot50\,\text{Hz}\cdot t), \qquad i(t) = \frac{u(t)}{100\,\Omega} = 0{,}1\,\text{A}\cdot\sin(2\pi\cdot50\,\text{Hz}\cdot t).$$

Eine Periode dauert $20\,\text{ms}$; Spannung und Strom wechseln alle $10\,\text{ms}$ ihr Vorzeichen, hundertmal pro Sekunde. Einige Augenblicke:

| $t$ | $u(t)$ | $i(t)$ | $p(t)$ |
|---|---|---|---|
| $2{,}5\,\text{ms}$ | $7{,}07\,\text{V}$ | $70{,}7\,\text{mA}$ | $0{,}50\,\text{W}$ |
| $5\,\text{ms}$ | $10\,\text{V}$ | $100\,\text{mA}$ | $1{,}00\,\text{W}$ |
| $12{,}5\,\text{ms}$ | $-7{,}07\,\text{V}$ | $-70{,}7\,\text{mA}$ | $0{,}50\,\text{W}$ |
| $15\,\text{ms}$ | $-10\,\text{V}$ | $-100\,\text{mA}$ | $1{,}00\,\text{W}$ |

Die Leistung schwankt zwischen $0$ und $1\,\text{W}$ und ist im Mittel halb so groß:

$$p(t) = 1\,\text{W}\cdot\sin^2(2\pi\cdot50\,\text{Hz}\cdot t) = 0{,}5\,\text{W}\cdot\big(1 - \cos(2\pi\cdot100\,\text{Hz}\cdot t)\big), \qquad \bar p = 0{,}5\,\text{W}.$$

:::herleitung
Mit der Doppelwinkelformel ist das Quadrat des Sinus eins halb minus ein halber Kosinus der doppelten Frequenz. Über eine volle Periode ist der Mittelwert
des Kosinus null, denn er ist gleich lang positiv wie negativ; übrig bleibt die Hälfte des Höchstwerts.
:::

**Im Bild:** Die Anzeige des Strommessers pendelt zwischen $+100$ und $-100\,\text{mA}$, die des Leistungsmessers zwischen $0$ und $1\,\text{W}$, nie darunter.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/03-wechselgroessen · Vorlage: u-i-p-verlauf
Oben ein Widerstand mit festen Zählpfeilen $u(t)$ und $i(t)$ im VZS, darunter drei Zeitverläufe über zwei Perioden: $u(t)$ mit $10\,\text{V}$ Scheitelwert,
$i(t)$ mit $0{,}1\,\text{A}$, beide wechseln bei $10\,\text{ms}$, $20\,\text{ms}$ und $30\,\text{ms}$ das Vorzeichen; $p(t)=u(t)\,i(t)$ bleibt zwischen $0$ und
$1\,\text{W}$ und schwingt mit doppelter Frequenz, eine gestrichelte Linie markiert den Mittelwert $0{,}5\,\text{W}$. Ein Zeitcursor läuft mit; an seiner
Stelle leuchtet im Schaltbild der tatsächliche Stromfluss auf, mal in, mal gegen die Pfeilrichtung. Kernaussage: Der Pfeil bleibt fest, das Vorzeichen
wechselt; am Widerstand ist die Leistung trotzdem nie negativ. (Rot = Zählpfeile und $p(t)$, blau = $u(t)$ und $i(t)$, orange = Zeitcursor und
tatsächlicher Fluss, grau = Achsen, gestrichelt = Mittelwert.)
:::

## Bedeutung und Ausblick

Zählpfeile sind die Grammatik der Netzwerkanalyse. Die Kirchhoffschen Regeln, die in diesem Kapitel noch kommen, sind mit ihnen formuliert: An einem
Knoten werden die Ströme nach ihren Pfeilen hinein- oder herausgezählt, in einer Masche die Spannungen nach ihren Pfeilen mit oder gegen den
Umlaufsinn. Das Rezept ist immer dasselbe — erst alle Pfeile festlegen, dann die Gleichungen aufstellen, zu Ende rechnen und am Schluss die Vorzeichen
deuten.

Auch die Messtechnik in Kapitel 6 folgt ihnen: Ein Messgerät wird so angeschlossen, wie der Pfeil es vorschreibt. Und die Leistungsrechnung in
Kapitel 7 lebt von den beiden Systemen. Zählt man in einem Netz alle Zweipole im VZS, ist die Summe aller aufgenommenen Leistungen null, weil die
Energie, die die einen abgeben, die anderen aufnehmen — eine nützliche Probe für jede Rechnung, die sich mit den Kirchhoffschen Regeln beweisen lässt.

Bei Wechselstrom, in einem späteren Modul, bleiben die Pfeile fest, und die Vorzeichen wechseln mit der Zeit; die Zählpfeile tragen dort jede Rechnung.

:::kern
- Spannung und Strom haben eine Richtung; erst ein __Zählpfeil__ macht eine Zahl vollständig.
- Ein Zählpfeil ist eine Messvorschrift: rote Spitze am Pfeilanfang, schwarze an der Pfeilspitze; der Wert ist die Anzeige samt Vorzeichen.
- __Spannungspfeil__ von $1$ nach $2$: $U_{12}=\varphi_1-\varphi_2$; umgedreht wechselt nur das Vorzeichen.
- __Strompfeil__: zählt positive Ladung in Pfeilrichtung; Elektronen laufen bei positivem Strom gegen den Pfeil.
- Ein negativer Wert heißt: In Wirklichkeit ist es andersherum. Pfeile während der Rechnung nicht umdrehen.
- __VZS__: Strom- und Spannungspfeil durch den Zweipol gleichsinnig; __GZS__: gegensinnig. Die Wahl ist eine Vereinbarung.
- Im VZS ist $U\,I$ die aufgenommene, im GZS die abgegebene Leistung; die abgegebene ist die negative aufgenommene.
- Ohmsches Gesetz: $U=R\,I$ im VZS, mit Minus im GZS.
- Verbraucher im VZS und Quellen im GZS liefern im Normalfall positive Werte; im Verbund ist die abgegebene Leistung der Quelle die aufgenommene des Verbrauchers.
- Die Rolle bestimmt das Vorzeichen: Eine Batterie, die geladen wird, hat im GZS eine negative abgegebene Leistung.
- Bei Wechselgrößen bleibt der Pfeil fest; am Widerstand ist $p(t)=R\,i(t)^2$ nie negativ.
:::

:::quiz
F: Warum ist die Angabe „die Spannung beträgt $12\,\text{V}$" unvollständig, und was ergänzt der Zählpfeil?
A: Eine Spannung ist eine Potenzialdifferenz zwischen zwei Punkten, und ihr Vorzeichen hängt von der Reihenfolge ab: $U_{12}=\varphi_1-\varphi_2$, umgekehrt $U_{21}=-U_{12}$. Der Spannungspfeil nennt Anfangs- und Endpunkt, also die Richtung, in der gezählt wird — wie rote und schwarze Spitze eines Spannungsmessers.
F: Was bedeutet es, wenn ein Spannungsmesser $-9\,\text{V}$ anzeigt?
A: Die schwarze Spitze, also das Ende des Zählpfeils, liegt um $9\,\text{V}$ höher als die rote. Die Messung ist nicht falsch; das Vorzeichen ist die Auskunft über die tatsächliche Richtung. Mit vertauschten Kabeln zeigte das Gerät $+9\,\text{V}$.
F: Was zählt ein Strompfeil, und was folgt für die Elektronen bei einem positiven Strom?
A: Er zählt die Ladung, die pro Zeit in Pfeilrichtung durch den Querschnitt tritt; Ladung gegen den Pfeil zählt negativ, ein Gegenpfeil kehrt das Vorzeichen um. Ein positiver Strom heißt positive Ladung in oder negative Ladung gegen die Pfeilrichtung — in Metallen laufen die Elektronen also gegen den Pfeil. Bei $6\,\text{mA}$ sind das rund $3{,}7\cdot10^{16}$ Elektronen pro Sekunde.
F: Wie unterscheiden sich Verbraucher- und Erzeugerzählpfeilsystem?
A: Im VZS zeigt der Strompfeil an der Klemme, an der der Spannungspfeil beginnt, in den Zweipol hinein; durch den Zweipol laufen beide gleichsinnig. Im GZS zeigt er dort heraus, die Pfeile laufen gegensinnig. Welches System man wählt, ist eine Vereinbarung.
F: Warum passt das VZS zu Verbrauchern und das GZS zu Quellen?
A: Im Widerstand fließt der technische Strom nach $\vec J=\sigma\vec E$ in Feldrichtung, vom höheren zum niedrigeren Potenzial, also wie der Spannungspfeil: Im VZS sind beide Werte positiv. In einer Quelle fließt er im Inneren von Minus nach Plus, gegen das Feld, angetrieben von einer nicht elektrischen Kraft: Im GZS sind beide positiv.
F: Was gibt das Produkt $U\,I$ im VZS und im GZS an, und warum?
A: Im VZS die aufgenommene, im GZS die abgegebene Leistung. Die Ladung $I\,dt$ tritt im VZS bei $1$ mit der Energie $I\,dt\,\varphi_1$ ein und bei $1'$ mit $I\,dt\,\varphi_{1'}$ aus; der Unterschied $U_{11'}\,I\,dt$ bleibt im Zweipol. Im GZS läuft die Ladung andersherum und nimmt diese Energie mit. Deshalb ist die abgegebene Leistung die negative aufgenommene.
F: Wie lautet das Ohmsche Gesetz im GZS, und welcher Fehler droht ohne Blick auf die Pfeile?
A: $U=-R\,I$, weil der GZS-Pfeil denselben Strom mit umgekehrtem Vorzeichen zählt. Misst man an $2{,}2\,\text{k}\Omega$ im GZS $4{,}4\,\text{V}$, ist $I=-2\,\text{mA}$ und die abgegebene Leistung $-8{,}8\,\text{mW}$. Mit $U=R\,I$ käme ein Widerstand heraus, der $8{,}8\,\text{mW}$ liefert — unmöglich.
F: Was zeigt der Quadrant des Betriebspunkts im Diagramm Strom über Spannung, wenn alles im VZS gezählt ist?
A: Im ersten und dritten Quadranten haben Spannung und Strom dasselbe Vorzeichen, der Zweipol nimmt Energie auf; im zweiten und vierten gibt er sie ab. Die Kennlinie eines Widerstands läuft nur durch den ersten und dritten — er ist passiv. Eine Quelle arbeitet beim Liefern im vierten Quadranten, beim Laden im ersten.
F: Warum ist bei einer Autobatterie, die mit $14{,}2\,\text{V}$ und $20\,\text{A}$ geladen wird, die abgegebene Leistung im GZS negativ?
A: Der GZS-Pfeil zählt den Strom, der am Pluspol herauskommt; beim Laden wird der Strom aber hineingedrückt, also ist $I=-20\,\text{A}$ und $P_\text{ab}=-284\,\text{W}$. Die Batterie nimmt $284\,\text{W}$ auf. Nicht das Schaltzeichen, sondern das Vorzeichen der Leistung sagt, ob ein Zweipol gibt oder nimmt.
F: Warum braucht man bei Wechselgrößen feste Zählpfeile, und warum ist die Leistung am Widerstand trotzdem nie negativ?
A: Eine Wechselspannung kehrt ihre Richtung ständig um; nur mit einem festen Pfeil bedeutet das Vorzeichen von $u(t)$ etwas. Am Widerstand im VZS gilt Ohm in jedem Augenblick, weil sich die Drift in Femtosekunden einstellt; Spannung und Strom wechseln ihr Vorzeichen gemeinsam, und $p(t)=R\,i(t)^2$ ist nie negativ. Bei $10\,\text{V}$ Scheitelwert an $100\,\Omega$ schwankt $p(t)$ zwischen $0$ und $1\,\text{W}$, im Mittel $0{,}5\,\text{W}$.
:::
