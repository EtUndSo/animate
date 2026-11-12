---
title: Stufe 8: Integrieren und Differenzieren
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210900
summary: Integrator und Differenzierer sind LTI-Systeme.
tags: Integrator, Differenzierer, Doppelimpuls
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Integrator und Differenzierer sind LTI-Systeme. Mit ihnen hängen Sprungantwort und Impulsantwort zusammen, und man kann die Impulsantwort des RC-Glieds aus seiner Sprungantwort gewinnen.
:::

**Der Integrator.** Ersetzt man in [(7.6)](der-dirac-impuls.html#gl-7-6) $\delta$ durch ein beliebiges $s$, folgt dieselbe Rechnung:

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

Ein System mit der Impulsantwort $\varepsilon(t)$ bildet das laufende Integral seines Eingangs, es heißt __Integrator__. Liest man [(8.1)](#gl-8-1) mit vertauschten Rollen ($\varepsilon*s$), sagt sie: **Die Sprungantwort eines Systems ist das laufende Integral seiner Impulsantwort.** Probe am RC-Glied: $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$, genau [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5). Zwei unabhängige Wege, Differentialgleichung und Faltung, geben dasselbe.

**Der Differenzierer.** Integrator und __Differenzierer__ nacheinander lassen jedes Signal unverändert, die Kette ist ideal verzerrungsfrei. Die Impulsantwort des Differenzierers ist deshalb die Distribution $\delta'(t)$ (__Doppelimpuls__), festgelegt durch

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

Näherungsweise ist $\delta'$ ein schmaler Doppelrechteckimpuls: erst ein Rechteck der Höhe $+1/T_0^2$, dann eines der Höhe $-1/T_0^2$, jedes $T_0$ breit. Gezeichnet wird er als Pfeilpaar nach oben und unten.

**Impulsantwort = Ableitung der Sprungantwort.** Weil $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ und das System linear und zeitinvariant ist, gilt $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{Sprungantwort})$. Für das RC-Glied mit der Produktregel:

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

Der zweite Summand verschwindet nach [(7.2)](der-dirac-impuls.html#gl-7-2): $(1-\mathrm{e}^{0})\,\delta(t)=0$. Der Mechanismus dahinter: Die Sprungantwort des RC-Glieds springt nicht, der Kondensator braucht Zeit zum Laden. Nur eine springende Sprungantwort erzeugt einen Dirac-Impuls in $h$ (Aufgabe [9](#aufg-9)).

:::aufgabe Aufgabe 9 ★★ Hochpass: ein Dirac-Impuls in der Impulsantwort
<span class="anker" id="aufg-9"></span>

Vertauscht man $R$ und $C$, wird die Spannung an $R$ abgegriffen (CR-Hochpass, $RC=1$ s). Seine Sprungantwort ist $\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Begründe die Sprungantwort mit dem Mechanismus: Was liegt im ersten Moment an $R$, was nach langer Zeit?

</li>

<li>

Bestimme die Impulsantwort durch Ableiten. Was bedeutet der Dirac-Anteil physikalisch?

</li>

<li>

Prüfe: Integrieren der Impulsantwort muss die Sprungantwort zurückgeben.

</li>

</ol>

:::loesung
(a) Im ersten Moment ist der Kondensator leer, über ihm liegt keine Spannung. Die vollen 1 V liegen an $R$. Danach lädt der Strom den Kondensator, seine Spannung steigt wie $1-\mathrm{e}^{-t}$, an $R$ bleibt $\mathrm{e}^{-t}$. Nach langer Zeit ist der Kondensator voll, es fließt kein Strom, an $R$ liegt nichts mehr.

(b) Produktregel:

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

Hier springt die Sprungantwort bei $t=0$ von 0 auf 1, deshalb bleibt der Dirac-Anteil stehen. Physikalisch: Ein unendlich kurzer Stoß geht vollständig durch, weil der Kondensator in null Zeit keine Spannung aufbauen kann. Die Ladung, die der Stoß auf den Kondensator gebracht hat, fließt danach über $R$ wieder ab, in Gegenrichtung: $-\mathrm{e}^{-t}$.

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$.
:::
:::

::::kurzfassung
Integrator und Differenzierer sind LTI-Systeme. Mit ihnen folgt: Die Sprungantwort ist das laufende Integral der Impulsantwort, und die Impulsantwort ist die Ableitung der Sprungantwort.

Ein System mit der Impulsantwort $\varepsilon(t)$ bildet das laufende Integral seines Eingangs,

$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau ,$$

und heißt __Integrator__. Mit vertauschten Rollen gelesen, als $\varepsilon*s$, sagt die Gleichung: Die Antwort eines Systems auf den Sprung $\varepsilon(t)$ ist das laufende Integral seiner Impulsantwort. Integrator und __Differenzierer__ nacheinander lassen jedes Signal unverändert. Die Impulsantwort des Differenzierers ist deshalb die Distribution $\delta'(t)$, der __Doppelimpuls__, festgelegt durch $\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t)$. Näherungsweise ist er ein Rechteck der Höhe $+1/T_0^2$, gefolgt von einem der Höhe $-1/T_0^2$, jedes $T_0$ breit.

Der Grund für die Ableitung: Weil $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ und das System linear und zeitinvariant ist, ist die Impulsantwort die Ableitung der Sprungantwort. Beim RC-Glied liefert die Produktregel aus $\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)$ die Impulsantwort $\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$ und dazu den Term $\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)$, der nach dem Sieb-Produkt null ist.

