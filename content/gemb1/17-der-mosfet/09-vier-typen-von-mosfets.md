---
title: Stufe 7: Vier Typen von MOSFETs
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270900
summary: Bisher ging es um einen n-Kanal-Transistor, der ohne Gatespannung sperrt.
tags: Anreicherungstyp, Verarmungstyp
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bisher ging es um einen n-Kanal-Transistor, der ohne Gatespannung sperrt. Diese Stufe ändert die Dotierung und erhält daraus vier Typen.
:::

**Die Idee.** Zwei Entscheidungen sind unabhängig voneinander. Erstens die Sorte der Träger: Vertauscht man alle Dotierungen, führen Löcher den Strom, und alle Spannungen und Ströme wechseln das Vorzeichen. Zweitens der Zustand bei $V_\mathrm{GS}=0$: Dotiert man das Substrat in einer dünnen Schicht an der Oberfläche wie Source und Drain, besteht der Kanal schon ohne Gatespannung. Je nach Vorzeichen von $V_\mathrm{GS}$ erhöht oder senkt das Gate dann die bewegliche Ladung. Ein Transistor, der erst durch die Gatespannung leitet, heißt __Anreicherungstyp__ (englisch enhancement), einer, der ohne Gatespannung leitet, __Verarmungstyp__ (englisch depletion).

:::definition Definition 7.1 (Die vier Typen)
<span class="anker" id="satz-7-1"></span>

| Typ | Substrat, Source und Drain | $V_\mathrm{th}$ | leitet bei $V_\mathrm{GS}=0$ |
|---|---|---|---|
| n-Kanal, Anreicherung | p, n$^+$ | $>0$ | nein |
| n-Kanal, Verarmung | p, n$^+$, n-Schicht | $<0$ | ja |
| p-Kanal, Anreicherung | n, p$^+$ | $<0$ | nein |
| p-Kanal, Verarmung | n, p$^+$, p-Schicht | $>0$ | ja |
:::

:::abbildung gemb1/k17typen 7
Die vier Typen mit Schaltzeichen und Transferkennlinie in Sättigung, schematisch. $I_\mathrm D$ zählt in den Drain hinein. Beim Verarmungstyp ist der Kanalstrich durchgezogen, denn der Kanal besteht schon. Der Pfeil zeigt von p nach n.
:::

:::satz Satz 7.2 (p-Kanal-MOSFET)
<span class="anker" id="satz-7-2"></span>

Mit $K_\mathrm p=\mu_\mathrm p(\varepsilon_\mathrm{IS}/d_\mathrm{IS})(W/L)$ gilt für $V_\mathrm{GS}\le V_\mathrm{th}$

<span class="anker" id="gl-7-1"></span>
$$I_\mathrm D=-K_\mathrm p\Bigl[(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}-\frac12V_\mathrm{DS}^2\Bigr]\ \text{ für }|V_\mathrm{DS}|\le|V_\mathrm{GS}-V_\mathrm{th}|,\qquad I_\mathrm D=-\frac{K_\mathrm p}2(V_\mathrm{GS}-V_\mathrm{th})^2\ \text{ darüber}, \tag{7.1}$$

für $|V_\mathrm{DS}|\ll|V_\mathrm{GS}-V_\mathrm{th}|$ also $I_\mathrm D\approx-K_\mathrm p(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}$. Für $V_\mathrm{GS}>V_\mathrm{th}$ sperrt er. Die Schwellspannung ist, mit $\varphi_\mathrm{s,SI}<0$ und $\gamma=\sqrt{2\varepsilon eN_\mathrm D}/C'_\mathrm{IS}$,

<span class="anker" id="gl-7-2"></span>
$$V_\mathrm{th}=V_\mathrm{FB}+\varphi_\mathrm{s,SI}-\gamma\sqrt{-\varphi_\mathrm{s,SI}-V_\mathrm{SB}}. \tag{7.2}$$
:::

