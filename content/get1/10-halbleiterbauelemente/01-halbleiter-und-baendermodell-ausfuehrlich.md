---
title: Halbleiter und das Bändermodell
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100100
summary: Warum reines Silizium kaum leitet, wie Dotierung Art und Zahl der Ladungsträger festlegt und wie am pn-Übergang eine Barriere entsteht, deren Höhe die äußere Spannung verschiebt. Ausführliche Fassung mit allen Herleitungen und Hintergründen.
tags: Halbleiter, Bändermodell, Bandlücke, Eigenleitung, Loch, Fermi-Niveau, Dotierung, pn-Übergang, Raumladungszone, Diffusionsspannung
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Eine Diode lässt Strom nur in eine Richtung durch.
Damit wandelt man zum Beispiel die Wechselspannung aus der Steckdose in die Gleichspannung, die ein Akku zum Laden braucht.
Gebaut wird sie aus einem Werkstoff, dessen Leitfähigkeit sich gezielt einstellen lässt: einem Halbleiter wie Silizium.
Alles in diesem Artikel hängt an einem Prinzip: **Ein Halbleiter hat wenige bewegliche Ladungsträger, deren Art und Zahl die Dotierung festlegt; wo ein n- und ein p-Gebiet aneinandergrenzen, baut der Dichteunterschied von selbst eine Barriere auf, deren Höhe eine äußere Spannung verschiebt.**
Vorausgesetzt werden nur der [elektrische Strom](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/elektrischer-strom.html), [Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html) und das [elektrische Feld](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/elektrisches-feld-und-feldstaerke.html); auf dem Thema bauen [die Kennlinie der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html) und der [Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) auf.

:::grafik
Szene: get1/halbleiterbauelemente/01-gesamtbild · Vorlage: banddiagramm-vergleich
**Abbildung 1:** Der Weg dieses Artikels im Bändermodell, berechnet für Silizium bei 300 K. (a) Reines Silizium: volles Valenzband, leeres Leitungsband, dazwischen 1,12 eV, nur wenige Elektronen und Löcher. (b), (c) Dotiertes Silizium: viele Elektronen bzw. viele Löcher; das Fermi-Niveau $W_F$ rückt an das jeweilige Band. (d) n- und p-Gebiet im Kontakt: Die Bänder bilden eine Stufe von 0,714 eV, an der sich entscheidet, ob Strom fließt. Teilchenzahlen schematisch.
:::

## Wozu ein Bauteil mit Vorzugsrichtung

*Was muss ein Bauteil können, damit aus Wechselspannung eine Spannung mit nur einer Polarität wird?*

:::grafik
Szene: get1/halbleiterbauelemente/01-einweggleichrichter · Vorlage: schaltung-und-zeitverlauf
**Abbildung 2:** Einweggleichrichter mit Wechselspannungsquelle (Scheitelwert 10 V, 50 Hz), Diode D und Widerstand R = 1 kΩ; Verläufe berechnet mit der idealen Beispieldiode dieses Artikels. Nur die positiven Halbwellen erreichen den Widerstand; an der Diode gehen dabei rund 0,7 V verloren.
:::

Abbildung 2 zeigt die einfachste Schaltung dafür, den __Einweggleichrichter__.
Während der positiven Halbwelle lässt die Diode Strom durch, und am Widerstand liegt fast die ganze Quellenspannung an; die Spitze erreicht im idealen Modell der Beispieldiode 9,3 V.
Während der negativen Halbwelle sperrt die Diode, und die Ausgangsspannung bleibt null.
Übrig bleibt eine pulsierende Spannung mit nur einer Polarität, die ein Kondensator anschließend glättet ([Gleichrichtung und Ladungspumpe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe.html)).

Ein Widerstand oder ein Draht kann das nicht, denn bei ihnen ist der Strom proportional zur Spannung, in beiden Richtungen gleich.
Gebraucht wird ein Bauteil, dessen Leitfähigkeit vom Vorzeichen der Spannung abhängt.
Die Bedingung betrifft den Augenblickswert: Nur bei $u_E(t) > 0$ soll Strom fließen; der Scheitelwert $\hat U_E$ ist eine feste Zahl, hier 10 V.

## Vom Atom zum Kristall: Energiebänder

*Warum können Elektronen in einem Kristall nur Energien in bestimmten Bereichen haben?*

**Die Akteure:**

- __$W$__: Energie eines Elektrons; angegeben in Elektronenvolt, wobei 1 eV die Energie ist, die ein Elektron beim Durchlaufen von 1 V gewinnt (1,602·10⁻¹⁹ J).
- __Valenzelektronen__: die vier äußeren Elektronen eines Siliziumatoms; nur sie nehmen an Bindung und Leitung teil.
- __$N$__: Zahl der Atome; ein Kubikzentimeter Silizium enthält 5·10²² davon.

**Das Zusammenspiel:** In einem einzelnen Atom darf ein Elektron nur ganz bestimmte Energien annehmen, die __Energieniveaus__ (in der Schulchemie die Schalen).
Jeder Zustand kann höchstens ein Elektron aufnehmen (__Pauli-Prinzip__). Zum Zustand gehört auch die Spinrichtung, eine von zwei möglichen Ausrichtungen des Elektrons; deshalb passen zwei Elektronen in jedes Niveau.
Rücken zwei Atome so nah zusammen, dass sich ihre äußeren Elektronenhüllen überlappen, koppeln ihre Zustände: Aus einem Niveau werden zwei, eines etwas tiefer, eines etwas höher.
Bei N Atomen spaltet jedes Niveau in N Niveaus auf.
Bei 5·10²² Atomen pro cm³ liegen diese im Mittel nur etwa 10⁻²² eV auseinander, weit weniger als jede messbare Energie; sie bilden ein praktisch lückenloses __Energieband__.
Zwischen den Bändern bleiben Bereiche, in denen es keinen einzigen Zustand gibt: die __verbotenen Zonen__.

Für die Elektrotechnik zählen zwei Bänder (Abbildung 1 a):

- Das __Valenzband__ entsteht aus den Zuständen, die die Bindungen zwischen den Atomen bilden. Es hat genau vier Plätze pro Atom, also genau so viele, wie es Valenzelektronen gibt; am absoluten Nullpunkt ist es deshalb vollständig besetzt. Seine Oberkante heißt __$W_V$__.
- Das __Leitungsband__ entsteht aus den nächsthöheren Zuständen und ist am absoluten Nullpunkt leer. Seine Unterkante heißt __$W_L$__.

:::formel Definition
$$W_g = W_L - W_V$$
:::

**So liest man das:** Die __Bandlücke__ $W_g$ ist der Abstand zwischen der Oberkante des vollen und der Unterkante des leeren Bandes, also die kleinste Energie, die ein Elektron braucht, um vom Valenz- ins Leitungsband zu gelangen.
Man definiert sie so, weil genau diese Energie entscheidet, ob ein Elektron frei werden kann.
Bei Silizium beträgt sie 1,12 eV (bei 300 K), bei Germanium 0,66 eV, bei Siliziumdioxid etwa 9 eV.

::::beispiel Längste Lichtwellenlänge, die in Silizium Elektronen freisetzt
**Gegeben:**
- Bandlücke von Silizium 1,12 eV (300 K);
- ein Lichtquant der Wellenlänge $\lambda$ trägt die Energie $hc/\lambda$ (Grundgesetz der Lichtquanten), mit $hc = 1240\ \mathrm{eV\,nm}$.

**Gesucht:** die größte Wellenlänge, bei der ein Lichtquant ein Elektron über die Lücke heben kann.

**Rechnung:** Das Lichtquant muss mindestens die Bandlücke liefern:

$$\frac{hc}{\lambda} \ge W_g \quad\Longleftrightarrow\quad \lambda \le \frac{hc}{W_g}$$

$$\lambda_\mathrm{max} = \frac{1240\ \mathrm{eV\,nm}}{1{,}12\ \mathrm{eV}} = 1107\ \mathrm{nm}$$

**Ergebnis:** **Licht mit Wellenlängen bis 1,1 µm setzt in Silizium Elektronen frei.**

**Einordnung:** Sichtbares Licht (400 bis 700 nm) trägt 1,8 bis 3,1 eV; deshalb arbeiten Solarzellen und Fotodioden aus Silizium im ganzen sichtbaren Bereich. Jenseits von 1,1 µm ist Silizium durchsichtig. Empfänger für die Glasfaser-Wellenlänge 1,55 µm baut man deshalb aus Germanium (0,66 eV, bis 1,9 µm) oder Indiumgalliumarsenid.
::::

## Leiter, Halbleiter, Isolator

*Warum leitet Kupfer, Silizium kaum und Glas praktisch gar nicht, obwohl alle drei Elektronen im Überfluss enthalten?*

:::grafik
Szene: get1/halbleiterbauelemente/01-leiter-halbleiter-isolator · Vorlage: baender-vergleich
**Abbildung 3:** Metall, Halbleiter (Silizium, Lücke 1,12 eV) und Isolator (Siliziumdioxid, Lücke etwa 9 eV) im Bändermodell, Energieachse in eV (bei Halbleiter und Isolator mit der Valenzbandkante bei null). Grau: besetzte Zustände. Leiten kann nur ein teilweise besetztes Band; beim Halbleiter entstehen solche Bänder erst, weil die Wärme einige Elektronen über die kleine Lücke hebt.
:::

**Das Zusammenspiel:** Strom fließt nur, wenn ein Feld die Elektronen im Mittel in eine Richtung lenken kann.
Dazu muss ein Elektron seinen Zustand wechseln, also in einen freien Zustand mit etwas mehr Geschwindigkeit in Richtung der Kraft übergehen, die das Feld auf es ausübt.
In einem **vollen Band** gibt es keinen freien Zustand.
Zu jedem Elektron, das sich mit einer bestimmten Geschwindigkeit bewegt, gibt es eines, das sich genau entgegengesetzt bewegt; die Geschwindigkeiten heben sich auf.
Ein Feld kann daran nichts ändern, weil kein Elektron in einen anderen Zustand ausweichen kann.
Ein volles Band trägt deshalb keinen Strom, so viele Elektronen es auch enthält, und ein leeres Band ebenso wenig, weil es keine Elektronen hat.
Leiten kann nur ein **teilweise besetztes Band**.

Damit unterscheiden sich die drei Stoffklassen in Abbildung 3:

- **Metall:** Das oberste besetzte Band ist nur teilweise gefüllt, bei Kupfer etwa zur Hälfte, weil jedes Atom ein Valenzelektron beisteuert. Direkt über den besetzten Zuständen liegen freie; alle 8,5·10²² Valenzelektronen pro cm³ sind beweglich. Oft beschreibt man Metalle mit $W_g = 0$; das trifft auf Metalle mit überlappenden Bändern zu (Magnesium), bei Kupfer ist ein Band nur halb voll. Entscheidend ist in beiden Fällen das teilweise besetzte Band.
- **Halbleiter:** Am absoluten Nullpunkt ist das Valenzband voll und das Leitungsband leer; Silizium wäre dann ein Isolator. Bei 300 K hebt die Wärmebewegung einige Elektronen über die Lücke. Die typische thermische Energie $k_B T$ ($k_B$ ist die Boltzmann-Konstante) beträgt 25,85 meV, die Lücke ist 43-mal größer; deshalb gelingt das nur selten. Danach sind beide Bänder ein wenig teilweise besetzt: oben einige Elektronen, unten ebenso viele freie Plätze. Beide Bänder leiten, aber schwach.
- **Isolator:** Siliziumdioxid hat eine Lücke von etwa 9 eV, 350-mal $k_B T$. Praktisch kein Elektron gelangt hinüber.

Der Unterschied zwischen Halbleiter und Isolator liegt also nur in der Breite der Lücke, die Zahl der freien Ladungsträger aber hängt exponentiell davon ab:

| Material | Bandlücke | freie Elektronen bei 300 K |
|---|---|---|
| Germanium | 0,66 eV | 2·10¹³ pro cm³ |
| Silizium | 1,12 eV | 10¹⁰ pro cm³ |
| Galliumarsenid | 1,42 eV | 2·10⁶ pro cm³ |
| Siliziumdioxid | etwa 9 eV | praktisch keine |

Im Bänderbild zählt man die Halbleiter oft zu den Isolatoren mit kleiner Bandlücke, denn bei $T = 0$ leiten sie nicht.
Bei Raumtemperatur trennen sie aber viele Zehnerpotenzen: Reines Silizium hat einen spezifischen Widerstand von 3·10⁵ Ωcm, Siliziumdioxid über 10¹⁴ Ωcm.

## Elektronen und Löcher

*Woher kommen in reinem Silizium bewegliche Ladungsträger, und warum gibt es gleich zwei Sorten?*

:::grafik
Szene: get1/halbleiterbauelemente/01-kristallgitter · Vorlage: kristallgitter-2d
**Abbildung 4:** Siliziumgitter als ebenes Schema (der echte Kristall ist dreidimensional); jede Doppellinie ist eine Bindung aus zwei Elektronen. (a) Die Wärme hat eine Bindung aufgebrochen: ein freies Elektron (blau) und eine Lücke (rot). (b) Phosphor gibt sein fünftes Elektron ab und bleibt als P⁺ zurück. (c) Bor hat ein Elektron aufgenommen und ist zu B⁻ geworden; die Lücke sitzt eine Bindung weiter. Schematisch.
:::

**Die Akteure:**

- __$n$__: Dichte der freien Elektronen im Leitungsband; in cm⁻³.
- __$p$__: Dichte der Löcher, also der Lücken im Valenzband; in cm⁻³.
- __$\mu_n$__, __$\mu_p$__: __Beweglichkeit__ der Elektronen bzw. Löcher, die mittlere Geschwindigkeit pro Feldstärke; 1250 bzw. 450 cm²/(V s) im Beispielsystem dieses Artikels. Ein Feld von 1 V/cm verleiht ihnen also im Mittel 1250 bzw. 450 cm/s. Sie bestimmt, wie leicht ein Feld die Ladungsträger in Bewegung setzt.

