---
title: Stufe 6: Quadratische Gleichungen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Komplexe Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Kapitel 2: Komplexe Zahlen
order: 1220700
summary: Das Ziel war eine Lösung von x 2=-1 .
tags: doppelte Lösung, Diskriminante, Polardarstellung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Das Ziel war eine Lösung von $x^2=-1$. Diese Stufe zeigt, dass $\mathbb{C}$ mehr leistet: Jede quadratische Gleichung ist dort lösbar, auch mit komplexen Vorfaktoren.
:::

**Die Idee.** Quadratisches Ergänzen benutzt nur Körperaxiome und gilt deshalb in $\mathbb{C}$. Es bleibt eine Gleichung $w^2=D$ übrig. In $\mathbb{R}$ scheitert sie an $D<0$. In $\mathbb{C}$ scheitert sie nie: $w^2=D$ zerfällt in Realteil und Imaginärteil, also in zwei reelle Gleichungen für die zwei reellen Unbekannten von $w$.

:::satz Satz 6.1 (Quadratwurzeln in $\mathbb{C}$)
<span class="anker" id="satz-6-1"></span>

Sei $D=s+\mathrm{i}t\ne0$ mit $s,t\in\mathbb{R}$. Für $w=u+\mathrm{i}v$ mit reellen $u,v$ ist $w^2=D$ gleichwertig mit $u^2-v^2=s$ und $2uv=t$. Es gibt genau zwei Lösungen $\pm w$, und zwar mit

<span class="anker" id="gl-6-1"></span>
$$u^2=\frac{|D|+s}2,\qquad v^2=\frac{|D|-s}2. \tag{6.1}$$

Die Vorzeichen von $u$ und $v$ sind so zu wählen, dass $2uv=t$ gilt. Für $D=0$ ist $w=0$ die einzige Lösung.
:::

⁠**So liest man das:** $s$ und $t$ sind Realteil und Imaginärteil von $D$. Ist $t>0$, haben $u$ und $v$ gleiche Vorzeichen, ist $t<0$, verschiedene. **Grenzfall:** Für reelles $D<0$ wird $u=0$ und $v^2=-D$: Die Lösungen sind rein imaginär, für $D=-1$ also $w=\pm\mathrm{i}$.

