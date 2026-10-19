---
title: Der Satz von Stokes im Raum
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050200
summary: Von Grund auf – der räumliche Satz von Stokes verknüpft die Zirkulation eines Vektorfelds längs der Randkurve einer Fläche mit dem Fluss seiner Rotation durch die Fläche, $\int_{\mathcal F}\operatorname{rot}F\cdot dS=\oint_{\partial\mathcal F}F\cdot dx$. Zuvor wird das Flussintegral $\int_{\mathcal F}F\cdot dS=\int_{\mathcal F}F\cdot n\,d\sigma$ über ein orientiertes Flächenstück definiert. Als Anwendung: Warum ein divergenzfreies Feld (Monopol) trotzdem kein Rotationsfeld sein muss.
tags: Satz von Stokes, Flussintegral, orientierte Fläche, Normalenfeld, Rotation, Zirkulation, Rotationsfeld, Vektorpotential, Rechte-Hand-Regel
---

:::grafik
Einstiegs-Animation: Eine gewölbte, orientierte Fläche $\mathcal{F}$ mit nach oben zeigendem Normalenfeld $n$ und
ihrer Randkurve $\partial\mathcal{F}$. Durch die Fläche strömt das Wirbelfeld $\operatorname{rot}F$ (Pfeile durch die
Maschen) — sein __Fluss__ $\int_{\mathcal F}\operatorname{rot}F\cdot dS$. Entlang des Randes läuft gleichzeitig die
__Zirkulation__ $\oint_{\partial\mathcal F}F\cdot dx$. Die __Rechte-Hand-Regel__ wird gezeigt: Daumen in Richtung $n$,
die Finger weisen in die Umlaufrichtung von $\partial\mathcal{F}$. Kernbotschaft (Stokes): Die beiden Größen sind
**gleich** — der Wirbel im Inneren treibt gerade die Randumströmung an.
:::

:::konzept
Der ebene Satz von Green hat die Zirkulation längs einer geschlossenen Kurve mit einem Flächenintegral der Rotation
verbunden. Der __Satz von Stokes__ hebt das in den **Raum**: Jetzt ist die Fläche nicht mehr eben, sondern eine
beliebig gewölbte Fläche im $\mathbb{R}^3$, und die Rotation $\operatorname{rot}F$ ist ein echtes Vektorfeld. Die
Aussage bleibt dieselbe: __Zirkulation am Rand = Rotationsfluss durch die Fläche__. Das ist das Herzstück der
Elektrodynamik (Faradaysches Induktionsgesetz, Ampèresches Gesetz) und klärt zugleich eine feine Frage: Wann ist
ein Feld ein __Rotationsfeld__ $F=\operatorname{rot}A$? Divergenzfreiheit allein reicht — anders als man denkt —
nicht aus.
:::

**Worum es geht:** Wir orientieren ein Flächenstück über sein __Normalenfeld__, definieren das __Flussintegral__
$\int_{\mathcal F}F\cdot dS$, formulieren und begründen den __Satz von Stokes im Raum__ und klären über Beispiele,
wann ein Feld ein __Rotationsfeld__ ist.

## Orientierung und das Flussintegral

Das Normalenfeld eines regulären Flächenstücks,

$$n(x(u,v)) = \frac{x_u\times x_v}{|x_u\times x_v|}, \qquad x_u=\frac{\partial x}{\partial u},\ \ x_v=\frac{\partial x}{\partial v},$$

ist bis auf die Umkehrung $n\mapsto -n$ unabhängig von der Parametrisierung und legt eine __Orientierung__ der Fläche
fest; man spricht dann von einem __orientierten (parametrisierten) Flächenstück__. Eine Vertauschung $(u,v)\mapsto
(v,u)$ im Parameterraum kehrt die Orientierung um. Für ein in einer Umgebung stetiges Vektorfeld $F$ definiert man das
__Flussintegral__ (Def. 5.9)

$$\int_{\mathcal F} F\cdot dS := \int_{\mathcal F} F\cdot n\,d\sigma.$$

Es misst, wie viel von $F$ **netto durch die Fläche hindurchströmt** (nur die Normalkomponente $F\cdot n$ zählt). Für
eine mit der Orientierung verträgliche Parametrisierung $x=x(u,v)$ über $G$ verschwindet der störende Normierungsnenner
und man erhält die Rechenformel (Bem. 5.10)

$$\int_{\mathcal F} F\cdot dS = \int_G F(x(u,v))\cdot (x_u\times x_v)(u,v)\,du\,dv.$$

Das ungekürzte $x_u\times x_v$ (nicht das normierte $n$) trägt den Flächenfaktor $|x_u\times x_v|=\sqrt{EG-F^2}$ gleich
in sich — Normierung und Oberflächenelement heben sich weg.

## Der Satz von Stokes im Raum

