---
title: Halbleiter und das Bändermodell
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100100
summary: Von Grund auf – warum ein Kristall wie Silizium mal leitet und mal isoliert und wie man das gezielt einstellt. Leitbild ist ein Parkhaus mit zwei Decks, unten zugeparkt, oben frei, dazwischen eine Rampe. Mit der Diode als Ventil im Einweggleichrichter, Energiebändern und Bandlücke, Leitern, Halbleitern und Isolatoren, Löchern als positiven Ladungsträgern, Fermi-Verteilung und Fermi-Niveau, Eigenleitung und Massenwirkungsgesetz, n- und p-Dotierung mit Majoritäts- und Minoritätsträgern sowie dem pn-Übergang mit Raumladungszone, Diffusionsspannung und Durchlass- und Sperrrichtung. Mit Beispiel-Seite.
tags: Halbleiter, Bändermodell, Bandlücke, Eigenleitung, Loch, Dotierung, pn-Übergang, Raumladungszone
---

## Anschaulich

Bisher kamen in diesem Fach Leiter vor, durch die Strom fließt, und Isolatoren, durch die keiner fließt. __Halbleiter__ liegen dazwischen, und darin liegt
ihr Wert: Ob und wie gut sie leiten, hängt von der Temperatur, vom Licht, von eingebauten Fremdatomen und von der angelegten Spannung ab. Daraus baut man
Bauteile, die Strom nur in einer Richtung durchlassen oder ihn steuern; Netzteile, Computer und Smartphones beruhen darauf.

**Das Leitbild dieses Artikels:** **ein Parkhaus mit zwei Decks.** Die Autos sind die Elektronen eines Kristalls, die Parkplätze die Zustände, die sie
einnehmen dürfen. Das Unterdeck ist bis auf den letzten Platz zugeparkt, das Oberdeck ist leer. Dazwischen führt eine Rampe, und ihre Höhe ist die Energie,
die ein Auto braucht, um nach oben zu kommen. Wärme rüttelt am ganzen Parkhaus und gibt einzelnen Autos ab und zu einen kräftigen Stoß.

Drei Folgerungen:

- **Ein volles Deck steht still.** Auf dem zugeparkten Unterdeck kann kein Auto fahren, weil kein Platz frei ist, in den es rollen könnte. Ein voller
  Kristall leitet nicht, so viele Elektronen er auch hat.
- **Bewegung braucht ein Auto oben oder eine Lücke unten.** Schafft es ein Auto über die Rampe, fährt es oben frei herum. Unten bleibt eine Lücke zurück:
  Das Nachbarauto rückt hinein, dann dessen Nachbar, und die Lücke wandert rückwärts durch das Deck. Auch sie trägt Strom.
- **Die Rampe entscheidet.** Ist sie niedrig, schafft es bei Raumtemperatur ein winziger Teil der Autos nach oben: ein Halbleiter. Ist sie hoch, schafft
  es praktisch keines: ein Isolator. Hat schon das untere Deck freie Plätze, fließt immer Verkehr: ein Metall.

Gezielt eingebaute Fremdatome sind wie wenige zusätzliche Autos, die knapp unter dem Oberdeck warten, oder wie wenige zusätzliche freie Plätze knapp über
dem Unterdeck; damit stellt man ein, wie viel Verkehr fließt. Fügt man zwei so vorbereitete Parkhäuser aneinander, entsteht zwischen ihnen eine Rampe, deren
Höhe die angelegte Spannung verstellt. Das ist das Ventil, das __Diode__ heißt.

Die Rollen auf einen Blick; jede Zeile bekommt unten ihren eigenen Abschnitt:

| Im Parkhaus | Im Kristall |
|---|---|
| Auto | Elektron |
| Parkplatz | erlaubter Zustand |
| Unterdeck, voll | Valenzband |
| Oberdeck, leer | Leitungsband |
| Höhe der Rampe | Bandlücke $W_g$ |
| Rütteln | Temperatur, Energieskala $k_BT$ |
| Lücke im Unterdeck | Loch, positiver Ladungsträger |
| Höhe, bis zu der das Haus zur Hälfte voll ist | Fermi-Niveau $W_F$ |
| wartende Autos knapp unter dem Oberdeck | Donatoren |
| freie Plätze knapp über dem Unterdeck | Akzeptoren |
| Rampe zwischen zwei Parkhäusern | Diffusionsspannung am pn-Übergang |

:::grafik
Szene: get1/halbleiterbauelemente/01-parkhaus · Vorlage: parkhaus-baender
Ein Parkhaus im Querschnitt mit zwei Decks übereinander: unten das Unterdeck voll mit Autos, oben das leere Oberdeck, dazwischen eine Rampe mit Höhenangabe.
Ein Regler „Temperatur“ lässt das Bild zittern; je höher die Temperatur, desto öfter springt ein Auto über die Rampe nach oben, und im Unterdeck bleibt eine
Lücke, in die das Nachbarauto rückt, sodass die Lücke sichtbar rückwärts wandert. Ein Schalter „Feld an“ lässt die oberen Autos nach links und die Lücken
nach rechts driften. Drei Tasten wechseln zwischen Metall (ein halbvolles Deck, viel Verkehr), Halbleiter (niedrige Rampe, wenige Autos oben) und Isolator
(sehr hohe Rampe, kein Auto oben). Kernaussage: Nur Autos mit freien Plätzen vor sich und Lücken können sich bewegen, und die Höhe der Rampe bestimmt, wie
viele es gibt. (Blau = Autos, rot = Lücken, orange = Rampe und Höhenangabe, grau = Parkhaus.)
:::

## Wozu Halbleiter: die Diode als Ventil

Das Skript beginnt mit einer Anwendung. Ein Akku braucht zum Laden einen Strom in einer Richtung, die Steckdose liefert Wechselspannung. Eine
__Wechselspannung__ ändert ihren Wert periodisch, meist sinusförmig. Ihr Momentanwert, nach DIN klein geschrieben, ist

$$u_E(t) = \hat U_E\,\sin(\omega t),$$

mit dem __Scheitelwert__ $\hat U_E$, im Skript $10\,\text{V}$, und der __Kreisfrequenz__ $\omega$, bei $50\,\text{Hz}$ also $2\pi\cdot50\,\text{s}^{-1}$.

Die __Diode__ ist das Bauteil, das Strom nur in einer Richtung durchlässt, das elektrische Gegenstück zum Rückschlagventil aus dem Artikel über das
Superpositionsverfahren. In Reihe mit einem Widerstand $R$ an die Wechselspannung gelegt, lässt sie nur die positiven Halbwellen durch; die Schaltung heißt
__Einweggleichrichter__. Das Skript rechnet in seinen Bildern mit einer Diode, die leitet, sobald an ihr etwa $0{,}6\,\text{V}$ liegen, und diese Spannung
dann hält. Diese __Durchlassspannung__ heißt hier $U_F$. Mit $u_A$ am Widerstand und $u_D$ an der Diode gilt:

$$u_A(t) = \begin{cases} u_E(t) - U_F, & u_E(t) > U_F, \\ 0 & \text{sonst}, \end{cases} \qquad u_D(t) = \begin{cases} U_F, & u_E(t) > U_F, \\ u_E(t) & \text{sonst}. \end{cases}$$

**So liest man das:** In der positiven Halbwelle leitet die Diode, und am Widerstand liegt die Eingangsspannung bis auf die $0{,}6\,\text{V}$ der Diode. In der
negativen Halbwelle sperrt sie; durch den Widerstand fließt kein Strom, und die ganze Spannung liegt an der Diode. Aus der Wechselspannung wird eine
pulsierende Spannung, die nie negativ ist, die erste Stufe jedes Netzteils; mehr dazu im Artikel über Gleichrichtung. Wie ein Kristall das fertigbringt,
erklärt der Rest dieses Artikels.

**Im Bild:** Ein Ventil, das nur in einer Richtung öffnet und dafür einen kleinen Mindestdruck braucht. Woraus dieses Ventil im Parkhaus besteht, zeigt der
Abschnitt über den pn-Übergang.

:::herleitung
**Die Maschenregel.** Quelle, Widerstand und Diode bilden eine Masche. Mit den Zählpfeilen des Skripts und dem Strom $i(t)$ durch die Masche:

$$u_E(t) = u_A(t) + u_D(t), \qquad u_A(t) = R\,i(t).$$

**Leitet die Diode,** hält sie $U_F$, und für den Widerstand bleibt der Rest der Eingangsspannung. Das geht nur, solange dabei ein Strom in
Durchlassrichtung fließt, also solange $u_E(t)$ größer als $U_F$ ist.

**Sperrt die Diode,** fließt kein Strom. Dann ist $u_A$ null, und die Diode trägt die ganze Eingangsspannung. Im Bild: Ein geschlossenes Ventil hält den
ganzen Gegendruck, und durch die Leitung dahinter fließt nichts.
:::

::::beispiel Ein Einweggleichrichter in Zahlen
Die Schaltung aus den Bildern 10.2 und 10.3 des Skripts, mit einem Widerstand dazu:

$$\hat U_E = 10\,\text{V}, \qquad U_F = 0{,}6\,\text{V}, \qquad R = 1\,\text{k}\Omega, \qquad \omega = 2\pi\cdot50\,\text{s}^{-1}.$$

**Spitzenwerte.** Im Scheitel der positiven Halbwelle:

$$\hat U_A = 10\,\text{V} - 0{,}6\,\text{V} = 9{,}4\,\text{V}, \qquad \hat I = \frac{9{,}4\,\text{V}}{1\,\text{k}\Omega} = 9{,}4\,\text{mA}.$$

**Wann die Diode leitet.** Sie öffnet, sobald der Sinus $0{,}6$ von $10\,\text{V}$ erreicht, also beim Winkel

$$\omega t_1 = \arcsin\frac{0{,}6\,\text{V}}{10\,\text{V}} = 3{,}44^\circ,$$

und schließt ebenso viel vor dem Ende der Halbwelle. Sie leitet also $173{,}1^\circ$ von $360^\circ$, gut 48 % jeder Periode; bei $50\,\text{Hz}$ sind das
$9{,}62\,\text{ms}$ von $20\,\text{ms}$.

**In Sperrrichtung.** Im Tiefpunkt der negativen Halbwelle liegt die ganze Spannung an der Diode:

$$u_D = -10\,\text{V}.$$

Die Diode muss also $10\,\text{V}$ in Sperrrichtung aushalten; Datenblätter nennen dafür eine höchste zulässige Sperrspannung.

**Im Bild:** Das Ventil öffnet erst bei einem Druck von $0{,}6$ und lässt dann den Rest durch. In der Gegenrichtung lastet der volle Druck von $10$ auf ihm.
::::

Das Skript schreibt die beiden Fälle als $\hat U_E > 0$ und $\hat U_E < 0$. Der Scheitelwert ist aber stets positiv; gemeint ist der Momentanwert
$u_E(t)$, und auch die Achsen seiner Bilder tragen Großbuchstaben, wo nach DIN kleine stehen. Dass nur positive Spannungen einen Strom fließen lassen,
stimmt mit seinen eigenen Bildern nicht ganz: Dort setzt der Strom erst bei $0{,}6\,\text{V}$ ein. Woher diese Schwelle kommt, zeigt der letzte Abschnitt.

