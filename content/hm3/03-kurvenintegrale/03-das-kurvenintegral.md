---
title: Stufe 2: Das Kurvenintegral
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Kurvenintegrale
adresse: elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale
knoten: Kapitel 3: Kurvenintegrale
order: 3130300
summary: Ein Vektorfeld liefert an jedem Ort einen Vektor, eine Kurve eine Laufrichtung.
tags: Kurvenintegral, Arbeit, Komposition, orientierte Einheitstangentialvektor, orientiertes Linienelement, Integral über die Bogenlänge
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Vektorfeld liefert an jedem Ort einen Vektor, eine Kurve eine Laufrichtung. Diese Stufe macht aus beidem eine einzige Zahl und gibt ihr eine Bedeutung.
:::

**Die Idee.** Läuft ein Punkt durch ein Feld, zählt an jedem Ort nur, wie stark das Feld in Laufrichtung zeigt. Das Skalarprodukt $\boldsymbol{F}\cdot\dot\gamma$ misst genau das, und man summiert diese Zahl über die Laufzeit (Abb. [2](#abb-2)).

:::abbildung hm3/k3integral 2
Vier Stellen einer Kurve mit Wegstück $\Delta\boldsymbol{x}$ (grün) und Feld $\boldsymbol{F}$ (blau). Zählen wird nur der Anteil von $\boldsymbol{F}$ in Wegrichtung (rot an der schrägen Stelle). Parallel zählt das Feld voll, quer gar nicht, entgegen negativ.
:::

:::definition Definition 2.1 (Kurvenintegral)
<span class="anker" id="satz-2-1"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen, $\gamma:[a,b]\to\mathcal U$ regulär parametrisiert und $\boldsymbol{F}$ ein stetiges Vektorfeld auf $\mathcal U$. Dann heißt

<span class="anker" id="gl-2-1"></span>
$$\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}:=\int_a^b\boldsymbol{F}(\gamma(t))\cdot\dot\gamma(t)\,\mathrm{d} t \tag{2.1}$$

das __Kurvenintegral__ von $\boldsymbol{F}$ längs $\gamma$. Hat $\gamma$ Knicke, ist genauer $\sum_{k=1}^N\int_{t_{k-1}}^{t_k}\boldsymbol{F}(\gamma(t))\cdot\dot\gamma(t)\,\mathrm{d} t$ gemeint, wobei $\gamma$ auf jedem $[t_{k-1},t_k]$ stetig differenzierbar ist. Formal ist $\mathrm{d}\boldsymbol{x}=\dot\gamma(t)\,\mathrm{d} t$.
:::

⁠**So liest man das:** $\mathrm{d}\boldsymbol{x}$ ist ein kleines Wegstück, also ein Vektor. Das Ergebnis ist eine reelle Zahl. Das Feld muss nur längs der Kurve erklärt sein, es genügt, dass $t\mapsto\boldsymbol{F}(\gamma(t))$ stetig ist. Ist $\boldsymbol{F}$ ein Kraftfeld, ist die Zahl die __Arbeit__, die das Feld an einem Teilchen längs $\gamma$ von $\gamma(a)$ nach $\gamma(b)$ verrichtet.

:::frage Wie kann man sich ein Kurvenintegral für Vektorfelder vorstellen?
Zerlege die Kurve in kleine Stücke mit den Wegvektoren $\Delta\boldsymbol{x}$. Auf jedem Stück zählt nur der Anteil von $\boldsymbol{F}$ längs des Wegs:

$$\boldsymbol{F}\cdot\Delta\boldsymbol{x}=|\boldsymbol{F}|\,|\Delta\boldsymbol{x}|\cos\vartheta,$$

wobei $\vartheta$ der Winkel zwischen $\boldsymbol{F}$ und $\Delta\boldsymbol{x}$ ist. Parallel zum Weg zählt das Feld voll, quer zum Weg gar nicht ($\vartheta=90^\circ$), entgegen dem Weg negativ. Summiert man alle Stücke und verfeinert die Zerlegung, entsteht das Integral. Die Kurve muss dabei im Definitionsbereich von $\boldsymbol{F}$ liegen, sonst fehlt an manchen Stellen der Vektor.

⁠**Beispiel:** Auf eine Ladung $q$ im elektrostatischen Feld $\boldsymbol{E}$ wirkt die Kraft $\boldsymbol{F}=q\boldsymbol{E}$. Das Integral $\int_\gamma\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{x}$ ist noch keine Arbeit, sondern eine Spannung. Erst $q\int_\gamma\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{x}$ ist die Arbeit des Felds. Läuft $\gamma$ von $A$ nach $B$, ist $W=q\,(\varphi(A)-\varphi(B))$ mit dem elektrischen Potential $\varphi$, für das in der Elektrotechnik $\boldsymbol{E}=-\nabla\varphi$ gilt.

Ein freies Teilchen folgt seiner Bahn von selbst. Läuft es einen vorgegebenen Weg, muss etwas anderes es führen, etwa eine Schiene. Das Integral liefert trotzdem die Arbeit des Felds, nicht die der Führung.
:::

**Beispiel.** Längs des Viertelkreises ist $\boldsymbol V(\kappa(t))=(-\sin t,\cos t)=\dot\kappa(t)$, also $\boldsymbol V\cdot\dot\kappa=1$ und $\int_\kappa\boldsymbol V\cdot\mathrm{d}\boldsymbol{x}=\int_0^{\pi/2}1\,\mathrm{d} t=\pi/2$. Das Feld zeigt überall in Laufrichtung und hat die Länge 1, also kommt die Weglänge heraus. **Grenzfall:** $\boldsymbol G(\kappa(t))=2\kappa(t)$ steht überall quer zum Kreis. Tatsächlich ist $\boldsymbol G\cdot\dot\kappa=-2\cos t\sin t+2\sin t\cos t=0$, und das Integral ist null.

**Rechenregeln.** Weil Skalarprodukt und Integral linear sind, gilt für Zahlen $\lambda,\mu$

<span class="anker" id="gl-2-2"></span>
$$\int_\gamma(\lambda\boldsymbol{F}_1+\mu\boldsymbol{F}_2)\cdot\mathrm{d}\boldsymbol{x}=\lambda\int_\gamma\boldsymbol{F}_1\cdot\mathrm{d}\boldsymbol{x}+\mu\int_\gamma\boldsymbol{F}_2\cdot\mathrm{d}\boldsymbol{x}. \tag{2.2}$$

Sind $\gamma_1:[a,b]\to\mathbb{R}^n$ und $\gamma_2:[c,d]\to\mathbb{R}^n$ regulär parametrisiert mit $\gamma_1(b)=\gamma_2(c)$, ist auch die __Komposition__

$$\gamma_1\oplus\gamma_2:[a,\,b+d-c]\to\mathbb{R}^n,\qquad(\gamma_1\oplus\gamma_2)(t):=\begin{cases}\gamma_1(t)&t\in[a,b]\\\gamma_2(c-b+t)&t\in(b,\,b+d-c]\end{cases}$$

regulär parametrisiert, erst läuft $\gamma_1$, dann $\gamma_2$. Das Integral teilt sich auf: $\int_{\gamma_1\oplus\gamma_2}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\gamma_1}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}+\int_{\gamma_2}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$. Damit zerlegt man Streckenzüge in gerade Stücke und jede regulär parametrisierte Kurve in einfache Stücke. Doppelpunkte stören beim Integrieren also nicht.

