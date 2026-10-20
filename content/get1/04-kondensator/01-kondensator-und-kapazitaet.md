---
title: Der Kondensator und seine Kapazität
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Kondensator
order: 40100
summary: Von Grund auf – wie ein Kondensator Ladung und Energie speichert. Leitbild ist eine Gummimembran in einem Wasserrohr: Man kann Ladung hineinschieben, aber nicht hindurch, und je mehr verschoben ist, desto stärker drückt sie zurück. Mit der Kapazität und warum Ladung und Spannung proportional sind, Strom und Spannung am Kondensator, der hergeleiteten Formel des Plattenkondensators, Dielektrikum und Polarisation, Kondensatortypen, Selbstentladung als reine Materialeigenschaft und der gespeicherten Energie samt Energiedichte des Felds. Mit Beispiel-Seite.
tags: Kondensator, Kapazität, Farad, Plattenkondensator, Dielektrikum, Permittivität, Energie
---

## Anschaulich

Ein Kondensator besteht aus zwei leitenden Flächen, die sich dicht gegenüberliegen, ohne sich zu berühren. Legt man eine Spannung an,
fließt Ladung auf die eine Fläche und gleich viel von der anderen weg — durch den Spalt selbst fließt nichts. Die getrennten Ladungen
bleiben dort, gehalten von ihrer gegenseitigen Anziehung, und mit ihnen bleibt Energie im Feld zwischen den Flächen gespeichert.

**Das Leitbild dieses Artikels:** eine **Gummimembran in einem Wasserrohr**. Das Rohr ist quer durch eine elastische Membran geteilt.
Pumpt man auf der einen Seite Wasser hinein, wölbt sich die Membran, und auf der anderen Seite fließt genauso viel Wasser hinaus. Durch die
Membran selbst fließt nichts; je weiter sie gedehnt ist, desto stärker drückt sie zurück.

Im Bild ist das Wasser die Ladung, der Druckunterschied über der Membran die Spannung und die verschobene Wassermenge die gespeicherte
Ladung. Eine nachgiebige Membran nimmt bei gleichem Druck mehr Wasser auf — das ist eine große Kapazität. Die gespannte Membran speichert
Energie, ein Riss ist der Durchschlag, eine winzige undichte Stelle die Selbstentladung. Das Bild ist eine Analogie, kein Gesetz; an jeder
Stelle steht unten die Physik dahinter.

:::grafik
Szene: get1/kondensator/01-membran-im-rohr · Vorlage: membran-kondensator
Oben ein waagerechtes Rohr, in der Mitte von einer Gummimembran geteilt, links eine Pumpe. Ein Regler erhöht den Pumpendruck: Die Membran
wölbt sich nach rechts, links fließt Wasser hinein und rechts genauso viel hinaus; ein Zähler zeigt die verschobene Menge, die mit dem Druck
proportional wächst. Darunter das elektrische Gegenstück: ein Plattenkondensator an einer Spannungsquelle, auf den Platten $+Q$ und $-Q$, und
derselbe Zähler für die Ladung. Kernaussage: Ladung lässt sich in einen Kondensator hineinschieben, aber nicht hindurch, und die verschobene
Ladung wächst mit der Spannung. (Blau = Wasser und Feld, rot = Membran und Platten, orange = Zähler, grau = Rohr und Leitungen.)
:::

## Aufbau und Schaltzeichen

Ein __Kondensator__ besteht aus zwei __Elektroden__, leitenden Flächen, und einem Isolator dazwischen, dem __Dielektrikum__. Die einfachste
Form ist der __Plattenkondensator__: zwei parallele Metallplatten der Fläche $A$ im Abstand $d$. Sein Schaltzeichen sind zwei parallele
Striche, die Platten im Querschnitt.

**Im Bild:** Die Elektroden sind die beiden Rohrhälften, das Dielektrikum die Membran.

In der Praxis sind die Elektroden aufgewickelte Metallfolien, Schichtstapel oder poröse Körper mit großer Oberfläche. Das Skript nennt
typische Bauformen:

| Kondensatortyp | Kapazitätsbereich | Größe | Betriebsspannung | selbstheilend | gepolt |
|---|---|---|---|---|---|
| Papier | $100\,\text{pF}$ bis $1\,\mu\text{F}$ | groß | $125$ bis $1000\,\text{V}$ | nein | nein |
| Metall-Papier | $0{,}1$ bis $50\,\mu\text{F}$ | groß | $160$ bis $600\,\text{V}$ | ja | nein |
| Styroflex | $2\,\text{pF}$ bis $50\,\text{nF}$ | mittel | $50$ bis $500\,\text{V}$ | nein | nein |
| Metall-Kunststoff | $0{,}001$ bis $0{,}25\,\mu\text{F}$ | klein | $300\,\text{V}$ bis $5\,\text{kV}$ | ja | nein |
| Metall-Lack | $0{,}1$ bis $200\,\mu\text{F}$ | sehr klein | $60$ bis $120\,\text{V}$ | ja | nein |
| Keramik | $0{,}5\,\text{pF}$ bis $50\,\text{nF}$ | groß | $250$ bis $500\,\text{V}$ | nein | nein |
| Elektrolyt | $0{,}5$ bis $10\,000\,\mu\text{F}$ | sehr klein | $3$ bis $650\,\text{V}$ | ja | ja |

