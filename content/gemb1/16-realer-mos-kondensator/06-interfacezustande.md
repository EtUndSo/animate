---
title: Stufe 4: Interfacezustände
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260600
summary: Die bisherigen Ladungen sind fest.
tags: arteigenes Oxid, Leitungsbandartige, Valenzbandartige, Ladungsneutralitätsniveau, Fermi-Level-Pinning
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die bisherigen Ladungen sind fest. An der Grenzfläche gibt es aber auch Zustände, deren Ladung sich mit der Bandverbiegung ändert. Diese Stufe zeigt, woher sie kommen und was sie bewirken.
:::

**Die Idee.** Im Kristall hat jedes Siliziumatom vier Bindungen. An einer Oberfläche fehlen die Partner: Jedes Atom einer $(100)$-Fläche behält zwei offene Bindungen (engl. dangling bonds), das sind über $10^{15}$ je cm$^2$. Eine offene Bindung liegt energetisch zwischen den bindenden Zuständen des Valenzbands und den antibindenden des Leitungsbands, also in der Bandlücke. Wächst das Oxid aus dem Silizium selbst (__arteigenes Oxid__), bindet fast jede davon an Sauerstoff, die Atome nahe der Grenzfläche verschieben sich nur etwas. Das senkt die Dichte der Zustände um den Faktor von rund 100 000. Die übrigen Zustände sitzen fest an der Grenzfläche und wandern mit den Bändern. Hebt das Gate die Bandverbiegung, sinken sie unter $E_\mathrm F$ und füllen sich mit Elektronen (Abb. [4](#abb-4)). Ein Teil der Ladung, die das Gate verlangt, landet also in ihnen statt im Halbleiter.

:::abbildung gemb1/k16zustaende 4
Interfacezustände als Streifen an der Grenzfläche, Isolator links, Substrat rechts. Sie wandern mit den Bändern. Bei $V_\mathrm{FB}$ liegt $E_\mathrm F$ unter $E_\mathrm{CNL}$, es bleiben donatorartige Zustände leer: positive Ladung. Bei $V_\mathrm G>V_\mathrm{FB}$ liegt $E_\mathrm F$ über $E_\mathrm{CNL}$, akzeptorartige Zustände sind besetzt: negative Ladung.
:::

:::definition Definition 4.1 (Interfacezustände)
<span class="anker" id="satz-4-1"></span>

Die Interfacezustände werden auch Grenzflächenzustände genannt. $D_\mathrm{it}$ ist ihre Zahl je Fläche und je Energie. __Leitungsbandartige__ Zustände verhalten sich wie Akzeptoren: neutral, wenn leer, negativ, wenn besetzt. __Valenzbandartige__ Zustände verhalten sich wie Donatoren: positiv, wenn leer, neutral, wenn besetzt. Das __Ladungsneutralitätsniveau__ $E_\mathrm{CNL}$ trennt beide Sorten.
:::

⁠**So liest man das:** Liegt $E_\mathrm F$ an der Grenzfläche auf $E_\mathrm{CNL}$, ist sie neutral, darüber negativ, darunter positiv. $D_\mathrm{it}$ misst man in 1/(eV cm$^2$). Eine offene Fläche hat rund $10^{15}$, ein gewachsenes Oxid $5\cdot10^{11}$, und nach dem Tempern in Wasserstoff, der offene Bindungen absättigt, sind es rund $10^{10}$.

:::satz Satz 4.2 (Wirkung der Interfacezustände)
<span class="anker" id="satz-4-2"></span>

Die Ladung $Q'_\mathrm{it}$ der Zustände zählt die Änderung gegenüber dem Flachbandfall. Die Ladung im Flachbandfall gehört zu $Q'_\mathrm{SS}$. Für konstantes $D_\mathrm{it}$ gilt

<span class="anker" id="gl-4-1"></span>
$$Q'_\mathrm{it}(\varphi_\mathrm s)=-e^2D_\mathrm{it}\,\varphi_\mathrm s,\qquad C'_\mathrm{it}=\Bigl|\frac{\mathrm{d} Q'_\mathrm{it}}{\mathrm{d}\varphi_\mathrm s}\Bigr|\approx e^2D_\mathrm{it}, \tag{4.1}$$

<span class="anker" id="gl-4-2"></span>
$$V_\mathrm G=V_\mathrm{FB}+\varphi_\mathrm s-\frac{Q'_\mathrm{SC}+Q'_\mathrm{it}}{C'_\mathrm{IS}},\qquad\frac{\mathrm{d}\varphi_\mathrm s}{\mathrm{d} V_\mathrm G}=\frac{C'_\mathrm{IS}}{C'_\mathrm{IS}+C'_\mathrm{SC}+C'_\mathrm{it}}, \tag{4.2}$$

<span class="anker" id="gl-4-3"></span>
$$C'_\mathrm{ges}=\frac{\bigl(C'_\mathrm{depl}+C'_\mathrm{it}+C'_\mathrm{inv/acc}\bigr)\,C'_\mathrm{IS}}{C'_\mathrm{depl}+C'_\mathrm{it}+C'_\mathrm{inv/acc}+C'_\mathrm{IS}}. \tag{4.3}$$
:::

⁠**So liest man das:** $C'_\mathrm{it}$ liegt parallel zu den Kapazitäten im Halbleiter, denn alle reagieren auf dasselbe $\mathrm{d}\varphi_\mathrm s$. Mit $D_\mathrm{it}$ in 1/(eV m$^2$) ist $C'_\mathrm{it}=eD_\mathrm{it}$ in F/m$^2$. **Gültigkeit:** Die Besetzung folgt $E_\mathrm F$, und $D_\mathrm{it}$ ändert sich im betrachteten Energiebereich wenig.

:::herleitung Die Ableitung der Fermi-Funktion pickt $E_\mathrm F$ heraus
Ein Zustand mit der Energie $E$ im Flachbandfall liegt bei Bandverbiegung auf $E-e\varphi_\mathrm s$. Bis auf eine Konstante ist die Ladung also

$$Q'_\mathrm{it}=-e\int\!\mathrm{d} E\,D_\mathrm{it}\,f(E-e\varphi_\mathrm s),\qquad\frac{\mathrm{d} Q'_\mathrm{it}}{\mathrm{d}\varphi_\mathrm s}=e^2\int\!\mathrm{d} E\,D_\mathrm{it}\,\frac{\partial f}{\partial E}\approx-e^2D_\mathrm{it}(E_\mathrm F).$$

$-\partial f/\partial E$ ist eine Spitze der Fläche 1 und der Breite $3{,}5\,k_\mathrm BT=90$ meV und wirkt wie eine Deltafunktion. In der Neutralität kommt $Q'_\mathrm{it}$ hinzu. Ableiten ergibt $\mathrm{d} V_\mathrm G=\mathrm{d}\varphi_\mathrm s\,(1+(C'_\mathrm{SC}+C'_\mathrm{it})/C'_\mathrm{IS})$ und $C'_\mathrm{ges}=(C'_\mathrm{SC}+C'_\mathrm{it})\,\mathrm{d}\varphi_\mathrm s/\mathrm{d} V_\mathrm G$, wie in [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html).
:::

::::beispiel
Getempert mit $D_\mathrm{it}=10^{10}/(\mathrm{eV\,cm^2})$ ist $C'_\mathrm{it}=1{,}6\,\mathrm{nF/cm^2}$, das sind 0,9 % von $C'_\mathrm{IS}$, und $V_\mathrm{th}$ steigt nur um 7 mV. Ungetempert mit $5\cdot10^{11}/(\mathrm{eV\,cm^2})$ sind es 80,1 nF/cm$^2$ und 46 %. Bis $\varphi_\mathrm{s,SI}$ nehmen die Zustände dann $3{,}9\cdot10^{11}$ Elektronen je cm$^2$ auf, also $Q'_\mathrm{it}=-62{,}3\,\mathrm{nC/cm^2}$, und $V_\mathrm{th}$ steigt um 0,361 V auf 0,684 V. Bei $\varphi_\mathrm s=0{,}3$ V sinkt $\mathrm{d}\varphi_\mathrm s/\mathrm{d} V_\mathrm G$ von 0,655 auf 0,502: Das Gate verliert Steuerwirkung.
::::

⁠**Grenzfall:** Eine offene Fläche mit $10^{15}/(\mathrm{eV\,cm^2})$ hat $C'_\mathrm{it}=160$ µ F/cm$^2$, das 928-Fache von $C'_\mathrm{IS}$. Dann ist $\mathrm{d}\varphi_\mathrm s/\mathrm{d} V_\mathrm G=1{,}1\cdot10^{-3}$, ein Volt am Gate bewegt die Bänder um 1 mV. $E_\mathrm F$ steckt an der Grenzfläche fest, das heißt __Fermi-Level-Pinning__. Erst das arteigene Oxid macht die Oberfläche steuerbar.

**Bandverbiegung ohne Spannung.** Geladene Zustände verbiegen die Bänder auch ohne Gate. Auf einem n-Halbleiter nimmt ein akzeptorartiger Zustand unter $E_\mathrm F$ ein Elektron auf. Die negative Oberfläche drückt Elektronen in die Tiefe, es entsteht eine positive Verarmungszone, und die Bänder biegen nach oben. Auf einem p-Halbleiter gibt ein donatorartiger Zustand über $E_\mathrm F$ ein Elektron ab, das mit einem Loch rekombiniert. Die positive Oberfläche ergibt eine negative Verarmungszone, die Bänder biegen nach unten.

:::frage Ist $Q'_\mathrm{it}$ nicht dasselbe wie $Q'_\mathrm{SS}$?
Beide sitzen an der Grenzfläche, aber $Q'_\mathrm{SS}$ hängt nicht von $V_\mathrm G$ ab und verschiebt deshalb nur die Kurven. $Q'_\mathrm{it}$ ändert sich mit $\varphi_\mathrm s$ und dehnt sie: Die Verschiebung wächst mit der Bandverbiegung.
:::

:::aufgabe Aufgabe 6 ★★ Wie viel Dichte verträgt das Gate?
<span class="anker" id="aufg-6"></span>

Rechne im Rechenmodell mit $D_\mathrm{it}=2\cdot10^{10}$ und $8\cdot10^{11}/(\mathrm{eV\,cm^2})$.

<ol class="al">

<li>

Berechne $C'_\mathrm{it}$, das Verhältnis zu $C'_\mathrm{IS}$ und den Anstieg von $V_\mathrm{th}$.

</li>

<li>

Berechne $\mathrm{d}\varphi_\mathrm s/\mathrm{d} V_\mathrm G$ bei $\varphi_\mathrm s=0{,}3$ V mit $C'_\mathrm{depl}=91{,}1\,\mathrm{nF/cm^2}$, auch ohne Zustände.

</li>

<li>

Bei welchem $D_\mathrm{it}$ sinkt $\mathrm{d}\varphi_\mathrm s/\mathrm{d} V_\mathrm G$ auf 0,1?

</li>

</ol>

:::loesung
(a) $2\cdot10^{10}$: $3{,}2\,\mathrm{nF/cm^2}$, Verhältnis 0,019, Anstieg 14 mV. $8\cdot10^{11}$: $128{,}2\,\mathrm{nF/cm^2}$, Verhältnis 0,742, Anstieg 0,577 V. (b) Ohne Zustände 0,655, mit ihnen 0,647 und 0,441. (c) $C'_\mathrm{it}=9\,C'_\mathrm{IS}-C'_\mathrm{depl}=1463\,\mathrm{nF/cm^2}$, also $D_\mathrm{it}=9{,}1\cdot10^{12}/(\mathrm{eV\,cm^2})$.
:::
:::
