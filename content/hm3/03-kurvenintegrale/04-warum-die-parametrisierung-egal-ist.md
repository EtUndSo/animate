---
title: Stufe 3: Warum die Parametrisierung egal ist
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Kurvenintegrale
adresse: elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale
knoten: Kapitel 3: Kurvenintegrale
order: 3130400
summary: Dieselbe Kurve lässt sich schnell oder langsam durchlaufen.
tags: Parameterinvarianz, Umparametrisierung, Durchlaufsinn, reguläre Kurve, Orientierung
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Dieselbe Kurve lässt sich schnell oder langsam durchlaufen. Das Integral soll aber zur Kurve gehören, nicht zur gewählten Formel. Diese Stufe zeigt, warum das stimmt und wo der Durchlaufsinn ins Spiel kommt.
:::

**Die Idee.** Durchläuft man dieselbe Kurve doppelt so schnell, ist der Tangentenvektor doppelt so lang, der Integrand $\boldsymbol{F}\cdot\dot\gamma$ also doppelt so groß. Dafür dauert jedes Stück nur halb so lange. Tempo und Dauer heben sich im Integral auf, und zwar auf jedem Stück einzeln, auch wenn das Tempo schwankt (Abb. [3](#abb-3)). Dass der Wert nicht von der Parametrisierung abhängt, heißt __Parameterinvarianz__. Läuft man dagegen rückwärts, zeigt $\dot\gamma$ überall in die Gegenrichtung.

:::abbildung hm3/k3invarianz 3
Derselbe Viertelkreis dreimal. Die Punkte gehören zu gleich großen Schritten im Parameter. Links liegen sie gleichmäßig, in der Mitte am Anfang dicht und am Ende weit auseinander: Kurve und Kurvenintegral bleiben dieselben. Rechts läuft die Kurve rückwärts, das Integral wechselt das Vorzeichen.
:::

:::satz Satz 3.1 (Parameterinvarianz bei Kurven)
<span class="anker" id="satz-3-1"></span>

Sei $\gamma:[a,b]\to\mathbb{R}^n$ regulär parametrisiert, $\boldsymbol{F}$ stetig längs $\gamma$ und $\tau:[c,d]\to[a,b]$ stetig differenzierbar und streng monoton. Für die __Umparametrisierung__ $\tilde\gamma=\gamma\circ\tau$ mit dem Parameter $u$ gilt:

<ul>

<li>

Ist $\tau$ wachsend mit $\tau(c)=a$, $\tau(d)=b$, dann ist $\int_{\tilde\gamma}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$.

</li>

<li>

Ist $\tau$ fallend mit $\tau(c)=b$, $\tau(d)=a$, dann ist $\int_{\tilde\gamma}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=-\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$.

</li>

<li>

In beiden Fällen ist $\int_{\tilde\gamma}f\,\mathrm{d} s=\int_\gamma f\,\mathrm{d} s$ für das Integral über die Bogenlänge.

</li>

</ul>
:::

:::beweis Parameterinvarianz bei Kurven
Die Kettenregel gibt $\frac{\mathrm{d}}{\mathrm{d} u}\tilde\gamma(u)=\dot\gamma(\tau(u))\,\tau'(u)$. Mit der Substitution $t=\tau(u)$, $\mathrm{d} t=\tau'(u)\,\mathrm{d} u$ folgt

$$\int_c^d\boldsymbol{F}(\gamma(\tau(u)))\cdot\dot\gamma(\tau(u))\,\tau'(u)\,\mathrm{d} u=\int_{\tau(c)}^{\tau(d)}\boldsymbol{F}(\gamma(t))\cdot\dot\gamma(t)\,\mathrm{d} t.$$

Ist $\tau$ wachsend, sind die Grenzen $a$ und $b$. Ist $\tau$ fallend, sind sie vertauscht, und das gibt ein Minus. Bei der Bogenlänge steht $|\frac{\mathrm{d}}{\mathrm{d} u}\tilde\gamma|=|\dot\gamma\circ\tau|\,|\tau'|$. Für fallendes $\tau$ ist $|\tau'|=-\tau'$, und dieses Minus hebt das Minus aus den vertauschten Grenzen auf. Bei Knicken rechnet man auf jedem Stück einzeln.
:::

⁠**So liest man das:** $\tau'(u)$ gibt an, wie schnell die neue Kurve die alte abläuft. Die Kettenregel stellt diesen Tempofaktor in den Integranden, und die Substitution verbraucht ihn wieder in $\mathrm{d} t=\tau'(u)\,\mathrm{d} u$. Das ist die Aufhebung von Tempo und Dauer als Rechnung.

Das *Arbeitsintegral* $\int\boldsymbol{F}\cdot\dot\gamma\,\mathrm{d} t$ fragt, in welche Richtung man läuft, deshalb zählt der __Durchlaufsinn__. Das *Integral über die Bogenlänge* $\int f\,|\dot\gamma|\,\mathrm{d} t$ fragt nur, wie lang das Stück ist:

| Integral | Tempo ändern | Richtung umkehren |
|---|---|---|
| Arbeit $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ | gleich | Vorzeichen wechselt |
| Bogenlänge $\int_\gamma f\,\mathrm{d} s$, Länge $\mathcal L$ | gleich | gleich |

Die rückwärts durchlaufene Kurve ist $\gamma^-(t):=\gamma(a+b-t)$ auf $[a,b]$, also $\gamma\circ\tau$ mit dem fallenden $\tau(t)=a+b-t$. Was das Feld auf dem Hinweg leistet, nimmt es auf dem Rückweg wieder weg.

**Beispiel.** Viertelkreis und $\boldsymbol V$ ergaben $\pi/2$. Mit $\tau(u)=\frac\pi2u^2$, $0\le u\le1$, ist der Integrand $\tau'(u)=\pi u$, und $\int_0^1\pi u\,\mathrm{d} u=\pi/2$. Mit $\tau(u)=\frac\pi2-u$, $0\le u\le\frac\pi2$, läuft die Kurve rückwärts, es kommt $-\pi/2$ heraus. Die Länge bleibt in beiden Fällen $\pi/2$.

:::frage Liefert also jede Parametrisierung derselben Spur denselben Wert?
Nein, nur eine, die jeden Punkt gleich oft durchläuft. Läuft $(\cos t,\sin t)$ auf $[0,4\pi]$, verdoppelt sich das Integral, für $\boldsymbol V$ von $2\pi$ auf $4\pi$. Das ist keine Umparametrisierung des einfachen Kreises: Dort ist jeder Punkt einmal dran, hier zweimal, und ein streng monotones $\tau$ ändert das nicht.
:::

**Kurven ohne Parameter.** Eine Menge $\Gamma\subset\mathbb{R}^n$ heißt __reguläre Kurve__, wenn sie Spur einer regulären und einfachen Parametrisierung ist. Man schreibt dann oft $\boldsymbol{x}=\boldsymbol{x}(t)$ statt $\gamma(t)$ und

<span class="anker" id="gl-3-1"></span>
$$\int_\Gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_a^b\boldsymbol{F}(\boldsymbol{x}(t))\cdot\dot{\boldsymbol{x}}(t)\,\mathrm{d} t. \tag{3.1}$$

Nach dem Satz hängt der Wert nicht von der gewählten einfachen Parametrisierung ab, solange der Durchlaufsinn bleibt. Deshalb ordnet man jeder regulären Kurve eine feste __Orientierung__ zu, also einen Durchlaufsinn. $-\Gamma$ ist die entgegengesetzt durchlaufene Kurve. Zu $\gamma_1\oplus\gamma_2$ gehört $\Gamma_1+\Gamma_2$, und $\Gamma_1-\Gamma_2$ steht für $\Gamma_1+(-\Gamma_2)$. Es gilt

<span class="anker" id="gl-3-2"></span>
$$\int_{\Gamma_1\pm\Gamma_2}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\Gamma_1}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}\pm\int_{\Gamma_2}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}. \tag{3.2}$$

