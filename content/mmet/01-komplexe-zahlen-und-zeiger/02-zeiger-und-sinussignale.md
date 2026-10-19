---
title: Zeiger (Phasoren) und Sinussignale
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Komplexe Zahlen und Zeiger
order: 10200
summary: Von Grund auf – was ein Sinussignal ist und warum es überall auftaucht, warum das Rechnen mit Sinus und Kosinus direkt so mühsam ist, und wie der rotierende Zeiger (Phasor) daraus einfache Addition und Multiplikation macht. Jeder Schritt wird hergeleitet.
tags: Sinussignal, Amplitude, Kreisfrequenz, Phase, Phasor, Zeiger, komplexe Amplitude, Zeigeraddition, Ableitung
---

:::grafik
Einstiegs-Animation: Links dreht sich ein Pfeil (Länge $A$) gleichmäßig in der komplexen Ebene gegen den
Uhrzeigersinn. Rechts, direkt daneben über eine gemeinsame waagerechte Zeitachse gekoppelt, zeichnet die
Projektion der Pfeilspitze auf die reelle Achse eine Kosinuskurve. Eine wandernde Verbindungslinie zeigt in
jedem Moment: Höhe der Kurve = waagerechter Schatten des Pfeils. Kernbotschaft des Bildes: **Ein Sinussignal ist
der Schatten eines rotierenden Zeigers.**
:::

:::konzept
Ein Sinussignal sieht aus wie eine endlos auf- und abschwingende Welle — aber dahinter steckt etwas viel
Einfacheres: ein Pfeil, der sich im Kreis dreht. Schaut man nur auf seinen **Schatten** an einer Wand, wandert
der genau als Sinuskurve auf und ab. Diese Sichtweise ist kein hübsches Beiwerk, sondern der entscheidende
Trick der ganzen Wechselstrom- und Signaltechnik: Weil wir im vorigen Abschnitt gelernt haben, dass sich
drehende Pfeile komplexe Zahlen sind, wird aus mühsamer Rechnerei mit Sinus und Kosinus plötzlich einfaches
Rechnen mit komplexen Zahlen — Addieren wird zum Aneinanderlegen von Pfeilen.
:::

**Worum es geht:** Komplexe Zahlen sind das Werkzeug (voriger Abschnitt), jetzt kommt die Anwendung. Wir klären
von Grund auf, was ein __Sinussignal__ ist, sehen, *warum* das direkte Rechnen damit so sperrig ist, und
entwickeln daraus den __Zeiger__ (Phasor), der alles einfach macht.

## Was ist ein Sinussignal — und warum ist es so wichtig?

Ein __Sinussignal__ (oder harmonisches Signal) ist eine Größe, die gleichmäßig zwischen einem Höchst- und einem
Tiefstwert hin- und herschwingt. In der Signalverarbeitung schreibt man es als Kosinus:

$$s(t) = A\,\cos(\omega t + \varphi).$$

Bevor wir die drei Buchstaben einzeln ansehen, die Frage: Warum ausgerechnet diese Kurve, und warum beschäftigt
sich ein ganzes Fach damit? Dafür gibt es zwei tiefe Gründe:

- **Sinusschwingungen sind überall.** Die Netzspannung aus der Steckdose, ein reiner Ton, die Pendelbewegung,
  Licht- und Funkwellen — alle sind sinusförmig.
- **Alle Signale bestehen aus ihnen.** Jedes noch so komplizierte periodische Signal lässt sich als Summe von
  Sinusschwingungen schreiben (die Fourier-Idee, die später kommt). Wer die Sinusschwingung beherrscht,
  beherrscht im Grunde alle Signale.

Deshalb lohnt sich der Aufwand, sie von Grund auf zu verstehen. Die drei Kenngrößen lassen sich direkt an der
Kurve ablesen:

- __$A$__: die __Amplitude__ — der maximale Ausschlag, also wie **hoch** die Welle schwingt.
- __$\omega$__: die __Kreisfrequenz__ — wie **schnell** sie schwingt (Einheit $\text{rad}/\text{s}$).
- __$\varphi$__: die __Phase__ — wie weit die Kurve **verschoben** ist, also wo sie bei $t=0$ gerade steht.

