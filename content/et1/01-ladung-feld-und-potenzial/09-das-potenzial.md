---
title: Stufe 7: Das Potenzial
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1110900
summary: Hängt die Arbeit nur von Start und Ziel ab, genügt eine einzige Zahl je Ort, um sie zu berechnen.
tags: Äquipotenzialflächen
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Hängt die Arbeit nur von Start und Ziel ab, genügt eine einzige Zahl je Ort, um sie zu berechnen. Diese Zahl ist das Potenzial.
:::

**Die Idee.** Man wählt einen Bezugspunkt und schreibt an jeden Ort die Arbeit je Ladung, die das Feld auf dem Weg von dort bis zum Bezugspunkt abgibt. Das Teilen durch die Ladung macht die Zahl zu einer Eigenschaft des Orts. Die Arbeit zwischen zwei Orten ist dann eine Differenz zweier solcher Zahlen.

:::analogie
Das Potenzial ist die Höhe einer Landschaft, das Feld ihr Gefälle, eine positive Ladung ein Ball, der bergab rollt. Das Bild endet bei negativen Ladungen: Sie rollen in derselben Landschaft bergauf.
:::

:::definition Definition 7.1 (Potenzial)
<span class="anker" id="satz-7-1"></span>

Im elektrostatischen Feld mit dem Bezugspunkt $P_0$ ist das Potenzial eines Punkts $P$

<span class="anker" id="gl-7-1"></span>
$$\varphi(P)=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s=-\int_{P_0}^{P}\vec E\cdot\mathrm{d}\vec s,\qquad[\varphi]=\frac{\mathrm J}{\mathrm C}=\mathrm V. \tag{7.1}$$

Eine Ladung $Q$ hat dort die potenzielle Energie $W_\mathrm{pot}=Q\,\varphi(P)$.
:::

:::satz Satz 7.2 (Arbeit als Potenzialdifferenz, zwei Verläufe)
<span class="anker" id="satz-7-2"></span>

<span class="anker" id="gl-7-2"></span>
$$W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr). \tag{7.2}$$

Im homogenen Feld in $x$-Richtung und im Feld einer Punktladung $Q_0$ (Bezugspunkt im Unendlichen) gilt

<span class="anker" id="gl-7-3"></span>
$$\varphi(x)=\varphi(0)-E\,x,\qquad\varphi(r)=k\,\frac{Q_0}{r}. \tag{7.3}$$
:::

:::herleitung Arbeit als Potenzialdifferenz
Weil die Arbeit nicht vom Weg abhängt, darf man von $P_1$ über $P_0$ nach $P_2$ gehen:

$$\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\int_{P_1}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_2}\vec E\cdot\mathrm{d}\vec s=\varphi(P_1)-\varphi(P_2).$$

