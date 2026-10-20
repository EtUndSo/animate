---
title: Ideale und reale Quellen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70300
summary: Von Grund auf – was eine Quelle festhält und was sie nachgibt, warum echte Quellen unter Last einbrechen und warum eine reale Spannungsquelle und eine reale Stromquelle von außen nicht zu unterscheiden sind. Leitbild sind Wasserturm und Spritzenpumpe: Der Turm hält den Druck, die Pumpe den Durchfluss, die dünne Zuleitung und das Leck machen sie real. Mit idealen Quellen und ihren Kennlinien, den verbotenen Grenzfällen Kurzschluss und Leerlauf, Innenwiderstand und Innenleitwert, Leerlaufspannung und Kurzschlussstrom, der Quellenumwandlung samt ihrer Grenze im Inneren und dem Zusammenschalten von Quellen mit Ausgleichsströmen. Mit Beispiel-Seite.
tags: Spannungsquelle, Stromquelle, Innenwiderstand, Leerlaufspannung, Kurzschlussstrom, Quellenumwandlung
---

## Anschaulich

Jede Schaltung braucht einen Antrieb, eine __Quelle__. Eine Quelle stellt Spannung und Strom bereit, aber nicht beides nach Belieben: Was die Last
verlangt, bestimmt immer mit. Eine __ideale__ Quelle hält eine der beiden Größen fest und lässt die andere sich nach der Last richten. Echte Quellen
schaffen auch das nur ungefähr; dass sie nachgeben, beschreibt ihr __Innenwiderstand__.

**Das Leitbild dieses Artikels:** **Wasserturm und Spritzenpumpe.** Ein Wasserturm hält den Druck am Wasserhahn fest, denn der hängt nur von der
Höhe des Wasserspiegels ab — gleich, wie viel man zapft. Eine Spritzenpumpe, wie sie im Krankenhaus Infusionen gibt, schiebt den Kolben mit festem
Tempo vor und hält damit den Durchfluss fest — gleich, gegen welchen Druck. Der Turm ist eine ideale __Spannungsquelle__, die Pumpe eine ideale
__Stromquelle__.

Echt werden beide durch einen Makel. Der Turm hängt an einer dünnen Zuleitung: Je mehr man zapft, desto mehr Druck geht in ihr verloren. Die Pumpe hat
ein Leck zurück in den Vorratsbehälter: Je höher der Gegendruck, desto mehr fließt zurück, statt beim Verbraucher anzukommen.

Drei Folgerungen kann man Turm und Pumpe direkt ansehen:

- **Jede ideale Quelle hat einen verbotenen Fall.** Den Hahn am Turm ohne jeden Widerstand ganz zu öffnen, hieße unendlicher Durchfluss; die Pumpe gegen
  einen geschlossenen Hahn laufen zu lassen, hieße unendlicher Druck.
- **Echte Quellen geben linear nach.** Der Druckverlust in der Zuleitung wächst mit dem Durchfluss, der Rückfluss durchs Leck mit dem Druck.
- **Von außen sind beide gleich.** Am Hahn misst man nur Druck und Durchfluss. Ein Turm mit Zuleitung und eine Pumpe mit Leck, passend bemessen, liefern
  bei jedem Verbrauch dasselbe — man kann sie ineinander umrechnen.

:::grafik
Szene: get1/analyse-linearer-netzwerke/01-turm-pumpe · Vorlage: wasserturm-spritzenpumpe
Links ein Wasserturm mit Hahn und einem Durchflussmesser, rechts eine Spritzenpumpe mit gleichmäßig vorrückendem Kolben, beide an einen verstellbaren
Verbraucher angeschlossen. Ein Regler öffnet den Verbraucher: Am Turm bleibt der Druck fest und der Durchfluss wächst, an der Pumpe bleibt der
Durchfluss fest und der Druck sinkt. Ein Schalter „real" fügt dem Turm eine dünne Zuleitung hinzu — der Druck am Hahn fällt mit steigendem Durchfluss —
und der Pumpe ein Leck zurück in den Behälter, das bei hohem Druck mehr zurückfließen lässt. Unten zwei Diagramme Druck über Durchfluss, die für passend
gewählte Zuleitung und Leck zu derselben fallenden Geraden zusammenfallen. Kernaussage: Ideale Quellen halten eine Größe fest, reale geben linear nach,
und von außen sind reale Spannungs- und Stromquellen gleichwertig. (Blau = Wasser, rot = Quellen, orange = Zuleitung und Leck, grau = Behälter und
Verbraucher.)
:::

## Die ideale Spannungsquelle

Eine __ideale Spannungsquelle__ stellt an ihren Klemmen eine feste Spannung $U_q$ bereit, unabhängig vom Strom, der aus ihr fließt (Bild 7.16 des
Skripts: ein Kreis, durch den die Leitung hindurchgeht, mit dem Spannungspfeil $U_q$). Ihre __Kennlinie__ ist deshalb eine Gerade parallel zur
Stromachse (Bild 7.17):

$$U = U_q \quad\text{für jeden Strom } I.$$