**Das Zusammenspiel:** In Abbildung 4 a ist jedes Siliziumatom über vier __kovalente Bindungen__ mit seinen Nachbarn verbunden; jede Bindung besteht aus zwei Elektronen, die sich die beiden Partner teilen.
Gelegentlich sammelt die Wärmebewegung des Gitters so viel Energie an einer Stelle, dass ein Elektron seine Bindung verlässt.
Im Bändermodell springt es dabei vom Valenz- ins Leitungsband.
Der Vorgang heißt __Generation__ und erzeugt immer ein Paar: ein freies Elektron und eine Bindung mit nur einem Elektron, eine Lücke im Valenzband.
Auch Licht kann Paare erzeugen, wenn seine Lichtquanten mehr als 1,12 eV tragen.
Eine gewöhnliche elektrische Spannung erzeugt dagegen keine Ladungsträger, sie bewegt vorhandene.
Erst Felder von einigen 10⁵ V/cm erzeugen Paare, beim Durchbruch einer Diode ([Folgeartikel](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)).

Die Lücke bleibt nicht an ihrem Platz (Abbildung 5).
Ein Elektron aus einer Nachbarbindung kann mit sehr wenig Energie hineinspringen; es bleibt dabei gebunden, hinterlässt aber an seinem alten Platz eine neue Lücke.
So wandert die Lücke durch den Kristall, entgegengesetzt zu den springenden Elektronen.
In einem Feld springen die gebundenen Elektronen bevorzugt gegen die Feldrichtung, denn auf sie wirkt die Kraft $-e\vec E$; die Lücke wandert dadurch mit dem Feld.
In ihrer Umgebung fehlt die negative Ladung eines Elektrons, während die positiven Atomkerne unverändert sind: Die Lücke trägt netto die Ladung $+e$.
Man nennt sie deshalb __Loch__ (auch Defektelektron) und behandelt sie wie ein bewegliches Teilchen mit der Ladung $+e$.

:::grafik
Szene: get1/halbleiterbauelemente/01-loch-wanderung · Vorlage: kette-mit-luecke
**Abbildung 5:** Wie ein Loch wandert, in drei Momenten. Eine Reihe von Bindungsplätzen: Auf allen bis auf einen sitzt ein gebundenes Elektron (blau), der freie Platz ist die Lücke (rot). Von Moment zu Moment springt ein Nachbarelektron gegen das Feld in die Lücke; die Lücke wandert dadurch mit dem Feld, wie eine positive Ladung. Schematisch.
:::

:::frage
„Ist ein Loch ein echtes Teilchen, so wie ein Elektron?“
Nein. Ein Loch ist ein fehlendes Elektron in einer sonst vollständigen Bindungsstruktur; man kann es nicht aus dem Kristall herausnehmen. Seine Bewegung ist die gemeinsame Bewegung vieler gebundener Elektronen, die nacheinander in die Lücke springen. Alle Gleichungen funktionieren aber genau so, als wäre es ein Teilchen mit der Ladung $+e$ und einer eigenen Beweglichkeit. Diese ist mit 450 cm²/(V s) kleiner als die der freien Elektronen (1250 cm²/(V s)), weil sich Löcher im Kristall so bewegen, als wären sie schwerer: Ihre wirksame Masse beträgt etwa 0,39 statt 0,26 der freien Elektronenmasse. Das Springen über Bindungen veranschaulicht die Bewegung nur.
:::

Elektronen und Löcher tragen Strom in dieselbe Richtung: Elektronen laufen gegen das Feld, tragen aber negative Ladung; Löcher laufen mit dem Feld und tragen positive.
Nach dem Artikel über den [ohmschen Widerstand](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/ohmscher-widerstand.html) liefert jede Ladungsträgersorte ihren Anteil Ladung mal Dichte mal Beweglichkeit zur Leitfähigkeit:

$$\sigma = e\,(n\,\mu_n + p\,\mu_p)$$

In reinem Silizium entsteht jedes freie Elektron zusammen mit einem Loch, deshalb ist dort $n = p$.

## Das Fermi-Niveau

*Wie verteilen sich die Elektronen bei einer bestimmten Temperatur auf die vorhandenen Zustände?*

:::grafik
Szene: get1/halbleiterbauelemente/01-fermi-verteilung · Vorlage: funktionsgraph-lin-log
**Abbildung 6:** Die Fermi-Verteilung bei 300 K. (a) Linear: Am Fermi-Niveau ist ein Zustand mit Wahrscheinlichkeit 1/2 besetzt; die Kante ist über wenige $k_B T$ verschmiert (gestrichelt die scharfe Kante bei T = 0). (b) Halblogarithmisch: Oberhalb von etwa 3 $k_B T$ fällt die Besetzung um den Faktor 2,72 je 25,85 meV, genau wie die Boltzmann-Verteilung (gestrichelt). An der Leitungsbandkante von reinem Silizium beträgt sie nur 3·10⁻¹⁰.
:::

**Die Akteure:**

- __$f(W)$__: Besetzungswahrscheinlichkeit, also die Wahrscheinlichkeit, dass ein Zustand der Energie $W$ mit einem Elektron besetzt ist; eine Zahl zwischen 0 und 1.
- __$W_F$__: __Fermi-Niveau__, die Energie, bei der diese Wahrscheinlichkeit genau 1/2 ist; in eV.
- __$k_B T$__: thermische Energie, 25,85 meV bei 300 K. Sie bestimmt, wie stark die Wärme die Besetzung verschmiert.

**Das Zusammenspiel:** Am absoluten Nullpunkt besetzen die Elektronen die Zustände von unten her, jeden mit genau einem Elektron, bis alle untergebracht sind.
Die Grenze zwischen voll und leer heißt Fermi-Niveau.
Bei endlicher Temperatur stößt die Wärmebewegung einige Elektronen in Zustände oberhalb dieser Grenze, und darunter bleiben dafür Plätze frei.
Die scharfe Kante verschmiert über einige $k_B T$ (Abbildung 6 a).
Das Fermi-Niveau ist dann die Energie, bei der ein Zustand, falls es dort einen gibt, zur Hälfte wahrscheinlich besetzt ist.
Einige $k_B T$ oberhalb davon fällt die Besetzung exponentiell ab, um den Faktor 2,72 je 25,85 meV mehr Energie (Abbildung 6 b).

:::formel Gesetz
$$f(W) = \frac{1}{1 + \exp\!\Big(\dfrac{W - W_F}{k_B T}\Big)}$$
:::

**So liest man das:** Man setzt die Energie eines Zustands ein und erhält die Wahrscheinlichkeit, dass er besetzt ist.
Einige $k_B T$ unter $W_F$ ist sie fast 1, einige $k_B T$ darüber fast 0, genau beim Fermi-Niveau 1/2; je höher die Temperatur, desto breiter der Übergang.

Idee der Herleitung: Man sucht die Verteilung, die bei fester Gesamtenergie und Elektronenzahl die meisten Anordnungsmöglichkeiten hat, und beachtet dabei, dass jeder Zustand höchstens ein Elektron aufnimmt.

:::herleitung
**Ausgangspunkt:** die Grundannahme der statistischen Physik: Im thermischen Gleichgewicht ist jede mikroskopische Anordnung mit gleicher Gesamtenergie gleich wahrscheinlich, und man beobachtet die Verteilung mit den meisten Anordnungen.

**Annahmen:**
(i) thermisches Gleichgewicht bei der Temperatur $T$;
(ii) jeder Zustand nimmt höchstens ein Elektron auf (Pauli-Prinzip);
(iii) die Elektronen sind ununterscheidbar;
(iv) die Elektronen beeinflussen einander nicht, jedes besetzt seinen Zustand unabhängig von den anderen.

**Beweisidee:** Man zählt, auf wie viele Arten sich die Elektronen auf Gruppen gleich energiereicher Zustände verteilen lassen. Dann sucht man das Maximum dieser Zahl unter den Nebenbedingungen „feste Elektronenzahl“ und „feste Gesamtenergie“. Die Nebenbedingungen gehen über zwei Lagrange-Multiplikatoren ein; einer erweist sich als $1/(k_B T)$, der andere als $-W_F/(k_B T)$. Das Pauli-Prinzip erzeugt die „+1“ im Nenner. Wo die Besetzung klein ist, spielt sie keine Rolle mehr, und es bleibt die Boltzmann-Verteilung der klassischen Physik.

**Hinweis:** Die vollständige Rechnung gehört zur statistischen Physik und geht über den Rahmen dieses Artikels hinaus. Sie steht in jedem Lehrbuch der Festkörperphysik.

**Proben:** Weit unterhalb von $W_F$ geht $f$ gegen 1, weit oberhalb gegen 0, und bei $W_F$ ist $f$ genau 1/2. Die Verteilung ist symmetrisch um $W_F$:

$$f(W_F + \Delta W) = 1 - f(W_F - \Delta W)$$

Ein Zustand $\Delta W$ oberhalb von $W_F$ ist also genau so wahrscheinlich besetzt, wie einer $\Delta W$ unterhalb leer ist.

**Grenzen:** Gilt nur im thermischen Gleichgewicht. Fließt Strom, beschreibt man Elektronen und Löcher mit getrennten Verteilungen; das zeigt der Artikel über den [pn-Übergang unter Spannung](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/diode-pn-uebergang-spannung.html).
:::

::::beispiel Besetzung einzelner Zustände bei 300 K
**Gegeben:**
- Fermi-Verteilung bei 300 K, also thermische Energie 25,85 meV;
- drei Zustände, die (a) 25,85 meV, (b) 0,10 eV und (c) 0,5674 eV über dem Fermi-Niveau liegen; der dritte entspricht der Leitungsbandkante in reinem Silizium.

**Gesucht:** die Besetzungswahrscheinlichkeiten.

**Rechnung:** (a) Der Exponent ist genau 1:

$$f = \frac{1}{1 + \exp(1)} = \frac{1}{3{,}718} = 0{,}269$$

(b) Der Exponent ist 0,10 eV geteilt durch 25,85 meV, also 3,87:

$$f = \frac{1}{1 + \exp(3{,}87)} = \frac{1}{1 + 47{,}9} = 0{,}0205$$

(c) Der Exponent ist 0,5674 eV geteilt durch 25,85 meV, also 21,95; die 1 im Nenner spielt keine Rolle mehr:

$$f \approx \exp(-21{,}95) = 2{,}9\cdot10^{-10}$$

**Ergebnis:** **0,269 bzw. 0,0205 bzw. 2,9·10⁻¹⁰.**

**Einordnung:** Schon 0,1 eV über dem Fermi-Niveau ist nur noch jeder fünfzigste Zustand besetzt. An der Leitungsbandkante von reinem Silizium ist es nur einer von drei Milliarden; das ist der Grund für die geringe Leitfähigkeit.
::::

Für Zustände weit oberhalb des Fermi-Niveaus, genauer mindestens etwa $3\,k_B T$ darüber, genügt eine Näherung, die __Boltzmann-Näherung__:

$$f(W) \approx \exp\!\Big(-\frac{W - W_F}{k_B T}\Big)$$

Idee der Herleitung: Ist die Exponentialfunktion im Nenner groß gegen 1, darf man die 1 weglassen.

:::herleitung
**Ausgangspunkt:** die Fermi-Verteilung.

**Annahme:** (i) $W - W_F \ge 3\,k_B T$; dann ist die Exponentialfunktion im Nenner mindestens 20.

**Schritt 1**: Im Nenner ist die 1 klein gegen die Exponentialfunktion und wird weggelassen:

$$f(W) = \frac{1}{1 + \exp\!\big((W - W_F)/(k_B T)\big)}$$

$$\approx \frac{1}{\exp\!\big((W - W_F)/(k_B T)\big)}$$

**Schritt 2**: Der Kehrwert einer Exponentialfunktion ist die Exponentialfunktion des negativen Arguments:

$$f(W) \approx \exp\!\Big(-\frac{W - W_F}{k_B T}\Big)$$

**Proben:** Bei $3\,k_B T$ ist der genaue Wert 0,0474, die Näherung 0,0498, also 5 % zu groß. Bei $5\,k_B T$ weichen beide nur noch um 0,7 % voneinander ab (0,00669 gegen 0,00674).

**Grenzen:** In der Nähe von $W_F$ ist die Näherung falsch, bei $W = W_F$ liefert sie 1 statt 1/2.
:::

Die Elektronen im Leitungsband sitzen fast alle wenige $k_B T$ über der Kante $W_L$, denn höher fällt die Besetzung exponentiell ab.
Alle Zustände dieses Bereichs zusammen wirken wie __$N_L$__ Plätze genau an der Kante, die __effektive Zustandsdichte__; bei Silizium und 300 K sind das 3,2·10¹⁹ pro cm³.
Für die Löcher, also die unbesetzten Zustände, gilt dasselbe an der Valenzbandkante mit __$N_V$__, 1,8·10¹⁹ pro cm³:

:::formel Formel
$$n = N_L\,\exp\!\Big(-\frac{W_L - W_F}{k_B T}\Big), \qquad p = N_V\,\exp\!\Big(-\frac{W_F - W_V}{k_B T}\Big)$$
:::

**So liest man das:** Die Elektronendichte ist die Zahl der Plätze an der Leitungsbandkante mal der Wahrscheinlichkeit, dass ein Platz dort besetzt ist.
Je näher das Fermi-Niveau am Leitungsband liegt, desto mehr Elektronen gibt es, und je näher es am Valenzband liegt, desto mehr Löcher.
Rückt $W_F$ um 59,5 meV näher an $W_L$, verzehnfacht sich $n$.

Idee der Herleitung: Man summiert über alle Zustände des Bandes Platzzahl mal Besetzung und fasst das Ergebnis an der Bandkante zusammen.

:::herleitung
**Ausgangspunkt:** Zahl der Elektronen pro Volumen = Summe über alle Zustände des Leitungsbands, jeder mit seiner Besetzungswahrscheinlichkeit $f(W)$.

**Annahmen:**
(i) Boltzmann-Näherung im ganzen Leitungsband, also $W_L - W_F \ge 3\,k_B T$;
(ii) die Zahl der Zustände je Energieintervall nahe der Kante folgt dem Verlauf, den die Quantenmechanik für Elektronen mit der wirksamen Masse im Kristall liefert.

**Schritt 1**: Mit der Boltzmann-Näherung zerfällt die Besetzung in einen Faktor an der Kante und einen Faktor für den Abstand $W - W_L$ über der Kante:

$$\exp\!\Big(-\frac{W - W_F}{k_B T}\Big)$$

$$= \exp\!\Big(-\frac{W_L - W_F}{k_B T}\Big)\cdot\exp\!\Big(-\frac{W - W_L}{k_B T}\Big)$$

**Schritt 2** (entscheidender Schritt): Der erste Faktor ist für alle Zustände gleich und kommt vor die Summe. Die Summe über die Zustände mal den zweiten Faktor hängt nur noch vom Material und von der Temperatur ab; man nennt sie $N_L$:

$$n = \exp\!\Big(-\frac{W_L - W_F}{k_B T}\Big)\cdot\underbrace{\sum_{\text{Zustände}}\exp\!\Big(-\frac{W - W_L}{k_B T}\Big)}_{=:\,N_L}$$

**Schritt 3**: Für Löcher zählt man unbesetzte Zustände im Valenzband. Wegen der Symmetrie der Fermi-Verteilung gilt für Zustände mindestens $3\,k_B T$ unter $W_F$:

$$1 - f(W) \approx \exp\!\Big(-\frac{W_F - W}{k_B T}\Big)$$

Dieselbe Rechnung von der Kante $W_V$ nach unten liefert $p$ mit $N_V$.

**Hinweis:** Wie man die Summe in Schritt 2 als Integral über die Zustandsdichte auswertet ($N_L \propto T^{3/2}$), zeigt der Artikel über die [Ladungsträgerdichte](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/zustandsdichte-und-fermi-verteilung/ladungstraegerdichte.html). Hier genügt das Ergebnis, $3{,}2\cdot10^{19}\ \mathrm{cm^{-3}}$ für Silizium bei 300 K.

**Proben:** Einheit cm⁻³ auf beiden Seiten. Rückt $W_F$ immer weiter unter $W_L$, geht $n$ gegen null, wie es sein muss.

**Grenzen:** Bei sehr hoher Dotierung (über etwa 10¹⁹ cm⁻³) rückt $W_F$ an oder in das Band, die Boltzmann-Näherung versagt („entarteter Halbleiter“).
:::

In reinem Silizium ist $n = p$; das Fermi-Niveau muss deshalb so liegen, dass beide Ausdrücke gleich groß werden.
Weil $N_L$ und $N_V$ ähnlich sind, liegt es fast genau in der Mitte der Lücke, rechnerisch 7 meV darunter.
Man nennt diese Lage das __Eigenleitungsniveau__ __$W_i$__.
Die Leitungsbandkante liegt dann 0,5674 eV darüber, die Valenzbandkante 0,5526 eV darunter, und die Besetzung an der Leitungsbandkante ist nur noch 3·10⁻¹⁰ (Abbildung 6 b).

::::beispiel Elektronen- und Löcherdichte in reinem Silizium
**Gegeben** (Silizium, 300 K):
- effektive Zustandsdichten 3,2·10¹⁹ cm⁻³ (Leitungsband) und 1,8·10¹⁹ cm⁻³ (Valenzband);
- thermische Energie 25,85 meV;
- Fermi-Niveau beim Eigenleitungsniveau, 0,5674 eV unter $W_L$ und 0,5526 eV über $W_V$.

**Gesucht:** $n$ und $p$.

**Rechnung:** (a) Elektronen:

$$n = 3{,}2\cdot10^{19}\ \mathrm{cm^{-3}}\cdot\exp\!\Big(-\frac{0{,}5674}{0{,}02585}\Big)$$

$$= 3{,}2\cdot10^{19}\ \mathrm{cm^{-3}}\cdot2{,}94\cdot10^{-10} = 9{,}4\cdot10^{9}\ \mathrm{cm^{-3}}$$

(b) Löcher:

$$p = 1{,}8\cdot10^{19}\ \mathrm{cm^{-3}}\cdot\exp\!\Big(-\frac{0{,}5526}{0{,}02585}\Big)$$

$$= 1{,}8\cdot10^{19}\ \mathrm{cm^{-3}}\cdot5{,}2\cdot10^{-10} = 9{,}4\cdot10^{9}\ \mathrm{cm^{-3}}$$

**Ergebnis:** **Beide Dichten sind 9,4·10⁹ cm⁻³**, in guter Übereinstimmung mit dem Messwert 9,65·10⁹ cm⁻³.

**Einordnung:** Gleich große Dichten verlangt die Paarbildung. Weil das Valenzband weniger effektive Plätze hat als das Leitungsband, muss das Fermi-Niveau etwas näher am Valenzband liegen, damit beide Produkte gleich werden; daher die 7 meV unter der Mitte.
::::

Ein häufiger Fehler ist, das Fermi-Niveau undotierter Halbleiter als Mitte der Bandlücke zu definieren; es ergibt sich dort aus der Bedingung $n = p$, eine Definition ist das nicht.

:::frage
„Wie kann das Fermi-Niveau in der Bandlücke liegen, wenn es dort gar keine Zustände gibt?“
Das Fermi-Niveau ist kein Zustand, sondern eine Kenngröße der Verteilung, ähnlich wie ein Mittelwert, den kein einzelner Messwert treffen muss. Es gibt an, wo die Besetzungswahrscheinlichkeit 1/2 wäre, falls es dort einen Zustand gäbe. In reinem Silizium liegt es in der Lücke, weil das Leitungsband oben (wenige besetzte Plätze) und das Valenzband unten (ebenso wenige leere Plätze) im Gleichgewicht stehen müssen. Gleich groß sind dann die Zahl der Elektronen oben (3,2·10¹⁹ Plätze mal 2,9·10⁻¹⁰) und die der Löcher unten (1,8·10¹⁹ Plätze mal 5,2·10⁻¹⁰). Weil das Valenzband weniger Plätze hat, muss sein Ausläufer etwas größer sein; deshalb liegt $W_F$ 7 meV unter der Mitte.
:::

## Eigenleitung: wie viele Ladungsträger es gibt

*Wie viele freie Elektronen hat reines Silizium, und warum hängt ihre Zahl so stark von der Temperatur ab?*

:::grafik
Szene: get1/halbleiterbauelemente/01-eigenleitung-temperatur · Vorlage: funktionsgraph-semilog
**Abbildung 7:** Eigenleitungsdichte n_i von Silizium über der Temperatur, halblogarithmisch, berechnet aus n_i = 10¹⁰ cm⁻³ bei 300 K und dem Temperaturgang der Herleitung unten. Sie wächst bei 300 K um 8,3 % pro Kelvin, bei 400 K noch um 4,7 %, und erreicht die Dotierung der Beispieldiode (10¹⁶ cm⁻³) erst bei 655 K.
:::

**Die Akteure:**

- __$n_i$__: __Eigenleitungsdichte__, die Dichte der Elektronen und ebenso der Löcher in reinem Silizium; 10¹⁰ cm⁻³ bei 300 K (genauester Messwert 9,65·10⁹ cm⁻³, hier gerundet).
- __$G$__: __Generationsrate__, die Zahl neu entstehender Paare pro cm³ und Sekunde.
- __$R$__: __Rekombinationsrate__, die Zahl verschwindender Paare pro cm³ und Sekunde. Bei einer __Rekombination__ fällt ein freies Elektron in ein Loch zurück; beide verschwinden, und die Energie geht als Wärme ans Gitter.

**Das Zusammenspiel:** Generation und Rekombination laufen ständig, auch ohne äußere Einwirkung.
Die Generation hängt nur davon ab, wie oft die Wärmebewegung genug Energie an einer Stelle sammelt.
Die Rekombination dagegen braucht ein Elektron und ein Loch am selben Ort und wird deshalb umso häufiger, je mehr von beiden da sind.
Die Dichten wachsen, bis beide Raten gleich sind.
In reinem Silizium bei 300 K ist das bei 10¹⁰ Elektronen und ebenso vielen Löchern pro cm³ erreicht.
Ein Kubikzentimeter enthält 5·10²² Atome: Auf 5·10¹² Atome kommt ein einziges freies Elektron.

:::formel Gesetz
$$n\,p = n_i^{2}$$
:::

**So liest man das:** Das Produkt aus Elektronen- und Löcherdichte ist im thermischen Gleichgewicht eine Materialkonstante, die nur von der Temperatur abhängt; die Beziehung heißt __Massenwirkungsgesetz__.
Sie gilt auch dann, wenn $n$ und $p$ verschieden sind: Wird eine Sorte häufiger, wird die andere im selben Verhältnis seltener.

Idee der Herleitung: Im Gleichgewicht entstehen pro Sekunde genau so viele Paare, wie verschwinden.

:::herleitung
**Ausgangspunkt:** Bilanz der Elektron-Loch-Paare in einem festen Volumen.

**Annahmen:**
(i) thermisches Gleichgewicht: keine äußere Spannung, kein Licht, konstante Temperatur;
(ii) Modell: Paare entstehen und verschwinden direkt zwischen den Bändern; die Rekombinationsrate $R$ (verschwindende Paare pro cm³ und Sekunde) ist dann proportional zu beiden Dichten, weil sich ein Elektron und ein Loch treffen müssen;
(iii) die Generationsrate $G$ (neu entstehende Paare pro cm³ und Sekunde) hängt nur von Material und Temperatur ab.

**Schritt 1**: Im Gleichgewicht ändern sich die Dichten nicht, also sind die Raten gleich:

$$G = R$$

**Schritt 2**: Nach Annahme (ii) ist $R$ gleich einer Materialkonstanten $r$ mal $n$ mal $p$:

$$G = r\,n\,p \quad\Longrightarrow\quad n\,p = \frac{G}{r}$$

**Schritt 3** (entscheidender Schritt): $G$ und $r$ hängen nicht davon ab, ob und wie das Silizium dotiert ist; also gilt das auch für das Produkt $n\,p$. Im reinen Silizium ist $n = p = n_i$, also:

$$n\,p = n_i \cdot n_i = n_i^{2}$$

**Ergebnis:**

$$n\,p = n_i^2$$

**Woher die Faktoren kommen:** $n_i^2$ ist das Verhältnis $G/r$. Das Quadrat entsteht, weil $R$ proportional zum Produkt $n\,p$ ist und im reinen Silizium beide Faktoren $n_i$ sind.

**Gültigkeit des Modells:** In Silizium laufen Generation und Rekombination überwiegend über Kristallfehler (Störstellen) als Zwischenstufe, und deren Raten folgen nicht genau Annahme (ii). Das Ergebnis gilt trotzdem, weil es eine Aussage über das Gleichgewicht ist und nicht davon abhängt, auf welchem Weg Paare entstehen und verschwinden.

**Zweiter Weg:** Multipliziert man die Formeln für $n$ und $p$ aus dem Abschnitt *Das Fermi-Niveau*, fällt das Fermi-Niveau heraus:

$$n\,p = N_L N_V \exp\!\Big(-\frac{(W_L - W_F) + (W_F - W_V)}{k_B T}\Big)$$

$$= N_L N_V \exp\!\Big(-\frac{W_g}{k_B T}\Big)$$

Die rechte Seite enthält nur Materialgrößen und die Temperatur, nicht die Lage von $W_F$, die die Dotierung festlegt.

**Proben:** Einheit cm⁻⁶ auf beiden Seiten. Reines Silizium: 10¹⁰ mal 10¹⁰ ergibt 10²⁰ cm⁻⁶.

**Grenzen:** Gilt nur im Gleichgewicht und ohne Entartung, also bei Dotierungen unter etwa 10¹⁸ cm⁻³. Unter Licht oder wenn eine äußere Spannung Ladungsträger zuführt oder absaugt, weicht $n\,p$ von $n_i^2$ ab.
:::

:::frage
„Warum rekombinieren nicht einfach alle Elektronen mit allen Löchern?“
Sie rekombinieren ständig, aber die Wärmebewegung erzeugt im selben Takt neue Paare. Die Rekombination wird mit dem Produkt $n\,p$ häufiger, die Generation hängt nur von der Temperatur ab. Gleichgewicht herrscht, wenn beide gleich sind, und genau das legt das Massenwirkungsgesetz fest. Ein einzelnes freies Elektron lebt in Silizium typischerweise Mikrosekunden bis Millisekunden, je nach Reinheit des Kristalls; in derselben Zeit entstehen anderswo neue.
:::

Wie viele Paare es im Gleichgewicht gibt, folgt aus dem zweiten Weg: In reinem Silizium ist $n = p = n_i$, also ist $n_i^2$ gleich der rechten Seite dort.

:::formel Formel
$$n_i = \sqrt{N_L\,N_V}\;\exp\!\Big(-\frac{W_g}{2\,k_B T}\Big)$$
:::

**So liest man das:** Eingabe sind Bandlücke und Temperatur, Ausgabe ist die Dichte jeder der beiden Ladungsträgersorten.
Entscheidend ist der Exponent, die halbe Bandlücke geteilt durch die thermische Energie, bei Silizium 21,7.
Halb, weil jedes Aufbrechen einer Bindung die volle Lücke kostet, aber zwei Ladungsträger erzeugt: Das Produkt $n\,p$ hängt mit der vollen Lücke von der Temperatur ab, jede einzelne Dichte nur mit der halben.
Mit den Zahlen für Silizium liefert die Formel 9,4·10⁹ cm⁻³.

Idee der Herleitung: Man setzt im zweiten Weg zum Massenwirkungsgesetz $n = p = n_i$ und zieht die Wurzel.

:::herleitung
**Ausgangspunkt:** das Ergebnis des zweiten Wegs zum Massenwirkungsgesetz:

$$n\,p = N_L N_V \exp\!\Big(-\frac{W_g}{k_B T}\Big)$$

**Annahme:** (i) reines Silizium, also $n = p = n_i$.

**Schritt 1**: Einsetzen:

$$n_i^2 = N_L N_V \exp\!\Big(-\frac{W_g}{k_B T}\Big)$$

**Schritt 2**: Wurzel ziehen; die Wurzel einer Exponentialfunktion halbiert ihr Argument:

$$n_i = \sqrt{N_L N_V}\;\exp\!\Big(-\frac{W_g}{2\,k_B T}\Big)$$

