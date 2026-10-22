---
title: Ersatzquellen – Thévenin und Norton
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70500
summary: Von Grund auf – warum sich jedes lineare Netz an zwei Klemmen wie eine einzige reale Quelle verhält und wie man diese Ersatzquelle findet. Leitbild ist das Wassernetz einer Stadt hinter dem Hahn: Zwei Messungen am Hahn genügen, und ein einziger Ersatzturm mit Ersatzleitung ersetzt das ganze Netz. Mit Eintor und Kennlinie, dem Satz von der Ersatzspannungs- und Ersatzstromquelle samt Beweis aus der Linearität, Leerlauf- und Kurzschlussversuch, zwei Belastungsfällen, dem Stilllegen der Quellen, Netzen mit mehreren Quellen, den Grenzen der Äquivalenz und der Wahl zwischen Spannungs- und Stromform. Mit Beispiel-Seite.
tags: Ersatzspannungsquelle, Ersatzstromquelle, Thévenin, Norton, Leerlaufspannung, Kurzschlussstrom, Innenwiderstand
---

## Anschaulich

Wer etwas an zwei Klemmen einer Schaltung anschließt, einen Verbraucher, ein Messgerät oder eine weitere Schaltung, den interessiert meist nicht, was
hinter den Klemmen steckt. Wichtig ist nur, wie Spannung und Strom an ihnen zusammenhängen. Für jedes lineare Netz aus Widerständen und Quellen, so
verwickelt es sein mag, genügen dafür zwei Zahlen: Von den Klemmen aus ist es eine einzige reale Quelle, seine __Ersatzquelle__.

**Das Leitbild dieses Artikels:** **Das Wassernetz hinter dem Hahn.** Es setzt das Bild des vorigen Artikels fort, in dem ein Wasserturm die
Spannungsquelle und eine Spritzenpumpe die Stromquelle war. Hinter dem Hahn einer Wohnung hängt das Versorgungsnetz einer ganzen Stadt: mehrere Türme,
Pumpen, die mit festem Durchfluss einspeisen, Rohre aller Weiten, Abzweige und Ringleitungen.

Wir nehmen Rohre an, in denen der Druckverlust proportional zum Durchfluss wächst; so verhält sich langsame, gleichmäßige Strömung in engen Rohren. Dann
ist das Wassernetz das genaue Gegenstück eines linearen elektrischen Netzes: Druck entspricht Spannung, Durchfluss Strom, ein Rohr einem Widerstand.

Am Hahn misst man von all dem nur zwei Größen, Druck und Durchfluss. Drei Folgerungen:

- **Zwei Messungen genügen.** Bei geschlossenem Hahn zeigt das Manometer, ein Druckmesser, den Ruhedruck, bei ganz offenem Hahn die Wasseruhr den
  größten Durchfluss.
  Weil alle Rohre linear sind, liegen alle anderen Betriebspunkte auf der Geraden zwischen diesen beiden.
- **Ein Ersatzturm tut es auch.** Ein einziger Turm, dessen Druck gleich dem Ruhedruck ist, mit einer Zuleitung, die gerade den größten Durchfluss
  durchlässt, liefert bei jedem Verbrauch dasselbe wie das ganze Netz — ebenso eine einzige Pumpe mit passendem Leck.
- **Die Ersatzleitung zeigt sich im stillgelegten Netz.** Senkt man alle Türme auf Höhe null, sind sie nur noch Rohrstücke; hält man alle Pumpen an,
  sperren ihre stehenden Kolben. Der Widerstand, den das so stillgelegte Netz Wasser entgegensetzt, das man in den Hahn hineindrückt, ist der Widerstand
  der Ersatzleitung.

:::grafik
Szene: get1/analyse-linearer-netzwerke/02-wassernetz · Vorlage: wassernetz-ersatzturm
Links ein Stadtplan des Wassernetzes: zwei Türme, eine Spritzenpumpe, Rohre unterschiedlicher Weite mit einer Ringleitung; rechts die Wohnung mit Hahn,
Manometer, Wasseruhr und Rücklauf. Ein Regler öffnet den Hahn vom geschlossenen bis zum ganz offenen Zustand, und ein Diagramm Druck über Durchfluss
zeichnet die Betriebspunkte mit, die auf einer fallenden Geraden liegen. Ein Knopf „ersetzen" blendet das Stadtnetz aus und an seiner Stelle einen
einzigen Ersatzturm mit Ersatzleitung ein, ein zweiter Knopf eine Ersatzpumpe mit Leck; der Regler läuft weiter, und die Punkte bleiben auf derselben
Geraden. Ein dritter Knopf „stilllegen" senkt die Türme auf Höhe null und hält die Pumpe an, deren Kolben nun sperrt; eine Testpumpe am Hahn drückt
Wasser hinein, und eine Anzeige zeigt den Widerstand der Ersatzleitung. Kernaussage: Von außen ist das ganze Netz eine einzige reale Quelle, festgelegt
durch Ruhedruck und größten Durchfluss. (Blau = Wasser und Kennlinie, rot = Türme, Pumpen und Ersatzquelle, orange = Ersatzleitung und Leck, grau =
Rohrnetz und Gebäude.)
:::

## Eintor, Klemmen und Kennlinie

Ein __Eintor__, auch __Zweipol__ genannt, ist ein Netzwerk mit genau zwei Anschlüssen nach außen, den __Klemmen__ A und B. Zusammen bilden sie ein
__Tor__: Was durch die eine Klemme hineinfließt, fließt durch die andere wieder heraus. Deshalb beschreibt ein einziger Strom, was durch das Tor fließt.

Wie im vorigen Artikel zählen wir den __Klemmenstrom__ $I_A$ aus der Klemme A heraus und die __Klemmenspannung__ $U_{AB}$ von A nach B.
Das ist das Generatorzählpfeilsystem aus dem Artikel über Zählpfeile: Das Produkt aus $U_{AB}$ und $I_A$ ist die Leistung, die das Eintor
abgibt.

Ein Eintor heißt __linear__, wenn es nur aus ohmschen Widerständen und idealen Quellen besteht. Es heißt __aktiv__, wenn Quellen darin wirken, und
__passiv__, wenn es keine enthält. Streng mathematisch ist ein aktives Netz nicht linear, sondern __affin__, also linear bis auf feste Zusatzbeiträge der
Quellen; in der Netzwerkanalyse nennt man es trotzdem linear.

Die __Kennlinie__ des Eintors ist die Gesamtheit aller Paare aus Klemmenstrom und Klemmenspannung, die sich bei irgendeiner äußeren Beschaltung
einstellen können. Mehr erfährt die Außenwelt nicht: Zwei Eintore mit derselben Kennlinie sind __äquivalent__, keine angeschlossene Schaltung kann sie
unterscheiden. Mit diesem Begriff hat der vorige Artikel reale Spannungs- und Stromquellen ineinander umgerechnet.

**Im Bild:** Das Eintor ist das ganze Stadtnetz; seine Klemmen sind der Hahn und der Rücklauf, über den das Wasser ins Netz zurückkehrt. Druck und
Durchfluss am Hahn sind alles, was die Wohnung vom Netz merkt.

:::herleitung
**Ein Strom für das ganze Tor.** Man schreibt die Knotenregel für jeden Knoten im Inneren des Eintors auf, alle Ströme als herausfließend gezählt, und
addiert alle diese Gleichungen. Jeder innere Zweig verbindet zwei innere Knoten; sein Strom fließt aus dem einen heraus und in den anderen hinein und
hebt sich in der Summe weg. Übrig bleiben nur die beiden Anschlussleitungen, mit $I_B$ als dem Strom, der aus B herausfließt:

$$I_A + I_B = 0.$$

Das ist die Knotenregel für eine Hülle um das ganze Netz: Im Inneren sammelt sich keine Ladung an, und was aus A herausfließt, fließt in B hinein. Im
Bild: Was aus dem Hahn läuft, kommt über den Rücklauf zurück.
:::

## Der Satz von der Ersatzquelle

**Die Akteure:**

- ein lineares aktives Eintor mit den Klemmen A und B. In ihm wirken Widerstände, ideale Spannungsquellen mit den Quellenspannungen
  $U_{q1}, U_{q2}, \dots$ und ideale Stromquellen mit den Quellströmen $I_{q1}, I_{q2}, \dots$; die Innenwiderstände realer Quellen zählen einfach zu
  den Widerständen;
- seine __Leerlaufspannung__ $U_{LL}$, die Klemmenspannung bei offenen Klemmen, und sein __Kurzschlussstrom__ $I_{KS}$, der Klemmenstrom bei
  kurzgeschlossenen Klemmen;
- die __Ersatzspannungsquelle__, eine ideale Spannungsquelle $U_i$ mit dem __Innenwiderstand__ $R_i$ in Reihe, und die __Ersatzstromquelle__, eine
  ideale Stromquelle $I_i$ mit dem __Innenleitwert__ $G_i$ parallel, beide mit den Zählpfeilen von $I_A$ und $U_{AB}$.

Spannungen werden in Volt gemessen, Ströme in Ampere, Widerstände in Ohm und Leitwerte in Siemens, dem Kehrwert des Ohm.

**Das Zusammenspiel:** *Lässt sich jedes solche Netz an seinen Klemmen durch eine einzige reale Quelle ersetzen, und durch welche?*

Ja. Gleichgültig, wie das Eintor innen aufgebaut ist, seine Kennlinie ist die einer realen Quelle:

:::formel Satz
$$U_{AB} = U_i - R_i\,I_A, \qquad I_A = I_i - G_i\,U_{AB},$$

$$U_i = U_{LL}, \qquad I_i = I_{KS}, \qquad G_i = \frac{1}{R_i}.$$
:::

**So liest man das:** Die erste Kennlinie gehört zur Ersatzspannungsquelle, nach Léon Charles Thévenin (1883, der Sache nach schon 1853 bei Hermann von
Helmholtz) auch __Thévenin-Quelle__ genannt. Die zweite gehört zur Ersatzstromquelle oder __Norton-Quelle__, nach Edward Lawry Norton (1926, im selben
Jahr unabhängig von Hans Ferdinand Mayer). Die Quellenspannung der einen ist die Leerlaufspannung des Netzes, der Quellstrom der anderen sein
Kurzschlussstrom, und der Innenwiderstand ist in beiden derselbe.

Alle drei Kenngrößen hängen nur vom Netz ab, nicht von dem, was außen angeschlossen ist. Gemeint ist dabei ein aktives Netz, denn ein passives hätte
weder Leerlaufspannung noch Kurzschlussstrom.

**Im Bild:** Statt des Stadtnetzes ein einziger Ersatzturm mit Ersatzleitung oder eine einzige Ersatzpumpe mit Leck. Der Turmdruck ist der Ruhedruck am
Hahn, der Pumpendurchfluss der größte Durchfluss am ganz offenen Hahn.

:::herleitung
**Schritt 1: Den Klemmenstrom vorgeben.** Was außen an den Klemmen hängt, wirkt auf das Eintor nur über Klemmenstrom und Klemmenspannung. Man darf sich
deshalb außen eine ideale Stromquelle denken, die einen beliebigen Strom $I_A$ aus A herauszieht und in B zurückspeist, und fragen, welche Spannung
$U_{AB}$ sich dann einstellt. Durchläuft $I_A$ alle Werte, entsteht die ganze Kennlinie; jede echte Beschaltung trifft einen ihrer Punkte. Im Bild: eine
Testpumpe am Hahn, die einen eingestellten Durchfluss abzapft, während das Manometer den Druck zeigt.

**Schritt 2: Die Netzgleichungen sind linear.** Knotenregel, Maschenregel und ohmsches Gesetz sind lineare Gleichungen in den unbekannten Zweigströmen
und Zweigspannungen. Die Quellenwerte und der vorgegebene Strom $I_A$ stehen darin als bekannte Größen auf der rechten Seite. Löst man ein solches
Gleichungssystem auf, etwa indem man nacheinander Unbekannte eliminiert, ist jede Unbekannte eine Summe der bekannten Größen, jede mit einem festen
Faktor, der nur von den Widerständen abhängt. Vorausgesetzt ist, dass die Lösung eindeutig ist. Für Netze aus Widerständen und Spannungsquellen hat das
der Artikel über die Kirchhoffschen Gesetze gezeigt; mit Stromquellen trägt dasselbe Argument, denn in der Differenz zweier Lösungen führen sie keinen
Strom. Ausgenommen sind nur die verbotenen Schaltungen idealer Quellen aus dem vorigen Artikel. Für die Klemmenspannung heißt das, mit Faktoren
$\alpha_\nu$ und $\beta_\mu$ und einem dritten, den wir $-R_i$ nennen:

$$U_{AB} = \sum_\nu \alpha_\nu\,U_{q\nu} + \sum_\mu \beta_\mu\,I_{q\mu} - R_i\,I_A.$$

Im Bild: In einem Netz linearer Rohre setzt sich der Druck am Hahn aus den Beiträgen aller Türme und Pumpen zusammen, und jeder Liter pro Sekunde, den
man abzapft, kostet einen festen Druck.

**Schritt 3: Leerlauf.** Mit $I_A$ gleich null bleiben nur die beiden Summen, und das ist die Leerlaufspannung:

$$U_{LL} = \sum_\nu \alpha_\nu\,U_{q\nu} + \sum_\mu \beta_\mu\,I_{q\mu}, \qquad U_{AB} = U_{LL} - R_i\,I_A.$$

Das ist die Kennlinie einer realen Spannungsquelle mit der Quellenspannung $U_{LL}$ und dem Innenwiderstand $R_i$, also der Ersatzspannungsquelle.

**Schritt 4: Kurzschluss und Stromform.** Bei kurzgeschlossenen Klemmen ist $U_{AB}$ null, und die Kennlinie liefert den Kurzschlussstrom. Nach der
Quellenumwandlung des vorigen Artikels ist die Spannungsquelle zugleich äquivalent zu einer Stromquelle mit dem Innenleitwert $1/R_i$ und genau diesem
Quellstrom:

$$0 = U_{LL} - R_i\,I_{KS}, \qquad I_i = \frac{U_{LL}}{R_i} = I_{KS}.$$

**Sonderfälle.** Liegt eine ideale Spannungsquelle unmittelbar zwischen den Klemmen, ist $R_i$ null, und es gibt nur die Spannungsform. Liegt eine ideale
Stromquelle in Reihe mit einer Klemme, legt sie den Klemmenstrom selbst fest; dann ist $G_i$ null, und es gibt nur die Stromform. Das sind die Grenzen der
Quellenumwandlung aus dem vorigen Artikel. Was $R_i$ im Netz bedeutet, zeigt der Abschnitt über das Stilllegen der Quellen.
:::

::::beispiel Drei Lasten, eine Gerade
Das __Referenznetz__ dieser Beispiel-Seite: Eine Spannungsquelle $U_q$ speist über $R_1$ einen Mittelknoten M; von M führt $R_2$ zur Klemme B, die am
Minuspol der Quelle liegt, und $R_3$ zur Klemme A.

$$U_q = 12\,\text{V}, \qquad R_1 = 6\,\text{k}\Omega, \qquad R_2 = 3\,\text{k}\Omega, \qquad R_3 = 2\,\text{k}\Omega.$$