**So liest man das:** Welcher Strom fließt, entscheidet allein die angeschlossene Schaltung; die Quelle hält nur die Spannung. In der Analyse setzt man
ihre Spannung direkt als Differenz der Potenziale der beiden Knoten an, an die sie angeschlossen ist. Kurzschließen darf man eine ideale
Spannungsquelle nicht: Ohne Widerstand im Kreis gäbe es keinen endlichen Strom.

**Im Bild:** Der Wasserturm mit unendlich weiter Zuleitung. Am Hahn herrscht immer derselbe Druck.

:::herleitung
**Der Strom kommt von der Last.** An einem Widerstand $R$ liegt die feste Spannung $U_q$, also fließt nach Ohm

$$I = \frac{U_q}{R}.$$

Halber Widerstand, doppelter Strom; die Quelle liefert, was die Last verlangt.

**Kurzschluss.** Lässt man $R$ gegen null gehen, wächst dieser Strom über alle Grenzen. Ein Kreis aus einer idealen Spannungsquelle und einem
widerstandslosen Draht verletzte die Maschenregel: Um den Kreis müsste die Spannung $U_q$ abfallen, am Draht fällt aber keine ab.
:::

## Die ideale Stromquelle

Eine __ideale Stromquelle__ erzwingt einen festen Strom $I_q$ durch sich hindurch, unabhängig von der Spannung, die an ihr liegt (Bild 7.18: ein Kreis
mit einem Querstrich senkrecht zur Leitung, mit dem Strompfeil $I_q$). Ihre Kennlinie ist eine Gerade parallel zur Spannungsachse (Bild 7.19; dessen
Unterschrift nennt versehentlich eine Spannungsquelle):

$$I = I_q \quad\text{für jede Spannung } U.$$

**So liest man das:** Welche Spannung sich einstellt, entscheidet die angeschlossene Schaltung; die Quelle hält nur den Strom. In der Analyse legt sie den
Strom in ihrem Zweig fest. Das setzt voraus, wie das Skript betont, dass die Beschaltung einen Stromfluss erlaubt: Offen lassen darf man eine ideale
Stromquelle nicht.

**Im Bild:** Die Spritzenpumpe ohne Leck. Sie schiebt immer denselben Durchfluss, und der Druck steigt so weit, wie es nötig ist.

:::herleitung
**Die Spannung kommt von der Last.** Durch einen Widerstand $R$ fließt der feste Strom $I_q$, also liegt an ihm nach Ohm

$$U = R\,I_q.$$

Doppelter Widerstand, doppelte Spannung.

**Leerlauf.** Lässt man $R$ gegen unendlich gehen, wächst die Spannung über alle Grenzen. Eine offene ideale Stromquelle verletzte die Knotenregel: Ihr
Strom müsste in den offenen Anschluss fließen, und dort geht er nicht weiter.
:::

::::beispiel Zwei ideale Quellen an drei Lasten
**(a) Eine Spannungsquelle mit 5 Volt** an $100\,\Omega$, $10\,\Omega$ und $1\,\Omega$:

$$I = 50\,\text{mA}, \qquad I = 0{,}5\,\text{A}, \qquad I = 5\,\text{A}.$$

Die Spannung bleibt $5\,\text{V}$, die abgegebene Leistung steigt von $0{,}25$ über $2{,}5$ auf $25\,\text{W}$.

**(b) Eine Stromquelle mit 20 Milliampere** an $100\,\Omega$, $1\,\text{k}\Omega$ und $10\,\text{k}\Omega$:

$$U = 2\,\text{V}, \qquad U = 20\,\text{V}, \qquad U = 200\,\text{V}.$$

Der Strom bleibt $20\,\text{mA}$, die Spannung und die Leistung steigen mit dem Widerstand, bei $10\,\text{k}\Omega$ auf $4\,\text{W}$. Keine echte Quelle hält
das unbegrenzt durch.

**Im Bild:** Je weiter der Hahn am Turm offen ist, desto mehr fließt; je enger er an der Pumpe ist, desto höher steigt der Druck.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/01-ideale-kennlinien · Vorlage: ideale-quellen
Zwei Spalten nach Bild 7.16 bis 7.19 des Skripts. Links das Symbol der idealen Spannungsquelle mit $U_q$ und darunter ihre Kennlinie, $U$ über $I$ als
waagrechte Gerade bei $U_q$ und $I$ über $U$ als senkrechte; rechts das Symbol der idealen Stromquelle mit $I_q$ und ihre Kennlinie, $I$ über $U$ waagrecht bei
$I_q$ und $U$ über $I$ senkrecht. Ein Lastregler verschiebt auf jeder Kennlinie den Betriebspunkt als Schnittpunkt mit der Widerstandsgeraden der Last;
bei Lastwiderstand null (Spannungsquelle) bzw. unendlich (Stromquelle) läuft der Punkt aus dem Bild, ein Warnsymbol erscheint. Kernaussage: Eine ideale
Quelle hält eine Größe fest, die andere bestimmt die Last. (Rot = Quellen und Kennlinien, blau = Lastgerade, orange = Betriebspunkt und Warnung, grau =
Achsen.)
:::

