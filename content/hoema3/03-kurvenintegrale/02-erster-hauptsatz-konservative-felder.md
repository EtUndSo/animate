---
title: Der erste Hauptsatz und konservative Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030200
summary: Von Grund auf – warum das Kurvenintegral eines Gradientenfelds nur von Start und Ziel abhängt, $\int_\gamma\nabla h\cdot d\vec x=h(\vec x_1)-h(\vec x_0)$. Leitbild ist ein Höhenmesser auf der Radtour – bei einem Gradientenfeld zeigt die Arbeit des Winds nur den Höhengewinn an, gleich auf welchem Weg. Mit Gebiet, Wegunabhängigkeit, Rundtour-Kriterium, dem Bau eines Potentials, der Spannung im Feld einer Punktladung und der Wendeltreppe, bei der die Rotation verschwindet und trotzdem kein Potential existiert. Mit Beispiel-Seite.
tags: erster Hauptsatz, konservatives Feld, Wegunabhängigkeit, Gradientenfeld, Potential, geschlossenes Kurvenintegral, Wirbelfeld, Gebiet
---

## Anschaulich

Auf der Radtour des vorigen Artikels hing die Arbeit des Winds vom Weg ab — im Wirbel brachte eine Rundtour sogar die
Arbeit $2\pi$. Manche Winde verhalten sich aber ganz anders.

**Das Leitbild dieses Artikels:** ein **Höhenmesser**. Stell dir einen Wind vor, der überall genau wie die Steigungspfeile
einer Landschaft bläst — bergauf, und umso stärker, je steiler es ist. Ein solcher Wind ist das Gradientenfeld $\nabla h$
einer Höhenfunktion $h$, wie im Artikel über den Gradienten. Seine Arbeit auf einer Tour ist dann genau der
**Höhengewinn**: Ziel-Höhe minus Start-Höhe. Welchen Weg man nimmt, ist egal, und auf einer Rundtour kommt null heraus —
man steht ja wieder auf derselben Höhe.

Felder mit dieser Eigenschaft heißen __konservativ__. Der __erste Hauptsatz für Kurvenintegrale__ sagt: Konservativ ist
dasselbe wie Gradientenfeld. In der Physik ist das der Grund, warum es potentielle Energie gibt; in der Elektrotechnik der
Grund, warum die Spannung zwischen zwei Punkten im elektrostatischen Feld nicht vom Weg abhängt.

Die Wendeltreppe aus dem Gradienten-Artikel ist das Gegenbild. Jede einzelne Stufe ist ein ganz normaler Hang, doch eine
Runde um die Säule bringt eine Etage nach oben. Dort kann kein Höhenmesser funktionieren — das Feld hat kein Potential,
obwohl es nirgends wirbelt. Schuld ist das Loch in der Mitte.

:::grafik
Szene: hoema3/kurvenintegrale/02-hoehenmesser · Vorlage: zwei-wege-und-wirbel-2d
Links eine Höhenlandschaft $h$ mit ihrem Steigungsfeld $\nabla h$; drei verschiedene Touren vom selben Start zum selben
Ziel, jede mit einem Arbeitszähler — alle enden beim selben Wert, dem Höhenunterschied; eine Rundtour endet bei null.
Rechts die Wendeltreppe $\vec W$ um ein Loch: Eine Runde um die Säule zeigt $2\pi$, obwohl man am Start steht. Kernaussage:
Bei Gradientenfeldern misst die Arbeit nur den Höhengewinn; die Wendeltreppe hat keinen Höhenmesser. (Rot = Potential bzw.
Landschaft, blau = Feld, orange = Touren, grau = Höhenlinien und Loch.)
:::

## Gebiete: wo man überall hinkommt

Damit „Arbeit von Start zu Ziel" für alle Punkte sinnvoll ist, muss man von jedem Punkt zu jedem anderen fahren können.

**Die Akteure:** Eine Menge $G\subseteq\mathbb{R}^n$ heißt __Gebiet__, wenn sie **offen** ist und sich je zwei ihrer Punkte
durch eine regulär parametrisierte Kurve verbinden lassen, die ganz in $G$ verläuft. Diese zweite Eigenschaft heißt
__wegzusammenhängend__.

**Im Bild:** Ein Gelände ohne unüberwindbare Grenzen. Offen heißt, um jeden Punkt ist noch ein Stückchen Platz in jede
Richtung — man kann von jedem Ort aus einen kleinen Schritt nach Osten oder Norden machen, ohne das Gelände zu verlassen.
Wegzusammenhängend heißt, man kommt von überall überall hin.

