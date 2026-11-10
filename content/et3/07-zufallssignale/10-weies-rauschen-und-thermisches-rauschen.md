---
title: Stufe 9: Weißes Rauschen und thermisches Rauschen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3271000
summary: Das wichtigste Modell für Störungen: Rauschen mit gleicher Leistungsdichte bei allen Frequenzen.
tags: weißes Rauschen
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Das wichtigste Modell für Störungen: Rauschen mit gleicher Leistungsdichte bei allen Frequenzen.
:::

:::definition Definition 9.1 (Weißes Rauschen)
<span class="anker" id="satz-9-1"></span>

Ein mittelwertfreier Prozess mit $\Phi_{ss}(f)=N_0$ für alle $f$ heißt __weißes Rauschen__. Seine AKF ist $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$.
:::

⁠**So liest man das:** Werte zu verschiedenen Zeiten sind unkorreliert, egal wie nahe sie beieinanderliegen. Die Leistung $\int N_0\mathrm{d} f$ ist unendlich: Weißes Rauschen ist ein Grenzmodell wie der Dirac-Impuls. Wirklich gemessen wird immer gefiltertes, „farbiges“ Rauschen:

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

Hinter einem idealen Tiefpass mit $f_\mathrm g$: $L_g=2N_0f_\mathrm g$ und $\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$ (Abb. [3](#abb-3)). Die AKF ist an den Stellen $\tau=k/(2f_\mathrm g)$, $k\neq0$, null: Abtastwerte im Abstand der Nyquist-Rate sind unkorreliert.

:::abbildung et3/k7tp 3
AKF von weißem Rauschen hinter einem idealen Tiefpass: $2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$. Bei $\tau=0$ die Leistung $2N_0f_\mathrm g$. An den roten Punkten ($\tau=k/(2f_\mathrm g)$) ist sie null.
:::

**Thermisches Rauschen.** Die Wärmebewegung der Elektronen erzeugt an jedem Widerstand $R$ eine Rauschspannung. Im Leerlauf, gemessen im Frequenzbereich $|f|\le f_\mathrm g$:

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

mit der Boltzmann-Konstanten $k=1{,}38\cdot10^{-23}$ W s/K. Bei Raumtemperatur (290 K) ist $kT\approx4\cdot10^{-21}$ W/Hz, also 4 pW je GHz Bandbreite. $L_{\max}$ ist die Leistung, die man dem Widerstand bei Leistungsanpassung höchstens entnehmen kann. Im Rechenmodell ($1\,\mathrm{k\Omega}$, 20 kHz) ist der Effektivwert $\sqrt{\mathrm E\{u^2\}}=0{,}57$ µ V. Diese Größenordnung begrenzt, wie empfindlich ein Mikrofonverstärker sein kann. Das Spektrum ist bis etwa $10^{12}$ Hz flach.

:::ltspice Thermisches Rauschen messen
LTspice gibt jedem Widerstand sein thermisches Rauschen mit. Die Analyse `.noise` rechnet an einem Knoten die Rauschdichte `V(onoise)` in V$/\sqrt{\mathrm{Hz}}$. Die Messung `.meas noise urms INTEG V(onoise)` integriert sie quadratisch über den Frequenzbereich der Analyse, wie in [(8.3)](zufallssignale-in-lti-systemen-leistungsdichte.html#gl-8-3), und liefert den Effektivwert. `.temp 16.85` stellt 290 K ein.

⁠**Widerstand:** `res` mit `{Rx}` vom Netz `a` nach Masse, parallel eine Stromquelle `current` mit dem Wert 0 (Name `I1`). Sie belastet nichts, `.noise` braucht sie nur als Bezugsquelle. Direktiven `.param Rx=1k` und `.noise V(a) I1 lin 20001 1 20k`. Ergebnis: 4,0 nV$/\sqrt{\mathrm{Hz}}$ und `urms` $=0{,}57$ µ V wie oben. Setze `Rx=1Meg` und vergleiche mit deinem Ergebnis aus Aufgabe [8](#aufg-8).

⁠**$kT/C$:** Quelle `voltage` `V1` mit dem Wert 0 und `AC 1`, `res` mit `{Rx}` nach `out`, `cap` mit `1p` nach Masse. Direktiven `.step param Rx list 1k 1Meg` und `.noise V(out) V1 dec 200 1 1T`, dazu wieder `.temp 16.85` und die Messung `urms`. `urms` ist für beide Widerstände gleich. Vergleiche den Wert mit deinem Ergebnis aus Aufgabe [9](#aufg-9)(b).
:::

:::aufgabe Aufgabe 8 ★ Rauschen eines Widerstands
<span class="anker" id="aufg-8"></span>

Berechne den Rauscheffektivwert eines Widerstands von $1\,\mathrm{M\Omega}$ bei 290 K und 20 kHz Bandbreite. Um welchen Faktor ist er größer als beim $1\,\mathrm{k\Omega}$-Widerstand, und warum gerade um diesen?

:::loesung
Der Effektivwert wächst mit $\sqrt R$: $\sqrt{1000}=31{,}6$-mal größer, also $0{,}566\cdot31{,}6=17{,}9$ µ V.
:::
:::

:::aufgabe Aufgabe 9 ★★ Das $kT/C$-Rauschen
<span class="anker" id="aufg-9"></span>

Das thermische Rauschen des Widerstands ($N_0=2kTR$) läuft durch das RC-Glied, das er mit einem Kondensator $C$ bildet ($h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$).

<ol class="al">

<li>

Zeige mit [(9.1)](#gl-9-1), dass die Rauschleistung am Kondensator $kT/C$ ist, unabhängig von $R$.

</li>

<li>

Wie groß ist der Effektivwert bei $C=1$ pF und 290 K? Warum hilft ein kleinerer Widerstand hier nicht?

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$. Also $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$.

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V. Ein kleinerer Widerstand rauscht zwar weniger pro Hertz, aber das RC-Glied wird breitbandiger ($1/RC$ größer). Beides hebt sich genau auf. Nur ein größerer Kondensator verringert das Rauschen.
:::
:::
