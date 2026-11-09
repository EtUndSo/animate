---
title: Stufe 5: Generation und Rekombination
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
order: 4230700
summary: Bisher blieb die Zahl der Teilchen erhalten.
tags: Überschussdichte, Injektion, schwach, stark, Rekombinationsraten, Rekombinationszeit, tiefe Störstellen
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Bisher blieb die Zahl der Teilchen erhalten. Elektronen und Löcher entstehen und verschwinden aber paarweise. Diese Stufe findet das Gesetz, nach dem ein Überschuss abgebaut wird.
:::

**Die Idee.** Wärme hebt laufend Elektronen ins Leitungsband (Generation), und Elektronen fallen in Löcher zurück (Rekombination). Dabei verschwinden beide. Im Gleichgewicht sind die Raten gleich ([Teil 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html)), deshalb gilt $n\,p=n_\mathrm i^2$. Licht mit $\hbar\omega>E_\mathrm g$ erzeugt zusätzliche Paare. Dann ist $n\,p>n_\mathrm i^2$: Elektron und Loch treffen sich öfter, als die Wärme nachliefert, und der Überschuss schrumpft. Je weniger davon übrig ist, desto langsamer geht es weiter. So entsteht ein exponentielles Abklingen.

:::definition Definition 5.1 (Überschuss und Injektion)
<span class="anker" id="satz-5-1"></span>

Die __Überschussdichte__ ist die Abweichung vom Gleichgewicht, $\Delta n=n-n^\text{eq}$ und $\Delta p=p-p^\text{eq}$. __Injektion__ heißt das Zuführen zusätzlicher Träger. Sie ist __schwach__, wenn der Überschuss klein gegen die Mehrheit ist, im n-Gebiet $\Delta p,p\ll n^\text{eq}$, und __stark__, wenn er die Mehrheit übertrifft. Dann ist $n\approx p$.
:::

⁠**So liest man das:** Die Minderheit im n-Gebiet heißt $p_\mathrm n$, ihr Gleichgewichtswert $p_{\mathrm n0}$, ihr Überschuss $\Delta p_\mathrm n=p_\mathrm n-p_{\mathrm n0}$. Im p-Gebiet entsprechend $n_\mathrm p$, $n_{\mathrm p0}$, $\Delta n_\mathrm p$. $G_\mathrm n,G_\mathrm p$ sind die Raten, mit denen Licht oder Injektion Träger erzeugen, $R_\mathrm n,R_\mathrm p$ die __Rekombinationsraten__ (Rekombination minus thermische Generation, im Gleichgewicht null), alle in cm$^{-3}$ s$^{-1}$.

:::satz Satz 5.2 (Zerfallsgesetz)
<span class="anker" id="satz-5-2"></span>

Bei schwacher Injektion hängt die Rate nur vom Überschuss der Minderheit ab,

<span class="anker" id="gl-5-1"></span>
$$R_\mathrm n=-\frac{\partial\Delta n_\mathrm p}{\partial t}=\frac{\Delta n_\mathrm p}{\tau_{\text{rec},\mathrm n}}\quad\text{im p-Gebiet},\qquad R_\mathrm p=-\frac{\partial\Delta p_\mathrm n}{\partial t}=\frac{\Delta p_\mathrm n}{\tau_{\text{rec},\mathrm p}}\quad\text{im n-Gebiet}, \tag{5.1}$$

und ein homogener Überschuss klingt exponentiell ab:

<span class="anker" id="gl-5-2"></span>
$$\Delta n_\mathrm p(t)=\Delta n_\mathrm p(0)\,\exp\bigl(-t/\tau_{\text{rec},\mathrm n}\bigr). \tag{5.2}$$
:::

⁠**So liest man das:** Die __Rekombinationszeit__ $\tau_\text{rec}$ ist die mittlere Lebensdauer eines Überschussträgers. Nach $\tau_\text{rec}$ sind 36,8 % übrig, nach $4{,}6\,\tau_\text{rec}$ noch 1 %. **Gültigkeit:** Bei starker Injektion hängt $R$ von $\Delta n$ und $\Delta p$ zugleich ab, und das Gesetz gilt nicht mehr.

:::herleitung Warum die Minderheit die Rate bestimmt
Eine Rekombination von Band zu Band verlangt ein Treffen, ihre Rate ist $c\,n\,p$. Wärme erzeugt Paare mit der Rate $c\,n^\text{eq}p^\text{eq}$, sonst stimmte das Gleichgewicht nicht. Paarweise ist $\Delta n=\Delta p$, also im n-Gebiet

$$R_\mathrm p=c\,(n\,p-n^\text{eq}p^\text{eq})=c\,\Delta p_\mathrm n\,(n^\text{eq}+p_{\mathrm n0}+\Delta p_\mathrm n)\approx c\,n^\text{eq}\,\Delta p_\mathrm n.$$

