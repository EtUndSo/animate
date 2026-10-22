---
title: Arbeit, Potenzial und Spannung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Elektrische Feldstärke und Potenzial
order: 30200
summary: Von Grund auf – was es kostet, eine Ladung im Feld zu verschieben, und warum daraus eine Höhe wird. Leitbild ist eine Wanderkarte mit Höhenlinien: Das Potenzial ist die Höhe, das Feld das Gefälle, die Spannung der Höhenunterschied, und auf jedem Rundweg kommt man auf derselben Höhe an. Mit der Arbeit als Wegintegral, der echten Begründung der Wegunabhängigkeit, dem Potenzial einer Punktladung, der Spannung und ihrem Vorzeichen, U = E·d im Plattenkondensator, dem Elektronenvolt, Bezugspotenzial und Masse sowie Äquipotentialflächen. Mit Beispiel-Seite.
tags: Arbeit, Energie, Potenzial, Spannung, Potenzialdifferenz, Volt, Äquipotentialfläche
---

## Anschaulich

Im vorigen Artikel war das Schwerefeld das Vorbild für das elektrische Feld. Jetzt kommt die Energie dazu. Wer einen Rucksack auf
einen Berg trägt, steckt Arbeit hinein; beim Abstieg bekommt er sie zurück. Wie viel, hängt nur vom Höhenunterschied ab — nicht davon,
ob man den steilen Pfad nimmt oder die Serpentinen.

**Das Leitbild dieses Artikels:** eine **Wanderkarte mit Höhenlinien**. Für Ladungen im elektrischen Feld gibt es dieselbe Karte. Jeder
Punkt hat eine „Höhe", das __Potenzial__. Das Feld ist das Gefälle: Es zeigt bergab, und eine positive Ladung rollt wie eine Kugel in
seine Richtung. Der Höhenunterschied zwischen zwei Punkten ist die __Spannung__.

Drei Dinge folgen daraus, bevor man eine Formel schreibt. Wer eine Runde läuft und zum Start zurückkehrt, ist wieder auf derselben
Höhe — auf einem Rundweg verrichtet das Feld insgesamt keine Arbeit. Längs einer Höhenlinie kostet das Gehen keine Hubarbeit. Und die
Höhe selbst ist Vereinbarung, „über Normalnull"; wirklich zählt nur der Unterschied.

:::grafik
Szene: get1/elektrische-feldstaerke-und-potenzial/02-wanderkarte · Vorlage: potenzial-landschaft
Eine Landschaft mit Höhenlinien in der Draufsicht, daneben dieselbe Landschaft schräg von der Seite als Gelände. Pfeile zeigen in jedem
Punkt bergab, senkrecht zu den Höhenlinien. Zwei Punkte A und B sind durch zwei verschiedene Wege verbunden, einen steilen und einen
in Serpentinen; zwei Zähler zeigen für beide Wege denselben Höhenunterschied. Ein dritter Weg ist ein Rundweg, sein Zähler zeigt null.
Kernaussage: Potenzial ist Höhe, Feld ist Gefälle, Spannung ist Höhenunterschied, und der hängt nicht vom Weg ab. (Blau =
Höhenlinien und Gefällepfeile, rot = die Punkte A und B, orange = Wege und Zähler, grau = Gelände.)
:::

## Arbeit im elektrischen Feld

Wie in der Mechanik ist Arbeit Kraft mal Weg. Auf eine Ladung $Q$ im Feld $\vec E$ wirkt die Kraft $Q\,\vec E$. In einem __homogenen__
Feld, überall gleich groß und gleich gerichtet, verrichtet das Feld an der Ladung deshalb auf einem geraden Wegstück $\Delta\vec s$ die
Arbeit

$$\Delta W = Q\,\vec E\cdot\Delta\vec s = Q\,E\,\Delta s\,\cos\alpha,$$

mit dem Winkel $\alpha$ zwischen Feld und Weg. Allgemein — Feld veränderlich, Weg gekrümmt — summiert man über kleine Wegstücke, und es
entsteht das Wegintegral aus dem Artikel über Größen und Einheiten. Bewegt sich die Ladung vom Punkt $P_1$ zum Punkt $P_2$, verrichtet
das Feld die Arbeit

:::formel
$$W_{12} = Q\int_{P_1}^{P_2}\vec E\cdot d\vec s.$$
:::

**So liest man das:** $W_{12}$ ist die Arbeit, die das Feld verrichtet, die Energie, die es dabei „freisetzt". Ist sie positiv, gewinnt
die Ladung Bewegungsenergie oder gibt sie an ihre Umgebung ab. Ist sie negativ, muss man die Ladung gegen das Feld schieben und die
Energie $-W_{12}$ selbst aufbringen. Es zählt nur der Anteil des Wegs längs des Felds, quer dazu nichts.

**Im Bild:** Eine positive Ladung, die mit dem Feld läuft, geht bergab und gewinnt Energie. Wer sie gegen das Feld schiebt, trägt sie
bergauf. Wer quer läuft, bleibt auf derselben Höhenlinie.

