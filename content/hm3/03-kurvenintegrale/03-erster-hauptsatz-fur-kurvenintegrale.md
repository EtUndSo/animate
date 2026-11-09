---
title: Erster Hauptsatz für Kurvenintegrale
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130300
summary: Längs zweier Wege mit gleichem Start und Ziel hat das Kurvenintegral im Allgemeinen verschiedene Werte.
tags: wegzusammenhängend, Gebiet, wegunabhängig, konservativ, Spannung, integrabel, Wirbelfeld
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Längs zweier Wege mit gleichem Start und Ziel hat das Kurvenintegral im Allgemeinen verschiedene Werte. Dieser Abschnitt sucht die Felder, bei denen es nur auf Start und Ziel ankommt, und zeigt, dass es genau die Gradientenfelder sind. Am Ende steht ein Feld, das alle Integrabilitätsbedingungen erfüllt und trotzdem nicht dazugehört.
:::

### Was du dafür brauchst: der Mittelwertsatz der Integralrechnung

<span class="anker" id="stufe-2-1"></span>

Der Mittelwert einer stetigen Funktion über ein kurzes Intervall wird an einer Stelle des Intervalls tatsächlich angenommen. Das braucht ein Beweis in diesem Abschnitt.

:::satz Satz 2.1 (Mittelwertsatz der Integralrechnung)
<span class="anker" id="satz-2-1"></span>

Ist $g$ stetig auf einem Intervall, das $0$ und eine Zahl $\eta\neq0$ enthält, dann gibt es eine Stelle $\vartheta$ zwischen $0$ und $\eta$ mit

$$\frac1\eta\int_0^\eta g(t)\,\mathrm{d} t=g(\vartheta).$$
:::

:::beweis Aus dem Mittelwertsatz der Differentialrechnung
Sei $G(s)=\int_0^sg(t)\,\mathrm{d} t$. Nach dem Hauptsatz ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) ist $G$ differenzierbar mit $G'=g$. Der Mittelwertsatz der Differentialrechnung ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) liefert eine Zwischenstelle $\vartheta$ mit $\frac{G(\eta)-G(0)}\eta=G'(\vartheta)=g(\vartheta)$, und links steht $\frac1\eta\int_0^\eta g\,\mathrm{d} t$.
:::

::::beispiel
Für $g(t)=t^2$ und $\eta=3$ ist $\frac13\int_0^3t^2\,\mathrm{d} t=3$. Die Stelle mit $g(\vartheta)=3$ ist $\vartheta=\sqrt3\approx1{,}73$, und sie liegt zwischen $0$ und $3$.
::::

⁠**Kurz gesagt:** Eine stetige Funktion nimmt ihren Mittelwert über ein Intervall an einer Stelle dieses Intervalls an.

### Gebiete

<span class="anker" id="stufe-2-2"></span>

Um zu fragen, ob ein Kurvenintegral nur von Start und Ziel abhängt, muss man je zwei Punkte durch Wege verbinden können, die im Definitionsbereich des Felds bleiben. Mengen, in denen das geht, bekommen einen Namen.

