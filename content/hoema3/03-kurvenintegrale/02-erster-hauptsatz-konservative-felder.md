---
title: Der erste Hauptsatz und konservative Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030200
summary: Von Grund auf – warum das Kurvenintegral eines Gradientenfelds nur von Anfangs- und Endpunkt abhängt, $\int_\gamma \nabla h\cdot dx=h(x_1)-h(x_0)$ (der Hauptsatz für Kurvenintegrale). Die drei gleichwertigen Gesichter: wegunabhängig ⟺ Gradientenfeld ⟺ jedes geschlossene Integral null. In 2D/3D ist $\operatorname{rot}F=0$ notwendig, aber auf Gebieten mit Loch nicht hinreichend – das berühmte Wirbelfeld.
tags: erster Hauptsatz, konservatives Feld, Wegunabhängigkeit, Gradientenfeld, Potential, geschlossenes Kurvenintegral, Wirbelfeld, Gebiet
---

## Anschaulich

Beim Wirbelfeld-Beispiel des vorigen Artikels kam entlang eines Weges ein echter Wert heraus. Bei anderen Feldern
aber hängt das Kurvenintegral **nur von Anfangs- und Endpunkt** ab, nicht vom Weg dazwischen.

Denk an eine Höhenlandschaft (ein Potential $h$). Egal, welchen Weg ein Wanderer von $A$ nach $B$ nimmt — sein
Netto-Höhengewinn ist immer $h(B)-h(A)$. Auf einem **Rundweg** zurück zum Start kommt null heraus.

Felder mit dieser Eigenschaft heißen __konservativ__, und sie sind genau die __Gradientenfelder__ $F=\nabla h$.
Das Kurvenintegral ist dann schlicht die **Potentialdifferenz** — der Hauptsatz der Differential- und
Integralrechnung, übertragen auf Wege. In der Physik: „Die Arbeit einer konservativen Kraft ist die Differenz der
potentiellen Energie" (Spannung = Potentialdifferenz).

Ein Kontrast schärft das Bild: Ein Wirbelfeld um ein kleines **Loch** gibt auf einem Rundweg $2\pi\neq0$ — es hat
kein Potential. Die Gestalt des Gebiets entscheidet mit.

:::grafik
Szene: hoema3/kurvenintegrale/02-wegunabhaengig-vs-wirbel · Vorlage: zwei-wege-und-wirbel-2d
Links eine Höhenlandschaft $h$ mit zwei verschiedenen Wegen zwischen demselben Start und Ziel; beide „Arbeits"-Zähler
$\int_\gamma\nabla h\cdot dx$ enden beim selben Wert $h(\text{Ziel})-h(\text{Start})$, ein Rundweg bei null. Rechts
als Kontrast ein Wirbelfeld um ein Loch bei $0$: Rundweg gibt $2\pi\neq0$. (Rot = Potential/Feld, orange = Wege,
grau = Höhenlinien/Loch.)
:::

## Gebiet, Wegunabhängigkeit, konservativ

Ein __Gebiet__ $G\subset\mathbb{R}^n$ ist eine **offene** und **wegzusammenhängende** Menge — je zwei Punkte lassen
sich durch eine ganz in $G$ verlaufende Kurve verbinden.

