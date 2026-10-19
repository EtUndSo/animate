---
title: Das Kurvenintegral und die Orientierung
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030100
summary: Von Grund auf – wie man ein Vektorfeld entlang eines Weges integriert, $\int_\gamma F\cdot dx=\int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt$, und warum das physikalisch die verrichtete Arbeit ist. Das Integral hängt nicht von der Parametrisierung ab, wohl aber von der Orientierung (Richtungsumkehr dreht das Vorzeichen). Mit Linienelement $ds$, Bogenlänge und der Standardabschätzung.
tags: Kurvenintegral, reguläre Kurve, Orientierung, Umparametrisierung, Arbeit, Linienelement, Bogenlänge, Tangentialvektor
---

:::grafik
Einstiegs-Animation: Ein Weg $\gamma$ schlängelt sich durch ein Vektorfeld $F$ (Pfeilgitter). Ein Punkt läuft die
Kurve entlang; an jeder Stelle werden der Tangentenvektor $\dot\gamma$ (Bewegungsrichtung) und der Feldvektor
$F(\gamma)$ gezeigt, und ihr **Skalarprodukt** $F\cdot\dot\gamma$ — die Komponente des Feldes **in**
Bewegungsrichtung — füllt einen Zähler „Arbeit". Dann wird der Weg **rückwärts** durchlaufen: Derselbe Betrag
kommt heraus, aber mit umgekehrtem Vorzeichen. Kernbotschaft: Das Kurvenintegral summiert die tangentiale
Feldkomponente entlang des Weges — und die Durchlaufrichtung entscheidet über das Vorzeichen.
:::

:::konzept
Bisher haben wir über Flächen und Volumina integriert. Jetzt integrieren wir **entlang eines Weges** — das ist
das Herzstück der Vektoranalysis und der Elektrotechnik. Das __Kurvenintegral__ eines Vektorfelds misst, wie
viel „Schub" das Feld einem längs der Kurve gibt: Es addiert in jedem Punkt die Feldkomponente **in
Bewegungsrichtung**. Physikalisch ist das die **Arbeit**, die ein Kraft- oder Feldlinienfeld an einem Teilchen
verrichtet (z. B. die Spannung als Wegintegral des elektrischen Feldes). Zwei Eigenschaften sind dabei
fundamental: Das Integral hängt **nicht** von der Wahl der Parametrisierung ab, wohl aber von der
**Orientierung** — kehrt man die Durchlaufrichtung um, dreht sich das Vorzeichen.
:::

**Worum es geht:** Wir definieren die __reguläre Kurve__, das __Kurvenintegral__ $\int_\gamma F\cdot dx$ (als
Arbeit), zeigen seine __Umparametrisierungs-Invarianz__ und __Orientierungs__-Abhängigkeit und führen
__Linienelement__ $ds$, Bogenlänge und die Standardabschätzung ein.

## Reguläre Kurven

Eine __regulär parametrisierte Kurve__ im $\mathbb{R}^n$ ist eine Abbildung $\gamma:[a,b]\to\mathbb{R}^n$, die
**stückweise stetig differenzierbar** ist (stetig, und bis auf endlich viele Knickpunkte stetig differenzierbar)
und deren Geschwindigkeit nie verschwindet:

$$\dot\gamma(t) := \frac{d}{dt}\gamma(t) \neq 0.$$

