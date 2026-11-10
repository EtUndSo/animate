---
title: Stufe 7: Beweglichkeit und Leitfähigkeit
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Strom im Halbleiter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter
knoten: Kapitel 12: Strom im Halbleiter
order: 4220900
summary: (6.3) gilt für eine Trägersorte bei fester Streuzeit.
tags: zweidimensionalen Elektronengas, Heterostruktur, \delta-Dotierung, Photoleitfähigkeit, Photowiderstand
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
[(6.3)](der-stationare-strom.html#gl-6-3) gilt für eine Trägersorte bei fester Streuzeit. Diese Stufe zeigt, wie Temperatur und Dotierung die Beweglichkeit bestimmen, und setzt beide Sorten zur Leitfähigkeit zusammen.
:::

**Die Idee.** Wärme erzeugt mehr Phononen und macht die Träger schneller, beides verkürzt die Zeit bis zum nächsten Stoß. An geladenen Störstellen wirkt sie umgekehrt: Ein schnelles Teilchen wird weniger abgelenkt. Die Beweglichkeit hat deshalb ein Maximum.

:::satz Satz 7.1 (Temperatur und Beweglichkeit)
<span class="anker" id="satz-7-1"></span>

Es ist $\mu_\mathrm n=e\tau_\mathrm n/m_\mathrm n^*$, $\mu_\mathrm p=e\tau_\mathrm p/m_\mathrm p^*$ und $\tau=l_\mathrm{mfp}/v_\text{th}$. Bei Streuung an Phononen (ph) und an Ionen (ion) folgt daraus

<span class="anker" id="gl-7-1"></span>
$$\mu_{\mathrm n,\mathrm{ph}},\mu_{\mathrm p,\mathrm{ph}}\propto T^{-3/2},\qquad\mu_{\mathrm n,\mathrm{ion}},\mu_{\mathrm p,\mathrm{ion}}\propto T^{+3/2},\qquad\text{allgemein }\mu\propto T^{-\beta}. \tag{7.1}$$
:::

⁠**So liest man das:** Phononen, hier akustische (benachbarte Atome schwingen fast im Gleichtakt), bestimmen $\mu$ bei hoher Temperatur ($T\gtrsim100$ K) und niedriger Dotierung, Ionen bei tiefer Temperatur oder hoher Dotierung. Zusammen gilt $1/\mu=1/\mu_\mathrm{ph}+1/\mu_\mathrm{ion}$. Mehr Dotierung heißt mehr Stoßpartner, also kleineres $\mu$.

:::herleitung Die beiden Exponenten
⁠**Phononen.** Ihre Zahl wächst linear mit $T$, also $l_\mathrm{mfp}\propto1/T$. Aus $\frac{m^*}2v_\text{th}^2=\frac32k_\mathrm BT$ folgt $v_\text{th}\propto T^{1/2}$, zusammen $\tau\propto T^{-3/2}$.

⁠**Ionen.** Abgelenkt wird ein Träger, wenn die Coulomb-Energie am Ion seine Bewegungsenergie erreicht, also im Abstand $r\propto1/T$. Die Trefferfläche ist $\pi r^2\propto T^{-2}$, die Weglänge bei $N$ Ionen je Volumen $l_\mathrm{mfp}\propto T^2/N$, also $\tau\propto T^{3/2}/N$.
:::

Die Kurven in Abb. [7](#abb-7) rechnet ein Modell, bei Löchern mit 450 und 6000, der Exponent 0,7 ist an Messwerte angepasst:

$$\mu_\mathrm{ph}=1400\,\mathrm{\frac{cm^2}{V\,s}}\Bigl(\frac T{300\,\mathrm{K}}\Bigr)^{-3/2},\qquad\mu_\mathrm{ion}=8400\,\mathrm{\frac{cm^2}{V\,s}}\Bigl(\frac T{300\,\mathrm{K}}\Bigr)^{3/2}\Bigl(\frac N{10^{16}\,\mathrm{cm^{-3}}}\Bigr)^{-0{,}7}.$$

Gemessene $\beta$ sind meist größer als $\frac32$, und es gibt leichte und schwere Träger ([Kapitel 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)). In $N_\mathrm C$, $N_\mathrm V$ und in $\mu$ stehen daher verschieden gemittelte Massen.

| Stoff | Ge | Si | GaAs | InSb |
|---|---|---|---|---|
| $\mu_\mathrm n$, $\mu_\mathrm p$ in cm$^2$/(V s) | 3900, 1900 | 1400, 450 | 8500, 400 | 80 000, 1250 |
| $\beta_\mathrm n$, $\beta_\mathrm p$ | 1,6; 2,3 | 2,5; 2,7 | 0,65; 2 | 1,7; 1,8 |

:::satz Satz 7.2 (Leitfähigkeit)
<span class="anker" id="satz-7-2"></span>

Mit Elektronen und Löchern gilt

<span class="anker" id="gl-7-2"></span>
$$\sigma=\sigma_\mathrm n+\sigma_\mathrm p=e\,(n\,\mu_\mathrm n+p\,\mu_\mathrm p). \tag{7.2}$$
:::

In den Bereichen aus [Kapitel 11](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung/eigenhalbleiter-und-dotierung.html) vereinfacht sich das. In II und III zählt nur die Mehrheit, die Minderheit trägt in der Probe bei 300 K nur das $3\cdot10^{-13}$-Fache bei.

| Bereich | n-Typ, p-Typ | Temperaturgang |
|---|---|---|
| I Eigenleitung | $\sigma=n_\mathrm i\,e\,(\mu_\mathrm n+\mu_\mathrm p)$ | $\propto\exp\bigl(-E_\mathrm g/(2k_\mathrm BT)\bigr)$, steigt stark |
| II Erschöpfung | $\sigma=e\,N_\mathrm D\,\mu_\mathrm n$, $\sigma=e\,N_\mathrm A\,\mu_\mathrm p$ | $\propto T^{-\beta_\mathrm n}$, $\propto T^{-\beta_\mathrm p}$, sinkt |
| III Reserve | $\sigma=e\,n\,\mu_\mathrm n$, $n=N_\mathrm D^+<N_\mathrm D$; $\sigma=e\,p\,\mu_\mathrm p$, $p=N_\mathrm A^-<N_\mathrm A$ | steigt mit der Ionisation |

:::abbildung gemb1/k12beweglichkeit 7
Silizium im Modell. Oben: $\mu_\mathrm n$ über $T$ für drei Dotierungen, gestrichelt die Anteile für $10^{16}\,\mathrm{cm^{-3}}$, daneben $\mu_\mathrm n$ und $\mu_\mathrm p$ über der Dotierung bei 300 K. Unten: $\sigma$ der Probe über $1000/T$ mit den Bereichen I, II, III, daneben $\rho$ bei 300 K.
:::

**Ergänzung: Spezifischer Widerstand.** Halbleiterscheiben werden meist mit $\rho=1/\sigma=1/\bigl(e(n\mu_\mathrm n+p\mu_\mathrm p)\bigr)$ angegeben, in Erschöpfung $\rho=1/(eN_\mathrm D\mu_\mathrm n)$. Die Probe hat $\sigma=1{,}92$ S/cm und $\rho=0{,}52\,\Omega$ cm, reines Silizium $3{,}8\cdot10^{5}\,\Omega$ cm, Kupfer $1{,}7\cdot10^{-6}\,\Omega$ cm. Ein Fremdatom je 5 Millionen Atome senkt $\rho$ auf ein 730 000stel. In reinem Halbleiter hebt sich $T^{3/2}$ aus $n_\mathrm i$ gegen $\mu\propto T^{-3/2}$ weg, und $\sigma$ zeigt direkt $E_\mathrm g$. **Grenzfall:** Für $N\to0$ bleibt $\mu_\mathrm{ph}\propto T^{-3/2}$.

**Zwei Wege zu größerem $\mu$.** Man vergrößert $\tau$ oder verkleinert $m^*$. Thermische Träger sind siebenmal langsamer als die Elektronen an der Fermi-Kante von Kupfer und oft leichter, deshalb ist $\mu$ in Silizium 32-mal größer als dort. Noch weiter kommt man mit einem __zweidimensionalen Elektronengas__ (2DEG): In einer __Heterostruktur__, einer Schichtfolge verschiedener Halbleiter wie GaAs/AlGaAs oder InGaAs/InAlAs, sitzen die Dotieratome in einer dünnen Schicht neben der leitenden Schicht (__$\delta$-Dotierung__). Die Elektronen laufen getrennt von ihren Ionen, bei tiefer Temperatur mit sehr hoher Beweglichkeit.

:::frage Halbleiter leiten doch besser, wenn sie warm werden. Warum sinkt $\sigma$ im Bereich II?
Das gilt für reine Halbleiter, deren Dichte exponentiell wächst. Im Bereich II ist $n$ fest, und nur $\mu$ ändert sich. Die Probe fällt von 300 auf 400 K auf das 0,71-Fache: Sie verhält sich wie ein Metall.
:::

:::zusatz Photoleitung
Licht mit $\hbar\omega>E_\mathrm g$ erzeugt zusätzlich Paare aus Elektron und Loch. Die Erhöhung der Leitfähigkeit heißt __Photoleitfähigkeit__, ein __Photowiderstand__ misst damit Lichtintensität. Sie fällt im Kristall nach $I_\mathrm L(x)/I_\mathrm L(0)=\exp(-\alpha_\mathrm Px)$, und die steile Kante von $\alpha_\mathrm P$ über $\hbar\omega$ liefert $E_\mathrm g$. Dauerlicht erzeugt eine feste Dichte, aber kein thermodynamisches Gleichgewicht, denn es führt ständig Energie zu. Nach dem Abschalten klingt der Strom ab, und die Abklingzeit sagt, wie lange die zusätzlichen Träger im Mittel überleben.
:::

:::aufgabe Aufgabe 7 ★★ Eine Scheibe über alle Temperaturen
<span class="anker" id="aufg-7"></span>

Eine Scheibe aus n-Silizium hat $N_\mathrm D=4\cdot10^{15}\,\mathrm{cm^{-3}}$ und $\Delta E_\mathrm D=54$ meV. Über den ganzen Bereich herrsche ein Mechanismus, $\mu_\mathrm n\propto T^{-\beta}$ und $\mu_\mathrm n/\mu_\mathrm p=3$. Gemessen sind $\mu_\mathrm n(300\,\mathrm{K})=1300$ und $\mu_\mathrm n(400\,\mathrm{K})=652\,\mathrm{cm^2/(V\,s)}$.

<ol class="al">

<li>

Bestimme $\beta$. Welcher Mechanismus herrscht?

</li>

<li>

Berechne $\mu_\mathrm n$, $\mu_\mathrm p$ und $\sigma$ für 60 K (Reserve, $n=\sqrt{N_\mathrm CN_\mathrm D/2}\,\mathrm{e}^{-\Delta E_\mathrm D/(2k_\mathrm BT)}$), 200, 300, 400 K (Erschöpfung) und 900 K (Eigenleitung).

</li>

<li>

Skizziere $\lg\sigma$ über $1000/T$. Welcher berechnete Wert ist unglaubwürdig, und warum?

</li>

</ol>

:::loesung
(a) $\beta=\ln(1300/652)/\ln(400/300)=2{,}40$. $\mu$ sinkt mit $T$, also herrschen Phononen. (b) Mit $\mu_\mathrm n=1300\,\mathrm{cm^2/(V\,s)}\,(T/300\,\mathrm{K})^{-2{,}4}$:

| $T$ in K | 60 | 200 | 300 | 400 | 900 |
|---|---|---|---|---|---|
| $\mu_\mathrm n$ in cm$^2$/(V s) | 61 900 | 3440 | 1300 | 652 | 93 |
| $\mu_\mathrm p$ in cm$^2$/(V s) | 20 600 | 1150 | 433 | 217 | 31 |
| $\sigma$ in S/cm | 3,8 | 2,2 | 0,83 | 0,42 | 1,7 |

Bei 60 K ist $n=3{,}8\cdot10^{14}$, bei 900 K $n_\mathrm i=8{,}6\cdot10^{16}\,\mathrm{cm^{-3}}$ und $\sigma=n_\mathrm ie(\mu_\mathrm n+\mu_\mathrm p)$. (c) Von rechts: Anstieg in der Reserve, Abfall in der Erschöpfung, Tal, steiler Anstieg in der Eigenleitung. Unglaubwürdig ist $\mu_\mathrm n(60\,\mathrm{K})$: Bei so tiefer Temperatur begrenzen Störstellen die Beweglichkeit, ein einziger Mechanismus reicht nicht.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Die kleinste Leitfähigkeit
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Ersetze in [(7.2)](#gl-7-2) $p=n_\mathrm i^2/n$ und zeige: $\sigma$ ist minimal für $n=n_\mathrm i\sqrt{\mu_\mathrm p/\mu_\mathrm n}$, mit $\sigma_\text{min}=2en_\mathrm i\sqrt{\mu_\mathrm n\mu_\mathrm p}$.

</li>

<li>

Berechne für das Rechenmodell $n$, $p$, die nötige Dotierung und den größten $\rho$. Warum leitet diese Probe schlechter als reines Silizium, obwohl sie mehr Träger enthält?

</li>

</ol>

:::loesung
(a) $\sigma=e(n\mu_\mathrm n+n_\mathrm i^2\mu_\mathrm p/n)$, und $\mathrm{d}\sigma/\mathrm{d} n=0$ gibt $n^2=n_\mathrm i^2\mu_\mathrm p/\mu_\mathrm n$. (b) $n=5{,}0\cdot10^{9}$, $p=1{,}57\cdot10^{10}\,\mathrm{cm^{-3}}$, also p-Dotierung mit $N_\mathrm A=p-n=1{,}06\cdot10^{10}\,\mathrm{cm^{-3}}$. $\sigma_\text{min}=2{,}26\cdot10^{-6}$ S/cm, $\rho=4{,}4\cdot10^{5}\,\Omega$ cm, das 1,17-Fache des reinen Werts. Schnelle Elektronen wurden gegen langsame Löcher getauscht.
:::
:::
