---
title: Stufe 6: Die Wheatstonesche Brücke
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140700
summary: R=U/I addiert die Fehler zweier Anzeigen.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
$R=U/I$ addiert die Fehler zweier Anzeigen. Im Rechenmodell sind das $\pm1{,}1\,\%$ bei der Spannung und $\pm2\,\%$ beim Strom, zusammen bis zu $\pm3{,}1\,\%$. Die Brücke braucht von ihrem Instrument nur eine Aussage: null oder nicht null.
:::

**Die Idee.** Zwei Spannungsteiler hängen an derselben Quelle (Abb. [8](#abb-8)). Ein empfindliches Instrument verbindet ihre Mittelpunkte. Teilen beide im selben Verhältnis, liegen die Mittelpunkte auf demselben Potenzial, zwischen ihnen besteht keine Spannung, und durch das Instrument fließt kein Strom. Man verstellt einen Widerstand, bis der Zeiger auf null steht: der Abgleich. Wenn kein Strom fließt, entnimmt das Instrument der Schaltung nichts. Sein Innenwiderstand wirkt nicht, und seine Skala wird nicht gebraucht.

:::abbildung et1/k4bruecke 8
Links das Prinzip. Rechts die praktische Ausführung: $R_1$ und $R_2$ sind die Teile eines Widerstandsdrahts, der Schleifkontakt legt ihr Verhältnis fest.
:::

:::satz Satz 6.1 (Abgleichbedingung)
<span class="anker" id="satz-6-1"></span>

Fließt durch das Instrument kein Strom, gilt

<span class="anker" id="gl-6-1"></span>
$$R_4=R_3\,\frac{R_2}{R_1}. \tag{6.1}$$
:::

⁠**So liest man das:** $R_3$ ist ein genau bekannter Referenzwiderstand. Von $R_1$ und $R_2$ zählt nur das einstellbare, bekannte Verhältnis, ihre Werte sind belanglos. $R_4$ ist gesucht. In der Gleichung fehlen $U_\mathrm q$ und der Innenwiderstand des Instruments. Schwankt die Quelle, verschieben sich beide Mittelpunkte gleich. **Gültigkeit:** exakt im Abgleich. Wie genau man ihn trifft, hängt davon ab, welche kleine Abweichung das Instrument noch zeigt.

:::herleitung Abgleich
Ohne Querstrom liefert die Knotenregel $I_1=I_2$ und $I_3=I_4$. Gleiche Potenziale der Mittelpunkte ergeben $U_{R2}=U_{R4}$ und $U_{R1}=U_{R3}$. Also ist

$$\frac{U_{R4}}{U_{R3}}=\frac{U_{R2}}{U_{R1}} \quad\Rightarrow\quad \frac{I_4R_4}{I_3R_3}=\frac{I_2R_2}{I_1R_1} \quad\Rightarrow\quad \frac{R_4}{R_3}=\frac{R_2}{R_1}.$$
:::

::::beispiel
Mit $R_2/R_1=1{,}8$ und $R_3=1$ k$\Omega$ steht der Zeiger bei $R_4=1800\,\Omega$ auf null, beide Mittelpunkte liegen auf 5,786 V. Sind $R_3$ und das Verhältnis auf je 0,1 % genau, ist $R_4$ auf $\pm0{,}2\,\%$ genau, mehr als 15-mal besser als $U/I$. Die Genauigkeit stammt nun aus Widerständen, und die lassen sich viel genauer fertigen als Zeigerskalen.
::::

⁠**Grenzfall:** Mit wachsendem $R_4$ läuft der rechte Mittelpunkt von 0 bis $U_\mathrm q$. Die Spannung am Instrument wechselt dabei genau einmal das Vorzeichen, es gibt also genau eine Abgleichstellung.

:::frage In der Brücke fließt doch Strom. Was genau ist null?
Nur der Strom im Querzweig. Durch beide Teiler fließen im Beispiel je 3,214 mA, die Quelle arbeitet normal.
:::

**Schleifdraht und Dekaden.** Im Schleifdraht (gleichmäßiger Widerstandsdraht mit verschiebbarem Kontakt, Länge $l$, Gesamtwiderstand $R_0$) ist bei der Kontaktstellung $x$ der untere Teil $R_2=R_0\,x/l$ und der obere $R_1=R_0\,(1-x/l)$. Daraus folgt $R_4=R_3\,x/(l-x)$, und $R_0$ fällt heraus. Für 1800 $\Omega$ bei $l=1$ m steht der Kontakt bei $x=642{,}9$ mm. Genauere Brücken stellen $R_3$ dekadisch ein: Stufenschalter mit je $9\times100\,\Omega$, $9\times10\,\Omega$, $9\times1\,\Omega$ und $9\times0{,}1\,\Omega$ liefern je eine Ziffer, $R_2/R_1$ ist ein in Zehnerpotenzen umschaltbarer Multiplikator. Mit dem Faktor 10 und der Schalterstellung 180,0 $\Omega$ ergeben sich 1800 $\Omega$ in Schritten von 1 $\Omega$. Als Nullanzeige taugt auch ein Voltmeter, denn im Abgleich sind die Spannungen an $R_2$ und $R_4$ gleich.

:::ltspice Der Abgleich hängt nicht vom Instrument ab
⁠**Zeichnen:** Quelle `voltage` mit 9 V am Netz `o`. `R1` = 1k von `o` nach `l`, `R2` = 1.8k von `l` nach Masse, `R3` = 1k von `o` nach `r`, `R4` = `{RX}` von `r` nach Masse. Das Messwerk ist `Rd` = 2k von `l` nach `r`.

⁠**Direktiven:** `.step param RX 1700 1900 10` und `.op`

⁠**Was du siehst:** Zeichne `I(Rd)` über `RX`: Die Kurve geht bei 1800 durch null, bei 1700 sind es $+36{,}4$ µ A, bei 1900 $-33{,}6$ µ A. Setze `Rd` auf 1 oder 1Meg: Die Kurve ändert ihre Höhe, der Nulldurchgang bleibt bei 1800. Bei 0,1 % Abweichung (1801,8 $\Omega$) fließen im Messwerk nur 0,63 µ A, also 1,3 % des Vollausschlags. Für Aufgabe [7](#aufg-7): Mit `R1` = 356.1 und `R2` = 643.9 (Kontakt 1 mm daneben) wandert der Nulldurchgang auf 1808 $\Omega$.
:::

:::aufgabe Aufgabe 7 ★★ Schleifdraht
<span class="anker" id="aufg-7"></span>

Der Draht ist 1 m lang, $R_3=1$ k$\Omega$. (a) Der Abgleich gelingt bei $x=642{,}9$ mm. Wie groß ist $R_4$? (b) Der Kontakt ist auf $\pm1$ mm ablesbar. Welcher Fehler von $R_4$ folgt daraus? (c) Wiederhole (b) für $R_3=1{,}8$ k$\Omega$ und $R_3=100\,\Omega$. Warum wählt man $R_3$ in der Größe von $R_4$?

:::loesung
(a) $R_4=1\,\mathrm{k\Omega}\cdot642{,}9/357{,}1=1800\,\Omega$. (b) Eine Verschiebung um $\Delta x$ ändert $x/(l-x)$ relativ um $\Delta x\,(1/x+1/(l-x))$. Das sind $1\,\mathrm{mm}\cdot(1/642{,}9+1/357{,}1)/\mathrm{mm}=\pm0{,}44\,\%$.

(c) $R_3=1{,}8$ k$\Omega$: $x=500$ mm, $\pm0{,}40\,\%$. $R_3=100\,\Omega$: $x=947{,}4$ mm, $\pm2{,}0\,\%$. Der Fehler ist am kleinsten, wenn der Kontakt in der Mitte steht, also bei $R_3\approx R_4$. Nahe dem Drahtende wiegt derselbe Millimeter relativ schwer.
:::
:::