So gewinnt man etwa eine Hilfsspannung für einen Sensor, mit $R_3$ als Schutzwiderstand.

**Eine Last, das ganze Netz gerechnet.** An den Klemmen hängt $R_L$ mit $4\,\text{k}\Omega$. Dann liegen $R_3$ und $R_L$ in Reihe, zusammen parallel zu
$R_2$, und das Ganze in Reihe mit $R_1$; $I_0$ ist der Strom aus der Quelle, $U_M$ die Spannung von M nach B:

$$R_2 \parallel (R_3 + R_L) = \frac{3\cdot6}{3 + 6}\,\text{k}\Omega = 2\,\text{k}\Omega, \qquad I_0 = \frac{12\,\text{V}}{6\,\text{k}\Omega + 2\,\text{k}\Omega} = 1{,}5\,\text{mA},$$

$$U_M = 1{,}5\,\text{mA}\cdot2\,\text{k}\Omega = 3\,\text{V}, \qquad I_A = \frac{3\,\text{V}}{6\,\text{k}\Omega} = 0{,}5\,\text{mA}, \qquad U_{AB} = 0{,}5\,\text{mA}\cdot4\,\text{k}\Omega = 2\,\text{V}.$$

**Drei Lasten.** Ebenso gerechnet:

| Last $R_L$ | Klemmenstrom $I_A$ | Klemmenspannung $U_{AB}$ |
|---|---|---|
| $12\,\text{k}\Omega$ | $0{,}25\,\text{mA}$ | $3\,\text{V}$ |
| $4\,\text{k}\Omega$ | $0{,}5\,\text{mA}$ | $2\,\text{V}$ |
| $1\,\text{k}\Omega$ | $0{,}8\,\text{mA}$ | $0{,}8\,\text{V}$ |

**Eine Gerade.** Die Steigungen zwischen benachbarten Punkten:

$$\frac{2\,\text{V} - 3\,\text{V}}{0{,}5\,\text{mA} - 0{,}25\,\text{mA}} = -4\,\text{k}\Omega, \qquad \frac{0{,}8\,\text{V} - 2\,\text{V}}{0{,}8\,\text{mA} - 0{,}5\,\text{mA}} = -4\,\text{k}\Omega.$$

Alle drei Punkte liegen auf einer Geraden mit der Steigung $-4\,\text{k}\Omega$. Bis zum Strom null verlängert, erreicht sie vom ersten Punkt aus die
Spannung

$$U_i = 3\,\text{V} + 0{,}25\,\text{mA}\cdot4\,\text{k}\Omega = 4\,\text{V}, \qquad R_i = 4\,\text{k}\Omega.$$

Jede weitere Last kann man mit dieser Ersatzspannungsquelle rechnen statt mit dem ganzen Netz.

**Im Bild:** Drei verschieden weit geöffnete Hähne, drei Messpunkte — und alle liegen auf der Geraden eines einzigen Ersatzturms, dessen Druck 4 V
entspricht, mit einer Zuleitung von 4 kΩ.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/02-ersatzquellen · Vorlage: eintor-ersatzquelle
Links das Referenznetz der Beispiel-Seite als graue Wolke mit sichtbarem Inhalt ($U_q = 12\,\text{V}$ über
$R_1 = 6\,\text{k}\Omega$ zum Mittelknoten M, $R_2 = 3\,\text{k}\Omega$ von M nach B, $R_3 = 2\,\text{k}\Omega$ von M nach A), Klemmenstrom $I_A$ aus A
heraus, Klemmenspannung $U_{AB}$ von A nach B. Zwei Pfeile führen nach rechts zu den beiden Ersatzschaltungen: oben die Ersatzspannungsquelle
$U_i = 4\,\text{V}$ mit $R_i = 4\,\text{k}\Omega$ in Reihe, unten die Ersatzstromquelle $I_i = 1\,\text{mA}$ mit $G_i = 0{,}25\,\text{mS}$ parallel, beide
mit denselben Zählpfeilen. An alle drei ist derselbe Lastregler angeschlossen; drei Anzeigen zeigen bei jeder Einstellung dieselben Werte von $I_A$ und
$U_{AB}$. Kernaussage: An den Klemmen sind Netz, Ersatzspannungs- und Ersatzstromquelle nicht zu unterscheiden. (Rot = Ersatzquellen, blau =
Klemmengrößen, orange = Innenwiderstand und Innenleitwert, grau = Netzinneres und Last.)
:::

## Leerlauf- und Kurzschlussversuch

Der Satz sagt, dass es die Ersatzquelle gibt. Ihre Kenngrößen findet man am einfachsten mit zwei Versuchen, die die Kennlinie an ihren beiden Enden
abtasten:

- Im __Leerlaufversuch__ bleiben die Klemmen offen. Man misst oder berechnet die Leerlaufspannung $U_{LL}$; ein Klemmenstrom fließt nicht.
- Im __Kurzschlussversuch__ verbindet man die Klemmen durch einen widerstandslosen Leiter. Man misst oder berechnet den Kurzschlussstrom $I_{KS}$; die
  Klemmenspannung ist null.

Die Leerlaufspannung ist die Quellenspannung der Ersatzspannungsquelle, der Kurzschlussstrom der Quellstrom der Ersatzstromquelle. Der Innenwiderstand,
der beiden gemeinsam ist, folgt aus ihrem Verhältnis:

:::formel
$$R_i = \frac{1}{G_i} = \frac{U_{LL}}{I_{KS}}.$$
:::

**So liest man das:** Die Kennlinie schneidet die Spannungsachse bei $U_{LL}$ und die Stromachse bei $I_{KS}$, und $R_i$ ist der Betrag ihrer Steigung. Ein
großer Innenwiderstand heißt: Schon ein kleiner Strom kostet viel Spannung. Die Formel versagt, wenn Leerlaufspannung und Kurzschlussstrom beide null
sind, etwa bei einem passiven Netz; dann hilft nur der direkte Weg über das Stilllegen der Quellen weiter unten.

**Im Bild:** Der Ruhedruck bei geschlossenem Hahn, geteilt durch den Durchfluss bei ganz offenem, ist der Widerstand der Ersatzleitung.

:::herleitung
**Die beiden Achsenabschnitte.** Die Kennlinie aus dem Satz, an ihren Enden ausgewertet: Im Leerlauf ist $I_A$ null, im Kurzschluss $U_{AB}$:

$$U_{LL} = U_i, \qquad 0 = U_i - R_i\,I_{KS}.$$

Die zweite Gleichung, nach $R_i$ aufgelöst und mit der ersten verbunden, ergibt die Formel; $G_i$ ist der Kehrwert von $R_i$.

**Die Steigung.** Zwischen den beiden Achsenpunkten ändert sich die Spannung um $-U_{LL}$ und der Strom um $I_{KS}$. Der Quotient ist die Steigung $-R_i$
der Geraden. Im Bild: Vom geschlossenen bis zum ganz offenen Hahn fällt der Druck gleichmäßig vom Ruhedruck auf null.
:::

::::beispiel Leerlauf und Kurzschluss am Referenznetz
Das Referenznetz: $U_q$ speist über $R_1$ den Mittelknoten M, $R_2$ führt von M nach B, $R_3$ von M nach A.

$$U_q = 12\,\text{V}, \qquad R_1 = 6\,\text{k}\Omega, \qquad R_2 = 3\,\text{k}\Omega, \qquad R_3 = 2\,\text{k}\Omega.$$

**Leerlauf.** Ohne Klemmenstrom fließt durch $R_3$ nichts, an ihm fällt keine Spannung ab, und an den Klemmen liegt die Spannung des Mittelknotens. Das
ist der unbelastete Teiler aus $R_1$ und $R_2$:

$$U_{LL} = 12\,\text{V}\cdot\frac{3\,\text{k}\Omega}{6\,\text{k}\Omega + 3\,\text{k}\Omega} = 4\,\text{V}.$$

**Kurzschluss.** Jetzt führt $R_3$ von M direkt nach B und liegt parallel zu $R_2$:

$$R_2 \parallel R_3 = 1{,}2\,\text{k}\Omega, \qquad I_0 = \frac{12\,\text{V}}{6\,\text{k}\Omega + 1{,}2\,\text{k}\Omega} \approx 1{,}667\,\text{mA}, \qquad U_M = I_0\cdot1{,}2\,\text{k}\Omega = 2\,\text{V},$$

$$I_{KS} = \frac{U_M}{R_3} = \frac{2\,\text{V}}{2\,\text{k}\Omega} = 1\,\text{mA}.$$

**Die Ersatzquellen.**

$$R_i = \frac{4\,\text{V}}{1\,\text{mA}} = 4\,\text{k}\Omega, \qquad I_i = 1\,\text{mA}, \qquad G_i = \frac{1}{4\,\text{k}\Omega} = 0{,}25\,\text{mS}.$$

Das sind genau die Werte, die die Gerade durch die drei Lastpunkte ergeben hat; zwei Versuche ersetzen die Rechnung mit jeder einzelnen Last.

**Im Bild:** Bei geschlossenem Hahn steht in der Leitung $R_3$ das Wasser, und der Hahn hat den Druck des Abzweigs M. Bei ganz offenem Hahn wird $R_3$ zu
einem zweiten Abfluss neben $R_2$, und der Druck am Abzweig sinkt von 4 auf 2 V.
::::

In der Praxis haben beide Versuche Tücken. Das Messgerät für die Leerlaufspannung belastet die Klemmen mit seinem eigenen Innenwiderstand, der deshalb
viel größer als $R_i$ sein muss (Artikel über Strom- und Spannungsmessung). Und ein Kurzschluss kann eine Quelle überlasten: Bei der Autobatterie des
vorigen Artikels flössen rechnerisch etwa 1600 A. Dann nimmt man statt der beiden Extremfälle zwei gewöhnliche Belastungen, wie im nächsten Abschnitt.

Ein weiteres Beispiel für den Leerlaufversuch ist eine reale Spannungsquelle $U_q$ mit dem Innenwiderstand $R_q$, zu deren Klemmen ein Widerstand $R_1$
parallel liegt. Im Leerlauf bilden $R_q$ und $R_1$ einen unbelasteten Spannungsteiler:

$$U_i = U_{LL} = \frac{R_1}{R_q + R_1}\,U_q.$$

## Zwei Belastungsfälle statt Kurzschluss

Lassen sich Leerlauf und Kurzschluss nicht messen, genügen zwei beliebige Belastungen. Man schließt nacheinander zwei verschiedene Lastwiderstände
$R_{L1}$ und $R_{L2}$ an, misst jeweils Strom und Spannung und erhält zwei Punkte $(I_1, U_1)$ und
$(I_2, U_2)$ der Kennlinie. Durch zwei Punkte geht genau eine Gerade:

:::formel
$$R_i = \frac{U_1 - U_2}{I_2 - I_1}, \qquad U_i = U_{LL} = \frac{U_1\,I_2 - U_2\,I_1}{I_2 - I_1}.$$
:::

**So liest man das:** Der Innenwiderstand ist die Spannungsabnahme pro Stromzunahme zwischen den beiden Lastpunkten, die Leerlaufspannung der Wert, den
die verlängerte Gerade beim Strom null erreicht. Die beiden Lastpunkte sollten weit auseinanderliegen, denn je kleiner die Stromdifferenz, desto stärker
schlägt ein Messfehler auf $R_i$ durch.

**Im Bild:** Zwei verschieden weit geöffnete Hähne statt zu und ganz offen. Auch zwei solche Punkte legen die Gerade des Ersatzturms fest.

:::herleitung
**Zwei Punkte auf der Kennlinie.** Beide Messpunkte erfüllen die Kennlinie der Ersatzspannungsquelle:

$$U_1 = U_i - R_i\,I_1, \qquad U_2 = U_i - R_i\,I_2.$$

**Innenwiderstand.** In der Differenz fällt $U_i$ heraus:

$$U_1 - U_2 = R_i\,(I_2 - I_1).$$

Für zwei verschiedene Ströme lässt sie sich nach $R_i$ auflösen. Im Bild: Der Druckunterschied zwischen den beiden Hähnen entsteht allein in der
Ersatzleitung.

**Leerlaufspannung.** Die erste Gleichung nach $U_i$ aufgelöst und $R_i$ eingesetzt; auf dem Hauptnenner $I_2 - I_1$ hebt sich $U_1 I_1$ weg:

$$U_i = U_1 + R_i\,I_1 = U_1 + \frac{(U_1 - U_2)\,I_1}{I_2 - I_1} = \frac{U_1\,I_2 - U_2\,I_1}{I_2 - I_1}.$$

**Messfehler.** Ist $U_1$ um einen kleinen Betrag $\delta$ falsch gemessen, ändert sich der berechnete Innenwiderstand nach der ersten Formel um

$$\Delta R_i = \frac{\delta}{I_2 - I_1}.$$

Je näher die beiden Ströme beieinanderliegen, desto größer wird dieser Fehler.
:::

::::beispiel Ein Steckernetzteil vermessen
Ein ungeregeltes Steckernetzteil mit der Aufschrift 9 V soll nicht kurzgeschlossen werden. Mit zwei Lastwiderständen von $48\,\Omega$ und $14\,\Omega$
misst man

$$I_1 = 0{,}2\,\text{A}, \qquad U_1 = 9{,}6\,\text{V}, \qquad I_2 = 0{,}6\,\text{A}, \qquad U_2 = 8{,}4\,\text{V}.$$

**Die Ersatzquelle.**

$$R_i = \frac{9{,}6\,\text{V} - 8{,}4\,\text{V}}{0{,}6\,\text{A} - 0{,}2\,\text{A}} = 3\,\Omega,$$

$$U_i = \frac{9{,}6\,\text{V}\cdot0{,}6\,\text{A} - 8{,}4\,\text{V}\cdot0{,}2\,\text{A}}{0{,}4\,\text{A}} = 10{,}2\,\text{V}, \qquad I_{KS} = \frac{10{,}2\,\text{V}}{3\,\Omega} = 3{,}4\,\text{A}.$$

Unbelastet liefert das Netzteil also mehr als die aufgedruckten 9 V, die nur bei der vorgesehenen Last gelten. Ein Kurzschluss würde rechnerisch
$3{,}4\,\text{A}$ treiben, weit mehr, als ein solches Netzteil auf Dauer verträgt. Ganz linear ist es nicht; im Bereich der Messpunkte beschreibt die Gerade es
aber gut.

**Der Messfehler.** Ein Fehler von $0{,}05\,\text{V}$ in $U_1$ wirkt bei den $0{,}4\,\text{A}$ Stromdifferenz oben wenig, bei nur $0{,}05\,\text{A}$
Stromdifferenz stark:

$$\Delta R_i = \frac{0{,}05\,\text{V}}{0{,}4\,\text{A}} = 0{,}125\,\Omega, \qquad \Delta R_i = \frac{0{,}05\,\text{V}}{0{,}05\,\text{A}} = 1\,\Omega.$$

Aus den $3\,\Omega$ würden im zweiten Fall $4\,\Omega$.

