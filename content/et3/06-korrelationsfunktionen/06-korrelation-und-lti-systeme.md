---
title: Stufe 5: Korrelation und LTI-Systeme
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260600
summary: Was macht ein LTI-System mit der AKF und dem Energiedichtespektrum?
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Was macht ein LTI-System mit der AKF und dem Energiedichtespektrum? Und wie misst man ein System mit der Kreuzkorrelation?
:::

:::satz Satz 5.1 (Wiener-Lee)
<span class="anker" id="satz-5-1"></span>

Für $g=s*h$:

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung Wiener-Lee
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$. Nach Kommutativ- und Assoziativgesetz umsortieren: $[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$. Ebenso $\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$.
:::

⁠**So liest man das:** Das System multipliziert die Energie bei jeder Frequenz mit $|H|^2$. Die Phase des Systems spielt für die Energie keine Rolle. [(5.2)](#gl-5-2) ist ein Messverfahren: Hat der Eingang eine AKF, die fast ein gewichteter Dirac-Impuls $c\,\delta(\tau)$ ist (etwa ein sehr kurzer Impuls), dann ist die Kreuzkorrelation zwischen Eingang und Ausgang fast $c\,h(\tau)$, also bis auf den Faktor $c$ die Impulsantwort. Anders als $|H|^2$ enthält sie auch die Phase.

:::ltspice Energie vor und hinter dem RC-Glied
⁠**Zeichnen:** Verhaltensquelle `bv` am Netz `s` mit `V=exp(-time)*(time>0)`, der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$. Der Faktor `(time>0)` sorgt dafür, dass LTspice den Anfangszustand bei $t=0$ mit 0 V rechnet und der Kondensator leer startet. Dahinter das RC-Glied (`res` mit `1Meg`, `cap` mit `1u`) mit dem Ausgang am Netz `g`.

⁠**Direktiven:** `.tran 0 30 0 1m`, `.meas tran Es INTEG V(s)*V(s)` und `.meas tran Eg INTEG V(g)*V(g)`, die Energien nach [(1.1)](energie-und-leistung.html#gl-1-1).

⁠**Was du siehst:** `Es` $=0{,}500$, wie $E_s=\varphi^E_{ss}(0)=\frac12$ in Stufe [4](energiedichtespektrum.html#stufe-4). Vergleiche `Eg` mit deinem Ergebnis aus Aufgabe [5](#aufg-5). Die Ausgangsenergie ist kleiner, weil das RC-Glied die Energie bei jeder Frequenz mit $|H|^2\le1$ multipliziert.
:::

:::aufgabe Aufgabe 5 ★★ Energie am Ausgang
<span class="anker" id="aufg-5"></span>

Der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ geht durch ein RC-Glied mit $RC=1$ s.

<ol class="al">

<li>

Bestimme $|G(f)|^2$ und daraus die Ausgangsenergie. Tipp: $\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$.

</li>

<li>

Prüfe im Zeitbereich mit $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ ([Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), zwei RC-Glieder in Kette).

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$. Mit $x=2\pi f$: $E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$.

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$. Beide Wege stimmen überein. Die Energie sinkt von $\frac12$ auf $\frac14$, weil das zweite RC-Glied die höheren Frequenzen weiter dämpft.
:::
:::

::::formelsammlung
**Wiener-Lee**

$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2$$

Für $g=s*h$. Das System multipliziert die Energie bei jeder Frequenz mit $|H|^2$; seine Phase spielt für die Energie keine Rolle.

**KKF zwischen Eingang und Ausgang**

$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f)$$

Messverfahren: Ist die AKF des Eingangs fast $c\,\delta(\tau)$ (etwa ein sehr kurzer Impuls), ist die KKF fast $c\,h(\tau)$, also bis auf den Faktor $c$ die Impulsantwort, mit Phase.
::::

::::lernkarten
:::karte formel Wiener-Lee
Wie hängen nach dem Satz von Wiener-Lee AKF und Energiedichtespektrum am Ausgang eines LTI-Systems mit denen am Eingang zusammen?
---
Für $g=s*h$ gilt $\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2$: Die AKF wird mit der AKF der Impulsantwort gefaltet, das Energiedichtespektrum mit $|H|^2$ multipliziert.
--- falsch
Für $g=s*h$ gilt $\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)$ und $|G(f)|^2=|S(f)|^2\,H(f)$: Die AKF wird wie das Signal selbst mit der Impulsantwort gefaltet, weil das System auf jede Größe gleich wirkt.
--- falsch
Für $g=s*h$ gilt $\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)\,\varphi^E_{hh}(\tau)$ und $|G(f)|^2=|S(f)|^2*|H(f)|^2$: Die AKFs werden multipliziert, die Energiedichtespektren gefaltet, weil die Korrelation Faltung und Produkt vertauscht.
--- falsch
Für $g=s*h$ gilt $\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)$ und $|G(f)|^2=|S(f)|^2\,|H(f)|$: Das Energiedichtespektrum wird mit dem Betrag des Frequenzgangs multipliziert.
:::
:::karte herleitung Wiener-Lee
Wie folgt aus $g=s*h$ und $\varphi^E_{gg}=g^*(-\tau)*g(\tau)$ die Beziehung $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$?
---
Man setzt $g=s*h$ ein und erhält $\varphi^E_{gg}=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$, weil das gespiegelte, konjugierte Ausgangssignal die Faltung der gespiegelten, konjugierten Signale $s$ und $h$ ist.
---
Man sortiert die vier Faktoren nach Kommutativ- und Assoziativgesetz um zu $[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]$, weil bei einer Faltung mehrerer Signale Reihenfolge und Klammerung keine Rolle spielen.
---
Die erste Klammer ist $\varphi^E_{ss}$ und die zweite $\varphi^E_{hh}$, weil jede die Form „gespiegeltes, konjugiertes Signal gefaltet mit dem Signal“ hat; also ist $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$.
---
Ebenso ist $\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$, also $\varphi^E_{sg}=\varphi^E_{ss}*h$, weil hier nur das Ausgangssignal $g=s*h$ eingesetzt wird und das Eingangssignal bleibt.
:::
:::karte formel KKF zwischen Eingang und Ausgang
Welche KKF besteht zwischen dem Eingang $s$ und dem Ausgang $g=s*h$ eines LTI-Systems, und welches Spektrum gehört zu ihr?
---
$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f)$: Die AKF des Eingangs wird mit der Impulsantwort gefaltet. Das Spektrum enthält $H(f)$ selbst, also auch die Phase des Systems.
--- falsch
$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,|H(f)|^2$: Die KKF ist dieselbe wie die AKF des Ausgangs, und die Phase des Systems fällt heraus.
--- falsch
$\varphi^E_{sg}(\tau)=s(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$: Die KKF zwischen Eingang und Ausgang ist das Ausgangssignal selbst, weil das System die Korrelation bildet.
--- falsch
$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(-\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H^*(f)$: Die Impulsantwort erscheint gespiegelt und konjugiert, weil die Korrelation eine Faltung mit dem gespiegelten Signal ist.
:::
:::karte zusammenhang Phase des Systems und Energie
Warum spielt die Phase eines LTI-Systems für die Energie des Ausgangssignals keine Rolle?
---
Weil das System das Energiedichtespektrum nach $|G(f)|^2=|S(f)|^2\,|H(f)|^2$ nur mit dem Betragsquadrat $|H|^2$ multipliziert. Die Energie bei jeder Frequenz hängt also allein vom Betrag des Frequenzgangs ab.
--- falsch
Weil jedes LTI-System eine lineare Phase hat und eine lineare Phase das Signal nur verzögert; eine Verzögerung ändert die Energie nicht, eine andere Phase würde es dagegen tun.
--- falsch
Weil die Phase bei der Faltung mit der Impulsantwort herausfällt: $g=s*h$ enthält nur die Beträge von $S$ und $H$, die Phasen beider gehen dabei verloren.
--- falsch
Sie spielt eine Rolle: Die Ausgangsenergie ist das Integral von $|S(f)|^2\,H(f)$, und je nach Phase von $H$ heben sich die Anteile verschiedener Frequenzen gegenseitig ganz oder teilweise auf.
:::
:::karte zusammenhang Impulsantwort messen
Wie kann man mit der Kreuzkorrelation zwischen Eingang und Ausgang die Impulsantwort eines LTI-Systems messen?
---
Man wählt einen Eingang, dessen AKF fast ein gewichteter Dirac-Impuls $c\,\delta(\tau)$ ist, etwa einen sehr kurzen Impuls. Dann ist die KKF $\varphi^E_{sg}=\varphi^E_{ss}*h$ fast $c\,h(\tau)$, bis auf den Faktor $c$ die Impulsantwort.
--- falsch
Man wählt einen Eingang, dessen AKF möglichst breit ist, etwa einen langen Rechteckimpuls. Dann ist die KKF $\varphi^E_{sg}=\varphi^E_{ss}*h$ fast konstant, und ihr Wert ist die Fläche der Impulsantwort.
--- falsch
Man wählt einen beliebigen Eingang und bildet die AKF des Ausgangs. Sie ist $\varphi^E_{ss}*h$ und damit bis auf einen Faktor die Impulsantwort, gleich welchen Eingang man nimmt.
--- falsch
Man wählt einen Eingang, dessen AKF fast $c\,\delta(\tau)$ ist. Dann ist die KKF fast $c\,|H(f)|^2$, und die Impulsantwort folgt durch Wurzelziehen und Rücktransformation, wobei die Phase vollständig erhalten bleibt.
:::
:::karte zusammenhang KKF enthält die Phase
Was liefert die Messung der KKF zwischen Eingang und Ausgang, was das Energiedichtespektrum des Ausgangs nicht liefern kann?
---
Die Phase des Systems: Die KKF gehört zu $|S(f)|^2\,H(f)$ und enthält $H$ mit seiner Phase. Das Energiedichtespektrum $|G(f)|^2=|S(f)|^2\,|H(f)|^2$ enthält nur $|H|^2$.
--- falsch
Die Energie des Systems: Die KKF gehört zu $|S(f)|^2\,|H(f)|^2$, während das Energiedichtespektrum des Ausgangs nur den Betrag $|H(f)|$ ohne Quadrat enthält.
--- falsch
Nichts zusätzlich: KKF und AKF des Ausgangs gehören beide zu $|S(f)|^2\,|H(f)|^2$ und unterscheiden sich nur in der Lage ihres Maximums auf der $\tau$-Achse.
--- falsch
Den Zeitpunkt, an dem das Signal am Eingang ankommt; Betrag und Phase des Systems stecken dagegen vollständig im Energiedichtespektrum $|G(f)|^2$ des Ausgangs.
:::
:::karte formel Energie hinter dem RC-Glied
Welche Energie hat der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$ hinter einem RC-Glied mit $RC=1$ s, und warum ist sie kleiner als am Eingang?
---
Aus $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$ folgt $E_g=\frac14$, im Zeitbereich ebenso aus $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$. Sie sinkt von $\frac12$ auf $\frac14$, weil das RC-Glied die Energie bei jeder Frequenz mit $|H|^2\le1$ multipliziert.
--- falsch
Aus $|G|^2=|S|^2|H|^2=\frac{1}{1+(2\pi f)^2}$ folgt $E_g=\frac12$: Das RC-Glied ändert die Energie nicht, weil es nur die Phase dreht und dem Signal keine Energie entzieht.
--- falsch
Aus $|G|^2=|S|^2+|H|^2$ folgt $E_g=1$: Die Energien von Signal und System addieren sich, weil der Kondensator zusätzlich Energie speichert und wieder an den Ausgang abgibt.
--- falsch
Aus $|G|^2=|S|^2|H|$ folgt eine Energie zwischen $\frac14$ und $\frac12$, weil in die Energie nur der Betrag $|H|$ des Frequenzgangs eingeht und nicht sein Quadrat; die Phase spielt dabei keine Rolle.
:::
::::