**Mit dem Linienelement.** Der __orientierte Einheitstangentialvektor__ $\boldsymbol{t}(\gamma(t))=\dot\gamma(t)/|\dot\gamma(t)|$ hat die Länge 1 und zeigt in Laufrichtung. Er ist ein stückweise stetiges Feld längs der Kurve, an Knickstellen gilt die rechtsseitige Ableitung. Mit dem Linienelement $\mathrm{d} s$ wird $\mathrm{d}\boldsymbol{x}=\boldsymbol{t}\,\mathrm{d} s$, weshalb $\mathrm{d}\boldsymbol{x}$ auch __orientiertes Linienelement__ heißt. Damit ist

<span class="anker" id="gl-2-3"></span>
$$\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_\gamma\boldsymbol{F}\cdot\boldsymbol{t}\;\mathrm{d} s, \tag{2.3}$$

also Tangentialanteil mal Weglänge, summiert. Für eine stetige skalare Funktion $f$ heißt $\int_\gamma f\,\mathrm{d} s:=\int_a^bf(\gamma(t))\,|\dot\gamma(t)|\,\mathrm{d} t$ das __Integral über die Bogenlänge__. Für $f=1$ ist es die Länge, $\mathcal L(\gamma)=\int_\gamma\mathrm{d} s$.

:::satz Satz 2.2 (Standardabschätzung)
<span class="anker" id="satz-2-2"></span>

Für ein längs $\gamma$ stetiges Vektorfeld gilt $\displaystyle\Bigl|\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}\Bigr|\le\sup_{\boldsymbol{x}\in\Gamma}|\boldsymbol{F}(\boldsymbol{x})|\;\mathcal L(\gamma)$.
:::

:::beweis Standardabschätzung
Mit [(2.3)](#gl-2-3), der Dreiecksungleichung für Integrale und Cauchy-Schwarz mit $|\boldsymbol{t}|=1$ gilt $\bigl|\int_\gamma\boldsymbol{F}\cdot\boldsymbol{t}\,\mathrm{d} s\bigr|\le\int_\gamma|\boldsymbol{F}\cdot\boldsymbol{t}|\,\mathrm{d} s\le\int_\gamma|\boldsymbol{F}|\,\mathrm{d} s\le\sup_\Gamma|\boldsymbol{F}|\int_\gamma\mathrm{d} s$.
:::

⁠**Kontrolle:** Für $\boldsymbol V$ auf dem Viertelkreis steht Gleichheit, $\pi/2=1\cdot\pi/2$, weil das Feld parallel zum Weg läuft und überall gleich lang ist.

:::aufgabe Aufgabe 2 ★ Zwei Wege, zwei Werte
<span class="anker" id="aufg-2"></span>

Sei $\boldsymbol{F}(x,y)=(y,\,x^2)$.

<ol class="al">

<li>

Berechne das Kurvenintegral längs der Strecke von $(0,0)$ nach $(3,4)$.

</li>

<li>

Berechne es längs des Streckenzugs $(0,0)\to(3,0)\to(3,4)$.

</li>

<li>

Prüfe (a) mit der Standardabschätzung.

</li>

</ol>

:::loesung
(a) $\gamma(t)=(3t,4t)$, $0\le t\le1$: $\boldsymbol{F}\cdot\dot\gamma=(4t,9t^2)\cdot(3,4)=12t+36t^2$, das Integral ist $6+12=18$. (b) Auf dem ersten Stück ist $y=0$ und $\mathrm{d} y=0$, also null. Auf dem zweiten ist $x=3$, $\mathrm{d} x=0$: $\int_0^49\,\mathrm{d} y=36$. Die Komposition ergibt $36$, also einen anderen Wert als in (a). (c) Auf der Strecke ist $|\boldsymbol{F}|^2=16t^2+81t^4\le97$ und $\mathcal L=5$, also $18\le5\sqrt{97}\approx49{,}2$.
:::
:::
