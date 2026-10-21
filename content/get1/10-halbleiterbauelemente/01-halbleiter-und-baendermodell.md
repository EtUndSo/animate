---
title: Halbleiter und das Bändermodell
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100100
summary: Warum reines Silizium kaum leitet, wie Dotierung Art und Zahl der Ladungsträger festlegt und warum ein pn-Übergang Strom nur in eine Richtung durchlässt. Kompakte Fassung; die ausführliche enthält zusätzlich Fermi-Statistik, Temperaturgang und weitere Hintergründe.
tags: Halbleiter, Bändermodell, Bandlücke, Eigenleitung, Loch, Fermi-Niveau, Dotierung, pn-Übergang, Raumladungszone, Diffusionsspannung
stil: 3
fassung: kompakt
---

## Worum es geht

Eine Diode lässt Strom nur in eine Richtung durch; damit macht man zum Beispiel aus der Wechselspannung der Steckdose die Gleichspannung, die ein Akku zum Laden braucht.
Gebaut wird sie aus einem Halbleiter wie Silizium, dessen Leitfähigkeit sich gezielt einstellen lässt.
Alles in diesem Artikel hängt an einem Prinzip: **Ein Halbleiter hat wenige bewegliche Ladungsträger, deren Art und Zahl die Dotierung festlegt; wo ein n- und ein p-Gebiet aneinandergrenzen, baut der Dichteunterschied von selbst eine Barriere auf, deren Höhe eine äußere Spannung verschiebt.**
Vorausgesetzt werden der [elektrische Strom](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/elektrischer-strom.html), [Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html) und das [elektrische Feld](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/elektrisches-feld-und-feldstaerke.html); darauf bauen [die Kennlinie der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html) und der [Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) auf.

:::grafik
Szene: get1/halbleiterbauelemente/01-gesamtbild · Vorlage: banddiagramm-vergleich
**Abbildung 1:** Der Weg dieses Artikels im Bändermodell, berechnet für Silizium bei 300 K: (a) reines Silizium mit wenigen Elektronen und Löchern, (b), (c) dotiertes Silizium, (d) n- und p-Gebiet im Kontakt. An der Stufe von 0,714 eV in (d) entscheidet sich, ob Strom fließt. Teilchenzahlen schematisch.
:::

## Bänder: warum Silizium kaum leitet

*Warum leitet Kupfer gut, Silizium kaum und Glas praktisch gar nicht, obwohl alle drei Elektronen im Überfluss enthalten?*

:::grafik
Szene: get1/halbleiterbauelemente/01-leiter-halbleiter-isolator · Vorlage: baender-vergleich
**Abbildung 2:** Metall, Halbleiter (Silizium, Lücke 1,12 eV) und Isolator (Siliziumdioxid, Lücke etwa 9 eV) im Bändermodell, Energie in eV (bei Halbleiter und Isolator mit der Valenzbandkante bei null); grau sind besetzte Zustände. Leiten kann nur ein teilweise besetztes Band.
:::

**Die Akteure:**

- __$W$__: Energie eines Elektrons, in Elektronenvolt; 1 eV gewinnt ein Elektron beim Durchlaufen von 1 V.
- __$k_B T$__: thermische Energie, die typische Energie der Wärmebewegung pro Teilchen; 25,85 meV bei 300 K ($k_B$ ist die Boltzmann-Konstante).

**Das Zusammenspiel:** Ein einzelnes Atom erlaubt seinen Elektronen nur bestimmte Energien, die Energieniveaus.
Im Kristall koppeln die Zustände benachbarter Atome, und jedes Niveau spaltet in so viele dicht benachbarte Niveaus auf, wie Atome beteiligt sind.
Bei 5·10²² Atomen pro cm³ entsteht so ein praktisch lückenloses __Energieband__; zwischen den Bändern bleiben __verbotene Zonen__ ohne jeden Zustand.
Zwei Bänder entscheiden über die Leitfähigkeit.
Das __Valenzband__ hat genau vier Plätze pro Siliziumatom, so viele, wie jedes Atom äußere Elektronen hat (__Valenzelektronen__); am absoluten Nullpunkt ist es deshalb voll. Seine Oberkante heißt __$W_V$__.
Das __Leitungsband__ darüber ist dann leer; seine Unterkante heißt __$W_L$__.

:::formel Definition
$$W_g = W_L - W_V$$
:::

**So liest man das:** Die __Bandlücke__ ist die kleinste Energie, die ein Elektron braucht, um vom vollen ins leere Band zu gelangen; deshalb definiert man sie so.
Bei Silizium beträgt sie 1,12 eV, das 43-Fache der thermischen Energie; bei Siliziumdioxid etwa 9 eV.

Strom tragen kann nur ein **teilweise besetztes Band**, denn ein Elektron muss dazu in einen freien Zustand mit etwas mehr Geschwindigkeit in Richtung der Kraft wechseln können, die das Feld auf es ausübt.

