---
title: Der Satz von Stokes im Raum
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050200
summary: Von Grund auf – der räumliche Satz von Stokes, $\int_S\operatorname{rot}\vec F\cdot d\vec S=\oint_{\partial S}\vec F\cdot d\vec x$. Leitbild ist ein Kescher: ein Netz aus kleinen Maschen, das an einem Ring hängt. Jede Masche misst mit einem kleinen Schaufelrad die Wirbel, innen heben sich die Ränder benachbarter Maschen weg, und übrig bleibt der Ring – egal, wie tief das Netz durchhängt. Mit Orientierung und Rechte-Hand-Regel, dem Flussintegral, dem Beweis über Green im Parameterbereich und der Frage, wann ein Feld ein Rotationsfeld ist: Das Coulomb-Feld ist auf $\mathbb{R}^3\setminus\{\vec 0\}$ ein Gradientenfeld, aber kein Rotationsfeld, das Wendeltreppen-Feld genau umgekehrt. Mit Beispiel-Seite.
tags: Satz von Stokes, Flussintegral, orientierte Fläche, Normalenfeld, Rotation, Zirkulation, Rotationsfeld, Vektorpotential, Rechte-Hand-Regel
---

## Anschaulich

Im Artikel über die
[Integralsätze in der Ebene](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/integralsaetze-in-der-ebene.html)
hat der Satz von Stokes in der Ebene die Arbeit längs eines Zauns mit den Wirbeln im eingezäunten Grundstück verbunden. Im Raum ist die Fläche nicht mehr flach, sondern beliebig gewölbt, und die Rotation ist ein
echter Vektor. Die Aussage bleibt: **Die Wirbel, die durch eine Fläche treten, sind die Zirkulation längs ihres Randes.**

**Das Leitbild dieses Artikels:** ein **Kescher** — ein Netz, das an einem Ring hängt. Das Netz besteht aus kleinen Maschen,
wie das Tuch im vorigen Artikel. In jeder Masche dreht sich ein winziges Schaufelrad, das misst, wie stark das Feld dort um die
Masche kreist. Benachbarte Maschen teilen sich eine Kante und laufen sie in entgegengesetzter Richtung ab; innen heben sich
diese Beiträge weg. Übrig bleibt der Weg um den Ring.

Daraus folgt etwas Erstaunliches: Wie tief das Netz durchhängt, spielt keine Rolle — nur der Ring zählt. Und eine geschlossene
Fläche, etwa eine Kugel, ist ein Netz ohne Ring. Durch sie tritt deshalb netto kein Wirbel hindurch. Genau daran scheitert das
Feld einer Punktladung, wenn man es als Rotation eines anderen Felds schreiben will.

:::grafik
Szene: hoema3/integralsaetze-im-raum/02-kescher · Vorlage: stokes-netz-3d
Ein Kescher: ein gewölbtes Netz aus Maschen an einem kreisförmigen Ring, darunter Pfeile eines Wirbelfelds. In jeder Masche
dreht sich ein kleines Schaufelrad; der Umlauf um jede Masche ist als kurzer Pfeilkreis gezeichnet. Ein Regler lässt die
inneren Umläufe verblassen, weil sich gemeinsame Kanten aufheben, bis nur der Umlauf am Ring bleibt. Ein zweiter Regler lässt
das Netz tiefer oder flacher durchhängen; zwei Zähler — Wirbelfluss durch das Netz und Zirkulation am Ring — bleiben gleich.
Eine Hand zeigt die Rechte-Hand-Regel: Daumen in Richtung der Normale, Finger im Umlaufsinn des Rings. (Rot = Wirbel,
blau = Netz und Ring, orange = Umläufe, grau = Achsen.)
:::

## Orientierung

Ein reguläres Flächenstück $S=\vec\Phi(B)$ aus dem vorigen Artikel hat an jedem Punkt die Einheitsnormale

$$\vec n\big(\vec\Phi(u,v)\big) = \frac{\partial_u\vec\Phi\times\partial_v\vec\Phi}{\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\rvert}.$$

Dieses __Normalenfeld__ hängt bis auf das Vorzeichen nicht von der Parametrisierung ab. Wählt man eine der beiden Seiten —
legt man also fest, nach welcher Seite die Normale zeigt —, ist das Flächenstück __orientiert__. Vertauscht man im
Parameterbereich die Rollen von $u$ und $v$, kehrt sich die Orientierung um. Aus jeder regulären Parametrisierung gewinnt man
so eine, die zur gewählten Orientierung passt.

**Im Bild:** Die Normale ist der Stiel, mit dem man den Kescher hält: Er zeigt auf die Seite, von der aus man ins Netz schaut.
Wer Zeilen und Spalten des Gitters vertauscht, dreht den Stiel um.

:::herleitung
**Das Vertauschen.** Das Kreuzprodukt ist antisymmetrisch:

$$\partial_v\vec\Phi\times\partial_u\vec\Phi = -\,\partial_u\vec\Phi\times\partial_v\vec\Phi.$$