:::grafik
Eine Kosinuskurve $s(t)$ über der Zeit, vollständig beschriftet: die Amplitude $A$ als Höhe vom Mittelwert bis
zum Maximum; die Periodendauer $T$ als waagerechter Abstand zweier aufeinanderfolgender Maxima; die
Phasenverschiebung als horizontaler Versatz des ersten Maximums gegenüber $t=0$ (bei $\varphi>0$ nach links).
:::

## Woher die Kreisfrequenz kommt: ω = 2πf

Die Kreisfrequenz $\omega$ wirkt zunächst künstlich — warum nicht einfach die gewohnte __Frequenz__ $f$ (Anzahl
der Schwingungen pro Sekunde, in Hertz)? Der Zusammenhang lässt sich herleiten, und dann wird $\omega$
natürlich. Eine volle Schwingung ist einmal rund um den Kreis, und das entspricht einem Winkel von $2\pi$ (dem
vollen Vollkreis im Bogenmaß). Dieser volle Durchlauf dauert genau eine __Periodendauer__ $T$. Das Argument des
Kosinus, $\omega t$, muss in dieser Zeit also um genau $2\pi$ zunehmen:

$$\omega\,T = 2\pi \quad\Longrightarrow\quad \omega = \frac{2\pi}{T} = 2\pi f.$$

- __$\omega$__: die __Kreisfrequenz__ (Winkelzuwachs pro Sekunde).
- __$T$__: die __Periodendauer__ (Dauer einer vollen Schwingung); $f = 1/T$ ist die __Frequenz__.

$\omega$ ist also nichts anderes als „wie viel Winkel pro Sekunde" — und genau das passt zum Bild des
rotierenden Pfeils, der pro Sekunde um $\omega$ weiterdreht. Der Faktor $2\pi$ ist nur die Umrechnung von „volle
Umläufe" in „Bogenmaß".

:::grafik
Links ein Kreis, auf dem ein Punkt in der Zeit $T$ einmal ganz herumläuft (Winkel $2\pi$). Rechts die zugehörige
Kosinuskurve mit derselben Periodendauer $T$. Pfeile verdeutlichen: ein voller Umlauf ($2\pi$) entspricht einer
Periode ($T$), daher $\omega = 2\pi/T$.
:::

## Warum nicht direkt rechnen? Das Problem mit Sinus und Kosinus

Jetzt die entscheidende Motivation. In Schaltungen muss man Sinussignale ständig **addieren** — etwa wenn zwei
Wechselspannungen gleicher Frequenz zusammenkommen. Versuchen wir das ganz direkt, nur mit Trigonometrie. Mit
dem Additionstheorem $\cos(\omega t + \varphi) = \cos\omega t\,\cos\varphi - \sin\omega t\,\sin\varphi$ wird aus
jedem Summanden eine Mischung aus $\cos\omega t$ und $\sin\omega t$. Für die Summe zweier Signale gleicher
Frequenz:

$$A_1\cos(\omega t + \varphi_1) + A_2\cos(\omega t + \varphi_2) = \underbrace{(A_1\cos\varphi_1 + A_2\cos\varphi_2)}_{=\,C}\,\cos\omega t \;-\; \underbrace{(A_1\sin\varphi_1 + A_2\sin\varphi_2)}_{=\,S}\,\sin\omega t.$$

Das Ergebnis, $C\cos\omega t - S\sin\omega t$, soll am Ende wieder ein **einziges** Kosinussignal
$A\cos(\omega t + \varphi)$ sein. Vergleicht man es mit $A\cos(\omega t+\varphi) = A\cos\varphi\,\cos\omega t -
A\sin\varphi\,\sin\omega t$, muss $A\cos\varphi = C$ und $A\sin\varphi = S$ gelten — woraus man
$A = \sqrt{C^2 + S^2}$ und $\varphi = \operatorname{atan2}(S, C)$ zurückrechnet.

Das funktioniert, verlangt aber für eine simple Addition drei umständliche Arbeitsschritte:

1. **Zerlegen** — jedes Signal mit dem Additionstheorem in einen $\cos\omega t$- und einen $\sin\omega t$-Anteil
   aufspalten.
2. **Sammeln** — alle $\cos\omega t$-Anteile zu $C$ und alle $\sin\omega t$-Anteile zu $S$ zusammenfassen.
3. **Zusammenbauen** — aus $C$ und $S$ wieder Amplitude und Phase des einen Kosinus zurückrechnen.

