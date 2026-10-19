---
title: Diffusion und die Einstein-Relation
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Halbleiter und Ladungstransport
order: 4050400
summary: Die zweite Triebkraft für Strom neben dem elektrischen Feld – ein Konzentrationsgefälle. Aus der zufälligen Wärmebewegung entsteht ein Diffusionsstrom $j=-eD\,\mathrm{d}n/\mathrm{d}x$. Weil Drift und Diffusion aus derselben Streuzeit stammen, verknüpft sie die Einstein-Beziehung $D=\tfrac{k_BT}{e}\mu$. Und die Beweglichkeit selbst durchläuft mit der Temperatur ein Maximum.
tags: Diffusion, Einstein-Relation, Beweglichkeit, Boltzmann-Transportgleichung, Relaxationszeit, Matthiessen-Regel, Streuung, 2DEG
---

:::grafik
Einstiegs-Animation: Links viele Teilchen dicht gedrängt, rechts wenige. Jedes macht eine zufällige
Wärmebewegung (Zitterpfeile in alle Richtungen) — doch weil links mehr sind, überqueren **netto** mehr die
Mittellinie nach rechts als umgekehrt. Es entsteht ein gerichteter __Diffusionsstrom__, ganz ohne Kraft. Rechts
daneben die Kurve der __Beweglichkeit__ $\mu(T)$: Sie steigt bei tiefer Temperatur (Störstellenstreuung), fällt
bei hoher (Phononenstreuung) und hat dazwischen ein **Maximum**. Kernbotschaft: Auch ein reines
Konzentrationsgefälle treibt einen Strom — und er ist eng mit dem Drift verwandt.
:::

:::konzept
Im vorigen Artikel trieb das **elektrische Feld** die Ladungsträger (Drift). Es gibt aber eine zweite, rein
**statistische** Triebkraft: ein **Konzentrationsgefälle**. Wo viele Ladungsträger sind, wandern durch die
zufällige Wärmebewegung netto mehr weg als zu — die __Diffusion__. In Halbleiter-Bauelementen (etwa am
pn-Übergang) ist Diffusion genauso wichtig wie Drift. Das Schöne: Beide entspringen **derselben** mikroskopischen
Ursache, der Streuung — und deshalb sind sie durch eine überraschend einfache Beziehung verknüpft, die
__Einstein-Relation__. Zum Abschluss klärt sich, warum die Beweglichkeit mit der Temperatur ein Maximum
durchläuft.
:::

**Worum es geht:** Wir führen den __Diffusionsstrom__ ein, skizzieren die __Boltzmann-Transportgleichung__ als
gemeinsame Quelle von Drift und Diffusion, leiten die __Einstein-Beziehung__ $D=\tfrac{k_BT}{e}\mu$ her und
verstehen die Temperaturabhängigkeit der __Beweglichkeit__.

## Diffusion: Strom ganz ohne Kraft

