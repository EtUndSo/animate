---
title: Die Wheatstonesche Messbrücke
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Strom- und Spannungsmessung
order: 60200
summary: Von Grund auf – wie man einen Widerstand nicht abliest, sondern mit bekannten Widerständen vergleicht, und warum die Messung gerade dann am genauesten ist, wenn das Messgerät nichts anzeigt. Leitbild ist die Balkenwaage: Abgleich ist der waagrechte Balken, der Schleifdraht das Laufgewicht, die Dekadenbrücke der Gewichtssatz. Mit zwei Spannungsteilern an einer Quelle, der Abgleichbedingung, der Unabhängigkeit von Quellenspannung und Innenwiderstand des Nullindikators, Schleifdraht- und Dekadenbrücke, der verstimmten Brücke mit Dehnungsmessstreifen, Viertel-, Halb- und Vollbrücke samt Temperaturausgleich und der Zusammenfassung der Messtechnik. Mit Beispiel-Seite.
tags: Wheatstone, Messbrücke, Abgleichbedingung, Nullmethode, Widerstandsmessung
---

## Anschaulich

Ein Strommesser oder Spannungsmesser muss einen Wert anzeigen, und jede Ungenauigkeit seiner Skala geht in das Ergebnis ein. Es gibt einen
genaueren Weg: den unbekannten Widerstand mit bekannten zu **vergleichen** und so lange nachzustellen, bis ein Messgerät **nichts** mehr anzeigt. Dann
hängt das Ergebnis nur noch von den bekannten Widerständen ab. Das leistet die __Wheatstonesche Messbrücke__, benannt nach Charles Wheatstone.

**Das Leitbild dieses Artikels:** **die Balkenwaage.** Eine Federwaage liest die Masse an einer Skala ab und ist nur so genau wie ihre Feder. Eine
Balkenwaage vergleicht: Man legt so lange bekannte Gewichte auf, bis der Balken waagrecht steht. Der Zeiger in der Mitte muss nur zeigen, ob der Balken
kippt, nicht wie weit, und die Messung stimmt sogar auf dem Mond, wo alles weniger wiegt — beide Seiten werden gleichermaßen leichter.

Die Brücke ist eine solche Waage für Widerstände. Ihre beiden Seiten sind zwei Spannungsteiler an derselben Quelle, ihr Zeiger ist ein Messgerät zwischen
den beiden Teilermitten. Abgeglichen ist sie, wenn durch das Messgerät kein Strom fließt.

Drei Folgerungen kann man der Waage direkt ansehen:

- **Die Quelle spielt keine Rolle.** Wie die Balkenwaage auf dem Mond: Ist die Quellenspannung kleiner, teilen beide Teiler sie gleichermaßen.
- **Der Zeiger muss nur empfindlich sein, nicht genau.** Er zeigt null oder nicht null; sein Innenwiderstand ist im Abgleich gleichgültig.
- **Kleine Abweichungen werden sichtbar.** Ändert sich ein Widerstand ein wenig, kippt der Balken ein wenig — die Brücke zeigt den Unterschied, nicht den
  ganzen Wert. Ändern sich alle Widerstände gleich, etwa durch Wärme, bleibt sie im Gleichgewicht.

Das Bild trägt die Struktur, nicht die Physik: Eine Waage vergleicht Drehmomente, die Brücke Spannungsverhältnisse. Dass beide Bedingungen gleich
aussehen, ein Produkt gleich einem anderen, zeigt der Abschnitt über die Abgleichbedingung.

:::grafik
Szene: get1/strom-und-spannungsmessung/02-waage-bruecke · Vorlage: balkenwaage-bruecke
Links eine Balkenwaage mit Zeiger: Auf die linke Schale wird ein unbekanntes Gewicht gelegt, rechts kommen bekannte Gewichtsstücke dazu, bis der Zeiger
auf null steht. Ein Regler „Schwerkraft" verringert die Fallbeschleunigung wie auf dem Mond: Beide Schalen werden leichter, der Balken bleibt waagrecht.
Rechts die Brücke nach Bild 6.12 des Skripts: eine Quelle $U_q$, links $R_1$ über $R_2$, rechts $R_3$ über $R_4$, dazwischen ein Strommesser als
Nullindikator. Ein Regler verstellt $R_3$; der Zeiger des Strommessers schlägt nach links oder rechts aus und steht beim Abgleich auf null. Ein Regler für
$U_q$ ändert nichts am Abgleichpunkt. Kernaussage: Abgleichen heißt vergleichen; im Gleichgewicht zählen nur die Verhältnisse. (Rot = unbekannter Widerstand
und unbekanntes Gewicht, blau = Ströme, orange = Zeiger und Nullindikator, grau = Waage und Leitungen.)
:::

## Aufbau: zwei Teiler an einer Quelle

**Die Akteure** (Bild 6.12 des Skripts):

