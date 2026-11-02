---
title: Stufe 4: Radiale Funktionen und Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110500
summary: Viele Felder hängen nur vom Abstand zum Ursprung ab.
tags: Gradientenfeld, Skalarpotential, Potentialfeld, Feldlinie, radialsymmetrische Funktion, radiale Einheitsvektor, Zentralfeld, Radialsymmetrisches Vektorfeld
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Viele Felder hängen nur vom Abstand zum Ursprung ab. Hier werden drei Begriffe getrennt, die sich leicht vermischen: die radialsymmetrische Funktion, das Zentralfeld und das radialsymmetrische Vektorfeld. Danach folgt, wie sie mit dem Gradienten zusammenhängen.
:::

**Die Idee.** Es gibt zwei Arten von Objekten: Eine skalare Funktion ordnet jedem Punkt $\boldsymbol{x}\in\mathbb{R}^n$ eine Zahl zu, ein Vektorfeld einen Vektor. Der Gradient verbindet beide. Hängt alles nur vom Abstand ab, wird die Rechnung eindimensional, und man kann ablesen, welche radialen Felder Gradienten sind.

:::definition Definition 4.1 (Gradientenfeld und Skalarpotential)
<span class="anker" id="satz-4-1"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $\boldsymbol{E}:\mathcal U\to\mathbb{R}^n$. Gilt $\boldsymbol{E}=\nabla\varphi$ für eine differenzierbare Funktion $\varphi$, heißt $\boldsymbol{E}$ ein __Gradientenfeld__ auf $\mathcal U$ und $\varphi$ ein __Skalarpotential__ von $\boldsymbol{E}$.
:::

