---
title: Stufe 4: Autokorrelation, Kovarianz und Kreuzkorrelation
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270500
summary: Wie schnell ändert sich ein Zufallssignal?
tags: Autokovarianzfunktion
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Wie schnell ändert sich ein Zufallssignal? Das sagt die AKF: wie ähnlich das Signal sich selbst nach der Zeit $\tau$ noch ist.
:::

:::satz Satz 4.1 (Eigenschaften der AKF stationärer Prozesse)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0). \tag{4.1}$$

Für ergodische Prozesse ist $\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$, also die AKF eines Leistungssignals aus [Kapitel 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html).
:::

:::herleitung Maximum bei $\tau=0$
$\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$, denn der Erwartungswert eines Quadrats ist nie negativ. Ausmultipliziert und mit Linearität: $\mathrm E\{s^2(t)\}+\mathrm E\{s^2(t+\tau)\}\pm2\mathrm E\{s(t)s(t+\tau)\}\ge0$, also $2\varphi_{ss}(0)\pm2\varphi_{ss}(\tau)\ge0$. Gerade: $t\to t-\tau$ in der Definition.
:::

**Kovarianz.** Zieht man vorher den Mittelwert ab, erhält man die __Autokovarianzfunktion__

<span class="anker" id="gl-4-2"></span>
$$\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2,\qquad\mu_{ss}(0)=\sigma_s^2. \tag{4.2}$$

Enthält der Prozess keine periodischen Anteile, werden weit auseinanderliegende Werte unabhängig: $\varphi_{ss}(\tau)\to m_s^2$ und $\mu_{ss}(\tau)\to0$ für $\tau\to\infty$.

**Kreuzkorrelation und Summen.** Für zwei Prozesse ist $\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$ mit $\varphi_{vu}(\tau)=\varphi_{uv}(-\tau)$ und die Kreuzkovarianz $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$. Für die Summe $s=u+v$ folgt durch Ausmultiplizieren

<span class="anker" id="gl-4-3"></span>
$$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv},\qquad L_s=L_u+L_v+2\varphi_{uv}(0),\qquad\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0). \tag{4.3}$$

⁠**Kurz gesagt:** Leistungen addieren sich nur, wenn die Signale unkorreliert sind. Sonst kommt der Kreuzterm hinzu. Zwei gleiche Signale ergeben die vierfache, zwei entgegengesetzte die Leistung null.

:::aufgabe Aufgabe 2 ★★ Zwei Rauschquellen
<span class="anker" id="aufg-2"></span>

Zwei mittelwertfreie Rauschspannungen mit den Effektivwerten 3 mV und 4 mV werden addiert. Wie groß ist der Effektivwert der Summe, wenn sie (a) unkorreliert sind, (b) dieselbe Form haben ($\varphi_{uv}(0)=\sigma_u\sigma_v$), (c) dieselbe Form mit umgekehrtem Vorzeichen haben ($\varphi_{uv}(0)=-\sigma_u\sigma_v$)?

:::loesung
(a) $\sigma=\sqrt{9+16}=5$ mV. (b) $\sigma^2=9+16+2\cdot12=49$, also 7 mV: Die Amplituden addieren sich. (c) $\sigma^2=9+16-24=1$, also 1 mV: Die Signale löschen sich fast aus.
:::
:::

::::formelsammlung
**Eigenschaften der AKF**

$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0)$$

Für stationäre Prozesse. Bei ergodischen ist $\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$, die AKF eines Leistungssignals.

**Autokovarianzfunktion**

$$\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2,\qquad\mu_{ss}(0)=\sigma_s^2$$

Ohne periodische Anteile gilt für $\tau\to\infty$: $\varphi_{ss}(\tau)\to m_s^2$ und $\mu_{ss}(\tau)\to0$.

**Kreuzkorrelation und Kreuzkovarianz**

$$\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\},\qquad\varphi_{vu}(\tau)=\varphi_{uv}(-\tau),\qquad\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$$

Für zwei Prozesse $u$ und $v$; Vertauschen spiegelt die KKF.

**Summe zweier Prozesse**

$$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv},\qquad L_s=L_u+L_v+2\varphi_{uv}(0),\qquad\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$$

Für $s=u+v$. Leistungen addieren sich nur bei unkorrelierten Signalen; zwei gleiche ergeben die vierfache, zwei entgegengesetzte die Leistung null.
::::

