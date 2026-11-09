---
title: Stufe 7: Tiefe Temperaturen und die Lage von $E_\mathrm F$
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
order: 4210900
summary: Bei tiefen Temperaturen reicht die Wärme nicht, um alle Donatoren zu ionisieren.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bei tiefen Temperaturen reicht die Wärme nicht, um alle Donatoren zu ionisieren. Diese Stufe berechnet $n$ und $E_\mathrm F$ in der Störstellenreserve und fasst die Lage von $E_\mathrm F$ für alle Bereiche zusammen.
:::

**Die Idee.** Unterhalb der Erschöpfung teilen sich die Donatoren in ionisierte und neutrale: $N_\mathrm D=N_\mathrm D^++N_\mathrm D^0$, ebenso $N_\mathrm A=N_\mathrm A^-+N_\mathrm A^0$. Ein neutraler Donator ist ein Vorrat an Elektronen, darum „Reserve“. Sinkt $T$, fallen die Elektronen auf die Donatoren zurück, der Halbleiter friert aus, englisch freeze-out. Paare spielen keine Rolle: Wegen $n>n_\mathrm i$ ist $n\gg p$, und die Neutralität wird zu $n=N_\mathrm D^+$. Das ist wieder eine Reaktion, $\mathrm D^0\rightleftharpoons\mathrm D^++\mathrm e^-$, mit dem Massenwirkungsgesetz

<span class="anker" id="gl-7-1"></span>
$$N_\mathrm D^+\cdot n=N_\mathrm D^0\cdot K_1(T),\qquad N_\mathrm A^-\cdot p=N_\mathrm A^0\cdot K_2(T), \tag{7.1}$$

mit $K_1=\frac12N_\mathrm C\mathrm{e}^{-\Delta E_\mathrm D/(k_\mathrm BT)}$ und $K_2=\frac1{g_\mathrm A}N_\mathrm V\mathrm{e}^{-\Delta E_\mathrm A/(k_\mathrm BT)}$. Beide enthalten den Boltzmann-Faktor der Aktivierungsenergie.

:::satz Satz 7.1 (Störstellenreserve, n-Typ)
<span class="anker" id="satz-7-1"></span>

Aus $n=N_\mathrm D^+$ folgt

<span class="anker" id="gl-7-2"></span>
$$n=\frac{K_1}2\Bigl(\sqrt{1+\frac{4N_\mathrm D}{K_1}}-1\Bigr)=\frac{N_\mathrm C}4\,\mathrm{e}^{-\Delta E_\mathrm D/(k_\mathrm BT)}\Bigl(\sqrt{1+8\frac{N_\mathrm D}{N_\mathrm C}\,\mathrm{e}^{\Delta E_\mathrm D/(k_\mathrm BT)}}-1\Bigr). \tag{7.2}$$

Tief in der Reserve, für $K_1\ll N_\mathrm D$, gilt

<span class="anker" id="gl-7-3"></span>
$$n=\sqrt{\frac{N_\mathrm DN_\mathrm C}2}\,\exp\Bigl(-\frac{E_\mathrm C-E_\mathrm D}{2k_\mathrm BT}\Bigr),\qquad E_\mathrm F=E_\mathrm C-\frac{E_\mathrm C-E_\mathrm D}2+\frac{k_\mathrm BT}2\ln\frac{N_\mathrm D}{2N_\mathrm C}. \tag{7.3}$$
:::

:::herleitung Von der Neutralität zur Wurzel
Mit $E_\mathrm F-E_\mathrm D=\Delta E_\mathrm D-(E_\mathrm C-E_\mathrm F)$ und [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) wird

$$N_\mathrm D^+=\frac{N_\mathrm D}{1+2\,\mathrm{e}^{\Delta E_\mathrm D/(k_\mathrm BT)}\,\mathrm{e}^{-(E_\mathrm C-E_\mathrm F)/(k_\mathrm BT)}}=\frac{N_\mathrm D}{1+2\,\mathrm{e}^{\Delta E_\mathrm D/(k_\mathrm BT)}\,n/N_\mathrm C}=\frac{N_\mathrm D}{1+n/K_1}.$$