## Die reale Spannungsquelle

Echte Quellen geben unter Last nach. Belastet man eine Batterie mit wachsendem Strom (Bild 7.20 des Skripts), fällt ihre Klemmenspannung vom Wert im
Leerlauf aus linear ab. Die Ursache sind Widerstände in ihrem Inneren, die Leiter und der chemische Weg der Ladung, an denen der Strom Spannung kostet.
Ein __Ersatzschaltbild__ ist eine Schaltung aus idealen Bauteilen, die sich an den Klemmen verhält wie das echte Gerät. Das der __realen
Spannungsquelle__ (Bild 7.21a) ist eine ideale Spannungsquelle $U_q$ mit dem __Innenwiderstand__ $R_q$ in Reihe, im Skript auch Quellwiderstand genannt;
$I_A$ ist der Strom aus der Klemme A, $U_{AB}$ die Klemmenspannung:

:::formel
$$U_{AB} = U_q - R_q\,I_A.$$
:::

**So liest man das:** Gleichung 7.1 des Skripts. Die Klemmenspannung ist die __Leerlaufspannung__ $U_q$ minus dem Spannungsabfall am Innenwiderstand. Im
Leerlauf, ohne Strom, liegt an den Klemmen die volle Leerlaufspannung; bei Kurzschluss, ohne Klemmenspannung, fließt der __Kurzschlussstrom__
$U_q/R_q$. Die Kennlinie ist eine fallende Gerade zwischen diesen beiden Punkten, umso flacher, je kleiner $R_q$ (Bild 7.22a). Den Innenwiderstand bestimmt
man aus zwei Messpunkten als Betrag der Steigung, $\frac{\Delta U}{\Delta I}$.

**Im Bild:** Der Wasserturm mit dünner Zuleitung. Der Druck am Hahn ist der Turmdruck minus dem Verlust in der Leitung, und der wächst mit dem Durchfluss.

:::herleitung
**Die Kennlinie.** Durch den Innenwiderstand fließt der Klemmenstrom $I_A$, an ihm fällt nach Ohm $R_q I_A$ ab. Die Maschenregel um Quelle, Innenwiderstand
und Klemmen ergibt die Formel.

**Leerlauf und Kurzschluss.** Mit $I_A$ gleich null bleibt $U_q$; mit $U_{AB}$ gleich null ist $I_A$ gleich $U_q/R_q$.

**Innenwiderstand aus zwei Punkten.** Zwei Messpunkte $(I_1, U_1)$ und $(I_2, U_2)$ erfüllen beide die Kennlinie; ihre Differenz enthält nur noch $R_q$:

$$U_1 - U_2 = R_q\,(I_2 - I_1), \qquad R_q = \frac{U_1 - U_2}{I_2 - I_1}.$$

**Mit Last.** Ein Lastwiderstand $R_L$ an den Klemmen liegt mit $R_q$ in Reihe; Strom und Klemmenspannung folgen aus der Reihenschaltung und dem
Spannungsteiler:

$$I_A = \frac{U_q}{R_q + R_L}, \qquad U_{AB} = U_q\,\frac{R_L}{R_q + R_L}.$$
:::

::::beispiel Die Autobatterie
Eine Autobatterie zeigt im Leerlauf $12{,}70\,\text{V}$; beim Anlassen, mit $200\,\text{A}$, nur noch $11{,}10\,\text{V}$. Ihr Innenwiderstand:

$$R_q = \frac{12{,}70\,\text{V} - 11{,}10\,\text{V}}{200\,\text{A} - 0\,\text{A}} = 8\,\text{m}\Omega.$$

Theoretisch läge der Kurzschlussstrom bei

$$\frac{12{,}70\,\text{V}}{8\,\text{m}\Omega} \approx 1600\,\text{A},$$

genug, um ein Werkzeug zwischen den Polen zu verschweißen. Mit den Scheinwerfern als Last von $1{,}3\,\Omega$ dagegen:

$$I_A = \frac{12{,}70\,\text{V}}{1{,}308\,\Omega} \approx 9{,}71\,\text{A}, \qquad U_{AB} \approx 12{,}62\,\text{V}.$$

Bei kleinen Strömen merkt man vom Innenwiderstand kaum etwas, beim Anlasser sehr wohl — das Licht wird beim Starten dunkler.

**Im Bild:** Eine weite Zuleitung: Beim Zähneputzen sinkt der Druck nicht, wenn aber alle Hähne gleichzeitig voll laufen, schon.
::::

## Die reale Stromquelle

Das Gegenstück ist die __reale Stromquelle__ (Bild 7.21b): eine ideale Stromquelle $I_q$ mit dem __Innenleitwert__ $G_q$ parallel, im Skript Quellleitwert genannt. Ein Teil ihres Stroms
fließt durch diesen Leitwert gleich wieder zurück, und zwar umso mehr, je höher die Klemmenspannung ist:

:::formel
$$I_A = I_q - G_q\,U_{AB}.$$
:::

