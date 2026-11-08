---
title: Kreuzentropie und KL-Divergenz
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
knoten: Grundlagen 5: Statistik und Information
nachschlagen: ja
order: 15251000
summary: Wer eine Quelle mit einem Code verschlüsselt, der für eine andere Verteilung gebaut wurde, braucht im Mittel mehr Binärziffern.
tags: Kreuzentropie, KL-Divergenz, relative Entropie
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Wer eine Quelle mit einem Code verschlüsselt, der für eine andere Verteilung gebaut wurde, braucht im Mittel mehr Binärziffern. Dieser Abschnitt misst diesen Mehraufwand, beweist, dass er nie negativ ist, und zeigt, warum er trotzdem kein Abstand zwischen zwei Verteilungen ist.
:::

### Die Kreuzentropie

<span class="anker" id="stufe-9-1"></span>

Nach dem Quellencodierungssatz gibt ein guter Code dem Zeichen $k$ die Länge $\log_2(1/p_k)$. Dafür muss man die Verteilung $\mathbf{p}$ der Quelle kennen. Wer sie falsch einschätzt und mit einer anderen Verteilung $\mathbf{q}$ rechnet, gibt dem Zeichen $k$ die Länge $\log_2(1/q_k)$. Gesendet wird aber mit den wahren Häufigkeiten $p_k$, und die mittlere Länge ist dann $\sum_kp_k\log_2(1/q_k)$.

:::definition Definition 9.1 (Kreuzentropie)
<span class="anker" id="satz-9-1"></span>

Für zwei Verteilungen $\mathbf{p}$ und $\mathbf{q}$ auf denselben $K$ Ergebnissen heißt

<span class="anker" id="gl-9-1"></span>
$$H(\mathbf{p},\mathbf{q})=\sum_{k=1}^Kp_k\log_2\frac1{q_k}\quad\text{bit} \tag{9.1}$$

die __Kreuzentropie__ von $\mathbf{q}$ bezüglich $\mathbf{p}$. Summanden mit $p_k=0$ lässt man weg; ist $q_k=0$ für ein $k$ mit $p_k>0$, so ist $H(\mathbf{p},\mathbf{q})$ unendlich. Mit $\ln$ statt $\log_2$ misst man sie in nat.
:::

An erster Stelle steht die Verteilung, mit der tatsächlich gemittelt wird, an zweiter die, mit der man rechnet. In der Sprache der Überraschung ist die Kreuzentropie die mittlere Überraschung, wenn die Wirklichkeit nach $\mathbf{p}$ verteilt ist, man aber $\mathbf{q}$ erwartet. Für $\mathbf{q}=\mathbf{p}$ ist sie die Entropie: $H(\mathbf{p},\mathbf{p})=H(\mathbf{p})$. Ein Ergebnis, das man für unmöglich hält und das trotzdem eintritt, überrascht unendlich; dafür gibt es kein Codewort.

⁠**Rechenbeispiel:** Die Quelle aus Unterabschnitt [8.3](informationsgehalt-und-entropie.html#stufe-8-3) hat $\mathbf{p}=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)^{\top}$. Wer sie mit $\mathbf{q}=(\tfrac18,\tfrac18,\tfrac14,\tfrac12)^{\top}$ beschreibt, baut den Code A $=110$, B $=111$, C $=10$, D $=0$ mit den Längen $\mathbf l'=(3,\,3,\,2,\,1)^{\top}$. Seine mittlere Länge ist $H(\mathbf{p},\mathbf{q})=\tfrac{21}8=2{,}625$ bit je Zeichen (Abb. [17](#abb-17)), mehr als die $2$ bit des Codes mit gleich langen Codewörtern und deutlich mehr als die Entropie $1{,}75$ bit.

:::abbildung ml/k5rkreuz 17
Die Kreuzentropie als mittlere Länge des Codes, der für $\mathbf{q}=(\tfrac18,\tfrac18,\tfrac14,\tfrac12)^{\top}$ gebaut ist, wenn die Zeichen tatsächlich mit $\mathbf{p}=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)^{\top}$ kommen.
:::

