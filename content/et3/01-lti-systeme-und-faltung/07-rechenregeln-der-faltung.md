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
