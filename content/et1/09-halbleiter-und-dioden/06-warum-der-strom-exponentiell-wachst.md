---
title: Stufe 4: Warum der Strom exponentiell wächst
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
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

::::beispiel
Mit [(4.1)](#gl-4-1) ergibt sich im Rechenmodell:

| $I$ | 1 µ A | 10 µ A | 100 µ A | 1 mA | 10 mA |
|---|---|---|---|---|---|
| $U$ | 0,476 V | 0,536 V | 0,595 V | 0,655 V | 0,714 V |

Bei 0,655 V ist die Barriere auf $2{,}3\,U_T$ geschrumpft, der Anteil von $10^{-12}$ auf 0,1 gestiegen.
::::

⁠**Grenzfälle:** Bei $U=0$ ist $I=0$. Für $U\ll-U_T$ bleibt $I=-I_\mathrm S$: Schon bei $-5\,U_T$ sind es 99,3 % davon. Ab $U=119$ mV ist der Summand $-1$ kleiner als 1 % des ersten.

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

::::formelsammlung
**Barriere mit äußerer Spannung**

$$W_\mathrm B=e(U_\mathrm{D0}-U)$$

$U$ von der p-Seite (Anode) zur n-Seite (Kathode); sie fällt fast ganz an der Zone ab. Spannung in Durchlassrichtung senkt die Barriere.

**Shockley-Gleichung**

$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr),\qquad U_T=\frac{k_\mathrm BT}{e}$$

Ideale Diode, $U$ und $I$ von Anode nach Kathode. $I_\mathrm S$ ist der Sättigungssperrstrom, je nach Fläche und Dotierung $10^{-15}$ bis $10^{-9}$ A; $U_T$ die Temperaturspannung, bei 300 K 25,85 mV. Gilt für $U<U_\mathrm{D0}$ und ohne Durchbruch. In Sperrrichtung ($U\ll-U_T$) bleibt $I=-I_\mathrm S$.

**Näherung im Durchlass**

$$I\approx I_\mathrm S\mathrm{e}^{U/U_T}$$

Ab $U=119$ mV ist der Summand $-1$ kleiner als 1 % des ersten.

**Spannung je Dekade**

$$U_T\ln10=59{,}5\,\mathrm{mV}$$

Spannungszuwachs für den Faktor 10 im Strom, also rund 60 mV je Dekade.

**Reale Dioden**

$$\mathrm{e}^{U/(mU_T)},\qquad 1\le m\le2$$

Reale Dioden folgen oft diesem Faktor statt $\mathrm{e}^{U/U_T}$. $I_\mathrm S$ wächst je 10 K rund um den Faktor 4; bei festem Strom sinkt die Spannung um rund 2 mV/K.
::::