- eine Quelle mit der Spannung $U_q$;
- links ein Spannungsteiler aus $R_1$ oben und $R_2$ unten, rechts einer aus $R_3$ oben und $R_4$ unten, beide an $U_q$;
- zwischen den beiden Teilermitten, in der __Brückendiagonale__, ein empfindliches Messgerät als __Nullindikator__, im Skript ein Strommesser;
- die Ströme $I_1$ bis $I_4$ durch die vier Widerstände, alle von oben nach unten gezählt, und die Spannungen $U_2$ über $R_2$ und $U_4$ über $R_4$.

Die Rollen verteilt das Skript so: $R_4$ ist der unbekannte, gesuchte Widerstand, $R_3$ ein genau bekannter __Referenzwiderstand__, und von $R_1$ und $R_2$
muss man nur das Verhältnis kennen, das man einstellen kann; ihre Werte selbst sind gleichgültig.

Ohne Strom durch die Diagonale ist jeder Teiler unbelastet, und die Teilermitten liegen nach der Spannungsteilerregel auf

$$U_2 = U_q\,\frac{R_2}{R_1 + R_2}, \qquad U_4 = U_q\,\frac{R_4}{R_3 + R_4}.$$

Das Messgerät in der Diagonale sieht den Unterschied $U_2-U_4$.

**Im Bild:** Die beiden Waagschalen. Jede Seite stellt ihr eigenes Gleichgewicht her; der Zeiger in der Mitte vergleicht sie.

## Die Abgleichbedingung

**Das Zusammenspiel:** *Wann fließt durch die Diagonale kein Strom?*

:::formel Satz
$$R_4 = R_3\,\frac{R_2}{R_1} \qquad\Longleftrightarrow\qquad R_1\,R_4 = R_2\,R_3.$$
:::

**So liest man das:** Die Brücke ist __abgeglichen__, wenn die beiden Teiler im selben Verhältnis teilen (Gleichung 6.3 des Skripts). Dann liegen die
beiden Teilermitten auf demselben Potenzial, und durch die Diagonale fließt nichts. Ist $R_3$ bekannt und das Verhältnis $R_2/R_1$ eingestellt, folgt der
unbekannte Widerstand $R_4$. Die Quellenspannung kommt in der Bedingung nicht vor.

**Im Bild:** Der Balken steht waagrecht, wenn sich die beiden Produkte die Waage halten, wie beim Hebelgesetz: Gewicht mal Hebelarm links gleich Gewicht
mal Hebelarm rechts.

:::herleitung
**Kein Diagonalstrom.** Fließt durch die Diagonale kein Strom, geht nach der Knotenregel an jeder Teilermitte der ganze Strom weiter:

$$I_1 = I_2, \qquad I_3 = I_4.$$

**Gleiche Potenziale.** Ein idealer Strommesser hat den Innenwiderstand null; ohne Strom fällt an ihm aber ohnehin nichts ab. Die beiden Teilermitten
liegen also auf demselben Potenzial, und nach der Maschenregel sind die Spannungen über den unteren Widerständen gleich, ebenso über den oberen, denn beide
Teiler liegen an $U_q$:

$$U_{R2} = U_{R4}, \qquad U_{R1} = U_{R3}.$$

**Teilen.** Mit dem Ohmschen Gesetz und den gleichen Strömen ist das

$$R_2\,I_1 = R_4\,I_3, \qquad R_1\,I_1 = R_3\,I_3.$$

Teilt man die erste Gleichung durch die zweite, kürzen sich die Ströme:

$$\frac{R_2}{R_1} = \frac{R_4}{R_3}, \qquad R_4 = R_3\,\frac{R_2}{R_1}.$$

Dasselbe ergibt sich, wenn man die beiden Teilerspannungen aus dem vorigen Abschnitt gleichsetzt und über Kreuz multipliziert.
:::

::::beispiel Ein Widerstand im Abgleich
Mit $R_1$ gleich $1\,\text{k}\Omega$, $R_2$ gleich $2{,}5\,\text{k}\Omega$ und dem Referenzwiderstand $R_3$ von $470\,\Omega$ steht der Nullindikator auf null.
Der gesuchte Widerstand:

$$R_4 = 470\,\Omega\cdot\frac{2{,}5\,\text{k}\Omega}{1\,\text{k}\Omega} = 1175\,\Omega.$$

Probe mit $U_q$ gleich $10\,\text{V}$: Beide Teilermitten liegen auf demselben Potenzial,

$$U_2 = 10\,\text{V}\cdot\frac{2{,}5}{3{,}5} \approx 7{,}143\,\text{V}, \qquad U_4 = 10\,\text{V}\cdot\frac{1175}{1645} \approx 7{,}143\,\text{V}.$$

**Im Bild:** Auf der linken Schale liegt das Unbekannte, rechts der Referenzwiderstand, und der Hebelarm wurde im Verhältnis $2{,}5$ zu $1$ verstellt.
::::

## Warum die Nullmethode so genau ist