Auf einem Gebiet heißt das Kurvenintegral von $F$ __wegunabhängig__, wenn $\int_\gamma F\cdot dx=\int_{\gamma'}
F\cdot dx$ für **alle** regulären Kurven $\gamma,\gamma'$ in $G$ mit gleichem Anfangs- und Endpunkt gilt. Ein
stetiges Feld mit dieser Eigenschaft heißt __konservativ__.

Dazu gleichwertig ist eine besonders handliche Bedingung:

:::formel Lemma
$$F \text{ konservativ} \quad\Longleftrightarrow\quad \oint_\gamma F\cdot dx = 0 \ \text{ für jede geschlossene Kurve } \gamma \text{ in } G.$$
:::

Der Grund: Zwei Wege mit gleichen Enden bilden zusammen — einer davon rückwärts durchlaufen — einen geschlossenen
Weg. Die Differenz ihrer Integrale ist genau dieses Umlaufintegral; es verschwindet also **genau dann**, wenn
beide Wege denselben Wert liefern.

## Der erste Hauptsatz für Kurvenintegrale

Jetzt der Kern. Ist $h:G\to\mathbb{R}$ stetig differenzierbar und $F=\nabla h$ ein **Gradientenfeld**, so gilt für
jede reguläre Kurve $\gamma$ von $x_0=\gamma(0)$ nach $x_1=\gamma(1)$:

:::formel Satz
$$\int_\gamma \nabla h\cdot dx = h(x_1) - h(x_0).$$
:::

Die rechte Seite enthält **keine Spur** mehr vom Weg — nur die beiden Endpunkte. Jedes Gradientenfeld ist also
wegunabhängig.

:::herleitung
Nach der Kettenregel (Kapitel 1) ist die Änderung des Potentials längs der Kurve

$$\frac{d}{dt}\,h(\gamma(t)) = \nabla h(\gamma(t))\cdot\dot\gamma(t) = F(\gamma(t))\cdot\dot\gamma(t).$$

Der Integrand des Kurvenintegrals ist also gerade diese Ableitung. Nach dem Hauptsatz der Differential- und
Integralrechnung folgt

$$\int_\gamma F\cdot dx = \int_0^1 \frac{d}{dt}h(\gamma(t))\,dt = h(\gamma(1)) - h(\gamma(0)).$$
:::

**Eigenes Beispiel.** Das Feld $F(x,y)=(y,x)$ ist der Gradient von $h(x,y)=xy$ (denn $\nabla(xy)=(y,x)$). Für jeden
Weg von $(0,0)$ nach $(1,1)$ ist daher

$$\int_\gamma F\cdot dx = h(1,1)-h(0,0) = 1-0 = 1,$$

egal ob erst nach rechts dann nach oben oder diagonal. Rundwege geben $0$.

## Konservativ ist dasselbe wie Gradientenfeld

Der Hauptsatz liefert die eine Richtung (Gradientenfeld $\Rightarrow$ konservativ). Es gilt aber die volle
Äquivalenz, in jeder Dimension:

:::formel Satz
$$F \text{ konservativ in } G \quad\Longleftrightarrow\quad F \text{ ist ein Gradientenfeld in } G.$$
:::

:::herleitung
Für die noch fehlende Richtung (konservativ $\Rightarrow$ Gradientenfeld) **baut** man das Potential direkt. Man
fixiert $x_0\in G$ und setzt

$$h(x) := \int_{\gamma(x)} F\cdot dy \quad\text{über irgendeinen Weg von } x_0 \text{ nach } x.$$

Wegen der Wegunabhängigkeit ist das wohldefiniert. Geht man ein kleines Stück $s$ in Koordinatenrichtung
$\hat e_k$ weiter, liefert der Mittelwertsatz der Integralrechnung

$$\frac{h(x+s\hat e_k)-h(x)}{s} = F_k(x+t_0\hat e_k) \xrightarrow{\,s\to0\,} F_k(x),$$

also $\frac{\partial h}{\partial x_k}=F_k$ für alle $k$, d. h. $\nabla h=F$.
:::

Physikalisch ist das der Grund, warum man einem Punkt überhaupt ein eindeutiges Potential (eine potentielle
Energie, eine Spannung) zuordnen darf.

## Notwendig, aber nicht hinreichend: $\operatorname{rot}F=0$

In $n=2,3$ folgt aus „$F$ ist Gradientenfeld" sofort $\operatorname{rot}F=0$ (das ist
$\operatorname{rot}\operatorname{grad}h=0$ aus Kapitel 1). Also ist $\operatorname{rot}F=0$ eine **notwendige**
Bedingung für Konservativität.

**Die Umkehrung gilt im Allgemeinen nicht** — aus einem topologischen Grund: Hat das Gebiet ein **Loch**, kann ein
Feld überall wirbelfrei sein und trotzdem kein Potential besitzen.

**Das berühmte Gegenbeispiel** auf $G=\mathbb{R}^2\setminus\{0\}$ (Ebene ohne Ursprung):

$$F(x,y) = \frac{1}{x^2+y^2}\begin{pmatrix}-y\\x\end{pmatrix}.$$

:::herleitung
Man rechnet nach, dass $\operatorname{rot}F=\partial_x F_2-\partial_y F_1=0$ überall in $G$. Dennoch ist das
Integral über den einmal gegen den Uhrzeigersinn durchlaufenen Kreis $K_R$ (Radius $R$, $\gamma(t)=(R\cos t,R\sin t)$):

