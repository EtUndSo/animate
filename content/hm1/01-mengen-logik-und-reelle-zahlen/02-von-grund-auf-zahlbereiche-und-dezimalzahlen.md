---
title: Von Grund auf: Zahlbereiche und Dezimalzahlen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210200
summary: Was man über die Zahlen voraussetzen muss und warum die Wurzel aus 2 kein Bruch ist
tags: natürlichen Zahlen, ganzen Zahlen, rationalen Zahlen, reelle Zahl, irrational
lang: de
---

Das Zeichen $:=$ heißt „wird definiert als“. Die __natürlichen Zahlen__ sind $\mathbb{N}:=\{1,2,3,\dots\}$, die __ganzen Zahlen__ $\mathbb{Z}:=\{0,1,-1,2,-2,\dots\}$, die __rationalen Zahlen__ (Brüche) $\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z},\ q\ne0\}$. Der Doppelpunkt heißt „für die gilt“.

:::definition Definition 0.1 (Reelle Zahl, vorläufig)
<span class="anker" id="satz-0-1"></span>

Eine __reelle Zahl__ ist eine Zahl mit Dezimaldarstellung, das heißt mit einem Vorzeichen, einem $m\in\mathbb{N}\cup\{0\}$ und Ziffern $a_1,a_2,\ldots\in\{0,1,\dots,9\}$, endlich oder unendlich vielen:

<span class="anker" id="gl-0-1"></span>
$$x=\pm\Bigl(m+\frac{a_1}{10}+\frac{a_2}{100}+\frac{a_3}{1000}+\dots\Bigr). \tag{0.1}$$

$\mathbb{R}$ ist die Menge der reellen Zahlen. Die Zahlen aus $\mathbb{R}$, die kein Bruch sind, heißen __irrational__.
:::

⁠**So liest man das:** $3/8=0{,}375$ endet, $5/11=0{,}4545\ldots$ ist periodisch, und jeder Bruch hat eine dieser beiden Formen. $\sqrt2=1{,}41421356\ldots$ wird nie periodisch. Es gilt $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$. Diese Definition ist eine Übergangslösung: Sie erklärt nicht, was eine unendliche Summe ist ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)), und sie ist nicht eindeutig, $1{,}000\ldots$ und $0{,}999\ldots$ sind dieselbe Zahl. Stufe [6](das-vollstandigkeitsaxiom.html#stufe-6) ersetzt sie durch Axiome.

::::formelsammlung
**Natürliche, ganze und rationale Zahlen**

$$\mathbb{N}:=\{1,2,3,\dots\},\qquad\mathbb{Z}:=\{0,1,-1,2,-2,\dots\},\qquad\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z},\ q\ne0\}$$

$:=$ heißt „wird definiert als“, der Doppelpunkt in der Mengenklammer „für die gilt“. Die rationalen Zahlen sind die Brüche. Die Null gehört nicht zu $\mathbb{N}$.

**Reelle Zahl (vorläufige Definition)**

$$x=\pm\Bigl(m+\frac{a_1}{10}+\frac{a_2}{100}+\frac{a_3}{1000}+\dots\Bigr)$$

Dezimaldarstellung mit Vorzeichen, $m\in\mathbb{N}\cup\{0\}$ und Ziffern $a_1,a_2,\ldots\in\{0,1,\dots,9\}$, endlich oder unendlich vielen; $\mathbb{R}$ ist die Menge der reellen Zahlen. Jeder Bruch hat eine endende oder periodische Darstellung, $\sqrt2$ wird nie periodisch. Die Darstellung ist nicht eindeutig ($1{,}000\ldots$ und $0{,}999\ldots$ sind dieselbe Zahl); später ersetzen Axiome diese Definition.

**Zahlbereiche**

$$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$$

Jeder Bereich enthält den vorigen. Die Zahlen aus $\mathbb{R}$, die kein Bruch sind, heißen irrational, etwa $\sqrt2$.
::::

