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

::::lernkarten
:::karte begriff si-Funktion
Wie ist die si-Funktion definiert, welchen Wert hat sie an der Stelle null, und wo tritt sie auf?
---
$\operatorname{si}(x)=\sin(x)/x$; an der Stelle null, wo der Bruch nicht erklärt ist, wird sie durch den Grenzwert $\operatorname{si}(0)=1$ ergänzt. Sie ist das Spektrum des Rechteckimpulses: $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$.
--- falsch
$\operatorname{si}(x)=\sin(x)/x$; an der Stelle null ist der Bruch $0/0$, deshalb setzt man $\operatorname{si}(0)=0$, damit sie wie der Sinus durch den Ursprung geht. Sie ist das Spektrum des Dreiecks.
--- falsch
$\operatorname{si}(x)=\sin(x)\cdot x$; an der Stelle null ist sie null, weil beide Faktoren dort verschwinden, und für große $x$ wächst sie wie $x$ an. Sie ist das Spektrum des Rechteckimpulses.
--- falsch
$\operatorname{si}(x)=\sin(\pi x)/x$; an der Stelle null wird sie durch den Grenzwert $\operatorname{si}(0)=\pi$ ergänzt, weil der Sinus für kleine Argumente fast linear ist. Sie ist das Spektrum des Dirac-Impulses.
:::
:::karte herleitung Spektrum des Rechteckimpulses
Wie berechnet man das Spektrum des Rechteckimpulses $\operatorname{rect}(t)$ direkt aus der Definition und daraus das Spektrum eines Rechtecks der Dauer $|T|$?
---
Man integriert nur von $-\frac12$ bis $\frac12$, weil $\operatorname{rect}(t)$ dort 1 und sonst 0 ist: $\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.
---
Die Stammfunktion ist $\mathrm{e}^{-\mathrm{j}2\pi ft}$ geteilt durch $-\mathrm{j}2\pi f$, weil die Ableitung des Exponenten diesen Faktor liefert. Eingesetzt ergibt das $\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}$.
---
Das ist $\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f)$, weil die Differenz der beiden Exponentialfunktionen nach der Euler-Formel das $2\mathrm{j}$-Fache des Sinus ist.
---
Für ein Rechteck der Dauer $|T|$ folgt mit der Ähnlichkeit $\operatorname{rect}\Bigl(\frac tT\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf)$, weil das Dehnen der Zeit das Spektrum staucht und mit $|T|$ multipliziert.
:::
:::karte formel Rechteckimpuls beliebiger Dauer
Welches Spektrum hat der Rechteckimpuls $\operatorname{rect}\bigl(\frac tT\bigr)$ der Dauer $|T|$, und wo liegen seine Nullstellen?
---
$\operatorname{rect}\Bigl(\frac tT\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf)$. Bei $f=0$ hat das Spektrum die Höhe $|T|$, die Fläche des Rechtecks. Nullstellen liegen bei allen von null verschiedenen Vielfachen von $1/T$.
--- falsch
$\operatorname{rect}\Bigl(\frac tT\Bigr)\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\operatorname{si}\Bigl(\frac{\pi f}{T}\Bigr)$. Bei $f=0$ hat das Spektrum die Höhe $1/|T|$. Nullstellen liegen bei allen von null verschiedenen Vielfachen von $T$.
--- falsch
$\operatorname{rect}\Bigl(\frac tT\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf)$. Bei $f=0$ hat das Spektrum die Höhe $|T|$. Nullstellen liegen bei allen ungeraden Vielfachen von $1/(2T)$, dazwischen die Maxima.
--- falsch
$\operatorname{rect}\Bigl(\frac tT\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf)$. Bei $f=0$ hat das Spektrum eine Nullstelle, weil das Rechteck keinen Wechselanteil hat. Weitere Nullstellen liegen bei allen Vielfachen von $1/T$.
:::
:::karte zusammenhang Nullstellen des Rechteckspektrums
Warum hat das Spektrum eines Rechteckimpulses der Dauer $T$ bei den Frequenzen $k/T$ mit ganzzahligem $k\neq0$ Nullstellen?
---
Bei diesen Frequenzen passen genau $k$ Perioden der Schwingung in das Rechteck. Das Fourier-Integral mittelt die Schwingung dann über volle Umdrehungen ihres Zeigers, und das ergibt null. Bei $f=0$ bleibt die Fläche $|T|$.
--- falsch
Weil das Rechteck an seinen Kanten springt und jeder Sprung die Frequenzen $k/T$ auslöscht. Ein Signal ohne Sprünge hätte an diesen Stellen keine Nullstellen, sondern im Gegenteil seine größten Werte.
--- falsch
Bei diesen Frequenzen passt genau eine halbe Periode der Schwingung in das Rechteck. Die positive Halbwelle wird dann vom Rechteck ausgeschnitten, die negative fehlt, und beide Anteile heben sich gegenseitig auf.
--- falsch
Weil die Schwingungen mit den Frequenzen $k/T$ das Rechteck periodisch fortsetzen würden. Ein einzelnes Rechteck ist nicht periodisch und darf diese Frequenzen deshalb überhaupt nicht enthalten.
:::
:::karte zusammenhang Doppelte Dauer, halbe Breite
Was passiert mit dem Spektrum eines Rechteckimpulses, wenn man seine Dauer von 1 s auf 2 s verdoppelt?
---
Das Spektrum wird doppelt so hoch und halb so breit: Die Höhe bei $f=0$ ist die Fläche, also 2 statt 1, und die erste Nullstelle rückt von 1 Hz nach 0,5 Hz. Dauer und Bandbreite verhalten sich umgekehrt.
--- falsch
Das Spektrum wird doppelt so breit und halb so hoch: Ein längerer Impuls enthält mehr Schwingungen, deshalb rückt die erste Nullstelle von 1 Hz nach 2 Hz, und die Höhe bei $f=0$ sinkt auf 0,5.
--- falsch
Das Spektrum bleibt gleich breit und wird doppelt so hoch: Die Nullstellen hängen nur von der Form des Impulses ab, nicht von seiner Dauer, und die Höhe bei $f=0$ ist die Fläche, also 2 statt 1.
--- falsch
Das Spektrum wird halb so breit, behält aber die Höhe 1: Die erste Nullstelle rückt von 1 Hz nach 0,5 Hz, und die Höhe bei $f=0$ ist der Wert des Impulses, der ja unverändert 1 bleibt.
:::
:::karte formel si-Funktion als Zeitsignal
Welches Spektrum hat das Zeitsignal $\operatorname{si}\bigl(\frac{\pi t}{T}\bigr)$, und welcher Satz liefert es?
---
$\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf)$: ein Rechteck im Frequenzbereich. Es folgt aus dem Paar für das Rechteck mit der Symmetrie, die Zeit und Frequenz vertauscht.
--- falsch
$\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf)$: wieder eine si-Funktion. Es folgt aus dem Paar für das Rechteck mit der Ähnlichkeit, weil die si-Funktion ihre eigene Transformierte ist.
--- falsch
$\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\Lambda(Tf)$: ein Dreieck im Frequenzbereich. Es folgt aus dem Faltungssatz, weil die si-Funktion aus zwei gefalteten Rechtecken entsteht.
--- falsch
$\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf)\,\mathrm{e}^{-\mathrm{j}\pi f}$: ein Rechteck mit linearer Phase. Es folgt aus der Verschiebung, weil die si-Funktion gegenüber dem Rechteck verschoben ist.
:::
:::karte formel Dreieck
Wie entsteht das Dreieck $\Lambda(t)$ aus Rechtecken, und welches Spektrum hat es deshalb?
---
Als Faltung zweier Rechtecke: $\Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f)$. Nach dem Faltungssatz wird die Faltung zum Produkt der beiden si-Spektren.
--- falsch
Als Produkt zweier Rechtecke: $\Lambda(t)=\operatorname{rect}(t)\cdot\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)*\operatorname{si}(\pi f)$. Das Produkt wird zur Faltung der beiden si-Spektren.
--- falsch
Als Faltung zweier Rechtecke: $\Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;2\operatorname{si}(\pi f)$. Nach dem Faltungssatz addieren sich die beiden si-Spektren, weil die Faltung linear ist.
--- falsch
Als Faltung zweier Rechtecke: $\Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(2\pi f)$. Das Dreieck ist doppelt so breit wie das Rechteck, sein Spektrum deshalb halb so breit.
:::
:::karte begriff idealer Tiefpass
Was ist ein idealer Tiefpass, und was macht er mit einem Signal, das schon auf sein Band begrenzt ist?
---
Ein System, das alle Frequenzen eines Bandes unverändert durchlässt und alle anderen sperrt; sein Frequenzgang ist ein Rechteck wie $\operatorname{rect}(f)$. Ein Signal, das schon auf dieses Band begrenzt ist, ändert er nicht.
--- falsch
Ein System, das alle Frequenzen unterhalb einer Grenze gleich stark abschwächt und alle darüber unverändert lässt. Ein Signal, das schon auf sein Band begrenzt ist, schwächt er deshalb gleichmäßig ab.
--- falsch
Ein System, dessen Frequenzgang wie beim RC-Glied mit $1/f$ abfällt, aber ohne Phasenverschiebung. Ein Signal, das schon auf sein Band begrenzt ist, glättet er trotzdem, weil auch tiefe Frequenzen etwas geschwächt werden.
--- falsch
Ein System, das alle Frequenzen eines Bandes unverändert durchlässt und alle anderen sperrt; seine Impulsantwort ist ein Rechteck wie $\operatorname{rect}(t)$. Ein Signal, das schon auf dieses Band begrenzt ist, ändert er nicht.
:::
:::karte formel Faltung der si-Funktion mit sich selbst
Warum ergibt die Faltung der si-Funktion mit sich selbst, $\operatorname{si}(\pi t)*\operatorname{si}(\pi t)$, wieder dieselbe Funktion?
---
$\operatorname{si}(\pi t)*\operatorname{si}(\pi t)=\operatorname{si}(\pi t)$, weil im Frequenzbereich $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$ ist: Ein idealer Tiefpass ändert ein Signal nicht, das schon auf sein Band begrenzt ist.
--- falsch
$\operatorname{si}(\pi t)*\operatorname{si}(\pi t)=\operatorname{si}^2(\pi t)$, weil die Faltung zweier gleicher Funktionen ihr Quadrat ist. Im Frequenzbereich entspricht das der Faltung zweier Rechtecke, also einem Dreieck.
--- falsch
$\operatorname{si}(\pi t)*\operatorname{si}(\pi t)=\operatorname{si}(\pi t)$, weil die si-Funktion bei $t=0$ den Wert 1 hat. Die Faltung mit einer Funktion, deren Maximum 1 ist, lässt jedes Signal unverändert, wie beim Dirac-Impuls.
--- falsch
$\operatorname{si}(\pi t)*\operatorname{si}(\pi t)=\Lambda(t)$, weil im Frequenzbereich $\operatorname{rect}(f)\cdot\operatorname{rect}(f)$ zum Dreieck wird. Zweimal durch einen idealen Tiefpass geschickt, wird jedes Signal zum Dreieck.
:::
:::karte formel Fläche und Energie der si-Funktion
Wie erhält man ohne Integration die Fläche $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ und die Energie $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$ der si-Funktion?
---
Beide sind 1. Der Flächensatz liefert $\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$, Parseval liefert $\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
--- falsch
Die Fläche ist 1, die Energie $\frac12$. Der Flächensatz liefert den Wert $\operatorname{rect}(0)=1$, und Parseval halbiert ihn, weil sich die Energie auf positive und negative Frequenzen gleich verteilt.
--- falsch
Beide sind unendlich, weil die si-Funktion nur wie $1/t$ abfällt und solche Integrale nicht konvergieren. Flächensatz und Parseval gelten nur für Signale, die deutlich schneller abfallen.
--- falsch
Die Fläche ist $\pi$, die Energie $\pi^2$. Der Flächensatz liefert $S(0)=\pi$, weil im Argument $\pi t$ steht, und Parseval quadriert diesen Wert, weil die Energie quadratisch vom Signal abhängt.
:::
:::karte zusammenhang Glattheit und Abfall des Spektrums
Warum fallen die Nebenzipfel des Spektrums umso schneller ab, je öfter man Rechtecke miteinander faltet?
---
Jede Faltung multipliziert das Spektrum mit $\operatorname{si}(\pi f)$, das in den Nebenzipfeln wie $1/(\pi f)$ abfällt: Bei $M$ Rechtecken fallen sie wie $1/f^M$. Im Zeitbereich wird das Signal dabei glatter; je glatter ein Signal, desto schneller fällt sein Spektrum ab.
--- falsch
Jede Faltung addiert zum Spektrum ein weiteres $\operatorname{si}(\pi f)$, und die Summe vieler gleicher Funktionen mittelt die Nebenzipfel weg. Im Zeitbereich wird das Signal dabei breiter, und breite Signale haben stets schmale Spektren.
--- falsch
Jede Faltung macht das Signal kürzer, und ein kürzeres Signal hat nach der Ähnlichkeit weniger Nebenzipfel. Bei $M$ Rechtecken fallen sie deshalb wie $1/M$ ab, und zwar unabhängig von der Frequenz, an der man sie betrachtet.
--- falsch
Jede Faltung multipliziert das Spektrum mit $\operatorname{si}(\pi f)$, das überall kleiner als 1 ist. Die Nebenzipfel werden deshalb mit jeder Faltung um denselben festen Faktor kleiner, die Form des Abfalls bleibt aber $1/f$.
:::
::::
