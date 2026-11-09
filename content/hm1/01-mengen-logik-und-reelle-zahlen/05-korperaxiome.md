---
title: Stufe 3: Körperaxiome
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
order: 1210500
summary: Welche wenigen Regeln für Plus und Mal muss man annehmen, damit alle anderen Rechenregeln beweisbar sind?
tags: Verknüpfung, Distributivgesetz, Differenz, Quotient
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Welche wenigen Regeln für Plus und Mal muss man annehmen, damit alle anderen Rechenregeln beweisbar sind?
:::

**Die Idee.** Jeder Zahlbereich entsteht, weil im vorigen eine Gleichung keine Lösung hat (Abb. [3](#abb-3)): $x+3=1$ hat in $\mathbb{N}$ keine Lösung, $3x=1$ nicht in $\mathbb{Z}$. Ein Körper ist der Bereich, in dem beide Gleichungstypen immer lösbar sind: Plus und Mal lassen sich umkehren. Mehr verlangen die Axiome nicht. Das einzige Bindeglied zwischen Plus und Mal ist das Distributivgesetz, und fast alle Beweise dieser Stufe laufen darüber.

:::abbildung hm1/k1zahlbereiche 3
Jede Gleichung ist erst in dem Bereich lösbar, in dem sie steht.
:::

:::definition Definition 3.1 (Körper)
<span class="anker" id="satz-3-1"></span>

Eine __Verknüpfung__ ordnet je zwei Elementen ein Element derselben Menge zu. Eine Menge $\mathbb K$ mit zwei Verknüpfungen „$+$“ und „$\cdot$“ heißt Körper, wenn für alle $x,y,z\in\mathbb K$ gilt:

|  | Addition | Multiplikation |
|---|---|---|
| kommutativ | (A1) $x+y=y+x$ | (M1) $x\cdot y=y\cdot x$ |
| assoziativ | (A2) $x+(y+z)=(x+y)+z$ | (M2) $x\cdot(y\cdot z)=(x\cdot y)\cdot z$ |
| neutrales Element | (A3) Es gibt $0\in\mathbb K$ mit $x+0=x$ für alle $x$. | (M3) Es gibt $1\in\mathbb K$ mit $x\cdot1=x$ für alle $x$. |
| inverses Element | (A4) Zu jedem $x$ gibt es $y$ mit $x+y=0$, geschrieben $-x$. | (M4) Zu jedem $x\ne0$ gibt es $y$ mit $x\cdot y=1$, geschrieben $x^{-1}$ oder $\frac1x$. |

Dazu kommen (AM) $x\cdot(y+z)=(x\cdot y)+(x\cdot z)$ (__Distributivgesetz__) und (NNE) $0\ne1$.
:::

⁠**So liest man das:** $0$ und $1$ sind hier nur Namen für zwei ausgezeichnete Elemente. Minus und Geteilt sind keine eigenen Verknüpfungen: $x-y:=x+(-y)$, und $\frac yx:=y\cdot x^{-1}$. Vereinbart sind „Punkt vor Strich“ und $xy:=x\cdot y$. Was aus den Axiomen folgt, gilt in jedem Körper, also auch für die komplexen Zahlen in [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Beispiele sind $\mathbb{Q}$ und $\mathbb{R}$. $\mathbb{N}$ ist keiner (keine 0, kein $-1$), $\mathbb{Z}$ auch nicht (2 hat kein Inverses). Der kleinste Körper ist $\{0,1\}$ mit $1+1=0$, die Addition der Digitaltechnik (XOR). **Warum die Voraussetzungen:** Ohne (NNE) wäre $\{0\}$ ein Körper. Ohne $x\ne0$ in (M4) wäre $1=0\cdot0^{-1}=0$ nach (iii) unten.

:::satz Satz 3.2 (Rechenregeln im Körper)
<span class="anker" id="satz-3-2"></span>

Für alle $x,y,z,u,v\in\mathbb K$ gilt:

<ol class="rm">

<li>

Inverse sind eindeutig: $(xy=1\wedge xz=1)\Rightarrow y=z$ und $(x+y=0\wedge x+z=0)\Rightarrow y=z$.

</li>

<li>

Gleichungen sind eindeutig lösbar: $x+z=y$ hat genau die Lösung $z=y-x$ (__Differenz__). $xz=y$ hat für $x\ne0$ genau die Lösung $z=y\cdot x^{-1}=\frac yx$ (__Quotient__).

</li>

<li>

$x\cdot0=0$, und für $x\ne0$ ist $(x^{-1})^{-1}=x$.

</li>

<li>

$-(-x)=x$ und $(-x)(-y)=xy$.

</li>

<li>

$xy=0\Rightarrow(x=0\vee y=0)$.

</li>

<li>

Für $u,v\ne0$ gilt $\frac xu\cdot\frac yv=\frac{xy}{uv}$ und $\frac xu+\frac yv=\frac{xv+yu}{uv}$, und für $u,v,y\ne0$ gilt $\frac xu:\frac yv=\frac{xv}{uy}$.

</li>

</ol>
:::

⁠**So liest man das:** Erst (i) macht die Schreibweisen $-x$ und $x^{-1}$ sinnvoll: Gäbe es zwei Inverse, wüsste man nicht, welches gemeint ist. (v) ist der Grund, warum man eine Gleichung in Faktoren zerlegt und jeden Faktor null setzt. **Warum $x\ne0$:** $0\cdot z=1$ hat nach (iii) keine Lösung, $0\cdot z=0$ hat jedes $z$ als Lösung. Teilen durch null scheitert an der Existenz oder an der Eindeutigkeit.

:::beweis Rechenregeln, jeder Schritt mit Axiom
(i) Aus $xy=xz$ (beide sind 1) folgt durch Multiplikation mit $y$: $(xy)y=(xz)y$. Links steht $1\cdot y=y$ (M1, M3). Rechts: $(xz)y\overset{\text{M2}}{=}x(zy)\overset{\text{M1}}{=}x(yz)\overset{\text{M2}}{=}(xy)z=1\cdot z=z$. Für die Addition geht es genauso (Aufgabe [4](#aufg-4)).

(ii) Existenz: $x(yx^{-1})=x(x^{-1}y)=(xx^{-1})y=1\cdot y=y$ (M1, M2, M4, M3). Eindeutigkeit: Aus $xz=x\tilde z$ folgt nach Multiplikation mit $x^{-1}$ über dieselben Axiome $z=\tilde z$. Für die Addition ebenso mit $-x$.

(iii) $x\cdot0\overset{\text{A3}}{=}(x\cdot0)+0\overset{\text{A4}}{=}(x\cdot0)+\bigl((x\cdot0)+(-(x\cdot0))\bigr)\overset{\text{A2}}{=}\bigl((x\cdot0)+(x\cdot0)\bigr)+(-(x\cdot0))\overset{\text{AM}}{=}x\cdot(0+0)+(-(x\cdot0))\overset{\text{A3}}{=}(x\cdot0)+(-(x\cdot0))\overset{\text{A4}}{=}0$. Für $x\ne0$ ist $x^{-1}\ne0$ (indirekt: aus $x^{-1}=0$ folgte $1=xx^{-1}=x\cdot0=0$, gegen NNE). Also hat $x^{-1}$ ein Inverses. Es ist $(x^{-1})^{-1}x^{-1}=1$ und $x\,x^{-1}=1$, nach (i) stimmen $x$ und $(x^{-1})^{-1}$ überein.

(iv) $x$ und $-(-x)$ sind beide additiv invers zu $-x$, nach (i) gleich. Weiter ist $x+(-1)x=(1+(-1))x=0\cdot x=0$, also $(-1)x=-x$. Aus $(-1)+(-1)(-1)=(-1)(1+(-1))=(-1)\cdot0=0$ folgt ebenso, dass $(-1)(-1)$ invers zu $-1$ ist, also $(-1)(-1)=-(-1)=1$. Damit $(-x)(-y)=(-1)(-1)xy=xy$.

(v) Ist $x\ne0$, dann $y=x^{-1}(xy)=x^{-1}\cdot0=0$.

(vi) $\frac xu\cdot\frac yv=(xu^{-1})(yv^{-1})=(xy)(u^{-1}v^{-1})$, und $u^{-1}v^{-1}=(uv)^{-1}$, denn $(u^{-1}v^{-1})(uv)=1$ und das Inverse ist eindeutig. Die Divisionsregel folgt mit $(y v^{-1})^{-1}=y^{-1}v$, die Summenregel durch Erweitern: $\frac xu=\frac{xv}{uv}$, $\frac yv=\frac{yu}{uv}$, dann (AM).
:::

::::beispiel
$(-3)(-5)=15$, $\frac23+\frac57=\frac{14+15}{21}=\frac{29}{21}$, $\frac34:\frac58=\frac{3\cdot8}{4\cdot5}=\frac65$.
::::

⁠**Grenzfall** $v=u=1$: Die Summenregel wird zu $x+y=x+y$.

:::frage Das weiß ich aus der Schule. Wozu ein Beweis?
Für $\mathbb{Q}$ und $\mathbb{R}$ sind sie vertraut. Aber sie stehen nicht in den Axiomen, und erst der Beweis zeigt, wo sie gelten: in jedem Körper. Die Schulregel „Quadrate sind nicht negativ“ folgt dagegen nicht aus dieser Liste und fällt in [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Außerdem übt man das Schließen an Inhalten, deren Ergebnis man kennt.
:::

:::aufgabe Aufgabe 4 ★★ Beweisen im Körper
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Zeige: $(x+y=0\wedge x+z=0)\Rightarrow y=z$. Gib zu jedem Schritt das Axiom an.

</li>

<li>

Zeige $(x+y)(x-y)=x^2-y^2$ und nenne, wo (AM) und (M1) gebraucht werden.

</li>

<li>

Im Körper $\{0,1\}$ mit $1+1=0$ und $1\cdot1=1$: Was ist $-1$? Prüfe $(-1)(-1)=1$.

</li>

</ol>

:::loesung
(a) Aus $x+y=0=x+z$ folgt $(-x)+(x+y)=(-x)+(x+z)$. Mit (A2), (A1), (A4) wird das zu $0+y=0+z$, mit (A1), (A3) zu $y=z$. (b) (AM) und (M1): $(x+y)(x-y)=(x+y)x+(x+y)(-y)=x^2+yx-xy-y^2=x^2-y^2$, wobei $yx=xy$ nach (M1) und $(x+y)(-y)=-(x+y)y$ nach $(-1)x=-x$. (c) $1+1=0$ heißt $-1=1$. Dann $(-1)(-1)=1\cdot1=1$. Das ist die Regel aus Satz [3.2](#satz-3-2), sie gilt in jedem Körper.
:::
:::
