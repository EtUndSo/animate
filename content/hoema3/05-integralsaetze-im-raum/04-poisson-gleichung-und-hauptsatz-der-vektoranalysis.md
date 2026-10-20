---
title: Poisson-Gleichung und Hauptsatz der Vektoranalysis
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050400
summary: Von Grund auf – was die Integralsätze in der Potentialtheorie leisten. Leitbild ist Wasser mit Quellen und Strudeln: Eine Quelle der Schüttung $1$ erzeugt die Strömung des Coulomb-Potentials $g$, und eine winzige Blase um den Messpunkt zeigt mit der partiellen Integration mit Rand, dass das Newtonpotential die Poisson-Gleichung $-\Delta u=f$ löst. Dazu die Greensche Funktion, der Hauptsatz der Vektoranalysis $\vec F=\nabla u+\operatorname{rot}\vec A$ mit ausdrücklichen Potentialen aus Quellen und Wirbeln, Coulomb-Eichung, Eindeutigkeit und die Potentialformeln der Elektro- und Magnetostatik. Mit Beispiel-Seite.
tags: Poisson-Gleichung, Greensche Funktion, Fundamentallösung, Coulomb-Potential, Helmholtz-Zerlegung, Hauptsatz der Vektoranalysis, Vektorpotential, Eichung
---

## Anschaulich

Die beiden Integralsätze des Kapitels verbinden einen Körper mit seiner Oberfläche und eine Fläche mit ihrem Rand. Dieser
letzte Artikel des Kapitels zeigt, was sie in der Potentialtheorie leisten: Aus seinen Quellen und Wirbeln lässt sich ein Feld
zurückgewinnen.

**Das Leitbild dieses Artikels:** **Wasser mit Quellen und Strudeln.** Man denke sich den ganzen Raum mit Wasser gefüllt, das
weit draußen ruht. In Bewegung setzen es zwei Dinge: __Quellen__, aus denen Wasser entspringt — oder Senken, in denen es
verschwindet —, und __Strudel__, um die es kreist. Die Quellen misst die Divergenz, die Strudel misst die Rotation.

**Eine einzelne Quelle.** Stößt eine Quelle in jeder Sekunde eine Einheit Wasser aus — ihre __Schüttung__ ist $1$ —, drückt sie
es gleichmäßig nach allen Seiten weg. Durch jede Kugel um die Quelle muss diese eine Einheit hindurch, wie groß die Kugel auch
ist. Die Kugel vom Radius $r$ hat die Fläche $4\pi r^2$, also strömt das Wasser dort mit der Stärke $\frac{1}{4\pi r^2}$. Das
Potential dieser Strömung ist das Coulomb-Potential aus dem Kapitel über Koordinatentransformationen.

**Viele Quellen.** Verteilt man Quellen mit einer Dichte $f$ im Raum, überlagern sich ihre Strömungen, und ihre Potentiale
addieren sich zum Newtonpotential $u$. Der erste Teil des Artikels beweist, dass diese Strömung genau die Quellen hat, die man
hineingesteckt hat. Das ist die __Poisson-Gleichung__

$$-\Delta u = f.$$

Den Beweis trägt eine winzige **Blase** um den Messpunkt. Außerhalb der Blase entspringt in der Strömung einer einzelnen Quelle
nirgends Wasser; ihre ganze Schüttung tritt gleichmäßig durch die Blasenhaut. Deshalb bleibt am Ende das Mittel der Quelldichte
über die Haut übrig — und eine winzige Blase misst damit die Dichte am Messpunkt.

**Quellen und Strudel getrennt.** Im Abfluss einer Badewanne steckt beides: Das Wasser verschwindet im Abfluss, einer Senke, und
kreist dabei, ein Strudel. Der zweite Teil, der __Hauptsatz der Vektoranalysis__, sagt: Jede glatte Strömung, die weit draußen
ruht, ist die Überlagerung einer **Quellenströmung**, die nur von den Quellen angetrieben wird und nicht wirbelt, und einer
**Wirbelströmung**, die nur von den Strudeln angetrieben wird und nirgends entspringt. Beide lassen sich sogar ausdrücklich aus
den Quellen und Strudeln berechnen.

:::grafik
Szene: hoema3/integralsaetze-im-raum/04-quellen-und-strudel · Vorlage: quelle-strudel-3d
Links eine einzelne Quelle im Ursprung mit radialen Strömungspfeilen und drei durchsichtigen Kugeln um sie. Ein Regler ändert
die Radien; die Pfeile werden nach außen wie $\frac{1}{4\pi r^2}$ kürzer, und ein Zähler zeigt für jede Kugel den Durchfluss —
immer $1$. Rechts eine Spiralströmung in einen Abfluss; ein zweiter Regler zieht sie in zwei Felder auseinander: einen reinen
Zufluss mit geraden Pfeilen zur Mitte, die Quellenströmung, und ein reines Kreisen, die Wirbelströmung. Kernaussage: Eine Quelle
schickt durch jede Kugel dieselbe Menge Wasser, und jede Strömung ist Quellenströmung plus Wirbelströmung. (Rot = Quelle und
Strudel, blau = Strömungspfeile, orange = Zähler und Zerlegung, grau = Kugeln und Achsen.)
:::

## Die Einheitsquelle

**Der Akteur:** das __Coulomb-Potential__ der Einheitsladung aus dem Artikel über das Newtonpotential,

$$g:\mathbb{R}^3\setminus\{\vec 0\}\to\mathbb{R}, \qquad g(\vec z) = \frac{1}{4\pi\lvert\vec z\rvert}.$$

Eingabe ist ein Punkt $\vec z$ außer dem Ursprung, Ausgabe eine Zahl. Mit dem Abstand $r=\lvert\vec z\rvert$ ist das
$\frac{1}{4\pi r}$; der Einheitsvektor $\vec e_r$ zeigt in Richtung von $\vec z$, vom Ursprung weg. Das Skript nennt die Funktion
$\phi$ und benutzt ähnliche Zeichen in diesem Abschnitt auch für eine Gewichtung und ein Eichpotential; hier heißt sie $g$ wie im
Artikel über das Newtonpotential.

Zwei Eigenschaften tragen den ganzen Artikel: das Gefälle von $g$ und seine Quellenfreiheit. Für jeden Punkt $\vec z$ außer dem
Ursprung gilt

:::formel
$$\nabla g(\vec z) = -\frac{\vec e_r}{4\pi r^2}, \qquad \Delta g(\vec z) = 0.$$
:::

**So liest man das:** Der Gradient zeigt zum Ursprung hin und hat den Betrag $\frac{1}{4\pi r^2}$. Eine Funktion mit
verschwindendem Laplace-Operator heißt __harmonisch__; $g$ ist es überall außer im Ursprung, wo es nicht definiert ist.

**Im Bild:** Wasser strömt im Potential bergab; die Strömung der Einheitsquelle ist $-\nabla g$. Sie zeigt vom Ursprung weg und
hat die Stärke $\frac{1}{4\pi r^2}$. Ihre Quelldichte ist

$$\operatorname{div}\big(-\nabla g\big) = -\Delta g = 0 \quad\text{außerhalb des Ursprungs}.$$

Außer in der Quelle selbst entspringt nirgends Wasser.

:::herleitung
**Der Gradient.** Der Abstand hat nach der Kettenregel die Ableitungen

$$\frac{\partial r}{\partial z_k} = \frac{\partial}{\partial z_k}\sqrt{z_1^2+z_2^2+z_3^2} = \frac{z_k}{r}, \qquad \nabla r = \frac{\vec z}{r} = \vec e_r.$$

Mit der Kettenregel für die Funktion $\frac1r$ folgt

$$\nabla g = \frac{1}{4\pi}\,\nabla\frac1r = -\frac{1}{4\pi r^2}\,\nabla r = -\frac{\vec e_r}{4\pi r^2} = -\frac{\vec z}{4\pi r^3}.$$

**Der Laplace-Operator** ist die Divergenz des Gradienten, hier bis auf den Faktor $-\frac{1}{4\pi}$ die Divergenz von
$\frac{\vec z}{r^3}$. Nach der Produktregel für die Divergenz aus dem Rechenregeln-Artikel, mit dem Skalarfeld $r^{-3}$ und dem
Ortsvektorfeld $\vec z$ der Divergenz $3$:

$$\operatorname{div}\Big(\frac{\vec z}{r^3}\Big) = \nabla\big(r^{-3}\big)\cdot\vec z+r^{-3}\operatorname{div}\vec z,$$

$$\nabla\big(r^{-3}\big)\cdot\vec z = -\frac{3}{r^4}\,\frac{\vec z}{r}\cdot\vec z = -\frac{3}{r^3}, \qquad r^{-3}\operatorname{div}\vec z = \frac{3}{r^3}.$$

Die beiden Terme heben sich auf, also verschwindet $\Delta g$.

**Im Bild:** Die Strömung wird nach außen genau so schnell schwächer, wie die Kugelflächen wachsen. Deshalb kommt auf jeder
Kugel dieselbe Menge Wasser an, und zwischen zwei Kugeln entspringt nichts.
:::

**Die Schüttung.** Daraus folgt die Eigenschaft, die der Einheitsquelle ihren Namen gibt. Sei $K_R(\vec 0)\subseteq\mathbb{R}^3$
die Kugel vom Radius $R>0$ um den Ursprung, ihre Oberfläche nach außen orientiert, mit dem orientierten Flächenelement $d\vec S$
aus dem Artikel über den Satz von Gauß. Dann ist

$$\int_{\partial K_R(\vec 0)}\big(-\nabla g\big)\cdot d\vec S = 1.$$

:::herleitung
Auf der Kugeloberfläche vom Radius $R$ ist die äußere Normale $\vec e_r$, die Normalkomponente der Strömung also überall gleich:

$$\big(-\nabla g\big)\cdot\vec e_r = \frac{\vec e_r\cdot\vec e_r}{4\pi R^2} = \frac{1}{4\pi R^2}.$$

Eine konstante Normalkomponente mal die Fläche $4\pi R^2$ ergibt den Fluss $1$.

**Im Bild:** Die Schüttung $1$ verteilt sich gleichmäßig auf die Kugelhaut; jedes Flächenstück bekommt seinen Anteil an der
Gesamtfläche.
:::

::::beispiel Schüttung 1 auf jeder Kugel
Die Strömung der Einheitsquelle ist

$$-\nabla g(\vec z) = \frac{\vec e_r}{4\pi r^2}, \qquad \vec z\in\mathbb{R}^3\setminus\{\vec 0\}.$$

Auf drei Kugeln um den Ursprung, jeweils Stärke mal Fläche:

| Radius $R$ | Stärke $\frac{1}{4\pi R^2}$ | Fläche $4\pi R^2$ | Fluss |
|---|---|---|---|
| $1$ | $\frac{1}{4\pi}$ | $4\pi$ | $1$ |
| $2$ | $\frac{1}{16\pi}$ | $16\pi$ | $1$ |
| $10$ | $\frac{1}{400\pi}$ | $400\pi$ | $1$ |

Zehnmal so weit draußen ist die Strömung hundertmal schwächer, die Kugel aber hundertmal größer.

**Im Bild:** Dasselbe Wasser durchströmt jede Kugelhaut, weiter draußen dünner verteilt. Dass zwischen zwei Kugeln nichts
verloren geht und nichts hinzukommt, ist die Quellenfreiheit außerhalb des Ursprungs.
::::

**Integrierbar trotz Singularität.** Am Ursprung werden $g$ und sein Gradient unendlich. Trotzdem sind beide über jede Kugel um
den Ursprung integrierbar, weil sie wie $\frac1r$ bzw. $\frac{1}{r^2}$ wachsen, beides langsamer als $\frac{1}{r^3}$ — das ist der
Satz über singuläre Integranden aus dem Kapitel über Koordinatentransformationen, im Skript Satz 4.8. Genau ist

