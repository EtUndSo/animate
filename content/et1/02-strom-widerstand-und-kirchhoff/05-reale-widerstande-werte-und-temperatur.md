---
title: Stufe 4: Reale Widerstände: Werte und Temperatur
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1120500
summary: Bisher war R eine Zahl aus Material und Form.
tags: Metall- oder Kohleschichtwiderstände, Drahtwiderstände, SMD, E-Reihe, Temperaturkoeffizient, PTC, Kaltleiter, NTC
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher war $R$ eine Zahl aus Material und Form. Ein gekauftes Bauteil hat einen genormten Wert und eine Toleranz, und sein Widerstand ändert sich mit der Temperatur.
:::

**Die Idee.** Fertigung streut um einen Prozentsatz. Deshalb sind die angebotenen Werte so gestuft, dass aufeinanderfolgende Werte denselben *prozentualen* Abstand haben. Bei der Temperatur entscheidet $\sigma=n\,e\,\mu$: Wärme ändert entweder die Beweglichkeit $\mu$ oder die Ladungsträgerdichte $n$.

**Bauformen.** __Metall- oder Kohleschichtwiderstände__ tragen eine dünne Schicht auf einem Keramikkörper, die übliche Bauform für 0,1 bis 2 W, der Wert steht als Farbcode darauf. __Drahtwiderstände__ verkraften hohe Leistung und Temperatur, sie sind für kleine Werte geeignet. __SMD__-Widerstände (Surface Mounted Device) werden direkt auf die Leiterplatte gelötet. Sie sind sehr klein, erlauben hohe Packungsdichte, vertragen wenig Leistung und eignen sich wegen der fehlenden Anschlussdrähte für hohe Frequenzen.

:::definition Definition 4.1 (E-Reihe)
<span class="anker" id="satz-4-1"></span>

Eine __E-Reihe__ E$N$ enthält je Zehnerstufe $N$ Werte, nach DIN IEC 60063 gibt es E3, E6, E12, E24, E48, E96 und E192:

<span class="anker" id="gl-4-1"></span>
$$w=\bigl(\sqrt[N]{10}\,\bigr)^{i}=\sqrt[N]{10^{i}},\qquad i=0,1,\dots,N-1. \tag{4.1}$$
:::

⁠**So liest man das:** $w$ ist der Vorfaktor, die Dekade (Zehnerpotenz) wählt man frei. Der Schritt ist ein fester Faktor, bei E12 gilt $\sqrt[12]{10}=1{,}21$. Die Normwerte sind gerundet: 1,0; 1,2; 1,5; 1,8; 2,2; 2,7; 3,3; 3,9; 4,7; 5,6; 6,8; 8,2. Einige weichen aus historischen Gründen etwas von [(4.1)](#gl-4-1) ab, etwa 2,7 statt 2,61. Warum dieser Faktor? E12 gehört zur Toleranz $\pm10\,\%$: Die Bereiche benachbarter Werte schließen dann lückenlos aneinander, jedes gefertigte Stück gehört zu einem Normwert. Ebenso gehören E6 zu $\pm20\,\%$ und E24 zu $\pm5\,\%$.

**Farbcode.** Bedrahtete Widerstände tragen meist vier Ringe: zwei Ziffern, den Multiplikator $10^x$, die Toleranz. Die Ziffern sind schwarz 0, braun 1, rot 2, orange 3, gelb 4, grün 5, blau 6, violett 7, grau 8, weiß 9. Als Multiplikator kommen dazu gold $10^{-1}$ und silber $10^{-2}$. Die Toleranz ist braun 1 %, rot 2 %, grün 0,5 %, blau 0,25 %, violett 0,1 %, gold 5 %, silber 10 %. Gelb, violett, rot, gold bedeutet $47\cdot10^2\,\Omega=4{,}7\,\mathrm{k\Omega}$ mit $\pm5\,\%$, also 4,47 bis 4,94 k$\Omega$. $R_1$ der Kette trägt rot, schwarz, rot, gold.

:::satz Satz 4.2 (Temperaturabhängigkeit)
<span class="anker" id="satz-4-2"></span>

In der Nähe einer Bezugstemperatur $\vartheta_0$ gilt

<span class="anker" id="gl-4-2"></span>
$$R(\vartheta)=R(\vartheta_0)\,\bigl(1+\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)\bigr). \tag{4.2}$$
:::

