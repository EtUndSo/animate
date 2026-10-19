---
title: Parameterintegrale und Ableiten unter dem Integral
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020100
summary: Von Grund auf – wenn eine Funktion durch ein Integral mit einem Parameter definiert ist, $F(x)=\int_a^b f(x,t)\,dt$. Wann ist $F$ stetig und differenzierbar, und darf man die Ableitung ins Integral ziehen ($\frac{\partial F}{\partial x_k}=\int_a^b\frac{\partial f}{\partial x_k}\,dt$)? Mit der Leibnizregel für den Fall, dass auch die Integrationsgrenzen vom Parameter abhängen.
tags: Parameterintegral, Ableiten unter dem Integral, Vertauschbarkeit, Leibnizregel, variable Grenzen, stetig differenzierbar
---

:::grafik
Einstiegs-Animation: Eine Kurvenschar $t\mapsto f(x,t)$ über dem Intervall $[a,b]$, bei der ein Schieberegler den
__Parameter__ $x$ verändert — die Kurve verformt sich, und die **Fläche darunter** (das Integral) ändert sich
mit. Daneben wird diese Fläche als Funktion $F(x)=\int_a^b f(x,t)\,dt$ des Parameters aufgetragen. Ein
Pfeil zeigt die Kernfrage: Darf man die Ableitung $\frac{d}{dx}$ einfach **in** das Integral hineinziehen? Eine
kleine Animation „$\frac{\partial}{\partial x}$ wandert durch das Integralzeichen". Kernbotschaft: Unter milden
Stetigkeitsbedingungen vertauschen Ableitung und Integral.
:::

:::konzept
Sehr viele wichtige Funktionen sind gar nicht durch eine Formel, sondern durch ein **Integral mit einem Parameter**
gegeben — die Gamma-Funktion, die Fourier- und Laplace-Transformierte, Potentiale in der Feldtheorie. Für solche
Funktionen stellt sich sofort die Frage: Sind sie stetig? Differenzierbar? Und wenn ja — darf man die Ableitung
nach dem Parameter einfach **unter das Integralzeichen ziehen**? Diese Vertauschung von Ableitung und Integral ist
eines der meistgenutzten Werkzeuge der angewandten Mathematik. Dieses Kapitel klärt, wann sie erlaubt ist — und
die __Leibnizregel__ ergänzt den Fall, dass sogar die Integrationsgrenzen vom Parameter abhängen.
:::

**Worum es geht:** Wir definieren das __Parameterintegral__ $F(x)=\int_a^b f(x,t)\,dt$, klären seine
__Stetigkeit__ und __Differenzierbarkeit__ (Ableiten unter dem Integral) und leiten die __Leibnizregel__ für
variable Grenzen her.

## Das Parameterintegral

Ist $f(x,t)$ eine Funktion zweier Argumente, so kann man über **eine** Variable integrieren und die andere als
__Parameter__ stehen lassen. Das Ergebnis ist wieder eine Funktion — nur noch des Parameters:

$$F(x) := \int_a^b f(x,t)\,dt.$$

