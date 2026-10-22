---
title: Strom- und Spannungsmessung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Strom- und Spannungsmessung
order: 60100
summary: Von Grund auf – warum jedes Messgerät die Schaltung verändert, die es misst, und wie man den Fehler klein hält und ausrechnet. Leitbild ist der Wasserkreislauf mit Wasseruhr aus dem Artikel über den Strom: Der Strommesser ist eine Uhr im Rohr, der Spannungsmesser eine Uhr in einem dünnen Nebenröhrchen. Mit Innenwiderstand und Idealwerten, dem Fehler der Strom- und der Spannungsmessung samt Ersatzquelle, strom- und spannungsrichtigem Messen mit Korrektur und Grenzwiderstand, der Widerstandsmessung im Multimeter und der Vierleitermessung, Messbereichserweiterung mit Nebenwiderstand und Vorwiderstand sowie Bürdenspannung und Ohm pro Volt. Mit Beispiel-Seite.
tags: Messung, Amperemeter, Voltmeter, Innenwiderstand, Shunt, Vorwiderstand, Messbereichserweiterung
---

## Anschaulich

Wer misst, greift ein. Ein Reifendruckprüfer lässt beim Aufsetzen ein wenig Luft heraus, ein Thermometer kühlt den heißen Tee, in den man es taucht. Bei
elektrischen Messungen ist es genauso: Ein Messgerät ist selbst ein Bauteil mit einem Widerstand, und wer es anschließt, ändert die Schaltung. Die Kunst
des Messens besteht darin, diese Änderung klein zu halten — und, wo sie nicht klein ist, auszurechnen.

**Das Leitbild dieses Artikels:** **der Wasserkreislauf mit Wasseruhr aus dem Artikel über den Strom.** Um den Durchfluss zu messen, baut man eine
Wasseruhr ins Rohr ein; jedes Wasserteilchen muss durch sie hindurch. Hat die Uhr selbst einen Strömungswiderstand, fließt nach dem Einbau weniger als
vorher. Den Druckunterschied zwischen zwei Stellen misst man dagegen mit einem dünnen Nebenröhrchen, das beide Stellen verbindet und in dem eine kleine
Uhr sitzt: Je größer der Druckunterschied, desto mehr fließt hindurch. Dieses Röhrchen zapft dem Kreislauf aber selbst etwas Wasser ab, und zwar umso
weniger, je dünner es ist.

Drei Folgerungen kann man dem Wasserkreislauf direkt ansehen:

- **Der Strommesser gehört in den Weg, der Spannungsmesser daneben.** Den Durchfluss misst nur, was im Rohr sitzt; einen Druckunterschied nur, was zwei
  Stellen verbindet.
- **Die Ideale sind entgegengesetzt.** Die Uhr im Rohr soll gar nicht bremsen, ihr Widerstand null sein. Das Nebenröhrchen soll fast nichts durchlassen,
  sein Widerstand unendlich groß sein.
- **Den Messbereich erweitert man mit Zusatzwegen.** Eine Umgehungsleitung neben der Uhr lässt sie nur einen bekannten Bruchteil des Durchflusses
  sehen; eine Engstelle vor dem Nebenröhrchen lässt nur einen bekannten Bruchteil des Druckunterschieds auf die kleine Uhr wirken.

Elektrisch ist das Nebenröhrchen keine Analogie, sondern wörtlich so: Ein Zeigerinstrument misst immer einen Strom, und zum Spannungsmesser wird es
erst durch einen großen bekannten Widerstand in Reihe.

:::grafik
Szene: get1/strom-und-spannungsmessung/01-messen-wasser · Vorlage: wasseruhr-nebenroehrchen
Ein geschlossener Wasserkreislauf mit Pumpe und einer Engstelle als Verbraucher. Ein Regler baut eine Wasseruhr ins Hauptrohr ein: Ihre Turbine bremst
sichtbar, der Durchfluss im ganzen Kreis sinkt ein wenig; ein zweiter Regler macht die Uhr reibungsärmer, bis der Unterschied verschwindet. An zwei
Stellen vor und hinter der Engstelle sitzt ein Nebenröhrchen mit einer kleinen Uhr; ein dritter Regler macht das Röhrchen dicker oder dünner: Je dicker,
desto mehr Wasser zweigt ab und desto stärker sinkt der Druckunterschied an der Engstelle. Daneben in derselben Anordnung die Schaltung mit Quelle,
Widerstand, Strommesser in Reihe und Spannungsmesser parallel. Kernaussage: Ein Strommesser soll nicht bremsen, ein Spannungsmesser nichts abzweigen.
(Blau = Wasser und Strom, rot = Messgeräte, orange = Störung durch das Messgerät, grau = Rohre und Pumpe.)
:::

## Messgeräte und Innenwiderstand

Ströme misst man mit __Strommessern__ (Amperemetern), Spannungen mit __Spannungsmessern__ (Voltmetern); beide stecken heute meist zusammen in einem
__Multimeter__. Ein Messgerät beschreiben vor allem zwei Angaben: sein __Messbereich__, der größte Wert, den es noch anzeigt, und sein
__Innenwiderstand__ $R_i$, der Widerstand zwischen seinen beiden Anschlüssen.

- Ein **Strommesser** liegt in Reihe im Zweig. Er soll keinen Spannungsabfall verursachen, also einen kleinen Innenwiderstand haben; typisch ist etwa
  $1\,\Omega$, ideal $0\,\Omega$.
- Ein **Spannungsmesser** liegt parallel zu dem, was man misst. Er soll keinen Strom ziehen, also einen großen Innenwiderstand haben; typisch für ein
  Digitalmultimeter sind $10\,\text{M}\Omega$, ideal unendlich.

