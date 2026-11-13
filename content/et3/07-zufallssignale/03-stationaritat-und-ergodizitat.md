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

::::formelsammlung
**Stationarität**

$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}$$

Für jede Verschiebung $t_0$ aller Beobachtungszeiten: Die Statistik ändert sich nicht mit der Zeit.

**Mittelwert und AKF eines stationären Prozesses**

$$m_s=\mathrm E\{s(t)\},\qquad\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$$

$m_s$ ist konstant; die AKF hängt nur vom Abstand $\tau=t_2-t_1$ ab.

**Ergodizität**

$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t$$

Für jedes $k$ und einen stationären Prozess: Eine einzige, lange beobachtete Musterfunktion zeigt alles, was die Schar zeigt. Nicht jeder stationäre Prozess ist ergodisch (Beispiel: ${}^ks(t)=c_k$).
::::

::::lernkarten
:::karte begriff stationär
Wann nennt man einen Zufallsprozess stationär, und was bedeutet das anschaulich für seine Statistik?
---
Wenn sich keiner seiner Mittelwerte ändert, wenn man alle Beobachtungszeiten um dieselbe Zeit $t_0$ verschiebt. Anschaulich ändert sich die Statistik des Prozesses nicht mit der Zeit.
--- falsch
Wenn sich jede seiner Musterfunktionen zeitlich nicht ändert, also konstant ist. Anschaulich steht das Signal still, und alle Werte einer Musterfunktion sind gleich groß.
--- falsch
Wenn jedes Zeitmittel einer Musterfunktion gleich dem entsprechenden Scharmittel ist. Anschaulich zeigt eine einzige lange Messung alles, was die ganze Schar zeigt.
--- falsch
Wenn sein Mittelwert null ist, auch wenn sich andere Mittelwerte mit der Zeit ändern. Anschaulich schwankt das Signal gleichmäßig um null, ohne jeden Gleichanteil.
:::
:::karte formel Bedingung für Stationarität
Welche Bedingung erfüllen die Mittelwerte eines stationären Prozesses für einen und für zwei Zeitpunkte?
---
$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\}$ und $\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}$ für jede Verschiebung $t_0$ aller Beobachtungszeiten.
--- falsch
$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\}$ und $\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2)]\}$: Es genügt, jeweils nur den ersten Zeitpunkt um $t_0$ zu verschieben.
--- falsch
$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}$ für jedes $k$ und jede Funktion $F$: Jedes Scharmittel stimmt mit dem Zeitmittel einer beliebigen Musterfunktion überein.
--- falsch
$\mathrm E\{F[s(t_1)]\}=0$ für jede Funktion $F$ und jeden Zeitpunkt $t_1$: Alle Mittelwerte verschwinden, und deshalb hängen sie auch nicht von der Zeit ab.
:::
:::karte formel AKF eines stationären Prozesses
Was folgt aus der Stationarität für den Mittelwert und die Autokorrelationsfunktion eines Prozesses?
---
Der Mittelwert $m_s=\mathrm E\{s(t)\}$ ist eine Konstante, und die AKF hängt nur noch vom Abstand $\tau=t_2-t_1$ ab: $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$.
--- falsch
Der Mittelwert $m_s$ ist null, und die AKF hängt nur noch vom ersten Zeitpunkt $t_1$ ab: $\varphi_{ss}(t_1)=\mathrm E\{s^2(t_1)\}$, weil sich der zweite Zeitpunkt herauskürzt.
--- falsch
Der Mittelwert $m_s=\mathrm E\{s(t)\}$ ist eine Konstante, und die AKF ist ebenfalls eine Konstante: $\varphi_{ss}=m_s^2$, unabhängig von beiden Zeitpunkten.
--- falsch
Der Mittelwert $m_s=\mathrm E\{s(t)\}$ ändert sich linear mit der Zeit, und die AKF hängt von der Summe $t_1+t_2$ der beiden Zeitpunkte ab, nicht von ihrem Abstand.
:::
:::karte begriff ergodisch
Wann heißt ein stationärer Prozess ergodisch, und was bedeutet das anschaulich?
---
Wenn außerdem jedes Zeitmittel einer Musterfunktion gleich dem entsprechenden Scharmittel ist. Anschaulich zeigt eine einzige, lange beobachtete Musterfunktion alles, was die ganze Schar zeigt.
--- falsch
Wenn alle seine Musterfunktionen gleich sind. Anschaulich liefert dann jede Messung denselben Verlauf, und man kann den Prozess wie ein bekanntes, vorhersagbares Signal behandeln.
--- falsch
Wenn sich keiner seiner Mittelwerte ändert, wenn man alle Beobachtungszeiten um dieselbe Zeit verschiebt. Anschaulich ändert sich die Statistik des Prozesses nicht mit der Zeit.
--- falsch
Wenn das Zeitmittel jeder Musterfunktion null ist. Anschaulich schwankt jede einzelne Messung gleichmäßig um null, auch wenn die Scharmittel des Prozesses davon abweichen.
:::
:::karte formel Bedingung für Ergodizität
Wie lautet die Bedingung für Ergodizität als Gleichung zwischen Scharmittel und Zeitmittel?
---
$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t$ für jedes $k$: Das Zeitmittel jeder einzelnen Musterfunktion stimmt mit dem Scharmittel überein.
--- falsch
$\mathrm E\{F[s(t)]\}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t$ für wenigstens ein $k$: Es genügt, dass eine einzige Musterfunktion im Zeitmittel das Scharmittel zeigt.
--- falsch
$\mathrm E\{F[s(t)]\}=\lim_{T\to\infty}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t$ für jedes $k$: Das Scharmittel ist das Integral über eine Musterfunktion, ohne Teilung durch die Dauer der Beobachtung.
--- falsch
$\mathrm E\{F[s(t)]\}=\mathrm E\{F[s(t+t_0)]\}$ für jede Verschiebung $t_0$: Das Scharmittel ändert sich nicht, wenn man den Beobachtungszeitpunkt um eine beliebige Zeit verschiebt.
:::
:::karte zusammenhang Stationär, aber nicht ergodisch
Warum ist ein Prozess aus Konstanten ${}^ks(t)=c_k$, deren Wert für jede Musterfunktion einmal gewürfelt wird, zwar stationär, aber nicht ergodisch?
---
Stationär ist er, weil nichts von $t$ abhängt. Das Zeitmittel einer Musterfunktion ist aber $c_k$ und für jede Musterfunktion anders, also nicht das Scharmittel: Eine einzelne Musterfunktion „sieht“ nie die anderen Werte.
--- falsch
Stationär ist er, weil jede Musterfunktion konstant ist. Ergodisch ist er nicht, weil das Scharmittel zu jedem Zeitpunkt einen anderen Wert hat, während jedes Zeitmittel über die ganze Zeit konstant bleibt.
--- falsch
Stationär ist er, weil nichts von $t$ abhängt. Ergodisch ist er nicht, weil das Zeitmittel einer Konstanten nicht definiert ist: Das Integral über unendlich lange Zeit wächst ohne Grenze.
--- falsch
Stationär ist er, weil der Würfel bei jedem Wurf dieselben Wahrscheinlichkeiten hat. Ergodisch ist er nicht, weil das Würfeln ein Vorgang ohne Zeitachse ist und Zeitmittel deshalb nichts aussagen.
:::
:::karte zusammenhang Rauschen mit einem einzigen Messgerät
Warum kann man das Rauschen eines Widerstands bei konstanter Temperatur mit einem einzigen Messgerät charakterisieren?
---
Weil dieses Rauschen ergodisch ist: Die Zeitmittel des einen gemessenen Signals sind gleich den Scharmitteln über alle gleich gebauten Widerstände. Sonst bräuchte man die ganze Schar.
--- falsch
Weil alle gleich gebauten Widerstände bei gleicher Temperatur genau dasselbe Rauschsignal erzeugen. Eine einzige Messung zeigt deshalb schon den Verlauf jeder Musterfunktion.
--- falsch
Weil das Rauschen eines Widerstands nur von der Temperatur abhängt und deshalb vorhersagbar ist. Das Messgerät prüft lediglich, ob die vorher berechnete Kurve stimmt.
--- falsch
Weil das Messgerät intern viele Widerstände parallel misst und über sie mittelt. So bildet es das Scharmittel unmittelbar, ohne jede Annahme über den Prozess.
:::
::::
