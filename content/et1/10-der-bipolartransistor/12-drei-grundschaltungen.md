---
title: Stufe 10: Drei Grundschaltungen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1201200
summary: Eingang und Ausgang brauchen je zwei Klemmen, der Transistor hat insgesamt drei.
tags: Emitterschaltung, Kollektorschaltung, Emitterfolger, Basisschaltung, Spannungshub, Puffer
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Eingang und Ausgang brauchen je zwei Klemmen, der Transistor hat insgesamt drei. Ein Anschluss wird also für das Signal gemeinsam. Diese Stufe rechnet die drei Möglichkeiten aus.
:::

**Die Idee.** Der gemeinsame Anschluss gibt der Schaltung den Namen (Abb. [12](#abb-12)). In der __Emitterschaltung__ kommt das Signal an die Basis und geht vom Kollektor weg. $u_\mathrm{ein}$ liegt voll an der BE-Strecke und erzeugt $i_\mathrm{c}=S\,u_\mathrm{ein}$. Dieser Strom fließt durch $R_\mathrm{C}$ und zieht das Kollektorpotenzial herab: Der Ausgang ist invertiert. In der __Kollektorschaltung__ kommt das Signal an die Basis und geht vom Emitter weg. Der Emitter folgt der Basis: Stünde er still, änderte sich $U_\mathrm{BE}$, und der entstehende Strom höbe ihn über $R_\mathrm{E}$ sofort nach. Deshalb heißt sie auch __Emitterfolger__. In der __Basisschaltung__ liegt die Basis fest, das Signal kommt an den Emitter. Sinkt der Emitter, steigt $U_\mathrm{BE}$, mehr Strom zieht den Kollektor herab: Ein- und Ausgang bewegen sich gleichsinnig. Der Betrag entspricht der Emitterschaltung.

:::abbildung et1/k10grundschaltungen 12
Oben die drei Grundschaltungen, unten ihre Kennlinien aus dem Rechenmodell mit $U_\mathrm{CC}=12$ V. Emitterschaltung ($R_\mathrm{C}=3$ k$\Omega$): fallend, steil um 0,6 V. Kollektorschaltung ($R_\mathrm{E}=3$ k$\Omega$): Der Ausgang liegt rund 0,6 V unter dem Eingang (grau). Basisschaltung: wie die Emitterschaltung, an der senkrechten Achse gespiegelt, steigend.
:::

:::satz Satz 10.1 (Spannungsverstärkung der Grundschaltungen)
<span class="anker" id="satz-10-1"></span>

Für kleine Signale im aktiven Bereich, $r_\mathrm{CE}$ vernachlässigt, $A=u_\mathrm{aus}/u_\mathrm{ein}$:

<span class="anker" id="gl-10-1"></span>
$$A_\mathrm{Emitter}=-S\,R_\mathrm{C}=-\frac{U_{R_\mathrm{C}}}{U_T},\qquad A_\mathrm{Kollektor}=\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}<1,\qquad A_\mathrm{Basis}=+S\,R_\mathrm{C}. \tag{10.1}$$

Mit Emitterwiderstand ist $A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)\approx-R_\mathrm{C}/R_\mathrm{E}$, mit $r_\mathrm{CE}$ ist $A_\mathrm{Emitter}=-S\,(R_\mathrm{C}\parallel r_\mathrm{CE})$.
:::

⁠**So liest man das:** $U_{R_\mathrm{C}}=I_\mathrm{C}R_\mathrm{C}$ ist die Gleichspannung am Kollektorwiderstand, 6 V im Rechenmodell. **Kurz gesagt:** Die Verstärkung der Emitterschaltung ist die Gleichspannung am Kollektorwiderstand geteilt durch $U_T$. Weder $B$ noch der Transistortyp kommen darin vor. **Gültigkeit:** $|u_\mathrm{be}|\ll U_T$, $R_\mathrm{C}\ll r_\mathrm{CE}$, Ansteuerung durch eine Quelle mit kleinem Innenwiderstand.

:::herleitung Drei Maschen im Kleinsignal
$U_\mathrm{CC}$ ist für das Signal Masse. Emitterschaltung: $u_\mathrm{be}=u_\mathrm{ein}$, $u_\mathrm{aus}=-R_\mathrm{C}i_\mathrm{c}=-R_\mathrm{C}S\,u_\mathrm{ein}$, und mit $S=I_\mathrm{C}/U_T$ folgt $S\,R_\mathrm{C}=I_\mathrm{C}R_\mathrm{C}/U_T$. Mit Emitterwiderstand: $u_\mathrm{ein}=u_\mathrm{be}+R_\mathrm{E}S\,u_\mathrm{be}$, der Großteil von $u_\mathrm{ein}$ liegt an $R_\mathrm{E}$, und der Rest $u_\mathrm{be}=u_\mathrm{ein}/(1+S\,R_\mathrm{E})$ steuert. Kollektorschaltung: $u_\mathrm{aus}=R_\mathrm{E}S\,u_\mathrm{be}$ mit $u_\mathrm{be}=u_\mathrm{ein}-u_\mathrm{aus}$, auflösen. Basisschaltung: Die Basis ruht, also $u_\mathrm{be}=-u_\mathrm{ein}$ und $u_\mathrm{aus}=-R_\mathrm{C}S\,u_\mathrm{be}=+S\,R_\mathrm{C}u_\mathrm{ein}$.
:::

