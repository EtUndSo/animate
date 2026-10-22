---
title: Das Kurvenintegral und die Orientierung
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030100
summary: Von Grund auf – wie man ein Vektorfeld entlang eines Weges aufsummiert, $\int_\gamma\vec F\cdot d\vec x=\int_a^b\vec F(\vec\gamma(t))\cdot\dot{\vec\gamma}(t)\,dt$. Leitbild ist eine Radtour im Wind – Rückenwind hilft, Gegenwind bremst, Seitenwind kostet nichts. Mit regulären Kurven, Sehnenpolygon, Umparametrisierung (Tempo egal), Orientierung (Richtung zählt), Linienelement, Bogenlänge, zusammengesetzten Wegen, Standardabschätzung und einer Beispiel-Seite.
tags: Kurvenintegral, reguläre Kurve, Orientierung, Umparametrisierung, Arbeit, Linienelement, Bogenlänge, Tangentialvektor
---

## Anschaulich

Eine **Radtour im Wind**. Kommt der Wind von hinten, schiebt er mit; kommt er von vorn, bremst er; kommt er von der Seite,
kostet er nichts. Was zählt, ist an jeder Stelle nur der Anteil des Winds **in Fahrtrichtung**.

**Das Leitbild dieses Artikels:** Der Wind ist ein Vektorfeld $\vec F$ — an jedem Ort ein Pfeil, die Kraft, die er dort
ausübt. Die Tour ist eine Kurve $\vec\gamma$. Zerlegt man die Strecke in kleine Wegstücke, leistet der Wind auf jedem
Stück die Arbeit „Windanteil in Fahrtrichtung mal Wegstück". Die Summe über die ganze Tour ist das __Kurvenintegral__ — die
**Arbeit**, die der Wind an der Radfahrerin verrichtet.

Zwei Dinge fallen sofort auf:

1. Das **Tempo** ist egal. Ob man schnell oder gemütlich fährt, ändert nichts daran, wo man welchen Wind von hinten hatte.
2. Die **Richtung** zählt. Fährt man dieselbe Strecke zurück, wird aus jedem Rückenwind ein Gegenwind — die Arbeit
   wechselt das Vorzeichen.

In der Physik ist das genau die Arbeit eines Kraftfelds, in der Elektrotechnik die **Spannung**: das Kurvenintegral des
elektrischen Felds, die Arbeit pro Ladung längs eines Weges.

:::grafik
Szene: hoema3/kurvenintegrale/01-radtour-im-wind · Vorlage: feld-und-kurve-2d
Ein Pfeilgitter (Windfeld $\vec F$) und ein gewundener Weg. Eine Radfahrerin fährt die Kurve $\vec\gamma$ ab; an ihrem Ort
sind der Windpfeil, die Fahrtrichtung und der Anteil des Winds in Fahrtrichtung eingezeichnet (grün bei Rückenwind, rot
bei Gegenwind). Ein Zähler „Arbeit" summiert mit. Ein Umschalter lässt sie dieselbe Strecke zurückfahren: Der Zähler
endet beim negativen Wert. Ein Regler ändert das Tempo — der Endwert bleibt gleich. Kernaussage: Das Kurvenintegral
summiert den Windanteil in Fahrtrichtung über den Weg. (Blau = Feld, rot = Kurve, orange = Anteil in Fahrtrichtung, grau =
Achsen.)
:::

## Was ist eine reguläre Kurve?

Im Artikel über [Skalar- und Vektorfelder](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/skalar-und-vektorfelder-differenzierbarkeit.html)
war eine Kurve eine Abbildung auf einem offenen Intervall. Für eine Tour braucht man Anfang und Ende,
also ein abgeschlossenes Intervall $[a,b]$, und man möchte Ecken zulassen — eine Tour um einen Häuserblock biegt ab.

**Stückweise stetig differenzierbar** heißt: $\vec\gamma:[a,b]\to\mathbb{R}^n$ ist stetig, und es gibt endlich viele
Stellen

$$a = a_0 < a_1 < \ldots < a_N = b,$$

sodass $\vec\gamma$ auf jedem Teilintervall $[a_{k-1},a_k]$ stetig differenzierbar ist. An den __Knickstellen__ $a_k$ und
an den Endpunkten existieren nur die einseitigen Ableitungen — dort darf die Kurve eine Ecke haben.

:::formel Definition
$$\vec\gamma:[a,b]\to\mathbb{R}^n \ \text{ stückweise stetig differenzierbar}, \qquad \dot{\vec\gamma}(t)\neq\vec 0.$$
:::

**So liest man das:** Eine solche Kurve heißt __regulär parametrisiert__, wenn ihre Geschwindigkeit $\dot{\vec\gamma}(t)$
nirgends der Nullvektor ist — an Knick- und Endpunkten gilt das für die einseitigen Ableitungen. Eingabe ist eine Zahl
$t\in[a,b]$, die Zeit; Ausgabe ein Ort $\vec\gamma(t)\in\mathbb{R}^n$.

**Im Bild:** Die Radfahrerin hält nie an. Deshalb hat sie in jedem Moment eine Fahrtrichtung, und genau die braucht man, um
„Wind in Fahrtrichtung" zu messen. An einer Ecke biegt sie ab; dort gibt es eine Richtung davor und eine danach.

Zwei weitere Begriffe beschreiben die Form der Tour:

- __geschlossen__: Ende gleich Anfang, $\vec\gamma(b)=\vec\gamma(a)$ — eine Rundtour;
- __doppelpunktfrei__ (einfach): Kein Ort wird zweimal besucht, höchstens kehrt die Tour am Ende zum Anfang zurück. Aus
  $\vec\gamma(s)=\vec\gamma(t)$ mit $s<t$ folgt also, dass $s$ die Anfangszeit $a$ und $t$ die Endzeit $b$ ist.

::::beispiel Kurven: regulär, geschlossen, doppelpunktfrei?
**(a) Die Strecke** von einem Punkt $\vec p$ zu einem anderen Punkt $\vec q$:

$$\vec\gamma(t) = \vec p+t\,(\vec q-\vec p), \qquad \dot{\vec\gamma}(t) = \vec q-\vec p\neq\vec 0, \qquad t\in[0,1].$$

Regulär und doppelpunktfrei, nicht geschlossen.

**(b) Der Kreis** vom Radius $r>0$:

$$\vec\gamma(t) = (r\cos t,\ r\sin t), \qquad \dot{\vec\gamma}(t) = r\,(-\sin t,\ \cos t), \qquad t\in[0,2\pi].$$

Die Geschwindigkeit hat den Betrag $r$, ist also nie null. Geschlossen, und doppelpunktfrei, denn nur Anfangs- und Endzeit
treffen denselben Punkt.

**(c) Der Rand des Einheitsquadrats**, gegen den Uhrzeigersinn, auf $[0,4]$:

$$\vec\gamma(t) = \begin{cases}(t,\,0), & 0\le t\le1,\\ (1,\,t-1), & 1\le t\le2,\\ (3-t,\,1), & 2\le t\le3,\\ (0,\,4-t), & 3\le t\le4.\end{cases}$$

An den Ecken passen die Stücke aneinander, die Kurve ist stetig. Die Knickstellen sind $t=1,2,3$; auf jedem Stück hat die
Geschwindigkeit den Betrag $1$. Regulär, geschlossen, doppelpunktfrei.

**(d) Die Spitze.**

$$\vec\gamma(t) = (t^3,\ t^2), \qquad \dot{\vec\gamma}(t) = (3t^2,\ 2t), \qquad t\in[-1,1].$$

Die Kurve ist sogar stetig differenzierbar, aber bei $t=0$ ist die Geschwindigkeit der Nullvektor: **nicht regulär**. Ihre
Spur ist der Graph der Funktion $\lvert x\rvert^{2/3}$, der im Ursprung eine Spitze hat — dort gibt es keine
Fahrtrichtung.

**(e) Die Acht.**

$$\vec\gamma(t) = (\sin t,\ \sin t\cos t), \qquad \dot{\vec\gamma}(t) = (\cos t,\ \cos2t), \qquad t\in[0,2\pi].$$

Die Geschwindigkeit verschwindet nie: Wo $\cos t$ null ist, also zu den Zeiten $\tfrac{\pi}{2}$ und $\tfrac{3\pi}{2}$,
ist $\cos2t$ gleich $-1$. Die Kurve ist regulär und geschlossen, aber nicht doppelpunktfrei — sie geht bei $t=\pi$ ein zweites
Mal durch den Ursprung.

**Im Bild:** Bei (d) bremst die Radfahrerin bis zum Stillstand und fährt in einer Spitze wieder heraus; bei (e) kreuzt sie
ihre eigene Spur.
::::

## Das Kurvenintegral

**Die Akteure:** eine offene Menge $U\subseteq\mathbb{R}^n$, ein stetiges Vektorfeld $\vec F:U\to\mathbb{R}^n$ — der Wind —
und eine regulär parametrisierte Kurve $\vec\gamma:[a,b]\to\mathbb{R}^n$, die ganz in $U$ verläuft — die Tour.

**Das Zusammenspiel:** *Wie viel Arbeit leistet der Wind auf der Tour?*

:::formel Definition
$$\int_\gamma\vec F\cdot d\vec x := \int_a^b \vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)\,dt.$$
:::

**So liest man das:**

- $\vec F(\vec\gamma(t))$ ist der Wind am Ort der Radfahrerin zur Zeit $t$ — ein Vektor.
- $\dot{\vec\gamma}(t)$ ist ihre Geschwindigkeit — ebenfalls ein Vektor.
- Das Skalarprodukt macht aus den beiden Vektoren eine Zahl: Windanteil in Fahrtrichtung mal Tempo.
- Das Integral über $t$ summiert diese Zahlen über die ganze Fahrzeit. Ergebnis ist eine einzige Zahl, die Arbeit.

Bei einer Kurve mit Knicken ist das genauer die Summe über die glatten Stücke,

$$\int_\gamma\vec F\cdot d\vec x = \sum_{k=1}^{N}\int_{a_{k-1}}^{a_k}\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)\,dt,$$

weil auf jedem Stück der Integrand stetig ist. Formal schreibt man für das vektorielle __Wegelement__

$$d\vec x = \dot{\vec\gamma}(t)\,dt.$$

Die Definition braucht das Feld nur **auf** der Kurve: Es genügt, dass $t\mapsto\vec F(\vec\gamma(t))$ stetig ist.

**Im Bild:** In der kleinen Zeitspanne $dt$ rückt die Radfahrerin um das Wegstück $d\vec x$ vor. Der Wind leistet dabei die
Arbeit „Kraft mal Verschiebung", wobei nur der Anteil längs der Verschiebung zählt — das Skalarprodukt.

:::herleitung
Warum gerade dieses Integral die Arbeit ist: Man ersetzt die Tour durch ein __Sehnenpolygon__ aus geraden Etappen zwischen
den Zeitpunkten

$$a = t_0 < t_1 < \ldots < t_m = b,$$

hier auf einem glatten Stück. Auf jeder Etappe nimmt man den Wind am Anfang als konstant an und rechnet „Kraft mal
Verschiebung":

$$W_m = \sum_{k=0}^{m-1}\vec F\big(\vec\gamma(t_k)\big)\cdot\big(\vec\gamma(t_{k+1})-\vec\gamma(t_k)\big).$$

Nach dem Hauptsatz, für jede Koordinate einzeln, ist die Verschiebung das Integral der Geschwindigkeit:

$$\vec\gamma(t_{k+1})-\vec\gamma(t_k) = \int_{t_k}^{t_{k+1}}\dot{\vec\gamma}(t)\,dt.$$

Damit unterscheidet sich $W_m$ vom Kurvenintegral nur dadurch, dass auf jeder Etappe der Wind festgehalten ist:

$$W_m-\int_a^b\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)\,dt = \sum_{k=0}^{m-1}\int_{t_k}^{t_{k+1}}\Big(\vec F\big(\vec\gamma(t_k)\big)-\vec F\big(\vec\gamma(t)\big)\Big)\cdot\dot{\vec\gamma}(t)\,dt.$$

Die Funktion $t\mapsto\vec F(\vec\gamma(t))$ ist auf $[a,b]$ gleichmäßig stetig: Zu $\varepsilon>0$ gibt es ein $\delta>0$,
sodass sie sich auf Etappen kürzer als $\delta$ um weniger als $\varepsilon$ ändert. Mit der Cauchy-Schwarz-Ungleichung
und dem größten Tempo $v_{\max}$ auf dem Stück ist der Unterschied dann höchstens

$$\varepsilon\cdot v_{\max}\cdot(b-a).$$

