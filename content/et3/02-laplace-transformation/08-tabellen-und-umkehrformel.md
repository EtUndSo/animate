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
