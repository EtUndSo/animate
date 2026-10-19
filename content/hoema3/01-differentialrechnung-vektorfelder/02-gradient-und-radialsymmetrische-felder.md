---
title: Der Gradient, Gradientenfelder und radialsymmetrische Felder
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010200
summary: Von Grund auf – warum der Gradient $\nabla f$ in Richtung des steilsten Anstiegs zeigt und senkrecht auf den Niveauflächen steht, was ein Gradientenfeld $E=\nabla\phi$ mit Skalarpotential ist, warum seine Jacobi-Matrix symmetrisch sein muss (Integrabilitätsbedingung) und wie man für radialsymmetrische Felder $u(x)=f(r)$ mit einem Schlag $\nabla u=f'(r)\,\hat e_r$ bekommt – bis hin zum Coulomb-Feld.
tags: Gradient, Niveaufläche, Gradientenfeld, Skalarpotential, Integrabilitätsbedingung, radialsymmetrisch, Zentralfeld, Coulomb-Feld
---

:::grafik
Einstiegs-Animation: Eine farbige Höhenlandschaft (Skalarfeld $f$) mit eingezeichneten __Niveaulinien__ (Linien
gleicher Höhe). An mehreren Punkten wächst der __Gradient__-Pfeil $\nabla f$ heraus — er zeigt stets **bergauf**
und steht überall **senkrecht** auf der Niveaulinie durch den Punkt, und er ist dort am längsten, wo die Linien
am dichtesten liegen (steilster Hang). Daneben ein zweites Bild: ein __radiales Feld__, dessen Pfeile sternförmig
aus einem Zentrum zeigen (das Feld einer Punktladung) — und die zugehörigen kreisförmigen Äquipotentiallinien,
auf denen die Pfeile senkrecht stehen. Kernbotschaft: Der Gradient übersetzt ein Potential in ein Feld, das
senkrecht auf den Höhenlinien bergauf zeigt.
:::

:::konzept
Im vorigen Artikel war der __Gradient__ $\nabla f$ nur die (transponierte) Jacobi-Matrix eines Skalarfelds. Jetzt
gewinnt er seine **geometrische** Bedeutung: Er zeigt in die Richtung, in der ein Feld am steilsten ansteigt, und
steht senkrecht auf den Flächen gleichen Werts. Felder, die als Gradient eines __Potentials__ entstehen
($E=\nabla\phi$), sind in der Physik allgegenwärtig — das elektrische Feld, das Gravitationsfeld. Sie haben eine
verräterische Eigenschaft (eine symmetrische Jacobi-Matrix), die später zum großen Thema „Wann ist ein Feld ein
Gradientenfeld?" führt. Besonders häufig und besonders einfach sind dabei die __radialsymmetrischen__ Felder, die
nur vom Abstand zum Zentrum abhängen.
:::

**Worum es geht:** Wir klären die __Geometrie des Gradienten__ (steilster Anstieg, senkrecht auf
__Niveauflächen__), führen __Gradientenfelder__ und __Skalarpotentiale__ ein, finden ihre notwendige
__Integrabilitätsbedingung__ und leiten die Gradientenformel für __radialsymmetrische__ Felder her.

## Der Gradient zeigt bergauf — und senkrecht auf die Niveauflächen

Zwei geometrische Aussagen machen den Gradienten zum zentralen Werkzeug. Beide folgen aus der Kettenregel für
ein Feld entlang einer Kurve aus dem vorigen Artikel, $\frac{d}{dt} f(\gamma(t)) = \nabla f(\gamma(t)) \cdot
\dot\gamma(t)$.

**1. Senkrecht auf den Niveauflächen.** Eine __Niveaufläche__ (in 2D: __Niveaulinie__) ist die Menge aller
Punkte mit gleichem Feldwert, $f = \text{const}$. Läuft man mit einer Kurve $\gamma$ **innerhalb** einer solchen
Fläche, ändert sich der Feldwert nicht, also ist $\frac{d}{dt} f(\gamma(t)) = 0$. Mit der Kettenregel heißt das

$$\nabla f \cdot \dot\gamma = 0.$$

