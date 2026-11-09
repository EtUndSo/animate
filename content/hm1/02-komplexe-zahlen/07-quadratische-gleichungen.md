---
title: Stufe 6: Quadratische Gleichungen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Komplexe Zahlen
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
Die Regel $\sqrt{ab}=\sqrt a\sqrt b$ aus [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) gilt nur für $a,b\ge0$. Für negative Zahlen ist die Wurzel nicht definiert: $w^2=-1$ hat zwei gleichberechtigte Lösungen, keine davon ist „die“ Wurzel. Deshalb schreibt dieses Kapitel $w^2=D$ und nicht $w=\sqrt D$.
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

**Ausblick.** Ein Punkt der Ebene lässt sich auch durch Betrag und Winkel angeben. Dann werden beim Multiplizieren die Beträge multipliziert und die Winkel addiert, die Drehung aus Stufe [2](die-komplexe-ebene.html#stufe-2) ist der Sonderfall $|\mathrm{i}|=1$ und Winkel $90^\circ$. Diese __Polardarstellung__, die Exponentialform und die $n$-ten Wurzeln brauchen Sinus, Cosinus und die Exponentialfunktion und folgen deshalb in [Teil 7](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/potenzreihen-und-eulersche-formel/potenzreihen-und-eulersche-formel.html).
