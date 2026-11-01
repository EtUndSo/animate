---
title: Orthogonalentwicklung und Leitungen
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Orthogonalentwicklung und Leitungen
order: 3280100
summary: Zwei Zusatzthemen: Signale als Vektoren, Wellen auf elektrischen Leitungen
tags: orthogonal, orthonormal, verallgemeinerte Parseval-Theorem, Leitungsbelägen, Wellengleichung, Ausbreitungskonstanten, Wellenwiderstand, Dämpfungskonstanten
lang: de
---

## Worum es geht

Dieser Artikel ergänzt die [Teile 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) bis 7 um zwei Themen. Das erste verallgemeinert die Fourier-Reihe: Man zerlegt ein Signal nach beliebigen orthogonalen Funktionen, so wie man einen Vektor in seine Komponenten zerlegt. Das zweite zeigt, was auf einer langen Leitung passiert: Spannung und Strom laufen als Wellen, die am Ende reflektiert werden können. Der optimale Quantisierer, der als drittes Zusatzthema in Frage käme, steht schon in [Teil 7](/wissen/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html) (Stufe 5).

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Bei orthonormalen Basisfunktionen ist der beste Koeffizient einer Funktion ihre Korrelation mit der Basisfunktion, und die Energie ist die Summe der Koeffizientenquadrate.

</li>

<li>

Auf einer Leitung ist jede Spannung eine Überlagerung einer hinlaufenden und einer rücklaufenden Welle. Die Leitung ist durch die Ausbreitungskonstante $\gamma$ und den Wellenwiderstand $Z$ beschrieben.

</li>

<li>

Wird die Leitung mit ihrem Wellenwiderstand abgeschlossen, verschwindet die rücklaufende Welle. Bei einer verlustlosen Leitung laufen alle Frequenzen gleich schnell, Signale kommen unverzerrt an.

</li>

</ol>
:::

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Die Rechenmodelle für diesen Artikel
<ul>

<li>

⁠**Orthogonalentwicklung** von $f(t)=t^2$ auf $[0,1]$ nach den orthonormalen Polynomen $s_0=1$, $s_1=\sqrt3(2t-1)$, $s_2=\sqrt5(6t^2-6t+1)$.

</li>

<li>

⁠**Koaxialkabel** mit $Z=50\,\Omega$ und $C'=100$ pF/m, verlustlos.

</li>

</ul>
:::

## Stufe 1: Signale als Vektoren, die Orthogonalentwicklung

<span class="anker" id="stufe-1"></span>

:::zweck
Die Fourier-Reihe zerlegt ein Signal nach Schwingungen. Dasselbe geht mit jedem System orthogonaler Funktionen. Diese Stufe zeigt, wie man die Koeffizienten findet und warum sie die beste Näherung liefern.
:::

**Die Idee.** Ein Vektor im Raum hat die Komponenten $b_i=\vec f\cdot\vec e_i$ bezüglich senkrechter Einheitsvektoren $\vec e_i$. Für Signale auf einem Intervall $[0,T]$ spielt das Integral $\int_0^Tf(t)g(t)\mathrm{d} t$ die Rolle des Skalarprodukts. Zwei Signale heißen __orthogonal__, wenn es null ist ([Teil 6](/wissen/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). Ein System von $M$ Funktionen $s_i(t)$ heißt __orthonormal__, wenn

<span class="anker" id="gl-1-1"></span>
$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}. \tag{1.1}$$

Man nähert ein Energiesignal $f(t)$ durch $\sum_{i=0}^{M-1}b_is_i(t)$, und es bleibt ein Rest $r(t)=f(t)-\sum b_is_i(t)$.

:::satz Satz 1.1 (Orthogonalentwicklung)
<span class="anker" id="satz-1-1"></span>

Die Energie des Rests $E_r=\int_0^Tr^2\mathrm{d} t$ ist am kleinsten für

<span class="anker" id="gl-1-2"></span>
$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t. \tag{1.2}$$