Je feiner die Etappen, desto genauer trifft die Polygon-Arbeit das Kurvenintegral.

**Im Bild:** Statt die Kurve abzufahren, fährt man gerade Etappen und misst auf jeder den Wind am Etappenstart. Werden die
Etappen kürzer, schmiegt sich das Polygon an die Kurve, und die gemessene Arbeit an das Integral.
:::

::::beispiel Das Sehnenpolygon am Halbkreis
Die Tour sei der obere Halbkreis, der Wind der Wirbel:

$$\vec\gamma(t) = (\cos t,\ \sin t), \quad t\in[0,\pi], \qquad \vec F(x,y) = (-y,\ x).$$

Man teilt in $m$ gleiche Etappen mit den Zeitpunkten

$$t_k = \frac{k\pi}{m}.$$

Am Etappenstart ist der Wind $(-\sin t_k,\ \cos t_k)$, die Etappe ist die Sehne zum nächsten Kreispunkt. Mit dem
Additionstheorem des Sinus ergibt jede Etappe denselben Beitrag:

$$\vec F\big(\vec\gamma(t_k)\big)\cdot\big(\vec\gamma(t_{k+1})-\vec\gamma(t_k)\big) = \sin t_{k+1}\cos t_k-\cos t_{k+1}\sin t_k = \sin\frac{\pi}{m}.$$

:::herleitung
Ausmultipliziert:

$$(-\sin t_k)\big(\cos t_{k+1}-\cos t_k\big)+\cos t_k\big(\sin t_{k+1}-\sin t_k\big) = \cos t_k\sin t_{k+1}-\sin t_k\cos t_{k+1},$$

denn die Terme $\sin t_k\cos t_k$ heben sich weg. Das ist der Sinus der Differenz $t_{k+1}-t_k$, also von $\tfrac{\pi}{m}$.
:::

Die Polygon-Arbeit ist also

$$W_m = m\,\sin\frac{\pi}{m}.$$

| Etappen $m$ | $1$ | $2$ | $4$ | $6$ | $\to\infty$ |
|---|---|---|---|---|---|
| Arbeit $W_m$ | $0$ | $2$ | $2\sqrt2\approx2{,}83$ | $3$ | $\pi$ |

**Im Bild:** Mit einer einzigen Etappe fährt man quer durch den Kreis; der Wind am Start bläst genau senkrecht dazu und
leistet nichts. Je mehr Etappen, desto mehr folgt man dem Kreis, auf dem der Wirbel immer von hinten kommt — die Arbeit
wächst gegen $\pi$, den Wert des Kurvenintegrals.
::::

**Linearität.** Zwei Winde zusammen leisten die Summe ihrer Arbeiten. Für stetige Vektorfelder $\vec F,\vec G$ und Zahlen
$\lambda,\mu\in\mathbb{R}$ gilt

$$\int_\gamma\big(\lambda\vec F+\mu\vec G\big)\cdot d\vec x = \lambda\int_\gamma\vec F\cdot d\vec x+\mu\int_\gamma\vec G\cdot d\vec x.$$

:::herleitung
Das Skalarprodukt ist linear in seinem ersten Faktor, der Integrand also

$$\big(\lambda\vec F+\mu\vec G\big)\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = \lambda\,\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)+\mu\,\vec G\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t),$$

und das gewöhnliche Integral ist linear.
:::

::::beispiel Drei Winde auf dem Halbkreis
Die Tour ist wieder der obere Halbkreis von $(1,0)$ nach $(-1,0)$:

$$\vec\gamma(t) = (\cos t,\ \sin t), \qquad \dot{\vec\gamma}(t) = (-\sin t,\ \cos t), \qquad t\in[0,\pi].$$

**(a) Radialer Wind.**

$$\vec F(x,y) = (x,\ y), \qquad \vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = -\cos t\sin t+\sin t\cos t = 0.$$

Die Arbeit ist $0$: Der Wind bläst überall vom Mittelpunkt weg, also genau von der Seite.

**(b) Der Wirbel.**

$$\vec F(x,y) = (-y,\ x), \qquad \vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = \sin^2t+\cos^2t = 1.$$

Die Arbeit ist $\int_0^\pi1\,dt=\pi$: Der Wind kommt überall von hinten, mit der Stärke $1$.

**(c) Konstanter Ostwind.**

$$\vec F(x,y) = (1,\ 0), \qquad \vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = -\sin t, \qquad \int_0^\pi(-\sin t)\,dt = -2.$$

Der Wind bläst nach rechts, die Tour führt insgesamt um $2$ nach links — Gegenwind. Bei einem konstanten Wind ist die Arbeit
einfach Wind mal Verschiebung:

$$(1,0)\cdot\big((-1,0)-(1,0)\big) = -2.$$

**(d) Linearität.** Radialer Wind plus Wirbel,

$$\vec F(x,y) = (x-y,\ y+x),$$

leistet $0+\pi=\pi$. Direkt nachgerechnet:

$$(\cos t-\sin t)(-\sin t)+(\sin t+\cos t)\cos t = \sin^2t+\cos^2t = 1.$$

**Im Bild:** Seitenwind kostet nichts, Rückenwind hilft, Gegenwind bremst — und zwei Winde zusammen leisten die Summe.
::::

## Das Tempo ist egal: Umparametrisierung

Fährt man dieselbe Strecke in derselben Richtung, aber mit anderem Tempo, ändert sich die Arbeit nicht. Mathematisch heißt
ein anderes Tempo: Man ersetzt die Zeit $t$ durch eine neue Zeit $s$, mit einer stetig differenzierbaren, streng monoton
wachsenden Funktion

$$\sigma:[\alpha,\beta]\to[a,b], \qquad \sigma(\alpha)=a, \qquad \sigma(\beta)=b.$$

Die neue Tour $\vec\gamma\circ\sigma$ besucht dieselben Orte in derselben Reihenfolge, nur zu anderen Zeiten.

:::formel Lemma
$$\int_\alpha^\beta \vec F\big(\vec\gamma(\sigma(s))\big)\cdot\frac{d}{ds}\,\vec\gamma\big(\sigma(s)\big)\,ds = \int_a^b \vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)\,dt.$$
:::

**So liest man das:** Links fährt man die Tour nach der neuen Uhr $s$, rechts nach der alten Uhr $t$. Kurz:

$$\int_{\gamma\circ\sigma}\vec F\cdot d\vec x = \int_\gamma\vec F\cdot d\vec x.$$

