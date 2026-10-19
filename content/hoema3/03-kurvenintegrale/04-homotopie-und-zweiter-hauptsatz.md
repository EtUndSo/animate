---
title: Homotopieinvarianz und der zweite Hauptsatz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030400
summary: Von Grund auf – warum sich das Kurvenintegral eines wirbelfreien Feldes nicht ändert, wenn man den Weg stetig verformt (Homotopieinvarianz), und was ein einfach zusammenhängendes Gebiet ist (jede Schleife zusammenziehbar, „keine Löcher"). Daraus folgt der zweite Hauptsatz: Auf einfach zusammenhängenden Gebieten ist $\operatorname{rot}F=0$ global hinreichend für ein Potential – und das erklärt endlich den Wert $2\pi$ des Wirbelfelds.
tags: Homotopie, Homotopieinvarianz, einfach zusammenhängend, zweiter Hauptsatz, Integrabilitätsbedingung, Umlaufzahl, geschlitzte Ebene, Argumentfunktion
---

:::grafik
Einstiegs-Animation: Eine geschlossene Schleife in einem Vektorfeld wird **stetig verformt** (ein Schieberegler
$s$ zieht sie von einer Form in eine andere). Solange das Feld wirbelfrei ist, bleibt der Zähler
$\oint_{\gamma_s}F\cdot dx$ **konstant** — Homotopieinvarianz. Dann zwei Fälle: In einem Gebiet **ohne Loch** lässt
sich die Schleife ganz auf einen **Punkt** zusammenziehen, und das Integral wird null. Umschließt die Schleife
aber ein **Loch**, bleibt sie daran „hängen" — sie lässt sich nicht zusammenziehen, und der Umlaufwert (beim
Wirbelfeld $2\pi$) bleibt erhalten. Kernbotschaft: Der Wert eines wirbelfreien Kurvenintegrals hängt nur von der
**Topologie** ab — davon, welche Löcher der Weg umschlingt.
:::

:::konzept
Das Poincaré-Lemma war **lokal**. Jetzt die **globale** Sicht. Entscheidend ist eine schöne Stabilität: Für ein
**integrables** Feld ($\operatorname{rot}F=0$) ändert sich das Kurvenintegral **nicht**, wenn man den Weg stetig
verformt (homotopiert), ohne das Gebiet zu verlassen. Hat das Gebiet **keine Löcher** — ist es __einfach
zusammenhängend__ —, kann man jede geschlossene Schleife auf einen Punkt zusammenziehen, und dann ist jedes
geschlossene Integral null. Damit wird $\operatorname{rot}F=0$ **global** hinreichend für ein Potential (der
__zweite Hauptsatz__). Und dasselbe Prinzip erklärt endlich, warum das Wirbelfeld-Integral um den Ursprung immer
$2\pi$ gibt: Die Schleife bleibt am Loch hängen.
:::

**Worum es geht:** Wir zeigen die __Homotopieinvarianz__ des Kurvenintegrals für integrable Felder, definieren
__einfach zusammenhängend__, formulieren den __zweiten Hauptsatz__ und verstehen damit den $2\pi$-Umlauf.

## Homotopieinvarianz

Eine __Homotopie__ ist eine **stetige Deformation** einer Kurve in eine andere: eine Familie $\gamma_s(t)=h(s,t)$,
die mit dem Parameter $s\in[0,1]$ von einer Kurve $\gamma_0$ stetig in eine Kurve $\gamma_1$ übergeht. Für ein
Feld $F$, das die __Integrabilitätsbedingung__ $\frac{\partial F_j}{\partial x_k}=\frac{\partial F_k}{\partial x_j}$
erfüllt, berechnet man die Änderung des Integrals unter der Deformation. Mit der Vertauschungs-Identität
$\frac{\partial}{\partial s}\big(F(h)\cdot\partial_t h\big)=\frac{\partial}{\partial t}\big(F(h)\cdot\partial_s h\big)$
(Lemma 3.19, folgt aus Produkt- und Kettenregel plus Integrabilität) wird

