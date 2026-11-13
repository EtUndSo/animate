---
title: Stufe 8: Zufallssignale in LTI-Systemen, Leistungsdichte
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270900
summary: Was macht ein LTI-System mit einem Zufallssignal?
tags: Leistungsdichtespektrum
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Was macht ein LTI-System mit einem Zufallssignal? Jede Musterfunktion wird gefaltet. Für die Mittelwerte gelten deshalb einfache Regeln.
:::

**Mittelwert.** Für jede Musterfunktion ist ${}^kg={}^ks*h$. Der Erwartungswert ist linear und darf ins Faltungsintegral:

<span class="anker" id="gl-8-1"></span>
$$m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}=\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau=m_s\int h\,\mathrm{d}\tau=m_s\,H(0). \tag{8.1}$$

Der Mittelwert wird übertragen wie ein Gleichanteil.

:::satz Satz 8.1 (Wiener-Lee für stationäre Prozesse)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2, \tag{8.2}$$

mit der Impuls-AKF $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ der Impulsantwort und dem __Leistungsdichtespektrum__ $\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$. Die Leistung ist

<span class="anker" id="gl-8-3"></span>
$$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f. \tag{8.3}$$
:::

:::herleitung Wiener-Lee
Beide Faltungsintegrale ausschreiben, mit verschiedenen Variablen:

$$g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta.$$

Erwartungswert ins Doppelintegral ziehen. Bei Stationarität ist $\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$. Mit $\vartheta=\beta-\alpha$:

$$\varphi_{gg}(\tau)=\int\varphi_{ss}(\tau-\vartheta)\underbrace{\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha}_{\varphi^E_{hh}(\vartheta)}\,\mathrm{d}\vartheta=\varphi_{ss}*\varphi^E_{hh}.$$

