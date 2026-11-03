---
title: Stufe 5: Warum man auch den Eingang transformiert
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220800
summary: Jedes Signal als Überlagerung von $\mathrm{e}^{pt}$, und warum ein LTI-System daraus eine Multiplikation macht
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::frage Die Transformation von $h(t)$ ist nützlich: $H(p)$ multipliziert die Eigenfunktionen, und daraus folgt der Ausgang. Wozu aber das Eingangssignal $s(t)$ transformieren? Zwar ist $s*h=h*s$, doch $h(t)$ ist meist keine Eigenfunktion, $h(t)\cdot S(p)$ ergibt also keinen Sinn. Welche Bedeutung für das System hat es, ein beliebiges Signal zu transformieren?
⁠**Was an der Frage stimmt:** $H(p)$ sagt, was das System mit einem Baustein $\mathrm{e}^{pt}$ macht. Und $h(t)\cdot S(p)$ ergibt tatsächlich keinen Sinn.

⁠**Wo der Denkfehler liegt:** Auch der Eingang ist fast nie eine Eigenfunktion. Ein Sprung, ein Sprachsignal, ein Rechteckimpuls sind keine einzelnen Bausteine $\mathrm{e}^{pt}$. Deshalb ergibt $H(p)\cdot s(t)$ genauso wenig Sinn wie $h(t)\cdot S(p)$: $H(p)$ darf nur auf einen Baustein angewandt werden, und für ein beliebiges $s(t)$ ist gar nicht klar, welches $p$ gemeint sein soll. Bevor $H(p)$ irgendetwas tun kann, muss der Eingang in Bausteine zerlegt sein. Genau das leistet $S(p)$.

⁠**Die richtige Sicht:** Im Faltungssatz $G(p)=H(p)\,S(p)$ hat jeder Faktor eine eigene, systembezogene Bedeutung:

<ul>

<li>

$S(p)$ ist das *Rezept des Eingangs*: wie viel vom Baustein $\mathrm{e}^{pt}$ im Eingang steckt;

</li>

<li>

$H(p)$ ist die *Wirkung des Systems*: mit welcher Zahl es diesen Baustein multipliziert;

</li>

<li>

$G(p)$ ist das Rezept des Ausgangs.

</li>

</ul>

Ohne $S(p)$ kennt man nur die Wirkung auf einzelne Bausteine, aber nicht, welche Bausteine ankommen. $H(p)$ allein beantwortet die Frage „Was passiert mit dem Ausgang?“ nur für den einen Sonderfall, dass der Eingang selbst ein einzelner Baustein ist.

⁠**Am Beispiel Sprung und RC-Tiefpass.** Der Sprung hat das Rezept $S(p)=1/p$. Auf der Linie $\sigma=0{,}5/\mathrm s$ ist $|S|=2$ bei $f=0$, $0{,}16$ bei 1 Hz und $0{,}016$ bei 10 Hz. Die schnellen Bausteine sind schwach, aber vorhanden, und sie bilden die scharfe Kante (Abb. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3): Je mehr schnelle Bausteine, desto steiler die Kante). Der RC-Tiefpass multipliziert sie mit $|H|=0{,}67$, $0{,}15$ und $0{,}016$. Im Ausgang sind die schnellen Bausteine also noch einmal etwa um den Faktor $2\pi f\cdot RC$ schwächer (für $f\gg1/(2\pi RC)=0{,}16$ Hz), und die Kante ist weg: $g(t)=1-\mathrm{e}^{-t}$ steigt stetig an. Diese Erklärung braucht beide Transformierten. $H$ allein sagt nur „schnelle Bausteine werden geschwächt“, erst $S$ sagt, dass die Kante aus schnellen Bausteinen besteht.

⁠**Und die Symmetrie $s*h=h*s$?** Mathematisch sind beide Signale gleichberechtigt: Man kann auch $h$ als Eingang und $s$ als „System“ lesen, dann ist $H(p)$ das Rezept und $S(p)$ die Wirkung. Die Systemtheorie verteilt die Rollen nur nach der Physik: Das eine Signal kommt von außen, das andere beschreibt die Schaltung. Im Bildbereich werden dabei immer *beide* transformiert.
:::

**Weitere Gründe, ein Signal für sich zu transformieren.**

<ul>

<li>