__Selbstheilend__ heißt: Bei einem lokalen Durchschlag verdampft die sehr dünne Metallschicht um die Fehlstelle, und der Kondensator
funktioniert weiter. __Gepolt__ heißt: Der Kondensator darf nur in einer Richtung an Spannung liegen. Beim Elektrolytkondensator ist das
Dielektrikum eine hauchdünne Oxidschicht, die bei falscher Polung abgebaut wird.

## Die Kapazität

Legt man an einen Kondensator die Spannung $U$, trägt die eine Elektrode die Ladung $+Q$, die andere $-Q$. Verdoppelt man die Spannung,
verdoppelt sich die Ladung. Der feste Proportionalitätsfaktor ist die __Kapazität__:

:::formel Definition
$$C = \frac{Q}{U}, \qquad [C] = \frac{\text{A}\,\text{s}}{\text{V}} = \text{F}.$$
:::

**So liest man das:** $C$ gibt an, wie viel Ladung der Kondensator pro Volt aufnimmt. Die Einheit ist das __Farad__, ein Coulomb pro Volt.
Weil Ladung und Spannung stets im selben Verhältnis wachsen, hängt $C$ nicht davon ab, wie stark man den Kondensator gerade lädt — nur von
seiner Geometrie und seinem Material.

**Im Bild:** Die Nachgiebigkeit der Membran. Eine weiche Membran nimmt bei gleichem Druck viel Wasser auf, eine steife wenig.

:::herleitung
**Warum Ladung und Spannung proportional sind.** Verdoppelt man die Ladung auf beiden Elektroden, verdoppelt sich nach dem Coulombschen
Gesetz und dem Superpositionsprinzip das Feld an jedem Punkt — jede einzelne Ladung trägt ihren Anteil bei, und doppelt so viele tragen
doppelt so viel bei. Die Spannung ist das Wegintegral des Felds von einer Elektrode zur anderen, also verdoppelt auch sie sich. Ihr
Verhältnis bleibt fest.

**Die Einheit.** Ladung durch Spannung: Coulomb durch Volt, und ein Coulomb ist eine Amperesekunde.
:::

Ein Farad ist sehr viel. Übliche Kondensatoren liegen im Bereich von Femtofarad in integrierten Schaltungen über Pikofarad und Nanofarad
bis zu Mikrofarad. Ausnahmen sind __Doppelschichtkondensatoren__, Goldcaps oder Supercaps genannt: Sie erreichen viele Farad, große Zellen
einige tausend Farad; das Skript nennt bis zu $100\,\text{F}$. Dafür haben sie einen vergleichsweise hohen Leckstrom und vertragen nur
wenige Volt.

::::beispiel Ladung auf einem Elko
Ein Elektrolytkondensator von $100\,\mu\text{F}$ liegt an $12\,\text{V}$. Die Ladung auf seiner Pluselektrode und die Zahl der Elektronen, die
dafür von ihr abgeflossen sind:

$$Q = C\,U = 10^{-4}\,\frac{\text{A}\,\text{s}}{\text{V}}\cdot12\,\text{V} = 1{,}2\cdot10^{-3}\,\text{C}, \qquad N = \frac{1{,}2\cdot10^{-3}\,\text{C}}{1{,}602\cdot10^{-19}\,\text{C}} \approx 7{,}5\cdot10^{15}.$$

Bei $6\,\text{V}$ wäre es genau die Hälfte. Ein Farad hätte bei $12\,\text{V}$ dagegen schon $12\,\text{C}$ getragen — zehntausendmal so viel.

**Im Bild:** Doppelter Druck, doppelt so viel verschobenes Wasser. Die Nachgiebigkeit der Membran bleibt dieselbe.
::::

## Strom und Spannung am Kondensator

Ändert sich die Spannung, ändert sich die Ladung, und dafür muss ein Strom fließen. Strom ist Ladung pro Zeit, wie Kapitel 5 genauer
zeigt. Mit kleinen Buchstaben für zeitabhängige Größen, dem Strom $i_C(t)$ in den Kondensator und der Spannung $u_C(t)$ an ihm:

:::formel
$$i_C(t) = \frac{dq}{dt} = C\,\frac{du_C}{dt}, \qquad u_C(t) = u_C(t_0)+\frac{1}{C}\int_{t_0}^{t}i_C(\tau)\;d\tau.$$
:::

