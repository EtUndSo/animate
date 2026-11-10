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
