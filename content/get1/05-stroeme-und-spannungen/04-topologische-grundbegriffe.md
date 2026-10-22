---
title: Topologische Grundbegriffe – Knoten, Zweige, Maschen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50400
summary: Von Grund auf – wie man die Struktur einer Schaltung beschreibt, unabhängig davon, welche Bauteile darin sitzen, und warum sich damit vorab abzählen lässt, wie viele Gleichungen ein Netzwerk braucht. Leitbild ist das Wegenetz eines Wandergebiets: Kreuzungen sind Knoten, Wegstücke Zweige, Rundwege Maschen, und der Räumplan für den Winter ist ein Baum. Mit Knoten zählen, dem Graphen eines Netzwerks, Maschen als Vektoren und ihrer linearen Unabhängigkeit, dem Baum mit genau k − 1 Zweigen, den Maschen aus Verbindungszweigen und dem Satz m = z − k + 1 samt Beweis, der Bilanz aller Gleichungen und Netzen aus mehreren Teilen. Mit Beispiel-Seite.
tags: Netzwerk, Knoten, Zweig, Masche, Topologie, Baum, unabhängige Maschen
---

## Anschaulich

Zwei Schaltungen können völlig verschiedene Bauteile enthalten und doch gleich gebaut sein: Hier ein Widerstand, dort eine Quelle, aber die
Verbindungen sind dieselben. Dieses Gerüst aus Verbindungen heißt die __Topologie__ eines Netzwerks. Sie entscheidet, wie viele Gleichungen man für
eine Schaltung aufstellen muss und welche davon wirklich neu sind — noch bevor man weiß, was in den Zweigen steckt.

**Das Leitbild dieses Artikels:** **das Wegenetz eines Wandergebiets**. Es hat Kreuzungen, an denen sich drei oder mehr Wege treffen, und Wegstücke
zwischen je zwei Kreuzungen. Auf der Übersichtstafel am Parkplatz sind die Wege nicht in ihrer wahren Länge und Krümmung gezeichnet, sondern nur so, dass
man sieht, welche Kreuzung mit welcher verbunden ist. Genau diese Information ist die Topologie.

Im Netzwerk sind die Kreuzungen die __Knoten__, die Wegstücke die __Zweige__ mit ihren Bauteilen und die Rundwege, die zum Ausgangspunkt
zurückführen, ohne eine Kreuzung doppelt zu besuchen, die __Maschen__. Die Übersichtstafel ist der __Graph__ des Netzwerks.

Drei Folgerungen kann man dem Wegenetz direkt ansehen:

- **Auf einem Wegstück zählt man überall gleich viele Wanderer.** Zwischen zwei Kreuzungen kann niemand ab- oder zusteigen. Im Netzwerk heißt das: Der
  Strom ist längs eines Zweigs überall derselbe.
- **Nicht jeder Rundweg ist neu.** Wer zwei benachbarte Runden nacheinander läuft, geht das gemeinsame Stück einmal hin und einmal zurück; übrig bleibt
  die große Runde außen herum. Sie bringt nichts Neues.
- **Im Winter genügt ein Baum.** Damit jede Kreuzung erreichbar bleibt, muss man nur so viele Wegstücke räumen, dass alles verbunden ist, ohne dass ein
  Rundweg entsteht — bei $k$ Kreuzungen genau $k-1$. Jedes weitere geräumte Stück schließt genau einen Rundweg.

:::grafik
Szene: get1/stroeme-und-spannungen/04-wegenetz · Vorlage: wegenetz-graph
Links eine Wanderkarte mit gewundenen Wegen, vier Kreuzungen (rote Punkte) und sechs Wegstücken, teils lang und kurvig. Ein Regler „zur Übersichtstafel"
verformt die Karte stetig: Die Wege werden zu geraden Linien, die Kreuzungen rücken auf ein Raster, aber keine Verbindung kommt hinzu oder fällt weg.
Rechts danach dasselbe als Schaltung: Die Linien bekommen Bauteile (Widerstände, eine Quelle), die Kreuzungen werden zu Knoten. Ein Klick auf einen
Rundweg färbt ihn ein und lässt eine Wanderfigur ihn ablaufen. Ein Schalter „Winterdienst" färbt drei Wegstücke als geräumten Baum, die übrigen grau.
Kernaussage: Topologie ist, was beim Verformen erhalten bleibt — welche Knoten durch welche Zweige verbunden sind. (Rot = Knoten, blau = Zweige,
orange = Rundweg und Baum, grau = Gelände und ungeräumte Wege.)
:::

## Knoten, Zweige, Maschen

Ein __Netzwerk__ ist nach dem Artikel über den Widerstand eine Zusammenschaltung von Zweipolen. Seine Struktur beschreibt man mit drei Begriffen:

- Ein __Knoten__ ist ein Netzwerkpunkt mit Stromverzweigung, ein Punkt, an dem mindestens drei Zweipole angeschlossen sind, so dass sich der Strom
  aufteilen kann.
- Ein __Zweig__ ist eine Verbindung zwischen zwei Knoten durch einen oder mehrere hintereinanderliegende Zweipole, ohne einen Knoten dazwischen.
- Eine __Masche__ ist ein geschlossener Weg im Netzwerk, auf dem kein Zweig und kein Knoten mehrfach durchlaufen wird.

