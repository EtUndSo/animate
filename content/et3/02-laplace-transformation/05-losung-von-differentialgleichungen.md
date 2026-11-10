---
title: Lösung von Differentialgleichungen
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Laplace-Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Kapitel 2: Laplace-Transformation
order: 3220500
summary: Jedes Netzwerk aus Widerständen, Spulen und Kondensatoren wird durch eine lineare Differentialgleichung beschrieben.
tags: Koeffizienten, linear, Ordnung, charakteristische Polynom, Eigenbewegungen, Kennkreisfrequenz, Dämpfungsgrad, Kennwiderstand
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Jedes Netzwerk aus Widerständen, Spulen und Kondensatoren wird durch eine lineare Differentialgleichung beschrieben. Dieser Abschnitt macht daraus mit der Ableitungsregel eine algebraische Gleichung und zeigt, wie man das Ergebnis in den Zeitbereich zurückholt.
:::

### Lineare Differentialgleichungen mit konstanten Koeffizienten

<span class="anker" id="stufe-4-1"></span>

Ein LTI-System mit der Eingangsspannung $u_1(t)$ und der Ausgangsspannung $u_2(t)$ wird oft durch eine Gleichung dieser Form beschrieben:

<span class="anker" id="gl-4-1"></span>
$$\sum_{r=0}^{R}\alpha_r\,\frac{\mathrm{d}^r u_2(t)}{\mathrm{d} t^r}=\sum_{q=0}^{Q}\beta_q\,\frac{\mathrm{d}^q u_1(t)}{\mathrm{d} t^q}. \tag{4.1}$$

Die Zahlen $\alpha_r$ und $\beta_q$ heißen __Koeffizienten__. Sie sind reell und hängen nicht von der Zeit ab, denn sie stammen aus den Bauteilwerten. Die Gleichung ist __linear__: $u_1$, $u_2$ und ihre Ableitungen kommen nur in der ersten Potenz vor und werden nie miteinander multipliziert. Die höchste Ableitung des Ausgangs, $R$, heißt __Ordnung__ der Gleichung. Die nullte Ableitung ist das Signal selbst.

::::beispiel der RC-Tiefpass
Die Maschenregel ergibt $u_1=R\,i+u_2$, und durch den Kondensator fließt $i=C\,\frac{\mathrm{d} u_2}{\mathrm{d} t}$. Zusammen:

$$RC\,\frac{\mathrm{d} u_2(t)}{\mathrm{d} t}+u_2(t)=u_1(t).$$