Der Geschwindigkeitsvektor $\dot\gamma$ zeigt in eine beliebige Richtung **innerhalb** der Niveaufläche
(tangential). Da das Skalarprodukt mit $\nabla f$ für **jede** solche Tangentialrichtung null ist, steht der
Gradient **senkrecht** auf der Niveaufläche.

**2. Richtung des steilsten Anstiegs.** Fragt man, in welche Einheitsrichtung $v$ ($|v|=1$) das Feld am
schnellsten wächst, so ist die Änderungsrate die __Richtungsableitung__ $\nabla f \cdot v = |\nabla f|\,\cos\theta$
(mit dem Winkel $\theta$ zwischen $\nabla f$ und $v$). Das ist maximal, wenn $\cos\theta = 1$, also $v$ **parallel
zu $\nabla f$**. Der Gradient zeigt daher in die Richtung des **steilsten Anstiegs**, und sein Betrag $|\nabla f|$
ist die Steigung in dieser Richtung.

:::grafik
Eine Niveaulinie $f=\text{const}$ mit Tangentialvektor $\dot\gamma$ und dem darauf senkrechten Gradienten
$\nabla f$. Ein Halbkreis von Einheitsrichtungen $v$ mit der Richtungsableitung $\nabla f\cdot v=|\nabla f|\cos\theta$;
hervorgehoben die Maximalrichtung $v\parallel\nabla f$ (steilster Anstieg) und die Nullrichtungen $v\perp\nabla f$
(entlang der Niveaulinie).
:::

## Gradientenfelder und Skalarpotentiale

Dreht man die Konstruktion um, erzeugt man aus einem Skalarfeld ein Vektorfeld. Ein Vektorfeld $E: U \to
\mathbb{R}^n$ heißt __Gradientenfeld__, wenn es der Gradient eines Skalarfelds ist:

$$E = \nabla \phi,$$

und $\phi$ heißt dann ein __Skalarpotential__ von $E$. In der **Physik** benutzt man meist die andere
Vorzeichenkonvention, $E = -\nabla \varphi$: Dann nimmt die potentielle Energie eines Teilchens, das den
Feldlinien folgt, stets **ab**. Das sieht man wieder mit der Kettenregel — längs einer Feldlinie $\gamma$ (also
$\dot\gamma$ parallel zu $E$) ist

$$\frac{d}{dt}\,\varphi(\gamma(t)) = \nabla\varphi \cdot \dot\gamma = -E \cdot \dot\gamma < 0.$$

Für den bloßen **Begriff** Gradientenfeld ist das Vorzeichen unerheblich.

## Die Integrabilitätsbedingung: ein Gradientenfeld hat symmetrische Jacobi-Matrix

Nicht jedes Vektorfeld ist ein Gradientenfeld. Es gibt eine einfache **notwendige** Bedingung. Ist $E = \nabla\phi$
mit einem zweimal stetig differenzierbaren Potential $\phi$, so sind die Einträge der Jacobi-Matrix gerade die
zweiten Ableitungen des Potentials,

$$(DE)_{jk} = \frac{\partial E_j}{\partial x_k} = \frac{\partial^2 \phi}{\partial x_k\,\partial x_j}.$$

Nach dem __Satz von Schwarz__ (Vertauschbarkeit gemischter Ableitungen, voriger Artikel) ist das symmetrisch in
$j$ und $k$. Also gilt für jedes Gradientenfeld:

$$DE = (DE)^{T}, \qquad\text{d.h.}\qquad \frac{\partial E_j}{\partial x_k} = \frac{\partial E_k}{\partial x_j} \ \ \text{für alle } j,k.$$

Das ist die __Integrabilitätsbedingung__. **Stolperstein:** Sie ist zwar notwendig, aber im Allgemeinen **nicht
hinreichend** — ein Feld kann sie erfüllen und trotzdem kein Potential besitzen, wenn sein Definitionsgebiet
„Löcher" hat. Unter welcher Bedingung an das Gebiet (einfach zusammenhängend) die Bedingung doch ausreicht, klärt
später das Poincaré-Lemma im Kapitel über Kurvenintegrale. Für $n=3$ ist die Symmetrie der Jacobi-Matrix übrigens
gleichbedeutend mit „__Rotation__ gleich null" — ein zentrales Thema des nächsten Artikels.