:::frage
„Warum leitet ein volles Band nicht, die Elektronen sind doch da?“
Weil kein Elektron seinen Zustand wechseln kann: Alle Zustände sind besetzt. Zu jedem Elektron, das sich mit einer bestimmten Geschwindigkeit bewegt, gibt es eines, das sich genau entgegengesetzt bewegt; die Summe ist null. Ein Feld müsste diese Verteilung verschieben, und dafür fehlen freie Plätze. Ein leeres Band trägt ebenso wenig Strom, weil es keine Elektronen enthält.
:::

Damit unterscheiden sich die drei Stoffklassen in Abbildung 2.
In Kupfer ist das oberste besetzte Band etwa halb voll, und alle 8,5·10²² Valenzelektronen pro cm³ sind beweglich.
In Silizium hebt die Wärmebewegung nur wenige Elektronen über die Lücke; danach sind beide Bänder ein wenig teilweise besetzt, und beide leiten schwach.
In Siliziumdioxid ist die Lücke so groß, dass praktisch kein Elektron hinübergelangt.
Das Skript zählt die Halbleiter zu den Isolatoren mit kleiner Lücke (S. 160); im Bänderbild ist das die übliche Einteilung, bei Raumtemperatur leitet reines Silizium aber um viele Zehnerpotenzen besser als Glas.

## Elektronen und Löcher

*Woher kommen in reinem Silizium bewegliche Ladungsträger, und wie viele sind es?*

:::grafik
Szene: get1/halbleiterbauelemente/01-kristallgitter · Vorlage: kristallgitter-2d
**Abbildung 3:** Siliziumgitter als ebenes Schema; jede Doppellinie ist eine Bindung aus zwei Elektronen. (a) Die Wärme hat eine Bindung aufgebrochen: freies Elektron (blau) und Lücke (rot). (b) Phosphor gibt sein fünftes Elektron ab und bleibt als P⁺ zurück. (c) Bor hat ein Elektron aufgenommen (B⁻); die Lücke sitzt eine Bindung weiter. Schematisch.
:::

**Die Akteure:**

- __$n$__, __$p$__: Dichte der freien Elektronen bzw. der Löcher (Lücken im Valenzband); in cm⁻³.
- __$n_i$__: __Eigenleitungsdichte__, die Dichte jeder der beiden Sorten in reinem Silizium; 10¹⁰ cm⁻³ bei 300 K.

**Das Zusammenspiel:** Jedes Siliziumatom ist über vier Bindungen aus je zwei Elektronen mit seinen Nachbarn verbunden (Abbildung 3 a).
Selten sammelt die Wärmebewegung genug Energie an einer Stelle, und ein Elektron verlässt seine Bindung: Es springt vom Valenz- ins Leitungsband und ist frei beweglich (__Generation__).
Zurück bleibt eine Bindung mit nur einem Elektron.
In diese Lücke springt mit sehr wenig Energie ein Elektron aus einer Nachbarbindung und hinterlässt dort eine neue Lücke; so wandert die Lücke durch den Kristall.
In einem Feld springen die gebundenen Elektronen bevorzugt gegen die Feldrichtung, die Lücke wandert dadurch mit dem Feld.
In ihrer Umgebung fehlt die Ladung eines Elektrons; sie verhält sich wie ein Teilchen mit der Ladung $+e$ und heißt __Loch__.

Fällt ein freies Elektron in ein Loch zurück, verschwinden beide (__Rekombination__).
Die Dichten wachsen, bis Generation und Rekombination gleich häufig sind; in reinem Silizium bei 300 K ist das bei je 10¹⁰ Elektronen und Löchern pro cm³ erreicht.
Auf 5·10¹² Siliziumatome kommt also ein freies Elektron; deshalb leitet reines Silizium kaum.
Weil die Bandlücke so groß gegen die thermische Energie ist, hängt diese Zahl stark von der Temperatur ab: Bei Raumtemperatur wächst sie um 8,3 % pro Kelvin.

:::frage
„Ist ein Loch ein echtes Teilchen?“
Nein. Ein Loch ist ein fehlendes Elektron in einer sonst vollständigen Bindungsstruktur, und seine Bewegung ist die gemeinsame Bewegung vieler gebundener Elektronen. Alle Gleichungen funktionieren aber genau so, als wäre es ein Teilchen mit der Ladung $+e$. Seine Beweglichkeit, die mittlere Geschwindigkeit pro Feldstärke, ist mit 450 cm²/(V s) kleiner als die der freien Elektronen (1250 cm²/(V s)), weil sich Löcher im Kristall so bewegen, als wären sie schwerer.
:::

Rekombination braucht ein Elektron und ein Loch am selben Ort und wird deshalb umso häufiger, je mehr von beiden da sind.
Daraus folgt eine Regel, die für jedes Silizium gilt, auch für dotiertes:

:::formel Gesetz
$$n\,p = n_i^{2}$$
:::