Abb. [7](#abb-7) zeigt links eine Hantel: zwei Scheiben, durch einen Steg verbunden. Jeder Punkt der einen Scheibe lässt sich mit jedem Punkt der anderen durch einen Weg verbinden, der in der Menge bleibt. Rechts berühren sich zwei offene Kreisscheiben in einem Punkt, der selbst zu keiner von beiden gehört. Von der einen Scheibe in die andere gibt es keinen Weg.

:::abbildung hm3/k3gebiet 7
Links eine offene Hantel: Zwei Scheiben, durch einen Steg verbunden, gestrichelt der Rand, der nicht dazugehört. Der rote Weg verbindet zwei Punkte und bleibt in der Menge. Rechts zwei offene Kreisscheiben, die sich in einem Punkt berühren. Dieser Punkt (weißer Kreis) gehört zu keiner der beiden; deshalb führt kein Weg von der einen Scheibe in die andere.
:::

Eine Menge $M\subset\mathbb{R}^n$ heißt __wegzusammenhängend__, wenn sich je zwei ihrer Punkte durch eine regulär parametrisierte Kurve verbinden lassen, die ganz in $M$ verläuft.

:::definition Definition 2.2 (Gebiet)
<span class="anker" id="satz-2-2"></span>

Ein __Gebiet__ ist eine offene, wegzusammenhängende Menge $\mathcal G\subset\mathbb{R}^n$.
:::

::::beispiel
Der ganze $\mathbb{R}^n$ und jede offene Kugel sind Gebiete: Die Strecke zwischen zwei Punkten bleibt in ihnen. Die Ebene ohne den Nullpunkt, $\mathbb{R}^2\setminus\{0\}$, ist ein Gebiet: Zwei Punkte verbindet man, indem man vom ersten aus auf einem Kreisbogen um den Nullpunkt bis zur Richtung des zweiten läuft und dann radial nach innen oder außen; sind beide Teilstücke nicht leer, ist das ein Streckenzug mit einem Knick, also regulär. Die Menge $\{(x,y):x\neq0\}$ ist offen, aber kein Gebiet. Jeder Weg von $(-1,0)$ nach $(1,0)$ hat eine erste Komponente, die stetig von $-1$ nach $1$ läuft und deshalb nach dem Zwischenwertsatz irgendwo null wird. Dort verlässt der Weg die Menge.
::::

⁠**Kurz gesagt:** Ein Gebiet ist offen und an einem Stück: Je zwei Punkte lassen sich durch einen Weg in ihm verbinden.

### Wegunabhängige Kurvenintegrale und konservative Felder

<span class="anker" id="stufe-2-3"></span>

Unterabschnitt [1.8](integration-langs-regularer-kurven.html#stufe-1-8) hat für das Drehfeld $\boldsymbol V$ längs zweier Wege von $(1,0)$ nach $(0,1)$ die Werte $\frac\pi2$ und $1$ ergeben, Unterabschnitt [1.14](integration-langs-regularer-kurven.html#stufe-1-14) längs eines dritten Wegs den Wert $0$. Für das Strahlfeld $\boldsymbol S$ ergaben dieselben Wege beide Male $0$. Welche Felder liefern für jeden Weg zwischen zwei Punkten dieselbe Zahl?

Abb. [8](#abb-8) stellt die beiden Felder nebeneinander. Links umkreist das Feld den Nullpunkt, und der Kreisbogen läuft mit ihm, die Strecke schneidet es schräg. Rechts zeigt das Feld vom Nullpunkt weg, und auf dem Kreisbogen steht es überall quer.

:::abbildung hm3/k3wege 8
Dieselben zwei Wege von $A=(1,0)$ nach $B=(0,1)$ in zwei Feldern: blau der Viertelkreis $\kappa$, rot die Strecke $\sigma$. Links das Drehfeld $\boldsymbol V$, dort hängt das Integral vom Weg ab. Rechts das Strahlfeld $\boldsymbol S$, dort ist es auf beiden Wegen null.
:::

:::definition Definition 2.3 (Wegunabhängigkeit, konservatives Feld)
<span class="anker" id="satz-2-3"></span>

Sei $\mathcal G\subset\mathbb{R}^n$ ein Gebiet und $\boldsymbol{F}\colon\mathcal G\to\mathbb{R}^n$ ein stetiges Vektorfeld. Das Kurvenintegral von $\boldsymbol{F}$ heißt __wegunabhängig__ in $\mathcal G$, wenn

$$\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\Gamma'}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$$

für alle regulären Kurven $\Gamma,\Gamma'$ in $\mathcal G$ mit gleichem Anfangs- und gleichem Endpunkt gilt. Ein stetiges Vektorfeld mit wegunabhängigen Kurvenintegralen heißt __konservativ__ in $\mathcal G$.
:::

⁠**So liest man das:** Bei einem konservativen Feld darf man $\int_{\boldsymbol{x}_0}^{\boldsymbol{x}_1}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ schreiben, ohne den Weg zu nennen. Die Bedingung betrifft *alle* Wege, die im Gebiet bleiben. Ein einziges Paar von Wegen mit verschiedenen Werten zeigt, dass ein Feld nicht konservativ ist; gleiche Werte auf einigen Wegen beweisen dagegen nichts.

::::beispiel
Das Drehfeld $\boldsymbol V$ ist auf $\mathbb{R}^2$ nicht konservativ, denn $\kappa$ und $\sigma$ haben denselben Start und dasselbe Ziel, aber die Werte $\frac\pi2$ und $1$. Ob das Strahlfeld konservativ ist, entscheiden die beiden Wege allein nicht; das klärt Unterabschnitt [2.5](#stufe-2-5).
::::

⁠**Kurz gesagt:** Ein Feld ist konservativ, wenn sein Kurvenintegral nur von Anfangs- und Endpunkt abhängt.

### Rundwege

<span class="anker" id="stufe-2-4"></span>

Statt alle Paare von Wegen zu vergleichen, kann man eine einfachere Frage stellen: Was ergibt das Kurvenintegral längs eines Wegs, der zum Start zurückführt?

Zwei Wege $\Gamma$ und $\Gamma'$ von $A$ nach $B$ lassen sich zu einem Rundweg zusammensetzen: auf $\Gamma$ hin und auf $\Gamma'$ zurück. Nach [(1.8)](integration-langs-regularer-kurven.html#gl-1-8) ist sein Integral die Differenz der beiden Wegintegrale.

:::satz Satz 2.4 (Konservativ heißt: Rundwege ergeben null)
<span class="anker" id="satz-2-4"></span>

Ein stetiges Vektorfeld $\boldsymbol{F}$ auf einem Gebiet $\mathcal G\subset\mathbb{R}^n$ ist genau dann konservativ, wenn

$$\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=0$$

für alle geschlossenen regulären Kurven $\Gamma$ in $\mathcal G$ gilt.
:::

:::beweis Hin und zurück
„$\Leftarrow$“: Haben $\Gamma$ und $\Gamma'$ denselben Anfangs- und Endpunkt, dann ist $\Gamma-\Gamma'$ geschlossen. Nach Voraussetzung und [(1.8)](integration-langs-regularer-kurven.html#gl-1-8) ist $0=\int_{\Gamma-\Gamma'}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}-\int_{\Gamma'}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$. Also ist das Feld konservativ.

„$\Rightarrow$“: Sei $\Gamma$ geschlossen. Man zerlegt $\Gamma$ an einem zweiten Punkt $Q$ in zwei Stücke, $\Gamma=\Gamma'+\Gamma''$, wobei $\Gamma'$ vom Anfangspunkt $P$ nach $Q$ läuft und $\Gamma''$ von $Q$ zurück nach $P$. Dann laufen $\Gamma'$ und $-\Gamma''$ beide von $P$ nach $Q$. Weil $\boldsymbol{F}$ konservativ ist, gilt $\int_{\Gamma'}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{-\Gamma''}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=-\int_{\Gamma''}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ nach [(1.5)](integration-langs-regularer-kurven.html#gl-1-5). Also ist $\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\Gamma'}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}+\int_{\Gamma''}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=0$.
:::

Das Wort *konservativ* kommt von der Energie: Auf einem Rundweg gewinnt ein Teilchen in einem konservativen Kraftfeld insgesamt nichts und verliert nichts, die Energie bleibt erhalten.

::::beispiel
Der Rundweg $\kappa-\sigma$ läuft auf dem Viertelkreis von $(1,0)$ nach $(0,1)$ und auf der Strecke zurück. Für das Drehfeld ergibt er $\frac\pi2-1\approx0{,}571\neq0$. Auch daran sieht man, dass $\boldsymbol V$ nicht konservativ ist.
::::

⁠**Kurz gesagt:** Ein Feld ist genau dann konservativ, wenn sein Kurvenintegral über jeden Rundweg null ist.

### Der erste Hauptsatz

<span class="anker" id="stufe-2-5"></span>

Für eine Funktion einer Variablen sagt der Hauptsatz der Differential- und Integralrechnung $\int_a^bf'(t)\,\mathrm{d} t=f(b)-f(a)$: Integriert man eine Ableitung, bleiben nur die Randwerte übrig. Gibt es dasselbe für Kurvenintegrale?

Das Gegenstück zur Ableitung ist der Gradient. Ist das Feld der Gradient einer Funktion $\varphi$, dann ist jeder Summand $\boldsymbol{F}\cdot\Delta\boldsymbol{x}$ nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) ungefähr die Änderung von $\varphi$ längs des Wegstücks. Die Summe dieser Änderungen ist die Gesamtänderung zwischen Start und Ziel.

:::satz Satz 2.5 (Erster Hauptsatz für Kurvenintegrale)
<span class="anker" id="satz-2-5"></span>

Sei $\mathcal G\subset\mathbb{R}^n$ ein Gebiet.

<ol class="rm">

<li>

Ist $\varphi\colon\mathcal G\to\mathbb{R}$ stetig differenzierbar und $\boldsymbol{F}=\nabla\varphi$, dann gilt für jede regulär parametrisierte Kurve $\gamma\colon[a,b]\to\mathcal G$ mit $\gamma(a)=\boldsymbol{x}_0$ und $\gamma(b)=\boldsymbol{x}_1$

<span class="anker" id="gl-2-1"></span>
$$\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\varphi(\boldsymbol{x}_1)-\varphi(\boldsymbol{x}_0). \tag{2.1}$$

</li>

<li>

Ist $\boldsymbol{F}\colon\mathcal G\to\mathbb{R}^n$ stetig, dann gilt: $\boldsymbol{F}$ ist genau dann konservativ in $\mathcal G$, wenn $\boldsymbol{F}$ ein Gradientenfeld in $\mathcal G$ ist.

</li>

</ol>
:::

:::beweis Teil (i): Kettenregel und Hauptsatz
Nach der Ableitung längs einer Kurve ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)), einer Folge der Kettenregel, ist

$$\frac{\mathrm{d}}{\mathrm{d} t}\,\varphi\bigl(\gamma(t)\bigr)=\nabla\varphi\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)=\boldsymbol{F}\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t).$$

Der Integrand des Kurvenintegrals ist also die Ableitung der Funktion $t\mapsto\varphi(\gamma(t))$. Auf jedem glatten Stück $[a_{k-1},a_k]$ gibt der Hauptsatz ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) $\int_{a_{k-1}}^{a_k}\boldsymbol{F}(\gamma)\cdot\dot\gamma\,\mathrm{d} t=\varphi(\gamma(a_k))-\varphi(\gamma(a_{k-1}))$. Summiert man über $k$, heben sich alle Zwischenwerte auf, und es bleibt $\varphi(\gamma(b))-\varphi(\gamma(a))=\varphi(\boldsymbol{x}_1)-\varphi(\boldsymbol{x}_0)$.
:::

