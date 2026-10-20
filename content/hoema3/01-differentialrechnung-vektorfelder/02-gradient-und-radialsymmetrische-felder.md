---
title: Der Gradient, Gradientenfelder und radialsymmetrische Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010200
summary: Von Grund auf – warum der Gradient $\nabla f$ in Richtung des steilsten Anstiegs zeigt und senkrecht auf den Niveauflächen steht, was ein Gradientenfeld $E=\nabla\phi$ ist, warum seine Jacobi-Matrix symmetrisch sein muss (Integrabilitätsbedingung) und wie man für radialsymmetrische Felder $u(x)=f(r)$ sofort $\nabla u=f'(r)\,\hat e_r$ erhält – bis zum Coulomb-Feld.
tags: Gradient, Niveaufläche, Gradientenfeld, Skalarpotential, Integrabilitätsbedingung, radialsymmetrisch, Zentralfeld, Coulomb-Feld
---

## Anschaulich

Stell dir ein Skalarfeld $f$ als **Gebirgslandschaft** vor: Jedem Ort ist eine Höhe zugeordnet. Ein Wanderer
spürt an jedem Punkt zwei Dinge — *in welche Richtung* geht es am steilsten bergauf, und *wie steil* ist es dort.

Genau das ist der __Gradient__ $\nabla f$: ein Vektor, der an jedem Punkt in Richtung des **stärksten Anstiegs**
zeigt und dessen Länge angibt, wie schnell das Feld dort wächst.

Zwei Dinge fallen sofort auf: Der Gradient steht **senkrecht** auf den Höhenlinien (entlang einer Höhenlinie
ändert sich ja nichts), und er ist dort am längsten, wo die Höhenlinien **dicht** liegen (steiler Hang).

Dreht man die Idee um, macht der Gradient aus einem **Potential** ein **Feld** — so entstehen das elektrische Feld
und das Gravitationsfeld. Besonders einfach sind dabei Felder, die nur vom **Abstand** zum Zentrum abhängen; sie
führen direkt zum Coulomb-Feld.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-gradient-landschaft · Vorlage: skalarfeld-hoehenlinien-2d
Eine farbige Höhenlandschaft (Skalarfeld $f$) mit Niveaulinien. An mehreren Punkten wächst der Gradient-Pfeil
$\nabla f$ heraus — stets bergauf und senkrecht zur Niveaulinie, am längsten dort, wo die Linien am dichtesten
liegen. Daneben ein radiales Feld (Pfeile sternförmig aus einem Zentrum) mit konzentrischen Äquipotentialkreisen,
auf denen die Pfeile senkrecht stehen. (Rot = Gradient/Feld, grau = Niveaulinien.)
:::

## Niveauflächen und die Geometrie des Gradienten

Beide anschaulichen Aussagen lassen sich sauber begründen — mit **einem** Werkzeug aus dem vorigen Artikel: der
Kettenregel für ein Feld entlang einer Kurve,

$$\frac{d}{dt}\,f(\gamma(t)) = \nabla f(\gamma(t))\cdot\dot\gamma(t).$$

Hier ist $\nabla f$ der Gradient (ein Vektor) und $\dot\gamma$ die Geschwindigkeit der Kurve (ein Vektor); ihr
**Skalarprodukt** ist eine Zahl — die momentane Änderungsrate des Feldwerts längs des Weges.

**1. Senkrecht auf den Niveauflächen.** Eine __Niveaufläche__ (in 2D: __Niveaulinie__) ist die Menge aller Punkte
mit gleichem Feldwert, $f=\text{const}$.

:::herleitung
Läuft man mit einer Kurve $\gamma$ **innerhalb** einer Niveaufläche, ändert sich der Feldwert nicht, also

$$\frac{d}{dt}\,f(\gamma(t)) = 0 \qquad\Longrightarrow\qquad \nabla f\cdot\dot\gamma = 0.$$

Der Geschwindigkeitsvektor $\dot\gamma$ kann dabei **jede** Richtung innerhalb der Fläche annehmen (tangential).
Da das Skalarprodukt mit $\nabla f$ für jede dieser Tangentialrichtungen null ist, steht $\nabla f$ auf allen
senkrecht — also senkrecht auf der Niveaufläche.
:::

**2. Richtung des steilsten Anstiegs.** Fragt man, in welche Einheitsrichtung $v$ (mit $|v|=1$) das Feld am
schnellsten wächst, ist die Rate die __Richtungsableitung__

$$D_v f = \nabla f\cdot v = |\nabla f|\,\cos\theta,$$

