---
title: Radialsymmetrische Funktionen und Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3110300
summary: Viele Funktionen und Felder hängen nur vom Abstand zu einem Punkt ab, zum Beispiel das Potential und das Feld einer Punktladung.
tags: Stammfunktion, Kugelfläche, radialsymmetrisch, Profil, radiale Einheitsvektor, Coulomb-Potential, Zentralfeld, radialsymmetrisches Vektorfeld
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Viele Funktionen und Felder hängen nur vom Abstand zu einem Punkt ab, zum Beispiel das Potential und das Feld einer Punktladung. Dieser Abschnitt zeigt, wie sich ihre Gradienten mit einer einzigen Variablen ausrechnen lassen und welche Felder dieser Art Gradientenfelder sind.
:::

### Was du dafür brauchst: Stammfunktionen

<span class="anker" id="stufe-2-1"></span>

Ableiten macht aus einer Funktion ihre Steigung. Manchmal kennt man die Steigung und sucht die Funktion dazu.

Eine differenzierbare Funktion $p$ auf einem Intervall heißt __Stammfunktion__ von $f$, wenn $p'=f$ gilt. Jede stetige Funktion $f$ auf einem Intervall hat eine Stammfunktion, zum Beispiel

$$p(r)=\int_{r_0}^{r}f(\sigma)\,\mathrm{d}\sigma$$

mit einer festen Zahl $r_0$ aus dem Intervall. Das ist der Hauptsatz der Differential- und Integralrechnung. Zwei Stammfunktionen derselben Funktion unterscheiden sich auf einem Intervall nur um eine Konstante, denn ihre Differenz hat die Ableitung null. Man schreibt alle zusammen als $\int f(r)\,\mathrm{d} r+\text{konst}$.

⁠**Beispiel:** Auf dem Intervall $(0,\infty)$ ist $p(r)=-1/r$ eine Stammfunktion von $f(r)=1/r^2$, denn $p'(r)=1/r^2$. Ebenso ist $r^2/2$ eine Stammfunktion von $r$.

⁠**Kurz gesagt:** Eine Stammfunktion ist eine Funktion mit vorgegebener Ableitung. Stetige Funktionen haben immer eine, bis auf eine Konstante eindeutig.

### Was du dafür brauchst: Kugelflächen

<span class="anker" id="stufe-2-2"></span>

Funktionen, die nur vom Abstand zum Nullpunkt abhängen, haben auf allen Punkten mit gleichem Abstand denselben Wert. Diese Punkte bilden eine Kugelfläche.

Für eine Zahl $R>0$ heißt die Menge aller Punkte mit dem Abstand $R$ vom Nullpunkt,

$$\{\boldsymbol{x}\in\mathbb{R}^n:\ |\boldsymbol{x}|=R\},$$

die __Kugelfläche__ mit dem Radius $R$ um den Nullpunkt. In der Ebene ist sie ein Kreis, im Raum die Oberfläche einer Kugel. Für $n\ge2$ kann man je zwei ihrer Punkte durch eine differenzierbare Kurve verbinden, die ganz auf ihr bleibt, zum Beispiel durch einen Kreisbogen um den Nullpunkt. Für $n=1$ besteht sie nur aus den beiden Punkten $R$ und $-R$.

⁠**Beispiel:** Der Punkt $(3,4)$ liegt auf dem Kreis mit dem Radius $5$, ebenso $(5,0)$ und $(0,-5)$. Der Punkt $(1,2,2)$ liegt auf der Kugelfläche mit dem Radius $3$.

⁠**Kurz gesagt:** Die Kugelfläche mit Radius $R$ besteht aus allen Punkten mit dem Abstand $R$ vom Nullpunkt.

### Radialsymmetrische Funktionen

<span class="anker" id="stufe-2-3"></span>

Das Potential einer Punktladung, die Helligkeit um eine Lampe oder die Temperatur um eine kleine Wärmequelle hängen nur davon ab, wie weit man von der Quelle entfernt ist, nicht davon, in welcher Richtung man steht.

