---
title: Laden und Entladen des Kondensators
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Kondensator
order: 40300
summary: Von Grund auf – wie schnell sich ein Kondensator über einen Widerstand lädt und entlädt. Leitbild ist die Gummimembran hinter einem engen Rohr: Anfangs strömt das Wasser kräftig, je voller die Kammer, desto schwächer. Mit dem Einschaltmoment und warum die Kondensatorspannung nicht springen kann, der sauber hergeleiteten Exponentialfunktion, der Zeitkonstante RC samt Tangente, Prozenttabelle und Halbwertszeit, dem Entladen mit Vorzeichen, der Energiebilanz – die Hälfte geht immer im Widerstand verloren – und dem Laden über eine Stromquelle. Mit Beispiel-Seite.
tags: RC-Glied, Ladevorgang, Entladevorgang, Zeitkonstante, e-Funktion, Differentialgleichung
---

## Anschaulich

In den beiden vorigen Artikeln war ein Kondensator eine Gummimembran in einem Wasserrohr. Bisher ging es nur um den Zustand vorher und nachher. Jetzt
geht es um den Weg dazwischen: Wie schnell füllt sich die Membrankammer, wenn das Wasser durch ein enges Rohr muss?

**Das Leitbild dieses Artikels:** **die Membran hinter einem engen Rohr**. Eine Pumpe hält einen festen Druck. Zwischen ihr und der Membran liegt ein
enges Rohr, das dem Wasser Widerstand entgegensetzt; wie viel hindurchfließt, hängt vom Druckunterschied über dem Rohr ab. Am Anfang ist die Membran
entspannt, der ganze Pumpendruck liegt am engen Rohr, und das Wasser strömt kräftig. Je weiter sich die Membran wölbt, desto stärker drückt sie zurück,
desto weniger Druck bleibt für das Rohr — der Strom wird schwächer.

Daraus folgt schon, ohne Formel, die Form des Vorgangs: Der Strom nimmt umso langsamer ab, je kleiner er schon ist, und die Membran nähert sich ihrer
Endwölbung immer langsamer, ohne sie je ganz zu erreichen. Genau das beschreibt eine Exponentialfunktion. Wie schnell das geht, legen zwei Dinge fest:
wie eng das Rohr ist und wie nachgiebig die Membran — elektrisch der Widerstand und die Kapazität.

:::grafik
Szene: get1/kondensator/03-membran-hinter-engem-rohr · Vorlage: rc-membran
Links eine Pumpe mit festem Druck, dann ein enges Rohrstück, dann die Membrankammer. Ein Startknopf öffnet das Ventil: Strömungspfeile im engen Rohr
sind anfangs dick und werden dünner, die Membran wölbt sich erst schnell, dann immer langsamer. Daneben laufen zwei Diagramme mit: der Strom fällt von
seinem Anfangswert ab, die Füllung steigt auf ihren Endwert zu. Darunter dasselbe elektrisch: Quelle $U_0$, Widerstand $R$, Kondensator $C$. Ein
Regler macht das Rohr enger bzw. die Membran nachgiebiger, und beide Kurven werden gleichermaßen gestreckt. Kernaussage: Weil der Strom vom
verbleibenden Druckunterschied abhängt, verläuft das Laden exponentiell, und Widerstand mal Kapazität bestimmt das Tempo. (Blau = Wasser und Strom,
rot = Membran und Kondensator, orange = Diagramme, grau = Rohre und Leitungen.)
:::

## Die Schaltung und der Einschaltmoment

Untersucht wird eine Reihenschaltung aus einem Widerstand $R$ und einem Kondensator $C$, ein __RC-Glied__. Ein Umschalter legt sie entweder an
eine Gleichspannungsquelle mit der Spannung $U_0$, Stellung 1, oder schließt sie über eine Leitung kurz, Stellung 2. Alle Zählpfeile zeigen in dieselbe
Richtung: der Strom $i(t)$ durch $R$ in den Kondensator, die Spannungen $u_R(t)$ am Widerstand und $u_C(t)$ am Kondensator in Stromrichtung. Kleine
Buchstaben stehen nach DIN für zeitabhängige Werte.

Zwei Gesetze bestimmen alles. Erstens addieren sich längs der geschlossenen Schleife die Spannungen; in Stellung 1 ist die Quellenspannung die Summe der
beiden anderen. Zweitens ist am Widerstand die Spannung proportional zum Strom, das __Ohmsche Gesetz__, das der Artikel über den
[ohmschen Widerstand](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/ohmscher-widerstand.html)
ausführlich behandelt. Mit der Gleichung des Kondensators aus dem Artikel [Der Kondensator und seine Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html):