Ziel des Ganzen ist die Berechnung, Zusammenfassung und Vereinfachung von Netzwerken. Nicht zu verwechseln sind Zweipole mit __Zweitoren__: Ein
Zweitor ist ein Bauteil mit zwei Klemmenpaaren, also vier Anschlüssen, wie ein Transformator.

**Im Bild:** Kreuzungen, Wegstücke, Rundwege. An einer Kreuzung kann man abbiegen, auf einem Wegstück nicht.

**Zweigstrom und Zweigspannung.** Jeder Zweig hat einen __Zweigstrom__ und eine __Zweigspannung__ zwischen seinen beiden Knoten. Der Zweigstrom ist längs
des ganzen Zweigs derselbe, auch wenn mehrere Bauteile hintereinander darin liegen. In einem Zweig aus Widerständen legt das Ohmsche Gesetz fest, wie
Zweigspannung und Zweigstrom zusammenhängen; in einem Quellenzweig legt die Quelle die Spannung fest.

:::herleitung
Zwischen den beiden Enden eines Zweigs liegt kein Knoten, also keine Abzweigung. Nach der Kontinuität aus dem Artikel über den Strom fließt im
stationären Zustand durch jeden Querschnitt eines unverzweigten Leiters derselbe Strom — Ladung kann sich nirgends anhäufen und hat keinen anderen Weg.
:::

**Was als ein Knoten zählt.** Punkte, die nur durch eine ideale Leitung ohne Bauteil verbunden sind, haben dasselbe Potenzial und bilden zusammen
__einen__ Knoten, auch wenn das Schaltbild mehrere Lötpunkte zeichnet. Ein Punkt, an dem nur zwei Bauteile hintereinander hängen, ist nach dieser
Definition kein Knoten; die beiden Bauteile gehören zu einem Zweig. Manche Bücher zählen solche Punkte trotzdem als Knoten, mit je einem Zweig pro Bauteil.
Wie man sich auch entscheidet, die Zahl der unabhängigen Maschen ändert sich dadurch nicht, wie sich unten zeigt.

**Im Bild:** Eine lange Leitung zwischen zwei Lötpunkten ist wie ein Platz, auf dem mehrere Wege enden: eine einzige Kreuzung, nur breit gezeichnet.
Ein Punkt, an dem ein Weg bloß die Beschilderung wechselt, ist keine Kreuzung.

::::beispiel Knoten zählen an einer Leiterschaltung
Eine Schaltung aus einer Quelle und vier Widerständen, als Leiter gezeichnet:

- links die Quelle $U_\text{q}$ von der unteren Schiene hinauf zum Punkt A;
- oben $R_1$ von A nach B und $R_3$ von B nach C;
- senkrecht $R_2$ von B hinunter und $R_4$ von C hinunter zur unteren Schiene.

Die untere Schiene ist eine durchgehende Leitung mit drei Lötpunkten, an denen die Quelle, $R_2$ und $R_4$ enden; sie ist ein einziger Knoten D.

**Nach der Definition oben** verzweigt sich der Strom nur an B (über $R_1$, $R_2$, $R_3$) und an D (über die Quelle, $R_2$, $R_4$). In A und C hängen nur zwei
Bauteile hintereinander. Also

$$k = 2, \qquad z = 3;$$

die Zweige sind Quelle mit $R_1$, dann $R_2$, dann $R_3$ mit $R_4$.

**Mit jedem Verbindungspunkt als Knoten** zählt man A, B, C, D und ein Zweig pro Bauteil:

$$k = 4, \qquad z = 5.$$

Falsch wäre es, die drei Lötpunkte der unteren Schiene als drei Knoten zu zählen, ohne die Leitungsstücke dazwischen als Zweige mitzunehmen.

**Im Bild:** Zwei echte Kreuzungen, B und D; A und C sind nur Stellen, an denen ein Weg die Beschilderung wechselt.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/04-leiter · Vorlage: leiterschaltung-knoten
Die Leiterschaltung: links die Quelle $U_\text{q}$ (Pluspol oben, Spannungspfeil nach unten), oben $R_1$ von A nach B und $R_3$ von B nach C, senkrecht $R_2$
unter B und $R_4$ unter C, unten eine durchgehende Schiene mit drei Lötpunkten. Ein Schalter „nur Stromverzweigungen" markiert B und D als große rote
Punkte und färbt die drei Zweige in drei Farben (Quelle mit $R_1$, $R_2$, $R_3$ mit $R_4$); ein zweiter Schalter „jeder Verbindungspunkt" markiert
zusätzlich A und C und färbt jedes Bauteil einzeln. Die untere Schiene leuchtet in beiden Fällen als ein einziger Knoten D auf, ihre drei Lötpunkte
verschmelzen beim Hineinzoomen zu einer Fläche gleichen Potenzials. Kernaussage: Ein Knoten ist alles, was ohne Bauteil verbunden ist. (Rot = Knoten,
blau = Zweige, orange = Hervorhebung, grau = Bauteilsymbole.)
:::

## Der Graph eines Netzwerks

Für die Struktur ist gleichgültig, welche Bauteile in den Zweigen sitzen. Ersetzt man jeden Zweig durch eine Linie, bleibt der __Graph__ des Netzwerks,
eine vereinfachte symbolische Darstellung seiner topologischen Struktur. Ein Beispiel ist eine Brückenschaltung mit fünf
Widerständen und einer Quelle, vier Knoten und sechs Zweigen.

