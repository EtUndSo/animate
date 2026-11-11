---
title: Stufe 3: Was ein LTI-System ist
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3210400
summary: Das RC-Glied hat zwei Eigenschaften, auf denen alles Weitere beruht: Es ist linear und zeitinvariant.
tags: System, Transformation, linear, zeitinvariant, LTI-System
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Das RC-Glied hat zwei Eigenschaften, auf denen alles Weitere beruht: Es ist linear und zeitinvariant. Diese Stufe definiert beide und zeigt, was sie erlauben.
:::

Ein __System__ ordnet einem Eingangssignal ein Ausgangssignal zu:

$$g(t)=\operatorname{Tr}\{s(t)\}.$$

Eine solche Zuordnung von Funktionen zu Funktionen heißt __Transformation__. Sie bildet nicht einen Zahlenwert auf einen anderen ab: Der Ausgang zur Zeit $t$ darf vom ganzen bisherigen Verlauf des Eingangs abhängen. Beim RC-Glied hängt $u_2(t)$ davon ab, wie viel Ladung sich bis $t$ angesammelt hat.

:::definition Definition 3.1 (LTI-System)
<span class="anker" id="satz-3-1"></span>

Ein System heißt

<ul>

<li>

__linear__, wenn für beliebige Konstanten $a_i$ der Überlagerungssatz gilt:

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t); \tag{3.1}$$

</li>

<li>

__zeitinvariant__, wenn für jede Verschiebung $t_0$ gilt:

<span class="anker" id="gl-3-2"></span>
$$\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0). \tag{3.2}$$

</li>

</ul>

Ein lineares, zeitinvariantes System heißt kurz __LTI-System__ (englisch linear time-invariant).
:::

