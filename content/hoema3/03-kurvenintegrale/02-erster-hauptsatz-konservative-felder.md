---
title: Der erste Hauptsatz und konservative Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030200
summary: Von Grund auf – warum das Kurvenintegral eines Gradientenfelds nur von Anfangs- und Endpunkt abhängt, $\int_\gamma \nabla h\cdot dx=h(x_1)-h(x_0)$ (der Hauptsatz für Kurvenintegrale). Die drei gleichwertigen Gesichter: wegunabhängig ⟺ Gradientenfeld ⟺ jedes geschlossene Integral null. In 2D/3D ist $\operatorname{rot}F=0$ notwendig, aber auf Gebieten mit Loch nicht hinreichend – das berühmte Wirbelfeld.
tags: erster Hauptsatz, konservatives Feld, Wegunabhängigkeit, Gradientenfeld, Potential, geschlossenes Kurvenintegral, Wirbelfeld, Gebiet
---

:::grafik
Einstiegs-Animation: Eine Höhenlandschaft $h$ (Potential) mit zwei **verschiedenen** Wegen zwischen demselben
Start- und Zielpunkt. Beide Wege werden abgelaufen; der „Arbeits"-Zähler $\int_\gamma\nabla h\cdot dx$ zeigt am
Ende **denselben** Wert — nämlich die Höhendifferenz $h(\text{Ziel})-h(\text{Start})$, unabhängig vom Weg. Dann
ein **geschlossener** Rundweg zurück zum Start: der Zähler landet bei **null**. Daneben, als Kontrast, ein
Wirbelfeld um ein kleines Loch: Hier gibt ein Rundweg $2\pi\neq0$ — dieses Feld hat kein Potential. Kernbotschaft:
Für Gradientenfelder zählt nur der Höhenunterschied; Rundwege geben null — außer das Gebiet hat ein Loch.
:::

:::konzept
Beim Wirbelfeld-Beispiel des vorigen Artikels kam entlang eines Weges ein echter Wert heraus — bei anderen
Feldern aber hängt das Kurvenintegral **nur von Anfangs- und Endpunkt** ab, nicht vom Weg dazwischen. Das sind die
__konservativen__ Felder, und sie sind genau die __Gradientenfelder__ $F=\nabla h$: Dann ist das Integral schlicht
die **Potentialdifferenz** $h(\text{Ende})-h(\text{Start})$ — der Hauptsatz der Differential- und Integralrechnung,
übertragen auf Wege. In der Physik ist das die Aussage „die Arbeit einer konservativen Kraft ist die Differenz der
potentiellen Energie" (Spannung = Potentialdifferenz). Drei Eigenschaften sind dabei **gleichwertig**:
wegunabhängig, Gradientenfeld, jedes geschlossene Integral null.
:::

**Worum es geht:** Wir definieren __Gebiet__, __Wegunabhängigkeit__ und __konservativ__, beweisen den __ersten
Hauptsatz__ ($\int\nabla h\cdot dx=h(x_1)-h(x_0)$ und die Äquivalenz konservativ ⟺ Gradientenfeld) und sehen, warum
$\operatorname{rot}F=0$ zwar notwendig, aber nicht hinreichend ist.

## Gebiet, Wegunabhängigkeit, konservativ

Ein __Gebiet__ $G\subset\mathbb{R}^n$ ist eine **offene** und **wegzusammenhängende** Menge — je zwei Punkte
lassen sich durch eine ganz in $G$ verlaufende reguläre Kurve verbinden. Auf einem Gebiet heißt das Kurvenintegral
von $F$ __wegunabhängig__, wenn

