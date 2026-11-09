---
title: Stufe 6: Die Box mit endlich hohen Wänden
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4130800
summary: Die Box aus Teil 2 hatte unendlich hohe Wände.
tags: gebundener Zustand
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Box aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) hatte unendlich hohe Wände. Jetzt sind die Wände endlich. Diese Stufe setzt stehende Welle und Eindringen zusammen und zeigt, was das für die erlaubten Energien bedeutet.
:::

**Die Idee.** Innen ist die Welle weiter eine stehende Welle. Die Wände sind jetzt Stufen mit $E<V_0$, also endet sie an der Wand nicht, sondern klingt mit der Eindringtiefe $\delta$ nach außen ab (Abb. [7](#abb-7)). Das Elektron hat dadurch mehr Raum. Eine längere Wellenlänge passt hinein, und mit dem kleineren $k$ sinkt die Energie. Hohe Niveaus liegen dicht unter der Oberkante, dort ist $V_0-E$ klein und $\delta$ groß. Sie reichen weit hinaus. Tiefe Niveaus bleiben fast gefangen.

:::abbildung gemb1/k3box 7
Box der Breite $L=1$ nm. Links mit unendlich hohen Wänden: $\psi$ ist an der Wand null. Rechts mit $V_0=2$ eV: Die Welle reicht in die Wände hinein, die drei Niveaus liegen tiefer, und das oberste reicht am weitesten hinaus. Wellenfunktionen schematisch über ihrem Niveau aufgetragen, Amplitude ohne Maßstab.
:::

:::definition Definition 6.1 (Box mit endlichen Wänden)
<span class="anker" id="satz-6-1"></span>

Es ist $V=0$ für $|x|<L/2$ und $V=V_0$ für $|x|\ge L/2$. Ein Zustand mit $0<E<V_0$ heißt __gebundener Zustand__: Außen klingt $\psi$ auf beiden Seiten ab.
:::

:::satz Satz 6.2 (Zustände der Box mit endlichen Wänden)
<span class="anker" id="satz-6-2"></span>

Innen ist $\psi$ eine stehende Welle, außen ist $\psi\propto\mathrm{e}^{-\kappa_n(|x|-L/2)}$ mit $\delta_n=1/\kappa_n=\sqrt{\hbar^2/(2m(V_0-E_n))}$. Je höher das Potential relativ zum Niveau ist, desto

<ol>

<li>

weniger dringt die Wellenfunktion in das verbotene Gebiet ein, und desto kleiner ist die Aufenthaltswahrscheinlichkeit außerhalb der Box;

</li>

<li>

mehr steigt die Energie und nähert sich den Werten $E_n^\infty=\hbar^2\pi^2n^2/(2mL^2)$ der Box mit unendlich hohen Wänden.

</li>

</ol>

Die Energien liegen unter denen der unendlich hohen Box, und es gibt nur endlich viele gebundene Zustände, nämlich die nächste ganze Zahl über $L\sqrt{2mV_0}/(\pi\hbar)$. Eine grobe Schätzung für tiefe Niveaus ersetzt $L$ durch die um beide Eindringtiefen größere Breite:

<span class="anker" id="gl-6-1"></span>
$$E_n\approx\frac{\hbar^2\pi^2n^2}{2m\,(L+2\delta_n)^2}. \tag{6.1}$$
:::

⁠**So liest man das:** $E_n$ wird vom Boden der Box aus gezählt. Zustände mit $E>V_0$ gibt es auch, sie sind nicht gebunden: Außen läuft die Welle fort. [(6.1)](#gl-6-1) ist eine Näherung, denn $\psi$ ist an der Wand nicht null. **Gültigkeit:** Wände beidseitig gleich hoch und unendlich dick.

:::zusatz Die exakte Bedingung
Innen gerade: $\psi=\cos(kx)$. Stetigkeit von $\psi'/\psi$ bei $x=L/2$ ergibt $k\tan(kL/2)=\kappa$. Innen ungerade: $\psi=\sin(kx)$ ergibt $-k\cot(kL/2)=\kappa$. Dazu kommt $k^2+\kappa^2=2mV_0/\hbar^2$. Diese Gleichungen lassen sich nicht nach $E$ auflösen. Die Zahlen unten sind numerisch gerechnet.
:::

::::beispiel
Für $L=1$ nm und $V_0=2$ eV ist $L\sqrt{2mV_0}/(\pi\hbar)=2{,}31$, es gibt also 3 gebundene Zustände.

| $n$ | $E_n^\infty$ in eV | $E_n$ in eV | $\delta_n$ in nm | Schätzung [(6.1)](#gl-6-1) in eV | außerhalb |
|---|---|---|---|---|---|
| 1 | 0,376 | 0,229 | 0,147 | 0,225 | 2,6 % |
| 2 | 1,504 | 0,887 | 0,185 | 0,801 | 12 % |
| 3 | 3,384 | 1,815 | 0,453 | 0,931 | 43 % |

Das tiefste Niveau sitzt zu 97 % in der Box, das oberste nur zu 57 %. Die Schätzung trifft $E_1$ auf 2 %, bei $E_3$ versagt sie, denn $\delta_3$ ist nicht klein gegen $L$.
::::

⁠**Grenzfall:** Mit wachsendem $V_0$ steigt $E_1$ auf den Wert der harten Wand: 0,191 eV, 0,272 eV, 0,318 eV und 0,367 eV bei $V_0=1$, 5, 20 und 1000 eV. Der Anteil außerhalb fällt dabei von 5,8 % auf unter 0,01 %.

Dasselbe gilt in zwei Richtungen: Sperrt man das Elektron in ein Quadrat mit endlichen Wänden, reichen die Hügel von $|\psi|^2$ an allen Rändern über die Box hinaus.

:::frage Wenn die Welle in die Wand ragt, läuft das Elektron dann nicht hinaus?
Nein, solange die Wand unendlich dick ist. Außen gibt es keine laufende Welle, und ein gebundener Zustand ist stationär: $|\psi|^2$ ändert sich zeitlich nicht. Das Elektron ist mit 2,6 % Wahrscheinlichkeit außerhalb, ohne wegzulaufen. Ist die Wand dünn, setzt sich dahinter eine laufende Welle fort, und das Elektron kann heraustunneln.
:::

:::aufgabe Aufgabe 11 ★★ Eine breite Box
<span class="anker" id="aufg-11"></span>

Eine Box hat $L=2$ nm und $V_0=1$ eV.

<ol class="al">

<li>

Berechne $E_1^\infty$ bis $E_4^\infty$. Wie viele gebundene Zustände gibt es?

</li>

<li>

Schätze $E_1$ mit [(6.1)](#gl-6-1): Starte mit $E_1^\infty$ für $\delta_1$, berechne $E_1$, und wiederhole, bis sich drei Stellen nicht mehr ändern. Der exakte Wert ist 0,0656 eV.

</li>

<li>

Vorhersage: Wie ändern sich $E_1$ und der Anteil außerhalb, wenn $V_0$ auf 3 eV steigt? Begründe mit $\delta_1$.

</li>

</ol>

:::loesung
(a) $E_n^\infty=0{,}094\,n^2$ eV: 0,094 eV, 0,376 eV, 0,846 eV, 1,504 eV. Mit $L\sqrt{2mV_0}/(\pi\hbar)=3{,}26$ gibt es 4 gebundene Zustände, obwohl $E_4^\infty$ über der Wand läge. (b) $\delta=0{,}195\,\mathrm{nm}/\sqrt{0{,}906}=0{,}205$ nm, $L+2\delta=2{,}41$ nm, $E_1=0{,}0647$ eV. Nächster Schritt: $\delta=0{,}202$ nm, $E_1=0{,}0651$ eV. Weitere Schritte ändern nichts. Die Schätzung liegt 0,7 % unter dem exakten Wert. (c) $V_0-E_1$ wächst auf rund 2,9 eV, $\delta_1$ sinkt auf rund 0,11 nm. $E_1$ steigt in Richtung $E_1^\infty$, der Anteil außerhalb sinkt.
:::
:::