**So liest man das:** Gleichung 7.2 des Skripts. Der Klemmenstrom ist der __Kurzschlussstrom__ $I_q$ minus dem Strom durch den Innenleitwert. Bei
Kurzschluss kommt der ganze Strom heraus; im Leerlauf fließt alles durch $G_q$, und an den Klemmen liegt die Leerlaufspannung $I_q/G_q$. Je kleiner $G_q$,
desto flacher die Kennlinie (Bild 7.22b), desto näher an der idealen Stromquelle.

**Im Bild:** Die Spritzenpumpe mit Leck. Was sie fördert, kommt beim Verbraucher an, abzüglich dessen, was der Gegendruck durchs Leck zurückdrückt.

:::herleitung
**Die Kennlinie.** An der Klemme A treffen drei Ströme zusammen: der Quellstrom $I_q$, der Strom $G_q U_{AB}$ durch den Innenleitwert, der parallel an der
Klemmenspannung liegt, und der Klemmenstrom $I_A$. Die Knotenregel ergibt die Formel.

**Kurzschluss und Leerlauf.** Mit $U_{AB}$ gleich null bleibt $I_q$; mit $I_A$ gleich null ist $U_{AB}$ gleich $I_q/G_q$.

**Mit Last.** Ein Lastwiderstand $R_L$ liegt parallel zu $G_q$; nach dem Stromteiler bekommt er

$$I_A = I_q\,\frac{1/R_L}{G_q + 1/R_L} = \frac{I_q}{1 + G_q R_L}.$$
:::

::::beispiel Die Stromschleife 4 bis 20 Milliampere
Industrielle Sensoren melden ihren Messwert oft als Strom zwischen $4$ und $20\,\text{mA}$. Der Sender ist eine Stromquelle; mit $20\,\text{mA}$ und einem
Innenleitwert von $1\,\mu\text{S}$, also $1\,\text{M}\Omega$ parallel, ergibt sich an einem Messwiderstand von $250\,\Omega$:

$$I_A = \frac{20\,\text{mA}}{1 + 10^{-6}\,\text{S}\cdot250\,\Omega} \approx 19{,}995\,\text{mA}, \qquad U_{AB} \approx 5{,}00\,\text{V}.$$

Kommen $100\,\Omega$ Leitungswiderstand dazu, sind es $19{,}993\,\text{mA}$, mit $1\,\text{k}\Omega$ insgesamt $19{,}98\,\text{mA}$. Der Messwert hängt kaum
von der Leitung ab — darum überträgt man Messwerte über weite Strecken lieber als Strom statt als Spannung.

**Im Bild:** Eine Pumpe mit winzigem Leck: Ob der Schlauch kurz oder lang ist, es kommt fast genau der eingestellte Durchfluss an.
::::

## Spannungsquelle und Stromquelle ineinander umrechnen

Zwei Netzwerke heißen __äquivalent__, wenn sie an ihren Klemmen dieselbe Kennlinie haben (Abschnitt 7.4.2 des Skripts): Eine angeschlossene Schaltung
kann sie dann nicht unterscheiden. Eine reale Spannungsquelle und eine reale Stromquelle sind äquivalent, wenn

:::formel Satz
$$U_q = \frac{I_q}{G_q}, \qquad R_q = \frac{1}{G_q}, \qquad\text{gleichwertig}\qquad I_q = \frac{U_q}{R_q}.$$
:::

**So liest man das:** Die Leerlaufspannung der Stromquelle ist die Quellenspannung der Spannungsquelle, der Kurzschlussstrom der Spannungsquelle der
Quellstrom der Stromquelle, und der Innenwiderstand ist in beiden Darstellungen derselbe — einmal in Reihe, einmal parallel. Für ideale Quellen gibt es
keine Umrechnung: Ohne Innenwiderstand würde der Kurzschlussstrom unendlich, ohne Innenleitwert die Leerlaufspannung.

**Im Bild:** Turm mit Zuleitung und Pumpe mit Leck, so bemessen, dass sie bei geschlossenem Hahn denselben Druck und bei offenem denselben Durchfluss
liefern. Dazwischen liegen beide auf derselben Geraden.

:::herleitung
**Kennlinien vergleichen.** Die Kennlinie der Stromquelle, nach der Klemmenspannung aufgelöst, und die der Spannungsquelle:

$$U_{AB} = \frac{I_q - I_A}{G_q} = \frac{I_q}{G_q} - \frac{1}{G_q}\,I_A, \qquad U_{AB} = U_q - R_q\,I_A.$$

Beide sind Geraden in $I_A$. Sie stimmen für jedes $I_A$ überein, wenn ihre Achsenabschnitte und ihre Steigungen gleich sind — das sind die beiden
Bedingungen. Die dritte Form folgt aus den beiden ersten.

**Gleich nur außen.** Äquivalent sind die beiden Ersatzschaltbilder nur an den Klemmen. Im Leerlauf fließt in der Spannungsquelle kein Strom, ihr
Innenwiderstand setzt nichts um; in der Stromquelle fließt dann der ganze Strom durch $G_q$ und setzt $I_q^2/G_q$ in Wärme um. Bei Kurzschluss ist es
umgekehrt. Die Ersatzschaltbilder beschreiben nur das Klemmenverhalten; die Verluste im Inneren einer echten Quelle lassen sich aus ihnen nicht ablesen.
:::

