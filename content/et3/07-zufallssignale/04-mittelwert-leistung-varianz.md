---
title: Stufe 3: Mittelwert, Leistung, Varianz
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Zufallssignale
order: 3270400
summary: Die wichtigsten Mittelwerte erster Ordnung und ihre anschauliche Bedeutung.
tags: Gleichanteil, Leistung, Varianz, Wechselleistung, Standardabweichung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die wichtigsten Mittelwerte erster Ordnung und ihre anschauliche Bedeutung.
:::

Der Erwartungswert ist linear: $\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$, für beliebige Zufallsgrößen. Bei stationären Prozessen definiert man:

<span class="anker" id="gl-3-1"></span>
$$m_s=\mathrm E\{s(t)\},\qquad L_s=\mathrm E\{s^2(t)\},\qquad\sigma_s^2=L_s-m_s^2. \tag{3.1}$$

⁠**So liest man das:** Bei einem ergodischen Prozess ist $m_s$ das Zeitmittel, also der __Gleichanteil__ des Signals, und $L_s$ der quadratische Zeitmittelwert, die __Leistung__ ([Teil 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). Die __Varianz__ $\sigma_s^2$ ist die Leistung minus die Leistung des Gleichanteils, also die __Wechselleistung__. Ihre Wurzel, die __Standardabweichung__ $\sigma_s$, ist der Effektivwert des Wechselanteils. Ein Multimeter auf AC zeigt $\sigma_s$, auf DC zeigt es $m_s$.

:::aufgabe Aufgabe 1 ★ Mittelwerte eines Signals
<span class="anker" id="aufg-1"></span>

Ein ergodisches Signal hat den Gleichanteil 2 V und einen Effektivwert (alles zusammen, „true RMS“) von 2,5 V. Wie groß sind die normierte Leistung, die Varianz und die Standardabweichung?

:::loesung
$L_s=2{,}5^2=6{,}25$ V$^2$, $\sigma_s^2=L_s-m_s^2=6{,}25-4=2{,}25$ V$^2$, $\sigma_s=1{,}5$ V. Ein AC-Messgerät zeigt 1,5 V.
:::
:::