**Im Bild:** Zwei Hähne, halb und weiter geöffnet. Die Gerade durch die beiden Punkte, bis zum geschlossenen Hahn verlängert, zeigt den Ruhedruck, den
man nie direkt gemessen hat.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/02-kennlinie-zwei-punkte · Vorlage: kennlinie-eintor
Die Kennlinie $U_{AB}$ über $I_A$ des Steckernetzteils als fallende Gerade von $U_{LL} = 10{,}2\,\text{V}$ bis
$I_{KS} = 3{,}4\,\text{A}$. Zwei verschiebbare Lastpunkte $(I_1, U_1)$ und $(I_2, U_2)$, anfangs bei $0{,}2\,\text{A}$ und $0{,}6\,\text{A}$, mit
gestrichelten Loten auf die Achsen; ein Steigungsdreieck zwischen ihnen zeigt $R_i$, die gestrichelte Verlängerung trifft beide Achsen. Ein Schalter
„Messfehler" hebt $U_1$ um $0{,}05\,\text{V}$: Liegen die Punkte weit auseinander, kippt die Gerade kaum; rücken sie zusammen, kippt sie stark, und die
Anzeigen für $R_i$ und $U_{LL}$ springen. Kernaussage: Zwei Lastpunkte legen die Ersatzquelle fest, am genauesten, wenn sie weit auseinanderliegen. (Rot =
Kennlinie, blau = Lastpunkte, orange = Steigungsdreieck, grau = Achsen, gestrichelt = Verlängerung und Lote.)
:::

## Den Innenwiderstand direkt ablesen

Oft ist es bequemer, $R_i$ nicht aus zwei Versuchen zu berechnen, sondern direkt aus dem Netz abzulesen. Die Herleitung des Satzes zeigt, warum das geht:
Der Faktor $R_i$ hängt nur von den Widerständen ab, nicht von den Quellen. Man darf deshalb alle Quellenwerte null setzen, ohne $R_i$ zu ändern; übrig
bleibt ein reines Widerstandsnetz. Oft heißt es dafür kurz: Jede Quelle wird durch ihren Innenwiderstand ersetzt. Was eine Quelle mit dem Wert null ist,
folgt aus ihrer Kennlinie:

- Eine ideale Spannungsquelle mit dem Wert null hält zwischen ihren Anschlüssen die Spannung null, bei jedem Strom. Sie ist ein __Kurzschluss__, ein
  Stück Draht, mit dem Innenwiderstand null.
- Eine ideale Stromquelle mit dem Wert null lässt bei jeder Spannung den Strom null durch. Sie ist eine __Unterbrechung__, eine offene Stelle, mit
  unendlichem Innenwiderstand.

Innenwiderstände realer Quellen bleiben dabei stehen, stillgelegt wird nur der ideale Teil. Den Innenwiderstand des Eintors liefert dann der Widerstand
$R_{AB}$, den man zwischen den Klemmen des stillgelegten Netzes misst oder mit den Regeln für Reihen- und Parallelschaltung berechnet:

:::formel Satz
$$R_i = R_{AB}\Big|_{\text{alle } U_{q\nu} = 0,\ \text{alle } I_{q\mu} = 0}.$$
:::

**So liest man das:** Man ersetzt jede ideale Spannungsquelle durch einen Draht und jede ideale Stromquelle durch eine Lücke und fasst zusammen, was
zwischen A und B übrig bleibt. Leerlauf- und Kurzschlussversuch liefern denselben Wert, eine gute Probe. Und weil ein stillgelegtes Netz Leistung nur
aufnehmen kann, ist $R_i$ nie negativ.

**Im Bild:** Alle Türme auf Höhe null, sie sind nur noch Rohrstücke; alle Pumpen angehalten, ihre stehenden Kolben sperren. Was das Netz dann Wasser
entgegensetzt, das man in den Hahn drückt, ist die Ersatzleitung.

:::herleitung
**Aus dem Satz.** Nach Schritt 2 der Herleitung des Satzes hängen die Faktoren $\alpha_\nu$, $\beta_\mu$ und $R_i$ nur von den Widerständen ab. Setzt man
alle Quellenwerte null, fallen beide Summen weg:

$$U_{AB} = -R_i\,I_A.$$

Das ist die Kennlinie eines Widerstands $R_i$ zwischen A und B: Der Strom $I_A$, der aus A herausgezogen wird, fließt im Netz von B nach A, und in dieser
Richtung fällt die Spannung $R_i I_A$ ab. Also ist $R_i$ der Widerstand des stillgelegten Netzes zwischen den Klemmen.

**Quelle mit dem Wert null.** Eine ideale Spannungsquelle mit dem Wert null erzwingt zwischen ihren Anschlüssen die Spannung null und lässt jeden Strom
zu; genau das tut ein widerstandsloser Draht. Eine ideale Stromquelle mit dem Wert null erzwingt den Strom null bei jeder Spannung; genau das tut eine
Unterbrechung. Im Bild: Ein Turm der Höhe null hebt den Druck nicht, er leitet nur weiter; ein stehender Kolben lässt nichts durch.

**Nie negativ.** Im stillgelegten Netz wirken keine Quellen mehr. Was man an den Klemmen an Leistung hineinsteckt, setzen allein die Widerstände in
Wärme um, jeder Widerstand $R_k$ mit seinem Strom $I_k$ den Anteil $R_k I_k^2$:

$$-U_{AB}\,I_A = R_i\,I_A^2 = \sum_k R_k\,I_k^2 \ge 0.$$

Im Bild: Ein stillgelegtes Rohrnetz kann Wasser nur bremsen, nie antreiben.
:::

::::beispiel Das Referenznetz, stillgelegt und mit einer zweiten Quelle
Das Referenznetz: $U_q$ speist über $R_1$ den Mittelknoten M, $R_2$ führt von M nach B, $R_3$ von M nach A.

$$U_q = 12\,\text{V}, \qquad R_1 = 6\,\text{k}\Omega, \qquad R_2 = 3\,\text{k}\Omega, \qquad R_3 = 2\,\text{k}\Omega.$$

**(a) Stilllegen.** Die Spannungsquelle wird zum Draht. Dann führt $R_1$ von M direkt nach B und liegt parallel zu $R_2$, und $R_3$ kommt in Reihe dazu:

$$R_i = R_3 + R_1 \parallel R_2 = 2\,\text{k}\Omega + \frac{6\cdot3}{6 + 3}\,\text{k}\Omega = 4\,\text{k}\Omega.$$

Derselbe Wert wie aus Leerlauf und Kurzschluss, ohne die Quelle überhaupt zu betrachten.

**(b) Eine zweite Quelle.** Zwischen B und A kommt eine ideale Stromquelle hinzu, die den Strom $I_{q2}$ in die Klemme A schiebt, etwa den Messstrom eines
Sensors:

$$I_{q2} = 0{,}5\,\text{mA}.$$

Stillgelegt ist sie eine Lücke, der Innenwiderstand bleibt bei $4\,\text{k}\Omega$. Im Leerlauf fließt ihr Strom über $R_3$ nach M. Die Knotenregel am
Mittelknoten, zufließend gleich abfließend, ergibt seine Spannung $U_M$, und an $R_3$ kommt der Abfall des Quellstroms dazu:

$$\frac{12\,\text{V} - U_M}{6\,\text{k}\Omega} + 0{,}5\,\text{mA} = \frac{U_M}{3\,\text{k}\Omega}, \qquad U_M = 5\,\text{V},$$

$$U_{LL} = U_M + R_3\,I_{q2} = 5\,\text{V} + 1\,\text{V} = 6\,\text{V}.$$

