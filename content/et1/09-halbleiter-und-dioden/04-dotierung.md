---
title: Stufe 2: Dotierung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1190400
summary: Reines Silizium hat zu wenige Ladungsträger, und ihre Zahl hängt stark von der Temperatur ab.
tags: Valenzelektronen, kovalente Bindung, Donator, Akzeptor, n-Gebiet, p-Gebiet, Mehrheitsträger, Minderheitsträger
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Reines Silizium hat zu wenige Ladungsträger, und ihre Zahl hängt stark von der Temperatur ab. Diese Stufe legt Art und Zahl der Träger mit Fremdatomen fest.
:::

**Die Idee.** Silizium hat vier __Valenzelektronen__ (Elektronen der äußersten Schale). Jedes Atom teilt mit jedem seiner vier Nachbarn ein Elektronenpaar, das ist die __kovalente Bindung__. Ersetzt man ein Atom durch Phosphor mit fünf Valenzelektronen, binden vier, das fünfte bleibt übrig (Abb. [3](#abb-3)). Es hängt nur mit 45 meV am Phosphorrumpf, das ist das 1,7-fache von $k_\mathrm BT$. Wärme löst es fast immer ab, es wird ein freies Elektron im LB, und ein ortsfestes $\mathrm P^+$-Ion bleibt zurück. Bor hat nur drei Valenzelektronen. Eine Bindung bleibt offen, und ein Nachbarelektron springt mit ebenfalls 45 meV hinein. Das ortsfeste $\mathrm B^-$-Ion bleibt, das Loch wandert davon.

:::abbildung et1/k9dotierung 3
Links: Kristall in der Ebene, jede Doppellinie ist eine Bindung. Rechts: Bänder bei 300 K, nicht maßstäblich. Das Niveau $W_\mathrm D$ des Phosphors liegt 45 meV unter dem LB, das Niveau $W_\mathrm A$ des Bors 45 meV über dem VB. Pfeile: Wärme gibt die Elektronen ins LB ab (oben) und holt sie aus dem VB (unten). Die Fermi-Energie rückt zum Band der Mehrheit.
:::

:::definition Definition 2.1 (n- und p-Dotierung)
<span class="anker" id="satz-2-1"></span>

Ein __Donator__ (Phosphor) gibt ein Elektron ab, ein __Akzeptor__ (Bor) nimmt eines auf. Mit $N_\mathrm D$ Donatoren je cm$^3$ entsteht ein __n-Gebiet__, mit $N_\mathrm A$ Akzeptoren je cm$^3$ ein __p-Gebiet__:

<span class="anker" id="gl-2-1"></span>
$$\text{n-Gebiet: }n\approx N_\mathrm D,\qquad\text{p-Gebiet: }p\approx N_\mathrm A,\qquad\text{überall: }n\,p=n_\mathrm i^2. \tag{2.1}$$
:::

⁠**So liest man das:** $n$ und $p$ sind die Dichten der Elektronen und Löcher in 1/cm$^3$. Die häufigere Sorte heißt __Mehrheitsträger__, die seltenere __Minderheitsträger__. Üblich sind $N=10^{15}$ bis $10^{19}\,\mathrm{cm^{-3}}$. Dotierung lädt den Kristall nicht auf: Zu jedem freien Elektron gehört ein ortsfestes $\mathrm P^+$. Die Fermi-Energie steigt im n-Gebiet um $k_\mathrm BT\ln(n/n_\mathrm i)$ über die Bandmitte. **Gültigkeit:** Raumtemperatur (alle Fremdatome ionisiert) und $N\gg n_\mathrm i$.

:::herleitung Warum das Produkt konstant ist
Die Wärme erzeugt Paare aus Elektron und Loch mit einer Rate, die nur von $T$ und dem Stoff abhängt. Rekombination braucht ein Treffen beider, ihre Rate ist $c\,n\,p$. Im Gleichgewicht sind beide Raten gleich, also ist $n\,p$ konstant. In reinem Silizium ist $n=p=n_\mathrm i$, also $n\,p=n_\mathrm i^2$. Mehr Elektronen bedeuten mehr Rekombination und weniger Löcher.
:::

::::beispiel
Mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ kommt ein Fremdatom auf $5\cdot10^{6}$ Siliziumatome, und doch steigt $n$ auf das Millionenfache von $n_\mathrm i$. Die Löcher sinken auf $p=10^{20}/10^{16}=10^{4}\,\mathrm{cm^{-3}}$. Mehrheit und Minderheit trennt der Faktor $10^{12}$. $W_\mathrm F$ steigt um $25{,}85\,\mathrm{meV}\cdot\ln10^{6}=0{,}36$ eV.
::::

⁠**Grenzfall:** Für $N_\mathrm D\to0$ ergibt [(2.1)](#gl-2-1) wieder $n=p=n_\mathrm i$.

:::frage Ist n-Silizium negativ und p-Silizium positiv geladen?
Nein, beide sind neutral. „n“ und „p“ nennen das Vorzeichen der beweglichen Ladungen, nicht das des Stücks. Im n-Gebiet steht jedem freien Elektron ein ortsfestes positives Ion gegenüber. Erst am pn-Übergang trennen sich beide (Stufe [3](die-raumladungszone.html#stufe-3)).
:::

:::aufgabe Aufgabe 2 ★★ Träger zählen
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Silizium erhält $N_\mathrm D=5\cdot10^{15}\,\mathrm{cm^{-3}}$. Wie viele Siliziumatome kommen auf ein Fremdatom? Wie groß sind $n$ und $p$?

</li>

<li>

Wie groß sind $n$ und $p$ bei $N_\mathrm A=2\cdot10^{17}\,\mathrm{cm^{-3}}$?

</li>

<li>

Vorhersage: Ein Stück erhält gleich viele Donatoren und Akzeptoren. Was passiert mit den Ladungsträgern?

</li>

</ol>

:::loesung
(a) $5\cdot10^{22}/5\cdot10^{15}=10^{7}$ Atome je Fremdatom, $n=5\cdot10^{15}\,\mathrm{cm^{-3}}$, $p=10^{20}/5\cdot10^{15}=2\cdot10^{4}\,\mathrm{cm^{-3}}$. (b) $p=2\cdot10^{17}\,\mathrm{cm^{-3}}$, $n=500\,\mathrm{cm^{-3}}$. (c) Jedes Donatorelektron fällt auf einen Akzeptor. Es entstehen keine zusätzlichen Träger, $n=p=n_\mathrm i$. Der Kristall verhält sich wie reines Silizium, obwohl er voller Ionen steckt. Das heißt __Kompensation__.
:::
:::

::::formelsammlung
**Mehrheitsträger**

$$\text{n-Gebiet: }n\approx N_\mathrm D,\qquad\text{p-Gebiet: }p\approx N_\mathrm A$$

$n$, $p$: Dichten der Elektronen und Löcher in 1/cm$^3$; $N_\mathrm D$, $N_\mathrm A$: Dichten der Donatoren und Akzeptoren, üblich $10^{15}$ bis $10^{19}\,\mathrm{cm^{-3}}$. Gilt bei Raumtemperatur (alle Fremdatome ionisiert) und für $N\gg n_\mathrm i$.

**Produkt der Trägerdichten**

$$n\,p=n_\mathrm i^2$$

Gilt überall im Gleichgewicht. $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ ist die Dichte der freien Elektronen in reinem Silizium. Die Minderheitsdichte ist $n_\mathrm i^2$ geteilt durch die Dotierung.

**Lage der Fermi-Energie im n-Gebiet**

$$k_\mathrm BT\ln(n/n_\mathrm i)$$

Betrag, um den $W_\mathrm F$ im n-Gebiet über der Bandmitte liegt.
::::

::::lernkarten
:::karte begriff Dotierung
Was bedeutet die Dotierung eines Halbleiters, und welche Größe legt man mit ihr fest?
---
Man baut wenige Fremdatome in den Kristall ein und legt so fest, wie viele Ladungsträger welcher Art er hat. Schon ein Fremdatom auf $5\cdot10^{6}$ Siliziumatome hebt $n$ auf das Millionenfache von $n_\mathrm i$.
--- falsch
Man erwärmt den Kristall gezielt und legt so Zahl und Art der Ladungsträger fest. Schon 10 K mehr heben $n$ auf das Millionenfache von $n_\mathrm i$, solange man die Temperatur danach konstant hält.
--- falsch
Man baut viele Fremdatome ein, etwa jedes zweite Atom, und ersetzt so das Silizium weitgehend durch ein Metall. Erst dann ändert sich die Zahl der Ladungsträger merklich.
--- falsch
Man lädt den Kristall mit zusätzlichen Elektronen auf und legt so seine Gesamtladung fest. Ein n-Gebiet ist danach negativ, ein p-Gebiet positiv geladen.
:::
:::karte begriff Valenzelektronen und kovalente Bindung
Was sind Valenzelektronen, und wie halten sie als kovalente Bindung den Siliziumkristall zusammen?
---
Valenzelektronen sind die Elektronen der äußersten Schale, Silizium hat vier. In der kovalenten Bindung teilt jedes Atom mit jedem seiner vier Nachbarn ein Elektronenpaar.
--- falsch
Valenzelektronen sind die Elektronen der innersten Schale, Silizium hat vier. In der kovalenten Bindung gibt jedes Atom sie an einen Nachbarn ab und wird dadurch zum Ion.
--- falsch
Valenzelektronen sind die freien Elektronen im LB, Silizium hat vier je Atom. In der kovalenten Bindung halten sie die Atome zusammen, indem sie zwischen allen Atomen umherwandern.
--- falsch
Valenzelektronen sind die Elektronen der äußersten Schale, Silizium hat fünf. In der kovalenten Bindung teilt jedes Atom mit jedem seiner fünf Nachbarn ein einzelnes Elektron.
:::
:::karte begriff Donator
Was macht ein Donator wie Phosphor im Siliziumkristall, und was bleibt dabei zurück?
---
Er gibt ein Elektron ab: Von seinen fünf Valenzelektronen binden vier, das fünfte hängt nur mit 45 meV am Rumpf und wird durch Wärme fast immer frei. Zurück bleibt ein ortsfestes $\mathrm P^+$-Ion.
--- falsch
Er nimmt ein Elektron auf: Von seinen drei Valenzelektronen binden alle, und ein Nachbarelektron füllt die offene Bindung. Zurück bleibt ein ortsfestes negatives Phosphor-Ion.
--- falsch
Er gibt ein Elektron ab: Das fünfte Valenzelektron ist mit 1,12 eV gebunden und wird nur bei hoher Temperatur frei. Zurück bleibt ein bewegliches $\mathrm P^+$-Ion, das dem Elektron folgt.
--- falsch
Er gibt alle fünf Valenzelektronen ab, weil Phosphor keine Bindung mit Silizium eingehen kann. Zurück bleibt ein fünffach positives Ion, das den Kristall auflädt.
:::
:::karte begriff Akzeptor
Was macht ein Akzeptor wie Bor im Siliziumkristall, und welcher bewegliche Ladungsträger entsteht dabei?
---
Er nimmt ein Elektron auf: Bor hat nur drei Valenzelektronen, eine Bindung bleibt offen, und ein Nachbarelektron springt hinein. Das ortsfeste $\mathrm B^-$-Ion bleibt, das Loch wandert davon.
--- falsch
Er gibt ein Elektron ab: Bor hat fünf Valenzelektronen, und das überzählige wird durch Wärme frei. Ein ortsfestes positives Bor-Ion bleibt zurück, das Elektron wandert als freier Ladungsträger davon ins LB.
--- falsch
Er nimmt ein Elektron auf: Bor hat drei Valenzelektronen, eine Bindung bleibt offen. Das Bor-Atom wird dabei selbst zum Loch und wandert als Ganzes durch den Kristall.
--- falsch
Er nimmt ein freies Elektron aus dem LB auf und hält es fest. Dadurch sinkt die Zahl der freien Elektronen, aber es entsteht kein neuer beweglicher Ladungsträger.
:::
:::karte begriff n-Gebiet und p-Gebiet
Was unterscheidet ein n-Gebiet von einem p-Gebiet, und welche Trägerdichte stellt sich jeweils ein?
---
Ein n-Gebiet enthält $N_\mathrm D$ Donatoren je cm$^3$, ein p-Gebiet $N_\mathrm A$ Akzeptoren je cm$^3$. Im n-Gebiet ist $n\approx N_\mathrm D$, im p-Gebiet $p\approx N_\mathrm A$.
--- falsch
Ein n-Gebiet ist negativ geladen, ein p-Gebiet positiv. Im n-Gebiet ist die Ladung je cm$^3$ gleich $-e\,N_\mathrm D$, im p-Gebiet $+e\,N_\mathrm A$, weil jedes Fremdatom eine Ladung trägt.
--- falsch
Ein n-Gebiet enthält $N_\mathrm A$ Akzeptoren je cm$^3$, ein p-Gebiet $N_\mathrm D$ Donatoren je cm$^3$. Im n-Gebiet ist $n\approx N_\mathrm A$, im p-Gebiet $p\approx N_\mathrm D$.
--- falsch
Ein n-Gebiet enthält $N_\mathrm D$ Donatoren je cm$^3$, ein p-Gebiet $N_\mathrm A$ Akzeptoren. In beiden ist $n=p=n_\mathrm i$, weil die Wärme die Wirkung der Dotierung ausgleicht.
:::
:::karte begriff Mehrheitsträger und Minderheitsträger
Welche Ladungsträger nennt man in einem dotierten Gebiet Mehrheitsträger und welche Minderheitsträger?
---
Die häufigere Sorte heißt Mehrheitsträger, die seltenere Minderheitsträger. Im n-Gebiet sind die Elektronen die Mehrheit und die Löcher die Minderheit, im p-Gebiet umgekehrt.
--- falsch
Die Ladungsträger, die von den Fremdatomen stammen, heißen Mehrheitsträger, die von der Wärme erzeugten Minderheitsträger. Im n-Gebiet sind beide Sorten Elektronen.
--- falsch
Die Elektronen heißen immer Mehrheitsträger, die Löcher immer Minderheitsträger, weil Elektronen in jedem Gebiet beweglicher sind als Löcher.
--- falsch
Die häufigere Sorte heißt Mehrheitsträger, die seltenere Minderheitsträger. Im n-Gebiet sind die Löcher die Mehrheit, weil jeder Donator ein positives Ion hinterlässt.
:::
:::karte formel Produkt der Trägerdichten
Welche Beziehung gilt im Gleichgewicht überall im Halbleiter zwischen den Dichten $n$ und $p$, und was folgt daraus für die Löcher im n-Gebiet?
---
$n\,p=n_\mathrm i^2$ mit der Dichte $n_\mathrm i$ in reinem Silizium. Mit $n\approx N_\mathrm D$ sinken die Löcher, bei $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ auf $p=10^{20}/10^{16}=10^{4}\,\mathrm{cm^{-3}}$.
--- falsch
$n+p=n_\mathrm i$, die Summe der Dichten bleibt fest. Mit $n\approx N_\mathrm D$ müsste $p$ negativ werden, also gibt es im n-Gebiet überhaupt keine Löcher.
--- falsch
$n\,p=n_\mathrm i^2$, aber nur in reinem Silizium. Im n-Gebiet ist zusätzlich $p\approx n_\mathrm i$, weil die Wärme dort ebenso viele Löcher erzeugt wie ohne Dotierung.
--- falsch
$n/p=n_\mathrm i$, das Verhältnis der Dichten bleibt fest. Mit $n\approx N_\mathrm D$ ist $p=N_\mathrm D/n_\mathrm i$, also gibt es mehr Löcher als in reinem Silizium.
:::
:::karte herleitung Warum das Produkt konstant ist
Wie folgt aus dem Gleichgewicht von Paarerzeugung und Rekombination, dass überall $n\,p=n_\mathrm i^2$ gilt?
---
Die Wärme erzeugt Paare aus Elektron und Loch mit einer Rate, die nur von $T$ und dem Stoff abhängt, weil dazu nur ein Elektron aus dem vollen VB ins LB gehoben werden muss.
---
Die Rate der Rekombination ist $c\,n\,p$, weil dabei ein Elektron und ein Loch einander treffen müssen.
---
Im Gleichgewicht sind beide Raten gleich, also ist $n\,p$ konstant, weil die Erzeugung nicht von $n$ und $p$ abhängt.
---
Die Konstante ist $n_\mathrm i^2$, weil in reinem Silizium $n=p=n_\mathrm i$ gilt.
:::
:::karte zusammenhang Ladung eines n-Gebiets
Ist ein Stück n-Silizium negativ geladen, weil es viele freie Elektronen enthält?
---
Nein, es ist neutral. „n“ nennt das Vorzeichen der beweglichen Ladungen, nicht das des Stücks: Jedem freien Elektron steht ein ortsfestes positives Ion gegenüber.
--- falsch
Ja, es ist negativ geladen, weil jeder Donator ein zusätzliches Elektron in den Kristall bringt. Diese Ladung verteilt sich gleichmäßig über das ganze Stück.
--- falsch
Ja, aber nur schwach: Ein Teil der freien Elektronen rekombiniert mit den Löchern, und nur der Rest bildet einen negativen Überschuss.
--- falsch
Nein, es ist positiv geladen, weil die Donatoren ihre Elektronen abgeben und als positive Ionen zurückbleiben. „n“ steht für die abgegebenen Elektronen.
:::
:::karte zusammenhang Bindung des fünften Elektrons
Warum liefert bei Raumtemperatur fast jedes Phosphoratom ein freies Elektron, während reines Silizium kaum freie Elektronen hat?
---
Das fünfte Elektron hängt nur mit 45 meV am Phosphorrumpf, dem 1,7-fachen von $k_\mathrm BT$; Wärme löst es fast immer ab. Ein Elektron aus einer Bindung bräuchte den Bandabstand, das 43-fache von $k_\mathrm BT$.
--- falsch
Das fünfte Elektron ist gar nicht gebunden, weil keine Bindung mehr für es übrig ist. Es ist schon bei $T=0$ frei, während die Siliziumelektronen erst den Bandabstand überwinden müssen.
--- falsch
Das fünfte Elektron hängt wie die Siliziumelektronen mit 1,12 eV am Rumpf, doch Phosphor schwingt stärker und gibt es durch Stöße leichter ab.
--- falsch
Phosphor senkt den Bandabstand des ganzen Kristalls auf 45 meV, sodass auch die Siliziumelektronen frei werden; die Zahl der freien Elektronen ist deshalb weit größer als $N_\mathrm D$, oft um das Hundertfache.
:::
:::karte begriff Kompensation
Was versteht man unter Kompensation, wenn ein Siliziumstück gleich viele Donatoren und Akzeptoren enthält?
---
Jedes Donatorelektron fällt auf einen Akzeptor, es entstehen keine zusätzlichen Träger, und $n=p=n_\mathrm i$. Der Kristall verhält sich wie reines Silizium, obwohl er voller Ionen steckt.
--- falsch
Jedes Donatorelektron und jedes Akzeptorloch wird frei, sodass $n\approx N_\mathrm D$ und $p\approx N_\mathrm A$ ist. Der Kristall leitet doppelt so gut wie ein nur mit einer Sorte dotierter.
--- falsch
Donatoren und Akzeptoren stoßen sich ab und sammeln sich an entgegengesetzten Enden des Stücks. Es entstehen von selbst ein n-Gebiet und ein p-Gebiet mit gleicher Dotierung.
--- falsch
Die Ionen heben sich gegenseitig auf, und die Fremdatome werden dabei wieder zu Siliziumatomen. Der Kristall ist danach wirklich rein und enthält keine Ionen mehr.
:::
:::karte formel Lage der Fermi-Energie im n-Gebiet
Um wie viel steigt die Fermi-Energie im n-Gebiet über die Bandmitte, und welchen Wert ergibt eine Dotierung mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$?
---
Um $k_\mathrm BT\ln(n/n_\mathrm i)$; sie rückt zum Band der Mehrheit, dem LB. Mit $n=10^{16}\,\mathrm{cm^{-3}}$ und $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ sind das $25{,}85\,\mathrm{meV}\cdot\ln10^{6}=0{,}36$ eV.
--- falsch
Um $k_\mathrm BT\,n/n_\mathrm i$, also linear mit der Dichte. Mit $n/n_\mathrm i=10^{6}$ wären das $25{,}85$ keV, weit über dem Rand des LB.
--- falsch
Um $k_\mathrm BT\ln(n/n_\mathrm i)$, aber nach unten zum VB, weil die Elektronen Energie abgeben. Mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ sinkt sie um 0,36 eV.
--- falsch
Um den halben Bandabstand $W_\mathrm g/2$, unabhängig von der Dotierung, weil schon wenige Donatoren sie an den Rand des LB schieben.
:::
:::karte zusammenhang Gültigkeit der Dotierungsformeln
Unter welchen Bedingungen darf man im n-Gebiet $n\approx N_\mathrm D$ setzen, und was ergibt sich ohne Dotierung?
---
Bei Raumtemperatur, wenn alle Fremdatome ionisiert sind, und für $N\gg n_\mathrm i$. Für $N_\mathrm D\to0$ ergibt sich wieder $n=p=n_\mathrm i$.
--- falsch
Nur bei $T=0$, weil die Wärme bei höherer Temperatur zusätzliche Elektronen erzeugt, die $n$ weit über $N_\mathrm D$ heben. Ohne Dotierung ist dann $n=0$.
--- falsch
Nur für $N_\mathrm D\ll n_\mathrm i$, weil sich die Donatorelektronen sonst gegenseitig verdrängen und nur ein Teil frei wird. Ohne Dotierung ist $n=p=n_\mathrm i$.
--- falsch
Bei jeder Temperatur und jeder Dotierung, weil jedes Fremdatom genau ein Elektron liefert und die Wärme keine weiteren Träger erzeugt. Ohne Dotierung ist $n=0$.
:::
::::