Dann gilt $E_r=E_f-\sum_ib_i^2$. Wird $E_r\to0$ mit wachsendem $M$ (vollständiges System), gilt das __verallgemeinerte Parseval-Theorem__ $E_f=\sum_ib_i^2$.
:::

:::herleitung Koeffizienten und Restenergie
$E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$. Ableiten nach $b_j$ und null setzen:

$$\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0\quad\Longrightarrow\quad\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t=b_j.$$

Die Orthonormalität lässt aus der Summe nur $i=j$ übrig. Setzt man diese $b_i$ ein und multipliziert aus, heben sich die gemischten Glieder wieder wegen der Orthonormalität weg: $E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$.
:::

⁠**So liest man das:** Jeder Koeffizient wird für sich bestimmt, unabhängig von den anderen. Nimmt man eine Basisfunktion hinzu, ändern sich die bisherigen Koeffizienten nicht. Das ist der Vorteil orthogonaler Systeme, genau wie bei der Fourier-Reihe ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). $b_i$ ist die Kreuzkorrelation $\varphi^E_{fs_i}(0)$. Deshalb kann man die Koeffizienten mit einer Bank von Korrelationsfiltern $h_i(t)=s_i(T-t)$ messen, deren Ausgänge man bei $t=T$ abtastet ([Teil 7](/wissen/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)).

**Beispiel.** $f(t)=t^2$ auf $[0,1]$, $E_f=\frac15$. Mit $s_0=1$ und $s_1=\sqrt3(2t-1)$:

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0{,}289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

Die Näherung ist $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$, die beste Gerade im Sinne der Energie. Die Restenergie ist $\frac15-\frac7{36}=\frac{1}{180}=0{,}0056$, also 2,8 % von $E_f$. Mit $s_2=\sqrt5(6t^2-6t+1)$ kommt $b_2=\frac{\sqrt5}{30}=0{,}075$ dazu, und der Rest wird null, weil $t^2$ selbst ein Polynom zweiten Grades ist.

:::aufgabe Aufgabe 1 ★ Orthonormal prüfen
<span class="anker" id="aufg-1"></span>

Zeige, dass $s_0=1$ und $s_1=\sqrt3(2t-1)$ auf $[0,1]$ orthonormal sind. Warum braucht $s_1$ den Faktor $\sqrt3$?

:::loesung
$\int_0^11\cdot\sqrt3(2t-1)\mathrm{d} t=\sqrt3\,[t^2-t]_0^1=0$: orthogonal. $\int_0^11^2\mathrm{d} t=1$. $\int_0^13(2t-1)^2\mathrm{d} t=3\cdot\bigl[\frac{(2t-1)^3}{6}\bigr]_0^1=3\cdot\frac{1+1}{6}=1$. Ohne den Faktor wäre die Energie von $2t-1$ nur $\frac13$. Der Faktor $\sqrt3$ normiert sie auf 1, sonst wäre $b_1=\int fs_1\mathrm{d} t$ nicht der richtige Koeffizient.
:::
:::

:::aufgabe Aufgabe 2 ★★ Beste Näherung
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Rechne $b_1$ für $f(t)=t^2$ nach und bestätige die Näherung $t-\frac16$.

</li>

<li>

Prüfe $E_r=\frac{1}{180}$, indem du $\int_0^1\bigl(t^2-t+\frac16\bigr)^2\mathrm{d} t$ direkt berechnest.

</li>

<li>

Bestimme die Koeffizienten von $f(t)=\sqrt2\cos(2\pi t)$ bezüglich $s_0$ und $s_1$. Was bedeutet das Ergebnis?

</li>

</ol>

:::loesung
(a) $\int_0^1t^2(2t-1)\mathrm{d} t=\frac24-\frac13=\frac16$, also $b_1=\frac{\sqrt3}{6}$. Näherung: $\frac13+\frac{\sqrt3}{6}\cdot\sqrt3(2t-1)=\frac13+t-\frac12=t-\frac16$.

