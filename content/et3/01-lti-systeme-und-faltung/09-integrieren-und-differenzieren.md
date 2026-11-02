---
title: Stufe 8: Integrieren und Differenzieren
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / LTI-Systeme und Faltung
order: 3210900
summary: Integrator und Differenzierer sind LTI-Systeme.
tags: Integrator, Differenzierer, Doppelimpuls
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Integrator und Differenzierer sind LTI-Systeme. Mit ihnen hängen Sprungantwort und Impulsantwort zusammen, und man kann die Impulsantwort des RC-Glieds aus seiner Sprungantwort gewinnen.
:::

**Der Integrator.** Ersetzt man in [(7.6)](der-dirac-impuls.html#gl-7-6) $\delta$ durch ein beliebiges $s$, folgt dieselbe Rechnung:

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

Ein System mit der Impulsantwort $\varepsilon(t)$ bildet das laufende Integral seines Eingangs, es heißt __Integrator__. Liest man [(8.1)](#gl-8-1) mit vertauschten Rollen ($\varepsilon*s$), sagt sie: **Die Sprungantwort eines Systems ist das laufende Integral seiner Impulsantwort.** Probe am RC-Glied: $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$, genau [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5). Zwei unabhängige Wege, Differentialgleichung und Faltung, geben dasselbe.

**Der Differenzierer.** Integrator und __Differenzierer__ nacheinander lassen jedes Signal unverändert, die Kette ist ideal verzerrungsfrei. Die Impulsantwort des Differenzierers ist deshalb die Distribution $\delta'(t)$ (__Doppelimpuls__), festgelegt durch

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

Näherungsweise ist $\delta'$ ein schmaler Doppelrechteckimpuls: erst ein Rechteck der Höhe $+1/T_0^2$, dann eines der Höhe $-1/T_0^2$, jedes $T_0$ breit. Gezeichnet wird er als Pfeilpaar nach oben und unten.

**Impulsantwort = Ableitung der Sprungantwort.** Weil $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ und das System linear und zeitinvariant ist, gilt $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{Sprungantwort})$. Für das RC-Glied mit der Produktregel:

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

Der zweite Summand verschwindet nach [(7.2)](der-dirac-impuls.html#gl-7-2): $(1-\mathrm{e}^{0})\,\delta(t)=0$. Der Mechanismus dahinter: Die Sprungantwort des RC-Glieds springt nicht, der Kondensator braucht Zeit zum Laden. Nur eine springende Sprungantwort erzeugt einen Dirac-Impuls in $h$ (Aufgabe [9](#aufg-9)).

:::aufgabe Aufgabe 9 ★★ Hochpass: ein Dirac-Impuls in der Impulsantwort
<span class="anker" id="aufg-9"></span>

Vertauscht man $R$ und $C$, wird die Spannung an $R$ abgegriffen (CR-Hochpass, $RC=1$ s). Seine Sprungantwort ist $\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Begründe die Sprungantwort mit dem Mechanismus: Was liegt im ersten Moment an $R$, was nach langer Zeit?

</li>

<li>

Bestimme die Impulsantwort durch Ableiten. Was bedeutet der Dirac-Anteil physikalisch?

</li>

<li>

Prüfe: Integrieren der Impulsantwort muss die Sprungantwort zurückgeben.

</li>

</ol>

:::loesung
(a) Im ersten Moment ist der Kondensator leer, über ihm liegt keine Spannung. Die vollen 1 V liegen an $R$. Danach lädt der Strom den Kondensator, seine Spannung steigt wie $1-\mathrm{e}^{-t}$, an $R$ bleibt $\mathrm{e}^{-t}$. Nach langer Zeit ist der Kondensator voll, es fließt kein Strom, an $R$ liegt nichts mehr.

(b) Produktregel:

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

Hier springt die Sprungantwort bei $t=0$ von 0 auf 1, deshalb bleibt der Dirac-Anteil stehen. Physikalisch: Ein unendlich kurzer Stoß geht vollständig durch, weil der Kondensator in null Zeit keine Spannung aufbauen kann. Die Ladung, die der Stoß auf den Kondensator gebracht hat, fließt danach über $R$ wieder ab, in Gegenrichtung: $-\mathrm{e}^{-t}$.

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$.
:::
:::
