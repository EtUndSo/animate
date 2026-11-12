---
title: Stufe 9: Tangente statt Kurve
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1201100
summary: Ein Verstärker arbeitet um einen festen Punkt im aktiven Bereich.
tags: Kleinsignal, partielle Ableitung, Eingangswiderstand, Ausgangswiderstand, Early-Spannung, erweiterte Ersatzschaltbild, Kleinsignal-Ersatzschaltbild
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Ein Verstärker arbeitet um einen festen Punkt im aktiven Bereich. Kleine Änderungen sehen dort keine e-Funktion, sondern eine Gerade. Diese Stufe liest deren Steigungen ab und zeichnet sie als Ersatzschaltbild.
:::

**Die Idee.** Das lineare Modell aus Stufe [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) hat zwei Fehler. Es macht die BE-Strecke zu einer festen Spannung, hat also den Eingangswiderstand null. Und es macht die Ausgangskennlinie waagerecht, setzt also den Leitwert null. Beide Steigungen sind in Wahrheit endlich. Für kleine Änderungen um den Arbeitspunkt genügt, was bei der Diode ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) die Tangente war: Das Gelände aus Stufe [3](eine-flache-viele-kennlinien.html#stufe-3) wird dort zu einer ebenen Schräge, mit je einer Steigung pro Richtung.

Die Zerlegung schreibt man so: Gesamtgröße gleich Gleichanteil plus Änderung, $u_\mathrm{BE}(t)=U_\mathrm{BE}+u_\mathrm{be}(t)$, $i_\mathrm{C}(t)=I_\mathrm{C}+i_\mathrm{c}(t)$. Die kleinen Buchstaben mit kleinen Indizes heißen __Kleinsignal__. Das Zeichen $\partial$ steht für die __partielle Ableitung__: die Ableitung nach einer Variablen, während die anderen festgehalten werden, also die Steigung eines Schnitts.

:::definition Definition 9.1 (Kleinsignalgrößen im Arbeitspunkt)
<span class="anker" id="satz-9-1"></span>

<span class="anker" id="gl-9-1"></span>
$$S=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{I_\mathrm{C}}{U_T},\qquad r_\mathrm{BE}=\frac{\partial U_\mathrm{BE}}{\partial I_\mathrm{B}}=\frac{U_T}{I_\mathrm{B}}=\frac{B}{S},\qquad G_\mathrm{CE}=\frac1{r_\mathrm{CE}}=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{CE}}=\frac{I_\mathrm{C}}{U_\mathrm{Early}+U_\mathrm{CE}}. \tag{9.1}$$

Für die Änderungen gilt damit

<span class="anker" id="gl-9-2"></span>
$$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}},\qquad i_\mathrm{c}=S\,u_\mathrm{be}+\frac{u_\mathrm{ce}}{r_\mathrm{CE}}. \tag{9.2}$$
:::

⁠**So liest man das:** Die Steilheit $S$ in A/V ist die Steigung der Steuerkennlinie, $r_\mathrm{BE}$ der __Eingangswiderstand__, die Steigung der Eingangskennlinie umgekehrt gelesen. $r_\mathrm{CE}$ ist der __Ausgangswiderstand__. Die Geraden der Ausgangskennlinien treffen sich nach links verlängert bei $-U_\mathrm{Early}$. Die __Early-Spannung__ $U_\mathrm{Early}$ liegt typisch zwischen 50 V und 200 V, bei T sind es 74 V. Mechanismus: Mehr $U_\mathrm{CB}$ verbreitert die Raumladungszone in die Basis hinein. Die Basis wird schmaler, das Dichtegefälle steiler, der Strom größer. **Gültigkeit:** aktiver Bereich und $|u_\mathrm{be}|\ll U_T$.

