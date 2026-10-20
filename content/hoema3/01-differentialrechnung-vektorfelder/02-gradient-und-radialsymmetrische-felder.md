---
title: Der Gradient, Gradientenfelder und radialsymmetrische Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010200
summary: Von Grund auf – der Gradient als Steigungspfeil einer Landschaft. Warum er in Richtung des steilsten Anstiegs zeigt und senkrecht auf den Höhenlinien steht, wie man die Steigung in jede Richtung als Schatten $\nabla f\cdot v$ abliest, wann ein Pfeilfeld überhaupt zu einer echten Landschaft gehört (Gradientenfeld, Integrabilitätsbedingung) und wie man für rotationssymmetrische Landschaften $u(x)=f(r)$ sofort $\nabla u=f'(r)\,\hat e_r$ erhält – bis zum Coulomb-Feld.
tags: Gradient, Richtungsableitung, Niveaufläche, Gradientenfeld, Skalarpotential, Integrabilitätsbedingung, radialsymmetrisch, Zentralfeld, Coulomb-Feld
---

## Anschaulich

Stell dir ein Skalarfeld $f$ als **Gebirgslandschaft** vor: Jedem Ort $x$ der Landkarte ist eine Höhe $f(x)$
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

Der Wanderer muss nicht in Gradientenrichtung laufen. Er kann jede Richtung wählen, beschrieben durch einen
__Einheitsvektor__ $v\in\mathbb{R}^n$ — einen Pfeil der Länge $1$, der nur die Richtung angibt.

Wie steil es in diese Richtung geht, misst die __Richtungsableitung__. Der Wanderer läuft vom Punkt $x_0$ geradeaus
in Richtung $v$, und man schaut, wie schnell sich seine Höhe beim Losgehen ändert:

$$D_v f(x_0) := \frac{d}{dt}\, f(x_0+t\,v)\Big|_{t=0}.$$

**So liest man das:** $x_0+t\,v$ ist der Ort des Wanderers nach der Zeit $t$, wenn er mit Tempo $1$ in Richtung $v$
läuft. $f(x_0+t\,v)$ ist seine Höhe zu diesem Zeitpunkt — eine Funktion der einen Variablen $t$. Ihre gewöhnliche
Ableitung bei $t=0$ ist die Steigung, die er beim Losgehen unter den Füßen spürt.

Für die Koordinatenrichtungen, also $v=e_k$, ist das genau die partielle Ableitung nach $x_k$. Die Richtungsableitung
verallgemeinert sie auf **jede** Richtung — und man muss dafür nichts Neues ausrechnen:

:::formel Satz
$$D_v f(x_0) = \nabla f(x_0)\cdot v = \lvert\nabla f(x_0)\rvert\,\cos\theta.$$
:::

Dabei ist $\theta$ der Winkel zwischen dem Gradientenpfeil und der Laufrichtung $v$.

**Im Bild:** Die Steigung, die der Wanderer spürt, ist der **Schatten** des Gradientenpfeils auf seine Laufrichtung.
Läuft er genau in Pfeilrichtung, ist der Schatten so lang wie der Pfeil selbst. Läuft er quer dazu, verschwindet der
Schatten.

:::herleitung
Der Weg des Wanderers ist eine Gerade, die er mit konstanter Geschwindigkeit durchläuft:

$$\gamma(t) = x_0+t\,v, \qquad \dot\gamma(t) = v.$$

Die Kettenregel für ein Feld entlang einer Kurve (voriger Artikel) liefert für die Höhe längs dieses Weges

$$\frac{d}{dt}\,f(x_0+t\,v) = \nabla f(x_0+t\,v)\cdot v.$$

Bei $t=0$ steht der Wanderer noch am Start — das ist genau die erste Form der Formel. Die zweite Form ist die
geometrische Deutung des Skalarprodukts (Betrag mal Betrag mal Kosinus des Zwischenwinkels), hier mit
$\lvert v\rvert=1$.
:::

**Warum der Gradient bergauf zeigt.** Aus der Formel liest man den steilsten Anstieg sofort ab, denn der Kosinus ist
höchstens $1$:

- In Gradientenrichtung ($\cos\theta=1$) ist die Steigung **maximal**, nämlich die Pfeillänge $\lvert\nabla f\rvert$.
  Der Gradient zeigt also bergauf, und seine Länge ist die größte Steigung, die es an diesem Punkt gibt.
