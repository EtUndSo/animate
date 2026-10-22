---
title: Homotopieinvarianz und der zweite Hauptsatz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030400
summary: Von Grund auf – warum sich das Kurvenintegral eines wirbelfreien Felds nicht ändert, wenn man den Weg stetig verformt. Leitbild ist ein Gummiband auf dem Gelände – solange keine Säule im Weg ist, lässt es sich zu einem Punkt zusammenziehen. Mit Homotopie, der Vertauschungs-Identität, einfach zusammenhängenden Gebieten, dem zweiten Hauptsatz (wirbelfrei gleich konservativ, wenn keine Säule stört), der Umlaufzahl und dem Magnetfeld eines Drahts als physikalischer Wendeltreppe. Mit Beispiel-Seite.
tags: Homotopie, Homotopieinvarianz, einfach zusammenhängend, zweiter Hauptsatz, Integrabilitätsbedingung, Umlaufzahl, geschlitzte Ebene, Argumentfunktion
---

## Anschaulich

Das Poincaré-Lemma brauchte einen Turm, der alles sieht. Das ist eine starke Forderung — viele Gelände ohne Säule haben
keinen solchen Turm, etwa ein Ring, den man an einer Stelle aufgeschnitten hat. Dieser Artikel findet die richtige,
schwächere Bedingung.

**Das Leitbild dieses Artikels:** ein **Gummiband** auf dem Gelände. Man legt es als Rundtour hin und schiebt es dann stetig
umher, ohne es zu zerreißen und ohne das Gelände zu verlassen. Für einen wirbelfreien Wind gilt das Erstaunliche: Die
Arbeit längs des Gummibands ändert sich beim Verschieben **nicht**. Kein Stück Weg, das man neu überstreicht, bringt einen
Wirbel mit.

Wenn sich das Gummiband zu einem Punkt zusammenziehen lässt, ist die Arbeit also dieselbe wie auf einem Punkt — null.
Geht das mit jedem Gummiband, heißt das Gelände __einfach zusammenhängend__. Dort ist ein wirbelfreier Wind konservativ: der
__zweite Hauptsatz für Kurvenintegrale__.

Steht eine Säule im Gelände, bleibt ein Gummiband, das sie umschlingt, an ihr hängen. Genau dort konnte die Wendeltreppe
Arbeit leisten — und ihr Wert $2\pi$ hängt nicht von der Form des Bandes ab, nur davon, wie oft es die Säule umschlingt.
In der Elektrotechnik ist das Magnetfeld um einen stromdurchflossenen Draht genau so eine Wendeltreppe.

:::grafik
Szene: hoema3/kurvenintegrale/04-gummiband · Vorlage: homotopie-schleife-2d
Ein wirbelfreies Windfeld auf einem Gelände mit einer Säule. Ein Gummiband wird mit einem Regler $s$ stetig verformt; ein
Zähler zeigt die Arbeit längs des Bandes, die während der ganzen Verformung gleich bleibt. Ein Band neben der Säule lässt
sich zu einem Punkt zusammenziehen, sein Zähler steht auf null. Ein Band um die Säule bleibt an ihr hängen, sein Zähler
steht auf $2\pi$ — für jede Form. Kernaussage: Bei wirbelfreien Feldern zählt nur, wie das Band um die Säulen liegt. (Blau =
Feld, orange = Gummiband, rot = Zähler, grau = Säule.)
:::

## Homotopie: einen Weg stetig verformen

**Die Akteure:** eine offene Menge $U\subseteq\mathbb{R}^n$ und eine stetige Abbildung

$$\vec h:[0,1]\times[a,b]\to U, \qquad (s,t)\mapsto\vec h(s,t).$$

Für jedes feste $s$ ist $t\mapsto\vec h(s,t)$ eine Kurve; wir nennen sie $\vec\gamma_s$. So eine Kurvenschar heißt
__Homotopie__ von $\vec\gamma_0$ nach $\vec\gamma_1$. Der Parameter $t$ ist die Fahrzeit auf einer Kurve, der Parameter $s$
die Zeit des Verformens.

**Zwei Sorten**, je nachdem, was mit den Enden passiert:

- __Homotopie geschlossener Kurven__: Jede Zwischenkurve ist geschlossen,

$$\vec h(s,a) = \vec h(s,b) \qquad\text{für alle } s\in[0,1].$$

- __Homotopie mit festen Endpunkten__: Anfang und Ende bewegen sich nicht,

$$\vec h(s,a) = \vec x_0, \qquad \vec h(s,b) = \vec x_1 \qquad\text{für alle } s\in[0,1].$$

**Im Bild:** Die erste Sorte ist das Gummiband, das man über das Gelände schiebt — es bleibt immer geschlossen. Die zweite
ist ein Seil, dessen Enden an zwei Pflöcken festgebunden sind; dazwischen darf man es beliebig verlegen.