:::beweis Teil (ii): das Potential als angesammeltes Kurvenintegral
„$\Leftarrow$“: Ist $\boldsymbol{F}=\nabla\varphi$ mit stetigem $\boldsymbol{F}$, dann ist $\varphi$ stetig differenzierbar, und nach (i) hängt das Integral nur von $\boldsymbol{x}_0$ und $\boldsymbol{x}_1$ ab.

„$\Rightarrow$“: Sei $\boldsymbol{F}$ konservativ. Man hält einen Punkt $\boldsymbol{x}_0\in\mathcal G$ fest. Weil $\mathcal G$ ein Gebiet ist, lässt sich jeder Punkt $\boldsymbol{x}\in\mathcal G$ mit $\boldsymbol{x}_0$ durch eine reguläre Kurve $\Gamma(\boldsymbol{x})$ in $\mathcal G$ verbinden. Man setzt

$$\varphi(\boldsymbol{x}):=\int_{\Gamma(\boldsymbol{x})}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{y} .$$

Weil das Feld konservativ ist, hängt der Wert nicht davon ab, welche Kurve man wählt. Nun sei $k\in\{1,\dots,n\}$. Weil $\mathcal G$ offen ist, liegt eine Kugel $B_\rho(\boldsymbol{x})$ um $\boldsymbol{x}$ ganz in $\mathcal G$, und für $0<|\eta|<\rho$ liegt die Strecke von $\boldsymbol{x}$ nach $\boldsymbol{x}+\eta\,\hat{\boldsymbol{e}}_k$ in ihr. Zum Punkt $\boldsymbol{x}+\eta\,\hat{\boldsymbol{e}}_k$ darf man über $\boldsymbol{x}$ laufen: zuerst $\Gamma(\boldsymbol{x})$, dann diese Strecke $\boldsymbol{y}(t)=\boldsymbol{x}+t\,\hat{\boldsymbol{e}}_k$, $t$ von $0$ bis $\eta$. Mit $\dot{\boldsymbol{y}}=\hat{\boldsymbol{e}}_k$ folgt