(b) $\int_0^1\bigl(t^2-t+\tfrac16\bigr)^2\mathrm{d} t=\int_0^1\bigl(t^4-2t^3+\tfrac43t^2-\tfrac13t+\tfrac1{36}\bigr)\mathrm{d} t=\tfrac15-\tfrac12+\tfrac49-\tfrac16+\tfrac1{36}=\tfrac{1}{180}$.

(c) $b_0=\sqrt2\int_0^1\cos(2\pi t)\mathrm{d} t=0$ und $b_1=\sqrt6\int_0^1(2t-1)\cos(2\pi t)\mathrm{d} t=0$ (der Kosinus ist symmetrisch um $t=\frac12$, $2t-1$ antisymmetrisch). Beide Koeffizienten sind null: Die Funktion ist zu beiden Basisfunktionen orthogonal, die Näherung ist null, und der ganze Signalinhalt bleibt im Rest. Eine Basis taugt nur für Signale, die ihren Funktionen ähneln.
:::
:::

## Stufe 2: Die Leitungsgleichungen

<span class="anker" id="stufe-2"></span>

:::zweck
Bisher waren Leitungen ideale Verbindungen. Ist eine Leitung lang gegenüber der Wellenlänge, braucht ein Signal merklich Zeit, um sie zu durchlaufen. Diese Stufe stellt die Gleichungen auf, die das beschreiben.
:::

**Die Idee.** Man zerlegt die Leitung in kurze Stücke der Länge $\mathrm{d} s$. Jedes Stück hat einen Längswiderstand und eine Längsinduktivität (die Hin- und Rückleiter), dazu eine Querkapazität und einen Querleitwert (zwischen den Leitern). Bei einer gleichförmigen Leitung sind diese Größen proportional zur Länge: $R'\mathrm{d} s$, $L'\mathrm{d} s$, $C'\mathrm{d} s$, $G'\mathrm{d} s$ mit den __Leitungsbelägen__ $R'$, $L'$, $C'$, $G'$ (Werte je Meter, Abb. [1](#abb-1)).

:::abbildung et3/k8element
Ersatzschaltbild eines kurzen Leitungsstücks der Länge $\mathrm{d} s$ mit den Leitungsbelägen $R'$, $L'$, $G'$, $C'$.
:::

:::satz Satz 2.1 (Leitungsgleichungen)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung Leitungsgleichungen
Maschenregel über das Stück: $u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$, also $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$. Knotenregel: Vom Strom $i$ fließt ein Teil durch $G'\mathrm{d} s$ und $C'\mathrm{d} s$ ab, $i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$. Durch $\mathrm{d} s$ teilen. (In der Knotenregel steht strenggenommen die Spannung am Ende des Stücks, der Unterschied ist von zweiter Ordnung in $\mathrm{d} s$.)
:::

⁠**So liest man das:** Die Spannung fällt entlang der Leitung, weil Strom durch die Längselemente fließt. Der Strom nimmt ab, weil er über die Querelemente zwischen den Leitern abfließt. Die beiden Gleichungen koppeln $u$ und $i$ in Ort und Zeit.

## Stufe 3: Wellen bei sinusförmiger Anregung

<span class="anker" id="stufe-3"></span>

:::zweck
Mit Zeigern wird aus den partiellen Differentialgleichungen eine gewöhnliche Gleichung im Ort. Ihre Lösung sind zwei gegenläufige Wellen.
:::

Mit $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$ und ebenso für $i$ wird $\frac{\partial}{\partial t}$ zu $\mathrm{j}2\pi f$:

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U.$$

Ableiten der ersten Gleichung und Einsetzen der zweiten ergibt die __Wellengleichung__ $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$.

:::satz Satz 3.1 (Hin- und rücklaufende Welle)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr), \tag{3.1}$$

mit der __Ausbreitungskonstanten__ und dem __Wellenwiderstand__

<span class="anker" id="gl-3-2"></span>
$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}. \tag{3.2}$$
:::