Ein idealer Strommesser verhält sich deshalb wie ein Stück Draht, ein idealer Spannungsmesser wie eine Unterbrechung. Daraus folgt auch die wichtigste
Warnung: Einen Strommesser darf man nie parallel zu einer Quelle legen. Sein kleiner Innenwiderstand schließt sie kurz, und es fließt ein sehr großer
Strom.

**Im Bild:** Die Wasseruhr im Rohr soll so leichtgängig sein wie ein Stück Rohr, das Nebenröhrchen so dünn, dass es praktisch verschlossen ist.

:::herleitung
**Kein Spannungsabfall am Strommesser.** Nach dem Ohmschen Gesetz fällt am Strommesser die Spannung $R_i\,I$ ab; sie fehlt dem übrigen Kreis. Null ist
sie für jeden Strom nur, wenn $R_i$ null ist.

**Kein Strom durch den Spannungsmesser.** Durch einen Spannungsmesser an der Spannung $U$ fließt der Strom $U/R_i$; er fehlt dem Zweig, an dem gemessen
wird. Er verschwindet für jede Spannung nur, wenn $R_i$ gegen unendlich geht.

**Kurzschluss.** Ein Strommesser mit $1\,\Omega$ an einer Quelle von $12\,\text{V}$ ließe nach Ohm $12\,\text{A}$ fließen, soweit die Quelle das hergibt.
:::

## Der Fehler der Strommessung

**Die Akteure:** eine ideale Spannungsquelle $U$, ein Widerstand $R$, der Strom $I_R$ ohne und $I_R'$ mit Strommesser, dessen Innenwiderstand $R_i$ in Reihe
zu $R$ liegt.

**Das Zusammenspiel:** *Wie viel kleiner wird der Strom, weil der Strommesser im Weg liegt?*

:::formel
$$I_R = \frac{U}{R}, \qquad I_R' = \frac{U}{R + R_i}, \qquad \frac{I_R'}{I_R} = \frac{R}{R + R_i} = \frac{1}{1 + R_i/R}.$$
:::

**So liest man das:** Der Strommesser liegt mit seinem Innenwiderstand in Reihe zum Widerstand, der Kreis hat jetzt $R+R_i$. Der angezeigte Strom ist um
den Faktor $\frac{1}{1+R_i/R}$ zu klein, der relative Fehler ist $-\frac{R_i}{R+R_i}$, ungefähr $-\frac{R_i}{R}$. Für einen kleinen Fehler muss $R_i$ viel
kleiner sein als $R$.

**Im Bild:** Eine Wasseruhr mit spürbarem Strömungswiderstand im Rohr: Der Kreislauf hat jetzt eine Engstelle mehr, und es fließt weniger, als ohne die
Uhr geflossen wäre.

:::herleitung
Ohne Strommesser gilt im Kreis aus Quelle und Widerstand das Ohmsche Gesetz. Mit Strommesser liegen $R$ und $R_i$ in Reihe, und ihr Ersatzwiderstand ist
die Summe. Das Verhältnis der beiden Ströme:

$$\frac{I_R'}{I_R} = \frac{U/(R+R_i)}{U/R} = \frac{R}{R + R_i}, \qquad \frac{I_R' - I_R}{I_R} = \frac{R}{R+R_i} - 1 = -\frac{R_i}{R + R_i}.$$

Ist $R_i$ klein gegen $R$, ist der Nenner ungefähr $R$.

**Allgemein.** Liegt der Strommesser in einem größeren Netz, steht an der Stelle von $R$ der Widerstand, den das übrige Netz zwischen den beiden
Anschlüssen des Strommessers bietet, wenn man die Quellen durch ihre Innenwiderstände ersetzt — das Bild der Ersatzquelle aus dem Artikel über die
Zusammenschaltung, ausgebaut im Artikel über [Ersatzquellen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html).
:::

::::beispiel Ein Strommesser im Kreis
Ein Strommesser mit $1\,\Omega$ Innenwiderstand misst den Strom einer Batterie von $4{,}5\,\text{V}$ durch einen Widerstand.

**(a) Bei 150 Ohm:**

$$I_R = \frac{4{,}5\,\text{V}}{150\,\Omega} = 30{,}0\,\text{mA}, \qquad I_R' = \frac{4{,}5\,\text{V}}{151\,\Omega} \approx 29{,}8\,\text{mA},$$

$0{,}66\,\%$ zu wenig, meist vernachlässigbar.

**(b) Bei 4,7 Ohm:**

$$I_R = \frac{4{,}5\,\text{V}}{4{,}7\,\Omega} \approx 957\,\text{mA}, \qquad I_R' = \frac{4{,}5\,\text{V}}{5{,}7\,\Omega} \approx 789\,\text{mA},$$

$17{,}5\,\%$ zu wenig. Bei kleinen Widerständen braucht man einen Strommesser mit viel kleinerem Innenwiderstand.

**Im Bild:** Eine kleine Uhr in einem dicken, weit offenen Rohr bremst viel mehr, als dieselbe Uhr in einem ohnehin engen.
::::

## Der Fehler der Spannungsmessung

**Die Akteure:** eine ideale Stromquelle $I_q$, die einen Lastwiderstand $R_L$ speist, die Spannung $U_L$ ohne und $U_L'$ mit Spannungsmesser, dessen
Innenwiderstand $R_i$ parallel zu $R_L$ liegt.

**Das Zusammenspiel:** *Wie viel kleiner wird die Spannung, weil der Spannungsmesser einen Teil des Stroms abzweigt?*

