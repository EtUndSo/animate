---
title: Stufe 9: Tangente statt Kurve
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
order: 1201100
summary: Ein Verstärker arbeitet um einen festen Punkt im aktiven Bereich.
tags: Kleinsignal, partielle Ableitung, Eingangswiderstand, Ausgangswiderstand, Early-Spannung, erweiterte Ersatzschaltbild, Kleinsignal-Ersatzschaltbild
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Ein Verstärker arbeitet um einen festen Punkt im aktiven Bereich. Kleine Änderungen sehen dort keine e-Funktion, sondern eine Gerade. Diese Stufe liest deren Steigungen ab und zeichnet sie als Ersatzschaltbild.
:::

**Die Idee.** Das lineare Modell aus Stufe [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) hat zwei Fehler. Es macht die BE-Strecke zu einer festen Spannung, hat also den Eingangswiderstand null. Und es macht die Ausgangskennlinie waagerecht, setzt also den Leitwert null. Beide Steigungen sind in Wahrheit endlich. Für kleine Änderungen um den Arbeitspunkt genügt, was bei der Diode ([Teil 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) die Tangente war: Das Gelände aus Stufe [3](eine-flache-viele-kennlinien.html#stufe-3) wird dort zu einer ebenen Schräge, mit je einer Steigung pro Richtung.

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

**Vom Modell zum Ersatzschaltbild.** Die Tangenten werden zu Bauteilen (Abb. [11](#abb-11)). Das __erweiterte Ersatzschaltbild__ enthält die Gleichanteile. Im Eingang liegen eine Quelle $U_0$ und $r_\mathrm{BE}$ in Reihe. Dabei ist $U_0=U_\mathrm{BE}-U_T=0{,}574$ V der Punkt, an dem die Tangente der Eingangskennlinie die Achse trifft. Im Ausgang liegen eine gesteuerte Stromquelle $I$ und $r_\mathrm{CE}$ parallel. Sie gibt im Punkt A $I=1{,}85$ mA ab, durch $r_\mathrm{CE}$ fließen die restlichen 0,15 mA. Lässt man die Gleichanteile weg, bleibt das __Kleinsignal-Ersatzschaltbild__. Konstante Quellen entfallen dabei: Eine konstante Spannung wird zum Draht, das gilt auch für $U_\mathrm{CC}$ (Überlagerung, [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Für die Übersetzung gilt: Hängt ein Strom von der Spannung über seinem eigenen Klemmenpaar ab, ist er ein Widerstand. Hängt er von einer fremden Spannung ab, ist er eine gesteuerte Quelle, hier eine spannungsgesteuerte Stromquelle (VCCS, [Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Als Zweitor ausgedrückt sind das die Y-Parameter $Y_{11}=1/r_\mathrm{BE}$, $Y_{12}=0$, $Y_{21}=S$, $Y_{22}=G_\mathrm{CE}$.

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
