---
title: Stufe 2: Reflexion trotz genügender Energie
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4130400
summary: Das Elektron hat genug Energie für die Kante, klassisch käme jedes hinüber.
tags: Teilchenstromdichte, Reflexionskoeffizient
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Das Elektron hat genug Energie für die Kante, klassisch käme jedes hinüber. Die Amplituden aus Stufe [1](zwei-gebiete-an-einer-kante-zusammensetzen.html#stufe-1) sagen etwas anderes. Hier wird aus ihnen der Anteil der Elektronen, der wirklich hinüberkommt.
:::

**Die Idee.** An der Kante springt die Wellenzahl. Eine durchgehende Welle allein könnte nicht zugleich im Wert und in der Steigung passen: Mit $C=A$ wäre die Steigung rechts um den Faktor $k_\mathrm{II}/k_\mathrm I$ zu klein. Die Bedingungen [(1.3)](zwei-gebiete-an-einer-kante-zusammensetzen.html#gl-1-3) lassen sich nur erfüllen, wenn ein Teil der Welle zurückläuft. Die Stetigkeit erzeugt also die Reflexion, nicht ein Stoß gegen ein Hindernis.

Zum Zählen braucht man Teilchenströme. Die __Teilchenstromdichte__ ist klassisch $\mathcal J=N_\mathrm V\,v$ mit $N_\mathrm V$ Teilchen je Volumen und der Geschwindigkeit $v$. Im Festkörper ist $v$ meist proportional zum elektrischen Feld, $v=\mu\,\mathcal E$ mit der Beweglichkeit $\mu$. Für $N$ gleiche Teilchen, die nicht aufeinander wirken, ist $N_\mathrm V=N\,|\psi|^2$. Auf ein Teilchen entfällt damit

<span class="anker" id="gl-2-1"></span>
$$\mathcal J_\mathrm e=|\psi|^2\,v. \tag{2.1}$$

:::definition Definition 2.1 (Reflexions- und Transmissionskoeffizient)
<span class="anker" id="satz-2-1"></span>

Der __Reflexionskoeffizient__ $R$ und der Transmissionskoeffizient $T$ sind

<span class="anker" id="gl-2-2"></span>
$$R=\frac{\text{reflektierter Teilchenstrom}}{\text{einlaufender Teilchenstrom}},\qquad T=\frac{\text{transmittierter Teilchenstrom}}{\text{einlaufender Teilchenstrom}}. \tag{2.2}$$
:::

:::satz Satz 2.2 ($R$ und $T$ der Stufe für $E>V_0$)
<span class="anker" id="satz-2-2"></span>

Mit den Geschwindigkeiten $|v_\mathrm I|=\hbar k_\mathrm I/m$ und $|v_\mathrm{II}|=\hbar k_\mathrm{II}/m$ gilt

<span class="anker" id="gl-2-3"></span>
$$R=\frac{|B|^2\,|v_\mathrm I|}{|A|^2\,|v_\mathrm I|}=\Bigl(\frac{k_\mathrm I-k_\mathrm{II}}{k_\mathrm I+k_\mathrm{II}}\Bigr)^2,\qquad T=\frac{|C|^2\,|v_\mathrm{II}|}{|A|^2\,|v_\mathrm I|}=\frac{4\,k_\mathrm{II}/k_\mathrm I}{\bigl(1+k_\mathrm{II}/k_\mathrm I\bigr)^2},\qquad R+T=1. \tag{2.3}$$
:::

⁠**So liest man das:** $R$ und $T$ sind Zahlen zwischen 0 und 1 ohne Einheit. Für ein einzelnes Elektron sind sie Wahrscheinlichkeiten, für viele Elektronen Anteile. $T$ ist hier keine Temperatur. $R+T=1$ sagt: Kein Elektron geht verloren. Beide hängen nur von $E/V_0$ ab, denn $k_\mathrm{II}/k_\mathrm I=\sqrt{1-V_0/E}$. **Gültigkeit:** wie in Stufe [1](zwei-gebiete-an-einer-kante-zusammensetzen.html#stufe-1), dazu $E>V_0$.

:::abbildung gemb1/k3oben 2
Links: Welle bei $E=3$ eV an der Kante mit $V_0=2$ eV (grau: Gebiet II), Realteil und Betrag für $A=1$. Im Gebiet I schwankt $|\psi|$ wegen der reflektierten Welle, im Gebiet II ist es konstant und die Wellenlänge größer. Rechts: Reflexions- und Transmissionskoeffizient über $E/V_0$. Punkte: Rechenmodell. Klassisch wäre $T=1$.
:::

:::herleitung Warum in $T$ die Geschwindigkeiten stehen
Nach [(2.1)](#gl-2-1) zählt der Strom, nicht die Dichte. Links haben einlaufende und reflektierte Welle dieselbe Geschwindigkeit, sie fällt in $R$ heraus: $R=|B/A|^2$. Rechts ist das Elektron langsamer, also $T=|C/A|^2\,k_\mathrm{II}/k_\mathrm I$. Mit [(1.4)](zwei-gebiete-an-einer-kante-zusammensetzen.html#gl-1-4) wird das $4k_\mathrm Ik_\mathrm{II}/(k_\mathrm I+k_\mathrm{II})^2$. Die Summe stimmt: $(k_\mathrm I-k_\mathrm{II})^2+4k_\mathrm Ik_\mathrm{II}=(k_\mathrm I+k_\mathrm{II})^2$.
:::

::::beispiel
Bei $E=3$ eV ist $R=0{,}268^2=0{,}072$. Von 1000 Elektronen kehren 72 um, obwohl alle genug Energie haben. $T$ ergibt sich zu $|C/A|^2\cdot k_\mathrm{II}/k_\mathrm I=1{,}608\cdot0{,}577=0{,}928$. Für $E/V_0=1{,}05$, 2 und 4 ist $R=0{,}412$, 0,029 und 0,005.
::::

⁠**Grenzfälle:** Für $E\gg V_0$ ist $k_\mathrm{II}\approx k_\mathrm I$, also $R\to0$ und $T\to1$, wie klassisch. Für $E\to V_0$ geht $k_\mathrm{II}\to0$, also $T\to0$. Knapp über der Kante kehrt fast jedes Elektron um. Das widerspricht der klassischen Erwartung am stärksten.

:::frage $C/A$ ist 1,27, also größer als 1. Kommt rechts mehr an, als links einläuft?
Nein. $|C|^2$ ist eine Dichte, kein Strom. Rechts sind die Elektronen langsamer, also drängen sie sich dichter. Der Strom ist nur das 0,928-fache des einlaufenden.
:::

:::frage Teilt sich das Elektron an der Stufe in zwei Stücke?
Nein. Es teilt sich die Welle. Weist man das Elektron nach, findet man es ganz, links oder rechts, mit den Wahrscheinlichkeiten $R$ und $T$.
:::

:::aufgabe Aufgabe 3 ★★ Reflexion ablesen
<span class="anker" id="aufg-3"></span>

Ein Elektron mit $E=1{,}5$ eV trifft auf eine Stufe mit $V_0=0{,}6$ eV.

<ol class="al">

<li>

Berechne $R$ und $T$ und prüfe $R+T=1$.

</li>

<li>

Bei welcher Energie sinkt $R$ auf 1 %?

</li>

<li>

Wie ändert sich $R$, wenn statt des Elektrons ein schwereres Teilchen mit derselben Energie kommt?

</li>

</ol>

:::loesung
(a) $k_\mathrm I=6{,}27\,\mathrm{nm^{-1}}$, $k_\mathrm{II}=4{,}86\,\mathrm{nm^{-1}}$. $R=(1{,}41/11{,}14)^2=0{,}016$, $T=4\cdot6{,}27\cdot4{,}86/11{,}14^2=0{,}984$. Summe 1. (b) $R=0{,}01$ verlangt $(k_\mathrm I-k_\mathrm{II})/(k_\mathrm I+k_\mathrm{II})=0{,}1$, also $k_\mathrm{II}/k_\mathrm I=9/11$. Mit $(k_\mathrm{II}/k_\mathrm I)^2=1-V_0/E$ folgt $E=3{,}03\,V_0=1{,}82$ eV. (c) Gar nicht: Die Masse kürzt sich in $k_\mathrm{II}/k_\mathrm I=\sqrt{1-V_0/E}$.
:::
:::

:::aufgabe Aufgabe 4 ★★ Die Stufe abwärts
<span class="anker" id="aufg-4"></span>

Ein Elektron läuft auf einem Sockel mit $V=0{,}6$ eV nach rechts und erreicht eine Kante, hinter der $V=0$ ist. Seine Gesamtenergie ist $E=1$ eV.

<ol class="al">

<li>

Vorhersage: Was erwartet man klassisch, was nach der Welle?

</li>

<li>

Berechne $R$ und $T$. Vergleiche mit der Gegenrichtung (Stufe aufwärts, dieselben Energien). Welches Vorzeichen hat $B/A$ jeweils?

</li>

</ol>

:::loesung
(a) Klassisch läuft jedes Elektron weiter und wird schneller. Nach der Welle springt $k$, also gibt es auch hier Reflexion. (b) Links ist die kinetische Energie 0,4 eV, rechts 1 eV: $k=3{,}24\,\mathrm{nm^{-1}}$ und $5{,}12\,\mathrm{nm^{-1}}$. Dann ist $B/A=(3{,}24-5{,}12)/(3{,}24+5{,}12)=-0{,}225$, $R=0{,}051$, $T=0{,}949$. Die Gegenrichtung ergibt dieselben $R$ und $T$, denn beide Formeln bleiben beim Tausch von $k_\mathrm I$ und $k_\mathrm{II}$ gleich. Nur $B/A$ dreht das Vorzeichen: aufwärts $+0{,}225$, abwärts $-0{,}225$, also Phasensprung $\pi$.
:::
:::

Offen bleibt, was geschieht, wenn die Energie nicht für die Kante reicht.
