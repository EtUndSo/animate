---
title: Stufe 3: Wellen bei sinusförmiger Anregung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Orthogonalentwicklung und Leitungen
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Kapitel 8: Orthogonalentwicklung und Leitungen
order: 3280400
summary: Mit Zeigern wird aus den partiellen Differentialgleichungen eine gewöhnliche Gleichung im Ort.
tags: Wellengleichung, Ausbreitungskonstanten, Wellenwiderstand, Dämpfungskonstanten, Reflexionsfaktor
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Mit Zeigern wird aus den partiellen Differentialgleichungen eine gewöhnliche Gleichung im Ort. Ihre Lösung sind zwei gegenläufige Wellen.
:::

Mit $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$ und ebenso für $i$ wird $\frac{\partial}{\partial t}$ zu $\mathrm{j}2\pi f$:

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U.$$

Ableiten der ersten Gleichung und Einsetzen der zweiten ergibt die __Wellengleichung__ $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$.

:::satz Satz 3.1 (Hin- und rücklaufende Welle)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr), \tag{3.1}$$

mit der __Ausbreitungskonstanten__ und dem __Wellenwiderstand__

<span class="anker" id="gl-3-2"></span>
$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}. \tag{3.2}$$
:::

⁠**So liest man das:** Mit $\gamma=\alpha+\mathrm{j}\beta$ wird der erste Summand im Zeitbereich zu $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$: eine Welle, die in Richtung wachsender $s$ läuft und dabei mit der __Dämpfungskonstanten__ $\alpha$ abklingt. Ein Nulldurchgang bewegt sich mit $v=2\pi f/\beta$, die Wellenlänge ist $\lambda=2\pi/\beta$. Der zweite Summand läuft in die Gegenrichtung. $Z$ ist das Verhältnis von Spannung zu Strom in einer einzelnen Welle. Die Randbedingungen legen die Konstanten $\underline U_1$, $\underline U_2$ fest, etwa Spannung und Strom am Anfang: $\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$.

**Reflexion am Ende.** Ist die Leitung am Ende ($s=l$) mit einem Widerstand $R_\mathrm E=\underline U_e/\underline I_e$ abgeschlossen, lässt sich die Spannung schreiben als

<span class="anker" id="gl-3-3"></span>
$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}. \tag{3.3}$$

Der erste Summand ist die hinlaufende, der zweite die vom Ende zurücklaufende Welle. Bei $R_\mathrm E=Z$ verschwindet die rücklaufende Welle: Ein Abschluss mit dem Wellenwiderstand nimmt die ankommende Welle vollständig auf, als ginge die Leitung unendlich weiter. Das Verhältnis der beiden Wellen am Ende ist der __Reflexionsfaktor__ $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$ (Zusatz: Kurzschluss $r=-1$, Leerlauf $r=+1$).

:::frage Warum stört ein falscher Abschluss bei kurzen Leitungen nicht?
Weil die reflektierte Welle dann fast sofort zurück ist. Ist die Laufzeit über die Leitung klein gegen die Dauer der Signaländerungen (Leitung kurz gegen die Wellenlänge), überlagern sich hin- und rücklaufende Welle praktisch gleichzeitig, und man merkt nur den Abschlusswiderstand. Erst wenn die Laufzeit vergleichbar wird, etwa bei schnellen Digitalsignalen oder Hochfrequenz, erscheinen Reflexionen als Echos und verzerren das Signal.
:::
