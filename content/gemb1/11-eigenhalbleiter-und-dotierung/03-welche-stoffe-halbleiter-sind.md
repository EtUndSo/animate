---
title: Stufe 1: Welche Stoffe Halbleiter sind
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
order: 4210300
summary: Eine Bandlücke haben viele Kristalle.
tags: Elementhalbleiter, Verbindungshalbleiter, III-V-Verbindungen, II-VI-Verbindungen, Wurtzit, Bänderdarstellung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Eine Bandlücke haben viele Kristalle. Diese Stufe zeigt, welche davon Halbleiter sind, was sie gemeinsam haben und wie groß ihre Lücke ist.
:::

**Die Idee.** Germanium, Silizium und Diamant haben dieselbe Struktur: Jedes Rumpfion ist tetraedrisch von vier nächsten Nachbarn umgeben ([Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html)). Jedes Atom gibt ein Elektron an jede seiner vier Bindungen und bleibt als vierfach positiver Rumpf $\mathrm{Si}^{4+}$ zurück. In jeder Bindung sitzen zwei Elektronen mit entgegengesetztem Spin, diese Valenzelektronen sind Bausteine des Gitters. Weitere Elektronen finden in den Bindungen keinen Platz: Das ist das volle Valenzband. Um ein Elektron frei beweglich zu machen, muss man es aus der Bindung lösen, und das kostet mindestens $E_\mathrm g$. Die Bandlücke misst also, wie fest die Valenzelektronen an ihrem Platz sitzen. Ob Wärme sie lösen kann, entscheidet über Halbleiter oder Isolator.

:::abbildung gemb1/k11material 1
Links: Bindungen, in die Ebene gedreht. Jede Bindung trägt zwei Elektronen. In GaAs bringen Ga drei und As fünf Elektronen mit, im Mittel also vier wie Si. Rechts: Bandabstände bei 300 K, grün der praktisch brauchbare Bereich von 0,1 bis 3 eV. C ist Diamant.
:::

:::definition Definition 1.1 (Element- und Verbindungshalbleiter)
<span class="anker" id="satz-1-1"></span>

Ein __Elementhalbleiter__ besteht aus einer einzigen Atomsorte, Silizium oder Germanium aus der Gruppe IV des Periodensystems. Ein __Verbindungshalbleiter__ besteht aus Atomsorten, die im Mittel ebenfalls vier Valenzelektronen je Atom mitbringen: __III-V-Verbindungen__ wie GaAs, InSb und AlAs, __II-VI-Verbindungen__ wie CdS, ferner IV-IV-Verbindungen wie SiC.
:::

⁠**So liest man das:** In GaAs bilden $3+5=8$ Elektronen vier Bindungsarme wie in Si. Die Rümpfe $\mathrm{Ga}^{3+}$ und $\mathrm{As}^{5+}$ sind verschieden geladen, deshalb hat die Bindung einen kleinen ionischen Anteil, sie heißt auch heteropolar. Die Verbindungen kristallisieren in der Zinkblendestruktur ([Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html)) oder als __Wurtzit__: zwei ineinandergeschachtelte hexagonale Gitter. In beiden hat jedes Atom vier Nachbarn der anderen Sorte. Brauchbar sind Bandlücken von 0,1 bis 3 eV, das sind bei 300 K rund 4 bis 116 $k_\mathrm BT$. Darunter regt Wärme schon sehr viele Elektronen an, darüber fast keine.

In der __Bänderdarstellung__ steht die Energie eines Elektrons nach oben, nach rechts der Ort $x$ oder die Zustandsdichte $D(E)$. Elektronen, die sich frei im Gitter bewegen, haben mindestens die Energie $E_\mathrm C$. Elektronen tieferer Schalen liegen noch unter dem Valenzband. Nur energiereiche Teilchen oder Röntgenstrahlung heben sie kurzzeitig ins Leitungsband.

:::satz Satz 1.2 (Temperaturabhängigkeit der Bandlücke)
<span class="anker" id="satz-1-2"></span>

Die Bandlücke schrumpft mit steigender Temperatur. Eine empirische Formel lautet

<span class="anker" id="gl-1-1"></span>
$$E_\mathrm g(T)=E_\mathrm g(0)-\frac{\alpha T^2}{T+\beta}. \tag{1.1}$$
:::

⁠**So liest man das:** $\alpha$ in eV/K und $\beta$ in K sind Materialwerte, für Si $E_\mathrm g(0)=1{,}170$ eV, $\alpha=4{,}73\cdot10^{-4}$ eV/K und $\beta=636$ K. Bei 0 K sind die Lücken in eV: Si 1,17, Ge 0,74, GaAs 1,52, InSb 0,23, InAs 0,36, CdS 2,58, CdTe 1,61, ZnO 3,44. Der Mechanismus: Wärme dehnt das Gitter und lässt die Atome schwingen. Beides schwächt im Mittel die Kopplung zwischen den Orbitalen ([Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html)), bindende und antibindende Zustände rücken zusammen. **Grenzfälle:** Für $T\ll\beta$ wächst der Abzug wie $T^2$, die Kurve beginnt flach. Für $T\gg\beta$ fällt sie mit der Steigung $-\alpha$.

::::beispiel
Silizium hat nach [(1.1)](#gl-1-1) bei 300 K den Wert 1,1245 eV und verliert dort 0,26 meV je Kelvin. Das Verhältnis $E_\mathrm g/(k_\mathrm BT)$ ist bei 300 K für InSb 7,0, für Ge 25,9, für Si 43,3 und für Diamant 213.
::::

:::frage Silizium und Diamant haben dieselbe Struktur. Warum ist das eine ein Halbleiter und das andere ein Isolator?
Die Struktur legt fest, dass das Valenzband voll ist, nicht wie groß die Lücke ist. Diamant hat kleine Atome und starke Bindungen, $E_\mathrm g=5{,}5$ eV. Das ist bei Raumtemperatur das 213-Fache von $k_\mathrm BT$, Wärme löst dort praktisch kein Elektron. Silizium isoliert ebenso, aber nur bei extrem tiefen Temperaturen.
:::

:::aufgabe Aufgabe 1 ★ Lücke und Wärme
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $\mathrm{e}^{-E_\mathrm g/(2k_\mathrm BT)}$ bei 300 K für InSb, Ge, Si und Diamant. Um wie viele Zehnerpotenzen liegen Si und Diamant auseinander?

</li>

<li>

Ordne InP, ZnSe, SiC und CdTe den Gruppen III-V, II-VI und IV-IV zu. Zeige, dass jedes Atompaar acht Valenzelektronen mitbringt.

</li>

<li>

Berechne $E_\mathrm g$ von Si bei 77 K und bei 400 K mit [(1.1)](#gl-1-1). Um wie viel unterscheiden sich beide Werte?

</li>

</ol>

:::loesung
(a) InSb $3{,}1\cdot10^{-2}$, Ge $2{,}4\cdot10^{-6}$, Si $3{,}9\cdot10^{-10}$, Diamant $6\cdot10^{-47}$. Si und Diamant trennen 37 Zehnerpotenzen. (b) InP: III-V, $3+5$. ZnSe und CdTe: II-VI, $2+6$. SiC: IV-IV, $4+4$. (c) $E_\mathrm g(77\,\mathrm{K})=1{,}166$ eV, $E_\mathrm g(400\,\mathrm{K})=1{,}097$ eV, Unterschied 69 meV.
:::
:::
