---
title: Stufe 2: Vier Größen, zwei Gleichungen, vier Zahlen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1160400
summary: Vier Torgrößen sind vier Unbekannte.
tags: Zweitorfunktionen, symmetrischen Zählpfeilsystem, Kettenpfeilsystem, gemischte Pfeilsystem
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Vier Torgrößen sind vier Unbekannte. Diese Stufe zeigt, warum das Zweitor genau zwei Gleichungen beiträgt und warum darin nur vier Zahlen stecken.
:::

**Die Idee.** Quelle und Last liefern je eine Gleichung zwischen Spannung und Strom ihres Tors. Es fehlen zwei, und die liefert das Zweitor. Gibt man zwei Torgrößen vor, etwa beide Ströme, liegen alle Ströme und Spannungen im Inneren fest, also auch die beiden übrigen Torgrößen. Die vorgegebenen Größen sind die Ursachen, die anderen die Wirkungen. Ist das Zweitor linear und enthält keine unabhängigen Quellen, gilt die Überlagerung aus [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): Jede Wirkung ist die Summe aus dem Anteil der ersten und dem Anteil der zweiten Ursache, jeder Anteil proportional zu seiner Ursache. Zwei Wirkungen mal zwei Ursachen ergeben vier Faktoren.

:::satz Satz 2.1 (Zweitorgleichungen)
<span class="anker" id="satz-2-1"></span>

Ein zeitunabhängiges Zweitor wird durch zwei __Zweitorfunktionen__ vollständig beschrieben, zum Beispiel

<span class="anker" id="gl-2-1"></span>
$$I_1=f_1(U_1,U_2),\quad I_2=g_1(U_1,U_2)\qquad\text{oder}\qquad U_1=f_2(I_1,I_2),\quad U_2=g_2(I_1,I_2). \tag{2.1}$$

Ist es linear und frei von unabhängigen Quellen, gilt für Wirkungen $y_1,y_2$ und Ursachen $x_1,x_2$

<span class="anker" id="gl-2-2"></span>
$$y_1=p_{11}x_1+p_{12}x_2,\qquad y_2=p_{21}x_1+p_{22}x_2. \tag{2.2}$$
:::

