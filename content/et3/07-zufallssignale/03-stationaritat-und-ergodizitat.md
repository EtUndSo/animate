---
title: Stufe 2: Stationarität und Ergodizität
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270300
summary: Eine unendliche Schar hat man nie, meist nur ein einziges Signal.
tags: stationär, ergodisch
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine unendliche Schar hat man nie, meist nur ein einziges Signal. Wann genügt es?
:::

Ein Prozess heißt __stationär__, wenn sich keine seiner Mittelwerte ändern, wenn man alle Beobachtungszeiten um dieselbe Zeit $t_0$ verschiebt:

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

Dann ist der Mittelwert $m_s=\mathrm E\{s(t)\}$ eine Konstante, und die AKF hängt nur noch vom Abstand $\tau=t_2-t_1$ ab: $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$. Ein stationärer Prozess heißt __ergodisch__, wenn außerdem jedes Zeitmittel einer Musterfunktion gleich dem entsprechenden Scharmittel ist:

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{für jedes }k. \tag{2.2}$$

⁠**So liest man das:** Stationär heißt, die Statistik ändert sich nicht mit der Zeit. Ergodisch heißt, eine einzige, lange beobachtete Musterfunktion zeigt im Lauf der Zeit alles, was die ganze Schar zeigt. Das Rauschen eines Widerstands bei konstanter Temperatur ist ergodisch. Nur deshalb kann man Rauschen mit einem einzigen Messgerät charakterisieren.

:::frage Ist jeder stationäre Prozess auch ergodisch?
Nein. Beispiel: Jede Musterfunktion ist eine Konstante, deren Wert einmal gewürfelt wird, ${}^ks(t)=c_k$. Der Prozess ist stationär, denn nichts hängt von $t$ ab. Das Zeitmittel einer Musterfunktion ist aber $c_k$, und das ist für jede Musterfunktion anders, nicht das Scharmittel. Eine einzelne Musterfunktion „sieht“ nie die anderen Werte.
:::
