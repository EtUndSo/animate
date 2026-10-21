---
title: Gleichrichtung und Ladungspumpe
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100600
summary: Von Grund auf – wie Dioden aus Wechselspannung Gleichspannung machen und wie Dioden mit Kondensatoren eine Spannung sogar vervielfachen. Leitbild ist eine Pendelpumpe, die Wasser hin und her schiebt, mit Rückschlagventilen und Gummimembranen als Speicher. Mit Mittelwert und Gleichrichtwert, der Brückenschaltung nach Graetz samt Strompfaden, Totzone und Sperrspannung, der Glättung mit dem Ladekondensator, Brummspannung und Stromflusswinkel sowie der Ladungspumpe des Skripts mit Ladungsteilung je Takt, Last und Kaskaden. Mit Beispiel-Seite.
tags: Gleichrichter, Einweggleichrichter, Brückengleichrichter, Graetz, Glättung, Brummspannung, Ladungspumpe
---

## Anschaulich

Die Steckdose liefert Wechselspannung, $230\,\text{V}$ Effektivwert bei $50\,\text{Hz}$, aber Akkus, Rechner und fast alle Elektronik brauchen Gleichspannung.
Dioden machen den Übergang, und mit Kondensatoren zusammen können sie eine Spannung sogar erhöhen. Das Skript zeigt im Abschnitt 10.6 die beiden Schaltungen,
um die es hier geht, die Brückenschaltung nach Graetz und die Ladungspumpe.

**Das Leitbild dieses Artikels:** **eine Pendelpumpe mit Rückschlagventilen und Membrankammern.** Eine Kolbenpumpe schiebt das Wasser in einem Rohrnetz
abwechselnd vor und zurück, wie die Wechselspannung die Ladungen. Rückschlagventile, wie die Dioden in den vorigen Artikeln, lassen nur eine Richtung durch,
und zwar erst ab einem kleinen Öffnungsdruck. Gummimembranen in Kammern, das Bild des Kondensators aus dem Kapitel über ihn, nehmen Wasser auf und drücken es
später wieder heraus.

Vier Folgerungen:

- **Ein Ventil lässt nur jeden zweiten Hub durch.** Mit einem einzigen Ventil vor dem Verbraucher kommt nur der Vorwärtshub an; der Rückwärtshub ist verloren.
  Das ist der Einweggleichrichter aus dem Artikel über Halbleiter und Bändermodell.
- **Vier Ventile nutzen beide Hübe.** Geschickt angeordnet, lenken vier Ventile das Wasser bei jedem Hub in derselben Richtung durch den Verbraucher. Das ist die
  Brückenschaltung. Die Hydraulik kennt dieselbe Anordnung, damit ein Filter in beiden Förderrichtungen gleich durchströmt wird.
- **Eine Kammer füllt die Pausen.** Liegt eine Membrankammer neben dem Verbraucher, wird sie bei jedem Hub gespannt und schiebt in den Pausen weiter. Der Druck
  schwankt dann nur noch wenig.
- **Eine umgesteckte Kammer pumpt höher.** Füllt man eine Kammer an der Pumpe und steckt sie dann so um, dass ihr Druck auf den der Pumpe obendrauf kommt,
  entleert sie sich in eine zweite Kammer bis zum doppelten Druck. Das ist die Ladungspumpe.

:::grafik
Szene: get1/halbleiterbauelemente/04-pendelpumpe · Vorlage: pendelpumpe-ventile
Eine Kolbenpumpe links, deren Kolben langsam hin und her läuft; ein Pfeil im Rohr zeigt die Strömung, die die Richtung wechselt. Drei Tasten bauen rechts
nacheinander auf: ein einzelnes Rückschlagventil vor einem Verbraucher (nur jeder zweite Hub kommt an), vier Ventile in Brückenform (der Pfeil durch den
Verbraucher zeigt bei beiden Hüben in dieselbe Richtung), und zusätzlich eine Gummimembran-Kammer parallel zum Verbraucher, die sich bei jedem Hub wölbt und
in den Pausen weiterschiebt. Darunter mitlaufend der Druck am Verbraucher über der Zeit: halbe Bögen, volle Bögen, eine fast glatte Linie mit kleinen Zacken.
Kernaussage: Ventile richten den Strom, Kammern glätten ihn. (Rot = Ventile, blau = Wasser und Druckverlauf, orange = Membran, grau = Rohre und Pumpe.)
:::

## Mittelwert und Gleichrichtwert

Wie viel Gleichspannung in einer gleichgerichteten Spannung steckt, misst ihr __arithmetischer Mittelwert__ über eine Periode $T$, der __Gleichanteil__. Ein
Drehspulmessgerät zeigt genau ihn an. Für eine Spannung $u(t)$ mit der Periode $T$ ist er definiert als

$$\overline{u} = \frac{1}{T}\int_0^T u(t)\,dt.$$

Eine reine Sinusspannung hat den Gleichanteil null; positive und negative Halbwelle heben sich auf. Mittelt man stattdessen ihren Betrag, erhält man den
__Gleichrichtwert__ $\overline{|u|}$. Für eine Sinusspannung mit dem Scheitelwert $\hat U$ ergibt sich, und für ihre einweg gleichgerichtete Form die Hälfte:

:::formel
$$\overline{|u|} = \frac{2}{\pi}\,\hat U, \qquad \overline{u}_\text{Einweg} = \frac{1}{\pi}\,\hat U.$$
:::

