---
title: Stufe 4: Abtastung im Frequenzbereich
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240500
summary: Dasselbe Prinzip gilt mit vertauschten Rollen: Tastet man das Spektrum ab, wird das Signal periodisch.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Dasselbe Prinzip gilt mit vertauschten Rollen: Tastet man das Spektrum ab, wird das Signal periodisch.
:::

Ein Spektrum, das nur bei den Frequenzen $kF$ bekannt ist, ist ein Kamm gewichteter Dirac-Impulse. Mit dem Faktor $F$ sind die Gewichte genau die Fourier-Koeffizienten aus [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html):

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

Das zugehörige Signal ist das Original, periodisch mit $1/F$ wiederholt. Ist das Signal kürzer als $1/F$, überlappen sich die Wiederholungen nicht. Dann gewinnt man es mit einem Zeitfenster zurück, und das Spektrum mit si-Funktionen:

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**Kurz gesagt:** Diskret in der Zeit heißt periodisch im Spektrum, diskret im Spektrum heißt periodisch in der Zeit. Das zweite ist die Fourier-Reihe aus [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Ihre Koeffizienten sind Abtastwerte des Spektrums eines Einzelimpulses, $S_p(k)=F\cdot S(kF)$.

::::formelsammlung
**Abtastung im Frequenzbereich**

$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr)$$

Spektrum nur bei den Frequenzen $kF$ bekannt; das zugehörige Signal ist das Original, periodisch mit $1/F$ wiederholt.

**Rückgewinnung aus den Spektralwerten**

$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr)$$

Nur wenn sich die Wiederholungen nicht überlappen: Das Signal ist kürzer als $1/F$ und liegt im Fenster $\operatorname{rect}(Ft)$. Zeitfenster statt Tiefpass, si-Funktionen im Spektrum statt in der Zeit.

**Fourier-Koeffizienten als Spektralwerte**

$$S_p(k)=F\cdot S(kF)$$

Die Koeffizienten der Fourier-Reihe sind, mit dem Faktor $F$, Abtastwerte des Spektrums eines Einzelimpulses. Diskret im Spektrum heißt periodisch in der Zeit.
::::

