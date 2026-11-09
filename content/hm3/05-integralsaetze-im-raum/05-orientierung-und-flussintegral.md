---
title: Stufe 4: Orientierung und Flussintegral
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3150500
summary: Wie viel eines Felds durch eine Fläche strömt, hängt davon ab, welche Seite als „vorn“ gilt.
tags: Orientierung, Flussintegral
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Wie viel eines Felds durch eine Fläche strömt, hängt davon ab, welche Seite als „vorn“ gilt. Diese Stufe legt die Seite fest und definiert den Fluss.
:::

**Die Idee.** Stell dir ein Netz in einem Wasserstrom vor. Durch das Netz fließt nur der Anteil der Strömung, der senkrecht auf ihm steht, parallel zum Netz läuft das Wasser vorbei. Für ein Flächenstück $\mathrm{d}\sigma$ mit Normale $\boldsymbol{n}$ ist der Durchfluss also $\boldsymbol{F}\cdot\boldsymbol{n}\,\mathrm{d}\sigma$. Das Vorzeichen sagt, in welche Richtung es geht, relativ zur gewählten Normale. Diese Wahl heißt __Orientierung__.

Das Normalenfeld $\boldsymbol{n}=(\boldsymbol{x}_u\times\boldsymbol{x}_v)/|\boldsymbol{x}_u\times\boldsymbol{x}_v|$ aus [(1.2)](flachen-beschreiben.html#gl-1-2) hängt bis auf das Vorzeichen nicht von der Parametrisierung ab. Vertauscht man $u$ und $v$, kehrt es sich um. Aus jeder Parametrisierung lässt sich so eine machen, die zur gewünschten Orientierung passt.

:::definition Definition 4.1 (Flussintegral)
<span class="anker" id="satz-4-1"></span>

Sei $\mathcal F$ orientiert mit Normalenfeld $\boldsymbol{n}$ und $\boldsymbol{F}$ stetig in einer Umgebung von $\mathcal F$. Dann heißt

<span class="anker" id="gl-4-1"></span>
$$\int_{\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}:=\int_{\mathcal F}\boldsymbol{F}\cdot\boldsymbol{n}\;\mathrm{d}\sigma \tag{4.1}$$

das __Flussintegral__. Für eine zur Orientierung passende Parametrisierung gilt

<span class="anker" id="gl-4-2"></span>
$$\int_{\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=\int_B\boldsymbol{F}(\boldsymbol{x}(u,v))\cdot(\boldsymbol{x}_u\times\boldsymbol{x}_v)\;\mathrm{d} u\,\mathrm{d} v. \tag{4.2}$$
:::

⁠**So liest man das:** In [(4.2)](#gl-4-2) kürzt sich der Betrag aus $\boldsymbol{n}$ gegen den aus $\mathrm{d}\sigma$. Man braucht also keine Wurzel, und das macht die Rechnung bequem: Flussintegrale sind meist leichter als Oberflächenintegrale.

::::beispiel
Fluss von $\boldsymbol{F}=(-y,x,2z)$ durch die Kuppel nach oben. Mit [(1.3)](flachen-beschreiben.html#gl-1-3) zeigt $\Phi_r\times\Phi_\varphi$ nach oben, weil die letzte Komponente $r>0$ ist. Das Skalarprodukt ist

$$\boldsymbol{F}\cdot(\Phi_r\times\Phi_\varphi)=-r\sin\varphi\cdot2r^2\cos\varphi+r\cos\varphi\cdot2r^2\sin\varphi+2(4-r^2)\,r=2r(4-r^2).$$

Die Drehanteile heben sich weg, denn sie laufen längs der Fläche. Es bleibt $\int_0^{2\pi}\!\int_0^22r(4-r^2)\,\mathrm{d} r\,\mathrm{d}\varphi=2\pi\cdot8=16\pi$.
::::

:::frage Zeigt $\boldsymbol{x}_u\times\boldsymbol{x}_v$ automatisch nach außen?
Nein. Es zeigt dorthin, wohin es die Reihenfolge der Parameter bestimmt. Bei der Kugel mit $(\theta,\varphi)$ zeigt $\boldsymbol{x}_\theta\times\boldsymbol{x}_\varphi$ nach außen, bei $(\varphi,\theta)$ nach innen. Prüfe immer an einem Punkt, ob das Vorzeichen zur verlangten Orientierung passt.
:::

:::aufgabe Aufgabe 6 ★★ Fluss durch die Halbkugel
<span class="anker" id="aufg-6"></span>

Berechne den Fluss von $\boldsymbol{F}=(0,0,z)$ durch die obere Halbkugel $|\boldsymbol{x}|=2$, $z\ge0$, nach außen. Was ändert sich, wenn $\boldsymbol{n}$ nach innen zeigt?

:::loesung
In Kugelkoordinaten ist $\boldsymbol{n}=\boldsymbol{x}/2$, also $\boldsymbol{F}\cdot\boldsymbol{n}=z^2/2$ mit $z=2\cos\theta$, und $\mathrm{d}\sigma=4\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$:

$$\int\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=\int_0^{2\pi}\!\!\int_0^{\pi/2}2\cos^2\theta\cdot4\sin\theta\;\mathrm{d}\theta\,\mathrm{d}\varphi=2\pi\cdot8\cdot\frac13=\frac{16\pi}{3}\approx16{,}8.$$

Mit $\boldsymbol{n}$ nach innen ändert sich nur das Vorzeichen. Kontrolle mit Gauß: $\operatorname{div}\boldsymbol{F}=1$, die Halbkugel hat das Volumen $\frac23\pi\cdot8=\frac{16\pi}{3}$, und durch den Boden fließt nichts, weil dort $z=0$ ist.
:::
:::
