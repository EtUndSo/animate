---
title: Stufe 5: Korrelation und LTI-Systeme
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260600
summary: Was macht ein LTI-System mit der AKF und dem Energiedichtespektrum?
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Was macht ein LTI-System mit der AKF und dem Energiedichtespektrum? Und wie misst man ein System mit der Kreuzkorrelation?
:::

:::satz Satz 5.1 (Wiener-Lee)
<span class="anker" id="satz-5-1"></span>

Für $g=s*h$:

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung Wiener-Lee
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$. Nach Kommutativ- und Assoziativgesetz umsortieren: $[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$. Ebenso $\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$.
:::

⁠**So liest man das:** Das System multipliziert die Energie bei jeder Frequenz mit $|H|^2$. Die Phase des Systems spielt für die Energie keine Rolle. [(5.2)](#gl-5-2) ist ein Messverfahren: Hat der Eingang eine AKF, die fast ein gewichteter Dirac-Impuls $c\,\delta(\tau)$ ist (etwa ein sehr kurzer Impuls), dann ist die Kreuzkorrelation zwischen Eingang und Ausgang fast $c\,h(\tau)$, also bis auf den Faktor $c$ die Impulsantwort. Anders als $|H|^2$ enthält sie auch die Phase.

:::ltspice Energie vor und hinter dem RC-Glied
⁠**Zeichnen:** Verhaltensquelle `bv` am Netz `s` mit `V=exp(-time)*(time>0)`, der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$. Der Faktor `(time>0)` sorgt dafür, dass LTspice den Anfangszustand bei $t=0$ mit 0 V rechnet und der Kondensator leer startet. Dahinter das RC-Glied (`res` mit `1Meg`, `cap` mit `1u`) mit dem Ausgang am Netz `g`.

⁠**Direktiven:** `.tran 0 30 0 1m`, `.meas tran Es INTEG V(s)*V(s)` und `.meas tran Eg INTEG V(g)*V(g)`, die Energien nach [(1.1)](energie-und-leistung.html#gl-1-1).

⁠**Was du siehst:** `Es` $=0{,}500$, wie $E_s=\varphi^E_{ss}(0)=\frac12$ in Stufe [4](energiedichtespektrum.html#stufe-4). Vergleiche `Eg` mit deinem Ergebnis aus Aufgabe [5](#aufg-5). Die Ausgangsenergie ist kleiner, weil das RC-Glied die Energie bei jeder Frequenz mit $|H|^2\le1$ multipliziert.
:::

:::aufgabe Aufgabe 5 ★★ Energie am Ausgang
<span class="anker" id="aufg-5"></span>

Der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ geht durch ein RC-Glied mit $RC=1$ s.

<ol class="al">

<li>

Bestimme $|G(f)|^2$ und daraus die Ausgangsenergie. Tipp: $\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$.

</li>

<li>

Prüfe im Zeitbereich mit $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ ([Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), zwei RC-Glieder in Kette).

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$. Mit $x=2\pi f$: $E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$.

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$. Beide Wege stimmen überein. Die Energie sinkt von $\frac12$ auf $\frac14$, weil das zweite RC-Glied die höheren Frequenzen weiter dämpft.
:::
:::
