---
title: Das elektrische Feld und die Feldstärke
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Elektrische Feldstärke und Potenzial
order: 30100
summary: Von Grund auf – wie Ladungen über den leeren Raum aufeinander wirken. Leitbild ist das Schwerefeld als Vorbild: So wie die Erde jedem Kilogramm eine Kraft zuteilt, teilt eine Ladung jedem Coulomb eine Kraft zu, die Feldstärke. Mit den elektrischen Erscheinungen von der Reibungselektrizität bis Ørsted, Faraday und Maxwell, der Definition der Feldstärke als Grenzwert, dem Coulombschen Gesetz samt richtiger Richtung des Abstandsvektors, der Genauigkeit des 1/r²-Gesetzes, dem Feld einer Punktladung, der Überlagerung, den Regeln für Feldlinien und typischen Feldstärken. Mit Beispiel-Seite.
tags: elektrisches Feld, Feldstärke, Coulomb, Probeladung, Feldlinien, Plattenkondensator, homogenes Feld
---

## Anschaulich

Reibt man einen Luftballon an den Haaren, richten sich die Haare danach zum Ballon auf, ohne ihn zu berühren. Ein Blitz springt
durch kilometerlange Luft. Elektrische Wirkungen reichen durch den Raum — wie aber „weiß" eine Ladung von einer anderen?

**Das Leitbild dieses Artikels:** **das Schwerefeld als Vorbild**. Ein Stein fällt, weil die Erde durch den leeren Raum auf ihn
wirkt. Man beschreibt das, indem man jedem Punkt einen Pfeil zuordnet, die Kraft pro Kilogramm, die dort auf jeden Körper wirkt:
das Schwerefeld. An der Erdoberfläche ist es rund $9{,}81\,\frac{\text{N}}{\text{kg}}$, senkrecht nach unten.

Mit Ladungen geht man genauso vor. Jede Ladung ordnet dem Raum um sich herum an jedem Punkt einen Pfeil zu, die Kraft pro Coulomb
auf eine positive Ladung dort: das __elektrische Feld__. Eine zweite Ladung spürt dann nicht die erste direkt, sondern das Feld an
ihrem eigenen Ort.

Drei Dinge unterscheiden das elektrische Feld vom Schwerefeld, und sie ziehen sich durch den ganzen Artikel. Es gibt zwei Sorten
Ladung, also Anziehung **und** Abstoßung. Elektrische Kräfte sind unvorstellbar viel stärker. Und man kann ein elektrisches Feld
abschirmen, ein Schwerefeld nicht.

:::grafik
Szene: get1/elektrische-feldstaerke-und-potenzial/01-schwerefeld-und-e-feld · Vorlage: feld-vergleich
Links die Erde mit Feldpfeilen, die überall zu ihrem Mittelpunkt zeigen, und ein kleiner Körper mit seinem Kraftpfeil. Rechts eine
positive Ladung mit Feldpfeilen, die radial nach außen zeigen, und eine kleine Probeladung mit ihrem Kraftpfeil. Ein Regler
verdoppelt die Masse bzw. die Probeladung: Der Kraftpfeil wird doppelt so lang, der Feldpfeil am Ort bleibt gleich. Ein zweiter
Regler macht die Probeladung negativ, und ihr Kraftpfeil kehrt sich um. Kernaussage: Das Feld ist Kraft pro Masse bzw. Kraft pro
Ladung und gehört zum Ort, nicht zum Probekörper. (Blau = Feldpfeile, rot = Probekörper und Probeladung, orange = Kraftpfeile,
grau = Erde und Achsen.)
:::

## Elektrische Erscheinungen

Lange kannte man elektrische Wirkungen nur als Kuriositäten: die __Reibungselektrizität__, bei der geriebene Körper leichte Dinge
anziehen; den Blitz als gewaltige elektrische Entladung; daneben, scheinbar ganz unabhängig, den Magnetismus. Drei Entdeckungen
haben diese Gebiete zum __Elektromagnetismus__ zusammengeführt.

**1820, Ørsted.** Hans Christian Ørsted bemerkte, dass eine Kompassnadel ausschlägt, wenn neben ihr ein Strom fließt. Ein Strom
erzeugt also ein Magnetfeld, beschrieben durch die __magnetische Feldstärke__ $\vec H$. Seine Richtung gibt die __Rechte-Faust-Regel__: Zeigt der
Daumen der rechten Hand in die technische Stromrichtung, von Plus nach Minus, so zeigen die gekrümmten Finger in die Richtung der
Feldlinien, die den Leiter ringförmig umschließen.

:::grafik
Szene: get1/elektrische-feldstaerke-und-potenzial/01-oersted-rechte-faust · Vorlage: leiter-magnetfeld-ringe
Ein senkrechter Leiter, durch den ein Strom $I$ nach oben fließt, dazu eine rechte Hand, deren Daumen in Stromrichtung zeigt. Um den
Leiter liegen kreisförmige Feldlinien von $\vec H$ mit Pfeilen in Richtung der gekrümmten Finger; auf einer Linie stehen kleine
Kompassnadeln tangential. Ein Schalter kehrt den Strom um, und Nadeln und Pfeile drehen sich mit. Kernaussage: Ein Strom erzeugt ein
ringförmiges Magnetfeld, dessen Umlaufsinn die Rechte-Faust-Regel angibt. (Rot = Leiter und Strompfeil, blau = Feldlinien, orange =
Hand und Kompassnadeln, grau = Hintergrund.)
:::

**1831, Faraday.** Michael Faraday kehrte den Gedanken um: Kann ein Magnetfeld einen Strom erzeugen? Bewegte er einen Magneten in
einer Spule, entstand an ihren Anschlüssen eine Spannung. Im zweiten Versuch wickelte er zwei Spulen auf einen gemeinsamen
Eisenring; schaltete er an der einen eine Batterie ein, schlug an der anderen ein Strommesser aus. Ursache ist in beiden Fällen
die __Änderung des magnetischen Flusses__ $\Phi$ durch die Spule, und für eine Spule mit $N$ Windungen gilt das __Induktionsgesetz__