**Im Bild:** Fährt man doppelt so schnell, ist der Windanteil pro Zeit doppelt so groß, aber man ist nur halb so lange
unterwegs. Beides hebt sich auf — die Arbeit hängt am Weg, nicht an der Uhr.

:::herleitung
Nach der Kettenregel ist die neue Geschwindigkeit die alte, gestreckt mit dem Faktor $\sigma'$:

$$\frac{d}{ds}\,\vec\gamma\big(\sigma(s)\big) = \dot{\vec\gamma}\big(\sigma(s)\big)\,\sigma'(s).$$

Die linke Seite des Lemmas wird damit zu

$$\int_\alpha^\beta \vec F\big(\vec\gamma(\sigma(s))\big)\cdot\dot{\vec\gamma}\big(\sigma(s)\big)\,\sigma'(s)\,ds,$$

und die Substitutionsregel mit

$$t=\sigma(s), \qquad dt=\sigma'(s)\,ds$$

macht daraus die rechte Seite; die Grenzen $\alpha,\beta$ gehen in $a,b$ über. Bei einer Kurve mit Knicken rechnet man so auf jedem glatten Stück. Das Lemma gilt auch, wenn $\sigma'$
an einzelnen Stellen null ist; nur ist $\vec\gamma\circ\sigma$ dort nicht mehr regulär.
:::

::::beispiel Dieselbe Tour, anderes Tempo
Der Wirbel auf dem oberen Halbkreis leistete $\pi$. Zwei andere Uhren:

**(a) Doppelt so schnell.** Mit

$$\sigma(s) = 2s, \qquad s\in\big[0,\tfrac{\pi}{2}\big],$$

ist die Geschwindigkeit $2\,(-\sin2s,\ \cos2s)$, der Integrand also $2$, und

$$\int_0^{\pi/2}2\,ds = \pi.$$

**(b) Anfahren aus dem Stand.** Mit

$$\sigma(s) = \pi s^2, \qquad s\in[0,1],$$

ist die Geschwindigkeit $2\pi s\,\big(-\sin(\pi s^2),\ \cos(\pi s^2)\big)$. Der Wind am Ort ist
$\big(-\sin(\pi s^2),\ \cos(\pi s^2)\big)$, der Integrand also $2\pi s$:

$$\int_0^1 2\pi s\,ds = \pi.$$

**Im Bild:** Ob man zügig fährt oder langsam anfährt und dann beschleunigt — der Rückenwind leistet auf derselben Strecke
dieselbe Arbeit. Bei (b) steht die Radfahrerin am Start kurz still; die neue Uhr ist dort nicht regulär, das Lemma gilt
trotzdem.
::::

## Die Richtung zählt: Orientierung

Fährt man dieselbe Strecke **zurück**, kehrt sich die Arbeit um. Die Rückfahrt ist die Kurve

$$\vec\gamma_-(t) := \vec\gamma(a+b-t), \qquad t\in[a,b].$$

Sie beginnt bei $\vec\gamma(b)$ und endet bei $\vec\gamma(a)$. Üblich ist auch die Schreibweise $\gamma^{-1}$ — gemeint ist
dann nicht die Umkehrabbildung, sondern die rückwärts durchlaufene Kurve.

:::formel Satz
$$\int_{\gamma_-}\vec F\cdot d\vec x = -\int_\gamma\vec F\cdot d\vec x.$$
:::

**Im Bild:** Auf der Rückfahrt kommt jeder Wind, der vorher von hinten kam, von vorn. Der Ort ist derselbe, die
Fahrtrichtung entgegengesetzt — also wechselt der Windanteil in Fahrtrichtung überall das Vorzeichen.

:::herleitung
Die Geschwindigkeit der Rückfahrt ist nach der Kettenregel

$$\dot{\vec\gamma}_-(t) = -\dot{\vec\gamma}(a+b-t).$$

Mit der Substitution

$$u=a+b-t, \qquad du=-dt,$$

die die Grenzen vertauscht, folgt

$$\int_a^b\vec F\big(\vec\gamma(a+b-t)\big)\cdot\big(-\dot{\vec\gamma}(a+b-t)\big)\,dt = \int_b^a\vec F\big(\vec\gamma(u)\big)\cdot\dot{\vec\gamma}(u)\,du = -\int_a^b\vec F\big(\vec\gamma(u)\big)\cdot\dot{\vec\gamma}(u)\,du.$$

Das ist die Umparametrisierung mit der **fallenden** Funktion $\sigma(t)=a+b-t$ — bei ihr dreht die Substitution die
Grenzen um, und das gibt das Minuszeichen.
:::

::::beispiel Hin und zurück
**(a) Der Wirbel auf der Rückfahrt.** Der obere Halbkreis rückwärts:

$$\vec\gamma_-(t) = \big(\cos(\pi-t),\ \sin(\pi-t)\big) = (-\cos t,\ \sin t), \qquad \dot{\vec\gamma}_-(t) = (\sin t,\ \cos t).$$

Der Wirbel ist dort $(-\sin t,\ -\cos t)$, der Integrand

$$-\sin^2t-\cos^2t = -1, \qquad \int_0^\pi(-1)\,dt = -\pi.$$

**(b) Hin und auf demselben Weg zurück** ergibt für **jeden** Wind null: Die Rückfahrt leistet genau das Negative der
Hinfahrt.

**(c) Eine echte Rundtour** ist etwas anderes. Auf dem ganzen Kreis, mit

$$\vec\gamma(t) = (\cos t,\ \sin t), \qquad t\in[0,2\pi],$$

kommt der Wirbel überall von hinten, und die Arbeit ist

$$\int_0^{2\pi}1\,dt = 2\pi\neq0.$$

**Im Bild:** Wer hin und auf derselben Straße zurückfährt, gewinnt vom Wind nichts. Wer im Wirbel eine Runde dreht, hat
überall Rückenwind — ob ein Wind auf Rundtouren Arbeit leisten kann, ist das Thema des nächsten Artikels.
::::

## Linienelement und Bogenlänge

Zerlegt man das Wegelement $d\vec x$ in **Länge** und **Richtung**, entstehen zwei wichtige Größen: der Kilometerzähler und
der Lenker.

:::formel Definition
$$ds := \lvert\dot{\vec\gamma}(t)\rvert\,dt, \qquad \vec\tau\big(\vec\gamma(t)\big) := \frac{\dot{\vec\gamma}(t)}{\lvert\dot{\vec\gamma}(t)\rvert}, \qquad \mathcal L(\gamma) := \int_a^b\lvert\dot{\vec\gamma}(t)\rvert\,dt = \int_\gamma ds.$$
:::

