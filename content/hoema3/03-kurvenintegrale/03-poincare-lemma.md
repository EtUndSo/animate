---
title: Das Poincaré-Lemma
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030300
summary: Von Grund auf – wann die Bedingung $\operatorname{rot}F=0$ doch ein Potential garantiert. Auf sternförmigen Gebieten (ohne Löcher) ist sie hinreichend: $F$ ist genau dann ein Gradientenfeld, wenn $\operatorname{rot}F=0$, und genau dann ein Wirbelfeld, wenn $\operatorname{div}F=0$. Mit der expliziten Potentialkonstruktion (Integration längs Strahl bzw. Koordinatenachsen) und der Eichfreiheit.
tags: Poincaré-Lemma, Sterngebiet, einfach zusammenhängend, Skalarpotential, Vektorpotential, Integrabilitätsbedingung, Potentialkonstruktion, Eichfreiheit
---

:::grafik
Einstiegs-Animation: Ein __Sterngebiet__ — eine Fläche, von deren Zentrum $x_0$ aus man jeden Punkt auf einer
**geraden Strecke** sehen kann (die Strecken leuchten auf, bleiben ganz im Gebiet). Für ein wirbelfreies Feld
$F$ ($\operatorname{rot}F=0$) wird das Potential $\phi$ gebaut, indem man $F$ **entlang dieser Strahlen** (oder
treppenförmig längs der Koordinatenachsen) aufintegriert. Daneben zum Kontrast die punktierte Ebene mit Loch:
Sie ist um das Loch herum **nicht** sternförmig — hier scheitert die globale Konstruktion (Wirbelfeld aus dem
vorigen Artikel). Kernbotschaft: Ohne Löcher wird aus „wirbelfrei" ein echtes Potential.
:::

:::konzept
Der vorige Artikel ließ eine Frage offen: $\operatorname{rot}F=0$ ist **notwendig** für ein Gradientenfeld —
aber wann ist es auch **hinreichend**? Die Antwort hängt allein an der **Gestalt des Gebiets**. Das
__Poincaré-Lemma__ sagt: Auf einem Gebiet **ohne Löcher** (sternförmig bzw. einfach zusammenhängend) genügt
$\operatorname{rot}F=0$, damit $F$ ein Skalarpotential besitzt — und spiegelbildlich genügt $\operatorname{div}F=0$
für ein Vektorpotential. **Lokal** (in jeder kleinen Kugel) gilt das immer. Noch besser: Der Beweis **liefert das
Potential gleich mit**, als explizites Integral — man kann es also konkret ausrechnen.
:::

**Worum es geht:** Wir formulieren das __Poincaré-Lemma__ (lokal und auf __Sterngebieten__), verstehen die
**explizite Potentialkonstruktion** (Strahl- bzw. Achsenintegration) und klären Eindeutigkeit und Eichfreiheit.

## Das Lemma auf einer Kugel

Der Kern ist eine lokale Aussage. Sei $F$ ein stetig differenzierbares Vektorfeld auf einer Kugel
$B_R(0)\subset\mathbb{R}^3$. Dann gilt:

- Ist $\operatorname{rot}F = 0$, so ist $F$ ein **Gradientenfeld** mit explizitem Potential
  $$F(x) = \nabla\!\left(\int_0^1 F(tx)\cdot x\,dt\right).$$
- Ist $\operatorname{div}F = 0$, so ist $F$ ein **Wirbelfeld** mit explizitem Vektorpotential
  $$F(x) = \operatorname{rot}\!\left(\int_0^1 F(tx)\times tx\,dt\right).$$
- Ist $F$ zweimal stetig differenzierbar mit $\operatorname{div}F=0$ **und** $\operatorname{rot}F=0$, so ist $F$
  __harmonisch__, $\Delta F = 0$.

**Beweisidee (erste Formel).** Man zieht den Gradienten unter das Integral (erlaubt nach dem Satz über
Parameterintegrale) und bildet die $k$-te Komponente. Mit der Produktregel und $y=tx$:

$$\int_0^1 \frac{\partial}{\partial x_k}\Big(\sum_j F_j(tx)\,x_j\Big)dt = \int_0^1\Big(\sum_j \frac{\partial F_k}{\partial y_j}(tx)\,t x_j + F_k(tx)\Big)dt,$$

wobei die **Integrabilitätsbedingung** $\frac{\partial F_j}{\partial y_k}=\frac{\partial F_k}{\partial y_j}$ (aus
$\operatorname{rot}F=0$) benutzt wurde, um $\frac{\partial F_j}{\partial x_k}$ durch $\frac{\partial F_k}{\partial
y_j}$ zu ersetzen. Der Integrand ist jetzt gerade die **volle Ableitung** $\frac{d}{dt}\big(t\,F_k(tx)\big)$,
also

$$\int_0^1 \frac{d}{dt}\big(t\,F_k(tx)\big)\,dt = \big[t\,F_k(tx)\big]_0^1 = F_k(x). \qquad\square$$

Die dritte Aussage folgt sofort: Aus $F=\nabla\phi$ und $\operatorname{div}F=0$ wird $\Delta\phi=0$, und damit
$\Delta F=\Delta\nabla\phi=\nabla\Delta\phi=0$.

## Sterngebiete und die globale Version

Durch Verschiebung gilt dasselbe für jede Kugel $B_R(x_0)$ — und allgemeiner für **Sterngebiete**. Ein
__Sterngebiet__ ist eine offene Menge $G$, in der es einen Punkt $x_0$ gibt, sodass **jede gerade
Verbindungsstrecke** von $x_0$ zu einem beliebigen anderen Punkt ganz in $G$ liegt. (Jede Kugel und jede konvexe
Menge ist sternförmig.) Darauf wird das Poincaré-Lemma zur vollen Äquivalenz (Satz 3.15), denn die eine Richtung
ist die Notwendigkeit aus Kapitel 1:

$$F \text{ Gradientenfeld} \iff \operatorname{rot}F = 0, \qquad F \text{ Wirbelfeld} \iff \operatorname{div}F = 0.$$

**Stolperstein:** Entscheidend ist „keine Löcher". Die punktierte Ebene $\mathbb{R}^2\setminus\{0\}$ aus dem
vorigen Artikel ist **nicht** sternförmig (kein Punkt sieht die ganze Menge, weil das Loch im Weg ist) — deshalb
scheitert dort trotz $\operatorname{rot}F=0$ die globale Potentialbildung. **Lokal**, in jeder kleinen
lochfreien Kugel, existiert das Potential aber immer.

:::grafik
Links ein Sterngebiet mit Zentrum $x_0$ und mehreren geraden Sichtstrahlen zu Randpunkten (alle im Gebiet).
Rechts die punktierte Ebene: vom „Zentrum" aus wird die Sichtlinie zu einem Punkt hinter dem Loch unterbrochen —
kein Sterngebiet. Beschriftung „sternförmig → rot F=0 reicht; Loch → nur lokal".
:::

## Das Potential praktisch berechnen

Die Formel $\phi(x)=\int_0^1 F(tx)\cdot x\,dt$ ist ein Kurvenintegral längs des **Strahls** $y(t)=tx$. Wegen der
Wegunabhängigkeit darf man aber jeden bequemen Weg nehmen — oft am einfachsten **treppenförmig entlang der
Koordinatenachsen**. Für $\operatorname{rot}F=0$ auf einer Kugel um $x_0=(x_0,y_0,z_0)$ ist

$$\phi(x,y,z) = \int_{x_0}^{x} F_1(t,y_0,z_0)\,dt + \int_{y_0}^{y} F_2(x,t,z_0)\,dt + \int_{z_0}^{z} F_3(x,y,t)\,dt$$

ein Skalarpotential: Man integriert zuerst $F_1$ in $x$-Richtung (bei festem $y_0,z_0$), dann $F_2$ in
$y$-Richtung (beim schon erreichten $x$), dann $F_3$ in $z$-Richtung.

**Eigenes Beispiel.** Sei $F(x,y,z) = (2xy,\ x^2+z^2,\ 2yz)$. Man prüft $\operatorname{rot}F=0$. Mit $x_0=0$
(das lässt viele Terme wegfallen):

