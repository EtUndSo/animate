---
title: Parameterintegrale und Ableiten unter dem Integral
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020100
summary: Von Grund auf – eine Funktion, die durch ein Integral mit Parameter gegeben ist, $g(\vec x)=\int_a^b f(\vec x,t)\,dt$. Leitbild ist eine Kurve über einem festen Intervall, die ein Schieberegler verformt; das Integral ist die Fläche darunter. Wann ändert sich die Fläche ohne Sprünge, wann darf man die Ableitung ins Integral ziehen, $\partial g/\partial x_k=\int_a^b\partial f/\partial x_k\,dt$ – und was passiert, wenn auch die Grenzen mitlaufen (Leibnizregel)? Mit Beweisen, einem Gegenbeispiel und einer Beispiel-Seite.
tags: Parameterintegral, Ableiten unter dem Integral, Vertauschbarkeit, Leibnizregel, variable Grenzen, stetig differenzierbar
---

## Anschaulich

Viele wichtige Funktionen sind gar nicht durch eine Formel gegeben, sondern durch ein **Integral mit einem
Parameter** — die Gamma-Funktion, die Fourier- und Laplace-Transformierte, Potentiale in der Feldtheorie.

**Das Leitbild dieses Artikels:** Über einem festen Intervall $[a,b]$ liegt eine Kurve, und ein **Schieberegler**
verformt sie. Steht der Regler auf $x$, hat die Kurve an der Stelle $t$ die Höhe $f(x,t)$. Die **Fläche** unter der Kurve
hängt dann vom Regler ab — sie ist eine Funktion $g(x)$, das Parameterintegral.

Zwei Fragen stellen sich sofort. Ändert sich die Fläche **ohne Sprünge**, wenn man den Regler ohne Sprünge bewegt? Und
**wie schnell** ändert sie sich? Die zweite Antwort ist verblüffend einfach: Jede Stelle $t$ trägt mit der Geschwindigkeit
bei, mit der ihre Höhe wächst. Man darf die Ableitung also ins Integral hineinziehen — unter milden Bedingungen, die
dieser Artikel genau herausarbeitet.

Hängen auch die **Grenzen** vom Regler ab, wandert zusätzlich das Fenster, über dem man die Fläche misst. Dann kommen
an den Rändern Streifen hinzu oder fallen weg — das ist die Leibnizregel.

:::grafik
Szene: hoema3/integralrechnung-rn/01-parameterintegral-slider · Vorlage: kurvenschar-flaeche-2d
Eine Kurve $t\mapsto f(x,t)$ über $[a,b]$ mit einem Schieberegler für den Parameter $x$; die Kurve verformt sich, die
Fläche darunter ändert sich. Daneben diese Fläche als Funktion $g(x)=\int_a^b f(x,t)\,dt$ aufgetragen. An einzelnen
Stellen $t$ zeigen kleine Pfeile, wie schnell die Höhe wächst; ihre Summe ist die Änderungsrate der Fläche. Kernaussage:
Die Fläche ändert sich mit der Summe der Höhenänderungen. (Blau = Kurve, orange = Fläche bzw. $g$, rot = Änderungsraten,
grau = Achsen.)
:::

## Was ist ein Parameterintegral?

**Die Akteure:** eine offene Menge $U\subseteq\mathbb{R}^n$ — die möglichen Stellungen des Reglers, der Parameter darf
also ein Vektor $\vec x$ sein —, ein festes Intervall $[a,b]\subseteq\mathbb{R}$ und eine stetige Funktion

$$f:U\times[a,b]\to\mathbb{R}, \qquad (\vec x,t)\mapsto f(\vec x,t).$$

Für jede feste Reglerstellung $\vec x$ ist $t\mapsto f(\vec x,t)$ eine stetige Kurve über $[a,b]$, und die Fläche
darunter ist eine Zahl. So entsteht eine neue Funktion des Parameters allein, das __Parameterintegral__:

:::formel Definition
$$g(\vec x) := \int_a^b f(\vec x,t)\,dt, \qquad \vec x\in U.$$
:::

**So liest man das:** $t$ ist die **Integrationsvariable** — sie wird weg-integriert und taucht im Ergebnis nicht mehr
auf. $\vec x$ ist der **Parameter**, er bleibt als Argument von $g$ stehen. Die Eingabe von $g$ ist ein Punkt
$\vec x\in U$, die Ausgabe eine Zahl. Das Ergebnis ist eine skalare Funktion, darum heißt sie klein, $g$ (im Skript $F$).

