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
