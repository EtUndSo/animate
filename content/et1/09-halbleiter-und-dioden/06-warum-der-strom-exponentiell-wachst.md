---
title: Stufe 4: Warum der Strom exponentiell wächst
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
order: 1190600
summary: Die Barriere steht.
tags: Sättigungssperrstrom, Temperaturspannung, Dekade, Bahnwiderstand
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Barriere steht. Diese Stufe legt eine äußere Spannung an und zeigt, warum der Strom in einer Richtung exponentiell wächst und in der anderen fast null bleibt.
:::

**Die Idee.** Eine äußere Spannung $U$ zwischen p-Seite (Anode) und n-Seite (Kathode) fällt fast ganz an der Zone ab, denn nur dort fehlen Ladungsträger. Die neutralen Gebiete leiten gut. Die Barriere ändert sich also auf $W_\mathrm B=e(U_\mathrm{D0}-U)$ (Abb. [5](#abb-5)). Über die Zone laufen zwei Elektronenströme:

<ul>

<li>

⁠**Bergauf:** Mehrheitselektronen des n-Gebiets. Nur der Anteil $\mathrm{e}^{-W_\mathrm B/(k_\mathrm BT)}$ kommt über die Barriere. Jedes $k_\mathrm BT$ weniger Barriere vergrößert ihn um den Faktor 2,718.

</li>

<li>

⁠**Bergab:** Minderheitselektronen des p-Gebiets, die an den Zonenrand geraten. Für sie ist die Potenzialstufe ein Gefälle, sie kommen immer durch. Ihre Zahl hängt nicht von der Barriere ab.

</li>

</ul>

Für Löcher gilt dasselbe in Gegenrichtung. Ohne Spannung sind beide Ströme gleich groß, deshalb fließt nichts.

:::abbildung et1/k9barriere 5
Energie eines Elektrons über dem Ort, Punkte: Elektronen, jede höhere Zeile enthält weniger (Verteilung schematisch, die echten Verhältnisse sind viel extremer). Rot: Elektronen über der Barriere $W_\mathrm B$, sie wandern nach links. Der blaue Pfeil oben links ist der Strom der Minderheit bergab, immer gleich groß. Bei $U=0$ heben sich beide Ströme auf.
:::

:::satz Satz 4.1 (Shockley-Gleichung)
<span class="anker" id="satz-4-1"></span>

Für die ideale Diode mit $U$ von Anode nach Kathode und $I$ von Anode nach Kathode gilt

<span class="anker" id="gl-4-1"></span>
$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr),\qquad U_T=\frac{k_\mathrm BT}{e}. \tag{4.1}$$
:::

⁠**So liest man das:** $I_\mathrm S$ ist der __Sättigungssperrstrom__ (kurz Sperrstrom), je nach Fläche und Dotierung $10^{-15}$ bis $10^{-9}$ A. Die __Temperaturspannung__ $U_T$ ist die Wärmeenergie $k_\mathrm BT$ in Volt, geteilt durch $e$, bei 300 K also 25,85 mV. Wichtig ist: $k_\mathrm BT$ allein ist eine Energie, erst $k_\mathrm BT/e$ eine Spannung. Der Faktor 10 (eine __Dekade__) kostet $U_T\ln10=59{,}5$ mV, also rund 60 mV. **Gültigkeit:** [(4.1)](#gl-4-1) gilt für $U<U_\mathrm{D0}$ und ohne Durchbruch (Stufe [5](kennlinie-durchbruch-und-spezialdioden.html#stufe-5)). Im Durchlass reicht $I\approx I_\mathrm S\mathrm{e}^{U/U_T}$.

:::herleitung Von der Barriere zur Kennlinie
<ol>

<li>

Bergauf: Der Strom ist dem Anteil über der Barriere proportional, $I_\text{auf}=c\,\mathrm{e}^{-(U_\mathrm{D0}-U)/U_T}=I_0\,\mathrm{e}^{U/U_T}$. Dabei fasst $I_0=c\,\mathrm{e}^{-U_\mathrm{D0}/U_T}$ alles zusammen, was nicht von $U$ abhängt.

</li>

<li>

Bergab: $I_\text{ab}$ hängt nicht von $U$ ab.

</li>

<li>

Bei $U=0$ fließt kein Strom, also $I_\text{ab}=I_0$. Der Nettostrom ist $I=I_\text{auf}-I_\text{ab}=I_0(\mathrm{e}^{U/U_T}-1)$.

</li>

<li>

Elektronen und Löcher haben dieselbe Barriere, ihre Ströme addieren sich mit demselben Faktor: $I_0$ wird $I_\mathrm S$.

</li>

</ol>

Vereinfachung: Die Größe von $I_\mathrm S$ bestimmt in Wirklichkeit die Diffusion der Minderheit in den neutralen Gebieten hinter der Zone. Der Faktor $\mathrm{e}^{U/U_T}$ bleibt, denn er legt die Trägerdichte am Zonenrand fest.
:::

**Beispiel.** Mit [(4.1)](#gl-4-1) ergibt sich im Rechenmodell:

| $I$ | 1 µ A | 10 µ A | 100 µ A | 1 mA | 10 mA |
|---|---|---|---|---|---|
| $U$ | 0,476 V | 0,536 V | 0,595 V | 0,655 V | 0,714 V |

Bei 0,655 V ist die Barriere auf $2{,}3\,U_T$ geschrumpft, der Anteil von $10^{-12}$ auf 0,1 gestiegen. **Grenzfälle:** Bei $U=0$ ist $I=0$. Für $U\ll-U_T$ bleibt $I=-I_\mathrm S$: Schon bei $-5\,U_T$ sind es 99,3 % davon. Ab $U=119$ mV ist der Summand $-1$ kleiner als 1 % des ersten.

**Sperrrichtung.** Bei $U<0$ wächst die Barriere, und die Zone wird breiter. Der Strom bergauf erlischt, es bleibt nur der Strom der Minderheit. Er hängt nicht davon ab, wie hoch die Barriere ist, nur davon, wie viele Träger an ihren Rand gelangen. Deshalb sättigt er bei $I_\mathrm S$. Reale Dioden sperren mit pA bis nA, weil zusätzlich Paare in der Zone entstehen.

:::ltspice Die Kennlinie der Rechenmodell-Diode
⁠**Zeichnen:** `voltage` namens `V1` von `a` nach Masse, `diode` von `a` nach Masse, Wert `DM`.

⁠**Direktiven:** `.model DM D(Is=1e-14)` und `.dc V1 0 0.8 1m`

⁠**Was du siehst:** `I(D1)` scheint bei 0,6 V zu starten. Stelle die Stromachse logarithmisch: Es wird eine Gerade. Bei 0,6547 V liest du 0,98 mA, bei 0,7142 V 9,8 mA, bei 0,7737 V 98 mA. LTspice rechnet bei 27 °C, daher die 2 % Abweichung von 1, 10 und 100 mA. Prüfe so Aufgabe [4](#aufg-4)(a).
:::

:::frage Was passiert, wenn $U$ größer als $U_\mathrm{D0}$ wird? Ist die Barriere dann weg?
Die Formel gilt dort nicht mehr. Bei so hohem Strom sind die über die Barriere gelangten Träger im fremden Gebiet so dicht wie die Dotierung, und die neutralen Gebiete haben einen merklichen Widerstand (__Bahnwiderstand__, wenige $\Omega$). Der Rest der äußeren Spannung fällt dort ab, die Kennlinie wird flacher und fast gerade. Die Barriere wird nie negativ.
:::

:::zusatz Temperatur
$I_\mathrm S$ enthält $n_\mathrm i^2$ und wächst je 10 K rund um den Faktor 4. Das überwiegt das Wachsen von $U_T$: Bei festem Strom sinkt die Spannung um rund 2 mV/K. Reale Dioden folgen oft $\mathrm{e}^{U/(mU_T)}$ mit $1\le m\le2$.
:::

:::aufgabe Aufgabe 4 ★ Dekaden
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Die Diode des Rechenmodells zeigt 0,655 V bei 1 mA. Schätze ohne Taschenrechner $U$ bei 100 mA und bei 10 µ A.

</li>

<li>

Um wie viel mV steigt $U$, wenn sich der Strom verdoppelt? Wenn er sich verdreifacht?

</li>

<li>

Welcher Strom fließt bei $U=-1$ V und bei $U=-0{,}2$ V?

</li>

</ol>

:::loesung
(a) 100 mA sind zwei Dekaden mehr: $0{,}655\,\mathrm{V}+2\cdot0{,}060\,\mathrm{V}=0{,}775$ V (exakt 0,774 V). 10 µ A sind zwei Dekaden weniger: 0,535 V (exakt 0,536 V). (b) Verdoppeln: $U_T\ln2=17{,}9$ mV. Verdreifachen: $U_T\ln3=28{,}4$ mV. (c) Bei $-1$ V ist $\mathrm{e}^{U/U_T}\approx0$, also $I=-10^{-14}$ A. Bei $-0{,}2$ V ist $\mathrm{e}^{-7{,}7}=4{,}4\cdot10^{-4}$, also ebenfalls $I=-10^{-14}$ A auf 0,05 % genau.
:::
:::