**So liest man das:** Ein Brückengleichrichter mit idealen Dioden macht aus der Wechselspannung ihren Betrag, sein Ausgang hat also den Gleichrichtwert als
Gleichanteil, knapp zwei Drittel des Scheitelwerts. Der Einweggleichrichter verliert jede zweite Halbwelle und kommt auf knapp ein Drittel. Der Effektivwert aus
dem Artikel über Energieumsetzung ist etwas anderes: Er misst die Leistung an einem Widerstand, $\hat U/\sqrt2$, rund $0{,}71\,\hat U$. Echte Dioden ziehen von
jedem Bogen ihre Durchlassspannung ab; dann rechnet man den Mittelwert numerisch.

**Im Bild:** Der mittlere Durchfluss durch den Verbraucher. Bei der Pendelpumpe allein ist er null, mit vier Ventilen zwei Drittel des Spitzendurchflusses,
mit einem Ventil ein Drittel.

:::herleitung
**Eine Halbwelle.** Der Betrag einer Sinusspannung wiederholt sich nach einer halben Periode; es genügt, über eine Halbwelle zu mitteln. Mit $x = \omega t$ läuft
eine Halbwelle von $0$ bis $\pi$:

$$\overline{|u|} = \frac{1}{\pi}\int_0^\pi \hat U\sin x\,dx = \frac{\hat U}{\pi}\,\big[-\cos x\big]_0^\pi = \frac{2}{\pi}\,\hat U.$$

**Einweg.** Über eine ganze Periode gemittelt trägt nur die positive Halbwelle bei, die negative ist null; das ergibt die Hälfte.

**Mit Durchlassspannung.** Jeder leitende Bogen ist um die Durchlassspannung niedriger und kürzer, weil er erst später beginnt; eine kurze Formel gibt es dafür
nicht, man integriert numerisch. Im Bild: Was das Ventil als Öffnungsdruck schluckt, fehlt jedem Hub.
:::

::::beispiel Gleichanteile ohne Verluste
**(a) Der Scheitelwert des Skripts.** Mit $\hat U = 10\,\text{V}$ und idealen Dioden:

$$\overline{|u|} = \frac{2}{\pi}\cdot10\,\text{V} = 6{,}37\,\text{V}, \qquad \overline{u}_\text{Einweg} = \frac{1}{\pi}\cdot10\,\text{V} = 3{,}18\,\text{V}.$$

**(b) Das Netz.** Die Steckdose hat $230\,\text{V}$ Effektivwert, also den Scheitelwert

$$\hat U = \sqrt2\cdot230\,\text{V} = 325\,\text{V}.$$

Eine Brücke direkt am Netz liefert im Mittel

$$\overline{|u|} = \frac{2}{\pi}\cdot325\,\text{V} = 207\,\text{V},$$

mit einem Ladekondensator aber fast den Scheitelwert. So beginnen viele Schaltnetzteile: Sie richten das Netz unmittelbar gleich und setzen die Spannung erst
danach herab.

**Im Bild:** Vier Ventile machen aus der Pendelbewegung einen Strom, der im Mittel zwei Drittel des Spitzendurchflusses führt.
::::

## Die Brückenschaltung nach Graetz

Die Brückenschaltung, nach dem Physiker Leo Graetz, besteht aus vier Dioden in einer Raute, wie Bild 10.25 des Skripts zeigt. Die Wechselspannung $u_e$ liegt an
zwei gegenüberliegenden Ecken, der Verbraucher an den beiden anderen. An der einen Verbraucherecke treffen sich zwei Kathoden, das ist der Pluspol des Ausgangs;
an der anderen zwei Anoden, der Minuspol.

In der positiven Halbwelle leiten $D_1$ und $D_3$: Der Strom fließt durch $D_1$ zum Pluspol, durch den Verbraucher, und über $D_3$ zurück zur Quelle, während
$D_2$ und $D_4$ sperren (Bild 10.26). In der negativen Halbwelle leiten $D_2$ und $D_4$ und führen den Strom auf dem anderen Weg, aber wieder vom Pluspol durch
den Verbraucher (Bild 10.27). In jeder Halbwelle liegen also zwei Dioden im Strompfad. Mit dem Modell der Stufe 2 aus dem vorigen Artikel, der
Durchlassspannung $U_F$ je Diode, ist die Ausgangsspannung $u_a$:

:::formel
$$u_a(t) = \begin{cases} |u_e(t)| - 2\,U_F, & |u_e(t)| > 2\,U_F, \\ 0 & \text{sonst}. \end{cases}$$
:::

**So liest man das:** Der Ausgang ist der Betrag der Eingangsspannung, verringert um zwei Durchlassspannungen. Er pulsiert mit der doppelten Netzfrequenz, am
$50$-Hz-Netz also mit $100\,\text{Hz}$. Um jeden Nulldurchgang liegt eine __Totzone__: Solange der Betrag unter $2U_F$ bleibt, im Skript $1{,}2\,\text{V}$,
leitet keine Diode, und der Ausgang ist null. Am gesunkenen Scheitelwert, im Skript $8{,}8$ statt $10\,\text{V}$, liest man ab, dass die Durchlassspannung der
Dioden um $0{,}6\,\text{V}$ liegt.

Das Skript schreibt, bei negativer oder sehr kleiner positiver Spannung leiteten $D_2$ und $D_4$. Für sehr kleine positive Spannungen stimmt das nicht: Dann
sperren alle vier, wie das Skript einen Absatz später selbst sagt. $D_2$ und $D_4$ leiten erst unter $-2U_F$.