Das ist [(4.1)](#gl-4-1) mit $R=1$, $\alpha_1=RC$, $\alpha_0=1$ und $Q=0$, $\beta_0=1$. (Das $R$ als Ordnung und das $R$ als Widerstand sind hier zufällig gleich geschrieben; aus dem Zusammenhang ist klar, was gemeint ist.)
::::

⁠**Kurz gesagt:** Eine lineare Differentialgleichung mit konstanten Koeffizienten verknüpft gewichtete Ableitungen von Ausgang und Eingang.

### Die Gleichung im Bildbereich

<span class="anker" id="stufe-4-2"></span>

Nach [(3.4)](pole-und-nullstellen-in-der-ebene.html#gl-3-4) wird jede Ableitung im Bildbereich zum Faktor $p$, die $r$-te Ableitung zum Faktor $p^r$. Die Transformation ist linear, also darf man jeden Summanden einzeln transformieren:

<span class="anker" id="gl-4-2"></span>
$$\Bigl(\sum_{r=0}^{R}\alpha_r\,p^r\Bigr)\,U_2(p)=\Bigl(\sum_{q=0}^{Q}\beta_q\,p^q\Bigr)\,U_1(p). \tag{4.2}$$

Aus der Differentialgleichung ist eine algebraische Gleichung geworden: Es kommen nur noch Multiplikationen mit Polynomen in $p$ vor.

⁠**Kurz gesagt:** Im Bildbereich wird aus jeder Ableitung ein Faktor $p$ und aus der Differentialgleichung eine algebraische Gleichung.

### Die Übertragungsfunktion als Polynombruch

<span class="anker" id="stufe-4-3"></span>

Der Ausgang ist $u_2=u_1*h$, im Bildbereich nach dem Faltungssatz $U_2(p)=H(p)\,U_1(p)$. Löst man [(4.2)](#gl-4-2) nach $U_2/U_1$ auf, erhält man die Übertragungsfunktion, die Transformierte der Impulsantwort:

<span class="anker" id="gl-4-3"></span>
$$\mathcal{L}\{h(t)\}=H(p)=\frac{U_2(p)}{U_1(p)}=\frac{\sum_{q=0}^{Q}\beta_q\,p^q}{\sum_{r=0}^{R}\alpha_r\,p^r}. \tag{4.3}$$

Damit kennt man auch Nullstellen und Pole:

<ul>

<li>

Die Nullstellen sind die $Q$ Lösungen von

<span class="anker" id="gl-4-4"></span>
$$\sum_{q=0}^{Q}\beta_q\,p^q=0 . \tag{4.4}$$

</li>

<li>

Die Pole sind die $R$ Lösungen von

<span class="anker" id="gl-4-5"></span>
$$\sum_{r=0}^{R}\alpha_r\,p^r=0 . \tag{4.5}$$

</li>

</ul>

Die Pole hängen also nur von der linken Seite ab, also davon, wie der Ausgang auf sich selbst zurückwirkt. Die Nullstellen hängen nur davon ab, wie der Eingang in die Gleichung eingeht.

::::beispiel
Für den RC-Tiefpass ist $H(p)=\frac{1}{RC\,p+1}$, mit einem Pol bei $p=-1/RC$ und ohne Nullstelle. Das ist dasselbe Ergebnis, das im ersten Abschnitt aus der Impulsantwort herauskam, jetzt aber ohne $h(t)$ zu kennen.
::::

⁠**Kurz gesagt:** Die Übertragungsfunktion eines Systems mit Differentialgleichung ist ein Bruch aus zwei Polynomen, deren Koeffizienten man direkt aus der Gleichung abliest.

:::hintergrund Warum die Pole die Eigenbewegungen des Systems sind
Eine lineare Differentialgleichung mit konstanten Koeffizienten löst man klassisch mit dem Exponentialansatz. Für die *homogene* Gleichung, also ohne Eingang,

$$\sum_{r=0}^{R}\alpha_r\,\frac{\mathrm{d}^r u_2}{\mathrm{d} t^r}=0,$$

setzt man $u_2(t)=\mathrm{e}^{\lambda t}$ ein. Jede Ableitung liefert einen Faktor $\lambda$, und es bleibt $\bigl(\sum_r\alpha_r\lambda^r\bigr)\mathrm{e}^{\lambda t}=0$. Das __charakteristische Polynom__ $\sum_r\alpha_r\lambda^r$ muss also null sein. Das ist genau der Nenner von $H(p)$, und seine Nullstellen sind die Pole [(4.5)](#gl-4-5).

Die Pole sind also die Exponenten der Bewegungen, die das System *ohne jeden Eingang* ausführen kann: seine __Eigenbewegungen__. Ein RC-Glied, dessen Kondensator geladen ist, entlädt sich mit $\mathrm{e}^{-t/RC}$; sein Pol liegt bei $-1/RC$. Damit wird auch klar, warum $H(p)$ an einem Pol unendlich ist. $H(p)$ ist das Verhältnis Ausgang zu Eingang für $\mathrm{e}^{pt}$, und für $p=p_\mathrm P$ gibt es einen Ausgang $\mathrm{e}^{p_\mathrm Pt}$ ganz ohne Eingang. Liegt der Eingang in der Nähe einer Eigenbewegung, antwortet das System entsprechend stark; das ist Resonanz.

Die Impulsantwort besteht deshalb aus Eigenbewegungen: Der Dirac-Impuls gibt dem System einen Stoß, danach bewegt es sich frei. Die Nullstellen dagegen sind nach dem Kasten „Landschaft“ im dritten Abschnitt die Exponentialfunktionen, die das System sperrt.
:::

### Beispiel: das RLC-System

<span class="anker" id="stufe-4-4"></span>

Das Netzwerk in Abb. [6](#abb-6) besteht aus einem Widerstand $R$ und einer Spule $L$ in Reihe und einem Kondensator $C$, an dem die Ausgangsspannung abgegriffen wird.

:::abbildung et3/k2rlc 6
RLC-System: Widerstand und Spule in Reihe, der Ausgang $u_2(t)$ liegt am Kondensator.
:::

**Die Differentialgleichung.** Die Maschenregel und $i=C\,\frac{\mathrm{d} u_2}{\mathrm{d} t}$ ergeben

<span class="anker" id="gl-4-6"></span>
$$R\cdot i(t)+L\cdot\frac{\mathrm{d} i(t)}{\mathrm{d} t}+u_2(t)=LC\,\frac{\mathrm{d}^2u_2(t)}{\mathrm{d} t^2}+RC\,\frac{\mathrm{d} u_2(t)}{\mathrm{d} t}+u_2(t)=u_1(t). \tag{4.6}$$

**Die Übertragungsfunktion.** Mit [(4.2)](#gl-4-2) bis [(4.5)](#gl-4-5):

$$LC\,p^2\,U_2(p)+RC\,p\,U_2(p)+U_2(p)=U_1(p)$$

<span class="anker" id="gl-4-7"></span>
$$\Longrightarrow\quad H(p)=\frac{U_2(p)}{U_1(p)}=\frac{1}{LCp^2+RCp+1}=\frac{1/LC}{p^2+(R/L)\,p+1/LC}. \tag{4.7}$$

**Die Pole.** Der Nenner $p^2+(R/L)\,p+1/LC$ wird null für

<span class="anker" id="gl-4-8"></span>
$$p_{\mathrm P1,2}=-\underbrace{\frac{R}{2L}}_{a}\pm\underbrace{\sqrt{\frac{R^2}{4L^2}-\frac{1}{LC}}}_{b}. \tag{4.8}$$

Die Abkürzungen $a$ und $b$ werden im Folgenden oft gebraucht. Gleichwertig schreibt man die Pole mit zwei anderen Kenngrößen:

<span class="anker" id="gl-4-9"></span>
$$p_{\mathrm P1,2}=-\underbrace{\xi\,\omega_0}_{a}\pm\underbrace{\omega_0\sqrt{\xi^2-1}}_{b}\qquad\text{mit}\qquad\omega_0=\frac{1}{\sqrt{LC}}\quad\text{und}\quad\xi=\frac R2\sqrt{\frac CL}. \tag{4.9}$$

Die Größe $\omega_0$ heißt __Kennkreisfrequenz__, gemessen in $1/\mathrm s$. Der Faktor $\xi$ ist eine reine Zahl und heißt __Dämpfungsgrad__. Einsetzen bestätigt $\xi\omega_0=\frac R2\sqrt{\frac CL}\cdot\frac{1}{\sqrt{LC}}=\frac{R}{2L}=a$.

Ob $b$ reell oder imaginär ist, entscheidet über die Lage der Pole (Abb. [7](#abb-7)):

<ul>

<li>

$\frac{R^2}{4L^2}>\frac{1}{LC}$, also $\xi>1$: Zwei reelle Pole auf der negativen reellen Achse, symmetrisch um $-\xi\omega_0$ im Abstand $\omega_0\sqrt{\xi^2-1}$.

</li>

<li>

$\frac{R^2}{4L^2}<\frac{1}{LC}$, also $\xi<1$: Ein Paar konjugiert komplexer Pole $-\xi\omega_0\pm\mathrm{j}\omega_0\sqrt{1-\xi^2}$. Beide liegen auf dem Kreis mit dem Radius $\omega_0$ um den Ursprung, denn $\xi^2\omega_0^2+\omega_0^2(1-\xi^2)=\omega_0^2$. Der Winkel $\theta$ zwischen der negativen reellen Achse und der Verbindungslinie zum Pol erfüllt $\cos\theta=\xi\omega_0/\omega_0=\xi$, also $\theta=\arccos\xi$.

</li>

</ul>

:::abbildung et3/k2rlcpole 7
Pole des RLC-Systems (Kreuze) und Konvergenzbereich des kausalen Systems (blau). (a) $\xi<1$, also $\frac{R^2}{4L^2}<\frac{1}{LC}$: konjugiert komplexes Polpaar auf dem Kreis mit Radius $\omega_0$ (gezeichnet für $\xi=0{,}5$). (b) $\xi>1$: zwei reelle Pole im Abstand $2\omega_0\sqrt{\xi^2-1}$ (gezeichnet für $\xi=1{,}25$).
:::

⁠**Kurz gesagt:** Das RLC-System hat zwei Pole. Bei kleinem Widerstand ($\xi<1$) bilden sie ein konjugiert komplexes Paar, bei großem ($\xi>1$) liegen beide auf der reellen Achse.

:::hintergrund Was im RLC-Kreis physikalisch passiert
Der Kondensator speichert Energie in seinem elektrischen Feld, $\frac12Cu_2^2$, die Spule in ihrem Magnetfeld, $\frac12Li^2$. Ein geladener Kondensator treibt einen Strom durch die Spule. Die Spule hält diesen Strom aufrecht, auch wenn der Kondensator leer ist, und lädt ihn mit umgekehrter Polarität wieder auf. Die Energie pendelt so zwischen den beiden Speichern hin und her. Ohne Widerstand wäre das eine ungedämpfte Schwingung mit der Kreisfrequenz $\omega_0=1/\sqrt{LC}$; deshalb heißt $\omega_0$ Kennkreisfrequenz.

Der Widerstand wandelt bei jedem Durchgang die Leistung $R\,i^2$ in Wärme um, die Schwingung klingt ab. Der Dämpfungsgrad vergleicht beides:

$$\xi=\frac R2\sqrt{\frac CL}=\frac{R}{2\sqrt{L/C}} .$$

Die Größe $\sqrt{L/C}$ hat die Einheit $\Omega$ und heißt __Kennwiderstand__. Ist $R$ klein gegen ihn, verliert der Kreis pro Schwingung wenig Energie und schwingt lange ($\xi<1$). Ist $R$ groß, wird die Energie verbraucht, bevor sie einmal hin- und zurückgependelt ist, und die Spannung kriecht zurück ($\xi>1$). Der aperiodische Grenzfall $\xi=1$ ist der schnellste Weg zurück zur Ruhe ohne Überschwingen. Deshalb legt man Zeigermessgeräte und die Stoßdämpfer von Autos in die Nähe dieses Falls: Feder, Masse und Dämpfer gehorchen derselben Differentialgleichung, mit der Masse an der Stelle von $L$, der Dämpfung an der Stelle von $R$ und der Federsteifigkeit an der Stelle von $1/C$.
:::

### Partialbruchzerlegung

<span class="anker" id="stufe-4-5"></span>

Um aus $H(p)$ die Impulsantwort zu gewinnen, zerlegt man den Bruch in Summanden, die man einzeln als Grundpaare kennt. Die Grundpaare [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) und [(2.10)](beispiele-zur-laplace-transformation.html#gl-2-10) haben die Form $\frac{1}{p-p_0}$. Also sucht man eine Zerlegung in Brüche mit je einem Pol im Nenner.

:::satz Satz 4.1 (Partialbruchzerlegung bei einfachen Polen)
<span class="anker" id="satz-4-1"></span>

Hat $H(p)$ in der Produktform [(3.1)](pole-und-nullstellen-in-der-ebene.html#gl-3-1) $R$ verschiedene Pole und höchstens so viele Nullstellen wie Pole ($Q\le R$), so gilt

<span class="anker" id="gl-4-10"></span>
$$H(p)=H_0\,\frac{\prod_{q=1}^{Q}\bigl(p-p_{\mathrm N,q}\bigr)}{\prod_{r=1}^{R}\bigl(p-p_{\mathrm P,r}\bigr)}=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_{\mathrm P,r}} \tag{4.10}$$

mit den Vorfaktoren

<span class="anker" id="gl-4-11"></span>
$$A_0=\lim_{p\to\infty}H(p)\ ;\qquad A_r=\lim_{p\to p_{\mathrm P,r}}\bigl[H(p)\,(p-p_{\mathrm P,r})\bigr]. \tag{4.11}$$
:::

Die Zerlegung heißt __Partialbruchzerlegung__, die Zahlen $A_r$ heißen Partialbruchkoeffizienten. $A_0$ ist nur dann von null verschieden, wenn Zähler und Nenner denselben Grad haben ($Q=R$). Dann ist $A_0=H_0$.

**Warum die Formel für $A_r$ stimmt.** Man multipliziert [(4.10)](#gl-4-10) mit $(p-p_{\mathrm P,r})$. Auf der rechten Seite bleibt $A_r$ allein stehen, alle anderen Summanden enthalten danach den Faktor $(p-p_{\mathrm P,r})$. Lässt man nun $p\to p_{\mathrm P,r}$ gehen, verschwinden sie, und es bleibt $A_r$.

::::beispiel mit zwei Polen und zwei Nullstellen
<span class="anker" id="gl-4-12"></span>
$$H(p)=H_0\,\frac{(p-p_{\mathrm N1})(p-p_{\mathrm N2})}{(p-p_{\mathrm P1})(p-p_{\mathrm P2})}=A_0+\frac{A_1}{p-p_{\mathrm P1}}+\frac{A_2}{p-p_{\mathrm P2}}. \tag{4.12}$$

Hier ist nach [(4.11)](#gl-4-11) $A_0=H_0$, denn für $p\to\infty$ geht der Bruch gegen 1. Multipliziert man [(4.12)](#gl-4-12) mit $(p-p_{\mathrm P1})$, so wird daraus

<span class="anker" id="gl-4-13"></span>
$$H_0\,\frac{(p-p_{\mathrm N1})(p-p_{\mathrm N2})}{p-p_{\mathrm P2}}=A_0\,(p-p_{\mathrm P1})+A_1+\frac{A_2\,(p-p_{\mathrm P1})}{p-p_{\mathrm P2}}. \tag{4.13}$$

Der Grenzübergang $p\to p_{\mathrm P1}$ ergibt

<span class="anker" id="gl-4-14"></span>
$$A_1=H_0\,\frac{(p_{\mathrm P1}-p_{\mathrm N1})(p_{\mathrm P1}-p_{\mathrm N2})}{p_{\mathrm P1}-p_{\mathrm P2}}, \tag{4.14}$$

und entsprechend

<span class="anker" id="gl-4-15"></span>
$$A_2=H_0\,\frac{(p_{\mathrm P2}-p_{\mathrm N1})(p_{\mathrm P2}-p_{\mathrm N2})}{p_{\mathrm P2}-p_{\mathrm P1}}. \tag{4.15}$$
::::

⁠**Kurz gesagt:** Die Partialbruchzerlegung schreibt einen Polynombruch als Summe von Brüchen mit je einem Pol. Den Koeffizienten eines Pols erhält man, indem man dessen Faktor herauskürzt und den Pol einsetzt.

:::hintergrund Was die Koeffizienten bedeuten
Jeder Summand $\frac{A_r}{p-p_{\mathrm P,r}}$ ist nach dem Kasten „Suchfilter“ im ersten Abschnitt genau das, was die Transformation aus einem einzelnen Anteil $A_r\,\mathrm{e}^{p_{\mathrm P,r}t}$ macht. Die Partialbruchzerlegung zerlegt die Transformierte also in die Anteile, aus denen das Signal besteht: ein Bruch je Exponentialfunktion. $A_r$ ist die Stärke, mit der dieser Anteil vorkommt. Bei einer Impulsantwort ist das die Anfangsamplitude, mit der der Stoß die Eigenbewegung $\mathrm{e}^{p_{\mathrm P,r}t}$ anregt.

Die Grenzwertformel liest diese Stärke ab. In der Nähe von $p_{\mathrm P,r}$ ist der Summand $\frac{A_r}{p-p_{\mathrm P,r}}$ viel größer als alle anderen, er bildet dort die Spitze der Landschaft. Multipliziert man mit $(p-p_{\mathrm P,r})$, so wird gerade diese Spitze zu der Konstanten $A_r$ abgeflacht, während alle anderen Summanden an der Stelle $p_{\mathrm P,r}$ verschwinden. In der Funktionentheorie heißt $A_r$ das __Residuum__ von $H$ am Pol $p_{\mathrm P,r}$.
:::

### Zurück in den Zeitbereich

<span class="anker" id="stufe-4-6"></span>

Jeder Summand der Zerlegung ist ein Grundpaar. Bei einem kausalen System liegt der Konvergenzbereich rechts aller Pole, also gehört nach [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9) jeder Bruch $\frac{A_r}{p-p_{\mathrm P,r}}$ zu $A_r\,\mathrm{e}^{p_{\mathrm P,r}t}\,\varepsilon(t)$. Der konstante Summand $A_0$ gehört nach [(2.11)](beispiele-zur-laplace-transformation.html#gl-2-11) zu $A_0\,\delta(t)$. Zusammen:

<span class="anker" id="gl-4-16"></span>
$$h(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_{\mathrm P,r}t}\,\varepsilon(t). \tag{4.16}$$

Die Pole sind die Exponenten, die Partialbruchkoeffizienten die Vorfaktoren.

::::beispiel die Sprungantwort des RC-Tiefpasses
Mit $RC=1\,\mathrm{s}$ ist $H(p)=\frac{1}{p+1}$ für $\operatorname{Re} p>-1$, der Eingang $\varepsilon(t)$ hat $S(p)=\frac1p$ für $\operatorname{Re} p>0$. Nach dem Faltungssatz ist der Ausgang im gemeinsamen Bereich $\operatorname{Re} p>0$

$$G(p)=\frac1p\cdot\frac{1}{p+1}.$$

Die Pole sind $0$ und $-1$. Mit [(4.11)](#gl-4-11): $A_1=\lim_{p\to0}\frac{1}{p+1}=1$ und $A_2=\lim_{p\to-1}\frac1p=-1$. Also

$$G(p)=\frac1p-\frac{1}{p+1}\quad\Longrightarrow\quad g(t)=\bigl(1-\mathrm{e}^{-t}\bigr)\,\varepsilon(t).$$

Direkt nachgerechnet: $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ für $t>0$. Zahlen: $g(0{,}5\,\mathrm{s})=0{,}3935$, $g(1\,\mathrm{s})=0{,}6321$, $g(3\,\mathrm{s})=0{,}9502$.
::::

⁠**Kurz gesagt:** Nach der Partialbruchzerlegung liest man das Zeitsignal Summand für Summand aus den Grundpaaren ab: Jeder Pol $p_{\mathrm P,r}$ liefert eine Exponentialfunktion $\mathrm{e}^{p_{\mathrm P,r}t}$.

:::hintergrund Was die Pole des Ausgangs verraten
Im Beispiel hat der Ausgang die Pole $0$ und $-1$:

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{Pol }0\text{ (vom Eingang)}}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{Pol }-1\text{ (vom System)}}\qquad(t>0).$$

Der Pol des Eingangs liefert den Anteil, den der Eingang erzwingt: die Endspannung 1. Der Pol des Systems liefert die *Eigenbewegung* des RC-Glieds, das Abklingen mit $RC=1\,\mathrm{s}$. Das gilt allgemein: Im Ausgang $G=S\,H$ stecken die Pole des Eingangs und die Pole des Systems (sofern sich keiner gegen eine Nullstelle kürzt). Ein Pol mit großem negativem Realteil gibt einen schnell abklingenden Anteil, ein Pol nahe der imaginären Achse einen langsamen.
:::

:::ltspice Die Übertragungsfunktion direkt eingeben
⁠**Zeichnen:** das RC-Glied (`1Meg`, `1u`) von `in` nach `rc`. Daneben eine spannungsgesteuerte Spannungsquelle `e`: Steuereingang an `in` und Masse, Ausgang am Netz `lap`, Wert `Laplace=1/(1+s)`. Diese Quelle ist ein LTI-System, das nur durch $H$ gegeben ist: LTspice berechnet daraus selbst die Impulsantwort und faltet den Eingang mit ihr. LTspice schreibt $s$ statt $p$.

⁠**Quelle und Direktive:** `PULSE(0 1 0 1u 1u 100)`, `.tran 0 5 0 1m`.

⁠**Was du siehst:** `V(rc)` und `V(lap)` liegen übereinander (Abstand unter 0,001), auf 0,3935 bei 0,5 s, 0,6321 bei 1 s und 0,9502 bei 3 s.

⁠**Zu Aufgabe [5](#aufg-5):** Quelle `PWL(0 0 10 10)`, die Rampe $t\,\varepsilon(t)$ bis 10 s, und `.tran 0 10 0 1m`. Vergleiche `V(rc)` mit deinem Ergebnis aus Aufgabe [5](#aufg-5)(b).
:::

### Die Impulsantwort des RLC-Systems

<span class="anker" id="stufe-4-7"></span>

Für das RLC-System [(4.7)](#gl-4-7) mit zwei verschiedenen Polen ist $H_0=1/LC$, und es gibt keine Nullstelle. Mit [(4.11)](#gl-4-11) ist $A_1=\frac{1/LC}{p_{\mathrm P1}-p_{\mathrm P2}}$ und $A_2=-A_1$. Nach [(4.8)](#gl-4-8) ist $p_{\mathrm P1}-p_{\mathrm P2}=2b$, und für reelles $b$ ist $LC\cdot2b=\sqrt{R^2C^2-4LC}$. Damit

<span class="anker" id="gl-4-17"></span>
$$H(p)=\frac{1/LC}{p^2+(R/L)\,p+1/LC}=\frac{\overbrace{1/LC}^{H_0}}{(p-p_{\mathrm P1})(p-p_{\mathrm P2})} =\underbrace{\frac{1}{\sqrt{R^2C^2-4LC}}}_{A_1=-A_2=\frac{1}{LC(p_{\mathrm P1}-p_{\mathrm P2})}}\cdot\Bigl[\frac{1}{p-p_{\mathrm P1}}-\frac{1}{p-p_{\mathrm P2}}\Bigr]. \tag{4.17}$$

Das System ist kausal, also folgt mit [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9)

<span class="anker" id="gl-4-18"></span>
$$h(t)=\frac{1}{\sqrt{R^2C^2-4LC}}\,\bigl[\mathrm{e}^{p_{\mathrm P1}t}-\mathrm{e}^{p_{\mathrm P2}t}\bigr]\cdot\varepsilon(t), \tag{4.18}$$

oder mit den Abkürzungen $a$ und $b$ aus [(4.8)](#gl-4-8), wegen $p_{\mathrm P1,2}=-a\pm b$ und $A_1=\frac{1}{2bLC}$:

<span class="anker" id="gl-4-19"></span>
$$h(t)=\frac{1}{bLC}\,\mathrm{e}^{-at}\Bigl(\frac{\mathrm{e}^{bt}-\mathrm{e}^{-bt}}{2}\Bigr)\cdot\varepsilon(t). \tag{4.19}$$

Die Klammer ist der __Sinus hyperbolicus__, $\sinh x=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}$. Je nachdem, ob $b$ reell, null oder imaginär ist, gibt es drei Fälle. Fall b) ist der Grenzfall zwischen a) und c).

<ol class="al">

<li>

$b$ reell, $\frac{1}{LC}<\frac{R^2}{4L^2}$ (__Kriechfall__): Die Impulsantwort ist eine Differenz zweier abklingender Exponentialfunktionen, ohne Schwingung:

<span class="anker" id="gl-4-20"></span>
$$h(t)=\frac{1}{bLC}\,\mathrm{e}^{-at}\sinh(bt)\cdot\varepsilon(t). \tag{4.20}$$

</li>

<li>

$b=0$, $\frac{1}{LC}=\frac{R^2}{4L^2}$ (__aperiodischer Grenzfall__): Dann steht in [(4.19)](#gl-4-19) ein Ausdruck der Form „$0/0$“. Man bildet den Grenzwert $b\to0$ mit der Regel von l'Hospital, also mit den Ableitungen von Zähler und Nenner nach $b$:

<span class="anker" id="gl-4-21"></span>
$$h(t)=\frac{1}{LC}\,\mathrm{e}^{-at}\,\frac{\frac{\mathrm{d}}{\mathrm{d} b}\sinh(bt)}{\frac{\mathrm{d}}{\mathrm{d} b}(b)}\bigg|_{b=0}\cdot\varepsilon(t)=\frac{1}{LC}\,\mathrm{e}^{-at}\,t\cosh(bt)\Big|_{b=0}\cdot\varepsilon(t)=\frac{1}{LC}\,t\,\mathrm{e}^{-at}\cdot\varepsilon(t). \tag{4.21}$$

Dabei ist $\cosh x=\frac{\mathrm{e}^x+\mathrm{e}^{-x}}{2}$ der Kosinus hyperbolicus mit $\cosh0=1$.

</li>

<li>

$b=\mathrm{j}\beta$ imaginär, $\frac{1}{LC}>\frac{R^2}{4L^2}$, mit $\beta=\sqrt{\frac{1}{LC}-\frac{R^2}{4L^2}}$ (__Schwingfall__): Wegen $\sinh(\mathrm{j}\beta t)=\frac{\mathrm{e}^{\mathrm{j}\beta t}-\mathrm{e}^{-\mathrm{j}\beta t}}{2}=\mathrm{j}\sin(\beta t)$ nach [(1.2)](eigenfunktionen-von-lti-systemen.html#gl-1-2) wird

<span class="anker" id="gl-4-22"></span>
$$h(t)=\frac{1}{\mathrm{j}\beta LC}\,\mathrm{e}^{-at}\,\mathrm{j}\sin(\beta t)\cdot\varepsilon(t)=\frac{1}{\beta LC}\,\mathrm{e}^{-at}\sin(\beta t)\cdot\varepsilon(t). \tag{4.22}$$

</li>

</ol>

Abbildung [8](#abb-8) zeigt alle drei Fälle für $R=4\,\mathrm{\Omega}$ und $L=1\,\mathrm{H}$, also $a=2/\mathrm s$, mit drei verschiedenen Kapazitäten.

:::abbildung et3/k2rlch 8
Impulsantwort des RLC-Systems mit $R=4\,\mathrm{\Omega}$, $L=1\,\mathrm{H}$ ($a=2/\mathrm s$): a) Kriechfall, $\omega_0=\sqrt3/\mathrm s$, $b=1/\mathrm s$; b) aperiodischer Grenzfall, $\omega_0=2/\mathrm s$, $b=0$; c) Schwingfall, $\omega_0=\sqrt{20}/\mathrm s$, $\beta=4/\mathrm s$. Nur im Schwingfall schwingt die Antwort.
:::

⁠**Kurz gesagt:** Je nach Dämpfung kriecht die Impulsantwort des RLC-Systems zurück auf null, erreicht im Grenzfall null gerade ohne Überschwingen, oder schwingt mit der Kreisfrequenz $\beta$ und der Abklingrate $a$ aus.

### Konjugiert komplexe Polpaare

<span class="anker" id="stufe-4-8"></span>

Im Schwingfall sind die beiden Pole zueinander konjugiert komplex. Man kann ein solches Paar bei der Partialbruchzerlegung zusammenhalten und erhält so direkt eine reelle Schwingung. Dazu schreibt man den Pol als $p_\mathrm P=-\gamma-\mathrm{j}\omega_1$ mit einer reellen __Abklingrate__ $\gamma$ und einer reellen Kreisfrequenz $\omega_1$:

<span class="anker" id="gl-4-23"></span>
$$H(p)=\frac{A_1}{p-p_\mathrm P}+\frac{A_2}{p-p_\mathrm P^*}\qquad\text{mit}\quad p_\mathrm P=-\gamma-\mathrm{j}\omega_1 . \tag{4.23}$$

Über den gemeinsamen Nenner $(p-p_\mathrm P)(p-p_\mathrm P^*)=(p+\gamma+\mathrm{j}\omega_1)(p+\gamma-\mathrm{j}\omega_1)=(p+\gamma)^2+\omega_1^2$ wird daraus

<span class="anker" id="gl-4-24"></span>
$$H(p)=\frac{A_1\,(p+\gamma-\mathrm{j}\omega_1)+A_2\,(p+\gamma+\mathrm{j}\omega_1)}{(p+\gamma)^2+\omega_1^2}. \tag{4.24}$$

Zwei Fälle mit rechtsseitigen Zeitfunktionen sind besonders wichtig:

<ul>

<li>

$A_1=A_2=\frac12$: Der Zähler wird $p+\gamma$, und

<span class="anker" id="gl-4-25"></span>
$$\begin{aligned} H(p)&=\frac{p+\gamma}{(p+\gamma)^2+\omega_1^2},\qquad h(t)=\tfrac12\Bigl(\mathrm{e}^{(-\gamma-\mathrm{j}\omega_1)t}+\mathrm{e}^{(-\gamma+\mathrm{j}\omega_1)t}\Bigr)\cdot\varepsilon(t)=\mathrm{e}^{-\gamma t}\cos(\omega_1t)\cdot\varepsilon(t)\\ &\Longrightarrow\quad\mathcal{L}\bigl\{\mathrm{e}^{-\gamma t}\cos(\omega_1t)\cdot\varepsilon(t)\bigr\}=\frac{p+\gamma}{(p+\gamma)^2+\omega_1^2}. \end{aligned} \tag{4.25}$$

</li>

<li>

$A_1=-A_2=\frac12$: Der Zähler wird $\tfrac12(p+\gamma-\mathrm{j}\omega_1)-\tfrac12(p+\gamma+\mathrm{j}\omega_1)=-\mathrm{j}\omega_1$, und

<span class="anker" id="gl-4-26"></span>
$$\begin{aligned} H(p)&=\frac{-\mathrm{j}\omega_1}{(p+\gamma)^2+\omega_1^2},\qquad h(t)=\tfrac12\Bigl(\mathrm{e}^{(-\gamma-\mathrm{j}\omega_1)t}-\mathrm{e}^{(-\gamma+\mathrm{j}\omega_1)t}\Bigr)\cdot\varepsilon(t)=-\mathrm{j}\,\mathrm{e}^{-\gamma t}\sin(\omega_1t)\cdot\varepsilon(t)\\ &\Longrightarrow\quad\mathcal{L}\bigl\{\mathrm{e}^{-\gamma t}\sin(\omega_1t)\cdot\varepsilon(t)\bigr\}=\frac{\omega_1}{(p+\gamma)^2+\omega_1^2}. \end{aligned} \tag{4.26}$$

</li>

</ul>

Beide Paare gelten für $\operatorname{Re} p>-\gamma$. Im zweiten Fall teilt man am Schluss beide Seiten durch $-\mathrm{j}$. Beim RLC-System im Schwingfall ist $\gamma=a$ und $\omega_1=\beta$; die Kreisfrequenz $\omega_1$ der Schwingung ist nicht dasselbe wie die Kennkreisfrequenz $\omega_0$.

⁠**Kurz gesagt:** Ein konjugiert komplexes Polpaar bei $-\gamma\pm\mathrm{j}\omega_1$ gehört zu einer Schwingung mit der Kreisfrequenz $\omega_1$, die mit $\mathrm{e}^{-\gamma t}$ abklingt.

### Mehrfache Pole

<span class="anker" id="stufe-4-9"></span>

Fallen $k$ Pole an derselben Stelle zusammen, spricht man von einem __Pol des Grades__ $k$. Im Pol-Nullstellen-Diagramm schreibt man den Grad in Klammern neben das Kreuz, also „$(k)$“. Hat der Pol $p_{\mathrm P,i}$ den Grad $k$, ändert sich die Zerlegung [(4.10)](#gl-4-10): Zu diesem Pol gehören $k$ Summanden mit den Potenzen $1$ bis $k$ im Nenner,

<span class="anker" id="gl-4-27"></span>
$$\begin{aligned} H(p)&=H_0\,\frac{(p-p_{\mathrm N1})(p-p_{\mathrm N2})\cdots(p-p_{\mathrm NQ})}{(p-p_{\mathrm P1})\cdots(p-p_{\mathrm P,i})^k\cdots(p-p_{\mathrm P,R-k+1})}\\ &=A_0+\frac{A_1}{p-p_{\mathrm P1}}+\ldots+\sum_{j=1}^{k}\frac{A_{i,j}}{(p-p_{\mathrm P,i})^j}+\ldots+\frac{A_{R-k+1}}{p-p_{\mathrm P,R-k+1}} . \end{aligned} \tag{4.27}$$

Insgesamt gibt es jetzt $R-k+1$ verschiedene Pole. Die $k$ Koeffizienten des mehrfachen Pols bestimmt man zum Beispiel mit

<span class="anker" id="gl-4-28"></span>
$$A_{i,j}=\frac{1}{(k-j)!}\,\lim_{p\to p_{\mathrm P,i}}\frac{\mathrm{d}^{\,k-j}}{\mathrm{d} p^{\,k-j}}\Bigl[H(p)\,(p-p_{\mathrm P,i})^k\Bigr]. \tag{4.28}$$

Für $j=k$ ist das dieselbe Regel wie bei einfachen Polen: Faktor herauskürzen, Pol einsetzen. Für kleinere $j$ leitet man vorher ab.

Für die Rücktransformation braucht man das Paar

<span class="anker" id="gl-4-29"></span>
$$\frac{t^{\,j-1}}{(j-1)!}\,\mathrm{e}^{p_0t}\,\varepsilon(t)\quad\longleftrightarrow\quad\frac{1}{(p-p_0)^j},\qquad\operatorname{Re} p>\operatorname{Re} p_0 . \tag{4.29}$$

:::herleitung Paar für mehrfache Pole
Mit $n=j-1$ ist zu zeigen: $\int_0^\infty t^n\,\mathrm{e}^{-(p-p_0)t}\,\mathrm{d} t=\frac{n!}{(p-p_0)^{n+1}}$. Für $n=0$ ist das das Grundpaar [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9). Partielle Integration mit $c=p-p_0$, $\operatorname{Re} c>0$:

$$\int_0^\infty t^n\,\mathrm{e}^{-ct}\,\mathrm{d} t=\Bigl[-\frac{t^n\,\mathrm{e}^{-ct}}{c}\Bigr]_0^\infty+\frac nc\int_0^\infty t^{n-1}\,\mathrm{e}^{-ct}\,\mathrm{d} t=\frac nc\int_0^\infty t^{n-1}\,\mathrm{e}^{-ct}\,\mathrm{d} t,$$

denn der Randterm verschwindet an beiden Grenzen. Jeder Schritt senkt die Potenz um eins und liefert einen Faktor $\frac{n}{c}$, $\frac{n-1}{c}$, …. Nach $n$ Schritten bleibt $\frac{n!}{c^n}\cdot\frac1c=\frac{n!}{c^{n+1}}$.
:::

::::beispiel der aperiodische Grenzfall
Für $b=0$ hat das RLC-System einen doppelten Pol bei $-a$: $H(p)=\frac{1/LC}{(p+a)^2}$. Mit $k=2$ ist $H(p)(p+a)^2=\frac{1}{LC}$ konstant. Also ist $A_{1,2}=\frac{1}{LC}$ und $A_{1,1}=\frac{\mathrm{d}}{\mathrm{d} p}\frac{1}{LC}=0$. Mit [(4.29)](#gl-4-29) für $j=2$ folgt $h(t)=\frac{1}{LC}\,t\,\mathrm{e}^{-at}\,\varepsilon(t)$, genau das Ergebnis [(4.21)](#gl-4-21) aus der Regel von l'Hospital.
::::

⁠**Kurz gesagt:** Ein Pol des Grades $k$ liefert $k$ Summanden. Im Zeitbereich erscheint dabei die Exponentialfunktion des Pols, multipliziert mit Potenzen von $t$ bis $t^{k-1}$.

:::hintergrund Woher der Faktor $t$ bei einem doppelten Pol kommt
Ein doppelter Pol entsteht, wenn zwei einfache Pole zusammenrücken. Solange sie getrennt sind, enthält die Antwort nach [(4.18)](#gl-4-18) die Differenz zweier Eigenbewegungen, geteilt durch den Abstand der Pole:

$$\frac{\mathrm{e}^{p_{\mathrm P1}t}-\mathrm{e}^{p_{\mathrm P2}t}}{p_{\mathrm P1}-p_{\mathrm P2}} .$$

Rücken die Pole zusammen, wird daraus ein Differenzenquotient und im Grenzfall die Ableitung nach dem Exponenten:

$$\frac{\mathrm{d}}{\mathrm{d} p}\,\mathrm{e}^{pt}=t\,\mathrm{e}^{pt}.$$

Der Faktor $t$ ist also die Spur zweier Eigenbewegungen, die gleich geworden sind. Er lässt die Antwort zunächst linear anwachsen. Bei einem Pol links der imaginären Achse gewinnt danach die abklingende Exponentialfunktion, weil sie schneller fällt, als $t$ wächst.
:::

:::aufgabe Aufgabe 5 ★★ Rampenantwort des RC-Tiefpasses
<span class="anker" id="aufg-5"></span>

Eingang $s(t)=t\,\varepsilon(t)$ mit $S(p)=1/p^2$ für $\operatorname{Re} p>0$, Grundpaar [(2.12)](beispiele-zur-laplace-transformation.html#gl-2-12). System: RC-Tiefpass mit $RC=1\,\mathrm{s}$.

<ol class="al">

<li>

Bestimme $G(p)$ und seinen Konvergenzbereich.

</li>

<li>

Prüfe die Zerlegung $G(p)=\frac{1}{p^2}-\frac1p+\frac{1}{p+1}$ und bestimme $g(t)$.

</li>

<li>

Kontrolle: Was ist $g(0)$, und warum muss das so sein? Was ist $\dot g(t)$?

</li>

<li>

Wie verhält sich $g(t)$ für $t\gg1$ s? Vergleiche mit Aufgabe [1](eigenfunktionen-von-lti-systemen.html#aufg-1)(b).

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$ für $\operatorname{Re} p>0$ (Durchschnitt aus $\operatorname{Re} p>0$ und $\operatorname{Re} p>-1$).

(b) Auf den Hauptnenner: $\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$. Rücktransformation mit [(2.12)](beispiele-zur-laplace-transformation.html#gl-2-12) und [(2.9)](beispiele-zur-laplace-transformation.html#gl-2-9):

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(Die Zerlegung folgt auch aus [(4.28)](#gl-4-28): Der doppelte Pol bei $0$ hat $A_{1,2}=\lim_{p\to0}\frac{1}{p+1}=1$ und $A_{1,1}=\lim_{p\to0}\frac{\mathrm{d}}{\mathrm{d} p}\frac{1}{p+1}=-1$, der Pol bei $-1$ hat $A_2=\lim_{p\to-1}\frac{1}{p^2}=1$.)

(c) $g(0)=0-1+1=0$: Die Kondensatorspannung kann nicht springen, und der Eingang startet bei null. $\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$, genau die Sprungantwort. Das passt: Die Rampe ist das Integral des Sprungs, also ist die Rampenantwort das Integral der Sprungantwort.

(d) Für $t\gg1$ s ist $\mathrm{e}^{-t}\approx0$ und $g(t)\approx t-1$: Der Ausgang folgt der Rampe mit einer Verzögerung von $RC=1$ s, genau wie bei der zweiseitigen Rampe in Aufgabe [1](eigenfunktionen-von-lti-systemen.html#aufg-1)(b). Der Unterschied ist der Summand $\mathrm{e}^{-t}$ (Pol $-1$ des Systems): der Einschwingvorgang, weil die Rampe hier erst bei $t=0$ beginnt.
:::
:::

:::aufgabe Aufgabe 6 ★★ Ein RLC-System
<span class="anker" id="aufg-6"></span>

RLC-System nach Abb. [6](#abb-6) mit $R=2\,\mathrm{\Omega}$, $L=1\,\mathrm{H}$ und $C=0{,}25\,\mathrm{F}$.

<ol class="al">

<li>

Bestimme $H(p)$, $\omega_0$, $\xi$ und die Pole. Welcher der drei Fälle liegt vor?

</li>

<li>

Bestimme $h(t)$, einmal mit der passenden Formel [(4.20)](#gl-4-20), [(4.21)](#gl-4-21) oder [(4.22)](#gl-4-22) und einmal mit dem Paar [(4.26)](#gl-4-26).

</li>

<li>

Welcher Widerstand führt bei gleichem $L$ und $C$ zum aperiodischen Grenzfall?

</li>

</ol>

:::loesung
(a) Mit [(4.7)](#gl-4-7): $H(p)=\frac{1}{0{,}25\,p^2+0{,}5\,p+1}=\frac{4}{p^2+2p+4}$ ($p$ in $1/\mathrm s$). Kennkreisfrequenz $\omega_0=1/\sqrt{LC}=1/\sqrt{0{,}25\,\mathrm{s^2}}=2/\mathrm s$, Dämpfungsgrad $\xi=\frac R2\sqrt{\frac CL}=1\cdot0{,}5=0{,}5$. Mit $a=R/2L=1/\mathrm s$ und $b=\sqrt{1-4}/\mathrm s=\mathrm{j}\sqrt3/\mathrm s$ liegen die Pole bei $p_{\mathrm P1,2}=-1\pm\mathrm{j}\sqrt3\approx-1\pm1{,}732\,\mathrm{j}$. Wegen $\xi<1$ ist es der Schwingfall.

(b) Mit [(4.22)](#gl-4-22) und $\beta=\sqrt3/\mathrm s$:

$$h(t)=\frac{1}{\beta LC}\,\mathrm{e}^{-at}\sin(\beta t)\,\varepsilon(t)=\frac{1}{\sqrt3\cdot0{,}25}\,\mathrm{e}^{-t}\sin(\sqrt3\,t)\,\varepsilon(t)=\frac{4}{\sqrt3}\,\mathrm{e}^{-t}\sin(\sqrt3\,t)\,\varepsilon(t)$$

in $1/\mathrm s$, also etwa $2{,}31\,\mathrm{e}^{-t}\sin(1{,}732\,t)$. Mit dem Paar [(4.26)](#gl-4-26): $p^2+2p+4=(p+1)^2+3$, also $H(p)=\frac{4}{\sqrt3}\cdot\frac{\sqrt3}{(p+1)^2+(\sqrt3)^2}$ mit $\gamma=1$ und $\omega_1=\sqrt3$. Das gibt dasselbe $h(t)$.

(c) Aperiodischer Grenzfall bei $\frac{R^2}{4L^2}=\frac{1}{LC}$, also $R=2\sqrt{L/C}=2\sqrt{4}\,\mathrm{\Omega}=4\,\mathrm{\Omega}$. Das entspricht $\xi=1$.
:::
:::
