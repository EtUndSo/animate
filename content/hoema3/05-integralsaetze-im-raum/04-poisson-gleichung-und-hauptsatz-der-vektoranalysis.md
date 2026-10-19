---
title: Poisson-Gleichung und Hauptsatz der Vektoranalysis
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050400
summary: Von Grund auf – wie die Integralsätze die Potentialtheorie tragen. Das Coulomb-Potential $\Phi(x)=\frac{1}{4\pi r}$ ist die Greensche Funktion des Laplace-Operators ($-\Delta\Phi=\delta$); damit löst $u=\Phi * f$ die Poisson-Gleichung $-\Delta u=f$. Der Nachweis nutzt den Satz von Gauß (kleine Kugel ausschneiden). Als Krönung folgt der Hauptsatz der Vektoranalysis (Helmholtz-Zerlegung): Jedes abklingende Feld zerfällt in $F=\nabla u+\operatorname{rot}A$ – einen Quellen- und einen Wirbelanteil.
tags: Poisson-Gleichung, Greensche Funktion, Fundamentallösung, Coulomb-Potential, Helmholtz-Zerlegung, Hauptsatz der Vektoranalysis, Vektorpotential, Eichung
---

:::grafik
Einstiegs-Animation: Zwei Teile. Links die __Poisson-Gleichung__: Eine Quelldichte $f$ erzeugt über die Faltung mit
dem Coulomb-Potential $\Phi=\frac{1}{4\pi r}$ ein Potential $u$; eine kleine Kugel $B_\varepsilon$ um den Aufpunkt wird
ausgeschnitten, und das Oberflächenmittel von $f$ über $S_\varepsilon$ strebt für $\varepsilon\to0$ gegen $f(x)$ —
daher $-\Delta u=f$. Rechts die __Helmholtz-Zerlegung__: Ein beliebiges Vektorfeld $F$ (gemischte Pfeile) wird in zwei
„reine" Felder aufgespalten — ein **Quellenfeld** $\nabla u$ (Pfeile aus Quellen heraus) und ein **Wirbelfeld**
$\operatorname{rot}A$ (geschlossene Ringe). Kernbotschaft: Gauß und Stokes machen aus Quellen und Wirbeln Potentiale.
:::

:::konzept
Die beiden räumlichen Integralsätze (Gauß, Stokes) sind kein Selbstzweck — sie sind das **Fundament der
Potentialtheorie und der Feldphysik**. Dieser Artikel zeigt ihre zwei großen Früchte. Erstens: Das Coulomb-Potential
$\Phi=\frac{1}{4\pi r}$ ist die __Greensche Funktion__ des Laplace-Operators, und damit löst die Faltung $u=\Phi * f$
die __Poisson-Gleichung__ $-\Delta u=f$ — die Gleichung des elektrostatischen Potentials. Zweitens der __Hauptsatz der
Vektoranalysis__ (Helmholtz-Zerlegung): **Jedes** hinreichend abklingende Vektorfeld zerfällt eindeutig in einen
**Quellenanteil** (ein Gradientenfeld) und einen **Wirbelanteil** (ein Rotationsfeld) — der Grund, warum man in der
Elektrodynamik mit einem Skalarpotential **und** einem Vektorpotential arbeitet.
:::

**Worum es geht:** Wir zeigen, dass $\Phi=\frac{1}{4\pi r}$ die __Greensche Funktion__ ist und $u=\Phi * f$ die
__Poisson-Gleichung__ $-\Delta u=f$ löst (Beweis mit Gauß), und beweisen den __Hauptsatz der Vektoranalysis__.

## Die Poisson-Gleichung und das Coulomb-Potential

Im Artikel über das Newtonpotential (Kap. 4) wurde bereits die Lösungsformel der Poisson-Gleichung $-\Delta u=f$ in
$\mathbb{R}^3$ angegeben:

$$u(x) = \int_{\mathbb{R}^3}\Phi(x-y)\,f(y)\,dy, \qquad \Phi(x)=\frac{1}{4\pi r},\ \ r=|x|.$$

