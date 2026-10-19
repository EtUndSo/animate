---
title: Tight-Binding und das Kosinus-Band
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bandstruktur
order: 4030200
summary: Die quantitative Herleitung eines Bandes – aus der Schrödinger-Gleichung auf einer Atomkette. Wir diskretisieren sie, erkennen den Hüpfparameter $t$ als Maß der Kopplung und erhalten mit einem ebene-Welle-Ansatz das Kosinus-Band $E(k)=\epsilon_0-2V_{ss}\cos(ka)$ mit der Bandbreite $4V_{ss}$. Aus seiner Steigung folgt die Gruppengeschwindigkeit, die an den Rändern der Brillouin-Zone null wird (Bragg-Reflexion).
tags: Tight-Binding, Kosinus-Band, Hüpfparameter, Hamilton-Matrix, Gruppengeschwindigkeit, Bragg-Reflexion, Bloch-Welle
---

:::grafik
Einstiegs-Animation: Oben eine Atomkette (Abstand $a$); eine Welle läuft darüber und „hüpft" von Atom zu Atom,
wobei die Hüpfstärke $t$ als leuchtende Brücke zwischen Nachbarn dargestellt ist. Darunter baut sich synchron die
Energiekurve $E(k)$ auf — ein Kosinus-Band, das sich von der Bandunterkante bei $k=0$ bis zum Bandrand bei
$k=\pi/a$ erstreckt. Ein zweiter Zeiger zeigt die **Steigung** der Kurve als Geschwindigkeit des Elektrons: steil
in der Mitte, flach (null) an beiden Rändern. Kernbotschaft: Eine Kette gekoppelter Atome ergibt ein
Kosinus-Band, und seine Form steckt voller Physik.
:::

:::konzept
Im vorigen Artikel haben wir *anschaulich* gesehen, dass Kopplung aus einem Atomniveau ein Band macht. Jetzt
**rechnen** wir es aus — mit dem __Tight-Binding-Modell__ („stark gebunden": die Elektronen bleiben überwiegend
an ihren Atomen und hüpfen nur gelegentlich zum Nachbarn). Das Schöne: Es gibt zwei Wege zum selben Ergebnis.
Einmal als reine **Rechenmethode** (die Schrödinger-Gleichung numerisch auf einem Gitter), einmal als
**physikalisches Modell** (gekoppelte Atomorbitale). Beide liefern dieselbe Bandform — das __Kosinus-Band__ — und
genau das ist die Brücke zwischen „Rechentrick" und echter Festkörperphysik.
:::

**Worum es geht:** Wir diskretisieren die Schrödinger-Gleichung, lesen am __Hüpfparameter__ die Kopplung ab,
gewinnen mit einem ebene-Welle-Ansatz das __Kosinus-Band__ und leiten daraus die __Gruppengeschwindigkeit__ der
Elektronen her — mit der überraschenden Folge, dass sie am Rand der Brillouin-Zone verschwindet.

## Die Schrödinger-Gleichung auf einem Gitter

Für ein realistisches Kristallpotential lässt sich die Schrödinger-Gleichung nicht geschlossen lösen. Der Ausweg:
Wir werten die Wellenfunktion nur an diskreten Gitterpunkten $x_j = j\,a$ aus (Abstand $a$) und ersetzen die
zweite Ableitung durch einen **Differenzenquotienten** über die Nachbarpunkte:

$$\frac{d^2\psi}{dx^2} \;\longrightarrow\; \frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{a^2}.$$

Setzt man das in die 1D-Schrödinger-Gleichung ein und sortiert um, entsteht die __diskrete
Schrödinger-Gleichung__:

$$-t\,(\psi_{j+1} - 2\psi_j + \psi_{j-1}) + V_j\,\psi_j = E\,\psi_j, \qquad t = \frac{\hbar^2}{2m a^2}.$$

- __$\psi_j$__: die Wellenfunktion am Gitterplatz $j$.
- __$t$__: der __Hüpfparameter__ (*hopping*) — er verknüpft einen Platz mit seinen Nachbarn. Physikalisch: wie
  leicht das Elektron zum Nachbarplatz übergeht. Wichtig: $t \propto 1/a^2$ — je enger das Gitter, desto stärker
  die Kopplung.
- __$V_j$__: die potentielle Energie am Platz $j$.