- Jeder Zweig bekommt eine __Richtung__, die Richtung des Zählpfeils seines Stroms (Artikel über Zählpfeile). Meist zählt man die Zweigspannung im VZS
  gleichsinnig dazu, dann trägt die eine Richtung beide Pfeile.
- Knoten und Zweige werden durchnummeriert; $k$ ist die Zahl der Knoten, $z$ die Zahl der Zweige.
- Der Graph ist __zusammenhängend__: Von jedem Knoten führt mindestens ein Weg aus Zweigen und Knoten zu jedem anderen.

**Im Bild:** Die Übersichtstafel mit einem Zählpfeil an jedem Wegstück: Wer in Pfeilrichtung geht, zählt plus, wer entgegen geht, minus.

Der Zusammenhang gehört hier zur Definition. In der Mathematik darf ein Graph auch in getrennte Teile zerfallen; elektrisch kommt das vor, wenn zwei
Kreise nur über einen Transformator gekoppelt sind. Darauf kommt der letzte Abschnitt zurück.

:::grafik
Szene: get1/stroeme-und-spannungen/04-graph · Vorlage: schaltung-zu-graph
Die Leiterschaltung aus dem Knotenzählen mit allen fünf Bauteilen und den Knoten A, B, C, D. Ein Regler lässt die Bauteilsymbole schrumpfen, bis nur
Linien übrig sind; jede Linie bekommt einen Richtungspfeil, nummeriert $1$ bis $5$: $1$ Quelle von D nach A, $2$ von A nach B, $3$ von B nach D, $4$ von B
nach C, $5$ von C nach D. Danach lässt sich der Graph frei verformen, Knoten verschieben, Linien biegen — Nummern, Richtungen und Verbindungen bleiben.
Kernaussage: Der Graph enthält nur, was von was abhängt: Knoten, Zweige, Richtungen. (Rot = Knoten, blau = Zweige mit Richtungspfeilen, grau = schrumpfende
Bauteile.)
:::

## Maschen und ihre Unabhängigkeit

Genauer ist eine Masche eine in sich geschlossene Folge von Zweigen und Knoten, in der jeder Knoten mit genau zwei benachbarten Zweigen
der Masche verbunden ist — man kommt an jedem Knoten einmal an und verlässt ihn einmal. Jede Masche bekommt einen __Umlaufsinn__, die Richtung, in der man
sie abläuft, im Schaltbild ein gebogener Pfeil mit dem Namen der Masche, etwa $M_1$.

**Maschen als Vektoren.** Mit den Richtungen der Zweige lässt sich jede Masche als Liste schreiben, ein Eintrag pro Zweig, der __Maschenvektor__:

:::formel Definition
$$\vec c = (c_1, \dots, c_z) \in \mathbb{R}^z,$$

$$c_j = \begin{cases} +1, & j \text{ in Zweigrichtung durchlaufen},\\ -1, & j \text{ entgegen durchlaufen},\\ \ \ 0, & j \text{ nicht in der Masche}.\end{cases}$$
:::

**So liest man das:** Eingabe ist die Masche mit ihrem Umlaufsinn, Ausgabe ein Vektor mit $z$ Einträgen aus $-1$, $0$ und $+1$. Läuft man zwei Maschen
nacheinander, addieren sich ihre Vektoren: Ein Zweig, den die eine in seiner Richtung und die andere entgegen durchläuft, hebt sich heraus.

Maschen heißen __linear unabhängig__, wenn sich keine von ihnen aus den anderen zusammensetzen lässt, genauer: wenn keine Kombination ihrer Vektoren mit
Zahlenfaktoren, die nicht alle null sind, den Nullvektor ergibt. Sonst heißen sie abhängig. Elektrisch ist das der Kern der Sache: Zu jeder Masche gehört
im nächsten Artikel eine Gleichung, die Maschenregel, und die Gleichung einer abhängigen Masche ist dieselbe Kombination der anderen Gleichungen. Sie
bringt keine neue Information.

**Im Bild:** Zwei benachbarte Rundwege nacheinander: Das gemeinsame Wegstück geht man einmal hin und einmal zurück, es fällt heraus, und übrig bleibt die
große Runde. Sie ist kein neuer Rundweg.

**Ein Kriterium.** Eine Folge von Maschen ist linear unabhängig, wenn es eine Reihenfolge gibt, in der jede Masche mindestens einen
Zweig enthält, der in den vorhergehenden nicht vorkommt. Diese Bedingung ist hinreichend: Wer sie erfüllt, ist sicher unabhängig.

:::herleitung
Angenommen, eine Kombination mit Faktoren $a_1, \dots, a_n$, nicht alle null, ergäbe den Nullvektor. Sei $s$ der größte Index mit einem Faktor
ungleich null. Die Masche $s$ enthält einen Zweig, der in keiner der Maschen davor vorkommt, und die Maschen danach haben den Faktor null. In der
Kombination steht an der Stelle dieses Zweigs also nur der Beitrag von Masche $s$:

$$\pm\,a_s \ne 0.$$

Das widerspricht dem Nullvektor. Also gibt es keine solche Kombination.
:::

