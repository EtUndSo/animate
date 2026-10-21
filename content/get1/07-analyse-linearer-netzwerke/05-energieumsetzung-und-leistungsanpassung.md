---
title: Energieumsetzung und Leistungsanpassung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70800
summary: Von Grund auf – wie viel Energie eine verschobene Ladung abgibt, was Leistung genau ist, warum Widerstände eine Belastungsgrenze haben und Strom über Hochspannungsleitungen reist, und bei welchem Lastwiderstand eine Quelle die größte Leistung abgibt – zu welchem Preis. Leitbild ist ein Wasserturm, der über eine Zuleitung ein Wasserrad treibt. Mit Energie und Leistung samt Einheiten, Joulescher Wärme, Nennbelastbarkeit, Leitungsverlusten und Spannungsebenen, der mittleren Leistung bei Sinusspannung, der Leistungsanpassung mit Herleitung auf zwei Wegen, der Anpassung an ein ganzes Netz über die Ersatzquelle und dem Wirkungsgrad. Mit Beispiel-Seite.
tags: Leistung, Joulesche Wärme, Leistungsanpassung, maximale Leistung, Wirkungsgrad
---

## Anschaulich

Bisher ging es darum, welche Ströme und Spannungen sich in einem Netz einstellen. Dieser Artikel fragt, was sie bewirken: wie viel Energie umgesetzt
wird, wie schnell, wo sie verloren geht und wie man möglichst viel davon zum Verbraucher bringt.

**Das Leitbild dieses Artikels:** **Turm, Zuleitung und Wasserrad.** Ein Wasserturm treibt über eine Zuleitung ein Wasserrad an. Jeder Liter, der vom
Turm durch Leitung und Rad hinunterfließt, gibt Energie ab, und zwar Druck mal Wassermenge — so wie eine Ladung, die eine Spannung durchläuft, Spannung
mal Ladung abgibt. Wie schnell das geschieht, die Leistung, ist Druck mal Durchfluss, im Elektrischen Spannung mal Strom. In der Zuleitung reibt sich das
Wasser und wärmt das Rohr; das ist der Verlust im Innenwiderstand der Quelle. Am Rad wird die Energie genutzt. Wir nehmen ein Rad an, das wie ein Rohr
bremst: Je mehr Wasser hindurchfließt, desto mehr Druck nimmt es auf, wie ein Lastwiderstand.

Drei Folgerungen:

- **Die Reibung wächst mit dem Quadrat des Durchflusses.** Doppelter Durchfluss heißt doppelter Druckverlust bei doppelter Menge, also vierfache Wärme.
  Wer viel Leistung weit transportieren will, nimmt deshalb hohen Druck und kleinen Durchfluss — im Stromnetz hohe Spannung und kleinen Strom.
- **Das Rad holt nicht beliebig viel heraus.** Ein leichtgängiges Rad lässt viel Wasser durch, nimmt aber kaum Druck auf; ein schwergängiges nimmt viel
  Druck auf, lässt aber kaum Wasser durch. Dazwischen liegt ein Maximum, und es liegt dort, wo das Rad genauso stark bremst wie die Zuleitung.
- **Im Maximum geht die Hälfte verloren.** Bremsen Rad und Zuleitung gleich stark, wärmt die Zuleitung genau so viel, wie das Rad nutzt. Wer sparsam
  sein will, nimmt ein viel schwergängigeres Rad und verzichtet auf das Maximum.

:::grafik
Szene: get1/analyse-linearer-netzwerke/05-turm-wasserrad · Vorlage: turm-zuleitung-wasserrad
Ein Wasserturm, eine Zuleitung mit Thermometer am Rohr und ein Wasserrad mit verstellbarer Bremse, dahinter ein Rücklauf. Anzeigen für den Druck am Rad,
den Durchfluss, die Leistung am Rad (Druck mal Durchfluss) und die Wärmeleistung in der Zuleitung. Ein Regler verstellt die Bremse vom leichtgängigen bis
zum blockierten Rad; ein Diagramm zeichnet die Leistung am Rad über der Bremsstärke mit, mit einem Maximum dort, wo Rad und Zuleitung gleich stark bremsen,
und darunter den Anteil der genutzten an der gesamten Leistung, der stetig steigt und im Maximum bei der Hälfte liegt. Kernaussage: Die größte Leistung am
Rad gibt es bei gleich starker Bremse, aber nur mit halbem Wirkungsgrad. (Blau = Wasser und Diagramme, rot = Turm und Rad, orange = Wärme in der
Zuleitung, grau = Rohre und Rücklauf.)
:::

## Energie beim Verschieben von Ladung

Eine Spannung ist Energie pro Ladung (Artikel über Arbeit, Potenzial und Spannung). Wandert eine kleine Ladung $dQ$ durch einen Widerstand vom Potenzial
$\varphi_1$ zum niedrigeren Potenzial $\varphi_2$, gibt sie deshalb die Energie

$$dW = U_{12}\,dQ, \qquad U_{12} = \varphi_1 - \varphi_2,$$

an den Widerstand ab. Fließt dabei der Strom $I$, wandert in der kurzen Zeit $dt$ die Ladung $I\,dt$; über ein Zeitintervall von $t_1$ bis $t_2$ summiert
sich die Energie zu

:::formel
$$W = \int_{t_1}^{t_2} U\,I\,dt, \qquad W = U\,I\,\Delta t\quad\text{bei Gleichstrom}.$$
:::

**So liest man das:** Die Energie ist das Integral von Spannung mal Strom über die Zeit; bleiben beide konstant, wie bei Gleichstrom, ist sie das
Produkt mit der Dauer $\Delta t$, gleich $t_2 - t_1$. Ihre Einheit ist das Joule:

$$[W] = \text{V}\,\text{A}\,\text{s} = \text{W}\,\text{s} = \text{J} = \text{N}\,\text{m}, \qquad 1\,\text{kWh} = 3{,}6\,\text{MJ}.$$

In der Elektrotechnik rechnet man meist in Wattsekunden oder Kilowattstunden. Im Widerstand wird die Energie zu Wärme, der __Jouleschen Wärme__ oder
__Stromwärme__: Nach dem Drude-Modell aus dem Artikel über den ohmschen Widerstand geben die Elektronen die Energie, die das Feld ihnen zwischen zwei
Stößen zuführt, beim Stoß an das Kristallgitter ab. So arbeiten Föhn, Toaster und Lötkolben.

Zwei Stellen im Skript sind ungenau. Es schreibt die Spannung hier als $\varphi_2 - \varphi_1$; das ist die Änderung der potenziellen Energie je Ladung,
die auf dem Weg zum niedrigeren Potenzial negativ ist, während die abgegebene Energie mit $U_{12}$ positiv zählt. Und das Newtonmeter ist keine Einheit
mechanischer Leistung, wie es dort heißt, sondern der mechanischen Arbeit und des Drehmoments.