## Die Vertauschungs-Identität

Wie ändert sich die Arbeit, wenn man den Weg verformt? Der Schlüssel ist eine Identität, für die es genau die
Wirbelfreiheit braucht.

**Die Akteure:** eine zweimal stetig differenzierbare Homotopie $\vec h$ wie oben und ein stetig differenzierbares
Vektorfeld $\vec F:U\to\mathbb{R}^n$, das die Integrabilitätsbedingung erfüllt. Dann gilt

:::formel Lemma
$$\frac{\partial}{\partial s}\Big(\vec F\big(\vec h(s,t)\big)\cdot\frac{\partial\vec h}{\partial t}(s,t)\Big) = \frac{\partial}{\partial t}\Big(\vec F\big(\vec h(s,t)\big)\cdot\frac{\partial\vec h}{\partial s}(s,t)\Big).$$
:::

**So liest man das:** Links steht, wie sich der Integrand des Kurvenintegrals — Wind mal Fahrgeschwindigkeit — beim
Verformen ändert. Rechts steht die Fahrzeit-Ableitung von „Wind mal Verformungsgeschwindigkeit". Die beiden Ableitungen
dürfen ihre Rollen tauschen.

**Im Bild:** Verschiebt man das Gummiband ein wenig, überstreicht es einen schmalen Streifen. Ein Wirbel in diesem
Streifen würde die Arbeit ändern; ohne Wirbel bleibt nur, was an den Enden des Bandes herein- oder hinausgeschoben wird.

:::herleitung
Beide Seiten werden mit Kettenregel und Produktregel ausgerechnet, mit $\partial_k F_j$ für die Ableitung der $j$-ten
Komponente nach der $k$-ten Koordinate. Links:

$$\frac{\partial}{\partial s}\Big(\vec F(\vec h)\cdot\partial_t\vec h\Big) = \sum_{j,k}\big(\partial_kF_j\big)(\vec h)\;\partial_sh_k\;\partial_th_j+\vec F(\vec h)\cdot\partial_s\partial_t\vec h.$$

Rechts, mit vertauschten Rollen von $s$ und $t$:

$$\frac{\partial}{\partial t}\Big(\vec F(\vec h)\cdot\partial_s\vec h\Big) = \sum_{j,k}\big(\partial_kF_j\big)(\vec h)\;\partial_th_k\;\partial_sh_j+\vec F(\vec h)\cdot\partial_t\partial_s\vec h.$$

Die zweiten Terme sind nach dem Satz von Schwarz gleich, weil $\vec h$ zweimal stetig differenzierbar ist. Im ersten Term
rechts benennt man die Summationsindizes um, $j$ heißt jetzt $k$ und umgekehrt:

$$\sum_{j,k}\big(\partial_jF_k\big)(\vec h)\;\partial_th_j\;\partial_sh_k.$$

Nach der Integrabilitätsbedingung ist $\partial_jF_k$ gleich $\partial_kF_j$ — dann steht dort genau der erste Term links.
:::

::::beispiel Die Identität nachgerechnet
Die Kurven $y=s\,x^2$ vom Ursprung zum Punkt $(1,s)$ bilden die Homotopie

$$\vec h(s,t) = (t,\ s\,t^2), \qquad \frac{\partial\vec h}{\partial t} = (1,\ 2st), \qquad \frac{\partial\vec h}{\partial s} = (0,\ t^2).$$

**(a) Das Sattelfeld** $(y,x)$ erfüllt die Integrabilitätsbedingung. Am Ort $\vec h(s,t)$ ist es $(st^2,\ t)$, und

$$\frac{\partial}{\partial s}\big(st^2+2st^2\big) = 3t^2, \qquad \frac{\partial}{\partial t}\big(t\cdot t^2\big) = 3t^2.$$

Beide Seiten stimmen überein.

**(b) Der Wirbel** $(-y,x)$ erfüllt sie nicht. Am Ort ist er $(-st^2,\ t)$, und

$$\frac{\partial}{\partial s}\big(-st^2+2st^2\big) = t^2, \qquad \frac{\partial}{\partial t}\big(t\cdot t^2\big) = 3t^2.$$

Die Seiten unterscheiden sich.

**Im Bild:** Beim Sattelfeld ist die Arbeit längs der Parabel zum Punkt $(1,s)$ gerade $s$, der Höhenunterschied von $xy$. Sie
wächst mit der Rate $1$, und genau das ist der Randterm: Das Ziel wandert mit der Geschwindigkeit $(0,1)$ nach oben, wo der
Wind $(s,1)$ weht. Beim Wirbel kommt im überstrichenen Streifen zusätzlich ein Wirbel hinzu.
::::

**Die Änderung der Arbeit.** Leitet man das Kurvenintegral längs $\vec\gamma_s$ nach $s$ ab, darf man unter dem Integral
ableiten, und die Identität macht aus dem Integranden eine Ableitung nach $t$:

$$\frac{d}{ds}\int_{\gamma_s}\vec F\cdot d\vec x = \int_a^b\frac{\partial}{\partial t}\Big(\vec F(\vec h)\cdot\frac{\partial\vec h}{\partial s}\Big)\,dt = \Big[\vec F\big(\vec h(s,t)\big)\cdot\frac{\partial\vec h}{\partial s}(s,t)\Big]_{t=a}^{t=b}.$$

Übrig bleibt nur, was an den beiden Enden geschieht.

:::herleitung
Der Integrand $(s,t)\mapsto\vec F(\vec h(s,t))\cdot\partial_t\vec h(s,t)$ ist auf dem kompakten Rechteck $[0,1]\times[a,b]$
stetig differenzierbar, weil $\vec F$ einmal und $\vec h$ zweimal stetig differenzierbar ist. Also darf man nach dem
Parameter $s$ unter dem Integral ableiten (Artikel über Parameterintegrale). Danach wirkt die Identität, und der Hauptsatz
über $t$ liefert die Randwerte. Die Formel für das Kurvenintegral ergibt dabei auch für Zwischenkurven Sinn, die nicht
regulär sind — etwa für eine Kurve, die zu einem Punkt zusammengeschrumpft ist und das Integral null hat.
:::

## Homotopieinvarianz

Der Randterm verschwindet in genau den beiden Fällen, die zählen. Für ein stetig differenzierbares Feld, das die
Integrabilitätsbedingung erfüllt, und eine zweimal stetig differenzierbare Homotopie gilt:

:::formel Satz
$$\int_{\gamma_0}\vec F\cdot d\vec x = \int_{\gamma_1}\vec F\cdot d\vec x \qquad\text{bei Homotopien geschlossener Kurven und bei Homotopien mit festen Endpunkten}.$$
:::

**So liest man das:** Verformt man eine Rundtour stetig, ohne sie aufzuschneiden, oder verlegt man einen Weg zwischen zwei
festen Pflöcken, so bleibt die Arbeit eines wirbelfreien Felds dieselbe.

**Im Bild:** Das Gummiband und das Seil lassen sich über das wirbelfreie Gelände schieben, ohne dass sich der Zähler rührt.
Nur Wirbel im überstrichenen Gebiet — oder eine Säule, an der man nicht vorbeikommt — könnten etwas ändern.

:::herleitung
**Geschlossene Kurven.** Für jedes $s$ ist $\vec h(s,a)$ gleich $\vec h(s,b)$. Dann sind auch die Ableitungen nach $s$ an
beiden Enden gleich, und die beiden Randwerte heben sich weg:

$$\vec F\big(\vec h(s,b)\big)\cdot\frac{\partial\vec h}{\partial s}(s,b)-\vec F\big(\vec h(s,a)\big)\cdot\frac{\partial\vec h}{\partial s}(s,a) = 0.$$

**Feste Endpunkte.** Hier bewegen sich die Enden nicht, ihre Ableitung nach $s$ ist der Nullvektor, und beide Randwerte sind
null.

In beiden Fällen hat die Arbeit als Funktion von $s$ die Ableitung null, ist also konstant. Insbesondere stimmen Anfangs- und
Endwert der Verformung überein.
:::

::::beispiel Ellipsen um die Säule
Die Wendeltreppe

$$\vec W(x,y) = \frac{1}{x^2+y^2}\,(-y,\ x)$$

ist auf der gelochten Ebene wirbelfrei. Man verformt den Einheitskreis in Ellipsen mit den Halbachsen $p\ge1$ und $1$,

$$\vec h(s,t) = \big(p\cos t,\ \sin t\big), \qquad p = 1+s, \qquad t\in[0,2\pi],$$

eine Homotopie geschlossener Kurven, die nie durch den Ursprung läuft. Der Integrand auf der Ellipse ist

$$\vec W\cdot\dot{\vec\gamma}_s = \frac{(-\sin t)(-p\sin t)+(p\cos t)(\cos t)}{p^2\cos^2t+\sin^2t} = \frac{p}{p^2\cos^2t+\sin^2t}.$$

Er hängt von $p$ ab — das Integral aber nicht:

$$\oint_{\gamma_s}\vec W\cdot d\vec x = \int_0^{2\pi}\frac{p\,dt}{p^2\cos^2t+\sin^2t} = 2\pi.$$

:::herleitung
Aus Symmetriegründen ist das Integral viermal das Integral über $[0,\tfrac{\pi}{2}]$. Dort substituiert man

$$u = \tan t, \qquad du = \frac{dt}{\cos^2t}, \qquad u\in[0,\infty),$$

und teilt Zähler und Nenner durch $\cos^2t$:

$$\int_0^{\pi/2}\frac{p\,dt}{p^2\cos^2t+\sin^2t} = \int_0^\infty\frac{p\,du}{p^2+u^2} = \Big[\arctan\frac{u}{p}\Big]_0^\infty = \frac{\pi}{2}.$$