**Was „vollständig" heißt.** Eine Folge unabhängiger Maschen heißt __vollständig__, wenn keine weitere Masche hinzukommen kann, ohne dass die Folge
abhängig wird — sie ist dann so lang wie möglich, und der Abschnitt *Maschen aus Verbindungszweigen* sagt, wie lang. Falsch wäre es, die
Vollständigkeit so zu beschreiben, dass jede Masche genau einen Zweig enthält, der in den vorhergehenden nicht vorkommt: Schon die erste Masche einer
Folge bringt mehrere neue Zweige mit. Richtig ist eine verwandte Eigenschaft der Maschen aus einem Baum weiter unten: Jede enthält genau einen eigenen
__Verbindungszweig__, der in keiner anderen vorkommt.

::::beispiel Drei Runden, zwei unabhängig
Der Graph der Leiterschaltung mit den Zweigen $1$ (Quelle, D nach A), $2$ (A nach B), $3$ (B nach D), $4$ (B nach C) und $5$ (C nach D). Drei Maschen,
alle im Uhrzeigersinn: das linke Fenster D–A–B–D, das rechte Fenster B–C–D–B und die äußere Runde D–A–B–C–D. Im rechten Fenster wird Zweig $3$ von D
nach B durchlaufen, gegen seine Richtung:

$$\vec c_\text{links} = (1, 1, 1, 0, 0), \qquad \vec c_\text{rechts} = (0, 0, -1, 1, 1), \qquad \vec c_\text{außen} = (1, 1, 0, 1, 1).$$

Die Summe der beiden Fenster ist die äußere Runde:

$$\vec c_\text{links} + \vec c_\text{rechts} = (1, 1, 0, 1, 1) = \vec c_\text{außen}.$$

Nur zwei der drei sind unabhängig.

**Mit Spannungen.** Haben die Knoten die Potenziale

$$\varphi_\text{A} = 10\,\text{V}, \qquad \varphi_\text{B} = 5\,\text{V}, \qquad \varphi_\text{C} = 2{,}5\,\text{V}, \qquad \varphi_\text{D} = 0\,\text{V},$$

ergeben die Spannungen längs jeder Runde nach der Kettenregel aus dem Artikel über Zählpfeile die Summe null:

$$U_\text{AB} + U_\text{BD} + U_\text{DA} = 5\,\text{V} + 5\,\text{V} - 10\,\text{V} = 0,$$

$$U_\text{BC} + U_\text{CD} + U_\text{DB} = 2{,}5\,\text{V} + 2{,}5\,\text{V} - 5\,\text{V} = 0.$$

Addiert man die beiden, heben sich $U_\text{BD}$ und $U_\text{DB}$ weg, und es bleibt die Gleichung der äußeren Runde:

$$U_\text{AB} + U_\text{BC} + U_\text{CD} + U_\text{DA} = 5\,\text{V} + 2{,}5\,\text{V} + 2{,}5\,\text{V} - 10\,\text{V} = 0.$$

**Im Bild:** Wer beide Fenster abwandert, steigt am gemeinsamen Stück einmal ab und einmal auf — die große Runde sagt über die Höhen nichts Neues.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/04-maschen-addieren · Vorlage: maschen-vektoren
Der Graph der Leiterschaltung mit nummerierten, gerichteten Zweigen. Links das Fenster D–A–B–D mit rotem Umlaufpfeil, rechts das Fenster B–C–D–B mit
blauem. Ein Regler „addieren" lässt beide Umläufe gleichzeitig laufen: Auf Zweig $3$ begegnen sich ein roter Pfeil nach unten und ein blauer nach oben und
löschen sich aus; übrig bleibt der orange Umlauf außen herum. Daneben die drei Maschenvektoren als Spalten, die Einträge an Zweig $3$ werden zu $1$ und
$-1$ und summieren sich zu $0$. Kernaussage: Die äußere Runde ist die Summe der beiden Fenster, also nicht unabhängig. (Rot und blau = die beiden
Fenster, orange = Summe, grau = Zweige und Nummern.)
:::

## Der Baum

Ein __Baum__ ist ein Teilgraph, der alle Knoten enthält, zusammenhängend ist und **keine Masche** enthält; oft sagt man __vollständiger Baum__.
Seine Zweige heißen __Baumzweige__, die übrigen __Verbindungszweige__. Ein häufiger Fehler ist, die letzte Bedingung wegzulassen; ohne sie wäre jeder
Graph sein eigener Baum.

:::formel Satz
$$z_\text{Baum} = k - 1;$$

zwischen je zwei Knoten gibt es im Baum genau einen Weg.
:::

**So liest man das:** Jeder Baum eines Graphen mit $k$ Knoten hat genau $k-1$ Zweige, gleich welchen man wählt. Weil er zusammenhängend ist, verbindet
er jedes Knotenpaar; weil er keine Masche hat, gibt es dafür nur einen Weg. Es bleiben $z-(k-1)$ Verbindungszweige.

**Im Bild:** Der Räumplan für den Winter: so wenige Wegstücke wie möglich, und trotzdem ist jede Kreuzung erreichbar. Bei vier Kreuzungen sind es immer
drei Stücke, gleich welche, und von jeder Kreuzung zur anderen gibt es genau einen geräumten Weg.

:::herleitung
**Schritt 1: Ein Baum hat ein Blatt.** Ein __Blatt__ ist ein Knoten, an dem nur ein Baumzweig hängt. Man startet an einem Knoten und geht über
Baumzweige weiter, ohne denselben Zweig zurückzugehen. Ein Knoten kann dabei nicht zum zweiten Mal erreicht werden, sonst hätte man eine Masche
gelaufen. Weil es nur endlich viele Knoten gibt, endet der Weg irgendwann an einem Knoten ohne weiteren Zweig: einem Blatt. (Bei mindestens zwei
Knoten gibt es auch Zweige, denn der Baum ist zusammenhängend.)