⁠**So liest man das:** Beim p-Kanal sind $V_\mathrm{GS}-V_\mathrm{th}$ und $V_\mathrm{DS}$ negativ, und $I_\mathrm D$ ist negativ, denn der Strom fließt aus dem Drain heraus. Beim n-Kanal schreibt man genauer $K_\mathrm n$ für $K$. Sperrend vorgespannt ist $V_\mathrm{SB}\le0$, dann ist die Ladung $Q'_\mathrm{SC}=+eN_\mathrm DL_\mathrm{depl}$ positiv. Der Sättigungsstrom heißt beim Verarmungstyp oft $I_\mathrm{DSS}$ und meint den Wert bei $V_\mathrm{GS}=0$. **Gültigkeit:** wie in Stufe [3](gradual-channel-approximation.html#stufe-3).

:::herleitung Vorzeichen tauschen
Der p-Kanal-Transistor ist das Spiegelbild des n-Kanal-Transistors: Elektronen werden Löcher, $N_\mathrm A$ wird $N_\mathrm D$, $\mu_\mathrm n$ wird $\mu_\mathrm p$, und alle Spannungen und Ströme drehen sich um. Ersetzt man in [(3.2)](gradual-channel-approximation.html#gl-3-2) $V_\mathrm{GS}$, $V_\mathrm{DS}$, $V_\mathrm{th}$ und $I_\mathrm D$ durch ihre Negativen, entsteht [(7.1)](#gl-7-1). Ebenso wird aus [(5.2)](transferkennlinie-und-schwellspannung.html#gl-5-2) die Gleichung [(7.2)](#gl-7-2).
:::

::::beispiel
Ein n-Substrat mit $N_\mathrm D=3\cdot10^{16}\,\mathrm{cm^{-3}}$ und sonst gleichem Aufbau hat $V_\mathrm{FB}=-0{,}19$ V, $\varphi_\mathrm{s,SI}=-0{,}777$ V und $V_\mathrm{th}=-1{,}47$ V, ist also ein Anreicherungstyp. Mit $\mu_\mathrm p=200\,\mathrm{cm^2/(V\,s)}$ ist $K_\mathrm p=0{,}345$ mA/V$^2$. Bei $V_\mathrm{GS}=V_\mathrm{DS}=-3$ V ist $V_\mathrm{GS}-V_\mathrm{th}=-1{,}53$ V, und in Sättigung fließt $I_\mathrm D=-0{,}40$ mA. Für denselben Betrag bräuchte er die 2,5-fache Weite, das ist $\mu_\mathrm n/\mu_\mathrm p$.
::::

Einen n-Kanal-Verarmungstyp erhält man im Rechenmodell mit einer n-Schicht. Trägt sie $N_\mathrm s$ Elektronen je Fläche, sinkt $V_\mathrm{th}$ näherungsweise um $eN_\mathrm s/C'_\mathrm{IS}$. Für $V_\mathrm{th}=-1$ V sind das 1,32 V, also $N_\mathrm s=1{,}4\cdot10^{12}\,\mathrm{cm^{-2}}$. Dann fließen bei $V_\mathrm{GS}=0$ schon 0,43 mA. **Grenzfall:** Für $N_\mathrm s\to0$ bleibt der Anreicherungstyp.

:::frage Warum sind n-Kanal-Transistoren meist schneller als p-Kanal-Transistoren?
Elektronen haben in Silizium die größere Beweglichkeit. Bei gleicher Geometrie und gleicher Gatekapazität ist $I_\mathrm D\propto\mu$, und mit dem größeren Strom wird die Kapazität des nächsten Gates schneller umgeladen.
:::

:::aufgabe Aufgabe 10 ★ Typen erkennen
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Benenne den Typ und sage, ob er bei $V_\mathrm{GS}=0$ leitet: (A) n$^+$ in p, $V_\mathrm{th}=0{,}7$ V. (B) p$^+$ in n, $V_\mathrm{th}=-0{,}6$ V. (C) n$^+$ in p mit dotierter n-Schicht, Gate aus Polysilizium, $V_\mathrm{th}=-1{,}2$ V. (D) p$^+$ in n mit p-Schicht, $V_\mathrm{th}=0{,}5$ V.

</li>

<li>

Transistor C hat $K=1$ mA/V$^2$. Berechne den Sättigungsstrom bei $V_\mathrm{GS}=0$, $+1$ und $-2$ V. In welchem Bereich arbeitet er jeweils als Anreicherungs- oder Verarmungsbetrieb?

</li>

<li>

Ein n-Kanal-Transistor ist 10 µ m weit, $\mu_\mathrm n=600$ und $\mu_\mathrm p=200\,\mathrm{cm^2/(V\,s)}$. Wie weit muss ein p-Kanal-Transistor sein, der bei gleichem $|V_\mathrm{GS}-V_\mathrm{th}|$ denselben Betrag des Stroms liefert?

</li>

</ol>

:::loesung
(a) A: n-Kanal, Anreicherung, sperrt. B: p-Kanal, Anreicherung, sperrt. C: n-Kanal, Verarmung, leitet. D: p-Kanal, Verarmung, leitet. (b) $V_\mathrm{GS}=0$: 0,72 mA. $+1$ V: $\frac12\cdot2{,}2^2\,\mathrm{mA}=2{,}42$ mA, die positive Gatespannung erhöht die Ladung (Anreicherungsbetrieb). $-2$ V: unter $V_\mathrm{th}$, Aus-Zustand. Dazwischen, für $-1{,}2\,\mathrm{V}<V_\mathrm{GS}<0$, senkt das Gate die Ladung (Verarmungsbetrieb). (c) $W_\mathrm p=W_\mathrm n\,\mu_\mathrm n/\mu_\mathrm p=30$ µ m.
:::
:::

:::aufgabe Aufgabe 11 ★★ Wärme im Transistor
<span class="anker" id="aufg-11"></span>

Das Rechenmodell erwärmt sich von 300 K auf 350 K. Es gilt $\mu_\mathrm n\propto T^{-3/2}$, $n_\mathrm i(350\,\mathrm{K})=2{,}5\cdot10^{11}\,\mathrm{cm^{-3}}$, $E_\mathrm g$ bleibt fest.

<ol class="al">

<li>

Zeige aus [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) und [(5.1)](transferkennlinie-und-schwellspannung.html#gl-5-1): $V_\mathrm{th}=(\Phi_\mathrm M-\chi_\mathrm{SC}-E_\mathrm g/2)/e-(Q'_\mathrm{IS}+Q'_\mathrm{SS})/C'_\mathrm{IS}+\varphi_\mathrm{s,WI}+\gamma\sqrt{2\varphi_\mathrm{s,WI}}$. Berechne $V_\mathrm{th}$ bei 350 K.

</li>

<li>

Berechne $I_\mathrm{D,sat}$ bei beiden Temperaturen für $V_\mathrm{GS}=3$ V und 0,5 V. Welche Änderung gewinnt jeweils?

</li>

<li>

Wie ändert sich die Verlustleistung $V_\mathrm{DS}I_\mathrm D$ im Betrieb bei $V_\mathrm{GS}=3$ V und festem $V_\mathrm{DS}$? Warum wirkt das stabilisierend?

</li>

</ol>

:::loesung
(a) Mit $\Phi_\mathrm{SC}=\chi_\mathrm{SC}+E_\mathrm g/2+e\varphi_\mathrm{s,WI}$ ist $V_\mathrm{FB}=(\Phi_\mathrm M-\chi_\mathrm{SC}-E_\mathrm g/2)/e-\varphi_\mathrm{s,WI}-(Q'_\mathrm{IS}+Q'_\mathrm{SS})/C'_\mathrm{IS}$. Dazu kommen $2\varphi_\mathrm{s,WI}$ und $\gamma\sqrt{2\varphi_\mathrm{s,WI}}$. Bei 350 K ist $V_\mathrm T=30{,}16$ mV, $\varphi_\mathrm{s,WI}=0{,}353$ V und $V_\mathrm{th}=-0{,}510-0{,}065+0{,}353+0{,}485=0{,}263$ V, also 60 mV weniger. (b) $\mu_\mathrm n$ fällt auf das 0,794-Fache, 397 cm$^2$/(V s). Bei 3 V: 3,09 mA auf 2,57 mA, die Beweglichkeit gewinnt. Bei 0,5 V: 0,013 mA auf 0,019 mA, die kleinere Schwelle gewinnt. Das Gleichgewicht liegt bei 0,81 V. (c) Sie sinkt um 17 %. Ein wärmerer Transistor führt weniger Strom und heizt sich weniger, das bremst die Erwärmung.
:::
:::