Im Kurzschluss liegen A und B auf gleichem Potenzial. Der Strom der Stromquelle fließt durch den Kurzschlussdraht unmittelbar zurück nach B, und durch
$R_3$ fließt wie ohne sie $1\,\text{mA}$:

$$I_{KS} = 1\,\text{mA} + 0{,}5\,\text{mA} = 1{,}5\,\text{mA}, \qquad \frac{U_{LL}}{I_{KS}} = \frac{6\,\text{V}}{1{,}5\,\text{mA}} = 4\,\text{k}\Omega.$$

Die Leerlaufspannung ist, wie in der Herleitung des Satzes, eine Summe der Beiträge beider Quellen mit festen Faktoren. Den ersten liefert der
unbelastete Teiler, den zweiten das stillgelegte Netz, durch dessen $4\,\text{k}\Omega$ die Stromquelle allein ihren Strom treibt:

$$U_{LL} = \frac{R_2}{R_1 + R_2}\,U_q + 4\,\text{k}\Omega\cdot I_{q2} = 4\,\text{V} + 2\,\text{V}.$$

**(c) Mit Innenwiderstand.** Hat die Stromquelle einen Innenwiderstand $R_{q2}$ von $12\,\text{k}\Omega$ parallel, bleibt er beim Stilllegen stehen und
liegt parallel zu den $4\,\text{k}\Omega$:

$$R_i = 4\,\text{k}\Omega \parallel 12\,\text{k}\Omega = 3\,\text{k}\Omega.$$

Im Kurzschluss ist $R_{q2}$ überbrückt, der Kurzschlussstrom bleibt bei $1{,}5\,\text{mA}$, und

$$U_{LL} = R_i\,I_{KS} = 3\,\text{k}\Omega\cdot1{,}5\,\text{mA} = 4{,}5\,\text{V}.$$

**Im Bild:** Eine Pumpe, die direkt in die Hahnleitung speist, hebt den Ruhedruck, ändert aber nichts an der Ersatzleitung, denn angehalten sperrt sie.
Hat sie ein Leck, ist es ein zusätzlicher Abfluss neben dem Hahn, und das Netz wird von außen durchlässiger.
::::

Ebenso lässt sich eine reale Stromquelle $I_q$ mit dem Innenwiderstand $R_q$ parallel behandeln, von der ein Widerstand $R_2$ zur Klemme A führt.
Stillgelegt liegen $R_q$ und $R_2$ in Reihe, $R_i$ ist ihre Summe. Im Kurzschluss teilt sich $I_q$ nach dem Stromteiler auf $R_q$ und $R_2$ auf:

$$I_i = I_q\,\frac{R_q}{R_q + R_2}.$$

:::grafik
Szene: get1/analyse-linearer-netzwerke/02-quellen-stilllegen · Vorlage: quellen-stilllegen
Am Referenznetz mit zweiter Quelle: $U_q = 12\,\text{V}$ über $R_1 = 6\,\text{k}\Omega$ zum Mittelknoten M,
$R_2 = 3\,\text{k}\Omega$ von M nach B, $R_3 = 2\,\text{k}\Omega$ von M nach A, zwischen B und A die Stromquelle $I_{q2} = 0{,}5\,\text{mA}$ mit Pfeil
zur Klemme A und wahlweise $R_{q2} = 12\,\text{k}\Omega$ parallel. Ein Knopf „stilllegen" lässt die Spannungsquelle zu einem Draht schrumpfen
(Beschriftung „Kurzschluss") und die Stromquelle verblassen (Beschriftung „offen"); $R_{q2}$ bleibt stehen. Dann fassen sich die Widerstände schrittweise
zusammen: $R_1 \parallel R_2 = 2\,\text{k}\Omega$, mit $R_3$ in Reihe $4\,\text{k}\Omega$, mit $R_{q2}$ parallel $3\,\text{k}\Omega$; ein Pfeil
„$R_i = ?$" zeigt in die Klemmen. Kernaussage: Den Innenwiderstand liefert das Netz mit Spannungsquellen als Draht und Stromquellen als Lücke. (Rot =
Quellen und ihr Ersatz, blau = Klemmen und $R_i$, orange = Zusammenfassen, grau = übrige Widerstände, gestrichelt = verblasste Stromquelle.)
:::

## Warum sich das Ersetzen lohnt — und wo es aufhört

Hat man die Ersatzquelle, rechnet man jede Last in einer Zeile, statt das ganze Netz neu aufzulösen. Mit einem Lastwiderstand $R_L$ an den Klemmen
bilden Ersatzspannungsquelle und Last eine einzige Masche:

$$I_A = \frac{U_i}{R_i + R_L}, \qquad U_{AB} = U_i\,\frac{R_L}{R_i + R_L}.$$

**So liest man das:** Vom Netz gehen nur $U_i$ und $R_i$ ein. Deshalb schneidet man eine Schaltung gern an der Stelle auf, die sich ändert, und ersetzt den
festen Rest durch seine Ersatzquelle. So wurde schon der belastete Spannungsteiler im Artikel über die Zusammenschaltung von Widerständen behandelt, und
so ließ sich bei der Wheatstone-Brücke zeigen, dass der Abgleich nicht von der Quelle abhängt.

**Im Bild:** Ist der Ersatzturm einmal bestimmt, braucht man für jeden neuen Verbraucher nur noch Ersatzleitung und Hahn.

:::herleitung
**Eine Masche.** Durch $R_i$ und $R_L$ fließt derselbe Strom $I_A$; nach der Maschenregel ist die Summe der beiden Abfälle gleich der Quellenspannung:

$$U_i = R_i\,I_A + R_L\,I_A.$$

Nach $I_A$ aufgelöst ergibt das die erste Formel, und weil an der Last $R_L I_A$ abfällt, die zweite, den Spannungsteiler. Da das Netz an den Klemmen
dieselbe Kennlinie hat wie die Ersatzquelle, gelten beide Formeln auch für das Netz selbst.
:::

Drei Grenzen hat das Ersetzen:

- **Nur außen gleich.** Was im Inneren an Leistung umgesetzt wird, gibt die Ersatzquelle nicht wieder. Das Netz und seine beiden Ersatzquellen haben
  verschiedene innere Verluste, wie schon bei der Quellenumwandlung im vorigen Artikel.
- **Nur für lineare Netze.** Enthält das Netz nichtlineare Bauteile wie Dioden, ist seine Kennlinie gekrümmt. Eine Ersatzquelle beschreibt sie dann nur
  in der Nähe eines Betriebspunkts, als Tangente an die Kurve.
- **Nur für ein Klemmenpaar.** Die Ersatzquelle gilt für die beiden Klemmen, für die man sie bestimmt hat; für zwei andere Knoten desselben Netzes ergibt
  sich eine andere.

::::beispiel Neue Last und innere Verluste am Referenznetz
**(a) Eine neue Last.** Mit der Ersatzquelle des Referenznetzes, $4\,\text{V}$ hinter $4\,\text{k}\Omega$, ist eine Last von $2\,\text{k}\Omega$ in einer
Zeile gerechnet:

$$I_A = \frac{4\,\text{V}}{4\,\text{k}\Omega + 2\,\text{k}\Omega} \approx 0{,}667\,\text{mA}, \qquad U_{AB} \approx 0{,}667\,\text{mA}\cdot2\,\text{k}\Omega \approx 1{,}33\,\text{V}.$$

Die Rechnung mit dem ganzen Netz, wie bei den drei Lasten, liefert dasselbe, braucht aber mehrere Schritte.

**(b) Innere Verluste im Leerlauf.** Im Netz fließt auch ohne Last der Teilerstrom durch $R_1$ und $R_2$. Die Ersatzspannungsquelle setzt im Leerlauf
nichts um, die Ersatzstromquelle schickt ihren ganzen Strom durch $G_i$:

$$P_\text{Netz} = \frac{(12\,\text{V})^2}{9\,\text{k}\Omega} = 16\,\text{mW}, \qquad P_\text{Thévenin} = 0, \qquad P_\text{Norton} = \frac{I_i^2}{G_i} = \frac{(1\,\text{mA})^2}{0{,}25\,\text{mS}} = 4\,\text{mW}.$$

Drei Schaltungen, die an den Klemmen dasselbe liefern, setzen innen 16 mW, nichts und 4 mW um.

**Im Bild:** Auch bei geschlossenem Hahn läuft im Stadtnetz Wasser durch den Abzweig $R_2$ ab. Der Ersatzturm steht dann still, die Ersatzpumpe drückt
alles durch ihr Leck zurück.
::::

## Spannungsform oder Stromform?

Beide Ersatzquellen beschreiben das Netz an den Klemmen gleich gut. Als Faustregel gilt: bei kleinem Innenwiderstand die
Ersatzspannungsquelle, bei großem die Ersatzstromquelle. Der Grund ist die Anschauung. Mit kleinem $R_i$ ist die Ersatzspannungsquelle fast ideal: Ihre
Klemmenspannung hängt kaum von der Last ab, und $U_i$ sagt unmittelbar, was an den Klemmen liegt. Die Stromform hätte dann einen riesigen Quellstrom,
der fast vollständig durch einen riesigen Innenleitwert zurückfließt — richtig, aber unanschaulich. Bei großem $R_i$ ist es umgekehrt.

In den Grenzfällen gibt es keine Wahl: Mit $R_i$ gleich null existiert nur die Spannungsform, mit $G_i$ gleich null nur die Stromform. Dazu passt die
übliche Sprechweise: Spannungsquellen sind __niederohmig__, ideal mit dem Innenwiderstand null, Stromquellen __hochohmig__, ideal mit unendlichem
Innenwiderstand.

**Im Bild:** Ein Turm mit sehr weiter Zuleitung ist fast ideal. Als Pumpe beschrieben, müsste er riesige Mengen fördern, die fast alle durch ein riesiges
Leck zurückfließen.

:::herleitung
**Stromteiler.** An der Ersatzstromquelle liegen $G_i$ und die Last parallel; die Last bekommt den Anteil ihres Leitwerts am Gesamtleitwert:

$$I_A = I_i\,\frac{1/R_L}{1/R_i + 1/R_L} = I_i\,\frac{R_i}{R_i + R_L}.$$

**Wie stark die Last durchgreift.** Mit dem Spannungsteiler aus dem vorigen Abschnitt und diesem Stromteiler folgen die relativen Abweichungen vom
Leerlauf und vom Kurzschluss:

$$\frac{U_i - U_{AB}}{U_i} = \frac{R_i}{R_i + R_L}, \qquad \frac{I_i - I_A}{I_i} = \frac{R_L}{R_i + R_L}.$$

Ist $R_i$ viel kleiner als $R_L$, ist die erste Abweichung klein und die Klemmenspannung fast $U_i$. Ist $R_i$ viel größer als $R_L$, ist die zweite klein
und der Klemmenstrom fast $I_i$. Im Bild: Eine weite Zuleitung lässt den Druck stehen, ein winziges Leck den Durchfluss.
:::

::::beispiel Ein Netzgerät und eine Stromquelle in beiden Formen
**(a) Kleiner Innenwiderstand.** Ein Netzgerät mit $5\,\text{V}$ hinter $10\,\text{m}\Omega$ liefert an $10\,\Omega$ und an $1\,\Omega$

$$U_{AB} = 5\,\text{V}\cdot\frac{10\,\Omega}{10{,}01\,\Omega} \approx 4{,}995\,\text{V}, \qquad U_{AB} = 5\,\text{V}\cdot\frac{1\,\Omega}{1{,}01\,\Omega} \approx 4{,}950\,\text{V}.$$

In der Stromform wäre es eine Quelle von $500\,\text{A}$ mit $100\,\text{S}$ parallel. An $10\,\Omega$ flössen davon $499{,}5\,\text{A}$ durch den
Innenleitwert zurück und nur $0{,}4995\,\text{A}$ in die Last — richtig, aber kein hilfreiches Bild.

**(b) Großer Innenwiderstand.** Eine elektronische Stromquelle, wie man sie später mit Transistoren baut, mit $1\,\text{mA}$ und $1\,\text{M}\Omega$
liefert an $1\,\text{k}\Omega$ und an $10\,\text{k}\Omega$

$$I_A = 1\,\text{mA}\cdot\frac{1\,\text{M}\Omega}{1{,}001\,\text{M}\Omega} \approx 0{,}999\,\text{mA}, \qquad I_A = 1\,\text{mA}\cdot\frac{1\,\text{M}\Omega}{1{,}01\,\text{M}\Omega} \approx 0{,}990\,\text{mA}.$$

In der Spannungsform wäre es eine Quelle von $1000\,\text{V}$ hinter $1\,\text{M}\Omega$. Diese $1000\,\text{V}$ treten nie an den Klemmen auf: Die echte
Schaltung ist nur in einem Bereich von wenigen Volt linear, und nur dort gilt jede der beiden Ersatzquellen. Ihre Leerlaufspannung ist hier ein
Rechenwert, der Schnittpunkt der verlängerten Geraden.

**Im Bild:** Ein Turm mit weiter Leitung beschreibt das Netzgerät, eine Pumpe mit winzigem Leck die Stromquelle. Die jeweils andere Beschreibung stimmt
auch, nur verdreht sie das Bild.
::::

## Bedeutung und Ausblick

Der Satz von der Ersatzquelle ist eines der meistgebrauchten Werkzeuge der Schaltungsanalyse. Man schneidet eine Schaltung an der Stelle auf, die
interessiert, ersetzt den festen Teil durch seine Ersatzquelle und untersucht den veränderlichen Teil mit einer einzigen Masche: einen Verbraucher an
einem Netzteil, ein Messgerät an einer Schaltung, die Diagonale einer Messbrücke. Messtechnisch erhält man die Ersatzquelle eines unbekannten Geräts aus
zwei Messungen an seinen Klemmen. Mit einem Schaltungssimulationsprogramm wie LTspice lassen sich die Kenngrößen einer Ersatzquelle ebenso bestimmen
und ihr Verhalten unter Last mit dem des Netzes vergleichen.

In der Herleitung war die Leerlaufspannung eine Summe von Beiträgen der einzelnen Quellen, jede mit ihrem festen Faktor; am Referenznetz mit zweiter
Quelle hat sich das gezeigt. Diese Zerlegung ist ein eigenes Rechenverfahren, das __Superpositionsverfahren__, dem der Artikel
[Das Superpositionsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html) gilt: Man rechnet jede Quelle allein, alle anderen stillgelegt, und addiert die Ergebnisse. Ebenfalls später folgt die Frage, bei welcher Last eine
Ersatzquelle die größte Leistung abgibt, die __Leistungsanpassung__. Der nächste Artikel betrachtet zunächst Netze mit zwei Klemmenpaaren, die
__Zweitore__. Und in der Wechselstromtechnik gilt der Satz genauso, mit komplexen Widerständen, den Impedanzen, an
Stelle der ohmschen.

