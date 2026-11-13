---
title: Stufe 2: Ähnlichkeit messen, der Korrelationskoeffizient
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260300
summary: Wie misst man mit einer Zahl, wie ähnlich zwei Signale sind?
tags: Korrelationskoeffizienten, orthogonal
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Wie misst man mit einer Zahl, wie ähnlich zwei Signale sind? Man misst, wie groß ihre Differenz ist.
:::

**Die Idee.** Die Energie der Differenz $\Delta(t)=s(t)-g(t)$ ist klein, wenn die Signale ähnlich sind. Ausmultipliziert:

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

Der Unterschied steckt also allein im Integral des Produkts. Damit die Größe der Signale nicht mitzählt, normiert man beide auf die Energie 1. Dann ist $E_\Delta=2-2\operatorname{Re}\,p_{sg}$ mit dem __Korrelationskoeffizienten__

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**So liest man das:** $|p_{sg}|\le1$ (Cauchy-Schwarz-Ungleichung). $p=1$ heißt $s=a\,g$ mit $a>0$: gleiche Form. $p=-1$ heißt $s=-a\,g$: gleiche Form, umgekehrtes Vorzeichen. $p=0$ heißt $\int s^*g\,\mathrm{d} t=0$, die Signale sind __orthogonal__, wie die Harmonischen einer Fourier-Reihe in [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html). Beispiel: $\operatorname{rect}(t)$ und $\Lambda(t)$ haben $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0{,}75$, $E_{\operatorname{rect}}=1$, $E_\Lambda=\frac23$, also $p=0{,}919$.

:::aufgabe Aufgabe 2 ★★ Korrelationskoeffizienten
<span class="anker" id="aufg-2"></span>

Berechne $p$ für (a) $\operatorname{rect}(t)$ und $\operatorname{rect}(t-0{,}5)$, (b) $\operatorname{rect}(t)$ und $\Lambda(t)$ (Ergebnis oben), (c) $\operatorname{rect}(t)$ und $\operatorname{sgn}(t)\operatorname{rect}(t)$.