**Folgerung für den Temperaturgang** (entscheidender Schritt für die Praxis): $N_L$ und $N_V$ wachsen beide wie $T^{3/2}$ (Ergebnis der Zustandsdichte-Rechnung im Artikel über die [Ladungsträgerdichte](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/zustandsdichte-und-fermi-verteilung/ladungstraegerdichte.html)), ihr Produkt unter der Wurzel also wie $T^3$. Die Bandlücke nimmt mit steigender Temperatur leicht ab; um 300 K gilt in guter Näherung

$$W_g(T) \approx W_{g0} - \alpha\,T, \qquad W_{g0} = 1{,}206\ \mathrm{eV}.$$

Der Anteil $\alpha T$ ergibt im Exponenten nur einen konstanten Faktor. Damit lautet der Logarithmus von $n_i$:

$$\ln n_i = \tfrac{3}{2}\ln T - \frac{W_{g0}}{2\,k_B T} + \text{konstant}$$

Leitet man nach $T$ ab, bleiben zwei Beiträge; ausgewertet bei 300 K:

$$\frac{1}{n_i}\,\frac{\mathrm{d}n_i}{\mathrm{d}T} = \frac{3}{2\,T} + \frac{W_{g0}}{2\,k_B T^{2}}$$

$$= 0{,}0050\ \mathrm{K^{-1}} + 0{,}0778\ \mathrm{K^{-1}} = 0{,}083\ \mathrm{K^{-1}}$$

Der Logarithmus eines Produkts ist die Summe der Logarithmen seiner Faktoren, und die Ableitung einer Summe ist die Summe der Ableitungen. Deshalb addieren sich beim Ableiten die Beiträge von Vorfaktor und Exponentialfunktion: 0,5 % und 7,8 % je Kelvin ergeben 8,3 %.

**Woher die Faktoren kommen:** Die Wurzel stammt aus $n = p$, der Faktor 1/2 im Exponenten ebenfalls; der Vorfaktor $\sqrt{N_L N_V}$ ist das geometrische Mittel der Platzzahlen beider Bänder.

**Proben:** Einheit cm⁻³. Zahlenwert: Die Wurzel aus 3,2·10¹⁹ mal 1,8·10¹⁹ cm⁻⁶ ist 2,4·10¹⁹ cm⁻³, der Exponentialfaktor 3,9·10⁻¹⁰; zusammen 9,4·10⁹ cm⁻³. Grenzfall $T \to 0$: $n_i \to 0$, Silizium wird zum Isolator.

**Grenzen:** Boltzmann-Näherung an beiden Bandkanten; in reinem Silizium ist sie immer erfüllt.
:::

Abbildung 7 zeigt, was das bedeutet.
Um 300 K verdoppelt sich die Dichte alle 8,4 K; weil die relative Zunahme mit steigender Temperatur kleiner wird (bei 400 K noch 4,7 % pro Kelvin), ist sie bei 400 K 525-mal so groß wie bei 300 K.
Bei 655 K (382 °C) erreicht sie 10¹⁶ cm⁻³, so viel wie die Dotierung der Beispieldiode im nächsten Abschnitt.
Oberhalb davon bestimmt die Wärme die Zahl der Ladungsträger, und die Dotierung verliert ihre Wirkung.

::::beispiel Eigenleitungsdichte bei 300 K und bei 400 K
**Gegeben:**
- Eigenleitungsdichte bei 300 K: 10¹⁰ cm⁻³;
- auf 0 K extrapolierte Bandlücke 1,206 eV, Boltzmann-Konstante 8,617·10⁻⁵ eV/K;
- Temperaturgang aus der Herleitung oben: Vorfaktor wie $T^{3/2}$, Exponent mit $W_{g0}$.

**Gesucht:** $n_i$ bei 400 K, also bei 127 °C.

**Rechnung:** Teilt man die Formel für $n_i$ bei 400 K durch die bei 300 K, fallen alle Konstanten heraus:

$$\frac{n_i(400\ \mathrm{K})}{n_i(300\ \mathrm{K})} = \Big(\frac{400}{300}\Big)^{3/2}\exp\!\Big[\frac{W_{g0}}{2\,k_B}\Big(\frac{1}{300\ \mathrm{K}} - \frac{1}{400\ \mathrm{K}}\Big)\Big]$$

$$\frac{W_{g0}}{2\,k_B} = \frac{1{,}206\ \mathrm{eV}}{2\cdot8{,}617\cdot10^{-5}\ \mathrm{eV/K}} = 6998\ \mathrm{K}$$

$$\frac{n_i(400\ \mathrm{K})}{n_i(300\ \mathrm{K})} = 1{,}540\cdot\exp(6998\cdot8{,}33\cdot10^{-4})$$

$$= 1{,}540\cdot\exp(5{,}83) = 1{,}540\cdot341 = 525$$

**Ergebnis:** **Bei 400 K beträgt die Eigenleitungsdichte 5,3·10¹² cm⁻³**, 525-mal so viel wie bei 300 K.

**Einordnung:** Hundert Kelvin mehr vervielfachen die Eigenleitung um mehr als das Fünfhundertfache. Gegen eine Dotierung von 10¹⁶ cm⁻³ ist sie damit immer noch fast zweitausendfach unterlegen; erst bei 655 K holt sie auf.
::::

:::frage
„Warum leitet reines Silizium warm besser, Kupfer aber schlechter?“
In Kupfer ist die Zahl der freien Elektronen fest, 8,5·10²² pro cm³. Mit der Temperatur schwingt das Gitter stärker, die Elektronen stoßen öfter, und ihre Beweglichkeit sinkt; der Widerstand steigt um 0,39 % pro Kelvin. In reinem Silizium sinkt die Beweglichkeit ebenfalls, aber die Zahl der Ladungsträger wächst bei Raumtemperatur um 8,3 % pro Kelvin, und das überwiegt bei weitem. Heißleiter, die im Artikel über den [ohmschen Widerstand](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/ohmscher-widerstand.html) vorkommen, bestehen aus halbleitenden Metalloxiden und nutzen einen verwandten Effekt: Auch bei ihnen wird die Leitung mit steigender Temperatur thermisch aktiviert.
:::

## Dotierung

*Wie macht man aus Silizium einen guten Leiter für genau eine Sorte von Ladungsträgern?*

:::grafik
Szene: get1/halbleiterbauelemente/01-baender-dotiert · Vorlage: banddiagramm-niveaus
**Abbildung 8:** Bänder von n- und p-Silizium mit je 10¹⁶ Fremdatomen pro cm³, Lagen berechnet. Donatorniveau $W_D$ 45 meV unter $W_L$, Akzeptorniveau $W_A$ 45 meV über $W_V$. Das Fermi-Niveau rückt um 0,36 eV aus der Mitte $W_i$ heraus, bis auf 0,21 eV an $W_L$ bzw. 0,19 eV an $W_V$; symmetrisch ist das nicht, weil das Valenzband weniger effektive Plätze hat. Teilchenzahlen schematisch.
:::

**Die Akteure:**

- __$N_D$__: Dichte der Fremdatome mit fünf Valenzelektronen, etwa Phosphor; in cm⁻³, in der Beispieldiode 10¹⁶.
- __$N_A$__: Dichte der Fremdatome mit drei Valenzelektronen, etwa Bor; ebenfalls 10¹⁶ cm⁻³.
- __$W_D$__, __$W_A$__: Energie des locker gebundenen fünften Elektrons bzw. des freien vierten Bindungsplatzes; 45 meV unter $W_L$ bzw. über $W_V$.

**Das Zusammenspiel:** Setzt man gezielt Fremdatome in den Kristall ein, nennt man das __Dotieren__.
Ein Phosphoratom (Abbildung 4 b) nimmt den Platz eines Siliziumatoms ein.
Vier seiner fünf Valenzelektronen bilden die vier Bindungen; das fünfte passt in keine Bindung und wird nur mit 45 meV vom Rumpf gehalten.
Das ist nicht einmal das Doppelte der thermischen Energie und ein Fünfundzwanzigstel der Bandlücke.
Zudem bietet das Leitungsband bei 10¹⁶ cm⁻³ rund 3200-mal mehr Plätze, als es Donatoren gibt; ein Elektron findet dort also weit mehr Zustände als an seinem Rumpf.
Beides zusammen bewirkt, dass bei 300 K über 99,6 % der Phosphoratome ihr fünftes Elektron abgegeben haben (nachgerechnet im Beispiel zum Fermi-Niveau weiter unten).
Im Bändermodell liegt sein Niveau $W_D$ dicht unter dem Leitungsband (Abbildung 8), und von dort gelangt es mit wenig Energie hinein.
Zurück bleibt ein fest eingebauter, positiv geladener Rumpf P⁺.
Solche Fremdatome heißen __Donatoren__ (Geber), das Silizium __n-dotiert__, weil negative Ladungsträger die Leitung tragen.

Bor (Abbildung 4 c) hat nur drei Valenzelektronen, einer der vier Bindungen fehlt also ein Elektron.
Ein Elektron aus einer Nachbarbindung füllt diesen Platz mit einem Aufwand von 45 meV.
Dadurch wird das Bor zum negativ geladenen Rumpf B⁻, und das Loch wandert davon.
Solche Fremdatome heißen __Akzeptoren__ (Nehmer), das Silizium __p-dotiert__.
Die Rümpfe P⁺ und B⁻ sind über vier Bindungen fest ins Gitter eingebaut und bewegen sich nicht; beweglich sind nur Elektronen und Löcher.

Typische Dotierungen liegen zwischen 10¹⁵ und 10²⁰ cm⁻³, ein Fremdatom auf 5·10⁷ bis 500 Siliziumatome.
Schon 10¹⁵ cm⁻³ sind hunderttausendmal mehr als $n_i$; die Dotierung legt die Ladungsträger deshalb vollständig fest.

„Halbmetall“ heißt Silizium nur in der Chemie; in der Festkörperphysik ist ein Halbmetall ein Stoff mit überlappenden Bändern wie Bismut, und Silizium ist ein Halbleiter.

:::frage
„Warum ist das fünfte Elektron so locker gebunden, wenn ein Wasserstoffatom 13,6 eV braucht, um sein Elektron abzugeben?“
Das fünfte Elektron umkreist den Phosphorrumpf ähnlich wie das Elektron den Kern im Wasserstoffatom, aber mitten im Silizium. Die umgebenden Atome werden vom Feld des Rumpfes polarisiert und schwächen es um den Faktor 11,7 ab (die relative Permittivität); die Bindungsenergie sinkt dadurch um 11,7², also um den Faktor 137. Zudem bewegt sich das Elektron im Kristall, als hätte es nur 0,26 der freien Elektronenmasse. Zusammen ergibt das 13,6 eV mal 0,26 durch 137, also etwa 26 meV. Gemessen werden 45 meV: Rechnet man genauer mit der richtungsabhängigen wirksamen Masse, kommt man auf etwa 31 meV, und den Rest liefert die unvollständige Abschirmung direkt am Rumpf. Die Bahn hat dann einen Radius von etwa 2,4 nm, zehn Bindungslängen, und umschließt rund 2800 Siliziumatome; deshalb darf man den Kristall dabei wie einen gleichmäßigen Stoff mit Permittivität behandeln.
:::

:::formel Formel
$$n \approx N_D, \qquad p \approx \frac{n_i^{2}}{N_D} \qquad \text{(n-Silizium)}$$
:::

**So liest man das:** Im n-Silizium stellt jeder Donator ein Elektron; die Elektronendichte ist gleich der Dotierung.
Die Löcher folgen aus dem Massenwirkungsgesetz: Je stärker dotiert, desto weniger Löcher.
Für p-Silizium gilt dasselbe mit vertauschten Rollen: Die Löcherdichte ist gleich der Akzeptordichte $N_A$, die Elektronendichte ist $n_i^2$ geteilt durch $N_A$.
Die zahlreiche Sorte heißt __Majoritätsträger__, die seltene __Minoritätsträger__; bei 10¹⁶ cm⁻³ stehen sie im Verhältnis 10¹² zu 1.

Idee der Herleitung: Das Material bleibt insgesamt neutral, und das Massenwirkungsgesetz koppelt die beiden Dichten.

:::herleitung
**Ausgangspunkt:** Ladungsneutralität eines gleichmäßig dotierten Gebiets und das Massenwirkungsgesetz.

**Annahmen:**
(i) alle Donatoren ionisiert (über 99,6 % bei 300 K);
(ii) keine Akzeptoren im n-Gebiet;
(iii) Dotierung groß gegen $n_i$.

**Schritt 1**: Neutralität: Die positiven Ladungen (Löcher und P⁺-Rümpfe) gleichen die negativen (Elektronen) genau aus:

$$p + N_D = n$$

**Schritt 2**: Das Massenwirkungsgesetz liefert die Löcherdichte:

$$p = \frac{n_i^{2}}{n}$$

**Schritt 3** (entscheidender Schritt): Nach Schritt 1 ist $n$ mindestens $N_D$, nach Schritt 2 also $p$ höchstens $n_i^2/N_D$. Für 10¹⁶ cm⁻³ sind das 10⁴ cm⁻³, zwölf Zehnerpotenzen weniger als $N_D$. In Schritt 1 darf man $p$ deshalb weglassen:

$$n \approx N_D, \qquad p \approx \frac{n_i^{2}}{N_D}$$

**Woher die Faktoren kommen:** $N_D$ aus der Neutralität, $n_i^2$ aus dem Massenwirkungsgesetz.

**Proben:** Einheit cm⁻³. Ohne Annahme (iii) ergeben Schritt 1 und 2 eine quadratische Gleichung für $n$ mit der Lösung

$$n = \frac{N_D}{2} + \sqrt{\Big(\frac{N_D}{2}\Big)^{2} + n_i^{2}}$$

Ohne Dotierung liefert sie $n_i$ (reines Silizium), bei einer Dotierung weit über $n_i$ den Näherungswert $N_D$.

**Grenzen:** Unterhalb von etwa 100 K binden die Donatoren ihre Elektronen wieder („Ausfrieren“), oberhalb von 655 K überwiegt bei 10¹⁶ cm⁻³ die Eigenleitung.
:::

