---
title: Stufe 4: Abtastung im Frequenzbereich
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Abtastung und zeitdiskrete Systeme
order: 3240500
summary: Dasselbe Prinzip gilt mit vertauschten Rollen: Tastet man das Spektrum ab, wird das Signal periodisch.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Dasselbe Prinzip gilt mit vertauschten Rollen: Tastet man das Spektrum ab, wird das Signal periodisch.
:::

Ein Spektrum, das nur bei den Frequenzen $kF$ bekannt ist, ist ein Kamm gewichteter Dirac-Impulse. Mit dem Faktor $F$ sind die Gewichte genau die Fourier-Koeffizienten aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html):

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

Das zugehörige Signal ist das Original, periodisch mit $1/F$ wiederholt. Ist das Signal kürzer als $1/F$, überlappen sich die Wiederholungen nicht. Dann gewinnt man es mit einem Zeitfenster zurück, und das Spektrum mit si-Funktionen:

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**Kurz gesagt:** Diskret in der Zeit heißt periodisch im Spektrum, diskret im Spektrum heißt periodisch in der Zeit. Das zweite ist die Fourier-Reihe aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Ihre Koeffizienten sind Abtastwerte des Spektrums eines Einzelimpulses, $S_p(k)=F\cdot S(kF)$.