**Im Bild:** Jeder Liter, der vom Turm hinunterfließt, gibt Druck mal Menge ab; fließt das Wasser gleichmäßig, wächst die abgegebene Energie
gleichmäßig mit der Zeit.

:::herleitung
**Energie pro Ladung.** Die Spannung $U_{12}$ ist die Arbeit, die das Feld an einer Ladung beim Weg von $\varphi_1$ nach $\varphi_2$ verrichtet, geteilt
durch diese Ladung. Für die kleine Ladung $dQ$ ist diese Arbeit $U_{12}\,dQ$; im Widerstand kommt sie nicht als Bewegungsenergie an, sondern geht in
den Stößen an das Gitter.

**Integrieren.** Mit der Ladung $I\,dt$, die in der Zeit $dt$ durchfließt, und der Summe über alle Zeitstücke:

$$dW = U\,I\,dt, \qquad W = \int_{t_1}^{t_2} U\,I\,dt = U\,I\,(t_2 - t_1)\quad\text{für konstante } U, I.$$

**Einheit.** Volt ist Joule pro Coulomb, Ampere Coulomb pro Sekunde:

$$\text{V}\,\text{A}\,\text{s} = \frac{\text{J}}{\text{C}}\cdot\frac{\text{C}}{\text{s}}\cdot\text{s} = \text{J}.$$
:::

::::beispiel Heckscheibenheizung und E-Bike-Akku
**(a) Die Heckscheibenheizung** eines Autos nimmt an $12\,\text{V}$ einen Strom von $12\,\text{A}$ auf und läuft $10$ Minuten:

$$W = 12\,\text{V}\cdot12\,\text{A}\cdot600\,\text{s} = 86\,400\,\text{J} = 0{,}024\,\text{kWh}.$$

Durch die Heizdrähte sind dabei geflossen

$$Q = 12\,\text{A}\cdot600\,\text{s} = 7200\,\text{A}\,\text{s} = 2\,\text{Ah}.$$

**(b) Ein E-Bike-Akku** mit $36\,\text{V}$ und einer Ladung von $14\,\text{Ah}$ speichert nach $W = UQ$ näherungsweise, denn die Spannung sinkt beim
Entladen etwas,

$$W = 36\,\text{V}\cdot14\,\text{Ah} = 504\,\text{Wh} \approx 1{,}81\,\text{MJ}.$$

**Im Bild:** Eine bestimmte Wassermenge, unter einem bestimmten Druck abgelassen, trägt eine bestimmte Energie, gleichgültig, wie schnell sie fließt.
::::

## Leistung

Elektrische Geräte laufen meist dauernd. Dann ist nicht die Energie die nützliche Angabe, sondern wie schnell sie umgesetzt wird, die __Leistung__:

:::formel Definition
$$P = \frac{W}{\Delta t}, \qquad [P] = \frac{\text{J}}{\text{s}} = \text{V}\,\text{A} = \text{W}\ \text{(Watt)}.$$
:::

**So liest man das:** Energie geteilt durch die Zeit, in der sie umgesetzt wird. Über ein Zeitintervall gerechnet ist das die __mittlere Leistung__; das
Skript spricht vom zeitlichen Mittelwert. Lässt man das Intervall schrumpfen, erhält man die __Augenblicksleistung__, für zeitabhängige Größen klein
geschrieben; bei Gleichstrom sind beide gleich. Für Gleichstrom und am Widerstand folgt mit dem ohmschen Gesetz:

$$P = U\,I = R\,I^2 = \frac{U^2}{R}, \qquad p(t) = \frac{dW}{dt} = u(t)\,i(t).$$

Die Leistung wächst quadratisch mit Strom oder Spannung: Halbe Spannung am selben Widerstand heißt ein Viertel der Leistung. Das Volt-Ampere ist dasselbe
wie das Watt; in der Wechselstromtechnik bekommt es später eine eigene Rolle.

**Im Bild:** Druck mal Durchfluss. In einem Rohr wächst mit dem Durchfluss auch der Druckverlust, die Reibungsleistung also mit dem Quadrat.

:::herleitung
**Aus der Energie.** Bei Gleichstrom ist die Energie $U\,I\,\Delta t$; geteilt durch $\Delta t$ bleibt $U\,I$.

**Am Widerstand.** Mit $U$ gleich $R I$ beziehungsweise $I$ gleich $U/R$:

$$P = U\,I = (R\,I)\,I = R\,I^2, \qquad P = U\cdot\frac{U}{R} = \frac{U^2}{R}.$$

**Augenblicklich.** Für ein schrumpfendes Intervall wird der Quotient zur Ableitung, und mit dem Energiezuwachs $u\,i\,dt$ aus dem vorigen Abschnitt:

$$p(t) = \lim_{\Delta t\to0}\frac{\Delta W}{\Delta t} = \frac{dW}{dt} = u(t)\,i(t).$$
:::

::::beispiel Ein Heizwiderstand
Ein Heizwiderstand ist für $24\,\text{V}$ und $60\,\text{W}$ gebaut. Strom und Widerstand:

$$I = \frac{60\,\text{W}}{24\,\text{V}} = 2{,}5\,\text{A}, \qquad R = \frac{24\,\text{V}}{2{,}5\,\text{A}} = 9{,}6\,\Omega.$$

**Probe** mit den anderen beiden Formen:

$$R\,I^2 = 9{,}6\,\Omega\cdot(2{,}5\,\text{A})^2 = 60\,\text{W}, \qquad \frac{U^2}{R} = \frac{(24\,\text{V})^2}{9{,}6\,\Omega} = 60\,\text{W}.$$

**An halber Spannung,** $12\,\text{V}$, leistet derselbe Widerstand nur ein Viertel, und in einer Stunde setzt er bei $24\,\text{V}$ $60\,\text{Wh}$ um:

$$P = \frac{(12\,\text{V})^2}{9{,}6\,\Omega} = 15\,\text{W}, \qquad W = 60\,\text{W}\cdot1\,\text{h} = 60\,\text{Wh}.$$

**Im Bild:** Halber Turmdruck halbiert den Durchfluss durch dasselbe Rohr; Druck mal Durchfluss wird ein Viertel.
::::

## Belastbarkeit von Widerständen

Jeder Widerstand hat eine __Nennbelastbarkeit__ $P_\text{max}$, die größte Leistung, die er dauerhaft in Wärme umsetzen darf, ohne zu überhitzen; kleine
Bauformen vertragen typisch $0{,}25$ bis $0{,}6\,\text{W}$. Die Bedingung begrenzt bei gegebenem Widerstand Spannung und Strom:

$$P \le P_\text{max}, \qquad U \le \sqrt{P_\text{max}\,R}, \qquad I \le \sqrt{\frac{P_\text{max}}{R}}.$$