$$\oint_{K_R} F\cdot dx = \int_0^{2\pi} \frac{1}{R^2}(-R\sin t,\,R\cos t)\cdot(-R\sin t,\,R\cos t)\,dt = \int_0^{2\pi} 1\,dt = 2\pi \neq 0.$$

Ein Gradientenfeld hätte auf jeder geschlossenen Kurve das Integral $0$ — also ist $F$ auf $G$ **kein**
Gradientenfeld, obwohl es wirbelfrei ist.
:::

Der „Schuldige" ist das Loch bei $0$: Der Kreis umschließt es, und das $2\pi$ ist gerade der Umlaufwinkel. Lokal,
in jeder lochfreien Umgebung, **gibt** es ein Potential (den Polarwinkel $\varphi$) — nur global nicht eindeutig,
weil $\varphi$ beim Umrunden um $2\pi$ springt.

:::grafik
Szene: hoema3/kurvenintegrale/02-wirbelfeld-loch · Vorlage: wirbelfeld-punktierte-ebene-2d
Das Wirbelfeld $F=\frac{(-y,x)}{x^2+y^2}$ auf der punktierten Ebene: kreisende Pfeile um das Loch bei $0$,
$\operatorname{rot}F=0$ an jedem Punkt, aber Umlauf $\oint_{K_R}=2\pi$. Daneben eine lochfreie Umgebung, in der
lokal ein Potential (der Winkel $\varphi$) existiert. (Blau = Feld, orange = Umlaufkreis, grau = Loch.)
:::

**Stolperstein:** $\operatorname{rot}F=0$ allein garantiert **kein** Potential. Erst die Gestalt des Gebiets
entscheidet — auf „lochfreien" (einfach zusammenhängenden) Gebieten ist $\operatorname{rot}F=0$ doch hinreichend.

## Bedeutung und Ausblick

Der erste Hauptsatz ist das mehrdimensionale Gegenstück zum Hauptsatz der Differential- und Integralrechnung: Er
macht aus einem Wegintegral eine bloße Differenz von Randwerten — und erklärt, warum Spannung und potentielle
Energie überhaupt wohldefinierte Größen sind.

Bleibt die Frage: Wann reicht $\operatorname{rot}F=0$ **doch** für ein Potential? Die Antwort hängt an der
Topologie des Gebiets. Das __Poincaré-Lemma__ zeigt, dass die Bedingung **lokal** immer hinreichend ist — das
Thema des nächsten Artikels.

:::kern
- Ein __Gebiet__ ist offen + wegzusammenhängend. $F$ heißt __konservativ__, wenn die Kurvenintegrale nur von Anfangs-/Endpunkt abhängen — gleichwertig: $\oint_\gamma F\cdot dx=0$ für jede geschlossene Kurve.
- __Erster Hauptsatz:__ für ein Gradientenfeld $F=\nabla h$ ist $\int_\gamma F\cdot dx=h(x_1)-h(x_0)$ (Beweis: $\tfrac{d}{dt}h(\gamma)=\nabla h\cdot\dot\gamma$ + Hauptsatz) — also wegunabhängig.
- Zentrale Äquivalenz: $F$ konservativ $\Leftrightarrow$ $F$ Gradientenfeld (Potential $h(x)=\int_{x_0}^x F\cdot dy$, MWT $\Rightarrow\partial_{x_k}h=F_k$).
- In 2D/3D ist $\operatorname{rot}F=0$ **notwendig** ($\operatorname{rot}\operatorname{grad}=0$), aber **nicht hinreichend** auf Gebieten mit Loch.
- Gegenbeispiel: $F=\tfrac{(-y,x)}{x^2+y^2}$ auf $\mathbb{R}^2\setminus\{0\}$ hat $\operatorname{rot}F=0$, aber $\oint_{K_R}F\cdot dx=2\pi$. Eigenes Beispiel: $F=(y,x)=\nabla(xy)$ gibt zwischen $(0,0)$ und $(1,1)$ stets $1$.
:::

