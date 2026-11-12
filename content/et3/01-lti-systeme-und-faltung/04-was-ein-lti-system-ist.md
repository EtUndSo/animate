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

::::lernkarten
:::karte begriff System
Was tut ein System im Sinn der Systemtheorie, und wie schreibt man das?
---
Es ordnet einem Eingangssignal $s(t)$ ein Ausgangssignal $g(t)$ zu, geschrieben $g(t)=\operatorname{Tr}\{s(t)\}$. Ein Beispiel ist das RC-Glied, das aus $u_1$ die Spannung $u_2$ macht.
--- falsch
Es ordnet jedem Zeitpunkt $t$ einen Signalwert zu, geschrieben $g(t)=\operatorname{Tr}\{t\}$. Ein Beispiel ist eine Quelle, die von sich aus eine Sinusspannung abgibt.
--- falsch
Es ordnet einem Ausgangssignal $g(t)$ das Eingangssignal zu, aus dem es entstanden ist, geschrieben $s(t)=\operatorname{Tr}\{g(t)\}$. Ein Beispiel ist ein Messgerät.
--- falsch
Es ordnet einem Eingangssignal $s(t)$ eine einzelne Zahl zu, etwa seinen Höchstwert, geschrieben $g=\operatorname{Tr}\{s(t)\}$. Ein Beispiel ist ein Spitzenwertmesser.
:::
:::karte begriff Transformation
Was unterscheidet eine Transformation wie $\operatorname{Tr}$ von einer Abbildung, die einen Zahlenwert auf einen anderen abbildet?
---
Sie ordnet Funktionen Funktionen zu. Der Ausgang zur Zeit $t$ darf vom ganzen bisherigen Verlauf des Eingangs abhängen; beim RC-Glied hängt $u_2(t)$ davon ab, wie viel Ladung sich bis $t$ angesammelt hat.
--- falsch
Sie ordnet Funktionen Funktionen zu, aber der Ausgang zur Zeit $t$ darf nur vom Eingang zur selben Zeit abhängen; beim RC-Glied ist $u_2(t)$ deshalb zu jeder Zeit ein fester Bruchteil von $u_1(t)$.
--- falsch
Sie bildet ebenfalls einen Zahlenwert auf einen anderen ab, behält dabei aber die Einheit bei; beim RC-Glied wird aus einer Spannung in Volt wieder eine Spannung in Volt.
--- falsch
Sie überführt ein Signal aus dem Zeitbereich in den Frequenzbereich: Aus $s(t)$ wird eine Funktion der Frequenz; beim RC-Glied ist das Ergebnis der Frequenzgang $H(F)$.
:::
:::karte begriff linear
Welche Bedingung muss ein System erfüllen, damit es linear heißt?
---
Für beliebige Konstanten $a_i$ muss der Überlagerungssatz gelten, $\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t)$: Die Antwort auf eine gewichtete Summe ist die gewichtete Summe der Antworten.
--- falsch
Seine Kennlinie muss eine Gerade sein, also $g(t)=m\,s(t)+b$ mit beliebigen Konstanten $m$ und $b$; dann ist die Antwort auf eine gewichtete Summe von Eingängen stets die gewichtete Summe der Antworten.
--- falsch
Der Überlagerungssatz muss nur für positive Konstanten $a_i$ gelten, $\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_ig_i(t)$; negative Gewichte kommen bei physikalischen Signalen gar nicht vor.
--- falsch
Ein verschobener Eingang muss den gleich verschobenen Ausgang ergeben, $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$; dann reagiert das System zu jeder Zeit auf dieselbe Weise und ist linear.
:::
:::karte begriff zeitinvariant
Welche Bedingung muss ein System erfüllen, damit es zeitinvariant heißt?
---
Für jede Verschiebung $t_0$ muss $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$ gelten: Ein verschobener Eingang ergibt den gleich verschobenen Ausgang. Beim RC-Glied liegt das daran, dass sich $R$ und $C$ nicht mit der Zeit ändern.
--- falsch
Für jede Verschiebung $t_0$ muss $\operatorname{Tr}\{s(t-t_0)\}=g(t)$ gelten: Der Ausgang darf nicht davon abhängen, wann der Eingang kommt. Beim RC-Glied liegt das daran, dass der Kondensator jede Ladung speichert.
--- falsch
Sein Ausgang darf sich bei konstantem Eingang zeitlich nicht ändern, er muss also sofort seinen Endwert annehmen. Beim RC-Glied gilt das erst im eingeschwungenen Zustand, vorher ist es zeitvariant.
--- falsch
Es darf keine Zeit zum Antworten brauchen: Der Ausgang zur Zeit $t$ hängt nur vom Eingang zur selben Zeit ab, ohne jede Verzögerung. Ein Laufzeitglied ist deshalb niemals zeitinvariant.
:::
:::karte begriff LTI-System
Was ist ein LTI-System, und wofür steht die Abkürzung?
---
Ein System, das linear und zeitinvariant ist, englisch linear time-invariant. Beispiele sind das RC-Glied und alle Netzwerke aus $R$, $L$ und $C$.
--- falsch
Ein System, das linear und zeitinvariant ist, englisch low time inertia. Gemeint ist, dass es ohne nennenswerte Verzögerung auf den Eingang antwortet.
--- falsch
Ein System, das durch eine lineare Differentialgleichung mit konstanten Koeffizienten beschrieben wird. Ein ideales Laufzeitglied ist deshalb keines.
--- falsch
Ein System, dessen Kennlinie eine Gerade ist, englisch linear transfer interface. Ob es sich mit der Zeit ändert, spielt dafür keine Rolle.
:::
:::karte zusammenhang Linearität und Zeitinvarianz des RC-Glieds
Woran liegt es, dass das RC-Glied linear und zeitinvariant ist?
---
Linear ist es, weil in seiner Differentialgleichung weder Produkte noch Quadrate von $u_1$ und $u_2$ stehen. Zeitinvariant ist es, weil sich $R$ und $C$ nicht mit der Zeit ändern.
--- falsch
Linear ist es, weil sich $R$ und $C$ nicht mit der Zeit ändern. Zeitinvariant ist es, weil in seiner Differentialgleichung weder Produkte noch Quadrate von $u_1$ und $u_2$ stehen.
--- falsch
Linear ist es, weil seine Sprungantwort gleichmäßig ansteigt. Zeitinvariant ist es, weil der Kondensator nach langer Zeit voll ist und sich danach nichts mehr ändert.
--- falsch
Linear ist es, weil die Differentialgleichung nur eine einzige Ableitung enthält. Zeitinvariant ist es, weil die Zeit in der Lösung $1-\mathrm{e}^{-t/RC}$ nur im Exponenten steht.
:::
:::karte zusammenhang LTI-Systeme ohne Differentialgleichung
Wird jedes LTI-System durch eine lineare Differentialgleichung mit konstanten Koeffizienten beschrieben?
---
Nein. Alle Netzwerke aus $R$, $L$ und $C$ werden so beschrieben, aber nicht jedes LTI-System: Ein ideales Laufzeitglied, das sein Eingangssignal nur um eine feste Zeit verzögert, hat keine solche Gleichung.
--- falsch
Ja. Linearität verlangt eine lineare Gleichung und Zeitinvarianz konstante Koeffizienten; ein System ohne eine solche Gleichung kann deshalb gar kein LTI-System sein, auch kein Laufzeitglied.
--- falsch
Nein. Schon Netzwerke aus $R$, $L$ und $C$ haben keine solche Gleichung, sobald mehr als ein Kondensator darin vorkommt; nur ein einzelnes RC-Glied hat eine.
--- falsch
Ja, mit einer Ausnahme: Systeme, deren Bauteile sich mit der Zeit ändern, haben eine Gleichung mit veränderlichen Koeffizienten und sind trotzdem LTI-Systeme.
:::
:::karte zusammenhang Was die beiden Eigenschaften erlauben
Was folgt für ein LTI-System, das auf den Rechteckimpuls $s_0$ mit $g_0$ antwortet, über seine Antwort auf $s(t)=s_0(t)+0{,}5\,s_0(t-2)$?
---
Ohne weitere Rechnung ist der Ausgang $g_0(t)+0{,}5\,g_0(t-2)$: Die Linearität überträgt Summe und Gewicht, die Zeitinvarianz die Verschiebung um 2.
--- falsch
Der Ausgang ist $1{,}5\,g_0(t)$, weil ein LTI-System nur die Summe der Gewichte sieht und die Verschiebung des zweiten Impulses nicht bemerkt.
--- falsch
Man muss die Differentialgleichung neu lösen, weil die Antwort auf eine Summe nicht aus den Einzelantworten folgt, sobald sich diese überlappen.
--- falsch
Der Ausgang ist $g_0(t)+0{,}5\,g_0(t+2)$, weil die Antwort auf den späteren Impuls um 2 nach links rückt, damit sie zum Eingang passt.
:::
:::karte begriff affin
Warum ist das System $g(t)=2s(t)+1$ nicht linear, obwohl seine Kennlinie eine Gerade ist, und wie nennt man es?
---
Ein lineares System muss auf den Eingang null mit null antworten, $\operatorname{Tr}\{0\}=0$; hier ist $\operatorname{Tr}\{0\}=1$. Eine Gerade, die nicht durch den Ursprung geht, heißt affin.
--- falsch
Weil $2s(t)$ mit wachsendem Eingang schneller steigt als die Konstante 1; linear ist es deshalb nur für große Eingänge. Ein solches System heißt affin.
--- falsch
Weil der Faktor 2 die Amplitude verdoppelt; ein lineares System darf die Amplitude eines Signals nicht verändern. Ein System mit einem solchen Faktor heißt affin.
--- falsch
Weil die Konstante 1 einen festen Zeitpunkt auszeichnet; das System ist deshalb nicht zeitinvariant und heißt affin, also zeitlich veränderlich.
:::
:::karte zusammenhang Bauteil, das sich mit der Zeit ändert
Warum ist das System $g(t)=t\,s(t)$ linear, aber nicht zeitinvariant?
---
Der Faktor $t$ lässt Summen und Gewichte durch. Aber $\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$, während $g(t-t_0)=(t-t_0)\,s(t-t_0)$ ist: Der Faktor $t$ wirkt wie ein Bauteil, das sich mit der Zeit ändert.
--- falsch
Der Faktor $t$ lässt Summen und Gewichte durch. Zeitinvariant ist es nicht, weil der Ausgang für $t<0$ das Vorzeichen wechselt; ein zeitinvariantes System darf das Vorzeichen eines Signals nicht ändern.
--- falsch
Linear ist es, weil $t$ nur einmal vorkommt und nicht quadriert wird. Zeitinvariant ist es nicht, weil der Ausgang mit der Zeit immer größer wird und so nie einen Endwert erreicht.
--- falsch
Der Faktor $t$ lässt Summen und Gewichte durch. Zeitinvariant ist es nicht, weil es nicht durch eine Differentialgleichung beschrieben wird; ohne eine solche Gleichung ist kein System zeitinvariant.
:::
::::
