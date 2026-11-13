---
title: Tabellen und Umkehrformel
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Laplace-Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Kapitel 2: Laplace-Transformation
order: 3220800
summary: Hier stehen die Rechenregeln und Transformationspaare auf einen Blick, ergänzt um einige weitere Regeln.
tags: Fourier-Darstellung, Spektrum
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Hier stehen die Rechenregeln und Transformationspaare auf einen Blick, ergänzt um einige weitere Regeln. Dazu kommt die Formel, die aus $S(p)$ das Signal zurückgewinnt.
:::

### Rechenregeln

<span class="anker" id="stufe-7-1"></span>

Tabelle [1](#tab-1) sammelt die Rechenregeln. Superposition, Faltung, Ableitung und Integration sind aus den vorigen Abschnitten bekannt. Die übrigen fünf folgen jeweils mit einer Substitution aus der Definition [(1.9)](eigenfunktionen-von-lti-systemen.html#gl-1-9); die Herleitungen stehen im Kasten darunter.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Rechenregeln der Laplace-Transformation. KB: Konvergenzbereich von $S(p)$.

| Regel | $s(t)$ | $S(p)$ |
|---|---|---|
| Superposition | $\sum_ia_i\,s_i(t)$ | $\sum_ia_i\,S_i(p)$ |
| Verschiebung in $t^{\mathrm a}$ | $s(t-t_0)$ | $S(p)\,\mathrm{e}^{-pt_0}$ |
| Verschiebung in $p$ | $s(t)\cdot\mathrm{e}^{p_0t}$ | $S(p-p_0)$, KB um $\operatorname{Re} p_0$ verschoben |
| Konjugation | $s^*(t)$ | $S^*(p^*)$ |
| Zeitspiegelung$^{\mathrm b}$ | $s(-t)$ | $S(-p)$, KB gespiegelt |
| Zeitdehnung$^{\mathrm c}$ | $s\bigl(\frac tT\bigr)$ | $\vert T\vert \,S(pT)$ |
| Faltung | $g(t)=s(t)*h(t)$ | $G(p)=S(p)\cdot H(p)$ |
| Ableitung | $\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)$ | $p^n\cdot S(p)$ |
| Integration | $\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$ | $\frac1p\,S(p)$, zusätzlich $\operatorname{Re} p>0$ |

$^{\mathrm a}$ Bei einseitiger Transformation nur für $t_0>0$ oder wenn $s(t)=0$ für $t<t_0$. $^{\mathrm b}$ Bei einseitiger Transformation nicht anwendbar. $^{\mathrm c}$ $T\ne0$; bei einseitiger Transformation nur für $T>0$.

:::herleitung Die fünf weiteren Regeln
⁠**Verschiebung in $t$:** Mit $u=t-t_0$ ist $\int s(t-t_0)\,\mathrm{e}^{-pt}\mathrm{d} t=\int s(u)\,\mathrm{e}^{-p(u+t_0)}\mathrm{d} u=\mathrm{e}^{-pt_0}S(p)$. Der Konvergenzbereich bleibt gleich.

⁠**Verschiebung in $p$:** $\int s(t)\,\mathrm{e}^{p_0t}\,\mathrm{e}^{-pt}\mathrm{d} t=\int s(t)\,\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=S(p-p_0)$. Das Integral konvergiert, wenn $p-p_0$ im Konvergenzbereich von $S$ liegt.

⁠**Konjugation:** $\int s^*(t)\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl(\int s(t)\,\mathrm{e}^{-p^*t}\mathrm{d} t\Bigr)^*=S^*(p^*)$, denn $(\mathrm{e}^{-p^*t})^*=\mathrm{e}^{-pt}$.

⁠**Zeitspiegelung:** Mit $u=-t$ ist $\int s(-t)\,\mathrm{e}^{-pt}\mathrm{d} t=\int s(u)\,\mathrm{e}^{-(-p)u}\mathrm{d} u=S(-p)$. Das Integral konvergiert, wenn $-p$ im Konvergenzbereich von $S$ liegt.

⁠**Zeitdehnung:** Mit $u=t/T$ und $\mathrm{d} t=T\,\mathrm{d} u$ ist für $T>0$: $\int s(t/T)\,\mathrm{e}^{-pt}\mathrm{d} t=T\int s(u)\,\mathrm{e}^{-(pT)u}\mathrm{d} u=T\,S(pT)$. Für $T<0$ vertauschen sich die Grenzen, das gibt ein zusätzliches Minus, zusammen $|T|\,S(pT)$.
:::

:::hintergrund Was die Regeln mit den Polen machen
Die Pole sind die Exponenten der Anteile eines Signals. Damit lassen sich die Regeln anschaulich lesen:

<ul>

<li>

⁠**Verschiebung in $t$:** Der Faktor $\mathrm{e}^{-pt_0}$ hat weder Pole noch Nullstellen. Ein verzögertes Signal besteht aus denselben Exponentialfunktionen, es findet nur später statt. Auf der imaginären Achse ist $|\mathrm{e}^{-\mathrm{j}2\pi Ft_0}|=1$: Eine Verzögerung ändert nur die Phase, nie den Betrag.

</li>

<li>

⁠**Verschiebung in $p$:** Multipliziert man das Signal mit $\mathrm{e}^{p_0t}$, so wird aus jedem Anteil $\mathrm{e}^{p_rt}$ der Anteil $\mathrm{e}^{(p_r+p_0)t}$. Alle Pole wandern um $p_0$. Ein zusätzlich gedämpftes Signal ($p_0$ reell und negativ) hat seine Pole weiter links. Multipliziert man mit $\mathrm{e}^{\mathrm{j}2\pi F_0t}$, wandern alle Pole um $2\pi F_0$ nach oben; alle Frequenzen des Signals sind um $F_0$ erhöht.

</li>

<li>

⁠**Zeitspiegelung:** Aus einem rechtsseitigen Anteil wird ein linksseitiger, die Pole und der Konvergenzbereich werden an der imaginären Achse gespiegelt.

</li>

<li>

⁠**Zeitdehnung:** Ein Pol $p_r$ von $S$ wird zu $p_r/T$. Läuft das Signal schneller ab ($|T|<1$), rücken die Pole vom Ursprung weg: Es klingt schneller ab und schwingt schneller.

</li>

</ul>
:::

### Transformationspaare

<span class="anker" id="stufe-7-2"></span>

Tabelle [2](#tab-2) sammelt die Paare dieses Kapitels. Neu ist nur der verschobene Dirac-Impuls; er folgt aus $\mathcal{L}\{\delta\}=1$ und der Verschiebung in $t$.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Elementare Laplace-Transformationspaare. $p_0$ komplex, $\gamma$ und $\omega_1$ reell.

| $s(t)$ | $S(p)$ | Konvergenzbereich |
|---|---|---|
| $\delta(t)$ | $1$ | alle $p$ |
| $\delta(t-t_0)$ | $\mathrm{e}^{-pt_0}$ | alle $p$ |
| $\varepsilon(t)$ | $\frac1p$ | $\operatorname{Re} p>0$ |
| $-\varepsilon(-t)$ | $\frac1p$ | $\operatorname{Re} p<0$ |
| $\frac{t^{n-1}}{(n-1)!}\,\varepsilon(t)=\underbrace{\varepsilon(t)*\ldots*\varepsilon(t)}_{n\text{ Funktionen}}$ | $\frac{1}{p^n}$ | $\operatorname{Re} p>0$ |
| $\mathrm{e}^{p_0t}\,\varepsilon(t)$ | $\frac{1}{p-p_0}$ | $\operatorname{Re} p>\operatorname{Re} p_0$ |
| $-\mathrm{e}^{p_0t}\,\varepsilon(-t)$ | $\frac{1}{p-p_0}$ | $\operatorname{Re} p<\operatorname{Re} p_0$ |
| $\frac{t^{\,j-1}}{(j-1)!}\,\mathrm{e}^{p_0t}\,\varepsilon(t)$ | $\frac{1}{(p-p_0)^j}$ | $\operatorname{Re} p>\operatorname{Re} p_0$ |
| $\mathrm{e}^{-\gamma t}\cos(\omega_1t)\cdot\varepsilon(t)$ | $\frac{p+\gamma}{(p+\gamma)^2+\omega_1^2}$ | $\operatorname{Re} p>-\gamma$ |
| $\mathrm{e}^{-\gamma t}\sin(\omega_1t)\cdot\varepsilon(t)$ | $\frac{\omega_1}{(p+\gamma)^2+\omega_1^2}$ | $\operatorname{Re} p>-\gamma$ |

### Die Umkehrformel

<span class="anker" id="stufe-7-3"></span>

Bisher hat das Kapitel Signale nur mit Partialbrüchen und der Tabelle zurückgewonnen. Für jede Laplace-Transformierte gibt es aber auch eine allgemeine Formel.

:::satz Satz 7.1 (Umkehrformel der Laplace-Transformation)
<span class="anker" id="satz-7-1"></span>

Liegt $\sigma_0$ im Konvergenzbereich von $S(p)$, dann gilt

<span class="anker" id="gl-7-1"></span>
$$s(t)=\mathcal{L}^{-1}\{S(p)\}=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p . \tag{7.1}$$

Dabei darf $\sigma_0$ im Konvergenzbereich beliebig gewählt werden.
:::

⁠**So liest man das:**

<ul>

<li>

Der Integrationsweg ist die senkrechte Gerade $\operatorname{Re} p=\sigma_0$ in der $p$-Ebene, von unten nach oben durchlaufen. Sie muss im Konvergenzbereich liegen.

</li>

<li>

Auf dem Weg ist $p=\sigma_0+\mathrm{j}2\pi f$ und $\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$. Damit wird die Formel zu $s(t)=\int_{-\infty}^{\infty}S(\sigma_0+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma_0+\mathrm{j}2\pi f)t}\,\mathrm{d} f$.

