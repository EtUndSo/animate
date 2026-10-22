---
title: Der pn-Übergang im Gleichgewicht
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bauelemente
order: 4060100
summary: Das Grundprinzip aller Halbleiterbauelemente – was passiert, wenn ein p- und ein n-dotiertes Gebiet aufeinandertreffen. Ladungsträger diffundieren, rekombinieren und lassen ortsfeste Ionen zurück; es entsteht eine Raumladungszone mit eingebautem Feld und einer Diffusionsspannung $V_d=\tfrac{k_BT}{e}\ln(N_AN_D/n_i^2)$. Im Gleichgewicht ist das Fermi-Niveau überall konstant.
tags: pn-Übergang, Raumladungszone, Diffusionsspannung, Verarmungszone, Schottky-Näherung, Bandverbiegung, Fermi-Niveau
---

:::grafik
Einstiegs-Animation: Zwei Blöcke rücken zusammen — links p-dotiert (viele Löcher „+", ortsfeste negative
Akzeptor-Ionen), rechts n-dotiert (viele Elektronen „−", ortsfeste positive Donator-Ionen). Am Kontakt
diffundieren Elektronen nach links und Löcher nach rechts und **rekombinieren**. Zurück bleibt beiderseits der
Grenze eine Zone aus nur noch **ortsfesten Ionen** — die __Raumladungszone__. Zwischen ihnen baut sich ein Feld
und eine Bandverbiegung auf, bis die Diffusion zum Stillstand kommt. Im Banddiagramm wird das Fermi-Niveau eine
durchgehende **waagerechte** Linie. Kernbotschaft: Aus dem Zusammentreffen zweier Dotierungen entsteht von selbst
eine Barriere — der Schalthebel aller Bauelemente.
:::

:::konzept
Dieses letzte Oberthema baut die eigentlichen __Bauelemente__: Diode, MOS-Kondensator, Transistor. Alle drei
beruhen auf **einem** Prinzip: Man bringt Materialien mit unterschiedlicher Lage des Fermi-Niveaus zusammen (oder
verbiegt die Bänder von außen); Ladungsträger fließen, bis sich ein **gemeinsames** Fermi-Niveau einstellt, und
lassen dabei **ortsfeste** ionisierte Ladungen zurück. Diese bilden eine __Raumladungszone__ und damit eine
__Bandverbiegung__ — und die ist der Schalthebel für alles Weitere. Wir fangen mit dem Grundbaustein an: dem
pn-Übergang im Gleichgewicht, also noch ohne angelegte Spannung.
:::

**Worum es geht:** Wir verstehen, *warum* am pn-Übergang eine __Raumladungszone__ entsteht, leiten die
__Diffusionsspannung__ $V_d$ her und berechnen mit der __Schottky-Näherung__ die Weite der Verarmungszone.

## Warum eine Raumladungszone entsteht

Legt man ein **p-Gebiet** (dotiert mit Akzeptoren der Dichte $N_A$, voller Löcher) an ein **n-Gebiet** (Donatoren
$N_D$, voller Elektronen), herrscht am Übergang ein gewaltiges **Konzentrationsgefälle**. Also setzt Diffusion ein:

1. Elektronen diffundieren vom n- ins p-Gebiet, Löcher umgekehrt.
2. Als **Minoritäten** auf der jeweils anderen Seite **rekombinieren** sie (ein Elektron füllt ein Loch).
3. Zurück bleiben die **ortsfesten, ionisierten Dotieratome**: im p-Gebiet die negativen $N_A^-$, im n-Gebiet die
   positiven $N_D^+$.

Diese ortsfeste Ladung ist die __Raumladungszone__ (auch __Verarmungszone__, weil sie an frei beweglichen Ladungen
verarmt ist). Sie erzeugt ein elektrisches Feld, das der Diffusion **entgegenwirkt**. Im Gleichgewicht stellt sich
ein Kräftegleichgewicht ein — die Diffusion wird vom eingebauten Feld gerade gestoppt.

:::grafik
Drei Phasen nebeneinander: (1) p und n getrennt (bewegliche Löcher/Elektronen gleichmäßig). (2) Kontakt:
Diffusionspfeile, Rekombination an der Grenze. (3) Gleichgewicht: beiderseits der Grenze nur noch ortsfeste Ionen
($N_A^-$ links, $N_D^+$ rechts), dazwischen ein Feldpfeil, der der Diffusion entgegenzeigt.
:::

## Die Gleichgewichtsbedingung: konstantes Fermi-Niveau

Im Gleichgewicht fließt **kein** Netto-Strom. Aus dem Transport-Oberthema wissen wir, dass das genau dann gilt,
wenn das (elektrochemische) __Fermi-Niveau__ überall **konstant** ist:

$$\frac{dE_f}{dx} = 0 \quad\Longleftrightarrow\quad \underbrace{\frac{d\mu}{dx}}_{\text{Diffusion}} + \underbrace{|e|\frac{d\phi}{dx}}_{\text{Feld}} = 0.$$

Der chemische „Antrieb" der Diffusion ($d\mu/dx$) wird exakt vom elektrostatischen „Gegendruck" des eingebauten
Feldes ($|e|\,d\phi/dx$) kompensiert. Im Banddiagramm heißt das: Das Fermi-Niveau ist eine durchgehende
waagerechte Linie, und **die Bänder** biegen sich, um das auszugleichen.

:::grafik
Banddiagramm des pn-Übergangs im Gleichgewicht: Leitungs- und Valenzband biegen sich vom n- (tiefer) zum
p-Gebiet (höher) nach oben, während $E_f$ als durchgehende **waagerechte** Linie eingezeichnet ist. Beschriftung
„$E_f$ konstant → kein Strom".
:::

## Die Diffusionsspannung

Wie hoch ist die Bandverbiegung? Genau so hoch wie der Unterschied der Fermi-Niveaus, den die beiden Gebiete
**vor** dem Kontakt hatten. Diese __Diffusionsspannung__ $V_d$ (engl. *built-in potential*) ist

$$V_d = \frac{k_B T}{e}\,\ln\!\left(\frac{N_A\,N_D}{n_i^2}\right),$$

mit der intrinsischen Dichte $n_i=\sqrt{N_L N_V}\,e^{-E_g/2k_BT}$ (aus dem Statistik-Oberthema).

- __$N_A, N_D$__: die Dotierdichten. Je stärker dotiert, desto **größer** $V_d$ — logisch, denn dann lagen die
  Fermi-Niveaus der beiden Gebiete weiter auseinander.
- __$n_i^2$__: über das Massenwirkungsgesetz; es macht $V_d$ stark bandlücken- und temperaturabhängig.

Die Bandverbiegung (als Energie) beträgt dann $e\,V_d$ — diese Barrierenhöhe heißt auch das __eingebaute
Potential__ $\Phi_{bi} = e\,V_d = E_f^{\,n} - E_f^{\,p}$ (in eV, gerade der ursprüngliche Fermi-Niveau-Abstand der
getrennten Gebiete). Weil $V_d$ nur **logarithmisch** von der Dotierung abhängt, liegt es für Silizium über viele
Dekaden hinweg nur bei einigen Zehntel Volt.

:::grafik
Links die zwei Gebiete vor Kontakt mit verschieden hohem $E_f^{\,n}$ (nahe $E_L$) und $E_f^{\,p}$ (nahe $E_V$).
Rechts nach Kontakt: die Bänder um $eV_d=E_f^{\,n}-E_f^{\,p}$ verbogen. Daneben die Formel $V_d=\tfrac{k_BT}{e}
\ln(N_AN_D/n_i^2)$.
:::

## Feld und Weite: die Schottky-Näherung

Um Feld und Potential auszurechnen, braucht man die genaue Form der Raumladung $\rho(x)$. Die ist am Rand der Zone
„weich" (die beweglichen Ladungen klingen über die Debye-Länge ab). Die __Schottky-Näherung__ (abrupte Näherung)
idealisiert das zu einer **kastenförmigen** Raumladung: Ein Ort ist entweder **voll verarmt** (nur ionisierte
Dotierung) oder **voll neutral**. Das macht die Poisson-Gleichung analytisch lösbar.

$$\rho(x) = \begin{cases} -e\,N_A & -x_p < x < 0 \quad(\text{p-Seite})\\ +e\,N_D & 0 < x < x_n \quad(\text{n-Seite})\\ 0 & \text{sonst (neutral)} \end{cases}$$

Zweimal Integrieren der Poisson-Gleichung $\dfrac{d^2\phi}{dx^2}=-\dfrac{\rho}{\varepsilon_0\varepsilon_r}$ liefert
**parabelförmige** Bandverläufe auf beiden Seiten, die am Übergang stetig ineinander übergehen.

:::grafik
Drei gestapelte Diagramme über $x$: (1) kastenförmige Raumladung $\rho$ (negativer Block links, positiver rechts),
(2) das daraus folgende dreieckige Feld $\mathcal E(x)$ mit Maximum am Übergang, (3) das parabelförmige Potential
$\phi(x)$ mit Gesamthub $V_d$.
:::

Zwei Bedingungen legen die Weiten $x_p$ (p-Seite) und $x_n$ (n-Seite) fest:

- **Ladungsneutralität** (die Zone ist nach außen neutral, positive = negative Gesamtladung):
  $$N_A\,x_p = N_D\,x_n.$$
- **Stetigkeit** des Potentials am Übergang, mit Gesamthub $V_d$.

Daraus folgt der entscheidende Befund: Die Verarmungszone reicht **weiter in das schwächer
dotierte Gebiet** hinein. Denn dort müssen **mehr** Atome „entblößt" werden, um dieselbe Gesamtladung
bereitzustellen wie die wenigen, aber dicht sitzenden Ionen der stark dotierten Seite.

**Ein Zahlenbeispiel zur Veranschaulichung:** Ist die n-Seite $100$-mal stärker dotiert als die p-Seite
($N_D = 100\,N_A$), dann folgt aus $N_A x_p = N_D x_n$ sofort $x_n = x_p/100$ — die Zone liegt fast vollständig
im schwach dotierten p-Gebiet. Allgemein gilt für die Gesamtweite $W=x_p+x_n$:

$$W = \sqrt{\frac{2\varepsilon_0\varepsilon_r\,V_d}{e}\left(\frac{1}{N_A}+\frac{1}{N_D}\right)}.$$

Daran liest man auch ab: **stärkere Dotierung → dünnere Verarmungszone** (größere $N$ im Nenner). Die einzelnen
Weiten auf p- und n-Seite folgen mit der Neutralität $N_A x_p = N_D x_n$ zu

$$x_p = \frac{N_D}{N_A+N_D}\,W = \sqrt{\frac{N_D}{N_A+N_D}\cdot\frac{2\varepsilon_0\varepsilon_r\,V_d}{e\,N_A}}, \qquad x_n = \frac{N_A}{N_A+N_D}\,W,$$

also fällt der größere Teil der Zone stets ins schwächer dotierte Gebiet.

:::grafik
Zwei pn-Übergänge mit gleichem $N_A$, aber unterschiedlichem $N_D$: beim symmetrischen Fall ($N_D=N_A$) ist die
Zone gleichmäßig verteilt; beim stark asymmetrischen ($N_D\gg N_A$) ragt sie fast nur in die p-Seite. Die
Verarmungsweiten $x_p, x_n$ sind als Doppelpfeile bemaßt, die Flächen (= Ladung) gleich groß markiert.
:::

:::kern
Trifft ein p- auf ein n-Gebiet, diffundieren Ladungsträger über das Konzentrationsgefälle und rekombinieren;
zurück bleiben ortsfeste ionisierte Dotieratome — die __Raumladungszone__ (Verarmungszone) mit eingebautem Feld.
Im Gleichgewicht ist das __Fermi-Niveau__ konstant ($dE_f/dx=0$: Diffusion $=$ Feld), die Bänder biegen sich um
$eV_d$. __Diffusionsspannung__ $V_d=\tfrac{k_BT}{e}\ln(N_AN_D/n_i^2)$ (nur logarithmisch von der Dotierung
abhängig). Mit der __Schottky-Näherung__ (kastenförmige Raumladung) liefert die Poisson-Gleichung parabolische
Bänder; Neutralität $N_A x_p=N_D x_n$ → die Zone reicht **weiter ins schwächer dotierte** Gebiet, Gesamtweite
$W=\sqrt{\tfrac{2\varepsilon_0\varepsilon_r V_d}{e}(\tfrac1{N_A}+\tfrac1{N_D})}$ (stärkere Dotierung → dünner).
:::

Der pn-Übergang im Gleichgewicht hat eine feste Barriere $eV_d$. Interessant wird er, wenn man eine **äußere
Spannung** anlegt, die diese Barriere hebt oder senkt — dann entsteht die stark asymmetrische Strom-Spannungs-
Kennlinie der __Diode__, das Thema des nächsten Artikels.

:::quiz
F: Warum entsteht am pn-Übergang überhaupt eine Raumladungszone?
A: Am Kontakt herrscht ein riesiges Konzentrationsgefälle, sodass Elektronen und Löcher über die Grenze diffundieren und dort rekombinieren. Zurück bleiben die ortsfesten ionisierten Dotieratome, die als unkompensierte Raumladung eine Zone ohne bewegliche Ladungsträger bilden.
F: Was stoppt die Diffusion am pn-Übergang, sodass kein Dauerstrom fließt?
A: Die zurückbleibenden Ionen erzeugen ein elektrisches Feld, das der Diffusion entgegenwirkt. Es wächst, bis sein „Gegendruck" den chemischen Diffusionsantrieb exakt kompensiert — dann herrscht Gleichgewicht.
F: Warum ist im Gleichgewicht das Fermi-Niveau über den ganzen Übergang konstant?
A: Ein konstantes (elektrochemisches) Fermi-Niveau ist gleichbedeutend mit „kein Netto-Strom". Diffusionsantrieb $d\mu/dx$ und Feldkraft $|e|\,d\phi/dx$ heben sich gerade auf, was eine durchgehend waagerechte $E_f$-Linie bedeutet.
F: Warum biegen sich die Bänder, obwohl $E_f$ waagerecht bleibt?
A: Die beiden Gebiete hatten vor dem Kontakt verschieden hohe Fermi-Niveaus; beim Angleichen auf ein gemeinsames $E_f$ müssen sich die Bandkanten relativ dazu verschieben. Diese Verschiebung ist genau die Bandverbiegung um $eV_d$.
F: Warum wird die Diffusionsspannung größer, je stärker beide Seiten dotiert sind?
A: Stärkere Dotierung schiebt $E_f$ der n-Seite näher an $E_L$ und das der p-Seite näher an $E_V$, sodass die beiden Fermi-Niveaus vor Kontakt weiter auseinanderliegen. Dieser Abstand ist gerade $eV_d$, also wächst $V_d$ mit der Dotierung — allerdings nur logarithmisch.
F: Warum hängt $V_d$ nur so schwach (logarithmisch) von der Dotierung ab?
A: $V_d$ misst den Fermi-Niveau-Abstand, und $E_f$ verschiebt sich gegenüber einer Bandkante nur logarithmisch mit der Ladungsträgerdichte ($E_f=E_L-k_BT\ln(N_L/N_D)$). Selbst über viele Dekaden Dotierung bleibt $V_d$ daher bei einigen Zehntel Volt.
F: Was idealisiert die Schottky-Näherung und wozu?
A: Sie ersetzt den weichen Übergang der Raumladung durch eine kastenförmige Verteilung: ein Ort ist entweder voll verarmt oder voll neutral. Dadurch wird die Poisson-Gleichung analytisch lösbar und liefert dreieckiges Feld und parabolische Bänder.
F: Warum reicht die Verarmungszone weiter in das schwächer dotierte Gebiet?
A: Die Ladungsneutralität $N_A x_p=N_D x_n$ verlangt beiderseits gleich viel Gesamtladung. Auf der schwach dotierten Seite sitzen die Ionen dünner, also müssen mehr Atome über eine größere Weite entblößt werden, um dieselbe Ladung bereitzustellen.
F: Warum wird die Verarmungszone bei stärkerer Dotierung dünner?
A: In $W=\sqrt{\tfrac{2\varepsilon_0\varepsilon_r V_d}{e}(1/N_A+1/N_D)}$ stehen die Dotierdichten im Nenner. Mehr Ionen pro Volumen liefern die nötige Ladung auf engerem Raum, sodass die Zone schrumpft (abgesehen vom schwachen logarithmischen Anstieg von $V_d$).
F: Warum ist das dreieckige Feldprofil am Übergang maximal und an den Zonenrändern null?
A: Das Feld ist das Integral der Raumladung; es baut sich über die ganze Zone auf und erreicht an der Grenze zwischen positiver und negativer Ladung sein Maximum. An den Außenrändern grenzt die Zone an das neutrale Gebiet, wo kein Feld herrschen darf — dort fällt es auf null.
:::
