---
title: Stabilität
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Laplace-Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Kapitel 2: Laplace-Transformation
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

::::kurzfassung
Ob ein LTI-System stabil ist, liest man an der Lage seiner Pole ab, ohne die Impulsantwort zu integrieren: Ein kausales System ist genau dann stabil, wenn alle Pole von $H(p)$ in der linken Halbebene liegen.

Stabil heißt, dass jeder beschränkte Eingang einen beschränkten Ausgang ergibt. Für ein LTI-System ist das gleichbedeutend mit

$$\int_{-\infty}^{\infty}|h(t)|\,\mathrm{d} t<\infty .$$

Bei einem Polynombruch $H(p)$ ist $h(t)$ nach der Partialbruchzerlegung eine Summe von Exponentialfunktionen $\mathrm{e}^{p_\mathrm Pt}$, eventuell mit Potenzen von $t$ und einem Dirac-Impuls. Die Summe ist genau dann absolut integrierbar, wenn jeder Summand auf seiner Seite abklingt, und das hängt nur von $\sigma_\mathrm P=\operatorname{Re} p_\mathrm P$ ab. Pole rechtsseitiger Summanden müssen deshalb bei $\sigma_\mathrm P<0$ liegen, Pole linksseitiger bei $\sigma_\mathrm P>0$. Beide Regeln fasst ein Kriterium zusammen: Ein LTI-System ist genau dann stabil, wenn die imaginäre Achse im Konvergenzbereich von $H(p)$ liegt.

Physikalisch: Ein Netzwerk aus Widerständen, Spulen und Kondensatoren verliert ohne Eingang Energie in den Widerständen. Seine Eigenbewegungen klingen ab, alle Pole liegen links. Ein Verstärker kann dagegen Energie zuführen und Pole in die rechte Halbebene schieben; gewollt ergibt das einen Oszillator. Das kausale System zweiter Ordnung ist genau dann stabil, wenn sein Dämpfungsgrad $\xi$ positiv ist.

Fallen: Ein Pol genau auf der imaginären Achse macht das System instabil, auch wenn $h(t)$ beschränkt bleibt. Nullstellen spielen für die Stabilität keine Rolle, auch nicht in der rechten Halbebene.
::::

::::formelsammlung
**Stabilität (BIBO) eines LTI-Systems**

$$\int_{-\infty}^{\infty}|h(t)|\,\mathrm{d} t<\infty$$

Genau dann antwortet das System auf jeden beschränkten Eingang mit einem beschränkten Ausgang.

**Bedingung für Pole rechtsseitiger Anteile**

$$\sigma_\mathrm P<0$$

$\sigma_\mathrm P=\operatorname{Re} p_\mathrm P$; gilt für jeden Pol eines rechtsseitigen (kausalen) Summanden von $h(t)$. Kausales System: stabil genau dann, wenn alle Pole in der linken Halbebene liegen.

**Bedingung für Pole linksseitiger Anteile**

$$\sigma_\mathrm P>0$$

Für jeden Pol eines linksseitigen (antikausalen) Summanden. Allgemein: stabil genau dann, wenn die imaginäre Achse im Konvergenzbereich von $H(p)$ liegt. Ein Pol auf der imaginären Achse macht instabil; Nullstellen spielen keine Rolle.

**System zweiter Ordnung: Impulsantwort**

$$h(t)=A\cdot\bigl[\mathrm{e}^{p_{\mathrm P1}t}-\mathrm{e}^{p_{\mathrm P2}t}\bigr]\cdot\varepsilon(t)\quad\text{mit}\quad A=\frac{\omega_0}{2\sqrt{\xi^2-1}}$$

Kausal; Pole $p_{\mathrm P1,2}=-\xi\omega_0\pm\omega_0\sqrt{\xi^2-1}$; beim RLC-System $\omega_0=1/\sqrt{LC}$, $\xi=\frac R2\sqrt{\frac CL}$.

**System zweiter Ordnung: Übertragungsfunktion**

$$H(p)=\frac{\omega_0^2}{(p-p_{\mathrm P1})(p-p_{\mathrm P2})}\qquad\text{mit}\qquad\operatorname{Re}\{p\}>\begin{cases}-\xi\omega_0+\omega_0\sqrt{\xi^2-1}, & \text{wenn }|\xi|\ge1,\\ -\xi\omega_0, & \text{wenn }|\xi|\le1 .\end{cases}$$