:::herleitung
Nach dem Artikel über Größen und Einheiten ist die Arbeit einer Kraft längs eines Wegs das Wegintegral der Kraft. Mit der Kraft auf
die Ladung im Feld:

$$W_{12} = \int_{P_1}^{P_2}\vec F\cdot d\vec s = \int_{P_1}^{P_2}Q\,\vec E\cdot d\vec s = Q\int_{P_1}^{P_2}\vec E\cdot d\vec s.$$

Die Ladung ist konstant und darf vor das Integral. Im homogenen Feld ist auch $\vec E$ konstant; das Integral eines geraden Wegstücks ist
dann einfach das Skalarprodukt mit dem Wegvektor.
:::

::::beispiel Arbeit im homogenen Feld
Eine Ladung von $2\,\text{nC}$ bewegt sich in einem homogenen Feld von $5\,\frac{\text{kV}}{\text{m}}$ jeweils $4\,\text{cm}$ weit.

**Längs des Felds:**

$$W = 2\cdot10^{-9}\,\text{C}\cdot5\cdot10^{3}\,\frac{\text{V}}{\text{m}}\cdot0{,}04\,\text{m} = 4\cdot10^{-7}\,\text{J}.$$

**Unter $60^\circ$** zur Feldrichtung zählt nur die Hälfte, $\cos60^\circ$ ist $0{,}5$: also $2\cdot10^{-7}\,\text{J}$. **Quer zum Feld**
verrichtet es nichts. **Gegen das Feld** sind es $-4\cdot10^{-7}\,\text{J}$ — diese Energie muss man selbst aufbringen.

Die Einheit geht auf: Coulomb mal Volt ist Joule, denn das Volt ist ein Joule pro Coulomb.

**Im Bild:** Vier Wege gleicher Länge, aber verschiedener Richtung: bergab, schräg bergab, auf der Höhenlinie und bergauf.
::::

## Der geschlossene Umlauf

Was geschieht, wenn die Ladung zum Ausgangspunkt zurückkehrt? Man führt sie von $P_1$ nach $P_2$ und wieder zurück: Die Arbeit
des Hinwegs wird auf dem Rückweg zurückgewonnen, insgesamt ist sie null. Als Integral über den geschlossenen Weg $L$:

:::formel Satz
$$\oint_L\vec E\cdot d\vec s = 0.$$
:::

**So liest man das:** Der Kreis im Integralzeichen bedeutet einen geschlossenen Weg. Für jeden solchen Weg im elektrostatischen Feld
ist das Integral null; das Feld verrichtet auf keiner Runde Arbeit. Felder mit dieser Eigenschaft heißen __wirbelfrei__.
Gleichbedeutend ist die __Wegunabhängigkeit__: Die Arbeit von $P_1$ nach $P_2$ ist auf jedem Weg dieselbe.

**Was der Hin- und Rückweg nicht zeigt.** Läuft man auf **demselben** Weg zurück, kehrt jedes Wegstück einfach seine Richtung um, und die Summe
ist null — für jedes beliebige Feld. Der eigentliche Inhalt des Satzes ist, dass auch ein **anderer** Rückweg die Arbeit wieder
aufhebt. Dass das für elektrostatische Felder stimmt, hat einen Grund im Coulombschen Gesetz.

**Im Bild:** Auf einem Rundweg kommt man wieder auf derselben Höhe an, gleichgültig, wie verschlungen er war.

:::herleitung
**Eine Punktladung.** Ihr Feld zeigt radial und hängt nur vom Abstand $r$ ab. Ein kleines Wegstück zerlegt man in einen Anteil längs
des Radius und einen quer dazu. Der Queranteil steht senkrecht auf dem Feld und trägt nichts bei; der radiale Anteil ändert den
Abstand um $dr$ und trägt das Feld mal $dr$ bei. Die Arbeit hängt deshalb nur vom Anfangs- und Endabstand ab:

$$\int_{P_1}^{P_2}\vec E\cdot d\vec s = \int_{r_1}^{r_2}\frac{Q_0}{4\pi\varepsilon_0\,r^2}\;dr = \frac{Q_0}{4\pi\varepsilon_0}\Big(\frac{1}{r_1}-\frac{1}{r_2}\Big).$$

Für eine Runde sind Anfangs- und Endabstand gleich, also ist das Integral null.

**Beliebige ruhende Ladungen.** Nach dem Superpositionsprinzip ist ihr Feld die Summe von Punktladungsfeldern, und das Integral einer
Summe ist die Summe der Integrale. Jeder Summand ist auf einer Runde null, also auch die Summe.

**Wo es nicht gilt.** Ein sich änderndes Magnetfeld erzeugt nach Faraday ein elektrisches Wirbelfeld. Dort ist das Integral über eine
Runde gerade die induzierte Spannung, und es gibt kein Potenzial.
:::

::::beispiel Zwei Wege, dieselbe Arbeit
Eine Punktladung von $1\,\text{nC}$ sitzt im Ursprung. Eine Probeladung von ebenfalls $1\,\text{nC}$ wandert vom Abstand $1\,\text{cm}$ in den
Abstand $2\,\text{cm}$.

**Weg A, geradlinig nach außen.** Mit der Formel aus der Herleitung und der Konstante aus dem Coulombschen Gesetz:

$$W = 8{,}988\cdot10^{9}\,\frac{\text{N}\,\text{m}^2}{\text{C}^2}\cdot10^{-9}\,\text{C}\cdot10^{-9}\,\text{C}\cdot\Big(\frac{1}{0{,}01\,\text{m}}-\frac{1}{0{,}02\,\text{m}}\Big) \approx 4{,}49\cdot10^{-7}\,\text{J}.$$

**Weg B, erst im Bogen, dann nach außen.** Die Probeladung läuft zuerst einen Viertelkreis im Abstand $1\,\text{cm}$ — dort steht das Feld
senkrecht zum Weg, Arbeit null — und dann radial auf $2\,\text{cm}$: wieder $4{,}49\cdot10^{-7}\,\text{J}$.

**Im Bild:** Der Viertelkreis ist ein Weg längs einer Höhenlinie. Den ganzen Höhenunterschied macht der radiale Teil.
::::

## Das elektrostatische Potenzial

Weil die Arbeit nicht vom Weg abhängt, kann man jedem Punkt eine Zahl zuordnen: wie viel Arbeit es kostet, eine Ladung dorthin zu
bringen. Dazu wählt man einen __Bezugspunkt__ $P_0$, oft unendlich weit weg oder die Erde, und definiert das __elektrostatische
Potenzial__

:::formel Definition
$$\varphi(P) = -\int_{P_0}^{P}\vec E\cdot d\vec s.$$
:::

**So liest man das:** Eingabe ist ein Punkt, Ausgabe eine Zahl in Volt. Durch das Minuszeichen ist $\varphi(P)$ die Arbeit, die man
**gegen** das Feld aufbringen muss, um eine Ladung vom Bezugspunkt nach $P$ zu bringen, geteilt durch die Ladung. Am Bezugspunkt ist
das Potenzial null. Üblich ist auch die Schreibweise $\phi$. Eine Ladung $Q$ hat am Punkt $P$ damit die __potentielle Energie__

$$W_\text{pot}(P) = Q\,\varphi(P).$$

**Im Bild:** Die Höhe über Normalnull. Im Schwerefeld ist die potentielle Energie pro Kilogramm Fallbeschleunigung mal Höhe; das
Potenzial ist die potentielle Energie pro Coulomb.

:::herleitung
Schiebt man die Ladung langsam vom Bezugspunkt nach $P$, muss man in jedem Moment die Feldkraft ausgleichen, also die Kraft
$-Q\,\vec E$ aufbringen. Ihre Arbeit ist

$$W_\text{ext} = \int_{P_0}^{P}\big(-Q\,\vec E\big)\cdot d\vec s = Q\,\varphi(P).$$

Weil die Arbeit nicht vom Weg abhängt, ist diese Zahl eindeutig — erst deshalb darf man jedem Punkt ein Potenzial zuordnen. In einem
Wirbelfeld ginge das nicht.
:::

Zwischen zwei Punkten hängt die Potenzialdifferenz mit der Arbeit des Felds aus dem ersten Abschnitt zusammen:

$$\varphi(P_2)-\varphi(P_1) = -\int_{P_1}^{P_2}\vec E\cdot d\vec s = -\frac{W_{12}}{Q}.$$

**Im Bild:** Wer bergab geht, verliert Höhe, und das Gelände gibt Energie ab. Steigt das Potenzial längs des Wegs, hat das Feld negative
Arbeit verrichtet.

:::herleitung
Man führt den Weg von $P_1$ nach $P_2$ über den Bezugspunkt; das darf man, weil die Arbeit nicht vom Weg abhängt. Kehrt man die Richtung
eines Wegstücks um, wechselt sein Integral das Vorzeichen:

$$\int_{P_1}^{P_2}\vec E\cdot d\vec s = \int_{P_1}^{P_0}\vec E\cdot d\vec s+\int_{P_0}^{P_2}\vec E\cdot d\vec s = \varphi(P_1)-\varphi(P_2).$$

Mit dem Minuszeichen und der Arbeit des Felds aus dem ersten Abschnitt folgt die Formel.
:::

**Achtung, Vorzeichen.** Mit dem Bezugspunkt $P_1$ ist $-\int_{P_1}^{P_2}\vec E\cdot d\vec s$ das Potenzial von $P_2$, also die Differenz
$\varphi(P_2)-\varphi(P_1)$; falsch wäre $-\big[\varphi(P_2)-\varphi(P_1)\big]$. Gleich $\frac{W}{Q}$ ist sie nur, wenn $W$ die Arbeit **gegen**
das Feld meint; die vom Feld freigesetzte Arbeit hat das umgekehrte Vorzeichen.

**Das Potenzial einer Punktladung.** Mit dem Bezugspunkt im Unendlichen ist das Potenzial einer Punktladung $Q_0$ im Abstand $r$

:::formel
$$\varphi(r) = \frac{1}{4\pi\varepsilon_0}\,\frac{Q_0}{r}.$$
:::

**So liest man das:** Das Potenzial fällt nur wie $\frac1r$, langsamer als das Feld. Eine positive Ladung ist ein Berg, eine negative ein
Tal; weit weg liegt das Gelände auf Normalnull.

