---
title: Stufe 7: Die Diodenkennlinie
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Der p-n-Übergang
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-p-n-ubergang
knoten: Kapitel 14: Der p-n-Übergang
order: 4240900
summary: Die Profile stehen.
tags: Shockley-Gleichung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Die Profile stehen. Diese Stufe liest aus ihrer Steigung den Strom ab, leitet die Kennlinie her und erklärt den kleinen Strom in Sperrrichtung.
:::

**Die Idee.** Am Zonenrand ist der Minoritätsstrom reine Diffusion, die Stromdichte ist also die Steigung des Profils, und die ist der Randwert geteilt durch die Abklinglänge. In der Zone geht nach Annahme 6 kein Träger verloren. Der Gesamtstrom ist deshalb überall die Summe beider Randwerte. Abb. [7](#abb-7) zeigt, wohin er im Neutralgebiet geht: Jedes rekombinierende Minoritätselektron wird durch ein nachströmendes Majoritätsloch ersetzt. So übergibt der eine Strom an den anderen.

:::abbildung gemb1/k14strom 7
Anteile der Elektronen und Löcher am Gesamtstrom über dem Ort, Rechenmodell, Durchlass. An der Zone tragen Löcher 77 %, Elektronen 23 %. Weit links tragen nur Löcher, weit rechts nur Elektronen, also jeweils die Majoritäten. Die Summe ist überall gleich.
:::

:::satz Satz 7.1 (Diodenkennlinie)
<span class="anker" id="satz-7-1"></span>

Für die Stromdichte vom p- zum n-Gebiet gilt

<span class="anker" id="gl-7-1"></span>
$$j=j_\mathrm n(-L_\mathrm{depl}^\mathrm A)+j_\mathrm p(L_\mathrm{depl}^\mathrm D)=j_\mathrm s\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr), \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$j_\mathrm s=e\frac{D_\mathrm pp_\mathrm{n0}}{L_\text{diff,p}}+e\frac{D_\mathrm nn_\mathrm{p0}}{L_\text{diff,n}}=e\sqrt{\frac{D_\mathrm p}{\tau_{\text{rec},\mathrm p}}}\frac{n_\mathrm i^2}{N_\mathrm D}+e\sqrt{\frac{D_\mathrm n}{\tau_{\text{rec},\mathrm n}}}\frac{n_\mathrm i^2}{N_\mathrm A}. \tag{7.2}$$

Mit der Fläche $A$ folgt die __Shockley-Gleichung__ $I=I_\mathrm S\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr)$ mit $I_\mathrm S=A\,j_\mathrm s$.
:::

