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