$$\frac{d}{ds}\int_{\gamma_s} F\cdot dx = \int_a^b \frac{\partial}{\partial t}\Big(F(h(s,t))\cdot\partial_s h(s,t)\Big)dt = \Big[F(h(s,t))\cdot\partial_s h(s,t)\Big]_{t=a}^{t=b}.$$

Es bleibt also nur ein **Randterm** bei $t=a$ und $t=b$. Dieser verschwindet in genau den beiden Fällen, die
zählen:

- **(i) Homotopie geschlossener Kurven** ($h(s,a)=h(s,b)$ für alle $s$): Anfang und Ende bleiben während der
  ganzen Deformation zusammengeheftet.
- **(ii) Homotopie mit festen Endpunkten** ($\partial_s h(s,a)=\partial_s h(s,b)=0$): Die Endpunkte bewegen sich
  nicht.

In beiden Fällen ist also $\frac{d}{ds}\int_{\gamma_s}F\cdot dx=0$ — das Integral ist **invariant unter der
Deformation** (Satz 3.20). Kurz: Für wirbelfreie Felder darf man den Weg beliebig „verbiegen", solange Enden
festbleiben oder die Schleife geschlossen bleibt.

:::grafik
Eine Kurvenfamilie $\gamma_s=h(s,t)$, die von $\gamma_0$ zu $\gamma_1$ deformiert wird; der Integralwert als
Anzeige, die während der ganzen Deformation konstant bleibt. Daneben die beiden Randfälle: geschlossene Schleife
(Enden zusammen) und feste Endpunkte.
:::

## Einfach zusammenhängende Gebiete

Wann lässt sich eine Schleife ganz **wegdeformieren**? Ein Gebiet $G$ heißt __einfach zusammenhängend__, wenn sich
**jede** geschlossene Kurve in $G$ stetig (innerhalb $G$) auf einen **Punkt zusammenziehen** lässt. Anschaulich
in der Ebene: $G$ hat **keine Löcher**.

- **Nicht** einfach zusammenhängend: ein Ringgebiet oder die punktierte Ebene $\mathbb{R}^2\setminus\{0\}$ — eine
  Schleife um das Loch bleibt hängen.
- **Einfach** zusammenhängend: die **geschlitzte Ebene** $\mathbb{R}^2\setminus\{(x,0):x\le0\}$ — der Schlitz
  verhindert, dass eine Schleife das Loch ganz umrunden kann.
- Jedes __Sterngebiet__ ist einfach zusammenhängend (die Homotopie $h(s,t)=(1-s)\gamma(t)+s\,x_0$ zieht jede
  Schleife zum Sternzentrum $x_0$ zusammen).

**Stolperstein (höhere Dimensionen):** Für $n\ge3$ ist die Anschauung „keine Löcher" trügerisch. Der punktierte
Raum $\mathbb{R}^3\setminus\{0\}$ ist **einfach zusammenhängend** (eine Schleife kann am Loch „vorbei" nach außen
gezogen werden) — im Gegensatz zur punktierten Ebene.

## Der zweite Hauptsatz

Jetzt die globale Charakterisierung. Auf einem **einfach zusammenhängenden** Gebiet $G$ gilt für stetig
differenzierbare Felder (Satz 3.23):

$$F \text{ konservativ in } G \quad\Longleftrightarrow\quad F \text{ integrabel in } G\ (\operatorname{rot}F=0).$$

**Beweis (Idee).** Ist $\gamma$ eine geschlossene Kurve in $G$, so lässt sie sich (einfacher Zusammenhang) per
Homotopie auf einen **Punkt** zusammenziehen. Das Integral über den Punkt ist null, und nach der
Homotopieinvarianz ändert sich der Wert bei der Deformation nicht — also $\oint_\gamma F\cdot dx=0$. Da das für
jede geschlossene Kurve gilt, ist $F$ konservativ. $\square$

Das ist die **globale** Fassung des Poincaré-Lemmas: Dort brauchte man ein Sterngebiet, hier genügt der
schwächere (allgemeinere) einfache Zusammenhang. Beide sagen: Ohne Löcher wird aus „wirbelfrei" ein echtes
Potential.

