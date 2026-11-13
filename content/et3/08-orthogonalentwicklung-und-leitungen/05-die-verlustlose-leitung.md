---
title: Stufe 4: Die verlustlose Leitung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Orthogonalentwicklung und Leitungen
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Kapitel 8: Orthogonalentwicklung und Leitungen
order: 3280500
summary: Ohne Verluste ( R'=G'=0 ) werden Wellenwiderstand und Geschwindigkeit frequenzunabhängig.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Ohne Verluste ($R'=G'=0$) werden Wellenwiderstand und Geschwindigkeit frequenzunabhängig. Dann gilt die Wellenlösung für beliebige Signale, nicht nur für Sinusschwingungen.
:::

Mit $R'=G'=0$ wird $\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$: keine Dämpfung ($\alpha=0$) und $\beta$ proportional zu $f$. Daraus:

<span class="anker" id="gl-4-1"></span>
$$Z=\sqrt{\frac{L'}{C'}},\qquad v=\frac{1}{\sqrt{L'C'}},\qquad\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}. \tag{4.1}$$

:::satz Satz 4.1 (d'Alembert-Lösung)
<span class="anker" id="satz-4-1"></span>

Jede Lösung der Wellengleichung [(4.1)](#gl-4-1) hat die Form

<span class="anker" id="gl-4-2"></span>
$$u(s,t)=u_\mathrm{hin}(s-vt)+u_\mathrm{rück}(s+vt) \tag{4.2}$$

mit beliebigen (zweimal differenzierbaren) Funktionen $u_\mathrm{hin}$ und $u_\mathrm{rück}$.
:::

⁠**So liest man das:** Eine beliebige Signalform läuft unverändert mit der Geschwindigkeit $v$ die Leitung entlang. Das liegt daran, dass alle Frequenzanteile gleich schnell sind und gleich wenig gedämpft werden: Die Leitung ist ein verzerrungsfreies System im Sinne von [Kapitel 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html), mit der Verzögerung $l/v$. Die Wellengleichung für $u$ folgt aus [(2.1)](die-leitungsgleichungen.html#gl-2-1), indem man die erste Gleichung nach $s$ und die zweite nach $t$ ableitet und $i$ eliminiert.

::::beispiel Koaxialkabel
$Z=50\,\Omega$ und $C'=100$ pF/m ergeben $L'=Z^2C'=250$ nH/m und $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s, zwei Drittel der Lichtgeschwindigkeit (wegen des Dielektrikums im Kabel). Ein Signal braucht für 10 m Kabel 50 ns. Wird das Kabel mit 75 $\Omega$ statt 50 $\Omega$ abgeschlossen, ist $r=\frac{75-50}{75+50}=0{,}2$: 20 % der Spannungsamplitude laufen als Echo zurück.
::::

:::ltspice Reflexionen auf einer Leitung
⁠**Zeichnen:** Quelle `voltage` mit `PULSE(0 2 0 1n 1n 10n 1)` und einem Innenwiderstand `res` mit `50` zum Netz `in`. Von `in` eine verlustlose Leitung `tline` mit `Td=50n Z0=50` (das 10-m-Koaxialkabel aus dem Beispiel) zum Netz `end`, dort `res` mit `{RE}` nach Masse. Weil der Innenwiderstand gleich $Z$ ist, läuft eine Welle von 1 V los, und das Echo wird an der Quelle vollständig aufgenommen.

⁠**Direktiven:** `.param RE=75`, `.step param RE list 1m 50 75 1G` (fast Kurzschluss, Anpassung, 75 $\Omega$, fast Leerlauf), `.tran 0 200n 0 0.1n`.

⁠**Was du siehst:** An `in` zuerst der Impuls mit 1 V. Nach $2\cdot50\,\mathrm{ns}=100$ ns kommt das Echo mit der Höhe $r\cdot1$ V zurück: $-1$; $0$; $0{,}2$ und $+1$, genau $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$. An `end` steht nach 50 ns die Summe aus hin- und rücklaufender Welle, $(1+r)\cdot1$ V. Stelle `Td` und `Z0` auf deine Werte aus Aufgabe [4](#aufg-4)(a), setze `RE` auf 100 und vergleiche die Echohöhe mit deinem Ergebnis aus Aufgabe [4](#aufg-4)(b).
:::

:::aufgabe Aufgabe 3 ★★ d'Alembert prüfen
<span class="anker" id="aufg-3"></span>

Zeige durch Einsetzen, dass $u(s,t)=u_\mathrm{hin}(s-vt)$ die Wellengleichung [(4.1)](#gl-4-1) mit $v=1/\sqrt{L'C'}$ löst. Wie hängt der zugehörige Strom mit der Spannung zusammen? Tipp: Erste Leitungsgleichung mit $R'=0$.

:::loesung
Mit $x=s-vt$: $\frac{\partial^2u}{\partial s^2}=u_\mathrm{hin}''(x)$ und $\frac{\partial^2u}{\partial t^2}=v^2u_\mathrm{hin}''(x)$. Die Wellengleichung verlangt $u''=L'C'v^2u''$, also $v^2=\frac{1}{L'C'}$. Strom: Mit $R'=0$ ist $\frac{\partial u}{\partial s}=-L'\frac{\partial i}{\partial t}$, also $u_\mathrm{hin}'(x)=-L'\frac{\partial i}{\partial t}$. Der Ansatz $i=u_\mathrm{hin}(x)/Z$ ergibt $\frac{\partial i}{\partial t}=-\frac vZu'_\mathrm{hin}$, und das passt mit $L'v/Z=L'\cdot\frac{1}{\sqrt{L'C'}}\cdot\sqrt{\frac{C'}{L'}}=1$. In der hinlaufenden Welle sind Spannung und Strom überall im Verhältnis $Z$.
:::
:::

:::aufgabe Aufgabe 4 ★★ Kabel und Abschluss
<span class="anker" id="aufg-4"></span>

Ein verlustloses Kabel hat $L'=300$ nH/m und $C'=120$ pF/m.

<ol class="al">

<li>

Berechne $Z$, $v$ und die Laufzeit für 5 m.

</li>

<li>

Mit welchem Widerstand muss es abgeschlossen werden, damit nichts reflektiert wird? Welcher Reflexionsfaktor ergibt sich bei 100 $\Omega$?

</li>

<li>

Bis zu welcher Frequenz kann man die 5 m noch als „kurz“ behandeln, wenn die Leitung höchstens ein Zehntel der Wellenlänge lang sein soll?

</li>

</ol>

:::loesung
(a) $Z=\sqrt{300/120}\cdot\sqrt{\frac{\text{nH}}{\text{pF}}}=\sqrt{2{,}5\cdot10^3}\,\Omega=50\,\Omega$. $v=\frac{1}{\sqrt{300\cdot10^{-9}\cdot120\cdot10^{-12}}}\,\mathrm{m/s}=\frac{1}{\sqrt{3{,}6\cdot10^{-17}}}\,\mathrm{m/s}=1{,}67\cdot10^8$ m/s. Laufzeit für 5 m: 30 ns.

(b) Mit $Z=50\,\Omega$. Bei 100 $\Omega$: $r=\frac{100-50}{150}=\frac13$.

(c) $\lambda=v/f\ge50$ m, also $f\le\frac{1{,}67\cdot10^8}{50}\,\mathrm{Hz}=3{,}3$ MHz.
:::
:::

::::formelsammlung
**Verlustlose Leitung**

$$\gamma=\mathrm{j}2\pi f\sqrt{L'C'},\qquad Z=\sqrt{\frac{L'}{C'}},\qquad v=\frac{1}{\sqrt{L'C'}}$$

Für $R'=G'=0$: keine Dämpfung ($\alpha=0$), $\beta$ proportional zu $f$. Wellenwiderstand und Geschwindigkeit hängen nicht von der Frequenz ab.

**Wellengleichung der verlustlosen Leitung**

$$\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}$$

Aus den Leitungsgleichungen mit $R'=G'=0$: die erste nach $s$, die zweite nach $t$ ableiten und $i$ eliminieren.

**d'Alembert-Lösung**

$$u(s,t)=u_\mathrm{hin}(s-vt)+u_\mathrm{rück}(s+vt)$$

Jede Lösung der Wellengleichung, mit beliebigen (zweimal differenzierbaren) Funktionen $u_\mathrm{hin}$ und $u_\mathrm{rück}$. Jede Signalform läuft unverändert mit $v$; die Leitung ist ein verzerrungsfreies System mit der Verzögerung $l/v$.

**Strom der hinlaufenden Welle**

$$i=u_\mathrm{hin}(x)/Z$$

Mit $x=s-vt$: In der hinlaufenden Welle stehen Spannung und Strom überall im Verhältnis $Z$.
::::

::::lernkarten
:::karte formel Verlustlose Leitung
Welche Ausbreitungskonstante, welchen Wellenwiderstand und welche Geschwindigkeit hat eine verlustlose Leitung mit $R'=G'=0$?
---
$\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$, also $\alpha=0$ und $\beta$ proportional zu $f$. Daraus folgen $Z=\sqrt{\frac{L'}{C'}}$ und $v=\frac{1}{\sqrt{L'C'}}$, beide unabhängig von der Frequenz.
--- falsch
$\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$, also $\alpha=0$. Daraus folgen $Z=\sqrt{L'C'}$ und $v=\frac{1}{\sqrt{L'C'}}$; der Wellenwiderstand wächst mit Induktivität und Kapazität gleichermaßen.
--- falsch
$\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$, also $\alpha=0$. Daraus folgen $Z=\sqrt{\frac{L'}{C'}}$ und $v=2\pi f\sqrt{L'C'}$; hohe Frequenzen laufen auf der Leitung schneller als tiefe.
--- falsch
$\gamma=\sqrt{L'C'}$, also $\beta=0$ und keine Phasendrehung. Daraus folgen $Z=\sqrt{\frac{L'}{C'}}$ und $v=\sqrt{L'C'}$, beide unabhängig von der Frequenz.
:::
:::karte herleitung Wellengleichung der verlustlosen Leitung
Wie folgt aus den Leitungsgleichungen mit $R'=G'=0$ die Wellengleichung $\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}$?
---
Mit $R'=G'=0$ lauten die Leitungsgleichungen $\frac{\partial u}{\partial s}=-L'\frac{\partial i}{\partial t}$ und $\frac{\partial i}{\partial s}=-C'\frac{\partial u}{\partial t}$, weil die Verlustglieder wegfallen.
---
Man leitet die erste Gleichung nach $s$ ab, weil links dann die zweite Ortsableitung $\frac{\partial^2u}{\partial s^2}$ steht; rechts steht $-L'$ mal die gemischte Ableitung von $i$ nach $s$ und $t$.
---
Man leitet die zweite Gleichung nach $t$ ab, weil dann dieselbe gemischte Ableitung von $i$ auftritt; sie ist gleich $-C'\frac{\partial^2u}{\partial t^2}$.
---
Einsetzen eliminiert $i$ und ergibt $\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}$, weil die Reihenfolge der Ableitungen nach $s$ und $t$ keine Rolle spielt.
:::
:::karte formel d'Alembert-Lösung
Welche Form hat jede Lösung der Wellengleichung $\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}$ der verlustlosen Leitung?
---
$u(s,t)=u_\mathrm{hin}(s-vt)+u_\mathrm{rück}(s+vt)$ mit beliebigen, zweimal differenzierbaren Funktionen und $v=1/\sqrt{L'C'}$: eine hin- und eine rücklaufende Welle beliebiger Form.
--- falsch
$u(s,t)=u_\mathrm{hin}(s-vt)+u_\mathrm{rück}(s+vt)$, aber nur mit sinusförmigen Funktionen einer festen Frequenz; Signale anderer Form laufen auf der Leitung auseinander.
--- falsch
$u(s,t)=u_\mathrm{hin}(s)\cdot u_\mathrm{rück}(t)$ mit beliebigen Funktionen: ein fester räumlicher Verlauf, dessen Höhe sich an allen Orten gleichzeitig mit der Zeit ändert.
--- falsch
$u(s,t)=u_\mathrm{hin}(s-vt)-u_\mathrm{rück}(s-vt)$: zwei Wellen beliebiger Form, die beide in Richtung wachsender $s$ laufen und sich dabei teilweise gegenseitig auslöschen.
:::
:::karte herleitung d'Alembert prüfen
Wie zeigt man durch Einsetzen, dass $u(s,t)=u_\mathrm{hin}(s-vt)$ die Wellengleichung der verlustlosen Leitung löst, und welche Geschwindigkeit $v$ folgt daraus?
---
Mit $x=s-vt$ ist $\frac{\partial^2u}{\partial s^2}=u_\mathrm{hin}''(x)$, weil $x$ mit dem Faktor 1 von $s$ abhängt.
---
Ebenso ist $\frac{\partial^2u}{\partial t^2}=v^2u_\mathrm{hin}''(x)$, weil jede Ableitung nach $t$ nach der Kettenregel den Faktor $-v$ bringt.
---
Die Wellengleichung verlangt $u''=L'C'v^2u''$, also $v^2=\frac{1}{L'C'}$, weil die Gleichung für jede Signalform $u_\mathrm{hin}$ gelten soll.
:::
:::karte zusammenhang Strom in der hinlaufenden Welle
Wie hängt in einer hinlaufenden Welle auf der verlustlosen Leitung der Strom mit der Spannung zusammen, und warum?
---
Es gilt $i=u_\mathrm{hin}(x)/Z$: Spannung und Strom stehen überall im Verhältnis $Z$. Das folgt aus der ersten Leitungsgleichung mit $R'=0$, weil $L'v/Z=1$ ist.
--- falsch
Der Strom ist überall null, weil auf einer verlustlosen Leitung keine Leistung umgesetzt wird. Die Welle besteht deshalb nur aus einer wandernden Spannung.
--- falsch
Es gilt $i=Z\,u_\mathrm{hin}(x)$: Der Strom ist das $Z$-fache der Spannung, weil der Wellenwiderstand angibt, wie viel Strom je Volt in der Welle fließt.
--- falsch
Es gilt $i=u_\mathrm{hin}(x)/Z$ nur am Ende der Leitung; an anderen Orten hängt das Verhältnis davon ab, wie lange die Welle bis dorthin gebraucht hat.
:::
:::karte zusammenhang Leitung als verzerrungsfreies System
Warum läuft auf einer verlustlosen Leitung eine beliebige Signalform unverändert die Leitung entlang?
---
Weil alle Frequenzanteile gleich schnell sind und gleich wenig gedämpft werden: $\alpha=0$ und $\beta$ proportional zu $f$. Die Leitung ist damit ein verzerrungsfreies System mit der Verzögerung $l/v$.
--- falsch
Weil alle Frequenzanteile gleich wenig gedämpft werden. Dass hohe Frequenzen schneller laufen als tiefe, ändert die Form nicht, weil die Amplituden aller Anteile erhalten bleiben.
--- falsch
Weil die Leitung jede Frequenz um denselben Phasenwinkel dreht. Ein fester Winkel für alle Frequenzen verschiebt jedes Signal als Ganzes, ohne es zu verformen.
--- falsch
Weil der Wellenwiderstand $Z=\sqrt{L'/C'}$ reell ist. Ein reeller Widerstand dreht keine Phase, deshalb kommen alle Frequenzen ohne jede Verzögerung am Ende an.
:::
:::karte formel Koaxialkabel
Wie berechnet man aus dem Wellenwiderstand $Z$ und dem Belag $C'$ eines verlustlosen Kabels den Belag $L'$ und die Geschwindigkeit $v$?
---
$L'=Z^2C'$ und $v=\frac{1}{\sqrt{L'C'}}$, weil $Z=\sqrt{L'/C'}$ gilt. Für $Z=50\,\Omega$ und $C'=100$ pF/m ergeben sich $L'=250$ nH/m und $v=2\cdot10^8$ m/s, zwei Drittel der Lichtgeschwindigkeit.
--- falsch
$L'=Z\,C'$ und $v=\frac{1}{\sqrt{L'C'}}$, weil $Z=L'/C'$ gilt. Für $Z=50\,\Omega$ und $C'=100$ pF/m ergibt sich $L'=5$ nH/m, und das Signal läuft dann schneller als Licht im freien Raum.
--- falsch
$L'=Z^2C'$ und $v=\sqrt{L'C'}$, weil $Z=\sqrt{L'/C'}$ gilt. Für $Z=50\,\Omega$ und $C'=100$ pF/m ergibt sich $L'=250$ nH/m; die Geschwindigkeit ist umso größer, je größer beide Beläge sind.
--- falsch
$L'=Z^2C'$ und $v=\frac{1}{\sqrt{L'C'}}$, weil $Z=\sqrt{L'/C'}$ gilt. Die Geschwindigkeit ist aber bei jedem Kabel gleich der Lichtgeschwindigkeit, weil sich die beiden Beläge immer gegenseitig ausgleichen.
:::
:::karte zusammenhang Echo bei falschem Abschluss
Was passiert, wenn man ein verlustloses Kabel mit $Z=50\,\Omega$ am Ende mit 75 $\Omega$ statt mit 50 $\Omega$ abschließt?
---
Am Ende entsteht eine rücklaufende Welle mit $r=\frac{75-50}{75+50}=0{,}2$: 20 % der Spannungsamplitude laufen als Echo zurück, das nach der doppelten Laufzeit wieder am Anfang ankommt.
--- falsch
Am Ende entsteht eine rücklaufende Welle mit $r=\frac{50}{75}=0{,}67$: Zwei Drittel der Spannungsamplitude laufen als Echo zurück, weil der Abschluss um die Hälfte zu groß ist.
--- falsch
Es entsteht keine rücklaufende Welle, weil 75 $\Omega$ größer als der Wellenwiderstand ist. Nur ein zu kleiner Abschluss reflektiert, ein zu großer nimmt die ankommende Welle vollständig auf.
--- falsch
Am Ende entsteht eine rücklaufende Welle mit $r=-0{,}2$: 20 % der Spannungsamplitude laufen mit umgekehrtem Vorzeichen zurück, weil der Abschluss größer als $Z$ ist.
:::
:::karte zusammenhang Spannung am Ende der Leitung
Welche Spannung stellt sich am Ende einer Leitung ein, wenn dort eine Welle der Höhe 1 V ankommt und mit dem Reflexionsfaktor $r$ reflektiert wird, und warum?
---
$(1+r)\cdot1$ V, weil am Ende hin- und rücklaufende Welle gleichzeitig vorhanden sind und sich addieren. Bei Leerlauf ($r=+1$) verdoppelt sich die Spannung, bei Kurzschluss ($r=-1$) ist sie null.
--- falsch
$r\cdot1$ V, weil am Ende nur die reflektierte Welle gemessen wird. Die hinlaufende Welle ist dort schon vollständig im Abschluss verschwunden, wenn die reflektierte entsteht.
--- falsch
$(1-r)\cdot1$ V, weil die reflektierte Welle der ankommenden entgegenläuft und deshalb von ihr abgezogen wird. Bei Leerlauf ($r=+1$) ist die Spannung am Ende deshalb null.
--- falsch
Immer 1 V, weil die Spannung am Ende nur von der Quelle abhängt. Der Reflexionsfaktor bestimmt allein, wie groß das Echo ist, das später am Anfang der Leitung ankommt.
:::
:::karte formel Wann eine Leitung kurz ist
Wie bestimmt man die höchste Frequenz, bei der eine Leitung der Länge $l$ noch als kurz gilt, wenn sie höchstens ein Zehntel der Wellenlänge lang sein soll?
---
Man verlangt $\lambda=v/f\ge10\,l$, also $f\le v/(10\,l)$: Je länger die Leitung, desto tiefer liegt die Grenze. Für 5 m Kabel mit $v=1{,}67\cdot10^8$ m/s ergibt das $f\le3{,}3$ MHz.
--- falsch
Aus $\lambda=v\,f\ge10\,l$ folgt $f\ge10\,l/v$: Die Leitung gilt erst oberhalb einer Mindestfrequenz als kurz, weil die Wellenlänge mit der Frequenz wächst.
--- falsch
Aus $\lambda=v/f\ge l/10$ folgt $f\le10\,v/l$: Die Leitung darf zehnmal so lang sein wie die Wellenlänge. Für 5 m Kabel mit $v=1{,}67\cdot10^8$ m/s ergibt das $f\le334$ MHz.
--- falsch
Die Frequenz spielt keine Rolle; ob eine Leitung kurz ist, hängt nur von ihrer Länge ab. Unter 10 m gilt jede Leitung als kurz, gleich welches Signal sie führt.
:::
::::