::::beispiel Ein Parameterintegral ausrechnen
Mit dem Parameter $x\in\mathbb{R}$ und

$$f(x,t) = (x+t)^2, \qquad t\in[0,1],$$

ist die Fläche unter der verschobenen Parabel

$$g(x) = \int_0^1 (x^2+2xt+t^2)\,dt = x^2 + x + \tfrac13.$$

**Im Bild:** Der Regler schiebt die Parabel $t^2$ nach links. Steht er auf $0$, ist die Fläche $\tfrac13$; schiebt man
ihn auf $1$, liegt über $[0,1]$ der steilere Teil der Parabel, und die Fläche ist $\tfrac73$.
::::

## Stetigkeit: keine Sprünge in der Fläche

Die erste Antwort ist beruhigend: **Ist $f$ stetig, so ist auch $g$ stetig auf $U$.** Bewegt man den Regler ein wenig,
ändert sich die Fläche nur wenig.

**Im Bild:** Entscheidend ist, dass sich die **ganze** Kurve nur wenig bewegt, wenn der Regler nur wenig bewegt wird —
nirgends darf ein Stück davonschießen. Dann ändert sich die Fläche höchstens um die Breite $b-a$ mal die größte
Höhenänderung.

:::herleitung
Sei $\vec x_0\in U$. Weil $U$ offen ist, liegt eine abgeschlossene Kugel um $\vec x_0$ ganz in $U$:

$$K = \big\{\,\vec x\in\mathbb{R}^n \;:\; \lvert\vec x-\vec x_0\rvert\le r\,\big\} \subseteq U \qquad\text{für ein } r>0.$$

Die Menge $K\times[a,b]\subseteq\mathbb{R}^{n+1}$ ist __kompakt__, also beschränkt und abgeschlossen. Eine stetige
Funktion auf einer kompakten Menge ist dort __gleichmäßig stetig__ (Satz von Heine, HM2): Zu jedem $\varepsilon>0$ gibt es
ein $\delta>0$, das für **alle** Stellen $t$ gleichzeitig funktioniert. Für $\vec x\in K$ mit
$\lvert\vec x-\vec x_0\rvert<\delta$ gilt also

$$\lvert f(\vec x,t)-f(\vec x_0,t)\rvert < \varepsilon \qquad\text{für alle } t\in[a,b].$$

Damit ist der Unterschied der Flächen klein:

$$\lvert g(\vec x)-g(\vec x_0)\rvert \le \int_a^b \lvert f(\vec x,t)-f(\vec x_0,t)\rvert\,dt \le (b-a)\,\varepsilon.$$

**Im Bild:** Das $\delta$ der gleichmäßigen Stetigkeit sorgt dafür, dass die ganze Kurve innerhalb eines schmalen
Bandes der Höhe $\varepsilon$ bleibt — und die Fläche damit innerhalb von $(b-a)\,\varepsilon$.
:::

::::beispiel Die Formel hat ein Loch, das Integral nicht
Mit dem Parameter $x\in\mathbb{R}$ betrachten wir

$$g(x) = \int_0^1 e^{xt}\,dt.$$

Für $x\neq0$ hat das Integral die geschlossene Form

$$g(x) = \Big[\frac{e^{xt}}{x}\Big]_{t=0}^{t=1} = \frac{e^x-1}{x},$$

die bei $x=0$ nicht definiert ist. Das Integral selbst ist es sehr wohl:

$$g(0) = \int_0^1 1\,dt = 1.$$

Weil der Integrand stetig ist, ist $g$ auch bei $0$ stetig. Das bestätigt die Formel im Grenzwert:

$$\lim_{x\to0}\frac{e^x-1}{x} = 1.$$

**Im Bild:** Steht der Regler auf $0$, ist die Kurve die waagerechte Gerade der Höhe $1$. Ein wenig daneben ist sie ein
ganz flacher Exponentialbogen, und die Fläche darunter liegt dicht bei $1$ — kein Sprung.

:::grafik
Szene: hoema3/integralrechnung-rn/01-e-hoch-xt · Vorlage: kurvenschar-flaeche-2d
Die Kurven $t\mapsto e^{xt}$ über $[0,1]$ für Reglerstellungen um $x=0$; die Fläche als Funktion von $x$ daneben. An der
Stelle $x=0$ zeigt die geschlossene Formel $\frac{e^x-1}{x}$ ein Loch (Kreis), das Integral füllt es mit dem Wert $1$.
Kernaussage: Ein Parameterintegral mit stetigem Integranden hat keine Sprünge und keine Löcher. (Blau = Kurven, orange =
Fläche, rot = Wert bei $0$.)
:::
::::

