---
title: Stufe 12: Zeitdiskrete Bandpässe und Hochpässe
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3251300
summary: Digitale Bandpässe und Hochpässe gewinnt man aus einem Tiefpass durch Modulation.
tags: Hochpass
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Digitale Bandpässe und Hochpässe gewinnt man aus einem Tiefpass durch Modulation.
:::

Hat der zeitdiskrete Tiefpass eine reelle Impulsantwort, verschiebt die Multiplikation mit $2\cos(2\pi f_0n)$ seinen Durchlassbereich nach $\pm f_0$:

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

gültig, solange sich die verschobenen Bänder nicht überlappen: $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$. Wegen der Periodizität darf das Band bei $f_0$ weder das Band bei $-f_0$ noch dessen Kopie bei $1-f_0$ berühren. Allgemein, auch für komplexe Tiefpass-Impulsantworten, gilt wie in [(8.1)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-1) $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$. Der Faktor 2 entspricht dem verdoppelten äquivalenten Tiefpass $H_T=2H_{\mathrm{TP}}$.

Ein __Hochpass__ ist ein Tiefpass, verschoben zur halben Abtastrate $f_0=\frac12$. Dort fallen das Band und sein Spiegelbild zusammen, deshalb verschiebt man nur einmal: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. Mit $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$:

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**Kurz gesagt:** Ein digitaler Hochpass entsteht aus einem Tiefpass, indem man jedes zweite Vorzeichen umdreht.

:::aufgabe Aufgabe 11 ★ Hochpass aus dem gleitenden Mittelwert
<span class="anker" id="aufg-11"></span>

Der gleitende Mittelwert $h_{\mathrm{TP}}=\frac13(1,1,1)$ ([Kapitel 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) ist ein einfacher Tiefpass.

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

::::formelsammlung
**Zeitdiskreter Bandpass**

$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n)$$

Für einen Tiefpass mit reeller Impulsantwort: Der Durchlassbereich rückt nach $\pm f_0$.

**Keine Überlappung**

$$f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$$

Wegen der Periodizität darf das Band bei $f_0$ weder das Band bei $-f_0$ noch dessen Kopie bei $1-f_0$ berühren.

**Zeitdiskreter Bandpass, allgemein**

$$h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$$

Auch für komplexe Tiefpass-Impulsantworten; der Faktor 2 entspricht dem verdoppelten äquivalenten Tiefpass $H_T=2H_{\mathrm{TP}}$.

**Hochpass**

$$H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\tfrac12),\qquad h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n)$$

Tiefpass, verschoben zur halben Abtastrate; dort fallen Band und Spiegelbild zusammen, deshalb verschiebt man nur einmal. Mit $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$: jedes zweite Vorzeichen umdrehen.
::::