**Schritt 2: Abzählen.** Nimmt man ein Blatt samt seinem einzigen Zweig weg, bleibt ein Baum mit einem Knoten und einem Zweig weniger, wieder
zusammenhängend und maschenfrei. Das wiederholt man, bis ein einzelner Knoten ohne Zweig übrig ist. Bei jedem Schritt verschwinden ein Knoten und ein
Zweig; am Ende sind noch ein Knoten und null Zweige da. Also hatte der Baum zu Beginn einen Zweig weniger als Knoten.

**Schritt 3: genau ein Weg.** Mindestens einen Weg gibt es, weil der Baum zusammenhängend ist. Gäbe es zwei verschiedene Wege zwischen denselben Knoten,
liefe man den einen hin und den anderen zurück; von der Stelle, an der sie sich trennen, bis zu der, an der sie sich wieder treffen, entstünde eine
Masche. Der Baum hat aber keine.
:::

Wie viele Bäume ein Graph hat, hängt von seiner Struktur ab. Die Brückenschaltung hat 16: Jeder ihrer vier Knoten ist mit jedem
anderen verbunden, und für einen solchen __vollständigen Graphen__ mit $k$ Knoten gibt es nach einem Satz von Cayley genau $k^{k-2}$ Bäume, hier
$4^2=16$.

::::beispiel Bäume der Leiterschaltung
Die Leiterschaltung hat mit jedem Verbindungspunkt als Knoten vier Knoten und fünf Zweige; jeder Baum hat also

$$z_\text{Baum} = 4 - 1 = 3$$

Zweige. Von den zehn Möglichkeiten, drei der fünf Zweige auszuwählen, sind acht Bäume:

$$\{1,2,4\},\ \{1,2,5\},\ \{1,3,4\},\ \{1,3,5\},\ \{1,4,5\},\ \{2,3,4\},\ \{2,3,5\},\ \{2,4,5\}.$$

Die beiden übrigen Auswahlen enthalten eine Masche und lassen dabei einen Knoten unverbunden: $\{1,2,3\}$ ist das linke Fenster ohne C, $\{3,4,5\}$ das
rechte Fenster ohne A.

**Genau ein Weg.** Im Baum $\{2,3,4\}$, dem Stern um B, führt von A nach C nur der Weg über B, mit den Zweigen $2$ und $4$.

**Im Bild:** Acht verschiedene Räumpläne, jeder mit genau drei geräumten Wegstücken.
::::

## Maschen aus Verbindungszweigen

Ein Baum liefert ein vollständiges System unabhängiger Maschen gleich mit. Nimmt man zum Baum einen einzigen Verbindungszweig hinzu, schließt er mit dem
einen Weg im Baum zwischen seinen Endpunkten genau eine Masche. Jeder Verbindungszweig ergibt so seine eigene Masche, und ihre Anzahl ist die
Zahl der unabhängigen Maschen:

:::formel Satz
$$m = z - k + 1.$$
:::

**So liest man das:** Ein zusammenhängender Graph mit $k$ Knoten und $z$ Zweigen hat genau $m$ linear unabhängige Maschen, die ein vollständiges System
bilden. Eingabe sind zwei Zahlen aus dem Abzählen, Ausgabe die Zahl der Maschengleichungen, die man braucht. Die Bauteile spielen keine Rolle.

**Im Bild:** Jedes nicht geräumte Wegstück würde, geräumt, genau einen Rundweg schließen. Es gibt $z-(k-1)$ solche Stücke, also ebenso viele Rundwege,
und jeder andere Rundweg setzt sich aus ihnen zusammen.

:::herleitung
**Schritt 1: Es gibt so viele.** Ein Baum hat nach dem vorigen Satz $k-1$ Zweige, also gibt es $z-(k-1)$ Verbindungszweige. Jeder schließt mit dem
eindeutigen Baumweg zwischen seinen Endpunkten eine Masche; diese $z-k+1$ Maschen heißen die Maschen des Baums.

**Schritt 2: Sie sind unabhängig.** Jede dieser Maschen enthält ihren Verbindungszweig, und keine andere enthält ihn, denn die anderen bestehen aus
einem anderen Verbindungszweig und Baumzweigen. In einer Kombination der Maschenvektoren steht an der Stelle dieses Zweigs nur der Faktor seiner eigenen
Masche, mit Vorzeichen. Ergibt die Kombination den Nullvektor, sind alle Faktoren null.

**Schritt 3: Mehr gibt es nicht.** Sei $\vec c$ irgendeine Masche. Man zieht von ihr für jeden Verbindungszweig, den sie enthält, dessen Baummasche ab,
mit dem Vorzeichen, mit dem sie ihn durchläuft. Der Rest $\vec d$ enthält keinen Verbindungszweig mehr, nur noch Baumzweige. Außerdem gilt für ihn wie
für jede Masche eine Knotenbilanz: An jedem Knoten heben sich die Einträge der angeschlossenen Zweige auf, gezählt als hinein minus heraus, denn eine
Masche betritt jeden ihrer Knoten so oft, wie sie ihn verlässt, und Summen behalten diese Eigenschaft. An einem Blatt des Baums hängt nur ein
Baumzweig; die Bilanz dort zwingt seinen Eintrag auf null. Man nimmt das Blatt weg und wiederholt das, bis alle Einträge null sind. Also ist $\vec d$ der
Nullvektor, und $\vec c$ ist eine Kombination der Baummaschen — jede weitere Masche ist abhängig, das System ist vollständig.
:::

