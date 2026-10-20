---
title: Die Grundgleichungen des Halbleiters
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Halbleiter und Ladungstransport
order: 4050500
summary: Das Zusammenschalten aller Transport-Ergebnisse zu einem Satz gekoppelter Gleichungen, mit dem sich jedes Bauelement berechnen lässt. Die Kontinuitätsgleichung sorgt für Ladungserhaltung, die Drift-Diffusions-Gleichung liefert die Ströme, und die Poisson-Gleichung koppelt das Potential an alle Ladungen. Nur gemeinsam und selbstkonsistent gelöst, bilden sie das Fundament jeder Bauelementsimulation.
tags: Kontinuitätsgleichung, Drift-Diffusion, Poisson-Gleichung, Rekombination, Shockley-Read-Hall, Bauelementsimulation, selbstkonsistent
---

:::grafik
Einstiegs-Animation: Ein geschlossener Kreislauf aus drei Kästen. (1) Die Ladungsträger $n, p$ speisen die
__Poisson-Gleichung__, die daraus Potential $\varphi$ und Feld $E$ berechnet. (2) Feld und Dichtegefälle gehen in
die __Drift-Diffusions-Gleichung__, die die Ströme $J_n, J_p$ liefert. (3) Die Ströme plus Generation/Rekombination
gehen in die __Kontinuitätsgleichung__, die wiederum $n, p$ aktualisiert — zurück zu (1). Der Kreis dreht sich,
bis sich alles „einpendelt". Kernbotschaft: Drei gekoppelte Gleichungen, gemeinsam gelöst, beschreiben jedes
Halbleiter-Bauelement.
:::

:::konzept
Wir haben jetzt alle Bausteine beisammen: Ladungsträgerdichte, Drift, Diffusion, Beweglichkeit, Rekombination.
Dieser letzte Artikel des Oberthemas **schaltet sie zusammen** zu dem Satz von Gleichungen, mit dem Ingenieure
tatsächlich rechnen — in jedem Bauelementsimulator (TCAD) stecken genau diese Gleichungen. Drei Stück sind es:
die __Kontinuitätsgleichung__ (Ladungserhaltung), die __Drift-Diffusions-Gleichung__ (die Ströme) und die
__Poisson-Gleichung__ (das Potential). Der Clou ist, dass sie **gekoppelt** sind und nur **gemeinsam,
selbstkonsistent** gelöst werden können. Damit ist das theoretische Fundament gelegt, auf dem im nächsten
Oberthema Diode und Transistor stehen.
:::

**Worum es geht:** Wir stellen die drei __Grundgleichungen__ vor, verstehen jede einzeln (Erhaltung, Ströme,
Potential), sehen *warum* sie selbstkonsistent gekoppelt sind, und ordnen sie in die Hierarchie der
Beschreibungsebenen ein.

## Kontinuität: Ladung geht nicht verloren

Die __Kontinuitätsgleichung__ ist die Buchführung über die Ladungsträger: Die Dichte an einem Ort ändert sich
durch **Zu-/Abfluss** (Divergenz des Stroms) plus **Erzeugung** $G$ minus **Vernichtung** $R$:

$$\frac{\partial n}{\partial t} = \frac{1}{e}\,\nabla\!\cdot\!\vec J_n + G_n - R_n, \qquad \frac{\partial p}{\partial t} = -\frac{1}{e}\,\nabla\!\cdot\!\vec J_p + G_p - R_p.$$

- __$\nabla\cdot\vec J$__: der **Netto-Abfluss** pro Volumen; fließt mehr Strom hinein als hinaus, steigt die
  Dichte.
- __$G$__: __Generation__ (z. B. ein Lichtquant erzeugt ein Elektron-Loch-Paar).
- __$R$__: __Rekombination__ (ein Elektron füllt ein Loch, beide verschwinden).
- Das unterschiedliche Vorzeichen bei $\vec J_p$ rührt von der positiven Ladung der Löcher.

:::grafik
Ein kleines Volumen mit einem Strompfeil hinein und einem (kleineren) hinaus; die Differenz füllt es. Zusätzlich
ein „$+G$"-Pfeil (Paarerzeugung) und ein „$-R$"-Pfeil (Rekombination). Beschriftung „Dichteänderung = Zufluss +
Generation − Rekombination".
:::

