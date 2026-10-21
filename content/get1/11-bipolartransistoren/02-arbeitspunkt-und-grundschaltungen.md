---
title: Arbeitspunkt und Grundschaltungen des Transistors
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110200
summary: Von Grund auf – wie man einen Bipolartransistor in seinen Arbeitspunkt bringt und dort hält, obwohl B streut und die Temperatur wandert. Leitbild ist ein Regelventil mit Steuerleitung an einem Wasserturm. Mit Arbeitsgerade und Verlustleistung, Schalter oder Verstärker, den linearen Ersatzschaltbildern, der Rechnung mit Annahme und Probe für Basis- und Emitterwiderstand, dem Arbeitspunkt in der Mitte, der Empfindlichkeit gegen B und Temperatur, Strom- und Spannungsgegenkopplung, den Betriebsgrenzen, dem Stromspiegel, dem Inverter und den drei Grundschaltungen. Mit Beispiel-Seite.
tags: Arbeitspunkt, Basisspannungsteiler, Emitterwiderstand, Gegenkopplung, Emitterschaltung, Kollektorschaltung, Basisschaltung
---

## Anschaulich

Im vorigen Artikel wurde der Bipolartransistor zu einer gesteuerten Stromquelle: Ein kleiner Basisstrom geht mit einem $B$-mal so großen Kollektorstrom einher.
Bevor er damit verstärken oder schalten kann, sind drei Fragen offen. In welchem Zustand soll er ruhen? Wie hält man ihn dort, obwohl $B$ von Exemplar zu
Exemplar streut und die Temperatur wandert? Und wie schließt man ihn an, damit aus seinen drei Anschlüssen ein Eingang und ein Ausgang werden?

**Das Leitbild dieses Artikels:** **ein Regelventil mit Steuerleitung an einem Wasserturm.** Wie im Artikel über den Arbeitspunkt der Diode speist ein
Wasserturm über ein enges Rohr eine Leitung, die in einen Abfluss mündet. Am Ende sitzt jetzt ein Regelventil mit einer dünnen Steuerleitung. Es lässt genau das
$B$-Fache des Wassers durch, das durch die Steuerleitung fließt, gleich wie viel Druck vor ihm ansteht, solange ein kleiner Restdruck bleibt. In der
Steuerleitung sitzt das Rückschlagventil aus den Diodenartikeln, das erst ab einem Mindestdruck öffnet, und das Steuerwasser läuft hinter dem Regelventil mit in
den Abfluss. Ein Manometer zeigt den Druck vor dem Ventil. Ein gewöhnliches Ventil kann das nicht, ein Durchflussregler schon: Er hält den Durchfluss fest,
auch wenn der Druck schwankt. Wie jedes Wasserbild ist auch dieses eine Analogie; Druck steht für Potenzial, Durchfluss für Strom.

Vier Folgerungen:

- **Ruhen in der Mitte.** Soll das Ventil ein Zittern des Steuerstroms in beide Richtungen weitergeben, darf es weder ganz zu noch ganz offen stehen. Am besten
  zeigt das Manometer in Ruhe die Mitte zwischen vollem Turmdruck und Restdruck. Das ist der Arbeitspunkt eines Verstärkers.
- **Jedes Ventil übersetzt anders.** Ein zweites Exemplar lässt beim selben Steuerstrom vielleicht doppelt so viel durch, und wer nur den Steuerstrom
  einstellt, findet sein Manometer am Anschlag. Abhilfe schafft eine Rückmeldung, bei der der Hauptstrom seinen eigenen Steuerstrom drosselt: die Gegenkopplung.
- **Zwei gleiche Ventile an einer Steuerleitung führen gleich viel.** Stellt sich das erste selbst auf einen gewünschten Durchfluss ein, kopiert ihn das zweite.
  Das ist der Stromspiegel.
- **Ganz zu oder ganz offen.** Ohne Steuerstrom zeigt das Manometer den vollen Turmdruck, mit reichlich Steuerstrom fast nichts. Diese beiden Zustände nutzt der
  Inverter der Digitaltechnik.

| Im Wasserbild | In der Schaltung |
|---|---|
| Wasserturm | Versorgungsspannung $U_{CC}$ |
| enges Rohr vor dem Ventil | Kollektorwiderstand $R_C$ |
| Regelventil, das das $B$-Fache des Steuerstroms durchlässt | Kollektor-Emitter-Strecke im aktiven Bereich |
| Steuerleitung mit Rückschlagventil | Basis-Emitter-Übergang mit der Schwelle $U_{BE,\text{ein}}$ |
| Steuerstrom | Basisstrom $I_B$ |
| Manometer vor dem Ventil | Kollektorpotenzial, bei Emitter an Masse gleich $U_{CE}$ |
| Ventil ganz offen, das Rohr gibt nicht mehr her | Sättigung mit $U_{CE,\text{sat}}$ |
| kein Steuerstrom, Ventil zu | Sperrbereich |
| Ruhestellung des Ventils | Arbeitspunkt |
| Hauptstrom drosselt seinen eigenen Steuerstrom | Gegenkopplung |

:::grafik
Szene: get1/bipolartransistoren/02-regelventil · Vorlage: transistor-regelventil
Links ein Wasserturm, von dem ein enges Rohr zu einem Regelventil führt, hinter dem das Wasser in einen Abfluss fällt; vor dem Ventil ein Manometer. Von links
führt eine dünne Steuerleitung mit einem kleinen Rückschlagventil an das Regelventil, und ihr Wasser mündet hinter dem Ventil in den Abfluss. Ein Regler stellt
den Steuerstrom ein, ein zweiter den Übersetzungsfaktor $B$ des Ventils. Bei null Steuerstrom ist das Ventil zu, und das Manometer zeigt den vollen Turmdruck;
mit wachsendem Steuerstrom öffnet es, der Hauptstrom wächst auf das $B$-Fache, und der Zeiger sinkt gleichmäßig; ist das enge Rohr ausgeschöpft, steht das
Ventil ganz offen, und der Zeiger bleibt beim Restdruck stehen, obwohl der Steuerstrom weiter wächst. Daneben das Schaltbild mit $U_{CC}$, $R_C$, dem
Transistor und den mitlaufenden Werten von $I_B$, $I_C$ und $U_{CE}$. Kernaussage: Der Steuerstrom stellt den Hauptstrom ein, bis das Rohr nicht mehr hergibt.
(Blau = Wasser und Ströme, rot = Regelventil und Transistor, orange = Steuerleitung und Manometer, grau = Turm, Rohre und Schaltbild.)
:::

## Arbeitspunkt, Arbeitsgerade und Verlustleistung

Wie bei der Diode ist der __Arbeitspunkt__ eines Transistors der Zustand, in dem er ohne Signal ruht: die Gleichwerte von $I_B$, $I_C$, $U_{BE}$ und $U_{CE}$.
Ein Signal ist später eine kleine Schwankung um diesen Punkt.

Die einfachste Schaltung dazu zeigt Bild 11.4 des Skripts. Der Kollektor liegt über $R_C$ an der Versorgung $U_{CC}$, der Emitter an Masse, und eine
Eingangsspannung $U_\text{ein}$ treibt über den __Basiswiderstand__ $R_B$ den Basisstrom. Das Skript nennt die Eingangsspannung $U_E$; hier heißt sie
$U_\text{ein}$, damit man sie nicht mit Größen des Emitters wie $I_E$ und $R_E$ verwechselt, und die Ausgangsspannung heißt $U_\text{aus}$. Ein- und
Ausgangsspannung zählen gegen Masse, Ströme und Transistorspannungen wie im vorigen Artikel.

Der Kollektorkreis ist für die Kollektor-Emitter-Strecke eine Ersatzspannungsquelle mit der Leerlaufspannung $U_{CC}$ und dem Innenwiderstand $R_C$. Nach dem
Artikel über den Arbeitspunkt der Diode gehört dazu eine __Arbeitsgerade__:

$$I_C = \frac{U_{CC} - U_{CE}}{R_C}.$$

**So liest man das:** Eingabe ist die Kollektor-Emitter-Spannung, Ausgabe der Kollektorstrom, den der Kollektorkreis bei ihr zulässt. Im Ausgangskennlinienfeld
läuft die Gerade vom Punkt $(U_{CC}, 0)$ des gesperrten Transistors zum Punkt $(0, U_{CC}/R_C)$. Der Arbeitspunkt ist ihr Schnittpunkt mit der Kennlinie
des Basisstroms, der gerade fließt.

**Im Bild:** Je mehr Wasser das Ventil durchlässt, desto mehr Druck verbraucht das enge Rohr, und desto weniger zeigt das Manometer.

:::herleitung
In einer Masche liegen die Versorgung, $R_C$ und die Kollektor-Emitter-Strecke. Nach der Maschenregel und dem Ohmschen Gesetz gilt

$$U_{CC} = R_C\,I_C + U_{CE}.$$

Nach $I_C$ aufgelöst ergibt sich die Gerade. Der Basisstrom fließt über den Emitter unmittelbar nach Masse und erzeugt in dieser Masche keinen Spannungsabfall.
Im Bild: Der Turmdruck teilt sich auf das Rohr und das Ventil auf.
:::

Was der Transistor dabei in Wärme umsetzt, ist seine __Verlustleistung__. Den kleinen Anteil des Basisstroms, das Produkt aus $U_{BE}$ und $I_B$, vernachlässigt
man; längs der Arbeitsgeraden ist sie dann, mit ihrem Höchstwert $P_\text{max}$:

$$P = U_{CE}\,I_C = \frac{U_{CE}\,(U_{CC} - U_{CE})}{R_C}, \qquad P_\text{max} = \frac{U_{CC}^2}{4\,R_C}.$$

**So liest man das:** Eingabe ist wieder $U_{CE}$, Ausgabe die Leistung in Watt. Über $U_{CE}$ aufgetragen ist sie eine nach unten offene Parabel, null an
beiden Enden der Geraden und am größten in der Mitte, bei der halben Versorgungsspannung.

Daraus folgt, was das Skript in Abschnitt 11.2 über die Wahl des Arbeitspunkts sagt. Ein __Schalter__ benutzt die beiden Enden, den Sperrbereich und die
Sättigung. Gesperrt fließt kein Strom; gesättigt fließt zwar der größte Strom, den die Gerade zulässt, aber bei nur $0{,}2\,\text{V}$. In beiden Zuständen
bleibt die Verlustleistung klein. Das Skript begründet die Sättigung auch damit, dass dort der Kollektorstrom kleiner sei; gemeint sein kann nur, kleiner als
$BI_B$, denn auf der Arbeitsgeraden ist er dort am größten. Der zweite Vorteil, den das Skript nennt, ist der große Abstand zum ausgeschalteten Zustand: Die
Ausgangsspannung springt zwischen fast $U_{CC}$ und $0{,}2\,\text{V}$, und beide Zustände bleiben auch unter Störungen sicher unterscheidbar.

Ein __Verstärker__ muss im aktiven Bereich arbeiten, wo der Kollektorstrom in erster Näherung linear vom Basisstrom abhängt, und dort weit genug von beiden
Enden, damit eine Schwankung nach oben und unten Platz hat. Das ist die Mitte der Geraden, also genau der Punkt der größten Verlustleistung. Das nimmt man in
Kauf, sagt das Skript, weil es hier darauf ankommt, ein Signal __verzerrungsfrei__ zu übertragen, also ohne seine Form zu verändern.

**Im Bild:** Ist das Ventil zu, fließt nichts, und nichts wird warm. Steht es ganz offen, fließt viel, aber fast der ganze Druck fällt im engen Rohr ab und kaum
etwas am Ventil. Halb offen ist beides mittelgroß, und am Ventil wird am meisten Leistung frei.

:::herleitung
**Die Parabel.** Man setzt den Strom der Arbeitsgeraden in das Produkt aus Spannung und Strom ein und erhält die erste Formel.

**Der Scheitel.** Die Ableitung nach $U_{CE}$ verschwindet in der Mitte der Geraden:

$$\frac{dP}{dU_{CE}} = \frac{U_{CC} - 2\,U_{CE}}{R_C} = 0, \qquad U_{CE} = \frac{U_{CC}}{2}.$$

Dort fließt die Hälfte des größten Stroms, und die Leistung ist

$$P_\text{max} = \frac{U_{CC}}{2}\cdot\frac{U_{CC}}{2\,R_C} = \frac{U_{CC}^2}{4\,R_C}.$$

**Die Enden.** Gesperrt ist $I_C$ null. Gesättigt liegt $U_{CE,\text{sat}}$ an, und die Verlustleistung $P_\text{sat}$ in der Sättigung beträgt im Verhältnis
zum Scheitel

$$\frac{P_\text{sat}}{P_\text{max}} = \frac{4\,U_{CE,\text{sat}}\,(U_{CC} - U_{CE,\text{sat}})}{U_{CC}^2} \approx \frac{4\,U_{CE,\text{sat}}}{U_{CC}},$$

bei einer Versorgung von einigen Volt also ein kleiner Bruchteil. Im Bild: Am Ventil wird Druckabfall mal Durchfluss frei, und ganz offen ist der Druckabfall
winzig.
:::

::::beispiel Arbeitsgerade und Verlustleistung
Die Schaltung aus dem Beispiel des vorigen Artikels, der Kollektor über $R_C$ an der Versorgung, der Emitter an Masse:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega.$$

**Die Gerade** läuft von $(12\,\text{V}, 0)$ bis $(0, 6\,\text{mA})$:

$$I_C = \frac{12\,\text{V} - U_{CE}}{2\,\text{k}\Omega}.$$

**Die Leistung längs der Geraden,** an fünf Punkten:

| $U_{CE}$ | $2\,\text{V}$ | $4\,\text{V}$ | $6\,\text{V}$ | $8\,\text{V}$ | $10\,\text{V}$ |
|---|---|---|---|---|---|
| $I_C$ | $5\,\text{mA}$ | $4\,\text{mA}$ | $3\,\text{mA}$ | $2\,\text{mA}$ | $1\,\text{mA}$ |
| $P$ | $10\,\text{mW}$ | $16\,\text{mW}$ | $18\,\text{mW}$ | $16\,\text{mW}$ | $10\,\text{mW}$ |

Die Werte liegen symmetrisch um die Mitte, und der Scheitel ist

$$P_\text{max} = \frac{(12\,\text{V})^2}{4\cdot2\,\text{k}\Omega} = 18\,\text{mW}.$$

**Als Schalter.** Gesättigt fließen $5{,}9\,\text{mA}$ bei $0{,}2\,\text{V}$:

$$P_\text{sat} = 0{,}2\,\text{V}\cdot5{,}9\,\text{mA} = 1{,}18\,\text{mW}.$$

Das ist rund ein Fünfzehntel des Scheitels, wie die Näherung vorhersagt; gesperrt ist die Leistung null.

**Im Bild:** Halb offen wird das Ventil am wärmsten; ganz offen trägt das Rohr fast den ganzen Druck.
::::