## Ableiten unter dem Integral

Wie schnell ändert sich die Fläche? Sind auch alle partiellen Ableitungen nach den Parametern stetig,

$$\frac{\partial f}{\partial x_k}:U\times[a,b]\to\mathbb{R} \ \text{ stetig} \qquad (k=1,\ldots,n),$$

so ist $g$ stetig differenzierbar auf $U$, und man darf die Ableitung ins Integral ziehen:

:::formel Satz
$$\frac{\partial g}{\partial x_k}(\vec x) = \int_a^b \frac{\partial f}{\partial x_k}(\vec x,t)\,dt.$$
:::

**So liest man das:** Links steht die Ableitung der durch das Integral definierten Funktion, rechts das Integral über die
abgeleitete Kurve. „Ableiten" und „integrieren" dürfen also die Reihenfolge tauschen.

**Im Bild:** Zerlegt man die Fläche in schmale senkrechte Streifen, so wächst jeder Streifen an der Stelle $t$ mit der
Geschwindigkeit $\partial f/\partial x_k(\vec x,t)$ — so schnell steigt dort die Kurve, wenn man den Regler verstellt.
Die Fläche wächst mit der Summe all dieser Geschwindigkeiten, also mit ihrem Integral.

:::herleitung
Sei $\vec x\in U$ und $h_0>0$ so klein, dass die Punkte $\vec x+h\,\vec e_k$ für $0<\lvert h\rvert\le h_0$ in $U$ liegen. Der
Differenzenquotient von $g$ ist das Integral der Differenzenquotienten der Kurve:

$$\frac{g(\vec x+h\,\vec e_k)-g(\vec x)}{h} = \int_a^b \frac{f(\vec x+h\,\vec e_k,t)-f(\vec x,t)}{h}\,dt.$$

Für jedes feste $t$ liefert der Mittelwertsatz aus HM1 eine Zwischenstelle $\xi$ zwischen $0$ und $h$ — sie darf von $t$
abhängen —, an der der Quotient gleich der Ableitung ist:

$$\frac{f(\vec x+h\,\vec e_k,t)-f(\vec x,t)}{h} = \frac{\partial f}{\partial x_k}(\vec x+\xi\,\vec e_k,\,t).$$

Die Ableitung $\partial f/\partial x_k$ ist auf der kompakten Menge der Punkte $(\vec x+s\,\vec e_k,t)$ mit
$\lvert s\rvert\le h_0$ und $t\in[a,b]$ gleichmäßig stetig. Zu $\varepsilon>0$ gibt es also ein $\delta>0$, sodass für
$\lvert h\rvert<\delta$ — und damit $\lvert\xi\rvert<\delta$ — an **allen** Stellen $t$ gilt:

$$\Big\lvert\frac{\partial f}{\partial x_k}(\vec x+\xi\,\vec e_k,t)-\frac{\partial f}{\partial x_k}(\vec x,t)\Big\rvert < \varepsilon.$$

Integriert über $[a,b]$:

$$\Big\lvert\frac{g(\vec x+h\,\vec e_k)-g(\vec x)}{h} - \int_a^b\frac{\partial f}{\partial x_k}(\vec x,t)\,dt\Big\rvert \le (b-a)\,\varepsilon.$$

Also existiert die partielle Ableitung von $g$ und ist das behauptete Integral. Sie ist stetig, denn sie ist selbst ein
Parameterintegral mit stetigem Integranden — dafür sorgt der Stetigkeitssatz. Stetige partielle Ableitungen machen $g$
nach dem ersten Artikel total differenzierbar.

**Im Bild:** Ohne die gleichmäßige Stetigkeit könnte ein winziges Stück der Kurve beim Verstellen des Reglers
davonschießen und die Fläche verändern, obwohl sich an jeder einzelnen Stelle kaum etwas tut.
:::

::::beispiel Die Ableitung im Loch der Formel
Für das Parameterintegral mit dem Integranden $e^{xt}$ gibt Ableiten unter dem Integral

