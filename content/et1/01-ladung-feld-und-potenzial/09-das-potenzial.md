---
title: Stufe 7: Das Potenzial
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Ladung, Feld und Potenzial
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

**Beispiel.** Mit $\varphi=0$ auf B liegt A bei 9 V, und $\varphi(x)=9\,\mathrm{V}-3\,\mathrm{kV/m}\cdot x$: 6 V bei 1 mm, 3 V bei 2 mm. Kugel A ($+10$ nC) hat in 3 cm Abstand das Potenzial 3,0 kV, in 6 cm Abstand 1,5 kV. Die Differenz mal 1 nC ergibt die 1,5 µ J aus Stufe [6](arbeit-im-feld.html#stufe-6).

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