**Die drei Rekombinationswege.** Wenn ein Elektron ins Leitungsband-Loch zurückfällt, muss es die Energie $E_g$
irgendwie abgeben — auf drei Arten:

- **strahlend** (ein Photon $h\nu \approx E_g$) — die Grundlage der __LED__ und des Lasers (effizient bei
  direkter Lücke, vgl. GaAs),
- **über Phononen** (die Energie wird als Wärme ans Gitter abgegeben),
- über **tiefe Störstellen** (der __Shockley-Read-Hall__-Mechanismus: ein Fallenzustand nahe der Bandmitte fängt
  erst das Elektron, dann das Loch).

:::grafik
Bänderschema mit drei Rekombinations-Pfeilen von Leitungs- zu Valenzband: (1) strahlend (Wellenlinie Photon,
„LED"), (2) über Phononen (Zickzack, „Wärme"), (3) zweistufig über ein Fallenniveau in Bandmitte („SRH").
:::

## Drift-Diffusion: die Ströme

Die __Drift-Diffusions-Gleichung__ fasst die beiden Transportarten der vorigen Artikel zusammen — Drift (durch
das Feld $E$) plus Diffusion (durch das Dichtegefälle), für Elektronen und Löcher getrennt:

$$\vec J_n = e\,n\,\mu_n\,\vec E + e\,D_n\,\nabla n, \qquad \vec J_p = e\,p\,\mu_p\,\vec E - e\,D_p\,\nabla p.$$

- Erster Term: __Drift__ ($\propto$ Feld und Ladungsträgerzahl).
- Zweiter Term: __Diffusion__ ($\propto$ Konzentrationsgefälle), mit $D=\tfrac{k_BT}{e}\mu$ (Einstein).
- Das **Minus** beim Löcher-Diffusionsterm kommt daher, dass Löcher **positiv** geladen sind: Ihr Teilchenfluss
  läuft wie bei Elektronen bergab, aber ihr Ladungsstrom hat das umgekehrte Vorzeichen.

:::grafik
Für Elektronen: ein Driftpfeil (Feld $E$ eingezeichnet) und ein Diffusionspfeil (Dichtegefälle $\nabla n$), die
sich zum Gesamtstrom $\vec J_n$ addieren. Daneben dasselbe für Löcher mit umgedrehtem Diffusionsvorzeichen.
:::

## Poisson: das Potential aus allen Ladungen

Die bisherigen Gleichungen brauchen das Feld $E=-\nabla\varphi$ — aber woher kommt es? Es wird von den Ladungen
**selbst** erzeugt. Das beschreibt die __Poisson-Gleichung__, die das elektrostatische Potential $\varphi$ an
**alle** Ladungen koppelt — die beweglichen ($n, p$) und die ortsfesten ionisierten Dotieratome
($N_a^-, N_d^+$):

$$\Delta\varphi = -\frac{e}{\varepsilon_0\varepsilon_r}\big(p - n + N_d^+ - N_a^-\big).$$

- __$p - n + N_d^+ - N_a^-$__: die **gesamte Raumladungsdichte** (geteilt durch $e$). In einem neutralen Gebiet
  ist sie null; an Grenzflächen (etwa im pn-Übergang) nicht — dort entsteht ein Feld.
- __$\varepsilon_r$__: die Dielektrizitätszahl des Halbleiters.

:::grafik
Ein Ladungsprofil (ortsfeste Dotier-Ionen plus bewegliche $n, p$) als Raumladung; darunter das daraus über die
Poisson-Gleichung berechnete Potential $\varphi(x)$ und das Feld $E=-d\varphi/dx$. Pfeil „Ladungen erzeugen ihr
eigenes Feld".
:::

## Warum selbstkonsistent?

Jetzt sieht man die Kopplung: Die Ladungsträger $n, p$ stehen in **Poisson** und bestimmen das Potential; das
Potential liefert das Feld $E$, das in die **Drift-Diffusion** eingeht und die Ströme bestimmt; die Ströme gehen
in die **Kontinuität** ein und ändern wieder $n, p$. Keine Gleichung steht für sich — man muss alle drei
**gleichzeitig** lösen, bis sich ein widerspruchsfreier (selbstkonsistenter) Zustand einstellt. Genau das tut ein
Bauelementsimulator: Er iteriert diesen Kreislauf, bis er sich nicht mehr ändert.

**Warum nicht einfach nacheinander lösen?** Weil die Größen sich gegenseitig bedingen: Ändert man $n$, ändert
sich $\varphi$, dadurch $E$, dadurch der Strom, dadurch wieder $n$. Nur die gemeinsame Lösung ist konsistent — ein
nacheinander „durchgerechnetes" Ergebnis würde sich selbst widersprechen.

:::grafik
Der geschlossene Dreier-Kreislauf noch einmal als Schema: Poisson ($n,p\to\varphi$) → Drift-Diffusion
($\varphi,E\to J$) → Kontinuität ($J,G,R\to n,p$) → zurück zu Poisson; ein „Iteration bis konvergiert"-Symbol in
der Mitte.
:::

## Die Hierarchie der Beschreibungsebenen

Die Drift-Diffusions-Gleichungen sind die **gröbste**, makroskopische Ebene. Sie entstehen aus der feineren
__Boltzmann-Transportgleichung__ (semiklassisch) durch Mittelung über die $k$-Zustände, und diese wiederum ist
eine Näherung der vollen quantenmechanischen Beschreibung über __Nicht-Gleichgewichts-Greensfunktionen__:

$$\underbrace{\text{Drift-Diffusion / Kontinuität}}_{\text{makroskopisch}} \;\xleftarrow{\ \text{mitteln}\ }\; \underbrace{\text{Boltzmann-Transport}}_{\text{semiklassisch}} \;\xleftarrow{}\; \underbrace{\text{Greensfunktion } G^r}_{\text{quantenmechanisch}}.$$

Je feiner die Ebene, desto genauer (und aufwändiger). Für die meisten Bauelemente genügt die Drift-Diffusion; nur
bei sehr kleinen, quantenmechanisch dominierten Strukturen (etwa Tunnel-Bauelementen) braucht man die tieferen
Ebenen.

:::grafik
Drei gestapelte Ebenen (Pyramide): unten breit „Drift-Diffusion (makroskopisch, einfach)", darüber
„Boltzmann (semiklassisch)", oben schmal „Greensfunktion (quantenmechanisch, exakt)"; ein Pfeil „gröber ↓ /
genauer ↑".
:::

:::kern
Die drei __Grundgleichungen__ beschreiben jedes Halbleiter-Bauelement. **Kontinuität** (Ladungserhaltung):
$\partial_t n=\tfrac1e\nabla\!\cdot\!\vec J_n+G_n-R_n$, $\partial_t p=-\tfrac1e\nabla\!\cdot\!\vec J_p+G_p-R_p$;
Rekombination $R$ über drei Wege (strahlend→LED, Phononen→Wärme, tiefe Störstellen→Shockley-Read-Hall).
**Drift-Diffusion** (Ströme): $\vec J_n=en\mu_n\vec E+eD_n\nabla n$, $\vec J_p=ep\mu_p\vec E-eD_p\nabla p$
(Minus wegen +Ladung der Löcher), $D=\tfrac{k_BT}{e}\mu$. **Poisson** (Potential aus allen Ladungen):
$\Delta\varphi=-\tfrac{e}{\varepsilon_0\varepsilon_r}(p-n+N_d^+-N_a^-)$. Die drei sind **gekoppelt** und werden
**selbstkonsistent** gelöst (Fundament jeder Bauelementsimulation). Hierarchie: Drift-Diffusion (makroskopisch) ←
Boltzmann (semiklassisch) ← Greensfunktion (quantenmechanisch).
:::

Damit ist das Oberthema **Halbleiter und Ladungstransport** komplett — und zugleich die gesamte Theorie
beisammen: von der Quantenmechanik über Kristall, Bänder und Statistik bis zu den Transportgleichungen. Im
**letzten** Oberthema wenden wir all das an und bauen die eigentlichen __Bauelemente__: den pn-Übergang, die
Diode und den Transistor.

:::quiz
F: Was drückt die Kontinuitätsgleichung physikalisch aus?
A: Die Erhaltung der Ladungsträger: Die Dichte an einem Ort ändert sich nur durch Netto-Zufluss (Divergenz des Stroms) plus Generation minus Rekombination. Ladung entsteht oder verschwindet nicht einfach, sie wird lückenlos bilanziert.
F: Warum steht in den Kontinuitätsgleichungen für $n$ und $p$ ein unterschiedliches Vorzeichen vor $\nabla\!\cdot\!\vec J$?
A: Der Strom $\vec J$ ist als Fluss *positiver* Ladung definiert. Weil Elektronen negativ sind, bedeutet ein auswärtsgerichteter Elektronenstrom einen Zuwachs an Elektronendichte — daher das umgekehrte Vorzeichen gegenüber den positiven Löchern.
F: Was muss bei jeder Rekombination mit der Energie $E_g$ geschehen, und welche Wege gibt es?
A: Das zurückfallende Elektron muss die Bandlückenenergie abgeben — strahlend als Photon (Basis der LED), über Phononen als Wärme ans Gitter, oder zweistufig über eine tiefe Störstelle (Shockley-Read-Hall). Der Weg hängt stark von Material und Defekten ab.
F: Warum ist strahlende Rekombination bei direkter Bandlücke (GaAs) effizient, bei Silizium aber nicht?
A: Bei direkter Lücke liegen Leitungsband-Minimum und Valenzband-Maximum beim selben $k$, sodass das Elektron ohne Impulsänderung ein Photon abgeben kann. Bei Silizium (indirekt) wäre zusätzlich ein Phonon nötig — dieser Dreierprozess ist unwahrscheinlich, deshalb dominiert dort nichtstrahlende Rekombination.
F: Woraus setzt sich der Strom in der Drift-Diffusions-Gleichung zusammen?
A: Aus zwei Beiträgen: dem Drift, proportional zum Feld und zur Ladungsträgerzahl, und der Diffusion, proportional zum Konzentrationsgefälle (mit $D=\tfrac{k_BT}{e}\mu$). Beide Triebkräfte wirken gleichzeitig und addieren sich zum Gesamtstrom.
F: Warum hat der Diffusionsterm bei Löchern ein Minuszeichen, bei Elektronen nicht?
A: Der Teilchenfluss läuft bei beiden bergab (von hoher zu niedriger Dichte). Weil Löcher aber positiv geladen sind, zeigt ihr *Ladungsstrom* in dieselbe Richtung wie der Teilchenfluss — bei den negativen Elektronen dreht sich das Vorzeichen um.
F: Welche Ladungen koppelt die Poisson-Gleichung an das Potential?
A: Alle: die beweglichen Elektronen und Löcher ($n,p$) *und* die ortsfesten ionisierten Dotieratome ($N_d^+,N_a^-$). Ihre Summe ist die Raumladungsdichte, die das Potential und damit das Feld erzeugt.
F: Warum verschwindet das Feld in einem neutralen Gebiet, nicht aber an einer Grenzfläche?
A: Im neutralen Inneren heben sich bewegliche und ortsfeste Ladungen auf, die Raumladung ist null und die Poisson-Gleichung liefert kein Feld. An Grenzflächen wie dem pn-Übergang bleibt eine Nettoraumladung übrig, aus der ein Feld entsteht.
F: Warum müssen die drei Grundgleichungen selbstkonsistent gelöst werden?
A: Sie bedingen sich gegenseitig im Kreis: $n,p$ bestimmen über Poisson das Potential, das Feld bestimmt über Drift-Diffusion die Ströme, die Ströme ändern über Kontinuität wieder $n,p$. Nur die gleichzeitige Lösung ist widerspruchsfrei — nacheinander gerechnet würde sich das Ergebnis selbst widersprechen.
F: Wie ordnen sich Drift-Diffusion, Boltzmann-Transport und Greensfunktion in eine Hierarchie ein?
A: Drift-Diffusion ist die gröbste, makroskopische Ebene, sie folgt durch Mittelung aus der semiklassischen Boltzmann-Gleichung, die wiederum eine Näherung der quantenmechanischen Greensfunktionen ist. Feiner heißt genauer, aber aufwändiger; für kleine, quantendominierte Strukturen braucht man die tieferen Ebenen.
:::