$$\int_{K_R(\vec 0)}g\;d^3z = \frac{R^2}{2}, \qquad \int_{K_R(\vec 0)}\lvert\nabla g\rvert\;d^3z = R.$$

:::herleitung
Hängt ein Integrand nur vom Abstand $r$ ab, zerlegt man die Kugel nach dem Artikel über Volumenintegrale in Kugelschalen der
Fläche $4\pi r^2$ und der Dicke $dr$:

$$\int_{K_R(\vec 0)}g\;d^3z = \int_0^R\frac{1}{4\pi r}\,4\pi r^2\;dr = \int_0^R r\;dr = \frac{R^2}{2},$$

$$\int_{K_R(\vec 0)}\lvert\nabla g\rvert\;d^3z = \int_0^R\frac{1}{4\pi r^2}\,4\pi r^2\;dr = \int_0^R 1\;dr = R.$$

Am Ursprung sind die Integrale uneigentlich, aber die Integranden in $r$ sind beschränkt — deshalb konvergieren sie.

**Im Bild:** Nahe der Quelle ist die Strömung heftig, aber dort ist wenig Raum: Die Schalenfläche $4\pi r^2$ macht die
Singularität wett.
:::

## Das Newtonpotential löst die Poisson-Gleichung

**Die Akteure:** eine stetig differenzierbare Quelldichte $f:\mathbb{R}^3\to\mathbb{R}$ mit kompaktem Träger — sie ist außerhalb
einer Kugel $K_{R_0}(\vec 0)\subseteq\mathbb{R}^3$ null — und ihr Newtonpotential aus dem Kapitel über Koordinatentransformationen,

$$u(\vec x) = \int_{\mathbb{R}^3}g(\vec x-\vec y)\,f(\vec y)\;d^3y, \qquad \vec x\in\mathbb{R}^3.$$

Der folgende Satz stand dort schon, im Skript als Satz 4.9, aber ohne Beweis. Jetzt folgt der Beweis mit dem Satz von Gauß: Die
Funktion $u$ ist zweimal stetig differenzierbar, und es gilt

:::formel Satz
$$-\Delta u = f \quad\text{in } \mathbb{R}^3.$$
:::

**So liest man das:** Der Laplace-Operator ist die Divergenz des Gradienten. Weil das Wasser im Potential bergab strömt, ist
$-\nabla u$ die Strömung, und ihre Quelldichte ist

$$\operatorname{div}\big(-\nabla u\big) = -\Delta u = f.$$

**Im Bild:** Die überlagerte Strömung aller Quellen hat genau die Quellen, die man verteilt hat — nicht mehr und nicht weniger.

**Das Zusammenspiel:** *Wie holt man aus einem Integral über alle Quellen die Dichte an einem einzigen Punkt heraus?* Der Beweis
braucht sieben kurze Schritte.

**Schritt 1: Verschieben.** Mit dem Versatz $\vec z$ vom Körnchen zum Messpunkt, also mit dem Körnchen am Ort $\vec x-\vec z$,
wird das Potential zu

$$u(\vec x) = \int_{\mathbb{R}^3}g(\vec z)\,f(\vec x-\vec z)\;d^3z.$$

**Im Bild:** Das Körnchen am Ort $\vec x-\vec z$ trägt $g(\vec z)$ mal seine Dichte bei. Der Kern hängt nur noch vom Versatz ab,
der Messpunkt steht nur noch in der Dichte. Das Skript nennt die neue Variable wieder $\vec y$.

:::herleitung
Die Abbildung $\vec z\mapsto\vec x-\vec z$ hat als Jacobi-Matrix die negative Einheitsmatrix, mit der Determinante $-1$. Ihr Betrag ist $1$, und nach dem
Transformationssatz ändert die Substitution das Integral nicht. Der singuläre Punkt, an dem $\vec y$ mit $\vec x$ zusammenfällt,
wandert in den Ursprung.
:::

**Schritt 2: Ableiten unter dem Integral.** Die erste Ableitung legt man auf den Kern, die zweite auf die Dichte:

$$\nabla u(\vec x) = \int_{\mathbb{R}^3}\nabla g(\vec x-\vec y)\,f(\vec y)\;d^3y = \int_{\mathbb{R}^3}\nabla g(\vec z)\,f(\vec x-\vec z)\;d^3z,$$

$$\Delta u(\vec x) = \int_{\mathbb{R}^3}\nabla g(\vec z)\cdot(\nabla f)(\vec x-\vec z)\;d^3z.$$

Im Skript fehlt im zweiten Integral für $\nabla u$ das Nabla vor dem Kern.

**Im Bild:** Die Strömung $-\nabla u$ ist die Summe der Strömungen aller Körnchen, jede die einer Einheitsquelle, gewichtet mit
der Dichte des Körnchens. Für die Quelldichte dieser Strömung leitet man noch einmal ab — aber nicht wieder den Kern, sondern die
Dichte.

:::herleitung
**Die Formeln.** Für $\nabla u$ leitet man die ursprüngliche Form nach $\vec x$ ab; die Ableitung trifft den Kern. Danach
verschiebt man wie in Schritt 1. Für $\Delta u$ bildet man die Divergenz der verschobenen Form. Dort steht $\vec x$ nur in der
Dichte, und nach der Kettenregel ist

$$\frac{\partial}{\partial x_k}\Big[f(\vec x-\vec z)\Big] = (\partial_k f)(\vec x-\vec z), \qquad \operatorname{div}_{\vec x}\Big[\nabla g(\vec z)\,f(\vec x-\vec z)\Big] = \nabla g(\vec z)\cdot(\nabla f)(\vec x-\vec z).$$

**Warum man unter dem Integral ableiten darf.** Ganz streng braucht das einen Satz über parameterabhängige Lebesgue-Integrale, auf
den das Skript verzichtet. Die Idee in drei Gedanken:

**Ohne Singularität ist alles gewöhnlich.** Rundet man den Kern in einer kleinen Kugel $K_\varepsilon(\vec 0)$ vom Radius
$\varepsilon>0$ glatt ab — innen eine beschränkte, glatte Kappe, außen unverändert —, sind alle Integranden stetig
differenzierbar, und nach dem Artikel über Parameterintegrale darf man unter dem Integral ableiten.

**Der Fehler ist klein, und zwar gleichmäßig.** Der abgerundete Kern weicht vom echten nur in $K_\varepsilon(\vec 0)$ ab. Weil dort
schon $\lvert\nabla g\rvert$ nur das Integral $\varepsilon$ hat, sind die Unterschiede aller Potentiale und Ableitungen höchstens
eine feste Zahl mal $\varepsilon$ — für jeden Messpunkt dieselbe Schranke.

**Grenzübergang.** Für $\varepsilon\to0$ konvergieren deshalb die abgerundeten Potentiale und ihre Ableitungen bis zur zweiten Ordnung
gleichmäßig. Nach dem Satz über gleichmäßige Konvergenz von Ableitungen aus dem Kapitel über Funktionenfolgen ist dann $u$
zweimal stetig differenzierbar, mit den Formeln oben.
:::

**Schritt 3: Eine Blase ausschneiden.** Weil $\nabla g$ integrierbar ist, ändert sich das Integral im Grenzwert nicht, wenn man um
den Ursprung eine kleine Kugel weglässt:

$$-\Delta u(\vec x) = -\lim_{\varepsilon\searrow0}\int_{\lvert\vec z\rvert\ge\varepsilon}\nabla g(\vec z)\cdot(\nabla f)(\vec x-\vec z)\;d^3z.$$

**Im Bild:** Die Punkte $\vec x-\vec z$ mit $\lvert\vec z\rvert<\varepsilon$ bilden eine __Blase__ vom Radius $\varepsilon$ um den
Messpunkt. Man rechnet nur noch außerhalb von ihr und lässt sie danach schrumpfen.

:::herleitung
Der weggelassene Teil ist das Integral über $K_\varepsilon(\vec 0)$. Weil $\nabla f$ stetig mit kompaktem Träger und daher
beschränkt ist, ist sein Betrag höchstens

$$\max\lvert\nabla f\rvert\cdot\int_{K_\varepsilon(\vec 0)}\lvert\nabla g\rvert\;d^3z = \max\lvert\nabla f\rvert\cdot\varepsilon,$$

und das geht für $\varepsilon\to0$ gegen null.
:::

**Warum nur eine Ableitung auf den Kern?** Man könnte versucht sein, beide Ableitungen des Laplace-Operators auf den Kern zu
legen. Wegen der Quellenfreiheit von $g$ käme dann für jede Dichte

$$\Delta u(\vec x) \overset{?}{=} \int_{\mathbb{R}^3}\Delta g(\vec x-\vec y)\,f(\vec y)\;d^3y = 0$$

heraus — falsch, sobald $f$ irgendwo nicht null ist. Der Fehler: Die zweiten Ableitungen von $g$ wachsen am Ursprung wie
$\frac{1}{r^3}$ und sind nicht mehr integrierbar. Die ganze Quellwirkung des Kerns sitzt im Ursprung, wo er nicht
differenzierbar ist.

**Im Bild:** Außerhalb ihres Zentrums hat die Strömung der Einheitsquelle keine Quellen. Wer nur dort hinschaut, übersieht die
Quelle selbst.

::::beispiel Eine Ableitung zu viel
**(a) Eine Ableitung auf dem Kern.** Was die Blase vom Radius $\varepsilon$ wegnimmt, schrumpft mit ihr:

$$\int_{K_\varepsilon(\vec 0)}\lvert\nabla g\rvert\;d^3z = \varepsilon, \qquad \varepsilon = 0{,}1:\ \ 0{,}1, \qquad \varepsilon = 10^{-3}:\ \ 10^{-3}.$$

**(b) Zwei Ableitungen auf dem Kern.** Die zweite Ableitung in radialer Richtung ist

$$\frac{\partial^2 g}{\partial r^2} = \frac{d^2}{dr^2}\,\frac{1}{4\pi r} = \frac{1}{2\pi r^3}.$$

Über die Kugelschale zwischen den Radien $\varepsilon$ und $1$ integriert, mit den Kugelschalen aus der Rechnung oben:

$$\int_{\varepsilon\le\lvert\vec z\rvert\le1}\frac{1}{2\pi r^3}\;d^3z = \int_\varepsilon^1\frac{4\pi r^2}{2\pi r^3}\;dr = 2\ln\frac1\varepsilon.$$

Das wächst ohne Grenze, wenn die Blase schrumpft:

$$\varepsilon = 0{,}1:\ \ 4{,}6, \qquad \varepsilon = 10^{-3}:\ \ 13{,}8, \qquad \varepsilon = 10^{-6}:\ \ 27{,}6.$$

Die radiale zweite Ableitung mischt die zweiten partiellen Ableitungen mit Gewichten vom Betrag höchstens $1$. Wären alle zweiten
partiellen Ableitungen integrierbar, wäre es auch sie — also ist mindestens eine von ihnen nicht integrierbar.

:::herleitung
Auf dem Strahl vom Ursprung in Richtung $\vec e_r$ gibt die Kettenregel zweimal

$$\frac{\partial^2 g}{\partial r^2} = \sum_{i,j=1}^3 e_i\,e_j\,\frac{\partial^2 g}{\partial z_i\,\partial z_j},$$

mit den Komponenten $e_i$ von $\vec e_r$. Sie sind betragsmäßig höchstens $1$, also ist der Betrag links höchstens die Summe der
Beträge aller zweiten partiellen Ableitungen.
:::

**Im Bild:** Mit einer Ableitung bleibt der Beitrag der nahen Körnchen klein. Mit zwei Ableitungen ballt er sich im Ursprung —
dort sitzt die Quelle, die man nicht übersehen darf.
::::