:::grafik
Links die $3\times3$-Jacobi-Matrix eines Gradientenfelds mit markierter Spiegelsymmetrie zur Diagonale
($\partial E_j/\partial x_k=\partial E_k/\partial x_j$). Rechts der Hinweis „notwendig, nicht hinreichend":
ein ringförmiges Gebiet mit Loch, auf dem ein Feld die Bedingung erfüllt, aber kein Potential hat (Vorverweis
Poincaré/Kurvenintegrale).
:::

## Radialsymmetrische Funktionen

In der Feldtheorie hängen viele Größen nur vom **Abstand zum Zentrum** ab. Eine __radialsymmetrische Funktion__
hat die Form

$$u(x) = f(r), \qquad r := |x| = \sqrt{x_1^2 + \cdots + x_n^2},$$

mit der euklidischen Norm $r$. Um ihren Gradienten zu bilden, braucht man zuerst den Gradienten von $r$ selbst.
Mit der Kettenregel (und $\frac{\partial}{\partial x_j}\sqrt{\sum_k x_k^2} = \frac{x_j}{\sqrt{\sum_k x_k^2}}$) ist

$$\frac{\partial r}{\partial x_j} = \frac{x_j}{r} \qquad\Longrightarrow\qquad \nabla r = \frac{x}{r} =: \hat e_r.$$

Das Vektorfeld $\hat e_r = x/r$ heißt __radialer Einheitsvektor__ — es zeigt an jedem Punkt radial nach außen und
hat Länge 1. Damit folgt mit einer weiteren Anwendung der Kettenregel sofort die allgemeine **Gradientenformel
für radialsymmetrische Funktionen**: Ist $f:(0,\infty)\to\mathbb{R}$ differenzierbar und $u(x)=f(r)$, so gilt

$$\nabla u = f'(r)\,\hat e_r.$$

In Worten: Der Gradient eines radialen Feldes zeigt (bis aufs Vorzeichen von $f'$) **radial**, und sein Betrag ist
schlicht $|f'(r)|$ — die Änderungsrate entlang des Radius. Das ist auch anschaulich klar: Bei einer Funktion, die
nur vom Abstand abhängt, kann die steilste Richtung nur die radiale sein.

**Eigenes Beispiel.** Für $u(x) = \tfrac12 r^2 = \tfrac12|x|^2$ ist $f(r)=\tfrac12 r^2$, also $f'(r)=r$ und
$\nabla u = r\,\hat e_r = r\cdot\frac{x}{r} = x$ — das Feld zeigt überall radial nach außen und wächst linear mit
dem Abstand.

:::grafik
Eine radiale Funktion $u(x)=f(r)$ als rotationssymmetrische „Schüssel" über der Ebene; die Niveaulinien sind
konzentrische Kreise. Der Gradient $\nabla u=f'(r)\hat e_r$ zeigt radial (nach außen, falls $f'>0$) und steht
senkrecht auf den Kreisen. Daneben die Herleitung $\nabla r=x/r=\hat e_r$.
:::

## Zentralfelder und das Coulomb-Feld

Ein __Zentralfeld__ ist ein Vektorfeld, das überall in radiale Richtung zeigt,

$$F(x) = f(x)\,\hat e_r,$$

mit einer skalaren Funktion $f$. Hängt diese nur vom Abstand ab, $F(x) = f(r)\,\hat e_r$, heißt das Feld
__radialsymmetrisch__. Solche Felder sind immer Gradientenfelder: Jedes radialsymmetrische Vektorfeld
$F(x) = f(r)\,\hat e_r$ (mit auf $(0,\infty)$ stetigem $f$) besitzt auf $\mathbb{R}^n\setminus\{0\}$ ein Potential
$\phi(x) = \varphi(r)$, dessen Radialteil einfach eine **Stammfunktion** von $f$ ist:

$$F = \nabla\phi, \qquad \varphi(r) = \int f(r)\,dr + \text{const}.$$

Denn nach der Gradientenformel ist $\nabla\big(\varphi(r)\big) = \varphi'(r)\,\hat e_r = f(r)\,\hat e_r = F$. Das
radiale „Hügelproblem" reduziert sich also auf eine **eindimensionale** Integration entlang des Radius.