:::grafik
Szene: get1/halbleiterbauelemente/01-einweggleichrichter · Vorlage: gleichrichter-zeitverlauf
Links die Schaltung: eine Wechselspannungsquelle mit dem Zählpfeil $u_E$ nach unten, darüber im rechten Zweig der Widerstand $R = 1\,\text{k}\Omega$ mit dem
Zählpfeil $u_A$, darunter die Diode mit der Anode oben und dem Zählpfeil $u_D$; alle Pfeile zeigen nach unten. Rechts drei Zeitverläufe untereinander über
zwei Perioden: $u_E$ als Sinus mit $10\,\text{V}$ Scheitelwert, $u_A$ als positive Halbwellen mit $9{,}4\,\text{V}$ Spitze, die bei $3{,}44^\circ$ einsetzen,
und $u_D$ mit $0{,}6\,\text{V}$ während der Leitphase und der negativen Halbwelle bis $-10\,\text{V}$. Ein Cursor fährt über die Zeit; die Diode leuchtet,
solange sie leitet, und ein Strompfeil erscheint im Widerstand. Ein Regler verändert $U_F$ zwischen $0$ und $1\,\text{V}$ und zeigt, wie Einsatzwinkel und
Spitze wandern. Kernaussage: Die Diode lässt nur die positiven Halbwellen durch, abzüglich ihrer Durchlassspannung. (Rot = Diode und ihr Zustand, blau =
Spannungsverläufe, orange = Strompfeil und Einsatzpunkte, grau = Achsen.)
:::

## Vom Atom zum Kristall: Energiebänder

Ein Elektron in einem Atom kann nicht jede beliebige Energie haben, sondern nur bestimmte, scharf getrennte Werte, die __Energieniveaus__. Der Grund ist
seine Wellennatur. An den Kern gebunden, verhält es sich wie eine stehende Welle, und um den Kern passen nur bestimmte Wellenformen, so wie eine
Gitarrensaite nur ihren Grundton und dessen Obertöne erklingen lässt. Das ist eine Analogie, keine Herleitung; die Rechnung dazu liefert die
Quantenmechanik.

Energien von Elektronen misst man in __Elektronvolt__. Ein Elektronvolt ist die Energie, die ein Elektron gewinnt, wenn es die Spannung $1\,\text{V}$
durchläuft; nach dem Artikel über Arbeit, Potenzial und Spannung ist das Ladung mal Spannung:

$$1\,\text{eV} = e\cdot1\,\text{V} = 1{,}602\cdot10^{-19}\,\text{J}.$$

Rücken viele Atome zu einem Kristall zusammen, überlappen die Elektronenwellen benachbarter Atome; die Atome sind __gekoppelt__. Gekoppelte Schwinger kennt
man aus der Mechanik. Zwei gleiche Pendel, durch eine schwache Feder verbunden, schwingen nicht mehr mit einer gemeinsamen Frequenz, sondern mit zwei
verschiedenen: gleichphasig mit der alten, gegenphasig mit einer etwas höheren. Bei $N$ gekoppelten Pendeln werden es $N$ verschiedene Frequenzen in einem
schmalen Bereich. Ebenso spaltet im Kristall jedes Energieniveau der Atome in $N$ dicht benachbarte Niveaus auf. Ein Kubikzentimeter Silizium enthält
$5\cdot10^{22}$ Atome; ihre Niveaus liegen so dicht, dass sie ein lückenloses __Energieband__ bilden. Zwischen den Bändern bleiben Energiebereiche ohne
jeden Zustand, die __verbotenen Zonen__.

:::herleitung
**Beweisidee: Zählen der Zustände.** Kopplung verschiebt Frequenzen, sie erzeugt und vernichtet aber keine Schwingungsformen: $N$ gekoppelte Pendel haben
genau $N$ Eigenschwingungen, so viele wie die Pendel einzeln. Genauso bringt jedes Atom seine Zustände in den Kristall mit, und aus einem Niveau von $N$
Atomen werden $N$ Niveaus. Wie weit sie auseinanderrücken, hängt von der Stärke der Kopplung ab; bei Halbleitern ergibt das Bänder von einigen
Elektronvolt Breite. Die genaue Rechnung ist Gegenstand der Festkörperphysik.
:::

Die chemische Sicht ergänzt das Bild. Jedes Siliziumatom hat vier __Valenzelektronen__, Elektronen in der äußeren Schale, und bindet sich mit vier
Elektronenpaarbindungen, __kovalenten Bindungen__, an vier Nachbarn. Die Zustände dieser Bindungen bilden ein Band, und weil jede Bindung genau zwei
Elektronen enthält, ist es bei $T = 0\,\text{K}$ restlos voll. Das oberste so besetzte Band heißt __Valenzband__ (VB), das leere darüber
__Leitungsband__ (LB). Ein Elektron im Leitungsband ist eines, das aus seiner Bindung herausgerissen wurde und frei durch den Kristall läuft.

Die Unterkante des Leitungsbands hat die Energie $W_L$, die Oberkante des Valenzbands die Energie $W_V$. Ihr Abstand ist der __Bandabstand__ oder die
__Bandlücke__:

:::formel Definition
$$W_g = W_L - W_V.$$
:::

**So liest man das:** $W_g$ ist die kleinste Energie, die ein Elektron braucht, um vom Valenz- ins Leitungsband zu gelangen; der Index steht für das
englische gap. Energien heißen in der Elektrotechnik nach DIN $W$, weil $E$ die Feldstärke ist. Im __Banddiagramm__, wie in Bild 10.4 des Skripts, steht die
Energie nach oben über dem Ort $x$ im Kristall; in einem gleichmäßigen Kristall sind die Bandkanten waagrechte Linien.

**Im Bild:** Das Unterdeck ist das Valenzband, das Oberdeck das Leitungsband, und $W_g$ ist die Höhe der Rampe.

::::beispiel Welches Licht über die Rampe hilft
Licht gibt seine Energie in Portionen ab, den __Photonen__; ein Photon der Wellenlänge $\lambda$ trägt nach Planck die Energie

$$W_\text{Ph} = \frac{h\,c}{\lambda}, \qquad h\,c = 1240\,\text{eV}\,\text{nm}.$$

Ein Photon kann ein Elektron über die Lücke heben, wenn seine Energie mindestens $W_g$ ist, also bis zur Grenzwellenlänge

$$\lambda_\text{max} = \frac{h\,c}{W_g}.$$

Für Silizium:

$$\lambda_\text{max} = \frac{1240\,\text{eV}\,\text{nm}}{1{,}12\,\text{eV}} = 1107\,\text{nm}.$$

Sichtbares Licht reicht von $380$ bis $780\,\text{nm}$, das sind $3{,}26$ bis $1{,}59\,\text{eV}$. Bandlücken bei Raumtemperatur und was aus ihnen folgt:

| Stoff | $W_g$ | $\lambda_\text{max}$ | Folge |
|---|---|---|---|
| Germanium | $0{,}66\,\text{eV}$ | $1879\,\text{nm}$ | Halbleiter, schluckt sichtbares Licht |
| Silizium | $1{,}12\,\text{eV}$ | $1107\,\text{nm}$ | Halbleiter, schluckt sichtbares Licht: Solarzellen, Kamerasensoren |
| Galliumarsenid | $1{,}42\,\text{eV}$ | $873\,\text{nm}$ | Halbleiter für Infrarot-Leuchtdioden |
| Galliumnitrid | $3{,}4\,\text{eV}$ | $365\,\text{nm}$ | Halbleiter, für sichtbares Licht durchsichtig |
| Diamant | $5{,}47\,\text{eV}$ | $227\,\text{nm}$ | Isolator, durchsichtig |
| Quarzglas | $\approx 9\,\text{eV}$ | $138\,\text{nm}$ | Isolator, durchsichtig |

Silizium sieht deshalb grau und undurchsichtig aus, Glas und Diamant sind klar: Ihr Unterdeck liegt so tief, dass kein sichtbares Photon ein Elektron
hinaufbringt.

**Im Bild:** Ein Photon ist ein einzelner Stoß von bekannter Stärke. Reicht er für die Rampe, fährt ein Auto nach oben; sonst passiert nichts, wie viele
Stöße auch kommen.
::::

:::grafik
Szene: get1/halbleiterbauelemente/01-baender-entstehen · Vorlage: niveaus-zu-baendern
Links ein einzelnes Atom mit zwei scharfen Energieniveaus auf einer senkrechten Energieachse $W$. Ein Regler „Zahl der Atome“ geht von 1 über 2 und 8 bis
„sehr viele“: Bei 2 spaltet jedes Niveau in zwei, bei 8 in acht, bei sehr vielen werden daraus zwei farbige Bänder. Das untere füllt sich mit Elektronen
(Valenzband), das obere bleibt leer (Leitungsband), dazwischen erscheint die Beschriftung $W_g$ zwischen $W_V$ und $W_L$. Daneben zur Erinnerung zwei durch
eine Feder gekoppelte Pendel, die gleichphasig und gegenphasig schwingen. Rechts drei Banddiagramme über dem Ort $x$ wie in Bild 10.4: Metall (oberstes
Band halb gefüllt), Halbleiter (Lücke $1{,}12\,\text{eV}$), Isolator (Lücke $9\,\text{eV}$). Kernaussage: Aus den Niveaus vieler gekoppelter Atome werden
Bänder, und die Lücke zwischen dem vollen und dem leeren Band entscheidet über das Verhalten. (Blau = Elektronen, rot = Bandkanten und $W_g$, orange =
Aufspaltung, grau = Achsen.)
:::

## Leiter, Halbleiter, Isolator

Ob ein Stoff leitet, entscheidet nicht die Zahl seiner Elektronen, sondern ob sie freie Zustände in ihrer Nähe haben. Nach dem __Pauli-Prinzip__ kann jeder
Zustand höchstens ein Elektron aufnehmen, die beiden Spinrichtungen als zwei Zustände gezählt. Ein Strom heißt: In eine Richtung bewegen sich mehr Elektronen
als in die Gegenrichtung. Dafür müsste ein Feld Elektronen in Zustände mit etwas mehr Geschwindigkeit in seiner Richtung schieben, und diese Zustände müssen
frei sein.

In einem vollen Band ist kein Zustand frei. Zu jedem Zustand mit der Geschwindigkeit $\vec v_k$ gehört einer mit $-\vec v_k$, beide besetzt, und ihre
Beiträge heben sich auf. Mit dem Volumen $V$ des Kristalls und der Summe über alle Zustände $k$ des Bandes ist die Stromdichte, wie im Artikel über den
Strom Ladung mal Geschwindigkeit je Volumen:

$$\vec J_\text{voll} = -\frac{e}{V}\sum_k \vec v_k = \vec 0.$$

Ein leeres Band trägt ebenfalls keinen Strom, denn es hat keine Elektronen. Leiten können nur Bänder, die teilweise gefüllt sind.

