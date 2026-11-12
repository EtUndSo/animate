---
title: Stufe 5: Die Faltung ausrechnen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210600
summary: Das Integral (4.2) ist für konkrete Signale auszuwerten.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Das Integral [(4.2)](das-faltungsintegral.html#gl-4-2) ist für konkrete Signale auszuwerten. Der Schlüssel ist, beide Faktoren über der Integrationsvariablen $\tau$ zu zeichnen.
:::

**Das Rezept.** Für einen festen Zeitpunkt $t$:

<ol>

<li>

$s(\tau)$ über $\tau$ zeichnen.

</li>

<li>

$h(-\tau)$ zeichnen: $h$ an der senkrechten Achse *spiegeln*.

</li>

<li>

$h(t-\tau)$: das gespiegelte $h$ um $t$ nach rechts *schieben*.

</li>

<li>

Beide *multiplizieren* und über $\tau$ *integrieren*: Das ist $g(t)$.

</li>

</ol>

Lässt man $t$ wachsen, gleitet das gespiegelte $h$ von links nach rechts über $s$. Wo sich die beiden nicht überlappen, ist $g(t)=0$.

Warum gespiegelt? Als Funktion von $\tau$ fällt das Argument $t-\tau$, wenn $\tau$ wächst. Der Anfang von $h$ (Alter null) liegt bei $\tau=t$, ältere Stöße liegen weiter links. Beim RC-Glied ist $h$ am Anfang am größten: Das System „erinnert“ sich an die jüngste Vergangenheit am stärksten.

::::beispiel RC-Glied und Rechteckimpuls
Die Impulsantwort des RC-Glieds mit der Zeitkonstanten $T=RC$ ist ein abfallender Exponentialimpuls der Fläche 1. Der kurze Stoß lädt den Kondensator schlagartig auf $1/T$, danach entlädt er sich über $R$:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

Eingang: Rechteck der Höhe $a$ von $0$ bis $T_0$. Abbildung [6](#abb-6) zeigt die Lage der beiden Faktoren für zwei Zeitpunkte. Es gibt drei Bereiche:

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$
::::

:::herleitung Antwort auf den Rechteckimpuls
⁠**$t<0$:** Das geschobene $h(t-\tau)$ ist nur für $\tau\le t<0$ von null verschieden, $s(\tau)$ nur für $\tau\ge0$. Keine Überlappung, $g=0$.

⁠**$0\le t\le T_0$:** Überlappung für $0<\tau<t$:

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$:** Überlappung nur noch für $0<\tau<T_0$:

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

Im Rechenmodell ($a=1$, $T_0=T=1$ s): $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$, $g(3)=0{,}0855$. Das ist dieselbe Kurve wie $g_0$ in Abb. [4](was-ein-lti-system-ist.html#abb-4).

:::abbildung et3/k1schieben 6
Faltung grafisch, $a=1$, $T_0=T=1$ s. Blau: $s(\tau)$. Rot: gespiegeltes und um $t$ geschobenes $h(t-\tau)$. Die orange Fläche ist $g(t)$: 0,3935 bei $t=0{,}5$ s (teilweise Überlappung), 0,2325 bei $t=2$ s (das ganze Rechteck liegt im abgeklungenen Teil von $h$). Rechts die vollständige Antwort mit beiden Punkten.
:::

:::frage Warum spiegelt man $h$ und nicht $s$?
Man darf auch $s$ statt $h$ spiegeln: Die Substitution $\tau'=t-\tau$ macht aus $\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ das Integral $\int s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$. Man spiegelt die Funktion, bei der das Schieben übersichtlicher ist, meist die mit der einfacheren Form.
:::

:::ltspice Antwort auf den Rechteckimpuls
⁠**Zeichnen:** das RC-Glied aus Stufe [2](ein-erstes-system-das-rc-glied.html#stufe-2) mit der Quelle `PULSE(0 1 0 1u 1u 1)`: Höhe 1 V, Dauer 1 s.

⁠**Direktiven:** `.tran 0 20 0 1m`, je Zeitpunkt eine Messung wie `.meas tran g2 FIND V(out) AT=2`, dazu `.meas tran gmax MAX V(out)` und `.meas tran flaeche INTEG V(out)`.

⁠**Was du siehst:** $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$ und $g(3)=0{,}0855$, genau wie nach [(5.2)](#gl-5-2). Vergleiche `gmax` und `flaeche` mit deinem Ergebnis aus Aufgabe [6](#aufg-6).
:::

:::aufgabe Aufgabe 5 ★★ Rechteck mit Rechteck
<span class="anker" id="aufg-5"></span>

Berechne $\operatorname{rect}(t)*\operatorname{rect}(t)$ mit dem Rezept. Unterscheide $|t|>1$, $-1\le t\le0$ und $0\le t\le1$. Welches Elementarsignal kommt heraus?

:::loesung
Das gespiegelte Rechteck ist wieder $\operatorname{rect}$ (symmetrisch), geschoben liegt es auf $[t-\frac12,t+\frac12]$. Das Integral ist die Länge der Überlappung mit $[-\frac12,\frac12]$:

<ul>

<li>

$|t|>1$: keine Überlappung, 0.

</li>

<li>

$-1\le t\le0$: Überlappung von $-\frac12$ bis $t+\frac12$, Länge $1+t$.

</li>

<li>

$0\le t\le1$: Überlappung von $t-\frac12$ bis $\frac12$, Länge $1-t$.

</li>

</ul>

Zusammen $1-|t|$ für $|t|\le1$: $\operatorname{rect}*\operatorname{rect}=\Lambda$. Numerisch: 1,000; 0,500; 0,200 bei $t=0$; 0,5; 0,8.
:::
:::

:::aufgabe Aufgabe 6 ★★ Die Rechteckantwort prüfen
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Zeige, dass [(5.2)](#gl-5-2) bei $t=T_0$ stetig ist. Warum muss sie stetig sein?

</li>

<li>

Wo hat $g(t)$ sein Maximum, und wie groß ist es im Rechenmodell?

</li>

<li>

Zeige, dass die Fläche unter $g(t)$ gleich $aT_0$ ist, und begründe das ohne Rechnung mit $\int h\,\mathrm{d} t=1$.

</li>

</ol>

:::loesung
(a) Bei $t=T_0$: $a(1-\mathrm{e}^{-T_0/T})$ und $a(\mathrm{e}^{T_0/T}-1)\mathrm{e}^{-T_0/T}=a(1-\mathrm{e}^{-T_0/T})$, gleich. Physikalisch: Die Kondensatorspannung kann nicht springen, dafür bräuchte es einen unendlichen Strom. Mathematisch: Die Faltung eines beschränkten Signals mit einem integrierbaren $h$ ist stetig.

(b) Während des Impulses steigt $g$, danach fällt es. Das Maximum liegt bei $t=T_0$: $g(1\,\mathrm{s})=1-\mathrm{e}^{-1}=0{,}632$.

(c) Rechnung:

$$\int g\,\mathrm{d} t=a\Bigl[T_0-T\bigl(1-\mathrm{e}^{-T_0/T}\bigr)\Bigr]+a\bigl(\mathrm{e}^{T_0/T}-1\bigr)T\mathrm{e}^{-T_0/T}=aT_0.$$

Ohne Rechnung: Die Fläche einer Faltung ist das Produkt der Flächen, $\int g\,\mathrm{d} t=\int\!\!\int s(\tau)h(t-\tau)\,\mathrm{d}\tau\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$. Numerisch: 1,000.
:::
:::

::::kurzfassung
Man wertet das Faltungsintegral aus, indem man beide Faktoren über der Integrationsvariablen $\tau$ zeichnet. Für einen festen Zeitpunkt $t$ gilt das Rezept:

<ol>

<li>

$s(\tau)$ über $\tau$ zeichnen;

</li>

<li>

$h$ an der senkrechten Achse spiegeln, das ergibt $h(-\tau)$;

</li>

<li>

das gespiegelte $h$ um $t$ nach rechts schieben, das ergibt $h(t-\tau)$;

</li>

<li>

beide multiplizieren und über $\tau$ integrieren, das ergibt $g(t)$.

</li>

</ol>

Lässt man $t$ wachsen, gleitet das gespiegelte $h$ von links nach rechts über $s$. Wo sich beide nicht überlappen, ist $g(t)=0$.

Der Grund für das Spiegeln: Als Funktion von $\tau$ fällt das Argument $t-\tau$, wenn $\tau$ wächst. Der Anfang von $h$, das Alter null, liegt bei $\tau=t$; ältere Stöße liegen weiter links.

Die Impulsantwort des RC-Glieds mit der __Zeitkonstanten__ $T=RC$ ist ein abfallender Exponentialimpuls der Fläche 1:

$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}.$$

Der kurze Stoß lädt den Kondensator schlagartig auf $1/T$, danach entlädt er sich über $R$.

Falle: Die Integrationsgrenzen sind die Ränder der Überlappung und hängen von $t$ ab. Deshalb zerfällt das Ergebnis in Bereiche, beim Rechteckimpuls am RC-Glied in drei. Spiegeln darf man auch $s$ statt $h$: Die Substitution $\tau'=t-\tau$ macht aus $\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ das Integral $\int s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$.
::::

::::formelsammlung
**Spiegeln von $s$ statt $h$**

$$\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$$

Substitution $\tau'=t-\tau$. Rezept für festes $t$: $s(\tau)$ zeichnen, $h$ zu $h(-\tau)$ spiegeln, um $t$ nach rechts zu $h(t-\tau)$ schieben, multiplizieren, über $\tau$ integrieren. Ohne Überlappung ist $g(t)=0$.

**Impulsantwort des RC-Glieds**

$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}$$

Zeitkonstante $T=RC$; abfallender Exponentialimpuls der Fläche 1. Der Stoß lädt den Kondensator schlagartig auf $1/T$, danach entlädt er sich über $R$.

**Antwort des RC-Glieds auf einen Rechteckimpuls**

$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases}$$

Eingang: Rechteck der Höhe $a$ von $0$ bis $T_0$; $T=RC$. Drei Bereiche: keine Überlappung, Überlappung für $0<\tau<t$, Überlappung für $0<\tau<T_0$.
::::

::::lernkarten
:::karte zusammenhang Rezept zum Ausrechnen
In welchen Schritten wertet man das Faltungsintegral für einen festen Zeitpunkt $t$ aus?
---
$s(\tau)$ über $\tau$ zeichnen, $h$ an der senkrechten Achse zu $h(-\tau)$ spiegeln, um $t$ nach rechts zu $h(t-\tau)$ schieben, beide multiplizieren und über $\tau$ integrieren.
--- falsch
$s(\tau)$ und $h(\tau)$ über $\tau$ zeichnen, beide multiplizieren und über $\tau$ integrieren; spiegeln ist unnötig, weil $h(t-\tau)$ nur eine verschobene Kopie von $h(\tau)$ ist.
--- falsch
$s(\tau)$ über $\tau$ zeichnen, $h$ zu $h(-\tau)$ spiegeln, um $t$ nach links schieben, beide addieren und über $\tau$ integrieren; die Summe ist dann $g(t)$.
--- falsch
$s$ an der senkrechten Achse spiegeln, $h(\tau)$ um $t$ nach links schieben, beide multiplizieren und über $t$ integrieren, weil $t$ die Zeit des Ausgangs ist.
:::
:::karte zusammenhang Warum gespiegelt
Warum erscheint $h(t-\tau)$ gespiegelt, wenn man es beim Ausrechnen der Faltung über $\tau$ zeichnet?
---
Als Funktion von $\tau$ fällt das Argument $t-\tau$, wenn $\tau$ wächst. Der Anfang von $h$ (Alter null) liegt deshalb bei $\tau=t$, ältere Stöße liegen weiter links.
--- falsch
Weil das System die Zeit umkehrt: Was zuerst hineingeht, kommt zuletzt heraus. Deshalb läuft $h$ beim Rechnen rückwärts, und sein Anfang liegt rechts.
--- falsch
Weil $h$ bei jedem System eine gerade Funktion ist; das Spiegeln ändert sie gar nicht und dient nur der Übersicht in der Zeichnung des Integranden.
--- falsch
Als Funktion von $\tau$ wächst das Argument $t-\tau$, wenn $\tau$ wächst. Der Anfang von $h$ liegt deshalb bei $\tau=0$, jüngere Stöße liegen weiter links.
:::
:::karte begriff Zeitkonstante
Welche Rolle spielt die Zeitkonstante $T=RC$ in der Impulsantwort des RC-Glieds?
---
Sie legt Höhe und Abklingen fest: $h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}$ beginnt bei $1/T$ und fällt mit $\mathrm{e}^{-t/T}$, nach der Zeit $T$ also auf den Bruchteil $\mathrm{e}^{-1}$ des Anfangswerts. Die Fläche bleibt 1.
--- falsch
Sie ist die Zeit, nach der das RC-Glied auf einen Stoß vollständig abgeklungen ist: Für $t>T$ ist $h(t)=0$, weil der Kondensator dann leer ist und kein Strom mehr fließt.
--- falsch
Sie ist die Zeit, die ein Stoß braucht, um durch das RC-Glied zu laufen: Die Antwort beginnt erst bei $t=T$, vorher bleibt der Ausgang null, weil der Kondensator sich erst füllen muss.
--- falsch
Sie ist die Höhe der Impulsantwort am Anfang, $h(0^+)=T$: Je größer $R$ und $C$, desto stärker antwortet das RC-Glied auf einen Stoß, und desto größer wird die Fläche.
:::
:::karte formel Impulsantwort des RC-Glieds
Welche Impulsantwort hat das RC-Glied mit der Zeitkonstanten $T=RC$, und wie kommt sie zustande?
---
$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}$, ein abfallender Exponentialimpuls der Fläche 1. Der kurze Stoß lädt den Kondensator schlagartig auf $1/T$, danach entlädt er sich über $R$.
--- falsch
$h(t)=\varepsilon(t)\,\mathrm{e}^{-t/T}$, ein abfallender Exponentialimpuls der Höhe 1. Der Stoß lädt den Kondensator auf 1, danach entlädt er sich über $R$; die Fläche ist $T$.
--- falsch
$h(t)=\frac1T\,\varepsilon(t)\,\bigl(1-\mathrm{e}^{-t/T}\bigr)$. Der Stoß lädt den Kondensator langsam auf, und er bleibt danach geladen, weil nach dem Stoß kein Strom mehr fließt.
--- falsch
$h(t)=\frac1T\,\mathrm{e}^{-|t|/T}$, zu beiden Seiten von $t=0$ abfallend. Der Kondensator reagiert schon kurz vor dem Stoß, weil sich die Ladung über $R$ ankündigt.
:::
:::karte formel RC-Glied und Rechteckimpuls
Wie antwortet das RC-Glied mit $T=RC$ auf ein Rechteck der Höhe $a$ von $0$ bis $T_0$?
---
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases}$$

