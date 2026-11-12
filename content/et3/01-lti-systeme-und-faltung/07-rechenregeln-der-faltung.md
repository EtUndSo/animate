---
title: Stufe 6: Rechenregeln der Faltung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210700
summary: Die Faltung verhält sich in vielem wie eine Multiplikation.
tags: Faltungsprodukt, ideal verzerrungsfrei
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Faltung verhält sich in vielem wie eine Multiplikation. Jede Rechenregel hat eine Bedeutung für Systeme.
:::

Man schreibt das Faltungsintegral kurz als __Faltungsprodukt__ $g(t)=s(t)*h(t)$. Gleichung [(4.1)](das-faltungsintegral.html#gl-4-1) lautet dann $s(t)=s(t)*\delta(t)$.

<ol class="al">

<li>

⁠**Einselement.** $s*\delta=s$: Der Dirac-Impuls spielt die Rolle der Eins. Ein System mit $h(t)=\delta(t)$ gibt jedes Signal unverändert weiter, es heißt __ideal verzerrungsfrei__.

</li>

<li>

⁠**Kommutativgesetz.** $s*h=h*s$. Bedeutung: Eingang und Impulsantwort dürfen die Rollen tauschen. Das System mit der Impulsantwort $s$ antwortet auf den Eingang $h$ genauso wie das System $h$ auf den Eingang $s$.

</li>

<li>

⁠**Assoziativgesetz.** $(f*s)*h=f*(s*h)$. Bedeutung: Zwei Systeme in Kette wirken wie ein System, dessen Impulsantwort die Faltung der beiden Impulsantworten ist.

</li>

<li>

⁠**Distributivgesetz.** $f*(s+h)=f*s+f*h$. Bedeutung: Zwei parallel geschaltete Systeme, deren Ausgänge addiert werden, wirken wie ein System mit der Summe der Impulsantworten.

</li>

<li>

⁠**Komplexe Signale.** Weil die Faltung linear ist, zerfällt sie in Real- und Imaginärteile:

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung Kommutativgesetz
Substitution $\tau'=t-\tau$, also $\tau=t-\tau'$ und $\mathrm{d}\tau=-\mathrm{d}\tau'$. Die Grenzen $\tau=\mp\infty$ werden zu $\tau'=\pm\infty$, das Vertauschen hebt das Minuszeichen auf:

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke 7
Oben: Kettenschaltung, Impulsantwort $h_1*h_2$ (Assoziativgesetz). Unten: Parallelschaltung mit Addition, Impulsantwort $h_1+h_2$ (Distributivgesetz).
:::

:::aufgabe Aufgabe 7 ★★ Zwei RC-Glieder in Kette
<span class="anker" id="aufg-7"></span>

Zwei RC-Glieder mit $RC=1$ s werden hintereinandergeschaltet. Das zweite belaste das erste nicht (zum Beispiel mit einem Spannungsfolger dazwischen).

<ol class="al">

<li>

Berechne die Impulsantwort der Kette, $h*h$ mit $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

</li>

<li>

Wann ist sie maximal, und wie groß ist ihre Fläche?

</li>

<li>

Warum braucht man die Bedingung „belastet nicht“?

</li>

</ol>

:::loesung
(a) Für $t\ge0$:

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

Also $h_{\text{Kette}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$.

(b) Ableitung $(1-t)\mathrm{e}^{-t}=0$ bei $t=1$ s, Maximum $\mathrm{e}^{-1}=0{,}368$. Fläche $\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$ (Produkt der Flächen).

(c) Ohne Entkopplung zieht das zweite RC-Glied Strom aus dem ersten Kondensator. Dann ist die Spannung am ersten Kondensator nicht mehr die eines unbelasteten RC-Glieds, und die Kette hat nicht $h*h$ als Impulsantwort. Sie bleibt ein LTI-System, aber mit einer anderen Impulsantwort. Die Faltung der Einzelantworten setzt voraus, dass jedes System seinen Eingang nicht zurückbeeinflusst.
:::
:::

::::kurzfassung
Die Faltung verhält sich in vielem wie eine Multiplikation, und jede ihrer Rechenregeln hat eine Bedeutung für Systeme.

Man schreibt das Faltungsintegral kurz als __Faltungsprodukt__ $g(t)=s(t)*h(t)$. Es gelten:

<ul>

<li>

Einselement: $s*\delta=s$. Ein System mit $h(t)=\delta(t)$ gibt jedes Signal unverändert weiter; es heißt __ideal verzerrungsfrei__.

</li>

<li>

Kommutativgesetz: $s*h=h*s$. Eingang und Impulsantwort dürfen die Rollen tauschen.

</li>

<li>

Assoziativgesetz: $(f*s)*h=f*(s*h)$. Zwei Systeme in Kette wirken wie eines mit der Impulsantwort $h_1*h_2$.

</li>

<li>

Distributivgesetz: $f*(s+h)=f*s+f*h$. Zwei parallele Systeme, deren Ausgänge addiert werden, wirken wie eines mit der Impulsantwort $h_1+h_2$.

</li>

</ul>

Weil die Faltung linear ist, zerfällt sie bei komplexen Signalen in Real- und Imaginärteile:

$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr].$$

Der Grund für das Kommutativgesetz ist die Substitution $\tau'=t-\tau$. Sie kehrt die Integrationsrichtung um, und das Vertauschen der Grenzen hebt das Minuszeichen aus $\mathrm{d}\tau=-\mathrm{d}\tau'$ wieder auf.

Falle: Die Impulsantwort $h_1*h_2$ der Kette setzt voraus, dass das zweite System das erste nicht belastet, etwa dank eines Spannungsfolgers dazwischen. Zieht ein zweites RC-Glied Strom aus dem ersten Kondensator, hat die Kette eine andere Impulsantwort.
::::

::::formelsammlung
**Faltungsprodukt**

$$g(t)=s(t)*h(t)$$

Kurzschreibweise für das Faltungsintegral.

**Einselement**

$$s*\delta=s$$

Ein System mit $h(t)=\delta(t)$ gibt jedes Signal unverändert weiter: ideal verzerrungsfrei.

**Kommutativgesetz**

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s$$

Substitution $\tau'=t-\tau$, $\mathrm{d}\tau=-\mathrm{d}\tau'$; das Vertauschen der Grenzen hebt das Minuszeichen auf. Eingang und Impulsantwort dürfen die Rollen tauschen.

**Assoziativgesetz**

$$(f*s)*h=f*(s*h)$$

Zwei Systeme in Kette wirken wie ein System mit der Impulsantwort $h_1*h_2$; vorausgesetzt, das zweite belastet das erste nicht.

**Distributivgesetz**

$$f*(s+h)=f*s+f*h$$

Zwei parallel geschaltete Systeme, deren Ausgänge addiert werden, wirken wie ein System mit der Impulsantwort $h_1+h_2$.

**Faltung komplexer Signale**

$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]$$

