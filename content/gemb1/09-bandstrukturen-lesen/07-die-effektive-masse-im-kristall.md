---
title: Stufe 5: Die effektive Masse im Kristall
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Bandstrukturen lesen
order: 4190700
summary: Teil 2 hat die Masse als Krümmung von E(k) eingeführt.
tags: Kristallimpuls
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
[Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) hat die Masse als Krümmung von $E(k)$ eingeführt. Diese Stufe zeigt, warum diese Größe tatsächlich in Newtons Gesetz gehört und was aus ihr längs eines ganzen Bands wird.
:::

**Die Idee.** Auf ein Elektron im Kristall wirken zwei Kräfte. Die Rumpfionen ziehen es mit starken, rasch wechselnden Kräften, ein äußeres Feld schiebt es viel schwächer und gleichmäßig. Die erste Kraft ist schon in $E(k)$ eingerechnet, die zweite verschiebt nur $k$. Man kann also so tun, als gäbe es das Gitter nicht, wenn man dem Elektron eine andere Masse gibt. Der Einfluss des Festkörperpotentials steckt dann pauschal in $m^*$.

:::satz Satz 5.1 (Bewegung im Band)
<span class="anker" id="satz-5-1"></span>

Eine äußere Kraft $F$ ändert den Wellenvektor, $\hbar\,\mathrm{d} k/\mathrm{d} t=F$, die Geschwindigkeit folgt aus $E(k)$ wie in [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1). Daraus ergibt sich

<span class="anker" id="gl-5-1"></span>
$$F=m^*\,\frac{\mathrm{d} v}{\mathrm{d} t}\qquad\text{mit}\qquad m^*(k)=\Bigl(\frac1{\hbar^2}\,\frac{\partial^2E(k)}{\partial k^2}\Bigr)^{-1}. \tag{5.1}$$
:::

:::herleitung Von Newton zur Krümmung
Newton verlangt $F=m\,\mathrm{d} v/\mathrm{d} t$. Mit $p=\hbar k$ ist zugleich $F=\hbar\,\mathrm{d} k/\mathrm{d} t=\hbar\,(\mathrm{d} k/\mathrm{d} v)(\mathrm{d} v/\mathrm{d} t)$. Der Vergleich ergibt

$$m=\hbar\,\frac{\mathrm{d} k}{\mathrm{d} v}=\Bigl(\frac1\hbar\,\frac{\mathrm{d} v}{\mathrm{d} k}\Bigr)^{-1}=\Bigl(\frac1\hbar\,\frac{\mathrm{d}}{\mathrm{d} k}\,\frac1\hbar\,\frac{\partial E}{\partial k}\Bigr)^{-1}=\Bigl(\frac1{\hbar^2}\,\frac{\partial^2E}{\partial k^2}\Bigr)^{-1}.$$

Dasselbe von der Zeit her: $\mathrm{d} v/\mathrm{d} t=\frac1\hbar\,\frac{\partial^2E}{\partial k^2}\,\frac{\mathrm{d} k}{\mathrm{d} t}$.
:::

⁠**So liest man das:** $\hbar k$ heißt __Kristallimpuls__. Er ist nicht der ganze Impuls, denn das Gitter tauscht ständig Impuls mit dem Elektron aus, doch er wächst genau mit der äußeren Kraft. $v$ ist die Gruppengeschwindigkeit eines Wellenpakets um $k$. Für das freie Elektron ist $E=\hbar^2k^2/(2m)+V_0$ und $m^*=m$. Im Band hängt die Masse von $k$ ab. Gleichungen für freie Elektronen gelten weiter, wenn man $m$ durch $m^*$ ersetzt. **Gültigkeit:** Die Kraft ändert sich langsam gegen $a$ und hält das Elektron im Band, also $e\mathcal Ea\ll$ Bandbreite. Bei $\mathcal E=10^6$ V/m ist $e\mathcal Ea=0{,}25$ meV, 8000-mal weniger als 2 eV.

**Längs des Bands.** Für $E(k)=E_\mathrm s-2V_\mathrm{ss}\cos(ka)$ folgen

<span class="anker" id="gl-5-2"></span>
$$v(k)=\frac{2V_\mathrm{ss}a}\hbar\sin(ka),\qquad m^*(k)=\frac{\hbar^2}{2V_\mathrm{ss}a^2\cos(ka)}. \tag{5.2}$$

:::abbildung gemb1/k9masse 5
Kosinus-Band mit $V_\mathrm{ss}=0{,}5$ eV und $a=0{,}25$ nm. Oben: Energie, grün gestrichelt die Parabeln an den Bandkanten. Mitte: Geschwindigkeit, die Steigung der oberen Kurve. Unten: effektive Masse, sie läuft bei $|ka|=\pi/2$ ins Unendliche und ist in den rot getönten Bereichen negativ.
:::

Von der Unterkante aus steigt $v$, erreicht bei $ka=\pi/2$ das Maximum und fällt bis zur Oberkante auf null. Dort liegen stehende Wellen vor ([Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html)), die Tangente an $E(k)$ ist waagerecht. Die Masse wächst und geht am Wendepunkt ($\partial^2E/\partial k^2=0$) gegen $+\infty$. Oben ist sie negativ, sie kommt von $-\infty$ und erreicht an der Oberkante $-\hbar^2/(2V_\mathrm{ss}a^2)$. Eine feste Masse gibt es nur nahe den Kanten, wo das Band eine Parabel ist:

<span class="anker" id="gl-5-3"></span>
$$E\approx E_\mathrm C+\frac{\hbar^2(k-k_\mathrm C)^2}{2m_\mathrm C^*},\qquad E\approx E_\mathrm V-\frac{\hbar^2(k-k_\mathrm V)^2}{2m_\mathrm V^*}. \tag{5.3}$$

$m_\mathrm C^*$ und $m_\mathrm V^*$ sind positive Beträge. Dazwischen sind wenig allgemeine Aussagen möglich. **Mechanismus der negativen Masse:** Die Kraft schiebt $k$ auf den Zonenrand zu. Dort wird die Welle am Gitter reflektiert, und die Reflexion gibt mehr Impuls ans Gitter ab, als die Kraft zuführt. Das Elektron wird langsamer. Der Energiegewinn geht in potentielle Energie, denn die stehende Welle rückt in die Gebiete hohen Potentials zwischen den Atomen. Beim freien Elektron wächst dagegen nur die kinetische Energie.

**Beispiel.** Im Rechenmodell ist $v_\text{max}=3{,}8\cdot10^5$ m/s und $\hbar^2/(2V_\mathrm{ss}a^2)=1{,}22\,m_0$. Bei $ka=\pi/4$ sind $v=2{,}69\cdot10^5$ m/s und $m^*=1{,}72\,m_0$, bei $3\pi/4$ gleiches $v$ und $m^*=-1{,}72\,m_0$. Dieselbe Kraft beschleunigt ein Elektron in GaAs 14,9-mal stärker als ein freies. **Grenzfall:** Mit der Kopplung $t_0=\hbar^2/(2ma^2)$ des Rechengitters aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) statt $V_\mathrm{ss}$ ergibt [(5.2)](#gl-5-2) bei $k=0$ genau $m^*=m$.

:::frage Läuft ein Elektron im Feld wirklich bis zum oberen Bandrand und wieder zurück?
Ohne Stöße ja, bei $10^6$ V/m wäre die Zone nach 16,5 ps durchlaufen. Das heißt Bloch-Schwingung. Stöße mit Gitterschwingungen bremsen das Elektron aber schon nach etwa 0,1 ps, nach gut 1 % des Wegs zum Zonenrand. Deshalb reicht meist die Parabel [(5.3)](#gl-5-3).
:::

:::aufgabe Aufgabe 5 ★★ Masse und Geschwindigkeit im Band
<span class="anker" id="aufg-5"></span>

Eine Kette hat $a=0{,}3$ nm und $V_\mathrm{ss}=0{,}25$ eV.

<ol class="al">

<li>

Berechne Bandbreite, $m^*(0)$ und $v_\text{max}$. Bei welchem $k$ liegt $v_\text{max}$?

</li>

<li>

Berechne $v$ und $m^*$ bei $ka=\pi/3$ und $ka=2\pi/3$.

</li>

<li>

Eine Kraft $F>0$ wirkt auf ein Elektron bei $ka=2\pi/3$. Wie ändert sich $k$? Wird das Elektron schneller oder langsamer?

</li>

</ol>

:::loesung
(a) Breite $4V_\mathrm{ss}=1$ eV, $m^*(0)=\hbar^2/(2V_\mathrm{ss}a^2)=1{,}69\,m_0$, $v_\text{max}=2V_\mathrm{ss}a/\hbar=2{,}28\cdot10^5$ m/s bei $k=\pi/(2a)=5{,}24\,\mathrm{nm^{-1}}$. (b) $ka=\pi/3$: $k=3{,}49\,\mathrm{nm^{-1}}$, $v=1{,}97\cdot10^5$ m/s, $m^*=+3{,}39\,m_0$. $ka=2\pi/3$: $k=6{,}98\,\mathrm{nm^{-1}}$, gleiches $v$, $m^*=-3{,}39\,m_0$. (c) $k$ wächst. Weil $m^*<0$ ist, sinkt $v$: Das Elektron wird langsamer.
:::
:::

:::aufgabe Aufgabe 6 ★★ Masse messen
<span class="anker" id="aufg-6"></span>

Im Magnetfeld $B$ senkrecht zur Bahn laufen Elektronen auf Kreisen. Eingestrahlte Mikrowellen werden aufgenommen, wenn ihre Frequenz der Umlauffrequenz entspricht.

<ol class="al">

<li>

Setze Lorentz-Kraft und Zentripetalkraft gleich und zeige $\omega=eB/m^*$. Warum kommt $v$ nicht vor?

</li>

<li>

Eine Probe zeigt die Resonanz bei $B=0{,}25$ T und $f=104$ GHz. Bestimme $m^*$. Was ergäbe ein freies Elektron?

</li>

</ol>

:::loesung
(a) $evB=m^*v^2/R$ ergibt $v/R=eB/m^*=\omega$. Ein schnelleres Elektron läuft auf einem größeren Kreis, die Umlaufzeit bleibt gleich. (b) $m^*=eB/(2\pi f)=0{,}067\,m_0$, passend zu GaAs. Ein freies Elektron hätte $f=7{,}0$ GHz.
:::
:::
