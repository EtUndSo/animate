---
title: Das Kurvenintegral und die Orientierung
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030100
summary: Von Grund auf – was eine Kurve überhaupt ist, wie man ein Vektorfeld entlang eines Weges aufsummiert, $\int_\gamma F\cdot dx=\int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt$, und warum das die verrichtete Arbeit ist. Mit Umparametrisierung, Orientierung, Linienelement und Bogenlänge.
tags: Kurvenintegral, reguläre Kurve, Orientierung, Umparametrisierung, Arbeit, Linienelement, Bogenlänge, Tangentialvektor
---

## Anschaulich

Stell dir vor, du schiebst einen Wagen auf einem gewundenen Weg durch ein **Kraftfeld** — etwa gegen einen
ortsabhängigen Wind. An jeder Stelle hilft oder bremst dich das Feld, aber immer nur mit dem Anteil, der **in
deine Bewegungsrichtung** zeigt; was quer dazu drückt, kostet keine Arbeit. Das __Kurvenintegral__ summiert genau
diesen „mitschiebenden" Anteil über den ganzen Weg auf — es misst die **Arbeit**, die das Feld an dir verrichtet.

Zwei Dinge fallen sofort auf:

1. *Wie schnell* du gehst, ist egal. Die Arbeit hängt am Weg und am Feld, nicht am Tempo — das Kurvenintegral ist
   eine **geometrische** Größe.
2. Gehst du den Weg **rückwärts**, hilft dir jetzt beim Bremsen, was vorher beim Schieben half. Die Arbeit kehrt
   ihr Vorzeichen um — die **Durchlaufrichtung** zählt.

:::grafik
Ein Weg schlängelt sich durch ein Pfeilgitter (Vektorfeld $F$). Ein Punkt läuft die Kurve entlang; an einer
Stelle sind der Bewegungspfeil (Tangente) und der Feldpfeil $F$ gezeigt, dazu ihre Projektion aufeinander — der
„mitschiebende" Anteil $F\cdot\dot\gamma$ — füllt einen Zähler „Arbeit". Rechts derselbe Weg rückwärts: gleicher
Betrag, umgekehrtes Vorzeichen.
:::

## Was ist eine Kurve?

Bevor wir „entlang eines Weges" integrieren, müssen wir sagen, **was ein Weg überhaupt ist** — das Skript setzt
das stillschweigend voraus, aber genau hier entscheidet sich das Verständnis.

**Anschaulich** ist eine Kurve ein *Punkt, dessen Position sich mit einem Parameter $t$ ändert* — wie der
Standort eines Wanderers zur „Zeit" $t$. Formal ist eine __parametrisierte Kurve__ im $\mathbb{R}^n$ eine Abbildung

:::formel Definition
$$\gamma:[a,b]\to\mathbb{R}^n,\qquad t\mapsto\gamma(t)=\big(\gamma_1(t),\ldots,\gamma_n(t)\big).$$
:::

**So liest man diese Zeile:** Die Abbildung bekommt als **Eingabe** eine einzelne reelle Zahl $t\in[a,b]$ — einen
**Skalar**, den „Zeitpunkt" auf dem Weg — und gibt als **Ausgabe** einen **Vektor** $\gamma(t)\in\mathbb{R}^n$
zurück. Im Anschauungsraum ($n=3$) sind das die drei Ortskoordinaten $(\gamma_1,\gamma_2,\gamma_3)$ des Punktes.

Die beiden Pfeile bedeuten Verschiedenes: $\to$ nennt die beiden **Räume** (von $[a,b]$ nach $\mathbb{R}^n$),
$\mapsto$ die konkrete **Zuordnung** (dieses eine $t$ auf diesen einen Punkt).

Eine Kurve ist also kein fertiges Bild im Raum, sondern eine **Vorschrift**, die Zahlen auf Punkte abbildet. Jeder
Wert $t\in[a,b]$ liefert **genau einen Punkt**; läuft $t$ von $a$ nach $b$, zeichnet dieser Punkt den Weg nach. Die
durchlaufene Punktmenge $\Gamma=\gamma([a,b])$ heißt __Spur__ der Kurve.

