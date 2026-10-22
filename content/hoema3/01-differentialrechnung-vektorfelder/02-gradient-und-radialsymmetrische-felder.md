---
title: Der Gradient, Gradientenfelder und radialsymmetrische Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010200
summary: Von Grund auf – der Gradient als Steigungspfeil einer Landschaft. Warum er in Richtung des steilsten Anstiegs zeigt und senkrecht auf den Höhenlinien steht, wie man die Steigung in jede Richtung als Schatten $\nabla f\cdot\vec v$ abliest, wann ein Pfeilfeld überhaupt zu einer echten Landschaft gehört (Gradientenfeld, Integrabilitätsbedingung, Wendeltreppe) und wie man für rotationssymmetrische Landschaften $u(\vec x)=h(r)$ sofort $\nabla u=h'(r)\,\vec e_r$ erhält – bis zum Coulomb-Feld. Mit Beispiel-Seite.
tags: Gradient, Richtungsableitung, Niveaufläche, Gradientenfeld, Skalarpotential, Integrabilitätsbedingung, radialsymmetrisch, Zentralfeld, Coulomb-Feld
---

## Anschaulich

Stell dir ein Skalarfeld $f$ als **Gebirgslandschaft** vor: Jedem Ort $\vec x$ der Landkarte ist eine Höhe $f(\vec x)$
zugeordnet. Auf der Karte sind die __Höhenlinien__ eingezeichnet — Linien, auf denen die Höhe überall gleich ist.

Ein Wanderer steht an einem Punkt und fragt sich zwei Dinge: *In welche Richtung geht es am steilsten bergauf?* Und
*wie steil ist es dort?*

Beide Antworten stecken in einem einzigen Pfeil, dem __Gradienten__ $\nabla f$. Er zeigt in die Richtung des
steilsten Anstiegs, und seine Länge ist die Steigung in genau dieser Richtung. Dieses Bild — Landschaft, Wanderer,
Steigungspfeil — begleitet uns durch den ganzen Artikel.

Zwei Dinge sieht man im Bild sofort. Der Pfeil steht **senkrecht** auf der Höhenlinie durch den Punkt, denn entlang
der Höhenlinie geht es weder hoch noch runter. Und er ist dort **lang**, wo die Höhenlinien dicht beieinander liegen
— am steilen Hang.

Dreht man die Idee um, wird es physikalisch: Aus einer Landschaft, einem __Potential__, entsteht ein Pfeilfeld, ein
__Kraftfeld__. So entstehen das elektrische Feld und das Gravitationsfeld. Am Ende führt eine besonders einfache,
rotationssymmetrische Landschaft direkt zum Feld einer Punktladung.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-gradient-landschaft · Vorlage: skalarfeld-hoehenlinien-2d
Eine farbige Höhenlandschaft $f$ mit Höhenlinien; ein Wanderer-Punkt wird über die Karte gezogen, an seiner Position
wächst der Gradient-Pfeil $\nabla f$ heraus — stets bergauf, senkrecht zur Höhenlinie, lang am steilen Hang (dichte
Linien), kurz im flachen Tal. Daneben das physikalische Gegenstück: eine Kugel rollt in Richtung $-\nabla f$ bergab.
(Rot = Gradient, orange = Bewegung der Kugel, grau = Höhenlinien.)
:::

## Wie steil ist es in meine Richtung? Die Richtungsableitung

Zuerst die Bühne: Im ganzen Artikel ist $U\subseteq\mathbb{R}^n$ eine offene Menge — das Gebiet, das die Landkarte
zeigt — und $f:U\to\mathbb{R}$ ein differenzierbares Skalarfeld, die Landschaft. Für eine echte Landkarte ist $n=2$.

Der Wanderer muss nicht in Gradientenrichtung laufen. Er kann jede Richtung wählen, beschrieben durch einen
__Einheitsvektor__ $\vec v\in\mathbb{R}^n$ — einen Pfeil der Länge $1$, der nur die Richtung angibt.

Wie steil es in diese Richtung geht, misst die __Richtungsableitung__. Der Wanderer läuft vom Punkt $\vec x_0\in U$
geradeaus in Richtung $\vec v$, und man schaut, wie schnell sich seine Höhe beim Losgehen ändert:

$$D_{\vec v} f(\vec x_0) := \frac{d}{dt}\, f(\vec x_0+t\,\vec v)\Big|_{t=0}.$$

**So liest man das:** $\vec x_0+t\,\vec v$ ist der Ort des Wanderers nach der Zeit $t$, wenn er mit Tempo $1$ in
Richtung $\vec v$ läuft; für kleine $t$ liegt er noch in $U$, weil $U$ offen ist. $f(\vec x_0+t\,\vec v)$ ist seine Höhe
zu diesem Zeitpunkt — eine Funktion der einen Variablen $t$. Ihre gewöhnliche Ableitung bei $t=0$ ist die Steigung, die
er beim Losgehen unter den Füßen spürt.

::::beispiel Richtungsableitung direkt aus der Definition
Für die elliptische Schüssel $f:\mathbb{R}^2\to\mathbb{R}$ mit

$$f(x,y) = x^2+2y^2$$

läuft der Wanderer vom Punkt $P=(1,1)$ diagonal nach Nordosten, in Richtung des Einheitsvektors

$$\vec v = \tfrac{1}{\sqrt2}\,(1,\,1).$$

Nach der Zeit $t$ ist er am Ort $P+t\,\vec v$, und seine Höhe ist

$$f\big(1+\tfrac{t}{\sqrt2},\ 1+\tfrac{t}{\sqrt2}\big) = \big(1+\tfrac{t}{\sqrt2}\big)^2+2\big(1+\tfrac{t}{\sqrt2}\big)^2 = 3\big(1+\tfrac{t}{\sqrt2}\big)^2.$$

Die gewöhnliche Ableitung bei $t=0$ ist die Richtungsableitung:

$$D_{\vec v}f(P) = 6\big(1+\tfrac{t}{\sqrt2}\big)\cdot\tfrac{1}{\sqrt2}\,\Big|_{t=0} = \frac{6}{\sqrt2} = 3\sqrt2 \approx 4{,}24.$$

**Im Bild:** Beim Losgehen nach Nordosten steigt der Weg mit der Rate $3\sqrt2$ — Höhe pro Wegstrecke. Das ist steil,
aber noch nicht der steilste mögliche Weg.
::::

Für die Koordinatenrichtungen, also $\vec v=\vec e_k$, ist das genau die partielle Ableitung nach $x_k$ (voriger
Artikel). Die Richtungsableitung verallgemeinert sie auf **jede** Richtung — und man muss dafür nichts Neues ausrechnen:

:::formel Satz
$$D_{\vec v} f(\vec x_0) = \nabla f(\vec x_0)\cdot\vec v = \lvert\nabla f(\vec x_0)\rvert\,\cos\theta.$$
:::

Dabei ist $\theta$ der Winkel zwischen dem Gradientenpfeil und der Laufrichtung $\vec v$.

