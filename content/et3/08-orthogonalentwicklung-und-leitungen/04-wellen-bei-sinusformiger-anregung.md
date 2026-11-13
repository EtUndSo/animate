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

::::formelsammlung
**Leitungsgleichungen mit Zeigern**

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U$$

Für sinusförmige Anregung mit $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$, ebenso für $i$: $\frac{\partial}{\partial t}$ wird zu $\mathrm{j}2\pi f$.

**Wellengleichung**

$$\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$$

Erste Zeigergleichung nach $s$ ableiten und die zweite einsetzen.

**Hin- und rücklaufende Welle**

$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr)$$

Allgemeine Lösung; die Randbedingungen legen die Konstanten $\underline U_1$, $\underline U_2$ fest.

**Ausbreitungskonstante und Wellenwiderstand**

$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}$$

$\alpha$ ist die Dämpfungskonstante. $Z$ ist das Verhältnis von Spannung zu Strom in einer einzelnen Welle.

**Welle im Zeitbereich**

$$\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$$

Erster Summand von $\underline U(s)$: eine Welle, die in Richtung wachsender $s$ läuft und mit der Dämpfungskonstanten $\alpha$ abklingt; der zweite Summand läuft in die Gegenrichtung.

**Geschwindigkeit und Wellenlänge**

$$v=2\pi f/\beta,\qquad\lambda=2\pi/\beta$$

$v$ ist die Geschwindigkeit, mit der sich ein Nulldurchgang der Welle bewegt.

**Konstanten aus dem Anfang der Leitung**

$$\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$$

Aus Spannung $\underline U_a$ und Strom $\underline I_a$ am Anfang $s=0$; Pluszeichen für die hinlaufende, Minuszeichen für die rücklaufende Welle.

**Spannung bei Abschluss am Ende**

$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}$$

Leitung am Ende $s=l$ mit $R_\mathrm E=\underline U_e/\underline I_e$ abgeschlossen. Der erste Summand ist die hinlaufende, der zweite die vom Ende zurücklaufende Welle.

**Reflexionsfaktor**

$$r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$$

Verhältnis der rücklaufenden zur hinlaufenden Welle am Ende. Bei $R_\mathrm E=Z$ keine rücklaufende Welle; Kurzschluss $r=-1$, Leerlauf $r=+1$.
::::

