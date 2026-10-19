---
title: Die Schrödinger-Gleichung
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010200
summary: Von Grund auf – warum man für Elektronen-Wellen eine eigene „Bewegungsgleichung" braucht, wie man sie aus Energieerhaltung und der Materiewelle konstruiert, warum man Zeit und Ort trennen darf (stationäre Zustände) und was die ebene Welle, die Gruppengeschwindigkeit und die effektive Masse bedeuten.
tags: Schrödinger-Gleichung, Wellenfunktion, Operator, stationäre Zustände, Separationsansatz, ebene Welle, Dispersion, Gruppengeschwindigkeit, effektive Masse
---

:::grafik
Einstiegs-Animation: In einem Potentialverlauf $V(x)$ (als „Landschaft" gezeichnet) liegt eine Wellenfunktion
$\psi(x)$. Man sieht, wie die Schrödinger-Gleichung ihre Form bestimmt: In Bereichen niedriger potentieller
Energie schwingt $\psi$ schnell (kurze Wellenlänge), in Bereichen hoher Energie langsam (lange Wellenlänge) oder
klingt ab. Darunter läuft die Zeit: Die Wellenfunktion dreht nur ihre Phase, während ihr Betragsquadrat
$|\psi|^2$ (die Aufenthaltswahrscheinlichkeit) ruhig stehen bleibt — ein stationärer Zustand. Kernbotschaft: Die
Schrödinger-Gleichung ist die „Bewegungsgleichung" für die Elektronen-Welle.
:::

:::konzept
Wir wissen jetzt: Ein Elektron ist eine Welle, beschrieben durch die Wellenfunktion $\psi$ (voriger Abschnitt).
Was noch fehlt, ist das **Gesetz**, das festlegt, welche Form diese Welle in einer gegebenen Umgebung annimmt —
das Gegenstück zu Newtons $F = m\,a$, aber für Wellen. Dieses Gesetz ist die **Schrödinger-Gleichung**. Mit ihr
rechnet man aus, welche Wellenformen und welche Energien ein Elektron in einem bestimmten Potential haben darf.
Sie ist das Arbeitspferd der gesamten Quantenmechanik und damit des ganzen Moduls.
:::

**Worum es geht:** Wir klären, *warum* man eine neue Gleichung braucht und wie man sie **konstruiert**, schreiben
die zeitabhängige und die stationäre Form auf, zeigen mit dem __Separationsansatz__, warum man Zeit und Ort
trennen darf, lösen sie für das einfachste Potential (die __ebene Welle__) und deuten __Gruppengeschwindigkeit__
und __effektive Masse__.

## Warum eine neue Gleichung — und warum nicht die klassische Wellengleichung?

In der klassischen Mechanik liefert $F = m\,a$ die **Bahn** $x(t)$ eines Teilchens. Für ein Elektron gibt es
aber keine Bahn mehr, sondern eine Welle $\psi(x,t)$ — gesucht ist also eine Gleichung, die $\psi$ bestimmt.

Man könnte auf die Idee kommen, einfach die bekannte **klassische Wellengleichung** zu nehmen (die etwa Schall-
oder Lichtwellen beschreibt). Das funktioniert aber nicht, und der Grund ist lehrreich: Die klassische
Wellengleichung beschreibt Wellen, die mit **fester** Geschwindigkeit laufen, bei denen also $\omega$
proportional zu $k$ ist. Für ein Elektron gilt aber die nichtrelativistische Energie-Impuls-Beziehung
$E = \tfrac{p^2}{2m}$ — mit $E = \hbar\omega$ und $p = \hbar k$ heißt das $\omega \propto k^2$, nicht $\omega
\propto k$. Man braucht also eine Gleichung, die genau diese **quadratische** Beziehung erzeugt. Genau danach
wird die Schrödinger-Gleichung gebaut.

Ein ehrlicher Hinweis vorab: Die Schrödinger-Gleichung lässt sich **nicht** aus der klassischen Physik ableiten
— sie ist ein neues Grundgesetz (ein Postulat). Man kann sie aber **motivieren** (plausibel machen), und genau
das tun wir jetzt.

## Die Gleichung konstruieren: Energieerhaltung mit Operatoren

Der Ausgangspunkt ist die Energieerhaltung. Die Gesamtenergie eines Teilchens ist Bewegungsenergie plus
Lageenergie:

$$E = \underbrace{\frac{p^2}{2m}}_{\text{kinetisch}} + \underbrace{V(x)}_{\text{potentiell}}.$$

Jetzt der entscheidende Schritt. Wir schauen, wie sich Energie und Impuls aus einer Materiewelle „herausholen"
lassen. Für eine ebene Welle $\psi = e^{\,i(kx - \omega t)}$ gilt nach de Broglie $p = \hbar k$ und $E =
\hbar\omega$ (mit $\hbar = h/2\pi$, dem reduzierten Wirkungsquantum). Leitet man die Welle ab, fallen genau
diese Größen heraus:

$$-i\hbar\,\frac{\partial \psi}{\partial x} = \hbar k\,\psi = p\,\psi, \qquad\qquad i\hbar\,\frac{\partial \psi}{\partial t} = \hbar\omega\,\psi = E\,\psi.$$

Das legt nahe, Energie und Impuls durch **Operatoren** (Rechenvorschriften, die auf $\psi$ wirken) zu
ersetzen:

- __$\hat{p} = -i\hbar\,\dfrac{\partial}{\partial x}$__: der __Impulsoperator__.
- __$\hat{E} = i\hbar\,\dfrac{\partial}{\partial t}$__: der __Energieoperator__.
- $\hat{p}^2/2m = -\dfrac{\hbar^2}{2m}\dfrac{\partial^2}{\partial x^2}$: der Operator der **kinetischen Energie**.

Setzt man diese Operatoren in die Energiebilanz $E = \tfrac{p^2}{2m} + V$ ein (jeweils angewendet auf $\psi$),
erhält man die __zeitabhängige Schrödinger-Gleichung__:

$$i\hbar\,\frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\,\frac{\partial^2 \psi}{\partial x^2} + V(x)\,\psi.$$

- __linke Seite__: die Gesamtenergie, auf $\psi$ angewendet ($\hat E \psi$).
- __erster Term rechts__: die kinetische Energie ($\hat p^2/2m\,\psi$) — sie hängt an der **Krümmung** von
  $\psi$ (zweite Ableitung): Je stärker die Welle gekrümmt ist (kurze Wellenlänge), desto höher die kinetische
  Energie.
- __zweiter Term rechts__: die potentielle Energie $V(x)\,\psi$.

Die ganze Gleichung sagt also schlicht: **Gesamtenergie = kinetische + potentielle Energie** — nur eben für eine
Welle formuliert.

:::grafik
Eine ebene Welle $e^{i(kx-\omega t)}$ mit zwei „Ausleseboxen": Die Box $-i\hbar\,\partial_x$ liefert daraus
$p = \hbar k$, die Box $i\hbar\,\partial_t$ liefert $E = \hbar\omega$. Pfeile zeigen, wie beide in die
Energiebilanz $E = p^2/2m + V$ eingesetzt werden und daraus die zeitabhängige Schrödinger-Gleichung entsteht.
:::

## Stationäre Zustände: warum man Zeit und Ort trennen darf

Die zeitabhängige Gleichung ist unhandlich. Zum Glück ist in fast allen Fällen das Potential $V(x)$ **zeitlich
konstant** (die „Landschaft" ändert sich nicht). Dann lohnt ein spezieller Ansatz: Man sucht Lösungen, bei denen
sich Orts- und Zeitabhängigkeit als **Produkt** trennen lassen, der __Separationsansatz__:

$$\psi(x,t) = \psi(x)\cdot \varphi(t).$$

**Schritt 1** — einsetzen und durch $\psi(x)\varphi(t)$ teilen. Dann steht links nur noch etwas, das von $t$
abhängt, rechts nur noch etwas, das von $x$ abhängt:

$$i\hbar\,\frac{\varphi'(t)}{\varphi(t)} = \frac{1}{\psi(x)}\left(-\frac{\hbar^2}{2m}\psi''(x) + V(x)\psi(x)\right).$$

**Schritt 2** — eine Größe, die zugleich nur von $t$ und nur von $x$ abhängt, muss **konstant** sein. Diese
Konstante ist gerade die Energie $E$.

**Schritt 3** — die beiden Teile getrennt lösen. Der Zeitteil $i\hbar\,\varphi' = E\,\varphi$ hat die Lösung

$$\varphi(t) = e^{-\,iEt/\hbar},$$

ein reiner **Phasendreher** mit der Kreisfrequenz $\omega = E/\hbar$. Der Ortsteil ist die __stationäre
(zeitunabhängige) Schrödinger-Gleichung__:

$$-\frac{\hbar^2}{2m}\,\psi''(x) + V(x)\,\psi(x) = E\,\psi(x).$$

**Warum „stationär"?** Weil die Aufenthaltswahrscheinlichkeit sich **nicht** mit der Zeit ändert: Da $\varphi(t)$
nur die Phase dreht, ist $|\psi(x,t)|^2 = |\psi(x)|^2\,|e^{-iEt/\hbar}|^2 = |\psi(x)|^2$ zeitlich konstant. Das
löst ganz nebenbei das Stabilitätsrätsel aus dem vorigen Abschnitt: Ein Elektron in einem solchen Zustand
fester Energie hat eine ruhende Ladungsverteilung und strahlt deshalb **nicht** ab — das Atom ist stabil. Diese
Zustände fester Energie sind die eigentlich gesuchten Objekte; man nennt sie __Eigenzustände__, die zugehörigen
$E$ ihre __Energieeigenwerte__.

:::grafik
Animation eines stationären Zustands: Die komplexe Wellenfunktion $\psi(x)\,e^{-iEt/\hbar}$ dreht gleichmäßig
ihre Phase (als rotierende Farbe/Zeiger entlang der Kurve dargestellt), während die Hüllkurve $|\psi(x)|^2$
darunter völlig unbewegt stehen bleibt. Beschriftung: „Phase dreht, Wahrscheinlichkeit ruht → stationär → keine
Abstrahlung".
:::

## Lösung für konstantes Potential: die ebene Welle

Der einfachste Fall ist das **freie Elektron**: ein konstantes Potential $V = \text{const}$ (ohne Beschränkung
der Allgemeinheit $V=0$). Die stationäre Gleichung wird dann

$$\psi''(x) = -\frac{2mE}{\hbar^2}\,\psi(x),$$

und das ist die bekannte Schwingungsgleichung mit den Lösungen $\psi(x) = e^{\pm i k x}$, einer __ebenen
Welle__, mit der __Wellenzahl__

$$k = \frac{\sqrt{2mE}}{\hbar} \qquad\Longleftrightarrow\qquad E = \frac{\hbar^2 k^2}{2m}.$$

Diese Beziehung zwischen Energie und Wellenzahl heißt __Dispersionsrelation__. Für das freie Elektron ist sie
eine **Parabel** $E(k) \propto k^2$ — genau die quadratische Beziehung, für die wir die Gleichung gebaut haben.
Diese $E(k)$-Kurve ist die „DNA" eines Materials: Im Kristall wird aus der freien Parabel später die
**Bandstruktur**, aus der sich Leiter, Halbleiter und Isolatoren ergeben.

:::grafik
Links die ebene Welle $e^{ikx}$ als gleichmäßig schwingende Kurve, die sich über den ganzen Raum erstreckt (ein
freies Elektron ist nirgends lokalisiert). Rechts die Dispersionsparabel $E(k) = \hbar^2 k^2/2m$ mit
beschrifteten Achsen; angedeutet, dass daraus im Kristall Energiebänder werden.
:::

## Wellenpaket, Gruppengeschwindigkeit und effektive Masse

Eine einzelne ebene Welle hat überall denselben Betrag — sie beschreibt ein Elektron, das über den **ganzen**
Raum „verschmiert" ist. Ein tatsächlich halbwegs lokalisiertes Teilchen baut man als __Wellenpaket__: eine
Überlagerung vieler ebener Wellen mit Wellenzahlen um einen Mittelwert $k_0$. Dieses Paket bewegt sich als Ganzes
mit der __Gruppengeschwindigkeit__

$$v_\text{g} = \frac{\mathrm{d}\omega}{\mathrm{d}k} = \frac{1}{\hbar}\frac{\mathrm{d}E}{\mathrm{d}k}.$$

Für das freie Elektron ($E = \hbar^2 k^2/2m$) ergibt das $v_\text{g} = \hbar k/m = p/m$ — also genau die
vertraute klassische Geschwindigkeit. Beruhigend: Im Mittel bewegt sich das Wellenpaket so, wie man es von einem
Teilchen erwartet.

Noch wichtiger für dieses Modul ist die zweite Ableitung. Fragt man, wie das Paket auf eine Kraft reagiert
(„beschleunigt"), landet man bei der __effektiven Masse__

$$\frac{1}{m^{*}} = \frac{1}{\hbar^2}\,\frac{\mathrm{d}^2 E}{\mathrm{d}k^2}.$$

Sie steckt in der **Krümmung** der $E(k)$-Kurve. Für das freie Elektron ist $\mathrm{d}^2E/\mathrm{d}k^2 =
\hbar^2/m$, also $m^{*} = m$ — die gewohnte Masse. Im Kristall aber ist die $E(k)$-Kurve keine einfache Parabel
mehr, sondern gekrümmt und verbogen; dort ist $m^{*}$ **anders** als die freie Elektronenmasse (manchmal
kleiner, manchmal größer, an Bandkanten sogar negativ). Die effektive Masse ist der Trick, mit dem man ein
Elektron im komplizierten Kristallpotential später trotzdem wie ein freies Teilchen behandeln kann — man steckt
die ganze Wirkung des Gitters in diese eine Zahl $m^{*}$.

:::grafik
Oben: Aus mehreren ebenen Wellen leicht verschiedener Wellenzahl entsteht durch Überlagerung ein lokalisiertes
Wellenpaket (Animation des Aufsummierens). Das Paket wandert mit der Gruppengeschwindigkeit $v_\text{g} =
\tfrac{1}{\hbar}\,\mathrm{d}E/\mathrm{d}k$. Unten: zwei $E(k)$-Kurven im Vergleich — eine stark gekrümmte (kleine
effektive Masse, „leichtes" Elektron) und eine flache (große effektive Masse, „schweres" Elektron), mit dem
Hinweis $1/m^{*} \propto \mathrm{d}^2E/\mathrm{d}k^2$.
:::

:::kern
Die __Schrödinger-Gleichung__ ist das Bewegungsgesetz der Elektronen-Welle. Man konstruiert sie aus der
Energiebilanz $E = \tfrac{p^2}{2m} + V$, indem man Impuls und Energie durch die __Operatoren__
$\hat p = -i\hbar\,\partial_x$ und $\hat E = i\hbar\,\partial_t$ ersetzt — das ergibt die __zeitabhängige__ Form
$i\hbar\,\partial_t\psi = -\tfrac{\hbar^2}{2m}\partial_x^2\psi + V\psi$ (kinetische Energie steckt in der Krümmung
von $\psi$). Bei zeitunabhängigem $V$ trennt der __Separationsansatz__ $\psi(x,t) = \psi(x)e^{-iEt/\hbar}$ Zeit
und Ort; übrig bleibt die __stationäre__ Gleichung $-\tfrac{\hbar^2}{2m}\psi'' + V\psi = E\psi$. Ihre Lösungen
sind __stationäre Zustände__ fester Energie ($|\psi|^2$ zeitlich konstant → keine Abstrahlung → stabile Atome).
Für konstantes $V$ ist die Lösung die __ebene Welle__ $e^{ikx}$ mit der __Dispersion__ $E = \hbar^2 k^2/2m$
(Parabel). Ein lokalisiertes Teilchen ist ein __Wellenpaket__ mit __Gruppengeschwindigkeit__ $v_\text{g} =
\tfrac{1}{\hbar}\mathrm{d}E/\mathrm{d}k$; die __effektive Masse__ $1/m^{*} = \tfrac{1}{\hbar^2}\mathrm{d}^2E/\mathrm{d}k^2$
folgt aus der Krümmung von $E(k)$ und macht Elektronen im Kristall wie freie Teilchen behandelbar.
:::

Jetzt haben wir das Werkzeug in der Hand. Wenden wir es auf den einfachsten eingesperrten Fall an — ein Elektron
zwischen zwei undurchdringlichen Wänden —, dann wird aus der Gitarrensaiten-Analogie des vorigen Abschnitts eine
exakte Rechnung: das __Teilchen in der Box__.
