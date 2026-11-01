---
title: Tiefpass- und Bandpasssysteme
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250100
summary: Verzerrungsfreie Übertragung, idealer Tiefpass, komplexe Hüllkurve und Gruppenlaufzeit
tags: Phasenlaufzeit, Gruppenlaufzeit, Signaldauer, Integralsinus, Einschwingzeit, Echo, Cosine-Rolloff-Filter, äquivalente Tiefpass
lang: de
---

## Worum es geht

Fast jede Übertragung soll ein Signal möglichst unverändert ankommen lassen, aber nur in einem bestimmten Frequenzbereich: Ein Tiefpass lässt die tiefen Frequenzen durch, ein Bandpass ein Band um eine Trägerfrequenz. Dieser Artikel fragt: *Was heißt „unverändert“ genau, was kostet ein scharf begrenztes Band, und wie rechnet man mit Signalen, die auf einem hochfrequenten Träger sitzen?*

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Unverzerrt heißt: nur verstärkt und verzögert. Dazu braucht man einen konstanten Betrag und eine Phase, die linear mit der Frequenz fällt.

</li>

<li>

Ein scharf begrenzter (idealer) Tiefpass ist nicht kausal, schwingt bei Sprüngen um etwa 9 % über und braucht eine Einschwingzeit von $1/(2f_\mathrm g)$. Weichere Flanken verringern das Überschwingen auf Kosten der Schärfe.

</li>

<li>

Ein Bandpasssignal ist ein Tiefpasssignal (die komplexe Hüllkurve) auf einem Träger. Man rechnet mit der Hüllkurve wie mit einem Tiefpasssignal: Sie wird um die Gruppenlaufzeit verzögert, der Träger um die Phasenlaufzeit.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.**

