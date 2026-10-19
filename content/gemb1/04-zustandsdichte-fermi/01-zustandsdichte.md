---
title: Die Zustandsdichte
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Zustandsdichte und Fermi-Verteilung
order: 4040100
summary: Wie viele elektronische Plätze es pro Energie überhaupt gibt – die Zustandsdichte $D(E)$. Sie folgt allein aus der Bandstruktur, indem man die im k-Raum gleichmäßig verteilten Zustände nach Energie sortiert. Für ein parabolisches Band in 3D ergibt sich der Wurzelverlauf $D(E)\propto\sqrt{E-E_L}$ – und je nach Dimension (1D, 2D, 3D, 0D) sieht die Zustandsdichte völlig anders aus.
tags: Zustandsdichte, density of states, k-Raum, parabolisches Band, Dimensionsabhängigkeit, van-Hove-Singularität, effektive Masse
---

:::grafik
Einstiegs-Animation: Links ein $k$-Raum, in dem die erlaubten Zustände als regelmäßiges Punktgitter sitzen
(Abstand $2\pi/L$). Eine Kugel mit Radius $k$ wächst; eine dünne Kugelschale $[k, k+dk]$ leuchtet auf — alle
Zustände auf ihr haben dieselbe Energie. Rechts baut sich daraus die Kurve $D(E)$ auf: ein von der Bandkante
wurzelförmig ansteigender Verlauf. Darunter wechselt die Form je nach Dimension: 3D Wurzel, 2D Treppe, 1D Spitzen,
0D einzelne Linien. Kernbotschaft: Die Zustandsdichte zählt dieselben Zustände wie die Bandstruktur, nur sortiert
nach Energie.
:::

:::konzept
Die Bandstruktur $E(\vec k)$ ordnet jedem Wellenvektor $\vec k$ eine Energie zu. Um aber auszurechnen, **wie viele
bewegliche Ladungsträger** ein Halbleiter enthält, interessiert uns nicht der einzelne $\vec k$-Zustand, sondern:
**Wie viele Zustände liegen in einem kleinen Energiefenster?** Denn die Besetzung (nächster Artikel) hängt von der
**Energie** ab. Diese Abzählung leistet die __Zustandsdichte__ $D(E)$ — „Plätze pro Energie und Volumen". Sie ist
keine neue Physik, sondern eine **Umbuchführung**: Wir zählen dieselben Zustände, nur nach Energie statt nach
$\vec k$ sortiert. Das ist der erste von zwei Bausteinen für die Ladungsträgerdichte $n=\int D(E)\,f(E)\,dE$.
:::

**Worum es geht:** Wir leiten her, dass die Zustände im $k$-Raum ein gleichmäßiges Raster bilden, zählen sie in
einer Energieschale ab und erhalten so für ein parabolisches Band in 3D den Wurzelverlauf
$D(E)\propto\sqrt{E-E_L}$. Anschließend sehen wir, *warum* die Form in 1D, 2D und 0D ganz anders aussieht.

## Zustände sitzen im k-Raum auf einem gleichmäßigen Raster

Löst man die Schrödinger-Gleichung in einem endlichen Kristall der Kantenlänge $L$ mit **periodischen
Randbedingungen** (__Born-von-Karman-Randbedingungen__: die Wellenfunktion wiederholt sich nach einer
Kristalllänge, $\psi(x+L)=\psi(x)$), sind die erlaubten Wellenzahlen **diskret und äquidistant**. Diese
periodischen Randbedingungen sind für einen ausgedehnten Kristall die realistische Wahl — sie liefern laufende
Wellen $e^{ikx}$ mit dem Rasterabstand $2\pi/L$ (gegenüber $\pi/L$ bei den harten Wänden des Potentialkastens,
die stehende Wellen erzwingen); für das Abzählen der Zustände ist nur der Rasterabstand entscheidend:

$$e^{ik_x(x+L)} = e^{ik_x x} \;\Longrightarrow\; k_x = \frac{2\pi}{L}\,n_x, \quad n_x \in \mathbb{Z}.$$

Der Abstand benachbarter erlaubter $k$-Werte ist also $\Delta k = 2\pi/L$ in jeder Richtung. Jeder Zustand
„belegt" damit im $k$-Raum ein kleines Kästchen vom Volumen

$$\Delta^3 k = \left(\frac{2\pi}{L}\right)^3 = \frac{(2\pi)^3}{V}.$$