**So liest man das:** Im Diagramm Strom über Spannung (Bild 7.72 des Skripts) liegt der erlaubte Bereich unter der Hyperbel, auf der Spannung mal Strom
gleich $P_\text{max}$ ist. Die Kennlinie eines Widerstands, eine Gerade durch den Ursprung, schneidet sie im höchsten erlaubten Betriebspunkt: Ein großer
Widerstand verträgt viel Spannung, aber wenig Strom, ein kleiner umgekehrt.

**Im Bild:** Ein Rohr hält nur eine bestimmte Reibungswärme aus. Ein enges Rohr verträgt viel Druck, aber wenig Durchfluss, ein weites umgekehrt.

:::herleitung
**Spannung und Strom.** Aus den beiden Formen der Leistung am Widerstand:

$$\frac{U^2}{R} \le P_\text{max} \iff U \le \sqrt{P_\text{max}\,R}, \qquad R\,I^2 \le P_\text{max} \iff I \le \sqrt{\frac{P_\text{max}}{R}}.$$

**Die Grenzkurve.** Auf ihr ist $U I$ gleich $P_\text{max}$, also ist der Strom $P_\text{max}/U$: eine Hyperbel. Die Gerade des Widerstands, $I$ gleich
$U/R$, trifft sie dort, wo $U^2/R$ gleich $P_\text{max}$ ist, bei der Spannung aus der ersten Formel.
:::

::::beispiel Viertelwatt-Widerstände und ein LED-Vorwiderstand
**(a) Grenzen.** Für Widerstände mit $0{,}25\,\text{W}$ Nennbelastbarkeit:

| Widerstand | höchste Spannung | höchster Strom |
|---|---|---|
| $100\,\Omega$ | $5\,\text{V}$ | $50\,\text{mA}$ |
| $1\,\text{k}\Omega$ | $15{,}8\,\text{V}$ | $15{,}8\,\text{mA}$ |
| $10\,\text{k}\Omega$ | $50\,\text{V}$ | $5\,\text{mA}$ |

**(b) Ein Vorwiderstand.** Eine Leuchtdiode soll an einer $9$-V-Batterie mit $20\,\text{mA}$ leuchten, wobei an ihr $2\,\text{V}$ abfallen. Der
Vorwiderstand nimmt den Rest auf:

$$R_v = \frac{9\,\text{V} - 2\,\text{V}}{20\,\text{mA}} = 350\,\Omega, \qquad P_v = 7\,\text{V}\cdot20\,\text{mA} = 140\,\text{mW}.$$

Ein Viertelwatt-Widerstand reicht, er ist zu $56\,\%$ ausgelastet.

**Im Bild:** Durch das Vorschaltrohr soll ein fester Durchfluss; es nimmt den übrigen Druck auf, und seine Reibungswärme muss unter der Grenze bleiben.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/05-belastbarkeit · Vorlage: belastbarkeit-hyperbel
Nach Bild 7.72 des Skripts: ein Diagramm Strom über Spannung von $0$ bis $60\,\text{V}$ und $0$ bis $60\,\text{mA}$ mit der Hyperbel für $0{,}25\,\text{W}$,
der Bereich darunter hell, darüber rot schraffiert. Drei Widerstandsgeraden für $100\,\Omega$, $1\,\text{k}\Omega$ und $10\,\text{k}\Omega$ enden an der
Hyperbel bei $(5\,\text{V}, 50\,\text{mA})$, $(15{,}8\,\text{V}, 15{,}8\,\text{mA})$ und $(50\,\text{V}, 5\,\text{mA})$. Ein Regler fährt die Spannung hoch; ein
Punkt läuft auf der gewählten Geraden, ein Widerstandssymbol daneben glüht stärker und wird rot, sobald der Punkt die Hyperbel überschreitet. Kernaussage:
Jeder Widerstand hat einen höchsten Betriebspunkt, wo seine Gerade die Leistungsgrenze schneidet. (Rot = Grenze und Überlast, blau = Widerstandsgeraden,
orange = Betriebspunkt, grau = Achsen.)
:::

## Leitungsverluste und Hochspannung

Wird Leistung über eine Leitung zu einem Verbraucher übertragen, setzt auch der Widerstand der Leitung einen Teil um (Bild 7.73 des Skripts). Eine Quelle
mit der Spannung $U_q$ treibt den Strom $I$ durch eine Leitung mit dem Widerstand $R_\text{Kabel}$ beider Leiter zusammen und weiter durch den Verbraucher.
Am Kabel fällt die Spannung $U_\text{Kabel}$ ab, es setzt die __Verlustleistung__ $P_V$ um, und beim Verbraucher kommt die __Nutzleistung__ an:

$$U_\text{Kabel} = R_\text{Kabel}\,I, \qquad P_V = R_\text{Kabel}\,I^2, \qquad P_\text{Nutz} = (U_q - U_\text{Kabel})\,I, \qquad \frac{P_\text{Nutz}}{P_q} = 1 - \frac{U_\text{Kabel}}{U_q}.$$

Soll eine feste Leistung $P_q$ übertragen werden, kann man das mit hoher Spannung und kleinem Strom tun oder umgekehrt. Die Verluste hängen davon stark ab:

:::formel
$$P_V = R_\text{Kabel}\,\frac{P_q^2}{U_q^2}.$$
:::

**So liest man das:** Bei gleicher übertragener Leistung und gleichem Kabel sinken die Verluste mit dem Quadrat der Spannung: zehnfache Spannung, ein
Hundertstel Verlust. Das Skript vergleicht $220\,\text{V}$ mit $220\,\text{kV}$, ein Tausendstel des Stroms und ein Millionstel der Verluste. Deshalb
überträgt man große Leistungen über weite Strecken mit Hoch- und Höchstspannung und setzt die Spannung erst nahe am Verbraucher herab.

**Im Bild:** Eine Fernwasserleitung bringt dieselbe Leistung mit hohem Druck und kleinem Durchfluss viel verlustärmer als mit niedrigem Druck und großem.

:::herleitung
**Strom aus der Leistung.** Die Quelle gibt $P_q$ gleich $U_q I$ ab; der Strom ist also $P_q/U_q$, und eingesetzt in die Verlustleistung:

$$P_V = R_\text{Kabel}\,I^2 = R_\text{Kabel}\Big(\frac{P_q}{U_q}\Big)^2.$$

**Der Anteil beim Verbraucher.** Am Verbraucher liegt, was am Kabel nicht abfällt; durch beide fließt derselbe Strom:

$$\frac{P_\text{Nutz}}{P_q} = \frac{(U_q - U_\text{Kabel})\,I}{U_q\,I} = 1 - \frac{U_\text{Kabel}}{U_q}.$$
:::

::::beispiel Ein Megawatt über zwei Ohm
Ein Megawatt soll über eine Leitung übertragen werden, deren beide Leiter zusammen $2\,\Omega$ haben, einmal mit $10\,\text{kV}$ und einmal mit $110\,\text{kV}$.

**Mit 10 Kilovolt:**