**Im Bild:** Die Steigung, die der Wanderer spürt, ist der **Schatten** des Gradientenpfeils auf seine Laufrichtung.
Läuft er genau in Pfeilrichtung, ist der Schatten so lang wie der Pfeil selbst. Läuft er quer dazu, verschwindet der
Schatten. Unter der Lupe des vorigen Artikels ist die Landschaft eine schiefe Ebene, und deren Steigung in Richtung
$\vec v$ ist die Jacobi-Zeile, angewandt auf die Richtung:

$$D_{\vec v} f(\vec x_0) = Df(\vec x_0)\,\vec v.$$

:::herleitung
Der Weg des Wanderers ist eine Gerade, die er mit konstanter Geschwindigkeit durchläuft:

$$\vec\gamma(t) = \vec x_0+t\,\vec v, \qquad \dot{\vec\gamma}(t) = \vec v.$$

Die Kettenregel für ein Feld entlang einer Kurve (voriger Artikel) liefert für die Höhe längs dieses Weges

$$\frac{d}{dt}\,f(\vec x_0+t\,\vec v) = \nabla f(\vec x_0+t\,\vec v)\cdot\vec v.$$

Bei $t=0$ steht der Wanderer noch am Start — das ist genau die erste Form der Formel. Die zweite Form ist die
geometrische Deutung des Skalarprodukts (Betrag mal Betrag mal Kosinus des Zwischenwinkels), hier mit
$\lvert\vec v\rvert=1$.
:::

**Warum der Gradient bergauf zeigt.** Aus der Formel liest man den steilsten Anstieg sofort ab, denn der Kosinus ist
höchstens $1$. An einer Stelle mit $\nabla f(\vec x_0)\neq\vec 0$ gilt:

- In Gradientenrichtung ($\cos\theta=1$) ist die Steigung **maximal**, nämlich die Pfeillänge $\lvert\nabla f\rvert$.
  Der Gradient zeigt also bergauf, und seine Länge ist die größte Steigung, die es an diesem Punkt gibt.
- Genau entgegengesetzt ($\cos\theta=-1$) geht es am steilsten **bergab**.
- Quer zum Gradienten ($\cos\theta=0$) ändert sich die Höhe beim Losgehen **nicht**.

::::beispiel Steigungen in vier Richtungen
Am selben Punkt $P=(1,1)$ der Schüssel liefert der Satz alle Richtungsableitungen auf einmal. Gradient und Länge sind

$$\nabla f(x,y) = (2x,\;4y), \qquad \nabla f(P) = (2,\;4), \qquad \lvert\nabla f(P)\rvert = \sqrt{2^2+4^2} = \sqrt{20}.$$

Damit ergeben sich die Steigungen in vier Laufrichtungen:

| Laufrichtung | Einheitsvektor $\vec v$ | Steigung $D_{\vec v} f(P)$ |
|---|---|---|
| nach Osten | $(1,0)$ | $2$ |
| nach Norden | $(0,1)$ | $4$ |
| bergauf (Gradientenrichtung) | $\tfrac{1}{\sqrt5}(1,2)$ | $\sqrt{20}$, rund $4{,}47$ — das Maximum |
| entlang der Höhenlinie | $\tfrac{1}{\sqrt5}(-2,1)$ | $0$ |

Die Zeile „bergauf" im Einzelnen:

$$D_{\vec v} f(P) = (2,4)\cdot\tfrac{1}{\sqrt5}(1,2) = \frac{2+8}{\sqrt5} = \frac{10}{\sqrt5} = \sqrt{20}.$$

Auch die Richtung nach Nordosten, die oben mühsam per Definition gerechnet wurde, kommt jetzt mit einem einzigen
Skalarprodukt heraus:

$$(2,4)\cdot\tfrac{1}{\sqrt2}(1,1) = \frac{6}{\sqrt2} = 3\sqrt2.$$

**Im Bild:** Nach Norden ist es doppelt so steil wie nach Osten — die Schüssel ist in $y$-Richtung enger gekrümmt,
ihre Höhenlinien (Ellipsen) liegen dort dichter. Der steilste Weg führt schräg bergauf, mehr nach Norden als nach
Osten, und ist mit $\sqrt{20}$ steiler als der Weg nach Nordosten. Genau quer dazu verläuft die Höhenlinie durch $P$.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-richtungsableitung-schatten · Vorlage: gradient-projektion-2d
Am Punkt $P=(1,1)$ der elliptischen Schüssel $f=x^2+2y^2$ (Höhenlinien als Ellipsen) steht der Gradientenpfeil
$(2,4)$. Ein drehbarer Einheitspfeil $\vec v$ (Kompassnadel) kreist um $P$; der Schatten des Gradienten auf $\vec v$
wird als Balken angezeigt, seine Länge ist $D_{\vec v} f(P)$ — maximal parallel zum Gradienten, null tangential zur
Höhenlinie, negativ in Gegenrichtung. (Rot = Gradient, orange = Laufrichtung $\vec v$ und Schatten, grau = Höhenlinien.)
:::
::::

## Höhenlinien und Niveauflächen: der Gradient steht senkrecht

Eine __Niveaufläche__ ist die Menge aller Punkte mit gleichem Feldwert $c$ — in der Ebene eine __Niveaulinie__ (die
Höhenlinie), im Raum eine Fläche, etwa eine Äquipotentialfläche:

$$N_c = \{\,\vec x\in U \;:\; f(\vec x)=c\,\}.$$

Der Gradient steht in jedem Punkt **senkrecht** auf der Niveaufläche durch diesen Punkt.

**Im Bild:** Wer genau auf der Höhenlinie wandert, bleibt auf gleicher Höhe. Sein Schritt hat deshalb keinen Anteil in
Gradientenrichtung — der Schatten des Gradienten auf seine Laufrichtung ist null.

:::herleitung
Läuft man mit einer Kurve $\vec\gamma$ **innerhalb** einer Niveaufläche, ändert sich der Feldwert nicht. Mit der
Kettenregel heißt das

$$0 = \frac{d}{dt}\,f(\vec\gamma(t)) = \nabla f(\vec\gamma(t))\cdot\dot{\vec\gamma}(t).$$

Die Geschwindigkeit $\dot{\vec\gamma}$ kann dabei **jede** Richtung annehmen, die in der Fläche liegt — jede
Tangentialrichtung. Das Skalarprodukt mit $\nabla f$ ist für alle diese Richtungen null. Also steht $\nabla f$
senkrecht auf der ganzen Fläche.
:::

**Genau genommen** gilt das an Stellen mit $\nabla f(\vec x)\neq\vec 0$. Dort ist die Niveaufläche nahe $\vec x$ wirklich
eine glatte Fläche, durch deren Tangentialrichtungen Kurven laufen (das sichert der Satz über implizite Funktionen).
Wo der Gradient null ist, etwa im Sattelpunkt einer Sattelfläche, können sich Niveaulinien sogar kreuzen.

::::beispiel Die Höhenlinie der Schüssel durch $P$
Durch $P=(1,1)$ läuft die Höhenlinie der Schüssel zur Höhe $3$, eine Ellipse:

$$N_3 = \{\,(x,y)\in\mathbb{R}^2 \;:\; x^2+2y^2=3\,\}.$$

Ein Wanderer kann sie mit der Kurve