Die Brücke ist ein Beispiel für eine __Nullmethode__: Gemessen wird nicht ein Wert, sondern das Verschwinden eines Werts. Daraus folgen drei Vorteile.

**Die Quellenspannung kürzt sich heraus.** In der Abgleichbedingung kommt $U_q$ nicht vor. Schwankt die Quelle oder ist ihre Spannung nur ungefähr
bekannt, bleibt der Abgleichpunkt derselbe.

**Der Nullindikator muss nicht genau sein.** Sein Innenwiderstand und seine Skala gehen nicht ein: Im Abgleich fließt durch ihn nichts, und an einem
Widerstand ohne Strom fällt keine Spannung ab. Er muss nur empfindlich genug sein, um ein kleines Ungleichgewicht zu erkennen. Statt eines
Strommessers kann man deshalb auch einen Spannungsmesser nehmen (Bild 6.14 des Skripts) — beide zeigen im Abgleich null.

**Die Genauigkeit liegt in den Vergleichswiderständen.** Das Ergebnis hängt nur von $R_3$ und vom Verhältnis $R_2/R_1$ ab. Präzise Referenzwiderstände und
Verhältnisse lassen sich viel genauer herstellen als präzise Zeigerskalen.

**Im Bild:** Die Balkenwaage auf dem Mond: Sie zeigt dasselbe, weil beide Seiten gleich betroffen sind, und ihr Zeiger muss nur Kippen erkennen.

:::herleitung
**Wie der Nullindikator die Brücke sieht.** Vom Nullindikator aus verhält sich die Brücke wie eine Ersatzquelle (Artikel über die Zusammenschaltung): mit
der Leerlaufspannung $U_2-U_4$ und dem Innenwiderstand, den man zwischen den beiden Teilermitten sieht, wenn man die Quelle durch einen Kurzschluss
ersetzt. Dann liegen $R_1$ und $R_2$ parallel, ebenso $R_3$ und $R_4$, und beide Paare in Reihe:

$$R_\text{ers} = R_1 \parallel R_2 + R_3 \parallel R_4, \qquad I_\text{D} = \frac{U_2 - U_4}{R_\text{ers} + R_i}.$$

**Der Abgleichpunkt hängt nicht von $R_i$ ab.** Der Diagonalstrom $I_\text{D}$ ist genau dann null, wenn $U_2-U_4$ null ist, gleich wie groß der
Innenwiderstand $R_i$ des Nullindikators ist. $R_i$ bestimmt nur, wie stark er außerhalb des Abgleichs ausschlägt, also die Empfindlichkeit.

**Und nicht von $U_q$.** $U_2-U_4$ ist $U_q$ mal der Differenz zweier Teilerverhältnisse; sie ist null, wenn die Verhältnisse gleich sind, unabhängig von
$U_q$.
:::

::::beispiel Wie empfindlich der Nullindikator ist
Eine Brücke aus drei Widerständen von $1\,\text{k}\Omega$ und einem vierten von $1001\,\Omega$, also $0{,}1\,\%$ daneben, an $10\,\text{V}$:

$$U_2 - U_4 = 10\,\text{V}\cdot\Big(\frac{1000}{2000} - \frac{1001}{2001}\Big) \approx -2{,}50\,\text{mV}, \qquad R_\text{ers} \approx 1000\,\Omega.$$

Ein Nullindikator mit $100\,\Omega$ und einer mit $10\,\text{k}\Omega$ zeigen dann

$$I_\text{D} = \frac{-2{,}50\,\text{mV}}{1100\,\Omega} \approx -2{,}27\,\mu\text{A}, \qquad I_\text{D} = \frac{-2{,}50\,\text{mV}}{11\,\text{k}\Omega} \approx -0{,}23\,\mu\text{A}.$$

Beide stehen bei abgeglichener Brücke auf null; der niederohmige schlägt bei derselben Verstimmung zehnmal so stark aus und ist hier der empfindlichere
Strommesser. Als Spannungsmesser mit großem Innenwiderstand misst man dagegen die vollen $2{,}5\,\text{mV}$.

**Im Bild:** Zwei Zeiger an derselben Waage, einer schwergängig, einer leichtgängig: Beide stehen im Gleichgewicht senkrecht, aber nur der leichtgängige
verrät schon ein winziges Übergewicht.
::::

## Schleifdraht und Dekaden

**Die Schleifdrahtbrücke.** In der praktischen Ausführung (Bild 6.12 rechts) bestehen $R_1$ und $R_2$ aus einem einzigen gleichmäßigen Widerstandsdraht der
Länge $l$ mit dem Gesamtwiderstand $R_0$, auf dem ein Schleifkontakt läuft. Er sitzt an der Stelle $x$, vom unteren Ende aus gemessen; das Skript nennt sie
$\alpha$, doch $\alpha$ ist in diesen Artikeln schon der Temperaturkoeffizient. Abgeglichen wird, indem man den Kontakt verschiebt:

:::formel
$$R_2 = R_0\,\frac{x}{l}, \qquad R_1 = R_0\Big(1 - \frac{x}{l}\Big), \qquad R_4 = R_3\,\frac{x}{l - x}.$$
:::

**So liest man das:** Das Teilerverhältnis ist das Verhältnis der beiden Drahtstücke; $R_0$ kürzt sich heraus, sein Wert ist, wie das Skript sagt, ohne
Belang. Man braucht nur einen gleichmäßigen Draht und einen Maßstab. Am genauesten misst man, wenn der Kontakt nahe der Mitte steht, also mit einem
Referenzwiderstand ähnlich dem gesuchten.

**Im Bild:** Die __Laufgewichtswaage__: Man schiebt ein festes Gewicht am Balken entlang, bis er waagrecht steht, und liest die Masse an der Stelle ab.

:::herleitung
**Die Drahtstücke.** Nach dem Artikel über den Widerstand ist der Widerstand eines gleichmäßigen Drahts proportional zu seiner Länge. Das untere Stück hat
die Länge $x$, das obere $l-x$; ihre Anteile am Gesamtwiderstand sind die Anteile an der Länge. Eingesetzt in die Abgleichbedingung:

$$R_4 = R_3\,\frac{R_2}{R_1} = R_3\,\frac{R_0\,x/l}{R_0\,(l-x)/l} = R_3\,\frac{x}{l-x}.$$

**Wo es am genauesten ist.** Ein Ablesefehler $dx$ verändert das Verhältnis relativ um

$$\frac{d}{dx}\ln\frac{x}{l-x}\cdot dx = \Big(\frac{1}{x} + \frac{1}{l-x}\Big)dx = \frac{l}{x\,(l-x)}\,dx.$$

Der Faktor $\frac{l}{x(l-x)}$ ist in der Mitte, bei $x$ gleich $l/2$, am kleinsten und wächst zu den Enden hin stark.
:::

::::beispiel Ein Meter Draht
Ein Schleifdraht von $1\,\text{m}$; mit dem Referenzwiderstand $100\,\Omega$ steht der Abgleich bei $60\,\text{cm}$ vom unteren Ende:

$$R_4 = 100\,\Omega\cdot\frac{0{,}6\,\text{m}}{0{,}4\,\text{m}} = 150\,\Omega.$$

Ein Ablesefehler von $1\,\text{mm}$ verändert das Ergebnis um

$$\frac{1\,\text{m}}{0{,}6\,\text{m}\cdot0{,}4\,\text{m}}\cdot1\,\text{mm} \approx 0{,}42\,\%,$$

auf rund $150{,}6\,\Omega$. Stünde der Abgleich bei $90\,\text{cm}$, wären es schon $1{,}1\,\%$ — dann lieber einen größeren Referenzwiderstand wählen.

**Im Bild:** Steht das Laufgewicht nahe am Drehpunkt, verändert schon ein kleines Verschieben das Gleichgewicht stark.
::::

**Die Dekadenbrücke.** Genauer als ein Schleifdraht sind fest abgestufte Widerstände. In Bild 6.13 des Skripts ist der Referenzwiderstand $R_3$ aus
__Dekaden__ zusammengesetzt, je neun gleichen Widerständen von $100\,\Omega$, $10\,\Omega$, $1\,\Omega$ und $0{,}1\,\Omega$, mit Schaltern für jede Stelle.
Der Messwiderstand $R_m$ sitzt dort links unten, $R_2$ und $R_4$ oben, und die Abgleichbedingung lautet

$$R_m = R_3\,\frac{R_2}{R_4}.$$

Das Verhältnis $R_2/R_4$ ist ein Multiplikator in Zehnerpotenzen, die Stellen von $R_3$ liest man direkt ab. Genau so arbeitet das historische Gerät in
Bild 6.11: Der Drehknopf stellt die Dekaden ein, der mittlere Schalter den Multiplikator von $0{,}01$ bis $1000$.

**Im Bild:** Der Gewichtssatz einer Feinwaage, mit Stücken zu $100$, $10$, $1$ und $0{,}1\,\text{g}$, und dazu ein umschaltbarer Hebelarm.

:::herleitung
In Bild 6.13 bilden $R_2$ über $R_m$ den linken, $R_4$ über $R_3$ den rechten Teiler. Gleiche Teilerverhältnisse heißen

$$\frac{R_2}{R_m} = \frac{R_4}{R_3}, \qquad R_m = R_3\,\frac{R_2}{R_4}.$$

Mit vier Dekaden zu je neun Stufen lässt sich $R_3$ in Schritten von $0{,}1\,\Omega$ von $0$ bis $999{,}9\,\Omega$ einstellen.
:::

::::beispiel Eine Dekadenbrücke ablesen
Abgleich bei den Dekadenstellungen $4$, $7$, $3$ und $5$ und dem Multiplikator $10$:

$$R_3 = 4\cdot100\,\Omega + 7\cdot10\,\Omega + 3\cdot1\,\Omega + 5\cdot0{,}1\,\Omega = 473{,}5\,\Omega, \qquad R_m = 10\cdot473{,}5\,\Omega = 4735\,\Omega.$$

Vier gültige Stellen, ohne dass ein Messgerät einen einzigen Wert anzeigen musste.

**Im Bild:** Vier Gewichtsstücke zu $100$, sieben zu $10$, drei zu $1$ und fünf zu $0{,}1$, und der Hebelarm auf zehnfach.
::::

## Die verstimmte Brücke

Eine Brücke muss nicht abgeglichen werden, um nützlich zu sein. Ist sie in der Ruhelage abgeglichen und ändert sich dann ein Widerstand ein wenig, zeigt
die __Verstimmung__ $U_2-U_4$ diese Änderung an. Mit einem Spannungsmesser als Indikator, der keinen Strom zieht:

:::formel
$$U_2 - U_4 = U_q\Big(\frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4}\Big), \qquad U_2 - U_4 \approx -\frac{U_q}{4}\,\frac{\Delta R}{R}.$$
:::

**So liest man das:** Die erste Form gilt immer. Die zweite gilt für die __Viertelbrücke__: Drei Widerstände sind gleich $R$, der vierte, $R_4$, ist um den
kleinen Bruchteil $\frac{\Delta R}{R}$ größer. Die Verstimmung ist dann proportional zu dieser relativen Änderung, mit dem Faktor ein Viertel der
Quellenspannung; das Minus heißt, dass die rechte Teilermitte höher liegt.

**Im Bild:** Ein kleines Zusatzgewicht auf einer Schale kippt den Balken ein wenig, und der Ausschlag ist proportional zum Zusatzgewicht.

:::herleitung
**Allgemein.** Ohne Strom durch den Spannungsmesser sind beide Teiler unbelastet, und $U_2-U_4$ ist die Differenz der beiden Teilerspannungen.

**Viertelbrücke.** Mit $R_1$, $R_2$, $R_3$ gleich $R$ und $R_4$ gleich $R\,(1+\varepsilon)$, wobei $\varepsilon$ die relative Änderung $\Delta R/R$ ist:

$$U_2 - U_4 = U_q\Big(\frac12 - \frac{1+\varepsilon}{2+\varepsilon}\Big) = U_q\,\frac{(2+\varepsilon) - 2\,(1+\varepsilon)}{2\,(2+\varepsilon)} = -U_q\,\frac{\varepsilon}{2\,(2+\varepsilon)}.$$

Für kleine $\varepsilon$ ist der Nenner ungefähr $4$. Der Fehler dieser Näherung ist von der Größe $\varepsilon/2$, relativ gesehen: bei einem Prozent
Änderung ein halbes Prozent der Anzeige.
:::

**Dehnungsmessstreifen.** Ein __Dehnungsmessstreifen__, kurz DMS, ist eine dünne Metallfolie in Mäanderform, die auf ein Bauteil geklebt wird und sich mit
ihm dehnt. Seine relative Widerstandsänderung ist der __Dehnung__ $\varepsilon_l$ proportional, der relativen Längenänderung des Bauteils:

$$\frac{\Delta R}{R} = k\,\varepsilon_l.$$

Der __k-Faktor__ liegt bei Metallfolien um $2$. Weil die Änderungen winzig sind, oft ein Tausendstel und weniger, misst man sie in einer Brücke: Ein
Spannungsmesser mit $100\,\text{mV}$ Messbereich genügt, wo man ohne Brücke wenige Millivolt auf einigen Volt auflösen müsste.

:::herleitung
**Woher der k-Faktor kommt.** Nach dem Artikel über den Widerstand ist $R$ gleich $\rho\,l/A$. Für kleine Änderungen addieren sich die relativen
Änderungen der Faktoren, mit Minus für den Nenner:

$$\frac{\Delta R}{R} = \frac{\Delta\rho}{\rho} + \frac{\Delta l}{l} - \frac{\Delta A}{A}.$$

Beim Dehnen wird der Draht länger, $\frac{\Delta l}{l}$ ist $\varepsilon_l$, und zugleich dünner: Jede Querabmessung schrumpft um das $\nu$-fache der
Dehnung, mit der __Querkontraktionszahl__ $\nu$, bei Metallen etwa $0{,}3$. Der Querschnitt als Produkt zweier Querabmessungen schrumpft um das
Doppelte:

$$\frac{\Delta A}{A} = -2\,\nu\,\varepsilon_l, \qquad \frac{\Delta R}{R} = \frac{\Delta\rho}{\rho} + (1 + 2\nu)\,\varepsilon_l.$$

Die Geometrie allein gibt also etwa $1{,}6$; den Rest bis zum gemessenen k-Faktor um $2$ liefert die Änderung des spezifischen Widerstands beim Dehnen,
eine Materialeigenschaft.
:::