- Genau entgegengesetzt ($\cos\theta=-1$) geht es am steilsten **bergab**.
- Quer zum Gradienten ($\cos\theta=0$) ändert sich die Höhe beim Losgehen **nicht**.

**Zahlenbeispiel.** Nimm die elliptische Schüssel

$$f(x,y) = x^2+2y^2$$

und den Punkt $P=(1,1)$ auf ihrem Hang. Der Gradient und seine Länge sind

$$\nabla f(x,y) = (2x,\;4y), \qquad \nabla f(P) = (2,\;4), \qquad \lvert\nabla f(P)\rvert = \sqrt{2^2+4^2} = \sqrt{20}.$$

Damit ergeben sich die Steigungen in vier Laufrichtungen:

| Laufrichtung | Einheitsvektor $v$ | Steigung $D_v f(P)$ |
|---|---|---|
| nach Osten | $(1,0)$ | $2$ |
| nach Norden | $(0,1)$ | $4$ |
| bergauf (Gradientenrichtung) | $\tfrac{1}{\sqrt5}(1,2)$ | $\sqrt{20}$, rund $4{,}47$ — das Maximum |
| entlang der Höhenlinie | $\tfrac{1}{\sqrt5}(-2,1)$ | $0$ |

Die Zeile „bergauf" im Einzelnen:

$$D_v f(P) = (2,4)\cdot\tfrac{1}{\sqrt5}(1,2) = \frac{2+8}{\sqrt5} = \frac{10}{\sqrt5} = \sqrt{20}.$$

**Im Bild:** Nach Norden ist es doppelt so steil wie nach Osten — die Schüssel ist in $y$-Richtung enger gekrümmt,
ihre Höhenlinien (Ellipsen) liegen dort dichter. Der steilste Weg führt schräg bergauf, mehr nach Norden als nach
Osten. Genau quer dazu verläuft die Höhenlinie durch $P$.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-richtungsableitung-schatten · Vorlage: gradient-projektion-2d
Am Punkt $P=(1,1)$ der elliptischen Schüssel $f=x^2+2y^2$ (Höhenlinien als Ellipsen) steht der Gradientenpfeil
$(2,4)$. Ein drehbarer Einheitspfeil $v$ (Kompassnadel) kreist um $P$; der Schatten des Gradienten auf $v$ wird als
Balken angezeigt, seine Länge ist $D_v f(P)$ — maximal parallel zum Gradienten, null tangential zur Höhenlinie,
negativ in Gegenrichtung. (Rot = Gradient, orange = Laufrichtung $v$ und Schatten, grau = Höhenlinien.)
:::

## Höhenlinien und Niveauflächen: der Gradient steht senkrecht

Eine __Niveaufläche__ ist die Menge aller Punkte mit gleichem Feldwert $c$ — in der Ebene eine __Niveaulinie__ (die
Höhenlinie), im Raum eine Fläche, etwa eine Äquipotentialfläche:

$$N_c = \{\,x\in U \;:\; f(x)=c\,\}.$$

Der Gradient steht in jedem Punkt **senkrecht** auf der Niveaufläche durch diesen Punkt.

**Im Bild:** Wer genau auf der Höhenlinie wandert, bleibt auf gleicher Höhe. Sein Schritt hat deshalb keinen Anteil in
Gradientenrichtung — der Schatten des Gradienten auf seine Laufrichtung ist null.

:::herleitung
Läuft man mit einer Kurve $\gamma$ **innerhalb** einer Niveaufläche, ändert sich der Feldwert nicht. Mit der
Kettenregel heißt das

$$0 = \frac{d}{dt}\,f(\gamma(t)) = \nabla f(\gamma(t))\cdot\dot\gamma(t).$$

Die Geschwindigkeit $\dot\gamma$ kann dabei **jede** Richtung annehmen, die in der Fläche liegt — jede
Tangentialrichtung. Das Skalarprodukt mit $\nabla f$ ist für alle diese Richtungen null. Also steht $\nabla f$
senkrecht auf der ganzen Fläche.
:::

**Im Bild, quantitativ:** Je dichter die Höhenlinien, desto länger der Pfeil. Liegen zwei Höhenlinien mit
Höhenunterschied $\Delta c$ im kleinen Abstand $\Delta s$ voneinander, so ist die Steigung quer zu ihnen ungefähr