$$\vec\gamma(t) = \big(\sqrt3\cos t,\ \sqrt{\tfrac32}\,\sin t\big)$$

umrunden; er bleibt dabei auf der Höhe $3$:

$$f(\vec\gamma(t)) = 3\cos^2t+2\cdot\tfrac32\sin^2t = 3.$$

Durch $P$ kommt er zu der Zeit $t$ mit

$$\cos t = \tfrac{1}{\sqrt3}, \qquad \sin t = \sqrt{\tfrac23}.$$

Dort ist seine Geschwindigkeit

$$\dot{\vec\gamma}(t) = \big(-\sqrt3\sin t,\ \sqrt{\tfrac32}\cos t\big) = \big(-\sqrt2,\ \tfrac{1}{\sqrt2}\big),$$

und sie steht senkrecht auf dem Gradienten:

$$\nabla f(P)\cdot\dot{\vec\gamma} = (2,4)\cdot\big(-\sqrt2,\ \tfrac{1}{\sqrt2}\big) = -2\sqrt2+2\sqrt2 = 0.$$

**Im Bild:** Die Laufrichtung $\big(-\sqrt2,\tfrac{1}{\sqrt2}\big)$ ist ein Vielfaches von $(-2,1)$ — genau die Richtung
„entlang der Höhenlinie" aus der Tabelle der vier Richtungen. Der Gradient $(2,4)$ zeigt quer dazu nach außen, den Hang
der Schüssel hinauf.
::::

**Im Bild, quantitativ:** Je dichter die Höhenlinien, desto länger der Pfeil. Liegen zwei Höhenlinien mit
Höhenunterschied $\Delta c$ im kleinen Abstand $\Delta s$ voneinander, so ist die Steigung quer zu ihnen ungefähr

$$\lvert\nabla f\rvert \approx \frac{\Delta c}{\Delta s}.$$

So liest man auf jeder Wanderkarte die Steilheit ab, ohne zu rechnen: Höhenunterschied geteilt durch den Abstand der
Linien.

:::herleitung
Man geht von einer Höhenlinie den kleinen Abstand $\Delta s$ quer zu ihr, also in Gradientenrichtung, bis zur nächsten.
Mit dem Einheitsvektor $\vec v=\nabla f/\lvert\nabla f\rvert$ ist die Steigung in dieser Richtung nach dem Satz über die
Richtungsableitung

$$D_{\vec v}f = \nabla f\cdot\frac{\nabla f}{\lvert\nabla f\rvert} = \lvert\nabla f\rvert.$$

Auf der kurzen Strecke ändert sich die Höhe deshalb ungefähr um $\lvert\nabla f\rvert\,\Delta s$ — und diese Änderung ist
gerade der Höhenunterschied $\Delta c$ der beiden Linien. Auflösen nach $\lvert\nabla f\rvert$ gibt die Formel; sie wird
umso genauer, je dichter die Linien liegen.
:::

::::beispiel Die Steilheit von der Wanderkarte ablesen
Auf einer Wanderkarte sind die Höhenlinien im Abstand von $10$ Höhenmetern gezeichnet. An einer Stelle liegen zwei
benachbarte Linien $50$ Meter auseinander. Dann ist dort ungefähr

$$\lvert\nabla f\rvert \approx \frac{\Delta c}{\Delta s} = \frac{10\ \text{m}}{50\ \text{m}} = 0{,}2.$$

Der Weg quer zu den Linien steigt also um $20\,\%$ — auf $100$ Meter Strecke $20$ Höhenmeter. An einer Stelle mit nur
$25$ Metern Linienabstand wäre es doppelt so steil.

**Im Bild:** Halber Linienabstand, doppelte Steigung — der Gradientenpfeil wird doppelt so lang.
::::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-hoehenlinien-dichte · Vorlage: hoehenlinien-abstand-2d
Zwei Kartenausschnitte nebeneinander: links dicht liegende Höhenlinien mit langem Gradientenpfeil (steiler Hang),
rechts weit auseinanderliegende mit kurzem Pfeil (flaches Tal); eingezeichnet $\Delta c$ und $\Delta s$. An einer
Höhenlinie ein tangentialer Schritt $\dot{\vec\gamma}$ (keine Höhenänderung) und der senkrecht darauf stehende
Gradient. (Rot = Gradient, orange = Tangentialschritt, grau = Höhenlinien.)
:::

## Gradientenfelder: Landschaft und Steigungspfeile

Jetzt drehen wir die Blickrichtung um. Bisher war die Landschaft gegeben, und wir haben ihre Steigungspfeile
abgelesen. Ein Vektorfeld, das genau so entsteht, heißt __Gradientenfeld__:

:::formel Definition
$$\vec E = \nabla\phi.$$
:::

Dabei ist $\phi:U\to\mathbb{R}$ ein differenzierbares Skalarfeld — die **Landschaft** —, und $\vec E:U\to\mathbb{R}^n$
ist das Feld ihrer **Steigungspfeile**. Man nennt $\phi$ ein __Skalarpotential__ von $\vec E$.

::::beispiel Ein Gradientenfeld und seine Potentiale
Die Sattelfläche $\phi:\mathbb{R}^2\to\mathbb{R}$ mit

$$\phi(x,y) = xy$$

hat die Steigungspfeile

$$\nabla\phi(x,y) = (y,\;x).$$

Das Feld

$$\vec F(x,y) = (y,\;x)$$

ist also ein Gradientenfeld mit dem Potential $\phi$. Ebenso gut ist $\phi+5$ ein Potential, denn die Konstante fällt
beim Ableiten weg:

$$\nabla(xy+5) = (y,\;x) = \vec F.$$

**Im Bild:** Am Punkt $(1,2)$ zeigt der Steigungspfeil $(2,1)$ — dort geht es nach Osten doppelt so steil bergauf wie
nach Norden. Ob die ganze Sattelfläche fünf Meter höher liegt oder nicht, ändert an diesem Pfeil nichts.
::::

**Ein Potential ist nie eindeutig.** Hebt man die ganze Landschaft um eine Konstante an, ändert sich keine einzige
Steigung, denn der Gradient einer Konstanten ist null. Mit $\phi$ ist also auch $\phi+c$ ein Potential desselben Feldes,
für jede Konstante $c$.

**Die physikalische Konvention.** In der Physik schreibt man meist

$$\vec E = -\nabla\varphi.$$

**Im Bild:** Das Feld zeigt dann nicht bergauf, sondern **bergab** — wie eine Kugel, die den Hang hinunterrollt.
Dabei nimmt die potentielle Energie einer positiven Ladung ab. Läuft ein Teilchen entlang einer Feldlinie $\vec\gamma$,
also mit einer Geschwindigkeit $\dot{\vec\gamma}$ in Feldrichtung, so liefert die Kettenregel

$$\frac{d}{dt}\,\varphi(\vec\gamma(t)) = \nabla\varphi\cdot\dot{\vec\gamma} = -\vec E\cdot\dot{\vec\gamma} < 0.$$