**So liest man das:** Der Strom ist proportional zur **Änderung** der Spannung, nicht zur Spannung selbst. Bei konstanter Spannung fließt
kein Strom: Ein geladener Kondensator sperrt Gleichstrom. Umgekehrt ist die Spannung der aufintegrierte Strom, ausgehend von ihrem Wert
zur Startzeit $t_0$. Das Skript schreibt die Ladung als $Q(t)$ und lässt beim Integral den Anfangswert weg; ohne ihn ist die Spannung nur bis
auf eine Konstante bestimmt.

**Im Bild:** Wasser fließt nur, solange sich die Membran weiter wölbt. Steht sie still, steht auch das Wasser — ein ständiger Strom durch
die Membran ist unmöglich.

:::herleitung
Zu jeder Zeit gilt $q(t)=C\,u_C(t)$ mit konstantem $C$. Leitet man nach der Zeit ab, kommt der Faktor $C$ vor die Ableitung:

$$i_C(t) = \frac{dq}{dt} = \frac{d}{dt}\big(C\,u_C(t)\big) = C\,\frac{du_C}{dt}.$$

Integriert man diese Gleichung von $t_0$ bis $t$, gibt der Hauptsatz der Differential- und Integralrechnung links das Integral des Stroms
und rechts $C$ mal die Änderung der Spannung; nach $u_C(t)$ aufgelöst steht die zweite Formel da.
:::

::::beispiel Laden mit konstantem Strom
Der Elko von $100\,\mu\text{F}$ wird aus dem leeren Zustand mit einem konstanten Strom von $2\,\text{mA}$ geladen. Die Spannung steigt dann
gleichmäßig:

$$\frac{du_C}{dt} = \frac{i_C}{C} = \frac{2\cdot10^{-3}\,\text{A}}{10^{-4}\,\text{A}\,\text{s}/\text{V}} = 20\,\frac{\text{V}}{\text{s}}, \qquad u_C(t) = 20\,\frac{\text{V}}{\text{s}}\cdot t.$$

Nach $0{,}6\,\text{s}$ sind $12\,\text{V}$ erreicht. Bis dahin sind $2\,\text{mA}$ mal $0{,}6\,\text{s}$ geflossen, also $1{,}2\,\text{mC}$ — dieselbe
Ladung wie oben.

**Im Bild:** Eine Pumpe, die gleichmäßig fördert, dehnt die Membran gleichmäßig — der Druck steigt linear mit der Zeit.
::::

**Laden und Entladen.** Schließt man einen leeren Kondensator an eine Gleichspannungsquelle, fließt Strom, bis seine Spannung die der Quelle
erreicht hat; dann reicht die Spannung der Quelle nicht mehr, weitere Ladung hinüberzuschieben, und der Strom steht. Verbindet man die
Elektroden eines geladenen Kondensators über einen Widerstand, gleichen sich die Ladungen aus: Der Strom fließt jetzt in die Gegenrichtung,
bis die Spannung null ist. Wie beides zeitlich abläuft, zeigt der Artikel über Laden und Entladen.

**Im Bild:** Die Pumpe dehnt die Membran, bis deren Gegendruck dem Pumpendruck gleicht. Öffnet man ein Ventil zwischen den beiden Rohrseiten,
entspannt sie sich und schiebt das Wasser zurück.

## Der Plattenkondensator

Für zwei parallele Platten der Fläche $A$ im Abstand $d$, mit einem Dielektrikum der __Permittivität__ $\varepsilon$ dazwischen, ist die
Kapazität

:::formel
$$C = \varepsilon\,\frac{A}{d}, \qquad \varepsilon = \varepsilon_0\,\varepsilon_\text{r}.$$
:::

**So liest man das:** Die Kapazität steigt mit größerer Fläche, kleinerem Abstand und größerer Permittivität. Diese ist das Produkt aus der
elektrischen Feldkonstante $\varepsilon_0$ aus dem Coulombschen Gesetz und der __Permittivitätszahl__ $\varepsilon_\text{r}$ des Materials, im
Vakuum $1$. Das Skript nennt $\varepsilon$ die Dielektrizitätszahl. Die Formel gilt, solange der Abstand klein gegen die Plattenmaße ist: Dann
ist das Feld innen homogen, und das Randfeld fällt nicht ins Gewicht.

**Im Bild:** Eine größere Membran gibt bei gleichem Druck mehr nach, eine dünnere ebenso, und ein weicheres Material auch.

:::grafik
Szene: get1/kondensator/01-plattenkondensator-gauss · Vorlage: plattenkondensator-feld
Zwei waagerechte Platten der Fläche $A$ im Abstand $d$, oben $+Q$, unten $-Q$, dazwischen gleich dichte senkrechte Feldlinien, am Rand ein schwach
gewölbtes Randfeld. Gestrichelt eine geschlossene Schachtel um die obere Platte; nur ihre Unterseite der Fläche $A$ wird von Feldlinien
durchstoßen, und ein Zähler zeigt $E\cdot A$ neben $\frac{Q}{\varepsilon_0}$. Regler für $A$ und $d$ verändern die Anordnung bei fester
Spannung; ein zweiter Zähler zeigt die Ladung, die mit $A$ wächst und mit $d$ fällt. Kernaussage: Das ganze Feld der Plusplatte tritt durch
die Spaltfläche, daraus folgt $C=\varepsilon_0\frac Ad$. (Rot = Platten und Ladungen, blau = Feldlinien, orange = Zähler, gestrichelt =
Gauß-Schachtel, grau = Randfeld.)
:::

