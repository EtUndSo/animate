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
