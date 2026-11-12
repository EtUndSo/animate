---
title: Stufe 7: Parallel- und Reihenschaltung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130800
summary: Mehrere Kondensatoren lassen sich wie einer behandeln.
tags: Insel
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Mehrere Kondensatoren lassen sich wie einer behandeln. Die Frage ist nur, welche Größe die Schaltung für alle gleich macht.
:::

**Die Idee.** ⁠**Parallel:** Alle oberen Platten hängen an einem Draht, alle unteren an einem anderen. Ein Draht ohne Strom hat überall dasselbe Potenzial, deshalb liegt an allen Kondensatoren dieselbe Spannung. Die Schaltung wirkt wie eine vergrößerte Platte, die Ladungen addieren sich. **Reihe:** Die untere Platte von $C_1$ und die obere von $C_2$ bilden mit ihrem Verbindungsdraht eine __Insel__: ein Leiterstück, zu dem nur Isolatoren führen (Abb. [7](#abb-7)). Ladung kann dort weder hinein noch heraus. War die Insel ungeladen, bleibt ihre Summe null: Zieht die obere Platte $+Q$ an der Insel $-Q$ an, muss das fehlende Gegenstück als $+Q$ auf die nächste Platte. Alle tragen also dieselbe Ladung, und die Spannungen addieren sich. Die Schaltung wirkt wie ein vergrößerter Abstand.

:::abbildung et1/k3schaltungen 7
$C_1=100\,\mu\text{F}$ und $C_2=50\,\mu\text{F}$ an 9 V. Parallel: dieselbe Spannung, die Ladungen addieren sich zu 1350 µC. In Reihe: dieselbe Ladung 300 µC, weil die gestrichelt umrandete Insel neutral bleibt. Der kleinere Kondensator bekommt die größere Spannung.
:::

:::satz Satz 7.1 (Gesamtkapazität)
<span class="anker" id="satz-7-1"></span>

Für $n$ parallel geschaltete Kondensatoren (links) und $n$ in Reihe geschaltete, anfangs ungeladene Kondensatoren (rechts) gilt

<span class="anker" id="gl-7-1"></span>
$$C_\mathrm{G}=\sum_{i=1}^nC_i,\qquad\qquad\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}. \tag{7.1}$$

Für zwei Kondensatoren in Reihe ist $C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2}$, und die Spannung teilt sich gemäß $U_1=U_\mathrm{G}\,\dfrac{C_2}{C_1+C_2}$.
:::

:::herleitung Gesamtkapazität
⁠**Parallel.** Zwang der Schaltung: $U_i=U_\mathrm{G}$ für alle $i$. Einzelladung: $Q_i=C_iU_i=C_iU_\mathrm{G}$. Gesamtladung: $Q_\mathrm{G}=\sum Q_i=U_\mathrm{G}\sum C_i$. Mit $C_\mathrm{G}=Q_\mathrm{G}/U_\mathrm{G}$ folgt die linke Formel.

⁠**Reihe.** Zwang der Schaltung: $Q_i=Q_\mathrm{G}$ für alle $i$. Gesamtspannung: $U_\mathrm{G}=\sum U_i$. Teilspannung: $U_i=Q_i/C_i=Q_\mathrm{G}/C_i$. Also $U_\mathrm{G}=Q_\mathrm{G}\sum 1/C_i$, und mit $U_\mathrm{G}=Q_\mathrm{G}/C_\mathrm{G}$ folgt die rechte Formel. Für den Teiler: $U_1=Q_\mathrm{G}/C_1=U_\mathrm{G}\,C_\mathrm{G}/C_1=U_\mathrm{G}\,C_2/(C_1+C_2)$.
:::

