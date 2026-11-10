---
title: Stufe 2: Vier Größen, zwei Gleichungen, vier Zahlen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1160400
summary: Vier Torgrößen sind vier Unbekannte.
tags: Zweitorfunktionen, symmetrischen Zählpfeilsystem, Kettenpfeilsystem, gemischte Pfeilsystem
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Vier Torgrößen sind vier Unbekannte. Diese Stufe zeigt, warum das Zweitor genau zwei Gleichungen beiträgt und warum darin nur vier Zahlen stecken.
:::

**Die Idee.** Quelle und Last liefern je eine Gleichung zwischen Spannung und Strom ihres Tors. Es fehlen zwei, und die liefert das Zweitor. Gibt man zwei Torgrößen vor, etwa beide Ströme, liegen alle Ströme und Spannungen im Inneren fest, also auch die beiden übrigen Torgrößen. Die vorgegebenen Größen sind die Ursachen, die anderen die Wirkungen. Ist das Zweitor linear und enthält keine unabhängigen Quellen, gilt die Überlagerung aus [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): Jede Wirkung ist die Summe aus dem Anteil der ersten und dem Anteil der zweiten Ursache, jeder Anteil proportional zu seiner Ursache. Zwei Wirkungen mal zwei Ursachen ergeben vier Faktoren.

:::satz Satz 2.1 (Zweitorgleichungen)
<span class="anker" id="satz-2-1"></span>

Ein zeitunabhängiges Zweitor wird durch zwei __Zweitorfunktionen__ vollständig beschrieben, zum Beispiel

<span class="anker" id="gl-2-1"></span>
$$I_1=f_1(U_1,U_2),\quad I_2=g_1(U_1,U_2)\qquad\text{oder}\qquad U_1=f_2(I_1,I_2),\quad U_2=g_2(I_1,I_2). \tag{2.1}$$

Ist es linear und frei von unabhängigen Quellen, gilt für Wirkungen $y_1,y_2$ und Ursachen $x_1,x_2$

<span class="anker" id="gl-2-2"></span>
$$y_1=p_{11}x_1+p_{12}x_2,\qquad y_2=p_{21}x_1+p_{22}x_2. \tag{2.2}$$
:::