**Die Unabhängigkeit bis aufs Vorzeichen.** Zwei Parametrisierungen $\vec\Phi$ und $\vec\Phi\circ\vec\Psi$ desselben Flächenstücks
hängen über einen Parameterwechsel $\vec\Psi$ zusammen. Nach der Kettenregel sind die neuen Tangenten Kombinationen der alten,
mit den Einträgen von $D\vec\Psi$ als Koeffizienten. Das Kreuzprodukt ist linear in beiden Faktoren und antisymmetrisch, und
ausmultipliziert bleibt

$$\partial_s\big(\vec\Phi\circ\vec\Psi\big)\times\partial_t\big(\vec\Phi\circ\vec\Psi\big) = \det D\vec\Psi\cdot\big(\partial_u\vec\Phi\times\partial_v\vec\Phi\big)\circ\vec\Psi.$$

Nach dem Normieren unterscheiden sich die beiden Normalen nur um das Vorzeichen von $\det D\vec\Psi$. Weil die Determinante
nirgends null ist und das Innere des Parameterbereichs zusammenhängt, hat sie überall dasselbe Vorzeichen.

**Im Bild:** Ein anderes Gitter auf demselben Netz kann den Stiel nur ganz umdrehen, nicht schief stellen.
:::

::::beispiel Wohin die Normale zeigt
**(a) Die Kugel** in Kugelkoordinaten mit festem Radius $R$: Die Tangenten aus dem vorigen Artikel haben das Kreuzprodukt

$$\partial_\theta\vec\Phi\times\partial_\varphi\vec\Phi = R^2\sin\theta\,\big(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta\big) = R^2\sin\theta\,\vec e_r.$$

Die Normale zeigt nach außen. In der Reihenfolge $(\varphi,\theta)$ zeigt sie nach innen.

**(b) Ein Graph** $z=h(x,y)$ hat das Kreuzprodukt

$$\partial_x\vec\Phi\times\partial_y\vec\Phi = \big(-\partial_xh,\ -\partial_yh,\ 1\big),$$

und die Normale zeigt nach oben, denn ihre dritte Komponente ist positiv.

**Im Bild:** Bei (a) hält man den Kescher von außen und schaut in die Kugel, bei (b) von oben aufs Dach.
::::

## Das Flussintegral

**Die Akteure:** ein orientiertes reguläres Flächenstück $S$ mit dem Normalenfeld $\vec n$ und ein Vektorfeld
$\vec F:U\to\mathbb{R}^3$, das auf einer offenen Menge $U\subseteq\mathbb{R}^3$ um $S$ stetig ist. Das __Flussintegral__ ist

:::formel Definition
$$\int_S\vec F\cdot d\vec S := \int_S\vec F\cdot\vec n\;d\sigma.$$
:::

**So liest man das:** Gemessen wird, wie viel vom Feld durch die Fläche hindurchtritt. Nur die Normalkomponente $\vec F\cdot\vec n$
zählt; der Anteil längs der Fläche streicht an ihr vorbei. Das Symbol $d\vec S$ steht für den Vektor $\vec n\,d\sigma$, Normale mal
Flächenstück.

**Im Bild:** Wind durch das Netz. Weht er senkrecht hindurch, zählt er voll, weht er am Netz entlang, gar nicht.

Für eine reguläre Parametrisierung, die zur Orientierung passt, wird daraus eine Rechenformel ohne Normieren:

$$\int_S\vec F\cdot d\vec S = \int_B\vec F\big(\vec\Phi(u,v)\big)\cdot\big(\partial_u\vec\Phi\times\partial_v\vec\Phi\big)(u,v)\;du\,dv.$$

:::herleitung
Nach der Definition des Oberflächenintegrals ist $d\sigma$ der Betrag des Kreuzprodukts mal $du\,dv$, und die Normale ist das
Kreuzprodukt geteilt durch denselben Betrag:

$$\vec F\cdot\vec n\;d\sigma = \vec F\cdot\frac{\partial_u\vec\Phi\times\partial_v\vec\Phi}{\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\rvert}\;\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\rvert\;du\,dv = \vec F\cdot\big(\partial_u\vec\Phi\times\partial_v\vec\Phi\big)\;du\,dv.$$

Der Betrag kürzt sich weg. Passt die Parametrisierung nicht zur Orientierung, bekommt die Formel ein Minuszeichen.

**Im Bild:** Das Kreuzprodukt ist zugleich Stiel und Maschengröße: Es zeigt in die Normalenrichtung und ist so lang wie die
Masche groß.
:::

::::beispiel Wind durch Netze
**(a) Das Ortsvektorfeld** $\vec x$ durch die Kugel vom Radius $R$, nach außen orientiert: Auf der Kugel ist die Normalkomponente
überall $R$, und

$$\int_{\partial K_R}\vec x\cdot d\vec S = R\cdot4\pi R^2 = 4\pi R^3.$$

Das ist das Dreifache des Kugelvolumens — eine Vorschau auf den Satz von Gauß, denn die Divergenz von $\vec x$ ist $3$.

**(b) Gleichmäßiger Wind von unten**, das konstante Feld $\vec e_z$, durch die obere Halbkugel, nach außen orientiert. Die
Normalkomponente ist $\cos\theta$, und

$$\int_{S}\vec e_z\cdot d\vec S = \int_0^{2\pi}\int_0^{\pi/2}\cos\theta\cdot R^2\sin\theta\;d\theta\,d\varphi = 2\pi R^2\cdot\frac12 = \pi R^2.$$