Weil $\gamma(t)$ für jedes $t$ ein Ortsvektor ist, darf man ihn nach $t$ ableiten. Der __Geschwindigkeits-__ oder
__Tangentialvektor__

$$\dot\gamma(t):=\frac{d}{dt}\gamma(t)=\big(\dot\gamma_1(t),\ldots,\dot\gamma_n(t)\big)$$

zeigt in die **Bewegungsrichtung** und hat als Länge das momentane **Tempo**.

Auch hier ist die Eingabe wieder der **Skalar** $t$ und die Ausgabe ein **Vektor**: Man leitet jede Koordinate
einzeln nach $t$ ab und stellt die Ergebnisse als Vektor zusammen. Erst jetzt, wo die Kurve als Objekt existiert,
ist dieser Ausdruck überhaupt sinnvoll.

Eine Kurve heißt __regulär parametrisiert__, wenn sie **stückweise stetig differenzierbar** ist (stetig, und bis
auf endlich viele Knickpunkte stetig differenzierbar) und ihre Geschwindigkeit **nie verschwindet**,
$\dot\gamma(t)\ne 0$. Diese Bedingung ist kein technisches Beiwerk: Bei $\dot\gamma=0$ käme der Wanderer zum
Stillstand und hätte dort keine wohldefinierte Richtung — die Kurve könnte eine „Spitze" bekommen. Zwei weitere
Sprechweisen:

- __geschlossen__: Anfang und Ende fallen zusammen, $\gamma(a)=\gamma(b)$ (ein Rundweg).
- __doppelpunktfrei__ (einfach): Die Kurve schneidet sich nicht selbst (außer evtl. Anfang = Ende).

Eine __reguläre Kurve__ $\Gamma$ ist eine Spur zusammen mit einer regulären, doppelpunktfreien Parametrisierung.

:::grafik
Szene: hoema3/kurvenintegrale/01-kurve-parameter · Vorlage: parametrische-kurve-2d
**Animation.** Links die Parameterachse $[a,b]$ mit einem gleitenden Marker $t$; rechts der $\mathbb{R}^2$. Während
$t$ läuft, wandert der Punkt $\gamma(t)$ die Spur $\Gamma$ entlang (rot = das definierte Objekt), und an ihm hängt
der Tangentialvektor $\dot\gamma(t)$ (orange = der Mechanismus), der stets in Bewegungsrichtung zeigt und bei
hohem Tempo länger wird. Kernbotschaft: ein **Skalar** $t$ erzeugt einen **Punkt**; die Ableitung ist die
Geschwindigkeit. Achsen in Grau.
:::

## Das Kurvenintegral: die zwei Akteure

**Die zwei Akteure.** Jetzt wirken zwei Objekte zusammen:

- __Die Kurve__ $\gamma:[a,b]\to\mathbb{R}^n$ (eben definiert) — der Weg durch den Raum mit Tangente $\dot\gamma$.
- __Das Vektorfeld__ $F:U\to\mathbb{R}^n$ auf einer offenen Menge $U\subset\mathbb{R}^n$, in der die Kurve
  verläuft — an **jedem** Punkt ein Pfeil (denk an ein Wind- oder Kraftfeld). $F$ sei stetig.

**Das Zusammenspiel.** Setzt man die Kurve ins Feld ein, erhält man das Feld **entlang** des Weges,
$F(\gamma(t))$ — welchen Pfeil der Wanderer an jeder Stelle vorfindet. Die zentrale Frage: *Wie viel Arbeit
verrichtet das Feld, während wir die Kurve durchlaufen?*

Die **Idee** ist einfach: den Weg in winzige Schritte zerlegen, für jeden Schritt die geleistete Arbeit bestimmen
und alles aufsummieren. Heraus kommt das __Kurvenintegral__ von $F$ längs $\gamma$:

:::formel Definition
$$\int_\gamma F\cdot dx := \int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt.$$
:::

:::herleitung
Ein Schritt von $t$ nach $t+dt$ verschiebt uns um den kleinen Vektor $d\vec x=\dot\gamma(t)\,dt$ (Geschwindigkeit
mal Zeitschritt).

Die Arbeit dieses Schritts ist „Kraft mal Weg" — aber nur der **tangentiale** Anteil zählt, also das Skalarprodukt

$$dW = F(\gamma(t))\cdot d\vec x = F(\gamma(t))\cdot\dot\gamma(t)\,dt.$$

Alle diese Beiträge über den ganzen Weg **aufsummieren** heißt integrieren, von $t=a$ bis $t=b$:

$$\int_\gamma F\cdot dx=\int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt.$$
:::

**Stück für Stück gelesen:**

- $F(\gamma(t))$: das **Feld am Kurvenpunkt** zur Stelle $t$ — ein Vektor (welchen Pfeil der Wanderer dort vorfindet).
- $\dot\gamma(t)$: die **Geschwindigkeit** dort — ebenfalls ein Vektor.
- Der Malpunkt $\cdot$ ist das **Skalarprodukt**: aus zwei Vektoren wird eine **Zahl** — gerade die mitschiebende (tangentiale) Komponente.
- $\int_a^b(\ldots)\,dt$: summiert diese Zahlen über **alle** $t$ von $a$ bis $b$; das Ergebnis ist eine einzige Zahl — die Gesamt-Arbeit.

Der Integrand ist also die **tangentiale Feldkomponente**, gewichtet mit dem Tempo.

Formal schreibt man $dx=\dot\gamma(t)\,dt$ für das vektorielle Wegelement; bei stückweise glatten Kurven summiert
man über die glatten Teilstücke. Das Integral ist **linear** in $F$.

**Eigene Beispiele.** Wir nehmen die obere Halbkreislinie

$$\gamma(t)=(\cos t,\ \sin t),\quad t\in[0,\pi],\qquad\text{somit}\quad \dot\gamma(t)=(-\sin t,\ \cos t).$$

**Radiales Feld** $F(x,y)=(x,y)$. Der Integrand wird

$$F(\gamma)\cdot\dot\gamma=\cos t\,(-\sin t)+\sin t\,\cos t=0,\qquad\text{also}\quad \int_\gamma F\cdot dx=0.$$

Ein radiales Feld steht senkrecht auf der Kreisbewegung — es schiebt nie mit und verrichtet keine Arbeit.

**Wirbelfeld** $F(x,y)=(-y,x)$. Hier ist

$$F(\gamma)\cdot\dot\gamma=(-\sin t)(-\sin t)+\cos t\,\cos t=1,\qquad\text{also}\quad \int_\gamma F\cdot dx=\int_0^\pi 1\,dt=\pi.$$

Das umlaufende Feld zeigt stets in Bewegungsrichtung und schiebt auf dem ganzen Weg mit.

:::grafik
Ein Kurvenstück mit Geschwindigkeitsvektor $\dot\gamma$ und Feldvektor $F(\gamma)$ an einem Punkt; eingezeichnet
die Projektion von $F$ auf $\dot\gamma$ (das Skalarprodukt). Darunter das aufintegrierte „Arbeits"-Band über die
ganze Kurve, daneben die zwei Beispiele (radial → $0$, Wirbel → $\pi$).
:::

## Warum die Parametrisierung egal ist — die Orientierung aber nicht

Beide anschaulichen Beobachtungen vom Anfang folgen jetzt direkt aus der Formel.

