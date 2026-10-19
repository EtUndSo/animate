---
title: Der MOSFET
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Bauelemente
order: 4060400
summary: Das wichtigste Bauelement der Elektronik – ein MOS-Kondensator mit zwei Kontakten. Die Gatespannung schaltet berührungslos einen leitenden Inversionskanal zwischen Source und Drain ein. Aus der Gradual-Channel-Näherung folgt die Kennlinie $I=W\tfrac{\mu}{L}C_{ox}(V_{ds}(V_{gs}-V_{th})-\tfrac{V_{ds}^2}{2})$ mit linearem und Sättigungsbereich – und die berühmte 60-mV/Dekade-Grenze des Schaltens.
tags: MOSFET, Transistor, Inversionskanal, Gradual-Channel-Näherung, Sättigung, pinch-off, Schwellenspannung, Unterschwellensteigung
---

:::grafik
Einstiegs-Animation: Ein MOSFET im Querschnitt — zwei stark n-dotierte Inseln (__Source__ links, __Drain__ rechts)
in einem p-Substrat, darüber ein isoliertes __Gate__ über dünnem Oxid. Dreht man die Gatespannung über die
Schwelle, erscheint unter dem Oxid ein dünner Elektronen-__Inversionskanal__, der Source und Drain verbindet — der
Transistor schaltet „ein". Legt man dann eine Drainspannung an, fließt Strom; bei großer Drainspannung wird der
Kanal am Drain-Ende **abgeschnürt** (pinch-off). Rechts bauen sich die Kennlinien auf: die Ausgangskennlinienschar
$I_D(V_{ds})$ und die Transferkennlinie $I_D(V_{gs})$. Kernbotschaft: Eine Spannung am isolierten Gate steuert
berührungslos einen Stromkanal — der Grundbaustein aller Logik.
:::

:::konzept
Der __MOSFET__ (Metall-Oxid-Halbleiter-Feldeffekt-Transistor) ist im Kern der __MOS-Kondensator__ aus dem vorigen
Artikel, erweitert um **zwei Kontakte**. Seine Idee: Die Gatespannung erzeugt (oder entfernt) den
__Inversionskanal__ an der Oberfläche und schaltet damit einen leitenden Pfad zwischen __Source__ und __Drain__
ein oder aus. Entscheidend und elegant: Die steuernde Barriere wird **berührungslos** über das isolierte Gate
verschoben — anders als bei der Diode, wo man eine Spannung direkt ins p-Gebiet legen muss. Der MOSFET ist das
meistgefertigte Bauelement der Geschichte und der Grund, warum dieses ganze Modul — von der Quantenmechanik bis
hierher — überhaupt so wichtig ist.
:::

**Worum es geht:** Wir verstehen den Aufbau und den Schaltmechanismus, leiten mit der
__Gradual-Channel-Näherung__ die Strom-Spannungs-Kennlinie her (linearer und Sättigungsbereich), und klären, was
die __Schwellenspannung__ und die fundamentale __60-mV/Dekade-Grenze__ bestimmen.

## Aufbau und Schaltmechanismus

Ein (n-Kanal-)MOSFET besteht aus zwei stark n-dotierten Gebieten — __Source__ und __Drain__ ($n^{++}$) — in einem
p-dotierten Substrat, mit einem isolierten __Gate__ über dünnem Oxid dazwischen. Der Strom fließt (wenn er fließt)
im Kanal der Länge $L$ und Weite $W$ von Source zu Drain.

Der Source-Kanal-Übergang ist im Grunde ein pn-Übergang mit einer Potentialbarriere. Der **Unterschied zur Diode**:
Diese Barriere wird **nicht** durch eine Spannung am p-Gebiet verschoben, sondern durch die Spannung am
**isolierten Gate**. Überschreitet die Gatespannung die __Schwellenspannung__ $V_{th}$, entsteht (wie im
MOS-Artikel gezeigt) der n-leitende Inversionskanal — Source und Drain sind verbunden, der Transistor ist „an".
Darunter fehlt der Kanal, die Barriere blockiert — „aus".

:::grafik
MOSFET-Querschnitt: $n^{++}$-Source und -Drain im p-Substrat, Gate/Oxid darüber, Kanallänge $L$, Weite $W$
beschriftet. Zwei Zustände: ohne Kanal (Gate unter $V_{th}$, Barriere blockiert) und mit Inversionskanal (Gate
über $V_{th}$, durchgehender Elektronenpfad Source→Drain).
:::

## Transport: über den „Top of the Barrier"

