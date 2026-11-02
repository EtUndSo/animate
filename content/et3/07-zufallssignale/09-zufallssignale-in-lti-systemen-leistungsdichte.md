---
title: Stufe 8: Zufallssignale in LTI-Systemen, Leistungsdichte
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Zufallssignale
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

Im Frequenzbereich wird $\varphi^E_{hh}$ zu $|H|^2$ ([Teil 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).
:::

⁠**So liest man das:** $\Phi_{ss}(f)$ gibt an, wie sich die Leistung auf die Frequenzen verteilt. Es ist reell, nie negativ und bei reellen Signalen gerade. Ein LTI-System multipliziert die Leistung bei jeder Frequenz mit $|H(f)|^2$, seine Phase spielt keine Rolle. Das ist dieselbe Regel wie für Energiesignale in [Teil 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html), jetzt für Prozesse. (Zusatz: Streng genommen definiert man $\Phi_{ss}$ als Grenzwert $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$ über Kurzzeitspektren von Ausschnitten der Dauer $T$. Dass das dasselbe ist wie die Transformierte der AKF, ist die eigentliche Aussage des Wiener-Khintchine-Theorems.)

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
