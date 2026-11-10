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
