---
title: Konvergenzbereich: welche Dämpfungen funktionieren
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220500
summary: Jedes Signal als Überlagerung von $\mathrm{e}^{pt}$, und warum ein LTI-System daraus eine Multiplikation macht
tags: 
lang: de
---

<span class="anker" id="stufe-2-3"></span>

**Die Idee.** Der Faktor $\mathrm{e}^{-\sigma t}$ wirkt auf beiden Seiten der Zeitachse, aber gegensätzlich. Für $t\to+\infty$ dämpft er umso stärker, je größer $\sigma$ ist. Für $t\to-\infty$ ist $\mathrm{e}^{-\sigma t}=\mathrm{e}^{\sigma|t|}$, dort verstärkt ein großes $\sigma$. Daraus folgen die drei Formen des Konvergenzbereichs:

<ul>

<li>

⁠**rechtsseitiges Signal**, $s(t)=0$ für $t<0$, wachsend höchstens wie $\mathrm{e}^{\alpha t}$: Jedes $\sigma>\alpha$ funktioniert. Konvergenzbereich: die Halbebene *rechts* einer Grenze.

</li>

<li>

⁠**linksseitiges Signal**: Nur die Seite $t\to-\infty$ zählt, kleine $\sigma$ helfen. Konvergenzbereich: eine Halbebene *links* einer Grenze.

</li>

<li>

⁠**zweiseitiges Signal**: Beide Bedingungen müssen gleichzeitig gelten. Konvergenzbereich: ein *Streifen*, der auch leer sein kann.

</li>

</ul>

Warum immer senkrechte Grenzen? Es gilt $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$. Ob $\int|s(t)\mathrm{e}^{-pt}|\mathrm{d} t$ endlich ist, hängt nur von $\sigma$ ab, nie von $f$.

⁠**Kurz gesagt:** Der Konvergenzbereich ist die Menge aller Dämpfungen $\sigma$, mit denen $s(t)\,\mathrm{e}^{-\sigma t}$ absolut integrierbar wird.

:::merke Die Grundpaare (werden im ganzen Kapitel benutzt)
Für eine beliebige komplexe Zahl $p_0$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
<span class="anker" id="gl-2-5"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{alle }p,\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.2|2.3|2.4|2.5}$$