Man kann sich Zwiebelschalen um den Nullpunkt vorstellen. Auf jeder Schale, also auf jeder Kugelfläche, hat die Funktion einen festen Wert. Die Kugelflächen sind ihre Niveauflächen, in der Ebene sind die Kreise um den Nullpunkt ihre Höhenlinien.

:::definition Definition 2.1 (Radialsymmetrische Funktion)
<span class="anker" id="satz-2-1"></span>

Für $\boldsymbol{x}\in\mathbb{R}^n$ sei

$$r:=|\boldsymbol{x}|=\sqrt{x_1^2+\dots+x_n^2}$$

der Abstand vom Nullpunkt. Eine skalare Funktion heißt __radialsymmetrisch__, wenn sie die Form

$$u(\boldsymbol{x})=f(r)=f(|\boldsymbol{x}|)$$

hat, mit einer Funktion $f$ einer Variablen.
:::

⁠**So liest man das:** Hier sind zwei Funktionen im Spiel. $u$ hat $n$ Argumente, $x_1$ bis $x_n$. Die Funktion $f$ hat nur eines, den Abstand $r$. Sie heißt das __Profil__ von $u$: Sie sagt, welchen Wert $u$ im Abstand $r$ hat. Meist betrachtet man $u$ auf $\mathbb{R}^n\setminus\{0\}$ und $f$ auf $(0,\infty)$, weil viele Profile im Nullpunkt nicht erklärt sind.

⁠**Beispiel:** $u(x,y)=x^2+y^2$ ist radialsymmetrisch mit dem Profil $f(r)=r^2$. Die Schale $\varphi(x,y)=x^2+2y^2$ ist es nicht: Die Punkte $(1,0)$ und $(0,1)$ haben beide den Abstand $1$, aber die Werte $1$ und $2$. Im Raum ist $u(\boldsymbol{x})=1/|\boldsymbol{x}|$ radialsymmetrisch mit dem Profil $f(r)=1/r$ auf $(0,\infty)$.

:::hintergrund Wird hier eine Funktion von $n$ Variablen in eine Funktion von einer Variablen umgewandelt?
Nein. $u$ hat weiterhin $n$ Argumente. Ihr Wert hängt aber von diesen $n$ Zahlen nur über die eine Zahl $r$ ab, und das schafft nicht jede Funktion. Für $u=x^2+y^2=r^2$ geht es, für die Schale $x^2+2y^2$ nicht. Der Nutzen: Ableiten und Integrieren werden zu Rechnungen mit nur einer Variablen, nämlich mit dem Profil $f$.
:::

⁠**Kurz gesagt:** Eine radialsymmetrische Funktion hat auf jeder Kugelfläche um den Nullpunkt denselben Wert. Sie ist durch ihr Profil $f(r)$ festgelegt.

### Der radiale Einheitsvektor

<span class="anker" id="stufe-2-4"></span>

Bei radialsymmetrischen Funktionen ist eine Richtung ausgezeichnet: die vom Nullpunkt weg. Man braucht einen Vektor, der in jedem Punkt in diese Richtung zeigt.

Man stellt sich in einem Punkt $\boldsymbol{x}\neq0$ vor und schaut vom Nullpunkt weg. Der Pfeil $\boldsymbol{x}$ zeigt in diese Richtung, ist aber $r$ lang. Teilt man durch $r$, bleibt die Richtung, und die Länge wird $1$.

:::definition Definition 2.2 (Radialer Einheitsvektor)
<span class="anker" id="satz-2-2"></span>

Für $\boldsymbol{x}\in\mathbb{R}^n\setminus\{0\}$ heißt

$$\hat{\boldsymbol{e}}_r=\frac{\boldsymbol{x}}{r}=\frac{\boldsymbol{x}}{|\boldsymbol{x}|}$$