$$g'(x) = \int_0^1 \frac{\partial}{\partial x}\,e^{xt}\,dt = \int_0^1 t\,e^{xt}\,dt, \qquad g'(0) = \int_0^1 t\,dt = \frac12.$$

Mit der geschlossenen Form $\frac{e^x-1}{x}$ wäre das mühsam; über die Reihe der Exponentialfunktion bestätigt es sich:

$$\frac{e^x-1}{x} = 1+\frac x2+\frac{x^2}{6}+\ldots, \qquad g'(0) = \frac12.$$

**Im Bild:** Bei $x=0$ ist die Kurve die Gerade der Höhe $1$. Dreht man den Regler hoch, steigt sie an der Stelle $t$ mit
der Rate $t$ — rechts schnell, links gar nicht. Im Mittel über $[0,1]$ ist das $\tfrac12$.
::::

::::beispiel Ein schwieriges Integral über die Ableitung knacken
Für den Parameter $s>0$ ist

$$g(s) = \int_0^1 t^s\,dt = \frac{1}{s+1}.$$

Der Integrand $t^s$ und seine Ableitung nach $s$, nämlich $t^s\ln t$, sind auf $(0,\infty)\times[0,1]$ stetig, wenn man
sie bei $t=0$ durch $0$ ergänzt. Ableiten unter dem Integral und direktes Ableiten müssen also dasselbe geben:

$$\int_0^1 t^s\ln t\,dt = g'(s) = -\frac{1}{(s+1)^2}.$$

Für $s=1$ zum Beispiel:

$$\int_0^1 t\ln t\,dt = -\frac14.$$

Die Formel gilt sogar für alle $s>-1$. Dort wird der Integrand aber bei $t=0$ unbeschränkt, das Integral ist
uneigentlich, und die Begründung liefert erst der nächste Artikel.

**Im Bild:** Statt das Integral mit dem Logarithmus direkt anzugehen, verstellt man den Regler an einem einfachen
Integral und liest ab, wie schnell sich dessen Fläche ändert. Physiker nennen das den Feynman-Trick.
::::

**Der Parameter in einem abgeschlossenen Intervall.** Dasselbe gilt für einen Parameter $y$ aus einem abgeschlossenen
Intervall $[c,d]$ statt aus einer offenen Menge, wenn man an den Rändern $c$ und $d$ die einseitigen Ableitungen meint:
Ist $f$ auf $[c,d]\times[a,b]$ stetig, so ist das Parameterintegral stetig auf $[c,d]$; ist zusätzlich $\partial f/\partial y$
dort stetig, so ist es stetig differenzierbar.

:::herleitung
Beide Beweise benutzen nur Punkte, die vom betrachteten Parameterwert aus erreichbar sind, und eine kompakte Menge,
auf der die Funktionen gleichmäßig stetig sind. Am Rand $c$ nimmt man nur Schritte nach innen, also $h>0$; am Rand $d$ nur
$h<0$. Die Menge $[c,d]\times[a,b]$ ist selbst kompakt — alles Weitere geht wörtlich wie oben.
:::

**Wenn die Voraussetzung fehlt.** Die Stetigkeit des Integranden ist keine Formsache. Ohne sie kann die Fläche sich
ändern, obwohl an jeder einzelnen Stelle $t$ die Höhe mit der Rate null wächst — dann scheitert die Vertauschung.

::::beispiel Die Fläche in der Spitze
Für $x\in\mathbb{R}$ und $t\in(0,1]$ sei

$$f(x,t) = \frac{x^3}{t^2}\,e^{-x^2/t}, \qquad f(x,0) := 0.$$

Das Parameterintegral lässt sich ausrechnen — für $x\neq0$ mit einer Substitution, für $x$ gleich null direkt, weil der
Integrand dann verschwindet:

$$g(x) = \int_0^1 f(x,t)\,dt = x\,e^{-x^2}, \qquad g'(0) = 1.$$

An jeder festen Stelle $t$ ist die Höhe aber in $x=0$ gar nicht im Wachsen:

$$\frac{\partial f}{\partial x}(0,t) = \lim_{h\to0}\frac{h^2}{t^2}\,e^{-h^2/t} = 0, \qquad \int_0^1\frac{\partial f}{\partial x}(0,t)\,dt = 0 \;\neq\; 1.$$

:::herleitung
Man substituiert

$$u = \frac{x^2}{t}, \qquad t = \frac{x^2}{u}, \qquad dt = -\frac{x^2}{u^2}\,du.$$