**Die kanonische Anwendung — das Coulomb-Feld.** Für das Potential einer Punktladung $Q$ im Ursprung,
$u(x) = \dfrac{Q}{4\pi r}$ auf $\mathbb{R}^3\setminus\{0\}$, liefert die Gradientenformel mit
$\frac{d}{dr}\frac{1}{r} = -\frac{1}{r^2}$ sofort

$$\nabla u(x) = -\frac{Q}{4\pi r^2}\,\hat e_r, \qquad E(x) = -\nabla u(x) = \frac{Q}{4\pi r^2}\,\hat e_r.$$

Das ist (in geeigneten Einheiten) genau das bekannte **elektrische Feld einer Punktladung**: radial, mit dem
charakteristischen $1/r^2$-Abfall. So verbindet die abstrakte Gradientenformel direkt mit der Elektrostatik.

:::grafik
Punktladung $Q$ im Ursprung: das radiale Feld $E=\frac{Q}{4\pi r^2}\hat e_r$ als sternförmiges Pfeilbild (Pfeile
nach außen, nach außen hin kürzer wegen $1/r^2$), dazu konzentrische Äquipotentialkreise $u=\frac{Q}{4\pi r}$, auf
denen die Feldpfeile senkrecht stehen.
:::

:::kern
Der __Gradient__ $\nabla f$ steht **senkrecht** auf den __Niveauflächen__ ($f=\text{const}$, denn
$\nabla f\cdot\dot\gamma=0$ längs ihnen) und zeigt in die Richtung des **steilsten Anstiegs** (Richtungsableitung
$\nabla f\cdot v=|\nabla f|\cos\theta$ maximal für $v\parallel\nabla f$). Ein __Gradientenfeld__ ist $E=\nabla\phi$
mit __Skalarpotential__ $\phi$ (Physik: $E=-\nabla\varphi$, Energie fällt längs Feldlinien). Notwendige
__Integrabilitätsbedingung__: $DE=(DE)^T$ symmetrisch, d.h. $\partial E_j/\partial x_k=\partial E_k/\partial x_j$
(Schwarz) — notwendig, nicht hinreichend (Gebiet mit Löchern → Poincaré später). __Radialsymmetrisch__:
$u(x)=f(r)$, $r=|x|$, mit $\nabla r=\hat e_r=x/r$ (__radialer Einheitsvektor__) folgt die Gradientenformel
$\nabla u=f'(r)\,\hat e_r$. Jedes radialsymmetrische __Zentralfeld__ $F=f(r)\hat e_r$ ist ein Gradientenfeld mit
$\varphi(r)=\int f(r)\,dr$. Beispiel Coulomb: $u=\tfrac{Q}{4\pi r}\Rightarrow E=-\nabla u=\tfrac{Q}{4\pi r^2}\hat e_r$.
:::

Der Gradient macht aus einem Skalarfeld ein Vektorfeld. Umgekehrt fragt man bei einem gegebenen Vektorfeld: Wie
stark **quillt** es an einem Punkt (Quelle/Senke) und wie stark **wirbelt** es? Diese beiden Maße sind die
__Divergenz__ und die __Rotation__ — die nächsten Differentialoperatoren der Vektoranalysis.

