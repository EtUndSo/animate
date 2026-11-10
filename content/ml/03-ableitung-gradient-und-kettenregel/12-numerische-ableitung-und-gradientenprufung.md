---
title: Numerische Ableitung und Gradientenprüfung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Kapitel 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15231200
summary: Ableitungen kann man auch ohne Formel schätzen: Man wertet die Funktion an zwei nahen Stellen aus und bildet den Differenzenquotienten.
tags: Vorwärtsdifferenz, Abschneidefehler, zentrale Differenz, Gleitkommazahlen, Maschinengenauigkeit, Auslöschung, Gradientenprüfung, relativen Fehler
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Ableitungen kann man auch ohne Formel schätzen: Man wertet die Funktion an zwei nahen Stellen aus und bildet den Differenzenquotienten. Das ist zu langsam, um damit alle Ableitungen einer Funktion mit vielen Eingängen zu berechnen, aber ideal, um eine hergeleitete oder programmierte Ableitung zu prüfen. Dieser Abschnitt zeigt, wie genau die beiden üblichen Quotienten sind, warum eine zu kleine Schrittweite schadet und wie man eine Gradientenprüfung durchführt und bewertet.
:::

### Die Vorwärtsdifferenz

<span class="anker" id="stufe-11-1"></span>

Nach der Definition [(1.3)](die-ableitung.html#gl-1-3) nähert sich der Differenzenquotient der Ableitung, wenn $h$ gegen null geht. Rechnet man ihn mit einem festen kleinen $h$ aus, erhält man eine Näherung, und die Frage ist, wie gut sie ist.

:::definition Definition 11.1 (Vorwärtsdifferenz)
<span class="anker" id="satz-11-1"></span>

Für eine feste Schrittweite $h>0$ heißt

<span class="anker" id="gl-11-1"></span>
$$D_+f(x)=\frac{f(x+h)-f(x)}{h} \tag{11.1}$$

die __Vorwärtsdifferenz__. Ihre Abweichung von $f'(x)$, die allein daher kommt, dass $h$ nicht null ist, heißt __Abschneidefehler__.
:::

Den Abschneidefehler liefert die quadratische Näherung [(1.6)](die-ableitung.html#gl-1-6): Setzt man $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$ ein, so ist

<span class="anker" id="gl-11-2"></span>
$$D_+f(x)\approx f'(x)+\tfrac12f''(x)\,h . \tag{11.2}$$

Der Fehler ist also etwa proportional zu $h$: Zehnmal kleineres $h$ gibt etwa zehnmal kleineren Abschneidefehler.

::::beispiel [Rechenbeispiel]
Für $f(x)=x^3$ an der Stelle $2$ mit $h=10^{-3}$ ist $2{,}001^3=8{,}012006001$ und

$$D_+f(2)=\frac{8{,}012006001-8}{0{,}001}=12{,}006001 .$$

Der Fehler $0{,}006001$ passt zu $\tfrac12f''(2)\,h=\tfrac12\cdot12\cdot0{,}001=0{,}006$; der Rest $0{,}000001=h^2$ ist das nächste Glied.
::::

⁠**Kurz gesagt:** Die Vorwärtsdifferenz hat einen Abschneidefehler von etwa $\tfrac12f''(x)\,h$, proportional zur Schrittweite.

### Die zentrale Differenz

<span class="anker" id="stufe-11-2"></span>

Die Vorwärtsdifferenz misst die Steigung der Sekante zwischen $x$ und $x+h$, und diese Sekante ist bei einer gekrümmten Kurve systematisch steiler oder flacher als die Tangente in $x$. Legt man die Sekante symmetrisch um $x$, von $x-h$ bis $x+h$, so gleicht sich dieser Fehler aus.

:::definition Definition 11.2 (Zentrale Differenz)
<span class="anker" id="satz-11-2"></span>

Für eine feste Schrittweite $h>0$ heißt

<span class="anker" id="gl-11-3"></span>
$$D_0f(x)=\frac{f(x+h)-f(x-h)}{2h} \tag{11.3}$$

die __zentrale Differenz__.
:::

:::satz Satz 11.3 (Abschneidefehler der zentralen Differenz)
<span class="anker" id="satz-11-3"></span>

Hat $f$ eine stetige dritte Ableitung, so ist

<span class="anker" id="gl-11-4"></span>
$$D_0f(x)\approx f'(x)+\tfrac16f'''(x)\,h^2 . \tag{11.4}$$

Der Abschneidefehler ist also etwa proportional zu $h^2$.
:::

:::herleitung Warum sich die Krümmung heraushebt
Man setzt die quadratische Näherung aus Abschnitt [1.5](die-ableitung.html#stufe-1-5) um ein Glied fort. Passt man wie dort bei der Parabel zusätzlich die dritte Ableitung an, so kommt das Glied $\tfrac16f'''(x)\,h^3$ hinzu; der Faktor $\tfrac16$ entsteht, weil die dritte Ableitung von $h^3$ gleich $6$ ist. Damit ist

$$f(x\pm h)\approx f(x)\pm f'(x)\,h+\tfrac12f''(x)\,h^2\pm\tfrac16f'''(x)\,h^3 .$$

Zieht man die beiden Gleichungen voneinander ab, fallen die Glieder mit geraden Potenzen von $h$ heraus, weil sie auf beiden Seiten dasselbe Vorzeichen haben: $f(x)$ und das Krümmungsglied $\tfrac12f''h^2$. Übrig bleibt $f(x+h)-f(x-h)\approx2f'(x)\,h+\tfrac13f'''(x)\,h^3$, und Teilen durch $2h$ ergibt [(11.4)](#gl-11-4). Anschaulich: Die Krümmung macht die rechte Sekante steiler und die linke flacher, und die zentrale Differenz ist der Mittelwert der beiden.
:::

Für eine quadratische Funktion ist $f'''=0$, und die zentrale Differenz ist für jedes $h$ exakt. Sie braucht zwei neue Auswertungen von $f$, die Vorwärtsdifferenz nur eine, wenn $f(x)$ schon bekannt ist.

::::beispiel [Rechenbeispiel]
Für $f(x)=x^3$ an der Stelle $2$ mit $h=10^{-3}$ ist $1{,}999^3=7{,}988005999$ und

$$D_0f(2)=\frac{8{,}012006001-7{,}988005999}{0{,}002}=\frac{0{,}024000002}{0{,}002}=12{,}000001 .$$

Der Fehler ist $0{,}000001=\tfrac16\cdot6\cdot h^2$, sechstausendmal kleiner als bei der Vorwärtsdifferenz.
::::

⁠**Kurz gesagt:** Die zentrale Differenz hat einen Abschneidefehler von etwa $\tfrac16f'''(x)\,h^2$, weil sich das Krümmungsglied heraushebt.

:::::vorwissen Was du dafür brauchst: Gleitkommazahlen

<span class="anker" id="stufe-11-3"></span>

Nach den beiden Formeln für den Abschneidefehler müsste man $h$ nur klein genug wählen. Mit dem Taschenrechner und mit jedem Rechenprogramm geht das schief, und der Grund ist die Art, wie Rechner Zahlen speichern.

Rechner speichern Kommazahlen als __Gleitkommazahlen__: als Zahl mit einer festen Anzahl von Ziffern im Zweiersystem, mal einer Zweierpotenz. Üblich ist die doppelte Genauigkeit nach der Norm IEEE 754 mit $53$ Binärziffern, das sind etwa $16$ Dezimalstellen. Das Ergebnis jeder Rechenoperation wird auf die nächste darstellbare Zahl gerundet. Der relative Fehler dieser Rundung ist höchstens $2^{-53}\approx1{,}1\cdot10^{-16}$. Der Abstand von $1$ zur nächstgrößeren darstellbaren Zahl ist doppelt so groß,

$$\varepsilon_{\mathrm M}=2^{-52}\approx2{,}2\cdot10^{-16};$$

diese Zahl heißt __Maschinengenauigkeit__, und Rechenprogramme geben sie unter diesem Namen aus. In einfacher Genauigkeit mit $24$ Binärziffern, etwa $7$ Dezimalstellen, ist $\varepsilon_{\mathrm M}=2^{-23}\approx1{,}2\cdot10^{-7}$.

Gefährlich wird die Rundung beim Abziehen fast gleicher Zahlen. Die vorderen Ziffern heben sich auf, die Rundungsfehler der hinteren bleiben, und vom Ergebnis sind nur noch wenige Ziffern richtig. Das heißt __Auslöschung__. Ein Differenzenquotient zieht genau solche Zahlen voneinander ab, und je kleiner $h$ ist, desto ähnlicher sind sie sich.

::::beispiel [Rechenbeispiel]
Für $f(x)=x^3$ an der Stelle $2$ und $h=10^{-8}$ ist $f(2+h)=8{,}00000012\ldots$ Beide Funktionswerte sind etwa $8$ und tragen je einen Rundungsfehler bis etwa $8\cdot1{,}1\cdot10^{-16}\approx9\cdot10^{-16}$. Ihre Differenz ist etwa $1{,}2\cdot10^{-7}$; ein Fehler von $10^{-15}$ darin ist ein relativer Fehler von fast $10^{-8}$. Von den $16$ Stellen sind nach dem Abziehen also nur noch etwa $8$ richtig, und die Division durch $h$ ändert daran nichts.
::::

⁠**Kurz gesagt:** Rechner runden jedes Ergebnis auf etwa $16$ Stellen, $\varepsilon_{\mathrm M}=2^{-52}$; beim Abziehen fast gleicher Zahlen bleiben davon nur wenige richtige Stellen übrig.

:::::

### Die Fehlerkurve

<span class="anker" id="stufe-11-4"></span>

Bei einem Differenzenquotienten wirken also zwei Fehler gegeneinander. Der Abschneidefehler wird mit kleinerem $h$ kleiner. Der Rundungsfehler wird mit kleinerem $h$ größer: Der Fehler der Differenz im Zähler bleibt etwa gleich, er wird aber durch ein immer kleineres $h$ geteilt.

:::satz Satz 11.4 (Gesamtfehler der Differenzenquotienten)
<span class="anker" id="satz-11-4"></span>

Sind die Funktionswerte bis auf einen relativen Fehler von höchstens $\tfrac12\varepsilon_{\mathrm M}$ genau, so ist der Gesamtfehler ungefähr höchstens

<span class="anker" id="gl-11-5"></span>
$$E_+(h)=\tfrac12|f''(x)|\,h+\frac{\varepsilon_{\mathrm M}|f(x)|}{h}\qquad\text{bzw.}\qquad E_0(h)=\tfrac16|f'''(x)|\,h^2+\frac{\varepsilon_{\mathrm M}|f(x)|}{2h} \tag{11.5}$$

für die Vorwärts- bzw. die zentrale Differenz. Am kleinsten wird $E_+$ bei $h_+=\sqrt{2\varepsilon_{\mathrm M}|f|/|f''|}$, mit dem Wert $\sqrt{2\varepsilon_{\mathrm M}|f|\,|f''|}$; am kleinsten wird $E_0$ bei $h_0=\bigl(\tfrac32\varepsilon_{\mathrm M}|f|/|f'''|\bigr)^{1/3}$.
:::

:::herleitung Die beste Schrittweite
Im Zähler stehen zwei Funktionswerte, jeder mit einem Rundungsfehler bis $\tfrac12\varepsilon_{\mathrm M}|f|$, zusammen bis $\varepsilon_{\mathrm M}|f|$. Bei der Vorwärtsdifferenz wird das durch $h$ geteilt, bei der zentralen durch $2h$. Dazu kommen die Abschneidefehler [(11.2)](#gl-11-2) und [(11.4)](#gl-11-4). Eine Funktion der Form $a\,h+b/h$ mit $a,b>0$ hat die Ableitung $a-b/h^2$, die bei $h=\sqrt{b/a}$ null wird; dort ist der Wert $2\sqrt{ab}$. Mit $a=\tfrac12|f''|$ und $b=\varepsilon_{\mathrm M}|f|$ ergibt das $h_+$. Für $a\,h^2+b/h$ ist die Ableitung $2ah-b/h^2$, die bei $h^3=b/(2a)$ null wird; mit $a=\tfrac16|f'''|$ und $b=\tfrac12\varepsilon_{\mathrm M}|f|$ ergibt das $h_0$.
:::

Trägt man den Fehler gegen $h$ doppelt logarithmisch auf, so entsteht ein V (Abb. [20](#abb-20)). Rechts steigt die Kurve mit der Steigung $1$ (vorwärts) bzw. $2$ (zentral), weil dort der Abschneidefehler herrscht. Links fällt sie mit der Steigung $-1$, weil dort der Rundungsfehler herrscht. Die gemessenen Punkte links streuen, denn Rundungsfehler fallen je nach Zahl größer oder kleiner aus; [(11.5)](#gl-11-5) gibt nur ihre Größenordnung an. Als Faustregel wählt man vorwärts $h\approx\sqrt{\varepsilon_{\mathrm M}}\approx10^{-8}$ und zentral $h\approx\varepsilon_{\mathrm M}^{1/3}\approx6\cdot10^{-6}$, jeweils mal der Größenordnung von $x$, wenn $|x|$ größer als $1$ ist.

:::abbildung ml/k3vkurve 20
Der Fehler der beiden Differenzenquotienten für $f(x)=x^3$ an der Stelle $2$, in doppelter Genauigkeit gerechnet, gegen die Schrittweite $h$ von $10^{-15}$ bis $10^{-1}$, beide Achsen logarithmisch. Rechts herrscht der Abschneidefehler (Steigung $1$ bzw. $2$), links der Rundungsfehler (Steigung $-1$). Die gestrichelten Kurven sind die Abschätzungen [(11.5)](#gl-11-5); die tiefsten Punkte liegen bei $h\approx10^{-8}$ (vorwärts) und $h\approx3\cdot10^{-6}$ (zentral).
:::

::::beispiel [Rechenbeispiel]
Für $f(x)=x^3$ an der Stelle $2$ ist $|f|=8$, $|f''|=12$ und $|f'''|=6$. Die beste Schrittweite der Vorwärtsdifferenz ist $h_+=\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8/12}\approx1{,}7\cdot10^{-8}$ mit einem Fehler von etwa $\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8\cdot12}\approx2{,}1\cdot10^{-7}$; bezogen auf $f'(2)=12$ sind das etwa acht richtige Stellen. Die beste Schrittweite der zentralen Differenz ist $h_0=(1{,}5\cdot2{,}2\cdot10^{-16}\cdot8/6)^{1/3}\approx7{,}6\cdot10^{-6}$ mit einem Fehler von etwa $(7{,}6\cdot10^{-6})^2+2{,}2\cdot10^{-16}\cdot8/(2\cdot7{,}6\cdot10^{-6})\approx1{,}7\cdot10^{-10}$, etwa elf richtige Stellen. Abb. [20](#abb-20) bestätigt beides: Gemessen wurden $7{,}3\cdot10^{-8}$ bei $h=10^{-8}$ und $2{,}0\cdot10^{-11}$ bei $h\approx3{,}2\cdot10^{-6}$. Mit $h=10^{-14}$ dagegen ist bei beiden Quotienten schon die erste Nachkommastelle falsch.
::::

⁠**Kurz gesagt:** Zu großes $h$ gibt Abschneidefehler, zu kleines gibt Rundungsfehler; am besten ist vorwärts $h\approx10^{-8}$, zentral $h\approx10^{-5}$ bis $10^{-6}$, und die zentrale Differenz erreicht dabei etwa elf statt acht richtige Stellen.

### Die Gradientenprüfung

<span class="anker" id="stufe-11-5"></span>

Wer einen Gradienten von Hand herleitet oder als Rückwärtsschritte programmiert, macht leicht Fehler: ein vergessener Weg, ein fehlendes Transponieren, ein falscher Faktor. Ein Differenzenquotient braucht keine Herleitung, er wertet nur die Funktion aus. Vergleicht man beide, findet man solche Fehler zuverlässig.

:::definition Definition 11.5 (Gradientenprüfung)
<span class="anker" id="satz-11-5"></span>

Bei der __Gradientenprüfung__ vergleicht man einen berechneten Gradienten $\mathbf{g}_{\mathrm a}$ an einer Stelle $\mathbf{x}$ mit dem numerischen Gradienten $\mathbf{g}_{\mathrm n}$, dessen Komponenten zentrale Differenzen sind,

<span class="anker" id="gl-11-6"></span>
$$g_{\mathrm n,j}=\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x}-h\,\mathbf{e}_j)}{2h}. \tag{11.6}$$

Für jede Komponente berechnet man dabei den __relativen Fehler__

<span class="anker" id="gl-11-7"></span>
$$\rho_j=\frac{|g_{\mathrm a,j}-g_{\mathrm n,j}|}{\max\bigl(|g_{\mathrm a,j}|,\,|g_{\mathrm n,j}|\bigr)}, \tag{11.7}$$

wobei man $\rho_j=0$ setzt, wenn beide Werte null sind.
:::

Man vergleicht relativ, weil ein absoluter Fehler von $10^{-6}$ bei einer Ableitung von $10^{6}$ hervorragend, bei einer Ableitung von $10^{-6}$ aber ein vollständiger Fehlschlag ist. Bei Rechnung in doppelter Genauigkeit und $h$ in der Größenordnung $10^{-5}$ gelten diese Erfahrungswerte: Ein relativer Fehler über $10^{-2}$ bedeutet fast sicher einen Fehler in der Formel. Zwischen $10^{-2}$ und $10^{-4}$ ist das Ergebnis verdächtig. Unter $10^{-4}$ ist es bei Funktionen mit Knicken meist in Ordnung, und $10^{-7}$ oder weniger ist ein gutes Ergebnis. Eine Prüfung kostet $2n$ Auswertungen von $f$; man prüft deshalb nur an wenigen Stellen oder nur einige Komponenten. Für die eigentliche Rechnung ist der Rückwärtsmodus da, für ihre Kontrolle der Differenzenquotient.

::::beispiel [Rechenbeispiel 1]
Für $f(\mathbf{x})=x_1^2x_2+x_2^2$ habe jemand den Gradienten $(2x_1x_2,\ x_1^2+x_2)^{\top}$ hergeleitet, mit einem vergessenen Faktor $2$. An der Stelle $(1,\,2)$ ist das $\mathbf{g}_{\mathrm a}=(4,\,3)^{\top}$. Mit $h=0{,}001$ ist

$$\begin{aligned} g_{\mathrm n,1}&=\frac{f(1{,}001;\ 2)-f(0{,}999;\ 2)}{0{,}002}=\frac{6{,}004002-5{,}996002}{0{,}002}=4,\\ g_{\mathrm n,2}&=\frac{f(1;\ 2{,}001)-f(1;\ 1{,}999)}{0{,}002}=\frac{6{,}005001-5{,}995001}{0{,}002}=5 . \end{aligned}$$

Die zentralen Differenzen sind hier exakt, weil $f$ in jeder einzelnen Variablen höchstens quadratisch ist. Die relativen Fehler sind $\rho_1=0$ und $\rho_2=|3-5|/5=0{,}4$: Die zweite Komponente ist falsch.
::::

::::beispiel [Rechenbeispiel 2]
Geprüft wird die Formel $\sigma'(x)=\sigma(x)(1-\sigma(x))$ an der Stelle $1$. Mit zehn Stellen ist $\sigma(1)\approx0{,}7310585786$, und die Formel ergibt $0{,}7310585786\cdot0{,}2689414214\approx0{,}1966119332$. Mit $h=0{,}01$ ist $\sigma(1{,}01)\approx0{,}7330201492$ und $\sigma(0{,}99)\approx0{,}7290879223$, also

$$g_{\mathrm n}=\frac{0{,}7330201492-0{,}7290879223}{0{,}02}=\frac{0{,}0039322269}{0{,}02}\approx0{,}196611345 .$$

Der relative Fehler ist $\rho\approx5{,}9\cdot10^{-7}/0{,}1966\approx3{,}0\cdot10^{-6}$. Er stammt vom Abschneidefehler der verhältnismäßig großen Schrittweite und ist weit unter der Schwelle $10^{-2}$; die Formel ist richtig. In doppelter Genauigkeit mit $h=10^{-5}$ sinkt er auf etwa $10^{-11}$.
::::

⁠**Kurz gesagt:** Die Gradientenprüfung vergleicht einen berechneten Gradienten komponentenweise mit zentralen Differenzen; relative Fehler über $10^{-2}$ zeigen einen Fehler in der Formel, solche unter $10^{-7}$ eine richtige Formel.

### Knicke und andere Fallstricke

<span class="anker" id="stufe-11-6"></span>

Eine Gradientenprüfung kann Alarm schlagen, obwohl die Formel stimmt, oder schweigen, obwohl sie falsch ist. Die häufigsten Ursachen lassen sich vorhersehen.

Die erste Ursache sind Knicke. An einem Knick, wie bei $|x|$ oder $\max(x,\,0)$ an der Stelle $0$, gibt es keine Ableitung. Liegt ein Knick zwischen $x-h$ und $x+h$, so misst die zentrale Differenz eine Mischung der beiden Steigungen links und rechts, während die berechnete Ableitung nur eine davon kennt. Die zweite Ursache ist zu geringe Genauigkeit. In einfacher Genauigkeit ist $\varepsilon_{\mathrm M}\approx1{,}2\cdot10^{-7}$; nach [(11.5)](#gl-11-5) liegt die beste Schrittweite der zentralen Differenz dann bei etwa $10^{-2}$, und relative Fehler um $10^{-5}$ bis $10^{-3}$ sind auch bei richtiger Formel normal. Die dritte ist eine zu kleine Schrittweite, die den Rundungsfehler in die Höhe treibt. Die vierte sind sehr kleine Gradienten: Sind beide Werte fast null, ist der relative Fehler wenig aussagekräftig, und man betrachtet zusätzlich den absoluten Fehler. Schließlich sollte man an einer zufälligen Stelle prüfen, nicht an einer besonderen: An der Stelle $\mathbf{x}=\mathbf{0}$ verschwinden viele Glieder einer Formel, und mit ihnen die Fehler, die in diesen Gliedern stecken.

:::warnung Geprüft ist nur, was man prüft
Eine bestandene Gradientenprüfung an einer Stelle zeigt, dass die Formel dort stimmt, nicht überall. Ein vergessenes Glied, das an der geprüften Stelle null ist, fällt nicht auf. Prüfe deshalb an mehreren Stellen mit unregelmäßigen Zahlen und alle Komponenten, die verschieden berechnet werden.
:::

::::beispiel [Rechenbeispiel]
Für $f(x)=|x|$ an der Stelle $x=10^{-6}$ ist die Ableitung $1$. Mit $h=10^{-5}$ liegt der Knick bei $0$ zwischen $x-h$ und $x+h$, und

$$D_0f(10^{-6})=\frac{|1{,}1\cdot10^{-5}|-|-0{,}9\cdot10^{-5}|}{2\cdot10^{-5}}=\frac{0{,}2\cdot10^{-5}}{2\cdot10^{-5}}=0{,}1 .$$

Der relative Fehler ist $0{,}9$, obwohl die Formel $f'(x)=1$ für $x>0$ richtig ist. Mit $h=10^{-7}$ liegt der Knick außerhalb, und die zentrale Differenz ist exakt $1$.
::::

⁠**Kurz gesagt:** Knicke, einfache Genauigkeit, zu kleine Schrittweiten und Gradienten nahe null verfälschen die Prüfung; man prüft an mehreren unregelmäßigen Stellen.

:::aufgabe Aufgabe 39 ★ Zwei Differenzenquotienten
<span class="anker" id="aufg-39"></span>

Es sei $f(x)=\mathrm{e}^x$ und $x=0$, also $f'(0)=1$.

<ol class="al">

<li>

Berechne mit dem Taschenrechner $D_+f(0)$ und $D_0f(0)$ für $h=0{,}1$ und $h=0{,}01$.

</li>

<li>

Vergleiche die Fehler mit den Näherungen $\tfrac12f''(0)\,h$ und $\tfrac16f'''(0)\,h^2$.

</li>

</ol>

:::loesung
(a) Mit $\mathrm{e}^{0{,}1}\approx1{,}105170918$, $\mathrm{e}^{-0{,}1}\approx0{,}904837418$, $\mathrm{e}^{0{,}01}\approx1{,}010050167$ und $\mathrm{e}^{-0{,}01}\approx0{,}990049834$:

$$\begin{aligned} h=0{,}1:&\quad D_+=\frac{1{,}105170918-1}{0{,}1}\approx1{,}05171,\\ &\quad D_0=\frac{1{,}105170918-0{,}904837418}{0{,}2}\approx1{,}001668;\\ h=0{,}01:&\quad D_+=\frac{1{,}010050167-1}{0{,}01}\approx1{,}005017,\\ &\quad D_0=\frac{1{,}010050167-0{,}990049834}{0{,}02}\approx1{,}0000167 . \end{aligned}$$

(b) Die Fehler der Vorwärtsdifferenz sind $0{,}0517$ und $0{,}0050$, die Näherung $\tfrac12h$ sagt $0{,}05$ und $0{,}005$ voraus. Die Fehler der zentralen Differenz sind $0{,}00167$ und $0{,}0000167$, die Näherung $\tfrac16h^2$ sagt $0{,}00167$ und $0{,}0000167$ voraus. Zehnmal kleineres $h$ macht den einen Fehler zehnmal, den anderen hundertmal kleiner.
:::
:::

:::aufgabe Aufgabe 40 ★★ Eine Gradientenprüfung
<span class="anker" id="aufg-40"></span>

Für $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ behauptet jemand $\nabla f(\mathbf{x})=(\mathrm{e}^{x_2},\ \mathrm{e}^{x_2})^{\top}$.

<ol class="al">

<li>

Berechne an der Stelle $(2,\,0)$ den numerischen Gradienten mit $h=0{,}01$ und die relativen Fehler beider Komponenten. Welche Komponente ist falsch?

</li>

<li>

Warum wäre die Prüfung an der Stelle $(1,\,0)$ ungeeignet gewesen?

</li>

</ol>

:::loesung
(a) Nach $x_1$: $\frac{f(2{,}01;\,0)-f(1{,}99;\,0)}{0{,}02}=\frac{2{,}01-1{,}99}{0{,}02}=1$, die Behauptung sagt $\mathrm{e}^0=1$, also $\rho_1=0$. Nach $x_2$:

$$g_{\mathrm n,2}=\frac{2\,\mathrm{e}^{0{,}01}-2\,\mathrm{e}^{-0{,}01}}{0{,}02}\approx\frac{2{,}0201003-1{,}9800997}{0{,}02}\approx2{,}0000333 .$$

Die Behauptung sagt $1$, also $\rho_2=|1-2{,}0000333|/2{,}0000333\approx0{,}5$. Die zweite Komponente ist falsch; richtig ist $x_1\mathrm{e}^{x_2}=2$.

(b) An der Stelle $(1,\,0)$ ist $x_1\mathrm{e}^{x_2}=1=\mathrm{e}^{x_2}$: Die falsche Formel stimmt dort zufällig mit der richtigen überein, und die Prüfung hätte nur einen relativen Fehler von etwa $2\cdot10^{-5}$ ergeben, verursacht vom Abschneidefehler. Der Fehler wäre unentdeckt geblieben.
:::
:::

:::aufgabe Aufgabe 41 ★★ Die beste Schrittweite
<span class="anker" id="aufg-41"></span>

Es sei $f(x)=\mathrm{e}^x$ an der Stelle $1$, also $f=f''=f'''=\mathrm{e}$.

<ol class="al">

<li>

Berechne $h_+$, $h_0$ und die zugehörigen kleinsten Fehler nach [(11.5)](#gl-11-5) für doppelte Genauigkeit.

</li>

<li>

Wiederhole die Rechnung für einfache Genauigkeit. Wie viele richtige Stellen kann man dann höchstens erwarten?

</li>

</ol>

:::loesung
(a) Mit $|f|=|f''|=|f'''|=\mathrm{e}$ und $\varepsilon_{\mathrm M}\approx2{,}22\cdot10^{-16}$:

$$\begin{aligned} h_+&=\sqrt{2\varepsilon_{\mathrm M}}\approx2{,}1\cdot10^{-8}, & E_+(h_+)&=\mathrm{e}\sqrt{2\varepsilon_{\mathrm M}}\approx5{,}7\cdot10^{-8},\\ h_0&=(1{,}5\,\varepsilon_{\mathrm M})^{1/3}\approx6{,}9\cdot10^{-6}, & E_0(h_0)&=\tfrac{\mathrm{e}}6h_0^2+\frac{\varepsilon_{\mathrm M}\mathrm{e}}{2h_0}\approx6{,}5\cdot10^{-11}. \end{aligned}$$

Bezogen auf $f'(1)=\mathrm{e}$ sind das relative Fehler von etwa $2\cdot10^{-8}$ und $2\cdot10^{-11}$, also knapp acht und knapp elf richtige Stellen.

(b) Mit $\varepsilon_{\mathrm M}\approx1{,}19\cdot10^{-7}$ ist $h_+\approx4{,}9\cdot10^{-4}$ mit $E_+\approx1{,}3\cdot10^{-3}$ und $h_0\approx5{,}6\cdot10^{-3}$ mit $E_0\approx4{,}3\cdot10^{-5}$. Relativ zu $\mathrm{e}$ sind das etwa $5\cdot10^{-4}$ und $1{,}6\cdot10^{-5}$: Man kann höchstens etwa drei bzw. fünf richtige Stellen erwarten. Eine Gradientenprüfung in einfacher Genauigkeit liefert deshalb auch bei richtiger Formel relative Fehler um $10^{-5}$ bis $10^{-3}$.
:::
:::

:::aufgabe Aufgabe 42 ★★★ Knick im Graphen
<span class="anker" id="aufg-42"></span>

Es sei $f(\mathbf{x})=\max(x_1,\,x_2)\cdot x_3$.

<ol class="al">

<li>

Berechne im Rückwärtsmodus den Gradienten an der Stelle $(2;\ 2{,}000001;\ 3)$.

</li>

<li>

Berechne die zentrale Differenz nach $x_1$ mit $h=10^{-5}$ und den relativen Fehler. Ist die Formel falsch?

</li>

<li>

Was liefert der Rückwärtsmodus an der Stelle $(2,\,2,\,3)$, und warum gibt es dort keinen Gradienten?

</li>

</ol>

:::loesung
(a) An der Stelle $(2;\ 2{,}000001;\ 3)$ ist $v=\max(x_1,x_2)=x_2=2{,}000001$ und $f=6{,}000003$. Rückwärts: $\bar f=1$, $\bar v=x_3=3$, $\bar x_3=v=2{,}000001$; das Maximum gibt $\bar v$ an den größeren Eingang $x_2$, also $\bar x_2=3$ und $\bar x_1=0$. Der Gradient ist $(0;\ 3;\ 2{,}000001)^{\top}$.

(b) $f(2{,}00001;\ 2{,}000001;\ 3)=3\cdot2{,}00001=6{,}00003$ und $f(1{,}99999;\ 2{,}000001;\ 3)=3\cdot2{,}000001=6{,}000003$, also

$$g_{\mathrm n,1}=\frac{6{,}00003-6{,}000003}{0{,}00002}=\frac{0{,}000027}{0{,}00002}=1{,}35$$

und $\rho_1=|0-1{,}35|/1{,}35=1$. Die Formel ist trotzdem richtig. Der Knick bei $x_1=x_2$ liegt zwischen $x_1-h$ und $x_1+h$: Rechts davon steigt $f$ mit der Steigung $3$ in $x_1$, links davon gar nicht, und die zentrale Differenz mischt beides.

(c) An der Stelle $(2,\,2,\,3)$ sind beide Eingänge des Maximums gleich. Der Rückwärtsmodus gibt $\bar v=3$ an einen der beiden, je nachdem, welchen die Rechnung bei Gleichstand als größer behandelt; er liefert also $(3,\,0,\,2)^{\top}$ oder $(0,\,3,\,2)^{\top}$. Einen Gradienten gibt es dort nicht: Vergrößert man $x_1$, steigt $f$ mit der Steigung $3$; verkleinert man $x_1$, bleibt $f$ gleich. Die einseitigen Steigungen sind verschieden, wie bei $|x|$ an der Stelle $0$.
:::
:::