:::herleitung Die Steigungen
Aus $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$ folgt $\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{1}{U_T}I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}=\frac{I_\mathrm{C}}{U_T}$. Die Ableitung einer e-Funktion ist die Funktion selbst durch die Skala im Exponenten. Ebenso ist $\partial I_\mathrm{B}/\partial U_\mathrm{BE}=I_\mathrm{B}/U_T$. Der Kehrwert ist $r_\mathrm{BE}$. Mit $I_\mathrm{B}=I_\mathrm{C}/B$ folgt $r_\mathrm{BE}=B/S$. Der dritte Faktor in [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1) ergibt $\partial I_\mathrm{C}/\partial U_\mathrm{CE}=I_\mathrm{C}/(74\,\mathrm{V}+U_\mathrm{CE})$. Das sind im Punkt A 80 V im Nenner. Die Summe in [(9.2)](#gl-9-2) ist die Tangentialebene, die beide Richtungen zusammenfasst.
:::

:::abbildung et1/k10tangente 10
Links die Steuerkennlinie mit Tangente im Punkt A (2 mA), Steigung $S=76{,}9$ mS. Rechts Ausgangskennlinien für zwei Werte von $U_\mathrm{BE}$. Der Abstand der Kurven ist die Wirkung von $S$. Die Steigung jeder Kurve ist $1/r_\mathrm{CE}$, nach links verlängert treffen sie $-74$ V.
:::

::::beispiel
Im Punkt A sind $S=2\,\mathrm{mA}/26\,\mathrm{mV}=76{,}9$ mS, also $1/S=13\,\Omega$, dazu $r_\mathrm{BE}=200/S=2{,}6$ k$\Omega$ und $r_\mathrm{CE}=80\,\mathrm{V}/2\,\mathrm{mA}=40$ k$\Omega$. Mechanismus von $S$: 1 mV mehr $U_\mathrm{BE}$ senkt die Barriere, die Injektion steigt nach der Tangente um 3,85 %, das sind 77 µ A. Um dasselbe über den Ausgang zu erreichen, brauchte man 3 V an $U_\mathrm{CE}$.
::::

⁠**Kurz gesagt:** Die Steilheit ist der Strom geteilt durch $U_T$, unabhängig von $B$ und $I_\mathrm{S}$. **Grenzfälle:** $I_\mathrm{C}\to0$ ergibt $S\to0$: Ohne Ruhestrom gibt es keine Steuerwirkung. $U_\mathrm{Early}\to\infty$ ergibt $r_\mathrm{CE}\to\infty$, die ideale Stromquelle.

**Wie klein ist klein?** Exakt ist $i_\mathrm{c}=I_\mathrm{C}(\mathrm{e}^{u_\mathrm{be}/U_T}-1)$, die Tangente sagt $I_\mathrm{C}u_\mathrm{be}/U_T$. Bei $u_\mathrm{be}=+1$ mV beträgt der Fehler 2 %, bei $+5$ mV sind es 10 % ($+424$ µ A statt $+385$ µ A), bei $-5$ mV fließen dagegen nur $-350$ µ A. Die positive Halbwelle wird größer als die negative, das Signal wird verzerrt. Bei 26 mV ist die Tangente unbrauchbar.

**Vom Modell zum Ersatzschaltbild.** Die Tangenten werden zu Bauteilen (Abb. [11](#abb-11)). Das __erweiterte Ersatzschaltbild__ enthält die Gleichanteile. Im Eingang liegen eine Quelle $U_0$ und $r_\mathrm{BE}$ in Reihe. Dabei ist $U_0=U_\mathrm{BE}-U_T=0{,}574$ V der Punkt, an dem die Tangente der Eingangskennlinie die Achse trifft. Im Ausgang liegen eine gesteuerte Stromquelle $I$ und $r_\mathrm{CE}$ parallel. Sie gibt im Punkt A $I=1{,}85$ mA ab, durch $r_\mathrm{CE}$ fließen die restlichen 0,15 mA. Lässt man die Gleichanteile weg, bleibt das __Kleinsignal-Ersatzschaltbild__. Konstante Quellen entfallen dabei: Eine konstante Spannung wird zum Draht, das gilt auch für $U_\mathrm{CC}$ (Überlagerung, [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Für die Übersetzung gilt: Hängt ein Strom von der Spannung über seinem eigenen Klemmenpaar ab, ist er ein Widerstand. Hängt er von einer fremden Spannung ab, ist er eine gesteuerte Quelle, hier eine spannungsgesteuerte Stromquelle (VCCS, [Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Als Zweitor ausgedrückt sind das die Y-Parameter $Y_{11}=1/r_\mathrm{BE}$, $Y_{12}=0$, $Y_{21}=S$, $Y_{22}=G_\mathrm{CE}$.

:::abbildung et1/k10kleinsignal 11
Links das erweiterte Ersatzschaltbild für Gleichgrößen im leitenden Betrieb. Rechts das Kleinsignal-Ersatzschaltbild: Die Konstanten sind verschwunden, nur die Steigungen bleiben. Die Quelle $S\,u_\mathrm{be}$ ist die Tangente in Richtung $U_\mathrm{BE}$, $r_\mathrm{CE}$ die in Richtung $U_\mathrm{CE}$.
:::

:::frage Ist die Steilheit nicht die Steigung im Ausgangskennlinienfeld?
Nein. Dort ist $U_\mathrm{CE}$ die waagerechte Achse, die Steigung ist also $1/r_\mathrm{CE}$. Die Steilheit gehört zur Richtung $U_\mathrm{BE}$ und erscheint im Ausgangsfeld als senkrechter Abstand zwischen zwei Kurven, geteilt durch ihren Unterschied in $U_\mathrm{BE}$.
:::

:::frage Warum ist $1/S=13\,\Omega$, aber $r_\mathrm{BE}=2{,}6$ k$\Omega$? Beide messen doch dieselbe Spannung.
Beide teilen die Spannungsänderung durch einen Strom, aber durch verschiedene. $1/S$ teilt durch die Änderung von $I_\mathrm{C}$, $r_\mathrm{BE}$ durch die $B$-mal kleinere Änderung von $I_\mathrm{B}$. Deshalb ist der Eingangswiderstand $B$-mal größer. Das Verhältnis ist hier 200.
:::

:::aufgabe Aufgabe 11 ★★ Kleinsignalgrößen
<span class="anker" id="aufg-11"></span>

T arbeitet bei $I_\mathrm{C}=0{,}5$ mA und $U_\mathrm{CE}=6$ V. (a) Bestimme $S$, $1/S$, $r_\mathrm{BE}$ und $r_\mathrm{CE}$. (b) Vergleiche für $u_\mathrm{be}=\pm5$ mV die exakte Stromänderung mit der Tangente. (c) Sage vorher: Wie ändern sich die vier Werte aus (a), wenn der Strom doppelt so groß wird?

:::loesung
(a) $S=19{,}2$ mS, $1/S=52\,\Omega$, $r_\mathrm{BE}=200/S=10{,}4$ k$\Omega$, $r_\mathrm{CE}=80\,\mathrm{V}/0{,}5\,\mathrm{mA}=160$ k$\Omega$.

(b) Tangente $\pm96$ µ A. Exakt: $+106$ µ A und $-87$ µ A.

(c) $S$ verdoppelt sich, $1/S$, $r_\mathrm{BE}$ und $r_\mathrm{CE}$ halbieren sich. Alle vier sind proportional oder umgekehrt proportional zum Strom.
:::
:::

::::formelsammlung
**Gleichanteil und Kleinsignal**

$$u_\mathrm{BE}(t)=U_\mathrm{BE}+u_\mathrm{be}(t),\qquad i_\mathrm{C}(t)=I_\mathrm{C}+i_\mathrm{c}(t)$$

Kleine Buchstaben mit kleinen Indizes bezeichnen das Kleinsignal, die Änderung um den Arbeitspunkt.

**Steilheit**

$$S=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{I_\mathrm{C}}{U_T}$$

Steigung der Steuerkennlinie in A/V, unabhängig von $B$ und $I_\mathrm{S}$. Im Punkt A ist $S=76{,}9$ mS.

**Eingangswiderstand**

$$r_\mathrm{BE}=\frac{\partial U_\mathrm{BE}}{\partial I_\mathrm{B}}=\frac{U_T}{I_\mathrm{B}}=\frac{B}{S}$$

Kehrwert der Steigung der Eingangskennlinie, $B$-mal größer als $1/S$.

**Ausgangsleitwert**

$$G_\mathrm{CE}=\frac1{r_\mathrm{CE}}=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{CE}}=\frac{I_\mathrm{C}}{U_\mathrm{Early}+U_\mathrm{CE}}$$

$r_\mathrm{CE}$ ist der Ausgangswiderstand, $r_\mathrm{CE}\approx U_\mathrm{Early}/I_\mathrm{C}$. Die Early-Spannung $U_\mathrm{Early}$ liegt typisch zwischen 50 V und 200 V, bei T sind es 74 V. Alle Kleinsignalgrößen gelten im aktiven Bereich für $|u_\mathrm{be}|\ll U_T$.

**Kleinsignalgleichungen**

$$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}},\qquad i_\mathrm{c}=S\,u_\mathrm{be}+\frac{u_\mathrm{ce}}{r_\mathrm{CE}}$$

