---
title: Schwebung und das Produkt zweier Sinussignale
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Spektrum und Fourier-Reihe
order: 20150
summary: Von Grund auf – warum zwei fast gleich hohe Töne ein langsames „Wah-wah" erzeugen (die Schwebung), wie eine einzige Identität Summe und Produkt zweier Kosinus verbindet ($2\cos\omega_\Delta t\,\cos\omega_M t = \cos\omega_1 t + \cos\omega_2 t$), warum die Schwebung keine eigene Spektrallinie hat und wieso das Produkt zweier Sinus vier Linien erzeugt – die Grundlage der Amplitudenmodulation.
tags: Schwebung, Schwebungston, Produkt zweier Sinussignale, Amplitudenmodulation, Hüllkurve, Trägerfrequenz, Seitenbänder
---

:::grafik
Einstiegs-Animation: Zwei Stimmgabeln mit leicht verschiedenen Tönen erklingen. Ihre beiden sauberen Sinuskurven
(fast gleiche Frequenz) werden addiert; die Summenkurve zeigt eine **schnelle** Schwingung, deren **Höhe langsam
an- und abschwillt** — eine ein- und ausatmende „Bauchbinde" (Hüllkurve) läuft darüber. Ein Ohr-Symbol pulsiert
im Takt dieses An- und Abschwellens. Kernbotschaft: Zwei dicht benachbarte Töne verschmelzen zu **einem** Ton,
dessen Lautstärke langsam pulsiert — das ist die Schwebung.
:::

:::konzept
Schlägt man zwei Klaviersaiten an, die fast — aber nicht ganz — gleich gestimmt sind, hört man nicht zwei Töne,
sondern **einen** Ton, der regelmäßig lauter und leiser wird: ein „Wah-wah-wah". Das ist die __Schwebung__, und
Klavierstimmer nutzen sie direkt (je langsamer das Pulsieren, desto reiner die Stimmung). Dahinter steckt eine
einzige trigonometrische Identität, die **Summe** und **Produkt** zweier Kosinusschwingungen ineinander
überführt. Dieselbe Identität ist – rückwärts gelesen – die Grundlage der **Amplitudenmodulation**, mit der jeder
AM-Radiosender arbeitet. Wir leiten alles aus der Eulerschen Formel her.
:::

**Worum es geht:** Wir addieren zwei Sinussignale fast gleicher Frequenz, formen die Summe in ein **Produkt**
aus langsamer __Hüllkurve__ und schneller __Trägerschwingung__ um, erklären daraus die hörbare __Schwebung__,
bestimmen das __Spektrum__ von Summe und Produkt und schlagen die Brücke zur __Amplitudenmodulation__.

## Mittenfrequenz und Differenzfrequenz

Wir betrachten zwei Kosinussignale gleicher Amplitude mit den Kreisfrequenzen $\omega_1$ und $\omega_2$, die
nahe beieinander liegen ($\omega_1 \approx \omega_2$). Statt mit $\omega_1$ und $\omega_2$ rechnet es sich viel
klarer mit zwei abgeleiteten Größen:

$$\omega_M = \tfrac{1}{2}(\omega_1 + \omega_2), \qquad \omega_\Delta = \tfrac{1}{2}(\omega_2 - \omega_1).$$

- __$\omega_M$__: die __Mittenfrequenz__ — der Mittelwert der beiden Frequenzen (groß, denn beide liegen hoch).
- __$\omega_\Delta$__: die halbe __Differenzfrequenz__ — wie weit die beiden auseinanderliegen (klein, denn sie
  sind fast gleich).

Umgekehrt ist dann $\omega_1 = \omega_M - \omega_\Delta$ und $\omega_2 = \omega_M + \omega_\Delta$: Die beiden
Töne liegen symmetrisch um die Mittenfrequenz, je um $\omega_\Delta$ nach unten und oben versetzt. Diese
Zerlegung ist der Schlüssel zu allem Weiteren.

## Die zentrale Identität: Summe wird Produkt

Jetzt die entscheidende Rechnung. Wir multiplizieren die langsame und die schnelle Schwingung und zeigen mit der
Eulerschen Formel, dass daraus genau die Summe unserer beiden Töne wird. Mit $\cos\alpha = \tfrac12(e^{j\alpha} +
e^{-j\alpha})$:

$$\cos(\omega_M t)\cdot\cos(\omega_\Delta t) = \tfrac{1}{2}\big(e^{j\omega_M t} + e^{-j\omega_M t}\big)\cdot\tfrac{1}{2}\big(e^{j\omega_\Delta t} + e^{-j\omega_\Delta t}\big).$$

Multipliziert man die beiden Klammern aus (jedes Glied mit jedem), entstehen vier Exponentialterme, deren
Exponenten sich jeweils addieren:

$$= \tfrac{1}{4}\Big(e^{j(\omega_M + \omega_\Delta)t} + e^{-j(\omega_M + \omega_\Delta)t} + e^{j(\omega_M - \omega_\Delta)t} + e^{-j(\omega_M - \omega_\Delta)t}\Big).$$

Je zwei dieser Terme (mit $+$ und $-$ im Exponenten) bilden wieder einen Kosinus, und mit $\omega_M + \omega_\Delta
= \omega_2$ sowie $\omega_M - \omega_\Delta = \omega_1$ wird daraus

$$\cos(\omega_M t)\,\cos(\omega_\Delta t) = \tfrac{1}{2}\cos(\omega_2 t) + \tfrac{1}{2}\cos(\omega_1 t).$$

Multipliziert man beide Seiten mit $2$, hat man die **zentrale Identität** in beide Richtungen lesbar:

$$\boxed{\;\cos(\omega_1 t) + \cos(\omega_2 t) = 2\,\cos(\omega_\Delta t)\,\cos(\omega_M t)\;}$$

**Links** steht die Summe zweier Töne, **rechts** ein Produkt aus einer **langsamen** Schwingung $\cos(\omega_\Delta
t)$ (kleine Frequenz) und einer **schnellen** $\cos(\omega_M t)$ (große Frequenz). Beides ist dasselbe Signal — nur
anders hingeschrieben. Genau diese Doppeldeutung erklärt die Schwebung.

:::grafik
Rechenkette als Tafelbild: oben das Produkt $\cos\omega_M t\cos\omega_\Delta t$, über die Eulersche Formel in vier
Exponentialterme zerlegt, diese paarweise zu $\tfrac12\cos\omega_2 t+\tfrac12\cos\omega_1 t$ zusammengefasst;
Ergebnis als eingerahmte Identität $\cos\omega_1 t+\cos\omega_2 t=2\cos\omega_\Delta t\,\cos\omega_M t$. Die
Zuordnung $\omega_1=\omega_M-\omega_\Delta$, $\omega_2=\omega_M+\omega_\Delta$ farbig markiert.
:::

## Warum man eine Schwebung hört

Lesen wir die Identität von der **Produkt**-Seite. Das Summensignal

$$s(t) = \cos(\omega_1 t) + \cos(\omega_2 t) = \underbrace{2\cos(\omega_\Delta t)}_{\text{Hüllkurve}}\cdot\underbrace{\cos(\omega_M t)}_{\text{Träger}}$$

ist eine schnelle Trägerschwingung mit der Mittenfrequenz $\omega_M$, deren Amplitude nicht konstant ist, sondern
langsam mit $\cos(\omega_\Delta t)$ **auf- und abschwillt**. Man hört deshalb einen Ton der (mittleren) Tonhöhe
$\omega_M$, dessen **Lautstärke** sich langsam ändert — das ist die __Schwebung__.

- __Träger__ $\cos(\omega_M t)$: die eigentliche, schnell schwingende Tonhöhe (Mittelwert der beiden Töne).
- __Hüllkurve__ $2\cos(\omega_\Delta t)$: der langsam veränderliche Faktor, der die Amplitude „einpackt".

**Stolperstein — Schwebungsfrequenz ist doppelt so hoch wie die Hüllkurve.** Die Hüllkurve $2\cos(\omega_\Delta
t)$ schwingt mit $\omega_\Delta$. Das Ohr nimmt aber **Lautstärke** wahr, und die hängt nur vom **Betrag** der
Amplitude ab — ob die Hüllkurve gerade $+$ oder $-$ ist, klingt gleich laut. Pro voller Hüllkurven-Periode wird
es deshalb **zweimal** laut (bei maximalem $+$ und bei maximalem $-$) und zweimal leise (an den Nulldurchgängen).
Die hörbare __Schwebungsfrequenz__ ist daher doppelt so groß wie die der Hüllkurve:

$$\omega_\text{Schwebung} = 2\,\omega_\Delta = \omega_2 - \omega_1 \qquad\Longleftrightarrow\qquad f_\text{Schwebung} = f_2 - f_1.$$

Das ist ein schönes, überprüfbares Ergebnis: Die Schwebung pulsiert mit genau der **Differenz** der beiden
Tonfrequenzen. Stimmt man eine Saite der anderen an, wird das Pulsieren immer langsamer und verschwindet, wenn
beide exakt gleich sind.

:::grafik
Drei übereinanderliegende Zeitkurven über derselben Achse: oben $\cos\omega_1 t$, darunter $\cos\omega_2 t$
(minimal andere Frequenz), unten ihre Summe $s(t)$ — eine schnelle Schwingung mit langsam an- und abschwellender
Amplitude. Die Hüllkurve $\pm 2\cos\omega_\Delta t$ ist gestrichelt eingezeichnet; markiert sind die **zwei**
Lautstärke-Maxima pro Hüllkurven-Periode, die zeigen, dass die Schwebung mit $2\omega_\Delta=\omega_2-\omega_1$
pulsiert.
:::

## Die Spektren: Summe gegen Produkt

Jetzt die Spektren — und hier zeigt sich ein überraschender, prüfungsrelevanter Unterschied. Wir nutzen die
zweiseitige Darstellung mit Koeffizienten $a_k$ aus dem vorigen Abschnitt.

**Spektrum der Summe (Schwebung).** Das Signal $s(t) = \cos\omega_1 t + \cos\omega_2 t$ ist einfach die Summe
zweier Kosinus, also hat es genau **zwei** Linien (plus ihre konjugierten Spiegelbilder bei den negativen
Frequenzen): bei $\omega_1$ und $\omega_2$, jede mit $|a| = \tfrac12$. Entscheidend:

- Bei der tatsächlichen Pulsationsfrequenz $\omega_\Delta$ (bzw. $2\omega_\Delta$) liegt **keine** Spektrallinie.
- Bei der Mittenfrequenz $\omega_M$ liegt **keine** Linie.

Die Schwebung ist also **keine eigene Frequenz** im Signal — sie ist nur die Art, wie unser Ohr zwei dicht
benachbarte Linien gemeinsam wahrnimmt. Im Spektrum stehen nüchtern zwei Striche.

**Spektrum des Produkts.** Liest man die Identität andersherum und bildet wirklich das Produkt $s(t) =
\cos(\omega_M t)\cos(\omega_\Delta t)$, so ist es laut Identität gleich $\tfrac12\cos\omega_1 t + \tfrac12\cos\omega_2
t$ — es hat also **vier** Spektrallinien (mit den negativen Frequenzen): bei $\pm\omega_1$ und $\pm\omega_2$, jede
mit $|a| = \tfrac14$. Und wieder gilt: Bei den „Zutatenfrequenzen" $\omega_M$ und $\omega_\Delta$ selbst steht
**keine** Linie. Das Produkt erzeugt also nur die **Summen- und Differenzfrequenz** $\omega_M \pm \omega_\Delta$,
nicht die Faktoren selbst.

:::grafik
Zwei zweiseitige Betragsspektren nebeneinander. Links „Summe": zwei Linienpaare bei $\pm\omega_1$ und $\pm\omega_2$
der Höhe $\tfrac12$, dicht beieinander; Hinweispfeile „keine Linie bei $\omega_M$, keine bei $\omega_\Delta$".
Rechts „Produkt": vier Linien bei $\pm(\omega_M-\omega_\Delta)$ und $\pm(\omega_M+\omega_\Delta)$ der Höhe
$\tfrac14$; ebenfalls „keine Linie bei $\omega_M$ oder $\omega_\Delta$".
:::

## Eigenes Zahlenbeispiel