::::beispiel Ladungsträger und Leitfähigkeit von n-Silizium mit 10¹⁶ Phosphoratomen pro cm³
**Gegeben:**
- Dotierung 10¹⁶ cm⁻³, Eigenleitungsdichte 10¹⁰ cm⁻³, 5·10²² Siliziumatome pro cm³;
- Beweglichkeiten bei dieser Dotierung 1250 (Elektronen) und 450 cm²/(V s) (Löcher), in reinem Silizium 1400 und 450 cm²/(V s); gerundete Werte des Beispielsystems, real ist die Löcherbeweglichkeit bei 10¹⁶ cm⁻³ etwas kleiner, rund 430 cm²/(V s).

**Gesucht:** $n$ und $p$, der Anteil der Fremdatome und die Leitfähigkeit im Vergleich mit reinem Silizium.

**Rechnung:** Dichten nach der Formel:

$$n = 10^{16}\ \mathrm{cm^{-3}}, \qquad p = \frac{(10^{10}\ \mathrm{cm^{-3}})^{2}}{10^{16}\ \mathrm{cm^{-3}}} = 10^{4}\ \mathrm{cm^{-3}}$$

Anteil der Fremdatome:

$$\frac{10^{16}}{5\cdot10^{22}} = 2\cdot10^{-7}$$

Leitfähigkeit nach dem Artikel über den ohmschen Widerstand; der Löcherbeitrag ist um zwölf Zehnerpotenzen kleiner und fällt weg:

$$\sigma = e\,(n\,\mu_n + p\,\mu_p) \approx e\,n\,\mu_n$$

$$= 1{,}602\cdot10^{-19}\ \mathrm{C}\cdot10^{16}\ \mathrm{cm^{-3}}\cdot1250\ \mathrm{\tfrac{cm^2}{V\,s}} = 2{,}00\ \mathrm{S/cm}$$

Reines Silizium zum Vergleich:

$$\sigma_i = 1{,}602\cdot10^{-19}\ \mathrm{C}\cdot10^{10}\ \mathrm{cm^{-3}}\cdot(1400 + 450)\ \mathrm{\tfrac{cm^2}{V\,s}} = 2{,}96\cdot10^{-6}\ \mathrm{S/cm}$$

**Ergebnis:** **10¹⁶ Elektronen und 10⁴ Löcher pro cm³; spezifischer Widerstand 0,50 Ωcm statt 3,4·10⁵ Ωcm.**

**Einordnung:** Ein Phosphoratom auf fünf Millionen Siliziumatome steigert die Leitfähigkeit auf das 680 000-Fache. Kupfer (1,68·10⁻⁶ Ωcm) leitet trotzdem noch 300 000-mal besser, denn dort ist jedes Atom an der Leitung beteiligt.
::::

:::fehlvorstellung
„n-dotiertes Silizium ist negativ geladen, es hat ja zusätzliche Elektronen.“
Das liegt nahe, weil „n“ für negativ steht. Jedes freie Elektron stammt aber von einem Donator, der dabei zum positiven Rumpf P⁺ geworden ist; Elektronen und Rümpfe gleichen sich genau aus. Das „n“ bezeichnet nur die Sorte der Majoritätsträger. Bei 10¹⁶ cm⁻³ liegen zwei Rümpfe im Mittel 46 nm auseinander; schon über wenige solcher Abstände gleichen die Elektronen ihre Ladung aus, und von außen wirkt das Gebiet ungeladen.
:::

Wo liegt das Fermi-Niveau im dotierten Silizium?
Nach der Formel für $n$ verlangen mehr Elektronen eine höhere Besetzung des Leitungsbands, also ein Fermi-Niveau näher an $W_L$:

:::formel Formel
$$W_F - W_i = k_B T\,\ln\frac{n}{n_i}$$
:::

**So liest man das:** Jede Verzehnfachung der Elektronendichte hebt das Fermi-Niveau um 59,5 meV an.
Im p-Silizium ist $n$ kleiner als $n_i$, der Logarithmus negativ, und $W_F$ rückt unter die Mitte.
In der Beispieldiode liegt es 0,357 eV über bzw. unter $W_i$ (Abbildung 8).

Idee der Herleitung: Man teilt die Formel für $n$ im dotierten durch die im reinen Silizium; Bandkante und Zustandsdichte fallen heraus.

:::herleitung
**Ausgangspunkt:** die Formel für $n$ aus dem Abschnitt *Das Fermi-Niveau*, einmal für das dotierte Silizium und einmal für das reine, in dem das Fermi-Niveau beim Eigenleitungsniveau $W_i$ liegt und die Elektronendichte $n_i$ ist.

**Annahmen:**
(i) Boltzmann-Näherung;
(ii) dasselbe Material bei derselben Temperatur, also gleiche $N_L$ und $W_L$.

**Schritt 1**: Quotient der beiden Ausdrücke; $N_L$ kürzt sich:

$$\frac{n}{n_i} = \frac{\exp\big(-(W_L - W_F)/(k_B T)\big)}{\exp\big(-(W_L - W_i)/(k_B T)\big)} = \exp\!\Big(\frac{W_F - W_i}{k_B T}\Big)$$

**Schritt 2**: Logarithmieren und mit $k_B T$ multiplizieren:

$$W_F - W_i = k_B T\,\ln\frac{n}{n_i}$$

**Proben:** Für $n = n_i$ ist der Abstand null. Für 10¹⁶ cm⁻³ ist er 25,85 meV mal ln(10⁶), also 25,85 meV mal 13,8, gleich 0,357 eV.

**Grenzen:** Die Boltzmann-Näherung verlangt $W_F$ mindestens $3\,k_B T$ unter $W_L$; im n-Silizium gilt das bis etwa 10¹⁸ cm⁻³.
:::

::::beispiel Fermi-Niveau und Donatorbesetzung in der Beispieldiode
**Gegeben:** n-Gebiet mit 10¹⁶ cm⁻³; Eigenleitungsdichte 10¹⁰ cm⁻³; effektive Zustandsdichte 3,2·10¹⁹ cm⁻³; Donatorniveau 45 meV unter $W_L$; thermische Energie 25,85 meV.

**Gesucht:** Lage des Fermi-Niveaus und der Anteil der Donatoren, die ihr Elektron noch tragen.

**Rechnung:** (a) Abstand zur Bandmitte nach der Formel:

$$W_F - W_i = 25{,}85\ \mathrm{meV}\cdot\ln(10^{6}) = 0{,}357\ \mathrm{eV}$$

Abstand zur Leitungsbandkante, aufgelöst aus der Formel für $n$:

$$W_L - W_F = k_B T\,\ln\frac{N_L}{n} = 25{,}85\ \mathrm{meV}\cdot\ln(3200) = 0{,}209\ \mathrm{eV}$$

(b) Das Donatorniveau liegt 45 meV unter $W_L$, also 0,164 eV über $W_F$. Besetzungswahrscheinlichkeit nach Fermi:

$$f(W_D) = \frac{1}{1 + \exp(0{,}164/0{,}02585)} = \frac{1}{1 + 569} = 0{,}0018$$

**Ergebnis:** **$W_F$ liegt 0,21 eV unter $W_L$; nur 0,18 % der Donatoren tragen ihr Elektron noch.** Rechnet man genauer mit den zwei Spinrichtungen am Donator, sind es 0,36 %; in jedem Fall sind über 99,6 % ionisiert.

**Einordnung:** Das Fermi-Niveau liegt bei 300 K unter dem Donatorniveau; deshalb ist das fünfte Elektron fast nie an seinem Rumpf. Die beiden Rechenwege in (a) passen auf 1 meV zusammen: Zieht man 0,357 eV vom Abstand 0,5674 eV zwischen $W_i$ und $W_L$ ab, bleiben 0,210 eV.
::::

Ein häufiger Fehler ist, das Fermi-Niveau im n-dotierten Halbleiter den höchsten besetzten Zustand zu nennen.
Bei 300 K stimmt das nicht: $W_F$ liegt 0,21 eV unter $W_L$ und 0,16 eV unter den Donatorniveaus, an einer Stelle ohne Zustände, und darüber sind Zustände besetzt, nämlich die 10¹⁶ Elektronen pro cm³ im Leitungsband.

## Der pn-Übergang

*Was geschieht, wenn ein n- und ein p-Gebiet im selben Kristall aneinandergrenzen?*

:::grafik
Szene: get1/halbleiterbauelemente/01-rlz-entstehung · Vorlage: pn-uebergang-teilchen
**Abbildung 9:** Wie die Raumladungszone entsteht, schematisch. (a) Zwei neutrale Gebiete: Jeder feste Rumpf hat seinen beweglichen Gegenpart in der Nähe. (b) Im Kontakt diffundieren Elektronen nach rechts und Löcher nach links und rekombinieren nahe der Grenze (×); zurück bleiben Rümpfe ohne Gegenpart. (c) Die freigelegten Rümpfe bilden die Raumladungszone; ihr Feld treibt die Ladungsträger zurück, bis sich Diffusion und Rücktrieb aufheben.
:::

**Die Akteure:**

- __$n_{n0}$__, __$p_{p0}$__: Majoritätsdichten im neutralen n- bzw. p-Gebiet; je 10¹⁶ cm⁻³ in der Beispieldiode (Dotierung auf beiden Seiten 10¹⁶ cm⁻³). Der Index 0 steht für das Gleichgewicht.
- __$n_{p0}$__, __$p_{n0}$__: Minoritätsdichten im p- bzw. n-Gebiet; je 10⁴ cm⁻³.
- __$\vec E$__: elektrisches Feld in der Grenzschicht; bis 3,2·10⁴ V/cm.
- __$U_\mathrm{Diff}$__: __Diffusionsspannung__, die Potenzialstufe zwischen den beiden neutralen Gebieten; 0,714 V.

**Das Zusammenspiel** ist ein Vorgang in fünf Schritten (Abbildung 9):

**Schritt 1**: Vor dem Kontakt sind beide Gebiete neutral. An der künftigen Grenze springt die Elektronendichte von 10¹⁶ auf 10⁴ cm⁻³, die Löcherdichte in Gegenrichtung ebenso.

**Schritt 2**: Jedes Teilchen bewegt sich ständig zufällig. Wo mehr Teilchen sind, bewegen sich auch mehr zur dünneren Seite als umgekehrt; so entsteht ganz ohne Kraft ein Netto-Fluss vom Dichten ins Dünne, die __Diffusion__. Elektronen diffundieren ins p-Gebiet, Löcher ins n-Gebiet, und nahe der Grenze rekombinieren sie mit den Majoritätsträgern der anderen Seite.

**Schritt 3**: Jedes Elektron, das das n-Gebiet verlässt, lässt einen P⁺-Rumpf ohne Gegenpart zurück; jedes Loch, das das p-Gebiet verlässt, einen B⁻-Rumpf. So entsteht eine Schicht positiver Ladung auf der n-Seite und eine negativer Ladung auf der p-Seite: die __Raumladungszone__. Weil sie an beweglichen Ladungsträgern verarmt ist, heißt sie auch Verarmungszone oder Sperrschicht.

**Schritt 4**: Die Ladungen erzeugen ein Feld von der n- zur p-Seite. Es treibt Elektronen zurück ins n-Gebiet und Löcher zurück ins p-Gebiet. Diese Bewegung im Feld heißt __Drift__; sie läuft der Diffusion entgegen.

**Schritt 5**: Je mehr Ladungsträger hinüberdiffundiert sind, desto mehr Rümpfe liegen frei und desto stärker treibt das Feld zurück. Das Wachstum endet, sobald für jede Sorte Drift und Diffusion gleich groß sind. Danach fließt netto nichts mehr, obwohl beide Bewegungen weiterlaufen.

:::fehlvorstellung
„Die Atomrümpfe in der Raumladungszone sind doch neutral. Wie können sie ein Feld erzeugen?“
Das liegt nahe, weil ein dotiertes Gebiet als Ganzes neutral ist. Die Rümpfe selbst sind es aber nicht: P⁺ trägt $+e$, B⁻ trägt $-e$. Neutral ist ein Gebiet nur, solange jeder Rumpf seinen beweglichen Gegenpart in der Nähe hat, und in der Raumladungszone ist dieser fortdiffundiert. 10¹⁶ freigelegte Rümpfe pro cm³ sind eine Raumladung von 1,6·10⁻³ C/cm³; das erzeugt schon über 0,2 µm ein Feld von über 3·10⁴ V/cm.
:::

:::grafik
Szene: get1/halbleiterbauelemente/01-profile-gleichgewicht · Vorlage: gestapelte-profile
**Abbildung 10:** Der pn-Übergang der Beispieldiode im Gleichgewicht, numerisch berechnet aus den Grundgleichungen für Ladung, Feld und Ladungsträgerdichten. Fünf Diagramme über demselben Ort von −0,6 bis 0,6 µm: (a) Elektronen- und Löcherdichte, halblogarithmisch; (b) Raumladung; (c) elektrisches Feld, an der Grenze 32 kV/cm; (d) Potenzial mit der Stufe von 0,714 V; (e) Bänder. Grau die 0,43 µm breite Raumladungszone, gestrichelt die Näherung mit scharf begrenzter Zone. Die ganze Potenzialstufe liegt in der verarmten Zone.
:::

Abbildung 10 zeigt den fertigen Zustand der Beispieldiode, fünf Größen über demselben Ort:

- (a) In der Mitte der Zone sind beide Dichten nur etwa 10¹⁰ cm⁻³, millionenfach weniger als die Dotierung; die Zone ist tatsächlich verarmt.
- (b) und (c) Die Raumladung bildet fast zwei Rechtecke, positiv im n- und negativ im p-Gebiet, zusammen 0,43 µm breit; das Feld wächst von beiden Rändern her an und erreicht an der Grenze 32 kV/cm.
- (d) Das Potenzial fällt S-förmig um 0,714 V; das n-Gebiet liegt höher, weil dort die positiven Rümpfe sitzen.
- (e) Das Banddiagramm zeigt die Energie der Elektronen, $-e\varphi$, also Bild (d) auf dem Kopf: Für Elektronen ist das p-Gebiet ein Plateau, 0,714 eV höher. Das Fermi-Niveau verläuft waagerecht.

