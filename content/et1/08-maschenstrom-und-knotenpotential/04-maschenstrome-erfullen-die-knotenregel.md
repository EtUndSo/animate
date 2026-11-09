---
title: Stufe 2: Maschenströme erfüllen die Knotenregel
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Maschenstrom- und Knotenpotentialverfahren
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
⁠*Knotenregel.* In einer Masche ist jeder Knoten mit genau zwei Zweigen verbunden ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Ihr Strom zählt am Knoten einmal zufließend und einmal abfließend, die Beiträge heben sich auf.

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