**Schritt 4: Die Ableitung umhängen.** Im verbleibenden Integral ersetzt man den Gradienten nach $\vec x$ durch den nach $\vec z$, mit
einem Minuszeichen. Für den festen Messpunkt $\vec x$ sei dazu die __Gewichtung__

$$\psi:\mathbb{R}^3\to\mathbb{R}, \qquad \psi(\vec z) = f(\vec x-\vec z).$$

Damit wird

$$-\Delta u(\vec x) = \lim_{\varepsilon\searrow0}\int_{\lvert\vec z\rvert\ge\varepsilon}\nabla g(\vec z)\cdot\nabla\psi(\vec z)\;d^3z.$$

**Im Bild:** $\psi$ ist die Quellwolke, vom Messpunkt aus gesehen — die Dichte am Ort mit dem Versatz $\vec z$. Geht man im Versatz
einen Schritt weiter, geht man in der Wolke einen Schritt in die Gegenrichtung; daher das Minuszeichen, das das Minus vor dem
Integral aufhebt. Das Skript nennt die Gewichtung $\varphi$ und schreibt die Zeile vor diesem Schritt schon ohne Minuszeichen;
gemeint ist dort bereits der Gradient nach der Integrationsvariablen.

:::herleitung
Nach der Kettenregel ist für jede Koordinate

$$\frac{\partial\psi}{\partial z_k}(\vec z) = \frac{\partial}{\partial z_k}\Big[f(\vec x-\vec z)\Big] = -(\partial_k f)(\vec x-\vec z),$$

denn die $k$-te Komponente von $\vec x-\vec z$ hat nach $z_k$ die Ableitung $-1$. Also ist

$$(\nabla f)(\vec x-\vec z) = -\nabla\psi(\vec z),$$

und dieses Minuszeichen hebt das vor dem Integral auf.
:::

**Schritt 5: Partielle Integration auf einer Kugelschale.** Die Gewichtung ist null, sobald $\vec x-\vec z$ außerhalb von
$K_{R_0}(\vec 0)$ liegt, also sicher für $\lvert\vec z\rvert>\lvert\vec x\rvert+R_0$. Für einen Radius $R$, der größer ist als
$\lvert\vec x\rvert+R_0$, ist das Integral deshalb dasselbe wie über die __Kugelschale__

$$V = \big\{\vec z\in\mathbb{R}^3 : \varepsilon\le\lvert\vec z\rvert\le R\big\}.$$

Sie ist beschränkt und abgeschlossen mit glattem Rand: außen die große Kugeloberfläche, innen die Blasenhaut
$S_\varepsilon=\partial K_\varepsilon(\vec 0)$. Die partielle Integration mit Rand aus dem Artikel über den Satz von Gauß verlangt
einen beschränkten Körper — deshalb der äußere Radius $R$, den das Skript stillschweigend übergeht. Mit dem Feld $\nabla g$ und der
Gewichtung $\psi$, beide stetig differenzierbar auf einer offenen Menge um $V$, weil $V$ den Ursprung nicht enthält, gilt

$$\int_V\nabla g\cdot\nabla\psi\;d^3z = \int_{\partial V}\psi\,\nabla g\cdot d\vec S-\int_V\Delta g\;\psi\;d^3z.$$

Rechts verschwindet das Volumenintegral, weil $g$ in $V$ harmonisch ist, und auf der äußeren Kugeloberfläche ist $\psi$ null.
Übrig bleibt die Blasenhaut, mit der **äußeren Normale der Schale** — und die zeigt dort zum Ursprung hin:

$$\int_V\nabla g\cdot\nabla\psi\;d^3z = \int_{S_\varepsilon}\psi\,\frac{\partial g}{\partial n}\;d\sigma, \qquad \vec n = -\vec e_r \quad\text{auf } S_\varepsilon.$$

Dabei ist $\frac{\partial g}{\partial n}=\nabla g\cdot\vec n$ die Normalableitung aus dem Artikel über den Satz von Gauß. Die
Blasenhaut ist hier Rand der Schale, nicht der Blase; darauf weist auch das Skript ausdrücklich hin.

**Im Bild:** In der Schale ist die Strömung der Einheitsquelle quellenfrei — ein Gebäude ohne Gebläse. Die partielle Integration
schiebt die Ableitung von der Wolke auf diese Strömung, wo sie nichts mehr findet. Übrig bleibt nur, was durch die Blasenhaut
tritt.

**Schritt 6: Die Blasenhaut mittelt.** Auf der Blasenhaut ist der Radius $\varepsilon$, und die Normalableitung ist überall gleich:

$$\frac{\partial g}{\partial n} = \Big(-\frac{\vec e_r}{4\pi\varepsilon^2}\Big)\cdot\big(-\vec e_r\big) = \frac{1}{4\pi\varepsilon^2} = \frac{1}{\lvert S_\varepsilon\rvert},$$

mit dem Flächeninhalt $\lvert S_\varepsilon\rvert$ der Blasenhaut, $4\pi\varepsilon^2$. Damit ist

$$-\Delta u(\vec x) = \lim_{\varepsilon\searrow0}\frac{1}{\lvert S_\varepsilon\rvert}\int_{S_\varepsilon}f(\vec x-\vec z)\;d\sigma.$$

**So liest man das:** Rechts steht der Mittelwert der Dichte über die Kugeloberfläche vom Radius $\varepsilon$ um den Messpunkt, das
__Kugelmittel__.

**Im Bild:** Die Normalableitung ist die Ausflussdichte der Einheitsquelle durch die Blasenhaut — ihre Schüttung $1$, gleichmäßig
auf die Fläche $4\pi\varepsilon^2$ verteilt. Jedes Hautstück trägt die Dichte dort mit seinem Anteil an der Fläche bei.

**Schritt 7: Die Blase schrumpft.** Das Kugelmittel unterscheidet sich von $f(\vec x)$ höchstens um die größte Abweichung auf der
Blasenhaut:

$$\Big\lvert\frac{1}{\lvert S_\varepsilon\rvert}\int_{S_\varepsilon}f(\vec x-\vec z)\;d\sigma-f(\vec x)\Big\rvert \le \max_{\lvert\vec z\rvert=\varepsilon}\big\lvert f(\vec x-\vec z)-f(\vec x)\big\rvert.$$

Weil $f$ stetig ist, geht die rechte Seite für $\varepsilon\to0$ gegen null. Also ist $-\Delta u(\vec x)=f(\vec x)$ für jeden
Messpunkt, und der Satz ist bewiesen. Das Skript schreibt die Bedingung unter dem Supremum als $\lvert x-y\rvert<\varepsilon$;
gemeint ist, dass der Punkt $\vec x-\vec z$ höchstens $\varepsilon$ vom Messpunkt entfernt ist.

**Im Bild:** Eine winzige Blase sieht nur noch die Dichte am Messpunkt.

:::herleitung
Man schreibt $f(\vec x)$ selbst als Kugelmittel der Konstanten $f(\vec x)$ und zieht ab:

$$\frac{1}{\lvert S_\varepsilon\rvert}\int_{S_\varepsilon}f(\vec x-\vec z)\;d\sigma-f(\vec x) = \frac{1}{\lvert S_\varepsilon\rvert}\int_{S_\varepsilon}\big(f(\vec x-\vec z)-f(\vec x)\big)\;d\sigma.$$

Der Betrag des Integranden ist höchstens das Maximum rechts, und das Integral der Konstanten $1$ über die Blasenhaut ist ihr
Flächeninhalt; er kürzt sich mit dem Faktor davor.
:::

:::grafik
Szene: hoema3/integralsaetze-im-raum/04-blase-um-den-messpunkt · Vorlage: blase-kugelschale-3d
Eine Quellwolke, deren Farbe die Dichte zeigt, und ein Messpunkt in ihr. Um den Messpunkt eine kleine Blase und eine große
Kugel, dazwischen halbdurchsichtig die Kugelschale. Vom Messpunkt aus laufen die Strömungspfeile einer gedachten Einheitsquelle
durch die Schale; ein Zähler zeigt, dass in der Schale nichts entspringt. Auf der Blasenhaut leuchten Flächenstücke in der Farbe
der Dichte dort, ihre Normalenpfeile zeigen zum Messpunkt hin. Ein Regler schrumpft die Blase, und ein zweiter Zähler zeigt das
Kugelmittel der Dichte, das sich dem Wert am Messpunkt nähert. Kernaussage: Die Einheitsquelle verteilt ihre Schüttung gleichmäßig
auf die Blasenhaut; deshalb mittelt der Randterm die Dichte, und eine winzige Blase misst die Dichte am Messpunkt. (Rot = Blase und
Messpunkt, blau = Wolke und Strömungspfeile, orange = Normalenpfeile und Zähler, grau = äußere Kugel, gestrichelt = Schalenrand.)
:::

::::beispiel Die Blase in der glatten Wolke
Die glatte Wolke aus dem Artikel über das Newtonpotential,

$$f(\vec y) = \big(1-\lvert\vec y\rvert^2\big)^2 \quad\text{für } \lvert\vec y\rvert\le1, \qquad f(\vec y) = 0 \quad\text{sonst},$$

erfüllt alle Voraussetzungen; dort wurde $-\Delta u=f$ für sie direkt nachgerechnet. Hier geht es um die Schritte 6 und 7, das
Kugelmittel um den Messpunkt

$$\vec x = \big(\tfrac12,\ 0,\ 0\big), \qquad f(\vec x) = \big(\tfrac34\big)^2 = 0{,}5625.$$

Für Radien bis $\frac12$ liegt die ganze Blasenhaut in der Wolke, und das Kugelmittel ist

$$\frac{1}{\lvert S_\varepsilon\rvert}\int_{S_\varepsilon}f(\vec x-\vec z)\;d\sigma = f(\vec x)-\frac76\,\varepsilon^2+\varepsilon^4.$$

:::herleitung
Auf der Blasenhaut ist $\lvert\vec z\rvert=\varepsilon$, also

$$\lvert\vec x-\vec z\rvert^2 = \frac14-2\,\vec x\cdot\vec z+\varepsilon^2, \qquad f(\vec x-\vec z) = \Big(\frac34-\varepsilon^2+2\,\vec x\cdot\vec z\Big)^2.$$

Ausmultipliziert stehen drei Terme. Im Mittel über die Kugeloberfläche fällt der lineare Term weg, weil mit $\vec z$ auch $-\vec z$
auf ihr liegt. Im quadratischen Term ist $2\,\vec x\cdot\vec z$ hier einfach $z_1$. Die Mittel von $z_1^2$, $z_2^2$ und $z_3^2$ sind aus
Symmetrie gleich und haben zusammen $\varepsilon^2$, jedes ist also $\frac{\varepsilon^2}{3}$. Zusammen mit dem konstanten Term:

$$\Big(\frac34-\varepsilon^2\Big)^2+\frac{\varepsilon^2}{3} = \frac{9}{16}-\frac32\,\varepsilon^2+\varepsilon^4+\frac13\,\varepsilon^2 = f(\vec x)-\frac76\,\varepsilon^2+\varepsilon^4.$$
:::

Schrumpft die Blase, nähert sich das Kugelmittel der Dichte am Messpunkt:

$$\varepsilon = 0{,}1:\ \ 0{,}5509, \qquad \varepsilon = 0{,}01:\ \ 0{,}562\,38, \qquad \varepsilon\to0:\ \ 0{,}5625.$$

Die Schranke aus Schritt 7 ist viel gröber. Auf der Haut vom Radius $0{,}1$ hat die Dichte die Form

$$f(\vec x-\vec z) = \big(0{,}74+z_1\big)^2, \qquad -0{,}1\le z_1\le0{,}1,$$