$$U_{\text{ind}} = -N\,\frac{d\Phi}{dt}.$$

**So liest man das:** Die induzierte Spannung ist umso größer, je schneller sich der Fluss ändert und je mehr Windungen die Spule
hat. Das Minuszeichen drückt die __Lenzsche Regel__ aus: Die induzierte Spannung treibt einen Strom, dessen Magnetfeld der
Flussänderung entgegenwirkt. Das Gesetz ist ein Erfahrungssatz; seine genauere Behandlung geht über den Rahmen dieses Artikels
hinaus.

::::beispiel Induktion in Zahlen
Eine Spule mit $200$ Windungen; der Fluss durch sie steigt in $0{,}1\,\text{s}$ gleichmäßig um $5\,\text{mWb}$. Die Änderung pro Zeit
und die induzierte Spannung:

$$\frac{d\Phi}{dt} = \frac{5\cdot10^{-3}\,\text{Wb}}{0{,}1\,\text{s}} = 0{,}05\,\frac{\text{Wb}}{\text{s}}, \qquad U_{\text{ind}} = -200\cdot0{,}05\,\frac{\text{Wb}}{\text{s}} = -10\,\text{V}.$$

Ein Weber pro Sekunde ist ein Volt, denn das Weber ist eine Voltsekunde. Der Betrag ist $10\,\text{V}$; das Vorzeichen sagt, dass die
Spannung der Flussänderung entgegenwirkt. Ändert sich der Fluss zehnmal so schnell, sind es $100\,\text{V}$.

**Im Bild:** Nicht der Fluss selbst erzeugt die Spannung, sondern seine Änderung. Ein ruhender Magnet in der Spule tut nichts.
::::

**1864, Maxwell.** James Clerk Maxwell fasste alle elektrischen und magnetischen Erscheinungen in vier Gleichungen zusammen. Für
sie reicht die Mathematik des ersten Semesters noch nicht; ihre Aussagen in Worten:

- Elektrische Ladungen sind Quellen und Senken des elektrischen Felds — dort beginnen und enden seine Feldlinien.
- Das Magnetfeld hat keine Quellen; seine Feldlinien sind geschlossen.
- Ein sich zeitlich änderndes Magnetfeld erzeugt ein elektrisches Wirbelfeld — das ist Faradays Induktion.
- Ströme und sich ändernde elektrische Felder erzeugen Magnetfelder — das ist Ørsteds Beobachtung, von Maxwell ergänzt.

**Im Bild:** Hier hat das Schwerefeld kein Gegenstück. Bewegte Massen erzeugen kein merkliches zweites Feld, bewegte Ladungen
dagegen ein Magnetfeld.

**Reibungselektrizität im Versuch.** Reibt man einen Glasstab mit einem Seidentuch und einen Hartgummistab mit einem Fell, so
ziehen sich die beiden Stäbe an, während zwei geriebene Hartgummistäbe einander abstoßen. Beim Reiben gehen Elektronen von einem
Körper auf den anderen über. Der Glasstab hat danach einen Mangel an Elektronen, der Hartgummistab einen Überschuss. Welcher Körper
welche Ladung bekommt, hängt von der Materialpaarung ab.

Historisch hieß die Ladung des Glases „glasige", die des Hartgummis „harzige" Elektrizität (Du Fay, 1733). Benjamin Franklin
führte um 1750 die Namen **positiv** und **negativ** ein: Ein Elektronenmangel ist positive, ein Überschuss negative Ladung.

Die Folgerung aus dem Versuch:

- Elektrisch geladene Körper üben Kräfte aufeinander aus, auch ohne Berührung.
- Ladungen gleichen Vorzeichens stoßen sich ab, Ladungen verschiedenen Vorzeichens ziehen sich an.
- Beim Reiben entsteht keine Ladung, sie wird nur verschoben: Die Summe aller positiven und negativen Ladungen bleibt null. Das ist
  der __Ladungserhaltungssatz__.

Zur Erklärung der Fernwirkung nimmt man, wie bei der Gravitation, ein Feld an.

**Im Bild:** Beim Schwerefeld gibt es nur Anziehung, weil es nur eine Sorte Masse gibt. Bei Ladungen gibt es zwei Sorten, und
daraus entstehen Anziehung und Abstoßung.

## Die elektrische Feldstärke

Eine erste Definition betrifft den Raum: Das __elektrische Feld__ ist der Raum, in dem auf eine Ladung eine Kraft ausgeübt wird. Um es
zu messen, bringt man eine kleine __Probeladung__ $Q$ an einen Punkt und misst die Kraft $\vec F$ auf sie. Die Kraft ist proportional
zur Probeladung; teilt man durch sie, bleibt eine Größe, die nur noch vom Ort abhängt, die __elektrische Feldstärke__:

:::formel Definition
$$\vec E := \lim_{Q\to0}\frac{\vec F}{Q}, \qquad \vec F = Q\cdot\vec E.$$
:::

**So liest man das:** Eingabe ist ein Punkt des Raums, Ausgabe ein Vektor, die Feldstärke dort. Sie zeigt in die Richtung der Kraft
auf eine **positive** Probeladung. Auf eine negative Ladung wirkt die Kraft entgegen der Feldrichtung, denn mit negativem $Q$ kehrt
$Q\cdot\vec E$ die Richtung um.

**Warum der Grenzwert?** Eine echte Probeladung hat selbst ein Feld. Sie zieht die Ladungen, die das Feld erzeugen, an oder stößt sie
ab — auf einem Metall etwa verschiebt sie die beweglichen Elektronen — und verfälscht so, was sie messen soll. Je kleiner sie ist,
desto weniger stört sie; im Grenzwert gar nicht mehr.

