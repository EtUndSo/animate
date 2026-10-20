---
title: Der ohmsche Widerstand und das Ohmsche Gesetz
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50200
summary: Von Grund auf – warum ein Draht dem Strom etwas entgegensetzt und warum der Strom dabei genau proportional zur Spannung wird. Leitbild ist ein schräges Nagelbrett: Kugeln rollen an, prallen gegen Nägel, rollen wieder an und kommen so mit einer festen mittleren Geschwindigkeit voran, die zur Neigung passt. Mit Beschleunigung im Feld, Sägezahn-Modell und Driftgeschwindigkeit, Beweglichkeit, Leitfähigkeit und spezifischem Widerstand, dem Ohmschen Gesetz für ein Leiterstück, Leitwert und Kennlinie, Stromwärme, Bauformen, E-Reihen und Farbcode, Kalt- und Heißleitern sowie linearen und nichtlinearen Zweipolen. Mit Beispiel-Seite.
tags: ohmscher Widerstand, Ohmsches Gesetz, spezifischer Widerstand, Leitwert, Kennlinie, Temperaturabhängigkeit
---

## Anschaulich

Ein Draht lässt nicht beliebig viel Strom durch. Legt man eine Spannung an, stellt sich ein ganz bestimmter Strom ein — und bei Metallen fließt
genau doppelt so viel, wenn man die Spannung verdoppelt. Dieser Artikel klärt, woher die Bremse im Draht kommt und warum sie so gleichmäßig wirkt.

**Das Leitbild dieses Artikels:** **ein schräges Nagelbrett**. Kugeln rollen ein geneigtes Brett hinab, das dicht mit Nägeln besetzt ist. Ohne Nägel
würden sie immer schneller. Mit Nägeln rollen sie ein Stück, prallen gegen einen Nagel, verlieren ihren Schwung und rollen wieder an. So stellt sich
eine gleichbleibende mittlere Geschwindigkeit ein, und die ist umso größer, je steiler das Brett steht.

Ein Metalldraht ist ein solches Brett. Schaut man in das volle Rohr aus dem Artikel über den Strom hinein, sieht man dort keine glatte Strömung,
sondern genau dieses Gewimmel: Die Kugeln sind die Leitungselektronen, die Nägel die Störstellen im Kristallgitter, an denen sie abprallen, und die
Neigung ist das elektrische Feld im Draht. Der Höhenunterschied zwischen oberem und unterem Rand ist die Spannung — wie auf der Wanderkarte im Artikel
über das Potenzial, wo Spannung ein Höhenunterschied war.

Drei Folgerungen kann man dem Brett direkt ansehen:

- **Strom proportional zur Spannung.** Doppelter Höhenunterschied bei gleicher Länge heißt doppelte Neigung, doppelte mittlere Geschwindigkeit und
  doppelt so viele Kugeln pro Sekunde über die Ziellinie. Das ist das __Ohmsche Gesetz__.
- **Länge und Breite zählen.** Ein doppelt so langes Brett mit demselben Höhenunterschied ist nur halb so steil, es kommt halb so viel an. Ein doppelt
  so breites Brett hat doppelt so viele Bahnen nebeneinander, es kommt doppelt so viel an. Der __Widerstand__ wächst mit der Länge und sinkt mit der
  Breite.
- **Die Energie wird zu Wärme.** Die Kugeln kommen unten nicht schneller an als oben. Was sie beim Hinabrollen an Höhenenergie verlieren, geben sie bei
  den Stößen an die Nägel ab, die davon zu zittern beginnen — im Draht ist das Wärme.

Das Brett ist eine Analogie. Wir lassen die Kugeln bergab rollen wie gedachte positive Ladungen in technischer Stromrichtung; echte Elektronen laufen
andersherum, am Strom ändert das nichts, wie im Artikel über den Strom gezeigt. Wo das Bild sonst nicht trägt — vor allem bei der Frage, woran die
Elektronen wirklich abprallen —, steht es unten dabei.

:::grafik
Szene: get1/stroeme-und-spannungen/02-nagelbrett · Vorlage: nagelbrett-drift
Ein geneigtes Brett, dicht mit Nägeln besetzt; oben fallen laufend Kugeln ein, unten quert eine Ziellinie mit Zähler (Kugeln pro Sekunde). Ein Schalter
„Nägel aus" zeigt zuerst das leere Brett: Die Kugeln werden immer schneller, eine Geschwindigkeitsanzeige wächst ohne Grenze. Mit Nägeln rollt jede
Kugel an, prallt, verliert ihren Schwung und rollt wieder an; eine markierte Kugel zieht eine Zickzackspur, ihre mittlere Geschwindigkeit bleibt
konstant. Regler 1 ändert die Neigung: Die mittlere Geschwindigkeit und der Zähler wachsen im selben Verhältnis, ein Diagramm daneben trägt den Zähler
über dem Höhenunterschied auf und zeigt eine Gerade durch den Ursprung. Regler 2 verlängert das Brett bei festem Höhenunterschied (flacher, weniger
Kugeln pro Sekunde), Regler 3 verbreitert es (mehr Bahnen, mehr Kugeln). Bei jedem Stoß zittert der getroffene Nagel kurz. Kernaussage: Die Stöße
machen aus der Beschleunigung eine feste mittlere Geschwindigkeit, die zur Neigung proportional ist — darum ist der Strom proportional zur Spannung.
(Blau = Kugeln, rot = markierte Kugel und ihre mittlere Geschwindigkeit, orange = Stöße und zitternde Nägel, grau = Brett, Nägel und Achsen.)
:::

## Wie ein Elektron im Leiter vorankommt

**Ein Feld im Draht.** Im Artikel über das elektrische Feld war das Innere eines Leiters im Ruhezustand feldfrei: Die beweglichen Ladungen verschieben
sich so lange, bis kein Feld mehr übrig ist. Das gilt nur, solange kein Strom fließt. Hält eine Quelle zwischen den Drahtenden eine Spannung aufrecht, kommt dieser
Ausgleich nie zur Ruhe — im Draht bleibt ein Feld $\vec E$, und das treibt die Elektronen an.

**Die Akteure:**

- das __Elektron__ mit der Ladung $-e$ und der Masse $m_\text{e}$, rund $9{,}109\cdot10^{-31}\,\text{kg}$;
- das __Feld__ $\vec E$ im Draht, ein Vektor in Volt pro Meter.

Auf eine Ladung $Q$ wirkt im Feld die Kraft $Q\vec E$, und eine Kraft beschleunigt eine Masse $m$ nach dem Newtonschen Gesetz. Zusammen ergibt das die
Beschleunigung, allgemein und für das Elektron (das Skript schreibt die Ladung klein, $q$):

$$\vec a = \frac{Q}{m}\,\vec E, \qquad \vec a = -\frac{e}{m_\text{e}}\,\vec E.$$

**So liest man das:** Eingabe ist das Feld, ein Vektor in Volt pro Meter; Ausgabe ist die Beschleunigung, ein Vektor in Meter pro Quadratsekunde. Beim
Elektron zeigt sie gegen das Feld, weil es negativ ist. Ihr Betrag ist riesig, denn ein Elektron ist extrem leicht: Das Verhältnis $e/m_\text{e}$ beträgt
rund $1{,}76\cdot10^{11}$ Coulomb pro Kilogramm.

**Im Bild:** Die Neigung des Bretts beschleunigt jede Kugel gleich stark. Ohne Nägel würde sie ohne Ende schneller.

:::herleitung
**Kraft im Feld.** Nach dem Artikel über das elektrische Feld wirkt auf eine Ladung $Q$ die Kraft

$$\vec F = Q\,\vec E.$$

**Newton.** Nach dem Artikel über Größen und Einheiten beschleunigt eine Kraft eine Masse $m$ gemäß

$$\vec F = m\,\vec a.$$

**Gleichsetzen.** Beide Ausdrücke beschreiben dieselbe Kraft. Gleichsetzen und durch $m$ teilen gibt die Beschleunigung. Für das Elektron setzt man
$-e$ für die Ladung und $m_\text{e}$ für die Masse ein. Das Minus dreht die Richtung um: Das Elektron wird gegen das Feld beschleunigt, zum Pluspol hin.
:::

::::beispiel Ein Elektron ohne Nägel
Wir nehmen das Feld in einem Kupferdraht von $1{,}5\,\text{mm}^2$ mit $1\,\text{A}$, wie im Artikel über den Strom. Es beträgt rund
$11{,}9\,\text{mV}/\text{m}$; nachrechnen lässt sich das unten mit der Leitfähigkeit. Ein Elektron, das in diesem Feld frei fliegen könnte, etwa im
Vakuum einer Elektronenröhre, erführe die Beschleunigung

$$a = \frac{e}{m_\text{e}}\,E = 1{,}76\cdot10^{11}\,\frac{\text{C}}{\text{kg}}\cdot0{,}0119\,\frac{\text{V}}{\text{m}} \approx 2{,}1\cdot10^{9}\,\frac{\text{m}}{\text{s}^2}.$$

Aus der Ruhe heraus wäre es nach einer Mikrosekunde und nach einer Millisekunde schon

$$v(1\,\mu\text{s}) \approx 2{,}1\,\frac{\text{km}}{\text{s}}, \qquad v(1\,\text{ms}) \approx 2100\,\frac{\text{km}}{\text{s}}$$

schnell, und es würde immer schneller. Im Draht dagegen wandern die Elektronen nach dem Artikel über den Strom mit knapp
$0{,}05\,\frac{\text{mm}}{\text{s}}$, und zwar dauerhaft.

**Im Bild:** Das Brett ohne Nägel. Etwas im Draht muss die Elektronen ständig wieder abbremsen.
::::

**Die Stöße.** Das Skript beschreibt das Abbremsen mit einem einfachen Modell. Ein Elektron fliegt im Mittel die Strecke $\lambda$, die
__mittlere freie Weglänge__, in der Zeit $T$, der __Laufzeit__, und stößt dann mit dem Kristallgitter zusammen. Dabei verliert es nach dem Modell seine
gesamte Bewegungsenergie und startet danach aus der Ruhe neu. Zwischen zwei Stößen wächst seine Geschwindigkeit also gleichmäßig von null bis zum
Höchstwert

$$v_\text{max} = \frac{e\,E}{m_\text{e}}\,T.$$

Dabei ist $E$ der Betrag des Felds. Über der Zeit aufgetragen, ergibt das einen __Sägezahn__: Anstieg, Absturz auf null, Anstieg, Absturz.

**Im Bild:** Die Kugel rollt von einem Nagel zum nächsten an und bleibt dort kurz liegen. Die Zeit zwischen zwei Nägeln ist $T$.

:::grafik
Szene: get1/stroeme-und-spannungen/02-saegezahn · Vorlage: saegezahn-drift
Oben ein Ausschnitt des Nagelbretts mit einer markierten Kugel, darunter das Diagramm ihrer Geschwindigkeit über der Zeit. Im Modell des Skripts steigt
die Geschwindigkeit in jedem Flug linear von $0$ auf $v_\text{max}$ und fällt beim Stoß auf $0$ zurück: Sägezähne bei $T$, $2T$, $3T$ … Eine gestrichelte
Linie auf halber Höhe markiert den Mittelwert $\tfrac12v_\text{max}$; ein Dreieck ist schraffiert, seine Fläche ist der Weg in einem Flug. Regler für das
Feld $E$ machen alle Zähne gleichmäßig höher oder flacher, die Mittellinie wandert proportional mit. Ein Umschalter „zufällige Flugzeiten" lässt die
Zähne verschieden lang werden, bei gleicher mittlerer Flugzeit $T$; die Mittellinie steigt dann auf das Doppelte. Kernaussage: Die mittlere
Geschwindigkeit ist proportional zum Feld. (Blau = Geschwindigkeitsverlauf, rot = Mittelwert $v_\text{D}$, orange = Stöße, grau = Achsen, gestrichelt =
$v_\text{max}$.)
:::

Gemittelt über einen Zahn ist die Geschwindigkeit die Hälfte des Höchstwerts. Sie ist konstant und zeigt gegen das Feld, und das Skript nennt sie die
__Driftgeschwindigkeit__ $\vec v_\text{D}$. Im Modell ist die Konstante davor $\frac{eT}{2m_\text{e}}$; allgemein heißt sie __Beweglichkeit__:

:::formel
$$\vec v_\text{D} = -\mu_\text{e}\,\vec E, \qquad \mu_\text{e} = \frac{e\,T}{2\,m_\text{e}} \quad\text{(Sägezahn-Modell)}.$$
:::

**So liest man das:** Eingabe ist das Feld, Ausgabe die mittlere Geschwindigkeit der Elektronen, beide Vektoren. Die __Beweglichkeit__ $\mu_\text{e}$
ist eine positive Materialkonstante; sie sagt, wie viel Driftgeschwindigkeit ein Volt pro Meter bringt, Einheit Meter pro Sekunde je Volt pro Meter,
also $\frac{\text{m}^2}{\text{V}\,\text{s}}$. Das Minus heißt: Die Elektronen driften gegen das Feld. Entscheidend ist, dass $\vec v_\text{D}$ proportional zu
$\vec E$ ist und nicht mit der Zeit wächst — darauf beruht das Ohmsche Gesetz. Im Artikel über den Strom stand nur der Betrag, kurz $v_\text{D}$.

**Im Bild:** Die mittlere Rollgeschwindigkeit auf dem Brett ist proportional zur Neigung. Eine große Beweglichkeit heißt: lange freie Strecken zwischen
den Nägeln und leichte Kugeln.

:::herleitung
**Schritt 1: der Anstieg.** Zwischen zwei Stößen wirkt die konstante Beschleunigung vom Betrag $\frac{e}{m_\text{e}}E$, und das Elektron startet bei null.
Seine Geschwindigkeit wächst deshalb linear mit der Zeit $t$ seit dem letzten Stoß:

$$v(t) = \frac{e\,E}{m_\text{e}}\,t, \qquad 0\le t\le T.$$

Bei $t=T$ erreicht sie den Höchstwert $v_\text{max}$.