:::formel
$$U_L = I_q\,R_L, \qquad U_L' = I_q\,(R_L \parallel R_i) = U_L\cdot\frac{1}{1 + R_L/R_i}.$$
:::

**So liest man das:** Der Spannungsmesser ist ein zusätzlicher Strompfad parallel zur Last. Der Strom der Quelle teilt sich auf, durch die Last fließt
weniger, und die Spannung sinkt um den __Fehlerfaktor__ $\frac{1}{1+R_L/R_i}$; der relative Fehler ist ungefähr $-\frac{R_L}{R_i}$. Für einen kleinen Fehler
muss $R_i$ viel größer sein als $R_L$.

**Im Bild:** Ein dickes Nebenröhrchen zapft so viel Wasser ab, dass der Druckunterschied, den es messen soll, selbst sinkt.

:::herleitung
**Mit Stromquelle.** Ohne Spannungsmesser fließt der ganze Strom $I_q$ durch $R_L$. Mit Spannungsmesser liegen $R_L$ und $R_i$ parallel, und an beiden
liegt dieselbe Spannung:

$$U_L' = I_q\,\frac{R_L R_i}{R_L + R_i} = I_q\,R_L\cdot\frac{R_i}{R_L + R_i} = U_L\cdot\frac{1}{1 + R_L/R_i}.$$

**Allgemein.** Wie im Artikel über die Zusammenschaltung verhält sich jede Schaltung an zwei Messpunkten wie eine Quelle mit der Leerlaufspannung $U_0$ und
einem Innenwiderstand $R_\text{ers}$. Der Spannungsmesser ist für sie eine Last, und nach dem belasteten Spannungsteiler zeigt er

$$U' = U_0\,\frac{R_i}{R_i + R_\text{ers}}.$$

In der Schaltung mit Stromquelle ist $R_\text{ers}$ gerade $R_L$: Die ideale Stromquelle hat einen unendlich großen Innenwiderstand und trägt nichts bei.
:::

::::beispiel Zwei Spannungsmesser an derselben Stelle
**(a) Eine Stromquelle** von $0{,}5\,\text{mA}$ speist $10\,\text{k}\Omega$, ohne Messgerät liegen dort $5\,\text{V}$. Ein Digitalmultimeter mit
$10\,\text{M}\Omega$ und ein Zeigerinstrument mit $200\,\text{k}\Omega$ im $10$-V-Bereich zeigen:

$$U_L' = \frac{5\,\text{V}}{1 + 10\,\text{k}\Omega/10\,\text{M}\Omega} \approx 4{,}995\,\text{V}, \qquad U_L' = \frac{5\,\text{V}}{1 + 10\,\text{k}\Omega/200\,\text{k}\Omega} \approx 4{,}76\,\text{V}.$$

Das Multimeter liegt $0{,}1\,\%$ daneben, das Zeigerinstrument $4{,}8\,\%$.

**(b) Der Teiler aus dem Artikel über die Zusammenschaltung,** zweimal $4{,}7\,\text{k}\Omega$ an $10\,\text{V}$, hat die Leerlaufspannung $5\,\text{V}$ und den
Innenwiderstand $2{,}35\,\text{k}\Omega$. Dieselben beiden Geräte zeigen dort

$$U' = 5\,\text{V}\cdot\frac{200\,\text{k}\Omega}{202{,}35\,\text{k}\Omega} \approx 4{,}94\,\text{V}, \qquad U' = 5\,\text{V}\cdot\frac{10\,\text{M}\Omega}{10{,}00235\,\text{M}\Omega} \approx 4{,}999\,\text{V}.$$

Entscheidend ist nicht der Widerstand, an dem man misst, sondern der Innenwiderstand der Schaltung an den Messpunkten.

**Im Bild:** Dasselbe Nebenröhrchen stört eine Engstelle, die nur langsam nachliefern kann, mehr als eine, hinter der eine kräftige Pumpe sitzt.
::::

:::grafik
Szene: get1/strom-und-spannungsmessung/01-messfehler · Vorlage: messgeraet-belastung
Zwei Schaltbilder. Links eine Spannungsquelle $U$ mit Widerstand $R$ und einem Strommesser, gezeichnet als ideales
Amperemeter mit $R_i$ in Reihe in einem gestrichelten Kasten; ein Regler für $R_i$ lässt den Strom $I_R'$ gegenüber $I_R$ sinken, ein Balken zeigt den
relativen Fehler $-R_i/(R+R_i)$. Rechts eine Stromquelle $I_q$ mit Last $R_L$ und einem Spannungsmesser, gezeichnet als ideales Voltmeter mit $R_i$
parallel; animierte Ladungen zweigen durch $R_i$ ab, $U_L'$ sinkt gegenüber $U_L$, ein Balken zeigt den Fehlerfaktor $1/(1+R_L/R_i)$. Kernaussage: Der
Strommesser fügt einen Widerstand in den Weg ein, der Spannungsmesser einen Weg neben die Last. (Rot = Messgeräte und Innenwiderstände, blau = Ströme
und Spannungen, orange = Fehlerbalken, grau = Quellen und Leitungen.)
:::

## Strom und Spannung zugleich messen

Will man den Widerstand $R$ eines Bauteils aus Spannung und Strom bestimmen, braucht man beide Geräte gleichzeitig. Dann misst eines von ihnen
zwangsläufig auch das andere mit:

- Bei der __stromrichtigen Messung__ liegt der Strommesser direkt in Reihe mit $R$, der Spannungsmesser über beiden. Der Strom stimmt, die Spannung
  enthält zusätzlich den Abfall am Strommesser.
- Bei der __spannungsrichtigen Messung__ liegt der Spannungsmesser direkt an $R$, der Strommesser davor. Die Spannung stimmt, der Strom enthält
  zusätzlich den Strom durch den Spannungsmesser.