$$\varphi(\boldsymbol{x}+\eta\,\hat{\boldsymbol{e}}_k)-\varphi(\boldsymbol{x})=\int_0^\eta\boldsymbol{F}(\boldsymbol{x}+t\,\hat{\boldsymbol{e}}_k)\cdot\hat{\boldsymbol{e}}_k\,\mathrm{d} t=\int_0^\eta F_k(\boldsymbol{x}+t\,\hat{\boldsymbol{e}}_k)\,\mathrm{d} t .$$

Nach dem Mittelwertsatz der Integralrechnung, Satz [2.1](#satz-2-1), gibt es ein $\vartheta$ zwischen $0$ und $\eta$ mit

$$\frac{\varphi(\boldsymbol{x}+\eta\,\hat{\boldsymbol{e}}_k)-\varphi(\boldsymbol{x})}\eta=F_k(\boldsymbol{x}+\vartheta\,\hat{\boldsymbol{e}}_k).$$

Für $\eta\to0$ geht auch $\vartheta\to0$, und weil $\boldsymbol{F}$ stetig ist, strebt die rechte Seite gegen $F_k(\boldsymbol{x})$. Also existiert $\frac{\partial\varphi}{\partial x_k}(\boldsymbol{x})=F_k(\boldsymbol{x})$. Da $k$ und $\boldsymbol{x}$ beliebig waren, ist $\nabla\varphi=\boldsymbol{F}$; die partiellen Ableitungen sind stetig, $\varphi$ ist also stetig differenzierbar ([Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html)).
:::

⁠**So liest man das:** (i) ist der Hauptsatz in mehreren Variablen: Das Kurvenintegral eines Gradienten ist die Differenz des Skalarpotentials zwischen Ziel und Start. (ii) sagt, dass konservativ und Gradientenfeld dasselbe sind. Zusammen mit Satz [2.4](#satz-2-4) sind *konservativ*, *Gradientenfeld* und *jeder Rundweg ergibt null* drei Beschreibungen derselben Eigenschaft.

::::beispiel [Beispiel 1]
Das Strahlfeld ist $\boldsymbol S=\nabla\varphi$ mit $\varphi(x,y)=\frac12(x^2+y^2)$. Es ist also konservativ, und jeder Weg von $(1,0)$ nach $(0,1)$ ergibt $\varphi(0,1)-\varphi(1,0)=\frac12-\frac12=0$, wie bei $\kappa$ und $\sigma$ gefunden.
::::

::::beispiel [Beispiel 2]
Auf dem Gebiet $\mathbb{R}^3\setminus\{0\}$ sei $\boldsymbol{F}(\boldsymbol{x})=-\boldsymbol{x}/|\boldsymbol{x}|^3$. Nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) ist $\nabla f(r)=f'(r)\,\hat{\boldsymbol{e}}_r$ mit $r=|\boldsymbol{x}|$ und $\hat{\boldsymbol{e}}_r=\boldsymbol{x}/r$; für $f(r)=1/r$ folgt $\nabla\frac1{|\boldsymbol{x}|}=-\frac1{r^2}\,\frac{\boldsymbol{x}}r=\boldsymbol{F}$. Längs jeder Kurve von $(1,0,0)$ nach $(0,0,2)$, die den Nullpunkt meidet, ist deshalb

$$\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\frac1{|(0,0,2)|}-\frac1{|(1,0,0)|}=\frac12-1=-\frac12 .$$

Ohne den Satz müsste man dafür eine Kurve wählen und integrieren.
::::

:::hintergrund Warum beim Gradientenfeld nur Start und Ziel zählen
Der Mechanismus ist eine Teleskopsumme. Ist $\boldsymbol{F}=\nabla\varphi$, dann ist nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) für einen kurzen Schritt $\Delta\boldsymbol{x}_k$ von $\boldsymbol{x}_{k-1}$ nach $\boldsymbol{x}_k$