::::lernkarten
:::karte formel Eigenschaften der AKF
Welche drei Eigenschaften hat die Autokorrelationsfunktion $\varphi_{ss}(\tau)$ eines stationären Prozesses?
---
$\varphi_{ss}(0)=L_s$, $\varphi_{ss}(\tau)=\varphi_{ss}(-\tau)$ und $|\varphi_{ss}(\tau)|\le\varphi_{ss}(0)$: Bei $\tau=0$ steht die Leistung, die AKF ist gerade und hat dort ihr Maximum.
--- falsch
$\varphi_{ss}(0)=m_s^2$, $\varphi_{ss}(\tau)=\varphi_{ss}(-\tau)$ und $|\varphi_{ss}(\tau)|\le\varphi_{ss}(0)$: Bei $\tau=0$ steht das Quadrat des Mittelwerts, die AKF ist gerade und hat dort ihr Maximum.
--- falsch
$\varphi_{ss}(0)=L_s$, $\varphi_{ss}(\tau)=-\varphi_{ss}(-\tau)$ und $\varphi_{ss}(\tau)\ge\varphi_{ss}(0)$: Bei $\tau=0$ steht die Leistung, die AKF ist ungerade und hat dort ihr Minimum.
--- falsch
$\varphi_{ss}(0)=\sigma_s^2$, $\varphi_{ss}(\tau)=\varphi_{ss}(-\tau)$ und $\varphi_{ss}(\tau)\ge0$: Bei $\tau=0$ steht die Varianz, die AKF ist gerade und wird für kein $\tau$ negativ.
:::
:::karte herleitung Maximum der AKF
Wie zeigt man ausgehend von $\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$, dass $|\varphi_{ss}(\tau)|\le\varphi_{ss}(0)$ gilt?
---
Man geht von $\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$ aus, weil der Erwartungswert eines Quadrats nie negativ ist.
---
Man multipliziert aus und erhält $\mathrm E\{s^2(t)\}+\mathrm E\{s^2(t+\tau)\}\pm2\mathrm E\{s(t)s(t+\tau)\}\ge0$, weil der Erwartungswert linear ist.
---
Das ist $2\varphi_{ss}(0)\pm2\varphi_{ss}(\tau)\ge0$, weil bei einem stationären Prozess beide quadratischen Mittelwerte gleich $\varphi_{ss}(0)$ sind und der Mischterm die AKF ist.
---
Es folgt $|\varphi_{ss}(\tau)|\le\varphi_{ss}(0)$, weil die Ungleichung für beide Vorzeichen gilt und $\varphi_{ss}(\tau)$ deshalb zwischen $-\varphi_{ss}(0)$ und $\varphi_{ss}(0)$ liegt.
:::
:::karte zusammenhang Gerade AKF
Warum ist die Autokorrelationsfunktion eines stationären Prozesses eine gerade Funktion von $\tau$?
---
Weil man in $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$ die Zeit $t$ durch $t-\tau$ ersetzen darf, ohne dass sich bei Stationarität der Mittelwert ändert. Dann steht dort $\mathrm E\{s(t-\tau)s(t)\}$, und das ist $\varphi_{ss}(-\tau)$.
--- falsch
Weil jedes stationäre Signal selbst eine gerade Funktion der Zeit ist, $s(t)=s(-t)$. Die AKF übernimmt diese Symmetrie, denn sie wird aus den Signalwerten gebildet und kann keine neue Richtung erzeugen.
--- falsch
Weil die AKF bei $\tau=0$ ihr Maximum hat und jede Funktion mit einem Maximum bei null gerade ist. Die Symmetrie folgt also unmittelbar aus der Ungleichung $|\varphi_{ss}(\tau)|\le\varphi_{ss}(0)$.
--- falsch
Weil ein stationärer Prozess den Mittelwert null hat. Mittelwertfreie Prozesse haben stets eine gerade AKF; bei einem Gleichanteil wird die AKF dagegen ungerade, weil sich die Kurve verschiebt.
:::
:::karte zusammenhang AKF ergodischer Prozesse
Wie hängt die AKF eines ergodischen Prozesses mit der AKF eines Leistungssignals zusammen?
---
Bei Ergodizität ist das Scharmittel gleich dem Zeitmittel einer Musterfunktion, also $\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$. Das ist genau die AKF eines Leistungssignals, gebildet aus einer einzigen Musterfunktion.
--- falsch
Bei Ergodizität ist sie die AKF eines Energiesignals, $\varphi_{ss}(\tau)=\int s(t)s(t+\tau)\,\mathrm{d} t$, ohne Mittelung über die Zeit, weil jede Musterfunktion eines ergodischen Prozesses endliche Energie hat.
--- falsch
Die beiden haben nichts miteinander zu tun: Die AKF eines Prozesses ist ein Scharmittel, die eines Leistungssignals ein Zeitmittel, und beide stimmen auch bei Ergodizität nur bei $\tau=0$ überein.
--- falsch
Bei Ergodizität ist sie das Quadrat des Zeitmittels, $\varphi_{ss}(\tau)=\overline{s(t)}^{\,2}$, also für alle $\tau$ gleich dem Quadrat des Gleichanteils einer Musterfunktion, ohne jede Abhängigkeit von $\tau$.
:::
:::karte begriff Autokovarianzfunktion
Was ist die Autokovarianzfunktion $\mu_{ss}(\tau)$ eines stationären Prozesses, und welchen Wert hat sie bei $\tau=0$?
---
Die AKF des Signals nach Abzug des Mittelwerts: $\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2$. Bei $\tau=0$ ist sie die Varianz, $\mu_{ss}(0)=\sigma_s^2$.
--- falsch
Die AKF des Signals plus das Quadrat des Mittelwerts: $\mu_{ss}(\tau)=\varphi_{ss}(\tau)+m_s^2$. Bei $\tau=0$ ist sie die Leistung samt der Leistung des Gleichanteils, $\mu_{ss}(0)=L_s+m_s^2$.
--- falsch
Die Korrelation zweier verschiedener Prozesse: $\mu_{ss}(\tau)=\mathrm E\{s(t)g(t+\tau)\}$. Bei $\tau=0$ ist sie null, weil verschiedene Prozesse zum selben Zeitpunkt nicht zusammenhängen.
--- falsch
Die AKF des Signals nach Abzug des Mittelwerts: $\mu_{ss}(\tau)=\varphi_{ss}(\tau)-m_s$. Bei $\tau=0$ ist sie der Effektivwert des Wechselanteils, also die Standardabweichung, $\mu_{ss}(0)=\sigma_s$.
:::
:::karte zusammenhang AKF für große Verschiebungen
Wogegen streben AKF und Autokovarianz eines ergodischen Prozesses ohne periodische Anteile für $\tau\to\infty$, und warum?
---
$\varphi_{ss}(\tau)\to m_s^2$ und $\mu_{ss}(\tau)\to0$, weil weit auseinanderliegende Werte unabhängig werden: Ihre Schwankungen hängen nicht mehr zusammen, und von der AKF bleibt nur der Beitrag des Mittelwerts.
--- falsch
$\varphi_{ss}(\tau)\to0$ und $\mu_{ss}(\tau)\to-m_s^2$, weil weit auseinanderliegende Werte unabhängig werden und unabhängige Werte im Mittel das Produkt null haben, auch wenn das Signal einen Gleichanteil hat.
--- falsch
$\varphi_{ss}(\tau)\to L_s$ und $\mu_{ss}(\tau)\to\sigma_s^2$, weil sich ein stationärer Prozess nach langer Zeit wiederholt und die Werte dann wieder so ähnlich sind wie bei $\tau=0$.
--- falsch
$\varphi_{ss}(\tau)\to m_s^2$ und $\mu_{ss}(\tau)\to m_s^2$, weil weit auseinanderliegende Werte unabhängig werden und die Autokovarianz dann genau wie die AKF das Quadrat des Mittelwerts ergibt.
:::
:::karte formel Kreuzkorrelation und Kreuzkovarianz
Wie sind Kreuzkorrelation und Kreuzkovarianz zweier Prozesse $u$ und $v$ definiert, und was passiert beim Vertauschen der Prozesse?
---
$\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$ und $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$. Vertauscht man die Prozesse, wird die KKF gespiegelt: $\varphi_{vu}(\tau)=\varphi_{uv}(-\tau)$.
--- falsch
$\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$ und $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$. Vertauscht man die Prozesse, bleibt die KKF unverändert: $\varphi_{vu}(\tau)=\varphi_{uv}(\tau)$.
--- falsch
$\varphi_{uv}(\tau)=\mathrm E\{u(t)\}\,\mathrm E\{v(t+\tau)\}$ und $\mu_{uv}(\tau)=\varphi_{uv}(\tau)$. Vertauscht man die Prozesse, wechselt die KKF ihr Vorzeichen: $\varphi_{vu}(\tau)=-\varphi_{uv}(\tau)$.
--- falsch
$\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$ und $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_u-m_v$. Vertauscht man die Prozesse, wird die KKF gespiegelt und negiert: $\varphi_{vu}(\tau)=-\varphi_{uv}(-\tau)$.
:::
:::karte formel Summe zweier Prozesse
Wie hängen AKF, Leistung und Varianz der Summe $s=u+v$ zweier Prozesse mit den entsprechenden Größen der Summanden zusammen?
---
$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv}$, $L_s=L_u+L_v+2\varphi_{uv}(0)$ und $\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$, wie das Ausmultiplizieren der Produkte ergibt.
--- falsch
$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{vv}$, $L_s=L_u+L_v$ und $\sigma_s^2=\sigma_u^2+\sigma_v^2$ für beliebige Prozesse: Die Kreuzterme heben sich beim Mitteln immer weg, weil $\varphi_{uv}$ und $\varphi_{vu}$ entgegengesetzt gleich sind.
--- falsch
$\varphi_{ss}(\tau)=\varphi_{uu}\,\varphi_{vv}$, $L_s=L_u\,L_v$ und $\sigma_s^2=\sigma_u^2\,\sigma_v^2$: Bei einer Summe multiplizieren sich die Leistungen, weil die Leistung quadratisch vom Signal abhängt.
--- falsch
$\varphi_{ss}(\tau)=\varphi_{uu}+2\varphi_{uv}+\varphi_{vv}$, $L_s=L_u+L_v+2\varphi_{uv}(0)$ und $\sigma_s^2=\sigma_u+\sigma_v$: Die Effektivwerte der Wechselanteile addieren sich bei jeder Summe unmittelbar.
:::
:::karte zusammenhang Addition von Leistungen
Wann addieren sich die Leistungen zweier Signale einfach, und was ergibt sich bei zwei gleichen oder zwei entgegengesetzten Signalen?
---
Nur wenn die Signale unkorreliert sind; sonst kommt der Kreuzterm $2\varphi_{uv}(0)$ hinzu. Zwei gleiche Signale ergeben deshalb die vierfache Leistung, zwei entgegengesetzte die Leistung null.
--- falsch
Immer, denn Leistungen sind nie negativ und addieren sich deshalb bei jeder Summe. Zwei gleiche Signale ergeben die doppelte Leistung, zwei entgegengesetzte ebenfalls die doppelte.
--- falsch
Nur wenn die Signale gleich sind; sonst fehlt der Kreuzterm $2\varphi_{uv}(0)$. Zwei gleiche Signale ergeben deshalb die doppelte Leistung, zwei entgegengesetzte die vierfache Leistung.
--- falsch
Nur wenn beide Signale mittelwertfrei sind; dann verschwindet der Kreuzterm $2\varphi_{uv}(0)$ von selbst. Zwei gleiche Signale ergeben die doppelte Leistung, zwei entgegengesetzte die Leistung null.
:::
:::karte zusammenhang Zwei Rauschquellen
Warum ergeben zwei mittelwertfreie Rauschspannungen mit 3 mV und 4 mV Effektivwert je nach ihrem Zusammenhang 5 mV, 7 mV oder 1 mV?
---
Weil sich die Varianzen samt Kreuzterm $2\mu_{uv}(0)$ addieren: unkorreliert $\sigma^2=9+16$, gleiche Form $\sigma^2=9+16+2\cdot12=49$, entgegengesetzte Form $\sigma^2=9+16-24=1$ (in mV$^2$). Die Wurzeln sind 5, 7 und 1 mV.
--- falsch
Weil sich die Varianzen immer zu $9+16=25$ mV$^2$ addieren, also 5 mV; die Werte 7 mV und 1 mV entstehen nur, wenn die Spannungen einen Gleichanteil haben, den die Korrelation vergrößert oder verkleinert.
--- falsch
Weil der Kreuzterm $2\mu_{uv}(0)$ zu den Effektivwerten hinzukommt, nicht zu den Varianzen: unkorreliert $3+4-2=5$, gleiche Form $3+4=7$, entgegengesetzte Form $4-3=1$, jeweils in mV, ohne dass man quadrieren muss.
--- falsch
Weil korrelierte Rauschspannungen Leistung austauschen: Bei gleicher Form gibt die kleinere ihre Leistung an die größere ab, bei entgegengesetzter Form verliert die größere ihre Leistung, und nur unkorreliert bleibt die Leistung erhalten.
:::
::::
