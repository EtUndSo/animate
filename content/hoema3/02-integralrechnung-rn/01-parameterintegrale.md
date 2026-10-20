---
title: Parameterintegrale und Ableiten unter dem Integral
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020100
summary: Von Grund auf – wenn eine Funktion durch ein Integral mit Parameter gegeben ist, $F(x)=\int_a^b f(x,t)\,dt$. Wann ist $F$ stetig und differenzierbar, und darf man die Ableitung ins Integral ziehen ($\frac{\partial F}{\partial x_k}=\int_a^b\frac{\partial f}{\partial x_k}\,dt$)? Mit der Leibnizregel für vom Parameter abhängende Grenzen.
tags: Parameterintegral, Ableiten unter dem Integral, Vertauschbarkeit, Leibnizregel, variable Grenzen, stetig differenzierbar
---

## Anschaulich

Viele wichtige Funktionen sind gar nicht durch eine Formel gegeben, sondern durch ein **Integral mit einem
Parameter** — die Gamma-Funktion, die Fourier- und Laplace-Transformierte, Potentiale in der Feldtheorie.

Stell dir eine Kurvenschar $t\mapsto f(x,t)$ über dem Intervall $[a,b]$ vor, bei der ein Schieberegler den
Parameter $x$ verstellt. Mit $x$ verformt sich die Kurve, und die **Fläche darunter** ändert sich mit. Diese
Fläche, als Funktion von $x$ aufgetragen, ist das Parameterintegral $F(x)$.

Die zentrale Frage lautet: Darf man die Ableitung $\frac{d}{dx}$ einfach **in** das Integral hineinziehen?

Die Antwort ist unter milden Bedingungen „ja" — und diese Vertauschung von Ableitung und Integral ist eines der
meistgenutzten Werkzeuge der angewandten Mathematik.

:::grafik
Szene: hoema3/integralrechnung-rn/01-parameterintegral-slider · Vorlage: kurvenschar-flaeche-2d
Eine Kurvenschar $f(x,t)$ über $[a,b]$ mit einem Schieberegler für den Parameter $x$; die Kurve verformt sich, die
Fläche darunter (das Integral) ändert sich. Daneben diese Fläche als Funktion $F(x)=\int_a^b f(x,t)\,dt$
aufgetragen. Eine kleine Animation „$\frac{\partial}{\partial x}$ wandert durch das Integralzeichen". (Blau =
Integrand, orange = Fläche/$F$, grau = Achsen.)
:::

## Das Parameterintegral

Ist $f(x,t)$ eine Funktion zweier Argumente, so kann man über **eine** Variable integrieren und die andere als
__Parameter__ stehen lassen. Das Ergebnis ist wieder eine Funktion — nur noch des Parameters:

:::formel Definition
$$F(x) := \int_a^b f(x,t)\,dt.$$
:::