Mal vier ergibt $2\pi$.
:::

**Im Bild:** Wird das Gummiband zur langen Ellipse gezogen, fährt man auf den Längsseiten weit weg von der Säule mit
schwachem Wind und an den Enden nah an ihr mit starkem. Beides gleicht sich genau aus.
::::

## Einfach zusammenhängende Gebiete

**Die Akteure:** Ein Gebiet $G\subseteq\mathbb{R}^n$ heißt __einfach zusammenhängend__, wenn sich jede geschlossene stetige
Kurve in $G$ durch eine Homotopie geschlossener Kurven in $G$ zu einem Punkt zusammenziehen lässt:

:::formel Definition
$$\vec h(0,t) = \vec\gamma(t), \qquad \vec h(1,t) = \text{konstant}, \qquad \vec h(s,a) = \vec h(s,b) \qquad\text{für alle } s,t.$$
:::

**So liest man das:** Die Homotopie beginnt bei der gegebenen Rundtour und endet bei einer Kurve, die stillsteht — einem
Punkt. Jede Zwischenkurve ist geschlossen und liegt in $G$. Achtung: Auf diese Geschlossenheit, die letzte Bedingung, kommt
es an. Ohne sie wäre jede Kurve zusammenziehbar: Man könnte sie einfach längs ihrer selbst aufrollen, also auch ein Band um eine Säule, das dabei
aufgeschnitten wird.

**Im Bild:** Jedes Gummiband lässt sich auf dem Gelände zu einem Punkt zusammenziehen, ohne zu reißen. In der Ebene heißt
das anschaulich: Das Gelände hat keine Löcher.

Sterngebiete sind einfach zusammenhängend:

:::formel Lemma
$$\vec h(s,t) := (1-s)\,\vec\gamma(t)+s\,\vec x_0 \qquad\text{zieht jede Rundtour zum Zentrum } \vec x_0 \text{ zusammen}.$$
:::

:::herleitung
Für festes $t$ läuft $\vec h(s,t)$ auf der Strecke vom Kurvenpunkt $\vec\gamma(t)$ zum Zentrum — und die liegt im Sterngebiet.
Zu Beginn der Verformung ist das die Kurve, am Ende der Punkt $\vec x_0$. Jede Zwischenkurve ist geschlossen, weil die Kurve
es ist: Anfangs- und Endpunkt fallen zusammen und werden in jedem Moment gleich verschoben. Und $\vec h$ ist stetig, sogar so
oft differenzierbar wie $\vec\gamma$.
:::

**Im Bild:** Vom Turm aus zieht man das Gummiband an Fäden, die längs der Sichtlinien laufen, gleichmäßig zu sich heran.

::::beispiel Gummibänder in vier Gebieten
**(a) Die geschlitzte Ebene** ist nach dem vorigen Artikel ein Sterngebiet mit dem Turm $(1,0)$, also einfach
zusammenhängend.

**(b) Der aufgeschnittene Ring**, der Ring zwischen den Radien $1$ und $2$ ohne die Punkte der negativen $x$-Achse, ist
einfach zusammenhängend, aber kein Sterngebiet — der Fall, für den sich der allgemeinere Begriff lohnt.

:::herleitung
**Einfach zusammenhängend.** Eine Rundtour im aufgeschnittenen Ring kreuzt nie die negative $x$-Achse. Ihr Polarwinkel
$\theta(t)$ zwischen $-\pi$ und $\pi$ und ihr Abstand $r(t)$ vom Ursprung ändern sich deshalb stetig. Man verformt beide
gleichmäßig zu festen Werten,

$$r_s(t) = (1-s)\,r(t)+s\cdot\tfrac32, \qquad \theta_s(t) = (1-s)\,\theta(t),$$

und setzt daraus den Punkt mit dem Abstand $r_s(t)$ und dem Winkel $\theta_s(t)$ zusammen. Der Abstand bleibt zwischen $1$
und $2$, der Winkel zwischen $-\pi$ und $\pi$: Die Zwischenkurven liegen im aufgeschnittenen Ring, sind geschlossen und
enden im Punkt $(\tfrac32,0)$.

**Kein Sterngebiet.** Zu einem möglichen Turm wählt man einen Punkt auf der anderen Seite des Lochs, genau gegenüber oder —
falls dort der Schnitt liegt — knapp daneben. Die Sichtlinie zu ihm läuft durch das innere Loch oder dicht am Ursprung
vorbei, also aus dem Gebiet hinaus.
:::

**(c) Die gelochte Ebene** ist **nicht** einfach zusammenhängend. Wäre sie es, so wäre nach dem zweiten Hauptsatz (unten)
die wirbelfreie Wendeltreppe konservativ. Sie ist es nicht, denn jeder Umlauf bringt $2\pi$.