$$\lvert\nabla f\rvert \approx \frac{\Delta c}{\Delta s}.$$

So liest man auf jeder Wanderkarte die Steilheit ab, ohne zu rechnen: Höhenunterschied geteilt durch den Abstand der
Linien.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-hoehenlinien-dichte · Vorlage: hoehenlinien-abstand-2d
Zwei Kartenausschnitte nebeneinander: links dicht liegende Höhenlinien mit langem Gradientenpfeil (steiler Hang),
rechts weit auseinanderliegende mit kurzem Pfeil (flaches Tal); eingezeichnet $\Delta c$ und $\Delta s$. An einer
Höhenlinie ein tangentialer Schritt $\dot\gamma$ (keine Höhenänderung) und der senkrecht darauf stehende Gradient.
(Rot = Gradient, orange = Tangentialschritt, grau = Höhenlinien.)
:::

## Gradientenfelder: Landschaft und Steigungspfeile

Jetzt drehen wir die Blickrichtung um. Bisher war die Landschaft gegeben, und wir haben ihre Steigungspfeile
abgelesen. Ein Vektorfeld, das genau so entsteht, heißt __Gradientenfeld__:

:::formel Definition
$$E = \nabla\phi.$$
:::

Dabei ist $\phi:U\to\mathbb{R}$ ein Skalarfeld — die **Landschaft** —, und $E:U\to\mathbb{R}^n$ ist das Feld ihrer
**Steigungspfeile**. Man nennt $\phi$ ein __Skalarpotential__ von $E$.

**Ein Potential ist nie eindeutig.** Hebt man die ganze Landschaft um eine Konstante an, ändert sich keine einzige
Steigung. Mit $\phi$ ist also auch $\phi+c$ ein Potential desselben Feldes, für jede Konstante $c$.

**Die physikalische Konvention.** In der Physik schreibt man meist

$$E = -\nabla\varphi.$$

**Im Bild:** Das Feld zeigt dann nicht bergauf, sondern **bergab** — wie eine Kugel, die den Hang hinunterrollt.
Dabei nimmt die potentielle Energie ab. Läuft ein Teilchen entlang einer Feldlinie $\gamma$, also mit einer
Geschwindigkeit $\dot\gamma$ in Feldrichtung, so liefert die Kettenregel

$$\frac{d}{dt}\,\varphi(\gamma(t)) = \nabla\varphi\cdot\dot\gamma = -E\cdot\dot\gamma < 0.$$

Der Ausdruck ist negativ, weil $E$ und $\dot\gamma$ in dieselbe Richtung zeigen. Für den bloßen **Begriff**
Gradientenfeld ist das Vorzeichen egal: $E$ ist genau dann ein Gradientenfeld, wenn $-E$ eines ist.

## Echte oder unmögliche Landschaft? Die Integrabilitätsbedingung

Nicht jedes Pfeilfeld gehört zu einer Landschaft. Man kann Pfeile zeichnen, die eine **unmögliche Treppe** im Stil
von Escher beschreiben würden: Man läuft im Kreis, folgt dabei immer den Pfeilen bergauf — und kommt trotzdem wieder
am Start an. Eine echte Landschaft kann das nicht.

Gibt es einen einfachen **lokalen Test**, der solche unmöglichen Pfeilfelder entlarvt? Ja. Für ein Gradientenfeld mit
zweimal stetig differenzierbarem Potential $\phi$ gilt:

:::formel Lemma
$$E=\nabla\phi \quad\Longrightarrow\quad \frac{\partial E_j}{\partial x_k} = \frac{\partial E_k}{\partial x_j} \quad\text{für alle } j,k.$$
:::

Gelesen: Die Jacobi-Matrix $DE$ eines Gradientenfelds ist **symmetrisch** — an der Diagonale gespiegelte Einträge
sind gleich. Diese Aussage heißt __Integrabilitätsbedingung__.

**Im Bild (in der Ebene):** $E_1$ ist die Steigung nach Osten, $E_2$ die Steigung nach Norden. Die linke Seite fragt:
Wie ändert sich die Ost-Steigung, wenn man nach Norden geht? Die rechte Seite fragt: Wie ändert sich die
Nord-Steigung, wenn man nach Osten geht? In einer echten Landschaft beschreiben beide dieselbe **Verwindung** des
Hangs — sie müssen übereinstimmen.

