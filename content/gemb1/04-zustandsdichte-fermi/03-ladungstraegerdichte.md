---
title: Ladungsträgerdichte – Elektronen und Löcher
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Zustandsdichte und Fermi-Verteilung
order: 4040300
summary: Der Zusammenbau beider Bausteine zur gesuchten Zahl – wie viele bewegliche Ladungsträger ein Halbleiter enthält. Aus $n=\int D(E)f(E)\,dE$ wird mit der Boltzmann-Näherung die einfache Form $n=N_L\,e^{-(E_L-E_f)/k_BT}$, analog $p=N_V\,e^{-(E_f-E_V)/k_BT}$ für die Löcher. Multipliziert man beide, fällt das Fermi-Niveau heraus – das Massenwirkungsgesetz $n\cdot p=n_i^2$.
tags: Ladungsträgerdichte, Elektronen, Löcher, effektive Zustandsdichte, Massenwirkungsgesetz, intrinsische Dichte, Boltzmann-Näherung
---

:::grafik
Einstiegs-Animation: Drei übereinanderliegende Diagramme mit gemeinsamer Energieachse. Oben die Zustandsdichte
$D(E)$ (Wurzelkurven, die von $E_L$ nach oben und von $E_V$ nach unten auffächern). In der Mitte die
Fermi-Funktion $f(E)$ (weiche Stufe mit $E_f$ in der Lücke). Unten ihr **Produkt** $D(E)\,f(E)$ — ein kleiner
Buckel knapp oberhalb $E_L$: die tatsächlich besetzten Leitungsband-Zustände (die Elektronen). Spiegelbildlich am
Valenzband der Buckel der leeren Zustände (die Löcher). Die schraffierten Flächen sind $n$ und $p$.
Kernbotschaft: Ladungsträgerdichte = „Plätze" mal „Besetzung", über die Energie aufsummiert.
:::

:::konzept
Jetzt fügen wir die beiden Bausteine zusammen. Die __Zustandsdichte__ $D(E)$ sagt, **wo** Plätze sind; die
__Fermi-Verteilung__ $f(E)$, **welche** besetzt sind. Ihr Produkt, über alle Energien integriert, ergibt die
gesuchte __Ladungsträgerdichte__ — und die bestimmt am Ende Leitfähigkeit, Diodenkennlinie und Transistorstrom.
Im Halbleiter gibt es dabei **zwei** Sorten beweglicher Ladung: Elektronen im Leitungsband und __Löcher__ im
Valenzband. Das Ergebnis dieses Artikels, das __Massenwirkungsgesetz__, ist zugleich der Startpunkt für das
nächste Oberthema (Dotierung).
:::

**Worum es geht:** Wir berechnen aus $n=\int D\,f\,dE$ die Elektronendichte, führen das __Loch__ sauber ein,
leiten die einfachen Formeln mit der __effektiven Zustandsdichte__ $N_L, N_V$ her und gewinnen daraus das
__Massenwirkungsgesetz__ und die intrinsische Dichte $n_i$.

## Die Masterformel und die zwei Ladungsträger

Die Zahl der Elektronen pro Volumen im Leitungsband ist das Integral über „Plätze mal Besetzung":

$$n = \int_{E_L}^{\infty} D_L(E)\,f(E)\,dE.$$

Analog gibt es im Valenzband __Löcher__ — fehlende Elektronen in einem sonst vollen Band. Ihre Dichte ist das
Integral über „Plätze mal Leer-Wahrscheinlichkeit" $1-f(E)$:

$$p = \int_{-\infty}^{E_V} D_V(E)\,\big(1-f(E)\big)\,dE.$$

**Warum beide Sorten?** Bei $T>0$ wird gelegentlich ein Elektron aus dem vollen Valenzband über die Lücke ins
Leitungsband angeregt. Es hinterlässt oben ein bewegliches Elektron **und** unten eine Lücke — beide tragen zum
Strom bei.

:::grafik
Bänderschema mit einem Pfeil, der ein Elektron von der Valenzbandkante über die Lücke ins Leitungsband hebt; oben
bleibt ein Elektron (−), unten eine Leerstelle (+). Daneben die zwei Integrale $n$ (über $f$) und $p$ (über
$1-f$).
:::

## Das Loch: die wandernde Leerstelle

Ein __Loch__ ist ein fehlendes Elektron in einem sonst voll besetzten Valenzband; es verhält sich wie ein Teilchen
mit **positiver** Ladung $+e$ und positiver effektiver Masse.