::::lernkarten
:::karte formel Abtastung im Frequenzbereich
Welches Signal gehört zu einem Spektrum, das nur bei den Frequenzen $kF$ bekannt ist, also zu $S_p(f)=F\sum_kS(kF)\,\delta(f-kF)$?
---
$s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr)$: das Original, periodisch mit $1/F$ wiederholt. Denn $S_p(f)=F\,S(f)\cdot\sum_k\delta(f-kF)$, und die Multiplikation mit dem Kamm wird im Zeitbereich eine Faltung mit einem Kamm.
--- falsch
$s_p(t)=\sum_ns\bigl(\frac nF\bigr)\,\delta\bigl(t-\frac nF\bigr)$: die Abtastwerte des Originals im Abstand $1/F$. Denn Abtasten im Spektrum ist dasselbe wie Abtasten in der Zeit, nur mit vertauschten Achsen.
--- falsch
$s_p(t)=s(t)\cdot\operatorname{rect}(Ft)$: das Original, auf ein Fenster der Breite $1/F$ beschnitten. Denn ein Spektrum aus einzelnen Linien beschreibt immer ein zeitlich begrenztes Signal.
--- falsch
$s_p(t)=F\,s(t)$: das unveränderte Original mit dem Faktor $F$. Denn die Werte $S(kF)$ enthalten bereits alle Information, und zwischen ihnen ist das Spektrum ohnehin null, sodass nichts verloren geht.
:::
:::karte zusammenhang Rückgewinnung aus den Spektralwerten
Unter welcher Bedingung lässt sich ein Signal aus den Spektralwerten $S(kF)$ exakt zurückgewinnen, und womit?
---
Wenn sich die Wiederholungen im Abstand $1/F$ nicht überlappen: Das Signal ist kürzer als $1/F$ und liegt innerhalb des Fensters. Dann schneidet ein Zeitfenster das Original aus, $s(t)=s_p(t)\cdot\operatorname{rect}(Ft)$.
--- falsch
Wenn das Spektrum oberhalb von $F$ verschwindet, das Signal also ein Tiefpasssignal ist. Dann schneidet ein idealer Tiefpass mit der Grenzfrequenz $F/2$ das Original aus dem Linienspektrum heraus.
--- falsch
Immer, denn die Werte $S(kF)$ bestimmen das Spektrum vollständig. Man setzt sie in die Fourier-Rücktransformation ein und erhält ohne weitere Bedingung das ursprüngliche Signal zurück.
--- falsch
Wenn das Signal länger als $1/F$ ist, damit jede Wiederholung das nächste Intervall vollständig füllt. Dann ergibt ein Zeitfenster der Breite $1/F$ ein lückenloses Stück des Originals.
:::
:::karte formel Spektrum aus den Spektralwerten
Wie berechnet man das Spektrum $S(f)$ eines zeitlich begrenzten Signals für jede Frequenz aus seinen Werten $S(kF)$?
---
$S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr)$. Das Zeitfenster $\operatorname{rect}(Ft)$ wird im Spektrum zu si-Funktionen, so wie der Tiefpass bei der Abtastung in der Zeit zu si-Funktionen in der Zeit führt.
--- falsch
$S(f)=\sum_kS(kF)\operatorname{rect}\bigl(\frac{f-kF}{F}\bigr)$. Jeder Wert $S(kF)$ gilt für ein Intervall der Breite $F$ um $kF$, weil sich das Spektrum zwischen zwei Abtastwerten nicht ändern kann.
--- falsch
$S(f)=\sum_kS(kF)\operatorname{si}\bigl(\pi\frac{t-kF}{F}\bigr)$. Die si-Funktionen entstehen in der Zeit, weil das Zeitfenster im Zeitbereich wirkt und dort die Lücken zwischen den Werten füllt.
--- falsch
$S(f)=F\sum_kS(kF)\,\delta(f-kF)$. Zwischen den Frequenzen $kF$ ist das Spektrum eines begrenzten Signals null, deshalb genügen die Dirac-Impulse an den bekannten Stellen, um es ganz zu beschreiben.
:::
:::karte zusammenhang Diskret heißt periodisch
Welches gemeinsame Prinzip steckt hinter dem periodischen Spektrum abgetasteter Signale und hinter der Fourier-Reihe periodischer Signale?
---
Diskret im einen Bereich heißt periodisch im anderen. Diskret in der Zeit macht das Spektrum periodisch, diskret im Spektrum macht die Zeitfunktion periodisch. Die Fourier-Reihe ist der zweite Fall.
--- falsch
Periodisch im einen Bereich heißt stetig im anderen. Ein periodisches Signal hat deshalb ein stetiges Spektrum, und ein abgetastetes Signal wird zwischen den Abtastpunkten stetig fortgesetzt.
--- falsch
Diskret im einen Bereich heißt diskret im anderen. Abgetastete Signale haben deshalb Linienspektren, und periodische Signale bestehen aus einzelnen Werten im Abstand ihrer Periode.
--- falsch
Kurz im einen Bereich heißt kurz im anderen. Abtasten verkürzt das Signal auf einzelne Punkte und deshalb auch das Spektrum; die Fourier-Reihe verkürzt es entsprechend auf eine einzige Periode.
:::
:::karte zusammenhang Fourier-Koeffizienten als Spektralwerte
Wie hängen die Fourier-Koeffizienten $S_p(k)$ eines periodisch wiederholten Impulses mit dem Spektrum $S(f)$ des Einzelimpulses zusammen?
---
Sie sind seine Abtastwerte an den Vielfachen der Grundfrequenz, mit dem Faktor $F$: $S_p(k)=F\cdot S(kF)$. Die Wiederholung im Abstand $1/F$ tastet das Spektrum im Abstand $F$ ab.
--- falsch
Sie sind die Mittelwerte des Spektrums über jeweils ein Intervall der Breite $F$ um $kF$. Die periodische Wiederholung glättet das Spektrum stückweise, und jedes Stück liefert einen Koeffizienten.
--- falsch
Sie sind seine Abtastwerte an den Vielfachen der Periode: $S_p(k)=S(k/F)$. Die Wiederholung im Abstand $1/F$ tastet das Spektrum im selben Abstand $1/F$ ab, ohne zusätzlichen Faktor.
--- falsch
Sie hängen nicht vom Einzelimpuls ab, sondern nur von der Periode $1/F$. Jeder periodisch wiederholte Impuls hat deshalb dieselben Koeffizienten, nur der Gleichanteil unterscheidet sich jeweils.
:::
::::
