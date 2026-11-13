---
title: Stufe 9: Hilbert-Transformation und analytisches Signal
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3231000
summary: Bei einem kausalen Signal hängen Real- und Imaginärteil des Spektrums zusammen: Der eine legt den anderen fest.
tags: Hilbert-Transformation, Hauptwert, analytische Komponente, Allpass
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Bei einem kausalen Signal hängen Real- und Imaginärteil des Spektrums zusammen: Der eine legt den anderen fest. Dieselbe Rechnung liefert ein Signal, das nur positive Frequenzen enthält.
:::

**Kausale Signale.** Ist $s(t)=0$ für $t<0$, dann sind gerader und ungerader Anteil für $t>0$ gleich ($\frac12s$) und für $t<0$ entgegengesetzt. Also $s_u(t)=s_g(t)\operatorname{sgn}(t)$ und $s_g(t)=s_u(t)\operatorname{sgn}(t)$. Im Frequenzbereich wird die Multiplikation mit $\operatorname{sgn}$ zur Faltung mit $\frac{1}{\mathrm{j}\pi f}$:

:::satz Satz 9.1 (Hilbert-Beziehung kausaler Signale)
<span class="anker" id="satz-9-1"></span>

Für ein kausales Signal gilt

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**So liest man das:** Die Faltung mit $\frac{1}{\pi f}$ heißt __Hilbert-Transformation__. Ihr Integral existiert nur als __Hauptwert__: Um die Stelle, an der der Kern unendlich wird, spart man ein symmetrisches Stück aus und lässt es gegen null schrumpfen. Bei einem kausalen System genügt es, den Realteil des Frequenzgangs zu kennen, der Imaginärteil folgt daraus. Kausalität ist also eine starke Einschränkung für das Spektrum.

**Analytische Komponente.** Mit dem Sprung im *Frequenzbereich* schneidet man die negativen Frequenzen ab: $S_+(f)=S(f)\,\varepsilon(f)$. Aus der Symmetrie folgt $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, also

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ heißt __analytische Komponente__, $\hat s$ die Hilbert-Transformierte von $s$; auch die Faltung mit $\frac{1}{\pi t}$ ist als Hauptwert gemeint. Ebenso enthält $S_-(f)=S(f)\,\varepsilon(-f)$ mit der Zeitfunktion $s_-(t)$ nur die negativen Frequenzen. Für reelle Signale ist $S_-(f)=S_+^*(-f)$, also $s_-=s_+^*$ und $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. Real- und Imaginärteil von $s_+$ sind wieder Hilbert-Transformierte voneinander.

**Der Hilbert-Transformator.** Das LTI-System mit $h(t)=\frac{1}{\pi t}$ hat $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: Betrag 1 bei allen Frequenzen (ein __Allpass__), Phase $-90^\circ$ für $f>0$ und $+90^\circ$ für $f<0$. Aus $\cos(2\pi Ft)$ macht er

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**Kurz gesagt:** Der Hilbert-Transformator dreht jede Schwingung um $90^\circ$, ohne ihre Amplitude zu ändern.

:::aufgabe Aufgabe 12 ★★ Hilbert-Transformator
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Was macht der Hilbert-Transformator aus $\sin(2\pi Ft)$? Was ergibt zweimaliges Anwenden?

</li>

<li>

Bestimme die analytische Komponente $s_+(t)$ von $\cos(2\pi Ft)$ und prüfe $s=2\operatorname{Re}\{s_+\}$.

</li>

<li>

Warum ist der Hilbert-Transformator nicht kausal? Schau auf $h(t)$.

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$. Multiplikation mit $-\mathrm{j}\operatorname{sgn}(f)$: bei $-F$ mit $+\mathrm{j}$, bei $+F$ mit $-\mathrm{j}$. Ergebnis $-\frac12\delta(f+F)-\frac12\delta(f-F)$, also $-\cos(2\pi Ft)$. Zweimal angewandt: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$, das Signal wird invertiert.

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$, also $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$. Das passt zu $\frac12(s+\mathrm{j}\hat s)$ mit $\hat s=\sin$. $2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$.

