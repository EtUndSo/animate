---
title: Pole und Nullstellen in der $p$-Ebene
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Laplace-Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Kapitel 2: Laplace-Transformation
order: 3220400
summary: In allen Beispielen war S(p) ein Bruch aus zwei Polynomen in p .
tags: Nullstelle, Pol-Nullstellen-Diagramm
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
In allen Beispielen war $S(p)$ ein Bruch aus zwei Polynomen in $p$. Dieser Abschnitt zeigt, durch welche wenigen Zahlen ein solcher Bruch festgelegt ist, wie man sie zeichnet, wo der Konvergenzbereich liegt und welche Rechenregeln die Transformation hat.
:::

### Nullstellen

<span class="anker" id="stufe-3-1"></span>

:::definition Definition 3.1 (Nullstelle)
<span class="anker" id="satz-3-1"></span>

Eine Stelle $p$, an der $S(p)=0$ ist, heißt __Nullstelle__ von $S(p)$. Ist $S(p)$ ein Bruch aus zwei Polynomen, so sind die Nullstellen die Nullstellen des Zählerpolynoms (sofern sie sich nicht gegen Pole kürzen).
:::

::::beispiel
Der Zähler von [(2.8)](beispiele-zur-laplace-transformation.html#gl-2-8) ist $2p^2+5p+12$. Mit der Lösungsformel für quadratische Gleichungen:

$$p_{\mathrm N1,2}=\frac{-5\pm\sqrt{25-96}}{4}=\frac{-5\pm\mathrm{j}\sqrt{71}}{4}=-\frac54\pm\frac{\sqrt{71}}{4}\,\mathrm{j}\approx-1{,}25\pm2{,}11\,\mathrm{j} .$$
::::

⁠**Kurz gesagt:** Nullstellen sind die Stellen, an denen $S(p)$ verschwindet.

### Die Produktform

<span class="anker" id="stufe-3-2"></span>

Ein Polynom vom Grad $Q$ hat genau $Q$ Nullstellen, wenn man mehrfache mehrfach zählt, und lässt sich in Linearfaktoren zerlegen. Kennt man also die $Q$ Nullstellen $p_{\mathrm N,q}$ und die $R$ Pole $p_{\mathrm P,r}$ eines Polynombruchs, so ist er bis auf einen Faktor bestimmt:

<span class="anker" id="gl-3-1"></span>
$$H(p)=H_0\,\frac{\prod_{q=1}^{Q}\bigl(p-p_{\mathrm N,q}\bigr)}{\prod_{r=1}^{R}\bigl(p-p_{\mathrm P,r}\bigr)} . \tag{3.1}$$

Der Faktor $H_0$ ist der Quotient der höchsten Koeffizienten von Zähler und Nenner. Die Formel gilt für jede rationale Laplace-Transformierte, hier mit $H$ geschrieben.

::::beispiel
Für [(2.8)](beispiele-zur-laplace-transformation.html#gl-2-8) ist der höchste Koeffizient des Zählers 2 und der des Nenners 1, also

$$S(p)=2\,\frac{(p-p_{\mathrm N1})(p-p_{\mathrm N2})}{(p+2)(p+1-3\mathrm{j})(p+1+3\mathrm{j})},\qquad H_0=2.$$
::::

⁠**Kurz gesagt:** Ein Polynombruch ist durch seine Pole, seine Nullstellen und den Faktor $H_0$ vollständig bestimmt.

### Das Pol-Nullstellen-Diagramm

<span class="anker" id="stufe-3-3"></span>

Man zeichnet Pole und Nullstellen in die $p$-Ebene: Pole als Kreuze ($\times$), Nullstellen als Kreise ($\circ$). Das ist das __Pol-Nullstellen-Diagramm__. Abbildung [4](#abb-4) zeigt es für das Signal [(2.6)](beispiele-zur-laplace-transformation.html#gl-2-6), zusammen mit dem Konvergenzbereich.

:::abbildung et3/k2pn 4
Pol-Nullstellen-Diagramm von $S(p)=\frac{2p^2+5p+12}{(p^2+2p+10)(p+2)}$ mit $H_0=2$: Pole (Kreuze) bei $-2$ und $-1\pm3\mathrm{j}$, Nullstellen (Kreise) bei $-1{,}25\pm2{,}11\,\mathrm{j}$, Achsen in $1/\mathrm s$. Der Konvergenzbereich $\operatorname{Re} p>-1$ (blau) liegt rechts des am weitesten rechts liegenden Pols.
:::

Das Diagramm zusammen mit $H_0$ legt den Ausdruck $S(p)$ fest. Um das Signal festzulegen, braucht man zusätzlich den Konvergenzbereich.

⁠**Kurz gesagt:** Kreuze für Pole, Kreise für Nullstellen, dazu der Konvergenzbereich: Mehr braucht man nicht, um ein Signal mit rationaler Transformierter zu beschreiben.

:::hintergrund Das Diagramm als Landschaft: was man an Polen und Nullstellen abliest
Trägt man $|H(p)|$ als Höhe über der $p$-Ebene auf, entsteht eine Landschaft. Man kann sie sich als Gummituch vorstellen: An jedem Pol wird es von einer Zeltstange ins Unendliche gehoben, an jeder Nullstelle mit einem Nagel auf den Boden gedrückt. Die Produktform [(3.1)](#gl-3-1) macht das genau. Weil der Betrag eines Produkts das Produkt der Beträge ist, gilt

$$|H(p)|=|H_0|\,\frac{\prod_q|p-p_{\mathrm N,q}|}{\prod_r|p-p_{\mathrm P,r}|}.$$

Jeder Faktor $|p-p_{\mathrm N,q}|$ ist der Abstand des Punkts $p$ von einer Nullstelle, jeder Faktor $|p-p_{\mathrm P,r}|$ der Abstand von einem Pol. Nahe an einem Pol wird ein Nenner klein und $|H|$ groß, nahe an einer Nullstelle wird ein Zähler klein und $|H|$ klein.

⁠**Was eine Nullstelle für ein System bedeutet.** Ist $H(p_\mathrm N)=0$ und liegt $p_\mathrm N$ im Konvergenzbereich, dann antwortet das System auf den Eingang $\mathrm{e}^{p_\mathrm Nt}$ mit $H(p_\mathrm N)\,\mathrm{e}^{p_\mathrm Nt}=0$: Es sperrt diese Exponentialfunktion vollständig. Ein Sperrfilter gegen 50-Hz-Brummen hat deshalb ein Nullstellenpaar bei $p=\pm\mathrm{j}2\pi\cdot50\,\mathrm{Hz}$.

⁠**Der Frequenzgang ist ein Schnitt durch die Landschaft.** Im Kapitel zur Faltung war der Frequenzgang $H(F)$ die Zahl, mit der ein System die Schwingung $\mathrm{e}^{\mathrm{j}2\pi Ft}$ multipliziert. Das ist $H(p)$ an der Stelle $p=\mathrm{j}2\pi F$, also auf der imaginären Achse (sofern sie im Konvergenzbereich liegt). Wer die imaginäre Achse hinaufwandert, sieht deshalb den Betrag des Frequenzgangs: Er steigt, wenn man an einem Pol vorbeikommt, und sinkt bei einer Nullstelle. Beim RC-Tiefpass $H(p)=\frac{1/RC}{p+1/RC}$ ist der Abstand vom Pol $-1/RC$ bei $F=0$ gleich $1/RC$ und wächst für große $F$ etwa wie $2\pi F$. Deshalb fällt $|H|$ bei hohen Frequenzen wie $1/F$: Das ist das Tiefpassverhalten, direkt aus der Lage des Pols abgelesen.
:::

### Wo der Konvergenzbereich liegt

<span class="anker" id="stufe-3-4"></span>

Jeder Pol gehört zu einem Exponentialimpuls im Signal, und dessen Konvergenzbereich ist eine Halbebene, die am Pol endet. Der Konvergenzbereich des ganzen Signals ist der Durchschnitt dieser Halbebenen. Daraus folgen drei Regeln. Der Konvergenzbereich liegt

<ul>

<li>

bei rein rechtsseitigen (kausalen) Signalen rechts von dem am weitesten rechts gelegenen Pol;

</li>

<li>

bei rein linksseitigen (antikausalen) Signalen links von dem am weitesten links gelegenen Pol;

</li>

<li>

bei zweiseitigen Signalen zwischen dem am weitesten rechts gelegenen Pol eines rechtsseitigen Anteils und dem am weitesten links gelegenen Pol eines linksseitigen Anteils.

</li>

</ul>

::::beispiel ein Ausdruck, drei Signale
Gegeben sei

<span class="anker" id="gl-3-2"></span>
$$S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2} \tag{3.2}$$

mit Polen bei $p_{\mathrm P1}=-1$ und $p_{\mathrm P2}=-2$ (Abb. [5](#abb-5)a). Die Zerlegung rechts prüft man über den Hauptnenner: $\frac{(p+2)-(p+1)}{(p+1)(p+2)}=\frac{1}{(p+1)(p+2)}$. Je nach Konvergenzbereich gehört dazu ein anderes Signal, jeweils mit den Grundpaaren [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) und [(2.10)](beispiele-zur-laplace-transformation.html#gl-2-10):

<ol class="al">

<li>

Rechtsseitig: Konvergenzbereich rechts des rechten Pols, $\operatorname{Re} p>-1$ (Abb. [5](#abb-5)b). Beide Brüche gehören zu rechtsseitigen Impulsen: $s(t)=\bigl(\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\cdot\varepsilon(t)$.

</li>

<li>

Linksseitig: Konvergenzbereich links des linken Pols, $\operatorname{Re} p<-2$ (Abb. [5](#abb-5)c). Beide gehören zu linksseitigen Impulsen: $s(t)=-\bigl(\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\cdot\varepsilon(-t)$.

</li>

<li>

Zweiseitig: Konvergenzbereich zwischen den Polen, $-2<\operatorname{Re} p<-1$ (Abb. [5](#abb-5)d). Dieser Streifen liegt links vom Pol $-1$ und rechts vom Pol $-2$. Also gehört $\frac{1}{p+1}$ zu einem linksseitigen und $-\frac{1}{p+2}$ zu einem rechtsseitigen Impuls: $s(t)=-\mathrm{e}^{-t}\cdot\varepsilon(-t)-\mathrm{e}^{-2t}\cdot\varepsilon(t)$.

</li>

</ol>

:::abbildung et3/k2dreikb 5
Ein Ausdruck, drei Signale: (a) die Pole von $S(p)=1/\bigl((p+1)(p+2)\bigr)$; Konvergenzbereich (blau) für (b) das rechtsseitige, (c) das linksseitige und (d) das zweiseitige Signal.
:::
::::

⁠**Kurz gesagt:** Bei einem rechtsseitigen Signal liegt der Konvergenzbereich rechts aller Pole, bei einem linksseitigen links aller Pole, bei einem zweiseitigen in einem Streifen zwischen ihnen.

### Faltung wird Multiplikation

<span class="anker" id="stufe-3-5"></span>

Die Kette [(1.8)](eigenfunktionen-von-lti-systemen.html#gl-1-8) hat schon gezeigt, dass sich Übertragungsfunktionen multiplizieren, solange der Eingang eine Eigenfunktion ist. Dasselbe gilt für beliebige Signale.

:::satz Satz 3.2 (Faltungssatz)
<span class="anker" id="satz-3-2"></span>

<span class="anker" id="gl-3-3"></span>
$$\mathcal{L}\{s(t)*h(t)\}=S(p)\cdot H(p) \tag{3.3}$$

für alle $p$, die in den Konvergenzbereichen von $S$ und von $H$ liegen.
:::

:::herleitung Faltungssatz
Man setzt das Faltungsintegral in die Transformation ein:

$$\mathcal{L}\{s*h\}=\int_{-\infty}^{\infty}\Bigl[\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau\Bigr]\mathrm{e}^{-pt}\,\mathrm{d} t .$$

Liegt $p$ in beiden Konvergenzbereichen, konvergiert das Doppelintegral absolut, und man darf die Reihenfolge der Integrationen tauschen. Im inneren Integral über $t$ substituiert man $u=t-\tau$ (bei festem $\tau$ ist $\mathrm{d} t=\mathrm{d} u$) und zerlegt $\mathrm{e}^{-pt}=\mathrm{e}^{-p\tau}\,\mathrm{e}^{-pu}$:

$$\mathcal{L}\{s*h\}=\int_{-\infty}^{\infty}s(\tau)\,\mathrm{e}^{-p\tau}\Bigl[\int_{-\infty}^{\infty}h(u)\,\mathrm{e}^{-pu}\,\mathrm{d} u\Bigr]\mathrm{d}\tau=\int_{-\infty}^{\infty}s(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau\cdot H(p)=S(p)\,H(p).$$
:::

::::beispiel
Im Kapitel zur Faltung ergab $\varepsilon(t)*\varepsilon(t)=t\,\varepsilon(t)$. Im Bildbereich ist das $\frac1p\cdot\frac1p=\frac{1}{p^2}$ für $\operatorname{Re} p>0$, und das ist nach [(2.12)](beispiele-zur-laplace-transformation.html#gl-2-12) tatsächlich die Transformierte von $t\,\varepsilon(t)$.
::::

⁠**Kurz gesagt:** Aus der Faltung im Zeitbereich wird im Bildbereich ein Produkt.

:::hintergrund Warum gerade ein Produkt
Das ist die Diagonalform aus dem Kasten „Eigenfunktionen als Koordinatensystem“ im ersten Abschnitt. $S(p)$ beschreibt den Eingang im Koordinatensystem der Funktionen $\mathrm{e}^{pt}$, $H(p)$ ist der Eigenwert, mit dem das System jede von ihnen multipliziert, und $G(p)=H(p)\,S(p)$ beschreibt den Ausgang im selben Koordinatensystem. Die Faltung koppelt im Zeitbereich jeden Ausgangswert mit allen Eingangswerten. Im Bildbereich gibt es keine Kopplung mehr: Jede Stelle $p$ wird für sich mit ihrem Eigenwert multipliziert. Die Herleitung oben zeigt dasselbe rechnerisch. Die Substitution $u=t-\tau$ trennt das Doppelintegral in zwei unabhängige Faktoren, weil $\mathrm{e}^{-pt}=\mathrm{e}^{-p\tau}\,\mathrm{e}^{-pu}$ Verschieben in Multiplizieren verwandelt.
:::

### Ableiten im Zeitbereich

<span class="anker" id="stufe-3-6"></span>

Aus dem Kapitel zur Faltung ist bekannt: Der Differenzierer ist ein LTI-System mit der Impulsantwort $\delta'(t)$, dem Doppelimpuls, und es gilt $s(t)*\delta'(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t)$. Seine Übertragungsfunktion bekommt man ohne Rechnung aus der Eigenfunktion: $\mathrm{e}^{pt}*\delta'(t)=\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$. Der Eigenwert ist also $p$:

<span class="anker" id="gl-3-4"></span>
$$\mathcal{L}\Bigl\{\frac{\mathrm{d}}{\mathrm{d} t}s(t)=s(t)*\delta'(t)\Bigr\}=p\cdot S(p)\qquad\Longrightarrow\qquad\mathcal{L}\{\delta'(t)\}=p . \tag{3.4}$$

Der Faltungssatz liefert das linke Ergebnis aus dem rechten. Der Konvergenzbereich ist mindestens der von $S(p)$, denn $\mathcal{L}\{\delta'\}=p$ existiert für alle $p$. Wer $n$-mal ableitet, multipliziert $n$-mal mit $p$: $\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\longleftrightarrow p^n\,S(p)$.

⁠**Kurz gesagt:** Ableiten im Zeitbereich ist Multiplizieren mit $p$ im Bildbereich.

### Integrieren im Zeitbereich

<span class="anker" id="stufe-3-7"></span>

Der Integrator ist ein LTI-System mit der Impulsantwort $\varepsilon(t)$: $\int_{-\infty}^t s(\tau)\,\mathrm{d}\tau=s(t)*\varepsilon(t)$. Mit $\mathcal{L}\{\varepsilon(t)\}=1/p$ für $\operatorname{Re} p>0$ und dem Faltungssatz folgt

<span class="anker" id="gl-3-5"></span>
$$\mathcal{L}\Bigl\{\int_{-\infty}^{t}s(\tau)\,\mathrm{d}\tau=s(t)*\varepsilon(t)\Bigr\}=\frac1p\,S(p)\qquad\Longrightarrow\qquad\mathcal{L}\{\varepsilon(t)\}=\frac1p,\ \operatorname{Re}\{p\}>0 . \tag{3.5}$$

Der Konvergenzbereich ist mindestens der Durchschnitt des Konvergenzbereichs von $S(p)$ mit der Halbebene $\operatorname{Re} p>0$.

⁠**Kurz gesagt:** Integrieren im Zeitbereich ist Dividieren durch $p$ im Bildbereich, mit der Zusatzbedingung $\operatorname{Re} p>0$.

:::hintergrund Warum beim Integrieren die Bedingung $\operatorname{Re} p>0$ dazukommt
Gibt man $\mathrm{e}^{pt}$ auf den Integrator, so ist der Ausgang

$$\int_{-\infty}^{t}\mathrm{e}^{p\tau}\,\mathrm{d}\tau=\Bigl[\frac{\mathrm{e}^{p\tau}}{p}\Bigr]_{-\infty}^{t}=\frac{\mathrm{e}^{pt}}{p},$$

aber nur, wenn $\mathrm{e}^{p\tau}$ für $\tau\to-\infty$ verschwindet, also für $\operatorname{Re} p>0$. Für $\operatorname{Re} p\le0$ war das Signal in der Vergangenheit nicht klein genug: Der Integrator hätte unendlich viel aufsummiert. Beim Differenzierer gibt es keine solche Bedingung, denn $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ gilt für jedes $p$.
:::

### Der Dirac-Impuls

<span class="anker" id="stufe-3-8"></span>

Faltung mit $\delta(t)$ lässt jedes Signal unverändert: $s(t)=s(t)*\delta(t)$. Im Bildbereich heißt das $S(p)=S(p)\cdot\mathcal{L}\{\delta(t)\}$, also

<span class="anker" id="gl-3-6"></span>
$$s(t)=s(t)*\delta(t)\qquad\Longrightarrow\qquad\mathcal{L}\{\delta(t)\}=1 . \tag{3.6}$$

Das stimmt mit dem Grundpaar [(2.11)](beispiele-zur-laplace-transformation.html#gl-2-11) überein.

⁠**Kurz gesagt:** Der Dirac-Impuls hat die Transformierte 1, für alle $p$.

:::aufgabe Aufgabe 3 ★ Pole, Nullstellen, Konvergenzbereiche
<span class="anker" id="aufg-3"></span>

$S(p)=\dfrac{p+3}{(p+1)(p+2)}$, $p$ in $1/\mathrm s$.

<ol class="al">

<li>

Bestimme Pole, Nullstellen und $H_0$ und zeichne das Pol-Nullstellen-Diagramm.

</li>

<li>

Prüfe die Zerlegung $S(p)=\frac{2}{p+1}-\frac{1}{p+2}$ über den Hauptnenner.

</li>

<li>

Welche drei Konvergenzbereiche sind möglich? Gib zu jedem das Signal an.

</li>

<li>

Welches der drei Signale ist absolut integrierbar? Woran erkennt man das am Konvergenzbereich?

</li>

</ol>

:::loesung
(a) Pole sind die Nullstellen des Nenners: $p_{\mathrm P1}=-1$, $p_{\mathrm P2}=-2$. Nullstelle des Zählers: $p_{\mathrm N}=-3$. Die höchsten Koeffizienten von Zähler ($p$) und Nenner ($p^2$) sind beide 1, also $H_0=1$. Im Diagramm: Kreuze bei $-1$ und $-2$, ein Kreis bei $-3$, alle auf der reellen Achse.

(b) $\frac{2}{p+1}-\frac{1}{p+2}=\frac{2(p+2)-(p+1)}{(p+1)(p+2)}=\frac{p+3}{(p+1)(p+2)}$.

(c) Mit den Grundpaaren [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) und [(2.10)](beispiele-zur-laplace-transformation.html#gl-2-10):

<ul>

<li>

$\operatorname{Re} p>-1$ (rechtsseitig): $s(t)=\bigl(2\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$.

</li>

<li>

$\operatorname{Re} p<-2$ (linksseitig): $s(t)=-\bigl(2\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\varepsilon(-t)$.

</li>

<li>

$-2<\operatorname{Re} p<-1$ (zweiseitig): Der Streifen liegt links vom Pol $-1$ und rechts vom Pol $-2$. $\frac{2}{p+1}$ gehört zu $-2\mathrm{e}^{-t}\varepsilon(-t)$, $-\frac{1}{p+2}$ zu $-\mathrm{e}^{-2t}\varepsilon(t)$. Zusammen $s(t)=-2\mathrm{e}^{-t}\varepsilon(-t)-\mathrm{e}^{-2t}\varepsilon(t)$.

</li>

</ul>

(d) Nur das rechtsseitige: Beide Summanden klingen für $t\to\infty$ ab. Beim linksseitigen und beim zweiseitigen Signal wächst $\mathrm{e}^{-t}$ für $t\to-\infty$ wie $\mathrm{e}^{|t|}$. Am Konvergenzbereich erkennt man es so: $\int|s(t)|\,\mathrm{d} t$ ist das Integral aus der Definition des Konvergenzbereichs an der Stelle $\sigma=0$. Absolut integrierbar ist das Signal also genau dann, wenn $\sigma=0$ im Konvergenzbereich liegt, und das ist nur bei $\operatorname{Re} p>-1$ der Fall.
:::
:::

:::aufgabe Aufgabe 4 ★★ Kette und Ableitung
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Begründe mit dem Faltungssatz, warum zwei LTI-Systeme in rückwirkungsfreier Kette für *jeden* Eingang, nicht nur für $\mathrm{e}^{pt}$, wie ein System mit der Übertragungsfunktion $H_1(p)H_2(p)$ wirken. Warum spielt die Reihenfolge der beiden Systeme im Bildbereich keine Rolle?

</li>

<li>

Leite $\mathcal{L}\{\dot s(t)\}=p\,S(p)$ ein zweites Mal her, diesmal mit partieller Integration. Setze dafür voraus, dass $s(t)\,\mathrm{e}^{-pt}$ für $t\to\pm\infty$ gegen null geht.

</li>

</ol>

:::loesung
(a) Der Ausgang der Kette ist $g=(s*h_1)*h_2$. Zweimal der Faltungssatz: $\mathcal{L}\{s*h_1\}=S\,H_1$ und dann $G=(S\,H_1)\,H_2=S\cdot(H_1H_2)$, für alle $p$ in den drei Konvergenzbereichen. Das ist genau der Ausgang eines Systems mit der Übertragungsfunktion $H_1H_2$, für jeden Eingang $s$. Vertauscht man die Systeme, erhält man $S\,H_2\,H_1$. Im Bildbereich sind beide gleich, weil Zahlen kommutieren: $H_1(p)H_2(p)=H_2(p)H_1(p)$. Im Zeitbereich entspricht das $h_1*h_2=h_2*h_1$, was man auch direkt mit einer Substitution im Faltungsintegral zeigen kann (Kapitel zur Faltung).

(b) Partielle Integration mit $u=\mathrm{e}^{-pt}$, $v'=\dot s$:

$$\int_{-\infty}^{\infty}\dot s(t)\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[s(t)\,\mathrm{e}^{-pt}\Bigr]_{-\infty}^{\infty}-\int_{-\infty}^{\infty}s(t)\,(-p)\,\mathrm{e}^{-pt}\mathrm{d} t=0+p\,S(p).$$

Der Randterm verschwindet nach Voraussetzung.
:::
:::

::::kurzfassung
Eine Laplace-Transformierte, die ein Bruch aus zwei Polynomen ist, ist durch ihre Pole, ihre Nullstellen und einen Faktor $H_0$ festgelegt. Das Signal legt erst der Konvergenzbereich dazu fest. Außerdem wird aus der Faltung ein Produkt.

Eine __Nullstelle__ ist eine Stelle $p$ mit $S(p)=0$; bei einem Polynombruch ist es eine Nullstelle des Zählers, die sich nicht gegen einen Pol kürzt. Mit den $Q$ Nullstellen $p_{\mathrm N,q}$ und den $R$ Polen $p_{\mathrm P,r}$ gilt die __Produktform__

$$H(p)=H_0\,\frac{\prod_{q=1}^{Q}\bigl(p-p_{\mathrm N,q}\bigr)}{\prod_{r=1}^{R}\bigl(p-p_{\mathrm P,r}\bigr)} ;$$

$H_0$ ist der Quotient der höchsten Koeffizienten von Zähler und Nenner. Pole als Kreuze und Nullstellen als Kreise in der $p$-Ebene ergeben das __Pol-Nullstellen-Diagramm__. Der Konvergenzbereich liegt bei rechtsseitigen Signalen rechts aller Pole, bei linksseitigen links aller Pole, bei zweiseitigen in einem Streifen zwischen ihnen.

Der __Faltungssatz__ $\mathcal{L}\{s(t)*h(t)\}=S(p)\cdot H(p)$ gilt für alle $p$ in beiden Konvergenzbereichen. Daraus folgt: Ableiten im Zeitbereich ist Multiplizieren mit $p$, denn $\mathcal{L}\{\delta'(t)\}=p$. Integrieren ist Dividieren durch $p$, mit der Zusatzbedingung $\operatorname{Re} p>0$. Der Dirac-Impuls hat die Transformierte $1$.

Der Grund für das Produkt: $S(p)$ beschreibt den Eingang durch die Funktionen $\mathrm{e}^{pt}$, und das System multipliziert jede von ihnen für sich mit ihrem Eigenwert $H(p)$. Die Kopplung aller Zeitpunkte durch die Faltung gibt es im Bildbereich nicht.

Falle: Diagramm und $H_0$ legen nur den Ausdruck fest. Je nach Konvergenzbereich gehört er zu einem rechtsseitigen, einem linksseitigen oder einem zweiseitigen Signal.
::::

::::formelsammlung
**Produktform**

$$H(p)=H_0\,\frac{\prod_{q=1}^{Q}\bigl(p-p_{\mathrm N,q}\bigr)}{\prod_{r=1}^{R}\bigl(p-p_{\mathrm P,r}\bigr)}$$

$p_{\mathrm N,q}$ die $Q$ Nullstellen, $p_{\mathrm P,r}$ die $R$ Pole (mehrfache mehrfach gezählt); $H_0$ Quotient der höchsten Koeffizienten von Zähler und Nenner. Gilt für jede rationale Laplace-Transformierte.

**Betrag aus Polen und Nullstellen**

$$|H(p)|=|H_0|\,\frac{\prod_q|p-p_{\mathrm N,q}|}{\prod_r|p-p_{\mathrm P,r}|}$$

Jeder Faktor ist ein Abstand des Punkts $p$ von einer Nullstelle bzw. einem Pol: nahe einem Pol wird $|H|$ groß, nahe einer Nullstelle klein.

**Faltungssatz**

$$\mathcal{L}\{s(t)*h(t)\}=S(p)\cdot H(p)$$

Für alle $p$, die in den Konvergenzbereichen von $S$ und von $H$ liegen.

**Ableitung im Zeitbereich**

$$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\longleftrightarrow p^n\,S(p)$$

Für $n=1$: Differenzierer mit der Impulsantwort $\delta'(t)$, $\frac{\mathrm{d}}{\mathrm{d} t}s(t)=s(t)*\delta'(t)$. Konvergenzbereich mindestens der von $S(p)$.

**Doppelimpuls**

$$\mathcal{L}\{\delta'(t)\}=p$$

Für alle $p$; folgt aus $\mathrm{e}^{pt}*\delta'(t)=\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$.

**Integration im Zeitbereich**

$$\mathcal{L}\Bigl\{\int_{-\infty}^{t}s(\tau)\,\mathrm{d}\tau=s(t)*\varepsilon(t)\Bigr\}=\frac1p\,S(p)$$

Konvergenzbereich mindestens der Durchschnitt des Konvergenzbereichs von $S(p)$ mit $\operatorname{Re} p>0$; Integrierer mit der Impulsantwort $\varepsilon(t)$, $\mathcal{L}\{\varepsilon(t)\}=\frac1p$ für $\operatorname{Re}\{p\}>0$.

**Dirac-Impuls**

$$\mathcal{L}\{\delta(t)\}=1$$

Für alle $p$; folgt aus $s(t)=s(t)*\delta(t)$.
::::

::::lernkarten
:::karte begriff Nullstelle
Was ist eine Nullstelle einer Laplace-Transformierten $S(p)$, und wo liegt sie, wenn $S(p)$ ein Bruch aus zwei Polynomen ist?
---
Eine Stelle $p$, an der $S(p)=0$ ist. Ist $S(p)$ ein Bruch aus zwei Polynomen, so sind die Nullstellen die Nullstellen des Zählerpolynoms, sofern sie sich nicht gegen Pole kürzen.
--- falsch
Eine Stelle $p$, an der $S(p)=0$ ist. Ist $S(p)$ ein Bruch aus zwei Polynomen, so sind die Nullstellen die Nullstellen des Nennerpolynoms, weil der Bruch dort keinen Wert hat und null gesetzt wird.
--- falsch
Ein Zeitpunkt $t$, an dem das Signal $s(t)$ durch null geht. Ist $S(p)$ ein Bruch aus zwei Polynomen, so liest man diese Nulldurchgänge an den Nullstellen des Zählerpolynoms ab, gemessen in Sekunden.
--- falsch
Die Stelle $p=0$, also der Ursprung der $p$-Ebene, an der $S(p)$ den Gleichanteil des Signals angibt. Ein Bruch aus zwei Polynomen hat deshalb genau eine Nullstelle, gleichgültig, welchen Grad der Zähler hat.
:::
:::karte begriff Produktform
Was ist die Produktform eines Polynombruchs $H(p)$, und durch welche Größen ist er damit festgelegt?
---
$H(p)=H_0\,\frac{\prod_{q=1}^{Q}\bigl(p-p_{\mathrm N,q}\bigr)}{\prod_{r=1}^{R}\bigl(p-p_{\mathrm P,r}\bigr)}$, Zähler und Nenner in Linearfaktoren zerlegt. Der Bruch ist durch seine $Q$ Nullstellen, seine $R$ Pole und den Faktor $H_0$ festgelegt, den Quotienten der höchsten Koeffizienten von Zähler und Nenner.
--- falsch
$H(p)=H_0\,\frac{\prod_{q=1}^{Q}\bigl(p+p_{\mathrm N,q}\bigr)}{\prod_{r=1}^{R}\bigl(p+p_{\mathrm P,r}\bigr)}$, Zähler und Nenner in Linearfaktoren zerlegt. Der Bruch ist durch Nullstellen, Pole und den Faktor $H_0$ festgelegt, den Quotienten der konstanten Glieder von Zähler und Nenner, also $H_0=H(0)$.
--- falsch
$H(p)=\frac{\prod_{q=1}^{Q}\bigl(p-p_{\mathrm N,q}\bigr)}{\prod_{r=1}^{R}\bigl(p-p_{\mathrm P,r}\bigr)}$, Zähler und Nenner in Linearfaktoren zerlegt. Der Bruch ist allein durch seine $Q$ Nullstellen und $R$ Pole vollständig festgelegt; ein zusätzlicher Faktor ist nicht nötig, weil er sich stets herauskürzt.
--- falsch
$H(p)=H_0\,\prod_{r=1}^{R}\frac{1}{p-p_{\mathrm P,r}}$, also ein Produkt aus einfachen Brüchen, einer je Pol. Die Nullstellen gehen nicht ein, weil sie sich bei einem Polynombruch stets gegen Pole kürzen; festgelegt ist der Bruch durch die Pole und den Faktor $H_0$.
:::
:::karte begriff Pol-Nullstellen-Diagramm
Was zeigt das Pol-Nullstellen-Diagramm einer Laplace-Transformierten, und was braucht man zusätzlich, um das Signal festzulegen?
---
Die Pole als Kreuze ($\times$) und die Nullstellen als Kreise ($\circ$) in der $p$-Ebene. Zusammen mit dem Faktor $H_0$ legt es den Ausdruck $S(p)$ fest; um das Signal festzulegen, braucht man zusätzlich den Konvergenzbereich.
--- falsch
Die Pole als Kreise ($\circ$) und die Nullstellen als Kreuze ($\times$) in der $p$-Ebene. Zusammen mit dem Konvergenzbereich legt es das Signal vollständig fest; der Faktor $H_0$ wird nicht gebraucht, weil er nur die Einheit festlegt.
--- falsch
Den Verlauf des Signals $s(t)$ über der Zeit, mit Kreuzen an den Maxima und Kreisen an den Nulldurchgängen. Es legt das Signal vollständig fest; zusätzlich braucht man nur die Einheit der Zeitachse, etwa Sekunden.
--- falsch
Die Pole als Kreuze ($\times$) und die Nullstellen als Kreise ($\circ$) in der $p$-Ebene. Es legt das Signal allein schon fest, weil die Lage jedes Pols zeigt, ob sein Anteil rechtsseitig ist: Pole links der imaginären Achse gehören zu rechtsseitigen Anteilen.
:::
:::karte zusammenhang Landschaft über der p-Ebene
Warum wird $|H(p)|$ in der Nähe eines Pols groß und in der Nähe einer Nullstelle klein?
---
Nach der Produktform ist $|H(p)|=|H_0|\,\frac{\prod_q|p-p_{\mathrm N,q}|}{\prod_r|p-p_{\mathrm P,r}|}$, weil der Betrag eines Produkts das Produkt der Beträge ist. Jeder Faktor ist ein Abstand: Nahe an einem Pol wird ein Nenner klein, nahe an einer Nullstelle ein Zähler.
--- falsch
Weil Pole die Stellen sind, an denen das Signal $s(t)$ selbst groß ist, und Nullstellen die Stellen, an denen es null ist. $|H(p)|$ übernimmt diese Werte unmittelbar, weil die Transformation den Betrag des Signals an jeder Stelle erhält.
--- falsch
Nach der Produktform ist $|H(p)|=|H_0|\,\frac{\prod_r|p-p_{\mathrm P,r}|}{\prod_q|p-p_{\mathrm N,q}|}$. Jeder Faktor ist ein Abstand: Weit weg von einem Pol wird ein Zähler groß, weit weg von einer Nullstelle ein Nenner, und dazwischen wechselt $|H|$ zwischen groß und klein.
--- falsch
Weil $|H(p)|$ wie der Konvergenzbereich nur von $\operatorname{Re} p$ abhängt. Pole liegen auf Geraden, auf denen das Integral nicht konvergiert, Nullstellen auf Geraden, auf denen es genau null ergibt; dazwischen ändert sich $|H|$ stetig.
:::
:::karte zusammenhang Nullstelle sperrt
Was macht ein System mit dem Eingang $\mathrm{e}^{p_\mathrm Nt}$, wenn $p_\mathrm N$ eine Nullstelle seiner Übertragungsfunktion ist, die im Konvergenzbereich liegt?
---
Es antwortet mit $H(p_\mathrm N)\,\mathrm{e}^{p_\mathrm Nt}=0$, sperrt diese Exponentialfunktion also vollständig. Deshalb hat ein Sperrfilter gegen 50-Hz-Brummen ein Nullstellenpaar bei $p=\pm\mathrm{j}2\pi\cdot50\,\mathrm{Hz}$.
--- falsch
Es verstärkt diese Exponentialfunktion unbegrenzt, weil der Nenner von $1/H$ dort null wird. Deshalb baut man Oszillatoren für 50 Hz mit einem Nullstellenpaar bei $p=\pm\mathrm{j}2\pi\cdot50\,\mathrm{Hz}$.
--- falsch
Es lässt diese Exponentialfunktion unverändert durch, weil eine Nullstelle den Eigenwert 1 bedeutet. Ein Sperrfilter gegen 50-Hz-Brummen braucht deshalb Pole bei $p=\pm\mathrm{j}2\pi\cdot50\,\mathrm{Hz}$, keine Nullstellen.
--- falsch
Es verzögert diese Exponentialfunktion um eine halbe Periode, weil $H(p_\mathrm N)=0$ eine Phasendrehung um $180^\circ$ bedeutet. Erst zwei Nullstellen hintereinander sperren das Signal vollständig.
:::
:::karte zusammenhang Frequenzgang als Schnitt
Warum fällt der Betrag des Frequenzgangs beim RC-Tiefpass $H(p)=\frac{1/RC}{p+1/RC}$ für hohe Frequenzen wie $1/F$?
---
Der Frequenzgang ist $H(p)$ an der Stelle $p=\mathrm{j}2\pi F$, also auf der imaginären Achse. Der Abstand dieses Punkts vom Pol $-1/RC$ steht im Nenner; er ist bei $F=0$ gleich $1/RC$ und wächst für große $F$ etwa wie $2\pi F$. Deshalb fällt $|H|$ wie $1/F$.
--- falsch
Der Frequenzgang ist $H(p)$ an der Stelle $p=F$, also auf der reellen Achse. Für große $F$ wächst der Nenner $p+1/RC$ wie $F$, und $|H|$ fällt wie $1/F$; auf der imaginären Achse wäre $|H|$ dagegen für alle Frequenzen konstant.
--- falsch
Weil der RC-Tiefpass eine Nullstelle bei $p=\infty$ hat, an der der Frequenzgang null wird. Je höher die Frequenz, desto näher liegt $\mathrm{j}2\pi F$ an dieser Nullstelle, und der Abstand zu ihr fällt wie $1/F$, also auch der Betrag $|H|$.
--- falsch
Der Frequenzgang ist $H(p)$ an der Stelle $p=\mathrm{j}2\pi F$. Der Abstand dieses Punkts vom Pol $-1/RC$ bleibt für alle $F$ gleich $1/RC$, weil der Pol auf der reellen Achse liegt; der Abfall kommt allein von der Phase, die mit $F$ wächst.
:::
:::karte zusammenhang Lage des Konvergenzbereichs
Wo liegt der Konvergenzbereich bei rein rechtsseitigen, rein linksseitigen und zweiseitigen Signalen, und warum liegt er dort?
---
Jeder Pol gehört zu einem Exponentialimpuls, dessen Konvergenzbereich eine Halbebene ist, die am Pol endet; der ganze Bereich ist ihr Durchschnitt. Rechtsseitig liegt er rechts des am weitesten rechts gelegenen Pols, linksseitig links des am weitesten links gelegenen, zweiseitig in einem Streifen dazwischen.
--- falsch
Rechtsseitig in der rechten Halbebene $\operatorname{Re} p>0$, linksseitig in der linken Halbebene $\operatorname{Re} p<0$, zweiseitig auf der imaginären Achse. Die Lage der Pole spielt keine Rolle, weil der Konvergenzbereich nur von der Seite der Zeitachse abhängt, auf der das Signal liegt.
--- falsch
Jeder Pol gehört zu einem Exponentialimpuls mit einer Halbebene als Konvergenzbereich; der ganze Bereich ist ihre Vereinigung. Rechtsseitig liegt er rechts des am weitesten links gelegenen Pols, linksseitig links des am weitesten rechts gelegenen, zweiseitig überall außer an den Polen.
--- falsch
Rechtsseitig links aller Pole, weil das Signal dort abklingt, linksseitig rechts aller Pole. Zweiseitig ist er ein Kreis um den Ursprung, der vom nächstgelegenen Pol begrenzt wird, weil das Signal nach beiden Seiten gleich stark abklingt und keine Richtung in der $p$-Ebene bevorzugt ist.
:::
:::karte formel Ein Ausdruck, drei Signale
Welche Signale gehören zu $S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$ bei den Konvergenzbereichen $\operatorname{Re} p>-1$, $\operatorname{Re} p<-2$ und $-2<\operatorname{Re} p<-1$?
---
$\bigl(\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\cdot\varepsilon(t)$, $-\bigl(\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\cdot\varepsilon(-t)$ und $-\mathrm{e}^{-t}\cdot\varepsilon(-t)-\mathrm{e}^{-2t}\cdot\varepsilon(t)$. Im Streifen liegt der Pol $-1$ rechts, sein Bruch gehört zu einem linksseitigen Impuls; der Pol $-2$ liegt links und liefert einen rechtsseitigen.
--- falsch
$\bigl(\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\cdot\varepsilon(t)$, $-\bigl(\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\cdot\varepsilon(-t)$ und $\mathrm{e}^{-t}\cdot\varepsilon(t)+\mathrm{e}^{-2t}\cdot\varepsilon(-t)$. Im Streifen liegt der Pol $-1$ rechts und gehört deshalb zu einem rechtsseitigen Impuls; der Pol $-2$ liefert einen linksseitigen.
--- falsch
In allen drei Fällen $\bigl(\mathrm{e}^{-t}-\mathrm{e}^{-2t}\bigr)\cdot\varepsilon(t)$, weil die Partialbrüche nur von den Polen abhängen. Der Konvergenzbereich legt lediglich fest, für welche $p$ man die Formel auswerten darf, nicht das Signal selbst.
--- falsch
$\bigl(\mathrm{e}^{t}-\mathrm{e}^{2t}\bigr)\cdot\varepsilon(t)$, $\bigl(\mathrm{e}^{t}-\mathrm{e}^{2t}\bigr)\cdot\varepsilon(-t)$ und $\mathrm{e}^{t}\cdot\varepsilon(-t)-\mathrm{e}^{2t}\cdot\varepsilon(t)$: Die Pole $-1$ und $-2$ werden zu den Exponenten $+1$ und $+2$, weil im Laplace-Integral der Faktor $\mathrm{e}^{-pt}$ steht.
:::
:::karte begriff Faltungssatz
Was besagt der Faltungssatz der Laplace-Transformation, und für welche $p$ gilt er?
---
Aus der Faltung im Zeitbereich wird ein Produkt im Bildbereich: $\mathcal{L}\{s(t)*h(t)\}=S(p)\cdot H(p)$. Er gilt für alle $p$, die in den Konvergenzbereichen von $S$ und von $H$ liegen.
--- falsch
Aus dem Produkt im Zeitbereich wird eine Faltung im Bildbereich: $\mathcal{L}\{s(t)\cdot h(t)\}=S(p)*H(p)$. Er gilt für alle $p$, die in mindestens einem der beiden Konvergenzbereiche liegen.
--- falsch
Aus der Faltung im Zeitbereich wird eine Summe im Bildbereich: $\mathcal{L}\{s(t)*h(t)\}=S(p)+H(p)$. Er gilt für alle $p$, die in den Konvergenzbereichen von $S$ und von $H$ liegen.
--- falsch
Aus der Faltung im Zeitbereich wird ein Produkt im Bildbereich: $\mathcal{L}\{s(t)*h(t)\}=S(p)\cdot H(p)$. Er gilt aber nur, wenn $s(t)$ eine Eigenfunktion $\mathrm{e}^{pt}$ ist, für andere Signale nicht.
:::
:::karte herleitung Faltungssatz durch Vertauschen der Integrale
Wie folgt der Faltungssatz $\mathcal{L}\{s(t)*h(t)\}=S(p)\cdot H(p)$, wenn man das Faltungsintegral in die Laplace-Transformation einsetzt?
---
Man setzt das Faltungsintegral ein, weil $s*h$ das zu transformierende Signal ist: $\mathcal{L}\{s*h\}=\int_{-\infty}^{\infty}\Bigl[\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau\Bigr]\mathrm{e}^{-pt}\,\mathrm{d} t$.
---
Man vertauscht die Reihenfolge der Integrationen, weil das Doppelintegral absolut konvergiert, wenn $p$ in beiden Konvergenzbereichen liegt.
---
Im inneren Integral über $t$ substituiert man $u=t-\tau$, weil bei festem $\tau$ dann $\mathrm{d} t=\mathrm{d} u$ ist, und zerlegt $\mathrm{e}^{-pt}=\mathrm{e}^{-p\tau}\,\mathrm{e}^{-pu}$, weil $t$ die Summe von $\tau$ und $u$ ist.
---
Das innere Integral $\int_{-\infty}^{\infty}h(u)\,\mathrm{e}^{-pu}\,\mathrm{d} u$ ist $H(p)$, weil es nicht mehr von $\tau$ abhängt. Übrig bleibt $\int_{-\infty}^{\infty}s(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau\cdot H(p)=S(p)\,H(p)$.
:::
:::karte zusammenhang Warum gerade ein Produkt
Warum wird aus der Faltung, die im Zeitbereich jeden Ausgangswert mit allen Eingangswerten koppelt, im Bildbereich ein einfaches Produkt?
---
$S(p)$ beschreibt den Eingang im Koordinatensystem der Funktionen $\mathrm{e}^{pt}$, und $H(p)$ ist der Eigenwert, mit dem das System jede von ihnen multipliziert. Im Bildbereich gibt es deshalb keine Kopplung mehr: Jede Stelle $p$ wird für sich mit ihrem Eigenwert multipliziert.
--- falsch
Weil die Transformation die Zeitachse so stark staucht, dass alle Eingangswerte praktisch zur selben Zeit liegen. Dann schrumpft das Faltungsintegral auf ein einziges Produkt, und die Kopplung zwischen den einzelnen Zeitpunkten fällt weg.
--- falsch
$S(p)$ beschreibt den Eingang im Koordinatensystem der Funktionen $\mathrm{e}^{pt}$. Das System koppelt im Bildbereich zwar weiterhin alle Stellen $p$ miteinander, aber diese Kopplung ist so schwach, dass man sie vernachlässigen darf; übrig bleibt das Produkt.
--- falsch
Weil Faltung und Multiplikation dasselbe sind, sobald man mit komplexen Zahlen rechnet. Im Zeitbereich rechnet man nur mit reellen Signalen, deshalb erscheint dort die Faltung; der Bildbereich lässt die Rechnung in komplexer Form unmittelbar zu.
:::
:::karte formel Ableiten im Zeitbereich
Was wird aus der $n$-fachen Ableitung eines Signals im Bildbereich, und warum hat der Differenzierer den Eigenwert $p$?
---
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\longleftrightarrow p^n\,S(p)$; der Konvergenzbereich ist mindestens der von $S(p)$. Der Differenzierer hat die Impulsantwort $\delta'(t)$, und wegen $\mathrm{e}^{pt}*\delta'(t)=\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ ist sein Eigenwert $p$, also $\mathcal{L}\{\delta'(t)\}=p$.
--- falsch
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\longleftrightarrow\frac{1}{p^n}\,S(p)$, zusätzlich $\operatorname{Re} p>0$. Der Differenzierer hat die Impulsantwort $\varepsilon(t)$, und wegen $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ ist sein Eigenwert $1/p$, für jede Ableitung einmal.
--- falsch
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\longleftrightarrow n\,p\,S(p)$; der Konvergenzbereich bleibt gleich. Der Differenzierer hat die Impulsantwort $\delta'(t)$, und jede weitere Ableitung addiert noch einmal den Eigenwert $p$, weil die Transformation linear ist und sich die Beiträge summieren.
--- falsch
$\frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\longleftrightarrow p^n\,S(p)$, aber nur für $\operatorname{Re} p>0$. Der Differenzierer hat die Impulsantwort $\delta(t)$, weil der Dirac-Impuls die Ableitung des Sprungs ist; deshalb ist sein Eigenwert $p$, und jede Ableitung braucht einen eigenen Sprung.
:::
:::karte formel Integrieren im Zeitbereich
Was wird aus dem Integral $\int_{-\infty}^{t}s(\tau)\,\mathrm{d}\tau$ im Bildbereich, und welche Bedingung kommt hinzu?
---
$\frac1p\,S(p)$: Der Integrator hat die Impulsantwort $\varepsilon(t)$ mit $\mathcal{L}\{\varepsilon(t)\}=1/p$, und nach dem Faltungssatz wird mit dieser Transformierten multipliziert. Der Konvergenzbereich ist mindestens der Durchschnitt des Bereichs von $S(p)$ mit der Halbebene $\operatorname{Re} p>0$.
--- falsch
$p\,S(p)$: Der Integrator hat die Impulsantwort $\delta'(t)$ mit $\mathcal{L}\{\delta'(t)\}=p$, und nach dem Faltungssatz wird mit dieser Transformierten multipliziert. Der Konvergenzbereich bleibt derselbe wie der von $S(p)$, eine Bedingung kommt nicht hinzu.
--- falsch
$\frac1p\,S(p)$: Der Integrator hat die Impulsantwort $\varepsilon(t)$ mit $\mathcal{L}\{\varepsilon(t)\}=1/p$. Der Konvergenzbereich ist der Durchschnitt des Bereichs von $S(p)$ mit der Halbebene $\operatorname{Re} p<0$, weil dort die Vergangenheit des Signals abklingt und das Integral endlich bleibt.
--- falsch
$S(p)-\frac1p$: Das Integral zieht vom Signal den Sprung ab, mit dem es beginnt, und es gilt $\mathcal{L}\{\varepsilon(t)\}=1/p$. Der Konvergenzbereich ist mindestens der Durchschnitt des Bereichs von $S(p)$ mit der Halbebene $\operatorname{Re} p>0$.
:::
:::karte zusammenhang Bedingung beim Integrieren
Warum kommt beim Integrieren im Zeitbereich die Bedingung $\operatorname{Re} p>0$ hinzu, beim Ableiten aber keine?
---
Der Integrator macht aus $\mathrm{e}^{pt}$ den Ausgang $\frac{\mathrm{e}^{pt}}{p}$ nur, wenn $\mathrm{e}^{p\tau}$ für $\tau\to-\infty$ verschwindet, also für $\operatorname{Re} p>0$; sonst summiert er aus der Vergangenheit unendlich viel auf. $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ gilt dagegen für jedes $p$.
--- falsch
Weil ein Integral immer eine positive Fläche liefert und deshalb nur für positive $p$ erklärt ist. Beim Ableiten entsteht eine Steigung, die auch negativ sein darf; deshalb gilt die Ableitungsregel in der ganzen $p$-Ebene ohne Einschränkung.
--- falsch
Weil $\frac1p$ bei $p=0$ nicht definiert ist und man deshalb vorsichtshalber die ganze linke Halbebene samt imaginärer Achse ausschließt. Beim Ableiten ist der Eigenwert $p$ überall definiert, deshalb entfällt dort jede Bedingung.
--- falsch
Weil ein Integrator nur bei Gleichspannung arbeitet und alle Schwingungen mit $\operatorname{Re} p\le0$ herausfiltert. Beim Ableiten werden Schwingungen dagegen verstärkt, deshalb ist dort jedes $p$ zugelassen, auch auf der imaginären Achse.
:::
:::karte zusammenhang Transformierte des Dirac-Impulses
Warum muss nach dem Faltungssatz $\mathcal{L}\{\delta(t)\}=1$ für alle $p$ gelten?
---
Faltung mit $\delta(t)$ lässt jedes Signal unverändert, $s(t)=s(t)*\delta(t)$. Im Bildbereich heißt das $S(p)=S(p)\cdot\mathcal{L}\{\delta(t)\}$, also muss der Faktor $\mathcal{L}\{\delta(t)\}$ gleich 1 sein, und zwar für alle $p$.
--- falsch
Faltung mit $\delta(t)$ verschiebt jedes Signal um eine Zeiteinheit. Im Bildbereich heißt das $S(p)\,\mathrm{e}^{-p}$, und für kleine $p$ ist dieser Faktor ungefähr 1; die Gleichung $\mathcal{L}\{\delta(t)\}=1$ ist also nur eine Näherung.
--- falsch
Weil der Dirac-Impuls die Fläche 1 hat und die Laplace-Transformation an jeder Stelle $p$ die Fläche des Signals angibt. Das gilt für jedes Signal: $S(p)$ ist stets gleich $\int s(t)\,\mathrm{d} t$, unabhängig von $p$.
--- falsch
Faltung mit $\delta(t)$ liefert die Impulsantwort des Systems, und die ist für ein System ohne Bauteile gleich 1. Im Bildbereich heißt das $H(p)=1$; der Faktor gilt aber nur für $\operatorname{Re} p>0$, weil der Impuls rechtsseitig ist.
:::
::::