**Das Tempo ist egal (Umparametrisierungs-Invarianz).** Durchläuft man denselben Weg schneller oder langsamer,
ändert sich der Wert nicht. Ist $\tau:[\alpha,\beta]\to[a,b]$ streng monoton wachsend und stetig differenzierbar,
so liefert $\gamma\circ\tau$ dasselbe Integral — in der Substitutionsregel hebt sich der Zeitdehnungsfaktor
$\tau'$ gerade heraus. Das muss so sein, weil das Integral eine **geometrische** Größe beschreibt (Arbeit entlang
des Weges), keine Frage der Geschwindigkeit.

**Die Richtung zählt (Orientierung).** Für die **entgegengesetzt** durchlaufene Kurve $-\gamma$ (etwa
$t\mapsto\gamma(b+a-t)$) zeigt der Geschwindigkeitsvektor überall genau umgekehrt, also wechselt
$F\cdot\dot\gamma$ an jedem Punkt das Vorzeichen:

$$\int_{-\gamma} F\cdot dx = -\int_\gamma F\cdot dx.$$

Deshalb gibt man einer regulären Kurve stets eine __Orientierung__ (einen Durchlaufsinn) mit; die
Gegenorientierung heißt $-\gamma$. Bei **geschlossenen** Kurven ist das Integral sogar vom gewählten Startpunkt
unabhängig. Und das Kurvenintegral ist **additiv**: Setzt man Wege aneinander, addieren sich die Integrale,
$\int_{\gamma_1\pm\gamma_2}F\cdot dx=\int_{\gamma_1}F\cdot dx\pm\int_{\gamma_2}F\cdot dx$ — man darf einen
komplizierten Weg in einfache Stücke zerlegen.

:::grafik
Dieselbe Spur, zweimal durchlaufen: vorwärts ($\gamma$, Wert $+W$) und rückwärts ($-\gamma$, Wert $-W$). Daneben
zwei verschieden schnelle Parametrisierungen desselben Vorwärtswegs mit identischem Wert.
:::

## Linienelement, Bogenlänge und das skalare Kurvenintegral

Zerlegt man das Wegelement $dx$ in **Länge** und **Richtung**, entstehen zwei nützliche Größen. Das
__Linienelement__ ist die infinitesimale Bogenlänge

$$ds=|\dot\gamma(t)|\,dt,$$

und der __orientierte Einheitstangentialvektor__ ist $\tau=\dfrac{\dot\gamma(t)}{|\dot\gamma(t)|}$ (reine Richtung,
Länge $1$). Damit zerfällt das Wegelement in $dx=\tau\,ds$, und das Kurvenintegral wird zum Integral der
tangentialen Feldkomponente über die Bogenlänge:

$$\int_\gamma F\cdot dx=\int_\gamma F\cdot\tau\,ds.$$

Die __Bogenlänge__ (Kurvenlänge) ist der Spezialfall $F\cdot\tau\equiv 1$:

$$L(\gamma)=\int_a^b|\dot\gamma(t)|\,dt=\int_\gamma ds.$$

Allgemeiner integriert man ein **Skalarfeld** $f$ längs der Kurve als $\int_\gamma f\,ds=\int_a^b
f(\gamma(t))\,|\dot\gamma(t)|\,dt$ (z. B. die Masse eines Drahtes mit Dichte $f$). **Stolperstein:** Das
**skalare** Kurvenintegral $\int_\gamma f\,ds$ ist orientierungs**unabhängig** — es steckt nur die positive Länge
$ds>0$ darin (die Masse eines Drahtes ändert sich nicht mit der Laufrichtung). Das **vektorielle**
$\int_\gamma F\cdot dx$ dagegen enthält die Richtung $\dot\gamma$ und ist damit orientierungs**abhängig**.

Schließlich die __Standardabschätzung__: Weil $|\tau|=1$, gilt nach Cauchy-Schwarz $|F\cdot\tau|\le|F|$;
integriert man diese Schranke über $ds$, folgt

$$\left|\int_\gamma F\cdot dx\right|\le\sup_{x\in\gamma}|F(x)|\cdot L(\gamma).$$

