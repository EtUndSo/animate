---
title: Zweitore und ihre Parameter
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70600
summary: Von Grund auf – wie man ein Netz mit einem Eingang und einem Ausgang als verschlossenen Kasten beschreibt, nur durch Spannungen und Ströme an seinen zwei Toren. Leitbild ist ein Rohrkasten mit zwei Anschlusspaaren, den man mit geschlossenem oder offenem Hahn befragt. Mit Tor und Torbedingung, Vierpol und Zweitor, Kennlinien, den Widerstands-, Leitwert-, Hybrid- und Kettenparametern samt Leerlauf- und Kurzschlussversuchen, Ersatzschaltbildern mit gesteuerten Quellen, Eingangswiderständen im Betrieb, der vollständigen Umrechnungstabelle, der Kettenschaltung als Matrizenprodukt und den Eigenschaften umkehrbar, rückwirkungsfrei, aktiv und passiv. Mit Beispiel-Seite.
tags: Zweitor, Vierpol, Widerstandsform, Leitwertform, Hybridparameter, Kettenparameter
---

## Anschaulich

Zwischen einer Quelle und einem Verbraucher liegt oft ein weiteres Netz mit einem Eingang und einem Ausgang: eine Leitung, ein Filter, ein
Dämpfungsglied, ein Verstärker. Wer es einsetzt, braucht nicht seinen inneren Aufbau, sondern nur, wie Spannungen und Ströme am Eingang mit denen am
Ausgang zusammenhängen. Ein solches Netz heißt __Zweitor__, und sein ganzes Verhalten steckt in vier Zahlen.

**Das Leitbild dieses Artikels:** **Der verschlossene Rohrkasten.** Ein Kasten voller Rohre, aus dem links und rechts je ein Paar Anschlüsse ragt, Zulauf
und Rücklauf. Hineinsehen kann man nicht; man kann nur an beiden Seiten Druck und Durchfluss messen und vorgeben. Die Rohre sollen linear sein, der
Druckverlust proportional zum Durchfluss.

Drei Folgerungen:

- **Vier Größen, zwei Gleichungen.** Gibt man an beiden Seiten etwas vor, etwa die beiden Durchflüsse, stellen sich die beiden Drücke ein. Zwei der vier
  Größen sind frei, die anderen beiden folgen — mit zwei linearen Gleichungen und vier Faktoren, die nur vom Inneren des Kastens abhängen.
- **Vier Arten zu fragen.** Man kann die Durchflüsse vorgeben und nach den Drücken fragen, die Drücke vorgeben und nach den Durchflüssen, links den
  Durchfluss und rechts den Druck, oder fragen, was man links liefern muss, damit rechts ein bestimmter Druck und Durchfluss herauskommt. Jede Frage
  ergibt einen eigenen Satz von vier Zahlen, alle über denselben Kasten.
- **Messen mit geschlossenem oder offenem Hahn.** Die vier Zahlen findet man, indem man eine Seite schließt, sodass dort nichts fließt, oder sie drucklos
  öffnet, und an der anderen Seite einspeist.

:::grafik
Szene: get1/analyse-linearer-netzwerke/06-rohrkasten · Vorlage: rohrkasten-zweitor
Ein grauer, verschlossener Kasten mit je einem Anschlusspaar links und rechts, an jedem Paar ein Manometer und eine Wasseruhr. Links eine Pumpe, rechts
wahlweise ein geschlossener Hahn, ein drucklos offener Auslauf oder ein Verbraucher. Ein Schalter „durchleuchten" macht den Inhalt sichtbar: ein
Rohrnetz aus einem Längsrohr, einem Querrohr und einem zweiten Längsrohr. Mit geschlossenem Hahn rechts zeigen die Anzeigen Druck links, Druck rechts und
Durchfluss links; mit offenem Auslauf Durchfluss rechts statt Druck. Vier Felder unter dem Kasten füllen sich mit den Quotienten, die die beiden Versuche
liefern. Kernaussage: Ein Zweitor ist durch vier Zahlen vollständig beschrieben, gemessen mit geschlossener oder offener Gegenseite. (Blau = Wasser und
Anzeigen, rot = Kasten und Tore, orange = gemessene Quotienten, grau = Rohre im Inneren.)
:::

## Vom Vierpol zum Zweitor

Ein Netz mit vier Anschlussklemmen heißt __Vierpol__. Seine vier Klemmenströme $I_1$ bis $I_4$, alle hineinfließend gezählt, und die
Spannungen zwischen den Klemmen sind nicht unabhängig: Nach der Knotenregel für eine Hülle um den Vierpol und nach der Maschenregel um die vier Klemmen
gilt

$$I_1 + I_2 + I_3 + I_4 = 0, \qquad U_{13} + U_{34} - U_{24} + U_{21} = 0,$$

sodass nur je drei Ströme und drei Spannungen frei sind. Fasst man je zwei Klemmen zu einem __Tor__ zusammen, Klemmen 1 und 1' links, 2 und 2' rechts, wird
daraus ein __Zweitor__, wenn an jedem Tor der Strom, der in die eine Klemme hineinfließt, aus der anderen wieder herausfließt:

:::formel Definition
$$I_1 = I'_1 = -I_3, \qquad I_2 = I'_2 = -I_4.$$
:::

**So liest man das:** Das ist die __Torbedingung__, mit $I'_1$ und $I'_2$ als den Strömen, die aus den Klemmen 1' und 2' herausfließen; im Vierpol sind das
die Klemmen 3 und 4, deren Ströme hineingezählt waren, daher das Minus. Sie gilt von selbst,
wenn an jedem Tor ein eigener Zweipol hängt, links etwa eine Quelle und rechts ein Verbraucher. Ob ein Vierpol ein Zweitor ist, hängt also von
seiner Beschaltung ab: Verbinden äußere Leitungen die beiden Seiten, kann die Bedingung verletzt sein, und die Zweitorbeschreibung gilt nicht mehr.
Ein Zweitor hat dann nur noch zwei Ströme $I_1$, $I_2$ und zwei Torspannungen $U_1$, $U_2$; die Energie fließt meist vom __Eingangstor__ 1 zum
__Ausgangstor__ 2, in __Vorwärtsrichtung__.

**Im Bild:** Was links durch den Zulauf in den Kasten fließt, kommt links durch den Rücklauf wieder heraus, solange außen nichts die linke mit der rechten
Seite verbindet.

:::herleitung
**Drei freie Ströme.** Eine Hülle um den Vierpol schneidet nur die vier Anschlussleitungen; nach der Knotenregel für Hüllen, wie im Artikel über
Ersatzquellen, ist die Summe der hineinfließenden Ströme null. Drei Ströme legen also den vierten fest.

**Drei freie Spannungen.** Die Spannungen zwischen den Klemmen sind Potenzialdifferenzen; eine Masche über alle vier Klemmen ergibt die zweite Gleichung,
und mit drei Spannungen, etwa gegen eine gemeinsame Klemme, sind alle anderen bestimmt.

**Die Torbedingung von selbst.** Hängt am linken Tor ein Zweipol, der sonst mit nichts verbunden ist, legt man eine Hülle um diesen Zweipol. Sie schneidet
nur die beiden Leitungen zu den Klemmen 1 und 1'; was durch die eine zum Vierpol fließt, muss durch die andere zurück. Im Bild: Eine Pumpe, die nur an den
linken Anschlüssen hängt, kann Wasser nur im Kreis durch diese beiden schicken.
:::

::::beispiel Ein Vierpol, der kein Zweitor mehr ist
Ein Kasten mit einem Längswiderstand in der oberen und einem in der unteren Leitung ist links an eine Quelle angeschlossen und rechts an einen
Verbraucher:

$$U_q = 10\,\text{V}, \qquad R_\text{oben} = R_\text{unten} = 100\,\Omega, \qquad R_L = 200\,\Omega.$$

**Als Zweitor betrieben.** Alles liegt in einer einzigen Masche, und durch beide Klemmen jedes Tores fließt derselbe Strom:

$$I_1 = I'_1 = \frac{10\,\text{V}}{100\,\Omega + 200\,\Omega + 100\,\Omega} = 25\,\text{mA}.$$

**Mit einer Masseverbindung.** Werden die beiden unteren Klemmen außen durch einen Draht verbunden, etwa weil Quelle und Verbraucher am selben Gehäuse
liegen, wird der untere Widerstand überbrückt. An ihm liegt keine Spannung mehr, und durch die Klemme 1' fließt nichts:

$$I_1 = \frac{10\,\text{V}}{100\,\Omega + 200\,\Omega} \approx 33{,}3\,\text{mA}, \qquad I'_1 = 0.$$

Die Torbedingung ist verletzt; der Strom kehrt durch den äußeren Draht zurück, und Zweitorparameter, die man ohne den Draht bestimmt hat, gelten nicht
mehr.

**Im Bild:** Eine Querverbindung außen zwischen dem linken und dem rechten Rücklauf: Das Wasser nimmt die Abkürzung, statt durch den Kasten
zurückzufließen.
::::

Ein paar Begriffe ordnen die Zweitore:

- __Erdunsymmetrisch__ ist ein Zweitor, dessen untere Klemmen innen durch eine durchgehende Leitung verbunden sind, die __Masse__; eigentlich ist es ein
  Dreipol. So sind die meisten Modelle von Transistoren und Verstärkern gebaut. __Erdsymmetrisch__ ist eines, das zu einer waagrechten Linie
  spiegelsymmetrisch ist, wie die Brückenschaltung; dort ist, wie das Beispiel zeigt, eine äußere Masseverbindung heikel.