mit dem Winkel $\theta$ zwischen $\nabla f$ und $v$. Dieser Ausdruck ist **maximal** für $\cos\theta=1$, also
$v\parallel\nabla f$.

Der Gradient zeigt daher in die Richtung des **steilsten Anstiegs**, und sein Betrag $|\nabla f|$ ist die Steigung
in dieser Richtung. Steht $v$ senkrecht auf $\nabla f$ ($\cos\theta=0$), ändert sich nichts — man läuft entlang der
Niveaufläche.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-richtungsableitung · Vorlage: gradient-halbkreis-2d
Eine Niveaulinie $f=\text{const}$ mit Tangentialvektor $\dot\gamma$ und dem darauf senkrechten Gradienten
$\nabla f$. Ein Halbkreis von Einheitsrichtungen $v$ mit der Richtungsableitung $|\nabla f|\cos\theta$;
hervorgehoben die Maximalrichtung $v\parallel\nabla f$ (steilster Anstieg) und die Nullrichtungen $v\perp\nabla f$.
(Rot = Gradient, orange = betrachtete Richtung $v$, grau = Niveaulinie.)
:::

## Gradientenfelder und das Skalarpotential

Dreht man die Konstruktion um, erzeugt man aus einem Skalarfeld ein Vektorfeld. Ein Vektorfeld
$E:U\to\mathbb{R}^n$ heißt __Gradientenfeld__, wenn es der Gradient eines Skalarfelds ist:

:::formel Definition
$$E = \nabla\phi.$$
:::

Dabei ist $\phi:U\to\mathbb{R}$ ein **Skalarfeld** (eine Zahl pro Punkt) und $E=\nabla\phi$ das daraus erzeugte
**Vektorfeld** (ein Pfeil pro Punkt). Man nennt $\phi$ ein __Skalarpotential__ von $E$.

In der **Physik** benutzt man meist die andere Vorzeichenkonvention, $E=-\nabla\varphi$. Dann nimmt die
potentielle Energie eines Teilchens, das den Feldlinien folgt, stets **ab** — längs einer Feldlinie $\gamma$ (mit
$\dot\gamma$ parallel zu $E$) ist

$$\frac{d}{dt}\,\varphi(\gamma(t)) = \nabla\varphi\cdot\dot\gamma = -E\cdot\dot\gamma < 0.$$

Für den bloßen **Begriff** Gradientenfeld ist das Vorzeichen unerheblich.

## Wann ist ein Feld ein Gradientenfeld? Die Integrabilitätsbedingung

Nicht jedes Vektorfeld ist ein Gradientenfeld. Es gibt aber eine einfache **notwendige** Bedingung, an der man
viele Kandidaten sofort ausschließen kann.

:::formel Satz
$$E=\nabla\phi \quad\Longrightarrow\quad \frac{\partial E_j}{\partial x_k} = \frac{\partial E_k}{\partial x_j}\ \ \text{für alle } j,k \qquad (\text{d.h. } DE=(DE)^T).$$
:::

Gelesen: Die Jacobi-Matrix $DE$ eines Gradientenfelds ist **symmetrisch** — gespiegelt an der Diagonale sind die
Einträge gleich.

:::herleitung
Ist $E=\nabla\phi$ mit zweimal stetig differenzierbarem $\phi$, so ist die $j$-te Komponente
$E_j=\partial\phi/\partial x_j$. Die Einträge der Jacobi-Matrix sind damit die **zweiten** Ableitungen des
Potentials:

$$(DE)_{jk} = \frac{\partial E_j}{\partial x_k} = \frac{\partial^2\phi}{\partial x_k\,\partial x_j}.$$

Nach dem __Satz von Schwarz__ (voriger Artikel) vertauschen gemischte zweite Ableitungen eines $C^2$-Feldes, also
$\frac{\partial^2\phi}{\partial x_k\partial x_j}=\frac{\partial^2\phi}{\partial x_j\partial x_k}$. Das ist genau
$\frac{\partial E_j}{\partial x_k}=\frac{\partial E_k}{\partial x_j}$.
:::

Das ist die __Integrabilitätsbedingung__.

**Stolperstein:** Sie ist notwendig, aber im Allgemeinen **nicht hinreichend**. Ein Feld kann sie überall erfüllen
und trotzdem kein Potential besitzen, wenn sein Definitionsgebiet „Löcher" hat (nicht einfach zusammenhängend).