**Schritt 2: der Mittelwert.** Der Mittelwert einer Geschwindigkeit über eine Zeitspanne ist der zurückgelegte Weg geteilt durch die Zeit. Der Weg ist
die Fläche unter der Kurve, hier ein Dreieck mit der Grundseite $T$ und der Höhe $v_\text{max}$:

$$\bar v = \frac{1}{T}\cdot\frac{1}{2}\,T\,v_\text{max} = \frac{1}{2}\,v_\text{max} = \frac{e\,T}{2\,m_\text{e}}\,E.$$

Jeder Zahn sieht gleich aus, also gilt dieser Mittelwert auch über viele Zähne.

**Schritt 3: die Richtung.** Die Beschleunigung zeigt gegen $\vec E$, also auch die mittlere Geschwindigkeit. Als Vektor ist sie deshalb
$-\frac{eT}{2m_\text{e}}\,\vec E$; die Konstante heißt $\mu_\text{e}$.

**Im Bild:** Steht das Brett doppelt so steil, rollt die Kugel zwischen zwei Nägeln doppelt so schnell an. Jeder Zahn wird doppelt so hoch, der
Mittelwert ebenfalls.
:::

::::beispiel Driften im Kupfer
Gemessen hat Kupfer eine Beweglichkeit der Leitungselektronen von rund

$$\mu_\text{e} \approx 4{,}1\cdot10^{-3}\,\frac{\text{m}^2}{\text{V}\,\text{s}} = 41\,\frac{\text{cm}^2}{\text{V}\,\text{s}}.$$

Wie dieser Wert aus der Leitfähigkeit folgt, zeigt der nächste Abschnitt. Im Feld von $11{,}9\,\text{mV}/\text{m}$ des Drahts mit $1\,\text{A}$ driften
die Elektronen mit

$$v_\text{D} = \mu_\text{e}\,E = 4{,}1\cdot10^{-3}\,\frac{\text{m}^2}{\text{V}\,\text{s}}\cdot0{,}0119\,\frac{\text{V}}{\text{m}} \approx 4{,}9\cdot10^{-5}\,\frac{\text{m}}{\text{s}}.$$

Das ist dieselbe Driftgeschwindigkeit wie im Artikel über den Strom, dort aus Strom, Trägerdichte und Querschnitt berechnet — zwei Wege, ein Ergebnis.
Im Sägezahn-Modell ist der Höchstwert doppelt so groß, rund $9{,}8\cdot10^{-5}\,\frac{\text{m}}{\text{s}}$, und die Laufzeit folgt aus der Formel für
die Beweglichkeit:

$$T = \frac{2\,m_\text{e}\,\mu_\text{e}}{e} = \frac{2\cdot9{,}109\cdot10^{-31}\,\text{kg}\cdot4{,}1\cdot10^{-3}\,\frac{\text{m}^2}{\text{V}\,\text{s}}}{1{,}602\cdot10^{-19}\,\text{C}} \approx 4{,}7\cdot10^{-14}\,\text{s}.$$

Rund $47$ Femtosekunden zwischen zwei Stößen.

**Im Bild:** Die Kugel stößt unvorstellbar oft, gut zwanzig Billionen Mal pro Sekunde, und kommt deshalb trotz steilem Brett kaum voran.
::::

**Was am Modell vereinfacht ist.** Der Sägezahn trifft das Wesentliche — die mittlere Geschwindigkeit ist proportional zum Feld —, ist aber in drei
Punkten zu grob.

**Erstens: Das Elektron bleibt nicht stehen.** Nach dem Artikel über den Strom flitzen die Leitungselektronen auch ohne Feld ungeordnet mit über tausend
Kilometern pro Sekunde durch das Metall. Ein Stoß hält ein Elektron nicht an, er wirft es in eine zufällige neue Richtung. Verloren geht dabei die
kleine Zusatzgeschwindigkeit in Feldrichtung, die es seit dem letzten Stoß aufgenommen hat: Über viele Elektronen gemittelt, hat die neue Richtung
keine Vorzugsrichtung. Für die Drift ist das genau die Annahme „Start bei null", nur eben für den gerichteten Anteil und nicht für die ganze Bewegung.
Die Energie, die das Feld zwischen zwei Stößen hineinsteckt, gibt das Elektron beim Stoß an das Gitter ab.

**Zweitens: Die Flugzeiten sind zufällig.** Nicht jeder Flug dauert genau gleich lang; mal stößt ein Elektron früher, mal später. Ist $T$ die
mittlere Flugzeit, entfällt dann der Faktor $\frac12$, und die Beweglichkeit wird

$$\mu_\text{e} = \frac{e\,T}{m_\text{e}}.$$

So steht sie in den meisten Lehrbüchern; das Modell heißt nach Paul Drude __Drude-Modell__. An der Proportionalität zum Feld ändert sich nichts.

**Drittens: Woran das Elektron stößt.** Nicht an jedem Atom. Ein Elektron verhält sich auch wie eine Welle, und eine Welle läuft durch ein vollkommen
regelmäßiges, ruhendes Gitter ungestört hindurch — eine Folge der Quantenmechanik. Gestreut wird es nur an Abweichungen von der Ordnung: an den
Wärmeschwingungen der Atomrümpfe, die mit der Temperatur zunehmen, und an Fremdatomen und Gitterfehlern. Darum ist die freie Weglänge viel größer als
der Abstand zweier Atome.

**Im Bild:** Die Nägel sind nicht die Atome selbst, sondern die Störungen: zitternde Atome und eingestreute Fremdkörper. Dass ein perfekt geordnetes,
ruhendes Gitter gar nicht bremst, hat im Nagelbrett keine Entsprechung — hier ist das Bild schief. Bild 5.3 des Skripts, das Elektron im Zickzack von
Atom zu Atom, ist in diesem Sinn eine Skizze und keine Momentaufnahme.

:::herleitung
**Der Mittelwert über viele Flüge.** Ein Elektron fliegt nacheinander die Zeiten $t_1, t_2, \dots, t_M$. Im Flug $k$ startet sein gerichteter Anteil bei
null und legt in Feldrichtung den Weg einer gleichmäßigen Beschleunigung zurück:

$$s_k = \frac{1}{2}\,a\,t_k^2, \qquad a = \frac{e\,E}{m_\text{e}}.$$

Die mittlere Driftgeschwindigkeit ist der Gesamtweg geteilt durch die Gesamtzeit:

$$v_\text{D} = \frac{\sum_k \frac12\,a\,t_k^2}{\sum_k t_k} = \frac{a}{2}\cdot\frac{\langle t^2\rangle}{\langle t\rangle}.$$

Dabei sind $\langle t\rangle$ und $\langle t^2\rangle$ die Mittelwerte von $t$ und $t^2$ über alle Flüge. Dauern alle Flüge genau $T$ wie im Skript, ist
der Quotient $T$, und es bleibt der Sägezahn-Wert $\frac{a}{2}\,T$.

**Zufällige Flugzeiten.** Realistischer ist: In jedem kurzen Zeitstück $dt$ stößt ein Elektron mit derselben Wahrscheinlichkeit $\frac{dt}{T}$, egal wie
lange der letzte Stoß her ist. Dann schrumpft der Anteil $p(t)$ der Flüge, die länger als $t$ dauern, in jedem Zeitstück um den Bruchteil
$\frac{dt}{T}$:

$$\frac{dp}{dt} = -\frac{p}{T}, \qquad p(t) = \exp\!\Big(-\frac{t}{T}\Big).$$

Die Wahrscheinlichkeitsdichte der Flugzeiten ist die negative Ableitung davon, $\frac1T\exp(-t/T)$. Die Mittelwerte folgen mit partieller Integration;
eine Stammfunktion der Dichte ist $-\exp(-t/T)$, und die Randterme bei $0$ und $\infty$ verschwinden:

$$\langle t\rangle = \int_0^\infty t\,\frac{1}{T}\,\exp\!\Big(-\frac{t}{T}\Big)\,dt = \int_0^\infty \exp\!\Big(-\frac{t}{T}\Big)\,dt = T,$$

$$\langle t^2\rangle = \int_0^\infty t^2\,\frac{1}{T}\,\exp\!\Big(-\frac{t}{T}\Big)\,dt = \int_0^\infty 2\,t\,\exp\!\Big(-\frac{t}{T}\Big)\,dt = 2\,T\,\langle t\rangle = 2\,T^2.$$

Eingesetzt:

$$v_\text{D} = \frac{a}{2}\cdot\frac{2\,T^2}{T} = a\,T = \frac{e\,T}{m_\text{e}}\,E.$$

**Warum doppelt so viel?** Lange Flüge zählen doppelt: Sie dauern länger, und in ihnen wird das Elektron auch schneller. Der Weg wächst mit dem Quadrat
der Flugzeit; darum heben die seltenen langen Flüge den Mittelwert stärker, als die häufigen kurzen ihn senken.
:::

::::beispiel Wie weit fliegt ein Elektron?
Mit der Beweglichkeit von Kupfer, $4{,}1\cdot10^{-3}\,\frac{\text{m}^2}{\text{V}\,\text{s}}$, und der Lehrbuch-Formel mit zufälligen Flugzeiten ist die
mittlere Flugzeit

$$T = \frac{m_\text{e}\,\mu_\text{e}}{e} = \frac{9{,}109\cdot10^{-31}\,\text{kg}\cdot4{,}1\cdot10^{-3}\,\frac{\text{m}^2}{\text{V}\,\text{s}}}{1{,}602\cdot10^{-19}\,\text{C}} \approx 2{,}3\cdot10^{-14}\,\text{s},$$

halb so lang wie im Sägezahn-Modell. In dieser Zeit legt das Elektron mit seiner ungeordneten Geschwindigkeit, in Kupfer rund
$1{,}57\cdot10^{6}\,\frac{\text{m}}{\text{s}}$, die freie Weglänge zurück:

$$\lambda = 1{,}57\cdot10^{6}\,\frac{\text{m}}{\text{s}}\cdot2{,}3\cdot10^{-14}\,\text{s} \approx 3{,}7\cdot10^{-8}\,\text{m} = 37\,\text{nm}.$$

Jedes Kupferatom gibt ein Leitungselektron ab, also ist die Atomdichte die Trägerdichte $8{,}49\cdot10^{28}\,\text{m}^{-3}$ aus dem Artikel über den Strom.
Der mittlere Atomabstand ist ihre Kubikwurzel im Kehrwert:

$$d_\text{A} = \big(8{,}49\cdot10^{28}\,\text{m}^{-3}\big)^{-1/3} \approx 2{,}3\cdot10^{-10}\,\text{m}, \qquad \frac{\lambda}{d_\text{A}} \approx 160.$$

Ein Elektron passiert also rund $160$ Atomabstände, bevor es gestreut wird.

**Gegenprobe zum Sägezahn.** Würde das Elektron nach jedem Stoß wirklich aus der Ruhe starten, käme es im Feld des $1$-A-Drahts mit der Beschleunigung
$2{,}1\cdot10^{9}\,\frac{\text{m}}{\text{s}^2}$ in der Laufzeit $4{,}7\cdot10^{-14}\,\text{s}$ nur

$$s = \frac{1}{2}\cdot2{,}1\cdot10^{9}\,\frac{\text{m}}{\text{s}^2}\cdot\big(4{,}7\cdot10^{-14}\,\text{s}\big)^2 \approx 2\cdot10^{-18}\,\text{m}$$

weit — weit weniger als der Durchmesser eines Atomkerns, der bei rund $10^{-14}\,\text{m}$ liegt. Von Atom zu Atom käme es so nie. Das Elektron fliegt
also mit seiner großen ungeordneten Geschwindigkeit; die Drift ist nur ein winziger Zusatz.

**Im Bild:** Auf dem echten Brett liegen zwischen zwei Nägeln rund $160$ Atomreihen, und die Kugel flitzt kreuz und quer. Voran kommt sie nur durch
einen winzigen gemeinsamen Hang.
::::

## Leitfähigkeit und spezifischer Widerstand

Aus der Driftgeschwindigkeit folgt die Stromdichte, und zwar ohne neue Annahme.

**Die Akteure:**

- die __Trägerdichte__ $n_\text{e}$, die Zahl der Leitungselektronen pro Volumen, in $\text{m}^{-3}$ — im Artikel über den Strom kurz $n$, für Kupfer
  rund $8{,}49\cdot10^{28}\,\text{m}^{-3}$;
- die Ladung eines Trägers, das Produkt $Z_\text{e}\,e$ aus der __Ladungszahl__ $Z_\text{e}$, beim Elektron $-1$, und der Elementarladung $e$;
- die __Stromdichte__ $\vec J$, ein Vektor in Ampere pro Quadratmeter.

Nach dem Artikel über den Strom ist die Stromdichte Raumladungsdichte mal Geschwindigkeit. Die Raumladungsdichte der Leitungselektronen ist
Trägerdichte mal Ladung pro Träger, also $-e\,n_\text{e}$; das Skript kürzt sie mit $q_\text{e}$ ab. Ein eigenes Zeichen bekommt sie hier nicht, weil
$\rho$ in diesem Artikel für den spezifischen Widerstand steht. Das Skript nennt $e_0$ (unser $e$) „Ladung des Elektrons"; gemeint ist die positive
Elementarladung. Das Vorzeichen kommt allein über $Z_\text{e}$ hinein — wäre $e_0$ selbst schon negativ, hätte $q_\text{e}$ das falsche Vorzeichen.

**Das Zusammenspiel:** *Welche Stromdichte entsteht, wenn alle Leitungselektronen mit $\vec v_\text{D}$ driften?*

:::formel Gesetz
$$\vec J = \sigma\,\vec E, \qquad \sigma = e\,n_\text{e}\,\mu_\text{e}.$$
:::

**So liest man das:** Eingabe ist das Feld, Ausgabe die Stromdichte; beide Vektoren zeigen in dieselbe Richtung. Die Konstante $\sigma$ ist die
__spezifische Leitfähigkeit__ des Materials, kurz __Leitfähigkeit__. Sie ist das Produkt aus Ladung pro Träger, Zahl der Träger ($n_\text{e}$) und
ihrer Beweglichkeit ($\mu_\text{e}$). Weil die Formel an jedem einzelnen Punkt des Leiters gilt, heißt sie das __Ohmsche Gesetz in Punktform__.

