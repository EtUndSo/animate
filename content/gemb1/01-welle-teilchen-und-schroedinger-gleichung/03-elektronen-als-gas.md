---
title: Stufe 1: Elektronen als Gas
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Welle, Teilchen und Schrödinger-Gleichung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung
knoten: Kapitel 1: Welle, Teilchen und Schrödinger-Gleichung
order: 4110300
summary: Der Widerstand hängt von der Form des Drahts ab.
tags: Atomrümpfen, Drude-Modell, Drift, Stromdichte, elektrische Feldstärke, spezifischer Widerstand, intrinsisch, Driftgeschwindigkeit
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Der Widerstand hängt von der Form des Drahts ab. Diese Stufe findet die Größe, die nur vom Stoff abhängt, erklärt sie im einfachsten Bild und zeigt dessen Grenzen.
:::

**Die Idee.** Teilt man den Strom durch die Querschnittsfläche und die Spannung durch die Länge, fällt die Form heraus, und es bleibt ein Gesetz des Stoffs. Um es zu erklären, stellt man sich die beweglichen Elektronen als Gas vor, das zwischen den festen __Atomrümpfen__ (Kerne mit den fest gebundenen inneren Elektronen) umherfliegt. Das ist das __Drude-Modell__. Die Wärme treibt jedes Elektron schnell in zufällige Richtungen, und es stößt ständig gegen Rümpfe. Im Mittel kommt es nicht voran. Ein elektrisches Feld schiebt alle Elektronen zwischen zwei Stößen ein Stück in dieselbe Richtung, jeder Stoß macht diesen Gewinn wieder zunichte. Übrig bleibt eine langsame gemeinsame Bewegung, die __Drift__ (Abb. [1](#abb-1)).

:::abbildung gemb1/k1drude 1
Weg eines Elektrons (blau, schematisch) zwischen den Atomrümpfen (grau). Links ohne Feld: Der Weg führt nirgendwohin. Rechts mit Feld: Zwischen zwei Stößen kommt ein kleiner Anteil gegen die Feldrichtung dazu, der rote Pfeil zeigt die Verschiebung. Die Drift ist hier stark übertrieben.
:::

:::definition Definition 1.1 (Stoffgrößen)
<span class="anker" id="satz-1-1"></span>

Ein Draht der Länge $\ell$ mit dem Querschnitt $A$ trägt bei der Spannung $U$ den Strom $I$, und es gilt $U=R\,I$. __Stromdichte__ $j$, __elektrische Feldstärke__ $\mathcal E$ und __spezifischer Widerstand__ $\rho$ sind

<span class="anker" id="gl-1-1"></span>
$$j=\frac IA,\qquad\mathcal E=\frac U\ell,\qquad R=\rho\,\frac\ell A. \tag{1.1}$$

Mit der Leitfähigkeit $\sigma=1/\rho$ lautet das ohmsche Gesetz dann

<span class="anker" id="gl-1-2"></span>
$$j=\sigma\,\mathcal E. \tag{1.2}$$
:::

⁠**So liest man das:** Einsetzen von [(1.1)](#gl-1-1) in $I=U/R$ gibt $j\,A=\mathcal E\,\ell\,A/(\rho\,\ell)$, Länge und Fläche kürzen sich. Einheiten: $j$ in A/m$^2$, $\mathcal E$ in V/m, $\rho$ in $\Omega$ m, $\sigma$ in S/m. Formunabhängige Größen heißen __intrinsisch__. Offen ist, woraus $\sigma$ besteht.

:::satz Satz 1.2 (Drude-Modell)
<span class="anker" id="satz-1-2"></span>

Elektronen der Dichte $n$ mit der mittleren Zeit $\tau$ zwischen zwei Stößen haben im Feld $\mathcal E$

<span class="anker" id="gl-1-3"></span>
$$v_\mathrm d=-\mu\,\mathcal E,\qquad\mu=\frac{e\,\tau}{m_0},\qquad j=-e\,n\,v_\mathrm d=e\,n\,\mu\,\mathcal E,\qquad\sigma=e\,n\,\mu. \tag{1.3}$$
:::

⁠**So liest man das:** $v_\mathrm d$ ist die __Driftgeschwindigkeit__. Das Minus sagt: Elektronen tragen die Ladung $-e$ und laufen gegen das Feld, der Strom fließt mit dem Feld. $n$ ist die __Ladungsträgerdichte__, die Zahl beweglicher Ladungen je m$^3$. $\tau$ heißt __Relaxationszeit__. Die __Beweglichkeit__ $\mu$ in m$^2$/(V s) sagt, wie schnell ein Feld die Elektronen treibt. **Gültigkeit:** $|v_\mathrm d|$ klein gegen die Wärmebewegung, dann bleibt $\tau$ fest und $j$ wächst linear mit $\mathcal E$.

:::herleitung Wärmebewegung und Drift
⁠**Wärmebewegung.** Im idealen Gas (Teilchen, die nur stoßen) verteilen sich die Beträge der Geschwindigkeit nach

$$f(v)=4\pi v^2\Bigl(\frac{m_0}{2\pi k_\mathrm BT}\Bigr)^{3/2}\mathrm{e}^{-m_0v^2/(2k_\mathrm BT)},\qquad\int_0^\infty f(v)\,\mathrm{d} v=1.$$

Der Exponentialfaktor macht hohe Energien selten, $4\pi v^2$ zählt die Geschwindigkeitsvektoren gleichen Betrags (eine Kugelschale). Die mittlere Bewegungsenergie ist $\langle E_\mathrm{kin}\rangle=\int_0^\infty\frac12m_0v^2f(v)\,\mathrm{d} v=\frac32k_\mathrm BT$. Gleichsetzen mit $\frac12m_0v_\mathrm e^2$ gibt die __thermische Geschwindigkeit__ $v_\mathrm e=\sqrt{3k_\mathrm BT/m_0}=1{,}17\cdot10^{5}$ m/s. Weil alle Richtungen gleich häufig sind, ist das Mittel der Geschwindigkeitsvektoren null.

⁠**Stöße.** Das Modell lässt jedes Elektron schon nach wenigen Atomabständen stoßen: Die __mittlere freie Weglänge__ $l_\mathrm{mfp}$, die Strecke zwischen zwei Stößen, beträgt rund 1 nm. Das gibt $\tau=l_\mathrm{mfp}/v_\mathrm e\approx10^{-14}$ s.

⁠**Drift.** Das Feld übt die Kraft $F=-e\mathcal E$ aus. Die Zeit $t$ nach einem Stoß hat ein Elektron die Geschwindigkeit $v_\text{Stoß}+F\,t/m_0$. Im Mittel über alle Elektronen fällt der zufällige Teil weg, und der letzte Stoß liegt $\tau$ zurück: $v_\mathrm d=-e\,\mathcal E\,\tau/m_0$. Durch die Fläche $A$ läuft in der Zeit $\Delta t$ die Ladung aller Elektronen im Zylinder der Länge $|v_\mathrm d|\Delta t$. Das gibt $j=e\,n\,|v_\mathrm d|$.
:::

::::beispiel
Mit $\tau=8{,}6\cdot10^{-15}$ s folgen für Kupfer $\mu=1{,}5\cdot10^{-3}\,\mathrm{m^2/(V\,s)}$ und $\sigma=2{,}1\cdot10^{7}$ S/m. Das liegt nur um den Faktor 2,9 unter dem Messwert. Bei 1 A in 1 mm$^2$ ist $j=10^{6}\,\mathrm{A/m^2}$, $\mathcal E=17$ mV/m und $|v_\mathrm d|=0{,}073$ mm/s. Die Elektronen rasen also $1{,}6\cdot10^{9}$-mal schneller, als sie vorankommen: Der Strom ist eine winzige Schlagseite der Wärmebewegung.
::::

⁠**Grenzfälle:** Für $n\to0$ gibt es keine Träger, $\sigma\to0$. Für $\tau\to\infty$ bremst nichts mehr, $\sigma\to\infty$.

**Wo das Bild endet.** Die Tabelle zeigt gemessene Leitfähigkeiten.

| Stoff | Ag | Cu | Au | Al | Na | Ti | Bi |
|---|---|---|---|---|---|---|---|
| $\sigma$ in S/m | $6{,}2\cdot10^{7}$ | $5{,}9\cdot10^{7}$ | $4{,}9\cdot10^{7}$ | $3{,}8\cdot10^{7}$ | $2{,}1\cdot10^{7}$ | $2{,}5\cdot10^{6}$ | $7{,}7\cdot10^{5}$ |
| Stoff | TiO | Ge | Si | NiO | Al$_2$O$_3$ | SiO$_2$ | Teflon |
| $\sigma$ in S/m | $3\cdot10^{5}$ | $2$ | $10^{-3}$ | $10^{-8}$ | $10^{-12}$ | $10^{-16}$ | $10^{-22}$ |

Alle Festkörper enthalten rund $10^{29}$ Atome je m$^3$, im Gasmodell hängen $n$ und $\tau$ also kaum vom Stoff ab. Trotzdem liegen zwischen Silber und Teflon fast 30 Zehnerpotenzen. Weitere Befunde bleiben unerklärt:

<ul>

<li>

Aluminium hat je Atom weniger äußere Elektronen als Titan oder Bismut und leitet trotzdem besser.

</li>

<li>

Silber und Kupfer leiten besser als Gold, obwohl jedes dieser Atome ein äußeres Elektron hat.

</li>

<li>

Silizium steht im Periodensystem neben Aluminium, hat ein Elektron mehr und leitet zehn Zehnerpotenzen schlechter. Dennoch baut die ganze Chipindustrie auf ihm auf.

</li>

</ul>

Auch eine Grenze zwischen __Metall__, __Halbleiter__ (mittlere Leitfähigkeit, etwa Silizium) und __Isolator__ (leitet praktisch nicht) zeigen die Zahlen nicht. Selbst bei Metallen stimmt die Größenordnung nur, weil sich zwei Fehler gegenseitig aufheben: Die angenommene Dichte beweglicher Ladungsträger ist zu hoch, denn tatsächlich nehmen nur wenige der äußeren Elektronen an der Leitung teil, diese aber viel schneller als im Gasmodell. Die mittlere freie Weglänge ist dagegen viel zu klein angesetzt. Die richtigen Werte beider Größen, die großen Unterschiede der Leitfähigkeit, den Unterschied zwischen Metall und Halbleiter oder Isolator, die Temperaturabhängigkeit der Leitfähigkeit und __optoelektronische Effekte__ (Licht wird zu Strom und umgekehrt) liefert erst die Quantenmechanik. Das Gasmodell setzt voraus, dass ein Elektron eine kleine Kugel ist. Diese Annahme gilt es zu prüfen.

:::frage Die Elektronen rasen mit über 100 km/s. Warum fließt ohne Spannung kein Strom?
Strom ist der Überschuss an Ladung in eine Richtung. Ohne Feld queren je Sekunde gleich viele Elektronen eine Fläche nach links wie nach rechts. Jedes einzelne ist schnell, der Mittelwert der Vektoren ist null.
:::

:::aufgabe Aufgabe 1 ★★ Eine Leiterbahn prüfen
<span class="anker" id="aufg-1"></span>

Eine Kupferbahn im Chip ist 10 µ m lang, 100 nm breit, 100 nm hoch und trägt 100 µ A.

<ol class="al">

<li>

Berechne $j$, $\mathcal E$, die Spannung über der Bahn und $|v_\mathrm d|$.

</li>

<li>

Bestimme aus dem gemessenen $\sigma$ die Werte $\mu$ und $\tau$. Welche mittlere freie Weglänge folgt daraus mit $v_\mathrm e$?

</li>

<li>

Silizium ($5\cdot10^{28}$ Atome je m$^3$) habe dieselbe Beweglichkeit. Welches $n$ ergibt $\sigma=10^{-3}$ S/m? Wie viele Atome kommen auf ein freies Elektron? Kann das Gasmodell diese Zahl begründen?

</li>

</ol>

:::loesung
(a) $A=(100\,\mathrm{nm})^2=10^{-14}\,\mathrm{m^2}$, also $j=10^{-4}\,\mathrm{A}/10^{-14}\,\mathrm{m^2}=10^{10}\,\mathrm{A/m^2}$. Dann ist $\mathcal E=j/\sigma=170$ V/m, über 10 µ m liegen 1,7 mV, und $|v_\mathrm d|=j/(e\,n)=0{,}73$ m/s. (b) $\mu=\sigma/(e\,n)=4{,}3\cdot10^{-3}\,\mathrm{m^2/(V\,s)}$, $\tau=\mu\,m_0/e=2{,}5\cdot10^{-14}$ s, $l_\mathrm{mfp}=v_\mathrm e\tau=2{,}9$ nm, also rund elf Atomabstände. (c) $n=\sigma/(e\,\mu)=1{,}4\cdot10^{18}\,\mathrm{m^{-3}}$. Auf ein freies Elektron kommen $3{,}5\cdot10^{10}$ Atome. Im Gasmodell gibt jedes Atom seine äußeren Elektronen ab. Warum nur eines von 35 Milliarden frei sein soll, kann es nicht sagen.
:::
:::