⁠**So liest man das:** $\vartheta$ ist die Temperatur in °C, in Datenblättern meist $\vartheta_0=20$ °C. Der __Temperaturkoeffizient__ $\alpha$ hat die Einheit 1/K: Kupfer $3{,}9\cdot10^{-3}$, Wolfram $4{,}5\cdot10^{-3}$, Kohle $-0{,}5\cdot10^{-3}$, Konstantan rund $10^{-5}$. Für $\alpha>0$ heißt das Material __PTC__ (positive temperature coefficient) oder __Kaltleiter__, es leitet kalt besser. Für $\alpha<0$ heißt es __NTC__ (negative temperature coefficient) oder __Heißleiter__. **Gültigkeit:** [(4.2)](#gl-4-2) ist die Tangente an die wahre Kurve. Bei Metallen trägt sie weit, bei Halbleitern nur wenige Kelvin (Abb. [5](#abb-5) links).

:::abbildung et1/k2temperatur 5
Links: $R/R_{20}$ über der Temperatur für Kupfer ($\alpha=3{,}9\cdot10^{-3}$ /K), die kompensierte Legierung Konstantan und einen Halbleiter-Heißleiter (rund $-4\,\%$/K bei 20 °C). Rechts: Modellkennlinie einer 9-V-Glühlampe. Kalt hat sie $1{,}5\,\Omega$, im Betrieb bei 0,5 A sind es $18\,\Omega$. Die Kurve wechselt zwischen den beiden gestrichelten Geraden.
:::

**Mechanismus.** Metalle (Kupfer, Silber, Platin, Wolfram): $n$ steht fest, ein wärmeres Gitter schwingt stärker, die Flugzeit $T$ sinkt, $\mu$ sinkt, $R$ steigt. Halbleiter (Silizium, Germanium): Bei Raumtemperatur sind nur wenige Elektronen frei. Wärme befreit weitere ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)), $n$ wächst viel schneller, als $\mu$ fällt, $R$ sinkt. __Kompensierte Legierungen__ wie Konstantan: Die Stöße an den unregelmäßig eingebauten Fremdatomen überwiegen und hängen kaum von der Temperatur ab. Alternativ legt man einen PTC und einen NTC in Reihe, sodass die Zunahme des einen die Abnahme des anderen ausgleicht ($R_1\alpha_1+R_2\alpha_2=0$).