Beim RC-Glied kommt die Linearität daher, dass in der Differentialgleichung [(2.1)](ein-erstes-system-das-rc-glied.html#gl-2-1) weder Produkte noch Quadrate von $u_1$ und $u_2$ stehen. Die Zeitinvarianz kommt daher, dass sich $R$ und $C$ nicht mit der Zeit ändern. Alle Netzwerke aus $R$, $L$ und $C$ werden durch lineare Differentialgleichungen mit konstanten Koeffizienten beschrieben. Das gilt aber nicht für jedes LTI-System: Ein ideales Laufzeitglied etwa, das sein Eingangssignal nur um eine feste Zeit verzögert, hat keine solche Gleichung.

**Was die beiden Eigenschaften erlauben.** Kennt man die Antwort $g_0$ auf einen Rechteckimpuls $s_0$, kennt man ohne weitere Rechnung die Antwort auf jede Summe verschobener und skalierter Rechteckimpulse. Abbildung [4](#abb-4) zeigt das für $s(t)=s_0(t)+0{,}5\,s_0(t-2)$: Der Ausgang ist $g_0(t)+0{,}5\,g_0(t-2)$.

:::abbildung et3/k1doppel 4
Links: Rechteck $s_0$ (Höhe 1 V, Dauer 1 s) und die Antwort $g_0$ des RC-Glieds. Rechts: Doppelimpuls. Die Antwort (rot) ist die Summe aus $g_0(t)$ und der verschobenen, halbierten Kopie $0{,}5\,g_0(t-2)$ (gestrichelt).
:::

:::frage Ist $g(t)=2s(t)+1$ linear? Die Kennlinie ist doch eine Gerade.
Nein. Für ein lineares System muss der Eingang null den Ausgang null ergeben: Setzt man in [(3.1)](#gl-3-1) alle $a_i=0$, folgt $\operatorname{Tr}\{0\}=0$. Hier ist $\operatorname{Tr}\{0\}=1$. Auch der Überlagerungssatz scheitert: Zwei Eingänge einzeln ergeben zusammen $2s_1+2s_2+2$, gemeinsam aber $2s_1+2s_2+1$. Eine Gerade, die nicht durch den Ursprung geht, heißt *affin*, nicht linear.
:::

:::ltspice Überlagerung prüfen: zwei Rechtecke
⁠**Zeichnen:** das RC-Glied aus Stufe [2](ein-erstes-system-das-rc-glied.html#stufe-2), aber mit zwei Quellen `voltage` in Reihe: `V1` mit dem Minuspol an Masse und dem Pluspol am Netz `a`, Wert `PULSE(0 {a1} 0 1u 1u 1)`, darauf `V2` von `a` nach `in`, Wert `PULSE(0 {a2} 2 1u 1u 1)`. In Reihe addieren sich die Spannungen, am RC-Glied liegt also $a_1s_0(t)+a_2s_0(t-2)$.

⁠**Direktiven:** `.param a1=1 a2=0.5`, `.step param a1 list 0 1`, `.step param a2 list 0 0.5`, `.tran 0 6 0 1m`. LTspice rechnet alle vier Kombinationen und zeichnet sie übereinander.

⁠**Was du siehst:** die Kurven $0$, $g_0(t)$, $0{,}5\,g_0(t-2)$ und ihre Summe wie in Abb. [4](#abb-4). Bei $t=2{,}5$ s ist $0{,}141+0{,}197=0{,}338$. Die Summe der Eingänge gibt die Summe der Antworten (Linearität), und die um 2 s verschobene Quelle gibt die um 2 s verschobene Kurve (Zeitinvarianz).
:::

:::aufgabe Aufgabe 3 ★ LTI oder nicht?
<span class="anker" id="aufg-3"></span>

Prüfe für jedes System Linearität und Zeitinvarianz: (a) $g(t)=3\,s(t-2)$, (b) $g(t)=s(t)^2$, (c) $g(t)=s(t)+1$, (d) $g(t)=t\,s(t)$, (e) $g(t)=s(2t)$, (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$.

:::loesung
(a) Linear und zeitinvariant (Verstärkung 3, Verzögerung 2): LTI. (b) Nicht linear: $\operatorname{Tr}\{2s\}=4s^2\neq2s^2$. Zeitinvariant. (c) Nicht linear (affin, $\operatorname{Tr}\{0\}=1$). Zeitinvariant. (d) Linear. Nicht zeitinvariant: $\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$, aber $g(t-t_0)=(t-t_0)\,s(t-t_0)$. Der Faktor $t$ ist ein Bauteil, das sich mit der Zeit ändert. (e) Linear. Nicht zeitinvariant: $\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$, aber $g(t-t_0)=s(2t-2t_0)$. Wer die Zeit staucht, staucht auch jede Verschiebung. (f) LTI. Linear, weil das Integral linear ist. Zeitinvariant: $\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$. Seine Impulsantwort ist $\varepsilon(t)$ (Stufe [8](integrieren-und-differenzieren.html#stufe-8)).
:::
:::

::::kurzfassung
Linearität und Zeitinvarianz sind die beiden Eigenschaften, auf denen alles Weitere beruht. Mit ihnen folgt aus der Antwort auf ein Signal die Antwort auf jede Summe verschobener und skalierter Kopien davon.

Ein __System__ ordnet einem Eingangssignal ein Ausgangssignal zu, $g(t)=\operatorname{Tr}\{s(t)\}$. Eine solche Zuordnung von Funktionen zu Funktionen heißt __Transformation__; der Ausgang zur Zeit $t$ darf vom ganzen bisherigen Verlauf des Eingangs abhängen. Ein System heißt __linear__, wenn für beliebige Konstanten $a_i$ der Überlagerungssatz gilt:

$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t).$$

Es heißt __zeitinvariant__, wenn für jede Verschiebung $t_0$ gilt: $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$. Ein System mit beiden Eigenschaften heißt __LTI-System__, nach dem englischen linear time-invariant.

Der Grund für die Wirkung: Die Zeitinvarianz liefert zu jeder verschobenen Kopie die verschobene Antwort, die Linearität überträgt Faktoren und Summe. Beim RC-Glied stehen in der Differentialgleichung weder Produkte noch Quadrate von $u_1$ und $u_2$, und $R$ und $C$ ändern sich nicht mit der Zeit. Netzwerke aus $R$, $L$ und $C$ werden durch lineare Differentialgleichungen mit konstanten Koeffizienten beschrieben. Nicht jedes LTI-System hat aber eine solche Gleichung, etwa ein ideales Laufzeitglied, das sein Eingangssignal nur um eine feste Zeit verzögert.

Falle: $g(t)=2s(t)+1$ ist nicht linear, obwohl die Kennlinie eine Gerade ist. Mit allen $a_i=0$ verlangt der Überlagerungssatz $\operatorname{Tr}\{0\}=0$, hier ist aber $\operatorname{Tr}\{0\}=1$. Eine Gerade, die nicht durch den Ursprung geht, heißt __affin__.
::::

::::formelsammlung
**System (Transformation)**

$$g(t)=\operatorname{Tr}\{s(t)\}$$

Ordnet dem Eingangssignal $s(t)$ das Ausgangssignal $g(t)$ zu; der Ausgang zur Zeit $t$ darf vom ganzen bisherigen Verlauf des Eingangs abhängen.

**Linearität (Überlagerungssatz)**

$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t)$$

Für beliebige Konstanten $a_i$; $g_i(t)$ Antwort auf $s_i(t)$.

**Nullsignal bei linearen Systemen**

$$\operatorname{Tr}\{0\}=0$$

Folgt aus dem Überlagerungssatz mit allen $a_i=0$. Deshalb ist $g(t)=2s(t)+1$ nicht linear, sondern affin.

**Zeitinvarianz**

$$\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$$

Für jede Verschiebung $t_0$. Linear und zeitinvariant zusammen: LTI-System.
::::
