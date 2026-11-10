---
title: Das Wichtigste bis hier
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Integralrechnung im Rⁿ
adresse: elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn
knoten: Kapitel 2: Integralrechnung im Rⁿ
order: 3120700
summary: Wann man Ableitung, Integral und Reihenfolge vertauschen darf
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Parameterintegral: $\partial_{x_k}\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t=\int_a^b\partial_{x_k}f(\boldsymbol{x},t)\,\mathrm{d} t$, wenn $f$ und $\partial_{x_k}f$ auf $\mathcal U\times[a,b]$ stetig sind; Grund ist die gleichmäßige Stetigkeit auf kompakten Mengen.

</li>

<li>

Leibnizregel: $F'(y)=\int_{\alpha(y)}^{\beta(y)}\partial_yf\,\mathrm{d} x+f(\beta(y),y)\,\beta'(y)-f(\alpha(y),y)\,\alpha'(y)$.

</li>

<li>

Uneigentlich: Konvergenz für jeden einzelnen Parameter reicht nicht. Eine Majorante $|f(\boldsymbol{x},t)|\le g(t)$ mit $\int g\,\mathrm{d} t<\infty$, die nicht von $\boldsymbol{x}$ abhängt, macht das Integral stetig; mit Majoranten der Ableitungen darf man ableiten. Lokal genügt sie.

</li>

<li>

Transformierte: $\frac{\mathrm{d}^k}{\mathrm{d} x^k}\mathcal{L} f=\mathcal{L}\bigl((-t)^kf\bigr)$; $\Gamma'(x)=\int_0^\infty\mathrm{e}^{-t}t^{x-1}\ln t\,\mathrm{d} t$, $\Gamma(n+1)=n!$; $\hat f^{(j)}$ ist die Fourier-Transformierte von $(-\mathrm ix)^jf$.

</li>

<li>

Fubini: Für stetiges $f$ auf einem kompakten Quader ist die Integrationsreihenfolge gleichgültig; das Mehrfachintegral ist das iterierte Integral. $\bigl|\int_Qf\,\mathrm{d}\boldsymbol{x}\bigr|\le|Q|\sup_Q|f|$.

</li>

<li>

Mengen: $\int_Mf\,\mathrm{d}\boldsymbol{x}=\int_Q\bar f\,\mathrm{d}\boldsymbol{x}$ mit der Fortsetzung durch null. Cavalieri: $\operatorname{vol}(M)=\int_0^H\mathcal A(z)\,\mathrm{d} z$.

</li>

<li>

Normalbereiche: $\int_Df=\int_c^d\bigl(\int_{\alpha(y)}^{\beta(y)}f\,\mathrm{d} x\bigr)\mathrm{d} y$, im Raum $\int_Mf=\int_D\bigl(\int_{\psi_1}^{\psi_2}f\,\mathrm{d} z\bigr)\mathrm{d} x\,\mathrm{d} y$. Innen Funktionen der äußeren Variablen, außen Zahlen; bei Bedarf zerlegen.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Unter dem Integralzeichen ableiten darf man, wenn der Integrand für alle Parameter zugleich unter Kontrolle ist: auf kompakten Intervallen durch die Stetigkeit, auf unendlichen durch eine Majorante; wandernde Grenzen liefern zwei Randterme.

</li>

<li>

Über einen Quader integriert man Variable für Variable, und für stetige Funktionen ist die Reihenfolge gleichgültig, weil eine endliche Summe von Säulen in jeder Reihenfolge dasselbe ergibt.

</li>

<li>

Über krumm berandete Bereiche integriert man in Streifen, Stäben oder Scheiben: Die Grenzen innen sind Funktionen der äußeren Variablen, und der Sprung am Rand verschwindet in diese Grenzen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Die Sätze dieses Kapitels antworten auf dieselbe Frage: Darf man zwei Grenzprozesse vertauschen, also Ableitung und Integral, zwei Integrale oder Grenzwert und Integral? Das geht, wenn sich der eine Grenzprozess gleichmäßig verhält, unabhängig davon, wo der andere gerade steht. Streifen, Stäbe und Scheiben nutzen diese Freiheit zum Rechnen.

| Ergebnis | Woher es kommt |
|---|---|
| Ableiten unter dem Integral | gleichmäßige Stetigkeit: Die Differenzenquotienten nähern sich an allen Stellen $t$ zugleich der Ableitung (Unterabschnitt [1.9](integrale-mit-parameter-uber-endlichen-intervallen.html#stufe-1-9)) |
| Leibnizregel | Kettenregel und Hauptsatz; jeder wandernde Rand liefert den Beitrag „Höhe mal Geschwindigkeit“ (Unterabschnitt [1.11](integrale-mit-parameter-uber-endlichen-intervallen.html#stufe-1-11)) |
| Unstetige uneigentliche Parameterintegrale | die Konvergenz wird für manche Parameter beliebig langsam (Unterabschnitt [2.7](uneigentliche-parameterintegrale.html#stufe-2-7)) |
| Majorantenkriterium | ein festes Dach macht den Rest für alle Parameter zugleich klein und versperrt die Fluchtwege der Fläche (Unterabschnitte [2.8](uneigentliche-parameterintegrale.html#stufe-2-8) und [2.9](uneigentliche-parameterintegrale.html#stufe-2-9)) |
| Regeln für Fourier, Gamma, Laplace | Ableiten nach einem Parameter in der Exponentialfunktion, abgesichert durch lokale Majoranten (Unterabschnitte [2.10](uneigentliche-parameterintegrale.html#stufe-2-10) bis [2.13](uneigentliche-parameterintegrale.html#stufe-2-13)) |
| Satz von Fubini | eine endliche Säulensumme ergibt in jeder Reihenfolge dasselbe; der Beweis: beide Reihenfolgen haben dieselbe Ableitung (Unterabschnitt [3.4](mehrfachintegrale.html#stufe-3-4)) |
| Prinzip von Cavalieri | iteriertes Integral mit der Höhe außen; Riemann-Summe der Schnittflächen (Unterabschnitt [4.3](integration-uber-mengen-und-berechnung-von-volumina.html#stufe-4-3)) |
| Integration über Normalbereiche | Fortsetzung durch null; der Sprung sitzt an den Grenzen des inneren Integrals (Unterabschnitte [5.1](integration-uber-normalbereiche.html#stufe-5-1) und [5.2](integration-uber-normalbereiche.html#stufe-5-2)) |
