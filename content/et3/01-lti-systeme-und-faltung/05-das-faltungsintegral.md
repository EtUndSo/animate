---
title: Stufe 4: Das Faltungsintegral
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210500
summary: Mit Linearität und Zeitinvarianz lässt sich die Antwort auf jedes Signal aus der Antwort auf einen einzigen kurzen Impuls berechnen.
tags: Dirac-Impuls, Impulsantwort
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Mit Linearität und Zeitinvarianz lässt sich die Antwort auf *jedes* Signal aus der Antwort auf einen einzigen kurzen Impuls berechnen. Das Ergebnis ist das Faltungsintegral.
:::

**Die Idee in vier Schritten.**

<ol>

<li>

⁠**Zerlegen.** Man nähert das Eingangssignal durch eine Treppe aus schmalen Rechtecken der Breite $T_0$. Als Baustein dient ein Rechteck $s_0(t)$ der Dauer $T_0$ und der Höhe $1/T_0$, also der Fläche 1. Die Stufe bei $nT_0$ ist dieser Baustein, verschoben um $nT_0$ und gewichtet mit $s(nT_0)\,T_0$, der Fläche des Streifens:

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**Ein Baustein durch das System.** Auf $s_0$ antwortet das System mit $g_0(t)$. Das muss man einmal kennen.

</li>

<li>

⁠**Zusammensetzen.** Zeitinvarianz: Der verschobene Baustein erzeugt die verschobene Antwort. Linearität: Gewichte und Summe gehen durch. Also

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**Grenzübergang $T_0\to0$.** Die Treppe wird zum Signal. Das Rechteck der Fläche 1 wird zum __Dirac-Impuls__ $\delta(t)$, einem unendlich kurzen Stoß der Fläche 1. Seine Antwort heißt __Impulsantwort__ $h(t)$. Aus $nT_0$ wird die stetige Variable $\tau$, aus $T_0$ das Differential $\mathrm{d}\tau$, aus den Summen Integrale.

</li>

</ol>

:::abbildung et3/k1treppe 5
Oben: Ein Dreieckimpuls $s(t)=\Lambda(t-1)$ und seine Treppennäherung mit $T_0=0{,}5$ s. Unten: die exakte Antwort des RC-Glieds und die Summe der verschobenen Rechteckantworten. Die größte Abweichung sinkt von 0,17 ($T_0=0{,}5$ s) über 0,08 ($0{,}25$ s) auf 0,03 ($0{,}1$ s).
:::

:::satz Satz 4.1 (Faltungsintegral)
<span class="anker" id="satz-4-1"></span>

Für jedes Signal $s(t)$ gilt

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

und ein LTI-System mit der Impulsantwort $h(t)$ antwortet darauf mit

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**So liest man das:** $\tau$ ist der Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht (die Fläche des Streifens). $h(t-\tau)$ ist die Antwort des Systems zur Zeit $t$ auf einen Stoß, der zur Zeit $\tau$ kam, also vor $t-\tau$ Sekunden. Der Ausgang sammelt alle Stöße der Vergangenheit, jeden gewichtet damit, wie stark sich das System nach dieser Zeit noch an ihn „erinnert“. Die Gleichung gilt exakt und für jedes LTI-System.

⁠**Kurz gesagt:** Der Ausgang eines LTI-Systems ist die Überlagerung seiner Impulsantworten, verschoben an jeden Zeitpunkt des Eingangs und gewichtet mit dem Eingang dort.

:::frage Warum müssen die Rechteckbausteine die Fläche 1 haben?
Damit die Antwort auf den Baustein beim Grenzübergang eine feste Form behält. Ein Rechteck der festen Höhe 1 hätte für $T_0\to0$ die Fläche null, und seine Antwort würde verschwinden. Mit der Höhe $1/T_0$ bleibt die Fläche 1, und die Antwort strebt gegen $h(t)$. Beim RC-Glied ist die Spitze der Antwort $(1-\mathrm{e}^{-T_0})/T_0$: 0,632 für $T_0=1$ s, 0,787 für 0,5 s, 0,952 für 0,1 s, und für $T_0\to0$ wird sie $1=h(0^+)$. Die Fläche der Antwort bleibt dabei immer 1.
:::

:::frage Gibt es den Stoß $\delta(t)$ in Wirklichkeit? Wie misst man dann $h(t)$?
Einen unendlich kurzen Stoß gibt es nicht. Es genügt aber jeder Impuls, der viel kürzer ist als die Zeitkonstanten des Systems. Dann sieht das System nur seine Fläche, und die Antwort ist praktisch $(\text{Fläche})\cdot h(t)$. Beim RC-Glied mit $RC=1$ s weicht die Spitze der Antwort auf einen 1-ms-Impuls nur um 0,05 % von $h(0^+)$ ab. So misst man Impulsantworten auch: Man klatscht in einem Raum in die Hände und nimmt den Nachhall auf.
:::

