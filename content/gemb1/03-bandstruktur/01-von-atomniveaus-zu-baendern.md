---
title: Von Atomniveaus zu Bändern
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bandstruktur
order: 4030100
summary: Das zentrale Prinzip der Festkörperelektronik – warum aus den scharfen, diskreten Energieniveaus einzelner Atome im Kristall breite Energiebänder mit verbotenen Lücken dazwischen werden. Der Mechanismus ist die Kopplung benachbarter Atome: Am $\text{H}_2^+$-Molekül spaltet ein Niveau in zwei (bindend/antibindend), bei $N$ Atomen wird daraus ein ganzes Band der Breite $\sim$ Kopplungsstärke.
tags: Energiebänder, Bandlücke, Kopplung, LCAO, bindend, antibindend, Tight-Binding, Atomorbitale
---

:::grafik
Einstiegs-Animation: Eine Reihe identischer Stimmgabeln, zunächst weit auseinander — jede schwingt mit ihrer
scharfen, gleichen Frequenz (= ein scharfes Atomniveau). Ein Schieberegler rückt sie enger zusammen auf einen
gemeinsamen Tisch; sie beginnen zu koppeln, und aus der einen Frequenz wird ein ganzes **Frequenzband** eng
benachbarter Gemeinschaftsschwingungen. Parallel dazu dasselbe für Atome: scharfe Niveaus $E_1, E_2, \ldots$ bei
großem Abstand, die beim Annähern zu breiten __Bändern__ auffächern, mit __Bandlücken__ dazwischen.
Kernbotschaft: Kopplung benachbarter Atome macht aus einem scharfen Niveau ein breites Band.
:::

