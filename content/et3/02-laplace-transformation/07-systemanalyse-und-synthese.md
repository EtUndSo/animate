---
title: Systemanalyse und -synthese
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Laplace-Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Kapitel 2: Laplace-Transformation
order: 3220700
summary: Ein System aus mehreren Teilsystemen lässt sich im Bildbereich mit einfacher Algebra analysieren.
tags: Rückkopplung, Vorwärtszweig, Summierstelle, Rückführung, Integrierer, Differenzierer, Proportionalglied, direkte Form
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Ein System aus mehreren Teilsystemen lässt sich im Bildbereich mit einfacher Algebra analysieren. Umgekehrt lässt sich jedes System mit rationaler Übertragungsfunktion aus wenigen Grundbausteinen aufbauen.
:::

### Rückkopplung

<span class="anker" id="stufe-6-1"></span>

Bei einer __Rückkopplung__ wird ein Teil des Ausgangs zum Eingang zurückgeführt (Abb. [9](#abb-9)). Das System $H_1(p)$ im __Vorwärtszweig__ erhält die Differenz aus dem Eingang und dem zurückgeführten Signal. Diese Differenz bildet eine __Summierstelle__, an der die Vorzeichen der Eingänge stehen. Das System $H_2(p)$ in der __Rückführung__ formt den Ausgang, bevor er abgezogen wird.

:::abbildung et3/k2rueck 9
Rückgekoppelte Verbindung zweier LTI-Systeme. Die Summierstelle bildet $S(p)-H_2(p)\,G(p)$.
:::

Im Bildbereich liest man die Gleichung direkt aus dem Bild ab:

<span class="anker" id="gl-6-1"></span>
$$G(p)=H_1(p)\cdot\bigl[S(p)-H_2(p)\cdot G(p)\bigr]. \tag{6.1}$$

Man bringt alle $G$ auf eine Seite, $G\,(1+H_1H_2)=H_1\,S$, und erhält die Übertragungsfunktion des ganzen Systems:

<span class="anker" id="gl-6-2"></span>
$$H(p)=\frac{G(p)}{S(p)}=\frac{H_1(p)}{1+H_1(p)\cdot H_2(p)}=\frac{1}{1/H_1(p)+H_2(p)} . \tag{6.2}$$

Im Zeitbereich müsste man dafür eine Gleichung lösen, in der $g$ in einer Faltung mit sich selbst vorkommt. Im Bildbereich genügt es, eine lineare Gleichung umzustellen.

⁠**Kurz gesagt:** Eine Rückkopplung mit $H_1$ vorwärts und $H_2$ zurück hat die Übertragungsfunktion $\frac{H_1}{1+H_1H_2}$.

:::hintergrund Wozu man rückkoppelt: der Trick der Gegenkopplung
Ist der Vorwärtszweig sehr stark, $|H_1H_2|\gg1$, dann ist die $1$ im Nenner von [(6.2)](#gl-6-2) vernachlässigbar:

$$H(p)=\frac{H_1}{1+H_1H_2}\approx\frac{H_1}{H_1H_2}=\frac{1}{H_2(p)} .$$

Das Verhalten des ganzen Systems hängt dann fast nur noch von der Rückführung ab und kaum noch vom Vorwärtszweig. Darin liegt der Nutzen. Transistorverstärker haben eine große, aber ungenaue Verstärkung, die mit Temperatur und Exemplar schwankt. Widerstände dagegen lassen sich genau herstellen. Ein Verstärker mit sehr großem $H_1$ und einem Spannungsteiler aus zwei Widerständen als $H_2$ ergibt ein System, das so genau ist wie die Widerstände. So arbeitet jede Operationsverstärkerschaltung mit Gegenkopplung. Erfunden hat das Prinzip Harold S. Black 1927 für Verstärker in Telefonleitungen.

Wie stark Schwankungen gedämpft werden, zeigt die Ableitung von [(6.2)](#gl-6-2) nach $H_1$:

$$\frac{\mathrm{d} H/H}{\mathrm{d} H_1/H_1}=\frac{1}{1+H_1H_2} .$$

Eine relative Änderung von $H_1$ kommt im Ganzen um den Faktor $1+H_1H_2$ verkleinert an. Mit $H_1=10^5$ und $H_2=0{,}01$ ist $H_1H_2=1000$: Ändert sich die Verstärkung $H_1$ um 10 %, ändert sich $H$ nur um etwa 0,01 %. Der Preis: Die Rückkopplung verschiebt auch die Pole, und bei ungünstiger Phase kann sie das System nach dem vorigen Abschnitt instabil machen.
:::

### Grundbausteine

<span class="anker" id="stufe-6-2"></span>

Vier einfache LTI-Systeme genügen, um jede rationale Übertragungsfunktion aufzubauen:

<ul>

<li>

der __Integrierer__ mit der Impulsantwort $\varepsilon(t)$ und $H(p)=1/p$, gezeichnet als Kasten „$1/p$“;

</li>

<li>

der __Differenzierer__ mit der Impulsantwort $\delta'(t)$ und $H(p)=p$, gezeichnet als Kasten „$p$“;

</li>

<li>

das __Proportionalglied__, das mit einer festen Zahl $b$ multipliziert, mit $H(p)=b$, gezeichnet als Kreis mit der Zahl;

</li>

<li>

die Summierstelle, die zwei oder mehr Signale mit Vorzeichen addiert.

</li>

</ul>

In der Praxis zieht man Integrierer den Differenzierern vor. Ein Differenzierer verstärkt schnelle Schwingungen umso mehr, je schneller sie sind ($|H(\mathrm{j}2\pi f)|=2\pi f$), und damit auch jede Störung.

### Ein System erster Ordnung aus Grundbausteinen

<span class="anker" id="stufe-6-3"></span>

Der rechtsseitige Exponentialimpuls [(2.1)](beispiele-zur-laplace-transformation.html#gl-2-1) ist die Impulsantwort des Systems $H(p)=\frac{1}{p+b}$. Liest man [(4.2)](losung-von-differentialgleichungen.html#gl-4-2) bis [(4.3)](losung-von-differentialgleichungen.html#gl-4-3) rückwärts, so gehört dazu die Differentialgleichung

<span class="anker" id="gl-6-3"></span>
$$\frac{\mathrm{d} g(t)}{\mathrm{d} t}+b\cdot g(t)=s(t). \tag{6.3}$$

Der Vergleich mit [(6.2)](#gl-6-2) zeigt zwei mögliche Aufbauten: $\frac{1}{p+b}=\frac{1}{1/H_1+H_2}$ gilt mit $H_1(p)=1/p$ und $H_2(p)=b$ (Abb. [10](#abb-10)a) oder mit $H_1(p)=\frac1b$ und $H_2(p)=p$ (Abb. [10](#abb-10)b). Der erste Aufbau kommt ohne Differenzierer aus. Er lässt sich auch direkt aus [(6.3)](#gl-6-3) lesen: Der Integrierer bekommt $\frac{\mathrm{d} g}{\mathrm{d} t}=s-b\,g$ und gibt $g$ aus.

:::abbildung et3/k2erster 10
Zwei Aufbauten des Systems $H(p)=\frac{1}{p+b}$ mit dem rechtsseitigen Exponentialimpuls als Impulsantwort: (a) Integrierer vorwärts, Proportionalglied zurück; (b) Proportionalglied vorwärts, Differenzierer zurück.
:::

⁠**Kurz gesagt:** Ein Integrierer mit der Rückführung $b$ ist ein System erster Ordnung mit dem Pol $-b$.

### Drei Aufbauten eines Systems zweiter Ordnung

<span class="anker" id="stufe-6-4"></span>

Ein System zweiter Ordnung mit den Polen $-c_1$ und $-c_2$ ($c_1\ne c_2$) lässt sich auf drei Arten schreiben:

<span class="anker" id="gl-6-4"></span>
$$H(p)=\underbrace{\frac{1}{p^2+(c_1+c_2)\,p+c_1c_2}}_{\text{Polynomform}}=\underbrace{\frac{1}{p+c_1}\cdot\frac{1}{p+c_2}}_{\text{Produktform}}=\underbrace{\frac{1}{c_2-c_1}\Bigl[\frac{1}{p+c_1}-\frac{1}{p+c_2}\Bigr]}_{\text{Parallelform}} . \tag{6.4}$$

Die Parallelform prüft man über den Hauptnenner: $\frac{1}{p+c_1}-\frac{1}{p+c_2}=\frac{c_2-c_1}{(p+c_1)(p+c_2)}$. Bis auf den Faktor $1/LC$ ist das die Übertragungsfunktion [(4.17)](losung-von-differentialgleichungen.html#gl-4-17) des RLC-Systems mit $c_{1,2}=a\mp b$. Nach [(4.2)](losung-von-differentialgleichungen.html#gl-4-2) bis [(4.3)](losung-von-differentialgleichungen.html#gl-4-3) gehört zu $H(p)$ die Differentialgleichung zweiter Ordnung

<span class="anker" id="gl-6-5"></span>
$$\frac{\mathrm{d}^2g(t)}{\mathrm{d} t^2}+(c_1+c_2)\,\frac{\mathrm{d} g(t)}{\mathrm{d} t}+c_1c_2\cdot g(t)=s(t). \tag{6.5}$$

Jede der drei Formen beschreibt einen eigenen Aufbau (Abb. [11](#abb-11)):

<ul>

<li>

⁠**Direkte Darstellung (Polynomform):** Zwei Integrierer hintereinander. Der erste bekommt $\frac{\mathrm{d}^2g}{\mathrm{d} t^2}$, gibt $\frac{\mathrm{d} g}{\mathrm{d} t}$ aus, der zweite gibt $g$ aus. Nach [(6.5)](#gl-6-5) ist $\frac{\mathrm{d}^2g}{\mathrm{d} t^2}=s-(c_1+c_2)\frac{\mathrm{d} g}{\mathrm{d} t}-c_1c_2\,g$; die beiden Rückführungen bilden genau diese Differenz.

</li>

<li>

⁠**Kaskadendarstellung (Produktform):** Zwei Systeme erster Ordnung aus Abb. [10](#abb-10)a in Kette, eines mit dem Pol $-c_1$, eines mit $-c_2$.

</li>

<li>

⁠**Paralleldarstellung (Parallelform):** Zwei Systeme erster Ordnung bekommen denselben Eingang. Ihre Ausgänge werden voneinander abgezogen und mit $\frac{1}{c_2-c_1}$ multipliziert.

</li>

</ul>

:::abbildung et3/k2formen 11
Drei Aufbauten des Systems zweiter Ordnung $H(p)=\frac{1}{(p+c_1)(p+c_2)}$: (a) direkte Darstellung, (b) Kaskadendarstellung, (c) Paralleldarstellung. Kreise mit Zahl: Proportionalglieder; kleine Kreise: Summierstellen mit den Vorzeichen ihrer Eingänge.
:::

⁠**Kurz gesagt:** Polynomform, Produktform und Parallelform derselben Übertragungsfunktion sind drei verschiedene Schaltungen mit demselben Verhalten.

### Die direkte Form

<span class="anker" id="stufe-6-5"></span>

Hat das System auch Nullstellen, braucht man einen weiteren Gedanken. Als Beispiel dient der Polynombruch zweiten Grades

<span class="anker" id="gl-6-6"></span>
$$H(p)=\frac{\beta_2p^2+\beta_1p+\beta_0}{p^2+\alpha_1p+\alpha_0}=\frac{H_1(p)}{H_2(p)} \tag{6.6}$$

mit Koeffizienten wie in [(4.1)](losung-von-differentialgleichungen.html#gl-4-1), hier mit $\alpha_2=1$. Man teilt das System in zwei Teile und schaltet sie in umgekehrter Reihenfolge, was bei Produkten von Übertragungsfunktionen erlaubt ist (Abb. [12](#abb-12)a):

<ol>

<li>

⁠**Zuerst $1/H_2(p)$.** Das ist ein System ohne Nullstellen wie in Abb. [11](#abb-11)a. Sein Ausgang $g_1(t)$ erfüllt $\frac{\mathrm{d}^2g_1}{\mathrm{d} t^2}+\alpha_1\frac{\mathrm{d} g_1}{\mathrm{d} t}+\alpha_0\,g_1=s$. Es besteht aus zwei Integrierern, die das Ausgangssignal zweimal gewichtet zurückführen.

</li>

<li>

⁠**Dann $H_1(p)$.** Es bildet $g=\beta_2\,\frac{\mathrm{d}^2g_1}{\mathrm{d} t^2}+\beta_1\,\frac{\mathrm{d} g_1}{\mathrm{d} t}+\beta_0\,g_1$, also eine gewichtete Summe aus $g_1$ und seinen Ableitungen. Für sich gebaut bräuchte es zwei Differenzierer.

</li>

</ol>

Der Trick: Beide Teile brauchen dieselben Signale $g_1$, $\frac{\mathrm{d} g_1}{\mathrm{d} t}$ und $\frac{\mathrm{d}^2g_1}{\mathrm{d} t^2}$, und die Kette der Integrierer im ersten Teil liefert sie schon: Am Eingang des ersten Integrierers liegt $\frac{\mathrm{d}^2g_1}{\mathrm{d} t^2}$, zwischen den Integrierern $\frac{\mathrm{d} g_1}{\mathrm{d} t}$, am Ende $g_1$. Man greift sie dort ab und gewichtet sie mit $\beta_2$, $\beta_1$, $\beta_0$. Das ergibt die __direkte Form__ in Abb. [12](#abb-12)b, ganz ohne Differenzierer.

:::abbildung et3/k2direkt 12
(a) Hintereinanderschaltung der Systeme $1/H_2(p)$ und $H_1(p)$. (b) Direkte Form von $H(p)=H_1(p)/H_2(p)$ ohne Differenzierer: Die Integriererkette liefert $\ddot g_1$, $\dot g_1$ und $g_1$; oben die Gewichte des Zählers, unten die des Nenners. Die Summierstelle $\Sigma$ addiert, die Summierstelle unten addiert ebenfalls, und am Eingang wird ihre Summe abgezogen.
:::

Die Multiplikationsfaktoren liest man direkt ab: oben die Koeffizienten des Zählers, unten die des Nenners. Allgemein lässt sich ein Polynombruch mit $Q$ Nullstellen und $R$ Polen ($Q\le R$) so mit $R+Q+1$ Proportionalgliedern, $R+Q$ Summierern mit je zwei Eingängen und $\max(R,Q)$ Integrierern aufbauen. Im Beispiel mit $Q=R=2$ sind das 5 Proportionalglieder, 4 Summierer und 2 Integrierer.

⁠**Kurz gesagt:** Die direkte Form baut jedes rationale $H(p)$ aus einer Kette von Integrierern. Der Nenner bestimmt die Rückführungen, der Zähler die Abgriffe.

### Bauelemente im Bildbereich

<span class="anker" id="stufe-6-6"></span>

Integrierer, Differenzierer und Proportionalglied lassen sich als Wirkung elektrischer Bauelemente deuten und auch so bauen. Man überträgt dazu die Beziehung zwischen Strom und Spannung an jedem Bauelement in den Bildbereich:

<ul>

<li>

Am Ohmschen Widerstand gilt wegen der Linearität

<span class="anker" id="gl-6-7"></span>
$$u(t)=R\cdot i(t)\quad\Longrightarrow\quad U(p)=R\cdot I(p). \tag{6.7}$$

</li>

<li>

An einer Kapazität ist die Spannung das Integral des Stroms:

<span class="anker" id="gl-6-8"></span>
$$u(t)=\frac1C\int i(t)\,\mathrm{d} t\quad\Longrightarrow\quad U(p)=\frac1p\cdot\frac{I(p)}{C}. \tag{6.8}$$

</li>

<li>

An einer Induktivität ist die Spannung umgekehrt die Ableitung des Stroms:

<span class="anker" id="gl-6-9"></span>
$$u(t)=L\,\frac{\mathrm{d} i(t)}{\mathrm{d} t}\quad\Longrightarrow\quad U(p)=p\cdot L\cdot I(p). \tag{6.9}$$

</li>

</ul>

Der Quotient $Z(p)=U(p)/I(p)$ heißt __Impedanz__ des Bauelements: $R$, $\frac{1}{pC}$ und $pL$. Damit rechnet man ein Netzwerk im Bildbereich wie eine Schaltung aus Widerständen. Zwei Beispiele mit der Spannungsteilerregel:

$$\text{RC-Tiefpass: }H(p)=\frac{\frac{1}{pC}}{R+\frac{1}{pC}}=\frac{1}{1+pRC},$$

$$\text{RLC-System: }H(p)=\frac{\frac{1}{pC}}{R+pL+\frac{1}{pC}}=\frac{1}{LCp^2+RCp+1}.$$

Das sind dieselben Ergebnisse wie über die Differentialgleichung, jetzt ohne sie aufzustellen.

⁠**Kurz gesagt:** Im Bildbereich verhält sich ein Kondensator wie ein Widerstand $\frac{1}{pC}$ und eine Spule wie ein Widerstand $pL$.

:::hintergrund Warum man mit Impedanzen rechnen darf
Man stelle sich vor, alle Spannungen und Ströme im Netzwerk wären Vielfache derselben Funktion $\mathrm{e}^{pt}$. Weil $\mathrm{e}^{pt}$ eine Eigenfunktion jedes LTI-Systems ist, bleibt das im ganzen Netzwerk so. Jede Ableitung wird zu einem Faktor $p$, jedes Integral zu $1/p$. An jedem Bauelement stehen Spannung und Strom dann in einem festen Verhältnis $Z(p)$, genau wie am Ohmschen Widerstand. Die Kirchhoffschen Regeln sind Summen von Strömen und Spannungen. Sie gelten deshalb auch für die Vorfaktoren der $\mathrm{e}^{pt}$. Damit wird jedes Netzwerk aus $R$, $L$ und $C$ zu einer Schaltung aus „Widerständen“ $Z(p)$, und man rechnet mit Spannungsteiler, Reihen- und Parallelschaltung.

Für $p=\mathrm{j}2\pi F$ ist das die Wechselstromrechnung mit Zeigern, die im Kapitel zur Faltung beim Frequenzgang des RC-Tiefpasses vorkam: Der Kondensator hat dort die Impedanz $\frac{1}{\mathrm{j}2\pi FC}$. Die Laplace-Fassung erweitert sie auf wachsende und abklingende Signale und damit auf Einschaltvorgänge.
:::

### Ein System aus Messungen bestimmen

<span class="anker" id="stufe-6-7"></span>

Kennt man Eingang und Ausgang eines unbekannten LTI-Systems, liefert der Faltungssatz das System: $H(p)=G(p)/S(p)$. Dafür transformiert man zwei Signale, jedes für sich (Aufgabe [9](#aufg-9)). Die Pole des Eingangs kürzen sich dabei heraus, übrig bleiben die des Systems.

:::ltspice Ein Netzwerk zu zwei Messungen
⁠**Zeichnen:** das Netzwerk, das du in Aufgabe [9](#aufg-9)(c) gefunden hast, mit der Quelle `PULSE(0 1 0 1u 1u 100)` am Eingang und dem Ausgang am Netz `out`. Daneben, ohne Verbindung zur Schaltung, eine Verhaltensquelle `bv` am Netz `mess` mit `V=1-exp(-2*time)`. Sie spielt die gemessene Ausgangskurve.

⁠**Direktiven:** `.tran 0 3 0 1m`, `.meas tran abw MAX abs(V(out)-V(mess))`.

⁠**Was du siehst:** Stimmen Netzwerk und Bauteilwerte, liegen `V(out)` und `V(mess)` übereinander, und die größte Abweichung `abw` ist praktisch null (unter $10^{-5}$).
:::

:::aufgabe Aufgabe 8 ★★ Ein Integrierer mit Rückführung
<span class="anker" id="aufg-8"></span>

Im Vorwärtszweig sitzt ein Integrierer mit Verstärkung, $H_1(p)=K/p$ mit $K>0$ in $1/\mathrm s$, in der Rückführung $H_2(p)=1$.

<ol class="al">

<li>

Bestimme die Übertragungsfunktion $H(p)$ des ganzen Systems und ihren Pol.

</li>

<li>

Bestimme $h(t)$ für das kausale System. Für welche $K$ ist es stabil?

</li>

<li>

Vergleiche mit dem RC-Tiefpass. Welchem $RC$ entspricht $K$?

</li>

</ol>

:::loesung
(a) Mit [(6.2)](#gl-6-2): $H(p)=\dfrac{K/p}{1+K/p}=\dfrac{K}{p+K}$. Pol bei $p=-K$.

(b) Kausal, also nach [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9): $h(t)=K\,\mathrm{e}^{-Kt}\,\varepsilon(t)$. Für $K>0$ liegt der Pol links, das System ist stabil. (Für $K<0$ läge er rechts, und $h$ wüchse.)

(c) Der RC-Tiefpass hat $H(p)=\frac{1}{1+pRC}=\frac{1/RC}{p+1/RC}$. Gleichheit mit $\frac{K}{p+K}$ für $K=1/RC$, also $RC=1/K$. Je größer die Verstärkung im Vorwärtszweig, desto schneller folgt der Ausgang dem Eingang.
:::
:::

:::aufgabe Aufgabe 9 ★★ Ein unbekanntes System aus zwei Messungen
<span class="anker" id="aufg-9"></span>

An ein unbekanntes kausales LTI-System wird zur Zeit $t=0$ eine Spannung von 1 V angelegt, $s(t)=\varepsilon(t)$ in V. Am Ausgang misst man $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$ in V ($t$ in s).

<ol class="al">

<li>

Transformiere beide Signale, jedes für sich.

</li>

<li>

Bestimme $H(p)$ und daraus $h(t)$.

</li>

<li>

Um welches Netzwerk könnte es sich handeln? Welcher Wert ergibt sich?

</li>

<li>

Welcher Pol in $G(p)$ stammt vom Eingang, welcher vom System?

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$ für $\operatorname{Re} p>0$. $G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$ für $\operatorname{Re} p>0$ (Grundpaar [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) mit $p_0=0$ und $p_0=-2$).

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$. Da das System kausal ist, liegt der Konvergenzbereich rechts vom Pol: $\operatorname{Re} p>-2$. Mit [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9): $h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$ in $1/\mathrm s$.

(c) Ein RC-Tiefpass hat $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$. Der Vergleich mit $\dfrac{2}{p+2}$ ergibt $RC=0{,}5$ s, zum Beispiel $R=500\,\mathrm{k\Omega}$ und $C=1$ µ F. (Jedes andere Netzwerk mit derselben Übertragungsfunktion verhielte sich an den Klemmen genauso. Aus Messungen an Ein- und Ausgang kennt man nur $H$, nicht die Bauteile.)

(d) Der Pol $p=0$ stammt vom Eingang (Sprung), der Pol $p=-2$ vom System. Beim Teilen $G/S$ kürzt sich genau der Pol des Eingangs heraus.
:::
:::

::::kurzfassung
Zusammengesetzte Systeme berechnet man im Bildbereich mit einfacher Algebra. Umgekehrt lässt sich jedes System mit rationaler Übertragungsfunktion aus wenigen Grundbausteinen aufbauen.

Bei einer __Rückkopplung__ wird ein Teil des Ausgangs zum Eingang zurückgeführt. Das System $H_1(p)$ im __Vorwärtszweig__ erhält die Differenz aus dem Eingang und dem Signal, das das System $H_2(p)$ in der __Rückführung__ aus dem Ausgang formt. Die Differenz bildet eine __Summierstelle__. Aus $G(p)=H_1(p)\cdot\bigl[S(p)-H_2(p)\cdot G(p)\bigr]$ folgt

$$H(p)=\frac{G(p)}{S(p)}=\frac{H_1(p)}{1+H_1(p)\cdot H_2(p)} .$$

Ist $|H_1H_2|\gg1$, wird $H(p)$ nahezu gleich $\frac{1}{H_2(p)}$: Das Verhalten hängt fast nur noch von der Rückführung ab. Darauf beruht jede Operationsverstärkerschaltung mit Gegenkopplung.

Grundbausteine sind der __Integrierer__ mit $H(p)=1/p$, der __Differenzierer__ mit $H(p)=p$, das __Proportionalglied__ mit einem festen Faktor und die Summierstelle. Ein Integrierer mit der Rückführung $b$ ergibt das System erster Ordnung $\frac{1}{p+b}$. Ein System zweiter Ordnung lässt sich in Polynomform, Produktform oder Parallelform schreiben; daraus folgen die direkte Darstellung, die Kaskadendarstellung und die Paralleldarstellung, drei Schaltungen mit demselben Verhalten. Die __direkte Form__ baut jeden Polynombruch aus einer Kette von Integrierern: Der Nenner bestimmt die Rückführungen, der Zähler die Abgriffe. Man zieht Integrierer vor, weil ein Differenzierer schnelle Störungen umso stärker verstärkt, je schneller sie sind.

Im Bildbereich hat jedes Bauelement eine __Impedanz__ $Z(p)=U(p)/I(p)$, nämlich $R$, $\frac{1}{pC}$ oder $pL$. Ein Netzwerk rechnet man damit wie eine Widerstandsschaltung. Aus gemessenem Eingang und Ausgang folgt das System als $H(p)=G(p)/S(p)$.

Falle: Die Rückkopplung verschiebt auch die Pole und kann ein System instabil machen.
::::

::::formelsammlung
**Rückkopplung: Gleichung im Bildbereich**

$$G(p)=H_1(p)\cdot\bigl[S(p)-H_2(p)\cdot G(p)\bigr]$$

$H_1$ im Vorwärtszweig, $H_2$ in der Rückführung; die Summierstelle bildet die Differenz.

**Rückkopplung: Übertragungsfunktion**

$$H(p)=\frac{G(p)}{S(p)}=\frac{H_1(p)}{1+H_1(p)\cdot H_2(p)}=\frac{1}{1/H_1(p)+H_2(p)}$$

Gesamtsystem vom Eingang $S$ zum Ausgang $G$.

**Gegenkopplung**

$$H(p)=\frac{H_1}{1+H_1H_2}\approx\frac{H_1}{H_1H_2}=\frac{1}{H_2(p)}$$

Für $|H_1H_2|\gg1$: Das Gesamtsystem hängt fast nur von der Rückführung ab.

**Empfindlichkeit gegen Änderungen von $H_1$**

$$\frac{\mathrm{d} H/H}{\mathrm{d} H_1/H_1}=\frac{1}{1+H_1H_2}$$

Eine relative Änderung von $H_1$ kommt um den Faktor $1+H_1H_2$ verkleinert an.

**Grundbausteine**

$$\text{Integrierer: }H(p)=1/p,\qquad\text{Differenzierer: }H(p)=p,\qquad\text{Proportionalglied: }H(p)=b$$

Impulsantworten $\varepsilon(t)$ bzw. $\delta'(t)$; das Proportionalglied multipliziert mit der festen Zahl $b$. Dazu die Summierstelle. Integrierer werden vorgezogen, da der Differenzierer mit $|H(\mathrm{j}2\pi f)|=2\pi f$ Störungen verstärkt.

**System erster Ordnung**

$$\frac{\mathrm{d} g(t)}{\mathrm{d} t}+b\cdot g(t)=s(t),\qquad H(p)=\frac{1}{p+b}$$

Aufbau als Rückkopplung mit $H_1(p)=1/p$ und $H_2(p)=b$ (ohne Differenzierer) oder mit $H_1(p)=\frac1b$ und $H_2(p)=p$.

**System zweiter Ordnung: drei Formen**

$$H(p)=\underbrace{\frac{1}{p^2+(c_1+c_2)\,p+c_1c_2}}_{\text{Polynomform}}=\underbrace{\frac{1}{p+c_1}\cdot\frac{1}{p+c_2}}_{\text{Produktform}}=\underbrace{\frac{1}{c_2-c_1}\Bigl[\frac{1}{p+c_1}-\frac{1}{p+c_2}\Bigr]}_{\text{Parallelform}}$$

Pole $-c_1$ und $-c_2$, $c_1\ne c_2$. Aufbauten: direkte Darstellung, Kaskadendarstellung, Paralleldarstellung.

**System zweiter Ordnung: Differentialgleichung**

$$\frac{\mathrm{d}^2g(t)}{\mathrm{d} t^2}+(c_1+c_2)\,\frac{\mathrm{d} g(t)}{\mathrm{d} t}+c_1c_2\cdot g(t)=s(t)$$

Gehört zu $H(p)$ in Polynomform.

**Direkte Form**

$$H(p)=\frac{\beta_2p^2+\beta_1p+\beta_0}{p^2+\alpha_1p+\alpha_0}=\frac{H_1(p)}{H_2(p)}$$

Kette $1/H_2$ (Integrierer mit Rückführungen $\alpha_1$, $\alpha_0$), dann $H_1$ (Abgriffe $\beta_2$, $\beta_1$, $\beta_0$). Allgemein bei $Q\le R$: $R+Q+1$ Proportionalglieder, $R+Q$ Summierer mit je zwei Eingängen, $\max(R,Q)$ Integrierer.

**Ohmscher Widerstand im Bildbereich**

$$u(t)=R\cdot i(t)\quad\Longrightarrow\quad U(p)=R\cdot I(p)$$

Wegen der Linearität.

**Kapazität im Bildbereich**

$$u(t)=\frac1C\int i(t)\,\mathrm{d} t\quad\Longrightarrow\quad U(p)=\frac1p\cdot\frac{I(p)}{C}$$

Spannung ist das Integral des Stroms.

**Induktivität im Bildbereich**

$$u(t)=L\,\frac{\mathrm{d} i(t)}{\mathrm{d} t}\quad\Longrightarrow\quad U(p)=p\cdot L\cdot I(p)$$

Spannung ist die Ableitung des Stroms.

**Impedanz**

$$Z(p)=U(p)/I(p)$$

$R$, $\frac{1}{pC}$ und $pL$; Netzwerke rechnet man damit wie Widerstandsschaltungen (Spannungsteiler, Reihen- und Parallelschaltung).

**System aus Messungen**

$$H(p)=G(p)/S(p)$$

Eingang $s(t)$ und Ausgang $g(t)$ je für sich transformiert; die Pole des Eingangs kürzen sich heraus.
::::

::::lernkarten
:::karte begriff Rückkopplung
Was versteht man bei der Verbindung zweier LTI-Systeme unter einer Rückkopplung?
---
Eine Verbindung, bei der ein Teil des Ausgangs zum Eingang zurückgeführt wird. Das System $H_1(p)$ erhält die Differenz aus dem Eingang und dem zurückgeführten Signal, das vorher das System $H_2(p)$ durchlaufen hat.
--- falsch
Eine Verbindung, bei der zwei Systeme denselben Eingang bekommen und ihre Ausgänge addiert werden. Das System $H_2(p)$ arbeitet dabei parallel zu $H_1(p)$ und gleicht dessen Fehler aus, bevor sie den Ausgang erreichen.
--- falsch
Eine Verbindung, bei der der Ausgang des ersten Systems der Eingang des zweiten ist, ohne dass das zweite das erste belastet. Das Signal läuft dabei nur in einer Richtung, vom Eingang zum Ausgang, und nie zurück.
--- falsch
Eine Verbindung, bei der der Eingang eines Systems aus seinem eigenen künftigen Ausgang gebildet wird. Das System $H_1(p)$ erhält die Summe aus Eingang und vorausberechnetem Ausgang, den $H_2(p)$ vorhersagt.
:::
:::karte begriff Vorwärtszweig und Rückführung
Welche Aufgaben haben bei einer Rückkopplung das System im Vorwärtszweig und das System in der Rückführung?
---
Das System $H_1(p)$ im Vorwärtszweig erhält die Differenz aus Eingang und zurückgeführtem Signal und liefert den Ausgang. Das System $H_2(p)$ in der Rückführung formt den Ausgang, bevor er vom Eingang abgezogen wird.
--- falsch
Das System $H_2(p)$ im Vorwärtszweig formt den Eingang, bevor er abgezogen wird. Das System $H_1(p)$ in der Rückführung erhält den Ausgang und liefert die Differenz, die am Ende als Ausgang des Ganzen erscheint.
--- falsch
Das System im Vorwärtszweig verstärkt den Eingang, das System in der Rückführung schwächt ihn um denselben Faktor wieder ab. Beide zusammen lassen das Signal deshalb unverändert, und der Ausgang ist gleich dem Eingang.
--- falsch
Das System $H_1(p)$ im Vorwärtszweig liefert den Ausgang für positive Zeiten, das System $H_2(p)$ in der Rückführung den für negative Zeiten. Zusammen ergeben sie eine zweiseitige Impulsantwort des ganzen Systems.
:::
:::karte begriff Summierstelle
Was leistet eine Summierstelle in einem Blockschaltbild aus LTI-Systemen?
---
Sie addiert zwei oder mehr Signale mit den Vorzeichen, die an ihren Eingängen stehen. Bei der Rückkopplung bildet sie so die Differenz $S(p)-H_2(p)\,G(p)$.
--- falsch
Sie multipliziert zwei Signale miteinander; das Vorzeichen an ihrem Eingang gibt an, ob eines davon vorher invertiert wird. Bei der Rückkopplung bildet sie so das Produkt $S(p)\cdot H_2(p)\,G(p)$.
--- falsch
Sie summiert ein Signal über die Zeit auf, integriert es also, und hat deshalb nur einen einzigen Eingang. Bei der Rückkopplung bildet sie so das Integral des Ausgangs, das zurückgeführt wird.
--- falsch
Sie verzweigt ein Signal auf mehrere Leitungen, damit es zugleich verschiedene Systeme erreicht. Die Vorzeichen geben an, welche Leitung das Signal unverändert und welche es invertiert weitergibt.
:::
:::karte formel Übertragungsfunktion der Rückkopplung
Welche Übertragungsfunktion hat eine Rückkopplung mit $H_1(p)$ im Vorwärtszweig und $H_2(p)$ in der Rückführung, und wie erhält man sie?
---
Aus dem Blockbild liest man $G(p)=H_1(p)\cdot\bigl[S(p)-H_2(p)\cdot G(p)\bigr]$ ab, weil die Summierstelle den zurückgeführten Ausgang vom Eingang abzieht. Bringt man alle $G$ auf eine Seite, $G\,(1+H_1H_2)=H_1\,S$, ergibt sich $H(p)=\frac{G(p)}{S(p)}=\frac{H_1(p)}{1+H_1(p)\cdot H_2(p)}=\frac{1}{1/H_1(p)+H_2(p)}$.
--- falsch
Aus dem Bild liest man $G(p)=H_1(p)\cdot\bigl[S(p)+H_2(p)\cdot G(p)\bigr]$ ab, weil die Summierstelle addiert. Damit ist $H(p)=\frac{H_1(p)}{1-H_1(p)\cdot H_2(p)}$, und die Rückführung vergrößert in jedem Fall die Verstärkung des Ganzen.
--- falsch
Die beiden Systeme liegen hintereinander, Vorwärtszweig und Rückführung in Kette. Damit ist $H(p)=H_1(p)\cdot H_2(p)$, denn in einer Kette multiplizieren sich die Übertragungsfunktionen, gleichgültig, in welcher Richtung das Signal läuft.
--- falsch
Aus dem Bild liest man $G(p)=H_1(p)\cdot S(p)-H_2(p)\cdot G(p)$ ab. Bringt man alle $G$ auf eine Seite, ergibt sich $H(p)=\frac{H_1(p)}{1+H_2(p)}$; der Vorwärtszweig wirkt also nur im Zähler, die Rückführung nur im Nenner.
:::
:::karte zusammenhang Gegenkopplung
Warum hängt eine Rückkopplung mit sehr starkem Vorwärtszweig, $|H_1H_2|\gg1$, fast nur noch von der Rückführung ab, und wozu nutzt man das?
---
Dann ist die $1$ im Nenner vernachlässigbar: $H(p)=\frac{H_1}{1+H_1H_2}\approx\frac{H_1}{H_1H_2}=\frac{1}{H_2(p)}$. Ein Verstärker mit großer, aber ungenauer Verstärkung ergibt mit einem Spannungsteiler aus genauen Widerständen als $H_2$ ein System, das so genau ist wie die Widerstände.
--- falsch
Dann ist $H_2$ gegen $H_1$ vernachlässigbar, und es gilt $H(p)\approx H_1(p)$. Die Rückführung wird praktisch nicht mehr gebraucht, und man nutzt das, um einen Verstärker ohne Rückführung zu betreiben, sobald seine Verstärkung groß genug ist und nicht mehr schwankt.
--- falsch
Dann ist der Nenner sehr groß und $H(p)\approx0$: Das System lässt fast nichts mehr durch. Man nutzt das, um Störungen vollständig zu unterdrücken, und baut deshalb Rückkopplungen mit möglichst großem Vorwärtszweig als Sperrfilter für einzelne Frequenzen.
--- falsch
Dann ist die $1$ im Nenner vernachlässigbar, und es gilt $H(p)\approx H_1(p)\cdot H_2(p)$. Das System verhält sich wie eine Kette, und man nutzt das, um zwei Verstärker zu einem einzigen mit dem Produkt der beiden Verstärkungen zu verbinden.
:::
:::karte formel Empfindlichkeit gegen Schwankungen
Um welchen Faktor verkleinert eine Rückkopplung relative Änderungen der Verstärkung $H_1$, und was bedeutet das für $H_1=10^5$ und $H_2=0{,}01$?
---
Um den Faktor $1+H_1H_2$, denn $\frac{\mathrm{d} H/H}{\mathrm{d} H_1/H_1}=\frac{1}{1+H_1H_2}$. Mit $H_1H_2=1000$ ändert sich $H$ nur um etwa 0,01 %, wenn sich $H_1$ um 10 % ändert.
--- falsch
Um den Faktor $1/H_2$, denn $\frac{\mathrm{d} H/H}{\mathrm{d} H_1/H_1}=H_2$. Mit $H_2=0{,}01$ ändert sich $H$ nur um 0,1 %, wenn sich $H_1$ um 10 % ändert; die Größe von $H_1$ spielt dabei keine Rolle.
--- falsch
Gar nicht, denn $\frac{\mathrm{d} H/H}{\mathrm{d} H_1/H_1}=1$, weil $H_1$ im Zähler steht und sich jede relative Änderung unverändert fortpflanzt. Ändert sich $H_1$ um 10 %, ändert sich auch $H$ um 10 %.
--- falsch
Um den Faktor $H_1$, denn $\frac{\mathrm{d} H/H}{\mathrm{d} H_1/H_1}=\frac{1}{H_1}$. Mit $H_1=10^5$ ändert sich $H$ nur um 0,0001 %, wenn sich $H_1$ um 10 % ändert, ganz unabhängig von der Rückführung.
:::
:::karte begriff Integrierer
Welche Impulsantwort und welche Übertragungsfunktion hat der Integrierer als Grundbaustein, und wie zeichnet man ihn?
---
Er hat die Impulsantwort $\varepsilon(t)$ und die Übertragungsfunktion $H(p)=1/p$; man zeichnet ihn als Kasten „$1/p$“. Er ist einer der vier Grundbausteine, aus denen sich jede rationale Übertragungsfunktion aufbauen lässt.
--- falsch
Er hat die Impulsantwort $\delta'(t)$ und die Übertragungsfunktion $H(p)=p$; man zeichnet ihn als Kasten „$p$“. Er ist einer der vier Grundbausteine und wird in der Praxis wegen seiner Störfestigkeit bevorzugt.
--- falsch
Er hat die Impulsantwort $t\,\varepsilon(t)$ und die Übertragungsfunktion $H(p)=1/p^2$; man zeichnet ihn als Kreis mit der Zahl $1/p$. Für jede Ordnung des Systems braucht man genau einen solchen Baustein.
--- falsch
Er hat die Impulsantwort $\varepsilon(t)$ und die Übertragungsfunktion $H(p)=p$, weil er die Fläche unter dem Signal bildet; man zeichnet ihn als Kasten mit Integralzeichen. Er ist der einzige Grundbaustein mit Gedächtnis.
:::
:::karte begriff Proportionalglied
Was macht das Proportionalglied als Grundbaustein mit einem Signal, und welche Übertragungsfunktion hat es?
---
Es multipliziert das Signal mit einer festen Zahl $b$, hat also $H(p)=b$; man zeichnet es als Kreis mit der Zahl.
--- falsch
Es verzögert das Signal um eine feste Zeit $b$, hat also $H(p)=\mathrm{e}^{-pb}$; man zeichnet es als Kreis mit der Zahl.
--- falsch
Es addiert eine feste Zahl $b$ zum Signal, hat also $H(p)=b/p$; man zeichnet es als Kreis mit der Zahl.
--- falsch
Es multipliziert das Signal mit einer Zahl $b$, hat aber $H(p)=b\,p$, weil jedes LTI-System eine Ableitung enthält.
:::
:::karte zusammenhang Differenzierer
Warum zieht man beim Aufbau aus Grundbausteinen Integrierer den Differenzierern vor?
---
Ein Differenzierer verstärkt schnelle Schwingungen umso mehr, je schneller sie sind, denn $|H(\mathrm{j}2\pi f)|=2\pi f$. Damit verstärkt er auch jede Störung.
--- falsch
Ein Differenzierer schwächt schnelle Schwingungen umso mehr, je schneller sie sind, denn $|H(\mathrm{j}2\pi f)|=1/(2\pi f)$. Damit gehen auch die Nutzsignale verloren.
--- falsch
Ein Differenzierer ist nicht kausal, weil er zur Ableitung den künftigen Verlauf des Signals kennen muss. Deshalb lässt er sich gar nicht bauen, nur der Integrierer.
--- falsch
Ein Differenzierer hat einen Pol bei $p=0$ und ist deshalb instabil, während der Integrierer an dieser Stelle eine Nullstelle hat und stets stabil bleibt.
:::
:::karte formel System erster Ordnung aus Grundbausteinen
Wie baut man das System $H(p)=\frac{1}{p+b}$ aus Grundbausteinen auf, ohne einen Differenzierer zu verwenden?
---
Mit einem Integrierer $H_1(p)=1/p$ im Vorwärtszweig und einem Proportionalglied $H_2(p)=b$ in der Rückführung, denn $\frac{1}{p+b}=\frac{1}{1/H_1+H_2}$. Der Integrierer bekommt $\frac{\mathrm{d} g}{\mathrm{d} t}=s-b\,g$ und gibt $g$ aus.
--- falsch
Mit einem Proportionalglied $H_1(p)=\frac1b$ im Vorwärtszweig und einem Integrierer $H_2(p)=1/p$ in der Rückführung, denn $\frac{1}{p+b}=\frac{1}{1/H_1+H_2}$. Der Integrierer bildet das Integral des Ausgangs und führt es zurück.
--- falsch
Mit einem Integrierer $1/p$ und einem Proportionalglied $b$ in Kette, ohne Rückführung, denn in einer Kette multiplizieren sich die Übertragungsfunktionen zu $\frac{1}{p+b}$. Der Integrierer bekommt $s$ und gibt $g/b$ aus.
--- falsch
Mit einem Integrierer $H_1(p)=1/p$ im Vorwärtszweig und einem Proportionalglied $H_2(p)=-b$ in der Rückführung, weil die Summierstelle das zurückgeführte Signal ohnehin abzieht. Der Integrierer bekommt $\frac{\mathrm{d} g}{\mathrm{d} t}=s+b\,g$.
:::
:::karte formel Polynomform, Produktform und Parallelform
Wie schreibt man die Übertragungsfunktion eines Systems zweiter Ordnung mit den Polen $-c_1$ und $-c_2$, $c_1\ne c_2$, in Polynomform, Produktform und Parallelform?
---
$H(p)=\frac{1}{p^2+(c_1+c_2)\,p+c_1c_2}=\frac{1}{p+c_1}\cdot\frac{1}{p+c_2}=\frac{1}{c_2-c_1}\Bigl[\frac{1}{p+c_1}-\frac{1}{p+c_2}\Bigr]$. Die Parallelform prüft man über den Hauptnenner: $\frac{1}{p+c_1}-\frac{1}{p+c_2}=\frac{c_2-c_1}{(p+c_1)(p+c_2)}$.
--- falsch
$H(p)=\frac{1}{p^2+(c_1+c_2)\,p+c_1c_2}=\frac{1}{p+c_1}+\frac{1}{p+c_2}$; Produktform und Parallelform stimmen überein, weil sich bei zwei Polen die Brüche einfach addieren. Prüfen kann man das über den Hauptnenner $(p+c_1)(p+c_2)$.
--- falsch
$H(p)=\frac{1}{p^2+c_1c_2\,p+(c_1+c_2)}=\frac{1}{p+c_1}\cdot\frac{1}{p+c_2}=\frac{1}{c_1-c_2}\Bigl[\frac{1}{p+c_1}-\frac{1}{p+c_2}\Bigr]$. Der Vorfaktor der Parallelform ist der Kehrwert des Abstands der Pole.
--- falsch
$H(p)=\frac{1}{p^2-(c_1+c_2)\,p+c_1c_2}=\frac{1}{p-c_1}\cdot\frac{1}{p-c_2}=\frac{1}{c_2-c_1}\Bigl[\frac{1}{p-c_1}-\frac{1}{p-c_2}\Bigr]$, weil die Pole bei $-c_1$ und $-c_2$ liegen und das Minus in jeden Faktor eingeht.
:::
:::karte zusammenhang Drei Aufbauten eines Systems zweiter Ordnung
Welche drei Aufbauten aus Grundbausteinen gehören zur Polynomform, zur Produktform und zur Parallelform eines Systems zweiter Ordnung?
---
Polynomform: direkte Darstellung, zwei Integrierer hintereinander mit zwei Rückführungen. Produktform: Kaskadendarstellung, zwei Systeme erster Ordnung in Kette. Parallelform: Paralleldarstellung, zwei Systeme erster Ordnung am selben Eingang, deren Ausgänge man voneinander abzieht und mit $\frac{1}{c_2-c_1}$ multipliziert.
--- falsch
Polynomform: zwei Systeme erster Ordnung mit demselben Eingang, deren Ausgänge addiert werden. Produktform: zwei Integrierer hintereinander mit zwei Rückführungen, deren Gewichte die Koeffizienten sind. Parallelform: zwei Systeme erster Ordnung in Kette, verbunden durch ein Proportionalglied $\frac{1}{c_2-c_1}$.
--- falsch
Alle drei Formen führen auf denselben Aufbau mit zwei Integrierern hintereinander; sie unterscheiden sich nur in der Schreibweise auf dem Papier, nicht in der Schaltung. Verschiedene Aufbauten gibt es erst bei Systemen dritter Ordnung, weil man dort die Pole verschieden gruppieren kann.
--- falsch
Polynomform: zwei Differenzierer hintereinander, weil die Differentialgleichung zwei Ableitungen enthält. Produktform: zwei Differenzierer nebeneinander am selben Eingang. Parallelform: ein Integrierer und ein Differenzierer in Kette, deren Ausgänge am Ende addiert und mit $\frac{1}{c_2-c_1}$ multipliziert werden.
:::
:::karte begriff direkte Form
Was ist die direkte Form eines Systems $H(p)=\frac{\beta_2p^2+\beta_1p+\beta_0}{p^2+\alpha_1p+\alpha_0}$, und warum braucht sie keinen Differenzierer?
---
Ein Aufbau aus einer Kette von Integrierern, deren Rückführungen die Nennerkoeffizienten $\alpha_1$, $\alpha_0$ tragen. Die Kette liefert schon $\ddot g_1$, $\dot g_1$ und $g_1$; diese greift man ab und gewichtet sie mit den Zählerkoeffizienten $\beta_2$, $\beta_1$, $\beta_0$, statt den Zähler mit Differenzierern zu bauen.
--- falsch
Ein Aufbau, bei dem man Zähler und Nenner getrennt baut: zuerst den Zähler mit zwei Differenzierern, dann den Kehrwert des Nenners mit zwei Integrierern. Die Differenzierer heben sich mit den Integrierern auf, sodass am Ende effektiv keine Ableitung übrig bleibt.
--- falsch
Ein Aufbau, der $H(p)$ in die Produktform zerlegt und für jedes Paar aus Nullstelle und Pol ein eigenes System erster Ordnung baut. Diese Teile kommen ohne Differenzierer aus, weil jedes nur einen Pol und eine Nullstelle hat und sich beide gegenseitig aufheben.
--- falsch
Ein Aufbau aus einer Kette von Integrierern, deren Rückführungen die Zählerkoeffizienten $\beta_2$, $\beta_1$, $\beta_0$ tragen; die Abgriffe tragen die Nennerkoeffizienten $\alpha_1$, $\alpha_0$. Differenzierer braucht sie nicht, weil der Zähler im Rückweg liegt.
:::
:::karte begriff Impedanz
Was ist die Impedanz eines Bauelements im Bildbereich, und welche Werte haben Widerstand, Kapazität und Induktivität?
---
Der Quotient $Z(p)=U(p)/I(p)$ aus Spannung und Strom im Bildbereich: $R$ für den Widerstand, $\frac{1}{pC}$ für die Kapazität und $pL$ für die Induktivität. Damit rechnet man ein Netzwerk im Bildbereich wie eine Schaltung aus Widerständen.
--- falsch
Der Quotient $Z(p)=I(p)/U(p)$ aus Strom und Spannung im Bildbereich: $1/R$ für den Widerstand, $pC$ für die Kapazität und $\frac{1}{pL}$ für die Induktivität. Damit rechnet man ein Netzwerk wie eine Schaltung aus Leitwerten.
--- falsch
Der Quotient $Z(p)=U(p)/I(p)$ im Bildbereich: $R$ für den Widerstand, $pC$ für die Kapazität und $\frac{1}{pL}$ für die Induktivität, weil die Spannung an der Kapazität die Ableitung des Stroms ist. Damit rechnet man wie mit Widerständen.
--- falsch
Der Gleichstromwiderstand eines Bauelements, gemessen bei $p=0$: $R$ für den Widerstand, unendlich für die Kapazität und null für die Induktivität. Im Bildbereich ist er für alle $p$ derselbe, weil Bauteilwerte nicht von der Frequenz abhängen.
:::
:::karte zusammenhang Rechnen mit Impedanzen
Warum darf man ein Netzwerk aus $R$, $L$ und $C$ im Bildbereich wie eine Schaltung aus Widerständen berechnen?
---
Sind alle Spannungen und Ströme Vielfache derselben Eigenfunktion $\mathrm{e}^{pt}$, bleibt das im ganzen Netzwerk so; jede Ableitung wird ein Faktor $p$, jedes Integral ein Faktor $1/p$. An jedem Bauelement stehen Spannung und Strom dann im festen Verhältnis $Z(p)$, und die Kirchhoffschen Regeln gelten auch für die Vorfaktoren.
--- falsch
Weil Spulen und Kondensatoren im Bildbereich ihre Energiespeicher verlieren und zu Ohmschen Widerständen werden. Die Ableitungen in ihren Gleichungen verschwinden ganz, und es bleiben reine Proportionalitäten zwischen Strom und Spannung mit reellen Faktoren.
--- falsch
Weil die Kirchhoffschen Regeln im Bildbereich nicht mehr gelten und durch das Ohmsche Gesetz ersetzt werden. Jedes Bauelement wird für sich mit seiner eigenen Spannung berechnet, und die Spannungen an den einzelnen Bauelementen addiert man am Ende einfach auf, ohne auf Maschen zu achten.
--- falsch
Sind alle Spannungen und Ströme Vielfache von $\mathrm{e}^{pt}$, wird jede Ableitung zum Faktor $1/p$ und jedes Integral zum Faktor $p$. An jedem Bauelement stehen Spannung und Strom dann im festen Verhältnis $Z(p)$, das allerdings nur für reelle $p$ gilt.
:::
:::karte formel Spannungsteiler im Bildbereich
Wie erhält man die Übertragungsfunktionen des RC-Tiefpasses und des RLC-Systems mit Impedanzen, ohne die Differentialgleichung aufzustellen?
---
Mit der Spannungsteilerregel: $H(p)=\frac{\frac{1}{pC}}{R+\frac{1}{pC}}=\frac{1}{1+pRC}$ für den RC-Tiefpass und $H(p)=\frac{\frac{1}{pC}}{R+pL+\frac{1}{pC}}=\frac{1}{LCp^2+RCp+1}$ für das RLC-System.
--- falsch
Mit der Spannungsteilerregel: $H(p)=\frac{R}{R+\frac{1}{pC}}=\frac{pRC}{1+pRC}$ für den RC-Tiefpass und entsprechend $\frac{R}{R+pL+\frac{1}{pC}}$ für das RLC-System, weil die Ausgangsspannung am Widerstand liegt.
--- falsch
Mit der Spannungsteilerregel: $H(p)=\frac{pC}{R+pC}$ für den RC-Tiefpass und $H(p)=\frac{pC}{R+pL+pC}$ für das RLC-System, weil die Impedanz des Kondensators $pC$ ist und mit der Frequenz wächst.
--- falsch
Mit der Reihenschaltung: $H(p)=R+\frac{1}{pC}$ für den RC-Tiefpass und $H(p)=R+pL+\frac{1}{pC}$ für das RLC-System, weil sich in Reihe die Impedanzen addieren und das Verhältnis der Spannungen ergeben.
:::
:::karte zusammenhang System aus Messungen
Wie bestimmt man ein unbekanntes LTI-System aus einem gemessenen Eingang und Ausgang, und was geschieht dabei mit den Polen des Eingangs?
---
Man transformiert beide Signale, jedes für sich, und teilt: Nach dem Faltungssatz ist $H(p)=G(p)/S(p)$. Die Pole des Eingangs kürzen sich dabei heraus, und übrig bleiben die des Systems; aus den Messungen kennt man nur $H$, nicht die Bauteile.
--- falsch
Man teilt den gemessenen Ausgang zu jedem Zeitpunkt durch den Eingang, $h(t)=g(t)/s(t)$, und transformiert das Ergebnis. Die Pole des Eingangs bleiben dabei erhalten und erscheinen zusätzlich zu denen des Systems in $H(p)$.
--- falsch
Man transformiert beide Signale und multipliziert sie: $H(p)=G(p)\cdot S(p)$. Die Pole des Eingangs verdoppeln sich dabei, und die doppelten Pole kennzeichnet man als Pole des Eingangs, die einfachen als Pole des Systems.
--- falsch
Man transformiert beide Signale und teilt: $H(p)=G(p)/S(p)$. Die Pole des Eingangs werden dabei zu Nullstellen des Systems, und aus diesen Polen und Nullstellen kann man die Bauteile der Schaltung samt ihren Werten eindeutig zurückrechnen.
:::
:::karte zusammenhang Impedanz und Zeigerrechnung
Wie hängt die Rechnung mit Impedanzen $Z(p)$ mit der Wechselstromrechnung mit Zeigern zusammen?
---
Für $p=\mathrm{j}2\pi F$ ist sie genau die Zeigerrechnung; der Kondensator hat dann die Impedanz $\frac{1}{\mathrm{j}2\pi FC}$. Die Laplace-Fassung erweitert sie auf wachsende und abklingende Signale und damit auf Einschaltvorgänge.
--- falsch
Für reelle $p$ ist sie genau die Zeigerrechnung; der Kondensator hat dann die Impedanz $\frac{1}{pC}$. Die Laplace-Fassung beschränkt sie auf abklingende Signale, weil Zeiger nur für gedämpfte Schwingungen gelten.
--- falsch
Beide haben nichts miteinander zu tun: Die Zeigerrechnung gilt für Gleichspannung, die Impedanzrechnung für Wechselspannung. Der Kondensator hat in der Zeigerrechnung deshalb immer die Impedanz unendlich.
--- falsch
Für $p=\mathrm{j}2\pi F$ ist sie die Zeigerrechnung, aber mit vertauschten Rollen: Der Kondensator hat dort die Impedanz $\mathrm{j}2\pi FC$. Die Laplace-Fassung erweitert sie auf Gleichspannung, die in der Zeigerrechnung fehlt.
:::
::::