Das __Coulomb-Potential__ $\Phi:\mathbb{R}^3\setminus\{0\}\to\mathbb{R}$ ist beliebig oft differenzierbar und
**harmonisch**, $\Delta\Phi=0$ in $\mathbb{R}^3\setminus\{0\}$; außerdem sind $\Phi$ und $\nabla\Phi$ lokal integrierbar
(die $1/r$- bzw. $1/r^2$-Singularität wird vom Volumenfaktor $r^2$ entschärft). Mit der Substitution $y\mapsto x-y$ ist
$u(x)=\int\Phi(y)\,f(x-y)\,dy$, und unter einer Abklingbedingung an $f$ darf man unter dem Integral differenzieren:

$$\nabla u(x)=\int_{\mathbb{R}^3}\nabla\Phi(y)\,f(x-y)\,dy, \qquad \Delta u(x)=\int_{\mathbb{R}^3}\Phi(y)\,\Delta_y f(x-y)\,dy.$$

## $\Phi$ ist die Greensche Funktion — Beweis mit Gauß

Jetzt zeigt sich, **warum** $\Phi$ genau das richtige Potential ist. Die Singularität bei $y=0$ behandelt man, indem
man eine kleine Kugel $B_\varepsilon(0)$ ausschneidet und den Grenzübergang $\varepsilon\downarrow0$ betrachtet. Auf
$\mathbb{R}^3\setminus B_\varepsilon(0)$ ist $\Phi$ harmonisch, das Vektorfeld $E(y)=\nabla\Phi(y)$ also divergenzfrei.
Mit $\varphi(y)=f(x-y)$ liefert die partielle Integration mit Rand (Satz von Gauß, Satz 5.18) — alle Volumenterme mit
$\Delta\Phi=0$ bzw. $\operatorname{div}E=0$ fallen weg —

$$-\Delta u(x)=\lim_{\varepsilon\downarrow0}\int_{S_\varepsilon}\frac{\partial\Phi}{\partial n}(y)\,f(x-y)\,d\sigma,$$

wobei $S_\varepsilon=\partial B_\varepsilon(0)$ und $n(y)=-\hat e_r$ das **äußere** Normalenfeld von $\mathbb{R}^3
\setminus B_\varepsilon$ (also die **innere** Normale der Kugel) ist. Mit $\nabla\Phi=-\frac{1}{4\pi r^2}\hat e_r$ wird
die Normalableitung

$$\frac{\partial\Phi}{\partial n}(y)=n\cdot\nabla\Phi(y)=(-\hat e_r)\cdot\Big(-\tfrac{1}{4\pi r^2}\hat e_r\Big)=\frac{1}{4\pi r^2}, \qquad\text{also } \frac{\partial\Phi}{\partial n}=\frac{1}{4\pi\varepsilon^2} \ \text{auf } S_\varepsilon.$$

Da $4\pi\varepsilon^2=|S_\varepsilon|$ gerade der Flächeninhalt der $\varepsilon$-Sphäre ist, ist das Randintegral das
**Oberflächenmittel** von $f$:

$$-\Delta u(x)=\lim_{\varepsilon\downarrow0}\frac{1}{|S_\varepsilon|}\int_{S_\varepsilon}f(x-y)\,d\sigma = f(x),$$

denn wegen der Stetigkeit von $f$ gilt $\big|\frac{1}{|S_\varepsilon|}\int_{S_\varepsilon}(f(x)-f(x-y))\,d\sigma\big|
\le\sup_{|x-y|<\varepsilon}|f(x)-f(x-y)|\to0$. Damit ist $-\Delta u=f$ bewiesen — und $\Phi$ als __Greensche Funktion__
(Fundamentallösung) des Laplace-Operators identifiziert: formal $-\Delta\Phi=\delta$. Das ist die exakte Begründung für
die im Newtonpotential-Artikel genutzte Relation.

