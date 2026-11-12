---
title: Stufe 2: Den Messbereich erweitern
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140300
summary: Das Messwerk endet bei 50 µ A und 100 mV.
tags: Shunt, Vorwiderstand
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Das Messwerk endet bei 50 µ A und 100 mV. Diese Stufe macht daraus ein Amperemeter bis 10 mA und ein Voltmeter bis 10 V und zeigt, woher $R_\mathrm{iA}$ und $R_\mathrm{iV}$ kommen.
:::

**Die Idee.** Das Messwerk verträgt nur 50 µ A. Soll es 10 mA anzeigen, muss der Rest vorbeifließen: Ein __Shunt__ (Nebenwiderstand) liegt parallel und übernimmt 9,95 mA. Soll es 10 V anzeigen, dürfen an ihm nur 100 mV liegen: Ein __Vorwiderstand__ in Reihe übernimmt 9,9 V (Abb. [2](#abb-2)). Das Messwerk sieht bei Vollausschlag dasselbe wie vorher, nur die Beschriftung der Skala ändert sich.

:::abbildung et1/k4bereich 2
Dasselbe Messwerk zweimal. Links teilt der Shunt den Strom im Verhältnis 199 zu 1, rechts teilt der Vorwiderstand die Spannung im Verhältnis 99 zu 1.
:::

:::satz Satz 2.1 (Shunt und Vorwiderstand)
<span class="anker" id="satz-2-1"></span>

Ein Instrument habe den Innenwiderstand $R_\mathrm{alt}$ und den Bereichsendwert $I_\mathrm{alt}$ beziehungsweise $U_\mathrm{alt}$. Für den neuen Endwert $I_\mathrm{neu}$ beziehungsweise $U_\mathrm{neu}=\alpha\,U_\mathrm{alt}$ braucht es

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{Shunt}=R_\mathrm{alt}\,\frac{I_\mathrm{alt}}{I_\mathrm{neu}-I_\mathrm{alt}},\qquad R_\mathrm V=R_\mathrm{alt}\,(\alpha-1). \tag{2.1}$$

Der neue Innenwiderstand ist $R_\mathrm{alt}\parallel R_\mathrm{Shunt}$ beziehungsweise $R_\mathrm{alt}+R_\mathrm V$.
:::

⁠**So liest man das:** $\alpha>1$ ist der Faktor der Erweiterung, ohne Einheit. $\parallel$ bedeutet parallel: $R_a\parallel R_b=R_aR_b/(R_a+R_b)$. Der Shunt ist klein gegen $R_\mathrm{alt}$, der Vorwiderstand groß. **Gültigkeit:** Der Ausschlag muss dem Strom proportional sein, und die Widerstände müssen genau sein, denn ihr Fehler geht in die Anzeige ein.

:::herleitung Stromteiler und Spannungsteiler
Shunt und Instrument liegen parallel, $G=1/R$ ist der Leitwert. Bei Vollausschlag gilt der Stromteiler

$$\frac{I_\mathrm{alt}}{I_\mathrm{neu}}=\frac{R_\mathrm{Shunt}}{R_\mathrm{Shunt}+R_\mathrm{alt}}=\frac{G_\mathrm{alt}}{G_\mathrm{Shunt}+G_\mathrm{alt}} \quad\Rightarrow\quad R_\mathrm{Shunt}=\frac{I_\mathrm{alt}}{I_\mathrm{neu}}\,(R_\mathrm{Shunt}+R_\mathrm{alt}).$$

Auflösen nach $R_\mathrm{Shunt}$ ergibt [(2.1)](#gl-2-1). Vorwiderstand und Instrument liegen in Reihe. Der Spannungsteiler gibt

$$U_\mathrm{alt}=U_\mathrm{neu}\,\frac{R_\mathrm{alt}}{R_\mathrm{alt}+R_\mathrm V} \quad\Rightarrow\quad \alpha=\frac{R_\mathrm{alt}+R_\mathrm V}{R_\mathrm{alt}}\quad\Rightarrow\quad R_\mathrm V=R_\mathrm{alt}\,(\alpha-1).$$
:::

::::beispiel
Für 10 mA: $R_\mathrm{Shunt}=2\,\mathrm{k\Omega}\cdot\frac{50\,\mu\text{A}}{9{,}95\,\mathrm{mA}}=10{,}05\,\Omega$, parallel zu 2 k$\Omega$ also $R_\mathrm{iA}=10\,\Omega$. Für 10 V: $\alpha=100$, $R_\mathrm V=2\,\mathrm{k\Omega}\cdot99=198$ k$\Omega$, also $R_\mathrm{iV}=200$ k$\Omega$.
::::

⁠**Kurz gesagt:** Am Amperemeter fallen bei Vollausschlag in jedem Bereich 100 mV ab, durch das Voltmeter fließen bei Vollausschlag in jedem Bereich 50 µ A. Daraus folgen die Innenwiderstände direkt: $R_\mathrm{iA}=100\,\mathrm{mV}/10\,\mathrm{mA}=10\,\Omega$ und $R_\mathrm{iV}=10\,\mathrm{V}/50\,\mu\text{A}=200$ k$\Omega$. Ein empfindlicher Strombereich hat also einen großen Innenwiderstand, ein hoher Spannungsbereich ebenfalls. Der Kehrwert von 50 µ A, 20 k$\Omega$/V, steht als Kennwert auf Zeigerinstrumenten.

⁠**Grenzfall:** Für $I_\mathrm{neu}\to I_\mathrm{alt}$ wird $R_\mathrm{Shunt}\to\infty$, für $\alpha=1$ wird $R_\mathrm V=0$. Ohne Erweiterung braucht man kein Bauteil.

**Mehrere Bereiche.** Ein Vielfachmessgerät (Gerät mit mehreren Bereichen) schaltet um (Abb. [3](#abb-3)). Beim Amperemeter legt jeder weitere Schalter einen Shunt parallel, beim Voltmeter gibt jeder weitere offene Schalter einen Vorwiderstand frei. Gleichung [(2.1)](#gl-2-1) gilt Schritt für Schritt: Das bisherige Gebilde ist das Instrument, sein Innenwiderstand heißt $R_\mathrm{alt}$.

:::abbildung et1/k4stufen 3
Stufenweise Erweiterung. Links kommt mit jedem geschlossenen Schalter ein Shunt hinzu, rechts mit jedem geöffneten Schalter ein Vorwiderstand.
:::

:::frage Macht der Shunt das Instrument empfindlicher?
Nein, unempfindlicher. Das Messwerk braucht weiter 50 µ A für den Vollausschlag, und der Shunt sorgt dafür, dass dazu erst 10 mA nötig sind.
:::

:::aufgabe Aufgabe 2 ★★ Stufenschalter
<span class="anker" id="aufg-2"></span>

Das Messwerk bekommt die Schaltungen aus Abb. [3](#abb-3). (a) Berechne $R_1$, $R_2$, $R_3$ für die Strombereiche 250 µ A, 1 mA, 10 mA und jeweils den Innenwiderstand. (b) Berechne $R_1$, $R_2$, $R_3$ für die Spannungsbereiche 1 V, 10 V, 100 V. (c) Prüfe beide Teile mit dem Satz aus „Kurz gesagt“.

:::loesung
(a) Mit [(2.1)](#gl-2-1) Schritt für Schritt:

$$\begin{aligned} R_1&=2\,\mathrm{k\Omega}\cdot\tfrac{50}{250-50}=500\,\Omega, & R^*&=2\,\mathrm{k\Omega}\parallel500\,\Omega=400\,\Omega,\\ R_2&=400\,\Omega\cdot\tfrac{250}{1000-250}=133{,}3\,\Omega, & R^{**}&=400\,\Omega\parallel133{,}3\,\Omega=100\,\Omega,\\ R_3&=100\,\Omega\cdot\tfrac{1}{10-1}=11{,}11\,\Omega, & R^{***}&=100\,\Omega\parallel11{,}11\,\Omega=10\,\Omega. \end{aligned}$$

Parallel ergeben die drei Shunts 10,05 $\Omega$, wie der einzelne Shunt im Beispiel.

(b) Jeder Schritt hat $\alpha=10$: $R_1=2\,\mathrm{k\Omega}\cdot9=18$ k$\Omega$ mit $R^*=20$ k$\Omega$, $R_2=20\,\mathrm{k\Omega}\cdot9=180$ k$\Omega$ mit $R^{**}=200$ k$\Omega$, $R_3=200\,\mathrm{k\Omega}\cdot9=1{,}8$ M$\Omega$ mit $R^{***}=2$ M$\Omega$.

(c) $250\,\mu\text{A}\cdot400\,\Omega=1\,\mathrm{mA}\cdot100\,\Omega=10\,\mathrm{mA}\cdot10\,\Omega=100$ mV. Beim Voltmeter ist $1\,\mathrm{V}/20\,\mathrm{k\Omega}=10\,\mathrm{V}/200\,\mathrm{k\Omega}=100\,\mathrm{V}/2\,\mathrm{M\Omega}=50$ µ A.
:::
:::

::::formelsammlung
**Shunt (Nebenwiderstand)**

$$R_\mathrm{Shunt}=R_\mathrm{alt}\,\frac{I_\mathrm{alt}}{I_\mathrm{neu}-I_\mathrm{alt}}$$

Parallel zum Instrument mit dem Innenwiderstand $R_\mathrm{alt}$ und dem Bereichsendwert $I_\mathrm{alt}$; $I_\mathrm{neu}$ ist der neue Endwert. Der neue Innenwiderstand ist $R_\mathrm{alt}\parallel R_\mathrm{Shunt}$, der Shunt ist klein gegen $R_\mathrm{alt}$. Folgt aus dem Stromteiler bei Vollausschlag. Für $I_\mathrm{neu}\to I_\mathrm{alt}$ wird $R_\mathrm{Shunt}\to\infty$.

**Vorwiderstand**

$$R_\mathrm V=R_\mathrm{alt}\,(\alpha-1),\qquad U_\mathrm{neu}=\alpha\,U_\mathrm{alt}$$

In Reihe zum Instrument; $\alpha>1$ ist der Faktor der Erweiterung, ohne Einheit. Der neue Innenwiderstand ist $R_\mathrm{alt}+R_\mathrm V$, der Vorwiderstand ist groß gegen $R_\mathrm{alt}$. Folgt aus dem Spannungsteiler. Beide Formeln setzen voraus, dass der Ausschlag dem Strom proportional ist und die Widerstände genau sind, denn ihr Fehler geht in die Anzeige ein. Bei mehreren Bereichen gelten sie Schritt für Schritt: Das bisherige Gebilde ist das Instrument.

**Parallelschaltung (Schreibweise)**

$$R_a\parallel R_b=R_aR_b/(R_a+R_b)$$

$\parallel$ bedeutet parallel.

**Innenwiderstand je Bereich**

$$R_\mathrm{iA}=100\,\mathrm{mV}/10\,\mathrm{mA}=10\,\Omega,\qquad R_\mathrm{iV}=10\,\mathrm{V}/50\,\mu\text{A}=200\,\mathrm{k\Omega}$$

Am Amperemeter fallen bei Vollausschlag in jedem Bereich die 100 mV des Messwerks ab, durch das Voltmeter fließen in jedem Bereich seine 50 µ A. Ein empfindlicher Strombereich hat also einen großen Innenwiderstand, ein hoher Spannungsbereich ebenfalls. Der Kehrwert von 50 µ A, 20 k$\Omega$/V, steht als Kennwert auf Zeigerinstrumenten.
::::

::::lernkarten
:::karte begriff Shunt
Was ist ein Shunt (Nebenwiderstand), und wozu dient er, wenn man den Strommessbereich eines Messwerks erweitert?
---
Ein Widerstand parallel zum Messwerk, der den Teil des Stroms übernimmt, den das Messwerk nicht verträgt. Bei Vollausschlag fließt so ein größerer Gesamtstrom; der Shunt ist klein gegen den Innenwiderstand des Instruments.
--- falsch
Ein Widerstand in Reihe zum Messwerk, der den Strom so weit bremst, dass das Messwerk ihn verträgt. Bei Vollausschlag fließt so weniger Strom; der Shunt ist groß gegen den Innenwiderstand des Instruments, damit er genug bremst.
--- falsch
Ein Widerstand parallel zum Messwerk, der den Strom durch das Messwerk verstärkt. So schlägt der Zeiger schon bei kleineren Strömen voll aus, und das Instrument wird empfindlicher.
--- falsch
Ein Schutzwiderstand, der das Messwerk bei zu großem Strom abtrennt. Im normalen Betrieb ist er unwirksam; er wird erst leitend, wenn der Bereichsendwert überschritten wird.
:::
:::karte begriff Vorwiderstand
Was ist ein Vorwiderstand, und wozu dient er, wenn man den Spannungsmessbereich eines Messwerks erweitert?
---
Ein Widerstand in Reihe zum Messwerk, der den Teil der Spannung übernimmt, den das Messwerk nicht verträgt. Bei Vollausschlag liegt so eine größere Gesamtspannung an; der Vorwiderstand ist groß gegen den Innenwiderstand des Instruments.
--- falsch
Ein Widerstand parallel zum Messwerk, der den Teil der Spannung ableitet, den das Messwerk nicht verträgt. Bei Vollausschlag liegt so eine größere Spannung an; der Vorwiderstand ist klein gegen den Innenwiderstand des Instruments, damit er gut ableitet.
--- falsch
Ein Widerstand vor der Quelle, der die zu messende Spannung vor dem Messen auf 100 mV herabsetzt. Danach zeigt das Messwerk die ursprüngliche Spannung ohne jede Umrechnung an.
--- falsch
Ein Widerstand in Reihe zum Messwerk, der den Strom durch das Messwerk erhöht, damit der Zeiger auch bei hohen Spannungen weit genug ausschlägt; er ist klein gegen den Innenwiderstand.
:::
:::karte formel Shunt
Wie groß muss der Shunt sein, wenn ein Instrument mit dem Innenwiderstand $R_\mathrm{alt}$ statt bis $I_\mathrm{alt}$ künftig bis $I_\mathrm{neu}$ anzeigen soll, und welchen Innenwiderstand hat es danach?
---
$R_\mathrm{Shunt}=R_\mathrm{alt}\,\frac{I_\mathrm{alt}}{I_\mathrm{neu}-I_\mathrm{alt}}$; der neue Innenwiderstand ist $R_\mathrm{alt}\parallel R_\mathrm{Shunt}$. Vorausgesetzt ist, dass der Ausschlag dem Strom proportional ist und die Widerstände genau sind.
--- falsch
$R_\mathrm{Shunt}=R_\mathrm{alt}\,\frac{I_\mathrm{neu}}{I_\mathrm{neu}-I_\mathrm{alt}}$; der neue Innenwiderstand ist $R_\mathrm{alt}\parallel R_\mathrm{Shunt}$. Das gilt auch dann, wenn der Ausschlag dem Strom nicht proportional ist, weil nur der Endwert zählt.
--- falsch
$R_\mathrm{Shunt}=R_\mathrm{alt}\,\frac{I_\mathrm{alt}}{I_\mathrm{neu}-I_\mathrm{alt}}$; der neue Innenwiderstand ist $R_\mathrm{alt}+R_\mathrm{Shunt}$, weil der Shunt zum Instrument hinzukommt und sich Widerstände addieren.
--- falsch
$R_\mathrm{Shunt}=R_\mathrm{alt}\,(I_\mathrm{neu}/I_\mathrm{alt}-1)$; der neue Innenwiderstand ist $R_\mathrm{alt}+R_\mathrm{Shunt}$. Der Shunt ist dabei groß gegen den Innenwiderstand $R_\mathrm{alt}$.
:::
:::karte formel Vorwiderstand
Wie groß muss der Vorwiderstand sein, wenn ein Instrument mit dem Innenwiderstand $R_\mathrm{alt}$ statt bis $U_\mathrm{alt}$ künftig bis $U_\mathrm{neu}=\alpha\,U_\mathrm{alt}$ anzeigen soll, und welchen Innenwiderstand hat es danach?
---
$R_\mathrm V=R_\mathrm{alt}\,(\alpha-1)$ mit dem Faktor $\alpha>1$ ohne Einheit; der neue Innenwiderstand ist $R_\mathrm{alt}+R_\mathrm V$. Der Vorwiderstand ist groß gegen $R_\mathrm{alt}$.
--- falsch
$R_\mathrm V=R_\mathrm{alt}\,\alpha$ mit dem Faktor $\alpha>1$ ohne Einheit; der neue Innenwiderstand ist $R_\mathrm{alt}+R_\mathrm V$, also das $(\alpha+1)$-Fache von $R_\mathrm{alt}$.
--- falsch
$R_\mathrm V=R_\mathrm{alt}/(\alpha-1)$ mit dem Faktor $\alpha>1$ ohne Einheit; der neue Innenwiderstand ist $R_\mathrm{alt}\parallel R_\mathrm V$, also kleiner als $R_\mathrm{alt}$.
--- falsch
$R_\mathrm V=R_\mathrm{alt}\,(\alpha-1)$ mit dem Faktor $\alpha>1$; der Innenwiderstand bleibt aber $R_\mathrm{alt}$, weil der Vorwiderstand außerhalb des Messwerks liegt.
:::
:::karte herleitung Shunt aus dem Stromteiler
Leite aus dem Stromteiler bei Vollausschlag die Formel für den Shunt her, der den Bereich eines Instruments von $I_\mathrm{alt}$ auf $I_\mathrm{neu}$ erweitert.
---
Shunt und Instrument liegen parallel, weil der Überschuss am Messwerk vorbeifließen soll; bei Vollausschlag fließt $I_\mathrm{alt}$ durch das Instrument und $I_\mathrm{neu}$ insgesamt.
---
Der Stromteiler gibt $\frac{I_\mathrm{alt}}{I_\mathrm{neu}}=\frac{R_\mathrm{Shunt}}{R_\mathrm{Shunt}+R_\mathrm{alt}}=\frac{G_\mathrm{alt}}{G_\mathrm{Shunt}+G_\mathrm{alt}}$, weil sich der Strom auf parallele Zweige im Verhältnis ihrer Leitwerte $G=1/R$ aufteilt.
---
Malnehmen mit dem Nenner ergibt $R_\mathrm{Shunt}=\frac{I_\mathrm{alt}}{I_\mathrm{neu}}\,(R_\mathrm{Shunt}+R_\mathrm{alt})$, weil so $R_\mathrm{Shunt}$ allein auf der linken Seite steht.
---
Auflösen nach $R_\mathrm{Shunt}$ ergibt $R_\mathrm{Shunt}=R_\mathrm{alt}\,\frac{I_\mathrm{alt}}{I_\mathrm{neu}-I_\mathrm{alt}}$, weil beim Zusammenfassen der Glieder mit $R_\mathrm{Shunt}$ (nach Malnehmen mit $I_\mathrm{neu}$) der Faktor $I_\mathrm{neu}-I_\mathrm{alt}$ entsteht.
:::
:::karte herleitung Vorwiderstand aus dem Spannungsteiler
Leite aus dem Spannungsteiler bei Vollausschlag die Formel für den Vorwiderstand her, der den Bereich eines Instruments um den Faktor $\alpha$ erweitert.
---
Vorwiderstand und Instrument liegen in Reihe, weil der Vorwiderstand den Überschuss der Spannung übernehmen soll; bei Vollausschlag liegt $U_\mathrm{alt}$ am Instrument und $U_\mathrm{neu}$ an beiden zusammen.
---
Der Spannungsteiler gibt $U_\mathrm{alt}=U_\mathrm{neu}\,\frac{R_\mathrm{alt}}{R_\mathrm{alt}+R_\mathrm V}$, weil durch beide derselbe Strom fließt und sich die Spannung im Verhältnis der Widerstände aufteilt.
---
Mit $U_\mathrm{neu}=\alpha\,U_\mathrm{alt}$ folgt $\alpha=\frac{R_\mathrm{alt}+R_\mathrm V}{R_\mathrm{alt}}$, weil man beide Seiten durch $U_\mathrm{alt}$ teilt und den Bruch umkehrt.
---
Auflösen ergibt $R_\mathrm V=R_\mathrm{alt}\,(\alpha-1)$, weil man mit $R_\mathrm{alt}$ malnimmt und $R_\mathrm{alt}$ abzieht.
:::
:::karte zusammenhang Was das Messwerk sieht
Was ändert sich für das Messwerk selbst, wenn man seinen Bereich mit einem Shunt oder einem Vorwiderstand erweitert?
---
Nichts: Bei Vollausschlag fließen weiter 50 µ A durch das Messwerk, und es liegen weiter 100 mV an. Shunt und Vorwiderstand übernehmen den Überschuss; nur die Beschriftung der Skala ändert sich.
--- falsch
Es braucht danach mehr Strom für den Vollausschlag, im 10-mA-Bereich also die vollen 10 mA; dafür ist seine Spule dicker gewickelt als beim Messwerk ohne Erweiterung.
--- falsch
Es bekommt einen kleineren Eigenwiderstand, weil der Shunt beziehungsweise der Vorwiderstand ein Teil von ihm wird; deshalb schlägt es danach schon bei kleineren Strömen voll aus als vorher.
--- falsch
Seine Feder wird gegen eine steifere getauscht, damit der Zeiger erst bei größeren Strömen voll ausschlägt; Shunt und Vorwiderstand schützen es nur vor Überlast.
:::
:::karte zusammenhang Empfindlicher Bereich, großer Innenwiderstand
Warum hat ein empfindlicher Strombereich einen großen Innenwiderstand und ein hoher Spannungsbereich ebenfalls?
---
Am Amperemeter fallen bei Vollausschlag in jedem Bereich 100 mV ab, also braucht ein kleiner Endstrom einen großen Widerstand. Durch das Voltmeter fließen in jedem Bereich 50 µ A, also braucht eine große Endspannung einen großen Widerstand.
--- falsch
Ein empfindlicher Strombereich braucht eine Spule mit mehr Windungen und damit mehr Draht, der Widerstand hat; ein hoher Spannungsbereich braucht eine dicke Isolation, deren Widerstand zum Innenwiderstand des Geräts hinzukommt.
--- falsch
Das stimmt nur beim Voltmeter: Ein empfindlicher Strombereich hat einen kleinen Innenwiderstand, weil er den kleinen Strom, den er messen soll, möglichst wenig behindern darf.
--- falsch
Weil das Gerät in beiden Fällen die Schaltung schonen soll: Der Innenwiderstand wird in jedem Bereich so groß gewählt wie der Widerstand, an dem gemessen wird, damit sich Strom und Spannung durch das Messen nicht verschieben.
:::
:::karte zusammenhang Kennwert von Zeigerinstrumenten
Was bedeutet der Kennwert 20 k$\Omega$/V auf einem Zeigerinstrument mit 50 µ A Vollausschlag?
---
Er ist der Kehrwert von 50 µ A: Jedes Volt Bereichsendwert bringt 20 k$\Omega$ Innenwiderstand, im 10-V-Bereich also $R_\mathrm{iV}=10\,\mathrm{V}/50\,\mu\text{A}=200$ k$\Omega$.
--- falsch
Er ist der Widerstand der Messleitungen je Volt Messspannung: Bei 10 V tragen die Leitungen 200 k$\Omega$ bei, das Messwerk selbst bleibt dabei bei seinen 2 k$\Omega$.
--- falsch
Er gibt an, wie stark der Innenwiderstand mit jedem Volt an den Anschlüssen sinkt: Liegen 10 V an, sind es 200 k$\Omega$ weniger als im spannungslosen Zustand.
--- falsch
Er ist die höchste Spannung je Kiloohm, die das Gerät verträgt: An einem Bauteil von 20 k$\Omega$ darf man also höchstens 1 V messen, sonst wird das Messwerk überlastet.
:::
:::karte zusammenhang Shunt und Empfindlichkeit
Macht ein Shunt das Instrument empfindlicher oder unempfindlicher, und warum?
---
Unempfindlicher: Das Messwerk braucht weiter 50 µ A für den Vollausschlag, und der Shunt sorgt dafür, dass dazu insgesamt erst 10 mA nötig sind.
--- falsch
Empfindlicher: Er leitet zusätzlichen Strom in das Messwerk, sodass schon kleinere Ströme im Kreis den Vollausschlag des Zeigers erreichen.
--- falsch
Weder noch: Der Shunt ändert nur den Innenwiderstand des Geräts; die Empfindlichkeit legt allein die Feder fest, und die bleibt dieselbe.
--- falsch
Empfindlicher: Weil sein Widerstand klein ist, fließt mehr Strom durch den Kreis, und das Messwerk reagiert stärker auf jede kleine Änderung.
:::
:::karte zusammenhang Ohne Erweiterung
Was ergeben die Formeln für Shunt und Vorwiderstand, wenn der Bereich gar nicht erweitert wird?
---
Für $I_\mathrm{neu}\to I_\mathrm{alt}$ wird $R_\mathrm{Shunt}\to\infty$, für $\alpha=1$ wird $R_\mathrm V=0$. Ein unendlicher Shunt ist eine offene Stelle, ein Vorwiderstand null ein Stück Draht: Ohne Erweiterung braucht man kein Bauteil.
--- falsch
Für $I_\mathrm{neu}\to I_\mathrm{alt}$ wird $R_\mathrm{Shunt}\to0$, für $\alpha=1$ wird $R_\mathrm V\to\infty$. Das Messwerk ist dann kurzgeschlossen beziehungsweise abgetrennt und zeigt überhaupt nichts mehr an.
--- falsch
Beide Formeln werden ungültig, weil durch null geteilt wird. Deshalb muss jedes Instrument mindestens einen Shunt und einen Vorwiderstand enthalten, auch wenn es nur einen Bereich hat.
--- falsch
Für $I_\mathrm{neu}\to I_\mathrm{alt}$ wird $R_\mathrm{Shunt}=R_\mathrm{alt}$, für $\alpha=1$ ebenso $R_\mathrm V=R_\mathrm{alt}$. Shunt und Vorwiderstand sind dann genau so groß wie das Messwerk selbst.
:::
:::karte zusammenhang Vielfachmessgerät
Wie schaltet ein Vielfachmessgerät (Gerät mit mehreren Bereichen) seine Bereiche um, und wie berechnet man die einzelnen Widerstände?
---
Beim Amperemeter legt jeder weitere Schalter einen Shunt parallel, beim Voltmeter gibt jeder weitere offene Schalter einen Vorwiderstand frei. Gerechnet wird Schritt für Schritt: Das bisherige Gebilde ist das Instrument mit dem Innenwiderstand $R_\mathrm{alt}$.
--- falsch
Für jeden Bereich gibt es ein eigenes Messwerk mit eigener Feder; der Schalter wählt das passende aus. Shunts und Vorwiderstände braucht ein solches Gerät deshalb nicht, die Skalen sind fest beschriftet.
--- falsch
Beim Amperemeter legt jeder weitere Schalter einen Vorwiderstand in Reihe, beim Voltmeter einen Shunt parallel. Jeder Widerstand wird dabei stets mit dem Messwerk allein als $R_\mathrm{alt}$ berechnet, gleich wie viele Schalter schon geschlossen sind.
--- falsch
Jeder Schalter legt einen Shunt parallel, beim Amperemeter wie beim Voltmeter. Alle Widerstände berechnet man mit dem Messwerk allein als $R_\mathrm{alt}$, weil die schon zugeschalteten Shunts nicht mitzählen.
:::
::::
