---
title: Stufe 9: Kausal und stabil
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3211000
summary: Zwei Eigenschaften, die jedes reale System haben soll, lassen sich direkt an h(t) ablesen.
tags: kausal, stabil
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Zwei Eigenschaften, die jedes reale System haben soll, lassen sich direkt an $h(t)$ ablesen.
:::

:::definition Definition 9.1 (Kausal, stabil)
<span class="anker" id="satz-9-1"></span>

Ein System heißt __kausal__, wenn der Ausgang nicht vor dem Eingang beginnt. Für ein LTI-System heißt das

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{für }t<0. \tag{9.1}$$

Ein System heißt __stabil__ (genauer BIBO-stabil, *bounded input, bounded output*), wenn es auf jeden beschränkten Eingang $|s(t)|\le A<\infty$ mit einem beschränkten Ausgang antwortet.
:::

Kausal: Ein Stoß zur Zeit 0 kann vorher keine Wirkung haben. In der Faltung tragen dann nur Stöße der Vergangenheit bei, $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$.

:::satz Satz 9.2 (Stabilitätsbedingung)
<span class="anker" id="satz-9-2"></span>

Ein LTI-System ist genau dann stabil, wenn seine Impulsantwort absolut integrierbar ist:

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung Stabilitätsbedingung
⁠**Hinreichend.** Mit der Dreiecksungleichung für Integrale und $|s|\le A$:

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

Ist das Integral endlich, ist $g$ beschränkt.

⁠**Notwendig.** Ist $\int|h|=\infty$, wählt man den ungünstigsten beschränkten Eingang: $s(t_1-\tau)=\operatorname{sign}h(\tau)$, also immer $\pm1$ mit dem Vorzeichen von $h$. Dann ist $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$, obwohl $|s|\le1$.
:::

Beispiele: Das RC-Glied hat $\int|h|=1$ und ist stabil. Das ideale Laufzeitglied ($\int|\delta(t-t_0)|\mathrm{d} t=1$) ist stabil. Der Integrator hat $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$ und ist instabil: Auf den beschränkten Sprung antwortet er mit der unbeschränkten Rampe $t\,\varepsilon(t)$.

:::aufgabe Aufgabe 10 ★★ Kausal? Stabil?
<span class="anker" id="aufg-10"></span>

Untersuche (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$, (b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$, (c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$, (d) $h(t)=\mathrm{e}^{-|t|}$, (e) $h(t)=\delta(t+1)$. Gib bei jedem instabilen System einen beschränkten Eingang an, der einen unbeschränkten Ausgang erzeugt.

:::loesung
(a) Kausal, $\int|h|=\tfrac12$: stabil.

(b) Kausal, $\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$: instabil. Der Sprung $\varepsilon(t)$ erzeugt $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$, unbeschränkt.

(c) Kausal, $\int|h|=1$: stabil. Das System bildet das Integral des Eingangs über die letzte Sekunde (gleitendes Fenster).

(d) Nicht kausal, denn $h(t)\neq0$ für $t<0$. $\int\mathrm{e}^{-|t|}\mathrm{d} t=2$: stabil.

(e) $\delta(t+1)$ ist für $t=-1<0$ wirksam: $g(t)=s(t+1)$, das System „sieht“ den Eingang eine Sekunde im Voraus. Nicht kausal, aber stabil ($\int|h|=1$).
:::
:::