Der Ausdruck ist negativ, weil $\vec E$ und $\dot{\vec\gamma}$ in dieselbe Richtung zeigen. Für den bloßen **Begriff**
Gradientenfeld ist das Vorzeichen egal: $\vec E$ ist genau dann ein Gradientenfeld, wenn $-\vec E$ eines ist.

::::beispiel Bergab mit der Physik-Konvention
Als physikalisches Potential nehmen wir eine Schüssel, $\varphi:\mathbb{R}^2\to\mathbb{R}$ mit

$$\varphi(x,y) = x^2+y^2.$$

Das Feld der Physik zeigt bergab, zum Mittelpunkt hin:

$$\vec E = -\nabla\varphi = (-2x,\ -2y).$$

Eine __Feldlinie__ ist eine Kurve, die überall in Feldrichtung läuft — ihre Geschwindigkeit ist der Feldpfeil an ihrem
Ort. Vom Punkt $(1,0)$ aus ist das

$$\vec\gamma(t) = (e^{-2t},\ 0), \qquad \dot{\vec\gamma}(t) = (-2e^{-2t},\ 0) = \vec E(\vec\gamma(t)).$$

Längs dieser Feldlinie nimmt das Potential ab:

$$\varphi(\vec\gamma(t)) = e^{-4t}, \qquad \frac{d}{dt}\,\varphi(\vec\gamma(t)) = -4e^{-4t} < 0.$$

Genau das liefert die Kettenregel mit $-\vec E\cdot\dot{\vec\gamma}$:

$$-\vec E(\vec\gamma(t))\cdot\dot{\vec\gamma}(t) = -\big((-2e^{-2t})^2+0\big) = -4e^{-4t}.$$

**Im Bild:** Ein Teilchen, das stets in Feldrichtung wandert, gleitet zum Grund der Schüssel und verliert dabei
ständig potentielle Energie. Es kommt dem Mittelpunkt immer näher, ohne ihn je zu erreichen.
::::

## Echte oder unmögliche Landschaft? Die Integrabilitätsbedingung

Nicht jedes Pfeilfeld gehört zu einer Landschaft. Man kann Pfeile zeichnen, die eine **unmögliche Treppe** im Stil
von Escher beschreiben würden: Man läuft im Kreis, folgt dabei immer den Pfeilen bergauf — und kommt trotzdem wieder
am Start an. Eine echte Landschaft kann das nicht.

Gibt es einen einfachen **lokalen Test**, der solche unmöglichen Pfeilfelder entlarvt? Ja. Für ein Gradientenfeld mit
zweimal stetig differenzierbarem Potential $\phi$ gilt:

:::formel Lemma
$$\vec E=\nabla\phi \quad\Longrightarrow\quad \frac{\partial E_j}{\partial x_k} = \frac{\partial E_k}{\partial x_j} \quad\text{für alle } j,k.$$
:::

Gelesen: Die Jacobi-Matrix $D\vec E$ eines Gradientenfelds ist **symmetrisch** — an der Diagonale gespiegelte
Einträge sind gleich. Diese Aussage heißt __Integrabilitätsbedingung__.

**Im Bild (in der Ebene):** $E_1$ ist die Steigung nach Osten, $E_2$ die Steigung nach Norden. Die linke Seite fragt:
Wie ändert sich die Ost-Steigung, wenn man nach Norden geht? Die rechte Seite fragt: Wie ändert sich die
Nord-Steigung, wenn man nach Osten geht? In einer echten Landschaft beschreiben beide dieselbe **Verwindung** des
Hangs — sie müssen übereinstimmen.

:::herleitung
Ist $\vec E=\nabla\phi$, so ist jede Komponente eine partielle Ableitung des Potentials:

$$E_j = \frac{\partial\phi}{\partial x_j}.$$

Die Einträge der Jacobi-Matrix von $\vec E$ sind damit **zweite** Ableitungen des Potentials:

$$\frac{\partial E_j}{\partial x_k} = \frac{\partial^2\phi}{\partial x_k\,\partial x_j}, \qquad \frac{\partial E_k}{\partial x_j} = \frac{\partial^2\phi}{\partial x_j\,\partial x_k}.$$

Nach dem __Satz von Schwarz__ (voriger Artikel) sind diese beiden gemischten Ableitungen gleich. Im Bild: Beide Seiten
messen dieselbe Verwindung der Landschaft, nur von zwei Seiten aus betrachtet.
:::

::::beispiel Der Test an zwei Feldern
**(a) Bestanden.** Für das Feld der Sattelfläche

$$\vec F(x,y) = (y,\;x)$$

sind die gespiegelten Einträge der Jacobi-Matrix gleich:

$$\frac{\partial F_1}{\partial y} = 1 = \frac{\partial F_2}{\partial x}.$$

Das muss so sein, denn $\vec F$ ist das Gradientenfeld von $xy$.

**(b) Durchgefallen.** Für das kreisende Feld

$$\vec G(x,y) = (-y,\;x)$$

sind sie verschieden:

$$\frac{\partial G_1}{\partial y} = -1 \;\neq\; 1 = \frac{\partial G_2}{\partial x}.$$

Also ist $\vec G$ **kein** Gradientenfeld. **Im Bild:** Die Pfeile kreisen gegen den Uhrzeigersinn um den Ursprung.
Wären es Steigungspfeile, ginge es beim Umlaufen ständig bergauf, und man käme trotzdem am Start an — genau die
unmögliche Escher-Treppe.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-echt-vs-unmoeglich · Vorlage: escher-vs-landschaft-2d
Zwei Pfeilfelder nebeneinander: links $\vec F=(y,x)$ als Steigungspfeile der Sattelfläche $\phi=xy$ (echte Landschaft,
Test bestanden: $1=1$), rechts das kreisende Feld $\vec G=(-y,x)$ als „Escher-Treppe" (Test fällt durch: $-1\neq1$). Ein
Wanderer umrundet in beiden Feldern einen Kreis: links heben sich die Höhenänderungen zu null auf, rechts geht es auf
dem ganzen Weg bergauf. Kernaussage: Die Integrabilitätsbedingung entlarvt unmögliche Landschaften. (Rot = echte
Landschaft/Potential, orange = Pfeilfeld, grau = Höhenlinien.)
:::
::::

**Stolperstein — notwendig, aber nicht hinreichend.** Die Bedingung ist nur ein **lokaler** Test: Sie prüft die
Verwindung an jeder Stelle einzeln. Hat das Gebiet ein **Loch**, kann ein Feld den Test überall bestehen und trotzdem
keine Landschaft besitzen.

**Im Bild:** eine **Wendeltreppe** um eine Säule. Jede einzelne Stufe ist ein ganz normaler Hang, doch wer einmal um die
Säule herumgeht, steht eine Etage höher. Das geht nur, weil man die Säule nicht betreten kann — das Gebiet hat dort ein
Loch.

::::beispiel Die Wendeltreppe: Test bestanden, trotzdem keine Landschaft
Auf der Ebene ohne Ursprung, $\mathbb{R}^2\setminus\{\vec 0\}$, betrachten wir das Feld

$$\vec W(x,y) = \frac{1}{x^2+y^2}\,(-y,\;x).$$

Es erfüllt die Integrabilitätsbedingung überall:

$$\frac{\partial W_1}{\partial y} = \frac{y^2-x^2}{(x^2+y^2)^2} = \frac{\partial W_2}{\partial x}.$$

:::herleitung
Mit der Abkürzung $\rho$ für das Abstandsquadrat lauten die Komponenten

$$\rho = x^2+y^2, \qquad W_1 = -\frac{y}{\rho}, \qquad W_2 = \frac{x}{\rho}.$$

Mit den Ableitungen des Abstandsquadrats

$$\frac{\partial\rho}{\partial y} = 2y, \qquad \frac{\partial\rho}{\partial x} = 2x$$

liefert die Quotientenregel

$$\frac{\partial W_1}{\partial y} = -\frac{\rho - y\cdot 2y}{\rho^2} = \frac{y^2-x^2}{\rho^2}, \qquad \frac{\partial W_2}{\partial x} = \frac{\rho - x\cdot 2x}{\rho^2} = \frac{y^2-x^2}{\rho^2}.$$

Beide Ausdrücke stimmen überein — auf der ganzen gelochten Ebene.
:::

Trotzdem besitzt $\vec W$ dort **kein** Potential: Ein Umlauf um den Ursprung gewinnt die Höhe $2\pi$, obwohl man wieder
am Start steht.

:::herleitung
Angenommen, es gäbe doch ein Potential $\phi$ mit $\nabla\phi=\vec W$. Ein Wanderer umrundet den Ursprung auf dem
Einheitskreis:

$$\vec\gamma(t) = (\cos t,\ \sin t), \qquad \dot{\vec\gamma}(t) = (-\sin t,\ \cos t), \qquad 0\le t\le 2\pi.$$

Auf dem Kreis ist der Nenner von $\vec W$ gleich $1$, also

$$\vec W(\vec\gamma(t)) = (-\sin t,\ \cos t).$$

Die Kettenregel gibt die Höhenänderung pro Zeit:

$$\frac{d}{dt}\,\phi(\vec\gamma(t)) = \vec W(\vec\gamma(t))\cdot\dot{\vec\gamma}(t) = \sin^2t+\cos^2t = 1.$$

Die Höhe wächst also gleichmäßig mit der Rate $1$; nach einer Runde ist sie um $2\pi$ gestiegen. Der Wanderer steht aber
wieder am Start, wo die Höhe dieselbe sein müsste — ein Widerspruch. Also gibt es kein Potential.
:::

**Im Bild:** $\vec W$ ist genau die Wendeltreppe. Jede Stufe ist ein normaler Hang (der Test passt überall), doch jede
Runde um die Säule im Ursprung bringt die Höhe $2\pi$. Im Artikel [Das Kurvenintegral und die Orientierung](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegral-und-orientierung.html)
wird diese Rechnung zum allgemeinen Werkzeug.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-wendeltreppe · Vorlage: wendeltreppe-loch-2d
Das Feld $\vec W$ um ein Loch im Ursprung als Wendeltreppe um eine Säule. Ein Wanderer umrundet die Säule auf dem
Einheitskreis; ein Zähler summiert die Höhenänderungen und zeigt nach einer Runde $2\pi$, obwohl der Wanderer wieder am
Start steht. Ein Umschalter zeigt die Verwindung an einzelnen Stellen: überall passt der Test. Kernaussage: Ohne Loch im
Gebiet wäre so eine Treppe unmöglich. (Orange = Pfeilfeld, rot = Weg des Wanderers, grau = Säule/Loch.)
:::
::::

In drei Dimensionen ist die Symmetrie der Jacobi-Matrix gleichbedeutend mit „Rotation gleich null" — dem Wirbel-Maß
des nächsten Artikels. Wann die Bedingung doch ausreicht (bei Gebieten ohne Löcher), klärt das
[Poincaré-Lemma](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/poincare-lemma.html).

## Rotationssymmetrische Landschaften

In der Feldtheorie hängen viele Größen nur vom **Abstand** zu einem Zentrum ab — etwa das Potential einer
Punktladung. Eine __radialsymmetrische Funktion__ auf $\mathbb{R}^n\setminus\{\vec 0\}$ hat die Form

$$u(\vec x) = h(r), \qquad r := \lvert\vec x\rvert = \sqrt{x_1^2+\cdots+x_n^2}.$$

**So liest man das:** $r$ ist der Abstand des Punktes $\vec x$ vom Ursprung, also eine Zahl. Die Funktion
$h:(0,\infty)\to\mathbb{R}$ ist eine gewöhnliche Funktion **einer** Variablen — das __Höhenprofil__, das man sieht, wenn
man vom Zentrum geradeaus nach außen läuft.

**Im Bild:** eine rotationssymmetrische Landschaft — eine Schüssel, ein Kegel, ein Vulkan. Die Höhenlinien sind Kreise
(im Raum: Kugeln) um das Zentrum. Weil der Gradient senkrecht auf den Höhenlinien steht, muss er überall **radial**
zeigen: direkt zum Zentrum hin oder von ihm weg.

**Der einfachste Fall: die Abstandsfunktion selbst.** Die Funktion $r$ ist ein Kegel mit Spitze im Ursprung. Läuft man
einen Schritt nach außen, wächst der Abstand um genau diesen Schritt — die Steigung nach außen ist überall $1$. Ihr
Gradient ist deshalb ein **Einheitspfeil nach außen**:

$$\nabla r = \frac{\vec x}{r} =: \vec e_r.$$

Das Feld $\vec e_r$ heißt __radialer Einheitsvektor__. Es zeigt an jedem Punkt außer dem Ursprung radial nach außen
und hat die Länge $1$.

:::herleitung
Nach der Kettenregel ist für jede Koordinate

$$\frac{\partial r}{\partial x_j} = \frac{\partial}{\partial x_j}\sqrt{x_1^2+\cdots+x_n^2} = \frac{1}{2\sqrt{x_1^2+\cdots+x_n^2}}\cdot 2x_j = \frac{x_j}{r}.$$

Fasst man die $n$ Komponenten zu einem Vektor zusammen, entsteht $\vec x/r$. Seine Länge ist $\lvert\vec x\rvert/r$,
also $1$.
:::

::::beispiel Der Kegel $r$ in Zahlen
Am Punkt $\vec x=(3,4)$ der Ebene ist der Abstand zum Ursprung

$$r = \sqrt{3^2+4^2} = 5.$$

Die partiellen Ableitungen der Abstandsfunktion sind dort

$$\frac{\partial r}{\partial x_1} = \frac{x_1}{r} = \frac35, \qquad \frac{\partial r}{\partial x_2} = \frac{x_2}{r} = \frac45,$$

zusammen also

$$\nabla r(3,4) = \big(\tfrac35,\ \tfrac45\big) = \vec e_r, \qquad \lvert\vec e_r\rvert = \sqrt{\tfrac{9}{25}+\tfrac{16}{25}} = 1.$$

**Im Bild:** Der Pfeil zeigt genau vom Ursprung weg, in Richtung des Punktes $(3,4)$, und hat die Länge $1$: Geht man
einen Meter nach außen, ist man einen Meter weiter vom Zentrum entfernt.
::::