:::grafik
Szene: get1/bipolartransistoren/02-verlustleistung · Vorlage: lastgerade-leistung
Unten das Ausgangskennlinienfeld $I_C$ über $U_{CE}$ bis $12\,\text{V}$ mit der Arbeitsgeraden von $(12\,\text{V}, 0)$ nach $(0, 6\,\text{mA})$, darüber mit
derselben Spannungsachse die Parabel der Verlustleistung mit dem Scheitel $18\,\text{mW}$ bei $6\,\text{V}$. Ein Punkt gleitet längs der Geraden; zu ihm
leuchtet auf der Parabel die momentane Leistung auf, und im Kennlinienfeld zeigt ein Rechteck aus $U_{CE}$ und $I_C$ dieselbe Leistung als Fläche. An den beiden
Enden markieren Symbole den Schalter, aus mit $0$ und ein mit $1{,}18\,\text{mW}$, in der Mitte ein Symbol den Verstärker. Kernaussage: Ein Schalter ruht an den
kühlen Enden der Geraden, ein Verstärker in ihrer heißen Mitte. (Rot = Arbeitspunkt und Rechteck, blau = Gerade und Parabel, orange = Punkte von Schalter und
Verstärker, grau = Achsen.)
:::

## Die linearen Ersatzschaltbilder

Für die Rechnung von Hand vereinfacht das Skript in Abschnitt 11.3 die Kennlinien des Transistors zu geraden Stücken, Bild 11.10, so wie im Artikel über den
Arbeitspunkt der Diode die Diode in Stufe 2:

- Die **Eingangskennlinie** ist links von $U_{BE,\text{ein}}$ die Achse ohne Strom und dort eine senkrechte Linie: Der Basis-Emitter-Übergang führt jeden Strom
  bei genau $0{,}6\,\text{V}$.
- Die **Steuerkennlinie** ist eine Gerade mit der Steigung $B$ bis zu einem Knick und danach waagrecht. Das Skript sagt, die Stromverstärkung sinke in der
  Sättigung auf null. Gemeint ist die Steigung, also wie viel Kollektorstrom ein zusätzlicher Basisstrom bringt; das Verhältnis $I_C/I_B$ selbst sinkt nur unter
  $B$. Der Knick ist auch keine Eigenschaft des Transistors allein: Er liegt dort, wo der Kollektorkreis nicht mehr Strom hergibt, in Bild 11.4 bei
  $(U_{CC} - U_{CE,\text{sat}})/R_C$. Das meint das Skript mit dem Satz, die Sättigung werde nur für große $I_B$ erreicht.
- Die **Ausgangskennlinie** besteht aus waagrechten Linien für die Basisströme, einer senkrechten Linie bei $U_{CE,\text{sat}}$ für die Sättigung und der Achse
  ohne Strom für den Sperrbereich.

Jedes dieser geraden Stücke gehört zu einem einfachen Schaltelement. Eine senkrechte Linie, auf der jeder Strom bei derselben Spannung möglich ist, beschreibt
eine ideale Spannungsquelle; eine waagrechte, auf der der Strom nicht von der Spannung abhängt, eine Stromquelle; die Achse ohne Strom einen offenen Anschluss.
So entstehen die drei __linearen Ersatzschaltbilder__ der Bilder 11.11 bis 11.13, eines je Arbeitsbereich. Im Sperrbereich sind alle drei Anschlüsse offen. Im
aktiven Bereich liegt zwischen Basis und Emitter eine Spannungsquelle von $0{,}6\,\text{V}$ und zwischen Kollektor und Emitter eine gesteuerte Stromquelle, die
das $B$-Fache des Basisstroms führt. In der Sättigung liegt zwischen Kollektor und Emitter stattdessen eine Spannungsquelle von $0{,}2\,\text{V}$. In allen
dreien fließen Basis- und Kollektorstrom im Emitter zusammen. Als Gleichungen der Elemente:

:::formel Definition
$$\begin{array}{lll} \text{Sperrbereich:} & I_B = 0, & I_C = 0, \\ \text{aktiver Bereich:} & U_{BE} = U_{BE,\text{ein}}, & I_C = B\,I_B, \\ \text{Sättigung:} & U_{BE} = U_{BE,\text{ein}}, & U_{CE} = U_{CE,\text{sat}}. \end{array}$$
:::

**So liest man das:** Mit diesen Elementen wird der Transistor für die Rechnung zu einem Stück lineares Netz aus Quellen, und jede Schaltung lässt sich mit
Maschen- und Knotenregel lösen wie in den Kapiteln 5 bis 9. Der Preis ist, dass man den Bereich vorher kennen muss. Man nimmt ihn deshalb an, rechnet und prüft
danach die Bedingungen aus dem vorigen Artikel: im aktiven Bereich $U_{CE} \ge U_{CE,\text{sat}}$,
in der Sättigung $I_C \le BI_B$,
im Sperrbereich $U_{BE} < U_{BE,\text{ein}}$. In den beiden leitenden Bereichen muss außerdem $I_B$ positiv sein, denn die Quelle zwischen Basis und Emitter
steht für einen Übergang in Durchlassrichtung, wie die Diode in Stufe 2.

**Im Bild:** Das Rückschlagventil hält genau seinen Öffnungsdruck, sobald Steuerwasser fließt. Das Regelventil ist im aktiven Bereich ein Durchflussregler, in
der Sättigung ein ganz offenes Ventil mit festem Restdruck, im Sperrbereich ein geschlossener Hahn.

:::herleitung
**Eingang.** Links von $U_{BE,\text{ein}}$ liegt die Eingangskennlinie auf der Achse: kein Strom bei jeder Spannung, also ein offener Anschluss. Rechts davon
ist sie senkrecht, jeder Strom bei derselben Spannung; das ist die Kennlinie einer idealen Spannungsquelle.

**Ausgang im aktiven Bereich.** Die waagrechten Linien sagen, dass der Kollektorstrom das $B$-Fache des Basisstroms ist, welche Spannung auch anliegt. Ein
Zweipol, dessen Strom nicht von seiner Spannung abhängt, ist eine Stromquelle; weil ihr Wert vom Basisstrom abhängt, ist sie nach dem Artikel über Zweitore
eine stromgesteuerte Stromquelle.

**Ausgang in der Sättigung und im Sperrbereich.** Die senkrechte Linie bei $U_{CE,\text{sat}}$ ist wieder eine Spannungsquelle. Im Sperrbereich sind beide
Ströme null und alle Anschlüsse offen.

**Emitterknoten.** In jedem Ersatzschaltbild fließen Basis- und Kollektorstrom im Emitter zusammen, damit die Knotenregel des Transistors gilt:

$$I_E = I_B + I_C.$$

Im Bild: Steuerwasser und Hauptstrom laufen hinter dem Ventil gemeinsam in den Abfluss.
:::

::::beispiel Welcher Bereich?
Die Schaltung von oben, mit einem Transistor der Stromverstärkung $200$:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega, \qquad B = 200.$$

An ihr werden drei Zustände gemessen. Welcher Bereich liegt jeweils vor?

**(a)** Basisstrom $40\,\mu\text{A}$, Kollektorstrom $5{,}9\,\text{mA}$. Im aktiven Bereich müssten es

$$B\,I_B = 200\cdot40\,\mu\text{A} = 8\,\text{mA}$$

sein. Es fließt weniger, also ist der Transistor gesättigt, und $U_{CE}$ beträgt $0{,}2\,\text{V}$. Im Ersatzschaltbild führt die Quelle zwischen Basis und
Emitter $40\,\mu\text{A}$, die zwischen Kollektor und Emitter $5{,}9\,\text{mA}$, und aus dem Emitter fließen $5{,}94\,\text{mA}$.

**(b)** Basisstrom $15\,\mu\text{A}$ bei $6\,\text{V}$ zwischen Kollektor und Emitter. Die Spannung liegt über $U_{CE,\text{sat}}$, und der Basisstrom ist
positiv: aktiver Bereich. Die Stromquelle führt

$$I_C = 200\cdot15\,\mu\text{A} = 3\,\text{mA},$$

und das passt zur Arbeitsgeraden, denn an $R_C$ fallen damit $6\,\text{V}$ ab. Aus dem Emitter fließen $3{,}015\,\text{mA}$.

**(c)** $-1\,\text{V}$ zwischen Basis und Emitter. Das liegt unter der Schwelle: Sperrbereich, alle Ströme null, und am Kollektor liegen die vollen
$12\,\text{V}$.

**Im Bild:** In (a) könnte das Ventil $8\,\text{mA}$ durchlassen, aber das Rohr liefert nur $5{,}9$; in (b) arbeitet ein halb offener Durchflussregler; in (c)
kommt kein Steuerwasser, und der Hahn ist zu.
::::

:::grafik
Szene: get1/bipolartransistoren/02-ersatzschaltbilder · Vorlage: transistor-ersatzschaltbilder
Oben die drei idealisierten Kennlinien von Bild 11.10 nebeneinander: der Eingang $I_B$ über $U_{BE}$ mit dem senkrechten Ast bei $0{,}6\,\text{V}$, die
Steuerkennlinie $I_C$ über $I_B$ mit der Steigung $B$ und dem waagrechten Ast ab dem Strom, den der Kollektorkreis höchstens liefert, und das
Ausgangskennlinienfeld mit waagrechten Ästen und der senkrechten Linie bei $0{,}2\,\text{V}$. Darunter die drei Ersatzschaltbilder: offene Anschlüsse; eine
Quelle von $0{,}6\,\text{V}$ zwischen B und E und eine gesteuerte Stromquelle $BI_B$ zwischen C und E; Quellen von $0{,}6\,\text{V}$ und $0{,}2\,\text{V}$; jeweils
mit dem Emitterknoten und den Zählpfeilen von $I_B$, $I_C$ und $I_E$. Ein Umschalter wählt den Bereich, dann leuchten das passende gerade Stück jeder Kennlinie
und das zugehörige Element auf. Ein Regler für $R_C$ verschiebt den Knick der Steuerkennlinie. Kernaussage: Jedes gerade Stück einer Kennlinie wird zu einer
Quelle oder einem offenen Anschluss. (Rot = Ersatzelemente, blau = Kennlinien, orange = Knick und Bereichsgrenzen, grau = Achsen.)
:::

## Den Arbeitspunkt berechnen: Annahme und Probe

Mit den Ersatzschaltbildern lässt sich der Arbeitspunkt der Schaltung von Bild 11.4 ausrechnen, wie es das Skript in Abschnitt 11.2 vorführt.

**Die drei Akteure:**

- der Eingangskreis: die Eingangsspannung $U_\text{ein}$ in Volt, die über den Basiswiderstand $R_B$ in Ohm den Basisstrom treibt;
- der Transistor als Ersatzschaltbild des angenommenen Bereichs, mit der Stromverstärkung $B$ ohne Einheit, der Schwelle $U_{BE,\text{ein}}$ von
  $0{,}6\,\text{V}$ und der Sättigungsspannung $U_{CE,\text{sat}}$ von $0{,}2\,\text{V}$;
- der Kollektorkreis aus $U_{CC}$ und $R_C$, also die Arbeitsgerade.

**Das Zusammenspiel:** *Welcher Bereich liegt vor, und welche Ströme und Spannungen stellen sich ein?*

Ist $U_\text{ein}$ höchstens $U_{BE,\text{ein}}$, sperrt der Transistor: Es fließt kein Basisstrom, an $R_B$ fällt nichts ab, und $U_{BE}$ ist gleich
$U_\text{ein}$, also tatsächlich nicht über der Schwelle. Ist $U_\text{ein}$ größer, leitet der Basis-Emitter-Übergang, im aktiven Bereich wie in der Sättigung,
und der Basisstrom ist in beiden derselbe. Nimmt man den aktiven Bereich an, folgt der Arbeitspunkt:

:::formel
$$I_B = \frac{U_\text{ein} - U_{BE,\text{ein}}}{R_B}, \qquad I_C = B\,I_B, \qquad U_{CE} = U_{CC} - B\,R_C\,I_B.$$
:::

**So liest man das:** Eingaben sind die Werte der Schaltung, Ausgaben die drei Größen des Arbeitspunkts. Die erste Gleichung gilt in beiden leitenden Bereichen,
die beiden anderen nur im aktiven. Die Probe verlangt, dass $U_{CE}$ mindestens $U_{CE,\text{sat}}$ beträgt. Fällt sie durch, ist der Transistor gesättigt, und
es gilt:

$$U_{CE} = U_{CE,\text{sat}}, \qquad I_C = \frac{U_{CC} - U_{CE,\text{sat}}}{R_C}.$$

Die Grenze zwischen beiden Bereichen liegt dort, wo das $B$-Fache des Basisstroms gerade so groß ist wie der Strom, den der Kollektorkreis in der Sättigung
liefert.

**Im Bild:** Der Eingangsdruck treibt das Steuerwasser durch das enge Steuerrohr $R_B$ gegen den Öffnungsdruck des Rückschlagventils. Das Regelventil verlangt
das $B$-Fache als Hauptstrom, und das Manometer zeigt den Turmdruck minus dem, was das Rohr dafür verbraucht. Gibt das Rohr so viel nicht her, steht das Ventil
ganz offen.

:::herleitung
**Sperrbereich.** Ohne Basisstrom fällt an $R_B$ nichts ab, und die Masche des Eingangs ergibt, dass $U_{BE}$ gleich $U_\text{ein}$ ist. Das ist
widerspruchsfrei, solange $U_\text{ein}$ die Schwelle nicht überschreitet.

**Eingangsmasche.** In beiden leitenden Bereichen liegt zwischen Basis und Emitter die Quelle $U_{BE,\text{ein}}$. Die Masche aus Eingangsspannung, $R_B$ und
dieser Quelle lautet

$$U_\text{ein} = R_B\,I_B + U_{BE,\text{ein}}.$$

Nach $I_B$ aufgelöst ergibt sich die erste Formel. Die Probe, dass $I_B$ positiv ist, verlangt eine Eingangsspannung über der Schwelle.

**Aktiver Bereich.** Die Stromquelle führt das $B$-Fache des Basisstroms, und die Arbeitsgerade ergibt die Spannung.

**Sättigung.** Zwischen Kollektor und Emitter liegt die Quelle $U_{CE,\text{sat}}$, und die Arbeitsgerade an dieser Stelle ergibt den Strom.

**Genau einer der beiden.** Setzt man die Formeln ein, lauten die Probe des aktiven Bereichs und die der Sättigung:

$$B\,I_B \le \frac{U_{CC} - U_{CE,\text{sat}}}{R_C}, \qquad \frac{U_{CC} - U_{CE,\text{sat}}}{R_C} \le B\,I_B.$$

Für jeden Basisstrom gilt genau eine der beiden Ungleichungen, an der Grenze beide mit demselben Ergebnis. Der Arbeitspunkt ist also eindeutig, und eine falsche
Annahme verrät sich immer durch eine verletzte Probe. Im Bild: Entweder liefert das Rohr, was das Ventil verlangt, oder das Ventil steht ganz offen; beides
zugleich gibt es nur an der Grenze.
:::

::::beispiel Ein Basiswiderstand, drei Fälle
Die Schaltung von oben, jetzt mit Basiswiderstand und einer Eingangsspannung von $5\,\text{V}$:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega, \qquad B = 200, \qquad U_\text{ein} = 5\,\text{V}.$$