Im Frequenzbereich wird $\varphi^E_{hh}$ zu $|H|^2$ ([Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).
:::

⁠**So liest man das:** $\Phi_{ss}(f)$ gibt an, wie sich die Leistung auf die Frequenzen verteilt. Es ist reell, nie negativ und bei reellen Signalen gerade. Ein LTI-System multipliziert die Leistung bei jeder Frequenz mit $|H(f)|^2$, seine Phase spielt keine Rolle. Das ist dieselbe Regel wie für Energiesignale in [Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html), jetzt für Prozesse. (Zusatz: Streng genommen definiert man $\Phi_{ss}$ als Grenzwert $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ über Kurzzeitspektren von Ausschnitten der Dauer $T$. Dass das dasselbe ist wie die Transformierte der AKF, ist die eigentliche Aussage des Wiener-Khintchine-Theorems.)

:::ltspice Rauschen mit Mittelwert durch Tief- und Hochpass
⁠**Zeichnen:** Verhaltensquelle `bv` am Netz `s` mit `V=1+white(1e3*time)`. `white(x)` liefert Zufallswerte zwischen $-0{,}5$ und $0{,}5$, bei jedem ganzzahligen $x$ einen neuen, weich verbunden, hier also jede Millisekunde. Daran parallel ein RC-Tiefpass (`res` mit `1Meg` nach `tp`, `cap` mit `1u` nach Masse) und ein CR-Hochpass (`cap` mit `1u` nach `hp`, `res` mit `1Meg` nach Masse).

⁠**Direktive:** `.tran 0 200 0 0.1m`.

⁠**Ablesen:** Zoome auf 20 s bis 200 s, also auf die Zeit nach dem Einschwingen. Ein Klick mit gedrückter Strg-Taste auf einen Kurvennamen zeigt Mittelwert (Average) und Effektivwert (RMS) im sichtbaren Bereich.

⁠**Was du siehst:** Der Eingang hat den Mittelwert 1 V. Vergleiche die Mittelwerte von `V(tp)` und `V(hp)` mit deinem Ergebnis aus Aufgabe [7](#aufg-7). Die Schwankungen sind am Tiefpass viel kleiner: Lass dir `V(s)-1` und `V(tp)-1` zeichnen, ihre Effektivwerte sind etwa 0,25 und 0,01. Der Tiefpass lässt von der breiten Leistungsdichte nur etwa den Teil unter $1/(2\pi RC)=0{,}16$ Hz durch, und die Leistung ist nach [(8.3)](#gl-8-3) die Fläche unter der Leistungsdichte.
:::

:::aufgabe Aufgabe 7 ★ Mittelwert durch ein Filter
<span class="anker" id="aufg-7"></span>

Ein Rauschen mit dem Mittelwert 1 V läuft durch einen RC-Tiefpass und durch einen CR-Hochpass. Welche Mittelwerte haben die Ausgänge, und warum?

:::loesung
RC-Tiefpass: $H(0)=1$, Mittelwert 1 V. CR-Hochpass: $H(0)=0$, Mittelwert 0. Der Kondensator lässt keinen Gleichstrom durch, der Gleichanteil wird gesperrt.
:::
:::

::::formelsammlung
**Mittelwert am Systemausgang**

$$m_g=m_s\int h\,\mathrm{d}\tau=m_s\,H(0)$$

Der Mittelwert wird übertragen wie ein Gleichanteil.

**Wiener-Lee für stationäre Prozesse**

$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2$$

Mit der Impuls-AKF $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$. Das System multipliziert die Leistung bei jeder Frequenz mit $|H(f)|^2$; seine Phase spielt keine Rolle.

**Leistungsdichtespektrum und Leistung**

$$\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau),\qquad L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f$$

$\Phi_{ss}$ verteilt die Leistung auf die Frequenzen: reell, nie negativ, bei reellen Signalen gerade.

**Strenge Definition (Wiener-Khintchine)**

$$\Phi_{ss}(f)=\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$$

Über Kurzzeitspektren $S_T$ von Ausschnitten der Dauer $T$. Dass das die Fourier-Transformierte der AKF ist, besagt das Wiener-Khintchine-Theorem.
::::

::::lernkarten
:::karte formel Mittelwert am Systemausgang
Welchen Mittelwert hat das Ausgangssignal eines LTI-Systems mit der Impulsantwort $h(t)$, wenn am Eingang ein stationärer Prozess mit dem Mittelwert $m_s$ liegt?
---
$m_g=m_s\int h\,\mathrm{d}\tau=m_s\,H(0)$: Der Mittelwert wird übertragen wie ein Gleichanteil, also mit dem Wert des Frequenzgangs bei der Frequenz null.
--- falsch
$m_g=m_s\,|H(f)|^2$ bei jeder Frequenz: Der Mittelwert wird wie die Leistung übertragen, also mit dem Betragsquadrat des Frequenzgangs.
--- falsch
$m_g=m_s\,h(0)$: Der Mittelwert wird mit dem Wert der Impulsantwort beim Zeitpunkt null übertragen, weil der Erwartungswert nur zum selben Zeitpunkt wirkt.
--- falsch
$m_g=m_s$: Ein LTI-System verändert den Mittelwert nie, weil Erwartungswert und Faltung vertauschbar sind und die Faltung den Mittelwert erhält.
:::
:::karte herleitung Mittelwert am Systemausgang
Wie folgt aus $g=s*h$ für jede Musterfunktion, dass der Ausgang den Mittelwert $m_g=m_s\,H(0)$ hat?
---
Man schreibt $m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}$, weil jede Musterfunktion des Ausgangs die Faltung der Eingangs-Musterfunktion mit $h$ ist.
---
Man zieht den Erwartungswert ins Integral und erhält $\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau$, weil der Erwartungswert linear ist und das Integral eine gewichtete Summe.
---
Es bleibt $m_s\int h\,\mathrm{d}\tau$, weil bei einem stationären Prozess der Mittelwert $m_s=\mathrm E\{s(t)\}$ nicht von der Zeit abhängt.
---
Das Integral der Impulsantwort ist $H(0)$, weil der Frequenzgang bei der Frequenz null die Fläche unter der Impulsantwort ist.
:::
:::karte formel Wiener-Lee für stationäre Prozesse
Wie hängen AKF und Leistungsdichtespektrum am Ausgang eines LTI-Systems mit denen eines stationären Eingangsprozesses zusammen?
---
$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau)$ und $\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2$, mit der Impuls-AKF $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ der Impulsantwort.
--- falsch
$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*h(\tau)$ und $\Phi_{gg}(f)=\Phi_{ss}(f)\,H(f)$: Die AKF wird wie ein Signal mit der Impulsantwort gefaltet, und das Leistungsdichtespektrum erhält dabei die Phase des Systems.
--- falsch
$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)\,\varphi^E_{hh}(\tau)$ und $\Phi_{gg}(f)=\Phi_{ss}(f)*|H(f)|^2$: Im Zeitbereich multipliziert man die beiden AKFs, im Frequenzbereich faltet man die beiden Spektren.
--- falsch
$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau)$ und $\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|$: Das Leistungsdichtespektrum wird mit dem Betrag des Frequenzgangs multipliziert, wie die Amplitude eines Kosinus.
:::
:::karte herleitung Wiener-Lee für stationäre Prozesse
Wie folgt aus den Faltungsintegralen für $g(t)$ und $g(t+\tau)$, dass $\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$ ist?
---
Man schreibt beide Faltungsintegrale mit verschiedenen Variablen aus, $g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta$, weil jeder Faktor seine eigene Integrationsvariable braucht.
---
Man zieht den Erwartungswert ins Doppelintegral, weil er linear ist und nur die Signalwerte zufällig sind, die Impulsantwort aber fest.
---
Bei Stationarität ist $\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$, weil die AKF nur vom Abstand der beiden Zeitpunkte abhängt.
---
Mit $\vartheta=\beta-\alpha$ steht innen das Integral $\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha$, also die Impuls-AKF $\varphi^E_{hh}(\vartheta)$, weil nur noch $h$ von $\alpha$ abhängt; außen bleibt die Faltung $\varphi_{ss}*\varphi^E_{hh}$.
---
Im Frequenzbereich wird daraus $\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2$, weil die Faltung zum Produkt wird und die Impuls-AKF das Spektrum $|H|^2$ hat.
:::
:::karte begriff Leistungsdichtespektrum
Was gibt das Leistungsdichtespektrum $\Phi_{ss}(f)$ eines stationären Prozesses an, und wie hängt es mit der AKF zusammen?
---
Wie sich die Leistung des Prozesses auf die Frequenzen verteilt. Es ist die Fourier-Transformierte der AKF, $\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$, reell, nie negativ und bei reellen Signalen gerade.
--- falsch
Wie sich die Leistung des Prozesses über die Zeit verteilt. Es ist die Fourier-Transformierte einer Musterfunktion selbst, im Allgemeinen komplex und bei reellen Signalen ungerade.
--- falsch
Wie sich die Leistung des Prozesses auf die Frequenzen verteilt. Es ist die Fourier-Transformierte der Verteilungsdichte, reell, nie negativ und bei reellen Signalen gerade.
--- falsch
Wie sich die Energie einer einzelnen Musterfunktion auf die Frequenzen verteilt. Es ist das Betragsquadrat ihres Spektrums und ändert sich deshalb von Musterfunktion zu Musterfunktion.
:::
:::karte formel Leistung aus der Leistungsdichte
Wie erhält man die Leistung eines stationären Prozesses aus seinem Leistungsdichtespektrum?
---
$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f$: Die Leistung ist der Wert der AKF bei $\tau=0$ und zugleich die Fläche unter der Leistungsdichte.
--- falsch
$L_s=\Phi_{ss}(0)$: Die Leistung ist der Wert der Leistungsdichte bei der Frequenz null, so wie die Leistung auch der Wert der AKF bei $\tau=0$ ist.
--- falsch
$L_s=\int_{-\infty}^{\infty}\Phi_{ss}^2(f)\,\mathrm{d} f$: Die Leistung ist die Fläche unter dem Quadrat der Leistungsdichte, weil die Leistung quadratisch vom Signal abhängt.
--- falsch
$L_s=\max_f\Phi_{ss}(f)$: Die Leistung ist der größte Wert der Leistungsdichte, weil bei dieser Frequenz die meiste Leistung des Prozesses konzentriert ist.
:::
:::karte zusammenhang Phase des Systems
Warum spielt die Phase eines LTI-Systems für das Leistungsdichtespektrum am Ausgang keine Rolle?
---
Weil das System die Leistung bei jeder Frequenz mit $|H(f)|^2$ multipliziert, und in diesem Betragsquadrat kommt die Phase von $H(f)$ nicht mehr vor. Das ist dieselbe Regel wie für Energiesignale.
--- falsch
Weil stationäre Prozesse keine Phase haben: Ihre Musterfunktionen sind symmetrisch um $t=0$, ihr Spektrum ist deshalb reell, und jede Phasenverschiebung fällt von selbst heraus.
--- falsch
Weil LTI-Systeme die Phase eines Zufallssignals nur um ganze Vielfache von $2\pi$ drehen können; solche Drehungen ändern kein Signal und damit auch keine Leistung.
--- falsch
Weil das Leistungsdichtespektrum nur die Frequenz null betrachtet, bei der jede Phase null ist. Bei allen anderen Frequenzen würde die Phase sehr wohl eine Rolle spielen.
:::
:::karte formel Strenge Definition der Leistungsdichte
Wie definiert man das Leistungsdichtespektrum streng genommen, und was besagt dann das Wiener-Khintchine-Theorem?
---
Als Grenzwert $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ über die Kurzzeitspektren $S_T$ von Ausschnitten der Dauer $T$. Das Theorem sagt, dass dieser Grenzwert dasselbe ist wie die Fourier-Transformierte der AKF.
--- falsch
Als Grenzwert $\lim_{T\to\infty}\mathrm E\{|S_T(f)|^2\}$ über die Kurzzeitspektren $S_T$ von Ausschnitten der Dauer $T$, ohne Teilung durch $T$. Das Theorem sagt, dass dieser Grenzwert stets endlich bleibt.
--- falsch
Als Betragsquadrat $|S(f)|^2$ des Spektrums einer einzigen, unendlich langen Musterfunktion. Das Theorem sagt, dass dieses Spektrum für alle Musterfunktionen des Prozesses gleich ist.
--- falsch
Als Grenzwert $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ über die Kurzzeitspektren $S_T$ von Ausschnitten der Dauer $T$. Das Theorem sagt, dass dieser Grenzwert die Fourier-Transformierte der Verteilungsdichte ist.
:::
:::karte zusammenhang Mittelwert hinter Tiefpass und Hochpass
Welche Mittelwerte haben die Ausgänge eines RC-Tiefpasses und eines CR-Hochpasses, wenn ein Rauschen mit dem Mittelwert 1 V hindurchläuft, und warum?
---
Am Tiefpass 1 V, weil $H(0)=1$ ist; am Hochpass 0, weil $H(0)=0$ ist. Der Kondensator lässt keinen Gleichstrom durch, der Gleichanteil wird gesperrt.
--- falsch
An beiden 1 V, weil ein LTI-System den Mittelwert eines Zufallssignals nie verändert; gefiltert werden nur die Schwankungen um den Mittelwert.
--- falsch
Am Tiefpass 0, weil er den Mittelwert über den Kondensator nach Masse ableitet; am Hochpass 1 V, weil er nur die schnellen Schwankungen sperrt.
--- falsch
An beiden etwa 0,5 V, weil jedes RC-Glied den Gleichanteil zwischen Widerstand und Kondensator halbiert, gleichgültig, wie die beiden geschaltet sind.
:::
:::karte zusammenhang Rauschen hinter einem schmalen Tiefpass
Warum schwankt ein breitbandiges Rauschen hinter einem RC-Tiefpass mit $1/(2\pi RC)=0{,}16$ Hz viel weniger als am Eingang?
---
Weil der Tiefpass von der breiten Leistungsdichte nur etwa den Teil unter 0,16 Hz durchlässt und die Leistung die Fläche unter der Leistungsdichte ist. Am Ausgang bleibt deshalb wenig Leistung.
--- falsch
Weil der Tiefpass den Mittelwert des Rauschens auf null setzt; ohne Gleichanteil sind die Schwankungen am Ausgang automatisch kleiner, gleichgültig, welche Frequenzen das Rauschen enthält.
--- falsch
Weil der Kondensator die Spitzenwerte des Rauschens speichert und später wieder abgibt; die Leistungsdichte bleibt dabei gleich, nur die Spitzen werden zeitlich auseinandergezogen.
--- falsch
Weil der Tiefpass die Phase der hohen Frequenzen so dreht, dass sie sich gegenseitig auslöschen; ihre Leistung bleibt im Leistungsdichtespektrum am Ausgang aber vollständig erhalten.
:::
::::