Mit $R_{IA}$ für den Innenwiderstand des Strommessers und $R_{IV}$ für den des Spannungsmessers ist der Quotient der Anzeigen jeweils ein anderer
Widerstand als $R$:

:::formel
$$\frac{U}{I} = R + R_{IA} \quad\text{(stromrichtig)}, \qquad \frac{U}{I} = R \parallel R_{IV} \quad\text{(spannungsrichtig)}.$$
:::

**So liest man das:** Stromrichtig misst man den Widerstand samt Strommesser, also etwas zu viel; spannungsrichtig den Widerstand parallel zum
Spannungsmesser, also etwas zu wenig. Mit den Anzeigen allein kann man Strom und Spannung deshalb nicht zugleich exakt messen. Kennt man aber die
Innenwiderstände, rechnet man den Fehler heraus:

$$R = \frac{U}{I} - R_{IA} \quad\text{(stromrichtig)}, \qquad R = \frac{U}{I - U/R_{IV}} \quad\text{(spannungsrichtig)}.$$

**Im Bild:** Misst man Durchfluss und Druckunterschied an derselben Engstelle zugleich, sieht entweder das Nebenröhrchen die Wasseruhr mit, oder die
Wasseruhr zählt das Wasser im Nebenröhrchen mit.

:::herleitung
**Stromrichtig.** Durch $R$ und den Strommesser fließt derselbe Strom $I$. Der Spannungsmesser liegt über beiden, nach der Maschenregel misst er die Summe
der Spannungen:

$$U = U_R + U_{IA} = R\,I + R_{IA}\,I, \qquad \frac{U}{I} = R + R_{IA}.$$

**Spannungsrichtig.** An $R$ und dem Spannungsmesser liegt dieselbe Spannung $U$. Der Strommesser misst nach der Knotenregel die Summe beider Ströme:

$$I = I_R + I_{IV} = \frac{U}{R} + \frac{U}{R_{IV}}, \qquad \frac{U}{I} = R \parallel R_{IV}.$$

**Korrektur.** Die erste Gleichung nach $R$ aufgelöst gibt die stromrichtige Korrektur. In der zweiten zieht man vom gemessenen Strom den Strom durch den
Spannungsmesser ab und teilt die Spannung durch den Rest.
:::

**Welche Schaltung?** Der relative Fehler der stromrichtigen Messung ist $\frac{R_{IA}}{R}$, der der spannungsrichtigen ungefähr $\frac{R}{R_{IV}}$. Für
große Widerstände ist die stromrichtige besser, für kleine die spannungsrichtige. Gleich groß sind beide Fehler beim __Grenzwiderstand__:

$$R_\text{G} = \sqrt{R_{IA}\,R_{IV}}.$$

:::herleitung
Stromrichtig ist der Messwert $R+R_{IA}$, der relative Fehler also $\frac{R_{IA}}{R}$. Spannungsrichtig ist der Messwert $\frac{R}{1+R/R_{IV}}$; für $R$ klein
gegen $R_{IV}$ ist das ungefähr $R\,(1-R/R_{IV})$, der relative Fehler also ungefähr $-\frac{R}{R_{IV}}$. Die Beträge sind gleich, wenn

$$\frac{R_{IA}}{R} = \frac{R}{R_{IV}}, \qquad R^2 = R_{IA}\,R_{IV}.$$

Oberhalb davon ist der Fehler der stromrichtigen Messung kleiner, unterhalb der der spannungsrichtigen.
:::

::::beispiel Stromrichtig oder spannungsrichtig?
Strommesser mit $1\,\Omega$, Spannungsmesser mit $10\,\text{M}\Omega$. Der Grenzwiderstand:

$$R_\text{G} = \sqrt{1\,\Omega\cdot10^{7}\,\Omega} \approx 3{,}2\,\text{k}\Omega.$$

**(a) Ein Widerstand von 100 Ohm** liegt darunter:

$$\text{stromrichtig: } 101\,\Omega\ (+1\,\%), \qquad \text{spannungsrichtig: } 99{,}999\,\Omega\ (-0{,}001\,\%).$$

**(b) Ein Widerstand von 1 Megaohm** liegt weit darüber:

$$\text{stromrichtig: } 1{,}000001\,\text{M}\Omega\ (+0{,}0001\,\%), \qquad \text{spannungsrichtig: } 909{,}1\,\text{k}\Omega\ (-9{,}1\,\%).$$

Wer die falsche Schaltung nimmt, kann mit der Korrekturformel trotzdem den richtigen Wert zurückrechnen, etwa im Fall (b) spannungsrichtig:

$$R = \frac{U}{I - U/R_{IV}}, \qquad \frac{1}{909{,}1\,\text{k}\Omega} - \frac{1}{10\,\text{M}\Omega} = \frac{1}{1\,\text{M}\Omega}.$$

**Im Bild:** An einer weiten Engstelle stört die Wasseruhr im Weg kaum, an einer sehr engen stört das Nebenröhrchen kaum.
::::

## Widerstandsmessung im Multimeter

Ein Digitalmultimeter misst Widerstände ohne Strommesser. Es schickt einen genau bekannten Strom $I_q$ aus einer
__Konstantstromquelle__ durch den Widerstand und misst nur die Spannung:

$$R = \frac{U}{I_q}.$$

**So liest man das:** Weil $I_q$ in jedem Messbereich eine glatte Zehnerpotenz ist, ist die angezeigte Spannung schon der Widerstandswert; das Gerät
setzt nur Komma und Vorsatz (Milli, Kilo, Mega) dazu. Ein Strommesser entfällt, und mit ihm sein Fehler; der Spannungsmesser mit seinen $10\,\text{M}\Omega$
zweigt bei gewöhnlichen Widerständen fast nichts ab.