**(a) Mit $470\,\text{k}\Omega$, zuerst falsch geraten.** Der Basisstrom ist in beiden leitenden Bereichen

$$I_B = \frac{5\,\text{V} - 0{,}6\,\text{V}}{470\,\text{k}\Omega} = 9{,}36\,\mu\text{A}.$$

Angenommen, der Transistor sei gesättigt. Dann flössen $5{,}9\,\text{mA}$; die Probe verlangt aber, dass das höchstens

$$B\,I_B = 200\cdot9{,}36\,\mu\text{A} = 1{,}87\,\text{mA}$$

ist, ein Widerspruch. Also aktiver Bereich:

$$I_C = 1{,}87\,\text{mA}, \qquad U_{CE} = 12\,\text{V} - 2\,\text{k}\Omega\cdot1{,}87\,\text{mA} = 8{,}26\,\text{V}.$$

Die Probe hält, denn $8{,}26\,\text{V}$ liegt über $0{,}2\,\text{V}$.

**(b) Mit $100\,\text{k}\Omega$.** Jetzt fließen $44\,\mu\text{A}$ in die Basis. Angenommen aktiv:

$$I_C = 200\cdot44\,\mu\text{A} = 8{,}8\,\text{mA}, \qquad U_{CE} = 12\,\text{V} - 17{,}6\,\text{V} = -5{,}6\,\text{V}.$$

Das liegt unter $0{,}2\,\text{V}$, ein Widerspruch. Also Sättigung mit $5{,}9\,\text{mA}$, und diese Probe hält, denn das ist weniger als $8{,}8\,\text{mA}$.

**(c) Mit $0{,}5\,\text{V}$ am Eingang.** Unter der Schwelle: Sperrbereich, $U_{BE}$ beträgt $0{,}5\,\text{V}$, und $U_{CE}$ beträgt $12\,\text{V}$.

**Die Grenze.** Gesättigt ist der Transistor ab einem Basisstrom von $5{,}9\,\text{mA}/200$, also $29{,}5\,\mu\text{A}$; bei $5\,\text{V}$ am Eingang ist das
für Basiswiderstände bis $149\,\text{k}\Omega$ der Fall.

**Im Bild:** Ein enges Steuerrohr lässt wenig Steuerwasser durch, und das Ventil steht halb offen; ein weites lässt so viel durch, dass das Ventil ganz aufgeht.
::::

Bild 11.5 des Skripts legt die Eingangsspannung ohne Vorwiderstand unmittelbar an die Basis und setzt dafür einen __Emitterwiderstand__ $R_E$ zwischen Emitter
und Masse. Für eine Eingangsspannung über der Schwelle kann der Transistor dann nicht sperren, wie das Skript bemerkt: Was die Eingangsspannung über
$U_{BE,\text{ein}}$ hinaus hat, muss an $R_E$ abfallen, und dafür braucht es Strom. Die Eingangsmasche führt jetzt durch $R_E$, und im aktiven Bereich folgt:

:::formel
$$I_E = \frac{U_\text{ein} - U_{BE,\text{ein}}}{R_E}, \qquad I_C = \frac{B}{B + 1}\,I_E.$$
:::

**So liest man das:** Eingangsspannung und Emitterwiderstand legen den Emitterstrom fest, und $B$ kommt darin nicht vor. $B$ entscheidet nur, wie sich der
Emitterstrom auf Basis und Kollektor aufteilt; weil $B/(B + 1)$ fast eins ist, ist $I_C$ fast $I_E$. Die Probe des aktiven Bereichs lautet nun, mit der Masche
des Ausgangs über $R_C$ und $R_E$:

$$U_{CE} = U_{CC} - R_C\,I_C - R_E\,I_E \ge U_{CE,\text{sat}}.$$

Im Zahlenbeispiel des Skripts steht hinter dem Emitterstrom die Ungleichung „$< B\cdot I_B$“. Sie gehört dort nicht hin, denn $BI_B$ ist gerade $I_C$ und damit
etwas kleiner als $I_E$. In der Zeile danach fehlt eine Klammer: Gemeint ist $I_B\,(B + 1)$, nicht $I_B\cdot B + 1$.

**Im Bild:** Hinter dem Regelventil sitzt jetzt ein enges Abflussrohr. Die Steuerleitung hängt an festem Druck, und das Rückschlagventil hält seinen
Öffnungsdruck; also steht am Abflussrohr immer derselbe Druck, und durch es fließt immer gleich viel ab, wie auch das Ventil übersetzt. Die Übersetzung bestimmt
nur, welcher kleine Teil davon Steuerwasser ist.

:::herleitung
**Eingangsmasche.** Von der Eingangsspannung über die Basis-Emitter-Strecke und $R_E$ nach Masse:

$$U_\text{ein} = U_{BE,\text{ein}} + R_E\,I_E.$$

Nach $I_E$ aufgelöst ergibt sich die erste Formel.

**Aufteilung.** Mit der Knotenregel und der gesteuerten Stromquelle ist

$$I_E = I_B + B\,I_B = (B + 1)\,I_B, \qquad I_C = B\,I_B = \frac{B}{B + 1}\,I_E.$$

**Ausgangsmasche.** Von $U_{CC}$ über $R_C$, die Kollektor-Emitter-Strecke und $R_E$ nach Masse:

$$U_{CC} = R_C\,I_C + U_{CE} + R_E\,I_E.$$

**Warum der Transistor nicht sperrt.** Wäre der Emitterstrom null, fiele an $R_E$ nichts ab, und die ganze Eingangsspannung läge zwischen Basis und Emitter,
mehr als die Schwelle; das widerspricht dem Sperrbereich. Im Bild: Steht am Rückschlagventil mehr als sein Öffnungsdruck, öffnet es, und es fließt so viel, bis
das Abflussrohr den Überschuss trägt.
:::

::::beispiel Ein Emitterwiderstand verdrängt B
Jetzt liegt die Eingangsspannung unmittelbar an der Basis, und ein Emitterwiderstand führt nach Masse:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega, \qquad R_E = 1\,\text{k}\Omega, \qquad U_\text{ein} = 2{,}6\,\text{V}.$$

**Der Emitterstrom** folgt ohne $B$:

$$I_E = \frac{2{,}6\,\text{V} - 0{,}6\,\text{V}}{1\,\text{k}\Omega} = 2\,\text{mA}.$$

**Drei Exemplare** mit verschiedener Stromverstärkung; die Spannung folgt aus der Ausgangsmasche:

| $B$ | $I_B$ | $I_C$ | $U_{CE}$ |
|---|---|---|---|
| $100$ | $19{,}8\,\mu\text{A}$ | $1{,}980\,\text{mA}$ | $6{,}04\,\text{V}$ |
| $200$ | $9{,}95\,\mu\text{A}$ | $1{,}990\,\text{mA}$ | $6{,}02\,\text{V}$ |
| $400$ | $4{,}99\,\mu\text{A}$ | $1{,}995\,\text{mA}$ | $6{,}01\,\text{V}$ |

Für das mittlere Exemplar etwa:

$$U_{CE} = 12\,\text{V} - 2\,\text{k}\Omega\cdot1{,}990\,\text{mA} - 1\,\text{k}\Omega\cdot2\,\text{mA} = 6{,}02\,\text{V}.$$

Die Probe hält in allen drei Fällen. Vervierfacht sich $B$, ändert sich der Kollektorstrom um weniger als ein Prozent; mit dem Basiswiderstand des vorigen
Beispiels hätte er sich vervierfacht.

**Im Bild:** Drei Ventile, die verschieden übersetzen, am selben Abflussrohr: Der Durchfluss ist fast derselbe, nur das Steuerwasser ist verschieden.
::::

## Den Arbeitspunkt in die Mitte legen

Für einen Verstärker soll der Arbeitspunkt nach dem Skript in der __Mitte des aktiven Bereichs__ liegen. Längs der Arbeitsgeraden reicht dieser Bereich von der
Sättigung bei $U_{CE,\text{sat}}$ bis zum Sperren bei $U_{CC}$. Ein Signal lässt $U_{CE}$ um den Arbeitspunkt schwanken, und die größte Schwankung ohne
Abschneiden hat Platz, wenn beide Grenzen gleich weit entfernt sind:

:::formel
$$U_{CE,\text{AP}} = \frac{U_{CC} + U_{CE,\text{sat}}}{2}, \qquad I_{C,\text{AP}} = \frac{U_{CC} - U_{CE,\text{sat}}}{2\,R_C}.$$
:::

**So liest man das:** Die erste Formel ist die Mitte zwischen beiden Grenzen, die zweite der zugehörige Strom auf der Arbeitsgeraden. Die Schwankung darf dann
einen Scheitelwert von $(U_{CC} - U_{CE,\text{sat}})/2$ haben. Für die Schaltung mit Basiswiderstand folgt daraus, wie das Skript vorrechnet, erst der
Basisstrom über $B$ und dann der Widerstand:

$$R_B = \frac{B\,(U_\text{ein} - U_{BE,\text{ein}})}{I_{C,\text{AP}}}.$$

Diese Rechnung hat einen Haken: Der Widerstand ist für ein bestimmtes $B$ berechnet. Ein anderes Exemplar setzt mit demselben $R_B$ einen ganz anderen
Arbeitspunkt, denn sein Kollektorstrom ist proportional zu seinem $B$. Das zeigt das Beispiel, und davon handeln die nächsten drei Abschnitte.

**Im Bild:** Das Manometer soll in Ruhe genau zwischen vollem Turmdruck und Restdruck stehen; dann kann es nach oben und unten gleich weit ausschlagen.

:::herleitung
**Die Grenzen.** Steigt der Kollektorstrom, sinkt $U_{CE}$ längs der Geraden bis $U_{CE,\text{sat}}$; dann sättigt der Transistor, und $U_{CE}$ sinkt nicht
weiter. Sinkt der Strom bis null, steigt $U_{CE}$ bis $U_{CC}$; dann sperrt er. Eine Schwankung mit dem Scheitelwert $\hat U$ um den Arbeitspunkt bleibt
unverzerrt, solange beide Abstände reichen:

$$\hat U \le U_{CC} - U_{CE,\text{AP}}, \qquad \hat U \le U_{CE,\text{AP}} - U_{CE,\text{sat}}.$$

**Die beste Lage.** Der erste Abstand nimmt ab, wenn der Arbeitspunkt nach rechts rückt, der zweite nimmt zu. Die kleinere der beiden Schranken ist deshalb dort
am größten, wo beide gleich sind. Gleichsetzen ergibt $U_{CE,\text{AP}}$ und den größten Scheitelwert:

$$\hat U_\text{max} = \frac{U_{CC} - U_{CE,\text{sat}}}{2}.$$

**Strom und Widerstand.** Die Arbeitsgerade bei $U_{CE,\text{AP}}$ ergibt $I_{C,\text{AP}}$. Der Basisstrom ist der $B$-te Teil davon, und nach der
Eingangsmasche ist $R_B$ der Quotient aus der Spannung $U_\text{ein} - U_{BE,\text{ein}}$ und diesem Basisstrom. Im Bild: Man schneidet das Steuerrohr so zu,
dass das Ventil halb offen steht, und zwar für genau dieses Ventil.
:::

::::beispiel Die Mitte einstellen und ein anderes Exemplar einsetzen
Die Schaltung mit Basiswiderstand, ausgelegt für $B = 200$:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega, \qquad U_\text{ein} = 5\,\text{V}.$$

**Die Mitte.**

$$U_{CE,\text{AP}} = \frac{12\,\text{V} + 0{,}2\,\text{V}}{2} = 6{,}1\,\text{V}, \qquad I_{C,\text{AP}} = \frac{12\,\text{V} - 6{,}1\,\text{V}}{2\,\text{k}\Omega} = 2{,}95\,\text{mA}.$$

Der Scheitelwert der Schwankung darf bis $5{,}9\,\text{V}$ betragen.

**Der Basiswiderstand.** Der Basisstrom ist $2{,}95\,\text{mA}/200$, also $14{,}75\,\mu\text{A}$:

$$R_B = \frac{5\,\text{V} - 0{,}6\,\text{V}}{14{,}75\,\mu\text{A}} = 298\,\text{k}\Omega.$$

Der nächste Normwert ist $300\,\text{k}\Omega$; damit fließen $14{,}67\,\mu\text{A}$ und $2{,}93\,\text{mA}$, und $U_{CE}$ beträgt $6{,}13\,\text{V}$.

**Andere Exemplare.** Angenommen, $B$ streut zwischen $100$ und $400$. Derselbe Widerstand ergibt:

| $B$ | $I_C$ | $U_{CE}$ | größter Scheitelwert |
|---|---|---|---|
| $100$ | $1{,}47\,\text{mA}$ | $9{,}07\,\text{V}$ | $2{,}93\,\text{V}$ |
| $200$ | $2{,}93\,\text{mA}$ | $6{,}13\,\text{V}$ | $5{,}87\,\text{V}$ |
| $400$ | $5{,}87\,\text{mA}$ | $0{,}27\,\text{V}$ | $0{,}07\,\text{V}$ |

Der größte Scheitelwert ist jeweils der kleinere der beiden Abstände zu $12\,\text{V}$ und zu $0{,}2\,\text{V}$. Mit $B = 400$ liegt der Arbeitspunkt am Rand der
Sättigung, und ab $B$ von etwa $402$ sättigt der Transistor ganz.

**Im Bild:** Das Steuerrohr ist für ein bestimmtes Ventil zugeschnitten; ein Ventil, das doppelt so stark übersetzt, steht damit fast ganz offen.
::::

:::grafik
Szene: get1/bipolartransistoren/02-mitte-und-streuung · Vorlage: lastgerade-transistor
Das Ausgangskennlinienfeld mit der Arbeitsgeraden für $U_{CC} = 12\,\text{V}$ und $R_C = 2\,\text{k}\Omega$, darauf der Arbeitspunkt in der Mitte bei
$6{,}1\,\text{V}$, mit zwei gleich langen Pfeilen für den Spielraum nach oben und unten. Ein Umschalter wählt die Schaltung: Basiswiderstand von
$300\,\text{k}\Omega$ an $5\,\text{V}$ oder Emitterwiderstand von $1\,\text{k}\Omega$ an $2{,}6\,\text{V}$, mit der zugehörigen Arbeitsgeraden. Ein Regler für $B$
von $100$ bis $450$ bewegt den Arbeitspunkt: mit Basiswiderstand rast er über die Gerade bis in die Sättigung, und ein Pfeil schrumpft auf fast nichts; mit
Emitterwiderstand bleibt er fast stehen. Kernaussage: Was nur über $B$ eingestellt ist, wandert mit $B$. (Rot = Arbeitspunkt, blau = Gerade und Kennlinien,
orange = Spielraum, grau = Achsen.)
:::

## Warum der Arbeitspunkt wandert