**Die Einheit.** Ampere pro Quadratmeter geteilt durch Volt pro Meter ergibt Ampere pro Volt und Meter. Ein Ampere pro Volt heißt __Siemens__, kurz
$\text{S}$; die Leitfähigkeit hat also die Einheit $\frac{\text{S}}{\text{m}}$. Das Skript rechnet in $\frac{\text{S}}{\text{cm}}$.

**Im Bild:** Wie viele Kugeln pro Sekunde einen Meter Ziellinie queren: Kugeln pro Fläche mal mittlere Geschwindigkeit. Ein Brett mit vielen Kugeln und
wenigen Nägeln leitet gut.

Die beiden Minuszeichen — negative Ladung, Drift gegen das Feld — heben sich auf. Darum zeigt $\vec J$ in Feldrichtung, obwohl die Elektronen gegen das
Feld wandern, genau wie es die technische Stromrichtung verlangt.

:::herleitung
**Stromdichte aus der Drift.** Die Stromdichte ist Raumladungsdichte mal Geschwindigkeit. Mit der Raumladungsdichte der Leitungselektronen und ihrer
Driftgeschwindigkeit:

$$\vec J = (-e\,n_\text{e})\,\vec v_\text{D} = (-e\,n_\text{e})\,(-\mu_\text{e}\,\vec E) = e\,n_\text{e}\,\mu_\text{e}\,\vec E.$$

Der Vorfaktor ist $\sigma$. In der Schreibweise des Skripts, mit $q_\text{e}$ für die Raumladungsdichte, ist das dasselbe:

$$\sigma = -\mu_\text{e}\,q_\text{e}, \qquad q_\text{e} = e\,Z_\text{e}\,n_\text{e} = -e\,n_\text{e}.$$

**Mehrere Trägersorten.** Tragen mehrere Sorten zum Strom bei, etwa Elektronen und Löcher in Halbleitern, addieren sich ihre Stromdichten. Jede Sorte
liefert dann ihren eigenen Beitrag Ladungsbetrag mal Dichte mal Beweglichkeit, und $\sigma$ ist die Summe.
:::

::::beispiel Kupfer gegen Silizium
**(a) Kupfer.** Die gemessene Leitfähigkeit aus der Tabelle unten, $5{,}6\cdot10^{7}\,\frac{\text{S}}{\text{m}}$, und die Trägerdichte liefern die
Beweglichkeit:

$$\mu_\text{e} = \frac{\sigma}{e\,n_\text{e}} = \frac{5{,}6\cdot10^{7}\,\frac{\text{S}}{\text{m}}}{1{,}602\cdot10^{-19}\,\text{C}\cdot8{,}49\cdot10^{28}\,\text{m}^{-3}} \approx 4{,}1\cdot10^{-3}\,\frac{\text{m}^2}{\text{V}\,\text{s}}.$$

Das ist der Wert, mit dem oben die Drift gerechnet wurde. Und das Feld im Draht von $1{,}5\,\text{mm}^2$ mit $1\,\text{A}$ folgt aus der Stromdichte:

$$E = \frac{J}{\sigma} = \frac{1\,\text{A}/(1{,}5\cdot10^{-6}\,\text{m}^2)}{5{,}6\cdot10^{7}\,\frac{\text{S}}{\text{m}}} \approx 0{,}0119\,\frac{\text{V}}{\text{m}} = 11{,}9\,\frac{\text{mV}}{\text{m}}.$$

**(b) Reines Silizium** bei Raumtemperatur hat nur rund $10^{16}$ freie Elektronen pro Kubikmeter, die dafür sehr beweglich sind, etwa
$0{,}14\,\frac{\text{m}^2}{\text{V}\,\text{s}}$. Ihr Beitrag zur Leitfähigkeit:

$$\sigma = 1{,}602\cdot10^{-19}\,\text{C}\cdot10^{16}\,\text{m}^{-3}\cdot0{,}14\,\frac{\text{m}^2}{\text{V}\,\text{s}} \approx 2{,}2\cdot10^{-4}\,\frac{\text{S}}{\text{m}}.$$

Die Löcher (Kapitel 10) bringen noch etwa ein Drittel dazu. Obwohl die Elektronen im Silizium $34$-mal so beweglich sind wie im Kupfer, liefern sie rund
$2{,}5\cdot10^{11}$-mal weniger Leitfähigkeit: Es gibt $8{,}5\cdot10^{12}$-mal weniger von ihnen.

**Im Bild:** Kupfer ist ein volles Brett mit vielen Nägeln, Silizium ein fast leeres, glattes Brett — die wenigen Kugeln rollen leicht, aber es sind kaum
welche da.
::::

Oft ist der Kehrwert praktischer, der __spezifische Widerstand__:

$$\rho = \frac{1}{\sigma}, \qquad [\rho] = \frac{\text{V}\,\text{m}}{\text{A}} = \Omega\,\text{m}.$$

Ein Volt pro Ampere heißt __Ohm__, $\Omega$; es ist die Einheit des Widerstands im nächsten Abschnitt. Gute Leiter haben ein kleines $\rho$, schlechte ein
großes. Das Skript gibt im Kasten die Einheit $\Omega\,\text{cm}^{-1}$ an; richtig ist $\Omega\,\text{cm}$, wie im Kopf der Tabelle dort. In der Praxis
rechnet man meist in $\Omega\,\frac{\text{mm}^2}{\text{m}}$, weil Drähte in Quadratmillimetern und Metern angegeben werden.

**Im Bild:** Der spezifische Widerstand sagt, wie dicht die Nägel stehen — unabhängig davon, wie groß das Brett ist.

:::herleitung
**Die Einheit von $\rho$.** Der Kehrwert von Siemens pro Meter ist Meter pro Siemens, und ein Siemens ist ein Ampere pro Volt:

$$\frac{1}{\text{S}/\text{m}} = \frac{\text{m}}{\text{S}} = \frac{\text{V}\,\text{m}}{\text{A}} = \Omega\,\text{m}.$$

Ein $\Omega\,\text{cm}^{-1}$ wäre dagegen Ohm geteilt durch eine Länge, die Einheit eines Widerstands pro Länge — das passt nicht zum Kehrwert einer
Leitfähigkeit.

**Die Umrechnungen.** Mit $1\,\text{mm}^2$ gleich $10^{-6}\,\text{m}^2$ und $1\,\text{cm}$ gleich $10^{-2}\,\text{m}$:

$$1\,\Omega\,\frac{\text{mm}^2}{\text{m}} = 10^{-6}\,\Omega\,\text{m}, \qquad 10^{-6}\,\Omega\,\text{cm} = 10^{-8}\,\Omega\,\text{m} = 0{,}01\,\Omega\,\frac{\text{mm}^2}{\text{m}}.$$

Für die Leitfähigkeit entsprechend:

$$10^{4}\,\frac{\text{S}}{\text{cm}} = 10^{6}\,\frac{\text{S}}{\text{m}} = 1\,\frac{\text{MS}}{\text{m}} = 1\,\frac{\text{m}}{\Omega\,\text{mm}^2}.$$
:::

Die Tabelle des Skripts, umgerechnet; eine Spalte in $\frac{\text{MS}}{\text{m}}$ entspricht der Skript-Spalte in $10^4\,\frac{\text{S}}{\text{cm}}$:

| Leiter | $\sigma$ in $\frac{\text{MS}}{\text{m}}$ | $\rho$ in $\Omega\,\frac{\text{mm}^2}{\text{m}}$ |
|---|---|---|
| Silber | $62{,}5$ | $0{,}016$ |
| Kupfer | $56$ | $0{,}0179$ |
| Gold | $44$ | $0{,}023$ |
| Aluminium | $35$ | $0{,}029$ |
| Wolfram | $18$ | $0{,}055$ |
| Messing (Cu, Zn) | $11$ … $14$ | $0{,}07$ … $0{,}09$ |
| Eisen | $7$ … $10$ | $0{,}10$ … $0{,}15$ |
| Platin | $7$ … $9$ | $0{,}11$ … $0{,}14$ |
| Konstantan (Cu, Ni) | $2{,}0$ | $0{,}50$ |
| Kohle | $0{,}01$ … $0{,}02$ | $50$ … $100$ |

Die Spannen bei Messing, Eisen und Platin hängen von Zusammensetzung und Reinheit ab. Auffällig ist Konstantan: eine Legierung aus Kupfer und Nickel,
die fast dreißigmal schlechter leitet als reines Kupfer — warum, zeigt der Abschnitt über die Temperatur.

## Vom Leiterstück zum Bauteil: das Ohmsche Gesetz

Bisher war alles örtlich: Feld und Stromdichte an einem Punkt. Gemessen werden aber Spannung und Strom an den Enden eines Bauteils. Das Skript betrachtet
dafür ein Leiterstück wie in seinem Bild: einen Zylinder mit Plus links und Minus rechts, durch den der Strom von links nach rechts fließt.

**Die Akteure:**

- ein __homogener Leiter__ — überall aus demselben Material, also mit überall gleichem $\sigma$ — der __Länge__ $l$ in Metern und mit überall gleichem
  __Querschnitt__ $A$, einer Fläche in Quadratmetern;
- die __Spannung__ $U$ zwischen den beiden Endflächen, in Volt;
- der __Strom__ $I$ durch den Leiter, in Ampere.

Das Skript schreibt die Länge groß, $L$; hier steht nach DIN das kleine $l$, weil $L$ später die Induktivität bezeichnet.

**Das Zusammenspiel:** *Wie wird aus der örtlichen Regel $\vec J=\sigma\vec E$ eine Regel für das ganze Leiterstück?*

:::formel Gesetz
$$U = R\cdot I, \qquad R = \frac{l}{\sigma\,A} = \rho\,\frac{l}{A}.$$
:::

**So liest man das:** Eingabe ist der Strom, Ausgabe die Spannung, beides Zahlen mit Einheit. Der __Widerstand__ $R$ ist der feste Faktor dazwischen,
in Volt pro Ampere, also in Ohm. Er hängt nur vom Material ($\rho$) und von der Form ($l$, $A$) ab, nicht von Spannung oder Strom — und genau darum ist
die Spannung dem Strom proportional. Doppelt so lang heißt doppelter Widerstand, doppelter Querschnitt heißt halber. Das Ohmsche Gesetz in Punktform ist der
Grund, $U=R\,I$ seine Folge für ein ganzes Bauteil.

**Im Bild:** Der Höhenunterschied $U$ verteilt sich gleichmäßig auf die Brettlänge $l$, die Neigung ist Höhe durch Länge — das Feld. Die Breite des
Bretts ist der Querschnitt $A$, die Dichte der Nägel der spezifische Widerstand $\rho$.

:::herleitung
**Schritt 1: überall derselbe Strom.** Im stationären Zustand fließt nach dem Artikel über den Strom durch jeden Querschnitt eines unverzweigten Leiters
derselbe Strom $I$ (Kontinuität).

**Schritt 2: überall dieselbe Stromdichte und dasselbe Feld.** Der Querschnitt ist überall gleich, und der Strom verteilt sich gleichmäßig darüber
(Voraussetzungen unten). Dann ist die Stromdichte überall dieselbe, und weil $\sigma$ überall gleich ist, auch das Feld:

$$J = \frac{I}{A}, \qquad E = \frac{J}{\sigma} = \frac{I}{\sigma\,A}.$$

Es zeigt längs der Achse von der Plus- zur Minusseite.

**Schritt 3: Spannung aus dem Feld.** Nach dem Artikel über Arbeit, Potenzial und Spannung ist die Spannung zwischen zwei Punkten das Wegintegral des
Felds. Längs der Achse zeigt das Feld überall in Wegrichtung und ist konstant, das Integral ist Feld mal Länge:

$$U = \int_0^l \vec E\cdot d\vec s = E\,l.$$

Das ist das $U=E\cdot L$, auf das das Skript zurückgreift.

**Schritt 4: zusammensetzen.** Nach $I$ aufgelöst ergibt sich zuerst die Form des Skripts, nach $U$ aufgelöst das Ohmsche Gesetz:

$$I = J\,A = \sigma\,E\,A = \frac{\sigma\,A}{l}\,U, \qquad U = \frac{l}{\sigma\,A}\,I.$$

Mit $\rho$ als Kehrwert von $\sigma$ folgt die zweite Form von $R$.

**Warum der Strom sich gleichmäßig verteilt.** Ein gleichmäßiges Feld längs der Achse erfüllt alles, was ein stationäres Strömungsfeld erfüllen muss:
Es ist quellen- und wirbelfrei, es läuft an den Seitenwänden entlang, ohne Strom hinauszutragen, und es steht senkrecht auf flächigen Kontakten an den Enden. Dass
es dann auch die einzige mögliche Verteilung ist, zeigt die Feldtheorie in einem späteren Semester (Eindeutigkeitssatz).

**Im Bild:** Auf einem gleichmäßigen Brett ist die Neigung überall gleich, Höhenunterschied durch Länge, und jede Bahn trägt gleich viel.
:::

**Wann das so gilt.** Die Herleitung braucht vier Voraussetzungen:

- Das Material ist __homogen__, $\sigma$ überall gleich.
- Der Querschnitt ist überall gleich.
- Der Strom tritt gleichmäßig über die ganzen Endflächen ein und aus, oder der Leiter ist viel länger als dick. Das meint die Bedingung des Skripts
  $l\gg\sqrt A$ (dort mit $L$): Die Wurzel aus dem Querschnitt ist ungefähr die Dicke. Wird der Strom an einem Punkt eingespeist, verteilt er sich erst auf einem Stück
  von etwa einer Dicke Länge über den Querschnitt; bei einem langen Draht fällt dieses Stück nicht ins Gewicht.
- Strom und Temperatur sind konstant. Bei schnell wechselnden Strömen drängt sich der Strom an die Oberfläche (Skin-Effekt), und bei Erwärmung ändert
  sich $\rho$ (unten).

**Im Bild:** Lässt man die Kugeln nur an einer Stelle oben einfallen, brauchen sie ein Stück, bis sie sich über die ganze Breite verteilt haben. Auf
einem langen Brett ist das egal.

