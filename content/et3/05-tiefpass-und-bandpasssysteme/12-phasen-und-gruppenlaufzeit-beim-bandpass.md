---
title: Stufe 11: Phasen- und Gruppenlaufzeit beim Bandpass
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
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