Das ist die Fläche der Kreisscheibe darunter: Was durch die Kuppel weht, weht auch durch ihren flachen Boden.

**Im Bild:** Bei (b) trifft der Wind die Kuppel am Scheitel senkrecht und am Rand streifend. Insgesamt zählt nur, wie viel
Grundfläche das Netz überspannt.
::::

## Der Satz von Stokes im Raum

**Die Akteure:** ein orientiertes reguläres Flächenstück $S$ mit dem Normalenfeld $\vec n$ und ein Vektorfeld
$\vec F:U\to\mathbb{R}^3$, das auf einer offenen Menge $U\subseteq\mathbb{R}^3$ um $S$ stetig differenzierbar ist. Dann gilt

:::formel Satz
$$\int_S\operatorname{rot}\vec F\cdot d\vec S = \oint_{\partial S}\vec F\cdot d\vec x.$$
:::

Dabei wird der Rand $\partial S$ so durchlaufen, dass er mit der Normale eine __Rechtsschraube__ bildet: Zeigt der Daumen der
rechten Hand in Richtung der Normale, zeigen die gekrümmten Finger den Umlaufsinn. Bequem heißt das: Ist die Parametrisierung
$\vec\Phi$ zur Orientierung passend und durchläuft eine reguläre Kurve $\vec\gamma$ den Rand von $B$ positiv — gegen den
Uhrzeigersinn, das Innere links —, dann durchläuft $\vec\Phi\circ\vec\gamma$ den Rand von $S$ im richtigen Sinn.

**So liest man das:** Links der Fluss der Rotation durch die Fläche, rechts die Zirkulation — die Arbeit des Felds längs der
Randkurve. Für eine flache Fläche in der $xy$-Ebene mit der Normale $\vec e_z$ ist $\operatorname{rot}\vec F\cdot\vec e_z$ die ebene
Rotation, und der Satz wird zum Satz von Stokes in der Ebene.

**Im Bild:** Der Kescher. Die Schaufelräder in den Maschen messen den Wirbelfluss, innen heben sich die gemeinsamen Kanten
weg, und am Ring bleibt die Zirkulation. Zwei Netze am selben Ring, ob flach oder tief durchhängend, fangen denselben
Wirbelfluss.

:::herleitung
**Warum die Rechtsschraube.** Die Randkurve $\vec\gamma$ von $B$ habe an einer Stelle den Tangentenvektor mit den Komponenten
$\alpha$ und $\beta$; die nach links gedrehte Richtung, mit den Komponenten $-\beta$ und $\alpha$, zeigt ins Innere. Auf der Fläche
werden daraus die Tangente $\vec T$ der Randkurve und eine Richtung $\vec I$ ins Innere der Fläche:

$$\vec T = \alpha\,\partial_u\vec\Phi+\beta\,\partial_v\vec\Phi, \qquad \vec I = -\beta\,\partial_u\vec\Phi+\alpha\,\partial_v\vec\Phi, \qquad \vec T\times\vec I = \big(\alpha^2+\beta^2\big)\,\partial_u\vec\Phi\times\partial_v\vec\Phi.$$

Das Kreuzprodukt von Laufrichtung und Innenrichtung zeigt also wie die Normale. Wer längs des Randes läuft, mit dem Kopf in
Normalenrichtung, hat die Fläche zur Linken — das ist die Rechtsschraube.
:::

::::beispiel Ein Wirbel im Kescher
Das Feld

$$\vec F(x,y,z) = (-y,\ x,\ 0), \qquad \operatorname{rot}\vec F = (0,\ 0,\ 2),$$

kreist um die $z$-Achse; seine Rotation ist überall dieselbe.

**(a) Durch die obere Halbkugel** vom Radius $R$, nach außen orientiert: Die Normalkomponente der Rotation ist $2\cos\theta$, und

$$\int_S\operatorname{rot}\vec F\cdot d\vec S = \int_0^{2\pi}\int_0^{\pi/2}2\cos\theta\cdot R^2\sin\theta\;d\theta\,d\varphi = 2\pi R^2.$$

**(b) Die Zirkulation am Äquator.** Nach der Rechte-Hand-Regel läuft er von oben gesehen gegen den Uhrzeigersinn:

$$\vec\gamma(t) = (R\cos t,\ R\sin t,\ 0), \qquad \vec F\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t) = R^2\sin^2t+R^2\cos^2t = R^2, \qquad \oint_{\partial S}\vec F\cdot d\vec x = 2\pi R^2.$$

**(c) Ein flaches Netz** am selben Ring, die Kreisscheibe mit der Normale $\vec e_z$: Die Normalkomponente der Rotation ist $2$, der
Fluss $2\cdot\pi R^2$ — derselbe Wert.

**Im Bild:** Ob das Netz flach im Ring hängt oder als Halbkugel durchhängt, es fängt denselben Wirbelfluss. Bei der Halbkugel
treffen die Wirbel das Netz am Scheitel senkrecht und am Rand streifend; dafür ist die Halbkugel größer.
::::

## Warum der Satz gilt