::::beispiel Maschen aus zwei verschiedenen Bäumen
**(a) Der Stern um B,** Baum $\{2,3,4\}$. Verbindungszweige sind $1$ (Quelle) und $5$. Zweig $1$ geht von D nach A, zurück im Baum von A über B nach D: das
linke Fenster. Zweig $5$ geht von C nach D, zurück im Baum von D über B nach C: das rechte Fenster. Mit vier Knoten und fünf Zweigen:

$$m = 5 - 4 + 1 = 2.$$

**(b) Der Pfad D–A–B–C,** Baum $\{1,2,4\}$. Verbindungszweige sind jetzt $3$ und $5$. Zweig $3$ schließt das linke Fenster, Zweig $5$ aber die äußere
Runde D–A–B–C–D. Ein anderes, ebenso gültiges System aus zwei unabhängigen Maschen.

**(c) Einige Netze im Überblick,** jedes Bauteil als eigener Zweig gezählt:

| Netz | $k$ | $z$ | $m$ |
|---|---|---|---|
| Quelle mit einem Widerstand | $2$ | $2$ | $1$ |
| Quelle mit drei Widerständen parallel | $2$ | $4$ | $3$ |
| Leiterschaltung | $4$ | $5$ | $2$ |
| Brückenschaltung mit fünf Widerständen und Quelle | $4$ | $6$ | $3$ |
| Widerstandswürfel, ein Widerstand pro Kante | $8$ | $12$ | $5$ |

Der Würfel hat $384$ verschiedene Bäume mit je sieben Zweigen, und jeder liefert fünf unabhängige Maschen.

**Im Bild:** Zwei Räumpläne, zwei Sätze von Rundwegen. Beide reichen, um jede andere Runde zusammenzusetzen.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/04-baum-maschen · Vorlage: baum-verbindungszweige
Der Graph der Brückenschaltung: vier Knoten, sechs gerichtete Zweige. Ein gewählter Baum ist schwarz und dick
gezeichnet (drei Zweige), die drei Verbindungszweige grau. Ein Klick auf einen Verbindungszweig färbt ihn rot und lässt den eindeutigen Baumweg zwischen
seinen Endpunkten mitleuchten: Es entsteht eine geschlossene Masche mit Umlaufpfeil $M_1$, $M_2$ oder $M_3$. Ein Schalter blättert durch alle 16 Bäume;
zu jedem erscheinen seine drei Maschen. Ein Zähler zeigt stets drei Baumzweige und drei Maschen. Kernaussage: Jeder Verbindungszweig
schließt genau eine Masche; ein Baum mit $k-1$ Zweigen liefert $z-k+1$ unabhängige Maschen. (Rot = Verbindungszweig und seine Masche, schwarz = Baum,
grau = übrige Verbindungszweige, orange = Umlaufpfeil.)
:::

## Warum gerade so viele Gleichungen

Wie bestimmt man die unbekannten Zweigspannungen und Zweigströme? Die Topologie beantwortet, wie viele Gleichungen dafür
zur Verfügung stehen. Jeder Zweig hat zwei Unbekannte, Strom und Spannung, zusammen $2z$. Dem stehen drei Sorten von Gleichungen gegenüber:

- $z$ __Zweiggleichungen__, eine pro Zweig: das Ohmsche Gesetz in einem Widerstandszweig, die Quellenspannung in einem Quellenzweig;
- $k-1$ unabhängige __Knotengleichungen__ aus der Knotenregel des nächsten Artikels;
- $m$ unabhängige __Maschengleichungen__ aus der Maschenregel des nächsten Artikels, eine pro unabhängiger Masche.

Zusammen sind das genau so viele wie Unbekannte:

$$z + (k - 1) + (z - k + 1) = 2z.$$

**Im Bild:** An jeder Kreuzung eine Zählbilanz der Wanderer, auf jedem unabhängigen Rundweg eine Höhenbilanz und auf jedem Wegstück eine Regel, wie
Steigung und Verkehr zusammenhängen — und keine Bilanz zu viel.

:::herleitung
**Warum nur $k-1$ Knotengleichungen unabhängig sind.** Die Knotenregel verlangt an jedem Knoten, dass sich die Ströme der angeschlossenen Zweige
aufheben. Jeder Zweig verbindet genau zwei Knoten: Sein Strom fließt an dem einen hinein und am anderen heraus. Addiert man alle $k$ Knotengleichungen,
kommt jeder Zweigstrom einmal mit Plus und einmal mit Minus vor, und es bleibt null gleich null. Eine der Gleichungen folgt also aus den übrigen.

**Warum die übrigen $k-1$ unabhängig sind.** Man lässt einen Knoten weg, den Bezugsknoten, und nimmt an, eine Kombination der übrigen Gleichungen mit
Faktoren ergäbe null gleich null; dem Bezugsknoten gibt man den Faktor null. Der Strom eines Zweigs zwischen zwei Knoten kommt in der Kombination mit
der Differenz ihrer Faktoren vor, also müssen benachbarte Knoten denselben Faktor haben. Weil der Graph zusammenhängend ist, reicht diese Gleichheit
vom Bezugsknoten aus zu jedem Knoten: Alle Faktoren sind null.