**Im Bild:** Das Schwerefeld ist die Gewichtskraft pro Masse. Ein Kieselstein misst es, ohne die Erde zu bewegen; eine zweite Erde
würde es verbiegen.

Die Einheit folgt aus der Definition, Kraft durch Ladung:

$$[E] = \frac{\text{N}}{\text{C}} = \frac{\text{kg}\,\text{m}\,\text{s}^{-2}}{\text{A}\,\text{s}} = \text{kg}\,\text{m}\,\text{A}^{-1}\,\text{s}^{-3} = \frac{\text{V}}{\text{m}}.$$

In der Elektrotechnik schreibt man Volt pro Meter.

:::herleitung
Das Newton ist $\text{kg}\,\text{m}\,\text{s}^{-2}$, das Coulomb $\text{A}\,\text{s}$; der Quotient ist $\text{kg}\,\text{m}\,\text{A}^{-1}\,\text{s}^{-3}$. Das Volt
ist nach dem Artikel über Einheiten $\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-1}$; durch einen Meter geteilt, bleibt genau dieselbe
Kombination. Anschaulich: Ein Volt ist ein Joule pro Coulomb, und ein Joule ist ein Newton mal Meter — also ist ein Volt pro Meter
ein Newton pro Coulomb.
:::

**Wie groß sind Feldstärken?** Einige typische Werte:

| Anordnung | Feldstärke |
|---|---|
| Atmosphäre bei klarem Wetter | $100$ bis $200\,\frac{\text{V}}{\text{m}}$ |
| Oberfläche einer Rundfunk-Sendeantenne | $1$ bis $10^3\,\frac{\text{V}}{\text{m}}$ |
| Oberfläche einer Hochspannungsleitung | etwa $10^6\,\frac{\text{V}}{\text{m}}$, also $10^4\,\frac{\text{V}}{\text{cm}}$ |
| Durchschlagsfestigkeit der Luft | etwa $3\cdot10^6\,\frac{\text{V}}{\text{m}}$ |
| im Kondensator | $10^6$ bis $10^8\,\frac{\text{V}}{\text{m}}$ |
| in einem stromdurchflossenen Leiter | etwa $0{,}1\,\frac{\text{V}}{\text{m}}$ |

Ab der __Durchschlagsfestigkeit__ wird Luft leitend, und es springt ein Funke über. Erstaunlich klein ist das Feld im Leiter: Um
einen Strom durch Kupfer zu treiben, genügt ein Zehntel Volt pro Meter.

::::beispiel Kräfte in typischen Feldern
**(a) Ein Elektron im Schönwetterfeld.** Bei klarem Wetter zeigt das Feld der Atmosphäre nach unten, etwa $150\,\frac{\text{V}}{\text{m}}$.
Ein Elektron trägt die Ladung $-e$; die Kraft hat den Betrag

$$F = e\,E = 1{,}602\cdot10^{-19}\,\text{C}\cdot150\,\frac{\text{V}}{\text{m}} \approx 2{,}4\cdot10^{-17}\,\text{N}$$

und zeigt wegen des negativen Vorzeichens nach **oben**. Zum Vergleich die Gewichtskraft des Elektrons, mit seiner Masse
$9{,}109\cdot10^{-31}\,\text{kg}$:

$$m_\text{e}\,g = 9{,}109\cdot10^{-31}\,\text{kg}\cdot9{,}81\,\frac{\text{m}}{\text{s}^2} \approx 8{,}9\cdot10^{-30}\,\text{N}.$$

Die elektrische Kraft ist rund $2{,}7\cdot10^{12}$-mal so groß.

**(b) Ein Elektron im Kondensator.** Bei $10^6\,\frac{\text{V}}{\text{m}}$, dem unteren Rand der Tabelle, ist die Kraft und die Beschleunigung

$$F = 1{,}602\cdot10^{-19}\,\text{C}\cdot10^6\,\frac{\text{V}}{\text{m}} \approx 1{,}6\cdot10^{-13}\,\text{N}, \qquad a = \frac{F}{m_\text{e}} \approx 1{,}8\cdot10^{17}\,\frac{\text{m}}{\text{s}^2}.$$

**Im Bild:** Für ein Elektron ist das Schwerefeld bedeutungslos. Schon das schwache Feld der Atmosphäre zieht billionenfach stärker
als die Erde — nur eben nach oben, weil das Elektron negativ ist.
::::

## Das Coulombsche Gesetz

Wie groß ist die Kraft zwischen zwei Ladungen? Das zeigt ein Gedankenexperiment: Eine kleine geladene Kugel mit
der Ladung $Q_A$ hängt an einem Faden; daneben steht eine zweite mit der Ladung $Q_B$ entgegengesetzten Vorzeichens. Auf $Q_A$ wirken
die Anziehung zu $Q_B$ hin und die Schwerkraft nach unten, und der Faden schlägt um einen Winkel $\alpha$ aus. Aus dem Winkel liest
man die Kraft ab:

$$F = m\,g\,\tan\alpha.$$

Dabei ist $m$ die Masse der Kugel und $g$ die Fallbeschleunigung.

:::herleitung
Im Gleichgewicht ruht die Kugel, die drei Kräfte heben sich auf: die waagerechte elektrische Kraft $F$, die Gewichtskraft $m\,g$ nach
unten und die Fadenkraft längs des Fadens. Der Faden ist um $\alpha$ gegen die Senkrechte geneigt. Damit seine Kraft beide anderen
ausgleicht, muss ihr waagerechter Anteil $F$ und ihr senkrechter Anteil $m\,g$ sein; das Verhältnis der beiden Anteile ist der
Tangens des Neigungswinkels:

$$\tan\alpha = \frac{F}{m\,g}.$$
:::

