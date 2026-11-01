---
title: Zufallssignale
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Zufallssignale
order: 3270100
summary: Mittelwerte, Verteilungen, Leistungsdichte, Rauschen in Systemen und der optimale Empfänger
tags: Musterfunktion, Zufallsprozess, Zufallsgröße, Erwartungswert, Autokorrelationsfunktion, stationär, ergodisch, Gleichanteil
lang: de
---

## Worum es geht

Das Rauschen eines Widerstands, Sprache, ein Datenstrom: Solche Signale kann man nicht vorhersagen. Ihren genauen Verlauf kennt man nicht, wohl aber ihre *Eigenschaften im Mittel*: wie groß sie typischerweise sind, wie schnell sie sich ändern, welche Frequenzen sie enthalten. Dieser Artikel zeigt, wie man solche Zufallssignale beschreibt, was ein LTI-System mit ihnen macht und wie man ein bekanntes Signal im Rauschen am sichersten erkennt.

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Ein Zufallssignal beschreibt man durch Mittelwerte: Mittelwert, Leistung, Varianz, Autokorrelationsfunktion und Verteilungsdichte. Bei ergodischen Prozessen darf man sie aus einem einzigen, langen Signal bestimmen.

</li>

<li>

Die Fourier-Transformierte der Autokorrelationsfunktion ist das Leistungsdichtespektrum. Ein LTI-System multipliziert es mit $|H(f)|^2$, genau wie bei Energiesignalen ([Teil 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).

</li>

<li>

Gegen weißes Rauschen ist das Korrelationsfilter $h(t)=s(T-t)$ optimal. Es erreicht das Signal-Rausch-Verhältnis $E_s/N_0$, unabhängig von der Signalform.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Man ersetzt das unbekannte Signal durch seine Mittelwerte, und für Mittelwerte gilt Linearität:

| Ergebnis | Woher es kommt |
|---|---|
| Mittelwert, Leistung, Varianz | Scharmittel und Zeitmittel (Stufen [1](#stufe-1)–[3](#stufe-3)) |
| AKF, Kovarianz, KKF | Mittel über Produkte zweier Zeitpunkte (Stufe [4](#stufe-4)) |
| Verteilungsdichte | Anteil der Zeit oder der Schar unter einer Schwelle (Stufe [5](#stufe-5)) |
| Summe unabhängiger Größen | Faltung der Dichten, daher Gauß (Stufen [6](#stufe-6), [7](#stufe-7)) |
| Leistungsdichte, Wiener-Lee | Linearität des Mittelwerts im Faltungsintegral (Stufe [8](#stufe-8)) |
| weißes Rauschen | konstante Leistungsdichte, AKF $=N_0\delta$ (Stufe [9](#stufe-9)) |
| Korrelationsfilter | Cauchy-Schwarz: Am größten ist die Korrelation mit sich selbst (Stufe [10](#stufe-10)) |
| Fehlerwahrscheinlichkeit | Fläche unter einer Gaußkurve jenseits der Schwelle (Stufe [11](#stufe-11)) |

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für diesen Artikel
<ul>

<li>

⁠**Gleichverteilte Zufallszahlen** zwischen $-\frac12$ und $\frac12$ (Varianz $\frac{1}{12}$), auch als zeitdiskretes weißes Rauschen.

</li>

<li>

⁠**Widerstand** $R=1\,\mathrm{k\Omega}$ bei 290 K, Bandbreite 20 kHz (Audio).

</li>

<li>

⁠**Rekursives System** $g(n)=s(n)+0{,}6\,g(n-1)$ aus [Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html).

</li>

</ul>

Die Zahlen rechnet `rechnung_kap7.py` nach, zum Teil zur Kontrolle mit simulierten Zufallszahlen.
:::

## Stufe 1: Der Zufallsprozess

<span class="anker" id="stufe-1"></span>

:::zweck
Wie beschreibt man ein Signal, dessen Verlauf man nicht kennt? Man stellt sich viele gleichartige Signale vor und mittelt über sie.
:::

**Die Idee.** Misst man das Rauschen an vielen gleich gebauten Widerständen bei gleicher Temperatur, bekommt man viele verschiedene Kurven ${}^ks(t)$, $k=1,2,\dots$ (Abb. [1](#abb-1)). Jede einzelne heißt __Musterfunktion__ oder Realisierung. Die gedachte Gesamtheit aller heißt __Zufallsprozess__ $s(t)$. Die Werte aller Musterfunktionen zu einem festen Zeitpunkt $t_1$ bilden eine __Zufallsgröße__ $s(t_1)$.

:::definition Definition 1.1 (Scharmittelwerte)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**So liest man das:** $\mathrm E\{\cdot\}$ heißt __Erwartungswert__ oder Scharmittelwert: Man mittelt über alle Musterfunktionen zum selben Zeitpunkt, also senkrecht in Abb. [1](#abb-1). Mit $F[x]=x^2$ erhält man den quadratischen Mittelwert. Die __Autokorrelationsfunktion__ mittelt das Produkt der Werte zu zwei Zeitpunkten. Sie sagt, wie stark der Wert bei $t_2$ mit dem bei $t_1$ zusammenhängt.

:::abbildung et3/k7schar
Drei Musterfunktionen eines Zufallsprozesses (simuliert, Mittelwert 1). Das Scharmittel bildet man senkrecht, über alle Musterfunktionen bei demselben $t_1$ (rot gestrichelt). Das Zeitmittel bildet man waagerecht, entlang einer Musterfunktion.
:::

## Stufe 2: Stationarität und Ergodizität

<span class="anker" id="stufe-2"></span>

:::zweck
Eine unendliche Schar hat man nie, meist nur ein einziges Signal. Wann genügt es?
:::

Ein Prozess heißt __stationär__, wenn sich keine seiner Mittelwerte ändern, wenn man alle Beobachtungszeiten um dieselbe Zeit $t_0$ verschiebt:

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

Dann ist der Mittelwert $m_s=\mathrm E\{s(t)\}$ eine Konstante, und die AKF hängt nur noch vom Abstand $\tau=t_2-t_1$ ab: $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$. Ein stationärer Prozess heißt __ergodisch__, wenn außerdem jedes Zeitmittel einer Musterfunktion gleich dem entsprechenden Scharmittel ist:

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{für jedes }k. \tag{2.2}$$

⁠**So liest man das:** Stationär heißt, die Statistik ändert sich nicht mit der Zeit. Ergodisch heißt, eine einzige, lange beobachtete Musterfunktion zeigt im Lauf der Zeit alles, was die ganze Schar zeigt. Das Rauschen eines Widerstands bei konstanter Temperatur ist ergodisch. Nur deshalb kann man Rauschen mit einem einzigen Messgerät charakterisieren.

:::frage Ist jeder stationäre Prozess auch ergodisch?
Nein. Beispiel: Jede Musterfunktion ist eine Konstante, deren Wert einmal gewürfelt wird, ${}^ks(t)=c_k$. Der Prozess ist stationär, denn nichts hängt von $t$ ab. Das Zeitmittel einer Musterfunktion ist aber $c_k$, und das ist für jede Musterfunktion anders, nicht das Scharmittel. Eine einzelne Musterfunktion „sieht“ nie die anderen Werte.
:::

## Stufe 3: Mittelwert, Leistung, Varianz

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

## Stufe 4: Autokorrelation, Kovarianz und Kreuzkorrelation

<span class="anker" id="stufe-4"></span>

:::zweck
Wie schnell ändert sich ein Zufallssignal? Das sagt die AKF: wie ähnlich das Signal sich selbst nach der Zeit $\tau$ noch ist.
:::

:::satz Satz 4.1 (Eigenschaften der AKF stationärer Prozesse)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0). \tag{4.1}$$

Für ergodische Prozesse ist $\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$, also die AKF eines Leistungssignals aus [Teil 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html).
:::

:::herleitung Maximum bei $\tau=0$
$\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$, denn der Erwartungswert eines Quadrats ist nie negativ. Ausmultipliziert und mit Linearität: $\mathrm E\{s^2(t)\}+\mathrm E\{s^2(t+\tau)\}\pm2\mathrm E\{s(t)s(t+\tau)\}\ge0$, also $2\varphi_{ss}(0)\pm2\varphi_{ss}(\tau)\ge0$. Gerade: $t\to t-\tau$ in der Definition.
:::

**Kovarianz.** Zieht man vorher den Mittelwert ab, erhält man die __Autokovarianzfunktion__

<span class="anker" id="gl-4-2"></span>
$$\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2,\qquad\mu_{ss}(0)=\sigma_s^2. \tag{4.2}$$

Enthält der Prozess keine periodischen Anteile, werden weit auseinanderliegende Werte unabhängig: $\varphi_{ss}(\tau)\to m_s^2$ und $\mu_{ss}(\tau)\to0$ für $\tau\to\infty$.

**Kreuzkorrelation und Summen.** Für zwei Prozesse ist $\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$ mit $\varphi_{vu}(\tau)=\varphi_{uv}(-\tau)$ und die Kreuzkovarianz $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$. Für die Summe $s=u+v$ folgt durch Ausmultiplizieren

<span class="anker" id="gl-4-3"></span>
$$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv},\qquad L_s=L_u+L_v+2\varphi_{uv}(0),\qquad\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0). \tag{4.3}$$

⁠**Kurz gesagt:** Leistungen addieren sich nur, wenn die Signale unkorreliert sind. Sonst kommt der Kreuzterm hinzu. Zwei gleiche Signale ergeben die vierfache, zwei entgegengesetzte die Leistung null.

:::aufgabe Aufgabe 2 ★★ Zwei Rauschquellen
<span class="anker" id="aufg-2"></span>

Zwei mittelwertfreie Rauschspannungen mit den Effektivwerten 3 mV und 4 mV werden addiert. Wie groß ist der Effektivwert der Summe, wenn sie (a) unkorreliert sind, (b) dieselbe Form haben ($\varphi_{uv}(0)=\sigma_u\sigma_v$), (c) dieselbe Form mit umgekehrtem Vorzeichen haben ($\varphi_{uv}(0)=-\sigma_u\sigma_v$)?

:::loesung
(a) $\sigma=\sqrt{9+16}=5$ mV. (b) $\sigma^2=9+16+2\cdot12=49$, also 7 mV: Die Amplituden addieren sich. (c) $\sigma^2=9+16-24=1$, also 1 mV: Die Signale löschen sich fast aus.
:::
:::

## Stufe 5: Verteilungsfunktion und Verteilungsdichte

<span class="anker" id="stufe-5"></span>

:::zweck
Mittelwerte sagen nicht alles. Wie oft nimmt ein Signal welche Werte an? Das beschreibt die Verteilung.
:::

:::definition Definition 5.1 (Verteilung)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-1"></span>
$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi. \tag{5.1}$$
:::

⁠**So liest man das:** Die __Verteilungsfunktion__ $P_s(x)$ ist der Anteil der Schar (bei ergodischen Prozessen: der Anteil der Zeit), in dem das Signal unter der Schwelle $x$ liegt. Sie steigt monoton von $P_s(-\infty)=0$ bis $P_s(\infty)=1$. Die __Verteilungsdichte__ $p_s(x)$ ist nie negativ, hat die Fläche 1, und $p_s(x)\,\mathrm{d} x$ ist die Wahrscheinlichkeit, dass das Signal zwischen $x$ und $x+\mathrm{d} x$ liegt. Daraus folgen alle Mittelwerte erster Ordnung:

<span class="anker" id="gl-5-2"></span>
$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x. \tag{5.2}$$

**Beispiel: Gleichverteilung.** Alle Werte in einem Intervall der Breite $a$ um $m_s$ sind gleich wahrscheinlich: $p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$. Dann ist

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

Die Zufallszahlen des Rechenmodells ($a=1$, $m_s=0$) haben die Varianz $\frac1{12}=0{,}0833$.

**Kennlinien.** Läuft ein Signal durch eine Kennlinie $y=k(x)$ (Verstärker mit Sättigung, Gleichrichter, Quantisierer), ändert sich seine Verteilung. Bei einer monotonen Kennlinie bleibt die Wahrscheinlichkeit jedes Intervalls erhalten:

<span class="anker" id="gl-5-3"></span>
$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\text{ steigend}). \tag{5.3}$$

Wo die Kennlinie steil ist, verteilen sich die Werte auf einen breiten Bereich, die Dichte sinkt. Mit dieser Regel kann man jede Verteilung in eine gewünschte umformen. Beispiel: $k(x)=(2|x|-x^2)\operatorname{sgn}x$ macht aus einer Dreieckverteilung auf $[-1,1]$ eine Gleichverteilung (Aufgabe [4](#aufg-4)).

**Quantisierung.** Ein __Quantisierer__ ersetzt jeden Wert durch den nächsten von $M$ Stufen. Bei gleichförmigen Stufen der Breite $\Delta$ ohne Übersteuerung ist der Fehler zwischen $-\frac\Delta2$ und $\frac\Delta2$ annähernd gleichverteilt, also mit der Varianz $\frac{\Delta^2}{12}$. Für ein gleichverteiltes Signal über alle $M$ Stufen (Varianz $\frac{(M\Delta)^2}{12}$) ist das Signal-Rausch-Verhältnis $M^2$, in Dezibel $20\lg M\approx6\,\text{dB je Bit}$: 48 dB bei 8 Bit, 96 dB bei 16 Bit.

:::aufgabe Aufgabe 3 ★ Gleichverteilung
<span class="anker" id="aufg-3"></span>

Ein Signal ist zwischen 1 V und 3 V gleichverteilt. Berechne $m_s$, $L_s$, $\sigma_s^2$ und die Wahrscheinlichkeit, dass es über 2,5 V liegt.

:::loesung
$a=2$ V, $m_s=2$ V. $\sigma_s^2=\frac{a^2}{12}=\frac13$ V$^2$, $L_s=\frac13+4=4{,}33$ V$^2$. Über 2,5 V liegt ein Viertel des Intervalls, also $\mathrm{Prob}=\frac{0{,}5}{2}=0{,}25$.
:::
:::

:::aufgabe Aufgabe 4 ★★ Verteilungen umformen
<span class="anker" id="aufg-4"></span>

Ein Signal hat die Dreieckdichte $p_s(x)=\Lambda(x)$ auf $[-1,1]$.

<ol class="al">

<li>

Bestimme $P_s(x)$ für $0\le x\le1$.

</li>

<li>

Zeige mit [(5.3)](#gl-5-3), dass $k(x)=(2x-x^2)$ für $x\ge0$ (und ungerade fortgesetzt) eine Gleichverteilung auf $[-1,1]$ erzeugt. Tipp: Für die Gleichverteilung ist $P_g(y)=\frac12+\frac y2$.

</li>

</ol>

:::loesung
(a) $P_s(x)=\frac12+\int_0^x(1-\xi)\,\mathrm{d}\xi=\frac12+x-\frac{x^2}{2}$ für $0\le x\le1$.

(b) Nach [(5.3)](#gl-5-3) muss $P_g(k(x))=P_s(x)$ sein, also $\frac12+\frac{k(x)}{2}=\frac12+x-\frac{x^2}{2}$. Das ergibt $k(x)=2x-x^2$. Die Kennlinie ist bei $x=0$ steil (Steigung 2), wo die Dreieckdichte am größten ist, und am Rand flach. So werden die häufigen Werte auseinandergezogen, die seltenen zusammengeschoben. Eine Simulation ergibt ein flaches Histogramm mit der Höhe 0,5.
:::
:::

:::aufgabe Aufgabe 4a ★★★ (Vertiefung) Der optimale Quantisierer
<span class="anker" id="aufg-4a"></span>

Ein Quantisierer mit den Schwellen $u_i$ und den Stufenwerten $v_i$ (Stufe $i$ gilt für $u_i<x\le u_{i+1}$) hat den mittleren quadratischen Fehler $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$.

<ol class="al">

<li>

Zeige durch Ableiten nach $v_i$: Im Optimum liegt $v_i$ im Schwerpunkt der Dichte auf seinem Intervall.

</li>

<li>

Zeige durch Ableiten nach $u_i$: Im Optimum liegt $u_i$ genau in der Mitte zwischen $v_{i-1}$ und $v_i$.

</li>

<li>

Warum ist für ein gleichverteiltes Signal der gleichförmige Quantisierer optimal?

</li>

</ol>

:::loesung
(a) $\frac{\partial N_q}{\partial v_i}=\int_{u_i}^{u_{i+1}}2(v_i-x)p_s(x)\mathrm{d} x=0$, also $v_i=\dfrac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x}$, der Schwerpunkt.

(b) $u_i$ kommt als obere Grenze des Intervalls $i-1$ und als untere Grenze des Intervalls $i$ vor: $\frac{\partial N_q}{\partial u_i}=(v_{i-1}-u_i)^2p_s(u_i)-(v_i-u_i)^2p_s(u_i)=0$, also $u_i=\frac12(v_{i-1}+v_i)$. Ein Wert wird der Stufe zugeordnet, deren Stufenwert näher liegt.

(c) Bei konstanter Dichte ist der Schwerpunkt jedes Intervalls seine Mitte. Gleich breite Intervalle mit den Mitten als Stufenwerten erfüllen beide Bedingungen, mit der Stufenbreite $\Delta=a/M$.
:::
:::

## Stufe 6: Verbundverteilung, Unabhängigkeit, Unkorreliertheit

<span class="anker" id="stufe-6"></span>

:::zweck
Zwei Zufallsgrößen zugleich: Wann hängen sie zusammen, und was folgt daraus für ihre Summe?
:::

Die __Verbundverteilung__ zweier Größen ist $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{und}\ g\le y]$, ihre Dichte $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$. Daraus folgen die Einzelverteilungen ($P_{sg}(x,\infty)=P_s(x)$) und die Korrelation $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$. Bei verbunden stationären Prozessen hängt alles nur von der Zeitverschiebung $\tau$ zwischen $s(t)$ und $g(t+\tau)$ ab.

:::definition Definition 6.1 (Unabhängig, unkorreliert)
<span class="anker" id="satz-6-1"></span>

$s$ und $g$ heißen __statistisch unabhängig__, wenn $p_{sg}(x,y)=p_s(x)\,p_g(y)$. Sie heißen __unkorreliert__, wenn $\mu_{sg}=\varphi_{sg}-m_sm_g=0$.
:::

Aus Unabhängigkeit folgt Unkorreliertheit: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$. Umgekehrt nicht: Unkorreliert heißt nur, dass kein *linearer* Zusammenhang besteht (Aufgabe [5](#aufg-5)).

**Die Summe zweier unabhängiger Größen.** Die Summe $s=f+g$ nimmt den Wert $x$ an, wenn $f=u$ und $g=x-u$, für irgendein $u$:

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{unabhängig}). \tag{6.1}$$

Das ist die Faltung aus [Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), dort am Beispiel der Würfel. Zwei gleichverteilte Größen ergeben eine Dreieckdichte, drei eine schon fast glockenförmige (Abb. [2](#abb-2)).

:::abbildung et3/k7summen
Verteilungsdichten von Summen unabhängiger, auf $[-\frac12,\frac12]$ gleichverteilter Zufallsgrößen. Schon die Summe von drei liegt nahe an der Gaußkurve mit derselben Varianz (bei $x=0$: 0,75 gegen 0,80).
:::

:::aufgabe Aufgabe 5 ★★ Unkorreliert, aber abhängig
<span class="anker" id="aufg-5"></span>

$s$ ist gleichverteilt auf $[-1,1]$ und $g=s^2$. Zeige, dass $s$ und $g$ unkorreliert sind, obwohl $g$ durch $s$ vollständig bestimmt ist.

:::loesung
$m_s=0$ und $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$, also $\mu_{sg}=0-0\cdot m_g=0$: unkorreliert. Trotzdem legt $s$ den Wert von $g$ fest. Der Zusammenhang ist quadratisch, und eine Korrelation erfasst nur lineare Zusammenhänge: Für positive $s$ steigt $g$ mit $s$, für negative fällt es, im Mittel heben sich beide Tendenzen auf.
:::
:::

## Stufe 7: Die Gauß-Verteilung

<span class="anker" id="stufe-7"></span>

:::zweck
Warum ist Rauschen so oft gaußverteilt, und wie rechnet man mit der Gauß-Verteilung?
:::

Faltet man viele Dichten miteinander, nähert sich das Ergebnis einer Gaußkurve (__zentraler Grenzwertsatz__, [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). Rauschen ist meist die Summe sehr vieler kleiner, unabhängiger Beiträge, etwa der Bewegungen vieler Elektronen. Deshalb ist es gaußverteilt.

:::satz Satz 7.1 (Gauß-Verteilung)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

mit der __Fehlerfunktion__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$ und $\operatorname{erfc}=1-\operatorname{erf}$.
:::

⁠**So liest man das:** Mittelwert und Varianz legen die Gauß-Verteilung vollständig fest. Innerhalb von $\pm\sigma_s$ um den Mittelwert liegen 68,3 % der Werte, innerhalb $\pm2\sigma_s$ 95,4 %, innerhalb $\pm3\sigma_s$ 99,73 %. Das Integral der Gaußkurve hat keine geschlossene Form, deshalb die Funktion erf, die man tabelliert oder numerisch berechnet. Für große $x$ gilt $\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$.

**Rechenregeln.** Die Summe zweier unabhängiger gaußverteilter Größen ist gaußverteilt mit $m_s=m_1+m_2$ und $\sigma_s^2=\sigma_1^2+\sigma_2^2$. Ein Gauß-Prozess bleibt nach einem LTI-System ein Gauß-Prozess, denn das Faltungsintegral ist eine (unendliche) gewichtete Summe. Und bei zwei gemeinsam gaußverteilten Größen ist „unkorreliert“ dasselbe wie „unabhängig“: Ist die normierte Kreuzkovarianz $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ null, zerfällt die Verbunddichte in ein Produkt.

:::zusatz Die zweidimensionale Gauß-Dichte
Für mittelwertfreie, gemeinsam gaußverteilte $s,g$ mit dem Korrelationskoeffizienten $\rho$ ist

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

Man erhält sie über die normierten Summen- und Differenzgrößen $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$: Sie sind unkorreliert, haben die Varianzen $2(1\pm\rho)$ und sind als Gauß-Größen unabhängig. Linien gleicher Dichte sind Ellipsen. In den normierten Koordinaten $x/\sigma_s$, $y/\sigma_g$ liegen ihre Achsen entlang dieser Summen und Differenzen. Für $\rho=0$ werden sie zu Kreisen (bei $\sigma_s=\sigma_g$), und die Dichte ist das Produkt der Einzeldichten.
:::

:::aufgabe Aufgabe 6 ★ Mit der Gauß-Verteilung rechnen
<span class="anker" id="aufg-6"></span>

Eine Rauschspannung ist gaußverteilt mit $m=0$ und $\sigma=1$ mV.

<ol class="al">

<li>

Mit welcher Wahrscheinlichkeit ist sie größer als 2 mV? (Tipp: $\operatorname{erfc}(1{,}414)=0{,}0455$.)

</li>

<li>

Zwei solche unabhängige Spannungen werden addiert. Welche Verteilung hat die Summe?

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1{,}414)=0{,}023$, also 2,3 %.

(b) Gaußverteilt mit $m=0$ und $\sigma^2=2$ mV$^2$, $\sigma=1{,}41$ mV.
:::
:::

## Stufe 8: Zufallssignale in LTI-Systemen, Leistungsdichte

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

## Stufe 9: Weißes Rauschen und thermisches Rauschen

<span class="anker" id="stufe-9"></span>

:::zweck
Das wichtigste Modell für Störungen: Rauschen mit gleicher Leistungsdichte bei allen Frequenzen.
:::

:::definition Definition 9.1 (Weißes Rauschen)
<span class="anker" id="satz-9-1"></span>

Ein mittelwertfreier Prozess mit $\Phi_{ss}(f)=N_0$ für alle $f$ heißt __weißes Rauschen__. Seine AKF ist $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$.
:::

⁠**So liest man das:** Werte zu verschiedenen Zeiten sind unkorreliert, egal wie nahe sie beieinanderliegen. Die Leistung $\int N_0\mathrm{d} f$ ist unendlich: Weißes Rauschen ist ein Grenzmodell wie der Dirac-Impuls. Wirklich gemessen wird immer gefiltertes, „farbiges“ Rauschen:

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

Hinter einem idealen Tiefpass mit $f_\mathrm g$: $L_g=2N_0f_\mathrm g$ und $\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$ (Abb. [3](#abb-3)). Die AKF ist an den Stellen $\tau=k/(2f_\mathrm g)$, $k\neq0$, null: Abtastwerte im Abstand der Nyquist-Rate sind unkorreliert.

:::abbildung et3/k7tp
AKF von weißem Rauschen hinter einem idealen Tiefpass: $2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$. Bei $\tau=0$ die Leistung $2N_0f_\mathrm g$. An den roten Punkten ($\tau=k/(2f_\mathrm g)$) ist sie null.
:::

**Thermisches Rauschen.** Die Wärmebewegung der Elektronen erzeugt an jedem Widerstand $R$ eine Rauschspannung. Im Leerlauf, gemessen im Frequenzbereich $|f|\le f_\mathrm g$:

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

mit der Boltzmann-Konstanten $k=1{,}38\cdot10^{-23}$ W s/K. Bei Raumtemperatur (290 K) ist $kT\approx4\cdot10^{-21}$ W/Hz, also 4 pW je GHz Bandbreite. $L_{\max}$ ist die Leistung, die man dem Widerstand bei Leistungsanpassung höchstens entnehmen kann. Im Rechenmodell ($1\,\mathrm{k\Omega}$, 20 kHz) ist der Effektivwert $\sqrt{\mathrm E\{u^2\}}=0{,}57$ µ V. Diese Größenordnung begrenzt, wie empfindlich ein Mikrofonverstärker sein kann. Das Spektrum ist bis etwa $10^{12}$ Hz flach.

:::ltspice Thermisches Rauschen messen
LTspice gibt jedem Widerstand sein thermisches Rauschen mit. Die Analyse `.noise` rechnet an einem Knoten die Rauschdichte `V(onoise)` in V$/\sqrt{\mathrm{Hz}}$. Die Messung `.meas noise urms INTEG V(onoise)` integriert sie quadratisch über den Frequenzbereich der Analyse, wie in [(8.3)](#gl-8-3), und liefert den Effektivwert. `.temp 16.85` stellt 290 K ein.

⁠**Widerstand:** `res` mit `{Rx}` vom Netz `a` nach Masse, parallel eine Stromquelle `current` mit dem Wert 0 (Name `I1`). Sie belastet nichts, `.noise` braucht sie nur als Bezugsquelle. Direktiven `.param Rx=1k` und `.noise V(a) I1 lin 20001 1 20k`. Ergebnis: 4,0 nV$/\sqrt{\mathrm{Hz}}$ und `urms` $=0{,}57$ µ V wie oben. Setze `Rx=1Meg` und vergleiche mit deinem Ergebnis aus Aufgabe [8](#aufg-8).

⁠**$kT/C$:** Quelle `voltage` `V1` mit dem Wert 0 und `AC 1`, `res` mit `{Rx}` nach `out`, `cap` mit `1p` nach Masse. Direktiven `.step param Rx list 1k 1Meg` und `.noise V(out) V1 dec 200 1 1T`, dazu wieder `.temp 16.85` und die Messung `urms`. `urms` ist für beide Widerstände gleich. Vergleiche den Wert mit deinem Ergebnis aus Aufgabe [9](#aufg-9)(b).
:::

:::aufgabe Aufgabe 8 ★ Rauschen eines Widerstands
<span class="anker" id="aufg-8"></span>

Berechne den Rauscheffektivwert eines Widerstands von $1\,\mathrm{M\Omega}$ bei 290 K und 20 kHz Bandbreite. Um welchen Faktor ist er größer als beim $1\,\mathrm{k\Omega}$-Widerstand, und warum gerade um diesen?

:::loesung
Der Effektivwert wächst mit $\sqrt R$: $\sqrt{1000}=31{,}6$-mal größer, also $0{,}566\cdot31{,}6=17{,}9$ µ V.
:::
:::

:::aufgabe Aufgabe 9 ★★ Das $kT/C$-Rauschen
<span class="anker" id="aufg-9"></span>

Das thermische Rauschen des Widerstands ($N_0=2kTR$) läuft durch das RC-Glied, das er mit einem Kondensator $C$ bildet ($h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$).

<ol class="al">

<li>

Zeige mit [(9.1)](#gl-9-1), dass die Rauschleistung am Kondensator $kT/C$ ist, unabhängig von $R$.

</li>

<li>

Wie groß ist der Effektivwert bei $C=1$ pF und 290 K? Warum hilft ein kleinerer Widerstand hier nicht?

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$. Also $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$.

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V. Ein kleinerer Widerstand rauscht zwar weniger pro Hertz, aber das RC-Glied wird breitbandiger ($1/RC$ größer). Beides hebt sich genau auf. Nur ein größerer Kondensator verringert das Rauschen.
:::
:::

## Stufe 10: Das Korrelationsfilter (Matched Filter)

<span class="anker" id="stufe-10"></span>

:::zweck
Ein bekannter Impuls $s(t)$ kommt verrauscht an. Mit welchem Filter wird er im Abtastzeitpunkt $T$ am deutlichsten sichtbar?
:::

**Der Ansatz.** Am Empfängereingang liegt $s(t)+n(t)$ mit weißem Rauschen $n$. Ein Filter $h$ liefert $y=g+n_e$ mit dem Nutzanteil $g=s*h$ und dem Störanteil $n_e=n*h$. Abgetastet wird bei $T$. Das Signal-Rausch-Verhältnis dort ist

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

Der rechte Bruch ist das Quadrat eines Korrelationskoeffizienten ([Teil 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)), zwischen $h(\tau)$ und $s(T-\tau)$. Er ist höchstens 1, und zwar genau dann, wenn beide dieselbe Form haben.

:::satz Satz 10.1 (Korrelationsfilter)
<span class="anker" id="satz-10-1"></span>

Gegen weißes Rauschen ist das beste erreichbare Signal-Rausch-Verhältnis

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{erreicht mit}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**So liest man das:** Die beste Impulsantwort ist das zeitgespiegelte, um $T$ verschobene Signal selbst, das __Korrelationsfilter__ (matched filter). Sein Ausgang ohne Rauschen ist $g(t)=a\,\varphi^E_{ss}(t-T)$, die verschobene AKF des Signals, und wird genau in ihrem Maximum abgetastet. Erstaunlich ist: Das Ergebnis hängt nur von der *Energie* des Signals ab, nicht von seiner Form. Ein kurzer, hoher Impuls ist so gut wie ein langer, flacher mit derselben Energie. Damit das Filter kausal ist, muss $T$ mindestens die Dauer des Signals sein. Gleichwertig ist ein __Korrelator__: Er multipliziert das Empfangssignal mit $s(t)$ und integriert über die Dauer des Signals.

:::aufgabe Aufgabe 10 ★★ Ein Rechteckimpuls im Rauschen
<span class="anker" id="aufg-10"></span>

Ein Rechteckimpuls der Höhe 1 V und Dauer 1 ms wird mit weißem Rauschen der Leistungsdichte $N_0=10^{-6}$ V$^2$/Hz empfangen.

<ol class="al">

<li>

Wie sieht das Korrelationsfilter aus, und welches $S_a/N$ (in dB) erreicht es?

</li>

<li>

Wie sieht der Ausgang ohne Rauschen aus, und wann muss abgetastet werden?

</li>

<li>

Der Impuls wird auf 0,25 ms verkürzt, bei gleicher Höhe. Was ändert sich?

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$: wieder ein Rechteck von 1 ms, mit $T\ge1$ ms kausal. $E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s, also $S_a/N=10^{-3}/10^{-6}=1000$, das sind 30 dB.

(b) Die AKF des Rechtecks, ein Dreieck der Breite 2 ms, verschoben um $T$: Es steigt ab $t=T-1\,\mathrm{ms}$ an und erreicht bei $t=T$ sein Maximum. Bei $T=1$ ms tastet man genau am Ende des Impulses ab, dann hat das Filter ihn ganz „gesehen“.

(c) $E_s$ sinkt auf ein Viertel, $S_a/N=250$, also 24 dB, 6 dB schlechter. Es zählt nur die Energie. Bei gleicher Höhe bedeutet ein kürzerer Impuls weniger Energie.
:::
:::

## Stufe 11: Fehlerwahrscheinlichkeit beim Binärempfang

<span class="anker" id="stufe-11"></span>

:::zweck
Der Empfänger soll entscheiden: Wurde der Impuls gesendet oder nicht? Wie oft irrt er sich?
:::

**Die Idee.** Der Abtastwert am Ausgang des Korrelationsfilters ist gaußverteilt mit der Varianz $N$ (Rauschen) und dem Mittelwert $\sqrt{S_a}$, wenn gesendet wurde, oder 0, wenn nicht. Der Empfänger vergleicht mit einer Schwelle $C$. Ein Fehler passiert, wenn das Rauschen den Wert über die Schwelle schiebt. Die beiden Fehlerwahrscheinlichkeiten sind die Flächen der beiden Gaußkurven jenseits der Schwelle:

<span class="anker" id="gl-11-1"></span>
$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr). \tag{11.1}$$

Werden beide Fälle gleich oft gesendet, ist die mittlere Fehlerwahrscheinlichkeit $\frac12(P_{e1}+P_{e0})$. Sie wird am kleinsten, wenn die Schwelle genau in der Mitte liegt, $C=\sqrt{S_a}/2$. Mit dem Korrelationsfilter ($S_a/N=E_s/N_0$):

<span class="anker" id="gl-11-2"></span>
$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}. \tag{11.2}$$

⁠**So liest man das:** Die Fehlerwahrscheinlichkeit hängt nur von $E_s/N_0$ ab und fällt extrem schnell: bei 10 dB $5{,}7\cdot10^{-2}$, bei 16 dB $8\cdot10^{-4}$, bei 20 dB $2{,}9\cdot10^{-7}$ (Abb. [4](#abb-4)). Wenige Dezibel mehr Signalenergie machen aus einer unbrauchbaren eine fast fehlerfreie Übertragung.

:::abbildung et3/k7pe
Minimale Fehlerwahrscheinlichkeit beim Ein-Aus-Empfang mit Korrelationsfilter. Rote Punkte: 10 dB, 16 dB, 20 dB.
:::

:::aufgabe Aufgabe 11 ★★ Fehlerwahrscheinlichkeit
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Berechne $P_{e,\min}$ für $E_s/N_0=10$ dB. Tipp: $\operatorname{erfc}(1{,}118)=0{,}114$.

</li>

<li>

Warum liegt die optimale Schwelle in der Mitte zwischen 0 und $\sqrt{S_a}$? Was passiert mit $P_{e1}$ und $P_{e0}$, wenn man sie nach oben verschiebt?

</li>

</ol>

:::loesung
(a) $E_s/N_0=10$: $\sqrt{10/8}=1{,}118$, $P_{e,\min}=\frac12\cdot0{,}114=0{,}057$.

(b) Die beiden Gaußkurven haben dieselbe Breite. Die Summe der beiden Fehlerflächen ist am kleinsten, wo sich die Kurven schneiden, und das ist aus Symmetriegründen die Mitte. Schiebt man die Schwelle nach oben, wird $P_{e0}$ kleiner, aber $P_{e1}$ wächst stärker, weil die Schwelle in den dichten Teil der oberen Kurve rückt.
:::
:::

## Stufe 12: Zeitdiskrete Zufallssignale

<span class="anker" id="stufe-12"></span>

:::zweck
Alles gilt auch für Folgen von Zufallszahlen, mit Summen statt Integralen.
:::

Tastet man einen auf $f_\mathrm g$ bandbegrenzten Prozess mit $T\le\frac{1}{2f_\mathrm g}$ ab, bilden die Abtastwerte einen zeitdiskreten Prozess $s(n)$. Verteilungen, Erwartungswerte und Korrelationen sind wie zuvor definiert, die Zeitmittel sind Summen, etwa $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$. Durch ein LSI-System mit $h(n)$:

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

mit dem periodischen Leistungsdichtespektrum $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$ und $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$. __Zeitdiskretes weißes Rauschen__ hat $\Phi_{ss,\mathrm a}=N$ und $\varphi_{ss}(m)=N\delta(m)$: Aufeinanderfolgende Zahlen sind unkorreliert. Anders als im Kontinuierlichen ist seine Leistung endlich, $L_s=N$.

**Beispiel 1: Mittelung zweier Werte.** Gleichverteiltes weißes Rauschen ($\sigma_s^2=\frac1{12}$) durch $h(n)=\frac12[\delta(n)+\delta(n-1)]$, also $g(n)=\frac12[s(n)+s(n-1)]$. Mit $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$:

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

Die Varianz halbiert sich auf $\frac{1}{24}$, und benachbarte Ausgangswerte sind jetzt korreliert (sie teilen sich einen Eingangswert). Die Ausgangswerte sind dreieckverteilt, weil jeder die halbe Summe zweier unabhängiger, gleichverteilter Zahlen ist. Eine Simulation mit 200 000 Zahlen ergibt die Varianz 0,0415 statt $\frac1{24}=0{,}0417$.

**Beispiel 2: Rekursives Filter (AR(1)-Prozess).** Weißes Rauschen der Varianz $\sigma_s^2$ durch $h(n)=b^n\varepsilon(n)$ ([Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)). Mit $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$:

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

Für $b=0{,}6$ ist die Varianz das $1{,}56$-Fache der Eingangsvarianz, und benachbarte Werte haben den Korrelationskoeffizienten $0{,}6$. Je näher $b$ an 1, desto stärker die tiefen Frequenzen (Abb. [5](#abb-5)).

:::abbildung et3/k7ar
Leistungsdichtespektren von AR(1)-Prozessen, periodisch mit 1. Bei $b=0{,}6$ reicht es von 6,25 ($f=0$) bis 0,39 ($f=\frac12$), bei $b=0{,}9$ von 100 bis 0,28.
:::

:::aufgabe Aufgabe 12 ★★ AR(1)-Prozess
<span class="anker" id="aufg-12"></span>

Gleichverteiltes weißes Rauschen ($\sigma_s^2=\frac1{12}$) läuft durch $g(n)=s(n)+0{,}6\,g(n-1)$.

<ol class="al">

<li>

Berechne die Ausgangsvarianz und $\varphi_{gg}(1)/\varphi_{gg}(0)$.

</li>

<li>

Leite $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$ mit der geometrischen Reihe her.

</li>

<li>

Ist der Ausgang noch gleichverteilt? Welche Verteilung erwartest du ungefähr, und warum?

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0{,}36}=0{,}130$, $\varphi_{gg}(1)/\varphi_{gg}(0)=b=0{,}6$. Die Simulation ergibt 0,130 und 0,600.

(b) Für $m\ge0$: $\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$. Die Impuls-AKF ist gerade, also gilt $b^{|m|}$.

(c) Nicht mehr gleichverteilt: Jeder Ausgangswert ist eine gewichtete Summe vieler unabhängiger Eingangswerte, $g(n)=\sum_kb^ks(n-k)$. Nach dem zentralen Grenzwertsatz ist das ungefähr gaußverteilt. Bei $b=0{,}6$ tragen nur wenige Summanden merklich bei, die Näherung ist deshalb grob, aber die Verteilung ist schon deutlich glockenförmig.
:::
:::

:::kern Das Wichtigste
<ul>

<li>

Scharmittel $\mathrm E\{\cdot\}$; stationär: verschiebungsunabhängig; ergodisch: Zeitmittel $=$ Scharmittel.

</li>

<li>

$m_s$ (Gleichanteil), $L_s=\mathrm E\{s^2\}$ (Leistung), $\sigma_s^2=L_s-m_s^2$ (Wechselleistung).

</li>

<li>

AKF: $\varphi_{ss}(0)=L_s$, gerade, Maximum bei 0; Kovarianz $\mu=\varphi-m^2$; Summe: $\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$.

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$, $p_s=P_s'$; $m_s=\int xp_s$, $L_s=\int x^2p_s$; Gleichverteilung $\sigma^2=a^2/12$.

</li>

<li>

Kennlinie: $p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$; Quantisierungsfehler $\Delta^2/12$, 6 dB je Bit.

</li>

<li>

Unabhängig $\Rightarrow$ unkorreliert; Summe unabhängiger: $p_s=p_f*p_g$; Gauß: $\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$.

</li>

<li>

LTI: $m_g=m_sH(0)$, $\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$, $\Phi_{gg}=\Phi_{ss}|H|^2$, $L=\int\Phi\,\mathrm{d} f$.

</li>

<li>

Weiß: $\Phi=N_0$, $\varphi=N_0\delta$; thermisch $\mathrm E\{u^2\}=4kTRf_\mathrm g$, $kT\approx4$ pW/GHz.

</li>

<li>

Matched Filter: $h=a\,s(T-t)$, $(S_a/N)_{\max}=E_s/N_0$; $P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$.

</li>

</ul>
:::
