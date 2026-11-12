---
title: Stufe 3: Die Raumladungszone
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1190500
summary: Ein n-Stück und ein p-Stück sind für sich nur Widerstände.
tags: Diffusion, Raumladung, Drift, Diffusionsspannung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Ein n-Stück und ein p-Stück sind für sich nur Widerstände. Diese Stufe zeigt, was an ihrer Grenze entsteht und warum es eine Barriere ist.
:::

**Die Idee.** In einem Kristall grenzt ein p-Gebiet an ein n-Gebiet. Vier Schritte laufen ab (Abb. [4](#abb-4)):

<ol>

<li>

⁠**Diffusion.** Ladungsträger bewegen sich ungeordnet. Aus dem Gebiet hoher Dichte wandern mehr hinaus als hinein. Dieser Ausgleich durch Zufallsbewegung heißt __Diffusion__. Elektronen wandern vom n- ins p-Gebiet, Löcher umgekehrt.

</li>

<li>

⁠**Rekombination.** Im fremden Gebiet treffen die Wanderer auf die dortige Mehrheit und verschwinden. Nahe der Grenze gibt es danach kaum noch freie Träger.

</li>

<li>

⁠**Feste Ionen bleiben.** Dort sind die Ionen nicht mehr ausgeglichen: $\mathrm P^+$ auf der n-Seite, $\mathrm B^-$ auf der p-Seite. Diese ortsfeste Ladung heißt __Raumladung__, die Schicht Raumladungszone.

</li>

<li>

⁠**Das Feld stoppt den Ausgleich.** Die Ionen erzeugen ein Feld von der n- zur p-Seite. Es treibt Elektronen zurück ins n-Gebiet und Löcher zurück ins p-Gebiet (__Drift__, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Die Zone wächst, bis der Driftstrom den Diffusionsstrom genau aufhebt.

</li>

</ol>

:::abbildung et1/k9rlz 4
pn-Übergang ohne äußere Spannung. Oben: Kästchen sind feste Ionen, gefüllte Kreise Elektronen, offene Kreise Löcher. In der Zone fehlen die beweglichen Träger, das Feld $E$ zeigt zur p-Seite. Unten: Das Potenzial steigt nur in der Zone, insgesamt um $U_\mathrm{D0}=0{,}71$ V. Diese Potenzialstufe bremst Elektronen auf dem Weg zur p-Seite.
:::

:::satz Satz 3.1 (Diffusionsspannung und Zonenbreite)
<span class="anker" id="satz-3-1"></span>

Für einen scharfen Übergang gilt mit der Temperaturspannung $U_T=k_\mathrm BT/e$

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2},\qquad w=\sqrt{\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}},\qquad E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}. \tag{3.1}$$
:::