$$I = \frac{1\,\text{MW}}{10\,\text{kV}} = 100\,\text{A}, \qquad P_V = 2\,\Omega\cdot(100\,\text{A})^2 = 20\,\text{kW}, \qquad U_\text{Kabel} = 200\,\text{V}.$$

Zwei Prozent gehen verloren, $98\,\%$ kommen an.

**Mit 110 Kilovolt:**

$$I = \frac{1\,\text{MW}}{110\,\text{kV}} \approx 9{,}09\,\text{A}, \qquad P_V = 2\,\Omega\cdot(9{,}09\,\text{A})^2 \approx 165\,\text{W}.$$

Elffache Spannung, ein Hunderteinundzwanzigstel der Verluste: weniger als zwei Zehntausendstel der Leistung. Das Stromnetz arbeitet mit Wechselspannung;
die Formeln gelten dann mit den Effektivwerten des nächsten Abschnitts.

**Im Bild:** Dieselbe Leistung, einmal als dicker Strom unter wenig Druck, einmal als dünner Strahl unter viel Druck — die Reibung im Rohr trifft vor allem
den dicken Strom.
::::

Die Spannungsebenen im deutschen Netz ordnen sich nach der Entfernung, über die sie Energie verteilen (Tabelle im Skript):

| Nennspannung | Bezeichnung | Entfernung | Aufgabe |
|---|---|---|---|
| $230/400\,\text{V}$ | Niederspannung | einige $100\,\text{m}$ | Versorgung von Haushalten und Gewerbe im Ort |
| $10\,\text{kV}$, $20\,\text{kV}$ | Mittelspannung | bis etwa $10$ bis $25\,\text{km}$ | Verteilung in Städten und auf dem Land |
| $110\,\text{kV}$ | Hochspannung | bis etwa $100\,\text{km}$ | Versorgung der Mittelspannungsnetze |
| $220\,\text{kV}$, $380\,\text{kV}$ | Höchstspannung | einige $100\,\text{km}$ bis über $1000\,\text{km}$ | Verbund im In- und Ausland |

Für die Niederspannung nennt das Skript noch $230/380\,\text{V}$; genormt sind heute $230\,\text{V}$ zwischen Außenleiter und Neutralleiter und $400\,\text{V}$
zwischen zwei Außenleitern.

## Leistung bei Sinusspannung

Das Stromnetz liefert Wechselspannung. An einem Widerstand $R$ liegt dann die Momentanspannung $u(t)$ mit dem __Scheitelwert__ $\hat u$, dem größten Wert,
und der __Kreisfrequenz__ $\omega$, dem $2\pi$-Fachen der Frequenz; der Strom $i(t)$ folgt ihr nach dem ohmschen Gesetz in jedem Augenblick:

$$u(t) = \hat u\cos(\omega t), \qquad i(t) = \frac{u(t)}{R} = \hat\imath\cos(\omega t), \qquad \hat\imath = \frac{\hat u}{R}.$$

Die Augenblicksleistung $u\,i$ schwankt zwischen null und $\hat u\,\hat\imath$, und zwar mit der doppelten Frequenz. Was zählt, ist ihr Mittelwert über eine
Periode $T$:

:::formel
$$P = \frac1T\int_0^T u(t)\,i(t)\,dt = \frac{\hat u^2}{2R} = \frac{\hat\imath^2 R}{2}.$$
:::

**So liest man das:** Die mittlere Leistung ist halb so groß wie die Spitzenleistung. Schreibt man sie wie bei Gleichstrom, mit dem __Effektivwert__ $\hat u/\sqrt2$,
wird daraus wieder $U^2/R$: Der Effektivwert ist die Gleichspannung, die am selben Widerstand dieselbe mittlere Leistung umsetzt. Die $230\,\text{V}$ der
Steckdose sind ein Effektivwert; der Scheitelwert ist um den Faktor $\sqrt2$ größer.

**Im Bild:** Ein Turm, dessen Wasserspiegel gleichmäßig auf und ab schwingt; das Rad arbeitet abwechselnd stark und gar nicht, im Mittel mit der Hälfte
der Spitze.

:::herleitung
**Quadrat des Kosinus.** Aus dem Additionstheorem $\cos(2x)$ gleich $2\cos^2 x - 1$ folgt

$$\cos^2(\omega t) = \frac12\big(1 + \cos(2\omega t)\big).$$

**Mitteln.** Eingesetzt, mit $u\,i$ gleich $u^2/R$; über eine volle Periode ist das Integral über $\cos(2\omega t)$ null, denn diese Funktion durchläuft
dabei zwei ganze Schwingungen:

$$P = \frac{1}{TR}\int_0^T \hat u^2\cos^2(\omega t)\,dt = \frac{\hat u^2}{2TR}\int_0^T \big(1 + \cos(2\omega t)\big)\,dt = \frac{\hat u^2}{2TR}\,T = \frac{\hat u^2}{2R}.$$

Mit $\hat u$ gleich $\hat\imath R$ folgt die zweite Form.
:::

::::beispiel Ein Heizlüfter an der Steckdose
Ein Heizlüfter nimmt an $230\,\text{V}$ eine Leistung von $2300\,\text{W}$ auf. Sein Widerstand, mit dem Effektivwert gerechnet, und die Scheitelwerte:

$$R = \frac{(230\,\text{V})^2}{2300\,\text{W}} = 23\,\Omega, \qquad \hat u = \sqrt2\cdot230\,\text{V} \approx 325\,\text{V}, \qquad \hat\imath = \frac{325\,\text{V}}{23\,\Omega} \approx 14{,}1\,\text{A}.$$

**Mit den Scheitelwerten** ergibt die Formel dieselbe Leistung, und die Spitzenleistung ist doppelt so groß:

$$P = \frac{(325\,\text{V})^2}{2\cdot23\,\Omega} \approx 2300\,\text{W}, \qquad \hat u\,\hat\imath \approx 4600\,\text{W}.$$

**Im Bild:** Ein schwingender Wasserspiegel, der im Mittel so viel leistet wie ein ruhender in der Höhe des Effektivwerts.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/05-sinusleistung · Vorlage: sinusleistung-mittelwert
Nach dem Bild auf Seite 136 des Skripts: oben eine Wechselspannungsquelle an einem Widerstand von $23\,\Omega$ mit den Zählpfeilen von $u(t)$ und $i(t)$.
Darunter drei Kurven über zwei Perioden: $u(t)$ mit dem Scheitelwert $325\,\text{V}$, $i(t)$ mit $14{,}1\,\text{A}$ und die Augenblicksleistung $p(t)$, die mit
doppelter Frequenz zwischen null und $4600\,\text{W}$ schwingt. Eine waagrechte Linie bei $2300\,\text{W}$ markiert den Mittelwert; ein Schieber füllt die
Flächen über der Linie in die Täler darunter, bis eine gleichmäßige Fläche entsteht. Daneben eine Gleichspannung von $230\,\text{V}$ am selben Widerstand
mit derselben Fläche. Kernaussage: Die mittlere Leistung ist die halbe Spitzenleistung; der Effektivwert ist die gleichwertige Gleichspannung. (Blau =
Spannung, rot = Strom, orange = Leistung und Mittelwert, grau = Achsen.)
:::