$n=N_\mathrm D^+$ ergibt $n^2+K_1n-K_1N_\mathrm D=0$, also $n_{1,2}=-\frac{K_1}2\pm\sqrt{\frac{K_1^2}4+K_1N_\mathrm D}$. Nur das Plus ist positiv, Ausklammern ergibt [(7.2)](#gl-7-2). Für $K_1\ll N_\mathrm D$ ist die Wurzel viel größer als 1, und $n=\frac{K_1}2\sqrt{4N_\mathrm D/K_1}=\sqrt{K_1N_\mathrm D}$.

⁠**Anders gesehen:** Aus $n=N_\mathrm D^+$ folgt $n=\sqrt{n\,N_\mathrm D^+}$. Für $T\to0$ ist $N_\mathrm D^+\to\frac12N_\mathrm D\,\mathrm{e}^{-(E_\mathrm F-E_\mathrm D)/(k_\mathrm BT)}$. Im Produkt mit $n=N_\mathrm C\mathrm{e}^{-(E_\mathrm C-E_\mathrm F)/(k_\mathrm BT)}$ fällt $E_\mathrm F$ heraus, genau wie in [(0.2)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-2). $E_\mathrm F$ selbst folgt aus [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1).
:::

⁠**So liest man das:** Auf der logarithmischen Achse ist die Steigung $-\Delta E_\mathrm D/(2k_\mathrm B)$, wieder die halbe Energie, denn wieder entstehen zwei Teilchen. Die genaue Abhängigkeit ist $n\propto T^{3/4}\mathrm{e}^{-\Delta E_\mathrm D/(2k_\mathrm BT)}$. $E_\mathrm F$ liegt über $E_\mathrm D$. Für $T\to0$ geht $n$ gegen null, und $E_\mathrm F$ geht in die Mitte zwischen beiden Niveaus, $E_\mathrm F(T\to0)=\frac12(E_\mathrm C+E_\mathrm D)$.

⁠**Für Akzeptoren** ersetzt man $n$, $N_\mathrm C$, $N_\mathrm D$, $\Delta E_\mathrm D$ und die 2 durch $p$, $N_\mathrm V$, $N_\mathrm A$, $\Delta E_\mathrm A$ und $g_\mathrm A$. Mit $g_\mathrm A=2$ ist das

<span class="anker" id="gl-7-4"></span>
$$p=\sqrt{\frac{N_\mathrm AN_\mathrm V}2}\,\exp\Bigl(-\frac{E_\mathrm A-E_\mathrm V}{2k_\mathrm BT}\Bigr), \tag{7.4}$$

mit $g_\mathrm A=4$ steht unter der Wurzel $N_\mathrm AN_\mathrm V/4$. Allgemein ist $E_\mathrm F=E_\mathrm V+\frac12\Delta E_\mathrm A+\frac12k_\mathrm BT\ln(g_\mathrm AN_\mathrm V/N_\mathrm A)$, und $E_\mathrm F$ geht für $T\to0$ nach $\frac12(E_\mathrm V+E_\mathrm A)$. Die Minderheit folgt in jedem Fall aus $n\,p=n_\mathrm i^2$. **Gültigkeit:** $E_\mathrm F-E_\mathrm D>3k_\mathrm BT$, „tief“ in der Reserve, sonst [(7.2)](#gl-7-2).

:::abbildung gemb1/k11fermi 7
$E_\mathrm F$ in Silizium über $T$, numerisch aus der Neutralität, für $N_\mathrm D$ (blau) und $N_\mathrm A$ (rot) von $10^{14}$, $10^{16}$ und $10^{18}\,\mathrm{cm^{-3}}$, mit $\Delta E=45$ meV und $g_\mathrm A=4$. Für $T\to0$ laufen alle Kurven in die Mitte zwischen Bandkante und Niveau, bei hohen $T$ auf $E_\mathrm{Fi}$. Je höher die Dotierung, desto länger bleibt $E_\mathrm F$ nahe am Band.
:::

::::beispiel
Die Grenze $K_1=N_\mathrm D$ liegt für die Probe bei 95 K, dort ist $n=0{,}62\,N_\mathrm D$. Bei 77 K ist nach [(7.2)](#gl-7-2) $n=3{,}6\cdot10^{15}\,\mathrm{cm^{-3}}$, die Wurzel gibt 25 % zu viel. Bei 40 K sind $n=1{,}2\cdot10^{14}\,\mathrm{cm^{-3}}$, nur noch 1,2 % der Donatoren ionisiert, und die Wurzel stimmt auf 0,6 %. Dort ist $E_\mathrm C-E_\mathrm F=32$ meV, also $E_\mathrm F-E_\mathrm D=3{,}7\,k_\mathrm BT$. Für $T\to0$ bleiben 22,5 meV.
::::

⁠**Grenzfälle:** Für $K_1\gg N_\mathrm D$ ist die Wurzel in [(7.2)](#gl-7-2) $1+2N_\mathrm D/K_1$, also $n=N_\mathrm D$: Das ist die Erschöpfung. Sobald $2N_\mathrm C<N_\mathrm D$ wird, ist der Logarithmus in [(7.3)](#gl-7-3) positiv, und $E_\mathrm F$ nähert sich der Mitte von oben. Bei der Probe geschieht das erst unter 1 K, bei $10^{18}\,\mathrm{cm^{-3}}$ schon bei 20 K.

**Überblick für n-Typ.** Die Bereiche grenzen bei $n_\mathrm i=N_\mathrm D$ und $K_1=N_\mathrm D$ aneinander.

| Bereich | Bedingung | Dichten | Fermi-Energie |
|---|---|---|---|
| I Eigenleitung | $N_\mathrm D\ll2n_\mathrm i$ | $n=p=n_\mathrm i\propto T^{3/2}\mathrm{e}^{-E_\mathrm g/(2k_\mathrm BT)}$ | $E_\mathrm F\approx E_\mathrm{Fi}$, nahe der Bandmitte |
| II Erschöpfung | $N_\mathrm D\gg2n_\mathrm i$, $K_1\gg N_\mathrm D$ | $n=N_\mathrm D$, $p=n_\mathrm i^2/N_\mathrm D$ | $E_\mathrm F=E_\mathrm C-k_\mathrm BT\ln(N_\mathrm C/N_\mathrm D)$, steigt mit sinkendem $T$ |
| III Reserve | $K_1\ll N_\mathrm D$, $E_\mathrm F-E_\mathrm D>3k_\mathrm BT$ | $n\propto T^{3/4}\mathrm{e}^{-\Delta E_\mathrm D/(2k_\mathrm BT)}$, $n\gg p$ | $E_\mathrm F>E_\mathrm D$, geht gegen $\frac12(E_\mathrm C+E_\mathrm D)$ |

:::frage Heißt Sättigung hier dasselbe wie Erschöpfung?
Ja, beides ist Bereich II: $n$ sättigt bei $N_\mathrm D$, weil die Donatoren erschöpft sind.
:::

:::aufgabe Aufgabe 9 ★★ Aktivierungsenergie aus zwei Messungen
<span class="anker" id="aufg-9"></span>

Ein p-Halbleiter in der Reserve zeigt $p(50\,\mathrm{K})=8{,}3\cdot10^{13}\,\mathrm{cm^{-3}}$ und $p(80\,\mathrm{K})=2{,}71\cdot10^{15}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Bestimme $\Delta E_\mathrm A$ und nimm $N_\mathrm V$ als konstant an.

</li>

<li>

Bestimme $\Delta E_\mathrm A$ mit dem Faktor $T^{3/4}$. Wie groß ist der Fehler aus (a)? Welches Element passt?

</li>

</ol>

:::loesung
$\ln(p_2/p_1)=3{,}486$ und $1/T_1-1/T_2=7{,}5\cdot10^{-3}\,\mathrm{K^{-1}}$. (a) $\Delta E_\mathrm A=2k_\mathrm B\cdot3{,}486/(7{,}5\cdot10^{-3}\,\mathrm{K^{-1}})=80$ meV. (b) Vom Logarithmus geht $\frac34\ln(T_2/T_1)=0{,}353$ ab, also $\Delta E_\mathrm A=72$ meV: Gallium. Der Fehler aus (a) beträgt 11 %.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Eine Probe von 40 K bis 900 K
<span class="anker" id="aufg-10"></span>

Si mit Arsen: $N_\mathrm D=3\cdot10^{15}\,\mathrm{cm^{-3}}$, $\Delta E_\mathrm D=54$ meV, $E_\mathrm g$ fest, $T=40$, 80, 150, 300, 500, 700, 900 K.

<ol class="al">

<li>

Bestimme die Grenzen der drei Bereiche und ordne jede Temperatur zu.

</li>

<li>

Berechne für jede Temperatur $N_\mathrm C$, $N_\mathrm V$, $n_\mathrm i$, $n$, $p$, $E_\mathrm C-E_\mathrm F$ und $E_\mathrm F-E_\mathrm V$ mit der Formel des jeweiligen Bereichs.

</li>

<li>

Skizziere $n$ über $1000/T$ und $E_\mathrm F$ im Banddiagramm. Vorhersage: Bei welchen Temperaturen ist die Formel am ungenauesten?

</li>

</ol>

:::loesung
(a) $K_1=N_\mathrm D$ bei 94 K, $n_\mathrm i=N_\mathrm D$ bei 645 K. 40 K und 80 K: III. 150, 300, 500 K: II. 700 K und 900 K: I, mit [(6.1)](hohe-und-mittlere-temperaturen.html#gl-6-1) und [(6.2)](hohe-und-mittlere-temperaturen.html#gl-6-2). (b) Dichten in cm$^{-3}$, Energien in eV:

| $T$ in K | $N_\mathrm C$ | $N_\mathrm V$ | $n_\mathrm i$ | $n$ | $p$ | $E_\mathrm C-E_\mathrm F$ | $E_\mathrm F-E_\mathrm V$ |
|---|---|---|---|---|---|---|---|
| 40 | $1{,}37\cdot10^{18}$ | $8{,}9\cdot10^{17}$ | $3\cdot10^{-53}$ | $1{,}8\cdot10^{13}$ | $\approx0$ | 0,039 | 1,081 |
| 80 | $3{,}88\cdot10^{18}$ | $2{,}5\cdot10^{18}$ | $1{,}6\cdot10^{-17}$ | $1{,}5\cdot10^{15}$ | $\approx0$ | 0,054 | 1,066 |
| 150 | $9{,}96\cdot10^{18}$ | $6{,}5\cdot10^{18}$ | 1,2 | $3{,}0\cdot10^{15}$ | $5\cdot10^{-16}$ | 0,105 | 1,015 |
| 300 | $2{,}82\cdot10^{19}$ | $1{,}83\cdot10^{19}$ | $8{,}9\cdot10^{9}$ | $3{,}0\cdot10^{15}$ | $2{,}6\cdot10^{4}$ | 0,236 | 0,884 |
| 500 | $6{,}06\cdot10^{19}$ | $3{,}9\cdot10^{19}$ | $1{,}1\cdot10^{14}$ | $3{,}0\cdot10^{15}$ | $4{,}1\cdot10^{12}$ | 0,427 | 0,693 |
| 700 | $1{,}00\cdot10^{20}$ | $6{,}5\cdot10^{19}$ | $7{,}5\cdot10^{15}$ | $9{,}2\cdot10^{15}$ | $6{,}2\cdot10^{15}$ | 0,561 | 0,559 |
| 900 | $1{,}46\cdot10^{20}$ | $9{,}5\cdot10^{19}$ | $8{,}6\cdot10^{16}$ | $8{,}8\cdot10^{16}$ | $8{,}5\cdot10^{16}$ | 0,575 | 0,545 |

(c) Am ungenauesten ist die Formel nahe den Grenzen: Bei 80 K ergibt die Numerik $n=1{,}2\cdot10^{15}\,\mathrm{cm^{-3}}$ und 0,056 eV, die Wurzel ist 29 % zu groß. Bei 150 K ist $n=2{,}9\cdot10^{15}\,\mathrm{cm^{-3}}$. Bei 700 K und 900 K stimmt [(6.1)](hohe-und-mittlere-temperaturen.html#gl-6-1) auf 0,01 %.
:::
:::