Unter welcher Bedingung an das Gebiet sie doch ausreicht, klärt später das Poincaré-Lemma. Für $n=3$ ist die
Symmetrie von $DE$ übrigens gleichbedeutend mit „__Rotation__ gleich null" — ein Thema des nächsten Artikels.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-integrabilitaet · Vorlage: matrix-symmetrie-schema
Links eine $3\times3$-Jacobi-Matrix mit markierter Spiegelsymmetrie zur Diagonale
($\partial E_j/\partial x_k=\partial E_k/\partial x_j$). Rechts ein ringförmiges Gebiet mit Loch als Hinweis
„notwendig, nicht hinreichend" (Vorverweis Poincaré/Kurvenintegrale). (Orange = gespiegeltes Eintragspaar, grau
= Gebiet.)
:::

## Radialsymmetrische Felder und die Gradientenformel

In der Feldtheorie hängen viele Größen nur vom **Abstand zum Zentrum** ab. Eine __radialsymmetrische Funktion__
hat die Form

$$u(x) = f(r), \qquad r := |x| = \sqrt{x_1^2+\cdots+x_n^2}.$$

Hier ist $r$ der Abstand zum Ursprung (ein Skalar), und $f:(0,\infty)\to\mathbb{R}$ ist eine gewöhnliche Funktion
**einer** Variablen — das „Höhenprofil" entlang des Radius.

Für den Gradienten einer solchen Funktion gibt es eine bestechend einfache Formel:

:::formel Satz
$$\nabla u = f'(r)\,\hat e_r, \qquad \hat e_r := \frac{x}{r}.$$
:::

Dabei ist $\hat e_r=x/r$ der __radiale Einheitsvektor__ (zeigt überall nach außen, Länge 1), und $f'(r)$ die
gewöhnliche Ableitung des Höhenprofils. In Worten: Der Gradient zeigt **radial**, und sein Betrag ist $|f'(r)|$ —
die Änderungsrate entlang des Radius.

:::herleitung
Man braucht zuerst den Gradienten von $r$ selbst. Mit der Kettenregel und
$\frac{\partial}{\partial x_j}\sqrt{\sum_k x_k^2}=\frac{x_j}{\sqrt{\sum_k x_k^2}}$ ist

$$\frac{\partial r}{\partial x_j} = \frac{x_j}{r} \qquad\Longrightarrow\qquad \nabla r = \frac{x}{r} = \hat e_r.$$

Eine weitere Anwendung der Kettenregel auf $u(x)=f(r)$ liefert dann

$$\nabla u = f'(r)\,\nabla r = f'(r)\,\hat e_r.$$

Anschaulich ist das zwingend: Eine Funktion, die nur vom Abstand abhängt, ändert sich tangential (entlang der
Kreise/Kugeln $r=\text{const}$) überhaupt nicht — die einzige Richtung mit Änderung, und damit die steilste, ist
die radiale.
:::

**Eigenes Beispiel.** Für $u(x)=\tfrac12 r^2=\tfrac12|x|^2$ ist $f(r)=\tfrac12 r^2$, also $f'(r)=r$ und

$$\nabla u = r\,\hat e_r = r\cdot\frac{x}{r} = x.$$

Das Feld zeigt überall radial nach außen und wächst linear mit dem Abstand.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-radialformel · Vorlage: radialfeld-schuessel-2d
Eine radiale Funktion $u(x)=f(r)$ als rotationssymmetrische „Schüssel" über der Ebene; die Niveaulinien sind
konzentrische Kreise. Der Gradient $\nabla u=f'(r)\hat e_r$ zeigt radial (nach außen für $f'>0$) und steht
senkrecht auf den Kreisen. Daneben die Herleitung $\nabla r=x/r=\hat e_r$. (Rot = Gradient, grau = Höhenkreise.)
:::

## Zentralfelder und das Coulomb-Feld

Ein __Zentralfeld__ zeigt überall in radiale Richtung, $F(x)=g(x)\,\hat e_r$. Hängt der Betrag nur vom Abstand ab,
$F(x)=f(r)\,\hat e_r$, heißt es __radialsymmetrisch__.

Solche Felder sind **immer** Gradientenfelder: Auf $\mathbb{R}^n\setminus\{0\}$ besitzt $F=f(r)\,\hat e_r$ ein
Potential $\phi(x)=\varphi(r)$, dessen Radialteil einfach eine **Stammfunktion** von $f$ ist,

$$\varphi(r) = \int f(r)\,dr + \text{const.}$$

