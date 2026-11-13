---
title: Stufe 6: Korrelation von Bandpasssignalen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260700
summary: Auch Korrelationsfunktionen von Bandpasssignalen rechnet man mit den komplexen Hüllkurven (Kapitel 5).
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Auch Korrelationsfunktionen von Bandpasssignalen rechnet man mit den komplexen Hüllkurven ([Kapitel 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)).
:::

Die KKF zweier reeller Bandpasssignale ist wieder ein Bandpasssignal:

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

Das gespiegelte Signal hat die Hüllkurve $s_T^*(-t)$, denn

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

Mit der Übertragungsregel $g_T=\frac12s_T*h_T$ aus [Kapitel 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html):

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**So liest man das:** Die Korrelation zweier Bandpasssignale ist die halbe Korrelation ihrer Hüllkurven, aufmoduliert auf den Träger. Die Energie eines Bandpasssignals ist die halbe Energie seiner komplexen Hüllkurve: Ein Kosinus der Amplitude $|s_T|$ hat im Mittel nur die halbe Leistung.

::::formelsammlung
**KKF zweier Bandpasssignale**

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}$$

Die KKF zweier reeller Bandpasssignale ist wieder ein Bandpasssignal mit der komplexen Hüllkurve $\varphi^E_{sgT}$.

**Korrelation der komplexen Hüllkurven**

$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t$$

Die halbe Korrelation der Hüllkurven. Der Faktor $\frac12$ stammt aus der Übertragungsregel $g_T=\frac12s_T*h_T$, denn das gespiegelte Signal $s(-t)$ hat die Hüllkurve $s_T^*(-t)$.

**Energie eines Bandpasssignals**

$$E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0)$$

Die halbe Energie der komplexen Hüllkurve: Ein Kosinus der Amplitude $|s_T|$ hat im Mittel nur die halbe Leistung.
::::

::::lernkarten
:::karte formel KKF zweier Bandpasssignale
Wie berechnet man die KKF zweier reeller Bandpasssignale aus ihren komplexen Hüllkurven $s_T$ und $g_T$?
---
$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}$ mit $\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]$: Man korreliert die Hüllkurven, halbiert und moduliert das Ergebnis auf den Träger.
--- falsch
$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}$ mit $\varphi^E_{sgT}(\tau)=s_T^*(-\tau)*g_T(\tau)$: Man korreliert die Hüllkurven ohne Faktor, weil die Korrelation kein System ist.
--- falsch
$\varphi^E_{sg}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]$: Die KKF zweier Bandpasssignale ist ein Tiefpasssignal, weil sich die Träger der beiden Signale bei der Korrelation gegenseitig aufheben.
--- falsch
$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}4\pi f_0\tau}\bigr\}$ mit $\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]$: Das Produkt zweier Bandpasssignale liegt bei der doppelten Trägerfrequenz.
:::
:::karte zusammenhang Hüllkurve des gespiegelten Signals
Warum hat das gespiegelte Bandpasssignal $s(-t)$ die komplexe Hüllkurve $s_T^*(-t)$ und nicht $s_T(-t)$?
---
Beim Spiegeln dreht der Träger rückwärts: $s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}$. Weil eine Zahl und ihre Konjugierte denselben Realteil haben, ist das $\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$; zum gewohnten Träger gehört also $s_T^*(-t)$.
--- falsch
Weil die Korrelation stets mit dem konjugierten Signal rechnet; die Konjugation gehört zur Definition der Korrelationsfunktion und nicht zur Spiegelung. Ohne Korrelation hätte $s(-t)$ die Hüllkurve $s_T(-t)$.
--- falsch
Weil beim Spiegeln die Trägerfrequenz von $f_0$ auf $2f_0$ springt und die Hüllkurve diesen Sprung durch die Konjugation ausgleicht; der Träger selbst bleibt dabei unverändert.
--- falsch
Weil eine reelle Hüllkurve beim Spiegeln ihr Vorzeichen wechselt; die Konjugation dreht dieses Vorzeichen zurück, sodass $s(-t)$ dieselbe Hüllkurve behält wie $s(t)$.
:::
:::karte herleitung Korrelation der Hüllkurven
Wie folgt aus $\varphi^E_{sg}(\tau)=s^*(-\tau)*g(\tau)$ die Korrelation zweier reeller Bandpasssignale über ihre komplexen Hüllkurven?
---
Man fasst die Korrelation als Faltung des gespiegelten Signals mit $g(\tau)$ auf, weil bei reellen Signalen das Konjugieren nichts ändert.
---
Das gespiegelte Signal ist wieder ein Bandpasssignal mit der Hüllkurve $s_T^*(-t)$, weil $s(-t)=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$ gilt.
---
Man faltet zwei Bandpasssignale und wendet die Übertragungsregel $g_T=\frac12s_T*h_T$ an, weil die Faltung zweier Bandpasssignale im Tiefpassbereich die halbe Faltung ihrer Hüllkurven ist.
---
Es folgt $\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]$ und $\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}$, weil das Ergebnis wieder auf den Träger moduliert wird.
:::
:::karte zusammenhang Faktor ein Halb bei der Korrelation
Woher kommt der Faktor $\frac12$ in der Korrelation der komplexen Hüllkurven zweier Bandpasssignale?
---
Aus der Übertragungsregel $g_T=\frac12s_T*h_T$: Die Korrelation ist eine Faltung mit dem gespiegelten Bandpasssignal, und eine Faltung zweier Bandpasssignale bringt im Tiefpassbereich den Faktor $\frac12$ mit.
--- falsch
Aus der Normierung: Man teilt durch die Energie der beiden Hüllkurven, die bei Bandpasssignalen doppelt so groß ist wie die Energie der Signale selbst, damit der Wert bei $\tau=0$ stimmt.
--- falsch
Aus der Spiegelung: Ein gespiegeltes Bandpasssignal hat nur die halbe Amplitude, weil sein Träger rückwärts dreht und dabei die Hälfte seiner Energie verliert.
--- falsch
Aus der Bandbreite: Die KKF zweier Bandpasssignale ist doppelt so breit wie die Signale selbst, deshalb muss man ihre Hüllkurve halbieren, damit die Fläche unter der KKF gleich bleibt.
:::
:::karte formel Energie eines Bandpasssignals
Wie hängt die Energie eines Bandpasssignals mit der Energie seiner komplexen Hüllkurve zusammen?
---
$E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0)$, und das ist die halbe Energie der komplexen Hüllkurve: Ein Kosinus der Amplitude $|s_T|$ hat im Mittel nur die halbe Leistung.
--- falsch
$E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0)$, und das ist die volle Energie der komplexen Hüllkurve: Der Träger ändert die Energie nicht, weil sein Betrag $|\mathrm{e}^{\mathrm{j}2\pi f_0t}|=1$ ist.
--- falsch
Die Energie des Bandpasssignals ist die doppelte Energie seiner komplexen Hüllkurve, weil Realteil und Imaginärteil der Hüllkurve zwei Signale ergeben, die beide Energie tragen.
--- falsch
Die Energie des Bandpasssignals ist die Energie der Hüllkurve mal $\frac{1}{\sqrt2}$, weil der Effektivwert eines Kosinus das $\frac{1}{\sqrt2}$-Fache seiner Amplitude ist.
:::
::::