::::beispiel Gebiet oder nicht?
**(a) Die Ebene ohne Ursprung** $\mathbb{R}^2\setminus\{\vec 0\}$ ist ein Gebiet. Offen ist sie nach dem ersten Kapitel.
Und zwei Punkte $\vec x,\vec y$ verbindet man durch die Strecke zwischen ihnen — es sei denn, der Ursprung liegt darauf.
Dann fährt man über einen Punkt $\vec z$ abseits der Geraden durch $\vec x$ und $\vec y$, erst geradeaus zu $\vec z$,
dann zu $\vec y$. Diese beiden Strecken treffen die Gerade nur in $\vec x$ bzw. $\vec y$, also nicht im Ursprung.

**(b) Zwei getrennte Scheiben**

$$M = B_1\big((-2,0)\big)\cup B_1\big((2,0)\big)$$

sind offen, aber kein Gebiet. Eine stetige Kurve von der linken zur rechten Scheibe beginnt bei einer $x$-Koordinate
unter $-1$ und endet bei einer über $1$. Nach dem Zwischenwertsatz (HM1) hat sie unterwegs die $x$-Koordinate $0$ — und
dort liegt kein Punkt von $M$.

**(c) Die abgeschlossene Kreisscheibe** ist wegzusammenhängend, aber nicht offen: Um einen Randpunkt ragt jede Kugel
hinaus. Also kein Gebiet; ihr Inneres, die offene Scheibe, ist eines.

**Im Bild:** Die gelochte Ebene ist ein Gelände mit einer Säule, um die man herumfahren kann. Zwei getrennte Inseln sind
kein Gebiet — keine Tour führt von der einen zur anderen.
::::

## Wegunabhängig und konservativ

**Die Akteure:** ein Gebiet $G\subseteq\mathbb{R}^n$ und ein stetiges Vektorfeld $\vec F:G\to\mathbb{R}^n$. Das
Kurvenintegral von $\vec F$ heißt __wegunabhängig__, wenn je zwei regulär parametrisierte Kurven $\gamma,\gamma'$ in $G$
mit gleichem Anfangs- und gleichem Endpunkt denselben Wert liefern:

:::formel Definition
$$\int_\gamma\vec F\cdot d\vec x = \int_{\gamma'}\vec F\cdot d\vec x \qquad\text{für alle Kurven } \gamma,\gamma' \text{ in } G \text{ von } \vec x_0 \text{ nach } \vec x_1.$$
:::

Ein stetiges Feld mit dieser Eigenschaft heißt __konservativ__. Das Skript formuliert die Definition mit doppelpunktfreien
Kurven; wir lassen Doppelpunkte zu, dann werden die folgenden Beweise einfacher.

**Im Bild:** Die Arbeit des Winds hängt nur davon ab, wo man startet und wo man ankommt — wie die Anzeige eines
Höhenmessers.

**Rundtouren genügen.** Ob ein Feld konservativ ist, lässt sich an geschlossenen Kurven allein ablesen:

:::formel Lemma
$$\vec F \text{ konservativ in } G \quad\Longleftrightarrow\quad \oint_\gamma\vec F\cdot d\vec x = 0 \ \text{ für jede geschlossene Kurve } \gamma \text{ in } G.$$
:::

**So liest man das:** Das Zeichen $\oint$ ist ein gewöhnliches Kurvenintegral; der Kreis erinnert daran, dass die Kurve
geschlossen ist. Gemeint sind alle geschlossenen, regulär parametrisierten Kurven in $G$.

**Im Bild:** Zwei Touren mit gleichem Start und Ziel ergeben zusammen eine Rundtour — die eine hin, die andere zurück. Sie
liefern genau dann dieselbe Arbeit, wenn die Rundtour die Arbeit null bringt.

:::herleitung
**Von links nach rechts.** Sei $\vec F$ konservativ und $\vec\gamma:[a,b]\to G$ geschlossen. Man wählt eine Zwischenzeit
$c\in(a,b)$ und teilt die Rundtour dort in zwei Etappen: $\gamma_1$ von $\vec\gamma(a)$ nach $\vec\gamma(c)$ und $\gamma_2$
von $\vec\gamma(c)$ zurück nach $\vec\gamma(b)$, also zum Start. Die Etappe $\gamma_1$ und die Rückfahrt $\gamma_{2,-}$
führen beide vom Start nach $\vec\gamma(c)$, liefern also dieselbe Arbeit. Mit der Additivität und dem Vorzeichen der
Rückfahrt aus dem vorigen Artikel:

$$\oint_\gamma\vec F\cdot d\vec x = \int_{\gamma_1}\vec F\cdot d\vec x+\int_{\gamma_2}\vec F\cdot d\vec x = \int_{\gamma_1}\vec F\cdot d\vec x-\int_{\gamma_{2,-}}\vec F\cdot d\vec x = 0.$$

**Von rechts nach links.** Führen $\gamma$ und $\gamma'$ beide von $\vec x_0$ nach $\vec x_1$, so ist „erst $\gamma$, dann
$\gamma'$ rückwärts" eine geschlossene Kurve. Ihr Integral ist null, und nach der Additivität ist es die Differenz der
beiden Wege:

$$0 = \oint_{\gamma\oplus\gamma'_-}\vec F\cdot d\vec x = \int_\gamma\vec F\cdot d\vec x-\int_{\gamma'}\vec F\cdot d\vec x.$$
:::

::::beispiel Zwei Winde auf zwei Wegen
Von $(1,0)$ nach $(-1,0)$ führen der obere und der untere Halbkreis,

$$\vec\gamma_o(t) = (\cos t,\ \sin t), \qquad \vec\gamma_u(t) = (\cos t,\ -\sin t), \qquad t\in[0,\pi].$$

**Der Wirbel** $(-y,x)$ ist nicht konservativ. Oben kommt er überall mit der Stärke $1$ von hinten, die Arbeit ist $\pi$.
Unten ist die Geschwindigkeit $(-\sin t,\ -\cos t)$ und der Wind $(\sin t,\ \cos t)$, also

$$\vec F\big(\vec\gamma_u(t)\big)\cdot\dot{\vec\gamma}_u(t) = -\sin^2t-\cos^2t = -1, \qquad \int_0^\pi(-1)\,dt = -\pi.$$

Zwei Wege, zwei Ergebnisse. Passend dazu bringt die Rundtour — oben hin, unten zurück — die Arbeit

$$\pi-(-\pi) = 2\pi\neq0.$$

**Das Sattelfeld** $(y,x)$ ist konservativ. Oben und unten ist der Integrand

$$(\sin t)(-\sin t)+(\cos t)(\cos t) = \cos2t, \qquad (-\sin t)(-\sin t)+(\cos t)(-\cos t) = -\cos2t,$$

beide Integrale über $[0,\pi]$ sind null. Die Rundtour bringt null.

**Im Bild:** Beim Wirbel hat man oben Rückenwind und unten Gegenwind. Beim Sattelfeld gleichen sich auf beiden Wegen
Rücken- und Gegenwind aus — wie es ein Höhenmesser verlangt, denn Start und Ziel liegen hier auf derselben Höhe.
::::

## Der erste Hauptsatz für Kurvenintegrale

**Teil (i): der Hauptsatz für Wege.** Ist $h:G\to\mathbb{R}$ stetig differenzierbar und $\vec F=\nabla h$, so gilt für jede
regulär parametrisierte Kurve $\vec\gamma:[0,1]\to G$ mit Start und Ziel

$$\vec x_0 = \vec\gamma(0), \qquad \vec x_1 = \vec\gamma(1)$$

die Gleichung

:::formel Satz
$$\int_\gamma\nabla h\cdot d\vec x = h(\vec x_1)-h(\vec x_0).$$
:::

**So liest man das:** Links steht die Arbeit des Felds $\nabla h$ auf der Tour, rechts nur noch die Potentialwerte an Ziel
und Start — vom Weg dazwischen keine Spur. Das ist der Hauptsatz der Differential- und Integralrechnung aus HM1, übertragen
auf Wege: Das Integral einer Ableitung ist die Differenz der Randwerte. Eine Funktion $h$ mit $\nabla h=\vec F$ heißt
__Potential__ oder Stammfunktion von $\vec F$, das Feld dann __Gradientenfeld__.

**Im Bild:** Der Höhenmesser. Der Integrand ist die Rate, mit der die Höhe gerade steigt; aufsummiert ergibt sich der
Höhengewinn. Damit ist jedes Gradientenfeld konservativ.

:::herleitung
Auf jedem glatten Stück der Kurve gibt die Kettenregel aus dem ersten Kapitel die Änderungsrate der Höhe:

$$\frac{d}{dt}\,h\big(\vec\gamma(t)\big) = \nabla h\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t).$$

Der Integrand ist also eine Ableitung. Auf dem Stück $[a_{k-1},a_k]$ liefert der Hauptsatz der Differential- und
Integralrechnung

$$\int_{a_{k-1}}^{a_k}\nabla h\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)\,dt = h\big(\vec\gamma(a_k)\big)-h\big(\vec\gamma(a_{k-1})\big).$$

Summiert über alle Stücke heben sich die Zwischenwerte weg — eine Teleskopsumme —, und es bleibt
$h(\vec\gamma(1))-h(\vec\gamma(0))$.
:::

::::beispiel Drei Wege, ein Ergebnis
Das Sattelfeld ist das Gradientenfeld von $xy$:

$$\vec F(x,y) = (y,\ x) = \nabla h, \qquad h(x,y) = xy.$$

Von $(0,0)$ nach $(1,1)$ muss also jede Tour die Arbeit $h(1,1)-h(0,0)=1$ bringen. Nachgerechnet:

**(a) Diagonal**, mit $\vec\gamma(t)=(t,t)$:

$$\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = (t,t)\cdot(1,1) = 2t, \qquad \int_0^1 2t\,dt = 1.$$

**(b) Treppe**: erst nach rechts bis $(1,0)$, dann nach oben. Auf der ersten Etappe ist $y$ null, also auch der Windanteil
nach rechts; auf der zweiten ist der Windanteil nach oben gleich $x=1$:

$$0+\int_0^1 1\,dt = 1.$$

**(c) Parabel**, mit $\vec\gamma(t)=(t,t^2)$:

$$\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = (t^2,\ t)\cdot(1,\ 2t) = 3t^2, \qquad \int_0^1 3t^2\,dt = 1.$$

**Rundtour:** Auf jeder geschlossenen Kurve ist die Arbeit $h$(Start) minus $h$(Start), also null.

**Im Bild:** Drei verschiedene Wege durch die Sattellandschaft $xy$, ein Höhengewinn: Das Ziel liegt $1$ höher als der
Start.
::::

**Physikalisch** ist das die potentielle Energie. Für das elektrostatische Feld $\vec E$ mit dem Potential $\varphi$ gilt
$\vec E=-\nabla\varphi$, das Minuszeichen ist Konvention. Die Spannung von $A$ nach $B$, das Kurvenintegral von $\vec E$,
ist dann die Potentialdifferenz $\varphi(A)-\varphi(B)$ — gleich auf welchem Weg.

::::beispiel Spannung im Feld einer Punktladung
Eine Punktladung $q$ im Ursprung erzeugt im Raum ohne Ursprung das Feld und das Potential

$$\vec E(\vec x) = \frac{q}{4\pi\varepsilon_0}\,\frac{\vec x}{\lvert\vec x\rvert^3}, \qquad \varphi(\vec x) = \frac{q}{4\pi\varepsilon_0}\,\frac{1}{\lvert\vec x\rvert}.$$

Nach dem Gradienten-Artikel ist

$$\nabla\frac{1}{\lvert\vec x\rvert} = -\frac{\vec x}{\lvert\vec x\rvert^3},$$

also tatsächlich $\vec E=-\nabla\varphi$. Für jeden Weg von einem Punkt $A$ im Abstand $r_A$ zu einem Punkt $B$ im Abstand
$r_B$ ist die Spannung deshalb

$$U_{AB} = \int_{A}^{B}\vec E\cdot d\vec x = \varphi(A)-\varphi(B) = \frac{q}{4\pi\varepsilon_0}\Big(\frac1{r_A}-\frac1{r_B}\Big).$$

**In Zahlen:** Mit

$$q = 1\,\text{nC}, \qquad r_A = 1\,\text{cm}, \qquad r_B = 2\,\text{cm}, \qquad \frac{1}{4\pi\varepsilon_0}\approx 8{,}99\cdot10^9\,\frac{\text{Vm}}{\text{C}}$$

ist

$$U_{AB} \approx 8{,}99\cdot10^9\cdot10^{-9}\cdot(100-50)\,\text{V} \approx 450\,\text{V}.$$

**Im Bild:** Nur die Abstände zählen. Ob man radial nach außen geht oder in einem Bogen um die Ladung, ändert nichts —
Bögen auf einer Kugel um die Ladung leisten gar keine Arbeit, weil das Feld dort senkrecht zur Bewegung steht.
::::

**Teil (ii): konservativ ist dasselbe wie Gradientenfeld.** Für ein stetiges Vektorfeld $\vec F:G\to\mathbb{R}^n$ gilt

:::formel Satz
$$\vec F \text{ konservativ in } G \quad\Longleftrightarrow\quad \vec F \text{ ist ein Gradientenfeld in } G.$$
:::

**So liest man das:** Von rechts nach links ist das Teil (i). Die neue Richtung sagt: Wenn die Arbeit nur von Start und
Ziel abhängt, **gibt** es eine Höhenfunktion, deren Steigungsfeld der Wind ist.

**Im Bild:** Man baut den Höhenmesser selbst. Man wählt einen Startpunkt und erklärt die Höhe jedes Punkts als die Arbeit
des Winds auf irgendeiner Tour dorthin — welche Tour, ist bei einem konservativen Wind egal. Ein kleiner Schritt nach Osten
ändert diese Höhe dann um den Ostanteil des Winds mal Schrittlänge.