⁠**Kurz gesagt:** Die Kreuzentropie $H(\mathbf{p},\mathbf{q})=\sum_kp_k\log_2(1/q_k)$ ist die mittlere Codelänge, wenn man mit $\mathbf{q}$ rechnet, die Wirklichkeit aber $\mathbf{p}$ ist.

### Die KL-Divergenz

<span class="anker" id="stufe-9-2"></span>

Mit der richtigen Verteilung käme man im Mittel mit $H(\mathbf{p})$ Binärziffern aus, mit der falschen braucht man $H(\mathbf{p},\mathbf{q})$. Der Unterschied ist der Preis des Irrtums.

:::definition Definition 9.2 (KL-Divergenz)
<span class="anker" id="satz-9-2"></span>

Die __KL-Divergenz__ von $\mathbf{q}$ zu $\mathbf{p}$ ist

<span class="anker" id="gl-9-2"></span>
$$D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})=\sum_{k=1}^Kp_k\log_2\frac{p_k}{q_k}=H(\mathbf{p},\mathbf{q})-H(\mathbf{p})\quad\text{bit}. \tag{9.2}$$

Summanden mit $p_k=0$ lässt man weg; ist $q_k=0$ für ein $k$ mit $p_k>0$, so ist sie unendlich. Mit $\ln$ statt $\log_2$ misst man sie in nat.
:::

Die zweite Form folgt aus $\log_2\frac{p_k}{q_k}=\log_2\frac1{q_k}-\log_2\frac1{p_k}$. Die Buchstaben KL stehen für Solomon Kullback und Richard Leibler, die den Begriff 1951 einführten; ein anderer Name ist __relative Entropie__. Die Reihenfolge der beiden Verteilungen ist wichtig: Gemittelt wird mit der ersten.

⁠**Rechenbeispiel:** Für $\mathbf{p}$ und $\mathbf{q}$ aus dem vorigen Unterabschnitt ist $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})=2{,}625-1{,}75=0{,}875$ bit. Direkt nach [(9.2)](#gl-9-2) ergibt sich dasselbe (Abb. [18](#abb-18)). Zwei der vier Summanden sind negativ, denn bei C und D ist $q_k>p_k$. Abb. [19](#abb-19) zeigt die Beiträge: Die positiven überwiegen.

:::abbildung ml/k5rkl 18
Die KL-Divergenz als Summe der Beiträge $p_k\log_2(p_k/q_k)$. Wo $\mathbf{q}$ einem Zeichen mehr Wahrscheinlichkeit gibt als $\mathbf{p}$, ist der Beitrag negativ.
:::

:::abbildung ml/k5kl 19
(a) Die wahre Verteilung $\mathbf{p}$ (blau) und die angenommene Verteilung $\mathbf{q}$ (rot). (b) Die Beiträge der vier Zeichen zur KL-Divergenz. Die Summe ist $1+\tfrac14-\tfrac18-\tfrac14=\tfrac78$ bit, also positiv, obwohl zwei Beiträge negativ sind.
:::

⁠**Kurz gesagt:** Die KL-Divergenz $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})=H(\mathbf{p},\mathbf{q})-H(\mathbf{p})$ ist der Mehraufwand, den man zahlt, wenn man mit $\mathbf{q}$ statt mit der wahren Verteilung $\mathbf{p}$ rechnet.

:::hintergrund Kreuzentropie und KL-Divergenz als Codelängen
Die Deutung als Codelänge ist mehr als ein Bild. Für einen Code, der für $\mathbf{q}$ gebaut ist, mit den aufgerundeten Längen $\lceil\log_2(1/q_k)\rceil$, liegt die mittlere Länge bei den wahren Häufigkeiten $\mathbf{p}$ zwischen $H(\mathbf{p})+D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})$ und dieser Zahl plus eins. Wer glaubt, die Quelle sei nach $\mathbf{q}$ verteilt, während sie nach $\mathbf{p}$ verteilt ist, zahlt also im Mittel $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})$ Binärziffern je Zeichen mehr als nötig. Im Beispiel sind das $0{,}875$ bit je Zeichen, $50\,\%$ mehr als die Entropie. Dieselbe Rechnung gilt für Überraschungen statt Codelängen: $H(\mathbf{p},\mathbf{q})$ ist die mittlere Überraschung dessen, der $\mathbf{q}$ erwartet, $H(\mathbf{p})$ die unvermeidliche Überraschung dessen, der die Wahrheit kennt, und $D_{\mathrm{KL}}$ die zusätzliche Überraschung durch die falsche Erwartung.
:::

