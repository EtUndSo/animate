---
title: Stufe 5: Die Faltung ausrechnen
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / LTI-Systeme und Faltung
order: 3210600
summary: Das Integral (4.2) ist für konkrete Signale auszuwerten.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Das Integral [(4.2)](das-faltungsintegral.html#gl-4-2) ist für konkrete Signale auszuwerten. Der Schlüssel ist, beide Faktoren über der Integrationsvariablen $\tau$ zu zeichnen.
:::

**Das Rezept.** Für einen festen Zeitpunkt $t$:

<ol>

<li>

$s(\tau)$ über $\tau$ zeichnen.

</li>

<li>

$h(-\tau)$ zeichnen: $h$ an der senkrechten Achse *spiegeln*.

</li>

<li>

$h(t-\tau)$: das gespiegelte $h$ um $t$ nach rechts *schieben*.

</li>

<li>

Beide *multiplizieren* und über $\tau$ *integrieren*: Das ist $g(t)$.

</li>

</ol>

Lässt man $t$ wachsen, gleitet das gespiegelte $h$ von links nach rechts über $s$. Wo sich die beiden nicht überlappen, ist $g(t)=0$.

Warum gespiegelt? Als Funktion von $\tau$ fällt das Argument $t-\tau$, wenn $\tau$ wächst. Der Anfang von $h$ (Alter null) liegt bei $\tau=t$, ältere Stöße liegen weiter links. Beim RC-Glied ist $h$ am Anfang am größten: Das System „erinnert“ sich an die jüngste Vergangenheit am stärksten.

**Beispiel: RC-Glied und Rechteckimpuls.** Die Impulsantwort des RC-Glieds mit der Zeitkonstanten $T=RC$ ist ein abfallender Exponentialimpuls der Fläche 1. Der kurze Stoß lädt den Kondensator schlagartig auf $1/T$, danach entlädt er sich über $R$:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

Eingang: Rechteck der Höhe $a$ von $0$ bis $T_0$. Abbildung [6](#abb-6) zeigt die Lage der beiden Faktoren für zwei Zeitpunkte. Es gibt drei Bereiche:

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$

:::herleitung Antwort auf den Rechteckimpuls
⁠**$t<0$:** Das geschobene $h(t-\tau)$ ist nur für $\tau\le t<0$ von null verschieden, $s(\tau)$ nur für $\tau\ge0$. Keine Überlappung, $g=0$.

⁠**$0\le t\le T_0$:** Überlappung für $0<\tau<t$:

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$:** Überlappung nur noch für $0<\tau<T_0$:

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

Im Rechenmodell ($a=1$, $T_0=T=1$ s): $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$, $g(3)=0{,}0855$. Das ist dieselbe Kurve wie $g_0$ in Abb. [4](was-ein-lti-system-ist.html#abb-4).

:::abbildung et3/k1schieben 6
Faltung grafisch, $a=1$, $T_0=T=1$ s. Blau: $s(\tau)$. Rot: gespiegeltes und um $t$ geschobenes $h(t-\tau)$. Die orange Fläche ist $g(t)$: 0,3935 bei $t=0{,}5$ s (teilweise Überlappung), 0,2325 bei $t=2$ s (das ganze Rechteck liegt im abgeklungenen Teil von $h$). Rechts die vollständige Antwort mit beiden Punkten.
:::

:::frage Warum spiegelt man $h$ und nicht $s$?
Man darf auch $s$ statt $h$ spiegeln: Die Substitution $\tau'=t-\tau$ macht aus $\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ das Integral $\int s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$. Man spiegelt die Funktion, bei der das Schieben übersichtlicher ist, meist die mit der einfacheren Form.
:::

:::ltspice Antwort auf den Rechteckimpuls
⁠**Zeichnen:** das RC-Glied aus Stufe [2](ein-erstes-system-das-rc-glied.html#stufe-2) mit der Quelle `PULSE(0 1 0 1u 1u 1)`: Höhe 1 V, Dauer 1 s.

⁠**Direktiven:** `.tran 0 20 0 1m`, je Zeitpunkt eine Messung wie `.meas tran g2 FIND V(out) AT=2`, dazu `.meas tran gmax MAX V(out)` und `.meas tran flaeche INTEG V(out)`.

⁠**Was du siehst:** $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$ und $g(3)=0{,}0855$, genau wie nach [(5.2)](#gl-5-2). Vergleiche `gmax` und `flaeche` mit deinem Ergebnis aus Aufgabe [6](#aufg-6).
:::

:::aufgabe Aufgabe 5 ★★ Rechteck mit Rechteck
<span class="anker" id="aufg-5"></span>

Berechne $\operatorname{rect}(t)*\operatorname{rect}(t)$ mit dem Rezept. Unterscheide $|t|>1$, $-1\le t\le0$ und $0\le t\le1$. Welches Elementarsignal kommt heraus?

:::loesung
Das gespiegelte Rechteck ist wieder $\operatorname{rect}$ (symmetrisch), geschoben liegt es auf $[t-\frac12,t+\frac12]$. Das Integral ist die Länge der Überlappung mit $[-\frac12,\frac12]$:

<ul>

<li>

$|t|>1$: keine Überlappung, 0.

</li>

<li>

$-1\le t\le0$: Überlappung von $-\frac12$ bis $t+\frac12$, Länge $1+t$.

</li>

<li>

$0\le t\le1$: Überlappung von $t-\frac12$ bis $\frac12$, Länge $1-t$.

</li>

</ul>

Zusammen $1-|t|$ für $|t|\le1$: $\operatorname{rect}*\operatorname{rect}=\Lambda$. Numerisch: 1,000; 0,500; 0,200 bei $t=0$; 0,5; 0,8.
:::
:::

:::aufgabe Aufgabe 6 ★★ Die Rechteckantwort prüfen
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Zeige, dass [(5.2)](#gl-5-2) bei $t=T_0$ stetig ist. Warum muss sie stetig sein?

</li>

<li>

Wo hat $g(t)$ sein Maximum, und wie groß ist es im Rechenmodell?

</li>

<li>

Zeige, dass die Fläche unter $g(t)$ gleich $aT_0$ ist, und begründe das ohne Rechnung mit $\int h\,\mathrm{d} t=1$.

</li>

</ol>

:::loesung
(a) Bei $t=T_0$: $a(1-\mathrm{e}^{-T_0/T})$ und $a(\mathrm{e}^{T_0/T}-1)\mathrm{e}^{-T_0/T}=a(1-\mathrm{e}^{-T_0/T})$, gleich. Physikalisch: Die Kondensatorspannung kann nicht springen, dafür bräuchte es einen unendlichen Strom. Mathematisch: Die Faltung eines beschränkten Signals mit einem integrierbaren $h$ ist stetig.

(b) Während des Impulses steigt $g$, danach fällt es. Das Maximum liegt bei $t=T_0$: $g(1\,\mathrm{s})=1-\mathrm{e}^{-1}=0{,}632$.

(c) Rechnung:

$$\int g\,\mathrm{d} t=a\Bigl[T_0-T\bigl(1-\mathrm{e}^{-T_0/T}\bigr)\Bigr]+a\bigl(\mathrm{e}^{T_0/T}-1\bigr)T\mathrm{e}^{-T_0/T}=aT_0.$$

Ohne Rechnung: Die Fläche einer Faltung ist das Produkt der Flächen, $\int g\,\mathrm{d} t=\int\!\!\int s(\tau)h(t-\tau)\,\mathrm{d}\tau\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$. Numerisch: 1,000.
:::
:::