::::beispiel Dieselbe Quelle, zwei Bilder
Eine Spannungsquelle mit $12\,\text{V}$ und $2\,\Omega$ wird umgerechnet:

$$I_q = \frac{12\,\text{V}}{2\,\Omega} = 6\,\text{A}, \qquad G_q = \frac{1}{2\,\Omega} = 0{,}5\,\text{S}.$$

**Probe mit einer Last von 4 Ohm.** Spannungsquelle: Reihenschaltung. Stromquelle: Parallelschaltung von $G_q$ und Last.

$$I_A = \frac{12\,\text{V}}{6\,\Omega} = 2\,\text{A}, \qquad U_{AB} = \frac{6\,\text{A}}{0{,}5\,\text{S} + 0{,}25\,\text{S}} = 8\,\text{V}.$$

Beide liefern $2\,\text{A}$ bei $8\,\text{V}$ an die Last.

**Innen dagegen nicht.** Der Innenwiderstand setzt in der Spannungsquelle $(2\,\text{A})^2\cdot2\,\Omega$ um, im Innenleitwert der Stromquelle
$(8\,\text{V})^2\cdot0{,}5\,\text{S}$:

$$8\,\text{W} \qquad\text{gegen}\qquad 32\,\text{W}.$$

Im Leerlauf sind es $0$ gegen $72\,\text{W}$, bei Kurzschluss $72\,\text{W}$ gegen $0$.

**Im Bild:** Am Hahn sind Turm und Pumpe nicht zu unterscheiden. Hinter der Wand kostet beim Turm die enge Zuleitung Druck, bei der Pumpe das Leck
Wasser — und beides verschieden viel Energie.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/01-umwandlung · Vorlage: quellenumwandlung
Oben die beiden Ersatzschaltbilder nach Bild 7.21 des Skripts: links $U_q=12\,\text{V}$ mit $R_q=2\,\Omega$ in Reihe, rechts $I_q=6\,\text{A}$ mit
$G_q=0{,}5\,\text{S}$ parallel, beide mit den Klemmen A und B, dem Klemmenstrom $I_A$ aus A und der Klemmenspannung $U_{AB}$ nach unten; dazwischen ein
Doppelpfeil mit den Umrechnungsformeln. Unten das Kennlinienfeld $U_{AB}$ über $I_A$: Beide Quellen liegen auf derselben fallenden Geraden von $12\,\text{V}$
nach $6\,\text{A}$. Ein Lastregler verschiebt den Betriebspunkt; zwei Balken zeigen die Leistung im Inneren, die bei der einen Quelle mit dem Strom,
bei der anderen mit der Spannung wächst. Kernaussage: Reale Spannungs- und Stromquelle sind an den Klemmen gleich, innen nicht. (Rot = Quellen, blau =
Kennlinie und Betriebspunkt, orange = innere Leistung, grau = Klemmen und Leitungen.)
:::

## Quellen zusammenschalten

Oft braucht man mehr Spannung oder mehr Strom, als eine Quelle hergibt (Abschnitt 7.4.3 des Skripts). Dann schaltet man Quellen zusammen, und ob das
gutgeht, hängt von der Art ab.

- **Spannungsquellen in Reihe** sind unkritisch: Die Spannungen und die Innenwiderstände addieren sich, wie bei Batterien hintereinander im Gerät.
- **Stromquellen parallel** sind ebenso unkritisch: Die Ströme und die Innenleitwerte addieren sich.
- **Spannungsquellen parallel** sind nur sinnvoll, wenn ihre Innenwiderstände groß genug sind, um Ausgleichsströme zwischen ihnen zu begrenzen. Am
  einfachsten rechnet man sie in Stromquellen um, addiert und rechnet zurück.

Für zwei reale Spannungsquellen parallel ergibt sich so eine Ersatzquelle mit einem gewichteten Mittel der Spannungen und der Parallelschaltung der
Innenwiderstände; ohne Last fließt zwischen ihnen ein __Ausgleichsstrom__ (das Skript nennt in Bild 7.23 den Ausgangsstrom $I_\text{aus}$, daher hier
$I_\text{ausgl}$):

$$U_\text{ers} = \frac{U_{q1}/R_{q1} + U_{q2}/R_{q2}}{1/R_{q1} + 1/R_{q2}}, \qquad R_\text{ers} = R_{q1} \parallel R_{q2}, \qquad I_\text{ausgl} = \frac{U_{q1} - U_{q2}}{R_{q1} + R_{q2}}.$$