:::grafik
Aufpunkt $x$, um ihn die kleine Kugel $B_\varepsilon$ mit der inneren Normale $n=-\hat e_r$; auf $S_\varepsilon$ ist
$\partial\Phi/\partial n=1/(4\pi\varepsilon^2)=1/|S_\varepsilon|$, das Randintegral wird zum Oberflächenmittel von $f$,
das für $\varepsilon\to0$ gegen $f(x)$ strebt. Beschriftung $-\Delta u=f$, $-\Delta\Phi=\delta$.
:::

## Der Hauptsatz der Vektoranalysis (Helmholtz-Zerlegung)

Nun die Krönung. **Satz 5.19 (Helmholtz-Zerlegung im $\mathbb{R}^3$).** Sei $F:\mathbb{R}^3\to\mathbb{R}^3$ ein zweimal
stetig differenzierbares Vektorfeld mit kompaktem Träger. Dann existiert eine Zerlegung

$$F=\nabla u+\operatorname{rot}A$$

mit zweimal stetig differenzierbaren $u:\mathbb{R}^3\to\mathbb{R}$ und $A:\mathbb{R}^3\to\mathbb{R}^3$.

Der Beweis ist eine elegante Kette der bisherigen Resultate: $\operatorname{div}F$ ist stetig differenzierbar, also
existiert nach der Lösungsformel (Satz 4.9) ein $u$ mit

$$\Delta u=\operatorname{div}F, \qquad\text{d.h.}\qquad \operatorname{div}(F-\nabla u)=0 \ \text{in } \mathbb{R}^3.$$

Das Restfeld $F-\nabla u$ ist also **divergenzfrei** — und nach dem __Poincaré-Lemma__ besitzt ein divergenzfreies Feld
(auf dem sternförmigen $\mathbb{R}^3$) ein __Vektorpotential__ $A$ mit $F-\nabla u=\operatorname{rot}A$. Zusammen:
$F=\nabla u+\operatorname{rot}A$. Dass $A$ zweimal stetig differenzierbar ist, folgt aus der Potentialformel (Lemma
3.13, Satz 2.1).

**Anschaulich** trennt die Zerlegung das Feld in zwei „reine" Bestandteile: $\nabla u$ trägt die **gesamte Divergenz**
(der **Quellenanteil**, denn $\operatorname{rot}\nabla u=0$), $\operatorname{rot}A$ trägt die **gesamte Rotation** (der
**Wirbelanteil**, denn $\operatorname{div}\operatorname{rot}A=0$). In der Elektrodynamik ist genau das der Grund für die
Potentiale: das elektrische Feld hat Quellen (Ladungen → Skalarpotential), das magnetische Feld ist quellenfrei, aber
wirbelbehaftet (Ströme → Vektorpotential).

**Eichfreiheit.** Das Vektorpotential $A$ ist nicht eindeutig: Addiert man ein Gradientenfeld $\nabla\psi$, so ändert
sich $\operatorname{rot}A$ nicht ($\operatorname{rot}\nabla\psi=0$). Man kann diese **Eichung** so wählen, dass
$\operatorname{div}A=0$ (Coulomb-Eichung) — dazu löst man $\Delta\psi=-\operatorname{div}A$ (dieselbe Art Gleichung wie
für $u$) und ersetzt $A$ durch $A+\nabla\psi$.

**Abschwächung der Voraussetzungen.** Der kompakte Träger ist entbehrlich: Es genügt die Abklingbedingung $F(x)=
o(1/|x|^2)$ für $|x|\to\infty$, die die Konvergenz der Potentialintegrale sichert. Für beliebig glatte Felder reicht
sogar irgendein Abklingen von $F$ samt aller Ableitungen — das bewies 1905 **Otto Blumenthal** (Mathematikprofessor an
der RWTH Aachen).