Bei drei oder mehr Signalen wird das noch zäher. Genau hier setzt die bessere Idee an. Ein Hinweis, der gleich
wichtig wird: Die Hilfsgrößen $C$ und $S$ sehen verdächtig aus wie Real- und Imaginärteil *einer komplexen Zahl*.

## Der Zeiger (Phasor)

Erinnern wir uns an die Eulersche Formel aus dem vorigen Abschnitt: $\cos\alpha = \operatorname{Re}\{e^{j\alpha}\}$,
der Kosinus ist der Realteil eines rotierenden Einheitszeigers. Damit schreiben wir das Sinussignal um:

$$s(t) = A\cos(\omega t + \varphi) = \operatorname{Re}\!\left\{A\,e^{\,j(\omega t + \varphi)}\right\} = \operatorname{Re}\!\left\{\underbrace{A\,e^{\,j\varphi}}_{=\,X}\;e^{\,j\omega t}\right\}.$$

Im letzten Schritt haben wir nur $e^{j(\omega t + \varphi)} = e^{j\varphi}\cdot e^{j\omega t}$ benutzt (Exponenten
addieren sich) und den Teil, der die Zeit enthält, abgespalten. Übrig bleibt vorne eine feste komplexe Zahl, der
__Zeiger__ oder __Phasor__:

$$X = A\,e^{\,j\varphi}.$$

- __$X$__: der __Phasor__ (komplexe Amplitude) — ein ruhender Zeiger der Länge $A$ unter dem Winkel
  $\varphi$, also $|X| = A$ und $\arg X = \varphi$.
- __$A$__: die __Amplitude__ (Betrag des Zeigers).
- __$\varphi$__: die __Phase__ (Winkel des Zeigers).

Der entscheidende Gedanke: Der Faktor $e^{j\omega t}$ ist für **alle** Signale derselben Frequenz **gleich** —
er beschreibt nur das gemeinsame Mitdrehen. Alles, was ein Signal von einem anderen unterscheidet, steckt in $A$
und $\varphi$, also im Phasor $X$. Deshalb klammert man $e^{j\omega t}$ aus und rechnet nur noch mit
den Phasoren. Man ist von der zeitabhängigen Funktion zu **einer komplexen Zahl** übergegangen.

:::grafik
In der komplexen Ebene ein ruhender Pfeil $X = A\,e^{j\varphi}$: Länge $A$, Winkel $\varphi$ zur
reellen Achse. Daneben die Notiz, dass hier die Zeit (der Faktor $e^{j\omega t}$) bewusst „geparkt" ist — der
Phasor speichert nur Amplitude und Phase.
:::

## Der rotierende Zeiger und sein Schatten

Die Zeit kommt zurück, sobald man den Phasor mit $e^{j\omega t}$ multipliziert. Dieses Produkt ist das
__komplexe Sinussignal__

$$z(t) = X\,e^{\,j\omega t} = A\,e^{\,j(\omega t + \varphi)}.$$

Nach der Multiplikationsregel aus dem vorigen Abschnitt dreht der Faktor $e^{j\omega t}$ den Pfeil fortlaufend um
den mit der Zeit wachsenden Winkel $\omega t$ — der Zeiger **rotiert** mit der Kreisfrequenz $\omega$ gegen den
Uhrzeigersinn, während seine Länge konstant bleibt. In Zahlen: $|z(t)| = A$ und $\arg z(t) = \omega t + \varphi$,
und bei $t = 0$ ist $z(0) = X$ — der Phasor ist also die „Momentaufnahme" des rotierenden Zeigers zum Zeitpunkt
null.

Das tatsächliche, reelle Signal ist der **Realteil** davon — die Projektion der rotierenden Pfeilspitze auf die
reelle Achse — ganz im Einklang mit $z = x + jy$ aus dem vorigen Abschnitt ($x$ ist der Realteil):

$$s(t) = \operatorname{Re}\{z(t)\} = \operatorname{Re}\!\left\{X\,e^{\,j\omega t}\right\} = A\cos(\omega t + \varphi).$$

Der **Imaginärteil** desselben rotierenden Zeigers liefert übrigens das um $90^\circ$ verschobene Sinussignal,
$y(t) = \operatorname{Im}\{z(t)\} = A\sin(\omega t + \varphi)$. Das ist genau die Einstiegs-Animation: Der volle,
rotierende komplexe Zeiger $z(t)$ ist das „ganze" Signal, die reelle Kosinuskurve nur sein Schatten auf der
reellen Achse.