Das Skript nennt zwei Gründe, den Kollektorstrom nicht über $B$ festzulegen. Erstens streut $B$ in der Fertigung stark. Zweitens reagiert $I_C$ sehr
empfindlich auf die Eingangsspannung des Transistors, $U_{BE}$, und diese hängt stark von der Temperatur ab. Wie sehr eine Streuung von $B$ durchschlägt, misst
die __Empfindlichkeit__ $S_B$: die relative Änderung des Kollektorstroms, geteilt durch die relative Änderung von $B$, die sie verursacht.

$$S_B = \frac{\Delta I_C / I_C}{\Delta B / B}.$$

**So liest man das:** Das ist eine Definition, gemeint für kleine Änderungen. Eine Empfindlichkeit von eins heißt: zehn Prozent mehr $B$, zehn Prozent mehr
Strom. Eine Empfindlichkeit nahe null heißt, dass $B$ keine Rolle spielt. Mit dem bloßen Basiswiderstand ist sie eins, mit dem Emitterwiderstand an einer
festen Eingangsspannung nur $1/(B + 1)$.

Gegen die Erwärmung helfen dagegen beide Widerstände. Bei festem Strom sinkt $U_{BE}$ mit ihr, wie bei der Diode um rund $1{,}8\,\text{mV}$ je Kelvin. Hält eine
Spannungsquelle $U_{BE}$ fest, steigt der Kollektorstrom deshalb nach dem vorigen Artikel um etwa $7\,\%$ je Kelvin. Mit Basis- oder Emitterwiderstand liegt aber
nicht $U_{BE}$ fest, sondern die Eingangsspannung. Die Verschiebung von $U_{BE}$ ändert dann nur die Spannung $U_R$ am Widerstand ein wenig, und für den Strom
$I$ durch ihn gilt:

$$\frac{\Delta I}{I} = -\frac{\Delta U_{BE}}{U_R}.$$

**So liest man das:** Je mehr Spannung am Widerstand liegt, desto weniger macht die Verschiebung von $U_{BE}$ aus. Beim Basiswiderstand ist der Strom durch ihn
der Basisstrom, beim Emitterwiderstand der Emitterstrom. Beim Basiswiderstand kommt allerdings hinzu, dass sich auch $B$ mit der Temperatur ändert und dort voll
durchschlägt.

Beide Mängel behebt eine __Gegenkopplung__. Dabei führt die Schaltung eine Größe, die vom Kollektorstrom abhängt, so auf den Eingang des Transistors zurück, dass
sie jeder Änderung dieses Stroms entgegenwirkt. Hängt die zurückgeführte Größe vom Ausgangsstrom ab, spricht man von __Stromgegenkopplung__, hängt sie von der
Ausgangsspannung ab, von __Spannungsgegenkopplung__. Der Emitterwiderstand ist schon eine Stromgegenkopplung: Die Spannung an ihm wächst mit dem Strom und zieht
von der festen Eingangsspannung ab, was für $U_{BE}$ bleibt. Das Skript stellt in Abschnitt 11.2 je eine Schaltung beider Arten vor; das Temperaturproblem im
Ganzen verweist es an das Fach Schaltungstechnik 2.

**Im Bild:** Ohne Rückmeldung macht ein Ventil, das stärker übersetzt oder warm wird, einfach weiter auf. Mit Rückmeldung drosselt der größere Hauptstrom seinen
eigenen Steuerstrom, bis der Durchfluss fast wieder stimmt.

:::herleitung
**Bloßer Basiswiderstand.** Der Basisstrom hängt nicht von $B$ ab, und der Kollektorstrom ist sein $B$-Faches. Jede relative Änderung von $B$ ändert $I_C$ um
denselben Anteil, also ist die Empfindlichkeit eins.

**Emitterwiderstand an fester Eingangsspannung.** Der Emitterstrom hängt nicht von $B$ ab, und $I_C$ ist $I_E$ mal $B/(B + 1)$. Die Ableitung dieses Faktors
nach $B$ ist

$$\frac{d}{dB}\,\frac{B}{B + 1} = \frac{(B + 1) - B}{(B + 1)^2} = \frac{1}{(B + 1)^2}.$$

Eine kleine Änderung von $B$ ändert $I_C$ deshalb relativ um

$$\frac{\Delta I_C}{I_C} = \frac{\Delta B}{(B + 1)^2}\cdot\frac{B + 1}{B} = \frac{1}{B + 1}\cdot\frac{\Delta B}{B}.$$

Der Faktor vor der relativen Änderung von $B$ ist die Empfindlichkeit.

**Temperatur.** In beiden Schaltungen ist der Strom durch den Widerstand der Quotient aus der Spannung an ihm und dem Widerstand, und diese Spannung ist die
Eingangsspannung minus $U_{BE}$. Ändert sich $U_{BE}$ um $\Delta U_{BE}$, ändert sich die Spannung am Widerstand um das Negative davon, und der Strom ändert
sich relativ um denselben Anteil wie diese Spannung. Im Bild: Ein Rohr, an dem viel Druck liegt, merkt kaum, wenn sich der Öffnungsdruck des Rückschlagventils
um eine Kleinigkeit verschiebt.
:::

::::beispiel Streuung und Erwärmung in Zahlen
Die beiden Schaltungen der vorigen Beispiele: der Basiswiderstand mit $4{,}4\,\text{V}$ an $R_B$ und der Emitterwiderstand mit $2\,\text{V}$ an $R_E$, beide mit
einem Transistor der Stromverstärkung $200$.

**(a) Zehn Prozent mehr $B$.** Mit dem Basiswiderstand steigt $I_C$ um zehn Prozent. Mit dem Emitterwiderstand ändert sich nur der Faktor:

$$\frac{200}{201} = 0{,}99502, \qquad \frac{220}{221} = 0{,}99548.$$

Das sind $0{,}045\,\%$, wie die Empfindlichkeit $1/201$ vorhersagt.

**(b) Zwanzig Kelvin wärmer.** Dann verschiebt sich $U_{BE}$ um $-36\,\text{mV}$. Hielte eine Quelle $U_{BE}$ fest, wüchse der Strom wie bei einer um
$36\,\text{mV}$ größeren Spannung, mit der Temperaturspannung bei Raumtemperatur gerechnet:

$$\exp\frac{36\,\text{mV}}{25{,}85\,\text{mV}} \approx 4.$$

Mit den Widerständen dagegen:

$$\frac{\Delta I_B}{I_B} = \frac{36\,\text{mV}}{4{,}4\,\text{V}} = 0{,}8\,\%, \qquad \frac{\Delta I_E}{I_E} = \frac{36\,\text{mV}}{2\,\text{V}} = 1{,}8\,\%.$$

Beim Basiswiderstand kommt die Änderung von $B$ mit der Temperatur noch voll hinzu, beim Emitterwiderstand nur mit dem winzigen Faktor aus (a).

**Im Bild:** Ein fest eingestellter Steuerdruck lässt das warme Ventil weit aufgehen; ein Steuerrohr mit viel Druck darauf oder ein Abflussrohr mit Gegendruck
merkt die Erwärmung kaum.
::::

## Stromgegenkopplung mit Basisspannungsteiler

Der Emitterwiderstand braucht eine feste Spannung an der Basis. Eine echte Schaltung hat meist nur die Versorgung; die Basisspannung erzeugt man deshalb mit
einem __Basisspannungsteiler__, Bild 11.6 des Skripts: $R_1$ führt von $U_{CC}$ zur Basis, $R_2$ von der Basis nach Masse. Für die Basis ist dieser Teiler nach
dem Artikel über Ersatzquellen eine Ersatzspannungsquelle, Bild 11.7, mit der Leerlaufspannung $U_q$ und dem Innenwiderstand $R_i$:

$$U_q = U_{CC}\,\frac{R_2}{R_1 + R_2}, \qquad R_i = R_1 \parallel R_2 = \frac{R_1\,R_2}{R_1 + R_2}.$$

Damit vereint die Schaltung beide vorigen: eine Quelle mit Vorwiderstand an der Basis wie in Bild 11.4 und einen Emitterwiderstand wie in Bild 11.5. Die
Eingangsmasche ergibt die Gleichung 11.1 des Skripts:

:::formel
$$I_C = \frac{U_q - U_{BE}}{R_E\,\Big(1 + \dfrac{1}{B}\Big) + \dfrac{R_i}{B}}.$$
:::

**So liest man das:** Eingaben sind die Werte der Schaltung, Ausgabe der Kollektorstrom im aktiven Bereich. $B$ steht nur in den beiden kleinen Gliedern des
Nenners, $R_E/B$ und $R_i/B$. Ist $R_E$ viel größer als $R_i/B$, fallen beide kaum ins Gewicht, und es bleibt die Näherung des Skripts; mit $B$ um $100$ steht
dort $1{,}01\,R_E$ im Nenner:

$$I_C \approx \frac{U_q - U_{BE}}{R_E}.$$

Die Bedingung heißt in Worten: Der Spannungsabfall des Basisstroms am Innenwiderstand des Teilers ist klein gegen den des Emitterstroms an $R_E$. Die Praxis
drückt das mit einer Faustregel über den __Querstrom__ aus, den Strom durch den Teiler: Er soll mindestens zehnmal so groß sein wie der Basisstrom; dann sinkt
die Spannung an der Basis unter Last um weniger als ein Zehntel. Wie stark $B$ noch wirkt, sagt die Empfindlichkeit:

$$S_B = \frac{R_E + R_i}{(B + 1)\,R_E + R_i}.$$

Ohne Emitterwiderstand ist sie eins wie beim bloßen Basiswiderstand, ohne Innenwiderstand $1/(B + 1)$ wie bei fester Eingangsspannung; jede Schaltung mit
Teiler liegt dazwischen. Gegen die Temperatur hilft der Teiler wie der Emitterwiderstand: Eine Verschiebung von $U_{BE}$ ändert den Strom relativ um ihren
Anteil an $U_q - U_{BE}$.

Das Skript vereinfacht danach weiter zu $U_{CC}R_2/(R_E(R_1 + R_2))$, also $U_q/R_E$, und lässt damit $U_{BE}$ weg. Das ist nur richtig, wenn $U_q$ viel größer
ist als $0{,}6\,\text{V}$. In üblichen Schaltungen liegt $U_q$ aber bei wenigen Volt, damit am Kollektor Spannung für das Signal bleibt, und dann ist dieser
Schritt ein grober Fehler; man behält $U_{BE}$.

Der Regelkreis Schritt für Schritt:

**Schritt 1** — Der Kollektorstrom steigt, etwa weil ein Exemplar stärker verstärkt oder der Transistor warm wird.

**Schritt 2** — Mit ihm steigt der Emitterstrom und damit die Spannung an $R_E$; das Potenzial des Emitters hebt sich.

**Schritt 3** — Das Potenzial der Basis hält der Teiler fast fest. Also sinkt $U_{BE}$, der Unterschied der beiden Potenziale.

**Schritt 4** — Ein kleineres $U_{BE}$ lässt weniger Strom fließen, und der Anstieg aus Schritt 1 wird zum größten Teil zurückgenommen.

Im linearen Modell ist $U_{BE}$ fest; dort zeigt sich dieselbe Regelung darin, dass der Emitterstrom fast nicht von $B$ abhängt. In Wirklichkeit genügen wenige
Millivolt weniger an $U_{BE}$, denn der Strom hängt exponentiell von ihr ab.

**Im Bild:** Die Steuerleitung zapft über einen Druckteiler aus zwei engen Rohren einen mittleren Druck vom Turm ab, und hinter dem Ventil sitzt das enge
Abflussrohr. Fließt mehr, steigt der Gegendruck hinter dem Ventil, am Rückschlagventil bleibt weniger Druck, und das Steuerwasser wird knapper.

:::herleitung
**Die Ersatzquelle.** Ohne Basisstrom ist der Teiler unbelastet, und an $R_2$ liegt der Anteil $R_2/(R_1 + R_2)$ der Versorgung; das ist $U_q$. Für den
Innenwiderstand legt man $U_{CC}$ still, also als Kurzschluss. Dann führen $R_1$ und $R_2$ beide von der Basis nach Masse und liegen parallel.

**Eingangsmasche.** Von $U_q$ über $R_i$, die Basis-Emitter-Strecke und $R_E$ nach Masse, mit dem Emitterstrom $(1 + B)\,I_B$:

$$U_q = R_i\,I_B + U_{BE} + (1 + B)\,R_E\,I_B, \qquad I_B = \frac{U_q - U_{BE}}{(1 + B)\,R_E + R_i}.$$

**Kollektorstrom.** Man multipliziert mit $B$ und teilt Zähler und Nenner durch $B$; das ergibt Formel (5).

**Die Näherung.** Ist $B$ groß gegen eins und $R_E$ groß gegen $R_i/B$, ist der Nenner fast $R_E$, und es bleibt der Quotient aus $U_q - U_{BE}$ und $R_E$.

**Empfindlichkeit.** Der Logarithmus des Kollektorstroms ist eine Summe:

$$\ln I_C = \ln B + \ln(U_q - U_{BE}) - \ln\big((1 + B)\,R_E + R_i\big).$$

Die relative Änderung je relativer Änderung von $B$ ist die Ableitung nach $\ln B$, also $B$ mal die Ableitung nach $B$:

$$S_B = 1 - \frac{B\,R_E}{(1 + B)\,R_E + R_i} = \frac{R_E + R_i}{(1 + B)\,R_E + R_i}.$$

**Querstrom.** Unbelastet fließt durch den Teiler der Querstrom $I_q$, der Quotient aus $U_{CC}$ und $R_1 + R_2$, und $U_q$ ist $R_2$ mal $I_q$. Unter Last
sinkt die Basisspannung um $R_i$ mal $I_B$, relativ also um

$$\frac{R_i\,I_B}{U_q} = \frac{I_B}{I_q}\cdot\frac{R_1}{R_1 + R_2} < \frac{I_B}{I_q}.$$

Ist der Querstrom mindestens zehnmal so groß wie der Basisstrom, bleibt der Rückgang unter einem Zehntel.

**Temperatur.** Nach Formel (5) ist der Kollektorstrom proportional zu $U_q - U_{BE}$; eine Verschiebung von $U_{BE}$ ändert ihn deshalb relativ um ihren
Anteil an dieser Spannung, mit umgekehrtem Vorzeichen. Im Bild: Je fester der abgezapfte Druck steht und je stärker das Abflussrohr gegen eine Änderung drückt,
desto weniger zählt die Übersetzung des Ventils.
:::

::::beispiel Ein Basisspannungsteiler mit Emitterwiderstand
Der Teiler ersetzt die feste Eingangsspannung des Beispiels mit Emitterwiderstand:

$$U_{CC} = 12\,\text{V}, \qquad R_1 = 33\,\text{k}\Omega, \qquad R_2 = 10\,\text{k}\Omega, \qquad R_C = 2\,\text{k}\Omega, \qquad R_E = 1\,\text{k}\Omega.$$

**Die Ersatzquelle.**

$$U_q = 12\,\text{V}\cdot\frac{10}{43} = 2{,}791\,\text{V}, \qquad R_i = \frac{33\cdot10}{43}\,\text{k}\Omega = 7{,}67\,\text{k}\Omega.$$

**Der Kollektorstrom** nach Formel (5), für $B = 200$:

$$I_C = \frac{2{,}791\,\text{V} - 0{,}6\,\text{V}}{1\,\text{k}\Omega\cdot1{,}005 + 38{,}4\,\Omega} = 2{,}100\,\text{mA}.$$

Dazu fließen $10{,}5\,\mu\text{A}$ Basisstrom, und die Ausgangsmasche ergibt $5{,}69\,\text{V}$ zwischen Kollektor und Emitter: aktiv, nahe der Mitte.

**Drei Exemplare.**

| $B$ | $I_C$ | $U_{CE}$ | $S_B$ |
|---|---|---|---|
| $100$ | $2{,}016\,\text{mA}$ | $5{,}93\,\text{V}$ | $0{,}080$ |
| $200$ | $2{,}100\,\text{mA}$ | $5{,}69\,\text{V}$ | $0{,}042$ |
| $400$ | $2{,}144\,\text{mA}$ | $5{,}56\,\text{V}$ | $0{,}021$ |

Vervierfacht sich $B$, wächst der Strom um $6\,\%$; mit dem bloßen Basiswiderstand wären es $300\,\%$.

**Die Näherungen.** Ohne die Glieder mit $B$ ergäben sich $2{,}19\,\text{mA}$, gut $4\,\%$ zu viel, weil $R_i/B$ mit $38\,\Omega$ neben $1\,\text{k}\Omega$ noch
mitspielt. Lässt man wie das Skript auch $U_{BE}$ weg, erhält man $2{,}79\,\text{mA}$, ein Drittel zu viel.

**Querstrom.** Unter Last liegen an der Basis $2{,}710\,\text{V}$, und durch $R_2$ fließen $0{,}271\,\text{mA}$, das $26$-Fache des Basisstroms; die Faustregel
ist erfüllt.

**Zwanzig Kelvin wärmer.** Eine Verschiebung von $36\,\text{mV}$ an $2{,}19\,\text{V}$ ändert den Strom um $1{,}6\,\%$.

**Im Bild:** Ventile mit Übersetzungen von $100$ bis $400$ führen am selben Druckteiler und Abflussrohr fast denselben Strom.
::::

:::grafik
Szene: get1/bipolartransistoren/02-stromgegenkopplung · Vorlage: transistor-gegenkopplung
Links die Schaltung von Bild 11.6 mit $U_{CC} = 12\,\text{V}$, dem Teiler aus $R_1 = 33\,\text{k}\Omega$ und $R_2 = 10\,\text{k}\Omega$, $R_C = 2\,\text{k}\Omega$
und $R_E = 1\,\text{k}\Omega$, mit den Zählpfeilen von $I_B$, $I_C$, $I_E$, $U_{BE}$ und $U_{CE}$; ein Pfeil verwandelt den Teiler in die Ersatzquelle
$U_q = 2{,}79\,\text{V}$ mit $R_i = 7{,}67\,\text{k}\Omega$ wie in Bild 11.7. Rechts die vier Schritte des Regelkreises als Kette: $I_C$ steigt, die Spannung an
$R_E$ steigt, $U_{BE}$ sinkt, $I_C$ sinkt; jeder Schritt leuchtet in der Schaltung an seinem Bauteil auf. Ein Regler für $B$ von $100$ bis $400$ und einer für die
Temperatur zeigen, wie wenig sich $I_C$ bewegt, neben einer zweiten Spur für den bloßen Basiswiderstand. Kernaussage: Der Emitterstrom drosselt seinen eigenen
Antrieb. (Rot = Transistor und Regelgröße $I_C$, blau = Teiler und Ersatzquelle, orange = Regelkreis, grau = übrige Bauteile.)
:::

## Spannungsgegenkopplung

Die zweite Schaltung des Skripts, Bild 11.8, kommt ohne Teiler und ohne Emitterwiderstand aus. Der Basiswiderstand $R_B$ hängt hier nicht an einer
Eingangsspannung, sondern am Kollektor, und der Emitter liegt an Masse. Durch $R_C$ fließen jetzt Kollektor- und Basisstrom zusammen, denn der Basisstrom zweigt
erst hinter $R_C$ ab. Die Masche von $U_{CC}$ über $R_C$, $R_B$ und die Basis-Emitter-Strecke ergibt die Gleichung 11.2 des Skripts:

:::formel
$$I_C = \frac{U_{CC} - U_{BE}}{R_C\,\Big(1 + \dfrac{1}{B}\Big) + \dfrac{R_B}{B}}.$$
:::

**So liest man das:** Das ist dieselbe Form wie Formel (5). $R_C$ übernimmt die Rolle von $R_E$, weil auch durch ihn die Summe aus Basis- und Kollektorstrom
fließt, und $R_B$ die von $R_i$. Mit $B$ über $100$ ist $1/B$ klein gegen eins; wählt man dazu $R_C$ viel größer als $R_B/B$, folgt die Näherung des Skripts:

$$I_C \approx \frac{U_{CC} - U_{BE}}{R_C}.$$

Der Regelkreis läuft über die Spannung am Kollektor, deshalb heißt die Schaltung Spannungsgegenkopplung: Steigt $I_C$, fällt an $R_C$ mehr ab, und das
Kollektorpotenzial sinkt. Weil der Basisstrom von der Spannung zwischen Kollektor und Basis getrieben wird, fließt dann weniger Basisstrom, und der Anstieg wird
gebremst.

Die Näherung hat einen Preis, den das Skript nicht nennt. Die Masche über $R_B$ ergibt für die Spannung am Kollektor:

$$U_{CE} = U_{BE} + R_B\,I_B.$$

Ist $R_B/B$ klein gegen $R_C$, ist auch der Abfall an $R_B$ klein gegen den an $R_C$, und $U_{CE}$ liegt nur wenig über $U_{BE}$, am Rand der Sättigung, wo für
ein Signal kaum Platz bleibt. Für einen Arbeitspunkt in der Mitte braucht man $R_B/B$ etwa so groß wie $R_C$, und dann wirkt $B$ wieder spürbar: Die
Empfindlichkeit beträgt knapp ein halb. Die Spannungsgegenkopplung verringert den Einfluss von $B$ also, beseitigt ihn aber nicht. Dafür hat sie eine angenehme
Eigenschaft: Weil $U_{CE}$ nie unter $U_{BE}$ fällt, kann der Transistor in dieser Schaltung nicht sättigen.

**Im Bild:** Die Steuerleitung zapft den Druck unmittelbar vor dem Ventil an. Öffnet das Ventil weiter, sinkt dort der Druck, und das Steuerwasser wird
knapper. Und weil kein Steuerwasser mehr flösse, wenn der Druck vor dem Ventil unter den Öffnungsdruck fiele, steht das Ventil nie ganz offen.

:::herleitung
**Masche.** Von $U_{CC}$ über $R_C$ mit dem Strom $I_C + I_B$, über $R_B$ mit dem Strom $I_B$ und über die Basis-Emitter-Strecke nach Masse:

$$U_{CC} = R_C\,(I_C + I_B) + R_B\,I_B + U_{BE}.$$

Mit $I_B$ gleich $I_C/B$ wird daraus die Gleichung des Skripts:

$$U_{CC} - U_{BE} = \Big(\frac{I_C}{B} + I_C\Big)\,R_C + \frac{I_C}{B}\,R_B.$$

Nach $I_C$ aufgelöst ergibt sich Formel (6). Mit $1/B$ klein gegen eins und $R_B/B$ klein gegen $R_C$ ist der Nenner fast $R_C$; das ist die Näherung.

**Die Kollektorspannung.** Die Masche vom Kollektor über $R_B$ und die Basis-Emitter-Strecke nach Masse ergibt die zweite Formel. Weil $R_B I_B$ nicht negativ
ist, liegt $U_{CE}$ mindestens bei $U_{BE}$, und mit $0{,}6\,\text{V}$ über $0{,}2\,\text{V}$ ist der Transistor nie gesättigt. Physikalisch heißt das: Der
Kollektor ist nie negativer als die Basis, und der Basis-Kollektor-Übergang wird nie in Durchlassrichtung gepolt.

**Die Mitte.** Soll $U_{CE}$ bei der halben Versorgung liegen, müssen an $R_B$ etwa $U_{CC}/2 - U_{BE}$ und an $R_C$ etwa $U_{CC}/2$ abfallen. Durch $R_B$
fließt der $(B + 1)$-te Teil des Stroms durch $R_C$, und mit $B + 1$ fast gleich $B$ folgt:

$$\frac{R_B}{B\,R_C} \approx \frac{U_{CC}/2 - U_{BE}}{U_{CC}/2} = 1 - \frac{2\,U_{BE}}{U_{CC}}.$$

**Empfindlichkeit.** Wie bei Formel (5), mit $R_C$ statt $R_E$ und $R_B$ statt $R_i$:

$$S_B = \frac{R_C + R_B}{(1 + B)\,R_C + R_B}.$$

Ist $R_B$ das $0{,}9$-Fache von $B R_C$, wie es die Mitte an $12\,\text{V}$ verlangt, ist das ungefähr $0{,}9/1{,}9$, also knapp ein halb. Im Bild: Damit das
Manometer in der Mitte steht, muss das Steuerrohr so eng sein, dass die Übersetzung des Ventils wieder mitredet.
:::

::::beispiel Spannungsgegenkopplung: Mitte oder Unabhängigkeit
Der Kollektor liegt über $R_C$ an der Versorgung, der Basiswiderstand führt vom Kollektor zur Basis, der Emitter liegt an Masse:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega.$$

**Für die Mitte ausgelegt,** mit $B = 200$: Bei $6\,\text{V}$ am Kollektor fließen durch $R_C$ insgesamt $3\,\text{mA}$. Davon geht der $201$-te Teil,
$14{,}93\,\mu\text{A}$, durch $R_B$, an dem $5{,}4\,\text{V}$ liegen:

$$R_B = \frac{5{,}4\,\text{V}}{14{,}93\,\mu\text{A}} = 362\,\text{k}\Omega.$$

Mit dem Normwert $360\,\text{k}\Omega$ ergibt Formel (6):

$$I_C = \frac{12\,\text{V} - 0{,}6\,\text{V}}{2\,\text{k}\Omega\cdot1{,}005 + 1{,}8\,\text{k}\Omega} = 2{,}99\,\text{mA}.$$

**Andere Exemplare** mit demselben Widerstand:

| $B$ | $I_C$ | $U_{CE}$ |
|---|---|---|
| $100$ | $2{,}03\,\text{mA}$ | $7{,}90\,\text{V}$ |
| $200$ | $2{,}99\,\text{mA}$ | $5{,}99\,\text{V}$ |
| $400$ | $3{,}92\,\text{mA}$ | $4{,}13\,\text{V}$ |

Vervierfacht sich $B$, wächst der Strom auf knapp das Doppelte: besser als das Vierfache beim bloßen Basiswiderstand, schlechter als die $6\,\%$ beim Teiler
mit Emitterwiderstand. Die Empfindlichkeit beträgt bei $B = 200$

$$S_B = \frac{2\,\text{k}\Omega + 360\,\text{k}\Omega}{201\cdot2\,\text{k}\Omega + 360\,\text{k}\Omega} = 0{,}48.$$

**Nach der Bedingung des Skripts,** mit $40\,\text{k}\Omega$, also $R_B/B$ von $200\,\Omega$, klein gegen $R_C$:

| $B$ | $I_C$ | $U_{CE}$ |
|---|---|---|
| $100$ | $4{,}71\,\text{mA}$ | $2{,}48\,\text{V}$ |
| $200$ | $5{,}16\,\text{mA}$ | $1{,}63\,\text{V}$ |
| $400$ | $5{,}42\,\text{mA}$ | $1{,}14\,\text{V}$ |

Der Strom schwankt nur noch um $15\,\%$, doch der Arbeitspunkt klebt am Rand der Sättigung; für ein Signal bleiben nach unten nur ein bis anderthalb Volt.
Gesättigt ist der Transistor in keinem Fall, $U_{CE}$ bleibt über $U_{BE}$.

**Im Bild:** Zapft die Steuerleitung den Druck vor dem Ventil mit einem weiten Rohr an, regelt sie kräftig, aber das Manometer steht dann fast beim Restdruck.
::::

## Betriebsgrenzen

Wie jedes reale Bauteil hat der Transistor nach dem Skript Grenzen, deren Überschreiten seine Lebensdauer rasch verkürzt oder ihn sofort zerstört. Der Text nennt
zwei: die __Durchbruchspannung__ $U_{CE,\max}$, ab der der gesperrte Basis-Kollektor-Übergang durchbricht, ähnlich dem Lawinendurchbruch der Diode, und den
__maximalen Kollektorstrom__ $I_{C,\max}$, den Anschlüsse und Halbleiter auf Dauer vertragen. Bild 11.9, im Skript Leistungskennlinie genannt, zeigt eine dritte
Grenze, die der Text nicht erwähnt: die Kurve zwischen den beiden, die Grenze der Verlustleistung $P_\text{tot}$. Was der Transistor in Wärme umsetzt, muss er
an die Umgebung abgeben; wird es mehr, steigt die Temperatur in seinem Inneren über ihren zulässigen Höchstwert. Erlaubt sind die Arbeitspunkte, die alle drei
Bedingungen erfüllen:

:::formel Definition
$$U_{CE} \le U_{CE,\max}, \qquad I_C \le I_{C,\max}, \qquad U_{CE}\,I_C \le P_\text{tot}.$$
:::

**So liest man das:** Im Ausgangskennlinienfeld ist die dritte Grenze eine Hyperbel, und die drei Grenzen umschließen den schraffierten Bereich von Bild 11.9.
$P_\text{tot}$ gilt für eine bestimmte Kühlung und Umgebungstemperatur, die das Datenblatt angibt. Sicher ist eine Schaltung, wenn ihre ganze Arbeitsgerade im
erlaubten Bereich liegt, denn ein Signal, eine Störung oder ein anderes Exemplar kann den Arbeitspunkt an jede Stelle der Geraden schieben. Nach dem Abschnitt
über die Verlustleistung genügen dafür drei Bedingungen:

$$U_{CC} \le U_{CE,\max}, \qquad \frac{U_{CC}}{R_C} \le I_{C,\max}, \qquad \frac{U_{CC}^2}{4\,R_C} \le P_\text{tot}.$$

**Im Bild:** Rohr und Ventil vertragen einen Höchstdruck, einen Höchstdurchfluss und nur so viel Leistung, wie das Ventil als Wärme loswird. Das Manometer darf
nur dort stehen, wo alle drei eingehalten sind.

:::herleitung
**Die Hyperbel.** Am Rand der dritten Grenze ist das Produkt aus $U_{CE}$ und $I_C$ gleich $P_\text{tot}$; nach dem Strom aufgelöst:

$$I_C = \frac{P_\text{tot}}{U_{CE}}.$$

Das ist eine Hyperbel, die bei kleinen Spannungen steil ansteigt und bei großen flach ausläuft; darunter ist die Leistung kleiner.