:::herleitung
Ist $E=\nabla\phi$, so ist jede Komponente eine partielle Ableitung des Potentials:

$$E_j = \frac{\partial\phi}{\partial x_j}.$$

Die Einträge der Jacobi-Matrix von $E$ sind damit **zweite** Ableitungen des Potentials:

$$\frac{\partial E_j}{\partial x_k} = \frac{\partial^2\phi}{\partial x_k\,\partial x_j}, \qquad \frac{\partial E_k}{\partial x_j} = \frac{\partial^2\phi}{\partial x_j\,\partial x_k}.$$

Nach dem __Satz von Schwarz__ (voriger Artikel) sind diese beiden gemischten Ableitungen gleich. Im Bild: Beide Seiten
messen dieselbe Verwindung der Landschaft, nur von zwei Seiten aus betrachtet.
:::

**Zwei Zahlenbeispiele in der Ebene.** Für das Feld

$$F(x,y) = (y,\;x)$$

besteht der Test:

$$\frac{\partial F_1}{\partial y} = 1 = \frac{\partial F_2}{\partial x}.$$

Tatsächlich ist $F$ ein Gradientenfeld — es sind die Steigungspfeile der Sattelfläche:

$$\phi(x,y) = xy, \qquad \nabla\phi = (y,\;x) = F.$$

Für das kreisende Feld

$$G(x,y) = (-y,\;x)$$

fällt der Test dagegen durch:

$$\frac{\partial G_1}{\partial y} = -1 \;\neq\; 1 = \frac{\partial G_2}{\partial x}.$$

Also ist $G$ **kein** Gradientenfeld. **Im Bild:** Die Pfeile kreisen gegen den Uhrzeigersinn um den Ursprung. Wären
es Steigungspfeile, ginge es beim Umlaufen ständig bergauf, und man käme trotzdem am Start an — genau die unmögliche
Escher-Treppe.

**Stolperstein — notwendig, aber nicht hinreichend.** Die Bedingung ist nur ein **lokaler** Test. Hat das Gebiet ein
**Loch**, kann ein Feld ihn überall bestehen und trotzdem keine Landschaft besitzen. Das berühmte Beispiel lebt auf der
Ebene ohne Ursprung:

$$W(x,y) = \frac{1}{x^2+y^2}\,(-y,\;x), \qquad (x,y)\neq(0,0).$$

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

**Im Bild:** $W$ ist eine **Wendeltreppe** um eine Säule im Ursprung. Jede einzelne Stufe ist ein ganz normaler Hang,
doch wer einmal um die Säule herumgeht, steht eine Etage höher. Das geht nur, weil man die Säule — den Ursprung —
nicht betreten kann. Im Kapitel über Kurvenintegrale wird diese Etage genau gemessen: Ein Umlauf liefert $2\pi$.

In drei Dimensionen ist die Symmetrie der Jacobi-Matrix gleichbedeutend mit „Rotation gleich null" — dem Wirbel-Maß
des nächsten Artikels. Wann die Bedingung doch ausreicht (bei Gebieten ohne Löcher), klärt das Poincaré-Lemma im
Kapitel über Kurvenintegrale.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-echt-vs-unmoeglich · Vorlage: escher-vs-landschaft-2d
Drei Pfeilfelder nebeneinander: links $F=(y,x)$ als Steigungspfeile der Sattelfläche $\phi=xy$ (echte Landschaft,
Test bestanden); Mitte das kreisende Feld $G=(-y,x)$ als „Escher-Treppe" (Test fällt durch: $-1\neq1$); rechts das
Feld $W$ um ein Loch als Wendeltreppe um eine Säule (Test lokal bestanden, ein Umlauf gewinnt eine Etage). (Rot =
echte Landschaft/Potential, orange = Pfeilfeld, grau = Säule/Loch.)
:::

## Rotationssymmetrische Landschaften

In der Feldtheorie hängen viele Größen nur vom **Abstand** zu einem Zentrum ab — etwa das Potential einer
Punktladung. Eine __radialsymmetrische Funktion__ hat die Form

$$u(x) = f(r), \qquad r := \lvert x\rvert = \sqrt{x_1^2+\cdots+x_n^2}.$$