:::grafik
Szene: get1/elektrische-feldstaerke-und-potenzial/01-coulomb-pendel · Vorlage: ladungspendel
Eine geladene Kugel $Q_A$ hängt an einem Faden von der Decke, daneben im Abstand $r$ eine Kugel $Q_B$ mit entgegengesetztem
Vorzeichen. An $Q_A$ greifen drei Kraftpfeile an: die elektrische Kraft waagerecht zu $Q_B$ hin, die Gewichtskraft $m\,g$ senkrecht nach
unten und die Fadenkraft längs des Fadens; gestrichelt das Kräftedreieck mit dem Winkel $\alpha$ gegen die Senkrechte. Regler für
$Q_A$, $Q_B$ und $r$ verändern den Ausschlag; ein Zähler zeigt $m\,g\tan\alpha$ neben dem Wert aus dem Coulombschen Gesetz. Kernaussage:
Aus dem Auslenkwinkel liest man die elektrische Kraft ab, und sie wächst mit beiden Ladungen und fällt mit dem Abstandsquadrat.
(Rot = Ladungen, blau = Faden und Kugeln, orange = Kraftpfeile, gestrichelt = Kräftedreieck, grau = Decke.)
:::

Variiert man die Ladungen und den Abstand $r$, findet man: Die Kraft ist proportional zu $Q_A$, proportional zu $Q_B$ und umgekehrt
proportional zum Quadrat des Abstands. Das ist das __Coulombsche Gesetz__, in skalarer und vektorieller Form:

:::formel Gesetz
$$F = k\,\frac{Q_A\,Q_B}{r^2}, \qquad \vec F = k\,\frac{Q_A\,Q_B}{r^2}\cdot\frac{\vec r}{r}.$$
:::

**So liest man das:** $\vec F$ ist die Kraft, die $Q_B$ auf $Q_A$ ausübt. Der __Abstandsvektor__ $\vec r$ zeigt von der Ladung, die die
Kraft ausübt, zu der Ladung, auf die sie wirkt — hier von $Q_B$ zu $Q_A$; $r$ ist seine Länge, also $\frac{\vec r}{r}$ ein Einheitsvektor.
Haben die Ladungen gleiches Vorzeichen, ist das Produkt positiv, und die Kraft zeigt längs $\vec r$ von $Q_B$ weg: Abstoßung. Bei
verschiedenen Vorzeichen ist es negativ, und die Kraft zeigt zu $Q_B$ hin: Anziehung. Die skalare Form mit Vorzeichen liefert den
Betrag als $|F|$.

**Ein Fallstrick.** Oft liest man, $\vec r$ zeige in Richtung der Kraft auf $Q_A$. Das stimmt nur bei Abstoßung. Im
beschriebenen Versuch ziehen sich die Ladungen an; ließe man $\vec r$ zu $Q_B$ hin zeigen, ergäbe die vektorielle Formel mit dem
negativen Produkt eine Kraft von $Q_B$ weg — das Gegenteil der Beobachtung.

**Die Konstante.** Im SI schreibt man sie mit der __elektrischen Feldkonstante__ $\varepsilon_0$:

$$k = \frac{1}{4\pi\varepsilon_0} \approx 8{,}988\cdot10^{9}\,\frac{\text{N}\,\text{m}^2}{\text{C}^2}, \qquad \varepsilon_0 \approx 8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}}.$$

Der Faktor $4\pi$ ist die Oberfläche der Einheitskugel; er sorgt dafür, dass er in den Formeln für ebene Anordnungen wie den
Plattenkondensator nicht mehr auftaucht. Seit der SI-Reform 2019 ist $\varepsilon_0$ ein Messwert.

**Im Bild:** Dieselbe Form wie das Gravitationsgesetz aus dem vorigen Artikel, Produkt der „Ladungen" durch Abstandsquadrat. Nur kann
das Produkt negativ werden, und die elektrischen Kräfte sind ungleich stärker — wie viel stärker, zeigt das Wasserstoffatom weiter
unten.

:::herleitung
**Die Kraft auf die andere Ladung.** Vertauscht man die Rollen, zeigt der Abstandsvektor von $Q_A$ zu $Q_B$, also genau entgegengesetzt.
Das Produkt der Ladungen und der Abstand bleiben gleich, also ist die Kraft auf $Q_B$ entgegengesetzt gleich der Kraft auf $Q_A$ —
Newtons Wechselwirkungsprinzip.

**Die Einheit der Konstante.** Aufgelöst nach $k$ ist die Einheit Newton mal Meterquadrat durch Coulombquadrat. Mit
$\frac{\text{N}\,\text{m}}{\text{C}}=\text{V}$ folgt für die Feldkonstante

$$[\varepsilon_0] = \frac{\text{C}^2}{\text{N}\,\text{m}^2} = \frac{\text{C}}{\text{V}\,\text{m}} = \frac{\text{A}\,\text{s}}{\text{V}\,\text{m}}.$$
:::

::::beispiel Ein Pendel misst die Kraft
Eine Kugel von $1\,\text{g}$ hängt am Faden und schlägt neben einer zweiten, gleich stark geladenen Kugel um den Winkel aus, dessen
Tangens $0{,}1$ ist, also um etwa $5{,}7^\circ$. Die elektrische Kraft:

$$F = 10^{-3}\,\text{kg}\cdot9{,}81\,\frac{\text{m}}{\text{s}^2}\cdot0{,}1 \approx 9{,}81\cdot10^{-4}\,\text{N}.$$

Die Mittelpunkte sind dabei $5\,\text{cm}$ voneinander entfernt. Mit gleich großen Ladungsbeträgen $Q$ folgt aus dem Coulombschen
Gesetz

$$Q = r\,\sqrt{\frac{F}{k}} = 0{,}05\,\text{m}\cdot\sqrt{\frac{9{,}81\cdot10^{-4}\,\text{N}}{8{,}988\cdot10^{9}\,\text{N}\,\text{m}^2/\text{C}^2}} \approx 1{,}65\cdot10^{-8}\,\text{C}.$$