⁠**So liest man das:** $C_\mathrm{G}$ ist die Kapazität eines einzelnen Kondensators, der dasselbe Verhalten an den beiden Außenklemmen zeigt. Parallel wird $C_\mathrm{G}$ größer als jeder Einzelwert, in Reihe kleiner als der kleinste. **Gültigkeit:** Die rechte Formel braucht ungeladene Inseln beim Start. Sonst bleibt die alte Inselladung erhalten, und $Q_i=Q_\mathrm{G}$ gilt nur für die hinzukommende Ladung.

::::beispiel
Parallel: $C_\mathrm{G}=150\,\mu\text{F}$, $Q_1=900\,\mu\text{C}$, $Q_2=450\,\mu\text{C}$. In Reihe: $1/C_\mathrm{G}=1/(100\,\mu\text{F})+1/(50\,\mu\text{F})$, also $C_\mathrm{G}=33{,}3\,\mu\text{F}$. Bei 9 V ist $Q=300\,\mu\text{C}$, $U_1=3$ V und $U_2=6$ V.
::::

⁠**Grenzfälle:** Für $C_2\to\infty$ geht in Reihe $C_\mathrm{G}\to C_1$, ein riesiger Kondensator verhält sich wie ein Draht. Für $C_2\to0$ geht in Reihe $C_\mathrm{G}\to0$, die Lücke unterbricht, parallel bleibt $C_1$.

:::frage Warum sind die Formeln genau umgekehrt wie bei Widerständen?
Bei Widerständen gilt $u=R\,i$: In Reihe addieren sich die Spannungen bei gleichem Strom, also addiert sich $R$. Beim Kondensator gilt $u=\frac1C\,q$: In Reihe addieren sich die Spannungen bei gleicher Ladung, also addiert sich $1/C$. **Kurz gesagt:** $1/C$ spielt beim Kondensator die Rolle von $R$.
:::

:::aufgabe Aufgabe 8 ★★ Ein gemischtes Netz
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Zwei Kondensatoren mit 10 µF und 20 µF liegen parallel, dazu in Reihe 60 µF, das Ganze an 9 V. Berechne $C_\mathrm{G}$, die Gesamtladung, alle Spannungen und alle Einzelladungen.

</li>

<li>

Zwei gleiche Kondensatoren mit 100 µF und 16 V Höchstspannung liegen in Reihe. Welche Kapazität und welche Höchstspannung hat die Kette?

</li>

</ol>

:::loesung
(a) Parallel: $10+20=30\,\mu\text{F}$. Mit 60 µF in Reihe: $C_\mathrm{G}=\frac{30\cdot60}{30+60}\,\mu\text{F}=20\,\mu\text{F}$. $Q=20\,\mu\text{F}\cdot9\,\mathrm{V}=180\,\mu\text{C}$. Am 60-µF-Kondensator: $180\,\mu\text{C}/60\,\mu\text{F}=3$ V. Am Parallelblock: $180\,\mu\text{C}/30\,\mu\text{F}=6$ V, zusammen 9 V. Die Ladung teilt sich: $10\,\mu\text{F}\cdot6\,\mathrm{V}=60\,\mu\text{C}$ und $20\,\mu\text{F}\cdot6\,\mathrm{V}=120\,\mu\text{C}$.

(b) $C_\mathrm{G}=50\,\mu\text{F}$. Bei gleichen Kondensatoren teilt sich die Spannung gleich, also je 16 V und zusammen 32 V.
:::
:::

::::formelsammlung
**Parallelschaltung**

$$C_\mathrm{G}=\sum_{i=1}^nC_i$$

$n$ Kondensatoren an denselben zwei Drähten: gleiche Spannung $U_i=U_\mathrm{G}$, die Ladungen addieren sich. Wirkt wie eine vergrößerte Platte; $C_\mathrm{G}$ ist größer als jeder Einzelwert.

**Reihenschaltung**

$$\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}$$

$n$ anfangs ungeladene Kondensatoren hintereinander: gleiche Ladung $Q_i=Q_\mathrm{G}$, weil die Inseln dazwischen neutral bleiben; die Spannungen addieren sich. Wirkt wie ein vergrößerter Abstand; $C_\mathrm{G}$ ist kleiner als der kleinste Einzelwert. $1/C$ spielt die Rolle von $R$.

