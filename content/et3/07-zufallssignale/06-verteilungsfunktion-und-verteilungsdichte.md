---
title: Stufe 5: Verteilungsfunktion und Verteilungsdichte
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270600
summary: Mittelwerte sagen nicht alles.
tags: Verteilungsfunktion, Verteilungsdichte, Quantisierer
lang: de
---

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

::::beispiel Gleichverteilung
Alle Werte in einem Intervall der Breite $a$ um $m_s$ sind gleich wahrscheinlich: $p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$. Dann ist

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

Die Zufallszahlen des Rechenmodells ($a=1$, $m_s=0$) haben die Varianz $\frac1{12}=0{,}0833$.
::::

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

::::formelsammlung
**Verteilungsfunktion und Verteilungsdichte**

$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi$$

$P_s$ steigt monoton von $P_s(-\infty)=0$ bis $P_s(\infty)=1$. $p_s$ ist nie negativ und hat die Fläche 1; $p_s(x)\,\mathrm{d} x$ ist die Wahrscheinlichkeit für einen Wert zwischen $x$ und $x+\mathrm{d} x$.

**Mittelwerte aus der Dichte**

$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x$$

Alle Mittelwerte erster Ordnung folgen aus der Verteilungsdichte.

**Gleichverteilung**

$$p_s(x)=\frac1a\operatorname{rect}\Bigl(\frac{x-m_s}{a}\Bigr),\qquad L_s=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}$$

Alle Werte in einem Intervall der Breite $a$ um $m_s$ gleich wahrscheinlich.

**Verteilung hinter einer Kennlinie**

$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\text{ steigend})$$

Für eine monotone Kennlinie $y=k(x)$: Die Wahrscheinlichkeit jedes Intervalls bleibt erhalten; wo die Kennlinie steil ist, sinkt die Dichte.

**Quantisierungsfehler**

$$\frac{\Delta^2}{12}$$

Varianz des Fehlers bei gleichförmigen Stufen der Breite $\Delta$ ohne Übersteuerung; der Fehler ist annähernd gleichverteilt zwischen $-\frac\Delta2$ und $\frac\Delta2$.

**Signal-Rausch-Verhältnis der Quantisierung**

$$M^2,\qquad20\lg M\approx6\,\text{dB je Bit}$$

Für ein gleichverteiltes Signal über alle $M$ Stufen (Varianz $\frac{(M\Delta)^2}{12}$).

**Optimaler Quantisierer**

$$v_i=\frac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x},\qquad u_i=\frac12(v_{i-1}+v_i)$$

Kleinster mittlerer quadratischer Fehler $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$: Stufenwert im Schwerpunkt der Dichte auf seinem Intervall, Schwelle in der Mitte zwischen zwei Stufenwerten. Für ein gleichverteiltes Signal ist der gleichförmige Quantisierer optimal.
::::

