---
title: Stufe 3: Mittelwert, Leistung, Varianz
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
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

⁠**So liest man das:** Bei einem ergodischen Prozess ist $m_s$ das Zeitmittel, also der __Gleichanteil__ des Signals, und $L_s$ der quadratische Zeitmittelwert, die __Leistung__ ([Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). Die __Varianz__ $\sigma_s^2$ ist die Leistung minus die Leistung des Gleichanteils, also die __Wechselleistung__. Ihre Wurzel, die __Standardabweichung__ $\sigma_s$, ist der Effektivwert des Wechselanteils. Ein Multimeter auf AC zeigt $\sigma_s$, auf DC zeigt es $m_s$.

:::aufgabe Aufgabe 1 ★ Mittelwerte eines Signals
<span class="anker" id="aufg-1"></span>

Ein ergodisches Signal hat den Gleichanteil 2 V und einen Effektivwert (alles zusammen, „true RMS“) von 2,5 V. Wie groß sind die normierte Leistung, die Varianz und die Standardabweichung?

:::loesung
$L_s=2{,}5^2=6{,}25$ V$^2$, $\sigma_s^2=L_s-m_s^2=6{,}25-4=2{,}25$ V$^2$, $\sigma_s=1{,}5$ V. Ein AC-Messgerät zeigt 1,5 V.
:::
:::

::::formelsammlung
**Linearität des Erwartungswerts**

$$\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$$

Für beliebige Zufallsgrößen.

**Mittelwert, Leistung, Varianz**

$$m_s=\mathrm E\{s(t)\},\qquad L_s=\mathrm E\{s^2(t)\},\qquad\sigma_s^2=L_s-m_s^2$$

Für stationäre Prozesse. Bei ergodischen ist $m_s$ der Gleichanteil (Anzeige auf DC), $L_s$ die Leistung, $\sigma_s^2$ die Wechselleistung und die Standardabweichung $\sigma_s$ der Effektivwert des Wechselanteils (Anzeige auf AC).
::::

::::lernkarten
:::karte formel Linearität des Erwartungswerts
Welche Rechenregel gilt für den Erwartungswert einer gewichteten Summe von Zufallsgrößen, und für welche Zufallsgrößen gilt sie?
---
$\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$: Der Erwartungswert ist linear, und zwar für beliebige Zufallsgrößen, ohne weitere Voraussetzung über ihren Zusammenhang.
--- falsch
$\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$: Der Erwartungswert ist linear, aber nur für unabhängige Zufallsgrößen; hängen sie zusammen, kommen noch Kreuzterme hinzu.
--- falsch
$\mathrm E\{\sum_ia_is_i\}=\sum_ia_i^2\mathrm E\{s_i\}$: Die Gewichte gehen quadratisch ein, weil der Erwartungswert über die Leistung der Zufallsgrößen gebildet wird.
--- falsch
$\mathrm E\{\sum_ia_is_i\}=\prod_ia_i\mathrm E\{s_i\}$: Der Erwartungswert einer Summe ist das Produkt der gewichteten Einzelwerte, sofern die Zufallsgrößen unabhängig sind.
:::
:::karte formel Mittelwert, Leistung und Varianz
Wie sind Mittelwert, Leistung und Varianz eines stationären Prozesses über Erwartungswerte definiert?
---
$m_s=\mathrm E\{s(t)\}$, $L_s=\mathrm E\{s^2(t)\}$ und $\sigma_s^2=L_s-m_s^2$: Der Mittelwert ist der Erwartungswert des Signals, die Leistung der seines Quadrats, die Varianz die Leistung minus das Quadrat des Mittelwerts.
--- falsch
$m_s=\mathrm E\{s(t)\}$, $L_s=m_s^2$ und $\sigma_s^2=\mathrm E\{s^2(t)\}$: Die Leistung ist das Quadrat des Mittelwerts, die Varianz der Erwartungswert des Quadrats, also das, was über den Gleichanteil hinaus übrig bleibt.
--- falsch
$m_s=\mathrm E\{s(t)\}$, $L_s=\mathrm E\{s^2(t)\}$ und $\sigma_s^2=L_s+m_s^2$: Die Varianz ist die Summe aus der Leistung und der Leistung des Gleichanteils, also die gesamte Leistung des Signals.
--- falsch
$m_s=\mathrm E\{s(t)\}$, $L_s=\mathrm E\{s^2(t)\}$ und $\sigma_s^2=L_s-m_s$: Die Varianz ist die Leistung minus den Mittelwert, weil man den Gleichanteil vom Signal abzieht, bevor man quadriert.
:::
:::karte zusammenhang Gleichanteil
Warum darf man den Mittelwert $m_s$ eines ergodischen Prozesses als Gleichanteil des Signals deuten?
---
Weil bei Ergodizität das Scharmittel $m_s$ gleich dem Zeitmittel einer Musterfunktion ist, und das Zeitmittel eines Signals ist sein Gleichanteil. Ein Multimeter auf DC zeigt deshalb $m_s$.
--- falsch
Weil der Mittelwert eines stationären Prozesses stets null ist und ein Signal ohne Gleichanteil ebenfalls den Mittelwert null hat. Ein Multimeter auf DC zeigt deshalb immer null.
--- falsch
Weil $m_s$ der kleinste Wert ist, den das Signal annimmt, und der Gleichanteil die Grundlinie ist, über der es schwankt. Ein Multimeter auf DC zeigt deshalb das Minimum des Signals.
--- falsch
Weil bei Ergodizität jede Musterfunktion konstant ist und eine Konstante nur aus Gleichanteil besteht. Ein Multimeter auf DC zeigt deshalb den Wert jeder Musterfunktion.
:::
:::karte zusammenhang Leistung
Warum ist $L_s=\mathrm E\{s^2(t)\}$ bei einem ergodischen Prozess dasselbe wie die Leistung des gemessenen Signals?
---
Weil bei Ergodizität das Scharmittel von $s^2$ gleich dem quadratischen Zeitmittelwert einer Musterfunktion ist. Genau dieser quadratische Zeitmittelwert ist die mittlere Leistung eines Signals.
--- falsch
Weil bei Ergodizität das Quadrat des Mittelwerts gleich dem Mittelwert des Quadrats ist. Die Leistung eines ergodischen Signals ist deshalb stets das Quadrat seines Gleichanteils.
--- falsch
Weil $\mathrm E\{s^2(t)\}$ das Quadrat des größten Werts ist, den das Signal annimmt. Die Leistung eines Signals ist nämlich allein durch seinen Spitzenwert festgelegt.
--- falsch
Weil bei Ergodizität jede Musterfunktion dieselbe Energie hat. Die Leistung ist dann die Energie einer einzelnen Musterfunktion, gemittelt über die ganze Schar.
:::
:::karte begriff Varianz und Wechselleistung
Was gibt die Varianz $\sigma_s^2$ eines stationären Prozesses an, und warum nennt man sie auch Wechselleistung?
---
Die Leistung minus die Leistung des Gleichanteils: $\sigma_s^2=L_s-m_s^2$. Übrig bleibt die Leistung der Schwankungen um den Mittelwert, deshalb heißt sie Wechselleistung.
--- falsch
Die Leistung des Gleichanteils allein: $\sigma_s^2=m_s^2$. Sie heißt Wechselleistung, weil sie sich beim Wechsel des Messbereichs am Multimeter nicht ändert.
--- falsch
Die gesamte Leistung samt Gleichanteil: $\sigma_s^2=L_s$. Sie heißt Wechselleistung, weil man sie mit einem Multimeter in der Stellung AC vollständig misst.
--- falsch
Den Effektivwert der Schwankungen um den Mittelwert: $\sigma_s^2=\sqrt{L_s-m_s^2}$. Sie heißt Wechselleistung, weil sie die Größe der Wechselspannung unmittelbar angibt.
:::
:::karte begriff Standardabweichung
Was gibt die Standardabweichung $\sigma_s$ eines Signals anschaulich an, und in welcher Stellung zeigt ein Multimeter sie an?
---
Sie ist die Wurzel der Varianz $\sigma_s^2$, also der Effektivwert des Wechselanteils. Ein Multimeter auf AC zeigt $\sigma_s$, auf DC zeigt es den Mittelwert $m_s$.
--- falsch
Sie ist die Wurzel der Leistung $L_s$, also der Effektivwert des ganzen Signals. Ein Multimeter auf AC zeigt sie, auf DC zeigt es das Quadrat des Mittelwerts.
--- falsch
Sie ist die mittlere Abweichung vom Mittelwert, also $\mathrm E\{s(t)-m_s\}$. Ein Multimeter auf DC zeigt sie, weil der Gleichanteil dabei abgezogen wird.
--- falsch
Sie ist das Quadrat der Varianz, also die Leistung der Schwankungen. Ein Multimeter auf AC zeigt sie, auf DC zeigt es die gesamte Leistung $L_s$.
:::
:::karte zusammenhang Anzeige in der Stellung AC
Warum zeigt ein Multimeter auf AC bei einem Signal mit 2 V Gleichanteil und 2,5 V Gesamteffektivwert 1,5 V an und nicht 0,5 V?
---
Weil sich Leistungen subtrahieren, nicht Effektivwerte: $L_s=2{,}5^2=6{,}25$ V$^2$, $\sigma_s^2=L_s-m_s^2=6{,}25-4=2{,}25$ V$^2$, also $\sigma_s=1{,}5$ V. Gleich- und Wechselanteil addieren sich quadratisch.
--- falsch
Weil das Multimeter auf AC den Gleichanteil nicht abzieht, sondern zum Effektivwert addiert und das Ergebnis durch drei teilt: $(2+2{,}5)/3=1{,}5$ V.
--- falsch
Weil ein Multimeter auf AC den Spitzenwert anzeigt: Bei 2,5 V Effektivwert schwankt das Signal um 1,5 V um den Gleichanteil, gleichgültig, welche Form das Signal hat.
--- falsch
Weil sich zwar Effektivwerte subtrahieren, das Multimeter den Wert aber mit 3 multipliziert, um von der Spitze auf den Effektivwert umzurechnen: $3\cdot0{,}5=1{,}5$ V.
:::
::::