Gut sechzehn Nanocoulomb genügen also, um ein Gramm merklich auszulenken.

**Im Bild:** Der Faden zeigt die Summe aus Schwerkraft und elektrischer Kraft. Je stärker die Ladungen ziehen, desto weiter neigt er
sich von der Senkrechten weg.
::::

**Wie genau gilt das $\frac{1}{r^2}$?** In frühen Versuchen war das nicht sicher. Man schreibt eine mögliche Abweichung als kleinen
Zusatz $\delta$ im Exponenten,

$$F \sim \frac{1}{r^{2\pm\delta}},$$

und Messungen haben ihn immer weiter eingegrenzt:

| Zeit | Experimentatoren | Abweichung $\delta$ höchstens |
|---|---|---|
| 18. Jahrhundert | Cavendish | $0{,}02$ |
| 19. Jahrhundert | Maxwell | $5\cdot10^{-5}$ |
| 1970 | Bartlett und andere | $10^{-13}$ |
| 1971 | Williams und andere | $3\cdot10^{-16}$ |

Gemessen hat man dabei nicht die Kraft zwischen zwei Kugeln, sondern etwas viel Empfindlicheres: Im Inneren einer geladenen
Metallkugel verschwindet das Feld nur dann vollständig, wenn das Gesetz exakt $\frac{1}{r^2}$ lautet. Man sucht also im Inneren nach einem
Restfeld — und findet keines. Mit dieser Abschirmung befasst sich der Abschnitt über Feldlinien.

**Im Bild:** Auch die Gravitation fällt mit dem Abstandsquadrat. Bei beiden ist der Grund derselbe: Das Feld verteilt sich auf
Kugeloberflächen, die mit $r^2$ wachsen.

::::beispiel Elektrisch gegen Gravitation
Im Wasserstoffatom sind Elektron und Proton etwa $5{,}29\cdot10^{-11}\,\text{m}$ voneinander entfernt. Die elektrische Anziehung, mit den
Beträgen $e$ beider Ladungen:

$$F_\text{el} = 8{,}988\cdot10^{9}\,\frac{\text{N}\,\text{m}^2}{\text{C}^2}\cdot\frac{\big(1{,}602\cdot10^{-19}\,\text{C}\big)^2}{\big(5{,}29\cdot10^{-11}\,\text{m}\big)^2} \approx 8{,}2\cdot10^{-8}\,\text{N}.$$

Die Gravitation zwischen beiden, mit den Massen $9{,}109\cdot10^{-31}\,\text{kg}$ und $1{,}673\cdot10^{-27}\,\text{kg}$:

$$F_\text{grav} = 6{,}674\cdot10^{-11}\,\frac{\text{m}^3}{\text{kg}\,\text{s}^2}\cdot\frac{9{,}109\cdot10^{-31}\,\text{kg}\cdot1{,}673\cdot10^{-27}\,\text{kg}}{\big(5{,}29\cdot10^{-11}\,\text{m}\big)^2} \approx 3{,}6\cdot10^{-47}\,\text{N}.$$

Das Verhältnis ist etwa $2{,}3\cdot10^{39}$, und es hängt nicht vom Abstand ab, weil beide Kräfte mit $\frac{1}{r^2}$ fallen.

**Im Bild:** Dass uns trotzdem die Schwerkraft am Boden hält und nicht die Elektrizität, liegt daran, dass sich positive und
negative Ladungen in fast jedem Körper genau ausgleichen. Massen dagegen addieren sich immer.
::::

## Das Feld einer Punktladung und die Überlagerung

Setzt man in das Coulombsche Gesetz eine Probeladung $Q$ und eine felderzeugende Punktladung $Q_0$ ein und teilt durch $Q$, bleibt
das Feld der Punktladung. Mit dem Abstandsvektor $\vec r$ von $Q_0$ zum betrachteten Punkt, seiner Länge $r$ und dem Einheitsvektor
$\vec e_r$ in seiner Richtung:

:::formel
$$\vec E(\vec r) = \frac{1}{4\pi\varepsilon_0}\,\frac{Q_0}{r^2}\,\vec e_r.$$
:::

**So liest man das:** Bei positivem $Q_0$ zeigt das Feld überall von der Ladung weg, bei negativem zu ihr hin. Sein Betrag fällt mit dem
Abstandsquadrat; doppelter Abstand heißt ein Viertel der Feldstärke.

**Im Bild:** Das Schwerefeld außerhalb der Erde ist genau so gebaut: Betrag $\gamma\frac{M}{r^2}$ mit der Erdmasse $M$, Richtung zum
Mittelpunkt — wie das Feld einer negativen Ladung, denn die Schwerkraft zieht immer an.

:::herleitung
Nach dem Coulombschen Gesetz mit $Q_0$ als kraftausübender Ladung zeigt der Abstandsvektor von $Q_0$ zur Probeladung, und die Kraft
ist

$$\vec F = \frac{1}{4\pi\varepsilon_0}\,\frac{Q_0\,Q}{r^2}\,\vec e_r.$$

Teilt man durch $Q$, fällt die Probeladung heraus. Weil das Ergebnis gar nicht mehr von ihr abhängt, ändert der Grenzwert nichts.
:::

**Mehrere Ladungen.** Die Kräfte, die mehrere Ladungen auf eine Probeladung ausüben, addieren sich als Vektoren, und jede wirkt so,
als wären die anderen nicht da. Deshalb addieren sich auch die Felder, das __Superpositionsprinzip__ oder die __Überlagerung__:

$$\vec E = \vec E_1+\vec E_2+\ldots+\vec E_n.$$

**Im Bild:** Erde und Mond ziehen beide an einem Satelliten; seine Gesamtbeschleunigung ist die Pfeilsumme beider Anteile.

:::herleitung
Dass sich die Coulomb-Kräfte einzelner Ladungen ungestört überlagern, ist eine Erfahrungstatsache. Für die Gesamtkraft gilt also