Ohne Wegunabhängigkeit wäre $\varphi$ gar nicht eindeutig. Die Verläufe [(7.3)](#gl-7-3) folgen aus [(7.1)](#gl-7-1) mit konstantem $E$ und aus der Herleitung in Stufe [6](arbeit-im-feld.html#stufe-6) mit $r_2\to\infty$.
:::

⁠**So liest man das:** $\varphi$ ist eine Zahl je Ort, kein Vektor. In Richtung von $\vec E$ fällt $\varphi$, die Feldstärke ist das Gefälle des Potenzials: $E_x=-\mathrm{d}\varphi/\mathrm{d} x$. Rückt man $P_0$ woanders hin, ändern sich alle Potenziale um denselben Betrag. **Gültigkeit:** Das Potenzial setzt ein elektrostatisches Feld voraus.

**Äquipotenzialflächen.** Orte gleichen Potenzials bilden __Äquipotenzialflächen__. Auf ihnen lässt sich eine Ladung ohne Arbeit verschieben. Daraus folgt: Feldlinien stehen senkrecht auf ihnen, sonst gäbe es Arbeit längs der Fläche. Im Plattenpaar sind es Ebenen parallel zu den Platten, um eine Punktladung Kugeln. Ein ruhender Metallkörper hat wegen $\vec E=0$ überall dasselbe Potenzial.

:::abbildung et1/k1potenzial 8
Links: das Plattenpaar mit Bezugspunkt auf Platte B. Die gestrichelten Linien sind Äquipotenzialflächen im Schnitt, sie liegen je 3 V auseinander. Rechts: Das Potenzial fällt längs $x$ von 9 V auf 0 V, seine Steigung $-3$ V/mm ist $-E$.
:::

::::beispiel
Mit $\varphi=0$ auf B liegt A bei 9 V, und $\varphi(x)=9\,\mathrm{V}-3\,\mathrm{kV/m}\cdot x$: 6 V bei 1 mm, 3 V bei 2 mm. Kugel A ($+10$ nC) hat in 3 cm Abstand das Potenzial 3,0 kV, in 6 cm Abstand 1,5 kV. Die Differenz mal 1 nC ergibt die 1,5 µ J aus Stufe [6](arbeit-im-feld.html#stufe-6).
::::

⁠**Kurz gesagt:** Das Potenzial ist die Energie je Ladung an einem Ort, gemessen vom Bezugspunkt aus.

⁠**Grenzfälle:** Für $r\to\infty$ geht $\varphi\to0$, das ist der gewählte Bezugspunkt. Für $E=0$ ist $\varphi$ konstant, muss aber nicht null sein.

:::frage Wenn $\varphi=0$ ist, gibt es dort auch kein Feld, oder?
Nein. Das Feld hängt vom Gefälle ab, nicht vom Wert. Platte B hat $\varphi=0$, direkt davor herrscht das volle Feld 3 kV/m. Umgekehrt ist im Inneren einer geladenen Metallkugel $E=0$, ihr Potenzial aber nicht null.
:::

:::aufgabe Aufgabe 7 ★★ Potenzial und Feld trennen
<span class="anker" id="aufg-7"></span>

Auf der $x$-Achse liegen $Q_1=+4$ nC bei $x=0$ und $Q_2=-1$ nC bei $x=6$ cm, der Bezugspunkt liegt im Unendlichen.

<ol class="al">

<li>

Berechne das Potenzial bei $x=3$ cm. Warum addiert man hier ohne Richtungen?

</li>

<li>

Wo zwischen den Ladungen ist $\varphi=0$? Wie groß ist $E$ dort?

</li>

</ol>

:::loesung
(a) Potenziale sind Zahlen, sie addieren sich mit Vorzeichen: $\varphi=k\,(4\,\mathrm{nC}-1\,\mathrm{nC})/3\,\mathrm{cm}=899$ V. (b) $4/x-1/(6-x)=0$ mit $x$ in cm ergibt $x=4{,}8$ cm. Dort zeigen beide Felder nach rechts: $E=k\cdot4\,\mathrm{nC}/(4{,}8\,\mathrm{cm})^2+k\cdot1\,\mathrm{nC}/(1{,}2\,\mathrm{cm})^2=15{,}6\,\mathrm{kV/m}+62{,}4\,\mathrm{kV/m}=78{,}0$ kV/m. $\varphi=0$ bedeutet also nicht $E=0$.
:::
:::

::::formelsammlung
**Potenzial**

$$\varphi(P)=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s=-\int_{P_0}^{P}\vec E\cdot\mathrm{d}\vec s,\qquad[\varphi]=\frac{\mathrm J}{\mathrm C}=\mathrm V$$

Arbeit je Ladung, die das Feld auf dem Weg von $P$ zum Bezugspunkt $P_0$ abgibt; eine Zahl je Ort, kein Vektor. Setzt ein elektrostatisches Feld voraus. Rückt $P_0$ woanders hin, ändern sich alle Potenziale um denselben Betrag.

**Potenzielle Energie**

$$W_\mathrm{pot}=Q\,\varphi(P)$$

Energie einer Ladung $Q$ am Ort $P$, gegenüber dem Bezugspunkt.

**Arbeit als Potenzialdifferenz**

$$W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr)$$

Folgt aus der Wegunabhängigkeit: Man darf von $P_1$ über $P_0$ nach $P_2$ gehen.

**Potenzial im homogenen Feld**

$$\varphi(x)=\varphi(0)-E\,x$$

Feld in $x$-Richtung; in Feldrichtung fällt $\varphi$.

**Potenzial einer Punktladung**

$$\varphi(r)=k\,\frac{Q_0}{r}$$

Bezugspunkt im Unendlichen.

**Feldstärke als Gefälle des Potenzials**

$$E_x=-\mathrm{d}\varphi/\mathrm{d} x$$

Das Feld hängt vom Gefälle ab, nicht vom Wert. Äquipotenzialflächen (Orte gleichen Potenzials) stehen senkrecht auf den Feldlinien; im Plattenpaar sind es Ebenen, um eine Punktladung Kugeln. Ein ruhender Metallkörper hat überall dasselbe Potenzial.
::::

::::lernkarten
:::karte begriff Potenzial
Was gibt das Potenzial $\varphi$ eines Punkts $P$ an?
---
Die Arbeit je Ladung, die das Feld auf dem Weg von $P$ bis zum Bezugspunkt $P_0$ abgibt: $\varphi(P)=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s$, Einheit $\mathrm{J/C}=\mathrm V$. Es ist eine Zahl je Ort, kein Vektor, und setzt ein elektrostatisches Feld voraus.
--- falsch
Die Arbeit je Ladung, die das Feld auf dem Weg vom Bezugspunkt $P_0$ bis $P$ abgibt: $\varphi(P)=\int_{P_0}^{P}\vec E\cdot\mathrm{d}\vec s$, Einheit $\mathrm{J/C}=\mathrm V$. Es ist eine Zahl je Ort, kein Vektor, und setzt ein elektrostatisches Feld voraus.
--- falsch
Die Kraft je Ladung an diesem Ort: $\varphi(P)=\vec F/Q$, Einheit V/m. Es ist ein Vektor in Richtung der Kraft auf eine positive Ladung und lässt sich in jedem Feld angeben, auch wenn die Arbeit vom Weg abhängt.
--- falsch
Die gesamte Energie, die eine Ladung $Q$ an diesem Ort hat: $\varphi(P)=Q\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s$, Einheit J. Es hängt von der Ladung ab, die man an den Ort bringt, und setzt ein elektrostatisches Feld voraus.
:::
:::karte begriff Bezugspunkt
Welche Rolle spielt der Bezugspunkt, wenn man jedem Ort ein Potenzial zuordnet, und was ändert sich, wenn man ihn verschiebt?
---
Der frei gewählte Punkt $P_0$ mit dem Potenzial null, bis zu dem die Arbeit je Ladung gezählt wird. Verschiebt man ihn, ändern sich alle Potenziale um denselben Betrag.
--- falsch
Ein von der Natur vorgegebener Punkt, stets im Unendlichen. Nur von dort aus gemessen haben Potenziale ihren richtigen Wert, andere Bezugspunkte verfälschen sie.
--- falsch
Der Punkt, an dem das Feld null ist. Verschiebt man ihn, ändern sich die Feldstärken an allen Orten um denselben Betrag, die Potenziale bleiben gleich.
--- falsch
Der frei gewählte Punkt $P_0$, an dem das Potenzial null ist. Verschiebt man ihn, ändern sich alle Potenziale, aber jedes um einen anderen Betrag.
:::
:::karte formel Arbeit als Potenzialdifferenz
Wie hängt die Arbeit des Felds an einer Ladung $Q$ auf dem Weg von $P_1$ nach $P_2$ mit den Potenzialen zusammen?
---
$W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr)$: Ladung mal Potenzial am Start minus Potenzial am Ziel. Das gilt im elektrostatischen Feld für jeden Weg.
--- falsch
$W_{12}=Q\,\bigl(\varphi(P_2)-\varphi(P_1)\bigr)$: Ladung mal Potenzial am Ziel minus Potenzial am Start. Das gilt im elektrostatischen Feld für jeden Weg.
--- falsch
$W_{12}=\varphi(P_1)-\varphi(P_2)$: Die Ladung fällt heraus, weil das Potenzial schon Energie je Ladung ist. Das gilt im elektrostatischen Feld für jeden Weg.
--- falsch
$W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr)$, aber nur auf dem geraden Weg von $P_1$ nach $P_2$. Auf jedem Umweg kommt ein Zusatzglied hinzu.
:::
:::karte herleitung Arbeit als Potenzialdifferenz
Leite aus der Definition des Potenzials und der Wegunabhängigkeit her, dass $W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr)$ ist.
---
Man geht von $P_1$ über den Bezugspunkt $P_0$ nach $P_2$: $\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\int_{P_1}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_2}\vec E\cdot\mathrm{d}\vec s$, weil die Arbeit nicht vom Weg abhängt.
---
Das erste Integral ist $\varphi(P_1)$, weil das Potenzial als Integral vom Punkt bis zum Bezugspunkt definiert ist.
---
Das zweite Integral ist $-\varphi(P_2)$, weil es in umgekehrter Richtung vom Bezugspunkt zum Punkt läuft: $\varphi(P)=-\int_{P_0}^{P}\vec E\cdot\mathrm{d}\vec s$.
---
Mit $W_{12}=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$ folgt $W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr)$, weil die Arbeit Ladung mal Integral ist. Ohne Wegunabhängigkeit wäre $\varphi$ gar nicht eindeutig.
:::
:::karte formel Potenzialverläufe
Wie verläuft das Potenzial im homogenen Feld in $x$-Richtung, und wie im Feld einer Punktladung $Q_0$ mit Bezugspunkt im Unendlichen?
---
Homogen: $\varphi(x)=\varphi(0)-E\,x$, es fällt linear in Feldrichtung. Punktladung: $\varphi(r)=k\,\frac{Q_0}{r}$, proportional zu $1/r$, für $r\to\infty$ geht $\varphi\to0$.
--- falsch
Homogen: $\varphi(x)=\varphi(0)+E\,x$, es steigt linear in Feldrichtung. Punktladung: $\varphi(r)=k\,\frac{Q_0}{r}$, proportional zu $1/r$, für $r\to\infty$ geht $\varphi\to0$.
--- falsch
Homogen: $\varphi(x)=\varphi(0)-E\,x$, es fällt linear in Feldrichtung. Punktladung: $\varphi(r)=k\,\frac{Q_0}{r^2}$, proportional zu $1/r^2$ wie das Feld selbst.
--- falsch
Homogen: $\varphi$ ist überall gleich, weil auch $E$ überall gleich ist. Punktladung: $\varphi(r)=k\,\frac{Q_0}{r}$, proportional zu $1/r$, für $r\to\infty$ geht $\varphi\to0$.
:::
:::karte formel Feldstärke als Gefälle
Wie hängt die Feldstärke mit dem Potenzial zusammen?
---
Die Feldstärke ist das Gefälle des Potenzials, $E_x=-\mathrm{d}\varphi/\mathrm{d} x$: In Richtung von $\vec E$ fällt $\varphi$. Es zählt die Änderung, nicht der Wert; auch wo $\varphi=0$ ist, kann ein Feld herrschen.
--- falsch
Die Feldstärke ist die Steigung des Potenzials, $E_x=+\mathrm{d}\varphi/\mathrm{d} x$: In Richtung von $\vec E$ steigt $\varphi$. Es zählt die Änderung, nicht der Wert; auch wo $\varphi=0$ ist, kann ein Feld herrschen.
--- falsch
Die Feldstärke ist proportional zum Potenzial, $E=\varphi/x$: Je höher das Potenzial an einem Ort, desto stärker das Feld dort. Wo $\varphi=0$ ist, herrscht kein Feld.
--- falsch
Die Feldstärke ist das Gefälle des Potenzials, $E_x=-\mathrm{d}\varphi/\mathrm{d} x$: In Richtung von $\vec E$ fällt $\varphi$. Wo $E=0$ ist, muss deshalb auch $\varphi=0$ sein, etwa im Inneren eines Metalls.
:::
:::karte formel Potenzielle Energie
Welche potenzielle Energie hat eine Ladung $Q$ an einem Ort mit dem Potenzial $\varphi(P)$?
---
$W_\mathrm{pot}=Q\,\varphi(P)$, gemessen vom Bezugspunkt aus. Für $Q<0$ ist sie dort am kleinsten, wo $\varphi$ am größten ist.
--- falsch
$W_\mathrm{pot}=\varphi(P)/Q$, gemessen vom Bezugspunkt aus. Je größer die Ladung, desto kleiner ihre potenzielle Energie am selben Ort.
--- falsch
$W_\mathrm{pot}=Q\,\varphi(P)$, gemessen vom Bezugspunkt aus. Für $Q<0$ ist sie dort am kleinsten, wo auch $\varphi$ am kleinsten ist.
--- falsch
$W_\mathrm{pot}=\varphi(P)$ für jede Ladung, weil das Potenzial schon die Energie am Ort ist. Das Vorzeichen von $Q$ spielt keine Rolle.
:::
:::karte begriff Äquipotenzialfläche
Was ist eine Äquipotenzialfläche, und wie stehen die Feldlinien zu ihr?
---
Eine Fläche aus Orten gleichen Potenzials. Auf ihr lässt sich eine Ladung ohne Arbeit verschieben, deshalb stehen die Feldlinien senkrecht auf ihr.
--- falsch
Eine Fläche, auf der die Feldstärke überall gleich groß ist. Die Feldlinien verlaufen parallel zu ihr, ohne sie irgendwo zu durchstoßen oder zu kreuzen.
--- falsch
Eine Fläche aus Orten gleichen Potenzials. Die Feldlinien verlaufen in ihr, denn längs der Fläche bewegen sich Ladungen ohne Arbeit.
--- falsch
Eine Fläche aus Orten mit $\varphi=0$, also der Bezugspunkt in ausgedehnter Form. Auf ihr ist das Feld überall null.
:::
:::karte zusammenhang Metall hat ein Potenzial
Warum hat ein ruhender Metallkörper überall dasselbe Potenzial?
---
Weil im ruhenden Metall $\vec E=0$ ist: Längs jedes Wegs im Metall verrichtet das Feld keine Arbeit, also ändert sich das Potenzial nicht. Null muss es dabei nicht sein.
--- falsch
Weil jeder Metallkörper mit dem Bezugspunkt verbunden ist. Sein Potenzial ist deshalb überall null, gleich welche Ladung er trägt und wo er steht.
--- falsch
Weil sich die Ladung im Metall gleichmäßig über das ganze Volumen verteilt, bis tief ins Innere. Gleich viel Ladung an jedem Ort ergibt an jedem Ort dasselbe Potenzial.
--- falsch
Weil die Feldlinien im Metall parallel und gleich dicht verlaufen. In einem solchen homogenen Feld hat jeder Ort dasselbe Potenzial.
:::
::::