**Im Bild:** Eine Pumpe, die einen genau bekannten Durchfluss erzwingt, gleich wie eng es wird. Der Druckunterschied an der Engstelle verrät dann
unmittelbar, wie eng sie ist.

:::herleitung
Die Konstantstromquelle erzwingt den Strom $I_q$ unabhängig vom Widerstand. Am Widerstand liegt nach Ohm die Spannung $R\,I_q$; aufgelöst nach $R$ folgt die
Formel. Ist $I_q$ zum Beispiel $1\,\text{mA}$, entspricht $1\,\text{V}$ gerade $1\,\text{k}\Omega$.
:::

**Kleine Widerstände und die Vierleitermessung.** Bei kleinen Widerständen verfälschen die Messleitungen und Kontakte das Ergebnis, denn ihr Widerstand
liegt in Reihe: Das Gerät misst die Spannung an seinen eigenen Buchsen, und dort fällt auch die Spannung an den Leitungen ab. Abhilfe schafft die
__Vierleitermessung__ (nach Kelvin): Zwei Leitungen führen den Strom, zwei getrennte Leitungen greifen die Spannung
direkt am Widerstand ab. Durch die Spannungsleitungen fließt wegen des großen Innenwiderstands des Spannungsmessers fast kein Strom, an ihnen fällt also
fast nichts ab.

:::herleitung
**Zweileiter.** Die beiden Zuleitungen mit je $R_\text{Ltg}$ liegen in Reihe mit $R$, durch alle fließt $I_q$, und gemessen wird die Summe der Spannungen:

$$\frac{U}{I_q} = R + 2\,R_\text{Ltg}.$$

**Vierleiter.** Die Spannungsleitungen tragen nur den Strom des Spannungsmessers, ungefähr $U/R_i$. An ihnen fällt deshalb nur $R_\text{Ltg}\,U/R_i$ ab,
bei einem Spannungsmesser von $10\,\text{M}\Omega$ und Leitungen von Bruchteilen eines Ohms weit weniger als ein Millionstel der Messspannung.
:::

::::beispiel Ein Ohm, zwei Leitungen, vier Leitungen
**(a) Das Prinzip.** Im $2$-k$\Omega$-Bereich schickt ein Multimeter $1\,\text{mA}$ durch einen Widerstand von $1{,}234\,\text{k}\Omega$:

$$U = 1{,}234\,\text{k}\Omega\cdot1\,\text{mA} = 1{,}234\,\text{V},$$

und angezeigt wird „1,234 kΩ".

**(b) Ein Widerstand von 1 Ohm** wird mit $10\,\text{mA}$ gemessen; Leitung und Kontakt haben auf jeder Seite zusammen $0{,}15\,\Omega$. Zweileiter:

$$\frac{U}{I_q} = 1\,\Omega + 2\cdot0{,}15\,\Omega = 1{,}30\,\Omega,$$

$30\,\%$ zu viel. Vierleiter: Durch die Spannungsleitungen fließen bei $10\,\text{mV}$ und $10\,\text{M}\Omega$ nur

$$\frac{10\,\text{mV}}{10\,\text{M}\Omega} = 1\,\text{nA},$$

an $0{,}15\,\Omega$ also $0{,}15\,\text{nV}$. Angezeigt wird $1{,}000\,\Omega$.

**Im Bild:** Den Druck misst man mit eigenen Röhrchen direkt an der Engstelle, nicht am Anfang der Zuleitung.
::::

## Den Messbereich eines Strommessers erweitern

Ein __Drehspulinstrument__, das klassische Zeigerinstrument, schlägt bei einem bestimmten Strom voll aus, zum Beispiel bei $100\,\mu\text{A}$. Für
größere Ströme legt man einen __Nebenwiderstand__ (englisch shunt) $R_\text{Shunt}$ parallel zum Messwerk. Er übernimmt den Überschuss, und durch
das Messwerk fließt ein fester Bruchteil des Stroms:

:::formel
$$R_\text{Shunt} = R_{iA}\,\frac{I_{iA}}{I - I_{iA}} = \frac{R_{iA}}{n - 1}, \qquad n = \frac{I}{I_{iA}}.$$
:::

**So liest man das:** $R_{iA}$ ist der Innenwiderstand des Messwerks, $I_{iA}$ sein Vollausschlag, $I$ der neue Vollausschlag und $n$ der Faktor der
Erweiterung. Für die zehnfache Erweiterung muss der Nebenwiderstand ein Neuntel des Messwerkwiderstands haben. Mehrere Bereiche
baut man schrittweise: Für den nächsten Bereich zählt die schon vorhandene Parallelschaltung als Messwerk.

**Im Bild:** Eine Umgehungsleitung neben der Wasseruhr, so bemessen, dass die Uhr genau ein $n$-tel des Durchflusses sieht.

:::herleitung
Messwerk und Nebenwiderstand liegen parallel; nach dem Stromteiler fließt durch das Messwerk der Anteil

$$\frac{I_{iA}}{I} = \frac{R_\text{Shunt}}{R_\text{Shunt} + R_{iA}} = \frac{G_{iA}}{G_\text{Shunt} + G_{iA}}.$$

Über Kreuz multipliziert und nach $R_\text{Shunt}$ sortiert:

$$I_{iA}\,(R_\text{Shunt} + R_{iA}) = I\,R_\text{Shunt}, \qquad R_\text{Shunt}\,(I - I_{iA}) = I_{iA}\,R_{iA}.$$