liegt also zwischen $0{,}4096$ und $0{,}7056$. Die größte Abweichung von $0{,}5625$ ist $0{,}1529$, das Mittel weicht nur um
$0{,}0116$ ab — Abweichungen nach oben und unten heben sich fast auf.

**Im Bild:** Die Abweichung $-\frac76\varepsilon^2$ ist $\frac{\varepsilon^2}{6}$ mal $\Delta f(\vec x)$. Wie beim Mittel der Nachbarn im
Divergenz-Artikel misst der Laplace-Operator, wie weit das Mittel der Umgebung vom Wert in der Mitte abweicht. Die Wolke ist am
Messpunkt nach unten gewölbt, deshalb liegt das Kugelmittel etwas darunter.

:::herleitung
Mit $r=\lvert\vec y\rvert$ ist die Dichte in der Wolke ein Polynom in $r^2$. Nach der radialen Formel für den Laplace-Operator aus
dem ersten Kapitel, Ableitung zweimal plus $\frac2r$ mal Ableitung einmal, ist

$$f = 1-2r^2+r^4, \qquad \Delta\big(r^2\big) = 2+4 = 6, \qquad \Delta\big(r^4\big) = 12r^2+8r^2 = 20\,r^2,$$

$$\Delta f(\vec x) = -12+20\cdot\frac14 = -7, \qquad \frac{\varepsilon^2}{6}\cdot(-7) = -\frac76\,\varepsilon^2.$$
:::
::::

## Was „Greensche Funktion" heißt

Der Satz sagt: Wer das Potential einer beliebigen Quellwolke sucht, muss nur die Antwort auf eine einzige Einheitsquelle kennen.
Das ist die Idee der Greenschen Funktion. Man nennt das Integral

$$(g*f)(\vec x) = \int_{\mathbb{R}^3}g(\vec x-\vec y)\,f(\vec y)\;d^3y$$

die __Faltung__ von $g$ und $f$; das Newtonpotential ist also $g*f$. Eine Funktion heißt __Greensche Funktion__ — auch
__Fundamentallösung__ — des Operators $-\Delta$ im $\mathbb{R}^3$, wenn ihre Faltung mit jeder stetig differenzierbaren Dichte mit
kompaktem Träger die Poisson-Gleichung löst. Nach dem Satz ist das Coulomb-Potential eine solche Funktion; das meint das Skript
mit dem Satz, das Ergebnis identifiziere sie als Greensche Funktion des Laplace-Operators.

**Im Bild:** $g(\vec x-\vec y)$ ist das Potential am Messpunkt $\vec x$, das eine Einheitsquelle am Ort $\vec y$ erzeugt. Weil sich
Strömungen überlagern, ist das Potential der ganzen Wolke die mit der Dichte gewichtete Summe dieser Antworten.

**Die Kurzschrift der Physik.** Physiker schreiben das als

$$-\Delta g = \delta_{\vec 0},$$

mit der __Dirac-Distribution__ $\delta_{\vec 0}$, einer Punktquelle der Stärke $1$ im Ursprung. Als Gleichung zwischen Funktionen ist
das nicht zu lesen: Außerhalb des Ursprungs ist $\Delta g$ null, und im Ursprung ist $g$ nicht einmal definiert. Gemeint ist, dass
die ganze Quellstärke $1$ im Ursprung sitzt. Den genauen Sinn gibt die folgende Formel; das Kapitel über Fourier-Reihen baut die
Idee aus.

**Der Filter.** Für jede zweimal stetig differenzierbare Funktion $f:\mathbb{R}^3\to\mathbb{R}$ mit kompaktem Träger gilt

$$\int_{\mathbb{R}^3}g(\vec y)\,\big(-\Delta f\big)(\vec y)\;d^3y = f(\vec 0).$$

**So liest man das:** Gewichtet man die Größe $-\Delta f$ mit dem Kern und integriert, bleibt nur der Wert von $f$ im Ursprung
übrig — genau das, was die Kurzschrift verspricht.

**Im Bild:** Fasst man $f$ selbst als Potential auf, ist $-\Delta f$ die Dichte seiner Quellen. Die Formel sagt: $f$ ist das
Newtonpotential seiner eigenen Quellen, hier im Ursprung ausgewertet. Wer die Quellen einer Strömung kennt, die weit draußen
ruht, kennt ihr Potential.

:::herleitung
Weil jetzt auch die zweiten Ableitungen von $f$ stetig mit kompaktem Träger sind, darf man in der verschobenen Form beide
Ableitungen des Laplace-Operators auf die Dichte legen, so wie in Schritt 2 die eine:

$$\Delta u(\vec x) = \int_{\mathbb{R}^3}g(\vec z)\,(\Delta f)(\vec x-\vec z)\;d^3z.$$

Nach dem Satz ist das $-f(\vec x)$. Im Ursprung ausgewertet und mit der Substitution $\vec y=-\vec z$, bei der sich $g$ nicht ändert,
weil es nur vom Betrag abhängt:

$$-f(\vec 0) = \int_{\mathbb{R}^3}g(\vec z)\,(\Delta f)(-\vec z)\;d^3z = \int_{\mathbb{R}^3}g(\vec y)\,(\Delta f)(\vec y)\;d^3y.$$

**Im Bild:** Die Ableitungen sitzen jetzt ganz auf der Dichte, und der Kern bleibt ungestört — das geht, weil die Dichte glatt
genug ist.
:::

::::beispiel Der Filter an einer glatteren Wolke
Die Wolke

$$f(\vec y) = \big(1-\lvert\vec y\rvert^2\big)^3 \quad\text{für } \lvert\vec y\rvert\le1, \qquad f(\vec y) = 0 \quad\text{sonst},$$

ist zweimal stetig differenzierbar mit kompaktem Träger: Am Rand der Einheitskugel sind sie und ihre ersten beiden Ableitungen in
radialer Richtung null. Mit $r=\lvert\vec y\rvert$ ist ihr Laplace-Operator in der Kugel

$$-\Delta f = 6\,\big(1-r^2\big)\big(3-7r^2\big).$$

:::herleitung
Die radialen Ableitungen sind

$$f' = -6r\big(1-r^2\big)^2, \qquad f'' = -6\big(1-r^2\big)^2+24r^2\big(1-r^2\big).$$

Nach der radialen Formel, zweite Ableitung plus $\frac2r$ mal erste:

$$\Delta f = -18\big(1-r^2\big)^2+24r^2\big(1-r^2\big) = \big(1-r^2\big)\big(42r^2-18\big) = -6\big(1-r^2\big)\big(3-7r^2\big).$$
:::

Der Filter, in Kugelschalen gerechnet und mit der Substitution $v=r^2$:

$$\int_{K_1(\vec 0)}g\,\big(-\Delta f\big)\;d^3y = \int_0^1\frac{1}{4\pi r}\,6\big(1-r^2\big)\big(3-7r^2\big)\,4\pi r^2\;dr = 3\int_0^1(1-v)(3-7v)\;dv,$$

$$3\int_0^1\big(3-10v+7v^2\big)\;dv = 3\Big(3-5+\frac73\Big) = 1 = f(\vec 0).$$

Dabei heben sich Quellen und Senken insgesamt auf:

$$\int_{K_1(\vec 0)}\big(-\Delta f\big)\;d^3y = 24\pi\int_0^1\big(3r^2-10r^4+7r^6\big)\;dr = 24\pi\,(1-2+1) = 0.$$

**Im Bild:** Die Quelldichte $-\Delta f$ ist innen positiv und in der äußeren Schale, für $r^2>\frac37$, negativ: Quellen in der
Mitte, Senken außen, insgesamt gleich viel. Der Kern gewichtet die nahen Quellen stärker als die fernen Senken, und heraus kommt
genau der Wert $1$ in der Mitte.
::::

## Der Hauptsatz der Vektoranalysis

Zurück zur Badewanne: Lässt sich jede Strömung in eine Quellen- und eine Wirbelströmung zerlegen? Ein __Gradientenfeld__ ist ein
Feld der Form $\nabla u$ mit einem Skalarfeld $u$, ein __Rotationsfeld__ oder Wirbelfeld eines der Form $\operatorname{rot}\vec A$ mit
einem Vektorfeld $\vec A$, seinem __Vektorpotential__ — beides wie im Poincaré-Artikel.

**Die Akteure:** ein zweimal stetig differenzierbares Vektorfeld $\vec F:\mathbb{R}^3\to\mathbb{R}^3$ mit kompaktem Träger; außerhalb
einer Kugel ist es null. Der Satz 5.19 des Skripts, die __Helmholtz-Zerlegung__, sagt: Es gibt zweimal stetig differenzierbare
Felder $u:\mathbb{R}^3\to\mathbb{R}$ und $\vec A:\mathbb{R}^3\to\mathbb{R}^3$ mit

:::formel Satz
$$\vec F = \nabla u+\operatorname{rot}\vec A.$$
:::

**So liest man das:** Jedes solche Feld ist die Summe eines Gradientenfelds und eines Rotationsfelds. $u$ nimmt einen Punkt und
gibt eine Zahl aus, $\vec A$ nimmt einen Punkt und gibt einen Vektor aus. Das Skript schreibt die Rotation als $\nabla\times\vec A$.

**Im Bild:** Die Strömung $\vec F$ ist eine Quellenströmung $\nabla u$ plus eine Wirbelströmung $\operatorname{rot}\vec A$.

**Die Arbeitsteilung.** Gradientenfelder wirbeln nicht, Wirbelfelder sind quellenfrei. Deshalb teilen die beiden Anteile die
Quellen und die Wirbel von $\vec F$ restlos unter sich auf:

$$\operatorname{div}\vec F = \Delta u, \qquad \operatorname{rot}\vec F = \operatorname{rot}\operatorname{rot}\vec A.$$

**Im Bild:** Alle Quellen der Strömung stecken in der Quellenströmung, alle Strudel in der Wirbelströmung.

:::herleitung
Nach dem Satz von Schwarz gilt für zweimal stetig differenzierbare Felder, wie im Rechenregeln-Artikel,

$$\operatorname{rot}\nabla u = \vec 0, \qquad \operatorname{div}\operatorname{rot}\vec A = 0.$$

In jeder Komponente von $\operatorname{rot}\nabla u$ steht eine Differenz wie $\partial_2\partial_3u-\partial_3\partial_2u$, und in
$\operatorname{div}\operatorname{rot}\vec A$ heben sich die gemischten Ableitungen paarweise auf. Man wendet Divergenz und Rotation
auf die Zerlegung an:

$$\operatorname{div}\vec F = \operatorname{div}\nabla u+\operatorname{div}\operatorname{rot}\vec A = \Delta u, \qquad \operatorname{rot}\vec F = \operatorname{rot}\nabla u+\operatorname{rot}\operatorname{rot}\vec A = \operatorname{rot}\operatorname{rot}\vec A.$$
:::

::::beispiel Eine Spiralströmung
Das Feld

$$\vec F(\vec x) = \big(-x_1-x_2,\ x_1-x_2,\ 0\big), \qquad \vec x\in\mathbb{R}^3,$$

strömt in jeder Ebene quer zur $x_3$-Achse spiralförmig nach innen, wie im Abfluss einer Badewanne. Es zerfällt sichtbar in

$$\nabla u = \big(-x_1,\ -x_2,\ 0\big), \qquad \operatorname{rot}\vec A = \big(-x_2,\ x_1,\ 0\big),$$

mit den Potentialen

$$u(\vec x) = -\frac{x_1^2+x_2^2}{2}, \qquad \vec A(\vec x) = \Big(0,\ 0,\ -\frac{x_1^2+x_2^2}{2}\Big).$$

Probe der Rotation, komponentenweise:

$$\operatorname{rot}\vec A = \big(\partial_2A_3-\partial_3A_2,\ \partial_3A_1-\partial_1A_3,\ \partial_1A_2-\partial_2A_1\big) = \big(-x_2,\ x_1,\ 0\big).$$