- Zweitore sind __linear__ und zeitunabhängig, __zeitabhängig__ oder __nichtlinear__. Hier geht es um lineare, zeitunabhängige; nichtlineare kommen mit
  den Transistoren.
- __Aktive__ Zweitore können am Ausgang mehr Leistung abgeben, als sie am Eingang aufnehmen; die Energie dafür liefert eine Hilfsquelle, etwa die
  Versorgungsspannung eines Verstärkers. __Passive__ können das nicht. Der Abschnitt über Zweitoreigenschaften macht beides genau.

Für die Zählpfeile gibt es zwei Gewohnheiten. Im __symmetrischen__ Pfeilsystem, einem Verbraucherzählpfeilsystem an beiden Toren, fließen beide
Ströme in das Zweitor hinein; es gilt hier für alle Formen außer der Kettenform. Im __Kettenpfeilsystem__ fließt der Ausgangsstrom zum Verbraucher hinaus;
die Kettenform behält deshalb den hineinfließenden Strom $I_2$ und schreibt den hinausfließenden als $-I_2$.

## Zweitorgleichungen und Kennlinien

Ein Zweitor wird durch zwei Gleichungen zwischen den vier Torgrößen vollständig beschrieben, etwa die Ströme als Funktionen der Spannungen oder
umgekehrt:

$$I_1 = f_1(U_1, U_2), \qquad I_2 = g_1(U_1, U_2) \qquad\text{oder}\qquad U_1 = f_2(I_1, I_2), \qquad U_2 = g_2(I_1, I_2).$$

Bei einem linearen Zweitor sind diese Funktionen linear, jede eine Summe der beiden unabhängigen Größen mit festen Faktoren. Trägt man eine Torgröße über
einer anderen auf und hält die dritte als __Parameter__ fest, entstehen __Kennlinien__:

- die __Eingangskennlinie__, $I_1$ über $U_1$, mit $U_2$ als Parameter;
- die __Übertragungskennlinie__, $I_2$ über $U_1$, mit $U_2$ als Parameter;
- die __Ausgangskennlinie__, $I_2$ über $U_2$, mit $U_1$ als Parameter.

**So liest man das:** Jeder Wert des Parameters ergibt eine Kennlinie, zusammen eine __Kurvenschar__; bei einem linearen Zweitor sind es parallele
Geraden. Dieselbe Beschreibung passt auf ein größeres Netz, von dem man nur zwei Tore betrachtet, auf einen Transformator oder einen Transistor, bei diesem
für kleine Änderungen um einen Arbeitspunkt.

**Im Bild:** Druck und Durchfluss links, Druck und Durchfluss rechts: Zwei davon gibt man vor, zwei stellen sich ein.

:::herleitung
**Zwei Gleichungen genügen.** Man denkt sich an beide Tore Spannungsquellen mit $U_1$ und $U_2$. Wie im Artikel über Ersatzquellen gezeigt, ist jeder Strom
im linearen Netz dann eine Summe der vorgegebenen Größen mit festen Faktoren, die nur von den Bauteilen abhängen; insbesondere $I_1$ und $I_2$. Damit sind
die zwei Gleichungen gefunden; jede andere Beschaltung der Tore trifft einen ihrer Lösungspunkte.

**Parallele Geraden.** In einer linearen Gleichung, etwa für $I_1$, ändert der Parameter $U_2$ nur den festen Anteil; die Steigung über $U_1$ bleibt
dieselbe.
:::

::::beispiel Kennlinien eines Längs- und eines Querleitwerts
Ein Zweitor aus einem Querleitwert $G_1$ am Eingang und einem Längsleitwert $G_2$ zum Ausgang:

$$G_1 = 10\,\text{mS}, \qquad G_2 = 5\,\text{mS}, \qquad I_1 = (G_1 + G_2)\,U_1 - G_2\,U_2, \qquad I_2 = -G_2\,U_1 + G_2\,U_2.$$

Die Gleichungen folgen aus der Knotenregel: In die linke Klemme fließen der Strom durch $G_1$ und der durch $G_2$ hinüber, in die rechte nur dieser zurück.

**Ein Betriebspunkt** mit $4\,\text{V}$ links und $2\,\text{V}$ rechts:

$$I_1 = 15\,\text{mS}\cdot4\,\text{V} - 5\,\text{mS}\cdot2\,\text{V} = 50\,\text{mA}, \qquad I_2 = -5\,\text{mS}\cdot4\,\text{V} + 5\,\text{mS}\cdot2\,\text{V} = -10\,\text{mA}.$$

Durch $G_1$ fließen $40\,\text{mA}$, durch $G_2$ $10\,\text{mA}$ nach rechts, die das rechte Tor verlassen, daher das Minus.

**Die Kennlinien.** Die Eingangskennlinie hat die Steigung $15\,\text{mS}$ und rückt mit $U_2$ gleich $2\,\text{V}$ um $10\,\text{mA}$ nach unten; die
Übertragungskennlinie fällt mit $5\,\text{mS}$, die Ausgangskennlinie steigt mit $5\,\text{mS}$.

**Im Bild:** Ein Querrohr links und ein Längsrohr nach rechts: Links fließt Wasser durch beide ab, rechts kommt an, was durch das Längsrohr geht.
::::

## Widerstandsform

Gibt man die beiden Ströme vor, sind die Spannungen lineare Funktionen von ihnen, die __Widerstandsform__:

:::formel Definition
$$U_1 = Z_{11}\,I_1 + Z_{12}\,I_2, \qquad U_2 = Z_{21}\,I_1 + Z_{22}\,I_2, \qquad \begin{pmatrix} U_1 \\ U_2 \end{pmatrix} = \mathbf Z \begin{pmatrix} I_1 \\ I_2 \end{pmatrix}, \qquad \mathbf Z = \begin{pmatrix} Z_{11} & Z_{12} \\ Z_{21} & Z_{22} \end{pmatrix}.$$
:::

**So liest man das:** Die vier __Widerstandsparameter__ oder Z-Parameter haben die Einheit Ohm und hängen nur vom Zweitor ab. Der Buchstabe Z erinnert an
die Impedanz, den Widerstand der Wechselstromtechnik; für ein Netz aus Widerständen sind die Parameter einfach Widerstände. Jeden misst man im
__Leerlaufversuch__: Man lässt ein Tor offen, sodass dort kein Strom fließt, und prägt am anderen einen Strom ein:

$$Z_{11} = \frac{U_1}{I_1}\Big|_{I_2 = 0}, \qquad Z_{21} = \frac{U_2}{I_1}\Big|_{I_2 = 0}, \qquad Z_{12} = \frac{U_1}{I_2}\Big|_{I_1 = 0}, \qquad Z_{22} = \frac{U_2}{I_2}\Big|_{I_1 = 0}.$$

$Z_{11}$ ist der __Eingangsleerlaufwiderstand__, $Z_{22}$ der __Ausgangsleerlaufwiderstand__; $Z_{21}$ und $Z_{12}$ sind die
__Leerlaufübertragungswiderstände__ vorwärts und rückwärts. Parameter mit gleichen Indizes heißen __Zweipolgrößen__, denn sie beschreiben ein Tor allein,
die übrigen __Übertragungsgrößen__.

**Im Bild:** Hahn rechts zu, links eine feste Menge hineinpumpen und die Drücke an beiden Seiten ablesen: Druck pro Durchfluss.

:::herleitung
**Ein Strom null.** Mit $I_2$ gleich null bleibt in beiden Gleichungen nur der Anteil von $I_1$:

$$U_1 = Z_{11}\,I_1, \qquad U_2 = Z_{21}\,I_1;$$

geteilt durch $I_1$ ergibt das $Z_{11}$ und $Z_{21}$. Ebenso mit $I_1$ gleich null die beiden anderen. Weil die Gleichungen linear sind, genügen diese zwei
Versuche, um die Spannungen für jede Kombination der Ströme vorherzusagen.
:::

::::beispiel Z-Parameter einer T-Schaltung und einer Brücke
**(a) Die T-Schaltung** aus einem Längswiderstand $R_1$ am Eingang, einem Querwiderstand $R_2$ und einem Längswiderstand $R_3$ am Ausgang:

$$R_1 = 100\,\Omega, \qquad R_2 = 300\,\Omega, \qquad R_3 = 200\,\Omega.$$

Bei offenem Ausgang fließt $I_1$ durch $R_1$ und $R_2$, und an $R_3$ fällt nichts ab, sodass $U_2$ die Spannung an $R_2$ ist; umgekehrt ebenso:

$$Z_{11} = R_1 + R_2 = 400\,\Omega, \qquad Z_{21} = Z_{12} = R_2 = 300\,\Omega, \qquad Z_{22} = R_2 + R_3 = 500\,\Omega.$$

**(b) Eine Brücke als Zweitor.** In einer Brücke liegt das Eingangstor an den Ecken, an denen sonst die Quelle hängt, das Ausgangstor in der Diagonale.
Umgezeichnet führt von der Eingangsklemme 1 ein Widerstand $R_a$ zur Ausgangsklemme 2 und ein $R_b$ zur Klemme 2', von der Klemme 1' ein $R_a$
zu 2' und ein $R_b$ zu 2:

$$R_a = 100\,\Omega, \qquad R_b = 300\,\Omega.$$