Teilen durch $I-I_{iA}$ gibt die erste Form; Zähler und Nenner durch $I_{iA}$ geteilt die zweite.

**Bürdenspannung.** Die Parallelschaltung hat den Widerstand $R_{iA}/n$, denn ihr Leitwert ist $n$-mal so groß wie der des Messwerks. Bei Vollausschlag
fällt an ihr deshalb immer dieselbe Spannung ab, in jedem Bereich:

$$I\,\frac{R_{iA}}{n} = I_{iA}\,R_{iA}.$$
:::

::::beispiel Ein Strommesser mit drei Bereichen
Ein Messwerk mit $50\,\mu\text{A}$ Vollausschlag und $2\,\text{k}\Omega$ Innenwiderstand soll durch zugeschaltete Nebenwiderstände bis $1$, $10$ und
$100\,\text{mA}$ messen. Erster Bereich, Erweiterung um $20$:

$$R_1 = \frac{2\,\text{k}\Omega}{20 - 1} \approx 105{,}3\,\Omega, \qquad R_{iA} \parallel R_1 = 100\,\Omega.$$

Für den zweiten Bereich ist die Parallelschaltung mit $100\,\Omega$ und $1\,\text{mA}$ das neue Messwerk, Erweiterung um $10$, und ebenso für den dritten:

$$R_2 = \frac{100\,\Omega}{10 - 1} \approx 11{,}11\,\Omega, \qquad R_3 = \frac{10\,\Omega}{10 - 1} \approx 1{,}111\,\Omega.$$

Die Parallelschaltungen haben $100\,\Omega$, $10\,\Omega$ und $1\,\Omega$, und bei Vollausschlag fallen in jedem Bereich $50\,\mu\text{A}\cdot2\,\text{k}\Omega$,
also $0{,}1\,\text{V}$, ab.

**Im Bild:** Immer breitere Umgehungsleitungen neben derselben kleinen Uhr; an der Gesamtanordnung fällt bei Vollausschlag stets derselbe Druck ab.
::::

## Den Messbereich eines Spannungsmessers erweitern

Ein Zeigerinstrument mit dem Vollausschlag $I_{iA}$ und dem Innenwiderstand $R_i$ ist auch ein Spannungsmesser mit dem kleinen Bereich $I_{iA}R_i$. Für
größere Spannungen schaltet man einen __Vorwiderstand__ $R_V$ in Reihe. Er nimmt den Überschuss der Spannung auf, und am Messwerk
liegt ein fester Bruchteil:

:::formel
$$R_V = R_i\,(\alpha - 1), \qquad \alpha = \frac{U_{V,\text{max,neu}}}{U_{V,\text{max,alt}}}.$$
:::

**So liest man das:** $\alpha$ ist der Faktor der Erweiterung. Für die zehnfache Erweiterung braucht man das Neunfache des
Innenwiderstands in Reihe. Auch hier baut man mehrere Bereiche schrittweise; für den nächsten Bereich zählt die vorhandene Reihe als Messwerk.

**Im Bild:** Eine Engstelle vor dem Nebenröhrchen, die den größten Teil des Druckunterschieds aufnimmt, so dass auf die kleine Uhr nur ein Bruchteil wirkt.

:::herleitung
Messwerk und Vorwiderstand bilden einen unbelasteten Spannungsteiler:

$$U_M = U\,\frac{R_i}{R_i + R_V}.$$

Bei Vollausschlag soll am Messwerk die alte Grenze $U_{V,\text{max,alt}}$ liegen, wenn außen die neue Grenze $\alpha\,U_{V,\text{max,alt}}$ anliegt:

$$\frac{R_i}{R_i + R_V} = \frac{1}{\alpha}, \qquad R_i + R_V = \alpha\,R_i, \qquad R_V = R_i\,(\alpha - 1).$$

**Ohm pro Volt.** Durch das Messwerk fließt bei Vollausschlag in jedem Bereich derselbe Strom $I_{iA}$, also ist der Gesamtwiderstand im Bereich $U_\text{max}$
gerade $U_\text{max}/I_{iA}$. Pro Volt Messbereich ist das stets dasselbe:

$$\frac{R_i + R_V}{U_\text{max}} = \frac{1}{I_{iA}}.$$

Auf Zeigerinstrumenten steht diese Angabe in Ohm pro Volt; je größer sie ist, desto weniger belastet das Gerät die Schaltung.
:::

::::beispiel Dasselbe Messwerk als Spannungsmesser
Das Messwerk mit $50\,\mu\text{A}$ und $2\,\text{k}\Omega$ hat als Spannungsmesser den Bereich

$$U_{V,\text{max}} = 50\,\mu\text{A}\cdot2\,\text{k}\Omega = 0{,}1\,\text{V}.$$

Für $1$, $10$ und $100\,\text{V}$ ist jeweils um $\alpha$ gleich $10$ zu erweitern:

$$R_1 = 2\,\text{k}\Omega\cdot9 = 18\,\text{k}\Omega, \qquad R_2 = 20\,\text{k}\Omega\cdot9 = 180\,\text{k}\Omega, \qquad R_3 = 200\,\text{k}\Omega\cdot9 = 1{,}8\,\text{M}\Omega.$$

Die Gesamtwiderstände sind $20\,\text{k}\Omega$, $200\,\text{k}\Omega$ und $2\,\text{M}\Omega$, in jedem Bereich

$$\frac{1}{50\,\mu\text{A}} = 20\,\frac{\text{k}\Omega}{\text{V}}.$$