**Stolperstein:** (1) Das **Vorzeichen** $-\Delta u=f$ (gleichbedeutend $\Delta u=-f$) gehört zur Fundamentallösung
$-\Delta\Phi=\delta$; es ist dieselbe Konvention wie im Newtonpotential-Artikel. (2) Im Beweis ist $n$ die **innere**
Normale der ausgeschnittenen Kugel (= äußere Normale des Integrationsgebiets $\mathbb{R}^3\setminus B_\varepsilon$) —
daraus das positive Vorzeichen der Normalableitung. (3) Die Helmholtz-Zerlegung braucht **Abklingen** im Unendlichen;
ohne das ist sie nicht garantiert (und $A$ bleibt bis auf Eichung frei).

:::kern
Das __Coulomb-Potential__ $\Phi(x)=\frac{1}{4\pi r}$ ist harmonisch in $\mathbb{R}^3\setminus\{0\}$ und die __Greensche
Funktion__ (Fundamentallösung) des Laplace-Operators: $-\Delta\Phi=\delta$. Daher löst $u=\Phi * f=\int\Phi(x-y)f(y)\,dy$
die __Poisson-Gleichung__ $-\Delta u=f$. **Beweis** (Satz von Gauß): kleine Kugel $B_\varepsilon$ ausschneiden, $\Phi$
harmonisch ⇒ partielle Integration (Satz 5.18) lässt nur das Randintegral über $S_\varepsilon$ übrig; mit $\nabla\Phi=
-\frac{\hat e_r}{4\pi r^2}$, innerer Normale $n=-\hat e_r$ ist $\frac{\partial\Phi}{\partial n}=\frac{1}{4\pi\varepsilon^2}
=\frac{1}{|S_\varepsilon|}$, also $-\Delta u(x)=\lim_\varepsilon\frac{1}{|S_\varepsilon|}\int_{S_\varepsilon}f(x-y)\,
d\sigma=f(x)$. __Hauptsatz der Vektoranalysis__ (Helmholtz, Satz 5.19): jedes $C^2$-Feld $F$ mit kompaktem Träger (bzw.
$F=o(1/|x|^2)$) zerfällt in $F=\nabla u+\operatorname{rot}A$ — **Quellenanteil** + **Wirbelanteil**. Beweis: $\Delta u=
\operatorname{div}F$ lösen ⇒ $\operatorname{div}(F-\nabla u)=0$ ⇒ Poincaré-Lemma ⇒ $F-\nabla u=\operatorname{rot}A$.
Eichung $\operatorname{div}A=0$ via $\Delta\psi=-\operatorname{div}A$.
:::

Damit schließt das Kapitel über die Integralsätze im Raum: Gauß und Stokes verbinden Volumen, Fläche und Rand über
Divergenz und Rotation — und tragen Potentialtheorie und Feldphysik. Das nächste Kapitel wechselt das Thema und fragt,
**wie Folgen von Funktionen konvergieren** — punktweise gegen gleichmäßig — die Grundlage für Fourier-Reihen.