**Halb-, Vollbrücke und Temperaturausgleich.** Klebt man zwei DMS so, dass einer gedehnt und einer gestaucht wird, und setzt sie in denselben Teiler
($R_3$ gestaucht, $R_4$ gedehnt), verdoppelt sich die Verstimmung und wird exakt linear, die __Halbbrücke__. Mit vier aktiven DMS, in jedem Teiler einer
gedehnt und einer gestaucht, vervierfacht sie sich, die __Vollbrücke__. Und weil nur Unterschiede zählen: Ändern sich alle vier Widerstände gleich, etwa
durch Erwärmung, bleiben beide Teilerverhältnisse und damit der Abgleich unverändert.

**Im Bild:** Zusatzgewichte auf beiden Schalen heben sich auf; nur der Unterschied kippt den Balken.

:::herleitung
**Halbbrücke.** Links $R_1$ und $R_2$ gleich $R$, rechts $R_3$ gleich $R(1-\varepsilon)$ und $R_4$ gleich $R(1+\varepsilon)$. Der rechte Gesamtwiderstand
bleibt $2R$:

$$U_2 - U_4 = U_q\Big(\frac12 - \frac{1+\varepsilon}{2}\Big) = -\frac{U_q}{2}\,\varepsilon.$$

**Vollbrücke.** Zusätzlich $R_1$ gleich $R(1+\varepsilon)$ und $R_2$ gleich $R(1-\varepsilon)$; dann ist $U_2$ gleich $U_q\,\frac{1-\varepsilon}{2}$ und

$$U_2 - U_4 = U_q\Big(\frac{1-\varepsilon}{2} - \frac{1+\varepsilon}{2}\Big) = -U_q\,\varepsilon.$$

**Temperatur.** Wachsen alle vier Widerstände um denselben Faktor, kürzt er sich in jedem Teilerverhältnis heraus.
:::

**Das Beispiel des Skripts.** In Bild 6.15 ist $R_4$ der Dehnungsmessstreifen, rot und mit Pfeil gezeichnet, und gerechnet wird mit $R_4$ gleich
$101\,\Omega$. Im Text heißt es dagegen, man berechne „die Änderung des Widerstandes $R_3$". Mit $R_4$ als DMS ist die Verstimmung negativ, $U_2-U_4$
ergibt rund $-24{,}9\,\text{mV}$; das Skript gibt nur den Betrag $24{,}9\,\text{mV}$ an. Der Betrag stimmt und passt zur Näherung, ein Viertel von
$10\,\text{V}$ mal ein Prozent sind $25\,\text{mV}$.

::::beispiel Ein Dehnungsmessstreifen in drei Brücken
DMS mit $350\,\Omega$, k-Faktor $2$, an $5\,\text{V}$. Eine Dehnung von $0{,}5$ Promille ändert den Widerstand um

$$\frac{\Delta R}{R} = 2\cdot0{,}5\cdot10^{-3} = 10^{-3}, \qquad \Delta R = 0{,}35\,\Omega.$$

**(a) Viertelbrücke:**

$$U_2 - U_4 = -5\,\text{V}\cdot\frac{10^{-3}}{2\,(2+10^{-3})} \approx -1{,}249\,\text{mV}, \qquad \frac{5\,\text{V}}{4}\cdot10^{-3} = 1{,}25\,\text{mV}.$$

**(b) Halbbrücke:** $-2{,}50\,\text{mV}$, **(c) Vollbrücke:** $-5{,}00\,\text{mV}$, beide exakt linear.

**Ohne Brücke** läge der DMS in einem Teiler mit einem festen $350\,\Omega$: Die Spannung an ihm stiege von $2{,}5\,\text{V}$ auf

$$5\,\text{V}\cdot\frac{350{,}35}{700{,}35} \approx 2{,}50125\,\text{V},$$

ebenfalls um $1{,}25\,\text{mV}$, aber auf $2{,}5\,\text{V}$ obendrauf — das Messgerät müsste $0{,}05\,\%$ einer Spannung von Volt auflösen.

**Temperatur:** Werden alle vier DMS um $0{,}2\,\%$ wärmer und größer, bleibt die Vollbrücke bei $0\,\text{V}$.

**Im Bild:** Ein Zusatzgewicht von einem Tausendstel auf einer Schale: Die Waage zeigt nur dieses Tausendstel, nicht das ganze Gewicht.
::::

:::grafik
Szene: get1/strom-und-spannungsmessung/02-dms-bruecke · Vorlage: verstimmte-bruecke
Die Brücke nach Bild 6.15 des Skripts mit eigenen Werten: $U_q=5\,\text{V}$, vier Widerstände zu $350\,\Omega$, in der Diagonale ein Spannungsmesser, die
Spannungen $U_2$ über $R_2$ und $U_4$ über $R_4$ nach unten. Daneben ein Biegebalken, auf dem die DMS kleben. Ein Regler biegt den Balken: Der DMS auf der
Oberseite wird gedehnt (rot), einer auf der Unterseite gestaucht (blau); die Anzeige zeigt die Verstimmung, und ein Umschalter wechselt zwischen
Viertel-, Halb- und Vollbrücke, wobei der Ausschlag sich verdoppelt und vervierfacht. Ein zweiter Regler erwärmt alle DMS gleich: Die Anzeige bleibt
bei null. Kernaussage: Die Brücke misst Unterschiede und unterdrückt, was alle Zweige gleich trifft. (Rot = gedehnte DMS, blau = gestauchte, orange =
Verstimmung, grau = Balken und Leitungen.)
:::