:::herleitung
**Paare entgegengesetzter Geschwindigkeit.** Ohne Magnetfeld ist jede Bewegung auch rückwärts abgespielt eine erlaubte Bewegung, mit derselben Energie.
Deshalb gehört zu jedem Zustand des Bandes einer mit der umgekehrten Geschwindigkeit. In einem vollen Band sind beide besetzt, und in der Summe hebt sich
jedes Paar auf.

**Das Feld ändert daran nichts.** Ein Feld könnte die Summe nur verändern, indem es Elektronen in andere Zustände bringt. Im vollen Band sind alle schon
besetzt, und nach dem Pauli-Prinzip nimmt keiner ein zweites Elektron auf; die Besetzung bleibt, wie sie ist, und die Summe null. Im Bild: Auf einem
zugeparkten Deck kann kein Auto anfahren, wie kräftig man auch schiebt.
:::

Damit unterscheiden sich die drei Stoffklassen so:

- **Metalle.** Ihr oberstes besetztes Band ist nur teilweise gefüllt, oder zwei Bänder überlappen; direkt über den besetzten Zuständen liegen freie. Metalle
  leiten deshalb schon am absoluten Nullpunkt. Das Skript fasst das so zusammen, als fehle die Lücke und lägen Valenz- und Leitungsband direkt aneinander.
- **Isolatoren.** Das Valenzband ist voll, das Leitungsband leer, dazwischen liegt eine Lücke von mehreren Elektronvolt. Wärme hebt so gut wie kein Elektron
  hinüber.
- **Halbleiter.** Am absoluten Nullpunkt sind sie ebenfalls Isolatoren, wie das Skript sagt, aber mit einer Lücke um ein Elektronvolt. Bei Raumtemperatur
  schafft es ein winziger Teil der Elektronen ins Leitungsband, und mit der Temperatur werden es sehr schnell mehr: Reine Halbleiter sind Heißleiter, wie im
  Artikel über den ohmschen Widerstand.

Wie winzig dieser Teil ist und wie schnell er wächst, rechnen die Abschnitte über das Fermi-Niveau und die Eigenleitung aus.

**Im Bild:** Ein Metall ist ein Parkhaus mit einem halbvollen Deck, ein Isolator eines mit einer unüberwindlichen Rampe, ein Halbleiter eines mit einer
niedrigen Rampe, über die das Rütteln gelegentlich ein Auto bringt.

## Elektronen und Löcher

Hebt die Wärme ein Elektron ins Leitungsband, entstehen zwei bewegliche Ladungsträger zugleich: das Elektron oben und die leere Stelle, die es im
Valenzband zurücklässt. Diese Leerstelle heißt __Loch__ oder __Defektelektron__. Das Skript sagt, im Valenzband blieben positive Ladungen zurück. Warum sich
ein fehlendes Elektron wie eine positive Ladung bewegt, zeigt die Rechnung von eben, mit einem einzigen freien Platz; $\vec v_0$ sei die Geschwindigkeit,
die zum leeren Zustand gehört:

:::formel Satz
$$\vec J_\text{Loch} = +\frac{e}{V}\,\vec v_0.$$
:::

**So liest man das:** Ein Valenzband mit einem freien Platz trägt genau den Strom einer positiven Ladung $+e$, die sich mit der Geschwindigkeit $\vec v_0$
des fehlenden Elektrons bewegt. Statt die vielen Elektronen des Bandes zu verfolgen, verfolgt man das eine Loch. Im Halbleiter gibt es damit zwei Sorten
beweglicher Ladungsträger: Elektronen im Leitungsband mit der Ladung $-e$ und Löcher im Valenzband mit $+e$. Das Skript sagt zuerst, nur Elektronen im
Leitungsband trügen zur Leitfähigkeit bei, und nennt die Löcher erst danach; beide zählen.

**Im Bild:** Rückt im Unterdeck ein Auto nach dem anderen um einen Platz nach links in die Lücke, wandert die Lücke Platz für Platz nach rechts. Statt vieler
Autos, die je ein kleines Stück fahren, sieht man eine Lücke, die weit fährt.

:::herleitung
**Das volle Band minus ein Elektron.** Im Band mit einem freien Platz fehlt in der Summe genau der Beitrag des leeren Zustands, und die Summe über alle
Zustände ist nach dem vorigen Abschnitt null:

$$\vec J_\text{Loch} = -\frac{e}{V}\Big(\sum_k \vec v_k - \vec v_0\Big) = -\frac{e}{V}\,\big(\vec 0 - \vec v_0\big) = +\frac{e}{V}\,\vec v_0.$$

**Deutung.** Das ist die Stromdichte, die eine einzige Ladung $+e$ mit der Geschwindigkeit $\vec v_0$ im Volumen $V$ erzeugte. Im Feld laufen die
Valenzelektronen gegen das Feld, das Loch also mit dem Feld, wie es eine positive Ladung täte. Im Bild: Die Autos rücken zum Pluspol, die Lücke wandert zum
Minuspol.
:::

Für die Leitfähigkeit übernimmt man die Formel aus dem Artikel über den ohmschen Widerstand für jede Trägersorte. Mit den __Trägerdichten__ $n$ der
Elektronen und $p$ der Löcher, jeweils Zahl pro Volumen, und ihren __Beweglichkeiten__ $\mu_n$ und $\mu_p$ ist

$$\sigma = e\,(n\,\mu_n + p\,\mu_p).$$

**So liest man das:** Beide Trägersorten tragen Strom in Richtung des Feldes: die Elektronen, weil sie negativ sind und gegen das Feld laufen, die Löcher,
weil sie positiv sind und mit ihm laufen. Löcher sind in Silizium nur etwa ein Drittel so beweglich wie Elektronen; anschaulich, weil ihre Bewegung aus
vielen Platzwechseln gebundener Elektronen besteht, in der Festkörperphysik beschrieben durch eine größere wirksame Masse der Löcher.

:::herleitung
**Eine Trägersorte.** Nach dem Artikel über den ohmschen Widerstand ist die Leitfähigkeit der Elektronen Elementarladung mal Trägerdichte mal
Beweglichkeit; die Elektronen driften gegen das Feld, ihr Strom zeigt mit dem Feld:

$$\vec J_n = e\,n\,\mu_n\,\vec E.$$

**Die Löcher.** Sie tragen $+e$ und driften mit dem Feld, mit ihrer eigenen Beweglichkeit; auch ihr Strom zeigt mit dem Feld:

$$\vec J_p = e\,p\,\mu_p\,\vec E.$$

**Zusammen.** Die Stromdichten addieren sich, und der Faktor vor $\vec E$ ist die Leitfähigkeit. Im Bild: Autos oben und Lücken unten fahren in
entgegengesetzte Richtungen und tragen doch beide zum Strom in derselben Richtung bei.
:::

::::beispiel Wie gut reines Silizium leitet
In reinem Silizium bei $300\,\text{K}$ gibt es nach Messungen je Kubikzentimeter rund $10^{10}$ Elektronen im Leitungsband und ebenso viele Löcher; woher
diese Zahl kommt, zeigt der Abschnitt über die Eigenleitung. Dazu die Beweglichkeiten in reinem Silizium:

$$n = p = 1\cdot10^{10}\,\text{cm}^{-3}, \qquad \mu_n = 1350\,\frac{\text{cm}^2}{\text{V}\,\text{s}}, \qquad \mu_p = 480\,\frac{\text{cm}^2}{\text{V}\,\text{s}}.$$

**Die Leitfähigkeit.** Mit $1350 + 480 = 1830$ in der Klammer:

$$\sigma_i = 1{,}602\cdot10^{-19}\,\text{C}\cdot10^{10}\,\text{cm}^{-3}\cdot1830\,\frac{\text{cm}^2}{\text{V}\,\text{s}} = 2{,}93\cdot10^{-6}\,\frac{\text{S}}{\text{cm}}.$$

Der spezifische Widerstand ist ihr Kehrwert:

$$\rho_i = \frac{1}{\sigma_i} = 3{,}4\cdot10^{5}\,\Omega\,\text{cm}.$$

Die Löcher tragen davon $480$ von $1830$ Teilen, gut ein Viertel.

**Zum Vergleich.** Kupfer hat $1{,}7\cdot10^{-6}\,\Omega\,\text{cm}$; reines Silizium leitet rund $2\cdot10^{11}$-mal schlechter. Ein Würfel aus reinem
Silizium mit $1\,\text{cm}$ Kantenlänge hat zwischen zwei gegenüberliegenden Flächen $340\,\text{k}\Omega$.

**Im Bild:** Auf jedes Auto, das oben fährt, kommen $5\cdot10^{12}$ Siliziumatome; die Lücke unten fährt nur etwa ein Drittel so schnell wie das Auto.
::::

## Das Fermi-Niveau

Wie viele Elektronen es über die Lücke schaffen, regelt die Temperatur über die __Fermi-Verteilung__. Sie gibt für jeden Zustand der Energie $W$ die
Wahrscheinlichkeit an, dass er besetzt ist. Darin stehen die absolute Temperatur $T$ in Kelvin, die __Boltzmann-Konstante__ $k_B$ und das
__Fermi-Niveau__ $W_F$, auch Fermi-Energie:

$$k_B = 1{,}381\cdot10^{-23}\,\frac{\text{J}}{\text{K}} = 8{,}617\cdot10^{-5}\,\frac{\text{eV}}{\text{K}}.$$

Bei $300\,\text{K}$ ist $k_BT = 25{,}9\,\text{meV}$, die typische Energie der Wärmebewegung.

:::formel Gesetz
$$f(W) = \frac{1}{1 + \exp\dfrac{W - W_F}{k_B\,T}}.$$
:::

**So liest man das:** Eingabe ist eine Energie, Ausgabe eine Zahl zwischen 0 und 1, die Besetzungswahrscheinlichkeit. Bei $W = W_F$ ist sie genau
$\tfrac12$: Das Fermi-Niveau ist die Energie, bei der ein Zustand, gäbe es dort einen, mit der Wahrscheinlichkeit $\tfrac12$ besetzt wäre. Darunter sind
Zustände fast sicher besetzt, darüber fast sicher leer; der Übergang ist einige $k_BT$ breit. Am absoluten Nullpunkt wird er zur Stufe: alle Zustände unter
$W_F$ voll, alle darüber leer. Das ist die Aussage des Skripts, das Fermi-Niveau sei die Grenze, bis zu der bei $T = 0\,\text{K}$ Zustände besetzt sind. Wo
$W_F$ genau liegt, legt die Zahl der Elektronen fest: so, dass die Besetzungen aller Zustände zusammen sie ergeben.