::::lernkarten
:::karte begriff Verteilungsfunktion
Was gibt die Verteilungsfunktion $P_s(x)$ eines Zufallssignals an, und welchen Verlauf hat sie?
---
Die Wahrscheinlichkeit $P_s(x)=\mathrm{Prob}[s(t)\le x]$, dass das Signal unter der Schwelle $x$ liegt, also den Anteil der Schar (bei ergodischen Prozessen: der Zeit). Sie steigt monoton von $P_s(-\infty)=0$ bis $P_s(\infty)=1$.
--- falsch
Die Wahrscheinlichkeit $P_s(x)=\mathrm{Prob}[s(t)=x]$, dass das Signal genau den Wert $x$ annimmt. Sie hat bei den häufigsten Werten des Signals ein Maximum und fällt nach beiden Seiten bis auf null ab.
--- falsch
Die Wahrscheinlichkeit $P_s(x)=\mathrm{Prob}[s(t)>x]$, dass das Signal über der Schwelle $x$ liegt, also den Anteil der Zeit oberhalb der Schwelle. Sie steigt monoton von $P_s(-\infty)=0$ bis $P_s(\infty)=1$.
--- falsch
Den Anteil der Musterfunktionen, deren Zeitmittelwert unter der Schwelle $x$ liegt. Sie kann je nach Prozess steigen oder fallen und erreicht nur bei ergodischen Prozessen am Ende den Wert 1.
:::
:::karte begriff Verteilungsdichte
Was gibt die Verteilungsdichte $p_s(x)$ eines Zufallssignals an, und welche Eigenschaften hat sie?
---
Die Ableitung $p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x}$ der Verteilungsfunktion: $p_s(x)\,\mathrm{d} x$ ist die Wahrscheinlichkeit, dass das Signal zwischen $x$ und $x+\mathrm{d} x$ liegt. Sie ist nie negativ und hat die Fläche 1.
--- falsch
Die Wahrscheinlichkeit, dass das Signal genau den Wert $x$ annimmt. Deshalb ist $p_s(x)$ an jeder Stelle höchstens 1, und die Summe ihrer Werte über alle $x$ ergibt bei jedem Signal genau 1.
--- falsch
Die Ableitung $p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x}$ der Verteilungsfunktion. Sie wird negativ, wo das Signal seltener wird, und ihre Fläche ist der Mittelwert $m_s$ des Signals, nicht 1.
--- falsch
Das Integral $p_s(x)=\int_{-\infty}^xP_s(\xi)\,\mathrm{d}\xi$ der Verteilungsfunktion: Sie gibt an, wie viel Zeit das Signal insgesamt unterhalb von $x$ verbracht hat, und wächst deshalb ohne Grenze.
:::
:::karte formel Verteilungsfunktion aus der Dichte
Wie erhält man die Verteilungsfunktion $P_s(x)$ aus der Verteilungsdichte, und was bedeutet das anschaulich?
---
$P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi$: Man summiert die Wahrscheinlichkeiten aller Werte unterhalb der Schwelle $x$, also die Fläche unter der Dichte links von $x$.
--- falsch
$P_s(x)=\frac{\mathrm{d} p_s(x)}{\mathrm{d} x}$: Die Verteilungsfunktion ist die Steigung der Dichte; sie ist dort groß, wo die Dichte am schnellsten zunimmt, und null an ihrem Maximum.
--- falsch
$P_s(x)=\int_x^{\infty}p_s(\xi)\,\mathrm{d}\xi$: Man summiert die Wahrscheinlichkeiten aller Werte oberhalb der Schwelle $x$, also die Fläche unter der Dichte rechts von $x$.
--- falsch
$P_s(x)=x\,p_s(x)$: Man multipliziert die Dichte an der Schwelle mit der Schwelle selbst, also mit der Breite des Bereichs von null bis $x$, wie bei einem Rechteck.
:::
:::karte formel Mittelwerte aus der Verteilungsdichte
Wie berechnet man Mittelwert, Leistung und allgemein den Erwartungswert $\mathrm E\{F[s]\}$ aus der Verteilungsdichte?
---
$m_s=\int x\,p_s(x)\,\mathrm{d} x$, $L_s=\int x^2p_s(x)\,\mathrm{d} x$ und $\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x$: Jeder Wert wird mit seiner Wahrscheinlichkeit gewichtet. So folgen alle Mittelwerte erster Ordnung aus der Dichte.
--- falsch
$m_s=\int p_s(x)\,\mathrm{d} x$, $L_s=\int p_s^2(x)\,\mathrm{d} x$ und $\mathrm E\{F[s]\}=\int F(p_s(x))\,\mathrm{d} x$: Man setzt die Dichte selbst in die Funktion ein und integriert. So folgen alle Mittelwerte erster Ordnung aus der Dichte.
--- falsch
$m_s=\int x\,p_s(x)\,\mathrm{d} x$, $L_s=\bigl(\int x\,p_s(x)\,\mathrm{d} x\bigr)^2$ und $\mathrm E\{F[s]\}=F(m_s)$: Alle Mittelwerte folgen schon aus dem Mittelwert, die Leistung ist zum Beispiel einfach sein Quadrat.
--- falsch
$m_s=\int x\,P_s(x)\,\mathrm{d} x$, $L_s=\int x^2P_s(x)\,\mathrm{d} x$ und $\mathrm E\{F[s]\}=\int F(x)\,P_s(x)\,\mathrm{d} x$: Man gewichtet jeden Wert mit der Verteilungsfunktion, nicht mit der Dichte, weil sie die Wahrscheinlichkeit angibt.
:::
:::karte formel Gleichverteilung
Welche Dichte, welche Leistung und welche Varianz hat ein Signal, das in einem Intervall der Breite $a$ um $m_s$ gleichverteilt ist?
---
$p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$ mit $L_s=\frac{a^2}{12}+m_s^2$ und $\sigma_s^2=\frac{a^2}{12}$. Die Varianz hängt nur von der Breite des Intervalls ab, nicht von seiner Lage.
--- falsch
$p_s(x)=\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$ mit $L_s=\frac{a^2}{4}+m_s^2$ und $\sigma_s^2=\frac{a^2}{4}$: Die Varianz ist das Quadrat der halben Breite, weil die Werte bis zu $a/2$ vom Mittelwert abweichen.
--- falsch
$p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$ mit $L_s=\frac{a^2}{12}$ und $\sigma_s^2=\frac{a^2}{12}-m_s^2$. Die Varianz wird kleiner, je weiter das Intervall vom Nullpunkt entfernt liegt.
--- falsch
$p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$ mit $L_s=\frac{a}{12}+m_s^2$ und $\sigma_s^2=\frac{a}{12}$. Die Varianz wächst linear mit der Breite des Intervalls, nicht quadratisch.
:::
:::karte herleitung Varianz der Gleichverteilung
Wie folgen aus der Dichte $p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$ die Leistung und die Varianz der Gleichverteilung?
---
Man setzt die Dichte in $L_s=\int x^2p_s(x)\,\mathrm{d} x$ ein, weil sich jeder Mittelwert erster Ordnung aus der Dichte berechnen lässt.
---
Es bleibt $L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x$, weil die Dichte nur auf dem Intervall der Breite $a$ um $m_s$ von null verschieden ist und dort den Wert $\frac1a$ hat.
---
Das Integral ergibt $\frac{a^2}{12}+m_s^2$, weil man die Stammfunktion $x^3/3$ an den Grenzen $m_s\pm a/2$ auswertet und durch $a$ teilt.
---
Die Varianz ist $\sigma_s^2=\frac{a^2}{12}$, weil $\sigma_s^2=L_s-m_s^2$ ist und sich der Anteil $m_s^2$ des Mittelwerts gerade abzieht.
:::
:::karte formel Verteilung hinter einer Kennlinie
Wie ändert sich die Verteilungsdichte, wenn ein Signal durch eine monotone Kennlinie $y=k(x)$ läuft?
---
Die Wahrscheinlichkeit jedes Intervalls bleibt erhalten: $p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|$, also $p_g(y)=\frac{p_s(x)}{|k'(x)|}$. Bei steigender Kennlinie gilt zudem $P_g\bigl(k(x)\bigr)=P_s(x)$.
--- falsch
Die Dichte wird mit der Steigung der Kennlinie multipliziert: $p_g(y)=p_s(x)\,|k'(x)|$. Wo die Kennlinie steil ist, wird die Dichte größer, weil dort mehr Werte des Ausgangs entstehen.
--- falsch
Die Dichte bleibt erhalten, $p_g(y)=p_s(x)$, denn eine monotone Kennlinie ordnet jedem Eingangswert genau einen Ausgangswert zu und ändert deshalb nur die Beschriftung der Achse.
--- falsch
Die Dichte wird durch die Kennlinie selbst geteilt: $p_g(y)=\frac{p_s(x)}{k(x)}$. Wo die Kennlinie große Werte liefert, werden die Ausgangswerte entsprechend seltener.
:::
:::karte zusammenhang Steile Kennlinie
Warum sinkt die Dichte des Ausgangssignals dort, wo die Kennlinie steil ist?
---
Weil die Wahrscheinlichkeit eines kleinen Eingangsintervalls erhalten bleibt, sich aber auf ein breiteres Ausgangsintervall verteilt. Die Dichte $p_g(y)=\frac{p_s(x)}{|k'(x)|}$ wird dort also kleiner.
--- falsch
Weil eine steile Kennlinie das Signal verstärkt und dabei Wahrscheinlichkeit verloren geht. Die Fläche unter der Ausgangsdichte ist deshalb kleiner als 1, und die Dichte sinkt überall.
--- falsch
Weil eine steile Kennlinie nur selten durchlaufen wird: Das Eingangssignal hält sich bevorzugt dort auf, wo die Kennlinie flach ist, und liefert in steilen Bereichen kaum Werte.
--- falsch
Weil die Dichte stets umgekehrt proportional zum Ausgangswert ist: Eine steile Kennlinie erzeugt große Ausgangswerte, und große Werte sind bei jeder Verteilung seltener.
:::
:::karte zusammenhang Aus einer Dreieckverteilung wird eine Gleichverteilung
Warum macht die Kennlinie $k(x)=2x-x^2$ für $x\ge0$, ungerade fortgesetzt, aus einer Dreieckverteilung auf $[-1,1]$ eine Gleichverteilung?
---
Weil sie bei $x=0$, wo die Dreieckdichte am größten ist, steil ist (Steigung 2) und am Rand flach. So werden die häufigen Werte auseinandergezogen, die seltenen zusammengeschoben; genau gilt $P_g(k(x))=P_s(x)$.
--- falsch
Weil sie bei $x=0$ flach ist (Steigung 0) und am Rand steil. So werden die häufigen Werte in der Mitte zusammengeschoben und die seltenen am Rand auseinandergezogen, bis alle Werte gleich häufig sind.
--- falsch
Weil sie das Signal quadriert und Quadrieren jede Verteilung gleichmäßiger macht. Der lineare Anteil $2x$ sorgt nur dafür, dass das Vorzeichen des Signals erhalten bleibt und die Werte im Intervall bleiben.
--- falsch
Weil sie die Dreieckdichte von der Dichte einer Gleichverteilung abzieht. Der Ausgang hat dann die Differenz beider Dichten als Dichte, und diese Differenz ist auf dem ganzen Intervall konstant.
:::
:::karte begriff Quantisierer
Was macht ein Quantisierer mit den Werten eines Signals, das durch ihn hindurchläuft?
---
Er ist eine Kennlinie, die jeden Wert durch den nächsten von $M$ Stufen ersetzt. Der Ausgang kann deshalb nur $M$ verschiedene Werte annehmen.
--- falsch
Er ist eine Kennlinie, die das Signal nur zu bestimmten Zeitpunkten abtastet. Der Ausgang besteht deshalb aus $M$ Abtastwerten je Sekunde, die Werte selbst bleiben unverändert.
--- falsch
Er ist eine Kennlinie, die jeden Wert auf das nächste Vielfache des Mittelwerts rundet. Der Ausgang ist deshalb immer ein ganzzahliges Vielfaches von $m_s$.
--- falsch
Er ist ein Filter, das die Schwankungen eines Signals in $M$ Frequenzbänder aufteilt. Jedes Band wird getrennt verstärkt, sodass das Rauschen gleichmäßig verteilt ist.
:::
:::karte formel Quantisierungsfehler
Welche Varianz hat der Fehler eines gleichförmigen Quantisierers, und welches Signal-Rausch-Verhältnis ergibt sich für ein gleichverteiltes Signal über alle $M$ Stufen?
---
Bei Stufen der Breite $\Delta$ ohne Übersteuerung ist der Fehler annähernd gleichverteilt zwischen $-\frac\Delta2$ und $\frac\Delta2$, mit der Varianz $\frac{\Delta^2}{12}$. Mit der Signalvarianz $\frac{(M\Delta)^2}{12}$ folgt $M^2$, also $20\lg M\approx6\,\text{dB je Bit}$.
--- falsch
Der Fehler ist gleichverteilt zwischen $-\Delta$ und $\Delta$, mit der Varianz $\frac{\Delta^2}{3}$, weil er bis zu einer ganzen Stufe betragen kann. Das Signal-Rausch-Verhältnis ist $M$, also $10\lg M\approx3\,\text{dB je Bit}$.
--- falsch
Der Fehler ist gleichverteilt zwischen $-\frac\Delta2$ und $\frac\Delta2$, mit der Varianz $\frac{\Delta^2}{12}$. Das Signal-Rausch-Verhältnis ist $M$, weil die Signalvarianz $M$-mal so groß ist wie die Fehlervarianz, also $10\lg M\approx3\,\text{dB je Bit}$.
--- falsch
Der Fehler ist gaußverteilt mit der Varianz $\Delta^2$, weil er aus vielen kleinen Rundungen entsteht. Das Signal-Rausch-Verhältnis ist $M^2$, also $20\lg M\approx6\,\text{dB}$ je zusätzlicher Stufe des Quantisierers.
:::
:::karte zusammenhang Optimaler Quantisierer
Wo liegen beim Quantisierer mit dem kleinsten mittleren quadratischen Fehler die Stufenwerte $v_i$ und die Schwellen $u_i$, und warum?
---
Jeder Stufenwert liegt im Schwerpunkt der Dichte auf seinem Intervall, weil dort die Ableitung des Fehlers nach $v_i$ null ist. Jede Schwelle liegt in der Mitte zwischen $v_{i-1}$ und $v_i$, damit jeder Wert der näheren Stufe zugeordnet wird.
--- falsch
Jeder Stufenwert liegt in der Mitte seines Intervalls, unabhängig von der Dichte, weil der Fehler in beide Richtungen gleich groß sein soll. Die Schwellen liegen dort, wo die Dichte ihr Maximum hat, damit dort am feinsten unterschieden wird.
--- falsch
Jeder Stufenwert liegt am Maximum der Dichte auf seinem Intervall, weil dort die meisten Werte auftreten. Jede Schwelle liegt im Schwerpunkt zwischen den beiden benachbarten Stufenwerten, gewichtet mit der Dichte des Signals.
--- falsch
Jeder Stufenwert liegt an der oberen Grenze seines Intervalls, damit kein Wert nach oben gerundet wird. Die Schwellen liegen in gleichen Abständen, weil nur ein gleichförmiger Quantisierer für jede Dichte optimal sein kann.
:::
::::