:::beweis Zwei reelle Gleichungen
Es ist $w^2=u^2-v^2+2\mathrm{i}uv$. Der Vergleich von Realteil und Imaginärteil gibt die beiden Gleichungen. Aus $|w|^2=|w^2|=|D|$ folgt zusätzlich $u^2+v^2=|D|$. Addieren und Subtrahieren mit $u^2-v^2=s$ ergibt [(6.1)](#gl-6-1). Die rechten Seiten sind nicht negativ, denn $|s|\le|D|$ (Stufe [5](betrag-und-abstand.html#stufe-5), Regel (v)). Umgekehrt erfüllen $u,v$ aus [(6.1)](#gl-6-1) die Gleichung $u^2-v^2=s$ und $(2uv)^2=(|D|+s)(|D|-s)=|D|^2-s^2=t^2$. Also ist $2uv=\pm t$, und die Wahl der Vorzeichen legt $2uv=t$ fest.
:::

:::satz Satz 6.2 (Quadratische Gleichung in $\mathbb{C}$)
<span class="anker" id="satz-6-2"></span>

Seien $p,q\in\mathbb{C}$ und $D:=p^2/4-q$. Die Gleichung $z^2+pz+q=0$ hat die Lösungen

<span class="anker" id="gl-6-2"></span>
$$z=-\frac p2\pm w\qquad\text{mit}\qquad w^2=D. \tag{6.2}$$

Für $D\ne0$ sind das zwei Lösungen $z_+\ne z_-$ mit $z_++z_-=-p$ und $z_+z_-=q$. Für $D=0$ gibt es nur $z=-p/2$, eine __doppelte Lösung__. Für reelle $p,q$ gilt: $D>0$ ergibt zwei reelle Lösungen, $D=0$ eine reelle, $D<0$ die zueinander konjugierten Lösungen $z=-\frac p2\pm\mathrm{i}\sqrt{-D}$.
:::

⁠**So liest man das:** $D$ heißt __Diskriminante__. Die Lösungen liegen punktsymmetrisch zur Mitte $-p/2$ (Abb. [6](#abb-6)). **Gültigkeit:** Der Vorfaktor von $z^2$ muss 1 sein. Sonst teilt man vorher durch ihn, das geht in $\mathbb{C}$ auch bei einem komplexen Vorfaktor $\ne0$. Reelle Gleichungen dieser Art beschreiben Schwingungen: Ein konjugiertes Lösungspaar steht für eine gedämpfte Schwingung.

:::herleitung Quadratisches Ergänzen
Es gilt $z^2+pz+q=(z+\frac p2)^2-\frac{p^2}4+q=(z+\frac p2)^2-w^2=(z+\frac p2-w)(z+\frac p2+w)$. Ein Produkt ist nur dann null, wenn ein Faktor null ist (Stufe [4](dividieren-und-was-verloren-geht.html#stufe-4)). Das ergibt [(6.2)](#gl-6-2), und es folgt $z_++z_-=-p$ und $z_+z_-=\frac{p^2}4-w^2=q$. Bei reellen $p,q$ ist $D$ reell, und für $D<0$ ist $w=\pm\mathrm{i}\sqrt{-D}$.
:::

:::abbildung hm1/k2loesungen 6
Links die reelle Gleichung des Rechenmodells: Die Lösungen $3\pm\mathrm{i}$ sind gespiegelt. Rechts die komplexe Gleichung: $z_1$ und $z_2$ liegen symmetrisch zur Mitte $2+1{,}5\mathrm{i}$.
:::

::::beispiel [Beispiel 1] reelle Vorfaktoren
$z^2-6z+10=0$ hat $p=-6$, $q=10$, $D=9-10=-1$, also $z=3\pm\mathrm{i}$. Das sind $z_1$ und $\overline{z_1}$. Probe: Summe $6=-p$, Produkt $|z_1|^2=10=q$.
::::

::::beispiel [Beispiel 2] komplexe Vorfaktoren
Für $z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$ ist $-p/2=2+1{,}5\mathrm{i}$ und

$$D=(2+1{,}5\mathrm{i})^2-(1+7\mathrm{i})=1{,}75+6\mathrm{i}-1-7\mathrm{i}=0{,}75-\mathrm{i}.$$

Also ist $s=0{,}75$, $t=-1$ und $|D|=\sqrt{0{,}5625+1}=1{,}25$. Aus [(6.1)](#gl-6-1) folgt $u^2=1$ und $v^2=0{,}25$. Wegen $t<0$ haben $u$ und $v$ verschiedene Vorzeichen: $w=\pm(1-0{,}5\mathrm{i})$. Damit ist $z=2+1{,}5\mathrm{i}\pm(1-0{,}5\mathrm{i})$, also $z=3+\mathrm{i}$ oder $z=1+2\mathrm{i}$. Probe: Summe $4+3\mathrm{i}=-p$, Produkt $1+7\mathrm{i}=q$.
::::

⁠**Grenzfall:** Für $q=0$ gibt [(6.2)](#gl-6-2) $z=-p/2\pm p/2$, also $z=0$ und $z=-p$, passend zu $z(z+p)=0$.

:::frage Warum darf man nicht $\sqrt{-1}\cdot\sqrt{-1}=\sqrt{(-1)(-1)}=1$ rechnen?
Die Regel $\sqrt{ab}=\sqrt a\sqrt b$ aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) gilt nur für $a,b\ge0$. Für negative Zahlen ist die Wurzel nicht definiert: $w^2=-1$ hat zwei gleichberechtigte Lösungen, keine davon ist „die“ Wurzel. Deshalb schreibt dieses Kapitel $w^2=D$ und nicht $w=\sqrt D$.
:::

:::aufgabe Aufgabe 8 ★★ Quadratische Gleichungen lösen
<span class="anker" id="aufg-8"></span>

(a) Löse $z^2+4z+13=0$ und prüfe Summe und Produkt. (b) $z^2+pz+q=0$ mit reellen $p,q$ hat die Lösung $2-5\mathrm{i}$. Wie heißt die zweite Lösung, wie groß sind $p$ und $q$? (c) Löse $z^2-3z+3-\mathrm{i}=0$ und mache die Probe. (d) Löse $\mathrm{i}z^2+2z-2\mathrm{i}=0$.

:::loesung
(a) $D=4-13=-9$, also $z=-2\pm3\mathrm{i}$. Summe $-4=-p$, Produkt $4+9=13=q$. (b) Bei reellen Vorfaktoren ist die zweite Lösung die konjugierte, $2+5\mathrm{i}$. Dann ist $p=-(2-5\mathrm{i})-(2+5\mathrm{i})=-4$ und $q=(2-5\mathrm{i})(2+5\mathrm{i})=29$.

(c) $p=-3$, $q=3-\mathrm{i}$, also $D=2{,}25-3+\mathrm{i}=-0{,}75+\mathrm{i}$. Mit $|D|=\sqrt{0{,}5625+1}=1{,}25$ gibt [(6.1)](#gl-6-1) $u^2=0{,}25$ und $v^2=1$. Wegen $t=1>0$ haben $u$ und $v$ gleiche Vorzeichen: $w=\pm(0{,}5+\mathrm{i})$. Also ist $z=1{,}5\pm(0{,}5+\mathrm{i})$, das heißt $z=2+\mathrm{i}$ oder $z=1-\mathrm{i}$. Probe: Summe $3=-p$, Produkt $(2+\mathrm{i})(1-\mathrm{i})=2-2\mathrm{i}+\mathrm{i}-\mathrm{i}^2=3-\mathrm{i}=q$.

(d) Zuerst den Vorfaktor von $z^2$ auf 1 bringen: Division durch $\mathrm{i}$ mit $1/\mathrm{i}=-\mathrm{i}$ gibt $z^2-2\mathrm{i}z-2=0$. Also ist $p=-2\mathrm{i}$, $q=-2$ und $D=(-2\mathrm{i})^2/4+2=-1+2=1$. Mit $w=\pm1$ folgt $z=\mathrm{i}\pm1$. Probe für $z=1+\mathrm{i}$: $\mathrm{i}\cdot2\mathrm{i}+2+2\mathrm{i}-2\mathrm{i}=-2+2=0$. Probe für $z=-1+\mathrm{i}$: $\mathrm{i}\cdot(-2\mathrm{i})-2+2\mathrm{i}-2\mathrm{i}=2-2=0$.
:::
:::

**Ausblick.** Ein Punkt der Ebene lässt sich auch durch Betrag und Winkel angeben. Dann werden beim Multiplizieren die Beträge multipliziert und die Winkel addiert, die Drehung aus Stufe [2](die-komplexe-ebene.html#stufe-2) ist der Sonderfall $|\mathrm{i}|=1$ und Winkel $90^\circ$. Diese __Polardarstellung__, die Exponentialform und die $n$-ten Wurzeln brauchen Sinus, Cosinus und die Exponentialfunktion und folgen deshalb in [Kapitel 7](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/potenzreihen-und-eulersche-formel/potenzreihen-und-eulersche-formel.html).

::::formelsammlung
**Quadratwurzeln in $\mathbb{C}$**

$$u^2=\frac{|D|+s}2,\qquad v^2=\frac{|D|-s}2$$

Für $D=s+\mathrm{i}t\ne0$ mit $s,t\in\mathbb{R}$ ist $w^2=D$ mit $w=u+\mathrm{i}v$ gleichwertig mit $u^2-v^2=s$ und $2uv=t$. Es gibt genau zwei Lösungen $\pm w$; die Vorzeichen von $u$ und $v$ so wählen, dass $2uv=t$ gilt ($t>0$: gleiche, $t<0$: verschiedene). Für $D=0$ ist $w=0$ die einzige Lösung. Man schreibt $w^2=D$, nicht $w=\sqrt D$: $\sqrt{ab}=\sqrt a\sqrt b$ gilt nur für $a,b\ge0$.

**Quadratische Gleichung**

$$z=-\frac p2\pm w\qquad\text{mit}\qquad w^2=D$$

Lösungen von $z^2+pz+q=0$ mit $p,q\in\mathbb{C}$ und der Diskriminante $D:=p^2/4-q$. Für $D=0$ nur $z=-p/2$, eine doppelte Lösung. Der Vorfaktor von $z^2$ muss 1 sein, sonst vorher durch ihn teilen.

**Quadratisches Ergänzen**

$$z^2+pz+q=(z+\frac p2)^2-\frac{p^2}4+q=(z+\frac p2)^2-w^2=(z+\frac p2-w)(z+\frac p2+w)$$

Benutzt nur Körperaxiome und gilt deshalb in $\mathbb{C}$; ein Produkt ist nur dann null, wenn ein Faktor null ist.

**Summe und Produkt der Lösungen**

$$z_++z_-=-p,\qquad z_+z_-=q$$

Für die Lösungen $z_\pm=-\frac p2\pm w$; dient als Probe.

**Reelle Vorfaktoren**

$$z=-\frac p2\pm\mathrm{i}\sqrt{-D}$$

Für reelle $p,q$ mit $D<0$: zwei zueinander konjugierte Lösungen. $D>0$ ergibt zwei reelle Lösungen, $D=0$ eine reelle.
::::

::::lernkarten
:::karte zusammenhang zwei reelle Unbekannte
Warum ist die Gleichung $w^2=D$ in $\mathbb{C}$ immer lösbar, während sie in $\mathbb{R}$ für $D<0$ keine Lösung hat?
---
Weil $w^2=D$ in $\mathbb{C}$ in zwei reelle Gleichungen zerfällt, für Realteil und Imaginärteil, mit den zwei reellen Unbekannten von $w$; die sind stets lösbar. In $\mathbb{R}$ ist ein Quadrat nie negativ.
--- falsch
Weil man in $\mathbb{C}$ aus negativen Zahlen die Wurzel nach der Regel $\sqrt{ab}=\sqrt a\sqrt b$ ziehen darf: Man zerlegt $D=(-1)\cdot(-D)$ und nimmt die Wurzeln der beiden Faktoren einzeln, eine davon ist $\mathrm{i}$.
--- falsch
Weil in $\mathbb{C}$ jedes Quadrat negativ sein darf: Für alle nicht reellen $w$ ist $w^2$ negativ reell, und genau diese negativen Werte von $D$ fehlen in $\mathbb{R}$, die übrigen deckt schon $\mathbb{R}$ ab.
--- falsch
Weil $\mathbb{C}$ angeordnet ist und man $w$ deshalb durch Intervallschachtelung zwischen immer engeren Schranken einfangen kann, so wie man in $\mathbb{R}$ die Wurzel aus 2 findet.
:::
:::karte formel Quadratwurzeln in C
Wie findet man die Lösungen $w=u+\mathrm{i}v$ von $w^2=D$ für $D=s+\mathrm{i}t\ne0$ mit reellen $s$, $t$?
---
Aus $u^2=\frac{|D|+s}2$ und $v^2=\frac{|D|-s}2$; die Vorzeichen von $u$ und $v$ wählt man so, dass $2uv=t$ gilt. Es gibt genau zwei Lösungen $\pm w$.
--- falsch
Aus $u^2=\frac{|D|+t}2$ und $v^2=\frac{|D|-t}2$; die Vorzeichen von $u$ und $v$ wählt man so, dass $u^2-v^2=s$ gilt. Es gibt genau zwei Lösungen $\pm w$.
--- falsch
Indem man Realteil und Imaginärteil einzeln radiziert, also $u$ aus $u^2=s$ und $v$ aus $v^2=t$; das geht für $s,t\ge0$. Für negative $s$ oder $t$ gibt es keine Lösung.
--- falsch
Aus $u^2=\frac{|D|+s}2$ und $v^2=\frac{|D|-s}2$; die Vorzeichen von $u$ und $v$ sind frei wählbar. Es gibt deshalb genau vier Lösungen, alle Kombinationen von $\pm u$ und $\pm v$.
:::
:::karte zusammenhang Wahl der Vorzeichen
Wie wählt man die Vorzeichen von $u$ und $v$ in $w=u+\mathrm{i}v$ mit $w^2=s+\mathrm{i}t$, und warum ist diese Wahl nötig?
---
Bei $t>0$ gleiche, bei $t<0$ verschiedene Vorzeichen, damit $2uv=t$ gilt. Die Formeln für $u^2$ und $v^2$ liefern nur $(2uv)^2=t^2$, also $2uv=\pm t$; erst die Wahl der Vorzeichen legt $2uv=t$ fest.
--- falsch
Immer beide positiv, weil eine Wurzel nie negativ ist. Die zweite Lösung $-w$ entsteht erst danach, indem man nur das Vorzeichen von $u$ umdreht und $v$ unverändert lässt.
--- falsch
Bei $s>0$ gleiche, bei $s<0$ verschiedene Vorzeichen, damit $u^2-v^2=s$ gilt. Der Imaginärteil $t$ spielt für die Vorzeichen keine Rolle, er bestimmt nur die Größe von $v$.
--- falsch
Bei $t>0$ verschiedene, bei $t<0$ gleiche Vorzeichen, damit $2uv=-t$ gilt. Das Minus gleicht das $\mathrm{i}^2$ aus, das beim Quadrieren von $w$ im Imaginärteil entsteht.
:::
:::karte herleitung Zwei reelle Gleichungen
Wie gewinnt man aus $w^2=D$ mit $w=u+\mathrm{i}v$ und $D=s+\mathrm{i}t$ die Formeln $u^2=\frac{|D|+s}2$ und $v^2=\frac{|D|-s}2$?
---
Es ist $w^2=u^2-v^2+2\mathrm{i}uv$; der Vergleich von Realteil und Imaginärteil gibt $u^2-v^2=s$ und $2uv=t$, weil eine Gleichung in $\mathbb{C}$ für zwei reelle Gleichungen steht.
---
Aus $|w|^2=|w^2|=|D|$ folgt zusätzlich $u^2+v^2=|D|$, weil der Betrag eines Produkts das Produkt der Beträge ist.
---
Addieren und Subtrahieren mit $u^2-v^2=s$ ergibt die beiden Formeln, weil dabei einmal $v^2$ und einmal $u^2$ wegfällt.
---
Die rechten Seiten sind nicht negativ, weil $|s|\le|D|$ gilt: Der Betrag ist mindestens so groß wie der Betrag des Realteils.
---
Umgekehrt gilt $(2uv)^2=(|D|+s)(|D|-s)=|D|^2-s^2=t^2$, also $2uv=\pm t$, weil nach der Definition des Betrags $|D|^2=s^2+t^2$ ist; die Wahl der Vorzeichen legt $2uv=t$ fest.
:::
:::karte formel Quadratische Gleichung
Wie lauten die Lösungen der Gleichung $z^2+pz+q=0$ mit $p,q\in\mathbb{C}$?
---
$z=-\frac p2\pm w$ mit $w^2=D$, wobei $D:=p^2/4-q$. Für $D\ne0$ sind das zwei verschiedene Lösungen, für $D=0$ nur $z=-p/2$; der Vorfaktor von $z^2$ muss 1 sein.
--- falsch
$z=-\frac p2\pm w$ mit $w^2=D$, wobei $D:=p^2/4-q$; das gilt aber nur für reelle $p,q$. Bei komplexen Vorfaktoren gibt es keine Lösungsformel, und man muss die Lösungen durch Probieren suchen.
--- falsch
$z=\frac p2\pm w$ mit $w^2=D$, wobei $D:=p^2/4+q$. Für $D\ne0$ sind das zwei verschiedene Lösungen, für $D=0$ nur $z=p/2$; der Vorfaktor von $z^2$ muss 1 sein.
--- falsch
$z=-\frac p2\pm w$ mit $w^2=D$, wobei $D:=p^2/4-q$. Für reelles $D$ sind das zwei Lösungen; für nicht reelles $D$ hat die Gleichung keine Lösung, weil $w$ dann nicht existiert.
:::
:::karte begriff Diskriminante
Was ist die Diskriminante der Gleichung $z^2+pz+q=0$, und was entscheidet sie bei reellen $p,q$?
---
Die Zahl $D:=p^2/4-q$. Bei reellen $p,q$ gibt $D>0$ zwei reelle Lösungen, $D=0$ eine reelle und $D<0$ die zueinander konjugierten Lösungen $z=-\frac p2\pm\mathrm{i}\sqrt{-D}$.
--- falsch
Die Zahl $D:=p^2-4q$. Bei reellen $p,q$ gibt $D>0$ zwei reelle Lösungen, $D=0$ keine Lösung und $D<0$ zwei rein imaginäre Lösungen $z=\pm\mathrm{i}\sqrt{-D}$.
--- falsch
Die Zahl $D:=p^2/4-q$. Bei reellen $p,q$ gibt $D>0$ zwei reelle Lösungen, $D=0$ eine reelle und $D<0$ gar keine Lösung, auch nicht in den komplexen Zahlen.
--- falsch
Die Zahl $D:=p^2/4-q$. Bei reellen $p,q$ gibt $D<0$ zwei reelle Lösungen, $D=0$ eine reelle und $D>0$ die zueinander konjugierten Lösungen $z=-\frac p2\pm\mathrm{i}\sqrt{D}$.
:::
:::karte begriff doppelte Lösung
Wann hat die Gleichung $z^2+pz+q=0$ eine doppelte Lösung, und wie lautet sie?
---
Wenn die Diskriminante $D=p^2/4-q$ null ist. Dann ist $w=0$, die beiden Lösungen $-\frac p2\pm w$ fallen zusammen, und es gibt nur $z=-p/2$.
--- falsch
Wenn $q=0$ ist. Dann fallen beide Lösungen zusammen, und es gibt nur $z=-p$, weil sich die Gleichung zu $z(z+p)=0$ vereinfacht und der Faktor $z$ wegfällt.
--- falsch
Wenn die Diskriminante negativ ist. Dann gibt es zwei Lösungen, die als Spiegelbilder zusammengehören und deshalb zusammen als eine doppelte Lösung gezählt werden.
--- falsch
Wenn die Diskriminante null ist. Dann gibt es die doppelte Lösung $z=p/2$, weil sich die beiden Lösungen $\frac p2\pm w$ mit $w=0$ genau decken.
:::
:::karte herleitung Quadratisches Ergänzen
Wie folgt die Lösungsformel $z=-\frac p2\pm w$ mit $w^2=D$ für $z^2+pz+q=0$ aus dem quadratischen Ergänzen?
---
Es gilt $z^2+pz+q=(z+\frac p2)^2-\frac{p^2}4+q$, weil man $\frac{p^2}4$ ergänzt und wieder abzieht.
---
Mit $w^2=D$ und $D:=p^2/4-q$ ist das $(z+\frac p2)^2-w^2=(z+\frac p2-w)(z+\frac p2+w)$, weil die dritte binomische Formel in jedem Körper gilt.
---
Das Produkt ist nur dann null, wenn ein Faktor null ist, weil $\mathbb{C}$ ein Körper ist; also ist $z=-\frac p2+w$ oder $z=-\frac p2-w$.
---
Es folgt $z_++z_-=-p$ und $z_+z_-=\frac{p^2}4-w^2=q$, weil sich in der Summe $\pm w$ aufhebt und das Produkt wieder die dritte binomische Formel ist.
:::
:::karte formel Summe und Produkt der Lösungen
Wie hängen die beiden Lösungen $z_+$ und $z_-$ von $z^2+pz+q=0$ mit $p$ und $q$ zusammen, und wozu nutzt man das?
---
$z_++z_-=-p$ und $z_+z_-=q$. Damit macht man die Probe, etwa bei $z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$: Summe $4+3\mathrm{i}=-p$, Produkt $1+7\mathrm{i}=q$.
--- falsch
$z_++z_-=p$ und $z_+z_-=q$. Damit macht man die Probe: Die Summe der Lösungen ist der Vorfaktor von $z$, ihr Produkt ist das Glied ohne $z$.
--- falsch
$z_++z_-=-p$ und $z_+z_-=-q$. Damit macht man die Probe: Beide Vorfaktoren der Gleichung treten mit umgekehrtem Vorzeichen auf.
--- falsch
$z_++z_-=-p$ und $z_+z_-=q$, aber nur für reelle $p,q$. Bei komplexen Vorfaktoren hängen die Lösungen nicht so einfach mit $p$ und $q$ zusammen.
:::
:::karte zusammenhang konjugierte Lösungen
Warum sind die nicht reellen Lösungen einer quadratischen Gleichung $z^2+pz+q=0$ mit reellen $p,q$ zueinander konjugiert?
---
Weil für reelle $p,q$ auch $D$ reell ist und für $D<0$ die Lösungen $z=-\frac p2\pm\mathrm{i}\sqrt{-D}$ lauten: gleicher Realteil $-p/2$, entgegengesetzte Imaginärteile, also Spiegelbilder.
--- falsch
Weil jede quadratische Gleichung zueinander konjugierte Lösungen hat, auch mit komplexen $p,q$; das folgt daraus, dass $\mathrm{i}$ und $-\mathrm{i}$ beide die Gleichung $x^2=-1$ lösen.
--- falsch
Weil für $D<0$ die Lösungen $z=\pm\mathrm{i}\sqrt{-D}$ lauten und damit rein imaginär sind; Spiegelbilder an der reellen Achse sind sie, weil ihr Realteil null ist.
--- falsch
Weil für reelle $p,q$ die beiden Lösungen stets reell sind; zueinander konjugiert sind sie, weil jede reelle Zahl ihre eigene konjugierte Zahl ist und die Spiegelung sie nicht verändert.
:::
:::karte zusammenhang Vorfaktor gleich 1
Was tut man bei einer Gleichung wie $\mathrm{i}z^2+2z-2\mathrm{i}=0$, bevor man die Lösungsformel anwendet?
---
Man teilt durch den Vorfaktor von $z^2$, damit er 1 wird; in $\mathbb{C}$ geht das auch bei einem komplexen Vorfaktor $\ne0$. Mit $1/\mathrm{i}=-\mathrm{i}$ entsteht hier $z^2-2\mathrm{i}z-2=0$.
--- falsch
Nichts: Die Lösungsformel gilt für jeden Vorfaktor von $z^2$. Man setzt $p=2$ und $q=-2\mathrm{i}$ ein und lässt das $\mathrm{i}$ vor $z^2$ einfach weg, weil es nur die Lage der Lösungen dreht.
--- falsch
Man multipliziert mit $\mathrm{i}$, damit der Vorfaktor reell wird; das ergibt $-z^2+2\mathrm{i}z+2=0$, und darauf wendet man die Lösungsformel mit $p=2\mathrm{i}$ und $q=2$ an.
--- falsch
Man teilt durch den Vorfaktor von $z^2$, aber nur, wenn er reell ist. Bei einem komplexen Vorfaktor wie $\mathrm{i}$ hat die Gleichung keine Lösung in Normalform.
:::
:::karte zusammenhang Wurzel aus negativen Zahlen
Warum darf man in $\mathbb{C}$ nicht $\sqrt{-1}\cdot\sqrt{-1}=\sqrt{(-1)(-1)}=1$ rechnen?
---
Weil $\sqrt{ab}=\sqrt a\sqrt b$ nur für $a,b\ge0$ gilt. Für negative Zahlen ist die Wurzel nicht definiert: $w^2=-1$ hat zwei gleichberechtigte Lösungen, keine ist „die“ Wurzel.
--- falsch
Man darf es: Die Rechnung ist richtig, und $\mathrm{i}^2=-1$ gilt nur in der Elektrotechnik, wo man $\mathrm{j}$ statt $\mathrm{i}$ schreibt und mit anderen Regeln rechnet.
--- falsch
Weil $\sqrt{-1}$ zwar gleich $\mathrm{i}$ ist, aber $\sqrt{(-1)(-1)}$ den Wert $-1$ hat; beim Zusammenfassen unter einer Wurzel bleibt das Minus der Faktoren erhalten.
--- falsch
Weil die Regel $\sqrt{ab}=\sqrt a\sqrt b$ nur für verschiedene Faktoren $a\ne b$ gilt. Für gleiche Faktoren muss man $\sqrt a\cdot\sqrt a=a$ verwenden, und das ergibt hier $-1$.
:::
:::karte begriff Polardarstellung
Wie gibt die Polardarstellung einen Punkt der komplexen Ebene an, und was geschieht darin beim Multiplizieren?
---
Durch Betrag und Winkel statt durch Realteil und Imaginärteil. Beim Multiplizieren werden die Beträge multipliziert und die Winkel addiert; die Drehung durch $\mathrm{i}$ ist der Sonderfall Betrag 1, Winkel $90^\circ$.
--- falsch
Durch Betrag und Winkel statt durch Realteil und Imaginärteil. Beim Multiplizieren werden die Beträge addiert und die Winkel multipliziert; die Drehung durch $\mathrm{i}$ ist der Sonderfall Betrag 0, Winkel $90^\circ$.
--- falsch
Durch Realteil und Winkel statt durch Realteil und Imaginärteil. Beim Multiplizieren werden die Realteile multipliziert und die Winkel addiert; $\mathrm{i}$ hat darin den Realteil 1 und den Winkel $90^\circ$.
--- falsch
Durch Betrag und Winkel statt durch Realteil und Imaginärteil. Beim Multiplizieren werden Beträge und Winkel jeweils multipliziert; die Drehung durch $\mathrm{i}$ ist der Sonderfall Betrag 1, Winkel $90^\circ$.
:::
::::