**So liest man das:** Das Produkt der beiden Dichten ist im thermischen Gleichgewicht eine Materialkonstante, die nur von der Temperatur abhängt (__Massenwirkungsgesetz__).
Wird eine Sorte häufiger, wird die andere im selben Verhältnis seltener.

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

**Proben:** Einheit cm⁻⁶ auf beiden Seiten. Reines Silizium: 10¹⁰ mal 10¹⁰ ergibt 10²⁰ cm⁻⁶.

**Grenzen:** Gilt nur im Gleichgewicht und ohne Entartung, also bei Dotierungen unter etwa 10¹⁸ cm⁻³. Unter Licht oder wenn eine äußere Spannung Ladungsträger zuführt oder absaugt, weicht $n\,p$ von $n_i^2$ ab.
:::

:::frage
„Warum rekombinieren nicht einfach alle Elektronen mit allen Löchern?“
Sie rekombinieren ständig, aber die Wärmebewegung erzeugt im selben Takt neue Paare. Gleichgewicht herrscht, wenn beides gleich häufig geschieht, und genau das legt das Massenwirkungsgesetz fest. Ein einzelnes freies Elektron lebt in Silizium typischerweise Mikrosekunden bis Millisekunden, je nach Reinheit des Kristalls; in derselben Zeit entstehen anderswo neue.
:::

## Dotierung

*Wie macht man aus Silizium einen guten Leiter für genau eine Sorte von Ladungsträgern?*

**Die Akteure:**

- __$N_D$__: Dichte der __Donatoren__, Fremdatome mit fünf Valenzelektronen wie Phosphor; in der Beispieldiode dieses Artikels 10¹⁶ cm⁻³, ein Fremdatom auf fünf Millionen Siliziumatome.
- __$N_A$__: Dichte der __Akzeptoren__, Fremdatome mit drei Valenzelektronen wie Bor; ebenfalls 10¹⁶ cm⁻³.

**Das Zusammenspiel:** Ein Phosphoratom im Gitter (Abbildung 3 b) bindet vier seiner fünf Valenzelektronen; das fünfte hält es nur mit 45 meV, weniger als das Doppelte der thermischen Energie.
Zudem bietet das Leitungsband bei 10¹⁶ cm⁻³ rund 3200-mal mehr Plätze, als es Donatoren gibt; bei 300 K ist dieses Elektron deshalb bei über 99,6 % der Phosphoratome frei, und zurück bleibt ein fest eingebauter Rumpf P⁺.
Silizium mit Donatoren heißt __n-dotiert__.
Dem Bor (Abbildung 3 c) fehlt ein Elektron für die vierte Bindung; ein Elektron aus einer Nachbarbindung füllt den Platz, das Bor wird zum festen Rumpf B⁻, und das Loch wandert davon.
Silizium mit Akzeptoren heißt __p-dotiert__.
Ein dotiertes Gebiet bleibt dabei elektrisch neutral: Zu jedem freien Elektron gibt es einen P⁺-Rumpf, und über Abstände von einigen 10 nm gleichen sich ihre Ladungen aus. Das „n“ bezeichnet nur die Sorte der beweglichen Ladungsträger.

:::formel Formel
$$n \approx N_D, \qquad p \approx \frac{n_i^{2}}{N_D} \qquad \text{(n-Silizium)}$$
:::

**So liest man das:** Jeder Donator liefert ein Elektron, und die Löcher folgen aus dem Massenwirkungsgesetz.
Die zahlreiche Sorte heißt __Majoritätsträger__, die seltene __Minoritätsträger__; bei 10¹⁶ cm⁻³ stehen sie im Verhältnis 10¹² zu 1.
Im p-Silizium sind die Rollen vertauscht.

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
- Dotierung 10¹⁶ cm⁻³, Eigenleitungsdichte 10¹⁰ cm⁻³;
- Beweglichkeit der Elektronen bei dieser Dotierung 1250 cm²/(V s); in reinem Silizium 1400 (Elektronen) und 450 cm²/(V s) (Löcher); gerundete Werte des Beispielsystems.

**Gesucht:** $n$ und $p$ und die Leitfähigkeit im Vergleich mit reinem Silizium.

**Rechnung:** Dichten nach der Formel:

$$n = 10^{16}\ \mathrm{cm^{-3}}, \qquad p = \frac{(10^{10}\ \mathrm{cm^{-3}})^{2}}{10^{16}\ \mathrm{cm^{-3}}} = 10^{4}\ \mathrm{cm^{-3}}$$

Nach dem Artikel über den [ohmschen Widerstand](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/ohmscher-widerstand.html) trägt jede Ladungsträgersorte Ladung mal Dichte mal Beweglichkeit zur Leitfähigkeit bei; die Löcher fallen hier weg:

$$\sigma = e\,n\,\mu_n = 1{,}602\cdot10^{-19}\ \mathrm{C}\cdot10^{16}\ \mathrm{cm^{-3}}\cdot1250\ \mathrm{\tfrac{cm^2}{V\,s}} = 2{,}00\ \mathrm{S/cm}$$