Wie sich die Elektronen auf Orte verschiedener Energie verteilen, folgt aus dem Ausläufer der Fermi-Verteilung (Abschnitt *Das Fermi-Niveau*), der __Boltzmann-Verteilung__: Wo ihre Energie um $\Delta W$ höher liegt, ist ihre Dichte um den Faktor $\exp(-\Delta W/(k_B T))$ kleiner.
Wie hoch die Stufe wird, misst man deshalb in Einheiten der __Temperaturspannung__:

:::formel Definition
$$U_T = \frac{k_B T}{e}$$
:::

**So liest man das:** $U_T$ ist die thermische Energie, ausgedrückt als Spannung: die Spannung, die ein Elektron durchlaufen muss, um die Energie $k_B T$ zu gewinnen; 25,85 mV bei 300 K.
Man definiert sie, weil Potenzialstufen genau im Vergleich mit ihr wirken: Eine Stufe von $U_T$ ändert eine Dichte im Gleichgewicht um den Faktor $\exp(1)$, also 2,72, eine Stufe von 59,5 mV um den Faktor 10.
Ein häufiger Fehler ist, schon das Produkt $k_B T$ „thermische Spannung“ zu nennen; das ist eine Energie, erst geteilt durch $e$ wird daraus eine Spannung.

**Kurz gesagt:** Im thermischen Gleichgewicht und solange die Boltzmann-Verteilung gilt, addieren sich die Höhen hintereinanderliegender Potenzialstufen, und die Faktoren, um die sie eine Dichte ändern, multiplizieren sich. Zwei Stufen von je 59,5 mV, zusammen 119 mV, ändern die Dichte um den Faktor 10 mal 10, also 100.

:::analogie
**Dieselbe Physik wie in der Erdatmosphäre.** Die Luftmoleküle stehen im selben Gleichgewicht wie die Elektronen am pn-Übergang: Die Schwerkraft zieht sie nach unten, das entspricht der Drift; die Wärmebewegung verteilt sie nach oben, das entspricht der Diffusion. Die Luftdichte nimmt deshalb mit der Höhe exponentiell ab, um den Faktor 2,72 je 8,4 km; auf dem Mount Everest ist es noch ein Drittel.

| In der Atmosphäre | Am pn-Übergang |
|---|---|
| Höhe über dem Boden | Energie der Elektronen über dem n-Gebiet |
| Schwerkraft | Feld der freigelegten Rümpfe |
| Skalenhöhe 8,4 km (Faktor 2,72) | thermische Energie 25,85 meV (Faktor 2,72) |
| Luftdichte am Boden und auf dem Gipfel | Elektronendichte im n- und im p-Gebiet |

**Wo der Vergleich nicht stimmt:** Die Schwerkraft ist vorgegeben. Das Feld am pn-Übergang erzeugen die Ladungsträger selbst, indem sie abwandern und Rümpfe freilegen; deshalb stellt sich die Höhe der Stufe von selbst ein.
:::

:::formel Gesetz
$$U_\mathrm{Diff} = U_T\,\ln\frac{n_{n0}}{n_{p0}} = U_T\,\ln\frac{N_A\,N_D}{n_i^{2}}$$
:::

**So liest man das:** Eingabe sind die beiden Dotierungen und die Temperatur, Ausgabe ist die Höhe der Potenzialstufe.
Die Stufe ist genau so hoch, dass die Boltzmann-Verteilung den Dichteunterschied der Elektronen von 10¹² trägt; dafür braucht es den natürlichen Logarithmus von 10¹², also 27,6 Temperaturspannungen oder 0,714 V.
Jede Zehnerpotenz mehr Dotierung auf einer Seite erhöht die Stufe um 59,5 mV.
Steigt die Temperatur, sinkt die Stufe, weil $n_i$ schneller wächst als $U_T$.

Idee der Herleitung: Im Gleichgewicht verteilen sich die Elektronen nach der Boltzmann-Verteilung auf beide Gebiete; man vergleicht die Dichte tief im n- mit der tief im p-Gebiet.

:::herleitung
**Ausgangspunkt:** die Boltzmann-Verteilung der Wärmebewegung: Im thermischen Gleichgewicht ist die Dichte von Teilchen an einem Ort, an dem ihre Energie um $\Delta W$ höher liegt, um den Faktor $\exp(-\Delta W/(k_B T))$ kleiner.

**Annahmen:**
(i) thermisches Gleichgewicht, kein Strom;
(ii) die Elektronen beider neutralen Gebiete gehören zu demselben Gleichgewicht, denn sie tauschen sich durch die Zone hindurch ständig aus;
(iii) ein Elektron trägt die Ladung $-e$; wo das Potenzial um $\Delta\varphi$ höher ist, ist seine Energie um $e\,\Delta\varphi$ niedriger;
(iv) volle Ionisation, also $N_D$ Elektronen pro cm³ im n-Gebiet und nach dem Massenwirkungsgesetz $n_i^2/N_A$ im p-Gebiet.

**Schritt 1**: Das n-Gebiet liegt um $U_\mathrm{Diff}$ höher als das p-Gebiet; nach (iii) haben die Elektronen im p-Gebiet deshalb die höhere Energie, und zwar um

$$\Delta W = e\,(\varphi_n - \varphi_p) = e\,U_\mathrm{Diff}$$

**Schritt 2** (entscheidender Schritt): Nach der Boltzmann-Verteilung ist die Elektronendichte im p-Gebiet um den zugehörigen Faktor kleiner; mit $U_T = k_B T/e$:

$$n_{p0} = n_{n0}\,\exp\!\Big(-\frac{e\,U_\mathrm{Diff}}{k_B T}\Big) = n_{n0}\,\exp\!\Big(-\frac{U_\mathrm{Diff}}{U_T}\Big)$$

**Schritt 3**: Nach $U_\mathrm{Diff}$ auflösen, also durch $n_{n0}$ teilen, logarithmieren und mit $-U_T$ multiplizieren:

$$U_\mathrm{Diff} = U_T\,\ln\frac{n_{n0}}{n_{p0}}$$

**Schritt 4**: Die Dichten nach (iv) einsetzen:

$$U_\mathrm{Diff} = U_T\,\ln\frac{N_D}{n_i^{2}/N_A} = U_T\,\ln\frac{N_A\,N_D}{n_i^{2}}$$

**Woher die Faktoren kommen:** $U_T$ stammt aus der Boltzmann-Verteilung, der Logarithmus kehrt die Exponentialfunktion um, und $N_A N_D/n_i^2$ ist das Dichteverhältnis der Elektronen zwischen den beiden Seiten.

**Zweiter Weg:** Mit dem Fermi-Niveau. Im Gleichgewicht liegt es im ganzen Kristall gleich hoch; sonst flössen Elektronen vom höheren zum tieferen Fermi-Niveau. Schreibt man die Formel für $n$ aus dem Abschnitt *Das Fermi-Niveau* für beide Gebiete mit demselben $W_F$ an, fallen im Quotienten $N_L$ und $W_F$ heraus:

$$\frac{n_{n0}}{n_{p0}} = \exp\!\Big(\frac{W_{L,p} - W_{L,n}}{k_B T}\Big)$$

Der Abstand der Bandkanten ist $e\,U_\mathrm{Diff}$, und es folgt dieselbe Formel.

Weil das Fermi-Niveau im Gleichgewicht überall gleich hoch liegt, steigen die Bänder vom n- zum p-Gebiet desselben Kristalls um genau die Summe der beiden Strecken an, um die die Dotierung das Fermi-Niveau auf jeder Seite aus dem Eigenleitungsniveau schiebt. In der Beispieldiode sind das 0,357 eV und 0,357 eV, zusammen 0,714 eV.

**Proben:** Einheit Volt. Dieselbe Rechnung mit den Löchern führt auf dasselbe Dichteverhältnis $N_A N_D/n_i^2$, also auf dieselbe Stufe; beide Sorten verlangen dieselbe Spannung, weil das Massenwirkungsgesetz beide Dichten koppelt. Grenzfall: Ohne Dotierung sind beide Dichten $n_i$, ihr Verhältnis ist 1, und die Stufe ist null.

**Grenzen:** Ab Dotierungen von etwa 10¹⁸ cm⁻³ wird die Boltzmann-Näherung ungenau.
:::

::::beispiel Diffusionsspannung der Beispieldiode und anderer Dotierungen
**Gegeben:** Dotierungen von 10¹⁶ cm⁻³ auf beiden Seiten; Eigenleitungsdichte 10¹⁰ cm⁻³; Temperaturspannung 25,85 mV.

**Gesucht:** (a) die Diffusionsspannung; (b) wie viele Elektronen des n-Gebiets genug Energie für die Stufe haben; (c) die Stufe bei anderen Dotierungen.

**Rechnung:** (a)

$$U_\mathrm{Diff} = 25{,}85\ \mathrm{mV}\cdot\ln\frac{10^{16}\cdot10^{16}}{10^{20}} = 25{,}85\ \mathrm{mV}\cdot\ln(10^{12})$$

$$= 25{,}85\ \mathrm{mV}\cdot27{,}63 = 0{,}714\ \mathrm{V}$$

(b) Den Bruchteil mit genug Energie gibt die Boltzmann-Verteilung:

$$n_{n0}\,\exp\!\Big(-\frac{U_\mathrm{Diff}}{U_T}\Big) = 10^{16}\ \mathrm{cm^{-3}}\cdot10^{-12} = 10^{4}\ \mathrm{cm^{-3}} = n_{p0}$$

(c) Mit derselben Formel:

| Dotierung p-Seite | Dotierung n-Seite | Diffusionsspannung |
|---|---|---|
| 10¹⁵ cm⁻³ | 10¹⁵ cm⁻³ | 0,595 V |
| 10¹⁶ cm⁻³ | 10¹⁶ cm⁻³ | 0,714 V |
| 10¹⁷ cm⁻³ | 10¹⁷ cm⁻³ | 0,833 V |
| 10¹⁹ cm⁻³ | 10¹⁶ cm⁻³ | 0,893 V (Näherung, Boltzmann ungenau) |

**Ergebnis:** **0,714 V**; oben auf der Stufe gibt es genau so viele energiereiche Elektronen aus dem n-Gebiet, wie das p-Gebiet Elektronen hat.

**Einordnung:** Zehnfache Dotierung auf beiden Seiten (Zeile 3) erhöht die Stufe nur um 0,12 V, zweimal 59,5 mV; der Logarithmus macht die Diffusionsspannung unempfindlich. Bei Siliziumdioden liegt sie deshalb fast immer zwischen 0,6 und 1 V.
::::

:::frage
„Kann man die Diffusionsspannung mit einem Voltmeter messen?“
Nein. Die Messleitungen bilden an beiden Enden Kontakte zwischen Metall und Halbleiter, und an diesen Kontakten entstehen ebenfalls Potenzialstufen. Im Gleichgewicht ist die Summe aller Stufen im geschlossenen Kreis genau null; wäre sie es nicht, flösse ohne jede Energiequelle dauerhaft ein Strom. Im Bändermodell heißt dasselbe: Das Fermi-Niveau ist im ganzen Kreis waagerecht, und ein Voltmeter zeigt gerade den Unterschied der Fermi-Niveaus seiner Anschlüsse an, hier also null. Indirekt lässt sich die Diffusionsspannung trotzdem bestimmen, etwa aus der Kapazität der Raumladungszone bei verschiedenen Sperrspannungen.
:::

Ein häufiger Fehler ist, den Potenzialunterschied zwischen den Gebieten „Durchlassspannung“ zu nennen.
Das sind zwei verschiedene Größen.
Die Diffusionsspannung ist die innere Stufe im Gleichgewicht, 0,714 V bei der Beispieldiode; ein Voltmeter an den Anschlüssen zeigt sie nicht, indirekt bestimmen lässt sie sich etwa aus der Sperrschichtkapazität.
Als Durchlass- oder Schleusenspannung bezeichnet man dagegen die Spannung, ab der eine Diode in einer Schaltung merklich Strom führt, typisch 0,6 bis 0,7 V bei Silizium; ihr Wert hängt davon ab, welchen Strom man als merklich ansieht ([Folgeartikel](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)).

## Zwei Ströme im Gleichgewicht

*Wenn sich Diffusion und Drift aufheben, steht dann alles still?*

:::grafik
Szene: get1/halbleiterbauelemente/01-hinauf-hinunter · Vorlage: banddiagramm-teilchenwolke
**Abbildung 11:** Die beiden Ströme im Gleichgewicht, schematisch (thermische Energien stark vergrößert). Oben das Leitungsband mit Elektronen (Punkte), unten das Valenzband mit Löchern (Kreise), orange die Minoritätsträger. Elektronen bewegen sich im Bild von selbst nach unten, Löcher nach oben. Für jede Sorte gleicht der Diffusionsstrom der wenigen energiereichen Majoritätsträger den Driftstrom der wenigen Minoritätsträger genau aus.
:::

**Das Zusammenspiel in Schritten**, hier für die Elektronen; für die Löcher gilt alles spiegelbildlich:

**Schritt 1**: Abbildung 11 trägt die Energie der Elektronen auf; von selbst bewegt sich ein Elektron darin nach unten. Links im n-Gebiet sitzen 10¹⁶ Elektronen pro cm³ im Tal, rechts im p-Gebiet nur 10⁴ auf einem Plateau, 0,714 eV höher; dazwischen steigt die Raumladungszone an.

**Schritt 2**: Alle Elektronen bewegen sich ständig zufällig. Von beiden Seiten gelangen deshalb dauernd welche an den Rand der Zone.

**Schritt 3**: Ein Elektron aus dem n-Gebiet, das in die Zone gerät, wird vom Feld zurückgetrieben. Auf die andere Seite kommt es nur, wenn seine thermische Energie für die Stufe von 0,714 eV reicht, und nach der Boltzmann-Verteilung schafft das nur der Bruchteil 10⁻¹². Das ist der Strom __hinauf__: sehr viele Anläufe, winzige Erfolgsquote. Physikalisch ist er ein Diffusionsstrom gegen das Feld.

**Schritt 4**: Ein Elektron aus dem p-Gebiet, das zufällig an den Rand der Zone gelangt, wird vom Feld hinübergezogen, und zwar jedes einzelne. Das ist der Strom __hinunter__: wenige Anläufe, Erfolgsquote eins. Physikalisch ist er ein Driftstrom.

