---
title: Stufe 1: Energie und Leistung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260200
summary: Bevor man Signale vergleicht, braucht man ein Maß für ihre „Größe“.
tags: Signalenergie, Energiesignal, Leistung, Leistungssignal
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man Signale vergleicht, braucht man ein Maß für ihre „Größe“. In der Systemtheorie ist das die Energie, bei unendlich langen Signalen die Leistung.
:::

An einem Widerstand $R$ wird in der Zeit von $t_1$ bis $t_2$ die Energie $\frac1R\int u^2\mathrm{d} t$ in Wärme umgesetzt. Ohne den Faktor $1/R$ heißt der Ausdruck __Signalenergie__:

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

Ist sie endlich, heißt $s$ __Energiesignal__ (zum Beispiel jeder Impuls). Dauert ein Signal unendlich lange an, ohne abzuklingen (ein Kosinus, ein Sprung), ist die Energie unendlich. Dann misst man die mittlere __Leistung__:

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

Ist sie endlich, heißt $s$ __Leistungssignal__. Bei periodischen Signalen genügt die Mittelung über eine Periode. Für Dirac-Impulse sind Energie und Leistung nicht definiert ($\delta^2$ gibt es nicht).

:::aufgabe Aufgabe 1 ★ Energie oder Leistung?
<span class="anker" id="aufg-1"></span>

Bestimme Energie oder Leistung von (a) $a\operatorname{rect}(t/T)$, (b) $\varepsilon(t)\mathrm{e}^{-t}$, (c) $A\cos(2\pi Ft)$, (d) $\varepsilon(t)$.