Jede sperrende Diode muss fast den Scheitelwert aushalten, genau $\hat U_e - U_F$. Bild 10.29 nennt den Ausgang $U_R$, der Text $U_a$, und die Achsen tragen
Großbuchstaben für zeitabhängige Größen, wie schon bei Bild 10.1.

**Im Bild:** Beim Vorwärtshub öffnen zwei Ventile und lassen das Wasser von oben durch den Verbraucher, beim Rückwärtshub die beiden anderen, wieder von oben.
Jeder Weg führt durch zwei Ventile, und jedes verlangt seinen Öffnungsdruck.

:::herleitung
**Positive Halbwelle.** Man nimmt nach dem Verfahren des vorigen Artikels an, dass $D_1$ und $D_3$ leiten. Die Masche aus Quelle, $D_1$, Verbraucher und $D_3$:

$$u_e = U_F + u_a + U_F, \qquad u_a = u_e - 2\,U_F.$$

**Probe der sperrenden Dioden.** $D_2$ und $D_4$ verbinden jeweils einen Ausgangspol mit einem Eingangspol. Geht man von der Anode von $D_4$ über die leitende
$D_3$ zum Minuspol und durch den Verbraucher zum Pluspol, ihrer Kathode, ergibt sich ihre Spannung, ebenso für $D_2$:

$$U_{D4} = U_{D2} = -(u_a + U_F).$$

Sie ist negativ, beide sperren also wirklich, und ihr Betrag ist im Scheitel $\hat U_e - 2U_F + U_F$, also $\hat U_e - U_F$.

**Negative Halbwelle.** Dasselbe mit vertauschten Rollen ergibt $u_a = -u_e - 2U_F$, zusammen also der Betrag.

**Die Totzone.** Leitet kein Paar, fließt kein Strom durch den Verbraucher, und $u_a$ ist null; dann liegt die Eingangsspannung an den beiden Dioden eines
Paares in Reihe. Damit beide leiten, braucht es mehr als $2U_F$. Im Bild: Zwei Ventile hintereinander öffnen erst beim doppelten Öffnungsdruck.
:::

::::beispiel Ein Brückengleichrichter am Transformator
Ein Transformator liefert $12\,\text{V}$ Effektivwert an eine Brücke mit einem Verbraucher; Durchlassspannung, Widerstand und Scheitelwert:

$$U_F = 0{,}7\,\text{V}, \qquad R_L = 100\,\Omega, \qquad \hat U_e = \sqrt2\cdot12\,\text{V} = 16{,}97\,\text{V}.$$

**Spitzen.** Am Ausgang und im Verbraucher:

$$\hat U_a = 16{,}97\,\text{V} - 1{,}4\,\text{V} = 15{,}57\,\text{V}, \qquad \hat I = \frac{15{,}57\,\text{V}}{100\,\Omega} = 156\,\text{mA}.$$

**Die Totzone.** Unter $1{,}4\,\text{V}$ leitet keine Diode, also in einem Winkel von

$$\arcsin\frac{1{,}4\,\text{V}}{16{,}97\,\text{V}} = 4{,}7^\circ$$

vor und nach jedem Nulldurchgang, zusammen gut $5\,\%$ jeder Halbwelle.

**Der Gleichanteil.** Numerisch über die Bögen gemittelt sind es $9{,}44\,\text{V}$; mit idealen Dioden wären es $\tfrac{2}{\pi}\cdot16{,}97\,\text{V}$, also
$10{,}80\,\text{V}$. Ein Einweggleichrichter mit einer Diode käme auf $5{,}06\,\text{V}$.

**Sperrspannung.** Jede sperrende Diode sieht im Scheitel

$$\hat U_e - U_F = 16{,}27\,\text{V}.$$

**Im Bild:** Jeder Hub muss erst zwei Öffnungsdrücke überwinden, $1{,}4$ zusammen, bevor Wasser fließt; im Scheitel kommen $15{,}57$ von $16{,}97$ an.
::::

:::grafik
Szene: get1/halbleiterbauelemente/04-graetz · Vorlage: graetz-strompfade
Die Brücke wie in Bild 10.25: links die Wechselspannungsquelle mit dem Zählpfeil $u_e$ nach unten, oben $D_1$ waagrecht zum Pluspol rechts oben, unten $D_3$
waagrecht vom Minuspol zur unteren Quellenseite, links $D_2$ senkrecht vom Minuspol zur oberen Quellenseite, rechts $D_4$ senkrecht von der unteren Quellenseite
zum Pluspol; rechts der Verbraucher $R_L$ mit dem Zählpfeil $u_a$ nach unten. Ein Cursor fährt über zwei Perioden: In der positiven Halbwelle leuchten $D_1$ und
$D_3$ und ein Strompfad durch sie und $R_L$, in der negativen $D_2$ und $D_4$, und der Pfeil durch $R_L$ zeigt immer nach unten. Die sperrenden Dioden zeigen
ihre Spannung als Zahl, bis $-16{,}27\,\text{V}$. Darunter $u_e$ mit $16{,}97\,\text{V}$ Scheitel und $u_a$ als Betragsbögen mit $15{,}57\,\text{V}$ Spitze, die
Totzone von $4{,}7^\circ$ um jeden Nulldurchgang grau hinterlegt. Kernaussage: In jeder Halbwelle führt ein anderes Diodenpaar den Strom in derselben Richtung
durch den Verbraucher. (Rot = leitende Dioden und Strompfad, blau = Spannungsverläufe, orange = Totzone und Sperrspannung, grau = sperrende Dioden und Achsen.)
:::