⁠**So liest man das:** $j_\mathrm s$ in A/cm$^2$ ist die Dichte des Sperrsättigungsstroms, in Silizium um $10^{-12}\,\mathrm{A/cm^2}$. $k_\mathrm BT/e=25{,}85$ mV heißt Temperaturspannung. Je $k_\mathrm BT\ln10/e=59{,}5$ mV wächst der Strom auf das Zehnfache. **Gültigkeit:** die Annahmen aus Stufe [6](injektion-und-minoritatstrager.html#stufe-6).

:::herleitung Von den Profilen zur Kennlinie
<ol>

<li>

$n_\mathrm{p0}$ ist ortsfest, also $\mathrm{d} n_\mathrm p/\mathrm{d} x=\mathrm{d}\Delta n_\mathrm p/\mathrm{d} x$. Das Feld im Neutralgebiet ist klein (Stufe [5](spannung-anlegen.html#stufe-5)) und $n_\mathrm p\ll p$, die Drift der Minoritäten zählt nicht. Aus [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2) bleibt $j_\mathrm n\approx j_\mathrm{n,diff}=eD_\mathrm n\,\mathrm{d}\Delta n_\mathrm p/\mathrm{d} x$ bei $x=-L_\mathrm{depl}^\mathrm A$.

</li>

<li>

Mit [(6.2)](injektion-und-minoritatstrager.html#gl-6-2) ist die Steigung dort $\Delta n_\mathrm p(-L_\mathrm{depl}^\mathrm A)/L_\text{diff,n}$, also

<span class="anker" id="gl-7-3"></span>
$$j_\mathrm n=\frac{e\,D_\mathrm n\,\Delta n_\mathrm p(-L_\mathrm{depl}^\mathrm A)}{L_\text{diff,n}}=\frac{e\,D_\mathrm n\,n_\mathrm{p0}}{L_\text{diff,n}}\bigl(\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}-1\bigr). \tag{7.3}$$

</li>

<li>

Auf der n-Seite ist $j_\mathrm p\approx-eD_\mathrm p\,\mathrm{d}\Delta p_\mathrm n/\mathrm{d} x$ bei $x=L_\mathrm{depl}^\mathrm D$. Die Steigung ist $-\Delta p_\mathrm n/L_\text{diff,p}$, beide Minuszeichen heben sich auf: Auch dieser Beitrag fließt nach rechts.

</li>

<li>

In der Zone ist nach Annahme 6 $\mathrm{d} j_\mathrm n/\mathrm{d} x=\mathrm{d} j_\mathrm p/\mathrm{d} x=0$. Der Gesamtstrom ist stetig, die Summe der beiden Randwerte ergibt [(7.1)](#gl-7-1).

</li>

<li>

Mit $n_\mathrm{p0}=n_\mathrm i^2/N_\mathrm A$, $p_\mathrm{n0}=n_\mathrm i^2/N_\mathrm D$, $L_\text{diff,n}=\sqrt{D_\mathrm n\tau_{\text{rec},\mathrm n}}$ und $L_\text{diff,p}=\sqrt{D_\mathrm p\tau_{\text{rec},\mathrm p}}$ folgt die zweite Form in [(7.2)](#gl-7-2).

</li>

</ol>
:::

::::beispiel
Mit $n_\mathrm{p0}=1{,}58\cdot10^{3}\,\mathrm{cm^{-3}}$ und $p_\mathrm{n0}=7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$ ist $j_\mathrm s=(4{,}16+1{,}24)\cdot10^{-12}\,\mathrm{A/cm^2}=5{,}4\cdot10^{-12}\,\mathrm{A/cm^2}$ und $I_\mathrm S=5{,}4\cdot10^{-14}$ A (Abb. [8](#abb-8)). Die Löcher im schwächer dotierten n-Gebiet tragen 77 %, denn dort sind die Minoritäten fünfmal häufiger. 1 µ A fließt bei 0,433 V, 1 mA bei 0,611 V, 10 mA bei 0,671 V. **Probe:** Bei $I=10$ mA, also $j=1\,\mathrm{A/cm^2}$, reicht den Majoritäten im n-Gebiet mit $\sigma=1{,}9$ S/cm das Feld 0,52 V/cm, $8{,}5\cdot10^{4}$-mal kleiner als in der Zone. Auf 100 µ m fallen 5,2 mV ab. Für die viel selteneren Minoritäten ist dieses Feld belanglos.
::::

⁠**Grenzfälle:** Bei $U_\mathrm{pn}=0$ ist $j=0$. Ab $+119$ mV ist die $-1$ unter 1 %. Über 0,66 V endet die schwache Injektion.

:::abbildung gemb1/k14kennlinie 8
Kennlinie des Rechenmodells, $I_\mathrm S=5{,}4\cdot10^{-14}$ A. Links linear: Der Strom scheint erst bei rund 0,6 V zu beginnen. Rechts logarithmisch: Es gibt keine Schwelle, die Kennlinie ist über zehn Dekaden eine Gerade.
:::

**Sperrsättigungsstrom.** Für $U_\mathrm{pn}<-3k_\mathrm BT/e=-78$ mV ist $\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}$ unter 5 %, und es bleibt $j\approx-j_\mathrm s$. Die Zone nimmt jeden Minoritätsträger mit, der ihren Rand erreicht. Mehr Spannung saugt nicht stärker, denn die Randdichte ist schon null. Der Nachschub stammt aus Paaren, die Wärme im Neutralgebiet erzeugt, und nur aus einer Schicht von einer Diffusionslänge schaffen es die Träger bis zum Rand. Wegen $D_\mathrm p/L_\text{diff,p}=L_\text{diff,p}/\tau_{\text{rec},\mathrm p}$, und ebenso für Elektronen, ist $j_\mathrm s=e\,p_\mathrm{n0}L_\text{diff,p}/\tau_{\text{rec},\mathrm p}+e\,n_\mathrm{p0}L_\text{diff,n}/\tau_{\text{rec},\mathrm n}$: genau die Erzeugung in diesen Schichten. Deshalb ist $j_\mathrm s$ von der Spannung unabhängig und klein. Wegen $j_\mathrm s\propto n_\mathrm i^2$ mit dem Faktor $\mathrm{e}^{-E_\mathrm g/(k_\mathrm BT)}$ ist er stark temperaturabhängig: $n_\mathrm i^2$ wächst in Silizium von 300 K auf 310 K auf das 4,5-fache.

:::ltspice Die Kennlinie des Rechenmodells
⁠**Zeichnen:** `voltage` namens `V1` von `a` nach Masse, `diode` von `a` nach Masse, Wert `DM`.

⁠**Direktiven:** `.model DM D(Is=5.4e-14)` und `.dc V1 -1 0.75 1m`

⁠**Was du siehst:** `I(D1)` mit logarithmischer Achse ist für positive Spannungen eine Gerade. Bei 0,5 V liest du 13,4 µ A, bei 0,6 V 0,641 mA, bei 0,7 V 30,6 mA. LTspice rechnet bei 27 °C, daher 1 % weniger als die Formel bei 300 K. Bei $-0{,}5$ V zeigt es $-0{,}55$ pA statt $-0{,}054$ pA, denn der Simulator legt der Diode $10^{-12}$ S parallel.
:::

:::zusatz Generation in der Zone
In Sperrrichtung ist Annahme 6 die schwächste. Paare aus der Zone zieht das Feld sofort auseinander. Das liefert rund $j_\mathrm{gen}=e\,n_\mathrm iL_\mathrm{depl}/(2\tau_\text{rec})$, bei $-5$ V das 12 000-fache von $j_\mathrm s$, nämlich $6{,}7\cdot10^{-8}\,\mathrm{A/cm^2}$. Es wächst mit $L_\mathrm{depl}$, reale Dioden sättigen deshalb nicht ganz.
:::

:::aufgabe Aufgabe 9 ★★ Wer trägt den Strom?
<span class="anker" id="aufg-9"></span>

Eine Diode hat $N_\mathrm A=10^{18}\,\mathrm{cm^{-3}}$ mit $\mu_\mathrm n=270\,\mathrm{cm^2/(V\,s)}$, $\tau_{\text{rec},\mathrm n}=0{,}1$ µ s und $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ mit $\mu_\mathrm p=419\,\mathrm{cm^2/(V\,s)}$, $\tau_{\text{rec},\mathrm p}=1$ µ s, die Fläche ist $A=4\,\mathrm{mm^2}$.

<ol class="al">

<li>

Berechne $L_\text{diff,n}$, $L_\text{diff,p}$ und beide Beiträge zu $j_\mathrm s$. Welche Sorte überwiegt, und warum?

</li>

<li>

Wie groß sind $I_\mathrm S$ und $U_\mathrm{pn}$ bei 1 mA? Was geschieht mit $j_\mathrm s$, wenn $N_\mathrm D$ sich verdoppelt?

</li>

</ol>

:::loesung
(a) $D_\mathrm n=6{,}98\,\mathrm{cm^2/s}$, $D_\mathrm p=10{,}8\,\mathrm{cm^2/s}$, $L_\text{diff,n}=8{,}4$ µ m, $L_\text{diff,p}=32{,}9$ µ m. Mit $n_\mathrm{p0}=79\,\mathrm{cm^{-3}}$ und $p_\mathrm{n0}=7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$: Elektronen $1{,}1\cdot10^{-13}\,\mathrm{A/cm^2}$, Löcher $4{,}2\cdot10^{-12}\,\mathrm{A/cm^2}$, $j_\mathrm s=4{,}3\cdot10^{-12}\,\mathrm{A/cm^2}$. Löcher tragen 97,5 %, denn im schwach dotierten n-Gebiet sind die Minoritäten hundertmal häufiger. (b) $I_\mathrm S=1{,}7\cdot10^{-13}$ A, $U_\mathrm{pn}=25{,}85\,\mathrm{mV}\cdot\ln(1\,\mathrm{mA}/I_\mathrm S)=0{,}581$ V. Bei doppeltem $N_\mathrm D$ halbiert sich der Löcheranteil, $j_\mathrm s$ sinkt auf $2{,}2\cdot10^{-12}\,\mathrm{A/cm^2}$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Die warme Diode
<span class="anker" id="aufg-10"></span>

Rechenmodell mit festem $I=1$ mA. $D_\mathrm n$, $D_\mathrm p$ und $\tau_\text{rec}$ gelten als temperaturunabhängig.

<ol class="al">

<li>

Berechne $U_\mathrm{pn}$ bei 300 K und bei 320 K, dazu den Faktor von $n_\mathrm i^2$ und $I_\mathrm S$.

</li>

<li>

Wie groß ist $\mathrm{d} U_\mathrm{pn}/\mathrm{d} T$? Warum sinkt die Spannung, obwohl $k_\mathrm BT/e$ steigt?

</li>

</ol>

:::loesung
(a) $U_\mathrm{pn}=25{,}85\,\mathrm{mV}\cdot\ln(10^{-3}/5{,}4\cdot10^{-14})=0{,}611$ V. Bei 320 K wächst $n_\mathrm i^2$ um den Faktor 18,2, $I_\mathrm S=9{,}8\cdot10^{-13}$ A, mit $k_\mathrm BT/e=27{,}58$ mV folgt $U_\mathrm{pn}=0{,}572$ V. (b) $-1{,}96$ mV/K. $k_\mathrm BT/e$ wächst nur um 7 %, aber $\ln(I/I_\mathrm S)$ schrumpft von 23,6 auf 20,7, denn $I_\mathrm S$ steigt steil.
:::
:::