:::grafik
Szene: get1/stroeme-und-spannungen/02-leiterstueck · Vorlage: leiter-zylinder
Ein grüner Zylinder der Länge $l$ mit markiertem Querschnitt $A$ (rot gestrichelte Ellipse), links „+", rechts „−"; außen der Strompfeil $I$ hinein und
hinaus, darüber ein Spannungspfeil $U$ von Plus nach Minus. Im Inneren gleich lange, parallele Feldpfeile $\vec E$ und Stromdichtepfeile $\vec J$; ein
Potenzialbalken längs der Achse fällt linear von $U$ auf $0$. Regler für $l$, $A$ und $\sigma$: Der Anzeigewert $R=\rho\,l/A$ und der Strom $I=U/R$
ändern sich mit. Umschalter „punktförmiger Anschluss": Der Strom tritt in der Mitte der Endfläche ein; nahe den Enden fächern die Stromlinien auf und
sind erst nach etwa einer Dicke gleichmäßig verteilt. Kernaussage: Im homogenen Leiter ist das Feld überall Spannung durch Länge, und daraus folgt
$U=R\,I$. (Rot = Querschnitt und Widerstand, blau = Feld und Strömung, orange = Potenzialabfall, grau = Zylinder, gestrichelt = Querschnitt.)
:::

::::beispiel Die Kabeltrommel
**(a) Die Trommel.** Eine Kabeltrommel hat $25\,\text{m}$ Leitung mit Adern aus Kupfer von je $1{,}5\,\text{mm}^2$. Der Strom fließt durch eine Ader hin
und durch die andere zurück; die stromdurchflossene Länge ist also $50\,\text{m}$. Mit dem spezifischen Widerstand von Kupfer aus der Tabelle:

$$R = \rho\,\frac{l}{A} = 0{,}0179\,\Omega\,\frac{\text{mm}^2}{\text{m}}\cdot\frac{50\,\text{m}}{1{,}5\,\text{mm}^2} \approx 0{,}60\,\Omega.$$

Zieht ein Heizlüfter $10\,\text{A}$, fallen auf der Leitung

$$U = R\,I \approx 0{,}60\,\Omega\cdot10\,\text{A} = 6{,}0\,\text{V},$$

ab, gut $2{,}5\,\%$ der Netzspannung von $230\,\text{V}$; bei $16\,\text{A}$, dem Nennstrom einer üblichen Haushaltssicherung, wären es rund
$9{,}5\,\text{V}$. Das Feld in den Adern ist bei $10\,\text{A}$ Spannung durch Länge:

$$E = \frac{U}{l} = \frac{6{,}0\,\text{V}}{50\,\text{m}} = 0{,}12\,\frac{\text{V}}{\text{m}}.$$

Zehnmal so viel wie im Draht mit $1\,\text{A}$ aus dem Abschnitt über die Drift ($11{,}9\,\text{mV}/\text{m}$), bei zehnfachem Strom — wie es die
Proportionalität verlangt.

**(b) Konstantan.** Ein Widerstand von $1\,\Omega$ aus Konstantandraht mit $0{,}5\,\text{mm}^2$ Querschnitt braucht die Länge

$$l = \frac{R\,A}{\rho} = \frac{1\,\Omega\cdot0{,}5\,\text{mm}^2}{0{,}50\,\Omega\,\text{mm}^2/\text{m}} = 1{,}0\,\text{m}.$$

Aus Kupfer wären es bei gleichem Querschnitt $28\,\text{m}$.

**Im Bild:** Die Trommel ist ein langes, schmales Brett mit wenigen Nägeln: Der Widerstand bleibt klein, aber nicht null. Konstantan ist dicht genagelt,
ein kurzes Stück bremst genauso stark.
::::

## Leitwert, Schaltsymbol und Kennlinie

Im Schaltplan steht ein ohmscher Widerstand als schmales Rechteck mit zwei Anschlüssen, beschriftet mit $R$ oder $G$ (Bild 5.5 des Skripts); die beiden
Symbole sind gleich, und die Beschriftungen sind gleichwertig. Das Wort „Widerstand" meint dabei zweierlei: das Bauteil und seine Größe $R$. Manchmal ist
die umgekehrte Sicht praktischer, der __Leitwert__:

:::formel Definition
$$G := \frac{1}{R} = \frac{I}{U}, \qquad [G] = \frac{1}{\Omega} = \frac{\text{A}}{\text{V}} = \text{S}.$$
:::

**So liest man das:** Der Leitwert beschreibt dasselbe Bauteil von der anderen Seite — wie gut statt wie schlecht es leitet. Seine Einheit ist das
Siemens, der Kehrwert des Ohm. Mit ihm schreibt sich das Ohmsche Gesetz nach dem Strom aufgelöst, und der Leitwert eines Leiterstücks folgt aus der
Leitfähigkeit:

$$I = G\cdot U, \qquad G = \frac{\sigma\,A}{l}.$$

Leitwert und Leitfähigkeit stehen zueinander wie Widerstand und spezifischer Widerstand: das eine gehört zum Bauteil, das andere zum Material. Die
Einheiten tragen die Namen von Georg Simon Ohm (1789–1854) und Werner von Siemens (1816–1892).

**Die Kennlinie.** Trägt man zusammengehörige Werte von Strom und Spannung eines Bauteils in ein Diagramm ein, entsteht seine __Kennlinie__. Beim
ohmschen Widerstand ist sie eine Gerade durch den Ursprung. Das Skript zeigt sie zweimal: Spannung über Strom mit der Steigung $R$ (Bild 5.6), Strom über
Spannung mit der Steigung $G$ (Bild 5.7):

$$R = \frac{\Delta U}{\Delta I}, \qquad G = \frac{\Delta I}{\Delta U}.$$

**Im Bild:** Das Diagramm neben dem Nagelbrett — Kugeln pro Sekunde über dem Höhenunterschied — ist die Kennlinie. Ein Brett mit wenigen Nägeln gibt
eine steile Gerade, also einen großen Leitwert, eines mit vielen eine flache.

:::herleitung
**Steigung und Verhältnis.** Zwei Punkte auf der Kennlinie, $(I_1, U_1)$ und $(I_2, U_2)$, erfüllen beide das Ohmsche Gesetz. Die Differenz der beiden
Gleichungen:

$$U_2 - U_1 = R\,I_2 - R\,I_1 = R\,(I_2 - I_1), \qquad \frac{\Delta U}{\Delta I} = R.$$

Die Steigung zwischen zwei beliebigen Punkten ist also dasselbe wie das Verhältnis $U/I$ in einem einzelnen Punkt. Für $I$ über $U$ gilt dasselbe mit
dem Kehrwert. Bei gekrümmten Kennlinien (unten bei den Zweipolen) fallen Steigung und Verhältnis auseinander.

**Leitwert eines Leiterstücks.** Der Kehrwert von $R=\frac{l}{\sigma A}$ ist $\frac{\sigma A}{l}$.
:::

:::grafik
Szene: get1/stroeme-und-spannungen/02-kennlinie · Vorlage: kennlinie-gerade
Zwei Diagramme nebeneinander: links $U$ über $I$, rechts $I$ über $U$, jeweils eine Ursprungsgerade für einen Widerstand. Zwei ziehbare Punkte auf der
Geraden spannen ein Steigungsdreieck mit $\Delta I$ und $\Delta U$ auf; links steht $R=\Delta U/\Delta I$, rechts $G=\Delta I/\Delta U$. Ein Regler für
$R$ dreht die linke Gerade steiler und die rechte flacher. Daneben das Schaltsymbol, ein Rechteck mit der Beschriftung $R$ bzw. $G$. Kernaussage: Beim
ohmschen Widerstand ist die Kennlinie eine Ursprungsgerade; ihre Steigung ist $R$ oder $G$, je nachdem, was man aufträgt. (Rot = Kennlinie,
orange = Steigungsdreieck, grau = Achsen und Symbol.)
:::

::::beispiel Ein Widerstand von 220 Ohm
Ein Widerstand mit $220\,\Omega$ hat den Leitwert

$$G = \frac{1}{220\,\Omega} \approx 4{,}55\cdot10^{-3}\,\text{S} = 4{,}55\,\text{mS}.$$

Einige Punkte seiner Kennlinie nach $I=G\,U$:

| $U$ | $1\,\text{V}$ | $2\,\text{V}$ | $5\,\text{V}$ |
|---|---|---|---|
| $I$ | $4{,}55\,\text{mA}$ | $9{,}09\,\text{mA}$ | $22{,}7\,\text{mA}$ |

Die Steigung zwischen den Punkten bei $2\,\text{V}$ und $5\,\text{V}$ gibt den Widerstand zurück:

$$\frac{\Delta U}{\Delta I} = \frac{5\,\text{V} - 2\,\text{V}}{22{,}73\,\text{mA} - 9{,}09\,\text{mA}} = \frac{3\,\text{V}}{13{,}64\,\text{mA}} \approx 220\,\Omega.$$

**Im Bild:** Fünfmal so viel Höhenunterschied, fünfmal so viele Kugeln pro Sekunde — die Punkte liegen auf einer Geraden.
::::

## Wohin die Energie geht

Die Elektronen verlassen den Widerstand nicht schneller, als sie hineingekommen sind; ihre Driftgeschwindigkeit ist überall dieselbe. Trotzdem hat das
Feld an ihnen Arbeit verrichtet: Nach dem Artikel über die Spannung verrichtet es an einer Ladung $Q$, die in technischer Stromrichtung die Spannung $U$
durchläuft, die Arbeit $Q\,U$. Für Elektronen in Gegenrichtung ist es dasselbe, weil sich beide Vorzeichen umkehren.

Diese Energie bleibt nicht bei den Elektronen. Sie geht bei den Stößen an das Gitter über und lässt die Atomrümpfe stärker schwingen — der Widerstand
wird warm. Das Skript: Die Energie der Ladungsträger wird durch Streuung im Festkörper in Wärme umgewandelt. Man nennt sie __Stromwärme__ oder
__Joulesche Wärme__. Pro Zeit ist das die __Leistung__:

:::formel
$$P = U\cdot I = R\,I^2 = \frac{U^2}{R}, \qquad [P] = \text{V}\,\text{A} = \text{W}.$$
:::

**So liest man das:** Die Leistung ist Energie pro Zeit, in Watt; dass ein Watt ein Volt mal Ampere ist, steht schon im Artikel über Größen und
Einheiten. Sie wächst mit dem Quadrat des Stroms: doppelter Strom, vierfache Wärme. Mit welchem Vorzeichen man eine Leistung zählt, klärt der nächste
Artikel über Zählpfeile; ausführlich kommt die Energieumsetzung im Widerstand in Kapitel 7.

**Im Bild:** Die Höhenenergie, die die Kugeln beim Hinabrollen verlieren, steckt am Ende in den zitternden Nägeln. Pro Sekunde ist das Höhenunterschied
mal Kugeln pro Sekunde.

:::herleitung
**Leistung.** In der kurzen Zeit $dt$ tritt die Ladung $I\,dt$ durch den Widerstand, und das Feld verrichtet an ihr die Arbeit $U\,I\,dt$. Arbeit pro
Zeit:

$$P = \frac{dW}{dt} = \frac{U\,I\,dt}{dt} = U\,I.$$

**Die beiden anderen Formen.** Setzt man das Ohmsche Gesetz für $U$ ein, folgt $R\,I^2$; setzt man es nach $I$ aufgelöst ein, folgt $U^2/R$.

**Örtlich.** Mit Schritt 2 und 3 der Herleitung des Ohmschen Gesetzes ist $U$ gleich $E\,l$ und $I$ gleich $J\,A$; das Produkt $l\,A$ ist das Volumen
$V$ des Leiters:

$$P = E\,l\cdot J\,A = J\,E\,V = \sigma\,E^2\,V.$$

Jedes Volumenstück erzeugt die Wärme $J\,E$ pro Volumen und Zeit — dort, wo Strom und Feld groß sind, wird es am wärmsten.
:::

::::beispiel Warme Leitungen, kleine Widerstände
**(a) Die Kabeltrommel** mit $0{,}595\,\Omega$ setzt bei $10\,\text{A}$ und bei $16\,\text{A}$ um:

$$P = R\,I^2 = 0{,}595\,\Omega\cdot(10\,\text{A})^2 \approx 60\,\text{W}, \qquad P = 0{,}595\,\Omega\cdot(16\,\text{A})^2 \approx 152\,\text{W}.$$

Abgerollt verteilt sich diese Wärme auf $25\,\text{m}$ Kabel. Aufgewickelt kann sie kaum entweichen, die Trommel heizt sich auf — deshalb ist auf
Kabeltrommeln eine viel kleinere zulässige Last für den aufgerollten Zustand angegeben.

**(b) Ein Schichtwiderstand** mit $1\,\text{k}\Omega$ verträgt $0{,}25\,\text{W}$. Nach den beiden letzten Formen der Leistung sind das höchstens

$$I = \sqrt{\frac{P}{R}} = \sqrt{\frac{0{,}25\,\text{W}}{1000\,\Omega}} \approx 15{,}8\,\text{mA}, \qquad U = \sqrt{P\,R} \approx 15{,}8\,\text{V}.$$

An $24\,\text{V}$ wäre er mehr als doppelt überlastet:

$$P = \frac{(24\,\text{V})^2}{1000\,\Omega} \approx 0{,}58\,\text{W}.$$

**Im Bild:** Doppelter Strom durch dasselbe Brett heißt doppelt so viele Kugeln, die je doppelt so viel Höhe verlieren — vierfache Wärme. Bei
$16$ statt $10\,\text{A}$, dem $1{,}6$-fachen Strom, wird es gut zweieinhalbmal so warm.
::::

## Bauformen

Wie ein Widerstand gebaut ist, folgt aus zwei Forderungen: Er soll den gewünschten Wert haben, und er muss seine Stromwärme loswerden. Das Skript nennt
drei typische Bauformen (Bild 5.8 und 5.9):