**So liest man das:** $ds$ ist das __Linienelement__, das in der Zeit $dt$ zurückgelegte Wegstück — Tempo mal Zeit, eine
positive Zahl. $\vec\tau$ ist der __orientierte Einheitstangentialvektor__, die reine Fahrtrichtung mit der Länge $1$; er
existiert, weil die Kurve regulär ist, und an Knickstellen nimmt man die rechtsseitige Ableitung. $\mathcal L(\gamma)$ ist
die __Bogenlänge__, die gesamte gefahrene Strecke.

**Im Bild:** $ds$ ist das, was der Kilometerzähler in der Zeit $dt$ weiterzählt, $\vec\tau$ zeigt, wohin der Lenker zeigt,
und $\mathcal L$ ist der Stand des Kilometerzählers am Ende der Tour.

:::herleitung
**Warum $\mathcal L$ die Länge ist.** Die Länge einer Kurve misst man über Sehnenpolygone: Ihre Längen sind nie größer als
die Bogenlänge und kommen ihr beliebig nahe.

**Nie größer.** Für jede Etappe gilt

$$\big\lvert\vec\gamma(t_{k+1})-\vec\gamma(t_k)\big\rvert = \Big\lvert\int_{t_k}^{t_{k+1}}\dot{\vec\gamma}(t)\,dt\Big\rvert \le \int_{t_k}^{t_{k+1}}\lvert\dot{\vec\gamma}(t)\rvert\,dt.$$

Die Ungleichung für das Integral eines Vektors folgt aus Cauchy-Schwarz: Ist $\vec e$ der Einheitsvektor in Richtung der
Verschiebung, so ist ihr Betrag

$$\vec e\cdot\int\dot{\vec\gamma}\,dt = \int\vec e\cdot\dot{\vec\gamma}\,dt \le \int\lvert\dot{\vec\gamma}\rvert\,dt.$$

Summiert über die Etappen: Kein Sehnenpolygon ist länger als $\mathcal L(\gamma)$.

**Beliebig nahe.** Auf einem glatten Stück ist $\dot{\vec\gamma}$ gleichmäßig stetig. Auf Etappen kürzer als ein passendes
$\delta$ weicht es um weniger als $\varepsilon$ vom Wert am Etappenstart ab, und dann ist

$$\big\lvert\vec\gamma(t_{k+1})-\vec\gamma(t_k)\big\rvert \ge \lvert\dot{\vec\gamma}(t_k)\rvert\,(t_{k+1}-t_k)-\varepsilon\,(t_{k+1}-t_k).$$

Summiert ist das eine Riemann-Summe von $\lvert\dot{\vec\gamma}\rvert$ minus $\varepsilon(b-a)$ — sie kommt dem Integral
beliebig nahe.

**Im Bild:** Eine Abkürzung über die Sehne ist nie länger als die Kurve, und kurze Sehnen schmiegen sich an sie an.
:::

**Das Kurvenintegral mit Länge und Richtung.** Mit dem Linienelement integriert man auch Skalarfelder längs einer Kurve:
Für eine stetige Funktion $f$ auf der Spur ist das __skalare Kurvenintegral__

$$\int_\gamma f\,ds := \int_a^b f\big(\vec\gamma(t)\big)\,\lvert\dot{\vec\gamma}(t)\rvert\,dt,$$

etwa die Masse eines Drahts mit der Liniendichte $f$. Das Kurvenintegral eines Vektorfelds ist dann das skalare
Kurvenintegral des Windanteils in Fahrtrichtung:

$$\int_\gamma\vec F\cdot d\vec x = \int_\gamma\vec F\cdot\vec\tau\,ds.$$

**Im Bild:** „Windanteil in Fahrtrichtung mal gefahrene Kilometer" — das ist das Leitbild, jetzt als Formel. Und ein
Unterschied: Das skalare Kurvenintegral hängt **nicht** von der Fahrtrichtung ab, denn das Linienelement ist immer
positiv. Ein Draht wiegt in beiden Richtungen gleich viel.

:::herleitung
**Die Zerlegung.** Weil die Kurve regulär ist, darf man durch das Tempo teilen:

$$\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = \vec F\big(\vec\gamma(t)\big)\cdot\vec\tau\big(\vec\gamma(t)\big)\,\lvert\dot{\vec\gamma}(t)\rvert.$$

Integriert über $t$ ist das links das Kurvenintegral, rechts das skalare Kurvenintegral der Funktion $\vec F\cdot\vec\tau$.

**Die Richtung spielt beim skalaren Integral keine Rolle.** Für die Rückfahrt ist das Tempo dasselbe,

$$\lvert\dot{\vec\gamma}_-(t)\rvert = \lvert\dot{\vec\gamma}(a+b-t)\rvert,$$

und dieselbe Substitution wie bei der Rückfahrt vertauscht die Grenzen und bringt mit dem Faktor $-1$ im Differential ein
zweites Minuszeichen — beide heben sich auf. Beim Kurvenintegral eines Vektorfelds kam das dritte Minuszeichen aus der umgedrehten Geschwindigkeit; hier fehlt es.
:::

::::beispiel Kilometerzähler und Drahtmasse
**(a) Der Kreis** vom Radius $r$ hat das Tempo $r$, also die Länge

$$\mathcal L = \int_0^{2\pi}r\,dt = 2\pi r.$$

**(b) Eine Schraubenlinie** — eine Windung einer Wendeltreppe —

$$\vec\gamma(t) = (\cos t,\ \sin t,\ t), \qquad \dot{\vec\gamma}(t) = (-\sin t,\ \cos t,\ 1), \qquad \lvert\dot{\vec\gamma}(t)\rvert = \sqrt2,$$

hat auf $[0,2\pi]$ die Länge $2\pi\sqrt2$. Zur Probe abgewickelt: Die Windung wird zur Schrägen eines rechtwinkligen
Dreiecks mit den Katheten $2\pi$ (einmal herum) und $2\pi$ (Höhengewinn), und deren Länge ist nach Pythagoras ebenfalls
$2\pi\sqrt2$.

**(c) Der Wirbel als Windanteil.** Auf dem oberen Halbkreis ist die Einheitstangente

$$\vec\tau = (-\sin t,\ \cos t),$$

