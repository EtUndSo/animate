---
title: Stufe 2: Maschenströme erfüllen die Knotenregel
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180400
summary: Gesucht sind m Größen, aus denen alle Zweigströme folgen.
tags: Fenster
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Gesucht sind $m$ Größen, aus denen alle Zweigströme folgen. Diese Stufe zeigt, warum Kreisströme das leisten und warum die Knotenregel dabei von selbst gilt.
:::

**Die Idee.** Man denkt sich in jeder unabhängigen Masche einen eigenen Strom, der im Kreis läuft (Abb. [2](#abb-2)). Der Mechanismus liegt im Wort Kreis: Tritt der Strom über einen Zweig in einen Knoten ein, verlässt er ihn über einen anderen Zweig derselben Masche. Er bringt dem Knoten nichts hinein. Das gilt für jeden Kreisstrom, an jedem Knoten und für jeden Zahlenwert. In einem Zweig, der zu zwei Maschen gehört, überlagern sich beide Kreisströme. Gemessen wird nur diese Summe.

:::analogie
Zwei Ringbuslinien teilen sich eine Straße. Auf der gemeinsamen Straße fahren die Busse beider Linien, und jede Linie, die in eine Kreuzung einfährt, fährt dort auch wieder heraus. Die Analogie endet beim Einzelnen: Ein Elektron gehört keiner Masche an. Maschenströme sind Rechengrößen, wirklich fließt nur der Zweigstrom.
:::

:::abbildung et1/k8kreis 2
Knoten 1 mit den Maschenströmen I und II. Links: Jeder Kreisstrom läuft durch den Knoten hindurch. Rechts: Dieselbe Lage als Zweigströme. Zum Knoten fließt $I_\mathrm I$, ab fließen $I_\mathrm I-I_\mathrm{II}$ und $I_\mathrm{II}$. Die Summe ist für alle Werte null.
:::

:::satz Satz 2.1 (Maschenströme)
<span class="anker" id="satz-2-1"></span>

Legt man in jede von $m$ unabhängigen Maschen einen *Maschenstrom* $I_\mu$ mit frei gewählter Richtung, gilt für den Strom eines Zweigs

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{Zweig}=\sum_{\mu=1}^{m}\sigma_\mu\,I_\mu,\qquad\sigma_\mu=\begin{cases}+1&\text{Masche }\mu\text{ läuft in Pfeilrichtung des Zweigs,}\\-1&\text{Masche }\mu\text{ läuft gegen den Pfeil,}\\0&\text{Masche }\mu\text{ enthält den Zweig nicht.}\end{cases} \tag{2.1}$$

Die Knotenregel ist dann für alle Werte der $I_\mu$ erfüllt. Umgekehrt lässt sich jede Stromverteilung, die die Knotenregel erfüllt, so darstellen.
:::

:::herleitung Warum das immer geht
⁠*Knotenregel.* In einer Masche ist jeder Knoten mit genau zwei Zweigen verbunden ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Ihr Strom zählt am Knoten einmal zufließend und einmal abfließend, die Beiträge heben sich auf.

⁠*Vollständigkeit.* Man wählt einen Baum. Jeder Verbindungszweig schließt genau eine Masche, ihr Maschenstrom sei der Strom dieses Verbindungszweigs. Zieht man alle diese Kreisströme von der gegebenen Verteilung ab, erfüllt der Rest weiter die Knotenregel und ist in allen Verbindungszweigen null. Er kann nur im Baum fließen. Der Baum hat aber ein Ende, einen Knoten mit nur einem Baumzweig. Dort erzwingt die Knotenregel den Strom null. Man streicht diesen Zweig und wiederholt das. Der Rest ist überall null.
:::

⁠**So liest man das:** $\mu$ nummeriert die Maschen, in den Beispielen mit römischen Ziffern. Die Richtung ist frei, ein negativer Wert heißt: Der Kreisstrom läuft andersherum. **Gültigkeit:** Die Maschen müssen unabhängig sein. Lässt sich das Netz ohne Kreuzungen zeichnen, wählt man die __Fenster__, die Flächen zwischen den Zweigen. Beim Aufbau aus dem Baum teilt jeder neue Verbindungszweig genau eine Fläche in zwei, also gibt es genau $m$ Fenster.

::::beispiel
Fasst man im Rechenmodell Stromquelle und $R_5$ zu einem Zweig mit Spannungsquelle zusammen (Stufe [3](das-maschenstromverfahren.html#stufe-3)), bleiben drei Fenster I, II, III mit Maschenströmen im Uhrzeigersinn. Daraus folgen alle fünf Zweigströme:

| Zweig | links, $R_1$ | $R_2$ | $R_3$ | $R_4$ | rechts, $R_5$ |
|---|---|---|---|---|---|
| Strom | $I_\mathrm I$ | $I_\mathrm I-I_\mathrm{II}$ | $I_\mathrm{II}$ | $I_\mathrm{II}-I_\mathrm{III}$ | $I_\mathrm{III}$ |

An Knoten 1 ergibt das $I_\mathrm I-(I_\mathrm I-I_\mathrm{II})-I_\mathrm{II}=0$, ganz gleich, welche Werte die Ströme haben.
::::

⁠**Grenzfälle:** Für $m=1$ ist der Maschenstrom der Strom der Reihenschaltung. Für $I_\mathrm{II}=0$ verschwindet der Strom in $R_3$, die linke und die rechte Hälfte tauschen nichts aus.

:::frage Was misst ein Strommesser im Zweig von $R_2$, $I_\mathrm I$ oder $I_\mathrm{II}$?
Keinen von beiden, sondern den Zweigstrom $I_\mathrm I-I_\mathrm{II}$. Ein Maschenstrom ist nur dort direkt messbar, wo er als einziger fließt, hier zum Beispiel $I_\mathrm I$ in $R_1$. Das ist der Baum-Gedanke: Der Maschenstrom ist der Strom eines Zweigs, der nur zu dieser Masche gehört.
:::

:::aufgabe Aufgabe 2 ★ Vom Maschenstrom zum Zweigstrom
<span class="anker" id="aufg-2"></span>

Zwei Maschen teilen sich den senkrechten Widerstand $R_\mathrm g=3\,\mathrm{k\Omega}$, Masche a liegt links davon, Masche b rechts. Sonst enthält a nur eine Quelle und $R_\mathrm a=2\,\mathrm{k\Omega}$, b nur eine Quelle und $R_\mathrm b=1\,\mathrm{k\Omega}$. Beide Maschenströme laufen im Uhrzeigersinn, $I_\mathrm a=3$ mA, $I_\mathrm b=-1$ mA.

<ol class="al">

<li>

Wie groß ist der Strom in $R_\mathrm g$ in Richtung von $I_\mathrm a$?

</li>

<li>

Prüfe die Knotenregel am oberen Ende von $R_\mathrm g$.

</li>

<li>

Welche Spannung muss die Quelle in jeder Masche in Umlaufrichtung treiben?

</li>

</ol>

:::loesung
(a) Im gemeinsamen Zweig laufen beide im Uhrzeigersinn gedrehten Kreise gegeneinander: $I_\mathrm a-I_\mathrm b=3-(-1)=4$ mA in Richtung von $I_\mathrm a$.

(b) Liegt $R_\mathrm g$ senkrecht zwischen den Maschen, läuft $I_\mathrm a$ oben auf den Knoten zu, $I_\mathrm b$ oben von ihm weg. Abfließend sind $I_\mathrm a-I_\mathrm b$ nach unten und $I_\mathrm b$ nach rechts: $3-4-(-1)=0$.

(c) Masche a: $R_\mathrm a\,I_\mathrm a+R_\mathrm g\,(I_\mathrm a-I_\mathrm b)=6+12=18$ V. Masche b: $R_\mathrm b\,I_\mathrm b+R_\mathrm g\,(I_\mathrm b-I_\mathrm a)=-1-12=-13$ V. Die Quelle in b treibt also mit 13 V gegen den Uhrzeigersinn.
:::
:::

::::formelsammlung
**Zweigstrom aus Maschenströmen**

$$I_\mathrm{Zweig}=\sum_{\mu=1}^{m}\sigma_\mu\,I_\mu,\qquad\sigma_\mu=\begin{cases}+1&\text{Masche }\mu\text{ läuft in Pfeilrichtung des Zweigs,}\\-1&\text{Masche }\mu\text{ läuft gegen den Pfeil,}\\0&\text{Masche }\mu\text{ enthält den Zweig nicht.}\end{cases}$$

$I_\mu$ ist der Maschenstrom der Masche $\mu$ mit frei gewählter Richtung; ein negativer Wert heißt, der Kreisstrom läuft andersherum. Die Knotenregel ist für alle Werte der $I_\mu$ erfüllt, und jede Stromverteilung, die die Knotenregel erfüllt, lässt sich so darstellen. Die $m$ Maschen müssen unabhängig sein, etwa die Fenster eines ohne Kreuzungen gezeichneten Netzes.
::::

::::lernkarten
:::karte begriff Maschenstrom
Was versteht man unter einem Maschenstrom, mit dem man die Ströme eines Netzes beschreibt?
---
Einen gedachten Kreisstrom mit frei gewählter Richtung, je einen in jeder von $m$ unabhängigen Maschen. Er ist eine Rechengröße: Wirklich fließt nur der Zweigstrom, die Summe der Maschenströme im Zweig.
--- falsch
Den Strom, den ein Strommesser in jedem Zweig einer Masche anzeigt. In allen Zweigen einer Masche fließt derselbe Maschenstrom, auch in Zweigen, die zu zwei Maschen gehören.
--- falsch
Den Strom, den die Quelle einer Masche liefert. Maschen ohne Quelle haben keinen Maschenstrom, und seine Richtung ist durch die Polung der Quelle festgelegt, nicht frei wählbar.
--- falsch
Einen gedachten Kreisstrom je Knoten, der durch alle Zweige an diesem Knoten läuft und zu ihm zurückkehrt. Er ist eine Rechengröße, und die Summe aller dieser Ströme eines Knotens ergibt seinen Knotenstrom.
:::
:::karte formel Zweigstrom aus Maschenströmen
Wie berechnet man den Strom eines Zweigs aus den Maschenströmen $I_\mu$ der $m$ unabhängigen Maschen?
---
$I_\mathrm{Zweig}=\sum_{\mu=1}^{m}\sigma_\mu\,I_\mu$ mit dem Vorzeichen $\sigma_\mu$: $+1$, wenn Masche $\mu$ in Pfeilrichtung des Zweigs läuft, $-1$, wenn sie gegen den Pfeil läuft, und $0$, wenn sie den Zweig nicht enthält.
--- falsch
$I_\mathrm{Zweig}=\sum_{\mu=1}^{m}I_\mu$, die Summe aller Maschenströme des Netzes ohne Vorzeichen. Jeder Maschenstrom trägt zu jedem Zweig bei, weil alle Maschen miteinander zusammenhängen.
--- falsch
$I_\mathrm{Zweig}=\sum_{\mu=1}^{m}\sigma_\mu\,I_\mu$ mit $\sigma_\mu=+1$ für jede Masche, die den Zweig enthält, und $0$ sonst. Die Richtung der Maschenströme spielt dabei keine Rolle.
--- falsch
Der Zweigstrom ist gleich dem größten Maschenstrom, der durch den Zweig läuft. Die übrigen Maschenströme fließen nur in den Zweigen, die ihrer Masche allein gehören.
:::
:::karte zusammenhang Knotenregel von selbst
Warum ist die Knotenregel für jeden Zahlenwert der Maschenströme von selbst erfüllt?
---
Weil jeder Maschenstrom im Kreis läuft: In einer Masche hängt jeder Knoten an genau zwei Zweigen. Der Strom tritt über den einen ein und über den anderen aus, seine Beiträge heben sich auf.
--- falsch
Weil man die Maschenströme so berechnet, dass die Knotenregel stimmt. Erst die Lösung des Gleichungssystems sorgt dafür, dass an jedem Knoten die Summe der Ströme null ist.
--- falsch
Weil jeder Maschenstrom nur durch Knoten läuft, an denen keine Quelle liegt. Solche Knoten haben keinen Zufluss von außen, deshalb ist ihre Stromsumme in jedem Fall null.
--- falsch
Weil sich an jedem Knoten die Maschenströme verschiedener Maschen gegenseitig aufheben. Zwei benachbarte Maschenströme laufen dort stets entgegengesetzt und löschen sich deshalb vollständig aus.
:::
:::karte herleitung Vollständigkeit der Maschenströme
Zeige, dass sich jede Stromverteilung, die die Knotenregel erfüllt, durch Maschenströme darstellen lässt.
---
Man wählt einen Baum und gibt jeder Masche, die ein Verbindungszweig mit Baumzweigen schließt, als Maschenstrom den Strom dieses Verbindungszweigs, weil jeder Verbindungszweig genau eine solche Masche schließt.
---
Man zieht alle diese Kreisströme von der gegebenen Verteilung ab. Der Rest erfüllt weiter die Knotenregel, weil jeder Kreisstrom sie für sich erfüllt.
---
Der Rest ist in allen Verbindungszweigen null, weil dort genau der abgezogene Maschenstrom floss. Er kann also nur im Baum fließen.
---
Der Baum hat ein Ende, einen Knoten mit nur einem Baumzweig. Dort erzwingt die Knotenregel den Strom null, weil die Verbindungszweige an diesem Knoten keinen Rest führen.
---
Man streicht diesen Zweig und wiederholt das, bis kein Baumzweig übrig ist. Der Rest ist überall null, weil so jeder Baumzweig einmal am Ende hängt; die Verteilung besteht also nur aus Maschenströmen.
:::
:::karte begriff Fenster
Welche Maschen wählt man als unabhängige Maschen, wenn sich ein Netz ohne Kreuzungen zeichnen lässt, und wie viele sind es?
---
Die Fenster, also die Flächen zwischen den Zweigen. Es gibt genau $m$ davon, weil beim Aufbau aus dem Baum jeder neue Verbindungszweig genau eine Fläche in zwei teilt.
--- falsch
Die Fenster, also die Flächen zwischen den Zweigen. Es gibt genau $k-1$ davon, weil jeder Knoten außer dem Bezug genau eine Fläche nach oben begrenzt.
--- falsch
Die Fenster, also die Flächen zwischen den Zweigen samt der Außenfläche um das Netz. Es gibt genau $m+1$ davon, weil die Außenfläche als eigene Masche mitzählt.
--- falsch
Die Fenster, also die Flächen zwischen den Zweigen. Ihre Zahl hängt aber davon ab, wie man das Netz zeichnet, deshalb muss man ihre Unabhängigkeit jedes Mal einzeln prüfen.
:::
:::karte zusammenhang Strommesser im gemeinsamen Zweig
Welchen Strom zeigt ein Strommesser in einem Zweig an, der zu zwei Maschen gehört, und wo ist ein Maschenstrom direkt messbar?
---
Den Zweigstrom, also die Summe beider Maschenströme mit Vorzeichen, etwa $I_\mathrm I-I_\mathrm{II}$ im Zweig von $R_2$. Direkt messbar ist ein Maschenstrom nur in einem Zweig, der allein zu seiner Masche gehört.
--- falsch
Den größeren der beiden Maschenströme, weil der kleinere im gemeinsamen Zweig vom größeren verdrängt wird. Direkt messbar ist ein Maschenstrom deshalb in jedem Zweig seiner Masche, auch im gemeinsamen.
--- falsch
Beide Maschenströme getrennt, je nachdem, wie man das Messgerät polt. Direkt messbar ist ein Maschenstrom deshalb in jedem Zweig seiner Masche, auch im gemeinsamen.
--- falsch
Den Zweigstrom, also die Summe beider Maschenströme mit Vorzeichen. Direkt messbar ist ein Maschenstrom nirgends, weil er in jedem Zweig von anderen Maschenströmen überlagert wird.
:::
:::karte zusammenhang Negativer Maschenstrom
Was bedeutet es, wenn sich für einen Maschenstrom mit frei gewählter Richtung ein negativer Wert ergibt?
---
Der Kreisstrom läuft in Wirklichkeit andersherum als gewählt. Die Richtung darf man frei wählen, ein Minus im Ergebnis ist deshalb kein Fehler.
--- falsch
Die Masche gibt Energie ab, weil in ihr eine Quelle gegen die gewählte Richtung arbeitet. Ein negativer Maschenstrom kommt deshalb nur in Maschen mit Quelle vor.
--- falsch
Die Richtung war falsch gewählt, und man muss die Rechnung mit umgedrehtem Maschenstrom wiederholen, weil die Gleichungen nur für positive Werte gelten.
--- falsch
In dieser Masche fließt kein Strom, weil ein Kreisstrom nicht negativ werden kann. Das Minus zeigt einen Rechenfehler beim Aufstellen der Gleichungen an.
:::
:::karte zusammenhang Maschenstrom als Rechengröße
Kann man bei einem Elektron im gemeinsamen Zweig zweier Maschen angeben, zu welchem Maschenstrom es gehört?
---
Nein. Ein Elektron gehört keiner Masche an. Maschenströme sind Rechengrößen, die sich im gemeinsamen Zweig überlagern; wirklich fließt nur der Zweigstrom.
--- falsch
Ja, an seiner Richtung: Elektronen, die im Uhrzeigersinn laufen, gehören zur einen Masche, die übrigen zur anderen. Der Zweigstrom zählt beide Gruppen.
--- falsch
Ja, wie bei zwei Buslinien auf derselben Straße: Jedes Elektron läuft in einer bestimmten Masche im Kreis und verlässt jede Kreuzung wieder in seiner Masche.
--- falsch
Nein, weil im gemeinsamen Zweig gar keine Elektronen fließen. Dort heben sich die beiden Maschenströme stets auf, und der Zweig bleibt stromlos.
:::
:::karte zusammenhang Eine einzige Masche
Welchem Strom entspricht der Maschenstrom eines Netzes, das nur eine unabhängige Masche hat, also $m=1$?
---
Dem Strom der Reihenschaltung. Es gibt keinen gemeinsamen Zweig, also fließt in allen Zweigen derselbe Strom, und das ist der Maschenstrom.
--- falsch
Gar keinem, er ist null, weil ein Maschenstrom erst durch den Unterschied zweier Maschen entsteht. Bei $m=1$ fließt der Strom nur in Zweigen außerhalb der Masche.
--- falsch
Der Hälfte des Stroms der Reihenschaltung, weil der Kreisstrom jeden Knoten einmal hinein- und einmal hinausläuft und deshalb doppelt gezählt wird.
--- falsch
Dem Strom einer Parallelschaltung, weil bei einer einzigen Masche alle Zweige an denselben zwei Knoten hängen und sich den Strom teilen.
:::
::::