**Zwei Kondensatoren in Reihe**

$$C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2},\qquad U_1=U_\mathrm{G}\,\dfrac{C_2}{C_1+C_2}$$

Der kleinere Kondensator bekommt die größere Spannung. Grenzfälle: $C_2\to\infty$ ergibt $C_\mathrm{G}\to C_1$, $C_2\to0$ ergibt $C_\mathrm{G}\to0$.
::::

::::lernkarten
:::karte formel Parallelschaltung
Wie groß ist die Gesamtkapazität von $n$ parallel geschalteten Kondensatoren, und welche Größe ist für alle gleich?
---
$C_\mathrm{G}=\sum_{i=1}^nC_i$: An allen liegt dieselbe Spannung, die Ladungen addieren sich. $C_\mathrm{G}$ ist größer als jeder Einzelwert.
--- falsch
$\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}$: An allen liegt dieselbe Spannung, die Kehrwerte addieren sich. $C_\mathrm{G}$ ist kleiner als der kleinste Einzelwert.
--- falsch
$C_\mathrm{G}=\sum_{i=1}^nC_i$: Alle tragen dieselbe Ladung, die Spannungen addieren sich. $C_\mathrm{G}$ ist größer als jeder Einzelwert.
--- falsch
$C_\mathrm{G}=\frac1n\sum_{i=1}^nC_i$: An allen liegt dieselbe Spannung, die Kapazitäten mitteln sich. $C_\mathrm{G}$ liegt zwischen den Einzelwerten.
:::
:::karte formel Reihenschaltung
Wie groß ist die Gesamtkapazität von $n$ anfangs ungeladenen Kondensatoren in Reihe, und welche Größe ist für alle gleich?
---
$\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}$: Alle tragen dieselbe Ladung, die Spannungen addieren sich. $C_\mathrm{G}$ ist kleiner als der kleinste Einzelwert.
--- falsch
$C_\mathrm{G}=\sum_{i=1}^nC_i$: Alle tragen dieselbe Ladung, die Spannungen addieren sich. $C_\mathrm{G}$ ist größer als jeder Einzelwert, wie bei Widerständen.
--- falsch
$\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}$: An allen liegt dieselbe Spannung, die Ladungen addieren sich. $C_\mathrm{G}$ ist kleiner als der kleinste Einzelwert.
--- falsch
$\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}$: Alle tragen dieselbe Ladung, auch wenn sie vor dem Zusammenschalten verschieden geladen waren.
:::
:::karte formel Zwei Kondensatoren in Reihe
Wie groß sind die Gesamtkapazität und die Teilspannung $U_1$, wenn zwei Kondensatoren $C_1$ und $C_2$ in Reihe an $U_\mathrm{G}$ liegen?
---
$C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2}$ und $U_1=U_\mathrm{G}\,\dfrac{C_2}{C_1+C_2}$: Der kleinere Kondensator bekommt die größere Spannung.
--- falsch
$C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2}$ und $U_1=U_\mathrm{G}\,\dfrac{C_1}{C_1+C_2}$: Der größere Kondensator bekommt die größere Spannung.
--- falsch
$C_\mathrm{G}=C_1+C_2$ und $U_1=U_\mathrm{G}\,\dfrac{C_2}{C_1+C_2}$: Der kleinere Kondensator bekommt die größere Spannung.
--- falsch
$C_\mathrm{G}=\dfrac{C_1+C_2}{C_1C_2}$ und $U_1=U_\mathrm{G}/2$: Beide bekommen dieselbe Spannung, gleich wie groß sie sind.
:::
:::karte herleitung Gesamtkapazität parallel
Leite aus der gleichen Spannung an allen Kondensatoren her, dass für $n$ parallel geschaltete Kondensatoren $C_\mathrm{G}=\sum_{i=1}^nC_i$ gilt.
---
Zwang der Schaltung: $U_i=U_\mathrm{G}$ für alle $i$, weil alle oberen Platten an einem Draht hängen und alle unteren an einem anderen.
---
Jeder trägt $Q_i=C_iU_i=C_iU_\mathrm{G}$, weil für jeden einzelnen Kondensator $Q=C\,U$ gilt.
---
Die Gesamtladung ist $Q_\mathrm{G}=\sum Q_i=U_\mathrm{G}\sum C_i$, weil sich die Ladungen der parallelen Platten addieren.
---
Mit $C_\mathrm{G}=Q_\mathrm{G}/U_\mathrm{G}$ folgt $C_\mathrm{G}=\sum_{i=1}^nC_i$, weil die Gesamtkapazität das Verhältnis von Ladung und Spannung an den Außenklemmen ist.
:::
:::karte herleitung Gesamtkapazität in Reihe
Leite aus der gleichen Ladung aller Kondensatoren her, dass für $n$ anfangs ungeladene Kondensatoren in Reihe $\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}$ gilt.
---
Zwang der Schaltung: $Q_i=Q_\mathrm{G}$ für alle $i$, weil die Inseln zwischen den Kondensatoren neutral bleiben.
---
Die Gesamtspannung ist $U_\mathrm{G}=\sum U_i$, weil sich die Spannungen längs der Kette nach der Maschenregel addieren.
---
Jede Teilspannung ist $U_i=Q_i/C_i=Q_\mathrm{G}/C_i$, weil für jeden Kondensator $Q=C\,U$ gilt.
---
Also ist $U_\mathrm{G}=Q_\mathrm{G}\sum 1/C_i$, und mit $U_\mathrm{G}=Q_\mathrm{G}/C_\mathrm{G}$ folgt $\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}$, weil $Q_\mathrm{G}$ auf beiden Seiten steht und sich kürzt.
---
Für zwei Kondensatoren ist $U_1=Q_\mathrm{G}/C_1=U_\mathrm{G}\,C_\mathrm{G}/C_1=U_\mathrm{G}\,C_2/(C_1+C_2)$, weil dann $C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2}$ ist.
:::
:::karte begriff Insel
Was nennt man in einer Schaltung aus Kondensatoren eine Insel, und was folgt daraus für ihre Ladung?
---
Ein Leiterstück, zu dem nur Isolatoren führen, etwa die Verbindung zweier Kondensatoren in Reihe. Ladung kann weder hinein noch heraus; war die Insel ungeladen, bleibt ihre Summe null.
--- falsch
Ein Leiterstück ohne Verbindung zur Quelle. Über die angeschlossenen Kondensatoren fließt so lange Ladung zu oder ab, bis es auf dem Potenzial der Masse liegt und damit wieder neutral ist.
--- falsch
Ein Kondensator, der von allen anderen Bauteilen getrennt ist. Seine Ladung fließt nach kurzer Zeit ab, weil ihn keine Quelle mehr festhält.
--- falsch
Ein Leiterstück, zu dem nur Isolatoren führen. Es nimmt beim Laden die Ladung $+Q$ auf, die die Batterie über die Kondensatoren hineinschiebt, und behält sie danach.
:::
:::karte zusammenhang Gleiche Ladung in Reihe
Warum tragen in Reihe geschaltete, anfangs ungeladene Kondensatoren alle dieselbe Ladung?
---
Weil ihre Verbindung eine Insel ist, deren Summe null bleibt: Zieht die obere Platte $+Q$ auf der Insel $-Q$ an, muss das Gegenstück $+Q$ auf der nächsten Platte sitzen. Die Kette wirkt wie ein vergrößerter Abstand.
--- falsch
Weil derselbe Strom durch alle Dielektrika hindurchfließt und auf jeder Platte, an der er vorbeikommt, dieselbe Ladung ablädt; die Kette wirkt deshalb wie ein einziger, besonders dicker Kondensator mit großer Fläche.
--- falsch
Weil die Batterie jedem Kondensator dieselbe Ladung zuteilt, unabhängig von seiner Lage in der Kette; das gilt allerdings nur, wenn alle Kondensatoren dieselbe Kapazität haben.
--- falsch
Weil sich die Ladung nach dem Laden über die Verbindungsdrähte gleichmäßig auf alle Platten verteilt, bis jede denselben Anteil trägt; die Kette wirkt wie eine vergrößerte Platte.
:::
:::karte zusammenhang Gleiche Spannung parallel
Warum liegt an parallel geschalteten Kondensatoren dieselbe Spannung, und wie wirkt die Schaltung?
---
Alle oberen Platten hängen an einem Draht, alle unteren an einem anderen, und ein Draht ohne Strom hat überall dasselbe Potenzial. Die Schaltung wirkt wie eine vergrößerte Platte.
--- falsch
Weil jeder Kondensator so lange Ladung aufnimmt, bis er dieselbe Ladung trägt wie die anderen, gleich welche Kapazität er hat; die Schaltung wirkt deshalb wie ein vergrößerter Abstand.
--- falsch
Weil die Batterie ihre Spannung gleichmäßig aufteilt und jedem Kondensator denselben Anteil gibt; die Schaltung wirkt wie eine verkleinerte Platte.
--- falsch
Weil die Kondensatoren über ihre Dielektrika miteinander verbunden sind und sich so angleichen; die Schaltung wirkt wie ein dickeres Dielektrikum.
:::
:::karte zusammenhang Umgekehrt wie bei Widerständen
Warum sind die Formeln für Kondensatoren in Reihe und parallel genau umgekehrt wie bei Widerständen?
---
Am Widerstand gilt $u=R\,i$, am Kondensator $u=\frac1C\,q$. In Reihe addieren sich die Spannungen bei gleicher Ladung, also addiert sich $1/C$: $1/C$ spielt beim Kondensator die Rolle von $R$.
--- falsch
Weil am Kondensator die Ladung statt der Spannung die treibende Größe ist; in Reihe addieren sich deshalb die Ladungen, parallel dagegen die Spannungen der einzelnen Kondensatoren.
--- falsch
Weil die Kapazität mit dem Plattenabstand wächst: In Reihe vergrößert sich der wirksame Abstand und damit die Kapazität, parallel bleibt der Abstand gleich und die Kapazität auch.
--- falsch
Weil in einer Reihe von Kondensatoren nicht überall derselbe Strom fließt; jeder Kondensator nimmt nur einen Teil des Stroms auf und gibt den Rest an den nächsten weiter.
:::
:::karte zusammenhang Grenzfälle der Reihenschaltung
Was geschieht mit der Gesamtkapazität zweier Kondensatoren in Reihe, wenn $C_2$ sehr groß oder sehr klein wird?
---
Für $C_2\to\infty$ geht $C_\mathrm{G}\to C_1$, der riesige Kondensator verhält sich wie ein Draht. Für $C_2\to0$ geht $C_\mathrm{G}\to0$, die Lücke unterbricht.
--- falsch
Für $C_2\to\infty$ geht $C_\mathrm{G}\to\infty$, weil sich die Kapazitäten addieren. Für $C_2\to0$ geht $C_\mathrm{G}\to C_1$, der kleine Kondensator verschwindet.
--- falsch
Für $C_2\to\infty$ geht $C_\mathrm{G}\to0$, der riesige Kondensator sperrt alles. Für $C_2\to0$ geht $C_\mathrm{G}\to C_1$, die Lücke wirkt wie ein Draht.
--- falsch
In beiden Fällen geht $C_\mathrm{G}\to C_1$, weil in Reihe stets der erste Kondensator die Kapazität bestimmt und der zweite nur die Spannung teilt.
:::
::::