und der Wirbel hat in Fahrtrichtung überall den Anteil $1$. Das Kurvenintegral ist also die Länge:

$$\int_\gamma\vec F\cdot\vec\tau\,ds = \int_\gamma1\,ds = \pi.$$

**(d) Ein Draht** in Form des oberen Halbkreises, oben schwerer, mit der Liniendichte

$$f(x,y) = y,$$

hat die Masse

$$\int_\gamma y\,ds = \int_0^\pi\sin t\cdot1\,dt = 2.$$

Rückwärts parametrisiert, mit $(-\cos t,\ \sin t)$, ist das Tempo wieder $1$ und die Höhe wieder $\sin t$: wieder $2$.

**Im Bild:** Der Kilometerzähler kennt keine Richtung — die Arbeit des Winds schon.
::::

## Kurven als Wege: Spur, Orientierung, Etappen

Bisher war eine Kurve eine Vorschrift mit Uhr. Für die Arbeit des Winds zählen aber nur der **Weg** und seine **Richtung**.

**Spur und reguläre Kurve.** Die Punktmenge, die eine Kurve durchläuft, heißt ihre __Spur__:

$$\Gamma = \vec\gamma\big([a,b]\big)\subseteq\mathbb{R}^n.$$

Eine Menge $\Gamma\subseteq\mathbb{R}^n$ heißt __reguläre Kurve__, wenn sie die Spur einer regulär parametrisierten,
doppelpunktfreien Kurve ist. Solche Parametrisierungen schreibt man oft $\vec x(t)$ statt $\vec\gamma(t)$, und für ein
Vektorfeld $\vec F$, das in einer Umgebung von $\Gamma$ stetig ist,

$$\int_\Gamma\vec F\cdot d\vec x = \int_a^b\vec F\big(\vec x(t)\big)\cdot\dot{\vec x}(t)\,dt.$$

Dieser Wert hängt nicht davon ab, welche doppelpunktfreie Parametrisierung man wählt — solange der Durchlaufsinn derselbe
bleibt. Deshalb gibt man einer regulären Kurve immer eine __Orientierung__ mit, einen Durchlaufsinn. Die Kurve mit
umgekehrtem Durchlaufsinn heißt $-\Gamma$.

:::herleitung
Nur die Beweisidee. Seien $\vec x_1:[a,b]\to\Gamma$ und $\vec x_2:[c,d]\to\Gamma$ zwei doppelpunktfreie reguläre
Parametrisierungen mit demselben Anfangs- und Endpunkt. Weil $\vec x_1$ keinen Punkt zweimal trifft, kann man zurückrechnen,
zu welcher Zeit der ersten Uhr ein Punkt erreicht wird:

$$\sigma := \vec x_1^{-1}\circ\vec x_2:[c,d]\to[a,b].$$

$\sigma$ ist stetig und streng monoton (eine stetige, umkehrbare Abbildung eines Intervalls), und wachsend, weil beide Uhren
denselben Anfang haben. Stetig differenzierbar ist sie wegen der Regularität: In der Nähe jedes Punkts ist eine Koordinate
von $\vec x_1$ streng monoton, und über deren Umkehrfunktion lässt sich $\sigma$ ausdrücken. Nach dem Lemma über das
Tempo geben dann beide Parametrisierungen dasselbe Kurvenintegral. Mit umgekehrtem Durchlaufsinn ist $\sigma$ fallend,
und es kommt das Minuszeichen der Rückfahrt hinzu.
:::

**Rundtouren.** Bei einer geschlossenen Kurve ist das Kurvenintegral auch davon unabhängig, wo auf der Kurve man losfährt.

:::herleitung
Sei $\vec x:[a,b]\to\mathbb{R}^n$ geschlossen, und man starte stattdessen zur Zeit $c\in(a,b)$. Die neue Tour fährt erst von
$c$ bis $b$ und dann, wegen der Geschlossenheit nahtlos, das Stück von $a$ bis $c$:

$$\vec y(t) = \begin{cases}\vec x(t), & c\le t\le b,\\ \vec x\big(t-(b-a)\big), & b\le t\le c+(b-a).\end{cases}$$

Im zweiten Teil gibt die Substitution $u=t-(b-a)$ das Integral über $[a,c]$. Zusammen mit dem ersten Teil über $[c,b]$ ist
das das Integral über $[a,b]$.
:::

**Etappen aneinanderhängen.** Endet eine Kurve $\vec\gamma_1:[a,b]\to\mathbb{R}^n$ dort, wo eine zweite
$\vec\gamma_2:[c,d]\to\mathbb{R}^n$ beginnt, so fährt man erst die eine und dann die andere:

$$\vec\gamma_1\oplus\vec\gamma_2(t) := \begin{cases}\vec\gamma_1(t), & a\le t\le b,\\ \vec\gamma_2(c-b+t), & b<t\le b+d-c.\end{cases}$$

Das ist wieder eine regulär parametrisierte Kurve, an der Nahtstelle mit einem möglichen Knick. Für die zugehörigen regulären
Kurven schreibt man $\Gamma_1+\Gamma_2$, und $\Gamma_1+(-\Gamma_2)$ kurz $\Gamma_1-\Gamma_2$. Kurvenintegrale sind
__additiv__:

$$\int_{\Gamma_1\pm\Gamma_2}\vec F\cdot d\vec x = \int_{\Gamma_1}\vec F\cdot d\vec x\pm\int_{\Gamma_2}\vec F\cdot d\vec x.$$

**Im Bild:** Eine Tour aus Etappen — die Arbeit der ganzen Tour ist die Summe der Etappen-Arbeiten. Damit lässt sich auch
jede Kurve mit Doppelpunkten in doppelpunktfreie Stücke zerlegen: Man schneidet sie an den Kreuzungen auf.

:::herleitung
Man teilt das Integral über $[a,b+d-c]$ an der Nahtstelle $t=b$. Der erste Teil ist das Integral längs $\vec\gamma_1$. Im
zweiten macht die Substitution $u=c-b+t$ daraus das Integral über $[c,d]$ längs $\vec\gamma_2$. Mit $-\Gamma_2$ statt
$\Gamma_2$ kommt das Minuszeichen der Rückfahrt hinzu.
:::

::::beispiel Eine Rundtour um das Quadrat
Der Wirbel $\vec F(x,y)=(-y,\ x)$ auf dem Rand des Einheitsquadrats, gegen den Uhrzeigersinn, in vier Etappen:

| Etappe | Parametrisierung, $t\in[0,1]$ | Geschwindigkeit | Wind am Ort | Integrand | Arbeit |
|---|---|---|---|---|---|
| unten | $(t,\,0)$ | $(1,\,0)$ | $(0,\,t)$ | $0$ | $0$ |
| rechts | $(1,\,t)$ | $(0,\,1)$ | $(-t,\,1)$ | $1$ | $1$ |
| oben | $(1-t,\,1)$ | $(-1,\,0)$ | $(-1,\,1-t)$ | $1$ | $1$ |
| links | $(0,\,1-t)$ | $(0,\,-1)$ | $(t-1,\,0)$ | $0$ | $0$ |

Zusammen leistet der Wind die Arbeit $2$. Startet man stattdessen in der Ecke $(1,1)$ und fährt oben, links, unten,
rechts, ergibt sich dieselbe Summe — bei einer Rundtour ist der Startpunkt egal.

**Im Bild:** Auf der unteren und der linken Kante bläst der Wirbel genau von der Seite, auf den beiden anderen von hinten.
Dass die Arbeit gerade doppelt so groß ist wie die umfahrene Fläche, ist kein Zufall — das erklärt später der Satz von
Stokes in der Ebene.
::::

## Die Standardabschätzung

Wie bei gewöhnlichen Integralen kann man die Arbeit grob nach oben abschätzen: Betrag höchstens stärkster Wind mal Länge.

:::formel Lemma
$$\Big\lvert\int_\Gamma\vec F\cdot d\vec x\Big\rvert \le \sup_{\vec x\in\Gamma}\lvert\vec F(\vec x)\rvert\;\mathcal L(\Gamma).$$
:::

**So liest man das:** Links steht der Betrag der Arbeit, rechts der stärkste Wind auf der Spur mal die Länge der Tour. Das
Supremum ist hier ein Maximum, weil $\vec F$ auf der kompakten Spur stetig ist.

**Im Bild:** Mehr als „voller Rückenwind auf der ganzen Strecke" kann der Wind nicht leisten. Gleichheit herrscht, wenn er
überall mit voller Stärke genau von hinten — oder überall genau von vorn — kommt.

:::herleitung
Nach der Cauchy-Schwarz-Ungleichung ist der Windanteil in Fahrtrichtung höchstens die Windstärke:

$$\big\lvert\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)\big\rvert \le \lvert\vec F\big(\vec\gamma(t)\big)\rvert\,\lvert\dot{\vec\gamma}(t)\rvert \le \sup_\Gamma\lvert\vec F\rvert\cdot\lvert\dot{\vec\gamma}(t)\rvert.$$

Integriert über $[a,b]$:

$$\Big\lvert\int_\Gamma\vec F\cdot d\vec x\Big\rvert \le \int_a^b\big\lvert\vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t)\big\rvert\,dt \le \sup_\Gamma\lvert\vec F\rvert\int_a^b\lvert\dot{\vec\gamma}(t)\rvert\,dt = \sup_\Gamma\lvert\vec F\rvert\;\mathcal L(\Gamma).$$
:::

::::beispiel Die Abschätzung an den drei Winden
Auf dem oberen Halbkreis, Länge $\pi$, haben alle drei Winde die Stärke $1$. Die Schranke ist also jedes Mal $\pi$:

| Wind | Arbeit | Schranke |
|---|---|---|
| Wirbel | $\pi$ | $\pi$ |
| Ostwind $(1,0)$ | $-2$ | $\pi$ |
| radial | $0$ | $\pi$ |

**Im Bild:** Der Wirbel erreicht die Schranke, weil er überall mit voller Stärke von hinten kommt. Der Ostwind kommt nur
teilweise von vorn, der radiale Wind nur von der Seite — sie bleiben darunter.
::::

## Bedeutung und Ausblick

Das Kurvenintegral ist das Werkzeug, mit dem man Felder **längs Wegen** auswertet: die Arbeit eines Kraftfelds, in der
Elektrotechnik die Spannung zwischen zwei Punkten als Kurvenintegral des elektrischen Felds, die Umlaufspannung längs einer
Leiterschleife. Es hängt nur am Weg und seiner Richtung, nicht am Tempo.

Die Beispiele zeigen zwei Sorten Wind. Beim konstanten Ostwind war die Arbeit einfach Wind mal Verschiebung — sie hing nur
von Start und Ziel ab. Beim Wirbel brachte eine Rundtour die Arbeit $2\pi$. Welche Felder **nur von Start und Ziel**
abhängen und auf Rundtouren nichts leisten, klärt der __erste Hauptsatz für Kurvenintegrale__ im nächsten Artikel: Es sind
genau die Gradientenfelder.

:::kern
- Eine __regulär parametrisierte Kurve__ ist stückweise stetig differenzierbar und hält nie an: $\dot{\vec\gamma}\neq\vec 0$.
- __Kurvenintegral__: $\int_\gamma\vec F\cdot d\vec x=\int_a^b\vec F(\vec\gamma(t))\cdot\dot{\vec\gamma}(t)\,dt$ — Windanteil in Fahrtrichtung, über die Tour summiert.
- Es ist der Grenzwert der Arbeit längs immer feinerer Sehnenpolygone, „Kraft mal Verschiebung" auf jeder Etappe.
- Es ist **linear** im Feld: Zwei Winde leisten die Summe ihrer Arbeiten.
- **Tempo egal:** Wachsende Umparametrisierungen ändern nichts — die Arbeit hängt am Weg, nicht an der Uhr.
- **Richtung zählt:** Die Rückfahrt liefert das Negative, $\int_{\gamma_-}\vec F\cdot d\vec x=-\int_\gamma\vec F\cdot d\vec x$.
- __Linienelement__ $ds$ (Kilometerzähler), __Einheitstangente__ $\vec\tau$ (Lenker) und __Bogenlänge__ $\mathcal L$, die ganze gefahrene Strecke.
- Das skalare Kurvenintegral $\int_\gamma f\,ds$ ist richtungsunabhängig, das Kurvenintegral eines Vektorfelds nicht.
- Für reguläre Kurven $\Gamma$ zählen nur Spur und Orientierung; bei Rundtouren ist der Startpunkt egal, Etappen addieren sich.
- __Standardabschätzung__: Betrag höchstens stärkster Wind mal Länge, $\lvert\int_\Gamma\vec F\cdot d\vec x\rvert\le\sup_\Gamma\lvert\vec F\rvert\,\mathcal L(\Gamma)$.
:::