$$\sigma_i = 1{,}602\cdot10^{-19}\ \mathrm{C}\cdot10^{10}\ \mathrm{cm^{-3}}\cdot(1400 + 450)\ \mathrm{\tfrac{cm^2}{V\,s}} = 2{,}96\cdot10^{-6}\ \mathrm{S/cm}$$

**Ergebnis:** **10¹⁶ Elektronen und 10⁴ Löcher pro cm³; spezifischer Widerstand 0,50 Ωcm statt 3,4·10⁵ Ωcm.**

**Einordnung:** Ein Phosphoratom auf fünf Millionen Siliziumatome steigert die Leitfähigkeit auf das 680 000-Fache. Kupfer (1,68·10⁻⁶ Ωcm) leitet trotzdem noch 300 000-mal besser, denn dort ist jedes Atom an der Leitung beteiligt.
::::

Das Skript zeichnet die Bänder zusätzlich mit dem __Fermi-Niveau__ $W_F$ (Bilder 10.4 und 10.5).
Es ist die Energie, bei der ein Zustand mit der Wahrscheinlichkeit 1/2 besetzt wäre; je näher es an einem Band liegt, desto mehr Ladungsträger hat dieses Band.
In reinem Silizium ergibt es sich fast genau in der Mitte der Lücke, weil Elektronen und Löcher gleich häufig sind; als Definition, wie im Skript (S. 160), taugt diese Lage nicht.
Dotierung schiebt es zum Band der Majoritätsträger, bei 10¹⁶ cm⁻³ bis auf 0,21 eV an $W_L$ bzw. 0,19 eV an $W_V$ heran (Abbildung 1 b, c).
Es liegt dann 0,16 eV unter dem Niveau des locker gebundenen fünften Elektrons, an einer Stelle ohne Zustände, und darüber sind Zustände besetzt, die 10¹⁶ Leitungselektronen pro cm³. Anders als das Skript schreibt (S. 161), ist es bei 300 K also nicht der „höchste besetzte Zustand“.
Zwei weitere Kleinigkeiten auf derselben Seite: Die Bindungen heißen kovalent, nicht „kohärent“, und in der Festkörperphysik ist Silizium ein Halbleiter, kein Halbmetall.

## Der pn-Übergang

*Was geschieht, wenn ein n- und ein p-Gebiet im selben Kristall aneinandergrenzen?*

:::grafik
Szene: get1/halbleiterbauelemente/01-rlz-entstehung · Vorlage: pn-uebergang-teilchen
**Abbildung 4:** Wie die Raumladungszone entsteht, schematisch. (a) Zwei neutrale Gebiete. (b) Elektronen und Löcher diffundieren hinüber und rekombinieren (×). (c) Zurück bleiben feste Rümpfe ohne Gegenpart; ihr Feld treibt die Ladungsträger zurück.
:::

**Die Akteure:**

- __$n_{n0}$__, __$n_{p0}$__: Elektronendichte im neutralen n- bzw. p-Gebiet; 10¹⁶ bzw. 10⁴ cm⁻³ in der Beispieldiode, die auf beiden Seiten mit 10¹⁶ cm⁻³ dotiert ist. Der Index 0 steht für das Gleichgewicht.
- __$U_\mathrm{Diff}$__: __Diffusionsspannung__, die Potenzialstufe zwischen den beiden neutralen Gebieten; 0,714 V.

**Das Zusammenspiel in Schritten** (Abbildung 4):

**Schritt 1**: An der Grenze springt die Elektronendichte von 10¹⁶ auf 10⁴ cm⁻³, die Löcherdichte in Gegenrichtung ebenso.

**Schritt 2**: Alle Ladungsträger bewegen sich ständig zufällig. Deshalb wandern mehr vom dichten ins dünne Gebiet als umgekehrt, ganz ohne Kraft (__Diffusion__): Elektronen ins p-Gebiet, Löcher ins n-Gebiet, wo sie mit den Majoritätsträgern rekombinieren.

**Schritt 3**: Zurück bleiben feste Rümpfe ohne beweglichen Gegenpart, P⁺ auf der n-Seite, B⁻ auf der p-Seite. Diese geladene, an Ladungsträgern verarmte Schicht heißt __Raumladungszone__; in der Beispieldiode ist sie 0,43 µm breit.

**Schritt 4**: Die Rümpfe erzeugen ein Feld von der n- zur p-Seite, bis 3,2·10⁴ V/cm stark, das Elektronen und Löcher zurücktreibt. Diese Bewegung im Feld heißt __Drift__.

**Schritt 5**: Je mehr Ladungsträger hinüberdiffundiert sind, desto stärker treibt das Feld zurück. Der Vorgang endet, wenn Drift und Diffusion für jede Sorte gleich groß sind.