## Messtechnik im Überblick

Das Skript schließt Kapitel 6 mit einer Vereinbarung: Sofern nicht ausdrücklich anders gesagt, gelten Messgeräte von nun an als **ideal** — Strommesser
mit verschwindendem, Spannungsmesser mit unendlich großem Innenwiderstand.

Zusammengefasst: Messgeräte haben einen Innenwiderstand, der vom idealen abweicht und eine Messung stark verfälschen kann; Strommesser sollen einen
möglichst kleinen, Spannungsmesser einen möglichst großen haben; Strom und Spannung lassen sich mit den Anzeigen allein nicht zugleich exakt messen, mit
bekannten Innenwiderständen aber korrigieren. Zur Brücke heißt es im Skript, mit ihr könne man „kleine Widerstände genau bestimmen". Gemeint sind, wie
das Skript selbst bei der Widerstandsmessung schreibt, kleinste **Widerstandsänderungen**. Für sehr kleine Widerstände unter etwa einem Ohm verfälschen
in der gewöhnlichen Brücke wieder Leitungs- und Kontaktwiderstände das Ergebnis; dafür gibt es die Vierleitermessung und eine erweiterte Brücke, die
Thomson-Brücke.

**Im Bild:** Eine Feinwaage wiegt keine Krümel, die an der Schale kleben bleiben — dafür braucht sie eine andere Bauart.

## Bedeutung und Ausblick

Die Brücke ist eine der ältesten Messschaltungen und heute in fast jedem Sensor zu finden. Eine Küchenwaage wiegt mit einer __Wägezelle__, einem
Metallkörper mit vier DMS in Vollbrücke — die elektrische Balkenwaage steckt also wörtlich in der echten. Drucksensoren, Kraftaufnehmer und
Temperaturfühler wie der Pt100 arbeiten ebenso.

Für die Netzwerkanalyse ist die Brücke außerdem ein Lehrstück: Mit einem Widerstand statt eines idealen Messgeräts in der Diagonale lässt sie sich nicht
mehr in Reihen und Parallelen zerlegen. Kapitel 7 zeigt, wie man solche Netze trotzdem behandelt, etwa mit der Stern-Dreieck-Umwandlung und mit
Ersatzquellen; die Kapitel 8 und 9 liefern die allgemeinen Verfahren.

:::kern
- Die __Wheatstonesche Messbrücke__ vergleicht zwei Spannungsteiler an derselben Quelle mit einem Nullindikator in der Diagonale.
- __Abgleichbedingung__: $R_1R_4=R_2R_3$; dann fließt durch die Diagonale kein Strom, und $R_4=R_3\frac{R_2}{R_1}$.
- __Nullmethode__: Der Abgleichpunkt hängt weder von der Quellenspannung noch vom Innenwiderstand des Indikators ab.
- Die Genauigkeit steckt im Referenzwiderstand und im Teilerverhältnis; der Indikator muss nur empfindlich sein.
- __Schleifdraht__: Das Verhältnis ist das der Drahtstücke, $R_4=R_3\frac{x}{l-x}$; am genauesten in der Mitte.
- __Dekadenbrücke__: Referenz aus Dekaden, Verhältnis als Multiplikator; man liest die Stellen direkt ab.
- __Verstimmte Viertelbrücke__: Die Verstimmung ist etwa ein Viertel der Quellenspannung mal der relativen Widerstandsänderung.
- __DMS__: relative Widerstandsänderung gleich k-Faktor mal Dehnung, $k$ um $2$; Halb- und Vollbrücke verdoppeln und vervierfachen.
- Gleiche Änderungen in allen Zweigen, etwa durch Wärme, heben sich auf.
:::