Stabil genau für $\xi>0$; für $\xi<0$ wachsende Impulsantwort.

**System zweiter Ordnung: ungedämpft**

$$h(t)=\omega_0\sin(\omega_0t)\,\varepsilon(t)$$

$\xi=0$, Pole bei $\pm\mathrm{j}\omega_0$ auf der imaginären Achse: beschränkt, aber nicht absolut integrierbar, also instabil.
::::

::::lernkarten
:::karte zusammenhang Pole eines kausalen stabilen Systems
Warum ist ein kausales LTI-System mit rationaler Übertragungsfunktion genau dann stabil, wenn alle Pole von $H(p)$ in der linken Halbebene liegen?
---
Nach der Partialbruchzerlegung ist $h(t)$ eine Summe rechtsseitiger Exponentialfunktionen $\mathrm{e}^{p_\mathrm Pt}$, eventuell mit Potenzen von $t$ und einem Summanden $A_0\,\delta(t)$. Die Summe ist genau dann absolut integrierbar, wenn jeder Anteil für $t\to+\infty$ abklingt, und das verlangt $\sigma_\mathrm P<0$ mit $\sigma_\mathrm P=\operatorname{Re} p_\mathrm P$.
--- falsch
Weil Pole in der linken Halbebene negative Frequenzen bedeuten und ein kausales System nur auf positive Frequenzen reagiert. Pole rechts würden Frequenzen durchlassen, die das System so lange verstärkt, bis es übersteuert und sein Ausgang an die Versorgung stößt.
--- falsch
Nach der Partialbruchzerlegung ist $h(t)$ eine Summe rechtsseitiger Anteile $\mathrm{e}^{p_\mathrm Pt}\varepsilon(t)$. Die Summe ist beschränkt, sobald mindestens ein Anteil abklingt; deshalb genügt es, wenn der am weitesten links liegende Pol einen negativen Realteil hat.
--- falsch
Weil ein Pol links der imaginären Achse eine Nullstelle des Nenners mit negativem Wert ist, sodass $H(p)$ dort negativ wird. Ein negatives $H$ wirkt wie eine Gegenkopplung, die jeden Ausgang begrenzt und das System deshalb stabil hält.
:::
:::karte zusammenhang Pole linksseitiger Anteile
Wo müssen die Pole liegen, die zu linksseitigen Anteilen der Impulsantwort gehören, damit das System stabil ist, und warum?
---
In der rechten Hälfte der $p$-Ebene, bei $\sigma_\mathrm P>0$: Dann klingt die zugehörige Zeitfunktion $\mathrm{e}^{\sigma_\mathrm Pt}\varepsilon(-t)$ für $t\to-\infty$ ab. Für rechtsseitige Anteile gilt umgekehrt $\sigma_\mathrm P<0$, damit $\mathrm{e}^{\sigma_\mathrm Pt}\varepsilon(t)$ für $t\to+\infty$ abklingt.
--- falsch
Ebenfalls in der linken Hälfte der $p$-Ebene, bei $\sigma_\mathrm P<0$: Die Stabilitätsregel gilt für jeden Pol gleich, ob er zu einem rechtsseitigen oder zu einem linksseitigen Anteil gehört, weil der Betrag $|\mathrm{e}^{\sigma_\mathrm Pt}|$ nicht von der Seite abhängt.
--- falsch
Genau auf der imaginären Achse, bei $\sigma_\mathrm P=0$: Dann ist $|\mathrm{e}^{\mathrm{j}\omega t}|=1$, und der Anteil bleibt für $t\to-\infty$ beschränkt. Liegt der Pol rechts davon, wächst der linksseitige Anteil in der Vergangenheit über alle Grenzen.
--- falsch
Linksseitige Anteile machen ein System immer instabil, gleichgültig, wo ihre Pole liegen, weil sie vor dem Eingang reagieren. Für rechtsseitige Anteile gilt die Regel $\sigma_\mathrm P<0$, damit $\mathrm{e}^{\sigma_\mathrm Pt}\varepsilon(t)$ für $t\to+\infty$ abklingt.
:::
:::karte zusammenhang Pol auf der imaginären Achse
Warum macht ein Pol genau auf der imaginären Achse ein System instabil, obwohl seine Impulsantwort beschränkt bleiben kann?
---
Für $\sigma_\mathrm P=0$ ist $|\mathrm{e}^{\mathrm{j}\omega t}|=1$, der Anteil klingt nicht ab. Die Impulsantwort bleibt dann zwar beschränkt, ist aber nicht absolut integrierbar; so erzeugt der beschränkte Eingang $\sin(2t)\varepsilon(t)$ bei Polen $\pm2\mathrm{j}$ einen Ausgang, der wie $t$ anwächst.
--- falsch
Weil ein Pol auf der imaginären Achse eine Schwingung bedeutet und jedes schwingende System instabil ist. Auch ein Pol bei $-1\pm\mathrm{j}$ macht ein System deshalb instabil, weil seine Impulsantwort schwingt und dabei immer wieder ihr Vorzeichen wechselt.
--- falsch
Für $\sigma_\mathrm P=0$ ist $|\mathrm{e}^{\mathrm{j}\omega t}|=0$, der Anteil verschwindet sofort. Das System antwortet auf diese Frequenz gar nicht mehr, und ein Eingang dieser Frequenz staut sich im System auf, bis der Ausgang über alle Grenzen wächst.
--- falsch
Weil die imaginäre Achse die Grenze des Konvergenzbereichs ist und $H(p)$ dort nicht existiert. Eine Impulsantwort ist auf dieser Achse nicht definiert, und ein System ohne definierte Impulsantwort gilt grundsätzlich als instabil.
:::
:::karte zusammenhang Mehrfacher Pol und Stabilität
Warum ändert ein Faktor $t^{j-1}$ bei einem mehrfachen Pol nichts an der Regel, dass der Pol links der imaginären Achse liegen muss?
---
Eine abklingende Exponentialfunktion wird schneller klein, als jede Potenz von $t$ wächst. Liegt der Pol links der imaginären Achse, klingt deshalb auch der Anteil mit dem Faktor $t^{j-1}$ für $t\to\infty$ ab und bleibt absolut integrierbar.
--- falsch
Weil der Faktor $t^{j-1}$ nur in der Nähe von $t=0$ wirkt und danach bedeutungslos wird. Für große $t$ ist $t^{j-1}$ ungefähr 1, und es bleibt allein die Exponentialfunktion des Pols übrig, die über die Stabilität entscheidet.
--- falsch
Weil sich der Faktor $t^{j-1}$ bei der Partialbruchzerlegung gegen die Nullstellen von $H(p)$ kürzt. In der Impulsantwort eines stabilen Systems tritt er deshalb gar nicht auf, sondern nur bei instabilen Systemen mit Polen rechts.
--- falsch
Weil eine Potenz von $t$ ebenfalls abklingt, sobald sie mit $\varepsilon(t)$ multipliziert wird. Das Produkt zweier abklingender Funktionen klingt erst recht ab, gleichgültig, wie groß der Exponent $j-1$ gewählt ist.
:::
:::karte zusammenhang Imaginäre Achse im Konvergenzbereich
Warum ist ein LTI-System genau dann stabil, wenn die imaginäre Achse im Konvergenzbereich von $H(p)$ liegt?
---
Der Punkt $p=\mathrm{j}2\pi f$ gehört genau dann zum Konvergenzbereich, wenn $\int|h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}|\,\mathrm{d} t=\int|h(t)|\,\mathrm{d} t$ endlich ist; das ist wörtlich die Stabilitätsbedingung. Bei einem kausalen System liegt der Bereich rechts aller Pole und enthält die Achse genau dann, wenn alle Pole links von ihr liegen.
--- falsch
Weil auf der imaginären Achse $H(p)$ der Frequenzgang ist und ein System nur stabil sein kann, wenn sein Frequenzgang überall den Betrag 1 hat. Das ist genau dann der Fall, wenn die Achse im Konvergenzbereich liegt, weil $H$ dort weder null noch unendlich wird.
--- falsch
Weil die imaginäre Achse die Grenze zwischen kausalen und antikausalen Systemen bildet: Liegt sie im Konvergenzbereich, ist das System kausal, und jedes kausale System mit rationaler Übertragungsfunktion ist stabil, gleichgültig, wo seine Pole liegen.
--- falsch
Der Punkt $p=\mathrm{j}2\pi f$ gehört genau dann zum Konvergenzbereich, wenn $h(t)$ beschränkt ist, also $|h(t)|$ einen Höchstwert hat; das ist die Stabilitätsbedingung. Deshalb ist jedes System mit beschränkter Impulsantwort stabil, auch eines mit Polen auf der Achse.
:::
:::karte zusammenhang Passive Netzwerke
Warum ist ein Netzwerk aus Widerständen, Spulen und Kondensatoren stabil, und was wäre ohne Widerstand?
---
Es enthält keine Energiequelle. Schweigt der Eingang, kann die gespeicherte Energie nur abnehmen, weil die Widerstände sie in Wärme umwandeln; jede Eigenbewegung klingt ab, und alle Pole liegen links der imaginären Achse. Ohne Widerstand bliebe die Energie erhalten, und die Pole lägen genau auf der Achse.
--- falsch
Weil Spulen und Kondensatoren die Energie unbegrenzt speichern und dadurch jede Schwingung festhalten; die Pole liegen deshalb genau auf der imaginären Achse. Erst ein Widerstand schiebt sie nach rechts, sodass die Schwingung wächst; ohne Widerstand bleibt das Netzwerk deshalb stabil.
--- falsch
Es enthält keine Energiequelle, deshalb liegen alle Pole bei $p=0$. Ohne Widerstand wäre das Netzwerk dagegen instabil, weil die Pole dann in die rechte Halbebene wandern und jede Schwingung von selbst anwächst, bis ein Bauteil zerstört wird.
--- falsch
Weil ein solches Netzwerk keine Pole hat, sondern nur Nullstellen. Pole entstehen erst durch aktive Bauteile wie Verstärker; ohne Widerstand würden sich die Nullstellen auf der imaginären Achse sammeln und dort bestimmte Frequenzen sperren.
:::
:::karte zusammenhang Oszillator
Wie kann eine Schaltung mit Verstärker Pole in der rechten Halbebene bekommen, und wozu nutzt man das?
---
Der Verstärker führt Energie aus seiner Versorgung zu. Mit Rückkopplung lassen sich die Pole dadurch in die rechte Halbebene schieben, und die Schwingung wächst, bis die Versorgungsspannung sie begrenzt. Ungewollt ist das ein Fehler, gewollt das Prinzip jedes Oszillators.
--- falsch
Der Verstärker vergrößert scheinbar die Bauteilwerte von Spule und Kondensator, sodass die Pole näher an den Ursprung rücken und schließlich die imaginäre Achse überqueren. Man nutzt das, um Signale langsamer abklingen zu lassen und länger zu halten.
--- falsch
Der Verstärker kehrt das Vorzeichen des Eingangs um, und mit dem Vorzeichen spiegeln sich alle Pole an der imaginären Achse in die rechte Halbebene. Man nutzt das in Gleichrichtern, die negative Spannungen in positive verwandeln.
--- falsch
Der Verstärker entnimmt der Schaltung Energie und gibt sie als Wärme ab; die Schwingung klingt dadurch schneller ab, und die Pole rücken nach rechts. Man nutzt das in Dämpfern, die eine Schwingung möglichst rasch beenden sollen, etwa in Zeigermessgeräten.
:::
:::karte zusammenhang Wachsender Exponentialimpuls
Warum ist das kausale System mit der Impulsantwort $h(t)=\mathrm{e}^{2t}\varepsilon(t)$ instabil, und woran erkennt man das an $H(p)$?
---
$H(p)=\frac{1}{p-2}$ für $\operatorname{Re}\{p\}>2$ hat seinen Pol bei $p=2/\mathrm s$, also in der rechten Halbebene. Die Impulsantwort wächst deshalb über alle Grenzen und ist nicht absolut integrierbar.
--- falsch
$H(p)=\frac{1}{p-2}$ hat eine Nullstelle bei $p=-2/\mathrm s$, also in der linken Halbebene, und eine Nullstelle links lässt die Impulsantwort anwachsen. Die Lage der Pole spielt für die Stabilität dagegen keine Rolle.
--- falsch
$H(p)=\frac{1}{p-2}$ für $\operatorname{Re}\{p\}<2$ hat seinen Pol bei $p=2/\mathrm s$. Instabil ist das System, weil der Pol reell ist: Reelle Pole erzeugen keine Schwingung, die durch die Dämpfung abklingen könnte.
--- falsch
$H(p)=2\,\frac1p$ für $\operatorname{Re}\{p\}>0$ hat seinen Pol bei $p=0$, auf der imaginären Achse. Der Faktor 2 im Exponenten wird im Bildbereich zu einem Vorfaktor, und der Pol auf der Achse macht das System instabil.
:::
:::karte formel Stabilität und Dämpfungsgrad
Für welche Werte des Dämpfungsgrads $\xi$ ist das kausale System zweiter Ordnung $H(p)=\frac{\omega_0^2}{(p-p_{\mathrm P1})(p-p_{\mathrm P2})}$ stabil?
---
Genau für $\xi>0$, denn dann liegen beide Pole $p_{\mathrm P1,2}=-\xi\omega_0\pm\omega_0\sqrt{\xi^2-1}$ links. Für $\xi<0$ haben die Pole einen positiven Realteil, die Impulsantwort wächst. Für $\xi=0$ liegen die Pole bei $\pm\mathrm{j}\omega_0$, und $h(t)=\omega_0\sin(\omega_0t)\,\varepsilon(t)$ ist nicht absolut integrierbar.
--- falsch
Genau für $\xi>1$, denn nur dann sind beide Pole reell; konjugiert komplexe Pole für $0<\xi<1$ machen das System instabil, weil die Impulsantwort schwingt. Für $\xi=1$ ist das System gerade noch stabil, weil der doppelte Pol reell ist.
--- falsch
Genau für $\xi\ge0$, denn für $\xi=0$ liegen die Pole bei $\pm\mathrm{j}\omega_0$, und die Impulsantwort $h(t)=\omega_0\sin(\omega_0t)\,\varepsilon(t)$ bleibt beschränkt; das genügt für Stabilität. Erst für $\xi<0$ wächst die Impulsantwort über alle Grenzen.
--- falsch
Für jeden Wert von $\xi$, weil der Zähler $\omega_0^2$ stets positiv ist und die Pole sich deshalb immer links der imaginären Achse befinden. Ein negativer Dämpfungsgrad verlangsamt nur das Abklingen, kann es aber nicht in ein Wachsen umkehren.
:::
:::karte zusammenhang Nullstelle in der rechten Halbebene
Warum stört eine Nullstelle in der rechten Halbebene die Stabilität eines kausalen Systems nicht, etwa bei $H(p)=\frac{p-2}{(p+1)(p+3)}$?
---
Für die Stabilität zählen nur die Pole, denn nur sie bestimmen die Exponenten in $h(t)$. Hier ist $h(t)=\bigl(-\tfrac32\mathrm{e}^{-t}+\tfrac52\mathrm{e}^{-3t}\bigr)\varepsilon(t)$: Beide Exponenten stammen von den Polen $-1$ und $-3$, die Nullstelle bei $+2$ ändert nur die Vorfaktoren.
--- falsch
Weil sich die Nullstelle bei $+2$ gegen den Pol bei $-1$ kürzt, sodass in $h(t)$ nur der Anteil $\mathrm{e}^{-3t}$ übrig bleibt. Ohne einen solchen Pol, gegen den sie sich kürzen kann, würde eine Nullstelle rechts das System instabil machen.
--- falsch
Weil eine Nullstelle rechts nur Eingänge sperrt, die für $t\to\infty$ wachsen; solche Eingänge sind nicht beschränkt und kommen in der Stabilitätsbedingung nicht vor. Für beschränkte Eingänge wirkt die Nullstelle wie eine feste Verstärkung.
--- falsch
Weil Nullstellen bei kausalen Systemen grundsätzlich in die rechte Halbebene gehören, so wie Pole in die linke. Eine Nullstelle links würde dagegen stören, weil sie den Ausgang für $t\to\infty$ auf null zieht und den Eingang verschluckt.
:::
::::