Die Mehrheit bietet so viele Partner, dass jedes Loch unabhängig von den anderen einen findet. Mit $\tau_{\text{rec},\mathrm p}=1/(c\,n^\text{eq})$ folgt [(5.1)](#gl-5-1). Über tiefe Störstellen bleibt die Form, dort zählt deren Dichte.
:::

:::abbildung gemb1/k13rekomb 5
Links: Generation durch Licht und drei Wege der Rekombination. Rechts: Überschuss bei konstanter Beleuchtung ab $t=0$ und Abschalten bei $t=6\tau_\text{rec}$. Die Tangente trifft die Zeitachse nach $\tau_\text{rec}$.
:::

**Wohin die Energie geht.** Die Energie $E_\mathrm g$ wird auf drei Wegen frei (Abb. [5](#abb-5)): als Licht mit $\hbar\omega=E_\mathrm g$, als Wärme durch Phononen, oder in zwei Schritten über __tiefe Störstellen__ mit Niveaus nahe der Bandmitte. In Silizium und Germanium geht sie als Wärme ans Gitter, weil ihre Lücke indirekt ist ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)), im direkten GaAs entsteht ein Lichtquant. $\tau_\text{rec}$ hängt von der Bandstruktur, der Dichte der Partner, der Dichte der Störstellen und der Temperatur ab. Reines Silizium und Germanium erreichen rund $10^{-3}$ s, Gold als tiefe Störstelle senkt das in Silizium bis auf $10^{-10}$ s, GaAs liegt bei $10^{-8}$ s. An Oberflächen ist die Rate viel höher als im Kristall.

::::beispiel
Licht erzeuge in der Probe homogen $G_\mathrm p=10^{19}\,\mathrm{cm^{-3}\,s^{-1}}$. Aus $\partial\Delta p_\mathrm n/\partial t=G_\mathrm p-\Delta p_\mathrm n/\tau_\text{rec}$ und $\Delta p_\mathrm n(0)=0$ folgt

<span class="anker" id="gl-5-3"></span>
$$\Delta p_\mathrm n(t)=G_\mathrm p\tau_\text{rec}\,\bigl(1-\mathrm{e}^{-t/\tau_\text{rec}}\bigr). \tag{5.3}$$

Stationär sind das $10^{13}\,\mathrm{cm^{-3}}$: 0,1 % der Mehrheit, aber das $1{,}3\cdot10^{9}$-fache von $p_{\mathrm n0}=7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$. Die Injektion ist schwach, obwohl sich die Minderheit um neun Größenordnungen ändert. Der Zustand ist konstant, aber kein Gleichgewicht: Das Licht führt ständig Energie zu, und wegen $n\,p\ne n_\mathrm i^2$ passt keine gemeinsame Fermi-Energie zu beiden Sorten, jede hat ihr eigenes Quasi-Fermi-Niveau ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)). Die Abklingzeit eines Photowiderstands ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)) ist genau $\tau_\text{rec}$.
::::

⁠**Grenzfall:** Für $t\ll\tau_\text{rec}$ ist $\Delta p_\mathrm n\approx G_\mathrm pt$.

:::frage Elektronen und Löcher verschwinden gleich oft. Warum entscheidet allein die Minderheit?
Weil nur sie sich relativ ändert. Die Mehrheit steht im Beispiel bei $1{,}001\cdot10^{16}\,\mathrm{cm^{-3}}$, die Zahl der Partner ist also fest. Die Rate folgt dem, was sich ändert: der Zahl der Löcher.
:::

:::aufgabe Aufgabe 6 ★★ Licht an, Licht aus
<span class="anker" id="aufg-6"></span>

Silizium mit $N_\mathrm D=2\cdot10^{15}\,\mathrm{cm^{-3}}$ und $\tau_\text{rec}=5$ µ s wird ab $t=0$ homogen mit $G_\mathrm p=4\cdot10^{18}\,\mathrm{cm^{-3}\,s^{-1}}$ beleuchtet.

<ol class="al">

<li>

Stelle die Differentialgleichung für $\Delta p_\mathrm n$ auf. Welche Art ist das? Wie lautet die Anfangsbedingung?

</li>

<li>

Löse sie. Wie groß sind $\Delta p_\mathrm n$ bei $t=2$ µ s und für $t\to\infty$? Ist die Injektion schwach?

</li>

<li>

Lange danach wird zur Zeit $t_1$ abgeschaltet. Gib $\Delta p_\mathrm n(t)$ an, skizziere den ganzen Verlauf. Wann ist $\Delta p_\mathrm n=10^{10}\,\mathrm{cm^{-3}}$?

</li>

</ol>

:::loesung
(a) $\partial\Delta p_\mathrm n/\partial t=G_\mathrm p-\Delta p_\mathrm n/\tau_\text{rec}$, lineare inhomogene gewöhnliche Differentialgleichung erster Ordnung, $\Delta p_\mathrm n(0)=0$. (b) [(5.3)](#gl-5-3): bei 2 µ s $6{,}6\cdot10^{12}\,\mathrm{cm^{-3}}$, für $t\to\infty$ $2\cdot10^{13}\,\mathrm{cm^{-3}}$, 1 % von $N_\mathrm D$, also schwach. (c) $\Delta p_\mathrm n=2\cdot10^{13}\,\mathrm{cm^{-3}}\,\mathrm{e}^{-(t-t_1)/\tau_\text{rec}}$. Bis $10^{10}\,\mathrm{cm^{-3}}$ dauert es $\tau_\text{rec}\ln2000=38$ µ s.
:::
:::
