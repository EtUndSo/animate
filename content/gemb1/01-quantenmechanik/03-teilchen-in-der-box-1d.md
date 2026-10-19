---
title: Teilchen in der Box (1D)
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010300
summary: Der einfachste Fall von Quantisierung, komplett durchgerechnet – ein Elektron zwischen zwei undurchdringlichen Wänden. Aus den Randbedingungen folgen stehende Wellen, daraus die diskreten Energien $E_n = n^2 h^2/(8mL^2)$, eine unvermeidbare Nullpunktsenergie und Aufenthaltswahrscheinlichkeiten mit Knoten.
tags: Potentialkasten, Teilchen in der Box, Randbedingungen, stehende Wellen, Quantisierung, Nullpunktsenergie, Normierung, Quantenpunkt
---

:::grafik
Einstiegs-Animation: Ein Kasten der Breite $L$ mit zwei senkrechten, unendlich hohen „Wänden". Darin erscheinen
nacheinander die erlaubten Elektronen-Zustände als stehende Wellen: $\psi_1$ (eine Halbwelle), $\psi_2$ (eine
ganze Welle), $\psi_3$ (anderthalb Wellen) … — jede genau null an beiden Wänden, wie eine eingespannte Saite.
Rechts daneben wächst eine **Energieleiter** mit: $E_1, E_2, E_3, \ldots$, deren Abstände immer größer werden.
Kernbotschaft: Einsperren erlaubt nur bestimmte Wellen — und damit nur bestimmte, diskrete Energien.
:::

:::konzept
Im Einführungsartikel war die Gitarrensaite nur ein Bild. Jetzt machen wir daraus eine **exakte Rechnung**. Der
einfachste denkbare Fall, in dem ein Elektron eingesperrt ist, ist ein Elektron zwischen zwei undurchdringlichen
Wänden — der **unendlich hohe Potentialkasten**. An ihm sieht man in Reinform, wie aus dem Wellencharakter die
**Quantisierung** entsteht: Nur Wellen, die „ganzzahlig in den Kasten passen", sind erlaubt, und jede gehört zu
einer festen Energie. Das Ergebnis — diskrete Energiestufen — ist das Fundament für Atome, Quantenpunkte und
die Energiebänder im Kristall.
:::

**Worum es geht:** Wir wenden die stationäre Schrödinger-Gleichung (voriger Abschnitt) auf den einfachsten
eingesperrten Fall an und leiten Schritt für Schritt die erlaubten __Wellenfunktionen__ und __Energien__ her.
Dabei klären wir, *warum* die Energie nicht null werden kann und *warum* das Elektron sich nicht überall gleich
oft aufhält.

## Das Modell: der unendlich hohe Potentialkasten

Wir idealisieren die „zwei Wände" als ein Potential, das innen null und außen unendlich hoch ist:

$$V(x) = \begin{cases} 0, & 0 < x < L \quad(\text{innerhalb des Kastens}),\\[2pt] \infty, & x \le 0 \text{ oder } x \ge L \quad(\text{außerhalb}). \end{cases}$$

- __$L$__: die __Breite__ des Kastens.
- __$V(x)$__: das __Potential__ — innen frei beweglich, außen eine unüberwindbare Energiemauer.