Ist $F$ in einer Umgebung des orientierten regulären Flächenstücks $\mathcal{F}$ **stetig differenzierbar**, so gilt
(Satz 5.11):

$$\int_{\mathcal F} \operatorname{rot}F\cdot dS = \oint_{\partial\mathcal F} F\cdot dx.$$

In Worten: Der __Fluss der Rotation__ durch die Fläche ist gleich der __Zirkulation__ von $F$ längs der Randkurve
$\partial\mathcal{F}$. Entscheidend ist die __Orientierungskopplung__: Die Randkurve wird so durchlaufen, dass die
Bildkurve mit dem Normalenfeld $n$ eine **Rechtsschraube** bildet (Rechte-Hand-Regel: Daumen $\parallel n$, Finger
zeigen die Umlaufrichtung). Konkret: Ist $\Phi:B\to\mathbb{R}^3$ eine orientierungstreue Parametrisierung und $\partial
B$ **positiv** (mathematisch positiv, gegen den Uhrzeigersinn) durchlaufen, so durchläuft die Bildkurve den Rand
$\partial\mathcal{F}=\Phi(\partial B)$ gerade im Sinne des Satzes (Bem. 5.12).

:::grafik
Orientierte Fläche mit Normale $n$ und Randkurve $\partial\mathcal F$; daneben dieselbe Fläche im Parameterraum als
Bereich $B$ mit positiv (gegen den Uhrzeigersinn) orientiertem Rand $\partial B$, dessen Bild $\Phi(\partial B)=
\partial\mathcal F$ ist. Rechte-Hand-Regel hervorgehoben.
:::

## Warum der Satz gilt — Rückführung auf Green

Für eine zweimal stetig differenzierbare Parametrisierung $\Phi=\Phi(u,v)$ mit $\mathcal{F}=\Phi(B)$ lässt sich Stokes
im Raum auf den **ebenen Satz von Green** zurückführen. Man definiert das ebene Hilfsfeld $(P,Q)^T$ durch

$$P(u,v):=F(\Phi(u,v))\cdot\frac{\partial\Phi}{\partial u}(u,v), \qquad Q(u,v):=F(\Phi(u,v))\cdot\frac{\partial\Phi}{\partial v}(u,v).$$

Beim Ausrechnen von $\partial Q/\partial u-\partial P/\partial v$ heben sich die zweiten Ableitungen von $\Phi$ heraus,
und es bleibt genau der Rotationsfluss-Integrand:

$$\left(\frac{\partial Q}{\partial u}-\frac{\partial P}{\partial v}\right)(u,v) = (\operatorname{rot}F)(\Phi(u,v))\cdot\left(\frac{\partial\Phi}{\partial u}\times\frac{\partial\Phi}{\partial v}\right)(u,v).$$

Mit der Rechenformel für das Flussintegral und der __Greenschen Formel__ folgt

$$\int_{\mathcal F}\operatorname{rot}F\cdot dS = \int_B\left(\frac{\partial Q}{\partial u}-\frac{\partial P}{\partial v}\right)du\,dv = \oint_{\partial B}P\,du+Q\,dv,$$

und per Kettenregel $dx=\frac{\partial\Phi}{\partial u}du+\frac{\partial\Phi}{\partial v}dv$ wird aus $\oint_{\partial B}
P\,du+Q\,dv$ gerade $\oint_{\partial\mathcal F}F(x)\cdot dx$ — das war zu zeigen. Der ebene Satz von Green ist also
genau der Spezialfall einer flachen Fläche (dort ist $\operatorname{rot}F\cdot n$ die skalare Rotation $\partial_x
F_2-\partial_y F_1$).

## Wann ist $F$ ein Rotationsfeld?

Ein Feld heißt __Rotationsfeld__ (oder besitzt ein __Vektorpotential__), wenn $F=\operatorname{rot}A$ für ein Feld $A$.
Notwendig ist $\operatorname{div}F=0$ (denn $\operatorname{div}\operatorname{rot}A=0$). Reicht das **lokal** (Poincaré-
Lemma auf sternförmigen Gebieten, Kapitel 1), so ist es **global** subtil:

**Monopolfeld (radiales Feld).** Betrachte auf $U=\mathbb{R}^3\setminus\{0\}$ das Feld $E(x)=\frac{Q}{4\pi r^2}\,
\hat e_r$. Es ist wirbelfrei ($\operatorname{rot}E=0$, also ein Gradientenfeld $E=-\nabla\varphi$ mit $\varphi=\frac{Q}
{4\pi r}$) **und** divergenzfrei ($\operatorname{div}E=0$). Ist es trotzdem ein Rotationsfeld? Der Fluss durch jede
Kugeloberfläche $S_R=\partial B_R(0)$ ist

