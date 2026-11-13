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

::::formelsammlung
**Weißes Rauschen**

$$\Phi_{ss}(f)=N_0,\qquad\varphi_{ss}(\tau)=N_0\,\delta(\tau)$$

Mittelwertfrei; Werte zu verschiedenen Zeiten sind unkorreliert. Die Leistung $\int N_0\mathrm{d} f$ ist unendlich: ein Grenzmodell wie der Dirac-Impuls.

**Gefiltertes weißes Rauschen**

$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f$$

Gemessen wird immer solches „farbiges“ Rauschen.

**Hinter einem idealen Tiefpass**

$$L_g=2N_0f_\mathrm g,\qquad\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$$

Die AKF ist bei $\tau=k/(2f_\mathrm g)$, $k\neq0$, null: Abtastwerte im Abstand der Nyquist-Rate sind unkorreliert.

**Thermisches Rauschen**

$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g$$

Leerlauf, Frequenzbereich $|f|\le f_\mathrm g$, Boltzmann-Konstante $k=1{,}38\cdot10^{-23}$ W s/K; bei 290 K ist $kT\approx4\cdot10^{-21}$ W/Hz. $L_{\max}$ ist die bei Leistungsanpassung höchstens entnehmbare Leistung.

**Rauschen am Kondensator eines RC-Glieds**

$$L=\frac{kT}{C}$$

Unabhängig von $R$: Ein kleinerer Widerstand rauscht weniger pro Hertz, macht das RC-Glied aber breitbandiger. Nur ein größerer Kondensator verringert das Rauschen.
::::

