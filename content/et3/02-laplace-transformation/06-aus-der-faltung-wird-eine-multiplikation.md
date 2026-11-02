---
title: Stufe 3: Aus der Faltung wird eine Multiplikation
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220600
summary: Stufe 1 sagt, was das System mit einem Baustein macht.
tags: 
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Stufe [1](warum-gerade.html#stufe-1) sagt, was das System mit einem Baustein macht. Stufe [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) sagt, dass jedes Signal aus Bausteinen besteht. Zusammen ergeben sie den wichtigsten Satz der Laplace-Transformation.
:::

**Die Idee.** Ein LTI-System ist linear: Es verarbeitet jeden Baustein des Eingangs für sich und addiert die Ergebnisse. Jeden Baustein $\mathrm{e}^{pt}$ multipliziert es mit $H(p)$. Der Ausgang besteht also aus *denselben* Bausteinen wie der Eingang, nur ist jedes Gewicht mit $H(p)$ multipliziert. Abbildung [4](#abb-4) zeigt die beiden Wege zum Ausgang.

:::abbildung et3/k2wege 4
Zwei Wege vom Eingang zum Ausgang. Oben direkt mit dem Faltungsintegral. Unten: Eingang in Bausteine zerlegen, jedes Gewicht mit $H(p)$ multiplizieren, wieder zusammensetzen. Der untere Weg funktioniert, weil jeder Baustein eine Eigenfunktion ist.
:::

:::satz Satz 3.1 (Faltungssatz)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$g(t)=s(t)*h(t)\quad\Longleftrightarrow\quad G(p)=S(p)\,H(p), \tag{3.1}$$

gültig für alle $p$, die in den Konvergenzbereichen von $S$ und von $H$ liegen.
:::

⁠**So liest man das:** $S(p)$ ist das Gewicht des Bausteins $\mathrm{e}^{pt}$ im Eingang, $H(p)$ der Faktor, mit dem das System diesen Baustein multipliziert, $G(p)$ das Gewicht im Ausgang. Die Bedingung an $p$ kommt daher, dass die Linie der Umkehrformel durch beide Konvergenzbereiche laufen muss: Der Eingang muss in Bausteine zerlegbar sein, und das System muss jeden davon verarbeiten können.

:::herleitung Faltungssatz aus Überlagerung und Eigenfunktion
Man setzt den Eingang als Überlagerung [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) in die Faltung ein, mit einer Linie $\operatorname{Re} p=\sigma$, die in beiden Konvergenzbereichen liegt:

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

Linearität: Die Faltung darf ins Integral, sie wirkt auf jeden Baustein einzeln:

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

Eigenfunktion [(1.1)](warum-gerade.html#gl-1-1): $\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$.

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[S(p)H(p)\bigr]\,\mathrm{e}^{pt}\,\mathrm{d} p.$$

Das ist die Umkehrformel für $g$ mit dem Gewicht $S(p)H(p)$. Da die Gewichte eines Signals eindeutig sind, ist $G(p)=S(p)H(p)$.
:::

⁠**Kurz gesagt:** Die Faltung wird zur Multiplikation, weil das System jeden Baustein $\mathrm{e}^{pt}$ nur mit der Zahl $H(p)$ multipliziert.

:::analogie
Ein Equalizer zerlegt Musik in Frequenzbänder, multipliziert jedes Band mit der Stellung seines Reglers und setzt die Bänder wieder zusammen. Ein LTI-System macht dasselbe mit den Bausteinen $\mathrm{e}^{pt}$, und die Reglerstellung ist $H(p)$. Die Analogie hinkt an zwei Stellen: Ein Equalizer hat endlich viele Bänder mit reellen Reglern. Hier gibt es kontinuierlich viele Bausteine, die auch wachsen oder abklingen können, und jeder „Regler“ ist eine komplexe Zahl, die zusätzlich die Phase verschiebt.
:::

**Derselbe Mechanismus erklärt Ableitung, Integral und Differentialgleichungen.**

<ul>

<li>

⁠**Ableiten.** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$. Der Differenzierer ist ein LTI-System, und jeder Baustein ist seine Eigenfunktion mit dem Eigenwert $p$. Also wird jedes Gewicht mit $p$ multipliziert: $\mathcal{L}\{\dot s\}=p\,S(p)$.

</li>

<li>

⁠**Integrieren.** $\int_{-\infty}^{t}\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$, aber nur für $\operatorname{Re} p>0$, sonst divergiert das Integral bei $-\infty$. Daher $\mathcal{L}\{\int_{-\infty}^t s\,\mathrm{d}\tau\}=S(p)/p$ mit der zusätzlichen Bedingung $\operatorname{Re} p>0$.

</li>

<li>

⁠**Kette.** Zwei Systeme hintereinander multiplizieren nacheinander mit $H_1(p)$ und $H_2(p)$, zusammen mit $H_1H_2$. Die Reihenfolge ist egal, weil Zahlen kommutieren.

</li>

<li>

⁠**Differentialgleichung.** Jede Ableitung wird zum Faktor $p$. Aus einer linearen Differentialgleichung mit konstanten Koeffizienten

$$\sum_{r=0}^{R}\alpha_r\frac{\mathrm{d}^r g}{\mathrm{d} t^r}=\sum_{q=0}^{Q}\beta_q\frac{\mathrm{d}^q s}{\mathrm{d} t^q} \quad\text{wird}\quad \Bigl(\sum_{r}\alpha_rp^r\Bigr)G(p)=\Bigl(\sum_q\beta_qp^q\Bigr)S(p),$$

also eine algebraische Gleichung, und $H(p)=G/S$ ist ein Polynombruch.

</li>

</ul>

**Beispiel: die Sprungantwort des RC-Tiefpasses.** Eingang $\varepsilon(t)$ mit $S(p)=1/p$ ($\operatorname{Re} p>0$), System $H(p)=1/(p+1)$ ($\operatorname{Re} p>-1$). Der gemeinsame Bereich ist $\operatorname{Re} p>0$:

$$G(p)=\frac{1}{p}\cdot\frac{1}{p+1}=\frac1p-\frac{1}{p+1}\quad\Longrightarrow\quad g(t)=\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

Die Rücktransformation der beiden Summanden folgt aus [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) mit $p_0=0$ und $p_0=-1$. Direkt nachgerechnet: $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ für $t>0$. Auch die Umkehrformel [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1), numerisch auf der Linie $\sigma=0{,}5/\mathrm s$ ausgewertet, ergibt $g(0{,}5\,\mathrm{s})=0{,}3935$, $g(1\,\mathrm{s})=0{,}6321$, $g(3\,\mathrm{s})=0{,}9502$ und $g(-1\,\mathrm{s})=0$, genau $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$.

:::ltspice Die Übertragungsfunktion direkt eingeben
⁠**Zeichnen:** das RC-Glied (`1Meg`, `1u`) von `in` nach `rc`. Daneben eine spannungsgesteuerte Spannungsquelle `e`: Steuereingang an `in` und Masse, Ausgang am Netz `lap`, Wert `Laplace=1/(1+s)`. Diese Quelle ist ein LTI-System, das nur durch $H$ gegeben ist: LTspice berechnet daraus selbst die Impulsantwort und faltet den Eingang mit ihr. LTspice schreibt $s$ statt $p$.

⁠**Quelle und Direktive:** `PULSE(0 1 0 1u 1u 100)`, `.tran 0 5 0 1m`.

⁠**Was du siehst:** `V(rc)` und `V(lap)` liegen übereinander (Abstand unter 0,001), auf 0,3935 bei 0,5 s, 0,6321 bei 1 s und 0,9502 bei 3 s. Mit dem Quellwert `AC 1` und `.ac dec 100 0.01 100` zeigt LTspice $H(s)$ für $s=\mathrm{j}2\pi f$, also nur auf der imaginären Achse: $-3{,}0$ dB und $-45^\circ$ bei 0,159 Hz.

⁠**Zu Aufgabe [6](#aufg-6):** Quelle `PWL(0 0 10 10)`, die Rampe $t\,\varepsilon(t)$ bis 10 s, und `.tran 0 10 0 1m`. Vergleiche `V(rc)` mit deinem Ergebnis aus Aufgabe [6](#aufg-6)(b).
:::

:::aufgabe Aufgabe 5 ★★ Kette und Ableitung über die Bausteine
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Begründe mit dem Bausteinbild (ohne Faltungsintegral), warum zwei LTI-Systeme in Kette die Übertragungsfunktion $H_1(p)H_2(p)$ haben. Warum folgt daraus, dass die Faltung kommutativ ist?

</li>

<li>

Leite $\mathcal{L}\{\dot s(t)\}=p\,S(p)$ aus der Umkehrformel her, indem du sie nach $t$ ableitest.

</li>

</ol>

:::loesung
(a) Der Eingang besteht aus Bausteinen $\mathrm{e}^{pt}$ mit Gewichten $S(p)$. Das erste System multipliziert jeden Baustein mit $H_1(p)$, die Gewichte sind danach $H_1S$. Das zweite multipliziert mit $H_2(p)$: $G=H_2H_1S$. Die Kette hat also $H=H_1H_2$. Weil $H_1H_2=H_2H_1$, ist das Ergebnis von der Reihenfolge unabhängig, und da $h_1*h_2$ die Impulsantwort der Kette ist, folgt $h_1*h_2=h_2*h_1$.

(b) Ableiten unter dem Integral wirkt nur auf $\mathrm{e}^{pt}$:

$$\dot s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}\,\mathrm{d} p=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[p\,S(p)\bigr]\mathrm{e}^{pt}\,\mathrm{d} p.$$

Das ist die Umkehrformel mit dem Gewicht $pS(p)$, also $\mathcal{L}\{\dot s\}=pS(p)$.
:::
:::

:::aufgabe Aufgabe 6 ★★ Rampenantwort des RC-Tiefpasses
<span class="anker" id="aufg-6"></span>

Eingang $s(t)=t\,\varepsilon(t)$ mit $S(p)=1/p^2$ für $\operatorname{Re} p>0$, Grundpaar [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5).

<ol class="al">

<li>

Bestimme $G(p)$ und seinen Konvergenzbereich.

</li>

<li>

Prüfe die Zerlegung $G(p)=\frac{1}{p^2}-\frac1p+\frac{1}{p+1}$ und bestimme $g(t)$.

</li>

<li>

Kontrolle: Was ist $g(0)$, und warum muss das so sein? Was ist $\dot g(t)$?

</li>

<li>

Wie verhält sich $g(t)$ für $t\gg1$ s? Vergleiche mit Aufgabe [1](warum-gerade.html#aufg-1)c.

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$ für $\operatorname{Re} p>0$ (Durchschnitt aus $\operatorname{Re} p>0$ und $\operatorname{Re} p>-1$).

(b) Auf den Hauptnenner: $\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$. Rücktransformation mit [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5) und [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2):

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$: Die Kondensatorspannung kann nicht springen, und der Eingang startet bei null. $\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$, genau die Sprungantwort. Das passt: Die Rampe ist das Integral des Sprungs, also ist die Rampenantwort das Integral der Sprungantwort.

(d) Für $t\gg1$ s ist $\mathrm{e}^{-t}\approx0$ und $g(t)\approx t-1$: Der Ausgang folgt der Rampe mit einer Verzögerung von $RC=1$ s, genau wie bei der zweiseitigen Rampe in Aufgabe [1](warum-gerade.html#aufg-1)c. Der Unterschied ist der Baustein $\mathrm{e}^{-t}$ (Pol $-1$ des Systems): der Einschwingvorgang, weil die Rampe hier erst bei $t=0$ beginnt.
:::
:::