Tangentialebene im Arbeitspunkt. Als Zweitor: $Y_{11}=1/r_\mathrm{BE}$, $Y_{12}=0$, $Y_{21}=S$, $Y_{22}=G_\mathrm{CE}$.

**Exakte Stromänderung**

$$i_\mathrm{c}=I_\mathrm{C}(\mathrm{e}^{u_\mathrm{be}/U_T}-1)$$

Die Tangente gibt $I_\mathrm{C}u_\mathrm{be}/U_T$; der Fehler beträgt 2 % bei $+1$ mV und 10 % bei $+5$ mV. Die positive Halbwelle wird größer als die negative, das Signal wird verzerrt.

**Erweitertes Ersatzschaltbild**

$$U_0=U_\mathrm{BE}-U_T$$

Im Eingang die Quelle $U_0$ und $r_\mathrm{BE}$ in Reihe; $U_0$ ist der Punkt, an dem die Tangente der Eingangskennlinie die Achse trifft. Im Ausgang eine gesteuerte Stromquelle und $r_\mathrm{CE}$ parallel. Ohne Gleichanteile bleibt das Kleinsignal-Ersatzschaltbild mit der Quelle $S\,u_\mathrm{be}$.
::::

::::lernkarten
:::karte zusammenhang Zwei Fehler des linearen Modells
Welche zwei Fehler hat das lineare Modell aus drei Bereichen, wenn man kleine Änderungen um den Arbeitspunkt betrachtet?
---
Es macht die BE-Strecke zu einer festen Spannung, also mit Eingangswiderstand null, und die Ausgangskennlinie waagerecht, also mit Leitwert null. In Wahrheit sind beide Steigungen endlich.
--- falsch
Es rechnet mit einem festen $B$ und einer festen Versorgung. In Wahrheit schwanken beide im Takt des Signals, deshalb muss man für kleine Änderungen im Arbeitspunkt neue Werte messen.
--- falsch
Es macht die BE-Strecke zu einem offenen Schalter und die Ausgangskennlinie senkrecht. In Wahrheit leitet die BE-Strecke schon ab 0 V, und die Kurve ist waagerecht.
--- falsch
Es vernachlässigt den Basisstrom und die Temperatur. Beide Fehler verschwinden aber bei kleinen Änderungen, deshalb genügt das lineare Modell dort ohne Ergänzung.
:::
:::karte zusammenhang Kleinsignal
Wie zerlegt man eine Größe am Transistor in Gleichanteil und Kleinsignal, und wie schreibt man beides?
---
Gesamtgröße gleich Gleichanteil plus Änderung: $u_\mathrm{BE}(t)=U_\mathrm{BE}+u_\mathrm{be}(t)$, $i_\mathrm{C}(t)=I_\mathrm{C}+i_\mathrm{c}(t)$. Das Kleinsignal schreibt man mit kleinen Buchstaben und kleinen Indizes.
--- falsch
Gesamtgröße gleich Gleichanteil mal Änderung: $u_\mathrm{BE}(t)=U_\mathrm{BE}\cdot u_\mathrm{be}(t)$. Das Kleinsignal schreibt man mit großen Buchstaben und kleinen Indizes, den Gleichanteil umgekehrt.
--- falsch
Gesamtgröße gleich Änderung minus Gleichanteil: $u_\mathrm{BE}(t)=u_\mathrm{be}(t)-U_\mathrm{BE}$. Das Kleinsignal schreibt man mit kleinen Buchstaben und großen Indizes.
--- falsch
Man trennt nicht, sondern schreibt die Gesamtgröße mit kleinen Buchstaben, sobald ein Signal anliegt. Der Gleichanteil wird dann nicht mehr gebraucht, weil er sich nicht ändert.
:::
:::karte begriff partielle Ableitung
Was bedeutet das Zeichen $\partial$ in $\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}$, wenn $I_\mathrm{C}$ von zwei Spannungen abhängt?
---
Die partielle Ableitung: die Ableitung nach einer Variablen, während die anderen festgehalten werden, also die Steigung eines Schnitts durch die Fläche.
--- falsch
Es steht für eine kleine, aber endliche Differenz zweier Messwerte, also $\Delta I_\mathrm{C}/\Delta U_\mathrm{BE}$. Beide Spannungen dürfen sich dabei gleichzeitig ändern.
--- falsch
Es steht für die Ableitung nach beiden Variablen zugleich, also für die größte Steigung der Fläche in irgendeiner Richtung, gemessen im Arbeitspunkt.
--- falsch
Es steht für die Ableitung nach der Zeit, also für die Geschwindigkeit, mit der sich $I_\mathrm{C}$ ändert, wenn am Eingang ein Signal anliegt.
:::
:::karte zusammenhang Steilheit
Woran liegt es, dass zwei verschiedene Transistortypen beim selben Kollektorstrom dieselbe Steilheit haben?
---
$S=I_\mathrm{C}/U_T$ ist die Steigung der Steuerkennlinie, und die Steigung einer e-Funktion ist ihr Wert durch die Skala $U_T$. $B$ und $I_\mathrm{S}$ kommen darin nicht vor, nur der Strom.
--- falsch
$S=B\,I_\mathrm{C}/U_T$ hängt zwar von $B$ ab, doch Transistoren mit demselben Strom haben immer dasselbe $B$, gleich welcher Typ. Deshalb ist auch die Steilheit gleich.
--- falsch
$S=I_\mathrm{S}/U_T$ hängt nur vom Sättigungssperrstrom ab, und der ist bei allen Siliziumtransistoren gleich. Der Kollektorstrom spielt dafür keine Rolle, nur das Material.
--- falsch
$S=U_T/I_\mathrm{C}$ ist ein Widerstand, der bei gleichem Strom gleich ist. Er hängt nur von der Temperatur ab, weil $U_T$ die einzige Größe des Bauteils darin ist.
:::
:::karte zusammenhang Wirkung von einem Millivolt
Was passiert im Transistor im Punkt A ($I_\mathrm{C}=2$ mA), wenn $U_\mathrm{BE}$ um 1 mV steigt?
---
Die Barriere sinkt, die Injektion steigt nach der Tangente um 3,85 %, also $I_\mathrm{C}$ um 77 µ A. Das ist $S=76{,}9$ mS mal 1 mV; über den Ausgang bräuchte man dafür 3 V an $U_\mathrm{CE}$.
--- falsch
Die Barriere steigt, die Injektion sinkt um 3,85 %, also $I_\mathrm{C}$ um 77 µ A. Über den Ausgang erreicht man dasselbe schon mit 1 mV mehr an $U_\mathrm{CE}$, weil beide Richtungen gleich steil sind.
--- falsch
Fast nichts: 1 mV ist im Vergleich zu 0,6 V nur 0,17 %, also steigt $I_\mathrm{C}$ ebenfalls um rund 0,17 %, das sind etwa 3 µ A.
--- falsch
$I_\mathrm{C}$ verdoppelt sich auf 4 mA, weil schon jedes Millivolt die Barriere um einen festen Faktor senkt. Erst ab 18 mV wird die Änderung wieder kleiner.
:::
:::karte formel Kleinsignalgrößen im Arbeitspunkt
Wie hängen die Steilheit $S$, der Eingangswiderstand $r_\mathrm{BE}$ und der Ausgangsleitwert $G_\mathrm{CE}$ vom Arbeitspunkt ab?
---
$S=I_\mathrm{C}/U_T$, $r_\mathrm{BE}=\frac{U_T}{I_\mathrm{B}}=\frac{B}{S}$, $G_\mathrm{CE}=\frac1{r_\mathrm{CE}}=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{CE}}=\frac{I_\mathrm{C}}{U_\mathrm{Early}+U_\mathrm{CE}}$. Gültig im aktiven Bereich und für $|u_\mathrm{be}|\ll U_T$.
--- falsch
$S=U_T/I_\mathrm{C}$, $r_\mathrm{BE}=\frac{U_T}{I_\mathrm{C}}=\frac{1}{S}$, $G_\mathrm{CE}=\frac{U_\mathrm{CE}}{I_\mathrm{C}}$. Gültig in allen drei Bereichen und für jede Signalgröße.
--- falsch
$S=I_\mathrm{C}/U_T$, $r_\mathrm{BE}=\frac{U_T}{I_\mathrm{B}}=B\,S$, $G_\mathrm{CE}=\frac{I_\mathrm{C}}{U_\mathrm{Early}-U_\mathrm{CE}}$. Gültig im aktiven Bereich und für $|u_\mathrm{be}|\gg U_T$.
--- falsch
$S=B\,I_\mathrm{B}$, $r_\mathrm{BE}=\frac{U_\mathrm{BE}}{I_\mathrm{B}}$, $G_\mathrm{CE}=\frac{I_\mathrm{C}}{U_\mathrm{CE}}$. Das sind die Verhältnisse der Gleichgrößen im Arbeitspunkt, gültig im aktiven Bereich.
:::
:::karte formel Kleinsignalgleichungen
Welche Gleichungen beschreiben die Änderungen $i_\mathrm{b}$ und $i_\mathrm{c}$ um den Arbeitspunkt?
---
$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}}$ und $i_\mathrm{c}=S\,u_\mathrm{be}+\frac{u_\mathrm{ce}}{r_\mathrm{CE}}$, die Tangentialebene, die beide Richtungen zusammenfasst; gültig im aktiven Bereich für $|u_\mathrm{be}|\ll U_T$.
--- falsch
$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}}$ und $i_\mathrm{c}=S\,u_\mathrm{ce}+\frac{u_\mathrm{be}}{r_\mathrm{CE}}$. Die Summe beschreibt beide Richtungen; sie gilt für jede Signalgröße im aktiven Bereich, weil die Tangente dort exakt ist.
--- falsch
$i_\mathrm{b}=r_\mathrm{BE}\,u_\mathrm{be}$ und $i_\mathrm{c}=B\,i_\mathrm{b}$. Der Ausgang hängt also nur vom Basisstrom ab, die Spannung $u_\mathrm{ce}$ geht nicht ein; gültig für $|u_\mathrm{be}|\ll U_T$.
--- falsch
$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}}$ und $i_\mathrm{c}=S\,u_\mathrm{be}\cdot\frac{u_\mathrm{ce}}{r_\mathrm{CE}}$. Das Produkt beschreibt die Krümmung der Fläche; es gilt für $|u_\mathrm{be}|\ll U_T$.
:::
:::karte herleitung Steigungen im Arbeitspunkt
Wie folgen aus der Modellfläche die Kleinsignalgrößen $S=I_\mathrm{C}/U_T$, $r_\mathrm{BE}=B/S$ und der Ausgangsleitwert?
---
Aus $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$ folgt $\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{1}{U_T}I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}=\frac{I_\mathrm{C}}{U_T}$, weil die Ableitung einer e-Funktion die Funktion selbst durch die Skala im Exponenten ist.
---
Ebenso ist $\partial I_\mathrm{B}/\partial U_\mathrm{BE}=I_\mathrm{B}/U_T$, und der Kehrwert ist $r_\mathrm{BE}$, weil $I_\mathrm{B}$ dieselbe e-Funktion enthält und $r_\mathrm{BE}$ die umgekehrt gelesene Steigung ist.
---
Mit $I_\mathrm{B}=I_\mathrm{C}/B$ folgt $r_\mathrm{BE}=B/S$, weil der Basisstrom der $B$-te Teil des Kollektorstroms ist.
---
Der dritte Faktor der Modellfläche ergibt $\partial I_\mathrm{C}/\partial U_\mathrm{CE}=I_\mathrm{C}/(74\,\mathrm{V}+U_\mathrm{CE})$, weil er linear in $U_\mathrm{CE}$ wächst und bei $U_\mathrm{CE}=-74$ V null wäre.
:::
:::karte begriff Eingangswiderstand
Was gibt der Eingangswiderstand $r_\mathrm{BE}$ eines Transistors im Arbeitspunkt an?
---
Der Kehrwert der Steigung der Eingangskennlinie im Arbeitspunkt: $r_\mathrm{BE}=\frac{\partial U_\mathrm{BE}}{\partial I_\mathrm{B}}=\frac{U_T}{I_\mathrm{B}}=\frac{B}{S}$. Im Punkt A sind es 2,6 k$\Omega$.
--- falsch
Das Verhältnis der Gleichgrößen im Arbeitspunkt: $U_\mathrm{BE}/I_\mathrm{B}$, also 0,6 V durch 10 µ A. Im Punkt A sind es 60 k$\Omega$.
--- falsch
Die Steigung der Steuerkennlinie, umgekehrt gelesen: $\frac{\partial U_\mathrm{BE}}{\partial I_\mathrm{C}}=\frac{U_T}{I_\mathrm{C}}=\frac{1}{S}$. Im Punkt A sind es 13 $\Omega$.
--- falsch
Der Widerstand des Basisanschlusses selbst, der vom Arbeitspunkt nicht abhängt. Er ist durch die Dotierung der Basis festgelegt und beträgt einige Ohm.
:::
:::karte begriff Ausgangswiderstand
Was beschreibt der Ausgangswiderstand $r_\mathrm{CE}$ eines Transistors im aktiven Bereich?
---
Der Kehrwert der Steigung der Ausgangskennlinie im Arbeitspunkt: $G_\mathrm{CE}=\frac1{r_\mathrm{CE}}=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{CE}}$. Im Punkt A sind es 40 k$\Omega$.
--- falsch
Das Verhältnis der Gleichgrößen am Ausgang, $U_\mathrm{CE}/I_\mathrm{C}$, im Punkt A also 6 V durch 2 mA. Das sind 3 k$\Omega$, genau wie der Kollektorwiderstand.
--- falsch
Der Kehrwert der Steilheit, $1/S$, also wie stark $U_\mathrm{BE}$ den Strom ändert. Im Punkt A sind es 13 $\Omega$, der Ausgang ist deshalb sehr niederohmig.
--- falsch
Die Steigung der Ausgangskennlinie selbst, gemessen in A/V. Im Punkt A ist sie null, weil die Ausgangskennlinie im aktiven Bereich genau waagerecht verläuft.
:::
:::karte begriff Early-Spannung
Was ist die Early-Spannung eines Transistors, und welcher Mechanismus steckt dahinter?
---
Die Spannung, bei deren negativem Wert $-U_\mathrm{Early}$ sich die verlängerten Ausgangskennlinien treffen, bei T 74 V. Mehr $U_\mathrm{CB}$ verbreitert die Raumladungszone in die Basis, die Basis wird schmaler und der Strom größer.
--- falsch
Die Spannung, ab der die CB-Grenze durchschlägt, typisch 50 V bis 200 V, bei T 74 V. Darüber steigt der Kollektorstrom lawinenartig an, weil Elektronen im starken Feld weitere freischlagen.
--- falsch
Die Spannung $U_\mathrm{Early}$, bei der sich die verlängerten Ausgangskennlinien rechts treffen, typisch 0,5 V bis 2 V. Mehr $U_\mathrm{CB}$ verengt die Raumladungszone, die Basis wird breiter, das Gefälle flacher und der Strom kleiner.
--- falsch
Die Spannung zwischen Basis und Emitter, bei der der Transistor zu leiten beginnt, rund 0,6 V. Sie heißt nach ihrem Entdecker und verschiebt sich um 2 mV je Kelvin.
:::
:::karte begriff erweitertes Ersatzschaltbild
Was enthält das erweiterte Ersatzschaltbild eines leitenden Transistors?
---
Die Tangenten samt Gleichanteilen: im Eingang eine Quelle $U_0=U_\mathrm{BE}-U_T$ und $r_\mathrm{BE}$ in Reihe, im Ausgang eine gesteuerte Stromquelle $I$ und $r_\mathrm{CE}$ parallel.
--- falsch
Die drei Ersatzschaltbilder der Arbeitsbereiche, zu einem einzigen Bild zusammengefügt, mit Schaltern, die je nach Bereich automatisch umgelegt werden.
--- falsch
Nur die Steigungen ohne Gleichanteile: im Eingang $r_\mathrm{BE}$, im Ausgang die Quelle $S\,u_\mathrm{be}$ und $r_\mathrm{CE}$ parallel. Konstante Quellen entfallen.
--- falsch
Die Tangenten samt Gleichanteilen: im Eingang eine Quelle $U_0=U_\mathrm{BE}+U_T$ parallel zu $r_\mathrm{BE}$, im Ausgang eine Spannungsquelle in Reihe mit $r_\mathrm{CE}$.
:::
:::karte begriff Kleinsignal-Ersatzschaltbild
Was bleibt im Kleinsignal-Ersatzschaltbild des Transistors übrig, und warum fallen die konstanten Quellen weg?
---
Das Ersatzschaltbild nur aus Steigungen: $r_\mathrm{BE}$ im Eingang, die Quelle $S\,u_\mathrm{be}$ und $r_\mathrm{CE}$ im Ausgang. Konstante Quellen entfallen, weil eine konstante Spannung für Änderungen ein Draht ist.
--- falsch
Nur die Gleichanteile: die Quelle $U_0$ im Eingang und die Stromquelle $I$ im Ausgang. Die Widerstände entfallen, weil sie für kleine Signale zu groß sind, um im Signalweg noch eine Rolle zu spielen.
--- falsch
Die Steigungen und alle Quellen: $U_\mathrm{CC}$ bleibt als Spannungsquelle stehen, weil sie den Strom liefert, nur $U_0$ entfällt, weil sie kleiner als $U_T$ ist.
--- falsch
Nur $r_\mathrm{BE}$ und $r_\mathrm{CE}$, ohne gesteuerte Quelle. Konstante Quellen entfallen, weil sie für Änderungen offen wirken, und damit verschwindet auch die Quelle $S\,u_\mathrm{be}$.
:::
:::karte zusammenhang Widerstand oder gesteuerte Quelle
Woran erkennt man beim Übersetzen der Tangenten in Bauteile, ob ein Strom zu einem Widerstand oder zu einer gesteuerten Quelle wird?
---
Hängt ein Strom von der Spannung an seinem eigenen Klemmenpaar ab, ist er ein Widerstand; hängt er von einer fremden Spannung ab, eine gesteuerte Quelle, hier eine spannungsgesteuerte Stromquelle.
--- falsch
Hängt ein Strom von einer Spannung ab, ist er immer ein Widerstand. Eine gesteuerte Quelle entsteht nur, wenn ein Strom von einem anderen Strom abhängt, wie im Transistor bei $I_\mathrm{C}=B\,I_\mathrm{B}$ zwischen Basis und Kollektor.
--- falsch
Ist die Steigung positiv, wird der Strom ein Widerstand; ist sie negativ, eine gesteuerte Quelle, weil nur Quellen Energie abgeben und deshalb eine fallende Kennlinie erzeugen können.
--- falsch
Große Steigungen werden gesteuerte Quellen, kleine werden Widerstände. Deshalb wird $S$ zur Quelle und $1/r_\mathrm{CE}$ zum Widerstand, unabhängig von den Klemmen.
:::
:::karte zusammenhang Wie klein klein ist
Warum wird ein Signal verzerrt, wenn $u_\mathrm{be}$ nicht mehr klein gegen $U_T$ ist?
---
Exakt ist $i_\mathrm{c}=I_\mathrm{C}(\mathrm{e}^{u_\mathrm{be}/U_T}-1)$, die Tangente sagt $I_\mathrm{C}u_\mathrm{be}/U_T$. Bei $+5$ mV fließen $+424$ µ A statt $+385$ µ A, bei $-5$ mV nur $-350$ µ A: Die positive Halbwelle wird größer als die negative.
--- falsch
Exakt ist $i_\mathrm{c}=I_\mathrm{C}u_\mathrm{be}/U_T$ für jede Signalgröße, nur der Kollektorwiderstand begrenzt den Ausgang. Verzerrt wird ein Signal erst, wenn der Transistor die Sättigung erreicht.
--- falsch
Bei großem $u_\mathrm{be}$ steigt die Temperatur des Transistors im Takt des Signals. Dadurch schwankt $U_T$, und beide Halbwellen werden gleich stark gestaucht, sodass der Sinus flacher wird.
--- falsch
Exakt ist $i_\mathrm{c}=I_\mathrm{C}(\mathrm{e}^{u_\mathrm{be}/U_T}-1)$, die Tangente sagt $I_\mathrm{C}u_\mathrm{be}/U_T$. Bei $+5$ mV fließen dadurch weniger, bei $-5$ mV mehr als vorhergesagt: Die negative Halbwelle wird größer.
:::
:::karte zusammenhang Steilheit im Ausgangskennlinienfeld
Warum ist die Steilheit nicht die Steigung der Kurven im Ausgangskennlinienfeld?
---
Dort ist $U_\mathrm{CE}$ die waagerechte Achse, die Steigung ist also $1/r_\mathrm{CE}$. Die Steilheit gehört zur Richtung $U_\mathrm{BE}$ und erscheint als senkrechter Abstand zweier Kurven, geteilt durch ihren Unterschied in $U_\mathrm{BE}$.
--- falsch
Weil die Ausgangskennlinien im aktiven Bereich genau waagerecht sind und keine Steigung haben. Die Steilheit liest man stattdessen an der Eingangskennlinie ab, als Steigung von $I_\mathrm{B}$ über $U_\mathrm{BE}$ im Arbeitspunkt.
--- falsch
Doch, sie ist genau diese Steigung, gemessen im Arbeitspunkt. Der Name kommt daher, dass die Kurven im Ausgangskennlinienfeld bei großem $U_\mathrm{CE}$ besonders steil ansteigen.
--- falsch
Weil die Steilheit die Steigung der Arbeitsgeraden ist, also $-1/R_\mathrm{C}$. Sie hängt deshalb von der Schaltung ab und nicht von den Kurven des Transistors.
:::
:::karte zusammenhang Zwei Widerstände an derselben Spannung
Warum ist im Punkt A $1/S=13\,\Omega$, der Eingangswiderstand $r_\mathrm{BE}$ aber 2,6 k$\Omega$, obwohl beide dieselbe Spannung betreffen?
---
Beide teilen die Änderung von $U_\mathrm{BE}$ durch einen Strom, $1/S$ durch die Änderung von $I_\mathrm{C}$, $r_\mathrm{BE}$ durch die $B$-mal kleinere von $I_\mathrm{B}$. Deshalb ist $r_\mathrm{BE}$ $B$-mal größer, hier um den Faktor 200.
--- falsch
$1/S$ ist der Widerstand im Ausgang, $r_\mathrm{BE}$ der im Eingang; beide liegen an verschiedenen Spannungen. Ihr Verhältnis ist der Spannungsteiler aus $R_\mathrm{B}$ und $R_\mathrm{C}$, hier rund 200.
--- falsch
$r_\mathrm{BE}$ enthält zusätzlich den Basiswiderstand $R_\mathrm{B}$ der Schaltung, $1/S$ nur den Transistor selbst. Ohne $R_\mathrm{B}$ wären beide gleich groß, nämlich 13 $\Omega$.
--- falsch
$1/S$ gilt nur für Gleichgrößen, $r_\mathrm{BE}$ nur für kleine Änderungen um den Arbeitspunkt. Für kleine Signale ist $1/S$ deshalb ohne Bedeutung, am Eingang zählen allein die 2,6 k$\Omega$ von $r_\mathrm{BE}$.
:::
::::