der __radiale Einheitsvektor__. Er hat die Länge $1$ und zeigt vom Nullpunkt weg. Ordnet man jedem Punkt seinen Vektor $\hat{\boldsymbol{e}}_r$ zu, ist $\hat{\boldsymbol{e}}_r$ ein Vektorfeld auf $\mathbb{R}^n\setminus\{0\}$.
:::

Dieser Vektor ist der Gradient des Abstands. Fasst man $r=\sqrt{x_1^2+\dots+x_n^2}$ als Funktion von $\boldsymbol{x}$ auf, gibt die Kettenregel einer Variablen

$$\frac{\partial r}{\partial x_j}=\frac{1}{2\sqrt{x_1^2+\dots+x_n^2}}\cdot2x_j=\frac{x_j}{r}.$$

Alle $n$ Komponenten zusammen ergeben die wichtige Formel

<span class="anker" id="gl-2-1"></span>
$$\nabla r=\hat{\boldsymbol{e}}_r . \tag{2.1}$$

Anschaulich: Der Abstand wächst am schnellsten, wenn man direkt vom Nullpunkt weggeht, und zwar mit der Steigung $1$.

⁠**Beispiel:** Im Punkt $\boldsymbol{x}=(3,4)$ ist $r=5$ und $\hat{\boldsymbol{e}}_r=(\tfrac35,\tfrac45)$. Die partiellen Ableitungen von $r=\sqrt{x^2+y^2}$ sind dort $\frac{x}{r}=\frac35$ und $\frac yr=\frac45$, in Übereinstimmung mit [(2.1)](#gl-2-1).

⁠**Kurz gesagt:** Der radiale Einheitsvektor $\hat{\boldsymbol{e}}_r=\boldsymbol{x}/r$ zeigt vom Nullpunkt weg, hat die Länge $1$ und ist der Gradient des Abstands $r$.

### Der Gradient einer radialsymmetrischen Funktion

<span class="anker" id="stufe-2-5"></span>

Wohin zeigt der Gradient einer Funktion, die nur vom Abstand abhängt? Er steht senkrecht auf den Niveauflächen, und das sind Kugelflächen. Also muss er radial zeigen, und seine Länge kann nur von der Steigung des Profils abhängen.

:::satz Satz 2.3 (Gradient radialsymmetrischer Funktionen)
<span class="anker" id="satz-2-3"></span>

Ist $f\colon(0,\infty)\to\mathbb{R}$ differenzierbar und $u(\boldsymbol{x})=f(r)$ mit $r=|\boldsymbol{x}|$, dann gilt auf $\mathbb{R}^n\setminus\{0\}$

<span class="anker" id="gl-2-2"></span>
$$\nabla u=f'(r)\,\hat{\boldsymbol{e}}_r . \tag{2.2}$$
:::

:::beweis Kettenregel
Nach der Kettenregel und [(2.1)](#gl-2-1) ist $\dfrac{\partial u}{\partial x_j}=f'(r)\,\dfrac{\partial r}{\partial x_j}=f'(r)\,\dfrac{x_j}{r}$ für jedes $j$. Zusammen ist das $\nabla u=f'(r)\,\boldsymbol{x}/r=f'(r)\,\hat{\boldsymbol{e}}_r$.
:::

⁠**So liest man das:** Der Gradient zeigt rein radial. Seine Länge ist $|f'(r)|$, die Steigung des Profils. Ist $f'(r)<0$, fällt $u$ nach außen, und der Gradient zeigt nach innen.

⁠**Beispiel:** Für $u(x,y)=x^2+y^2$ ist $f(r)=r^2$ und $f'(r)=2r$. Nach [(2.2)](#gl-2-2) ist $\nabla u=2r\,\hat{\boldsymbol{e}}_r=2\boldsymbol{x}=(2x,2y)^T$. Direkt abgeleitet kommt dasselbe heraus.

⁠**Kurz gesagt:** Der Gradient einer radialsymmetrischen Funktion ist die Steigung des Profils mal $\hat{\boldsymbol{e}}_r$.

### Das Coulomb-Potential

<span class="anker" id="stufe-2-6"></span>

Das wichtigste radialsymmetrische Beispiel der Elektrotechnik ist das Potential einer Punktladung. Mit Satz [2.3](#satz-2-3) erhält man sein Feld ohne Rechnung in Komponenten.

Sei $Q\in\mathbb{R}$ eine Zahl und

$$u(\boldsymbol{x})=\frac{Q}{4\pi r},\qquad r=|\boldsymbol{x}|,\qquad\boldsymbol{x}\in\mathbb{R}^3\setminus\{0\}.$$

Das Profil ist $f(r)=\frac{Q}{4\pi r}$. Wegen $\frac{\mathrm{d}}{\mathrm{d} r}\frac1r=-\frac1{r^2}$ ist $f'(r)=-\frac{Q}{4\pi r^2}$, und [(2.2)](#gl-2-2) liefert

$$\nabla u(\boldsymbol{x})=-\frac{Q}{4\pi r^2}\,\hat{\boldsymbol{e}}_r .$$

Das Potentialfeld $\boldsymbol{E}=-\nabla u=\frac{Q}{4\pi r^2}\,\hat{\boldsymbol{e}}_r$ ist in geeigneten Einheiten das elektrische Feld einer Punktladung $Q$ im Nullpunkt. Für $Q>0$ zeigt es nach außen und wird mit $1/r^2$ schwächer. Man nennt $u$ das __Coulomb-Potential__.

⁠**Beispiel:** Mit $Q=4\pi$ ist $u=1/r$ und $\boldsymbol{E}=\hat{\boldsymbol{e}}_r/r^2=\boldsymbol{x}/r^3$. Im Punkt $(0,3,4)$ ist $r=5$, also $u=\frac15$ und $\boldsymbol{E}=\frac{1}{125}(0,3,4)$.

⁠**Kurz gesagt:** Das Coulomb-Potential $Q/(4\pi r)$ hat das Feld $\boldsymbol{E}=-\nabla u=\frac{Q}{4\pi r^2}\hat{\boldsymbol{e}}_r$, das mit $1/r^2$ abfällt.

### Zentralfelder

<span class="anker" id="stufe-2-7"></span>

Bei manchen Feldern zeigen alle Pfeile genau vom Nullpunkt weg oder auf ihn zu, wie die Speichen eines Rads. Die Länge der Pfeile darf dabei von Punkt zu Punkt verschieden sein.

:::definition Definition 2.4 (Zentralfeld)
<span class="anker" id="satz-2-4"></span>

Ein Vektorfeld auf $\mathbb{R}^n\setminus\{0\}$ der Form

$$\boldsymbol{F}(\boldsymbol{x})=g(\boldsymbol{x})\,\hat{\boldsymbol{e}}_r$$

mit einer skalaren Funktion $g$ heißt __Zentralfeld__.
:::

⁠**So liest man das:** Die Richtung ist überall radial. Die Zahl $g(\boldsymbol{x})$ gibt Länge und Sinn des Pfeils an: Für $g(\boldsymbol{x})>0$ zeigt er nach außen, für $g(\boldsymbol{x})<0$ nach innen, und seine Länge ist $|g(\boldsymbol{x})|$. Die Zahl $g(\boldsymbol{x})$ darf von allen Koordinaten abhängen, auf einer Kugelfläche also schwanken.

⁠**Beispiel:** $\boldsymbol{F}(x,y)=x\,\hat{\boldsymbol{e}}_r$ in der Ebene. Im Punkt $(1,0)$ ist $\hat{\boldsymbol{e}}_r=(1,0)$ und $g=1$, also $\boldsymbol{F}=(1,0)$. Im Punkt $(0,1)$ ist $g=0$, also $\boldsymbol{F}=0$. Im Punkt $(-1,0)$ ist $\hat{\boldsymbol{e}}_r=(-1,0)$ und $g=-1$, also $\boldsymbol{F}=(1,0)$: Der Pfeil zeigt dort zum Nullpunkt hin. Alle drei Punkte liegen auf dem Kreis mit Radius $1$, die Pfeile sind dort aber verschieden lang.

⁠**Kurz gesagt:** Ein Zentralfeld zeigt überall radial, seine Länge darf vom Ort abhängen.

### Radialsymmetrische Vektorfelder

<span class="anker" id="stufe-2-8"></span>

Beim Feld einer Punktladung zeigen die Pfeile nicht nur radial, sie sind auch auf jeder Kugelfläche gleich lang. Das ist eine stärkere Eigenschaft (Abb. [11](#abb-11)).

:::abbildung hm3/k1radial 11
Links: Eine radialsymmetrische Funktion liefert Zahlen, hier $u=r^2$ auf den Kreisen $r=1,2,3$. Mitte: Ein radialsymmetrisches Vektorfeld liefert radiale Vektoren, auf jedem Kreis gleich lang. Rechts: Ein Zentralfeld zeigt ebenfalls radial, ist auf einem Kreis aber verschieden lang.
:::

:::definition Definition 2.5 (Radialsymmetrisches Vektorfeld)
<span class="anker" id="satz-2-5"></span>

Ein Vektorfeld auf $\mathbb{R}^n\setminus\{0\}$ der Form

$$\boldsymbol{F}(\boldsymbol{x})=f(r)\,\hat{\boldsymbol{e}}_r,\qquad r=|\boldsymbol{x}|,$$

mit einer Funktion $f$ einer Variablen heißt __radialsymmetrisches Vektorfeld__.
:::

Ein radialsymmetrisches Vektorfeld ist ein Zentralfeld, bei dem die Zahl vor $\hat{\boldsymbol{e}}_r$ nur von $r$ abhängt. Jedes radialsymmetrische Vektorfeld ist also ein Zentralfeld. Umgekehrt ist nicht jedes Zentralfeld radialsymmetrisch: Das Feld $x\,\hat{\boldsymbol{e}}_r$ aus dem letzten Unterabschnitt ist auf dem Kreis mit Radius $1$ verschieden lang.

⁠**Beispiel:** Das Strahlfeld $\boldsymbol{x}=r\,\hat{\boldsymbol{e}}_r$ ist radialsymmetrisch mit $f(r)=r$. Das Feld $\boldsymbol{E}=\frac{Q}{4\pi r^2}\,\hat{\boldsymbol{e}}_r$ der Punktladung ist radialsymmetrisch mit $f(r)=\frac{Q}{4\pi r^2}$. Nach Satz [2.3](#satz-2-3) ist der Gradient jeder radialsymmetrischen Funktion ein radialsymmetrisches Vektorfeld.

:::hintergrund Ist $f(r)\,\hat{\boldsymbol{e}}_r$ dasselbe wie $f(r)$?
Nein. $f(r)$ ist eine Zahl, die Funktion $\boldsymbol{x}\mapsto f(r)$ ist eine radialsymmetrische Funktion. Erst der Faktor $\hat{\boldsymbol{e}}_r$ macht daraus einen Vektor, also ein Vektorfeld. Die Zahl $f(r)$ gibt dabei Länge und Sinn an: Für $f(r)<0$ zeigt der Vektor nach innen, und seine Länge ist $|f(r)|$.
:::

⁠**Kurz gesagt:** Ein radialsymmetrisches Vektorfeld zeigt überall radial und ist auf jeder Kugelfläche gleich lang.

### Radialsymmetrische Vektorfelder sind Gradientenfelder

<span class="anker" id="stufe-2-9"></span>

Hat jedes radialsymmetrische Feld ein Skalarpotential, und wie findet man es? Satz [2.3](#satz-2-3) sagt, wie man von einem Profil zu seinem Feld kommt. Man muss den Weg nur rückwärts gehen: Gesucht ist ein Profil, dessen Ableitung die Zahl $f(r)$ vor $\hat{\boldsymbol{e}}_r$ ist.

:::satz Satz 2.6 (Skalarpotential radialsymmetrischer Felder)
<span class="anker" id="satz-2-6"></span>

Jedes radialsymmetrische Vektorfeld $\boldsymbol{F}(\boldsymbol{x})=f(r)\,\hat{\boldsymbol{e}}_r$ mit einer auf $(0,\infty)$ stetigen Funktion $f$ ist ein Gradientenfeld $\boldsymbol{F}=\nabla\varphi$ auf $\mathbb{R}^n\setminus\{0\}$, mit

$$\varphi(\boldsymbol{x})=p(r),\qquad p(r)=\int f(r)\,\mathrm{d} r+\text{konst}.$$

Das heißt: $p$ ist eine beliebige Stammfunktion von $f$.
:::

:::beweis Satz [2.3](#satz-2-3) rückwärts
Weil $f$ stetig ist, hat es eine Stammfunktion $p$ mit $p'=f$. Nach [(2.2)](#gl-2-2) ist $\nabla p(r)=p'(r)\,\hat{\boldsymbol{e}}_r=f(r)\,\hat{\boldsymbol{e}}_r=\boldsymbol{F}$.
:::

⁠**Beispiel:** Das Feld $\boldsymbol{F}=\hat{\boldsymbol{e}}_r/r^2$ in $\mathbb{R}^3\setminus\{0\}$ hat $f(r)=1/r^2$. Eine Stammfunktion ist $p(r)=-1/r$, also ist $\varphi(\boldsymbol{x})=-1/r$ ein Skalarpotential. Zur Kontrolle: $\nabla(-1/r)=\frac1{r^2}\,\hat{\boldsymbol{e}}_r$. Das Strahlfeld $\boldsymbol{x}=r\,\hat{\boldsymbol{e}}_r$ hat das Skalarpotential $r^2/2$, wie in Unterabschnitt [1.23](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#stufe-1-23).

⁠**Kurz gesagt:** Ein radialsymmetrisches Feld $f(r)\,\hat{\boldsymbol{e}}_r$ hat als Skalarpotential eine Stammfunktion des Profils $f$, eingesetzt in $r$.

### Welche Zentralfelder Gradientenfelder sind

<span class="anker" id="stufe-2-10"></span>

Radialsymmetrische Felder sind Gradientenfelder. Gilt das für alle Zentralfelder? Nein, und zwar genau dann nicht, wenn sie nicht radialsymmetrisch sind.

Ein Zentralfeld steht senkrecht auf jeder Kurve, die auf einer Kugelfläche bleibt. Ist es ein Gradientenfeld, ändert sich sein Skalarpotential längs einer solchen Kurve nicht. Das Potential ist dann auf der Kugelfläche konstant, hängt also nur von $r$ ab, und damit auch die Länge des Felds.

:::satz Satz 2.7 (Zentralfelder und Gradientenfelder)
<span class="anker" id="satz-2-7"></span>

Sei $n\ge2$. Ein Zentralfeld $\boldsymbol{F}=g\,\hat{\boldsymbol{e}}_r$ mit einer stetigen Funktion $g$ auf $\mathbb{R}^n\setminus\{0\}$ ist genau dann ein Gradientenfeld, wenn es radialsymmetrisch ist.
:::

:::beweis Konstant auf Kugelflächen
Ist das Feld radialsymmetrisch, ist es nach Satz [2.6](#satz-2-6) ein Gradientenfeld.

Sei umgekehrt $g\,\hat{\boldsymbol{e}}_r=\nabla\varphi$ mit einer differenzierbaren Funktion $\varphi$. Sei $\gamma$ eine differenzierbare Kurve, die auf der Kugelfläche $|\boldsymbol{x}|=R$ bleibt. Aus $\gamma(t)\cdot\gamma(t)=R^2$ folgt durch Ableiten $2\,\gamma(t)\cdot\dot\gamma(t)=0$. Mit [(1.10)](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#gl-1-10) und $\hat{\boldsymbol{e}}_r=\gamma/R$ auf der Kugelfläche ist

$$\frac{\mathrm{d}}{\mathrm{d} t}\,\varphi\bigl(\gamma(t)\bigr)=\nabla\varphi\bigl(\gamma(t)\bigr)\cdot\dot\gamma(t)=\frac{g(\gamma(t))}{R}\,\gamma(t)\cdot\dot\gamma(t)=0 .$$

Also ist $\varphi$ längs jeder solchen Kurve konstant. Für $n\ge2$ lassen sich je zwei Punkte der Kugelfläche durch eine solche Kurve verbinden, also hat $\varphi$ auf der ganzen Kugelfläche denselben Wert. Das gilt für jeden Radius $R$, also ist $\varphi(\boldsymbol{x})=p(r)$ mit $p(r)=\varphi(r\,\hat{\boldsymbol{e}}_1)$. Die Funktion $p$ ist differenzierbar, weil $r\mapsto r\,\hat{\boldsymbol{e}}_1$ eine differenzierbare Kurve ist. Nach [(2.2)](#gl-2-2) ist $\nabla\varphi=p'(r)\,\hat{\boldsymbol{e}}_r$, und der Vergleich mit $g\,\hat{\boldsymbol{e}}_r$ gibt $g(\boldsymbol{x})=p'(r)$. Die Zahl vor $\hat{\boldsymbol{e}}_r$ hängt also nur von $r$ ab, das Feld ist radialsymmetrisch.
:::

⁠**Grenzfall:** Für $n=1$ besteht eine Kugelfläche aus zwei getrennten Punkten, und der Satz wird falsch. Auf $\mathbb{R}\setminus\{0\}$ ist $\hat{\boldsymbol{e}}_r=1$ für $x>0$ und $\hat{\boldsymbol{e}}_r=-1$ für $x<0$. Das Zentralfeld mit $g=1$ für $x>0$ und $g=2$ für $x<0$ ist $F(x)=1$ für $x>0$ und $F(x)=-2$ für $x<0$. Es hat das Skalarpotential $\varphi(x)=x$ für $x>0$ und $\varphi(x)=-2x$ für $x<0$, ist aber nicht radialsymmetrisch, denn bei $x=1$ und $x=-1$ ist $g$ verschieden.

**Übersicht.** Die drei Eigenschaften Zentralfeld, radialsymmetrisch und Gradientenfeld sind verschieden. Die Tabelle zeigt Beispiele in der Ebene und im Raum:

| Feld | Zentralfeld | radialsymmetrisch | Gradientenfeld |
|---|---|---|---|
| $\boldsymbol{x}=r\,\hat{\boldsymbol{e}}_r$ | ja | ja | ja, $\varphi=r^2/2$ |
| $\hat{\boldsymbol{e}}_r/r^2$ in $\mathbb{R}^3$ | ja | ja | ja, $\varphi=-1/r$ |
| $x\,\hat{\boldsymbol{e}}_r$ in $\mathbb{R}^2$ | ja | nein | nein, nach Satz [2.7](#satz-2-7) |
| $(2x,\,4y)$ | nein | nein | ja, $\varphi=x^2+2y^2$ |
| $(-y,\,x)$ | nein | nein | nein, nach Satz [1.15](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#satz-1-15) |

Zur letzten Zeile: Das Drehfeld hat nach Unterabschnitt [1.24](differenzierbarkeit-und-kettenregel-fur-abbildungen.html#stufe-1-24) keine symmetrische Jacobi-Matrix.

⁠**Kurz gesagt:** Ein Zentralfeld in mindestens zwei Dimensionen ist genau dann ein Gradientenfeld, wenn es auf jeder Kugelfläche gleich lang ist.

### Aufgaben

<span class="anker" id="stufe-2-11"></span>

:::aufgabe Aufgabe 7 ★ Radial oder nicht
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Berechne $\nabla u$ für $u(\boldsymbol{x})=\ln r$ auf $\mathbb{R}^2\setminus\{0\}$.

</li>

<li>

Finde ein Skalarpotential zu $\boldsymbol{F}(\boldsymbol{x})=r^2\,\hat{\boldsymbol{e}}_r$ auf $\mathbb{R}^n\setminus\{0\}$.

</li>

<li>

Ist $\boldsymbol{F}(x,y)=\dfrac yr\,\hat{\boldsymbol{e}}_r$ ein Gradientenfeld auf $\mathbb{R}^2\setminus\{0\}$? Begründe ohne Rechnung.

</li>

</ol>

:::loesung
(a) Das Profil ist $f(r)=\ln r$ mit $f'(r)=1/r$. Nach [(2.2)](#gl-2-2) ist $\nabla u=\frac1r\,\hat{\boldsymbol{e}}_r=\boldsymbol{x}/r^2=\dfrac{(x,\,y)}{x^2+y^2}$.

(b) Eine Stammfunktion von $r^2$ ist $r^3/3$. Nach Satz [2.6](#satz-2-6) ist $\varphi(\boldsymbol{x})=r^3/3$ ein Skalarpotential.

(c) Nein. Das Feld ist ein Zentralfeld mit $g(x,y)=y/r$. Auf einem Kreis mit Radius $R$ ist $g$ nicht konstant: Bei $(0,R)$ ist $g=1$, bei $(R,0)$ ist $g=0$. Das Feld ist also nicht radialsymmetrisch und nach Satz [2.7](#satz-2-7) kein Gradientenfeld.
:::
:::

:::aufgabe Aufgabe 8 ★★ Potentiale radialer Felder
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Gib ein Skalarpotential $\varphi$ von $\boldsymbol{F}(\boldsymbol{x})=\mathrm{e}^{-r}\,\hat{\boldsymbol{e}}_r$ auf $\mathbb{R}^3\setminus\{0\}$ an. Prüfe im Punkt $(1,2,2)$ komponentenweise, dass $\nabla\varphi=\boldsymbol{F}$ gilt.

</li>

<li>

In der Ebene sei $\boldsymbol{E}(\boldsymbol{x})=\hat{\boldsymbol{e}}_r/r$ auf $\mathbb{R}^2\setminus\{0\}$. Bestimme das Potential $u$ im Sinn der Physik, also $\boldsymbol{E}=-\nabla u$, mit $u=0$ auf dem Kreis $r=1$.

</li>

<li>

Berechne $\boldsymbol{E}$ und $u$ aus (b) im Punkt $(3,4)$.

</li>

</ol>

:::loesung
(a) Das Profil $\mathrm{e}^{-r}$ hat die Stammfunktion $p(r)=-\mathrm{e}^{-r}$, also ist $\varphi(\boldsymbol{x})=-\mathrm{e}^{-r}$ ein Skalarpotential. Kontrolle im Punkt $(1,2,2)$ mit $r=3$: Nach der Kettenregel und $\partial r/\partial x_j=x_j/r$ ist $\partial\varphi/\partial x_j=\mathrm{e}^{-r}x_j/r$, also

$$\nabla\varphi(1,2,2)=\frac{\mathrm{e}^{-3}}{3}\,(1,2,2)^T,\qquad\boldsymbol{F}(1,2,2)=\mathrm{e}^{-3}\,\hat{\boldsymbol{e}}_r=\mathrm{e}^{-3}\,\frac{(1,2,2)}{3}.$$

Beide stimmen überein.

(b) Gesucht ist $u$ mit $\nabla u=-\boldsymbol{E}=-\frac1r\,\hat{\boldsymbol{e}}_r$. Das ist ein radialsymmetrisches Feld mit dem Profil $-1/r$, eine Stammfunktion ist $-\ln r$. Also ist $u=-\ln r+c$, und aus $u=0$ bei $r=1$ folgt $c=0$: $u(\boldsymbol{x})=-\ln r$.

(c) Im Punkt $(3,4)$ ist $r=5$, $\boldsymbol{E}=\frac15\cdot\frac{(3,4)}{5}=\bigl(\tfrac3{25},\tfrac4{25}\bigr)=(0{,}12;\;0{,}16)$ und $u=-\ln5\approx-1{,}609$.
:::
:::