::::lernkarten
:::karte begriff weißes Rauschen
Was versteht man unter weißem Rauschen, und welche AKF hat es?
---
Einen mittelwertfreien Prozess mit derselben Leistungsdichte $\Phi_{ss}(f)=N_0$ bei allen Frequenzen. Seine AKF ist $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$.
--- falsch
Einen mittelwertfreien Prozess, dessen Werte gleichverteilt sind. Seine AKF ist konstant, $\varphi_{ss}(\tau)=N_0$, weil alle Werte gleich wahrscheinlich sind.
--- falsch
Einen Prozess mit der Leistungsdichte $N_0$ nur im hörbaren Bereich und null darüber. Seine AKF ist ein Rechteck der Breite $N_0$ um $\tau=0$.
--- falsch
Einen mittelwertfreien Prozess mit derselben Leistungsdichte $\Phi_{ss}(f)=N_0$ bei allen Frequenzen. Seine AKF ist $\varphi_{ss}(\tau)=N_0$ für alle $\tau$, weil alle Frequenzen gleich stark sind.
:::
:::karte zusammenhang Unkorrelierte Werte
Was bedeutet die AKF $N_0\,\delta(\tau)$ des weißen Rauschens für Werte zu verschiedenen Zeitpunkten?
---
Werte zu verschiedenen Zeiten sind unkorreliert, egal wie nahe sie beieinanderliegen, weil die AKF außer bei $\tau=0$ überall null ist.
--- falsch
Werte zu verschiedenen Zeiten sind gleich, weil die AKF bei $\tau=0$ unendlich groß ist und sich das Signal dadurch nie ändern kann.
--- falsch
Werte zu verschiedenen Zeiten sind nur unkorreliert, wenn sie weiter als eine Sekunde auseinanderliegen; nahe Werte hängen stark zusammen.
--- falsch
Werte zu verschiedenen Zeiten sind abwechselnd positiv und negativ korreliert, weil die AKF um $\tau=0$ schwingt und dabei ihr Vorzeichen wechselt.
:::
:::karte zusammenhang Weißes Rauschen als Grenzmodell
Warum ist weißes Rauschen nur ein Grenzmodell, und welches Rauschen misst man in Wirklichkeit?
---
Weil seine Leistung $\int N_0\mathrm{d} f$ unendlich ist, so wie der Dirac-Impuls nur ein Grenzfall ist. Gemessen wird immer gefiltertes, „farbiges“ Rauschen mit endlicher Leistung.
--- falsch
Weil es nur in der Theorie den Mittelwert null hat; jedes gemessene Rauschen hat einen kleinen Gleichanteil, und erst ohne diesen Gleichanteil wäre es wirklich weiß.
--- falsch
Weil seine Leistung null ist: Die Leistungsdichte $N_0$ ist so klein, dass ihr Integral verschwindet; gemessen wird deshalb nur das Rauschen der Messgeräte.
--- falsch
Weil es sich nur bei sehr tiefen Temperaturen einstellt; bei Raumtemperatur ist jedes Rauschen von vornherein „farbig“ und auf eine Bandbreite begrenzt.
:::
:::karte formel Gefiltertes weißes Rauschen
Welches Leistungsdichtespektrum, welche AKF und welche Leistung hat weißes Rauschen hinter einem LTI-System mit der Impulsantwort $h(t)$?
---
$\Phi_{gg}(f)=N_0|H(f)|^2$, $\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau)$ und $L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f$: Die Leistung ist $N_0$ mal die Energie der Impulsantwort.
--- falsch
$\Phi_{gg}(f)=N_0|H(f)|$, $\varphi_{gg}(\tau)=N_0\,h(\tau)$ und $L_g=N_0\int h(t)\,\mathrm{d} t$: Die Leistung ist $N_0$ mal die Fläche unter der Impulsantwort, also $N_0\,H(0)$.
--- falsch
$\Phi_{gg}(f)=N_0+|H(f)|^2$, $\varphi_{gg}(\tau)=N_0\,\delta(\tau)+\varphi^E_{hh}(\tau)$ und $L_g=N_0+\int|h(t)|^2\mathrm{d} t$: Das System addiert seine eigene Energie zum Rauschen.
--- falsch
$\Phi_{gg}(f)=N_0|H(f)|^2$, $\varphi_{gg}(\tau)=N_0\,\delta(\tau)$ und $L_g=\infty$: Das Filter ändert die Leistungsdichte, aber die Werte bleiben unkorreliert und die Leistung unendlich.
:::
:::karte formel Weißes Rauschen hinter einem idealen Tiefpass
Welche Leistung und welche AKF hat weißes Rauschen hinter einem idealen Tiefpass mit der Grenzfrequenz $f_\mathrm g$?
---
$L_g=2N_0f_\mathrm g$ und $\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$: Die Leistung ist $N_0$ mal die Breite $2f_\mathrm g$ des Durchlassbereichs, und die AKF ist eine si-Funktion.
--- falsch
$L_g=N_0f_\mathrm g$ und $\varphi_{gg}(\tau)=N_0f_\mathrm g\operatorname{rect}(\tau f_\mathrm g)$: Die Leistung ist $N_0$ mal die Grenzfrequenz, und die AKF ist ein Rechteck, so wie der Frequenzgang des Tiefpasses.
--- falsch
$L_g=2N_0f_\mathrm g$ und $\varphi_{gg}(\tau)=2N_0f_\mathrm g\,\delta(\tau)$: Die Leistung wird endlich, aber die AKF bleibt ein Dirac-Impuls, weil das Rauschen im Durchlassbereich weiß bleibt.
--- falsch
$L_g=N_0/(2f_\mathrm g)$ und $\varphi_{gg}(\tau)=N_0\mathrm{e}^{-2f_\mathrm g|\tau|}$: Die Leistung sinkt mit wachsender Bandbreite, weil sich das Rauschen auf mehr Frequenzen verteilt.
:::
:::karte zusammenhang Abtastwerte im Abstand der Nyquist-Rate
Warum sind Abtastwerte von weißem Rauschen hinter einem idealen Tiefpass unkorreliert, wenn man im Abstand der Nyquist-Rate abtastet?
---
Weil die AKF $2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$ an den Stellen $\tau=k/(2f_\mathrm g)$, $k\neq0$, null ist. Genau in diesen Abständen liegen die Abtastwerte zueinander.
--- falsch
Weil das Abtasten jeden Zusammenhang zwischen den Werten zerstört: Abtastwerte eines Zufallssignals sind bei jeder Abtastrate unkorreliert, gleichgültig, welche AKF es hat.
--- falsch
Weil die AKF hinter dem Tiefpass für Verschiebungen ab einem Abtastabstand überall null ist: Es hängen nur Werte zusammen, die näher als ein Abtastabstand beieinanderliegen.
--- falsch
Weil der ideale Tiefpass die Leistungsdichte bei $f_\mathrm g$ verdoppelt und diese Frequenz beim Abtasten gerade herausfällt, sodass nur unkorrelierte Anteile übrig bleiben.
:::
:::karte formel Thermisches Rauschen
Welche Rauschspannung erzeugt ein Widerstand $R$ bei der absoluten Temperatur $T_\mathrm{abs}$ im Leerlauf, gemessen im Frequenzbereich $|f|\le f_\mathrm g$?
---
$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g$ mit der Leistungsdichte $N_0=2kT_\mathrm{abs}R$ und der Boltzmann-Konstanten $k=1{,}38\cdot10^{-23}$ W s/K. Ursache ist die Wärmebewegung der Elektronen.
--- falsch
$\mathrm E\{u^2\}=kT_\mathrm{abs}Rf_\mathrm g$ mit der Leistungsdichte $N_0=kT_\mathrm{abs}R$. Die Rauschspannung entsteht nur, wenn Strom durch den Widerstand fließt; im Leerlauf ist sie null.
--- falsch
$\mathrm E\{u^2\}=4kT_\mathrm{abs}f_\mathrm g/R$ mit der Leistungsdichte $N_0=2kT_\mathrm{abs}/R$: Ein größerer Widerstand rauscht weniger, weil er die Bewegung der Elektronen stärker bremst.
--- falsch
$\mathrm E\{u^2\}=4kT_\mathrm{abs}R$, unabhängig von der Bandbreite, mit $k=1{,}38\cdot10^{-23}$ W s/K: Die Rauschspannung ist eine Eigenschaft des Widerstands und hängt nicht vom Messbereich ab.
:::
:::karte formel Verfügbare Rauschleistung
Welche Rauschleistung kann man einem Widerstand höchstens entnehmen, und wie groß ist sie bei Raumtemperatur?
---
$L_{\max}=kT_\mathrm{abs}f_\mathrm g$, bei Leistungsanpassung und unabhängig vom Widerstandswert. Bei 290 K ist $kT\approx4\cdot10^{-21}$ W/Hz, also 4 pW je GHz Bandbreite.
--- falsch
$L_{\max}=4kT_\mathrm{abs}Rf_\mathrm g$, die volle Leerlaufleistung, die man mit jedem Lastwiderstand entnehmen kann. Bei 290 K sind das etwa 4 mW je GHz Bandbreite.
--- falsch
$L_{\max}=kT_\mathrm{abs}f_\mathrm g/R$, bei Kurzschluss, weil dann der größte Strom fließt. Ein kleiner Widerstand liefert deshalb mehr Rauschleistung als ein großer.
--- falsch
$L_{\max}=kT_\mathrm{abs}$, unabhängig von Widerstand und Bandbreite. Bei 290 K ist das etwa $4\cdot10^{-21}$ W, eine feste Leistung, die jeder Widerstand abgibt.
:::
:::karte zusammenhang Rauschen eines großen Widerstands
Warum ist der Rauscheffektivwert eines Widerstands von $1\,\mathrm{M\Omega}$ bei gleicher Temperatur und Bandbreite etwa 31,6-mal so groß wie der eines Widerstands von $1\,\mathrm{k\Omega}$?
---
Weil $\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g$ proportional zu $R$ ist und der Effektivwert als Wurzel daraus nur mit $\sqrt R$ wächst: $\sqrt{1000}=31{,}6$. Aus 0,57 µ V werden so 17,9 µ V.
--- falsch
Weil der Effektivwert proportional zu $R$ wächst und der Faktor 1000 durch die Bandbreite von 20 kHz auf etwa 31,6 verkleinert wird. Aus 0,57 µ V werden so 17,9 µ V.
--- falsch
Weil die Leistungsdichte mit $R^2$ wächst und der Effektivwert mit $R$ selbst; dass nur der Faktor 31,6 herauskommt, liegt an der höheren Temperatur im großen Widerstand.
--- falsch
Weil bei $1\,\mathrm{M\Omega}$ das flache Spektrum nur bis zu einer tieferen Frequenz reicht, sodass von der 1000-fachen Leistungsdichte nur ein Teil gemessen wird.
:::
:::karte zusammenhang Rauschen am Kondensator eines RC-Glieds
Warum hängt die Rauschleistung am Kondensator eines RC-Glieds nicht vom Widerstand ab?
---
Weil $N_0=2kTR$ zwar mit $R$ wächst, das RC-Glied aber mit $\int h^2\mathrm{d} t=\frac{1}{2RC}$ im gleichen Maß schmalbandiger wird. Beides hebt sich auf, und es bleibt $\frac{kT}{C}$; nur ein größerer Kondensator verringert das Rauschen.
--- falsch
Weil ein Kondensator kein eigenes Rauschen erzeugt und das Rauschen des Widerstands vollständig sperrt. Am Kondensator liegt deshalb nur ein fester Rest, der allein von der Temperatur abhängt, nicht von $C$.
--- falsch
Weil $N_0=2kTR$ mit $R$ wächst und die Bandbreite $1/RC$ ebenfalls; beide Effekte zusammen ergeben eine Leistung, die mit $R^2$ wächst, aber durch den Kondensator genau wieder ausgeglichen wird.
--- falsch
Weil bei einem RC-Glied immer Leistungsanpassung herrscht und dann nach $L_{\max}=kT_\mathrm{abs}f_\mathrm g$ nur Temperatur und Bandbreite zählen. Ein größerer Kondensator ändert daran nichts.
:::
:::karte herleitung Rauschleistung am Kondensator
Wie zeigt man mit $L_g=N_0\int|h(t)|^2\mathrm{d} t$, dass das thermische Rauschen am Kondensator eines RC-Glieds die Leistung $kT/C$ hat?
---
Man nimmt die Impulsantwort $h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$, weil das Rauschen des Widerstands durch das RC-Glied läuft, das er mit dem Kondensator bildet.
---
Man berechnet $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$, weil das Quadrat der Exponentialfunktion doppelt so schnell abklingt.
---
Mit $N_0=2kTR$ folgt $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$, weil die Leistung des gefilterten weißen Rauschens $N_0$ mal die Energie der Impulsantwort ist.
---
Der Widerstand kürzt sich heraus, weil er die Rauschdichte erhöht, aber die Bandbreite $1/RC$ des Glieds im gleichen Maß verringert.
:::
::::