Die Arbeitsteilung:

$$\operatorname{div}\vec F = -2 = \Delta u, \qquad \operatorname{rot}\vec F = (0,\ 0,\ 2) = \operatorname{rot}\big(-x_2,\ x_1,\ 0\big).$$

Das Feld ruht weit draußen nicht. Der Satz garantiert hier nichts, aber die Zerlegung lässt sich ablesen — und sie ist hier
nicht die einzige, wie der Abschnitt über Eindeutigkeit zeigt.

**Im Bild:** Überall versickert Wasser gleichmäßig, mit der Quelldichte $-2$, und alles kreist wie ein starrer Körper mit der
Wirbelstärke $2$. Zieht man das Kreisen ab, fließt das Wasser geradewegs zur Achse; zieht man den Zufluss ab, kreist es nur.
::::

**Das Zusammenspiel:** *Wie trennt man die Quellen von den Wirbeln?* Man berechnet zuerst die Quellenströmung; was übrig bleibt,
ist quellenfrei.

**Schritt 1: Die Quellenströmung.** Weil $\vec F$ zweimal stetig differenzierbar ist mit kompaktem Träger, ist
$\operatorname{div}\vec F$ stetig differenzierbar mit kompaktem Träger. Nach dem Poisson-Satz, angewandt auf die Dichte
$-\operatorname{div}\vec F$, ist das Newtonpotential

$$u(\vec x) = -\int_{\mathbb{R}^3}g(\vec x-\vec y)\,\operatorname{div}\vec F(\vec y)\;d^3y$$

zweimal stetig differenzierbar und löst

$$\Delta u = \operatorname{div}\vec F.$$

**Im Bild:** Die Quellen von $\vec F$ haben die Dichte $\operatorname{div}\vec F$. Ihre Strömung ist minus der Gradient ihres
Newtonpotentials — und das ist genau $\nabla u$, die Strömung, die die Quellen allein erzeugen würden.

:::herleitung
$u$ ist das Newtonpotential der Dichte $-\operatorname{div}\vec F$. Der Poisson-Satz gibt deshalb

$$-\Delta u = -\operatorname{div}\vec F,$$

und das ist die Gleichung oben.
:::

**Schritt 2: Der Rest ist quellenfrei.** Zieht man die Quellenströmung ab, ist

$$\operatorname{div}\big(\vec F-\nabla u\big) = \operatorname{div}\vec F-\Delta u = 0.$$

**Im Bild:** Ohne die Quellenströmung entspringt nirgends mehr Wasser.

**Schritt 3: Poincaré.** Der ganze Raum ist ein Sterngebiet: Von einem Aussichtsturm im Ursprung aus sieht man jeden Punkt. Nach
dem Poincaré-Lemma hat das quellenfreie, stetig differenzierbare Restfeld dort ein Vektorpotential,

$$\vec F-\nabla u = \operatorname{rot}\vec A, \qquad \vec A(\vec x) = \int_0^1\big(\vec F-\nabla u\big)(t\vec x)\times t\vec x\;dt.$$

Zusammen ist das die Zerlegung des Satzes.

**Im Bild:** Vom Turm aus sammelt man längs jeder Sichtlinie Feld mal Hebelarm. So entsteht die Strömung, deren Wirbelbild der
quellenfreie Rest ist.

**Schritt 4: Glattheit.** Die Formel zeigt: $\vec A$ ist mindestens so oft stetig differenzierbar wie das Restfeld
$\vec F-\nabla u$; das Skript verweist dafür auf das Ableiten unter dem Integral, Satz 2.1. Vom Restfeld weiß man nach dem
Poisson-Satz aber zunächst nur, dass es einmal stetig differenzierbar ist — $u$ ist zweimal stetig differenzierbar, $\nabla u$ also
einmal. Damit ist $\vec A$ sicher einmal stetig differenzierbar. Dass es sogar ein zweimal stetig differenzierbares
Vektorpotential gibt, wie der Satz behauptet, zeigt der nächste Abschnitt ausdrücklich.

## Die Potentiale ausdrücklich

Es geht auch ohne Poincaré-Lemma, und dann sieht man, **woraus** die beiden Potentiale bestehen. Man wendet die Poisson-Lösung auf
jede Komponente von $\vec F$ an, also auf das Feld selbst:

$$\vec Z(\vec x) = \int_{\mathbb{R}^3}g(\vec x-\vec y)\,\vec F(\vec y)\;d^3y, \qquad \vec x\in\mathbb{R}^3.$$

Das Integral ist komponentenweise gemeint; $\vec Z$ nimmt einen Punkt und gibt einen Vektor aus. Die Potentiale der Zerlegung
sind dann

$$u = -\operatorname{div}\vec Z, \qquad \vec A = \operatorname{rot}\vec Z,$$

ausgeschrieben

:::formel
$$u(\vec x) = -\int_{\mathbb{R}^3}g(\vec x-\vec y)\,\operatorname{div}\vec F(\vec y)\;d^3y, \qquad \vec A(\vec x) = \int_{\mathbb{R}^3}g(\vec x-\vec y)\,\operatorname{rot}\vec F(\vec y)\;d^3y.$$
:::

Beide sind zweimal stetig differenzierbar, sie zerlegen $\vec F$ wie im Satz, und $\vec A$ ist von selbst quellenfrei. Das $u$ ist
dasselbe wie im Beweis des Skripts.

**So liest man das:** $u$ ist minus das Newtonpotential der Quelldichte $\operatorname{div}\vec F$, $\vec A$ komponentenweise das
Newtonpotential der __Wirbeldichte__ $\operatorname{rot}\vec F$. Das Feld ist aus seinen Quellen und Wirbeln vollständig
zurückgewonnen.

**Im Bild:** Die Quellen erzeugen die Quellenströmung, die Strudel die Wirbelströmung — beide über dieselbe Einheitsquelle $g$. Ein
Strudel bewegt das Wasser in seiner Umgebung so, wie ein elektrischer Strom ein Magnetfeld um sich erzeugt.

:::herleitung
**Schritt 1: $\vec Z$ löst die Poisson-Gleichung.** Jede Komponente $F_j$ ist stetig differenzierbar mit kompaktem Träger. Nach
dem Poisson-Satz, komponentenweise angewandt, ist

$$-\Delta\vec Z = \vec F.$$

Außerdem darf man jede Ableitung von $\vec Z$ auf $\vec F$ legen, wie in Schritt 2 des Poisson-Beweises die zweite: $\partial_kZ_j$
ist das Newtonpotential von $\partial_kF_j$. Diese Dichte ist wieder stetig differenzierbar mit kompaktem Träger, also ist
$\partial_kZ_j$ nach dem Poisson-Satz zweimal stetig differenzierbar — und $\vec Z$ dreimal.

**Schritt 2: rot rot.** Für zweimal stetig differenzierbare Felder gilt nach dem Rechenregeln-Artikel

$$\operatorname{rot}\operatorname{rot}\vec Z = \nabla\big(\operatorname{div}\vec Z\big)-\Delta\vec Z.$$

Also ist

$$\vec F = -\Delta\vec Z = \operatorname{rot}\big(\operatorname{rot}\vec Z\big)+\nabla\big(-\operatorname{div}\vec Z\big) = \operatorname{rot}\vec A+\nabla u.$$

**Schritt 3: Ableitungen nach innen.** Weil $\partial_kZ_j$ das Newtonpotential von $\partial_kF_j$ ist, sind
$\operatorname{div}\vec Z$ und $\operatorname{rot}\vec Z$ die Newtonpotentiale von $\operatorname{div}\vec F$ und
$\operatorname{rot}\vec F$ — das sind die ausgeschriebenen Formeln. Als Ableitungen des dreimal stetig differenzierbaren $\vec Z$
sind $u$ und $\vec A$ zweimal stetig differenzierbar.

**Schritt 4: Von selbst quellenfrei.** Nach dem Satz von Schwarz ist

$$\operatorname{div}\vec A = \operatorname{div}\operatorname{rot}\vec Z = 0.$$

Das $u$ ist das Newtonpotential von $-\operatorname{div}\vec F$, also dasselbe wie in Schritt 1 des Skript-Beweises.

**Im Bild:** $\vec Z$ ist das Potential der ganzen Strömung, Komponente für Komponente. Divergenz und Rotation sortieren daraus die
Quellen und die Strudel.
:::

::::beispiel Ein Strahl in einer Kugel
Mit der glatteren Wolke vom Filter als Profil sei

$$\vec F(\vec x) = f(\vec x)\,\vec e_3, \qquad f(\vec x) = \big(1-\lvert\vec x\rvert^2\big)^3 \quad\text{für } \lvert\vec x\rvert\le1, \qquad f = 0 \quad\text{sonst}.$$

Das ist ein Strahl, der in der Einheitskugel nach oben schießt, in der Mitte am stärksten; außerhalb ruht das Wasser. Das Feld
ist zweimal stetig differenzierbar mit kompaktem Träger.

**(a) Quellen und Wirbel.** Mit dem konstanten Vektor $\vec e_3$ ist

$$\operatorname{div}\vec F = \partial_3 f, \qquad \operatorname{rot}\vec F = \nabla f\times\vec e_3 = \big(\partial_2 f,\ -\partial_1 f,\ 0\big).$$

In der unteren Kugelhälfte nimmt $f$ nach oben zu; dort ist $\partial_3f$ positiv, dort entspringt Wasser. In der oberen Hälfte
versickert es. Die Wirbeldichte kreist um die $x_3$-Achse, von oben gesehen gegen den Uhrzeigersinn: ein __Wirbelring__, die
Scherung zwischen dem schnellen Kern und dem ruhenden Rand.

:::herleitung
Die Produktregeln für ein Skalarfeld mal ein Vektorfeld aus dem Rechenregeln-Artikel geben, weil der konstante Vektor $\vec e_3$
weder Quellen noch Wirbel hat,

$$\operatorname{div}\big(f\,\vec e_3\big) = \nabla f\cdot\vec e_3 = \partial_3f, \qquad \operatorname{rot}\big(f\,\vec e_3\big) = \nabla f\times\vec e_3.$$

Mit dem radialen Profil ist $\nabla f$ die Ableitung $f'(r)$ mal $\vec e_r$, und $f'$ ist in der Kugel negativ:

$$\nabla f\times\vec e_3 = \frac{f'(r)}{r}\,\big(x_2,\ -x_1,\ 0\big) = \frac{\lvert f'(r)\rvert}{r}\,\big(-x_2,\ x_1,\ 0\big).$$

Das Feld $(-x_2,\,x_1,\,0)$ kreist von oben gesehen gegen den Uhrzeigersinn um die $x_3$-Achse.
:::

**(b) Die Potentiale.** Mit dem Newtonpotential $w$ der Dichte $f$ ist $\vec Z=w\,\vec e_3$, also

$$u = -\partial_3 w, \qquad \vec A = \operatorname{rot}\big(w\,\vec e_3\big) = \big(\partial_2 w,\ -\partial_1 w,\ 0\big).$$

Probe mit der komponentenweisen Rotation und der Poisson-Gleichung für $w$:

$$\nabla u = \big(-\partial_1\partial_3w,\ -\partial_2\partial_3w,\ -\partial_3^2w\big), \qquad \operatorname{rot}\vec A = \big(\partial_1\partial_3w,\ \partial_2\partial_3w,\ -\partial_1^2w-\partial_2^2w\big),$$

$$\nabla u+\operatorname{rot}\vec A = \big(0,\ 0,\ -\Delta w\big) = f\,\vec e_3.$$

**Im Bild:** Die Quellenströmung schiebt das Wasser von den Quellen unten zu den Senken oben; die Wirbelströmung ist das Kreisen,
das der Wirbelring antreibt. Zusammen ergeben sie den Strahl.