::::lernkarten
:::karte begriff natürliche Zahlen
Welche Zahlen gehören zur Menge $\mathbb{N}$ der natürlichen Zahlen, und gehört die Null dazu?
---
Die Zahlen, die beim Zählen entstehen: $\mathbb{N}:=\{1,2,3,\dots\}$. Die Menge beginnt bei 1, die Null gehört nicht dazu.
--- falsch
Die Zahlen, die beim Zählen entstehen, mit der Null als erstem Element: $\mathbb{N}:=\{0,1,2,3,\dots\}$, denn auch „keins“ ist eine Anzahl.
--- falsch
Die positiven und die negativen ganzen Zahlen ohne die Null: $\mathbb{N}:=\{1,-1,2,-2,\dots\}$. Die Null gehört zu keinem Zahlbereich.
--- falsch
Alle positiven Zahlen, auch Brüche wie $\frac12$. Die Null gehört nicht dazu, weil sie nicht positiv ist.
:::
:::karte begriff ganze Zahlen
Welche Zahlen fasst die Menge $\mathbb{Z}$ der ganzen Zahlen zusammen?
---
Die natürlichen Zahlen, die Null und die Gegenzahlen der natürlichen Zahlen: $\mathbb{Z}:=\{0,1,-1,2,-2,\dots\}$.
--- falsch
Die natürlichen Zahlen zusammen mit der Null, aber ohne negative Zahlen: $\mathbb{Z}:=\{0,1,2,3,\dots\}$.
--- falsch
Alle Zahlen mit endlicher Dezimaldarstellung, also auch $0{,}5$ und $-2{,}25$, aber keine periodischen Zahlen.
--- falsch
Die natürlichen Zahlen und ihre Gegenzahlen ohne die Null, $\mathbb{Z}:=\{1,-1,2,-2,\dots\}$, weil die Null kein Ganzes zählt.
:::
:::karte begriff rationale Zahlen
Wie ist die Menge $\mathbb{Q}$ der rationalen Zahlen definiert, und welche Bedingung steht an den Nenner?
---
Als Menge der Brüche: $\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z},\ q\ne0\}$. Zähler und Nenner sind ganze Zahlen, der Nenner darf nicht null sein.
--- falsch
Als Menge der Brüche mit natürlichen Zahlen in Zähler und Nenner: $\mathbb{Q}:=\{p/q:p,q\in\mathbb{N}\}$. Negative Brüche gehören nicht dazu.
--- falsch
Als Menge der Brüche: $\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z}\}$. Zähler und Nenner sind beliebige ganze Zahlen, auch der Nenner null ist erlaubt.
--- falsch
Als Menge aller Zahlen mit Dezimaldarstellung: Jede Folge von Ziffern nach dem Komma ergibt einen Bruch, auch eine nie periodische.
:::
:::karte begriff reelle Zahl
Wie wird eine reelle Zahl vorläufig über ihre Dezimaldarstellung erklärt?
---
Als Zahl mit einem Vorzeichen, einem $m\in\mathbb{N}\cup\{0\}$ und endlich oder unendlich vielen Ziffern $a_1,a_2,\ldots\in\{0,1,\dots,9\}$: $x=\pm\Bigl(m+\frac{a_1}{10}+\frac{a_2}{100}+\frac{a_3}{1000}+\dots\Bigr)$.
--- falsch
Als Zahl mit einem Vorzeichen, einem $m\in\mathbb{N}\cup\{0\}$ und endlich vielen Ziffern nach dem Komma. Unendlich viele Ziffern sind nicht erlaubt, weil man sie nie vollständig aufschreiben könnte.
--- falsch
Als Zahl mit einem Vorzeichen, einem $m\in\mathbb{N}\cup\{0\}$ und Ziffern nach dem Komma, die sich ab einer Stelle periodisch wiederholen. Andere Ziffernfolgen ergeben keine Zahl.
--- falsch
Als Bruch $p/q$ mit $q\ne0$, dessen Dezimaldarstellung man durch schriftliches Teilen bestimmt. Jede reelle Zahl ist auf diese Weise ein Bruch mit ganzzahligem Zähler und Nenner.
:::
:::karte begriff irrational
Welche reellen Zahlen heißen irrational, und welches Beispiel kennt man dafür?
---
Die Zahlen aus $\mathbb{R}$, die kein Bruch sind. Ein Beispiel ist $\sqrt2=1{,}41421356\ldots$, dessen Dezimaldarstellung nie periodisch wird.
--- falsch
Die Zahlen aus $\mathbb{R}$, die negativ sind. Ein Beispiel ist $-\frac12$, das man nicht als Länge einer Strecke zeichnen kann.
--- falsch
Die Zahlen aus $\mathbb{R}$, deren Dezimaldarstellung nicht endet. Ein Beispiel ist $5/11=0{,}4545\ldots$ mit unendlich vielen Ziffern nach dem Komma.
--- falsch
Die Zahlen, die nicht in $\mathbb{R}$ liegen, weil sie keine Dezimaldarstellung haben. Ein Beispiel ist $\sqrt2$, das man nur näherungsweise angeben kann.
:::
:::karte zusammenhang Dezimaldarstellung eines Bruchs
Welche Form hat die Dezimaldarstellung eines Bruchs, und was folgt daraus für $\sqrt2$?
---
Sie endet oder ist periodisch, etwa $3/8=0{,}375$ und $5/11=0{,}4545\ldots$. Weil $\sqrt2=1{,}41421356\ldots$ nie periodisch wird, ist $\sqrt2$ kein Bruch.
--- falsch
Sie endet immer, etwa $3/8=0{,}375$. Weil $\sqrt2=1{,}41421356\ldots$ nicht endet, ist $\sqrt2$ kein Bruch; auch periodische Zahlen wie $0{,}4545\ldots$ sind keine Brüche.
--- falsch
Sie ist immer periodisch, etwa $5/11=0{,}4545\ldots$. Weil auch $\sqrt2$ nach genügend vielen Stellen periodisch wird, ist $\sqrt2$ ein Bruch mit sehr großem Nenner.
--- falsch
Sie kann jede beliebige Form haben, auch eine nie periodische. Ob $\sqrt2$ ein Bruch ist, lässt sich an der Dezimaldarstellung deshalb nicht ablesen.
:::
:::karte zusammenhang Übergangslösung
Warum ist die Erklärung der reellen Zahlen über Dezimaldarstellungen nur eine Übergangslösung?
---
Weil sie nicht erklärt, was eine unendliche Summe ist, und weil sie nicht eindeutig ist: $1{,}000\ldots$ und $0{,}999\ldots$ sind dieselbe Zahl. Später ersetzen Axiome sie.
--- falsch
Weil sie nur für positive Zahlen funktioniert: Ein Vorzeichen lässt sich in einer Dezimaldarstellung nicht unterbringen. Später ersetzen Axiome sie.
--- falsch
Weil sie die Brüche nicht erfasst: Brüche wie $3/8$ haben keine Dezimaldarstellung, sondern nur einen Zähler und einen Nenner. Später ersetzen Axiome sie.
--- falsch
Weil sie nur endlich viele Ziffern zulässt und damit $\sqrt2$ nicht erfasst. Später ersetzen Axiome sie, die auch unendliche Ziffernfolgen erlauben.
:::
:::karte formel Zahlbereiche
Wie liegen die Zahlbereiche $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ und $\mathbb{R}$ ineinander?
---
$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$: Jeder Bereich enthält den vorigen. In $\mathbb{R}$ liegen zusätzlich irrationale Zahlen wie $\sqrt2$.
--- falsch
$\mathbb{N}\subset\mathbb{Q}\subset\mathbb{Z}\subset\mathbb{R}$: Die Brüche liegen zwischen den natürlichen und den ganzen Zahlen, weil jeder Bruch zwischen zwei ganzen Zahlen liegt.
--- falsch
$\mathbb{N}\subset\mathbb{Z}\subset\mathbb{R}\subset\mathbb{Q}$: Jede reelle Zahl ist ein Bruch, und $\mathbb{Q}$ enthält zusätzlich Brüche mit unendlich langem Nenner.
--- falsch
Die Bereiche liegen nebeneinander und haben keine gemeinsamen Zahlen: Eine natürliche Zahl ist weder ein Bruch noch eine reelle Zahl.
:::
::::