Denn nach der Gradientenformel ist $\nabla\big(\varphi(r)\big)=\varphi'(r)\,\hat e_r=f(r)\,\hat e_r=F$. Die Suche
nach einem Potential — eigentlich ein mehrdimensionales Problem — reduziert sich damit auf eine **eindimensionale**
Integration entlang des Radius.

**Die kanonische Anwendung — das Coulomb-Feld.** Für das Potential einer Punktladung $Q$ im Ursprung,
$u(x)=\dfrac{Q}{4\pi r}$ auf $\mathbb{R}^3\setminus\{0\}$, liefert die Gradientenformel mit
$\frac{d}{dr}\frac1r=-\frac1{r^2}$ sofort

$$\nabla u = -\frac{Q}{4\pi r^2}\,\hat e_r, \qquad E = -\nabla u = \frac{Q}{4\pi r^2}\,\hat e_r.$$

Das ist (in geeigneten Einheiten) genau das bekannte **elektrische Feld einer Punktladung**: radial, mit dem
charakteristischen $1/r^2$-Abfall. So verbindet die abstrakte Gradientenformel direkt mit der Elektrostatik.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/02-coulomb · Vorlage: punktladung-feld-2d
Punktladung $Q$ im Ursprung: das radiale Feld $E=\frac{Q}{4\pi r^2}\hat e_r$ als sternförmiges Pfeilbild (Pfeile
nach außen, mit dem Abstand kürzer wegen $1/r^2$), dazu konzentrische Äquipotentialkreise $u=\frac{Q}{4\pi r}$, auf
denen die Feldpfeile senkrecht stehen. (Rot = Feld, grau = Äquipotentiallinien.)
:::

## Bedeutung und Ausblick

Der Gradient ist der erste der drei großen Differentialoperatoren der Vektoranalysis. Er macht aus einem Skalarfeld
(einem Potential) ein Vektorfeld und steckt so hinter jedem Potentialfeld der Elektrotechnik.

Umgekehrt fragt man bei einem gegebenen Vektorfeld zwei andere Dinge: Wie stark **quillt** es an einem Punkt
(Quelle/Senke)? Und wie stark **wirbelt** es? Diese beiden Maße sind die __Divergenz__ und die __Rotation__ — die
nächsten Operatoren und das Thema des folgenden Artikels.

:::kern
- Der __Gradient__ $\nabla f$ steht **senkrecht** auf den __Niveauflächen__ ($f=\text{const}$, denn $\nabla f\cdot\dot\gamma=0$ längs ihnen) und zeigt in die Richtung des **steilsten Anstiegs** (Richtungsableitung $\nabla f\cdot v=|\nabla f|\cos\theta$, maximal für $v\parallel\nabla f$).
- Ein __Gradientenfeld__ ist $E=\nabla\phi$ mit __Skalarpotential__ $\phi$ (Physik: $E=-\nabla\varphi$, Energie fällt längs der Feldlinien).
- Notwendige __Integrabilitätsbedingung__: $DE=(DE)^T$, also $\partial E_j/\partial x_k=\partial E_k/\partial x_j$ (Satz von Schwarz) — notwendig, **nicht** hinreichend (Gebiete mit Löchern → Poincaré später).
- __Radialsymmetrisch__ $u(x)=f(r)$, $r=|x|$: mit $\nabla r=\hat e_r=x/r$ folgt die Gradientenformel $\nabla u=f'(r)\,\hat e_r$.
- Jedes radialsymmetrische __Zentralfeld__ $F=f(r)\hat e_r$ ist ein Gradientenfeld mit $\varphi(r)=\int f(r)\,dr$.
- Beispiel Coulomb: $u=\tfrac{Q}{4\pi r}\Rightarrow E=-\nabla u=\tfrac{Q}{4\pi r^2}\hat e_r$ (radial, $1/r^2$).
:::