**So liest man das:** Die Ersatzspannung liegt zwischen den beiden Quellenspannungen, näher an der mit dem kleineren Innenwiderstand. Bei gleichen
Quellen ist sie die gemeinsame Spannung, der Innenwiderstand halbiert sich, und ein Ausgleichsstrom fließt nicht. Das ist der Fall im Skript mit zwei
Akkus von $1{,}2\,\text{V}$ und $10\,\Omega$: $5\,\Omega$ Innenwiderstand, $240\,\text{mA}$ Kurzschlussstrom. Seine Formel für die Ausgangsspannung ist dort
verdruckt, $U_a$ ist gleich $U_q-\frac{R}{2}\,I_a$, nicht $U_q-\frac{R}{2I_a}$; und die Gerade in Bild 7.24 scheint die Stromachse schon bei rund
$120\,\text{mA}$ zu schneiden, wo nach der Rechnung $240\,\text{mA}$ hingehören.

**Im Bild:** Zwei Wassertürme, durch Leitungen verbunden. Steht das Wasser in beiden gleich hoch, ruht es; steht es in einem höher, strömt es hinüber,
und nur die Leitungen bremsen.

:::herleitung
**Reihe von Spannungsquellen.** Durch beide fließt derselbe Strom; nach der Maschenregel addieren sich die Klemmenspannungen:

$$U_{AB} = (U_{q1} - R_{q1} I_A) + (U_{q2} - R_{q2} I_A) = (U_{q1} + U_{q2}) - (R_{q1} + R_{q2})\,I_A.$$

**Parallele Stromquellen.** An beiden liegt dieselbe Spannung; nach der Knotenregel addieren sich die Klemmenströme:

$$I_A = (I_{q1} - G_{q1} U_{AB}) + (I_{q2} - G_{q2} U_{AB}) = (I_{q1} + I_{q2}) - (G_{q1} + G_{q2})\,U_{AB}.$$

**Parallele Spannungsquellen.** Jede wird in eine Stromquelle mit $U_{q\nu}/R_{q\nu}$ und $1/R_{q\nu}$ umgerechnet; die Summe ist eine Stromquelle mit der Summe
der Ströme und der Summe der Leitwerte, und zurückgerechnet ist ihre Leerlaufspannung der Quotient, ihr Innenwiderstand der Kehrwert der Leitwertsumme.

**Ausgleichsstrom.** Ohne Last bilden die beiden Quellen allein eine Masche; nach der Maschenregel treibt der Spannungsunterschied den Strom durch beide
Innenwiderstände in Reihe.

**Ideale Quellen.** Zwei ideale Spannungsquellen verschiedener Spannung parallel verletzen die Maschenregel, zwei ideale Stromquellen verschiedenen Stroms in
Reihe die Knotenregel — solche Schaltungen gibt es nicht. Reale Quellen lösen den Widerspruch über ihre Innenwiderstände: Je kleiner diese bei
parallelen Spannungsquellen sind, desto größer der Ausgleichsstrom; bei Stromquellen in Reihe wachsen entsprechend die Spannungen an ihnen, je kleiner
die Innenleitwerte sind.
:::

::::beispiel Batterien in Reihe und parallel
**(a) In Reihe.** Vier Mignonzellen mit je $1{,}5\,\text{V}$ und $0{,}15\,\Omega$ in einem Gerät: zusammen eine Quelle mit

$$U_q = 4\cdot1{,}5\,\text{V} = 6\,\text{V}, \qquad R_q = 4\cdot0{,}15\,\Omega = 0{,}6\,\Omega.$$

**(b) Parallel, ungleich geladen.** Zwei Akkuzellen mit $1{,}30\,\text{V}$ und $1{,}25\,\text{V}$ und je $0{,}05\,\Omega$:

$$I_\text{ausgl} = \frac{1{,}30\,\text{V} - 1{,}25\,\text{V}}{0{,}1\,\Omega} = 0{,}5\,\text{A}, \qquad U_\text{ers} = 1{,}275\,\text{V}, \qquad R_\text{ers} = 25\,\text{m}\Omega.$$

Ohne angeschlossenes Gerät fließt ein halbes Ampere von der volleren in die leerere Zelle.

**(c) Zwei Autobatterien** mit $12{,}7\,\text{V}$ und $12{,}1\,\text{V}$ und je $10\,\text{m}\Omega$ Innenwiderstand, direkt parallel verbunden:

$$I_\text{ausgl} = \frac{0{,}6\,\text{V}}{20\,\text{m}\Omega} = 30\,\text{A}.$$

Genau das geschieht bei der Starthilfe, nur kommen die wenigen Milliohm der Kabel hinzu: Die volle Batterie lädt die leere, und den Strom begrenzen
allein Innenwiderstände und Kabel. Darum sind Starthilfekabel dick, und die letzte Klemme setzt man an blankes Metall des Motors, entfernt von der
Batterie — beim Anklemmen springt ein Funke über, und eine Batterie kann Knallgas abgeben.

