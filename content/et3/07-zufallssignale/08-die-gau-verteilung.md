---
title: Stufe 7: Die Gauß-Verteilung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270800
summary: Warum ist Rauschen so oft gaußverteilt, und wie rechnet man mit der Gauß-Verteilung?
tags: zentraler Grenzwertsatz, Fehlerfunktion
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Warum ist Rauschen so oft gaußverteilt, und wie rechnet man mit der Gauß-Verteilung?
:::

Faltet man viele Dichten miteinander, nähert sich das Ergebnis einer Gaußkurve (__zentraler Grenzwertsatz__, [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). Rauschen ist meist die Summe sehr vieler kleiner, unabhängiger Beiträge, etwa der Bewegungen vieler Elektronen. Deshalb ist es gaußverteilt.

:::satz Satz 7.1 (Gauß-Verteilung)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

mit der __Fehlerfunktion__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$ und $\operatorname{erfc}=1-\operatorname{erf}$.
:::

⁠**So liest man das:** Mittelwert und Varianz legen die Gauß-Verteilung vollständig fest. Innerhalb von $\pm\sigma_s$ um den Mittelwert liegen 68,3 % der Werte, innerhalb $\pm2\sigma_s$ 95,4 %, innerhalb $\pm3\sigma_s$ 99,73 %. Das Integral der Gaußkurve hat keine geschlossene Form, deshalb die Funktion erf, die man tabelliert oder numerisch berechnet. Für große $x$ gilt $\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$.

**Rechenregeln.** Die Summe zweier unabhängiger gaußverteilter Größen ist gaußverteilt mit $m_s=m_1+m_2$ und $\sigma_s^2=\sigma_1^2+\sigma_2^2$. Ein Gauß-Prozess bleibt nach einem LTI-System ein Gauß-Prozess, denn das Faltungsintegral ist eine (unendliche) gewichtete Summe. Und bei zwei gemeinsam gaußverteilten Größen ist „unkorreliert“ dasselbe wie „unabhängig“: Ist die normierte Kreuzkovarianz $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ null, zerfällt die Verbunddichte in ein Produkt.

:::zusatz Die zweidimensionale Gauß-Dichte
Für mittelwertfreie, gemeinsam gaußverteilte $s,g$ mit dem Korrelationskoeffizienten $\rho$ ist

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

Man erhält sie über die normierten Summen- und Differenzgrößen $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$: Sie sind unkorreliert, haben die Varianzen $2(1\pm\rho)$ und sind als Gauß-Größen unabhängig. Linien gleicher Dichte sind Ellipsen. In den normierten Koordinaten $x/\sigma_s$, $y/\sigma_g$ liegen ihre Achsen entlang dieser Summen und Differenzen. Für $\rho=0$ werden sie zu Kreisen (bei $\sigma_s=\sigma_g$), und die Dichte ist das Produkt der Einzeldichten.
:::

:::aufgabe Aufgabe 6 ★ Mit der Gauß-Verteilung rechnen
<span class="anker" id="aufg-6"></span>

Eine Rauschspannung ist gaußverteilt mit $m=0$ und $\sigma=1$ mV.

<ol class="al">

<li>

Mit welcher Wahrscheinlichkeit ist sie größer als 2 mV? (Tipp: $\operatorname{erfc}(1{,}414)=0{,}0455$.)

</li>

<li>

Zwei solche unabhängige Spannungen werden addiert. Welche Verteilung hat die Summe?

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1{,}414)=0{,}023$, also 2,3 %.

(b) Gaußverteilt mit $m=0$ und $\sigma^2=2$ mV$^2$, $\sigma=1{,}41$ mV.
:::
:::

::::formelsammlung
**Gauß-Dichte**

$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)}$$

Mittelwert und Varianz legen sie vollständig fest. Innerhalb von $\pm\sigma_s$, $\pm2\sigma_s$, $\pm3\sigma_s$ um den Mittelwert liegen 68,3 %, 95,4 % und 99,73 % der Werte.

**Gauß-Verteilungsfunktion**

$$P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr)$$

Das Integral der Gaußkurve hat keine geschlossene Form; erf wird tabelliert oder numerisch berechnet.

**Fehlerfunktion**

$$\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi,\qquad\operatorname{erfc}=1-\operatorname{erf}$$

Für große $x$ gilt $\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$.

**Summe unabhängiger Gauß-Größen**

$$m_s=m_1+m_2,\qquad\sigma_s^2=\sigma_1^2+\sigma_2^2$$