**Die ganze Gerade.** Längs der Arbeitsgeraden ist $U_{CE}$ höchstens $U_{CC}$, im gesperrten Zustand, und $I_C$ kleiner als $U_{CC}/R_C$, sein Wert bei
$U_{CE}$ null. Die Leistung ist nach dem Abschnitt über die Verlustleistung höchstens $U_{CC}^2/(4R_C)$. Halten diese drei Höchstwerte die Grenzen ein, tut es
jeder Punkt der Geraden. Im Bild: Hält die Leitung den größten Druck, den größten Durchfluss und die größte Leistung aus, die überhaupt vorkommen können, hält
sie alles aus.
:::

::::beispiel Liegt die Arbeitsgerade sicher?
Ein Kleinsignaltransistor mit den Grenzwerten

$$U_{CE,\max} = 45\,\text{V}, \qquad I_{C,\max} = 100\,\text{mA}, \qquad P_\text{tot} = 0{,}5\,\text{W}.$$

Seine Hyperbel geht durch die Punkte $(5\,\text{V}, 100\,\text{mA})$, $(10\,\text{V}, 50\,\text{mA})$ und $(20\,\text{V}, 25\,\text{mA})$.

**(a) Die Schaltung der Beispiele,** $12\,\text{V}$ und $2\,\text{k}\Omega$: höchstens $6\,\text{mA}$ und $18\,\text{mW}$, weit im erlaubten Bereich.

**(b) Mit $24\,\text{V}$ an $100\,\Omega$.** Die Gerade reicht bis $240\,\text{mA}$, und in ihrer Mitte wären es

$$P_\text{max} = \frac{(24\,\text{V})^2}{4\cdot100\,\Omega} = 1{,}44\,\text{W}.$$

Beides ist zu viel. Wo die Gerade die Hyperbel schneidet, sagt die Gleichung

$$\frac{U_{CE}\,(24\,\text{V} - U_{CE})}{100\,\Omega} = 0{,}5\,\text{W}, \qquad U_{CE} = 2{,}3\,\text{V} \ \text{oder} \ 21{,}7\,\text{V}.$$

Dazwischen würde der Transistor überhitzen.

**(c) Der kleinste sichere Kollektorwiderstand** an $24\,\text{V}$ folgt aus Strom- und Leistungsgrenze:

$$R_C \ge \frac{24\,\text{V}}{100\,\text{mA}} = 240\,\Omega, \qquad R_C \ge \frac{(24\,\text{V})^2}{4\cdot0{,}5\,\text{W}} = 288\,\Omega.$$

Mit dem Normwert $300\,\Omega$ sind es höchstens $80\,\text{mA}$ und $0{,}48\,\text{W}$, und die $24\,\text{V}$ liegen unter $45\,\text{V}$.

**Im Bild:** Ein weites Rohr an einem hohen Turm lässt mehr durch, als das Ventil aushält; erst ein engeres Rohr hält jede Stellung des Ventils im erlaubten
Bereich.
::::

:::grafik
Szene: get1/bipolartransistoren/02-betriebsgrenzen · Vorlage: transistor-soa
Das Ausgangskennlinienfeld bis $50\,\text{V}$ und $250\,\text{mA}$ mit den Grenzen $U_{CE,\max} = 45\,\text{V}$ und $I_{C,\max} = 100\,\text{mA}$ als gestrichelte
Linien und der Hyperbel für $0{,}5\,\text{W}$; der erlaubte Bereich darunter ist schraffiert wie in Bild 11.9. Regler für $U_{CC}$ und $R_C$ legen eine
Arbeitsgerade hinein; Stücke außerhalb des erlaubten Bereichs färben sich, und der Punkt größter Leistung auf der Geraden ist markiert. Voreinstellungen:
$12\,\text{V}$ mit $2\,\text{k}\Omega$, $24\,\text{V}$ mit $100\,\Omega$ und $24\,\text{V}$ mit $300\,\Omega$. Kernaussage: Eine Schaltung ist sicher, wenn ihre
ganze Arbeitsgerade unter allen drei Grenzen bleibt. (Rot = Stücke der Geraden außerhalb, blau = Arbeitsgerade, orange = Hyperbel, grau = Achsen und Schraffur,
gestrichelt = Strom- und Spannungsgrenze.)
:::

## Der Stromspiegel

Abschnitt 11.4 des Skripts rechnet zwei wichtige Schaltungen an Gleichspannung durch. Die erste ist der __Stromspiegel__, Bild 11.15. Er kopiert einen
__Referenzstrom__ $I_\text{ref}$ aus einem Zweig in einen anderen, er „spiegelt“ ihn, und kann ihn bei Bedarf vervielfachen. Zwei gleiche npn-Transistoren T1
und T2 haben ihre Emitter an Masse und ihre Basen verbunden. Bei T1 ist zusätzlich der Kollektor mit der Basis verbunden, und über einen Widerstand, hier
$R_\text{ref}$ und im Skript $R_C$ genannt, fließt der Referenzstrom von $U_{CC}$ in diesen Knoten. T2 bezieht seinen Kollektorstrom $I_{C2}$ über die Last
$R_L$ aus $U_{CC}$. Das Skript nimmt an, beide Transistoren und ihre Basis-Emitter-Spannungen seien gleich, und erhält seine Gleichung 11.3:

:::formel
$$I_\text{ref} = \frac{U_{CC} - U_{BE}}{R_\text{ref}}, \qquad I_{C2} = \frac{I_\text{ref}}{1 + \dfrac{2}{B}} \approx I_\text{ref}.$$
:::

**So liest man das:** Eingaben sind die Versorgung und $R_\text{ref}$, Ausgabe der Strom im zweiten Zweig. Er ist der Referenzstrom bis auf die kleine Korrektur
$2/B$, die von den beiden Basisströmen stammt, und er hängt nicht von $R_L$ ab, solange T2 im aktiven Bereich bleibt. Der Spiegel ist also eine Stromquelle,
deren Wert man mit einem Widerstand einstellt, für jede Last bis

$$R_L \le \frac{U_{CC} - U_{CE,\text{sat}}}{I_{C2}}.$$

Wie er funktioniert, verrät T1. Weil sein Kollektor mit der Basis verbunden ist, wirkt er wie eine Diode, und er kann nicht sättigen, denn $U_{CE}$ ist bei ihm
gleich $U_{BE}$. Er stellt sich selbst ein: Wäre $U_{BE}$ zu klein, nähme T1 weniger auf, als $R_\text{ref}$ liefert; der Überschuss flösse in die Basen und
höbe $U_{BE}$, bis sein Kollektorstrom passt. So übersetzt T1 den Referenzstrom in genau die Spannung $U_{BE}$, die zu ihm gehört. T2 bekommt dieselbe Spannung
und übersetzt sie zurück in denselben Strom.

Das lineare Ersatzschaltbild allein erklärt das nicht. Darin lägen zwei Spannungsquellen von $0{,}6\,\text{V}$ parallel, und wie sich der Strom auf sie
verteilt, ließe das Modell offen. Die Annahme gleicher Transistoren stützt sich auf die Transfergleichung des vorigen Artikels: Gleiche Transistoren bei gleicher
Temperatur und gleicher Spannung $U_{BE}$ führen denselben Kollektorstrom. Deshalb fertigt man die beiden nebeneinander auf demselben Chip; das Skript kündigt
die Schaltung für die Schaltungstechnik an, und in integrierten Schaltungen steckt sie fast überall. Mit $n$ gleichen Transistoren parallel als T2, oder einem
mit $n$-facher Fläche, wird der Strom $n$-fach gespiegelt, denn $I_S$ wächst mit der Fläche.

**Im Bild:** Zwei gleiche Regelventile hängen an derselben Steuerleitung. Das erste speist die Steuerleitung aus seinem eigenen Zulauf und stellt sich so ein,
dass es genau den Referenzstrom durchlässt. Das zweite bekommt denselben Steuerdruck und lässt dasselbe durch, gleich wie eng sein eigenes Zulaufrohr ist,
solange ihm Restdruck bleibt.

:::herleitung
**T1 ist immer aktiv.** Kollektor und Basis sind verbunden, also ist $U_{CB}$ null und nach der Maschenregel $U_{CE}$ gleich $U_{BE}$, mit $0{,}6\,\text{V}$
über $U_{CE,\text{sat}}$.

**Gleiche Ströme.** Beide Basis-Emitter-Übergänge liegen zwischen denselben Knoten, also an derselben Spannung. Nach der Transfergleichung mit gleichem $I_S$
sind die Kollektorströme gleich, solange auch T2 aktiv ist; mit gleichem $B$ sind es auch die Basisströme.

**Der Knoten am Kollektor von T1.** Der Referenzstrom teilt sich auf den Kollektor von T1 und die beiden Basen auf:

$$I_\text{ref} = I_{C1} + I_{B1} + I_{B2} = B\,I_{B2} + I_{B2} + I_{B2} = (B + 2)\,I_{B2}.$$

**Der Ausgang.**

$$I_{C2} = B\,I_{B2} = \frac{B}{B + 2}\,I_\text{ref} = \frac{I_\text{ref}}{1 + 2/B}.$$

**Der Referenzstrom.** Die Masche von $U_{CC}$ über $R_\text{ref}$ und die Basis-Emitter-Strecke von T1 nach Masse ergibt die erste Formel.

**Die Lastgrenze.** T2 bleibt aktiv, solange an ihm mindestens $U_{CE,\text{sat}}$ liegen; die Masche über $R_L$ ergibt die Bedingung.

**Vervielfachen.** Besteht T2 aus $n$ gleichen Transistoren parallel, führt jeder denselben Strom wie T1, und ihre Basen ziehen zusammen das $n$-Fache von
$I_{B1}$:

$$I_\text{ref} = (B + 1 + n)\,I_{B1}, \qquad I_{C2} = n\,B\,I_{B1} = \frac{n\,I_\text{ref}}{1 + (n + 1)/B}.$$

Im Bild: Das erste Ventil misst den Referenzstrom und stellt den Steuerdruck dazu ein; jedes gleiche Ventil an diesem Druck führt denselben Strom.
:::

::::beispiel Ein Stromspiegel für ein Milliampere
Zwei gleiche Transistoren mit der Stromverstärkung $200$:

$$U_{CC} = 12\,\text{V}, \qquad R_\text{ref} = 11\,\text{k}\Omega.$$

**Referenz und Spiegelstrom.**

$$I_\text{ref} = \frac{12\,\text{V} - 0{,}6\,\text{V}}{11\,\text{k}\Omega} = 1{,}036\,\text{mA}, \qquad I_{C2} = \frac{1{,}036\,\text{mA}}{1{,}01} = 1{,}026\,\text{mA}.$$

Jede Basis zieht $5{,}13\,\mu\text{A}$.

**Verschiedene Lasten.** Bis $11{,}5\,\text{k}\Omega$ bleibt T2 aktiv:

| $R_L$ | $U_{CE2}$ | $I_{C2}$ |
|---|---|---|
| $1\,\text{k}\Omega$ | $10{,}97\,\text{V}$ | $1{,}026\,\text{mA}$ |
| $10\,\text{k}\Omega$ | $1{,}74\,\text{V}$ | $1{,}026\,\text{mA}$ |
| $22\,\text{k}\Omega$ | $0{,}2\,\text{V}$ | $0{,}536\,\text{mA}$ |

Mit $22\,\text{k}\Omega$ verlangte der aktive Bereich $22{,}6\,\text{V}$ an der Last; T2 sättigt, und der Spiegel versagt.

**Andere Verstärkungen.** Mit einer Stromverstärkung von $50$ sind es $0{,}997\,\text{mA}$, mit einer von $400$ sind es $1{,}031\,\text{mA}$; selbst eine
kleine Verstärkung verschiebt den Strom nur um wenige Prozent.

**Dreifach.** Mit drei parallelen Transistoren als T2 fließen nach der Herleitung

$$I_{C2} = \frac{3\cdot1{,}036\,\text{mA}}{1 + 4/200} = 3{,}05\,\text{mA}.$$

**Im Bild:** Das zweite Ventil führt bei jedem Zulaufrohr bis $11{,}5\,\text{k}\Omega$ dasselbe Milliampere; bei einem noch engeren Rohr kommt das Wasser nicht
mehr nach.
::::

:::grafik
Szene: get1/bipolartransistoren/02-stromspiegel · Vorlage: stromspiegel
Die Schaltung von Bild 11.15: links $U_{CC}$, $R_\text{ref}$ und T1 mit dem Kollektor an der Basis, rechts $R_L$ und T2, die Basen verbunden, beide Emitter an
Masse; Zählpfeile für $I_\text{ref}$, $I_{C1}$, $I_{B1}$, $I_{B2}$ und $I_{C2}$. Daneben das Ausgangskennlinienfeld von T2 mit der waagrechten Linie bei
$1{,}026\,\text{mA}$ und der Arbeitsgeraden der Last. Ein Regler für $R_L$ von $0$ bis $25\,\text{k}\Omega$ dreht die Gerade; der Arbeitspunkt gleitet auf der
waagrechten Linie, bis er bei $11{,}5\,\text{k}\Omega$ in die Sättigung fällt und der Strom einbricht. Ein zweiter Regler für $R_\text{ref}$ hebt und senkt die
Linie. Kernaussage: Der Spiegel liefert einen festen Strom, solange T2 Restspannung bleibt. (Rot = T2 und sein Strom, blau = Referenzzweig, orange = gemeinsame
Spannung $U_{BE}$, grau = Achsen und Versorgung.)
:::

## Der Inverter

Die zweite Schaltung des Abschnitts ist der __Inverter__, Bild 11.16: die Schaltung von Bild 11.4 mit dem Kollektor als Ausgang. Der Name kommt daher, dass er
ein Signal umkehrt. Man kann ihn als invertierenden Verstärker betrachten oder, wie das Skript, als Logikbaustein, in dem eine Spannung nahe null den Wert 0
darstellt und eine nahe $U_{CC}$ den Wert 1. Die Rechnung mit Annahme und Probe liefert zu jeder Eingangsspannung den Ausgang, die __Übertragungskennlinie__ von
Bild 11.17. Sie besteht aus drei geraden Stücken. Gesperrt, bis $U_{BE,\text{ein}}$, liegt der Ausgang auf $U_{CC}$, gesättigt auf $U_{CE,\text{sat}}$, und
dazwischen, im aktiven Bereich, fällt die Kennlinie geradlinig:

$$U_\text{aus} = U_{CC} - \frac{B\,R_C}{R_B}\,\big(U_\text{ein} - U_{BE,\text{ein}}\big).$$

Die Sättigung beginnt bei der Eingangsspannung $U_{\text{ein,sat}}$, im Skript $U_{E,\text{sat}}$, nach seiner Gleichung 11.4:

:::formel
$$U_{\text{ein,sat}} = U_{BE,\text{ein}} + \frac{R_B}{B\,R_C}\,\big(U_{CC} - U_{CE,\text{sat}}\big).$$
:::