Die Bedingung $\dot\gamma\ne0$ sorgt dafür, dass die Kurve an jeder Stelle eine wohldefinierte **Tangente** hat
(kein Stillstand, keine „Spitze" im Inneren eines glatten Stücks). Zwei Sprechweisen:

- __geschlossen__: Anfang und Ende fallen zusammen, $\gamma(a)=\gamma(b)$.
- __doppelpunktfrei__ (einfach): Die Kurve schneidet sich nicht selbst (außer evtl. Anfang = Ende).

Die __Spur__ $\Gamma=\gamma([a,b])$ ist die Punktmenge, die die Kurve durchläuft; eine __reguläre Kurve__ $\Gamma$
ist eine solche Spur zusammen mit einer regulären, doppelpunktfreien Parametrisierung.

## Das Kurvenintegral eines Vektorfelds

Sei $F$ ein stetiges Vektorfeld in einer offenen Menge $U\subset\mathbb{R}^n$, in der die Kurve verläuft. Das
__Kurvenintegral__ von $F$ längs $\gamma$ ist

$$\int_\gamma F\cdot dx := \int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt.$$

Formal schreibt man $dx = \dot\gamma(t)\,dt$ für das (vektorielle) Wegelement; bei stückweise glatten Kurven
summiert man über die glatten Teilstücke. Der Integrand $F(\gamma(t))\cdot\dot\gamma(t)$ ist das Skalarprodukt aus
Feld und Geschwindigkeit — also genau die **tangentiale Komponente** des Feldes, gewichtet mit der
Durchlaufgeschwindigkeit. Physikalisch ist das die __Arbeit__, die verrichtet wird, wenn ein Teilchen im Kraftfeld
$F$ von $\gamma(a)$ nach $\gamma(b)$ bewegt wird. Das Kurvenintegral ist offensichtlich **linear** in $F$.

:::grafik
Ein Kurvenstück mit Geschwindigkeitsvektor $\dot\gamma$ und Feldvektor $F(\gamma)$ an einem Punkt; eingezeichnet
die Projektion von $F$ auf $\dot\gamma$ (das Skalarprodukt $F\cdot\dot\gamma$). Darunter das aufintegrierte
„Arbeits"-Band entlang der ganzen Kurve. Formel $\int_\gamma F\cdot dx=\int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt$.
:::

**Eigene Beispiele.** Auf der oberen Halbkreislinie $\gamma(t)=(\cos t,\sin t)$, $t\in[0,\pi]$ (also
$\dot\gamma=(-\sin t,\cos t)$):

- **Radiales Feld** $F(x,y)=(x,y)$: $F(\gamma)\cdot\dot\gamma = \cos t\,(-\sin t)+\sin t\,\cos t = 0$, also
  $\int_\gamma F\cdot dx = 0$. Ein radiales Feld steht senkrecht auf der Kreisbewegung — es verrichtet keine
  Arbeit.
- **Wirbelfeld** $F(x,y)=(-y,x)$: $F(\gamma)\cdot\dot\gamma = (-\sin t)(-\sin t)+\cos t\,\cos t = 1$, also
  $\int_\gamma F\cdot dx = \int_0^\pi 1\,dt = \pi$. Das umlaufende Feld zeigt stets in Bewegungsrichtung und
  verrichtet maximale Arbeit.

## Umparametrisierung und Orientierung

Das Kurvenintegral beschreibt eine **geometrische** Größe (Arbeit entlang des Weges) — es sollte also nicht davon
abhängen, wie schnell man die Kurve durchläuft. Tatsächlich ist es **invariant unter Umparametrisierung**, solange
der **Durchlaufsinn** erhalten bleibt: Ist $\tau:[\alpha,\beta]\to[a,b]$ streng monoton wachsend und stetig
differenzierbar, so liefert $\gamma\circ\tau$ dasselbe Integral (die Substitutionsregel sorgt dafür, dass sich der
Faktor $\tau'$ gerade heraushebt).

Die **Durchlaufrichtung** zählt aber sehr wohl. Für die **entgegengesetzt** durchlaufene Kurve $-\gamma$ (etwa
$t\mapsto\gamma(b+a-t)$) gilt

$$\int_{-\gamma} F\cdot dx = -\int_\gamma F\cdot dx.$$

Deshalb ordnet man einer regulären Kurve stets eine __Orientierung__ (einen Durchlaufsinn) zu; die
Gegenorientierung schreibt man $-\gamma$. Bei **geschlossenen** Kurven ist das Integral sogar vom gewählten
Anfangspunkt unabhängig. Zudem ist das Kurvenintegral **additiv**: Setzt man zwei Kurven aneinander, addieren sich
die Integrale, $\int_{\gamma_1\pm\gamma_2}F\cdot dx = \int_{\gamma_1}F\cdot dx \pm \int_{\gamma_2}F\cdot dx$.

:::grafik
Dieselbe Spur, zweimal durchlaufen: einmal vorwärts ($\gamma$, Integralwert $+W$), einmal rückwärts ($-\gamma$,
Wert $-W$). Daneben zwei verschieden schnelle Parametrisierungen desselben Vorwärtswegs mit identischem Wert
(Umparametrisierungs-Invarianz).
:::

## Linienelement, Bogenlänge und skalares Kurvenintegral

Zerlegt man das Wegelement in Länge und Richtung, entstehen zwei nützliche Größen. Das __Linienelement__ ist die
infinitesimale Bogenlänge

$$ds = |\dot\gamma(t)|\,dt,$$

und der __orientierte Einheitstangentialvektor__ ist $\tau = \dfrac{\dot\gamma(t)}{|\dot\gamma(t)|}$ (Richtung der
Bewegung, Länge 1). Damit zerfällt das vektorielle Wegelement in $dx = \tau\,ds$, und das Kurvenintegral schreibt
sich als Integral der tangentialen Feldkomponente über die Bogenlänge:

$$\int_\gamma F\cdot dx = \int_\gamma F\cdot\tau\,ds.$$

Die __Bogenlänge__ (Kurvenlänge) ist der Spezialfall $F\cdot\tau\equiv1$, also

$$L(\gamma) = \int_a^b |\dot\gamma(t)|\,dt = \int_\gamma ds.$$

Allgemeiner integriert man ein **Skalarfeld** $f$ längs der Kurve als $\int_\gamma f\,ds=\int_a^b
f(\gamma(t))\,|\dot\gamma(t)|\,dt$ (z. B. die Masse eines Drahtes mit Dichte $f$). **Stolperstein:** Das
**skalare** Kurvenintegral $\int_\gamma f\,ds$ ist orientierungs**unabhängig** (die Länge $ds>0$ zählt immer
positiv), das **vektorielle** $\int_\gamma F\cdot dx$ dagegen orientierungs**abhängig** (Vorzeichen). Schließlich
gilt die __Standardabschätzung__

$$\left|\int_\gamma F\cdot dx\right| \le \sup_{x\in\gamma}|F(x)|\cdot L(\gamma).$$

:::grafik
Ein Kurvenstück mit Linienelement $ds=|\dot\gamma|\,dt$ und Einheitstangente $\tau$; Zerlegung $dx=\tau\,ds$.
Daneben ein Draht mit örtlicher Dichte $f$, dessen Masse $\int_\gamma f\,ds$ ist (orientierungsunabhängig), im
Kontrast zum vorzeichenbehafteten $\int_\gamma F\cdot dx$.
:::

:::kern
Eine __regulär parametrisierte Kurve__ $\gamma:[a,b]\to\mathbb{R}^n$ ist stückweise $C^1$ mit $\dot\gamma\ne0$
(geschlossen falls $\gamma(a)=\gamma(b)$, einfach falls doppelpunktfrei). Das __Kurvenintegral__ eines stetigen
Vektorfelds ist $\int_\gamma F\cdot dx=\int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt$ ($dx=\dot\gamma\,dt$),
physikalisch die __Arbeit__ (tangentiale Feldkomponente aufsummiert); linear und **additiv**. Es ist
**invariant** unter orientierungserhaltender Umparametrisierung, aber die __Orientierung__ zählt:
$\int_{-\gamma}F\cdot dx=-\int_\gamma F\cdot dx$. __Linienelement__ $ds=|\dot\gamma|\,dt$, Einheitstangente
$\tau=\dot\gamma/|\dot\gamma|$, $dx=\tau\,ds$, __Bogenlänge__ $L(\gamma)=\int_\gamma ds$,
$\int_\gamma F\cdot dx=\int_\gamma F\cdot\tau\,ds$; skalares $\int_\gamma f\,ds$ (orientierungsUNabhängig).
__Standardabschätzung__ $|\int_\gamma F\cdot dx|\le\sup_\gamma|F|\cdot L(\gamma)$. Beispiel Halbkreis: radiales
Feld $(x,y)$ gibt $0$, Wirbelfeld $(-y,x)$ gibt $\pi$.
:::

Beim Wirbelfeld-Beispiel kam entlang des halben Kreises etwas Nichttriviales heraus — bei manchen Feldern hängt
das Integral aber **nur von Anfangs- und Endpunkt** ab, nicht vom Weg. Genau das sind die Gradientenfelder, und
der Zusammenhang „wegunabhängig ⟺ Gradientenfeld ⟺ geschlossenes Integral null" ist der __erste Hauptsatz für
Kurvenintegrale__ — das Thema des nächsten Artikels.
