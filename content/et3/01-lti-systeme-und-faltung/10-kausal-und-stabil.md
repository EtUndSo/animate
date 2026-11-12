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

::::kurzfassung
Zwei Eigenschaften, die jedes reale System haben soll, liest man bei einem LTI-System direkt an der Impulsantwort $h(t)$ ab.

Ein System heißt __kausal__, wenn der Ausgang nicht vor dem Eingang beginnt. Für ein LTI-System heißt das $h(t)=0$ für $t<0$: Ein Stoß zur Zeit 0 kann vorher keine Wirkung haben. In der Faltung tragen dann nur Stöße der Vergangenheit bei, $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$. Ein System heißt __stabil__, genauer BIBO-stabil (bounded input, bounded output), wenn es auf jeden beschränkten Eingang $|s(t)|\le A<\infty$ mit einem beschränkten Ausgang antwortet. Ein LTI-System ist genau dann stabil, wenn seine Impulsantwort absolut integrierbar ist:

$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty .$$

Der Grund: Ist das Integral endlich, begrenzt die Dreiecksungleichung den Ausgang durch $A\int|h(\tau)|\,\mathrm{d}\tau$. Ist es unendlich, wählt man den ungünstigsten beschränkten Eingang $s(t_1-\tau)=\operatorname{sign}h(\tau)$, also immer $\pm1$ mit dem Vorzeichen von $h$. Dann addieren sich alle Beiträge, und $g(t_1)$ wird unendlich, obwohl $|s|\le1$ ist.

Falle: Instabil heißt nicht, dass der Ausgang zu einer bestimmten Zeit unendlich werden muss. Der Integrator hat $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$; auf den beschränkten Sprung antwortet er mit der Rampe $t\,\varepsilon(t)$, die zu jeder Zeit endlich, aber nicht beschränkt ist.
::::

::::formelsammlung
**Kausalität**

$$h(t)=0\quad\text{für }t<0$$

Für LTI-Systeme gleichwertig damit, dass der Ausgang nicht vor dem Eingang beginnt.

**Faltung bei kausalen Systemen**

$$g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$$

Nur Stöße der Vergangenheit tragen bei.

**Beschränkter Eingang**

$$|s(t)|\le A<\infty$$

BIBO-stabil (bounded input, bounded output): Jeder solche Eingang ergibt einen beschränkten Ausgang.

**Stabilitätsbedingung**

$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty$$

Notwendig und hinreichend für die Stabilität eines LTI-Systems. Beispiele: RC-Glied und ideales Laufzeitglied stabil ($\int|h|=1$), Integrator instabil.

**Schranke des Ausgangs**

$$|g(t)|\le A\int|h(\tau)|\,\mathrm{d}\tau$$

Aus der Dreiecksungleichung für Integrale und $|s|\le A$; zeigt, dass die Bedingung hinreicht.

**Ungünstigster beschränkter Eingang**

$$s(t_1-\tau)=\operatorname{sign}h(\tau)$$

Immer $\pm1$ mit dem Vorzeichen von $h$; ergibt $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau$ und zeigt, dass die Bedingung notwendig ist.
::::