**Ein Rätsel des Skripts.** Beim reinen Halbleiter, sagt das Skript, liege das Fermi-Niveau in der Mitte der Bandlücke, obwohl es dort keine Zustände gibt.
Das ist kein Widerspruch: $W_F$ ist kein Zustand, sondern eine Kenngröße der Verteilung. Liegt es in der Mitte, ist die Besetzung an der Unterkante des
Leitungsbands genauso klein wie die Leere an der Oberkante des Valenzbands, passend dazu, dass ein reiner Halbleiter gleich viele Elektronen und Löcher hat;
der Abschnitt über die Eigenleitung rechnet das nach. Bei $T = 0\,\text{K}$ wäre jede Lage in der Lücke mit der Stufe verträglich, erst die Temperatur legt
sie fest.

**Im Bild:** Das Fermi-Niveau ist die Höhe, bis zu der das Parkhaus zur Hälfte gefüllt ist: tief darunter ist jeder Platz belegt, hoch darüber jeder frei.
Beim Halbleiter liegt diese Höhe mitten auf der Rampe, wo es keine Plätze gibt.

:::herleitung
**Beweisidee.** Nach dem Pauli-Prinzip ist ein Zustand entweder leer oder mit einem Elektron besetzt. Die statistische Physik sagt: Im Wärmegleichgewicht ist
ein Zustand, dessen Besetzung gegenüber dem Fermi-Niveau die Energie $W - W_F$ kostet, um den __Boltzmann-Faktor__ seltener besetzt als leer:

$$\frac{f}{1 - f} = \exp\Big(-\frac{W - W_F}{k_B\,T}\Big).$$

Nach $f$ aufgelöst ergibt das die Fermi-Verteilung. Den Boltzmann-Faktor kennt man von der Luft: Ein Molekül in größerer Höhe hat mehr Lageenergie, und die
Luftdichte nimmt mit der Höhe nach demselben Exponentialgesetz ab, der barometrischen Höhenformel. Die vollständige Begründung liefert die statistische
Physik.

**Die Stufe bei null Kelvin.** Geht $T$ gegen null, geht der Exponent gegen plus unendlich, wenn $W$ über $W_F$ liegt, und gegen minus unendlich, wenn es
darunter liegt; der Bruch geht dann gegen 0 beziehungsweise 1. Im Bild: Ohne Rütteln steht jedes Auto so tief wie möglich, das Haus ist bis zur Füllhöhe voll
und darüber leer.
:::

Liegt eine Energie viele $k_BT$ über dem Fermi-Niveau, wird die Eins im Nenner unwichtig, und die Fermi-Verteilung geht in den Boltzmann-Faktor über;
ebenso die Leere eines Zustands viele $k_BT$ unter dem Fermi-Niveau:

$$f(W) \approx \exp\Big(-\frac{W - W_F}{k_B\,T}\Big), \qquad 1 - f(W) \approx \exp\Big(-\frac{W_F - W}{k_B\,T}\Big).$$

:::herleitung
**Über dem Fermi-Niveau.** Mit der Abkürzung $x$ für $(W - W_F)/(k_BT)$ ist die Besetzung ein Bruch, dessen Nenner für großes $x$ fast nur aus $e^x$
besteht:

$$f = \frac{1}{1 + e^x} \approx e^{-x}.$$

**Unter dem Fermi-Niveau.** Die Leere ist eins minus die Besetzung; für stark negatives $x$ ist $e^x$ winzig:

$$1 - f = \frac{e^x}{1 + e^x} \approx e^{x}.$$

Das ist der Boltzmann-Faktor des Abstands $W_F - W$. Im Bild: Ein Platz hoch über der Füllhöhe ist so selten belegt, wie ein Auto selten so hoch geschleudert
wird.
:::

::::beispiel Besetzung bei Raumtemperatur
Reines Silizium bei $300\,\text{K}$, das Fermi-Niveau in der Mitte der Lücke, also eine halbe Bandlücke unter der Leitungsbandkante:

$$k_BT = 0{,}0259\,\text{eV}, \qquad W_L - W_F = 0{,}56\,\text{eV}.$$

**An der Leitungsbandkante.** Der Exponent ist $0{,}56$ geteilt durch $0{,}0259$, also $21{,}7$:

$$f(W_L) = \frac{1}{1 + e^{21{,}7}} = 3{,}9\cdot10^{-10}.$$

Die Boltzmann-Näherung $e^{-21{,}7}$ ergibt denselben Wert. Von zehn Milliarden Zuständen an der Unterkante sind also rund vier besetzt, und an der
Oberkante des Valenzbands sind ebenso wenige leer.

**Nahe am Fermi-Niveau.** Drei $k_BT$ darüber und darunter:

$$f(W_F + 3\,k_BT) = 0{,}047, \qquad f(W_F - 3\,k_BT) = 0{,}953.$$

Hier liegt die Boltzmann-Näherung mit $e^{-3} = 0{,}050$ schon $5\,\%$ daneben; sie taugt nur weit weg vom Fermi-Niveau. Der Übergang von voll zu leer ist also
nur einige $k_BT$ breit, gut $0{,}1\,\text{eV}$, die Lücke aber $1{,}12\,\text{eV}$.

**Im Bild:** Die Rampe ist $43$-mal so hoch wie ein typischer Stoß. Weil die Füllhöhe auf halber Rampe liegt, zählt nur die halbe Höhe, und trotzdem kommt nur
eines von zweieinhalb Milliarden Autos oben an.
::::

## Eigenleitung: wie viele Ladungsträger

Wie viele Elektronen im Leitungsband sind, ergibt sich aus der Besetzungswahrscheinlichkeit und der Zahl der Zustände. Weil die Besetzung über der Bandkante
nach dem Boltzmann-Faktor schnell abfällt, zählen nur Zustände knapp über $W_L$. Man fasst sie zu einer __effektiven Zustandsdichte__ $N_L$ zusammen: so
viele Zustände je Volumen, als säßen sie alle an der Kante. Ebenso für die Löcher mit $N_V$ an der Valenzbandkante. Für Silizium bei $300\,\text{K}$ sind das
$2{,}8\cdot10^{19}$ und $1{,}0\cdot10^{19}$ je Kubikzentimeter, und beide wachsen mit $T^{3/2}$. Damit gilt, solange das Fermi-Niveau einige $k_BT$ von beiden
Bandkanten entfernt ist:

$$n = N_L\,\exp\Big(-\frac{W_L - W_F}{k_B\,T}\Big), \qquad p = N_V\,\exp\Big(-\frac{W_F - W_V}{k_B\,T}\Big).$$

:::herleitung
**Beweisidee.** Die Elektronendichte ist die Summe der Besetzungswahrscheinlichkeiten aller Zustände des Leitungsbands, je Volumen. In jedem steckt nach der
Boltzmann-Näherung der Faktor seines Abstands von $W_F$; man zerlegt ihn in den Abstand der Kante und den Abstand über der Kante:

$$\begin{aligned} \exp\Big(-\frac{W - W_F}{k_B\,T}\Big) &= \exp\Big(-\frac{W_L - W_F}{k_B\,T}\Big) \\ &\quad\cdot\exp\Big(-\frac{W - W_L}{k_B\,T}\Big). \end{aligned}$$

Der erste Faktor ist für alle Zustände gleich und kommt vor die Summe. Die Summe der zweiten Faktoren über alle Zustände je Volumen ist eine Materialgröße,
eben $N_L$; wie sie mit der Temperatur wächst, folgt aus der Zahl der Zustände je Energie, die die Festkörperphysik ausrechnet. Für die Löcher gilt dasselbe
mit der Leere. Im Bild: Was oben ankommt, ist die Zahl der Plätze knapp über der Rampe mal dem Faktor für ihre Höhe.
:::

Multipliziert man beide Dichten, fällt das Fermi-Niveau heraus. Das ist das __Massenwirkungsgesetz__ der Halbleiter, mit der __Eigenleitungsdichte__
$n_i$:

:::formel Satz
$$n\,p = n_i^2, \qquad n_i = \sqrt{N_L\,N_V}\,\exp\Big(-\frac{W_g}{2\,k_B\,T}\Big).$$
:::

**So liest man das:** Das Produkt aus Elektronen- und Löcherdichte hängt nur vom Material und der Temperatur ab, nicht von der Lage des Fermi-Niveaus und
damit, wie der nächste Abschnitt zeigt, auch nicht von der Dotierung. Im reinen Halbleiter sind beide gleich der Eigenleitungsdichte; diese Leitung heißt
__Eigenleitung__. Der Name stammt aus der Chemie: Wärme erzeugt laufend Elektron-Loch-Paare, die __Generation__, und Elektronen fallen in Löcher zurück, die
__Rekombination__. Im Gleichgewicht sind beide gleich schnell, und das Produkt der Dichten liegt fest. Der Exponent enthält nur die halbe Lücke, weil
Elektron und Loch je eine halbe Lücke vom Fermi-Niveau entfernt sind; gegen ihn fällt der Faktor $T^{3/2}$ kaum ins Gewicht.

**Im Bild:** Autos oben mal Lücken unten ergibt eine Zahl, die allein das Rütteln festlegt. Kommen von irgendwoher zusätzliche Autos aufs Oberdeck, fallen mehr
von ihnen in Lücken zurück, bis das Produkt wieder stimmt.

:::herleitung
**Das Produkt.** Multipliziert man $n$ und $p$, addieren sich die Exponenten, und $W_F$ fällt heraus:

$$\begin{aligned} n\,p &= N_L\,N_V\,\exp\Big(-\frac{(W_L - W_F) + (W_F - W_V)}{k_B\,T}\Big) \\ &= N_L\,N_V\,\exp\Big(-\frac{W_g}{k_B\,T}\Big). \end{aligned}$$

**Die Eigenleitungsdichte.** Im reinen Halbleiter entsteht jedes Elektron zusammen mit einem Loch, also ist $n$ gleich $p$; beide heißen dann $n_i$, und ihr
Produkt ist $n_i^2$. Weil das Produkt nicht von $W_F$ abhängt, ist es für jedes Stück aus demselben Material bei derselben Temperatur gleich, auch für ein
dotiertes. Die Wurzel ergibt $n_i$ mit dem halben Exponenten.

**Das Fermi-Niveau des reinen Halbleiters.** Setzt man $n$ gleich $p$ und löst nach $W_F$ auf, ergibt sich:

$$W_F = \frac{W_L + W_V}{2} + \frac{k_B\,T}{2}\,\ln\frac{N_V}{N_L}.$$

Für Silizium ist der zweite Term $-13\,\text{meV}$: Das Fermi-Niveau liegt knapp unter der Mitte, wie das Skript sagt. Im Bild: Die Füllhöhe steht fast genau
auf halber Rampe.
:::

::::beispiel Eigenleitung und Temperatur
**(a) Wie selten.** Reines Silizium bei $300\,\text{K}$ hat rund $10^{10}$ freie Elektronen je Kubikzentimeter, bei $5\cdot10^{22}$ Atomen:

$$\frac{5\cdot10^{22}\,\text{cm}^{-3}}{10^{10}\,\text{cm}^{-3}} = 5\cdot10^{12}.$$

Auf fünf Billionen Atome kommt ein freies Elektron.

**(b) Wie schnell es mit der Wärme wächst.** Von $300$ auf $350\,\text{K}$, mit festem $W_g = 1{,}12\,\text{eV}$. Der Faktor $T^{3/2}$ bringt $1{,}26$; der
Exponent wächst um

