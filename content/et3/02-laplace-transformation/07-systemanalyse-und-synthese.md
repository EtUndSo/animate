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