In der Physik ist das Vorzeichen meist anders: Zu einem Potential $\phi$ gehört das __Potentialfeld__ $\boldsymbol{E}=-\nabla\phi$. So nimmt die potentielle Energie eines Teilchens längs einer __Feldlinie__ ab, also längs einer Kurve $\gamma$, die in Richtung von $\boldsymbol{E}$ läuft: Nach [(3.3)](die-kettenregel.html#gl-3-3) ist $\frac{\mathrm{d}}{\mathrm{d} t}\phi(\gamma(t))=-\boldsymbol{E}(\gamma(t))\cdot\dot\gamma(t)<0$. Für den Begriff Gradientenfeld spielt das Vorzeichen keine Rolle, denn $-\nabla\phi$ ist der Gradient von $-\phi$.

**Radialsymmetrische Funktion.** Eine __radialsymmetrische Funktion__ ist eine skalare Funktion der Form

<span class="anker" id="gl-4-1"></span>
$$u(\boldsymbol{x})=f(r),\qquad r=|\boldsymbol{x}|=\sqrt{x_1^2+\dots+x_n^2}. \tag{4.1}$$

⁠**So liest man das:** Hier sind zwei Funktionen im Spiel. $u$ hat $n$ Argumente, $f$ hat nur eines, den Abstand $r$. Der Wert ist eine Zahl, kein Vektor. Auf jeder Kugel um den Ursprung hat $u$ denselben Wert, die Kugeln sind also die Niveauflächen von $u$, die Höhenlinien in höherer Dimension.

**Der radiale Einheitsvektor.** Für $\boldsymbol{x}\neq0$ zeigt $\hat{\boldsymbol{e}}_r=\boldsymbol{x}/r$ vom Ursprung aus nach außen und hat die Länge 1. Das ist der __radiale Einheitsvektor__. Aus $r=\sqrt{x_1^2+\dots+x_n^2}$ folgt mit der Kettenregel $\partial r/\partial x_j=x_j/r$, also

<span class="anker" id="gl-4-2"></span>
$$\nabla r=\hat{\boldsymbol{e}}_r. \tag{4.2}$$

:::definition Definition 4.2 (Zwei Arten von Feldern)
<span class="anker" id="satz-4-2"></span>

Beide zeigen überall radial, sie unterscheiden sich in der Länge:

<ul>

<li>

__Zentralfeld__: $\boldsymbol{F}(\boldsymbol{x})=g(\boldsymbol{x})\,\hat{\boldsymbol{e}}_r$ mit einer beliebigen skalaren Funktion $g$. Auf einer Kugel darf die Länge schwanken.

</li>

<li>

__Radialsymmetrisches Vektorfeld__: $\boldsymbol{F}(\boldsymbol{x})=f(r)\,\hat{\boldsymbol{e}}_r$. Die Länge hängt nur von $r$ ab und ist auf jeder Kugel gleich.

</li>

</ul>
:::

Jedes radialsymmetrische Vektorfeld ist also ein Zentralfeld, aber nicht umgekehrt (Abb. [4](#abb-4)).

:::abbildung hm3/k1radial 4
Links: Eine radialsymmetrische Funktion liefert Zahlen, hier $u=r^2$ auf den Kreisen $r=1,2,3$. Mitte: Ein radialsymmetrisches Vektorfeld liefert radiale Vektoren, auf jedem Kreis gleich lang. Rechts: Ein Zentralfeld zeigt ebenfalls radial, ist auf einem Kreis aber verschieden lang.
:::

:::satz Satz 4.3 (Radiale Felder und Gradienten)
<span class="anker" id="satz-4-3"></span>

Auf $\mathbb{R}^n\setminus\{0\}$ mit $n\ge2$ gilt:

<ol class="rm">

<li>

Ist $f:(0,\infty)\to\mathbb{R}$ differenzierbar und $u(\boldsymbol{x})=f(r)$, dann ist

<span class="anker" id="gl-4-3"></span>
$$\nabla u=f'(r)\,\hat{\boldsymbol{e}}_r. \tag{4.3}$$

Der Gradient einer radialsymmetrischen Funktion ist ein radialsymmetrisches Vektorfeld.

</li>

<li>

Ist $f$ auf $(0,\infty)$ stetig, dann ist $\boldsymbol{F}=f(r)\,\hat{\boldsymbol{e}}_r$ ein Gradientenfeld mit $\varphi(\boldsymbol{x})=h(r)$, wobei $h(r)=\int f(r)\,\mathrm{d} r+\text{konst}$ eine beliebige Stammfunktion von $f$ ist.

</li>

<li>

Ein stetiges Zentralfeld ist genau dann ein Gradientenfeld, wenn es radialsymmetrisch ist.

</li>

</ol>
:::

⁠**So liest man das:** Der Gradient steht senkrecht auf den Niveauflächen. Bei $u=f(r)$ sind das Kugeln, also zeigt $\nabla u$ radial, und seine Länge ist die Steigung $|f'(r)|$. Umgekehrt steht ein radiales Feld senkrecht auf jedem Weg, der auf einer Kugel bleibt. Ist es ein Gradient, ändert sich das Potential auf diesem Weg also nicht. Das Potential hängt dann nur von $r$ ab, und damit auch die Länge des Felds.

:::herleitung Die drei Aussagen
(i) Kettenregel: $\partial u/\partial x_j=f'(r)\,\partial r/\partial x_j=f'(r)\,x_j/r$.

(ii) Setze $h'=f$ und wende (i) auf $\varphi(\boldsymbol{x})=h(r)$ an: $\nabla\varphi=h'(r)\,\hat{\boldsymbol{e}}_r=f(r)\,\hat{\boldsymbol{e}}_r$.

(iii) Dass radialsymmetrische Felder Gradientenfelder sind, sagt (ii). Sei umgekehrt $g\,\hat{\boldsymbol{e}}_r=\nabla\varphi$, und sei $\gamma$ eine Kurve auf einer Kugel $|\boldsymbol{x}|=R$. Aus $\gamma\cdot\gamma=R^2$ folgt $\gamma\cdot\dot\gamma=0$, also mit [(3.3)](die-kettenregel.html#gl-3-3)

$$\frac{\mathrm{d}}{\mathrm{d} t}\,\varphi(\gamma)=\nabla\varphi(\gamma)\cdot\dot\gamma=\frac{g(\gamma)}{R}\,\gamma\cdot\dot\gamma=0.$$

$\varphi$ ist also längs jeder Kurve auf der Kugel konstant. Für $n\ge2$ lassen sich zwei Punkte der Kugel immer durch eine solche Kurve verbinden, also ist $\varphi=h(r)$. Nach (i) folgt $g=h'(r)$.
:::

⁠**Grenzfall:** Für $n=1$ besteht die Kugel aus zwei getrennten Punkten, und (iii) wird falsch: Auf $\mathbb{R}\setminus\{0\}$ ist das Zentralfeld mit $g=1$ für $x>0$ und $g=2$ für $x<0$ ein Gradient, aber nicht radialsymmetrisch.

**Beispiel: Punktladung.** In $\mathbb{R}^3\setminus\{0\}$ ist $u(\boldsymbol{x})=Q/(4\pi r)$ radialsymmetrisch. Wegen $\frac{\mathrm{d}}{\mathrm{d} r}(1/r)=-1/r^2$ ist $\nabla u=-\frac{Q}{4\pi r^2}\,\hat{\boldsymbol{e}}_r$. Das Feld $\boldsymbol{E}=-\nabla u=\frac{Q}{4\pi r^2}\,\hat{\boldsymbol{e}}_r$ ist in geeigneten Einheiten das elektrische Feld einer Punktladung $Q$ im Ursprung. Hier ist $u$ das Potential im Sinn der Physik.

**Übersicht.** Die drei Eigenschaften sind verschieden. Die Tabelle zeigt für jede Kombination, die vorkommt, ein Beispiel:

| Feld | Zentralfeld | radialsymmetrisch | Gradientenfeld |
|---|---|---|---|
| $\boldsymbol{x}=r\,\hat{\boldsymbol{e}}_r$ | ja | ja | ja, $\varphi=r^2/2$ |
| $\hat{\boldsymbol{e}}_r/r^2$ in $\mathbb{R}^3$ | ja | ja | ja, $\varphi=-1/r$ |
| $x\,\hat{\boldsymbol{e}}_r$ in $\mathbb{R}^2$ | ja | nein | nein, nach (iii) |
| $(2x,4y)=\nabla(x^2+2y^2)$ | nein | nein | ja |
| $(-y,x)$ | nein | nein | nein, wegen Schwarz |

Zur letzten Zeile: Wäre $(-y,x)=\nabla\varphi$, dann wäre $\partial\varphi/\partial x=-y$ und $\partial\varphi/\partial y=x$, also $\partial^2\varphi/\partial y\,\partial x=-1$ und $\partial^2\varphi/\partial x\,\partial y=1$. Das widerspricht Satz [2.5](differenzierbar-heit-linear-genahert.html#satz-2-5).

:::frage Wird hier eine Funktion mit $n$ Argumenten in eine mit einem Argument umgewandelt?
Nein. $u$ hat weiter $n$ Argumente. Nur hängt ihr Wert von diesen $n$ Zahlen allein über die eine Zahl $r$ ab, und das schafft nicht jede Funktion. $u=x^2+y^2=r^2$ geht. $u=x^2+2y^2$ geht nicht, denn $(1,0)$ und $(0,1)$ haben denselben Abstand, aber die Werte 1 und 2. Der Nutzen: Ableiten und Integrieren werden zu Rechnungen mit nur einer Variablen.
:::

:::frage Ist $f(r)\,\hat{\boldsymbol{e}}_r$ dasselbe wie $f(r)$?
Nein. $f(r)$ ist eine Zahl, also eine radialsymmetrische Funktion. Erst der Faktor $\hat{\boldsymbol{e}}_r$ macht daraus einen Vektor, also ein Vektorfeld. Die Zahl $f(r)$ gibt dabei Länge und Vorzeichen an: Für $f(r)<0$ zeigt der Vektor nach innen.
:::

:::aufgabe Aufgabe 6 ★ Radial oder nicht
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Berechne $\nabla u$ für $u(\boldsymbol{x})=\ln r$ auf $\mathbb{R}^2\setminus\{0\}$.

</li>

<li>

Finde ein Skalarpotential zu $\boldsymbol{F}(\boldsymbol{x})=r^2\,\hat{\boldsymbol{e}}_r$.

</li>

<li>

Ist $\boldsymbol{F}(x,y)=\frac yr\,\hat{\boldsymbol{e}}_r$ ein Gradientenfeld auf $\mathbb{R}^2\setminus\{0\}$? Begründe ohne Rechnung.

</li>

</ol>

:::loesung
(a) Mit $f(r)=\ln r$ ist $f'(r)=1/r$, also $\nabla u=\hat{\boldsymbol{e}}_r/r=\boldsymbol{x}/r^2$. (b) Eine Stammfunktion von $r^2$ ist $r^3/3$, also $\varphi(\boldsymbol{x})=r^3/3$. (c) Nein. Das Feld ist ein Zentralfeld mit $g=y/r$. Auf einem Kreis ist $g$ nicht konstant, bei $(0,R)$ ist $g=1$, bei $(R,0)$ ist $g=0$. Es ist also nicht radialsymmetrisch und damit kein Gradientenfeld.
:::
:::