**Schritt 5**: Von den 10¹⁶ Elektronen links hat nur der Bruchteil 10⁻¹² genug Energie, das sind 10⁴ pro cm³, genau so viele, wie rechts auf dem Plateau sitzen. Auf der Höhe der Plateaukante gibt es links und rechts also gleich viele Elektronen, und zwischen zwei Orten gleicher Energie und gleicher Dichte wechseln in jede Richtung gleich viele. Deshalb heben sich die beiden Ströme genau auf. Wäre die Stufe niedriger, hätten links mehr Elektronen genug Energie, als rechts sitzen; netto flössen Elektronen nach rechts, legten weitere Rümpfe frei, und die Stufe wüchse, bis die Dichten wieder gleich sind. So legt das Gleichgewicht der beiden Ströme die Höhe der Barriere fest.

Beide Ströme sind klein: In der Beispieldiode wechseln pro Sekunde und Quadratzentimeter rund 10⁸ Ladungsträger vollständig die Seite, in jede Richtung gleich viele.
Für die ganze Diode mit 0,1 mm² Fläche ist jeder der beiden Ströme 1,46·10⁻¹⁴ A groß, Elektronen und Löcher zusammen.
Dieser Betrag heißt __Sättigungssperrstrom__ __$I_S$__; wie er aus der Dotierung und der mittleren Zeit bis zur Rekombination der Minoritätsträger folgt, leitet der Artikel über den [pn-Übergang unter Spannung](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/diode-pn-uebergang-spannung.html) her.

| | hinauf | hinunter |
|---|---|---|
| wer | Majoritätsträger mit genug thermischer Energie | Minoritätsträger, die an den Rand der Zone gelangen |
| wie viele Kandidaten | sehr viele, 10¹⁶ cm⁻³ | sehr wenige, 10⁴ cm⁻³ |
| Erfolgsquote | winzig, 10⁻¹² | eins |
| Art der Bewegung | Diffusion gegen das Feld | Drift im Feld |
| hängt von der Höhe der Stufe ab | exponentiell | gar nicht |

Die letzte Zeile ist der Schlüssel zur Diode.

:::frage
„Sind die Ströme hinauf und hinunter dasselbe wie die Diffusion und die Drift, die sich in der Zone aufheben?“
Nein. Hinauf und hinunter zählen nur Ladungsträger, die die Seite ganz wechseln; das sind in der Beispieldiode rund 10⁻¹¹ A/cm² in jede Richtung. Die örtlichen Diffusions- und Driftstromdichten in der Zone sind dagegen riesig, bis etwa 4·10³ A/cm² (numerisch berechnet), und heben sich fast genau auf. Die meisten Elektronen, die in die Zone hineinwandern, kehren also um, bevor sie die andere Seite erreichen.
:::

## Durchlass- und Sperrrichtung

*Was ändert eine äußere Spannung am Gleichgewicht der beiden Ströme?*

:::grafik
Szene: get1/halbleiterbauelemente/01-baender-spannung · Vorlage: banddiagramm-parameter
**Abbildung 12:** Bänder der Beispieldiode ohne Spannung (a), in Durchlassrichtung mit +0,5 V (b) und in Sperrrichtung mit −2 V (c), berechnet mit scharf begrenzter Zone; das n-Gebiet ist jeweils festgehalten. Die Spannung verändert nur die Höhe der Stufe: 0,714 eV, 0,214 eV und 2,714 eV. Der Strom hinauf steigt bei +0,5 V auf das 2,5·10⁸-Fache seines Gleichgewichtswerts und sinkt bei −2 V auf das 2,5·10⁻³⁴-Fache; der Strom hinunter bleibt gleich.
:::

**Die Akteure:**

- __$U$__: äußere Spannung an der Diode, gezählt von der p-Seite, der __Anode__, zur n-Seite, der __Kathode__ ([Zählpfeile und Vorzeichen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zaehlpfeile-und-vorzeichen.html)). Positiv heißt: Die p-Seite liegt auf höherem Potenzial, die Diode ist in __Durchlassrichtung__ gepolt; negativ heißt __Sperrrichtung__.
- __$I$__: Netto-Strom durch die Diode, gezählt von der Anode zur Kathode; in A.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Die äußere Spannung fällt fast vollständig an der Raumladungszone ab. Die neutralen Gebiete leiten gut, das n-Gebiet 680 000-mal und das p-Gebiet 240 000-mal besser als reines Silizium, und tragen den Strom deshalb schon mit einem winzigen Feld: Bei 0,6 V fallen auf je 100 µm nur 0,9 mV im n- und 2,4 mV im p-Gebiet ab (Beispiel weiter unten). Für die Stufe in der Zone bleibt fast die ganze Spannung.

**Schritt 2**: Eine Spannung in Durchlassrichtung verkleinert die Stufe auf $U_\mathrm{Diff} - U$, eine Spannung in Sperrrichtung vergrößert sie (Abbildung 12). Das ist gemeint, wenn es heißt, eine Spannung in Durchlassrichtung wirke dem elektrischen Feld in der Diode entgegen.

**Schritt 3**: Der Strom hinauf hängt nach der Boltzmann-Verteilung exponentiell von der Höhe der Stufe ab. Wird sie um $U$ niedriger, haben $\exp(U/U_T)$-mal so viele Ladungsträger genug Energie: bei 0,5 V das 2,5·10⁸-Fache, bei 0,6 V das 1,2·10¹⁰-Fache.

**Schritt 4**: Der Strom hinunter bleibt gleich. Jeder Minoritätsträger, der den Rand der Zone erreicht, fällt hinab, ganz gleich, wie hoch die Stufe ist. Wie viele dort ankommen, bestimmt allein der Nachschub durch Generation.

**Schritt 5**: Netto fließt die Differenz der beiden Ströme. In Durchlassrichtung überwiegt der Strom hinauf bei weitem, und der Netto-Strom wächst um den Faktor 10 je 59,5 mV. In Sperrrichtung verschwindet der Strom hinauf schon bei −0,1 V auf 2 % seines Gleichgewichtswerts. Übrig bleibt der Strom hinunter, 15 fA in der Beispieldiode, und weil er nicht von der Stufe abhängt, bleibt er im idealen Modell bei jeder weiteren Sperrspannung gleich.

Reale Siliziumdioden sperren schlechter als dieses ideale Modell.
In der Zone selbst entstehen durch Generation zusätzlich Paare, deren Ladungsträger das Feld sofort trennt.
Mit einer mittleren Lebensdauer der Ladungsträger bis zur Rekombination von 1 µs, wie in der Beispieldiode, sind das bei −1 V etwa 20 pA, über tausendmal mehr als $I_S$.
Weil die Zone mit der Sperrspannung breiter wird, wächst dieser Anteil langsam mit, bei −5 V auf etwa 64 pA.

:::analogie
**Der Sperrstrom wie ein Wasserfall.** Wie viel Wasser pro Sekunde einen Wasserfall hinabstürzt, bestimmt der Zufluss oben, nicht die Fallhöhe. Ebenso bestimmt den Strom hinunter der Nachschub an Minoritätsträgern, nicht die Höhe der Stufe.

| Am Wasserfall | Am pn-Übergang in Sperrrichtung |
|---|---|
| Zufluss des Flusses | Generation von Minoritätsträgern nahe der Zone |
| Kante | Rand der Raumladungszone |
| Fallhöhe | Höhe der Stufe |
| Wassermenge pro Sekunde | Sperrstrom $I_S$ |

**Wo der Vergleich nicht stimmt:** Wasser fließt gerichtet auf die Kante zu. Minoritätsträger wandern zufällig umher; ein Netto-Fluss zur Kante entsteht nur, weil jeder, der sie erreicht, hinabfällt und keiner zurückkommt.
:::

:::merke
Die äußere Spannung schiebt die Ladungsträger nicht über die Barriere. Sie verändert nur deren Höhe; über die Barriere bringt die Ladungsträger ihre eigene Wärmebewegung.
:::

:::grafik
Szene: get1/halbleiterbauelemente/01-teilstroeme · Vorlage: kennlinie-semilog
**Abbildung 13:** Teilströme und Netto-Strom der Beispieldiode über der Spannung, halblogarithmisch. Der Netto-Strom folgt in Durchlassrichtung dem Strom hinauf (Faktor 10 je 59,5 mV), in Sperrrichtung dem konstanten Strom hinunter (15 fA).
:::

In Abbildung 13 ist die Stromachse logarithmisch, damit 15 fA und 10 mA in dasselbe Bild passen; dadurch wird der exponentiell wachsende Strom hinauf zur Geraden.

:::formel Gesetz
$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$
:::

**So liest man das:** Eingabe ist die Spannung an der Diode, Ausgabe der Strom.
Der erste Summand ist der Strom hinauf, die −1 steht für den Strom hinunter.
Ab etwa 0,08 V, dem Dreifachen von $U_T$, ist die −1 vernachlässigbar; unterhalb von −0,08 V ist der Strom praktisch −$I_S$.
Diese Beziehung ist die __Shockley-Gleichung__; der [Folgeartikel](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html) untersucht sie als Kennlinie der Diode.

Idee der Herleitung: Man multipliziert den Strom hinauf mit dem Boltzmann-Faktor der abgesenkten Stufe und zieht den unveränderten Strom hinunter ab.

:::herleitung
**Ausgangspunkt:** die beiden Ströme hinauf und hinunter im Gleichgewicht, jeder vom Betrag $I_S$.

**Annahmen:**
(i) die äußere Spannung fällt ganz an der Raumladungszone ab;
(ii) die Majoritätsträger bleiben bis in die Zone hinein im thermischen Gleichgewicht mit ihrem Gebiet, ihre Energien also Boltzmann-verteilt;
(iii) der Nachschub an Minoritätsträgern durch Generation in den neutralen Gebieten hängt nicht von der Spannung ab;
(iv) schwache Injektion: Die Ladungsträger, die über die Barriere kommen, bleiben auf der anderen Seite selten gegenüber der Dotierung; in der Beispieldiode gilt das bis etwa 0,65 V;
(v) in der Zone selbst entstehen und verschwinden keine Paare.

**Schritt 1**: Mit Spannung ist die Stufe für die Elektronen

$$W_\mathrm{Stufe} = e\,(U_\mathrm{Diff} - U)$$

**Schritt 2** (entscheidender Schritt): Der Strom hinauf ist proportional zum Anteil der Majoritätsträger mit genug Energie, nach (ii) also zum Boltzmann-Faktor der Stufe; der Proportionalitätsfaktor hängt wegen (iv) nicht von $U$ ab:

$$I_\mathrm{hinauf}(U) \propto \exp\!\Big(-\frac{U_\mathrm{Diff} - U}{U_T}\Big)$$

$$= \exp\!\Big(-\frac{U_\mathrm{Diff}}{U_T}\Big)\cdot\exp\!\Big(\frac{U}{U_T}\Big)$$

Teilt man durch denselben Ausdruck bei $U = 0$, bleibt nur der zweite Faktor:

$$I_\mathrm{hinauf}(U) = I_\mathrm{hinauf}(0)\cdot\exp\!\Big(\frac{U}{U_T}\Big) = I_S\,\exp\!\Big(\frac{U}{U_T}\Big)$$

**Schritt 3**: Nach (iii) bleibt der Strom hinunter beim Gleichgewichtswert:

$$I_\mathrm{hinunter} = I_S$$

**Schritt 4**: Richtung: Hinauf wandern Elektronen von n nach p, der elektrische Strom fließt also von p nach n, von der Anode zur Kathode, und zählt positiv. Hinunter ist es umgekehrt. Netto:

$$I = I_\mathrm{hinauf} - I_\mathrm{hinunter} = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$

Für die Löcher gilt dieselbe Rechnung mit denselben Vorzeichen; beide Beiträge addieren sich, und $I_S$ ist die Summe der Anteile von Elektronen und Löchern.

**Ergebnis:**

$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$

**Woher die Faktoren kommen:** $\exp(U/U_T)$ ist der Boltzmann-Faktor der abgesenkten Stufe (Schritt 2), die −1 der unveränderte Driftstrom (Schritt 3), und $I_S$ der Betrag beider Ströme im Gleichgewicht.

**Proben:** Ohne Spannung ist der Strom null, das Gleichgewicht. Für große negative Spannungen geht er gegen $-I_S$, die Sättigung. Einheit Ampere. Zahlenwert bei 0,6 V: 1,46·10⁻¹⁴ A mal 1,2·10¹⁰ ergibt 0,18 mA (ideales Modell).

**Grenzen:** Oberhalb von etwa 0,65 V erreichen die übergetretenen Minoritätsträger am Rand der Zone 8 % der Dotierung, bei 0,7 V schon 57 %; Annahme (iv) bricht zusammen (starke Injektion). Zugleich fällt ein wachsender Teil der Spannung an den neutralen Gebieten ab, und Annahme (i) gilt nicht mehr (Bahnwiderstand). In Sperrrichtung setzt bei hohen Feldern der Durchbruch ein. Annahme (v) gilt in realen Siliziumdioden meist nicht: Bei Raumtemperatur bestimmt die Generation in der Zone den Sperrstrom (mit 1 µs Lebensdauer etwa 20 pA bei −1 V statt 15 fA), und bei kleinen Durchlassspannungen kommt Rekombination in der Zone hinzu. Diese Abweichungen behandelt der Folgeartikel.
:::

::::beispiel Ströme der Beispieldiode und Spitzenspannung im Einweggleichrichter
**Gegeben:**
- Sättigungssperrstrom der Beispieldiode 1,457·10⁻¹⁴ A;
- Temperaturspannung 25,85 mV;
- Einweggleichrichter aus Abbildung 2 mit Scheitelwert 10 V und Widerstand 1 kΩ.

**Gesucht:** (a) die Ströme bei 0,4 V, 0,6 V, 0,7 V und −1 V; (b) der Faktor, um den der Strom bei 0,12 V mehr Spannung wächst; (c) die Spitzenspannung am Widerstand.

**Rechnung:** (a) Mit der Shockley-Gleichung:

$$I(0{,}4\ \mathrm{V}) = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot\big[\exp(15{,}47) - 1\big]$$

$$= 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot5{,}245\cdot10^{6} = 76\ \mathrm{nA}$$