$$\frac{W_g}{2\,k_B}\Big(\frac{1}{300\,\text{K}} - \frac{1}{350\,\text{K}}\Big) = 6499\,\text{K}\cdot4{,}76\cdot10^{-4}\,\text{K}^{-1} = 3{,}09,$$

und $e^{3{,}09}$ ist $22{,}1$. Zusammen:

$$\frac{n_i(350\,\text{K})}{n_i(300\,\text{K})} = 1{,}26\cdot22{,}1 = 27{,}8.$$

Fünfzig Grad mehr ergeben fast dreißigmal so viele Ladungsträger; darum sind reine Halbleiter Heißleiter. In Wirklichkeit wird $W_g$ mit der Wärme noch etwas
kleiner, und der Anstieg fällt steiler aus.

**(c) Ein Isolator.** Für Quarzglas mit $W_g \approx 9\,\text{eV}$ steht im Massenwirkungsgesetz statt $e^{-21{,}7}$ wie bei Silizium:

$$\exp\Big(-\frac{9\,\text{eV}}{2\cdot0{,}0259\,\text{eV}}\Big) = 2{,}5\cdot10^{-76}.$$

Selbst mit $10^{19}$ Zuständen je Kubikzentimeter bleibt nichts, was man noch als Ladungsträger zählen könnte.

**Im Bild:** Eine Rampe, die nur achtmal so hoch ist, verringert den Verkehr nicht achtmal, sondern um 66 Zehnerpotenzen, denn der Faktor ist exponentiell.
::::

:::grafik
Szene: get1/halbleiterbauelemente/01-fermi-verteilung · Vorlage: fermi-banddiagramm
Links das Banddiagramm von reinem Silizium: Energie $W$ nach oben über dem Ort $x$, Valenzband und Leitungsband als graue Flächen, $W_V$, $W_L$ und die
Lücke $W_g = 1{,}12\,\text{eV}$ beschriftet, $W_F$ gestrichelt knapp unter der Mitte. Rechts mit derselben senkrechten Energieachse die Fermi-Verteilung
$f(W)$, waagrecht von 0 bis 1 aufgetragen. Ein Regler für die Temperatur von $0$ bis $600\,\text{K}$: bei $0\,\text{K}$ eine scharfe Stufe bei $W_F$, bei
höheren Temperaturen ein Übergang von einigen $k_BT$ Breite. An den Bandkanten zeigen zwei Lupen die winzigen Ausläufer: wenige besetzte Zustände im
Leitungsband als Punkte und ebenso viele leere im Valenzband als Kreise, mit den Dichten $n$ und $p$ als Zahlen, die mit der Temperatur steigen; ihr Produkt
wird angezeigt und hängt nur von der Temperatur ab. Kernaussage: Die Fermi-Verteilung legt fest, wie viele Zustände über und unter der Lücke besetzt
beziehungsweise leer sind, und diese winzigen Ausläufer sind die Ladungsträger. (Blau = Elektronen, rot = Löcher, orange = Fermi-Verteilung und
Temperaturregler, grau = Bänder und Achsen, gestrichelt = Fermi-Niveau.)
:::

## Dotierung

Die Eigenleitung ist schwach und hängt stark von der Temperatur ab; für Bauteile taugt sie so nicht. Die __Dotierung__ ändert das: Man baut gezielt
Fremdatome in den Kristall ein, jedes an den Platz eines Siliziumatoms, und bestimmt über ihre Zahl die Leitfähigkeit. Das Skript nennt Silizium dabei ein
Halbmetall. Das ist der Sprachgebrauch der Chemie für Elemente zwischen Metallen und Nichtmetallen; in der Festkörperphysik ist ein Halbmetall etwas anderes,
ein Stoff mit leicht überlappenden Bändern wie Bismut. Silizium ist ein Halbleiter.

**n-Dotierung.** Ein Phosphoratom hat fünf Valenzelektronen. Vier davon bilden die vier kovalenten Bindungen zu den Siliziumnachbarn; das Skript schreibt
„kohärente Bindung“, gemeint ist die kovalente. Das fünfte Elektron findet in keiner Bindung Platz. Es bleibt nur schwach an den Phosphorkern gebunden, mit
rund $45\,\text{meV}$, und schon die Wärme bei Raumtemperatur löst es: Es wird ein freies Elektron im Leitungsband. Zurück bleibt ein ortsfestes, positiv
geladenes Phosphor-Ion. Weil das Fremdatom ein Elektron spendet, heißt es __Donator__. Im Banddiagramm sitzt sein fünftes Elektron, solange es gebunden ist,
auf dem __Donatorniveau__ $W_D$ knapp unter $W_L$, wie in Bild 10.5 des Skripts; dort heißt es Niveau der ungebundenen Elektronen, gemeint sind die schwach
gebundenen.

**p-Dotierung.** Ein Boratom hat nur drei Valenzelektronen. Es bildet drei vollständige Bindungen, der vierten zu einem Siliziumnachbarn fehlt ein Elektron.
Schon wenig Wärme, wieder rund $45\,\text{meV}$, genügt, damit ein Elektron aus einer benachbarten Silizium-Silizium-Bindung in diese Lücke springt. Dann hat
das Bor vier Bindungen und ist ein ortsfestes, negativ geladenes Ion, und in der Bindung, aus der das Elektron kam, fehlt eines: ein Loch im Valenzband, das
durch den Kristall wandern kann. Weil das Fremdatom ein Elektron aufnimmt, heißt es __Akzeptor__; sein __Akzeptorniveau__ $W_A$ liegt knapp über $W_V$. Das
Skript verkürzt den Vorgang: Das Elektron, das die Bindung vervollständigt, kommt aus einer Nachbarbindung, und das Loch gehört zum Valenzband des ganzen
Kristalls, nicht zu einem einzelnen Siliziumatom.

**Majoritäts- und Minoritätsträger.** Im n-dotierten Halbleiter sind die Elektronen in der Mehrheit, die __Majoritätsträger__; die Löcher sind die
__Minoritätsträger__. Im p-dotierten ist es umgekehrt. Mit der __Donatordichte__ $N_D$, der Zahl der Donatoren pro Volumen, gilt bei Raumtemperatur, solange
$N_D$ viel größer als $n_i$ ist:

:::formel
$$n \approx N_D, \qquad p \approx \frac{n_i^2}{N_D}.$$
:::

**So liest man das:** Jeder Donator liefert ein Elektron, und die wenigen Elektronen der Eigenleitung fallen daneben nicht ins Gewicht. Die Löcher werden
dabei weniger als im reinen Halbleiter: Die vielen Elektronen füllen Löcher auf, bis das Massenwirkungsgesetz wieder gilt. Bei p-Dotierung mit der
__Akzeptordichte__ $N_A$ gilt dasselbe mit vertauschten Rollen: Die Löcherdichte ist $N_A$, die Elektronendichte $n_i^2/N_A$.

Dotiertes Silizium ist im üblichen Temperaturbereich deshalb kein Heißleiter mehr, wie der Artikel über den ohmschen Widerstand vorweggenommen hat: Die
Trägerdichte liegt durch die Fremdatome fest, während die Beweglichkeit mit der Wärme sinkt. Erst bei einigen hundert Grad Celsius wächst $n_i$ bis an $N_D$
heran, und die Eigenleitung übernimmt wieder.

**Im Bild:** Bei n-Dotierung warten zusätzliche Autos auf kleinen Plattformen knapp unter dem Oberdeck; schon leichtes Rütteln hebt sie hinauf, und die
leeren Plattformen bleiben als positive Ladung zurück. Bei p-Dotierung gibt es freie Plätze auf Plattformen knapp über dem Unterdeck; Autos aus dem
Unterdeck hüpfen hinein und hinterlassen unten Lücken.

:::herleitung
**Neutralität.** Der Kristall als Ganzes ist ungeladen. Sind alle Donatoren ionisiert, stehen den Elektronen die Löcher und die positiven Donator-Ionen
gegenüber:

$$n = p + N_D.$$

**Mit dem Massenwirkungsgesetz.** Setzt man für $p$ den Bruch $n_i^2/n$ ein, entsteht eine quadratische Gleichung für $n$; ihre positive Lösung ist

$$n = \frac{N_D}{2} + \sqrt{\frac{N_D^2}{4} + n_i^2}.$$

Ist $N_D$ viel größer als $n_i$, ist die Wurzel fast $N_D/2$ und $n$ fast $N_D$; $p$ folgt aus dem Massenwirkungsgesetz. Im Bild: Die vielen Autos von den
Plattformen fahren oben, und unten bleiben nur so wenige Lücken, wie das Produkt erlaubt.

**Fast alle Donatoren sind ionisiert.** Das folgt aus der Lage des Fermi-Niveaus, die das Beispiel unten ausrechnet: Es liegt deutlich unter $W_D$, und nach
der Fermi-Verteilung ist das Donatorniveau dann fast leer.
:::

Mit den Trägern wandert das Fermi-Niveau. Es sei $W_i$ das Fermi-Niveau des reinen Halbleiters, fast genau die Mitte der Lücke. Aus den Formeln für $n$ und
$n_i$ folgt:

$$W_F - W_i = k_B\,T\,\ln\frac{n}{n_i}.$$

**So liest man das:** Mehr Elektronen schieben $W_F$ zum Leitungsband hin, je Verzehnfachung von $n$ um $k_BT\ln10$, also um $60\,\text{meV}$. Bei
p-Dotierung rückt es ebenso zum Valenzband, um $k_BT\ln(p/n_i)$ unter $W_i$. Das Skript sagt für n-Dotierung dasselbe: Das Fermi-Niveau verschiebt sich nach
oben. Im Bild: Mehr Autos im Haus heben die Füllhöhe.

:::herleitung
Für den reinen Halbleiter ist $n$ gleich $n_i$ und $W_F$ gleich $W_i$. Teilt man die Formel für $n$ durch dieselbe Formel mit diesen Werten, kürzt sich
$N_L$ heraus, ebenso $W_L$:

$$\frac{n}{n_i} = \exp\Big(\frac{W_F - W_i}{k_B\,T}\Big).$$

Logarithmieren ergibt die Formel; für die Löcher geht es ebenso mit der Formel für $p$. Im Bild: Jede Verzehnfachung der Autos oben verlangt dieselbe
zusätzliche Füllhöhe.
:::

::::beispiel Silizium mit einer Prise Phosphor
Silizium mit Phosphor bei $300\,\text{K}$, die Beweglichkeit wie im reinen Silizium:

$$N_D = 10^{16}\,\text{cm}^{-3}, \qquad n_i = 10^{10}\,\text{cm}^{-3}, \qquad \mu_n = 1350\,\frac{\text{cm}^2}{\text{V}\,\text{s}}.$$

**Wie wenig.** Auf $5\cdot10^{22}$ Siliziumatome kommen $10^{16}$ Phosphoratome, eines auf fünf Millionen.

**Die Träger.**