## Leistungsanpassung

Eine reale Spannungsquelle gibt Leistung an einen Verbraucher ab (Bild 7.74 des Skripts). Wie viel, hängt vom Verbraucher ab; das Skript fragt nach dem
Lastwiderstand, der die größte Leistung aufnimmt.

**Die Akteure:**

- die reale Spannungsquelle aus der Quellenspannung $U_q$ und dem Innenwiderstand $R_q$ (Artikel über ideale und reale Quellen), im Skript an dieser
  Stelle versehentlich als $(U_q, I_q)$ bezeichnet;
- der __Lastwiderstand__ $R_L$ und das Verhältnis $\alpha$ von Last- zu Innenwiderstand, eine Zahl ohne Einheit;
- der Strom im Kreis und die drei Leistungen: die der Quelle, $P_q$ gleich $U_q I$, die Verlustleistung im Innenwiderstand, $P_v$ gleich $R_q I^2$, und die
  Nutzleistung am Verbraucher, $P_L$ gleich $R_L I^2$;
- die __Kurzschlussleistung__ $P_K$, die Leistung, die die Quelle bei kurzgeschlossenen Klemmen aufbringt.

$$I = \frac{U_q}{R_q + R_L}, \qquad \alpha = \frac{R_L}{R_q}, \qquad P_K = \frac{U_q^2}{R_q}, \qquad P_q = P_v + P_L.$$

**Das Zusammenspiel:** *Bei welchem Lastwiderstand nimmt der Verbraucher die größte Leistung auf, und wie groß ist sie?*

:::formel Satz
$$P_L = \frac{U_q^2\,R_L}{(R_q + R_L)^2} = P_K\,\frac{\alpha}{(1 + \alpha)^2},$$

$$R_L = R_q:\qquad P_{L,\max} = \frac{P_K}{4} = \frac{U_q^2}{4R_q}.$$
:::

**So liest man das:** Das ist die __Leistungsanpassung__: Der Verbraucher nimmt die größte Leistung auf, wenn sein Widerstand gleich dem Innenwiderstand
der Quelle ist, und dann ein Viertel der Kurzschlussleistung. Ist er kleiner, fließt zwar viel Strom, aber an ihm liegt wenig Spannung; ist er größer, liegt
viel Spannung an, aber es fließt wenig Strom. Bei Anpassung liegt an ihm die halbe Quellenspannung, und es fließt der halbe Kurzschlussstrom.

Das Verhältnis zur Kurzschlussleistung hängt nur von $\alpha$ ab, jede Quelle hat dieselbe Kurve (Bild 7.75). Sie ist symmetrisch in einem bemerkenswerten
Sinn: Ein Lastwiderstand $\alpha R_q$ und einer $R_q/\alpha$ nehmen dieselbe Leistung auf. Halber und doppelter Innenwiderstand liefern also gleich viel,
wie im Skript $50\,\Omega$ und $200\,\Omega$ an einer Quelle mit $100\,\Omega$.

**Im Bild:** Das Rad holt am meisten heraus, wenn es genauso stark bremst wie die Zuleitung. Dann liegt am Rad der halbe Turmdruck, und es fließt der halbe
Durchfluss, den ein offenes Rohr zuließe.

:::herleitung
**Die Leistung am Verbraucher.** Mit dem Strom der Reihenschaltung:

$$P_L = R_L\,I^2 = \frac{U_q^2\,R_L}{(R_q + R_L)^2} = \frac{U_q^2}{R_q}\cdot\frac{R_L/R_q}{(1 + R_L/R_q)^2} = P_K\,\frac{\alpha}{(1 + \alpha)^2}.$$

**Das Maximum mit der Ableitung.** Nach der Quotientenregel, wie im Skript:

$$\frac{dP_L}{d\alpha} = P_K\,\frac{(1 + \alpha)^2 - 2\alpha\,(1 + \alpha)}{(1 + \alpha)^4} = P_K\,\frac{1 - \alpha}{(1 + \alpha)^3}.$$

Die Ableitung ist für $\alpha$ kleiner als eins positiv und für $\alpha$ größer als eins negativ; die Leistung steigt also bis zu $\alpha$ gleich eins und fällt
danach. Dort ist $P_L$ gleich $P_K/4$.

**Ohne Ableitung.** Teilt man Zähler und Nenner durch $R_L$, steht im Nenner eine Summe, die man nach unten abschätzen kann:

$$P_L = \frac{U_q^2}{\frac{R_q^2}{R_L} + 2R_q + R_L}, \qquad \frac{R_q^2}{R_L} + R_L - 2R_q = \frac{(R_L - R_q)^2}{R_L} \ge 0.$$

Der Nenner ist also mindestens $4R_q$, und gleich $4R_q$ genau für $R_L$ gleich $R_q$.

**Symmetrie.** Ersetzt man $\alpha$ durch seinen Kehrwert und erweitert mit $\alpha^2$, entsteht derselbe Ausdruck:

$$\frac{1/\alpha}{(1 + 1/\alpha)^2} = \frac{\alpha}{(\alpha + 1)^2}.$$

**Spannung und Strom bei Anpassung.** Mit $R_L$ gleich $R_q$ ist der Strom $U_q/(2R_q)$, die Hälfte des Kurzschlussstroms, und am Verbraucher liegt die
halbe Quellenspannung. Im Bild: Halber Druck mal halber Durchfluss ist ein Viertel des Produkts aus vollem Druck und vollem Durchfluss.
:::

::::beispiel Ein thermoelektrischer Generator
Ein thermoelektrischer Generator erzeugt aus einem Temperaturunterschied eine Spannung und verhält sich bei fester Temperatur in guter Näherung wie eine
lineare Quelle:

$$U_q = 2{,}4\,\text{V}, \qquad R_q = 2\,\Omega, \qquad P_K = \frac{(2{,}4\,\text{V})^2}{2\,\Omega} = 2{,}88\,\text{W}.$$

**Fünf Lasten:**

| Last $R_L$ | $\alpha$ | Strom | Leistung $P_L$ | Leistung der Quelle | Wirkungsgrad |
|---|---|---|---|---|---|
| $0{,}5\,\Omega$ | $0{,}25$ | $0{,}96\,\text{A}$ | $0{,}46\,\text{W}$ | $2{,}30\,\text{W}$ | $20\,\%$ |
| $1\,\Omega$ | $0{,}5$ | $0{,}8\,\text{A}$ | $0{,}64\,\text{W}$ | $1{,}92\,\text{W}$ | $33\,\%$ |
| $2\,\Omega$ | $1$ | $0{,}6\,\text{A}$ | $0{,}72\,\text{W}$ | $1{,}44\,\text{W}$ | $50\,\%$ |
| $4\,\Omega$ | $2$ | $0{,}4\,\text{A}$ | $0{,}64\,\text{W}$ | $0{,}96\,\text{W}$ | $67\,\%$ |
| $8\,\Omega$ | $4$ | $0{,}24\,\text{A}$ | $0{,}46\,\text{W}$ | $0{,}58\,\text{W}$ | $80\,\%$ |