:::herleitung
**Schritt 1: der Fluss einer Ladung.** Um eine Punktladung $Q$ hat das Feld auf einer Kugel vom Radius $r$ überall den Betrag
$\frac{Q}{4\pi\varepsilon_0r^2}$ und zeigt nach außen. Feld mal Kugelfläche hängt deshalb nicht vom Radius ab:

$$E\cdot4\pi r^2 = \frac{Q}{\varepsilon_0}.$$

Das __Gaußsche Gesetz__ verallgemeinert das auf jede geschlossene Fläche: Die Summe aus Normalkomponente des Felds mal Flächenstück, der
__elektrische Fluss__, ist die eingeschlossene Ladung durch $\varepsilon_0$. Es ist die genaue Form des Feldlinienzählens aus dem Artikel
über das Feld und folgt allgemein aus Maxwells Gleichungen.

**Schritt 2: das Feld im Spalt.** Im idealen Plattenkondensator laufen alle Feldlinien der Plusplatte gerade durch den Spalt zur
Minusplatte; außen ist kein Feld. Eine geschlossene Schachtel um die Plusplatte wird nur auf ihrer Innenseite mit der Fläche $A$ vom Feld
durchsetzt:

$$E\cdot A = \frac{Q}{\varepsilon_0}, \qquad E = \frac{Q}{\varepsilon_0\,A}.$$

**Schritt 3: Spannung und Kapazität.** Im homogenen Feld ist die Spannung Feld mal Abstand:

$$U = E\cdot d = \frac{Q\,d}{\varepsilon_0\,A}, \qquad C = \frac{Q}{U} = \varepsilon_0\,\frac{A}{d}.$$

Mit Dielektrikum ist das Feld bei gleicher Ladung um den Faktor $\varepsilon_\text{r}$ schwächer, wie der nächste Abschnitt zeigt, und aus
$\varepsilon_0$ wird $\varepsilon_0\,\varepsilon_\text{r}$.
:::

::::beispiel Ein Plattenkondensator in Zahlen
**(a) Luft im Spalt.** Zwei Platten von $10\,\text{cm}$ mal $10\,\text{cm}$, also $0{,}01\,\text{m}^2$, im Abstand $0{,}1\,\text{mm}$; die Feldkonstante
ist rund $8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}}$:

$$C = 8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}}\cdot\frac{0{,}01\,\text{m}^2}{10^{-4}\,\text{m}} \approx 8{,}85\cdot10^{-10}\,\text{F} = 885\,\text{pF}.$$

An $100\,\text{V}$ trägt er die Ladung $88{,}5\,\text{nC}$, und das Feld im Spalt ist auf beiden Wegen dasselbe:

$$E = \frac{U}{d} = \frac{100\,\text{V}}{10^{-4}\,\text{m}} = 10^{6}\,\frac{\text{V}}{\text{m}}, \qquad E = \frac{Q}{\varepsilon_0\,A} = \frac{8{,}85\cdot10^{-8}\,\text{C}}{8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}}\cdot0{,}01\,\text{m}^2} \approx 10^{6}\,\frac{\text{V}}{\text{m}}.$$

**(b) Keramik im Spalt.** Mit einer Kondensatorkeramik der Permittivitätszahl $1000$ wird daraus $0{,}885\,\mu\text{F}$.

**(c) Ein Farad aus Luft.** Bei $1\,\text{mm}$ Abstand bräuchte man die Fläche

$$A = \frac{C\,d}{\varepsilon_0} = \frac{1\,\text{F}\cdot10^{-3}\,\text{m}}{8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}}} \approx 1{,}13\cdot10^{8}\,\text{m}^2,$$

gut $110\,\text{km}^2$ — ein Quadrat von über zehn Kilometern Seitenlänge.

**Im Bild:** Bei (c) wird klar, warum ein Farad riesig ist: Eine Luftmembran ist sehr steif. Weich wird sie erst mit großer Fläche, winzigem
Abstand und einem Material, das gut nachgibt.
::::

## Das Dielektrikum

**Polarisation.** Im Feld verschieben sich in jedem Atom oder Molekül eines Isolators die Elektronenhülle und der Kern ein wenig gegeneinander,
und schon vorhandene Dipolmoleküle wie Wasser drehen sich in Feldrichtung. Das Material wird __polarisiert__: An seiner Oberfläche zur
Plusplatte sitzen dann negative, zur Minusplatte positive __gebundene Ladungen__. Ihr Feld zeigt dem Feld der Platten entgegen und schwächt
es im Inneren.