## Glättung mit dem Ladekondensator

Eine pulsierende Spannung ist noch keine Gleichspannung. Das Skript zeigt keine Glättung; sie gehört aber zu jedem Netzteil. Man schaltet einen
__Ladekondensator__ $C$ parallel zum Verbraucher. Kurz vor jedem Scheitel leiten die Dioden und laden ihn auf die Spitze; danach sinkt die Eingangsspannung unter
seine Spannung, alle Dioden sperren, und er versorgt den Verbraucher allein, wobei er sich langsam entlädt. Am Ausgang bleibt eine fast feste Spannung mit einer
kleinen sägezahnförmigen Schwankung, der __Brummspannung__ $\Delta U$, benannt nach dem Brummton, den sie in Lautsprechern erzeugt. Mit dem Laststrom $I_L$ und
der __Pulsfrequenz__ $f_p$, mit der nachgeladen wird, bei der Brücke am $50$-Hz-Netz $100\,\text{Hz}$, beim Einweggleichrichter $50\,\text{Hz}$:

:::formel
$$\Delta U \approx \frac{I_L}{f_p\,C}.$$
:::

**So liest man das:** Doppelte Kapazität oder doppelte Pulsfrequenz halbieren die Brummspannung; die Brücke hat deshalb bei gleichem Kondensator nur die halbe
Brummspannung des Einweggleichrichters. Die Ausgangsspannung schwankt zwischen dem Scheitel $\hat U_a$ und $\hat U_a - \Delta U$. Die Näherung überschätzt etwas,
weil die Entladung nicht ganz eine Pulsperiode dauert.

**Im Bild:** Die Membrankammer wird bei jedem Hub bis zum Spitzendruck gespannt und schiebt in der Pause das Wasser durch den Verbraucher weiter. Je größer die
Kammer und je kürzer die Pause, desto weniger sinkt der Druck.

:::herleitung
**Die Entladung.** Zwischen zwei Nachladungen liefert der Kondensator den Laststrom allein, fast eine ganze Pulsperiode lang, also für die Zeit $1/f_p$. Er
verliert die Ladung $I_L/f_p$, und nach dem Artikel über den Kondensator ändert sich seine Spannung dabei um Ladung durch Kapazität:

$$\Delta Q = \frac{I_L}{f_p}, \qquad \Delta U = \frac{\Delta Q}{C} = \frac{I_L}{f_p\,C}.$$

**Die Voraussetzungen.** Die Brummspannung muss klein gegen die Ausgangsspannung sein; dann bleibt der Laststrom während der Entladung fast fest, und das
Nachladen dauert nur kurz. Im Bild: Eine große Kammer an einem gleichmäßig abnehmenden Verbraucher verliert in jeder Pause dieselbe Wassermenge.
:::

Nachgeladen wird also nur in einem kurzen Stück jeder Halbwelle vor dem Scheitel, ab dem Winkel $\theta$ vor dem Scheitel, dem __Stromflusswinkel__:

$$\cos\theta = 1 - \frac{\Delta U}{\hat U_a}.$$

**So liest man das:** In dieser kurzen Zeit müssen die Dioden die ganze Ladung einer Pulsperiode nachliefern. Ihr Strom ist deshalb während des Nachladens ein
Vielfaches des Laststroms, und Dioden wie Transformator müssen diese Stromspitzen aushalten. Beim Einweggleichrichter mit Ladekondensator kommt etwas
Unangenehmes hinzu: Im negativen Scheitel liegt an der Diode der Kondensator, auf fast $+\hat U$, gegen die Quelle, auf $-\hat U$; die Diode muss fast den
doppelten Scheitelwert sperren.

**Im Bild:** Die Ventile öffnen nur kurz vor jedem Spitzendruck und müssen dann in einem Augenblick alles nachschieben, was die Kammer in der Pause hergegeben hat.

:::herleitung
**Der Winkel.** Nahe dem Scheitel ist die gleichgerichtete Eingangsspannung, um den Winkel $\varphi$ vor dem Scheitel, gleich $\hat U_a\cos\varphi$. Das
Nachladen beginnt, sobald sie die Kondensatorspannung erreicht, die bis dahin auf etwa $\hat U_a - \Delta U$ gesunken ist:

$$\hat U_a\cos\theta = \hat U_a - \Delta U.$$

Division durch $\hat U_a$ ergibt die Formel.

**Der Diodenstrom.** Die Ladung $I_L/f_p$ fließt bei der Brücke innerhalb von $\theta$ je Halbwelle von $180^\circ$; im Mittel ist der Strom in dieser Zeit
also das $180^\circ/\theta$-Fache des Laststroms. Im Bild: Was in der ganzen Pause abgeflossen ist, muss durch das kurz geöffnete Ventil nachkommen.
:::

::::beispiel Ein geglättetes Netzteil
Der Brückengleichrichter am Transformator von oben, jetzt mit Ladekondensator und einem Verbraucher von $150\,\Omega$:

$$\hat U_a = 15{,}57\,\text{V}, \qquad C = 2200\,\mu\text{F}, \qquad R_L = 150\,\Omega, \qquad f_p = 100\,\text{Hz}.$$

**Brummspannung.** Bei rund $15{,}3\,\text{V}$ fließen etwa $102\,\text{mA}$:

$$\Delta U \approx \frac{0{,}102\,\text{A}}{100\,\text{Hz}\cdot2200\,\mu\text{F}} = 0{,}46\,\text{V}.$$

Eine Rechnung Schritt für Schritt in der Zeit, mit idealen Dioden der Durchlassspannung $0{,}7\,\text{V}$, ergibt $0{,}43\,\text{V}$ und einen Mittelwert von
$15{,}36\,\text{V}$; die Näherung überschätzt also leicht. Mit $4700\,\mu\text{F}$ halbiert sich die Brummspannung auf $0{,}21\,\text{V}$.

**Stromflusswinkel.**

$$\cos\theta = 1 - \frac{0{,}46\,\text{V}}{15{,}57\,\text{V}} = 0{,}970, \qquad \theta = 14^\circ.$$

Nachgeladen wird also nur in $14^\circ$ von $180^\circ$, knapp $8\,\%$ der Zeit. In dieser Zeit fließen im Mittel

$$I_L\cdot\frac{180^\circ}{14^\circ} = 102\,\text{mA}\cdot12{,}8 = 1{,}3\,\text{A},$$

mit Spitzen um $2{,}7\,\text{A}$ bei idealen Dioden; in Wirklichkeit begrenzen die Widerstände von Transformator und Dioden sie etwas.

**Einweg zum Vergleich.** Mit nur einer Diode und demselben Kondensator wird nur mit $50\,\text{Hz}$ nachgeladen; die Brummspannung verdoppelt sich auf rund
$0{,}9\,\text{V}$, und die Diode muss im negativen Scheitel

$$2\,\hat U_e - U_F = 2\cdot16{,}97\,\text{V} - 0{,}7\,\text{V} = 33{,}2\,\text{V}$$

sperren.

**Im Bild:** Eine Kammer von $2200\,\mu\text{F}$ verliert in jeder Pause von $10\,\text{ms}$ so viel, dass der Druck um knapp drei Prozent fällt; die Ventile
holen das in weniger als einer Millisekunde wieder herein.
::::

:::grafik
Szene: get1/halbleiterbauelemente/04-glaettung · Vorlage: ladekondensator-brumm
Oben die Brücke mit dem Ladekondensator $C$ parallel zum Verbraucher $R_L$. Darunter zwei Zeitverläufe über drei Halbwellen: die Betragsbögen der
gleichgerichteten Eingangsspannung bis $15{,}57\,\text{V}$ als dünne Linie und darüber die Kondensatorspannung, die jeweils kurz vor dem Scheitel auf den Bogen
aufläuft, ihm bis zur Spitze folgt und dann flach absinkt; die Brummspannung $\Delta U$ ist als Höhe des Sägezahns beschriftet, der Stromflusswinkel $\theta$ als
schmaler Streifen vor jedem Scheitel. Ganz unten der Diodenstrom als schmale, hohe Pulse in diesen Streifen, mit dem Laststrom als niedrige Linie zum Vergleich.
Regler für $C$ von $470$ bis $10\,000\,\mu\text{F}$ und für $R_L$ von $50$ bis $1000\,\Omega$ verändern Sägezahn, Streifen und Pulse; ein Schalter wechselt zum
Einweggleichrichter mit nur jedem zweiten Puls. Kernaussage: Der Ladekondensator überbrückt die Pausen, und nachgeladen wird in kurzen, starken Stromstößen.
(Rot = Kondensatorspannung und Brummspannung, blau = Eingangsbögen, orange = Diodenstrompulse, grau = Achsen und Laststrom.)
:::

## Die Ladungspumpe

Die zweite Schaltung des Skripts erhöht eine Gleichspannung. In Bild 10.23 führen von der Eingangsspannung $U_e$ eine Diode $D_1$ und ein Widerstand $R_1$ zur
oberen Platte des __Pumpkondensators__ $C_1$, von dort ein Widerstand $R_2$ und eine Diode $D_2$ zum Ausgang mit dem __Ausgangskondensator__ $C_2$. Ein Schalter
legt die untere Platte von $C_1$ entweder an Masse oder an den Pluspol des Eingangs. Die Dioden sind, wie im Skript, ideal.

Im ersten Schritt liegt die untere Platte an Masse, und $C_1$ lädt sich über $D_1$ und $R_1$ auf $U_e$. Im zweiten Schritt schaltet der Schalter die untere
Platte an $U_e$. Die Spannung von $C_1$ kommt damit auf die Eingangsspannung obendrauf, die obere Platte liegt bei $2U_e$; $D_1$ sperrt, weil ihre Kathode jetzt
höher liegt als ihre Anode, $D_2$ leitet, und $C_1$ schiebt Ladung in $C_2$. Wiederholt man die beiden Schritte, steigt die Spannung an $C_2$ gegen $2U_e$. Die
Widerstände begrenzen die Stromstöße beim Umschalten und legen mit den Kapazitäten die Zeitkonstanten fest, wie im Artikel über Laden und Entladen; dauert jeder
Schritt einige Zeitkonstanten, ändern sie die Endwerte nicht. Ohne Last gilt von Takt $k$ zu Takt $k + 1$ für die Ausgangsspannung $U_a$:

:::formel
$$U_{a,k+1} = U_{a,k} + \frac{C_1}{C_1 + C_2}\,\big(2\,U_e - U_{a,k}\big).$$
:::

