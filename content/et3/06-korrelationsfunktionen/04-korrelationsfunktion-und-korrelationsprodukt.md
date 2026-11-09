---
title: Stufe 3: Korrelationsfunktion und Korrelationsprodukt
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Korrelationsfunktionen
order: 3260400
summary: Ein Echo ist dem Sendeimpuls ähnlich, aber verschoben.
tags: Autokorrelationsfunktion, Kreuzkorrelationsfunktion, Korrelationsprodukt
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Ein Echo ist dem Sendeimpuls ähnlich, aber verschoben. Man vergleicht deshalb für jede Verschiebung $\tau$.
:::

:::definition Definition 3.1 (Korrelationsfunktion für Energiesignale)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t=s^*(-\tau)*g(\tau). \tag{3.1}$$

Für $g=s$ heißt sie __Autokorrelationsfunktion__ (AKF) $\varphi^E_{ss}(\tau)$, sonst __Kreuzkorrelationsfunktion__ (KKF). Geteilt durch $\sqrt{E_sE_g}$ heißt sie normiert.
:::

⁠**So liest man das:** Man schiebt $g$ um $\tau$ nach links und bildet das Integral des Produkts. Das zweite Gleichheitszeichen ist der Kern: Korrelation ist Faltung mit dem gespiegelten, konjugierten Signal. Deshalb heißt sie auch __Korrelationsprodukt__. Im Unterschied zur Faltung wird hier nicht gespiegelt, beide Signale laufen in dieselbe Richtung.

:::herleitung Korrelation als Faltung
In [(3.1)](#gl-3-1) $t=-\vartheta$ setzen: $\int s^*(-\vartheta)\,g(\tau-\vartheta)\,\mathrm{d}\vartheta$. Das ist das Faltungsintegral von $s^*(-\tau)$ mit $g(\tau)$.
:::

:::satz Satz 3.2 (Eigenschaften der Korrelationsfunktionen)
<span class="anker" id="satz-3-2"></span>

<span class="anker" id="gl-3-2"></span>
<span class="anker" id="gl-3-3"></span>
$$\begin{aligned} &\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau),\qquad\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)\ \ (\text{bei reellem }s\text{ gerade}),\\ &|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s. \end{aligned} \tag{3.2|3.3}$$

Ein zeitbegrenztes Signal hat eine AKF der doppelten Dauer.
:::

⁠**So liest man das:** Am ähnlichsten ist ein Signal sich selbst ohne Verschiebung, und dort ist die AKF seine Energie. Die AKF eines Rechtecks ist das Dreieck: $\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$, doppelt so breit wie das Rechteck (Abb. [1](#abb-1) links).

::::beispiel ein Echo finden
Gesendet wird $s=\operatorname{rect}(t)$, empfangen das abgeschwächte, verzögerte Echo $g=0{,}5\operatorname{rect}(t-3)$. Die KKF ist $\varphi^E_{sg}(\tau)=0{,}5\,\Lambda(\tau-3)$: Ihr Maximum liegt bei $\tau=3$, der Verzögerung, und seine Höhe $0{,}5=0{,}5\cdot E_s$ gibt die Dämpfung an (Abb. [1](#abb-1) rechts). So misst ein Radar die Entfernung.

:::abbildung et3/k6korr 1
Links: Die AKF des Rechtecks ist das Dreieck, Maximum $=E_s=1$ bei $\tau=0$, doppelte Breite. Rechts: Die KKF zwischen Sendeimpuls und Echo $0{,}5\operatorname{rect}(t-3)$ hat ihr Maximum bei der Verzögerung $\tau=3$.
:::
::::

:::frage Faltung und Korrelation sehen fast gleich aus. Wo ist der Unterschied?
Bei der Faltung $\int s(\tau)h(t-\tau)\mathrm{d}\tau$ läuft das zweite Signal rückwärts ($-\tau$): Das System „erinnert“ sich an die Vergangenheit. Bei der Korrelation $\int s^*(t)g(t+\tau)\mathrm{d} t$ laufen beide vorwärts: Man legt zwei Formen deckungsgleich übereinander und misst die Übereinstimmung. Rechnerisch ist der Unterschied genau das Spiegeln, deshalb ist Korrelation Faltung mit dem gespiegelten Signal.
:::

:::ltspice Ein Echo mit einem gleitenden Integrator finden
Ein Filter, das in jedem Moment über die letzte Sekunde integriert, bildet $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$. Mit $s=\operatorname{rect}(t)$ ist das genau die KKF [(3.1)](#gl-3-1), um 0,5 s verzögert: $y(t)=\varphi^E_{sg}(t-0{,}5)$. Das Filter rechnet sie für alle $\tau$, während das Signal hereinkommt.

⁠**Zeichnen:** Quelle `voltage` am Netz `g` mit `PULSE(0 0.5 2.5 1u 1u 1)`, das Echo $0{,}5\operatorname{rect}(t-3)$. Zwei Verhaltensquellen `bv`: am Netz `int` mit `V=idt(V(g))` (laufendes Integral) und am Netz `y` mit `V=V(int)-delay(V(int),1)` (Integral über die letzte Sekunde).

⁠**Direktiven:** `.tran 0 6 0 1m`, `.meas tran ymax MAX V(y)`.

⁠**Was du siehst:** `V(y)` ist das Dreieck $0{,}5\,\Lambda(t-3{,}5)$ mit dem Maximum 0,5 bei $t=3{,}5$ s: die Verzögerung 3 s plus 0,5 s, weil das Filter erst am Ende des Echos fertig integriert hat. Die Höhe 0,5 ist die Dämpfung des Echos.

⁠**Zu Aufgabe [3](#aufg-3):** Eingang `PULSE(0 1 0 1u 1u 1 2 2)`, das Doppelrechteck, je 0,5 s später als im Text. Für `y` nimmst du

`V=V(int)-delay(V(int),1)+delay(V(int),2)-delay(V(int),3)`.

Dieses Filter integriert über zwei Fenster, die zum Doppelrechteck passen, und `V(y)` ist dessen AKF, um 3 s verschoben. Vergleiche mit deinem Ergebnis aus Aufgabe [3](#aufg-3)(a).
:::

:::aufgabe Aufgabe 3 ★★ Echo und Wiederholung
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Ein Signal besteht aus zwei Rechtecken: $s(t)=\operatorname{rect}(t)+\operatorname{rect}(t-2)$. Bestimme seine AKF. Woran sieht man die Wiederholung?

</li>

<li>

Prüfe [(3.3)](#gl-3-3) für dieses Signal.

</li>

</ol>

:::loesung
(a) Mit $\operatorname{rect}(-\tau)=\operatorname{rect}(\tau)$ und $\operatorname{rect}*\operatorname{rect}=\Lambda$ ergeben die vier Teilprodukte

$$\varphi^E_{ss}(\tau)=2\Lambda(\tau)+\Lambda(\tau-2)+\Lambda(\tau+2).$$

Die Nebenspitzen bei $\tau=\pm2$ zeigen den Abstand der Wiederholung. Dort liegt jeweils eines der beiden Rechtecke über dem anderen. Bei $\tau=0$ liegen beide übereinander, das gibt die doppelte Höhe.

(b) $\varphi^E_{ss}(0)=2=E_s=1+1$, und die Nebenspitzen haben nur den Wert 1.
:::
:::