Ist die Parametrisierung sogar zweimal stetig differenzierbar, führt man den Satz auf den Satz von Stokes in der Ebene
zurück — im Parameterbereich $B$. Dort definiert man ein ebenes Hilfsfeld $\vec G$ mit den Komponenten

$$G_1(u,v) := \vec F\big(\vec\Phi(u,v)\big)\cdot\partial_u\vec\Phi(u,v), \qquad G_2(u,v) := \vec F\big(\vec\Phi(u,v)\big)\cdot\partial_v\vec\Phi(u,v).$$

Ihre ebene Rotation ist genau der Integrand des Wirbelflusses:

:::formel Lemma
$$\partial_uG_2-\partial_vG_1 = \big(\operatorname{rot}\vec F\big)\big(\vec\Phi\big)\cdot\big(\partial_u\vec\Phi\times\partial_v\vec\Phi\big).$$
:::

**Im Bild:** Das Hilfsfeld ist der Wind, wie ihn ein Läufer auf dem Gitter des Parameterbereichs spürt: die Komponente längs
der Gitterlinien, die er gerade entlangläuft. Seine Wirbel im Parameterbereich sind die Wirbel durch die Maschen des Netzes.

:::herleitung
**Schritt 1: das Lemma.** Nach der Produkt- und der Kettenregel ist

$$\partial_uG_2 = \big(D\vec F\,\partial_u\vec\Phi\big)\cdot\partial_v\vec\Phi+\vec F\cdot\partial_u\partial_v\vec\Phi, \qquad \partial_vG_1 = \big(D\vec F\,\partial_v\vec\Phi\big)\cdot\partial_u\vec\Phi+\vec F\cdot\partial_v\partial_u\vec\Phi.$$

Nach dem Satz von Schwarz heben sich die zweiten Ableitungen von $\vec\Phi$ weg. Mit den Abkürzungen $\vec p$ für
$\partial_u\vec\Phi$ und $\vec q$ für $\partial_v\vec\Phi$ bleibt

$$\partial_uG_2-\partial_vG_1 = \vec q\cdot D\vec F\,\vec p-\vec p\cdot D\vec F\,\vec q = \vec q\cdot\big(D\vec F-D\vec F^{\mathsf T}\big)\,\vec p.$$

Der antisymmetrische Teil der Jacobi-Matrix wirkt wie ein Kreuzprodukt mit der Rotation; die erste Komponente zeigt es,
die anderen gehen genauso:

$$\Big(\big(D\vec F-D\vec F^{\mathsf T}\big)\,\vec p\Big)_1 = \big(\partial_2F_1-\partial_1F_2\big)\,p_2+\big(\partial_3F_1-\partial_1F_3\big)\,p_3 = \big(\operatorname{rot}\vec F\times\vec p\big)_1.$$

Damit ist die Differenz ein Spatprodukt, und zyklisches Vertauschen gibt das Lemma:

$$\vec q\cdot\big(\operatorname{rot}\vec F\times\vec p\big) = \operatorname{rot}\vec F\cdot\big(\vec p\times\vec q\big).$$

**Schritt 2: Green.** Mit der Rechenformel für das Flussintegral und dem Satz von Stokes in der Ebene, angewandt auf $\vec G$ im
Parameterbereich, ist

$$\int_S\operatorname{rot}\vec F\cdot d\vec S = \int_B\big(\partial_uG_2-\partial_vG_1\big)\;d(u,v) = \oint_{\partial B}G_1\,du+G_2\,dv.$$

**Schritt 3: zurück auf die Fläche.** Durchläuft $\vec\gamma$ den Rand von $B$ positiv, ist nach der Kettenregel die
Geschwindigkeit der Bildkurve $\partial_u\vec\Phi\,\dot\gamma_1+\partial_v\vec\Phi\,\dot\gamma_2$, und

$$\oint_{\partial B}G_1\,du+G_2\,dv = \int_a^b\vec F\big(\vec\Phi(\vec\gamma)\big)\cdot\Big(\partial_u\vec\Phi\,\dot\gamma_1+\partial_v\vec\Phi\,\dot\gamma_2\Big)\;dt = \oint_{\partial S}\vec F\cdot d\vec x.$$

**Im Bild:** Erst rechnet man die Wirbel durch jede Masche in Wirbel des Hilfsfelds um, dann gilt im flachen Parameterbereich
das Grundstücks-Argument aus dem Artikel über die Integralsätze in der Ebene, und zuletzt wird der Zaun um $B$ wieder zum Ring
des Keschers.
:::

::::beispiel Der Beweis an der Halbkugel
Für den Wirbel $\vec F=(-y,\ x,\ 0)$ und die Kugelkoordinaten aus dem vorigen Artikel ist das Hilfsfeld

$$G_1 = \vec F\cdot\partial_\theta\vec\Phi = 0, \qquad G_2 = \vec F\cdot\partial_\varphi\vec\Phi = R^2\sin^2\theta.$$

Das Lemma stimmt:

$$\partial_\theta G_2-\partial_\varphi G_1 = 2R^2\sin\theta\cos\theta, \qquad \operatorname{rot}\vec F\cdot\big(\partial_\theta\vec\Phi\times\partial_\varphi\vec\Phi\big) = (0,\ 0,\ 2)\cdot R^2\sin\theta\,\vec e_r = 2R^2\sin\theta\cos\theta.$$