Aus $t\to0$ wird dabei $u\to\infty$, und die obere Grenze $1$ geht in $x^2$ über. Der Integrand wird

$$\frac{x^3}{t^2}\,e^{-x^2/t}\,dt = \frac{u^2}{x}\,e^{-u}\cdot\Big(-\frac{x^2}{u^2}\Big)\,du = -x\,e^{-u}\,du.$$

Also

$$\int_0^1 f(x,t)\,dt = -x\int_{\infty}^{x^2}e^{-u}\,du = x\int_{x^2}^{\infty}e^{-u}\,du = x\,e^{-x^2}.$$
:::

**Warum der Satz nicht greift:** $f$ ist in der Ecke $(0,0)$ nicht einmal stetig. Längs der Kurve $t=x^2$ wächst der
Integrand über alle Grenzen:

$$f(x,x^2) = \frac{x^3}{x^4}\,e^{-1} = \frac{1}{e\,x}.$$

**Im Bild:** Bei kleinem Regler steckt die ganze Fläche in einer schmalen, hohen Spitze nahe $t\approx x^2$. Dreht man
den Regler gegen null, rutscht die Spitze in die Ecke, wird höher und schmaler — und ihre Fläche schrumpft wie $x$. An
jeder festen Stelle $t$ merkt man davon nichts, denn die Spitze ist dort längst vorbeigezogen.

:::grafik
Szene: hoema3/integralrechnung-rn/01-spitze-in-der-ecke · Vorlage: kurvenschar-flaeche-2d
Die Kurven $t\mapsto f(x,t)$ für kleine Reglerstellungen $x$: eine schmale Spitze nahe $t=x^2$, die mit kleinerem $x$
höher und schmaler wird und in die Ecke $t=0$ rutscht. Daneben die Fläche $g(x)=xe^{-x^2}$ mit der Tangentensteigung $1$
bei $0$ und, an einer festen Stelle $t$, die Höhe über $x$ — flach bei $x=0$. Kernaussage: Ohne Stetigkeit des Integranden
kann die Fläche sich ändern, ohne dass es an einer einzelnen Stelle sichtbar wird. (Blau = Kurven, orange = Fläche, rot =
Spitze, grau = Achsen.)
:::
::::

## Die Leibnizregel: wenn die Grenzen mitlaufen

Oft hängen nicht nur die Kurve, sondern auch die **Grenzen** vom Parameter ab. **Die Akteure:** ein Parameter
$y\in[c,d]$, zwei stetig differenzierbare Grenzfunktionen $\alpha,\beta:[c,d]\to\mathbb{R}$ mit $\alpha\le\beta$ und eine
Funktion $f$, die in einer Umgebung des Bereichs

$$D = \big\{\,(y,t)\in\mathbb{R}^2 \;:\; c\le y\le d,\ \ \alpha(y)\le t\le\beta(y)\,\big\}$$

stetig differenzierbar ist. Das Parameterintegral mit wandernden Grenzen ist

$$g(y) := \int_{\alpha(y)}^{\beta(y)} f(y,t)\,dt.$$

Im Skript heißen die Variablen umgekehrt, $f(x,y)\,dx$; hier steht wie oben der Parameter vorn und $t$ für die
Integrationsvariable. Es gilt die __Leibnizregel__:

:::formel Satz
$$g'(y) = \int_{\alpha(y)}^{\beta(y)} \frac{\partial f}{\partial y}(y,t)\,dt \;+\; f\big(y,\beta(y)\big)\,\beta'(y) \;-\; f\big(y,\alpha(y)\big)\,\alpha'(y).$$
:::

**Im Bild** hat jeder der drei Beiträge eine klare Bedeutung:

- **Integral-Term:** Die Kurve selbst verformt sich mit $y$ — das ist das Ableiten unter dem Integral von oben, die
  Fläche „atmet".
- **Oberer Randterm** $f(y,\beta)\,\beta'$: Die rechte Grenze wandert mit der Geschwindigkeit $\beta'$ und schiebt einen
  Streifen der Höhe $f(y,\beta)$ hinzu.
- **Unterer Randterm** $-f(y,\alpha)\,\alpha'$: Wandert die linke Grenze nach rechts, fällt dort ein Streifen der Höhe
  $f(y,\alpha)$ weg — daher das Minuszeichen.

:::herleitung
Man trennt die drei Rollen des Parameters. Für Grenzen $u,v$ und einen Parameter $y$ sei