$$n = 10^{16}\,\text{cm}^{-3}, \qquad p = \frac{(10^{10}\,\text{cm}^{-3})^2}{10^{16}\,\text{cm}^{-3}} = 10^{4}\,\text{cm}^{-3}.$$

Auf eine Billion Elektronen kommt ein Loch.

**Die Leitfähigkeit.** Die Löcher fallen weg:

$$\sigma = 1{,}602\cdot10^{-19}\,\text{C}\cdot10^{16}\,\text{cm}^{-3}\cdot1350\,\frac{\text{cm}^2}{\text{V}\,\text{s}} = 2{,}16\,\frac{\text{S}}{\text{cm}}, \qquad \rho = 0{,}46\,\Omega\,\text{cm}.$$

Das ist das $7{,}4\cdot10^{5}$-Fache der Leitfähigkeit von reinem Silizium. Die Fremdatome stören die Elektronen etwas; bei dieser Dotierung sinkt die
Beweglichkeit auf rund $1200\,\frac{\text{cm}^2}{\text{V}\,\text{s}}$, und gemessen sind es etwa $0{,}5\,\Omega\,\text{cm}$.

**Das Fermi-Niveau.**

$$W_F - W_i = 0{,}0259\,\text{eV}\cdot\ln10^{6} = 0{,}357\,\text{eV}.$$

Mit $W_i$ in der Mitte, $0{,}56\,\text{eV}$ unter $W_L$, liegt $W_F$ also $0{,}20\,\text{eV}$ unter der Leitungsbandkante und $0{,}16\,\text{eV}$ unter dem
Donatorniveau. Nach der Fermi-Verteilung ist das Donatorniveau damit zu weniger als einem Prozent besetzt: Fast alle Donatoren haben ihr Elektron abgegeben,
wie angenommen. Bild 10.5 des Skripts zeichnet $W_F$ zwischen $W_D$ und $W_L$; dort liegt es nur bei tiefer Temperatur, solange die Donatoren ihre
Elektronen noch festhalten.

**Im Bild:** Eine Prise zusätzlicher Autos, eines auf fünf Millionen Plätze, steht bereit. Das Rütteln hebt sie fast alle aufs Oberdeck, und die Füllhöhe
steigt bis $0{,}2\,\text{eV}$ unter das Oberdeck.
::::

:::grafik
Szene: get1/halbleiterbauelemente/01-dotierung · Vorlage: dotierung-gitter-band
Oben zwei ebene Ausschnitte des Siliziumgitters, jedes Atom mit vier Bindungsstrichen zu seinen Nachbarn und je zwei Elektronen pro Bindung. Links ein
Phosphoratom mit einem fünften Elektron, das lose um es kreist; auf den Knopf „Wärme“ löst es sich und wandert davon, und am Phosphor erscheint ein Plus.
Rechts ein Boratom, dessen vierter Bindung ein Elektron fehlt; auf „Wärme“ springt ein Elektron aus einer Nachbarbindung hinein, am Bor erscheint ein Minus,
und die leere Stelle wandert als Loch durch das Gitter. Darunter die Banddiagramme: links das Donatorniveau $W_D$ knapp unter $W_L$, dessen Elektronen bei
Erwärmung ins Leitungsband steigen, und $W_F$, das bei $300\,\text{K}$ und $10^{16}\,\text{cm}^{-3}$ auf $0{,}20\,\text{eV}$ unter $W_L$ steht; rechts das
Akzeptorniveau $W_A$ knapp über $W_V$, das Elektronen aus dem Valenzband aufnimmt, und $W_F$ entsprechend unten. Ein Regler für die Dotierdichte von
$10^{14}$ bis $10^{18}\,\text{cm}^{-3}$ verschiebt $W_F$ und zeigt $n$ und $p$ als Zahlen. Kernaussage: Donatoren spenden Elektronen ins Leitungsband,
Akzeptoren nehmen Elektronen aus dem Valenzband auf und erzeugen Löcher; die Dotierdichte stellt Träger und Fermi-Niveau ein. (Rot = Fremdatome und ihre
Ionenladung, blau = Elektronen und Löcher, orange = Wärmeanstoß und Fermi-Niveau, grau = Gitter und Bänder.)
:::

## Der pn-Übergang

Grenzen ein p-dotiertes und ein n-dotiertes Gebiet aneinander, in der Praxis zwei verschieden dotierte Zonen desselben Kristalls, entsteht ein
__pn-Übergang__. Auf der n-Seite gibt es sehr viele freie Elektronen und kaum Löcher, auf der p-Seite umgekehrt.

**Diffusion.** Teilchen, die sich frei bewegen, verteilen sich von selbst, aus Gebieten hoher Dichte in Gebiete niedriger. Dieser Transport allein durch den
Dichteunterschied heißt __Diffusion__, wie in der Fußnote des Skripts. Elektronen diffundieren also von n nach p, Löcher von p nach n. Wo sie sich treffen,
__rekombinieren__ sie: Ein Elektron füllt ein Loch, und beide sind als freie Träger verschwunden.

**Die Raumladungszone.** Zurück bleiben nahe der Grenze die ortsfesten Ionen: positive Donator-Ionen auf der n-Seite, negative Akzeptor-Ionen auf der
p-Seite, nicht mehr durch freie Träger ausgeglichen. Diese an freien Trägern verarmte Schicht heißt __Raumladungszone__ oder __Sperrschicht__. Ihre Ladungen
erzeugen ein elektrisches Feld, das von der positiven n-Seite zur negativen p-Seite zeigt.

**Gleichgewicht.** Das Feld treibt Elektronen zur n-Seite und Löcher zur p-Seite zurück, einen __Driftstrom__ gegen die Diffusion. Je mehr Träger
hinübergewandert sind, desto stärker wird das Feld, bis sich Drift und Diffusion für jede Trägersorte gerade aufheben. Dann fließt kein Strom, aber zwischen
den beiden Seiten liegt eine Potenzialdifferenz, die __Diffusionsspannung__ $U_\text{Diff}$, die n-Seite positiv gegen die p-Seite. Für sie braucht man
die __Temperaturspannung__ $U_T$, die Wärmeenergie $k_BT$ als Spannung ausgedrückt:

:::formel
$$U_\text{Diff} = U_T\,\ln\frac{N_A\,N_D}{n_i^2}, \qquad U_T = \frac{k_B\,T}{e}.$$
:::

**So liest man das:** Bei $300\,\text{K}$ ist $U_T = 25{,}9\,\text{mV}$. Die Diffusionsspannung hängt nur logarithmisch von der Dotierung ab; für Silizium
mit Dotierungen zwischen $10^{15}$ und $10^{18}\,\text{cm}^{-3}$ auf beiden Seiten liegt sie zwischen etwa $0{,}6$ und $0{,}95\,\text{V}$. Im Banddiagramm
sind die Bänder der p-Seite um $e\,U_\text{Diff}$ höher als die der n-Seite, und in der Raumladungszone verbiegen sie sich von der einen Höhe zur anderen. Das
Skript nennt diesen Potenzialunterschied die Durchlassspannung; das ist verkürzt, wie der nächste Abschnitt zeigt.

**Im Bild:** Die n-Seite ist ein Parkhaus mit vielen Autos oben, die p-Seite eines mit vielen Lücken unten. Verbindet man sie, fahren Autos hinüber und fallen
in Lücken. Die geladenen Plattformen, die zurückbleiben, heben das p-Parkhaus an, bis zwischen den Oberdecks eine Rampe der Höhe $e\,U_\text{Diff}$ liegt.
Jetzt kommen nur noch Autos mit genug Schwung hinauf, und ebenso viele rollen zurück.

:::herleitung
**Ein Fermi-Niveau für beide Seiten.** Im Gleichgewicht liegt das Fermi-Niveau auf beiden Seiten gleich hoch. Läge es auf einer Seite höher, wären dort
Zustände gleicher Energie stärker besetzt als drüben, und Elektronen wanderten hinüber, bis der Unterschied verschwunden ist, wie Wasser in verbundenen
Gefäßen.

**Die Verschiebung der Bänder.** Auf der n-Seite liegt das Fermi-Niveau nach dem Abschnitt über die Dotierung um $k_BT\ln(N_D/n_i)$ über der Mitte $W_i$,
auf der p-Seite um $k_BT\ln(N_A/n_i)$ darunter. Damit beide Fermi-Niveaus gleich hoch liegen, müssen sich die Bänder der beiden Seiten um die Summe
gegeneinander verschieben:

$$e\,U_\text{Diff} = k_B\,T\,\ln\frac{N_D}{n_i} + k_B\,T\,\ln\frac{N_A}{n_i} = k_B\,T\,\ln\frac{N_A\,N_D}{n_i^2}.$$

Division durch $e$ ergibt die Formel.

**Dasselbe mit dem Boltzmann-Faktor.** Mit $n_n$ und $n_p$ für die Elektronendichten auf der n- und der p-Seite: Die Elektronen der p-Seite sind die, die von
der n-Seite die Rampe hinaufgekommen sind, und ihr Anteil ist der Boltzmann-Faktor der Rampenhöhe:

$$\frac{n_p}{n_n} = \exp\Big(-\frac{U_\text{Diff}}{U_T}\Big), \qquad n_n = N_D, \qquad n_p = \frac{n_i^2}{N_A}.$$

Logarithmiert ergibt das dieselbe Spannung. Im Bild: Oben auf der Rampe stehen so viel weniger Autos, wie es ihrer Höhe entspricht.
:::

Wie breit die Raumladungszone ist und wie stark ihr Feld, zeigt der Vergleich mit dem Plattenkondensator aus dem Kapitel über den Kondensator. Für einen
Übergang mit gleicher Dotierung $N$ auf beiden Seiten und der Permittivität $\varepsilon$ des Kristalls, bei Silizium $11{,}7\,\varepsilon_0$, ergeben sich
die Breite $w$ und die größte Feldstärke $E_\text{max}$ an der Grenze:

$$w = \sqrt{\frac{4\,\varepsilon\,U_\text{Diff}}{e\,N}}, \qquad E_\text{max} = \frac{2\,U_\text{Diff}}{w}.$$

:::herleitung
**Die Ladung.** Die Zone reicht auf jeder Seite $w/2$ weit. Auf der n-Seite sitzt dort die Ladung $e\,N$ je Volumen, auf der p-Seite $-e\,N$; auf einer
Fläche $A$ trägt jede Hälfte die Ladung $e\,N\,A\,w/2$.

**Das Feld.** Wie zwischen den Platten eines Kondensators ist das Feld an der Grenze die Ladung einer Seite je Fläche, geteilt durch $\varepsilon$. Zu den
Rändern der Zone hin nimmt es gleichmäßig ab, weil immer weniger Ladung zwischen dem Rand und dem betrachteten Ort liegt, und am Rand ist es null:

$$E_\text{max} = \frac{e\,N\,w}{2\,\varepsilon}.$$

**Die Spannung.** Die Spannung ist das Integral der Feldstärke über den Weg, hier die Fläche eines Dreiecks mit der Grundseite $w$ und der Höhe
$E_\text{max}$:

$$U_\text{Diff} = \frac{1}{2}\,E_\text{max}\,w = \frac{e\,N\,w^2}{4\,\varepsilon}.$$

Nach $w$ aufgelöst ergibt sich die Formel, und $E_\text{max}$ ist das Doppelte von $U_\text{Diff}$ durch $w$. Im Bild: Die Rampe ist ein kurzer, steiler
Anstieg, so lang wie die Zone breit ist.
:::

**Messen lässt sich die Diffusionsspannung nicht.** Ein Spannungsmesser an den Anschlüssen einer stromlosen Diode zeigt null. Wo die Metallkontakte auf den
Halbleiter treffen, entstehen weitere Sprünge des Potenzials, die die Diffusionsspannung genau ausgleichen.

:::herleitung
Im Gleichgewicht gibt es keine Energiequelle. Zeigte das Messgerät eine Spannung, könnte man die Anschlüsse über einen Widerstand verbinden, und es flösse ein
Dauerstrom, der den Widerstand heizt, ohne dass irgendwo Energie zugeführt wird. Das widerspricht der Energieerhaltung. Also ist die Summe aller
Potenzialsprünge um den geschlossenen Kreis null, die Diffusionsspannung eingeschlossen, und nach der Maschenregel zeigt das Messgerät nichts. Im Bild: Zwei
Parkhäuser mit einer Rampe dazwischen, über Straßen zu einem Ring verbunden; einmal herum kommt man auf derselben Höhe an, sonst rollten die Autos ewig im
Kreis.
:::

::::beispiel Diffusionsspannung und Raumladungszone
**(a) Gleich dotiert.** Silizium bei $300\,\text{K}$, beide Seiten gleich stark:

$$N_A = N_D = 10^{16}\,\text{cm}^{-3}, \qquad n_i = 10^{10}\,\text{cm}^{-3}, \qquad U_T = 25{,}9\,\text{mV}.$$

Im Logarithmus kürzen sich die Einheiten:

$$U_\text{Diff} = 25{,}9\,\text{mV}\cdot\ln\frac{10^{32}}{10^{20}} = 25{,}9\,\text{mV}\cdot27{,}6 = 0{,}714\,\text{V}.$$

**(b) Ungleich dotiert.** Die p-Seite ist hundertmal stärker dotiert, mit $10^{18}$ Akzeptoren je Kubikzentimeter:

$$U_\text{Diff} = 25{,}9\,\text{mV}\cdot\ln\frac{10^{34}}{10^{20}} = 0{,}833\,\text{V}.$$

Hundertmal mehr Akzeptoren erhöhen die Spannung nur um $U_T\ln100$, also um $0{,}119\,\text{V}$.

**(c) Breite und Feld.** Für den gleich dotierten Übergang, in SI-Einheiten:

$$\varepsilon = 11{,}7\cdot8{,}854\cdot10^{-12}\,\frac{\text{F}}{\text{m}} = 1{,}036\cdot10^{-10}\,\frac{\text{F}}{\text{m}}, \qquad N = 10^{22}\,\text{m}^{-3}.$$

$$w = \sqrt{\frac{4\cdot1{,}036\cdot10^{-10}\,\frac{\text{F}}{\text{m}}\cdot0{,}714\,\text{V}}{1{,}602\cdot10^{-19}\,\text{C}\cdot10^{22}\,\text{m}^{-3}}} = 0{,}43\,\mu\text{m},$$

$$E_\text{max} = \frac{2\cdot0{,}714\,\text{V}}{0{,}43\,\mu\text{m}} = 3{,}3\,\frac{\text{MV}}{\text{m}}.$$

Die Zone ist weniger als ein halbes Mikrometer breit, und ihr Feld ist so stark wie das, bei dem Luft durchschlägt. Die bescheidenen $0{,}7\,\text{V}$
reichen dafür, weil die Strecke so kurz ist.

**Im Bild:** Eine Rampe von $0{,}7\,\text{eV}$ Höhe auf weniger als einem halben Mikrometer: kurz, aber steil.
::::

:::grafik
Szene: get1/halbleiterbauelemente/01-pn-uebergang · Vorlage: pn-banddiagramm
Oben ein Kristallstab, links p-dotiert mit Löchern als Kreisen und ortsfesten Akzeptor-Ionen mit Minus, rechts n-dotiert mit Elektronen als Punkten und
ortsfesten Donator-Ionen mit Plus. Anfangs sind beide Hälften getrennt; ein Knopf „verbinden“ lässt Elektronen nach links und Löcher nach rechts
diffundieren und an der Grenze paarweise verschwinden, bis eine Zone ohne freie Träger bleibt, in der nur die Ionen sitzen. Ein Feldpfeil von n nach p wächst
mit, bis Drift und Diffusion im Gleichgewicht sind; zwei Zähler für die beiden Ströme zeigen dann gleiche Werte. Darunter das Banddiagramm: Die Bänder der
p-Seite liegen um $e\,U_\text{Diff} = 0{,}71\,\text{eV}$ höher, dazwischen auf $0{,}43\,\mu\text{m}$ verbogen, das Fermi-Niveau als durchgehende gestrichelte
Linie. Ein Regler für die angelegte Spannung $U$ von $-2\,\text{V}$ bis $+0{,}7\,\text{V}$ senkt oder hebt die Rampe auf $e(U_\text{Diff} - U)$; die Pfeile
der Majoritätsträger, die hinaufkommen, werden dabei exponentiell dicker oder verschwinden, während der dünne Rückfluss der Minoritätsträger gleich bleibt.
Kernaussage: Am pn-Übergang baut die Diffusion eine Rampe auf, und die angelegte Spannung verstellt ihre Höhe. (Rot = ortsfeste Ionen und Feld, blau =
Elektronen und Löcher, orange = Rampe und Ströme, grau = Bänder und Kristall, gestrichelt = Fermi-Niveau.)
:::

## Durchlass- und Sperrrichtung

Liegt an der p-Seite der Pluspol einer äußeren Spannung $U$, heißt das __Durchlassrichtung__; liegt er an der n-Seite, __Sperrrichtung__, und $U$ ist
negativ. Die äußere Spannung fällt fast ganz an der Raumladungszone ab, denn dort gibt es kaum freie Träger, sie hat den größten Widerstand im Kristall. In
Durchlassrichtung wirkt die Spannung, wie das Skript sagt, dem Feld der Zone entgegen, und die Rampe sinkt auf $e(U_\text{Diff} - U)$; in Sperrrichtung
wird sie höher.

Zwei Ströme kreuzen die Rampe. Den __Hinstrom__ tragen Majoritätsträger, die die Rampe hinaufkommen, Elektronen von n nach p und Löcher von p nach n. Den
__Rückstrom__ tragen Minoritätsträger, die nahe der Zone durch Wärme entstehen und an ihren Rand geraten, etwa Elektronen der p-Seite; für sie geht es die
Rampe hinunter, und das Feld zieht sie hinüber, wie hoch die Rampe auch ist. Den Rückstrom nennt man den __Sättigungssperrstrom__ $I_S$:

:::formel Satz
$$I_\text{hin}(U) = I_S\,\exp\frac{U}{U_T}, \qquad I_\text{rück} = I_S.$$
:::

**So liest man das:** Ohne äußere Spannung sind beide gleich, und es fließt kein Strom. Jede Absenkung der Rampe um $U_T$ vervielfacht den Hinstrom um den
Faktor $e$, je $59{,}5\,\text{mV}$ verzehnfacht er sich. Der Rückstrom hängt nicht von $U$ ab; er ist winzig, weil es nur wenige Minoritätsträger gibt, und
wächst mit $n_i^2$ stark mit der Temperatur. In Sperrrichtung ist der Hinstrom schon nach einigen Zehntelvolt verschwunden, und es bleibt der kleine
Rückstrom. Der Strom durch die Diode ist der Unterschied der beiden; daraus wird im nächsten Artikel die Kennlinie der Diode, die Shockley-Gleichung.

**Im Bild:** Senkt die Spannung die Rampe, kommen exponentiell mehr Autos hinauf, denn der Boltzmann-Faktor wächst mit jedem Stück, das die Rampe niedriger
wird. Hebt sie die Rampe, kommt keines mehr hinauf; übrig bleiben die wenigen, die drüben oben stehen und hinunterrollen, wie hoch die Rampe auch ist.

:::herleitung
**Der Hinstrom.** Über die Rampe kommen die Majoritätsträger, deren Energie für ihre Höhe reicht, und ihr Anteil ist der Boltzmann-Faktor der Rampenhöhe:

$$I_\text{hin}(U) \sim \exp\Big(-\frac{U_\text{Diff} - U}{U_T}\Big) = \exp\Big(-\frac{U_\text{Diff}}{U_T}\Big)\,\exp\frac{U}{U_T}.$$

Der erste Faktor ist fest; die Spannung wirkt allein über den zweiten.

**Der Rückstrom.** Ein Minoritätsträger, der den Rand der Zone erreicht, wird vom Feld hinübergezogen, gleich wie stark es ist. Wie viele ankommen, hängt nur
davon ab, wie viele es gibt und wie schnell sie entstehen, nicht von der Rampe; das ist $I_S$. Weil die Minoritätsdichte $n_i^2/N$ ist, wächst $I_S$ mit
$n_i^2$.

**Das Gleichgewicht legt die Konstante fest.** Ohne äußere Spannung fließt kein Strom, Hin- und Rückstrom sind gleich. Also ist der Hinstrom bei $U = 0$ gleich
$I_S$, und für jedes $U$ ist er $I_S$ mal dem Faktor $\exp(U/U_T)$. Dieses vereinfachte Bild liefert dieselbe Spannungsabhängigkeit wie die genaue Theorie von
Shockley, die die Diffusion der Träger durchrechnet. Im Bild: Ohne Spannung fahren je Sekunde genauso viele Autos hinauf, wie hinunterrollen.
:::

::::beispiel Wie stark die Rampe den Strom steuert
Bei $300\,\text{K}$ ist $U_T = 25{,}9\,\text{mV}$.

**(a) Je Zehntelvolt.** Senkt man die Rampe um $0{,}1\,\text{V}$:

$$\exp\frac{0{,}1\,\text{V}}{0{,}0259\,\text{V}} = e^{3{,}87} = 47{,}9.$$

Der Hinstrom wächst auf das Achtundvierzigfache. Um das Zehnfache wächst er je

$$U_T\,\ln10 = 59{,}5\,\text{mV}.$$

**(b) Bei 0,6 und 0,7 V.** Der Hinstrom im Verhältnis zum Rückstrom:

$$\exp\frac{0{,}6\,\text{V}}{0{,}0259\,\text{V}} = 1{,}2\cdot10^{10}, \qquad \exp\frac{0{,}7\,\text{V}}{0{,}0259\,\text{V}} = 5{,}7\cdot10^{11}.$$