:::quiz
F: Was besagt der erste Hauptsatz für Kurvenintegrale, und warum fällt der Weg aus dem Ergebnis heraus?
A: Für ein Gradientenfeld ist $\int_\gamma\nabla h\cdot dx=h(x_1)-h(x_0)$ — nur die Endpunkte zählen. Grund: Nach der Kettenregel ist der Integrand gerade $\frac{d}{dt}h(\gamma(t))$, und der Hauptsatz der Differential- und Integralrechnung liefert die Differenz der Randwerte, unabhängig vom dazwischenliegenden Weg.
F: Was heißt „konservativ", und warum ist das gleichwertig zu „jedes geschlossene Integral ist null"?
A: Konservativ heißt: die Kurvenintegrale hängen nur von Anfangs- und Endpunkt ab. Zwei Wege mit gleichen Enden bilden, wenn man einen rückwärts durchläuft, einen geschlossenen Weg; die Differenz ihrer Integrale ist genau dieses Umlaufintegral. Es ist also null ⟺ beide Wege liefern dasselbe.
F: Warum ist jedes Gradientenfeld automatisch konservativ?
A: Nach dem ersten Hauptsatz ist sein Kurvenintegral die Potentialdifferenz $h(x_1)-h(x_0)$. Diese hängt nur von den Endpunkten ab — damit ist das Feld per Definition wegunabhängig, also konservativ.
F: Wie konstruiert man aus einem konservativen Feld ein Potential, und warum ist es wohldefiniert?
A: Man setzt $h(x):=\int_{x_0}^{x}F\cdot dy$ über irgendeinen Weg von einem festen $x_0$ nach $x$. Wegen der Wegunabhängigkeit ist der Wert vom gewählten Weg unabhängig (wohldefiniert); ein kleiner Schritt in Richtung $\hat e_k$ zeigt mit dem Mittelwertsatz $\partial h/\partial x_k=F_k$, also $\nabla h=F$.
F: Was ist die physikalische Bedeutung des Hauptsatzes (Arbeit, Spannung)?
A: Die Arbeit einer konservativen Kraft hängt nur von Start und Ziel ab und ist die Differenz der potentiellen Energie. In der Elektrotechnik ist die Spannung genau das Wegintegral des $E$-Feldes, also die Potentialdifferenz $\varphi(x_0)-\varphi(x_1)$ — unabhängig vom gewählten Weg.
F: Warum ist $\operatorname{rot}F=0$ notwendig für Konservativität, aber nicht hinreichend?
A: Notwendig, weil ein Gradientenfeld stets $\operatorname{rot}\operatorname{grad}h=0$ erfüllt. Nicht hinreichend, weil auf einem Gebiet mit „Loch" ein Feld überall wirbelfrei sein und trotzdem kein globales Potential besitzen kann — die Topologie des Gebiets entscheidet mit.
F: Beim Wirbelfeld $F=\frac{(-y,x)}{x^2+y^2}$: Warum ist $\operatorname{rot}F=0$ überall, der Umlauf aber $\oint_{K_R}=2\pi$?
A: Lokal ist $F$ der Gradient des Polarwinkels $\varphi$, also wirbelfrei. Der Kreis $K_R$ umschließt aber das Loch bei $0$; beim vollen Umlauf wächst $\varphi$ um $2\pi$. Dieser Sprung ist gerade das Integral — er entsteht nur, weil das Loch eingeschlossen wird.
F: Warum beweist $\oint_{K_R}F\cdot dx=2\pi\neq0$, dass $F$ kein Gradientenfeld ist?
A: Ein Gradientenfeld hat auf **jeder** geschlossenen Kurve das Integral $0$ (erster Hauptsatz). Ein Umlaufwert $2\pi\neq0$ widerspricht dem — also kann $F$ auf $\mathbb{R}^2\setminus\{0\}$ kein Potential besitzen.
F: Was bedeutet es, dass beim Wirbelfeld „lokal ein Potential existiert, global aber nicht"?
A: In jeder lochfreien Umgebung lässt sich der Winkel $\varphi$ eindeutig als Potential wählen ($F=\nabla\varphi$). Global scheitert das, weil $\varphi$ beim Umrunden des Lochs um $2\pi$ springt — es gibt keine über ganz $G$ eindeutige Potentialfunktion.
F: Welche Eigenschaft des Gebiets macht $\operatorname{rot}F=0$ doch hinreichend für ein Potential?
A: Ein **einfach zusammenhängendes** (lochfreies) Gebiet: Dort lässt sich jede geschlossene Kurve zusammenziehen, und $\operatorname{rot}F=0$ erzwingt dann ein globales Potential. Das ist die Aussage des Poincaré-Lemmas (nächster Artikel).
:::