Bei gleicher Ladung auf den Platten ist das Feld deshalb um die Permittivitätszahl schwächer:

$$E = \frac{Q}{\varepsilon_0\,\varepsilon_\text{r}\,A}.$$

Damit ist auch die Spannung um diesen Faktor kleiner — und bei gleicher Spannung nimmt der Kondensator entsprechend mehr Ladung auf.

**Im Bild:** Ein weicheres Membranmaterial. Es gibt bei gleichem Druck weiter nach und nimmt mehr Wasser auf.

:::grafik
Szene: get1/kondensator/01-polarisation · Vorlage: dielektrikum-dipole
Der Spalt eines Plattenkondensators, gefüllt mit vielen kleinen Atomen als Kreise. Ein Regler schaltet das Feld ein: In jedem Atom verschiebt
sich die Elektronenwolke ein wenig zur Plusplatte, aus den Kreisen werden kleine Dipole mit dem negativen Ende zur Plusplatte. An den beiden
Oberflächen des Dielektrikums leuchten die übrig bleibenden gebundenen Ladungen auf. Daneben drei Feldpfeile: das Feld der Platten, das
Gegenfeld der gebundenen Ladungen und das geschwächte Gesamtfeld, um den Faktor $\varepsilon_\text{r}$ kürzer. Kernaussage: Das polarisierte
Dielektrikum schwächt das Feld und erhöht so die Kapazität. (Rot = Platten, blau = Feldpfeile, orange = gebundene Ladungen und Dipole, grau =
Atomrümpfe.)
:::

:::herleitung
Die Permittivitätszahl ist genau als dieser Faktor festgelegt, um den das Feld im Material bei gleicher Ladung auf den Platten geschwächt ist;
wie groß er ist, hängt davon ab, wie leicht sich das Material polarisieren lässt, und wird gemessen. Mit dem geschwächten Feld folgt wie im
Plattenkondensator

$$U = E\cdot d = \frac{Q\,d}{\varepsilon_0\,\varepsilon_\text{r}\,A}, \qquad C = \frac{Q}{U} = \varepsilon_0\,\varepsilon_\text{r}\,\frac{A}{d}.$$
:::

Einige Permittivitätszahlen aus dem Skript:

| Isolator | Permittivitätszahl |
|---|---|
| Luft | $1$ |
| Papier | etwa $2$ |
| Glimmer | etwa $5$ |
| Porzellan | etwa $6$ |
| Wasser | etwa $81$ |
| Kondensatorkeramik | $60$ bis $3000$ |

Wasser hat einen so großen Wert, weil seine Moleküle schon von sich aus Dipole sind, die sich im Feld drehen. Wie dünn ein Dielektrikum sein
darf, begrenzt seine Durchschlagsfestigkeit: Bei gleicher Spannung wächst das Feld, je dünner es ist.

**Selbstentladung.** Ein ideales Dielektrikum leitet gar nicht; sein __Isolationswiderstand__ $R_\text{I}$ ist unendlich, und der Kondensator
behält seine Ladung. Ein reales leitet ein wenig, und die Ladung sickert mit der Zeit durch das Dielektrikum. Wie schnell, beschreibt das
Produkt aus Isolationswiderstand und Kapazität. Für einen Plattenkondensator hängt es nur vom Material ab, vom spezifischen Widerstand $\rho$
und der Permittivität:

$$R_\text{I}\,C = \rho\,\varepsilon.$$

Das Skript sagt dazu, die Selbstentladung hänge von $\varepsilon$ ab; genau das steckt in dieser Formel.

**Im Bild:** Eine winzige undichte Stelle in der Membran. Wie schnell das Wasser durchsickert, hängt vom Material ab, nicht von der Größe der
Membran: Eine größere Membran lässt mehr durch, hält aber auch mehr.

:::herleitung
Ein Quader aus einem Material mit dem spezifischen Widerstand $\rho$, der Länge $d$ und dem Querschnitt $A$ hat nach Kapitel 5 den Widerstand
$\rho$ mal Länge durch Querschnitt. Mit der Kapazität des Plattenkondensators kürzen sich Fläche und Abstand:

$$R_\text{I}\,C = \rho\,\frac{d}{A}\cdot\varepsilon\,\frac{A}{d} = \rho\,\varepsilon.$$

Ohm mal Farad ist eine Sekunde, wie im Artikel über Einheiten: $R_\text{I}C$ ist eine Zeit. Wie die Spannung mit dieser Zeit abfällt, zeigt
der Artikel über Laden und Entladen.
:::

::::beispiel Wie lange hält die Ladung?
**(a) Eine Kunststofffolie** mit dem spezifischen Widerstand $10^{15}\,\Omega\,\text{m}$ und der Permittivitätszahl $2{,}2$:

$$R_\text{I}\,C = 10^{15}\,\Omega\,\text{m}\cdot2{,}2\cdot8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}} \approx 1{,}9\cdot10^{4}\,\text{s},$$

