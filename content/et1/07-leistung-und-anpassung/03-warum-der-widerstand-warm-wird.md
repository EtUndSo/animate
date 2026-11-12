---
title: Stufe 2: Warum der Widerstand warm wird
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Leistung, Anpassung und Wirkungsgrad
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Kapitel 7: Leistung, Anpassung und Wirkungsgrad
order: 1170300
summary: Im Widerstand verlässt die Energie den Stromkreis.
tags: Nennbelastbarkeit, Hyperbel
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Im Widerstand verlässt die Energie den Stromkreis. Diese Stufe zeigt den Mechanismus und die Grenze, die daraus folgt.
:::

**Die Idee.** Liegt an einem Widerstand eine Spannung, herrscht in ihm ein Feld. Es beschleunigt jedes freie Elektron. Nach der Flugzeit $T$ stößt das Elektron und verliert die gerichtete Geschwindigkeit wieder ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Dabei geht seine Bewegungsenergie an das Kristallgitter, die Atome schwingen stärker, und diese Schwingung ist Wärme (Abb. [2](#abb-2)). Das Elektron ist nur der Überbringer: Hinter dem Widerstand hat es dieselbe Drift wie davor, denn Strom und Querschnitt sind gleich. Es hat Potenzial verloren, ohne schneller zu werden. Also steckt die ganze Energie im Gitter. Die Drift selbst fällt nicht ins Gewicht: Bei 0,44 µ m/s ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) trägt ein Elektron $8{,}8\cdot10^{-44}$ J, an 9 V gibt es $1{,}44\cdot10^{-18}$ J ab, das $1{,}6\cdot10^{25}$-Fache.

:::abbildung et1/k7stoss 2
Stoßmodell für ein Elektron. Im Flug wächst die Arbeit des Felds (blau) und steckt als Bewegungsenergie im Elektron. Beim Stoß springt die Wärme im Gitter um $W_1$ (rot). Nach jedem Stoß sind beide Kurven gleich hoch: Alles geht ans Gitter.
:::

:::satz Satz 2.1 (Stromwärme und Belastbarkeit)
<span class="anker" id="satz-2-1"></span>

In einem Widerstand wird die gesamte elektrische Leistung zu Wärme:

<span class="anker" id="gl-2-1"></span>
$$P=U\,I=R\,I^2=\frac{U^2}{R}. \tag{2.1}$$

Ein Bauteil verträgt das nur bis zu seiner __Nennbelastbarkeit__ $P_\mathrm{max}$:

<span class="anker" id="gl-2-2"></span>
$$P\le P_\mathrm{max}. \tag{2.2}$$
:::

⁠**So liest man das:** Ein kleiner Schichtwiderstand hat $P_\mathrm{max}=250$ mW, ein Heizlüfter wandelt 2 kW. Quadratisch ist die Formel, weil der Strom zweimal zählt: Doppelter Strom heißt doppelt so viele Coulomb je Sekunde, und wegen $U=R\,I$ gibt jedes doppelt so viel ab. Bei gleichem Strom (Reihe) wächst die Wärme mit $R$, bei gleicher Spannung (parallel) fällt sie mit $R$. **Gültigkeit:** $P=U\,I$ gilt immer, die beiden anderen Formen nur für den ohmschen Widerstand ($R$ unabhängig vom Strom), und $U$ und $I$ müssen zu diesem Widerstand gehören.

:::herleitung Von den Stößen zu $U^2/R$
Im Modell aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) wird ein Elektron mit $a=e\,E/m_\mathrm e$ beschleunigt und erreicht $v_\mathrm{max}=a\,T$ auf der Strecke $s=\frac12a\,T^2$. Das Feld verrichtet die Arbeit $e\,E\,s=m_\mathrm e\,a\,s=\frac12m_\mathrm e(a\,T)^2=W_1$, genau die Bewegungsenergie beim Stoß. Im Volumen $A\,L$ sitzen $n\,A\,L$ freie Elektronen, jedes stößt $1/T$-mal je Sekunde:

$$P=n\,A\,L\,\frac{W_1}{T}=n\,A\,L\,\frac{e^2E^2\,T}{2\,m_\mathrm e}=\sigma\,E^2\,A\,L.$$

Dabei ist $\sigma=n\,e\,\mu$ und $\mu=e\,T/(2\,m_\mathrm e)$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Mit $U=E\,L$ und $R=L/(\sigma A)$ wird daraus $P=U^2/R$.
:::

**Belastbarkeit.** Die Temperatur steigt, bis das Bauteil je Sekunde so viel Wärme an die Umgebung abgibt, wie im Inneren entsteht. Mehr Leistung heißt also höhere Temperatur, und zu hohe Temperatur zerstört es. Im Diagramm aus Abb. [3](#abb-3) ist die Grenze die __Hyperbel__ $I=P_\mathrm{max}/U$, jeder Widerstand eine Gerade durch den Ursprung. Ihr Schnittpunkt liegt bei $U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$ und $I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$.

:::abbildung et1/k7grenze 3
Grenze eines Widerstands mit 250 mW. Jeder Widerstandswert darf nur bis zur Hyperbel betrieben werden: 25 $\Omega$ bis 100 mA, 100 $\Omega$ bis 50 mA, 400 $\Omega$ bis 25 mA.
:::

::::beispiel
Mit 100 $\Omega$ und 250 mW sind $U_\mathrm{max}=5$ V und $I_\mathrm{max}=50$ mA zulässig. An idealen 9 V entstünden 810 mW, das 3,24-Fache. Nötig wäre $R\ge(9\,\mathrm{V})^2/250\,\mathrm{mW}=324\,\Omega$.
::::

⁠**Grenzfälle:** $R\to\infty$ ergibt $P\to0$. $R\to0$ ergibt an fester Spannung $P\to\infty$. Das verhindert nur der Innenwiderstand der Quelle (Stufe [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5)).

:::frage Heizdraht und Zuleitung führen denselben Strom. Warum glüht nur der Heizdraht?
Bei gleichem Strom ist die Wärme proportional zu $R$. Eine Zuleitung mit 10 m$\Omega$ setzt bei 0,5 A nur 2,5 mW um, die Last mit 16 $\Omega$ dagegen 4 W, das 1600-Fache. In Haartrockner und Lötkolben ist die Wärme der Zweck, in der Leitung ist sie Verlust (Stufe [4](leitungsverluste.html#stufe-4)).
:::

:::aufgabe Aufgabe 2 ★★ Welcher wird heißer?
<span class="anker" id="aufg-2"></span>

Zwei Widerstände mit 100 $\Omega$ und 300 $\Omega$, beide für 250 mW ausgelegt, liegen an 12 V. Sage zuerst voraus, welcher jeweils heißer wird. (a) Sie liegen in Reihe. (b) Sie liegen parallel. Berechne alle Leistungen. (c) Wo wird die Nennbelastbarkeit überschritten?

:::loesung
(a) Reihe: $I=12\,\mathrm{V}/400\,\Omega=30$ mA, $P=R\,I^2$ ergibt 90 mW und 270 mW. Der größere Widerstand wird heißer: gleich viele Coulomb, jedes gibt dort dreimal so viel ab. (b) Parallel: $P=U^2/R$ ergibt 1,44 W und 0,48 W. Der kleinere wird heißer: gleiche Energie je Coulomb, aber dreimal so viele Coulomb. (c) In Reihe ist der 300-$\Omega$-Widerstand mit 270 mW überlastet, parallel sind es beide.
:::
:::

::::formelsammlung
**Stromwärme**

$$P=U\,I=R\,I^2=\frac{U^2}{R}$$

Im Widerstand wird die gesamte elektrische Leistung zu Wärme. $P=U\,I$ gilt immer, die beiden anderen Formen nur für den ohmschen Widerstand ($R$ unabhängig vom Strom); $U$ und $I$ müssen zu diesem Widerstand gehören. Bei gleichem Strom (Reihe) wächst die Wärme mit $R$, bei gleicher Spannung (parallel) fällt sie mit $R$.

**Nennbelastbarkeit**

$$P\le P_\mathrm{max}$$

$P_\mathrm{max}$ ist die Leistung, die das Bauteil höchstens verträgt; ein kleiner Schichtwiderstand hat $P_\mathrm{max}=250$ mW.

**Belastbarkeitsgrenze**

$$I=P_\mathrm{max}/U,\qquad U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R},\qquad I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$$

Im Strom-Spannungs-Diagramm ist die Grenze die Hyperbel $I=P_\mathrm{max}/U$, jeder Widerstand eine Gerade durch den Ursprung. $U_\mathrm{max}$ und $I_\mathrm{max}$ sind ihr Schnittpunkt.

**Stromwärme im Stoßmodell**

$$P=n\,A\,L\,\frac{W_1}{T}=n\,A\,L\,\frac{e^2E^2\,T}{2\,m_\mathrm e}=\sigma\,E^2\,A\,L$$

$n\,A\,L$ freie Elektronen im Volumen $A\,L$, jedes stößt $1/T$-mal je Sekunde ($T$ Flugzeit). $W_1=\frac12m_\mathrm e(a\,T)^2$ ist die Bewegungsenergie, die ein Elektron je Stoß ans Gitter gibt, mit $a=e\,E/m_\mathrm e$. Dabei sind $\sigma=n\,e\,\mu$ und $\mu=e\,T/(2\,m_\mathrm e)$. Mit $U=E\,L$ und $R=L/(\sigma A)$ folgt $P=U^2/R$.
::::

::::lernkarten
:::karte begriff Stromwärme
Was bezeichnet man als Stromwärme in einem Widerstand, und wie groß ist sie?
---
Die Wärme, zu der in einem Widerstand die gesamte elektrische Leistung wird, weil die Elektronen ihre Energie bei Stößen ans Gitter abgeben: $P=U\,I=R\,I^2=\frac{U^2}{R}$.
--- falsch
Den Teil der elektrischen Leistung, der im Widerstand zu Wärme wird; der Rest bleibt als Bewegungsenergie in den schnelleren Elektronen hinter dem Widerstand. Er ist $P=R\,I$.
--- falsch
Die Wärme, die beim Einschalten eines Widerstands einmalig entsteht, bis der Strom seinen Endwert erreicht hat. Danach fließt der Strom verlustfrei, und es gilt $P=0$.
--- falsch
Die Wärme, die in den Zuleitungen eines Widerstands entsteht. Im Widerstand selbst bleibt die Energie erhalten, weil der Strom hinter ihm genauso groß ist wie davor.
:::
:::karte begriff Nennbelastbarkeit
Was gibt die Nennbelastbarkeit eines Widerstands an, und welche Bedingung muss im Betrieb gelten?
---
Die größte Leistung $P_\mathrm{max}$, die das Bauteil als Wärme verträgt; darüber wird es zu heiß und zerstört. Im Betrieb muss $P\le P_\mathrm{max}$ gelten, bei kleinen Schichtwiderständen sind es 250 mW.
--- falsch
Die größte Spannung $U_\mathrm{max}$, die man an das Bauteil legen darf, gleich welchen Widerstandswert es hat. Im Betrieb muss $U\le U_\mathrm{max}$ gelten, bei kleinen Schichtwiderständen sind es 250 mV.
--- falsch
Den größten Strom, den das Bauteil führen darf; er ist für alle Widerstandswerte einer Bauform gleich. Im Betrieb muss $I\le I_\mathrm{max}$ gelten, bei kleinen Schichtwiderständen sind es 250 mA.
--- falsch
Die Leistung, die das Bauteil im Betrieb mindestens umsetzen muss, damit es seinen Widerstandswert erreicht. Im Betrieb muss $P\ge P_\mathrm{max}$ gelten, bei kleinen Schichtwiderständen sind es 250 mW.
:::
:::karte formel Gültigkeit der drei Formen
Welche der drei Formen $P=U\,I$, $P=R\,I^2$ und $P=U^2/R$ für die Leistung an einem Widerstand gilt immer, und was setzen die anderen voraus?
---
$P=U\,I$ gilt immer. $P=R\,I^2$ und $P=U^2/R$ gelten nur für den ohmschen Widerstand, bei dem $R$ nicht vom Strom abhängt, und $U$ und $I$ müssen zu diesem Widerstand gehören.
--- falsch
Alle drei gelten immer, auch wenn $R$ vom Strom abhängt. Man darf für $U$ jede Spannung der Schaltung einsetzen, weil der Strom in der ganzen Schaltung derselbe ist.
--- falsch
$P=R\,I^2$ gilt immer, weil die Wärme nur vom Strom abhängt. $P=U\,I$ und $P=U^2/R$ gelten nur, wenn $U$ die Quellenspannung der ganzen Schaltung ist.
--- falsch
$P=U^2/R$ gilt immer. $P=U\,I$ und $P=R\,I^2$ gelten nur für den ohmschen Widerstand, und für $I$ muss man den Gesamtstrom der Schaltung einsetzen.
:::
:::karte zusammenhang Stoßmechanismus
Warum wird die elektrische Leistung in einem Widerstand vollständig zu Wärme?
---
Das Feld beschleunigt jedes freie Elektron. Beim Stoß gibt das Elektron seine Bewegungsenergie an das Kristallgitter ab, die Atome schwingen stärker, und diese Schwingung ist Wärme.
--- falsch
Die Elektronen reiben sich an der Oberfläche des Drahts. Je schneller sie im Mittel driften, desto stärker die Reibung, und die Reibungswärme heizt den Querschnitt.
--- falsch
Die Elektronen werden im Widerstand dauerhaft schneller und geben die zusätzliche Bewegungsenergie erst hinter ihm als Wärme ab, wenn sie in den gut leitenden Draht eintreten.
--- falsch
Ein Teil der Elektronen bleibt im Widerstand hängen und wird dort vom Gitter eingefangen. Die Energie, die sie dabei abgeben, erscheint als Wärme.
:::
:::karte zusammenhang Elektron als Überbringer
Warum steckt die im Widerstand umgesetzte Energie ganz im Gitter und nicht in schnelleren Elektronen hinter dem Widerstand?
---
Hinter dem Widerstand haben die Elektronen dieselbe Drift wie davor, denn Strom und Querschnitt sind gleich. Sie haben Potenzial verloren, ohne schneller zu werden; die Energie steckt also im Gitter.
--- falsch
Die Elektronen sind hinter dem Widerstand zwar schneller, geben ihre Bewegungsenergie aber sofort an den nächsten Draht ab. Am Ende landet so auch dieser Teil als Wärme im Gitter der Zuleitung.
--- falsch
Die Elektronen werden im Widerstand langsamer und geben die Differenz ihrer Bewegungsenergie ans Gitter ab. Hinter dem Widerstand fließt deshalb ein kleinerer Strom als davor.
--- falsch
Die Drift der Elektronen trägt den größten Teil der Energie und geht beim Stoß vollständig verloren. Hinter dem Widerstand beginnen die Elektronen deshalb wieder aus der Ruhe.
:::
:::karte zusammenhang Quadratische Abhängigkeit vom Strom
Warum wächst die Wärme in einem ohmschen Widerstand mit dem Quadrat des Stroms und nicht linear?
---
Weil der Strom zweimal zählt: Doppelter Strom heißt doppelt so viele Coulomb je Sekunde, und wegen $U=R\,I$ gibt jedes Coulomb doppelt so viel Energie ab.
--- falsch
Weil bei doppeltem Strom die Elektronen doppelt so schnell driften und ihre Bewegungsenergie mit dem Quadrat der Geschwindigkeit wächst. Diese Energie heizt das Gitter.
--- falsch
Weil sich bei doppeltem Strom auch der Widerstand verdoppelt, da das Gitter wärmer wird. Doppelter Widerstand mal doppelter Strom ergibt die vierfache Wärme.
--- falsch
Weil der Strom einmal durch den Hinleiter und einmal durch den Rückleiter fließt. Jede der beiden Strecken bringt einen Faktor $I$, zusammen also $I^2$.
:::
:::karte zusammenhang Reihe und parallel
Welcher von zwei verschiedenen Widerständen wird heißer, wenn sie in Reihe liegen, und welcher, wenn sie parallel an derselben Spannung liegen?
---
In Reihe der größere: Bei gleichem Strom wächst die Wärme mit $R$. Parallel der kleinere: Bei gleicher Spannung fällt sie mit $R$, weil durch ihn mehr Coulomb fließen.
--- falsch
In beiden Fällen der größere, weil die Wärme nach $P=R\,I^2$ stets mit dem Widerstand wächst, gleich wie die beiden Widerstände geschaltet sind.
--- falsch
In beiden Fällen der kleinere, weil durch einen kleinen Widerstand stets mehr Strom fließt und die Wärme nur vom Strom abhängt, nicht von der Spannung.
--- falsch
In Reihe der kleinere, weil die Ladung ihn schneller durchläuft. Parallel der größere, weil an ihm je Coulomb mehr Energie abgegeben wird als am kleineren.
:::
:::karte zusammenhang Heizdraht und Zuleitung
Warum glüht in einem Heizgerät nur der Heizdraht, obwohl die Zuleitung denselben Strom führt?
---
Bei gleichem Strom ist die Wärme proportional zu $R$. Eine Zuleitung mit 10 m$\Omega$ setzt bei 0,5 A nur 2,5 mW um, eine Last mit 16 $\Omega$ dagegen 4 W, das 1600-Fache.
--- falsch
Weil die Zuleitung aus Kupfer besteht und Kupfer Wärme sofort an die Luft abgibt. Im Heizdraht entsteht je Ohm genauso viel Wärme, sie kann dort nur nicht entweichen.
--- falsch
Weil der Strom in der Zuleitung kleiner ist: Ein Teil fließt über die Isolierung zurück, bevor er den Heizdraht erreicht, und nur im Heizdraht wirkt der volle Strom.
--- falsch
Bei gleichem Strom ist die Wärme umgekehrt proportional zu $R$, sie müsste also in der Zuleitung größer sein. Der Draht glüht nur, weil er dünner ist und schneller heiß wird.
:::
:::karte begriff Hyperbel
Welche Kurve begrenzt im Strom-Spannungs-Diagramm den zulässigen Betrieb eines Widerstands, und warum hat sie diese Form?
---
Die Hyperbel $I=P_\mathrm{max}/U$: Auf ihr ist das Produkt aus Spannung und Strom gleich der Nennbelastbarkeit. Jeder Widerstand ist eine Gerade durch den Ursprung und darf nur bis zu ihr betrieben werden.
--- falsch
Eine waagerechte Gerade $I=I_\mathrm{max}$: Der Strom darf einen festen Höchstwert nicht überschreiten, weil zu viele Elektronen das Gitter überlasten. Er ist für alle Widerstandswerte gleich.
--- falsch
Eine Gerade durch den Ursprung mit der Steigung $P_\mathrm{max}$: Spannung und Strom dürfen gemeinsam wachsen, solange ihr Verhältnis unter der Nennbelastbarkeit bleibt.
--- falsch
Eine Kurve $I=P_\mathrm{max}/U^2$: Weil die Leistung quadratisch mit der Spannung wächst, sinkt der zulässige Strom mit dem Quadrat der Spannung, bei doppelter Spannung auf ein Viertel.
:::
:::karte formel Größte zulässige Spannung und größter zulässiger Strom
Bis zu welcher Spannung und welchem Strom darf ein Widerstand $R$ mit der Nennbelastbarkeit $P_\mathrm{max}$ betrieben werden?
---
$U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$ und $I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$, der Schnittpunkt seiner Geraden mit der Hyperbel. Für 100 $\Omega$ und 250 mW sind das 5 V und 50 mA.
--- falsch
$U_\mathrm{max}=P_\mathrm{max}\,R$ und $I_\mathrm{max}=P_\mathrm{max}/R$, der Schnittpunkt seiner Geraden mit der Hyperbel. Für 100 $\Omega$ und 250 mW sind das 25 V und 2,5 mA.
--- falsch
$U_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$ und $I_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$, der Schnittpunkt seiner Geraden mit der Hyperbel. Für 100 $\Omega$ und 250 mW sind das 50 mV und 5 A.
--- falsch
$U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$ und $I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$. Ein größerer Widerstand verträgt also mehr Spannung und zugleich mehr Strom als ein kleinerer.
:::
:::karte zusammenhang Temperatur und Belastbarkeit
Warum ist die Leistung, die ein Widerstand verträgt, begrenzt, und wovon hängt seine Betriebstemperatur ab?
---
Die Temperatur steigt, bis das Bauteil je Sekunde so viel Wärme an die Umgebung abgibt, wie im Inneren entsteht. Mehr Leistung heißt also höhere Temperatur, und zu hohe Temperatur zerstört es.
--- falsch
Die Temperatur steigt, solange Strom fließt, weil die Wärme nicht entweichen kann. Jeder Widerstand wird deshalb nach einer bestimmten Betriebszeit zerstört, gleich wie klein die Leistung ist.
--- falsch
Die Temperatur hängt nur vom Material ab, nicht von der Leistung. Begrenzt ist die Leistung, weil zu viele Elektronen das Gitter nicht gleichzeitig durchqueren können.
--- falsch
Die Temperatur stellt sich so ein, dass der Widerstand stets genau $P_\mathrm{max}$ an die Umgebung abgibt, gleich welche Leistung entsteht. Begrenzt ist nur die Spannung, die er isoliert.
:::
:::karte herleitung Von den Stößen zur Stromwärme
Leite aus dem Stoßmodell eines Elektrons im Feld $E$ die Leistung $P=U^2/R$ in einem Widerstand der Länge $L$ und des Querschnitts $A$ her.
---
Das Elektron wird mit $a=e\,E/m_\mathrm e$ beschleunigt und erreicht in der Flugzeit $T$ die Geschwindigkeit $v_\mathrm{max}=a\,T$ auf der Strecke $s=\frac12a\,T^2$, weil die Kraft $e\,E$ im Flug konstant ist.
---
Das Feld verrichtet die Arbeit $e\,E\,s=m_\mathrm e\,a\,s=\frac12m_\mathrm e(a\,T)^2=W_1$, weil Arbeit Kraft mal Weg ist; das ist genau die Bewegungsenergie, die beim Stoß ans Gitter geht.
---
Im Volumen $A\,L$ sitzen $n\,A\,L$ freie Elektronen, und jedes stößt $1/T$-mal je Sekunde, weil zwischen zwei Stößen die Flugzeit $T$ liegt.
---
Also ist $P=n\,A\,L\,\frac{W_1}{T}=n\,A\,L\,\frac{e^2E^2\,T}{2\,m_\mathrm e}=\sigma\,E^2\,A\,L$, weil $\sigma=n\,e\,\mu$ und $\mu=e\,T/(2\,m_\mathrm e)$ gelten.
---
Mit $U=E\,L$ und $R=L/(\sigma A)$ wird daraus $P=U^2/R$, weil $E^2L^2$ gerade $U^2$ ist und $\sigma A/L$ gerade $1/R$.
:::
::::
