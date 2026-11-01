---
title: Signale, LTI-Systeme und die Faltung
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / LTI-Systeme und Faltung
order: 3210100
summary: Warum die Antwort auf einen einzigen Stoß das ganze System beschreibt
tags: Signal, normiert, Periodendauer, Frequenz, System, Transformation, linear, zeitinvariant
lang: de
---

## Worum es geht

Ein System nimmt ein Signal auf und gibt ein anderes ab: Ein RC-Glied glättet eine Spannung, ein Lautsprechergehäuse färbt einen Klang, ein Messverstärker verzögert und verstärkt. Die Frage dieses Artikels lautet: *Was muss man über ein System wissen, um für jedes beliebige Eingangssignal den Ausgang ausrechnen zu können?*

Für die große Klasse der linearen, zeitinvarianten Systeme (LTI-Systeme) ist die Antwort überraschend knapp: die Antwort auf einen einzigen, unendlich kurzen Stoß. Das Werkzeug, das aus dieser einen Antwort jede andere macht, ist die Faltung.

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Jedes Signal ist eine Überlagerung unendlich vieler kurzer Stöße: an jeder Stelle $\tau$ ein Stoß mit dem Gewicht $s(\tau)\,\mathrm{d}\tau$.

</li>

<li>

Ein LTI-System antwortet auf einen verschobenen Stoß mit der verschobenen Impulsantwort $h(t-\tau)$ (Zeitinvarianz) und auf eine Summe von Stößen mit der Summe der Antworten (Linearität).

</li>

<li>

Deshalb ist der Ausgang die Faltung $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$, und $h(t)$ beschreibt das System vollständig.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Die Tabelle ordnet die Ergebnisse dieses Artikels dem Prinzip „zerlegen, Baustein durchschicken, zusammensetzen“ zu.