$$H(u,v,y) := \int_u^v f(y,t)\,dt.$$

Ihre drei partiellen Ableitungen kennt man: nach der oberen Grenze aus dem Hauptsatz der Differential- und
Integralrechnung, nach der unteren ebenso mit umgekehrtem Vorzeichen, nach dem Parameter aus dem Satz über das Ableiten
unter dem Integral:

$$\frac{\partial H}{\partial v} = f(y,v), \qquad \frac{\partial H}{\partial u} = -f(y,u), \qquad \frac{\partial H}{\partial y} = \int_u^v\frac{\partial f}{\partial y}(y,t)\,dt.$$

Alle drei sind stetig, also ist $H$ stetig differenzierbar. Das gesuchte $g$ ist die Verkettung von $H$ mit
$y\mapsto(\alpha(y),\beta(y),y)$, und die Kettenregel des ersten Artikels gibt

$$g'(y) = \frac{\partial H}{\partial u}\,\alpha'(y) + \frac{\partial H}{\partial v}\,\beta'(y) + \frac{\partial H}{\partial y}\cdot1,$$

wobei man für $u$ die untere Grenze $\alpha(y)$ und für $v$ die obere $\beta(y)$ einsetzt — genau die drei Terme der
Leibnizregel.

**Im Bild:** Die Kettenregel zählt die drei Wege, auf denen der Regler die Fläche verändert: über die linke Grenze, über
die rechte Grenze und über die Kurve selbst.
:::

**Spezialfälle.** Sind die Grenzen konstant, fallen beide Randterme weg, und es bleibt das reine Ableiten unter dem
Integral. Hängt umgekehrt nur die obere Grenze vom Parameter ab und der Integrand nicht, steht da der Hauptsatz der
Differential- und Integralrechnung: Die Fläche unter einer festen Kurve wächst, wenn die rechte Grenze wandert, mit der
Höhe an dieser Grenze.

**Nur Stetigkeit.** Setzt man lediglich voraus, dass $f$, $\alpha$ und $\beta$ stetig sind, so ist $g$ immer noch
stetig. Für die stetige Differenzierbarkeit genügt es, zusätzlich die Existenz und Stetigkeit von
$\partial f/\partial y$, $\alpha'$ und $\beta'$ zu verlangen.

:::herleitung
Auf einer kompakten Umgebung des Bereichs ist $f$ beschränkt, etwa durch eine Zahl $M$, und gleichmäßig stetig. Dann
ist $H$ stetig, denn eine kleine Änderung der Grenzen ändert die Fläche höchstens um $M$ mal die Verschiebung, und eine
kleine Änderung des Parameters höchstens um die Breite mal die größte Höhenänderung:

$$\lvert H(u,v,y)-H(u_0,v_0,y_0)\rvert \le M\lvert u-u_0\rvert + M\lvert v-v_0\rvert + \int_{u_0}^{v_0}\lvert f(y,t)-f(y_0,t)\rvert\,dt.$$

Als Verkettung stetiger Abbildungen ist $g$ dann stetig. Die Differenzierbarkeit folgt wie in der Herleitung oben.
:::

::::beispiel Die Leibnizregel an zwei Beispielen
**(a) Nur die obere Grenze wandert.** Für

$$g(y) = \int_0^{y}(t^2+y)\,dt$$

ergibt die direkte Rechnung

$$g(y) = \frac{y^3}{3}+y^2, \qquad g'(y) = y^2+2y.$$

Die Leibnizregel gibt dasselbe: Der Integral-Term ist das Integral von $1$, der obere Randterm ist die Höhe $y^2+y$ mal
$1$, der untere fällt weg, weil die untere Grenze festsitzt:

$$\int_0^y 1\,dt + (y^2+y)\cdot1 - (0+y)\cdot0 = y+y^2+y = y^2+2y.$$

**(b) Beide Grenzen wandern.** Für

$$g(y) = \int_y^{2y} t\,dt = \frac{(2y)^2-y^2}{2} = \frac32\,y^2$$

ist $g'(y)=3y$. Der Integrand hängt nicht von $y$ ab, also bleiben nur die Randterme:

$$0 + 2y\cdot2 - y\cdot1 = 3y.$$

**Im Bild:** Bei (b) läuft die rechte Grenze doppelt so schnell wie die linke und schiebt dabei Streifen der Höhe $2y$
hinzu, während links Streifen der Höhe $y$ wegfallen.
::::

