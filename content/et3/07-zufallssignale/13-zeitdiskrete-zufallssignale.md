---
title: Stufe 12: Zeitdiskrete Zufallssignale
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3271300
summary: Alles gilt auch für Folgen von Zufallszahlen, mit Summen statt Integralen.
tags: Zeitdiskretes weißes Rauschen
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Alles gilt auch für Folgen von Zufallszahlen, mit Summen statt Integralen.
:::

Tastet man einen auf $f_\mathrm g$ bandbegrenzten Prozess mit $T\le\frac{1}{2f_\mathrm g}$ ab, bilden die Abtastwerte einen zeitdiskreten Prozess $s(n)$. Verteilungen, Erwartungswerte und Korrelationen sind wie zuvor definiert, die Zeitmittel sind Summen, etwa $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$. Durch ein LSI-System mit $h(n)$:

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

mit dem periodischen Leistungsdichtespektrum $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$ und $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$. __Zeitdiskretes weißes Rauschen__ hat $\Phi_{ss,\mathrm a}=N$ und $\varphi_{ss}(m)=N\delta(m)$: Aufeinanderfolgende Zahlen sind unkorreliert. Anders als im Kontinuierlichen ist seine Leistung endlich, $L_s=N$.

::::beispiel [Beispiel 1] Mittelung zweier Werte
Gleichverteiltes weißes Rauschen ($\sigma_s^2=\frac1{12}$) durch $h(n)=\frac12[\delta(n)+\delta(n-1)]$, also $g(n)=\frac12[s(n)+s(n-1)]$. Mit $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$:

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

Die Varianz halbiert sich auf $\frac{1}{24}$, und benachbarte Ausgangswerte sind jetzt korreliert (sie teilen sich einen Eingangswert). Die Ausgangswerte sind dreieckverteilt, weil jeder die halbe Summe zweier unabhängiger, gleichverteilter Zahlen ist. Eine Simulation mit 200 000 Zahlen ergibt die Varianz 0,0415 statt $\frac1{24}=0{,}0417$.
::::

::::beispiel [Beispiel 2] Rekursives Filter (AR(1)-Prozess)
Weißes Rauschen der Varianz $\sigma_s^2$ durch $h(n)=b^n\varepsilon(n)$ ([Kapitel 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)). Mit $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$:

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

Für $b=0{,}6$ ist die Varianz das $1{,}56$-Fache der Eingangsvarianz, und benachbarte Werte haben den Korrelationskoeffizienten $0{,}6$. Je näher $b$ an 1, desto stärker die tiefen Frequenzen (Abb. [5](#abb-5)).

:::abbildung et3/k7ar 5
Leistungsdichtespektren von AR(1)-Prozessen, periodisch mit 1. Bei $b=0{,}6$ reicht es von 6,25 ($f=0$) bis 0,39 ($f=\frac12$), bei $b=0{,}9$ von 100 bis 0,28.
:::
::::

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
