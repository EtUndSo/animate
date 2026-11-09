---
title: Stufe 2: Fluoreszenz und Nanokristalle
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Ergänzung: Licht und Laser
order: 4290400
summary: Ein Stoff nimmt ultraviolettes Licht auf und leuchtet sichtbar.
tags: Nanokristall, Suspension
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Stoff nimmt ultraviolettes Licht auf und leuchtet sichtbar. Diese Stufe erklärt, warum das abgegebene Licht langwelliger ist und warum bei sehr kleinen Kristallen die Größe die Farbe festlegt.
:::

**Die Idee.** Ein __Nanokristall__ ist ein Halbleiterteilchen von wenigen Nanometern, das in einer Flüssigkeit schwebt (__Suspension__). Er ist ein Quantenpunkt ([Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)) mit endlich hohen Wänden ([Teil 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html)). Ein UV-Photon hebt ein Elektron aus dem Valenzband weit ins Leitungsband und lässt ein Loch zurück (Abb. [2](#abb-2)). In Pikosekunden gibt das Elektron strahlungslos Energie ans Gitter ab, bis es auf dem tiefsten Niveau des Leitungsbands sitzt. Das Loch läuft ebenso zum obersten Niveau des Valenzbands. Jetzt liegt die ganze Lücke vor dem Elektron. Ein Phonon trägt nur einige 10 meV und kann sie nicht überbrücken. Das Elektron wartet Nanosekunden und fällt dann unter Abgabe eines Photons ins Loch. Das ist Fluoreszenz: Der Stoff absorbiert kurzwelliges Licht und emittiert Licht größerer Wellenlänge. Die Differenz $\hbar\omega_\mathrm{ein}-\hbar\omega_\mathrm{aus}>0$ wird strahlungslos als Wärme abgegeben.

:::abbildung gemb1/k19nanokristall 2
Links: UV-Licht von 365 nm hebt ein Elektron in Würfeln mit 7 nm und 4 nm Kante. Es steigt strahlungslos ab (gestrichelt) und fällt von dort unter Emission. Die Niveaus liegen im kleinen Würfel weiter außen. Rechts: Photonenenergie nach [(2.1)](#gl-2-1). Für große Kanten nähert sie sich $E_\mathrm g$.
:::

:::satz Satz 2.1 (Farbe eines Nanokristalls)
<span class="anker" id="satz-2-1"></span>

Für einen Würfel der Kante $L$ mit unendlich hohen Wänden ist die Energie des emittierten Photons

<span class="anker" id="gl-2-1"></span>
$$\hbar\omega(L)=E_\mathrm g+\frac{3\hbar^2\pi^2}{2L^2}\Bigl(\frac1{m_\mathrm C^*}+\frac1{m_\mathrm V^*}\Bigr). \tag{2.1}$$
:::

⁠**So liest man das:** Der erste Summand ist die Lücke des großen Kristalls, der zweite die Energie, die das Einsperren von Elektron und Loch kostet. Er fällt wie $1/L^2$, im Rechenmodell ist sein Vorfaktor $11{,}2\,\mathrm{eV\,nm^2}$. Leichte Teilchen zeigen die Quantisierung stärker. **Gültigkeit:** Das Modell überschätzt $\hbar\omega$, denn endlich hohe Wände lassen die Welle eindringen und senken die Niveaus ([Teil 3](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt/stufe-barriere-und-tunneleffekt.html)). Die Anziehung zwischen Elektron und Loch fehlt. Sie liegt bei $L=4$ nm mit $\varepsilon_\mathrm r=9{,}5$ in der Größenordnung $e^2/(4\pi\varepsilon L)=0{,}04$ eV, das sind 5 % des Einschlussterms.

:::herleitung Elektron und Loch in der Box
Das Elektron ist ein Teilchen der Masse $m_\mathrm C^*$ im Würfel. Sein tiefstes Niveau $(1,1,1)$ liegt um $3E_0^\mathrm C=3\hbar^2\pi^2/(2m_\mathrm C^*L^2)$ über $E_\mathrm C$. Für das Loch mit der Masse $m_\mathrm V^*$ liegt das oberste Niveau des Valenzbands entsprechend um $3E_0^\mathrm V$ unter $E_\mathrm V$. Also ist $\hbar\omega=(E_\mathrm C+3E_0^\mathrm C)-(E_\mathrm V-3E_0^\mathrm V)=E_\mathrm g+3E_0^\mathrm C+3E_0^\mathrm V$. Auch der Abstand zweier Niveaus derselben Box fällt wie $1/L^2$: Von $(1,1,1)$ nach $(2,1,1)$ sind es $3E_0$.
:::

::::beispiel
Mit [(2.1)](#gl-2-1) ergibt das Rechenmodell:

| $L$ | 3 nm | 4 nm | 5 nm | 7 nm | $\to\infty$ |
|---|---|---|---|---|---|
| $\hbar\omega$ | 2,98 eV | 2,44 eV | 2,19 eV | 1,97 eV | 1,74 eV |
| $\lambda$ | 416 nm | 508 nm | 567 nm | 630 nm | 713 nm |
| Farbe | violett | blaugrün | gelbgrün | rot | tiefrot |

Eine UV-Lampe von 365 nm liefert 3,40 eV je Photon. Beim 4-nm-Würfel gehen 0,96 eV, also 28 %, als Wärme verloren. Der Abstand von $(1,1,1)$ zu $(2,1,1)$ im Leitungsband sinkt von 0,54 eV bei 4 nm auf 0,18 eV bei 7 nm, das ist der Faktor $(7/4)^2=3{,}06$. Diese Farbeinstellung nutzen Bildschirme mit Quantenpunkten.
::::

⁠**Grenzfälle:** Für $L\to\infty$ bleibt $\hbar\omega=E_\mathrm g$. Halbiert man $L$, vervierfacht sich der Einschlussterm, $\hbar\omega$ aber nicht.

:::frage Warum leuchten verschieden große Kristalle unter derselben Lampe verschieden?
Die Lampe bestimmt nur, wie weit das Elektron zuerst steigt. Das Photon entsteht immer vom tiefsten Niveau aus, und dessen Lage hängt allein von $L$ und dem Stoff ab.
:::

:::aufgabe Aufgabe 3 ★★ Farbe nach Maß
<span class="anker" id="aufg-3"></span>

Rechne mit dem CdSe-Würfel des Rechenmodells.

<ol class="al">

<li>

Welche Kante $L$ liefert 620 nm? Welche Farbe liefert die halbe Kante?

</li>

<li>

Der Würfel aus (a) wird mit 405 nm beleuchtet. Welcher Anteil jedes Photons wird Wärme?

</li>

<li>

Vorhersage: Eine Lampe von 530 nm trifft Würfel mit 3 nm und mit der Kante aus (a). Welche leuchten?

</li>

</ol>

:::loesung
(a) 620 nm sind 2,00 eV. Aus $0{,}26\,\mathrm{eV}=11{,}2\,\mathrm{eV\,nm^2}/L^2$ folgt $L=6{,}56$ nm. Bei $L=3{,}28$ nm vervierfacht sich der Einschluss auf 1,04 eV, das ergibt 2,78 eV und 446 nm (blau). (b) 405 nm sind 3,06 eV. Es bleiben 2,00 eV, also werden $1{,}06/3{,}06=35$ % Wärme. (c) 530 nm sind 2,34 eV. Der große Würfel absorbiert ab 2,00 eV und leuchtet orangerot. Beim 3-nm-Würfel liegt die tiefste Absorption bei 2,98 eV, er bleibt dunkel.
:::
:::