$$\vec F = \vec F_1+\ldots+\vec F_n = Q\,\vec E_1+\ldots+Q\,\vec E_n = Q\,\big(\vec E_1+\ldots+\vec E_n\big).$$

Teilt man durch $Q$, steht links das Gesamtfeld.
:::

::::beispiel Feldstärken einer Ladung und eines Paars
**(a) Eine Punktladung** von $1\,\text{nC}$, in zwei Abständen:

$$r = 1\,\text{cm}: \ \ E = 8{,}988\cdot10^{9}\,\frac{\text{N}\,\text{m}^2}{\text{C}^2}\cdot\frac{10^{-9}\,\text{C}}{\big(10^{-2}\,\text{m}\big)^2} \approx 9{,}0\cdot10^{4}\,\frac{\text{V}}{\text{m}}, \qquad r = 10\,\text{cm}: \ \ E \approx 900\,\frac{\text{V}}{\text{m}}.$$

Zehnmal so weit weg ist das Feld hundertmal schwächer.

**(b) Ein Ladungspaar** auf einer Geraden, mit der Koordinate $x$ längs dieser Geraden:

$$+1\,\text{nC} \ \text{bei} \ x = -1\,\text{cm}, \qquad -1\,\text{nC} \ \text{bei} \ x = +1\,\text{cm}.$$

In der Mitte ist jede Ladung $1\,\text{cm}$ entfernt, jede liefert also $9{,}0\cdot10^{4}\,\frac{\text{V}}{\text{m}}$. Das Feld der positiven Ladung zeigt von ihr weg, nach rechts; das
der negativen zu ihr hin, ebenfalls nach rechts:

$$\vec E = 2\cdot9{,}0\cdot10^{4}\,\frac{\text{V}}{\text{m}}\cdot\vec e_x = 1{,}8\cdot10^{5}\,\frac{\text{V}}{\text{m}}\cdot\vec e_x,$$

mit dem Einheitsvektor $\vec e_x$ nach rechts.

**Im Bild:** Zwischen den Ladungen ziehen beide Felder in dieselbe Richtung und verstärken sich. Wären beide Ladungen positiv, höben
sich die Felder in der Mitte genau auf.
::::

## Feldlinien

Ein Feld ist unsichtbar. Man macht es mit __Feldlinien__ sichtbar: Kurven, deren Tangente in jedem Punkt die Richtung des Felds
angibt und deren Dichte seine Stärke zeigt. Im Versuch streut man Eisenspäne um Magnete; sie richten sich im Magnetfeld aus, und
ihr Muster gleicht dem elektrischen Feld entsprechender Ladungen.

So entstehen die typischen Bilder: Um eine einzelne Ladung laufen die Linien strahlenförmig. Zwischen zwei ungleichnamigen Ladungen
laufen sie in Bögen von der positiven zur negativen; zwischen zwei gleichnamigen weichen sie einander aus, und in der Mitte bleibt
ein feldfreier Punkt. Zwischen den Platten eines __Plattenkondensators__ laufen sie parallel und gleich dicht — dort ist das Feld
__homogen__, überall gleich groß und gleich gerichtet; nur am Rand wölben sie sich nach außen. Ein hohler Leiter in diesem Feld
bleibt innen frei von Linien.

Aus solchen Versuchen folgen fünf Regeln:

- Die __Quellen__ und __Senken__ der Feldlinien sind die positiven und negativen Ladungen.
- Feldlinien verlaufen von positiven zu negativen Ladungen. Sie beginnen und enden nie im leeren Raum.
- Feldlinien schneiden sich nicht — außer in Punkten, an denen das Feld null ist und keine Richtung hat.
- Ein von einem Leiter umschlossener ladungsfreier Raum ist feldfrei, die __Abschirmung__.
- Feldlinien treffen stets senkrecht auf leitende Oberflächen.

**Im Bild:** Die Feldlinien des Schwerefelds sind die Lotlinien, die überall zum Erdmittelpunkt zeigen. Auch sie schneiden sich nicht,
und eine ruhende Wasseroberfläche steht senkrecht auf ihnen — so wie die beweglichen Ladungen eines Leiters erst zur Ruhe kommen,
wenn das Feld senkrecht auf seiner Oberfläche steht. Bei der Abschirmung endet die Analogie: Gegen die Schwerkraft gibt es keinen
Schirm.

:::herleitung
**Quellen und Senken.** Das Feld einer positiven Ladung zeigt von ihr weg, das einer negativen zu ihr hin. Folgt man der Feldrichtung,
läuft man also von positiven Ladungen fort und auf negative zu.

**Kein Anfang im leeren Raum.** Bei einer Punktladung fällt das Feld wie $\frac{1}{r^2}$, und die Kugelflächen um sie wachsen wie $r^2$.
Zeichnet man eine feste Zahl von Linien, ist ihre Dichte auf jeder Kugel genau proportional zur Feldstärke — aber nur, wenn keine
Linie zwischen zwei Kugeln anfängt oder aufhört. Dass das für jedes elektrostatische Feld gilt, besagt das Gaußsche Gesetz aus
Maxwells Gleichungen; hier nimmt man es als Ergebnis der Versuche.

**Keine Schnittpunkte.** Die Tangente einer Feldlinie ist die Feldrichtung. Schnitten sich zwei Linien, hätte das Feld dort zwei
Richtungen. Das geht nur, wo es null ist und gar keine Richtung hat.

**Senkrecht auf Leitern.** In einem Leiter sind Ladungen frei beweglich. Hätte das Feld an der Oberfläche einen Anteil längs der
Oberfläche, würde es die Ladungen verschieben. Im Ruhezustand haben sie sich so verteilt, dass dieser Anteil verschwindet.