Hier ist $t$ die Integrationsvariable (sie „verschwindet" durch das Integrieren) und $x$ der Parameter, der als
Argument von $F$ übrig bleibt. Allgemein darf der Parameter sogar ein Vektor $x \in U \subset \mathbb{R}^n$ sein.
Die erste Frage: Überträgt sich die Glätte des Integranden $f$ auf $F$?

## Stetigkeit und Ableiten unter dem Integral

Die Antwort ist beruhigend. Für eine offene Menge $U \subset \mathbb{R}^n$ und einen **stetigen** Integranden
$f: U \times [a,b] \to \mathbb{R}$ gilt (Satz 2.1):

- **Stetigkeit:** $F(x) = \int_a^b f(x,t)\,dt$ ist stetig auf $U$.
- **Differenzierbarkeit:** Sind zusätzlich alle partiellen Ableitungen $\dfrac{\partial f}{\partial x_k}: U\times[a,b]
  \to \mathbb{R}$ stetig, so ist $F$ **stetig differenzierbar**, und man darf die Ableitung in das Integral ziehen:

$$\frac{\partial F}{\partial x_k}(x) = \int_a^b \frac{\partial f}{\partial x_k}(x,t)\,dt.$$

**Warum das geht (Beweisidee).** Man bildet den Differenzenquotienten in Richtung $x_k$ und wendet im Integranden
den **Mittelwertsatz** an: $\frac{f(x+h\hat e_k,t)-f(x,t)}{h} = \frac{\partial f}{\partial x_k}(x+\xi_h\hat e_k,t)$
mit einem Zwischenwert $\xi_h\in[0,h]$. Weil $\frac{\partial f}{\partial x_k}$ auf dem kompakten Bereich
$[0,h_0]\times[a,b]$ **gleichmäßig stetig** ist, darf man beim Grenzübergang $h\to 0$ den Limes ins Integral ziehen
— und übrig bleibt $\int_a^b \frac{\partial f}{\partial x_k}(x,t)\,dt$. Die gleichmäßige Stetigkeit (die der
Kompaktheit zu verdanken ist) ist der entscheidende Punkt; bei unendlichem Integrationsbereich fehlt sie, und
genau dann kann die Vertauschung scheitern (nächster Artikel).

:::grafik
Links der Differenzenquotient: zwei benachbarte Kurven $f(x,t)$ und $f(x+h,t)$, ihre Differenz geteilt durch $h$,
die sich der Ableitungskurve $\frac{\partial f}{\partial x}(x,t)$ annähert. Rechts das Fazit „$\frac{\partial}{\partial x}\int
= \int\frac{\partial}{\partial x}$", darunter die Bedingung „Integrand und seine $x$-Ableitung stetig, Bereich
$[a,b]$ endlich".
:::

**Eigenes Beispiel.** Für $F(s) = \int_0^1 x^s\,dx = \dfrac{1}{s+1}$ (mit Parameter $s > -1$) liefert das Ableiten
unter dem Integral $F'(s) = \int_0^1 x^s \ln x\,dx$. Andererseits ist $F'(s) = -\dfrac{1}{(s+1)^2}$. Man hat also
ganz nebenbei das nichttriviale Integral $\int_0^1 x^s\ln x\,dx = -\dfrac{1}{(s+1)^2}$ ausgerechnet — ein
typischer Nutzen der Methode: schwierige Integrale über die Ableitung nach einem Parameter knacken.

## Die Leibnizregel: wenn auch die Grenzen mitlaufen

Oft hängen nicht nur der Integrand, sondern auch die **Integrationsgrenzen** vom Parameter ab. Dann kommen zur
Ableitung zwei „Randterme" hinzu. Ist $f$ stetig differenzierbar und sind $\alpha, \beta$ stetig differenzierbare
Grenzfunktionen, so gilt für

$$F(y) = \int_{\alpha(y)}^{\beta(y)} f(x,y)\,dx$$

die __Leibnizregel__:

$$F'(y) = \int_{\alpha(y)}^{\beta(y)} \frac{\partial f}{\partial y}(x,y)\,dx \;+\; f\big(\beta(y),y\big)\,\beta'(y) \;-\; f\big(\alpha(y),y\big)\,\alpha'(y).$$

Die drei Beiträge haben eine klare Bedeutung:

- **Integral-Term** $\int \frac{\partial f}{\partial y}\,dx$: Der Integrand selbst ändert sich mit $y$ (das ist das
  Ableiten unter dem Integral von oben).
- **oberer Randterm** $f(\beta,y)\,\beta'$: Die obere Grenze wandert mit Geschwindigkeit $\beta'$ und „schiebt"
  dabei neue Fläche vom Wert $f(\beta,y)$ hinzu.
- **unterer Randterm** $-f(\alpha,y)\,\alpha'$: Die untere Grenze wandert und gibt Fläche vom Wert $f(\alpha,y)$ ab
  (daher das Minus).

:::grafik
Die Fläche unter $f(\cdot,y)$ zwischen den beweglichen Grenzen $\alpha(y)$ und $\beta(y)$. Drei farbige Beiträge
zur Änderung: die ganze Fläche „atmet" ($\partial_y f$), am rechten Rand kommt ein dünner Streifen hinzu
($f(\beta,y)\beta'$), am linken Rand verschwindet einer ($-f(\alpha,y)\alpha'$). Beschriftung mit der Leibnizregel.
:::

**Eigenes Beispiel.** Für $F(y) = \int_0^{y} (x^2 + y)\,dx$ rechnet man direkt $F(y) = \frac{y^3}{3} + y^2$, also
$F'(y) = y^2 + 2y$. Die Leibnizregel gibt dasselbe: der Integral-Term $\int_0^y \frac{\partial}{\partial y}(x^2+y)\,dx
= \int_0^y 1\,dx = y$, der obere Randterm $f(y,y)\cdot 1 = (y^2+y)$, der untere Randterm $-f(0,y)\cdot 0 = 0$ —
zusammen $y + y^2 + y = y^2 + 2y$. ✓

:::kern
Ein __Parameterintegral__ $F(x)=\int_a^b f(x,t)\,dt$ lässt eine Variable ($t$) wegintegrieren und behält den
__Parameter__ $x$. Ist $f$ **stetig**, so ist $F$ stetig; sind zusätzlich die $\frac{\partial f}{\partial x_k}$
stetig, so ist $F$ stetig differenzierbar und man darf __unter dem Integral ableiten__:
$\frac{\partial F}{\partial x_k}=\int_a^b \frac{\partial f}{\partial x_k}\,dt$ (Beweis: MWT + gleichmäßige
Stetigkeit auf kompaktem $[a,b]$). Hängen auch die Grenzen vom Parameter ab, gilt die __Leibnizregel__
$F'(y)=\int_{\alpha(y)}^{\beta(y)} \frac{\partial f}{\partial y}\,dx + f(\beta,y)\beta' - f(\alpha,y)\alpha'$
(Integral-Term + zwei Randterme der wandernden Grenzen). **Vorsicht:** Das alles gilt für **endliche** Intervalle;
bei unendlichem Integrationsbereich kann die Vertauschung scheitern.
:::

Die ganze Argumentation ruhte auf der **Kompaktheit** des Intervalls $[a,b]$ (gleichmäßige Stetigkeit). Lässt man
das Integral bis $\infty$ laufen, bricht diese Grundlage weg — und tatsächlich können Stetigkeit und
Differenzierbarkeit verloren gehen. Wann sie trotzdem erhalten bleiben (Stichwort: __Majorantenkriterium__), ist
das Thema des nächsten Artikels über __uneigentliche Parameterintegrale__.

:::quiz
F: Was ist ein Parameterintegral, und welche Rolle spielen dabei Integrationsvariable und Parameter?
A: $F(x)=\int_a^b f(x,t)\,dt$: Über $t$ wird integriert (es „verschwindet"), $x$ bleibt als **Parameter** stehen und ist das Argument der neuen Funktion $F$. Aus einer Funktion zweier Argumente wird so eine Funktion nur noch von $x$.
F: Warum sind viele zentrale Funktionen überhaupt als Parameterintegral definiert?
A: Weil sie keine elementare geschlossene Formel haben, sondern erst durch ein Integral entstehen — z. B. die Gamma-Funktion, die Fourier- und Laplace-Transformierte oder Potentiale in der Feldtheorie. Ihre Eigenschaften (Stetigkeit, Ableitung) muss man dann aus dem Integral gewinnen.
F: Welche Bedingung sichert die Stetigkeit von $F$, und welche zusätzlich die Differenzierbarkeit?
A: Ist der Integrand $f$ stetig, so ist $F$ stetig. Sind zusätzlich die partiellen Ableitungen $\partial f/\partial x_k$ stetig, ist $F$ sogar stetig differenzierbar und man darf unter dem Integral ableiten.
F: Warum darf man die Ableitung ins Integral ziehen — wozu dient die Kompaktheit von $[a,b]$ im Beweis?
A: Man schreibt den Differenzenquotienten mit dem Mittelwertsatz als $\partial f/\partial x_k$ an einer Zwischenstelle. Auf dem **kompakten** Bereich $[0,h_0]\times[a,b]$ ist diese Ableitung gleichmäßig stetig — dadurch darf man beim Grenzübergang $h\to0$ den Limes ins Integral ziehen. Genau diese Gleichmäßigkeit liefert die Kompaktheit.
F: Warum kann dieselbe Vertauschung bei einem unendlichen Integrationsbereich scheitern?
A: Dann ist der Bereich nicht kompakt, die gleichmäßige Stetigkeit fehlt, und der Grenzübergang „Limes ins Integral" ist nicht mehr automatisch erlaubt. Es braucht eine Zusatzbedingung (Majorante), sonst können Stetigkeit/Differenzierbarkeit verloren gehen.
F: Wie knackt man mit „Ableiten unter dem Integral" ein schwieriges Integral — am Beispiel $\int_0^1 x^s\ln x\,dx$?
A: Man kennt $F(s)=\int_0^1 x^s\,dx=\frac{1}{s+1}$. Einmal direkt abgeleitet ist $F'(s)=-\frac{1}{(s+1)^2}$; andererseits liefert Ableiten unter dem Integral $F'(s)=\int_0^1 x^s\ln x\,dx$. Gleichsetzen gibt sofort $\int_0^1 x^s\ln x\,dx=-\frac{1}{(s+1)^2}$.
F: Was bedeuten die drei Terme der Leibnizregel anschaulich?
A: Der Integral-Term $\int\partial_y f\,dx$ erfasst, dass sich der **Integrand** mit $y$ ändert („die Fläche atmet"). Der obere Randterm $f(\beta,y)\beta'$ ist der Flächenstreifen, den die wandernde obere Grenze **hinzuschiebt**; der untere $-f(\alpha,y)\alpha'$ der Streifen, den die untere Grenze **abgibt**.
F: Warum trägt der untere Randterm ein Minuszeichen?
A: Wandert die untere Grenze $\alpha$ nach rechts, wird am linken Rand Fläche **entfernt** — das verkleinert $F$. Die Orientierung des Integrals (untere Grenze) kehrt das Vorzeichen gegenüber dem oberen Randterm um.
F: Was wird aus der Leibnizregel, wenn die Grenzen konstant sind?
A: Dann ist $\alpha'=\beta'=0$, beide Randterme fallen weg, und es bleibt das reine Ableiten unter dem Integral $F'(y)=\int_a^b\partial_y f\,dx$. Die Leibnizregel ist also die Verallgemeinerung für mitlaufende Grenzen.
F: Warum ist es korrekt, dass $F$ nur noch vom Parameter abhängt, obwohl $f$ von zwei Variablen abhängt?
A: Das bestimmte Integral über $t$ liefert für **jeden** festen Parameterwert $x$ eine einzige Zahl (die Fläche); die Abhängigkeit von $t$ ist „weg-integriert". Damit ist $F(x)$ eine wohldefinierte Funktion allein von $x$.
:::