:::grafik
Szene: hoema3/integralsaetze-im-raum/04-strahl-in-der-kugel · Vorlage: helmholtz-strahl-3d
Ein Schnitt durch die Einheitskugel längs der $x_3$-Achse. Links der Strahl $\vec F$ als senkrechte Pfeile, in der Mitte am
längsten; unten Quellpunkte, oben Senkenpunkte, dazu der Wirbelring als zwei gegenläufig drehende Kreise im Schnitt. Ein Regler
zerlegt das Bild in zwei Felder nebeneinander: die Quellenströmung $\nabla u$, die von den Quellen unten zu den Senken oben läuft,
innen wie außen herum, wie ein elektrisches Dipolfeld; und die Wirbelströmung $\operatorname{rot}\vec A$, die durch den Ring nach
oben und außen herum nach unten läuft, wie das Magnetfeld einer Leiterschleife. Ein zweiter Regler überlagert beide wieder, und
außerhalb der Kugel löschen sie sich aus. Kernaussage: Quellen und Wirbelring zusammen ergeben den Strahl, und draußen heben
sich ihre Strömungen auf. (Rot = Quellen, Senken und Wirbelring, blau = Strahl, orange = die beiden Anteile, grau = Kugelrand und
Achse.)
:::
::::

**Die Anteile reichen über das Feld hinaus.** Auch wenn $\vec F$ außerhalb einer Kugel null ist, sind es $\nabla u$ und
$\operatorname{rot}\vec A$ im Allgemeinen nicht. Dort heben sie sich auf:

$$\nabla u = -\operatorname{rot}\vec A \quad\text{außerhalb des Trägers von } \vec F.$$

**Im Bild:** Die Quellen allein würden auch das Wasser draußen bewegen, ebenso die Strudel allein. Erst beide zusammen lassen es
dort ruhen.

:::herleitung
Außerhalb des Trägers ist $\vec F$ null, und die Zerlegung gibt dort $\vec 0=\nabla u+\operatorname{rot}\vec A$. Dass die Anteile
dort tatsächlich nicht null sein müssen, zeigt der Strahl.
:::

::::beispiel Außerhalb des Strahls
Außerhalb der Einheitskugel wirkt die Wolke $f$ des Strahls nach dem Schalentheorem aus dem Artikel über das Newtonpotential wie
eine Punktladung. Mit ihrer Gesamtladung $Q$ ist dort

$$w(\vec x) = \frac{Q}{4\pi\lvert\vec x\rvert} = \frac{q}{\lvert\vec x\rvert}, \qquad q = \frac{Q}{4\pi} = \int_0^1\big(1-r^2\big)^3r^2\;dr = \frac{16}{315}.$$

Damit sind die Potentiale draußen

$$u(\vec x) = q\,\frac{x_3}{\lvert\vec x\rvert^3}, \qquad \vec A(\vec x) = \frac{q}{\lvert\vec x\rvert^3}\,\big(-x_2,\ x_1,\ 0\big).$$

Über der Kugel, im Punkt $(0,0,2)$, sind beide Anteile nicht null:

$$\nabla u = -\frac q4\,\vec e_3, \qquad \operatorname{rot}\vec A = \frac q4\,\vec e_3, \qquad \frac q4 = \frac{4}{315}\approx0{,}0127.$$

:::herleitung
**Die Ladung.** Ausmultipliziert ist der Integrand ein Polynom:

$$\int_0^1\big(r^2-3r^4+3r^6-r^8\big)\;dr = \frac13-\frac35+\frac37-\frac19 = \frac{16}{315}.$$

**Die Potentiale.** Mit den Ableitungen von $\frac{1}{\lvert\vec x\rvert}$, nämlich $-\frac{x_k}{\lvert\vec x\rvert^3}$, folgen $u$ als
$-\partial_3w$ und $\vec A$ als $(\partial_2w,\,-\partial_1w,\,0)$.

**Im Punkt $(0,0,2)$.** Der Gradient von $u$ ist nach der Produktregel

$$\nabla u = q\,\Big(\frac{\vec e_3}{\lvert\vec x\rvert^3}-\frac{3x_3\,\vec x}{\lvert\vec x\rvert^5}\Big) = q\,\Big(\frac18-\frac{12}{32}\Big)\,\vec e_3 = -\frac q4\,\vec e_3.$$

Von der Rotation zählt auf der Achse nur die dritte Komponente; die anderen beiden enthalten den Faktor $x_1$ bzw. $x_2$:

$$\big(\operatorname{rot}\vec A\big)_3 = \partial_1\Big(\frac{q\,x_1}{\lvert\vec x\rvert^3}\Big)+\partial_2\Big(\frac{q\,x_2}{\lvert\vec x\rvert^3}\Big) = q\,\Big(\frac{2}{\lvert\vec x\rvert^3}-\frac{3\,(x_1^2+x_2^2)}{\lvert\vec x\rvert^5}\Big) = \frac{2q}{8} = \frac q4.$$
:::

**Im Bild:** Über der Kugel zieht die Quellenströmung das Wasser nach unten, zu den Senken in der oberen Kugelhälfte. Der
Wirbelring schiebt es gleich stark nach oben, so wie ein Rauchring Luft durch seine Mitte treibt. Zusammen ruht das Wasser. Die
Formen sind die eines elektrischen und eines magnetischen Dipols — draußen sehen beide Felder gleich aus.
::::

## Eichung

Das Vektorpotential ist nie eindeutig. Mit jedem zweimal stetig differenzierbaren Skalarfeld $\chi:\mathbb{R}^3\to\mathbb{R}$ ist auch
$\vec A+\nabla\chi$ eines — die __Eichfreiheit__ aus dem Poincaré-Artikel. Rotation und Divergenz ändern sich dabei so:

$$\operatorname{rot}\big(\vec A+\nabla\chi\big) = \operatorname{rot}\vec A, \qquad \operatorname{div}\big(\vec A+\nabla\chi\big) = \operatorname{div}\vec A+\Delta\chi.$$

Wie in Bemerkung 3.18 des Skripts erreicht man deshalb die __Coulomb-Eichung__, ein quellenfreies Vektorpotential, indem man $\chi$
als Lösung der Poisson-Gleichung

$$\Delta\chi = -\operatorname{div}\vec A$$

wählt. Das ist dieselbe Aufgabe wie für $u$: Ist $\operatorname{div}\vec A$ stetig differenzierbar mit kompaktem Träger, löst sie das
Newtonpotential von $\operatorname{div}\vec A$. So beantwortet sich die Frage, die der Poincaré-Artikel offen gelassen hat. Das
Potential aus den ausdrücklichen Formeln braucht keine Eichung mehr — es ist schon quellenfrei.

**Im Bild:** Ein Gradientenfeld zu $\vec A$ zu addieren heißt, eine wirbelfreie Strömung hinzuzufügen; das Wirbelbild bleibt
dasselbe. Die Eichung wählt unter allen Potentialen eines ohne Quellen.

:::herleitung
Nach dem Satz von Schwarz wirbelt ein Gradientenfeld nicht, und die Divergenz eines Gradienten ist der Laplace-Operator:

$$\operatorname{rot}\nabla\chi = \vec 0, \qquad \operatorname{div}\nabla\chi = \Delta\chi.$$

Mit der Wahl von $\chi$ heben sich die beiden Terme der Divergenz auf. Das Newtonpotential von $\operatorname{div}\vec A$ ist nach dem
Poisson-Satz eine Lösung, denn

$$-\Delta\Big(\int_{\mathbb{R}^3}g(\vec x-\vec y)\,\operatorname{div}\vec A(\vec y)\;d^3y\Big) = \operatorname{div}\vec A(\vec x).$$
:::

::::beispiel Eichen nach dem Turm
Die Wirbelströmung der Spirale, $(-x_2,\,x_1,\,0)$, hat vom Turm im Ursprung aus das Vektorpotential des Poincaré-Lemmas. Der
Integrand ist $t^2$ mal das Kreuzprodukt des Felds mit $\vec x$:

$$\vec A_T(\vec x) = \int_0^1 t^2\,\big(-x_2,\ x_1,\ 0\big)\times\vec x\;dt = \frac13\,\big(x_1x_3,\ x_2x_3,\ -x_1^2-x_2^2\big).$$

Es hat dieselbe Rotation wie das Potential aus der Spirale, aber Quellen:

$$\operatorname{rot}\vec A_T = \big(-x_2,\ x_1,\ 0\big), \qquad \operatorname{div}\vec A_T = \frac23\,x_3.$$

Die Eichung verlangt eine Lösung von

$$\Delta\chi = -\frac23\,x_3, \qquad \chi(\vec x) = -\frac{x_3^3}{9}, \qquad \vec A_T+\nabla\chi = \frac13\,\big(x_1x_3,\ x_2x_3,\ -\lvert\vec x\rvert^2\big).$$

Hier errät man die Lösung; für Daten mit kompaktem Träger liefert sie das Newtonpotential. Die Divergenz des neuen Potentials ist
$\frac13\,(x_3+x_3-2x_3)$, also null. Auch das Potential aus der Spirale, $(0,\,0,\,-\frac{x_1^2+x_2^2}{2})$, ist quellenfrei und hat
dieselbe Rotation — ohne Abklingen legt selbst die Coulomb-Eichung das Vektorpotential nicht fest.

:::herleitung
**Das Kreuzprodukt.** Komponentenweise ist

$$\big(-x_2,\ x_1,\ 0\big)\times\big(x_1,\ x_2,\ x_3\big) = \big(x_1x_3,\ x_2x_3,\ -x_2^2-x_1^2\big),$$

und das Integral von $t^2$ über $[0,1]$ ist $\frac13$.

**Rotation und Divergenz** von $\vec A_T$, komponentenweise:

$$\operatorname{rot}\vec A_T = \frac13\,\big(-2x_2-x_2,\ x_1+2x_1,\ 0\big), \qquad \operatorname{div}\vec A_T = \frac13\,\big(x_3+x_3\big).$$

**Die Eichfunktion.** Der Laplace-Operator von $x_3^3$ ist $6x_3$, also hat $\chi$ den Laplace-Operator $-\frac69x_3$, und ihr
Gradient ist $(0,\,0,\,-\frac{x_3^2}{3})$.
:::

**Im Bild:** Vom Turm aus gebaut, hat das Potential oben Quellen und unten Senken. Das Gradientenfeld von $\chi$ saugt sie ab, ohne
am Wirbelbild etwas zu ändern.
::::

## Ist die Zerlegung eindeutig?

Das Skript sagt nur, dass es eine Zerlegung **gibt**. Eindeutig ist sie ohne Zusatzbedingung nicht. Hat $\vec F$ zwei Zerlegungen,
mit $u_1,\vec A_1$ und mit $u_2,\vec A_2$, so ist ihre Differenz

$$\vec H = \nabla u_1-\nabla u_2 = \operatorname{rot}\vec A_2-\operatorname{rot}\vec A_1$$

zugleich ein Gradientenfeld und ein Rotationsfeld, also wirbelfrei und quellenfrei. Nach dem Poincaré-Artikel ist es dann
__harmonisch__: Jede Komponente erfüllt die Laplace-Gleichung. Solche Felder gibt es, etwa jedes konstante Feld.

**Im Bild:** Eine gleichmäßige Strömung, die den ganzen Raum durchzieht, hat weder Quellen noch Strudel. Nichts verrät, ob sie zur
Quellen- oder zur Wirbelströmung gehört.

:::herleitung
Zieht man die beiden Zerlegungen voneinander ab, steht links ein Gradient und rechts eine Rotation:

$$\nabla\big(u_1-u_2\big) = \operatorname{rot}\big(\vec A_2-\vec A_1\big).$$

