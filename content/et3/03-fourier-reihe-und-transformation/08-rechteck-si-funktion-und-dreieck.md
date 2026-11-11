---
title: Stufe 7: Rechteck, si-Funktion und Dreieck
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230800
summary: Drei Transformationspaare kommen ständig vor.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Drei Transformationspaare kommen ständig vor. Mit den Theoremen folgen sie aus einer einzigen Rechnung.
:::

**Rechteck.** Mit $\operatorname{si}(x)=\sin(x)/x$:

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz Satz 7.1 (Rechteck, si und Dreieck)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**So liest man das:** Ein Rechteck der Dauer $T$ hat ein Spektrum der Höhe $T$ (seine Fläche) mit Nullstellen bei allen von null verschiedenen Vielfachen von $1/T$. Doppelt so lang heißt halb so breit im Spektrum (Abb. [6](#abb-6)). [(7.2)](#gl-7-2) folgt aus der Symmetrie, [(7.3)](#gl-7-3) aus dem Faltungssatz, und [(7.4)](#gl-7-4) gilt, weil im Frequenzbereich $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$ ist: Ein idealer Tiefpass ändert ein Signal nicht, das schon auf sein Band begrenzt ist.

:::abbildung et3/k3rectsi 6
$\operatorname{rect}(t/T)$ und sein Spektrum $|T|\operatorname{si}(\pi Tf)$ für $T=1$ s und $T=2$ s. Doppelte Dauer: doppelte Höhe ($=$ Fläche), halbe Breite, erste Nullstelle bei $1/T$.
:::

:::ltspice Spektrum eines Rechteckimpulses
⁠**Zeichnen:** nur eine Quelle `voltage` mit `PULSE(0 1 0 1u 1u {T0} 16)`: ein Rechteck der Dauer $T_0$, alle 16 s wiederholt.

⁠**Direktiven:** `.param T0=1`, `.step param T0 list 1 2`, `.tran 0 16 0 1m`, `.options plotwinsize=0`, `.four 0.0625 40 V(in)`.

⁠**Was du siehst:** Die Wiederholung alle 16 s macht aus dem Spektrum Linien im Abstand $1/16$ Hz (Stufe [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4)). `.four` gibt ihre Amplituden $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$ an, also Abtastwerte der si-Hüllkurve. Bei $T_0=1$ s sind die Linien bei 1 Hz und 2 Hz null, bei $T_0=2$ s schon die bei 0,5 Hz, 1 Hz, 1,5 Hz und 2 Hz. Der Gleichanteil verdoppelt sich von 0,0625 auf 0,125. Doppelte Dauer heißt also halbe Breite und doppelte Höhe, wie in Abb. [6](#abb-6). In der FFT-Ansicht siehst du die Hüllkurve mit ihren Nullstellen direkt.
:::

:::aufgabe Aufgabe 8 ★ Flächen und Energie der si-Funktion
<span class="anker" id="aufg-8"></span>

Berechne ohne Integration $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ und $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$. Benutze den Flächensatz und Parseval.

:::loesung
Flächensatz: $\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$. Parseval: $\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Dreieck und Mehrfachfaltung
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Bestimme das Spektrum von $\Lambda(t/2)$ (Dreieck der halben Breite 2 s). Wo liegen die Nullstellen?

</li>

<li>

Welches Spektrum hat $\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$? Warum fallen die Nebenzipfel umso schneller ab, je öfter man faltet?

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$ und Ähnlichkeit mit $T=2$: $\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$. Nullstellen bei $f=k/2$, $k\neq0$.

(b) $\operatorname{si}^3(\pi f)$. Jede weitere Faltung multipliziert das Spektrum mit $\operatorname{si}(\pi f)$, das in den Nebenzipfeln wie $1/(\pi f)$ abfällt. Bei $M$ gefalteten Rechtecken fallen die Nebenzipfel wie $1/f^M$. Im Zeitbereich: Das Rechteck springt (Abfall $1/f$), das Dreieck hat Knicke ($1/f^2$), die dreifache Faltung hat eine stetige Ableitung ($1/f^3$). Je glatter ein Signal, desto schneller fällt sein Spektrum ab.
:::
:::

::::kurzfassung
Drei Transformationspaare kommen ständig vor: Rechteck, si-Funktion und Dreieck. Alle folgen aus einer einzigen Rechnung und den Rechenregeln.

Die __si-Funktion__ ist $\operatorname{si}(x)=\sin(x)/x$, an der Stelle null durch ihren Grenzwert 1 ergänzt. Das Rechteck $\operatorname{rect}(t)$ hat das Spektrum $\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t=\operatorname{si}(\pi f)$. Mit der Ähnlichkeit folgt für ein Rechteck der Dauer $|T|$

$$\operatorname{rect}\Bigl(\frac tT\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf).$$

Die Symmetrie liefert umgekehrt $\operatorname{si}\bigl(\frac{\pi t}{T}\bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf)$. Das Dreieck ist die Faltung zweier Rechtecke, $\Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)$; nach dem Faltungssatz ist sein Spektrum $\operatorname{si}^2(\pi f)$. Schließlich gilt $\operatorname{si}(\pi t)*\operatorname{si}(\pi t)=\operatorname{si}(\pi t)$, weil im Frequenzbereich $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$ ist. Ein __idealer Tiefpass__ lässt alle Frequenzen eines Bandes unverändert durch und sperrt alle anderen; er ändert ein Signal nicht, das schon auf sein Band begrenzt ist.

Der Grund für die Form des Spektrums: Bei $f=0$ ist es die Fläche $|T|$ des Rechtecks. Bei den Frequenzen $k/T$ mit ganzzahligem $k\neq0$ passen genau $k$ Perioden der Schwingung in das Rechteck. Sie mitteln sich zu null, daher die Nullstellen. Doppelte Dauer heißt doppelte Höhe und halbe Breite des Spektrums.

Falle: $\operatorname{si}(x)$ ist null, wo $\sin(x)$ null ist, also bei den von null verschiedenen ganzzahligen Vielfachen von $\pi$. Im Argument $\pi Tf$ steckt das $\pi$ schon. Die Nullstellen von $\operatorname{si}(\pi Tf)$ liegen deshalb bei $k/T$.
::::

::::formelsammlung
**si-Funktion**

$$\operatorname{si}(x)=\sin(x)/x$$

An der Stelle null durch den Grenzwert 1 ergänzt.

**Rechteck**

$$\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$$

Direkt aus $\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t=\operatorname{si}(\pi f)$.

**Rechteck der Dauer $|T|$**

$$\operatorname{rect}\Bigl(\frac tT\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf)$$

$T$ ungleich null. Höhe $|T|$ bei $f=0$ (Fläche des Rechtecks), Nullstellen bei allen von null verschiedenen Vielfachen von $1/T$. Doppelte Dauer: doppelte Höhe, halbe Breite.

**si-Funktion als Zeitsignal**

$$\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf)$$

Folgt aus der Symmetrie.

**Dreieck**

$$\Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f)$$

Folgt aus dem Faltungssatz.

**Faltung der si-Funktion mit sich selbst**

$$\operatorname{si}(\pi t)*\operatorname{si}(\pi t)=\operatorname{si}(\pi t)$$

Weil $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$: Ein idealer Tiefpass ändert ein Signal nicht, das schon auf sein Band begrenzt ist.

**Fläche und Energie der si-Funktion**

$$\int_{-\infty}^{\infty}\operatorname{si}(\pi t)\,\mathrm{d} t=1,\qquad\int_{-\infty}^{\infty}\operatorname{si}^2(\pi t)\,\mathrm{d} t=1$$

Mit dem Flächensatz, $\operatorname{rect}(0)=1$, und mit Parseval, $\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
::::
