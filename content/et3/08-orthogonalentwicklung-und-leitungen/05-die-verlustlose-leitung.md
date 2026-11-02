---
title: Stufe 4: Die verlustlose Leitung
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Orthogonalentwicklung und Leitungen
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

⁠**So liest man das:** Eine beliebige Signalform läuft unverändert mit der Geschwindigkeit $v$ die Leitung entlang. Das liegt daran, dass alle Frequenzanteile gleich schnell sind und gleich wenig gedämpft werden: Die Leitung ist ein verzerrungsfreies System im Sinne von [Teil 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html), mit der Verzögerung $l/v$. Die Wellengleichung für $u$ folgt aus [(2.1)](die-leitungsgleichungen.html#gl-2-1), indem man die erste Gleichung nach $s$ und die zweite nach $t$ ableitet und $i$ eliminiert.

**Beispiel: Koaxialkabel.** $Z=50\,\Omega$ und $C'=100$ pF/m ergeben $L'=Z^2C'=250$ nH/m und $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s, zwei Drittel der Lichtgeschwindigkeit (wegen des Dielektrikums im Kabel). Ein Signal braucht für 10 m Kabel 50 ns. Wird das Kabel mit 75 $\Omega$ statt 50 $\Omega$ abgeschlossen, ist $r=\frac{75-50}{75+50}=0{,}2$: 20 % der Spannungsamplitude laufen als Echo zurück.

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