**So liest man das:** Jeder Takt schließt die Lücke zur doppelten Eingangsspannung um den Anteil $C_1/(C_1 + C_2)$, bei gleichen Kondensatoren um die Hälfte.
Die $2U_e$, die das Skript als „ca. $2U_e$“ nennt, erreicht die Pumpe ohne Last nach vielen Takten, aber nie ganz. Sind die Dioden nicht ideal, kostet jede ihre
Durchlassspannung: $C_1$ lädt sich nur auf $U_e - U_F$, so wie Bild 10.24 es beschriftet, obwohl das Skript die Dioden ideal nennt, und am Ausgang kommen höchstens
$2U_e - 2U_F$ an.

**Im Bild:** Eine Membrankammer wird an der Pumpe gefüllt und dann so umgesteckt, dass ihr Druck auf den der Pumpe obendrauf kommt. Sie entleert sich in eine
zweite Kammer, und jeder Hub hebt deren Druck ein Stück weiter zum Doppelten.

:::herleitung
**Die Ladung bleibt erhalten.** Am Anfang des zweiten Schritts hat $C_1$ die Spannung $U_e$, $C_2$ die Spannung $U_{a,k}$. Die Ladung $q$, die durch $D_2$
fließt, verlässt $C_1$ und kommt in $C_2$ an; der Strom fließt, bis die Spannungen auf beiden Seiten der Diode gleich sind:

$$U_e + \Big(U_e - \frac{q}{C_1}\Big) = U_{a,k} + \frac{q}{C_2}.$$

**Nach der Ladung aufgelöst** und durch $C_2$ geteilt ergibt sich der Spannungszuwachs:

$$q = \frac{C_1\,C_2}{C_1 + C_2}\,\big(2\,U_e - U_{a,k}\big), \qquad U_{a,k+1} = U_{a,k} + \frac{q}{C_2}.$$

Im nächsten ersten Schritt lädt sich $C_1$ wieder voll auf $U_e$. Im Bild: Die umgesteckte Kammer und die zweite Kammer gleichen ihren Druck aus, und was die eine
abgibt, nimmt die andere auf.
:::

Unter Last entnimmt der Verbraucher in jedem Takt die Ladung $I_L/f_s$, wenn die Pumpe mit der Frequenz $f_s$ schaltet. Am Ende jedes Umladens und als
Schwankung bis zum nächsten gilt dann:

$$U_{a,\text{max}} = 2\,U_e - \frac{I_L}{f_s\,C_1}, \qquad \Delta U_a = \frac{I_L}{f_s\,C_2}.$$

**So liest man das:** Die Pumpe wirkt wie eine Quelle von $2U_e$ mit dem Innenwiderstand $1/(f_sC_1)$. Schneller takten oder einen größeren Pumpkondensator
nehmen macht sie belastbarer, ein größerer Ausgangskondensator macht sie glatter. In integrierten Schaltungen ist der Schalter ein Transistor, der mit
$100\,\text{kHz}$ bis einigen Megahertz taktet; so erzeugen Schnittstellenbausteine für RS-232 aus $5\,\text{V}$ die nötigen $\pm10\,\text{V}$ und Flash-Speicher
ihre Programmierspannung.

Weitere Stufen, wie das Skript andeutet, stapeln je einen Kondensator auf die schon erhöhte Spannung; mit $N$ Stufen sind ohne Verluste bis zu $(N + 1)\,U_e$
möglich. Mit Wechselspannung statt Schalter arbeiten der Spannungsverdoppler nach Greinacher und die Kaskade von Cockcroft und Walton, mit der beide 1932 erstmals
Atomkerne, Lithium, mit beschleunigten Protonen spalteten.

**Im Bild:** Bei jedem Umstecken muss die Kammer den Verbrauch eines Takts nachliefern; was ihr dabei an Druck fehlt, fehlt am Ausgang.

:::herleitung
**Stationär.** Im Gleichgewicht muss $C_1$ in jedem Takt die Ladung $q = I_L/f_s$ nach $C_2$ bringen. Weil $C_1$ zu Beginn jedes Umladens auf $U_e$ steht,
endet das Umladen bei

$$U_{a,\text{max}} = U_e + \Big(U_e - \frac{q}{C_1}\Big) = 2\,U_e - \frac{I_L}{f_s\,C_1}.$$

**Die Schwankung.** Bis zum nächsten Umladen versorgt $C_2$ den Verbraucher allein und verliert dabei $q$, also die Spannung $q/C_2$.

**Stufen.** Jede weitere Stufe lädt ihren Kondensator auf die Ausgangsspannung der vorigen und hebt ihn um die Eingangsspannung an; ohne Verluste kommt je Stufe
einmal $U_e$ hinzu. Im Bild: Jede weitere Kammer steht eine Etage höher auf der vorigen.
:::

::::beispiel Eine Ladungspumpe für 10 V aus 5 V
**(a) Gleiche Kondensatoren.** Ideale Dioden, ohne Last, der Ausgangskondensator anfangs leer:

$$U_e = 5\,\text{V}, \qquad C_1 = C_2 = 1\,\mu\text{F}.$$

Jeder Takt schließt die halbe Lücke zu $10\,\text{V}$:

$$U_a: \quad 5\,\text{V}, \quad 7{,}5\,\text{V}, \quad 8{,}75\,\text{V}, \quad 9{,}38\,\text{V}, \quad 9{,}69\,\text{V}, \quad \dots$$

Nach sieben Takten fehlen noch $0{,}08\,\text{V}$.