:::fehlvorstellung
„Die Atomrümpfe in der Raumladungszone sind doch neutral. Wie können sie ein Feld erzeugen?“
Das liegt nahe, weil ein dotiertes Gebiet als Ganzes neutral ist. Die Rümpfe selbst sind es nicht: P⁺ trägt $+e$, B⁻ trägt $-e$. Neutral ist ein Gebiet nur, solange jeder Rumpf seinen beweglichen Gegenpart in der Nähe hat, und in der Raumladungszone ist dieser fortdiffundiert. 10¹⁶ freigelegte Rümpfe pro cm³ erzeugen schon über 0,2 µm ein Feld von über 3·10⁴ V/cm.
:::

Wie sich Teilchen im Gleichgewicht auf Orte verschiedener Energie verteilen, beschreibt die __Boltzmann-Verteilung__: Wo ihre Energie um $\Delta W$ höher liegt, ist ihre Dichte um den Faktor $\exp(-\Delta W/(k_B T))$ kleiner.
Wie hoch die Stufe wird, misst man deshalb in Einheiten der __Temperaturspannung__:

:::formel Definition
$$U_T = \frac{k_B T}{e}$$
:::

**So liest man das:** $U_T$ ist die thermische Energie als Spannung ausgedrückt, 25,85 mV bei 300 K.
Man definiert sie, weil Potenzialstufen im Vergleich mit ihr wirken: Eine Stufe von 59,5 mV ändert eine Dichte im Gleichgewicht um den Faktor 10.

:::analogie
**Dieselbe Physik wie in der Erdatmosphäre.** Die Schwerkraft zieht die Luftmoleküle nach unten, das entspricht der Drift; die Wärmebewegung verteilt sie nach oben, das entspricht der Diffusion. Deshalb nimmt die Luftdichte mit der Höhe exponentiell ab, um den Faktor 2,72 je 8,4 km. Am pn-Übergang ist es genauso: Die Elektronendichte nimmt mit der Energie exponentiell ab, um den Faktor 2,72 je 25,85 meV.

| In der Atmosphäre | Am pn-Übergang |
|---|---|
| Höhe über dem Boden | Energie der Elektronen über dem n-Gebiet |
| Schwerkraft | Feld der freigelegten Rümpfe |
| 8,4 km je Faktor 2,72 | 25,85 meV je Faktor 2,72 |
| Luftdichte am Boden und auf dem Gipfel | Elektronendichte im n- und im p-Gebiet |

**Wo der Vergleich nicht stimmt:** Die Schwerkraft ist vorgegeben. Das Feld am pn-Übergang erzeugen die Ladungsträger selbst, indem sie abwandern und Rümpfe freilegen; deshalb stellt sich die Höhe der Stufe von selbst ein.
:::

:::formel Gesetz
$$U_\mathrm{Diff} = U_T\,\ln\frac{n_{n0}}{n_{p0}} = U_T\,\ln\frac{N_A\,N_D}{n_i^{2}}$$
:::

**So liest man das:** Eingabe sind die Dotierungen und die Temperatur, Ausgabe die Höhe der Stufe.
Sie ist so hoch, dass die Boltzmann-Verteilung den Dichteunterschied von 10¹² trägt: 27,6 Temperaturspannungen, also 0,714 V.
Jede Zehnerpotenz mehr Dotierung auf einer Seite erhöht sie um 59,5 mV; das n-Gebiet liegt höher, weil dort die positiven Rümpfe sitzen.

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

**Proben:** Einheit Volt. Dieselbe Rechnung mit den Löchern führt auf dasselbe Dichteverhältnis $N_A N_D/n_i^2$, also auf dieselbe Stufe; beide Sorten verlangen dieselbe Spannung, weil das Massenwirkungsgesetz beide Dichten koppelt. Grenzfall: Ohne Dotierung sind beide Dichten $n_i$, ihr Verhältnis ist 1, und die Stufe ist null.

**Grenzen:** Ab Dotierungen von etwa 10¹⁸ cm⁻³ wird die Boltzmann-Näherung ungenau.
:::

::::beispiel Diffusionsspannung der Beispieldiode
**Gegeben:** Dotierungen von 10¹⁶ cm⁻³ auf beiden Seiten; Eigenleitungsdichte 10¹⁰ cm⁻³; Temperaturspannung 25,85 mV.

**Gesucht:** (a) die Diffusionsspannung; (b) wie viele Elektronen des n-Gebiets genug Energie für die Stufe haben.

**Rechnung:** (a)

$$U_\mathrm{Diff} = 25{,}85\ \mathrm{mV}\cdot\ln\frac{10^{16}\cdot10^{16}}{10^{20}} = 25{,}85\ \mathrm{mV}\cdot\ln(10^{12})$$

$$= 25{,}85\ \mathrm{mV}\cdot27{,}63 = 0{,}714\ \mathrm{V}$$

(b) Den Bruchteil mit genug Energie gibt die Boltzmann-Verteilung:

$$n_{n0}\,\exp\!\Big(-\frac{U_\mathrm{Diff}}{U_T}\Big) = 10^{16}\ \mathrm{cm^{-3}}\cdot10^{-12} = 10^{4}\ \mathrm{cm^{-3}} = n_{p0}$$