Bei offenem Ausgang teilt sich $I_1$ zu gleichen Hälften auf zwei Wege aus je $R_a + R_b$, und das Ausgangstor greift den Unterschied der beiden
Teilerspannungen ab:

$$Z_{11} = Z_{22} = \frac{R_a + R_b}{2} = 200\,\Omega, \qquad Z_{21} = Z_{12} = \frac{R_b - R_a}{2} = 100\,\Omega.$$

Bei gleichen Widerständen ist die Brücke abgeglichen, wie im Artikel über die Wheatstone-Brücke, und der Übertragungswiderstand wird null: Am Ausgang kommt
nichts an.

**Im Bild:** Ein Kasten mit drei Rohren in T-Form: Durch das Querrohr fließt bei geschlossenem rechtem Hahn alles, und sein Druckverlust ist der Druck
rechts.
::::

Die Gleichungen lassen sich als Schaltung lesen, das __Ersatzschaltbild__ der Widerstandsform. Es braucht ein neues Bauteil, die __gesteuerte
Quelle__: eine ideale Quelle, deren Wert von einer Spannung oder einem Strom an anderer Stelle abhängt. Hier sind es zwei __stromgesteuerte
Spannungsquellen__ (englisch *current-controlled voltage source*, CCVS). Am Eingang liegt $Z_{11}$ in Reihe mit einer Quelle $Z_{12} I_2$, die der
Ausgangsstrom steuert, am Ausgang $Z_{22}$ in Reihe mit einer Quelle $Z_{21} I_1$, die der Eingangsstrom steuert. Achtung, Indizes: Der erste nennt das Tor, an dem die
Quelle sitzt, der zweite das Tor des steuernden Stroms.

Hängt am Ausgang ein Lastwiderstand $R_L$, fließt der Strom $I_2$, im symmetrischen Pfeilsystem in das Zweitor hineingezählt, durch die Last hinaus. Der
Eingangswiderstand hängt dann von der Last ab:

:::formel
$$Z_1 = \frac{U_1}{I_1} = Z_{11} - \frac{Z_{12}\,Z_{21}}{Z_{22} + R_L}, \qquad Z_{1,LL} = Z_{11}, \qquad Z_{1,KS} = Z_{11} - \frac{Z_{12}\,Z_{21}}{Z_{22}}.$$
:::

**So liest man das:** Bei offenem Ausgang ist der Eingangswiderstand $Z_{11}$, bei kurzgeschlossenem um $Z_{12}Z_{21}/Z_{22}$ kleiner, dazwischen liegt jede
Last. Verantwortlich ist $Z_{12}$, die __Rückwirkung__ des Ausgangs auf den Eingang. Ist sie null, ist der Eingangswiderstand bei jeder Last $Z_{11}$, und
das Zweitor heißt __rückwirkungsfrei__.

**Im Bild:** Was rechts angeschlossen ist, bestimmt mit, wie leicht das Wasser durch den Kasten fließt, und das spürt die Pumpe links — außer der Kasten
lässt nichts von rechts nach links zurückwirken.

:::herleitung
**Die rechte Masche.** An der Last ist $U_2$ gleich $-R_L I_2$; gleichgesetzt mit der zweiten Zweitorgleichung:

$$Z_{21}\,I_1 + Z_{22}\,I_2 = -R_L\,I_2, \qquad I_2 = -\frac{Z_{21}}{Z_{22} + R_L}\,I_1.$$

**Die linke Masche.** In die erste Zweitorgleichung eingesetzt und durch $I_1$ geteilt:

$$Z_1 = \frac{Z_{11}\,I_1 + Z_{12}\,I_2}{I_1} = Z_{11} - \frac{Z_{12}\,Z_{21}}{Z_{22} + R_L}.$$

**Grenzfälle.** Für sehr großes $R_L$ verschwindet der Bruch, das ist der Leerlauf; mit $R_L$ gleich null bleibt der Kurzschlusswert.
:::

::::beispiel Die T-Schaltung unter Last
Die T-Schaltung von oben mit ihrer Widerstandsmatrix:

$$R_1 = 100\,\Omega, \qquad R_2 = 300\,\Omega, \qquad R_3 = 200\,\Omega, \qquad \mathbf Z = \begin{pmatrix} 400 & 300 \\ 300 & 500 \end{pmatrix}\Omega.$$

**Eingangswiderstände:**

$$Z_{1,LL} = 400\,\Omega, \qquad Z_{1,KS} = 400\,\Omega - \frac{300\cdot300}{500}\,\Omega = 220\,\Omega, \qquad Z_1\big|_{R_L = 100\,\Omega} = 400\,\Omega - \frac{90\,000}{600}\,\Omega = 250\,\Omega.$$

**Probe** an der Schaltung selbst, mit Reihen- und Parallelschaltung:

$$R_1 + R_2 \parallel R_3 = 100\,\Omega + 120\,\Omega = 220\,\Omega, \qquad R_1 + R_2 \parallel (R_3 + R_L) = 100\,\Omega + 150\,\Omega = 250\,\Omega.$$

**Übertragung bei 100 Ohm Last:** Der Ausgangsstrom ist halb so groß wie der Eingangsstrom und fließt hinaus; die Ausgangsspannung ist ein Fünftel der
Eingangsspannung:

$$\frac{I_2}{I_1} = -\frac{300}{500 + 100} = -0{,}5, \qquad \frac{U_2}{U_1} = \frac{-R_L\,I_2}{Z_1\,I_1} = \frac{100\,\Omega\cdot0{,}5}{250\,\Omega} = 0{,}2.$$

**Im Bild:** Ein Verbraucher rechts öffnet dem Wasser einen zweiten Weg neben dem Querrohr; der Kasten wird von links gesehen durchlässiger.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/06-z-ersatzschaltbild · Vorlage: zweitor-z-esb
Links eine Stromquelle $I_q$ am Eingangstor, rechts ein verstellbarer Lastwiderstand $R_L$. Dazwischen das
Ersatzschaltbild der Widerstandsform: am Eingang $Z_{11} = 400\,\Omega$ in Reihe mit einer stromgesteuerten Spannungsquelle $Z_{12} I_2$, am Ausgang
$Z_{22} = 500\,\Omega$ in Reihe mit $Z_{21} I_1$, beide Quellen als Rauten mit Spannungspfeilen nach unten; $I_1$ fließt in Klemme 1, $I_2$ in Klemme 2
hinein, $U_1$ und $U_2$ zeigen nach unten. Gestrichelte Pfeile verbinden jede gesteuerte Quelle mit dem Strom, der sie steuert. Der Lastregler fährt von
Kurzschluss bis Leerlauf; eine Anzeige zeigt $Z_1$ von $220\,\Omega$ bis $400\,\Omega$, bei $100\,\Omega$ den Wert $250\,\Omega$. Ein Schalter setzt $Z_{12}$ auf
null, und die Anzeige bleibt bei jeder Last auf $400\,\Omega$. Kernaussage: Die Rückwirkung $Z_{12}$ macht den Eingangswiderstand lastabhängig. (Rot =
gesteuerte Quellen, blau = Torgrößen, orange = Steuerpfeile, grau = Widerstände.)
:::

## Leitwertform

Gibt man die beiden Spannungen vor, sind die Ströme lineare Funktionen von ihnen, die __Leitwertform__:

:::formel Definition
$$I_1 = Y_{11}\,U_1 + Y_{12}\,U_2, \qquad I_2 = Y_{21}\,U_1 + Y_{22}\,U_2, \qquad \begin{pmatrix} I_1 \\ I_2 \end{pmatrix} = \mathbf Y \begin{pmatrix} U_1 \\ U_2 \end{pmatrix}.$$
:::

**So liest man das:** Die vier __Leitwertparameter__ oder Y-Parameter haben die Einheit Siemens. Man misst sie im __Kurzschlussversuch__: Ein Tor
wird kurzgeschlossen, sodass seine Spannung null ist, und am anderen wird eine Spannung eingeprägt:

$$Y_{11} = \frac{I_1}{U_1}\Big|_{U_2 = 0}, \qquad Y_{21} = \frac{I_2}{U_1}\Big|_{U_2 = 0}, \qquad Y_{12} = \frac{I_1}{U_2}\Big|_{U_1 = 0}, \qquad Y_{22} = \frac{I_2}{U_2}\Big|_{U_1 = 0}.$$

$Y_{11}$ ist der __Kurzschlusseingangsleitwert__, $Y_{22}$ der __Kurzschlussausgangsleitwert__, $Y_{21}$ der Kurzschlussübertragungsleitwert vorwärts, bei
Transistoren __Steilheit__ genannt, $Y_{12}$ der rückwärts. Im Ersatzschaltbild liegen am Eingang $Y_{11}$ und eine __spannungsgesteuerte
Stromquelle__ (*voltage-controlled current source*, VCCS) $Y_{12} U_2$ parallel, am Ausgang $Y_{22}$ und die Quelle $Y_{21} U_1$. Mit einem Lastleitwert $G_L$
am Ausgang gilt für den Eingangsleitwert, ganz entsprechend zur Widerstandsform:

$$Y_1 = \frac{I_1}{U_1} = Y_{11} - \frac{Y_{12}\,Y_{21}}{Y_{22} + G_L}, \qquad Y_{1,KS} = Y_{11}, \qquad Y_{1,LL} = Y_{11} - \frac{Y_{12}\,Y_{21}}{Y_{22}}.$$