- __$L$__: Kantenlänge des Kristalls, __$V=L^3$__: sein Volumen.
- __$\Delta k = 2\pi/L$__: Je größer der Kristall, desto **feiner** das Raster — bei realen Kristallen
  ($L \sim$ mm) liegen die Zustände praktisch kontinuierlich.

Weil das Raster so fein ist, wird aus der Summe über Zustände ein **Integral** über den $k$-Raum (mit einem
Faktor 2 für den Spin, da jeder $\vec k$-Zustand zwei Elektronen fasst):

$$\frac{1}{V}\sum_{\vec k} \;\longrightarrow\; \frac{2}{(2\pi)^3}\int d^3k.$$

:::grafik
Ein 2D-Ausschnitt des $k$-Rasters: Punkte (Zustände) im gleichmäßigen Abstand $2\pi/L$, jeder umrahmt von seinem
Kästchen der Fläche $(2\pi/L)^2$. Hinweis „großer Kristall → feines Raster → Summe wird Integral".
:::

## Abzählen in der Energieschale (3D, parabolisches Band)

Nahe einer Bandkante ist das Band parabolisch: $E - E_L = \hbar^2 k^2/(2m^\star)$ (mit der effektiven Masse aus dem
Bandstruktur-Oberthema). Die Zustände **gleicher Energie** liegen dann auf einer **Kugel** im $k$-Raum. Wir zählen
in drei Schritten.

__Schritt 1__ — Zustände bis zum Betrag $k$ (Kugelvolumen / Rasterkästchen, mal Spin 2), pro Volumen:

$$\frac{N(k)}{V} = \frac{2}{(2\pi/L)^3}\cdot\frac{4}{3}\pi k^3 \cdot \frac{1}{V} = \frac{k^3}{3\pi^2}.$$

__Schritt 2__ — Ableiten nach $k$ gibt die Zustände in der Kugelschale $[k, k+dk]$:

$$\frac{1}{V}\frac{dN}{dk} = \frac{k^2}{\pi^2}.$$

Das ist im Kern die **Oberfläche der $k$-Kugel** ($\propto k^2$), auf der alle Zustände gleicher Energie sitzen.

__Schritt 3__ — Von $dk$ auf $dE$ umrechnen über die Bandbeziehung:

$$k = \frac{\sqrt{2m^\star(E-E_L)}}{\hbar}, \qquad \frac{dk}{dE} = \frac{\sqrt{2m^\star}}{2\hbar\sqrt{E-E_L}}.$$