Über das Parameterrechteck der oberen Halbkugel integriert, gibt das wieder $2\pi R^2$.

**Im Bild:** Ein Läufer auf einem Meridian spürt keinen Wind längs seines Wegs, einer auf einem Breitenkreis umso mehr, je weiter
der Kreis ist — daraus allein entsteht der ganze Wirbelfluss.
::::

## Wann ist ein Feld ein Rotationsfeld?

Ein Vektorfeld $\vec F$ auf einer offenen Menge $U\subseteq\mathbb{R}^3$ heißt __Rotationsfeld__, wenn es ein Vektorfeld $\vec A$ auf $U$
gibt — ein __Vektorpotential__ — mit

$$\vec F = \operatorname{rot}\vec A.$$

Notwendig ist dann, dass $\vec F$ quellenfrei ist, denn für ein zweimal stetig differenzierbares $\vec A$ ist
$\operatorname{div}\operatorname{rot}\vec A=0$ (Artikel über Rechenregeln). Auf sternförmigen Mengen reicht das nach dem
Poincaré-Lemma auch. Im Allgemeinen reicht es nicht — und der Satz von Stokes zeigt, warum.

**Das Coulomb-Feld.** Auf $U=\mathbb{R}^3\setminus\{\vec 0\}$ — nach dem Artikel
[Homotopieinvarianz und der zweite Hauptsatz](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/homotopie-und-zweiter-hauptsatz.html)
einfach zusammenhängend — betrachtet man das Feld einer Punktladung $Q$:

$$\vec E(\vec x) = \frac{Q}{4\pi r^2}\,\vec e_r, \qquad r = \lvert\vec x\rvert.$$

Es ist wirbelfrei, also ein Gradientenfeld, und zwar

$$\vec E = -\nabla\Big(\frac{Q}{4\pi r}\Big).$$

Es ist auch quellenfrei. Ist es damit ein Rotationsfeld? Nein. Sein Fluss durch jede Kugel um den Ursprung ist $Q$, und das
widerspricht dem Satz von Stokes:

:::herleitung
**Der Fluss.** Auf der Kugel vom Radius $R$ ist die Normalkomponente überall $\frac{Q}{4\pi R^2}$, also

$$\int_{\partial K_R}\vec E\cdot d\vec S = \frac{Q}{4\pi R^2}\cdot4\pi R^2 = Q.$$

**Der Widerspruch.** Wäre $\vec E=\operatorname{rot}\vec A$, zerlegt man die Kugel in die obere und die untere Halbkugel. Beide sind nach
außen orientiert und haben den Äquator als Rand — nach der Rechte-Hand-Regel aber in entgegengesetzter Richtung. Nach Stokes
ist dann

$$\int_{\partial K_R}\vec E\cdot d\vec S = \int_{S_R^+}\operatorname{rot}\vec A\cdot d\vec S+\int_{S_R^-}\operatorname{rot}\vec A\cdot d\vec S = \oint_{\vec\gamma_R}\vec A\cdot d\vec x-\oint_{\vec\gamma_R}\vec A\cdot d\vec x = 0,$$

mit $\vec\gamma_R$ für den Äquator im Umlaufsinn der oberen Hälfte. Das widerspricht dem Fluss $Q$. Also gibt es kein Vektorpotential.

**Im Bild:** Die Kugel ist ein Netz ohne Ring — oder zwei Kescher am selben Ring, deren Ränder sich gegenseitig aufheben.
Durch sie kann kein Wirbelfluss treten, die Punktladung schickt aber den Fluss $Q$ hindurch.
:::

**Das Wendeltreppen-Feld.** Auf dem Raum ohne die $z$-Achse,

$$U = \big\{(x,y,z)\in\mathbb{R}^3 : x^2+y^2\neq0\big\},$$

betrachtet man die räumliche Fassung der Wendeltreppe aus dem Artikel
[Homotopieinvarianz und der zweite Hauptsatz](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/homotopie-und-zweiter-hauptsatz.html):

$$\vec W(x,y,z) = \frac{1}{x^2+y^2}\,\big(-y,\ x,\ 0\big).$$

Es ist wirbelfrei, aber kein Gradientenfeld — um die Achse herum leistet es die Arbeit $2\pi$, und $U$ ist nicht einfach
zusammenhängend. Es ist aber quellenfrei, und es **ist** ein Rotationsfeld, mit dem Vektorpotential

$$\vec W = \operatorname{rot}\vec A, \qquad \vec A(x,y,z) = -\ln\varrho\;\vec e_z, \qquad \varrho = \sqrt{x^2+y^2}.$$

:::herleitung
**Quellenfrei.** Mit der Quotientenregel heben sich die beiden Ableitungen weg:

$$\operatorname{div}\vec W = \frac{\partial}{\partial x}\Big(\frac{-y}{x^2+y^2}\Big)+\frac{\partial}{\partial y}\Big(\frac{x}{x^2+y^2}\Big) = \frac{2xy}{(x^2+y^2)^2}-\frac{2xy}{(x^2+y^2)^2} = 0.$$