**(d) Der Raum ohne Ursprung** $\mathbb{R}^3\setminus\{\vec 0\}$ **ist** einfach zusammenhängend — im Raum hat ein Gummiband
Platz, an einem fehlenden Punkt vorbeizurutschen.

:::herleitung
Die Beweisidee für reguläre Rundtouren. Projiziert man eine solche Kurve vom Ursprung aus auf die Einheitskugel, entsteht
eine Kurve auf der Kugel. Als stückweise glatte Kurve hat sie keine Fläche, kann die Kugel also nicht ganz bedecken. Es gibt
deshalb eine Richtung $\vec e$, in die die Rundtour nie zeigt — sie liegt im Raum ohne den Strahl der Punkte $t\,\vec e$ mit
$t\ge0$.

Dieser Raum ist ein Sterngebiet mit dem Zentrum $-\vec e$: Träfe die Strecke von $-\vec e$ zu einem Punkt $\vec p$ den Strahl,
so wäre $\vec p$ selbst ein positives Vielfaches von $\vec e$ oder der Ursprung, läge also auf dem Strahl. Im Sterngebiet
lässt sich die Rundtour zusammenziehen, ohne den Ursprung zu berühren.
:::

**Im Bild:** In der Ebene sperrt ein fehlender Punkt das Gummiband ein; im Raum hebt man es einfach darüber hinweg. Ein
fehlender **Strahl** oder eine fehlende Gerade würde es dagegen auch im Raum festhalten.
::::

## Der zweite Hauptsatz

Jetzt die globale Antwort auf die Frage, wann wirbelfrei schon konservativ heißt. Für ein einfach zusammenhängendes Gebiet
$G\subseteq\mathbb{R}^n$ und ein stetig differenzierbares Vektorfeld $\vec F$ auf $G$ gilt:

:::formel Satz
$$\vec F \text{ konservativ in } G \quad\Longleftrightarrow\quad \vec F \text{ erfüllt in } G \text{ die Integrabilitätsbedingung}.$$
:::

**So liest man das:** In zwei und drei Dimensionen heißt die rechte Seite „$\operatorname{rot}\vec F=\vec 0$". Mit dem ersten
Hauptsatz ist konservativ dasselbe wie Gradientenfeld — auf einfach zusammenhängenden Gebieten ist ein wirbelfreies Feld
also immer ein Gradientenfeld. Das verallgemeinert das Poincaré-Lemma von Sterngebieten auf alle Gebiete ohne Säulen.

**Im Bild:** Jede Rundtour ist ein Gummiband. Es lässt sich zu einem Punkt zusammenziehen, und dabei ändert sich die Arbeit
des wirbelfreien Winds nicht. Auf einem Punkt ist sie null — also auch auf der Rundtour.

:::herleitung
**Von links nach rechts.** Ein konservatives Feld ist nach dem ersten Hauptsatz ein Gradientenfeld $\nabla\varphi$, mit
zweimal stetig differenzierbarem $\varphi$; nach Schwarz erfüllt es die Integrabilitätsbedingung.

**Von rechts nach links.** Sei $\vec\gamma:[a,b]\to G$ eine regulär parametrisierte geschlossene Kurve. Weil $G$ einfach
zusammenhängend ist, gibt es eine Homotopie geschlossener Kurven zu einer Kurve $\vec\gamma_1$, die stillsteht. Deren
Geschwindigkeit ist null, das Integral über sie also null. Ist die Homotopie zweimal stetig differenzierbar, gibt die
Homotopieinvarianz

$$\oint_\gamma\vec F\cdot d\vec x = \oint_{\gamma_1}\vec F\cdot d\vec x = 0.$$

Im allgemeinen Fall ist die Homotopie nur stetig; dann glättet man sie zuerst — diesen technischen Schritt führen wir
hier nicht aus. Weil jede Rundtour die Arbeit null bringt, ist $\vec F$ nach dem Rundtour-Lemma konservativ.
:::

::::beispiel Ein Gummiband neben der Säule
Der Kreis vom Radius $1$ um den Punkt $(3,0)$,

$$\vec\gamma(t) = (3+\cos t,\ \sin t), \qquad t\in[0,2\pi],$$

liegt in der rechten Halbebene. Dort zieht ihn die Homotopie

$$\vec h(s,t) = (1-s)\,\vec\gamma(t)+s\,(3,0) = \big(3+(1-s)\cos t,\ (1-s)\sin t\big)$$

zu seinem Mittelpunkt zusammen, ohne je den Ursprung zu berühren. Nach der Homotopieinvarianz bringt die Wendeltreppe auf
diesem Kreis die Arbeit null.

**Probe:** In der rechten Halbebene hat die Wendeltreppe den Polarwinkel als Potential, den Arcustangens von $y/x$. Auf
einer Rundtour ist die Potentialdifferenz null.