**So liest man das:** Eingaben sind die Werte der Schaltung, Ausgabe die Eingangsspannung, ab der der Ausgang unten liegt. Die Steigung des mittleren Stücks ist
$-BR_C/R_B$; über das Verhältnis der Widerstände bestimmt man, wie steil der Übergang ist, wie das Skript sagt. Als Logikbaustein: Unter $U_{BE,\text{ein}}$ ist
der Eingang 0 und der Ausgang $U_{CC}$, also 1; über $U_{\text{ein,sat}}$ ist der Eingang 1 und der Ausgang $U_{CE,\text{sat}}$, also 0. Dazwischen ist der
Ausgang keiner der beiden Werte, und ein Logiksignal darf dort nicht stehen bleiben; das Skript spricht von einem Fehler.

Deshalb legt man $U_{\text{ein,sat}}$ möglichst nahe an $U_{BE,\text{ein}}$, mit großem $BR_C/R_B$. Weil $B$ streut, rechnet man mit dem kleinsten $B$, das den
größten Wert von $U_{\text{ein,sat}}$ ergibt. Bild 11.18 zeigt das Ergebnis für eine Rechteckspannung zwischen null und $U_{CC}$ am Eingang: Der Ausgang springt
gegenläufig zwischen $U_{CC}$ und $U_{CE,\text{sat}}$.

Drei Druckfehler des Skripts: Im Satz über den Sperrbereich steht „$0{,}6\,\Omega$“ statt Volt, und im Bruch der Gleichung für die Eingangsspannung wie in
Gleichung 11.4 fehlt $R_C$ im Nenner, dort steht nur „$B\cdot$“.

**Im Bild:** Das Manometer vor dem Ventil ist der Ausgang. Ohne Steuerstrom zeigt es den vollen Turmdruck, mit genug Steuerstrom den Restdruck; dazwischen steht
es irgendwo, und diesen Übergang soll ein Logiksignal rasch durchqueren.

:::herleitung
**Sperrbereich.** Unter der Schwelle fließt kein Strom, an $R_C$ fällt nichts ab, und der Ausgang liegt auf $U_{CC}$.

**Aktiver Bereich.** Nach Formel (2) ist $U_\text{aus}$ die Versorgung minus $BR_C I_B$, mit dem Basisstrom aus der Eingangsmasche; das ergibt die Gerade. Ihre
Ableitung nach $U_\text{ein}$ ist $-BR_C/R_B$.

**Die Grenze.** Die Gerade erreicht $U_{CE,\text{sat}}$ bei der Eingangsspannung $U_{\text{ein,sat}}$, für die gilt:

$$U_{CE,\text{sat}} = U_{CC} - \frac{B\,R_C}{R_B}\,\big(U_{\text{ein,sat}} - U_{BE,\text{ein}}\big).$$

Nach $U_{\text{ein,sat}}$ aufgelöst ergibt sich Formel (9). Für größere Eingangsspannungen wäre $U_{CE}$ nach der Geraden kleiner als $U_{CE,\text{sat}}$; der
Transistor ist dann gesättigt, und der Ausgang bleibt dort.

**Der Bruch des Skripts.** Das Skript löst die Gerade zuerst allgemein nach der Eingangsspannung auf, die zu einem bestimmten $U_{CE}$ gehört:

$$U_\text{ein} = \frac{(U_{CC} - U_{CE})\,R_B}{B\,R_C} + U_{BE,\text{ein}}.$$

Mit $U_{CE,\text{sat}}$ eingesetzt ist das wieder Formel (9). Im Bild: Wie viel Steuerdruck man braucht, bis das Ventil ganz offen ist, hängt davon ab, wie viel
Steuerwasser das Steuerrohr durchlässt und wie stark das Ventil übersetzt.
:::

::::beispiel Ein Inverter an fünf Volt
Ein Logikinverter mit

$$U_{CC} = 5\,\text{V}, \qquad R_C = 1\,\text{k}\Omega, \qquad R_B = 10\,\text{k}\Omega, \qquad B = 100.$$

**Die Sättigungsgrenze.**

$$U_{\text{ein,sat}} = 0{,}6\,\text{V} + \frac{10\,\text{k}\Omega}{100\cdot1\,\text{k}\Omega}\,(5\,\text{V} - 0{,}2\,\text{V}) = 1{,}08\,\text{V}.$$

Im Übergang zwischen $0{,}6$ und $1{,}08\,\text{V}$ fällt der Ausgang mit der Steigung $-10$.

**Vier Eingangsspannungen.**

| $U_\text{ein}$ | Bereich | $I_B$ | $U_\text{aus}$ |
|---|---|---|---|
| $0\,\text{V}$ | Sperrbereich | $0$ | $5\,\text{V}$ |
| $0{,}8\,\text{V}$ | aktiv | $20\,\mu\text{A}$ | $3{,}0\,\text{V}$ |
| $1{,}08\,\text{V}$ | Grenze | $48\,\mu\text{A}$ | $0{,}2\,\text{V}$ |
| $5\,\text{V}$ | Sättigung | $440\,\mu\text{A}$ | $0{,}2\,\text{V}$ |

Bei $0{,}8\,\text{V}$ liefert der Inverter $3\,\text{V}$, weder eine saubere Null noch eine saubere Eins. Bei $5\,\text{V}$ fließt das Neunfache des
Basisstroms, den die Sättigung braucht; das ist die Übersteuerung aus dem vorigen Artikel.

**Ein Exemplar mit $B = 300$.** Die Grenze rückt auf

$$U_{\text{ein,sat}} = 0{,}6\,\text{V} + 0{,}16\,\text{V} = 0{,}76\,\text{V},$$

und der Übergang wird dreimal so steil. Auslegen muss man für das kleinste $B$.

**Im Bild:** Bei $0{,}8\,\text{V}$ steht das Ventil halb offen und das Manometer mitten auf der Skala; bei $5\,\text{V}$ ist es weit aufgerissen.
::::

:::grafik
Szene: get1/bipolartransistoren/02-inverter · Vorlage: inverter-kennlinie
Links die Schaltung von Bild 11.16 mit $U_{CC} = 5\,\text{V}$, $R_C = 1\,\text{k}\Omega$ und $R_B = 10\,\text{k}\Omega$; in der Mitte die Übertragungskennlinie
$U_\text{aus}$ über $U_\text{ein}$ von $0$ bis $5\,\text{V}$ mit den drei geraden Stücken, den Knicken bei $0{,}6$ und $1{,}08\,\text{V}$ und dem Übergang
dazwischen; rechts wie in Bild 11.18 eine Rechteckspannung am Eingang und die gegenläufige am Ausgang über der Zeit. Regler für $B$ von $50$ bis $300$ und für
$R_B$ verschieben den zweiten Knick und die Steigung; ein Punkt auf der Kennlinie folgt der Eingangsspannung, und die Bereiche färben sich. Kernaussage: Ein
Inverter kehrt das Signal um, mit einem schmalen Übergang zwischen den beiden Logikwerten. (Rot = Kennlinie, blau = Ein- und Ausgangssignal, orange = Übergang,
grau = Achsen.)
:::

## Die drei Grundschaltungen

Ein Verstärker hat einen Eingang und einen Ausgang, und beide Spannungen misst man gegen einen Bezugspunkt. Der Transistor hat aber nur drei Anschlüsse. Einer
davon liegt deshalb fest, an Masse oder an der Versorgung, und gehört zu Eingang und Ausgang zugleich; er gibt der __Grundschaltung__ ihren Namen. Abschnitt 11.5
des Skripts stellt die drei Möglichkeiten mit ihren Übertragungskennlinien vor, Bilder 11.22 bis 11.27.

Dass auch die Versorgung als gemeinsamer Anschluss zählt, liegt daran, dass sie sich nicht ändert. Ein Signal ist eine Änderung, und nach dem
Überlagerungsverfahren trägt eine Gleichspannungsquelle zu Änderungen nichts bei: Für sie ist die Quelle stillgelegt, also ein Kurzschluss, und ihr Anschluss
wirkt wie Masse.

**Die Emitterschaltung**, Bild 11.22: Emitter an Masse, Eingang an der Basis, Ausgang am Kollektor. Mit Basiswiderstand ist das der Inverter, und die Kennlinie
fällt: Die Schaltung kehrt das Signal um, mit der Steigung $-BR_C/R_B$ im aktiven Bereich. Bild 11.22 zeigt die Schaltung ohne $R_B$. Dann liegt die
Eingangsspannung unmittelbar als $U_{BE}$ an, und im linearen Modell fiele die Kennlinie bei $U_{BE,\text{ein}}$ senkrecht ab. In Wirklichkeit folgt der Strom
der Transfergleichung, und die Steigung im Arbeitspunkt ist

$$\frac{dU_\text{aus}}{dU_\text{ein}} = -\frac{R_C\,I_C}{U_T}.$$

Weil der Strom auf knapp $60\,\text{mV}$ um eine Zehnerpotenz wächst, ist der Übergang dann nur gut $0{,}1\,\text{V}$ breit. Bild 11.23 zeigt einen Übergang von
rund $0{,}5\,\text{V}$; die Simulation des Skripts enthielt offenbar einen Widerstand vor der Basis, passend zu seinem Satz, es sei dieselbe Kennlinie wie beim
Inverter. Gemeint ist dort Bild 11.17, nicht 11.18. Am Ausgang fließt der Kollektorstrom, am Eingang der Basisstrom; ihr Verhältnis ist $B$.

**Die Kollektorschaltung**, Bild 11.24: Kollektor an der Versorgung, Eingang an der Basis, Ausgang am Emitter, von dem $R_E$ nach Masse führt. Die Masche vom
Eingang über die Basis-Emitter-Strecke zum Ausgang ergibt:

:::formel
$$U_\text{aus} = U_\text{ein} - U_{BE,\text{ein}}.$$
:::

**So liest man das:** Für Eingangsspannungen über der Schwelle folgt der Ausgang dem Eingang, um $U_{BE}$ nach unten verschoben, wie Bild 11.25 zeigt; daher der
Name __Emitterfolger__. Darunter sperrt der Transistor, und der Ausgang liegt auf null. Die Steigung ist im Modell genau eins, in Wirklichkeit etwas kleiner,
weil $U_{BE}$ mit dem Strom ein wenig wächst; das Skript nennt den Verstärkungsfaktor kleiner eins. Der Nutzen liegt im Strom: Am Ausgang fließt der
Emitterstrom, am Eingang nur der Basisstrom, und ihr Verhältnis ist $B + 1$, die besonders hohe Stromverstärkung, die das Skript erwähnt. Eine Quelle am Eingang
sieht deshalb statt $R_E$ einen $(B + 1)$-mal so großen Widerstand. Die Schaltung ist ein __Impedanzwandler__: Über sie treibt eine schwache Quelle eine
kräftige Last, ohne selbst nennenswert belastet zu werden.

**Die Basisschaltung**, Bild 11.26: Basis an Masse, Eingang am Emitter, Ausgang am Kollektor über $R_C$. Der Transistor leitet, wenn die Eingangsspannung unter
$-U_{BE,\text{ein}}$ liegt, denn $U_{BE}$ ist hier $-U_\text{ein}$. Je negativer der Eingang, desto größer der Strom und desto tiefer der Ausgang; die Kennlinie
steigt also, und die Schaltung kehrt nicht um. Ihre Steigung ist nach der Transfergleichung

$$\frac{dU_\text{aus}}{dU_\text{ein}} = +\frac{R_C\,I_C}{U_T},$$

so groß wie bei der Emitterschaltung, wenn eine Spannungsquelle sie unmittelbar ansteuert, nur mit anderem Vorzeichen. Dass das Skript die größte Steigung der
Basisschaltung größer nennt als die der Emitterschaltung, liegt an seinen beiden Simulationen: In Bild 11.27 wird der Emitter unmittelbar angesteuert, in Bild
11.23 offenbar über einen Widerstand. Für sehr negative Eingangsspannungen sättigt der Transistor, und der Ausgang folgt dem Eingang im Abstand
$U_{CE,\text{sat}}$; das ist der linke Teil von Bild 11.27. Am Eingang fließt hier der ganze Emitterstrom, am Ausgang der Kollektorstrom; ihr Verhältnis ist
$\alpha$, knapp unter eins. Eine Stromverstärkung gibt es also nicht, und die Quelle am Eingang muss den vollen Strom aufnehmen.

| Grundschaltung | Eingang | Ausgang | Kennlinie | Ausgangs- durch Eingangsstrom |
|---|---|---|---|---|
| Emitterschaltung | Basis | Kollektor | fallend, steil | $B$ |
| Kollektorschaltung | Basis | Emitter | Steigung fast eins | $B + 1$ |
| Basisschaltung | Emitter | Kollektor | steigend, steil | $\alpha$, knapp unter eins |

**Im Bild:** In der Emitterschaltung ist die Steuerleitung der Eingang und das Manometer vor dem Ventil der Ausgang. In der Kollektorschaltung liest man den
Druck hinter dem Ventil ab, am Abflussrohr; er ist der Steuerdruck minus dem Öffnungsdruck. In der Basisschaltung hängt die Steuerleitung an festem Druck, und
man verstellt stattdessen den Druck im Abfluss.

:::herleitung
**Emitterschaltung ohne Vorwiderstand.** Mit der Transfergleichung ist der Ausgang

$$U_\text{aus} = U_{CC} - R_C\,I_S\,\exp\frac{U_\text{ein}}{U_T}.$$

Die Ableitung nach $U_\text{ein}$ ist $-R_C$ mal $I_C/U_T$, denn die Exponentialfunktion ist ihre eigene Ableitung. Um den Faktor $99$ wächst der Strom in der
Spannung $U_T\ln 99$, rund $0{,}12\,\text{V}$; so breit ist der Übergang von einem auf neunundneunzig Prozent des größten Stroms.

**Kollektorschaltung.** Die Masche von der Eingangsquelle über die Basis-Emitter-Strecke und $R_E$ nach Masse ergibt, dass $U_\text{ein}$ die Summe aus
$U_{BE,\text{ein}}$ und $U_\text{aus}$ ist; das ist Formel (10). Der Basisstrom ist der $(B + 1)$-te Teil des Emitterstroms:

$$I_B = \frac{U_\text{aus}}{(B + 1)\,R_E} = \frac{U_\text{ein} - U_{BE,\text{ein}}}{(B + 1)\,R_E}.$$

Ändert sich die Eingangsspannung, ändert sich $I_B$ also so, als läge an der Quelle der Widerstand $(B + 1)R_E$. Aktiv bleibt der Transistor, solange zwischen
Kollektor und Emitter mindestens $U_{CE,\text{sat}}$ liegen, also für Eingangsspannungen bis $U_{CC} + U_{BE,\text{ein}} - U_{CE,\text{sat}}$, praktisch für
jede Eingangsspannung bis zur Versorgung.

**Basisschaltung.** Die Basis liegt auf null, der Emitter auf $U_\text{ein}$, also ist $U_{BE}$ gleich $-U_\text{ein}$. Mit der Transfergleichung:

$$U_\text{aus} = U_{CC} - R_C\,I_S\,\exp\frac{-U_\text{ein}}{U_T}.$$