**Das Vektorpotential.** $\vec A$ hat nur die dritte Komponente $-\ln\varrho$, und deren Ableitungen nach $x$ und $y$ sind
$-\frac{x}{\varrho^2}$ und $-\frac{y}{\varrho^2}$. Nach der Definition der Rotation ist

$$\operatorname{rot}\vec A = \Big(\partial_yA_3,\ -\partial_xA_3,\ 0\Big) = \Big(-\frac{y}{\varrho^2},\ \frac{x}{\varrho^2},\ 0\Big) = \vec W.$$

**Im Bild:** Um die Achse kann man herumlaufen, ohne sie zu treffen — daher die Arbeit $2\pi$. Aber jede geschlossene Fläche,
die die Achse nicht trifft, umschließt kein Stück von ihr, denn die Achse ist unendlich lang. Kein Netz ohne Ring fängt einen
Fluss.
:::

**Die allgemeine Bedingung.** Für Rotationsfelder kommt es also auf Flächen an, nicht auf Kurven. Dazu gilt der folgende
Satz, hier ohne vollständigen Beweis. Ist $U\subseteq\mathbb{R}^3$ ein Gebiet, in dem jede geschlossene stückweise reguläre Fläche der Rand
eines regulären Bereichs $V\subseteq U$ ist, und ist $\vec F:U\to\mathbb{R}^3$ stetig differenzierbar, so gilt

:::formel Satz
$$\vec F \text{ ist ein Rotationsfeld in } U \quad\Longleftrightarrow\quad \operatorname{div}\vec F = 0 \text{ in } U.$$
:::

**So liest man das:** Die Bedingung an das Gebiet ist das Gegenstück zur Sternform im Poincaré-Lemma. Für Gradientenfelder
kommt es darauf an, ob sich jede geschlossene Kurve zusammenziehen lässt; für Rotationsfelder darauf, ob jede geschlossene
Fläche etwas im Gebiet umschließt.

| | Gradientenfeld | Rotationsfeld |
|---|---|---|
| notwendig | wirbelfrei | quellenfrei |
| hinreichend, wenn | jede geschlossene Kurve sich zusammenziehen lässt | jede geschlossene Fläche einen Bereich im Gebiet umschließt |
| Raum ohne Ursprung | ja — das Coulomb-Feld | nein — das Coulomb-Feld nicht |
| Raum ohne $z$-Achse | nein — die Wendeltreppe nicht | ja — die Wendeltreppe |

:::herleitung
**Von links nach rechts** gilt das immer, für ein zweimal stetig differenzierbares Vektorpotential: Die Divergenz einer
Rotation ist null.

**Von rechts nach links** folgt hier nur die Beweisidee: Die Bedingung an das Gebiet sorgt dafür, dass der
Fluss eines quellenfreien Felds durch jede geschlossene Fläche verschwindet — nach dem Satz von Gauß im nächsten Artikel ist er
das Integral der Divergenz über den umschlossenen Bereich. Damit fehlt genau das Hindernis, an dem das Coulomb-Feld scheitert.
Aus dieser Flussbedingung ein Vektorpotential zu bauen, führt hier zu weit.
:::

:::grafik
Szene: hoema3/integralsaetze-im-raum/02-kurven-und-flaechen · Vorlage: topologie-vergleich-3d
Zwei Räume nebeneinander. Links der Raum ohne den Ursprung: Eine Kugel um das Loch lässt sich nicht zu einem Punkt schrumpfen,
ohne das Loch zu treffen, und die Feldlinien des Coulomb-Felds treten mit dem Fluss $Q$ hindurch; eine Kurve um das Loch lässt
sich dagegen über das Loch hinwegheben. Rechts der Raum ohne die $z$-Achse: Eine Kurve um die Achse bleibt hängen, die
Wendeltreppe leistet längs ihr die Arbeit $2\pi$; jede Kugel, die die Achse nicht trifft, umschließt nichts von ihr. Kernaussage:
Für Gradientenfelder zählen Kurven, für Rotationsfelder Flächen. (Rot = Löcher, blau = Kurven und Flächen, orange = Felder,
grau = Achsen.)
:::

::::beispiel Monopol, Wendeltreppe und ein Faden
**(a) Das Coulomb-Feld auf dem Raum ohne Ursprung:** Fluss $Q$ durch jede Kugel um den Ursprung, also kein Vektorpotential —
obwohl es quellenfrei ist. Der Raum verletzt die Bedingung des Satzes: Die Kugel umschließt den fehlenden Punkt.

**(b) Die Wendeltreppe auf dem Raum ohne $z$-Achse:** Der Raum erfüllt die Bedingung, und $-\ln\varrho\,\vec e_z$ ist ein
Vektorpotential. Zur Probe der Fluss durch ein Rechteck in der Halbebene $y=0$, $x>0$, zwischen den Abständen $1$ und $2$ zur
Achse und den Höhen $0$ und $1$, mit der Normale $\vec e_y$: Die Normalkomponente ist $\frac1x$, der Fluss

$$\int_0^1\int_1^2\frac1x\;dx\,dz = \ln2\approx0{,}69.$$

Die Zirkulation von $\vec A$ längs des Rands gibt dasselbe. Nach der Rechte-Hand-Regel läuft der Rand im Abstand $1$ von der
Achse aufwärts und im Abstand $2$ abwärts. Weil $\vec A$ nur eine $z$-Komponente hat, tragen nur diese beiden Seiten bei: die
erste mit $-\ln1$, also nichts, die zweite mit $-\ln2$ mal dem Höhenunterschied $-1$, zusammen $\ln2$.

