---
title: Stufe 12: Zeitdiskrete Bandpässe und Hochpässe
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3251300
summary: Digitale Bandpässe und Hochpässe gewinnt man aus einem Tiefpass durch Modulation.
tags: Hochpass
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Digitale Bandpässe und Hochpässe gewinnt man aus einem Tiefpass durch Modulation.
:::

Hat der zeitdiskrete Tiefpass eine reelle Impulsantwort, verschiebt die Multiplikation mit $2\cos(2\pi f_0n)$ seinen Durchlassbereich nach $\pm f_0$:

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

gültig, solange sich die verschobenen Bänder nicht überlappen: $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$. Wegen der Periodizität darf das Band bei $f_0$ weder das Band bei $-f_0$ noch dessen Kopie bei $1-f_0$ berühren. Allgemein, auch für komplexe Tiefpass-Impulsantworten, gilt wie in [(8.1)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-1) $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$. Der Faktor 2 entspricht dem verdoppelten äquivalenten Tiefpass $H_T=2H_{\mathrm{TP}}$.

Ein __Hochpass__ ist ein Tiefpass, verschoben zur halben Abtastrate $f_0=\frac12$. Dort fallen das Band und sein Spiegelbild zusammen, deshalb verschiebt man nur einmal: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. Mit $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$:

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**Kurz gesagt:** Ein digitaler Hochpass entsteht aus einem Tiefpass, indem man jedes zweite Vorzeichen umdreht.

:::aufgabe Aufgabe 11 ★ Hochpass aus dem gleitenden Mittelwert
<span class="anker" id="aufg-11"></span>

Der gleitende Mittelwert $h_{\mathrm{TP}}=\frac13(1,1,1)$ ([Kapitel 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) ist ein einfacher Tiefpass.

<ol class="al">

<li>

Bilde $h_{\mathrm{HP}}$ nach [(12.2)](#gl-12-2).

</li>

<li>

Berechne $H_{\mathrm{TP}}$ und $H_{\mathrm{HP}}$ bei $f=0$ und $f=\frac12$. Passt das zu einem Hochpass?

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$.

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$: $|H_{\mathrm{TP}}(0)|=1$, $|H_{\mathrm{TP}}(\frac12)|=\frac13$. Der Hochpass ist um $\frac12$ verschoben: $|H_{\mathrm{HP}}(0)|=\frac13$, $|H_{\mathrm{HP}}(\frac12)|=1$. Er lässt die schnellste Folge $(+1,-1,+1,\dots)$ voll durch und dämpft den Gleichanteil auf ein Drittel. Ein einfacher, nicht sehr steiler Hochpass.
:::
:::