gut fünf Stunden — gleichgültig, wie groß der Kondensator ist.

**(b) Reines Wasser** hat zwar die große Permittivitätszahl $81$, aber nur den spezifischen Widerstand von etwa $1{,}8\cdot10^{5}\,\Omega\,\text{m}$:

$$R_\text{I}\,C = 1{,}8\cdot10^{5}\,\Omega\,\text{m}\cdot81\cdot8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}} \approx 1{,}3\cdot10^{-4}\,\text{s}.$$

Ein Wasserkondensator wäre nach einem Zehntel einer Millisekunde schon spürbar entladen.

**Im Bild:** Eine weiche, aber poröse Membran nützt nichts. Ein gutes Dielektrikum muss nachgiebig **und** dicht sein.
::::

## Die gespeicherte Energie

Um die Ladungen zu trennen, verrichtet man Arbeit gegen ihre gegenseitige Anziehung. Sie steckt danach im Kondensator:

:::formel
$$W = \frac12\,C\,U^2 = \frac{Q^2}{2C} = \frac12\,Q\,U.$$
:::

**So liest man das:** Nicht Ladung mal Spannung, sondern die Hälfte. Die ersten Ladungen wandern noch bei fast null Volt hinüber, die letzten
bei der vollen Spannung — im Mittel bei der halben.

**Im Bild:** Die gespannte Membran wie eine gespannte Feder, deren Energie halbe Steifigkeit mal Auslenkung zum Quadrat ist. Hier ist die
Steifigkeit der Kehrwert der Kapazität und die Auslenkung die verschobene Ladung.

:::grafik
Szene: get1/kondensator/01-energie-dreieck · Vorlage: ladung-spannung-diagramm
Ein Diagramm mit der Spannung nach rechts und der Ladung nach oben; eine Gerade durch den Ursprung mit der Steigung $C$. Ein Regler lädt den
Kondensator in kleinen Schritten: Jeder Schritt bringt ein Ladungsstück $dq$ bei der gerade erreichten Spannung hinüber und färbt einen dünnen
Streifen der Breite $dq$ und der Länge $\frac qC$; die Streifen füllen nach und nach das Dreieck unter der Geraden. Gestrichelt das Rechteck
$Q\,U$, von dem das Dreieck genau die Hälfte ist. Kernaussage: Die gespeicherte Energie ist die Dreiecksfläche $\frac12QU$. (Blau = Gerade,
rot = gefüllte Streifen, orange = aktueller Schritt, gestrichelt = Rechteck, grau = Achsen.)
:::

:::herleitung
Trägt der Kondensator schon die Ladung $q$, liegt an ihm die Spannung $\frac{q}{C}$. Ein weiteres kleines Ladungsstück $dq$ von der Minus- zur
Plusplatte zu bringen, kostet nach dem Artikel über Spannung Ladung mal Spannung:

$$dW = \frac{q}{C}\;dq, \qquad W = \int_0^Q\frac{q}{C}\;dq = \frac{Q^2}{2C}.$$

Die Integrationsvariable heißt $q$, weil $Q$ schon die Endladung ist. Mit $Q=C\,U$ folgen die anderen beiden Formen. Im
Ladung-Spannung-Diagramm ist $W$ die Dreiecksfläche unter der Geraden durch den Ursprung, halb so groß wie das Rechteck $Q\,U$. Das Skript
rechnet dasselbe über Kraft mal Weg: Auf das Ladungsstück wirkt im Spalt die Kraft Ladung mal Feld, und längs des Abstands $d$ verschoben
ergibt das Ladung mal $E\,d$, also Ladung mal Spannung.
:::

**Die Energie sitzt im Feld.** Im Plattenkondensator verteilt sie sich gleichmäßig auf das Volumen zwischen den Platten, Fläche mal Abstand,
mit der __Energiedichte__

$$w = \frac{W}{A\,d} = \frac12\,\varepsilon\,E^2.$$

**Im Bild:** Bei der gedehnten Membran steckt die Energie im Gummi, nicht im Wasser — beim Kondensator im Feld, nicht in den Ladungen.

:::herleitung
Man setzt die Kapazität des Plattenkondensators und die Spannung im homogenen Feld ein:

$$W = \frac12\cdot\varepsilon\,\frac{A}{d}\cdot\big(E\,d\big)^2 = \frac12\,\varepsilon\,E^2\cdot A\,d.$$

Geteilt durch das Volumen bleibt die Energiedichte.
:::

::::beispiel Energie in Zahlen
**(a) Der Elko** von $100\,\mu\text{F}$ an $12\,\text{V}$:

$$W = \frac12\cdot10^{-4}\,\text{F}\cdot(12\,\text{V})^2 = 7{,}2\cdot10^{-3}\,\text{J}.$$

**(b) Ein Doppelschichtkondensator** von $3000\,\text{F}$ an $2{,}7\,\text{V}$:

$$W = \frac12\cdot3000\,\text{F}\cdot(2{,}7\,\text{V})^2 \approx 1{,}09\cdot10^{4}\,\text{J}.$$

