---
title: Stufe 9: Poisson-Gleichung
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Integralsätze im Raum
adresse: elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum
knoten: Kapitel 5: Integralsätze im Raum
order: 3151000
summary: In Kapitel 4 stand eine Lösungsformel für die Poisson-Gleichung ohne Begründung.
tags: Poisson-Gleichung, Faltung, Greensche Funktion
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
In [Kapitel 4](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen/koordinatentransformationen.html) stand eine Lösungsformel für die Poisson-Gleichung ohne Begründung. Mit Satz [8.3](der-satz-von-gau.html#satz-8-3) lässt sie sich jetzt verstehen: Die Punktquelle des Coulomb-Potentials erzeugt genau das $f$ auf der rechten Seite.
:::

**Die Idee.** Die __Poisson-Gleichung__ $-\Delta u=f$ im $\mathbb{R}^3$ fragt: Welches Potential gehört zur Quellverteilung $f$? Das Potential einer Punktquelle kennst du schon, $\phi(\boldsymbol{x})=1/(4\pi r)$. Eine Verteilung ist die Überlagerung vieler Punktquellen, also sollte das Potential die Summe aller Beiträge sein. Das ist die __Faltung__

<span class="anker" id="gl-9-1"></span>
$$u(\boldsymbol{x})=\int_{\mathbb{R}^3}\phi(\boldsymbol{x}-\boldsymbol{y})\,f(\boldsymbol{y})\;\mathrm{d}\boldsymbol{y},\qquad\phi(\boldsymbol{x})=\frac{1}{4\pi|\boldsymbol{x}|}. \tag{9.1}$$

Die Schwierigkeit: $\phi$ ist bei $0$ singulär, und abseits davon ist $\Delta\phi=0$. Wo kommt dann das $f$ her? Es entsteht genau an der Singularität, am Rand einer kleinen Kugel um den Aufpunkt.

:::satz Satz 9.1 (Lösung der Poisson-Gleichung)
<span class="anker" id="satz-9-1"></span>

Für stetig differenzierbares $f$ mit genügendem Abklingen, zum Beispiel mit kompaktem Träger, erfüllt $u$ aus [(9.1)](#gl-9-1) die Gleichung $-\Delta u=f$. Die Funktion $\phi$ heißt __Greensche Funktion__ des Laplace-Operators.
:::

:::beweis Die Quelle sitzt am Rand der kleinen Kugel
⁠**Schritt 1: Ableitungen verschieben.** Die Substitution $\boldsymbol{y}\mapsto\boldsymbol{x}-\boldsymbol{y}$ gibt $u(\boldsymbol{x})=\int\phi(\boldsymbol{y})f(\boldsymbol{x}-\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$. So kann man nach $\boldsymbol{x}$ differenzieren, ohne die Singularität anzufassen, und erhält nach einmaligem Verschieben

$$-\Delta u(\boldsymbol{x})=-\int_{\mathbb{R}^3}\nabla\phi(\boldsymbol{y})\cdot\nabla_{\boldsymbol{x}}f(\boldsymbol{x}-\boldsymbol{y})\;\mathrm{d}\boldsymbol{y}.$$

Dass Ableitung und Integral vertauscht werden dürfen, liefert ein Satz über Parameterintegrale, $\nabla\phi$ ist nach [Kapitel 4](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen/koordinatentransformationen.html) lokal integrierbar.

⁠**Schritt 2: Singularität ausschneiden.** Es ist $\nabla_{\boldsymbol{x}}f(\boldsymbol{x}-\boldsymbol{y})=-\nabla_{\boldsymbol{y}}f(\boldsymbol{x}-\boldsymbol{y})$. Schneidet man eine kleine Kugel $B_\varepsilon(0)$ aus (Abb. [8](#abb-8)), so gilt

$$-\Delta u(\boldsymbol{x})=\lim_{\varepsilon\to0}\int_{\mathbb{R}^3\setminus B_\varepsilon(0)}\nabla\phi(\boldsymbol{y})\cdot\nabla_{\boldsymbol{y}}f(\boldsymbol{x}-\boldsymbol{y})\;\mathrm{d}\boldsymbol{y}.$$

⁠**Schritt 3: partielle Integration.** Das Feld $\boldsymbol{E}=\nabla\phi$ ist außerhalb des Nullpunkts divergenzfrei, weil $\phi$ dort harmonisch ist. In Satz [8.3](der-satz-von-gau.html#satz-8-3) fällt also der Volumenterm weg, und es bleibt der Randterm auf $S_\varepsilon=\partial B_\varepsilon(0)$. Weil $f$ kompakten Träger hat, gibt es weit draußen keinen Beitrag:

$$\int_{\mathbb{R}^3\setminus B_\varepsilon(0)}\nabla\phi\cdot\nabla_{\boldsymbol{y}}f(\boldsymbol{x}-\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}=\int_{S_\varepsilon}\frac{\partial\phi}{\partial\boldsymbol{n}}(\boldsymbol{y})\,f(\boldsymbol{x}-\boldsymbol{y})\,\mathrm{d}\sigma_{\boldsymbol{y}}.$$

Achtung: $S_\varepsilon$ ist hier der Rand des *Außenraums*. Die äußere Normale des Außenraums zeigt deshalb zum Nullpunkt, $\boldsymbol{n}=-\hat{\boldsymbol{e}}_r$.

⁠**Schritt 4: Normalableitung.** Aus $\nabla\phi=-\frac{1}{4\pi r^2}\hat{\boldsymbol{e}}_r$ folgt auf $S_\varepsilon$

$$\frac{\partial\phi}{\partial\boldsymbol{n}}=\boldsymbol{n}\cdot\nabla\phi=\frac{1}{4\pi\varepsilon^2}=\frac{1}{|S_\varepsilon|}.$$

⁠**Schritt 5: Grenzwert.** Es bleibt der Mittelwert von $f(\boldsymbol{x}-\boldsymbol{y})$ über die kleine Kugel:

$$-\Delta u(\boldsymbol{x})=\lim_{\varepsilon\to0}\frac{1}{|S_\varepsilon|}\int_{S_\varepsilon}f(\boldsymbol{x}-\boldsymbol{y})\,\mathrm{d}\sigma_{\boldsymbol{y}}=f(\boldsymbol{x}).$$

Der Grenzwert gilt wegen der Stetigkeit von $f$: Die Abweichung vom Wert $f(\boldsymbol{x})$ ist höchstens $\sup_{|\boldsymbol{y}|<\varepsilon}|f(\boldsymbol{x})-f(\boldsymbol{x}-\boldsymbol{y})|$, und das geht gegen null.
:::

:::abbildung hm3/k5epsilon 8
Der Außenraum $\mathbb{R}^3\setminus B_\varepsilon(0)$ hat die kleine Kugel $S_\varepsilon$ als Rand. Seine äußere Normale zeigt zum Nullpunkt. Das Feld $\nabla\phi$ zeigt ebenfalls dorthin. Deshalb ist $\partial\phi/\partial\boldsymbol{n}$ positiv und gerade so groß, dass der Faktor $|S_\varepsilon|$ herausfällt.
:::

⁠**So liest man das:** Der Fluss von $\nabla\phi$ durch jede kleine Kugel ist $1$ dem Betrag nach, unabhängig vom Radius. Das ist die Aussage „im Nullpunkt sitzt eine Einheitsquelle“. In der Sprache der Signale und Systeme ist $-\Delta\phi=\delta$: Die Greensche Funktion ist die Impulsantwort des Laplace-Operators, und [(9.1)](#gl-9-1) ist die Faltung mit dieser Impulsantwort.

:::aufgabe Aufgabe 16 ★★ Eine homogen geladene Kugel
<span class="anker" id="aufg-16"></span>

Sei $f=1$ in $B_2(0)$ und $f=0$ außerhalb.

<ol class="al">

<li>

Berechne $u(0)$ aus [(9.1)](#gl-9-1).

</li>

<li>

Prüfe, dass $u(\boldsymbol{x})=2-r^2/6$ für $r\le2$ und $u(\boldsymbol{x})=8/(3r)$ für $r\ge2$ auf beiden Seiten die Gleichung erfüllt und bei $r=2$ stetig ist. Tipp: Für radiale Funktionen ist $\Delta u=\frac{1}{r^2}(r^2u')'$.

</li>

</ol>

:::loesung
(a) $u(0)=\int_{B_2}\frac{1}{4\pi|\boldsymbol{y}|}\,\mathrm{d}\boldsymbol{y}=\int_0^2\frac{1}{4\pi\rho}4\pi\rho^2\,\mathrm{d}\rho=\int_0^2\rho\,\mathrm{d}\rho=2$. (b) Innen: $u'=-r/3$, $(r^2u')'=-r^2$, also $\Delta u=-1$ und $-\Delta u=1$. Außen: $u'=-\frac{8}{3r^2}$, $r^2u'$ ist konstant, also $\Delta u=0$. Bei $r=2$ ist $u=2-\frac46=\frac43$ und $\frac{8}{6}=\frac43$. Auch die Steigungen stimmen, beide sind $-\frac23$. Der Wert bei $0$ passt zu (a).
:::
:::