Zwei Flötentöne von $f_1 = 200\,$Hz und $f_2 = 206\,$Hz werden zusammen gespielt. Dann ist die Mittenfrequenz
$f_M = \tfrac12(200+206) = 203\,$Hz und die halbe Differenz $f_\Delta = \tfrac12(206-200) = 3\,$Hz. Man hört
einen Ton der Höhe $203\,$Hz, dessen Lautstärke mit der Schwebungsfrequenz

$$f_\text{Schwebung} = f_2 - f_1 = 2\,f_\Delta = 6\,\text{Hz}$$

pulsiert — also sechsmal pro Sekunde lauter und leiser wird. Im Spektrum der Summe stehen nur zwei Linien, bei
$200\,$Hz und $206\,$Hz; weder bei $203\,$Hz noch bei $3\,$Hz liegt etwas.

## Ausblick: Amplitudenmodulation

Die Produkt-Sichtweise ist technisch enorm wichtig. **Multipliziert** man eine hohe __Trägerschwingung__
$\cos(\omega_M t)$ mit einem langsameren Signal, so verschiebt das (nach genau derselben Identität) das Spektrum
des langsamen Signals nach oben an die Trägerfrequenz — es entstehen __Seitenbänder__ bei $\omega_M \pm
\omega_\Delta$. Das ist die __Amplitudenmodulation__ (AM): Ein hörbares (niederfrequentes) Signal wird einem
hochfrequenten Träger „aufgeprägt" und so sendefähig gemacht. Der Empfänger macht die Multiplikation rückgängig.
Dass dabei im Spektrum **keine** Linie beim Träger $\omega_M$ allein steht (nur die Seitenbänder tragen die
Information), ist genau die Eigenschaft, die wir oben gefunden haben.

:::kern
Zwei Kosinus fast gleicher Frequenz ergeben über die zentrale Identität
$\cos\omega_1 t + \cos\omega_2 t = 2\cos(\omega_\Delta t)\cos(\omega_M t)$ (mit __Mittenfrequenz__
$\omega_M = \tfrac12(\omega_1+\omega_2)$ und halber __Differenzfrequenz__ $\omega_\Delta =
\tfrac12(\omega_2-\omega_1)$) einen __Träger__ $\cos\omega_M t$ mit langsam schwellender __Hüllkurve__
$2\cos\omega_\Delta t$ — die __Schwebung__. Weil das Ohr den Betrag der Hüllkurve hört, pulsiert sie mit
$\omega_\text{Schwebung} = 2\omega_\Delta = \omega_2 - \omega_1$ ($f_\text{Schwebung} = f_2 - f_1$). Das
__Spektrum der Summe__ hat nur zwei Linien (bei $\omega_1,\omega_2$, je $\tfrac12$) — **keine** bei $\omega_M$
oder $\omega_\Delta$; das __Produkt__ $\cos\omega_M t\cos\omega_\Delta t$ hat vier Linien (bei
$\pm\omega_M\pm\omega_\Delta$, je $\tfrac14$). Dieselbe Identität ist rückwärts die __Amplitudenmodulation__
(Träger × Signal → __Seitenbänder__ $\omega_M\pm\omega_\Delta$).
:::

Schwebung und Produkt entstehen aus **nicht** harmonisch verwandten Frequenzen und ergeben kein periodisches
Linienraster. Sobald die Frequenzen eines Signals aber ganzzahlige Vielfache einer Grundfrequenz sind, wird das
Signal periodisch — und lässt sich vollständig in seine Harmonischen zerlegen: die __Fourier-Reihe__, das nächste
Thema.