⁠**So liest man das:** Die erste Ziffer eines Parameters nennt die Wirkung, die zweite die Ursache. Die Parameter hängen nur vom Zweitor ab, nicht von Quelle oder Last. Vier Größen lassen sich auf sechs Arten in zwei Ursachen und zwei Wirkungen teilen. Gebräuchlich sind die vier Formen dieses Kapitels. **Gültigkeit:** [(2.1)](#gl-2-1) gilt auch für nichtlineare Zweitore, dann als Kurven. Beim Transistor beschreibt man so entweder das Verhalten für Gleichgrößen oder das Signalverhalten für kleine Wechselgrößen. Ein Transformator mit getrennten Wicklungen überträgt nur zeitveränderliche Größen. [(2.2)](#gl-2-2) verlangt Linearität.

**Zählpfeile.** Damit die Vorzeichen eindeutig sind, braucht man eine Vereinbarung (Abb. [3](#abb-3)). Im __symmetrischen Zählpfeilsystem__, auch mathematische Vorzeichenrichtung genannt, gilt an beiden Toren das Verbraucherzählpfeilsystem aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): Die Strompfeile zeigen in das Zweitor hinein. Im __Kettenpfeilsystem__, auch technisches Pfeilsystem genannt, gilt es nur am Eingang, am Ausgang gilt das Erzeugerzählpfeilsystem: Der Ausgangsstrom zeigt heraus, zur Last. Dieses Kapitel benutzt das __gemischte Pfeilsystem__: $I_1$ und $I_2$ zeigen immer hinein. Wo die Kettenform den herausfließenden Strom braucht, schreibt sie ihn ausdrücklich als $-I_2$. Eine Last ergibt deshalb im Normalbetrieb ein negatives $I_2$.

:::abbildung et1/k6zaehlpfeile 3
Die drei Pfeilsysteme. Links symmetrisch: Beide Ströme zeigen in das Zweitor. Mitte Kettenpfeil: Der Ausgangsstrom zeigt zur Last. Rechts gemischt, wie in diesem Kapitel: $I_2$ bleibt definiert wie links, der Strom zur Last heißt $-I_2$.
:::

::::beispiel
Am Mittelpunkt des T-Zweitors treffen sich $I_1$ und $I_2$, durch $R_\mathrm{b}$ fließt ihre Summe. Die Maschenregel ergibt

$$U_1=R_\mathrm{a}I_1+R_\mathrm{b}(I_1+I_2)=35\,\Omega\cdot I_1+20\,\Omega\cdot I_2,\qquad U_2=R_\mathrm{c}I_2+R_\mathrm{b}(I_1+I_2)=20\,\Omega\cdot I_1+40\,\Omega\cdot I_2.$$

Der Summand $20\,\Omega\cdot I_2$ in $U_1$ ist der Mechanismus: Der Strom von Tor 2 läuft durch $R_\mathrm{b}$, hebt dort das Potenzial des Mittelpunkts, und Tor 1 sieht diese Anhebung. Mit $I_1=250$ mA und $I_2=-50$ mA folgt $U_1=8{,}75\,\mathrm{V}-1\,\mathrm{V}=7{,}75$ V und $U_2=5\,\mathrm{V}-2\,\mathrm{V}=3$ V.
::::

⁠**Grenzfall:** Ohne Ursachen, $I_1=I_2=0$, sind beide Spannungen null, wie es ein Zweitor ohne eigene Quellen verlangt. Mit einer unabhängigen Quelle im Inneren käme in jeder Gleichung eine Konstante hinzu.

⁠**Kurz gesagt:** Zwei Größen sind frei, und jede der beiden anderen ist eine Summe mit zwei festen Faktoren.

:::frage Wer entscheidet, welche zwei Größen die Ursachen sind, das Netzwerk?
Nein, das ist die Rechnung. Physikalisch stellt sich alles gleichzeitig ein. Die Gleichungen beschreiben einen Zusammenhang zwischen vier Größen, und man darf ihn nach zwei beliebigen auflösen, sofern diese wirklich frei wählbar sind. „Ursache“ heißt hier: Das steht rechts vom Gleichheitszeichen.
:::

:::aufgabe Aufgabe 2 ★ Eine Blackbox vorhersagen
<span class="anker" id="aufg-2"></span>

Ein unbekanntes lineares Zweitor ohne eigene Quellen ergibt zwei Messungen. Mit $I_1=200$ mA, $I_2=0$ ist $U_1=8$ V, $U_2=3$ V. Mit $I_1=0$, $I_2=100$ mA ist $U_1=1{,}5$ V, $U_2=3$ V.

<ol class="al">

<li>

Sage ohne weitere Messung $U_1$ und $U_2$ für $I_1=100$ mA, $I_2=200$ mA voraus.

</li>

<li>

Was ergibt sich für $I_1=100$ mA, $I_2=-50$ mA? Was fällt an $U_2$ auf?

</li>

</ol>

:::loesung
Die Messungen ergeben $Z_{11}=8\,\mathrm{V}/200\,\mathrm{mA}=40\,\Omega$, $Z_{21}=15\,\Omega$, $Z_{12}=1{,}5\,\mathrm{V}/100\,\mathrm{mA}=15\,\Omega$, $Z_{22}=30\,\Omega$. (a) $U_1=40\,\Omega\cdot0{,}1\,\mathrm{A}+15\,\Omega\cdot0{,}2\,\mathrm{A}=7$ V, $U_2=15\,\Omega\cdot0{,}1\,\mathrm{A}+30\,\Omega\cdot0{,}2\,\mathrm{A}=7{,}5$ V. (b) $U_1=4\,\mathrm{V}-0{,}75\,\mathrm{V}=3{,}25$ V, $U_2=1{,}5\,\mathrm{V}-1{,}5\,\mathrm{V}=0$. Dieses Strompaar gehört also zu einem kurzgeschlossenen Tor 2.
:::
:::