:::grafik
Szene: hoema3/kurvenintegrale/02-hoehenmesser-bauen · Vorlage: feld-und-kurve-2d
Ein konservatives Windfeld mit einem markierten Startpunkt $\vec x_0$. Ein Punkt $\vec x$ wird mit der Maus bewegt; drei
verschiedene Touren von $\vec x_0$ nach $\vec x$ zeigen alle dieselbe Arbeit, die als Höhe $h(\vec x)$ über dem Punkt
aufgetragen wird — so wächst Punkt für Punkt eine Landschaft. Ein kurzer Schritt $s\,\vec e_1$ nach Osten hebt die Höhe um
etwa $F_1\,s$. Kernaussage: Bei einem konservativen Feld baut die Arbeit vom Startpunkt aus die Landschaft, deren
Steigungsfeld das Feld ist. (Blau = Feld, orange = Touren, rot = entstehende Landschaft $h$, grau = Achsen.)
:::

:::herleitung
Die Richtung von rechts nach links ist Teil (i). Für die andere fixiert man einen Punkt $\vec x_0\in G$. Weil $G$ ein Gebiet
ist, gibt es zu jedem $\vec x\in G$ eine Kurve von $\vec x_0$ nach $\vec x$, und man setzt

$$h(\vec x) := \int_{\gamma(\vec x)}\vec F\cdot d\vec y.$$

Wegen der Wegunabhängigkeit hängt der Wert nicht davon ab, welche Kurve $\gamma(\vec x)$ man nimmt.

**Ein Schritt in Richtung $\vec e_k$.** Weil $G$ offen ist, liegt die Strecke von $\vec x$ nach $\vec x+s\,\vec e_k$ für
kleine $s\neq0$ ganz in $G$. Fährt man erst $\gamma(\vec x)$ und dann diese Strecke, kommt man von $\vec x_0$ nach
$\vec x+s\,\vec e_k$. Wegunabhängigkeit und Additivität geben

$$h(\vec x+s\,\vec e_k)-h(\vec x) = \int_{\text{Strecke}}\vec F\cdot d\vec y.$$

Mit der Parametrisierung der Strecke

$$\vec y(t) = \vec x+t\,s\,\vec e_k, \qquad \dot{\vec y}(t) = s\,\vec e_k, \qquad t\in[0,1],$$

wird der Integrand die $k$-te Komponente des Felds mal $s$:

$$\frac{h(\vec x+s\,\vec e_k)-h(\vec x)}{s} = \int_0^1 F_k(\vec x+t\,s\,\vec e_k)\,dt.$$

Für $s\to0$ strebt der Integrand gleichmäßig gegen $F_k(\vec x)$, weil $F_k$ stetig ist, also auch das Integral. Damit
existieren alle partiellen Ableitungen,

$$\frac{\partial h}{\partial x_k}(\vec x) = F_k(\vec x),$$

und sie sind stetig. Also ist $h$ stetig differenzierbar mit $\nabla h=\vec F$.
:::

::::beispiel Ein Potential bauen
Für das Feld

$$\vec F(x,y) = (2xy+1,\ x^2)$$

baut man den Höhenmesser vom Ursprung aus. **Treppenweg** zum Punkt $(x,y)$: erst nach rechts bis $(x,0)$, dann nach oben
bis $(x,y)$. Auf der ersten Stufe zählt nur der Windanteil nach rechts, auf der zweiten nur der nach oben:

$$F_1(t,0) = 1, \qquad F_2(x,t) = x^2.$$

Also

$$h(x,y) = \int_0^x 1\,dt+\int_0^y x^2\,dt = x+x^2y.$$

**Probe:**

$$\nabla h = (1+2xy,\ x^2) = \vec F.$$

Damit ist $\vec F$ ein Gradientenfeld, also konservativ. **Zur Kontrolle diagonal**, mit $\vec y(t)=t\,(x,y)$:

$$\vec F(tx,ty)\cdot(x,y) = (2t^2xy+1)\,x+t^2x^2\,y = 3t^2x^2y+x, \qquad \int_0^1\big(3t^2x^2y+x\big)\,dt = x^2y+x.$$

**Im Bild:** Zwei verschiedene Wege zum selben Punkt, dieselbe Höhe — so muss es bei einem Höhenmesser sein. Der Treppenweg
ist meist der bequemste, weil auf jeder Stufe nur eine Komponente des Felds zählt.
::::

## Rotation null: notwendig, aber nicht hinreichend

In zwei und drei Dimensionen gibt es einen schnellen Test. Für ein stetig differenzierbares Feld gilt:

$$\vec F \text{ konservativ in } G \quad\Longrightarrow\quad \operatorname{rot}\vec F = \vec 0 \ \text{ in } G.$$

In der Ebene ist dabei die Rotation die Zahl $\partial_1F_2-\partial_2F_1$, wie im Artikel über Divergenz und Rotation.

**Im Bild:** In einer echten Landschaft dreht sich kein Schaufelrad — Steigungsfelder haben keinen Wirbel.

:::herleitung
Nach Teil (ii) ist $\vec F=\nabla h$. Weil $\vec F$ stetig differenzierbar ist, ist $h$ sogar zweimal stetig
differenzierbar. Dann ist die Rotation eines Gradientenfelds null (Rechenregeln-Artikel), in der Ebene etwa