Wie kommt der Strom zustande? Die Elektronen werden aus der Source per **Diffusion** in den Kanal injiziert, bis
zum höchsten Punkt der Barriere („Top of the Barrier"). Genau dort ist das Feld null — kein Drift. Jenseits des
Maximums, zum Drain hin, wird die Bewegung in einen **Driftstrom** umgewandelt. Im Gleichgewicht (keine
Drainspannung) ist der Strom null, weil $+k_x$ und $-k_x$ gleich besetzt sind; eine Drainspannung **entvölkert**
die $-k_x$-Hälfte, und es bleibt ein Nettostrom. Anders als bei der Diode spalten hier **keine** Quasi-Fermi-Niveaus
auf — das Gate verbiegt die Bänder rein elektrostatisch.

:::grafik
Energieprofil entlang des Kanals Source→Drain mit einer Barriere; am Scheitel („Top of the Barrier") ist das Feld
null. Pfeile: Diffusion hinauf, Drift hinab zum Drain. Zwei Besetzungs-Halbkreise ($+k_x$ voll, $-k_x$ durch die
Drainspannung entleert).
:::

## Die Kennlinie aus der Gradual-Channel-Näherung

Die __Gradual-Channel-Näherung__ nimmt an, dass sich das Potential **entlang** des Kanals nur langsam ändert — so
langsam, dass man an jedem Ort $x$ die MOS-Kapazität lokal als Plattenkondensator behandeln darf.

__Schritt 1 — Kanalladung.__ In starker Inversion ist die Flächenladung die eines Plattenkondensators, vermindert
um das lokale Kanalpotential $V(x)$ (es steigt von $0$ an der Source auf $V_{ds}$ am Drain):

$$Q(x) = C_{ox}\big(V_{gs} - V_{th} - V(x)\big).$$

__Schritt 2 — Stromgleichung.__ Wegen der Kontinuität ist der Strom an **jedem** Ort gleich groß; lokal ist es ein
Driftstrom $I = W\,\mu\,Q(x)\,\dfrac{dV}{dx}$.

__Schritt 3 — Integration von Source ($V=0$) bis Drain ($V=V_{ds}$).__ Da $I$ konstant ist:

$$I\!\cdot\!L = W\mu C_{ox}\!\int_0^{V_{ds}}\!\!\big(V_{gs}-V_{th}-V\big)\,dV \;\Longrightarrow\; I = W\frac{\mu}{L}C_{ox}\left(V_{ds}(V_{gs}-V_{th}) - \frac{V_{ds}^2}{2}\right).$$

:::grafik
Der Kanal mit ansteigendem Potential $V(x)$ von 0 (Source) auf $V_{ds}$ (Drain); die Kanalladung $Q(x)=C_{ox}
(V_{gs}-V_{th}-V(x))$ wird zum Drain hin dünner (keilförmige Ladungsschicht). Daneben die integrierte Kennlinie.
:::

## Die drei Betriebsbereiche

**1. Linearer (ohmscher) Bereich** ($V_{ds}\to 0$): Der quadratische Term ist vernachlässigbar, der Strom steigt
**linear** mit $V_{ds}$ — der Transistor wirkt als **spannungsgesteuerter Widerstand**:

$$I \approx W\frac{\mu}{L}C_{ox}\,V_{ds}\,(V_{gs}-V_{th}).$$

**2. Sättigung / pinch-off** ($V_{ds}\ge V_{sat}$): Erhöht man $V_{ds}$, wird die Kanalladung am Drain-Ende immer
dünner. Bei $V_{ds}=V_{sat}=V_{gs}-V_{th}$ verschwindet sie dort ganz — der Kanal ist am Drain **abgeschnürt**
(*pinch-off*). Einsetzen liefert den konstanten __Sättigungsstrom__:

$$I_{sat} = W\frac{\mu}{2L}C_{ox}\,(V_{gs}-V_{th})^2.$$

Für $V_{ds}>V_{sat}$ bleibt der Strom **konstant**: Der Scheitel der Barriere wird idealerweise nur vom Gate
bestimmt, nicht von weiter steigendem $V_{ds}$.

**3. Transferkennlinie** (Sättigung, über $V_{gs}$): Der Strom steigt **quadratisch** mit $(V_{gs}-V_{th})$ im
Anzustand; unterhalb $V_{th}$ ist der Auszustand.

:::grafik
Links die Ausgangskennlinienschar $I_D(V_{ds})$ für mehrere $V_{gs}$: erst linearer Anstieg, dann Abknicken in
ein waagerechtes Sättigungsplateau; die Abschnür-Grenze $V_{ds}=V_{gs}-V_{th}$ als gestrichelte Parabel. Rechts die
Transferkennlinie $I_D(V_{gs})$: null bis $V_{th}$, dann quadratischer Anstieg.
:::

## Was die Schwellenspannung einstellt

$V_{th}$ ist keine Naturkonstante des Siliziums, sondern über die **Materialwahl** einstellbar. Bringt man Metall
und Halbleiter in Kontakt, müssen sich die Bänder verbiegen, damit sich ein gemeinsames Fermi-Niveau einstellt.
Der Antrieb ist die **Austrittsarbeitsdifferenz** $\Phi_m - \chi_{si}$:

- __$\Phi_m$__: die __Austrittsarbeit__ des Gate-Metalls (Energie, ein Elektron ins Vakuum zu heben).
- __$\chi_{si}$__: die __Elektronenaffinität__ des Siliziums (Vakuumniveau → Leitungsband, $\chi_{si}=4{,}05\,$eV).

Hinzu kommt die **Dotierung des Substrats** (über das Bulk-Potential). Fazit: An der Schwellenspannung dreht der
Prozessingenieur über **Gate-Material** und **Substratdotierung** — die zwei zentralen Stellschrauben.

:::grafik
Energieniveau-Schema vor und nach dem Kontakt Metall–Oxid–Si mit eingezeichneter Austrittsarbeit $\Phi_m$ und
Elektronenaffinität $\chi_{si}=4{,}05\,$eV; die resultierende Bandverbiegung legt zusammen mit der Dotierung
$V_{th}$ fest.
:::

## Der Auszustand und die 60-mV/Dekade-Grenze

Auch **unterhalb** der Schwelle fließt ein kleiner Strom: Die Source-Kanal-Barriere ist endlich hoch, und über sie
diffundieren thermisch angeregte Elektronen — genau wie über die Diodenbarriere, also **exponentiell**. Wie
„effektiv" das Gate diese Barriere absenkt, misst die __inverse Unterschwellensteigung__ $S$: die Gatespannung, die
man braucht, um den Strom um **eine Dekade** (Faktor 10) zu ändern.

Nur ein Bruchteil der Gatespannung erreicht die Oberfläche — ein kapazitiver Spannungsteiler aus Oxid- und
Verarmungskapazität:

$$S = \frac{k_B T}{e}\,\ln(10)\cdot\frac{C_{ox}+C_{\text{depl}}}{C_{ox}}.$$

Im **Idealfall** perfekter Gate-Kontrolle ($C_{ox}\gg C_{\text{depl}}$) erreicht man die physikalische Untergrenze

$$S_{\min} = \frac{k_B T}{e}\,\ln(10) \approx 60\ \text{mV/Dekade} \quad(\text{bei Raumtemperatur}).$$

Das ist die berühmte __60-mV/Dekade-Grenze__: Weil der Strom über eine **thermisch** besetzte Barriere fließt
(Boltzmann-Faktor $\propto k_B T$), kann ein klassischer MOSFET bei Raumtemperatur nicht steiler schalten. Diese
Grenze bestimmt, wie weit man die Versorgungsspannung — und damit die Verlustleistung — senken kann, und ist der
zentrale Engpass bei der weiteren Verkleinerung der Transistoren.

:::grafik
Transferkennlinie **halblogarithmisch** ($\log I_D$ über $V_{gs}$): im Unterschwellenbereich eine Gerade, deren
Steigung die Unterschwellensteigung $S$ ist; eingezeichnet die ideale Grenze „$60\,$mV/Dekade". Daneben der
kapazitive Teiler $C_{ox}$ / $C_{\text{depl}}$.
:::

:::kern
Der __MOSFET__ ist ein MOS-Kondensator mit __Source__/__Drain__ ($n^{++}$): Die Gatespannung erzeugt über $V_{th}$
den __Inversionskanal__ und schaltet den Strom **berührungslos** (keine Quasi-Fermi-Aufspaltung). Transport über
den „Top of the Barrier" (Diffusion hinauf, Drift hinab). __Gradual-Channel-Näherung__: $Q(x)=C_{ox}(V_{gs}-V_{th}
-V(x))$, Integration → $I=W\tfrac{\mu}{L}C_{ox}(V_{ds}(V_{gs}-V_{th})-\tfrac{V_{ds}^2}{2})$. **Linear** (kleine
$V_{ds}$: spannungsgesteuerter Widerstand), **Sättigung/pinch-off** ($V_{ds}=V_{gs}-V_{th}$, $I_{sat}=W\tfrac{\mu}
{2L}C_{ox}(V_{gs}-V_{th})^2$, Strom konstant). $V_{th}$ über Austrittsarbeit $\Phi_m-\chi_{si}$ ($\chi_{si}=4{,}05\,$eV)
+ Bulk-Dotierung. Im Auszustand exponentieller Unterschwellenstrom; __inverse Unterschwellensteigung__
$S=\tfrac{k_BT}{e}\ln(10)\tfrac{C_{ox}+C_{\text{depl}}}{C_{ox}}\ge 60\,$mV/Dekade bei RT (thermische Grenze,
Skalierungs-Engpass).
:::

Damit ist der Bogen komplett: von der Quantenmechanik einzelner Elektronen über Kristall, Energiebänder und
Statistik bis zum Transistor, der daraus Logik macht. Der MOSFET vereint praktisch **alles** aus diesem Modul —
Bandlücke, effektive Masse, Dotierung, Inversionskanal, Drift, Diffusion und Barrierensteuerung — in einem einzigen
Bauelement.
