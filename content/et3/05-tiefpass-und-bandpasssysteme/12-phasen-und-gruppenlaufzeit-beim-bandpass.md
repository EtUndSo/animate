---
title: Stufe 11: Phasen- und Gruppenlaufzeit beim Bandpass
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3251200
summary: Warum gibt es zwei Laufzeiten?
tags: Laufzeitverzerrung
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Warum gibt es zwei Laufzeiten? Weil Träger und Hüllkurve verschieden verzögert werden können.
:::

**Die Idee.** Ein Bandpass habe im Durchlassbereich den Betrag konstant und eine schwach gekrümmte Phase. Um $f_0$ nähert man sie durch ihre Tangente:

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$$

mit $t_\mathrm p=t_\mathrm p(f_0)$ und $t_\mathrm g=t_\mathrm g(f_0)$ aus [(1.4)](das-verzerrungsfreie-system.html#gl-1-4) und [(1.5)](das-verzerrungsfreie-system.html#gl-1-5). Im Tiefpassbereich ($f-f_0\to f$) ist das $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$: eine konstante Phase und eine Verzögerung.

:::satz Satz 11.1 (Laufzeiten im Bandpass)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**So liest man das:** Die Hüllkurve, die die Information trägt, wird um die *Gruppenlaufzeit* verzögert. Der Träger wird um die *Phasenlaufzeit* verzögert. Unverzerrt im strengen Sinn ist die Übertragung nur, wenn beide gleich sind. Das heißt, die Phasengerade geht durch den Ursprung (oder durch ein Vielfaches von $2\pi$ bei $f=0$). Für die Information genügt meist schon eine konstante Gruppenlaufzeit: Ist $t_\mathrm g$ nicht konstant, kommen verschiedene Frequenzanteile der Hüllkurve verschieden spät an, und Impulse zerfließen (__Laufzeitverzerrung__).

:::ltspice Hüllkurve und Träger kommen verschieden spät an
⁠**Zeichnen:** der Schwingkreis aus dem LTspice-Hinweis in Stufe [9](bandpasssignal-durch-bandpasssystem.html#stufe-9) ($f_0=10$ Hz, $\Delta f=2$ Hz). In der `.ac`-Analyse hat er bei 10 Hz die Phase $0^\circ$, also $t_\mathrm p(f_0)=0$. Schaltest du die Phasenachse auf „Group Delay“ um, zeigt sie bei 10 Hz $t_\mathrm g(f_0)=0{,}16$ s.

⁠**Versuch:** als Eingang eine Verhaltensquelle `bv`, ein Träger mit langsam schwankender Hüllkurve:

`V=(1+0.5*cos(2*pi*0.2*time))*cos(2*pi*10*time)`

Direktiven `.tran 0 20 0 0.2m` und `.options plotwinsize=0`.

⁠**Was du siehst:** Zeichne `V(in)` und `V(out)` übereinander und zoome auf 14,5 s bis 15,5 s. Das Maximum der Hüllkurve kommt am Ausgang etwa 0,16 s später an, die Nulldurchgänge des Trägers liegen aber an denselben Stellen wie am Eingang. Genau das sagt [(11.1)](#gl-11-1): Die Hüllkurve wird um $t_\mathrm g$ verzögert, der Träger um $t_\mathrm p$.
:::

:::aufgabe Aufgabe 10 ★★ Laufzeiten ablesen
<span class="anker" id="aufg-10"></span>

Ein Bandpass hat bei $f_0=1$ MHz die Phase $\varphi(f_0)=-\pi/2$ und die Steigung $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-2\pi\cdot2\,\mu\text{s}$.

<ol class="al">

<li>

Berechne $t_\mathrm p$ und $t_\mathrm g$.

</li>

<li>

Um wie viel ist die Hüllkurve eines Pulses am Ausgang verzögert? Liegt der Träger danach noch in derselben Lage relativ zur Hüllkurve?

</li>

</ol>

:::loesung
(a) $t_\mathrm p=-\frac{\varphi(f_0)}{2\pi f_0}=\frac{\pi/2}{2\pi\cdot10^6\,\mathrm{Hz}}=0{,}25$ µ s. $t_\mathrm g=2$ µ s.

(b) Die Hüllkurve kommt 2 µ s später an. Der Träger ist nur um 0,25 µ s verschoben. Gegenüber der Hüllkurve ist er also um $2\pi f_0(t_\mathrm g-t_\mathrm p)=3{,}5\pi$ verdreht, das ist modulo $2\pi$ gleich $1{,}5\pi$, also $-\pi/2$: eine Viertelperiode. Die Information in der Hüllkurve bleibt unverzerrt, solange $t_\mathrm g$ über das Band konstant ist.
:::
:::

::::formelsammlung
**Tangentennäherung der Phase**

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$$

Betrag im Durchlassbereich konstant, Phase schwach gekrümmt; $t_\mathrm p=t_\mathrm p(f_0)$ und $t_\mathrm g=t_\mathrm g(f_0)$.

**Äquivalenter Tiefpass bei linearer Phase**

$$H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$$

Im Tiefpassbereich ($f-f_0\to f$): eine konstante Phase und eine Verzögerung.

**Laufzeiten im Bandpass**

$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}$$

Die Hüllkurve wird um die Gruppenlaufzeit verzögert, der Träger um die Phasenlaufzeit. Streng unverzerrt nur bei $t_\mathrm p=t_\mathrm g$; ist $t_\mathrm g$ im Band nicht konstant, zerfließen Impulse (Laufzeitverzerrung).
::::

::::lernkarten
:::karte formel Tangentennäherung der Phase
Wie nähert man die Phase eines Bandpasses um die Mittenfrequenz $f_0$, und welche Rolle spielen dabei die beiden Laufzeiten?
---
Durch ihre Tangente: $\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$. Der Phasenwert bei $f_0$ liefert $t_\mathrm p$, die Steigung $t_\mathrm g$.
--- falsch
Durch eine Konstante, $\varphi(f)\approx\varphi(f_0)=-2\pi f_0t_\mathrm p$: Im schmalen Band ändert sich die Phase kaum, deshalb genügt die Phasenlaufzeit, und die Gruppenlaufzeit spielt beim Bandpass keine Rolle.
--- falsch
Durch ihre Tangente: $\varphi(f)\approx-2\pi f_0t_\mathrm g-2\pi(f-f_0)t_\mathrm p$. Der Phasenwert bei $f_0$ liefert die Gruppenlaufzeit, die Steigung der Phase dort die Phasenlaufzeit.
--- falsch
Durch eine Gerade durch den Ursprung, $\varphi(f)\approx-2\pi ft_\mathrm p$: Jeder Bandpass verhält sich im Durchlassbereich wie ein reines Laufzeitglied, und beide Laufzeiten sind dort stets gleich.
:::
:::karte formel Laufzeiten im Bandpass
Wie lautet der Ausgang eines Bandpasses mit konstantem Betrag und schwach gekrümmter Phase für ein Bandpasssignal mit der Hüllkurve $s_T$?
---
$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}$ und $g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}$: Die Hüllkurve wird um die Gruppenlaufzeit verzögert, der Träger um die Phasenlaufzeit.
--- falsch
$g_T(t)=s_T(t-t_\mathrm p)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm g}$ und $g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm p)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm g)}\bigr\}$: Die Hüllkurve wird um die Phasenlaufzeit verzögert, der Träger um die Gruppenlaufzeit.
--- falsch
$g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm g)}\bigr\}$: Hüllkurve und Träger werden stets gemeinsam um die Gruppenlaufzeit verzögert, weil der Träger fest mit der Hüllkurve verbunden ist.
--- falsch
$g_T(t)=s_T(t)\,\mathrm{e}^{-\mathrm{j}2\pi f_0(t_\mathrm p+t_\mathrm g)}$: Die Hüllkurve bleibt unverzögert, nur ihre Phase dreht sich um die Summe beider Laufzeiten, weil im Tiefpassbereich keine Verzögerung auftritt.
:::
:::karte zusammenhang Zwei Laufzeiten
Warum braucht man beim Bandpass zwei verschiedene Laufzeiten?
---
Weil Träger und Hüllkurve verschieden verzögert werden können: der Träger um die Phasenlaufzeit, die Hüllkurve mit der Information um die Gruppenlaufzeit. Die eine hängt vom Wert der Phase bei $f_0$ ab, die andere von ihrer Steigung.
--- falsch
Weil der Bandpass zwei Flanken hat: Die Phasenlaufzeit gilt für die untere Bandgrenze, die Gruppenlaufzeit für die obere, und für Frequenzen dazwischen mittelt man einfach die beiden Werte der Flanken.
--- falsch
Weil Eingang und Ausgang verschieden schnell reagieren: Die Phasenlaufzeit beschreibt die Verzögerung am Eingang, die Gruppenlaufzeit die am Ausgang, und erst ihre Summe ergibt die gesamte Laufzeit des Systems.
--- falsch
Weil Betrag und Phase getrennt verzögert werden: Die Phasenlaufzeit verzögert die Phase des Signals, die Gruppenlaufzeit seinen Betrag, und beim Bandpass sind die beiden Laufzeiten trotzdem stets gleich groß.
:::
:::karte zusammenhang Streng unverzerrt
Wann ist die Übertragung durch einen Bandpass im strengen Sinn unverzerrt, und was genügt meist für die Information?
---
Streng unverzerrt ist sie nur, wenn $t_\mathrm p=t_\mathrm g$ ist: Die Phasengerade geht durch den Ursprung oder bei $f=0$ durch ein Vielfaches von $2\pi$. Für die Information genügt meist eine konstante Gruppenlaufzeit.
--- falsch
Streng unverzerrt ist sie, sobald die Phasenlaufzeit konstant ist; die Gruppenlaufzeit darf schwanken, weil sie nur die Hüllkurve betrifft, die beim Bandpass ohnehin keine Information trägt.
--- falsch
Streng unverzerrt ist sie nur, wenn beide Laufzeiten null sind; jede Verzögerung von Träger oder Hüllkurve verfälscht das Signal, auch wenn sie für alle Frequenzen des Bandes gleich ist.
--- falsch
Streng unverzerrt ist sie, wenn $t_\mathrm g=2t_\mathrm p$ ist; dann liegt der Träger nach der Verzögerung wieder in derselben Lage zur Hüllkurve, weil sich die beiden Phasen genau ergänzen.
:::
:::karte begriff Laufzeitverzerrung
Was versteht man unter Laufzeitverzerrung, und wodurch entsteht sie beim Bandpass?
---
Laufzeitverzerrung entsteht, wenn die Gruppenlaufzeit $t_\mathrm g$ im Band nicht konstant ist: Verschiedene Frequenzanteile der Hüllkurve kommen verschieden spät an, und Impulse zerfließen.
--- falsch
Laufzeitverzerrung entsteht, wenn die Phasenlaufzeit $t_\mathrm p$ von der Gruppenlaufzeit abweicht: Der Träger verschiebt sich gegen die Hüllkurve, und schon dadurch zerfließen die Impulse.
--- falsch
Laufzeitverzerrung entsteht, wenn der Betrag im Band nicht konstant ist: Stärker gedämpfte Frequenzanteile der Hüllkurve wirken verspätet, und Impulse werden niedriger und breiter.
--- falsch
Laufzeitverzerrung entsteht, wenn die Gruppenlaufzeit im Band konstant, aber von null verschieden ist: Die ganze Hüllkurve kommt verspätet an, und dadurch ändert sich ihre Form.
:::
:::karte herleitung Verzögerung von Hüllkurve und Träger
Wie folgt aus der Tangentennäherung der Phase um $f_0$, dass die Hüllkurve um $t_\mathrm g$ und der Träger um $t_\mathrm p$ verzögert wird?
---
Man nähert die Phase durch $-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g$, weil ihr Wert bei $f_0$ durch $t_\mathrm p$ und ihre Steigung durch $t_\mathrm g$ festgelegt ist.
---
Im Tiefpassbereich ($f-f_0\to f$) wird daraus $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$, weil der Betrag im Band konstant ist und man das Band um $f_0$ nach links schiebt.
---
Nach $G_T=\frac12S_TH_T$ hebt der Faktor $\frac12$ die 2 auf, und der Faktor $\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$ verzögert die Hüllkurve um $t_\mathrm g$, weil das Signal ganz im Durchlassbereich liegt und ein solcher Faktor im Spektrum eine Verschiebung in der Zeit bedeutet.
---
Es bleibt $g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}$; mit dem Träger $\mathrm{e}^{\mathrm{j}2\pi f_0t}$ ergibt sich $\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}$, weil sich die Exponenten addieren. Der Träger ist also um $t_\mathrm p$ verzögert.
:::
:::karte zusammenhang Hüllkurve verzögert, Träger nicht
Was zeigt ein Reihenschwingkreis mit $f_0=10$ Hz, der bei 10 Hz die Phase $0^\circ$ und die Gruppenlaufzeit 0,16 s hat, wenn man ein Signal mit langsam schwankender Hüllkurve anlegt?
---
Das Maximum der Hüllkurve kommt am Ausgang etwa 0,16 s später an, die Nulldurchgänge des Trägers liegen aber an denselben Stellen wie am Eingang. Die Hüllkurve wird um $t_\mathrm g$ verzögert, der Träger um $t_\mathrm p(f_0)=0$.
--- falsch
Hüllkurve und Träger kommen beide etwa 0,16 s später an, weil die Gruppenlaufzeit für das ganze Signal gilt; die Phase $0^\circ$ bedeutet nur, dass der Betrag des Frequenzgangs bei 10 Hz am größten ist.
--- falsch
Die Hüllkurve kommt unverzögert an, weil die Phase bei 10 Hz null ist; nur der Träger verschiebt sich um 0,16 s, sodass seine Nulldurchgänge gegenüber denen am Eingang deutlich wandern.
--- falsch
Die Hüllkurve kommt etwa 0,08 s später an, die Hälfte der Gruppenlaufzeit, weil sie nur die halbe Bandbreite belegt; die Nulldurchgänge des Trägers verschieben sich um dieselbe Zeit.
:::
::::