Erst lädt sich der Kondensator, nach dem Ende des Rechtecks entlädt er sich exponentiell.
--- falsch
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\,\mathrm{e}^{-t/T} & t>T_0.\end{cases}$$

Nach dem Ende des Rechtecks fällt der Ausgang auf die Impulsantwort zurück, als hätte der Kondensator nichts gespeichert.
--- falsch
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\,\mathrm{e}^{-t/T} & 0\le t\le T_0,\\[2pt] 0 & t>T_0.\end{cases}$$

Während des Rechtecks klingt der Ausgang ab, danach ist er null, weil ohne Eingang auch kein Ausgang entsteht.
--- falsch
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & t\ge0.\end{cases}$$

Das Ende des Rechtecks wirkt sich nicht aus, weil der Kondensator seine Ladung danach unverändert hält.
:::
:::karte herleitung Antwort auf den Rechteckimpuls
Wie folgt aus dem Faltungsintegral mit $h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}$ die Antwort auf das Rechteck der Höhe $a$ von $0$ bis $T_0$?
---
Für $t<0$ ist $g=0$, weil das geschobene $h(t-\tau)$ nur für $\tau\le t<0$ und $s(\tau)$ nur für $\tau\ge0$ von null verschieden ist; die beiden überlappen sich nicht.
---
Für $0\le t\le T_0$ integriert man nur über $0<\tau<t$, weil sich die beiden nur dort überlappen: $g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau$.
---
Den Faktor $\mathrm{e}^{-t/T}$ zieht man vor das Integral, weil er nicht von $\tau$ abhängt: $\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr)$.
---
Für $t>T_0$ reicht die Überlappung nur noch von $0$ bis $T_0$, weil das Rechteck dort endet; dieselbe Rechnung gibt $g(t)=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}$.
:::
:::karte zusammenhang Spiegeln von s statt h
Darf man beim Ausrechnen der Faltung auch $s$ spiegeln statt $h$?
---
Ja. Die Substitution $\tau'=t-\tau$ macht aus $\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ das Integral $\int s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$. Man spiegelt die Funktion, bei der das Schieben übersichtlicher ist, meist die mit der einfacheren Form.
--- falsch
Nein. Nur die Impulsantwort darf gespiegelt werden, weil sie zum System gehört; spiegelt man stattdessen $s$, erhält man die Antwort auf das zeitlich umgekehrte Eingangssignal und nicht $g(t)$.
--- falsch
Ja, aber dann kommt $g(-t)$ statt $g(t)$ heraus. Man muss das Ergebnis zum Schluss noch einmal an der senkrechten Achse zurückspiegeln, damit die Zeitrichtung des Ausgangs wieder stimmt.
--- falsch
Ja, aber das Ergebnis wechselt dabei das Vorzeichen, weil die Substitution $\tau'=t-\tau$ das Differential $\mathrm{d}\tau=-\mathrm{d}\tau'$ liefert; man muss es zum Schluss noch mit $-1$ multiplizieren.
:::
:::karte zusammenhang Stetigkeit der Rechteckantwort
Warum muss die Antwort des RC-Glieds auf den Rechteckimpuls bei $t=T_0$ stetig sein, obwohl der Eingang dort springt?
---
Physikalisch kann die Kondensatorspannung nicht springen, dafür bräuchte es einen unendlichen Strom. Mathematisch ist die Faltung eines beschränkten Signals mit einem integrierbaren $h$ stetig.
--- falsch
Sie muss es nicht sein: Bei $t=T_0$ springt der Ausgang um $a$ nach unten, weil der Eingang dort um $a$ fällt und das RC-Glied jeden Sprung des Eingangs direkt weitergibt.
--- falsch
Weil der Widerstand den Strom begrenzt und der Ausgang beim RC-Glied am Widerstand abgegriffen wird; ein begrenzter Strom erzeugt am Widerstand eine Spannung, die nicht springen kann.
--- falsch
Weil die Faltung zwei Rechtecke stets zu einer stetigen Kurve glättet; ein Eingang, der kein Rechteck ist, könnte dagegen auch einen springenden Ausgang erzeugen.
:::
:::karte zusammenhang Fläche der Rechteckantwort
Warum ist die Fläche unter der Antwort des RC-Glieds auf das Rechteck der Höhe $a$ und der Dauer $T_0$ gleich $aT_0$?
---
Die Fläche einer Faltung ist das Produkt der Flächen: $\int g\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$. Das Rechteck hat die Fläche $aT_0$, die Impulsantwort die Fläche 1.
--- falsch
Die Fläche einer Faltung ist das Produkt der Flächen, und die Impulsantwort des RC-Glieds hat die Fläche $T=RC$: Allgemein ist sie $aT_0\,T$, nur im Rechenmodell mit $T=1$ s gleich $aT_0$.
--- falsch
Der Ausgang ist höchstens $a$ hoch und dauert etwa $T_0$; die Fläche ist deshalb nur ungefähr $aT_0$, weil der abklingende Teil nach dem Rechteck noch etwas hinzufügt.
--- falsch
Die Fläche einer Faltung ist die Summe der Flächen, $aT_0+1$; davon geht im Widerstand die Fläche 1 als Wärme verloren, und am Ausgang bleibt genau $aT_0$ übrig.
:::
::::