**Ergebnis:** **0,714 V**; oben auf der Stufe gibt es genau so viele energiereiche Elektronen aus dem n-Gebiet, wie das p-Gebiet Elektronen hat.

**Einordnung:** Zehnfache Dotierung auf beiden Seiten ergäbe 0,833 V, nur 0,12 V mehr; der Logarithmus macht die Diffusionsspannung unempfindlich. Bei Siliziumdioden liegt sie fast immer zwischen 0,6 und 1 V.
::::

:::frage
„Kann man die Diffusionsspannung mit einem Voltmeter messen?“
Nein. Die Messleitungen bilden an beiden Enden Kontakte zwischen Metall und Halbleiter, an denen ebenfalls Potenzialstufen entstehen. Im Gleichgewicht ist die Summe aller Stufen im geschlossenen Kreis genau null; wäre sie es nicht, flösse ohne jede Energiequelle dauerhaft ein Strom. Das Voltmeter zeigt deshalb null.
:::

Das Skript nennt den Potenzialunterschied zwischen den Gebieten die „Durchlassspannung“ (S. 161).
Das sind zwei verschiedene Größen: Die Diffusionsspannung ist die innere Stufe im Gleichgewicht, die kein Voltmeter an den Anschlüssen zeigt; als Durchlass- oder Schleusenspannung bezeichnet man die Spannung, ab der eine Diode in einer Schaltung merklich Strom führt, typisch 0,6 bis 0,7 V bei Silizium.

## Zwei Ströme und die Wirkung einer Spannung

*Warum lässt der pn-Übergang Strom nur in eine Richtung durch?*

:::grafik
Szene: get1/halbleiterbauelemente/01-baender-spannung · Vorlage: banddiagramm-parameter
**Abbildung 5:** Bänder der Beispieldiode ohne Spannung (a), in Durchlassrichtung mit +0,5 V (b) und in Sperrrichtung mit −2 V (c), berechnet; das n-Gebiet ist jeweils festgehalten. Die Spannung verändert nur die Höhe der Stufe: 0,714 eV, 0,214 eV und 2,714 eV. Der Strom hinauf steigt bei +0,5 V auf das 2,5·10⁸-Fache seines Gleichgewichtswerts und sinkt bei −2 V auf das 2,5·10⁻³⁴-Fache; der Strom hinunter bleibt gleich.
:::

**Die Akteure:**

- __$U$__: äußere Spannung an der Diode, gezählt von der p-Seite, der __Anode__, zur n-Seite, der __Kathode__ ([Zählpfeile und Vorzeichen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zaehlpfeile-und-vorzeichen.html)). Positiv heißt __Durchlassrichtung__, negativ __Sperrrichtung__.
- __$I$__: Netto-Strom durch die Diode, gezählt von der Anode zur Kathode.
- __$I_S$__: __Sättigungssperrstrom__, der Betrag jedes der beiden Ströme, die im Gleichgewicht gegeneinander fließen; 1,46·10⁻¹⁴ A in der Beispieldiode mit 0,1 mm² Fläche.

**Das Zusammenspiel in Schritten**, für die Elektronen (für die Löcher gilt alles spiegelbildlich):

**Schritt 1**: Auch im Gleichgewicht wechseln ständig Elektronen die Seite. Von den 10¹⁶ Elektronen pro cm³ des n-Gebiets kommt nur hinüber, wer genug Wärmeenergie für die Stufe von 0,714 eV hat, nach Boltzmann der Bruchteil 10⁻¹². Das ist der Strom __hinauf__, ein Diffusionsstrom gegen das Feld.

**Schritt 2**: Ein Elektron aus dem p-Gebiet, das zufällig an den Rand der Zone gerät, wird vom Feld hinübergezogen, und zwar jedes einzelne. Das ist der Strom __hinunter__, ein Driftstrom.

**Schritt 3**: Der Bruchteil 10⁻¹² von 10¹⁶ sind 10⁴ Elektronen pro cm³, genau so viele, wie das p-Gebiet hat. Auf der Höhe der Stufe gibt es links und rechts also gleich viele Elektronen, und beide Ströme sind gleich groß. Wäre die Stufe niedriger, flössen netto Elektronen hinüber und legten weitere Rümpfe frei, bis die Stufe wieder diese Höhe hat. Gezählt werden dabei nur Ladungsträger, die die Seite ganz wechseln; die örtlichen Drift- und Diffusionsströme in der Zone sind viel größer und heben sich fast genau auf.

**Schritt 4**: Eine äußere Spannung fällt fast ganz an der Zone ab: Die gut leitenden neutralen Gebiete tragen den Strom schon mit einem winzigen Feld, bei 0,6 V nur einige Zehntel Volt pro Zentimeter. Die Spannung verändert deshalb nur die Höhe der Stufe: Eine Spannung in Durchlassrichtung verkleinert sie auf $U_\mathrm{Diff} - U$, eine in Sperrrichtung vergrößert sie (Abbildung 5).