</li>

<li>

Das ist eine Überlagerung von Exponentialfunktionen $\mathrm{e}^{pt}$, eine für jeden Punkt der Geraden, jede mit dem komplexen Gewicht $S(p)\,\mathrm{d} f$. $S(p)$ gibt also an, wie stark die Funktion $\mathrm{e}^{pt}$ im Signal $s(t)$ vertreten ist. Es ist eine Dichte: Gewicht pro Frequenzintervall. Ist $s$ eine Spannung in V, hat $S$ die Einheit V s.

</li>

<li>

Das Integral ist als Grenzwert $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$ gemeint. Es liefert $s(t)$ an jeder Stelle, an der $s$ stetig ist, und an einer Sprungstelle den Mittelwert aus links- und rechtsseitigem Grenzwert.

</li>

</ul>

Zum Rechnen braucht man die Formel selten: Bei rationalem $S(p)$ führen Partialbrüche und Tabelle schneller zum Ziel. Ihr Wert liegt im Verständnis: Sie sagt, *was* $S(p)$ ist.

⁠**Kurz gesagt:** Die Umkehrformel setzt das Signal aus den Funktionen $\mathrm{e}^{pt}$ auf einer senkrechten Geraden im Konvergenzbereich zusammen, jede mit dem Gewicht $S(p)$.

:::hintergrund Analyse und Synthese: wie sich der Kreis schließt
Im ersten Abschnitt hieß es im Kasten „Suchfilter“: Die Transformation sucht das Signal nach Exponentialfunktionen ab. Die Umkehrformel ist das Gegenstück. Die Transformation *analysiert*: Sie bestimmt, mit welchem Gewicht $S(p)$ jede Funktion $\mathrm{e}^{pt}$ im Signal steckt. Die Umkehrformel *synthetisiert*: Sie setzt das Signal aus diesen Funktionen und Gewichten wieder zusammen. Damit ist auch die Aussage aus dem Kasten „Koordinatensystem“ exakt: Jedes Signal mit nicht leerem Konvergenzbereich ist eine Überlagerung von Funktionen $\mathrm{e}^{pt}$, und $S(p)$ sind seine Koordinaten.

Es gibt zwei Arten, ein Signal so zu zerlegen, und beide sind richtig:

<ul>

<li>

⁠**Als Integral über eine Gerade:** Die Umkehrformel benutzt kontinuierlich viele Funktionen $\mathrm{e}^{pt}$, die für alle Zeiten $t$ von $-\infty$ bis $\infty$ laufen. Erst ihre Überlagerung ergibt zum Beispiel, dass der Sprung für $t<0$ null ist.

</li>

<li>

⁠**Als endliche Summe über die Pole:** Ist $S(p)$ ein Polynombruch, so ist das Signal auf jeder Hälfte der Zeitachse eine endliche Summe $\sum_rA_r\,\mathrm{e}^{p_rt}$, mit den Polen als Exponenten. Die Partialbruchzerlegung findet genau diese Summe. Dass die Umkehrformel dasselbe ergibt, begründet der Residuensatz der Funktionentheorie.

</li>

</ul>
:::

:::hintergrund Woher die Umkehrformel kommt
Die Herleitung braucht die __Fourier-Darstellung__. Ein Signal, das *absolut integrierbar* ist ($\int|s(t)|\,\mathrm{d} t<\infty$), lässt sich aus reinen Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$ zusammensetzen. Hier genügt ihre Formel; die Funktion $\mathcal{F}\{s\}(f)$ heißt __Spektrum__ und gibt das Gewicht der Schwingung mit der Frequenz $f$ an:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

Viele Signale der Systemtheorie sind nicht absolut integrierbar: Der Sprung $\varepsilon(t)$ klingt nicht ab, $\mathrm{e}^{2t}\varepsilon(t)$ wächst sogar. Der Ausweg geht in drei Schritten:

<ol>

<li>

⁠**Dämpfen.** Man multipliziert mit $\mathrm{e}^{-\sigma_0t}$. Liegt $\sigma_0$ im Konvergenzbereich, ist $s(t)\,\mathrm{e}^{-\sigma_0t}$ absolut integrierbar.

</li>

<li>