$$U_0 = u_R(t)+u_C(t), \qquad u_R(t) = R\,i(t), \qquad i(t) = C\,\frac{du_C}{dt}.$$

**Im Bild:** Der Pumpendruck teilt sich auf das enge Rohr und die Membran auf. Durch das Rohr fließt umso mehr, je mehr Druck an ihm liegt, und die
Membran wölbt sich in dem Maß, in dem Wasser ankommt.

:::herleitung
**Die Schleife.** Im Artikel über Spannung war die Spannung eine Potenzialdifferenz, und längs einer Kette von Punkten addieren sich die
Teilspannungen. Der Kreis von der Quelle über $R$ und $C$ zurück zur Quelle beginnt und endet am selben Punkt; die Spannung der Quelle in Zählrichtung
ist deshalb die Summe der Spannungen an $R$ und $C$. Der Artikel über die
[Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html)
macht daraus die Maschenregel.

**Der Kondensator.** Ladung pro Zeit ist Strom, und die Ladung ist Kapazität mal Spannung; abgeleitet ergibt das die dritte Gleichung, wie im ersten
Artikel über den Kondensator.
:::

**Der Einschaltmoment.** Zu Beginn ist der Kondensator leer, der Schalter steht auf 2. Zur Zeit $t_0$ wird er auf 1 umgelegt; wir zählen die Zeit ab
diesem Moment, $t_0=0$. Die Spannung am Kondensator kann nicht springen: Sie ist im ersten Augenblick noch null. Die ganze Quellenspannung liegt am
Widerstand, und es fließt der größtmögliche Strom:

:::formel
$$u_C(0) = 0, \qquad u_R(0) = U_0, \qquad i(0) = \frac{U_0}{R}.$$
:::

**So liest man das:** Im Einschaltmoment wirkt ein ungeladener Kondensator wie ein __Kurzschluss__ — als wäre an seiner Stelle ein Draht. Ist er
dagegen voll geladen, fließt kein Strom mehr, und er wirkt wie __offene Klemmen__.

**Im Bild:** Die entspannte Membran drückt noch nicht zurück; der ganze Pumpendruck treibt das Wasser durch das enge Rohr.

:::herleitung
**Warum die Spannung nicht springt.** Nach der Kondensatorgleichung ist der Strom Kapazität mal Änderungsrate der Spannung. Ein Sprung der Spannung in
der Zeit null hätte eine unendliche Änderungsrate und damit einen unendlichen Strom. Den lässt der Widerstand nicht zu: Der Strom ist höchstens
Quellenspannung durch Widerstand. Also ändert sich die Kondensatorspannung stetig und startet bei ihrem alten Wert, null.

**Der Rest.** Ist die Kondensatorspannung null, liegt nach der Schleifengleichung die ganze Quellenspannung am Widerstand, und das Ohmsche Gesetz gibt
den Strom.
:::

::::beispiel Der Einschaltmoment in Zahlen
Ein leerer Kondensator von $470\,\mu\text{F}$ wird über $1\,\text{k}\Omega$ an $12\,\text{V}$ gelegt. Im ersten Augenblick:

$$u_C(0) = 0\,\text{V}, \qquad u_R(0) = 12\,\text{V}, \qquad i(0) = \frac{12\,\text{V}}{1\,\text{k}\Omega} = 12\,\text{mA}.$$

Die Kapazität spielt dabei keine Rolle — sie entscheidet erst, wie lange der Strom so groß bleibt. Ohne Widerstand wäre der Einschaltstrom nur durch die
Zuleitungen und den Innenwiderstand der Quelle begrenzt und entsprechend riesig.

**Im Bild:** Im ersten Moment ist die Membran noch gar nicht gespannt; wie viel Wasser fließt, bestimmt allein das enge Rohr.
::::

## Der Aufladevorgang

Danach nimmt der Strom ab, denn mit jeder Ladung wächst die Spannung am Kondensator, und für den Widerstand bleibt weniger. Löst man die Gleichungen, so
ergibt sich mit der __Zeitkonstante__ $\tau=R\,C$:

:::formel Satz
$$i(t) = \frac{U_0}{R}\,\mathrm{e}^{-t/\tau}, \qquad u_C(t) = U_0\,\big(1-\mathrm{e}^{-t/\tau}\big), \qquad u_R(t) = U_0\,\mathrm{e}^{-t/\tau}.$$
:::

