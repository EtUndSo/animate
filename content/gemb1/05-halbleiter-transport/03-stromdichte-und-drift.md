---
title: Stromdichte und Drift
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Halbleiter und Ladungstransport
order: 4050300
summary: Wie aus beweglichen Ladungsträgern ein Strom wird – und zwei überraschende Einsichten dabei. Ein vollständig gefülltes Band trägt keinen Strom, obwohl es voller Elektronen steckt, weil sich die Geschwindigkeiten paarweise aufheben. Und ohne Streuung gäbe es gar keinen Gleichstrom, sondern nur Oszillationen. Erst die Streuung führt zum stationären Drift mit $J=\sigma E$, $\sigma=en\mu$ und $\mu=e\tau/m^\star$.
tags: Stromdichte, Drift, Gruppengeschwindigkeit, Bloch-Oszillation, Streuung, Beweglichkeit, Leitfähigkeit, Relaxationszeit
---

:::grafik
Einstiegs-Animation: Ein Kosinus-Band mit der im $k$-Raum besetzten Zustandswolke. Im Gleichgewicht ist sie
**symmetrisch** um $k=0$ — zu jedem Elektron bei $+k$ eines bei $-k$, Pfeile heben sich auf, kein Strom. Dann wird
ein Feld eingeschaltet: Die ganze Wolke **verschiebt** sich um $\delta k$ gegen das Feld; jetzt überwiegen die
$+v$-Elektronen → Netto-Strom. Eine zweite Spur zeigt ein einzelnes Elektron, das im Feld durch die Brillouin-Zone
„klettert", am Rand zurückgeworfen wird und **oszilliert** — bis ein Streu-Blitz es zurücksetzt. Kernbotschaft:
Strom ist die Asymmetrie der Besetzung, und Streuung macht ihn stationär.
:::