Mit einem Sättigungsstrom von $10^{-14}\,\text{A}$, der Größenordnung kleiner Siliziumübergänge, sind das $0{,}12\,\text{mA}$ bei $0{,}6\,\text{V}$ und knapp
$6\,\text{mA}$ bei $0{,}7\,\text{V}$. Zwischen $0{,}6$ und $0{,}7\,\text{V}$ wird aus fast nichts ein merklicher Strom; das ist die Schwelle von
$0{,}6\,\text{V}$ in den Bildern des Skripts.

**(c) In Sperrrichtung.** Bei $-0{,}1$ und $-0{,}2\,\text{V}$ ist der Hinstrom nur noch ein kleiner Teil des Rückstroms:

$$\exp\frac{-0{,}1\,\text{V}}{0{,}0259\,\text{V}} = 0{,}021, \qquad \exp\frac{-0{,}2\,\text{V}}{0{,}0259\,\text{V}} = 4{,}4\cdot10^{-4}.$$

Schon ab einigen Zehntelvolt Sperrspannung fließt praktisch nur noch $I_S$, wie groß die Spannung auch wird, bis zum Durchbruch, den der nächste Artikel
behandelt.

**Im Bild:** Jedes Stück, um das die Rampe sinkt, vervielfacht den Verkehr hinauf. Hebt man sie, bleibt nur das stetige Rinnsal der wenigen Autos, die von
drüben herunterrollen.
::::

Das Skript sagt, sobald die angelegte Spannung die Durchlassspannung überschreite, fließe ein Strom. Eine feste Schwelle gibt es aber nicht: Der Strom wächst
stetig und exponentiell und wird zwischen $0{,}6$ und $0{,}7\,\text{V}$ merklich, etwas unterhalb der Diffusionsspannung, die das Skript Durchlassspannung
nennt. Den Sperrstrom nennt es einen Diffusionsstrom; genauer diffundieren die Minoritätsträger bis an die Sperrschicht und werden dort vom Feld
hinübergezogen.

## Bedeutung und Ausblick

Das Bändermodell erklärt, warum ein Kristall leitet oder isoliert: Nicht die Zahl der Elektronen entscheidet, sondern ob freie Zustände in Reichweite sind.
Bei Halbleitern ist die Lücke so klein, dass Wärme, Licht und eingebaute Fremdatome die Zahl der Träger um viele Zehnerpotenzen verändern. Die Dotierung macht
daraus einen Werkstoff nach Maß, und der pn-Übergang macht daraus ein Ventil, dessen Rampe die angelegte Spannung verstellt.

Darauf bauen die folgenden Artikel auf. Der nächste behandelt die Kennlinie der Diode mit der Shockley-Gleichung und Spezialdioden wie Zener-, Kapazitäts-
und Fotodiode, deren Wirkungen sich hier schon andeuten: die Sperrschicht als Kondensator und Licht, dessen Photonen die Bandlücke überwinden. Danach folgen
Arbeitspunkt und Ersatzschaltungen der Diode, Gleichrichter und der Transistor, zwei pn-Übergänge hintereinander. Die Halbleiterphysik selbst, mit
Zustandsdichten, Fermi-Statistik und Ladungstransport, behandelt das Modul über die Grundlagen elektronischer Materialien und Bauelemente ausführlich.

:::kern
- Im Kristall werden die Energieniveaus der Atome zu Bändern; die Lücke zwischen vollem Valenzband und leerem Leitungsband ist $W_g=W_L-W_V$.
- Ein volles Band trägt keinen Strom; leiten können nur Elektronen mit freien Zuständen in Reichweite.
- Metall: teilweise gefülltes Band; Halbleiter: Lücke um ein Elektronvolt; Isolator: mehrere Elektronvolt.
- Ein Loch ist der fehlende Platz im Valenzband und wirkt wie eine positive Ladung $+e$.
- Beide Trägersorten leiten: $\sigma=e\,(n\mu_n+p\mu_p)$.
- Die Fermi-Verteilung gibt die Besetzung an; am Fermi-Niveau ist sie $\tfrac12$, weit darüber ein Boltzmann-Faktor.
- Massenwirkungsgesetz: $np=n_i^2$; reines Silizium hat bei $300\,\text{K}$ rund $10^{10}$ Träger je $\text{cm}^3$.
- Donatoren wie Phosphor liefern Elektronen, Akzeptoren wie Bor Löcher; Majoritätsträger etwa gleich der Dotierdichte, Minoritätsträger $n_i^2/N$.
- Am pn-Übergang baut die Diffusion eine Raumladungszone mit Feld auf, bis die Drift sie ausgleicht.
- Diffusionsspannung: $U_\text{Diff}=U_T\ln(N_AN_D/n_i^2)$, bei Silizium um $0{,}7\,\text{V}$; messen lässt sie sich nicht.
- Durchlassrichtung senkt die Rampe, der Hinstrom wächst mit $e^{U/U_T}$; in Sperrrichtung bleibt der kleine Sättigungsstrom $I_S$.
- Im Einweggleichrichter lässt die Diode nur die positiven Halbwellen durch, abzüglich etwa $0{,}6\,\text{V}$.
:::

:::quiz
F: Was macht die Diode im Einweggleichrichter des Skripts?
A: Sie leitet nur, solange die Eingangsspannung ihre Durchlassspannung von etwa $0{,}6\,\text{V}$ übersteigt; dann liegt der Rest am Widerstand, sonst fließt nichts, und die ganze Spannung liegt an der Diode. Bei $10\,\text{V}$ Scheitelwert sind das $9{,}4\,\text{V}$ Spitze, gut 48 % Leitdauer und $10\,\text{V}$ in Sperrrichtung.
F: Wie entstehen Energiebänder, und was sind Valenzband, Leitungsband und Bandlücke?
A: Im Kristall sind die Atome gekoppelt, und wie bei gekoppelten Pendeln spaltet jedes Niveau in so viele Niveaus auf, wie es Atome gibt; sie liegen so dicht, dass Bänder entstehen. Das Valenzband ist bei $0\,\text{K}$ voll, bei Silizium mit den Bindungselektronen, das Leitungsband darüber leer, und die Lücke $W_g=W_L-W_V$ beträgt bei Silizium $1{,}12\,\text{eV}$.
F: Warum leitet ein volles Band nicht, und was unterscheidet Metall, Halbleiter und Isolator?
A: Im vollen Band gehört zu jedem Zustand einer mit umgekehrter Geschwindigkeit, die Summe ist null, und nach dem Pauli-Prinzip kann kein Elektron in einen anderen Zustand wechseln. Metalle haben ein teilweise gefülltes Band, Halbleiter eine Lücke um ein Elektronvolt, die Wärme gelegentlich überwindet, Isolatoren eine von mehreren Elektronvolt.
F: Warum verhält sich ein Loch wie eine positive Ladung?
A: Das Band mit einem freien Platz trägt den Strom des vollen Bandes, also null, minus den Beitrag des fehlenden Elektrons; das ergibt $+e\,\vec v_0/V$. Das ist der Strom einer Ladung $+e$ mit der Geschwindigkeit des fehlenden Elektrons, und im Feld wandert das Loch mit dem Feld zum Minuspol.
F: Was gibt die Fermi-Verteilung an, und warum darf das Fermi-Niveau in der Bandlücke liegen?
A: Sie gibt die Wahrscheinlichkeit an, dass ein Zustand der Energie $W$ besetzt ist; am Fermi-Niveau ist sie $\tfrac12$, weit darüber ein Boltzmann-Faktor. $W_F$ ist kein Zustand, sondern eine Kenngröße der Verteilung. Beim reinen Halbleiter liegt es in der Mitte, weil dort die Besetzung des Leitungsbands so klein ist wie die Leere des Valenzbands, bei Silizium an der Kante $3{,}9\cdot10^{-10}$.
F: Was sagt das Massenwirkungsgesetz, und warum leitet reines Silizium bei Wärme viel besser?
A: $np=n_i^2$, unabhängig vom Fermi-Niveau und damit von der Dotierung, mit $n_i$ proportional zu $T^{3/2}e^{-W_g/(2k_BT)}$. Wegen des Exponentialfaktors steigt $n_i$ von $300$ auf $350\,\text{K}$ etwa auf das 28-Fache; reine Halbleiter sind Heißleiter. Bei $300\,\text{K}$ sind es rund $10^{10}\,\text{cm}^{-3}$, ein freies Elektron auf $5\cdot10^{12}$ Atome.
F: Wie wirken Donatoren und Akzeptoren?
A: Phosphor hat fünf Valenzelektronen; vier binden, das fünfte ist mit rund $45\,\text{meV}$ schwach gebunden und wird bei Raumtemperatur frei, Phosphor bleibt als positives Ion zurück. Bor hat drei; in seine unvollständige Bindung springt ein Elektron aus einer Nachbarbindung, Bor wird negativ, und im Valenzband bleibt ein Loch. Das Donatorniveau liegt knapp unter $W_L$, das Akzeptorniveau knapp über $W_V$.
F: Wie viele Ladungsträger hat Silizium mit $10^{16}$ Phosphoratomen je Kubikzentimeter?
A: Elektronen etwa $10^{16}$, Löcher $n_i^2/N_D=10^{4}\,\text{cm}^{-3}$; die Leitfähigkeit ist rund $2{,}2\,\text{S/cm}$, gemessen etwa $0{,}5\,\Omega\,\text{cm}$, das $7{,}4\cdot10^5$-Fache von reinem Silizium. Das Fermi-Niveau steigt um $0{,}36\,\text{eV}$ auf $0{,}20\,\text{eV}$ unter $W_L$, also unter das Donatorniveau, und deshalb sind fast alle Donatoren ionisiert.
F: Wie entstehen Raumladungszone und Diffusionsspannung, und warum kann man diese nicht messen?
A: Elektronen diffundieren von n nach p, Löcher umgekehrt, und rekombinieren; zurück bleiben ortsfeste Ionen, deren Feld einen Driftstrom treibt, bis er die Diffusion ausgleicht. Weil das Fermi-Niveau auf beiden Seiten gleich hoch liegen muss, ist $U_\text{Diff}=U_T\ln(N_AN_D/n_i^2)$, bei $10^{16}\,\text{cm}^{-3}$ auf beiden Seiten $0{,}71\,\text{V}$ über $0{,}43\,\mu\text{m}$. Messen kann man sie nicht, weil die Kontaktspannungen sie im stromlosen Kreis genau ausgleichen; sonst flösse ein Dauerstrom ohne Energiequelle.
F: Was geschieht in Durchlass- und Sperrrichtung, und was stellt das Skript dabei ungenau dar?
A: Die Durchlassrichtung senkt die Rampe, und der Hinstrom wächst mit $e^{U/U_T}$, je $59{,}5\,\text{mV}$ auf das Zehnfache; in Sperrrichtung bleibt der konstante Rückstrom $I_S$ der Minoritätsträger. Das Skript nennt die Diffusionsspannung Durchlassspannung und lässt erst ab ihr Strom fließen, statt stetig exponentiell. Außerdem schreibt es „kohärente“ statt kovalente Bindung, $\hat U_E>0$ statt $u_E(t)>0$, und sein Bild 10.5 zeigt das Fermi-Niveau, wie es nur bei tiefer Temperatur liegt.
:::