::::beispiel
Der Draht erwärmt sich von 20 °C auf 70 °C. Aus [(4.2)](#gl-4-2) folgt der Faktor $1+3{,}9\cdot10^{-3}\cdot50=1{,}195$, also 40,6 m$\Omega$ statt 34 m$\Omega$. Ein extremer Fall ist der Wolframdraht der Lampe: Der Faktor 12 von $1{,}5\,\Omega$ auf $18\,\Omega$ entspricht nach [(4.2)](#gl-4-2) rund 2460 °C, als grobe Näherung über diese große Spanne.
::::

⁠**Grenzfälle:** $\vartheta=\vartheta_0$ ergibt $R(\vartheta_0)$, $\alpha=0$ ergibt einen konstanten Wert.

:::frage Warum brennen Glühlampen meist beim Einschalten durch?
Kalt hat der Draht nur $1{,}5\,\Omega$, an 9 V fließen im ersten Moment 6 A statt 0,5 A. Dieser Stoß heizt den Draht in Sekundenbruchteilen auf. Sein Widerstand steigt, das senkt den Strom, bis sich $18\,\Omega$ einstellen. An dünnen Stellen ist die Erwärmung am stärksten, dort reißt der Draht.
:::

:::aufgabe Aufgabe 4 ★★ Normwerte und Temperatur
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Ein Widerstand trägt blau, grau, rot, gold. Wert und Bereich?

</li>

<li>

Berechne den Schrittfaktor von E24. Welche Toleranz lässt benachbarte Bereiche gerade aneinanderstoßen?

</li>

<li>

Eine Kupferspule hat bei 20 °C genau $10\,\Omega$, warm $12\,\Omega$. Wie warm ist sie?

</li>

<li>

Ein Kupferwiderstand mit $100\,\Omega$ soll mit Kohle in Reihe temperaturunabhängig werden. Welchen Wert braucht die Kohle?

</li>

</ol>

:::loesung
(a) Blau 6, grau 8, rot $10^2$, gold $\pm5\,\%$: $6{,}8\,\mathrm{k\Omega}$, Bereich 6,46 bis 7,14 k$\Omega$.

(b) $\sqrt[24]{10}=1{,}10$. Aus $(1+t)/(1-t)=1{,}10$ folgt $t=4{,}8\,\%$, gerundet $\pm5\,\%$.

(c) $\vartheta=20\text{\,°C}+(12/10-1)/(3{,}9\cdot10^{-3}\,\mathrm{K^{-1}})=71$ °C.

(d) $R_\mathrm{Cu}\,\alpha_\mathrm{Cu}+R_\mathrm K\,\alpha_\mathrm K=0$: $R_\mathrm K=100\,\Omega\cdot3{,}9/0{,}5=780\,\Omega$.
:::
:::

::::formelsammlung
**E-Reihe**

$$w=\bigl(\sqrt[N]{10}\,\bigr)^{i}=\sqrt[N]{10^{i}},\qquad i=0,1,\dots,N-1$$

E$N$ hat $N$ Werte je Zehnerstufe; $w$ ist der Vorfaktor, die Dekade wählt man frei. Aufeinanderfolgende Werte haben denselben prozentualen Abstand, bei E12 den Faktor $\sqrt[12]{10}=1{,}21$; die Normwerte sind gerundet. E6 gehört zu $\pm20\,\%$, E12 zu $\pm10\,\%$, E24 zu $\pm5\,\%$.

**Temperaturabhängigkeit**

$$R(\vartheta)=R(\vartheta_0)\,\bigl(1+\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)\bigr)$$

$\vartheta$ Temperatur in °C, meist $\vartheta_0=20$ °C; $\alpha$ Temperaturkoeffizient in 1/K. $\alpha>0$: PTC oder Kaltleiter (Metalle), $\alpha<0$: NTC oder Heißleiter (Halbleiter, Kohle). Tangente an die wahre Kurve: Bei Metallen trägt sie weit, bei Halbleitern nur wenige Kelvin.

**Temperaturkompensation in Reihe**

$$R_1\alpha_1+R_2\alpha_2=0$$

Ein PTC und ein NTC in Reihe: Die Zunahme des einen gleicht die Abnahme des anderen aus. Kompensierte Legierungen wie Konstantan (rund $10^{-5}$/K) erreichen dasselbe im Material.
::::