**Die Maschen.** Dass es genau $z-k+1$ unabhängige Maschen gibt, zeigt der vorige Abschnitt.
:::

**Zweipunkte ändern nichts.** Ob man Punkte, an denen nur zwei Bauteile hintereinander hängen, als Knoten zählt oder nicht, ändert die Zahl der
Maschen nicht. Ein zusätzlicher solcher Knoten teilt einen Zweig in zwei, bringt also einen Knoten und einen Zweig mehr, und in $z-k+1$ heben sich beide
auf.

**Netze aus mehreren Teilen.** Zerfällt ein Netz in $p$ Teile, die nicht leitend miteinander verbunden sind, etwa zwei Kreise an den beiden Wicklungen
eines Transformators, gilt die Formel für jeden Teil einzeln, und insgesamt:

$$m = z - k + p.$$

:::herleitung
Jeder Teil $i$ mit $k_i$ Knoten und $z_i$ Zweigen ist für sich zusammenhängend und hat $z_i-k_i+1$ unabhängige Maschen. Maschen verschiedener Teile
haben keinen gemeinsamen Zweig, also bleiben sie zusammen unabhängig. Summiert über alle $p$ Teile:

$$m = \sum_{i=1}^{p}(z_i - k_i + 1) = z - k + p.$$
:::

::::beispiel Gleichungen der Leiterschaltung
**(a) Jedes Bauteil ein Zweig.** Mit vier Knoten und fünf Zweigen gibt es zehn Unbekannte, fünf Ströme und fünf Spannungen:

$$5 + (4 - 1) + (5 - 4 + 1) = 5 + 3 + 2 = 10.$$

Fünf Zweiggleichungen (die Quellenspannung und viermal Ohm), drei Knotengleichungen (an A, B und C, mit D als Bezugsknoten) und zwei Maschengleichungen
(die beiden Fenster).

**(b) Nur Verzweigungen als Knoten.** Mit den zwei Knoten B und D und drei Zweigen sind es sechs Unbekannte:

$$3 + (2 - 1) + (3 - 2 + 1) = 3 + 1 + 2 = 6.$$

Die Zahl der Maschen ist in beiden Zählweisen zwei. In (a) gibt es vier Unbekannte mehr, weil zwei Zweige in je zwei Bauteile geteilt sind, und dafür
zwei Zweiggleichungen und zwei Knotengleichungen mehr. Die Knotenregeln an A und C sagen nur, dass durch hintereinanderliegende Bauteile derselbe Strom
fließt.

**(c) Zwei Kreise an einem Transformator.** Links eine Quelle mit der ersten Wicklung, rechts die zweite Wicklung mit einem Widerstand, leitend nicht
verbunden. Jeder Kreis hat zwei Knoten und zwei Zweige:

$$m = 4 - 4 + 2 = 2.$$

Jeder Kreis ist eine eigene Masche. Die Formel für zusammenhängende Netze gäbe fälschlich nur eine.

**Im Bild:** Zwei getrennte Wandergebiete ohne Verbindungsweg — jedes hat seinen eigenen Rundweg.
::::

## Bedeutung und Ausblick

Die Topologie ist das Gerüst, an dem die ganze Netzwerkanalyse hängt. Im nächsten Artikel kommen die beiden Kirchhoffschen Regeln: die Knotenregel,
angewandt auf $k-1$ Knoten, und die Maschenregel, angewandt auf $m$ unabhängige Maschen. Welche Maschen das sind, liefert ein Baum ohne Rätselraten.

Die großen Rechenverfahren, das
[Maschenstromverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/maschenstromverfahren/maschenstromverfahren.html) und das
[Knotenpotentialverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/knotenpotentialverfahren/knotenpotentialverfahren.html),
nutzen genau diese Zahlen. Das __Maschenstromverfahren__ führt für jede der $m$ unabhängigen Maschen
einen Strom als Unbekannte ein, das __Knotenpotentialverfahren__ für jeden der $k-1$ Knoten außer dem Bezugsknoten ein Potenzial. Bei der
Brückenschaltung sind das drei Maschenströme oder drei Knotenpotenziale statt zwölf Unbekannten. Schaltungssimulatoren arbeiten mit einer Erweiterung des
Knotenpotentialverfahrens, der modifizierten Knotenpotentialanalyse, die der Artikel zum Knotenpotentialverfahren in einem Exkurs vorstellt.

Weil die Topologie nicht fragt, was in den Zweigen sitzt, gelten alle diese Zahlen ebenso für Wechselstromnetze, für Netze mit Kondensatoren und für
nichtlineare Bauteile — nur die Zweiggleichungen ändern sich.

:::kern
- Die __Topologie__ beschreibt nur, wie ein Netzwerk verbunden ist, nicht, welche Bauteile darin sitzen.
- __Knoten__: Punkt mit Stromverzweigung; alles, was ohne Bauteil verbunden ist, ist ein Knoten.
- __Zweig__: Verbindung zwischen zwei Knoten durch Zweipole; der Strom ist längs des Zweigs überall derselbe.
- __Masche__: geschlossener Weg, der keinen Zweig und keinen Knoten doppelt durchläuft.
- Der __Graph__ ersetzt jeden Zweig durch eine gerichtete Linie; $k$ Knoten, $z$ Zweige.
- Maschen als Vektoren mit Einträgen $-1$, $0$, $+1$; __linear unabhängig__ heißt: keine setzt sich aus den anderen zusammen.
- __Baum__: alle Knoten, zusammenhängend, **keine Masche**; er hat genau $k-1$ Zweige.
- Jeder __Verbindungszweig__ schließt mit dem eindeutigen Baumweg genau eine Masche; zusammen ein vollständiges System.
- Zahl der unabhängigen Maschen: $m=z-k+1$, bei $p$ getrennten Teilen $z-k+p$.
- Gleichungsbilanz: $z$ Zweig-, $k-1$ Knoten- und $m$ Maschengleichungen für $2z$ Unbekannte.
:::