**Im Bild:** Ein Gummiband, das die Säule nicht umschlingt, lässt sich neben ihr zusammenziehen — es bringt nichts, auch wenn
es durch ein Gelände läuft, in dem anderswo eine Wendeltreppe steht.
::::

## Warum die Wendeltreppe gerade $2\pi$ bringt

Die gelochte Ebene ist nicht einfach zusammenhängend, und dort darf die Wendeltreppe Arbeit leisten. Die
Homotopieinvarianz sagt aber noch mehr: Alle Rundtouren, die sich in den einmal durchlaufenen Einheitskreis verformen
lassen, bringen dieselben $2\pi$ — gleich, welche Form sie haben.

Durchläuft eine Rundtour den Kreis $k$-mal, mit $k\in\mathbb{Z}$ — negative Werte im Uhrzeigersinn —, so ist die Arbeit

$$\oint\vec W\cdot d\vec x = 2\pi k.$$

Deshalb nennt man für eine beliebige Rundtour $\gamma$ in der gelochten Ebene die Zahl

$$\frac{1}{2\pi}\oint_\gamma\vec W\cdot d\vec x$$

ihre __Umlaufzahl__ um den Ursprung. Sie zählt, wie oft das Gummiband die Säule umschlingt.

:::herleitung
Der $k$-mal durchlaufene Kreis ist

$$\vec\gamma(t) = (\cos kt,\ \sin kt), \qquad \dot{\vec\gamma}(t) = k\,(-\sin kt,\ \cos kt), \qquad t\in[0,2\pi].$$

Der Integrand ist überall $k$, wie beim einfachen Kreis mit dem zusätzlichen Faktor aus der Geschwindigkeit, also ist die
Arbeit $2\pi k$. Für $k=0$ steht die Kurve still.
:::

**Feste Pflöcke.** Auch Wege mit festen Endpunkten unterscheiden sich nur darin, auf welcher Seite sie an der Säule vorbeigehen
und wie oft sie sie umrunden.

::::beispiel Feste Enden, zwei Seiten der Säule
Von $(1,0)$ nach $(-1,0)$ führen der obere Halbkreis mit der Arbeit $\pi$ und der untere mit der Arbeit $-\pi$ (vorletzter
Artikel). Ein dritter Weg oben herum, über die Ecken $(1,1)$ und $(-1,1)$:

| Stück | Parametrisierung, $t\in[0,1]$ | Integrand | Arbeit |
|---|---|---|---|
| hoch | $(1,\,t)$ | $\frac{1}{1+t^2}$ | $\frac{\pi}{4}$ |
| quer | $(1-2t,\,1)$ | $\frac{2}{(1-2t)^2+1}$ | $\frac{\pi}{2}$ |
| runter | $(-1,\,1-t)$ | $\frac{1}{1+(1-t)^2}$ | $\frac{\pi}{4}$ |

Zusammen $\pi$ — wie beim oberen Halbkreis. Die beiden oberen Wege lassen sich mit festen Enden ineinander verformen, ohne
den Ursprung zu treffen; der untere nicht.

:::herleitung
**Hoch:** Die Geschwindigkeit ist $(0,1)$, der Windanteil nach oben $W_2(1,t)$; das Integral ist $\arctan1$.

**Quer:** Die Geschwindigkeit ist $(-2,0)$, und die erste Komponente des Winds ist dort negativ:

$$W_1(1-2t,\,1) = -\frac{1}{(1-2t)^2+1}.$$

Das Produkt ist also positiv. Mit der Substitution $u=1-2t$:

$$\int_0^1\frac{2\,dt}{(1-2t)^2+1} = \int_{-1}^{1}\frac{du}{u^2+1} = \frac{\pi}{2}.$$

**Runter:** Die Geschwindigkeit ist $(0,-1)$, und die zweite Komponente des Winds ist dort negativ:

$$W_2(-1,\,1-t) = -\frac{1}{1+(1-t)^2}.$$

Das Produkt ist positiv, und mit der Substitution $u=1-t$ ist das Integral wieder $\arctan1$.
:::

**Im Bild:** Ein Seil zwischen zwei Pflöcken lässt sich oberhalb der Säule beliebig verlegen, ohne dass sich die Arbeit
ändert. Will man es auf die untere Seite bringen, muss man es über die Säule heben — und genau dort ändert sich die Arbeit um
eine ganze Runde, $2\pi$.
::::

## Die Wendeltreppe in der Elektrotechnik

Die bekannteste Wendeltreppe ist das Magnetfeld eines langen, geraden Drahts. Fließt der Strom $I$ längs der $z$-Achse, so
ist das Feld außerhalb des Drahts

$$\vec H(x,y,z) = \frac{I}{2\pi}\,\frac{1}{x^2+y^2}\,(-y,\ x,\ 0).$$