$$\int_\gamma F\cdot dx = \int_{\gamma'} F\cdot dx$$

für **alle** regulären Kurven $\gamma,\gamma'$ in $G$ mit gleichem Anfangs- und Endpunkt gilt. Ein stetiges Feld,
dessen Kurvenintegrale nur von Anfangs- und Endpunkt abhängen, heißt __konservativ__. Dazu gleichwertig ist eine
besonders handliche Bedingung (Lemma 3.10):

$$F \text{ konservativ} \quad\Longleftrightarrow\quad \oint_\gamma F\cdot dx = 0 \ \text{ für jede geschlossene Kurve } \gamma \text{ in } G.$$

(Denn: Zwei Wege mit gleichen Enden bilden zusammen — einer davon rückwärts — einen geschlossenen Weg; die
Differenz der Integrale ist das geschlossene Integral.)

## Der erste Hauptsatz für Kurvenintegrale

Jetzt der Kern. Ist $h:G\to\mathbb{R}$ stetig differenzierbar und $F=\nabla h$ ein **Gradientenfeld**, so gilt für
jede reguläre Kurve $\gamma$ von $x_0=\gamma(0)$ nach $x_1=\gamma(1)$:

$$\int_\gamma F\cdot dx = h(x_1) - h(x_0).$$

**Beweis (kurz).** Nach der Kettenregel ist $\frac{d}{dt}h(\gamma(t)) = \nabla h(\gamma(t))\cdot\dot\gamma(t) =
F(\gamma(t))\cdot\dot\gamma(t)$. Das Kurvenintegral ist also das gewöhnliche Integral dieser Ableitung, und nach
dem Hauptsatz der Differential- und Integralrechnung

$$\int_\gamma F\cdot dx = \int_0^1 \frac{d}{dt}h(\gamma(t))\,dt = h(\gamma(1)) - h(\gamma(0)). \qquad\square$$

Die rechte Seite enthält **keine Spur** mehr vom Weg — nur die Endpunkte. Also ist jedes Gradientenfeld
wegunabhängig (konservativ). Das ist die eine Richtung der zentralen Äquivalenz; sie gilt in jeder Dimension:

$$F \text{ konservativ in } G \quad\Longleftrightarrow\quad F \text{ ist ein Gradientenfeld in } G.$$

**Die Umkehrung — ein Potential bauen.** Ist $F$ konservativ, konstruiert man sein Potential direkt: Man fixiert
$x_0\in G$ und setzt $h(x):=\int_{\gamma(x)} F\cdot dy$ über irgendeinen Weg von $x_0$ nach $x$ (wegen
Wegunabhängigkeit wohldefiniert). Integriert man ein kleines Stück in Koordinatenrichtung $\hat e_k$ weiter, so
ist nach dem Mittelwertsatz der Integralrechnung $\frac{1}{s}\big(h(x+s\hat e_k)-h(x)\big) = F_k(x+t_0\hat e_k)
\to F_k(x)$ für $s\to0$. Also $\frac{\partial h}{\partial x_k}=F_k$, d. h. $\nabla h=F$ — $F$ ist Gradientenfeld.

:::grafik
Zwei Wege von $x_0$ nach $x_1$ über einer Potential-Landschaft $h$; beide Integrale ergeben $h(x_1)-h(x_0)$
(gleiche „Höhendifferenz"). Daneben die Potentialkonstruktion $h(x)=\int_{x_0}^{x}F\cdot dy$ mit einem kleinen
Schritt $s\hat e_k$, der $\partial h/\partial x_k=F_k$ liefert.
:::

**Eigenes Beispiel.** Das Feld $F(x,y)=(y,x)$ ist der Gradient von $h(x,y)=xy$ (denn $\nabla(xy)=(y,x)$). Also ist
für jeden Weg von $(0,0)$ nach $(1,1)$

$$\int_\gamma F\cdot dx = h(1,1) - h(0,0) = 1\cdot1 - 0 = 1,$$

egal ob man z. B. erst nach rechts und dann nach oben läuft oder diagonal — immer $1$. Rundwege geben $0$.

## Notwendig, aber nicht hinreichend: $\operatorname{rot}F=0$

In $n=2,3$ folgt aus „$F$ ist Gradientenfeld" sofort $\operatorname{rot}F=0$ (das ist $\operatorname{rot}
\operatorname{grad}h=0$ aus Kapitel 1). Also ist $\operatorname{rot}F=0$ eine **notwendige** Bedingung für
Konservativität. **Die Umkehrung gilt im Allgemeinen nicht** — und zwar aus einem topologischen Grund: Hat das
Gebiet ein **Loch**, kann ein Feld überall wirbelfrei sein und trotzdem kein Potential besitzen.

**Das berühmte Gegenbeispiel.** Auf $G=\mathbb{R}^2\setminus\{0\}$ (Ebene ohne Ursprung) betrachte

$$F(x,y) = \frac{1}{x^2+y^2}\begin{pmatrix} -y \\ x \end{pmatrix}.$$

Man rechnet nach: $\operatorname{rot}F = 0$ überall in $G$. Dennoch ist das Integral über den einmal gegen den
Uhrzeigersinn durchlaufenen Kreis $K_R$ (beliebiger Radius $R>0$)

$$\oint_{K_R} F\cdot dx = 2\pi \neq 0.$$

Also ist $F$ **nicht** konservativ und kein Gradientenfeld in $G$ — obwohl es wirbelfrei ist. Der „Schuldige" ist
das Loch bei $0$: Der Weg $K_R$ umschließt es, und das $2\pi$ ist gerade der Umlaufwinkel. (Lokal, in jeder
lochfreien Umgebung, **gibt** es ein Potential — nämlich den Polarwinkel $\varphi$ —, nur nicht global eindeutig.)

:::grafik
Das Wirbelfeld $F=\frac{(-y,x)}{x^2+y^2}$ auf der punktierten Ebene: kreisende Pfeile um das Loch bei $0$;
$\operatorname{rot}F=0$ an jedem Punkt, aber der Umlauf $\oint_{K_R}=2\pi$. Daneben eine lochfreie Umgebung, in der
lokal ein Potential (der Winkel $\varphi$) existiert. Beschriftung „wirbelfrei $\neq$ Gradientenfeld, wenn das
Gebiet ein Loch hat".
:::

**Stolperstein:** $\operatorname{rot}F=0$ allein garantiert **kein** Potential. Erst die Gestalt des Gebiets
entscheidet: Auf „lochfreien" (einfach zusammenhängenden) Gebieten ist $\operatorname{rot}F=0$ doch hinreichend —
das ist das Poincaré-Lemma des nächsten Artikels.

:::kern
Auf einem __Gebiet__ (offen + wegzusammenhängend) heißt $F$ __konservativ__, wenn seine Kurvenintegrale nur von
Anfangs-/Endpunkt abhängen — gleichwertig: $\oint_\gamma F\cdot dx=0$ für jede geschlossene Kurve (Lemma 3.10). Der
__erste Hauptsatz__ (Satz 3.11): für ein Gradientenfeld $F=\nabla h$ ist $\int_\gamma F\cdot dx=h(x_1)-h(x_0)$
(Beweis: $\tfrac{d}{dt}h(\gamma)=\nabla h\cdot\dot\gamma$ + Hauptsatz), also **wegunabhängig**. Zentrale Äquivalenz:
$F$ konservativ $\Leftrightarrow$ $F$ Gradientenfeld (Potential $h(x)=\int_{x_0}^x F\cdot dy$, MWT →
$\partial_{x_k}h=F_k$). In 2D/3D folgt $\operatorname{rot}F=0$ (**notwendig**). **Nicht hinreichend** auf Gebieten
mit Loch: Wirbelfeld $F=\tfrac{(-y,x)}{x^2+y^2}$ auf $\mathbb{R}^2\setminus\{0\}$ hat $\operatorname{rot}F=0$, aber
$\oint_{K_R}F\cdot dx=2\pi$. Eigenes Beispiel: $F=(y,x)=\nabla(xy)$ gibt zwischen $(0,0)$ und $(1,1)$ stets $1$.
:::

Bleibt die Frage: Wann reicht $\operatorname{rot}F=0$ **doch** für ein Potential? Die Antwort hängt an der
Topologie des Gebiets. Das __Poincaré-Lemma__ zeigt, dass die Rotations- (und analog die Divergenz-)Bedingung
**lokal** immer hinreichend ist — das Thema des nächsten Artikels.

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