(c) $h(t)=\frac{1}{\pi t}$ ist auch für $t<0$ von null verschieden. Der Ausgang zur Zeit $t$ hängt also von zukünftigen Eingangswerten ab. In der Praxis nähert man den Hilbert-Transformator mit einer abgeschnittenen Impulsantwort und nimmt dafür eine Verzögerung in Kauf.
:::
:::

::::kurzfassung
Bei einem kausalen Signal legt der Realteil des Spektrums den Imaginärteil fest und umgekehrt. Dieselbe Rechnung liefert ein Signal, das nur positive Frequenzen enthält.

Ein Signal heißt __kausal__, wenn $s(t)=0$ für $t<0$ gilt. Dann sind gerader und ungerader Anteil für $t>0$ gleich und für $t<0$ entgegengesetzt, also $s_u(t)=s_g(t)\operatorname{sgn}(t)$. Die Multiplikation mit $\operatorname{sgn}(t)$ wird im Frequenzbereich zur Faltung mit $\frac{1}{\mathrm{j}\pi f}$:

$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}.$$

Die Faltung mit $\frac{1}{\pi f}$ heißt __Hilbert-Transformation__. Ihr Integral nimmt man als __Hauptwert__: Um die Stelle, an der der Kern unendlich wird, spart man ein symmetrisches Stück aus und lässt es gegen null schrumpfen. Schneidet man die negativen Frequenzen ab, $S_+(f)=S(f)\,\varepsilon(f)$, entsteht die __analytische Komponente__ $s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t)$ mit der Hilbert-Transformierten $\hat s(t)=s(t)*\frac{1}{\pi t}$. Für reelle Signale gilt $s(t)=2\operatorname{Re}\{s_+(t)\}$.

Der Grund: Das System mit $h(t)=\frac{1}{\pi t}$, der __Hilbert-Transformator__, hat $H(f)=-\mathrm{j}\operatorname{sgn}(f)$. Es ist ein __Allpass__, ändert also keinen Betrag, und dreht jede Schwingung um $90^\circ$. Aus $\cos(2\pi Ft)$ wird so $\sin(2\pi Ft)$.

Falle: Die Phase ist nur für $f>0$ gleich $-90^\circ$, für $f<0$ ist sie $+90^\circ$. Nur so bleibt ein reelles Signal reell, denn seine Schwingungen treten in konjugierten Paaren auf.
::::

::::formelsammlung
**Kausales Signal**

$$s_u(t)=s_g(t)\operatorname{sgn}(t),\qquad s_g(t)=s_u(t)\operatorname{sgn}(t)$$

Für $s(t)=0$ bei $t<0$: Gerader und ungerader Anteil sind für $t>0$ gleich ($\frac12s$), für $t<0$ entgegengesetzt.

**Hilbert-Beziehung kausaler Signale**

$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}$$

Die Faltung mit $\frac{1}{\pi f}$ heißt Hilbert-Transformation; ihr Integral als Hauptwert (symmetrisch ausgesparte, gegen null schrumpfende Umgebung der Stelle, an der der Kern unendlich wird). Bei einem kausalen System legt der Realteil des Frequenzgangs den Imaginärteil fest.

**Analytische Komponente im Frequenzbereich**

$$S_+(f)=S(f)\,\varepsilon(f)$$

Die negativen Frequenzen werden abgeschnitten.

**Sprung im Frequenzbereich**

$$\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$$

Folgt mit der Symmetrie aus dem Spektrum des Sprungs.

**Analytische Komponente und Hilbert-Transformierte**

$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f)$$

$\hat s$ Hilbert-Transformierte von $s$; das Faltungsintegral ebenfalls als Hauptwert.

**Reelle Signale**

$$S_-(f)=S_+^*(-f),\qquad s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$$

