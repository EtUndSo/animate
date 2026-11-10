---
title: Stufe 5: Warum die Parametrisierung egal ist
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Integralsätze im Raum
adresse: elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum
knoten: Kapitel 5: Integralsätze im Raum
order: 3150600
summary: Eine Fläche lässt sich auf viele Arten parametrisieren.
tags: Parameterinvarianz
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Eine Fläche lässt sich auf viele Arten parametrisieren. Ein Integral soll aber zur Fläche gehören, nicht zur gewählten Beschreibung. Bei Kurven hat das [Kapitel 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html) gezeigt. Diese Stufe überträgt es auf Flächen und zeigt, wo die Orientierung ins Spiel kommt.
:::

**Die Idee.** Bei Kurven heben sich Tempo und Dauer im Integral auf ([Kapitel 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html)). Bei Flächen ist es genauso: Ein dichteres Gitter hat kleinere Zellen, dafür mehr davon, und große Zellen zählen entsprechend mehr (Abb. [3](#abb-3)). Dass der Wert nicht von der Parametrisierung abhängt, heißt __Parameterinvarianz__.

:::abbildung hm3/k5invarianz 3
Dieselbe Kreisscheibe mit zwei Gittern. Links die Parameter $(x,y)$, rechts $(r,\varphi)$. Die Zellen sehen verschieden aus, zusammen ergeben sie denselben Inhalt.
:::

**Der Satz.** Sei $\psi:B'\to B$ bijektiv und in beide Richtungen stetig differenzierbar, und sei $\boldsymbol{y}=\boldsymbol{x}\circ\psi$ mit den Parametern $(s,t)\in B'$. Mit [(2.2)](das-oberflachenelement.html#gl-2-2) und dem Transformationssatz ist

$$\int_{B'}f(\boldsymbol{y})\sqrt{\det\boldsymbol{g}'}\;\mathrm{d} s\,\mathrm{d} t=\int_{B'}f(\boldsymbol{x}\circ\psi)\sqrt{\det(\boldsymbol{g}\circ\psi)}\;|\det D\psi|\;\mathrm{d} s\,\mathrm{d} t=\int_Bf(\boldsymbol{x})\sqrt{\det\boldsymbol{g}}\;\mathrm{d} u\,\mathrm{d} v.$$

Der Faktor $|\det D\psi|$ im Oberflächenelement ist genau der Faktor des Transformationssatzes. $\int_{\mathcal F}f\,\mathrm{d}\sigma$ hängt also nicht von der Parametrisierung ab.

Beim Fluss zählt zusätzlich die Richtung. Aus $\boldsymbol{y}_s=\boldsymbol{x}_uu_s+\boldsymbol{x}_vv_s$ und $\boldsymbol{y}_t=\boldsymbol{x}_uu_t+\boldsymbol{x}_vv_t$ folgt

<span class="anker" id="gl-5-1"></span>
$$\boldsymbol{y}_s\times\boldsymbol{y}_t=(u_sv_t-v_su_t)\;\boldsymbol{x}_u\times\boldsymbol{x}_v=\det D\psi\;\,(\boldsymbol{x}_u\times\boldsymbol{x}_v)\circ\psi. \tag{5.1}$$

Für $\det D\psi>0$ bleibt die Normale erhalten, und der Fluss ändert sich nicht. Für $\det D\psi<0$ dreht sich die Normale um, und der Fluss wechselt das Vorzeichen.

| Integral | Richtung bleibt | Richtung kehrt um |
|---|---|---|
| $\int f\,\vert \dot\gamma\vert \,\mathrm{d} t$ und $\int_{\mathcal F}f\,\mathrm{d}\sigma$ | gleich | gleich |
| $\int\boldsymbol{F}\cdot\dot\gamma\,\mathrm{d} t$ und $\int_{\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$ | gleich | Vorzeichen wechselt |

::::beispiel Fläche
Die Kuppel aus Stufe [2](das-oberflachenelement.html#stufe-2) als Graph über $(x,y)$ hat das Oberflächenelement $\sqrt{1+4x^2+4y^2}\;\mathrm{d} x\,\mathrm{d} y$. In der Parametrisierung $(r,\varphi)$ war es $r\sqrt{1+4r^2}\;\mathrm{d} r\,\mathrm{d}\varphi$. Der Wechsel $(x,y)=(r\cos\varphi,r\sin\varphi)$ hat $\det D\psi=r$, und genau dieser Faktor unterscheidet beide Ausdrücke. Beide Rechnungen geben $\frac\pi6(17\sqrt{17}-1)\approx36{,}2$.
::::

:::frage Liefert also jede Parametrisierung denselben Wert?
Nein, $\psi$ muss bijektiv sein, die Fläche also genau einmal überdeckt werden. Lässt man in den Kugelkoordinaten $\varphi$ von 0 bis $4\pi$ laufen, wird die Kugel doppelt gezählt, und der Inhalt verdoppelt sich.
:::

:::frage Wozu ist das in der Praxis gut?
Man darf die bequemste Beschreibung wählen. Eine Kuppel rechnet man in Polarkoordinaten, ein Graph über $(x,y)$, und das Ergebnis ist trotzdem eine Eigenschaft der Fläche. Erst dadurch ist $\int_{\mathcal F}f\,\mathrm{d}\sigma$ überhaupt sinnvoll definiert.
:::

:::aufgabe Aufgabe 7 ★★ Dieselbe Fläche, zwei Beschreibungen
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Berechne den Inhalt des Kegelmantels $z=\sqrt{x^2+y^2}$, $0\le z\le1$, einmal als Graph über $(x,y)$ und einmal mit $\Phi(r,\varphi)=(r\cos\varphi,r\sin\varphi,r)$. Welcher Faktor verbindet beide Oberflächenelemente?

</li>

<li>

Berechne den Fluss von $\boldsymbol{F}=(0,0,1)$ durch die Einheitskreisscheibe in der Ebene $z=0$ mit $\boldsymbol{x}(u,v)=(u,v,0)$ und mit $\boldsymbol{y}(s,t)=(t,s,0)$. Erkläre das Vorzeichen mit [(5.1)](#gl-5-1).

</li>

</ol>

:::loesung
(a) Als Graph ist $H=\sqrt{x^2+y^2}$, $|\nabla H|=1$, also $\mathrm{d}\sigma=\sqrt2\,\mathrm{d} x\,\mathrm{d} y$ und der Inhalt $\sqrt2\,\pi$. Mit $\Phi$ ist $|\Phi_r\times\Phi_\varphi|=\sqrt2\,r$, also $\int_0^{2\pi}\!\int_0^1\sqrt2\,r\,\mathrm{d} r\,\mathrm{d}\varphi=\sqrt2\,\pi$. Der Faktor ist $\det D\psi=r$ des Wechsels $(x,y)=(r\cos\varphi,r\sin\varphi)$. (b) $\boldsymbol{x}_u\times\boldsymbol{x}_v=(0,0,1)$ gibt den Fluss $\pi$. $\boldsymbol{y}_s\times\boldsymbol{y}_t=(0,0,-1)$ gibt $-\pi$. Der Wechsel $(u,v)=(t,s)$ vertauscht die Parameter, also ist $\det D\psi=-1$, und nach [(5.1)](#gl-5-1) dreht sich die Normale um.
:::
:::