:::loesung
(a) Die Rechtecke überlappen auf der Länge 0,5, also $\int=0{,}5$, beide Energien 1: $p=0{,}5$. (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0{,}75$, $E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$: $p=\frac{0{,}75}{\sqrt{2/3}}=0{,}919$. Sehr ähnliche Formen. (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$: $p=0$, die Signale sind orthogonal, obwohl sie auf der rechten Hälfte gleich sind.
:::
:::

::::formelsammlung
**Energie der Differenz**

$$E_\Delta=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t$$

Energie von $\Delta(t)=s(t)-g(t)$. Der Unterschied zweier Signale steckt allein im Integral ihres Produkts.

**Korrelationskoeffizient**

$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}$$

Ähnlichkeit der Formen, unabhängig von der Größe der Signale: Sind beide auf die Energie 1 normiert, ist $E_\Delta=2-2\operatorname{Re}\,p_{sg}$.

**Grenzen des Korrelationskoeffizienten**

$$|p_{sg}|\le1$$

Cauchy-Schwarz-Ungleichung. $p=1$: $s=a\,g$ mit $a>0$, gleiche Form; $p=-1$: $s=-a\,g$, gleiche Form mit umgekehrtem Vorzeichen; $p=0$: $\int s^*g\,\mathrm{d} t=0$, die Signale sind orthogonal.
::::

::::lernkarten
:::karte formel Energie der Differenz
Wie hängt die Energie der Differenz $\Delta(t)=s(t)-g(t)$ zweier Signale mit ihren Energien und dem Integral ihres Produkts zusammen?
---
$E_\Delta=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t$. Die Energien allein sagen nichts über die Ähnlichkeit; der Unterschied steckt allein im Integral des Produkts.
--- falsch
$E_\Delta=E_s-E_g$: Die Energie der Differenz ist die Differenz der Energien; zwei Signale sind ähnlich, wenn ihre Energien fast gleich groß sind.
--- falsch
$E_\Delta=E_s+E_g$: Die Energien zweier Signale addieren sich immer, auch bei der Differenz, weil das Betragsquadrat das Vorzeichen von $g$ beseitigt.
--- falsch
$E_\Delta=E_s+E_g+2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t$. Je größer das Integral des Produkts, desto größer die Energie der Differenz, denn ähnliche Signale verstärken einander.
:::
:::karte begriff Korrelationskoeffizient
Was misst der Korrelationskoeffizient $p_{sg}$ zweier Energiesignale, und wie ist er definiert?
---
Eine Zahl für die Ähnlichkeit der Formen, unabhängig von der Größe der Signale: $p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}$, das Integral des Produkts nach Normierung auf die Energie 1.
--- falsch
Die Energie der Differenz der beiden Signale: $p_{sg}=\int|s(t)-g(t)|^2\,\mathrm{d} t$. Ein großer Wert bedeutet, dass die Signale einander sehr ähnlich sind, ein kleiner, dass sie sich deutlich unterscheiden.
--- falsch
Das Verhältnis der Energien: $p_{sg}=E_s/E_g$. Bei $p_{sg}=1$ sind beide Signale gleich groß und deshalb auch gleich geformt.
--- falsch
Die Ähnlichkeit, gemessen mit dem nicht normierten Integral $p_{sg}=\int s^*(t)\,g(t)\,\mathrm{d} t$; die Größe der Signale zählt dabei bewusst mit, weil größere Signale einander ähnlicher sind.
:::
:::karte zusammenhang Normierung auf die Energie 1
Warum normiert man beide Signale auf die Energie 1, bevor man ihre Ähnlichkeit am Integral des Produkts abliest?
---
Damit die Größe der Signale nicht mitzählt. Nach der Normierung ist $E_\Delta=2-2\operatorname{Re}\,p_{sg}$, die Differenz hängt also nur noch von $p_{sg}$ ab: Je größer $\operatorname{Re}\,p_{sg}$, desto ähnlicher die Formen.
--- falsch
Weil nur Signale mit der Energie 1 ein endliches Produktintegral haben. Ohne Normierung wäre das Integral des Produkts für jedes Paar von Energiesignalen unendlich.
--- falsch
Damit die Energie der Differenz immer null wird. Nach der Normierung ist $E_\Delta=0$, und man liest die Ähnlichkeit nur noch an der Phase des Produkts ab.
--- falsch
Damit $p_{sg}$ unabhängig von einer Verschiebung wird. Nach der Normierung ist $E_\Delta=2+2\operatorname{Re}\,p_{sg}$: Je größer $p_{sg}$, desto ähnlicher die beiden Formen.
:::
:::karte zusammenhang Grenzen des Korrelationskoeffizienten
Was bedeuten die Werte $p_{sg}=1$ und $p_{sg}=-1$ des Korrelationskoeffizienten, und warum kann $|p_{sg}|$ nicht größer als 1 werden?
---
$p=1$ heißt $s=a\,g$ mit $a>0$, gleiche Form; $p=-1$ heißt $s=-a\,g$, gleiche Form mit umgekehrtem Vorzeichen. Nach der Cauchy-Schwarz-Ungleichung gilt stets $|p_{sg}|\le1$.
--- falsch
$p=1$ heißt $s=g$, die Signale sind auch gleich groß; $p=-1$ heißt, sie haben nichts gemeinsam. $|p_{sg}|\le1$ gilt, weil beide Energien höchstens 1 sein dürfen.
--- falsch
$p=1$ heißt gleiche Form, $p=-1$ heißt gleiche Energie bei verschiedener Form. $|p_{sg}|\le1$ folgt daraus, dass das Integral des Produkts nie negativ ist.
--- falsch
$p=1$ heißt $s=a\,g$ mit $a>0$, gleiche Form; $p=-1$ heißt, die Signale sind orthogonal. Nach der Cauchy-Schwarz-Ungleichung gilt stets $|p_{sg}|\le1$.
:::
:::karte zusammenhang Orthogonale Signale
Was bedeutet es, wenn der Korrelationskoeffizient zweier Signale null ist, und welches bekannte Beispiel gibt es dafür?
---
Dann ist $\int s^*g\,\mathrm{d} t=0$, die Signale sind orthogonal: Ihre Differenz hat die Energie $E_s+E_g$, als hätten sie nichts gemeinsam. Beispiele sind die Harmonischen einer Fourier-Reihe.
--- falsch
Dann sind die Signale gleich, nur verschieden groß: Ihre Differenz hat die Energie null. Ein Beispiel sind ein Rechteck und dasselbe Rechteck mit halber Höhe.
--- falsch
Dann hat eines der beiden Signale die Energie null, denn nur so kann das Integral des Produkts verschwinden. Ein Beispiel sind ein beliebiges Signal und die Nullfunktion.
--- falsch
Dann haben die Signale entgegengesetzte Form, $s=-a\,g$: Ihre Differenz hat die größtmögliche Energie. Ein Beispiel sind ein Kosinus und der um eine halbe Periode verschobene Kosinus.
:::
:::karte zusammenhang Orthogonal trotz gleicher Hälfte
Warum sind $\operatorname{rect}(t)$ und $\operatorname{sgn}(t)\operatorname{rect}(t)$ orthogonal, obwohl sie auf der rechten Hälfte übereinstimmen?
---
Weil das Integral des Produkts $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$ ist: Die Übereinstimmung rechts liefert $+\frac12$, die entgegengesetzten Vorzeichen links liefern $-\frac12$. Damit ist $p=0$.
--- falsch
Weil sie sich auf der linken Hälfte unterscheiden und der Korrelationskoeffizient nur die schlechter passende Hälfte bewertet; die Übereinstimmung rechts zählt deshalb nicht.
--- falsch
Weil $\operatorname{sgn}(t)\operatorname{rect}(t)$ die Energie null hat: Positive und negative Hälfte heben sich auf, und ein Signal ohne Energie ist zu jedem anderen Signal orthogonal.
--- falsch
Weil die beiden Signale verschieden große Sprünge haben: $\operatorname{sgn}(t)\operatorname{rect}(t)$ springt bei $t=0$ von $-1$ auf $+1$, und dieser Sprung allein macht den Korrelationskoeffizienten zu null.
:::
:::karte zusammenhang Verschobene Rechtecke
Was ergibt der Korrelationskoeffizient, wenn man $\operatorname{rect}(t)$ mit dem verschobenen Rechteck $\operatorname{rect}(t-0{,}5)$ vergleicht?
---
$p=0{,}5$: Die Rechtecke überlappen auf der Länge 0,5, also ist das Integral des Produkts 0,5, und beide Energien sind 1. Die Verschiebung allein senkt die Ähnlichkeit.
--- falsch
$p=0$: Die Rechtecke sind gegeneinander verschoben, und verschobene Signale sind stets orthogonal, weil ihr Produkt an keiner Stelle von null verschieden ist.
--- falsch
$p=1$: Beide haben dieselbe Form und dieselbe Energie 1; eine Verschiebung ändert den Korrelationskoeffizienten nicht, denn er vergleicht nur die Formen der Signale.
--- falsch
$p=0{,}25$: Das Integral des Produkts ist 0,5, und man teilt durch $E_s+E_g=2$, damit der Wert stets zwischen 0 und 1 bleibt.
:::
:::karte formel Rechteck und Dreieck
Wie groß ist der Korrelationskoeffizient von Rechteck $\operatorname{rect}(t)$ und Dreieck $\Lambda(t)$, und woraus setzt er sich zusammen?
---
$p=0{,}919$: Das Integral des Produkts ist $0{,}75$, die Energien sind $E_{\operatorname{rect}}=1$ und $E_\Lambda=\frac23$, also $p=\frac{0{,}75}{\sqrt{2/3}}$. Die Formen sind sehr ähnlich.
--- falsch
$p=0{,}75$: Das ist das Integral des Produkts; eine Division ist nicht nötig, weil das Rechteck die Energie 1 hat und das Dreieck dieselbe Höhe 1.
--- falsch
$p=1{,}125$: Das Integral des Produkts $0{,}75$ geteilt durch $E_\Lambda=\frac23$; der Wert über 1 zeigt, dass das Dreieck ganz im Rechteck liegt.
--- falsch
$p=0{,}5$: Das Dreieck hat nur die halbe Fläche des Rechtecks, und der Korrelationskoeffizient ist das Verhältnis der Flächen der beiden Signale.
:::
::::
