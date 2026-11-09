---
title: Stufe 7: Ergänzung: Quantenfilm, Draht und Punkt
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Das Teilchen in der Box
order: 4120900
summary: Kristalline Schichten lassen sich heute mit atomarer Genauigkeit aufbauen und seitlich auf wenige Nanometer strukturieren.
tags: Teilband, Quantenfilm, Quantendraht, Quantenpunkt, zweidimensionales Elektronengas, Epitaxie, Heteroepitaxie, Tunneln
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Kristalline Schichten lassen sich heute mit atomarer Genauigkeit aufbauen und seitlich auf wenige Nanometer strukturieren. Diese Stufe ordnet die Bauformen danach, wie viele Richtungen eingesperrt sind.
:::

**Die Idee.** In einer eingeschränkten Richtung gibt es nur diskrete Niveaus, in einer freien Richtung die Parabel. Jede Struktur ist eine Mischung aus beidem (Abb. [7](#abb-7)). Jedes diskrete Niveau trägt seine eigene Parabel. Sie heißt __Teilband__ (englisch subband).

| Struktur | eingesperrt | frei | Energie |
|---|---|---|---|
| __Quantenfilm__ | $z$ | $x,y$ | $E=E_{n_z}+\hbar^2(k_x^2+k_y^2)/(2m)$ |
| __Quantendraht__ | $y,z$ | $x$ | $E=E_{n_y,n_z}+\hbar^2k_x^2/(2m)$ |
| __Quantenpunkt__ | $x,y,z$ | keine | $E=E_{n_x,n_y,n_z}$ |

:::abbildung gemb1/k2film 7
Schematisch mit quadratischem Querschnitt und Würfel, $E_0=\hbar^2\pi^2/(2mL^2)$. Der Film hat Teilbänder ab 1, 4 und 9 $E_0$, der Draht ab 2, 5 und 8 $E_0$, der Punkt nur noch einzelne Niveaus. Die Zahlen an den Kurven nennen die Entartung.
:::

⁠**So liest man das:** Der Film ist die Box aus Stufe [3](das-elektron-zwischen-zwei-wanden.html#stufe-3) in $z$ mit zwei freien Richtungen, die Elektronen darin bilden ein __zweidimensionales Elektronengas__. Ein Beispiel ist eine nur Nanometer dünne Siliziumschicht auf einem Isolator. Quantenfilme sind in der Optoelektronik wichtig, etwa in hocheffizienten Leuchtdioden und Halbleiterlasern. Der Draht hat zwei eingesperrte Richtungen und leitet nur noch längs. Im Punkt ist $k$ in keiner Richtung frei, die Energien sind diskret wie im Atom.

::::beispiel ein Quantenpunkt im Nanodraht
An Gold-Nanopartikeln wachsen aus der Gasphase einkristalline Nadeln aus InAs, sogenannte Whisker, hier mit 40 nm mal 40 nm Querschnitt. Ändert man beim Wachsen die Gasmischung, entstehen dünne Zonen aus InP. Das Kristallgitter läuft dabei ungestört weiter (__Epitaxie__). Weil sich die Zusammensetzung selbst ändert und nicht nur eine Beimischung, spricht man von __Heteroepitaxie__. InP hat einen größeren Bandabstand als InAs: Die tiefste Energie eines beweglichen Elektrons liegt dort höher. Für Elektronen im InAs wirken die InP-Zonen deshalb als Wände. Zwischen zwei Zonen im Abstand $L_z=20$ nm liegt ein Quantenpunkt.

Die Wände sind endlich hoch, die Box mit unendlich hohen Wänden ist also eine erste Näherung. In InAs gilt $m^*=0{,}023\,m_0$, denn das Kristallgitter lässt das Elektron dort viel leichter erscheinen. Die Niveaus rechnet man getrennt und addiert sie. In $z$ ist $E^z_1=0{,}376\,\mathrm{eV\,nm^2}/(0{,}023\cdot400\,\mathrm{nm^2})=40{,}9$ meV und $E^z_2=164$ meV. Im Querschnitt ist $E^\perp_{1,1}=20{,}4$ meV, $E^\perp_{1,2}=E^\perp_{2,1}=51{,}1$ meV (zweifach entartet) und $E^\perp_{2,2}=81{,}8$ meV. Das tiefste Niveau liegt also bei 61,3 meV, das nächste bei 92,0 meV. **Kontrolle:** Mit $m_0$ statt $m^*$ wäre es 1,4 meV. Die kleine effektive Masse macht die Quantisierung erst groß.
::::

:::frage Warum ist nicht jede dünne Schicht ein Quantenfilm?
Die Niveaus zählen nur, wenn ihr Abstand groß gegen die Wärmeenergie $k_\mathrm BT\approx26$ meV bei 300 K ist. Sonst verteilt die Wärme die Elektronen über viele Niveaus, und die Stufen verschwimmen.
:::

:::zusatz Resonante Tunneldioden
Ist eine Wand endlich hoch und dünn, wird $\psi$ in ihr nicht sofort null, sondern reicht bis zur anderen Seite. Ein Elektron kann deshalb hindurch, das heißt __Tunneln__. In einem Nanodraht mit dünnen InP-Zonen läuft es vom Emitter (InAs links) über den Punkt zum Kollektor (InAs rechts). Das gelingt vor allem dann, wenn seine Energie zu einem Niveau des Punkts passt. Die Strom-Spannungs-Kennlinie zeigt daher direkt die Lage der Niveaus. Solche resonanten Tunneldioden kommen für sehr schnelle Logikschaltungen infrage.
:::

:::aufgabe Aufgabe 10 ★★ Wann zählt die Quantisierung?
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Ein Film soll $E_2-E_1>k_\mathrm BT=25{,}9$ meV erfüllen. Wie dünn muss er für $m=m_0$ sein, wie dünn für InAs mit $m^*=0{,}023\,m_0$?

</li>

<li>

Berechne die zwei tiefsten Niveaus eines InAs-Würfels mit $L=10$ nm.

</li>

<li>

Vorhersage: Ein Nanokristall sendet Licht aus, wenn ein Elektron zwischen zwei Niveaus fällt, die Photonenenergie ist die Differenz. Was geschieht mit der Farbe, wenn der Durchmesser sich halbiert?

</li>

</ol>

:::loesung
(a) $3E_1>k_\mathrm BT$ verlangt $L<\sqrt{3\cdot0{,}376\,\mathrm{eV\,nm^2}/(0{,}0259\,\mathrm{eV})}=6{,}6$ nm für $m_0$. Für InAs ist $L$ um $\sqrt{1/0{,}023}=6{,}6$ größer, also $L<44$ nm. (b) $E_0=0{,}376\,\mathrm{eV\,nm^2}/(0{,}023\cdot100\,\mathrm{nm^2})=163{,}5$ meV, also $E_{1,1,1}=491$ meV und $E_{2,1,1}=981$ meV. (c) Alle Niveauabstände werden viermal so groß. Das Licht wird energiereicher, die Wellenlänge kürzer: Kleinere Kristalle leuchten blauer.
:::
:::
