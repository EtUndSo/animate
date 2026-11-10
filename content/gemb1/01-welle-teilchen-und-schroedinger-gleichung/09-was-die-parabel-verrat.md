---
title: Stufe 7: Was die Parabel verrät
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung
knoten: Kapitel 1: Welle, Teilchen und Schrödinger-Gleichung
order: 4110900
summary: Diese Stufe liest aus der Form von E(k) Geschwindigkeit und Masse ab und zeigt, was ein elektrisches Feld mit dem Elektron macht.
tags: Energiediagramm
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Diese Stufe liest aus der Form von $E(k)$ Geschwindigkeit und Masse ab und zeigt, was ein elektrisches Feld mit dem Elektron macht.
:::

**Die Idee.** Die Steigung der Kurve gibt die Geschwindigkeit an, das sagt schon [(6.3)](das-wellenpaket.html#gl-6-3). Eine Kraft ändert den Impuls und damit $k$: Das Elektron rutscht auf der Kurve. Ist sie stark gekrümmt, wächst die Steigung dabei schnell, und dieselbe Kraft ändert die Geschwindigkeit stark. Das Elektron ist leicht. Eine flache Kurve bedeutet ein schweres Elektron (Abb. [7](#abb-7)).

:::satz Satz 7.1 (Geschwindigkeit und Masse)
<span class="anker" id="satz-7-1"></span>

Für ein Teilchen mit der Dispersionsrelation $E(k)$ gilt

<span class="anker" id="gl-7-1"></span>
$$v=\frac1\hbar\frac{\partial E(k)}{\partial k},\qquad m=\Bigl(\frac1{\hbar^2}\frac{\partial^2E(k)}{\partial k^2}\Bigr)^{-1}. \tag{7.1}$$
:::

⁠**So liest man das:** $v$ in m/s, $m$ in kg oder eV s$^2$/m$^2$. Die Masse ist der Kehrwert der Krümmung: große Krümmung, kleine Masse. **Kontrolle:** Für die Parabel ist $\partial^2E/\partial k^2=\hbar^2/m$, und [(7.1)](#gl-7-1) gibt $m$ zurück.

:::herleitung Masse aus der Krümmung
Newton lautet $F=m\,\mathrm{d} v/\mathrm{d} t$ und ebenso $F=\mathrm{d} p/\mathrm{d} t$. Mit $p=\hbar k$ ist

$$F=\hbar\frac{\mathrm{d} k}{\mathrm{d} t}=\hbar\frac{\mathrm{d} k}{\mathrm{d} v}\frac{\mathrm{d} v}{\mathrm{d} t}\quad\Rightarrow\quad m=\hbar\frac{\mathrm{d} k}{\mathrm{d} v}=\Bigl(\frac1\hbar\frac{\mathrm{d} v}{\mathrm{d} k}\Bigr)^{-1}=\Bigl(\frac1\hbar\frac{\mathrm{d}}{\mathrm{d} k}\frac1\hbar\frac{\partial E}{\partial k}\Bigr)^{-1}=\Bigl(\frac1{\hbar^2}\frac{\partial^2E}{\partial k^2}\Bigr)^{-1}.$$
:::

:::abbildung gemb1/k1kruemmung 7
Links: Zwei Parabeln mit $V_0=0$, die rote gehört zu einem fünfmal leichteren Teilchen. Die gestrichelte Tangente zeigt die Steigung am blauen Punkt. Rechts: Die Geschwindigkeit ist die Steigung der linken Kurve, geteilt durch $\hbar$, und wächst linear mit $k$.
:::

**Elektron im Feld.** Zwei Platten im Abstand $d$ liegen an der Spannung $U$, rechts der Pluspol. Das elektrostatische Potential $\varphi(x)=U\,x/d$ gibt dem Elektron die potentielle Energie $V(x)=V(0)-e\,U\,x/d$, sie fällt nach rechts ab. Ändert sich $V$ über eine Wellenlänge nur wenig, gilt an jedem Ort die Parabel mit dem Scheitel $V(x)$ (Abb. [8](#abb-8)). Ohne Stöße bleibt die Gesamtenergie $E$ erhalten: Im Bild läuft das Elektron auf einer waagerechten Linie. Der Scheitel sinkt unter ihm weg, und die potentielle Energie wird zu kinetischer:

<span class="anker" id="gl-7-2"></span>
$$E_\mathrm{kin}(x)=E-V(x),\qquad k(x)=\frac{\sqrt{2m\bigl(E-V(x)\bigr)}}\hbar,\qquad\frac{\mathrm{d} k}{\mathrm{d} t}=\frac F\hbar. \tag{7.2}$$

⁠**So liest man das:** Ein solches Bild, Energie über dem Ort, heißt __Energiediagramm__. Die Feldstärke $\mathcal E=-\mathrm{d}\varphi/\mathrm{d} x=-U/d$ zeigt nach links, die Kraft $F=-e\,\mathcal E=e\,U/d$ auf das Elektron nach rechts. **Gültigkeit:** $V$ ändert sich über eine Wellenlänge wenig gegen $E_\mathrm{kin}$. Direkt am Start, wo $\lambda$ groß ist, gilt das nur grob.

:::abbildung gemb1/k1feld 8
Energiediagramm zwischen zwei Platten. Blau: Scheitel $V(x)$. Grün: die an drei Orten gültige Parabel mit eigener $k$-Achse. Rot: Gesamtenergie $E$, sie bleibt fest. Das Elektron startet links mit $k=0$. Der rote Punkt liegt an jedem Ort dort auf der Parabel, wo sie $E$ erreicht, $k$ wächst nach rechts. Orange: kinetische Energie.
:::

::::beispiel
Bei $U=1$ V und $d=100$ nm ist $|\mathcal E|=10^{7}$ V/m und $F=1{,}60\cdot10^{-12}$ N. Damit wächst $k$ je Sekunde um $F/\hbar=1{,}52\cdot10^{22}\,\mathrm{m^{-1}}$. Das Elektron braucht ohne Stöße $t=2d/v=3{,}4\cdot10^{-13}$ s und kommt als Probe-Elektron mit 1 eV und $v=5{,}93\cdot10^{5}$ m/s an. Über die letzte Wellenlänge von 1,23 nm ändert sich $V$ nur um 12 meV.
::::

⁠**Grenzfall:** Bei $U=0$ ist $V$ konstant, $F=0$, und $k$ bleibt fest.

:::frage Die Masse des Elektrons steht doch in jeder Tabelle. Wozu dann [(7.1)](#gl-7-1)?
Für das freie Elektron gibt die Formel nur $m_0$ zurück, das stimmt. Ihre Herleitung braucht aber nur $p=\hbar k$ und $F=\mathrm{d} p/\mathrm{d} t$, nicht die Parabel. Sie gilt für jede Kurve $E(k)$ und liefert die Masse, mit der das Teilchen auf eine Kraft reagiert, gleich woher die Kurve kommt.
:::

:::aufgabe Aufgabe 8 ★ Masse aus der Kurve
<span class="anker" id="aufg-8"></span>

Nahe $k=0$ messe man $E(k)=V_0+\alpha\,k^2$ mit $\alpha=0{,}19\,\mathrm{eV\,nm^2}$.

<ol class="al">

<li>

Berechne $m$ in kg, in eV s$^2$/m$^2$ und in Vielfachen von $m_0$.

</li>

<li>

Wie groß ist $v$ bei $E-V_0=1$ eV? Vergleiche mit dem Probe-Elektron.

</li>

<li>

Vorhersage: Dieses Teilchen und ein freies Elektron spüren dieselbe Kraft gleich lange. Bei welchem wächst $k$ stärker, bei welchem $v$?

</li>

</ol>

:::loesung
(a) $\partial^2E/\partial k^2=2\alpha$, also $m=\hbar^2/(2\alpha)=1{,}83\cdot10^{-31}$ kg $=1{,}14\cdot10^{-12}$ eV s$^2$/m$^2$ $=0{,}20\,m_0$. (b) $k=\sqrt{1\,\mathrm{eV}/\alpha}=2{,}29\cdot10^{9}\,\mathrm{m^{-1}}$, $v=\hbar k/m=1{,}32\cdot10^{6}$ m/s, das 2,2-fache des Probe-Elektrons. (c) $k$ wächst bei beiden gleich, denn $\mathrm{d} k/\mathrm{d} t=F/\hbar$ enthält keine Masse. $v$ wächst beim leichten Teilchen fünfmal stärker.
:::
:::

:::aufgabe Aufgabe 9 ★★ Zwischen zwei Platten
<span class="anker" id="aufg-9"></span>

Ein Elektron startet in Ruhe an der Platte auf 0 V. Die andere Platte liegt bei $U=0{,}5$ V im Abstand $d=200$ nm. Es gibt keine Stöße.

<ol class="al">

<li>

Berechne $|\mathcal E|$, $F$, die Werte von $k$ und $v$ an der Gegenplatte und die Flugzeit.

</li>

<li>

Wie groß sind $k$ und $\lambda$ auf halbem Weg?

</li>

<li>

Dasselbe Feld wirke in Kupfer, wo nach $\tau=2{,}5\cdot10^{-14}$ s ein Stoß kommt. Wie weit rutscht ein ruhendes Elektron bis dahin in $k$, und welche Energie gewinnt es? Vergleiche mit $k_\mathrm BT$. Was sagt das über die Drift aus Stufe [1](elektronen-als-gas.html#stufe-1)?

</li>

</ol>

:::loesung
(a) $|\mathcal E|=2{,}5\cdot10^{6}$ V/m, $F=4{,}0\cdot10^{-13}$ N. An der Gegenplatte ist $E_\mathrm{kin}=0{,}5$ eV, also $k=3{,}62\cdot10^{9}\,\mathrm{m^{-1}}$ und $v=4{,}19\cdot10^{5}$ m/s. Die Flugzeit ist $\hbar k/F=2d/v=9{,}5\cdot10^{-13}$ s. (b) $E_\mathrm{kin}=0{,}25$ eV, $k=2{,}56\cdot10^{9}\,\mathrm{m^{-1}}$, $\lambda=2{,}45$ nm. (c) $\Delta k=F\tau/\hbar=9{,}4\cdot10^{7}\,\mathrm{m^{-1}}$, kaum 2 % der Wellenzahl des Probe-Elektrons. Die gewonnene Energie ist $\hbar^2\Delta k^2/(2m_0)=0{,}33$ meV, viel weniger als $k_\mathrm BT=26$ meV. Selbst hier rutscht ein Elektron zwischen zwei Stößen nur ein kleines Stück auf der Parabel: die winzige Schlagseite aus Stufe [1](elektronen-als-gas.html#stufe-1).
:::
:::

:::aufgabe Aufgabe 10 ★★★ Strom aus der Wellenfunktion
<span class="anker" id="aufg-10"></span>

Die Wahrscheinlichkeit, die je Sekunde durch einen Punkt läuft, ist in einer Dimension

$$S=\frac\hbar{2m\mathrm{j}}\Bigl(\psi^*\frac{\partial\psi}{\partial x}-\psi\frac{\partial\psi^*}{\partial x}\Bigr).$$

<ol class="al">

<li>

Zeige für $\psi=C\,\mathrm{e}^{\mathrm{j} kx}$, dass $S=v\,|C|^2$ gilt. Vergleiche mit $j=e\,n\,|v_\mathrm d|$.

</li>

<li>

Zeige für [(5.1)](freies-elektron-ebene-welle-dispersion.html#gl-5-1), dass $S=(\hbar k/m)\bigl(|C_+|^2-|C_-|^2\bigr)$ gilt. Was folgt für eine stehende Welle?

</li>

<li>

Das Probe-Elektron laufe auf einem Ring der Länge $L=1$ µ m, also $C=1/\sqrt L$. Welchen Strom $I=e\,S$ trägt es?

</li>

</ol>

:::loesung
(a) Mit $\partial\psi/\partial x=\mathrm{j} k\psi$ und $\partial\psi^*/\partial x=-\mathrm{j} k\psi^*$ ist die Klammer $2\mathrm{j} k|C|^2$, also $S=(\hbar k/m)\,|C|^2=v\,|C|^2$. Das hat dieselbe Form wie $j=e\,n\,|v_\mathrm d|$: Dichte mal Geschwindigkeit. (b) In $\psi^*\partial\psi/\partial x$ stehen $\mathrm{j} k\bigl(|C_+|^2-|C_-|^2\bigr)$ und Mischterme $\mathrm{j} k\,(z-z^*)$ mit $z=C_-^*C_+\mathrm{e}^{2\mathrm{j} kx}$. Die Klammer in $S$ ist $2\mathrm{j}$ mal der Imaginärteil davon, die Mischterme sind reell und fallen weg. Es bleibt $S=(\hbar k/m)\bigl(|C_+|^2-|C_-|^2\bigr)$. Bei einer stehenden Welle ist $|C_+|=|C_-|$ und $S=0$: Sie transportiert nichts. (c) $S=v/L=5{,}93\cdot10^{11}\,\mathrm{s^{-1}}$, das Elektron läuft so oft je Sekunde um. Der Strom ist $I=e\,S=95$ nA.
:::
:::