**(c) Ein Faden für den Monopol.** Entfernt man aus dem Raum statt des Punkts die ganze untere Hälfte der $z$-Achse, erfüllt der
Rest die Bedingung — jetzt hat das Coulomb-Feld dort ein Vektorpotential, in Kugelkoordinaten

$$\vec A = \frac{Q}{4\pi}\,\frac{1-\cos\theta}{r\sin\theta}\,\vec e_\varphi.$$

Probe mit Stokes an der Kugelkappe bis zum Polarwinkel $\theta_0$: Der Fluss von $\vec E$ ist $\frac{Q}{4\pi r^2}$ mal die Kappenfläche
$2\pi r^2(1-\cos\theta_0)$, die Zirkulation von $\vec A$ ist $A_\varphi$ mal den Umfang $2\pi r\sin\theta_0$ — beide sind
$\frac{Q}{2}(1-\cos\theta_0)$. Lässt man die Kappe bis zum Südpol wachsen, wird der Ring winzig, aber $A_\varphi$ dort unendlich groß:
Der Fluss $Q$ verschwindet durch den Faden.

**Im Bild:** Bei (a) hat das Netz ohne Ring kein Schlupfloch. Bei (c) bohrt der Faden eines hinein, und durch dieses Loch kann
der Fluss einen Ring haben.
::::

## Bedeutung und Ausblick

Der Satz von Stokes im Raum ist die Integralform zweier Maxwell-Gleichungen. Das __Induktionsgesetz__ sagt: Die Rotation des
elektrischen Felds ist die negative zeitliche Änderung der magnetischen Flussdichte — nach Stokes ist die Umlaufspannung längs
einer Leiterschleife die negative Änderung des magnetischen Flusses durch jede Fläche, die an der Schleife hängt. Das
__Durchflutungsgesetz__ verbindet ebenso die Umlaufarbeit des Magnetfelds mit dem Strom durch die Schleife.

Dass der Fluss nur vom Ring abhängt, ist dabei entscheidend: Welche Fläche man an die Leiterschleife hängt, ist gleichgültig.
Der nächste Artikel verbindet einen Körper mit seiner Oberfläche über die Divergenz — der Satz von Gauß im Raum, mit dem auch
die offene Richtung des Satzes über Rotationsfelder ihre Idee bekommt.

:::kern
- Ein __orientiertes__ Flächenstück hat ein gewähltes Normalenfeld; Vertauschen der Parameter dreht die Normale um.
- __Flussintegral__: $\int_S\vec F\cdot d\vec S=\int_S\vec F\cdot\vec n\,d\sigma$ — nur die Normalkomponente tritt durch die Fläche.
- Mit einer passenden Parametrisierung ist der Integrand $\vec F(\vec\Phi)\cdot(\partial_u\vec\Phi\times\partial_v\vec\Phi)$; das Kreuzprodukt ist Stiel und Maschengröße zugleich.
- __Satz von Stokes__: $\int_S\operatorname{rot}\vec F\cdot d\vec S=\oint_{\partial S}\vec F\cdot d\vec x$ — Wirbelfluss durch das Netz gleich Zirkulation am Ring.
- __Rechte-Hand-Regel__: Daumen in Richtung der Normale, Finger im Umlaufsinn des Randes.
- Zwei Netze am selben Ring fangen denselben Wirbelfluss; eine geschlossene Fläche fängt keinen.
- Beweis: Green im Parameterbereich für das Hilfsfeld der Komponenten von $\vec F$ längs der Gitterlinien.
- Rotationsfelder sind quellenfrei; umgekehrt nur, wenn jede geschlossene Fläche einen Bereich im Gebiet umschließt.
- Das Coulomb-Feld ist ohne Ursprung ein Gradienten-, aber kein Rotationsfeld; die Wendeltreppe ohne $z$-Achse umgekehrt.
:::