Die unendlich hohen Wände sind eine Idealisierung, machen die Rechnung aber besonders klar: Das Elektron kann
den Kasten **nicht** verlassen. (Den realistischeren Fall endlich hoher Wände — bei dem die Welle ein Stück in
die Wand „hineinleckt" — behandeln wir in einem späteren Abschnitt.)

## Die Randbedingungen: warum ψ an den Wänden null ist

Hier liegt der Schlüssel zur ganzen Quantisierung. Außerhalb des Kastens ist die potentielle Energie unendlich —
dort kann sich das Elektron nicht aufhalten, also ist die Wellenfunktion dort **null**: $\psi(x) = 0$ für
$x \le 0$ und $x \ge L$. Weil die Wellenfunktion außerdem **stetig** sein muss (sie kann nicht springen), muss
sie an den Wänden stetig an diese Null anschließen:

$$\psi(0) = 0 \qquad\text{und}\qquad \psi(L) = 0.$$

Diese beiden __Randbedingungen__ sind genau die „festen Enden" der eingespannten Saite. Sie werden gleich dafür
sorgen, dass nur bestimmte Wellen überleben.

:::grafik
Der Potentialkasten $V(x)$: zwei senkrechte Wände bei $x=0$ und $x=L$, dazwischen $V=0$. Eingezeichnet, dass
$\psi$ außerhalb null ist und an beiden Wänden stetig auf null trifft ($\psi(0)=\psi(L)=0$). Ein durchgestrichenes
Beispiel zeigt eine Welle, die an der Wand nicht null ist — „verboten".
:::

## Die Schrödinger-Gleichung im Kasten lösen

**Schritt 1** — die Gleichung innen aufstellen. Innerhalb ist $V = 0$, also lautet die stationäre
Schrödinger-Gleichung $-\tfrac{\hbar^2}{2m}\psi'' = E\psi$, umgestellt

$$\psi''(x) = -k^2\,\psi(x), \qquad k = \frac{\sqrt{2mE}}{\hbar}.$$

**Schritt 2** — die allgemeine Lösung hinschreiben. Das ist die bekannte Schwingungsgleichung mit der Lösung

$$\psi(x) = A\sin(kx) + B\cos(kx).$$

**Schritt 3** — die Randbedingungen anwenden. Aus $\psi(0) = 0$ folgt (weil $\cos 0 = 1$ und $\sin 0 = 0$)
sofort $B = 0$; es bleibt $\psi(x) = A\sin(kx)$. Die zweite Bedingung $\psi(L) = 0$ verlangt dann

$$A\sin(kL) = 0.$$

$A = 0$ wäre die „leere" Lösung (gar kein Elektron) und scheidet aus. Also muss der **Sinus** null sein, und das
ist nur für bestimmte Argumente der Fall: $\sin(kL) = 0 \Rightarrow kL = n\pi$ mit einer ganzen Zahl $n$. Damit
sind nur die __diskreten Wellenzahlen__

$$k_n = \frac{n\pi}{L}, \qquad n = 1, 2, 3, \ldots$$

erlaubt. Genau das ist die Quantisierung: Nicht jede Welle passt, sondern nur die, bei denen ein ganzzahliges
Vielfaches von Halbwellen in den Kasten passt (das entspricht $\lambda_n = 2L/n$ — die Gitarrensaiten-Bedingung,
jetzt exakt). Der Fall $n=0$ gibt $\psi \equiv 0$ (kein Elektron) und ist ausgeschlossen; negative $n$ liefern
dieselben Zustände.

:::grafik
Die ersten erlaubten stehenden Wellen im Kasten übereinander: $\psi_1$ (eine Halbwelle), $\psi_2$ (zwei),
$\psi_3$ (drei), jeweils null an beiden Wänden. Daneben zur Einordnung die eingespannte Gitarrensaite mit
denselben Mustern und die Bedingung $\lambda_n = 2L/n$ bzw. $k_n = n\pi/L$.
:::

## Die erlaubten Energien

Zu jeder erlaubten Wellenzahl $k_n$ gehört über $E = \hbar^2 k^2/2m$ eine feste Energie. Einsetzen von
$k_n = n\pi/L$ liefert das zentrale Ergebnis:

$$E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{\hbar^2 \pi^2 n^2}{2mL^2} = \frac{n^2 h^2}{8 m L^2}, \qquad n = 1, 2, 3, \ldots$$

- __$E_n$__: die erlaubten __Energieeigenwerte__ (die „Sprossen" der Energieleiter).
- __$n$__: die __Quantenzahl__ ($n = 1, 2, 3, \ldots$).
- __$m$__: die __Masse__ des Elektrons, __$L$__ die __Kastenbreite__, __$h$__ das Plancksche Wirkungsquantum.

Drei Aussagen stecken darin:

- **Die Energie ist diskret** — nur die Werte $E_1, E_2, \ldots$ sind erlaubt, dazwischen nichts. Das ist die
  Erklärung für die scharfen Spektrallinien aus dem Einführungsartikel.
- **Sie wächst mit $n^2$** — die Abstände zwischen den Stufen werden nach oben immer größer.
- **Sie hängt mit $1/L^2$ von der Kastenbreite ab** — und das ist technisch enorm wichtig: Macht man den Kasten
  **kleiner**, steigen alle Energien stark an. Genau das nutzt man bei __Quantenpunkten__ — winzigen
  Halbleiterkristallen, deren „Leuchtfarbe" sich allein über ihre **Größe** einstellen lässt, weil die
  Energieabstände von $L$ abhängen.

:::grafik
Eine Energieleiter mit den Niveaus $E_1, E_2, E_3, E_4$ im Verhältnis $1 : 4 : 9 : 16$ (Abstände wachsen).
Daneben zwei Kästen unterschiedlicher Breite $L$: Im schmaleren Kasten liegen dieselben Niveaus deutlich höher
und weiter auseinander — mit dem Hinweis „kleiner Kasten → höhere Energien (Quantenpunkt-Farbe über die Größe)".
:::

## Die Nullpunktsenergie: warum das Elektron nie ganz ruht

Ein überraschender Punkt: Die niedrigste erlaubte Energie ist **nicht** null, sondern

$$E_1 = \frac{h^2}{8 m L^2} > 0.$$

Das nennt man die __Nullpunktsenergie__. **Warum kann das Elektron nicht einfach bei $E = 0$ ruhig im Kasten
liegen?** Klassisch wäre das selbstverständlich — eine Kugel darf ruhig an einer Stelle liegen bleiben.
Quantenmechanisch ist es verboten, und zwar aus zwei zusammenhängenden Gründen:

- Ein Zustand mit $E = 0$ hätte $k = 0$, also $\psi = A\sin(0) = 0$ überall — das wäre **kein** Elektron. Die
  kleinste Welle, die in den Kasten passt und an den Wänden null wird, ist bereits eine halbe Wellenlänge ($n=1$)
  — und die hat eine von null verschiedene Krümmung, also kinetische Energie.
- Anschaulich über die **Unschärferelation**: Das Elektron ist auf den Bereich $\Delta x \sim L$ eingesperrt.
  Dann kann sein Impuls nicht exakt null sein ($\Delta p \gtrsim \hbar/L$), und ein unvermeidbarer Impuls
  bedeutet unvermeidbare Bewegungsenergie. Je enger der Kasten, desto größer diese Mindestenergie — konsistent
  mit dem $1/L^2$ in der Formel.

Einsperren kostet also immer eine Mindest-Bewegungsenergie. Ein eingesperrtes Quantenteilchen „zappelt" selbst
bei tiefster Temperatur noch.

## Normierung und die Aufenthaltswahrscheinlichkeit

Zuletzt legen wir die Vorfaktoren fest. Die __Normierung__ verlangt, dass das Elektron mit Sicherheit
**irgendwo** im Kasten ist, $\int_0^L |\psi|^2\,\mathrm{d}x = 1$. Das Integral über $\sin^2$ ergibt $L/2$, also
$A^2\cdot L/2 = 1$ und damit $A = \sqrt{2/L}$. Die normierten __Eigenfunktionen__ sind

$$\psi_n(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{n\pi x}{L}\right).$$

Interessant ist ihr Betragsquadrat $|\psi_n|^2$, die Aufenthaltswahrscheinlichkeit. **Hier zeigt sich ein klarer
Unterschied zur klassischen Vorstellung:** Klassisch wäre das Elektron im Kasten überall gleich wahrscheinlich
anzutreffen (es prallt gleichmäßig hin und her). Quantenmechanisch hat $|\psi_n|^2$ aber **Berge und Täler** — im
Zustand $n$ gibt es $n$ Stellen hoher Wahrscheinlichkeit und dazwischen __Knoten__, an denen das Elektron **nie**
angetroffen wird. Erst für sehr große $n$ verwischen die Zacken zur gleichmäßigen klassischen Verteilung (ein
Beispiel dafür, wie die klassische Physik als Grenzfall großer Quantenzahlen wieder auftaucht).

:::grafik
Für $n = 1, 2, 3$ jeweils übereinander die Wellenfunktion $\psi_n(x)$ und darunter ihr Betragsquadrat
$|\psi_n|^2$ als Wahrscheinlichkeitsdichte, mit markierten Knoten (Nullstellen von $|\psi_n|^2$). Gestrichelt zum
Vergleich die klassische Gleichverteilung (konstante Linie). Hinweis: Fläche unter jedem $|\psi_n|^2$ ist 1
(Normierung $A=\sqrt{2/L}$).
:::

:::kern
Im __unendlich hohen Potentialkasten__ ($V=0$ innen, $\infty$ außen) erzwingen die __Randbedingungen__
$\psi(0)=\psi(L)=0$, dass nur stehende Wellen passen: $\psi_n(x) = \sqrt{2/L}\,\sin(n\pi x/L)$ mit den diskreten
Wellenzahlen $k_n = n\pi/L$. Daraus folgen die __diskreten Energien__ $E_n = \dfrac{n^2 h^2}{8mL^2}$
($n=1,2,3,\ldots$): quadratisch in $n$, und $\propto 1/L^2$ (Grundlage der größenabhängigen __Quantenpunkt__-Farbe).
Die tiefste Energie ist die __Nullpunktsenergie__ $E_1 = h^2/(8mL^2) > 0$ — Einsperren erzwingt eine
Mindest-Bewegungsenergie (Unschärfe). Die Aufenthaltswahrscheinlichkeit $|\psi_n|^2$ hat $n$ Berge und dazwischen
__Knoten__ (nicht gleichverteilt wie klassisch).
:::

Dasselbe Prinzip lässt sich auf zwei und drei Raumrichtungen übertragen. Sperrt man das Elektron in einer, zwei
oder drei Richtungen ein, entstehen __Quantenfilme__, __Quantendrähte__ und __Quantenpunkte__ — das Thema der
nächsten Abschnitte, mit wichtigen Folgen für die Zustandsdichte.