::::lernkarten
:::karte zusammenhang Rechnen mit Zeigern
Warum werden die Leitungsgleichungen bei sinusförmiger Anregung zu gewöhnlichen Differentialgleichungen im Ort?
---
Weil man mit $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$ die ganze Zeitabhängigkeit in den Faktor $\mathrm{e}^{\mathrm{j}2\pi ft}$ legt. Die Ableitung $\frac{\partial}{\partial t}$ wird dann zur Multiplikation mit $\mathrm{j}2\pi f$, und nur der Ort bleibt.
--- falsch
Weil Spannung und Strom bei sinusförmiger Anregung an jedem Ort gleich groß sind. Die Ableitung nach dem Ort verschwindet deshalb, und in den Gleichungen bleibt nur die Abhängigkeit von der Zeit übrig.
--- falsch
Weil man die Leitung bei einer festen Frequenz als kurz ansehen darf. Dann ist die Laufzeit null, die Zeitableitung fällt aus beiden Gleichungen heraus, und es bleibt nur die Abhängigkeit vom Ort.
--- falsch
Weil man mit Zeigern die ganze Ortsabhängigkeit in den Faktor $\mathrm{e}^{\mathrm{j}2\pi ft}$ legt. Die Ableitung $\frac{\partial}{\partial s}$ wird dann zur Multiplikation mit $\mathrm{j}2\pi f$, und in den Gleichungen bleibt nur die Zeit.
:::
:::karte begriff Wellengleichung
Welche Gleichung bezeichnet man als Wellengleichung für den Spannungszeiger $\underline U(s)$ auf einer Leitung?
---
Die Differentialgleichung zweiter Ordnung $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$, in der nur noch die Spannung vorkommt. Ihre Lösungen sind die hin- und die rücklaufende Welle.
--- falsch
Die Differentialgleichung erster Ordnung $\frac{\mathrm{d}\underline U}{\mathrm{d} s}=\gamma\underline I$, in der Spannung und Strom gemeinsam vorkommen. Man erhält sie, indem man die beiden Zeigergleichungen addiert.
--- falsch
Die Differentialgleichung $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=-\gamma^2\underline U$, deren Lösungen reine Schwingungen im Ort ohne Abklingen sind, gleich wie groß die Verluste der Leitung sind.
--- falsch
Die Gleichung $\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}$ für eine einzelne Welle. Sie gilt, wenn man die Leitung am Ende offen lässt, sodass keine Welle zurücklaufen kann.
:::
:::karte herleitung Wellengleichung für den Spannungszeiger
Wie folgt aus den Leitungsgleichungen bei sinusförmiger Anregung die Wellengleichung $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$?
---
Mit $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$ und ebenso für $i$ wird $\frac{\partial}{\partial t}$ zu $\mathrm{j}2\pi f$, weil die Zeit nur noch im Faktor $\mathrm{e}^{\mathrm{j}2\pi ft}$ steht: $\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I$ und $\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U$.
---
Man leitet die erste Gleichung nach $s$ ab, $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=-(R'+\mathrm{j}2\pi fL')\frac{\mathrm{d}\underline I}{\mathrm{d} s}$, weil die Beläge einer gleichförmigen Leitung nicht vom Ort abhängen.
---
Man setzt die zweite Gleichung für $\frac{\mathrm{d}\underline I}{\mathrm{d} s}$ ein und erhält $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$, weil $\gamma^2=(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')$ genau das Produkt der beiden Klammern ist.
:::
:::karte formel Hin- und rücklaufende Welle
Wie lauten Spannungs- und Stromzeiger auf einer Leitung bei sinusförmiger Anregung allgemein?
---
$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$ und $\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr)$: eine hin- und eine rücklaufende Welle; die Randbedingungen legen $\underline U_1$, $\underline U_2$ fest.
--- falsch
$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$ und $\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}\bigr)$: Spannung und Strom haben in beiden Wellen dasselbe Vorzeichen.
--- falsch
$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}$ und $\underline I(s)=\underline U_1\mathrm{e}^{-\gamma s}/Z$: Es gibt nur eine Welle vom Anfang zum Ende; eine Welle in Gegenrichtung ist auf einer Leitung mit Verlusten nicht möglich.
--- falsch
$\underline U(s)=\underline U_1\cos(\gamma s)+\underline U_2\sin(\gamma s)$ und $\underline I(s)=Z\bigl(\underline U_1\sin(\gamma s)-\underline U_2\cos(\gamma s)\bigr)$: eine stehende Schwingung im Ort.
:::
:::karte begriff Ausbreitungskonstante
Was ist die Ausbreitungskonstante $\gamma$ einer Leitung, und wie hängt sie von den Leitungsbelägen ab?
---
Die komplexe Größe im Exponenten der beiden Wellen: $\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta$. Ihr Realteil beschreibt das Abklingen, ihr Imaginärteil bestimmt die Wellenlänge $\lambda=2\pi/\beta$.
--- falsch
Die reelle Größe $\gamma=\sqrt{L'C'}$, die angibt, wie schnell sich die Welle ausbreitet. Sie hängt nur von Induktivität und Kapazität ab, nicht von den Verlusten $R'$, $G'$ oder von der Frequenz.
--- falsch
Die komplexe Größe $\gamma=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}$ im Exponenten der beiden Wellen. Ihr Realteil beschreibt das Abklingen, ihr Imaginärteil bestimmt die Wellenlänge.
--- falsch
Die komplexe Größe $\gamma=(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')$ im Exponenten der beiden Wellen. Ihr Realteil bestimmt die Wellenlänge, ihr Imaginärteil beschreibt das Abklingen.
:::
:::karte begriff Wellenwiderstand
Was gibt der Wellenwiderstand $Z$ einer Leitung an, und wie berechnet man ihn aus den Leitungsbelägen?
---
Das Verhältnis von Spannung zu Strom in einer einzelnen Welle: $Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}$. Er hängt nur von den Leitungsbelägen und der Frequenz ab, nicht von der Länge.
--- falsch
Den ohmschen Widerstand der ganzen Leitung, $Z=R'l$. Er wächst mit der Länge der Leitung, weil der Strom einen längeren Weg durch Hin- und Rückleiter zurücklegen muss.
--- falsch
Das Verhältnis von Spannung zu Strom am Anfang der Leitung, $Z=\underline U_a/\underline I_a$. Er hängt deshalb vom Widerstand ab, mit dem die Leitung am Ende abgeschlossen ist.
--- falsch
Das Verhältnis von Spannung zu Strom in einer einzelnen Welle: $Z=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}$, also das Produkt aus Längs- und Querbelägen unter einer gemeinsamen Wurzel.
:::
:::karte begriff Dämpfungskonstante
Was beschreibt die Dämpfungskonstante $\alpha$ einer Welle auf einer Leitung?
---
Sie ist der Realteil der Ausbreitungskonstanten $\gamma=\alpha+\mathrm{j}\beta$ und gibt an, wie schnell die Amplitude einer Welle mit dem Ort abklingt: Die hinlaufende Welle enthält den Faktor $\mathrm{e}^{-\alpha s}$.
--- falsch
Sie ist der Imaginärteil der Ausbreitungskonstanten $\gamma=\alpha+\mathrm{j}\beta$ und gibt an, um welchen Winkel sich die Phase einer Welle auf jedem Meter Leitung weiterdreht.
--- falsch
Sie ist der Realteil des Wellenwiderstands $Z$ und gibt an, welcher Anteil der ankommenden Leistung im Abschlusswiderstand am Ende der Leitung in Wärme umgesetzt wird.
--- falsch
Sie ist der Realteil der Ausbreitungskonstanten $\gamma=\alpha+\mathrm{j}\beta$ und gibt an, wie schnell eine Welle an einem festen Ort mit der Zeit abklingt, nachdem man die Quelle abgeschaltet hat.
:::
:::karte formel Geschwindigkeit und Wellenlänge
Wie hängen die Geschwindigkeit $v$ und die Wellenlänge $\lambda$ einer Welle auf der Leitung mit $\beta$ zusammen?
---
$v=2\pi f/\beta$ und $\lambda=2\pi/\beta$. Mit dieser Geschwindigkeit bewegt sich ein Nulldurchgang der Welle $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$ in Richtung wachsender $s$.
--- falsch
$v=\beta/(2\pi f)$ und $\lambda=\beta/(2\pi)$. Je größer $\beta$, desto schneller läuft die Welle, weil sich ihre Phase dann auf jedem Meter Leitung stärker dreht und sie so weiter vorankommt.
--- falsch
$v=2\pi f/\alpha$ und $\lambda=2\pi/\alpha$. Die Geschwindigkeit folgt aus der Dämpfungskonstanten, weil sich eine stark gedämpfte Welle nur langsam entlang der Leitung ausbreitet.
--- falsch
$v=2\pi f/\beta$ und $\lambda=2\pi f/\beta$. Geschwindigkeit und Wellenlänge sind auf der Leitung dieselbe Größe, weil beide angeben, wie weit die Welle während einer Schwingung kommt.
:::
:::karte formel Konstanten aus dem Anfang der Leitung
Wie bestimmt man die Konstanten $\underline U_1$ und $\underline U_2$ der beiden Wellen aus Spannung $\underline U_a$ und Strom $\underline I_a$ am Anfang der Leitung?
---
$\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$: Die Randbedingungen am Anfang legen beide Konstanten fest. Das Pluszeichen gehört zur hinlaufenden, das Minuszeichen zur rücklaufenden Welle.
--- falsch
$\underline U_{1,2}=\frac12(\underline U_a\pm\underline I_a/Z)$: Die Randbedingungen am Anfang legen beide Konstanten fest; der Strom wird dazu durch den Wellenwiderstand geteilt, damit eine Spannung entsteht.
--- falsch
$\underline U_1=\underline U_a$ und $\underline U_2=0$: Am Anfang gibt es nur die hinlaufende Welle, weil die rücklaufende erst am Ende der Leitung entsteht und den Anfang nie erreicht.
--- falsch
$\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$: Das Minuszeichen gehört zur hinlaufenden, das Pluszeichen zur rücklaufenden Welle, weil diese dem Strom am Anfang entgegenläuft.
:::
:::karte formel Reflexion am Ende
Wie lässt sich die Spannung auf einer Leitung schreiben, die am Ende $s=l$ mit dem Widerstand $R_\mathrm E=\underline U_e/\underline I_e$ abgeschlossen ist?
---
$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}$. Der erste Summand ist die hinlaufende, der zweite die vom Ende zurücklaufende Welle.
--- falsch
$\underline U(s)=\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}$. Der erste Summand ist die hinlaufende, der zweite die vom Ende zurücklaufende Welle.
--- falsch
$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}$. Der erste Summand ist die zurücklaufende, der zweite die hinlaufende Welle, weil $l-s$ zum Ende hin abnimmt.
--- falsch
$\underline U(s)=R_\mathrm E\,\underline I_e\,\mathrm{e}^{-\gamma s}$: Es gibt nur eine Welle, deren Höhe der Abschluss so festlegt, dass am Ende der Leitung genau $\underline U_e=R_\mathrm E\underline I_e$ gilt, gleich welchen Wert $R_\mathrm E$ hat.
:::
:::karte begriff Reflexionsfaktor
Was gibt der Reflexionsfaktor $r$ am Ende einer Leitung an, und wie hängt er vom Abschlusswiderstand ab?
---
Das Verhältnis der rücklaufenden zur hinlaufenden Welle am Ende: $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$. Bei Kurzschluss ist $r=-1$, bei Leerlauf $r=+1$, bei Abschluss mit $Z$ ist $r=0$.
--- falsch
Das Verhältnis der hinlaufenden zur rücklaufenden Welle am Ende: $r=\frac{R_\mathrm E+Z}{R_\mathrm E-Z}$. Bei Abschluss mit $Z$ wird $r$ unendlich groß, weil dann die ganze Welle zurückläuft.
--- falsch
Das Verhältnis der rücklaufenden zur hinlaufenden Welle am Ende: $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$. Bei Kurzschluss ist $r=+1$, bei Leerlauf $r=-1$, bei Abschluss mit $Z$ ist $r=0$.
--- falsch
Den Anteil der Spannung, der am Abschluss ankommt: $r=\frac{R_\mathrm E}{R_\mathrm E+Z}$. Bei Kurzschluss ist $r=0$, bei Leerlauf $r=1$, bei Abschluss mit $Z$ ist $r=\frac12$.
:::
:::karte zusammenhang Abschluss mit dem Wellenwiderstand
Warum entsteht keine rücklaufende Welle, wenn man eine Leitung mit ihrem Wellenwiderstand abschließt?
---
Weil der Abschluss dann dasselbe Verhältnis von Spannung zu Strom verlangt, das die hinlaufende Welle schon hat. Er nimmt die Welle ganz auf, als ginge die Leitung unendlich weiter.
--- falsch
Weil der Wellenwiderstand die größte Leistung aufnimmt, die eine Quelle abgeben kann. Die rücklaufende Welle wird deshalb im Abschluss in Wärme umgewandelt, bevor sie entstehen kann.
--- falsch
Weil die Leitung bei diesem Abschluss keinen Strom mehr führt. Ohne Strom kann am Ende der Leitung keine Welle entstehen, die zum Anfang zurückläuft, und die Spannung bleibt stehen.
--- falsch
Weil die rücklaufende Welle dann genau gleich groß wie die hinlaufende ist und mit umgekehrtem Vorzeichen zurückläuft, sodass sich beide Wellen auf der ganzen Leitung auslöschen.
:::
:::karte zusammenhang Falscher Abschluss bei kurzen Leitungen
Warum stört ein falscher Abschluss bei einer kurzen Leitung nicht, wohl aber bei schnellen Digitalsignalen oder Hochfrequenz?
---
Weil die reflektierte Welle bei kurzer Laufzeit fast sofort zurück ist und sich mit der hinlaufenden praktisch gleichzeitig überlagert; man merkt nur den Abschlusswiderstand. Erst bei Laufzeiten in der Größe der Signaländerungen erscheinen Echos.
--- falsch
Weil auf einer kurzen Leitung gar keine Reflexion entsteht: Der Reflexionsfaktor hängt von der Länge der Leitung ab und ist bei kurzen Leitungen null, gleich womit man sie abschließt. Erst auf langen Leitungen wird er von null verschieden.
--- falsch
Weil die reflektierte Welle auf einer kurzen Leitung durch die Dämpfung verschwindet, bevor sie den Anfang erreicht. Bei Hochfrequenz und schnellen Digitalsignalen ist die Dämpfung kleiner, deshalb kommt das Echo dort an.
--- falsch
Weil schnelle Digitalsignale und Hochfrequenz mehr Leistung haben als langsame Signale. Erst bei hoher Leistung wird die reflektierte Welle groß genug, um das Signal sichtbar zu verzerren; bei kleiner Leistung geht sie im Rauschen unter.
:::
::::