:::quiz
F: Was heißt es, ein Flächenstück zu orientieren, und wie dreht man die Orientierung um?
A: Man wählt eine der beiden Seiten, also ein Normalenfeld $\vec n$; bis auf das Vorzeichen hängt es nicht von der Parametrisierung ab, weil sich das Kreuzprodukt beim Parameterwechsel mit $\det D\vec\Psi$ multipliziert. Vertauscht man $u$ und $v$, wechselt das Kreuzprodukt das Vorzeichen, und die Normale zeigt auf die andere Seite — bei der Kugel in der Reihenfolge $(\theta,\varphi)$ nach außen, umgekehrt nach innen.
F: Was misst das Flussintegral, und warum braucht die Rechenformel kein Normieren?
A: Wie viel vom Feld durch die Fläche tritt: $\int\vec F\cdot\vec n\,d\sigma$, nur die Normalkomponente zählt. Mit $\vec n=\frac{\partial_u\vec\Phi\times\partial_v\vec\Phi}{\lvert\cdot\rvert}$ und $d\sigma=\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\rvert\,du\,dv$ kürzt sich der Betrag, und der Integrand ist $\vec F(\vec\Phi)\cdot(\partial_u\vec\Phi\times\partial_v\vec\Phi)$.
F: Wie viel weht vom konstanten Wind $\vec e_z$ durch die obere Halbkugel, und wie viel vom Ortsvektorfeld durch die Kugel?
A: Durch die Halbkugel $\int\cos\theta\,R^2\sin\theta=\pi R^2$ — so viel wie durch die Kreisscheibe darunter. Das Ortsvektorfeld hat auf der Kugel die Normalkomponente $R$, sein Fluss ist $4\pi R^3$, das Dreifache des Kugelvolumens.
F: Was besagt der Satz von Stokes im Raum, und wie ist der Rand zu durchlaufen?
A: Für ein stetig differenzierbares Feld ist der Fluss der Rotation durch ein orientiertes reguläres Flächenstück gleich der Zirkulation längs des Randes, $\int_S\operatorname{rot}\vec F\cdot d\vec S=\oint_{\partial S}\vec F\cdot d\vec x$. Der Rand bildet mit der Normale eine Rechtsschraube: Daumen in Normalenrichtung, Finger im Umlaufsinn — bei passender Parametrisierung ist das das Bild des positiv durchlaufenen Randes von $B$.
F: Warum fangen zwei Netze am selben Ring denselben Wirbelfluss?
A: Nach Stokes hängt der Wirbelfluss nur von der Zirkulation am Rand ab. Für den Wirbel $(-y,x,0)$ geben die obere Halbkugel vom Radius $R$ und die flache Kreisscheibe darunter beide $2\pi R^2$, ebenso die Zirkulation am Äquator mit $\vec F\cdot\dot{\vec\gamma}=R^2$.
F: Wie führt man den Satz auf den Satz von Stokes in der Ebene zurück?
A: Im Parameterbereich bildet man das Hilfsfeld $G_1=\vec F(\vec\Phi)\cdot\partial_u\vec\Phi$, $G_2=\vec F(\vec\Phi)\cdot\partial_v\vec\Phi$. Seine ebene Rotation ist $\operatorname{rot}\vec F\cdot(\partial_u\vec\Phi\times\partial_v\vec\Phi)$: Die zweiten Ableitungen heben sich nach Schwarz weg, und der antisymmetrische Teil der Jacobi-Matrix wirkt wie ein Kreuzprodukt mit der Rotation. Green macht daraus ein Randintegral, und die Kettenregel bringt es auf den Rand der Fläche.
F: Warum zeigt der Rand bei positiv durchlaufenem Parameterrand mit der Normale eine Rechtsschraube?
A: Mit der Laufrichtung $\vec T=\alpha\partial_u\vec\Phi+\beta\partial_v\vec\Phi$ und der Innenrichtung $\vec I=-\beta\partial_u\vec\Phi+\alpha\partial_v\vec\Phi$ ist $\vec T\times\vec I=(\alpha^2+\beta^2)\,\partial_u\vec\Phi\times\partial_v\vec\Phi$. Laufrichtung, Innenrichtung und Normale bilden also ein Rechtssystem — wer mit dem Kopf in Normalenrichtung am Rand entlangläuft, hat die Fläche links.
F: Warum ist das Coulomb-Feld auf $\mathbb{R}^3\setminus\{\vec 0\}$ kein Rotationsfeld, obwohl es quellenfrei ist?
A: Sein Fluss durch jede Kugel um den Ursprung ist $Q$. Wäre es $\operatorname{rot}\vec A$, gäben die beiden Halbkugeln nach Stokes die Zirkulation von $\vec A$ am Äquator einmal vorwärts und einmal rückwärts, zusammen null. Die Kugel umschließt den fehlenden Punkt — das Gebiet verletzt die Bedingung des Satzes.
F: Warum ist die Wendeltreppe auf dem Raum ohne $z$-Achse ein Rotationsfeld, aber kein Gradientenfeld?
A: Sie ist quellenfrei, und $-\ln\varrho\,\vec e_z$ hat die Rotation $(-\frac{y}{\varrho^2},\frac{x}{\varrho^2},0)$, also die Wendeltreppe; jede geschlossene Fläche im Gebiet umschließt nichts von der unendlich langen Achse. Kein Gradientenfeld ist sie, weil sie um die Achse die Arbeit $2\pi$ leistet — dort bleibt eine Kurve hängen. Der Fluss durch ein Rechteck neben der Achse ist $\ln2$, wie die Zirkulation von $\vec A$ am Rand.
F: Welche Bedingung an das Gebiet macht Quellenfreiheit hinreichend für ein Vektorpotential, und wie zeigt der Monopol mit Faden das?
A: Jede geschlossene stückweise reguläre Fläche im Gebiet muss einen regulären Bereich im Gebiet beranden; dann gilt: Rotationsfeld genau dann, wenn quellenfrei. Entfernt man statt des Ursprungs die untere $z$-Halbachse, ist das erfüllt, und das Coulomb-Feld hat das Vektorpotential $\frac{Q}{4\pi}\frac{1-\cos\theta}{r\sin\theta}\vec e_\varphi$ — an jeder Kugelkappe sind Fluss und Zirkulation $\frac{Q}{2}(1-\cos\theta_0)$.
:::
