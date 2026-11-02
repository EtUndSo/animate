---
title: Stufe 4: Aus dem Integral wird eine Summe
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220700
summary: Die Vermutung wörtlich: Für die Signale, um die es in der Systemtheorie fast immer geht, ist das Signal eine endliche Summe komplexer e-Funktionen.
tags: Partialbruchzerlegung, Stabilität, Eigenbewegung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Vermutung wörtlich: Für die Signale, um die es in der Systemtheorie fast immer geht, ist das Signal eine *endliche Summe* komplexer e-Funktionen. Die Pole sind die Exponenten.
:::

**Die Idee.** Bei Netzwerken aus $R$, $L$, $C$ und bei allen Systemen mit einer Differentialgleichung ist $S(p)$ ein Bruch aus Polynomen. Die __Partialbruchzerlegung__ schreibt ihn bei einfachen Polen als

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

Jeder Summand ist die Transformierte *eines einzigen Bausteins*: Nach [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) gehört $A_r/(p-p_r)$ zu $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$, wenn der Konvergenzbereich rechts des Pols liegt, und der konstante Summand $A_0$ gehört nach [(2.4)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-4) zu $A_0\,\delta(t)$. Für ein rechtsseitiges Signal ist also

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**Kurz gesagt:** Ein rechtsseitiges Signal mit rationaler Laplace-Transformierten ist eine endliche Summe von Bausteinen $\mathrm{e}^{p_r t}$. Die Pole sind die Exponenten, die Partialbruchkoeffizienten die Gewichte.

Damit lässt sich jedes solche Signal an seinen Polen ablesen, mit der Landkarte aus Abb. [1](warum-gerade.html#abb-1): $\operatorname{Re} p_r$ sagt, ob der Baustein abklingt oder wächst, $\operatorname{Im} p_r$, wie schnell er schwingt. Ein konjugiertes Polpaar $p_r,p_r^*$ ergibt zusammen eine reelle gedämpfte Schwingung. Hier liegt auch der Kern der __Stabilität__: Ein kausaler Baustein $\mathrm{e}^{p_r t}\varepsilon(t)$ klingt genau dann ab, wenn $\operatorname{Re} p_r<0$. Ein kausales System ist deshalb stabil, wenn alle Pole von $H(p)$ in der linken Halbebene liegen.

**Beispiel.** Die Sprungantwort aus Stufe [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3) hat die Pole $0$ und $-1$:

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{Pol }0\text{ (von }S)}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{Pol }-1\text{ (von }H)}\qquad(t>0).$$

Der Pol des Eingangs liefert den Anteil, den der Eingang erzwingt (die Endspannung 1). Der Pol des Systems liefert die __Eigenbewegung__ des RC-Glieds, das Abklingen mit $RC=1$ s. Das gilt allgemein: Im Ausgang $G=SH$ stecken die Pole des Eingangs und die Pole des Systems.

:::zusatz Warum das Integral zur Summe zusammenfällt: der Residuensatz
Dieser Abschnitt braucht den Residuensatz der Funktionentheorie. Er erklärt, warum [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) und [(4.1)](#gl-4-1) dasselbe sind und warum der Konvergenzbereich über das Signal entscheidet.

Sei $S(p)$ ein Polynombruch mit kleinerem Zählergrad als Nennergrad und einfachen Polen.

<ul>

<li>

⁠**$t>0$:** Man schließt die Integrationslinie durch einen großen Halbkreis nach *links*. Dort geht $\operatorname{Re} p\to-\infty$, also $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$, und $S(p)\to0$. Der Halbkreis trägt im Grenzfall nichts bei (Jordansches Lemma). Der geschlossene Weg läuft gegen den Uhrzeigersinn, und der Residuensatz gibt

$$s(t)=\sum_{\text{Pole links der Linie}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{links}}A_r\,\mathrm{e}^{p_r t}.$$

Das Residuum an einem einfachen Pol ist $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$: genau der Partialbruchkoeffizient.

</li>

<li>

⁠**$t<0$:** Jetzt verschwindet $\mathrm{e}^{pt}$ für $\operatorname{Re} p\to+\infty$. Man schließt nach *rechts*, der Weg läuft im Uhrzeigersinn, das gibt ein Minuszeichen:

$$s(t)=-\sum_{\text{Pole rechts der Linie}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**Folge:** Die Lage der Linie, also der Konvergenzbereich, entscheidet, welche Pole kausale Bausteine liefern (links der Linie) und welche antikausale (rechts der Linie). Beispiel: $S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$ (Abb. [5](#abb-5)). Liegt die Linie zwischen den Polen, $-2<\sigma<-1$, wirkt $-2$ für $t>0$ und $-1$ für $t<0$:

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

Numerisch auf der Linie $\sigma=-1{,}5/\mathrm s$ ausgewertet: $s(1\,\mathrm{s})=-0{,}1353=-\mathrm{e}^{-2}$ und $s(-1\,\mathrm{s})=-2{,}7183=-\mathrm{e}^{1}$. Liegt die Linie rechts von beiden Polen, ergibt dieselbe Formel das kausale Signal $(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(t)$, liegt sie links von beiden, das antikausale $-(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(-t)$.

:::abbildung et3/k2residuen 5
Integrationslinie $\sigma=-1{,}5/\mathrm s$ im Streifen $-2<\operatorname{Re} p<-1$ (blau) und die Halbkreise, mit denen man sie schließt (rot).
:::
:::

:::aufgabe Aufgabe 7 ★★★ (Vertiefung) Dieselbe Formel, zwei Signale
<span class="anker" id="aufg-7"></span>

$S(p)=\dfrac{1}{p+1}$.

<ol class="al">

<li>

Konvergenzbereich $\operatorname{Re} p>-1$. Werte die Umkehrformel mit dem Residuensatz aus, getrennt für $t>0$ und $t<0$.

</li>

<li>

Dasselbe für den Konvergenzbereich $\operatorname{Re} p<-1$.

</li>

<li>

Vergleiche mit den Grundpaaren [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) und [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3). Was lernst du daraus über die Angabe „$S(p)=1/(p+1)$“ ohne Konvergenzbereich?

</li>

</ol>

:::loesung
(a) Linie rechts vom Pol, zum Beispiel $\sigma=0$. Für $t>0$ nach links schließen: Der Pol $-1$ liegt innen, $\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$, also $s(t)=\mathrm{e}^{-t}$. Für $t<0$ nach rechts schließen: Rechts der Linie liegt kein Pol, $s(t)=0$. Zusammen $s(t)=\mathrm{e}^{-t}\varepsilon(t)$.

(b) Linie links vom Pol, zum Beispiel $\sigma=-2$. Für $t>0$ nach links schließen: kein Pol, $s(t)=0$. Für $t<0$ nach rechts schließen: Pol innen, Umlauf im Uhrzeigersinn, $s(t)=-\mathrm{e}^{-t}$. Zusammen $s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$.

(c) Das sind genau die Grundpaare [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) und [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3) mit $p_0=-1$. Die Angabe „$S(p)=1/(p+1)$“ allein legt das Signal nicht fest. Erst mit dem Konvergenzbereich ist klar, auf welcher Seite der Linie der Pol liegt und ob er einen kausalen oder einen antikausalen Baustein liefert.
:::
:::