Außerhalb des Drahts ist es wirbelfrei — dort fließt kein Strom. Auf dem Gebiet „Raum ohne die $z$-Achse" ist es trotzdem
nicht konservativ: Jeder Weg, der den Draht einmal umrundet, bringt dieselbe Umlaufspannung $I$. Das ist das
__Durchflutungsgesetz__.

::::beispiel Das Magnetfeld eines Drahts
**Wirbelfrei:** Die Komponenten hängen nicht von $z$ ab, und die dritte ist null. Die erste und zweite Komponente der
Rotation verschwinden deshalb, und die dritte ist bis auf den Faktor $\frac{I}{2\pi}$ die ebene Rotation der Wendeltreppe,
also null:

$$\operatorname{rot}\vec H = \frac{I}{2\pi}\,\Big(0,\ 0,\ \frac{\partial W_2}{\partial x}-\frac{\partial W_1}{\partial y}\Big) = \vec 0.$$

**Umlauf:** Auf einem Kreis vom Radius $R$ um den Draht in einer Ebene $z=$ konstant ist der Integrand wie bei der
Wendeltreppe konstant, und

$$\oint\vec H\cdot d\vec x = \frac{I}{2\pi}\cdot2\pi = I.$$

**In Zahlen:** Mit

$$I = 10\,\text{A}, \qquad R = 5\,\text{cm}$$

ist die Feldstärke

$$\lvert\vec H\rvert = \frac{I}{2\pi R} = \frac{10}{2\pi\cdot0{,}05}\,\frac{\text{A}}{\text{m}} \approx 31{,}8\,\frac{\text{A}}{\text{m}},$$

und die Umlaufspannung ist für jeden Radius $10\,\text{A}$ — der Umfang wächst genau so, wie das Feld abnimmt.

**Im Bild:** Der Draht ist die Säule der Wendeltreppe. Ein Gummiband um ihn herum lässt sich im Raum ohne Draht nicht
zusammenziehen — es bleibt am Draht hängen, wie in der Ebene an der Säule. Ein Gummiband, das den Draht nicht umschlingt,
bringt dagegen null.
::::

## Bedeutung und Ausblick

Die Homotopieinvarianz macht Kurvenintegrale wirbelfreier Felder zu **topologischen** Größen: Es zählt nicht die Form des
Wegs, sondern nur, wie er um die Löcher des Gebiets liegt. Damit ist die Frage aus dem ersten Hauptsatz vollständig
beantwortet. Auf einfach zusammenhängenden Gebieten ist „wirbelfrei" dasselbe wie „hat ein Potential". Auf Gebieten mit
Säulen zählt jede Säule mit ihrer Umlaufzahl — beim Draht ist das die Durchflutung.

Was aber, wenn das Feld **nicht** wirbelfrei ist? Dann ändert sich die Arbeit beim Verschieben des Gummibands um die Wirbel
im überstrichenen Gebiet. Summiert man diese Wirbel über eine ganze Fläche, erhält man die Arbeit längs ihres Randes — den
__Satz von Stokes in der Ebene__, Thema des nächsten Artikels.

:::kern
- Eine __Homotopie__ verformt einen Weg stetig: als geschlossenes Gummiband oder als Seil zwischen festen Pflöcken.
- Für wirbelfreie Felder dürfen Fahr- und Verformungsableitung tauschen; die Änderung der Arbeit ist ein reiner Randterm.
- __Homotopieinvarianz__: Bei beiden Sorten von Homotopie bleibt die Arbeit eines wirbelfreien Felds dieselbe.
- __Einfach zusammenhängend__: Jedes Gummiband lässt sich im Gebiet zu einem Punkt zusammenziehen, mit geschlossenen Zwischenkurven.
- Sterngebiete sind einfach zusammenhängend, ebenso der aufgeschnittene Ring und der Raum ohne einen Punkt; die gelochte Ebene nicht.
- __Zweiter Hauptsatz__: Auf einfach zusammenhängenden Gebieten ist ein wirbelfreies, stetig differenzierbares Feld konservativ.
- Die Wendeltreppe bringt auf dem $k$-mal durchlaufenen Kreis $2\pi k$; geteilt durch $2\pi$ ist das die __Umlaufzahl__.
- Das Magnetfeld eines Drahts ist eine Wendeltreppe: wirbelfrei außerhalb, aber jeder Umlauf bringt den Strom $I$.
:::