:::grafik
Die kontinuierliche Kurve $\psi(x)$ mit drei markierten Stützstellen $\psi_{j-1}, \psi_j, \psi_{j+1}$ im Abstand
$a$; darunter die Differenzenformel, die daraus die zweite Ableitung macht. Ein Pfeil „$t$ koppelt Nachbarn"
verbindet $\psi_j$ mit $\psi_{j\pm1}$.
:::

## Die Hamilton-Matrix: sitzen und hüpfen

Schreibt man die diskrete Gleichung für alle Plätze als Gleichungssystem, entsteht eine __tridiagonale
Hamilton-Matrix__ — Einträge nur auf der Haupt- und den beiden Nebendiagonalen. Jeder Eintrag hat eine klare
Bedeutung:

- **Hauptdiagonale** $2t + V_j$: die __Onsite-Energie__ — die Energie, am Platz $j$ zu **sitzen**.
- **Nebendiagonalen** $-t$: der Kopplungsterm — der Energiebeitrag durch **Hüpfen** zum Nachbarn.

Dieses Muster — Diagonale = „sitzen", Nebendiagonale = „hüpfen" — kehrt in **jeder** Tight-Binding-Rechnung
wieder, egal wie kompliziert der Kristall ist.

:::grafik
Eine tridiagonale Matrix, deren Hauptdiagonale mit „$2t+V_j$ = sitzen" und deren Nebendiagonalen mit „$-t$ =
hüpfen" beschriftet sind; daneben die zugeordnete Atomkette, bei der „sitzen" ein Atomplatz und „hüpfen" eine
Brücke zum Nachbarn ist.
:::

## Das Kosinus-Band

Bei konstantem Potential $V_j \equiv V_0$ ist jeder Platz gleichwertig — die Lösung muss eine **ebene Welle**
sein (hier ist $i$ die imaginäre Einheit, $j$ der Platz-Index):

$$\psi_j = \Phi_0\,e^{ikja}, \qquad \psi_{j\pm 1} = \psi_j\,e^{\pm ika}.$$

Einsetzen in die diskrete Gleichung lässt $\psi_j$ herausfallen, und mit $e^{ika}+e^{-ika}=2\cos(ka)$ bleibt:

$$E(k) = 2t\,\bigl(1 - \cos(ka)\bigr) + V_0.$$

Das ist das __Kosinus-Band__: Die erlaubten Energien liegen nicht mehr scharf, sondern verteilen sich stetig über
einen Bereich der Breite $4t$ (von $V_0$ bei $k=0$ bis $V_0+4t$ am Bandrand $k=\pi/a$).

:::grafik
Die Kurve $E(k)=2t(1-\cos ka)+V_0$ über der 1. Brillouin-Zone $[-\pi/a, \pi/a]$: Minimum $V_0$ bei $k=0$, Maximum
$V_0+4t$ an den Rändern. Die Bandbreite $4t$ ist als vertikaler Doppelpfeil markiert.
:::

## Dasselbe aus Atomsicht: Bandbreite = Kopplung

Rechnet man statt der numerischen Diskretisierung das **physikalische** Modell (eine Kette echter Atomorbitale,
gekoppelt über das Überlappintegral $V_{ss}$ zum Nachbarn), kommt exakt dieselbe Form heraus:

$$E(k) = \epsilon_0 - 2V_{ss}\cos(ka).$$

- __$\epsilon_0$__: die __Onsite-Energie__ — das ursprüngliche Atomniveau; es liegt in der **Bandmitte**.
- __$V_{ss}$__: das __Kopplungs-/Überlappintegral__ zweier benachbarter s-Orbitale.

Jetzt wird der Zusammenhang aus dem vorigen Artikel **quantitativ**: Die **Bandbreite** beträgt genau $4V_{ss}$ —
sie misst direkt die Kopplung. Der numerische Hüpfparameter $t$ und das physikalische Überlappintegral $V_{ss}$
spielen dieselbe Rolle. Damit schließt sich der Kreis: *ein Atomniveau $\epsilon_0$, aufgeweitet durch die
Nachbarkopplung, ergibt ein Kosinus-Band der Breite $4V_{ss}$.*

:::grafik
Das Kosinus-Band mit der Bandmitte auf Höhe $\epsilon_0$ und der Gesamtbreite $4V_{ss}$ (Doppelpfeil). Links
daneben ein schmales Band (kleines $V_{ss}$, schwache Kopplung), rechts ein breites Band (großes $V_{ss}$) — mit
Beschriftung „Bandbreite $= 4V_{ss} =$ Kopplung".
:::