**Im Bild:** Zwei Türme mit einem kleinen Höhenunterschied, aber sehr weiten Verbindungsleitungen: Es fließt viel hinüber.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/01-zusammenschaltung · Vorlage: quellen-zusammenschalten
Drei Felder. Links zwei reale Spannungsquellen in Reihe, je $U_q=1{,}5\,\text{V}$ mit $R_q=0{,}15\,\Omega$, Spannungspfeile gleichsinnig von Plus nach
Minus, daneben die Ersatzquelle mit $3\,\text{V}$ und $0{,}3\,\Omega$. In der Mitte zwei reale Stromquellen parallel, $I_{q1}=20\,\text{mA}$ mit
$G_{q1}=1\,\mu\text{S}$ und $I_{q2}=10\,\text{mA}$ mit $G_{q2}=2\,\mu\text{S}$, daneben die Ersatzquelle mit $30\,\text{mA}$ und $3\,\mu\text{S}$. Rechts zwei
reale Spannungsquellen parallel wie in Bild 7.23 des Skripts, $U_{q1}=1{,}30\,\text{V}$ und $U_{q2}$ mit je $0{,}05\,\Omega$, beide mit Plus oben, die
Klemmen offen; ein Regler verstellt $U_{q2}$, ein Strompfeil im Uhrzeigersinn (aufwärts durch Quelle 1, abwärts durch Quelle 2) zeigt den
Ausgleichsstrom $I_\text{ausgl}$, der bei gleichen Spannungen verschwindet und bei $U_{q2}=1{,}25\,\text{V}$ $0{,}5\,\text{A}$ erreicht; darunter die
Kennlinie der Ersatzquelle, deren Leerlaufspannung zwischen den beiden Quellenspannungen liegt. Ein zweiter Regler verkleinert die Innenwiderstände,
und der Ausgleichsstrom wächst über alle Grenzen. Kernaussage: Spannungsquellen in Reihe und Stromquellen parallel addieren sich, parallele
Spannungsquellen gleichen sich über ihre Innenwiderstände aus. (Rot = Quellen, blau = Klemmengrößen und Kennlinie, orange = Ausgleichsstrom, grau =
Leitungen.)
:::

## Bedeutung und Ausblick

Ideale Quellen sind Modelle, aber sehr brauchbare: Ein geregeltes Labornetzgerät hält die eingestellte Spannung fest wie eine ideale Spannungsquelle,
solange die Last weniger als den eingestellten Höchststrom zieht; würde sie mehr ziehen, hält es stattdessen diesen Strom fest und verhält sich wie eine
ideale Stromquelle — es schaltet selbst zwischen den beiden Betriebsarten um. Batterien und Generatoren sind reale Quellen, deren Kennlinie nur in einem
begrenzten Bereich eine Gerade ist; die Batteriespannung hängt zudem vom Ladezustand und von der Temperatur ab. Eine Solarzelle ist bei kleiner Spannung
fast eine Stromquelle, ihre Kennlinie knickt aber zu höheren Spannungen hin ab. Für solche __nichtlinearen__ Quellen gilt ein lineares Ersatzschaltbild
nur in der Nähe eines Betriebspunkts.

Der nächste Artikel verallgemeinert die Umwandlung: Jedes lineare Netz aus Quellen und Widerständen verhält sich von zwei Klemmen aus wie eine einzige
reale Spannungs- oder Stromquelle, die __Ersatzquelle__. Und der Innenwiderstand begrenzt, wie viel Leistung eine Quelle abgeben kann — das Thema der
Leistungsanpassung am Ende dieses Kapitels.

:::kern
- Eine __ideale Spannungsquelle__ hält ihre Spannung $U_q$ bei jedem Strom; kurzschließen darf man sie nicht.
- Eine __ideale Stromquelle__ hält ihren Strom $I_q$ bei jeder Spannung; offen lassen darf man sie nicht.
- __Reale Spannungsquelle__: $U_q$ mit $R_q$ in Reihe, Kennlinie $U_{AB}=U_q-R_qI_A$, Kurzschlussstrom $U_q/R_q$.
- __Reale Stromquelle__: $I_q$ mit $G_q$ parallel, Kennlinie $I_A=I_q-G_qU_{AB}$, Leerlaufspannung $I_q/G_q$.
- Den Innenwiderstand misst man als Betrag der Kennliniensteigung aus zwei Lastpunkten.
- __Umwandlung__: $I_q=\frac{U_q}{R_q}$ und derselbe Innenwiderstand — äquivalent an den Klemmen, nicht im Inneren.
- Spannungsquellen in Reihe und Stromquellen parallel addieren sich unproblematisch.
- Spannungsquellen parallel brauchen Innenwiderstände; sonst fließen große Ausgleichsströme.
:::