:::grafik
Drei Panels: (1) gefüllte $k$-Kugel mit Radius $k$ („alle Zustände bis $k$"), (2) dünne Kugelschale $[k,k+dk]$
(„Zustände dieser Energie", $\propto k^2$), (3) die Parabel $E-E_L=\hbar^2k^2/2m^\star$ mit markiertem $dk \to dE$.
:::

Zusammensetzen ($D(E) = \tfrac1V\tfrac{dN}{dk}\cdot\tfrac{dk}{dE}$, mit $k^2 = 2m^\star(E-E_L)/\hbar^2$) ergibt die
__Zustandsdichte des Leitungsbandes__:

$$D(E) = \frac{(2m^\star)^{3/2}}{2\pi^2\hbar^3}\sqrt{E-E_L} = \frac{4\pi\,(2m^\star)^{3/2}}{h^3}\sqrt{E-E_L}, \qquad E \ge E_L.$$

Für das **Valenzband** gilt dasselbe gespiegelt — die Zustände füllen den Bereich **unterhalb** der Kante $E_V$,
also steht dort $\sqrt{E_V - E}$.

:::grafik
Die Kurve $D(E) = \tfrac{4\pi(2m^\star)^{3/2}}{h^3}\sqrt{E-E_L}$ über $E$: startet bei null an der Bandkante $E_L$
und steigt wurzelförmig an. Gespiegelt darunter die Valenzband-Zustandsdichte $\propto\sqrt{E_V-E}$, die von $E_V$
nach unten ansteigt. Dazwischen die leere Bandlücke.
:::

## Warum ausgerechnet ein Wurzelverlauf?

Der $\sqrt{E}$-Verlauf ist **keine Rechenzufälligkeit, sondern Geometrie** des $k$-Raums. Er entsteht aus zwei
gegenläufigen Effekten:

- **Größe der Energieschale** (Schritt 2): In $d$ Dimensionen wächst die „Fläche" gleicher Energie wie
  $k^{\,d-1}$ — in 3D die Kugeloberfläche $\propto k^2$.
- **Umrechnung $dk/dE$** (Schritt 3): Bei parabolischem Band immer $\propto 1/\sqrt{E}$.

In 3D überwiegt das Wachstum der Kugeloberfläche ($k^2 \propto E$) den absenkenden Faktor $1/\sqrt{E}$ — netto
bleibt $\sqrt{E}$. Deshalb gibt es an der Bandkante zunächst **wenige** Zustände ($D\to 0$), und ihre Zahl wächst
nach oben wurzelförmig.

## Dieselbe Rechnung in 1D, 2D, 0D

Macht man die Abzählung in anderer Dimension, ändert sich nur der Schalen-Faktor $k^{\,d-1}$ — und das Ergebnis
sieht völlig anders aus. Das ist der tiefe Grund, warum niederdimensionale Strukturen (aus dem Quantenpunkt-
Artikel) so andere Eigenschaften haben:

| Dimension | Schale $\propto$ | $D(E)\propto$ | Charakter |
|---|---|---|---|
| **1D** (Draht) | $k^0$ | $(E-E_L)^{-1/2}$ | **divergiert** an der Kante (van-Hove-Spitze) |
| **2D** (Film) | $k^1$ | const | **Treppenstufe**, energieunabhängig |
| **3D** (Volumen) | $k^2$ | $(E-E_L)^{+1/2}$ | **Wurzel**, startet bei 0 |
| **0D** (Punkt) | — | $\delta$-Linien | **einzelne scharfe Niveaus** (wie im Atom) |

:::grafik
Vier kleine $D(E)$-Diagramme nebeneinander: 1D (Kurve mit scharfer Spitze an der Kante), 2D (waagerechte Treppe),
3D (ansteigende Wurzel), 0D (einzelne senkrechte Striche). Beschriftet „Draht / Film / Volumen / Punkt".
:::

## Nachtrag: die DOS-effektive Masse bei Silizium

In der Formel steckt eine effektive Masse $m^\star$. Bei einem einfachen, kugelförmigen Band ist das genau die
Krümmungsmasse. **Silizium** hat aber sechs gleichwertige, ellipsoide Täler (aus dem Bandstruktur-Oberthema), mit
longitudinaler Masse $m_l^\star \approx 0{,}92\,m_0$ und transversaler $m_t^\star \approx 0{,}19\,m_0$. Damit man
trotzdem die *eine* einfache Wurzelformel benutzen kann, bündelt man alle sechs Täler zu **einer**
__DOS-effektiven Masse__

$$m_{\text{DOS}}^\star = 6^{2/3}\,\big((m_t^\star)^2\,m_l^\star\big)^{1/3}.$$

Der Faktor $6^{2/3}$ fasst die sechs Täler zusammen, das geometrische Mittel mittelt die Anisotropie. Diese
„Buchhaltungsmasse" sorgt dafür, dass die einfache Kugelformel dieselbe Gesamtzahl an Zuständen liefert wie die
tatsächlichen Ellipsoide.

:::grafik
Links die sechs ellipsoiden Si-Täler entlang $\langle100\rangle$; ein Pfeil bündelt sie zu einer einzigen
kugelförmigen „Ersatz-Dichte" mit Masse $m_{\text{DOS}}^\star$ rechts, die dieselbe $\sqrt{E}$-Zustandsdichte
erzeugt.
:::

:::kern
Die __Zustandsdichte__ $D(E)$ zählt die elektronischen Plätze pro Energie und Volumen — dieselben Zustände wie
$E(\vec k)$, nur nach Energie sortiert. Im $k$-Raum sitzen die Zustände auf einem Raster mit Abstand $2\pi/L$, die
Summe wird zum Integral $\tfrac{2}{(2\pi)^3}\int d^3k$ (Faktor 2 = Spin). Für ein parabolisches 3D-Band:
$D(E)=\tfrac{4\pi(2m^\star)^{3/2}}{h^3}\sqrt{E-E_L}$ (Valenzband: $\sqrt{E_V-E}$). Der **Wurzelverlauf** kommt aus
Kugeloberfläche $\propto k^2\propto E$ mal Umrechnung $dk/dE\propto1/\sqrt{E}$. Je Dimension anders: **1D**
$\propto(E-E_L)^{-1/2}$ (Divergenz), **2D** konstant (Treppe), **3D** $\sqrt{E}$, **0D** einzelne Linien. Bei
Silizium fasst die __DOS-effektive Masse__ $m_{\text{DOS}}^\star=6^{2/3}((m_t^\star)^2 m_l^\star)^{1/3}$ die sechs
Täler zusammen.
:::

$D(E)$ sagt uns, **wo** Plätze sind. Offen bleibt, **welche** davon besetzt sind. Das beantwortet die
__Fermi-Dirac-Verteilung__ — die Wahrscheinlichkeit, dass ein Zustand bei gegebener Temperatur besetzt ist — das
Thema des nächsten Artikels.

:::quiz
F: Was zählt die Zustandsdichte $D(E)$, und warum ist sie „keine neue Physik"?
A: Sie gibt die Zahl elektronischer Plätze pro Energie und Volumen an — dieselben Zustände wie die Bandstruktur $E(\vec k)$, nur nach Energie statt nach $\vec k$ sortiert. Es ist eine reine Umbuchführung, die man für die Ladungsträgerdichte $n=\int D(E)f(E)\,dE$ braucht.
F: Warum sitzen die erlaubten $k$-Zustände auf einem gleichmäßigen Raster mit Abstand $2\pi/L$?
A: Die periodischen Born-von-Karman-Randbedingungen $\psi(x+L)=\psi(x)$ erzwingen $e^{ik_xL}=1$, also $k_x=\frac{2\pi}{L}n_x$. Damit sind die erlaubten Wellenzahlen diskret und äquidistant mit Abstand $2\pi/L$.
F: Warum darf man die Summe über Zustände durch ein Integral ersetzen?
A: Bei realen Kristallen ($L\sim$ mm) ist der Rasterabstand $2\pi/L$ winzig, die Zustände liegen praktisch kontinuierlich. Dann wird aus $\frac1V\sum_{\vec k}$ das Integral $\frac{2}{(2\pi)^3}\int d^3k$, mit dem Faktor 2 für den Spin.
F: Warum liegen Zustände gleicher Energie in 3D auf einer Kugel im $k$-Raum?
A: Nahe der Bandkante ist $E-E_L=\hbar^2k^2/2m^\star$, die Energie hängt also nur vom Betrag $k$ ab, nicht von der Richtung. Alle $\vec k$ mit gleichem $|k|$ — und damit gleicher Energie — bilden eine Kugelfläche.
F: Warum ist die Zahl der Zustände in einer Energieschale proportional zu $k^2$?
A: Die Zustände einer Energie sitzen auf der Kugeloberfläche im $k$-Raum, und deren Fläche wächst wie $k^2$. Die dünne Schale $[k,k+dk]$ enthält daher $\propto k^2\,dk$ Zustände.
F: Woher kommt der Wurzelverlauf $D(E)\propto\sqrt{E-E_L}$ in 3D?
A: Aus zwei Faktoren: die Kugeloberfläche $\propto k^2\propto E$ (wächst) und die Umrechnung $dk/dE\propto1/\sqrt{E}$ (fällt). In 3D überwiegt das Flächenwachstum, netto bleibt $\sqrt{E}$ — an der Kante gibt es wenige Zustände, nach oben wurzelförmig mehr.
F: Warum verschwindet die Zustandsdichte an der Bandkante?
A: An der Kante ist $k=0$, die Energieschale schrumpft auf einen Punkt (Kugeloberfläche $\to0$). Daher gibt es dort praktisch keine Zustände, $D(E_L)=0$; erst mit wachsender Energie öffnet sich die Kugel und $D$ steigt an.
F: Warum sieht die Zustandsdichte in 1D, 2D und 3D so unterschiedlich aus?
A: Es ändert sich nur der Schalen-Faktor $k^{d-1}$: 1D $\propto k^0$ (→ $D\propto(E-E_L)^{-1/2}$, Divergenz an der Kante), 2D $\propto k^1$ (→ konstant, Treppe), 3D $\propto k^2$ (→ Wurzel). Deshalb haben niederdimensionale Strukturen völlig andere elektronische Eigenschaften.
F: Warum besteht die Zustandsdichte eines Quantenpunkts (0D) aus einzelnen Linien?
A: In 0D ist das Elektron in allen Richtungen eingesperrt, es gibt keine freie Bewegung und damit kein kontinuierliches Band — nur diskrete Energieniveaus wie im Atom. Diese erscheinen als scharfe $\delta$-Linien in $D(E)$.
F: Wozu dient die DOS-effektive Masse $m_{\text{DOS}}^\star$ bei Silizium?
A: Silizium hat sechs ellipsoide Täler statt einer Kugel; die DOS-effektive Masse $6^{2/3}((m_t^\star)^2 m_l^\star)^{1/3}$ bündelt alle sechs (Faktor $6^{2/3}$) und mittelt die Anisotropie (geometrisches Mittel). So liefert die einfache Kugel-Wurzelformel dieselbe Gesamtzahl an Zuständen wie die echten Ellipsoide.
:::