$$\partial_1F_2-\partial_2F_1 = \frac{\partial^2h}{\partial x_1\,\partial x_2}-\frac{\partial^2h}{\partial x_2\,\partial x_1} = 0$$

nach dem Satz von Schwarz.
:::

**Die Umkehrung ist falsch.** Ein Feld kann überall wirbelfrei sein und trotzdem kein Potential haben — wenn das Gebiet ein
Loch hat. Das Gegenbeispiel des Skripts ist die Wendeltreppe aus dem Gradienten-Artikel.

::::beispiel Die Wendeltreppe
Auf dem Gebiet $G=\mathbb{R}^2\setminus\{\vec 0\}$ sei

$$\vec W(x,y) = \frac{1}{x^2+y^2}\,(-y,\ x).$$

**Wirbelfrei.** Im Gradienten-Artikel wurde nachgerechnet, dass beide gemischten Ableitungen übereinstimmen,

$$\frac{\partial W_1}{\partial y} = \frac{y^2-x^2}{(x^2+y^2)^2} = \frac{\partial W_2}{\partial x},$$

also ist die Rotation null.

**Trotzdem nicht konservativ.** Auf dem Kreis $K_R$ vom Radius $R>0$, gegen den Uhrzeigersinn,

$$\vec\gamma(t) = (R\cos t,\ R\sin t), \qquad \dot{\vec\gamma}(t) = R\,(-\sin t,\ \cos t), \qquad t\in[0,2\pi],$$

ist der Wind $\frac1R(-\sin t,\ \cos t)$ und der Integrand

$$\frac1R\,(-\sin t,\ \cos t)\cdot R\,(-\sin t,\ \cos t) = 1, \qquad \oint_{K_R}\vec W\cdot d\vec x = 2\pi.$$

Das gilt für **jeden** Radius. Eine Rundtour mit Arbeit $2\pi\neq0$ — nach dem Lemma über Rundtouren ist $\vec W$ nicht
konservativ und nach Teil (ii) kein Gradientenfeld.

**Im Bild:** Jede Stufe der Wendeltreppe ist ein normaler Hang, nirgends dreht sich ein Schaufelrad. Wer aber einmal um die
Säule im Ursprung fährt, ist eine Etage höher. Bemerkenswert: Der Radius spielt keine Rolle — enge und weite Runden um die
Säule bringen dieselben $2\pi$.

:::grafik
Szene: hoema3/kurvenintegrale/02-wendeltreppe-umlauf · Vorlage: wendeltreppe-loch-2d
Das Feld $\vec W$ um die Säule im Ursprung als Wendeltreppe. Drei Rundtouren mit verschiedenen Radien laufen gleichzeitig;
jeder Arbeitszähler zeigt am Ende $2\pi$. Ein kleines Schaufelrad an beliebiger Stelle dreht sich nicht. Kernaussage:
Wirbelfrei an jeder Stelle, und trotzdem bringt jeder Umlauf um das Loch $2\pi$. (Blau = Feld, orange = Rundtouren, grau =
Säule.)
:::
::::

**Lokal gibt es doch ein Potential.** Wer die Säule nicht umrunden kann, merkt nichts von der Treppe: In der rechten
Halbebene der Punkte mit $x>0$ ist der __Polarwinkel__ ein Potential von $\vec W$,

$$\theta(x,y) = \arctan\frac{y}{x}, \qquad \nabla\theta = \vec W \quad\text{für } x>0.$$

:::herleitung
Mit der Ableitung des Arcustangens und der Kettenregel:

$$\frac{\partial\theta}{\partial x} = \frac{1}{1+\frac{y^2}{x^2}}\cdot\Big(-\frac{y}{x^2}\Big) = -\frac{y}{x^2+y^2}, \qquad \frac{\partial\theta}{\partial y} = \frac{1}{1+\frac{y^2}{x^2}}\cdot\frac1x = \frac{x}{x^2+y^2}.$$

Das sind genau die Komponenten von $\vec W$.
:::

**Im Bild:** Der Polarwinkel ist die „Etagenhöhe" auf der Wendeltreppe. Auf einem Stück Treppe ohne volle Runde ist er ein
guter Höhenmesser. Auf der ganzen gelochten Ebene lässt er sich aber nicht stetig erklären — nach einer Runde müsste er um
$2\pi$ größer sein als am Start.

::::beispiel Zwei Wege um die Säule
Von $(1,-1)$ nach $(1,1)$ führen zwei Wege durch $G$:

**Rechts vorbei**, auf der Strecke mit $x=1$, ganz in der rechten Halbebene. Dort ist der Polarwinkel ein Potential, die
Arbeit also die Winkeldifferenz:

$$\theta(1,1)-\theta(1,-1) = \frac{\pi}{4}-\Big(-\frac{\pi}{4}\Big) = \frac{\pi}{2}.$$

Direkt nachgerechnet: Auf der Strecke $(1,t)$ ist der Windanteil nach oben $W_2(1,t)$, also

$$\int_{-1}^{1}\frac{1}{1+t^2}\,dt = \arctan1-\arctan(-1) = \frac{\pi}{2}.$$

**Links herum**, im Uhrzeigersinn auf dem Kreis vom Radius $\sqrt2$ durch $(-\sqrt2,0)$: Der Winkel fällt von
$-\tfrac{\pi}{4}$ um $\tfrac{3\pi}{2}$. Wie auf dem Kreis $K_R$ ist der Integrand konstant, jetzt aber $-1$, weil man gegen
die Pfeile fährt:

$$\int_0^{3\pi/2}(-1)\,dt = -\frac{3\pi}{2}.$$

Die beiden Ergebnisse unterscheiden sich um

$$\frac{\pi}{2}-\Big(-\frac{3\pi}{2}\Big) = 2\pi$$

— genau eine Runde um die Säule.

**Im Bild:** Rechts vorbei steigt man eine Viertel-Etage hinauf, links herum steigt man drei Viertel hinab. Zusammen ist das
eine volle Runde, und die ist auf der Wendeltreppe eine ganze Etage wert.
::::

## Bedeutung und Ausblick

Der erste Hauptsatz macht aus einem Wegintegral eine bloße Differenz von Randwerten — sobald man ein Potential kennt. Er
erklärt, warum potentielle Energie und elektrisches Potential sinnvolle Größen sind: Die Arbeit einer konservativen Kraft
hängt nur von Start und Ziel ab. Umgekehrt zeigt er, woran man nicht-konservative Felder erkennt: an einer Rundtour, die
Arbeit leistet. Das ist der Normalfall bei der __Induktion__. Ein zeitlich veränderliches Magnetfeld erzeugt ein elektrisches
Feld, dessen Umlaufintegral längs einer Leiterschleife die induzierte Spannung ist — dieses Feld ist nicht konservativ.

Offen bleibt die praktische Frage: Wann folgt aus der verschwindenden Rotation **doch** ein Potential? Die Wendeltreppe zeigt,
dass die Gestalt des Gebiets mitentscheidet. Das __Poincaré-Lemma__ im nächsten Artikel gibt die Antwort für Gebiete ohne
solche Löcher und liefert dazu eine Formel, mit der man das Potential direkt ausrechnet.

:::kern
- Ein __Gebiet__ ist offen und wegzusammenhängend: Man kommt von jedem Punkt zu jedem anderen.
- __Konservativ__ heißt: Die Arbeit hängt nur von Start und Ziel ab — wie die Anzeige eines Höhenmessers.
- Gleichwertig: Jede Rundtour bringt die Arbeit null, $\oint_\gamma\vec F\cdot d\vec x=0$.
- __Erster Hauptsatz__ (i): $\int_\gamma\nabla h\cdot d\vec x=h(\vec x_1)-h(\vec x_0)$ — Kettenregel plus Hauptsatz aus HM1.
- (ii): Konservativ ist dasselbe wie Gradientenfeld; das Potential baut man als Arbeit vom festen Startpunkt aus.
- Physik: Die Spannung im elektrostatischen Feld ist die Potentialdifferenz, unabhängig vom Weg.
- In 2D und 3D ist $\operatorname{rot}\vec F=\vec 0$ **notwendig** für ein Potential, aber nicht hinreichend.
- Gegenbeispiel Wendeltreppe: wirbelfrei auf der gelochten Ebene, aber jeder Umlauf um das Loch bringt $2\pi$.
- Lokal, ohne Umrundung des Lochs, ist der Polarwinkel ein Potential der Wendeltreppe.
:::