:::konzept
Wir wissen jetzt, **wie viele** bewegliche Ladungsträger ein Halbleiter hat. Jetzt die Frage: Wie erzeugen sie
einen __Strom__? Zwei Dinge sind dabei zunächst verblüffend. Erstens: Ein randvoll gefülltes Band trägt **keinen**
Strom, obwohl es die meisten Elektronen enthält — es kommt nicht auf die Zahl, sondern auf die **Asymmetrie** der
Besetzung an. Zweitens: Ohne Stöße gäbe es gar keinen stationären Gleichstrom, sondern nur Oszillationen —
ausgerechnet die **Streuung** (die man als „Widerstand" kennt) ermöglicht den gleichmäßigen Stromfluss. Am Ende
steht das vertraute Ohmsche Gesetz in seiner mikroskopischen Form $J=\sigma E$ mit der __Beweglichkeit__ $\mu$.
:::

**Worum es geht:** Wir schreiben den Strom als Summe über besetzte Zustände, verstehen *warum* volle Bänder und
das Gleichgewicht stromlos sind, wie ein Feld die Besetzung verschiebt, warum erst __Streuung__ einen Gleichstrom
erzeugt, und leiten die __Drift__-Form $J=en\mu E$ her.

## Strom als Summe über besetzte Zustände

Ein Strom ist bewegte Ladung. Jeder besetzte Zustand $k$ trägt mit seiner Ladung $-e$ mal seiner
__Gruppengeschwindigkeit__ $v(k)=\tfrac1\hbar\tfrac{\partial E}{\partial k}$ bei, gewichtet mit der Besetzung
$f(k)$. Die __Stromdichte__ ist die Summe über alle Zustände:

$$J = -\frac{e}{L}\sum_k v(k)\,f(k).$$

- __$v(k)=\tfrac1\hbar\tfrac{\partial E}{\partial k}$__: die Geschwindigkeit des Wellenpakets im Zustand $k$ (aus
  dem Bandstruktur-Oberthema).
- __$f(k)$__: die Besetzungswahrscheinlichkeit — hier entscheidet sich alles.

:::grafik
Das Kosinus-Band mit einigen besetzten Zuständen; zu jedem ein Geschwindigkeitspfeil $v(k)=\tfrac1\hbar
\partial E/\partial k$ (Steigung des Bandes). Darunter die Summenformel $J=-\tfrac{e}{L}\sum_k v(k)f(k)$.
:::

## Warum ein volles Band keinen Strom trägt

Die Banddispersion ist **symmetrisch**: $E(-k)=E(k)$, und damit $v(-k)=-v(k)$. In einem **vollständig gefüllten**
Band ist zu jedem besetzten Zustand $+k$ auch $-k$ besetzt. Ihre Geschwindigkeiten sind entgegengesetzt gleich und
heben sich **paarweise auf**:

$$\sum_k v(k)\,f(k) = 0 \quad\Rightarrow\quad J = 0.$$

Das Gleiche gilt im **Gleichgewicht** bei jeder Temperatur: Die Besetzung $f(k)$ ist dann symmetrisch in $k$, also
fließt kein Strom. Die Lehre: Nicht die **Zahl** der Elektronen erzeugt Strom, sondern eine **asymmetrische**
Besetzung — mehr Elektronen, die in eine Richtung laufen, als in die andere.

:::grafik
Ein voll besetztes (oder symmetrisch besetztes) Band: zu jedem $+k$-Zustand der Partner bei $-k$ markiert, mit
entgegengesetzten Pfeilen, die sich zu null addieren. Beschriftung „symmetrisch → $J=0$".
:::

## Wie ein Feld Strom erzeugt

Legt man ein elektrisches Feld $E$ an, wirkt auf jedes Elektron die Kraft $F=-eE$. Sie ändert den
**Kristallimpuls** $\hbar k$ nach der semiklassischen Bewegungsgleichung:

$$\hbar\frac{dk}{dt} = F \quad\Rightarrow\quad k(t) = k(0) + \frac{F}{\hbar}\,t.$$

Die **gesamte** Besetzungswolke verschiebt sich dadurch im $k$-Raum um einen kleinen Betrag $\delta k$. Jetzt ist
die Besetzung **asymmetrisch** — es gibt netto mehr Elektronen mit $v>0$ als mit $v<0$, und
$\sum_k v(k)f(k)\neq 0$. Es fließt ein Strom. Im Anschluss an die Elektrotechnik ist das gerade das Ohmsche Gesetz
in materialbezogener Form:

$$J = \sigma E, \qquad \sigma = \frac{1}{\rho}\ (\text{Leitfähigkeit}).$$

:::grafik
Die Fermi-Besetzung im $k$-Raum als Kreis/Intervall: links symmetrisch um $k=0$ (Gleichgewicht), rechts um
$\delta k$ verschoben (Feld an). Im verschobenen Fall sind die überzähligen $+k$-Zustände farbig hervorgehoben →
Netto-Strom. Pfeil „Feld verschiebt die Verteilung".
:::

## Warum erst Streuung einen Gleichstrom macht

Jetzt der zweite überraschende Punkt. Die Bewegungsgleichung $k(t)=k(0)+\tfrac{F}{\hbar}t$ sagt: Das Elektron
klettert im $k$-Raum **immer weiter**. Am Zonenrand $k=\pi/a$ wird es aber (wie im Bandstruktur-Oberthema)
**Bragg-reflektiert**, läuft zurück, wird erneut beschleunigt — es **oszilliert**. Diese __Bloch-Oszillation__
bedeutet: Im zeitlichen Mittel fließt **kein** Strom. Ein idealer, streufreier Kristall wäre also im Gleichfeld
stromlos!

Erst die **Streuung** (Stöße, die das Elektron aus seinem Zustand werfen) bricht diese Oszillation ab: Nach kurzer
Zeit wird das Elektron „zurückgesetzt", bevor es den Zonenrand erreicht. Es stellt sich ein **stationärer**
Zustand ein — eine konstante, kleine Verschiebung $\delta k$ der Verteilung, also ein konstanter Strom. Verblüffend:
Ausgerechnet die Streuung, die den elektrischen **Widerstand** verursacht, ist die Voraussetzung für einen
stetigen Gleichstrom.

:::grafik
Ein Elektron läuft im $E(k)$-Band bergauf Richtung Zonenrand; ohne Streuung kehrt es dort um und pendelt
(gestrichelte Oszillation, Mittelwert null). Mit einem „Streu-Blitz" wird es vorher zurückgesetzt → es verbleibt
bei kleiner mittlerer Verschiebung → stationärer Strom.
:::

**Woran streuen die Ladungsträger?** An mehreren Partnern:

- **Phononen** (Gitterschwingungen) — dominieren bei hoher Temperatur.
- **ionisierte Störstellen** (Coulomb-Potential der Dotieratome) — dominieren bei tiefer Temperatur / hoher
  Dotierung.
- **Defekte und Fehlstellen** im Gitter, sowie andere **Elektronen**.

Ändert ein Stoß nur die Richtung (gleiche Energie), ist er **elastisch**; ändert er auch die Energie,
**inelastisch**.

## Die Drift-Form: Beweglichkeit und Leitfähigkeit

Im stationären Zustand halten sich Beschleunigung durch das Feld und Abbremsung durch Streuung die Waage. Die
mittlere Zeit zwischen zwei Stößen ist die __Streu-/Relaxationszeit__ $\tau$. Das Ergebnis ist eine konstante
mittlere __Driftgeschwindigkeit__ proportional zum Feld, $v_{\text{drift}}=\mu E$, mit der __Beweglichkeit__

$$\mu = \frac{e\,\tau}{m^\star}.$$

Die Stromdichte ist dann (Ladungsträgerdichte $n$ mal Ladung mal Driftgeschwindigkeit):

$$J = e\,n\,v_{\text{drift}} = e\,n\,\mu\,E = \sigma E, \qquad \sigma = e\,n\,\mu.$$

- __$\mu=e\tau/m^\star$__: groß, wenn die Streuzeit $\tau$ groß (selten gestreut) und die effektive Masse $m^\star$
  klein ist.
- __$\sigma=en\mu$__: die Leitfähigkeit steigt mit **Ladungsträgerzahl** $n$ (Dotierung!) und **Beweglichkeit**.

Bisher haben wir nur **eine** Ladungsträgersorte betrachtet. In einem Halbleiter tragen aber **Elektronen und
Löcher** parallel zum Strom bei; ihre Leitfähigkeiten addieren sich:

$$\sigma = \sigma_n + \sigma_p = e\,n\,\mu_n + e\,p\,\mu_p.$$

Dabei ist $n$ die Elektronen-, $p$ die Löcherdichte und $\mu_n, \mu_p$ ihre (im Allgemeinen verschiedenen)
Beweglichkeiten.

**Warum beschleunigt das Elektron nicht unbegrenzt (unendlicher Strom)?** Weil jeder Stoß seinen Impulsgewinn im
Mittel wieder vernichtet — nach der Zeit $\tau$ beginnt die Beschleunigung von vorn. Daraus folgt eine
**endliche**, feldproportionale Driftgeschwindigkeit statt ewiger Beschleunigung. (Zahlenbeispiel: Das naive
Drude-Modell schätzt $\mu\approx15\,$cm²/Vs; reales Silizium erreicht $\mu\approx1500\,$cm²/Vs — der Unterschied
steckt in der kleinen effektiven Masse.)

:::grafik
Oben die „Sägezahn"-Geschwindigkeit eines einzelnen Elektrons: lineare Beschleunigung im Feld, dann abrupter
Reset durch einen Stoß, immer wieder — der Mittelwert ist die konstante Driftgeschwindigkeit $v_{\text{drift}}$.
Daneben $\mu=e\tau/m^\star$ und $J=en\mu E=\sigma E$.
:::

:::kern
Die __Stromdichte__ ist $J=-\tfrac{e}{L}\sum_k v(k)f(k)$ mit $v(k)=\tfrac1\hbar\partial E/\partial k$. Ein
**volles** (oder symmetrisch besetztes) Band trägt **keinen** Strom, weil $v(-k)=-v(k)$ sich paarweise aufhebt —
es zählt die **Asymmetrie**, nicht die Zahl. Ein Feld verschiebt die Verteilung ($\hbar\,dk/dt=F$) → asymmetrische
Besetzung → Strom $J=\sigma E$. Ohne Streuung würde das Elektron am Zonenrand Bragg-reflektiert und
**oszillieren** (__Bloch-Oszillation__, kein Gleichstrom); erst __Streuung__ (Phononen, ionisierte Störstellen,
Defekte) erzeugt den stationären Drift. Ergebnis: __Beweglichkeit__ $\mu=e\tau/m^\star$, Driftgeschwindigkeit
$v_{\text{drift}}=\mu E$, __Leitfähigkeit__ $\sigma=en\mu$.
:::

Der Drift ist die eine treibende Kraft für Strom — das elektrische Feld. Es gibt eine zweite, rein statistische:
ein **Konzentrationsgefälle** der Ladungsträger. Diese __Diffusion__ und ihre enge Verwandtschaft mit der
Beweglichkeit (die __Einstein-Beziehung__) sind das Thema des nächsten Artikels.
