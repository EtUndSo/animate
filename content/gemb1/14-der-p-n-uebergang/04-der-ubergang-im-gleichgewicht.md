---
title: Stufe 2: Der Übergang im Gleichgewicht
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der p-n-Übergang
order: 4240400
summary: Ein p- und ein n-Gebiet haben verschiedene Fermi-Energien.
tags: Neutralgebiete, eingebautes Potential
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein p- und ein n-Gebiet haben verschiedene Fermi-Energien. Diese Stufe zeigt, was an ihrer Grenze von selbst geschieht und welche Spannung dabei entsteht.
:::

**Die Idee.** In einem Gedankenexperiment berühren sich ein p-Stück links und ein n-Stück rechts. Vier Schritte laufen ab (Abb. [2](#abb-2)):

<ol>

<li>

⁠**Diffusion.** Rechts sind $10^{16}$ Elektronen je cm$^3$, links $10^{3}$. Die ungeordnete Bewegung trägt mehr Elektronen nach links als zurück, und ebenso Löcher nach rechts.

</li>

<li>

⁠**Rekombination.** Im fremden Gebiet sind die Ankömmlinge Minoritätsträger. Sie treffen auf die Majoritätsträger und verschwinden paarweise.

</li>

<li>

⁠**Ionen bleiben.** Nahe der Grenze fehlen nun bewegliche Träger. Die Donatoren rechts und die Akzeptoren links sitzen fest im Gitter und sind nicht mehr ausgeglichen.

</li>

<li>

⁠**Das Feld stoppt den Ausgleich.** Die Ionen erzeugen ein Feld von rechts nach links. Es treibt Elektronen zurück nach rechts und Löcher zurück nach links. Die Schicht wächst, bis für jede Sorte die Drift die Diffusion genau aufhebt.

</li>

</ol>

:::abbildung gemb1/k14kontakt 2
Links: zwei getrennte Stücke mit gleichen Bandkanten und verschiedenen Fermi-Energien, Abstand $\Phi_\mathrm{bi}=0{,}762$ eV. Rechts: im Gleichgewicht ist $E_\mathrm F$ überall gleich, die Bänder des p-Gebiets liegen um $\Phi_\mathrm{bi}$ höher. Oben in der Zone stehen die Vorzeichen der festen Ionen. Zahlen des Rechenmodells.
:::

Das ist der Pegelausgleich aus [Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html): Vor dem Kontakt liegt $E_\mathrm F$ im n-Stück höher. Am Ende ist es überall gleich, und dafür verschiebt die zurückbleibende Ladung die Bänder selbst. Das Gleichgewicht ist dynamisch: Diffusion und Drift laufen in der Zone weiter und heben sich auf.

:::herleitung Warum $E_\mathrm F$ im Gleichgewicht überall gleich ist
[Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html) zerlegt $E_\mathrm F(x)=E_\mathrm C(x)+\zeta(x)$ mit $\zeta=-k_\mathrm BT\ln(N_\mathrm C/n)$, also $\mathrm{d} E_\mathrm F/\mathrm{d} x=e\mathcal E+(k_\mathrm BT/n)\,\mathrm{d} n/\mathrm{d} x$. Mit $\mu_\mathrm n\,n$ multipliziert steht rechts genau $j_\mathrm n$ aus [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2):

<span class="anker" id="gl-2-1"></span>
$$j_\mathrm n=\mu_\mathrm n\,n\,\frac{\mathrm{d} E_\mathrm F}{\mathrm{d} x},\qquad\text{ebenso}\quad j_\mathrm p=\mu_\mathrm p\,p\,\frac{\mathrm{d} E_\mathrm F}{\mathrm{d} x}. \tag{2.1}$$

Kein Strom heißt also $\mathrm{d} E_\mathrm F/\mathrm{d} x=0$. Mit $E_\mathrm C=\text{konst}-e\varphi$ lautet das $\mathrm{d}\zeta/\mathrm{d} x-e\,\mathrm{d}\varphi/\mathrm{d} x=0$: Das Dichtegefälle, das die Diffusion treibt, und das Potentialgefälle, das die Drift treibt, heben sich an jedem Ort auf.
:::

:::definition Definition 2.1 (Raumladungszone und Diffusionsspannung)
<span class="anker" id="satz-2-1"></span>

Die Schicht, in der die Ionen nicht ausgeglichen sind, heißt Raumladungszone (RLZ) oder Verarmungszone. Sie reicht von $x_\mathrm p$ im p-Gebiet bis $x_\mathrm n$ im n-Gebiet. Außerhalb liegen die __Neutralgebiete__, ohne Raumladung und ohne Feld. Die Potentialdifferenz über die Zone ist die Diffusionsspannung $U_\mathrm d=\varphi(x_\mathrm n)-\varphi(x_\mathrm p)$, die Energie $\Phi_\mathrm{bi}=eU_\mathrm d$ heißt __eingebautes Potential__ (englisch built-in).
:::

:::satz Satz 2.2 (Diffusionsspannung)
<span class="anker" id="satz-2-2"></span>

In der Störstellenerschöpfung gilt mit den Fermi-Energien $E_\mathrm{Fn}$ und $E_\mathrm{Fp}$ der getrennten Stücke

<span class="anker" id="gl-2-2"></span>
$$\Phi_\mathrm{bi}=eU_\mathrm d=E_\mathrm{Fn}-E_\mathrm{Fp}=k_\mathrm BT\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2}, \tag{2.2}$$

<span class="anker" id="gl-2-3"></span>
$$U_\mathrm d=\frac{E_\mathrm g}{e}-\frac{k_\mathrm BT}{e}\ln\frac{N_\mathrm CN_\mathrm V}{N_\mathrm AN_\mathrm D}=\frac{k_\mathrm BT}{e}\ln\frac{n_\mathrm{n0}}{n_\mathrm{p0}}=\frac{k_\mathrm BT}{e}\ln\frac{p_\mathrm{p0}}{p_\mathrm{n0}}. \tag{2.3}$$
:::

⁠**So liest man das:** $\Phi_\mathrm{bi}$ steht in eV, $U_\mathrm d$ in V, beide haben denselben Zahlenwert, in Silizium um 0,7 bis 1 V. Die Bänder fallen über die Zone nach rechts um $\Phi_\mathrm{bi}$. Für ein Elektron ist das eine Barriere auf dem Weg ins p-Gebiet. Die Formen mit den Dichten gelten auch ohne Störstellenerschöpfung.

:::herleitung Die Stufe aus dem Bänderdiagramm
Die Bandkanten folgen dem Potential, also ist $eU_\mathrm d=E_\mathrm C^\mathrm p-E_\mathrm C^\mathrm n=E_\mathrm V^\mathrm p-E_\mathrm V^\mathrm n$, die Hochzahl nennt das Neutralgebiet. In Abb. [2](#abb-2) rechts liest man ab:

<span class="anker" id="gl-2-4"></span>
$$eU_\mathrm d=E_\mathrm g-\bigl(E_\mathrm C-E_\mathrm F\bigr)_\mathrm n-\bigl(E_\mathrm F-E_\mathrm V\bigr)_\mathrm p. \tag{2.4}$$

Aus [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) folgt mit $n=N_\mathrm D$ und $p=N_\mathrm A$: $(E_\mathrm C-E_\mathrm F)_\mathrm n=k_\mathrm BT\ln(N_\mathrm C/N_\mathrm D)$ und $(E_\mathrm F-E_\mathrm V)_\mathrm p=k_\mathrm BT\ln(N_\mathrm V/N_\mathrm A)$. Einsetzen ergibt die erste Form in [(2.3)](#gl-2-3). Mit $n_\mathrm i=\sqrt{N_\mathrm CN_\mathrm V}\,\mathrm{e}^{-E_\mathrm g/(2k_\mathrm BT)}$ wird daraus [(2.2)](#gl-2-2), und wegen $n_\mathrm{n0}p_\mathrm{n0}=n_\mathrm{p0}p_\mathrm{p0}=n_\mathrm i^2$ entstehen die Formen mit den Dichten.
:::

::::beispiel
Im Rechenmodell ist $E_\mathrm C-E_\mathrm F=205{,}4$ meV im n-Gebiet und $E_\mathrm F-E_\mathrm V=152{,}6$ meV im p-Gebiet. Das sind $7{,}9$ und $5{,}9\,k_\mathrm BT$, die Boltzmann-Näherung gilt. Daraus folgt $\Phi_\mathrm{bi}=1{,}12\,\mathrm{eV}-0{,}2054\,\mathrm{eV}-0{,}1526\,\mathrm{eV}=0{,}762$ eV, und $k_\mathrm BT\cdot\ln(6{,}3\cdot10^{12})=25{,}85\,\mathrm{meV}\cdot29{,}48$ ergibt denselben Wert. Der Boltzmann-Faktor der Barriere ist $\mathrm{e}^{-29{,}48}=1{,}6\cdot10^{-13}$, genau das Verhältnis $n_\mathrm{p0}/n_\mathrm{n0}$.
::::

⁠**Grenzfälle:** Für $N_\mathrm A\to N_\mathrm V$ und $N_\mathrm D\to N_\mathrm C$ geht $U_\mathrm d\to E_\mathrm g/e$. Für $N_\mathrm A=N_\mathrm D=n_\mathrm i$ ist $U_\mathrm d=0$. Zehnmal mehr Dotierung auf einer Seite bringt nur $k_\mathrm BT\ln10=59{,}5$ mV. Mit der Temperatur sinkt $U_\mathrm d$, weil $n_\mathrm i$ steil wächst: Bei 350 K sind es 0,688 V.

:::frage In der Diode stecken 0,76 V. Warum zeigt ein Spannungsmesser 0 V?
Die Potentialstufe ist echt, aber ein Spannungsmesser misst keinen Potentialverlauf im Inneren. Er zeigt die Differenz der Fermi-Energien an seinen Anschlüssen, geteilt durch $e$. Im Gleichgewicht ist $E_\mathrm F$ überall gleich, also zeigt er null. Es fließt auch kein Strom, und die Diode gibt keine Leistung ab.
:::

:::aufgabe Aufgabe 2 ★★ Zwei Wege zu $\Phi_\mathrm{bi}$
<span class="anker" id="aufg-2"></span>

Ein Silizium-Übergang hat $N_\mathrm A=2\cdot10^{17}\,\mathrm{cm^{-3}}$ und $N_\mathrm D=3\cdot10^{15}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Berechne die Abstände von $E_\mathrm F$ zu den Bandkanten in beiden Neutralgebieten und daraus $\Phi_\mathrm{bi}$.

</li>

<li>

Berechne $\Phi_\mathrm{bi}$ aus [(2.2)](#gl-2-2) und $U_\mathrm d$ aus den Dichten $n_\mathrm{n0}$ und $n_\mathrm{p0}$.

</li>

<li>

Zeichne das Bänderdiagramm mit $E_\mathrm C$, $E_\mathrm V$, $E_\mathrm F$, $E_\mathrm D$, $E_\mathrm A$, $E_\mathrm g$, $\Phi_\mathrm{bi}$ und den Rändern der Zone. Welche Abstände bleiben überall gleich?

</li>

</ol>

:::loesung
(a) $E_\mathrm F-E_\mathrm V=116{,}8$ meV, $E_\mathrm C-E_\mathrm F=236{,}5$ meV, also $\Phi_\mathrm{bi}=1{,}12\,\mathrm{eV}-0{,}1168\,\mathrm{eV}-0{,}2365\,\mathrm{eV}=0{,}7667$ eV. (b) $k_\mathrm BT\ln\bigl(6\cdot10^{32}/7{,}9\cdot10^{19}\bigr)=0{,}7667$ eV. Mit $n_\mathrm{n0}=3\cdot10^{15}\,\mathrm{cm^{-3}}$ und $n_\mathrm{p0}=395\,\mathrm{cm^{-3}}$ ist $U_\mathrm d=25{,}85\,\mathrm{mV}\cdot29{,}66=0{,}767$ V. (c) $E_\mathrm F$ ist eine Waagerechte, $E_\mathrm C$, $E_\mathrm D$, $E_\mathrm A$ und $E_\mathrm V$ fallen nach rechts gemeinsam um $\Phi_\mathrm{bi}$. Überall gleich bleiben $E_\mathrm g$, $E_\mathrm C-E_\mathrm D$ und $E_\mathrm A-E_\mathrm V$.
:::
:::