### Was du dafür brauchst: Die Ungleichung $\ln x\le x-1$

<span class="anker" id="stufe-9-3"></span>

Dass der Mehraufwand nie negativ ist, folgt aus einer einzigen Ungleichung. Sie stand schon als Rechenbeispiel in Unterabschnitt [5.1](die-maximum-likelihood-schatzung.html#stufe-5-1): Für alle $x>0$ ist $\ln x\le x-1$, mit Gleichheit nur bei $x=1$ [(5.1)](die-maximum-likelihood-schatzung.html#gl-5-1).

Abb. [20](#abb-20) zeigt, was sie bedeutet. Die Gerade $y=x-1$ ist die Tangente an $\ln x$ an der Stelle $x=1$, denn dort hat $\ln$ den Wert $0$ und die Steigung $1/x=1$. Die zweite Ableitung von $\ln x$ ist $-1/x^2<0$; nach [Grundlagen 3, Abschnitt 1.5](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-ableitung.html#stufe-1-5), biegt sich der Graph deshalb überall nach unten von seinen Tangenten weg. Er liegt also ganz unter der Tangente und berührt sie nur bei $x=1$.

:::abbildung ml/k5lnx 20
Der natürliche Logarithmus liegt überall unter seiner Tangente $y=x-1$ an der Stelle $x=1$ und berührt sie nur dort.
:::

⁠**Rechenbeispiel:** Bei $x=2$ ist $\ln2\approx0{,}693\le1$, bei $x=0{,}5$ ist $\ln0{,}5\approx-0{,}693\le-0{,}5$, und nahe bei $1$ ist die Ungleichung fast eine Gleichung: $\ln1{,}1\approx0{,}0953\le0{,}1$.

⁠**Kurz gesagt:** Der Logarithmus liegt unter seiner Tangente an der Stelle $1$: $\ln x\le x-1$, mit Gleichheit nur für $x=1$.

### Die Gibbs-Ungleichung

<span class="anker" id="stufe-9-4"></span>

Kann eine falsche Annahme den Code verkürzen? Nein: Die richtige Verteilung ist immer die beste.

:::satz Satz 9.3 (Gibbs-Ungleichung)
<span class="anker" id="satz-9-3"></span>

Für zwei Verteilungen $\mathbf{p}$ und $\mathbf{q}$ auf denselben Ergebnissen ist

<span class="anker" id="gl-9-3"></span>
$$D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})\ge0 , \tag{9.3}$$

und Gleichheit gilt genau dann, wenn $\mathbf{q}=\mathbf{p}$ ist. Gleichwertig: $H(\mathbf{p},\mathbf{q})\ge H(\mathbf{p})$.
:::

:::beweis Gibbs-Ungleichung
Man rechnet in nat; in bit unterscheidet sich die KL-Divergenz nach [(4.2)](die-likelihood.html#gl-4-2) nur um den positiven Faktor $1/\ln2$. Ist $q_k=0$ für ein $k$ mit $p_k>0$, so ist die Divergenz unendlich, also nicht negativ. Sonst summiert man über die Menge $A$ der $k$ mit $p_k>0$ und benutzt $\ln x\le x-1$ mit $x=q_k/p_k$:

$$-D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})=\sum_{k\in A}p_k\ln\frac{q_k}{p_k}\le\sum_{k\in A}p_k\Bigl(\frac{q_k}{p_k}-1\Bigr)=\sum_{k\in A}q_k-\sum_{k\in A}p_k=\sum_{k\in A}q_k-1\le0 .$$