Bei einer geschlossenen Kurve hängt das Integral auch nicht vom Anfangspunkt ab: Ein anderer Startpunkt teilt die Runde in zwei Stücke und vertauscht nur die Reihenfolge der beiden Summanden.

:::aufgabe Aufgabe 3 ★★ Dasselbe Integral, zwei Beschreibungen
<span class="anker" id="aufg-3"></span>

Sei $\boldsymbol{F}(x,y)=(y,\,2x)$ und $\gamma(t)=(t,t^2)$, $0\le t\le1$.

<ol class="al">

<li>

Berechne $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ direkt und mit $\tau(u)=u^3$, $0\le u\le1$.

</li>

<li>

Was ergibt sich für $\gamma_1(t)=(1-t,(1-t)^2)$, $0\le t\le1$? Welches $\tau$ gehört dazu?

</li>

<li>

Berechne $\int_\gamma x\,\mathrm{d} s$ und $\int_{\gamma_1}x\,\mathrm{d} s$. Warum kippt hier kein Vorzeichen?

</li>

</ol>

:::loesung
(a) $\boldsymbol{F}\cdot\dot\gamma=(t^2,2t)\cdot(1,2t)=5t^2$, das Integral ist $\frac53$. Mit $\tilde\gamma(u)=(u^3,u^6)$ ist $(u^6,2u^3)\cdot(3u^2,6u^5)=15u^8$, das Integral ist wieder $\frac53$. (b) $\gamma_1=\gamma\circ\tau$ mit $\tau(t)=1-t$, fallend. Also $-\frac53$. (c) $\int_\gamma x\,\mathrm{d} s=\int_0^1t\sqrt{1+4t^2}\,\mathrm{d} t=\bigl[\frac1{12}(1+4t^2)^{3/2}\bigr]_0^1=\frac{5\sqrt5-1}{12}\approx0{,}848$. Für $\gamma_1$ kommt mit $w=1-t$ dasselbe heraus. In $|\dot\gamma|$ geht die Richtung nicht ein.
:::
:::
