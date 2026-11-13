---
title: Stufe 3: Körperaxiome
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
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

⁠**So liest man das:** $0$ und $1$ sind hier nur Namen für zwei ausgezeichnete Elemente. Minus und Geteilt sind keine eigenen Verknüpfungen: $x-y:=x+(-y)$, und $\frac yx:=y\cdot x^{-1}$. Vereinbart sind „Punkt vor Strich“ und $xy:=x\cdot y$. Was aus den Axiomen folgt, gilt in jedem Körper, also auch für die komplexen Zahlen in [Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Beispiele sind $\mathbb{Q}$ und $\mathbb{R}$. $\mathbb{N}$ ist keiner (keine 0, kein $-1$), $\mathbb{Z}$ auch nicht (2 hat kein Inverses). Der kleinste Körper ist $\{0,1\}$ mit $1+1=0$, die Addition der Digitaltechnik (XOR). **Warum die Voraussetzungen:** Ohne (NNE) wäre $\{0\}$ ein Körper. Ohne $x\ne0$ in (M4) wäre $1=0\cdot0^{-1}=0$ nach (iii) unten.

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
Für $\mathbb{Q}$ und $\mathbb{R}$ sind sie vertraut. Aber sie stehen nicht in den Axiomen, und erst der Beweis zeigt, wo sie gelten: in jedem Körper. Die Schulregel „Quadrate sind nicht negativ“ folgt dagegen nicht aus dieser Liste und fällt in [Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Außerdem übt man das Schließen an Inhalten, deren Ergebnis man kennt.
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

::::formelsammlung
**Körperaxiome der Addition**

$$x+y=y+x,\qquad x+(y+z)=(x+y)+z,\qquad x+0=x,\qquad x+(-x)=0$$

Für alle $x,y,z$ eines Körpers $\mathbb K$: (A1) kommutativ, (A2) assoziativ, (A3) es gibt ein neutrales Element $0\in\mathbb K$, (A4) zu jedem $x$ gibt es ein inverses Element $-x$.

**Körperaxiome der Multiplikation**

$$x\cdot y=y\cdot x,\qquad x\cdot(y\cdot z)=(x\cdot y)\cdot z,\qquad x\cdot1=x,\qquad x\cdot x^{-1}=1$$

(M1) bis (M4); das inverse Element $x^{-1}=\frac1x$ gibt es zu jedem $x\ne0$.

**Distributivgesetz und Nichttrivialität**

$$x\cdot(y+z)=(x\cdot y)+(x\cdot z),\qquad0\ne1$$

(AM) ist das einzige Bindeglied zwischen Plus und Mal, (NNE) schließt die Menge $\{0\}$ als Körper aus. $\mathbb{Q}$ und $\mathbb{R}$ sind Körper, $\mathbb{N}$ und $\mathbb{Z}$ nicht; der kleinste Körper ist $\{0,1\}$ mit $1+1=0$.

**Minus und Geteilt**

$$x-y:=x+(-y),\qquad\frac yx:=y\cdot x^{-1}$$

Keine eigenen Verknüpfungen; der Quotient für $x\ne0$. Vereinbart sind „Punkt vor Strich“ und $xy:=x\cdot y$.

**Eindeutige Inverse**

$$(xy=1\wedge xz=1)\Rightarrow y=z,\qquad(x+y=0\wedge x+z=0)\Rightarrow y=z$$

Erst damit sind die Schreibweisen $-x$ und $x^{-1}$ sinnvoll.

**Eindeutig lösbare Gleichungen**

$$x+z=y\ \Leftrightarrow\ z=y-x,\qquad xz=y\ \Leftrightarrow\ z=y\cdot x^{-1}=\frac yx$$

Die zweite für $x\ne0$; $y-x$ heißt Differenz, $\frac yx$ Quotient. $0\cdot z=1$ hat keine Lösung, $0\cdot z=0$ hat jedes $z$ als Lösung: Teilen durch null scheitert an der Existenz oder an der Eindeutigkeit.

**Null und Vorzeichen**

$$x\cdot0=0,\qquad-(-x)=x,\qquad(-x)(-y)=xy,\qquad(x^{-1})^{-1}=x$$

Die letzte Regel für $x\ne0$. Insbesondere $(-1)x=-x$ und $(-1)(-1)=1$.

**Produkt null**

$$xy=0\Rightarrow(x=0\vee y=0)$$

Deshalb zerlegt man eine Gleichung in Faktoren und setzt jeden Faktor null.

**Bruchrechnen**

$$\frac xu\cdot\frac yv=\frac{xy}{uv},\qquad\frac xu+\frac yv=\frac{xv+yu}{uv},\qquad\frac xu:\frac yv=\frac{xv}{uy}$$

Für $u,v\ne0$; die Division zusätzlich für $y\ne0$. Wie alle Regeln dieser Stufe gilt das in jedem Körper.
::::

::::lernkarten
:::karte begriff Verknüpfung
Was ist eine Verknüpfung auf einer Menge, wie es Plus und Mal in einem Körper sind?
---
Eine Vorschrift, die je zwei Elementen der Menge ein Element derselben Menge zuordnet.
--- falsch
Eine Vorschrift, die je zwei Elementen der Menge eine Aussage zuordnet, die wahr oder falsch ist.
--- falsch
Eine Vorschrift, die jedem einzelnen Element der Menge ein Element einer anderen Menge zuordnet.
--- falsch
Eine Vorschrift, die je zwei Elementen eine beliebige Zahl zuordnet, die auch außerhalb der Menge liegen darf.
:::
:::karte begriff Körper
Wann heißt eine Menge $\mathbb K$ mit zwei Verknüpfungen „$+$“ und „$\cdot$“ ein Körper?
---
Wenn für alle $x,y,z\in\mathbb K$ gilt: Plus und Mal sind kommutativ und assoziativ, es gibt $0$ mit $x+0=x$ und $1$ mit $x\cdot1=x$, zu jedem $x$ ein $-x$ und zu jedem $x\ne0$ ein $x^{-1}$; dazu das Distributivgesetz (AM) und $0\ne1$ (NNE).
--- falsch
Wenn für alle $x,y,z\in\mathbb K$ gilt: Plus und Mal sind kommutativ und assoziativ, es gibt $0$ mit $x+0=x$ und $1$ mit $x\cdot1=x$, und jedes $x$ hat ein $-x$ und ein $x^{-1}$, auch $x=0$; das Distributivgesetz folgt dann von selbst.
--- falsch
Wenn $\mathbb K$ die Zahlen $0$ und $1$ enthält und mit je zwei Zahlen auch ihre Summe und ihr Produkt. Inverse Elemente werden nicht verlangt, deshalb ist zum Beispiel auch $\mathbb{Z}$ ein Körper.
--- falsch
Wenn für alle $x,y,z\in\mathbb K$ gilt: Plus und Mal sind kommutativ und assoziativ, es gibt $0$ und $1$, zu jedem $x$ ein $-x$, zu jedem $x\ne0$ ein $x^{-1}$, und zusätzlich sind Quadrate nie negativ.
:::
:::karte formel Distributivgesetz
Wie lautet das Distributivgesetz (AM), und welche Rolle spielt es unter den Körperaxiomen?
---
$x\cdot(y+z)=(x\cdot y)+(x\cdot z)$. Es ist das einzige Axiom, das Plus und Mal verbindet; fast alle Rechenregeln im Körper werden darüber bewiesen.
--- falsch
$x+(y\cdot z)=(x+y)\cdot(x+z)$. Es ist das einzige Axiom, das Plus und Mal verbindet; fast alle Rechenregeln im Körper werden darüber bewiesen.
--- falsch
$x\cdot(y+z)=(x\cdot y)+(x\cdot z)$. Es folgt aus der Kommutativität und Assoziativität von Plus und Mal und wird deshalb in den Beweisen nur selten gebraucht.
--- falsch
$x\cdot(y\cdot z)=(x\cdot y)\cdot z$. Es ist das einzige Axiom, das Plus und Mal verbindet; fast alle Rechenregeln im Körper werden darüber bewiesen.
:::
:::karte zusammenhang Welche Zahlbereiche Körper sind
Welche der Zahlbereiche $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ sind Körper, und woran scheitern die anderen?
---
$\mathbb{Q}$ und $\mathbb{R}$ sind Körper. $\mathbb{N}$ ist keiner, weil die $0$ und $-1$ fehlen; $\mathbb{Z}$ ist keiner, weil $2$ kein Inverses für die Multiplikation hat.
--- falsch
Alle vier sind Körper, weil man in jedem von ihnen addieren und multiplizieren kann und dabei die bekannten Rechenregeln gelten.
--- falsch
Nur $\mathbb{R}$ ist ein Körper. $\mathbb{Q}$ scheitert, weil $2$ dort kein Inverses für die Multiplikation hat; $\mathbb{N}$ und $\mathbb{Z}$ scheitern, weil die $0$ fehlt.
--- falsch
$\mathbb{Z}$, $\mathbb{Q}$ und $\mathbb{R}$ sind Körper. Nur $\mathbb{N}$ ist keiner, weil die $0$ und $-1$ fehlen; in $\mathbb{Z}$ hat dagegen jede Zahl ihr Negatives.
:::
:::karte zusammenhang kleinster Körper
Welcher Körper ist der kleinste, und was gilt darin für $1+1$?
---
Der Körper $\{0,1\}$ mit $1+1=0$ und $1\cdot1=1$; seine Addition ist die XOR-Verknüpfung der Digitaltechnik. Darin ist $-1=1$.
--- falsch
Der Körper $\{0\}$ mit $0+0=0$ und $0\cdot0=0$; er erfüllt alle Axiome, weil sein einziges Element zugleich neutral und invers ist.
--- falsch
Der Körper $\{0,1\}$ mit $1+1=2$; weil $2$ nicht in der Menge liegt, ist die Addition nur für $0+0$, $0+1$ und $1+0$ erklärt.
--- falsch
Der Körper $\{-1,0,1\}$ mit $1+1=-1$; mit weniger als drei Elementen hätte die $1$ kein additiv inverses Element.
:::
:::karte zusammenhang Voraussetzungen der Körperaxiome
Wozu verlangen die Körperaxiome $0\ne1$ (NNE) und in (M4) die Einschränkung $x\ne0$?
---
Ohne (NNE) wäre die Menge $\{0\}$ ein Körper. Ohne $x\ne0$ in (M4) hätte auch $0$ ein Inverses, und wegen $x\cdot0=0$ folgte $1=0\cdot0^{-1}=0$.
--- falsch
Ohne (NNE) könnte man Plus und Mal nicht unterscheiden. Die Einschränkung $x\ne0$ dient nur der Bequemlichkeit, weil $0^{-1}$ ein unhandlicher Wert wäre.
--- falsch
Beide Bedingungen folgen aus den übrigen Axiomen und stehen nur zur Erinnerung in der Liste. Man könnte sie streichen, ohne dass sich etwas ändert.
--- falsch
Ohne (NNE) wäre $\mathbb{Q}$ kein Körper, weil $0$ und $1$ dort zusammenfielen. Ohne $x\ne0$ wäre $0^{-1}=0$, und das Distributivgesetz wäre verletzt.
:::
:::karte begriff Differenz und Quotient
Was sind Differenz und Quotient in einem Körper, in dem Minus und Geteilt keine eigenen Verknüpfungen sind?
---
Mit $x-y:=x+(-y)$ und $\frac yx:=y\cdot x^{-1}$ ist die Differenz $z=y-x$ die einzige Lösung von $x+z=y$ und der Quotient $z=\frac yx$ für $x\ne0$ die einzige Lösung von $xz=y$.
--- falsch
Zwei eigene Verknüpfungen neben Plus und Mal, für die eigene Axiome gelten: Die Differenz ist kommutativ wie die Summe, und der Quotient ist auch für $x=0$ erklärt.
--- falsch
Mit $x-y:=x+(-y)$ und $\frac yx:=y\cdot x^{-1}$ ist die Differenz $z=x-y$ die einzige Lösung von $x+z=y$ und der Quotient $z=\frac xy$ für jedes $x$ die einzige Lösung von $xz=y$.
--- falsch
Mit $x-y:=x+(-y)$ und $\frac yx:=y\cdot x^{-1}$ ist $z=y-x$ die einzige Lösung von $x+z=y$; der Quotient $z=\frac yx$ löst $xz=y$ für jedes $x$, ist für $x=0$ aber nicht eindeutig.
:::
:::karte zusammenhang Eindeutigkeit der Inversen
Warum ist es wichtig, dass Inverse im Körper eindeutig sind, also $(xy=1\wedge xz=1)\Rightarrow y=z$ gilt?
---
Weil erst die Eindeutigkeit die Schreibweisen $-x$ und $x^{-1}$ sinnvoll macht: Gäbe es zwei Inverse, wüsste man nicht, welches gemeint ist. Die Axiome verlangen nur, dass es eines gibt.
--- falsch
Weil die Axiome (A4) und (M4) die Eindeutigkeit ausdrücklich fordern und man sie deshalb in jedem Beweis zitieren muss; sie ist kein Satz, sondern eine eigene Annahme der Liste.
--- falsch
Weil sonst die Addition nicht kommutativ wäre: Zwei verschiedene Inverse $y$ und $z$ von $x$ ergäben $x+y\ne y+x$, und (A1) wäre verletzt.
--- falsch
Weil man ohne die Eindeutigkeit nicht durch null teilen könnte: Erst die Eindeutigkeit der Inversen sichert, dass auch $0^{-1}$ einen festen Wert hat.
:::
:::karte herleitung Produkt mit null
Wie beweist man $x\cdot0=0$ allein aus den Körperaxiomen?
---
Man schreibt $x\cdot0=(x\cdot0)+0$ und ersetzt die $0$ durch $(x\cdot0)+(-(x\cdot0))$, weil $0$ nach (A3) neutral ist und $x\cdot0$ nach (A4) ein Negatives hat.
---
Man klammert um zu $\bigl((x\cdot0)+(x\cdot0)\bigr)+(-(x\cdot0))$, weil die Addition nach (A2) assoziativ ist.
---
Man fasst $(x\cdot0)+(x\cdot0)$ zu $x\cdot(0+0)=x\cdot0$ zusammen, weil das Distributivgesetz (AM) gilt und $0+0=0$ nach (A3) ist.
---
Es bleibt $(x\cdot0)+(-(x\cdot0))=0$, weil eine Zahl plus ihr Negatives nach (A4) null ergibt.
:::
:::karte herleitung Minus mal Minus
Wie folgt $(-1)(-1)=1$ und damit $(-x)(-y)=xy$ aus den Körperaxiomen?
---
Es gilt $x+(-1)x=(1+(-1))x=0\cdot x=0$, weil man nach dem Distributivgesetz ausklammern darf und $x\cdot0=0$ schon bewiesen ist; also ist $(-1)x=-x$, weil das additive Inverse eindeutig ist.
---
Ebenso ist $(-1)+(-1)(-1)=(-1)(1+(-1))=(-1)\cdot0=0$, weil man $-1$ ausklammern darf; also ist $(-1)(-1)$ additiv invers zu $-1$.
---
Deshalb ist $(-1)(-1)=-(-1)=1$, weil $(-1)(-1)$, $-(-1)$ und $1$ alle additiv invers zu $-1$ sind und das Inverse eindeutig ist.
---
Schließlich ist $(-x)(-y)=(-1)(-1)xy=xy$, weil $-x=(-1)x$ und $-y=(-1)y$ gilt und man nach (M1) und (M2) umordnen darf.
:::
:::karte formel Produkt null
Was folgt in einem Körper aus $xy=0$, und wozu nutzt man das beim Lösen von Gleichungen?
---
$xy=0\Rightarrow(x=0\vee y=0)$: Ist $x\ne0$, dann ist $y=x^{-1}(xy)=x^{-1}\cdot0=0$. Deshalb zerlegt man eine Gleichung in Faktoren und setzt jeden Faktor null.
--- falsch
$xy=0\Rightarrow(x=0\wedge y=0)$: Beide Faktoren müssen null sein, weil ein Faktor ungleich null das Produkt nie zu null machen kann. Man setzt alle Faktoren zugleich null.
--- falsch
$xy=0\Rightarrow(x=0\vee y=0)$ gilt nur in $\mathbb{Q}$ und $\mathbb{R}$, nicht in jedem Körper, weil man dafür die Anordnung der Zahlen braucht; im Allgemeinen fehlt die Regel.
--- falsch
$xy=0\Rightarrow x=y$: Zwei Zahlen mit Produkt null sind gleich. Deshalb setzt man beim Lösen einer Gleichung die einzelnen Faktoren einander gleich.
:::
:::karte zusammenhang Teilen durch null
Woran scheitert das Teilen durch null, also das Lösen von $0\cdot z=y$?
---
An der Existenz oder an der Eindeutigkeit: Wegen $x\cdot0=0$ hat $0\cdot z=1$ keine Lösung, und $0\cdot z=0$ hat jedes $z$ als Lösung.
--- falsch
Nur an der Existenz: $0\cdot z=y$ hat für kein $y$ eine Lösung, auch nicht für $y=0$, weil null mal etwas gar nicht definiert ist.
--- falsch
Nur an einer Vereinbarung: Man könnte $\frac10$ als neue Zahl einführen, ohne dass ein Körperaxiom verletzt wird; es ist nur nicht üblich.
--- falsch
Nur an der Eindeutigkeit: $0\cdot z=y$ hat für jedes $y$ unendlich viele Lösungen, und man weiß nicht, welche davon gemeint ist.
:::
:::karte formel Bruchrechnen
Wie multipliziert, addiert und dividiert man Brüche in einem Körper, und unter welchen Bedingungen?
---
Für $u,v\ne0$ gilt $\frac xu\cdot\frac yv=\frac{xy}{uv}$ und $\frac xu+\frac yv=\frac{xv+yu}{uv}$; für $u,v,y\ne0$ gilt $\frac xu:\frac yv=\frac{xv}{uy}$.
--- falsch
Für $u,v\ne0$ gilt $\frac xu\cdot\frac yv=\frac{xy}{uv}$ und $\frac xu+\frac yv=\frac{x+y}{u+v}$; für $u,v,y\ne0$ gilt $\frac xu:\frac yv=\frac{xv}{uy}$.
--- falsch
Für $u,v\ne0$ gilt $\frac xu\cdot\frac yv=\frac{xv}{uy}$ und $\frac xu+\frac yv=\frac{xv+yu}{uv}$; für $u,v,y\ne0$ gilt $\frac xu:\frac yv=\frac{xy}{uv}$.
--- falsch
Für alle $u,v$ gilt $\frac xu\cdot\frac yv=\frac{xy}{uv}$ und $\frac xu+\frac yv=\frac{xv+yu}{uv}$; diese Regeln gelten aber nur in $\mathbb{Q}$, nicht in jedem Körper.
:::
:::karte zusammenhang Rechenregeln beweisen
Warum beweist man vertraute Rechenregeln wie $(-1)\cdot(-1)=1$ aus den Körperaxiomen, statt sie aus der Schule zu übernehmen?
---
Weil sie nicht in den Axiomen stehen und erst der Beweis zeigt, wo sie gelten: in jedem Körper. „Quadrate sind nicht negativ“ folgt dagegen nicht aus den Körperaxiomen.
--- falsch
Weil die Schulregeln manchmal falsch sind: In $\mathbb{R}$ gilt zum Beispiel $(-1)\cdot(-1)=-1$, und erst der Beweis aus den Axiomen liefert das richtige Ergebnis $1$ für jeden Körper.
--- falsch
Weil der Beweis zeigt, dass die Regeln nur in $\mathbb{Q}$ und $\mathbb{R}$ gelten. In jedem anderen Körper muss man jede Rechenregel neu festlegen und eigens prüfen, ob sie dort stimmt.
--- falsch
Weil alle Schulregeln aus den Körperaxiomen folgen, auch „Quadrate sind nicht negativ“; erst der Beweis macht sie für jeden Körper gültig, auch für die komplexen Zahlen.
:::
::::