:::herleitung
Weil der Weg gleichgültig ist, kommt man aus dem Unendlichen radial heran. Das Feld zeigt radial nach außen, der Weg nach innen; mit
der radialen Koordinate $r'$ als Integrationsvariable:

$$\varphi(r) = -\int_{\infty}^{r}\frac{Q_0}{4\pi\varepsilon_0\,r'^2}\;dr' = -\frac{Q_0}{4\pi\varepsilon_0}\Big[-\frac{1}{r'}\Big]_{\infty}^{r} = \frac{Q_0}{4\pi\varepsilon_0\,r}.$$
:::

::::beispiel Das Potenzial einer Punktladung
Für die Punktladung von $1\,\text{nC}$ aus dem Beispiel mit den zwei Wegen ist der Vorfaktor

$$\frac{Q_0}{4\pi\varepsilon_0} \approx 8{,}988\,\text{V}\,\text{m}, \qquad \varphi(1\,\text{cm}) = \frac{8{,}988\,\text{V}\,\text{m}}{0{,}01\,\text{m}} \approx 899\,\text{V}, \qquad \varphi(2\,\text{cm}) \approx 449\,\text{V}.$$

Die Potenzialdifferenz ist rund $449\,\text{V}$. Mal der Probeladung von $1\,\text{nC}$ ist das die Arbeit, die das Feld auf beiden Wegen
verrichtet hat:

$$W_{12} = Q\,\big(\varphi(1\,\text{cm})-\varphi(2\,\text{cm})\big) = 10^{-9}\,\text{C}\cdot449\,\text{V} \approx 4{,}49\cdot10^{-7}\,\text{J}.$$

**Im Bild:** Die Probeladung ist vom Gipfelhang in $1\,\text{cm}$ zum flacheren Hang in $2\,\text{cm}$ hinabgestiegen. Die Höhen sagen, wie
viel Energie dabei frei wird, ohne dass man den Weg kennen muss.
::::

## Die elektrische Spannung

Die technisch wichtigste Potenzialdifferenz heißt __elektrische Spannung__. Die Spannung zwischen den Punkten $P_1$ und $P_2$ ist

:::formel Definition
$$U_{12} = \varphi(P_1)-\varphi(P_2) = \int_{P_1}^{P_2}\vec E\cdot d\vec s.$$
:::

**So liest man das:** Die Reihenfolge der Indizes zählt. $U_{12}$ ist das Potenzial am ersten Punkt minus das am zweiten, also ist $U_{21}$
das Negative von $U_{12}$. Positiv ist $U_{12}$, wenn der erste Punkt höher liegt. Im Schaltbild zeichnet man die Spannung als Pfeil vom
ersten zum zweiten Punkt, den __Spannungspfeil__.

**Kein Minus vor dem Integral.** Ein häufiger Fehler ist, die Spannung mit einem Minus vor dem Integral zu schreiben. Die Probe am Plattenkondensator zeigt,
dass es nicht hingehört: Vom Plus- zur Minusplatte zeigt das Feld in Wegrichtung, das Integral ist positiv, und die Plusplatte hat das
höhere Potenzial. Die Spannung von Plus nach Minus ist also positiv — mit dem Minus wäre sie negativ.

:::herleitung
Das zweite Gleichheitszeichen ist die Potenzialdifferenz aus dem vorigen Abschnitt, nur mit vertauschter Reihenfolge der Punkte:

$$\varphi(P_1)-\varphi(P_2) = -\big(\varphi(P_2)-\varphi(P_1)\big) = \int_{P_1}^{P_2}\vec E\cdot d\vec s.$$
:::

Die Arbeit, die das Feld an einer Ladung von $P_1$ nach $P_2$ verrichtet, ist damit Ladung mal Spannung:

$$W_{12} = Q\,U_{12}, \qquad 1\,\text{V} = 1\,\frac{\text{J}}{\text{C}}.$$

**So liest man das:** Die Spannung hängt nicht von der Ladung ab, die man verschiebt. Man nennt sie deshalb das
körperunabhängige Maß für das Feld zwischen zwei Punkten: Sie gibt das __Arbeitsvermögen__ jeder Ladung an, die diese Strecke
durchläuft. Ein Volt bedeutet ein Joule pro Coulomb.

**Im Bild:** Der Höhenunterschied zwischen zwei Punkten. Die Energie, die ein Körper beim Abstieg abgibt, ist sein Gewicht mal diesem
Unterschied — bei Ladungen die Ladung mal der Spannung.

:::herleitung
Mit der Arbeit des Felds aus dem ersten Abschnitt und der Definition der Spannung:

$$W_{12} = Q\int_{P_1}^{P_2}\vec E\cdot d\vec s = Q\,U_{12}.$$

Die Einheit folgt aus Arbeit durch Ladung:

$$[U] = \frac{[W]}{[Q]} = \frac{\text{N}\,\text{m}}{\text{A}\,\text{s}} = \frac{\text{kg}\,\text{m}^2}{\text{A}\,\text{s}^3} = \text{V}.$$
:::

**Unabhängig vom Bezugspunkt.** Wählt man einen anderen Bezugspunkt, ändern sich alle Potenziale um dieselbe Konstante, nämlich das
Integral zwischen altem und neuem Bezugspunkt. In der Differenz fällt sie heraus: Potenziale hängen vom Bezugspunkt ab, Spannungen
nicht.

**Im homogenen Feld.** Zwischen den Platten eines Plattenkondensators im Abstand $d$ ist das Feld homogen. Vom Plus- zum Minuspol
gerechnet:

$$U = E\cdot d, \qquad E = \frac{U}{d}.$$

**Im Bild:** Ein gleichmäßiger Hang: Höhenunterschied ist Steigung mal Strecke.

:::herleitung
Man integriert längs einer Feldlinie von der Plus- zur Minusplatte. Feld und Weg zeigen in dieselbe Richtung, und das Feld ist
konstant:

$$U = \int_{+}^{-}\vec E\cdot d\vec s = E\int_0^d ds = E\cdot d.$$
:::

**Das Elektronenvolt.** Durchläuft eine Elementarladung die Spannung $1\,\text{V}$, wird die Energie Ladung mal Spannung frei:

$$1\,\text{eV} = 1{,}602\cdot10^{-19}\,\text{C}\cdot1\,\text{V} = 1{,}602\cdot10^{-19}\,\text{J}.$$

Dieses __Elektronenvolt__ ist in der Physik und der Halbleitertechnik die übliche Energieeinheit.

::::beispiel Kondensator und Elektronenvolt
**(a) Ein Plattenkondensator** mit $1\,\text{mm}$ Plattenabstand liegt an $12\,\text{V}$:

$$E = \frac{12\,\text{V}}{10^{-3}\,\text{m}} = 12\,\frac{\text{kV}}{\text{m}}.$$

Bis zur Durchschlagsfestigkeit der Luft von etwa $3\,\frac{\text{MV}}{\text{m}}$ fehlt noch der Faktor $250$; nach dieser Faustregel schlüge
der Spalt erst bei etwa $3\,\text{kV}$ durch.

**(b) Ein Elektron** startet ruhend an der Minusplatte und erreicht die Plusplatte. Es durchläuft $12\,\text{V}$, gewinnt also $12\,\text{eV}$:

$$W = 12\cdot1{,}602\cdot10^{-19}\,\text{J} \approx 1{,}92\cdot10^{-18}\,\text{J}, \qquad v = \sqrt{\frac{2W}{m_\text{e}}} = \sqrt{\frac{2\cdot1{,}92\cdot10^{-18}\,\text{J}}{9{,}109\cdot10^{-31}\,\text{kg}}} \approx 2{,}05\cdot10^{6}\,\frac{\text{m}}{\text{s}}.$$

Dabei ist $m_\text{e}$ die Elektronenmasse und $v$ die Endgeschwindigkeit aus der Bewegungsenergie $\frac12m_\text{e}v^2$.

**Im Bild:** Für negative Ladungen steht die Landschaft Kopf: Das Elektron „rollt" zum höheren Potenzial, von Minus nach Plus, und
gewinnt dabei Energie.
::::

**Wie groß sind Spannungen?** Einige typische Werte:

| Anwendung | Spannung |
|---|---|
| Empfindlichkeit moderner Spannungsmesser | etwa $0{,}1\,\text{nV}$ |
| zwischen Hand und Herz | etwa $1\,\text{mV}$ |
| Empfangsspannung an einer Fernsehantenne | $12\,\mu\text{V}$ bis $10\,\text{mV}$ |
| Autobatterie | etwa $12\,\text{V}$ |
| Lichtnetz in Europa | $230\,\text{V}$ (früher $220\,\text{V}$) |
| Hochspannungsleitung | $120\,\text{kV}$ bis $800\,\text{kV}$ |
| Van-de-Graaff-Generator | etwa $10\,\text{MV}$ |
| Blitz | bis $100\,\text{MV}$ |

:::grafik
Szene: get1/elektrische-feldstaerke-und-potenzial/02-spannungsquellen · Vorlage: quellen-symbole
Links das Schaltzeichen einer Batterie: zwei parallele Striche, der längere dünne ist der Pluspol, der kürzere dicke der Minuspol;
daneben der Spannungspfeil $U$ vom Plus- zum Minuspol. Rechts das Schaltzeichen einer Gleichspannungsquelle: ein Kreis, durch den die
Leitung senkrecht hindurchläuft, daneben ebenfalls der Spannungspfeil. Darunter eine Autobatterie mit $12\,\text{V}$, deren Minuspol über das
Massesymbol mit der Karosserie verbunden ist; an den Klemmen stehen die Potenziale $12\,\text{V}$ und $0\,\text{V}$. Kernaussage: Der
Spannungspfeil zeigt vom höheren zum niedrigeren Potenzial, und die Masse legt den Nullpunkt fest. (Rot = Quellen, blau = Leitungen,
orange = Spannungspfeile, grau = Massesymbol und Karosserie.)
:::

## Bezugspotenzial und Masse

In einer Schaltung legt man einen Punkt als Bezugspunkt fest, gibt ihm das Potenzial $0\,\text{V}$ und kennzeichnet ihn mit dem
__Massesymbol__ — Erdanschluss, Masse, englisch GND für *ground*. Erst damit haben die übrigen Punkte Potenziale; ohne Bezugspunkt kann
man nur Spannungen angeben. Punkte, die durch eine ideale Leitung verbunden sind, liegen auf demselben Potenzial, denn in ihr fällt keine
Spannung ab.

Im Auto ist meist, aber nicht immer, der Minuspol der Batterie mit der Karosserie verbunden und dient als Masse; der Pluspol liegt dann
auf $12\,\text{V}$. Wählt man einen anderen Bezugspunkt, verschieben sich beide Potenziale um denselben Betrag, und die Spannung der
Batterie bleibt $12\,\text{V}$.

**Im Bild:** Normalnull ist eine Vereinbarung. Ob man Höhen über dem Meer oder über dem Talboden angibt, der Höhenunterschied zwischen zwei
Gipfeln bleibt derselbe.

::::beispiel Potenziale in einer Kette
Vier Punkte A, B, C, D liegen in einer Schaltung hintereinander; bekannt sind die Spannungen zwischen Nachbarn:

$$U_\text{AB} = 3\,\text{V}, \qquad U_\text{BC} = 4\,\text{V}, \qquad U_\text{CD} = 2\,\text{V}.$$

**Masse an D.** Von $\varphi_\text{D}=0$ aus geht man rückwärts, denn jede Spannung ist das Potenzial des ersten Punkts minus das des
zweiten:

$$\varphi_\text{C} = 2\,\text{V}, \qquad \varphi_\text{B} = 6\,\text{V}, \qquad \varphi_\text{A} = 9\,\text{V}.$$

**Masse an B.** Jetzt ist $\varphi_\text{B}=0$, und alle Potenziale verschieben sich um $-6\,\text{V}$:

$$\varphi_\text{A} = 3\,\text{V}, \qquad \varphi_\text{C} = -4\,\text{V}, \qquad \varphi_\text{D} = -6\,\text{V}.$$

Die Spannung von A nach D ist in beiden Fällen dieselbe, $9\,\text{V}$, und auch die Summe der drei Teilspannungen.

**Im Bild:** Eine Treppe aus drei Stufen. Wo man den Boden hinlegt, ändert die Höhenangaben, aber nicht die Stufen.
::::

## Äquipotentialflächen

Punkte gleichen Potenzials bilden __Äquipotentialflächen__. Auf ihnen kann man Ladungen verschieben, ohne Arbeit zu verrichten. Sie
stehen überall senkrecht auf den Feldlinien, und das Feld zeigt vom höheren zum niedrigeren Potenzial.

Bei einer Punktladung sind die Äquipotentialflächen Kugeln um die Ladung, im Plattenkondensator Ebenen parallel zu den Platten. Auch
jeder Leiter ist im Ruhezustand ein Äquipotentialkörper: In seinem Inneren ist das Feld null, also ändert sich das Potenzial darin nicht.

**Im Bild:** Die Höhenlinien der Wanderkarte. Das Gefälle steht senkrecht auf ihnen und zeigt bergab, und wo sie dicht liegen, ist der
Hang steil.

:::herleitung
Für ein kleines Wegstück $d\vec s$ ändert sich das Potenzial nach der Formel für die Potenzialdifferenz um

$$d\varphi = -\vec E\cdot d\vec s.$$

**Senkrecht.** Längs einer Äquipotentialfläche ändert sich das Potenzial nicht; dort ist das Skalarprodukt null, das Feld steht also
senkrecht auf jedem Wegstück in der Fläche.

**Bergab.** Geht man ein Stück in Feldrichtung, ist das Skalarprodukt positiv, und das Potenzial nimmt ab.

**Dichte Flächen, starkes Feld.** Zwischen zwei benachbarten Flächen mit der Potenzialdifferenz $\Delta\varphi$ im Abstand $\Delta s$ ist der
Betrag des Felds ungefähr $\frac{\Delta\varphi}{\Delta s}$ — je enger die Flächen, desto größer.
:::

::::beispiel Höhenlinien einer Punktladung
Für die Punktladung von $1\,\text{nC}$ liegen die Äquipotentialflächen bei den Radien

$$r = \frac{8{,}988\,\text{V}\,\text{m}}{\varphi}: \qquad 100\,\text{V}: \ 8{,}99\,\text{cm}, \qquad 200\,\text{V}: \ 4{,}49\,\text{cm}, \qquad 300\,\text{V}: \ 3{,}00\,\text{cm}, \qquad 400\,\text{V}: \ 2{,}25\,\text{cm}.$$

Die Abstände zwischen den Flächen schrumpfen: $4{,}49\,\text{cm}$, $1{,}50\,\text{cm}$, $0{,}75\,\text{cm}$. Zwischen $300$ und $400\,\text{V}$
schätzt man das Feld als Potenzialdifferenz durch Abstand:

$$E \approx \frac{100\,\text{V}}{0{,}0075\,\text{m}} \approx 1{,}33\cdot10^{4}\,\frac{\text{V}}{\text{m}}.$$

Genau dazwischen, bei $r\approx2{,}6\,\text{cm}$, gibt die Formel der Punktladung denselben Wert.

**Im Bild:** Nahe am Gipfel liegen die Höhenlinien eng, der Hang ist steil. Weiter draußen flacht er ab.
::::

:::grafik
Szene: get1/elektrische-feldstaerke-und-potenzial/02-aequipotentialflaechen · Vorlage: aequipotential-und-feldlinien
Links eine positive Punktladung mit radialen Feldlinien und konzentrischen Äquipotentialkreisen bei $100$, $200$, $300$ und $400\,\text{V}$,
die nach innen enger werden. Rechts ein Plattenkondensator mit senkrechten Feldlinien und waagerechten, gleich weit entfernten
Äquipotentiallinien. An einigen Schnittpunkten ist der rechte Winkel markiert. Ein Regler bewegt eine Probeladung längs einer
Äquipotentiallinie, ein Zähler zeigt dabei die Arbeit null; bewegt man sie quer, zählt der Zähler. Kernaussage: Äquipotentialflächen
stehen senkrecht auf den Feldlinien, und ihr Abstand zeigt die Feldstärke. (Blau = Feldlinien, rot = Äquipotentiallinien, orange =
Probeladung und Zähler, grau = Platten und rechte Winkel.)
:::

## Bedeutung und Ausblick

Die Spannung ist die zentrale Größe jeder Schaltung, und mit dem Potenzial lässt sie sich wie eine Höhe denken. Aus dem geschlossenen
Umlauf wird die __Maschenregel__ von Kirchhoff, die der Artikel [Die Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html)
behandelt: Längs jedes geschlossenen Wegs durch eine Schaltung addieren sich die Spannungen zu null — so wie in der Kette der Punkte
A bis D.

Der Artikel [Der Kondensator und seine Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html)
behandelt als Nächstes den Kondensator. Er speichert Ladung auf zwei Platten, und die Spannung zwischen ihnen hängt über
$U=E\cdot d$ mit dem Feld im Spalt zusammen.

:::kern
- Das Feld verrichtet an einer Ladung die Arbeit $W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot d\vec s$; es zählt nur der Wegteil längs des Felds.
- Im elektrostatischen Feld ist die Arbeit wegunabhängig und auf jedem geschlossenen Weg null — das Feld ist __wirbelfrei__.
- Der Grund: Das Feld einer Punktladung ist radial, nur Abstandsänderungen zählen; die Überlagerung überträgt das auf alle ruhenden Ladungen.
- __Potenzial__: $\varphi(P)=-\int_{P_0}^{P}\vec E\cdot d\vec s$, die Arbeit gegen das Feld pro Ladung vom Bezugspunkt aus.
- Eine Punktladung hat mit dem Bezugspunkt im Unendlichen das Potenzial $\frac{1}{4\pi\varepsilon_0}\frac{Q_0}{r}$.
- __Spannung__: $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot d\vec s$, ohne Minus vor dem Integral.
- Die vom Feld verrichtete Arbeit ist Ladung mal Spannung; ein Volt ist ein Joule pro Coulomb.
- Ein __Elektronenvolt__ ist die Energie einer Elementarladung nach einem Volt: $1{,}602\cdot10^{-19}\,\text{J}$.
- Potenziale hängen vom Bezugspunkt ab, Spannungen nicht; die __Masse__ legt den Nullpunkt fest.
- Im homogenen Feld gilt $U=E\cdot d$; im Plattenkondensator ist die Feldstärke Spannung durch Plattenabstand.
- __Äquipotentialflächen__ stehen senkrecht auf den Feldlinien, das Feld zeigt zum niedrigeren Potenzial, und dichte Flächen bedeuten starkes Feld.
:::

:::quiz
F: Welche Arbeit verrichtet das Feld an einer Ladung, und was ergibt sich für $2\,\text{nC}$ im Feld von $5\,\frac{\text{kV}}{\text{m}}$ auf $4\,\text{cm}$?
A: Die Arbeit ist $W_{12}=Q\int\vec E\cdot d\vec s$, im homogenen Feld $Q\,E\,\Delta s\cos\alpha$. Längs des Felds sind das $4\cdot10^{-7}\,\text{J}$, unter $60^\circ$ die Hälfte, quer zum Feld nichts und gegen das Feld $-4\cdot10^{-7}\,\text{J}$ — Energie, die man selbst aufbringen muss.
F: Warum ist das Integral über einen geschlossenen Weg im elektrostatischen Feld null, und warum reicht „hin und auf demselben Weg zurück" als Begründung nicht?
A: Auf demselben Weg zurück kehrt jedes Wegstück nur seine Richtung um; das gibt für jedes Feld null. Der Inhalt des Satzes ist, dass auch ein anderer Rückweg die Arbeit aufhebt. Das folgt aus dem Coulombschen Gesetz: Das Feld einer Punktladung ist radial, nur Abstandsänderungen zählen, und die Überlagerung überträgt das auf alle ruhenden Ladungen. Ein Wirbelfeld aus der Induktion erfüllt es nicht.
F: Wie zeigt die Punktladung von $1\,\text{nC}$, dass die Arbeit nicht vom Weg abhängt?
A: Eine Probeladung von $1\,\text{nC}$ wandert von $1\,\text{cm}$ auf $2\,\text{cm}$ Abstand. Geradlinig nach außen verrichtet das Feld $\frac{Q_0Q}{4\pi\varepsilon_0}\big(\frac{1}{r_1}-\frac{1}{r_2}\big)\approx4{,}49\cdot10^{-7}\,\text{J}$. Auf einem Umweg über einen Viertelkreis im Abstand $1\,\text{cm}$ ist der Bogen arbeitsfrei, weil das Feld senkrecht auf ihm steht, und der radiale Rest liefert dieselbe Arbeit.
F: Wie ist das Potenzial definiert, und warum steht ein Minuszeichen vor dem Integral?
A: $\varphi(P)=-\int_{P_0}^{P}\vec E\cdot d\vec s$ mit einem gewählten Bezugspunkt $P_0$. Durch das Minus ist es die Arbeit, die man gegen das Feld aufbringen muss, um eine Ladung vom Bezugspunkt nach $P$ zu bringen, pro Ladung; die potentielle Energie ist $Q\varphi$. Eindeutig ist die Zahl nur, weil die Arbeit nicht vom Weg abhängt.
F: Welches Potenzial hat eine Punktladung, und wie passt es zur Arbeit zwischen $1\,\text{cm}$ und $2\,\text{cm}$?
A: Mit dem Bezugspunkt im Unendlichen ist $\varphi(r)=\frac{1}{4\pi\varepsilon_0}\frac{Q_0}{r}$, bei $1\,\text{nC}$ also etwa $899\,\text{V}$ in $1\,\text{cm}$ und $449\,\text{V}$ in $2\,\text{cm}$. Die Differenz mal der Probeladung von $1\,\text{nC}$ ergibt $4{,}49\cdot10^{-7}\,\text{J}$, genau die Arbeit auf beiden Wegen.
F: Wie ist die Spannung $U_{12}$ definiert, und warum gehört kein Minus vor das Integral?
A: $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot d\vec s$, mit $U_{21}=-U_{12}$. Probe am Plattenkondensator: Von der Plus- zur Minusplatte zeigt das Feld in Wegrichtung, das Integral ist positiv, und die Plusplatte liegt höher — die Spannung ist positiv. Mit einem Minus wäre sie negativ.
F: Warum hängt die Spannung nicht vom Bezugspunkt ab, und was zeigt die Kette der Punkte A bis D?
A: Ein anderer Bezugspunkt verschiebt alle Potenziale um dieselbe Konstante, die in jeder Differenz herausfällt. Mit Masse an D liegen A, B, C auf $9$, $6$ und $2\,\text{V}$, mit Masse an B auf $3$, $0$ und $-4\,\text{V}$ und D auf $-6\,\text{V}$; die Spannung von A nach D bleibt $9\,\text{V}$, die Summe der Teilspannungen.
F: Wie hängen Spannung und Feldstärke im Plattenkondensator zusammen, und was ergibt einer mit $12\,\text{V}$ und $1\,\text{mm}$ Abstand?
A: Im homogenen Feld integriert man längs einer Feldlinie von Plus nach Minus und erhält $U=E\cdot d$, also $E=\frac Ud$. Bei $12\,\text{V}$ und $1\,\text{mm}$ sind das $12\,\frac{\text{kV}}{\text{m}}$ — noch das $250$-Fache unter der Durchschlagsfestigkeit der Luft von etwa $3\,\frac{\text{MV}}{\text{m}}$.
F: Was ist ein Elektronenvolt, und wie schnell wird ein Elektron, das ruhend $12\,\text{V}$ durchläuft?
A: Ein Elektronenvolt ist die Energie, die eine Elementarladung beim Durchlaufen von einem Volt gewinnt, $1{,}602\cdot10^{-19}\,\text{J}$. Nach $12\,\text{V}$ hat das Elektron $12\,\text{eV}$, rund $1{,}92\cdot10^{-18}\,\text{J}$; aus $\frac12m_\text{e}v^2$ folgt etwa $2{,}05\cdot10^6\,\frac{\text{m}}{\text{s}}$. Als negative Ladung läuft es dabei von Minus nach Plus, zum höheren Potenzial.
F: Warum stehen Äquipotentialflächen senkrecht auf den Feldlinien, und was verrät ihr Abstand?
A: Für ein kleines Wegstück ist $d\varphi=-\vec E\cdot d\vec s$. Längs einer Äquipotentialfläche ist das null, also steht das Feld senkrecht auf ihr; in Feldrichtung nimmt das Potenzial ab. Der Abstand zweier Flächen zeigt die Feldstärke, ungefähr Potenzialdifferenz durch Abstand: Bei der Punktladung liegen die Flächen für $300$ und $400\,\text{V}$ nur $0{,}75\,\text{cm}$ auseinander, das Feld dort ist etwa $1{,}33\cdot10^4\,\frac{\text{V}}{\text{m}}$.
:::