$$I(0{,}6\ \mathrm{V}) = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot1{,}201\cdot10^{10} = 0{,}175\ \mathrm{mA}, \qquad I(0{,}7\ \mathrm{V}) = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot5{,}748\cdot10^{11} = 8{,}4\ \mathrm{mA}$$

$$I(-1\ \mathrm{V}) = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot\big[\exp(-38{,}7) - 1\big]$$

$$= -1{,}457\cdot10^{-14}\ \mathrm{A} \approx -15\ \mathrm{fA}$$

(b) Der Faktor ist

$$\exp\!\Big(\frac{0{,}12\ \mathrm{V}}{25{,}85\ \mathrm{mV}}\Big) = \exp(4{,}64) = 104$$

(c) An der Spitze teilen sich Diode und Widerstand die 10 V. Nach $U$ aufgelöst lautet die Shockley-Gleichung

$$U = U_T\,\ln\Big(\frac{I}{I_S} + 1\Big)$$

Startwert 0,7 V an der Diode, also 9,3 V am Widerstand und 9,3 mA:

$$U = 25{,}85\ \mathrm{mV}\cdot\ln\Big(\frac{9{,}3\cdot10^{-3}\ \mathrm{A}}{1{,}457\cdot10^{-14}\ \mathrm{A}}\Big) = 25{,}85\ \mathrm{mV}\cdot27{,}18 = 0{,}703\ \mathrm{V}$$

Ein zweiter Durchgang mit 9,297 mA ändert das Ergebnis nicht mehr.

**Ergebnis:** **Im idealen Modell 76 nA, 0,175 mA, 8,4 mA und −15 fA; Faktor 104 je 0,12 V; Spitze rund 9,3 V am Widerstand.**

**Einordnung:** Zwischen 0,4 und 0,7 V wächst der Strom um mehr als das Hunderttausendfache. Im Gleichrichter verliert man deshalb rund 0,7 V, fast unabhängig vom Strom: Doppelter Strom kostet im idealen Modell nur 18 mV mehr. Mit 0,70 V liegt die Diode allerdings schon jenseits der Gültigkeitsgrenze von etwa 0,65 V; eine reale Diode verliert bei 9 mA etwas mehr, weil zusätzlich Spannung an den neutralen Gebieten abfällt.
::::

:::fehlvorstellung
„Unter 0,7 V fließt kein Strom durch die Diode.“
Das liegt nahe, weil eine Siliziumdiode in Schaltungen erst ab etwa 0,6 V merklich leitet und weil es oft heißt, ein Strom fließe, sobald die Spannung die Durchlassspannung überschreitet. Tatsächlich fließt bei jeder positiven Spannung Strom, nur wenig: im idealen Modell 76 nA bei 0,4 V und 3,7 µA bei 0,5 V; reale Dioden führen dort durch Rekombination in der Zone eher noch mehr. Die scheinbare Schwelle entsteht durch den steilen Anstieg; auf einer linearen Achse in Milliampere wird der Strom erst ab etwa 0,6 V sichtbar.
:::

::::beispiel Wie viel Spannung in den neutralen Gebieten abfällt
**Gegeben:**
- Beispieldiode bei 0,6 V, Strom 0,175 mA, Fläche 0,1 mm²;
- Leitfähigkeit des n-Gebiets 2,00 S/cm, des p-Gebiets 0,72 S/cm (10¹⁶ cm⁻³ mal Löcherbeweglichkeit 450 cm²/(V s) mal $e$).

**Gesucht:** das Feld in beiden neutralen Gebieten und die Spannung über je 100 µm.

**Rechnung:** Stromdichte:

$$J = \frac{I}{A} = \frac{0{,}175\cdot10^{-3}\ \mathrm{A}}{10^{-3}\ \mathrm{cm^2}} = 0{,}175\ \mathrm{A/cm^2}$$

Feld nach dem ohmschen Gesetz in der Form $J = \sigma E$:

$$E = \frac{J}{\sigma} = \frac{0{,}175\ \mathrm{A/cm^2}}{2{,}00\ \mathrm{S/cm}} = 0{,}087\ \mathrm{V/cm}$$

Spannung über 100 µm:

$$\Delta U = E\cdot l = 0{,}087\ \mathrm{V/cm}\cdot0{,}01\ \mathrm{cm} = 0{,}87\ \mathrm{mV}$$

Im p-Gebiet entsprechend:

$$E_p = \frac{0{,}175\ \mathrm{A/cm^2}}{0{,}72\ \mathrm{S/cm}} = 0{,}24\ \mathrm{V/cm}, \qquad \Delta U_p = 0{,}24\ \mathrm{V/cm}\cdot0{,}01\ \mathrm{cm} = 2{,}4\ \mathrm{mV}$$

**Ergebnis:** **Zusammen fallen auf je 100 µm neutralem Gebiet nur 3,3 mV der 0,6 V ab.**

**Einordnung:** Annahme (i) der Herleitung ist damit gerechtfertigt: Fast die ganze Spannung liegt an der Raumladungszone. In der Zone selbst herrschen dagegen Felder von über 10⁴ V/cm.
::::

:::fehlvorstellung
„In Durchlassrichtung stößt der Pluspol die Löcher über die Barriere.“
Das liegt nahe, weil in einem Widerstand tatsächlich die Quelle die Ladungsträger durch ihr Feld treibt. Am pn-Übergang verkleinert sie dagegen die Stufe, bei 0,6 V von 0,714 auf 0,114 V, und über den Rest kommen die Ladungsträger durch ihre eigene Wärmebewegung. Das Feld der Quelle im neutralen p-Gebiet, aus dem die Löcher kommen, beträgt bei 0,6 V nur 0,24 V/cm; über 100 µm sind das 2,4 mV, verglichen mit der verbliebenen Stufe von 114 mV. Es lässt nur Majoritätsträger aus dem Kontakt nachfließen.
:::

Den Sperrstrom nennt man üblicherweise einen Diffusionsstrom: Seine Größe bestimmt die Diffusion der Minoritätsträger in den neutralen Gebieten zum Rand der Zone; über die Zone selbst gelangen sie durch Drift, als Strom hinunter.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Reines Silizium leitet kaum | Die Bandlücke ist 43-mal größer als die thermische Energie; es gibt nur wenige bewegliche Ladungsträger. |
| Löcher als zweite Sorte | Jedes Elektron im Leitungsband hinterlässt einen beweglichen freien Platz im Valenzband. |
| Dotierung | Fremdatome übertreffen die wenigen Eigenleitungsträger um Zehnerpotenzen und legen Art und Zahl der Ladungsträger fest. |
| Minoritätsträger | Das Massenwirkungsgesetz koppelt beide Sorten: Viele der einen bedeuten wenige der anderen. |
| Raumladungszone und Diffusionsspannung | Der Dichteunterschied treibt Diffusion; die freigelegten Rümpfe bauen die Barriere auf, bis Drift und Diffusion gleich sind. |
| Zwei Ströme im Gleichgewicht | Viele Ladungsträger mit winziger Erfolgsquote gleichen wenige Ladungsträger mit voller Erfolgsquote aus. |
| Durchlass und Sperr | Die Spannung verschiebt nur die Barriere, und nur einer der beiden Ströme reagiert darauf. |
| Temperaturempfindlichkeit | Die Zahl der Eigenleitungsträger hängt exponentiell von der Temperatur ab. |

Ein Halbleiter hat wenige bewegliche Ladungsträger, deren Art und Zahl die Dotierung festlegt; wo ein n- und ein p-Gebiet aneinandergrenzen, baut der Dichteunterschied von selbst eine Barriere auf, deren Höhe eine äußere Spannung verschiebt.

## Bedeutung und Ausblick

Jede Siliziumdiode beruht auf diesem Mechanismus, vom Gleichrichter in einem Ladegerät bis zur Schutzdiode an einem Mikrocontroller-Eingang.
Fotodioden und Solarzellen nutzen die Paarbildung durch Licht bis 1,1 µm Wellenlänge, und ein [Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) besteht aus zwei pn-Übergängen dicht hintereinander; einer davon ist die Basis-Emitter-Strecke eines Transistors wie des BC547C.
Das Modell dieses Artikels hat Grenzen: Oberhalb von etwa 0,65 V werden die übergetretenen Ladungsträger so zahlreich, dass seine Annahmen nicht mehr gelten, und der Widerstand der neutralen Gebiete macht sich bemerkbar; in Sperrrichtung setzt bei hohen Feldern der Durchbruch ein, und mit der Temperatur ändern sich $I_S$ und die Durchlassspannung erheblich.
Diese Effekte und die Kennlinie als Ganzes behandelt der nächste Artikel, [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html).

:::kern
- Leiten können nur Elektronen in teilweise besetzten Bändern. Im Halbleiter trennt eine Lücke $W_g$ von 1,12 eV das volle Valenzband vom leeren Leitungsband.
- Die Wärme hebt in reinem Silizium nur 10¹⁰ Elektronen pro cm³ über die Lücke; jedes hinterlässt ein Loch, das sich wie eine Ladung $+e$ bewegt.
- Im thermischen Gleichgewicht gilt immer: $n\,p = n_i^2$.
- Dotierung legt die Majoritätsträger fest ($n \approx N_D$ bzw. $p \approx N_A$); die Minoritätsträger sind um viele Zehnerpotenzen seltener.
- Das Fermi-Niveau ist der 50-%-Punkt der Besetzung; Dotierung schiebt es aus der Bandmitte zum jeweiligen Band.
- Am pn-Übergang entsteht von selbst eine Barriere: $U_\mathrm{Diff} = U_T \ln(N_A N_D/n_i^2)$, in der Beispieldiode 0,714 V.
- Im Gleichgewicht fließen zwei gleich große Ströme gegeneinander. Die äußere Spannung ändert nur die Barriere: $I = I_S\,[\exp(U/U_T) - 1]$.
- Durchlassrichtung: Faktor 10 je 59,5 mV. Sperrrichtung: im idealen Modell nur $I_S$, unabhängig von der Spannung.
:::

:::quiz
F: Warum leitet ein vollständig besetztes Band keinen Strom, obwohl es sehr viele Elektronen enthält?
A: Weil es keinen freien Zustand gibt, in den ein Elektron wechseln könnte. Zu jedem Elektron mit einer Geschwindigkeit gibt es eines mit der entgegengesetzten; ein Feld kann diese Verteilung nicht verschieben, die Summe bleibt null.
F: Warum gibt es in reinem Silizium bei 300 K nur etwa 10¹⁰ freie Elektronen pro cm³?
A: Die Bandlücke von 1,12 eV ist 43-mal größer als die thermische Energie von 25,85 meV. Die Wahrscheinlichkeit, so viel Energie an einer Stelle zu sammeln, fällt exponentiell: n_i ist die mittlere effektive Zustandsdichte von 2,4·10¹⁹ cm⁻³ mal dem Faktor exp(−W_g/(2k_BT)), der bei Silizium nur 3,9·10⁻¹⁰ beträgt.
F: Stimmt es, dass n-dotiertes Silizium negativ geladen ist?
A: Nein. Jedes freie Elektron stammt von einem Donator, der dabei zum positiven Rumpf P⁺ wurde; Elektronen und Rümpfe gleichen sich genau aus. Das „n“ bezeichnet nur die Majoritätsträger.
F: Wie viele Löcher hat n-Silizium mit 10¹⁶ Donatoren pro cm³, und warum so wenige?
A: 10⁴ pro cm³, nach dem Massenwirkungsgesetz (10²⁰ cm⁻⁶ geteilt durch 10¹⁶ cm⁻³). Bei so vielen Elektronen trifft jedes Loch schnell auf einen Partner und rekombiniert; die Generation liefert nur sehr wenig Nachschub.
F: Stimmt es, dass die Atomrümpfe in der Raumladungszone neutral sind?
A: Nein. P⁺ trägt +e, B⁻ trägt −e. Neutral ist ein Gebiet nur, wenn jeder Rumpf seinen beweglichen Gegenpart in der Nähe hat; in der Zone ist dieser fortdiffundiert, und die Rümpfe erzeugen das Feld von über 3·10⁴ V/cm.
F: Warum wird die Barriere der Beispieldiode genau 0,714 V hoch?
A: Weil dann von den 10¹⁶ Elektronen des n-Gebiets genau der Bruchteil 10⁻¹² genug Energie hat, also 10⁴ pro cm³, so viele, wie das p-Gebiet hat. Erst dann sind die Ströme hinauf und hinunter gleich; wäre die Stufe niedriger, flössen netto Elektronen hinüber und die Stufe wüchse weiter.
F: Stimmt es, dass unter 0,7 V kein Strom durch eine Siliziumdiode fließt?
A: Nein. Bei jeder positiven Spannung fließt Strom, bei der Beispieldiode im idealen Modell 76 nA bei 0,4 V. Er wächst nur so steil, um den Faktor 10 je 59,5 mV, dass er auf einer linearen Achse erst ab etwa 0,6 V sichtbar wird.
F: Warum hängt der Sperrstrom im idealen Modell nicht von der Sperrspannung ab?
A: Er ist der Strom hinunter: Jeder Minoritätsträger, der den Rand der Zone erreicht, wird hinübergezogen, ganz gleich, wie hoch die Stufe ist. Wie viele ankommen, bestimmt nur die Generation. Der Strom hinauf ist schon bei −0,1 V auf 2 % gefallen. Reale Dioden haben zusätzlich einen Generationsstrom aus der Zone selbst, der mit der Sperrspannung langsam wächst.
F: Um welchen Faktor steigt der Durchlassstrom, wenn die Spannung um 0,12 V steigt?
A: Um exp(0,12 V/25,85 mV) = exp(4,64), also etwa das Hundertfache (genau 104): je 59,5 mV eine Zehnerpotenz.
F: Warum kann man die Diffusionsspannung nicht mit einem Voltmeter messen?
A: An den Kontakten der Messleitungen entstehen ebenfalls Potenzialstufen, und im Gleichgewicht ist ihre Summe im geschlossenen Kreis null; sonst flösse ohne Energiequelle dauerhaft Strom. Das Fermi-Niveau ist überall gleich hoch, und das Voltmeter zeigt null.
:::