:::kern
- Ein __Eintor__ ist ein Netz mit zwei Klemmen; von außen zählt nur seine Kennlinie.
- Jedes lineare Eintor ist an seinen Klemmen eine reale Quelle: $U_{AB}=U_i-R_iI_A$.
- Die Quellenspannung $U_i$ der Ersatzspannungsquelle ist die Leerlaufspannung, der Quellstrom $I_i$ der Ersatzstromquelle der Kurzschlussstrom.
- Der Innenwiderstand ist in beiden Formen derselbe: $R_i=U_{LL}/I_{KS}$.
- Ohne Kurzschluss genügen zwei Lastpunkte; $R_i$ ist der Betrag der Steigung zwischen ihnen.
- Direkt: Spannungsquellen durch Draht, Stromquellen durch Lücke ersetzen und den Widerstand zwischen A und B bestimmen.
- Netz und Ersatzquelle sind nur an den Klemmen gleich, ihre inneren Verluste verschieden.
- Kleiner $R_i$ legt die Spannungsform nahe, großer die Stromform.
:::

:::quiz
F: Was ist ein Eintor, und warum genügt ein einziger Strom, um zu beschreiben, was durch seine Klemmen fließt?
A: Ein Netzwerk mit genau zwei Anschlüssen A und B, die zusammen ein Tor bilden. Nach der Knotenregel für eine Hülle um das Netz fließt in B genau der Strom hinein, der aus A herausfließt, weil sich innen keine Ladung ansammeln kann. Im Bild: Was aus dem Hahn läuft, kommt über den Rücklauf zurück.
F: Was besagt der Satz von der Ersatzquelle, und welche Kenngrößen hat die Ersatzquelle?
A: Jedes lineare Eintor verhält sich an seinen Klemmen wie eine reale Spannungsquelle mit $U_{AB}=U_i-R_iI_A$ (Thévenin) oder wie eine reale Stromquelle mit $I_A=I_i-G_iU_{AB}$ (Norton). Dabei ist $U_i$ die Leerlaufspannung, $I_i$ der Kurzschlussstrom und $R_i=1/G_i$ in beiden Formen derselbe; alle drei hängen nur vom Netz ab, nicht von der Last.
F: Warum ist die Kennlinie eines linearen Eintors eine Gerade?
A: Man denkt sich außen eine ideale Stromquelle, die $I_A$ vorgibt. Knotenregel, Maschenregel und ohmsches Gesetz sind lineare Gleichungen mit Quellenwerten und $I_A$ auf der rechten Seite; die eindeutige Lösung ist eine Summe dieser Größen mit festen Faktoren, die nur von den Widerständen abhängen. Also ist $U_{AB}$ die Leerlaufspannung minus $R_iI_A$, eine Gerade in $I_A$.
F: Wie bestimmt man die Ersatzquelle mit Leerlauf- und Kurzschlussversuch, und was ergibt sich beim Referenznetz mit 12 V, 6 kΩ, 3 kΩ und 2 kΩ?
A: Bei offenen Klemmen misst oder berechnet man $U_{LL}$, bei kurzgeschlossenen $I_{KS}$, und $R_i=U_{LL}/I_{KS}$. Im Referenznetz ist die Leerlaufspannung die des unbelasteten Teilers, $4\,\text{V}$; im Kurzschluss liegt $R_3$ parallel zu $R_2$, und es fließt $1\,\text{mA}$. Das ergibt $4\,\text{k}\Omega$, $I_i=1\,\text{mA}$ und $G_i=0{,}25\,\text{mS}$, genau die Gerade durch die drei Lastpunkte.
F: Wie bestimmt man die Ersatzquelle aus zwei Belastungsfällen, und warum sollen die Lastpunkte weit auseinanderliegen?
A: Zwei Messpunkte $(I_1,U_1)$ und $(I_2,U_2)$ legen die Gerade fest: $R_i=\frac{U_1-U_2}{I_2-I_1}$ und $U_i=\frac{U_1I_2-U_2I_1}{I_2-I_1}$; beim Steckernetzteil ergeben $9{,}6\,\text{V}$ bei $0{,}2\,\text{A}$ und $8{,}4\,\text{V}$ bei $0{,}6\,\text{A}$ einen Innenwiderstand von $3\,\Omega$ und eine Leerlaufspannung von $10{,}2\,\text{V}$. Ein Messfehler $\delta$ verfälscht $R_i$ um $\frac{\delta}{I_2-I_1}$, umso mehr, je kleiner die Stromdifferenz ist.
F: Wie bestimmt man den Innenwiderstand durch Stilllegen der Quellen, und warum ersetzt man Spannungsquellen durch Draht und Stromquellen durch eine Lücke?
A: Man setzt alle Quellenwerte null und bestimmt den Widerstand zwischen A und B; das darf man, weil $R_i$ nur von den Widerständen abhängt. Eine Spannungsquelle mit null Volt hält bei jedem Strom die Spannung null wie ein Draht, eine Stromquelle mit null Ampere lässt bei jeder Spannung keinen Strom durch wie eine Unterbrechung. Innenwiderstände realer Quellen bleiben stehen. Im Referenznetz ergibt das $R_3+R_1\parallel R_2=4\,\text{k}\Omega$.
F: Was ändert eine zusätzliche Stromquelle zwischen den Klemmen an der Ersatzquelle?
A: Eine ideale Stromquelle ist stillgelegt eine Lücke, also bleibt $R_i$ gleich, während Leerlaufspannung und Kurzschlussstrom wachsen: Im Referenznetz heben $0{,}5\,\text{mA}$ die Leerlaufspannung von $4$ auf $6\,\text{V}$ und den Kurzschlussstrom von $1$ auf $1{,}5\,\text{mA}$. Mit $12\,\text{k}\Omega$ Innenwiderstand parallel sinkt $R_i$ auf $3\,\text{k}\Omega$; der Kurzschlussstrom bleibt, und die Leerlaufspannung wird $4{,}5\,\text{V}$.
F: In welchem Sinn sind ein Netz und seine Ersatzquelle gleich, und wo hört die Gleichheit auf?
A: An den Klemmen liefern sie bei jeder Last dasselbe, im Inneren nicht: Im Leerlauf setzt das Referenznetz $16\,\text{mW}$ um, die Ersatzspannungsquelle nichts, die Ersatzstromquelle $4\,\text{mW}$. Außerdem gilt die Ersatzquelle nur für lineare Netze, mit Dioden nur als Tangente an einem Betriebspunkt, und nur für das Klemmenpaar, für das man sie bestimmt hat.
F: Wann wählt man die Spannungsform, wann die Stromform, und wann gibt es keine Wahl?
A: Bei kleinem $R_i$ die Spannungsform, weil die Klemmenspannung dann fast $U_i$ ist; bei großem $R_i$ die Stromform, weil der Klemmenstrom fast $I_i$ ist. Ein Netzgerät mit $5\,\text{V}$ und $10\,\text{m}\Omega$ wäre als Stromquelle $500\,\text{A}$ parallel zu $100\,\text{S}$ — richtig, aber unanschaulich. Mit $R_i$ gleich null gibt es nur die Spannungsform, mit $G_i$ gleich null nur die Stromform.
F: Welche Kenngrößen haben eine reale Spannungsquelle $U_q$ mit $R_q$, zu deren Klemmen $R_1$ parallel liegt, und eine reale Stromquelle $I_q$ mit $R_q$ parallel, von der $R_2$ zur Klemme A führt?
A: Im ersten Netz bilden $R_q$ und $R_1$ im Leerlauf einen unbelasteten Teiler, $U_i=\frac{R_1}{R_q+R_1}\,U_q$. Im zweiten teilt sich $I_q$ im Kurzschluss auf $R_q$ und $R_2$ auf, $I_i=I_q\frac{R_q}{R_q+R_2}$; stillgelegt liegen $R_q$ und $R_2$ in Reihe, $R_i=R_q+R_2$. Ein passives Netz hätte dagegen weder Leerlaufspannung noch Kurzschlussstrom.
:::