Teilchen in Wärmebewegung laufen zufällig in alle Richtungen (ein „Random Walk"). Sitzt auf der einen Seite einer
gedachten Grenze eine höhere Konzentration als auf der anderen, überqueren von der dichten Seite **mehr** Teilchen
die Grenze als von der dünnen zurück — einfach, weil es dort mehr Kandidaten gibt. Netto fließt ein Strom von hoch
nach niedrig, ohne dass eine Kraft wirkt. Das ist der __Diffusionsstrom__, quantitativ das **Ficksche Gesetz**:

$$j_{\text{diff}} = -e\,D\,\frac{dn}{dx}.$$

- __$D$__: die __Diffusionskonstante__ — wie leicht sich die Ladungsträger ausbreiten.
- __$dn/dx$__: das Konzentrationsgefälle; das Minuszeichen sagt: der Teilchenfluss läuft **abwärts** (von hoher zu
  niedriger Dichte). Der Faktor $-e$ macht daraus den elektrischen Strom.

:::grafik
Ein Dichteprofil $n(x)$, das von links (hoch) nach rechts (niedrig) abfällt; darunter der konstante
Teilchenfluss-Pfeil „bergab". Daneben die Formel $j_{\text{diff}}=-eD\,dn/dx$ mit markiertem Gefälle $dn/dx$.
:::

## Die gemeinsame Wurzel: die Boltzmann-Transportgleichung

Drift und Diffusion sehen verschieden aus, stammen aber aus **einer** Gleichung. Man beschreibt die Elektronen
semiklassisch durch die __Verteilungsfunktion__ $f(x,k,t)$ (Wahrscheinlichkeit, ein Teilchen am Ort $x$ mit
Wellenzahl $k$ zur Zeit $t$ zu finden). Ihre Bewegung samt Streuung ist die __Boltzmann-Transportgleichung__ in der
__Relaxationszeitnäherung__:

$$\frac{\partial f}{\partial t} + v\,\frac{\partial f}{\partial x} + \frac{F}{\hbar}\,\frac{\partial f}{\partial k} = -\frac{f - f^0}{\tau}.$$

- Der Term $v\,\tfrac{\partial f}{\partial x}$ (Ortsabhängigkeit) erzeugt die **Diffusion**.
- Der Term $\tfrac{F}{\hbar}\tfrac{\partial f}{\partial k}$ (Kraft) erzeugt den **Drift**.
- Die rechte Seite ist die __Relaxationszeitnäherung__: Jede Abweichung $f-f^0$ vom Gleichgewicht $f^0$ klingt mit
  der __Streuzeit__ $\tau$ exponentiell ab, $\delta f(t)=\delta f(0)\,e^{-t/\tau}$.

Beide Transportarten werden also von **derselben** Streuzeit $\tau$ gedämpft — das ist der Schlüssel zur
Einstein-Relation.

:::grafik
Die Boltzmann-Gleichung mit drei farbig markierten Termen: „$\partial f/\partial t$ zeitlich", „$v\,\partial
f/\partial x$ → Diffusion", „$\tfrac{F}{\hbar}\partial f/\partial k$ → Drift", rechts der Streuterm
„$-(f-f^0)/\tau$". Darunter die abklingende Kurve $\delta f(t)=\delta f(0)e^{-t/\tau}$.
:::

**Matthiessen-Regel.** Wirken mehrere **unabhängige** Streumechanismen gleichzeitig, addieren sich ihre
**Raten** (nicht die Zeiten), weil jeder Prozess pro Zeiteinheit eigenständig einen Stoß beisteuert:

$$\frac{1}{\tau} = \frac{1}{\tau_{\text{Phonon}}} + \frac{1}{\tau_{\text{Störstelle}}} + \frac{1}{\tau_{\text{Defekt}}} + \dots$$

Konsequenz: Der **schnellste** Mechanismus (kürzestes $\tau$) dominiert die Beweglichkeit.

## Die Einstein-Relation

Jetzt der elegante Zusammenhang. Wertet man die Boltzmann-Gleichung einmal für den **reinen Feldfall** (Drift) und
einmal für den **reinen Gradientenfall** (Diffusion) aus, erhält man:

- Drift: $\;\mu = \dfrac{e\,\tau}{m^\star}\;$ (aus dem vorigen Artikel),
- Diffusion: $\;D = \dfrac{k_B T\,\tau}{m^\star}\;$ (dieselbe Streuzeit $\tau$, dieselbe Masse $m^\star$).

Beide enthalten den **identischen** Faktor $\tau/m^\star$. Teilt man sie, fällt er heraus, und es bleibt die
__Einstein-Beziehung__:

$$\boxed{\;D = \frac{k_B T}{e}\,\mu\;}$$

Das ist tiefgründig: Die **Zufallsbewegung** (Diffusion $D$) und die **Reaktion auf eine Kraft** (Beweglichkeit
$\mu$) sind nicht unabhängig, sondern über die Temperatur fest gekoppelt — beide gehen auf dieselben Stöße zurück
(ein Beispiel für das allgemeine Fluktuations-Dissipations-Prinzip). Kennt man $\mu$, kennt man $D$.

:::grafik
Zwei Kästchen „Drift: $\mu=e\tau/m^\star$" und „Diffusion: $D=k_BT\tau/m^\star$", verbunden durch einen Pfeil
„gleiches $\tau/m^\star$", der zum gerahmten Ergebnis $D=\tfrac{k_BT}{e}\mu$ führt. Darunter „gleiche Streuung →
feste Kopplung".
:::

## Warum die Beweglichkeit ein Maximum hat

Die Temperaturabhängigkeit steckt in $\tau(T)=\lambda(T)/v_{\text{th}}(T)$ (mittlere freie Weglänge $\lambda$ pro
thermischer Geschwindigkeit $v_{\text{th}}$). Zwei Mechanismen wirken gegenläufig:

- **Phononenstreuung** (dominiert bei **hoher** Temperatur): Die Zahl der Gitterschwingungen wächst $\propto T$,
  also $\lambda\propto 1/T$; mit $v_{\text{th}}\propto T^{1/2}$ (aus $\tfrac{m^\star}{2}v_{\text{th}}^2=\tfrac32
  k_BT$) folgt $\tau\propto T^{-3/2}$, also
  $$\mu_{\text{Phonon}} \propto T^{-3/2}.$$
- **Streuung an ionisierten Störstellen** (dominiert bei **tiefer** Temperatur): Schnellere Elektronen entkommen
  dem Coulomb-Potential der Dotier-Ionen leichter, daher
  $$\mu_{\text{Störstelle}} \propto T^{+3/2}.$$

Über die Matthiessen-Regel ($1/\tau$ addiert) ergibt sich ein **Maximum** der Beweglichkeit bei mittlerer
Temperatur: tiefe $T$ von der Störstellenstreuung begrenzt, hohe $T$ von der Phononenstreuung.

:::grafik
Doppelt-logarithmischer Plot $\mu$ über $T$: eine ansteigende Gerade $\propto T^{+3/2}$ (Störstellen, tiefe $T$),
eine abfallende $\propto T^{-3/2}$ (Phononen, hohe $T$), ihre Matthiessen-Überlagerung als Kurve mit deutlichem
Maximum dazwischen.
:::

**Wie macht man die Beweglichkeit groß?** Nach $\mu=e\tau/m^\star$ gibt es zwei Wege: $\tau$ vergrößern (seltener
streuen) oder $m^\star$ verkleinern. Beides nutzt das __2DEG__ (zweidimensionales Elektronengas) in
III-V-Heterostrukturen: Durch __$\delta$-Dotierung__ werden die Dotier-Ionen in eine dünne Schicht gelegt, die
vom leitenden Kanal **räumlich getrennt** ist. Die beweglichen Elektronen sind dann weit von ihren Streuzentren
entfernt → sehr hohe Beweglichkeit (Grundlage der schnellsten Transistoren, HEMTs).

:::grafik
Schichtstruktur: eine dünne $\delta$-dotierte Lage (ortsfeste Ionen) räumlich getrennt von einem Kanal, in dem
die Elektronen (2DEG) laufen; ein Abstandspfeil zeigt die Trennung, Beschriftung „Streuzentren fern vom Kanal →
großes $\tau$ → hohe $\mu$".
:::

**Die treibenden Kräfte zusammengefasst:** Strom fließt, wenn das __Fermi-Niveau__ (genauer: das
elektrochemische Potential, chemischer „Konzentrationsdruck" plus elektrostatische Energie) oder die
**Temperatur** einen Gradienten hat. Der Fermi-Niveau-Gradient vereint Drift (elektrisches Feld) und Diffusion
(Konzentration) in einer Größe — im Gleichgewicht ist er null, und es fließt kein Strom.

:::kern
Neben dem Drift treibt ein **Konzentrationsgefälle** einen __Diffusionsstrom__ $j_{\text{diff}}=-eD\,dn/dx$
(Ficksches Gesetz, rein statistisch). Drift und Diffusion folgen beide aus der __Boltzmann-Transportgleichung__
$\partial_t f+v\partial_x f+\tfrac{F}{\hbar}\partial_k f=-(f-f^0)/\tau$ (Relaxationszeitnäherung, $\delta f\propto
e^{-t/\tau}$; Matthiessen $1/\tau=\sum_i 1/\tau_i$). Weil beide dieselbe Streuzeit teilen ($\mu=e\tau/m^\star$,
$D=k_BT\tau/m^\star$), gilt die __Einstein-Beziehung__ $D=\tfrac{k_BT}{e}\mu$. Die Beweglichkeit $\mu(T)$ hat ein
**Maximum**: $\mu\propto T^{-3/2}$ (Phononen, hohe $T$), $\mu\propto T^{+3/2}$ (ionisierte Störstellen, tiefe $T$).
Sehr hohe $\mu$ im __2DEG__ durch $\delta$-Dotierung (Streuzentren räumlich vom Kanal getrennt). Treibende Kräfte:
Gradient von Fermi-Niveau und Temperatur.
:::

Wir haben jetzt alle Bausteine: Ladungsträgerdichte, Drift, Diffusion und ihre Kopplung. Im letzten Artikel
dieses Oberthemas schalten wir sie zu den __Grundgleichungen des Halbleiters__ zusammen — Kontinuität,
Drift-Diffusion und Poisson —, mit denen sich jedes Bauelement berechnen lässt.
