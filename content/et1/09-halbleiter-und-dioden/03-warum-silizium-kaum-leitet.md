---
title: Stufe 1: Warum Silizium kaum leitet
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1190300
summary: Metall leitet, Glas nicht, reines Silizium kaum.
tags: Energieniveaus, Band, verbotene Zone, Valenzband, Leitungsband, Bandabstand, Fermi-Energie, Metall
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Metall leitet, Glas nicht, reines Silizium kaum. Der Unterschied liegt in der Zahl der beweglichen Elektronen. Diese Stufe erklärt sie aus den erlaubten Energien im Kristall.
:::

**Die Idee.** Im einzelnen Atom haben Elektronen nur bestimmte Energien, die __Energieniveaus__. Im Kristall (regelmäßiges Gitter von Atomen) überlappen sich die Hüllen, die Elektronen gehören dem ganzen Kristall. Keine zwei Elektronen dürfen denselben Zustand besetzen. Deshalb spaltet jedes Niveau in so viele dicht liegende Niveaus auf, wie der Kristall Atome hat. So entsteht ein __Band__ erlaubter Energien. Zwischen den Bändern liegt die __verbotene Zone__: Dort gibt es keine Zustände. Ein Feld kann ein Elektron nur beschleunigen, wenn knapp über ihm ein freier Zustand liegt. Ein volles Band leitet also nicht, gleich wie viele Elektronen es enthält.

:::abbildung et1/k9baender 2
Bändermodell, nicht maßstäblich; $W$ ist die Energie eines Elektrons. Im Metall ist das oberste Band nur teilweise gefüllt. Im Halbleiter hebt Wärme wenige Elektronen über die kleine Lücke, zurück bleiben Löcher. Im Isolator ist die Lücke zu groß.
:::

:::definition Definition 1.1 (Bänder)
<span class="anker" id="satz-1-1"></span>

Das __Valenzband__ (VB) ist das oberste Band, das bei $T=0$ voll besetzt ist. Das __Leitungsband__ (LB) liegt darüber und ist bei $T=0$ leer. Der __Bandabstand__ $W_\mathrm g$ ist die kleinste Energie, die ein Elektron vom VB ins LB hebt. Die __Fermi-Energie__ $W_\mathrm F$ trennt bei $T=0$ besetzte von leeren Zuständen. Bei $T>0$ ist sie die Energie, bei der ein Zustand zur Hälfte der Zeit besetzt wäre; sie darf in der Lücke liegen, obwohl es dort keinen Zustand gibt.
:::

⁠**So liest man das:** Silizium hat $W_\mathrm g=1{,}12$ eV, Germanium 0,67 eV, Diamant 5,5 eV. **Drei Fälle:** Im __Metall__ ist das oberste besetzte Band nur teilweise gefüllt, freie Zustände liegen direkt über den Elektronen, und es leitet bei jeder Temperatur. Im __Isolator__ ist $W_\mathrm g$ so groß, dass kein Elektron hinübergelangt. Ein Halbleiter ist ein Isolator mit kleiner Lücke: Bei $T=0$ isoliert er, bei Anregung durch Wärme, Licht oder starke Felder gelangen Elektronen ins LB.

Ein Elektron, das ins LB wechselt, hinterlässt im VB einen freien Platz. Ein Nachbarelektron rückt nach, und der Platz wandert. Das __Loch__ (Defektelektron) verhält sich wie ein bewegliches Teilchen mit der Ladung $+e$. Beide zählen als Ladungsträger: Elektronen im LB und Löcher im VB. Fällt ein Elektron in ein Loch zurück, verschwinden beide, das heißt __Rekombination__.

:::satz Satz 1.2 (Anteil der Elektronen im Leitungsband)
<span class="anker" id="satz-1-2"></span>

In reinem Halbleiter liegt $W_\mathrm F$ in der Mitte der Lücke. Für die Zustände am Rand des LB ist deshalb

<span class="anker" id="gl-1-1"></span>
$$\text{Besetzung}\approx\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}. \tag{1.1}$$
:::

:::herleitung Warum die halbe Lücke zählt
Jedes Elektron im LB lässt ein Loch im VB zurück, also ist die Zahl beider gleich. Das geht bei ähnlich vielen Zuständen in beiden Bändern nur, wenn $W_\mathrm F$ von beiden Bandrändern denselben Abstand $W_\mathrm g/2$ hat. In [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1) zählt die Energie über $W_\mathrm F$, also $W=W_\mathrm g/2$.
:::