:::grafik
Ein Kurvenstück mit Linienelement $ds=|\dot\gamma|\,dt$ und Einheitstangente $\tau$; Zerlegung $dx=\tau\,ds$.
Daneben ein Draht mit örtlicher Dichte $f$, dessen Masse $\int_\gamma f\,ds$ ist (orientierungsunabhängig), im
Kontrast zum vorzeichenbehafteten $\int_\gamma F\cdot dx$.
:::

## Physikalische Bedeutung und Ausblick

In der Elektrotechnik ist das Kurvenintegral allgegenwärtig: Die **Spannung** zwischen zwei Punkten ist das
Wegintegral des elektrischen Feldes, $U=\int_\gamma \vec E\cdot d\vec r$ — die Arbeit pro Ladung entlang des
Weges. Dass diese Arbeit bei manchen Feldern **nur** von Anfang und Ende abhängt (und bei anderen nicht), ist
daher eine physikalisch zentrale Frage.

Genau dorthin geht es weiter. Beim Wirbelfeld kam entlang des Halbkreises etwas Nichttriviales heraus — bei
manchen Feldern hängt das Integral aber **nur von Anfangs- und Endpunkt** ab, nicht vom Weg. Das sind die
__Gradientenfelder__, und der Zusammenhang „wegunabhängig $\Leftrightarrow$ Gradientenfeld $\Leftrightarrow$
geschlossenes Integral null" ist der __erste Hauptsatz für Kurvenintegrale__ — das Thema des nächsten Artikels.

:::kern
- Eine __Kurve__ $\gamma:[a,b]\to\mathbb{R}^n$ ist ein Punkt, dessen Ort der Parameter $t$ abfährt; ihre Ableitung $\dot\gamma$ ist der __Tangentialvektor__ (Richtung + Tempo). **Regulär:** stückweise $C^1$ mit $\dot\gamma\ne0$.
- __Kurvenintegral__ eines stetigen Vektorfelds: $\int_\gamma F\cdot dx=\int_a^b F(\gamma(t))\cdot\dot\gamma(t)\,dt$ (mit $dx=\dot\gamma\,dt$) — physikalisch die __Arbeit__, die tangentiale Feldkomponente aufsummiert; **linear** und **additiv**.
- **Tempo egal** (invariant unter orientierungserhaltender Umparametrisierung), aber die __Orientierung__ zählt: $\int_{-\gamma}F\cdot dx=-\int_\gamma F\cdot dx$.
- __Linienelement__ $ds=|\dot\gamma|\,dt$, Einheitstangente $\tau=\dot\gamma/|\dot\gamma|$, Zerlegung $dx=\tau\,ds$, __Bogenlänge__ $L=\int_\gamma ds$.
- Das **skalare** $\int_\gamma f\,ds$ ist orientierungs**unabhängig**, das **vektorielle** $\int_\gamma F\cdot dx$ dagegen nicht.
- __Standardabschätzung__: $\left|\int_\gamma F\cdot dx\right|\le\sup_\gamma|F|\cdot L(\gamma)$ (aus Cauchy-Schwarz, $|\tau|=1$).
:::