::::lernkarten
:::karte zusammenhang Spannung an der Raumladungszone
Warum fällt eine äußere Spannung an der Diode fast ganz an der Raumladungszone ab, und wie ändert sie die Barriere?
---
Nur in der Zone fehlen Ladungsträger, die neutralen Gebiete leiten gut. Die Barriere ändert sich deshalb auf $W_\mathrm B=e(U_\mathrm{D0}-U)$: Spannung in Durchlassrichtung senkt sie.
--- falsch
Die Zone ist der dünnste Teil der Diode, und an dünnen Schichten fällt immer die meiste Spannung ab. Die Barriere ändert sich auf $W_\mathrm B=e(U_\mathrm{D0}+U)$, Durchlassspannung erhöht sie.
--- falsch
Nur in der Zone gibt es bewegliche Träger, die neutralen Gebiete sind leer und isolieren. Die Barriere bleibt dabei fest bei $e\,U_\mathrm{D0}$, nur der Strom über sie ändert sich.
--- falsch
Die äußere Spannung verteilt sich gleichmäßig auf die ganze Diode, und die Zone erhält nur ihren Anteil. Die Barriere ändert sich deshalb nur um wenige Prozent von $U$.
:::
:::karte zusammenhang Zwei Ströme über die Barriere
Welche zwei Elektronenströme laufen über die Raumladungszone, und warum fließt ohne äußere Spannung kein Strom?
---
Bergauf die Mehrheitselektronen des n-Gebiets, von denen nur der Anteil $\mathrm{e}^{-W_\mathrm B/(k_\mathrm BT)}$ über die Barriere kommt; bergab die Minderheitselektronen des p-Gebiets, die immer durchkommen. Ohne Spannung sind beide gleich groß.
--- falsch
Bergauf die Minderheitselektronen des p-Gebiets, deren Zahl mit der Barriere sinkt; bergab die Mehrheitselektronen des n-Gebiets, die immer durchkommen. Ohne Spannung sind beide null, weil die Zone alle Träger fernhält.
--- falsch
Bergauf die Mehrheitselektronen des n-Gebiets, bergab die Löcher des p-Gebiets; beide sind bei jeder Spannung gleich groß. Ohne Spannung fließt nichts, weil die Zone dann alle Träger einfängt.
--- falsch
Ein Strom der Elektronen und ein gleich großer Strom der Ionen in Gegenrichtung. Ohne Spannung bleiben die Ionen fest, und beide Ströme sind deshalb null.
:::
:::karte formel Shockley-Gleichung
Wie lautet die Shockley-Gleichung für den Strom einer idealen Diode, und in welchen Richtungen zählen $U$ und $I$?
---
$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)$ mit $U_T=\frac{k_\mathrm BT}{e}$; $U$ und $I$ zählen von Anode nach Kathode. Gilt für $U<U_\mathrm{D0}$ und ohne Durchbruch.
--- falsch
$I=I_\mathrm S\,\mathrm{e}^{-U/U_T}$ mit $U_T=\frac{k_\mathrm BT}{e}$; $U$ und $I$ zählen von Kathode nach Anode. Gilt für alle Spannungen, auch im Durchbruch.
--- falsch
$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)$ mit $U_T=\frac{k_\mathrm BT}{e}$; $U$ zählt von Anode nach Kathode, $I$ von Kathode nach Anode. Gilt nur für $U>U_\mathrm{D0}$.
--- falsch
$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}+1\bigr)$ mit $U_T=k_\mathrm BT$; $U$ und $I$ zählen von Anode nach Kathode. Gilt für $U<U_\mathrm{D0}$ und ohne Durchbruch.
:::
:::karte herleitung Von der Barriere zur Kennlinie
Wie folgt aus den beiden Strömen über die Barriere die Shockley-Gleichung $I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)$?
---
Bergauf gilt $I_\text{auf}=c\,\mathrm{e}^{-(U_\mathrm{D0}-U)/U_T}=I_0\,\mathrm{e}^{U/U_T}$, weil der Strom dem Anteil über der auf $e(U_\mathrm{D0}-U)$ gesenkten Barriere proportional ist.
---
Der Strom bergab $I_\text{ab}$ hängt nicht von $U$ ab, weil die Potenzialstufe für die Minderheit ein Gefälle ist.
---
Bei $U=0$ fließt kein Strom, also ist $I_\text{ab}=I_0$ und $I=I_\text{auf}-I_\text{ab}=I_0(\mathrm{e}^{U/U_T}-1)$, weil sich beide Ströme ohne Spannung genau aufheben.
---
Für Elektronen und Löcher addieren sich die Ströme mit demselben Faktor, und $I_0$ wird $I_\mathrm S$, weil beide Sorten dieselbe Barriere sehen.
:::
:::karte begriff Sättigungssperrstrom
Was gibt der Sättigungssperrstrom $I_\mathrm S$ in der Shockley-Gleichung an, und in welchem Bereich liegt er?
---
Den winzigen Strom, der in Sperrrichtung übrig bleibt, $I=-I_\mathrm S$. Er hängt von Fläche und Dotierung ab und liegt bei $10^{-15}$ bis $10^{-9}$ A.
--- falsch
Den größten Strom, den die Diode in Durchlassrichtung führen kann, bevor sie sättigt. Er hängt von der Fläche ab und liegt bei 1 bis 10 A.
--- falsch
Den Strom, ab dem die Diode in Durchlassrichtung zu leiten beginnt. Er liegt bei 1 mA und legt die Schwelle von 0,6 V fest.
--- falsch
Den winzigen Strom, der in Sperrrichtung fließt. Er wächst mit der Sperrspannung linear an und erreicht bei 1 V Sperrspannung $10^{-3}$ A.
:::
:::karte begriff Temperaturspannung
Was ist die Temperaturspannung $U_T$, und warum ist sie nicht dasselbe wie $k_\mathrm BT$?
---
Die Wärmeenergie $k_\mathrm BT$ geteilt durch $e$, also $U_T=k_\mathrm BT/e$, bei 300 K 25,85 mV. $k_\mathrm BT$ allein ist eine Energie, erst $k_\mathrm BT/e$ eine Spannung.
--- falsch
Die Spannung, die eine Diode bei 300 K in Durchlassrichtung hält, rund 0,7 V. Sie ist dasselbe wie $k_\mathrm BT$, nur in Volt statt in Joule geschrieben.
--- falsch
Die Wärmeenergie $k_\mathrm BT$ mal $e$, also $U_T=e\,k_\mathrm BT$, bei 300 K 25,85 mV. Der Faktor $e$ macht aus der Energie eine Spannung.
--- falsch
Die Spannung, um die sich die Diodenspannung je Kelvin ändert, rund 2 mV/K. Sie ist dasselbe wie $k_\mathrm B$, nur auf die Ladung eines Elektrons bezogen.
:::
:::karte begriff Dekade
Was ist eine Dekade des Diodenstroms, und welche Spannungsänderung kostet sie nach der Shockley-Gleichung?
---
Eine Änderung des Stroms um den Faktor 10. Sie kostet $U_T\ln10=59{,}5$ mV, also rund 60 mV, gleich bei welchem Strom, weil der Strom exponentiell mit der Spannung wächst.
--- falsch
Eine Änderung des Stroms um den Faktor 10. Sie kostet 0,7 V, die Durchlassspannung einer Siliziumdiode, weil jede Dekade die Barriere neu überwinden muss.
--- falsch
Eine Änderung des Stroms um den Faktor 2,718. Sie kostet genau 25,85 mV, also eine Temperaturspannung, weil der Strom exponentiell mit $U/U_T$ wächst.
--- falsch
Eine Änderung des Stroms um zehn Prozent. Sie kostet nur wenige Millivolt, rund 2,5 mV, weil die Kennlinie im Durchlass sehr steil ist.
:::
:::karte zusammenhang Spannung bei hundertfachem Strom
Eine Diode zeigt 0,655 V bei 1 mA. Welche Spannung erwartet man bei 100 mA, und warum genügt dafür eine Kopfrechnung?
---
Rund 0,775 V, exakt 0,774 V: 100 mA sind zwei Dekaden mehr, und jede Dekade kostet rund 60 mV.
--- falsch
Rund 65,5 V, weil die Spannung wie bei einem Widerstand proportional zum Strom wächst und der Strom hundertmal größer ist.
--- falsch
Rund 0,715 V, weil 100 mA eine Dekade mehr sind als 1 mA und jede Dekade rund 60 mV kostet.
--- falsch
Rund 0,775 V, weil die Spannung je Milliampere Strom um 1,2 mV steigt und das für 99 mA mehr gut 0,12 V ergibt.
:::
:::karte zusammenhang Sättigung in Sperrrichtung
Warum bleibt der Strom in Sperrrichtung bei $-I_\mathrm S$ stehen, auch wenn die Sperrspannung weiter wächst?
---
Die Barriere wächst, und der Strom bergauf erlischt. Es bleibt nur der Strom der Minderheit bergab; er hängt nicht von der Höhe der Barriere ab, nur davon, wie viele Träger an ihren Rand gelangen.
--- falsch
Die Zone wird mit der Sperrspannung so breit, dass sie die ganze Diode füllt. Danach kann sie nicht weiter wachsen, und der Strom bleibt bei dem Wert stehen, den diese größte Breite vorgibt.
--- falsch
Die Minderheitsträger werden von der steigenden Barriere zunehmend gebremst, und der Strom bergauf wächst im Gegenzug. Beide Änderungen heben sich bei jeder Sperrspannung genau auf.
--- falsch
Die Sperrspannung lädt die Zone wie einen Kondensator auf. Sobald er voll ist, fließt nur noch ein Leckstrom $I_\mathrm S$, der allein vom Material der Kontakte abhängt.
:::
:::karte zusammenhang Näherung im Durchlass
Ab welcher Spannung darf man die Shockley-Gleichung im Durchlass durch $I\approx I_\mathrm S\mathrm{e}^{U/U_T}$ ersetzen, und warum?
---
Ab $U=119$ mV ist der Summand $-1$ kleiner als 1 % des ersten Glieds, denn $\mathrm{e}^{U/U_T}$ erreicht dort rund 100. Im üblichen Durchlass ist der Fehler verschwindend klein.
--- falsch
Erst ab $U=U_\mathrm{D0}$, weil die Barriere dort verschwindet und der Summand $-1$ den Strom der Minderheit beschreibt, der erst dann gegen den Strom bergauf vernachlässigbar wird.
--- falsch
Ab $U=0$, weil der Summand $-1$ nur in Sperrrichtung eine Bedeutung hat und im Durchlass bei jeder Spannung wegfällt.
--- falsch
Ab $U=0{,}6$ V, weil die Diode dort zu leiten beginnt; darunter fließt kein Strom, und die Gleichung gilt dort nicht.
:::
:::karte begriff Bahnwiderstand
Was ist der Bahnwiderstand einer Diode, und wann macht er sich bemerkbar?
---
Der Widerstand der neutralen Gebiete, wenige $\Omega$. Bei hohem Strom, wenn $U$ in die Nähe von $U_\mathrm{D0}$ kommt, fällt an ihm ein Teil der äußeren Spannung ab, und die Kennlinie wird flacher und fast gerade.
--- falsch
Der Widerstand der Raumladungszone in Sperrrichtung, einige G$\Omega$. Er macht sich bei hoher Sperrspannung bemerkbar, wenn der Strom kurz vor dem Durchbruch allein durch ihn begrenzt wird und die Kennlinie abknickt.
--- falsch
Der Widerstand der Anschlussdrähte, der bei sehr kleinem Strom die Kennlinie bestimmt, weil die Zone dann noch kaum Spannung aufnimmt und der Draht den Rest trägt.
--- falsch
Der Widerstand der neutralen Gebiete, wenige $\Omega$. Bei hohem Strom senkt er die Barriere unter null, sodass die Kennlinie dort steiler als exponentiell ansteigt.
:::
:::karte zusammenhang Erwärmte Diode
Was passiert mit der Diodenspannung bei festem Strom, wenn sich die Diode erwärmt?
---
Sie sinkt um rund 2 mV/K. $I_\mathrm S$ enthält $n_\mathrm i^2$ und wächst je 10 K rund um den Faktor 4; das überwiegt das Wachsen von $U_T$.
--- falsch
Sie steigt um rund 2 mV/K, weil $U_T=k_\mathrm BT/e$ mit der Temperatur wächst und für denselben Exponenten mehr Spannung nötig ist.
--- falsch
Sie bleibt gleich, weil $I_\mathrm S$ und $U_T$ mit der Temperatur genau gleich schnell wachsen und sich ihre Wirkungen aufheben.
--- falsch
Sie sinkt um rund 60 mV/K, weil sich $I_\mathrm S$ je Kelvin verzehnfacht und jede Dekade des Stroms rund 60 mV kostet.
:::
::::