## Die Gruppengeschwindigkeit

Wie schnell bewegt sich ein Elektron mit Wellenzahl $k$? Nicht die Welle selbst, sondern das aus mehreren $k$
zusammengesetzte **Wellenpaket** transportiert das Elektron — mit der __Gruppengeschwindigkeit__, die sich aus
der **Steigung** des Bandes ergibt:

$$v = \frac{1}{\hbar}\frac{\partial E}{\partial k} = \frac{2V_{ss}\,a}{\hbar}\,\sin(ka).$$

Daran liest man direkt die Physik der Ladungsträger ab:

- **Bei $k=0$ (Bandunterkante):** $v=0$, und wegen $1-\cos(ka)\approx\tfrac12(ka)^2$ ist das Band dort eine
  **Parabel**. Das Elektron verhält sich wie ein **freies** Teilchen mit fester Masse — ein Befund, der im
  nächsten Artikel zur effektiven Masse führt.
- **In der Bandmitte** ist $v$ maximal — hier bewegt sich das Elektron am schnellsten.
- **Am Bandrand $k=\pi/a$:** $\sin(\pi)=0$, also wieder $v=0$.

:::grafik
Zwei übereinanderliegende Kurven über $k\in[-\pi/a,\pi/a]$: oben $E(k)$ (Kosinus), unten die Steigung
$v(k)\propto\sin(ka)$. Markiert: $v=0$ bei $k=0$ und $k=\pi/a$, Maximum von $v$ dazwischen; am Minimum von $E$ die
angeschmiegte Parabel „$\approx$ freies Elektron".
:::

## Warum das Elektron am Bandrand stehen bleibt

Dass die Geschwindigkeit am Bandrand verschwindet, überrascht — dort ist die Energie am höchsten. **Warum
transportiert das Elektron dort nichts mehr?** Weil die Welle am Bandrand $k=\pi/a$ gerade die Bedingung für
**Bragg-Reflexion** am periodischen Gitter erfüllt: Sie wird an den Atomreihen so zurückgeworfen, dass hin- und
rücklaufende Welle sich zu einer **stehenden Welle** überlagern. Eine stehende Welle läuft nicht — sie trägt
keinen Netto-Strom, daher $v=0$.

:::grafik
Am Bandrand $k=\pi/a$: eine einlaufende und eine Bragg-reflektierte Welle überlagern sich zu einer stehenden
Welle über der Atomkette (Knoten/Bäuche ortsfest). Beschriftung „Bragg-Reflexion → stehende Welle → $v=0$".
:::

:::kern
Das __Tight-Binding-Modell__ liefert ein Band aus der Atomkette. Aus der kontinuierlichen Schrödinger-Gleichung
wird per Differenzenquotient die __diskrete__ Form $-t(\psi_{j+1}-2\psi_j+\psi_{j-1})+V_j\psi_j=E\psi_j$ mit dem
__Hüpfparameter__ $t=\hbar^2/(2ma^2)$; die __Hamilton-Matrix__ ist tridiagonal (Diagonale $2t+V_j$ = sitzen,
Nebendiagonale $-t$ = hüpfen). Der ebene-Welle-Ansatz $\psi_j=\Phi_0 e^{ikja}$ gibt das __Kosinus-Band__
$E(k)=2t(1-\cos ka)+V_0 = \epsilon_0 - 2V_{ss}\cos(ka)$ mit Bandbreite $4V_{ss}$ (= Kopplung). Die
__Gruppengeschwindigkeit__ $v=\tfrac1\hbar\partial E/\partial k = \tfrac{2V_{ss}a}{\hbar}\sin(ka)$ ist null bei
$k=0$ (dort parabolisch ≈ frei) und am Bandrand $k=\pi/a$ (dort __Bragg-Reflexion__ → stehende Welle), maximal in
der Bandmitte.
:::

Wir haben jetzt die Form eines **einzelnen** Bandes. Reale Festkörper haben aber **mehrere** Bänder mit
**Lücken** dazwischen — und erst deren **Besetzung** entscheidet, ob ein Material ein Metall, ein Halbleiter oder
ein Isolator ist. Das ist das Thema des nächsten Artikels.
