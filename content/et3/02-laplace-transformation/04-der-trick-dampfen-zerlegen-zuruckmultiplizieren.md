---
title: Der Trick: dämpfen, zerlegen, zurückmultiplizieren
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220400
summary: Jedes Signal als Überlagerung von $\ee^{pt}$, und warum ein LTI-System daraus eine Multiplikation macht
tags: Dichte
lang: de
---

<span class="anker" id="stufe-2-2"></span>

**Die Idee.** Man macht das Signal erst zerlegbar und nimmt die Änderung danach wieder zurück:

<ol>

<li>

⁠**Dämpfen.** Man multipliziert mit $\mathrm{e}^{-\sigma t}$. Wächst ein rechtsseitiges Signal höchstens wie $\mathrm{e}^{\alpha t}$, klingt $s(t)\,\mathrm{e}^{-\sigma t}$ für jedes $\sigma>\alpha$ ab und ist absolut integrierbar.

</li>

<li>

⁠**Zerlegen.** Das gedämpfte Signal ist eine Überlagerung reiner Schwingungen. Sein Fourier-Spektrum ist genau die Laplace-Transformierte $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ auf der Linie $\operatorname{Re} p=\sigma$ (Aufgabe [2](konvergenzbereich-welche-dampfungen-funktionieren.html#aufg-2)):

$$\mathcal{F}\bigl\{s(t)\,\mathrm{e}^{-\sigma t}\bigr\}(f)=S(\sigma+\mathrm{j}2\pi f).$$

</li>

<li>

⁠**Zurückmultiplizieren.** Man multipliziert die Zerlegung mit $\mathrm{e}^{\sigma t}$. Der Faktor hängt nicht von $f$ ab und darf ins Integral. Dort macht er aus jeder Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ den Baustein $\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}=\mathrm{e}^{pt}$.

</li>

</ol>

Das Ergebnis ist die vermutete Überlagerung.

:::satz Satz 2.1 (Umkehrformel der Laplace-Transformation)
<span class="anker" id="satz-2-1"></span>

Liegt $\sigma$ im Konvergenzbereich von $S(p)$, dann gilt

<span class="anker" id="gl-2-1"></span>
$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p =\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f. \tag{2.1}$$
:::

⁠**So liest man das:**

<ul>

<li>

Der Integrationsweg ist die senkrechte Linie $\operatorname{Re} p=\sigma$ in der $p$-Ebene, von unten nach oben durchlaufen ($f$ von $-\infty$ bis $+\infty$, Abb. [2](#abb-2)).

</li>

<li>

$\mathrm{e}^{pt}$ ist der Baustein, $S(p)\,\mathrm{d} p/(2\pi\mathrm{j})=S(\sigma+\mathrm{j}2\pi f)\,\mathrm{d} f$ sein komplexes Gewicht. $S(p)$ selbst ist eine __Dichte__: Gewicht pro Frequenzintervall. Ist $s$ eine Spannung in V, hat $S$ die Einheit V s.

</li>

<li>

Das Integral ist als Grenzwert $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$ gemeint. Es liefert $s(t)$ an jeder Stelle, an der $s$ stetig ist, und an einer Sprungstelle den Mittelwert aus links- und rechtsseitigem Grenzwert.

</li>

</ul>

⁠**Grenzfall $\sigma=0$:** Liegt die imaginäre Achse im Konvergenzbereich, darf man $\sigma=0$ wählen. Dann ist $p=\mathrm{j}2\pi f$, und [(2.1)](#gl-2-1) wird die Fourier-Umkehrformel. Die Laplace-Transformation enthält die Fourier-Transformation als Spezialfall.

:::herleitung Umkehrformel aus der Fourier-Umkehrformel
Nach Schritt 2 ist $S(\sigma+\mathrm{j}2\pi f)$ das Fourier-Spektrum von $s(t)\mathrm{e}^{-\sigma t}$. Die Fourier-Umkehrformel liefert

$$s(t)\,\mathrm{e}^{-\sigma t}=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f.$$

Multiplikation mit $\mathrm{e}^{\sigma t}$, das nicht von $f$ abhängt:

$$s(t)=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f.$$

Substitution $p=\sigma+\mathrm{j}2\pi f$ bei festem $\sigma$: $\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$, also $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$. Die Grenzen $f=\mp\infty$ werden zu $p=\sigma\mp\mathrm{j}\infty$:

$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p.$$
:::

**Beispiel: der Sprung aus Bausteinen.** Für $\varepsilon(t)$ ist $S(p)=1/p$ mit $\operatorname{Re} p>0$. Gewählt wird $\sigma=0{,}5/\mathrm s$ (Abb. [2](#abb-2)). Abbildung [3](#abb-3) zeigt, was herauskommt, wenn man nur die Bausteine mit $|f|\le F$ überlagert. Schon bei $F=0{,}25$ Hz ist die Form des Sprungs erkennbar. Mit wachsendem $F$ wird die Kante steiler, bei $t=0$ strebt die Kurve gegen den Mittelwert $\tfrac12$ (0,40; 0,47; 0,49), bei $t=-1$ s gegen null (0,053; 0,029; 0,008).

:::abbildung et3/k2linie 2
$p$-Ebene für den Sprung $\varepsilon(t)$, $S(p)=1/p$. Der Konvergenzbereich (blau hinterlegt) liegt rechts vom Pol $p=0$. Jede senkrechte Linie darin taugt als Integrationsweg; hier $\sigma=0{,}5/\mathrm s$. Jeder Punkt der Linie ist ein Baustein $\mathrm{e}^{pt}$ mit dem Gewicht $S(p)$.
:::

:::abbildung et3/k2sprung 3
Der Sprung, überlagert aus den Bausteinen $\mathrm{e}^{pt}$ auf der Linie $\operatorname{Re} p=0{,}5/\mathrm s$, wobei nur die Bausteine mit $|f|\le F$ mitgenommen werden: $s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$ mit $S(p)=1/p$. Je mehr Bausteine, desto genauer der Sprung; bei $t=0$ strebt die Kurve gegen $\tfrac12$.
:::

:::frage Alle Bausteine sind komplex. Warum kommt eine reelle Kurve heraus?
Die Bausteine treten paarweise auf: zu $f$ gehört $-f$, also zu $p$ der konjugierte Punkt $p^*$. Für ein reelles Signal ist das Gewicht dort konjugiert, $S(p^*)=S(p)^*$ (die Rechnung $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ mit reellem $s$ zeigt es). Jedes Paar ergibt $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$, also eine reelle, gedämpfte oder wachsende Schwingung. Die Imaginärteile heben sich paarweise auf.
:::

:::frage Ist es nun eine Summe oder ein Integral?
Im Allgemeinen ein Integral: Auf der Linie liegen kontinuierlich viele Bausteine, jeder mit einem infinitesimalen Gewicht $S\,\mathrm{d} f$. Eine echte Summe mit endlich vielen Gliedern entsteht in einem wichtigen Fall: wenn $S(p)$ ein Polynombruch ist. Dann ist das Signal eine Summe von Bausteinen an den Polen (Stufe [4](aus-dem-integral-wird-eine-summe.html#stufe-4)). Eine Summe mit unendlich vielen Gliedern ist die Fourier-Reihe eines periodischen Signals.
:::