:::quiz
F: Was heißt es, dass das Coulomb-Potential $\Phi=\frac{1}{4\pi r}$ die „Greensche Funktion" des Laplace-Operators ist?
A: Es ist die Antwort auf eine Punktquelle: formal $-\Delta\Phi=\delta$. Weil der Laplace-Operator linear ist, erhält man die Lösung für eine beliebige Quelldichte $f$ durch Überlagerung (Faltung) der Punktantworten, also $u=\Phi*f$.
F: Warum ist es nötig, im Beweis eine kleine Kugel $B_\varepsilon$ um den Aufpunkt auszuschneiden?
A: Der Kern $\Phi$ ist bei $r=0$ singulär, und sein Laplace ist dort eine $\delta$-Spitze — direktes Anwenden von Gauß ist unmöglich. Schneidet man $B_\varepsilon$ aus, ist $\Phi$ auf dem Rest harmonisch, und der ganze „Quellbeitrag" sammelt sich im Randintegral über $S_\varepsilon$.
F: Warum fallen beim Anwenden der partiellen Integration alle Volumenterme weg?
A: Außerhalb der kleinen Kugel ist $\Phi$ harmonisch ($\Delta\Phi=0$, also $\operatorname{div}\nabla\Phi=0$). In der Greenschen Formel multiplizieren die Volumenterme gerade diesen Ausdruck, sind also null — übrig bleibt nur das Oberflächenintegral über $S_\varepsilon$.
F: Warum ist auf $S_\varepsilon$ die Normalableitung $\partial\Phi/\partial n$ gerade $1/|S_\varepsilon|=1/(4\pi\varepsilon^2)$?
A: Mit $\nabla\Phi=-\frac{1}{4\pi r^2}\hat e_r$ und der (nach innen zeigenden) Normale $n=-\hat e_r$ ist $n\cdot\nabla\Phi=\frac{1}{4\pi r^2}$, auf $S_\varepsilon$ also $\frac{1}{4\pi\varepsilon^2}$. Das ist genau der Kehrwert des Kugelflächeninhalts $4\pi\varepsilon^2$.
F: Wieso strebt das Randintegral für $\varepsilon\to0$ gerade gegen $f(x)$?
A: Weil $\partial\Phi/\partial n=1/|S_\varepsilon|$ ist, ist das Randintegral das Oberflächenmittel von $f$ über die kleine Sphäre. Da $f$ stetig ist, strebt dieser Mittelwert gegen den Funktionswert im Zentrum, also $f(x)$.
F: Was besagt der Hauptsatz der Vektoranalysis (Helmholtz-Zerlegung) anschaulich?
A: Jedes hinreichend abklingende Vektorfeld lässt sich in zwei „reine" Teile zerlegen: einen Quellenanteil $\nabla u$ (trägt die gesamte Divergenz, ist wirbelfrei) und einen Wirbelanteil $\operatorname{rot}A$ (trägt die gesamte Rotation, ist quellenfrei).
F: Wie baut der Beweis der Helmholtz-Zerlegung auf den vorigen Resultaten auf?
A: Man löst zuerst $\Delta u=\operatorname{div}F$ (Poisson-Lösungsformel), dann ist $F-\nabla u$ divergenzfrei. Nach dem Poincaré-Lemma besitzt ein divergenzfreies Feld im sternförmigen $\mathbb{R}^3$ ein Vektorpotential $A$ mit $F-\nabla u=\operatorname{rot}A$ — zusammen $F=\nabla u+\operatorname{rot}A$.
F: Warum ist es kein Widerspruch, dass $\nabla u$ die Divergenz und $\operatorname{rot}A$ die Rotation „allein" trägt?
A: Es gilt $\operatorname{rot}\nabla u=0$ und $\operatorname{div}\operatorname{rot}A=0$ (beides Identitäten). Der Gradiententerm hat also keine Rotation, der Rotationsterm keine Divergenz — die beiden Anteile stören einander nicht und teilen die beiden „Eigenschaften" sauber auf.
F: Was bedeutet die Eichfreiheit des Vektorpotentials $A$, und wie nutzt man sie?
A: $A$ ist nur bis auf ein Gradientenfeld $\nabla\psi$ bestimmt, denn $\operatorname{rot}(A+\nabla\psi)=\operatorname{rot}A$. Man kann diese Freiheit nutzen, um $\operatorname{div}A=0$ zu erzwingen (Coulomb-Eichung), indem man $\Delta\psi=-\operatorname{div}A$ löst und $A$ durch $A+\nabla\psi$ ersetzt.
F: Warum braucht die Helmholtz-Zerlegung eine Abklingbedingung im Unendlichen?
A: Die Potentiale $u$ und $A$ werden über Faltungsintegrale mit dem Coulomb-Kern konstruiert; diese konvergieren nur, wenn $F$ hinreichend schnell abfällt (kompakter Träger oder $F=o(1/|x|^2)$). Ohne Abklingen ist die Existenz der Zerlegung nicht garantiert.
:::