$$\boldsymbol{F}(\boldsymbol{x}_{k-1})\cdot\Delta\boldsymbol{x}_k\approx\varphi(\boldsymbol{x}_k)-\varphi(\boldsymbol{x}_{k-1}),$$

„Gradient mal Schritt ist ungefähr die Änderung“. Summiert man über alle Schritte des Wegs, heben sich alle Zwischenwerte auf:

$$\bigl(\varphi(\boldsymbol{x}_1)-\varphi(\boldsymbol{x}_0)\bigr)+\bigl(\varphi(\boldsymbol{x}_2)-\varphi(\boldsymbol{x}_1)\bigr)+\dots+\bigl(\varphi(\boldsymbol{x}_N)-\varphi(\boldsymbol{x}_{N-1})\bigr)=\varphi(\boldsymbol{x}_N)-\varphi(\boldsymbol{x}_0).$$

Wo die Zwischenpunkte lagen, ist verschwunden. Bei einer Wanderung ist das die Summe aller kleinen Höhenunterschiede: Sie ist Zielhöhe minus Starthöhe, gleichgültig, über welche Hügel der Weg führte. Der Beweis macht dasselbe exakt. Die Kettenregel zeigt, dass der Integrand $\boldsymbol{F}(\gamma)\cdot\dot\gamma$ die Änderungsrate von $\varphi$ längs des Wegs ist, und der Hauptsatz summiert Änderungsraten zur Gesamtänderung.

Bei einem Feld, das kein Gradient ist, gibt es keine solche Funktion $\varphi$. Dann hängt jeder Summand $\boldsymbol{F}\cdot\Delta\boldsymbol{x}_k$ davon ab, wo das Wegstück liegt, und die Summe merkt sich den Weg.
:::

:::hintergrund Woher das Potential im Beweis kommt
Teil (ii) baut das Skalarpotential als angesammeltes Kurvenintegral von einem festen Punkt aus, so wie man in einer Variablen eine Stammfunktion als $F(x)=\int_a^xf(t)\,\mathrm{d} t$ baut. In der Physik ist das genau die Definition der potentiellen Energie: Man wählt einen Bezugspunkt und ordnet jedem Ort die Arbeit zu, die das Feld auf dem Weg vom Bezugspunkt dorthin verrichtet, mit umgekehrtem Vorzeichen. Wegunabhängigkeit ist die Bedingung dafür, dass diese Zuordnung eindeutig ist. Ein anderer Bezugspunkt ändert $\varphi$ nur um eine Konstante, nämlich um das Integral zwischen den beiden Bezugspunkten. Dass $\nabla\varphi=\boldsymbol{F}$ herauskommt, sieht man am letzten Schritt des Wegs: Wer $\boldsymbol{x}$ um $\eta$ in Richtung $x_k$ verschiebt, verlängert den Weg um ein kurzes gerades Stück, auf dem nur die Komponente $F_k$ zählt.
:::

⁠**Kurz gesagt:** Das Kurvenintegral eines Gradientenfelds ist die Differenz des Skalarpotentials zwischen Ziel und Start. Konservativ und Gradientenfeld sind dasselbe.

### Arbeit und Spannung in konservativen Feldern

<span class="anker" id="stufe-2-6"></span>

In der Physik schreibt man ein Potentialfeld mit Minuszeichen. Was wird dann aus dem ersten Hauptsatz?

Nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) heißt eine Funktion $u$ mit $\boldsymbol{E}=-\nabla u$ ein Potential des Felds $\boldsymbol{E}$ im Sinn der Physik. Dann ist $\boldsymbol{E}=\nabla(-u)$, und [(2.1)](#gl-2-1) gibt für jeden Weg von $A$ nach $B$

<span class="anker" id="gl-2-2"></span>
$$\int_A^B\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{x}=u(A)-u(B). \tag{2.2}$$

Ist $\boldsymbol{E}$ ein elektrisches Feld, gemessen in $\mathrm V/\mathrm m$, und $u$ das elektrische Potential in $\mathrm V$, dann heißt diese Zahl die __Spannung__ zwischen $A$ und $B$, kurz $U_{AB}$. Sie hängt nach dem ersten Hauptsatz nicht vom Weg ab. Die Arbeit, die das Feld an einer Ladung $q$ auf dem Weg von $A$ nach $B$ verrichtet, ist $W=q\,U_{AB}$. Das Feld leistet positive Arbeit, wenn die Ladung zu kleinerem $q\,u$ läuft, so wie ein Ball beim Bergabrollen Höhe verliert.

::::beispiel
Sei $u(x,y,z)=-3x\,\mathrm{V}/\mathrm m$ im ganzen Raum, also $\boldsymbol{E}=-\nabla u=(3,0,0)\,\mathrm{V}/\mathrm m$. Von $A=(0,0,0)$ nach $B=(2,1,0)$, Längen in Metern, ist $U_{AB}=u(A)-u(B)=0-(-6\,\mathrm{V})=6\,\mathrm{V}$, auf jedem Weg. Eine Ladung $q=2\,\mathrm{\mu C}$ erhält dabei vom Feld die Arbeit $W=2\,\mathrm{\mu C}\cdot6\,\mathrm{V}=12\,\mathrm{\mu J}$.
::::

:::hintergrund Elektrische Felder, die nicht konservativ sind
Elektrostatische Felder, also Felder ruhender Ladungen, sind Gradientenfelder. Deshalb hat jedes Punktepaar eine Spannung, und die Summe der Spannungen längs jeder Masche eines Netzwerks ist null; das ist die Maschenregel. Ein elektrisches Feld, das ein sich zeitlich ändernder Magnetfluss erzeugt, ist dagegen nicht konservativ. Ein Umlauf um den Fluss ergibt nicht null, sondern die induzierte Spannung. In einer Leiterschleife um einen Transformatorkern hängt die gemessene Spannung zwischen zwei Punkten deshalb davon ab, auf welcher Seite des Kerns die Messleitungen verlaufen. Die Rede von „der“ Spannung zwischen zwei Punkten setzt also ein konservatives Feld voraus.
:::

⁠**Kurz gesagt:** In einem konservativen Feld ist $\int_A^B\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{x}=u(A)-u(B)$, die Spannung zwischen $A$ und $B$; sie hängt nicht vom Weg ab.

### Konservative Felder sind rotationsfrei

<span class="anker" id="stufe-2-7"></span>

Ob ein Feld konservativ ist, ist nach dem ersten Hauptsatz dieselbe Frage wie die nach einem Skalarpotential. [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) hat dafür eine notwendige Bedingung geliefert, die man durch bloßes Ableiten prüft.

Sei $\boldsymbol{F}$ stetig differenzierbar und konservativ auf einem Gebiet $\mathcal G$. Nach Satz [2.5](#satz-2-5) ist $\boldsymbol{F}=\nabla\varphi$, und weil $\nabla\varphi=\boldsymbol{F}$ stetig differenzierbar ist, ist $\varphi$ zweimal stetig differenzierbar. Nach den Integrabilitätsbedingungen aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) gilt dann

<span class="anker" id="gl-2-3"></span>
$$\frac{\partial F_k}{\partial x_j}=\frac{\partial F_j}{\partial x_k}\quad\text{für alle }j,k,\qquad\text{für }n=2,3\text{ also}\qquad\operatorname{rot}\boldsymbol{F}=0\ \text{in }\mathcal G . \tag{2.3}$$

Ein stetig differenzierbares Feld, das die Integrabilitätsbedingungen erfüllt, heißt kurz __integrabel__. Jedes stetig differenzierbare konservative Feld ist also integrabel. Umgekehrt gilt: Ist $\operatorname{rot}\boldsymbol{F}\neq0$ an auch nur einer Stelle, ist $\boldsymbol{F}$ nicht konservativ.

::::beispiel
Das Drehfeld hat $\operatorname{rot}\boldsymbol V=\frac{\partial x}{\partial x}-\frac{\partial(-y)}{\partial y}=2\neq0$. Es kann also nicht konservativ sein, passend zu den verschiedenen Werten auf $\kappa$ und $\sigma$. Das Strahlfeld hat $\operatorname{rot}\boldsymbol S=0-0=0$, wie es für ein Gradientenfeld sein muss.
::::

⁠**Kurz gesagt:** Ein stetig differenzierbares konservatives Feld ist integrabel, in Ebene und Raum also rotationsfrei.

### Ein rotationsfreies Feld, das nicht konservativ ist

<span class="anker" id="stufe-2-8"></span>

Gilt auch die Umkehrung: Ist jedes rotationsfreie Feld konservativ? [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) hat am Feld $\boldsymbol{H}$ gezeigt, dass es ein Skalarpotential nicht immer gibt. Mit Kurvenintegralen lässt sich dasselbe Beispiel jetzt in einer einzigen Zahl ausdrücken.

Sei $\mathcal G=\mathbb{R}^2\setminus\{0\}$, ein Gebiet nach Unterabschnitt [2.2](#stufe-2-2), und

$$\boldsymbol{H}\colon\mathcal G\to\mathbb{R}^2,\qquad\boldsymbol{H}(x,y)=\frac{1}{x^2+y^2}\begin{pmatrix}-y\\x\end{pmatrix}.$$

Die Pfeile laufen gegen den Uhrzeigersinn um den Nullpunkt und werden nach außen kürzer. Nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) ist, mit der Quotientenregel,

$$\frac{\partial H_2}{\partial x}=\frac{(x^2+y^2)-x\cdot2x}{(x^2+y^2)^2}=\frac{y^2-x^2}{(x^2+y^2)^2},\qquad \frac{\partial H_1}{\partial y}=\frac{-(x^2+y^2)+y\cdot2y}{(x^2+y^2)^2}=\frac{y^2-x^2}{(x^2+y^2)^2},$$

also $\operatorname{rot}\boldsymbol{H}=0$ überall in $\mathcal G$.

Sei $K_R$ der gegen den Uhrzeigersinn durchlaufene Kreis mit dem Radius $R>0$ um den Nullpunkt, $\gamma(t)=R(\cos t,\sin t)$, $t\in[0,2\pi]$. Es ist $\boldsymbol{H}(\gamma(t))=\frac1R(-\sin t,\cos t)$ und $\dot\gamma(t)=R(-\sin t,\cos t)$, also $\boldsymbol{H}(\gamma)\cdot\dot\gamma=\sin^2t+\cos^2t=1$ und

<span class="anker" id="gl-2-4"></span>
$$\int_{K_R}\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{x}=\int_0^{2\pi}1\,\mathrm{d} t=2\pi\neq0 . \tag{2.4}$$

Nach Satz [2.4](#satz-2-4) ist $\boldsymbol{H}$ nicht konservativ in $\mathcal G$, nach Satz [2.5](#satz-2-5) also kein Gradientenfeld in $\mathcal G$, obwohl $\operatorname{rot}\boldsymbol{H}=0$ ist. Der Wert hängt nicht vom Radius ab. Das Feld $\boldsymbol{H}$ heißt in diesem Kapitel das __Wirbelfeld__.

Die Integrabilitätsbedingung ist also notwendig dafür, dass ein Feld konservativ ist, aber im Allgemeinen nicht hinreichend. Wie im Beispiel aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) hat die Menge $\mathcal G$ ein Loch, um das der Weg herumläuft.

:::hintergrund Was das Wirbelfeld zählt: den überstrichenen Winkel
Für eine Kurve $\gamma(t)=(x(t),y(t))$, die den Nullpunkt meidet, ist

$$\boldsymbol{H}(\gamma)\cdot\dot\gamma=\frac{x\,\dot y-y\,\dot x}{x^2+y^2}.$$

Beschreibt man den Punkt durch seinen Abstand $r(t)$ vom Nullpunkt und den Winkel $\theta(t)$ seines Ortspfeils gegen die $x$-Achse, also $x=r\cos\theta$, $y=r\sin\theta$, und folgt dem Winkel stetig längs der Kurve, dann ergibt Einsetzen $x\dot y-y\dot x=r^2\,\dot\theta$. Der Integrand ist also genau $\dot\theta$, die Geschwindigkeit, mit der sich der Ortspfeil dreht. Das Kurvenintegral von $\boldsymbol{H}$ ist die Änderung des Winkels zwischen Start und Ziel: Es misst, welchen Winkel der Weg vom Nullpunkt aus gesehen überstreicht.

Daraus folgt alles Weitere ohne Rechnung. Ein Umlauf um den Nullpunkt überstreicht $2\pi$, gleichgültig, wie groß oder wie verbeult er ist. Zweimal herum ergibt $4\pi$, im Uhrzeigersinn $-2\pi$. Ein Rundweg, der den Nullpunkt nicht umläuft, kehrt zum Anfangswinkel zurück und ergibt $0$. Das Kurvenintegral zählt also, wie oft der Weg das Loch umläuft. Örtlich ist $\boldsymbol{H}$ der Gradient des Winkels, deshalb ist es rotationsfrei. Auf ganz $\mathcal G$ gibt es aber keine stetige Winkelfunktion: Nach einem Umlauf ist der Winkel um $2\pi$ gewachsen, obwohl man wieder am Startpunkt steht.
:::

:::hintergrund Sind die Kurvenintegrale eines konservativen Felds immer wegunabhängig?
Ja, das ist die Definition: Konservativ heißt, dass alle Kurvenintegrale zwischen zwei Punkten übereinstimmen. Der Inhalt der Sätze dieses Abschnitts ist, dass diese Eigenschaft mit zwei anderen zusammenfällt, dem Skalarpotential und den verschwindenden Rundwegen. Zwei Dinge muss man beim Anwenden beachten.

Erstens ist „konservativ“ eine Eigenschaft des Felds *und* des Gebiets. Die Wegunabhängigkeit gilt nur für Wege, die im Gebiet bleiben. Das Wirbelfeld $\boldsymbol{H}$ ist auf der rechten Halbebene $\{x>0\}$ konservativ, denn dort ist es nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) der Gradient von $\arctan(y/x)$. Auf $\mathbb{R}^2\setminus\{0\}$ ist es nicht konservativ, denn dort gibt es Wege um den Nullpunkt herum.

Zweitens folgt aus $\operatorname{rot}\boldsymbol{F}=0$ allein nicht, dass ein Feld konservativ ist. Wer aus der verschwindenden Rotation auf Wegunabhängigkeit schließen will, braucht zusätzlich eine Aussage über die Form des Gebiets.
:::

⁠**Kurz gesagt:** Das Wirbelfeld ist rotationsfrei, ergibt aber auf jedem Kreis um den Nullpunkt $2\pi$. Die Integrabilitätsbedingung ist notwendig, aber im Allgemeinen nicht hinreichend.

### Aufgaben

<span class="anker" id="stufe-2-9"></span>

:::aufgabe Aufgabe 5 ★ Arbeit im Coulomb-Feld
<span class="anker" id="aufg-5"></span>

Sei $\boldsymbol{F}(\boldsymbol{x})=-\boldsymbol{x}/|\boldsymbol{x}|^3$ auf $\mathbb{R}^3\setminus\{0\}$, wie in Unterabschnitt [2.5](#stufe-2-5).

<ol class="al">

<li>

Berechne $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ für die Schraubenlinie $\gamma(t)=(\cos t,\sin t,t)$, $t\in[0,2\pi]$, mit dem ersten Hauptsatz.

</li>

<li>

Rechne dasselbe Integral direkt mit [(1.2)](integration-langs-regularer-kurven.html#gl-1-2) nach.

</li>

<li>

Welchen Wert hat das Kurvenintegral längs jeder geschlossenen regulären Kurve, die den Nullpunkt meidet? Begründe.

</li>

</ol>

:::

:::aufgabe Aufgabe 6 ★★ Wann ist dieses Feld konservativ?
<span class="anker" id="aufg-6"></span>

Seien $\alpha,\beta\in\mathbb{R}$ und $\boldsymbol{F}(x,y)=\dfrac{\alpha}{(x^2+y^2)^2}\,(x,y)+\beta\,\boldsymbol{H}(x,y)$ auf $\mathbb{R}^2\setminus\{0\}$.

<ol class="al">

<li>

Berechne das Kurvenintegral über den Kreis mit dem Radius $2$ um den Nullpunkt, gegen den Uhrzeigersinn.

</li>

<li>

Für welche $\alpha,\beta$ ist $\boldsymbol{F}$ konservativ? Gib dann ein Skalarpotential an.

</li>

<li>

Berechne für diesen Fall das Kurvenintegral von $(1,0)$ nach $(0,2)$.

</li>

</ol>

:::loesung
(a) Der erste Summand steht auf dem Kreis senkrecht zum Weg und liefert null. Der zweite liefert nach [(2.4)](#gl-2-4) den Wert $2\pi b$. (b) Für $b\neq0$ ist der Umlauf nicht null, also ist $\boldsymbol{F}$ nicht konservativ. Für $b=0$ ist $\boldsymbol{F}=\nabla\varphi$ mit $\varphi=-\frac{a}{2(x^2+y^2)}$. $a$ ist beliebig. (c) $\varphi(0,2)-\varphi(1,0)=-\frac a8+\frac a2=\frac{3a}{8}$.
:::
:::

:::aufgabe Aufgabe 7 ★★ Ein Rundweg mit null reicht nicht
<span class="anker" id="aufg-7"></span>

Sei $\boldsymbol{F}(x,y)=(|y|,\,|x|)$ auf $\mathbb{R}^2$.

<ol class="al">

<li>

Berechne das Kurvenintegral über den Einheitskreis, gegen den Uhrzeigersinn.

</li>

<li>

Berechne es über den Rand des Quadrats $[-1,0]\times[0,1]$, gegen den Uhrzeigersinn: von $(0,0)$ über $(0,1)$, $(-1,1)$ und $(-1,0)$ zurück nach $(0,0)$.

</li>

<li>

Ist $\boldsymbol{F}$ konservativ? Was folgt aus (a) allein?

</li>

<li>

Berechne $\operatorname{rot}\boldsymbol{F}$ in den vier offenen Quadranten und erkläre damit das Ergebnis von (c).

</li>

</ol>

:::