**Das Maximum** liegt bei $2\,\Omega$, mit einem Viertel der Kurzschlussleistung:

$$P_{L,\max} = \frac{(2{,}4\,\text{V})^2}{4\cdot2\,\Omega} = 0{,}72\,\text{W}.$$

Je $1\,\Omega$ und $4\,\Omega$ sowie $0{,}5\,\Omega$ und $8\,\Omega$ liefern gleich viel, wie es die Symmetrie verlangt; der Wirkungsgrad, der Anteil der
genutzten an der aufgewendeten Leistung, steigt dagegen stetig.

**Im Bild:** Fünf verschieden schwergängige Räder an demselben Turm; das mittlere holt am meisten heraus, die beiden äußeren Paare gleich viel.
::::

Was für eine einzelne reale Quelle gilt, gilt für jedes lineare Netz: Von zwei Klemmen aus ist es eine Ersatzspannungsquelle mit $U_i$ und $R_i$ (Artikel
über Ersatzquellen), und angepasst ist ein Verbraucher, dessen Widerstand gleich $R_i$ ist. Das Skript rechnet das an einer Quelle $U_q$ mit $R_q$ und einem
Widerstand $R$ parallel zu den Klemmen vor (Bild 7.77). Über die Ersatzquelle geht es kurz:

$$U_i = \frac{R}{R_q + R}\,U_q, \qquad R_i = \frac{R_q R}{R_q + R}, \qquad P_{L,\max} = \frac{U_i^2}{4R_i} = \frac{R}{4R_q\,(R_q + R)}\,U_q^2.$$

Bezogen auf die eigentliche Quelle $U_q$ ist der Wirkungsgrad dann kleiner als die Hälfte, weil auch $R$ Leistung verbraucht:

$$\eta = \frac12\cdot\frac{R}{2R_q + R}.$$

:::herleitung
**Anpassung an die Ersatzquelle.** Die Leerlaufspannung ist die des unbelasteten Teilers, der Innenwiderstand der des Netzes mit kurzgeschlossener
Quelle, $R_q$ parallel zu $R$. Eingesetzt in $U_i^2/(4R_i)$:

$$P_{L,\max} = \frac{R^2\,U_q^2}{(R_q + R)^2}\cdot\frac{R_q + R}{4R_q R} = \frac{R}{4R_q\,(R_q + R)}\,U_q^2.$$

**Die Leistung der Quelle.** Bei Anpassung liegt $R_L$ gleich $R_i$ parallel zu $R$. Mit $R_i$ eingesetzt und mit $R_q + R$ erweitert ist diese
Parallelschaltung

$$\frac{R\,R_i}{R + R_i} = \frac{R^2R_q}{R\,(R_q + R) + R_qR} = \frac{R\,R_q}{2R_q + R},$$

und der Gesamtwiderstand vor der Quelle und ihre Leistung sind

$$R_\text{ges} = R_q + \frac{R\,R_q}{2R_q + R} = \frac{2R_q\,(R_q + R)}{2R_q + R}, \qquad P_q = \frac{U_q^2}{R_\text{ges}} = \frac{(2R_q + R)\,U_q^2}{2R_q\,(R_q + R)}.$$

**Der Wirkungsgrad.** Der Quotient der beiden Leistungen:

$$\eta = \frac{P_{L,\max}}{P_q} = \frac{R}{4R_q\,(R_q + R)}\cdot\frac{2R_q\,(R_q + R)}{2R_q + R} = \frac12\cdot\frac{R}{2R_q + R}.$$

Für jedes endliche $R$ ist der zweite Faktor kleiner als eins. Das Skript kommt über die Spannung am Verbraucher auf einem längeren Weg zum selben
Ergebnis.
:::

::::beispiel Anpassung an das Referenznetz der Ersatzquellen
Das Netz aus dem Artikel über Ersatzquellen: $U_q$ speist über $R_1$ einen Mittelknoten M, $R_2$ führt von M nach B, $R_3$ von M nach A. Seine Ersatzquelle hat
$4\,\text{V}$ und $4\,\text{k}\Omega$.

$$U_q = 12\,\text{V}, \qquad R_1 = 6\,\text{k}\Omega, \qquad R_2 = 3\,\text{k}\Omega, \qquad R_3 = 2\,\text{k}\Omega.$$

**Angepasst** ist eine Last von $4\,\text{k}\Omega$; sie nimmt

$$P_{L,\max} = \frac{(4\,\text{V})^2}{4\cdot4\,\text{k}\Omega} = 1\,\text{mW}$$

auf. Mit $2\,\text{k}\Omega$ oder $8\,\text{k}\Omega$ wären es je $0{,}89\,\text{mW}$.

**Was die Quelle aufbringt.** Die Rechnung mit dem ganzen Netz, wie im Artikel über Ersatzquellen, ergibt bei der angepassten Last einen Quellstrom von
$1{,}5\,\text{mA}$:

$$P_q = 12\,\text{V}\cdot1{,}5\,\text{mA} = 18\,\text{mW}, \qquad \eta = \frac{1\,\text{mW}}{18\,\text{mW}} \approx 5{,}6\,\%.$$

Der Rest wird in $R_1$, $R_2$ und $R_3$ zu Wärme; die Ersatzquelle allein hätte $50\,\%$ vorgetäuscht, denn sie ist nur an den Klemmen gleichwertig.

**Im Bild:** Hinter dem Hahn liegt ein ganzes Netz mit Abzweigen, die ständig Wasser ablaufen lassen; angepasst bekommt das Rad zwar das Maximum, aber das
meiste Wasser läuft woanders ab.
::::

## Wirkungsgrad

Die größte Leistung zu holen ist nicht dasselbe, wie sparsam mit der Energie umzugehen. Wie gut eine Übertragung die aufgewendete Leistung nutzt, misst der
__Wirkungsgrad__:

:::formel Definition
$$\eta = \frac{\text{genutzte Leistung}}{\text{gesamte aufgewendete Leistung der Quelle}}.$$
:::

**So liest man das:** Für die reale Quelle am Lastwiderstand ist die genutzte Leistung $P_L$ und die aufgewendete $P_q$:

$$\eta = \frac{P_L}{P_q} = \frac{R_L}{R_L + R_q} = \frac{\alpha}{1 + \alpha}.$$