**(b) Großer Ausgangskondensator.** Mit $C_2 = 10\,\mu\text{F}$ schließt jeder Takt nur ein Elftel der Lücke:

$$U_a: \quad 0{,}91\,\text{V}, \quad 1{,}74\,\text{V}, \quad 2{,}49\,\text{V}, \quad 3{,}17\,\text{V}, \quad \dots$$

Die Pumpe braucht länger, glättet dafür später besser.

**(c) Echte Dioden.** Mit $0{,}6\,\text{V}$ je Diode lädt sich $C_1$ auf $4{,}4\,\text{V}$, seine obere Platte kommt auf $9{,}4\,\text{V}$, und am Ausgang bleiben
höchstens

$$2\cdot5\,\text{V} - 2\cdot0{,}6\,\text{V} = 8{,}8\,\text{V}.$$

**(d) Unter Last.** Ideale Dioden und

$$C_1 = 1\,\mu\text{F}, \qquad C_2 = 10\,\mu\text{F}, \qquad f_s = 100\,\text{kHz}, \qquad I_L = 10\,\text{mA}.$$

Je Takt fließen $0{,}1\,\mu\text{C}$:

$$U_{a,\text{max}} = 10\,\text{V} - \frac{10\,\text{mA}}{100\,\text{kHz}\cdot1\,\mu\text{F}} = 9{,}9\,\text{V}, \qquad \Delta U_a = \frac{10\,\text{mA}}{100\,\text{kHz}\cdot10\,\mu\text{F}} = 10\,\text{mV}.$$

Eine Rechnung Takt für Takt bestätigt beide Werte.

**Im Bild:** Eine kleine Kammer, hunderttausendmal je Sekunde umgesteckt, hält eine große Kammer fast auf dem doppelten Druck, obwohl ständig Wasser abfließt.
::::

:::grafik
Szene: get1/halbleiterbauelemente/04-ladungspumpe · Vorlage: ladungspumpe-takte
Die Schaltung aus Bild 10.23: Eingang $U_e = 5\,\text{V}$, $D_1$ und $R_1$ zur oberen Platte von $C_1$, $R_2$ und $D_2$ zum Ausgang mit $C_2$ und dem Zählpfeil
$U_a$, ein Schalter an der unteren Platte von $C_1$. Ein Knopf „Takt“ schaltet um: Im ersten Schritt fließt ein Strompfeil über $D_1$ in $C_1$, und dessen
Spannung steigt auf $5\,\text{V}$; im zweiten springt die untere Platte auf $5\,\text{V}$, die obere auf $10\,\text{V}$, $D_1$ wird grau, ein Strompfeil fließt
über $D_2$ in $C_2$. Rechts ein Treppendiagramm von $U_a$ über der Taktzahl, mit wählbarem Verhältnis $C_2/C_1$ von $1$ bis $10$ und einer gestrichelten Linie
bei $2U_e$. Ein Regler für den Laststrom senkt den Endwert auf $2U_e - I_L/(f_sC_1)$ und lässt am Ausgang eine kleine Zacke erscheinen. Kernaussage: Die
Pumpe stapelt die Spannung des Pumpkondensators auf die Eingangsspannung und schiebt in jedem Takt Ladung nach oben. (Rot = Dioden und ihr Zustand, blau =
Ladungen und Spannungen, orange = Schalter und Treppe, grau = Schaltung.)
:::

## Bedeutung und Ausblick

Ein klassisches Netzteil besteht aus genau diesen Bausteinen: Ein Transformator setzt die Netzspannung herab und trennt sie galvanisch, eine Brücke richtet sie
gleich, ein Ladekondensator glättet sie, und eine Stabilisierung, etwa mit der Z-Diode aus dem Artikel über die Kennlinie, hält sie fest. Moderne
Schaltnetzteile richten das Netz unmittelbar gleich, zerhacken die Gleichspannung mit vielen Kilohertz, übertragen sie mit einem kleinen Transformator und
richten sie wieder gleich; die Bausteine sind dieselben. Ladungspumpen versorgen innerhalb von Chips Teile, die mehr Spannung brauchen, als von außen anliegt.

Damit ist die Diode als erstes Halbleiterbauelement vollständig. Das nächste Kapitel setzt zwei pn-Übergänge eng hintereinander: Im Bipolartransistor steuert
ein kleiner Strom einen großen.

:::kern
- Der Gleichanteil ist der arithmetische Mittelwert; der Gleichrichtwert einer Sinusspannung ist $\tfrac{2}{\pi}\hat U$.
- In der Graetz-Brücke leiten je Halbwelle zwei Dioden, und der Strom durchfließt den Verbraucher immer in derselben Richtung.
- Der Brückenausgang ist der Betrag der Eingangsspannung minus zwei Durchlassspannungen: $u_a=|u_e|-2U_F$.
- In der Totzone unter $2U_F$ leitet keine Diode; jede sperrende Diode muss fast den Scheitelwert aushalten.
- Ein Ladekondensator glättet bis auf die Brummspannung $\Delta U\approx I_L/(f_pC)$.
- Nachgeladen wird nur kurz vor dem Scheitel; die Diodenströme sind dann ein Vielfaches des Laststroms.
- Die Ladungspumpe lädt einen Kondensator, stapelt ihn auf die Eingangsspannung und entlädt ihn in den Ausgang, bis gegen $2U_e$.
- Je Takt schließt sich die Lücke um $C_1/(C_1+C_2)$; unter Last fehlt $I_L/(f_sC_1)$.
:::