**Schritt 5**: Der Strom hinauf reagiert exponentiell: Je 59,5 mV niedrigere Stufe haben zehnmal so viele Elektronen genug Energie. Der Strom hinunter reagiert gar nicht, denn jedes Minoritätselektron am Rand fällt hinab, wie hoch die Stufe auch ist; wie viele dort ankommen, bestimmt allein die Generation.

**Schritt 6**: In Durchlassrichtung überwiegt deshalb der Strom hinauf, und der Netto-Strom wächst um den Faktor 10 je 59,5 mV. In Sperrrichtung ist der Strom hinauf schon bei −0,1 V auf 2 % gefallen; übrig bleibt der Strom hinunter, 15 fA, und der hängt im idealen Modell nicht von der Spannung ab (Abbildung 6). Reale Siliziumdioden sperren schlechter, weil in der Zone selbst zusätzlich Paare entstehen; bei der Beispieldiode wären das bei −1 V etwa 20 pA, und dieser Anteil wächst langsam mit der Sperrspannung.

:::grafik
Szene: get1/halbleiterbauelemente/01-teilstroeme · Vorlage: kennlinie-semilog
**Abbildung 6:** Teilströme und Netto-Strom der Beispieldiode über der Spannung, halblogarithmisch. Der Netto-Strom folgt in Durchlassrichtung dem Strom hinauf (Faktor 10 je 59,5 mV), in Sperrrichtung dem konstanten Strom hinunter (15 fA).
:::

:::formel Gesetz
$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$
:::

**So liest man das:** Der erste Summand ist der Strom hinauf, die −1 steht für den Strom hinunter.
Ab etwa 0,08 V ist die −1 vernachlässigbar, unterhalb von −0,08 V ist der Strom praktisch −$I_S$.
Diese __Shockley-Gleichung__ untersucht der [Folgeartikel](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html) als Kennlinie der Diode.

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

::::beispiel Ströme der Beispieldiode und Spitzenspannung in einem Einweggleichrichter
**Gegeben:**
- Sättigungssperrstrom der Beispieldiode 1,457·10⁻¹⁴ A (genauer Wert aus dem Zahlenwerk);
- Temperaturspannung 25,85 mV;
- Einweggleichrichter: Wechselspannungsquelle mit Scheitelwert 10 V, Diode und Widerstand 1 kΩ in Reihe.

**Gesucht:** (a) die Ströme bei 0,4 V, 0,6 V und −1 V; (b) die Spitzenspannung am Widerstand des Gleichrichters.

**Rechnung:** (a) Mit der Shockley-Gleichung:

$$I(0{,}4\ \mathrm{V}) = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot\big[\exp(15{,}47) - 1\big]$$

$$= 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot5{,}245\cdot10^{6} = 76\ \mathrm{nA}$$

$$I(0{,}6\ \mathrm{V}) = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot1{,}201\cdot10^{10} = 0{,}175\ \mathrm{mA}$$

$$I(-1\ \mathrm{V}) = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot\big[\exp(-38{,}7) - 1\big] \approx -15\ \mathrm{fA}$$

(b) An der Spitze teilen sich Diode und Widerstand die 10 V. Nach $U$ aufgelöst lautet die Shockley-Gleichung

$$U = U_T\,\ln\Big(\frac{I}{I_S} + 1\Big)$$

Startwert 0,7 V an der Diode, also 9,3 V am Widerstand und 9,3 mA:

$$U = 25{,}85\ \mathrm{mV}\cdot\ln\Big(\frac{9{,}3\cdot10^{-3}\ \mathrm{A}}{1{,}457\cdot10^{-14}\ \mathrm{A}}\Big) = 25{,}85\ \mathrm{mV}\cdot27{,}18 = 0{,}703\ \mathrm{V}$$

Ein zweiter Durchgang mit 9,297 mA ändert das Ergebnis nicht mehr.

**Ergebnis:** **Im idealen Modell 76 nA, 0,175 mA und −15 fA; Spitze rund 9,3 V am Widerstand.**

**Einordnung:** Im Gleichrichter gehen rund 0,7 V an der Diode verloren, fast unabhängig vom Strom: Doppelter Strom kostet im idealen Modell nur 18 mV mehr. Mit 0,70 V liegt die Diode allerdings schon jenseits der Gültigkeitsgrenze von etwa 0,65 V; eine reale Diode verliert bei 9 mA etwas mehr, weil zusätzlich Spannung an den neutralen Gebieten abfällt.
::::