**Zweite Sichtweise: zwei gegenläufige Zeiger.** Man kann denselben Kosinus auch als Summe **zweier**
gegenläufig rotierender Zeiger sehen. Aus der umgekehrten Eulerschen Formel folgt nämlich
$\cos\alpha = \tfrac{1}{2}(e^{j\alpha} + e^{-j\alpha})$. Addiert man zum komplexen Signal $z(t)$ sein
konjugiertes $z^*(t)$, heben sich die Imaginärteile weg und der Realteil verdoppelt sich, also

$$A\cos(\omega t + \varphi) = \tfrac{1}{2}\big(z(t) + z^{*}(t)\big) = \tfrac{1}{2}X\,e^{\,j\omega t} + \tfrac{1}{2}X^{*}\,e^{-j\omega t}.$$

Ein Zeiger dreht gegen den Uhrzeigersinn, der andere (mit der konjugierten Amplitude $X^*$) im
Uhrzeigersinn; ihre Imaginärteile heben sich in jedem Moment auf, sodass die Summe stets reell bleibt. Diese
Zerlegung in eine „positive" und eine „negative" Drehrichtung ist später der Schlüssel zum **Spektrum** mit
seinen positiven und negativen Frequenzen.

:::grafik
Animation mit zwei Teilbildern. Oben: ein einzelner Zeiger $Xe^{j\omega t}$ rotiert, seine
Projektion zeichnet die Kosinuskurve. Unten: zwei gegenläufig rotierende Zeiger ($\tfrac12Xe^{j\omega t}$
gegen den Uhrzeigersinn, $\tfrac12X^*e^{-j\omega t}$ im Uhrzeigersinn); ihre Summe bleibt in jedem
Moment auf der reellen Achse und ergibt dieselbe Kosinuskurve.
:::

## Der Lohn: Addition wird zur Zeigeraddition

Jetzt lösen wir das Additionsproblem von oben noch einmal — mit Phasoren. Weil jedes Signal der Realteil seines
rotierenden Zeigers ist und der Realteil eine **lineare** Operation ist (man darf die Summe zweier Realteile als
Realteil der Summe schreiben), gilt:

$$s_1(t) + s_2(t) = \operatorname{Re}\{X_1 e^{j\omega t}\} + \operatorname{Re}\{X_2 e^{j\omega t}\} = \operatorname{Re}\{(X_1 + X_2)\,e^{j\omega t}\}.$$

Das Ergebnis ist also wieder ein Sinussignal derselben Frequenz, und sein Phasor ist einfach die **Summe der
Einzelphasoren**:

$$X_\text{ges} = X_1 + X_2 + \ldots$$

Statt der ganzen Zerlege-Sortiere-Zusammenbau-Prozedur aus Trigonometrie legt man nur noch die Zeiger als Pfeile
aneinander (Real- und Imaginärteile addieren sich getrennt) und liest Amplitude und Phase des Summenpfeils ab.
Und hier schließt sich der Kreis zur vorhin aufgefallenen Beobachtung: Die mühsamen Hilfsgrößen $C$ und $S$ von
oben waren **genau** der Real- und Imaginärteil von $X_1 + X_2$. Die Trigonometrie-Rechnung
hat also heimlich dasselbe getan wie die Zeigeraddition — nur viel umständlicher. Das ist der Grund, warum die
Wechselstromtechnik grundsätzlich mit Zeigern rechnet.

:::grafik
Zwei Phasoren $X_1$ und $X_2$ (gleiche Frequenz, verschiedene Länge/Winkel) werden
Pfeil-an-Pfeil addiert; der Summenpfeil $X_\text{ges}$ vom Ursprung zur Spitze ist hervorgehoben, mit
abgelesener Amplitude und Phase. Darunter, zeitlich gekoppelt, die drei Kosinuskurven: $s_1$, $s_2$ und ihre
Summe — sichtbar wieder eine reine Kosinuskurve derselben Frequenz.
:::

## Ableiten und Integrieren werden zu Multiplikation

Ein zweiter, ebenso großer Vorteil. Leitet man den rotierenden Zeiger nach der Zeit ab, so gilt (die Ableitung
von $e^{j\omega t}$ ist $j\omega\,e^{j\omega t}$):

$$\frac{\mathrm{d}}{\mathrm{d}t}\left(X\,e^{j\omega t}\right) = j\omega\,X\,e^{j\omega t}.$$