**Abschirmung, Beweisidee.** Auch im Inneren des Metalls verschieben sich die Ladungen, bis dort kein Feld mehr wirkt. Gäbe es im
ladungsfreien Hohlraum eine Feldlinie, müsste sie auf der Innenwand beginnen und enden. Führte man eine Probeladung längs dieser
Linie und durch das feldfreie Metall zurück, hätte das Feld auf der Runde Arbeit verrichtet, ohne dass sich etwas verbraucht. Dass
das im elektrostatischen Feld unmöglich ist, zeigt der nächste Artikel.
:::

:::grafik
Szene: get1/elektrische-feldstaerke-und-potenzial/01-feldlinienbilder · Vorlage: feldlinien-muster
Fünf Felder nebeneinander, jeweils links das Eisenspan-Muster, rechts die gezeichneten Feldlinien mit Pfeilen: eine positive
Punktladung mit strahlenförmigen Linien; zwei ungleichnamige Ladungen mit Bögen von plus nach minus; zwei gleichnamige mit dem
feldfreien Punkt in der Mitte; ein Plattenkondensator mit parallelen Linien innen und gewölbtem Randfeld; ein hohler Metallring im
Kondensatorfeld, auf dessen Außenseite die Linien senkrecht enden und dessen Inneres leer bleibt. Ein Zeiger tastet die Linien ab
und zeigt in jedem Punkt den Feldpfeil als Tangente. Kernaussage: Feldlinien zeigen Richtung und Stärke des Felds und folgen fünf
festen Regeln. (Rot = Ladungen, blau = Feldlinien, orange = Tangenten-Pfeil, grau = Leiter und Eisenspäne.)
:::

::::beispiel Feldlinien zählen
Von einer positiven Punktladung gehen $24$ Feldlinien aus. Auf einer Kugel um sie verteilen sie sich gleichmäßig; ihre Dichte ist
Linienzahl durch Kugelfläche:

$$r = 1\,\text{cm}: \ \ \frac{24}{4\pi\cdot(1\,\text{cm})^2} \approx 1{,}91\,\frac{\text{Linien}}{\text{cm}^2}, \qquad r = 2\,\text{cm}: \ \ \frac{24}{4\pi\cdot(2\,\text{cm})^2} \approx 0{,}48\,\frac{\text{Linien}}{\text{cm}^2}.$$

Beim doppelten Abstand ist die Dichte ein Viertel — genau wie die Feldstärke der Punktladung. Die Linien zeigen das
$\frac{1}{r^2}$ also richtig an, weil keine unterwegs verloren geht.

**Im Bild:** Dieselben $24$ Linien durchstoßen jede Kugel um die Ladung. Weiter draußen verteilen sie sich auf mehr Fläche, und das Feld
wird schwächer.
::::

## Bedeutung und Ausblick

Die Feldstärke ist der Grundbegriff der Elektrostatik. Aus ihr folgt die Kraft auf jede Ladung, und mit ihr beginnt fast jede
Rechnung an elektrischen Anordnungen. Die Tabelle der Feldstärken zeigt, wo das praktisch wird: Isolierungen müssen unter der
Durchschlagsfestigkeit bleiben, und Kondensatoren nutzen sehr hohe Feldstärken in sehr dünnen Schichten. Die Abschirmung schützt
Insassen eines Autos bei Blitzschlag und die Signale in einem abgeschirmten Kabel.

Der nächste Artikel fragt nach der Energie: Welche Arbeit verrichtet das Feld, wenn sich eine Ladung in ihm bewegt? Daraus
entstehen das Potenzial und die Spannung — und auch der Zusammenhang zwischen der Feldstärke im Plattenkondensator, der Spannung an
seinen Platten und ihrem Abstand.

:::kern
- Das __elektrische Feld__ ordnet jedem Punkt die Kraft pro Ladung auf eine positive Probeladung zu: $\vec E=\lim_{Q\to0}\frac{\vec F}{Q}$.
- Auf eine Ladung wirkt $\vec F=Q\,\vec E$; auf negative Ladungen entgegen der Feldrichtung.
- Die Einheit ist Newton pro Coulomb, gleich Volt pro Meter.
- Gleichnamige Ladungen stoßen sich ab, ungleichnamige ziehen sich an; beim Reiben wird Ladung nur verschoben (__Ladungserhaltung__).
- __Coulombsches Gesetz__: $F=\frac{1}{4\pi\varepsilon_0}\frac{Q_AQ_B}{r^2}$; der Abstandsvektor zeigt von der kraftausübenden zur kraftempfangenden Ladung.
- Das $\frac{1}{r^2}$ ist im Exponenten auf $3\cdot10^{-16}$ genau bestätigt, gemessen über die Feldfreiheit im Inneren geladener Kugeln.
- Eine Punktladung erzeugt ein radiales Feld vom Betrag $\frac{1}{4\pi\varepsilon_0}\frac{Q_0}{r^2}$; mehrere Felder addieren sich als Vektoren.
- __Feldlinien__: Tangente gleich Feldrichtung, Dichte gleich Feldstärke; sie beginnen auf positiven und enden auf negativen Ladungen.
- Feldlinien schneiden sich nur, wo das Feld null ist, und stehen senkrecht auf Leiteroberflächen.
- Ein von einem Leiter umschlossener ladungsfreier Raum ist feldfrei — die __Abschirmung__.
- Im Wasserstoffatom ist die elektrische Anziehung rund $2{,}3\cdot10^{39}$-mal so stark wie die Gravitation.
- Ørsted: Ströme erzeugen Magnetfelder; Faraday: Flussänderungen induzieren Spannungen, $U_{\text{ind}}=-N\frac{d\Phi}{dt}$.
:::