:::loesung
(a) $E=a^2|T|$. (b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$. (c) Energie unendlich, Leistung $\frac{A^2}{2}$ (Mittelwert von $\cos^2$ ist $\frac12$). (d) Energie unendlich, Leistung $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$: Die Hälfte der Zeit ist das Signal 1.
:::
:::

::::formelsammlung
**Signalenergie**

$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t$$

Die Energie $\frac1R\int u^2\mathrm{d} t$ am Widerstand ohne den Faktor $1/R$. Ist sie endlich, heißt $s$ Energiesignal (zum Beispiel jeder Impuls).

**Mittlere Leistung**

$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t$$

Für Signale unendlicher Energie, die nicht abklingen (Kosinus, Sprung). Ist sie endlich, heißt $s$ Leistungssignal. Bei periodischen Signalen genügt die Mittelung über eine Periode. Für Dirac-Impulse sind Energie und Leistung nicht definiert.
::::

::::lernkarten
:::karte begriff Signalenergie
Was gibt die Signalenergie $E_s$ eines Signals $s(t)$ an, und wie hängt sie mit der Energie an einem Widerstand zusammen?
---
Das Integral des Betragsquadrats über alle Zeiten: $E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t$. Es ist die Energie $\frac1R\int u^2\mathrm{d} t$, die ein Widerstand in Wärme umsetzt, ohne den Faktor $1/R$.
--- falsch
Das Integral des Signals selbst über alle Zeiten: $E_s=\int_{-\infty}^{\infty}s(t)\,\mathrm{d} t$. Es ist die Fläche unter der Kurve, wobei sich positive und negative Teile gegenseitig aufheben.
--- falsch
Das größte Betragsquadrat des Signals, $E_s=\max|s(t)|^2$. Es entspricht der Spitzenleistung, die ein Widerstand von $1\,\Omega$ im ungünstigsten Augenblick in Wärme umsetzt.
--- falsch
Das Integral des Betragsquadrats, geteilt durch den Widerstand: $E_s=\frac1R\int|s(t)|^2\,\mathrm{d} t$. Ohne Angabe eines Widerstands $R$ lässt sich die Energie eines Signals deshalb nicht bestimmen.
:::
:::karte begriff Energiesignal
Wann nennt man ein Signal $s(t)$ ein Energiesignal, und welche Signale gehören typischerweise dazu?
---
Ein Signal mit endlicher Signalenergie $E_s$. Dazu gehört zum Beispiel jeder Impuls, etwa ein Rechteckimpuls oder der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$.
--- falsch
Ein Signal mit endlicher mittlerer Leistung. Dazu gehören vor allem Dauersignale wie ein Kosinus oder ein Sprung, deren Energie sich gleichmäßig über alle Zeiten verteilt.
--- falsch
Ein Signal mit unendlicher Signalenergie. Dazu gehören Signale, die unendlich lange andauern, ohne abzuklingen, etwa ein Kosinus oder ein Sprung.
--- falsch
Ein Signal, das einen Dirac-Impuls enthält. Der Dirac-Impuls bündelt seine Energie in einem einzigen Augenblick und ist deshalb das Musterbeispiel eines Energiesignals.
:::
:::karte formel Mittlere Leistung
Wie misst man die Größe eines Signals, dessen Energie unendlich ist, und wie lautet die Formel dafür?
---
Mit der mittleren Leistung $L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t$, also dem Mittelwert des Betragsquadrats über ein immer längeres Zeitfenster. Bei periodischen Signalen genügt eine Periode.
--- falsch
Mit der mittleren Leistung $L_s=\lim_{T\to\infty}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t$: Man integriert das Betragsquadrat über ein immer längeres Zeitfenster, ohne durch dessen Länge zu teilen.
--- falsch
Mit der mittleren Leistung $L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}s(t)\,\mathrm{d} t$, also dem Mittelwert des Signals selbst über ein immer längeres Zeitfenster. Bei periodischen Signalen genügt eine Periode.
--- falsch
Mit der mittleren Leistung $L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t$, die man bei periodischen Signalen aber über alle Zeiten mitteln muss, weil eine einzelne Periode nichts über den Rest des Signals aussagt.
:::
:::karte begriff Leistungssignal
Wann nennt man ein Signal ein Leistungssignal, und welche Beispiele gibt es dafür?
---
Ein Signal mit unendlicher Energie, aber endlicher mittlerer Leistung $L_s$. Beispiele sind Signale, die unendlich lange andauern, ohne abzuklingen, etwa ein Kosinus oder ein Sprung.
--- falsch
Ein Signal mit endlicher Energie, dessen Leistung deshalb unendlich wird. Beispiele sind kurze Impulse, weil sie ihre ganze Energie in sehr kurzer Zeit abgeben.
--- falsch
Ein Signal mit unendlicher mittlerer Leistung, aber endlicher Energie. Beispiele sind Dirac-Impulse, die in einem einzigen Augenblick unbegrenzt viel Leistung tragen.
--- falsch
Ein Signal, das an einem Widerstand Leistung umsetzt, also jedes Spannungs- oder Stromsignal. Ob Energie oder Leistung endlich sind, spielt für diese Einteilung keine Rolle.
:::
:::karte formel Leistung eines Kosinus
Welche mittlere Leistung hat der Kosinus $A\cos(2\pi Ft)$, und warum ist er kein Energiesignal?
---
$L_s=\frac{A^2}{2}$, weil der Mittelwert von $\cos^2$ gleich $\frac12$ ist. Seine Energie ist unendlich, denn er dauert unendlich lange an, ohne abzuklingen.
--- falsch
$L_s=A^2$, weil $|\cos|$ höchstens 1 ist und die Leistung durch den Spitzenwert bestimmt wird. Seine Energie ist unendlich, weil er nie abklingt.
--- falsch
$L_s=0$, weil sich positive und negative Halbwellen über eine Periode aufheben. Seine Energie ist deshalb ebenfalls null, und er ist weder Energie- noch Leistungssignal.
--- falsch
$L_s=\frac{A}{\sqrt2}$, der Effektivwert des Kosinus. Seine Energie ist endlich, weil das Integral von $\cos^2$ über eine Periode endlich ist und sich jede Periode wiederholt.
:::
:::karte zusammenhang Leistung des Sprungs
Warum hat der Sprung $\varepsilon(t)$ die mittlere Leistung $\frac12$ und nicht 1?
---
Weil das Mittelungsfenster von $-T$ bis $T$ reicht und der Sprung nur in der Hälfte davon den Wert 1 hat: $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$.
--- falsch
Weil die halbe Leistung in der Sprungstelle bei $t=0$ steckt, wo das Signal unendlich steil ist; diesen Anteil erfasst das Integral über $|s(t)|^2$ nicht.
--- falsch
Weil man das Betragsquadrat bei jedem Signal noch durch 2 teilen muss: Der Faktor $\frac12$ tritt immer auf, so wie beim Kosinus mit der Leistung $\frac{A^2}{2}$.
--- falsch
Weil der Sprung ein Energiesignal mit der Energie $\frac12$ ist, die sich gleichmäßig über die Zeit verteilt; deshalb ist auch die mittlere Leistung $\frac12$.
:::
:::karte formel Energie eines Rechteckimpulses
Welche Signalenergie hat der Rechteckimpuls $a\operatorname{rect}(t/T)$, und warum?
---
$E=a^2|T|$: Das Betragsquadrat $a^2$ liegt während der Dauer $|T|$ an, außerhalb ist das Signal null. Die Höhe geht deshalb quadratisch ein.
--- falsch
$E=a|T|$: Die Energie ist die Fläche des Rechtecks, also Höhe mal Dauer, denn das Integral des Signals misst seine Größe.
--- falsch
$E=a^2$: Die Energie hängt nur von der Höhe ab; die Dauer spielt keine Rolle, weil das Signal nach dem Impuls wieder null ist.
--- falsch
$E=a^2T^2$: Höhe und Dauer gehen beide quadratisch ein, weil das Betragsquadrat des ganzen Rechtecks gebildet wird.
:::
:::karte zusammenhang Dirac-Impuls
Warum kann man einem Dirac-Impuls weder eine Energie noch eine Leistung zuordnen?
---
Weil beide Größen das Quadrat des Signals verlangen und es $\delta^2$ nicht gibt. Der Dirac-Impuls ist deshalb weder Energie- noch Leistungssignal.
--- falsch
Weil seine Energie null ist: Er dauert nur einen Augenblick, und über eine Zeitspanne der Länge null ergibt das Integral von $|s|^2$ stets null.
--- falsch
Weil er nicht kausal ist: Energie und Leistung sind nur für Signale erklärt, die erst bei $t=0$ beginnen, und ein Dirac-Impuls kann an jeder Stelle sitzen.
--- falsch
Weil seine Energie zwar endlich ist, aber in einem einzigen Augenblick anfällt; Energie und Leistung sind nur für Signale erklärt, die eine Zeit lang andauern.
:::
::::