**Im Bild:** Rechts drucklos offen, links einen festen Druck anlegen und die Durchflüsse an beiden Seiten messen: Durchfluss pro Druck.

:::herleitung
**Eine Spannung null.** Mit $U_2$ gleich null bleiben die Anteile von $U_1$; geteilt durch $U_1$ ergeben sie $Y_{11}$ und $Y_{21}$, ebenso mit $U_1$ gleich null
die beiden anderen.

**Eingangsleitwert unter Last.** Am Lastleitwert fließt der Strom hinaus, $I_2$ ist $-G_L U_2$. Gleichgesetzt mit der zweiten Gleichung und in die erste
eingesetzt:

$$Y_{21}\,U_1 + Y_{22}\,U_2 = -G_L\,U_2, \qquad U_2 = -\frac{Y_{21}}{Y_{22} + G_L}\,U_1, \qquad Y_1 = Y_{11} - \frac{Y_{12}\,Y_{21}}{Y_{22} + G_L}.$$

Mit $G_L$ unendlich groß, also kurzgeschlossenem Ausgang, bleibt $Y_{11}$; mit $G_L$ gleich null, also Leerlauf, der dritte Ausdruck.
:::

::::beispiel Die Leitwertmatrix einer π-Schaltung
Eine π-Schaltung aus einem Querleitwert $G_1$ am Eingang, einem Längsleitwert $G_2$ und einem Querleitwert $G_3$ am Ausgang:

$$G_1 = 2\,\text{mS}, \qquad G_2 = 5\,\text{mS}, \qquad G_3 = 1\,\text{mS}.$$

**Kurzschlussversuche.** Mit kurzgeschlossenem Ausgang fließt $I_1$ durch $G_1$ und $G_2$, und durch $G_2$ fließt Strom aus dem Ausgangstor hinaus;
umgekehrt ebenso:

$$\mathbf Y = \begin{pmatrix} G_1 + G_2 & -G_2 \\ -G_2 & G_2 + G_3 \end{pmatrix} = \begin{pmatrix} 7 & -5 \\ -5 & 6 \end{pmatrix}\text{mS}.$$

**Eingangsleitwert** bei offenem Ausgang und mit einer Last von $250\,\Omega$, also $4\,\text{mS}$:

$$Y_{1,LL} = 7\,\text{mS} - \frac{25}{6}\,\text{mS} \approx 2{,}83\,\text{mS}, \qquad Y_1 = 7\,\text{mS} - \frac{25}{6 + 4}\,\text{mS} = 4{,}5\,\text{mS}.$$

Die Probe: Bei offenem Ausgang liegen $G_1$ und die Reihe aus $200\,\Omega$ und $1\,\text{k}\Omega$ parallel, $2\,\text{mS}$ und $0{,}83\,\text{mS}$; mit Last ist
die Reihe aus $G_2$ und $G_3 + G_L$ zwei Leitwerte von je $5\,\text{mS}$ hintereinander, $2{,}5\,\text{mS}$, plus $G_1$.

**Im Bild:** Zwei Querrohre und ein Längsrohr: Bei drucklos offenem rechtem Auslauf fließt das Wasser links durch das erste Querrohr und durch das
Längsrohr ab.
::::

## Widerstands- und Leitwertform ineinander umrechnen

Beide Formen beschreiben dasselbe Zweitor. Die eine löst die Gleichungen nach den Spannungen auf, die andere nach den Strömen; ihre Matrizen sind deshalb
zueinander invers:

:::formel
$$\mathbf Y = \mathbf Z^{-1} = \frac{1}{\det\mathbf Z}\begin{pmatrix} Z_{22} & -Z_{12} \\ -Z_{21} & Z_{11} \end{pmatrix}, \qquad \det\mathbf Z = Z_{11}Z_{22} - Z_{12}Z_{21},$$

$$\mathbf Z = \mathbf Y^{-1} = \frac{1}{\det\mathbf Y}\begin{pmatrix} Y_{22} & -Y_{12} \\ -Y_{21} & Y_{11} \end{pmatrix}, \qquad \det\mathbf Y = Y_{11}Y_{22} - Y_{12}Y_{21}.$$
:::

**So liest man das:** Invers heißt nicht elementweise: $Y_{11}$ ist im Allgemeinen nicht $1/Z_{11}$, denn das eine ist ein Kurzschluss-, das andere ein
Leerlaufwert. Ein Netz aus Widerständen in
T-Form hat eine einfache Widerstandsmatrix, eines in π-Form eine einfache Leitwertmatrix, und beide Schaltungen gehen durch die Stern-Dreieck-Umwandlung
ineinander über. So kann man jedes umkehrbare Zweitor als T oder als π aus drei Widerständen darstellen, wobei die Werte bei manchen Netzen,
etwa Brücken, auch negativ ausfallen.

**Im Bild:** Ob man nach dem Druck bei vorgegebenem Durchfluss oder nach dem Durchfluss bei vorgegebenem Druck fragt: Es ist derselbe Kasten, nur die Frage
umgedreht.

:::herleitung
**Auflösen.** Aus der Widerstandsform folgt durch Multiplikation mit der inversen Matrix die Leitwertform; die inverse einer $2\times2$-Matrix erhält man,
indem man die Diagonale tauscht, die Nebendiagonale umpolt und durch die Determinante teilt. Die Probe ist das Produkt:

$$\frac{1}{\det\mathbf Z}\begin{pmatrix} Z_{22} & -Z_{12} \\ -Z_{21} & Z_{11} \end{pmatrix}\begin{pmatrix} Z_{11} & Z_{12} \\ Z_{21} & Z_{22} \end{pmatrix} = \frac{1}{\det\mathbf Z}\begin{pmatrix} Z_{11}Z_{22} - Z_{12}Z_{21} & 0 \\ 0 & Z_{11}Z_{22} - Z_{12}Z_{21} \end{pmatrix}.$$

**Im Ersatzschaltbild.** Dasselbe ergibt sich über Kurzschlussversuche am Ersatzschaltbild der Widerstandsform. Mit kurzgeschlossenem Ausgang ist
$Z_{21}I_1$ gleich $-Z_{22}I_2$, und

$$I_2 = -\frac{Z_{21}}{Z_{22}}\,I_1, \qquad U_1 = \Big(Z_{11} - \frac{Z_{12}Z_{21}}{Z_{22}}\Big)I_1, \qquad Y_{11} = \frac{I_1}{U_1} = \frac{Z_{22}}{\det\mathbf Z}.$$

Die übrigen drei folgen ebenso, die beiden in der zweiten Zeile mit kurzgeschlossenem Eingang.

**Die π-Deutung.** Die Leitwertmatrix einer π-Schaltung hat, wie im Beispiel oben, $G_1 + G_2$, $-G_2$ und $G_2 + G_3$. Ist $Y_{12}$ gleich $Y_{21}$, lassen sich
die drei Leitwerte aus jeder Leitwertmatrix ablesen:

$$G_2 = -Y_{12}, \qquad G_1 = Y_{11} + Y_{12}, \qquad G_3 = Y_{22} + Y_{12}.$$
:::

::::beispiel Von der T- zur π-Schaltung
Die T-Schaltung mit $100\,\Omega$, $300\,\Omega$ und $200\,\Omega$ hat die Widerstandsmatrix von oben:

$$\mathbf Z = \begin{pmatrix} 400 & 300 \\ 300 & 500 \end{pmatrix}\Omega, \qquad \det\mathbf Z = 400\cdot500 - 300^2 = 110\,000\,\Omega^2.$$

**Die Leitwertmatrix:**

$$\mathbf Y = \frac{1}{110\,000\,\Omega^2}\begin{pmatrix} 500 & -300 \\ -300 & 400 \end{pmatrix}\Omega \approx \begin{pmatrix} 4{,}545 & -2{,}727 \\ -2{,}727 & 3{,}636 \end{pmatrix}\text{mS}.$$

$Y_{11}$ ist $4{,}545\,\text{mS}$, während $1/Z_{11}$ nur $2{,}5\,\text{mS}$ ergäbe: Kurzschluss- und Leerlaufwert sind verschieden.

**Die gleichwertige π-Schaltung:**

$$G_2 \approx 2{,}727\,\text{mS} \to 366{,}7\,\Omega, \qquad G_1 \approx 1{,}818\,\text{mS} \to 550\,\Omega, \qquad G_3 \approx 0{,}909\,\text{mS} \to 1100\,\Omega.$$

Das sind genau die Werte der Stern-Dreieck-Umwandlung: $100 + 200 + \frac{100\cdot200}{300}$, $100 + 300 + \frac{100\cdot300}{200}$ und
$200 + 300 + \frac{200\cdot300}{100}$ Ohm.

**Im Bild:** Ein Kasten mit Rohren in T-Form und einer mit Rohren in π-Form, von außen nicht zu unterscheiden.
::::

## Hybridform

Gibt man den Eingangsstrom und die Ausgangsspannung vor, entsteht die __Hybridform__, die Leerlauf und Kurzschluss mischt:

:::formel Definition
$$U_1 = H_{11}\,I_1 + H_{12}\,U_2, \qquad I_2 = H_{21}\,I_1 + H_{22}\,U_2, \qquad \begin{pmatrix} U_1 \\ I_2 \end{pmatrix} = \mathbf H \begin{pmatrix} I_1 \\ U_2 \end{pmatrix}.$$
:::