Die Ableitung nach $U_\text{ein}$ ist $+R_C$ mal $I_C/U_T$; das Minus im Exponenten hebt das Minus vor dem Strom auf. Die Stromverhältnisse folgen aus der
Knotenregel: Eingangsstrom $I_E$, Ausgangsstrom $I_C$, Verhältnis $\alpha$. In der Sättigung liegt zwischen Kollektor und Emitter $U_{CE,\text{sat}}$, und der
Ausgang ist $U_\text{ein} + U_{CE,\text{sat}}$. Im Bild: Senkt man den Druck im Abfluss, steigt der Druck über dem Rückschlagventil, das Ventil öffnet, und der
Druck vor ihm sinkt mit dem Eingang.
:::

::::beispiel Drei Grundschaltungen in Zahlen
Transistoren mit der Stromverstärkung $200$ an $U_{CC} = 12\,\text{V}$.

**(a) Emitterfolger mit $1\,\text{k}\Omega$ als $R_E$.** Bei $3\,\text{V}$ am Eingang:

$$U_\text{aus} = 3\,\text{V} - 0{,}6\,\text{V} = 2{,}4\,\text{V}, \qquad I_E = \frac{2{,}4\,\text{V}}{1\,\text{k}\Omega} = 2{,}4\,\text{mA}.$$

Der Basisstrom ist der $201$-te Teil davon:

$$I_B = \frac{2{,}4\,\text{mA}}{201} = 11{,}94\,\mu\text{A}.$$

Bei $3{,}5\,\text{V}$ am Eingang sind es $2{,}9\,\text{V}$ und $14{,}43\,\mu\text{A}$. Der Ausgang folgt dem Eingang Volt für Volt, und die Quelle am Eingang
sieht

$$\frac{0{,}5\,\text{V}}{14{,}43\,\mu\text{A} - 11{,}94\,\mu\text{A}} = 201\,\text{k}\Omega,$$

das $201$-Fache von $R_E$. Zwischen Kollektor und Emitter liegen $9{,}6\,\text{V}$; aktiv bleibt der Transistor bis zu einer Eingangsspannung von
$12{,}4\,\text{V}$.

**(b) Emitter- und Basisschaltung, unmittelbar angesteuert,** mit $2\,\text{k}\Omega$ als $R_C$ im Arbeitspunkt $3\,\text{mA}$, also bei $6\,\text{V}$ am
Ausgang:

$$\frac{R_C\,I_C}{U_T} = \frac{2\,\text{k}\Omega\cdot3\,\text{mA}}{25{,}85\,\text{mV}} = 232.$$

Die Emitterschaltung hat die Steigung $-232$, die Basisschaltung $+232$. Ein Millivolt am Eingang bewegt den Ausgang um $0{,}23\,\text{V}$, und der ganze
Übergang ist nur rund $0{,}12\,\text{V}$ breit.

**(c) Die Eingangsströme** in diesem Arbeitspunkt: Die Emitterschaltung zieht an der Basis $15\,\mu\text{A}$, die Basisschaltung am Emitter
$3{,}015\,\text{mA}$, das $201$-Fache. Das Verhältnis von Ausgangs- zu Eingangsstrom ist $200$ bei der Emitterschaltung und $0{,}995$ bei der Basisschaltung.

**Im Bild:** Der Folger gibt den Steuerdruck fast unverändert weiter, nur um den Öffnungsdruck vermindert, und kostet die Quelle kaum Wasser; die Basisschaltung
verlangt vom Eingang das ganze Wasser des Abflusses.
::::

:::grafik
Szene: get1/bipolartransistoren/02-grundschaltungen · Vorlage: grundschaltungen-kennlinien
Drei Spalten, je eine Grundschaltung: oben das Schaltbild nach den Bildern 11.22, 11.24 und 11.26 mit hervorgehobenem festem Anschluss und markiertem Ein- und
Ausgang, darunter die Übertragungskennlinie $U_\text{aus}$ über $U_\text{ein}$. Bei der Emitterschaltung fällt sie von $12\,\text{V}$ auf $0{,}2\,\text{V}$,
umschaltbar zwischen unmittelbarer Ansteuerung mit dem schmalen Übergang von $0{,}12\,\text{V}$ und Ansteuerung über $R_B$; beim Emitterfolger ist sie die
Gerade im Abstand $0{,}6\,\text{V}$ unter der gestrichelten Diagonale; bei der Basisschaltung steigt sie steil knapp unter $-0{,}6\,\text{V}$, mit dem
gesättigten Ast links. Ein gemeinsamer Regler für die Eingangsspannung bewegt in allen drei Kennlinien einen Punkt, und Zähler zeigen Ein- und Ausgangsstrom mit
ihrem Verhältnis $B$, $B + 1$ und $\alpha$. Kernaussage: Welcher Anschluss fest liegt, entscheidet über Richtung und Steigung der Kennlinie und über die Ströme.
(Rot = fester Anschluss, blau = Kennlinien, orange = Ein- und Ausgang, grau = Achsen, gestrichelt = Diagonale.)
:::

## Bedeutung und Ausblick

Mit dem Arbeitspunkt entscheidet man, wozu ein Transistor dient: Als Schalter springt er zwischen Sperren und Sättigung, wo er wenig Leistung verliert, als
Verstärker ruht er in der Mitte des aktiven Bereichs. Gerechnet wird mit den linearen Ersatzschaltbildern, mit Annahme und Probe. Weil $B$ streut und $U_{BE}$
mit der Temperatur wandert, legt man den Strom über die äußere Schaltung fest. Die Stromgegenkopplung mit Basisspannungsteiler und Emitterwiderstand ist dafür
die übliche Schaltung, weil sie $B$ fast ganz verdrängt und trotzdem einen Arbeitspunkt in der Mitte zulässt; die Spannungsgegenkopplung ist einfacher, aber nur
ein Kompromiss.

Stromspiegel und Inverter zeigen zwei Seiten derselben Physik. Der Spiegel ist eine Stromquelle aus zwei Transistoren und steckt in fast jeder integrierten
Analogschaltung, auch in Operationsverstärkern wie denen des nächsten Kapitels. Der Inverter ist die einfachste Logikschaltung; aus Widerständen und
Transistoren bestand die erste Familie integrierter Logikschaltungen.

Die drei Grundschaltungen unterscheiden sich darin, welcher Anschluss fest liegt; ihre Kennlinien zeigen schon, welche umkehrt, welche folgt und welche Ströme
sie verlangen. Wie groß ihre Verstärkungen für kleine Signale genau sind, zeigt der nächste Artikel über den Transistor als linearen Verstärker, mit den realen
Kennlinien, einem erweiterten Ersatzschaltbild und einer Anwendung zur Spannungsstabilisierung.

:::kern
- Der Arbeitspunkt sind die Ruhewerte; er liegt auf der Arbeitsgeraden $I_C=(U_{CC}-U_{CE})/R_C$.
- Längs der Geraden ist die Verlustleistung eine Parabel mit dem Höchstwert $U_{CC}^2/(4R_C)$ in der Mitte.
- Ein Schalter nutzt Sperrbereich und Sättigung, beide verlustarm; ein Verstärker die Mitte des aktiven Bereichs.
- Lineare Ersatzschaltbilder: offene Anschlüsse; Quelle von $0{,}6\,\text{V}$ und Stromquelle $BI_B$; Quellen von $0{,}6$ und $0{,}2\,\text{V}$.
- Annehmen, rechnen, prüfen: Der Arbeitspunkt ist eindeutig, und eine falsche Annahme verletzt ihre Probe.
- Die Mitte des aktiven Bereichs liegt bei $U_{CE,\text{AP}}=(U_{CC}+U_{CE,\text{sat}})/2$.
- Mit bloßem Basiswiderstand ist $I_C$ proportional zu $B$; ein Emitterwiderstand legt den Emitterstrom fest.
- Stromgegenkopplung mit Teiler: Für $R_E\gg R_i/B$ ist $I_C$ fast unabhängig von $B$; $U_{BE}$ darf man nicht weglassen.
- Spannungsgegenkopplung: $R_B$ führt vom Kollektor zur Basis; weniger Einfluss von $B$, und der Transistor sättigt nie.
- Betriebsgrenzen sind $U_{CE,\max}$, $I_{C,\max}$ und die Leistungshyperbel; die ganze Arbeitsgerade muss darunter liegen.
- Stromspiegel: $I_{C2}=I_\text{ref}/(1+2/B)$, unabhängig von der Last, solange T2 aktiv bleibt.
- Inverter: drei gerade Stücke, Sättigung ab $U_{\text{ein,sat}}$, dazwischen ein verbotener Übergang.
- Grundschaltungen heißen nach dem festen Anschluss: Die Emitterschaltung kehrt um, die Kollektorschaltung folgt, die Basisschaltung kehrt nicht um.
:::

:::quiz
F: Warum betreibt man einen Schalttransistor in Sperrbereich und Sättigung, einen Verstärker aber in der Mitte des aktiven Bereichs?
A: Längs der Arbeitsgeraden ist die Verlustleistung eine Parabel, null an den Enden und am größten in der Mitte; bei $12\,\text{V}$ und $2\,\text{k}\Omega$ sind es $18\,\text{mW}$ in der Mitte und $1{,}18\,\text{mW}$ gesättigt. Ein Verstärker braucht dagegen den linearen aktiven Bereich und nach beiden Seiten Platz für das Signal, also die Mitte, trotz der größten Verlustleistung.
F: Wie sehen die linearen Ersatzschaltbilder aus, und woher kommen sie?
A: Aus den zu geraden Stücken vereinfachten Kennlinien: Senkrechte Stücke werden Spannungsquellen, waagrechte Stromquellen, die Achse ohne Strom ein offener Anschluss. Im Sperrbereich ist alles offen; aktiv liegen $0{,}6\,\text{V}$ zwischen Basis und Emitter und die Stromquelle $BI_B$ zwischen Kollektor und Emitter; gesättigt $0{,}6\,\text{V}$ und $0{,}2\,\text{V}$.
F: Wie bestimmt man den Arbeitspunkt der Schaltung mit Basiswiderstand?
A: Unter der Schwelle sperrt der Transistor. Sonst ist $I_B=(U_\text{ein}-U_{BE,\text{ein}})/R_B$; man nimmt den aktiven Bereich an und prüft $U_{CE}\ge U_{CE,\text{sat}}$, sonst ist er gesättigt. Mit $5\,\text{V}$ am Eingang, $12\,\text{V}$, $2\,\text{k}\Omega$ und $B=200$ ergibt $470\,\text{k}\Omega$ den aktiven Bereich mit $1{,}87\,\text{mA}$ bei $8{,}26\,\text{V}$ und $100\,\text{k}\Omega$ die Sättigung mit $5{,}9\,\text{mA}$.
F: Warum macht ein Emitterwiderstand den Kollektorstrom fast unabhängig von $B$?
A: Eingangsspannung und $R_E$ legen den Emitterstrom fest, $I_E=(U_\text{ein}-U_{BE,\text{ein}})/R_E$, und $B$ entscheidet nur über die Aufteilung $I_C=I_E\,B/(B+1)$. Die Empfindlichkeit ist $1/(B+1)$; mit $2\,\text{mA}$ Emitterstrom liegt $I_C$ für $B$ von $100$ bis $400$ zwischen $1{,}980$ und $1{,}995\,\text{mA}$.
F: Wo liegt die Mitte des aktiven Bereichs, und warum genügt ein dafür berechneter Basiswiderstand nicht?
A: Bei $U_{CE,\text{AP}}=(U_{CC}+U_{CE,\text{sat}})/2$; dann hat das Signal nach beiden Seiten gleich viel Platz. Der Basiswiderstand gilt aber nur für ein $B$: Für $B=200$ mit $300\,\text{k}\Omega$ ausgelegt, landet ein Exemplar mit $B=400$ bei $0{,}27\,\text{V}$ am Rand der Sättigung.
F: Wie wirkt die Stromgegenkopplung mit Basisspannungsteiler, und was ist an der Näherung des Skripts zu beachten?
A: Steigt $I_C$, steigt die Spannung an $R_E$; bei fast fester Basisspannung sinkt $U_{BE}$, und der Strom geht zurück. Nach Formel (5) wirkt $B$ nur in $R_E/B$ und $R_i/B$, und für $R_E\gg R_i/B$ ist $I_C\approx(U_q-U_{BE})/R_E$. $U_{BE}$ wegzulassen, wie das Skript im letzten Schritt, ist bei wenigen Volt an $U_q$ ein grober Fehler: im Beispiel $2{,}79$ statt $2{,}10\,\text{mA}$.
F: Was leistet die Spannungsgegenkopplung, und welchen Preis hat die Näherung des Skripts?
A: Der Basiswiderstand hängt am Kollektor: Steigt $I_C$, sinkt das Kollektorpotenzial und mit ihm der Basisstrom. Mit $R_C\gg R_B/B$ wird $I_C$ fast unabhängig von $B$, aber $U_{CE}=U_{BE}+R_BI_B$ liegt dann nahe $U_{BE}$, am Rand der Sättigung; für die Mitte braucht man $R_B/B$ etwa gleich $R_C$, und die Empfindlichkeit beträgt knapp ein halb. Sättigen kann der Transistor in dieser Schaltung nie.
F: Welche Betriebsgrenzen hat ein Transistor, und wann liegt eine ganze Arbeitsgerade sicher?
A: Die Durchbruchspannung $U_{CE,\max}$, der Höchststrom $I_{C,\max}$ und die Verlustleistung $P_\text{tot}$, die im Kennlinienfeld eine Hyperbel bildet; das Skript nennt im Text nur die ersten beiden. Die Gerade liegt sicher, wenn $U_{CC}$, $U_{CC}/R_C$ und $U_{CC}^2/(4R_C)$ die Grenzen einhalten; an $24\,\text{V}$ mit $0{,}5\,\text{W}$ und $100\,\text{mA}$ braucht man mindestens $288\,\Omega$.
F: Wie funktioniert der Stromspiegel, und wann versagt er?
A: T1 ist als Diode geschaltet und stellt sein $U_{BE}$ so ein, dass er den Referenzstrom führt; T2 liegt an derselben Spannung und führt nach der Transfergleichung denselben Strom, $I_{C2}=I_\text{ref}/(1+2/B)$. Das gilt für jede Last, solange T2 aktiv bleibt; mit $1{,}026\,\text{mA}$ an $12\,\text{V}$ bis $11{,}5\,\text{k}\Omega$, darüber sättigt T2.
F: Was zeigt die Kennlinie des Inverters, und wie unterscheiden sich die drei Grundschaltungen?
A: Der Inverter liefert $U_{CC}$ unter der Schwelle, $U_{CE,\text{sat}}$ ab $U_{\text{ein,sat}}=U_{BE,\text{ein}}+R_B(U_{CC}-U_{CE,\text{sat}})/(BR_C)$ und dazwischen eine fallende Gerade, die man steil haben will. Die Grundschaltungen heißen nach dem festen Anschluss: Die Emitterschaltung kehrt um, die Kollektorschaltung folgt mit $U_\text{aus}=U_\text{ein}-U_{BE,\text{ein}}$ und dem Stromverhältnis $B+1$, die Basisschaltung kehrt nicht um und hat das Stromverhältnis $\alpha$.
:::