⁠**So liest man das:** $U_\mathrm{D0}$ ist die __Diffusionsspannung__, die Potenzialstufe zwischen beiden Gebieten, bei Silizium um 0,7 bis 0,9 V. Elektronen sehen auf dem Weg zur p-Seite eine Energiebarriere $W_\mathrm B=e\,U_\mathrm{D0}$. $w$ ist die Breite der Zone, $\varepsilon=\varepsilon_0\varepsilon_\mathrm r=1{,}04\cdot10^{-10}$ A s/(V m) die Permittivität ([Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)). Die Zone reicht tiefer in das schwächer dotierte Gebiet: $w_\mathrm n/w_\mathrm p=N_\mathrm A/N_\mathrm D$. **Gültigkeit:** Gleichgewicht, Dichten in [(3.1)](#gl-3-1) in 1/m$^3$ einsetzen.

:::herleitung Potenzialstufe und Breite
⁠**Potenzialstufe.** Ein Elektron auf der p-Seite hat die Barriere erklommen. Nach [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1) gilt für die Dichten $n_\mathrm p/n_\mathrm n=\mathrm{e}^{-U_\mathrm{D0}/U_T}$. Mit $n_\mathrm n=N_\mathrm D$ und $n_\mathrm p=n_\mathrm i^2/N_\mathrm A$ aus [(2.1)](dotierung.html#gl-2-1) folgt die erste Gleichung.

⁠**Breite.** Beide Seiten tragen gleich viel Ladung, also $N_\mathrm Aw_\mathrm p=N_\mathrm Dw_\mathrm n$. Das Feld wächst von den Rändern linear bis zur Grenze und erreicht dort den Wert einer Flächenladung ([Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), $E_\mathrm{max}=e\,N_\mathrm Dw_\mathrm n/\varepsilon$. Die Spannung ist die Fläche unter dem Feldverlauf, ein Dreieck: $U_\mathrm{D0}=\tfrac12E_\mathrm{max}w$. Mit $w=w_\mathrm n+w_\mathrm p$ ergibt das [(3.1)](#gl-3-1).
:::

::::beispiel
$U_\mathrm{D0}=25{,}85\,\mathrm{mV}\cdot\ln10^{12}=0{,}714$ V, das sind $27{,}6\,U_T$. Die Barriere lässt also den Anteil $\mathrm{e}^{-27{,}6}=10^{-12}$ passieren, genau das Verhältnis $10^{4}/10^{16}$ der Dichten. Weiter ist $w=0{,}43$ µ m, je zur Hälfte in beiden Gebieten, und $E_\mathrm{max}=3{,}3$ MV/m, so viel wie die Durchschlagsfeldstärke von Luft ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)).
::::

⁠**Grenzfälle:** Ist eine Seite viel stärker dotiert, liegt die Zone fast ganz in der anderen. Zehnmal mehr Dotierung auf einer Seite hebt $U_\mathrm{D0}$ nur um 60 mV.

:::frage In der Diode stecken 0,71 V. Warum misst man an ihr 0 V, und warum treibt sie keinen Strom?
Die Potenzialstufe ist echt, aber sie ist nicht die einzige im Kreis. Wo Metallkontakte auf den Halbleiter treffen, entstehen weitere Kontaktspannungen. Rund um jeden Kreis ist ihre Summe null, denn im Gleichgewicht gibt es keine Energiequelle. Sie stellt nur das Gleichgewicht zwischen Diffusion und Drift her.
:::

:::aufgabe Aufgabe 3 ★★ Ein einseitiger Übergang
<span class="anker" id="aufg-3"></span>

Ein pn-Übergang hat $N_\mathrm A=10^{18}\,\mathrm{cm^{-3}}$ und $N_\mathrm D=10^{15}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Berechne $U_\mathrm{D0}$, $w$ und $E_\mathrm{max}$.

</li>

<li>

Wie breit ist die Zone auf jeder Seite? Warum liegt sie fast ganz im schwach dotierten Gebiet?

</li>

</ol>

:::loesung
(a) $U_\mathrm{D0}=25{,}85\,\mathrm{mV}\cdot\ln(10^{33}/10^{20})=0{,}774$ V. Weil $1/N_\mathrm A$ neben $1/N_\mathrm D$ entfällt, ist $w=\sqrt{2\varepsilon U_\mathrm{D0}/(e\,N_\mathrm D)}=1{,}00$ µ m und $E_\mathrm{max}=2U_\mathrm{D0}/w=1{,}55$ MV/m. (b) $w_\mathrm n/w_\mathrm p=1000$, also $w_\mathrm n=1{,}00$ µ m und $w_\mathrm p=1{,}0$ nm. Beide Seiten müssen dieselbe Ionenladung stellen. Im schwach dotierten Gebiet sitzen die Ionen tausendmal dünner, also braucht es tausendmal mehr Tiefe.
:::
:::

::::formelsammlung
**Diffusionsspannung**

$$U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2}$$

Potenzialstufe zwischen p- und n-Gebiet, mit der Temperaturspannung $U_T=k_\mathrm BT/e$; bei Silizium um 0,7 bis 0,9 V. Folgt aus dem Dichteverhältnis $n_\mathrm p/n_\mathrm n=\mathrm{e}^{-U_\mathrm{D0}/U_T}$. Gilt für einen scharfen Übergang im Gleichgewicht.

**Energiebarriere**

$$W_\mathrm B=e\,U_\mathrm{D0}$$

Barriere für Elektronen auf dem Weg zur p-Seite.

**Breite der Raumladungszone**

$$w=\sqrt{\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}}$$