Damit ließe sich ein Kilogramm um über einen Kilometer anheben.

**(c) Der Luftkondensator** von $885\,\text{pF}$ an $100\,\text{V}$, mit dem Feld $10^6\,\frac{\text{V}}{\text{m}}$ im Volumen $10^{-6}\,\text{m}^3$:

$$w = \frac12\cdot8{,}854\cdot10^{-12}\,\frac{\text{A}\,\text{s}}{\text{V}\,\text{m}}\cdot\Big(10^{6}\,\frac{\text{V}}{\text{m}}\Big)^2 \approx 4{,}43\,\frac{\text{J}}{\text{m}^3}, \qquad W = w\cdot10^{-6}\,\text{m}^3 \approx 4{,}43\cdot10^{-6}\,\text{J}.$$

Dasselbe ergibt $\frac12CU^2$ mit $885\,\text{pF}$ und $100\,\text{V}$.

**Im Bild:** Die Energie wächst mit dem Quadrat der Spannung: Doppelter Druck dehnt die Membran doppelt so weit, gegen doppelte Gegenkraft —
viermal so viel Arbeit.
::::

## Bedeutung und Ausblick

Kondensatoren sind überall. Sie glätten die Spannung in Netzteilen, puffern die Versorgung jedes Chips, speichern die Energie für den Blitz
einer Kamera und bestimmen in Filtern und Schwingkreisen die Frequenz. In einem dynamischen Arbeitsspeicher ist jedes Bit eine winzige Ladung
auf einem Kondensator von einigen Femtofarad.

Der nächste Artikel schaltet mehrere Kondensatoren zusammen, parallel und in Reihe, und zeigt, warum dabei die Ladungserhaltung entscheidet.
Danach folgt der zeitliche Verlauf beim Laden und Entladen über einen Widerstand.

:::kern
- Ein __Kondensator__ trennt Ladung auf zwei Elektroden; durch das Dielektrikum fließt kein Strom.
- __Kapazität__: $C=\frac QU$, Einheit Farad; Ladung und Spannung sind proportional, weil das Feld mit der Ladung wächst.
- Am Kondensator ist $i_C=C\,\frac{du_C}{dt}$: Strom fließt nur, während sich die Spannung ändert — Gleichstrom wird gesperrt.
- __Plattenkondensator__: $C=\varepsilon_0\varepsilon_\text{r}\frac Ad$, hergeleitet aus dem Gaußschen Gesetz und Spannung gleich Feld mal Abstand.
- Ein __Dielektrikum__ polarisiert sich, schwächt das Feld um den Faktor $\varepsilon_\text{r}$ und erhöht so die Kapazität.
- Die Selbstentladung hängt nur vom Material ab: $R_\text{I}C=\rho\,\varepsilon$.
- Gespeicherte __Energie__: $W=\frac12CU^2$ — die Hälfte von Ladung mal Spannung, weil die Spannung beim Laden erst ansteigt.
- Die Energie sitzt im Feld, mit der Dichte $\frac12\varepsilon E^2$.
- Übliche Kapazitäten reichen von Femtofarad bis Millifarad; Doppelschichtkondensatoren erreichen tausende Farad bei wenigen Volt.
:::