Gleichheit verlangt in jedem Summanden $\ln x=x-1$, also $q_k=p_k$ für alle $k\in A$, und außerdem $\sum_{k\in A}q_k=1$. Dann ist $q_k=0$ für alle $k$ außerhalb von $A$, und $\mathbf{q}=\mathbf{p}$.
:::

Der Beweis zeigt, woher die Ungleichung kommt: Sie ist die Ungleichung $\ln x\le x-1$, gemittelt mit den Gewichten $p_k$. Die Summe $\sum_kp_k\,(q_k/p_k)$ ist immer höchstens $1$, weil $\mathbf{q}$ eine Verteilung ist, und deshalb kann der Logarithmus nicht im Mittel positiv sein.

Jetzt lässt sich die untere Schranke des Quellencodierungssatzes aus Unterabschnitt [8.3](informationsgehalt-und-entropie.html#stufe-8-3) beweisen. Ein Präfixcode habe die Längen $l_k$, und $z=\sum_k2^{-l_k}$ sei nach der Kraft-Ungleichung höchstens $1$. Dann ist $q_k=2^{-l_k}/z$ eine Verteilung, und $l_k=\log_2(1/q_k)+\log_2(1/z)$. Also ist

$$L=\sum_kp_k\,l_k=H(\mathbf{p},\mathbf{q})+\log_2\frac1z\ge H(\mathbf{p},\mathbf{q})\ge H(\mathbf{p}) ,$$

mit Gleichheit genau dann, wenn $z=1$ und $\mathbf{q}=\mathbf{p}$ ist, also $2^{-l_k}=p_k$ für alle $k$.

⁠**Rechenbeispiel:** Für die Verteilungen $\mathbf{p}=(0{,}5;\ 0{,}3;\ 0{,}2)^{\top}$ und $\mathbf{q}=(0{,}5;\ 0{,}2;\ 0{,}3)^{\top}$ ist $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})=0+0{,}3\log_21{,}5+0{,}2\log_2\tfrac23\approx0{,}175-0{,}117=0{,}058$ bit. Die Vertauschung zweier Wahrscheinlichkeiten kostet also etwas, wenn auch wenig. Im Beispiel des vorigen Unterabschnitts war es viel mehr, $0{,}875$ bit.

⁠**Kurz gesagt:** Die KL-Divergenz ist nie negativ und nur für gleiche Verteilungen null; deshalb ist kein Code kürzer als die Entropie und keine falsche Erwartung im Mittel weniger überraschend als die richtige.

:::hintergrund Herkunft und andere Beweise
Die Ungleichung trägt den Namen des amerikanischen Physikers Josiah Willard Gibbs, der sie in der statistischen Mechanik benutzte. In der Informationstheorie gilt sie als eine der wichtigsten Ungleichungen überhaupt, weil fast jede Schranke, die dort bewiesen wird, auf sie zurückgeht. Viele Bücher beweisen sie mit einer allgemeineren Ungleichung, der Jensen-Ungleichung; der Weg über $\ln x\le x-1$ braucht nur die Tangente an den Logarithmus und kommt ohne sie aus.
:::

### Die KL-Divergenz ist kein Abstand

<span class="anker" id="stufe-9-5"></span>

Die KL-Divergenz ist nie negativ und nur für gleiche Verteilungen null, so wie ein Abstand. Zwei andere Eigenschaften eines Abstands aus [Grundlagen 1, Abschnitt 4.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-1), hat sie aber nicht: Sie ist nicht symmetrisch, und die Dreiecksungleichung gilt nicht. Die Rechenbeispiele dieses Unterabschnitts sind in nat angegeben, wie alle KL-Divergenzen von hier an.

⁠**Rechenbeispiel:** Für $\mathbf{p}=(0{,}5;\ 0{,}5)^{\top}$ und $\mathbf{r}=(0{,}9;\ 0{,}1)^{\top}$ ist