Im $10$-V-Bereich hat dieses Instrument also die $200\,\text{k}\Omega$, mit denen es weiter oben den Spannungsteiler um $1{,}2\,\%$ belastet hat; ein
Digitalmultimeter mit $10\,\text{M}\Omega$ in jedem Bereich stört fünfzigmal weniger.

**Im Bild:** Vor dasselbe Nebenröhrchen kommen immer längere Engstellen; durch die kleine Uhr fließt bei Vollausschlag immer derselbe Strom.
::::

:::grafik
Szene: get1/strom-und-spannungsmessung/01-messbereiche · Vorlage: shunt-vorwiderstand
Links das Messwerk (Kreis mit A, $R_{iA}=2\,\text{k}\Omega$, $50\,\mu\text{A}$) mit drei zuschaltbaren Nebenwiderständen $R_1$, $R_2$, $R_3$ parallel; ein Bereichsschalter $1$, $10$, $100\,\text{mA}$, eine Stromaufteilung als Pfeilbreiten, die
Bürdenspannung $0{,}1\,\text{V}$ bleibt eingeblendet. Rechts dasselbe Messwerk mit drei Vorwiderständen $R_1$, $R_2$, $R_3$ in Reihe, die je ein Schalter
überbrückt, für $1$, $10$, $100\,\text{V}$; ein Potenzialbalken zeigt, wie sich die Spannung aufteilt, und die Anzeige „$20\,\text{k}\Omega/\text{V}$"
bleibt stehen. Kernaussage: Ein Nebenwiderstand teilt den Strom, ein Vorwiderstand die Spannung — beides sind die Teilerregeln. (Rot = Messwerk, blau =
Ströme und Spannungen, orange = Zusatzwiderstände, grau = Schalter und Leitungen.)
:::

## Bedeutung und Ausblick

Jede Messung ist ein Eingriff, und der Innenwiderstand sagt, wie groß er ist. Mit den Formeln dieses Artikels lässt sich der Eingriff abschätzen und, wo
nötig, herausrechnen: Ein Strommesser vergrößert den Widerstand des Kreises um $R_i$, ein Spannungsmesser belastet die Schaltung wie eine Last am
Spannungsteiler. Dasselbe Prinzip steckt in jedem Tastkopf eines Oszilloskops: Ein Tastkopf „$10:1$" ist ein Vorwiderstand von $9\,\text{M}\Omega$ vor dem
Eingang mit $1\,\text{M}\Omega$, er teilt die Spannung durch zehn und belastet die Schaltung nur noch mit $10\,\text{M}\Omega$.

Der nächste Artikel zeigt einen Weg, den Eingriff ganz zu vermeiden: die __Wheatstonesche Messbrücke__. Sie vergleicht zwei Spannungsteiler und gleicht
ab, bis durch das Messgerät kein Strom mehr fließt. Dann spielt sein Innenwiderstand keine Rolle mehr. Der Artikel über
[Ersatzquellen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html) baut das Bild aus, nach dem sich jede
Schaltung an zwei Klemmen wie eine Quelle mit Innenwiderstand verhält — genau das Bild, mit dem sich hier der Fehler eines Spannungsmessers in beliebigen
Schaltungen berechnen ließ.

:::kern
- Ein Messgerät ist selbst ein Bauteil; sein __Innenwiderstand__ $R_i$ bestimmt, wie stark es die Messung verfälscht.
- __Strommesser__: in Reihe, $R_i$ klein, ideal null — er verhält sich wie ein Stück Draht. Nie parallel zu einer Quelle anschließen.
- __Spannungsmesser__: parallel, $R_i$ groß, ideal unendlich — er verhält sich wie eine Unterbrechung.
- Fehler der Strommessung: Der Strom sinkt um den Faktor $\frac{R}{R+R_i}$.
- Fehler der Spannungsmessung: $U'=U_0\,\frac{R_i}{R_i+R_\text{ers}}$ mit dem Innenwiderstand der Schaltung an den Messpunkten.
- Zugleich gemessen ist stromrichtig der Strom exakt, spannungsrichtig die Spannung; der Fehler lässt sich mit den Innenwiderständen herausrechnen.
- Grenzwiderstand $\sqrt{R_{IA}R_{IV}}$: darüber stromrichtig, darunter spannungsrichtig messen.
- Ein Multimeter misst Widerstände mit Konstantstrom und Spannungsmesser; kleine Widerstände mit vier Leitungen.
- __Nebenwiderstand__ für den Strommesser: $R_\text{Shunt}=\frac{R_{iA}}{n-1}$, ein Stromteiler mit konstanter Bürdenspannung.
- __Vorwiderstand__ für den Spannungsmesser: $R_V=R_i\,(\alpha-1)$, ein Spannungsteiler mit konstanten Ohm pro Volt.
:::