::::lernkarten
:::karte begriff kausal
Wann heißt ein System kausal, und woran erkennt man das an der Impulsantwort eines LTI-Systems?
---
Wenn der Ausgang nicht vor dem Eingang beginnt. Für ein LTI-System heißt das $h(t)=0$ für $t<0$: Ein Stoß zur Zeit 0 kann vorher keine Wirkung haben.
--- falsch
Wenn der Ausgang nicht nach dem Eingang endet. Für ein LTI-System heißt das $h(t)=0$ für $t>0$: Nach dem Stoß darf keine Wirkung mehr übrig bleiben.
--- falsch
Wenn der Ausgang nicht vor dem Eingang beginnt. Für ein LTI-System heißt das $h(0)=0$: Im Moment des Stoßes darf das System noch nicht antworten.
--- falsch
Wenn jede Wirkung eine Ursache hat. Für ein LTI-System heißt das $h(t)\neq0$ für alle $t$, denn wo $h$ null ist, hätte ein Stoß keine Wirkung.
:::
:::karte begriff stabil
Wann heißt ein System stabil im Sinne der BIBO-Stabilität?
---
Wenn es auf jeden beschränkten Eingang $|s(t)|\le A<\infty$ mit einem beschränkten Ausgang antwortet. BIBO steht für bounded input, bounded output.
--- falsch
Wenn es auf mindestens einen beschränkten Eingang mit einem beschränkten Ausgang antwortet. BIBO steht für bounded input, bounded output.
--- falsch
Wenn sein Ausgang nie größer ist als sein Eingang, $|g(t)|\le|s(t)|$ für alle $t$. BIBO steht für bounded input, bounded output.
--- falsch
Wenn es auf einen Sprung mit einem Ausgang antwortet, der nach langer Zeit einen festen Endwert erreicht. BIBO steht für bounded input, balanced output.
:::
:::karte formel Stabilitätsbedingung
Welche Bedingung an die Impulsantwort ist notwendig und hinreichend dafür, dass ein LTI-System stabil ist?
---
$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty$: Die Impulsantwort muss absolut integrierbar sein. Das RC-Glied mit $\int|h|=1$ ist stabil, der Integrator mit $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$ nicht.
--- falsch
$\int_{-\infty}^{\infty}h(\tau)\,\mathrm{d}\tau<\infty$: Die Fläche der Impulsantwort muss endlich sein, wobei sich positive und negative Anteile ausgleichen dürfen. Das RC-Glied mit der Fläche 1 ist stabil.
--- falsch
$|h(t)|<\infty$ für alle $t$: Die Impulsantwort muss beschränkt sein. Das RC-Glied ist deshalb stabil, ebenso der Integrator, dessen Impulsantwort $\varepsilon(t)$ nie größer als 1 wird.
--- falsch
$h(t)\to0$ für $t\to\infty$: Die Impulsantwort muss abklingen; wie schnell, spielt keine Rolle, weil jede abklingende Antwort endlich bleibt. Das RC-Glied ist deshalb stabil.
:::
:::karte herleitung Stabilitätsbedingung hinreichend und notwendig
Wie zeigt man, dass $\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty$ für die Stabilität eines LTI-Systems hinreicht und notwendig ist?
---
Hinreichend: Mit $|s|\le A$ ist $|g(t)|$ höchstens $\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau$, weil der Betrag eines Integrals höchstens das Integral des Betrags ist (Dreiecksungleichung für Integrale).
---
Ist dieses Integral endlich, ist $g$ beschränkt, weil die Schranke für alle $t$ dieselbe ist.
---
Notwendig: Ist $\int|h|=\infty$, wählt man den ungünstigsten beschränkten Eingang $s(t_1-\tau)=\operatorname{sign}h(\tau)$, weil er immer $\pm1$ ist und überall das Vorzeichen von $h$ hat.
---
Dann ist $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$, obwohl $|s|\le1$ ist, weil jedes Produkt im Integral den Betrag von $h$ ergibt und sich nichts aufhebt.
:::
:::karte zusammenhang Integrator instabil
Warum ist der Integrator nicht stabil, obwohl seine Impulsantwort $\varepsilon(t)$ nie größer als 1 wird?
---
Für die Stabilität zählt die Fläche von $|h|$, nicht ihre Höhe, und $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$. Auf den beschränkten Sprung antwortet der Integrator deshalb mit der unbeschränkten Rampe $t\,\varepsilon(t)$.
--- falsch
Weil seine Impulsantwort bei $t=0$ springt; jeder Sprung in $h$ macht ein System instabil, weil der Ausgang an dieser Stelle nicht stetig ist und dort über alle Grenzen wachsen kann.
--- falsch
Weil der Sprung als Eingang nicht beschränkt ist: Er bleibt für alle Zeiten 1, und ein Eingang, der nie endet, zählt nicht als beschränkt, auch wenn er nie größer als 1 wird.
--- falsch
Weil er nicht kausal ist: Das laufende Integral braucht den ganzen Eingang bis $t=\infty$, und dieses Integral kann unendlich werden, auch wenn der Eingang selbst beschränkt ist.
:::
:::karte zusammenhang Faltung bei kausalen Systemen
Warum genügt bei einem kausalen LTI-System das Faltungsintegral bis zur oberen Grenze $t$?
---
Weil $h$ für negative Argumente null ist und das Argument $t-\tau$ für Stöße nach dem Zeitpunkt $t$ negativ wird. Nur Stöße der Vergangenheit tragen bei: $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$.
--- falsch
Weil der Eingang nach dem Zeitpunkt $t$ noch nicht bekannt ist. Man setzt ihn vorläufig null und berechnet nur $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$; später muss man das Ergebnis korrigieren.
--- falsch
Weil bei einem kausalen System der Eingang $s(\tau)$ für $\tau>t$ null ist. Das System sorgt selbst dafür, dass nach dem Zeitpunkt $t$ kein Eingang mehr ankommt, den es verarbeiten müsste.
--- falsch
Weil die Impulsantwort eines kausalen Systems nach der Zeit $t$ abgeklungen ist. Stöße, die länger als $t$ zurückliegen, tragen deshalb nicht mehr bei, und das Integral endet bei $t$.
:::
:::karte zusammenhang Eingang im Voraus
Ist das System mit der Impulsantwort $h(t)=\delta(t+1)$ kausal, und ist es stabil?
---
Nicht kausal, aber stabil. $\delta(t+1)$ wirkt bei $t=-1<0$, also ist $g(t)=s(t+1)$: Das System „sieht“ den Eingang eine Sekunde im Voraus. Stabil ist es, weil $\int|h|=1$ ist.
--- falsch
Kausal und stabil. Es verzögert den Eingang um eine Sekunde wie ein ideales Laufzeitglied, denn $\delta(t+1)$ wirkt eine Sekunde nach dem Stoß, und $\int|h|=1$ ist endlich.
--- falsch
Kausal, aber instabil. Ein Dirac-Impuls ist unendlich hoch, deshalb ist auch $\int|h|$ unendlich, und auf einen beschränkten Eingang folgt ein unbeschränkter Ausgang.
--- falsch
Weder kausal noch stabil. Es sieht den Eingang im Voraus, und ein System, das in die Zukunft sieht, kann auf einen beschränkten Eingang keinen beschränkten Ausgang liefern.
:::
:::karte zusammenhang Wachsende Impulsantwort
Warum ist das System mit $h(t)=\mathrm{e}^{t}\varepsilon(t)$ instabil, und welcher beschränkte Eingang zeigt das?
---
Seine Impulsantwort ist nicht absolut integrierbar, $\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$. Schon der Sprung $\varepsilon(t)$ erzeugt den unbeschränkten Ausgang $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$.
--- falsch
Weil seine Impulsantwort bei $t=0$ den Wert 1 hat; ein stabiles System muss mit $h(0)=0$ beginnen. Der Dirac-Impuls $\delta(t)$ zeigt das, denn er erzeugt den Ausgang $\mathrm{e}^t$.
--- falsch
Weil $h$ bei $t=0$ springt; der Sprung $\varepsilon(t)$ erzeugt an dieser Stelle einen Dirac-Impuls am Ausgang, und ein Dirac-Impuls ist unbeschränkt.
--- falsch
Es ist nur für unbeschränkte Eingänge instabil: Erst ein Eingang wie $\mathrm{e}^t$ erzeugt einen unbeschränkten Ausgang, jeder beschränkte Eingang bleibt beschränkt.
:::
::::