Mit einer weiteren Anwendung der Kettenregel folgt die Gradientenformel für **jede** rotationssymmetrische
Landschaft. Ist das Höhenprofil $h:(0,\infty)\to\mathbb{R}$ differenzierbar, so gilt auf $\mathbb{R}^n\setminus\{\vec 0\}$:

:::formel Satz
$$u(\vec x)=h(r) \quad\Longrightarrow\quad \nabla u = h'(r)\,\vec e_r.$$
:::

**Im Bild:** Der Gradient zeigt radial, und seine Länge ist die Steigung des Höhenprofils, $\lvert h'(r)\rvert$.
Steigt die Landschaft nach außen an wie eine Schüssel ($h'>0$), zeigt er nach außen. Fällt sie nach außen ab wie ein
Berg ($h'<0$), zeigt er nach innen — zum Gipfel hin.

:::herleitung
$u$ ist die Verkettung der Abstandsfunktion $\vec x\mapsto r$ mit dem Höhenprofil $r\mapsto h(r)$. Die Kettenregel
gibt „äußere Ableitung mal innere Ableitung":

$$\nabla u = h'(r)\,\nabla r = h'(r)\,\vec e_r.$$
:::

::::beispiel Die Schüssel $\tfrac12 r^2$
Für die Schüssel

$$u(\vec x) = \tfrac12\,r^2 = \tfrac12\,\lvert\vec x\rvert^2$$

ist das Höhenprofil eine Parabel, und die Gradientenformel liefert

$$h(r) = \tfrac12\,r^2, \qquad h'(r) = r, \qquad \nabla u = r\,\vec e_r = r\cdot\frac{\vec x}{r} = \vec x.$$

Zur Probe schreibt man $u$ in Koordinaten aus und leitet direkt ab:

$$u = \tfrac12\big(x_1^2+\cdots+x_n^2\big), \qquad \frac{\partial u}{\partial x_j} = x_j, \qquad \nabla u = \vec x.$$

**Im Bild:** Die Steigungspfeile zeigen überall nach außen und werden linear mit dem Abstand länger — je weiter vom
Zentrum, desto steiler die Schüssel.
::::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-radialformel · Vorlage: radialfeld-schuessel-2d
Eine rotationssymmetrische Landschaft $u(\vec x)=h(r)$ als „Schüssel" über der Ebene; die Höhenlinien sind
konzentrische Kreise. Ein Schieberegler blendet das Höhenprofil $h(r)$ entlang eines Radius ein; der Gradient
$\nabla u=h'(r)\vec e_r$ zeigt radial (nach außen für $h'>0$) und steht senkrecht auf den Kreisen. Daneben der Kegel
$r$ mit Steigung $1$ und seinem Einheitspfeil $\vec e_r$. (Rot = Gradient, orange = Höhenprofil, grau = Höhenkreise.)
:::

## Zentralfelder und das Coulomb-Feld

Ein __Zentralfeld__ ist ein Vektorfeld auf $\mathbb{R}^n\setminus\{\vec 0\}$, dessen Pfeile überall radial zeigen:

$$\vec F(\vec x) = g(\vec x)\,\vec e_r.$$

Die skalare Funktion $g:\mathbb{R}^n\setminus\{\vec 0\}\to\mathbb{R}$ gibt an, wie lang der Pfeil ist und ob er nach
außen ($g>0$) oder innen ($g<0$) zeigt. Hängt diese Länge nur vom Abstand ab, heißt das Feld __radialsymmetrisch__:

$$\vec F(\vec x) = s(r)\,\vec e_r.$$

Die Funktion $s:(0,\infty)\to\mathbb{R}$ heißt hier __Feldprofil__ — die Feldstärke im Abstand $r$.

Radialsymmetrische Felder sind **immer** Gradientenfelder, und die passende Landschaft findet man durch eine einzige
eindimensionale Integration. Ist $s$ stetig auf $(0,\infty)$, so gilt auf $\mathbb{R}^n\setminus\{\vec 0\}$:

:::formel Satz
$$\vec F=s(r)\,\vec e_r \quad\Longrightarrow\quad \vec F=\nabla\phi \quad\text{mit}\quad \phi(\vec x)=h(r),\ \ h'=s.$$
:::

Gelesen: Das Höhenprofil $h$ der gesuchten Landschaft ist eine **Stammfunktion** des Feldprofils $s$. Im Bild: Die
Steigung des Profils soll ja gerade die Pfeillänge sein — also muss man die Pfeillängen entlang des Radius
aufsummieren, um die Höhe zu erhalten.

:::herleitung
Weil $s$ stetig ist, hat es nach dem Hauptsatz der Differential- und Integralrechnung eine Stammfunktion $h$. Nach der
Gradientenformel für rotationssymmetrische Landschaften ist dann

$$\nabla\big(h(r)\big) = h'(r)\,\vec e_r = s(r)\,\vec e_r = \vec F.$$

Der Ursprung muss ausgenommen werden, weil $\vec e_r$ dort nicht definiert ist. Die Stammfunktion ist nur bis auf eine
Konstante bestimmt — das ist wieder das Anheben der ganzen Landschaft.
:::

::::beispiel Ein Potential durch Integrieren finden
Gesucht ist ein Potential für das radialsymmetrische Feld auf $\mathbb{R}^2\setminus\{\vec 0\}$ mit der Feldstärke
$1/r$:

$$\vec F(\vec x) = \frac1r\,\vec e_r = \frac{\vec x}{r^2}.$$

Das Feldprofil ist $1/r$, und eine Stammfunktion davon ist der natürliche Logarithmus:

$$s(r) = \frac1r, \qquad h(r) = \ln r, \qquad h'(r) = \frac1r = s(r).$$

Also ist

$$\phi(\vec x) = \ln r = \ln\lvert\vec x\rvert$$

ein Potential. Die Probe mit der Gradientenformel bestätigt das:

$$\nabla\ln r = \frac1r\,\vec e_r = \vec F.$$

**Im Bild:** Die Landschaft ist ein Trichter, der zum Zentrum hin unbegrenzt abfällt; seine Steigung $1/r$ wird nach
außen immer flacher. Bis auf Konstanten und das Vorzeichen der Physik-Konvention ist das die Landschaft eines langen
geladenen Drahts, im Querschnitt betrachtet.
::::

**Auch die Umkehrung gilt** (für $n\ge2$): Ist ein Zentralfeld ein Gradientenfeld, dann ist es automatisch
radialsymmetrisch. **Im Bild:** Zeigen alle Steigungspfeile radial, so geht es auf jeder Kugel um den Ursprung weder
hoch noch runter. Die Landschaft hat auf jeder Kugel überall dieselbe Höhe — sie ist rotationssymmetrisch.

:::herleitung
Angenommen, das Zentralfeld ist ein Gradientenfeld:

$$\vec F = g(\vec x)\,\vec e_r = \nabla\phi.$$

Sei $\vec\gamma$ eine beliebige Kurve, die ganz auf einer Kugel um den Ursprung verläuft. Ihre Geschwindigkeit
$\dot{\vec\gamma}$ ist tangential zur Kugel, steht also senkrecht auf $\vec e_r$. Die Kettenregel gibt

$$\frac{d}{dt}\,\phi(\vec\gamma(t)) = \nabla\phi\cdot\dot{\vec\gamma} = g\,\vec e_r\cdot\dot{\vec\gamma} = 0.$$

Also ist $\phi$ längs jeder solchen Kurve konstant. Für $n\ge2$ lassen sich je zwei Punkte der Kugel durch so eine
Kurve verbinden — $\phi$ hat auf der ganzen Kugel denselben Wert und hängt nur vom Radius ab:

$$\phi(\vec x) = h(r) \qquad\text{mit dem Profil}\qquad h(r) := \phi(r\,\vec e_1).$$

Das Profil ist differenzierbar, weil $\phi$ es ist. Nach der Gradientenformel ist dann $\nabla\phi=h'(r)\,\vec e_r$ — das
Feld ist radialsymmetrisch mit dem Feldprofil $h'$.
:::

::::beispiel Ein Zentralfeld ohne Landschaft
Das Zentralfeld auf $\mathbb{R}^2\setminus\{\vec 0\}$ mit der Pfeillänge $g(\vec x)=x_1$,

$$\vec F(\vec x) = x_1\,\vec e_r = \Big(\frac{x_1^2}{r},\ \frac{x_1x_2}{r}\Big),$$

ist nicht radialsymmetrisch: Auf dem Einheitskreis zeigt es am rechten Rand nach außen und am linken Rand nach innen,
jeweils mit der Länge $1$. Nach der Umkehrung kann es deshalb kein Gradientenfeld sein. Der Integrabilitätstest
bestätigt das:

$$\frac{\partial F_2}{\partial x_1} - \frac{\partial F_1}{\partial x_2} = \frac{x_2}{r} \;\neq\; 0 \qquad (x_2\neq0).$$

:::herleitung
Mit der Ableitung der Abstandsfunktion, $\partial r/\partial x_j=x_j/r$, gilt für ihren Kehrwert

$$\frac{\partial}{\partial x_j}\,\frac1r = -\frac{1}{r^2}\cdot\frac{x_j}{r} = -\frac{x_j}{r^3}.$$

Damit liefern Produkt- und Kettenregel

$$\frac{\partial F_1}{\partial x_2} = x_1^2\cdot\Big(-\frac{x_2}{r^3}\Big) = -\frac{x_1^2x_2}{r^3}, \qquad \frac{\partial F_2}{\partial x_1} = \frac{x_2}{r}+x_1x_2\cdot\Big(-\frac{x_1}{r^3}\Big) = \frac{x_2}{r}-\frac{x_1^2x_2}{r^3}.$$

Die Differenz ist $x_2/r$.
:::

**Im Bild:** Eine Landschaft mit lauter radialen Steigungspfeilen müsste auf jedem Kreis um das Zentrum überall gleich
hoch sein. Dann wäre aber auch die Steigung nach außen auf dem ganzen Kreis gleich — hier geht es rechts bergauf und
links bergab. So eine Landschaft gibt es nicht.
::::

**Die wichtigste Anwendung** ist das Potential einer Punktladung. Es fällt wie $1/r$ ab, und die Gradientenformel
macht daraus in einer Zeile das bekannte $1/r^2$-Feld.

::::beispiel Das Coulomb-Feld einer Punktladung
Das Potential einer Punktladung $Q$ im Ursprung ist

$$u(\vec x) = \frac{Q}{4\pi r}, \qquad \vec x\in\mathbb{R}^3\setminus\{\vec 0\}.$$

**Im Bild** (für $Q>0$): ein Berg, der zum Zentrum hin immer steiler und höher wird. Sein Höhenprofil fällt nach außen
wie $1/r$ ab, mit der Ableitung

$$h(r) = \frac{Q}{4\pi r}, \qquad h'(r) = \frac{Q}{4\pi}\cdot\Big(-\frac{1}{r^2}\Big) = -\frac{Q}{4\pi r^2}.$$

Die Gradientenformel liefert damit sofort Gradient und Feld:

$$\nabla u = -\frac{Q}{4\pi r^2}\,\vec e_r, \qquad \vec E = -\nabla u = \frac{Q}{4\pi r^2}\,\vec e_r.$$

**Im Bild:** Das Feld zeigt bergab, also vom Gipfel weg nach außen — eine positive Probeladung wird abgestoßen und rollt
den Potentialberg hinunter. Seine Stärke fällt wie $1/r^2$, weil der Berg nach außen immer flacher wird. Das ist (in
geeigneten Einheiten) genau das bekannte elektrische Feld einer Punktladung.

**In Zahlen:** Mit $Q=4\pi$ (in diesen Einheiten) ist die Feldstärke einfach $1/r^2$:

$$\lvert\vec E\rvert = 1 \ \ (r=1), \qquad \lvert\vec E\rvert = \tfrac14 \ \ (r=2), \qquad \lvert\vec E\rvert = \tfrac19 \ \ (r=3).$$

Doppelter Abstand, ein Viertel des Feldes.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-coulomb · Vorlage: punktladung-feld-2d
Links das Coulomb-Potential $u=\frac{Q}{4\pi r}$ als nach innen spitz ansteigender Berg mit konzentrischen
Äquipotentialkreisen; rechts das Feld $\vec E=\frac{Q}{4\pi r^2}\vec e_r$ als sternförmiges Pfeilbild (Pfeile nach
außen, mit dem Abstand kürzer wegen $1/r^2$), senkrecht auf den Kreisen. Eine kleine Probeladung rollt den Berg hinab
nach außen. (Rot = Feld, orange = Probeladung, grau = Äquipotentiallinien.)
:::
::::

## Bedeutung und Ausblick

Der Gradient übersetzt zwischen zwei Sichtweisen derselben Physik: der **Landschaft** (dem Potential, eine Zahl pro
Ort) und dem **Pfeilfeld** (der Kraft, ein Vektor pro Ort). Wer die Landschaft kennt, kennt das Feld — und für
rotationssymmetrische Landschaften genügt sogar eine eindimensionale Rechnung.

Die Integrabilitätsbedingung hat gezeigt, dass nicht jedes Pfeilfeld von einer Landschaft stammt. Wie stark ein Feld
„kreist", misst die __Rotation__; wie stark es aus einem Punkt „quillt", die __Divergenz__. Diese beiden Operatoren
sind das Thema des nächsten Artikels.

:::kern
- Der __Gradient__ $\nabla f$ ist der Steigungspfeil der Landschaft $f$: Er zeigt in Richtung des steilsten Anstiegs, seine Länge ist die größte Steigung.
- Die __Richtungsableitung__ in Richtung eines Einheitsvektors $\vec v$ ist der Schatten des Gradienten auf $\vec v$: $D_{\vec v} f=\nabla f\cdot\vec v$.
- Der Gradient steht **senkrecht** auf den __Niveauflächen__ (wo er nicht null ist); dicht liegende Höhenlinien bedeuten einen langen Pfeil.
- Ein __Gradientenfeld__ ist $\vec E=\nabla\phi$ mit __Skalarpotential__ $\phi$; mit $\phi$ ist auch $\phi+c$ ein Potential.
- Die Physik schreibt $\vec E=-\nabla\varphi$: Das Feld zeigt bergab, die potentielle Energie einer positiven Ladung nimmt längs der Feldlinien ab.
- __Integrabilitätsbedingung__: Die Jacobi-Matrix eines Gradientenfelds ist symmetrisch, $\partial E_j/\partial x_k=\partial E_k/\partial x_j$ (Satz von Schwarz).
- Die Bedingung ist **notwendig, nicht hinreichend**: Das kreisende Feld $(-y,x)$ fällt durch, die Wendeltreppe um ein Loch besteht sie trotzdem ohne Potential.
- __Radialsymmetrisch__: Aus $u=h(r)$ folgt $\nabla u=h'(r)\,\vec e_r$.
- Der __radiale Einheitsvektor__ $\vec e_r=\vec x/r$ ist der Gradient der Abstandsfunktion $r$.
- Jedes radialsymmetrische Feld $s(r)\,\vec e_r$ ist ein Gradientenfeld (Höhenprofil = Stammfunktion von $s$); ein Zentralfeld ist nur dann ein Gradientenfeld, wenn es radialsymmetrisch ist.
- __Coulomb__: Aus $u=\tfrac{Q}{4\pi r}$ folgt das Feld $\vec E=-\nabla u=\tfrac{Q}{4\pi r^2}\vec e_r$.
:::

:::quiz
F: Warum steht der Gradient $\nabla f$ senkrecht auf den Niveauflächen?
A: Wer auf einer Niveaufläche (Höhenlinie) läuft, bleibt auf gleicher Höhe: Mit der Kettenregel ist $\nabla f\cdot\dot{\vec\gamma}=0$ für jede Laufrichtung $\dot{\vec\gamma}$ in der Fläche. Ein Vektor, dessen Skalarprodukt mit allen Tangentialrichtungen null ist, steht senkrecht auf der Fläche — an der Schüssel $x^2+2y^2$ etwa steht $(2,4)$ senkrecht auf der Ellipse durch $(1,1)$.
F: Warum zeigt der Gradient in Richtung des steilsten Anstiegs, und was bedeutet seine Länge?
A: Die Steigung in Richtung $\vec v$ ist der Schatten des Gradienten auf $\vec v$, also $|\nabla f|\cos\theta$. Das ist maximal für $\cos\theta=1$, wenn man genau in Pfeilrichtung läuft; die maximale Steigung ist dann die Pfeillänge $|\nabla f|$.
F: Woher kommt die Formel $D_{\vec v} f(\vec x_0)=\nabla f(\vec x_0)\cdot\vec v$ für die Richtungsableitung?
A: Man läuft auf der Geraden $\vec\gamma(t)=\vec x_0+t\vec v$, deren Geschwindigkeit überall $\vec v$ ist. Die Kettenregel für ein Feld längs einer Kurve gibt $\frac{d}{dt}f(\vec x_0+t\vec v)=\nabla f(\vec x_0+t\vec v)\cdot\vec v$; bei $t=0$ ist das die Richtungsableitung.
F: Wie steil ist die Schüssel $f=x^2+2y^2$ im Punkt $(1,1)$ nach Osten, nach Norden, bergauf und entlang der Höhenlinie?
A: Der Gradient dort ist $(2,4)$. Nach Osten ist die Steigung $2$, nach Norden $4$, in Gradientenrichtung $\sqrt{20}\approx4{,}47$ (das Maximum) und entlang der Höhenlinie, also senkrecht zum Gradienten, $0$. Nach Nordosten sind es $3\sqrt2$ — per Definition wie per Skalarprodukt.
F: Was ist ein Gradientenfeld mit Skalarpotential, und warum schreibt die Physik $\vec E=-\nabla\varphi$?
A: Ein Gradientenfeld ist das Feld der Steigungspfeile einer Landschaft, $\vec E=\nabla\phi$; mit $\phi$ ist auch $\phi+c$ ein Potential, weil Anheben keine Steigung ändert. Mit dem Minuszeichen zeigt das Feld bergab wie eine rollende Kugel, und die potentielle Energie einer positiven Ladung nimmt längs der Feldlinien ab. Für den Begriff selbst ist das Vorzeichen egal.
F: Warum muss die Jacobi-Matrix eines Gradientenfelds symmetrisch sein — formal und im Bild?
A: Formal sind ihre Einträge zweite Ableitungen des Potentials, und nach dem Satz von Schwarz vertauschen diese. Im Bild misst $\partial E_1/\partial y$, wie sich die Ost-Steigung nach Norden ändert, und $\partial E_2/\partial x$, wie sich die Nord-Steigung nach Osten ändert — in einer echten Landschaft ist das dieselbe Verwindung des Hangs.
F: Warum ist das kreisende Feld $\vec G=(-y,x)$ kein Gradientenfeld?
A: Es ist $\partial G_1/\partial y=-1$, aber $\partial G_2/\partial x=1$ — die Integrabilitätsbedingung ist verletzt. Im Bild: Wären das Steigungspfeile, ginge es beim Umlaufen ständig bergauf, und man käme trotzdem am Start an — eine unmögliche Escher-Treppe.
F: Warum ist die Integrabilitätsbedingung nicht hinreichend, und was hat das mit einer Wendeltreppe zu tun?
A: Sie ist nur ein lokaler Test. Das Feld $\vec W=\frac{(-y,x)}{x^2+y^2}$ besteht ihn auf der ganzen Ebene ohne Ursprung, hat dort aber kein Potential: Auf dem Einheitskreis wächst die Höhe mit der Rate $1$, ein Umlauf gewinnt also $2\pi$, obwohl man wieder am Start steht. Wie bei einer Wendeltreppe um eine Säule geht das nur, weil das Gebiet ein Loch hat.
F: Warum gilt $\nabla u=h'(r)\,\vec e_r$ für $u(\vec x)=h(r)$, und wie findet man damit ein Potential für ein radialsymmetrisches Feld?
A: Kettenregel: äußere Ableitung $h'(r)$ mal innere Ableitung $\nabla r=\vec e_r$. Für ein Feld $s(r)\vec e_r$ nimmt man als Höhenprofil eine Stammfunktion $h$ von $s$; dann ist $\nabla h(r)=h'(r)\vec e_r=s(r)\vec e_r$. Beim Feld $\vec e_r/r$ ist das etwa $h=\ln r$.
F: Wie entsteht aus dem Coulomb-Potential $u=\frac{Q}{4\pi r}$ das $1/r^2$-Feld, und warum zeigt es für $Q>0$ nach außen?
A: Die Gradientenformel mit $\frac{d}{dr}\frac1r=-\frac1{r^2}$ gibt $\nabla u=-\frac{Q}{4\pi r^2}\vec e_r$, also $\vec E=-\nabla u=\frac{Q}{4\pi r^2}\vec e_r$. Das Potential ist ein Berg mit Gipfel im Zentrum; das Feld zeigt bergab, also nach außen, und wird schwächer, weil der Berg nach außen flacher wird — bei doppeltem Abstand auf ein Viertel.
:::