:::quiz
F: Was ist eine Homotopie, und welche zwei Sorten braucht man?
A: Eine stetige Abbildung $\vec h(s,t)$, die für jedes feste $s$ eine Kurve $\vec\gamma_s$ ist; $s$ ist die Verformungszeit. Bei einer Homotopie geschlossener Kurven ist jede Zwischenkurve geschlossen — das Gummiband. Bei einer Homotopie mit festen Endpunkten bleiben Anfang und Ende fest — das Seil zwischen zwei Pflöcken.
F: Was besagt die Vertauschungs-Identität, und wo braucht ihr Beweis die Wirbelfreiheit?
A: $\partial_s(\vec F(\vec h)\cdot\partial_t\vec h)=\partial_t(\vec F(\vec h)\cdot\partial_s\vec h)$. Beide Seiten enthalten einen Term mit zweiten Ableitungen von $\vec h$, die nach Schwarz gleich sind, und eine Doppelsumme mit Ableitungen von $\vec F$. Nach Umbenennen der Indizes stimmen die Doppelsummen genau dann überein, wenn $\partial_jF_k=\partial_kF_j$ gilt.
F: Warum ändert sich die Arbeit eines wirbelfreien Felds beim Verformen nicht?
A: Mit der Identität ist die Ableitung der Arbeit nach $s$ das Integral einer $t$-Ableitung, also der Randterm $[\vec F(\vec h)\cdot\partial_s\vec h]_{t=a}^{t=b}$. Bei geschlossenen Zwischenkurven heben sich die beiden Randwerte weg, bei festen Endpunkten ist $\partial_s\vec h$ dort null. Die Arbeit ist also konstant in $s$.
F: Was zeigt die Rechnung an den Ellipsen um die Säule?
A: Verformt man den Einheitskreis in Ellipsen $(p\cos t,\sin t)$, hängt der Integrand $\frac{p}{p^2\cos^2t+\sin^2t}$ von $p$ ab, das Integral über $[0,2\pi]$ ist aber immer $2\pi$. Auf den Längsseiten ist der Wind schwach, an den Enden nah an der Säule stark — beides gleicht sich genau aus.
F: Was heißt einfach zusammenhängend, und warum müssen die Zwischenkurven geschlossen bleiben?
A: Jede geschlossene Kurve im Gebiet lässt sich durch eine Homotopie geschlossener Kurven im Gebiet zu einem Punkt zusammenziehen. Ohne die Bedingung, dass die Zwischenkurven geschlossen bleiben, könnte man jede Kurve längs ihrer selbst aufrollen, und der Begriff wäre leer.
F: Warum ist jedes Sterngebiet einfach zusammenhängend, und warum braucht man trotzdem den allgemeineren Begriff?
A: Die Homotopie $(1-s)\vec\gamma(t)+s\vec x_0$ zieht jede Rundtour längs der Sichtlinien zum Zentrum, und jede Zwischenkurve bleibt geschlossen und im Gebiet. Es gibt aber einfach zusammenhängende Gebiete ohne Turm, der alles sieht, etwa den aufgeschnittenen Ring; für sie liefert erst der zweite Hauptsatz das Potential.
F: Was besagt der zweite Hauptsatz, und wie beweist man ihn?
A: Auf einem einfach zusammenhängenden Gebiet ist ein stetig differenzierbares Feld genau dann konservativ, wenn es die Integrabilitätsbedingung erfüllt. Eine Rundtour lässt sich zu einem stillstehenden Punkt zusammenziehen, dessen Integral null ist; die Homotopieinvarianz überträgt das auf die Rundtour (bei nur stetiger Homotopie nach einer Glättung). Nach dem Rundtour-Lemma ist das Feld dann konservativ.
F: Warum ist die gelochte Ebene nicht einfach zusammenhängend, der Raum ohne Ursprung aber schon?
A: Wäre die gelochte Ebene einfach zusammenhängend, müsste die wirbelfreie Wendeltreppe konservativ sein — sie bringt aber $2\pi$ pro Umlauf. Im Raum zeigt eine reguläre Rundtour nie in eine bestimmte Richtung $\vec e$, liegt also im Raum ohne einen Strahl, und der ist ein Sterngebiet mit dem Zentrum $-\vec e$. Dort lässt sie sich zusammenziehen.
F: Was ist die Umlaufzahl, und was ergibt der $k$-mal durchlaufene Kreis?
A: Für eine Rundtour in der gelochten Ebene ist $\frac{1}{2\pi}\oint\vec W\cdot d\vec x$ ihre Umlaufzahl um den Ursprung. Auf dem $k$-mal durchlaufenen Kreis ist der Integrand $k$, die Arbeit also $2\pi k$, die Umlaufzahl $k$. Nach der Homotopieinvarianz hängt sie nur davon ab, wie oft das Band die Säule umschlingt.
F: Warum ist das Magnetfeld eines geraden Drahts eine Wendeltreppe?
A: Außerhalb des Drahts ist $\vec H=\frac{I}{2\pi}\frac{(-y,x,0)}{x^2+y^2}$ wirbelfrei, weil dort kein Strom fließt. Auf jedem Kreis um den Draht ist die Umlaufspannung $I$, unabhängig vom Radius — das Durchflutungsgesetz. Der Raum ohne den Draht ist nicht einfach zusammenhängend, ein Gummiband um den Draht bleibt hängen, und ein Potential gibt es nicht.
:::