Hier ist $t$ die **Integrationsvariable** (sie „verschwindet" durch das Integrieren), und $x$ ist der **Parameter**,
der als Argument von $F$ übrig bleibt.

Für jeden festen Wert $x$ liefert das bestimmte Integral eine einzige Zahl (die Fläche); deshalb ist $F$ eine
wohldefinierte Funktion allein von $x$. Allgemein darf der Parameter sogar ein Vektor $x\in U\subseteq\mathbb{R}^n$
sein.

Die erste Frage: Überträgt sich die Glätte des Integranden $f$ auf $F$?

## Stetigkeit und Ableiten unter dem Integral

Die Antwort ist beruhigend. Für eine offene Menge $U\subseteq\mathbb{R}^n$ und einen **stetigen** Integranden
$f:U\times[a,b]\to\mathbb{R}$ ist $F$ stetig. Sind zusätzlich alle partiellen Ableitungen
$\partial f/\partial x_k$ stetig, so ist $F$ sogar stetig differenzierbar, und man darf die Ableitung in das
Integral ziehen:

:::formel Satz
$$\frac{\partial F}{\partial x_k}(x) = \int_a^b \frac{\partial f}{\partial x_k}(x,t)\,dt.$$
:::

Links steht die Ableitung der durch das Integral definierten Funktion $F$, rechts das Integral über die
abgeleitete Integrandenfunktion — die Reihenfolge „ableiten" und „integrieren" ist also vertauschbar.

:::herleitung
Man bildet den Differenzenquotienten in Richtung $x_k$ und wendet im Integranden den **Mittelwertsatz** an:

$$\frac{f(x+h\hat e_k,t)-f(x,t)}{h} = \frac{\partial f}{\partial x_k}(x+\xi_h\hat e_k,\,t), \qquad \xi_h\in[0,h].$$

Weil $\frac{\partial f}{\partial x_k}$ auf dem **kompakten** Bereich $[0,h_0]\times[a,b]$ gleichmäßig stetig ist,
darf man beim Grenzübergang $h\to0$ den Limes ins Integral ziehen; übrig bleibt
$\int_a^b\frac{\partial f}{\partial x_k}(x,t)\,dt$.

Die gleichmäßige Stetigkeit — eine Folge der Kompaktheit von $[a,b]$ — ist der entscheidende Punkt. Bei
unendlichem Integrationsbereich fehlt sie, und genau dann kann die Vertauschung scheitern (nächster Artikel).
:::

**Eigenes Beispiel.** Für $F(s)=\int_0^1 x^s\,dx=\dfrac{1}{s+1}$ (Parameter $s>-1$) gibt Ableiten unter dem
Integral $F'(s)=\int_0^1 x^s\ln x\,dx$. Andererseits ist $F'(s)=-\dfrac{1}{(s+1)^2}$. Gleichsetzen liefert nebenbei
das nichttriviale Integral

$$\int_0^1 x^s\ln x\,dx = -\frac{1}{(s+1)^2}.$$

Das ist der typische Nutzen der Methode: schwierige Integrale über die Ableitung nach einem Parameter knacken.

## Die Leibnizregel: wenn auch die Grenzen mitlaufen

Oft hängen nicht nur der Integrand, sondern auch die **Integrationsgrenzen** vom Parameter ab. Ist $f$ stetig
differenzierbar und sind $\alpha,\beta$ stetig differenzierbare Grenzfunktionen, so gilt für
$F(y)=\int_{\alpha(y)}^{\beta(y)} f(x,y)\,dx$ die __Leibnizregel__:

:::formel Satz
$$F'(y) = \int_{\alpha(y)}^{\beta(y)} \frac{\partial f}{\partial y}(x,y)\,dx \;+\; f\big(\beta(y),y\big)\,\beta'(y) \;-\; f\big(\alpha(y),y\big)\,\alpha'(y).$$
:::

Die drei Beiträge haben eine klare Bedeutung:

- **Integral-Term** $\int\frac{\partial f}{\partial y}\,dx$: Der Integrand selbst ändert sich mit $y$ — das ist das
  Ableiten unter dem Integral von oben („die Fläche atmet").
- **oberer Randterm** $f(\beta,y)\,\beta'$: Die obere Grenze wandert mit Geschwindigkeit $\beta'$ und schiebt neue
  Fläche vom Wert $f(\beta,y)$ hinzu.
- **unterer Randterm** $-f(\alpha,y)\,\alpha'$: Die untere Grenze wandert und gibt Fläche vom Wert $f(\alpha,y)$
  ab — daher das Minuszeichen.

Sind die Grenzen konstant, ist $\alpha'=\beta'=0$, beide Randterme fallen weg, und es bleibt das reine Ableiten
unter dem Integral.

:::grafik
Szene: hoema3/integralrechnung-rn/01-leibniz-randterme · Vorlage: flaeche-bewegliche-grenzen-2d
Die Fläche unter $f(\cdot,y)$ zwischen den beweglichen Grenzen $\alpha(y)$ und $\beta(y)$. Drei farbige Beiträge:
die ganze Fläche „atmet" ($\partial_y f$), am rechten Rand kommt ein dünner Streifen hinzu ($f(\beta,y)\beta'$),
am linken verschwindet einer ($-f(\alpha,y)\alpha'$). (Orange = Integrand-Änderung, rot = rechter Streifen,
grau = linker Streifen.)
:::

**Eigenes Beispiel.** Für $F(y)=\int_0^{y}(x^2+y)\,dx$ ist direkt $F(y)=\tfrac{y^3}{3}+y^2$, also $F'(y)=y^2+2y$.
Die Leibnizregel gibt dasselbe: Integral-Term $\int_0^y 1\,dx=y$, oberer Randterm $f(y,y)\cdot1=y^2+y$, unterer
Randterm $-f(0,y)\cdot0=0$ — zusammen $y+(y^2+y)=y^2+2y$. ✓

## Bedeutung und Ausblick

Das Ableiten unter dem Integral macht aus einer nur implizit (durch ein Integral) gegebenen Funktion ein
greifbares Objekt, dessen Ableitung man kennt. Es ist das Standardwerkzeug für Transformationen (Fourier,
Laplace) und für Potentiale.

Die ganze Argumentation ruhte auf der **Kompaktheit** des Intervalls $[a,b]$. Lässt man das Integral bis $\infty$
laufen, bricht diese Grundlage weg — und tatsächlich können Stetigkeit und Differenzierbarkeit verloren gehen.
Wann sie trotzdem erhalten bleiben (Stichwort __Majorantenkriterium__), ist das Thema des nächsten Artikels über
__uneigentliche Parameterintegrale__.

:::kern
- Ein __Parameterintegral__ $F(x)=\int_a^b f(x,t)\,dt$ integriert eine Variable ($t$) weg und behält den __Parameter__ $x$; für jedes feste $x$ ist es eine Zahl, also $F$ eine Funktion von $x$.
- Ist $f$ **stetig**, so ist $F$ stetig; sind zusätzlich die $\partial f/\partial x_k$ stetig, ist $F$ stetig differenzierbar und man darf __unter dem Integral ableiten__: $\frac{\partial F}{\partial x_k}=\int_a^b\frac{\partial f}{\partial x_k}\,dt$.
- Beweisidee: Mittelwertsatz im Integranden + gleichmäßige Stetigkeit auf dem **kompakten** $[a,b]$.
- Hängen auch die Grenzen vom Parameter ab, gilt die __Leibnizregel__ $F'(y)=\int_{\alpha}^{\beta}\partial_y f\,dx+f(\beta,y)\beta'-f(\alpha,y)\alpha'$ (Integral-Term + zwei Randterme der wandernden Grenzen).
- **Vorsicht:** Alles gilt für **endliche** Intervalle; bei unendlichem Bereich kann die Vertauschung scheitern (Majorante nötig).
:::

:::quiz
F: Was ist ein Parameterintegral, und welche Rolle spielen Integrationsvariable und Parameter?
A: $F(x)=\int_a^b f(x,t)\,dt$: Über $t$ wird integriert (es „verschwindet"), $x$ bleibt als **Parameter** stehen und ist das Argument der neuen Funktion $F$. Aus einer Funktion zweier Argumente wird eine Funktion nur noch von $x$.
F: Warum sind viele zentrale Funktionen überhaupt als Parameterintegral definiert?
A: Weil sie keine elementare geschlossene Formel haben, sondern erst durch ein Integral entstehen — z. B. die Gamma-Funktion, die Fourier- und Laplace-Transformierte oder Potentiale in der Feldtheorie. Ihre Eigenschaften gewinnt man dann aus dem Integral.
F: Welche Bedingung sichert die Stetigkeit von $F$, und welche zusätzlich die Differenzierbarkeit?
A: Ist der Integrand $f$ stetig, so ist $F$ stetig. Sind zusätzlich die partiellen Ableitungen $\partial f/\partial x_k$ stetig, ist $F$ stetig differenzierbar und man darf unter dem Integral ableiten.
F: Warum darf man die Ableitung ins Integral ziehen — wozu dient die Kompaktheit von $[a,b]$ im Beweis?
A: Man schreibt den Differenzenquotienten mit dem Mittelwertsatz als $\partial f/\partial x_k$ an einer Zwischenstelle. Auf dem **kompakten** Bereich $[0,h_0]\times[a,b]$ ist diese Ableitung gleichmäßig stetig — dadurch darf man beim Grenzübergang $h\to0$ den Limes ins Integral ziehen.
F: Warum kann dieselbe Vertauschung bei einem unendlichen Integrationsbereich scheitern?
A: Dann ist der Bereich nicht kompakt, die gleichmäßige Stetigkeit fehlt, und der Grenzübergang „Limes ins Integral" ist nicht mehr automatisch erlaubt. Es braucht eine Zusatzbedingung (Majorante), sonst können Stetigkeit/Differenzierbarkeit verloren gehen.
F: Wie knackt man mit „Ableiten unter dem Integral" das Integral $\int_0^1 x^s\ln x\,dx$?
A: Man kennt $F(s)=\int_0^1 x^s\,dx=\frac{1}{s+1}$. Direkt abgeleitet ist $F'(s)=-\frac{1}{(s+1)^2}$; andererseits liefert Ableiten unter dem Integral $F'(s)=\int_0^1 x^s\ln x\,dx$. Gleichsetzen gibt $\int_0^1 x^s\ln x\,dx=-\frac{1}{(s+1)^2}$.
F: Was bedeuten die drei Terme der Leibnizregel anschaulich?
A: Der Integral-Term $\int\partial_y f\,dx$ erfasst, dass sich der **Integrand** mit $y$ ändert („die Fläche atmet"). Der obere Randterm $f(\beta,y)\beta'$ ist der Flächenstreifen, den die wandernde obere Grenze **hinzuschiebt**; der untere $-f(\alpha,y)\alpha'$ der Streifen, den die untere Grenze **abgibt**.
F: Warum trägt der untere Randterm ein Minuszeichen?
A: Wandert die untere Grenze $\alpha$ nach rechts, wird am linken Rand Fläche **entfernt** — das verkleinert $F$. Die Orientierung des Integrals (untere Grenze) kehrt das Vorzeichen gegenüber dem oberen Randterm um.
F: Was wird aus der Leibnizregel, wenn die Grenzen konstant sind?
A: Dann ist $\alpha'=\beta'=0$, beide Randterme fallen weg, und es bleibt das reine Ableiten unter dem Integral $F'(y)=\int_a^b\partial_y f\,dx$. Die Leibnizregel ist also die Verallgemeinerung für mitlaufende Grenzen.
F: Warum ist es korrekt, dass $F$ nur noch vom Parameter abhängt, obwohl $f$ von zwei Variablen abhängt?
A: Das bestimmte Integral über $t$ liefert für **jeden** festen Parameterwert $x$ eine einzige Zahl (die Fläche); die Abhängigkeit von $t$ ist weg-integriert. Damit ist $F(x)$ eine wohldefinierte Funktion allein von $x$.
:::