⁠**Ein System ausmessen.** Misst man Eingang und Ausgang eines unbekannten Systems, liefert $H(p)=G(p)/S(p)$ das System. Dafür transformiert man zwei Signale, jedes für sich (Aufgabe [9](#aufg-9)).

</li>

<li>

⁠**Das Signal selbst verstehen.** Der Ton einer angeschlagenen Glocke ist eine Summe gedämpfter Schwingungen, jede ein konjugiertes Polpaar. $\operatorname{Im} p_r$ ist die Tonhöhe eines Teiltons, $-\operatorname{Re} p_r$ seine Abklingrate. Wenige Pole beschreiben den ganzen Klang. Ein Messgerät, das ein Spektrum anzeigt, tut dasselbe auf der Linie $\sigma=0$.

</li>

<li>

⁠**Faltung ohne System.** Die Faltung überlagert verschobene, gewichtete Kopien eines Signals. Das System ist eine Deutung dieser Operation, nicht die einzige. Ein Beispiel ganz ohne System ist die Augensumme zweier Würfel (Kapitel zur Faltung).

</li>

</ul>

:::ltspice Ein Netzwerk zu zwei Messungen
⁠**Zeichnen:** das Netzwerk, das du in Aufgabe [9](#aufg-9)(c) gefunden hast, mit der Quelle `PULSE(0 1 0 1u 1u 100)` am Eingang und dem Ausgang am Netz `out`. Daneben, ohne Verbindung zur Schaltung, eine Verhaltensquelle `bv` am Netz `mess` mit `V=1-exp(-2*time)`. Sie spielt die gemessene Ausgangskurve.

⁠**Direktiven:** `.tran 0 3 0 1m`, `.meas tran abw MAX abs(V(out)-V(mess))`.

⁠**Was du siehst:** Stimmen Netzwerk und Bauteilwerte, liegen `V(out)` und `V(mess)` übereinander, und die größte Abweichung `abw` ist praktisch null (unter $10^{-5}$). Vergleiche so die Kurven mit deinem Ergebnis aus Aufgabe [9](#aufg-9)(c).
:::

:::aufgabe Aufgabe 8 ★★ Welche Bausteine bilden die Kante?
<span class="anker" id="aufg-8"></span>

Eingang $\varepsilon(t)$, System RC-Tiefpass mit $RC=1$ s. Betrachte die Bausteine auf der Linie $\sigma=0{,}5/\mathrm s$.

<ol class="al">

<li>

Berechne $|S(p)|$, $|H(p)|$ und $|G(p)|$ für $f=0$, $1$ Hz und $10$ Hz.

</li>

<li>

Um welchen Faktor schwächt das System die Bausteine bei 10 Hz stärker als die bei 1 Hz?

</li>

<li>

Erkläre mit (a) und Abb. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3), warum der Ausgang keine Kante hat. Warum reicht $H(p)$ allein für diese Erklärung nicht?

</li>

</ol>

:::loesung
(a) Mit $p=0{,}5+\mathrm{j}2\pi f$ (in $1/\mathrm s$), $S=1/p$, $H=1/(p+1)$, $G=SH$:

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0,667 | 1,33 |
| 1 Hz | 0,159 | 0,155 | 0,0246 |
| 10 Hz | 0,0159 | 0,0159 | 0,000253 |

(b) $0{,}155/0{,}0159\approx9{,}7$, also fast um den Faktor 10, so wie die Frequenz. Für große $|p|$ ist $|H|\approx1/|p|\approx1/(2\pi f)$.

(c) Die Kante des Sprungs besteht aus den schnellen Bausteinen: In Abb. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3) wird sie steiler, je mehr davon mitgenommen werden. Im Eingang fallen ihre Gewichte wie $1/f$, im Ausgang wie $1/f^2$. Die schnellen Bausteine sind im Ausgang so schwach, dass keine Kante mehr entsteht, und $g(t)$ steigt stetig an. $H(p)$ allein sagt nur, dass schnelle Bausteine geschwächt werden. Dass die Kante aus genau diesen Bausteinen besteht, ist eine Aussage über den Eingang, und die steht in $S(p)$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Ein unbekanntes System aus zwei Messungen
<span class="anker" id="aufg-9"></span>

An ein unbekanntes kausales LTI-System wird zur Zeit $t=0$ eine Spannung von 1 V angelegt, $s(t)=\varepsilon(t)$ in V. Am Ausgang misst man $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$ in V ($t$ in s).

<ol class="al">

<li>

Transformiere beide Signale, jedes für sich.

</li>

<li>

Bestimme $H(p)$ und daraus $h(t)$.

</li>

<li>

Um welches Netzwerk könnte es sich handeln? Welcher Wert ergibt sich?

</li>

<li>

Welcher Pol in $G(p)$ stammt vom Eingang, welcher vom System?

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$ für $\operatorname{Re} p>0$. $G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$ für $\operatorname{Re} p>0$ (Grundpaar [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) mit $p_0=0$ und $p_0=-2$).

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$. Da das System kausal ist, liegt der Konvergenzbereich rechts vom Pol: $\operatorname{Re} p>-2$. Mit [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2): $h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$ in $1/\mathrm s$.

(c) Ein RC-Tiefpass hat $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$. Der Vergleich mit $\dfrac{2}{p+2}$ ergibt $RC=0{,}5$ s, zum Beispiel $R=500\,\mathrm{k\Omega}$ und $C=1$ µ F. (Jedes andere Netzwerk mit derselben Übertragungsfunktion verhielte sich an den Klemmen genauso. Aus Messungen an Ein- und Ausgang kennt man nur $H$, nicht die Bauteile.)

(d) Der Pol $p=0$ stammt vom Eingang (Sprung), der Pol $p=-2$ vom System. Beim Teilen $G/S$ kürzt sich genau der Pol des Eingangs heraus.
:::
:::