Falle: Dieser Zusatzterm verschwindet nur, weil die Sprungantwort bei $t=0$ nicht springt; der Kondensator braucht Zeit zum Laden. Eine springende Sprungantwort erzeugt einen Dirac-Impuls in $h$.
::::

::::formelsammlung
**Integrator**

$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$$

System mit der Impulsantwort $\varepsilon(t)$; bildet das laufende Integral seines Eingangs.

**Sprungantwort aus der Impulsantwort**

$$\varepsilon(t)*h(t)=\int_{-\infty}^{t}h(\tau)\,\mathrm{d}\tau$$

Die Sprungantwort eines Systems ist das laufende Integral seiner Impulsantwort (Integrator-Formel mit vertauschten Rollen).

**Doppelimpuls**

$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t)$$

$\delta'(t)$ Impulsantwort des Differenzierers. Näherung: Rechteck der Höhe $+1/T_0^2$, dann eines der Höhe $-1/T_0^2$, jedes $T_0$ breit.

**Impulsantwort aus der Sprungantwort**

$$h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{Sprungantwort})$$

Für jedes LTI-System, wegen $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$.

**Impulsantwort des RC-Glieds durch Ableiten**

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$$

Produktregel; der zweite Summand ist nach dem Sieb-Produkt null, weil die Sprungantwort bei $t=0$ nicht springt. Nur eine springende Sprungantwort erzeugt einen Dirac-Impuls in $h$.
::::