:::grafik
Szene: hoema3/integralrechnung-rn/01-leibniz-randterme · Vorlage: flaeche-bewegliche-grenzen-2d
Die Fläche unter $t\mapsto f(y,t)$ zwischen den beweglichen Grenzen $\alpha(y)$ und $\beta(y)$. Drei farbige Beiträge: die
ganze Fläche „atmet" ($\partial_y f$), am rechten Rand kommt ein dünner Streifen hinzu ($f(y,\beta)\beta'$), am linken
verschwindet einer ($-f(y,\alpha)\alpha'$). Kernaussage: Die Leibnizregel zählt drei Wege, auf denen sich die Fläche
ändert. (Orange = Änderung der Kurve, rot = rechter Streifen, grau = linker Streifen.)
:::

## Bedeutung und Ausblick

Das Ableiten unter dem Integral macht aus einer nur durch ein Integral gegebenen Funktion ein greifbares Objekt, dessen
Ableitung man kennt. Es ist das Standardwerkzeug für Transformationen (Fourier, Laplace), für Potentiale in der
Feldtheorie — und ein Trick, um schwierige Integrale über einen künstlich eingeführten Parameter auszurechnen.

Die ganze Argumentation ruhte auf der **Kompaktheit**: Das feste Intervall $[a,b]$ sorgte für gleichmäßige Stetigkeit.
Lässt man das Integral bis $\infty$ laufen oder wird der Integrand am Rand unbeschränkt, bricht diese Grundlage weg — und
tatsächlich können Stetigkeit und Differenzierbarkeit verloren gehen. Wann sie trotzdem erhalten bleiben (Stichwort
__Majorante__), ist das Thema des nächsten Artikels über __uneigentliche Parameterintegrale__.

:::kern
- Ein __Parameterintegral__ $g(\vec x)=\int_a^b f(\vec x,t)\,dt$ integriert $t$ weg und behält den __Parameter__ $\vec x$ — die Fläche unter einer Kurve, die ein Regler verformt.
- Ist $f$ auf $U\times[a,b]$ **stetig**, so ist $g$ stetig: Die ganze Kurve bewegt sich nur wenig, also auch die Fläche.
- Sind zusätzlich die $\partial f/\partial x_k$ stetig, so ist $g$ stetig differenzierbar, und man darf __unter dem Integral ableiten__: $\partial g/\partial x_k=\int_a^b\partial f/\partial x_k\,dt$.
- Beweisidee: Mittelwertsatz an jeder Stelle $t$ und gleichmäßige Stetigkeit auf einer **kompakten** Menge.
- Die Voraussetzung ist nötig: Steckt die Fläche in einer Spitze, die in eine Ecke wandert, scheitert die Vertauschung.
- __Leibnizregel__ für wandernde Grenzen: $g'=\int_\alpha^\beta\partial_y f\,dt+f(y,\beta)\beta'-f(y,\alpha)\alpha'$ — Kurve, rechter Rand, linker Rand.
- Herleitung über die Kettenregel mit $H(u,v,y)=\int_u^v f(y,t)\,dt$; Spezialfälle sind das reine Ableiten unter dem Integral und der Hauptsatz.
- **Vorsicht:** Alles gilt für endliche Intervalle und beschränkte Integranden; sonst braucht man eine Majorante.
:::

:::quiz
F: Was ist ein Parameterintegral, und welche Rolle spielen Integrationsvariable und Parameter?
A: $g(\vec x)=\int_a^b f(\vec x,t)\,dt$: Über $t$ wird integriert, es verschwindet; $\vec x$ bleibt als **Parameter** stehen und ist das Argument der neuen Funktion. Im Bild ist $g(\vec x)$ die Fläche unter der Kurve $t\mapsto f(\vec x,t)$, die der Regler $\vec x$ verformt — für jede Reglerstellung eine Zahl.
F: Warum ist $g$ stetig, wenn $f$ stetig ist — und wozu braucht man dabei die Kompaktheit?
A: Auf der kompakten Menge $K\times[a,b]$ ist $f$ gleichmäßig stetig: Ein einziges $\delta$ sorgt dafür, dass sich die Kurve an **allen** Stellen $t$ um weniger als $\varepsilon$ ändert. Dann ändert sich die Fläche höchstens um $(b-a)\varepsilon$. Im Bild: Die ganze Kurve bleibt in einem schmalen Band, kein Stück schießt davon.
F: Wie zeigt das Beispiel $g(x)=\int_0^1 e^{xt}\,dt$, dass ein Parameterintegral kein Loch haben kann?
A: Für $x\neq0$ ist $g(x)=\frac{e^x-1}{x}$, und diese Formel ist bei $0$ nicht definiert. Das Integral liefert aber $g(0)=\int_0^1 1\,dt=1$, und weil der Integrand stetig ist, ist $g$ dort stetig — passend zum Grenzwert $\frac{e^x-1}{x}\to1$.
F: Warum darf man unter dem Integral ableiten — was bedeutet das im Bild der Streifen?
A: Jeder schmale Streifen der Fläche wächst an seiner Stelle $t$ mit der Geschwindigkeit $\partial f/\partial x_k(\vec x,t)$; die Fläche wächst mit der Summe, also dem Integral dieser Geschwindigkeiten. Formal schreibt man den Differenzenquotienten mit dem Mittelwertsatz als Ableitung an Zwischenstellen und nutzt die gleichmäßige Stetigkeit der Ableitung, um den Grenzwert ins Integral zu ziehen.
F: Wie knackt man mit Ableiten unter dem Integral das Integral $\int_0^1 t^s\ln t\,dt$?
A: Man kennt $g(s)=\int_0^1 t^s\,dt=\frac{1}{s+1}$. Ableiten unter dem Integral gibt $g'(s)=\int_0^1 t^s\ln t\,dt$, direktes Ableiten $g'(s)=-\frac{1}{(s+1)^2}$. Gleichsetzen liefert das Integral, für $s=1$ etwa $-\frac14$. Für $s>0$ deckt der Satz das ab; für $-1<s\le0$ ist das Integral uneigentlich.
F: Warum scheitert die Vertauschung bei $f(x,t)=\frac{x^3}{t^2}e^{-x^2/t}$?
A: Das Parameterintegral ist $g(x)=xe^{-x^2}$ mit $g'(0)=1$, aber an jeder festen Stelle $t$ ist $\partial f/\partial x(0,t)=0$, das Integral der Ableitung also $0$. Der Satz greift nicht, weil $f$ in der Ecke $(0,0)$ nicht stetig ist: Die Fläche steckt in einer Spitze nahe $t\approx x^2$, die beim Verkleinern von $x$ in die Ecke rutscht.
F: Was bedeuten die drei Terme der Leibnizregel anschaulich?
A: Der Integral-Term $\int\partial_y f\,dt$ erfasst, dass sich die Kurve selbst mit $y$ verformt — die Fläche atmet. Der obere Randterm $f(y,\beta)\beta'$ ist der Streifen, den die wandernde rechte Grenze **hinzuschiebt**; der untere $-f(y,\alpha)\alpha'$ der Streifen, der an der linken Grenze **wegfällt**.
F: Wie leitet man die Leibnizregel aus der Kettenregel her?
A: Man setzt $H(u,v,y)=\int_u^v f(y,t)\,dt$ mit getrennten Rollen für die beiden Grenzen und den Parameter. Seine partiellen Ableitungen sind $-f(y,u)$, $f(y,v)$ und $\int_u^v\partial_yf\,dt$ (Hauptsatz und Ableiten unter dem Integral). Die Kettenregel für $g(y)=H(\alpha(y),\beta(y),y)$ setzt daraus die drei Terme zusammen.
F: Was gibt die Leibnizregel für $g(y)=\int_y^{2y}t\,dt$, und warum fehlt dort der Integral-Term?
A: Der Integrand $t$ hängt nicht von $y$ ab, also bleibt nur der Rand: $2y\cdot2-y\cdot1=3y$. Das passt zur direkten Rechnung $g(y)=\frac32y^2$. Im Bild läuft die rechte Grenze doppelt so schnell wie die linke und schiebt Streifen der Höhe $2y$ hinzu, links fallen Streifen der Höhe $y$ weg.
F: Welche Spezialfälle stecken in der Leibnizregel, und wo endet ihre Gültigkeit?
A: Bei konstanten Grenzen bleibt das reine Ableiten unter dem Integral; hängt nur die obere Grenze vom Parameter ab, steht der Hauptsatz da. Alles beruht auf endlichen Intervallen und stetigen Integranden: Bei unendlichen Bereichen oder unbeschränkten Integranden fehlt die Kompaktheit, und man braucht eine Majorante (nächster Artikel).
:::