:::quiz
F: Was ist ein Gebiet, und warum ist die Ebene ohne Ursprung eines, zwei getrennte Scheiben aber nicht?
A: Eine offene Menge, in der sich je zwei Punkte durch eine Kurve in der Menge verbinden lassen. In der gelochten Ebene verbindet man zwei Punkte durch die Strecke oder, wenn der Ursprung im Weg liegt, über einen Punkt abseits der Geraden. Zwischen zwei getrennten Scheiben müsste eine stetige Kurve nach dem Zwischenwertsatz die Lücke kreuzen, in der kein Punkt der Menge liegt.
F: Was heißt konservativ, und warum genügt es, Rundtouren zu prüfen?
A: Konservativ heißt, dass das Kurvenintegral nur von Anfangs- und Endpunkt abhängt. Zwei Wege mit gleichem Start und Ziel ergeben, den einen rückwärts gefahren, eine Rundtour; ihre Arbeit ist die Differenz der beiden Wege. Also liefern alle Wege dasselbe genau dann, wenn jede Rundtour die Arbeit null bringt.
F: Was besagt der erste Hauptsatz (i), und wie beweist man ihn?
A: Für ein Gradientenfeld ist $\int_\gamma\nabla h\cdot d\vec x=h(\vec x_1)-h(\vec x_0)$. Nach der Kettenregel ist der Integrand die Ableitung $\frac{d}{dt}h(\vec\gamma(t))$; der Hauptsatz aus HM1 gibt auf jedem glatten Stück die Differenz der Randwerte, und über die Stücke summiert bleibt eine Teleskopsumme. Im Bild zeigt der Höhenmesser nur den Höhengewinn an.
F: Warum liefern beim Sattelfeld $(y,x)$ Diagonale, Treppe und Parabel von $(0,0)$ nach $(1,1)$ alle die Arbeit $1$?
A: Weil $(y,x)=\nabla(xy)$ ein Gradientenfeld ist; die Arbeit ist $h(1,1)-h(0,0)=1$. Nachgerechnet: diagonal $\int_0^1 2t\,dt$, auf der Treppe $0+1$, auf der Parabel $\int_0^1 3t^2\,dt$ — jeweils $1$. Jede Rundtour bringt null.
F: Warum ist die Spannung im Feld einer Punktladung wegunabhängig, und welchen Wert hat sie?
A: Das Feld ist $\vec E=-\nabla\varphi$ mit $\varphi=\frac{q}{4\pi\varepsilon_0}\frac1{\lvert\vec x\rvert}$, also ein Gradientenfeld. Nach dem ersten Hauptsatz ist die Spannung von $A$ nach $B$ die Potentialdifferenz $\frac{q}{4\pi\varepsilon_0}(\frac1{r_A}-\frac1{r_B})$; für $1\,\text{nC}$ zwischen $1\,\text{cm}$ und $2\,\text{cm}$ rund $450\,\text{V}$. Bögen um die Ladung leisten keine Arbeit.
F: Wie baut man aus einem konservativen Feld ein Potential, und warum ist $\partial h/\partial x_k=F_k$?
A: Man setzt $h(\vec x)$ gleich der Arbeit auf irgendeiner Kurve von einem festen $\vec x_0$ nach $\vec x$ — wegen der Wegunabhängigkeit eindeutig. Ein kleiner Schritt $s\,\vec e_k$ ändert $h$ um die Arbeit auf der Strecke, also um $s\int_0^1F_k(\vec x+ts\vec e_k)\,dt$. Geteilt durch $s$ strebt das wegen der Stetigkeit gegen $F_k(\vec x)$.
F: Wie findet man für $\vec F=(2xy+1,\,x^2)$ ein Potential?
A: Auf dem Treppenweg vom Ursprung: erst nach rechts, wo der Windanteil $F_1(t,0)=1$ ist, dann nach oben, wo er $F_2(x,t)=x^2$ ist. Das gibt $h=x+x^2y$, und die Probe $\nabla h=(1+2xy,\,x^2)$ bestätigt es. Auch der diagonale Weg liefert $x^2y+x$.
F: Warum folgt aus „konservativ" in 2D und 3D, dass die Rotation verschwindet, und warum nicht umgekehrt?
A: Ein konservatives Feld ist ein Gradientenfeld $\nabla h$; bei stetig differenzierbarem Feld ist $h$ zweimal stetig differenzierbar, und nach Schwarz ist die Rotation null. Umgekehrt reicht das nicht: Die Wendeltreppe $\vec W=\frac{(-y,x)}{x^2+y^2}$ ist auf der gelochten Ebene wirbelfrei, aber jeder Umlauf um das Loch bringt $2\pi$.
F: Warum hängt der Umlauf der Wendeltreppe nicht vom Radius ab?
A: Auf dem Kreis vom Radius $R$ ist der Wind $\frac1R(-\sin t,\cos t)$ und die Geschwindigkeit $R(-\sin t,\cos t)$; der Integrand ist $1$, die Arbeit $2\pi$ für jedes $R$. Im Bild bringt jede Runde um die Säule eine ganze Etage, egal wie eng sie ist.
F: In welchem Sinn hat die Wendeltreppe doch ein Potential, und was zeigen die zwei Wege von $(1,-1)$ nach $(1,1)$?
A: In der rechten Halbebene ist der Polarwinkel $\theta=\arctan\frac yx$ ein Potential, denn $\nabla\theta=\vec W$. Rechts vorbei ist die Arbeit die Winkeldifferenz $\frac{\pi}{2}$, links herum um die Säule $-\frac{3\pi}{2}$. Der Unterschied ist $2\pi$, eine volle Runde — ein globales Potential kann es deshalb nicht geben.
:::