:::quiz
F: Was hält eine ideale Spannungsquelle fest, was eine ideale Stromquelle, und was bestimmt jeweils die andere Größe?
A: Die Spannungsquelle hält ihre Spannung $U_q$, der Strom ist $U_q/R$ und kommt von der Last; die Stromquelle hält ihren Strom $I_q$, die Spannung ist $R\,I_q$. An $5\,\text{V}$ fließen durch $1\,\Omega$ $5\,\text{A}$; $20\,\text{mA}$ erzeugen an $10\,\text{k}\Omega$ $200\,\text{V}$. Im Bild hält der Wasserturm den Druck, die Spritzenpumpe den Durchfluss.
F: Warum darf man eine ideale Spannungsquelle nicht kurzschließen und eine ideale Stromquelle nicht offen lassen?
A: Bei Kurzschluss müsste um den Kreis die Spannung $U_q$ abfallen, am widerstandslosen Draht fällt aber nichts ab — der Strom würde unendlich, die Maschenregel ist verletzt. Offen müsste der Strom der Stromquelle in einen Anschluss fließen, der nicht weiterführt — die Spannung würde unendlich, die Knotenregel ist verletzt.
F: Warum bricht eine Batterie unter Last ein, und wie bestimmt man ihren Innenwiderstand?
A: In ihr liegen Widerstände der Leiter und des chemischen Wegs, an denen der Strom Spannung kostet: $U_{AB}=U_q-R_qI_A$. Aus zwei Messpunkten ist $R_q=\frac{U_1-U_2}{I_2-I_1}$; bei der Autobatterie mit $12{,}70\,\text{V}$ im Leerlauf und $11{,}10\,\text{V}$ bei $200\,\text{A}$ sind das $8\,\text{m}\Omega$.
F: Wie verhält sich eine reale Stromquelle, und wo nutzt man das?
A: Ein Teil des Quellstroms fließt durch den parallelen Innenleitwert zurück, umso mehr, je höher die Spannung: $I_A=I_q-G_qU_{AB}$. Mit kleinem $G_q$ hängt der Klemmenstrom kaum von der Last ab; deshalb übertragen Sensoren Messwerte als Strom von $4$ bis $20\,\text{mA}$, bei dem zusätzliche Leitungswiderstände fast nichts ändern.
F: Unter welcher Bedingung sind eine reale Spannungs- und eine reale Stromquelle äquivalent, und warum?
A: Wenn $U_q=\frac{I_q}{G_q}$ und $R_q=\frac{1}{G_q}$ sind. Beide Kennlinien sind Geraden in $I_A$; sie stimmen überein, wenn Achsenabschnitt (Leerlaufspannung) und Steigung (Innenwiderstand) gleich sind. Eine Quelle mit $12\,\text{V}$ und $2\,\Omega$ entspricht $6\,\text{A}$ parallel zu $0{,}5\,\text{S}$.
F: In welchem Sinn sind umgerechnete Quellen nur „außen" gleich?
A: An den Klemmen liefern beide bei jeder Last dasselbe, im Inneren setzen sie verschiedene Leistung um. Im Leerlauf verliert die Spannungsquelle nichts, die Stromquelle aber $I_q^2/G_q$; an $4\,\Omega$ sind es bei $12\,\text{V}$ und $2\,\Omega$ $8\,\text{W}$ gegen $32\,\text{W}$. Die Verluste im Inneren einer echten Quelle lassen sich aus den Ersatzschaltbildern nicht ablesen.
F: Warum lassen sich ideale Quellen nicht ineinander umrechnen?
A: Für eine ideale Spannungsquelle mit $R_q$ gleich null wäre der Kurzschlussstrom $U_q/R_q$ unendlich, für eine ideale Stromquelle mit $G_q$ gleich null die Leerlaufspannung $I_q/G_q$. Die Umrechnung braucht einen endlichen Innenwiderstand.
F: Was ergibt die Reihenschaltung von Spannungsquellen und die Parallelschaltung von Stromquellen?
A: In Reihe fließt durch alle derselbe Strom, und nach der Maschenregel addieren sich Quellenspannungen und Innenwiderstände: vier Zellen mit $1{,}5\,\text{V}$ und $0{,}15\,\Omega$ ergeben $6\,\text{V}$ und $0{,}6\,\Omega$. Parallel liegt an allen dieselbe Spannung, und nach der Knotenregel addieren sich Quellströme und Innenleitwerte.
F: Was passiert, wenn man zwei Spannungsquellen verschiedener Spannung parallel schaltet?
A: Ohne Last bilden sie eine Masche, und der Unterschied treibt den Ausgleichsstrom $\frac{U_{q1}-U_{q2}}{R_{q1}+R_{q2}}$ durch beide Innenwiderstände. Bei zwei Akkuzellen mit $1{,}30$ und $1{,}25\,\text{V}$ und je $0{,}05\,\Omega$ sind das $0{,}5\,\text{A}$, bei zwei Autobatterien mit $0{,}6\,\text{V}$ Unterschied und je $10\,\text{m}\Omega$ schon $30\,\text{A}$. Bei idealen Quellen wäre der Strom unendlich.
F: Welche Fehler stehen im Skript bei den parallelen Akkus und den Kennlinien der Stromquelle?
A: Die Ausgangsspannung ist $U_a=U_q-\frac R2\,I_a$; im Skript steht $\frac{R}{2I_a}$, was nicht einmal die Einheit einer Spannung hat. Die Gerade in Bild 7.24 scheint die Stromachse schon bei etwa $120\,\text{mA}$ zu schneiden, nach der Rechnung gehört der Kurzschlussstrom von $240\,\text{mA}$ dorthin. Und die Unterschrift von Bild 7.19 nennt eine Spannungsquelle, gezeigt ist die Kennlinie der Stromquelle.
:::