**So liest man das:** Die Parameter sind von gemischter Art, daher der Name: $H_{11}$ ist ein Widerstand, $H_{22}$ ein Leitwert, $H_{12}$ und $H_{21}$ sind
Zahlen ohne Einheit. Man bestimmt sie mit kurzgeschlossenem Ausgang und mit offenem Eingang:

$$H_{11} = \frac{U_1}{I_1}\Big|_{U_2 = 0}, \qquad H_{21} = \frac{I_2}{I_1}\Big|_{U_2 = 0}, \qquad H_{12} = \frac{U_1}{U_2}\Big|_{I_1 = 0}, \qquad H_{22} = \frac{I_2}{U_2}\Big|_{I_1 = 0}.$$

$H_{11}$ ist der __Kurzschlusseingangswiderstand__, $H_{21}$ die __Kurzschlussstromübersetzung__ oder __Stromverstärkung__, $H_{12}$ die __Spannungsrückwirkung__
bei offenem Eingang und $H_{22}$ der __Leerlaufausgangsleitwert__. Im Ersatzschaltbild liegt am Eingang $H_{11}$ in Reihe mit einer
__spannungsgesteuerten Spannungsquelle__ (VCVS) $H_{12} U_2$, am Ausgang $H_{22}$ parallel zu einer __stromgesteuerten Stromquelle__ (CCCS) $H_{21} I_1$. Das ist
das klassische Modell des Transistors für kleine Änderungen um einen Arbeitspunkt.

**Im Bild:** Links eine feste Wassermenge hineinpumpen, rechts den Druck vorgeben: Links stellt sich ein Druck ein, rechts ein Durchfluss.

:::herleitung
**Kurzschluss am Ausgang.** Mit $U_2$ gleich null bleibt $U_1$ gleich $H_{11}I_1$ und $I_2$ gleich $H_{21}I_1$; geteilt durch $I_1$ folgen die ersten beiden.

**Leerlauf am Eingang.** Mit $I_1$ gleich null bleibt $U_1$ gleich $H_{12}U_2$ und $I_2$ gleich $H_{22}U_2$; geteilt durch $U_2$ die anderen beiden.

**Einheiten.** In der ersten Gleichung werden ein Strom und eine Spannung zu einer Spannung: $H_{11}$ in Ohm, $H_{12}$ ohne Einheit; in der zweiten werden sie zu
einem Strom: $H_{21}$ ohne Einheit, $H_{22}$ in Siemens.
:::

::::beispiel Ein Transistor in Hybridform
Ein Bipolartransistor in Emitterschaltung verhält sich für kleine Änderungen um seinen Arbeitspunkt wie ein Zweitor mit den typischen Werten

$$H_{11} = 2{,}5\,\text{k}\Omega, \qquad H_{12} \approx 0, \qquad H_{21} = 200, \qquad H_{22} = 20\,\mu\text{S}.$$

Am Ausgang hängt ein Lastwiderstand von $5\,\text{k}\Omega$; dort ist $U_2$ gleich $-R_L I_2$.

**Stromverstärkung.** Aus der zweiten Gleichung, nach $I_2$ aufgelöst:

$$I_2 = \frac{H_{21}}{1 + H_{22}R_L}\,I_1 = \frac{200}{1 + 0{,}1}\,I_1 \approx 181{,}8\,I_1.$$

**Spannungsverstärkung und Leistung.** Mit $H_{12}$ gleich null ist der Eingangswiderstand $H_{11}$; die Spannung kehrt das Vorzeichen um, und die Leistung
am Ausgang ist mehr als sechzigtausendmal so groß wie die am Eingang:

$$\frac{U_2}{U_1} = \frac{-R_L\,I_2}{H_{11}\,I_1} \approx -363{,}6, \qquad \frac{R_L\,I_2^2}{H_{11}\,I_1^2} \approx 6{,}6\cdot10^4.$$

Die zusätzliche Leistung stammt aus der Versorgungsspannung des Transistors, nicht aus dem Eingangssignal.

**Im Bild:** Ein Kasten mit einer eigenen, von außen angetriebenen Pumpe, die rechts ein Vielfaches dessen liefert, was links hineingeht.
::::

## Kettenform

Fragt man, was man am Eingang liefern muss, damit am Ausgang eine bestimmte Spannung und ein bestimmter Strom herauskommen, drückt man die Eingangsgrößen
durch die Ausgangsgrößen aus, die __Kettenform__:

:::formel Definition
$$U_1 = A_{11}\,U_2 + A_{12}\,(-I_2), \qquad I_1 = A_{21}\,U_2 + A_{22}\,(-I_2), \qquad \begin{pmatrix} U_1 \\ I_1 \end{pmatrix} = \mathbf A \begin{pmatrix} U_2 \\ -I_2 \end{pmatrix}.$$
:::

**So liest man das:** Statt $I_2$ steht $-I_2$, der Strom, der aus dem Ausgangstor hinaus zum nächsten Glied fließt. Die Parameter misst man mit offenem und
mit kurzgeschlossenem Ausgang:

$$A_{11} = \frac{U_1}{U_2}\Big|_{I_2 = 0}, \qquad A_{21} = \frac{I_1}{U_2}\Big|_{I_2 = 0}, \qquad A_{12} = -\frac{U_1}{I_2}\Big|_{U_2 = 0}, \qquad A_{22} = -\frac{I_1}{I_2}\Big|_{U_2 = 0}.$$

$A_{11}$ ist die __reziproke Leerlaufspannungsübersetzung__, wie viel Spannung man vorne für ein Volt hinten braucht; $A_{21}$ der
Leerlaufübertragungsleitwert, $A_{12}$ der __Kurzschlussübertragungswiderstand__ und $A_{22}$ die reziproke Kurzschlussstromübersetzung. Ihren Namen hat die
Form von der __Kettenschaltung__: Hängen Zweitore hintereinander, ist der Ausgang des einen der Eingang des nächsten, und die Kettenmatrizen multiplizieren
sich:

:::formel Satz
$$\mathbf A = \mathbf A'\,\mathbf A''.$$
:::

**Im Bild:** Von hinten nach vorne fragen: Was muss der letzte Kasten bekommen, damit hinten das Gewünschte herauskommt, was der vorletzte, damit der
letzte das bekommt — und so weiter bis zur Pumpe.

:::herleitung
**Die Parameter.** Mit $I_2$ gleich null bleiben $U_1$ gleich $A_{11}U_2$ und $I_1$ gleich $A_{21}U_2$; mit $U_2$ gleich null bleiben $U_1$ gleich $A_{12}(-I_2)$ und
$I_1$ gleich $A_{22}(-I_2)$, geteilt durch $-I_2$ mit dem Minuszeichen der Formeln.

**Die Kette.** Das erste Glied hat die Matrix $\mathbf A'$, das zweite $\mathbf A''$. Ausgangsspannung des ersten und Eingangsspannung des zweiten sind
gleich, und der Strom, der das erste hinaus verlässt, fließt in das zweite hinein:

$$\begin{pmatrix} U_1 \\ I_1 \end{pmatrix} = \mathbf A' \begin{pmatrix} U'_2 \\ -I'_2 \end{pmatrix}, \qquad \begin{pmatrix} U'_2 \\ -I'_2 \end{pmatrix} = \begin{pmatrix} U''_1 \\ I''_1 \end{pmatrix} = \mathbf A'' \begin{pmatrix} U''_2 \\ -I''_2 \end{pmatrix}.$$

Eingesetzt steht das Produkt der beiden Matrizen vor den Ausgangsgrößen des zweiten Gliedes. Genau dafür ist das Vorzeichen von $I_2$ umgedreht: Ohne es
stünde zwischen den Gliedern ein Minus. Die Reihenfolge der Faktoren ist die der Glieder, denn beim Matrizenprodukt kommt es auf die Reihenfolge an.
:::

::::beispiel Das Dämpfungsglied in Kettenform, einzeln und doppelt
Das π-Dämpfungsglied für $50\,\Omega$ aus dem Artikel über die Stern-Dreieck-Transformation hat zwei Querwiderstände und einen Längswiderstand:

$$R_\text{quer} = 150\,\Omega, \qquad R_\text{längs} = 37{,}5\,\Omega.$$

**Die Kettenmatrix.** Bei offenem Ausgang teilen Längs- und hinterer Querwiderstand die Spannung, bei kurzgeschlossenem fließt der Ausgangsstrom nur durch
den Längswiderstand:

$$A_{11} = A_{22} = 1 + \frac{37{,}5}{150} = 1{,}25, \qquad A_{12} = 37{,}5\,\Omega, \qquad A_{21} = \frac{2}{150\,\Omega} + \frac{37{,}5\,\Omega}{(150\,\Omega)^2} = 0{,}015\,\text{S}.$$

:::herleitung
**Die Kettenmatrix einer π-Schaltung.** Mit den Leitwerten $G_1$ und $G_3$ quer und $G_2$ längs. Bei offenem
Ausgang teilen $G_2$ und $G_3$ die Eingangsspannung, und der Eingangsstrom fließt durch $G_1$ und durch die Reihe aus $G_2$ und $G_3$:

$$U_2 = U_1\,\frac{G_2}{G_2 + G_3}, \qquad I_1 = U_1\Big(G_1 + \frac{G_2G_3}{G_2 + G_3}\Big), \qquad A_{11} = 1 + \frac{G_3}{G_2}, \qquad A_{21} = G_1 + G_3 + \frac{G_1G_3}{G_2}.$$