:::quiz
F: Warum steht der Gradient $\nabla f$ senkrecht auf den Niveauflächen?
A: Läuft man mit einer Kurve $\gamma$ innerhalb einer Niveaufläche, bleibt $f$ konstant, also $\frac{d}{dt}f(\gamma)=\nabla f\cdot\dot\gamma=0$. Da $\dot\gamma$ jede beliebige Tangentialrichtung annehmen kann und das Skalarprodukt stets null ist, muss $\nabla f$ auf allen Tangentialrichtungen — und damit auf der Fläche — senkrecht stehen.
F: Warum zeigt der Gradient in Richtung des steilsten Anstiegs, und was bedeutet sein Betrag?
A: Die Änderungsrate in Einheitsrichtung $v$ ist $\nabla f\cdot v=|\nabla f|\cos\theta$. Das ist maximal für $\cos\theta=1$, also $v\parallel\nabla f$. Daher zeigt der Gradient bergauf; sein Betrag $|\nabla f|$ ist die Steigung in dieser steilsten Richtung.
F: Wann ist die Richtungsableitung $\nabla f\cdot v$ null bzw. minimal — und was heißt das anschaulich?
A: Null bei $v\perp\nabla f$ (man läuft entlang der Niveaufläche, der Wert ändert sich nicht); minimal (steilster **Abstieg**) bei $v$ antiparallel zu $\nabla f$. Es ist dieselbe $\cos\theta$-Formel, nur mit $\theta=90°$ bzw. $180°$.
F: Was ist ein Gradientenfeld mit Skalarpotential, und warum schreibt die Physik $E=-\nabla\varphi$ statt $+$?
A: $E=\nabla\phi$ heißt Gradientenfeld, $\phi$ sein Potential. Das Minuszeichen in $E=-\nabla\varphi$ sorgt dafür, dass die potentielle Energie längs der Feldlinien **abnimmt**: $\frac{d}{dt}\varphi(\gamma)=\nabla\varphi\cdot\dot\gamma=-E\cdot\dot\gamma<0$, wenn $\dot\gamma$ parallel zu $E$ läuft. Für den bloßen Begriff ist das Vorzeichen egal.
F: Warum muss die Jacobi-Matrix eines Gradientenfelds symmetrisch sein?
A: Für $E=\nabla\phi$ sind ihre Einträge die zweiten Ableitungen des Potentials, $\partial E_j/\partial x_k=\partial^2\phi/(\partial x_k\partial x_j)$. Nach dem Satz von Schwarz vertauschen diese, also $\partial E_j/\partial x_k=\partial E_k/\partial x_j$ — die Matrix ist symmetrisch.
F: Warum ist die Integrabilitätsbedingung $DE=(DE)^T$ zwar notwendig, aber nicht hinreichend für ein Potential?
A: Notwendig folgt sie aus Schwarz. Nicht hinreichend: Auf einem Gebiet mit „Löchern" (nicht einfach zusammenhängend) kann ein Feld die Bedingung lokal überall erfüllen und trotzdem global kein Potential besitzen. Erst ein einfach zusammenhängendes Gebiet macht sie hinreichend (Poincaré-Lemma, später).
F: Warum ist $\nabla r=\frac{x}{r}=\hat e_r$, und was bedeutet dieses Feld anschaulich?
A: Mit der Kettenregel ist $\frac{\partial r}{\partial x_j}=\frac{x_j}{r}$, also $\nabla r=x/r$. Dieser Vektor zeigt radial nach außen und hat Länge 1: Der Abstand zum Ursprung wächst am schnellsten, wenn man **radial** nach außen läuft (Rate 1), und gar nicht, wenn man um das Zentrum kreist.
F: Warum gilt $\nabla u=f'(r)\,\hat e_r$ für $u(x)=f(r)$, und warum kann die steilste Richtung nur radial sein?
A: Kettenregel: $\nabla u=f'(r)\,\nabla r=f'(r)\,\hat e_r$. Da $u$ nur vom Abstand abhängt, ändert sich der Wert tangential (entlang der Kreise/Kugeln $r=\text{const}$) überhaupt nicht — die einzige Richtung mit Änderung, und damit die steilste, ist die radiale.
F: Warum ist **jedes** radialsymmetrische Zentralfeld $F=f(r)\hat e_r$ ein Gradientenfeld, und worauf reduziert sich die Potentialsuche?
A: Setzt man $\varphi(r)=\int f(r)\,dr$, so ist nach der Gradientenformel $\nabla\varphi(r)=\varphi'(r)\hat e_r=f(r)\hat e_r=F$. Das mehrdimensionale Potentialproblem reduziert sich also auf eine **eindimensionale** Integration entlang des Radius.
F: Wie entsteht aus dem Coulomb-Potential $u=\frac{Q}{4\pi r}$ das $1/r^2$-Feld, und woher kommt das Vorzeichen?
A: Die Gradientenformel mit $\frac{d}{dr}\frac1r=-\frac1{r^2}$ gibt $\nabla u=-\frac{Q}{4\pi r^2}\hat e_r$; das physikalische Feld $E=-\nabla u=\frac{Q}{4\pi r^2}\hat e_r$ zeigt (für $Q>0$) nach außen. Das Minus stammt aus der Konvention $E=-\nabla\varphi$; der $1/r^2$-Abfall kommt direkt aus der Ableitung von $1/r$.
:::