:::fehlvorstellung
„Unter 0,7 V fließt kein Strom durch die Diode.“
Das liegt nahe, weil eine Siliziumdiode in Schaltungen erst ab etwa 0,6 V merklich leitet, und das Skript schreibt, ein Strom fließe, sobald die Spannung die Durchlassspannung überschreitet (S. 161). Tatsächlich fließt bei jeder positiven Spannung Strom, nur wenig: im idealen Modell 76 nA bei 0,4 V und 3,7 µA bei 0,5 V; reale Dioden führen dort durch Rekombination in der Zone eher noch mehr. Die scheinbare Schwelle entsteht durch den steilen Anstieg; auf einer linearen Achse in Milliampere wird der Strom erst ab etwa 0,6 V sichtbar.
:::

Das Skript nennt den Sperrstrom einen „sehr kleinen Diffusionsstrom“ (S. 161).
Das ist die übliche Bezeichnung: Seine Größe bestimmt die Diffusion der Minoritätsträger in den neutralen Gebieten zum Rand der Zone; über die Zone selbst gelangen sie durch Drift, als Strom hinunter.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Reines Silizium leitet kaum | Die Bandlücke ist 43-mal größer als die thermische Energie; es gibt nur wenige bewegliche Ladungsträger. |
| Dotierung | Fremdatome übertreffen die wenigen Eigenleitungsträger um Zehnerpotenzen und legen Art und Zahl der Ladungsträger fest. |
| Raumladungszone und Diffusionsspannung | Der Dichteunterschied treibt Diffusion; die freigelegten Rümpfe bauen die Barriere auf. |
| Zwei Ströme im Gleichgewicht | Viele Ladungsträger mit winziger Erfolgsquote gleichen wenige mit voller Erfolgsquote aus. |
| Durchlass und Sperr | Die Spannung verschiebt nur die Barriere, und nur einer der beiden Ströme reagiert darauf. |

Ein Halbleiter hat wenige bewegliche Ladungsträger, deren Art und Zahl die Dotierung festlegt; wo ein n- und ein p-Gebiet aneinandergrenzen, baut der Dichteunterschied von selbst eine Barriere auf, deren Höhe eine äußere Spannung verschiebt.

## Bedeutung und Ausblick

Jede Siliziumdiode beruht auf diesem Mechanismus, vom Gleichrichter im Ladegerät bis zur Schutzdiode an einem Mikrocontroller-Eingang, und ein [Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) besteht aus zwei pn-Übergängen dicht hintereinander.
Oberhalb von etwa 0,65 V, im Durchbruch und bei hohen Temperaturen weicht eine reale Diode vom Modell ab; das behandelt der nächste Artikel, [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html).

**In der ausführlichen Fassung:** Fermi-Verteilung und Lage des Fermi-Niveaus mit Herleitung, der Temperaturgang der Eigenleitung (8,3 % pro Kelvin) und warum Silizium warm besser leitet als kalt, warum das fünfte Elektron des Phosphors so locker gebunden ist, die berechneten Profile von Dichte, Feld und Potenzial am Übergang, ein Wasserfall-Vergleich für den Sperrstrom und weitere Rechenbeispiele. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html)

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
F: Wie viele Löcher hat n-Silizium mit 10¹⁶ Donatoren pro cm³, und warum so wenige?
A: 10⁴ pro cm³, nach dem Massenwirkungsgesetz (10²⁰ cm⁻⁶ geteilt durch 10¹⁶ cm⁻³). Bei so vielen Elektronen trifft jedes Loch schnell einen Partner und rekombiniert.
F: Stimmt es, dass die Atomrümpfe in der Raumladungszone neutral sind?
A: Nein. P⁺ trägt +e, B⁻ trägt −e. Neutral ist ein Gebiet nur, wenn jeder Rumpf seinen beweglichen Gegenpart in der Nähe hat; in der Zone ist dieser fortdiffundiert, und die Rümpfe erzeugen ein Feld von über 3·10⁴ V/cm.
F: Warum wird die Barriere der Beispieldiode genau 0,714 V hoch?
A: Weil dann von den 10¹⁶ Elektronen des n-Gebiets genau der Bruchteil 10⁻¹² genug Energie hat, also 10⁴ pro cm³, so viele, wie das p-Gebiet hat. Erst dann sind die Ströme hinauf und hinunter gleich groß.
F: Stimmt es, dass unter 0,7 V kein Strom durch eine Siliziumdiode fließt?
A: Nein. Bei jeder positiven Spannung fließt Strom, bei der Beispieldiode im idealen Modell 76 nA bei 0,4 V. Er wächst nur so steil, um den Faktor 10 je 59,5 mV, dass er auf einer linearen Achse erst ab etwa 0,6 V sichtbar wird.
F: Warum hängt der Sperrstrom im idealen Modell nicht von der Sperrspannung ab?
A: Er ist der Strom hinunter: Jeder Minoritätsträger, der den Rand der Zone erreicht, wird hinübergezogen, ganz gleich, wie hoch die Stufe ist. Wie viele ankommen, bestimmt nur die Generation; der Strom hinauf ist schon bei −0,1 V auf 2 % gefallen. Reale Dioden haben zusätzlich einen Generationsstrom aus der Zone selbst, der mit der Sperrspannung langsam wächst.
:::