:::quiz
F: Was misst das Kurvenintegral $\int_\gamma\vec F\cdot d\vec x$, und warum steht im Integranden ein Skalarprodukt?
A: Die Arbeit, die das Feld längs der Kurve verrichtet — im Bild die Arbeit des Winds auf einer Radtour. Das Skalarprodukt $\vec F(\vec\gamma(t))\cdot\dot{\vec\gamma}(t)$ nimmt nur den Anteil des Felds in Bewegungsrichtung, mal Tempo: Rückenwind zählt positiv, Gegenwind negativ, Seitenwind gar nicht.
F: Was heißt „regulär parametrisiert", und was geht bei $(t^3,t^2)$ schief?
A: Die Kurve ist stückweise stetig differenzierbar, und ihre Geschwindigkeit ist nie der Nullvektor (an Knicken und Enden für die einseitigen Ableitungen). Dann gibt es überall eine Fahrtrichtung. $(t^3,t^2)$ ist zwar glatt, hat aber bei $t=0$ die Geschwindigkeit $\vec 0$; die Spur hat dort eine Spitze und keine Richtung.
F: Warum ist gerade $\int_a^b\vec F(\vec\gamma)\cdot\dot{\vec\gamma}\,dt$ die Arbeit?
A: Man ersetzt die Kurve durch ein Sehnenpolygon und rechnet auf jeder Etappe „Kraft am Etappenstart mal Verschiebung". Die Verschiebung ist das Integral der Geschwindigkeit, und weil $\vec F(\vec\gamma(t))$ gleichmäßig stetig ist, unterscheidet sich die Polygon-Arbeit vom Integral höchstens um $\varepsilon\,v_{\max}(b-a)$. Am Halbkreis im Wirbel ist die Polygon-Arbeit $m\sin\frac{\pi}{m}$, was gegen $\pi$ strebt.
F: Was leisten radialer Wind, Wirbel und konstanter Ostwind auf dem oberen Halbkreis von $(1,0)$ nach $(-1,0)$?
A: Der radiale Wind $(x,y)$ steht überall senkrecht zur Fahrtrichtung: Arbeit $0$. Der Wirbel $(-y,x)$ kommt überall mit Stärke $1$ von hinten: Arbeit $\pi$. Der Ostwind $(1,0)$ ist konstant, die Arbeit ist Wind mal Verschiebung, $(1,0)\cdot(-2,0)=-2$ — Gegenwind.
F: Warum ändert ein anderes Tempo die Arbeit nicht?
A: Ein anderes Tempo ist eine wachsende Umparametrisierung $t=\sigma(s)$. Die neue Geschwindigkeit ist die alte mal $\sigma'(s)$, und die Substitutionsregel mit $dt=\sigma'(s)\,ds$ hebt diesen Faktor genau auf. Im Bild: doppelt so schnell heißt doppelter Windanteil pro Zeit, aber halbe Fahrzeit.
F: Warum wechselt die Arbeit bei der Rückfahrt das Vorzeichen — und warum ist das bei einer Rundtour im Wirbel trotzdem nicht null?
A: Auf der Rückfahrt $\vec\gamma(a+b-t)$ ist die Geschwindigkeit überall umgedreht, aus Rückenwind wird Gegenwind, also $\int_{\gamma_-}=-\int_\gamma$. Hin und auf demselben Weg zurück ergibt darum null. Eine echte Rundtour wie der ganze Kreis führt aber auf einem anderen Weg zurück; im Wirbel ist dort überall Rückenwind, und die Arbeit ist $2\pi$.
F: Was sind Linienelement, Einheitstangente und Bogenlänge, und wie lang ist eine Windung der Schraubenlinie $(\cos t,\sin t,t)$?
A: $ds=\lvert\dot{\vec\gamma}\rvert\,dt$ ist das in der Zeit $dt$ gefahrene Wegstück (Kilometerzähler), $\vec\tau=\dot{\vec\gamma}/\lvert\dot{\vec\gamma}\rvert$ die Fahrtrichtung (Lenker), $\mathcal L=\int\lvert\dot{\vec\gamma}\rvert\,dt$ die ganze Strecke. Die Schraubenlinie hat das Tempo $\sqrt2$, eine Windung also die Länge $2\pi\sqrt2$ — wie die Schräge des abgewickelten Dreiecks mit zwei Katheten $2\pi$.
F: Warum hängt die Drahtmasse $\int_\gamma f\,ds$ nicht von der Richtung ab, die Arbeit $\int_\gamma\vec F\cdot d\vec x$ aber schon?
A: Im skalaren Integral steht das Tempo $\lvert\dot{\vec\gamma}\rvert$, das bei der Rückfahrt gleich bleibt; das Minuszeichen aus $du=-dt$ und das aus den vertauschten Grenzen heben sich auf. Im Vektorfeld-Integral steht die Geschwindigkeit selbst, die sich umdreht — ein drittes Minuszeichen. Der Halbkreis-Draht mit Dichte $y$ wiegt in beiden Richtungen $2$.
F: Warum zählen bei einer regulären Kurve $\Gamma$ nur Spur und Orientierung, und was gilt für Rundtouren und Etappen?
A: Zwei doppelpunktfreie Parametrisierungen derselben Spur mit gleichem Anfang gehen durch eine wachsende Umparametrisierung $\sigma=\vec x_1^{-1}\circ\vec x_2$ auseinander hervor, und die ändert das Integral nicht. Bei geschlossenen Kurven ist zudem der Startpunkt egal, und hängt man Etappen aneinander, addieren sich die Integrale — beim Wirbel auf dem Quadratrand zu $0+1+1+0=2$.
F: Was besagt die Standardabschätzung, und wann gilt Gleichheit?
A: $\lvert\int_\Gamma\vec F\cdot d\vec x\rvert\le\sup_\Gamma\lvert\vec F\rvert\,\mathcal L(\Gamma)$: Der Windanteil in Fahrtrichtung ist nach Cauchy-Schwarz höchstens die Windstärke, integriert ergibt das stärksten Wind mal Länge. Gleichheit gilt, wenn der Wind überall mit voller Stärke genau von hinten (oder genau von vorn) kommt — wie der Wirbel auf dem Halbkreis mit Arbeit $\pi$ und Schranke $\pi$.
:::
