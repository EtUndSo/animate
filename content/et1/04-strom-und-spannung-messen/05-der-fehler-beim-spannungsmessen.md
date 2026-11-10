---
title: Stufe 4: Der Fehler beim Spannungsmessen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140500
summary: Das Voltmeter liegt außerhalb des Stromkreises, und trotzdem fließt Strom durch es.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Das Voltmeter liegt außerhalb des Stromkreises, und trotzdem fließt Strom durch es. Diese Stufe zeigt, wann das die Spannung senkt, die es messen soll.
:::

**Die Idee.** Das Voltmeter öffnet zwischen zwei Knoten einen zweiten Strompfad. Sein Strom muss irgendwoher kommen. Treibt eine Stromquelle (sie hält ihren Strom fest, [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) den Lastwiderstand $R_L$, teilt sich der feste Strom auf: Was durch das Voltmeter fließt, fehlt in $R_L$, und die Spannung sinkt (Abb. [5](#abb-5)). Hängt $R_L$ dagegen direkt an einer idealen Spannungsquelle, liefert sie den Zusatzstrom, und nichts ändert sich. Fehler entstehen also nur dort, wo der Strom nicht frei nachfließen kann. Beim Spannungsteiler bremst $R_1$ den Nachschub: Der Gesamtstrom steigt, an $R_1$ fällt mehr ab, die Mitte sinkt.

:::abbildung et1/k4spannung 5
Das Voltmeter (Bereich 10 V, gestrichelt: Innenwiderstand und ideales Gerät) an zwei gleichwertigen Schaltungen. In beiden zweigt es 13,6 µ A ab, und die Anzeige fällt von 3 V auf 2,727 V.
:::

:::satz Satz 4.1 (Fehler des Voltmeters)
<span class="anker" id="satz-4-1"></span>

An einer Stromquelle $I_\mathrm q$ mit Last $R_L$ gilt ohne Gerät $U_L=I_\mathrm qR_L$ und mit Gerät

<span class="anker" id="gl-4-1"></span>
$$U_L'=I_\mathrm q\,(R_L\parallel R_\mathrm i)=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}. \tag{4.1}$$

Der relative Fehler ist $f=-R_L/(R_L+R_\mathrm i)$, für $R_L\ll R_\mathrm i$ also $f\approx-R_L/R_\mathrm i$. Am Spannungsteiler gilt dasselbe mit $R_L=R_1\parallel R_2$.
:::

⁠**So liest man das:** Der Bruch ist der Fehlerfaktor. $R_L$ ist der Widerstand, den das Gerät zwischen seinen Anschlüssen vorfindet. Für einen kleinen Fehler braucht es $R_\mathrm i\gg R_L$, ideal $R_\mathrm i\to\infty$. **Gültigkeit:** ideale Quellen, Widerstände unabhängig von der Spannung.

:::herleitung Fehlerfaktor
Mit der Knotenregel $I_\mathrm q=I_{RL}'+I_{\mathrm{i}}$ teilt sich der Strom auf zwei parallele Widerstände auf, an beiden liegt $U_L'$. Also ist $U_L'=I_\mathrm q\,R_LR_\mathrm i/(R_L+R_\mathrm i)$, und Kürzen mit $R_\mathrm i$ ergibt [(4.1)](#gl-4-1). Am Teiler gilt ohne Gerät $U_2=U\,R_2/(R_1+R_2)$. Mit Gerät ist $R_2$ durch $R_2\parallel R_\mathrm i$ zu ersetzen (belasteter Spannungsteiler, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)):

$$U_2'=U\,\frac{R_2R_\mathrm i}{R_1R_2+R_\mathrm i(R_1+R_2)} \quad\Rightarrow\quad \frac{U_2'}{U_2}=\frac{R_\mathrm i(R_1+R_2)}{R_1R_2+R_\mathrm i(R_1+R_2)}=\frac{1}{1+(R_1\parallel R_2)/R_\mathrm i}.$$
:::

::::beispiel
Am Teiler ist $R_1\parallel R_2=20$ k$\Omega$ und $R_L/R_\mathrm i=0{,}1$. Die Anzeige beträgt $3\,\mathrm{V}/1{,}1=2{,}727$ V, also $f=-9{,}1\,\%$. Der Mechanismus in Zahlen: Der Strom durch $R_1$ steigt von 100 µ A auf 104,5 µ A, davon fließen 90,9 µ A durch $R_2$ und 13,6 µ A durch das Voltmeter. Dieselben Werte ergibt $I_\mathrm q=150$ µ A an $R_L=20$ k$\Omega$. Ein Digitalmultimeter mit 10 M$\Omega$ zeigt 2,994 V, also $f=-0{,}2\,\%$.
::::

⁠**Grenzfälle:** $R_\mathrm i\to\infty$ ergibt $f\to0$. $R_L\to0$ (Quelle direkt am Gerät) ergibt ebenfalls $f\to0$. Bei $R_\mathrm i=R_L$ halbiert sich die Spannung.

:::frage 200 k$\Omega$ klingt nach viel. Warum stört das Gerät den Teiler trotzdem?
Groß oder klein gibt es nur im Vergleich mit $R_L$. Der Teiler führt nur 100 µ A. Daneben sind 13,6 µ A kein kleiner Anteil.
:::

:::aufgabe Aufgabe 4 ★★ Hochohmiger Teiler
<span class="anker" id="aufg-4"></span>

$R_1=6$ M$\Omega$ und $R_2=3$ M$\Omega$ liegen an 9 V. (a) Was zeigen das Voltmeter mit 200 k$\Omega$ und das Digitalmultimeter mit 10 M$\Omega$ an $R_2$? (b) Wie gewinnst du aus der Anzeige 2,5 V den wahren Wert zurück? (c) Welches $R_\mathrm i$ bräuchte man für 1 % Fehler?

:::loesung
(a) $R_L=6\,\mathrm{M\Omega}\parallel3\,\mathrm{M\Omega}=2$ M$\Omega$, wahr sind 3 V. Mit 200 k$\Omega$: $3\,\mathrm{V}/(1+10)=0{,}273$ V, $f=-91\,\%$. Mit 10 M$\Omega$: $3\,\mathrm{V}/(1+0{,}2)=2{,}5$ V, $f=-16{,}7\,\%$.

(b) Umstellen von [(4.1)](#gl-4-1): $U=U'(1+R_L/R_\mathrm i)=2{,}5\,\mathrm{V}\cdot1{,}2=3$ V. (c) $R_L/(R_L+R_\mathrm i)\le0{,}01$ ergibt $R_\mathrm i\ge99\,R_L=198$ M$\Omega$.
:::
:::