Bei kurzgeschlossenem Ausgang fließt durch $G_2$ der Strom $U_1G_2$ hinaus, und in den Eingang fließen die Ströme durch $G_1$ und $G_2$:

$$-I_2 = U_1\,G_2, \qquad I_1 = U_1\,(G_1 + G_2), \qquad A_{12} = \frac{1}{G_2}, \qquad A_{22} = 1 + \frac{G_1}{G_2}.$$
:::

**Mit 50 Ohm Last** ist $-I_2$ gleich $U_2/(50\,\Omega)$:

$$U_1 = \Big(1{,}25 + \frac{37{,}5}{50}\Big)U_2 = 2\,U_2, \qquad I_1 = \Big(0{,}015\,\text{S} + \frac{1{,}25}{50\,\Omega}\Big)U_2 = 0{,}04\,\text{S}\cdot U_2, \qquad \frac{U_1}{I_1} = 50\,\Omega.$$

Das Glied halbiert die Spannung und zeigt am Eingang $50\,\Omega$, wie im Artikel über die Stern-Dreieck-Transformation.

**Zwei Glieder in Kette:**

$$\mathbf A^2 = \begin{pmatrix} 1{,}25 & 37{,}5\,\Omega \\ 0{,}015\,\text{S} & 1{,}25 \end{pmatrix}^2 = \begin{pmatrix} 2{,}125 & 93{,}75\,\Omega \\ 0{,}0375\,\text{S} & 2{,}125 \end{pmatrix}.$$

Mit derselben Last ergibt das ein Viertel der Spannung und wieder $50\,\Omega$ am Eingang:

$$U_1 = \Big(2{,}125 + \frac{93{,}75}{50}\Big)U_2 = 4\,U_2, \qquad I_1 = \Big(0{,}0375\,\text{S} + \frac{2{,}125}{50\,\Omega}\Big)U_2 = 0{,}08\,\text{S}\cdot U_2.$$

**Im Bild:** Zwei gleiche Kästen hintereinander, jeder halbiert den Druck; zusammen bleibt ein Viertel, und jeder Kasten sieht hinter sich, was er braucht.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/06-kettenschaltung · Vorlage: zweitor-kette
Zwei π-Dämpfungsglieder hintereinander zwischen einer Quelle mit $50\,\Omega$ Innenwiderstand und einer Last von $50\,\Omega$, jedes mit $150\,\Omega$ quer,
$37{,}5\,\Omega$ längs und $150\,\Omega$ quer. Über jedem Glied steht seine Kettenmatrix, über beiden zusammen das Produkt. Pfeile zeigen den Strom, der das erste
Glied als $-I'_2$ verlässt und als $I''_1$ in das zweite fließt. Ein Schalter fügt ein drittes Glied hinzu; Anzeigen zeigen die Spannung an jeder
Verbindungsstelle, halbiert von Glied zu Glied, und den Eingangswiderstand, der bei $50\,\Omega$ bleibt. Kernaussage: In der Kettenschaltung multiplizieren
sich die Kettenmatrizen. (Rot = Glieder, blau = Spannungen, orange = Matrizen und Ströme zwischen den Gliedern, grau = Quelle und Last.)
:::

## Alle Formen ineinander umrechnen

Jede Form lässt sich in jede andere umrechnen, indem man die beiden Gleichungen nach dem anderen Paar von Größen auflöst. Zusammengefasst
steht hier zeilenweise jede Matrix in den Parametern der drei anderen:

:::formel
$$\mathbf Z = \begin{pmatrix} \frac{Y_{22}}{\det\mathbf Y} & \frac{-Y_{12}}{\det\mathbf Y} \\ \frac{-Y_{21}}{\det\mathbf Y} & \frac{Y_{11}}{\det\mathbf Y} \end{pmatrix} \qquad = \begin{pmatrix} \frac{\det\mathbf H}{H_{22}} & \frac{H_{12}}{H_{22}} \\ \frac{-H_{21}}{H_{22}} & \frac{1}{H_{22}} \end{pmatrix} \qquad = \begin{pmatrix} \frac{A_{11}}{A_{21}} & \frac{\det\mathbf A}{A_{21}} \\ \frac{1}{A_{21}} & \frac{A_{22}}{A_{21}} \end{pmatrix},$$

$$\mathbf Y = \begin{pmatrix} \frac{Z_{22}}{\det\mathbf Z} & \frac{-Z_{12}}{\det\mathbf Z} \\ \frac{-Z_{21}}{\det\mathbf Z} & \frac{Z_{11}}{\det\mathbf Z} \end{pmatrix} \qquad = \begin{pmatrix} \frac{1}{H_{11}} & \frac{-H_{12}}{H_{11}} \\ \frac{H_{21}}{H_{11}} & \frac{\det\mathbf H}{H_{11}} \end{pmatrix} \qquad = \begin{pmatrix} \frac{A_{22}}{A_{12}} & \frac{-\det\mathbf A}{A_{12}} \\ \frac{-1}{A_{12}} & \frac{A_{11}}{A_{12}} \end{pmatrix},$$

$$\mathbf H = \begin{pmatrix} \frac{\det\mathbf Z}{Z_{22}} & \frac{Z_{12}}{Z_{22}} \\ \frac{-Z_{21}}{Z_{22}} & \frac{1}{Z_{22}} \end{pmatrix} \qquad = \begin{pmatrix} \frac{1}{Y_{11}} & \frac{-Y_{12}}{Y_{11}} \\ \frac{Y_{21}}{Y_{11}} & \frac{\det\mathbf Y}{Y_{11}} \end{pmatrix} \qquad = \begin{pmatrix} \frac{A_{12}}{A_{22}} & \frac{\det\mathbf A}{A_{22}} \\ \frac{-1}{A_{22}} & \frac{A_{21}}{A_{22}} \end{pmatrix},$$

$$\mathbf A = \begin{pmatrix} \frac{Z_{11}}{Z_{21}} & \frac{\det\mathbf Z}{Z_{21}} \\ \frac{1}{Z_{21}} & \frac{Z_{22}}{Z_{21}} \end{pmatrix} \qquad = \begin{pmatrix} \frac{-Y_{22}}{Y_{21}} & \frac{-1}{Y_{21}} \\ \frac{-\det\mathbf Y}{Y_{21}} & \frac{-Y_{11}}{Y_{21}} \end{pmatrix} \qquad = \begin{pmatrix} \frac{-\det\mathbf H}{H_{21}} & \frac{-H_{11}}{H_{21}} \\ \frac{-H_{22}}{H_{21}} & \frac{-1}{H_{21}} \end{pmatrix}.$$
:::

**So liest man das:** In jeder Zeile steht dieselbe Matrix, einmal durch jede der anderen ausgedrückt.
Wird ein Nenner null, gibt es die Form nicht. Bei einer abgeglichenen Brücke etwa ist $Z_{21}$ null, und eine Kettenmatrix existiert nicht: Man kann vorne
nichts einspeisen, um hinten eine Spannung zu bekommen.

**Im Bild:** Vier Arten, denselben Kasten zu befragen; wer die Antworten auf eine Art kennt, kann die auf jede andere ausrechnen.

:::herleitung
**Die Hybridform aus der Widerstandsform.** Die zweite Gleichung der Widerstandsform nach $I_2$ aufgelöst, dann in die erste eingesetzt:

$$I_2 = -\frac{Z_{21}}{Z_{22}}\,I_1 + \frac{1}{Z_{22}}\,U_2, \qquad U_1 = \Big(Z_{11} - \frac{Z_{12}Z_{21}}{Z_{22}}\Big)I_1 + \frac{Z_{12}}{Z_{22}}\,U_2 = \frac{\det\mathbf Z}{Z_{22}}\,I_1 + \frac{Z_{12}}{Z_{22}}\,U_2.$$

Die Faktoren sind die vier Einträge der dritten Zeile, erste Spalte.

**Die Kettenform aus der Widerstandsform.** Die zweite Gleichung nach $I_1$ aufgelöst und in die erste eingesetzt, jeweils mit $-I_2$ geschrieben:

$$I_1 = \frac{1}{Z_{21}}\,U_2 + \frac{Z_{22}}{Z_{21}}\,(-I_2), \qquad U_1 = \frac{Z_{11}}{Z_{21}}\,U_2 + \frac{Z_{11}Z_{22} - Z_{12}Z_{21}}{Z_{21}}\,(-I_2).$$

Alle übrigen Einträge entstehen ebenso, durch Auflösen nach den jeweils vorgegebenen Größen; eine Probe an einem beliebigen Zahlenbeispiel bestätigt die
ganze Tabelle.

**Eine Determinante.** Aus der letzten Zeile, erste Spalte, folgt ein Zusammenhang, den der nächste Abschnitt braucht:

$$\det\mathbf A = \frac{Z_{11}Z_{22} - \det\mathbf Z}{Z_{21}^2} = \frac{Z_{12}}{Z_{21}}.$$
:::

::::beispiel Die T-Schaltung in allen Formen
Die T-Schaltung mit $100\,\Omega$, $300\,\Omega$ und $200\,\Omega$:

$$\mathbf Z = \begin{pmatrix} 400 & 300 \\ 300 & 500 \end{pmatrix}\Omega, \qquad \det\mathbf Z = 110\,000\,\Omega^2.$$

**Hybrid- und Kettenform** nach der Tabelle:

$$\mathbf H = \begin{pmatrix} 220\,\Omega & 0{,}6 \\ -0{,}6 & 2\,\text{mS} \end{pmatrix}, \qquad \mathbf A = \frac{1}{300\,\Omega}\begin{pmatrix} 400\,\Omega & 110\,000\,\Omega^2 \\ 1 & 500\,\Omega \end{pmatrix} \approx \begin{pmatrix} 1{,}333 & 366{,}7\,\Omega \\ 3{,}333\,\text{mS} & 1{,}667 \end{pmatrix}.$$

$H_{11}$ ist der Kurzschlusseingangswiderstand $220\,\Omega$ von oben, und die Determinante der Kettenmatrix ist eins.

**Dieselbe Last, anders gerechnet.** Mit $100\,\Omega$ am Ausgang ergibt die Kettenform dieselbe Spannungsübersetzung wie die Widerstandsform:

$$\frac{U_1}{U_2} = A_{11} + \frac{A_{12}}{R_L} = 1{,}333 + \frac{366{,}7\,\Omega}{100\,\Omega} = 5, \qquad \frac{U_2}{U_1} = 0{,}2.$$

**Im Bild:** Derselbe Kasten, viermal befragt, und jede Antwort führt bei demselben Verbraucher auf dasselbe Ergebnis.
::::

## Zweitoreigenschaften

Drei Eigenschaften sortieren die Zweitore. Ein Zweitor heißt __umkehrbar__, __übertragungssymmetrisch__ oder __reziprok__, wenn
dieselbe Ursache an der einen Seite dieselbe Wirkung an der anderen hat wie umgekehrt: Ein Strom, der in Tor 1 eingespeist wird, erzeugt am offenen Tor 2
dieselbe Spannung wie derselbe Strom in Tor 2 am offenen Tor 1. In jeder Form lässt sich das ablesen:

:::formel Satz
$$Y_{12} = Y_{21}, \qquad Z_{12} = Z_{21}, \qquad H_{12} = -H_{21}, \qquad \det\mathbf A = 1.$$
:::

**So liest man das:** Die vier Bedingungen sind gleichwertig; jede zieht die anderen nach sich. Ein umkehrbares Zweitor hat nur drei unabhängige Parameter und lässt sich durch eine T- oder π-Schaltung ohne Quellen nachbilden.
Jedes Netz aus Widerständen ist umkehrbar, und später auch jedes aus Spulen und Kondensatoren; nicht umkehrbar sind Zweitore mit gesteuerten Quellen wie
Verstärker. Umkehrbar ist dabei schwächer als __symmetrisch__: Ein symmetrisches Zweitor hat zusätzlich gleiche Ein- und Ausgangswiderstände, man darf seine
Tore vertauschen. Und nicht umkehrbar heißt nicht automatisch aktiv.

Ein nicht umkehrbares Zweitor wird im Grenzfall ohne jede Rückwirkung __rückwirkungsfrei__, mit vier wieder gleichwertigen Bedingungen:

$$Y_{12} = 0, \qquad Z_{12} = 0, \qquad H_{12} = 0, \qquad \det\mathbf A = 0.$$

Dann hängt das Verhalten des Eingangs nicht von dem ab, was am Ausgang geschieht. Ein rückwirkungsfreies Zweitor hat drei Parameter, einen Eingangs- und
einen Ausgangswiderstand und eine Steuergröße; das ist die Grundform eines Verstärkers.

Schließlich nimmt ein Zweitor im symmetrischen Pfeilsystem insgesamt die Leistung

$$P = U_1I_1 + U_2I_2 = Y_{11}\,U_1^2 + (Y_{12} + Y_{21})\,U_1U_2 + Y_{22}\,U_2^2$$

auf. Es ist __passiv__, wenn diese Leistung bei keiner Beschaltung negativ wird, und __aktiv__, wenn sie negativ werden kann, das Zweitor also am Ausgang
mehr abgibt, als es am Eingang aufnimmt. Achtung, Vorzeichen: Weil die abgegebene Leistung als $-U_2I_2$ zählt, nimmt das Zweitor insgesamt
$U_1I_1 + U_2I_2$ auf, nicht $U_1I_1 - U_2I_2$.

**Im Bild:** Ein Kasten nur aus Rohren antwortet in beide Richtungen gleich und kann nie mehr Leistung abgeben, als er bekommt; einer mit eigener,
angetriebener Pumpe kann beides brechen.

:::herleitung
**Die vier Bedingungen sind gleichwertig.** Aus der Umrechnungstabelle:

$$Y_{12} = \frac{-Z_{12}}{\det\mathbf Z}, \quad Y_{21} = \frac{-Z_{21}}{\det\mathbf Z}, \qquad H_{12} = \frac{Z_{12}}{Z_{22}}, \quad H_{21} = \frac{-Z_{21}}{Z_{22}}, \qquad \det\mathbf A = \frac{Z_{12}}{Z_{21}}.$$

Gleiche $Y$-Nebendiagonale, entgegengesetzte $H$-Nebendiagonale und $\det\mathbf A$ gleich eins sagen also alle dasselbe wie $Z_{12}$ gleich $Z_{21}$; und
alle drei Nebendiagonalen verschwinden mit $Z_{12}$, ebenso $\det\mathbf A$.

**Widerstandsnetze sind umkehrbar.** In der Knotenanalyse trägt ein Widerstand zwischen den Knoten $j$ und $k$ seinen Leitwert mit Minus an beiden Stellen
$(j,k)$ und $(k,j)$ der Leitwertmatrix ein, sie ist also symmetrisch. Eliminiert man die inneren Knoten, entstehen nach der Stern-Vieleck-Regel aus dem
Artikel über die Stern-Dreieck-Transformation Leitwerte der Form $G_{j0}G_{k0}/G_\Sigma$, wieder symmetrisch in $j$ und $k$. Was für die beiden Tore übrig
bleibt, ist eine symmetrische Leitwertmatrix.

**Die Leistung.** Die Leitwertgleichungen in $U_1I_1 + U_2I_2$ eingesetzt ergibt die quadratische Form. Bei einem Netz aus Widerständen ist diese Leistung
nach dem Satz von Tellegen aus dem Artikel über die Kirchhoffschen Gesetze die Summe der $R_kI_k^2$ aller Widerstände, also nie negativ: Solche Netze
sind passiv.
:::

::::beispiel Drei Zweitore auf dem Prüfstand
**(a) Die T-Schaltung** mit $\mathbf Z$ von oben ist umkehrbar, denn $Z_{12}$ und $Z_{21}$ sind beide $300\,\Omega$. Ihre Leistung, in Strömen geschrieben, ist
nie negativ, denn der Ausdruck hat keine reelle Nullstelle außer bei verschwindenden Strömen:

$$P = 400\,\Omega\cdot I_1^2 + 600\,\Omega\cdot I_1I_2 + 500\,\Omega\cdot I_2^2, \qquad 600^2 - 4\cdot400\cdot500 = -440\,000 < 0.$$

Mit kurzgeschlossenem Ausgang, $I_2$ gleich $-0{,}6\,I_1$, bleibt $220\,\Omega\cdot I_1^2$, die Leistung im Kurzschlusseingangswiderstand.

**(b) Das Dämpfungsglied** ist umkehrbar:

$$\det\mathbf A = 1{,}25^2 - 37{,}5\,\Omega\cdot0{,}015\,\text{S} = 1{,}5625 - 0{,}5625 = 1.$$

**(c) Der Transistor** mit $H_{12}$ gleich null und $H_{21}$ gleich $200$ ist nicht umkehrbar, aber rückwirkungsfrei. Mit $1\,\mu\text{A}$ am Eingang und
$5\,\text{k}\Omega$ Last nimmt er $2{,}5\,\text{nW}$ auf und gibt $0{,}165\,\text{mW}$ ab; seine Gesamtleistung ist negativ, er ist aktiv:

$$P_1 = 2{,}5\,\text{k}\Omega\cdot(1\,\mu\text{A})^2 = 2{,}5\,\text{nW}, \qquad -U_2I_2 = 5\,\text{k}\Omega\cdot(181{,}8\,\mu\text{A})^2 \approx 0{,}165\,\text{mW}.$$

**Im Bild:** Zwei Kästen nur aus Rohren und einer mit eigener Pumpe; nur dieser liefert rechts mehr, als links hineingeht.
::::

## Bedeutung und Ausblick

Zweitore sind die Bausteine der Nachrichten- und Elektronikschaltungen: Filter, Leitungen, Dämpfungsglieder, Übertrager und Verstärker. Ein
Transformator überträgt nur Wechselgrößen und wird deshalb erst in der Wechselstromtechnik zum Zweitor; ein Transistor ist für Gleichgrößen ein
nichtlineares Bauteil mit Kennlinien und für kleine Signale um einen Arbeitspunkt ein lineares Zweitor in Hybridform.

Für die vier Arten, Zweitore zu verbinden, gibt es je eine passende Form. In der __Kettenschaltung__ multiplizieren sich die Kettenmatrizen. In der
__Reihenschaltung__, beide Eingänge und beide Ausgänge in Reihe, addieren sich die Widerstandsmatrizen, in der __Parallelschaltung__ die Leitwertmatrizen,
und in der __Reihen-Parallel-Schaltung__, Eingänge in Reihe und Ausgänge parallel, die Hybridmatrizen, die man deshalb auch Reihen-Parallel-Matrizen
nennt. Das gilt, solange die Torbedingungen erhalten bleiben; dass sie verletzt werden können, hat das Beispiel mit der Masseverbindung gezeigt.