:::quiz
F: Was unterscheidet Gleichanteil und Gleichrichtwert, und welche Werte ergeben sich für eine Sinusspannung?
A: Der Gleichanteil ist der Mittelwert der Spannung selbst, bei einer Sinusspannung null; der Gleichrichtwert ist der Mittelwert ihres Betrags, $\tfrac{2}{\pi}\hat U$. Bei $10\,\text{V}$ Scheitelwert sind das $6{,}37\,\text{V}$ nach einer idealen Brücke und $3{,}18\,\text{V}$ nach einem Einweggleichrichter; am Netz liefert eine Brücke im Mittel $207\,\text{V}$.
F: Wie nutzt die Graetz-Brücke beide Halbwellen?
A: In der positiven Halbwelle leiten $D_1$ und $D_3$, in der negativen $D_2$ und $D_4$; beide Paare führen den Strom vom Pluspol durch den Verbraucher. Der Ausgang ist der Betrag der Eingangsspannung und pulsiert mit doppelter Netzfrequenz, am $50$-Hz-Netz mit $100\,\text{Hz}$.
F: Warum ist der Scheitel am Brückenausgang um $2U_F$ kleiner, und was ist die Totzone?
A: In jeder Halbwelle liegen zwei Dioden im Strompfad, und jede verlangt ihre Durchlassspannung; beim Skript $8{,}8$ statt $10\,\text{V}$, am Transformator $15{,}57$ statt $16{,}97\,\text{V}$. Unter $2U_F$ leitet keine Diode, und der Ausgang ist null, am Transformator $4{,}7^\circ$ vor und nach jedem Nulldurchgang.
F: Welche Sperrspannung müssen die Dioden aushalten?
A: In der Brücke liegt an jeder sperrenden Diode $-(u_a+U_F)$, im Scheitel also $\hat U_e-U_F$, am Transformator $16{,}27\,\text{V}$. Ein Einweggleichrichter mit Ladekondensator verlangt dagegen fast den doppelten Scheitelwert, dort $33{,}2\,\text{V}$, weil der geladene Kondensator gegen den negativen Scheitel der Quelle steht.
F: Was stimmt in der Aussage des Skripts über sehr kleine positive Spannungen nicht?
A: Das Skript sagt, bei negativer oder sehr kleiner positiver Spannung leiteten $D_2$ und $D_4$. Bei kleinen positiven Spannungen sperren aber alle vier, wie es selbst kurz danach schreibt; $D_2$ und $D_4$ leiten erst unter $-2U_F$.
F: Wie glättet der Ladekondensator, und wie groß ist die Brummspannung?
A: Er wird kurz vor jedem Scheitel nachgeladen und versorgt den Verbraucher in den Pausen allein; dabei verliert er die Ladung $I_L/f_p$ und damit $\Delta U\approx I_L/(f_pC)$. Am Transformator mit $2200\,\mu\text{F}$ und $102\,\text{mA}$ sind das $0{,}46\,\text{V}$, schrittweise in der Zeit gerechnet $0{,}43\,\text{V}$; der Einweggleichrichter hätte das Doppelte.
F: Warum sind die Diodenströme beim Glätten viel größer als der Laststrom?
A: Nachgeladen wird nur im Stromflusswinkel vor dem Scheitel, mit $\cos\theta=1-\Delta U/\hat U_a$, im Beispiel $14^\circ$ von $180^\circ$. In dieser kurzen Zeit muss die ganze Ladung einer Pulsperiode nachfließen; im Mittel $1{,}3\,\text{A}$ statt $102\,\text{mA}$, mit Spitzen um $2{,}7\,\text{A}$ bei idealen Dioden.
F: Wie funktioniert die Ladungspumpe des Skripts?
A: Im ersten Schritt lädt sich $C_1$ über $D_1$ auf $U_e$. Im zweiten legt der Schalter seine untere Platte an $U_e$, die obere kommt auf $2U_e$, $D_1$ sperrt, $D_2$ leitet, und $C_1$ schiebt Ladung in $C_2$. Wiederholt man das, steigt $U_a$ gegen $2U_e$; $R_1$ und $R_2$ begrenzen die Stromstöße.
F: Wie schnell nähert sich die Pumpe $2U_e$, und was bewirkt eine Last?
A: Jeder Takt schließt die Lücke um $C_1/(C_1+C_2)$; mit gleichen Kondensatoren und $5\,\text{V}$ ergeben sich $5$, $7{,}5$, $8{,}75$, $9{,}38\,\text{V}$ und so fort. Unter Last fehlt am Ende jedes Umladens $I_L/(f_sC_1)$, und $C_2$ schwankt um $I_L/(f_sC_2)$; mit $10\,\text{mA}$ bei $100\,\text{kHz}$ sind das $9{,}9\,\text{V}$ und $10\,\text{mV}$.
F: Was ändern echte Dioden und weitere Stufen?
A: Jede Diode kostet ihre Durchlassspannung: $C_1$ lädt sich nur auf $U_e-U_F$, wie Bild 10.24 beschriftet, obwohl das Skript ideale Dioden annimmt, und am Ausgang bleiben höchstens $2U_e-2U_F$, aus $5\,\text{V}$ also $8{,}8\,\text{V}$. Jede weitere Stufe stapelt einen Kondensator auf und bringt ohne Verluste bis zu einmal $U_e$ hinzu.
:::