Der Wirkungsgrad steigt mit dem Lastwiderstand stetig an (Bild 7.76): Bei Kurzschluss ist er null, bei Anpassung die Hälfte, und für einen Lastwiderstand
weit über dem Innenwiderstand kommt er der Eins nahe — dann ist aber auch die Leistung klein. Größte Leistung und größter Wirkungsgrad schließen sich aus,
und die Anwendung entscheidet, worauf es ankommt:

- **Nachrichtentechnik**, etwa ein Funkempfänger: Die Leistungen sind winzig, im Bereich von Mikrowatt. Es zählt, möglichst viel davon aufzunehmen; man
  passt an, und der Wirkungsgrad spielt keine Rolle.
- **Energietechnik**, etwa eine Autobatterie oder das Stromnetz: Die Leistungen liegen bei Kilowatt und mehr. Es zählt der Wirkungsgrad; der
  Innenwiderstand wird so klein wie möglich gehalten, weit unter dem Lastwiderstand.

**Im Bild:** Ein schwergängiges Rad lässt wenig Wasser durch, aber fast der ganze Druck liegt an ihm; die Zuleitung verliert kaum etwas.

:::herleitung
**Gleicher Strom.** Durch Quelle und Verbraucher fließt derselbe Strom; die Leistungen sind $R_L I^2$ und $U_q I$, und mit dem Strom der Reihenschaltung:

$$\eta = \frac{R_L\,I^2}{U_q\,I} = \frac{R_L\,I}{U_q} = \frac{R_L}{R_q + R_L}.$$

Teilt man durch $R_q$, steht $\alpha/(1 + \alpha)$ da; diese Funktion wächst mit $\alpha$ und strebt gegen eins. Bei Anpassung, mit $\alpha$ gleich eins, ist
sie $1/2$. Im Bild: Der Anteil des Drucks, der am Rad liegt, ist der Anteil der Leistung, die am Rad ankommt, denn durch Zuleitung und Rad fließt dasselbe
Wasser.
:::

::::beispiel Der Akku eines E-Bikes
Ein E-Bike-Akku mit Zuleitungen hat einen Innenwiderstand von $0{,}25\,\Omega$:

$$U_q = 36\,\text{V}, \qquad R_q = 0{,}25\,\Omega.$$

**(a) Der Motor** zieht beim Anfahren $15\,\text{A}$:

$$P_q = 36\,\text{V}\cdot15\,\text{A} = 540\,\text{W}, \qquad P_v = (15\,\text{A})^2\cdot0{,}25\,\Omega \approx 56{,}3\,\text{W}, \qquad \eta = 1 - \frac{56{,}3\,\text{W}}{540\,\text{W}} \approx 89{,}6\,\%.$$

An den Klemmen liegen dann nur noch $32{,}25\,\text{V}$.

**(b) Das Licht** zieht $0{,}3\,\text{A}$:

$$P_v = (0{,}3\,\text{A})^2\cdot0{,}25\,\Omega = 0{,}0225\,\text{W}, \qquad \eta = 1 - \frac{0{,}0225\,\text{W}}{10{,}8\,\text{W}} \approx 99{,}8\,\%.$$

Bei großem Strom kostet der Innenwiderstand einen spürbaren Teil, bei kleinem fast nichts. Das Skript zeigt dasselbe an einer Autobatterie beim Anlassen
und mit dem Parklicht; sein Bild 7.78 zeigt dabei die belastete Batterie, nicht, wie die Unterschrift sagt, ihren Ladevorgang.

**Im Bild:** Ein Turm mit weiter Zuleitung: Wer viel zapft, verliert in der Leitung merklich Druck, wer wenig zapft, merkt nichts.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/05-anpassung-wirkungsgrad · Vorlage: anpassung-wirkungsgrad
Nach Bild 7.74 bis 7.76 des Skripts: oben die reale Quelle mit $U_q = 2{,}4\,\text{V}$ und $R_q = 2\,\Omega$ an einem verstellbaren Lastwiderstand $R_L$, mit
den Zählpfeilen von $I$, $U_{Rq}$ und $U_L$. Darunter zwei Kurven über $\alpha$ von $0$ bis $10$: $P_L/P_K$ mit dem Maximum $0{,}25$ bei $\alpha$ gleich eins und
der Wirkungsgrad $\eta$, der von null gegen eins steigt und bei $\alpha$ gleich eins die Hälfte erreicht. Ein Regler verschiebt $R_L$; zwei Balken zeigen die
Leistung im Innenwiderstand und im Verbraucher, und eine gestrichelte Linie verbindet die gleich hohen Punkte bei $\alpha$ und $1/\alpha$. Kernaussage:
Größte Leistung bei Anpassung mit $50\,\%$, hoher Wirkungsgrad nur weit darüber. (Rot = Quelle und Leistungskurve, blau = Wirkungsgrad, orange = Balken
der Leistungen, grau = Achsen, gestrichelt = Symmetrielinie.)
:::

## Bedeutung und Ausblick

Leistungsanpassung ist das tägliche Brot der Nachrichten- und Hochfrequenztechnik: Antennen, Kabel, Verstärker und Messgeräte werden auf einen gemeinsamen
Widerstand abgestimmt, meist $50\,\Omega$, und Dämpfungsglieder wie das im Artikel über die Stern-Dreieck-Transformation halten diese Anpassung an beiden
Seiten aufrecht. In der Energietechnik wäre Anpassung dagegen ein Fehler: Ein angepasstes Kraftwerk verlöre die Hälfte seiner Leistung im eigenen
Innenwiderstand und lieferte den halben Kurzschlussstrom, einen riesigen Strom — wirtschaftlich und technisch undenkbar. Auch ein Audioverstärker hat einen Innenwiderstand weit unter dem eines Lautsprechers mit $4$ oder
$8\,\Omega$ und ist bewusst nicht angepasst.

Bei Wechselstrom mit Spulen und Kondensatoren wird die Bedingung zur Anpassung komplexer Widerstände, ein Thema der Wechselstromtechnik. Der nächste
Artikel beginnt ein neues Kapitel: Mit dem __Maschenstromverfahren__ lassen sich auch große Netze systematisch berechnen, Masche für Masche.

:::kern
- Energie ist das Zeitintegral von Spannung mal Strom, bei Gleichstrom $W=UI\,\Delta t$; gemessen in Joule, Wattsekunden oder Kilowattstunden.
- Leistung ist Energie pro Zeit, $P=UI$; am Widerstand $RI^2$ oder $U^2/R$, quadratisch in Strom und Spannung.
- Ein Widerstand darf dauerhaft höchstens seine Nennbelastbarkeit in Wärme umsetzen.
- Bei gleicher übertragener Leistung sinken die Leitungsverluste mit dem Quadrat der Spannung: $P_V=R_\text{Kabel}P_q^2/U_q^2$.
- Bei Sinusspannung ist die mittlere Leistung $\hat u^2/(2R)$, die halbe Spitzenleistung.
- Leistungsanpassung: Die größte Leistung $U_q^2/(4R_q)$ nimmt ein Verbraucher mit $R_L=R_q$ auf.
- Wirkungsgrad: $\eta=R_L/(R_L+R_q)$, bei Anpassung die Hälfte, für $R_L\gg R_q$ nahe eins.
- Die Nachrichtentechnik passt an, die Energietechnik strebt nach hohem Wirkungsgrad.
:::