:::quiz
F: Warum rechnet man mit Mitten- und Differenzfrequenz statt direkt mit $\omega_1,\omega_2$?
A: Die Zerlegung $\omega_M=\tfrac12(\omega_1+\omega_2)$ (groß) und $\omega_\Delta=\tfrac12(\omega_2-\omega_1)$ (klein) trennt die schnelle Trägerschwingung sauber vom langsamen Auf- und Abschwellen. In diesen Größen wird die Doppelnatur „ein schneller Ton, langsam pulsierend" direkt sichtbar.
F: Wie zeigt die Eulersche Formel, dass $\cos\omega_1 t+\cos\omega_2 t=2\cos\omega_\Delta t\cos\omega_M t$ ist?
A: Man schreibt das Produkt der beiden Kosinus als Produkt zweier Klammern $\tfrac12(e^{j\cdot}+e^{-j\cdot})$, multipliziert aus und erhält vier Exponentialterme mit Exponenten $\pm(\omega_M\pm\omega_\Delta)$. Da $\omega_M\pm\omega_\Delta=\omega_2,\omega_1$, fassen sich je zwei zu einem Kosinus zusammen — die Summenformel entsteht.
F: Warum hört man bei zwei dicht benachbarten Tönen nur einen pulsierenden Ton statt zwei?
A: Rechts der Identität steht ein schneller Träger $\cos\omega_M t$ mit einer langsam schwellenden Hüllkurve $2\cos\omega_\Delta t$. Das Ohr nimmt eine mittlere Tonhöhe $\omega_M$ wahr, deren Lautstärke langsam an- und abschwillt — das ist die Schwebung.
F: Warum ist die hörbare Schwebungsfrequenz doppelt so hoch wie die der Hüllkurve?
A: Die Lautstärke hängt vom Betrag der Hüllkurve ab; ob $2\cos\omega_\Delta t$ gerade $+$ oder $-$ ist, klingt gleich laut. Pro voller Hüllkurven-Periode gibt es daher zwei Lautstärkemaxima, also $\omega_\text{Schwebung}=2\omega_\Delta=\omega_2-\omega_1$.
F: Warum hat das Summensignal keine Spektrallinie bei der Mittenfrequenz $\omega_M$ oder der Pulsationsfrequenz?
A: Die Summe ist schlicht $\cos\omega_1 t+\cos\omega_2 t$, also stehen nur Linien bei $\omega_1$ und $\omega_2$. $\omega_M$ und $\omega_\Delta$ sind nur Rechen- bzw. Wahrnehmungsgrößen — die Schwebung ist keine eigene Frequenz, sondern die gemeinsame Wahrnehmung zweier dichter Linien.
F: Wie unterscheiden sich die Spektren von Summe und Produkt?
A: Die Summe $\cos\omega_1 t+\cos\omega_2 t$ hat zwei Linien (bei $\omega_1,\omega_2$, Höhe $\tfrac12$). Das Produkt $\cos\omega_M t\cos\omega_\Delta t$ ist gleich $\tfrac12\cos\omega_1 t+\tfrac12\cos\omega_2 t$, hat also vier Linien (bei $\pm\omega_M\pm\omega_\Delta$, Höhe $\tfrac14$) — und ebenfalls keine bei den Faktorfrequenzen selbst.
F: Warum erzeugt das Produkt zweier Sinus nur Summen- und Differenzfrequenz, nicht die Faktoren?
A: Beim Ausmultiplizieren addieren sich die Exponenten der komplexen Exponentialterme, sodass nur $\omega_M+\omega_\Delta$ und $\omega_M-\omega_\Delta$ auftreten. Die Faktorfrequenzen $\omega_M$ und $\omega_\Delta$ selbst erscheinen nie — Multiplikation verschiebt Frequenzen, erzeugt sie nicht einzeln.
F: Was bedeutet die Schwebung praktisch für das Stimmen eines Instruments?
A: Je näher die beiden Frequenzen, desto kleiner $\omega_2-\omega_1$ und desto langsamer das Pulsieren. Verschwindet die Schwebung ganz, sind beide Töne exakt gleich — Klavierstimmer nutzen das als direktes, hörbares Nullabgleich-Kriterium.
F: Wie liefert dieselbe Identität die Amplitudenmodulation?
A: Rückwärts gelesen: Multipliziert man einen hochfrequenten Träger $\cos\omega_M t$ mit einem langsamen Signal, verschiebt das dessen Spektrum an den Träger — es entstehen Seitenbänder bei $\omega_M\pm\omega_\Delta$. So wird ein niederfrequentes Signal sendefähig „aufgeprägt".
F: Warum trägt bei der AM der Träger $\omega_M$ allein keine Information?
A: Wie beim reinen Produkt gezeigt, steht bei $\omega_M$ selbst keine Linie — die gesamte Information steckt in den Seitenbändern $\omega_M\pm\omega_\Delta$. Der Träger ist nur die „Transportfrequenz", die Botschaft reist in den Seitenbändern.
:::