Bei Wechselstrom werden die Parameter komplexe Zahlen, die Formen bleiben dieselben. Der nächste Artikel kehrt zu Netzen mit mehreren Quellen zurück: Das
__Superpositionsverfahren__ zerlegt ihre Wirkung in die Beiträge der einzelnen Quellen.

:::herleitung
**Reihe, Parallele, Reihe-Parallele.** In der Reihenschaltung fließen durch beide Zweitore an jedem Tor dieselben Ströme, und ihre Spannungen addieren
sich; mit der Widerstandsform jedes Zweitors folgt:

$$\begin{pmatrix} U_1 \\ U_2 \end{pmatrix} = \mathbf Z'\begin{pmatrix} I_1 \\ I_2 \end{pmatrix} + \mathbf Z''\begin{pmatrix} I_1 \\ I_2 \end{pmatrix} = (\mathbf Z' + \mathbf Z'')\begin{pmatrix} I_1 \\ I_2 \end{pmatrix}.$$

In der Parallelschaltung liegen an jedem Tor dieselben Spannungen, und die Ströme addieren sich, also die Leitwertmatrizen. In der Reihen-Parallel-Schaltung
sind $I_1$ und $U_2$ beiden gemeinsam, $U_1$ und $I_2$ addieren sich, also die Hybridmatrizen. Vorausgesetzt ist jedes Mal, dass in jedem Zweitor die
Torbedingungen gelten.
:::

:::kern
- Ein __Zweitor__ ist ein Vierpol, dessen Klemmen zwei Tore bilden: Was in ein Tor hineinfließt, fließt am selben Tor wieder heraus.
- Vier Torgrößen, zwei lineare Gleichungen; je nachdem, welche zwei man vorgibt, ergibt sich die Z-, Y-, H- oder A-Form.
- Z-Parameter misst man im Leerlauf, Y-Parameter im Kurzschluss, H-Parameter gemischt, A-Parameter mit offenem und kurzgeschlossenem Ausgang.
- Eingangswiderstand unter Last: $Z_1=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+R_L}$; ohne Rückwirkung bleibt er $Z_{11}$.
- Leitwert- und Widerstandsmatrix sind zueinander invers, $\mathbf Y=\mathbf Z^{-1}$; alle Formen lassen sich ineinander umrechnen.
- In der Kettenschaltung multiplizieren sich die Kettenmatrizen: $\mathbf A=\mathbf A'\mathbf A''$.
- Umkehrbar heißt $Z_{12}=Z_{21}$, wie bei jedem Widerstandsnetz; rückwirkungsfrei heißt $Z_{12}=0$.
- Aktiv ist ein Zweitor, wenn $U_1I_1+U_2I_2$ negativ werden kann; Netze aus Widerständen sind passiv.
:::

:::quiz
F: Wann ist ein Vierpol ein Zweitor, und wie kann die Torbedingung verletzt werden?
A: Wenn an jedem Tor der Strom, der in die eine Klemme fließt, aus der anderen wieder herausfließt; das gilt von selbst, wenn an jedem Tor ein eigener Zweipol hängt. Eine äußere Verbindung zwischen den Seiten verletzt es: Beim Kasten mit je $100\,\Omega$ oben und unten an $10\,\text{V}$ und $200\,\Omega$ fließen als Zweitor $25\,\text{mA}$ durch beide Eingangsklemmen, mit einer Masseverbindung der unteren Klemmen $33{,}3\,\text{mA}$ hinein und keiner aus 1' heraus.
F: Warum genügen zwei Gleichungen, und warum gibt es vier Formen?
A: In einem linearen Netz sind alle Ströme und Spannungen Summen der vorgegebenen Größen mit festen Faktoren; gibt man zwei der vier Torgrößen vor, folgen die anderen beiden linear. Welche zwei man vorgibt, ist eine Wahl: beide Ströme (Z), beide Spannungen (Y), Eingangsstrom und Ausgangsspannung (H) oder die Ausgangsgrößen (A).
F: Wie bestimmt man die Z-Parameter, und welche hat die T-Schaltung mit $100$, $300$ und $200\,\Omega$?
A: Im Leerlaufversuch: Ein Tor bleibt offen, am anderen wird ein Strom eingeprägt; dann sind $Z_{11}$, $Z_{21}$ beziehungsweise $Z_{12}$, $Z_{22}$ Spannung durch Strom. Für die T-Schaltung sind $Z_{11}=R_1+R_2=400\,\Omega$, $Z_{12}=Z_{21}=R_2=300\,\Omega$ und $Z_{22}=R_2+R_3=500\,\Omega$.
F: Wie hängt der Eingangswiderstand eines Zweitors von der Last ab?
A: $Z_1=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+R_L}$, aus den beiden Maschen mit $U_2=-R_LI_2$; im Leerlauf $Z_{11}$, im Kurzschluss $Z_{11}-Z_{12}Z_{21}/Z_{22}$. Die T-Schaltung hat $400\,\Omega$, $220\,\Omega$ und mit $100\,\Omega$ Last $250\,\Omega$. Ohne Rückwirkung, mit $Z_{12}=0$, ist der Eingangswiderstand von der Last unabhängig.
F: Wie bestimmt man die Y-Parameter, und warum ist $Y_{11}$ nicht $1/Z_{11}$?
A: Im Kurzschlussversuch: Ein Tor wird kurzgeschlossen, am anderen eine Spannung eingeprägt; dann sind die Parameter Strom durch Spannung. $Y_{11}$ ist ein Kurzschlusswert, $Z_{11}$ ein Leerlaufwert; bei der T-Schaltung sind es $4{,}545\,\text{mS}$ gegenüber $1/(400\,\Omega)=2{,}5\,\text{mS}$. Die π-Schaltung mit $2$, $5$ und $1\,\text{mS}$ hat $\mathbf Y$ mit $7$, $-5$, $-5$ und $6\,\text{mS}$.
F: Wie rechnet man Widerstands- und Leitwertform ineinander um, und was hat das mit Stern und Dreieck zu tun?
A: Die Matrizen sind invers, $\mathbf Y=\mathbf Z^{-1}$: Diagonale tauschen, Nebendiagonale umpolen, durch $\det\mathbf Z$ teilen. Aus der Leitwertmatrix eines umkehrbaren Zweitors liest man eine π-Schaltung ab, $G_2=-Y_{12}$, $G_1=Y_{11}+Y_{12}$, $G_3=Y_{22}+Y_{12}$; für die T-Schaltung mit $100$, $300$, $200\,\Omega$ ergeben sich $550$, $366{,}7$ und $1100\,\Omega$ — genau die Stern-Dreieck-Umwandlung.
F: Was beschreibt die Hybridform, und was folgt für den Transistor mit $H_{11}=2{,}5\,\text{k}\Omega$, $H_{21}=200$, $H_{22}=20\,\mu\text{S}$ an $5\,\text{k}\Omega$?
A: Sie gibt Eingangsstrom und Ausgangsspannung vor; $H_{11}$ ist ein Widerstand, $H_{22}$ ein Leitwert, $H_{12}$ und $H_{21}$ sind ohne Einheit, $H_{21}$ ist die Stromverstärkung. Aus $I_2=\frac{H_{21}}{1+H_{22}R_L}I_1$ folgt eine Stromverstärkung von $181{,}8$, eine Spannungsverstärkung von $-363{,}6$ und eine Leistungsverstärkung von etwa $6{,}6\cdot10^4$, gespeist aus der Versorgungsspannung.
F: Warum steht in der Kettenform $-I_2$, und was ergibt das für hintereinandergeschaltete Zweitore?
A: $-I_2$ ist der Strom, der das Zweitor hinaus zum nächsten verlässt und dort als dessen Eingangsstrom hineinfließt. Damit gehen die Ausgangsgrößen des einen Glieds ohne Vorzeichenwechsel in die Eingangsgrößen des nächsten über, und die Kettenmatrizen multiplizieren sich. Das π-Dämpfungsglied mit $\det\mathbf A=1$ halbiert an $50\,\Omega$ die Spannung, zwei hintereinander vierteln sie, und beide zeigen am Eingang $50\,\Omega$.
F: Was heißt umkehrbar, rückwirkungsfrei und aktiv, und warum sind Widerstandsnetze umkehrbar und passiv?
A: Umkehrbar: $Z_{12}=Z_{21}$, gleichwertig $Y_{12}=Y_{21}$, $H_{12}=-H_{21}$, $\det\mathbf A=1$; rückwirkungsfrei: alle diese Nebengrößen null; aktiv: $U_1I_1+U_2I_2$ kann negativ werden. Ein Widerstandsnetz hat eine symmetrische Knotenleitwertmatrix, die beim Eliminieren innerer Knoten symmetrisch bleibt, und seine aufgenommene Leistung ist nach Tellegen die Summe der $R_kI_k^2$, also nie negativ.
F: Welche Verwechslungen passieren bei Zweitoren leicht?
A: Bei den gesteuerten Quellen der Widerstandsform sitzt $Z_{12}I_2$ am Eingang und $Z_{21}I_1$ am Ausgang; der erste Index nennt das Tor der Quelle. In der Hybridform steuert die Ausgangsspannung die Eingangsquelle, $H_{12}U_2$, nicht der Ausgangsstrom. Und im symmetrischen Pfeilsystem nimmt ein Zweitor die Leistung $U_1I_1+U_2I_2$ auf; ein Minus vor $U_2I_2$ wäre falsch, weil $I_2$ schon in das Zweitor hineinzählt.
:::
