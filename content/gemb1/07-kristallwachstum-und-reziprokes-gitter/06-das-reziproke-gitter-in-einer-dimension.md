---
title: Stufe 4: Das reziproke Gitter in einer Dimension
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
order: 4170600
summary: Der Kristall ist fertig, und er ist periodisch.
tags: k-Raum, reziproke Gittervektoren, reduziertes Zonenschema
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Der Kristall ist fertig, und er ist periodisch. In [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) war das Kosinus-Band periodisch in $k$. Diese Stufe zeigt, warum das so sein muss und dass dahinter ein eigenes Gitter steht.
:::

**Die Idee.** Eine Kette tastet eine Welle nur an den Punkten $x_\ell=\ell a$ ab. Legt man zu $k$ den Betrag $2\pi/a$ hinzu, dreht sich die Phase von Punkt zu Punkt einmal mehr ganz herum. Das Gitter merkt davon nichts. Deshalb wiederholt sich alles, was von $k$ abhängt, mit der Periode $2\pi/a$. Trägt man Wellenzahlen auf einer Achse auf, dem __k-Raum__, bilden die Werte $0,\pm2\pi/a,\pm4\pi/a,\dots$ selbst ein Punktgitter. Reziprok heißt Kehrwert: großer Abstand im Ort, kleiner Abstand im $k$-Raum.

:::definition Definition 4.1 (Reziprokes Gitter der Kette)
<span class="anker" id="satz-4-1"></span>

Die Kette hat die Gittervektoren $R_\ell=\ell a$. Ihr reziprokes Gitter besteht aus allen Wellenzahlen $G$ mit

<span class="anker" id="gl-4-1"></span>
$$\mathrm{e}^{\mathrm{j} GR_\ell}=1\quad\text{für alle ganzen }\ell,\qquad\text{also}\qquad G=h_1\,\frac{2\pi}a,\quad h_1\ \text{ganz}. \tag{4.1}$$

Die $G$ heißen __reziproke Gittervektoren__.
:::

⁠**So liest man das:** $h_1$ zählt die Punkte des reziproken Gitters, $G=0$ gehört dazu. $G$ hat die Einheit 1/m. Für $a=0{,}2$ nm ist $2\pi/a=31{,}4\,\mathrm{nm^{-1}}$, für Silizium sind es $11{,}57\,\mathrm{nm^{-1}}$. $GR_\ell=\ell Ga$ muss für $\ell=1$ ein Vielfaches von $2\pi$ sein, dann ist es das für jedes $\ell$.