::::beispiel
Bei 300 K ist $W_\mathrm g/(k_\mathrm BT)=43{,}3$ und $\mathrm{e}^{-21{,}7}=3{,}9\cdot10^{-10}$. Die gemessene Dichte der freien Elektronen beträgt $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$. Das ist eines je $5\cdot10^{12}$ Atome, denn Silizium hat $5\cdot10^{22}$ Atome je cm$^3$. Kupfer hat $8{,}5\cdot10^{12}$-mal mehr freie Elektronen ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).
::::

⁠**Grenzfälle:** Für $T\to0$ geht [(1.1)](#gl-1-1) gegen null: Silizium isoliert. Je 10 K Erwärmung verdoppelt sich der Anteil. Deshalb sinkt der Widerstand eines Halbleiters mit der Temperatur ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

:::frage Warum leitet ein volles Band nicht, obwohl es voller Elektronen steckt?
Weil Strom eine Bewegung in Vorzugsrichtung braucht. Dafür müsste ein Elektron in einen Zustand mit etwas mehr Energie wechseln. Im vollen Band ist jeder solche Zustand besetzt. Zwei Elektronen könnten nur tauschen, und das ändert nichts. Das erste Loch macht das Band leitfähig.
:::

:::aufgabe Aufgabe 1 ★ Drei Stoffe vergleichen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Gib $W_\mathrm g=1{,}12$ eV in Joule an. Das Wievielfache von $k_\mathrm BT$ ist das bei 300 K?

</li>

<li>

Berechne [(1.1)](#gl-1-1) für Silizium, Germanium und Diamant. Welcher reine Stoff leitet am besten?

</li>

<li>

Silizium erwärmt sich von 300 K auf 330 K. Um welchen Faktor wächst der Anteil?

</li>

</ol>

:::loesung
(a) $1{,}12\cdot1{,}602\cdot10^{-19}\,\mathrm{J}=1{,}79\cdot10^{-19}$ J, das sind $1{,}12\,\mathrm{eV}/25{,}85\,\mathrm{meV}=43{,}3$-mal $k_\mathrm BT$. (b) Silizium $3{,}9\cdot10^{-10}$, Germanium $2{,}4\cdot10^{-6}$, Diamant $6{,}3\cdot10^{-47}$. Germanium leitet am besten, rund 6000-mal mehr Besetzung als Silizium, Diamant hat praktisch keine freien Elektronen. (c) Mit $U_T=28{,}44$ mV bei 330 K ist der Anteil $2{,}8\cdot10^{-9}$, das 7,2-fache.
:::
:::

::::formelsammlung
**Bandabstand von Silizium**

$$W_\mathrm g=1{,}12\,\mathrm{eV}$$

Kleinste Energie, die ein Elektron vom Valenzband ins Leitungsband hebt. Germanium 0,67 eV, Diamant 5,5 eV.

**Anteil der Elektronen im Leitungsband**

$$\text{Besetzung}\approx\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}$$

Besetzung der Zustände am Rand des Leitungsbands in reinem Halbleiter, in dem die Fermi-Energie $W_\mathrm F$ in der Mitte der Lücke liegt. Für $T\to0$ geht sie gegen null; bei Silizium verdoppelt sie sich je 10 K Erwärmung.
::::

::::lernkarten
:::karte begriff Energieniveaus
Was versteht man unter den Energieniveaus der Elektronen in einem einzelnen Atom?
---
Die bestimmten, einzelnen Energien, die ein Elektron im einzelnen Atom haben kann. Energien zwischen diesen Werten kommen für ein Elektron im Atom nicht vor.
--- falsch
Die Energien, die ein Elektron beim Durchlaufen von 1, 2, 3 und mehr Volt gewinnt. Dazwischen sind alle Werte möglich, solange das Elektron frei ist.
--- falsch
Die Schalen, auf denen die Elektronen ruhen. Ihre Energie ist für alle Atome gleich groß und hängt nur von der Temperatur ab.
--- falsch
Die Bereiche, in denen ein Elektron jede beliebige Energie annehmen kann. Zwischen ihnen gibt es keine Elektronen, weil dort die Wärme fehlt.
:::
:::karte begriff Band
Wie entsteht im Kristall aus einem Energieniveau des einzelnen Atoms ein Band erlaubter Energien?
---
Im Kristall überlappen sich die Hüllen, und die Elektronen gehören dem ganzen Kristall. Weil keine zwei Elektronen denselben Zustand besetzen dürfen, spaltet jedes Niveau in so viele dicht liegende Niveaus auf, wie der Kristall Atome hat.
--- falsch
Im Kristall stoßen die Elektronen ständig mit den Atomen zusammen. Jeder Stoß verschiebt ihre Energie ein wenig, und so verschmiert jedes Niveau zu einem Bereich, der mit der Temperatur breiter wird.
--- falsch
Im Kristall bleiben die Hüllen getrennt, aber die Niveaus aller Atome liegen genau aufeinander. Ein Band ist also ein einzelnes Niveau, das so viele Elektronen aufnimmt, wie der Kristall Atome hat.
--- falsch
Im Kristall überlappen sich die Hüllen, und die Elektronen gehören dem ganzen Kristall. Dabei verschmelzen alle Niveaus zu einem einzigen breiten Band, das jede Energie von null bis zur Bindungsenergie der Elektronen lückenlos umfasst.
:::
:::karte begriff verbotene Zone
Was ist die verbotene Zone im Bändermodell eines Kristalls?
---
Der Energiebereich zwischen zwei Bändern. Dort gibt es keine Zustände, ein Elektron kann also keine Energie aus diesem Bereich haben.
--- falsch
Der Bereich im Kristall, in dem keine Atome sitzen. Elektronen dürfen sich dort nicht aufhalten, weil sie keine Bindung eingehen können.
--- falsch
Der Energiebereich oberhalb des obersten Bands. Elektronen, die ihn erreichen, verlassen den Kristall und tragen deshalb nichts zum Strom bei.
--- falsch
Der Energiebereich zwischen zwei Bändern. Dort gibt es zwar Zustände, doch sie dürfen nur bei hoher Temperatur besetzt werden.
:::
:::karte zusammenhang Volles Band
Warum leitet ein vollständig besetztes Band nicht, obwohl es viele Elektronen enthält?
---
Strom braucht eine Bewegung in Vorzugsrichtung, dafür müsste ein Elektron in einen Zustand mit etwas mehr Energie wechseln. Im vollen Band ist jeder solche Zustand besetzt, und ein Tausch zweier Elektronen ändert nichts.
--- falsch
Die Elektronen eines vollen Bands sind so dicht gepackt, dass sie sich gegenseitig abstoßen und das Feld abschirmen. Im Inneren des Bands wirkt deshalb keine Kraft auf sie, und sie bleiben trotz der angelegten Spannung in Ruhe.
--- falsch
Die Elektronen eines vollen Bands sind fest an ihre Atome gebunden, weil volle Bänder immer die innersten Schalen sind. Erst Elektronen äußerer Schalen können wandern.
--- falsch
Ein Feld beschleunigt alle Elektronen des vollen Bands gleich stark, aber die Hälfte läuft in Gegenrichtung. Beide Ströme heben sich deshalb in jedem Augenblick genau auf.
:::
:::karte begriff Valenzband und Leitungsband
Wie unterscheiden sich Valenzband und Leitungsband eines Halbleiters bei der Temperatur $T=0$?
---
Das Valenzband (VB) ist das oberste Band, das bei $T=0$ voll besetzt ist. Das Leitungsband (LB) liegt darüber und ist bei $T=0$ leer.
--- falsch
Das Valenzband (VB) ist das oberste Band, das bei $T=0$ leer ist. Das Leitungsband (LB) liegt darunter und ist bei $T=0$ voll besetzt.
--- falsch
Das Valenzband (VB) und das Leitungsband (LB) sind bei $T=0$ beide halb besetzt. Das LB liegt über dem VB und nimmt bei Erwärmung dessen Elektronen auf.
--- falsch
Das Valenzband (VB) ist das unterste Band und enthält die Elektronen der inneren Schalen. Das Leitungsband (LB) ist bei $T=0$ voll besetzt und trägt den Strom.
:::
:::karte begriff Bandabstand
Was gibt der Bandabstand $W_\mathrm g$ eines Halbleiters an, und wie groß ist er bei Silizium?
---
Die kleinste Energie, die ein Elektron vom VB ins LB hebt. Bei Silizium ist $W_\mathrm g=1{,}12$ eV, bei Germanium 0,67 eV, bei Diamant 5,5 eV.
--- falsch
Den räumlichen Abstand zweier Atome im Kristall, über den ein Elektron beim Leiten springen muss. Bei Silizium sind es 1,12 nm, bei Germanium 0,67 nm.
--- falsch
Die größte Energie, die ein Elektron im VB haben kann, gemessen vom unteren Rand des Bands. Bei Silizium ist $W_\mathrm g=1{,}12$ eV, bei Diamant 0,67 eV.
--- falsch
Die kleinste Energie, die ein Elektron vom VB ins LB hebt. Bei Silizium ist $W_\mathrm g=25{,}85$ meV, genau so viel wie die Wärmeenergie bei 300 K.
:::
:::karte begriff Fermi-Energie
Welche Energie bezeichnet die Fermi-Energie $W_\mathrm F$ bei $T=0$ und bei $T>0$?
---
Bei $T=0$ trennt sie besetzte von leeren Zuständen. Bei $T>0$ ist sie die Energie, bei der ein Zustand zur Hälfte der Zeit besetzt wäre; sie darf in der Lücke liegen, obwohl es dort keinen Zustand gibt.
--- falsch
Bei $T=0$ ist sie die Energie des untersten Zustands im VB. Bei $T>0$ steigt sie mit der Wärmeenergie und erreicht bei Raumtemperatur den unteren Rand des LB.
--- falsch
Bei $T=0$ trennt sie besetzte von leeren Zuständen. Bei $T>0$ ist sie die Energie, ab der alle Zustände sicher leer sind; sie liegt deshalb immer im LB und nie in der Lücke, weil es dort keine Zustände gibt.
--- falsch
Bei $T=0$ ist sie die Energie, die ein Elektron zum Verlassen des Kristalls braucht. Bei $T>0$ sinkt sie, weil die Wärme einen Teil dieser Arbeit liefert.
:::
:::karte begriff Metall
Woran erkennt man im Bändermodell ein Metall, und warum leitet es bei jeder Temperatur?
---
Sein oberstes besetztes Band ist nur teilweise gefüllt. Freie Zustände liegen direkt über den Elektronen, also kann ein Feld sie bei jeder Temperatur beschleunigen.
--- falsch
Sein Bandabstand ist kleiner als die Wärmeenergie $k_\mathrm BT$, sodass Wärme einige Elektronen ins LB hebt. Bei $T=0$ isoliert es dagegen wie jeder Halbleiter.
--- falsch
Sein oberstes Band ist voll besetzt und enthält besonders viele Elektronen. Je mehr Elektronen ein Band enthält, desto besser leitet es bei jeder Temperatur.
--- falsch
Es hat gar keine Bänder, weil seine Elektronen nicht an Atome gebunden sind. Die Elektronen können jede Energie annehmen und deshalb immer Strom tragen.
:::
:::karte zusammenhang Isolator
Warum leitet ein Isolator im Bändermodell auch bei Raumtemperatur praktisch nicht, und was unterscheidet ihn von einem Halbleiter?
---
Sein Bandabstand $W_\mathrm g$ ist so groß, dass kein Elektron ins LB gelangt. Ein Halbleiter ist ein Isolator mit kleiner Lücke, über die Wärme, Licht oder starke Felder einige Elektronen heben.
--- falsch
Sein oberstes Band ist nur teilweise gefüllt, aber die Elektronen darin sind zu schwer, um zu wandern. Ein Halbleiter hat leichtere Elektronen und leitet deshalb etwas.
--- falsch
Er hat kein Leitungsband, weil seine Atome zu weit auseinanderliegen. Ein Halbleiter hat ein Leitungsband, das aber erst ab etwa 1000 K Elektronen aufnimmt.
--- falsch
Sein Bandabstand ist kleiner als bei einem Halbleiter, aber seine Elektronen sind fest an die Löcher gebunden. Ein Halbleiter hat keine Löcher und leitet deshalb bei gleicher Temperatur leichter als ein Isolator.
:::
:::karte begriff Halbleiter
Was ist ein Halbleiter im Bändermodell, und wie verhält er sich bei $T=0$ und bei Anregung?
---
Ein Stoff mit kleiner Bandlücke, dessen Leitfähigkeit zwischen Metall und Isolator liegt und sich gezielt einstellen lässt. Bei $T=0$ isoliert er; Wärme, Licht oder starke Felder heben Elektronen ins LB.
--- falsch
Ein Metall mit wenigen freien Elektronen, dessen oberstes Band nur zu einem kleinen Teil gefüllt ist. Bei $T=0$ leitet er gut, und Wärme verringert seine Leitfähigkeit, weil die Atome stärker schwingen.
--- falsch
Ein Stoff ohne Bandlücke, dessen Bänder sich überlappen. Bei $T=0$ leitet er halb so gut wie ein Metall, weil nur die Hälfte seiner Elektronen frei ist.
--- falsch
Ein Isolator mit großer Bandlücke, der nur bei starkem Feld leitet. Bei $T=0$ und bei Erwärmung isoliert er gleich gut, denn Wärme hebt keine Elektronen ins LB.
:::
:::karte begriff Loch
Was ist ein Loch (Defektelektron) im Valenzband, und wie bewegt es sich?
---
Der freie Platz, den ein ins LB gewechseltes Elektron im VB hinterlässt. Ein Nachbarelektron rückt nach, der Platz wandert, und das Loch verhält sich wie ein bewegliches Teilchen mit der Ladung $+e$.
--- falsch
Ein Fehlplatz im Kristallgitter, an dem ein ganzes Atom fehlt. Es bewegt sich nicht, fängt aber vorbeikommende Elektronen ein und trägt deshalb die Ladung $-e$.
--- falsch
Ein positiv geladener Atomrumpf, der beim Ablösen eines Elektrons zurückbleibt und ins LB aufsteigt. Er wandert wie ein Elektron durch den Kristall, aber in Feldrichtung, und trägt die Ladung $+e$.
--- falsch
Der freie Platz, den ein Elektron im LB hinterlässt, wenn es ins VB zurückfällt. Er wandert im LB mit und trägt die Ladung $-e$ wie ein Elektron.
:::
:::karte begriff Ladungsträger
Welche beweglichen Ladungen zählen in einem Halbleiter als Ladungsträger?
---
Bewegliche Ladungen, die einen Strom tragen können: die Elektronen im LB und die Löcher im VB.
--- falsch
Alle Elektronen des Kristalls, auch die im vollen VB, denn jedes Elektron trägt die Ladung $-e$ und wird im Feld beschleunigt.
--- falsch
Nur die Elektronen im LB. Löcher sind bloß fehlende Elektronen und tragen keinen eigenen Strom.
--- falsch
Die Ionen des Kristalls und die Elektronen im LB, denn beide sind geladen und werden im Feld beschleunigt.
:::
:::karte begriff Rekombination
Was geschieht bei der Rekombination in einem Halbleiter mit den beteiligten Ladungsträgern?
---
Ein Elektron aus dem LB fällt in ein Loch im VB zurück, und beide Ladungsträger verschwinden.
--- falsch
Ein Elektron aus dem VB springt durch Wärme ins LB, und es entsteht ein neues Paar aus Elektron und Loch.
--- falsch
Zwei Löcher vereinigen sich zu einem doppelt positiv geladenen Loch, das sich langsamer bewegt.
--- falsch
Ein Elektron aus dem LB verlässt den Kristall an der Oberfläche, und das zugehörige Loch bleibt allein zurück.
:::
:::karte formel Anteil der Elektronen im Leitungsband
Welcher Anteil der Zustände am Rand des Leitungsbands ist in reinem Halbleiter besetzt, und warum steht dort der halbe Bandabstand?
---
$\text{Besetzung}\approx\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}$. In reinem Halbleiter liegt $W_\mathrm F$ in der Mitte der Lücke, und in der Boltzmann-Verteilung zählt die Energie über $W_\mathrm F$, also $W_\mathrm g/2$.
--- falsch
$\text{Besetzung}\approx\mathrm{e}^{-W_\mathrm g/(k_\mathrm BT)}$. Ein Elektron muss die ganze Lücke überwinden, und in der Boltzmann-Verteilung zählt die volle Energie vom VB bis zum LB.
--- falsch
$\text{Besetzung}\approx\mathrm{e}^{-2W_\mathrm g/(k_\mathrm BT)}$. Ein Elektron und ein Loch müssen beide die Lücke überwinden, deshalb zählt in der Boltzmann-Verteilung die doppelte Energie.
--- falsch
$\text{Besetzung}\approx W_\mathrm g/(2k_\mathrm BT)$. Die Besetzung wächst linear mit der Lücke, weil eine größere Lücke mehr Zustände für Elektronen bietet.
:::
:::karte herleitung Warum die halbe Lücke zählt
Wie folgt aus der Boltzmann-Verteilung, dass in reinem Halbleiter die Besetzung am Rand des LB etwa $\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}$ beträgt?
---
Die Zahl der Elektronen im LB ist gleich der Zahl der Löcher im VB, weil jedes Elektron im LB ein Loch im VB zurücklässt.
---
Bei ähnlich vielen Zuständen in beiden Bändern muss $W_\mathrm F$ deshalb von beiden Bandrändern denselben Abstand $W_\mathrm g/2$ haben, weil sonst eine der beiden Sorten häufiger wäre.
---
In der Boltzmann-Verteilung $\mathrm{e}^{-W/(k_\mathrm BT)}$ setzt man $W=W_\mathrm g/2$ ein, weil die Energie über $W_\mathrm F$ zählt.
---
Es folgt $\text{Besetzung}\approx\mathrm{e}^{-W_\mathrm g/(2k_\mathrm BT)}$, weil der Rand des LB genau $W_\mathrm g/2$ über $W_\mathrm F$ liegt.
:::
:::karte zusammenhang Reines Silizium bei Raumtemperatur
Warum leitet reines Silizium bei 300 K kaum, obwohl Wärme Elektronen ins LB heben kann?
---
Seine Bandlücke ist 43-mal größer als die Wärmeenergie $k_\mathrm BT$. Besetzt ist nur der Anteil $\mathrm{e}^{-21{,}7}=3{,}9\cdot10^{-10}$ der Randzustände, frei ist eines je $5\cdot10^{12}$ Atome.
--- falsch
Seine Elektronen sind alle fest gebunden, weil Silizium gar kein Leitungsband besitzt. Nur Verunreinigungen liefern ein paar freie Ladungen, eine je $5\cdot10^{12}$ Atome.
--- falsch
Seine Bandlücke ist kleiner als die Wärmeenergie, doch die Elektronen im LB rekombinieren sofort wieder, sodass im Mittel nur eines je $5\cdot10^{12}$ Atome frei ist.
--- falsch
Sein oberstes Band ist nur teilweise gefüllt, aber die freien Zustände darüber liegen so dicht, dass sich die Elektronen gegenseitig blockieren und kaum wandern.
:::
:::karte zusammenhang Erwärmung von Silizium
Was passiert mit dem Anteil der Elektronen im LB von Silizium, wenn es sich um 10 K erwärmt, und was folgt daraus für seinen Widerstand?
---
Der Anteil verdoppelt sich je 10 K Erwärmung, weil er exponentiell von $W_\mathrm g/(2k_\mathrm BT)$ abhängt. Deshalb sinkt der Widerstand eines Halbleiters mit der Temperatur.
--- falsch
Der Anteil steigt je 10 K um rund 3 %, so wie die absolute Temperatur selbst. Der Widerstand des Halbleiters ändert sich deshalb kaum mit der Temperatur.
--- falsch
Der Anteil verdoppelt sich je 10 K Erwärmung. Der Widerstand steigt trotzdem, weil die zusätzlichen Elektronen öfter mit den Atomen zusammenstoßen.
--- falsch
Der Anteil halbiert sich je 10 K, weil die Wärme Elektronen aus dem LB ins VB zurückwirft. Der Widerstand des Halbleiters steigt deshalb mit der Temperatur.
:::
:::karte zusammenhang Silizium, Germanium und Diamant
Welcher der drei reinen Stoffe Silizium, Germanium und Diamant leitet bei 300 K am besten, und warum?
---
Germanium, weil es mit 0,67 eV die kleinste Lücke hat: Seine Besetzung ist rund 6000-mal größer als bei Silizium. Diamant hat mit 5,5 eV praktisch keine freien Elektronen.
--- falsch
Diamant, weil er mit 5,5 eV die größte Lücke hat: Eine große Lücke bietet den Elektronen viel Platz im LB, und die Besetzung ist dort deshalb bei jeder Temperatur am höchsten.
--- falsch
Silizium, weil sein Bandabstand von 1,12 eV genau der Wärmeenergie bei Raumtemperatur entspricht und die Elektronen dann am leichtesten übergehen.
--- falsch
Alle drei gleich gut, weil reine Stoffe bei derselben Temperatur dieselbe Wärmeenergie haben und der Bandabstand nur die Farbe des Stoffs bestimmt.
:::
::::
