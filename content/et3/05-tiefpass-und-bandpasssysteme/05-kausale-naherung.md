---
title: Stufe 4: Kausale Näherung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3250500
summary: Wie baut man etwas, das dem idealen Tiefpass möglichst nahekommt?
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Wie baut man etwas, das dem idealen Tiefpass möglichst nahekommt? Man verzögert die Impulsantwort und schneidet den Rest ab.
:::

**Die Idee.** Man verschiebt $h(t)$ um $t_0$ nach rechts, bis der Teil bei $t<0$ vernachlässigbar ist, und schneidet ihn ab. Die Hüllkurve der si-Funktion fällt wie $1/(2\pi f_\mathrm g|t|)$. Soll sie vor $t=0$ unter 1 % des Maximums liegen, braucht man $t_0\approx16/f_\mathrm g$. Mit einem symmetrischen Fenster der Breite $2t_0$:

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**So liest man das:** Das Abschneiden ist eine Multiplikation mit einem Fenster, im Spektrum also eine Faltung mit dessen si-Spektrum. Die scharfe Kante wird verschmiert und bekommt Wellen. Der Faktor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ ist die Verzögerung: Das kausale Filter hat eine lineare Phase, es verzögert alle Frequenzen gleich (Abb. [2](#abb-2)). Je größer $t_0$, desto schmaler der Übergang, aber desto später die Antwort.

:::abbildung et3/k5kausal 2
Betrag des kausal gefensterten Tiefpasses mit $f_\mathrm g=1$ Hz und $t_0=3$ s (blau), gestrichelt das Ideal. An der Kante entsteht ein Übergangsbereich mit $|H_k(f_\mathrm g)|=0{,}49$, davor Wellen bis 1,10.
:::

:::aufgabe Aufgabe 4 ★★ Wie viel Verzögerung kostet die Kausalität?
<span class="anker" id="aufg-4"></span>

Ein Tiefpass mit $f_\mathrm g=1$ kHz soll kausal angenähert werden. Der verschobene ideale Tiefpass soll vor $t=0$, also im abgeschnittenen Teil, unter 1 % seines Maximums liegen.

<ol class="al">

<li>

Wie groß muss $t_0$ mindestens sein?

</li>

<li>

Was bedeutet das für ein Telefongespräch mit einer Kette aus zehn solchen Filtern?

</li>

</ol>

:::loesung
(a) Hüllkurve $\frac{1}{2\pi f_\mathrm g|t|}<0{,}01$ verlangt $|t|>\frac{100}{2\pi f_\mathrm g}=15{,}9$ ms. Also $t_0\approx16$ ms.

(b) Zehn Filter verzögern um etwa 0,16 s. Das merkt man im Gespräch als Verzögerung. Die Kausalität eines steilen Filters kostet Zeit, und zwar umso mehr, je schmaler das Band ist.
:::
:::

::::formelsammlung
**Kausal gefensterter Tiefpass**

$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}$$

Impulsantwort um $t_0$ verzögert und mit einem symmetrischen Fenster der Breite $2t_0$ abgeschnitten. Das Abschneiden ist im Spektrum eine Faltung mit dem si-Spektrum des Fensters; $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ ist die Verzögerung, die Phase ist linear. Je größer $t_0$, desto schmaler der Übergang, desto später die Antwort.

**Nötige Verzögerung**

$$\frac{1}{2\pi f_\mathrm g|t|}<0{,}01\qquad\Longrightarrow\qquad t_0\approx16/f_\mathrm g$$

Die Hüllkurve der si-Funktion fällt wie $1/(2\pi f_\mathrm g|t|)$; so groß muss $t_0$ sein, damit der abgeschnittene Teil vor $t=0$ unter 1 % des Maximums liegt.
::::

::::lernkarten
:::karte formel Kausal gefensterter Tiefpass
Wie lauten Impulsantwort und Frequenzgang des kausal angenäherten Tiefpasses, der um $t_0$ verzögert und mit einem Fenster der Breite $2t_0$ abgeschnitten wird?
---
$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)$ und $H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: das ideale Rechteck, gefaltet mit dem si-Spektrum des Fensters, mal die Verzögerung.
--- falsch
$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)$ und $H_k(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\cdot2t_0\operatorname{si}(2\pi t_0f)\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: das ideale Rechteck, multipliziert mit dem si-Spektrum des Fensters, mal die Verzögerung.
--- falsch
$h_k(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)\,\varepsilon(t)$ und $H_k(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: Man schneidet den Teil bei $t<0$ einfach ab; der Frequenzgang bleibt dabei das ideale Rechteck, nur mit einer Verzögerung um $t_0$.
--- falsch
$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)$ und $H_k(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: Die Verschiebung allein macht das Filter kausal, weil die si-Funktion nach rechts rückt; ein Fenster braucht man dafür nicht.
:::
:::karte zusammenhang Abschneiden ist Faltung im Spektrum
Warum bekommt der Frequenzgang des kausal angenäherten Tiefpasses an der Kante einen Übergangsbereich und Wellen?
---
Das Abschneiden der Impulsantwort ist eine Multiplikation mit einem Fenster, im Spektrum also eine Faltung mit dessen si-Spektrum. Diese Faltung verschmiert die scharfe Kante und erzeugt die Wellen.
--- falsch
Weil die Verzögerung um $t_0$ den Betrag des Frequenzgangs verändert: Der Faktor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ dämpft hohe Frequenzen stärker als tiefe und rundet so die senkrechte Kante des Rechtecks ab.
--- falsch
Weil das Abschneiden im Spektrum eine Multiplikation mit dem si-Spektrum des Fensters ist: Wo die si-Funktion negativ wird, kehrt sich der Frequenzgang um, und so entstehen die Wellen.
--- falsch
Weil ein kausales Filter immer eine nichtlineare Phase hat: Verschiedene Frequenzen werden verschieden verzögert, und diese Laufzeitunterschiede zeigen sich im Betrag als Wellen an der Kante.
:::
:::karte zusammenhang Lineare Phase der kausalen Näherung
Welche Phase hat der kausal angenäherte Tiefpass, und was bedeutet das für die Verzögerung der einzelnen Frequenzen?
---
Der Faktor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ ist eine reine Verzögerung: Das Filter hat eine lineare Phase und verzögert alle Frequenzen gleich um $t_0$. Je größer $t_0$, desto später kommt die Antwort.
--- falsch
Das Abschneiden zerstört die lineare Phase: Weil die Impulsantwort nicht mehr vollständig ist, kommen die Frequenzen an der Kante später an als die tiefen Frequenzen im Durchlassbereich.
--- falsch
Die Phase ist null wie beim idealen Tiefpass, weil die Verzögerung nur die Impulsantwort verschiebt und eine Verschiebung in der Zeit den Frequenzgang nicht verändert.
--- falsch
Der Faktor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ ist eine Dämpfung: Er senkt den Betrag mit wachsender Frequenz, sodass die hohen Frequenzen im Durchlassbereich schwächer ankommen als die tiefen.
:::
:::karte zusammenhang Kausalität kostet Zeit
Was gewinnt und was verliert man, wenn man beim kausal angenäherten Tiefpass die Verzögerung $t_0$ vergrößert?
---
Je größer $t_0$, desto schmaler wird der Übergangsbereich, weil das längere Fenster ein schmaleres si-Spektrum hat. Dafür kommt die Antwort später: Die Kausalität eines steilen Filters kostet Zeit.
--- falsch
Je größer $t_0$, desto breiter wird der Übergangsbereich, weil mehr von der si-Funktion übrig bleibt und deren Nebenschwingungen die Kante verschmieren; dafür kommt die Antwort früher.
--- falsch
Je größer $t_0$, desto kleiner werden die Wellen im Frequenzgang, bis sie ganz verschwinden; die Verzögerung spielt dabei keine Rolle, weil sie nur die Phase betrifft und nicht den Betrag des Frequenzgangs.
--- falsch
Die Verzögerung $t_0$ hat keinen Einfluss auf den Frequenzgang, nur auf die Laufzeit; der Übergangsbereich hängt allein von der Grenzfrequenz $f_\mathrm g$ ab, nicht von der Fensterbreite.
:::
:::karte herleitung Nötige Verzögerung
Wie folgt aus der Hüllkurve der si-Funktion, dass man für einen abgeschnittenen Rest unter 1 % des Maximums etwa $t_0\approx16/f_\mathrm g$ braucht?
---
Die Hüllkurve der si-Funktion fällt, bezogen auf das Maximum, wie $1/(2\pi f_\mathrm g|t|)$, weil der Sinus im Zähler höchstens 1 ist.
---
Der abgeschnittene Teil vor $t=0$ liegt nach der Verschiebung mindestens $t_0$ vom Maximum entfernt, weil die si-Funktion um $t_0$ nach rechts gerückt ist.
---
Man verlangt $\frac{1}{2\pi f_\mathrm g|t|}<0{,}01$ für alle diese Zeiten, weil der Rest unter 1 % liegen soll; daraus folgt $|t|>\frac{100}{2\pi f_\mathrm g}$.
---
Es ergibt sich $t_0\approx16/f_\mathrm g$, weil $100/(2\pi)\approx15{,}9$ ist.
:::
:::karte zusammenhang Verzögerung und Bandbreite
Wie hängt die für die kausale Näherung nötige Verzögerung von der Grenzfrequenz ab, und was folgt daraus für eine Kette solcher Filter?
---
Die Verzögerung $t_0\approx16/f_\mathrm g$ ist umgekehrt proportional zur Grenzfrequenz: Je schmaler das Band, desto länger muss man warten. Bei $f_\mathrm g=1$ kHz sind es etwa 16 ms, zehn solche Filter verzögern schon um 0,16 s.
--- falsch
Die Verzögerung wächst mit der Grenzfrequenz, weil ein breites Band mehr Frequenzen enthält, deren si-Anteile länger nachklingen. Bei $f_\mathrm g=1$ kHz sind es etwa 16 s, bei schmalen Bändern dagegen nur wenige Millisekunden.
--- falsch
Die Verzögerung ist unabhängig von der Grenzfrequenz immer etwa 16 ms, weil die Hüllkurve der si-Funktion stets gleich schnell abfällt; eine Kette aus zehn Filtern verzögert deshalb ebenfalls nur 16 ms.
--- falsch
Die Verzögerung ist $t_0\approx16/f_\mathrm g$, sie addiert sich in einer Kette aber nicht: Zehn Filter hintereinander verzögern zusammen nur so viel wie das langsamste, bei $f_\mathrm g=1$ kHz also etwa 16 ms.
:::
::::
