---
title: Stufe 3: Korrelationsfunktion und Korrelationsprodukt
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
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

::::formelsammlung
**Korrelationsfunktion für Energiesignale**

$$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t=s^*(-\tau)*g(\tau)$$

$g$ wird um $\tau$ nach links geschoben, dann das Integral des Produkts gebildet. Für $g=s$ Autokorrelationsfunktion (AKF) $\varphi^E_{ss}(\tau)$, sonst Kreuzkorrelationsfunktion (KKF); geteilt durch $\sqrt{E_sE_g}$ normiert. Die rechte Seite ist das Korrelationsprodukt: Faltung mit dem gespiegelten, konjugierten Signal.

**Symmetrie**

$$\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau),\qquad\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)$$

Vertauschen der Signale spiegelt und konjugiert die KKF. Die AKF eines reellen Signals ist gerade.

**Maximum der AKF**

$$|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s$$

Am ähnlichsten ist ein Signal sich selbst ohne Verschiebung. Ein zeitbegrenztes Signal hat eine AKF der doppelten Dauer.

**AKF des Rechtecks**

$$\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$$

Das Dreieck mit dem Maximum $E_s=1$ bei $\tau=0$, doppelt so breit wie das Rechteck.
::::

::::lernkarten
:::karte formel Korrelationsfunktion für Energiesignale
Wie ist die Korrelationsfunktion $\varphi^E_{sg}(\tau)$ zweier Energiesignale definiert, und was tut man dabei für jede Verschiebung $\tau$?
---
$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t$: Man schiebt $g$ um $\tau$ nach links und bildet das Integral des Produkts mit $s^*$. So vergleicht man die Signale bei jeder Verschiebung.
--- falsch
$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(\tau-t)\,\mathrm{d} t$: Man spiegelt $g$, schiebt es um $\tau$ und bildet das Integral des Produkts, genau wie bei der Faltung.
--- falsch
$\varphi^E_{sg}(\tau)=s^*(\tau)\,g(t+\tau)$: Man multipliziert die beiden Signale bei der Verschiebung $\tau$, ohne zu integrieren; der Wert hängt deshalb von $t$ und von $\tau$ ab.
--- falsch
$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t$: Man schiebt $g$ um $\tau$ nach rechts und bildet das Integral des Produkts; kommt $g$ später als $s$, liegt das Maximum deshalb bei negativem $\tau$.
:::
:::karte begriff Autokorrelationsfunktion
Was ist die Autokorrelationsfunktion (AKF) eines Energiesignals $s$, und welchen Wert hat sie bei $\tau=0$?
---
Die Korrelationsfunktion $\varphi^E_{ss}(\tau)$ des Signals mit sich selbst, also der Fall $g=s$. Bei $\tau=0$ ist sie die Energie $E_s$ des Signals.
--- falsch
Die Korrelationsfunktion $\varphi^E_{sg}(\tau)$ zweier verschiedener Signale $s$ und $g$. Bei $\tau=0$ ist sie der Korrelationskoeffizient $p_{sg}$ der beiden Signale.
--- falsch
Die Faltung $s(\tau)*s(\tau)$ des Signals mit sich selbst. Bei $\tau=0$ ist sie null, weil sich das Signal dort mit seinem Spiegelbild genau aufhebt.
--- falsch
Die Korrelationsfunktion $\varphi^E_{ss}(\tau)$ des Signals mit sich selbst. Bei $\tau=0$ ist sie stets 1, weil jedes Signal sich selbst vollkommen gleicht, gleich wie groß es ist.
:::
:::karte begriff Kreuzkorrelationsfunktion
Was bezeichnet man als Kreuzkorrelationsfunktion (KKF), und wozu nutzt man sie etwa beim Radar?
---
Die Korrelationsfunktion $\varphi^E_{sg}(\tau)$ zweier verschiedener Signale $s$ und $g$. Beim Radar vergleicht sie Sendeimpuls und Empfangssignal; ihr Maximum liegt bei der Verzögerung des Echos.
--- falsch
Die Korrelationsfunktion $\varphi^E_{ss}(\tau)$ eines Signals mit sich selbst. Beim Radar zeigt ihr Maximum bei $\tau=0$, dass das Echo ohne Verzögerung zurückkommt.
--- falsch
Die Faltung $s*g$ zweier verschiedener Signale. Beim Radar ist sie die Impulsantwort der Übertragungsstrecke, und ihr Maximum liegt immer bei $\tau=0$.
--- falsch
Die Korrelationsfunktion zweier verschiedener Signale, geteilt durch $\sqrt{E_sE_g}$. Beim Radar zeigt die Höhe ihres Maximums die Entfernung des Ziels, die Lage des Maximums die Dämpfung des Echos.
:::
:::karte begriff Korrelationsprodukt
Was versteht man unter dem Korrelationsprodukt zweier Signale $s$ und $g$?
---
Die Korrelationsfunktion, geschrieben als Faltung mit dem gespiegelten, konjugierten Signal: $\varphi^E_{sg}(\tau)=s^*(-\tau)*g(\tau)$. Deshalb gelten für sie alle Rechenregeln der Faltung.
--- falsch
Das Produkt $s^*(\tau)\,g(\tau)$ der beiden Signale ohne Integral: Man multipliziert sie Punkt für Punkt, und die Korrelationsfunktion ist dann die Fläche unter diesem Produkt bis zur Stelle $\tau$.
--- falsch
Die Faltung $s(\tau)*g(\tau)$ der beiden Signale ohne Spiegeln und Konjugieren: Korrelation und Faltung sind dasselbe, nur unter einem anderen Namen.
--- falsch
Die Faltung mit dem gespiegelten Signal ohne Konjugation, $s(-\tau)*g(\tau)$: Die Konjugation entfällt, weil sie beim Spiegeln eines Signals von selbst entsteht.
:::
:::karte herleitung Korrelation als Faltung
Wie zeigt man ausgehend von $\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t$, dass die Korrelationsfunktion die Faltung $s^*(-\tau)*g(\tau)$ ist?
---
Man setzt $t=-\vartheta$, weil dann im zweiten Signal $t+\tau$ zu $\tau-\vartheta$ wird, der Form, die im Faltungsintegral steht.
---
Man erhält $\int s^*(-\vartheta)\,g(\tau-\vartheta)\,\mathrm{d}\vartheta$, weil sich beim Substituieren die Grenzen vertauschen und das Minuszeichen aus der Ableitung sie wieder zurückdreht.
---
Das ist das Faltungsintegral von $s^*(-\tau)$ mit $g(\tau)$, weil das erste Signal an der Stelle $\vartheta$ mit dem zweiten an der Stelle $\tau-\vartheta$ multipliziert und über $\vartheta$ integriert wird.
---
Also ist $\varphi^E_{sg}(\tau)=s^*(-\tau)*g(\tau)$: Korrelation ist Faltung mit dem gespiegelten, konjugierten Signal, weil das erste Signal gespiegelt und konjugiert in die Faltung eingeht.
:::
:::karte formel Symmetrie der Korrelationsfunktionen
Wie hängen $\varphi^E_{gs}(\tau)$ und $\varphi^E_{sg}(\tau)$ zusammen, und welche Symmetrie folgt daraus für die AKF eines reellen Signals?
---
$\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$: Vertauscht man die Signale, wird die KKF gespiegelt und konjugiert. Für $g=s$ folgt $\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)$; bei reellem $s$ ist die AKF also gerade.
--- falsch
$\varphi^E_{gs}(\tau)=\varphi^E_{sg}(\tau)$: Die Reihenfolge der Signale spielt keine Rolle, weil das Produkt zweier Signale kommutativ ist. Deshalb ist auch jede AKF gerade, ob das Signal reell ist oder nicht.
--- falsch
$\varphi^E_{gs}(\tau)=-\varphi^E_{sg}(\tau)$: Vertauscht man die Signale, kehrt sich das Vorzeichen um. Für $g=s$ ist die AKF deshalb eine ungerade Funktion von $\tau$.
--- falsch
$\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$: Vertauscht man die Signale, wird die KKF gespiegelt und konjugiert. Die AKF eines reellen Signals ist deshalb eine ungerade Funktion von $\tau$.
:::
:::karte formel Maximum der AKF
Wo hat die AKF eines Energiesignals ihr Maximum, und welchen Wert hat sie dort?
---
Bei $\tau=0$: $|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s$. Am ähnlichsten ist ein Signal sich selbst ohne Verschiebung, und dort ist die AKF seine Energie.
--- falsch
Bei $\tau=0$ mit dem Wert 1: Jedes Signal stimmt mit sich selbst vollkommen überein, deshalb ist die AKF dort immer genau 1, gleich wie groß das Signal ist.
--- falsch
Bei einer Verschiebung um die halbe Signaldauer: Dort überlappt das verschobene Signal am stärksten mit dem ursprünglichen, und der Wert ist die halbe Energie.
--- falsch
Dort, wo das Signal selbst sein Maximum hat; ihr Wert ist das Quadrat dieses Höchstwerts, also $\max|s(t)|^2$, weil die AKF Betragsquadrate vergleicht.
:::
:::karte formel AKF des Rechtecks
Welche AKF hat der Rechteckimpuls $\operatorname{rect}(t)$, und wie breit ist sie im Vergleich zum Rechteck?
---
$\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$, das Dreieck mit dem Maximum $E_s=1$ bei $\tau=0$. Es ist doppelt so breit wie das Rechteck: Ein zeitbegrenztes Signal hat eine AKF der doppelten Dauer.
--- falsch
$\varphi^E_{ss}=\operatorname{rect}(\tau)$: Das Rechteck stimmt bei jeder Verschiebung innerhalb seiner Breite vollständig mit sich überein, deshalb ist die AKF wieder ein Rechteck derselben Breite.
--- falsch
$\varphi^E_{ss}=\Lambda(\tau)$ mit derselben Breite wie das Rechteck: Die AKF ist nur dort von null verschieden, wo auch das Rechteck selbst von null verschieden ist.
--- falsch
$\varphi^E_{ss}=\Lambda(\tau/2)$ mit der vierfachen Breite: Spiegeln und Verschieben verdoppeln die Dauer jeweils, deshalb wird die AKF viermal so breit wie das Rechteck.
:::
:::karte zusammenhang Ein Echo finden
Woran erkennt man in der KKF zwischen dem Sendeimpuls $\operatorname{rect}(t)$ und dem Echo $0{,}5\operatorname{rect}(t-3)$ die Verzögerung und die Dämpfung des Echos?
---
Die KKF ist $\varphi^E_{sg}(\tau)=0{,}5\,\Lambda(\tau-3)$. Ihr Maximum liegt bei $\tau=3$, der Verzögerung, und seine Höhe $0{,}5=0{,}5\cdot E_s$ gibt die Dämpfung an.
--- falsch
Die KKF ist $0{,}5\,\Lambda(\tau+3)$. Ihr Maximum liegt bei $\tau=-3$, weil man das Echo um drei Einheiten zurückschieben muss; seine Höhe gibt die Dämpfung an.
--- falsch
Die KKF ist $\varphi^E_{sg}(\tau)=0{,}5\,\Lambda(\tau-3)$. Die Breite des Dreiecks gibt die Verzögerung des Echos an, die Lage seines Maximums die Dämpfung.
--- falsch
Die KKF ist $0{,}25\,\Lambda(\tau-3)$. Ihr Maximum liegt bei $\tau=3$, und seine Höhe ist das Quadrat der Dämpfung, weil die Korrelation Energien miteinander vergleicht.
:::
:::karte zusammenhang Faltung und Korrelation
Worin unterscheiden sich Faltung und Korrelation, obwohl ihre Integrale fast gleich aussehen?
---
Bei der Faltung $\int s(\tau)h(t-\tau)\mathrm{d}\tau$ läuft das zweite Signal rückwärts, bei der Korrelation laufen beide vorwärts: Man legt zwei Formen übereinander. Rechnerisch ist der Unterschied genau das Spiegeln.
--- falsch
Bei der Korrelation läuft das zweite Signal rückwärts, bei der Faltung laufen beide vorwärts. Deshalb ist die Faltung eine Korrelation mit dem gespiegelten Signal und nicht umgekehrt.
--- falsch
Die Faltung gilt nur für LTI-Systeme, die Korrelation nur für Energiesignale; rechnerisch sind beide Integrale gleich, sie unterscheiden sich nur in ihrer Anwendung und in ihrem Namen.
--- falsch
Bei der Korrelation wird das Produkt der beiden Signale nicht integriert, sondern nur an der Stelle $\tau$ gebildet; deshalb braucht sie kein Spiegeln und ist schneller zu berechnen als eine Faltung.
:::
:::karte zusammenhang Wiederholung in der AKF
Woran erkennt man in der AKF des Signals $s(t)=\operatorname{rect}(t)+\operatorname{rect}(t-2)$, dass sich ein Rechteck wiederholt?
---
An den Nebenspitzen bei $\tau=\pm2$: $\varphi^E_{ss}(\tau)=2\Lambda(\tau)+\Lambda(\tau-2)+\Lambda(\tau+2)$. Dort liegt jeweils ein Rechteck über dem anderen; bei $\tau=0$ liegen beide übereinander, das gibt die Höhe $2=E_s$.
--- falsch
An einer einzigen Nebenspitze bei $\tau=2$: Die AKF ist $\Lambda(\tau)+\Lambda(\tau-2)$ und zeigt nur positive Verschiebungen, weil das zweite Rechteck später kommt als das erste.
--- falsch
An drei gleich hohen Spitzen bei $\tau=0$ und $\tau=\pm2$: Jede Überdeckung zweier Rechtecke liefert dieselbe Höhe 1, gleich wie viele Rechtecke gerade übereinanderliegen.
--- falsch
An der doppelten Breite der Hauptspitze bei $\tau=0$: Zwei Rechtecke im Abstand 2 verbreitern das Dreieck; Nebenspitzen gibt es nicht, weil sich die beiden Rechtecke nirgends berühren.
:::
:::karte zusammenhang Gleitender Integrator
Warum liefert ein Filter, das in jedem Moment über die letzte Sekunde integriert, die KKF eines Empfangssignals $g$ mit dem Rechteck $\operatorname{rect}(t)$?
---
Es bildet $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$, und das ist die KKF mit $s=\operatorname{rect}(t)$, um 0,5 s verzögert: $y(t)=\varphi^E_{sg}(t-0{,}5)$. Das Filter rechnet sie für alle $\tau$, während das Signal hereinkommt.
--- falsch
Es bildet $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$, und das ist die AKF von $g$ ohne Verzögerung, weil das Integral über die letzte Sekunde das Signal $g$ mit sich selbst vergleicht.
--- falsch
Es bildet die Differenz zum Wert eine Sekunde zuvor, $g(t)-g(t-1)$; diese Differenz ist genau dann null, wenn das Echo und das Rechteck übereinstimmen.
--- falsch
Es bildet das laufende Integral $\int_{-\infty}^{t}g(u)\,\mathrm{d} u$, und dessen Wert am Ende des Echos ist die KKF bei der Verschiebung null; andere Verschiebungen liefert das Filter nicht.
:::
::::