Im Zeiger-Bild bedeutet Ableiten also schlicht: **Multiplizieren mit $j\omega$**. Und weil $j\omega = \omega\,e^{j\pi/2}$
ist, heißt das anschaulich: um $90^\circ$ drehen (das $j$) und mit $\omega$ strecken. Umgekehrt wird Integrieren
zur **Division durch $j\omega$**. Das ist enorm: Eine Differentialgleichung für Ströme und Spannungen (mit
Ableitungen) verwandelt sich im Zeiger-Bild in eine ganz gewöhnliche **algebraische** Gleichung mit komplexen
Zahlen. Genau das macht später die Berechnung von Wechselstromschaltungen mit Spulen und Kondensatoren so
handlich.

:::grafik
Ein Phasor $X$ und sein abgeleiteter Zeiger $j\omegaX$: um $90^\circ$ gegen den
Uhrzeigersinn gedreht (durch das $j$) und um den Faktor $\omega$ gestreckt. Pfeile und Winkel beschriftet;
daneben der Hinweis „Ableiten = $\times\,j\omega$, Integrieren = $\div\,j\omega$".
:::

**Stolperstein: Kosinus oder Sinus, Amplitude oder Effektivwert?** Zwei Konventionen muss man vorab festlegen:

- **Bezugsform (Kosinus oder Sinus):** Ein Sinus ist ein um $90^\circ$ verschobener Kosinus, $\sin(\omega t) =
  \cos(\omega t - \tfrac{\pi}{2})$. Rechnet man die Phasen mal auf Kosinus, mal auf Sinus bezogen, verschiebt
  sich alles um $90^\circ$.
- **Zeigerlänge (Amplitude oder Effektivwert):** In der Elektrotechnik nimmt man als Länge häufig nicht die
  Amplitude $A$, sondern den **Effektivwert** $A/\sqrt{2}$ (praktisch fürs Rechnen mit Leistungen).

Beides ist in Ordnung — man muss nur bei **einer** Wahl konsequent bleiben.

:::kern
Ein __Sinussignal__ $s(t) = A\cos(\omega t + \varphi)$ hat __Amplitude__ $A$, __Kreisfrequenz__ $\omega = 2\pi f$
(hergeleitet: ein voller Umlauf $2\pi$ je Periode $T$) und __Phase__ $\varphi$. Direktes Addieren über
Trigonometrie ist umständlich; der __Zeiger__ (Phasor) $X = A e^{j\varphi}$ fasst Amplitude und Phase
in einer komplexen Zahl zusammen (der gemeinsame Faktor $e^{j\omega t}$ wird ausgeklammert), und
$s(t) = \operatorname{Re}\{Xe^{j\omega t}\}$ ist der Schatten des rotierenden Zeigers. Dann wird
__Addition__ gleichfrequenter Signale zur __Zeigeraddition__ $X_\text{ges} = X_1 +
X_2$ (genau das, was die Trigonometrie heimlich tut), und __Ableiten/Integrieren__ wird zu
$\times\,j\omega$ bzw. $\div\,j\omega$ — Differentialgleichungen werden zu Algebra. Konventionen (Kosinus/Sinus,
Amplitude/Effektivwert) vorher festlegen.
:::

Ein einzelner Zeiger beschreibt genau eine Frequenz. Setzt man ein Signal aus mehreren Frequenzen zusammen,
braucht man eine Darstellung, die alle Anteile auf einmal zeigt — das __Spektrum__, das Thema des nächsten
Abschnitts.