:::quiz
F: Was beschreibt die Topologie eines Netzwerks, und was lässt sie bewusst weg?
A: Nur, welche Knoten durch welche Zweige verbunden sind — das Gerüst, wie es die Übersichtstafel eines Wandergebiets zeigt. Welche Bauteile in den Zweigen sitzen, wie lang oder gekrümmt die Leitungen sind, spielt keine Rolle. Darum gelten ihre Zahlen für Gleich- und Wechselstromnetze ebenso wie für nichtlineare Bauteile.
F: Warum bilden die Lötpunkte einer durchgehenden Masseschiene nur einen Knoten?
A: Punkte, die nur durch eine ideale Leitung ohne Bauteil verbunden sind, haben dasselbe Potenzial; sie bilden zusammen einen Knoten. Zählte man sie einzeln, müsste man die Leitungsstücke dazwischen als zusätzliche Zweige mitnehmen, die nichts beitragen.
F: Warum ist der Strom längs eines Zweigs überall derselbe?
A: Zwischen den Enden eines Zweigs liegt kein Knoten, also keine Abzweigung. Nach der Kontinuität fließt im stationären Zustand durch jeden Querschnitt eines unverzweigten Leiters derselbe Strom, auch wenn mehrere Bauteile hintereinanderliegen.
F: Wann sind Maschen linear unabhängig, und warum ist das elektrisch wichtig?
A: Wenn sich keine aus den anderen zusammensetzen lässt, genauer: wenn keine Kombination ihrer Maschenvektoren mit nicht lauter verschwindenden Faktoren den Nullvektor ergibt. Zu jeder Masche gehört eine Maschengleichung, und die einer abhängigen Masche ist dieselbe Kombination der anderen Gleichungen — sie bringt nichts Neues.
F: Warum ist in der Leiterschaltung die äußere Runde nicht unabhängig von den beiden Fenstern?
A: Läuft man beide Fenster im Uhrzeigersinn, wird der gemeinsame Zweig einmal in und einmal gegen seine Richtung durchlaufen und hebt sich heraus: $(1,1,1,0,0)+(0,0,-1,1,1)=(1,1,0,1,1)$, der Vektor der äußeren Runde. Auch die Spannungssummen addieren sich so: Die Gleichung der äußeren Runde ist die Summe der beiden anderen.
F: Welche Bedingung darf in der Definition des Baums nicht fehlen, und was folgt aus der vollständigen Definition?
A: Ein Baum darf keine Masche enthalten; sonst wäre jeder zusammenhängende Graph sein eigener Baum. Mit dieser Bedingung hat jeder Baum genau $k-1$ Zweige: Man nimmt immer wieder ein Blatt samt Zweig weg, bis ein Knoten übrig bleibt. Zwischen zwei Knoten gibt es im Baum genau einen Weg.
F: Warum liefert jeder Verbindungszweig genau eine Masche, und warum sind diese Maschen unabhängig?
A: Zusammen mit dem eindeutigen Baumweg zwischen seinen Endpunkten schließt der Verbindungszweig genau eine Masche. Jede dieser Maschen enthält ihren eigenen Verbindungszweig, den keine andere enthält; in einer Kombination, die null ergibt, muss deshalb jeder Faktor null sein.
F: Warum gibt es nicht mehr als $z-k+1$ unabhängige Maschen?
A: Zieht man von einer beliebigen Masche für jeden ihrer Verbindungszweige dessen Baummasche ab, bleibt ein Rest nur auf Baumzweigen, der an jedem Knoten eine ausgeglichene Bilanz hat. An einem Blatt muss der einzige Eintrag dann null sein; Blatt für Blatt wird der ganze Rest null. Jede Masche ist also eine Kombination der $z-k+1$ Baummaschen.
F: Wie viele Gleichungen braucht ein Netzwerk, und woher kommen sie?
A: Jeder Zweig hat Strom und Spannung, zusammen $2z$ Unbekannte. Dafür gibt es $z$ Zweiggleichungen (Ohm oder Quelle), $k-1$ unabhängige Knotengleichungen und $m=z-k+1$ unabhängige Maschengleichungen, zusammen genau $2z$. Bei der Leiterschaltung sind das $5+3+2=10$.
F: Warum ändert sich die Zahl der Maschen nicht, wenn man Punkte zwischen zwei Bauteilen als Knoten zählt, und was ändert sich bei getrennten Netzteilen?
A: Ein solcher Punkt teilt einen Zweig in zwei: ein Knoten und ein Zweig mehr, die sich in $z-k+1$ aufheben. Zerfällt ein Netz dagegen in $p$ leitend getrennte Teile, etwa zwei Kreise an einem Transformator, gilt die Formel für jeden Teil, und insgesamt $m=z-k+p$ — bei zwei einfachen Kreisen zwei Maschen statt einer.
:::