**So liest man das:** $r$ ist der Abstand des Punktes $x$ vom Ursprung, also eine Zahl. Die Funktion
$f:(0,\infty)\to\mathbb{R}$ ist eine gewöhnliche Funktion **einer** Variablen — das Höhenprofil, das man sieht, wenn
man vom Zentrum geradeaus nach außen läuft.

**Im Bild:** eine rotationssymmetrische Landschaft — eine Schüssel, ein Kegel, ein Vulkan. Die Höhenlinien sind Kreise
(im Raum: Kugeln) um das Zentrum. Weil der Gradient senkrecht auf den Höhenlinien steht, muss er überall **radial**
zeigen: direkt zum Zentrum hin oder von ihm weg.

**Der einfachste Fall: die Abstandsfunktion selbst.** Die Funktion $r$ ist ein Kegel mit Spitze im Ursprung. Läuft man
einen Schritt nach außen, wächst der Abstand um genau diesen Schritt — die Steigung nach außen ist überall $1$. Ihr
Gradient ist deshalb ein **Einheitspfeil nach außen**:

$$\nabla r = \frac{x}{r} =: \hat e_r.$$

Das Feld $\hat e_r$ heißt __radialer Einheitsvektor__. Es zeigt an jedem Punkt außer dem Ursprung radial nach außen
und hat die Länge $1$.

:::herleitung
Nach der Kettenregel ist für jede Koordinate

$$\frac{\partial r}{\partial x_j} = \frac{\partial}{\partial x_j}\sqrt{x_1^2+\cdots+x_n^2} = \frac{1}{2\sqrt{x_1^2+\cdots+x_n^2}}\cdot 2x_j = \frac{x_j}{r}.$$

Fasst man die $n$ Komponenten zu einem Vektor zusammen, entsteht $x/r$. Seine Länge ist $\lvert x\rvert/r$, also $1$.
:::

Mit einer weiteren Anwendung der Kettenregel folgt die Gradientenformel für **jede** rotationssymmetrische
Landschaft. Ist das Höhenprofil $f:(0,\infty)\to\mathbb{R}$ differenzierbar, so gilt:

:::formel Satz
$$u(x)=f(r) \quad\Longrightarrow\quad \nabla u = f'(r)\,\hat e_r.$$
:::

