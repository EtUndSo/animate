---
title: Stufe 2: Der ideale Tiefpass
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3250300
summary: Der ideale Tiefpass lässt alle Frequenzen bis f mathrm g unverändert durch und sperrt alle darüber.
tags: Signaldauer
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Der ideale Tiefpass lässt alle Frequenzen bis $f_\mathrm g$ unverändert durch und sperrt alle darüber. Diese Stufe zeigt, was dieses scharfe Abschneiden im Zeitbereich bedeutet.
:::

:::satz Satz 2.1 (Idealer Tiefpass)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**So liest man das:** Die Impulsantwort reicht in beide Richtungen ins Unendliche. Der ideale Tiefpass ist also *nicht kausal*: Er müsste auf einen Stoß schon antworten, bevor er kommt. Er ist ein mathematisches Grenzobjekt, das man nur annähern kann (Stufen [4](kausale-naherung.html#stufe-4), [6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6)).

**Dauer und Bandbreite.** Als __Signaldauer__ $t_m$ einer Impulsantwort nimmt man die Breite eines Rechtecks mit derselben Höhe $h_{\max}$ und derselben Fläche:

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

Beim idealen Tiefpass ist $H(0)=1$ und $h_{\max}=2f_\mathrm g$, also $t_m=\frac{1}{2f_\mathrm g}$ und $f_\mathrm g\cdot t_m=\frac12$. Allgemein gilt für Tiefpässe $f_\mathrm g\cdot t_m=\text{konst.}$: Doppelte Bandbreite heißt halbe Antwortdauer. Das ist der Ähnlichkeitssatz aus [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).

**Überschwingen.** Das Verhältnis des betragsgrößten Nebenmaximums $a_1$ zum Hauptmaximum $a_0$ ist bei der si-Funktion

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21{,}7\,\%,$$

unabhängig von $f_\mathrm g$ (das erste Nebenminimum von $\operatorname{si}(\pi u)$ liegt bei $u=1{,}43$ mit $-0{,}217$). Eine Änderung von $f_\mathrm g$ staucht die Kurve nur, sie ändert nicht ihre Form.

:::aufgabe Aufgabe 2 ★ Idealer Tiefpass für Sprache
<span class="anker" id="aufg-2"></span>

Ein idealer Tiefpass mit $f_\mathrm g=4$ kHz. Wie groß sind die Signaldauer der Impulsantwort und das Überschwingen? Was ändert sich bei $f_\mathrm g=8$ kHz?

:::loesung
$t_m=\frac{1}{2f_\mathrm g}=125$ µ s, Überschwingen 21,7 %. Bei 8 kHz halbiert sich die Signaldauer auf 62,5 µ s. Das Überschwingen bleibt 21,7 %, weil die Impulsantwort nur gestaucht wird.
:::
:::

::::formelsammlung
**Idealer Tiefpass**

$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$$

Alle Frequenzen bis $f_\mathrm g$ unverändert durch, alle darüber gesperrt. Die Impulsantwort reicht in beide Richtungen ins Unendliche: Der ideale Tiefpass ist nicht kausal.

**Signaldauer**

$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}$$

Breite eines Rechtecks mit derselben Höhe $h_{\max}$ und derselben Fläche wie die Impulsantwort.

**Dauer und Bandbreite des idealen Tiefpasses**

$$t_m=\frac{1}{2f_\mathrm g},\qquad f_\mathrm g\cdot t_m=\frac12$$

Mit $H(0)=1$ und $h_{\max}=2f_\mathrm g$. Allgemein gilt für Tiefpässe $f_\mathrm g\cdot t_m=\text{konst.}$: doppelte Bandbreite, halbe Antwortdauer (Ähnlichkeitssatz).

**Überschwingen der Impulsantwort**

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21{,}7\,\%$$

Betragsgrößtes Nebenmaximum $a_1$ zum Hauptmaximum $a_0$ der si-Funktion; unabhängig von $f_\mathrm g$, weil eine andere Grenzfrequenz die Kurve nur staucht.
::::

::::lernkarten
:::karte formel Frequenzgang und Impulsantwort des idealen Tiefpasses
Wie lauten Frequenzgang und Impulsantwort des idealen Tiefpasses mit der Grenzfrequenz $f_\mathrm g$?
---
$H(f)=\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$ und $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$: Alle Frequenzen bis $f_\mathrm g$ kommen unverändert durch, alle darüber gar nicht; die Impulsantwort ist eine si-Funktion.
--- falsch
$H(f)=\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$ und $h(t)=\operatorname{rect}\bigl(\frac{t}{2f_\mathrm g}\bigr)$: Ein Rechteck im Spektrum gehört zu einem Rechteck in der Zeit, deshalb ist die Impulsantwort ein kurzer Rechteckimpuls.
--- falsch
$H(f)=\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$ und $h(t)=2f_\mathrm g\,\mathrm{e}^{-2\pi f_\mathrm gt}\varepsilon(t)$: Die Impulsantwort klingt wie beim RC-Glied exponentiell ab und beginnt erst bei $t=0$.
--- falsch
$H(f)=\operatorname{rect}\bigl(\frac{f}{f_\mathrm g}\bigr)$ und $h(t)=f_\mathrm g\operatorname{si}(\pi f_\mathrm gt)$: Das Rechteck reicht von $-f_\mathrm g$ bis $f_\mathrm g$, und die Impulsantwort ist eine si-Funktion mit der Höhe $f_\mathrm g$.
:::
:::karte zusammenhang Idealer Tiefpass nicht kausal
Warum lässt sich der ideale Tiefpass nicht exakt bauen, sondern nur annähern?
---
Seine Impulsantwort $2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$ reicht in beide Richtungen ins Unendliche. Er ist also nicht kausal: Er müsste auf einen Stoß schon antworten, bevor dieser kommt.
--- falsch
Seine Impulsantwort wächst mit der Zeit immer weiter an, er ist also instabil: Jeder kurze Stoß am Eingang würde am Ausgang eine unbegrenzt wachsende Schwingung auslösen.
--- falsch
Seine Bauteile müssten unendlich große Werte haben: Für die senkrechte Kante bräuchte man eine unendliche Kapazität, die Impulsantwort beginnt aber wie bei jedem System erst bei $t=0$.
--- falsch
Seine Impulsantwort ist nur für eine sehr kurze Zeit von null verschieden; einen so kurzen Impuls können reale Bauteile nicht erzeugen, deshalb bleibt das Filter ein Grenzobjekt.
:::
:::karte begriff Signaldauer
Wie ist die Signaldauer $t_m$ einer Impulsantwort definiert, mit der man Dauer und Bandbreite eines Tiefpasses vergleicht?
---
Die Signaldauer ist die Breite eines Rechtecks mit derselben Höhe $h_{\max}$ und derselben Fläche wie die Impulsantwort: $t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}$.
--- falsch
Die Signaldauer ist der Abstand der beiden ersten Nullstellen der Impulsantwort links und rechts des Maximums. Sie misst also die volle Breite der Hauptkeule und ist beim idealen Tiefpass $\frac{1}{f_\mathrm g}$.
--- falsch
Die Signaldauer ist die gesamte Zeit, in der die Impulsantwort von null verschieden ist. Beim idealen Tiefpass ist sie deshalb unendlich groß, weil die si-Funktion nie endgültig verschwindet.
--- falsch
Die Signaldauer ist die Breite eines Rechtecks mit derselben Höhe $h_{\max}$ und derselben Energie wie die Impulsantwort: $t_m=\frac{1}{h_{\max}^2}\int_{-\infty}^{\infty}h^2(t)\,\mathrm{d} t$.
:::
:::karte formel Dauer und Bandbreite
Welches Produkt aus Grenzfrequenz und Signaldauer hat der ideale Tiefpass, und was sagt es allgemein über Tiefpässe aus?
---
Mit $H(0)=1$ und $h_{\max}=2f_\mathrm g$ ist $t_m=\frac{1}{2f_\mathrm g}$, also $f_\mathrm g\cdot t_m=\frac12$. Allgemein ist $f_\mathrm g\cdot t_m$ konstant: Doppelte Bandbreite heißt halbe Antwortdauer (Ähnlichkeitssatz).
--- falsch
Mit $H(0)=1$ und $h_{\max}=2f_\mathrm g$ ist $t_m=2f_\mathrm g$, Dauer und Bandbreite wachsen also gemeinsam: Doppelte Bandbreite heißt doppelte Antwortdauer, weil mehr Frequenzen beteiligt sind.
--- falsch
Das Produkt $f_\mathrm g\cdot t_m$ ist beim idealen Tiefpass 1 und bei allen anderen Tiefpässen kleiner; der ideale Tiefpass hat also für jede Bandbreite die längste mögliche Antwortdauer.
--- falsch
Es gibt kein festes Produkt: Die Signaldauer hängt nur von der Form des Durchlassbereichs ab, nicht von seiner Breite, deshalb ändert eine größere Grenzfrequenz die Antwortdauer nicht.
:::
:::karte formel Überschwingen der Impulsantwort
Wie groß ist das Überschwingen der Impulsantwort des idealen Tiefpasses, und wie hängt es von $f_\mathrm g$ ab?
---
Das Verhältnis des betragsgrößten Nebenmaximums zum Hauptmaximum ist $\ddot u=\bigl|\frac{a_1}{a_0}\bigr|=21{,}7\,\%$, unabhängig von $f_\mathrm g$. Eine andere Grenzfrequenz staucht die Kurve nur, ihre Form bleibt.
--- falsch
Bei $f_\mathrm g=1$ Hz sind es 21,7 % des Hauptmaximums; bei doppelter Grenzfrequenz halbiert sich das Überschwingen, weil die Impulsantwort dann doppelt so schnell abklingt.
--- falsch
Das Überschwingen ist null: Die si-Funktion hat außer dem Hauptmaximum nur Nullstellen und keine weiteren Maxima oder Minima, weil sie stets zwischen null und eins bleibt.
--- falsch
Das Verhältnis des betragsgrößten Nebenmaximums zum Hauptmaximum ist $\ddot u=\bigl|\frac{a_1}{a_0}\bigr|=21{,}7\,\%$ bei $f_\mathrm g=1$ Hz; es wächst mit der Grenzfrequenz, weil die Nebenmaxima dichter liegen.
:::
:::karte zusammenhang Grenzfrequenz verdoppeln
Was ändert sich an der Impulsantwort des idealen Tiefpasses, wenn man die Grenzfrequenz verdoppelt?
---
Die Impulsantwort wird zeitlich auf die Hälfte gestaucht und doppelt so hoch, die Signaldauer halbiert sich. Ihre Form bleibt gleich, deshalb bleibt auch das Überschwingen bei 21,7 %.
--- falsch
Die Impulsantwort wird doppelt so breit und halb so hoch, weil mehr Frequenzen durchkommen und sich länger überlagern; das Überschwingen halbiert sich dabei auf etwa 11 %.
--- falsch
Die Impulsantwort wird halb so breit, und ihre Nebenmaxima klingen schneller ab; das Überschwingen sinkt deshalb deutlich unter 21,7 %, weil die Kante nun weiter außen liegt.
--- falsch
Nichts: Die Impulsantwort hängt nur von der Form des Frequenzgangs ab, nicht von seiner Breite, deshalb bleiben Breite, Höhe und Überschwingen der si-Funktion gleich.
:::
:::karte herleitung Signaldauer des idealen Tiefpasses
Wie folgt aus der Definition $t_m=\frac{H(0)}{h_{\max}}$, dass beim idealen Tiefpass $f_\mathrm g\cdot t_m=\frac12$ gilt?
---
Die Fläche der Impulsantwort ist gleich $H(0)$, weil der Frequenzgang bei $f=0$ das Integral über $h(t)$ ist; deshalb darf man das Integral in der Definition durch $H(0)$ ersetzen.
---
Beim idealen Tiefpass ist $H(0)=1$, weil das Rechteck $\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$ bei $f=0$ den Wert 1 hat.
---
Das Maximum der Impulsantwort ist $h_{\max}=2f_\mathrm g$, weil die si-Funktion bei $t=0$ ihren größten Wert 1 annimmt.
---
Damit ist $t_m=\frac{1}{2f_\mathrm g}$ und $f_\mathrm g\cdot t_m=\frac12$, weil man nur die beiden Werte in die Definition einsetzt.
:::
::::
