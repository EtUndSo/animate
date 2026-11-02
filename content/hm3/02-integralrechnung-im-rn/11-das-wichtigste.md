---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3121100
summary: Wann man Ableitung, Integral und Reihenfolge vertauschen darf
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

Parameterintegral: $\partial_{x_k}\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t=\int_a^b\partial_{x_k}f(\boldsymbol{x},t)\,\mathrm{d} t$, wenn $f$ und $\partial_{x_k}f$ auf $\mathcal U\times[a,b]$ stetig sind.

</li>

<li>

Leibnizregel: $F'(y)=\int_{\alpha(y)}^{\beta(y)}\partial_yf\,\mathrm{d} x+f(\beta,y)\,\beta'-f(\alpha,y)\,\alpha'$.

</li>

<li>

Uneigentlich: Konvergenz für jedes einzelne $\boldsymbol{x}$ reicht nicht. Man braucht eine Majorante $|f(\boldsymbol{x},t)|\le g(t)$ mit $\int g\,\mathrm{d} t<\infty$, die nicht von $\boldsymbol{x}$ abhängt. Lokal genügt sie.

</li>

<li>

Transformierte: $\frac{\mathrm{d}^k}{\mathrm{d} x^k}\mathcal{L} f=\mathcal{L}((-t)^kf)$, $\Gamma'(x)=\int_0^\infty\mathrm{e}^{-t}t^{x-1}\ln t\,\mathrm{d} t$, $\hat f^{(\ell)}$ gehört zu $(-\mathrm ix)^\ell f$.

</li>

<li>

Fubini: Für stetiges $f$ auf einem kompakten Quader ist die Reihenfolge egal. Wähle die günstige.

</li>

<li>

Mengen: $\int_Mf\,\mathrm{d}\boldsymbol{x}=\int_Q\bar f\,\mathrm{d}\boldsymbol{x}$. Cavalieri: $\operatorname{vol}(M)=\int_0^H\mathcal A(z)\,\mathrm{d} z$.

</li>

<li>

Normalbereich: $\int_Df=\int_c^d\bigl(\int_{\alpha(y)}^{\beta(y)}f\,\mathrm{d} x\bigr)\mathrm{d} y$, im Raum $\int_Mf=\int_D\bigl(\int_{\mu}^{\nu}f\,\mathrm{d} z\bigr)\mathrm{d} x\,\mathrm{d} y$. Innen Funktionen, außen Zahlen.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Unter dem Integralzeichen ableiten darf man, wenn der Integrand für alle Parameter zugleich unter Kontrolle ist: auf kompakten Intervallen durch Stetigkeit, sonst durch eine Majorante. Wandernde Grenzen liefern zwei Randterme.

</li>

<li>

Über Quader integriert man Variable für Variable, und für stetige Funktionen ist die Reihenfolge egal.

</li>

<li>

Über krumme Bereiche integriert man in Streifen oder Scheiben: Die inneren Grenzen sind Funktionen der äußeren Variablen.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Die Sätze dieses Kapitels antworten auf dieselbe Frage: Darf man zwei Grenzprozesse vertauschen? Das geht, wenn sich der eine gleichmäßig verhält, also unabhängig vom Ort des anderen. Streifen, Scheiben und Stäbe nutzen diese Freiheit zum Rechnen.

| Ergebnis | Woher es kommt |
|---|---|
| Ableiten unter dem Integral | gleichmäßige Stetigkeit auf dem kompakten $[a,b]$ (Stufe [1](integrale-mit-parameter.html#stufe-1)) |
| Leibnizregel | Kettenregel und Hauptsatz (Stufe [2](wandernde-grenzen.html#stufe-2)) |
| Majorantenkriterium | Rest des Integrals für alle $\boldsymbol{x}$ zugleich klein (Stufe [3](bis-ins-unendliche.html#stufe-3)) |
| Regeln der Transformierten | lokale Majorante (Stufe [4](lokale-majoranten-und-transformierte.html#stufe-4)) |
| Satz von Fubini | beide Reihenfolgen haben dieselbe Ableitung (Stufe [5](uber-quader-integrieren.html#stufe-5)) |
| Prinzip von Cavalieri | Riemann-Summe über die Schnittflächen (Stufe [6](mengen-und-scheiben.html#stufe-6)) |
| Integration über Normalbereiche | Fortsetzung durch null, dann zeilenweise (Stufen [7](bereiche-zwischen-zwei-kurven.html#stufe-7) und [8](korper-zwischen-zwei-flachen.html#stufe-8)) |