$$D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{r})=0{,}5\ln\frac{0{,}5}{0{,}9}+0{,}5\ln\frac{0{,}5}{0{,}1}\approx0{,}511,\qquad D_{\mathrm{KL}}(\mathbf{r}\,\|\,\mathbf{p})=0{,}9\ln\frac{0{,}9}{0{,}5}+0{,}1\ln\frac{0{,}1}{0{,}5}\approx0{,}368 .$$

Die beiden Richtungen sind verschieden. Der Grund ist anschaulich: Wer eine faire Münze für eine Münze mit $\mathbf{r}$ hält, wird von der Hälfte der Würfe stark überrascht, denn er erwartet Zahl nur in einem von zehn Fällen. Wer umgekehrt die Münze mit $\mathbf{r}$ für fair hält, erwartet von jedem Wurf eine mittlere Überraschung und wird nie sehr stark überrascht. Mit $\mathbf{q}=(0{,}7;\ 0{,}3)^{\top}$ dazwischen ist außerdem

$$D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})+D_{\mathrm{KL}}(\mathbf{q}\,\|\,\mathbf{r})\approx0{,}087+0{,}154=0{,}241<0{,}511\approx D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{r}) .$$

Der Umweg über $\mathbf{q}$ ist also „kürzer“ als der direkte Weg, und die Dreiecksungleichung ist verletzt.

Deshalb heißt die Größe Divergenz und nicht Abstand. Wer sie benutzt, muss sagen, welche Verteilung an erster Stelle steht: die, mit der gemittelt wird, meist die wahre.

⁠**Kurz gesagt:** Die KL-Divergenz ist nicht symmetrisch und erfüllt die Dreiecksungleichung nicht; sie misst einen gerichteten Mehraufwand, keinen Abstand.

:::aufgabe Aufgabe 38 ★ Kreuzentropie und KL-Divergenz
<span class="anker" id="aufg-38"></span>

Es sei $\mathbf{p}=(\tfrac12,\tfrac14,\tfrac14)^{\top}$ und $\mathbf{u}=(\tfrac13,\tfrac13,\tfrac13)^{\top}$.

<ol class="al">

<li>

Berechne $H(\mathbf{p})$, $H(\mathbf{p},\mathbf{u})$ und $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})$ in bit.

</li>

<li>

Berechne $D_{\mathrm{KL}}(\mathbf{u}\,\|\,\mathbf{p})$ und vergleiche.

</li>

</ol>

:::loesung
(a) $H(\mathbf{p})=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac14\cdot2=1{,}5$ bit; $H(\mathbf{p},\mathbf{u})=\log_23\approx1{,}585$ bit, denn jedes $q_k$ ist $\tfrac13$; $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{u})\approx0{,}085$ bit.

(b) $D_{\mathrm{KL}}(\mathbf{u}\,\|\,\mathbf{p})=\tfrac13\log_2\frac{1/3}{1/2}+\tfrac23\log_2\frac{1/3}{1/4}=\tfrac13\log_2\tfrac23+\tfrac23\log_2\tfrac43\approx-0{,}195+0{,}277=0{,}082$ bit. Die beiden Richtungen sind fast, aber nicht genau gleich.
:::
:::

:::aufgabe Aufgabe 39 ★★ Ein Ergebnis für unmöglich halten
<span class="anker" id="aufg-39"></span>

Es sei $\mathbf{p}=(0{,}5;\ 0{,}5)^{\top}$ und $\mathbf{q}=(1;\ 0)^{\top}$.

<ol class="al">

<li>

Berechne $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})$ und $D_{\mathrm{KL}}(\mathbf{q}\,\|\,\mathbf{p})$ in bit.

</li>

<li>

Deute das Ergebnis für den Maximum-Likelihood-Schätzer $\hat\theta_{\mathrm{ML}}=1$ nach dreimal Kopf in drei Würfen aus Unterabschnitt [5.2](die-maximum-likelihood-schatzung.html#stufe-5-2).

</li>

</ol>

:::loesung
(a) $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})$ ist unendlich, denn das zweite Ergebnis hat $p_2=0{,}5>0$, aber $q_2=0$. $D_{\mathrm{KL}}(\mathbf{q}\,\|\,\mathbf{p})=1\cdot\log_2\frac1{0{,}5}+0=1$ bit; der Summand mit $q_2=0$ fällt weg.