**Im Bild:** Der Gradient zeigt radial, und seine Länge ist die Steigung des Höhenprofils, $\lvert f'(r)\rvert$.
Steigt die Landschaft nach außen an wie eine Schüssel ($f'>0$), zeigt er nach außen. Fällt sie nach außen ab wie ein
Berg ($f'<0$), zeigt er nach innen — zum Gipfel hin.

:::herleitung
$u$ ist die Verkettung der Abstandsfunktion $x\mapsto r$ mit dem Höhenprofil $r\mapsto f(r)$. Die Kettenregel gibt
„äußere Ableitung mal innere Ableitung":

$$\nabla u = f'(r)\,\nabla r = f'(r)\,\hat e_r.$$
:::

**Zahlenbeispiel.** Für die Schüssel

$$u(x) = \tfrac12\,r^2 = \tfrac12\,\lvert x\rvert^2$$

ist das Höhenprofil eine Parabel, und die Gradientenformel liefert

$$f(r) = \tfrac12\,r^2, \qquad f'(r) = r, \qquad \nabla u = r\,\hat e_r = r\cdot\frac{x}{r} = x.$$

**Im Bild:** Die Steigungspfeile zeigen überall nach außen und werden linear mit dem Abstand länger — je weiter vom
Zentrum, desto steiler die Schüssel.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-radialformel · Vorlage: radialfeld-schuessel-2d
Eine rotationssymmetrische Landschaft $u(x)=f(r)$ als „Schüssel" über der Ebene; die Höhenlinien sind konzentrische
Kreise. Ein Schieberegler blendet das Höhenprofil $f(r)$ entlang eines Radius ein; der Gradient $\nabla u=f'(r)\hat e_r$
zeigt radial (nach außen für $f'>0$) und steht senkrecht auf den Kreisen. Daneben der Kegel $r$ mit Steigung $1$ und
seinem Einheitspfeil $\hat e_r$. (Rot = Gradient, orange = Höhenprofil, grau = Höhenkreise.)
:::

## Zentralfelder und das Coulomb-Feld

Ein __Zentralfeld__ ist ein Vektorfeld, dessen Pfeile überall radial zeigen:

$$F(x) = g(x)\,\hat e_r.$$

Die skalare Funktion $g$ gibt an, wie lang der Pfeil ist und ob er nach außen ($g>0$) oder innen ($g<0$) zeigt. Hängt
diese Länge nur vom Abstand ab, heißt das Feld __radialsymmetrisch__:

$$F(x) = f(r)\,\hat e_r.$$

Radialsymmetrische Felder sind **immer** Gradientenfelder, und die passende Landschaft findet man durch eine einzige
eindimensionale Integration. Ist $f$ stetig auf $(0,\infty)$, so gilt auf $\mathbb{R}^n\setminus\{0\}$:

:::formel Satz
$$F=f(r)\,\hat e_r \quad\Longrightarrow\quad F=\nabla\phi \quad\text{mit}\quad \phi(x)=\Phi(r),\ \ \Phi'=f.$$
:::

Gelesen: Das Höhenprofil $\Phi$ der gesuchten Landschaft ist eine **Stammfunktion** des Feldprofils $f$. Im Bild: Die
Steigung des Profils soll ja gerade die Pfeillänge sein — also muss man die Pfeillängen entlang des Radius
aufsummieren, um die Höhe zu erhalten.

:::herleitung
Nach der Gradientenformel für rotationssymmetrische Landschaften ist

$$\nabla\big(\Phi(r)\big) = \Phi'(r)\,\hat e_r = f(r)\,\hat e_r = F.$$

Der Ursprung muss ausgenommen werden, weil $\hat e_r$ dort nicht definiert ist. Die Stammfunktion ist nur bis auf eine
Konstante bestimmt — das ist wieder das Anheben der ganzen Landschaft.
:::

**Auch die Umkehrung gilt** (für $n\ge2$): Ist ein Zentralfeld ein Gradientenfeld, dann ist es automatisch
radialsymmetrisch. **Im Bild:** Zeigen alle Steigungspfeile radial, so geht es auf jeder Kugel um den Ursprung weder
hoch noch runter. Die Landschaft hat auf jeder Kugel überall dieselbe Höhe — sie ist rotationssymmetrisch.

:::herleitung
Angenommen, das Zentralfeld ist ein Gradientenfeld:

$$F = g(x)\,\hat e_r = \nabla\phi.$$

Sei $\gamma$ eine beliebige Kurve, die ganz auf einer Kugel um den Ursprung verläuft. Ihre Geschwindigkeit
$\dot\gamma$ ist tangential zur Kugel, steht also senkrecht auf $\hat e_r$. Die Kettenregel gibt

$$\frac{d}{dt}\,\phi(\gamma(t)) = \nabla\phi\cdot\dot\gamma = g\,\hat e_r\cdot\dot\gamma = 0.$$

Also ist $\phi$ längs jeder solchen Kurve konstant. Für $n\ge2$ lassen sich je zwei Punkte der Kugel durch so eine
Kurve verbinden — $\phi$ hat auf der ganzen Kugel denselben Wert und hängt nur vom Radius ab. Nach der Gradientenformel
hat $\nabla\phi$ dann die Form $f(r)\,\hat e_r$, das Feld ist also radialsymmetrisch.
:::

**Die kanonische Anwendung — das Coulomb-Feld.** Das Potential einer Punktladung $Q$ im Ursprung ist

$$u(x) = \frac{Q}{4\pi r}, \qquad x\in\mathbb{R}^3\setminus\{0\}.$$

**Im Bild** (für $Q>0$): ein Berg, der zum Zentrum hin immer steiler und höher wird. Sein Höhenprofil fällt nach außen
wie $1/r$ ab, mit der Ableitung

$$\frac{d}{dr}\,\frac{Q}{4\pi r} = \frac{Q}{4\pi}\cdot\Big(-\frac{1}{r^2}\Big) = -\frac{Q}{4\pi r^2}.$$

Die Gradientenformel liefert damit sofort Gradient und Feld:

$$\nabla u = -\frac{Q}{4\pi r^2}\,\hat e_r, \qquad E = -\nabla u = \frac{Q}{4\pi r^2}\,\hat e_r.$$

**Im Bild:** Das Feld zeigt bergab, also vom Gipfel weg nach außen — eine positive Probeladung wird abgestoßen und rollt
den Potentialberg hinunter. Seine Stärke fällt wie $1/r^2$, weil der Berg nach außen immer flacher wird. Das ist (in
geeigneten Einheiten) genau das bekannte elektrische Feld einer Punktladung.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-coulomb · Vorlage: punktladung-feld-2d
Links das Coulomb-Potential $u=\frac{Q}{4\pi r}$ als nach innen spitz ansteigender Berg mit konzentrischen
Äquipotentialkreisen; rechts das Feld $E=\frac{Q}{4\pi r^2}\hat e_r$ als sternförmiges Pfeilbild (Pfeile nach außen,
mit dem Abstand kürzer wegen $1/r^2$), senkrecht auf den Kreisen. Eine kleine Probeladung rollt den Berg hinab nach
außen. (Rot = Feld, orange = Probeladung, grau = Äquipotentiallinien.)
:::

## Bedeutung und Ausblick

Der Gradient übersetzt zwischen zwei Sichtweisen derselben Physik: der **Landschaft** (dem Potential, eine Zahl pro
Ort) und dem **Pfeilfeld** (der Kraft, ein Vektor pro Ort). Wer die Landschaft kennt, kennt das Feld — und für
rotationssymmetrische Landschaften genügt sogar eine eindimensionale Rechnung.

Die Integrabilitätsbedingung hat gezeigt, dass nicht jedes Pfeilfeld von einer Landschaft stammt. Wie stark ein Feld
„kreist", misst die __Rotation__; wie stark es aus einem Punkt „quillt", die __Divergenz__. Diese beiden Operatoren
sind das Thema des nächsten Artikels.

:::kern
- Der __Gradient__ $\nabla f$ ist der Steigungspfeil der Landschaft $f$: Er zeigt in Richtung des steilsten Anstiegs, seine Länge ist die größte Steigung.
- Die __Richtungsableitung__ in Richtung eines Einheitsvektors $v$ ist der Schatten des Gradienten auf $v$: $D_v f=\nabla f\cdot v$.
- Der Gradient steht **senkrecht** auf den __Niveauflächen__ (Höhenlinien); dicht liegende Höhenlinien bedeuten einen langen Pfeil.
- Ein __Gradientenfeld__ ist $E=\nabla\phi$ mit __Skalarpotential__ $\phi$; das Potential ist nur bis auf eine Konstante bestimmt.
- Die Physik schreibt $E=-\nabla\varphi$: Das Feld zeigt bergab, die potentielle Energie nimmt längs der Feldlinien ab.
- __Integrabilitätsbedingung__: Die Jacobi-Matrix eines Gradientenfelds ist symmetrisch, $\partial E_j/\partial x_k=\partial E_k/\partial x_j$ (Satz von Schwarz).
- Die Bedingung ist **notwendig, nicht hinreichend**: $(-y,x)$ fällt durch, das Wendeltreppen-Feld $W$ um ein Loch besteht sie trotzdem ohne Potential.
- __Radialsymmetrisch__: Aus $u=f(r)$ folgt $\nabla u=f'(r)\,\hat e_r$ mit dem __radialen Einheitsvektor__ $\hat e_r=x/r$.
- Jedes radialsymmetrische Feld $f(r)\hat e_r$ ist ein Gradientenfeld (Höhenprofil = Stammfunktion von $f$); ein Zentralfeld ist nur dann ein Gradientenfeld, wenn es radialsymmetrisch ist.
- __Coulomb__: Aus $u=\tfrac{Q}{4\pi r}$ folgt das Feld $E=-\nabla u=\tfrac{Q}{4\pi r^2}\hat e_r$.
:::

:::quiz
F: Warum steht der Gradient $\nabla f$ senkrecht auf den Niveauflächen?
A: Wer auf einer Niveaufläche (Höhenlinie) läuft, bleibt auf gleicher Höhe: Mit der Kettenregel ist $\nabla f\cdot\dot\gamma=0$ für jede Laufrichtung $\dot\gamma$ in der Fläche. Ein Vektor, dessen Skalarprodukt mit allen Tangentialrichtungen null ist, steht senkrecht auf der Fläche.
F: Warum zeigt der Gradient in Richtung des steilsten Anstiegs, und was bedeutet seine Länge?
A: Die Steigung in Richtung $v$ ist der Schatten des Gradienten auf $v$, also $|\nabla f|\cos\theta$. Das ist maximal für $\cos\theta=1$, wenn man genau in Pfeilrichtung läuft; die maximale Steigung ist dann die Pfeillänge $|\nabla f|$.
F: Woher kommt die Formel $D_v f(x_0)=\nabla f(x_0)\cdot v$ für die Richtungsableitung?
A: Man läuft auf der Geraden $\gamma(t)=x_0+tv$, deren Geschwindigkeit überall $v$ ist. Die Kettenregel für ein Feld längs einer Kurve gibt $\frac{d}{dt}f(x_0+tv)=\nabla f(x_0+tv)\cdot v$; bei $t=0$ ist das die Richtungsableitung.
F: Wie steil ist die Schüssel $f=x^2+2y^2$ im Punkt $(1,1)$ nach Osten, nach Norden, bergauf und entlang der Höhenlinie?
A: Der Gradient dort ist $(2,4)$. Nach Osten ist die Steigung $2$, nach Norden $4$, in Gradientenrichtung $\sqrt{20}\approx4{,}47$ (das Maximum) und entlang der Höhenlinie, also senkrecht zum Gradienten, $0$.
F: Was ist ein Gradientenfeld mit Skalarpotential, und warum schreibt die Physik $E=-\nabla\varphi$?
A: Ein Gradientenfeld ist das Feld der Steigungspfeile einer Landschaft, $E=\nabla\phi$; die Landschaft $\phi$ ist das Potential, bis auf eine Konstante bestimmt. Mit dem Minuszeichen zeigt das Feld bergab wie eine rollende Kugel, und die potentielle Energie nimmt längs der Feldlinien ab. Für den Begriff selbst ist das Vorzeichen egal.
F: Warum muss die Jacobi-Matrix eines Gradientenfelds symmetrisch sein — formal und im Bild?
A: Formal sind ihre Einträge zweite Ableitungen des Potentials, und nach dem Satz von Schwarz vertauschen diese. Im Bild misst $\partial E_1/\partial y$, wie sich die Ost-Steigung nach Norden ändert, und $\partial E_2/\partial x$, wie sich die Nord-Steigung nach Osten ändert — in einer echten Landschaft ist das dieselbe Verwindung des Hangs.
F: Warum ist das kreisende Feld $G=(-y,x)$ kein Gradientenfeld?
A: Es ist $\partial G_1/\partial y=-1$, aber $\partial G_2/\partial x=1$ — die Integrabilitätsbedingung ist verletzt. Im Bild: Wären das Steigungspfeile, ginge es beim Umlaufen ständig bergauf, und man käme trotzdem am Start an — eine unmögliche Escher-Treppe.
F: Warum ist die Integrabilitätsbedingung nicht hinreichend, und was hat das mit einer Wendeltreppe zu tun?
A: Sie ist nur ein lokaler Test. Das Feld $W=\frac{(-y,x)}{x^2+y^2}$ besteht ihn auf der ganzen Ebene ohne Ursprung, hat dort aber kein Potential: Wie bei einer Wendeltreppe um eine Säule ist jede Stufe ein normaler Hang, doch ein Umlauf führt eine Etage höher. Das ist nur möglich, weil das Gebiet ein Loch hat.
F: Warum gilt $\nabla u=f'(r)\,\hat e_r$ für $u(x)=f(r)$, und warum folgt daraus, dass jedes radialsymmetrische Feld ein Gradientenfeld ist?
A: Kettenregel: äußere Ableitung $f'(r)$ mal innere Ableitung $\nabla r=\hat e_r$. Für ein Feld $f(r)\hat e_r$ nimmt man als Höhenprofil eine Stammfunktion $\Phi$ von $f$; dann ist $\nabla\Phi(r)=\Phi'(r)\hat e_r=f(r)\hat e_r$ — die Landschaft ist mit einer einzigen eindimensionalen Integration gefunden.
F: Wie entsteht aus dem Coulomb-Potential $u=\frac{Q}{4\pi r}$ das $1/r^2$-Feld, und warum zeigt es für $Q>0$ nach außen?
A: Die Gradientenformel mit $\frac{d}{dr}\frac1r=-\frac1{r^2}$ gibt $\nabla u=-\frac{Q}{4\pi r^2}\hat e_r$, also $E=-\nabla u=\frac{Q}{4\pi r^2}\hat e_r$. Das Potential ist ein Berg mit Gipfel im Zentrum; das Feld zeigt bergab, also nach außen, und wird schwächer, weil der Berg nach außen flacher wird.
:::