- __Schichtwiderstand__ (Metall- oder Kohleschicht): eine dünne Widerstandsschicht auf einem Keramikröhrchen. Eine eingeschliffene Wendel macht aus der
  Schicht einen langen, schmalen Streifen, der um das Röhrchen läuft — nach $R=\rho\,l/A$ ein großer Widerstand auf kleinem Raum, weil $l$ groß und $A$
  klein wird. Relativ geringe Leistung, etwa $0{,}1$ bis $2\,\text{W}$; der Wert steht im Farbcode auf dem Bauteil. Das ist die „typische" Bauform.
- __Drahtwiderstand__: Widerstandsdraht, etwa aus Konstantan, auf einen Keramikkörper gewickelt, oft in einem Metallgehäuse mit Kühlfläche (das
  goldfarbene Bauteil in Bild 5.8). Ein dicker Draht hat einen kleinen Widerstand, und die große Oberfläche führt viel Wärme ab: hohe Leistung, hohe
  Temperaturbelastbarkeit. Weil der Draht gewickelt ist, bildet er eine kleine Spule, die schnelle Wechselströme behindert (Thema eines späteren
  Moduls).
- __SMD-Widerstand__ (surface mounted device, oberflächenmontiertes Bauteil): ein winziger Quader, der direkt auf die Leiterplatte gelötet wird. Die
  geringen Abmessungen erlauben eine hohe Packungsdichte, ohne Anschlussdrähte gibt es kaum störende Spulenwirkung — gut für die Hochfrequenztechnik.
  Die kleine Oberfläche führt aber wenig Wärme ab: geringe Leistung.

**Im Bild:** Die Wendel des Schichtwiderstands macht aus einem kurzen, breiten Brett ein langes, schmales, das sich um das Röhrchen windet.

:::grafik
Szene: get1/stroeme-und-spannungen/02-schichtwiderstand · Vorlage: wendel-abrollen
Ein Keramikröhrchen mit einer dünnen Metallschicht, an beiden Enden Kappen mit Anschlussdrähten. Eine Schleifscheibe fräst eine Wendel in die Schicht.
Danach wird die Schicht wie ein Etikett abgerollt: Aus dem kurzen, breiten Rechteck ohne Wendel (Länge gleich Röhrchenlänge, Breite gleich Umfang) wird
ein langer, schmaler Streifen. Ein Zähler zeigt jeweils $R=\rho\,l/A$ mit dem Querschnitt Breite mal Schichtdicke; ein Regler für die Zahl der Windungen
lässt $R$ etwa mit deren Quadrat wachsen. Kernaussage: Die Wendel vervielfacht den Widerstand, weil sie die Länge vergrößert und zugleich die Breite
verkleinert. (Rot = Widerstandsstreifen, orange = Wendel und Schleifscheibe, grau = Keramik und Kappen.)
:::

::::beispiel Was die Wendel bewirkt
Ein Röhrchen von $6\,\text{mm}$ Länge und $2\,\text{mm}$ Durchmesser, also rund $6{,}28\,\text{mm}$ Umfang, trägt eine Metallschicht von $50\,\text{nm}$
Dicke mit dem spezifischen Widerstand $1{,}1\cdot10^{-6}\,\Omega\,\text{m}$ (eine Nickel-Chrom-Legierung). Ohne Wendel fließt der Strom längs über die
ganze Breite des Umfangs:

$$R = \rho\,\frac{l}{b\,h} = 1{,}1\cdot10^{-6}\,\Omega\,\text{m}\cdot\frac{6\cdot10^{-3}\,\text{m}}{6{,}28\cdot10^{-3}\,\text{m}\cdot5\cdot10^{-8}\,\text{m}} \approx 21\,\Omega.$$

Dabei ist $b$ die Breite und $h$ die Dicke der Schicht, ihr Produkt der Querschnitt. Eine Wendel mit $0{,}2\,\text{mm}$ Steigung legt $30$ Windungen um
das Röhrchen. Daraus wird ein Streifen von $0{,}2\,\text{mm}$ Breite und der Länge

$$l = 30\cdot6{,}28\,\text{mm} \approx 188\,\text{mm},$$

$$R = 1{,}1\cdot10^{-6}\,\Omega\,\text{m}\cdot\frac{0{,}188\,\text{m}}{0{,}2\cdot10^{-3}\,\text{m}\cdot5\cdot10^{-8}\,\text{m}} \approx 21\,\text{k}\Omega.$$

Rund tausendmal so viel: Die Länge wächst um den Faktor $31$, die Breite schrumpft um denselben Faktor, und beides geht in $R$ ein. Die Breite der
geschliffenen Rille selbst ist dabei vernachlässigt.

**Im Bild:** Dasselbe Material, dieselbe Nageldichte — nur ist das Brett jetzt $31$-mal so lang und $31$-mal so schmal.
::::

## Normwerte: die E-Reihen und der Farbcode

Kein Widerstand hat genau den aufgedruckten Wert. Die Fertigung streut, und der Hersteller garantiert nur eine __Toleranz__, eine erlaubte relative
Abweichung, etwa $\pm5\,\%$. Weil die Toleranz relativ ist, wächst die absolute Unsicherheit mit dem Wert: $\pm5\,\%$ sind bei $100\,\Omega$ fünf Ohm,
bei $10\,\text{k}\Omega$ fünfhundert. Werte im festen Abstand anzubieten, etwa $100$, $110$, $120\,\Omega$ und so weiter bis in den Megaohmbereich,
wäre deshalb sinnlos. Sinnvoll ist ein festes **Verhältnis** zwischen Nachbarn.

So entstehen die __E-Reihen__ nach DIN IEC 60063, sieben Reihen E3, E6, E12, E24, E48, E96 und E192. Die Zahl $N$ hinter dem E gibt an, wie viele
Werte auf eine __Dekade__ kommen, also auf jeden Faktor $10$. Innerhalb einer Dekade lauten die Werte:

:::formel Definition
$$w_j = \sqrt[N]{10^{\,j}} = \big(\sqrt[N]{10}\big)^{j}, \qquad j \in \{0, 1, \dots, N-1\}.$$
:::

**So liest man das:** Eingabe ist die Nummer $j$ des Werts in der Dekade, Ausgabe eine Zahl zwischen $1$ und $10$, gerundet auf zwei Stellen (E3 bis
E24) oder drei Stellen (E48 bis E192). Mit Zehnerpotenzen multipliziert ergibt sie alle Normwerte, etwa $4{,}7\,\Omega$, $47\,\Omega$, $470\,\Omega$ und
$4{,}7\,\text{k}\Omega$. Benachbarte Werte stehen im festen Verhältnis $\sqrt[N]{10}$, dem __Stufenfaktor__ $q$; auf einer logarithmischen Skala liegen sie
gleichmäßig verteilt. Das Skript nennt die Werte $k$, die Nummer $m$ und die Anzahl $n$; hier heißen sie $w_j$, $j$ und $N$, weil $m_\text{e}$ und
$n_\text{e}$ schon vergeben sind.

**Im Bild:** Nagelbretter gäbe es dann nicht in jeder Länge, sondern in Stufen, und jede Stufe wäre um denselben Faktor länger als die vorige.

:::herleitung
**Festes Verhältnis.** Ist $q$ der Faktor zwischen Nachbarn und beginnt die Dekade bei $1$, ist der Wert mit der Nummer $j$ gleich $q^j$. Nach $N$
Schritten soll genau eine Dekade durchlaufen sein:

$$q^N = 10, \qquad q = \sqrt[N]{10}, \qquad w_j = q^j = \big(\sqrt[N]{10}\big)^{j} = \sqrt[N]{10^{\,j}}.$$

**Lückenlose Abdeckung.** Ein Wert $w$ mit der relativen Toleranz $\delta$ deckt das Band von $(1-\delta)\,w$ bis $(1+\delta)\,w$ ab. Zwei Nachbarn berühren
oder überlappen sich, wenn die obere Grenze des kleineren mindestens die untere des größeren erreicht:

$$(1+\delta)\,w_j \ge (1-\delta)\,q\,w_j \quad\Longleftrightarrow\quad \frac{1+\delta}{1-\delta} \ge q.$$

Der Faktor $w_j$ kürzt sich heraus: Die Bedingung ist für alle Nachbarn dieselbe — genau das leistet das feste Verhältnis.
:::

Die Reihen mit ihren üblichen Toleranzen, ihrem Stufenfaktor und dem Wert, den der Stufenfaktor höchstens haben darf, damit sich die Bänder lückenlos
überlappen:

| Reihe | Toleranz | Stufenfaktor $q$ | Grenze $\frac{1+\delta}{1-\delta}$ |
|---|---|---|---|
| E3 | über $\pm20\,\%$ | $2{,}15$ | — |
| E6 | $\pm20\,\%$ | $1{,}47$ | $1{,}50$ |
| E12 | $\pm10\,\%$ | $1{,}21$ | $1{,}22$ |
| E24 | $\pm5\,\%$ | $1{,}10$ | $1{,}11$ |
| E48 | $\pm2\,\%$ | $1{,}049$ | $1{,}041$ |
| E96 | $\pm1\,\%$ | $1{,}024$ | $1{,}020$ |
| E192 | $\pm0{,}5\,\%$ und feiner | $1{,}012$ | $1{,}010$ |

Bis E24 überlappen die Toleranzbänder: Jeder Widerstand, den die Fertigung liefert, fällt in das Band eines Normwerts und lässt sich danach einsortieren.
Ab E48 bleiben schmale Lücken; Präzisionswiderstände werden gezielt auf ihren Wert abgeglichen, statt aus einer Streuung aussortiert zu werden.

:::grafik
Szene: get1/stroeme-und-spannungen/02-e-reihe · Vorlage: log-skala-baender
Eine logarithmische Achse von $1$ bis $10$. Darauf die zwölf E12-Werte als Punkte, jeder mit seinem Toleranzband von $\pm10\,\%$ als Balken; die Balken
berühren oder überlappen sich lückenlos. Ein Umschalter wechselt auf E24 ($\pm5\,\%$) und auf E96 ($\pm1\,\%$): Bei E96 bleiben zwischen den Balken schmale
Lücken, die beim Hineinzoomen sichtbar werden. Ein Regler für $j$ markiert $w_j=10^{j/N}$ und den Stufenfaktor als gleich lange Schritte auf der
logarithmischen Achse. Kernaussage: Ein festes Verhältnis zwischen Nachbarn passt zu einer festen relativen Toleranz. (Rot = Normwerte, blau =
Toleranzbänder, orange = Lücken, grau = Achse.)
:::

::::beispiel Die E12-Reihe nachgerechnet
Für E12 ist der Stufenfaktor

$$q = \sqrt[12]{10} \approx 1{,}2115.$$

Die exakten Werte $10^{j/12}$, auf zwei Stellen gerundet, und die genormten Werte:

| $j$ | exakt | gerundet | Normwert |
|---|---|---|---|
| $0$ | $1{,}000$ | $1{,}0$ | $1{,}0$ |
| $1$ | $1{,}212$ | $1{,}2$ | $1{,}2$ |
| $2$ | $1{,}468$ | $1{,}5$ | $1{,}5$ |
| $3$ | $1{,}778$ | $1{,}8$ | $1{,}8$ |
| $4$ | $2{,}154$ | $2{,}2$ | $2{,}2$ |
| $5$ | $2{,}610$ | $2{,}6$ | $2{,}7$ |
| $6$ | $3{,}162$ | $3{,}2$ | $3{,}3$ |
| $7$ | $3{,}831$ | $3{,}8$ | $3{,}9$ |
| $8$ | $4{,}642$ | $4{,}6$ | $4{,}7$ |
| $9$ | $5{,}623$ | $5{,}6$ | $5{,}6$ |
| $10$ | $6{,}813$ | $6{,}8$ | $6{,}8$ |
| $11$ | $8{,}254$ | $8{,}3$ | $8{,}2$ |

Fünf Normwerte weichen in der letzten Stelle um eins ab: Die Reihen sind älter als ihre Norm und wurden mit den eingebürgerten Werten übernommen. In E48 und E96 stimmen
dagegen alle Normwerte mit der auf drei Stellen gerundeten Formel überein. Der letzte E48-Wert etwa ist

$$10^{47/48} \approx 9{,}53;$$

in Bild 5.10 des Skripts steht dort versehentlich $963$ statt $953$.

**Abdeckung.** Die Grenze für E12 mit $\pm10\,\%$ ist $\frac{1{,}1}{0{,}9}$, rund $1{,}222$, also größer als der Stufenfaktor $1{,}2115$. Zum Beispiel
überlappen $1{,}0\,\text{k}\Omega$ und $1{,}2\,\text{k}\Omega$:

$$1{,}0\,\text{k}\Omega\pm10\,\%:\ 0{,}90\ \text{bis}\ 1{,}10\,\text{k}\Omega, \qquad 1{,}2\,\text{k}\Omega\pm10\,\%:\ 1{,}08\ \text{bis}\ 1{,}32\,\text{k}\Omega.$$

**Im Bild:** Zwölf Stufen pro Dekade, jede gut $21\,\%$ länger als die vorige — und kein gefertigtes Brett fällt durch die Lücken.
::::

**Der Farbcode.** Bedrahtete Widerstände tragen ihren Wert als Farbringe (IEC 60062). Beim verbreiteten Code mit vier Ringen stehen die ersten beiden
Ringe für zwei Ziffern $z_1$ und $z_2$, der dritte für den Multiplikator $10^x$ und der vierte für die Toleranz:

$$R = (10\,z_1 + z_2)\cdot10^{x}\,\Omega.$$

| Farbe | Ziffer | Multiplikator | Toleranz |
|---|---|---|---|
| schwarz | $0$ | $10^0$ | — |
| braun | $1$ | $10^1$ | $\pm1\,\%$ |
| rot | $2$ | $10^2$ | $\pm2\,\%$ |
| orange | $3$ | $10^3$ | — |
| gelb | $4$ | $10^4$ | — |
| grün | $5$ | $10^5$ | $\pm0{,}5\,\%$ |
| blau | $6$ | $10^6$ | $\pm0{,}25\,\%$ |
| violett | $7$ | $10^7$ | $\pm0{,}1\,\%$ |
| grau | $8$ | $10^8$ | $\pm0{,}05\,\%$ |
| weiß | $9$ | $10^9$ | — |
| gold | — | $10^{-1}$ | $\pm5\,\%$ |
| silber | — | $10^{-2}$ | $\pm10\,\%$ |
| kein Ring | — | — | $\pm20\,\%$ |

