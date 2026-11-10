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