:::quiz
F: Was ist die Grundidee der Messbrücke, und was entspricht im Bild der Balkenwaage dem Abgleich?
A: Statt einen Wert abzulesen, vergleicht man den unbekannten Widerstand mit bekannten, bis ein Nullindikator nichts mehr anzeigt. Zwei Spannungsteiler an derselben Quelle sind die beiden Schalen, der Indikator in der Diagonale ist der Zeiger; abgeglichen ist die Brücke, wenn durch die Diagonale kein Strom fließt, wie der Balken waagrecht steht.
F: Wie leitet man die Abgleichbedingung her?
A: Ohne Diagonalstrom sind $I_1=I_2$ und $I_3=I_4$, und die beiden Teilermitten liegen auf demselben Potenzial, also $U_{R2}=U_{R4}$ und $U_{R1}=U_{R3}$. Mit Ohm ist das $R_2I_1=R_4I_3$ und $R_1I_1=R_3I_3$; geteilt kürzen sich die Ströme, und es bleibt $R_4=R_3\frac{R_2}{R_1}$, gleichbedeutend $R_1R_4=R_2R_3$.
F: Warum hängt der Abgleichpunkt nicht von der Quellenspannung ab?
A: Die Teilerspannungen sind $U_q$ mal ein Verhältnis; ihre Differenz verschwindet, wenn die Verhältnisse gleich sind, gleich wie groß $U_q$ ist. In der Abgleichbedingung kommt $U_q$ nicht vor — wie bei einer Balkenwaage, die auf dem Mond dasselbe zeigt.
F: Warum ist der Innenwiderstand des Nullindikators im Abgleich gleichgültig, und wofür zählt er doch?
A: Vom Indikator aus ist die Brücke eine Ersatzquelle mit der Leerlaufspannung $U_2-U_4$ und dem Innenwiderstand $R_1\parallel R_2+R_3\parallel R_4$; der Diagonalstrom ist $\frac{U_2-U_4}{R_\text{ers}+R_i}$. Er ist genau dann null, wenn $U_2-U_4$ null ist, gleich welches $R_i$. Außerhalb des Abgleichs bestimmt $R_i$ den Ausschlag, also die Empfindlichkeit.
F: Wie misst eine Schleifdrahtbrücke, und warum soll der Kontakt nahe der Mitte stehen?
A: $R_1$ und $R_2$ sind die beiden Stücke eines gleichmäßigen Drahts; ihr Verhältnis ist das der Längen, $R_4=R_3\frac{x}{l-x}$, und $R_0$ kürzt sich heraus. Ein Ablesefehler $dx$ verändert das Ergebnis relativ um $\frac{l}{x(l-x)}dx$, in der Mitte am wenigsten. Bei $1\,\text{m}$ Draht und $60\,\text{cm}$ macht $1\,\text{mm}$ rund $0{,}42\,\%$ aus.
F: Wie liest man eine Dekadenbrücke ab?
A: Der Referenzwiderstand besteht aus Dekaden zu je neun Stufen von $100$, $10$, $1$ und $0{,}1\,\Omega$, das Teilerverhältnis wirkt als Multiplikator in Zehnerpotenzen. Bei den Stellungen $4$, $7$, $3$, $5$ und dem Multiplikator $10$ ist der gesuchte Widerstand $10\cdot473{,}5\,\Omega=4735\,\Omega$.
F: Wie groß ist die Verstimmung einer Viertelbrücke, und woher kommt der Faktor ein Viertel?
A: Mit drei gleichen Widerständen $R$ und $R_4=R(1+\varepsilon)$ ist $U_2-U_4=-U_q\frac{\varepsilon}{2(2+\varepsilon)}$, für kleine $\varepsilon$ etwa $-\frac{U_q}{4}\varepsilon$. Die linke Mitte liegt bei der halben Quellenspannung, die rechte um rund $\frac{\varepsilon}{4}U_q$ höher. Beim DMS mit $\varepsilon=10^{-3}$ an $5\,\text{V}$ sind das $1{,}25\,\text{mV}$.
F: Woher kommt der k-Faktor eines Dehnungsmessstreifens?
A: Aus $R=\rho\frac lA$: Beim Dehnen wächst die Länge um $\varepsilon_l$, der Querschnitt schrumpft um $2\nu\varepsilon_l$, und die relativen Änderungen addieren sich. Die Geometrie gibt $(1+2\nu)\varepsilon_l$, mit $\nu\approx0{,}3$ also etwa $1{,}6\,\varepsilon_l$; den Rest bis zum k-Faktor um $2$ liefert die Änderung des spezifischen Widerstands.
F: Warum verwendet man Halb- und Vollbrücken, und warum stört eine Erwärmung nicht?
A: Mit einem gedehnten und einem gestauchten DMS im selben Teiler verdoppelt sich die Verstimmung auf $-\frac{U_q}{2}\varepsilon$ und wird exakt linear; mit vier aktiven DMS vervierfacht sie sich auf $-U_q\varepsilon$. Ändern sich alle Widerstände um denselben Faktor, kürzt er sich in jedem Teilerverhältnis heraus, und der Abgleich bleibt.
F: Welche Unstimmigkeiten hat das DMS-Beispiel des Skripts, und was bedeutet „kleine Widerstände" in seiner Zusammenfassung?
A: Bild und Rechnung verändern $R_4$ auf $101\,\Omega$, der Text spricht von $R_3$; mit $R_4$ als DMS ist $U_2-U_4$ rund $-24{,}9\,\text{mV}$, das Skript nennt nur den Betrag. In der Zusammenfassung sind kleine Widerstandsänderungen gemeint; sehr kleine Widerstände misst man wegen der Leitungswiderstände mit vier Leitern oder der Thomson-Brücke.
:::