:::ltspice Impulsantwort mit einem kurzen Rechteck nähern
⁠**Zeichnen:** das RC-Glied aus Stufe [2](ein-erstes-system-das-rc-glied.html#stufe-2) mit der Quelle `PULSE(0 {1/T0} 0 1n 1n {T0})`: ein Rechteck der Breite $T_0$ und der Höhe $1/T_0$, also der Fläche 1.

⁠**Direktiven:** `.param T0=1`, `.step param T0 list 1 0.5 0.1 1m`, `.tran 0 10 0 1m`, `.meas tran spitze MAX V(out)`, `.meas tran flaeche INTEG V(out)`.

⁠**Was du siehst:** Die Spitzen sind 0,632; 0,787; 0,952 und 0,9995, wie $(1-\mathrm{e}^{-T_0})/T_0$. Beim 1-ms-Impuls ist die Antwort praktisch schon $h(t)=\mathrm{e}^{-t}$. Die Fläche ist in allen vier Läufen 1,000: Ein Impuls, der viel kürzer ist als $RC$, wirkt nur über seine Fläche.
:::

:::aufgabe Aufgabe 4 ★★ Die Treppe genauer
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Berechne die Antwort $g_0(t)$ des RC-Glieds ($RC=1$ s) auf das Rechteck der Höhe $1/T_0$ von $0$ bis $T_0$. Benutze dazu [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5) und schreibe das Rechteck als Differenz zweier Sprünge.

</li>

<li>

Zeige, dass $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$ ist und für $T_0\to0$ gegen 1 strebt.

</li>

<li>

Warum ist die Näherung $g_a$ in Abb. [5](#abb-5) zu spät? (Tipp: Wo liegt die Stufe im Vergleich zum Dreieck auf der steigenden und auf der fallenden Flanke?)

</li>

</ol>

:::loesung
(a) Das Rechteck ist $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$. Linearität und Zeitinvarianz mit der Sprungantwort [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5):

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) Bei $t=T_0$ ist der zweite Summand null: $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$. Mit $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$ für kleine $T_0$ ist das $\approx1-T_0/2\to1=h(0^+)$. Zahlen: 0,632; 0,787; 0,952 für $T_0=1$; 0,5; 0,1 s.

(c) Jede Stufe hält den Wert $s(nT_0)$ vom *Anfang* des Intervalls bis zu dessen Ende. Auf der steigenden Flanke liegt die Treppe deshalb unter dem Dreieck, auf der fallenden darüber: Sie ist im Mittel um $T_0/2$ verzögert. Der Ausgang erbt diese Verzögerung, auf der abfallenden Seite liegt $g_a$ über $g$ ($g_a(2)=0{,}508$ statt $0{,}400$ für $T_0=0{,}5$ s). Mit kleinerem $T_0$ schrumpft die Verzögerung und mit ihr der Fehler.
:::
:::

::::kurzfassung
Ein LTI-System ist durch seine Antwort auf einen einzigen, unendlich kurzen Stoß vollständig beschrieben. Die Antwort auf jedes andere Signal liefert das Faltungsintegral.

Man nähert den Eingang durch eine Treppe aus schmalen Rechtecken der Breite $T_0$. Baustein ist ein Rechteck $s_0(t)$ der Höhe $1/T_0$, also der Fläche 1; die Stufe bei $nT_0$ trägt das Gewicht $s(nT_0)\,T_0$. Das System antwortet auf $s_0$ mit $g_0(t)$. Die Zeitinvarianz liefert zu jedem verschobenen Baustein die verschobene Antwort, die Linearität überträgt Gewichte und Summe. Für $T_0\to0$ wird das Rechteck der Fläche 1 zum __Dirac-Impuls__ $\delta(t)$, einem unendlich kurzen Stoß der Fläche 1. Die Antwort darauf heißt __Impulsantwort__ $h(t)$. Aus der Summe wird das Integral

$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau .$$

Darin ist $\tau$ der Zeitpunkt eines Eingangsstoßes und $s(\tau)\,\mathrm{d}\tau$ sein Gewicht. $h(t-\tau)$ ist die Antwort zur Zeit $t$ auf einen Stoß, der vor $t-\tau$ Sekunden kam. Der Eingang selbst ist eine Überlagerung solcher Stöße, $s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$. Die Zerlegung gilt für jedes Signal, das Faltungsintegral exakt für jedes LTI-System.

Anschaulich sammelt der Ausgang alle Stöße der Vergangenheit, jeden gewichtet damit, wie stark sich das System nach dieser Zeit noch an ihn „erinnert“.

Falle: Die Bausteine brauchen die Fläche 1. Ein Rechteck der festen Höhe 1 hätte für $T_0\to0$ die Fläche null, und seine Antwort würde verschwinden. Zum Messen von $h(t)$ genügt ein Impuls, der viel kürzer ist als die Zeitkonstanten des Systems, beim RC-Glied also viel kürzer als $RC$: Das System sieht dann nur seine Fläche.
::::

::::formelsammlung
**Treppennäherung des Eingangs**

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0$$

$s_0(t)$ Rechteck der Dauer $T_0$ und der Höhe $1/T_0$, also der Fläche 1; $s(nT_0)\,T_0$ Fläche des Streifens bei $nT_0$.

**Summe der Bausteinantworten**

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t)$$

$g_0(t)$ Antwort des Systems auf $s_0(t)$; folgt aus Zeitinvarianz (verschobener Baustein, verschobene Antwort) und Linearität (Gewichte und Summe).

**Zerlegung in Stöße**

$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau$$

Für jedes Signal $s(t)$. Grenzübergang $T_0\to0$: $s_0$ wird zum Dirac-Impuls $\delta(t)$ (unendlich kurzer Stoß der Fläche 1), $nT_0\to\tau$, $T_0\to\mathrm{d}\tau$.

**Faltungsintegral**

$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$$

Exakt für jedes LTI-System; $h(t)$ Impulsantwort (Antwort auf $\delta(t)$). $\tau$ Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht, $h(t-\tau)$ Antwort zur Zeit $t$ auf einen Stoß, der vor $t-\tau$ Sekunden kam.
::::