:::quiz
F: Warum braucht ein Strommesser einen kleinen und ein Spannungsmesser einen großen Innenwiderstand?
A: Der Strommesser liegt in Reihe im Zweig; an ihm fällt die Spannung $R_i\,I$ ab, die dem Kreis fehlt, und nur bei $R_i$ gleich null stört er nicht. Der Spannungsmesser liegt parallel und zieht den Strom $U/R_i$, der der Last fehlt; nur bei unendlichem $R_i$ stört er nicht. Im Wasserbild: Die Uhr im Rohr soll nicht bremsen, das Nebenröhrchen nichts abzweigen.
F: Wie groß ist der Fehler eines Strommessers mit $1\,\Omega$ an $4{,}5\,\text{V}$ und $4{,}7\,\Omega$, und warum so groß?
A: Ohne Messgerät flössen $957\,\text{mA}$, mit ihm hat der Kreis $5{,}7\,\Omega$ und es fließen nur $789\,\text{mA}$, $17{,}5\,\%$ weniger. Der relative Fehler ist $\frac{R_i}{R+R_i}$; bei einem kleinen Widerstand im Kreis fällt der Innenwiderstand stark ins Gewicht. An $150\,\Omega$ wären es nur $0{,}66\,\%$.
F: Was hängt beim Spannungsmessen vom Messgerät ab und was von der Schaltung?
A: Der Spannungsmesser zeigt $U_0\,\frac{R_i}{R_i+R_\text{ers}}$: Sein Innenwiderstand $R_i$ steht dem Innenwiderstand $R_\text{ers}$ der Schaltung an den Messpunkten gegenüber. In der Schaltung mit Stromquelle ist $R_\text{ers}$ gleich $R_L$; am Teiler aus zweimal $4{,}7\,\text{k}\Omega$ sind es $2{,}35\,\text{k}\Omega$, und ein Zeigerinstrument mit $200\,\text{k}\Omega$ zeigt dort $4{,}94$ statt $5\,\text{V}$.
F: Eine Stromquelle mit $1\,\mu\text{A}$ speist $1\,\text{M}\Omega$, gemessen wird mit einem Spannungsmesser von $10\,\text{M}\Omega$. Was zeigt er, und wie groß ist der Fehler?
A: Ohne Messgerät liegen $1\,\mu\text{A}\cdot1\,\text{M}\Omega = 1\,\text{V}$ an. Der Fehlerfaktor $\frac{1}{1+R_L/R_i}$ ist $\frac{1}{1{,}1}$; angezeigt werden $0{,}9091\,\text{V}$, rund $9\,\%$ zu wenig. Der Innenwiderstand des Spannungsmessers ist zwar zehnmal so groß wie $R_L$, für einen kleinen Fehler aber nicht groß genug.
F: Was misst man stromrichtig und spannungsrichtig, und wie bekommt man trotzdem den genauen Widerstand?
A: Stromrichtig liegt der Strommesser direkt in Reihe mit $R$, der Quotient der Anzeigen ist $R+R_{IA}$. Spannungsrichtig liegt der Spannungsmesser direkt an $R$, der Quotient ist $R\parallel R_{IV}$. Mit bekannten Innenwiderständen rechnet man zurück: $R=\frac UI-R_{IA}$ bzw. $R=\frac{U}{I-U/R_{IV}}$.
F: Woher kommt der Grenzwiderstand $\sqrt{R_{IA}R_{IV}}$, und was sagt er?
A: Der relative Fehler ist stromrichtig $\frac{R_{IA}}{R}$, spannungsrichtig ungefähr $\frac{R}{R_{IV}}$; gleich sind beide bei $R^2=R_{IA}R_{IV}$. Darüber misst man stromrichtig, darunter spannungsrichtig. Mit $1\,\Omega$ und $10\,\text{M}\Omega$ liegt die Grenze bei rund $3{,}2\,\text{k}\Omega$: $100\,\Omega$ spannungsrichtig, $1\,\text{M}\Omega$ stromrichtig.
F: Wie misst ein Digitalmultimeter einen Widerstand, und warum braucht man für kleine Widerstände vier Leitungen?
A: Es schickt einen bekannten Strom in Zehnerpotenzen durch den Widerstand und misst nur die Spannung; die Anzeige ist dann schon der Widerstandswert. Bei zwei Leitungen misst es den Spannungsabfall an Leitungen und Kontakten mit, bei $1\,\Omega$ und je $0{,}15\,\Omega$ Zuleitung $1{,}30\,\Omega$. Bei vier Leitungen greifen eigene Leitungen die Spannung direkt ab; durch sie fließt nur etwa $1\,\text{nA}$, und der Wert stimmt.
F: Wie berechnet man den Nebenwiderstand für einen Strommesser, und was bleibt in allen Bereichen gleich?
A: Nach dem Stromteiler soll durch das Messwerk der Anteil $\frac{I_{iA}}{I}$ fließen; daraus folgt $R_\text{Shunt}=R_{iA}\frac{I_{iA}}{I-I_{iA}}=\frac{R_{iA}}{n-1}$. Die Parallelschaltung hat $R_{iA}/n$, also fällt bei Vollausschlag stets $I_{iA}R_{iA}$ ab, beim Messwerk mit $50\,\mu\text{A}$ und $2\,\text{k}\Omega$ in jedem Bereich $0{,}1\,\text{V}$.
F: Wie berechnet man den Vorwiderstand für einen Spannungsmesser, und was bedeutet die Angabe Ohm pro Volt?
A: Messwerk und Vorwiderstand bilden einen Spannungsteiler, der bei Vollausschlag um den Faktor $\alpha$ teilen soll: $R_i+R_V=\alpha R_i$, also $R_V=R_i(\alpha-1)$. Weil bei Vollausschlag in jedem Bereich derselbe Strom $I_{iA}$ fließt, ist der Gesamtwiderstand pro Volt Bereich stets $\frac{1}{I_{iA}}$, beim Messwerk mit $50\,\mu\text{A}$ also $20\,\text{k}\Omega/\text{V}$.
F: Warum belastet ein Zeigerinstrument mit $20\,\text{k}\Omega/\text{V}$ eine Schaltung im $10$-V-Bereich stärker als ein Digitalmultimeter?
A: Es hat in diesem Bereich $200\,\text{k}\Omega$, das Multimeter in jedem Bereich $10\,\text{M}\Omega$, fünfzigmal mehr. Am Teiler mit $2{,}35\,\text{k}\Omega$ Innenwiderstand zeigt das Zeigerinstrument deshalb $1{,}2\,\%$ zu wenig, das Multimeter nur $0{,}02\,\%$.
:::