| Ergebnis | Woher es kommt |
|---|---|
| Faltungsintegral | Stöße überlagern, verschobene Impulsantworten überlagern (Stufe [4](#stufe-4)) |
| Spiegeln beim Ausrechnen | $h(t-\tau)$ ist die Antwort auf einen Stoß, der vor $t-\tau$ Sekunden kam (Stufe [5](#stufe-5)) |
| $\delta$ ist das Einselement | ein Signal aus Stößen, durch ein System, das jeden Stoß unverändert lässt (Stufe [6](#stufe-6)) |
| Kommutativ-, Assoziativ-, Distributivgesetz | Rollen tauschen, Systeme in Kette, Systeme parallel (Stufe [6](#stufe-6)) |
| Siebeigenschaft, Dehnung des Dirac-Impulses | $\delta$ ist nur über seine Fläche definiert (Stufe [7](#stufe-7)) |
| Sprungantwort = Integral der Impulsantwort | ein Sprung ist die Summe aller Stöße bis $t$ (Stufe [8](#stufe-8)) |
| Kausalität, Stabilität | Bedingungen an $h(t)$: null vor dem Stoß, endliche Fläche von $\vert h\vert $ (Stufe [9](#stufe-9)) |
| Faltung ohne System | dieselbe Überlagerung, zum Beispiel bei der Augensumme zweier Würfel (Stufe [10](#stufe-10)) |

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für diesen Artikel
<ul>

<li>

⁠**RC-Tiefpass** mit $T=RC=1$ s (zum Beispiel $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Zeiten in s, Spannungen in V, also dimensionslos gerechnet.

</li>

<li>

⁠**Rechteckimpuls** der Höhe $a=1$ V und Dauer $T_0=1$ s, beginnend bei $t=0$.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap1.py` nach.
:::

## Stufe 1: Signale beschreiben

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man Systeme untersucht, braucht man eine Sprache für Signale: einige Grundformen und zwei Operationen auf der Zeitachse, Verschieben und Dehnen.
:::

Ein __Signal__ ist der Verlauf einer physikalischen Größe über der Zeit, geschrieben als Funktion $s(t)$. In der Systemtheorie rechnet man meist __normiert__: Zeiten in Vielfachen von 1 s, Spannungen in Vielfachen von 1 V. Dann werden Größengleichungen zu Zahlenwertgleichungen, und $\mathrm{e}^{-t}$ ist ohne Einheitenproblem hinschreibbar.

**Elementarsignale.** Einige Signale lassen sich durch einen einfachen Ausdruck beschreiben und kommen immer wieder vor (Abb. [1](#abb-1)):

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{(Gauß)},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

Sprung $\varepsilon(t)$ und Rechteck $\operatorname{rect}(t)$ springen. Welcher Wert genau an der Sprungstelle gilt, ist Vereinbarungssache. Oft wählt man dort $\tfrac12$: Dann ergeben aneinandergesetzte Rechtecke überall genau 1.

:::abbildung et3/k1elementar
Elementarsignale. Unten rechts ein verschobenes und gedehntes Rechteck: Mitte bei $t_0=2$, Breite $T=2$, Höhe $a=0{,}8$.
:::

**Verschieben und Dehnen.** Aus einem Signal entstehen neue, wenn man die Zeitachse umrechnet:

<ul>

<li>

⁠**Verschieben:** $t\to t-t_0$. Für $t_0>0$ wird das Signal um $t_0$ *verzögert*, also nach rechts geschoben.

</li>

<li>

⁠**Dehnen:** $t\to t/T$. Für $|T|>1$ wird das Signal breiter, für $0<|T|<1$ schmaler, für $T<0$ zusätzlich gespiegelt.

</li>

</ul>

Beides zusammen, dazu eine Amplitude $a$, ergibt zum Beispiel den Rechteckimpuls

<span class="anker" id="gl-1-1"></span>
$$s(t)=a\operatorname{rect}\Bigl(\frac{t-t_0}{T}\Bigr)=\begin{cases}a & |t-t_0|\le |T|/2\\ 0 & \text{sonst}\end{cases} \tag{1.1}$$

mit der Mitte $t_0$, der Dauer $|T|$ und der Höhe $a$. Man prüft es, indem man das Argument $(t-t_0)/T$ in die Definition von $\operatorname{rect}$ einsetzt. Ebenso ist $\sin(2\pi t/T)=\sin(2\pi Ft)$ der gedehnte Sinus mit der __Periodendauer__ $T$ und der __Frequenz__ $F=1/T$.

:::frage Warum verschiebt $t-t_0$ das Signal nach rechts, obwohl man etwas abzieht?
Das neue Signal zeigt zur Zeit $t$ den Wert, den das alte zur Zeit $t-t_0$ hatte, also *früher*. Alles, was das alte Signal tat, tut das neue $t_0$ später. Am einfachsten prüft man es an einer markanten Stelle: Die Kante von $\varepsilon(t-t_0)$ liegt dort, wo das Argument null wird, bei $t=t_0$.
:::

**Die komplexe Exponentialfunktion.** Für die Systemtheorie am wichtigsten ist

$$\mathrm{e}^{\mathrm{j}2\pi Ft}=\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft).$$

Aus einem konjugiert komplexen Paar entstehen nach Euler die reellen Schwingungen:

$$\cos(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2},\qquad \sin(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}-\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2\mathrm{j}}.$$

Eine Verzögerung um $t_0$ erscheint bei einer Schwingung als Phasenverschiebung:

<span class="anker" id="gl-1-2"></span>
$$\cos\bigl(2\pi F(t-t_0)\bigr)=\cos(2\pi Ft+\varphi)=\operatorname{Re}\bigl\{\mathrm{e}^{\mathrm{j}2\pi Ft}\,\mathrm{e}^{\mathrm{j}\varphi}\bigr\},\qquad\varphi=-2\pi Ft_0. \tag{1.2}$$

⁠**Kurz gesagt:** Bei einer Schwingung ist Verzögern dasselbe wie Phasedrehen, und bei $\mathrm{e}^{\mathrm{j}2\pi Ft}$ ist es sogar dasselbe wie Multiplizieren mit der Zahl $\mathrm{e}^{\mathrm{j}\varphi}$. Diese Eigenschaft trägt in [Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) die ganze Laplace-Transformation.

:::aufgabe Aufgabe 1 ★ Verschieben, dehnen, Phase
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Wo beginnt und endet $s(t)=2\operatorname{rect}\bigl(\frac{t-3}{4}\bigr)$, und wie hoch ist der Impuls?

</li>

<li>

Schreibe einen Rechteckimpuls, der von $t=1$ s bis $t=4$ s die Höhe 0,5 V hat.

</li>

<li>

Skizziere $s(-t)$ für $s(t)=\varepsilon(t-1)$. Wo liegt die Kante?

</li>

<li>

Ein Kosinus mit $F=50$ Hz wird um $t_0=5$ ms verzögert. Welche Phase $\varphi$ hat er danach?

</li>

</ol>

:::loesung
(a) Mitte $t_0=3$, Dauer $T=4$: von $t=1$ bis $t=5$, Höhe 2.

(b) Mitte 2,5 s, Dauer 3 s: $s(t)=0{,}5\operatorname{rect}\bigl(\frac{t-2{,}5}{3}\bigr)$.

(c) $s(-t)=\varepsilon(-t-1)$. Die Kante liegt dort, wo das Argument null wird: $-t-1=0$, also $t=-1$. Der Wert ist 1, wo das Argument $\ge0$ ist, also für $t\le-1$. Ein gespiegelter Sprung: 1 links von $-1$, 0 rechts davon.

(d) $\varphi=-2\pi Ft_0=-2\pi\cdot50\,\mathrm{Hz}\cdot5\,\mathrm{ms}=-\pi/2=-90^\circ$. Eine Viertelperiode Verzögerung ist eine Viertelumdrehung.
:::
:::

## Stufe 2: Ein erstes System, das RC-Glied

<span class="anker" id="stufe-2"></span>

:::zweck
Am RC-Tiefpass (Abb. [2](#abb-2)) zeigen sich alle Ideen dieses Artikels schon im Kleinen: Eine komplexe Exponentialfunktion kommt nur mit einer Zahl multipliziert heraus, und auf einen Sprung antwortet die Schaltung mit einer Exponentialkurve.
:::

**Die Differentialgleichung.** Der Strom durch $R$ ist $(u_1-u_2)/R$. Er fließt vollständig in den Kondensator und lädt ihn, $C\,\dot u_2=(u_1-u_2)/R$. Umgestellt:

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung
RC-Tiefpass: Eingang $u_1$, Ausgang $u_2$ am Kondensator. Im Rechenmodell ist $RC=1$ s.
:::

**Eingang $\mathrm{e}^{\mathrm{j}2\pi Ft}$: der Ausgang ist eine Zahl mal der Eingang.** Legt man $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$ an, hat der Ausgang im eingeschwungenen Zustand dieselbe Form, nur mit anderer Amplitude und Phase: $u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Der Grund ist, dass Ableiten die Form nicht ändert, $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$. Eingesetzt in [(2.1)](#gl-2-1):

$$H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}\quad\Longrightarrow\quad H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

Dasselbe liefert die Wechselstromrechnung mit Zeigern: Der Kondensator hat die Impedanz $1/(\mathrm{j}2\pi FC)$, und die Schaltung ist ein Spannungsteiler,

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1.$$

Die reelle Spannung zu einem Zeiger ist $u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$ (Effektivwertzeiger).

:::satz Satz 2.1 (Übertragungsfunktion des RC-Tiefpasses)
<span class="anker" id="satz-2-1"></span>

Mit $x=2\pi FRC$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} \operatorname{Re}\{H\}&=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2},\\ |H(F)|&=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x. \end{aligned} \tag{2.2|2.3}$$
:::

⁠**So liest man das:** $|H|$ sagt, um welchen Faktor die Amplitude schrumpft, $\varphi$, um welchen Winkel die Schwingung nacheilt. Bei $x=1$, also $F=1/(2\pi RC)=0{,}16$ Hz im Rechenmodell, ist $|H|=0{,}707$ und $\varphi=-45^\circ$. Bei $x=10$ ist $|H|=0{,}0995$ und $\varphi=-84{,}3^\circ$ (Abb. [3](#abb-3)). **Grenzfälle:** $F\to0$ ergibt $H\to1$ (der Kondensator hat Zeit, sich voll aufzuladen), $F\to\infty$ ergibt $H\to0$ mit $\varphi\to-90^\circ$ (der Kondensator wirkt wie ein Kurzschluss).

:::abbildung et3/k1bode
Betrag und Phase der Übertragungsfunktion des RC-Tiefpasses über $x=2\pi FRC$ (logarithmisch). Langsame Schwingungen kommen fast unverändert durch, schnelle werden geschwächt und eilen bis zu $90^\circ$ nach.
:::

**Die Phase allgemein.** Für eine beliebige komplexe Zahl $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$ gilt

<span class="anker" id="gl-2-4"></span>
$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases},\quad l\ \text{ganzzahlig}, \tag{2.4}$$

wobei $\arctan$ den Hauptwert in $[-\pi/2,\pi/2]$ liefert.

:::frage Warum braucht die Phasenformel den Zusatz $\lambda\pi$?
$\arctan$ sieht nur das Verhältnis $\operatorname{Im}/\operatorname{Re}$. Die Zahlen $1+\mathrm{j}$ und $-1-\mathrm{j}$ haben dasselbe Verhältnis 1, liegen aber in entgegengesetzten Quadranten. $\arctan1=45^\circ$ stimmt für $1+\mathrm{j}$. Für $-1-\mathrm{j}$ ist der wahre Winkel $45^\circ+180^\circ=225^\circ$, gleichwertig $-135^\circ$ (mit $l=-1$). Immer wenn der Realteil negativ ist, muss man $\pi$ addieren.
:::

**Eingang Sprung: die Exponentialkurve.** Bei $t=0$ wird $u_1=1$ V angelegt, der Kondensator ist leer. Für $t\ge0$ liefert die Maschenregel mit dem Strom $i$

$$1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau.$$

Ableiten gibt $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$, also $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, und Integrieren

$$\ln|i|=-\frac{t}{RC}+K\quad\Longrightarrow\quad i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R,$$

denn im ersten Moment liegt die ganze Spannung an $R$. Mit der Maschenregel $u_2=1-R\,i$ folgt

<span class="anker" id="gl-2-5"></span>
$$u_2(t)=1-\mathrm{e}^{-t/RC}\qquad(t\ge0). \tag{2.5}$$

Der Mechanismus: Je voller der Kondensator, desto weniger Spannung bleibt für $R$, desto kleiner der Ladestrom, desto langsamer füllt er sich weiter. Diese Rückwirkung macht die Kurve exponentiell.

:::ltspice RC-Tiefpass: Sprungantwort und Frequenzgang
⁠**Zeichnen:** Quelle `voltage` am Netz `in`, `res` mit `1Meg` von `in` nach `out`, `cap` mit `1u` von `out` nach Masse, also $RC=1$ s. Vorsicht: SPICE liest `1M` als 1 Milli, Mega heißt `Meg`.

⁠**Sprung:** Quelle `PULSE(0 1 0 1u 1u 100)`, Direktive `.tran 5`. Genaue Werte liefert eine Messung wie `.meas tran g1 FIND V(out) AT=1`, das Ergebnis steht im SPICE Error Log (View, SPICE Error Log). Erwartet: 0,393 bei 0,5 s, 0,632 bei 1 s und 0,950 bei 3 s, also $1-\mathrm{e}^{-t}$ wie in [(2.5)](#gl-2-5).

⁠**Frequenzgang:** Quellwert `AC 1`, statt `.tran` die Direktive `.ac dec 100 0.01 100`. LTspice zeichnet den Betrag in dB (durchgezogen) und die Phase (gestrichelt). Bei 0,159 Hz ($x=1$) stehen dort $-3{,}0$ dB, also $|H|=0{,}707$, und $-45^\circ$. Vergleiche die Werte bei $x=10$ mit deinem Ergebnis aus Aufgabe [2](#aufg-2)(a).
:::

:::aufgabe Aufgabe 2 ★★ Frequenzgang und Phase
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Berechne $|H|$ und $\varphi$ des RC-Tiefpasses für $x=0$, $1$ und $10$. Bei welcher Frequenz in Hz liegt $x=10$ im Rechenmodell?

</li>

<li>

Ein Signal $u_1(t)=\cos(2\pi Ft)$ mit $x=1$ liegt an. Schreibe $u_2(t)$ hin. Um wie viel Sekunden eilt $u_2$ nach, wenn $RC=1$ s?

</li>

<li>

Bestimme mit [(2.4)](#gl-2-4) die Phasen von $-1-\mathrm{j}$, $-\mathrm{j}$ und $-2$.

</li>

</ol>

:::loesung
(a) $x=0$: $|H|=1$, $\varphi=0$. $x=1$: $|H|=0{,}707$, $\varphi=-45^\circ$. $x=10$: $|H|=0{,}0995$, $\varphi=-84{,}3^\circ$. $x=10$ bedeutet $F=10/(2\pi RC)=1{,}59$ Hz.

(b) $u_2(t)=0{,}707\cos(2\pi Ft-45^\circ)$ mit $2\pi F=1/\mathrm s$, also $F=0{,}159$ Hz. Nacheilen um $t_0=-\varphi/(2\pi F)=(\pi/4)/(1/\mathrm s)=0{,}785$ s.

(c) $-1-\mathrm{j}$: $\arctan1=45^\circ$, Realteil negativ, also $+180^\circ$: $225^\circ$, gleichwertig $-135^\circ$. $-\mathrm{j}$: Realteil null, Imaginärteil negativ; $\arctan(\operatorname{Im}/\operatorname{Re})$ strebt gegen $-90^\circ$, die Phase ist $-90^\circ$. $-2$: $\arctan0=0$, Realteil negativ, also $180^\circ$.
:::
:::

## Stufe 3: Was ein LTI-System ist

<span class="anker" id="stufe-3"></span>

:::zweck
Das RC-Glied hat zwei Eigenschaften, auf denen alles Weitere beruht: Es ist linear und zeitinvariant. Diese Stufe definiert beide und zeigt, was sie erlauben.
:::

Ein __System__ ordnet einem Eingangssignal ein Ausgangssignal zu:

$$g(t)=\operatorname{Tr}\{s(t)\}.$$

Eine solche Zuordnung von Funktionen zu Funktionen heißt __Transformation__. Sie bildet nicht einen Zahlenwert auf einen anderen ab: Der Ausgang zur Zeit $t$ darf vom ganzen bisherigen Verlauf des Eingangs abhängen. Beim RC-Glied hängt $u_2(t)$ davon ab, wie viel Ladung sich bis $t$ angesammelt hat.

:::definition Definition 3.1 (LTI-System)
<span class="anker" id="satz-3-1"></span>

Ein System heißt

<ul>

<li>

__linear__, wenn für beliebige Konstanten $a_i$ der Überlagerungssatz gilt:

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t); \tag{3.1}$$

</li>

<li>

__zeitinvariant__, wenn für jede Verschiebung $t_0$ gilt:

<span class="anker" id="gl-3-2"></span>
$$\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0). \tag{3.2}$$

</li>

</ul>

Ein lineares, zeitinvariantes System heißt kurz __LTI-System__ (englisch linear time-invariant).
:::

Beim RC-Glied kommt die Linearität daher, dass in der Differentialgleichung [(2.1)](#gl-2-1) weder Produkte noch Quadrate von $u_1$ und $u_2$ stehen. Die Zeitinvarianz kommt daher, dass sich $R$ und $C$ nicht mit der Zeit ändern. Alle Netzwerke aus $R$, $L$ und $C$ werden durch lineare Differentialgleichungen mit konstanten Koeffizienten beschrieben. Das gilt aber nicht für jedes LTI-System: Das ideale Laufzeitglied aus Stufe [7](#stufe-7) etwa hat keine solche Gleichung.

**Was die beiden Eigenschaften erlauben.** Kennt man die Antwort $g_0$ auf einen Rechteckimpuls $s_0$, kennt man ohne weitere Rechnung die Antwort auf jede Summe verschobener und skalierter Rechteckimpulse. Abbildung [4](#abb-4) zeigt das für $s(t)=s_0(t)+0{,}5\,s_0(t-2)$: Der Ausgang ist $g_0(t)+0{,}5\,g_0(t-2)$.

:::abbildung et3/k1doppel
Links: Rechteck $s_0$ (Höhe 1 V, Dauer 1 s) und die Antwort $g_0$ des RC-Glieds. Rechts: Doppelimpuls. Die Antwort (rot) ist die Summe aus $g_0(t)$ und der verschobenen, halbierten Kopie $0{,}5\,g_0(t-2)$ (gestrichelt).
:::

:::frage Ist $g(t)=2s(t)+1$ linear? Die Kennlinie ist doch eine Gerade.
Nein. Für ein lineares System muss der Eingang null den Ausgang null ergeben: Setzt man in [(3.1)](#gl-3-1) alle $a_i=0$, folgt $\operatorname{Tr}\{0\}=0$. Hier ist $\operatorname{Tr}\{0\}=1$. Auch der Überlagerungssatz scheitert: Zwei Eingänge einzeln ergeben zusammen $2s_1+2s_2+2$, gemeinsam aber $2s_1+2s_2+1$. Eine Gerade, die nicht durch den Ursprung geht, heißt *affin*, nicht linear.
:::

:::ltspice Überlagerung prüfen: zwei Rechtecke
⁠**Zeichnen:** das RC-Glied aus Stufe [2](#stufe-2), aber mit zwei Quellen `voltage` in Reihe: `V1` mit dem Minuspol an Masse und dem Pluspol am Netz `a`, Wert `PULSE(0 {a1} 0 1u 1u 1)`, darauf `V2` von `a` nach `in`, Wert `PULSE(0 {a2} 2 1u 1u 1)`. In Reihe addieren sich die Spannungen, am RC-Glied liegt also $a_1s_0(t)+a_2s_0(t-2)$.

⁠**Direktiven:** `.param a1=1 a2=0.5`, `.step param a1 list 0 1`, `.step param a2 list 0 0.5`, `.tran 0 6 0 1m`. LTspice rechnet alle vier Kombinationen und zeichnet sie übereinander.

⁠**Was du siehst:** die Kurven $0$, $g_0(t)$, $0{,}5\,g_0(t-2)$ und ihre Summe wie in Abb. [4](#abb-4). Bei $t=2{,}5$ s ist $0{,}141+0{,}197=0{,}338$. Die Summe der Eingänge gibt die Summe der Antworten (Linearität), und die um 2 s verschobene Quelle gibt die um 2 s verschobene Kurve (Zeitinvarianz).
:::

:::aufgabe Aufgabe 3 ★ LTI oder nicht?
<span class="anker" id="aufg-3"></span>

Prüfe für jedes System Linearität und Zeitinvarianz: (a) $g(t)=3\,s(t-2)$, (b) $g(t)=s(t)^2$, (c) $g(t)=s(t)+1$, (d) $g(t)=t\,s(t)$, (e) $g(t)=s(2t)$, (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$.

:::loesung
(a) Linear und zeitinvariant (Verstärkung 3, Verzögerung 2): LTI. (b) Nicht linear: $\operatorname{Tr}\{2s\}=4s^2\neq2s^2$. Zeitinvariant. (c) Nicht linear (affin, $\operatorname{Tr}\{0\}=1$). Zeitinvariant. (d) Linear. Nicht zeitinvariant: $\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$, aber $g(t-t_0)=(t-t_0)\,s(t-t_0)$. Der Faktor $t$ ist ein Bauteil, das sich mit der Zeit ändert. (e) Linear. Nicht zeitinvariant: $\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$, aber $g(t-t_0)=s(2t-2t_0)$. Wer die Zeit staucht, staucht auch jede Verschiebung. (f) LTI. Linear, weil das Integral linear ist. Zeitinvariant: $\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$. Seine Impulsantwort ist $\varepsilon(t)$ (Stufe [8](#stufe-8)).
:::
:::

## Stufe 4: Das Faltungsintegral

<span class="anker" id="stufe-4"></span>

:::zweck
Mit Linearität und Zeitinvarianz lässt sich die Antwort auf *jedes* Signal aus der Antwort auf einen einzigen kurzen Impuls berechnen. Das Ergebnis ist das Faltungsintegral.
:::

**Die Idee in vier Schritten.**

<ol>

<li>

⁠**Zerlegen.** Man nähert das Eingangssignal durch eine Treppe aus schmalen Rechtecken der Breite $T_0$. Als Baustein dient ein Rechteck $s_0(t)$ der Dauer $T_0$ und der Höhe $1/T_0$, also der Fläche 1. Die Stufe bei $nT_0$ ist dieser Baustein, verschoben um $nT_0$ und gewichtet mit $s(nT_0)\,T_0$, der Fläche des Streifens:

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**Ein Baustein durch das System.** Auf $s_0$ antwortet das System mit $g_0(t)$. Das muss man einmal kennen.

</li>

<li>

⁠**Zusammensetzen.** Zeitinvarianz: Der verschobene Baustein erzeugt die verschobene Antwort. Linearität: Gewichte und Summe gehen durch. Also

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**Grenzübergang $T_0\to0$.** Die Treppe wird zum Signal. Das Rechteck der Fläche 1 wird zum __Dirac-Impuls__ $\delta(t)$, einem unendlich kurzen Stoß der Fläche 1 (Stufe [7](#stufe-7)). Seine Antwort heißt __Impulsantwort__ $h(t)$. Aus $nT_0$ wird die stetige Variable $\tau$, aus $T_0$ das Differential $\mathrm{d}\tau$, aus den Summen Integrale.

</li>

</ol>

:::abbildung et3/k1treppe
Oben: Ein Dreieckimpuls $s(t)=\Lambda(t-1)$ und seine Treppennäherung mit $T_0=0{,}5$ s. Unten: die exakte Antwort des RC-Glieds und die Summe der verschobenen Rechteckantworten. Die größte Abweichung sinkt von 0,17 ($T_0=0{,}5$ s) über 0,08 ($0{,}25$ s) auf 0,03 ($0{,}1$ s).
:::

:::satz Satz 4.1 (Faltungsintegral)
<span class="anker" id="satz-4-1"></span>

Für jedes Signal $s(t)$ gilt

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

und ein LTI-System mit der Impulsantwort $h(t)$ antwortet darauf mit

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**So liest man das:** $\tau$ ist der Zeitpunkt eines Eingangsstoßes, $s(\tau)\,\mathrm{d}\tau$ sein Gewicht (die Fläche des Streifens). $h(t-\tau)$ ist die Antwort des Systems zur Zeit $t$ auf einen Stoß, der zur Zeit $\tau$ kam, also vor $t-\tau$ Sekunden. Der Ausgang sammelt alle Stöße der Vergangenheit, jeden gewichtet damit, wie stark sich das System nach dieser Zeit noch an ihn „erinnert“. Die Gleichung gilt exakt und für jedes LTI-System.

⁠**Kurz gesagt:** Der Ausgang eines LTI-Systems ist die Überlagerung seiner Impulsantworten, verschoben an jeden Zeitpunkt des Eingangs und gewichtet mit dem Eingang dort.

:::frage Warum müssen die Rechteckbausteine die Fläche 1 haben?
Damit die Antwort auf den Baustein beim Grenzübergang eine feste Form behält. Ein Rechteck der festen Höhe 1 hätte für $T_0\to0$ die Fläche null, und seine Antwort würde verschwinden. Mit der Höhe $1/T_0$ bleibt die Fläche 1, und die Antwort strebt gegen $h(t)$. Beim RC-Glied ist die Spitze der Antwort $(1-\mathrm{e}^{-T_0})/T_0$: 0,632 für $T_0=1$ s, 0,787 für 0,5 s, 0,952 für 0,1 s, und für $T_0\to0$ wird sie $1=h(0^+)$. Die Fläche der Antwort bleibt dabei immer 1.
:::

:::frage Gibt es den Stoß $\delta(t)$ in Wirklichkeit? Wie misst man dann $h(t)$?
Einen unendlich kurzen Stoß gibt es nicht. Es genügt aber jeder Impuls, der viel kürzer ist als die Zeitkonstanten des Systems. Dann sieht das System nur seine Fläche, und die Antwort ist praktisch $(\text{Fläche})\cdot h(t)$. Beim RC-Glied mit $RC=1$ s weicht die Spitze der Antwort auf einen 1-ms-Impuls nur um 0,05 % von $h(0^+)$ ab. So misst man Impulsantworten auch: Man klatscht in einem Raum in die Hände und nimmt den Nachhall auf.
:::

:::ltspice Impulsantwort mit einem kurzen Rechteck nähern
⁠**Zeichnen:** das RC-Glied aus Stufe [2](#stufe-2) mit der Quelle `PULSE(0 {1/T0} 0 1n 1n {T0})`: ein Rechteck der Breite $T_0$ und der Höhe $1/T_0$, also der Fläche 1.

⁠**Direktiven:** `.param T0=1`, `.step param T0 list 1 0.5 0.1 1m`, `.tran 0 10 0 1m`, `.meas tran spitze MAX V(out)`, `.meas tran flaeche INTEG V(out)`.

⁠**Was du siehst:** Die Spitzen sind 0,632; 0,787; 0,952 und 0,9995, wie $(1-\mathrm{e}^{-T_0})/T_0$. Beim 1-ms-Impuls ist die Antwort praktisch schon $h(t)=\mathrm{e}^{-t}$. Die Fläche ist in allen vier Läufen 1,000: Ein Impuls, der viel kürzer ist als $RC$, wirkt nur über seine Fläche.
:::

:::aufgabe Aufgabe 4 ★★ Die Treppe genauer
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Berechne die Antwort $g_0(t)$ des RC-Glieds ($RC=1$ s) auf das Rechteck der Höhe $1/T_0$ von $0$ bis $T_0$. Benutze dazu [(2.5)](#gl-2-5) und schreibe das Rechteck als Differenz zweier Sprünge.

</li>

<li>

Zeige, dass $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$ ist und für $T_0\to0$ gegen 1 strebt.

</li>

<li>

Warum ist die Näherung $g_a$ in Abb. [5](#abb-5) zu spät? (Tipp: Wo liegt die Stufe im Vergleich zum Dreieck auf der steigenden und auf der fallenden Flanke?)

</li>

</ol>

:::loesung
(a) Das Rechteck ist $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$. Linearität und Zeitinvarianz mit der Sprungantwort [(2.5)](#gl-2-5):

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) Bei $t=T_0$ ist der zweite Summand null: $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$. Mit $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$ für kleine $T_0$ ist das $\approx1-T_0/2\to1=h(0^+)$. Zahlen: 0,632; 0,787; 0,952 für $T_0=1$; 0,5; 0,1 s.

(c) Jede Stufe hält den Wert $s(nT_0)$ vom *Anfang* des Intervalls bis zu dessen Ende. Auf der steigenden Flanke liegt die Treppe deshalb unter dem Dreieck, auf der fallenden darüber: Sie ist im Mittel um $T_0/2$ verzögert. Der Ausgang erbt diese Verzögerung, auf der abfallenden Seite liegt $g_a$ über $g$ ($g_a(2)=0{,}508$ statt $0{,}400$ für $T_0=0{,}5$ s). Mit kleinerem $T_0$ schrumpft die Verzögerung und mit ihr der Fehler.
:::
:::

## Stufe 5: Die Faltung ausrechnen

<span class="anker" id="stufe-5"></span>

:::zweck
Das Integral [(4.2)](#gl-4-2) ist für konkrete Signale auszuwerten. Der Schlüssel ist, beide Faktoren über der Integrationsvariablen $\tau$ zu zeichnen.
:::

**Das Rezept.** Für einen festen Zeitpunkt $t$:

<ol>

<li>

$s(\tau)$ über $\tau$ zeichnen.

</li>

<li>

$h(-\tau)$ zeichnen: $h$ an der senkrechten Achse *spiegeln*.

</li>

<li>

$h(t-\tau)$: das gespiegelte $h$ um $t$ nach rechts *schieben*.

</li>

<li>

Beide *multiplizieren* und über $\tau$ *integrieren*: Das ist $g(t)$.

</li>

</ol>

Lässt man $t$ wachsen, gleitet das gespiegelte $h$ von links nach rechts über $s$. Wo sich die beiden nicht überlappen, ist $g(t)=0$.

Warum gespiegelt? Als Funktion von $\tau$ fällt das Argument $t-\tau$, wenn $\tau$ wächst. Der Anfang von $h$ (Alter null) liegt bei $\tau=t$, ältere Stöße liegen weiter links. Beim RC-Glied ist $h$ am Anfang am größten: Das System „erinnert“ sich an die jüngste Vergangenheit am stärksten.

**Beispiel: RC-Glied und Rechteckimpuls.** Die Impulsantwort des RC-Glieds mit der Zeitkonstanten $T=RC$ ist ein abfallender Exponentialimpuls der Fläche 1 (Stufe [8](#stufe-8) leitet ihn her):

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

Eingang: Rechteck der Höhe $a$ von $0$ bis $T_0$. Abbildung [6](#abb-6) zeigt die Lage der beiden Faktoren für zwei Zeitpunkte. Es gibt drei Bereiche:

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$

:::herleitung Antwort auf den Rechteckimpuls
⁠**$t<0$:** Das geschobene $h(t-\tau)$ ist nur für $\tau\le t<0$ von null verschieden, $s(\tau)$ nur für $\tau\ge0$. Keine Überlappung, $g=0$.

⁠**$0\le t\le T_0$:** Überlappung für $0<\tau<t$:

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$:** Überlappung nur noch für $0<\tau<T_0$:

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

Im Rechenmodell ($a=1$, $T_0=T=1$ s): $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$, $g(3)=0{,}0855$. Das ist dieselbe Kurve wie $g_0$ in Abb. [4](#abb-4).

:::abbildung et3/k1schieben
Faltung grafisch, $a=1$, $T_0=T=1$ s. Blau: $s(\tau)$. Rot: gespiegeltes und um $t$ geschobenes $h(t-\tau)$. Die orange Fläche ist $g(t)$: 0,3935 bei $t=0{,}5$ s (teilweise Überlappung), 0,2325 bei $t=2$ s (das ganze Rechteck liegt im abgeklungenen Teil von $h$). Rechts die vollständige Antwort mit beiden Punkten.
:::

:::frage Warum spiegelt man $h$ und nicht $s$?
Man darf auch $s$ spiegeln, denn die Faltung ist kommutativ (Stufe [6](#stufe-6)). Man spiegelt die Funktion, bei der das Schieben übersichtlicher ist, meist die mit der einfacheren Form.
:::

:::ltspice Antwort auf den Rechteckimpuls
⁠**Zeichnen:** das RC-Glied aus Stufe [2](#stufe-2) mit der Quelle `PULSE(0 1 0 1u 1u 1)`: Höhe 1 V, Dauer 1 s.

⁠**Direktiven:** `.tran 0 20 0 1m`, je Zeitpunkt eine Messung wie `.meas tran g2 FIND V(out) AT=2`, dazu `.meas tran gmax MAX V(out)` und `.meas tran flaeche INTEG V(out)`.

⁠**Was du siehst:** $g(0{,}5)=0{,}3935$, $g(1)=0{,}6321$, $g(2)=0{,}2325$ und $g(3)=0{,}0855$, genau wie nach [(5.2)](#gl-5-2). Vergleiche `gmax` und `flaeche` mit deinem Ergebnis aus Aufgabe [6](#aufg-6).
:::

:::aufgabe Aufgabe 5 ★★ Rechteck mit Rechteck
<span class="anker" id="aufg-5"></span>

Berechne $\operatorname{rect}(t)*\operatorname{rect}(t)$ mit dem Rezept. Unterscheide $|t|>1$, $-1\le t\le0$ und $0\le t\le1$. Welches Elementarsignal kommt heraus?

:::loesung
Das gespiegelte Rechteck ist wieder $\operatorname{rect}$ (symmetrisch), geschoben liegt es auf $[t-\frac12,t+\frac12]$. Das Integral ist die Länge der Überlappung mit $[-\frac12,\frac12]$:

<ul>

<li>

$|t|>1$: keine Überlappung, 0.

</li>

<li>

$-1\le t\le0$: Überlappung von $-\frac12$ bis $t+\frac12$, Länge $1+t$.

</li>

<li>

$0\le t\le1$: Überlappung von $t-\frac12$ bis $\frac12$, Länge $1-t$.

</li>

</ul>

Zusammen $1-|t|$ für $|t|\le1$: $\operatorname{rect}*\operatorname{rect}=\Lambda$. Numerisch: 1,000; 0,500; 0,200 bei $t=0$; 0,5; 0,8.
:::
:::

:::aufgabe Aufgabe 6 ★★ Die Rechteckantwort prüfen
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Zeige, dass [(5.2)](#gl-5-2) bei $t=T_0$ stetig ist. Warum muss sie stetig sein?

</li>

<li>

Wo hat $g(t)$ sein Maximum, und wie groß ist es im Rechenmodell?

</li>

<li>

Zeige, dass die Fläche unter $g(t)$ gleich $aT_0$ ist, und begründe das ohne Rechnung mit $\int h\,\mathrm{d} t=1$.

</li>

</ol>

:::loesung
(a) Bei $t=T_0$: $a(1-\mathrm{e}^{-T_0/T})$ und $a(\mathrm{e}^{T_0/T}-1)\mathrm{e}^{-T_0/T}=a(1-\mathrm{e}^{-T_0/T})$, gleich. Physikalisch: Die Kondensatorspannung kann nicht springen, dafür bräuchte es einen unendlichen Strom. Mathematisch: Die Faltung eines beschränkten Signals mit einem integrierbaren $h$ ist stetig.

(b) Während des Impulses steigt $g$, danach fällt es. Das Maximum liegt bei $t=T_0$: $g(1\,\mathrm{s})=1-\mathrm{e}^{-1}=0{,}632$.

(c) Rechnung:

$$\int g\,\mathrm{d} t=a\Bigl[T_0-T\bigl(1-\mathrm{e}^{-T_0/T}\bigr)\Bigr]+a\bigl(\mathrm{e}^{T_0/T}-1\bigr)T\mathrm{e}^{-T_0/T}=aT_0.$$

Ohne Rechnung: Die Fläche einer Faltung ist das Produkt der Flächen, $\int g\,\mathrm{d} t=\int\!\!\int s(\tau)h(t-\tau)\,\mathrm{d}\tau\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$. Numerisch: 1,000.
:::
:::

## Stufe 6: Rechenregeln der Faltung

<span class="anker" id="stufe-6"></span>

:::zweck
Die Faltung verhält sich in vielem wie eine Multiplikation. Jede Rechenregel hat eine Bedeutung für Systeme.
:::

Man schreibt das Faltungsintegral kurz als __Faltungsprodukt__ $g(t)=s(t)*h(t)$. Gleichung [(4.1)](#gl-4-1) lautet dann $s(t)=s(t)*\delta(t)$.

<ol class="al">

<li>

⁠**Einselement.** $s*\delta=s$: Der Dirac-Impuls spielt die Rolle der Eins. Ein System mit $h(t)=\delta(t)$ gibt jedes Signal unverändert weiter, es heißt __ideal verzerrungsfrei__.

</li>

<li>

⁠**Kommutativgesetz.** $s*h=h*s$. Bedeutung: Eingang und Impulsantwort dürfen die Rollen tauschen. Das System mit der Impulsantwort $s$ antwortet auf den Eingang $h$ genauso wie das System $h$ auf den Eingang $s$.

</li>

<li>

⁠**Assoziativgesetz.** $(f*s)*h=f*(s*h)$. Bedeutung: Zwei Systeme in Kette wirken wie ein System, dessen Impulsantwort die Faltung der beiden Impulsantworten ist.

</li>

<li>

⁠**Distributivgesetz.** $f*(s+h)=f*s+f*h$. Bedeutung: Zwei parallel geschaltete Systeme, deren Ausgänge addiert werden, wirken wie ein System mit der Summe der Impulsantworten.

</li>

<li>

⁠**Komplexe Signale.** Weil die Faltung linear ist, zerfällt sie in Real- und Imaginärteile:

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung Kommutativgesetz
Substitution $\tau'=t-\tau$, also $\tau=t-\tau'$ und $\mathrm{d}\tau=-\mathrm{d}\tau'$. Die Grenzen $\tau=\mp\infty$ werden zu $\tau'=\pm\infty$, das Vertauschen hebt das Minuszeichen auf:

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke
Oben: Kettenschaltung, Impulsantwort $h_1*h_2$ (Assoziativgesetz). Unten: Parallelschaltung mit Addition, Impulsantwort $h_1+h_2$ (Distributivgesetz).
:::

:::aufgabe Aufgabe 7 ★★ Zwei RC-Glieder in Kette
<span class="anker" id="aufg-7"></span>

Zwei RC-Glieder mit $RC=1$ s werden hintereinandergeschaltet. Das zweite belaste das erste nicht (zum Beispiel mit einem Spannungsfolger dazwischen).

<ol class="al">

<li>

Berechne die Impulsantwort der Kette, $h*h$ mit $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

</li>

<li>

Wann ist sie maximal, und wie groß ist ihre Fläche?

</li>

<li>

Warum braucht man die Bedingung „belastet nicht“?

</li>

</ol>

:::loesung
(a) Für $t\ge0$:

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

Also $h_{\text{Kette}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$.

(b) Ableitung $(1-t)\mathrm{e}^{-t}=0$ bei $t=1$ s, Maximum $\mathrm{e}^{-1}=0{,}368$. Fläche $\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$ (Produkt der Flächen).

(c) Ohne Entkopplung zieht das zweite RC-Glied Strom aus dem ersten Kondensator. Dann ist die Spannung am ersten Kondensator nicht mehr die eines unbelasteten RC-Glieds, und die Kette hat nicht $h*h$ als Impulsantwort. Sie bleibt ein LTI-System, aber mit einer anderen Impulsantwort. Die Faltung der Einzelantworten setzt voraus, dass jedes System seinen Eingang nicht zurückbeeinflusst.
:::
:::

## Stufe 7: Der Dirac-Impuls

<span class="anker" id="stufe-7"></span>

:::zweck
Der Dirac-Impuls ist das Grenzobjekt aus Stufe [4](#stufe-4). Er ist keine gewöhnliche Funktion. Alle seine Eigenschaften folgen daraus, dass er nur über seine Fläche wirkt.
:::

**Was $\delta$ ist und was nicht.** Die Rechtecke $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ werden für $T_0\to0$ immer schmaler und höher, ihre Fläche bleibt 1 (Abb. [8](#abb-8)). Einen Grenzwert im Sinne gewöhnlicher Funktionen gibt es nicht: Eine Funktion, die überall außer in einem Punkt null ist, hat die Fläche null, egal welchen Wert sie in diesem Punkt hat. $\delta(t)$ ist deshalb eine __Distribution__: ein Objekt, das nur durch seine Wirkung unter einem Integral festgelegt ist, nämlich durch [(4.1)](#gl-4-1). Gezeichnet wird es als Pfeil, dessen Höhe das Gewicht (die Fläche) angibt.

:::abbildung et3/k1dirac
Links: Rechtecke der Fläche 1, immer schmaler und höher. Rechts: das Symbol des Grenzobjekts. Die Pfeilhöhe ist das Gewicht, nicht der Funktionswert.
:::

:::satz Satz 7.1 (Eigenschaften des Dirac-Impulses)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{Gewicht:} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{Sieb:} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{Fläche:} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{Dehnung:} && \delta(bt)=\frac{1}{|b|}\,\delta(t),\qquad \delta(-t)=\delta(t),\\ &\text{Verschiebung:} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{Integral:} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**So liest man das:** Das Produkt $s(t)\,\delta(t-T)$ kann nur an der Stelle $T$ etwas bewirken, also zählt nur $s(T)$. Ein gestauchter Impuls $\delta(bt)$ ist zwar genauso „unendlich hoch“, hat aber nur noch die Fläche $1/|b|$. Ein System mit $h(t)=\delta(t-t_0)$ verzögert jedes Signal um $t_0$, es heißt __ideales Laufzeitglied__. Und weil der Sprung das laufende Integral des Stoßes ist, darf man Funktionen mit Sprungstellen ableiten: Ein Sprung der Höhe $A$ wird zu $A\,\delta$. Das heißt __verallgemeinerte Differentiation__. Vorsicht: Viele Operationen, etwa das Quadrieren $\delta^2$, sind für Dirac-Impulse nicht definiert.

:::herleitung Dehnung und Sieb-Produkt
⁠**Dehnung.** Für $b>0$ mit $\vartheta=b\tau$:

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

Für $b<0$ kehrt die Substitution die Integrationsrichtung um, es kommt $-\frac1b=\frac{1}{|b|}$ heraus. Also wirkt $\delta(bt)$ wie $\frac1{|b|}\delta(t)$. Mit $b=-1$ folgt die Symmetrie $\delta(-t)=\delta(t)$.

⁠**Sieb-Produkt.** Faltet man $s(t)\delta(t)$ mit einem beliebigen $g(t)$, ergibt die Siebeigenschaft

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

Beide wirken auf jedes $g$ gleich, also $s(t)\delta(t)=s(0)\delta(t)$. Mit Verschiebung folgt $s(t)\delta(t-T)=s(T)\delta(t-T)$.

⁠**Integral.** $\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$, und $\varepsilon(t-\tau)=1$ genau für $\tau\le t$.
:::

:::frage $\delta(0)$ ist doch unendlich. Dann ist $\delta(2t)$ dasselbe wie $\delta(t)$, oder?
Nein. „Unendlich hoch“ beschreibt $\delta$ nicht, denn alle Funktionswerte außer bei $0$ sind gleich, und der Wert bei $0$ ist keine Zahl. Was $\delta$ ausmacht, ist seine Fläche. Staucht man das Rechteck der Fläche 1 auf die halbe Breite und lässt die Höhe gleich, halbiert sich die Fläche. Deshalb ist $\delta(2t)=\frac12\delta(t)$.
:::

:::aufgabe Aufgabe 8 ★ Rechnen mit $\delta$
<span class="anker" id="aufg-8"></span>

Berechne: (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$, (b) $\mathrm{e}^{-t}\,\delta(t-1)$, (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$, (d) $\delta(t)*\delta(t-3)$, (e) $\operatorname{rect}(t)*\delta(t-1)$, (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$.

:::loesung
(a) $\mathrm{e}^{-2}=0{,}135$. (b) $\mathrm{e}^{-1}\,\delta(t-1)$. (c) $\tfrac12$. (d) $\delta(t-3)$. (e) $\operatorname{rect}(t-1)$. (f) $3\,\delta(t-1)$.
:::
:::

## Stufe 8: Integrieren und Differenzieren

<span class="anker" id="stufe-8"></span>

:::zweck
Integrator und Differenzierer sind LTI-Systeme. Mit ihnen hängen Sprungantwort und Impulsantwort zusammen, und man kann die Impulsantwort des RC-Glieds aus seiner Sprungantwort gewinnen.
:::

**Der Integrator.** Ersetzt man in [(7.6)](#gl-7-6) $\delta$ durch ein beliebiges $s$, folgt dieselbe Rechnung:

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

Ein System mit der Impulsantwort $\varepsilon(t)$ bildet das laufende Integral seines Eingangs, es heißt __Integrator__. Liest man [(8.1)](#gl-8-1) mit vertauschten Rollen ($\varepsilon*s$), sagt sie: **Die Sprungantwort eines Systems ist das laufende Integral seiner Impulsantwort.** Probe am RC-Glied: $\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$, genau [(2.5)](#gl-2-5). Zwei unabhängige Wege, Differentialgleichung und Faltung, geben dasselbe.

**Der Differenzierer.** Integrator und __Differenzierer__ nacheinander lassen jedes Signal unverändert, die Kette ist ideal verzerrungsfrei. Die Impulsantwort des Differenzierers ist deshalb die Distribution $\delta'(t)$ (__Doppelimpuls__), festgelegt durch

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

Näherungsweise ist $\delta'$ ein schmaler Doppelrechteckimpuls: erst ein Rechteck der Höhe $+1/T_0^2$, dann eines der Höhe $-1/T_0^2$, jedes $T_0$ breit. Gezeichnet wird er als Pfeilpaar nach oben und unten.

**Impulsantwort = Ableitung der Sprungantwort.** Weil $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$ und das System linear und zeitinvariant ist, gilt $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{Sprungantwort})$. Für das RC-Glied mit der Produktregel:

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

Der zweite Summand verschwindet nach [(7.2)](#gl-7-2): $(1-\mathrm{e}^{0})\,\delta(t)=0$. Der Mechanismus dahinter: Die Sprungantwort des RC-Glieds springt nicht, der Kondensator braucht Zeit zum Laden. Nur eine springende Sprungantwort erzeugt einen Dirac-Impuls in $h$ (Aufgabe [9](#aufg-9)).

:::aufgabe Aufgabe 9 ★★ Hochpass: ein Dirac-Impuls in der Impulsantwort
<span class="anker" id="aufg-9"></span>

Vertauscht man $R$ und $C$, wird die Spannung an $R$ abgegriffen (CR-Hochpass, $RC=1$ s). Seine Sprungantwort ist $\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Begründe die Sprungantwort mit dem Mechanismus: Was liegt im ersten Moment an $R$, was nach langer Zeit?

</li>

<li>

Bestimme die Impulsantwort durch Ableiten. Was bedeutet der Dirac-Anteil physikalisch?

</li>

<li>

Prüfe: Integrieren der Impulsantwort muss die Sprungantwort zurückgeben.

</li>

</ol>

:::loesung
(a) Im ersten Moment ist der Kondensator leer, über ihm liegt keine Spannung. Die vollen 1 V liegen an $R$. Danach lädt der Strom den Kondensator, seine Spannung steigt wie $1-\mathrm{e}^{-t}$, an $R$ bleibt $\mathrm{e}^{-t}$. Nach langer Zeit ist der Kondensator voll, es fließt kein Strom, an $R$ liegt nichts mehr.

(b) Produktregel:

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

Hier springt die Sprungantwort bei $t=0$ von 0 auf 1, deshalb bleibt der Dirac-Anteil stehen. Physikalisch: Ein unendlich kurzer Stoß geht vollständig durch, weil der Kondensator in null Zeit keine Spannung aufbauen kann. Die Ladung, die der Stoß auf den Kondensator gebracht hat, fließt danach über $R$ wieder ab, in Gegenrichtung: $-\mathrm{e}^{-t}$.

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$.
:::
:::

## Stufe 9: Kausal und stabil

<span class="anker" id="stufe-9"></span>

:::zweck
Zwei Eigenschaften, die jedes reale System haben soll, lassen sich direkt an $h(t)$ ablesen.
:::

:::definition Definition 9.1 (Kausal, stabil)
<span class="anker" id="satz-9-1"></span>

Ein System heißt __kausal__, wenn der Ausgang nicht vor dem Eingang beginnt. Für ein LTI-System heißt das

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{für }t<0. \tag{9.1}$$

Ein System heißt __stabil__ (genauer BIBO-stabil, *bounded input, bounded output*), wenn es auf jeden beschränkten Eingang $|s(t)|\le A<\infty$ mit einem beschränkten Ausgang antwortet.
:::

Kausal: Ein Stoß zur Zeit 0 kann vorher keine Wirkung haben. In der Faltung tragen dann nur Stöße der Vergangenheit bei, $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$.

:::satz Satz 9.2 (Stabilitätsbedingung)
<span class="anker" id="satz-9-2"></span>

Ein LTI-System ist genau dann stabil, wenn seine Impulsantwort absolut integrierbar ist:

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung Stabilitätsbedingung
⁠**Hinreichend.** Mit der Dreiecksungleichung für Integrale und $|s|\le A$:

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

Ist das Integral endlich, ist $g$ beschränkt.

⁠**Notwendig.** Ist $\int|h|=\infty$, wählt man den ungünstigsten beschränkten Eingang: $s(t_1-\tau)=\operatorname{sign}h(\tau)$, also immer $\pm1$ mit dem Vorzeichen von $h$. Dann ist $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$, obwohl $|s|\le1$.
:::

Beispiele: Das RC-Glied hat $\int|h|=1$ und ist stabil. Das ideale Laufzeitglied ($\int|\delta(t-t_0)|\mathrm{d} t=1$) ist stabil. Der Integrator hat $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$ und ist instabil: Auf den beschränkten Sprung antwortet er mit der unbeschränkten Rampe $t\,\varepsilon(t)$.

:::aufgabe Aufgabe 10 ★★ Kausal? Stabil?
<span class="anker" id="aufg-10"></span>

Untersuche (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$, (b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$, (c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$, (d) $h(t)=\mathrm{e}^{-|t|}$, (e) $h(t)=\delta(t+1)$. Gib bei jedem instabilen System einen beschränkten Eingang an, der einen unbeschränkten Ausgang erzeugt.

:::loesung
(a) Kausal, $\int|h|=\tfrac12$: stabil.

(b) Kausal, $\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$: instabil. Der Sprung $\varepsilon(t)$ erzeugt $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$, unbeschränkt.

(c) Kausal, $\int|h|=1$: stabil. Das System bildet das Integral des Eingangs über die letzte Sekunde (gleitendes Fenster).

(d) Nicht kausal, denn $h(t)\neq0$ für $t<0$. $\int\mathrm{e}^{-|t|}\mathrm{d} t=2$: stabil.

(e) $\delta(t+1)$ ist für $t=-1<0$ wirksam: $g(t)=s(t+1)$, das System „sieht“ den Eingang eine Sekunde im Voraus. Nicht kausal, aber stabil ($\int|h|=1$).
:::
:::

## Stufe 10: Faltung ganz ohne System

<span class="anker" id="stufe-10"></span>

:::frage Die Faltung ergibt Sinn, wenn ein Signal wirklich durch ein System geht. Was bedeutet sie, wenn kein System im Spiel ist?
Die Faltung ist eine Rechenoperation mit einer eigenen, allgemeinen Bedeutung: *Für jede Art, ein Ergebnis in zwei Anteile aufzuteilen, multipliziert man die Gewichte der beiden Anteile und summiert über alle Aufteilungen.* Das System ist eine Deutung davon (Anteil 1: wann kam der Stoß, Anteil 2: wie alt ist er), nicht die einzige.

⁠**Beispiel ohne System und ohne Zeit: zwei Würfel.** Mit welcher Wahrscheinlichkeit ist die Augensumme $k$? Jede Aufteilung $k=i+(k-i)$ trägt bei, mit der Wahrscheinlichkeit $P_1(i)\,P_2(k-i)$:

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

Das ist eine Faltung, mit genau derselben Struktur wie $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$: $\tau$ entspricht der Augenzahl des ersten Würfels, $t$ der Summe, $t-\tau$ der Augenzahl des zweiten. Zwei gleichverteilte Würfel („Rechtecke“) ergeben eine Dreieckverteilung, genau wie $\operatorname{rect}*\operatorname{rect}=\Lambda$ in Aufgabe [5](#aufg-5). Die 7 ist am häufigsten, weil sie die meisten Aufteilungen hat (Abb. [9](#abb-9)).

Weitere Beispiele: Ein gleitender Mittelwert über Messwerte ist eine Faltung mit einem Rechteck. Ein unscharfes Foto ist das scharfe Bild, gefaltet mit dem Lichtfleck, den die Optik aus einem Punkt macht. Und wer zwei Polynome multipliziert, faltet ihre Koeffizienten (Aufgabe [11](#aufg-11)).
:::

:::abbildung et3/k1wuerfel
Wahrscheinlichkeiten der Augensumme. Jede Verteilung ist die Faltung der vorigen mit der eines einzelnen Würfels. Aus dem Rechteck wird ein Dreieck ($P(7)=6/36$), daraus eine glockenförmige Kurve ($P(10)=P(11)=27/216$).
:::

:::zusatz Warum Faltungen so oft auftreten
Faltet man immer mehr gleiche Verteilungen, nähert sich das Ergebnis einer Gaußkurve, fast unabhängig von der Ausgangsform (zentraler Grenzwertsatz). Deshalb ist Rauschen, die Summe vieler kleiner unabhängiger Einflüsse, so oft gaußverteilt. Und dass die Faltung der Koeffizienten zu einem Produkt von Polynomen gehört, ist der Kern aller Transformationen, die Faltungen in Produkte verwandeln: [Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) macht dasselbe mit den Bausteinen $\mathrm{e}^{pt}$ statt den Potenzen $x^n$.
:::

:::aufgabe Aufgabe 11 ★ Faltung mit Würfeln und Polynomen
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Berechne $P(7)$ und $P(4)$ für zwei Würfel aus der Faltungssumme. Welche Aufteilungen tragen jeweils bei?

</li>

<li>

Berechne $P(10)$ für drei Würfel, indem du die Verteilung zweier Würfel mit der eines Würfels faltest.

</li>

<li>

Multipliziere $(1+2x)(3+x)$ aus. Zeige, dass die Koeffizientenfolge des Ergebnisses die Faltung der Folgen $(1,2)$ und $(3,1)$ ist.

</li>

</ol>

:::loesung
(a) $P(7)$: Aufteilungen $1+6,\,2+5,\dots,6+1$, sechs Stück, jede mit $\frac16\cdot\frac16$: $P(7)=\frac{6}{36}=\frac16$. $P(4)$: $1+3,\,2+2,\,3+1$: $\frac{3}{36}=\frac{1}{12}$.

(b) $P_3(10)=\sum_{j=1}^6P_2(10-j)\cdot\frac16=\frac16\bigl[P_2(9)+P_2(8)+P_2(7)+P_2(6)+P_2(5)+P_2(4)\bigr]=\frac16\cdot\frac{4+5+6+5+4+3}{36}=\frac{27}{216}=\frac18$.

(c) $(1+2x)(3+x)=3+x+6x+2x^2=3+7x+2x^2$. Der Koeffizient von $x^k$ sammelt alle Paare von Potenzen $i+j=k$: $c_0=1\cdot3=3$, $c_1=1\cdot1+2\cdot3=7$, $c_2=2\cdot1=2$. Das ist die Faltungssumme $c_k=\sum_ia_ib_{k-i}$, dieselbe Struktur wie bei den Würfeln.
:::
:::

:::kern Das Wichtigste
<ul>

<li>

Verschieben $t\to t-t_0$ verzögert, Dehnen $t\to t/T$ verbreitert; $a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$: Mitte $t_0$, Dauer $|T|$, Höhe $a$.

</li>

<li>

RC-Tiefpass: $H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$, $|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$, $\varphi=-\arctan(2\pi FRC)$; Sprungantwort $1-\mathrm{e}^{-t/RC}$.

</li>

<li>

LTI: Überlagerungssatz und $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$.

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$ und $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$.

</li>

<li>

Rechnen: spiegeln, schieben, multiplizieren, integrieren.

</li>

<li>

$s*\delta=s$; kommutativ, assoziativ (Kette: $h_1*h_2$), distributiv (parallel: $h_1+h_2$).

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$; $\delta(bt)=\delta(t)/|b|$; $\delta(t-t_0)*s=s(t-t_0)$; $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$.

</li>

<li>

Sprungantwort $=\int h$, Impulsantwort $=\frac{\mathrm{d}}{\mathrm{d} t}$Sprungantwort.

</li>

<li>

Kausal: $h(t)=0$ für $t<0$. Stabil: $\int|h|\mathrm{d} t<\infty$.

</li>

</ul>
:::

**Ausblick auf [Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html).** Dieser Artikel zerlegt Signale in Stöße $\delta(t-\tau)$. Das System antwortet auf jeden mit einer verschobenen Kopie von $h$, und man muss alle Kopien aufsummieren, die Faltung. [Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) zerlegt Signale in Bausteine $\mathrm{e}^{pt}$. Auf jeden davon antwortet das System nur mit einer Zahl $H(p)$, und aus der Faltung wird eine Multiplikation.