:::quiz
F: Inwiefern ist ein Sinussignal „der Schatten eines rotierenden Zeigers"?
A: Lässt man einen Pfeil der Länge $A$ gleichmäßig in der komplexen Ebene rotieren, so wandert die Projektion seiner Spitze auf die reelle Achse genau als Kosinuskurve auf und ab. Das reelle Signal $s(t)=A\cos(\omega t+\varphi)$ ist also der Realteil (Schatten) des vollen komplexen Zeigers $z(t)=A e^{j(\omega t+\varphi)}$.
F: Warum beschäftigt sich ein ganzes Fach gerade mit der Sinusschwingung?
A: Erstens sind Sinusschwingungen überall (Netzspannung, Ton, Welle, Pendel). Zweitens lässt sich jedes periodische Signal als Summe von Sinusschwingungen schreiben (Fourier) — wer die Sinusschwingung beherrscht, beherrscht im Grunde alle Signale.
F: Wie leitet sich $\omega=2\pi f$ her, und was bedeutet $\omega$ anschaulich?
A: Eine volle Schwingung entspricht einem Umlauf um $2\pi$ im Bogenmaß und dauert eine Periode $T$; das Kosinusargument $\omega t$ muss in dieser Zeit um $2\pi$ zunehmen, also $\omega T=2\pi$, d. h. $\omega=2\pi/T=2\pi f$. $\omega$ ist der Winkelzuwachs pro Sekunde — wie schnell der Zeiger dreht.
F: Warum ist das direkte Addieren zweier Sinussignale über Trigonometrie so umständlich?
A: Man muss jedes Signal per Additionstheorem in $\cos\omega t$- und $\sin\omega t$-Anteile zerlegen, diese getrennt zu $C$ und $S$ sammeln und daraus Amplitude und Phase des Summensignals zurückrechnen — drei Schritte, die mit jedem weiteren Summanden zäher werden.
F: Was ist der Phasor $X=Ae^{j\varphi}$, und warum darf man den Faktor $e^{j\omega t}$ ausklammern?
A: Der Phasor ist ein ruhender Zeiger, der Amplitude ($|X|=A$) und Phase ($\arg X=\varphi$) in einer komplexen Zahl speichert. Da $e^{j\omega t}$ das gemeinsame Mitdrehen aller Signale derselben Frequenz beschreibt, trägt nur $X$ die unterscheidende Information — man klammert den Zeitfaktor aus und rechnet nur mit den Phasoren.
F: Warum ist das reelle Signal der Realteil und nicht der Zeiger selbst?
A: Der physikalisch messbare Wert ist eine reelle Größe — die waagerechte Projektion des rotierenden Zeigers, also $\operatorname{Re}\{z(t)\}=A\cos(\omega t+\varphi)$. Der komplexe Zeiger ist das vollständige Rechenobjekt; der Imaginärteil liefert dasselbe Signal um $90^\circ$ verschoben.
F: Was besagt die Zerlegung $A\cos(\omega t+\varphi)=\tfrac12(z+z^*)$ in zwei gegenläufige Zeiger?
A: Ein Kosinus lässt sich als Summe zweier halb so langer Zeiger schreiben, die gegenläufig rotieren ($\tfrac12Xe^{j\omega t}$ und $\tfrac12X^*e^{-j\omega t}$); ihre Imaginärteile heben sich stets auf, die Summe bleibt reell. Diese Aufspaltung in positive und negative Drehrichtung ist später der Ursprung der positiven und negativen Frequenzen im Spektrum.
F: Warum wird die Addition gleichfrequenter Signale zur bloßen Zeigeraddition $X_\text{ges}=X_1+X_2$?
A: Weil der Realteil linear ist, darf man $\operatorname{Re}\{X_1e^{j\omega t}\}+\operatorname{Re}\{X_2e^{j\omega t}\}=\operatorname{Re}\{(X_1+X_2)e^{j\omega t}\}$ schreiben. Das Ergebnis ist wieder ein Sinussignal derselben Frequenz mit Phasor $X_1+X_2$ — man legt nur noch die Pfeile aneinander. Die Hilfsgrößen $C,S$ der Trigonometrie waren gerade Real- und Imaginärteil dieser Summe.
F: Warum wird Ableiten im Zeigerbild zur Multiplikation mit $j\omega$?
A: Die Ableitung von $e^{j\omega t}$ ist $j\omega e^{j\omega t}$, also $\frac{d}{dt}(Xe^{j\omega t})=j\omega Xe^{j\omega t}$. Mit $j\omega=\omega e^{j\pi/2}$ heißt das: um $90^\circ$ drehen und mit $\omega$ strecken; Integrieren ist entsprechend Division durch $j\omega$. Dadurch werden Differentialgleichungen für Ströme und Spannungen zu algebraischen Gleichungen.
F: Welche zwei Konventionen muss man beim Rechnen mit Zeigern vorab festlegen?
A: Erstens die Bezugsform (Kosinus oder Sinus), denn ein Sinus ist ein um $90^\circ$ verschobener Kosinus — sonst verschieben sich alle Phasen. Zweitens die Zeigerlänge (Amplitude $A$ oder Effektivwert $A/\sqrt2$); in der ET nimmt man oft den Effektivwert. Entscheidend ist, bei einer Wahl konsequent zu bleiben.
:::