::::lernkarten
:::karte begriff E-Reihe
Was ist eine E-Reihe, nach der die Werte gekaufter Widerstände gestuft sind?
---
Eine genormte Reihe mit $N$ Werten je Zehnerstufe, die im festen Faktor $\sqrt[N]{10}$ aufeinander folgen: $w=\bigl(\sqrt[N]{10}\,\bigr)^{i}$, $i=0,1,\dots,N-1$. Die Normwerte sind gerundet.
--- falsch
Eine genormte Reihe mit $N$ gleichmäßig verteilten Werten je Zehnerstufe: Benachbarte Werte haben denselben absoluten Abstand, $w=1+9\,i/N$, $i=0,1,\dots,N-1$.
--- falsch
Eine genormte Reihe mit $N$ Werten, deren Vorfaktor sich von Wert zu Wert verdoppelt: $w=2^{i}$, $i=0,1,\dots,N-1$. So deckt E12 mehr als drei Zehnerstufen ab.
--- falsch
Eine Reihe gleicher Widerstände, die man hintereinanderschaltet, um Zwischenwerte zu erhalten. $N$ gibt an, wie viele Stück in einer Packung zusammen verkauft werden.
:::
:::karte zusammenhang E-Reihe und Toleranz
Warum gehört die E12-Reihe mit dem Schrittfaktor $\sqrt[12]{10}=1{,}21$ zur Toleranz $\pm10\,\%$?
---
Weil dann die Toleranzbereiche benachbarter Werte lückenlos aneinanderschließen: Jedes gefertigte Stück gehört zu einem Normwert. Ebenso gehören E6 zu $\pm20\,\%$ und E24 zu $\pm5\,\%$.
--- falsch
Weil sich bei $\pm10\,\%$ benachbarte Bereiche zur Hälfte überlappen: Jedes Stück passt zu zwei Normwerten. Ebenso gehört E24 zu $\pm20\,\%$.
--- falsch
Weil die Toleranz bei allen E-Reihen $\pm10\,\%$ beträgt. Die Zahl $N$ legt nur fest, wie viele Werte angeboten werden, nicht die Genauigkeit.
--- falsch
Weil sich Widerstände im Betrieb um bis zu 10 % erwärmen. Der Schrittfaktor sorgt dafür, dass ein warmer Widerstand nie in den Toleranzbereich des nächsthöheren Normwerts gerät.
:::
:::karte begriff Temperaturkoeffizient
Was gibt der Temperaturkoeffizient $\alpha$ eines Widerstandsmaterials an?
---
Um welchen Bruchteil von $R(\vartheta_0)$ sich der Widerstand je Kelvin Erwärmung ändert; Einheit 1/K. Kupfer hat $3{,}9\cdot10^{-3}$/K, Kohle $-0{,}5\cdot10^{-3}$/K.
--- falsch
Um wie viel Ohm sich der Widerstand je Kelvin Erwärmung ändert, gleich wie groß er ist; Einheit $\Omega$/K. Er ist bei allen Metallen gleich.
--- falsch
Die Temperatur, bei der ein Widerstand seinen aufgedruckten Wert hat; Einheit °C. In Datenblättern sind das meist 20 °C.
--- falsch
Um welchen Bruchteil sich der Widerstand je Kelvin Erwärmung ändert; Einheit 1/K. Für Metalle ist er negativ, für Halbleiter positiv.
:::
:::karte formel Temperaturabhängigkeit
Wie hängt der Widerstand $R(\vartheta)$ in der Nähe einer Bezugstemperatur $\vartheta_0$ von der Temperatur ab?
---
$R(\vartheta)=R(\vartheta_0)\,\bigl(1+\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)\bigr)$. Das ist die Tangente an die wahre Kurve: Bei Metallen trägt sie weit, bei Halbleitern nur wenige Kelvin.
--- falsch
$R(\vartheta)=R(\vartheta_0)\,\bigl(1+\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)\bigr)$. Die Gleichung ist exakt und gilt für jedes Material über den ganzen Temperaturbereich, auch für Halbleiter.
--- falsch
$R(\vartheta)=R(\vartheta_0)+\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)$. Das ist die Tangente an die wahre Kurve: Bei Metallen trägt sie weit, bei Halbleitern nur wenige Kelvin.
--- falsch
$R(\vartheta)=R(\vartheta_0)\,\alpha_{\vartheta_0}\,(\vartheta-\vartheta_0)$. Das ist die Tangente an die wahre Kurve: Bei Metallen trägt sie weit, bei Halbleitern nur wenige Kelvin.
:::
:::karte begriff PTC und Kaltleiter
Was bezeichnet man als PTC oder Kaltleiter, und welche Stoffe verhalten sich so?
---
Ein Material mit positivem Temperaturkoeffizienten, $\alpha>0$: Sein Widerstand steigt mit der Temperatur, es leitet kalt besser. So verhalten sich Metalle wie Kupfer und Wolfram.
--- falsch
Ein Material mit negativem Temperaturkoeffizienten, $\alpha<0$: Sein Widerstand sinkt mit der Temperatur, es leitet kalt schlechter. So verhalten sich Halbleiter wie Silizium und Germanium.
--- falsch
Ein Material mit positivem Temperaturkoeffizienten, $\alpha>0$: Sein Widerstand sinkt mit der Temperatur, es leitet warm besser. So verhält sich Kohle.
--- falsch
Ein Material, dessen Widerstand nicht von der Temperatur abhängt, $\alpha=0$: Es leitet kalt und warm gleich gut. So verhält sich Konstantan.
:::
:::karte begriff NTC und Heißleiter
Was bezeichnet man als NTC oder Heißleiter, und welche Stoffe verhalten sich so?
---
Ein Material mit negativem Temperaturkoeffizienten, $\alpha<0$: Sein Widerstand sinkt mit der Temperatur, es leitet heiß besser. So verhalten sich Halbleiter und Kohle.
--- falsch
Ein Material mit negativem Temperaturkoeffizienten, $\alpha<0$: Sein Widerstand steigt mit der Temperatur, es leitet heiß schlechter. So verhalten sich Metalle wie Kupfer.
--- falsch
Ein Material mit positivem Temperaturkoeffizienten, $\alpha>0$: Sein Widerstand steigt mit der Temperatur, es leitet kalt besser. So verhalten sich Metalle wie Wolfram.
--- falsch
Ein Material, das sich bei Stromfluss stark erwärmt, weil sein Widerstand besonders groß ist. So verhalten sich Widerstände aus Konstantan.
:::
:::karte zusammenhang Metalle in der Wärme
Warum steigt der Widerstand eines Metalls, wenn es wärmer wird?
---
Weil das wärmere Gitter stärker schwingt: Die Flugzeit $T$ sinkt, damit sinkt $\mu$ und mit ihm $\sigma=n\,e\,\mu$. Die Zahl $n$ der freien Elektronen steht im Metall fest.
--- falsch
Weil Wärme freie Elektronen bindet: Ihre Zahl $n$ sinkt, damit sinkt $\sigma=n\,e\,\mu$. Die Flugzeit zwischen den Stößen bleibt dabei gleich.
--- falsch
Weil sich das Metall ausdehnt: Der Draht wird länger, und nach $R=\rho\,L/A$ wächst sein Widerstand mit der Länge. Am Material selbst ändert sich dabei nichts.
--- falsch
Weil die Elektronen in der Wärme schneller driften: Bei höherer Driftgeschwindigkeit stoßen sie öfter, und der Strom sinkt.
:::
:::karte zusammenhang Halbleiter in der Wärme
Warum sinkt der Widerstand eines Halbleiters wie Silizium, wenn er wärmer wird?
---
Weil Wärme weitere Elektronen befreit: Bei Raumtemperatur sind nur wenige frei, und $n$ wächst viel schneller, als $\mu$ fällt.
--- falsch
Weil das Gitter in der Wärme weniger schwingt: Die Flugzeit zwischen den Stößen wird länger, $\mu$ steigt, während $n$ gleich bleibt.
--- falsch
Weil Wärme die freien Elektronen bindet, die sonst an das Gitter stoßen würden. Weniger Stöße bedeuten weniger Widerstand.
--- falsch
Weil sich Halbleiter in der Wärme zusammenziehen: Der Querschnitt bleibt gleich, aber die Länge sinkt und mit ihr der Widerstand.
:::
:::karte begriff kompensierte Legierungen
Was sind kompensierte Legierungen wie Konstantan, und warum hängt ihr Widerstand kaum von der Temperatur ab?
---
Legierungen, in denen die Stöße an den unregelmäßig eingebauten Fremdatomen überwiegen. Diese Stöße hängen kaum von der Temperatur ab; bei Konstantan ist $\alpha$ nur rund $10^{-5}$/K.
--- falsch
Legierungen aus einem Metall und einem Halbleiter zu gleichen Teilen. Die Zunahme des einen Anteils gleicht die Abnahme des anderen bei jeder Temperatur genau aus, deshalb ist $\alpha=0$.
--- falsch
Legierungen, die bei Erwärmung ihre freien Elektronen behalten. In reinen Metallen verdampfen freie Elektronen in der Wärme, deshalb steigt dort der Widerstand.
--- falsch
Legierungen mit besonders hohem Schmelzpunkt. Sie erwärmen sich im Betrieb kaum, deshalb ändert sich ihr Widerstand nicht.
:::
:::karte formel Temperaturkompensation in Reihe
Welche Bedingung müssen ein PTC und ein NTC in Reihe erfüllen, damit der Gesamtwiderstand nicht von der Temperatur abhängt?
---
$R_1\alpha_1+R_2\alpha_2=0$: Die Zunahme des einen Widerstands gleicht die Abnahme des anderen genau aus.
--- falsch
$\alpha_1+\alpha_2=0$: Die Koeffizienten müssen entgegengesetzt gleich sein, gleich welche Werte die beiden Widerstände haben.
--- falsch
$R_1\alpha_1=R_2\alpha_2$: Beide Widerstände müssen sich gleich stark ändern, damit ihre Summe gleich bleibt.
--- falsch
$R_1/\alpha_1+R_2/\alpha_2=0$: Der größere Widerstand braucht dafür auch den größeren Betrag von $\alpha$.
:::
:::karte begriff Metall- oder Kohleschichtwiderstände
Wie sind Metall- oder Kohleschichtwiderstände aufgebaut, und wofür sind sie üblich?
---
Eine dünne Widerstandsschicht auf einem Keramikkörper. Sie sind die übliche Bauform für 0,1 bis 2 W; der Wert steht als Farbcode darauf.
--- falsch
Ein aufgewickelter Draht auf einem Keramikkörper. Sie sind die übliche Bauform für hohe Leistung und hohe Temperatur.
--- falsch
Ein winziger Block ohne Anschlussdrähte, der direkt auf die Leiterplatte gelötet wird. Sie sind die übliche Bauform für hohe Frequenzen.
--- falsch
Ein massiver Stab aus Metall oder Kohle ohne Träger. Sie sind die übliche Bauform für Werte unter einem Ohm; ihr Wert ist nicht aufgedruckt.
:::
:::karte begriff Drahtwiderstände
Wofür eignen sich Drahtwiderstände besonders?
---
Sie verkraften hohe Leistung und hohe Temperatur und sind für kleine Widerstandswerte geeignet.
--- falsch
Sie eignen sich für hohe Frequenzen, weil sie keine Anschlussdrähte haben, und für sehr große Widerstandswerte.
--- falsch
Sie eignen sich für kleine Leistung auf engem Raum, weil man sie direkt auf die Leiterplatte lötet.
--- falsch
Sie eignen sich als Temperaturfühler, weil ihr Widerstand in der Wärme stark sinkt, und für große Werte.
:::
:::karte begriff SMD
Was sind SMD-Widerstände, und welche Vor- und Nachteile haben sie?
---
Widerstände, die direkt auf die Leiterplatte gelötet werden (Surface Mounted Device): sehr klein, hohe Packungsdichte, ohne Anschlussdrähte gut für hohe Frequenzen, aber nur für wenig Leistung.
--- falsch
Widerstände mit langen Anschlussdrähten, die durch Löcher der Leiterplatte gesteckt werden. Sie vertragen viel Leistung, eignen sich wegen der Drähte aber nicht für hohe Frequenzen.
--- falsch
Widerstände, die direkt auf die Leiterplatte gelötet werden. Sie sind sehr klein und vertragen dank der großen Lötfläche besonders viel Leistung, eignen sich aber nicht für hohe Frequenzen.
--- falsch
Widerstände aus einem aufgewickelten Draht, die für Messungen bei hoher Temperatur gebaut sind. Sie sind groß, vertragen viel Leistung und eignen sich für kleine Werte.
:::
::::