**Das Parkplatz-Bild:** Ein randvoll belegter Parkplatz (Autos = Elektronen) erzeugt keinen Verkehr — nichts kann
sich bewegen. Fehlt **ein** Auto, kann das Nachbarauto nachrücken; dann ist an dessen Stelle die Lücke. Effektiv
**wandert die Lücke** in Gegenrichtung zu den Autos. Statt $10^{23}$ Elektronen zu verfolgen, beschreibt man
bequem die **eine** Lücke. Da das fehlende Objekt negativ geladen ist, trägt sich die Lücke wie eine **positive**
Ladung.

Rechnerisch ist die Leer-Wahrscheinlichkeit $1-f(E)$, und sie lässt sich in dieselbe Gestalt wie $f$ bringen:

$$1 - f(E) = \frac{\exp\!\big(\tfrac{E-E_f}{k_BT}\big)}{1+\exp\!\big(\tfrac{E-E_f}{k_BT}\big)} = \frac{1}{\exp\!\big(\tfrac{E_f-E}{k_BT}\big)+1} \equiv f_h(E).$$

Diese „Loch-Fermi-Funktion" $f_h$ hat **dieselbe Form** wie $f$, nur mit umgedrehtem Vorzeichen im Exponenten.
Löcher „sehen" die Energieachse gespiegelt — sie sammeln sich an der **oberen** Valenzbandkante, Elektronen an der
**unteren** Leitungsbandkante.

:::grafik
Oben voll belegter Parkplatz = kein Verkehr; darunter eine Lücke, in die Autos nacheinander nachrücken, sodass die
Lücke nach links wandert (Autos nach rechts). Rechts die gespiegelten Kurven $f(E)$ (Elektronen) und $f_h(E)$
(Löcher) um $E_f$.
:::

## Herleitung der Elektronendichte

Wir setzen $D_L(E)=\tfrac{4\pi(2m_L^\star)^{3/2}}{h^3}\sqrt{E-E_L}$ und $f(E)$ ein. Weil im Leitungsband
$E\ge E_L > E_f$ gilt (also $E-E_f\gg k_BT$), dürfen wir die __Boltzmann-Näherung__
$f(E)\approx e^{-(E-E_f)/k_BT}$ verwenden:

$$n \approx \frac{4\pi(2m_L^\star)^{3/2}}{h^3}\int_{E_L}^{\infty}\sqrt{E-E_L}\;\exp\!\left(-\frac{E-E_f}{k_BT}\right)dE.$$

Mit der Substitution $x=\tfrac{E-E_L}{k_BT}$ (also $dE=k_BT\,dx$) spaltet sich der konstante Teil des Exponenten
als Vorfaktor ab, und das Restintegral ist ein reiner Zahlenwert — die Gamma-Funktion
$\int_0^\infty\sqrt{x}\,e^{-x}dx=\Gamma(\tfrac32)=\tfrac{\sqrt\pi}{2}$:

$$n = \underbrace{2\left(\frac{2\pi m_L^\star k_BT}{h^2}\right)^{3/2}}_{N_L}\;\exp\!\left(-\frac{E_L-E_f}{k_BT}\right).$$

Das ist das zentrale Ergebnis:

$$n = N_L\,\exp\!\left(-\frac{E_L-E_f}{k_BT}\right), \qquad N_L = 2\left(\frac{2\pi m_L^\star k_BT}{h^2}\right)^{3/2}.$$

:::grafik
Links die zu integrierende Fläche: Produkt aus Wurzelkurve $D_L$ und abfallender Boltzmann-Kurve ergibt einen
schmalen Buckel über $E_L$ (Fläche = $n$). Rechts die Zusammenfassung: dieselbe Fläche als **ein** Ersatzzustand
$N_L$ direkt an der Kante $E_L$, besetzt mit $e^{-(E_L-E_f)/k_BT}$.
:::

## Was die effektive Zustandsdichte bedeutet

Die __effektive Zustandsdichte__ $N_L$ fasst das **gesamte** über die Energie verteilte Leitungsband zu **einem
einzigen** Ersatzzustand direkt an der Bandkante $E_L$ zusammen. Interpretation: „Es ist so, *als ob* es $N_L$
Plätze genau bei $E_L$ gäbe, die mit dem Boltzmann-Faktor besetzt werden." Das ist die enorme Vereinfachung —
statt eines Integrals nur noch ein Produkt. Der Faktor $N_L\propto T^{3/2}$ wächst mit der Temperatur, weil ein
breiteres Energiefenster thermisch zugänglich wird.

Für die **Löcher** läuft alles symmetrisch (mit $D_V$ und $1-f$), und man erhält:

$$p = N_V\,\exp\!\left(-\frac{E_f-E_V}{k_BT}\right), \qquad N_V = 2\left(\frac{2\pi m_V^\star k_BT}{h^2}\right)^{3/2}.$$

Für **Silizium** bei $300\,$K: $N_L \approx 2{,}82\times10^{19}\,\text{cm}^{-3}$ und
$N_V \approx 1{,}83\times10^{19}\,\text{cm}^{-3}$. Dass $N_L>N_V$ ist, liegt an der größeren
DOS-effektiven Masse des Leitungsbandes (sechs Täler).

| | Elektronen ($n$) | Löcher ($p$) |
|---|---|---|
| Band | Leitungsband, oberhalb $E_L$ | Valenzband, unterhalb $E_V$ |
| Zustandsdichte | $D_L\propto\sqrt{E-E_L}$ | $D_V\propto\sqrt{E_V-E}$ |
| Besetzung | $f(E)$ | $1-f(E)=f_h$ |
| sammeln sich an | Kante $E_L$ | Kante $E_V$ |
| Dichte | $N_L\,e^{-(E_L-E_f)/k_BT}$ | $N_V\,e^{-(E_f-E_V)/k_BT}$ |
| Ladung | $-e$ | $+e$ |

## Das Massenwirkungsgesetz

Jetzt der elegante Abschluss. Multipliziert man $n$ und $p$, **fällt das Fermi-Niveau heraus** (die Exponenten
addieren sich zu $-(E_L-E_V)/k_BT = -E_g/k_BT$):

$$n\cdot p = N_L N_V\,\exp\!\left(-\frac{E_g}{k_BT}\right), \qquad E_g = E_L - E_V.$$

Das ist das __Massenwirkungsgesetz__: Das **Produkt** $n\cdot p$ hängt nur von Temperatur und Bandlücke ab —
**nicht** von der Lage des Fermi-Niveaus und damit **nicht** von der Dotierung. Erhöht eine Dotierung die
Elektronenzahl, sinkt die Löcherzahl im selben Maß.

Für den **intrinsischen** (undotierten) Halbleiter gilt zusätzlich $n=p=:n_i$, woraus folgt:

$$n_i = \sqrt{N_L N_V}\,\exp\!\left(-\frac{E_g}{2k_BT}\right), \qquad n\cdot p = n_i^2.$$

Für Silizium ergibt das $n_i \approx 10^{10}\,\text{cm}^{-3}$ bei $300\,$K — winzig gegenüber den $\sim 10^{22}$
Atomen pro cm³, weshalb reines Silizium ein sehr schlechter Leiter ist. Zugleich stellt sich das Fermi-Niveau
ungefähr in **Bandlückenmitte** ein.

:::grafik
Zwei Bänderschemata: links intrinsisch (wenige Elektronen oben, gleich viele Löcher unten, $E_f$ mittig), rechts
dotiert (viele Elektronen, wenige Löcher, $E_f$ nach oben verschoben). Darunter die Waage „$n\cdot p = n_i^2 =$
const" — mehr $n$ bedeutet weniger $p$.
:::

:::kern
__Ladungsträgerdichte__ = Zustandsdichte mal Besetzung, integriert: $n=\int D_L f\,dE$,
$p=\int D_V (1-f)\,dE$. Ein __Loch__ ist ein fehlendes Elektron (Ladung $+e$); $1-f(E)=f_h$ hat dieselbe Form wie
$f$, gespiegelt. Mit der __Boltzmann-Näherung__ und $\Gamma(\tfrac32)=\tfrac{\sqrt\pi}{2}$:
$n=N_L\,e^{-(E_L-E_f)/k_BT}$, $p=N_V\,e^{-(E_f-E_V)/k_BT}$ mit der __effektiven Zustandsdichte__
$N_{C,V}=2(2\pi m^\star k_BT/h^2)^{3/2}\propto T^{3/2}$ (das ganze Band auf **einen** Ersatzzustand an der Kante).
Si (300 K): $N_L\approx2{,}82\cdot10^{19}$, $N_V\approx1{,}83\cdot10^{19}\,$cm⁻³. __Massenwirkungsgesetz__
$n\cdot p=N_L N_V\,e^{-E_g/k_BT}=n_i^2$ — **$E_f$-unabhängig**; intrinsisch $n=p=n_i=\sqrt{N_L N_V}\,e^{-E_g/2k_BT}$
($\approx10^{10}\,$cm⁻³ für Si), $E_f$ etwa in Bandlückenmitte.
:::