::::beispiel
Emitterschaltung im Punkt A: $A=-6\,\mathrm{V}/26\,\mathrm{mV}=-231$, mit $r_\mathrm{CE}$ genauer $-215$. Aus 1 mV am Eingang werden 0,23 V am Ausgang. Der Punkt in der Mitte erlaubt einen __Spannungshub__, eine Ausgangsamplitude, von fast 6 V, doch bei 25 mV am Eingang ist die Tangente längst ungültig. Für die Kleinsignalgrenze 2,6 mV sind es 0,6 V. Für einen Verstärker muss der Arbeitspunkt im Gebiet nahezu konstanter Steigung liegen, und der Hub soll möglichst groß sein. Die gegengekoppelte Fassung hat $A=-3\,\text{k}\Omega/(1\,\text{k}\Omega+12{,}9\,\Omega)=-2{,}96$: nur 1,3 % von $u_\mathrm{ein}$ liegen an der BE-Strecke, dafür ist die Verstärkung fast nur durch zwei Widerstände bestimmt. Emitterfolger mit $R_\mathrm{E}=3$ k$\Omega$ bei 2 mA: $S\,R_\mathrm{E}=231$, $A=0{,}996$. Seine Stärke ist nicht die Spannung, sondern der Strom: Die Stromverstärkung ist $1+B=201$. Er dient als __Puffer__: Er belastet die Quelle kaum und treibt die Last niederohmig.
::::

⁠**Grenzfälle:** $R_\mathrm{E}\to0$ in der gegengekoppelten Form ergibt $-S\,R_\mathrm{C}$. $R_\mathrm{E}\to\infty$ beim Emitterfolger ergibt $A\to1$.

| Schaltung | $A$ | Eingangswiderstand | Ausgangswiderstand | Einsatz |
|---|---|---|---|---|
| Emitter | $-231$ | $r_\mathrm{BE}=2{,}6$ k$\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Spannung verstärken |
| Kollektor | $0{,}996$ | $r_\mathrm{BE}+(1+B)R_\mathrm{E}=606$ k$\Omega$ | $1/S=13\,\Omega$ | Puffer, Stromverstärkung |
| Basis | $+231$ | $1/S=13\,\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Niederohmige Quelle verstärken |

:::frage Eine reale Emitterschaltung hat doch eine flachere Kennlinie als die Basisschaltung. Wieso soll der Betrag gleich sein?
Gleich ist er bei direkter Ansteuerung, gleichem $R_\mathrm{C}$ und gleichem Strom. Liegt vor der Basis ein Vorwiderstand oder eine Quelle mit Innenwiderstand, bildet er mit $r_\mathrm{BE}$ einen Spannungsteiler, und nur ein Teil von $u_\mathrm{ein}$ erreicht die BE-Strecke. Dann ist die Kennlinie der Emitterschaltung flacher. In der Basisschaltung entfällt dieser Teiler, weil die niederohmige Quelle am Emitter liegt.
:::

:::ltspice Die Übertragungskennlinie der Emitterschaltung
⁠**Zeichnen:** `voltage` `VCC` mit 12 an `res` 3k zum Kollektor (Netz `c`), `npn` mit Modell `T`, Emitter an Masse, an der Basis `voltage` `VE`.

⁠**Direktiven:** das Modell aus Stufe [3](eine-flache-viele-kennlinien.html#stufe-3), `.dc VE 0.5 0.7 0.1m`, `.meas dc a1 FIND V(c) AT=0.5995`, `.meas dc a2 FIND V(c) AT=0.6005`, `.meas dc au PARAM (a2-a1)/1m`.

⁠**Was du siehst:** $U_\mathrm{aus}$ fällt von 12 V bis nahe 0, in einem Fenster von rund 60 mV. `au` ergibt $-213$, gegen $-215$ in der Rechnung. LTspice rechnet mit $U_T=25{,}86$ mV und steht bei $U_\mathrm{BE}=0{,}6$ V auf 1,98 mA. Für Aufgabe [12](#aufg-12) setze `VCC` auf 9, den Widerstand auf 4.7k und die `AT`-Werte auf 0.582 und 0.583: `au` ergibt bei 0,98 mA dann $-169$.
:::

:::aufgabe Aufgabe 12 ★★★ Verstärker und Folger
<span class="anker" id="aufg-12"></span>

T arbeitet bei $I_\mathrm{C}=1$ mA und $U_\mathrm{CE}=4{,}3$ V mit $U_\mathrm{CC}=9$ V, $R_\mathrm{C}=4{,}7$ k$\Omega$. (a) Sage vorher, wie groß $A$ der Emitterschaltung ist, nur aus der Spannung an $R_\mathrm{C}$. (b) Wie groß ist die Ausgangsamplitude bei $\hat u_\mathrm{ein}=2$ mV? Wie ändert $r_\mathrm{CE}$ das Ergebnis? (c) Mit einem Emitterwiderstand 470 $\Omega$: Wie groß ist $A$? (d) Als Emitterfolger mit $R_\mathrm{E}=4{,}7$ k$\Omega$: Wie groß ist $A$? Ist der Ausgang invertiert?

:::loesung
(a) $U_{R_\mathrm{C}}=4{,}7$ V, also $A=-4{,}7\,\mathrm{V}/26\,\mathrm{mV}=-181$.

(b) $\hat u_\mathrm{aus}=0{,}36$ V. Mit $r_\mathrm{CE}=78$ k$\Omega$ ist $A=-S(R_\mathrm{C}\parallel r_\mathrm{CE})=-171$, nur 6 % weniger.

(c) $A=-4{,}7\,\text{k}\Omega/(470\,\Omega+26\,\Omega)=-9{,}5$. Die Näherung $-R_\mathrm{C}/R_\mathrm{E}$ ergibt $-10$.

(d) $S\,R_\mathrm{E}=181$, $A=0{,}994$. Der Ausgang ist nicht invertiert, der Emitter folgt der Basis gleichphasig.
:::
:::