:::herleitung Warum gerade diese Wellen?
Eine gitterperiodische Größe $f(x)$, etwa das Potential der Atomrümpfe oder die Teilchendichte, ändert sich beim Verschieben um $R_\ell$ nicht: $f(x+R_\ell)=f(x)$. Sie lässt sich als Summe von Wellen schreiben (Fourier-Reihe): $f(x)=\sum_kc_k\,\mathrm{e}^{\mathrm{j} kx}$. Beim Verschieben bekommt jede Teilwelle den Faktor $\mathrm{e}^{\mathrm{j} kR_\ell}$. Die Summe bleibt nur gleich, wenn jeder Faktor 1 ist. Also kommen nur die Wellen aus [(4.1)](#gl-4-1) vor. Das reziproke Gitter ist die Liste aller Wellen, die selbst gitterperiodisch sind.
:::

:::satz Satz 4.2 (Periodizität im $k$-Raum)
<span class="anker" id="satz-4-2"></span>

Auf der Kette sind $k$ und $k+G$ dieselbe Welle, und alles daraus Berechnete ist in $k$ periodisch:

<span class="anker" id="gl-4-2"></span>
$$\psi_\ell(k+G)=\psi_\ell(k),\qquad E(k+G)=E(k),\qquad v(k+G)=v(k). \tag{4.2}$$
:::

Der Beweis ist eine Zeile: $\mathrm{e}^{\mathrm{j}(k+G)\ell a}=\mathrm{e}^{\mathrm{j} k\ell a}\,\mathrm{e}^{\mathrm{j} GR_\ell}=\mathrm{e}^{\mathrm{j} k\ell a}$ nach [(4.1)](#gl-4-1). Für das Kosinus-Band heißt das $\cos\bigl((k+G)a\bigr)=\cos(ka+2\pi h_1)=\cos(ka)$.

:::abbildung gemb1/k7periodisch 4
Oben: Kosinus-Band im Rechenmodell. Es wiederholt sich mit der Periode $2\pi/a$, rot die Punkte des reziproken Gitters, getönt die Zone. Unten links: freie Parabel (blau) mit ihren Kopien, Scheitel bei $G$. Energie in Einheiten des Werts bei $k=\pi/a$. Unten rechts: reduziertes Zonenschema mit den Abschnitten 1, 2, 3.
:::

**Die Parabel im Gitter.** Auch ein Elektron, das vom Gitter fast nichts spürt, hat $k$ nur bis auf ein $G$ genau. Schreibt man jeden Zustand mit einem $k$ aus der Zone, gehört zu jedem $k$ eine ganze Folge von Energien:

<span class="anker" id="gl-4-3"></span>
$$E=\frac{\hbar^2}{2m}\,(k+G)^2,\qquad G=h_1\,\frac{2\pi}a,\quad h_1=0,\pm1,\pm2,\dots \tag{4.3}$$

Das ist eine Schar von Parabeln, deren Scheitel um die reziproken Gittervektoren verschoben sind (Abb. [4](#abb-4)). Es ist dieselbe Parabel, nur in Stücke geschnitten. Ist $k$ größer als $\pi/a$, zieht man ein passendes $G$ ab und landet in der Zone. So faltet man die Parabel stückweise in den Bereich $-\pi/a<k<+\pi/a$. Das heißt __reduziertes Zonenschema__. **Gültigkeit:** [(4.3)](#gl-4-3) setzt voraus, dass das Gitter die Energie nicht merklich ändert.

::::beispiel
Bei $a=0{,}2$ nm hat die Parabel am Zonenrand 9,40 eV. Der Zustand $k=40\,\mathrm{nm^{-1}}$ liegt außerhalb der Zone. Abzug von $G=31{,}4\,\mathrm{nm^{-1}}$ ergibt $k=8{,}58\,\mathrm{nm^{-1}}$, und [(4.3)](#gl-4-3) liefert mit $k+G=40\,\mathrm{nm^{-1}}$ die Energie 61 eV wie zuvor.
::::

⁠**Grenzfall:** Für $a\to0$ wächst $G$ über alle Grenzen, die Kopien rücken ins Unendliche, und eine einzige Parabel bleibt: der freie Raum aus [Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html).

:::frage Die Dichte $|\psi|^2$ einer ebenen Welle ist doch überall gleich. Wozu dann die Bedingung?
Richtig: Für eine einzelne Welle ist $|\mathrm{e}^{\mathrm{j} kx}|^2=1$ bei jedem $k$, und eine Welle mit beliebigem $k$ darf im Gitter existieren. Die Bedingung [(4.1)](#gl-4-1) betrifft die Teilwellen, aus denen eine gitterperiodische Größe besteht. Sie müssen selbst periodisch sein, die Welle $\psi$ muss es nicht.
:::

:::aufgabe Aufgabe 5 ★★ Eine Wellenzahl außerhalb der Zone
<span class="anker" id="aufg-5"></span>

Eine Kette hat $a=0{,}25$ nm, $m=m_0$, $V_0=0$. Betrachte $k=20\,\mathrm{nm^{-1}}$.

<ol class="al">

<li>

Berechne $t_0$, $2\pi/a$ und den Zonenrand. Welches $k'$ in der Zone ist dieselbe Welle?

</li>

<li>

Prüfe das an $\psi_\ell/A$ für $\ell=1,2,3$.

</li>

<li>

Berechne $E$ und $v$ nach [(0.2)](von-grund-auf-was-aus-teil-2-und-teil-6-gebraucht-wird.html#gl-0-2) für $k$ und $k'$.

</li>

<li>

Für ein fast freies Elektron: Welche Energie hat dieser Zustand? Auf welchem Abschnitt des reduzierten Zonenschemas liegt er?

</li>

</ol>

:::loesung
(a) $t_0=0{,}0381\,\mathrm{eV\,nm^2}/(0{,}25\,\mathrm{nm})^2=0{,}610$ eV, $2\pi/a=25{,}13\,\mathrm{nm^{-1}}$, Zonenrand $12{,}57\,\mathrm{nm^{-1}}$. $k'=20-25{,}13=-5{,}13\,\mathrm{nm^{-1}}$. (b) Für beide gilt $\ell=1$: $0{,}284-0{,}959\,\mathrm{j}$; $\ell=2$: $-0{,}839-0{,}544\,\mathrm{j}$; $\ell=3$: $-0{,}760+0{,}650\,\mathrm{j}$. (c) $\cos(ka)=\cos(k'a)=0{,}284$, also $E=0{,}873$ eV. $\sin(ka)=-0{,}959$, also $v=-4{,}44\cdot10^5$ m/s. Die Welle läuft trotz positivem $k$ nach links. (d) Die Parabel gibt $0{,}0381\,\mathrm{eV\,nm^2}\cdot(20\,\mathrm{nm^{-1}})^2=15{,}2$ eV. $k$ liegt zwischen $\pi/a$ und $2\pi/a$, also auf dem zweiten Abschnitt.
:::
:::