$\varepsilon=\varepsilon_0\varepsilon_\mathrm r$ ist die Permittivität. Scharfer Übergang im Gleichgewicht, Dichten in 1/m$^3$ einsetzen.

**Größte Feldstärke**

$$E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}$$

Das Feld wächst von den Rändern linear bis zur Grenze; die Spannung ist die Dreiecksfläche $U_\mathrm{D0}=\tfrac12E_\mathrm{max}w$.

**Aufteilung der Zone**

$$N_\mathrm Aw_\mathrm p=N_\mathrm Dw_\mathrm n,\qquad w_\mathrm n/w_\mathrm p=N_\mathrm A/N_\mathrm D$$

Beide Seiten tragen gleich viel Ladung; die Zone reicht tiefer in das schwächer dotierte Gebiet. Es ist $w=w_\mathrm n+w_\mathrm p$.
::::

::::lernkarten
:::karte begriff pn-Übergang
Was ist ein pn-Übergang in einem Halbleiterkristall, und was bildet sich an ihm?
---
Die Grenze zwischen einem p-Gebiet und einem n-Gebiet in ein und demselben Kristall. An ihr bildet sich von selbst die Raumladungszone, die als Energiebarriere wirkt.
--- falsch
Eine Lötstelle, an der ein p-dotiertes und ein n-dotiertes Stück mit einem Metalldraht verbunden werden. Der Draht trägt den Strom zwischen beiden Stücken.
--- falsch
Die Grenze zwischen einem dotierten Gebiet und reinem Silizium. An ihr wechselt das Material vom Leiter zum Isolator, und es bildet sich eine Schicht ohne Ionen.
--- falsch
Die Grenze zwischen dem VB und dem LB im Bändermodell, an der Elektronen vom p-Zustand in den n-Zustand übergehen und dabei Energie abgeben.
:::
:::karte begriff Diffusion
Was versteht man unter Diffusion, und in welche Richtung wandern die Ladungsträger am pn-Übergang?
---
Den Ausgleich durch Zufallsbewegung: Aus einem Gebiet hoher Dichte wandern mehr Teilchen hinaus als hinein. Elektronen wandern vom n- ins p-Gebiet, Löcher umgekehrt.
--- falsch
Die Bewegung von Ladungsträgern unter der Kraft eines Feldes. Elektronen wandern vom p- ins n-Gebiet, Löcher umgekehrt, weil das Feld zur p-Seite zeigt.
--- falsch
Den Ausgleich durch Zufallsbewegung: Aus einem Gebiet hoher Dichte wandern mehr Teilchen hinaus als hinein. Elektronen und Löcher wandern beide vom n- ins p-Gebiet.
--- falsch
Das Verschwinden von Elektronen und Löchern, wenn sie sich treffen. Es läuft am pn-Übergang nur von der n-Seite aus ab, weil dort mehr Elektronen sind.
:::
:::karte zusammenhang Vier Schritte am pn-Übergang
Welche vier Vorgänge laufen ab, wenn ein p-Gebiet an ein n-Gebiet grenzt, und wann endet der Ausgleich?
---
Diffusion ins andere Gebiet, Rekombination mit der dortigen Mehrheit, zurückbleibende feste Ionen und deren Feld, das die Träger zurücktreibt. Die Zone wächst, bis der Driftstrom den Diffusionsstrom genau aufhebt.
--- falsch
Diffusion ins andere Gebiet, bis beide Seiten gleich dotiert sind, dann Rekombination, Ionisation und Feld. Der Ausgleich endet erst, wenn alle beweglichen Träger beider Gebiete miteinander rekombiniert sind und der Kristall isoliert.
--- falsch
Feld, Drift, Rekombination und Diffusion in dieser Reihenfolge: Das Feld ist von Anfang an da und zieht die Träger an die Grenze. Der Ausgleich endet, wenn das Feld verschwindet.
--- falsch
Diffusion der Ionen ins andere Gebiet, Rekombination mit den Trägern, Neutralisation und Abkühlung. Der Ausgleich endet, wenn beide Gebiete dieselbe Temperatur haben.
:::
:::karte begriff Raumladung und Raumladungszone
Was ist die Raumladung am pn-Übergang, und was kennzeichnet die Raumladungszone?
---
Die ortsfeste Ladung der nicht mehr ausgeglichenen Ionen, $\mathrm P^+$ auf der n-Seite und $\mathrm B^-$ auf der p-Seite. Die Raumladungszone ist die dünne Schicht mit dieser Ladung ohne bewegliche Ladungsträger; sie wirkt als Energiebarriere.
--- falsch
Die Ladung der Elektronen und Löcher, die sich an der Grenze stauen, Elektronen auf der p-Seite und Löcher auf der n-Seite. Die Raumladungszone ist die Schicht, in der sie sich besonders dicht sammeln, weil sie dort nicht weiterkommen.
--- falsch
Die ortsfeste Ladung der Ionen, $\mathrm B^-$ auf der n-Seite und $\mathrm P^+$ auf der p-Seite. Die Raumladungszone ist die dünne Schicht mit dieser Ladung, in der besonders viele Ladungsträger frei beweglich sind.
--- falsch
Die Ladung, die eine äußere Quelle auf den Kristall bringt. Die Raumladungszone ist der Bereich nahe den Metallkontakten, in dem diese Ladung sitzt und den Strom durch die Diode begrenzt.
:::
:::karte begriff Drift
Was bezeichnet man in der Raumladungszone als Drift, und in welche Richtung treibt das Feld die Ladungsträger?
---
Die Bewegung der Ladungsträger unter dem Feld. Das Feld der Ionen zeigt von der n- zur p-Seite und treibt Elektronen zurück ins n-Gebiet und Löcher zurück ins p-Gebiet.
--- falsch
Die Zufallsbewegung der Ladungsträger durch Wärme. Sie treibt Elektronen ins p-Gebiet und Löcher ins n-Gebiet, bis die Dichten auf beiden Seiten der Grenze gleich groß sind.
--- falsch
Die Bewegung der Ladungsträger unter dem Feld. Das Feld der Ionen zeigt von der p- zur n-Seite und treibt Elektronen ins p-Gebiet und Löcher ins n-Gebiet.
--- falsch
Das langsame Wandern der Ionen unter dem Feld. Die $\mathrm P^+$-Ionen driften zur p-Seite, die $\mathrm B^-$-Ionen zur n-Seite, bis sich die Zone wieder schließt.
:::
:::karte begriff Diffusionsspannung
Was ist die Diffusionsspannung $U_\mathrm{D0}$ eines pn-Übergangs, und wie groß ist sie bei Silizium?
---
Die Potenzialstufe zwischen p- und n-Gebiet im Gleichgewicht, bei Silizium um 0,7 bis 0,9 V. Elektronen sehen auf dem Weg zur p-Seite die Energiebarriere $W_\mathrm B=e\,U_\mathrm{D0}$.
--- falsch
Die Spannung, die man außen an die Diode legen muss, damit überhaupt Strom fließt, bei Silizium genau 0,7 V. Darunter fließt kein Strom, darüber der volle.
--- falsch
Die Spannung, die ein Voltmeter an den Anschlüssen der stromlosen Diode misst, bei Silizium um 0,7 bis 0,9 V. Sie treibt einen kleinen Strom durch jede angeschlossene Last.
--- falsch
Die Potenzialstufe zwischen p- und n-Gebiet, bei Silizium um 25,85 mV, so groß wie die Temperaturspannung. Elektronen sehen dabei die Barriere $W_\mathrm B=e\,U_\mathrm{D0}$.
:::
:::karte formel Diffusionsspannung
Wie berechnet man die Diffusionsspannung eines scharfen pn-Übergangs aus den Dotierungen, und welchen Wert ergeben je $10^{16}$ Fremdatome pro cm$^3$ in Silizium?
---
$U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2}$ mit $U_T=k_\mathrm BT/e$, gültig im Gleichgewicht. Mit $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ sind das $25{,}85\,\mathrm{mV}\cdot\ln10^{12}=0{,}714$ V.
--- falsch
$U_\mathrm{D0}=U_T\,\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2}$, ohne Logarithmus. Mit $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ wären das $25{,}85\,\mathrm{mV}\cdot10^{12}$, eine riesige Spannung, die die Zone sofort durchschlägt.
--- falsch
$U_\mathrm{D0}=U_T\ln\frac{n_\mathrm i^2}{N_\mathrm AN_\mathrm D}$, gültig im Gleichgewicht. Mit $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ sind das $-0{,}714$ V, die n-Seite liegt also tiefer als die p-Seite.
--- falsch
$U_\mathrm{D0}=U_T\ln\frac{N_\mathrm A+N_\mathrm D}{n_\mathrm i}$, gültig im Gleichgewicht. Mit $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ sind das $25{,}85\,\mathrm{mV}\cdot\ln(2\cdot10^{6})=0{,}38$ V.
:::
:::karte herleitung Diffusionsspannung aus der Boltzmann-Verteilung
Wie folgt aus der Boltzmann-Verteilung und den Trägerdichten beider Gebiete die Formel $U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2}$?
---
Für die Elektronendichten beider Seiten gilt $n_\mathrm p/n_\mathrm n=\mathrm{e}^{-U_\mathrm{D0}/U_T}$, weil ein Elektron auf der p-Seite die Barriere $e\,U_\mathrm{D0}$ erklommen hat und nach der Boltzmann-Verteilung nur dieser Anteil das schafft.
---
Im n-Gebiet ist $n_\mathrm n=N_\mathrm D$, weil dort jeder Donator ein Elektron liefert.
---
Im p-Gebiet ist $n_\mathrm p=n_\mathrm i^2/N_\mathrm A$, weil dort $p\approx N_\mathrm A$ ist und überall $n\,p=n_\mathrm i^2$ gilt.
---
Einsetzen und Logarithmieren ergibt $U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2}$, weil der Logarithmus die Exponentialfunktion umkehrt.
:::
:::karte formel Zonenbreite und Feldstärke
Wie hängen die Breite $w$ der Raumladungszone und die größte Feldstärke $E_\mathrm{max}$ von Dotierung und Diffusionsspannung ab?
---
$w=\sqrt{\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}}$ und $E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}$ mit $\varepsilon=\varepsilon_0\varepsilon_\mathrm r$. Gilt für einen scharfen Übergang im Gleichgewicht, Dichten in 1/m$^3$.
--- falsch
$w=\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}$ ohne Wurzel und $E_\mathrm{max}=\frac{U_\mathrm{D0}}{w}$, weil das Feld in der Zone überall gleich groß ist wie im Plattenkondensator mit festem Abstand.
--- falsch
$w=\sqrt{\frac{2\varepsilon}{e}\bigl(N_\mathrm A+N_\mathrm D\bigr)U_\mathrm{D0}}$ und $E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}$: Stärkere Dotierung macht die Zone breiter, weil mehr Ionen mehr Platz brauchen.
--- falsch
$w=\sqrt{\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}}$ und $E_\mathrm{max}=\frac{w}{2U_\mathrm{D0}}$, sodass eine breitere Zone ein stärkeres Feld trägt. Gilt bei jeder äußeren Spannung.
:::
:::karte herleitung Zonenbreite aus Ladung und Feldverlauf
Wie folgen aus der Ladungsgleichheit beider Seiten und dem Feldverlauf die Formeln für $E_\mathrm{max}$ und die Zonenbreite $w$?
---
Beide Seiten tragen gleich viel Ladung, $N_\mathrm Aw_\mathrm p=N_\mathrm Dw_\mathrm n$, weil der Kristall als Ganzes neutral bleibt.
---
Das Feld wächst von den Rändern linear bis zur Grenze und erreicht dort $E_\mathrm{max}=e\,N_\mathrm Dw_\mathrm n/\varepsilon$, weil die Ionen gleichmäßig verteilt sind und an der Grenze wie eine Flächenladung wirken.
---
Die Spannung ist die Fläche unter dem dreieckigen Feldverlauf, $U_\mathrm{D0}=\tfrac12E_\mathrm{max}w$, weil sie sich als Feldstärke mal Wegstück aufsummiert.
---
Mit $w=w_\mathrm n+w_\mathrm p$ ergeben sich $E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}$ und die Formel für $w$, weil sich $w_\mathrm n$ über die Ladungsgleichheit durch $w$ ausdrücken lässt.
:::
:::karte zusammenhang Zone im schwach dotierten Gebiet
Warum reicht die Raumladungszone tiefer in das schwächer dotierte Gebiet hinein?
---
Beide Seiten müssen dieselbe Ionenladung stellen, $N_\mathrm Aw_\mathrm p=N_\mathrm Dw_\mathrm n$. Im schwach dotierten Gebiet sitzen die Ionen dünner, also braucht es mehr Tiefe: $w_\mathrm n/w_\mathrm p=N_\mathrm A/N_\mathrm D$.
--- falsch
Im schwach dotierten Gebiet gibt es weniger Ladungsträger, die das Feld abschirmen, also dringt das Feld dort tiefer ein. Die Tiefen verhalten sich wie $w_\mathrm n/w_\mathrm p=N_\mathrm D/N_\mathrm A$.
--- falsch
Die Träger des stark dotierten Gebiets diffundieren tief in das schwache hinein und laden es dort auf. Die Zone liegt deshalb dort, wo die Wanderer ankommen, mit $w_\mathrm n/w_\mathrm p=N_\mathrm D/N_\mathrm A$.
--- falsch
Beide Seiten der Zone sind zunächst gleich breit, aber das Feld räumt das schwach dotierte Gebiet zusätzlich aus. Die Zone reicht dort deshalb immer doppelt so tief, gleich wie stark dotiert wird.
:::
:::karte zusammenhang Stromlose Diode
Warum misst man an einer stromlosen Diode 0 V, obwohl in ihr eine Diffusionsspannung von 0,71 V steckt?
---
Wo die Metallkontakte auf den Halbleiter treffen, entstehen weitere Kontaktspannungen. Rund um jeden Kreis ist ihre Summe null, denn im Gleichgewicht gibt es keine Energiequelle.
--- falsch
Die Diffusionsspannung besteht nur, solange Strom durch die Diode fließt; ohne Strom bricht die Zone zusammen. Ein Voltmeter zieht zu wenig Strom, um sie während der Messung aufrechtzuerhalten.
--- falsch
Das Voltmeter hat einen zu kleinen Innenwiderstand: Es entlädt die Zone sofort, und die 0,71 V sinken auf null, bevor die Anzeige sie erfasst. Ein besseres Gerät würde sie anzeigen.
--- falsch
Die Diffusionsspannung ist zu klein, um gemessen zu werden; erst ab etwa 1 V zeigt ein übliches Voltmeter etwas an. Mit einem empfindlichen Gerät sieht man die 0,71 V.
:::
:::karte zusammenhang Stärkere Dotierung einer Seite
Was passiert mit der Diffusionsspannung, wenn man eine Seite des pn-Übergangs zehnmal stärker dotiert?
---
Sie steigt nur um rund 60 mV, weil die Dotierung im Logarithmus von $U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2}$ steht. Die Zone verlagert sich dabei weiter in das schwächer dotierte Gebiet.
--- falsch
Sie steigt auf das Zehnfache, also auf rund 7 V, weil die Zahl der Ionen in der Zone zehnmal größer ist und jede Ladung zur Spannung beiträgt.
--- falsch
Sie sinkt um rund 60 mV, weil die stärkere Dotierung mehr bewegliche Ladungsträger liefert, die das Feld der Ionen teilweise abschirmen und die Potenzialstufe dadurch abflachen.
--- falsch
Sie bleibt genau gleich, weil sie nur von der Temperatur abhängt; nur die Breite der Zone ändert sich mit der Dotierung.
:::
::::