Als Gradient wirbelt $\vec H$ nicht, als Rotation hat es keine Quellen — beides nach dem Satz von Schwarz.
:::

::::beispiel Ein Feld, zwei Zerlegungen
Ein konstantes Feld $\vec c\in\mathbb{R}^3$ ist ganz Quellenströmung und zugleich ganz Wirbelströmung:

$$\vec c = \nabla\big(\vec c\cdot\vec x\big), \qquad \vec c = \operatorname{rot}\Big(\frac12\,\vec c\times\vec x\Big).$$

Für $\vec c=(0,0,2)$ ist das zweite Potential das kreisende $(-x_2,\,x_1,\,0)$ aus dem Poincaré-Artikel. Bei der Spiralströmung kann
man deshalb ein konstantes Feld zur Quellenströmung addieren und von der Wirbelströmung abziehen — eine zweite Zerlegung
desselben Felds.

:::herleitung
Der Gradient von $c_1x_1+c_2x_2+c_3x_3$ ist $(c_1,\,c_2,\,c_3)$. Für die Rotation, am Beispiel $\vec c=(0,0,2)$:

$$\frac12\,(0,\ 0,\ 2)\times\big(x_1,\ x_2,\ x_3\big) = \big(-x_2,\ x_1,\ 0\big), \qquad \operatorname{rot}\big(-x_2,\ x_1,\ 0\big) = (0,\ 0,\ 2).$$

Für ein beliebiges konstantes Feld zeigt der Poincaré-Artikel dasselbe mit der Formel vom Turm.
:::

**Im Bild:** Ein gleichmäßiger Strom ist das Gefälle einer schiefen Ebene und zugleich das Wirbelbild eines starr kreisenden Felds.
::::

**Mit Abklingen eindeutig.** Verlangt man, dass beide Anteile im Unendlichen gegen null gehen, bleibt nur das Nullfeld; das Skript
führt das nicht aus. Die Anteile aus den ausdrücklichen Formeln erfüllen die Bedingung: Wie im Fernfeld des Newtonpotentials
fallen sie mindestens wie $\frac{1}{\lvert\vec x\rvert^2}$ ab. Die Beweisidee benutzt wieder ein Kugelmittel. Für eine harmonische
Funktion $h$ ist das Mittel über jede Kugeloberfläche um einen Punkt gleich dem Wert in der Mitte, die __Mittelwerteigenschaft__:

$$h(\vec x) = \frac{1}{\lvert\partial K_R(\vec x)\rvert}\int_{\partial K_R(\vec x)}h\;d\sigma \qquad\text{für jeden Radius } R>0.$$

Für die Komponenten von $\vec H$ und einen sehr großen Radius liegt die ganze Kugeloberfläche weit draußen, wo die Komponenten
beliebig klein sind. Also ist jede Komponente null.

**Im Bild:** Eine Strömung ohne Quellen und Strudel, die weit draußen zur Ruhe kommt, hat nichts, was sie antreibt — sie ruht
überall.

:::herleitung
**Das Abklingen.** Liegt der Träger von $\vec F$ in $K_{R_0}(\vec 0)$, ist für $\lvert\vec x\rvert>R_0$ der Abstand zu jedem Punkt des
Trägers mindestens $\lvert\vec x\rvert-R_0$. Mit Schritt 2 des Poisson-Beweises folgt

$$\lvert\nabla u(\vec x)\rvert \le \int_{K_{R_0}(\vec 0)}\lvert\nabla g(\vec x-\vec y)\rvert\,\lvert\operatorname{div}\vec F(\vec y)\rvert\;d^3y \le \frac{1}{4\pi\,(\lvert\vec x\rvert-R_0)^2}\int_{K_{R_0}(\vec 0)}\lvert\operatorname{div}\vec F\rvert\;d^3y,$$

und genauso für $\operatorname{rot}\vec A$ mit $\operatorname{rot}\vec F$ statt $\operatorname{div}\vec F$.

**Die Mittelwerteigenschaft.** Sei $m(R)$ das Kugelmittel von $h$ über die Kugeloberfläche vom Radius $R$ um $\vec x$. Schreibt
man ihre Punkte als $\vec x+R\,\vec\omega$ mit Einheitsvektoren $\vec\omega$, hängt nur noch der Integrand von $R$ ab, und
Ableiten unter dem Integral gibt das Mittel der Normalableitung:

$$m'(R) = \frac{1}{\lvert\partial K_R(\vec x)\rvert}\int_{\partial K_R(\vec x)}\frac{\partial h}{\partial n}\;d\sigma = \frac{1}{\lvert\partial K_R(\vec x)\rvert}\int_{K_R(\vec x)}\Delta h\;d^3y = 0.$$

Das zweite Gleichheitszeichen ist der Satz von Gauß für das Feld $\nabla h$. Also ist $m$ konstant, und für $R\to0$ strebt es wie
in Schritt 7 gegen $h(\vec x)$.

**Glatt genug.** Hier ist $\vec H$ der Gradient der harmonischen Funktion $u_1-u_2$. Dass dessen Komponenten wieder harmonisch sind,
sichert ein Satz über harmonische Funktionen jenseits des Kurses: Sie sind automatisch beliebig oft differenzierbar.
:::

## Schwächere Voraussetzungen

Der kompakte Träger ist bequem, aber nicht nötig. Laut Skript genügt die Abklingbedingung

$$\vec F(\vec x) = o\Big(\frac{1}{\lvert\vec x\rvert^2}\Big) \quad\text{für } \lvert\vec x\rvert\to\infty.$$

Das heißt: $\lvert\vec x\rvert^2\,\lvert\vec F(\vec x)\rvert$ geht gegen null, das Feld fällt schneller ab als $\frac{1}{\lvert\vec x\rvert^2}$.
Die Bedingung sichert die Konvergenz der Integrale aus dem Poisson-Satz. Für beliebig oft differenzierbare Felder genügt sogar
irgendein Abklingen von $\vec F$ samt aller Ableitungen; das bewies 1905 Otto Blumenthal, Mathematikprofessor an der RWTH Aachen.
Beide Abschwächungen nennt das Skript ohne Beweis, sie gehen über den Kurs hinaus.

**Im Bild:** Die Strömung muss weit draußen nicht ruhen, aber schnell genug abflauen. Sonst summieren sich die fernen Quellen und
Strudel nicht mehr zu endlichen Potentialen.

::::beispiel Ohne Abklingen keine Formel
**(a) Eine konstante Dichte.** Ist die Dichte überall $1$, liefert schon die Kugel vom Radius $R$ um den Messpunkt den Beitrag

$$\int_{K_R(\vec x)}g(\vec x-\vec y)\;d^3y = \frac{R^2}{2} \to \infty \quad\text{für } R\to\infty.$$

Das Integral über den ganzen Raum existiert nicht. Dabei hat die Poisson-Gleichung Lösungen, etwa

$$u(\vec x) = -\frac{\lvert\vec x\rvert^2}{6}, \qquad -\Delta u = \frac{6}{6} = 1.$$

Die Formel findet sie nur nicht.

**(b) Ein konstantes Feld** fällt gar nicht ab. Für $\vec Z$ divergiert das Integral aus demselben Grund, und die Zerlegung ist, wie
gesehen, nicht eindeutig.

:::herleitung
Nach Schritt 1 des Poisson-Beweises ist das Integral über $K_R(\vec x)$ dasselbe wie das Integral von $g$ über $K_R(\vec 0)$, und das
ist nach der Rechnung zur Integrierbarkeit $\frac{R^2}{2}$. Für die Lösung: Der Laplace-Operator von $\lvert\vec x\rvert^2$ ist $6$, je
$2$ aus jeder Koordinate.
:::

**Im Bild:** Eine Quelldichte, die den ganzen Raum füllt, schüttet unendlich viel Wasser aus. Jede Kugelschale vom Radius $s$ und der
Dicke $ds$ trägt zum Potential im Mittelpunkt $s\,ds$ bei, und die Summe wächst ohne Grenze.
::::

## Bedeutung und Ausblick

Mit diesem Artikel ist die Potentialtheorie der Feldphysik beisammen. In der Elektrostatik hat das elektrische Feld nur Quellen,
in der Magnetostatik das Magnetfeld nur Wirbel. Mit der Ladungsdichte $\rho$, der Stromdichte $\vec J$ und den Feldkonstanten
$\varepsilon_0$ und $\mu_0$ lauten die Maxwell-Gleichungen der Statik

$$\operatorname{rot}\vec E = \vec 0, \qquad \operatorname{div}\vec E = \frac{\rho}{\varepsilon_0}, \qquad \operatorname{div}\vec B = 0, \qquad \operatorname{rot}\vec B = \mu_0\,\vec J.$$

Setzt man sie in die ausdrücklichen Formeln ein, bekommt $\vec E$ nur einen Quellenanteil und $\vec B$ nur einen Wirbelanteil. Es
entstehen die beiden Grundformeln der Potentialrechnung, mit dem elektrischen Potential und dem magnetischen Vektorpotential in
den Klammern:

$$\vec E(\vec x) = -\nabla\Big(\frac{1}{4\pi\varepsilon_0}\int_{\mathbb{R}^3}\frac{\rho(\vec y)}{\lvert\vec x-\vec y\rvert}\;d^3y\Big), \qquad \vec B(\vec x) = \operatorname{rot}\Big(\frac{\mu_0}{4\pi}\int_{\mathbb{R}^3}\frac{\vec J(\vec y)}{\lvert\vec x-\vec y\rvert}\;d^3y\Big).$$

**Im Bild:** Ladungen sind die Quellen, Ströme die Strudel. Ein Strom treibt das Magnetfeld um sich herum so an, wie ein Wirbelring
das Wasser in Bewegung setzt. Diese Analogie benutzte Hermann von Helmholtz 1858 in seiner Arbeit über Wirbelbewegungen; nach ihm
ist die Zerlegung benannt.

:::herleitung
**Das elektrische Feld.** Wirbel hat es keine, also ist $\vec A$ null. Die Quelldichte ist $\frac{\rho}{\varepsilon_0}$, also ist $u$
minus deren Newtonpotential, und $\nabla u$ ist die Formel links.

**Das Magnetfeld.** Quellen hat es keine, also ist $u$ null, und $\vec A$ ist das Newtonpotential von $\mu_0\vec J$.

**Streng genommen** haben $\vec E$ und $\vec B$ keinen kompakten Träger — sie klingen nur ab, das Coulomb-Feld einer Ladung sogar nur
wie $\frac{1}{r^2}$. Die beiden Formeln lassen sich aber direkt prüfen, wenn $\rho$ und $\vec J$ stetig differenzierbar mit kompaktem
Träger sind und $\vec J$ quellenfrei ist, wie bei stationären Strömen. Für das elektrische Potential gibt der Poisson-Satz die
Quelldichte $\frac{\rho}{\varepsilon_0}$ des Felds, und als Gradientenfeld wirbelt es nicht. Für das Vektorpotential $\vec A$ in der
Klammer gibt der Poisson-Satz, und weil man die Divergenz auf die Dichte legen darf,

$$-\Delta\vec A = \mu_0\vec J, \qquad \operatorname{div}\vec A = \mu_0\int_{\mathbb{R}^3}g(\vec x-\vec y)\,\operatorname{div}\vec J(\vec y)\;d^3y = 0.$$

Mit der rot-rot-Identität folgt

$$\operatorname{rot}\vec B = \operatorname{rot}\operatorname{rot}\vec A = \nabla\big(\operatorname{div}\vec A\big)-\Delta\vec A = \mu_0\vec J,$$

und quellenfrei ist $\vec B$ als Rotationsfeld ohnehin.
:::

