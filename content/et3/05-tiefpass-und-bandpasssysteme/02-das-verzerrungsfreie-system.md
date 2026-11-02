---
title: Stufe 1: Das verzerrungsfreie System
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250200
summary: Was genau soll eine „gute“ Übertragung leisten?
tags: Phasenlaufzeit, Gruppenlaufzeit
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Was genau soll eine „gute“ Übertragung leisten? Und mit welchen Kenngrößen misst man, wie weit ein System davon abweicht?
:::

**Die Idee.** Ein Signal ist unverzerrt angekommen, wenn es nur lauter oder leiser und später ist, seine Form aber gleich:

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

Im Spektrum heißt das: Jede Schwingung wird mit demselben Faktor $h_0$ multipliziert, und jede wird um dieselbe Zeit $t_0$ verschoben. Eine Zeitverschiebung $t_0$ ist bei der Frequenz $f$ der Winkel $2\pi ft_0$. Deshalb muss die Phase $\varphi(f)=-2\pi t_0f$ eine Gerade durch den Ursprung sein.

:::definition Definition 1.1 (Kenngrößen eines LTI-Systems)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{Dämpfungsmaß:} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{bzw.}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{Dämpfungswinkel:} && b(f)=-\varphi(f),\\ &\text{Phasenlaufzeit:} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{Gruppenlaufzeit:} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**So liest man das:** Die __Phasenlaufzeit__ ist die Verzögerung einer einzelnen Schwingung der Frequenz $f$. Die __Gruppenlaufzeit__ ist die Verzögerung einer Gruppe benachbarter Frequenzen, also einer Hüllkurve (Stufe [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11)). Beim verzerrungsfreien System sind $a$, $t_\mathrm p$ und $t_\mathrm g$ konstant und $t_\mathrm p=t_\mathrm g=t_0$.

**Beispiel: das RC-Glied.** Mit $\varphi=-\arctan(2\pi f\,RC)$ und $RC=1$ s:

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

Für $f\to0$ sind beide $RC=1$ s. Bei $f=0{,}159$ Hz ($2\pi fRC=1$) ist $t_\mathrm p=0{,}785$ s, $t_\mathrm g=0{,}5$ s und $a=3{,}0$ dB. Das RC-Glied ist also nicht verzerrungsfrei: Es dämpft frequenzabhängig, und verschiedene Frequenzen kommen verschieden spät an.

:::ltspice Dämpfung und Laufzeiten des RC-Glieds ablesen
⁠**Zeichnen:** RC-Glied (`res` mit `1Meg`, `cap` mit `1u`), Quellwert `AC 1`, Direktive `.ac dec 100 0.01 10`.

⁠**Ablesen:** Die linke Achse zeigt $20\lg|H|=-a$ in dB. Fahre mit der Maus auf die rechte Achse (Phase), bis der Zeiger zum Lineal wird, klicke und wähle „Group Delay“: Dann zeigt sie $t_\mathrm g(f)$ nach [(1.5)](#gl-1-5). Die Phasenlaufzeit rechnest du aus der Phase, $t_\mathrm p=-\varphi/(2\pi f)$ mit $\varphi$ im Bogenmaß.

⁠**Was du siehst:** Zu tiefen Frequenzen hin strebt $t_\mathrm g$ gegen 1 s. Bei 0,159 Hz liest du $a=3{,}0$ dB, $\varphi=-45^\circ$ und $t_\mathrm g=0{,}5$ s ab, daraus $t_\mathrm p=0{,}785$ s. Vergleiche die Werte bei $2\pi fRC=10$ mit deinem Ergebnis aus Aufgabe [1](#aufg-1)(b).
:::

:::aufgabe Aufgabe 1 ★ Laufzeiten des RC-Glieds
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Leite $t_\mathrm g$ des RC-Glieds aus [(1.5)](#gl-1-5) her.

</li>

<li>

Berechne $t_\mathrm p$, $t_\mathrm g$ und $a$ bei $2\pi fRC=10$. In welchem Frequenzbereich ist das RC-Glied näherungsweise verzerrungsfrei?

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$, $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$, also $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$.

(b) Bei $2\pi fRC=10$: $t_\mathrm p=\frac{\arctan10}{10}RC=0{,}147$ s, $t_\mathrm g=\frac{RC}{101}=0{,}0099$ s, $a=20{,}0$ dB. Näherungsweise verzerrungsfrei ist das RC-Glied nur für $2\pi fRC\ll1$, also weit unter 0,16 Hz: Dort ist $|H|\approx1$ und $t_\mathrm p\approx t_\mathrm g\approx RC$.
:::
:::