⁠**So liest man das:** Die erste Ziffer eines Parameters nennt die Wirkung, die zweite die Ursache. Die Parameter hängen nur vom Zweitor ab, nicht von Quelle oder Last. Vier Größen lassen sich auf sechs Arten in zwei Ursachen und zwei Wirkungen teilen. Gebräuchlich sind die vier Formen dieses Kapitels. **Gültigkeit:** [(2.1)](#gl-2-1) gilt auch für nichtlineare Zweitore, dann als Kurven. Beim Transistor beschreibt man so entweder das Verhalten für Gleichgrößen oder das Signalverhalten für kleine Wechselgrößen. Ein Transformator mit getrennten Wicklungen überträgt nur zeitveränderliche Größen. [(2.2)](#gl-2-2) verlangt Linearität.

**Zählpfeile.** Damit die Vorzeichen eindeutig sind, braucht man eine Vereinbarung (Abb. [3](#abb-3)). Im __symmetrischen Zählpfeilsystem__, auch mathematische Vorzeichenrichtung genannt, gilt an beiden Toren das Verbraucherzählpfeilsystem aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): Die Strompfeile zeigen in das Zweitor hinein. Im __Kettenpfeilsystem__, auch technisches Pfeilsystem genannt, gilt es nur am Eingang, am Ausgang gilt das Erzeugerzählpfeilsystem: Der Ausgangsstrom zeigt heraus, zur Last. Dieses Kapitel benutzt das __gemischte Pfeilsystem__: $I_1$ und $I_2$ zeigen immer hinein. Wo die Kettenform den herausfließenden Strom braucht, schreibt sie ihn ausdrücklich als $-I_2$. Eine Last ergibt deshalb im Normalbetrieb ein negatives $I_2$.

:::abbildung et1/k6zaehlpfeile 3
Die drei Pfeilsysteme. Links symmetrisch: Beide Ströme zeigen in das Zweitor. Mitte Kettenpfeil: Der Ausgangsstrom zeigt zur Last. Rechts gemischt, wie in diesem Kapitel: $I_2$ bleibt definiert wie links, der Strom zur Last heißt $-I_2$.
:::

::::beispiel
Am Mittelpunkt des T-Zweitors treffen sich $I_1$ und $I_2$, durch $R_\mathrm{b}$ fließt ihre Summe. Die Maschenregel ergibt

$$U_1=R_\mathrm{a}I_1+R_\mathrm{b}(I_1+I_2)=35\,\Omega\cdot I_1+20\,\Omega\cdot I_2,\qquad U_2=R_\mathrm{c}I_2+R_\mathrm{b}(I_1+I_2)=20\,\Omega\cdot I_1+40\,\Omega\cdot I_2.$$

Der Summand $20\,\Omega\cdot I_2$ in $U_1$ ist der Mechanismus: Der Strom von Tor 2 läuft durch $R_\mathrm{b}$, hebt dort das Potenzial des Mittelpunkts, und Tor 1 sieht diese Anhebung. Mit $I_1=250$ mA und $I_2=-50$ mA folgt $U_1=8{,}75\,\mathrm{V}-1\,\mathrm{V}=7{,}75$ V und $U_2=5\,\mathrm{V}-2\,\mathrm{V}=3$ V.
::::

⁠**Grenzfall:** Ohne Ursachen, $I_1=I_2=0$, sind beide Spannungen null, wie es ein Zweitor ohne eigene Quellen verlangt. Mit einer unabhängigen Quelle im Inneren käme in jeder Gleichung eine Konstante hinzu.

⁠**Kurz gesagt:** Zwei Größen sind frei, und jede der beiden anderen ist eine Summe mit zwei festen Faktoren.

:::frage Wer entscheidet, welche zwei Größen die Ursachen sind, das Netzwerk?
Nein, das ist die Rechnung. Physikalisch stellt sich alles gleichzeitig ein. Die Gleichungen beschreiben einen Zusammenhang zwischen vier Größen, und man darf ihn nach zwei beliebigen auflösen, sofern diese wirklich frei wählbar sind. „Ursache“ heißt hier: Das steht rechts vom Gleichheitszeichen.
:::

:::aufgabe Aufgabe 2 ★ Eine Blackbox vorhersagen
<span class="anker" id="aufg-2"></span>

Ein unbekanntes lineares Zweitor ohne eigene Quellen ergibt zwei Messungen. Mit $I_1=200$ mA, $I_2=0$ ist $U_1=8$ V, $U_2=3$ V. Mit $I_1=0$, $I_2=100$ mA ist $U_1=1{,}5$ V, $U_2=3$ V.

<ol class="al">

<li>

Sage ohne weitere Messung $U_1$ und $U_2$ für $I_1=100$ mA, $I_2=200$ mA voraus.

</li>

<li>

Was ergibt sich für $I_1=100$ mA, $I_2=-50$ mA? Was fällt an $U_2$ auf?

</li>

</ol>

:::loesung
Die Messungen ergeben $Z_{11}=8\,\mathrm{V}/200\,\mathrm{mA}=40\,\Omega$, $Z_{21}=15\,\Omega$, $Z_{12}=1{,}5\,\mathrm{V}/100\,\mathrm{mA}=15\,\Omega$, $Z_{22}=30\,\Omega$. (a) $U_1=40\,\Omega\cdot0{,}1\,\mathrm{A}+15\,\Omega\cdot0{,}2\,\mathrm{A}=7$ V, $U_2=15\,\Omega\cdot0{,}1\,\mathrm{A}+30\,\Omega\cdot0{,}2\,\mathrm{A}=7{,}5$ V. (b) $U_1=4\,\mathrm{V}-0{,}75\,\mathrm{V}=3{,}25$ V, $U_2=1{,}5\,\mathrm{V}-1{,}5\,\mathrm{V}=0$. Dieses Strompaar gehört also zu einem kurzgeschlossenen Tor 2.
:::
:::

::::formelsammlung
**Zweitorfunktionen**

$$I_1=f_1(U_1,U_2),\quad I_2=g_1(U_1,U_2)\qquad\text{oder}\qquad U_1=f_2(I_1,I_2),\quad U_2=g_2(I_1,I_2)$$

Zwei Funktionen beschreiben ein zeitunabhängiges Zweitor vollständig. Sie gelten auch für nichtlineare Zweitore, dann als Kurven.

**Lineares Zweitor ohne unabhängige Quellen**

$$y_1=p_{11}x_1+p_{12}x_2,\qquad y_2=p_{21}x_1+p_{22}x_2$$

Wirkungen $y_1,y_2$, Ursachen $x_1,x_2$ (zwei frei wählbare Torgrößen). Erste Ziffer des Parameters: Wirkung, zweite: Ursache. Die vier Parameter hängen nur vom Zweitor ab, nicht von Quelle oder Last. Verlangt Linearität; eine unabhängige Quelle im Inneren brächte in jede Gleichung eine Konstante.
::::

::::lernkarten
:::karte zusammenhang Zwei Gleichungen vom Zweitor
Warum muss das Zweitor selbst genau zwei Gleichungen beitragen, wenn an seinen Toren Quelle und Last hängen?
---
Vier Torgrößen sind vier Unbekannte; Quelle und Last liefern je eine Gleichung, also fehlen zwei. Gibt man zwei Torgrößen vor, liegen alle Ströme und Spannungen im Inneren fest, also auch die beiden übrigen.
--- falsch
Weil jedes Tor eine eigene Gleichung liefert, die nur Strom und Spannung dieses Tors verbindet. Zwei vorgegebene Größen legen die anderen fest, weil sich die beiden Tore gegenseitig nicht beeinflussen.
--- falsch
Weil Knotenregel und Maschenregel für das ganze Netzwerk zusammen genau zwei Gleichungen ergeben. Zwei vorgegebene Größen genügen, weil die Torbedingung die anderen zwei festlegt.
--- falsch
Weil die vier Torgrößen paarweise gleich sind, $U_1=U_2$ und $I_1=-I_2$. Gibt man zwei Größen vor, kennt man deshalb auch die beiden anderen ohne jede weitere Rechnung.
:::
:::karte begriff Zweitorfunktionen
Was sind Zweitorfunktionen, und gelten sie auch für nichtlineare Zweitore?
---
Zwei Funktionen, die ein zeitunabhängiges Zweitor vollständig beschreiben, zum Beispiel $I_1=f_1(U_1,U_2)$ und $I_2=g_1(U_1,U_2)$. Sie gelten auch für nichtlineare Zweitore, dann als Kurven.
--- falsch
Vier Funktionen, je eine für jede Torgröße, zum Beispiel $U_1=f(I_1)$. Sie gelten nur für lineare Zweitore, weil sich gekrümmte Kurven nicht als Funktionen schreiben lassen.
--- falsch
Zwei Funktionen, die ein Zweitor beschreiben, zum Beispiel $I_1=f_1(U_1,U_2)$ und $I_2=g_1(U_1,U_2)$. Sie gelten nur für lineare Zweitore ohne eigene Quellen.
--- falsch
Die Funktionen, die angeben, wie sich die Torgrößen mit der Zeit ändern. Ein zeitunabhängiges Zweitor hat deshalb keine Zweitorfunktionen, sondern nur feste Werte.
:::
:::karte formel Lineares Zweitor
Wie hängen bei einem linearen Zweitor ohne unabhängige Quellen die Wirkungen $y_1,y_2$ von den Ursachen $x_1,x_2$ ab, und was bedeuten die Ziffern der Parameter?
---
$y_1=p_{11}x_1+p_{12}x_2$, $y_2=p_{21}x_1+p_{22}x_2$. Die erste Ziffer eines Parameters nennt die Wirkung, die zweite die Ursache. Die Parameter hängen nur vom Zweitor ab, nicht von Quelle oder Last.
--- falsch
$y_1=p_{11}x_1+p_{12}x_2$, $y_2=p_{21}x_1+p_{22}x_2$. Die erste Ziffer eines Parameters nennt die Ursache, die zweite die Wirkung. Die Parameter hängen auch von Quelle und Last ab.
--- falsch
$y_1=p_{11}x_1$, $y_2=p_{22}x_2$. Jede Wirkung hängt nur von ihrer eigenen Ursache ab, deshalb nennen beide Ziffern dieselbe Größe. Die Parameter hängen nur vom Zweitor ab, nicht von Quelle oder Last.
--- falsch
$y_1=p_{11}x_1+p_{12}x_2$, $y_2=p_{21}x_1+p_{22}x_2$. Das gilt auch mit unabhängigen Quellen im Inneren, weil deren Werte einfach in die vier Parameter eingehen und sie verschieben.
:::
:::karte begriff Zweitorparameter
Was sind die Zweitorparameter eines linearen Zweitors ohne eigene Quellen, und warum sind es genau vier?
---
Die festen Faktoren, mit denen jede Wirkung als Summe der Anteile beider Ursachen entsteht. Jeder Anteil ist proportional zu seiner Ursache; zwei Wirkungen mal zwei Ursachen ergeben vier Faktoren.
--- falsch
Die vier Torgrößen $U_1$, $I_1$, $U_2$, $I_2$, die man an den Toren misst. Es sind genau vier, weil ein Zweitor vier Klemmen hat und jede Klemme genau eine Größe beiträgt.
--- falsch
Die Werte der vier Bauteile, aus denen jedes lineare Zweitor besteht. Ein Zweitor mit mehr Bauteilen fasst man vorher so lange zusammen, bis genau vier übrig bleiben.
--- falsch
Die Faktoren, mit denen jede Wirkung aus beiden Ursachen entsteht. Sie hängen von Quelle und Last ab und müssen deshalb für jeden Betriebszustand neu bestimmt werden, sobald sich die Last ändert.
:::
:::karte zusammenhang Ursachen und Wirkungen
Wer legt fest, welche zwei der vier Torgrößen Ursachen und welche Wirkungen sind?
---
Die Rechnung, nicht das Netzwerk. Physikalisch stellt sich alles gleichzeitig ein; man darf nach zwei beliebigen Größen auflösen, sofern sie frei wählbar sind. Ursache heißt: Das steht rechts vom Gleichheitszeichen.
--- falsch
Das Netzwerk: Die Größen am Eingang sind immer die Ursachen, weil dort die Quelle sitzt, und die Größen am Ausgang sind immer die Wirkungen, weil dort die Last sitzt und alles aufnimmt, was die Quelle über das Zweitor liefert.
--- falsch
Das Netzwerk: Ströme sind immer die Ursachen, weil Spannungen erst durch Ströme in den Widerständen entstehen. Jede andere Wahl würde Ursache und Wirkung physikalisch vertauschen.
--- falsch
Die Rechnung, aber nur einmal je Zweitor: Hat man die Ursachen gewählt, ist jede andere Aufteilung für dieses Zweitor nicht mehr möglich, weil die vier Parameter dann festliegen.
:::
:::karte formel T-Zweitor mit Strömen als Ursachen
Wie lauten die Torspannungen $U_1$ und $U_2$ des T-Zweitors mit $R_\mathrm{a}$ am Eingang, $R_\mathrm{b}$ quer und $R_\mathrm{c}$ am Ausgang, wenn man die Ströme als Ursachen nimmt?
---
$U_1=R_\mathrm{a}I_1+R_\mathrm{b}(I_1+I_2)$ und $U_2=R_\mathrm{c}I_2+R_\mathrm{b}(I_1+I_2)$. Am Mittelpunkt treffen sich $I_1$ und $I_2$, durch $R_\mathrm{b}$ fließt ihre Summe.
--- falsch
$U_1=R_\mathrm{a}I_1+R_\mathrm{b}I_1$ und $U_2=R_\mathrm{c}I_2+R_\mathrm{b}I_2$. Jeder Strom fließt nur durch die Widerstände seiner eigenen Seite, durch $R_\mathrm{b}$ also nacheinander.
--- falsch
$U_1=R_\mathrm{a}I_1+R_\mathrm{b}(I_1-I_2)$ und $U_2=R_\mathrm{c}I_2+R_\mathrm{b}(I_2-I_1)$. Die beiden Ströme fließen durch $R_\mathrm{b}$ gegeneinander, deshalb zählt dort ihre Differenz.
--- falsch
$U_1=(R_\mathrm{a}+R_\mathrm{b}+R_\mathrm{c})I_1$ und $U_2=R_\mathrm{c}I_2$. Der Eingangsstrom fließt durch alle drei Widerstände, der Ausgangsstrom dagegen nur durch $R_\mathrm{c}$.
:::
:::karte zusammenhang Kopplung über den Querwiderstand
Warum hängt die Eingangsspannung $U_1$ des T-Zweitors auch vom Strom $I_2$ des anderen Tors ab?
---
Der Strom von Tor 2 läuft durch $R_\mathrm{b}$ und hebt dort das Potenzial des Mittelpunkts. Tor 1 sieht diese Anhebung, das ist der Summand mit $I_2$ in $U_1$.
--- falsch
Weil Tor 2 über die Masseleitung direkt mit Tor 1 verbunden ist. Der Strom $I_2$ fließt durch sie zur Klemme 1 und erhöht dort den Eingangsstrom.
--- falsch
Weil die Last an Tor 2 Energie entnimmt, die der Quelle am Eingang fehlt. Die Quelle gleicht das aus, indem sie ihre Spannung $U_1$ entsprechend anpasst.
--- falsch
Weil der Strom $I_2$ auch durch $R_\mathrm{a}$ fließt. Er erzeugt dort einen zusätzlichen Spannungsabfall, den man an Tor 1 als Teil von $U_1$ misst.
:::
:::karte zusammenhang Zweitor ohne eigene Quellen
Was gilt für die Wirkungen eines linearen Zweitors ohne eigene Quellen, wenn beide Ursachen null sind, und was würde eine unabhängige Quelle im Inneren ändern?
---
Ohne Ursachen, etwa $I_1=I_2=0$, sind beide Wirkungen null. Mit einer unabhängigen Quelle im Inneren käme in jeder Gleichung eine Konstante hinzu.
--- falsch
Die Wirkungen sind dann gleich den Parametern $p_{11}$ und $p_{22}$. Eine unabhängige Quelle im Inneren würde nur diese Parameter ändern, nicht die Form der Gleichungen.
--- falsch
Beide Wirkungen sind null. Eine unabhängige Quelle im Inneren ändert daran nichts, weil sie ohne Ursachen an den Toren keinen Strom treiben kann.
--- falsch
Die Gleichungen gelten dann nicht, weil man durch null Ursachen nicht teilen darf. Eine unabhängige Quelle im Inneren ist nötig, damit sie wieder gelten.
:::
:::karte begriff symmetrisches Zählpfeilsystem
Wie zeigen die Strompfeile eines Zweitors im symmetrischen Zählpfeilsystem, und wie heißt es noch?
---
An beiden Toren gilt das Verbraucherzählpfeilsystem: Beide Strompfeile zeigen in das Zweitor hinein. Es heißt auch mathematische Vorzeichenrichtung.
--- falsch
An beiden Toren gilt das Erzeugerzählpfeilsystem: Beide Strompfeile zeigen aus dem Zweitor heraus. Es heißt auch technisches Pfeilsystem.
--- falsch
Der Eingangsstrom zeigt hinein, der Ausgangsstrom heraus zur Last, sodass beide in Vorwärtsrichtung zählen. Es heißt auch mathematische Vorzeichenrichtung.
--- falsch
Die Strompfeile liegen spiegelbildlich zur Mittellinie des Zweitors: Oben zeigen sie hinein, unten heraus. Daher kommt der Name symmetrisch.
:::
:::karte begriff Kettenpfeilsystem
Wie sind die Strompfeile eines Zweitors im Kettenpfeilsystem gerichtet, und wie heißt es noch?
---
Am Eingang gilt das Verbraucherzählpfeilsystem, der Strom zeigt hinein; am Ausgang gilt das Erzeugerzählpfeilsystem, der Strom zeigt heraus, zur Last. Es heißt auch technisches Pfeilsystem.
--- falsch
An beiden Toren zeigen die Strompfeile hinein, wie beim Verbraucherzählpfeilsystem, damit beide Tore gleich behandelt werden. Es heißt auch technisches Pfeilsystem.
--- falsch
Am Eingang zeigt der Strom heraus zur Quelle, am Ausgang hinein von der Last, sodass die Ströme eine geschlossene Kette um das Zweitor bilden. Es heißt auch mathematische Vorzeichenrichtung.
--- falsch
An beiden Toren zeigen die Strompfeile heraus, wie beim Erzeugerzählpfeilsystem, weil ein Zweitor Energie an beide Seiten weitergibt. Es heißt auch technisches Pfeilsystem.
:::
:::karte begriff gemischtes Pfeilsystem
Wie sind die Torströme im gemischten Pfeilsystem gezählt, das in diesem Kapitel gilt, und welches Vorzeichen hat $I_2$ im Normalbetrieb mit Last?
---
$I_1$ und $I_2$ zeigen immer hinein. Wo der herausfließende Strom gebraucht wird, schreibt man ihn ausdrücklich als $-I_2$. Eine Last ergibt im Normalbetrieb deshalb ein negatives $I_2$.
--- falsch
$I_1$ zeigt hinein, $I_2$ heraus zur Last, wie im Kettenpfeilsystem. Eine Last ergibt im Normalbetrieb deshalb ein positives $I_2$, und ein Minus braucht man an keiner Stelle.
--- falsch
$I_1$ und $I_2$ zeigen immer hinein. Eine Last ergibt trotzdem ein positives $I_2$, weil sie den Strom über die zweite Klemme wieder in das Zweitor zurückschickt.
--- falsch
An jedem Tor wählt man die Pfeilrichtung so, dass der Strom positiv wird. $I_2$ ist deshalb im Normalbetrieb mit Last immer positiv, ohne Last null.
:::
::::