$S_-(f)=S(f)\,\varepsilon(-f)$ und $s_-$ sind der Anteil der negativen Frequenzen; für reelle Signale ist $s_-=s_+^*$. Für reelles $s$ ist der Imaginärteil von $s_+$ die Hilbert-Transformierte seines Realteils.

**Hilbert-Transformator**

$$h(t)=\frac{1}{\pi t},\qquad H(f)=-\mathrm{j}\operatorname{sgn}(f)$$

Allpass: Betrag 1 bei allen Frequenzen; Phase $-90^\circ$ für $f>0$ und $+90^\circ$ für $f<0$. Nicht kausal, denn $h(t)$ ist auch für $t<0$ von null verschieden.

**Hilbert-Transformierte von Kosinus und Sinus**

$$\cos(2\pi Ft)\;\to\;\sin(2\pi Ft),\qquad\sin(2\pi Ft)\;\to\;-\cos(2\pi Ft)$$

Zweimal angewandt: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$, das Signal wird invertiert.
::::

::::lernkarten
:::karte zusammenhang kausal
Warum hängen bei einem kausalen Signal, also $s(t)=0$ für $t<0$, der gerade und der ungerade Anteil zusammen?
---
Für $t>0$ fällt der gespiegelte Teil weg, beide Anteile sind gleich $\frac12s$. Für $t<0$ ist $s(t)=0$, und die Anteile sind entgegengesetzt gleich. Deshalb gilt $s_u(t)=s_g(t)\operatorname{sgn}(t)$ und $s_g(t)=s_u(t)\operatorname{sgn}(t)$.
--- falsch
Für $t>0$ ist der gerade Anteil gleich $s$ und der ungerade null, für $t<0$ ist es umgekehrt. Deshalb gilt zwar $s_u(t)=s_g(t)\operatorname{sgn}(t)$, aber nicht umgekehrt; der gerade Anteil legt den ungeraden also nicht fest.
--- falsch
Weil bei einem kausalen Signal der ungerade Anteil immer null ist: Ein Signal, das erst bei $t=0$ beginnt, kann nicht punktsymmetrisch sein. Der gerade Anteil ist dann das ganze Signal, und der ungerade fehlt.
--- falsch
Für $t>0$ sind beide Anteile gleich $\frac12s$, für $t<0$ ebenfalls gleich. Deshalb gilt $s_u(t)=s_g(t)$ für alle $t$, und Real- und Imaginärteil des Spektrums sind bis auf den Faktor $\mathrm{j}$ gleich.
:::
:::karte formel Hilbert-Beziehung kausaler Signale
Wie hängen Real- und Imaginärteil des Spektrums eines kausalen Signals zusammen?
---
$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f}$ und $\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}$: Jeder Teil folgt aus dem anderen durch Faltung mit $\frac{1}{\pi f}$, beim Imaginärteil mit Minuszeichen.
--- falsch
$\operatorname{Re}\{S(f)\}=-\operatorname{Im}\{S(f)\}*\frac{1}{\pi f}$ und $\operatorname{Im}\{S(f)\}=\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}$: Jeder Teil folgt aus dem anderen durch Faltung mit $\frac{1}{\pi f}$, beim Realteil mit Minuszeichen.
--- falsch
$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}\cdot\frac{1}{\pi f}$ und $\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}\cdot\frac{1}{\pi f}$: Jeder Teil folgt aus dem anderen durch Multiplikation mit $\frac{1}{\pi f}$, beim Imaginärteil mit Minuszeichen.
--- falsch
$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}$: Real- und Imaginärteil sind gleich, weil gerader und ungerader Anteil eines kausalen Signals für $t>0$ übereinstimmen und $t<0$ nichts beiträgt.
:::
:::karte herleitung Hilbert-Beziehung aus der Kausalität
Wie folgt aus $s_u(t)=s_g(t)\operatorname{sgn}(t)$ für ein kausales Signal, dass $\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}$ ist?
---
Man transformiert beide Seiten, weil die Spektren der beiden Anteile bekannt sind: $s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\}$ und $s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}$.
---
Die Multiplikation mit $\operatorname{sgn}(t)$ wird zur Faltung mit dessen Spektrum $\frac{1}{\mathrm{j}\pi f}$, weil ein Produkt im Zeitbereich eine Faltung im Frequenzbereich ist. Also ist $\mathrm{j}\operatorname{Im}\{S(f)\}$ gleich $\operatorname{Re}\{S(f)\}$ gefaltet mit $\frac{1}{\mathrm{j}\pi f}$.
---
Man teilt durch $\mathrm{j}$, weil links nur der Imaginärteil stehen soll. Rechts wird dadurch zweimal durch $\mathrm{j}$ geteilt, und das ist eine Multiplikation mit $-1$: Es ergibt sich $\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}$.
---
Ebenso folgt aus $s_g(t)=s_u(t)\operatorname{sgn}(t)$ die Beziehung $\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f}$, weil sich dort das $\mathrm{j}$ des ungeraden Anteils gegen das $\mathrm{j}$ im Nenner kürzt.
:::
:::karte begriff Hilbert-Transformation
Was versteht man unter der Hilbert-Transformation, und wo tritt sie auf?
---
Die Faltung mit $\frac{1}{\pi f}$, im Zeitbereich entsprechend mit $\frac{1}{\pi t}$, gebildet als Hauptwert. Sie verbindet Real- und Imaginärteil des Spektrums eines kausalen Signals; im Zeitbereich liefert $\hat s(t)=s(t)*\frac{1}{\pi t}$ die Hilbert-Transformierte von $s$.
--- falsch
Die Multiplikation mit $\frac{1}{\pi f}$, die im Frequenzbereich hohe Frequenzen dämpft. Sie verbindet Betrag und Phase des Spektrums eines stabilen Signals; im Zeitbereich entspricht sie der Integration des Signals über die Zeit.
--- falsch
Die Faltung mit $\operatorname{sgn}(f)$, gebildet als gewöhnliches Integral. Sie trennt die positiven von den negativen Frequenzen eines Signals; im Zeitbereich liefert sie die Ableitung des Signals nach der Zeit.
--- falsch
Die Faltung mit $\frac{1}{\pi f}$, gebildet als gewöhnliches Integral über alle Frequenzen. Sie verbindet Real- und Imaginärteil des Spektrums jedes reellen Signals, gleich ob es kausal ist oder nicht.
:::
:::karte begriff Hauptwert
Was bedeutet es, dass das Integral der Hilbert-Transformation als Hauptwert genommen wird?
---
Um die Stelle, an der der Kern wie $\frac{1}{\pi f}$ unendlich wird, spart man ein symmetrisches Stück aus und lässt es gegen null schrumpfen. Nur in diesem Sinn existiert das Integral.
--- falsch
Man nimmt vom Integral nur den Betrag, weil der Kern $\frac{1}{\pi f}$ das Vorzeichen wechselt und sich positive und negative Beiträge sonst aufheben würden. Ohne Betrag wäre das Integral stets null.
--- falsch
Man berechnet das Integral nur an seinem Hauptbeitrag, der Stelle, an der der Kern unendlich wird, und vernachlässigt den Rest. Das ergibt eine Näherung, die für schmale Spektren gut ist.
--- falsch
Um die Stelle, an der der Kern unendlich wird, spart man ein festes Stück der Breite 1 aus. Was darin liegt, ersetzt man durch den Mittelwert des Signals, damit das Integral endlich bleibt.
:::
:::karte zusammenhang Kausalität legt das Spektrum fest
Warum genügt es bei einem kausalen System, den Realteil seines Frequenzgangs zu kennen?
---
Weil sich der Imaginärteil daraus mit der Hilbert-Beziehung berechnen lässt: Bei einem kausalen Signal legt der gerade Anteil, der den Realteil liefert, den ungeraden fest. Kausalität schränkt das Spektrum also stark ein.
--- falsch
Weil der Frequenzgang eines kausalen Systems immer reell ist. Ein Imaginärteil entstünde nur, wenn das System auf zukünftige Eingangswerte reagieren könnte, und das ist bei kausalen Systemen ja gerade ausgeschlossen.
--- falsch
Weil sich der Imaginärteil daraus durch Ableiten nach $f$ ergibt. Real- und Imaginärteil des Frequenzgangs hängen wie Kosinus und Sinus zusammen, und der Sinus ist bis auf das Vorzeichen die Ableitung des Kosinus.
--- falsch
Es genügt nicht: Real- und Imaginärteil sind auch bei kausalen Systemen unabhängig voneinander. Man braucht immer beide, weil erst sie zusammen Betrag und Phase des Frequenzgangs festlegen, und die Kausalität ändert daran nichts.
:::
:::karte begriff analytische Komponente
Was ist die analytische Komponente $s_+(t)$ eines Signals, und wie hängt sie mit der Hilbert-Transformierten $\hat s(t)$ zusammen?
---
Das Signal, dessen Spektrum nur die positiven Frequenzen enthält: $S_+(f)=S(f)\,\varepsilon(f)$. Im Zeitbereich ist $s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t)$ mit $\hat s(t)=s(t)*\frac{1}{\pi t}$.
--- falsch
Das Signal, dessen Spektrum nur die positiven Frequenzen enthält: $S_+(f)=S(f)\,\varepsilon(f)$. Im Zeitbereich ist $s_+(t)=s(t)+\mathrm{j}\,\hat s(t)$, ohne Faktor $\frac12$, weil das Abschneiden die Amplitude nicht ändert.
--- falsch
Der kausale Teil des Signals, also das Signal für $t>0$: $s_+(t)=s(t)\,\varepsilon(t)$. Er hängt mit der Hilbert-Transformierten zusammen, weil Real- und Imaginärteil seines Spektrums Hilbert-Transformierte sind.
--- falsch
Der Realteil des Signals, $s_+(t)=\operatorname{Re}\{s(t)\}$, der für reelle Signale mit dem Signal übereinstimmt. Die Hilbert-Transformierte liefert dazu den Imaginärteil des Signals, $\hat s(t)=\operatorname{Im}\{s(t)\}$.
:::
:::karte herleitung Analytische Komponente aus dem Sprung im Frequenzbereich
Wie gewinnt man aus $S_+(f)=S(f)\,\varepsilon(f)$ die Zeitfunktion $s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t)$?
---
Die Multiplikation mit $\varepsilon(f)$ im Frequenzbereich wird zur Faltung mit der Zeitfunktion von $\varepsilon(f)$, weil Faltung und Multiplikation einander entsprechen.
---
Diese Zeitfunktion folgt aus dem Spektrum des Sprungs mit der Symmetrie: $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, weil die Symmetrie die Rollen von Zeit und Frequenz vertauscht.
---
Die Faltung mit $\frac12\delta(t)$ liefert $\frac12s(t)$, weil die Faltung mit dem Dirac-Impuls das Signal unverändert lässt.
---
Die Faltung mit $\frac{\mathrm{j}}{2\pi t}$ liefert $\frac{\mathrm{j}}{2}\,\hat s(t)$ mit $\hat s(t)=s(t)*\frac{1}{\pi t}$, weil sich der konstante Faktor $\frac{\mathrm{j}}{2}$ vor die Faltung ziehen lässt.
:::
:::karte formel Reelles Signal aus der analytischen Komponente
Wie gewinnt man ein reelles Signal $s(t)$ aus seiner analytischen Komponente $s_+(t)$ zurück, und warum?
---
$s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. Der Anteil $s_-$ der negativen Frequenzen ist bei reellen Signalen wegen $S_-(f)=S_+^*(-f)$ gleich $s_+^*$, und eine Zahl plus ihre konjugierte ist das Doppelte ihres Realteils.
--- falsch
$s(t)=\operatorname{Re}\{s_+(t)\}$. Die analytische Komponente enthält bereits das ganze Signal in ihrem Realteil, und der Imaginärteil ist nur die Hilbert-Transformierte, die man beim Zurückgewinnen einfach weglässt.
--- falsch
$s(t)=2|s_+(t)|$. Der Anteil der negativen Frequenzen hat bei reellen Signalen denselben Betrag wie der der positiven, und die Beträge beider Anteile addieren sich zum Signal, zu jeder Zeit $t$.
--- falsch
$s(t)=s_+(t)-s_+^*(t)$. Der Anteil der negativen Frequenzen ist bei reellen Signalen $-s_+^*$, und eine Zahl minus ihre konjugierte ist das Doppelte ihres Realteils, also wieder reell.
:::
:::karte begriff Hilbert-Transformator
Was ist der Hilbert-Transformator, und welchen Frequenzgang hat er?
---
Das LTI-System mit der Impulsantwort $h(t)=\frac{1}{\pi t}$; es bildet die Hilbert-Transformierte. Sein Frequenzgang ist $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: Betrag 1 bei allen Frequenzen, Phase $-90^\circ$ für $f>0$ und $+90^\circ$ für $f<0$.
--- falsch
Das LTI-System mit der Impulsantwort $h(t)=\frac{1}{\pi t}$; es bildet die Hilbert-Transformierte. Sein Frequenzgang ist $H(f)=\frac{1}{\mathrm{j}\pi f}$: Sein Betrag fällt mit $1/f$ ab, und die Phase ist bei allen Frequenzen $-90^\circ$.
--- falsch
Das LTI-System mit der Impulsantwort $h(t)=\operatorname{sgn}(t)$; es bildet die Hilbert-Transformierte. Sein Frequenzgang ist $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: Betrag 1 bei allen Frequenzen, Phase $-90^\circ$ für $f>0$.
--- falsch
Das LTI-System mit der Impulsantwort $h(t)=\frac{1}{\pi t}$; es bildet die Hilbert-Transformierte. Sein Frequenzgang ist $H(f)=-\mathrm{j}$: Betrag 1 und Phase $-90^\circ$ bei allen Frequenzen, positiven wie negativen.
:::
:::karte begriff Allpass
Was ist ein Allpass, und warum ist der Hilbert-Transformator einer?
---
Ein System, dessen Frequenzgang bei allen Frequenzen den Betrag 1 hat: Es ändert keine Amplitude, nur die Phase. Der Hilbert-Transformator mit $H(f)=-\mathrm{j}\operatorname{sgn}(f)$ hat diesen Betrag bei allen Frequenzen.
--- falsch
Ein System, das alle Frequenzen durchlässt, ohne irgendetwas an ihnen zu verändern, also weder Amplitude noch Phase. Der Hilbert-Transformator ist einer, weil er bei keiner einzigen Frequenz sperrt.
--- falsch
Ein System, dessen Phase bei allen Frequenzen gleich ist, während der Betrag beliebig sein darf. Der Hilbert-Transformator ist einer, weil er jede Schwingung um denselben Winkel von $90^\circ$ dreht.
--- falsch
Ein Filter, das alle Frequenzen oberhalb einer Grenze durchlässt und darunter sperrt, also ein Hochpass ohne obere Grenze. Der Hilbert-Transformator ist einer, weil er bei $f=0$ den Wert null hat.
:::
:::karte zusammenhang Kosinus wird Sinus
Was macht der Hilbert-Transformator aus $\cos(2\pi Ft)$ und aus $\sin(2\pi Ft)$, und was ergibt zweimaliges Anwenden?
---
Aus $\cos(2\pi Ft)$ wird $\sin(2\pi Ft)$, aus $\sin(2\pi Ft)$ wird $-\cos(2\pi Ft)$: Er dreht jede Schwingung um $90^\circ$, ohne ihre Amplitude zu ändern. Zweimal angewandt gilt $(-\mathrm{j}\operatorname{sgn}f)^2=-1$, das Signal wird invertiert.
--- falsch
Aus $\cos(2\pi Ft)$ wird $-\sin(2\pi Ft)$, aus $\sin(2\pi Ft)$ wird $\cos(2\pi Ft)$: Er dreht jede Schwingung um $90^\circ$ in Gegenrichtung. Zweimal angewandt ergibt das ursprüngliche Signal, weil sich zwei Drehungen aufheben.
--- falsch
Aus $\cos(2\pi Ft)$ wird $\sin(2\pi Ft)$, aus $\sin(2\pi Ft)$ wird $\cos(2\pi Ft)$: Er vertauscht Kosinus und Sinus. Zweimal angewandt ergibt das ursprüngliche Signal, denn zweimaliges Vertauschen stellt alles wieder her.
--- falsch
Aus $\cos(2\pi Ft)$ wird $\frac{1}{2\pi F}\sin(2\pi Ft)$, er integriert also das Signal. Zweimal angewandt ergibt $-\frac{1}{(2\pi F)^2}\cos(2\pi Ft)$, das Signal wird invertiert und zugleich geschwächt.
:::
:::karte zusammenhang Phase für positive und negative Frequenzen
Warum dreht der Hilbert-Transformator die Phase für $f>0$ um $-90^\circ$, für $f<0$ dagegen um $+90^\circ$?
---
Nur so bleibt ein reelles Signal reell. Seine Schwingungen treten in konjugierten Paaren auf, und ein Paar bleibt nur dann konjugiert, wenn die Phasendrehungen bei $f$ und $-f$ entgegengesetzt sind.
--- falsch
Weil negative Frequenzen rückwärts laufende Zeit bedeuten. Eine Verzögerung um eine Viertelperiode wird bei rückwärts laufender Zeit zu einer Voreilung, deshalb wechselt das Vorzeichen der Phase.
--- falsch
Das ist eine Folge der Kausalität: Ein kausales System muss bei negativen Frequenzen voreilen, damit sein Ausgang nicht vor dem Eingang beginnt. Der Hilbert-Transformator ist deshalb kausal.
--- falsch
Weil der Frequenzgang bei $f=0$ springen muss, damit er den Betrag 1 behält. Mit derselben Phase auf beiden Seiten wäre er bei $f=0$ null, und der Gleichanteil ginge verloren.
:::
:::karte zusammenhang Hilbert-Transformator nicht kausal
Warum ist der Hilbert-Transformator nicht kausal, und wie nähert man ihn in der Praxis an?
---
Seine Impulsantwort $h(t)=\frac{1}{\pi t}$ ist auch für $t<0$ von null verschieden, der Ausgang zur Zeit $t$ hängt also von zukünftigen Eingangswerten ab. Man nähert ihn mit einer abgeschnittenen Impulsantwort und nimmt dafür eine Verzögerung in Kauf.
--- falsch
Weil sein Frequenzgang komplex ist; ein kausales System muss einen reellen Frequenzgang haben. Man nähert ihn an, indem man nur den Betrag 1 verwirklicht und die Phasendrehung einfach weglässt, die ohnehin kaum auffällt.
--- falsch
Weil seine Impulsantwort $h(t)=\frac{1}{\pi t}$ bei $t=0$ unendlich wird. Man nähert ihn an, indem man diesen einen Wert durch einen großen, endlichen Wert ersetzt; eine Verzögerung ist dafür nicht nötig.
--- falsch
Er ist kausal, weil seine Impulsantwort für $t<0$ negativ ist und negative Werte der Impulsantwort keine Wirkung haben. Man kann ihn deshalb ohne Näherung und ohne jede Verzögerung bauen.
:::
::::