$$\int_{S_R} E\cdot dS = \frac{Q}{4\pi R^2}\int_{S_R} d\sigma = \frac{Q}{4\pi R^2}\cdot 4\pi R^2 = Q \neq 0.$$

Wäre $E=\operatorname{rot}A$, so zerlegte man $S_R$ in obere und untere Hemisphäre, die den Äquator $\gamma_R$ als
gemeinsame Randkurve **mit entgegengesetzter Orientierung** teilen. Nach Stokes wäre dann $\int_{S_R}E\cdot dS=
\int_{\gamma_R}A\cdot dx+\int_{-\gamma_R}A\cdot dx=0$ — Widerspruch zu $Q\neq0$. **Also ist $E$ kein Rotationsfeld**,
obwohl $\operatorname{div}E=0$. Der Grund: $U=\mathbb{R}^3\setminus\{0\}$ enthält geschlossene Flächen (die Kugel), die
**kein** Gebiet in $U$ berandet (der Ursprung fehlt).

Die richtige Bedingung ist daher **geometrisch** (Satz 5.15): Ist $U\subset\mathbb{R}^3$ ein Gebiet, in dem **jede**
geschlossene stückweise reguläre Fläche $\mathcal{F}\subset U$ der Rand $\mathcal{F}=\partial V$ eines regulären
Bereichs $V\subset U$ ist, so gilt für stetig differenzierbares $F$:

$$F \text{ ist Rotationsfeld in } U \quad\Longleftrightarrow\quad \operatorname{div}F=0 \text{ in } U.$$

Dies ist das **Gegenstück zum Poincaré-Lemma** (dort: sternförmig + $\operatorname{rot}F=0$ ⇒ Gradientenfeld).

:::grafik
Links: Monopolfeld $E=\frac{Q}{4\pi r^2}\hat e_r$ radial nach außen; Flussbilanz durch eine Kugel $=Q$; die Kugel in
obere/untere Hemisphäre zerlegt mit gemeinsamem Äquator $\gamma_R$ in Gegenrichtung. Rechts die Bedingung von Satz
5.15: ein „gutes" Gebiet (jede geschlossene Fläche berandet ein Teilgebiet) vs. $\mathbb{R}^3\setminus\{0\}$ mit dem
fehlenden Punkt im Zentrum.
:::

**Stolperstein:** (1) **Orientierung koppeln** — Normalenrichtung $n$ und Umlaufsinn von $\partial\mathcal{F}$ müssen
per Rechter-Hand-Regel zusammenpassen; dreht man $n$ um, kehrt sich das Vorzeichen des Randintegrals um. (2) Für
Stokes zählt nur $\operatorname{rot}F$ und der **Rand** — zwei Flächen mit **derselben** Randkurve liefern denselben
Rotationsfluss. (3) $\operatorname{div}F=0$ ist für ein Vektorpotential **notwendig, aber nicht hinreichend**; die
Topologie des Gebiets (Satz 5.15) entscheidet.

:::kern
__Orientierung__ via Normalenfeld $n=\frac{x_u\times x_v}{|x_u\times x_v|}$ (bis auf $n\mapsto-n$); __Flussintegral__
$\int_{\mathcal F}F\cdot dS=\int_{\mathcal F}F\cdot n\,d\sigma=\int_G F(x(u,v))\cdot(x_u\times x_v)\,du\,dv$ (nur die
Normalkomponente zählt). __Satz von Stokes im Raum__: für $C^1$-Feld $F$ gilt $\int_{\mathcal F}\operatorname{rot}F
\cdot dS=\oint_{\partial\mathcal F}F\cdot dx$ (Rotationsfluss = Zirkulation), Rand per __Rechter-Hand-Regel__ zu $n$
orientiert. Beweis: Rückführung auf __Green__ über $P=F\cdot\Phi_u$, $Q=F\cdot\Phi_v$, mit $\partial_u Q-\partial_v P
=\operatorname{rot}F\cdot(\Phi_u\times\Phi_v)$. __Rotationsfeld__ $F=\operatorname{rot}A$ ⇒ $\operatorname{div}F=0$
(notwendig). Umkehrung nur auf Gebieten, wo jede geschlossene Fläche ein Teilgebiet berandet (Satz 5.15): dort
$F$ Rotationsfeld $\Leftrightarrow\operatorname{div}F=0$. **Gegenbeispiel** Monopol $E=\frac{Q}{4\pi r^2}\hat e_r$ auf
$\mathbb{R}^3\setminus\{0\}$: $\operatorname{div}E=0$, aber Fluss durch die Kugel $=Q\neq0$ ⇒ **kein** Rotationsfeld.
:::

Stokes verbindet Fläche und Rand über die **Rotation**. Das zweite große Raumtheorem verknüpft ein **Volumen** mit
seiner Randfläche über die **Divergenz**: der __Satz von Gauß im Raum__ — das Thema des nächsten Artikels.