| Ergebnis | Woher es kommt |
|---|---|
| verzerrungsfreies System | jede Schwingung gleich verstärkt und um dieselbe Zeit verzögert (Stufe [1](#stufe-1)) |
| Phasen- und Gruppenlaufzeit | Verzögerung des Trägers bzw. der Hüllkurve (Stufen [1](#stufe-1), [11](#stufe-11)) |
| Signaldauer $\cdot$ Bandbreite $=$ konst. | Ähnlichkeitssatz (Stufe [2](#stufe-2)) |
| Überschwingen 21,7 % und 8,95 % | Nebenzipfel der si-Funktion, Gibbs (Stufen [2](#stufe-2), [3](#stufe-3)) |
| kausale Näherung, Fensterentwurf | Abschneiden der Impulsantwort = Faltung im Spektrum (Stufen [4](#stufe-4), [6](#stufe-6)) |
| Pulsformfilter | weiche Flanke im Spektrum, schnell abklingende Impulsantwort (Stufe [5](#stufe-5)) |
| äquivalenter Tiefpass, komplexe Hüllkurve | positive Frequenzen nach null verschieben (Stufen [7](#stufe-7), [8](#stufe-8)) |
| Quadraturschaltung, Bandpass-Abtastung | Bandpass im Tiefpassbereich rechnen (Stufe [10](#stufe-10)) |

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für diesen Artikel
<ul>

<li>

⁠**RC-Tiefpass** mit $RC=1$ s wie in den [Teilen 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) bis 3.

</li>

<li>

⁠**Idealer Tiefpass** mit $f_\mathrm g=1$ Hz (zum Vergleich auch 2 Hz).

</li>

<li>

⁠**Idealer Bandpass** mit der Mittenfrequenz $f_0=10$ Hz und der Bandbreite $\Delta f=2$ Hz.

</li>

<li>

⁠**Zeitdiskreter Tiefpass** mit $f_\mathrm g=0{,}2$ (bezogen auf die Abtastrate) und 21 Koeffizienten.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap5.py` nach. $\operatorname{si}(x)=\sin(x)/x$ wie in [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).
:::

## Stufe 1: Das verzerrungsfreie System

<span class="anker" id="stufe-1"></span>

:::zweck
Was genau soll eine „gute“ Übertragung leisten? Und mit welchen Kenngrößen misst man, wie weit ein System davon abweicht?
:::

**Die Idee.** Ein Signal ist unverzerrt angekommen, wenn es nur lauter oder leiser und später ist, seine Form aber gleich:

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

Im Spektrum heißt das: Jede Schwingung wird mit demselben Faktor $h_0$ multipliziert, und jede wird um dieselbe Zeit $t_0$ verschoben. Eine Zeitverschiebung $t_0$ ist bei der Frequenz $f$ der Winkel $2\pi ft_0$. Deshalb muss die Phase $\varphi(f)=-2\pi t_0f$ eine Gerade durch den Ursprung sein.

:::definition Definition 1.1 (Kenngrößen eines LTI-Systems)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{Dämpfungsmaß:} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{bzw.}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{Dämpfungswinkel:} && b(f)=-\varphi(f),\\ &\text{Phasenlaufzeit:} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{Gruppenlaufzeit:} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**So liest man das:** Die __Phasenlaufzeit__ ist die Verzögerung einer einzelnen Schwingung der Frequenz $f$. Die __Gruppenlaufzeit__ ist die Verzögerung einer Gruppe benachbarter Frequenzen, also einer Hüllkurve (Stufe [11](#stufe-11)). Beim verzerrungsfreien System sind $a$, $t_\mathrm p$ und $t_\mathrm g$ konstant und $t_\mathrm p=t_\mathrm g=t_0$.

**Beispiel: das RC-Glied.** Mit $\varphi=-\arctan(2\pi f\,RC)$ und $RC=1$ s:

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

Für $f\to0$ sind beide $RC=1$ s. Bei $f=0{,}159$ Hz ($2\pi fRC=1$) ist $t_\mathrm p=0{,}785$ s, $t_\mathrm g=0{,}5$ s und $a=3{,}0$ dB. Das RC-Glied ist also nicht verzerrungsfrei: Es dämpft frequenzabhängig, und verschiedene Frequenzen kommen verschieden spät an.

:::ltspice Dämpfung und Laufzeiten des RC-Glieds ablesen
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg`, `cap` mit `1u`), Quellwert `AC 1`, Direktive `.ac dec 100 0.01 10`.

⁠**Ablesen:** Die linke Achse zeigt $20\lg|H|=-a$ in dB. Fahre mit der Maus auf die rechte Achse (Phase), bis der Zeiger zum Lineal wird, klicke und wähle „Group Delay“: Dann zeigt sie $t_\mathrm g(f)$ nach [(1.5)](#gl-1-5). Die Phasenlaufzeit rechnest du aus der Phase, $t_\mathrm p=-\varphi/(2\pi f)$ mit $\varphi$ im Bogenmaß.

⁠**Was du siehst:** Zu tiefen Frequenzen hin strebt $t_\mathrm g$ gegen 1 s. Bei 0,159 Hz liest du $a=3{,}0$ dB, $\varphi=-45^\circ$ und $t_\mathrm g=0{,}5$ s ab, daraus $t_\mathrm p=0{,}785$ s. Vergleiche die Werte bei $2\pi fRC=10$ mit deinem Ergebnis aus Aufgabe [1](#aufg-1)(b).
:::

:::aufgabe Aufgabe 1 ★ Laufzeiten des RC-Glieds
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Leite $t_\mathrm g$ des RC-Glieds aus [(1.5)](#gl-1-5) her.

</li>

<li>

Berechne $t_\mathrm p$, $t_\mathrm g$ und $a$ bei $2\pi fRC=10$. In welchem Frequenzbereich ist das RC-Glied näherungsweise verzerrungsfrei?

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$, $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$, also $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$.

(b) Bei $2\pi fRC=10$: $t_\mathrm p=\frac{\arctan10}{10}RC=0{,}147$ s, $t_\mathrm g=\frac{RC}{101}=0{,}0099$ s, $a=20{,}0$ dB. Näherungsweise verzerrungsfrei ist das RC-Glied nur für $2\pi fRC\ll1$, also weit unter 0,16 Hz: Dort ist $|H|\approx1$ und $t_\mathrm p\approx t_\mathrm g\approx RC$.
:::
:::

## Stufe 2: Der ideale Tiefpass

<span class="anker" id="stufe-2"></span>

:::zweck
Der ideale Tiefpass lässt alle Frequenzen bis $f_\mathrm g$ unverändert durch und sperrt alle darüber. Diese Stufe zeigt, was dieses scharfe Abschneiden im Zeitbereich bedeutet.
:::

:::satz Satz 2.1 (Idealer Tiefpass)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**So liest man das:** Die Impulsantwort reicht in beide Richtungen ins Unendliche. Der ideale Tiefpass ist also *nicht kausal*: Er müsste auf einen Stoß schon antworten, bevor er kommt. Er ist ein mathematisches Grenzobjekt, das man nur annähern kann (Stufen [4](#stufe-4), [6](#stufe-6)).

**Dauer und Bandbreite.** Als __Signaldauer__ $t_m$ einer Impulsantwort nimmt man die Breite eines Rechtecks mit derselben Höhe $h_{\max}$ und derselben Fläche:

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

Beim idealen Tiefpass ist $H(0)=1$ und $h_{\max}=2f_\mathrm g$, also $t_m=\frac{1}{2f_\mathrm g}$ und $f_\mathrm g\cdot t_m=\frac12$. Allgemein gilt für Tiefpässe $f_\mathrm g\cdot t_m=\text{konst.}$: Doppelte Bandbreite heißt halbe Antwortdauer. Das ist der Ähnlichkeitssatz aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).

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

## Stufe 3: Sprungantwort und Einschwingzeit

<span class="anker" id="stufe-3"></span>

:::zweck
Wie reagiert der ideale Tiefpass auf einen Sprung? Wie schnell steigt er, und wie weit schießt er über?
:::

Die Sprungantwort ist das laufende Integral der Impulsantwort ([Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Mit dem __Integralsinus__

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2 \tag{3.1}$$

ergibt sich

<span class="anker" id="gl-3-2"></span>
$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt). \tag{3.2}$$

:::herleitung Sprungantwort
Das Integral bis $t$ teilt man bei 0. Der Teil von $-\infty$ bis 0 ist die halbe Fläche von $h$, also $\frac12H(0)=\frac12$, weil $h$ gerade ist. Für den Rest substituiert man $\xi=2\pi f_\mathrm g\tau$, $\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$: $\int_0^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\mathrm{d}\tau=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$. Den Wert $\operatorname{Si}(\infty)=\frac\pi2$ liefert der Flächensatz: $\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$, also $\int_0^\infty\operatorname{si}(\xi)\mathrm{d}\xi=\frac\pi2$.
:::

⁠**So liest man das:** Bei $t=0$ ist die Antwort genau $\frac12$, sie beginnt schon vorher (nicht kausal) und strebt gegen 1. Die __Einschwingzeit__ $t_e$ definiert man als Anstiegszeit einer Rampe mit der größten Steigung der Sprungantwort. Die größte Steigung ist $h(0)=2f_\mathrm g$, also

<span class="anker" id="gl-3-3"></span>
$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}. \tag{3.3}$$

Die Sprungantwort schießt um $8{,}95\,\%$ über (bei $t=\frac{1}{2f_\mathrm g}$). Das ist das Gibbs-Phänomen aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Ein größeres $f_\mathrm g$ verkürzt die Einschwingzeit, das Überschwingen bleibt (Abb. [1](#abb-1)).

:::abbildung et3/k5sprung
Sprungantwort des idealen Tiefpasses für $f_\mathrm g=1$ Hz und 2 Hz. Gestrichelt die Rampe mit der größten Steigung: Ihre Anstiegszeit ist $t_e=1/(2f_\mathrm g)=0{,}5$ s. Beide Kurven schießen gleich weit über, auf 1,0895.
:::

:::frage Ein Tiefpass mit mehr Bandbreite ist doch „besser“. Warum wird das Überschwingen dann nicht kleiner?
Weil es von der *Form* des Frequenzgangs kommt, nicht von seiner Breite. Das Überschwingen entsteht an der senkrechten Kante bei $f_\mathrm g$: Alle Frequenzen bis dorthin kommen voll an, alle darüber gar nicht. Verschiebt man die Kante, bleibt sie senkrecht, und die Sprungantwort wird nur zeitlich gestaucht. Kleiner wird das Überschwingen erst, wenn die Kante weich wird (Stufe [5](#stufe-5)).
:::

:::aufgabe Aufgabe 3 ★★ Integralsinus
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Zeige $h_\varepsilon(0)=\frac12$ und $h_\varepsilon(\infty)=1$ mit [(3.1)](#gl-3-1).

</li>

<li>

Wo liegt das Maximum der Sprungantwort? Tipp: Die Ableitung der Sprungantwort ist die Impulsantwort.

</li>

</ol>

:::loesung
(a) $h_\varepsilon(0)=\frac12+\frac1\pi\operatorname{Si}(0)=\frac12$, $h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$.

(b) Die Steigung der Sprungantwort ist $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$. Sie wird zum ersten Mal bei $2\pi f_\mathrm gt=\pi$ null und wechselt dort von positiv zu negativ. Das Maximum liegt also bei $t=\frac{1}{2f_\mathrm g}$ und ist $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1{,}852}{\pi}=1{,}0895$.
:::
:::

## Stufe 4: Kausale Näherung

<span class="anker" id="stufe-4"></span>

:::zweck
Wie baut man etwas, das dem idealen Tiefpass möglichst nahekommt? Man verzögert die Impulsantwort und schneidet den Rest ab.
:::

**Die Idee.** Man verschiebt $h(t)$ um $t_0$ nach rechts, bis der Teil bei $t<0$ vernachlässigbar ist, und schneidet ihn ab. Die Hüllkurve der si-Funktion fällt wie $1/(2\pi f_\mathrm g|t|)$. Soll sie vor $t=0$ unter 1 % des Maximums liegen, braucht man $t_0\approx16/f_\mathrm g$. Mit einem symmetrischen Fenster der Breite $2t_0$:

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**So liest man das:** Das Abschneiden ist eine Multiplikation mit einem Fenster, im Spektrum also eine Faltung mit dessen si-Spektrum. Die scharfe Kante wird verschmiert und bekommt Wellen. Der Faktor $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ ist die Verzögerung: Das kausale Filter hat eine lineare Phase, es verzögert alle Frequenzen gleich (Abb. [2](#abb-2)). Je größer $t_0$, desto schmaler der Übergang, aber desto später die Antwort.

:::abbildung et3/k5kausal
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

## Stufe 5: Echomethode und Pulsformfilter

<span class="anker" id="stufe-5"></span>

:::zweck
Wie entwirft man einen Tiefpass mit weniger Überschwingen? Man setzt die Impulsantwort aus verschobenen si-Funktionen zusammen und wählt deren Gewichte.
:::

**Echomethode.** Jede Impulsantwort eines Tiefpasses bis $f_\mathrm g=\frac{1}{2T}$ ist nach dem Abtasttheorem eine si-Reihe:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f. \tag{5.2}$$

Jeder Abtastwert $h(nT)$ ist ein __Echo__: eine um $nT$ verschobene si-Funktion. Im Spektrum wird daraus eine Fourier-Reihe in $f$. Ist $h$ reell und gerade, ist $H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$.

**Pulsformfilter.** Zur Hauptkomponente $\operatorname{si}(\pi t/T)$ kommen zwei Echos mit der Amplitude $a$ im Abstand $\pm T$. Bei $a=\frac12$ heben sich die Nebenschwingungen weitgehend auf, und das Spektrum bekommt eine kosinusförmige, weiche Flanke:

<span class="anker" id="gl-5-3"></span>
$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]. \tag{5.3}$$

Das ist das __Cosine-Rolloff-Filter__. Sein Überschwingen ist 2,7 % statt 21,7 %, dafür ist die Hauptkeule doppelt so breit (erste Nullstelle bei $2T$ statt $T$). Abbildung [3](#abb-3) zeigt beide Impulsantworten auf gleiche Fläche normiert.

:::abbildung et3/k5pulsform
Impulsantworten des idealen Tiefpasses und des Pulsformfilters (beide mit der Fläche $T$). Das Pulsformfilter klingt viel schneller ab: Sein größtes Nebenmaximum ist 2,7 % des Hauptmaximums statt 21,7 %.
:::

**Transversalfilter.** Eine Summe verzögerter, gewichteter Kopien baut man mit einer Kette von Verzögerungsgliedern, deren Abgriffe gewichtet und addiert werden. Damit kein Glied in die Zukunft greifen muss, verzögert man alles gemeinsam. Das ist dieselbe Struktur wie ein FIR-Filter ([Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

:::aufgabe Aufgabe 5 ★★ Das Cosine-Rolloff-Filter
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Leite $H(f)$ in [(5.3)](#gl-5-3) aus [(5.1)](#gl-5-1) her.

</li>

<li>

Welchen Wert hat $H$ bei $f=0$ und bei $f=f_\mathrm g=\frac{1}{2T}$? Warum ist die Flanke dort glatt?

</li>

</ol>

:::loesung
(a) Bei $t=mT$ ist $\operatorname{si}(\pi(t\pm T)/T)$ nur für $m=\mp1$ gleich 1, sonst null. Also $h(0)=1$, $h(\pm T)=\frac12$, alle anderen $h(nT)=0$. Nach [(5.1)](#gl-5-1): $H=T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$.

(b) $H(0)=2T$, $H(\frac{1}{2T})=T(1+\cos\pi)=0$. Auch die Steigung $-2\pi T^2\sin(2\pi Tf)$ ist bei $f=\frac{1}{2T}$ null. Der Frequenzgang geht ohne Sprung und ohne Knick auf null. Je glatter das Spektrum, desto schneller klingt die Impulsantwort ab ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
:::
:::

## Stufe 6: Zeitdiskrete Tiefpässe, Entwurf mit Fenstern

<span class="anker" id="stufe-6"></span>

:::zweck
Wie entwirft man einen digitalen Tiefpass? Genau wie den kausalen analogen: idealen Tiefpass nehmen, verzögern, mit einem Fenster abschneiden.
:::

Der ideale zeitdiskrete Tiefpass hat den periodisch wiederholten Rechteck-Frequenzgang und die Impulsantwort

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

im Rechenmodell ($f_\mathrm g=0{,}2$) also $h(0)=0{,}4$, $h(\pm1)=0{,}303$, $h(\pm2)=0{,}094$, $h(\pm3)=-0{,}062$. Auch er ist nicht kausal. Man multipliziert ihn mit einem Fenster $w(n)$ von $2N+1$ Werten, verschiebt um $N$ und erhält ein FIR-Filter mit linearer Phase. Das Fenster bestimmt das Ergebnis (Abb. [4](#abb-4)):

<ul>

<li>

⁠**Rechteckfenster:** schärfster Übergang, aber hohe Nebenzipfel. Im Rechenmodell ($N=10$) erreicht der Sperrbereich ab $f=0{,}3$ noch $-26{,}6$ dB, der Durchlass schwankt um etwa $\pm0{,}5$ dB.

</li>

<li>

⁠**Hann-Fenster:** weicherer Übergang, aber viel tiefere Sperrung: ab $f=0{,}3$ höchstens $-45{,}9$ dB, Durchlass auf $0{,}05$ dB glatt.

</li>

</ul>

Der Grund ist derselbe wie bei der Kurzzeit-Fourier-Transformation in [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Das Spektrum des Fensters wird mit dem Ideal gefaltet, und die harten Kanten des Rechtecks erzeugen langsam abklingende Nebenzipfel.

:::abbildung et3/k5fenster
Betragsfrequenzgang zweier FIR-Tiefpässe mit $f_\mathrm g=0{,}2$ und 21 Koeffizienten. Rechteckfenster: steile Flanke, ab $f=0{,}3$ Sperrung nur bis $-26{,}6$ dB. Hann-Fenster: flachere Flanke, ab $f=0{,}3$ höchstens $-45{,}9$ dB.
:::

:::aufgabe Aufgabe 6 ★ Halbbandfilter
<span class="anker" id="aufg-6"></span>

Berechne die Koeffizienten $h(0)$ bis $h(3)$ des idealen zeitdiskreten Tiefpasses mit $f_\mathrm g=0{,}25$. Was fällt auf, und warum spart das bei einem FIR-Filter Rechenarbeit?

:::loesung
$h(n)=0{,}5\operatorname{si}(\pi n/2)$: $h(0)=0{,}5$, $h(\pm1)=\frac1\pi=0{,}318$, $h(\pm2)=0$, $h(\pm3)=-\frac{1}{3\pi}=-0{,}106$. Alle geraden Koeffizienten außer $h(0)$ sind null, weil $\sin(\pi n/2)=0$ für gerade $n$. Im FIR-Filter entfallen diese Multiplikationen, fast die Hälfte.
:::
:::

## Stufe 7: Der ideale Bandpass und sein äquivalenter Tiefpass

<span class="anker" id="stufe-7"></span>

:::zweck
Ein Bandpass lässt ein Band um die Mittenfrequenz $f_0$ durch. Diese Stufe zeigt, dass man ihn vollständig durch einen Tiefpass und die Frequenz $f_0$ beschreiben kann.
:::

**Idealer Bandpass.** Zwei Rechtecke der Breite $\Delta f$ bei $\pm f_0$ ($f_0>\Delta f/2$):

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

Die Impulsantwort ist eine Schwingung mit $f_0$, deren Hüllkurve die Impulsantwort eines Tiefpasses der Bandbreite $\Delta f/2$ ist. Die Modulationsregel aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html) erklärt es: Ein Tiefpass, dessen Spektrum nach $\pm f_0$ verschoben wird.

**Äquivalenter Tiefpass.** Bei reeller Impulsantwort ist $H(-f)=H^*(f)$, die negative Hälfte enthält nichts Neues. Man behält nur die positiven Frequenzen, verdoppelt sie und schiebt sie um eine Trägerfrequenz $f_0$ nach links. Das Ergebnis ist der __äquivalente Tiefpass__ $H_T(f)$:

<span class="anker" id="gl-7-2"></span>
$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad H_T(f)=0\ \text{für}\ f\le-f_0. \tag{7.2}$$

$H_T$ muss nicht symmetrisch um $f=0$ sein, seine Impulsantwort $h_T(t)$ kann also komplex sein. Gibt es ein $f_0$, für das $H_T(-f)=H_T^*(f)$ gilt (und $h_T$ damit reell ist), heißt der Bandpass __symmetrisch__. Beim idealen Bandpass mit $f_0$ in der Mitte ist $H_T(f)=2\operatorname{rect}(f/\Delta f)$ und $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$, reell und gerade. Das ist ein Sonderfall: Auch symmetrische Bandpässe haben in der Regel einen Imaginärteil im Spektrum.

:::aufgabe Aufgabe 7 ★★ Äquivalenter Tiefpass mit anderem Bezug
<span class="anker" id="aufg-7"></span>

Idealer Bandpass von 9 bis 11 Hz.

<ol class="al">

<li>

Bestimme $H_T$ und $h_T$ für $f_0=10$ Hz.

</li>

<li>

Bestimme $H_T$ und $h_T$ für $f_0=9$ Hz. Warum ist $h_T$ jetzt komplex? Beschreiben beide denselben Bandpass?

</li>

</ol>

:::loesung
(a) $f_0=10$ Hz: Das Band liegt nach dem Verschieben symmetrisch von $-1$ bis $1$ Hz. $H_T=2\operatorname{rect}(f/2)$, $h_T=4\operatorname{si}(2\pi t)$, reell.

(b) $f_0=9$ Hz: Das Band liegt von 0 bis 2 Hz. $H_T=2\operatorname{rect}\bigl(\frac{f-1}{2}\bigr)$, $h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$. Komplex, weil $H_T$ nicht symmetrisch um $f=0$ ist. Beide beschreiben denselben Bandpass: $\operatorname{Re}\{4\operatorname{si}(2\pi t)\mathrm{e}^{\mathrm{j}2\pi t}\mathrm{e}^{\mathrm{j}2\pi9t}\}=4\operatorname{si}(2\pi t)\cos(2\pi\cdot10t)$, dasselbe wie in (a) und wie [(7.1)](#gl-7-1).
:::
:::

## Stufe 8: Komplexe Hüllkurve und Quadraturkomponenten

<span class="anker" id="stufe-8"></span>

:::zweck
Was für Systeme gilt, gilt auch für Signale: Ein Bandpasssignal ist ein Tiefpasssignal auf einem Träger. Diese Stufe zeigt die verschiedenen Arten, das hinzuschreiben.
:::

Die Rücktransformation von [(7.2)](#gl-7-2) ergibt mit der Modulationsregel $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$, also wegen $z+z^*=2\operatorname{Re} z$:

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ heißt __komplexe Hüllkurve__, $\mathrm{e}^{\mathrm{j}2\pi f_0t}$ __komplexer Träger__. Ihr halbes Produkt ist die analytische Komponente aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$, also $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

:::satz Satz 8.1 (Quadraturdarstellung)
<span class="anker" id="satz-8-1"></span>

Mit $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ und der Hilbert-Transformierten $\hat s=s*\frac{1}{\pi t}$:

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**So liest man das:** $s_{Tr}$ und $s_{Ti}$ heißen __Quadraturkomponenten__: Die eine moduliert den Kosinus, die andere den Sinus des Trägers. $|s_T|$ ist die __Einhüllende__, die man auf einem Oszilloskop als „Umriss“ des Signals sieht, und $\varphi_T$ die Phasenabweichung des Trägers. Ist die Hüllkurve reell (symmetrischer Fall), ist $s(t)=s_T(t)\cos(2\pi f_0t)$: ein amplitudenmodulierter Kosinus.

:::herleitung Quadraturkomponenten
[(8.2)](#gl-8-2): $\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$. Für [(8.3)](#gl-8-3): $2s_+=s+\mathrm{j}\hat s$ ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), also

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe Aufgabe 8 ★★ Komplexe Hüllkurven bestimmen
<span class="anker" id="aufg-8"></span>

Bestimme $s_T$, $s_{Tr}$, $s_{Ti}$ und $|s_T|$ bezüglich $f_0=10$ Hz für (a) $s(t)=\bigl[1+0{,}5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$, (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0{,}3)$, (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$. Prüfe (c) mit [(8.2)](#gl-8-2).

:::loesung
(a) $s_T=1+0{,}5\cos(2\pi t)$, reell: $s_{Tr}=s_T$, $s_{Ti}=0$, $|s_T|=1+0{,}5\cos(2\pi t)$ zwischen 0,5 und 1,5. Ein amplitudenmodulierter Kosinus.

(b) $s_T=\mathrm{e}^{\mathrm{j}0{,}3}$: $s_{Tr}=\cos0{,}3=0{,}955$, $s_{Ti}=\sin0{,}3=0{,}296$, $|s_T|=1$. Die Hüllkurve ist konstant, nur die Phase ist um 0,3 verschoben.

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$, also $s_T=-\mathrm{j}$: $s_{Tr}=0$, $s_{Ti}=-1$, $|s_T|=1$. Probe: $0\cdot\cos-(-1)\sin=\sin$.
:::
:::

## Stufe 9: Bandpasssignal durch Bandpasssystem

<span class="anker" id="stufe-9"></span>

:::zweck
Der Nutzen der Hüllkurven: Wie ein Bandpass auf ein Bandpasssignal wirkt, rechnet man vollständig im Tiefpassbereich.
:::

:::satz Satz 9.1 (Übertragung im äquivalenten Tiefpassbereich)
<span class="anker" id="satz-9-1"></span>

Erfüllen $S_T$ und $H_T$ beide [(7.2)](#gl-7-2) (nichts unterhalb von $-f_0$), dann gilt für die Hüllkurve des Ausgangs

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung Übertragung
$G=S\cdot H$ mit beiden Darstellungen [(7.2)](#gl-7-2) ausmultipliziert gibt vier Produkte. Die gemischten, etwa $S_T(f-f_0)H_T^*(-f-f_0)$, sind null: Der erste Faktor lebt bei positiven, der zweite bei negativen Frequenzen. Es bleibt $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$. Der Vergleich mit $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ gibt $G_T=\frac12S_TH_T$.
:::

⁠**So liest man das:** Der Faktor $\frac12$ gleicht aus, dass $S_T$ und $H_T$ beide verdoppelt wurden. Sonst ist es der gewohnte Faltungssatz, nur für die Hüllkurven. Der Träger muss gar nicht mitgerechnet werden.

**Beispiel: eingeschalteter Kosinus durch den idealen Bandpass.** $s(t)=\varepsilon(t)\cos(2\pi f_0t)$ mit $f_0=10$ Hz, Bandpass mit $\Delta f=2$ Hz um $f_0$. Die Hüllkurve des Eingangs ist $s_T\approx\varepsilon(t)$. (Näherung: Das Spektrum des Sprungs ist nicht auf $f>-f_0$ begrenzt, im Durchlassbereich $|f|\le\Delta f/2\ll f_0$ stimmt es aber.) Mit $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$:

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

Die Hüllkurve ist die Sprungantwort eines idealen Tiefpasses mit $f_\mathrm g=\Delta f/2$: Einschwingzeit $1/\Delta f=0{,}5$ s, Überschwingen 8,95 % (Abb. [5](#abb-5)). Ein schmaler Bandpass braucht lange, bis er „eingeschwungen“ ist.

:::abbildung et3/k5bandpass
Antwort des idealen Bandpasses ($f_0=10$ Hz, $\Delta f=2$ Hz) auf einen bei $t=0$ eingeschalteten Kosinus der Mittenfrequenz. Blau das Ausgangssignal, rot die Einhüllende $\pm g_T(t)$. Sie steigt in etwa 0,5 s an und schwingt auf 1,09 über.
:::

:::ltspice Eingeschalteter Träger durch einen Schwingkreis
Einen idealen Bandpass kann man nicht bauen, einen Reihenschwingkreis schon. **Zeichnen:** Quelle `voltage` am Netz `in`, dann in Reihe `ind` mit `{L}`, `cap` mit `{1/((2*pi*f0)**2*L)}` und `res` mit `{2*pi*df*L}` nach Masse. Der Ausgang `out` ist die Spannung am Widerstand. Mit `.param f0=10 df=2 L=1` ist die Mittenfrequenz 10 Hz und die Bandbreite zwischen den $-3$-dB-Punkten 2 Hz.

⁠**Kontrolle:** Quellwert `AC 1` und `.ac lin 2001 5 15` zeigen das Maximum 1 bei 10 Hz und die $-3$-dB-Punkte bei 9,05 Hz und 11,05 Hz.

⁠**Versuch:** Quelle `SINE(0 1 10 0 0 90)`, das ist $\varepsilon(t)\cos(2\pi f_0t)$, und `.tran 0 3 0 0.1m`. Die Hüllkurve steigt ohne Überschwingen an: Die Spitzen des Trägers erreichen 0,72 bei 0,2 s, 0,96 bei 0,5 s und praktisch 1 nach 1 s, fast genau wie $1-\mathrm{e}^{-t/0{,}16\,\mathrm s}$. Der ideale Bandpass schwingt dagegen auf 1,09 über (Abb. [5](#abb-5)). Der Grund ist derselbe wie beim Tiefpass in Stufe [3](#stufe-3): Die Flanken des Schwingkreises sind weich, die des idealen Bandpasses senkrecht.
:::

## Stufe 10: Quadraturschaltung und Bandpass-Abtastung

<span class="anker" id="stufe-10"></span>

:::zweck
Wie gewinnt man die Quadraturkomponenten technisch? Und wie viele Abtastwerte braucht ein Bandpasssignal?
:::

**Quadraturschaltung.** Multipliziert man ein Bandpasssignal mit $\cos(2\pi f_0t)$ und filtert mit einem Tiefpass, bleibt $\frac12s_{Tr}$. Mit $-\sin(2\pi f_0t)$ bleibt $\frac12s_{Ti}$. Der Grund ist trigonometrisch:

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{bei }2f_0,\text{ vom Tiefpass entfernt}},$$

und ebenso $-s\sin=\frac12s_{Ti}+(\text{Anteile bei }2f_0)$. Voraussetzung ist, dass das Band unterhalb von $2f_0$ endet. Im Tiefpassbereich filtert man dann mit vier Tiefpässen ($h_{Tr}$, $\pm h_{Ti}$) nach [(9.1)](#gl-9-1). Am Ausgang moduliert man nach [(8.2)](#gl-8-2) wieder auf den Träger, oder man bildet die Einhüllende $\sqrt{g_{Tr}^2+g_{Ti}^2}$ (Abb. [6](#abb-6)).

:::abbildung et3/k5quadratur
Quadraturdemodulator: Er gewinnt aus einem Bandpasssignal die beiden Quadraturkomponenten, also die komplexe Hüllkurve.
:::

**Abtasttheorem für Bandpasssignale.** Ein Bandpasssignal der Bandbreite $\Delta f$ hat, bezogen auf die Mittenfrequenz, Quadraturkomponenten, die Tiefpasssignale bis $\Delta f/2$ sind. Jede lässt sich mit $1/T=\Delta f$ abtasten:

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

Insgesamt braucht man $2\Delta f$ Werte je Sekunde, so viele wie für ein Tiefpasssignal der Grenzfrequenz $\Delta f$. Es kommt also auf die Bandbreite an, nicht auf die höchste Frequenz.

:::aufgabe Aufgabe 9 ★★ Ein Funksignal abtasten
<span class="anker" id="aufg-9"></span>

Ein Signal belegt das Band von 10,0 bis 10,2 MHz.

<ol class="al">

<li>

Welche Abtastrate bräuchte man nach dem gewöhnlichen Abtasttheorem?

</li>

<li>

Wie viele Abtastwerte je Sekunde genügen mit der Quadraturschaltung insgesamt, und mit welcher Rate wird jeder Zweig abgetastet?

</li>

</ol>

:::loesung
(a) Mindestens $2\cdot10{,}2=20{,}4$ MHz.

(b) $\Delta f=0{,}2$ MHz. Jeder Zweig wird mit 0,2 MHz abgetastet ($T=5$ µ s), zusammen 0,4 MHz, rund fünfzigmal weniger.
:::
:::

## Stufe 11: Phasen- und Gruppenlaufzeit beim Bandpass

<span class="anker" id="stufe-11"></span>

:::zweck
Warum gibt es zwei Laufzeiten? Weil Träger und Hüllkurve verschieden verzögert werden können.
:::

**Die Idee.** Ein Bandpass habe im Durchlassbereich den Betrag konstant und eine schwach gekrümmte Phase. Um $f_0$ nähert man sie durch ihre Tangente:

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$$

mit $t_\mathrm p=t_\mathrm p(f_0)$ und $t_\mathrm g=t_\mathrm g(f_0)$ aus [(1.4)](#gl-1-4) und [(1.5)](#gl-1-5). Im Tiefpassbereich ($f-f_0\to f$) ist das $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$: eine konstante Phase und eine Verzögerung.

:::satz Satz 11.1 (Laufzeiten im Bandpass)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**So liest man das:** Die Hüllkurve, die die Information trägt, wird um die *Gruppenlaufzeit* verzögert. Der Träger wird um die *Phasenlaufzeit* verzögert. Unverzerrt im strengen Sinn ist die Übertragung nur, wenn beide gleich sind. Das heißt, die Phasengerade geht durch den Ursprung (oder durch ein Vielfaches von $2\pi$ bei $f=0$). Für die Information genügt meist schon eine konstante Gruppenlaufzeit: Ist $t_\mathrm g$ nicht konstant, kommen verschiedene Frequenzanteile der Hüllkurve verschieden spät an, und Impulse zerfließen (__Laufzeitverzerrung__).

:::ltspice Hüllkurve und Träger kommen verschieden spät an
⁠**Zeichnen:** der Schwingkreis aus dem LTspice-Hinweis in Stufe [9](#stufe-9) ($f_0=10$ Hz, $\Delta f=2$ Hz). In der `.ac`-Analyse hat er bei 10 Hz die Phase $0^\circ$, also $t_\mathrm p(f_0)=0$. Schaltest du die Phasenachse auf „Group Delay“ um, zeigt sie bei 10 Hz $t_\mathrm g(f_0)=0{,}16$ s.

⁠**Versuch:** als Eingang eine Verhaltensquelle `bv`, ein Träger mit langsam schwankender Hüllkurve:

`V=(1+0.5*cos(2*pi*0.2*time))*cos(2*pi*10*time)`

Direktiven `.tran 0 20 0 0.2m` und `.options plotwinsize=0`.

⁠**Was du siehst:** Zeichne `V(in)` und `V(out)` übereinander und zoome auf 14,5 s bis 15,5 s. Das Maximum der Hüllkurve kommt am Ausgang etwa 0,16 s später an, die Nulldurchgänge des Trägers liegen aber an denselben Stellen wie am Eingang. Genau das sagt [(11.1)](#gl-11-1): Die Hüllkurve wird um $t_\mathrm g$ verzögert, der Träger um $t_\mathrm p$.
:::

:::aufgabe Aufgabe 10 ★★ Laufzeiten ablesen
<span class="anker" id="aufg-10"></span>

Ein Bandpass hat bei $f_0=1$ MHz die Phase $\varphi(f_0)=-\pi/2$ und die Steigung $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-2\pi\cdot2\,\mu\text{s}$.

<ol class="al">

<li>

Berechne $t_\mathrm p$ und $t_\mathrm g$.

</li>

<li>

Um wie viel ist die Hüllkurve eines Pulses am Ausgang verzögert? Liegt der Träger danach noch in derselben Lage relativ zur Hüllkurve?

</li>

</ol>

:::loesung
(a) $t_\mathrm p=-\frac{\varphi(f_0)}{2\pi f_0}=\frac{\pi/2}{2\pi\cdot10^6\,\mathrm{Hz}}=0{,}25$ µ s. $t_\mathrm g=2$ µ s.

(b) Die Hüllkurve kommt 2 µ s später an. Der Träger ist nur um 0,25 µ s verschoben. Gegenüber der Hüllkurve ist er also um $2\pi f_0(t_\mathrm g-t_\mathrm p)=3{,}5\pi$ verdreht, das ist modulo $2\pi$ gleich $1{,}5\pi$, also $-\pi/2$: eine Viertelperiode. Die Information in der Hüllkurve bleibt unverzerrt, solange $t_\mathrm g$ über das Band konstant ist.
:::
:::

## Stufe 12: Zeitdiskrete Bandpässe und Hochpässe

<span class="anker" id="stufe-12"></span>

:::zweck
Digitale Bandpässe und Hochpässe gewinnt man aus einem Tiefpass durch Modulation.
:::

Hat der zeitdiskrete Tiefpass eine reelle Impulsantwort, verschiebt die Multiplikation mit $2\cos(2\pi f_0n)$ seinen Durchlassbereich nach $\pm f_0$:

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

gültig, solange sich die verschobenen Bänder nicht überlappen: $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$. Wegen der Periodizität darf das Band bei $f_0$ weder das Band bei $-f_0$ noch dessen Kopie bei $1-f_0$ berühren. Allgemein, auch für komplexe Tiefpass-Impulsantworten, gilt wie in [(8.1)](#gl-8-1) $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$. Der Faktor 2 entspricht dem verdoppelten äquivalenten Tiefpass $H_T=2H_{\mathrm{TP}}$.

Ein __Hochpass__ ist ein Tiefpass, verschoben zur halben Abtastrate $f_0=\frac12$. Dort fallen das Band und sein Spiegelbild zusammen, deshalb verschiebt man nur einmal: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. Mit $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$:

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**Kurz gesagt:** Ein digitaler Hochpass entsteht aus einem Tiefpass, indem man jedes zweite Vorzeichen umdreht.

:::aufgabe Aufgabe 11 ★ Hochpass aus dem gleitenden Mittelwert
<span class="anker" id="aufg-11"></span>

Der gleitende Mittelwert $h_{\mathrm{TP}}=\frac13(1,1,1)$ ([Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) ist ein einfacher Tiefpass.

<ol class="al">

<li>

Bilde $h_{\mathrm{HP}}$ nach [(12.2)](#gl-12-2).

</li>

<li>

Berechne $H_{\mathrm{TP}}$ und $H_{\mathrm{HP}}$ bei $f=0$ und $f=\frac12$. Passt das zu einem Hochpass?

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$.

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$: $|H_{\mathrm{TP}}(0)|=1$, $|H_{\mathrm{TP}}(\frac12)|=\frac13$. Der Hochpass ist um $\frac12$ verschoben: $|H_{\mathrm{HP}}(0)|=\frac13$, $|H_{\mathrm{HP}}(\frac12)|=1$. Er lässt die schnellste Folge $(+1,-1,+1,\dots)$ voll durch und dämpft den Gleichanteil auf ein Drittel. Ein einfacher, nicht sehr steiler Hochpass.
:::
:::

:::kern Das Wichtigste
<ul>

<li>

Verzerrungsfrei: $h=h_0\delta(t-t_0)$, $H=h_0\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: konstanter Betrag, lineare Phase.

</li>

<li>

$a=-20\lg|H|$ dB; $t_\mathrm p=-\frac{\varphi}{2\pi f}$; $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$.

</li>

<li>

Idealer Tiefpass: $\operatorname{rect}(f/2f_\mathrm g)\leftrightarrow2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$, nicht kausal; $f_\mathrm g t_m=\frac12$; Überschwingen 21,7 % (Impuls), 8,95 % (Sprung).

</li>

<li>

Sprungantwort $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$, $\operatorname{Si}(\infty)=\frac\pi2$, Einschwingzeit $\frac{1}{2f_\mathrm g}$.

</li>

<li>

Abschneiden der Impulsantwort $=$ Faltung im Spektrum; weiche Fenster: tiefere Sperrung, flachere Flanke.

</li>

<li>

Pulsformfilter: $T\operatorname{rect}(Tf)[1+\cos(2\pi Tf)]$, wenig Überschwingen.

</li>

<li>

$H(f)=\frac12H_T(f-f_0)+\frac12H_T^*(-f-f_0)$; $s=\operatorname{Re}\{s_T\mathrm{e}^{\mathrm{j}2\pi f_0t}\}=s_{Tr}\cos-s_{Ti}\sin$; $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

</li>

<li>

$g_T=\frac12s_T*h_T$; Hüllkurve um $t_\mathrm g$, Träger um $t_\mathrm p$ verzögert.

</li>

<li>

Bandpass-Abtastung: $2\Delta f$ Werte je Sekunde; digitaler Hochpass: $(-1)^nh_{\mathrm{TP}}(n)$.

</li>

</ul>
:::