:::quiz
F: Warum definiert man die Feldstärke als Kraft pro Ladung, und warum als Grenzwert für eine immer kleinere Probeladung?
A: Die Kraft ist proportional zur Probeladung; teilt man durch sie, bleibt eine Größe, die nur vom Ort abhängt — wie das Schwerefeld als Kraft pro Masse. Eine echte Probeladung hat aber selbst ein Feld und verschiebt die felderzeugenden Ladungen, etwa die Elektronen eines Metalls. Erst im Grenzwert stört sie nicht mehr.
F: In welche Richtung wirkt die Kraft auf ein Elektron im Schönwetterfeld, und wie verhält sie sich zur Gewichtskraft?
A: Das Feld zeigt nach unten, das Elektron ist negativ, also wirkt die Kraft $\vec F=Q\vec E$ nach oben. Bei $150\,\frac{\text{V}}{\text{m}}$ ist sie etwa $2{,}4\cdot10^{-17}\,\text{N}$, rund $2{,}7\cdot10^{12}$-mal so groß wie die Gewichtskraft des Elektrons von $8{,}9\cdot10^{-30}\,\text{N}$.
F: Warum ist ein Newton pro Coulomb dasselbe wie ein Volt pro Meter?
A: Ein Newton pro Coulomb ist $\text{kg}\,\text{m}\,\text{s}^{-2}$ durch $\text{A}\,\text{s}$, also $\text{kg}\,\text{m}\,\text{A}^{-1}\,\text{s}^{-3}$. Ein Volt ist ein Joule pro Coulomb, ein Joule ein Newton mal Meter; ein Volt pro Meter ist deshalb ebenfalls ein Newton pro Coulomb — in Basiseinheiten dieselbe Kombination.
F: Was beobachtet man beim Reiben von Glas und Hartgummi, und was besagt die Ladungserhaltung?
A: Glas mit Seide und Hartgummi mit Fell gerieben ziehen sich an, zwei Hartgummistäbe stoßen sich ab. Beim Reiben gehen Elektronen über: Das Glas hat danach einen Mangel, positiv, der Hartgummi einen Überschuss, negativ. Ladung wird dabei nur verschoben; die Summe aller positiven und negativen Ladungen bleibt null.
F: Was haben Ørsted und Faraday entdeckt, und welche Spannung liefert die Spule mit $200$ Windungen?
A: Ørsted fand, dass ein Strom ein Magnetfeld erzeugt, dessen Richtung die Rechte-Faust-Regel gibt. Faraday fand die Umkehrung: Eine Änderung des magnetischen Flusses induziert eine Spannung, $U_{\text{ind}}=-N\frac{d\Phi}{dt}$. Steigt der Fluss in $0{,}1\,\text{s}$ um $5\,\text{mWb}$, sind das bei $200$ Windungen $10\,\text{V}$, mit dem Minuszeichen der Lenzschen Regel.
F: Wie misst ein Pendel die Kraft zwischen zwei Ladungen, und welche Ladung ergibt das Beispiel?
A: Im Gleichgewicht gleicht die Fadenkraft Schwerkraft und elektrische Kraft aus; das Verhältnis ihrer Anteile ist der Tangens des Auslenkwinkels, also $F=m\,g\,\tan\alpha$. Eine Kugel von $1\,\text{g}$ mit $\tan\alpha=0{,}1$ erfährt etwa $9{,}8\cdot10^{-4}\,\text{N}$; bei $5\,\text{cm}$ Abstand und gleich großen Ladungen sind das je rund $16{,}5\,\text{nC}$.
F: In welche Richtung zeigt der Abstandsvektor im Coulombschen Gesetz, und warum darf man ihn nicht einfach in Kraftrichtung zeigen lassen?
A: Er zeigt von der Ladung, die die Kraft ausübt, zu der Ladung, auf die sie wirkt. Dann gibt ein positives Produkt der Ladungen eine Kraft längs $\vec r$, also Abstoßung, ein negatives eine Kraft entgegen $\vec r$, also Anziehung. Ließe man $\vec r$ in Kraftrichtung zeigen, ergäbe die vektorielle Formel bei der Anziehung im Versuch eine abstoßende Kraft.
F: Wie genau gilt das $\frac{1}{r^2}$ im Coulombschen Gesetz, und wie hat man das gemessen?
A: Eine mögliche Abweichung im Exponenten ist von $0{,}02$ bei Cavendish über $5\cdot10^{-5}$ bei Maxwell bis auf $3\cdot10^{-16}$ im Jahr 1971 eingegrenzt. Gemessen hat man über die Abschirmung: Nur bei exaktem $\frac{1}{r^2}$ verschwindet das Feld im Inneren einer geladenen Metallkugel vollständig, und dort findet man kein Restfeld.
F: Wie sieht das Feld einer Punktladung aus, und was ergibt die Überlagerung in der Mitte zwischen $+1\,\text{nC}$ und $-1\,\text{nC}$ im Abstand $2\,\text{cm}$?
A: Es ist radial, bei positiver Ladung nach außen, mit dem Betrag $\frac{1}{4\pi\varepsilon_0}\frac{Q_0}{r^2}$ — bei $1\,\text{nC}$ in $1\,\text{cm}$ etwa $9\cdot10^4\,\frac{\text{V}}{\text{m}}$, in $10\,\text{cm}$ nur $900\,\frac{\text{V}}{\text{m}}$. In der Mitte des Paars zeigen beide Anteile zur negativen Ladung hin und addieren sich zu $1{,}8\cdot10^5\,\frac{\text{V}}{\text{m}}$.
F: Warum schneiden sich Feldlinien nicht, warum stehen sie senkrecht auf Leitern, und warum ist ein umschlossener Hohlraum feldfrei?
A: Die Tangente einer Feldlinie ist die Feldrichtung; ein Schnittpunkt hieße zwei Richtungen, möglich nur, wo das Feld null ist. Ein Feldanteil längs einer Leiteroberfläche würde die freien Ladungen verschieben, im Ruhezustand ist er verschwunden. Eine Feldlinie im ladungsfreien Hohlraum müsste auf der Innenwand beginnen und enden, und eine Runde längs dieser Linie und durch das feldfreie Metall zurück lieferte Arbeit aus dem Nichts — im elektrostatischen Feld unmöglich.
:::