::::lernkarten
:::karte begriff Integrator
Was ist ein Integrator, und welche Impulsantwort hat er?
---
Ein System, das das laufende Integral seines Eingangs bildet, $s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$. Seine Impulsantwort ist der Sprung $\varepsilon(t)$.
--- falsch
Ein System, das das Integral seines Eingangs über alle Zeiten bildet, $\int_{-\infty}^{\infty}s(\tau)\,\mathrm{d}\tau$. Seine Impulsantwort ist die Konstante 1.
--- falsch
Ein System, das das laufende Integral seines Eingangs bildet. Seine Impulsantwort ist der Dirac-Impuls $\delta(t)$, weil dieser die Fläche 1 hat.
--- falsch
Ein System, das seinen Eingang ableitet und so die Steigung bildet, $\frac{\mathrm{d}}{\mathrm{d} t}s(t)$. Seine Impulsantwort ist der Sprung $\varepsilon(t)$.
:::
:::karte begriff Differenzierer
Was ist ein Differenzierer, und welche Impulsantwort hat er?
---
Ein System, das die Ableitung seines Eingangs bildet. Mit einem Integrator in Kette lässt es jedes Signal unverändert; seine Impulsantwort ist deshalb die Distribution $\delta'(t)$.
--- falsch
Ein System, das die Ableitung seines Eingangs bildet. Seine Impulsantwort ist der Sprung $\varepsilon(t)$, weil der Sprung beim Ableiten den Dirac-Impuls liefert und die Faltung mit ihm deshalb jedes Signal ableitet.
--- falsch
Ein System, das die Differenz von Eingang und Ausgang bildet. Seine Impulsantwort ist $-\delta(t)$, weil es den Eingang vom Ausgang abzieht und so jedes Signal umkehrt.
--- falsch
Ein System, das die Ableitung seines Eingangs bildet. Seine Impulsantwort ist $\delta(t)$, weil Ableiten und Integrieren einander aufheben und nur das Einselement der Faltung übrig bleibt.
:::
:::karte begriff Doppelimpuls
Was ist der Doppelimpuls $\delta'(t)$, und wie kann man sich ihn näherungsweise vorstellen?
---
Die Impulsantwort des Differenzierers, festgelegt durch $\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t)$. Näherungsweise ist er ein schmaler Doppelrechteckimpuls: erst ein Rechteck der Höhe $+1/T_0^2$, dann eines der Höhe $-1/T_0^2$, jedes $T_0$ breit.
--- falsch
Zwei gleiche Dirac-Impulse kurz hintereinander, $\delta(t)+\delta(t-T_0)$. Näherungsweise sind das zwei Rechtecke der Höhe $+1/T_0$, jedes $T_0$ breit; gefaltet mit einem Signal ergibt er das Signal zweimal, um $T_0$ gegeneinander versetzt.
--- falsch
Die Impulsantwort des Integrators, festgelegt durch $\delta'(t)*s(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$. Näherungsweise ist er ein einzelnes Rechteck der Höhe $1/T_0$ und der Breite $T_0$, also der Fläche 1.
--- falsch
Ein Dirac-Impuls mit dem doppelten Gewicht, $2\delta(t)$, festgelegt durch $\delta'(t)*s(t)=2s(t)$. Näherungsweise ist er ein Rechteck der Höhe $2/T_0$ und der Breite $T_0$, also der Fläche 2.
:::
:::karte formel Sprungantwort und Impulsantwort
Wie hängen Sprungantwort und Impulsantwort eines LTI-Systems zusammen, und warum?
---
Die Sprungantwort ist das laufende Integral der Impulsantwort, die Impulsantwort die Ableitung der Sprungantwort. Denn mit $h$ statt $s$ besagt $s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$: Die Antwort auf $\varepsilon$ ist das laufende Integral von $h$. Umgekehrt ist $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$.
--- falsch
Die Sprungantwort ist die Ableitung der Impulsantwort, die Impulsantwort das laufende Integral der Sprungantwort. Denn ein Sprung ändert sich schneller als ein Stoß, und schnellere Eingänge erzeugen abgeleitete, steilere Antworten.
--- falsch
Die Sprungantwort ist das Produkt $\varepsilon(t)\,h(t)$: Der Sprung hat für $t\ge0$ den Wert 1 und lässt die Impulsantwort dort unverändert. Beide Antworten sind deshalb für $t\ge0$ gleich, für $t<0$ ist die Sprungantwort null.
--- falsch
Die Sprungantwort ist die Impulsantwort, verschoben um die Dauer des Sprungs. Beide haben dieselbe Form, denn das System ist zeitinvariant und antwortet auf jede Eingabe gleich.
:::
:::karte zusammenhang Probe am RC-Glied
Was zeigt die Probe $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ am RC-Glied mit $RC=1$ s?
---
Dass die Sprungantwort das laufende Integral der Impulsantwort ist: Integriert man $h(t)=\mathrm{e}^{-t}$, erhält man genau die Sprungantwort $1-\mathrm{e}^{-t}$ aus der Differentialgleichung. Zwei unabhängige Wege geben dasselbe.
--- falsch
Dass das RC-Glied für $t\ge0$ ein Integrator ist: Es bildet das laufende Integral jedes Eingangs, und die Probe liefert dafür die Kurve $1-\mathrm{e}^{-t}$. Ein Integrator und ein RC-Glied sind also für $t\ge0$ dasselbe System.
--- falsch
Dass die Fläche der Impulsantwort des RC-Glieds mit der Zeit wächst und erst nach unendlich langer Zeit 1 erreicht. Eine feste Fläche hat nur der Dirac-Impuls, alle anderen Impulsantworten wachsen mit $t$.
--- falsch
Dass die Differentialgleichung des RC-Glieds nur für $t\le1$ s gilt. Danach wird $\mathrm{e}^{-t}$ so klein, dass man auf die Faltung umsteigen muss; die Probe zeigt, dass beide bei $t=1$ s zusammenpassen.
:::
:::karte herleitung Impulsantwort des RC-Glieds durch Ableiten
Wie folgt die Impulsantwort des RC-Glieds aus seiner Sprungantwort $\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)$?
---
Die Impulsantwort ist die Ableitung der Sprungantwort, weil $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ gilt und das System linear und zeitinvariant ist.
---
Die Produktregel gibt $\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)$, weil $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t)$ ist.
---
Der zweite Summand verschwindet, weil nach dem Sieb-Produkt nur der Wert bei $t=0$ zählt: $(1-\mathrm{e}^{0})\,\delta(t)=0$.
---
Es bleibt $h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$, weil die Sprungantwort des RC-Glieds nicht springt; der Kondensator braucht Zeit zum Laden.
:::
:::karte zusammenhang Dirac-Impuls in der Impulsantwort
Wann enthält die Impulsantwort eines Systems einen Dirac-Impuls?
---
Nur wenn seine Sprungantwort springt. Beim RC-Tiefpass springt sie nicht, weil der Kondensator Zeit zum Laden braucht. Beim CR-Hochpass springt sie bei $t=0$ von 0 auf 1, und seine Impulsantwort $h(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t)$ enthält deshalb $\delta$.
--- falsch
Immer dann, wenn das System einen Kondensator enthält: Der Stoß lädt den Kondensator schlagartig, und diese Ladung gibt er als Dirac-Impuls wieder ab. Deshalb enthalten die Impulsantworten von RC-Tiefpass und CR-Hochpass beide $\delta$.
--- falsch
Nur wenn seine Sprungantwort stetig ist: Eine springende Sprungantwort lässt sich nicht ableiten. Deshalb hat der CR-Hochpass, dessen Sprungantwort bei $t=0$ springt, gar keine Impulsantwort, der RC-Tiefpass dagegen schon.
--- falsch
Bei keinem realen System: Ein Dirac-Impuls ist unendlich hoch, und kein System aus $R$ und $C$ kann einen unendlich hohen Ausgang liefern. Ein Dirac-Anteil in einer berechneten Impulsantwort ist deshalb immer ein Rechenfehler.
:::
:::karte zusammenhang Dirac-Anteil beim Hochpass
Was bedeutet der Dirac-Anteil in der Impulsantwort $\delta(t)-\mathrm{e}^{-t}\varepsilon(t)$ des CR-Hochpasses physikalisch?
---
Ein unendlich kurzer Stoß geht vollständig durch, weil der Kondensator in null Zeit keine Spannung aufbauen kann. Die Ladung, die er dabei bekommt, fließt danach über $R$ zurück, in Gegenrichtung: $-\mathrm{e}^{-t}$.
--- falsch
Der Stoß wird im Kondensator gespeichert und erscheint erst nach der Zeit $RC$ am Ausgang, dann aber vollständig. Der Anteil $-\mathrm{e}^{-t}$ beschreibt das Einschwingen bis dahin, in dem der Kondensator die Ladung sammelt.
--- falsch
Der Kondensator wirkt beim Stoß wie eine Unterbrechung, deshalb liegt der ganze Stoß an $C$ und nicht an $R$. Der Anteil $-\mathrm{e}^{-t}$ ist die Ladung, die danach im Widerstand in Wärme umgesetzt wird.
--- falsch
Der Dirac-Anteil ist ein Rechenergebnis der Produktregel ohne physikalische Bedeutung. Am Ausgang misst man nur $-\mathrm{e}^{-t}$, weil kein Messgerät einen unendlich kurzen Stoß anzeigen kann.
:::
::::