Damit ist die Kette aus Quantenmechanik und Statistik komplett: Wir können die Ladungsträgerdichte eines reinen
Halbleiters ausrechnen. Technisch interessant wird es aber erst, wenn man $n$ und $p$ **gezielt einstellt** — durch
__Dotierung__. Wie das geht und wie sich die Ladungsträger dann im Feld bewegen (Drift und Diffusion), ist das
Thema des nächsten Oberthemas: __Halbleiter und Ladungstransport__.

:::quiz
F: Warum ist die Ladungsträgerdichte ein Integral über das Produkt $D(E)\,f(E)$?
A: $D(E)$ sagt, wie viele Plätze bei einer Energie existieren, $f(E)$, mit welcher Wahrscheinlichkeit sie besetzt sind. Erst „Plätze mal Besetzung", über alle Energien aufsummiert, ergibt die tatsächliche Zahl beweglicher Elektronen.
F: Warum tragen in einem Halbleiter immer zwei Ladungssorten zum Strom bei?
A: Hebt die thermische Energie ein Elektron über die Lücke ins Leitungsband, bleibt im Valenzband eine Leerstelle zurück. Oben entsteht ein bewegliches Elektron, unten ein bewegliches Loch — beide gleichzeitig und immer paarweise.
F: Was ist ein Loch anschaulich, und warum trägt es positive Ladung?
A: Ein Loch ist ein fehlendes Elektron in einem sonst vollen Band. Wie beim randvollen Parkplatz, auf dem nur die eine Lücke Bewegung erlaubt, verfolgt man bequem die Leerstelle statt $10^{23}$ Autos; weil das fehlende Objekt negativ ist, verhält sich die Lücke wie eine positive Ladung.
F: Warum beschreibt man die Löcher über $1-f(E)$ statt über $f(E)$?
A: $f(E)$ ist die Wahrscheinlichkeit, dass ein Zustand besetzt ist; ein Loch ist aber ein *leerer* Zustand, also die Gegenwahrscheinlichkeit $1-f(E)$. Umgeformt hat diese „Loch-Fermi-Funktion" dieselbe Gestalt wie $f$, nur mit umgedrehtem Vorzeichen im Exponenten.
F: Warum darf man im Leitungsband die Boltzmann-Näherung verwenden?
A: Die Leitungsbandzustände liegen bei $E\ge E_L$, und $E_L$ liegt viele $k_BT$ oberhalb von $E_f$. Damit ist $E-E_f\gg k_BT$, der Exponentialterm dominiert, und $f(E)\approx e^{-(E-E_f)/k_BT}$ gilt mit hoher Genauigkeit.
F: Was bedeutet die effektive Zustandsdichte $N_L$ anschaulich?
A: Sie fasst das gesamte, über die Energie verteilte Leitungsband zu einem einzigen Ersatzzustand genau an der Bandkante $E_L$ zusammen. Statt eines Integrals rechnet man dann nur noch mit „$N_L$ Plätzen bei $E_L$", besetzt mit dem Boltzmann-Faktor.
F: Warum wächst $N_L$ mit der Temperatur ($\propto T^{3/2}$)?
A: Je höher die Temperatur, desto breiter das thermisch zugängliche Energiefenster oberhalb der Bandkante. Mehr erreichbare Zustände bedeuten eine größere effektive Platzzahl, und die Rechnung liefert dafür die Potenz $T^{3/2}$.
F: Warum fällt beim Massenwirkungsgesetz das Fermi-Niveau heraus?
A: In $n$ steht $e^{-(E_L-E_f)/k_BT}$, in $p$ steht $e^{-(E_f-E_V)/k_BT}$. Im Produkt addieren sich die Exponenten, $+E_f$ und $-E_f$ heben sich auf, und übrig bleibt nur $-(E_L-E_V)/k_BT=-E_g/k_BT$.
F: Was folgt aus $n\cdot p=n_i^2$ für die Dotierung?
A: Das Produkt hängt nur von Temperatur und Bandlücke ab, nicht von der Lage von $E_f$. Erhöht eine Dotierung die Elektronenzahl, muss die Löcherzahl im selben Maß sinken — die beiden verhalten sich wie eine Waage mit konstantem Produkt.
F: Warum ist reines Silizium trotz $10^{22}$ Atomen/cm³ ein schlechter Leiter?
A: Weil die intrinsische Dichte $n_i\approx10^{10}\,$cm⁻³ winzig ist — nur jedes rund $10^{12}$-te Atom stellt einen beweglichen Ladungsträger. Die große Bandlücke im Exponenten $e^{-E_g/2k_BT}$ unterdrückt die thermische Paarbildung sehr stark.
:::