::::lernkarten
:::karte formel Zeitdiskreter Bandpass
Wie gewinnt man aus einem zeitdiskreten Tiefpass mit reeller Impulsantwort einen Bandpass mit der Mittenfrequenz $f_0$?
---
Man multipliziert die Impulsantwort mit $2\cos(2\pi f_0n)$: $h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n)$, im Spektrum $H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]$. Der Durchlassbereich rückt nach $\pm f_0$.
--- falsch
Man faltet die Impulsantwort mit $2\cos(2\pi f_0n)$, im Spektrum also $H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)\cdot\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]$. Der Durchlassbereich wird dabei auf die zwei Linien bei $\pm f_0$ reduziert, und nur diese beiden Frequenzen kommen durch.
--- falsch
Man verschiebt die Impulsantwort um $f_0$ Takte: $h_{\mathrm{BP}}(n)=h_{\mathrm{TP}}(n-f_0)$, im Spektrum $H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0f}$. Eine Verzögerung in der Zeit verschiebt den Durchlassbereich zur Frequenz $f_0$.
--- falsch
Man addiert zur Impulsantwort einen Kosinus: $h_{\mathrm{BP}}(n)=h_{\mathrm{TP}}(n)+2\cos(2\pi f_0n)$, im Spektrum kommen zwei Linien bei $\pm f_0$ hinzu. Der Durchlassbereich des Tiefpasses bleibt erhalten und wird um das neue Band ergänzt.
:::
:::karte zusammenhang Bedingung für den Bandpass
Für welche Mittenfrequenzen $f_0$ ergibt die Modulation eines zeitdiskreten Tiefpasses mit der Grenzfrequenz $f_{\mathrm g,\mathrm{TP}}$ einen Bandpass, und warum?
---
Für $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$: Die verschobenen Bänder dürfen sich nicht überlappen. Wegen der Periodizität darf das Band bei $f_0$ weder das Band bei $-f_0$ noch dessen Kopie bei $1-f_0$ berühren.
--- falsch
Für alle $f_0$ zwischen 0 und 1: Das Spektrum eines zeitdiskreten Signals ist periodisch mit 1, deshalb passt das verschobene Band bei jeder Mittenfrequenz innerhalb einer Periode, ohne mit anderen Bändern zusammenzustoßen.
--- falsch
Für alle $f_0\ge f_{\mathrm g,\mathrm{TP}}$, nach oben unbegrenzt: Es genügt, dass das Band bei $f_0$ das Band bei $-f_0$ nicht berührt; weitere Kopien des Spektrums gibt es bei Folgen nicht.
--- falsch
Für $f_0\le f_{\mathrm g,\mathrm{TP}}$: Die Mittenfrequenz muss im Durchlassbereich des Tiefpasses liegen, sonst verschiebt die Modulation das Band in den Sperrbereich, und es wird dort ausgelöscht.
:::
:::karte formel Zeitdiskreter Bandpass, allgemein
Wie lautet die Impulsantwort des zeitdiskreten Bandpasses allgemein, auch für eine komplexe Tiefpass-Impulsantwort, und woher kommt der Faktor 2?
---
$h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$, wie bei der komplexen Hüllkurve. Der Faktor 2 entspricht dem verdoppelten äquivalenten Tiefpass $H_T=2H_{\mathrm{TP}}$.
--- falsch
$h_{\mathrm{BP}}(n)=\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$ ohne Faktor: Die Bildung des Realteils ändert die Höhe des Bandes nicht, deshalb kommt der Bandpass mit der Höhe des Tiefpasses aus.
--- falsch
$h_{\mathrm{BP}}(n)=2h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}$: Der Bandpass hat stets eine komplexe Impulsantwort, und der Faktor 2 gleicht aus, dass nur das Band bei $+f_0$ entsteht.
--- falsch
$h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\}\cos(2\pi f_0n)$: Nur der Realteil des Tiefpasses wird moduliert, der Imaginärteil fällt weg; der Faktor 2 kommt von den zwei Dirac-Impulsen bei $\pm f_0$.
:::
:::karte begriff Hochpass
Wie entsteht ein zeitdiskreter Hochpass aus einem Tiefpass, wenn man ihn als verschobenen Tiefpass auffasst?
---
Ein Hochpass ist ein Tiefpass, verschoben zur halben Abtastrate $f_0=\frac12$: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. Dort fallen das Band und sein Spiegelbild zusammen, deshalb verschiebt man nur einmal.
--- falsch
Ein Hochpass ist ein Tiefpass, verschoben zur Abtastrate $f_0=1$: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-1)$. Dort liegt die höchste Frequenz, die eine Folge überhaupt darstellen kann.
--- falsch
Ein Hochpass ist ein Tiefpass, verschoben zur halben Abtastrate: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)+H_{\mathrm{TP}}(f+\frac12)$. Band und Spiegelbild werden wie beim Bandpass beide verschoben.
--- falsch
Ein Hochpass ist der Kehrwert eines Tiefpasses: $H_{\mathrm{HP}}(f)=1/H_{\mathrm{TP}}(f)$. Wo der Tiefpass stark dämpft, verstärkt der Hochpass entsprechend stark, und umgekehrt.
:::
:::karte formel Hochpass aus dem Tiefpass
Wie hängt die Impulsantwort des zeitdiskreten Hochpasses mit der des Tiefpasses zusammen, und warum?
---
$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n)$, weil die Verschiebung um $\frac12$ eine Multiplikation mit $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$ ist. Man dreht also jedes zweite Vorzeichen um.
--- falsch
$h_{\mathrm{HP}}(n)=h_{\mathrm{TP}}(-n)$, weil die Spiegelung der Zeit die Frequenzen spiegelt: Tiefe Frequenzen werden zu hohen, und man liest die Koeffizienten einfach rückwärts.
--- falsch
$h_{\mathrm{HP}}(n)=2\cos(\pi n)\,h_{\mathrm{TP}}(n)$, weil man wie beim Bandpass mit dem doppelten Kosinus moduliert: Jedes zweite Vorzeichen dreht sich um, und alle Werte verdoppeln sich.
--- falsch
$h_{\mathrm{HP}}(n)=-h_{\mathrm{TP}}(n)$, weil ein Hochpass das Gegenteil eines Tiefpasses ist: Alle Vorzeichen werden umgedreht, und so wird aus dem Durchlassbereich der Sperrbereich.
:::
:::karte zusammenhang Hochpass aus dem gleitenden Mittelwert
Welchen Hochpass erhält man aus dem gleitenden Mittelwert $h_{\mathrm{TP}}=\frac13(1,1,1)$, und wie verhält er sich bei $f=0$ und $f=\frac12$?
---
$h_{\mathrm{HP}}=\frac13(1,-1,1)$ mit $|H_{\mathrm{HP}}(0)|=\frac13$ und $|H_{\mathrm{HP}}(\frac12)|=1$: Die schnellste Folge $(+1,-1,+1,\dots)$ kommt voll durch, der Gleichanteil nur zu einem Drittel.
--- falsch
$h_{\mathrm{HP}}=\frac13(-1,-1,-1)$ mit $|H_{\mathrm{HP}}(0)|=1$ und $|H_{\mathrm{HP}}(\frac12)|=\frac13$: Das Umdrehen aller Vorzeichen ändert den Betrag nicht, deshalb verhält er sich genau wie der Tiefpass.
--- falsch
$h_{\mathrm{HP}}=\frac13(1,-1,1)$ mit $|H_{\mathrm{HP}}(0)|=0$ und $|H_{\mathrm{HP}}(\frac12)|=1$: Weil sich die Vorzeichen abwechseln, heben sich die Koeffizienten bei $f=0$ vollständig gegenseitig auf.
--- falsch
$h_{\mathrm{HP}}=\frac13(1,0,-1)$ mit $|H_{\mathrm{HP}}(0)|=0$ und $|H_{\mathrm{HP}}(\frac12)|=0$: Der mittlere Wert fällt weg, und das Filter sperrt den Gleichanteil und die schnellste Folge gleichermaßen.
:::
:::karte herleitung Impulsantwort des Hochpasses
Wie folgt aus $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$ die Impulsantwort $h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n)$?
---
Eine Verschiebung des Spektrums um $f_0$ ist im Zeitbereich eine Multiplikation mit $\mathrm{e}^{\mathrm{j}2\pi f_0n}$, weil die Modulationsregel auch für Folgen gilt.
---
Mit $f_0=\frac12$ wird daraus $\mathrm{e}^{\mathrm{j}\pi n}$, weil sich der Faktor $2\pi$ mit $\frac12$ zu $\pi$ verkürzt.
---
Es gilt $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$, weil jede halbe Umdrehung auf dem Einheitskreis das Vorzeichen wechselt und $n$ ganzzahlig ist.
---
Man verschiebt nur einmal und ohne Faktor 2, weil bei $f_0=\frac12$ das Band und sein Spiegelbild zusammenfallen; also ist $h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n)$.
:::
::::
