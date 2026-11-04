---
title: Stabilität
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220600
summary: Ob ein System stabil ist, lässt sich an der Lage seiner Pole ablesen, ohne die Impulsantwort zu integrieren.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ob ein System stabil ist, lässt sich an der Lage seiner Pole ablesen, ohne die Impulsantwort zu integrieren.
:::

### Rückblick: Stabilität im Zeitbereich

<span class="anker" id="stufe-5-1"></span>

Aus dem Kapitel zur Faltung: Ein System heißt stabil (BIBO-stabil), wenn es auf jeden beschränkten Eingang mit einem beschränkten Ausgang antwortet. Ein LTI-System ist genau dann stabil, wenn seine Impulsantwort absolut integrierbar ist:

<span class="anker" id="gl-5-1"></span>
$$\int_{-\infty}^{\infty}|h(t)|\,\mathrm{d} t<\infty . \tag{5.1}$$

### Die Bedingung in der $p$-Ebene

<span class="anker" id="stufe-5-2"></span>

Hat $H(p)$ die Form eines Polynombruchs, so ist $h(t)$ nach der Partialbruchzerlegung eine Summe von Exponentialfunktionen $\mathrm{e}^{p_\mathrm Pt}$, rechtsseitig oder linksseitig, eventuell mit Potenzen von $t$ davor, und eventuell einem Summanden $A_0\,\delta(t)$. Der Dirac-Impuls stört die Bedingung [(5.1)](#gl-5-1) nicht. Die Summe ist genau dann absolut integrierbar, wenn jeder Summand es ist. Ein Summand ist es genau dann, wenn er auf seiner Seite abklingt, und dafür kommt es nur auf $\sigma_\mathrm P=\operatorname{Re} p_\mathrm P$ an. Damit [(5.1)](#gl-5-1) erfüllt ist, müssen also

<ul>

<li>

alle Pole, die zu einem rechtsseitigen (kausalen) Summanden der Impulsantwort gehören, in der linken Hälfte der $p$-Ebene liegen, also bei $\sigma_\mathrm P<0$. Dann klingt die zugehörige Zeitfunktion $\mathrm{e}^{\sigma_\mathrm Pt}\varepsilon(t)$ für $t\to+\infty$ ab.

</li>

<li>

alle Pole, die zu einem linksseitigen (antikausalen) Summanden der Impulsantwort gehören, in der rechten Hälfte der $p$-Ebene liegen, also bei $\sigma_\mathrm P>0$. Dann klingt die zugehörige Zeitfunktion $\mathrm{e}^{\sigma_\mathrm Pt}\varepsilon(-t)$ für $t\to-\infty$ ab.

</li>

</ul>

Ein Faktor $t^{j-1}$ bei einem mehrfachen Pol ändert daran nichts, denn eine abklingende Exponentialfunktion wird schneller klein, als jede Potenz von $t$ wächst. Ein Pol genau auf der imaginären Achse ($\sigma_\mathrm P=0$) macht das System instabil, denn $|\mathrm{e}^{\mathrm{j}\omega t}|=1$ klingt nicht ab.

⁠**Kurz gesagt:** Ein kausales System ist genau dann stabil, wenn alle Pole von $H(p)$ in der linken Halbebene liegen.

:::hintergrund Ein Kriterium für alle Fälle: die imaginäre Achse
Beide Regeln lassen sich zu einer zusammenfassen: Ein LTI-System ist genau dann stabil, wenn die imaginäre Achse $\sigma=0$ im Konvergenzbereich von $H(p)$ liegt. Der Grund steckt in der Definition des Konvergenzbereichs: $p=\mathrm{j}2\pi f$ gehört genau dann dazu, wenn $\int|h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}|\,\mathrm{d} t=\int|h(t)|\,\mathrm{d} t$ endlich ist. Das ist wörtlich die Stabilitätsbedingung [(5.1)](#gl-5-1). Für ein kausales System liegt der Konvergenzbereich rechts aller Pole. Er enthält die imaginäre Achse also genau dann, wenn alle Pole links von ihr liegen.
:::

:::hintergrund Warum passive Netzwerke stabil sind und wie Oszillatoren entstehen
Nach dem Kasten zu den Eigenbewegungen im vierten Abschnitt ist jeder Pol der Exponent einer Bewegung, die das System ohne Eingang ausführen kann. Ein Netzwerk aus Widerständen, Spulen und Kondensatoren enthält keine Energiequelle. Sobald der Eingang schweigt, kann die gespeicherte Energie nur abnehmen, weil die Widerstände sie in Wärme umwandeln. Jede Eigenbewegung muss deshalb abklingen, und alle Pole liegen links der imaginären Achse. Ohne Widerstand bliebe die Energie erhalten, und die Pole lägen genau auf der Achse: eine ungedämpfte Schwingung, die nie abklingt.

Ein Verstärker kann dagegen Energie aus seiner Versorgung zuführen. Mit Rückkopplung lassen sich die Pole dadurch in die rechte Halbebene schieben; die Schwingung wächst dann, bis die Versorgungsspannung sie begrenzt. Ungewollt ist das ein Fehler: Ein Verstärker „schwingt“. Gewollt ist es das Prinzip jedes Oszillators, der eine Schwingung erzeugen soll.
:::

### Beispiel: ein wachsender Exponentialimpuls

<span class="anker" id="stufe-5-3"></span>

Ein kausales System mit der Impulsantwort $h(t)=\mathrm{e}^{2t}\varepsilon(t)$ hat einen Pol bei $p=2/\mathrm s$:

<span class="anker" id="gl-5-2"></span>
$$h(t)=\mathrm{e}^{2t}\varepsilon(t)\quad\Longrightarrow\quad H(p)=\frac{1}{p-2},\qquad\text{wenn }\operatorname{Re}\{p\}>2 . \tag{5.2}$$

Der Pol liegt in der rechten Halbebene, die Impulsantwort wächst über alle Grenzen. Dieses System ist instabil.

### Beispiel: ein System zweiter Ordnung

<span class="anker" id="stufe-5-4"></span>

Ein kausales System mit zwei Polen habe die Impulsantwort

<span class="anker" id="gl-5-3"></span>
$$h(t)=A\cdot\bigl[\mathrm{e}^{p_{\mathrm P1}t}-\mathrm{e}^{p_{\mathrm P2}t}\bigr]\cdot\varepsilon(t)\quad\text{mit}\quad A=\frac{\omega_0}{2\sqrt{\xi^2-1}},\qquad p_{\mathrm P1,2}=-\underbrace{\xi\omega_0}_{a}\pm\underbrace{\omega_0\sqrt{\xi^2-1}}_{b}. \tag{5.3}$$

Mit dem Grundpaar [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) ist

<span class="anker" id="gl-5-4"></span>
$$H(p)=\frac{\omega_0^2}{(p-p_{\mathrm P1})(p-p_{\mathrm P2})}\qquad\text{mit}\qquad\operatorname{Re}\{p\}>\begin{cases}-\xi\omega_0+\omega_0\sqrt{\xi^2-1}, & \text{wenn }|\xi|\ge1,\\ -\xi\omega_0, & \text{wenn }|\xi|\le1 .\end{cases} \tag{5.4}$$

Zur Kontrolle: $A\,\bigl[\frac{1}{p-p_{\mathrm P1}}-\frac{1}{p-p_{\mathrm P2}}\bigr]=A\,\frac{p_{\mathrm P1}-p_{\mathrm P2}}{(p-p_{\mathrm P1})(p-p_{\mathrm P2})}$ mit $A\,(p_{\mathrm P1}-p_{\mathrm P2})=\frac{\omega_0}{2\sqrt{\xi^2-1}}\cdot2\omega_0\sqrt{\xi^2-1}=\omega_0^2$. Die Grenze des Konvergenzbereichs ist der Realteil des am weitesten rechts liegenden Pols: für $|\xi|\ge1$ der reelle Pol $-\xi\omega_0+\omega_0\sqrt{\xi^2-1}$, für $|\xi|\le1$ der gemeinsame Realteil $-\xi\omega_0$ des Polpaars.

Die Polpositionen und die Lage des Konvergenzbereichs zeigt Abb. [7](losung-von-differentialgleichungen.html#abb-7). Formal ist das das RLC-System mit der Parametrierung

<span class="anker" id="gl-5-5"></span>
$$\omega_0=\frac{1}{\sqrt{LC}}\ ;\qquad\xi=\frac R2\sqrt{\frac CL}, \tag{5.5}$$

denn $\omega_0^2=1/LC$ ist genau der Zähler von [(4.7)](losung-von-differentialgleichungen.html#gl-4-7). Für $\xi>0$ liegen beide Pole links, das System ist stabil. Für $\xi\le0$ ist es instabil:

<ul>

<li>

$\xi<0$: Der Realteil $-\xi\omega_0$ der Pole ist positiv, die Impulsantwort wächst. Beim RLC-System hieße das $R<0$, ein „negativer Widerstand“, wie ihn eine aktive Schaltung nachbilden kann, die Energie zuführt.

</li>

<li>

$\xi=0$: Die Pole liegen bei $\pm\mathrm{j}\omega_0$ auf der imaginären Achse. Die Impulsantwort ist $h(t)=\omega_0\sin(\omega_0t)\,\varepsilon(t)$ (der Faktor $A=\frac{\omega_0}{2\mathrm{j}}$ macht aus der Klammer einen Sinus). Sie bleibt beschränkt, ist aber nicht absolut integrierbar.

</li>

</ul>

⁠**Kurz gesagt:** Das System zweiter Ordnung ist genau dann stabil, wenn der Dämpfungsgrad positiv ist.

:::aufgabe Aufgabe 7 ★ Stabil oder nicht?
<span class="anker" id="aufg-7"></span>

Gegeben sind Übertragungsfunktionen mit Konvergenzbereich ($p$ in $1/\mathrm s$). Bestimme jeweils $h(t)$ und entscheide, ob das System stabil und ob es kausal ist.

<ol class="al">

<li>

$H(p)=\frac{1}{p+3}$, $\operatorname{Re} p>-3$.

</li>

<li>

$H(p)=\frac{1}{p-1}$, $\operatorname{Re} p<1$.

</li>

<li>

$H(p)=\frac{1}{p^2+4}$, $\operatorname{Re} p>0$.

</li>

<li>

$H(p)=\frac{p-2}{(p+1)(p+3)}$, $\operatorname{Re} p>-1$. Stört die Nullstelle in der rechten Halbebene?

</li>

</ol>

:::loesung
(a) $h(t)=\mathrm{e}^{-3t}\varepsilon(t)$ nach [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9). Kausal, denn der Konvergenzbereich liegt rechts des Pols. Stabil, denn der Pol $-3$ liegt links; $\int|h|\,\mathrm{d} t=\frac13$.

(b) Der Konvergenzbereich liegt links des Pols, also nach [(2.10)](beispiele-zur-laplace-transformation.html#gl-2-10): $h(t)=-\mathrm{e}^{t}\varepsilon(-t)$. Nicht kausal (antikausal). Stabil: Der Pol bei $+1$ gehört zu einem linksseitigen Summanden und liegt rechts, wie es die Regel verlangt. $\int|h|\,\mathrm{d} t=\int_{-\infty}^0\mathrm{e}^t\mathrm{d} t=1$.

(c) $H(p)=\frac12\cdot\frac{2}{p^2+2^2}$ ist nach [(4.26)](losung-von-differentialgleichungen.html#gl-4-26) mit $\gamma=0$ und $\omega_1=2$ die Transformierte von $h(t)=\frac12\sin(2t)\,\varepsilon(t)$. Kausal, aber instabil: Die Pole $\pm2\mathrm{j}$ liegen auf der imaginären Achse. $h$ bleibt beschränkt, aber $\int|h|\,\mathrm{d} t=\infty$. Ein Eingang $\sin(2t)\varepsilon(t)$ (beschränkt) erzeugt einen Ausgang, der wie $t$ anwächst.

(d) Partialbrüche mit [(4.11)](losung-von-differentialgleichungen.html#gl-4-11): $A_1=\lim_{p\to-1}\frac{p-2}{p+3}=\frac{-3}{2}$, $A_2=\lim_{p\to-3}\frac{p-2}{p+1}=\frac{-5}{-2}=\frac52$. Also $h(t)=\bigl(-\tfrac32\mathrm{e}^{-t}+\tfrac52\mathrm{e}^{-3t}\bigr)\varepsilon(t)$. Kausal und stabil, denn beide Pole liegen links. Die Nullstelle bei $+2$ stört nicht: Für die Stabilität zählen nur die Pole, denn nur sie bestimmen die Exponenten in $h(t)$.
:::
:::