Mit $p_0=0$ folgt aus [(2.2)](#gl-2-2) der Sprung: $\varepsilon(t)\leftrightarrow1/p$ für $\operatorname{Re} p>0$. Die ersten beiden Zeilen haben *denselben* Ausdruck und verschiedene Konvergenzbereiche: Erst beide zusammen legen das Signal fest.
:::

:::herleitung Grundpaare
[(2.2)](#gl-2-2): $\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$. Der Wert an der oberen Grenze verschwindet genau dann, wenn $\operatorname{Re}(p-p_0)>0$.

[(2.3)](#gl-2-3): $-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$. Der Wert bei $t\to-\infty$ verschwindet genau dann, wenn $\operatorname{Re}(p-p_0)<0$.

[(2.4)](#gl-2-4): Siebeigenschaft, $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$.

[(2.5)](#gl-2-5): partielle Integration, $\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$ für $\operatorname{Re} p>0$.
:::

:::frage Warum fallen beim Ausrechnen von $\int_0^\infty\mathrm{e}^{-bt}\mathrm{e}^{-pt}\mathrm{d} t$ die e-Terme weg, und warum kommt $\frac{1}{b+p}$ heraus und nicht $\frac{1}{-(b+p)}$?
Beides liegt am Einsetzen der Grenzen. Die Stammfunktion von $\mathrm{e}^{-(b+p)t}$ ist $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, mit Minus, weil Ableiten den Faktor $-(b+p)$ liefert. Dann rechnet man „obere Grenze minus untere Grenze“:

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

<ul>

<li>

⁠**Obere Grenze:** $|\mathrm{e}^{-(b+p)t}|=\mathrm{e}^{-(\operatorname{Re} b+\sigma)t}$ geht genau dann gegen null, wenn $\operatorname{Re} p>-\operatorname{Re} b$. Diese Bedingung *ist* der Konvergenzbereich. Außerhalb bliebe der e-Term stehen und wüchse über alle Grenzen.

</li>

<li>

⁠**Untere Grenze:** $\mathrm{e}^0=1$, dort bleibt kein e-Term übrig.

</li>

<li>

⁠**Vorzeichen:** Das Minus der Stammfunktion trifft auf das Minus, mit dem die untere Grenze abgezogen wird. Minus mal Minus ergibt Plus.

</li>

</ul>

Beim linksseitigen Impuls $\mathrm{e}^{-bt}\varepsilon(-t)$ ist es umgekehrt. Integriert wird von $-\infty$ bis $0$, jetzt ist $t=0$ die *obere* Grenze. Ihr Beitrag $-\frac{1}{b+p}$ wird nicht abgezogen, das Minus bleibt stehen. Die untere Grenze $t\to-\infty$ verschwindet nur für $\operatorname{Re}(b+p)<0$, deshalb liegt dieser Konvergenzbereich links. Mit $p_0=-b$ sind das die Grundpaare [(2.2)](#gl-2-2) und [(2.3)](#gl-2-3).
:::

:::frage Betrachtet man die Realteile von $b$ und $p$, weil das Abklingen des Integranden über die Integrierbarkeit entscheidet? Für manche $b$ klingt das Signal ab, für andere wächst es, sinkt nicht auf null, und das Integral konvergiert nicht, weil immer noch etwas dazukommt.
Ja, genau so. Der Betrag des Integranden ist

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\underbrace{\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|}_{=\,1}.$$

Der Imaginärteil lässt den Integranden nur in der komplexen Ebene kreisen, am Betrag ändert er nichts. Über Wachsen oder Abklingen entscheidet allein der Realteil. Drei Präzisierungen:

<ul>

<li>

Es zählt die *Summe* $\operatorname{Re} b+\sigma$. Das Signal darf selbst wachsen ($\operatorname{Re} b<0$), solange die Dämpfung $\sigma$ stärker ist. Das ist der Trick „dämpfen“ aus Abschnitt 2.2.

</li>

<li>

„Geht gegen null“ allein reicht nicht. Auch $1/t$ geht gegen null, aber $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$, weil die Beiträge zu langsam kleiner werden. Exponentielles Abklingen ist schnell genug: $\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ ist endlich.

</li>

<li>

Auf der Grenze $\operatorname{Re}(b+p)=0$ hat der Integrand den konstanten Betrag 1 und kreist nur. Das Integral pendelt dann, statt sich einem Wert zu nähern, und genau im Pol wächst es sogar linear (Aufgabe [3a](#aufg-3a)). Deshalb gehört die Grenzlinie nicht zum Konvergenzbereich.

</li>

</ul>
:::

:::frage Gilt das also für jede beliebige Funktion?
Nein, nur für Funktionen mit nicht leerem Konvergenzbereich. Drei Gegenbeispiele:

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ wächst schneller als jede Exponentialfunktion. $\mathrm{e}^{t^2-\sigma t}\to\infty$ für jedes $\sigma$, keine Dämpfung reicht.

</li>

<li>

$\mathrm{e}^{|t|}$: Die rechte Hälfte verlangt $\sigma>1$, die linke $\sigma<-1$. Beides zugleich geht nicht.

</li>

<li>

Selbst die Konstante $s(t)=1$ für alle $t$: rechts $\sigma>0$, links $\sigma<0$. Die Fourier-Transformation erfasst solche Signale trotzdem, mit einem Dirac-Impuls im Spektrum.

</li>

</ul>

Für rechtsseitige Signale mit höchstens exponentiellem Wachstum klappt es immer. Dazu gehört jedes Signal, das in einer Schaltung bei $t=0$ eingeschaltet wird.
:::

:::frage Warum reicht eine einzige Linie, wenn die $p$-Ebene zweidimensional ist?
Jede Linie im Konvergenzbereich liefert dasselbe $s(t)$: Bei größerem $\sigma$ dämpft man in Schritt 1 stärker und multipliziert in Schritt 3 stärker zurück, beides hebt sich auf. Numerisch bestätigt: Mit $\sigma=0{,}2$ und $\sigma=1/\mathrm s$ ergibt sich für den Sprung beide Male $s(1\,\mathrm{s})\approx1{,}00$ und $s(-1\,\mathrm{s})\approx0{,}00$. Die Ebene enthält also mehr, als man für die Überlagerung braucht. Ihr Nutzen liegt woanders: In der Ebene lässt sich $S(p)$ durch wenige Zahlen beschreiben, die Pole und Nullstellen. (Zusatz: $S(p)$ ist im Konvergenzbereich komplex differenzierbar, deshalb legen die Werte auf einer Linie die Funktion im ganzen Bereich fest.)
:::

:::aufgabe Aufgabe 2 ★ Laplace ist Fourier eines gedämpften Signals
<span class="anker" id="aufg-2"></span>

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

:::aufgabe Aufgabe 3 ★★ Ein wachsendes Signal
<span class="anker" id="aufg-3"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$, zum Beispiel die Impulsantwort eines instabilen Systems ($t$ in s).

<ol class="al">

<li>

Warum gibt es keine Fourier-Transformierte im klassischen Sinn?

</li>

<li>

Für welche $\sigma$ ist $s(t)\,\mathrm{e}^{-\sigma t}$ absolut integrierbar?

</li>

<li>

Berechne $S(p)$ direkt aus dem Integral. Zeichne Pol und Konvergenzbereich in die $p$-Ebene.

</li>

<li>

Welche $\sigma$ darfst du in der Umkehrformel benutzen? Der Ausdruck $S(\mathrm{j}2\pi f)$ ist endlich. Warum darfst du trotzdem nicht $\sigma=0$ wählen, und welches Signal käme mit $\sigma=0$ heraus? (Tipp: [(2.3)](#gl-2-3).)

</li>

</ol>

:::loesung
(a) $\int_0^\infty\mathrm{e}^{2t}\mathrm{d} t=\infty$: Das Signal ist nicht absolut integrierbar. Anschaulich: Aus Schwingungen konstanter Amplitude lässt sich nichts Wachsendes zusammensetzen.

(b) $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$ für $t>0$, integrierbar genau für $\sigma>2/\mathrm s$.

(c) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$ für $\operatorname{Re} p>2$. Pol bei $p=2$, Konvergenzbereich rechts davon, wie bei jedem rechtsseitigen Signal. Numerische Kontrolle: $S(3)=1$, $S(2{,}5+\mathrm{j})=0{,}4-0{,}8\mathrm{j}$.

(d) Jedes $\sigma>2/\mathrm s$, zum Beispiel $\sigma=3/\mathrm s$. $\sigma=0$ liegt links vom Pol, also außerhalb des Konvergenzbereichs. Der Ausdruck $1/(\mathrm{j}2\pi f-2)$ ist zwar endlich, er gehört aber zu einem *anderen* Signal: Nach [(2.3)](#gl-2-3) hat auch $-\mathrm{e}^{2t}\varepsilon(-t)$ die Transformierte $1/(p-2)$, mit Konvergenzbereich $\operatorname{Re} p<2$. Mit $\sigma=0$ käme dieses linksseitige, abklingende Signal heraus. Das ist das Signal, dessen Fourier-Transformierte $1/(\mathrm{j}2\pi f-2)$ tatsächlich ist.
:::
:::

:::aufgabe Aufgabe 3a ★★ Was auf der Grenze passiert
<span class="anker" id="aufg-3a"></span>

$s(t)=\mathrm{e}^{(1+3\mathrm{j})t}\varepsilon(t)$, also $b=-1-3\mathrm{j}$ ($t$ in s).

<ol class="al">

<li>

Für welche $\sigma$ konvergiert $\int_0^\infty s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$? Welche Rolle spielt die 3?

</li>

<li>

Setze $p=1+\mathrm{j}\omega$, also genau auf die Grenze, und berechne $\int_0^T s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. Was passiert für $T\to\infty$? Unterscheide $\omega\neq3$ und $\omega=3$. Wo liegt der Pol?

</li>

</ol>

:::loesung
(a) $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$ mit $p=\sigma+\mathrm{j}\omega$. Der Betrag des Integranden ist $\mathrm{e}^{-(\sigma-1)t}$, das Integral konvergiert genau für $\sigma>1$. Die 3 (die Kreisfrequenz des Signals) taucht im Betrag nicht auf. Sie bestimmt nur, wo auf der Grenzlinie der Pol sitzt: $S(p)=\frac{1}{p-(1+3\mathrm{j})}$, Pol bei $p=1+3\mathrm{j}$.

(b) Mit $p=1+\mathrm{j}\omega$ ist $b+p=\mathrm{j}(\omega-3)$.

<ul>

<li>

$\omega\neq3$: $\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$. Der Zähler kreist für wachsendes $T$ auf einem Kreis um 1 und nähert sich keinem Wert. Das Integral bleibt beschränkt, hat aber keinen Grenzwert.

</li>

<li>

$\omega=3$, also genau im Pol $p=1+3\mathrm{j}$: Der Integrand ist konstant 1, das Integral ist $T$ und wächst über alle Grenzen.

</li>

</ul>

Auf der Grenzlinie konvergiert das Integral also nirgends. Der Konvergenzbereich ist die offene Halbebene $\operatorname{Re} p>1$.
:::
:::

:::aufgabe Aufgabe 4 ★ Richtig oder falsch? Mit Begründung
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Jede Funktion hat eine Laplace-Transformierte.

</li>

<li>

Ob $p$ im Konvergenzbereich liegt, hängt nur von $\operatorname{Re} p$ ab.

</li>

<li>

Liegt die imaginäre Achse im Konvergenzbereich, ist $S(\mathrm{j}2\pi f)$ die Fourier-Transformierte von $s(t)$.

</li>

<li>

In der Umkehrformel liefert $\sigma=1/\mathrm s$ ein anderes Signal als $\sigma=2/\mathrm s$, wenn beide im Konvergenzbereich liegen.

</li>

<li>

$\cos(2\pi f_0t)$ ist eine Eigenfunktion jedes LTI-Systems.

</li>

</ol>

:::loesung
(a) Falsch. Gegenbeispiele: $\mathrm{e}^{t^2}\varepsilon(t)$, $\mathrm{e}^{|t|}$, die zweiseitige Konstante.

(b) Richtig. $|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$, die Frequenz $f$ kommt im Betrag nicht vor. Deshalb besteht der Konvergenzbereich aus ganzen senkrechten Linien.

(c) Richtig. Mit $\sigma=0$ ist $S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$.

(d) Falsch. Jede Linie im Konvergenzbereich liefert dasselbe Signal, weil die Dämpfung $\mathrm{e}^{-\sigma t}$ und das Zurückmultiplizieren mit $\mathrm{e}^{\sigma t}$ sich aufheben.

(e) Falsch. Der Ausgang ist $|H|\cos(2\pi f_0t+\varphi)$ mit $H=H(\mathrm{j}2\pi f_0)$. Er ist nur dann ein Vielfaches von $\cos(2\pi f_0t)$, wenn $\varphi=0$ oder $\varphi=\pi$ ist, wenn also $H(\mathrm{j}2\pi f_0)$ reell ist. Für den RC-Tiefpass ist das bei keiner Frequenz $f_0>0$ der Fall.
:::
:::