$$\phi = \underbrace{\int_0^x 2t\cdot 0\,dt}_{=\,0} + \int_0^y (x^2+0)\,dt + \int_0^z 2y\,t\,dt = x^2 y + y z^2.$$

Probe: $\nabla(x^2 y + y z^2) = (2xy,\ x^2+z^2,\ 2yz) = F$. ✓ Die Achsenmethode rekonstruiert das Potential in drei
gewöhnlichen Integralen.

:::grafik
Der treppenförmige Integrationsweg von $x_0$ zu $(x,y,z)$: erst in $x$-, dann in $y$-, dann in $z$-Richtung, mit
den drei Teilintegralen $\int F_1$, $\int F_2$, $\int F_3$ beschriftet. Daneben die Probe $\nabla\phi=F$.
:::

## Eindeutigkeit und Eichfreiheit

Wie eindeutig ist das Potential? Ein __Skalarpotential__ ist auf einem zusammenhängenden Gebiet **bis auf eine
additive Konstante** eindeutig: $\nabla g=\nabla h \Leftrightarrow \nabla(g-h)=0 \Leftrightarrow g-h=\text{const}$.
Ein __Vektorpotential__ ist noch freier — man darf ein beliebiges Gradientenfeld addieren, denn

$$F = \operatorname{rot}A = \operatorname{rot}(A+\nabla\psi),$$

da $\operatorname{rot}\nabla\psi=0$. Das ist die __Eichfreiheit__. Man nutzt sie, um bequeme Zusatzbedingungen zu
erfüllen, etwa die __Coulomb-Eichung__ $\operatorname{div}A=0$: Zu einem gegebenen $A_0$ addiert man $\nabla\psi$
mit $\Delta\psi=-\operatorname{div}A_0$ (eine Poisson-Gleichung), und das neue $A$ ist divergenzfrei. Damit
schließt sich der Kreis zu den Identitäten aus Kapitel 1.

:::kern
Das __Poincaré-Lemma__ macht die notwendigen Bedingungen aus Kapitel 1 lokal **hinreichend**. Auf einer Kugel
(allgemeiner einem __Sterngebiet__: jeder Punkt vom Zentrum $x_0$ aus geradlinig erreichbar) gilt für stetig
differenzierbare $F$: $\operatorname{rot}F=0 \Rightarrow F=\nabla\big(\int_0^1 F(tx)\cdot x\,dt\big)$
(Gradientenfeld) und $\operatorname{div}F=0 \Rightarrow F=\operatorname{rot}\big(\int_0^1 F(tx)\times tx\,dt\big)$
(Wirbelfeld); bei beidem ist $F$ harmonisch. Auf Sterngebieten also die Äquivalenzen (Satz 3.15):
$F$ Gradientenfeld $\Leftrightarrow \operatorname{rot}F=0$, $F$ Wirbelfeld $\Leftrightarrow \operatorname{div}F=0$.
**Praktisch** baut man das Skalarpotential durch Integration **längs der Koordinatenachsen**
$\phi=\int_{x_0}^x F_1(t,y_0,z_0)dt+\int_{y_0}^y F_2(x,t,z_0)dt+\int_{z_0}^z F_3(x,y,t)dt$ (eigenes Beispiel
$F=(2xy,x^2+z^2,2yz)\Rightarrow\phi=x^2y+yz^2$). Skalarpotential eindeutig bis auf Konstante, Vektorpotential bis
auf $\nabla\psi$ (__Eichfreiheit__; Coulomb-Eichung $\operatorname{div}A=0$). **Stolperstein:** nur ohne Löcher
global — die punktierte Ebene ist kein Sterngebiet.
:::

Das Poincaré-Lemma klärt den **lokalen** Fall. Was aber passiert **global**, wenn ein Weg ein Loch umschlingt —
und warum gibt der Wirbelfeld-Umlauf immer $2\pi$, egal wie der Weg genau aussieht? Das beantwortet die
__Homotopieinvarianz__ und der __zweite Hauptsatz__ für Kurvenintegrale im nächsten Artikel.