:::konzept
Dies ist das **Herzstück** des ganzen Themenbereichs — die Frage, warum sich Festkörper elektrisch so unterschiedlich
verhalten (Metall, Halbleiter, Isolator), beginnt genau hier. Ein einzelnes Atom hat **scharfe, diskrete**
Energieniveaus (wie das „Teilchen in der Box" aus dem QM-Oberthema). Bringt man aber $10^{23}$ Atome zu einem
Kristall zusammen, entstehen aus jedem scharfen Niveau breite **Energiebänder** mit **verbotenen Lücken**
dazwischen. Der Grund ist ein einziger Mechanismus: die **Kopplung** benachbarter Atome über den Überlapp ihrer
Wellenfunktionen. Dieser eine Gedanke — *Atomniveau + Kopplung = Band* — trägt das gesamte Oberthema.
:::

**Worum es geht:** Wir verstehen *qualitativ* (die Rechnung folgt im nächsten Artikel), wie aus Atomniveaus
Bänder werden. Wir bauen es vom kleinsten Fall auf: erst **zwei** gekoppelte Atome (das $\text{H}_2^+$-Molekül),
dann **$N$** Atome (die Kette), und lesen daran den zentralen Zusammenhang *Kopplung ⇔ Bandbreite* ab.

## Ein Atom: scharfe Niveaus im Potentialtopf

Ein Elektron in einem isolierten Atom sitzt im anziehenden __Coulomb-Topf__ des Kerns. Wie beim Teilchen in der
Box sind dort nur bestimmte, **diskrete** Energien erlaubt — die scharfen Atomniveaus $E_1, E_2, E_3, \ldots$
Solange das Atom für sich allein steht, bleiben diese Niveaus **unendlich scharf**: eine einzige Energie pro
Niveau.

Die Frage ist also: Was passiert mit diesen scharfen Linien, wenn viele Atome dicht zusammenrücken?

:::grafik
Ein einzelner Coulomb-Topf mit den scharfen horizontalen Energieniveaus $E_1, E_2, E_3$ als Linien im Topf.
Daneben die Wellenfunktion des untersten Niveaus, die außerhalb des Topfes exponentiell abklingt (Anschluss an
Tunneleffekt/endliche Box).
:::

## Zwei Atome: aus einem Niveau werden zwei

Der kleinste Schritt zum Verständnis ist das __$\text{H}_2^+$-Molekül__: zwei Protonen, die sich **ein**
Elektron teilen. Jeder Kern hätte für sich das gleiche Atomorbital $\phi_1$ bzw. $\phi_2$ mit derselben Energie
$\epsilon_0$. Rücken die Kerne zusammen, **überlappen** die beiden Wellenfunktionen — und das Elektron kann nicht
mehr sagen, zu welchem Kern es gehört. Man beschreibt es deshalb als **Linearkombination** beider Atomorbitale
(der __LCAO-Ansatz__, *Linear Combination of Atomic Orbitals*):

$$\psi = c_1\,\phi_1 + c_2\,\phi_2.$$

Dafür gibt es genau zwei ausgezeichnete Möglichkeiten — und das ist der entscheidende Punkt:

- **Symmetrisch** ($c_1 = c_2$, gleiches Vorzeichen): Die Orbitale addieren sich **konstruktiv** zwischen den
  Kernen → dort sitzt viel Ladung, die beide Kerne „zusammenklebt". Das ist die __bindende__ Lösung, und sie
  liegt energetisch **tiefer** als $\epsilon_0$.
- **Antisymmetrisch** ($c_1 = -c_2$, entgegengesetztes Vorzeichen): **destruktive** Interferenz, ein __Knoten__
  (Nullstelle) genau zwischen den Kernen → keine bindende Ladung. Das ist die __antibindende__ Lösung, sie liegt
  **höher** als $\epsilon_0$.

Aus dem **einen** Atomniveau $\epsilon_0$ sind durch die Kopplung also **zwei** Molekülniveaus geworden — eines
darunter, eines darüber.

:::grafik
Links die zwei Atome mit je einem Niveau $\epsilon_0$ (weit entfernt). In der Mitte das Zusammenrücken. Rechts
das Ergebnis: $\epsilon_0$ spaltet in ein bindendes Niveau (tiefer, Wellenfunktion mit Bauch zwischen den Kernen)
und ein antibindendes (höher, Wellenfunktion mit Knoten dazwischen). Pfeile markieren „Aufspaltung durch
Kopplung".
:::

**Warum spaltet es überhaupt?** Weil zwei gekoppelte, gleiche Systeme nie dieselbe Energie behalten — genau wie
zwei gekoppelte Pendel nicht mehr mit *einer* Frequenz schwingen, sondern mit zweien (gleichphasig und
gegenphasig). Die Kopplung „zwingt" die entartete Energie auseinander.

## N Atome: aus einem Niveau wird ein Band

Jetzt koppeln wir nicht zwei, sondern eine ganze Kette aus $N$ Atomen. Die Logik setzt sich fort: Jedes der $N$
Atome steuert sein Niveau $\epsilon_0$ bei, und die Kopplung fächert sie in **$N$ eng benachbarte** Niveaus auf.
Weil $N$ gigantisch groß ist ($\sim 10^{23}$), liegen diese Niveaus so dicht, dass sie ein praktisch
**kontinuierliches Band** bilden:

- 2 Atome → 2 Niveaus
- $N$ Atome → $N$ Niveaus = ein __Band__

Jedes ursprüngliche Atomniveau ($E_1, E_2, \ldots$) wird so zu einem **eigenen** Band. Zwischen diesen Bändern
bleiben Energiebereiche, in denen es **keine** erlaubten Zustände gibt — die __Bandlücken__.

:::grafik
Ein „Fächer"-Diagramm: auf der x-Achse der Atomabstand (von groß nach klein), auf der y-Achse die Energie. Rechts
(große Abstände) scharfe Linien $E_1, E_2, E_3$; nach links fächern sie zu breiter werdenden Bändern auf.
Zwischen den Bändern bleiben weiße Streifen (Bandlücken). Senkrechte Linie beim realen Gitterabstand $a$ markiert,
wie breit die Bänder dort sind.
:::

## Der zentrale Zusammenhang: Kopplung ⇔ Bandbreite

Die eine Sache, die man sich merken muss: **Wie breit ein Band wird, hängt direkt von der Stärke der Kopplung
ab.** Und die Kopplung ist der Überlapp der Wellenfunktionen benachbarter Atome:

- **Enge Atome / dünne, niedrige Barrieren** zwischen den Töpfen → starker Überlapp → starke Kopplung →
  **breites** Band.
- **Weit auseinander / hohe, dicke Barrieren** → schwacher Überlapp → schwache Kopplung → **schmales** Band
  (im Grenzfall wieder die scharfe Atomlinie).

Dieser Zusammenhang ist technisch bares Geld wert: Über mechanische **Verspannung** (*strain*) ändert man den
Atomabstand und damit gezielt Bandbreite und Ladungsträger-Geschwindigkeit — in modernen Transistoren steigert
das den Strom spürbar.

:::grafik
Zwei Fälle übereinander: oben enge Töpfe mit dünner Barriere → starker Wellen-Überlapp → breites Band; unten
weite Töpfe mit dicker Barriere → kaum Überlapp → schmales Band. Daneben jeweils die Bandbreite als Doppelpfeil,
beschriftet „Überlapp = Kopplung = Bandbreite".
:::

:::kern
Das zentrale Prinzip: __Atomniveau + Kopplung = Band__. Ein isoliertes Atom hat scharfe, diskrete Niveaus. Rücken
Atome zusammen, **überlappen** ihre Wellenfunktionen (Kopplung), und jedes scharfe Niveau fächert auf. Am
__$\text{H}_2^+$-Molekül__ (LCAO $\psi = c_1\phi_1 + c_2\phi_2$) spaltet $\epsilon_0$ in ein __bindendes__
(symmetrisch, tiefer, Ladung zwischen den Kernen) und ein __antibindendes__ Niveau (antisymmetrisch, höher,
Knoten dazwischen). Bei $N$ Atomen werden daraus $N$ dicht liegende Niveaus = ein __Band__; dazwischen bleiben
__Bandlücken__. Die **Bandbreite** wächst mit der **Kopplungsstärke** (Überlapp): enge Atome / dünne Barrieren →
breites Band, weite Atome → schmales Band.
:::

Das war die anschauliche Seite. Im nächsten Artikel rechnen wir es aus: Mit dem __Tight-Binding__-Modell leiten
wir die konkrete Bandform $E(k) = \epsilon_0 - 2V_{ss}\cos(ka)$ her — das __Kosinus-Band__ — und sehen, dass die
Bandbreite exakt $4V_{ss}$ beträgt, also direkt die Kopplung misst.

:::quiz
F: Warum sind die Energieniveaus eines isolierten Atoms scharf und diskret?
A: Das Elektron sitzt im Coulomb-Topf des Kerns, und wie beim Teilchen in der Box sind dort nur bestimmte stehende Wellen und damit diskrete Energien erlaubt. Solange das Atom allein steht, gibt es keine Kopplung, die diese Linien verbreitern könnte.
F: Warum wird das Elektron im H₂⁺-Molekül als Linearkombination beider Atomorbitale beschrieben?
A: Rücken die Kerne zusammen, überlappen ihre Wellenfunktionen und das Elektron kann nicht mehr einem einzelnen Kern zugeordnet werden. Der LCAO-Ansatz $\psi=c_1\phi_1+c_2\phi_2$ trägt genau dieser Delokalisierung über beide Kerne Rechnung.
F: Was unterscheidet die bindende von der antibindenden Lösung?
A: Bei der bindenden (symmetrischen) addieren sich die Orbitale konstruktiv zwischen den Kernen, es sitzt viel Ladung dort, die sie zusammenhält — Energie tiefer als $\epsilon_0$. Bei der antibindenden (antisymmetrischen) gibt es einen Knoten dazwischen, keine bindende Ladung — Energie höher als $\epsilon_0$.
F: Warum liegt die bindende Lösung energetisch tiefer?
A: Weil sich zwischen den Kernen Ladung konzentriert, die der Anziehung beider positiver Kerne ausgesetzt ist — das senkt die potentielle Energie. Die antibindende mit ihrem Knoten meidet diesen günstigen Bereich und liegt daher höher.
F: Warum muss ein Atomniveau beim Koppeln überhaupt aufspalten?
A: Zwei gekoppelte gleiche Systeme behalten nie dieselbe Energie — wie zwei gekoppelte Pendel nicht mehr mit einer, sondern mit zwei Frequenzen (gleich- und gegenphasig) schwingen. Die Kopplung hebt die Entartung auf und zwingt die Energien auseinander.
F: Wie wird aus einem Atomniveau bei N Atomen ein Band?
A: Jedes der $N$ Atome steuert sein Niveau $\epsilon_0$ bei, und die Kopplung fächert sie in $N$ eng benachbarte Niveaus auf. Bei $N\sim10^{23}$ liegen diese so dicht, dass sie ein praktisch kontinuierliches Band bilden.
F: Woher kommen die Bandlücken zwischen den Bändern?
A: Jedes ursprüngliche Atomniveau ($E_1,E_2,\dots$) wird zu einem eigenen Band. Zwischen diesen Bändern bleiben Energiebereiche, in denen keine erlaubten Zustände liegen — das sind die verbotenen Bandlücken.
F: Wovon hängt die Breite eines Bandes ab?
A: Von der Kopplungsstärke, also dem Überlapp der Wellenfunktionen benachbarter Atome. Starker Überlapp (enge Atome, dünne Barrieren) ergibt ein breites Band, schwacher Überlapp ein schmales.
F: Was passiert mit der Bandbreite im Grenzfall sehr großer Atomabstände?
A: Dann überlappen die Wellenfunktionen kaum, die Kopplung geht gegen null und das Band schrumpft zur scharfen Atomlinie zusammen. Ohne Kopplung gibt es kein Band — man ist wieder beim isolierten Atom.
F: Wie nutzt man den Zusammenhang Kopplung ⇔ Bandbreite technisch aus?
A: Über mechanische Verspannung (strain) ändert man den Atomabstand und damit gezielt Überlapp, Bandbreite und Ladungsträger-Geschwindigkeit. In modernen Transistoren steigert das den Strom spürbar (strained silicon).
:::