(b) Der Schätzer $\hat\theta_{\mathrm{ML}}=1$ ist das Modell $\mathbf{q}$: Es hält Zahl für unmöglich. Ist die Münze in Wahrheit fair, so ist dieses Modell unendlich weit von der Wahrheit entfernt, gemessen mit der KL-Divergenz in der Richtung, die mit der Wahrheit mittelt; schon ein einziger Wurf mit Zahl überrascht es unendlich stark. Ein Prior wie in Abschnitt [6](prior-und-posterior.html#stufe-6) verhindert das.
:::
:::

:::aufgabe Aufgabe 40 ★★ Codes und Kraft-Ungleichung
<span class="anker" id="aufg-40"></span>

<ol class="al">

<li>

Gibt es einen Präfixcode mit den Längen $1,2,2,3$? Und mit den Längen $2,2,2,3,3$? Gib ihn gegebenenfalls an.

</li>

<li>

Die Quelle mit $\mathbf{p}=(0{,}4;\ 0{,}3;\ 0{,}2;\ 0{,}1)^{\top}$ werde mit den Längen $\lceil\log_2(1/p_k)\rceil$ codiert. Berechne die Längen, prüfe die Kraft-Ungleichung und vergleiche die mittlere Länge mit der Entropie.

</li>

</ol>

:::loesung
(a) Für $1,2,2,3$ ist $\tfrac12+\tfrac14+\tfrac14+\tfrac18=\tfrac98>1$; es gibt keinen solchen Präfixcode. Für $2,2,2,3,3$ ist $\tfrac34+\tfrac28=1$; ein Code ist $00$, $01$, $10$, $110$, $111$.

(b) $\log_2(1/p_k)\approx1{,}32;\ 1{,}74;\ 2{,}32;\ 3{,}32$, aufgerundet $2,2,3,4$. Kraft: $\tfrac14+\tfrac14+\tfrac18+\tfrac1{16}=0{,}6875\le1$. Mittlere Länge $0{,}8+0{,}6+0{,}6+0{,}4=2{,}4$, Entropie $\approx1{,}846$ bit. Es ist $1{,}846\le2{,}4<2{,}846$, wie der Quellencodierungssatz sagt. Ein besserer Code mit den Längen $1,2,3,3$ hätte die mittlere Länge $1{,}9$.
:::
:::

:::aufgabe Aufgabe 41 ★★★ Gibbs für zwei Ergebnisse
<span class="anker" id="aufg-41"></span>

Für $0<p<1$ und $0<q<1$ sei $f(q)=p\ln\frac pq+(1-p)\ln\frac{1-p}{1-q}$ die KL-Divergenz zweier Bernoulli-Verteilungen in nat.

<ol class="al">

<li>

Zeige ohne die Gibbs-Ungleichung, mit der Ableitung nach $q$ und dem Vorzeichenwechsel, dass $f$ bei $q=p$ am kleinsten ist und dort den Wert $0$ hat.

</li>

<li>

Berechne $f$ für $p=0{,}5$ und $q=0{,}9$ und vergleiche mit dem Rechenbeispiel in Unterabschnitt [9.5](#stufe-9-5).

</li>

</ol>

:::loesung
(a) $f'(q)=-\frac pq+\frac{1-p}{1-q}=\frac{q-p}{q(1-q)}$. Der Nenner ist positiv, also ist $f'$ negativ für $q<p$ und positiv für $q>p$: $f$ fällt bis $q=p$ und steigt danach. Der kleinste Wert ist $f(p)=p\ln1+(1-p)\ln1=0$, also ist $f(q)\ge0$ mit Gleichheit nur bei $q=p$.

(b) $f(0{,}9)=0{,}5\ln\frac{0{,}5}{0{,}9}+0{,}5\ln\frac{0{,}5}{0{,}1}\approx-0{,}294+0{,}805=0{,}511$ nat, die Zahl $D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{r})$ aus Unterabschnitt [9.5](#stufe-9-5).
:::
:::