⁠**So liest man das:** Mit $\gamma=\alpha+\mathrm{j}\beta$ wird der erste Summand im Zeitbereich zu $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$: eine Welle, die in Richtung wachsender $s$ läuft und dabei mit der __Dämpfungskonstanten__ $\alpha$ abklingt. Ein Nulldurchgang bewegt sich mit $v=2\pi f/\beta$, die Wellenlänge ist $\lambda=2\pi/\beta$. Der zweite Summand läuft in die Gegenrichtung. $Z$ ist das Verhältnis von Spannung zu Strom in einer einzelnen Welle. Die Randbedingungen legen die Konstanten $\underline U_1$, $\underline U_2$ fest, etwa Spannung und Strom am Anfang: $\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$.

**Reflexion am Ende.** Ist die Leitung am Ende ($s=l$) mit einem Widerstand $R_\mathrm E=\underline U_e/\underline I_e$ abgeschlossen, lässt sich die Spannung schreiben als

<span class="anker" id="gl-3-3"></span>
$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}. \tag{3.3}$$

Der erste Summand ist die hinlaufende, der zweite die vom Ende zurücklaufende Welle. Bei $R_\mathrm E=Z$ verschwindet die rücklaufende Welle: Ein Abschluss mit dem Wellenwiderstand nimmt die ankommende Welle vollständig auf, als ginge die Leitung unendlich weiter. Das Verhältnis der beiden Wellen am Ende ist der __Reflexionsfaktor__ $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$ (Zusatz: Kurzschluss $r=-1$, Leerlauf $r=+1$).

:::frage Warum stört ein falscher Abschluss bei kurzen Leitungen nicht?
Weil die reflektierte Welle dann fast sofort zurück ist. Ist die Laufzeit über die Leitung klein gegen die Dauer der Signaländerungen (Leitung kurz gegen die Wellenlänge), überlagern sich hin- und rücklaufende Welle praktisch gleichzeitig, und man merkt nur den Abschlusswiderstand. Erst wenn die Laufzeit vergleichbar wird, etwa bei schnellen Digitalsignalen oder Hochfrequenz, erscheinen Reflexionen als Echos und verzerren das Signal.
:::

## Stufe 4: Die verlustlose Leitung

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

⁠**So liest man das:** Eine beliebige Signalform läuft unverändert mit der Geschwindigkeit $v$ die Leitung entlang. Das liegt daran, dass alle Frequenzanteile gleich schnell sind und gleich wenig gedämpft werden: Die Leitung ist ein verzerrungsfreies System im Sinne von [Teil 5](/wissen/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html), mit der Verzögerung $l/v$. Die Wellengleichung für $u$ folgt aus [(2.1)](#gl-2-1), indem man die erste Gleichung nach $s$ und die zweite nach $t$ ableitet und $i$ eliminiert.

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

:::kern Das Wichtigste
<ul>

<li>

Orthonormal: $\int s_is_j\mathrm{d} t=\delta_{ij}$; beste Koeffizienten $b_i=\int fs_i\mathrm{d} t$; $E_r=E_f-\sum b_i^2$; vollständig: $E_f=\sum b_i^2$.

</li>

<li>

Leitungsgleichungen: $\partial_su=-(R'+L'\partial_t)i$, $\partial_si=-(G'+C'\partial_t)u$.

</li>

<li>

Zeiger (mit $\omega=2\pi f$): $\underline U=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$; $\gamma=\sqrt{(R'+\mathrm{j}\omega L')(G'+\mathrm{j}\omega C')}=\alpha+\mathrm{j}\beta$; $Z=\sqrt{\frac{R'+\mathrm{j}\omega L'}{G'+\mathrm{j}\omega C'}}$.

</li>

<li>

Abschluss mit $Z$: keine Reflexion; $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$.

</li>

<li>

Verlustlos: $Z=\sqrt{L'/C'}$, $v=1/\sqrt{L'C'}$, $u=u_\mathrm{hin}(s-vt)+u_\mathrm{rück}(s+vt)$.

</li>

</ul>
:::