:::quiz
F: Warum steht der Gradient $\nabla f$ senkrecht auf den Niveauflächen?
A: Läuft man mit einer Kurve $\gamma$ innerhalb einer Niveaufläche, bleibt $f$ konstant, also $\frac{d}{dt}f(\gamma)=\nabla f\cdot\dot\gamma=0$. Da $\dot\gamma$ jede beliebige Tangentialrichtung annehmen kann und das Skalarprodukt stets null ist, muss $\nabla f$ auf allen Tangentialrichtungen — und damit auf der Fläche — senkrecht stehen.
F: Warum zeigt der Gradient in Richtung des steilsten Anstiegs, und was bedeutet sein Betrag?
A: Die Änderungsrate in Einheitsrichtung $v$ ist $\nabla f\cdot v=|\nabla f|\cos\theta$. Das ist maximal für $\cos\theta=1$, also $v\parallel\nabla f$. Daher zeigt der Gradient bergauf; sein Betrag $|\nabla f|$ ist die Steigung in dieser steilsten Richtung.
F: Wann ist die Richtungsableitung $\nabla f\cdot v$ null bzw. minimal — und was heißt das anschaulich?
A: Null bei $v\perp\nabla f$ (man läuft entlang der Niveaufläche, der Wert ändert sich nicht); minimal (steilster **Abstieg**) bei $v$ antiparallel zu $\nabla f$. Es ist dieselbe $\cos\theta$-Formel, nur $\theta=90°$ bzw. $180°$.
F: Was ist ein Gradientenfeld mit Skalarpotential, und warum schreibt die Physik $E=-\nabla\varphi$ statt $+$?
A: $E=\nabla\phi$ heißt Gradientenfeld, $\phi$ sein Potential. Das Minuszeichen in $E=-\nabla\varphi$ sorgt dafür, dass die potentielle Energie längs der Feldlinien **abnimmt**: $\frac{d}{dt}\varphi(\gamma)=\nabla\varphi\cdot\dot\gamma=-E\cdot\dot\gamma<0$, wenn $\dot\gamma$ parallel zu $E$ läuft. Für den bloßen Begriff ist das Vorzeichen egal.
F: Warum muss die Jacobi-Matrix eines Gradientenfelds symmetrisch sein?
A: Für $E=\nabla\phi$ sind ihre Einträge die zweiten Ableitungen des Potentials, $\partial E_j/\partial x_k=\partial^2\phi/(\partial x_k\partial x_j)$. Nach dem Satz von Schwarz vertauschen diese, also $\partial E_j/\partial x_k=\partial E_k/\partial x_j$ — die Matrix ist symmetrisch.
F: Warum ist die Integrabilitätsbedingung $DE=(DE)^T$ zwar notwendig, aber nicht hinreichend für ein Potential?
A: Notwendig folgt sie aus Schwarz. Nicht hinreichend: Auf einem Gebiet mit „Löchern" (nicht einfach zusammenhängend) kann ein Feld die Bedingung lokal überall erfüllen und trotzdem global kein Potential besitzen. Erst ein einfach zusammenhängendes Gebiet macht sie hinreichend (Poincaré-Lemma, später).
F: Warum ist $\nabla r=\frac{x}{r}=\hat e_r$, und was bedeutet dieses Feld anschaulich?
A: Mit der Kettenregel ist $\frac{\partial r}{\partial x_j}=\frac{x_j}{r}$, also $\nabla r=x/r$. Dieser Vektor zeigt radial nach außen und hat Länge 1: Der Abstand zum Ursprung wächst am schnellsten, wenn man **radial** nach außen läuft (Rate 1), und gar nicht, wenn man um das Zentrum kreist.
F: Warum gilt $\nabla u=f'(r)\,\hat e_r$ für $u(x)=f(r)$, und warum kann die steilste Richtung nur radial sein?
A: Kettenregel: $\nabla f(r)=f'(r)\,\nabla r=f'(r)\,\hat e_r$. Da $u$ nur vom Abstand abhängt, ändert sich der Wert tangential (entlang der Kreise/Kugeln $r=\text{const}$) überhaupt nicht — die einzige Richtung mit Änderung, und damit die steilste, ist die radiale.
F: Warum ist **jedes** radialsymmetrische Zentralfeld $F=f(r)\hat e_r$ ein Gradientenfeld, und worauf reduziert sich die Potentialsuche?
A: Setzt man $\varphi(r)=\int f(r)\,dr$, so ist nach der Gradientenformel $\nabla\varphi(r)=\varphi'(r)\hat e_r=f(r)\hat e_r=F$. Das (mehrdimensionale) Potentialproblem reduziert sich also auf eine **eindimensionale** Integration entlang des Radius.
F: Wie entsteht aus dem Coulomb-Potential $u=\frac{Q}{4\pi r}$ das $1/r^2$-Feld, und woher das Vorzeichen?
A: Die Gradientenformel mit $\frac{d}{dr}\frac1r=-\frac1{r^2}$ gibt $\nabla u=-\frac{Q}{4\pi r^2}\hat e_r$; das physikalische Feld $E=-\nabla u=\frac{Q}{4\pi r^2}\hat e_r$ zeigt also (für $Q>0$) nach außen. Das Minus stammt aus der Konvention $E=-\nabla\varphi$ (Energie fällt in Feldrichtung); der $1/r^2$-Abfall kommt direkt aus der Ableitung von $1/r$.
:::