:::quiz
F: Was misst das Kurvenintegral $\int_\gamma F\cdot dx$ physikalisch, und warum steht im Integranden ein Skalarprodukt?
A: Es misst die **Arbeit**, die das Feld an einem längs $\gamma$ bewegten Teilchen verrichtet. Das Skalarprodukt $F(\gamma)\cdot\dot\gamma$ pickt genau die Feldkomponente **in Bewegungsrichtung** heraus — nur der tangentiale Anteil leistet Arbeit, der senkrechte nicht.
F: Was ist eine Kurve, und warum darf man $\dot\gamma(t)$ erst danach hinschreiben?
A: Eine Kurve ist eine Abbildung $\gamma:[a,b]\to\mathbb{R}^n$ — ein Punkt, dessen Ort der Parameter $t$ abfährt. Erst wenn dieses Objekt existiert, ist seine Ableitung $\dot\gamma(t)$ (der Tangentialvektor) überhaupt definiert; vorher gäbe es nichts abzuleiten.
F: Warum verrichtet ein radiales Feld $F=(x,y)$ entlang einer Kreislinie keine Arbeit?
A: Auf dem Kreis steht das radiale Feld senkrecht zur Bewegungsrichtung (Tangente). Damit ist $F\cdot\dot\gamma=0$ an jedem Punkt, und das Integral verschwindet — es gibt keine tangentiale Komponente, die „schiebt".
F: Warum liefert das Wirbelfeld $F=(-y,x)$ auf dem Kreis den maximalen (nichttrivialen) Wert?
A: Dieses Feld zeigt überall **tangential**, also genau in Bewegungsrichtung: $F\cdot\dot\gamma=1$ konstant. Das Feld „schiebt" entlang des ganzen Wegs mit, daher summiert sich die Arbeit auf (auf dem Halbkreis zu $\pi$).
F: Warum ist das Kurvenintegral invariant unter einer orientierungserhaltenden Umparametrisierung?
A: Es beschreibt eine geometrische Größe (Arbeit entlang des Weges), nicht die Durchlaufgeschwindigkeit. Formal sorgt die Substitutionsregel dafür, dass sich der Zeitdehnungsfaktor $\tau'$ gerade heraushebt — schneller oder langsamer durchlaufen ändert den Wert nicht.
F: Warum dreht die Umkehr der Durchlaufrichtung das Vorzeichen des Integrals?
A: Bei $-\gamma$ zeigt der Geschwindigkeitsvektor $\dot\gamma$ genau entgegengesetzt, also wechselt $F\cdot\dot\gamma$ überall das Vorzeichen. Daher $\int_{-\gamma}F\cdot dx=-\int_\gamma F\cdot dx$ — Arbeit „zurück" ist das Negative der Arbeit „hin".
F: Wozu dient die Bedingung $\dot\gamma\neq0$ einer regulären Kurve?
A: Sie garantiert an jeder Stelle eine wohldefinierte **Tangente** (Richtung der Bewegung). Bei $\dot\gamma=0$ käme die Kurve zum Stillstand oder bekäme eine Spitze — dann wäre die Richtung und damit $F\cdot\dot\gamma$ nicht sinnvoll definiert.
F: Warum ist das **skalare** Kurvenintegral $\int_\gamma f\,ds$ orientierungsunabhängig, das **vektorielle** $\int_\gamma F\cdot dx$ aber nicht?
A: Im skalaren Fall steckt nur das Längenelement $ds=|\dot\gamma|\,dt>0$ drin, das immer positiv ist (eine Drahtmasse ändert sich nicht mit der Laufrichtung). Im vektoriellen Fall steckt die **Richtung** $\dot\gamma$ (bzw. $\tau$) drin, die sich bei Umkehr umdreht — daher der Vorzeichenwechsel.
F: Wie zerlegt man das Wegelement $dx$, und wie ergibt sich daraus die Bogenlänge?
A: $dx=\tau\,ds$ mit der Einheitstangente $\tau=\dot\gamma/|\dot\gamma|$ und dem Linienelement $ds=|\dot\gamma|\,dt$. Mit $F\cdot\tau\equiv1$ (also $F=\tau$) wird das Kurvenintegral zu $\int_\gamma ds=\int_a^b|\dot\gamma|\,dt$ — der Bogenlänge.
F: Woher kommt die Standardabschätzung $|\int_\gamma F\cdot dx|\le\sup_\gamma|F|\cdot L(\gamma)$?
A: Es ist $|F\cdot\tau|\le|F|$ (weil $|\tau|=1$, Cauchy-Schwarz). Integriert man diese Schranke über $ds$, erhält man $\sup_\gamma|F|$ mal die Gesamtlänge $L(\gamma)=\int ds$.
:::