Folgt aus der Linearität der Faltung.
::::

::::lernkarten
:::karte begriff Faltungsprodukt
Was bezeichnet das Faltungsprodukt $s(t)*h(t)$, und wie lautet damit die Zerlegung eines Signals in Stöße?
---
Die Kurzschreibweise $g(t)=s(t)*h(t)$ für das Faltungsintegral $\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$. Die Zerlegung in Stöße lautet damit $s(t)=s(t)*\delta(t)$.
--- falsch
Das gewöhnliche Produkt $s(t)\,h(t)$ zweier Signale zur selben Zeit; den Stern schreibt man nur, um es von Produkten von Zahlen zu unterscheiden. Die Zerlegung lautet $s(t)=s(t)*1$.
--- falsch
Die Kurzschreibweise $g(t)=s(t)*h(t)$ für $\int_{-\infty}^{\infty}s(\tau)\,h(\tau)\,\mathrm{d}\tau$, also für die Fläche des Produkts der beiden Signale. Die Zerlegung lautet $s(t)=s(t)*\varepsilon(t)$.
--- falsch
Das Produkt $s(t)\,h^*(t)$ mit dem konjugiert komplexen $h$; für reelle Signale ist es das gewöhnliche Produkt. Die Zerlegung in Stöße lautet damit $s(t)=s(t)*s(t)$.
:::
:::karte begriff ideal verzerrungsfrei
Wann heißt ein System ideal verzerrungsfrei, und welche Rechenregel der Faltung steckt dahinter?
---
Wenn seine Impulsantwort $h(t)=\delta(t)$ ist: Es gibt jedes Signal unverändert weiter. Dahinter steckt das Einselement der Faltung, $s*\delta=s$; der Dirac-Impuls spielt die Rolle der Eins.
--- falsch
Wenn seine Impulsantwort $h(t)=\varepsilon(t)$ ist: Ein Sprung bleibt ein Sprung, also wird jedes Signal unverändert weitergegeben. Der Sprung spielt bei der Faltung die Rolle der Eins.
--- falsch
Wenn seine Impulsantwort für alle $t$ gleich 1 ist: Dann ist $s*h=s$, weil die Faltung mit der Konstanten 1 wie die Multiplikation mit 1 wirkt und nichts verändert.
--- falsch
Wenn es linear ist: Jedes lineare System gibt die Form eines Signals unverändert weiter und ändert höchstens die Amplitude. Das folgt unmittelbar aus dem Überlagerungssatz.
:::
:::karte formel Kommutativgesetz
Was besagt das Kommutativgesetz der Faltung für Eingang und Impulsantwort eines Systems?
---
$s*h=h*s$: Eingang und Impulsantwort dürfen die Rollen tauschen. Das System mit der Impulsantwort $s$ antwortet auf den Eingang $h$ genauso wie das System $h$ auf den Eingang $s$.
--- falsch
$s*h=-h*s$: Beim Vertauschen kehrt sich das Vorzeichen um, weil die Substitution $\tau'=t-\tau$ das Differential $\mathrm{d}\tau=-\mathrm{d}\tau'$ liefert. Eingang und Impulsantwort sind daher nicht gleichwertig.
--- falsch
$s*h=h*s$ gilt nur für symmetrische Signale. Sonst kommt beim Vertauschen das zeitlich gespiegelte Ergebnis heraus, weil die Spiegelung beim Ausrechnen dann die andere Funktion trifft.
--- falsch
$s*h=h*s$ gilt nur für Signale, die vor $t=0$ null sind. Sonst ändern sich beim Vertauschen die Integrationsgrenzen, und es kommt ein anderes Ergebnis heraus.
:::
:::karte herleitung Kommutativgesetz durch Substitution
Wie zeigt man mit der Substitution $\tau'=t-\tau$, dass $s*h=h*s$ gilt?
---
Aus $\tau'=t-\tau$ folgt $\tau=t-\tau'$ und $\mathrm{d}\tau=-\mathrm{d}\tau'$, weil $t$ beim Integrieren fest ist.
---
Die Grenzen $\tau=\mp\infty$ werden zu $\tau'=\pm\infty$, weil die Substitution das Vorzeichen von $\tau$ umkehrt.
---
Das Vertauschen der Grenzen hebt das Minuszeichen aus $\mathrm{d}\tau=-\mathrm{d}\tau'$ auf, weil ein Integral beim Vertauschen der Grenzen sein Vorzeichen wechselt.
---
Es bleibt $\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s$, weil jetzt $h$ an der Integrationsvariablen und $s$ am gespiegelten, geschobenen Argument steht.
:::
:::karte formel Assoziativgesetz
Was bedeutet das Assoziativgesetz $(f*s)*h=f*(s*h)$ für zwei Systeme in Kette?
---
Zwei Systeme in Kette wirken wie ein System, dessen Impulsantwort die Faltung der beiden Impulsantworten ist, $h_1*h_2$.
--- falsch
Zwei Systeme in Kette wirken wie ein System mit der Impulsantwort $h_1+h_2$, weil sich die Wirkungen der beiden Systeme addieren.
--- falsch
Zwei Systeme in Kette wirken wie ein System mit der Impulsantwort $h_1\,h_2$, weil jedes System das Signal mit seiner Antwort multipliziert.
--- falsch
Zwei Systeme in Kette kann man nur nacheinander berechnen, erst das erste, dann das zweite; eine gemeinsame Impulsantwort gibt es nicht.
:::
:::karte formel Distributivgesetz
Was bedeutet das Distributivgesetz $f*(s+h)=f*s+f*h$ für zwei parallel geschaltete Systeme, deren Ausgänge addiert werden?
---
Sie wirken wie ein System mit der Summe der Impulsantworten, $h_1+h_2$, denn jedes bekommt denselben Eingang.
--- falsch
Sie wirken wie ein System mit der Impulsantwort $h_1*h_2$, weil das Signal beide Systeme durchläuft.
--- falsch
Sie wirken wie ein System mit der Impulsantwort $\frac12(h_1+h_2)$, weil sich der Eingang auf beide Zweige aufteilt.
--- falsch
Sie wirken wie ein System mit der Summe $h_1+h_2$, aber nur, wenn beide Impulsantworten gleich sind; sonst stören sie sich.
:::
:::karte formel Faltung komplexer Signale
Wie zerfällt die Faltung zweier komplexer Signale $s$ und $h$ in Real- und Imaginärteile?
---
$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]$. Das folgt aus der Linearität der Faltung: Man faltet jedes Paar von Teilen einzeln.
--- falsch
$s*h=\operatorname{Re} s*\operatorname{Re} h+\mathrm{j}\,\operatorname{Im} s*\operatorname{Im} h$: Realteile falten sich mit Realteilen, Imaginärteile mit Imaginärteilen, gemischte Glieder fallen weg.
--- falsch
$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h+\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h-\operatorname{Im} s*\operatorname{Re} h\bigr]$, weil die Faltung mit dem konjugiert Komplexen rechnet.
--- falsch
Gar nicht: Die Faltung ist nur für reelle Signale definiert. Bei komplexen Signalen faltet man stattdessen Betrag und Phase getrennt und setzt das Ergebnis danach wieder zusammen.
:::
:::karte zusammenhang Zwei RC-Glieder in Kette
Welche Impulsantwort hat eine Kette aus zwei RC-Gliedern mit $RC=1$ s, und was muss dafür gelten?
---
$h*h$ mit $h(t)=\mathrm{e}^{-t}\varepsilon(t)$, also $t\,\mathrm{e}^{-t}\varepsilon(t)$, mit dem Maximum $\mathrm{e}^{-1}=0{,}368$ bei $t=1$ s und der Fläche 1. Das zweite Glied darf das erste nicht belasten, sonst zieht es Strom aus dem ersten Kondensator.
--- falsch
$h(t)^2=\mathrm{e}^{-2t}\varepsilon(t)$, das Quadrat der Einzelantwort, weil jedes Glied das Signal mit seiner Impulsantwort multipliziert. Ob das zweite Glied das erste belastet, spielt keine Rolle, weil beide LTI-Systeme sind.
--- falsch
$2\,\mathrm{e}^{-t}\varepsilon(t)$, die Summe der beiden Einzelantworten, mit der Fläche 2. Das zweite Glied muss das erste dabei belasten, denn nur wenn Strom vom ersten ins zweite fließt, kommt das Signal überhaupt an.
--- falsch
$t\,\mathrm{e}^{-t}\varepsilon(t)$ mit dem Maximum bei $t=0$ und der Fläche 2. Ob das zweite Glied das erste belastet, spielt keine Rolle: Die Kette ist in jedem Fall ein LTI-System mit der Impulsantwort $h*h$.
:::
::::