:::quiz
F: Wie viel Energie gibt eine Ladung ab, die eine Spannung durchläuft, und wie viel setzt ein Gleichstromverbraucher in einer Zeit um?
A: Die Energie $dW=U_{12}\,dQ$, denn Spannung ist Energie pro Ladung; mit $dQ=I\,dt$ folgt $W=\int UI\,dt$, bei Gleichstrom $W=UI\,\Delta t$. Die Heckscheibenheizung mit $12\,\text{V}$ und $12\,\text{A}$ setzt in $10$ Minuten $86{,}4\,\text{kJ}$ um, also $0{,}024\,\text{kWh}$, und dabei fließen $2\,\text{Ah}$ durch sie.
F: Was ist Leistung, und warum wächst sie am Widerstand quadratisch mit der Spannung?
A: Energie pro Zeit, $P=W/\Delta t$, bei Gleichstrom $P=UI$. Am Widerstand ist mit dem ohmschen Gesetz $P=U^2/R$: Doppelte Spannung bringt doppelten Strom, das Produkt wird vierfach. Der Heizwiderstand für $24\,\text{V}$ und $60\,\text{W}$ leistet an $12\,\text{V}$ nur $15\,\text{W}$.
F: Was begrenzt die Nennbelastbarkeit eines Widerstands, und wie findet man seine Grenzen?
A: Die Wärme, die er dauerhaft abführen kann. Aus $U^2/R\le P_\text{max}$ und $RI^2\le P_\text{max}$ folgen $U\le\sqrt{P_\text{max}R}$ und $I\le\sqrt{P_\text{max}/R}$; ein Viertelwatt-Widerstand mit $1\,\text{k}\Omega$ verträgt $15{,}8\,\text{V}$ und $15{,}8\,\text{mA}$. Der LED-Vorwiderstand mit $350\,\Omega$ setzt $140\,\text{mW}$ um und ist damit zu $56\,\%$ ausgelastet.
F: Warum überträgt man große Leistungen mit Hochspannung?
A: Bei gleicher Leistung ist der Strom $P_q/U_q$, und die Leitungsverluste sind $R_\text{Kabel}P_q^2/U_q^2$, sinken also mit dem Quadrat der Spannung. Ein Megawatt über $2\,\Omega$ verliert mit $10\,\text{kV}$ $20\,\text{kW}$, mit $110\,\text{kV}$ nur $165\,\text{W}$.
F: Warum ist die mittlere Leistung bei Sinusspannung die Hälfte der Spitzenleistung, und was ist der Effektivwert?
A: Die Augenblicksleistung ist proportional zu $\cos^2(\omega t)$, und das ist $\frac12(1+\cos(2\omega t))$; der Kosinusanteil mittelt sich über eine Periode heraus, also ist $P=\hat u^2/(2R)$. Der Effektivwert $\hat u/\sqrt2$ ist die Gleichspannung mit derselben mittleren Leistung; zu $230\,\text{V}$ gehört ein Scheitelwert von $325\,\text{V}$, am Heizlüfter mit $23\,\Omega$ also $2300\,\text{W}$.
F: Bei welchem Lastwiderstand gibt eine reale Quelle die größte Leistung ab, und wie zeigt man das?
A: Bei $R_L=R_q$, mit $U_q^2/(4R_q)$, einem Viertel der Kurzschlussleistung. Mit der Ableitung: $\frac{dP_L}{d\alpha}=P_K\frac{1-\alpha}{(1+\alpha)^3}$ wechselt bei $\alpha=1$ das Vorzeichen. Ohne Ableitung: Im Nenner von $P_L=U_q^2/(R_q^2/R_L+2R_q+R_L)$ ist $R_q^2/R_L+R_L$ mindestens $2R_q$, denn die Differenz ist $(R_L-R_q)^2/R_L$.
F: Warum liefern beim thermoelektrischen Generator mit $2\,\Omega$ die Lasten $1\,\Omega$ und $4\,\Omega$ dieselbe Leistung?
A: Das Verhältnis $P_L/P_K=\alpha/(1+\alpha)^2$ ändert sich nicht, wenn man $\alpha$ durch $1/\alpha$ ersetzt. Halber und doppelter Innenwiderstand ergeben beide $0{,}64\,\text{W}$, das Maximum bei $2\,\Omega$ sind $0{,}72\,\text{W}$; der Wirkungsgrad ist dabei $33\,\%$, $50\,\%$ und $67\,\%$.
F: Was ist der Wirkungsgrad, und warum schließen sich größte Leistung und größter Wirkungsgrad aus?
A: Genutzte durch aufgewendete Leistung; an der realen Quelle $\eta=R_L/(R_L+R_q)$, denn durch beide Widerstände fließt derselbe Strom. Bei Anpassung ist er die Hälfte, nahe eins erst für $R_L\gg R_q$, wo die Leistung klein ist. Die Nachrichtentechnik passt deshalb an, die Energietechnik hält den Innenwiderstand klein; der E-Bike-Akku mit $0{,}25\,\Omega$ hat bei $15\,\text{A}$ noch $89{,}6\,\%$.
F: Wie passt man einen Verbraucher an ein ganzes Netz an, und welchen Wirkungsgrad hat das?
A: Man bestimmt die Ersatzquelle und wählt $R_L=R_i$; die Leistung ist dann $U_i^2/(4R_i)$. Bezogen auf die eigentliche Quelle kann der Wirkungsgrad weit unter $50\,\%$ liegen, weil die übrigen Widerstände mitverbrauchen: beim Teiler aus $R_q$ und $R$ ist er $\frac12\cdot\frac{R}{2R_q+R}$, beim Referenznetz mit $12\,\text{V}$ nur $1\,\text{mW}$ von $18\,\text{mW}$, gut $5{,}6\,\%$.
F: Welche Ungenauigkeiten stehen im Skript bei Energie und Leistung?
A: Die Spannung beim Verschieben der Ladung ist als $\varphi_2-\varphi_1$ geschrieben; die abgegebene Energie zählt mit $U_{12}=\varphi_1-\varphi_2$ positiv. Das Newtonmeter ist eine Einheit der Arbeit und des Drehmoments, nicht der mechanischen Leistung. Die Niederspannung ist heute $230/400\,\text{V}$ statt $230/380\,\text{V}$; die Quelle in 7.9 heißt einmal $(U_q, I_q)$ statt $(U_q, R_q)$, und Bild 7.78 zeigt die belastete Batterie, keinen Ladevorgang.
:::