## Warum gibt der Wirbel $2\pi$?

Damit klärt sich das Gegenbeispiel aus dem ersten Hauptsatz vollständig. Das Wirbelfeld
$F=\frac{1}{x^2+y^2}(-y,x)$ lebt auf der punktierten Ebene $\mathbb{R}^2\setminus\{0\}$ — die **nicht** einfach
zusammenhängend ist. Ein Kreis um den Ursprung lässt sich nicht zusammenziehen (das Loch ist im Weg), also greift
der zweite Hauptsatz nicht, und $\oint_{K_R}F\cdot dx=2\pi$ darf von null verschieden sein. Der Wert $2\pi$ ist
dabei nach der Homotopieinvarianz **für jede** das Loch einmal umschlingende Schleife gleich — er misst die
__Umlaufzahl__ (wie oft der Weg das Loch umrundet), nicht die genaue Form.

**Reparatur durch Aufschneiden.** Ersetzt man die punktierte durch die **geschlitzte** Ebene (die einfach
zusammenhängend ist), so besitzt dasselbe Feld plötzlich ein globales Potential — nämlich die __Argumentfunktion__
(den Polarwinkel) $\varphi(x,y)\in(-\pi,\pi)$, mit $\nabla\varphi=\frac{1}{x^2+y^2}(-y,x)=F$. Der Schlitz
verhindert gerade den vollen Umlauf, der $\varphi$ unstetig springen ließe. Schön zu sehen: **Dieselbe Formel,
anderes Gebiet — und schon existiert (oder fehlt) das Potential.**

:::grafik
Links die punktierte Ebene: ein Kreis um das Loch, der beim Zusammenziehen am Loch hängenbleibt → $\oint=2\pi$
(Umlaufzahl 1). Rechts die geschlitzte Ebene mit demselben Feld: Der Schlitz blockiert den Umlauf, die
Argumentfunktion $\varphi$ ist ein globales Potential ($\nabla\varphi=F$). Beschriftung „Loch → $2\pi$; Schlitz →
Potential existiert".
:::

:::kern
__Homotopie__ = stetige Deformation $\gamma_s=h(s,t)$ einer Kurve. Für __integrable__ Felder
($\operatorname{rot}F=0$) ist das Kurvenintegral **homotopieinvariant**: $\frac{d}{ds}\int_{\gamma_s}F\cdot dx=
[F(h)\cdot\partial_s h]_a^b=0$ bei (i) geschlossenen Kurven oder (ii) festen Endpunkten (Satz 3.20). Ein Gebiet ist
__einfach zusammenhängend__, wenn jede Schleife auf einen Punkt zusammenziehbar ist (2D: keine Löcher;
Ring/punktierte Ebene nein, geschlitzte Ebene ja; $\mathbb{R}^3\setminus\{0\}$ ja). Sterngebiete sind einfach
zusammenhängend. __Zweiter Hauptsatz__ (Satz 3.23): auf einfach zusammenhängendem $G$ ist $F$ konservativ
$\Leftrightarrow$ $\operatorname{rot}F=0$ (Beweis: Schleife zusammenziehen → $\oint=0$) — die globale Fassung des
Poincaré-Lemmas. Das Wirbelfeld $\tfrac{(-y,x)}{x^2+y^2}$ gibt $\oint=2\pi$, weil die punktierte Ebene **nicht**
einfach zusammenhängend ist (Umlaufzahl um das Loch); auf der geschlitzten Ebene ist die __Argumentfunktion__
$\varphi$ ein globales Potential.
:::

Wir haben Kurvenintegrale und die Frage nach Potentialen vollständig durchdrungen. Es fehlt noch der direkte
Zusammenhang zwischen einem **Randintegral** (längs einer geschlossenen Kurve) und einem **Flächenintegral** über
das eingeschlossene Gebiet — die __Integralsätze in der Ebene__ (Green und Gauß), das Thema des letzten Artikels
dieses Kapitels.