Die Summe ist wieder gaußverteilt. Ein Gauß-Prozess bleibt nach einem LTI-System ein Gauß-Prozess. Rauschen ist als Summe sehr vieler kleiner, unabhängiger Beiträge nach dem zentralen Grenzwertsatz gaußverteilt.

**Normierte Kreuzkovarianz**

$$\rho=\mu_{sg}/(\sigma_s\sigma_g)$$

Bei gemeinsam gaußverteilten Größen ist „unkorreliert“ ($\rho=0$) dasselbe wie „unabhängig“.

**Zweidimensionale Gauß-Dichte**

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr)$$

Für mittelwertfreie, gemeinsam gaußverteilte $s,g$. Linien gleicher Dichte sind Ellipsen; für $\rho=0$ das Produkt der Einzeldichten.
::::

::::lernkarten
:::karte zusammenhang zentraler Grenzwertsatz
Warum ist Rauschen, etwa das eines Widerstands, meist gaußverteilt?
---
Weil es meist die Summe sehr vieler kleiner, unabhängiger Beiträge ist, etwa der Bewegungen vieler Elektronen. Die Dichte der Summe ist die Faltung vieler Dichten, und diese nähert sich nach dem zentralen Grenzwertsatz einer Gaußkurve.
--- falsch
Weil sich jedes einzelne Elektron gaußverteilt bewegt und die Summe gaußverteilter Beiträge wieder gaußverteilt ist. Ohne gaußverteilte Einzelbeiträge wäre auch das Rauschen nicht gaußverteilt, gleichgültig, wie viele Beiträge zusammenkommen.
--- falsch
Weil Rauschen definitionsgemäß gaußverteilt ist: Ein Signal mit einer anderen Verteilung nennt man nicht Rauschen, sondern Störsignal, auch wenn es ebenso zufällig und unvorhersagbar ist wie Rauschen.
--- falsch
Weil die Gaußkurve die einzige Dichte ist, die ein stationärer Prozess haben kann: Jede andere Dichte würde sich mit der Zeit verändern und damit die Stationarität des Prozesses verletzen.
:::
:::karte formel Gauß-Dichte
Wie lautet die Verteilungsdichte der Gauß-Verteilung, und welche Größen legen sie fest?
---
$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)}$. Mittelwert $m_s$ und Varianz $\sigma_s^2$ legen die Gauß-Verteilung vollständig fest.
--- falsch
$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)/(2\sigma_s^2)}$. Mittelwert und Varianz legen nur die Lage fest; die Form bestimmt man zusätzlich aus der AKF des Prozesses.
--- falsch
$p_s(x)=\frac{1}{2\pi\sigma_s}\,\mathrm{e}^{-(x-m_s)^2/\sigma_s}$. Neben Mittelwert und Varianz braucht man noch die Leistung $L_s$, um die Verteilung vollständig festzulegen.
--- falsch
$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-x^2/(2\sigma_s^2)}$. Sie wird allein durch die Varianz festgelegt, denn eine Gauß-Verteilung hat immer den Mittelwert null.
:::
:::karte formel Gauß-Verteilungsfunktion
Wie drückt man die Verteilungsfunktion der Gauß-Verteilung mit der Fehlerfunktion bzw. ihrem Komplement aus?
---
$P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr)$, mit $\operatorname{erfc}=1-\operatorname{erf}$.
--- falsch
$P_s(x)=\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=1-\operatorname{erfc}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)$, mit $\operatorname{erfc}=1-\operatorname{erf}$; bei $x=m_s$ ist sie null.
--- falsch
$P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{2\sigma_s^2}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{x-m_s}{2\sigma_s^2}\Bigr)$, mit $\operatorname{erfc}=1+\operatorname{erf}$.
--- falsch
$P_s(x)=\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)$, mit $\operatorname{erfc}=1-\operatorname{erf}$.
:::
:::karte begriff Fehlerfunktion
Was ist die Fehlerfunktion $\operatorname{erf}$, und warum braucht man sie zum Rechnen mit der Gauß-Verteilung?
---
Eine durch ein Integral der Gaußkurve definierte Funktion: $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$. Man braucht sie, weil dieses Integral keine geschlossene Form hat; erf wird tabelliert oder numerisch berechnet.
--- falsch
Die Abweichung zwischen einer gemessenen Dichte und der Gaußkurve: $\operatorname{erf}(x)=p_s(x)-\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-x^2/2}$. Man braucht sie, um zu prüfen, ob ein gemessenes Rauschen wirklich gaußverteilt ist.
--- falsch
Die Ableitung der Gaußkurve: $\operatorname{erf}(x)=\frac{\mathrm{d}}{\mathrm{d} x}\mathrm{e}^{-x^2}$. Man braucht sie, weil die Verteilungsfunktion der Gauß-Verteilung die Steigung der Gaußkurve angibt und sich diese Steigung nicht in einfacher Form schreiben lässt.
--- falsch
Eine durch ein Integral der Gaußkurve definierte Funktion: $\operatorname{erf}(x)=\int_{-\infty}^{\infty}\mathrm{e}^{-\xi^2}\mathrm{d}\xi$. Man braucht sie, weil die Gaußkurve nicht die Fläche 1 hat und erst durch erf geteilt werden muss.
:::
:::karte formel Werte um den Mittelwert
Welcher Anteil der Werte einer Gauß-Verteilung liegt innerhalb von $\pm\sigma_s$, $\pm2\sigma_s$ und $\pm3\sigma_s$ um den Mittelwert?
---
68,3 % innerhalb $\pm\sigma_s$, 95,4 % innerhalb $\pm2\sigma_s$ und 99,73 % innerhalb $\pm3\sigma_s$: Werte, die um mehr als drei Standardabweichungen vom Mittelwert abweichen, sind sehr selten.
--- falsch
50 % innerhalb $\pm\sigma_s$, 75 % innerhalb $\pm2\sigma_s$ und 87,5 % innerhalb $\pm3\sigma_s$: Jede weitere Standardabweichung halbiert den Anteil der Werte, die noch außerhalb liegen.
--- falsch
33,3 % innerhalb $\pm\sigma_s$, 66,7 % innerhalb $\pm2\sigma_s$ und 100 % innerhalb $\pm3\sigma_s$: Eine Gauß-Verteilung reicht genau drei Standardabweichungen weit, darüber hinaus ist ihre Dichte null.
--- falsch
68,3 % innerhalb $\pm2\sigma_s$, 95,4 % innerhalb $\pm4\sigma_s$ und 99,73 % innerhalb $\pm6\sigma_s$: Die Breite der Kurve ist die doppelte Standardabweichung, nicht die einfache.
:::
:::karte formel Näherung für große Argumente
Wie verhält sich die Funktion $\operatorname{erfc}(x)$ für große $x$, und was folgt daraus?
---
$\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$: Sie fällt im Wesentlichen wie $\mathrm{e}^{-x^2}$, also sehr schnell, sodass schon wenig größere Argumente viel kleinere Werte ergeben.
--- falsch
$\operatorname{erfc}(x)\approx\frac{1}{\sqrt\pi\,x}$: Sie fällt nur wie $1/x$, also langsam, sodass auch sehr große Argumente noch merkliche Werte ergeben und Fehler nie ganz verschwinden.
--- falsch
$\operatorname{erfc}(x)\approx1-\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$: Sie nähert sich für große Argumente dem Wert 1, weil dann fast die ganze Fläche der Gaußkurve erfasst ist.
--- falsch
$\operatorname{erfc}(x)\approx\mathrm{e}^{-x}$: Sie fällt rein exponentiell, also wie die Entladekurve eines Kondensators, sodass jede Vergrößerung des Arguments um 1 den Wert um denselben Faktor senkt.
:::
:::karte formel Summe unabhängiger Gauß-Größen
Welche Verteilung hat die Summe zweier unabhängiger gaußverteilter Größen, und wie folgen ihr Mittelwert und ihre Varianz?
---
Wieder eine Gauß-Verteilung, mit $m_s=m_1+m_2$ und $\sigma_s^2=\sigma_1^2+\sigma_2^2$. Zwei unabhängige Rauschspannungen mit je $\sigma=1$ mV ergeben also $\sigma=1{,}41$ mV, nicht 2 mV.
--- falsch
Eine Dreieckverteilung, weil die Faltung zweier gleicher Dichten ein Dreieck ergibt, mit $m_s=m_1+m_2$ und $\sigma_s^2=\sigma_1^2+\sigma_2^2$. Erst sehr viele Summanden ergeben wieder eine Gaußkurve.
--- falsch
Wieder eine Gauß-Verteilung, mit $m_s=m_1+m_2$ und $\sigma_s=\sigma_1+\sigma_2$. Zwei unabhängige Rauschspannungen mit je $\sigma=1$ mV ergeben also $\sigma=2$ mV.
--- falsch
Wieder eine Gauß-Verteilung, mit $m_s=m_1\,m_2$ und $\sigma_s^2=\sigma_1^2\,\sigma_2^2$. Zwei unabhängige Rauschspannungen mit je $\sigma=1$ mV ergeben also wieder $\sigma=1$ mV.
:::
:::karte zusammenhang Gauß-Prozess im LTI-System
Warum bleibt ein Gauß-Prozess nach einem LTI-System ein Gauß-Prozess?
---
Weil das Faltungsintegral eine (unendliche) gewichtete Summe von Werten des Eingangsprozesses ist und gewichtete Summen gaußverteilter Größen wieder gaußverteilt sind.
--- falsch
Weil ein LTI-System nur die Phase des Signals verändert, nicht seine Werte. Die Verteilung der Werte bleibt deshalb unverändert, ebenso Mittelwert und Varianz.
--- falsch
Weil jedes LTI-System selbst ein Gauß-Filter ist, dessen Impulsantwort eine Gaußkurve ist. Die Faltung zweier Gaußkurven ergibt dann wieder eine Gaußkurve.
--- falsch
Weil jedes LTI-System aus Widerständen besteht, die selbst gaußverteiltes Rauschen hinzufügen. Dieses Rauschen überdeckt am Ausgang jede andere Verteilung.
:::
:::karte zusammenhang Unkorreliert heißt bei Gauß-Größen unabhängig
Warum ist bei zwei gemeinsam gaußverteilten Größen „unkorreliert“ dasselbe wie „unabhängig“?
---
Weil ihre Kopplung in der gemeinsamen Gauß-Dichte nur über die normierte Kreuzkovarianz $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ eingeht. Ist $\rho$ null, zerfällt die Verbunddichte in das Produkt der Einzeldichten.
--- falsch
Weil gaußverteilte Größen stets unabhängig sind, gleichgültig, wie stark sie korreliert sind. Die gemeinsame Gauß-Dichte lässt sich immer als Produkt der beiden Einzeldichten schreiben.
--- falsch
Weil die Verbunddichte zweier Gauß-Größen nur von ihren beiden Mittelwerten abhängt. Sind diese Mittelwerte null, zerfällt die Verbunddichte in das Produkt der Einzeldichten.
--- falsch
Weil bei gaußverteilten Größen jeder Zusammenhang quadratisch ist und eine verschwindende Korrelation deshalb auch quadratische Zusammenhänge ausschließt, also alle möglichen.
:::
:::karte zusammenhang Linien gleicher Dichte
Welche Form haben die Linien gleicher Dichte einer zweidimensionalen Gauß-Dichte, und was ändert sich für $\rho=0$?
---
Es sind Ellipsen; in den normierten Koordinaten $x/\sigma_s$, $y/\sigma_g$ liegen ihre Achsen entlang der Summen und Differenzen $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$. Für $\rho=0$ ist die Dichte das Produkt der Einzeldichten, bei $\sigma_s=\sigma_g$ sind die Linien Kreise.
--- falsch
Es sind Geraden durch den Mittelwert, deren Steigung der Korrelationskoeffizient $\rho$ ist; je stärker die beiden Größen korreliert sind, desto steiler verlaufen sie. Für $\rho=0$ liegen alle Linien waagerecht.
--- falsch
Es sind Rechtecke, deren Seitenlängen $\sigma_s$ und $\sigma_g$ sind; die Korrelation dreht sie um den Winkel $\rho$ aus der Lage parallel zu den Achsen. Für $\rho=0$ liegen ihre Seiten parallel zu den Achsen.
--- falsch
Es sind Kreise um den Mittelwert, deren Radius mit $\rho$ wächst, gleichgültig, wie groß die beiden Varianzen sind. Für $\rho=0$ schrumpfen sie auf einen einzigen Punkt, weil die beiden Größen dann gar nichts gemeinsam haben.
:::
:::karte zusammenhang Überschreiten einer Schwelle
Mit welcher Wahrscheinlichkeit ist eine gaußverteilte Rauschspannung mit $m=0$ und $\sigma=1$ mV größer als 2 mV, und warum?
---
Mit $\frac12\operatorname{erfc}(1{,}414)=0{,}023$, also 2,3 %: Das ist die Fläche der Gaußkurve oberhalb von $2\sigma$, nur auf einer Seite des Mittelwerts.
--- falsch
Mit $\operatorname{erfc}(1{,}414)=0{,}0455$, also 4,6 %: Das ist die Fläche der Gaußkurve außerhalb von $\pm2\sigma$, die man bei einer Überschreitung vollständig zählen muss.
--- falsch
Mit 95,4 %: Innerhalb von $\pm2\sigma$ liegen 95,4 % der Werte, und genau so oft ist die Spannung größer als die Schwelle von zwei Standardabweichungen.
--- falsch
Mit $\frac12\operatorname{erfc}(2)=0{,}0023$, also 0,23 %: Man setzt die Schwelle in Vielfachen von $\sigma$ direkt in erfc ein, ohne durch $\sqrt2$ zu teilen.
:::
::::