**So liest man das:** Der Strom fällt von $\frac{U_0}{R}$ exponentiell auf null, die Kondensatorspannung steigt von null exponentiell auf $U_0$, und die
Widerstandsspannung fällt wie der Strom. Das aufrechte $\mathrm{e}$ ist die Eulersche Zahl $2{,}718\ldots$. Zu jeder Zeit addieren sich die beiden
Spannungen zu $U_0$.

**Im Bild:** Das Wasser strömt erst kräftig, dann immer schwächer durch das enge Rohr, und die Membran wölbt sich ihrer Endstellung entgegen.

:::herleitung
**Schritt 1: eine Gleichung für den Strom.** Man setzt die Kondensatorspannung als Integral des Stroms ein und leitet die Schleifengleichung nach
der Zeit ab; die konstante Quellenspannung fällt dabei weg:

$$U_0 = R\,i(t)+u_C(t), \qquad 0 = R\,\frac{di}{dt}+\frac{1}{C}\,i(t).$$

**Schritt 2: Trennen.** Der Strom ändert sich mit einer Rate, die proportional zu ihm selbst ist. Man bringt alles mit $i$ auf eine Seite und
integriert von $0$ bis $t$, mit Integrationsvariablen in Strich-Schreibweise:

$$\int_{i(0)}^{i(t)}\frac{di'}{i'} = -\int_0^t\frac{dt'}{R\,C}, \qquad \ln\frac{i(t)}{i(0)} = -\frac{t}{R\,C}.$$

Falsch wäre der Logarithmus des Stroms selbst: Ein Logarithmus braucht eine reine Zahl, deshalb steht hier das Verhältnis zum Anfangswert.

**Schritt 3: der Anfangswert.** Mit $i(0)=\frac{U_0}{R}$ aus dem Einschaltmoment und der Exponentialfunktion als Umkehrung des Logarithmus folgt der
Strom. Die Widerstandsspannung ist $R$ mal Strom, die Kondensatorspannung der Rest bis $U_0$.

**Im Bild:** Weil das Wasser im engen Rohr vom verbleibenden Druckunterschied getrieben wird und genau dieser Unterschied durch das ankommende Wasser
schrumpft, schrumpft er in jedem gleich langen Zeitabschnitt um denselben Bruchteil — das ist die Eigenschaft der Exponentialfunktion.
:::

::::beispiel Aufladen in Zahlen
Mit $470\,\mu\text{F}$, $1\,\text{k}\Omega$ und $12\,\text{V}$ ist die Zeitkonstante

$$\tau = 1\,\text{k}\Omega\cdot470\,\mu\text{F} = 0{,}47\,\text{s}.$$

Nach einer Zeitkonstante und nach drei:

| Zeit | $\mathrm{e}^{-t/\tau}$ | Strom $i$ | Spannung $u_C$ |
|---|---|---|---|
| $0$ | $1$ | $12\,\text{mA}$ | $0\,\text{V}$ |
| $\tau$, also $0{,}47\,\text{s}$ | $0{,}368$ | $4{,}4\,\text{mA}$ | $7{,}6\,\text{V}$ |
| $3\tau$, also $1{,}41\,\text{s}$ | $0{,}050$ | $0{,}60\,\text{mA}$ | $11{,}4\,\text{V}$ |

In jeder Zeile ergeben $R\,i$ und $u_C$ zusammen $12\,\text{V}$.

**Im Bild:** Nach knapp einer halben Sekunde ist die Membran zu fast zwei Dritteln gewölbt, nach anderthalb Sekunden fast ganz. Das enge Rohr lässt dann
nur noch ein Rinnsal durch.
::::

## Die Zeitkonstante

Die Zeitkonstante ist das Zeitmaß des ganzen Vorgangs:

:::formel Definition
$$\tau = R\cdot C.$$
:::

**So liest man das:** Ohm mal Farad ist eine Sekunde, wie im Artikel über Einheiten. In jeder Zeitkonstante schrumpft der Strom auf den Bruchteil
$\frac{1}{\mathrm{e}}$, rund $36{,}8\,\%$, und die Kondensatorspannung rückt ihrem Endwert um denselben Bruchteil des verbleibenden Abstands näher. Laden
und Entladen gehen schneller bei kleinerem Widerstand und kleinerer Kapazität. Wie weit die Ladung nach einigen Zeitkonstanten ist:

| Zeit | erreichter Anteil der Endspannung |
|---|---|
| $1\,\tau$ | $63{,}2\,\%$ |
| $2\,\tau$ | $86{,}5\,\%$ |
| $3\,\tau$ | $95{,}0\,\%$ |
| $4\,\tau$ | $98{,}2\,\%$ |
| $5\,\tau$ | $99{,}3\,\%$ |

Als Faustregel gilt der Vorgang nach fünf Zeitkonstanten als abgeschlossen. Gerundet merkt man sich $63$, $86$, $95$, $98$ und $99\,\%$.

**Im Bild:** Ein engeres Rohr lässt das Wasser langsamer nachfließen, eine nachgiebigere Membran braucht mehr Wasser bis zum Gegendruck. Beides streckt
den Vorgang im selben Maß.

:::herleitung
**Die Tabelle.** Nach $n$ Zeitkonstanten ist der Exponent $-n$, der erreichte Anteil also $1-\mathrm{e}^{-n}$: für $n=1$ bis $5$ die Werte $0{,}632$,
$0{,}865$, $0{,}950$, $0{,}982$ und $0{,}993$.

**Derselbe Bruchteil in jeder Zeitkonstante.** Nach den Potenzgesetzen ist

$$\mathrm{e}^{-(t+\tau)/\tau} = \mathrm{e}^{-t/\tau}\cdot\mathrm{e}^{-1}.$$

Gleichgültig, wo man startet: Eine Zeitkonstante später ist der Strom — und ebenso der Abstand der Spannung zum Endwert — auf das $\frac{1}{\mathrm{e}}$-Fache
geschrumpft.
:::

**Die Anfangstangente.** Zu Beginn steigt die Kondensatorspannung mit der Steigung $\frac{U_0}{\tau}$. Würde der Anfangsstrom unverändert weiterfließen,
wäre der Kondensator nach genau einer Zeitkonstante voll. So liest man $\tau$ an einer gemessenen Kurve ab: Die Tangente im Startpunkt schneidet die
Endspannung bei $t=\tau$. Die halbe Endspannung ist nach der __Halbwertszeit__ erreicht:

$$t_{1/2} = \tau\,\ln2 \approx 0{,}69\,\tau.$$

**Im Bild:** Hielte die Pumpe den anfänglichen Wasserstrom aufrecht, wäre die Membran nach einer Zeitkonstante gespannt. Weil der Strom aber nachlässt,
dauert es in Wirklichkeit unendlich lange — und nach einer Zeitkonstante sind erst knapp zwei Drittel erreicht.

:::herleitung
**Die Steigung.** Nach der Kondensatorgleichung ist die Änderungsrate der Spannung Strom durch Kapazität, im Startpunkt also

$$\frac{du_C}{dt}(0) = \frac{i(0)}{C} = \frac{U_0}{R\,C} = \frac{U_0}{\tau}.$$

Eine Gerade mit dieser Steigung erreicht $U_0$ nach der Zeit $\tau$.

**Die Halbwertszeit.** Die Spannung ist halb so groß wie $U_0$, wenn $\mathrm{e}^{-t/\tau}$ gleich $\frac12$ ist; mit dem natürlichen Logarithmus folgt
die Formel.
:::

::::beispiel Die Zeitkonstante ablesen
Ein RC-Glied aus $10\,\text{k}\Omega$ und $100\,\mu\text{F}$:

$$\tau = 10^{4}\,\Omega\cdot10^{-4}\,\text{F} = 1\,\text{s}, \qquad t_{1/2} = 0{,}69\,\text{s}.$$

Nach $5\,\text{s}$ sind $99{,}3\,\%$ erreicht. Für $99{,}9\,\%$ muss der Restanteil auf ein Tausendstel fallen:

$$\mathrm{e}^{-t/\tau} = 10^{-3}, \qquad t = \tau\,\ln1000 \approx 6{,}9\,\text{s}.$$

Mit einem Zehntel des Widerstands ginge alles zehnmal so schnell.

**Im Bild:** Die letzten Promille dauern am längsten — das enge Rohr lässt am Ende nur noch Tropfen durch.
::::

## Der Entladevorgang

Ist der Kondensator auf $U_0$ geladen und legt man zur Zeit null den Schalter von 1 auf 2, liegt keine Quelle mehr in der Schleife; die Spannungen an $R$
und $C$ addieren sich zu null. Die Kondensatorspannung startet bei $U_0$, denn sie kann nicht springen. Am Widerstand liegt deshalb $-U_0$, und der Strom
fließt gegen die Zählrichtung:

:::formel Satz
$$u_C(t) = U_0\,\mathrm{e}^{-t/\tau}, \qquad i(t) = -\frac{U_0}{R}\,\mathrm{e}^{-t/\tau}, \qquad u_R(t) = -U_0\,\mathrm{e}^{-t/\tau}.$$
:::

**So liest man das:** Die Spannung fällt von $U_0$ exponentiell auf null, mit derselben Zeitkonstante wie beim Laden. Das Minuszeichen beim Strom heißt:
Er fließt jetzt aus dem Kondensator heraus, entgegen dem Zählpfeil, der für das Laden gewählt war. Nach einer Zeitkonstante sind noch $36{,}8\,\%$ der
Spannung übrig.

**Im Bild:** Die gespannte Membran drückt das Wasser durch das enge Rohr zurück, erst kräftig, dann immer schwächer.

:::herleitung
In Stellung 2 gilt für die Schleife ohne Quelle

$$R\,i(t)+u_C(t) = 0, \qquad R\,C\,\frac{du_C}{dt} = -u_C(t).$$

Die Änderungsrate der Spannung ist proportional zu ihr selbst, mit dem Faktor $-\frac1\tau$. Trennt und integriert man wie beim Laden, folgt

$$\ln\frac{u_C(t)}{u_C(0)} = -\frac{t}{\tau}, \qquad u_C(t) = U_0\,\mathrm{e}^{-t/\tau}.$$

Der Strom ist $C$ mal die Ableitung, und die Ableitung von $\mathrm{e}^{-t/\tau}$ ist $-\frac1\tau\,\mathrm{e}^{-t/\tau}$; mit $C/\tau=1/R$ folgt $i(t)$, und
die Widerstandsspannung ist $R$ mal Strom.
:::

::::beispiel Ein Entladewiderstand
Ein Kondensator von $100\,\mu\text{F}$ in einem Netzteil ist auf $400\,\text{V}$ geladen. Ein Widerstand von $100\,\text{k}\Omega$ parallel zu ihm soll ihn
nach dem Abschalten auf eine ungefährliche Spannung entladen, hier $60\,\text{V}$:

$$\tau = 10^{5}\,\Omega\cdot10^{-4}\,\text{F} = 10\,\text{s}, \qquad t = \tau\,\ln\frac{400\,\text{V}}{60\,\text{V}} \approx 10\,\text{s}\cdot1{,}90 = 19\,\text{s}.$$

Der Strom beginnt bei $-4\,\text{mA}$. Nach fünf Zeitkonstanten, $50\,\text{s}$, sind noch etwa $2{,}7\,\text{V}$ übrig.

**Im Bild:** Ein enges Rückflussrohr entspannt die Membran langsam und gefahrlos; ein weites würde sie schlagartig entladen.
::::

## Die Energiebilanz

Beim Laden liefert die Quelle die Ladung $C\,U_0$ bei der festen Spannung $U_0$. Im Kondensator steckt danach aber nur die Hälfte der gelieferten Energie;
die andere Hälfte hat der Widerstand in Wärme umgesetzt:

$$W_\text{Quelle} = C\,U_0^2, \qquad W_C = \frac12\,C\,U_0^2, \qquad W_R = \frac12\,C\,U_0^2.$$

**So liest man das:** Das gilt für jeden Widerstand. Ein kleiner lässt einen großen Strom kurz fließen, ein großer einen kleinen lange — die Wärme ist
dieselbe. Beim Entladen wird die gespeicherte Hälfte im Widerstand zu Wärme. Das ist dieselbe Unabhängigkeit vom Widerstand wie beim Umladen zweier
Kondensatoren im vorigen Artikel.

**Im Bild:** Durch ein enges Rohr fließt das Wasser langsam, dafür lange, durch ein weites schnell, dafür kurz. Die Reibungsverluste sind am Ende gleich.

:::herleitung
Leistung ist Spannung mal Strom, wie im Artikel über Einheiten; Energie ist Leistung mal Zeit, aufsummiert.

**Die Quelle** liefert bei fester Spannung die gesamte geflossene Ladung $C\,U_0$:

$$W_\text{Quelle} = \int_0^\infty U_0\,i(t)\;dt = U_0\cdot C\,U_0.$$

**Der Widerstand** setzt die Leistung $u_R\,i$, also $R\,i^2$, um:

$$W_R = \int_0^\infty R\,\frac{U_0^2}{R^2}\,\mathrm{e}^{-2t/\tau}\;dt = \frac{U_0^2}{R}\cdot\frac{\tau}{2} = \frac12\,C\,U_0^2.$$

Der Widerstand kürzt sich weg, weil die Zeitkonstante mit ihm wächst. Der Kondensator speichert nach dem vorigen Artikel $\frac12CU_0^2$; die Summe stimmt.
:::

::::beispiel Energie beim Laden
Der Kondensator von $470\,\mu\text{F}$ an $12\,\text{V}$:

$$W_\text{Quelle} = 470\,\mu\text{F}\cdot(12\,\text{V})^2 \approx 67{,}7\,\text{mJ}, \qquad W_C = W_R \approx 33{,}8\,\text{mJ}.$$

Mit $10\,\Omega$ ist er nach einer Zeitkonstante von $4{,}7\,\text{ms}$ fast voll, der Anfangsstrom $1{,}2\,\text{A}$; mit $10\,\text{k}\Omega$ dauert es
$4{,}7\,\text{s}$ bei $1{,}2\,\text{mA}$. In beiden Fällen werden $33{,}8\,\text{mJ}$ zu Wärme.

**Im Bild:** Weites oder enges Rohr — der Verlust beim Füllen ist derselbe, nur das Tempo ändert sich.
::::

## Laden über eine Stromquelle

Zum Vergleich eine __Stromquelle__: Sie hält den Strom $I$ fest, gleichgültig, welche Spannung dafür nötig ist. Lädt sie einen leeren
Kondensator über einen Widerstand, verläuft der Vorgang ganz anders:

$$u_R(t) = R\,I, \qquad u_C(t) = \frac{I\,t}{C}.$$

**So liest man das:** Am Widerstand liegt eine feste Spannung, und die Kondensatorspannung steigt linear, ohne sich einem Endwert zu nähern — bis die
Stromquelle die nötige Spannung nicht mehr aufbringen kann. Mit einer Spannungsquelle dagegen sinkt der Strom, je voller der Kondensator wird.

**Im Bild:** Eine Pumpe, die eine feste Wassermenge pro Sekunde fördert, wölbt die Membran gleichmäßig weiter. Das enge Rohr kostet dabei einen festen
Druck.

:::herleitung
Der Strom ist konstant, also ist nach dem Ohmschen Gesetz auch die Widerstandsspannung konstant. Der Kondensator nimmt in der Zeit $t$ die Ladung $I\,t$
auf, und seine Spannung ist Ladung durch Kapazität.
:::

::::beispiel Eine Stromquelle lädt
Eine Stromquelle von $1\,\text{mA}$ lädt über $2\,\text{k}\Omega$ einen leeren Kondensator von $10\,\mu\text{F}$:

$$u_R = 2\,\text{k}\Omega\cdot1\,\text{mA} = 2\,\text{V}, \qquad \frac{du_C}{dt} = \frac{1\,\text{mA}}{10\,\mu\text{F}} = 100\,\frac{\text{V}}{\text{s}}.$$

Nach $50\,\text{ms}$ hat der Kondensator $5\,\text{V}$, und die Stromquelle muss $7\,\text{V}$ aufbringen; nach $100\,\text{ms}$ wären es schon $12\,\text{V}$.

**Im Bild:** Die Pumpe fördert stur dieselbe Menge. Ihr Druck muss mit der Wölbung der Membran mitwachsen.
::::

:::grafik
Szene: get1/kondensator/03-laden-entladen-kurven · Vorlage: rc-verlaeufe
Oben das Schaltbild: links die Quelle $U_0$ mit Spannungspfeil nach unten, oben ein Umschalter mit den Stellungen 1 (zur Quelle) und 2 (zur
rechten Rückleitung), darunter in Reihe $R$ mit dem Pfeil $u_R(t)$ und $C$ mit dem Pfeil $u_C(t)$, beide nach unten, und der Strompfeil $i(t)$ nach unten.
Darunter zwei Diagramme über der Zeit in Vielfachen von $\tau$: links Laden mit $u_C$ von $0$ auf $U_0$, dazu die Anfangstangente, die $U_0$ bei $\tau$
erreicht, und Markierungen bei $63$, $86$, $95\,\%$; rechts Entladen mit $u_C$ von $U_0$ auf $0$ und dem negativen Strom. Ein Schalterknopf wechselt
zwischen Laden und Entladen, ein Regler ändert $R$ und $C$. Kernaussage: Laden und Entladen verlaufen exponentiell mit derselben Zeitkonstante $R\,C$.
(Rot = Kondensatorspannung, blau = Strom, orange = Tangente und Markierungen, grau = Achsen und Schaltung.)
:::

## Bedeutung und Ausblick

RC-Glieder sind die einfachsten Zeitgeber der Elektronik. Sie verzögern Signale, entprellen Taster, bestimmen in Oszillatoren den Takt und begrenzen in
Digitalschaltungen, wie schnell eine Leitung umgeladen werden kann. Als Filter lassen sie langsame Änderungen durch und dämpfen schnelle — ein Thema der
Wechselstromtechnik. Auch die Selbstentladung aus dem Artikel [Der Kondensator und seine Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html) ist ein solcher Entladevorgang, über den Isolationswiderstand mit der
Zeitkonstante $R_\text{I}C$.

Ohmsches Gesetz und Maschenregel, die hier schon benutzt wurden, führen die folgenden Artikel von Grund auf ein, beginnend mit
[Der elektrische Strom](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/elektrischer-strom.html):
Was ist Strom, was ist ein Widerstand, und wie verteilen sich Ströme und Spannungen in einem Netz?

:::kern
- Ein __RC-Glied__ lädt und entlädt sich exponentiell, weil der Strom vom verbleibenden Spannungsunterschied abhängt.
- Die Kondensatorspannung kann nicht springen: Im Einschaltmoment wirkt ein leerer Kondensator wie ein Kurzschluss, $i(0)=\frac{U_0}{R}$.
- Ein geladener Kondensator sperrt Gleichstrom und wirkt wie offene Klemmen.
- Laden: $u_C(t)=U_0\,(1-\mathrm{e}^{-t/\tau})$; Strom und Widerstandsspannung fallen wie $\mathrm{e}^{-t/\tau}$.
- Die __Zeitkonstante__ $\tau=R\,C$ ist das Zeitmaß: nach einer $63\,\%$, nach drei $95\,\%$, nach fünf über $99\,\%$.
- Die Anfangstangente erreicht den Endwert nach genau einer Zeitkonstante; die halbe Spannung ist nach $\tau\ln2$ erreicht.
- Entladen: $u_C(t)=U_0\,\mathrm{e}^{-t/\tau}$; der Strom fließt gegen die Zählrichtung des Ladens.
- Beim Laden über einen Widerstand geht die Hälfte der gelieferten Energie verloren, unabhängig von seiner Größe.
- Mit einer Stromquelle steigt die Kondensatorspannung linear: $u_C=\frac{I\,t}{C}$.
:::

:::quiz
F: Warum verläuft das Laden über einen Widerstand exponentiell und nicht linear?
A: Der Strom durch den Widerstand ist proportional zur Spannung an ihm, und die ist der Rest der Quellenspannung, den der Kondensator noch nicht übernommen hat. Mit jeder Ladung wächst die Kondensatorspannung, der Rest schrumpft, und damit schrumpft der Strom — in jedem gleich langen Zeitabschnitt um denselben Bruchteil. Eine Größe, deren Änderungsrate proportional zu ihr selbst ist, verläuft exponentiell.
F: Warum wirkt ein leerer Kondensator im Einschaltmoment wie ein Kurzschluss, und welcher Strom fließt über $1\,\text{k}\Omega$ an $12\,\text{V}$?
A: Seine Spannung kann nicht springen, denn ein Sprung bräuchte einen unendlichen Strom, und den begrenzt der Widerstand. Im ersten Augenblick ist sie also noch null, die ganze Quellenspannung liegt am Widerstand, und es fließt $\frac{U_0}{R}$, hier $12\,\text{mA}$ — als wäre der Kondensator ein Draht.
F: Wie folgt die Exponentialfunktion aus den Gleichungen der Schaltung, und warum steht im Logarithmus ein Verhältnis?
A: Die Schleifengleichung $U_0=R\,i+u_C$ wird nach der Zeit abgeleitet; mit $\frac{du_C}{dt}=\frac iC$ entsteht $0=R\frac{di}{dt}+\frac iC$. Getrennt und von $0$ bis $t$ integriert, ergibt sich $\ln\frac{i(t)}{i(0)}=-\frac{t}{RC}$, also $i=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$. Ein Logarithmus braucht eine reine Zahl; deshalb steht darin das Verhältnis zum Anfangswert und nicht der Strom selbst.
F: Was bedeutet die Zeitkonstante, und welche Werte ergeben sich mit $470\,\mu\text{F}$ und $1\,\text{k}\Omega$ an $12\,\text{V}$?
A: $\tau=RC$ ist das Zeitmaß des Vorgangs; in jeder Zeitkonstante fällt der Strom auf den Bruchteil $\frac1{\mathrm e}$. Hier ist $\tau=0{,}47\,\text{s}$; nach einer Zeitkonstante fließen $4{,}4\,\text{mA}$ bei $7{,}6\,\text{V}$ am Kondensator, nach drei $0{,}60\,\text{mA}$ bei $11{,}4\,\text{V}$.
F: Woher kommen die Prozentwerte $63$, $86$, $95$, $98$ und $99$, und was zeigt die Anfangstangente?
A: Nach $n$ Zeitkonstanten ist der erreichte Anteil $1-\mathrm{e}^{-n}$, also $63{,}2$, $86{,}5$, $95{,}0$, $98{,}2$ und $99{,}3\,\%$. Die Anfangssteigung der Spannung ist $\frac{U_0}{\tau}$: Würde der Anfangsstrom weiterfließen, wäre der Kondensator nach genau einer Zeitkonstante voll. So liest man $\tau$ an einer gemessenen Kurve ab.
F: Wie lange dauert es bei $\tau=1\,\text{s}$ bis zur halben Spannung und bis $99{,}9\,\%$?
A: Die halbe Spannung ist erreicht, wenn $\mathrm{e}^{-t/\tau}=\frac12$, also nach $\tau\ln2\approx0{,}69\,\text{s}$. Für $99{,}9\,\%$ muss der Rest auf ein Tausendstel fallen, $t=\tau\ln1000\approx6{,}9\,\text{s}$ — die letzten Promille dauern am längsten.
F: Wie verläuft das Entladen, und warum ist der Strom negativ?
A: Ohne Quelle addieren sich die Spannungen an $R$ und $C$ zu null; die Spannung startet bei $U_0$ und fällt wie $U_0\mathrm{e}^{-t/\tau}$. Der Strom ist $C$ mal ihre Ableitung, $-\frac{U_0}{R}\mathrm{e}^{-t/\tau}$: Er fließt aus dem Kondensator heraus, entgegen dem Zählpfeil des Ladens. Am Widerstand liegt deshalb anfangs $-U_0$.
F: Wie lange braucht ein Entladewiderstand von $100\,\text{k}\Omega$, um $100\,\mu\text{F}$ von $400\,\text{V}$ auf $60\,\text{V}$ zu bringen?
A: Die Zeitkonstante ist $10\,\text{s}$, und die Spannung fällt wie $\mathrm{e}^{-t/\tau}$. Aus $\frac{60}{400}=\mathrm{e}^{-t/\tau}$ folgt $t=\tau\ln\frac{400}{60}\approx19\,\text{s}$. Der Strom beginnt bei $-4\,\text{mA}$, und nach fünf Zeitkonstanten sind noch etwa $2{,}7\,\text{V}$ übrig.
F: Warum geht beim Laden über einen Widerstand immer die Hälfte der Energie verloren, gleich wie groß der Widerstand ist?
A: Die Quelle liefert die Ladung $CU_0$ bei der Spannung $U_0$, also $CU_0^2$; der Kondensator speichert $\frac12CU_0^2$. Der Widerstand setzt $\int Ri^2\,dt=\frac{U_0^2}{R}\cdot\frac\tau2=\frac12CU_0^2$ um — der Widerstand kürzt sich, weil die Zeitkonstante mit ihm wächst. Bei $470\,\mu\text{F}$ und $12\,\text{V}$ sind das $33{,}8\,\text{mJ}$, ob mit $10\,\Omega$ in Millisekunden oder mit $10\,\text{k}\Omega$ in Sekunden.
F: Was ändert sich beim Laden über eine Stromquelle?
A: Der Strom bleibt fest, also liegt am Widerstand die feste Spannung $RI$, und die Kondensatorspannung steigt linear, $u_C=\frac{It}{C}$, ohne sich einem Endwert zu nähern. Bei $1\,\text{mA}$ in $10\,\mu\text{F}$ sind das $100\,\frac{\text{V}}{\text{s}}$; über $2\,\text{k}\Omega$ muss die Quelle nach $50\,\text{ms}$ schon $7\,\text{V}$ aufbringen.
:::