:::quiz
F: Warum fließt durch einen geladenen Kondensator kein Gleichstrom, und was zeigt dazu das Bild der Membran?
A: Zwischen den Elektroden liegt ein Isolator; Ladung lässt sich nur auf die eine Elektrode schieben und von der anderen abziehen, nicht hindurch. Nach $i_C=C\frac{du_C}{dt}$ fließt nur Strom, solange sich die Spannung ändert. Im Bild wölbt sich die Membran, solange gepumpt wird; steht sie still, steht das Wasser, und ein ständiger Strom durch sie ist unmöglich.
F: Warum sind Ladung und Spannung am Kondensator proportional, und welche Ladung trägt ein Elko von $100\,\mu\text{F}$ an $12\,\text{V}$?
A: Doppelte Ladung erzeugt nach Coulomb und Superposition an jedem Punkt doppeltes Feld, und die Spannung ist das Wegintegral des Felds — also doppelte Spannung. Ihr Verhältnis, die Kapazität, ist fest. Der Elko trägt $Q=CU=1{,}2\,\text{mC}$, rund $7{,}5\cdot10^{15}$ Elementarladungen.
F: Wie hängen Strom und Spannung am Kondensator zusammen, und wie schnell steigt die Spannung beim Laden mit $2\,\text{mA}$?
A: Aus $q=Cu_C$ folgt durch Ableiten $i_C=C\frac{du_C}{dt}$; umgekehrt ist die Spannung der Anfangswert plus das Integral des Stroms durch $C$. Bei $2\,\text{mA}$ in $100\,\mu\text{F}$ steigt die Spannung um $20\,\frac{\text{V}}{\text{s}}$ und erreicht $12\,\text{V}$ nach $0{,}6\,\text{s}$.
F: Wie folgt die Formel des Plattenkondensators?
A: Nach dem Gaußschen Gesetz ist der Fluss durch eine geschlossene Fläche die eingeschlossene Ladung durch $\varepsilon_0$ — bei der Punktladung nachgerechnet, Feld mal Kugelfläche. Um die Plusplatte tritt das ganze Feld durch die Innenseite der Fläche $A$, also $E=\frac{Q}{\varepsilon_0A}$. Mit $U=E\,d$ wird $C=\frac QU=\varepsilon_0\frac Ad$, mit Dielektrikum zusätzlich mal $\varepsilon_\text{r}$.
F: Welche Kapazität haben Platten von $10\,\text{cm}$ mal $10\,\text{cm}$ mit $0{,}1\,\text{mm}$ Luft, und wie groß müssten sie für ein Farad bei $1\,\text{mm}$ sein?
A: $C=\varepsilon_0\frac Ad\approx885\,\text{pF}$; an $100\,\text{V}$ trägt er $88{,}5\,\text{nC}$, und das Feld ist $10^6\,\frac{\text{V}}{\text{m}}$, aus $\frac Ud$ wie aus $\frac{Q}{\varepsilon_0A}$. Für ein Farad bei $1\,\text{mm}$ Luftspalt bräuchte man rund $1{,}13\cdot10^8\,\text{m}^2$, gut $110\,\text{km}^2$.
F: Wie erhöht ein Dielektrikum die Kapazität, und warum hat Wasser ein so großes $\varepsilon_\text{r}$?
A: Das Feld polarisiert den Isolator: Hüllen und Kerne verschieben sich, Dipolmoleküle drehen sich. An der Oberfläche entstehen gebundene Ladungen, deren Feld das Plattenfeld schwächt — um den Faktor $\varepsilon_\text{r}$. Bei gleicher Ladung sinkt die Spannung, also steigt die Kapazität. Wasser hat mit etwa $81$ einen großen Wert, weil seine Moleküle schon Dipole sind, die sich drehen.
F: Warum hängt die Selbstentladung eines Plattenkondensators nur vom Material ab, und warum taugt Wasser trotz $\varepsilon_\text{r}=81$ nicht als Dielektrikum?
A: Der Isolationswiderstand ist $\rho\frac dA$, die Kapazität $\varepsilon\frac Ad$; im Produkt kürzen sich Fläche und Abstand zu $R_\text{I}C=\rho\varepsilon$, einer Zeit. Bei einer Folie mit $10^{15}\,\Omega\,\text{m}$ sind das rund $1{,}9\cdot10^4\,\text{s}$. Reines Wasser hat nur etwa $1{,}8\cdot10^5\,\Omega\,\text{m}$, also rund $1{,}3\cdot10^{-4}\,\text{s}$ — nach einem Zehntel einer Millisekunde merklich entladen.
F: Warum ist die gespeicherte Energie $\frac12CU^2$ und nicht $QU$?
A: Bei der Ladung $q$ liegt die Spannung $\frac qC$ an; ein weiteres Stück $dq$ kostet $\frac qC\,dq$. Das Integral von $0$ bis $Q$ gibt $\frac{Q^2}{2C}=\frac12CU^2=\frac12QU$. Die ersten Ladungen wandern bei fast null Volt, die letzten bei voller Spannung, im Mittel bei der halben — im Diagramm die Dreiecksfläche statt des Rechtecks.
F: Wo sitzt die Energie eines Kondensators, und wie groß ist die Energiedichte bei $10^6\,\frac{\text{V}}{\text{m}}$ in Luft?
A: Im Feld zwischen den Platten. Setzt man $C=\varepsilon\frac Ad$ und $U=Ed$ in $\frac12CU^2$ ein, entsteht $\frac12\varepsilon E^2$ mal Volumen; die Energiedichte ist also $\frac12\varepsilon E^2$. In Luft bei $10^6\,\frac{\text{V}}{\text{m}}$ sind das rund $4{,}43\,\frac{\text{J}}{\text{m}^3}$ — im Volumen von $10^{-6}\,\text{m}^3$ des Beispielkondensators genau sein $\frac12CU^2$.
F: Was bedeuten „selbstheilend" und „gepolt", und was leisten Doppelschichtkondensatoren?
A: Selbstheilend: Bei einem lokalen Durchschlag verdampft die dünne Metallschicht um die Fehlstelle, und der Kondensator arbeitet weiter. Gepolt: Er darf nur in einer Richtung an Spannung liegen; beim Elektrolytkondensator würde sonst die dünne Oxidschicht, sein Dielektrikum, abgebaut. Doppelschichtkondensatoren erreichen viele Farad bis zu einigen tausend, vertragen aber nur wenige Volt und haben einen höheren Leckstrom; $3000\,\text{F}$ an $2{,}7\,\text{V}$ speichern rund $11\,\text{kJ}$.
:::