Im Text des Skripts steht, der erste Ring gebe den Faktor $10^n$ an; nach seiner eigenen Tabelle (Bild 5.11) ist es der dritte. Für die feineren
Reihen ab E48 mit drei Ziffern gibt es den Code mit fünf Ringen: drei Ziffernringe, dann Multiplikator und Toleranz. Gelesen wird von der Seite, an der
die Ringe näher am Rand sitzen; der Toleranzring ist oft etwas abgesetzt, und Gold oder Silber stehen nie vorn.

**Im Bild:** Der Farbcode ist das Etikett am Brett: Er nennt den Widerstand, den das Brett im Mittel hat, und wie weit ein einzelnes davon abweichen darf.

::::beispiel Farbringe lesen
**(a) Gelb, violett, rot, gold.** Ziffern $4$ und $7$, Multiplikator $10^2$, Toleranz $\pm5\,\%$:

$$R = 47\cdot10^{2}\,\Omega = 4{,}7\,\text{k}\Omega, \qquad 4{,}7\,\text{k}\Omega\pm5\,\%:\ 4465\ \text{bis}\ 4935\,\Omega.$$

$47$ gehört zu E6, E12 und E24.

**(b) Braun, schwarz, schwarz, braun, braun** mit fünf Ringen. Ziffern $1$, $0$, $0$, Multiplikator $10^1$, Toleranz $\pm1\,\%$:

$$R = 100\cdot10^{1}\,\Omega = 1{,}00\,\text{k}\Omega \pm 1\,\%.$$

**(c) Braun, schwarz, gold, gold.** Gold als dritter Ring heißt Multiplikator $10^{-1}$:

$$R = 10\cdot10^{-1}\,\Omega = 1{,}0\,\Omega \pm 5\,\%.$$

**Im Bild:** Zwei Bretter mit dem Etikett $4{,}7\,\text{k}\Omega$ aus derselben Fertigung dürfen sich um bis zu $470\,\Omega$ unterscheiden — mal
etwas mehr, mal etwas weniger Nägel.
::::

## Temperatur: Kaltleiter und Heißleiter

Der Widerstand eines Bauteils ist nur bei fester Temperatur fest. Erwärmt es sich, ändert sich der spezifische Widerstand und mit ihm $R$. In einem nicht
zu großen Bereich um eine __Bezugstemperatur__ $\vartheta_0$ ist die Änderung nahezu linear:

:::formel
$$R(\vartheta) = R(\vartheta_0)\,\big(1 + \alpha_{\vartheta_0}\,(\vartheta - \vartheta_0)\big).$$
:::

**So liest man das:** Eingabe ist die Temperatur $\vartheta$ in Grad Celsius, Ausgabe der Widerstand bei dieser Temperatur. Der
__Temperaturkoeffizient__ $\alpha_{\vartheta_0}$ ist die relative Änderung des Widerstands pro Kelvin, bezogen auf den Wert bei $\vartheta_0$; in
Datenblättern ist das meist $20\,\text{°C}$. Für Kupfer ist $\alpha_{20}$ rund $3{,}9\cdot10^{-3}\,\text{K}^{-1}$: $0{,}39\,\%$ mehr Widerstand pro Kelvin,
$39\,\%$ mehr bei $100\,\text{K}$ Erwärmung. Temperaturunterschiede misst man in Kelvin; ein Kelvin Unterschied ist ein Grad Celsius Unterschied. Das
Skript schreibt die Temperatur $t$; hier steht nach DIN $\vartheta$, weil $t$ die Zeit ist. Die Formel ist eine **Näherung**: die Tangente an die
wahre, leicht gekrümmte Kurve.

**Im Bild:** Rüttelt man das Brett, zittern die Nägel stärker und werden öfter getroffen; die Kugeln kommen bei gleicher Neigung langsamer voran.

:::herleitung
**Linearisieren.** $R(\vartheta)$ ist eine glatte Funktion der Temperatur. In der Nähe von $\vartheta_0$ ersetzt man sie durch ihre Tangente, das erste
Glied der Taylor-Entwicklung:

$$R(\vartheta) \approx R(\vartheta_0) + R'(\vartheta_0)\,(\vartheta - \vartheta_0).$$

Klammert man $R(\vartheta_0)$ aus, steht die Formel da, mit der Steigung bezogen auf den Wert als Temperaturkoeffizient:

$$\alpha_{\vartheta_0} := \frac{R'(\vartheta_0)}{R(\vartheta_0)}.$$

Der Fehler wächst mit dem Quadrat des Abstands von $\vartheta_0$, so wie das nächste Glied der Taylor-Entwicklung. Für große Bereiche nimmt man deshalb
ein quadratisches Glied hinzu oder rechnet mit Tabellen.

**Warum $\alpha$ einen Index trägt.** Beschreibt man dieselbe Gerade von einer anderen Bezugstemperatur $\vartheta_1$ aus, bleibt ihre Steigung
$R(\vartheta_0)\,\alpha_{\vartheta_0}$ gleich, aber der Bezugswert ist jetzt $R(\vartheta_1)$. Geteilt durch ihn:

$$\alpha_{\vartheta_1} = \frac{R(\vartheta_0)\,\alpha_{\vartheta_0}}{R(\vartheta_1)} = \frac{\alpha_{\vartheta_0}}{1 + \alpha_{\vartheta_0}\,(\vartheta_1 - \vartheta_0)}.$$

Ein Kaltleiter hat also bei $0\,\text{°C}$ einen größeren Koeffizienten als bei $20\,\text{°C}$; ein $\alpha$ ohne Bezugstemperatur ist unvollständig.
:::

::::beispiel Wie warm ist die Motorwicklung?
**(a) Die Widerstandsmethode.** Die Kupferwicklung eines Motors hat bei $20\,\text{°C}$ den Widerstand $2{,}00\,\Omega$, nach einer Stunde Betrieb
$2{,}60\,\Omega$. Ein Thermometer lässt sich nicht hineinstecken, die Formel nach der Temperatur aufgelöst schon; mit
$3{,}93\cdot10^{-3}\,\text{K}^{-1}$ für Kupfer:

$$\vartheta - 20\,\text{°C} = \frac{R(\vartheta)/R(20\,\text{°C}) - 1}{\alpha_{20}} = \frac{1{,}30 - 1}{3{,}93\cdot10^{-3}\,\text{K}^{-1}} \approx 76\,\text{K}, \qquad \vartheta \approx 96\,\text{°C}.$$

Für Kupferwicklungen ist in der Praxis eine Formel mit $234{,}5\,\text{K}$ üblich, in der IEC-Norm für elektrische Maschinen gerundet $235\,\text{K}$.
Das ist genau der Kehrwert des Koeffizienten von Kupfer bei $0\,\text{°C}$:

$$\alpha_0 = \frac{\alpha_{20}}{1 - 20\,\text{K}\cdot\alpha_{20}} = \frac{3{,}93\cdot10^{-3}\,\text{K}^{-1}}{0{,}9214} \approx 4{,}27\cdot10^{-3}\,\text{K}^{-1}, \qquad \frac{1}{\alpha_0} \approx 234{,}5\,\text{K}.$$

**(b) Ein Pt100**, ein Temperaturfühler aus Platin, hat bei $0\,\text{°C}$ genau $100\,\Omega$. Sein Koeffizient $3{,}85\cdot10^{-3}\,\text{K}^{-1}$ ist
als mittlerer Anstieg zwischen $0$ und $100\,\text{°C}$ festgelegt, bezogen auf den Wert bei $0\,\text{°C}$ — eine Sekante statt der Tangente, für die
Rechnung gleichwertig. Bei Körpertemperatur:

$$R(37\,\text{°C}) = 100\,\Omega\cdot\big(1 + 3{,}85\cdot10^{-3}\,\text{K}^{-1}\cdot37\,\text{K}\big) \approx 114{,}2\,\Omega.$$

Die Normkurve mit quadratischem Glied gibt $114{,}4\,\Omega$; für genaue Messungen rechnet man mit ihr.

**Im Bild:** Nach einer Stunde Betrieb zittern die Nägel der Wicklung so heftig, dass das Brett $30\,\%$ stärker bremst — daran liest man ab, wie heiß es
ist.
::::

**Metalle sind Kaltleiter.** In einem Metall ist die Trägerdichte fest: Jedes Atom gibt seine Leitungselektronen ab, gleich wie warm es ist. Mit der
Temperatur schwingen die Atomrümpfe aber heftiger, die Elektronen werden häufiger gestreut, die mittlere Flugzeit $T$ wird kürzer, und mit ihr sinken
Beweglichkeit und Leitfähigkeit. Der Widerstand steigt, $\alpha$ ist positiv. Solche Materialien heißen __PTC__ (positive temperature coefficient) oder
__Kaltleiter__: Sie leiten besser, je kälter sie sind. Beispiele sind Kupfer, Silber, Platin und Wolfram.

**Im Bild:** Gerüttelte Nägel werden öfter getroffen; die Zahl der Kugeln bleibt dieselbe.

**Reine Halbleiter sind Heißleiter.** In einem reinen Halbleiter sind bei tiefer Temperatur fast alle Elektronen gebunden. Wärme reißt laufend weitere
los: Die Trägerdichte wächst mit der Temperatur sehr stark — viel stärker, als die Beweglichkeit durch die häufigeren Stöße sinkt. Der Widerstand fällt,
$\alpha$ ist negativ: ein __NTC__ (negative temperature coefficient) oder __Heißleiter__, der besser leitet, je wärmer er ist. Beispiele sind reines
Silizium und Germanium; technische Heißleiter bestehen meist aus halbleitenden Metalloxiden. Ihr Widerstand fällt etwa exponentiell, die Gerade aus der
Formel beschreibt sie nur in der Nähe von $\vartheta_0$. Und dotiertes Silizium, in dem eingebaute Fremdatome die Träger schon liefern (Kapitel 10),
verhält sich im üblichen Temperaturbereich sogar wie ein Kaltleiter.

**Im Bild:** Ein fast leeres Brett, auf dem die meisten Kugeln in Mulden festliegen. Rüttelt man es, springen viele heraus; dass die Nägel dabei stärker
zittern, fällt kaum ins Gewicht.

:::herleitung
**Der Mechanismus in der Formel.** Mit der Beweglichkeit des Drude-Modells ist die Leitfähigkeit

$$\sigma = e\,n_\text{e}\,\mu_\text{e} = \frac{e^2\,n_\text{e}\,T}{m_\text{e}}.$$

**Metall.** $n_\text{e}$ hängt nicht von der Temperatur ab, $T$ wird mit steigender Temperatur kürzer. Also sinkt $\sigma$, $\rho$ und $R$ steigen, und die
Ableitung $R'(\vartheta_0)$ in der Definition von $\alpha$ ist positiv.

**Halbleiter.** $T$ wird ebenfalls kürzer, aber die Trägerdichte wächst viel schneller. Das Produkt aus beiden wächst, $\sigma$ steigt, $R$ fällt, und
$R'(\vartheta_0)$ ist negativ.
:::

:::grafik
Szene: get1/stroeme-und-spannungen/02-temperatur · Vorlage: kalt-heissleiter
Links ein Diagramm $\rho/\rho_{20}$ über der Temperatur in °C wie Bild 5.12 des Skripts: drei Geraden, die sich bei $20\,\text{°C}$ im Wert $1$ schneiden — eine
steigende (PTC, Kaltleiter), eine fallende (NTC, Heißleiter) und eine waagrechte (kompensierte Legierung). Rechts drei kleine Nagelbretter. Ein
Temperaturregler rüttelt alle drei: Beim Metall-Brett zittern die Nägel stärker, die Kugeln werden langsamer; beim Halbleiter-Brett springen Kugeln aus
Mulden, es kommen viel mehr an; beim Legierungs-Brett mit vielen fest eingeschlagenen, schiefen Nägeln ändert das Zittern kaum etwas. Ein
Diagrammpunkt wandert auf jeder Geraden mit. Kernaussage: Beim Metall bremsen mehr Stöße, beim Halbleiter überwiegen die zusätzlichen Träger, bei der
Legierung dominiert die feste Unordnung. (Rot = PTC, blau = NTC, orange = kompensiert, grau = Achsen, gestrichelt = $20\,\text{°C}$.)
:::

**Kompensierte Legierungen.** In einer Legierung wie Konstantan sitzen die Nickelatome regellos zwischen den Kupferatomen. Jedes ist eine Störung, an der
die Elektronen gestreut werden, und diese Streuung hängt nicht von der Temperatur ab. Der spezifische Widerstand ist deshalb schon bei Zimmertemperatur
groß, fast dreißigmal so groß wie bei Kupfer, und die zusätzliche Streuung durch die Wärmeschwingungen macht nur einen kleinen Teil davon aus. Bezogen
auf das große $\rho$ ist der Anstieg winzig, $\alpha$ fast null. Bei Konstantan, rund $55\,\%$ Kupfer und $45\,\%$ Nickel, ist die Zusammensetzung
außerdem so gewählt, dass der verbleibende Anstieg nahezu verschwindet. Darum baut man Mess- und Präzisionswiderstände aus solchen Legierungen.

**Im Bild:** Ein Brett voller fest eingeschlagener, schiefer Nägel. Rüttelt man es, zittern ein paar Nägel mehr, aber gegen die vielen schiefen fällt das
kaum ins Gewicht.

:::herleitung
**Die Streuraten addieren sich.** Zwei voneinander unabhängige Ursachen streuen ein Elektron: die Wärmeschwingungen, für sich allein mit der mittleren
Flugzeit $T_\text{G}$, und die Fremdatome mit $T_\text{F}$. In einem kurzen Zeitstück $dt$ ist die Wahrscheinlichkeit für einen Stoß die Summe
$\frac{dt}{T_\text{G}}+\frac{dt}{T_\text{F}}$, also gilt für die gemeinsame Flugzeit:

$$\frac{1}{T} = \frac{1}{T_\text{G}} + \frac{1}{T_\text{F}}.$$

**Die Widerstände addieren sich.** Nach der Formel für $\sigma$ ist $\rho$ proportional zu $1/T$; die Summe überträgt sich auf $\rho$:

$$\rho = \frac{m_\text{e}}{e^2\,n_\text{e}}\Big(\frac{1}{T_\text{G}} + \frac{1}{T_\text{F}}\Big) = \rho_\text{G}(\vartheta) + \rho_\text{F}.$$

Das ist die __Matthiessensche Regel__. Nur $\rho_\text{G}$ hängt von der Temperatur ab.

**Darum ist $\alpha$ klein.** Der Temperaturkoeffizient ist der Anstieg bezogen auf den ganzen Wert:

$$\alpha = \frac{\rho_\text{G}'(\vartheta_0)}{\rho_\text{G}(\vartheta_0) + \rho_\text{F}}.$$

Steigt der Gitteranteil ungefähr so wie bei Kupfer, mit rund $7\cdot10^{-11}\,\Omega\,\text{m}$ pro Kelvin, ist der Koeffizient bei einem spezifischen
Widerstand von $5\cdot10^{-7}\,\Omega\,\text{m}$ nur etwa $1{,}4\cdot10^{-4}\,\text{K}^{-1}$, rund dreißigmal kleiner als bei Kupfer. Die abgestimmte
Zusammensetzung von Konstantan drückt ihn weiter auf die Größenordnung $10^{-5}\,\text{K}^{-1}$.
:::

Richtwerte für $\alpha_{20}$, je nach Reinheit leicht verschieden:

| Material | $\alpha_{20}$ in $10^{-3}\,\text{K}^{-1}$ | Verhalten |
|---|---|---|
| Kupfer | $3{,}9$ | Kaltleiter |
| Aluminium | $4{,}0$ | Kaltleiter |
| Silber | $3{,}8$ | Kaltleiter |
| Wolfram | $4{,}4$ | Kaltleiter |
| Platin | $3{,}9$ | Kaltleiter |
| Konstantan | etwa $0{,}01$ | nahezu konstant |
| Kohle | etwa $-0{,}5$ | Heißleiter |

**Kaltleiter und Heißleiter in Reihe.** Statt im Material kann man auch im Bauteil ausgleichen: Man schaltet einen Kaltleiter und einen Heißleiter
hintereinander. Ihre Widerstände addieren sich, und die Summe hängt in der linearen Näherung nicht von der Temperatur ab, wenn sich die beiden Anstiege
aufheben:

$$R_1(\vartheta_0)\,\alpha_1 + R_2(\vartheta_0)\,\alpha_2 = 0.$$

Dabei sind $R_1$, $R_2$ die beiden Widerstände und $\alpha_1$, $\alpha_2$ ihre Koeffizienten bei derselben Bezugstemperatur; einer davon muss negativ
sein.

**Im Bild:** Ein Brett, das beim Rütteln bremst, hinter einem, das beim Rütteln Kugeln freigibt — insgesamt kommt gleich viel an.

:::herleitung
**Hintereinander addieren sich Widerstände.** Durch beide fließt derselbe Strom $I$, denn Ladung häuft sich zwischen ihnen nicht an (Kontinuität). Die
Spannung über beide ist die Summe der Einzelspannungen, denn das Wegintegral des Felds zerfällt in die beiden Teilstücke:

$$U = U_1 + U_2 = R_1\,I + R_2\,I = (R_1 + R_2)\,I.$$

Die Kombination wirkt also wie ein Widerstand $R_1+R_2$; ausführlich im Artikel über die Zusammenschaltung von Widerständen.

**Die Temperatur.** Beide in der linearen Näherung eingesetzt und nach Gliedern sortiert:

$$R_1(\vartheta) + R_2(\vartheta) = R_1(\vartheta_0) + R_2(\vartheta_0) + \big(R_1(\vartheta_0)\,\alpha_1 + R_2(\vartheta_0)\,\alpha_2\big)\,(\vartheta - \vartheta_0).$$

Verschwindet die Klammer, bleibt die Summe für jede Temperatur gleich. Weil der Widerstand von Heißleitern stark gekrümmt von der Temperatur abhängt,
gelingt der Ausgleich nur in der Nähe von $\vartheta_0$.
:::

::::beispiel Ausgleich mit Kupfer
Ein Kohleschichtwiderstand $R_\text{C}$ mit $1000\,\Omega$ und dem Koeffizienten $\alpha_\text{C}$ von $-5\cdot10^{-4}\,\text{K}^{-1}$ soll mit einem
Kupferdraht $R_\text{Cu}$ in Reihe temperaturunabhängig werden; Kupfer hat $\alpha_\text{Cu}$ von $3{,}93\cdot10^{-3}\,\text{K}^{-1}$. Der
Kupferwiderstand folgt aus der Bedingung:

$$R_\text{Cu} = -\frac{R_\text{C}\,\alpha_\text{C}}{\alpha_\text{Cu}} = \frac{1000\,\Omega\cdot5\cdot10^{-4}\,\text{K}^{-1}}{3{,}93\cdot10^{-3}\,\text{K}^{-1}} \approx 127{,}2\,\Omega.$$

Probe bei $50\,\text{°C}$, also $30\,\text{K}$ wärmer:

$$R_\text{C} = 1000\,\Omega\cdot(1 - 0{,}015) = 985{,}0\,\Omega, \qquad R_\text{Cu} = 127{,}2\,\Omega\cdot(1 + 0{,}118) \approx 142{,}2\,\Omega.$$

Die Summe ist bei $20\,\text{°C}$ wie bei $50\,\text{°C}$ gleich $1127{,}2\,\Omega$. Ein Kupferwiderstand von $1127{,}2\,\Omega$ allein wäre bei $50\,\text{°C}$ um
$11{,}8\,\%$ gestiegen.

**Im Bild:** Das Kohle-Brett gibt beim Rütteln $15\,\Omega$ nach, das Kupfer-Brett legt $15\,\Omega$ zu.
::::

## Zweipole: linear und nichtlinear

Der Widerstand ist das erste Beispiel einer Sichtweise, mit der die ganze Schaltungstechnik arbeitet. Das Skript führt dazu drei Begriffe ein:

- Ein __Zweipol__ ist ein Bauelement mit zwei Anschlussklemmen, dessen Verhalten sich vollständig durch den Zusammenhang von Strom und Spannung an
  diesen Klemmen beschreiben lässt.
- Eine __Blackbox__ ist ein Zweipol, dessen Verhalten nach außen man kennt, dessen innerer Aufbau aber unbekannt oder uninteressant ist.
- Ein __Netzwerk__ ist eine Zusammenschaltung von Zweipolen.

Das __stationäre__ Klemmenverhalten, wenn sich zeitlich nichts mehr ändert, beschreibt die __Kennlinie__:

$$I = f(U).$$

Zu jeder Spannung an den Klemmen gehört der Strom, der sich nach dem Einschwingen einstellt. Strom und Spannung zählt man mit Pfeilen, die beide in
dieselbe Richtung durch den Zweipol zeigen (Bild 5.14 des Skripts); was diese Vereinbarung bedeutet und wozu sie gut ist, zeigt der nächste Artikel über
Zählpfeile.

**Im Bild:** Für die Kennlinie ist es gleich, wie das Brett innen aussieht. Man misst nur, wie viele Kugeln pro Sekunde bei welchem Höhenunterschied
ankommen.

**Lineare Zweipole** haben eine gerade Kennlinie. Das Skript zeigt als Beispiele (Bild 5.13) einen Widerstand, eine ideale Spannungsquelle und eine
ideale Stromquelle; die Quellen kommen in Kapitel 7 genauer vor. Beim Widerstand geht die Gerade durch den Ursprung, und es gilt das Ohmsche Gesetz:

$$G = \frac{I}{U} = \text{const}, \qquad R = \frac{U}{I} = \text{const}.$$

Bild 5.15 zeigt drei Widerstände mit $R_1<R_2<R_3$: Je kleiner der Widerstand, desto steiler die Gerade, denn ihre Steigung im Diagramm Strom über
Spannung ist der Leitwert. Die Geraden laufen durch den Ursprung in den dritten Quadranten weiter: Kehrt man die Spannung um, kehrt sich der Strom um, und
ein Widerstand leitet in beide Richtungen gleich.

Genau genommen gilt der Satz des Skripts „Für lineare Zweipole gilt das ohmsche Gesetz" nur für Geraden durch den Ursprung. Auch eine Quelle hat eine
gerade Kennlinie, aber eine, die nicht durch den Ursprung geht: Eine ideale Spannungsquelle hält ihre Spannung bei jedem Strom, eine ideale Stromquelle
ihren Strom bei jeder Spannung. Das Verhältnis von Spannung zu Strom ist dort nicht konstant.

**Nichtlineare Zweipole** haben eine gekrümmte Kennlinie. Das Verhältnis $U/I$ ist dann in jedem Punkt ein anderes. Man kann es weiterhin ausrechnen,
als Widerstand im jeweiligen Betriebspunkt, aber es ist keine Konstante des Bauteils mehr. Für kleine Änderungen um einen Punkt zählt stattdessen die
Steigung der Kennlinie dort, der __differentielle Widerstand__, der bei Dioden wichtig wird (Kapitel 10).

**Die Glühlampe.** Das Beispiel des Skripts ist die __Glühlampe__ (Bild 5.16). Ihr Glühfaden besteht meist aus Wolfram, einem Kaltleiter. Fließt Strom,
erzeugt er Wärme, und der Faden heizt sich auf, bis er so viel abstrahlt, wie er erzeugt. Je höher die Spannung, desto heißer der Faden und desto größer
sein Widerstand: Die Kennlinie beginnt im Ursprung steil — kalter Faden, kleiner Widerstand — und wird mit wachsender Spannung immer flacher. Sie ist
punktsymmetrisch zum Ursprung, denn die Wärme hängt nicht von der Richtung des Stroms ab.

**Der Einschaltstrom.** Vor dem Einschalten ist der Faden kalt und sein Widerstand klein; im Moment des Einschaltens fließt deshalb ein Vielfaches des
Nennstroms. Der dünne Faden heizt sich in Sekundenbruchteilen auf, sein Widerstand steigt, und der Strom sinkt, bis er seinen Nennwert erreicht. Die
Kennlinie aus Bild 5.16 beschreibt nur den eingeschwungenen Zustand. Beim Einschalten liegt der Betriebspunkt zuerst auf der steilen Geraden des kalten
Fadens und wandert dann auf die Kennlinie hinunter.

**Im Bild:** Ein Brett, dessen Nägel sich durch die Stöße selbst erwärmen. Je steiler es steht, desto mehr Stöße pro Sekunde, desto heftiger zittern die
Nägel und desto stärker bremsen sie — der Strom wächst langsamer als die Spannung. Beim Einschalten ist das Brett noch kalt.

:::herleitung
**Warum die Kurve flacher wird.** Im eingeschwungenen Zustand gibt der Faden so viel Wärme ab, wie der Strom erzeugt. Mehr Spannung bedeutet mehr
Leistung $U\,I$, also eine höhere Gleichgewichtstemperatur und nach der Temperaturformel einen größeren Widerstand. Das Verhältnis $I/U$, die Steigung
der Geraden vom Ursprung zum Betriebspunkt, sinkt deshalb mit wachsender Spannung.

**Punktsymmetrie.** Kehrt man die Spannung um, fließt derselbe Strom in Gegenrichtung und erzeugt dieselbe Wärme $R\,I^2$, denn das Quadrat ändert sich
nicht. Gleiche Temperatur heißt gleicher Widerstand, also ein gleich großer Strom mit umgekehrtem Vorzeichen:

$$f(-U) = -f(U).$$

**Einschaltstrom.** Im ersten Augenblick hat der Faden noch seine Raumtemperatur, also seinen kleinen kalten Widerstand, und der Strom ist Spannung durch
diesen Widerstand.
:::

:::grafik
Szene: get1/stroeme-und-spannungen/02-zweipole · Vorlage: zweipol-kennlinien
Links eine Blackbox mit zwei Klemmen, der Strompfeil $I$ zeigt in die obere Klemme hinein, der Spannungspfeil $U$ von der oberen zur unteren Klemme. Ein
Auswahlschalter setzt in die Box: einen Widerstand, eine ideale Spannungsquelle, eine ideale Stromquelle, eine Glühlampe oder eine Diode. Rechts das
Diagramm $I$ über $U$: Widerstand = Ursprungsgerade, dazu drei Beispielgeraden $R_1<R_2<R_3$, die kleinste am steilsten; Spannungsquelle = senkrechte
Gerade bei $U_\text{q}$; Stromquelle = waagrechte Gerade bei $I_\text{q}$; Glühlampe = punktsymmetrische S-Kurve, am Ursprung steil und nach außen
flacher; Diode = lange flach, dann steil ansteigend, in Gegenrichtung nahezu null. Ein Betriebspunkt ist auf der Kurve verschiebbar; die gestrichelte
Gerade zum Ursprung zeigt das Verhältnis $U/I$, eine Tangente die Steigung. Kernaussage: Linear heißt gerade Kennlinie; das Ohmsche Gesetz mit festem
$R$ gilt für die Ursprungsgerade. (Rot = Kennlinie, blau = Zählpfeile, orange = Betriebspunkt und Tangente, grau = Achsen und Box, gestrichelt =
Ursprungsgerade.)
:::

::::beispiel Eine kleine Glühlampe
Eine Lampe für $6\,\text{V}$ nimmt im Betrieb $0{,}5\,\text{A}$ auf; kalt misst man am Faden $1{,}0\,\Omega$. Der Widerstand im Betrieb und der Strom im
Einschaltmoment:

$$R_\text{heiß} = \frac{6\,\text{V}}{0{,}5\,\text{A}} = 12\,\Omega, \qquad I_\text{Ein} = \frac{6\,\text{V}}{1{,}0\,\Omega} = 6\,\text{A}.$$

Beim Einschalten fließt kurz das Zwölffache des Nennstroms — darum brennen Glühlampen meist im Einschaltmoment durch.

**Die Krümmung.** Angenommen, bei $3\,\text{V}$ fließen $0{,}35\,\text{A}$. Dort ist das Verhältnis

$$\frac{U}{I} = \frac{3\,\text{V}}{0{,}35\,\text{A}} \approx 8{,}6\,\Omega.$$

Halbe Spannung, aber $70\,\%$ des Stroms: Bei einer Ursprungsgeraden wären es $50\,\%$.

**Wie heiß ist der Faden?** Mit der linearen Temperaturformel und dem Koeffizienten von Wolfram, $4{,}4\cdot10^{-3}\,\text{K}^{-1}$:

$$\vartheta - 20\,\text{°C} = \frac{12\,\Omega/1{,}0\,\Omega - 1}{4{,}4\cdot10^{-3}\,\text{K}^{-1}} = 2500\,\text{K}, \qquad \vartheta \approx 2520\,\text{°C}.$$

Über so viele Kelvin ist die Gerade aber nur eine grobe Näherung. Der Widerstand von Wolfram wächst bei hohen Temperaturen stärker als linear; dasselbe
Verhältnis $12$ wird deshalb schon bei niedrigerer Temperatur erreicht, eher um $2000\,\text{°C}$.

**Im Bild:** Beim Einschalten ist das Brett kalt und bremst kaum, die Kugeln schießen in Massen hinunter. Erst wenn die Nägel heiß zittern, stellt sich
der ruhige Betrieb ein.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/02-gluehlampe · Vorlage: einschaltstrom
Oben das Diagramm $I$ über $U$ der Glühlampe: die eingeschwungene S-Kurve und eine steile Gerade für den kalten Faden mit $1\,\Omega$. Beim Druck auf
„Einschalten" springt der Betriebspunkt bei $6\,\text{V}$ auf die kalte Gerade ($6\,\text{A}$) und wandert dann senkrecht nach unten auf die Kurve
($0{,}5\,\text{A}$). Darunter der Strom über der Zeit: eine hohe Spitze, die in Sekundenbruchteilen auf den Nennstrom abklingt; daneben ein Glühfaden,
der von dunkel über rot nach gelbweiß aufleuchtet, und das Nagelbrett, dessen Nägel immer stärker zittern. Kernaussage: Die Kennlinie gilt nur
eingeschwungen; beim Einschalten ist der kalte Faden ein kleiner Widerstand. (Rot = Betriebspunkt und Strom, blau = Kennlinien, orange = Aufheizen,
grau = Achsen.)
:::

## Bedeutung und Ausblick

Das Ohmsche Gesetz ist das Arbeitspferd der Schaltungstechnik. Zusammen mit den Kirchhoffschen Regeln, die in diesem Kapitel noch folgen, lässt sich
damit jedes Netz aus Widerständen und Quellen berechnen. Fast alles Weitere baut darauf auf: die Zählpfeile im nächsten Artikel, Knoten und Maschen, die
Zusammenschaltung von Widerständen — hintereinander addieren sich Widerstände, nebeneinander Leitwerte — und die Mess- und Netzwerkverfahren der
Kapitel 6 bis 9.

Die mikroskopische Seite kehrt bei den Halbleitern zurück (Kapitel 10). Dort stellt man über eingebaute Fremdatome gezielt die Trägerdichte in
$\sigma=e\,n_\text{e}\,\mu_\text{e}$ ein — der Kern jeder Diode und jedes Transistors.

An seine Grenzen kommt das Ohmsche Gesetz an drei Stellen. Bei schnell wechselnden Strömen drängt sich der Strom an die Oberfläche, der wirksame
Querschnitt schrumpft, und der Widerstand steigt (Skin-Effekt). Wird ein Leiter stark warm, ändert sich $\rho$, und die Kennlinie krümmt sich wie bei der
Glühlampe. Und manche Stoffe verlieren unterhalb einer kritischen Temperatur ihren Widerstand vollständig — die __Supraleitung__, die das Stoßmodell
nicht erklären kann.

:::kern
- Im stromdurchflossenen Draht herrscht ein Feld; es beschleunigt jedes Elektron gegen die Feldrichtung.
- Stöße machen daraus eine konstante __Driftgeschwindigkeit__ $\vec v_\text{D}=-\mu_\text{e}\vec E$, proportional zum Feld statt mit der Zeit wachsend.
- Im Sägezahn-Modell ist die __Beweglichkeit__ $\mu_\text{e}=\frac{eT}{2m_\text{e}}$; mit zufälligen Flugzeiten entfällt der Faktor $\frac12$.
- Gestreut wird an Störungen des Gitters, an Wärmeschwingungen und Fremdatomen, nicht an jedem Atom; in Kupfer fliegt ein Elektron rund $37\,\text{nm}$.
- __Ohmsches Gesetz in Punktform__: $\vec J=\sigma\vec E$, mit der Leitfähigkeit Ladung mal Trägerdichte mal Beweglichkeit.
- __Spezifischer Widerstand__ $\rho=\frac1\sigma$ in $\Omega\,\text{m}$, nicht in $\Omega\,\text{cm}^{-1}$; Kupfer hat $0{,}0179\,\Omega\,\frac{\text{mm}^2}{\text{m}}$.
- Homogenes Leiterstück: $R=\rho\,\frac{l}{A}$ hängt nur von Material und Form ab, darum ist die Spannung proportional zum Strom.
- __Leitwert__ $G=\frac1R$ in Siemens; die Kennlinie des Widerstands ist eine Ursprungsgerade mit der Steigung $R$ oder $G$.
- Die Energie geht bei den Stößen ans Gitter, als __Stromwärme__ $P=U\,I=R\,I^2$.
- __E-Reihen__: Normwerte im festen Verhältnis $\sqrt[N]{10}$, passend zur festen relativen Toleranz; bis E24 überlappen die Bänder.
- __Farbcode__: Ziffernringe, dann Multiplikator, dann Toleranz — der Multiplikator ist der dritte Ring.
- Temperatur: $R(\vartheta)\approx R(\vartheta_0)\big(1+\alpha_{\vartheta_0}(\vartheta-\vartheta_0)\big)$; Metalle sind Kaltleiter, reine Halbleiter Heißleiter.
- Legierungen wie Konstantan bleiben fast temperaturunabhängig, weil die feste Unordnung die Streuung beherrscht.
- __Zweipol__: beschrieben durch die Kennlinie; linear heißt Gerade, ohmsch heißt Ursprungsgerade; die Glühlampe ist nichtlinear.
:::

:::quiz
F: Warum wird ein Elektron im Draht nicht immer schneller, obwohl das Feld es ständig beschleunigt?
A: Es wird im Mittel alle paar Femtosekunden an Störungen des Gitters gestreut und verliert dabei die in Feldrichtung gewonnene Zusatzgeschwindigkeit. Zwischen zwei Stößen wächst die Geschwindigkeit linear; im Mittel bleibt eine konstante Driftgeschwindigkeit $\vec v_\text{D}=-\mu_\text{e}\vec E$, proportional zum Feld. Im Vakuum hätte ein Elektron im Feld von $11{,}9\,\text{mV}/\text{m}$ nach einer Mikrosekunde schon $2{,}1\,\text{km}/\text{s}$, im Kupferdraht driftet es dauerhaft mit $0{,}05\,\text{mm}/\text{s}$.
F: Woher kommt im Sägezahn-Modell der Faktor $\frac12$ in der Beweglichkeit, und warum fehlt er in den meisten Lehrbüchern?
A: In jedem Flug steigt die Geschwindigkeit linear von null auf $v_\text{max}=\frac{eE}{m_\text{e}}T$; der Mittelwert eines Dreiecks ist die halbe Höhe, also $\mu_\text{e}=\frac{eT}{2m_\text{e}}$. Bei zufälligen Flugzeiten mit dem Mittelwert $T$ zählen lange Flüge stärker, weil der Weg mit dem Quadrat der Flugzeit wächst: Der Mittelwert $\frac a2\frac{\langle t^2\rangle}{\langle t\rangle}$ wird $a\,T$, und es bleibt $\mu_\text{e}=\frac{eT}{m_\text{e}}$, das Drude-Modell.
F: Woran werden die Elektronen in einem Metall wirklich gestreut, und wie weit fliegen sie in Kupfer?
A: Nicht an jedem Atom — durch ein vollkommen regelmäßiges, ruhendes Gitter liefe die Elektronenwelle ungestört. Gestreut wird an Störungen: an Wärmeschwingungen der Atomrümpfe, Fremdatomen und Gitterfehlern. In Kupfer ist die mittlere Flugzeit etwa $2{,}3\cdot10^{-14}\,\text{s}$; mit der ungeordneten Geschwindigkeit von rund $1{,}57\cdot10^6\,\text{m}/\text{s}$ sind das etwa $37\,\text{nm}$ oder rund $160$ Atomabstände. Startete das Elektron wie im Sägezahn jedes Mal aus der Ruhe, käme es nur $2\cdot10^{-18}\,\text{m}$ weit.
F: Warum zeigt die Stromdichte $\vec J=\sigma\vec E$ in Feldrichtung, obwohl die Elektronen gegen das Feld driften?
A: Die Stromdichte ist Raumladungsdichte mal Geschwindigkeit. Die Raumladungsdichte der Elektronen, $-e\,n_\text{e}$, ist negativ, und die Drift $-\mu_\text{e}\vec E$ zeigt gegen das Feld. Die beiden Minuszeichen heben sich auf, $\vec J=e\,n_\text{e}\,\mu_\text{e}\,\vec E$, und $\sigma$ ist positiv — wie es die technische Stromrichtung verlangt.
F: Warum leitet reines Silizium so viel schlechter als Kupfer, obwohl seine Elektronen $34$-mal so beweglich sind?
A: Die Leitfähigkeit ist das Produkt $e\,n_\text{e}\,\mu_\text{e}$. Kupfer hat rund $8{,}5\cdot10^{28}$ Leitungselektronen pro Kubikmeter, reines Silizium bei Raumtemperatur nur etwa $10^{16}$, also $8{,}5\cdot10^{12}$-mal weniger. Das überwiegt die höhere Beweglichkeit bei Weitem: Die Elektronen liefern im Silizium rund $2{,}5\cdot10^{11}$-mal weniger Leitfähigkeit.
F: Wie folgt aus $\vec J=\sigma\vec E$ das Ohmsche Gesetz für ein Leiterstück, und welche Voraussetzungen braucht man?
A: Im stationären Zustand fließt durch jeden Querschnitt derselbe Strom. Bei homogenem Material und gleichem Querschnitt sind dann Stromdichte $\frac IA$ und Feld $\frac{I}{\sigma A}$ überall gleich, und die Spannung ist Feld mal Länge. Zusammen: $U=\frac{l}{\sigma A}I=R\,I$ mit $R=\rho\,\frac lA$. Voraussetzungen: homogenes Material, gleicher Querschnitt, gleichmäßige Einspeisung oder Länge viel größer als die Dicke, konstanter Strom und konstante Temperatur.
F: Welchen Widerstand hat eine Kabeltrommel mit $25\,\text{m}$ Leitung aus $1{,}5\,\text{mm}^2$ Kupfer, und was folgt daraus bei $16\,\text{A}$?
A: Hin- und Rückleiter ergeben $50\,\text{m}$, also $R=0{,}0179\,\Omega\,\frac{\text{mm}^2}{\text{m}}\cdot\frac{50\,\text{m}}{1{,}5\,\text{mm}^2}\approx0{,}6\,\Omega$. Bei $16\,\text{A}$ fallen rund $9{,}5\,\text{V}$ ab, und die Leitung setzt $R\,I^2\approx152\,\text{W}$ in Wärme um. Aufgerollt kann diese Wärme kaum entweichen; deshalb ist für den aufgerollten Zustand eine viel kleinere Last zulässig.
F: Warum sind die E-Reihen geometrisch gestuft, und warum lässt sich bei E12 mit $\pm10\,\%$ jeder gefertigte Widerstand einem Normwert zuordnen?
A: Die Toleranz ist relativ, die absolute Unsicherheit wächst also mit dem Wert; passend dazu stehen Nachbarn im festen Verhältnis $q=\sqrt[N]{10}$. Zwei Toleranzbänder überlappen, wenn $\frac{1+\delta}{1-\delta}\ge q$ ist. Für E12 ist $q\approx1{,}2115$ und die Grenze $\frac{1{,}1}{0{,}9}\approx1{,}222$, die Bänder überlappen lückenlos. Ab E48 bleiben schmale Lücken.
F: Warum steigt der Widerstand von Metallen mit der Temperatur, warum fällt er bei reinen Halbleitern, und warum bleibt Konstantan fast konstant?
A: Im Metall ist die Trägerdichte fest, aber stärkere Wärmeschwingungen verkürzen die Flugzeit; Beweglichkeit und Leitfähigkeit sinken, $R$ steigt — ein Kaltleiter mit positivem $\alpha$. Im reinen Halbleiter setzt Wärme viele neue Träger frei; das überwiegt, $R$ fällt — ein Heißleiter. In Konstantan beherrscht die temperaturunabhängige Streuung an den regellos verteilten Fremdatomen den Widerstand (Matthiessensche Regel); der wärmeabhängige Anteil ist relativ klein, und die abgestimmte Zusammensetzung drückt $\alpha$ auf etwa $10^{-5}\,\text{K}^{-1}$.
F: Was unterscheidet einen linearen von einem nichtlinearen Zweipol, und warum zieht eine Glühlampe beim Einschalten so viel Strom?
A: Ein linearer Zweipol hat eine gerade Kennlinie; geht sie durch den Ursprung, ist es ein ohmscher Widerstand mit konstantem $\frac UI$, während Quellen Geraden außerhalb des Ursprungs haben. Beim nichtlinearen Zweipol ist die Kennlinie gekrümmt, $\frac UI$ hängt vom Betriebspunkt ab. Der Wolframfaden einer Glühlampe ist ein Kaltleiter und kalt viel niederohmiger — bei der $6$-V-Lampe $1\,\Omega$ statt $12\,\Omega$. Beim Einschalten fließt deshalb kurz das Zwölffache des Nennstroms, bis sich der Faden in Sekundenbruchteilen aufgeheizt hat.
:::
