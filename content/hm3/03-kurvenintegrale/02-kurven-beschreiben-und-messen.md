---
title: Stufe 1: Kurven beschreiben und messen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130200
summary: Wer längs eines Wegs rechnen will, braucht den Weg als Formel.
tags: Kurve, Parametrisierung, stückweise stetig differenzierbar, regulär parametrisierte Kurve, geschlossene Kurve, einfache Kurve, Spur, einfach geschlossen
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Wer längs eines Wegs rechnen will, braucht den Weg als Formel. Diese Stufe sagt, welche Formeln zulässig sind, welche Eigenschaften einer Kurve man unterscheidet und wie man ihre Länge berechnet.
:::

**Die Idee.** Eine __Kurve__ ist der Weg eines Punkts: Zu jedem Zeitpunkt $t$ ist er am Ort $\gamma(t)$. Die Abbildung $\gamma$ heißt __Parametrisierung__. Ihre komponentenweise Ableitung $\dot\gamma(t)=\frac{\mathrm{d}}{\mathrm{d} t}\gamma(t)$ ist der Geschwindigkeitsvektor. Er liegt tangential an der Kurve und zeigt in Laufrichtung, seine Länge $|\dot\gamma(t)|$ ist das Tempo. Drei Fragen unterscheiden Kurven (Abb. [1](#abb-1)): Bleibt der Punkt irgendwo stehen? Kommt er zum Start zurück? Ist er zu zwei Zeiten am selben Ort?

:::abbildung hm3/k3kurven 1
Vier Kurven. Der Kreis ist nur am Anfang und am Ende am selben Ort. Der zweimal durchlaufene Kreis und die Acht sind auch zwischendurch am selben Ort (rot). In der Spitze steht der Punkt einen Augenblick still, obwohl die Formel glatt ist.
:::

:::definition Definition 1.1 (Reguläre Kurve)
<span class="anker" id="satz-1-1"></span>

Sei $\gamma:[a,b]\to\mathbb{R}^n$ __stückweise stetig differenzierbar__: $\gamma$ ist stetig und bis auf endlich viele Knick- und Endpunkte stetig differenzierbar, an diesen existieren die einseitigen Ableitungen. Gilt überall $\dot\gamma(t)\neq0$, an Knick- und Endpunkten für die einseitigen Ableitungen, heißt $\gamma$ __regulär parametrisierte Kurve__. Sie heißt

<ul>

<li>

__geschlossene Kurve__, falls $\gamma(a)=\gamma(b)$,

</li>

<li>

__einfache Kurve__ oder doppelpunktfrei, falls aus $\gamma(s)=\gamma(t)$ mit $s<t$ stets $s=a$ und $t=b$ folgt.

</li>

</ul>

Die Punktmenge $\Gamma=\gamma([a,b])$ heißt __Spur__ der Kurve.
:::

⁠**So liest man das:** Regulär heißt: Der Punkt bleibt nie stehen, also gibt es überall eine Laufrichtung. Das ist nicht selbstverständlich: $(t^2,t^3)$ ist glatt in $t$, hat bei $t=0$ aber $\dot\gamma=0$ und eine Spitze. Knicke sind erlaubt, etwa die Ecken eines Quadratrands. Dort existieren beide einseitigen Ableitungen, sie sind nur verschieden. In der Bedingung für *einfach* sind $s$ und $t$ zwei Zeitpunkte auf derselben Kurve. Einmal und zweimal durchlaufener Kreis haben dieselbe Spur, sind aber verschiedene Kurven.

| Kurve | regulär | geschlossen | einfach |
|---|---|---|---|
| Kreis $(\cos t,\sin t)$ auf $[0,2\pi]$ | ja | ja | ja |
| Kreis $(\cos t,\sin t)$ auf $[0,4\pi]$ | ja | ja | nein |
| Acht $(\sin t,\sin2t)$ auf $[0,2\pi]$ | ja | ja | nein |
| Viertelkreis $\kappa$ aus dem Rechenmodell | ja | nein | ja |
| Spitze $(t^2,t^3)$ auf $[-1,1]$ | nein | nein | ja |

:::frage Was heißt es, dass eine Kurve einfach ist?
Sie läuft durch keinen Punkt zweimal. Prüfen kann man das so: Suche zwei Zeitpunkte $s<t$ mit $\gamma(s)=\gamma(t)$. Erlaubt ist nur das Paar $s=a$, $t=b$, also dass Anfangs- und Endpunkt zusammenfallen. Dann heißt die Kurve __einfach geschlossen__. Der Kreis auf $[0,2\pi]$ ist es. Der Kreis auf $[0,4\pi]$ nicht, denn $\gamma(0)=\gamma(2\pi)$, und $2\pi$ ist nicht das Ende des Intervalls. Die Acht auch nicht: Sie ist bei $t=0$ und bei $t=\pi$ im Nullpunkt. Eine einfach geschlossene Kurve in der Ebene trennt ein Inneres von einem Äußeren. Deshalb kann sie eine Fläche umranden.
:::

**Wie berechnet man die Länge einer Kurve?** Man setzt Punkte auf die Kurve und verbindet sie geradlinig zu einem __Sehnenzug__. Für einen kleinen Zeitschritt $\Delta t$ ist die Sehne fast Geschwindigkeit mal Zeit:

$$|\gamma(t+\Delta t)-\gamma(t)|\approx|\dot\gamma(t)|\,\Delta t.$$

Die Summe aller Sehnen ist also fast eine Riemann-Summe von $|\dot\gamma|$. Für $\Delta t\to0$ entsteht ein Integral, die __Kurvenlänge__

<span class="anker" id="gl-1-1"></span>
$$\mathcal L(\gamma)=\int_a^b|\dot\gamma(t)|\,\mathrm{d} t=\int_a^b\sqrt{\dot\gamma_1(t)^2+\dots+\dot\gamma_n(t)^2}\;\mathrm{d} t. \tag{1.1}$$

Das ist Tempo mal Zeit, summiert. Das Längenstück $\mathrm{d} s=|\dot\gamma(t)|\,\mathrm{d} t$ heißt __Linienelement__. Ein Graph $y=f(x)$, $a\le x\le b$, ist die Kurve $\gamma(x)=(x,f(x))$ mit $\dot\gamma=(1,f'(x))$. Für ihn wird [(1.1)](#gl-1-1) zu

<span class="anker" id="gl-1-2"></span>
$$\mathcal L=\int_a^b\sqrt{1+f'(x)^2}\;\mathrm{d} x. \tag{1.2}$$

⁠**Beispiele.** Der Kreis $\gamma(t)=R(\cos t,\sin t)$ hat das feste Tempo $R$, also $\mathcal L=\int_0^{2\pi}R\,\mathrm{d} t=2\pi R$. Die Schraubenlinie $(\cos t,\sin t,t)$ auf $[0,2\pi]$ hat $|\dot\gamma|=\sqrt{\sin^2t+\cos^2t+1}=\sqrt2$, also $\mathcal L=2\pi\sqrt2\approx8{,}89$. **Kontrolle:** Für die Gerade $f(x)=mx$ gibt [(1.2)](#gl-1-2) den Wert $(b-a)\sqrt{1+m^2}$, das ist Pythagoras.

Rechnerisch ist die Wurzel das Problem, sie hat oft keine geschlossene Stammfunktion. Bei der Ellipse $(a_1\cos t,\,a_2\sin t)$ ist $|\dot\gamma|=\sqrt{a_1^2\sin^2t+a_2^2\cos^2t}$. Für $a_1\neq a_2$ führt das auf __elliptische Integrale__, die man nur numerisch auswerten kann.

:::aufgabe Aufgabe 1 ★ Kurven einordnen
<span class="anker" id="aufg-1"></span>

Sind die Kurven regulär, geschlossen, einfach?

<ol class="al">

<li>

$(2\cos t,\,\sin t)$ auf $[0,2\pi]$

</li>

<li>

$(t^2-4,\,t^3-4t)$ auf $[-3,3]$

</li>

<li>

$(\cos t,\,\sin t,\,t)$ auf $[0,4\pi]$

</li>

<li>

$(\cos^3t,\,\sin^3t)$ auf $[0,2\pi]$

</li>

<li>

$(t,\,|t|)$ auf $[-1,1]$

</li>

</ol>

Berechne außerdem die Längen der Kurven aus (c) und (d).

:::loesung
(a) $\dot\gamma=(-2\sin t,\cos t)\neq0$: regulär, geschlossen, einfach (eine Ellipse). (b) $\dot\gamma=(2t,3t^2-4)$: Die erste Komponente ist nur bei $t=0$ null, dort ist die zweite $-4$. Also regulär. $\gamma(-3)=(5,-15)\neq\gamma(3)=(5,15)$: nicht geschlossen. $\gamma(-2)=\gamma(2)=(0,0)$: nicht einfach. (c) $|\dot\gamma|=\sqrt2$: regulär, nicht geschlossen, einfach, weil die dritte Komponente wächst. Länge $4\pi\sqrt2$. (d) $\dot\gamma=3\sin t\cos t\,(-\cos t,\sin t)$ ist bei $t=k\pi/2$ null: nicht regulär, dort sitzen vier Spitzen. Geschlossen und einfach. Länge: $|\dot\gamma|=3|\sin t\cos t|$, also $4\int_0^{\pi/2}3\sin t\cos t\,\mathrm{d} t=6$. (e) Knick bei $t=0$ mit den einseitigen Ableitungen $(1,-1)$ und $(1,1)$: regulär, nicht geschlossen, einfach.
:::
:::