⁠**Zerlegen.** Das Spektrum des gedämpften Signals ist die Laplace-Transformierte auf der Geraden $\operatorname{Re} p=\sigma_0$ (Aufgabe [10](#aufg-10)):

$$\mathcal{F}\bigl\{s(t)\,\mathrm{e}^{-\sigma_0t}\bigr\}(f)=\int s(t)\,\mathrm{e}^{-(\sigma_0+\mathrm{j}2\pi f)t}\,\mathrm{d} t=S(\sigma_0+\mathrm{j}2\pi f).$$

Die Fourier-Darstellung gibt also $s(t)\,\mathrm{e}^{-\sigma_0t}=\int S(\sigma_0+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$.

</li>

<li>

⁠**Zurückmultiplizieren.** Man multipliziert mit $\mathrm{e}^{\sigma_0t}$. Der Faktor hängt nicht von $f$ ab und darf ins Integral:

$$s(t)=\int_{-\infty}^{\infty}S(\sigma_0+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma_0+\mathrm{j}2\pi f)t}\,\mathrm{d} f.$$

</li>

</ol>

Mit $p=\sigma_0+\mathrm{j}2\pi f$, also $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$, und den Grenzen $f=\mp\infty\ \to\ p=\sigma_0\mp\mathrm{j}\infty$ ist das die Umkehrformel [(7.1)](#gl-7-1).

⁠**Grenzfall $\sigma_0=0$:** Liegt die imaginäre Achse im Konvergenzbereich, darf man $\sigma_0=0$ wählen. Dann ist $S(\mathrm{j}2\pi f)=\mathcal{F}\{s\}(f)$, und [(7.1)](#gl-7-1) wird die Fourier-Darstellung. Die Laplace-Transformation enthält die Fourier-Transformation als Spezialfall.
:::

:::hintergrund Ein Sprung, aus Exponentialfunktionen zusammengesetzt
Für $\varepsilon(t)$ ist $S(p)=1/p$ mit $\operatorname{Re} p>0$. Gewählt wird $\sigma_0=0{,}5/\mathrm s$ (Abb. [13](#abb-13)). Abbildung [14](#abb-14) zeigt, was herauskommt, wenn man nur die Funktionen $\mathrm{e}^{pt}$ mit $|f|\le F$ überlagert. Schon bei $F=0{,}25$ Hz ist die Form des Sprungs erkennbar. Mit wachsendem $F$ wird die Kante steiler. Bei $t=0$ strebt die Kurve gegen den Mittelwert $\tfrac12$ (0,40; 0,47; 0,49), bei $t=-1$ s gegen null (0,053; 0,029; 0,008).

:::abbildung et3/k2linie 13
$p$-Ebene für den Sprung $\varepsilon(t)$, $S(p)=1/p$. Der Konvergenzbereich (blau) liegt rechts vom Pol $p=0$. Jede senkrechte Gerade darin taugt als Integrationsweg; hier $\sigma_0=0{,}5/\mathrm s$. Jeder Punkt der Geraden ist eine Funktion $\mathrm{e}^{pt}$ mit dem Gewicht $S(p)$.
:::

:::abbildung et3/k2sprung 14
Der Sprung, überlagert aus den Funktionen $\mathrm{e}^{pt}$ auf der Geraden $\operatorname{Re} p=0{,}5/\mathrm s$, wobei nur die mit $|f|\le F$ mitgenommen werden: $s_F(t)=\int_{-F}^{F}S(\sigma_0+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma_0+\mathrm{j}2\pi f)t}\mathrm{d} f$ mit $S(p)=1/p$. Je mehr Anteile, desto genauer der Sprung; bei $t=0$ strebt die Kurve gegen $\tfrac12$.
:::
:::

:::hintergrund Warum jede Gerade im Konvergenzbereich dasselbe Signal liefert
Bei größerem $\sigma_0$ dämpft man im ersten Schritt stärker und multipliziert im dritten stärker zurück; beides hebt sich auf. Numerisch bestätigt: Mit $\sigma_0=0{,}2$ und $\sigma_0=1/\mathrm s$ ergibt sich für den Sprung beide Male $s(1\,\mathrm{s})\approx1{,}00$ und $s(-1\,\mathrm{s})\approx0{,}00$.

Dass trotz komplexer Anteile eine reelle Kurve herauskommt, liegt an der Paarung: Zu $f$ gehört $-f$, zu $p$ also der konjugierte Punkt $p^*$. Für ein reelles Signal ist $S(p^*)=S(p)^*$ (nach der Regel zur Konjugation). Jedes Paar ergibt $S\,\mathrm{e}^{pt}+(S\,\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\,\mathrm{e}^{pt}\}$, also eine reelle gedämpfte oder wachsende Schwingung.

Im Allgemeinen ist die Überlagerung ein Integral, keine Summe: Auf der Geraden liegen kontinuierlich viele Funktionen $\mathrm{e}^{pt}$, jede mit einem infinitesimalen Gewicht.
:::

:::hintergrund Warum aus der Faltung eine Multiplikation wird: das Bild der Überlagerung
Mit der Umkehrformel bekommt der Faltungssatz eine anschauliche Bedeutung. Ein LTI-System ist linear: Es verarbeitet jede Funktion $\mathrm{e}^{pt}$ des Eingangs für sich und addiert die Ergebnisse. Jede multipliziert es nach [(1.6)](eigenfunktionen-von-lti-systemen.html#gl-1-6) mit $H(p)$. Der Ausgang besteht also aus *denselben* Funktionen $\mathrm{e}^{pt}$ wie der Eingang, nur ist jedes Gewicht mit $H(p)$ multipliziert (Abb. [15](#abb-15)):

$$\begin{aligned} g(t)&=\Bigl[\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\Bigr]*h(t) =\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\mathrm{d} p\\ &=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}\bigl[S(p)\,H(p)\bigr]\mathrm{e}^{pt}\,\mathrm{d} p . \end{aligned}$$

Die Gerade muss dafür in beiden Konvergenzbereichen liegen. Das ist die Umkehrformel für $g$ mit dem Gewicht $S(p)H(p)$.

:::abbildung et3/k2wege 15
Zwei Wege vom Eingang zum Ausgang. Oben direkt mit dem Faltungsintegral. Unten: Eingang zerlegen, jedes Gewicht mit $H(p)$ multiplizieren, wieder zusammensetzen. Der untere Weg funktioniert, weil jedes $\mathrm{e}^{pt}$ eine Eigenfunktion ist.
:::

Ein Bild dazu: Ein Equalizer zerlegt Musik in Frequenzbänder, multipliziert jedes Band mit der Stellung seines Reglers und setzt die Bänder wieder zusammen. Ein LTI-System macht dasselbe mit den Funktionen $\mathrm{e}^{pt}$, und die Reglerstellung ist $H(p)$. Das Bild hinkt an zwei Stellen: Ein Equalizer hat endlich viele Bänder mit reellen Reglern. Hier gibt es kontinuierlich viele Funktionen, die auch wachsen oder abklingen können, und jeder „Regler“ ist eine komplexe Zahl, die zusätzlich die Phase verschiebt.
:::

:::hintergrund Warum das Integral bei rationalem $S(p)$ zur Summe wird: der Residuensatz
Dieser Kasten braucht den Residuensatz der Funktionentheorie. Er erklärt, warum die Umkehrformel [(7.1)](#gl-7-1) und die Summe [(4.16)](losung-von-differentialgleichungen.html#gl-4-16) dasselbe liefern und warum der Konvergenzbereich über das Signal entscheidet.

Sei $S(p)$ ein Polynombruch mit kleinerem Zählergrad als Nennergrad und einfachen Polen.

<ul>

<li>

⁠**$t>0$:** Man schließt die Integrationsgerade durch einen großen Halbkreis nach *links*. Dort geht $\operatorname{Re} p\to-\infty$, also $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$, und $S(p)\to0$. Der Halbkreis trägt im Grenzfall nichts bei (Jordansches Lemma). Der geschlossene Weg läuft gegen den Uhrzeigersinn, und der Residuensatz gibt

$$s(t)=\sum_{\text{Pole links der Geraden}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{links}}A_r\,\mathrm{e}^{p_r t}.$$

Das Residuum an einem einfachen Pol ist $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$: genau der Partialbruchkoeffizient [(4.11)](losung-von-differentialgleichungen.html#gl-4-11).

</li>

<li>

⁠**$t<0$:** Jetzt verschwindet $\mathrm{e}^{pt}$ für $\operatorname{Re} p\to+\infty$. Man schließt nach *rechts*, der Weg läuft im Uhrzeigersinn, das gibt ein Minuszeichen:

$$s(t)=-\sum_{\text{Pole rechts der Geraden}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**Folge:** Die Lage der Geraden, also der Konvergenzbereich, entscheidet, welche Pole rechtsseitige Anteile liefern (links der Geraden) und welche linksseitige (rechts der Geraden). Beispiel: $S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$ (Abb. [16](#abb-16)). Liegt die Gerade zwischen den Polen, $-2<\sigma_0<-1$, wirkt $-2$ für $t>0$ und $-1$ für $t<0$:

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

Das ist Fall c) aus Abschnitt [3.4](pole-und-nullstellen-in-der-ebene.html#stufe-3-4). Numerisch auf der Geraden $\sigma_0=-1{,}5/\mathrm s$ ausgewertet: $s(1\,\mathrm{s})=-0{,}1353=-\mathrm{e}^{-2}$ und $s(-1\,\mathrm{s})=-2{,}7183=-\mathrm{e}^{1}$.

:::abbildung et3/k2residuen 16
Integrationsgerade $\sigma_0=-1{,}5/\mathrm s$ im Streifen $-2<\operatorname{Re} p<-1$ (blau) und die Halbkreise, mit denen man sie schließt (rot).
:::
:::

:::hintergrund Wozu man auch das Eingangssignal transformiert
$H(p)$ sagt, was das System mit einer einzelnen Funktion $\mathrm{e}^{pt}$ macht. Ein Eingang wie ein Sprung, ein Sprachsignal oder ein Rechteckimpuls ist aber keine einzelne solche Funktion. Ein Ausdruck wie $H(p)\cdot s(t)$ ergibt deshalb keinen Sinn: $H(p)$ darf nur auf eine Funktion $\mathrm{e}^{pt}$ angewandt werden, und für ein beliebiges $s(t)$ ist gar nicht klar, welches $p$ gemeint sein soll. Bevor $H(p)$ etwas tun kann, muss der Eingang in Funktionen $\mathrm{e}^{pt}$ zerlegt sein. Genau das leistet $S(p)$.

Im Faltungssatz $G(p)=H(p)\,S(p)$ hat deshalb jeder Faktor eine eigene Bedeutung:

<ul>

<li>

$S(p)$ ist das *Rezept des Eingangs*: wie viel von $\mathrm{e}^{pt}$ im Eingang steckt;

</li>

<li>

$H(p)$ ist die *Wirkung des Systems*: mit welcher Zahl es $\mathrm{e}^{pt}$ multipliziert;

</li>

<li>

$G(p)$ ist das Rezept des Ausgangs.

</li>

</ul>

⁠**Am Beispiel Sprung und RC-Tiefpass.** Der Sprung hat das Rezept $S(p)=1/p$. Auf der Geraden $\sigma_0=0{,}5/\mathrm s$ ist $|S|=2$ bei $f=0$, $0{,}16$ bei 1 Hz und $0{,}016$ bei 10 Hz. Die schnellen Anteile sind schwach, aber vorhanden, und sie bilden die scharfe Kante (Abb. [14](#abb-14): Je mehr schnelle Anteile, desto steiler die Kante). Der RC-Tiefpass mit $RC=1\,\mathrm{s}$ multipliziert sie mit $|H|=0{,}67$, $0{,}15$ und $0{,}016$. Im Ausgang sind die schnellen Anteile also noch einmal etwa um den Faktor $2\pi f\cdot RC$ schwächer (für $f\gg1/(2\pi RC)=0{,}16$ Hz), und die Kante ist weg: $g(t)=1-\mathrm{e}^{-t}$ steigt stetig an. Diese Erklärung braucht beide Transformierten. $H$ allein sagt nur „schnelle Anteile werden geschwächt“, erst $S$ sagt, dass die Kante aus schnellen Anteilen besteht.

⁠**Und die Symmetrie $s*h=h*s$?** Mathematisch sind beide Signale gleichberechtigt: Man kann auch $h$ als Eingang und $s$ als „System“ lesen. Die Systemtheorie verteilt die Rollen nur nach der Physik: Das eine Signal kommt von außen, das andere beschreibt die Schaltung.

⁠**Weitere Gründe, ein Signal für sich zu transformieren:**

<ul>

<li>

⁠**Ein System ausmessen:** $H(p)=G(p)/S(p)$ braucht zwei transformierte Signale (Aufgabe [9](systemanalyse-und-synthese.html#aufg-9)).

</li>

<li>

⁠**Das Signal selbst verstehen:** Der Ton einer angeschlagenen Glocke ist eine Summe gedämpfter Schwingungen, jede ein konjugiert komplexes Polpaar. Der Imaginärteil eines Pols ist die Kreisfrequenz eines Teiltons, der negative Realteil seine Abklingrate. Wenige Pole beschreiben den ganzen Klang.

</li>

</ul>
:::

:::aufgabe Aufgabe 10 ★ Laplace ist Fourier eines gedämpften Signals
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Zeige $S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$, indem du $\mathrm{e}^{-pt}$ in zwei Faktoren zerlegst.

</li>

<li>

Prüfe es am Sprung: Berechne $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}$ für $\sigma>0$ direkt und vergleiche mit $S(p)=1/p$.

</li>

</ol>

:::loesung
(a) $S(\sigma+\mathrm{j}2\pi f)=\int s(t)\,\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\int\bigl[s(t)\mathrm{e}^{-\sigma t}\bigr]\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}(f)$.

(b) $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}=\int_0^\infty\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\dfrac{1}{\sigma+\mathrm{j}2\pi f}$ für $\sigma>0$. Das ist $1/p$ an der Stelle $p=\sigma+\mathrm{j}2\pi f$.
:::
:::

:::aufgabe Aufgabe 11 ★ Richtig oder falsch? Mit Begründung
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Jede Funktion hat eine Laplace-Transformierte.

</li>

<li>

Ob $p$ im Konvergenzbereich liegt, hängt nur von $\operatorname{Re} p$ ab.

</li>

<li>

Liegt die imaginäre Achse im Konvergenzbereich, ist $S(\mathrm{j}2\pi f)$ das Spektrum von $s(t)$.

</li>

<li>

In der Umkehrformel liefert $\sigma_0=1/\mathrm s$ ein anderes Signal als $\sigma_0=2/\mathrm s$, wenn beide im Konvergenzbereich liegen.

</li>

<li>

$\cos(2\pi f_0t)$ ist eine Eigenfunktion jedes LTI-Systems.

</li>

</ol>

:::loesung
(a) Falsch. Gegenbeispiele: $\mathrm{e}^{t^2}\varepsilon(t)$, $\mathrm{e}^{|t|}$, die zweiseitige Konstante.

(b) Richtig. $|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$, die Frequenz $f$ kommt im Betrag nicht vor. Deshalb besteht der Konvergenzbereich aus ganzen senkrechten Geraden.

(c) Richtig. Mit $\sigma=0$ ist $S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$.

(d) Falsch. Jede Gerade im Konvergenzbereich liefert dasselbe Signal, weil die Dämpfung $\mathrm{e}^{-\sigma_0t}$ und das Zurückmultiplizieren mit $\mathrm{e}^{\sigma_0t}$ sich aufheben.

(e) Falsch. Der Ausgang ist $|H|\cos(2\pi f_0t+\varphi)$ mit $H=H(\mathrm{j}2\pi f_0)$. Er ist nur dann ein Vielfaches von $\cos(2\pi f_0t)$, wenn $\varphi=0$ oder $\varphi=\pi$ ist, wenn also $H(\mathrm{j}2\pi f_0)$ reell ist. Für den RC-Tiefpass ist das bei keiner Frequenz $f_0>0$ der Fall.
:::
:::

:::aufgabe Aufgabe 12 ★★ Welche Anteile bilden die Kante?
<span class="anker" id="aufg-12"></span>

Eingang $\varepsilon(t)$, System RC-Tiefpass mit $RC=1$ s. Betrachte die Funktionen $\mathrm{e}^{pt}$ auf der Geraden $\sigma_0=0{,}5/\mathrm s$.

<ol class="al">

<li>

Berechne $|S(p)|$, $|H(p)|$ und $|G(p)|$ für $f=0$, $1$ Hz und $10$ Hz.

</li>

<li>

Um welchen Faktor schwächt das System die Anteile bei 10 Hz stärker als die bei 1 Hz?

</li>

<li>

Erkläre mit (a) und Abb. [14](#abb-14), warum der Ausgang keine Kante hat. Warum reicht $H(p)$ allein für diese Erklärung nicht?

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

(c) Die Kante des Sprungs besteht aus den schnellen Anteilen: In Abb. [14](#abb-14) wird sie steiler, je mehr davon mitgenommen werden. Im Eingang fallen ihre Gewichte wie $1/f$, im Ausgang wie $1/f^2$. Die schnellen Anteile sind im Ausgang so schwach, dass keine Kante mehr entsteht, und $g(t)$ steigt stetig an. $H(p)$ allein sagt nur, dass schnelle Anteile geschwächt werden. Dass die Kante aus genau diesen Anteilen besteht, ist eine Aussage über den Eingang, und die steht in $S(p)$.
:::
:::

:::aufgabe Aufgabe 13 ★★★ Dieselbe Formel, zwei Signale (mit Residuensatz)
<span class="anker" id="aufg-13"></span>

$S(p)=\dfrac{1}{p+1}$.

<ol class="al">

<li>

Konvergenzbereich $\operatorname{Re} p>-1$. Werte die Umkehrformel mit dem Residuensatz aus, getrennt für $t>0$ und $t<0$.

</li>

<li>

Dasselbe für den Konvergenzbereich $\operatorname{Re} p<-1$.

</li>

<li>

Vergleiche mit den Grundpaaren [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) und [(2.10)](beispiele-zur-laplace-transformation.html#gl-2-10). Was lernst du daraus über die Angabe „$S(p)=1/(p+1)$“ ohne Konvergenzbereich?

</li>

</ol>

:::loesung
(a) Gerade rechts vom Pol, zum Beispiel $\sigma_0=0$. Für $t>0$ nach links schließen: Der Pol $-1$ liegt innen, $\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$, also $s(t)=\mathrm{e}^{-t}$. Für $t<0$ nach rechts schließen: Rechts der Geraden liegt kein Pol, $s(t)=0$. Zusammen $s(t)=\mathrm{e}^{-t}\varepsilon(t)$.

(b) Gerade links vom Pol, zum Beispiel $\sigma_0=-2$. Für $t>0$ nach links schließen: kein Pol, $s(t)=0$. Für $t<0$ nach rechts schließen: Pol innen, Umlauf im Uhrzeigersinn, $s(t)=-\mathrm{e}^{-t}$. Zusammen $s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$.

(c) Das sind genau die Grundpaare [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) und [(2.10)](beispiele-zur-laplace-transformation.html#gl-2-10) mit $p_0=-1$. Die Angabe „$S(p)=1/(p+1)$“ allein legt das Signal nicht fest. Erst mit dem Konvergenzbereich ist klar, auf welcher Seite der Geraden der Pol liegt und ob er einen rechtsseitigen oder einen linksseitigen Anteil liefert.
:::
:::

::::kurzfassung
Hier stehen die Rechenregeln und Transformationspaare des Kapitels gesammelt, ergänzt um fünf Regeln. Dazu kommt die Umkehrformel, die aus $S(p)$ das Signal zurückgewinnt.

Die neuen Regeln folgen je mit einer Substitution aus der Definition. Eine Verzögerung $s(t-t_0)$ multipliziert $S(p)$ mit $\mathrm{e}^{-pt_0}$. Der Faktor $\mathrm{e}^{p_0t}$ im Zeitbereich verschiebt die Transformierte zu $S(p-p_0)$ und damit alle Pole um $p_0$. Konjugation ergibt $S^*(p^*)$, Zeitspiegelung $S(-p)$ mit gespiegeltem Konvergenzbereich, Zeitdehnung $s\bigl(\frac tT\bigr)$ ergibt $|T|\,S(pT)$. Neu unter den Paaren ist nur der verschobene Dirac-Impuls, $\delta(t-t_0)\longleftrightarrow\mathrm{e}^{-pt_0}$ für alle $p$.

Mit $\sigma_0$ beliebig im Konvergenzbereich lautet die Umkehrformel

$$s(t)=\mathcal{L}^{-1}\{S(p)\}=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p .$$

Sie setzt das Signal aus den Funktionen $\mathrm{e}^{pt}$ auf der senkrechten Geraden $\operatorname{Re} p=\sigma_0$ zusammen, jede mit dem Gewicht $S(p)$; $S(p)$ ist also eine Dichte. An einer Sprungstelle liefert sie den Mittelwert aus links- und rechtsseitigem Grenzwert.

Der Mechanismus: Man dämpft das Signal mit $\mathrm{e}^{-\sigma_0t}$, bis es absolut integrierbar ist, und zerlegt es mit der __Fourier-Darstellung__ in Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$. Das __Spektrum__ des gedämpften Signals ist $S(\sigma_0+\mathrm{j}2\pi f)$. Danach multipliziert man mit $\mathrm{e}^{\sigma_0t}$ zurück. Liegt die imaginäre Achse im Konvergenzbereich, ist $\sigma_0=0$ erlaubt, und die Formel wird zur Fourier-Darstellung.

Bei einem Polynombruch $S(p)$ führen Partialbrüche und Tabelle schneller zum Ziel. Falle: Die Gerade muss im Konvergenzbereich liegen; ihre Lage entscheidet, welche Pole rechtsseitige und welche linksseitige Anteile liefern.
::::

::::formelsammlung
**Superposition**

$$\sum_ia_i\,s_i(t)\longleftrightarrow\sum_ia_i\,S_i(p)$$

Für alle $p$, für die alle Integrale konvergieren.

**Verschiebung in $t$**

$$s(t-t_0)\longleftrightarrow S(p)\,\mathrm{e}^{-pt_0}$$

Konvergenzbereich bleibt gleich. Einseitig nur für $t_0>0$ oder wenn $s(t)=0$ für $t<t_0$.

**Verschiebung in $p$**

$$s(t)\cdot\mathrm{e}^{p_0t}\longleftrightarrow S(p-p_0)$$

Konvergenzbereich um $\operatorname{Re} p_0$ verschoben; alle Pole wandern um $p_0$.

**Konjugation**

$$s^*(t)\longleftrightarrow S^*(p^*)$$

Für ein reelles Signal folgt $S(p^*)=S(p)^*$.

**Zeitspiegelung**

$$s(-t)\longleftrightarrow S(-p)$$

Konvergenzbereich und Pole an der imaginären Achse gespiegelt. Bei einseitiger Transformation nicht anwendbar.

**Zeitdehnung**

$$s\bigl(\frac tT\bigr)\longleftrightarrow|T|\,S(pT)$$

$T\ne0$; bei einseitiger Transformation nur für $T>0$. Ein Pol $p_r$ wird zu $p_r/T$.

**Faltung**

$$g(t)=s(t)*h(t)\longleftrightarrow G(p)=S(p)\cdot H(p)$$

Für alle $p$ in den Konvergenzbereichen von $S$ und $H$.

**Ableitung**

$$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\longleftrightarrow p^n\cdot S(p)$$

Konvergenzbereich mindestens der von $S(p)$.

**Integration**

$$\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau\longleftrightarrow\frac1p\,S(p)$$

Zusätzlich $\operatorname{Re} p>0$.

**Paar: Dirac-Impuls**

$$\delta(t)\longleftrightarrow1$$

Alle $p$.

**Paar: verschobener Dirac-Impuls**

$$\delta(t-t_0)\longleftrightarrow\mathrm{e}^{-pt_0}$$

Alle $p$.

**Paar: Sprung**

$$\varepsilon(t)\longleftrightarrow\frac1p$$

$\operatorname{Re} p>0$.

**Paar: linksseitiger Sprung**

$$-\varepsilon(-t)\longleftrightarrow\frac1p$$

$\operatorname{Re} p<0$.

**Paar: Potenzen von $t$**

$$\frac{t^{n-1}}{(n-1)!}\,\varepsilon(t)=\underbrace{\varepsilon(t)*\ldots*\varepsilon(t)}_{n\text{ Funktionen}}\longleftrightarrow\frac{1}{p^n}$$

$\operatorname{Re} p>0$.

**Paar: rechtsseitige Exponentialfunktion**

$$\mathrm{e}^{p_0t}\,\varepsilon(t)\longleftrightarrow\frac{1}{p-p_0}$$

$\operatorname{Re} p>\operatorname{Re} p_0$; $p_0$ komplex.

**Paar: linksseitige Exponentialfunktion**

$$-\mathrm{e}^{p_0t}\,\varepsilon(-t)\longleftrightarrow\frac{1}{p-p_0}$$

$\operatorname{Re} p<\operatorname{Re} p_0$.

**Paar: mehrfacher Pol**

$$\frac{t^{\,j-1}}{(j-1)!}\,\mathrm{e}^{p_0t}\,\varepsilon(t)\longleftrightarrow\frac{1}{(p-p_0)^j}$$

$\operatorname{Re} p>\operatorname{Re} p_0$.

**Paar: gedämpfter Kosinus**

$$\mathrm{e}^{-\gamma t}\cos(\omega_1t)\cdot\varepsilon(t)\longleftrightarrow\frac{p+\gamma}{(p+\gamma)^2+\omega_1^2}$$

$\operatorname{Re} p>-\gamma$; $\gamma$, $\omega_1$ reell.

**Paar: gedämpfter Sinus**

$$\mathrm{e}^{-\gamma t}\sin(\omega_1t)\cdot\varepsilon(t)\longleftrightarrow\frac{\omega_1}{(p+\gamma)^2+\omega_1^2}$$

$\operatorname{Re} p>-\gamma$.

**Umkehrformel**

$$s(t)=\mathcal{L}^{-1}\{S(p)\}=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p$$

$\sigma_0$ beliebig im Konvergenzbereich; Weg: senkrechte Gerade $\operatorname{Re} p=\sigma_0$, von unten nach oben. An Sprungstellen liefert sie den Mittelwert aus links- und rechtsseitigem Grenzwert.

**Umkehrformel über die Frequenz**

$$s(t)=\int_{-\infty}^{\infty}S(\sigma_0+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma_0+\mathrm{j}2\pi f)t}\,\mathrm{d} f$$

Mit $p=\sigma_0+\mathrm{j}2\pi f$, $\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$; Integral als $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$. $S(p)$ ist eine Dichte (Gewicht pro Frequenzintervall).

**Fourier-Darstellung**

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$$

Für absolut integrierbare Signale; $\mathcal{F}\{s\}(f)$ ist das Spektrum.

**Laplace als Fourier eines gedämpften Signals**

$$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$$

Für $\sigma$ im Konvergenzbereich. Liegt die imaginäre Achse darin, ist $S(\mathrm{j}2\pi f)=\mathcal{F}\{s\}(f)$.

**Rücktransformation mit Residuen, $t>0$**

$$s(t)=\sum_{\text{Pole links der Geraden}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{links}}A_r\,\mathrm{e}^{p_r t}$$

$S(p)$ Polynombruch mit kleinerem Zähler- als Nennergrad und einfachen Polen; Weg nach links geschlossen.

**Rücktransformation mit Residuen, $t<0$**

$$s(t)=-\sum_{\text{Pole rechts der Geraden}}A_r\,\mathrm{e}^{p_r t}$$

Weg nach rechts geschlossen. Die Lage der Geraden entscheidet, welche Pole rechts- und welche linksseitige Anteile liefern.
::::

::::lernkarten
:::karte formel Verschiebung in der Zeit
Was wird aus einem verzögerten Signal $s(t-t_0)$ im Bildbereich, und was ändert die Verzögerung an Polen und Betrag?
---
Es wird $S(p)\,\mathrm{e}^{-pt_0}$, der Konvergenzbereich bleibt gleich. Der Faktor $\mathrm{e}^{-pt_0}$ hat weder Pole noch Nullstellen: Das Signal besteht aus denselben Exponentialfunktionen, nur später. Auf der imaginären Achse ist $|\mathrm{e}^{-\mathrm{j}2\pi Ft_0}|=1$, die Verzögerung ändert nur die Phase.
--- falsch
Es wird $S(p-t_0)$, und der Konvergenzbereich verschiebt sich um $t_0$ nach rechts. Alle Pole wandern um $t_0$, weil ein späteres Signal langsamer abklingt; auf der imaginären Achse wird der Betrag dadurch bei allen Frequenzen kleiner.
--- falsch
Es wird $S(p)\,\mathrm{e}^{pt_0}$, der Konvergenzbereich bleibt gleich. Der Faktor $\mathrm{e}^{pt_0}$ fügt bei $p=t_0$ einen zusätzlichen Pol hinzu, der die Verzögerung beschreibt; auf der imaginären Achse wächst der Betrag mit der Frequenz.
--- falsch
Es wird $S(p)-t_0$, weil sich das Signal nur entlang der Zeitachse verschiebt und die Transformation linear ist. Pole und Nullstellen bleiben gleich, aber der Betrag auf der imaginären Achse sinkt bei allen Frequenzen um denselben Wert $t_0$, gemessen in Sekunden.
:::
:::karte formel Verschiebung in der komplexen Frequenz
Was wird aus dem Signal $s(t)\cdot\mathrm{e}^{p_0t}$ im Bildbereich, und was passiert dabei mit den Polen?
---
Es wird $S(p-p_0)$, der Konvergenzbereich ist um $\operatorname{Re} p_0$ verschoben. Aus jedem Anteil $\mathrm{e}^{p_rt}$ wird $\mathrm{e}^{(p_r+p_0)t}$, alle Pole wandern um $p_0$; bei $\mathrm{e}^{\mathrm{j}2\pi F_0t}$ wandern sie um $2\pi F_0$ nach oben, und alle Frequenzen steigen um $F_0$.
--- falsch
Es wird $S(p+p_0)$, der Konvergenzbereich ist um $-\operatorname{Re} p_0$ verschoben. Aus jedem Anteil $\mathrm{e}^{p_rt}$ wird $\mathrm{e}^{(p_r-p_0)t}$, alle Pole wandern um $-p_0$, weil im Laplace-Integral $\mathrm{e}^{-pt}$ steht und das Vorzeichen umdreht.
--- falsch
Es wird $S(p)\cdot\frac{1}{p-p_0}$, weil zum Signal ein neuer Anteil $\mathrm{e}^{p_0t}$ hinzukommt. Die alten Pole bleiben an ihrem Ort, und ein zusätzlicher Pol bei $p_0$ erscheint; die Frequenzen des Signals ändern sich dabei nicht.
--- falsch
Es wird $S(p)\,\mathrm{e}^{-pt_0}$ mit $t_0=p_0$, denn eine Multiplikation mit einer Exponentialfunktion ist dasselbe wie eine Verzögerung. Die Pole bleiben an ihrem Ort, nur die Phase auf der imaginären Achse ändert sich.
:::
:::karte formel Zeitspiegelung und Zeitdehnung
Welche Transformierten haben das gespiegelte Signal $s(-t)$ und das gedehnte Signal $s\bigl(\frac tT\bigr)$, und was geschieht mit den Polen?
---
Zu $s(-t)$ gehört $S(-p)$: Pole und Konvergenzbereich werden an der imaginären Achse gespiegelt, rechtsseitige Anteile werden linksseitig. Zu $s\bigl(\frac tT\bigr)$ gehört $|T|\,S(pT)$ mit $T\ne0$; ein Pol $p_r$ wird zu $p_r/T$.
--- falsch
Zu $s(-t)$ gehört $-S(p)$, weil sich nur das Vorzeichen der Zeit ändert; Pole und Konvergenzbereich bleiben gleich. Zu $s\bigl(\frac tT\bigr)$ gehört $\frac{1}{T}\,S\bigl(\frac pT\bigr)$, und ein Pol $p_r$ wird zu $p_r\,T$.
--- falsch
Zu $s(-t)$ gehört $S^*(p)$, die konjugierte Transformierte, und die Pole werden an der reellen Achse gespiegelt. Zu $s\bigl(\frac tT\bigr)$ gehört $S(pT)$ ohne Vorfaktor; ein Pol $p_r$ wird zu $p_r/T$, für jedes Vorzeichen von $T$.
--- falsch
Zu $s(-t)$ gehört $S(-p)$, aber der Konvergenzbereich bleibt derselbe, weil er nur von $\operatorname{Re} p$ abhängt. Zu $s\bigl(\frac tT\bigr)$ gehört $|T|\,S(pT)$; läuft das Signal schneller ab, rücken die Pole näher an den Ursprung.
:::
:::karte formel Konjugation
Welche Transformierte hat das konjugiert komplexe Signal $s^*(t)$, und was folgt daraus für ein reelles Signal?
---
Zu $s^*(t)$ gehört $S^*(p^*)$, denn $(\mathrm{e}^{-p^*t})^*=\mathrm{e}^{-pt}$. Für ein reelles Signal ist $s^*=s$, also $S(p^*)=S(p)^*$: Am konjugierten Punkt hat die Transformierte den konjugierten Wert.
--- falsch
Zu $s^*(t)$ gehört $S^*(p)$, weil man nur das Ergebnis konjugieren muss. Für ein reelles Signal ist deshalb $S(p)$ selbst reell, für jedes komplexe $p$, und hat nirgends einen Imaginärteil.
--- falsch
Zu $s^*(t)$ gehört $S(-p)$, weil Konjugieren einer Spiegelung der Zeit entspricht. Für ein reelles Signal ist deshalb $S(-p)=S(p)$: Die Transformierte ist symmetrisch zum Ursprung der $p$-Ebene.
--- falsch
Zu $s^*(t)$ gehört $S(p^*)$ ohne weitere Konjugation. Für ein reelles Signal ist deshalb $S(p^*)=S(p)$: Am konjugierten Punkt hat die Transformierte denselben Wert, auch im Imaginärteil.
:::
:::karte herleitung Regel für die Zeitdehnung
Wie folgt aus der Definition der Laplace-Transformation die Regel, dass zu $s\bigl(\frac tT\bigr)$ die Transformierte $|T|\,S(pT)$ gehört?
---
Man substituiert $u=t/T$ mit $\mathrm{d} t=T\,\mathrm{d} u$, weil dann im Signal nur noch $s(u)$ steht.
---
Für $T>0$ ist $\int s(t/T)\,\mathrm{e}^{-pt}\mathrm{d} t=T\int s(u)\,\mathrm{e}^{-(pT)u}\mathrm{d} u=T\,S(pT)$, weil der Exponent $-(pT)u$ lautet und die Grenzen erhalten bleiben.
---
Für $T<0$ vertauschen sich die Grenzen, weil $u$ dann von $+\infty$ nach $-\infty$ läuft; das gibt ein zusätzliches Minus.
---
Zusammen entsteht $|T|\,S(pT)$, weil $T$ für $T>0$ und $-T$ für $T<0$ gerade der Betrag $|T|$ ist.
:::
:::karte formel Umkehrformel
Wie lautet die Umkehrformel der Laplace-Transformation, und auf welchem Weg wird integriert?
---
$s(t)=\mathcal{L}^{-1}\{S(p)\}=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p$. Integriert wird längs der senkrechten Geraden $\operatorname{Re} p=\sigma_0$ von unten nach oben; $\sigma_0$ muss im Konvergenzbereich liegen und darf dort beliebig gewählt werden.
--- falsch
$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\mathrm{e}^{-pt}\,\mathrm{d} p$, mit demselben Vorzeichen im Exponenten wie bei der Hintransformation. Integriert wird längs der Geraden $\operatorname{Re} p=\sigma_0$, die genau durch den am weitesten rechts liegenden Pol gehen muss.
--- falsch
$s(t)=\int_{-\infty}^{\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p$ über die reelle Achse der $p$-Ebene. Integriert wird von links nach rechts über alle reellen $p$, gleichgültig, wo der Konvergenzbereich liegt, weil das Signal reell ist und nur reelle $p$ braucht.
--- falsch
$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p$. Integriert wird längs der imaginären Achse, also stets mit $\sigma_0=0$; andere Geraden liefern ein anderes Signal, das um den Faktor $\mathrm{e}^{\sigma_0t}$ verfälscht ist.
:::
:::karte zusammenhang Transformierte als Gewicht
Was gibt $S(p)$ nach der Umkehrformel über das Signal $s(t)$ an, und welche Einheit hat es, wenn $s$ eine Spannung ist?
---
Wie stark die Funktion $\mathrm{e}^{pt}$ im Signal vertreten ist: Die Umkehrformel überlagert die $\mathrm{e}^{pt}$ auf der Geraden, jede mit dem komplexen Gewicht $S(p)\,\mathrm{d} f$. $S(p)$ ist also eine Dichte, ein Gewicht pro Frequenzintervall; ist $s$ eine Spannung in V, hat $S$ die Einheit V s.
--- falsch
Den Wert des Signals zur komplexen Zeit $t=p$: Die Umkehrformel rechnet diese Werte auf reelle Zeiten zurück. $S(p)$ hat deshalb dieselbe Einheit wie das Signal, bei einer Spannung also V, und ist für reelles $p$ der Wert des Signals selbst.
--- falsch
Wie stark die Funktion $\mathrm{e}^{pt}$ im Signal vertreten ist, und zwar als Amplitude, nicht als Dichte: Jede Funktion geht mit dem Gewicht $S(p)$ ein. $S(p)$ hat deshalb dieselbe Einheit wie das Signal, bei einer Spannung also V, unabhängig von der Frequenz.
--- falsch
Die Energie des Signals bei der komplexen Frequenz $p$: Die Umkehrformel addiert die Energien aller Funktionen $\mathrm{e}^{pt}$ auf. $S(p)$ hat deshalb die Einheit einer Energie je Frequenz, bei einer Spannung also $\mathrm V^2\,\mathrm s$.
:::
:::karte zusammenhang Wert an einer Sprungstelle
Was liefert die Umkehrformel an einer Sprungstelle des Signals, etwa beim Einheitssprung zur Zeit $t=0$?
---
Den Mittelwert aus links- und rechtsseitigem Grenzwert; an jeder Stelle, an der $s$ stetig ist, liefert sie $s(t)$. Beim Sprung $\varepsilon(t)$ strebt die Überlagerung bei $t=0$ deshalb gegen $\tfrac12$.
--- falsch
Den rechtsseitigen Grenzwert, weil die Umkehrformel nur für $t>0$ gilt. Beim Sprung $\varepsilon(t)$ liefert sie bei $t=0$ deshalb den Wert 1, wie für alle späteren Zeiten auch.
--- falsch
Den linksseitigen Grenzwert, weil das Integral vom unteren Ende der Geraden her läuft. Beim Sprung $\varepsilon(t)$ liefert sie bei $t=0$ deshalb den Wert 0, wie für alle früheren Zeiten.
--- falsch
Gar keinen Wert: An einer Sprungstelle divergiert das Integral, weil dort beliebig schnelle Anteile nötig sind. Beim Sprung $\varepsilon(t)$ wächst die Überlagerung bei $t=0$ über alle Grenzen.
:::
:::karte begriff Fourier-Darstellung und Spektrum
Was beschreiben die Fourier-Darstellung eines absolut integrierbaren Signals und sein Spektrum?
---
Die Fourier-Darstellung setzt das Signal aus reinen Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$ zusammen: $s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$. Das Spektrum $\mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$ gibt das Gewicht der Schwingung mit der Frequenz $f$ an.
--- falsch
Die Fourier-Darstellung setzt das Signal aus gedämpften Schwingungen $\mathrm{e}^{pt}$ zusammen, für jedes Signal, auch für wachsende. Das Spektrum ist die Laplace-Transformierte auf der reellen Achse, $S(\sigma)$, und gibt die Dämpfung jedes einzelnen Anteils an.
--- falsch
Die Fourier-Darstellung zerlegt das Signal in Rechteckimpulse gleicher Breite: $s(t)=\sum_k s(k)\operatorname{rect}(t-k)$. Das Spektrum ist die Folge der Höhen $s(k)$ dieser Impulse und gibt den Wert des Signals zu jeder ganzzahligen Zeit an.
--- falsch
Die Fourier-Darstellung setzt das Signal aus reinen Schwingungen zusammen: $s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} f$. Das Spektrum $\mathcal{F}\{s\}(f)$ ist der Betrag des Signals zur Zeit $t=1/f$, also eine reelle, nicht negative Größe.
:::
:::karte herleitung Umkehrformel aus der Fourier-Darstellung
Wie gewinnt man die Umkehrformel aus der Fourier-Darstellung, wenn das Signal selbst nicht absolut integrierbar ist?
---
Dämpfen: Man multipliziert mit $\mathrm{e}^{-\sigma_0t}$, weil $s(t)\,\mathrm{e}^{-\sigma_0t}$ absolut integrierbar ist, wenn $\sigma_0$ im Konvergenzbereich liegt.
---
Zerlegen: Das Spektrum des gedämpften Signals ist $S(\sigma_0+\mathrm{j}2\pi f)$, weil sich die Faktoren zu $\mathrm{e}^{-(\sigma_0+\mathrm{j}2\pi f)t}$ zusammenfassen. Die Fourier-Darstellung gibt $s(t)\,\mathrm{e}^{-\sigma_0t}=\int S(\sigma_0+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$.
---
Zurückmultiplizieren: Man multipliziert mit $\mathrm{e}^{\sigma_0t}$ und zieht den Faktor ins Integral, weil er nicht von $f$ abhängt: $s(t)=\int_{-\infty}^{\infty}S(\sigma_0+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma_0+\mathrm{j}2\pi f)t}\,\mathrm{d} f$.
---
Mit $p=\sigma_0+\mathrm{j}2\pi f$, also $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$, entsteht die Umkehrformel, weil die Grenzen $f=\mp\infty$ zu $p=\sigma_0\mp\mathrm{j}\infty$ werden.
:::
:::karte zusammenhang Laplace enthält Fourier
Was wird aus der Laplace-Transformation, wenn die imaginäre Achse im Konvergenzbereich liegt und man $\sigma_0=0$ wählt?
---
Dann ist $S(\mathrm{j}2\pi f)=\mathcal{F}\{s\}(f)$ das Spektrum des Signals, und die Umkehrformel wird zur Fourier-Darstellung. Die Laplace-Transformation enthält die Fourier-Transformation also als Spezialfall.
--- falsch
Dann ist $S(\mathrm{j}2\pi f)=0$ für alle $f$, weil auf der imaginären Achse keine gedämpften Anteile liegen. Die Umkehrformel liefert in diesem Fall nur das Nullsignal und ist deshalb nicht anwendbar.
--- falsch
Dann ist $S(\mathrm{j}2\pi f)$ der Betrag des Spektrums, $|\mathcal{F}\{s\}(f)|$, ohne Phase. Die Umkehrformel wird zur Fourier-Darstellung, aber nur für gerade Signale, deren Spektrum reell ist.
--- falsch
Dann ist $S(0)=\mathcal{F}\{s\}(f)$ für jede Frequenz $f$, weil der Realteil null ist. Die Laplace-Transformation und die Fourier-Transformation stimmen deshalb nur im Ursprung der $p$-Ebene überein.
:::
:::karte zusammenhang Jede Gerade liefert dasselbe Signal
Warum liefert jede senkrechte Gerade im Konvergenzbereich in der Umkehrformel dasselbe Signal?
---
Die Herleitung dämpft das Signal mit $\mathrm{e}^{-\sigma_0t}$ und multipliziert am Ende mit $\mathrm{e}^{\sigma_0t}$ zurück. Bei größerem $\sigma_0$ dämpft man stärker und multipliziert stärker zurück; beides hebt sich auf.
--- falsch
Weil $S(p)$ auf allen senkrechten Geraden dieselben Werte hat: Es hängt wie der Konvergenzbereich nur vom Imaginärteil von $p$ ab. Das Integral ist deshalb auf jeder Geraden dasselbe.
--- falsch
Weil die Gerade die Pole nicht berührt und das Integral zwischen zwei Polen nach dem Residuensatz immer null ist. Deshalb trägt nur der Punkt der Geraden bei, der auf der reellen Achse liegt.
--- falsch
Weil die Umkehrformel nur die Pole auswertet und alle Geraden dieselben Pole umschließen. Auch eine Gerade außerhalb des Konvergenzbereichs liefert deshalb dasselbe Signal, solange sie keinen Pol schneidet.
:::
:::karte zusammenhang Reelles Signal aus komplexen Anteilen
Warum kommt bei der Umkehrformel für ein reelles Signal eine reelle Kurve heraus, obwohl die Anteile $\mathrm{e}^{pt}$ komplex sind?
---
Zu $f$ gehört $-f$, zu $p$ also der konjugierte Punkt $p^*$, und für ein reelles Signal ist $S(p^*)=S(p)^*$. Jedes Paar ergibt $S\,\mathrm{e}^{pt}+(S\,\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\,\mathrm{e}^{pt}\}$, eine reelle gedämpfte oder wachsende Schwingung.
--- falsch
Weil man von der Umkehrformel am Ende nur den Realteil nimmt und den Imaginärteil verwirft. Der Imaginärteil enthält die negativen Frequenzen, die physikalisch keine Bedeutung haben und deshalb wegfallen dürfen.
--- falsch
Weil $S(p)$ für ein reelles Signal auf der ganzen Geraden reell ist und $\mathrm{e}^{pt}$ sich über eine Periode zu einer reellen Zahl mittelt. Die Imaginärteile heben sich deshalb in jedem einzelnen Anteil für sich auf.
--- falsch
Zu $f$ gehört $-f$, und für ein reelles Signal ist $S(p^*)=-S(p)$. Jedes Paar ergibt deshalb $S\,\mathrm{e}^{pt}-S\,\mathrm{e}^{p^*t}$, und weil die Exponentialfunktionen konjugiert sind, bleibt nur ein reeller Rest übrig.
:::
:::karte zusammenhang Residuensatz und Konvergenzbereich
Warum entscheidet bei der Auswertung der Umkehrformel mit dem Residuensatz die Lage der Integrationsgeraden, welche Pole rechtsseitige und welche linksseitige Anteile liefern?
---
Für $t>0$ verschwindet $\mathrm{e}^{pt}$ für $\operatorname{Re} p\to-\infty$; man schließt die Gerade nach links, und die Pole links von ihr liefern $\sum_rA_r\,\mathrm{e}^{p_rt}$. Für $t<0$ schließt man nach rechts, im Uhrzeigersinn, und die Pole rechts der Geraden liefern mit Minuszeichen die linksseitigen Anteile.
--- falsch
Für $t>0$ schließt man die Gerade nach rechts, weil dort die Zukunft liegt, und die Pole rechts liefern die rechtsseitigen Anteile. Für $t<0$ schließt man nach links; die Lage der Geraden ist dabei gleichgültig, es zählen allein die Pole.
--- falsch
Für jedes $t$ schließt man die Gerade nach links und erfasst so alle Pole der $p$-Ebene. Ob ein Anteil rechtsseitig ist, entscheidet dann das Vorzeichen seines Residuums: Positive Residuen gehören zu rechtsseitigen, negative zu linksseitigen Anteilen.
--- falsch
Für $t>0$ schließt man die Gerade nach links, und die Pole links liefern linksseitige Anteile, weil sie links in der $p$-Ebene liegen. Für $t<0$ liefern die Pole rechts entsprechend die rechtsseitigen Anteile, und zwar ohne Minuszeichen.
:::
:::karte zusammenhang Wozu man den Eingang transformiert
Warum ergibt ein Ausdruck wie $H(p)\cdot s(t)$ keinen Sinn, und wozu transformiert man deshalb auch den Eingang?
---
$H(p)$ darf nur auf eine Funktion $\mathrm{e}^{pt}$ angewandt werden, und für ein beliebiges $s(t)$ ist nicht klar, welches $p$ gemeint ist. Erst $S(p)$ zerlegt den Eingang in Funktionen $\mathrm{e}^{pt}$; dann ist $G(p)=H(p)\,S(p)$ das Rezept des Ausgangs.
--- falsch
Weil $H(p)$ eine komplexe und $s(t)$ eine reelle Größe ist und man beide nicht multiplizieren darf. Transformiert man den Eingang, wird er ebenfalls komplex, und das Produkt $H(p)\,S(p)$ ist dann erlaubt.
--- falsch
Weil $H(p)$ eine reine Zahl ist und $s(t)$ in V gemessen wird, sodass die Einheiten nicht zusammenpassen. Transformiert man den Eingang, bekommt er die Einheit V s, und das Produkt hat wieder die Einheit einer Spannung.
--- falsch
Weil $H(p)\cdot s(t)$ nur für $t>0$ definiert ist und der Eingang auch vor dem Einschalten Werte haben kann. Die Transformation schneidet den Eingang bei $t=0$ ab, sodass das Produkt danach überall definiert ist.
:::
:::karte zusammenhang Die Kante verschwindet
Warum hat die Sprungantwort $g(t)=1-\mathrm{e}^{-t}$ des RC-Tiefpasses mit $RC=1$ s keine Kante, obwohl der Sprung am Eingang eine hat?
---
Die Kante besteht aus den schnellen Anteilen, deren Gewichte $|S|$ im Sprung wie $1/f$ fallen. Der Tiefpass schwächt sie zusätzlich etwa um den Faktor $2\pi f\cdot RC$; im Ausgang fallen sie wie $1/f^2$ und reichen für keine Kante mehr. Das zeigen erst $S$ und $H$ zusammen.
--- falsch
Weil der Tiefpass alle schnellen Anteile vollständig entfernt: Oberhalb einer Grenzfrequenz ist $|H|=0$. Ohne diese Anteile bleibt nur der Gleichanteil übrig, der langsam aufgebaut wird; $S(p)$ spielt für diese Erklärung keine Rolle, nur $H(p)$.
--- falsch
Weil der Sprung selbst gar keine schnellen Anteile enthält; seine Kante entsteht allein aus dem Pol bei $p=0$. Der Tiefpass verschiebt diesen Pol nach $-1$, und ein Pol links der imaginären Achse kann keine Kante erzeugen.
--- falsch
Weil der Tiefpass die langsamen Anteile so stark verstärkt, dass sie die schnellen überdecken. Die schnellen Anteile bleiben dabei in voller Stärke erhalten, fallen aber neben den verstärkten langsamen Anteilen nicht mehr auf.
:::
::::