Damit endet das Kapitel über die Integralsätze im Raum. Das nächste Kapitel wechselt das Thema und fragt, wie Folgen von
Funktionen konvergieren — punktweise oder gleichmäßig. Genau diese Frage steckte im zweiten Beweisschritt: Darf man einen
Grenzübergang mit dem Ableiten vertauschen? Und die Gewichte $\frac{1}{\lvert S_\varepsilon\rvert}$ auf immer kleineren
Kugeloberflächen sind ein erstes Beispiel einer Dirac-Schar, die das Kapitel über Fourier-Reihen genauer untersucht.

:::kern
- Die __Einheitsquelle__ $g(\vec z)=\frac{1}{4\pi\lvert\vec z\rvert}$ schickt durch jede Kugel um den Ursprung die Schüttung $1$; außerhalb des Ursprungs ist sie harmonisch.
- $g$ und $\nabla g$ sind integrierbar, die zweiten Ableitungen nicht — deshalb trägt der Kern im Beweis nur eine Ableitung.
- __Poisson-Gleichung__: Das Newtonpotential einer stetig differenzierbaren Dichte mit kompaktem Träger ist zweimal stetig differenzierbar und löst $-\Delta u=f$.
- Beweis: Blase ausschneiden, Ableitung auf die Gewichtung umhängen, partielle Integration auf der Kugelschale; auf der Blasenhaut zeigt die Normale zum Ursprung, die Normalableitung ist $\frac{1}{\lvert S_\varepsilon\rvert}$.
- Der Randterm ist das __Kugelmittel__ der Dichte; es strebt gegen $f(\vec x)$ und weicht etwa um $\frac{\varepsilon^2}{6}\Delta f$ davon ab.
- __Greensche Funktion__: die Antwort auf eine Einheitsquelle, kurz $-\Delta g=\delta_{\vec 0}$ — gegen die Quellen eines Potentials integriert, liefert $g$ dessen Wert im Ursprung.
- __Hauptsatz der Vektoranalysis__: Jedes zweimal stetig differenzierbare Feld mit kompaktem Träger zerfällt in $\vec F=\nabla u+\operatorname{rot}\vec A$, Quellenströmung plus Wirbelströmung.
- Beweis: $\Delta u=\operatorname{div}\vec F$ lösen; der Rest ist quellenfrei und nach Poincaré ein Wirbelfeld.
- Ausdrücklich ist $u$ minus das Newtonpotential der Quellen und $\vec A$ das der Wirbel — zweimal stetig differenzierbar, von selbst quellenfrei; außerhalb des Trägers heben sich die Anteile auf.
- __Coulomb-Eichung__: $\Delta\chi=-\operatorname{div}\vec A$ lösen und $\nabla\chi$ addieren.
- Eindeutig wird die Zerlegung erst, wenn beide Anteile im Unendlichen verschwinden; ein konstantes Feld ist Gradienten- und Wirbelfeld zugleich.
- Statt des kompakten Trägers genügt $\vec F(\vec x)=o(1/\lvert\vec x\rvert^2)$, für glatte Felder irgendein Abklingen (Blumenthal 1905).
:::

:::quiz
F: Warum fließt durch jede Kugel um den Ursprung genau die Schüttung $1$, gleichgültig wie groß sie ist?
A: Die Strömung der Einheitsquelle ist $-\nabla g=\frac{\vec e_r}{4\pi r^2}$. Auf der Kugel vom Radius $R$ ist ihre Normalkomponente überall $\frac{1}{4\pi R^2}$, die Fläche ist $4\pi R^2$, das Produkt $1$. Zehnmal so weit draußen ist die Strömung hundertmal schwächer und die Kugel hundertmal größer; dass zwischen zwei Kugeln nichts hinzukommt, ist die Quellenfreiheit $\Delta g=0$ außerhalb des Ursprungs.
F: Warum darf man im Beweis nicht beide Ableitungen des Laplace-Operators auf den Kern legen?
A: Wegen $\Delta g=0$ außerhalb des Ursprungs käme $\Delta u=0$ für jede Dichte heraus — falsch. Die zweiten Ableitungen von $g$ wachsen wie $\frac{1}{r^3}$ und sind nicht integrierbar: Schon die radiale zweite Ableitung $\frac{1}{2\pi r^3}$ hat über die Schale zwischen $\varepsilon$ und $1$ das Integral $2\ln\frac1\varepsilon$, das ohne Grenze wächst. Eine Ableitung ist harmlos, denn $\int_{K_\varepsilon}\lvert\nabla g\rvert\,d^3z=\varepsilon$; die Quellwirkung des Kerns sitzt im Ursprung.
F: Was geschieht in den Schritten 1 bis 4 des Poisson-Beweises?
A: Schritt 1 verschiebt auf den Versatz $\vec z$, sodass der Messpunkt nur noch in der Dichte steht. Schritt 2 legt eine Ableitung auf den Kern und die zweite auf die Dichte: $\Delta u(\vec x)=\int\nabla g(\vec z)\cdot(\nabla f)(\vec x-\vec z)\,d^3z$. Schritt 3 schneidet eine Blase vom Radius $\varepsilon$ aus, deren Beitrag höchstens $\max\lvert\nabla f\rvert\cdot\varepsilon$ ist. Schritt 4 ersetzt nach der Kettenregel $(\nabla f)(\vec x-\vec z)$ durch $-\nabla\psi(\vec z)$ mit der Gewichtung $\psi(\vec z)=f(\vec x-\vec z)$; dieses Minus hebt das vor dem Integral auf.
F: Was geschieht in den Schritten 5 bis 7, und warum bleibt am Ende $f(\vec x)$ übrig?
A: Auf der Kugelschale zwischen $\varepsilon$ und einem großen Radius $R$ — die partielle Integration mit Rand braucht einen beschränkten Körper — fällt das Volumenintegral weg, weil $g$ dort harmonisch ist, und auf der äußeren Kugel ist $\psi$ null. Auf der Blasenhaut zeigt die äußere Normale der Schale zum Ursprung, $\vec n=-\vec e_r$, und die Normalableitung ist $\frac{1}{4\pi\varepsilon^2}=\frac{1}{\lvert S_\varepsilon\rvert}$: die Schüttung $1$, gleichmäßig auf die Haut verteilt. Der Randterm ist deshalb das Kugelmittel der Dichte; es weicht von $f(\vec x)$ höchstens um die größte Abweichung auf der Haut ab, und die geht wegen der Stetigkeit gegen null.
F: Was zeigt das Kugelmittel der glatten Wolke $(1-\lvert\vec y\rvert^2)^2$ um den Punkt $(\frac12,0,0)$?
A: Es ist $f(\vec x)-\frac76\varepsilon^2+\varepsilon^4$, also $0{,}5509$ für $\varepsilon=0{,}1$ und $0{,}562\,38$ für $\varepsilon=0{,}01$, mit dem Grenzwert $f(\vec x)=0{,}5625$. Die Schranke aus Schritt 7 ist mit $0{,}1529$ viel gröber, weil sich Abweichungen nach oben und unten fast aufheben. Die Abweichung $-\frac76\varepsilon^2$ ist $\frac{\varepsilon^2}{6}$ mal $\Delta f(\vec x)=-7$: Der Laplace-Operator misst, wie weit das Mittel der Umgebung vom Wert in der Mitte abweicht.
F: Was bedeuten „Greensche Funktion" und die Kurzschrift $-\Delta g=\delta_{\vec 0}$ genau?
A: $g$ ist die Greensche Funktion von $-\Delta$, weil ihre Faltung $g*f$ mit jeder zulässigen Dichte die Poisson-Gleichung löst; $g(\vec x-\vec y)$ ist die Antwort auf eine Einheitsquelle bei $\vec y$, und die Wolke ist eine Überlagerung solcher Quellen. Die Kurzschrift sagt, dass die ganze Quellstärke $1$ im Ursprung sitzt. Genau heißt sie: Für jede zweimal stetig differenzierbare Funktion $f$ mit kompaktem Träger ist $\int g\,(-\Delta f)\,d^3y=f(\vec 0)$ — für $f=(1-r^2)^3$ kommt $1$ heraus, obwohl sich Quellen und Senken von $-\Delta f$ insgesamt aufheben.
F: Wie beweist das Skript den Hauptsatz der Vektoranalysis, und was fehlt dem Glattheitsargument?
A: Man löst $\Delta u=\operatorname{div}\vec F$ mit dem Newtonpotential von $-\operatorname{div}\vec F$; dann ist $\vec F-\nabla u$ quellenfrei und nach dem Poincaré-Lemma auf dem Sterngebiet $\mathbb{R}^3$ ein Wirbelfeld $\operatorname{rot}\vec A$. Die Formel des Lemmas macht $\vec A$ mindestens so glatt wie das Restfeld, und das ist zunächst nur einmal stetig differenzierbar, weil $u$ zweimal stetig differenzierbar ist. Ein zweimal stetig differenzierbares Vektorpotential liefern erst die ausdrücklichen Formeln.
F: Wie lauten die ausdrücklichen Potentiale, und was zeigen sie am Strahl in der Kugel?
A: Mit $\vec Z$, dem komponentenweisen Newtonpotential von $\vec F$, ist $u=-\operatorname{div}\vec Z$, minus das Newtonpotential der Quellen $\operatorname{div}\vec F$, und $\vec A=\operatorname{rot}\vec Z$, das Newtonpotential der Wirbel $\operatorname{rot}\vec F$. Das folgt aus $-\Delta\vec Z=\vec F$ und der rot-rot-Identität; $\vec A$ ist von selbst quellenfrei. Beim Strahl $f\,\vec e_3$ sitzen Quellen unten, Senken oben und ein Wirbelring um die Achse. Draußen sind beide Anteile nicht null — bei $(0,0,2)$ ist $\nabla u=-\frac q4\vec e_3$ und $\operatorname{rot}\vec A=\frac q4\vec e_3$ mit $q=\frac{16}{315}$ —, aber sie heben sich auf.
F: Wann ist die Helmholtz-Zerlegung eindeutig, und wie erreicht man die Coulomb-Eichung?
A: Zwei Zerlegungen unterscheiden sich um ein Feld, das Gradienten- und Rotationsfeld zugleich ist, also harmonisch — etwa ein konstantes Feld, das $\nabla(\vec c\cdot\vec x)$ und $\operatorname{rot}(\frac12\vec c\times\vec x)$ zugleich ist. Verlangt man, dass beide Anteile im Unendlichen verschwinden, bleibt wegen der Mittelwerteigenschaft harmonischer Funktionen nur das Nullfeld. Das Vektorpotential bleibt frei bis auf ein $\nabla\chi$; die Coulomb-Eichung erreicht man mit $\Delta\chi=-\operatorname{div}\vec A$ — beim Turm-Potential der Spirale mit $\chi=-\frac{x_3^3}{9}$.
F: Wie folgen aus den ausdrücklichen Formeln die Potentialformeln der Elektro- und Magnetostatik?
A: Das elektrostatische Feld hat keine Wirbel und die Quelldichte $\frac{\rho}{\varepsilon_0}$; also ist $\vec A=\vec 0$, und $\vec E$ ist minus der Gradient von $\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vec y)}{\lvert\vec x-\vec y\rvert}\,d^3y$. Das Magnetfeld hat keine Quellen und die Wirbeldichte $\mu_0\vec J$; also ist $u=0$, und $\vec B$ ist die Rotation von $\frac{\mu_0}{4\pi}\int\frac{\vec J(\vec y)}{\lvert\vec x-\vec y\rvert}\,d^3y$. Weil die Felder nur abklingen, prüft man das direkt: Das Vektorpotential ist wegen $\operatorname{div}\vec J=0$ quellenfrei, und mit $-\Delta\vec A=\mu_0\vec J$ gibt die rot-rot-Identität $\operatorname{rot}\vec B=\mu_0\vec J$.
:::
