---
title: Stufe 1: Integrale mit Parameter
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120300
summary: Hängt der Integrand von einer weiteren Größe ab, hängt auch das Integral von ihr ab.
tags: Parameterintegral, Parameter, Integrationsvariable
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Hängt der Integrand von einer weiteren Größe ab, hängt auch das Integral von ihr ab. Diese Stufe klärt, wann diese neue Funktion stetig ist und wann man sie unter dem Integralzeichen ableiten darf.
:::

**Die Idee.** Für jeden festen Wert von $x$ ist $t\mapsto\mathrm{e}^{-xt}$ eine gewöhnliche Kurve. Die Fläche darunter ist eine Zahl, und jeder Wert von $x$ liefert eine andere Zahl (Abb. [1](#abb-1)):

<span class="anker" id="gl-1-1"></span>
$$F(x)=\int_0^1\mathrm{e}^{-xt}\,\mathrm{d} t=\begin{cases}(1-\mathrm{e}^{-x})/x&x\neq0,\\1&x=0.\end{cases} \tag{1.1}$$

Das ist ein __Parameterintegral__: Über $t$ wird integriert, $t$ verschwindet dabei, und übrig bleibt eine Funktion von $x$. Diese Größe heißt __Parameter__. Dreht man $x$ ein wenig weiter, ändert sich die Kurve an jeder Stelle $t$ ein wenig. Die Fläche ändert sich um die Summe all dieser kleinen Änderungen. Also sollte die Ableitung von $F$ das Integral der Ableitung des Integranden sein.

:::abbildung hm3/k2schar 1
Links die Kurven $\mathrm{e}^{-xt}$ für $x=0$, $x=1$ und $x=3$. Rechts wird jede dieser Flächen zu einem Punkt auf der Kurve $F(x)$. Bei $x=1$ ist die Steigung von $F$ gleich $2/\mathrm{e}-1\approx-0{,}264$.
:::

:::satz Satz 1.1 (Parameterintegrale)
<span class="anker" id="satz-1-1"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $f:\mathcal U\times[a,b]\to\mathbb{R}$ stetig. Dann ist

$$F(\boldsymbol{x}):=\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t$$

stetig in $\mathcal U$. Sind ferner für alle $k=1,\dots,n$ die Ableitungen $\frac{\partial f}{\partial x_k}:\mathcal U\times[a,b]\to\mathbb{R}$ stetig, dann ist $F$ stetig differenzierbar in $\mathcal U$, und für alle $\boldsymbol{x}\in\mathcal U$ und $k=1,\dots,n$ gilt

<span class="anker" id="gl-1-2"></span>
$$\frac{\partial F}{\partial x_k}(\boldsymbol{x})=\int_a^b\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\,\mathrm{d} t. \tag{1.2}$$
:::

⁠**So liest man das:** $\boldsymbol{x}$ ist der Parameter, im Modell die Zahl $x=1$. $t$ ist die __Integrationsvariable__, sie läuft von $a=0$ bis $b=1$. $f(\boldsymbol{x},t)$ ist die Höhe der Kurve an der Stelle $t$, im Modell $\mathrm{e}^{-t}$. Formel [(1.2)](#gl-1-2) vertauscht zwei Grenzwerte, denn Ableitung und Integral sind beide Grenzwerte.

**Beispiel.** Für das Modell sagt [(1.2)](#gl-1-2): $F'(x)=-\int_0^1t\,\mathrm{e}^{-xt}\,\mathrm{d} t$. Bei $x=0$ ist $F'(0)=-\int_0^1t\,\mathrm{d} t=-\frac12$. Aus der geschlossenen Form in [(1.1)](#gl-1-1) wäre das nur über einen Grenzwert zu bekommen. Bei $x=1$ gibt partielle Integration $F'(1)=\frac{2}{\mathrm{e}}-1\approx-0{,}264$, und Ableiten von $(1-\mathrm{e}^{-x})/x$ liefert denselben Wert. **Grenzfall:** Hängt $f$ nicht von $\boldsymbol{x}$ ab, ist $F$ konstant und beide Seiten von [(1.2)](#gl-1-2) sind null.

:::beweis Ableitung und Integral vertauschen
⁠**Stetigkeit.** Sei $\boldsymbol{x}\in\mathcal U$. Eine kleine abgeschlossene Kugel $B$ um $\boldsymbol{x}$ liegt in $\mathcal U$, und $B\times[a,b]$ ist kompakt. Dort ist $f$ gleichmäßig stetig: Zu $\varepsilon>0$ gibt es $\delta>0$ mit $|f(\boldsymbol{y},t)-f(\boldsymbol{x},t)|<\varepsilon$ für alle $t\in[a,b]$, falls $\boldsymbol{y}\in B$ und $|\boldsymbol{y}-\boldsymbol{x}|<\delta$. Dann ist $|F(\boldsymbol{y})-F(\boldsymbol{x})|\le\varepsilon\,(b-a)$.

⁠**Schritt 1: Differenzenquotient.** Fixiere $k$ und wähle $h_0>0$ so klein, dass $\boldsymbol{x}+h\hat{\boldsymbol{e}}_k\in\mathcal U$ für alle $0\le h\le h_0$ gilt. Das geht, weil $\mathcal U$ offen ist. Das Integral ist linear, also ist für $0<h\le h_0$

$$\frac{F(\boldsymbol{x}+h\hat{\boldsymbol{e}}_k)-F(\boldsymbol{x})}{h}=\int_a^b\frac{f(\boldsymbol{x}+h\hat{\boldsymbol{e}}_k,t)-f(\boldsymbol{x},t)}{h}\,\mathrm{d} t.$$

⁠**Schritt 2: Mittelwertsatz.** Für festes $t$ ist $s\mapsto f(\boldsymbol{x}+s\hat{\boldsymbol{e}}_k,t)$ eine Funktion einer Variablen. Der Mittelwertsatz liefert ein $\tau_h(t)\in[0,h]$ mit

$$\frac{f(\boldsymbol{x}+h\hat{\boldsymbol{e}}_k,t)-f(\boldsymbol{x},t)}{h}=\frac{\partial f}{\partial x_k}\bigl(\boldsymbol{x}+\tau_h(t)\,\hat{\boldsymbol{e}}_k,t\bigr).$$

⁠**Schritt 3: gleichmäßige Stetigkeit.** Die Funktion $(\tau,t)\mapsto\frac{\partial f}{\partial x_k}(\boldsymbol{x}+\tau\hat{\boldsymbol{e}}_k,t)$ ist stetig auf der kompakten Menge $[0,h_0]\times[a,b]$, also gleichmäßig stetig. Zu jedem $\varepsilon>0$ gibt es daher ein $\delta>0$, das nicht von $t$ abhängt, mit

$$\Bigl|\frac{\partial f}{\partial x_k}(\boldsymbol{x}+\tau\hat{\boldsymbol{e}}_k,t)-\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\Bigr|<\varepsilon\quad\text{für alle }t\in[a,b],\quad\text{falls }|\tau|<\delta.$$

⁠**Schritt 4: Grenzübergang.** Wegen $0\le\tau_h(t)\le h$ gilt das für jedes $h<\delta$ mit $\tau=\tau_h(t)$. Aus den Schritten 1 und 2 folgt

$$\Bigl|\frac{F(\boldsymbol{x}+h\hat{\boldsymbol{e}}_k)-F(\boldsymbol{x})}{h}-\int_a^b\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\,\mathrm{d} t\Bigr|\le\varepsilon\,(b-a).$$

Für $h\searrow0$ ist das der rechtsseitige Grenzwert in [(1.2)](#gl-1-2). Für $h\nearrow0$ argumentiert man genauso. Damit existiert $\partial F/\partial x_k$. Nach dem Stetigkeitsteil, angewandt auf $\partial f/\partial x_k$, ist diese Ableitung stetig.
:::

**Abgeschlossenes Parameterintervall.** Der Satz gilt auch für $f:[a,b]\times[c,d]\to\mathbb{R}$ mit Parameter $y$ in einem abgeschlossenen Intervall. Ist $f$ stetig, dann ist $F(y)=\int_a^bf(x,y)\,\mathrm{d} x$ stetig auf $[c,d]$. Existiert $\partial f/\partial y$ auf $[a,b]\times[c,d]$ und ist dort stetig, dann ist $F$ stetig differenzierbar auf $[c,d]$. An den Rändern $y=c$ und $y=d$ sind die rechts- bzw. linksseitigen Ableitungen gemeint.

:::frage Ableitung und Integral sind beide linear. Wozu braucht man dann den Satz?
Linearität erlaubt das Vertauschen mit endlichen Summen. Das Integral ist aber ein Grenzwert von Summen, und zwei Grenzwerte darf man nicht blind tauschen. Der Beweis zeigt, was es erlaubt: In Schritt 3 hängt $\delta$ nicht von $t$ ab, die Differenzenquotienten nähern sich also an allen Stellen $t$ zugleich der Ableitung. Das kommt daher, dass $[0,h_0]\times[a,b]$ kompakt ist.
:::

:::aufgabe Aufgabe 1 ★ Ein Integral durch Ableiten
<span class="anker" id="aufg-1"></span>

Zeige mit [(1.2)](#gl-1-2), dass $\int_0^1t^2\,\mathrm{e}^{-xt}\,\mathrm{d} t=F''(x)$ für das Modell [(1.1)](#gl-1-1) gilt. Berechne damit $\int_0^1t^2\,\mathrm{e}^{-t}\,\mathrm{d} t$ ohne partielle Integration.

:::loesung
$f=\mathrm{e}^{-xt}$ und alle Ableitungen nach $x$ sind auf $\mathbb{R}\times[0,1]$ stetig. Zweimal [(1.2)](#gl-1-2) gibt $F''(x)=\int_0^1\partial_x^2\mathrm{e}^{-xt}\,\mathrm{d} t=\int_0^1t^2\mathrm{e}^{-xt}\,\mathrm{d} t$. Aus $F(x)=(1-\mathrm{e}^{-x})/x$ folgt

$$F'(x)=\frac{(x+1)\mathrm{e}^{-x}-1}{x^2},\qquad F''(x)=\frac{2-(x^2+2x+2)\mathrm{e}^{-x}}{x^3}.$$

Bei $x=1$ ist also $\int_0^1t^2\mathrm{e}^{-t}\,\mathrm{d} t=2-\frac{5}{\mathrm{e}}\approx0{,}161$.
:::
:::

:::aufgabe Aufgabe 2 ★★ Die wandernde Spitze
<span class="anker" id="aufg-2"></span>

Auf $[0,1]\times[0,1]$ sei $f(x,t)=x/(x^2+t^2)$ für $(x,t)\neq(0,0)$ und $f(0,0)=0$.

<ol class="al">

<li>

Berechne $F(x)=\int_0^1f(x,t)\,\mathrm{d} t$ für $x>0$ und für $x=0$.

</li>

<li>

Ist $F$ bei $x=0$ stetig? Welche Voraussetzung des Satzes fehlt, und an wie vielen Punkten?

</li>

<li>

Was macht die Kurve $t\mapsto f(x,t)$ für $x\searrow0$ bei $t=0$? Warum geht dabei keine Fläche verloren?

</li>

</ol>

:::loesung
(a) Für $x>0$ ist $F(x)=\bigl[\arctan(t/x)\bigr]_{t=0}^{1}=\arctan(1/x)$. Für $x=0$ ist $f(0,t)=0$ für alle $t$, also $F(0)=0$. (b) $\lim_{x\searrow0}F(x)=\frac\pi2\neq0=F(0)$. $F$ ist unstetig. Es fehlt die Stetigkeit von $f$, und zwar in dem einen Punkt $(0,0)$: Dort hat $f$ keinen Grenzwert, denn $f(x,0)=1/x$ wächst, während $f(0,t)=0$ ist. (c) Bei $t=0$ entsteht eine Spitze der Höhe $1/x$ und der Breite von der Größenordnung $x$. Ihre Fläche bleibt fast $\frac\pi2$. Für $x=0$ ist die Spitze weg, ihre Fläche springt auf null.
:::
:::
