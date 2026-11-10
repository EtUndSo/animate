---
title: Anwendung: der Zinssatz eines Ratenkredits
pfad: Informatik / Programmieren / Python / Entscheidungen und Schleifen
adresse: informatik/programmieren/python/entscheidungen-und-schleifen
knoten: Kapitel 3: Entscheidungen und Schleifen
order: 6041000
summary: Bisektion und Newton sind nicht für Wurzeln gemacht, sondern für Gleichungen, die man nicht nach der Unbekannten auflösen kann.
tags: Restschuld, Annuitätenformel, effektiven Jahreszins
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Bisektion und Newton sind nicht für Wurzeln gemacht, sondern für Gleichungen, die man nicht nach der Unbekannten auflösen kann. Dieser Abschnitt löst eine solche Gleichung aus dem Alltag: Welcher Zinssatz steckt in einem Kredit, den man in gleichen Monatsraten zurückzahlt?
:::

### Was du dafür brauchst: Zinsen, Raten und Restschuld

<span class="anker" id="stufe-9-1"></span>

Ein Autohaus bietet ein Auto für 20 000 Euro an, alternativ in 60 Monatsraten zu 400 Euro. Zusammen sind das 24 000 Euro; die 4000 Euro mehr sind die Zinsen. Welcher Zinssatz steckt darin?

Wer einen Kredit über den Betrag $K$ aufnimmt, schuldet anfangs $K$. Was jeweils noch zurückzuzahlen ist, heißt die __Restschuld__ $S$. Jeden Monat kommen Zinsen hinzu: Beim Monatszins $r$, als Dezimalzahl geschrieben (0,5 % ist 0,005), wächst die Restschuld auf $S\,(1+r)$. Danach zahlt man die Monatsrate $R$, und die Restschuld sinkt um $R$. Mit der Abkürzung $q=1+r$ gilt also von Monat zu Monat

$$S_0=K,\qquad S_{k+1}=S_k\,q-R .$$

Der Kredit ist nach $n$ Monaten genau dann abbezahlt, wenn $S_n=0$ ist.

Setzt man die Regel immer wieder in sich selbst ein, entsteht eine Formel für $S_n$:

$$S_1=Kq-R,\qquad S_2=Kq^2-Rq-R,\qquad\ldots,\qquad S_n=Kq^n-R\,\bigl(q^{n-1}+q^{n-2}+\cdots+q+1\bigr).$$

Mit dem Wert der Summe in der Klammer, $(q^n-1)/r$ für $r\ne0$, folgt aus $S_n=0$ die __Annuitätenformel__

$$R=\frac{K\,r\,q^n}{q^n-1}=\frac{K\,r}{1-q^{-n}} .$$

Sie liefert zu einem bekannten Zins die Monatsrate.

:::herleitung Die Summe in der Klammer
Sei $G=1+q+q^2+\cdots+q^{n-1}$. Multipliziert man mit $q$, verschiebt sich jeder Summand um eine Stelle: $qG=q+q^2+\cdots+q^n$. In der Differenz $qG-G$ heben sich alle Summanden bis auf $q^n$ und $1$ weg, also $(q-1)\,G=q^n-1$ und mit $q-1=r$

$$G=\frac{q^n-1}{r}\qquad(r\ne0).$$

Eingesetzt wird $S_n=Kq^n-R\,(q^n-1)/r$. Aus $S_n=0$ folgt $R\,(q^n-1)=K\,r\,q^n$, und Teilen durch $q^n-1$ ergibt die Annuitätenformel; der zweite Bruch entsteht, wenn man Zähler und Nenner durch $q^n$ teilt.
:::

Kreditangebote in der EU müssen einen __effektiven Jahreszins__ nennen. Er rechnet die Kosten des Kredits mit Zinseszins auf ein Jahr um. Ohne weitere Kosten und bei gleichen Monatsraten ist er $(1+r)^{12}-1$: der Zins, der in zwölf Monaten mit Zinseszins aus dem Monatszins $r$ wird.

::::beispiel
Für das Auto ist $K=20\,000$ Euro und $n=60$. Bei einem Monatszins von 0,5 % wäre die Rate $20\,000\cdot0{,}005/(1-1{,}005^{-60})\approx386{,}66$ Euro, also weniger als die verlangten 400 Euro. Bei 1 % wären es 444,89 Euro, also mehr. Der gesuchte Monatszins liegt deshalb zwischen 0,5 % und 1 %.
::::

⁠**Kurz gesagt:** Die Restschuld wächst jeden Monat um die Zinsen und sinkt um die Rate; beim richtigen Zins ist sie nach der letzten Rate genau null.

### Der Zinssatz als Nullstelle

<span class="anker" id="stufe-9-2"></span>

Trägt man die Rate, die nach der Annuitätenformel zu einem Monatszins gehört, über dem Zins auf, und dazu die verlangte Rate von 400 Euro als waagerechte Gerade, schneiden sich beide beim gesuchten Zins (Abb. [11](#abb-11)).

:::abbildung prog/k3kredit 11
Die Monatsrate für einen Kredit über 20 000 Euro mit 60 Raten in Abhängigkeit vom Monatszins (blau) und die verlangte Rate von 400 Euro (orange). Ihr Schnittpunkt ist der Zins, der im Angebot steckt. Ohne Zins wäre die Rate $20\,000/60\approx333{,}33$ Euro; mit jedem Zehntelprozent mehr steigt sie.
:::

Den Schnittpunkt kann man als Nullstelle schreiben. Am einfachsten geht das mit der Restschuld nach der letzten Rate, als Funktion des Zinses betrachtet:

$$f(r)=S_n=Kq^n-R\,\bigl(q^{n-1}+q^{n-2}+\cdots+q+1\bigr),\qquad q=1+r .$$

Ist $f(r)>0$, reicht die verlangte Rate bei diesem Zins nicht, und es bleibt Schuld übrig; ist $f(r)<0$, hätte man zu viel zurückgezahlt. Beim gesuchten Zins ist $f(r)=0$.

Bei $r=0$ gibt es keine Zinsen, und es bleibt $f(0)=K-nR=20\,000-24\,000=-4000$ Euro, also $f(0)<0$. Beim Zins $r=R/K$, hier 2 % im Monat, sind die Zinsen auf die volle Schuld genau so groß wie die Rate: Die Restschuld bleibt bei $K$, und $f(R/K)=K>0$. $f$ ist stetig, also liegt nach dem Zwischenwertsatz eine Nullstelle zwischen 0 und $R/K$. Es ist auch nur eine. Teilt man $f(r)$ durch $q^n$, steht $K-R\,\bigl(q^{-1}+q^{-2}+\cdots+q^{-n}\bigr)$ da. Jeder Summand $q^{-k}$ wird kleiner, wenn $r$ wächst; dieser Ausdruck wächst also streng. Weil $q^n$ positiv ist, hat $f$ dasselbe Vorzeichen wie er und wechselt es genau einmal. Nach $r$ auflösen lässt sich die Gleichung $f(r)=0$ mit den üblichen Mitteln nicht, denn für $n=60$ ist sie eine Gleichung 60. Grades in $q$.

⁠**Kurz gesagt:** Der gesuchte Zins ist die einzige Nullstelle der Restschuld $f(r)$ zwischen 0 und $R/K$.

:::hintergrund Gibt es doch eine Formel?
$f(r)=0$ ist eine Polynomgleichung vom Grad $n$ in $q$. Für Grad 2 kennt man die Lösungsformel aus der Schule, und auch für die Grade 3 und 4 gibt es Formeln, die nur Grundrechenarten und Wurzeln benutzen. Für Grad 5 und höher gibt es keine solche Formel, die für alle Polynome gilt; das ist der Satz von Abel und Ruffini. Er schließt nicht aus, dass besondere Gleichungen wie diese doch eine Lösung mit Wurzeln haben; eine Formel für den Zins eines beliebigen Kredits ist aber nicht bekannt. Tabellenkalkulationen rechnen den Zins deshalb schrittweise aus, wie dieses Kapitel. Ihre Funktion dafür heißt ZINS, englisch RATE. Sie beginnt bei einem Schätzwert, ohne Angabe bei 10 %, und meldet einen Fehler, wenn sich die aufeinanderfolgenden Ergebnisse nach 20 Schritten nicht bis auf 0,0000001 angenähert haben.
:::

### Der Zinssatz durch Bisektion

<span class="anker" id="stufe-9-3"></span>

Die Bisektion braucht nur das Vorzeichen von $f$ und das Startintervall $[0,R/K]$. Hier ist $f(\mathit{lo})<0$ wie bei der Wurzel, die Fälle in der Schleife stehen also wie dort: Ist die Restschuld beim Zins in der Mitte negativ, hätte man bei diesem Zins zu viel zurückgezahlt, und der gesuchte Zins liegt höher. Den Wert $f(\mathit{mitte})$ rechnet das Skript ohne Formel aus: Eine innere Schleife schreibt die Restschuld Monat für Monat nach der Regel $S_{k+1}=S_k\,q-R$ fort. Die beiden Schleifen sind verschachtelt wie in Unterabschnitt [5.3](schleifen-steuern-verschachteln-und-ergebnisse-sammeln.html#stufe-5-3).

```python kredit_bisektion.py
# Zinssatz eines Ratenkredits: Nullstelle der Restschuld f(r) durch Bisektion
kredit = 20000.0      # geliehener Betrag in Euro
monate = 60           # Laufzeit in Monaten
rate = 400.0          # Monatsrate in Euro
eps = 1e-12           # Breite des Intervalls für den Monatszins

lo = 0.0              # f(0) = kredit - monate * rate < 0
hi = rate / kredit    # f(hi) = kredit > 0: die Zinsen verbrauchen die ganze Rate
schritte = 0
while hi - lo > eps:
    mitte = (lo + hi) / 2
    f = kredit                    # Restschuld beim Zins mitte, Monat für Monat
    for monat in range(monate):
        f = f * (1 + mitte) - rate
    if f < 0:         # zu viel zurückgezahlt: der Zins liegt höher als mitte
        lo = mitte
    else:
        hi = mitte
    schritte = schritte + 1
zins = (lo + hi) / 2
print(f"Monatszins: {zins * 100:.4f} %, Schritte: {schritte}")
print(f"effektiver Jahreszins: {((1 + zins) ** 12 - 1) * 100:.2f} %")
```

```console Linux
$ python3 kredit_bisektion.py
Monatszins: 0.6183 %, Schritte: 35
effektiver Jahreszins: 7.68 %
```

Satz [7.3](die-bisektion.html#satz-7-3) sagt die Schrittzahl voraus: $\lceil\log_2(0{,}02/10^{-12})\rceil=\lceil34{,}2\rceil=35$. Die Bisektion braucht dafür weder die Ableitung noch einen guten Startwert, nur den Vorzeichenwechsel. Das Angebot des Autohauses entspricht einem Monatszins von 0,6183 % und einem effektiven Jahreszins von 7,68 %.

⁠**Kurz gesagt:** Die Bisektion findet den Monatszins 0,6183 % sicher in 35 Schritten.

### Der Zinssatz durch Newton

<span class="anker" id="stufe-9-4"></span>

Für das Newton-Verfahren braucht man die Ableitung $f'(r)$, und man bekommt sie aus derselben Schleife wie $f$. Aus $S_{k+1}=S_k\,(1+r)-R$ folgt mit der Produktregel $(u\,v)'=u'v+u\,v'$ aus der Schule

$$S'_0=0,\qquad S'_{k+1}=S'_k\,(1+r)+S_k ,$$

denn der Kreditbetrag $K$ und die Rate $R$ hängen nicht vom Zins ab, und $1+r$ hat nach $r$ die Ableitung 1. In Worten: Steigt der Zins ein wenig, kommt in jedem Monat der zusätzliche Zins auf die Restschuld $S_k$ hinzu, und was die Restschuld schon an Zuwachs mitbringt, wird mitverzinst. Am Ende ist $f'(r)=S'_n$. Im Skript muss die Zeile für die Ableitung vor der Zeile für die Restschuld stehen, denn sie braucht noch die Restschuld des Vormonats.

Das Skript stoppt, sobald ein Newton-Schritt den Zins um weniger als $10^{-12}$ ändert, und hat eine Notbremse nach 1000 Schritten. Den Startwert fragt es ab:

```python kredit_newton.py
# Zinssatz eines Ratenkredits: Nullstelle der Restschuld f(r) mit dem Newton-Verfahren
kredit = 20000.0      # geliehener Betrag in Euro
monate = 60           # Laufzeit in Monaten
rate = 400.0          # Monatsrate in Euro

zins = float(input("Startwert für den Monatszins: "))
schritt = 1.0         # Länge des letzten Newton-Schritts, zu Beginn beliebig groß
schritte = 0
while abs(schritt) > 1e-12 and schritte < 1000:
    f = kredit        # Restschuld bei diesem Zins, Monat für Monat
    f_strich = 0.0    # ihre Ableitung nach dem Zins
    for monat in range(monate):
        f_strich = f_strich * (1 + zins) + f    # zuerst, denn hier steht noch die alte Restschuld
        f = f * (1 + zins) - rate
    schritt = -f / f_strich
    zins = zins + schritt
    schritte = schritte + 1
print(f"Monatszins: {zins * 100:.4f} %, Schritte: {schritte}")
```

```console Linux
$ python3 kredit_newton.py
Startwert für den Monatszins: 0.01
Monatszins: 0.6183 %, Schritte: 5
$ python3 kredit_newton.py
Startwert für den Monatszins: 0
Monatszins: 0.6183 %, Schritte: 6
$ python3 kredit_newton.py
Startwert für den Monatszins: 1
Monatszins: 0.6183 %, Schritte: 47
```

Mit einem Startwert in der Nähe, 1 % im Monat, braucht Newton 5 Schritte, vom Startwert 0 aus 6. Wer aber `1` für 1 % eintippt, startet bei 100 % im Monat, und dann sind es 47 Schritte, mehr als bei der Bisektion. Der Grund ist der Zinseszins. Weit oberhalb der Lösung wächst die Restschuld fast nur noch durch ihn, ungefähr wie ein fester Betrag $c$ mal $q^n$. Für eine Funktion $c\,q^n$ ist $f/f'=c\,q^n/(c\,n\,q^{n-1})=q/n$, hier gilt das also ungefähr. Jeder Newton-Schritt senkt $q$ deshalb nur um etwa den $n$-ten Teil, hier wird $q$ mit etwa $59/60$ multipliziert. Von $q=2$ bis $q\approx1{,}006$ sind das $\ln(2/1{,}006)/\ln(60/59)\approx41$ Schritte, bevor die schnelle Phase beginnt.

Daraus folgt die übliche Arbeitsteilung: Man grenzt die Lösung mit einer sicheren Methode oder mit Vorwissen ein, für Ratenkredite etwa 0 % bis 2 % im Monat, und lässt dann Newton die letzten Stellen holen.

⁠**Kurz gesagt:** Nahe an der Lösung gestartet, braucht Newton 5 Schritte; weit weg kriecht es, weil $q$ in jedem Schritt nur um etwa den $n$-ten Teil sinkt, und ist dann langsamer als die Bisektion.

:::hintergrund Wie fertige Löser das Newton-Verfahren absichern
Das Kriechen hier und der Kreislauf in Unterabschnitt [8.5](das-newton-verfahren.html#stufe-8-5) haben dieselbe Ursache: Weit weg von der Nullstelle beschreibt die Tangente die Funktion schlecht, und ihr Schritt ist zu kurz oder zu lang. Fertige Löser sichern das Verfahren deshalb ab. Zwei Arten sind verbreitet.

Die erste ist ein Sicherheitsnetz aus der Bisektion. Der Löser hält wie die Bisektion ein Intervall mit Vorzeichenwechsel fest und probiert in jedem Schritt zuerst den Newton-Schritt. Landet dieser außerhalb des Intervalls oder verkleinert er es zu wenig, nimmt der Löser stattdessen die Mitte. Am neuen Punkt bestimmt er das Vorzeichen von $f$ und ersetzt damit eine Grenze, wie in der Bisektion. So bleibt jeder Schritt im Intervall, ein kriechender Newton-Schritt wird durch einen Halbierungsschritt ersetzt, und nahe der Nullstelle, wo die Newton-Schritte gut sind, ist der Löser so schnell wie Newton.

Die zweite ist die Dämpfung. Sie hilft auch dort, wo es kein Intervall gibt, etwa wenn viele Gleichungen zugleich gelöst werden. Der Löser nimmt den Newton-Schritt $\Delta=-f(g)/f'(g)$ nur dann ganz, wenn $|f|$ danach kleiner ist als vorher; sonst halbiert er den Schritt, bis es so ist. Das gelingt immer, solange $f(g)\ne0$ und $f'(g)\ne0$ ist: Für einen Bruchteil $\lambda$ des Schritts ist nach der Tangente $f(g+\lambda\Delta)\approx f(g)+\lambda f'(g)\,\Delta=(1-\lambda)\,f(g)$, und für kleine $\lambda$ ist der Fehler dieser Näherung klein gegen $\lambda\,|f(g)|$. Ein kurzer Schritt in Richtung der Tangente verkleinert $|f|$ also stets. Nahe der Nullstelle wird der volle Schritt angenommen, und das Verfahren behält seine Geschwindigkeit.
:::

### Aufgaben zu Abschnitt [9](#stufe-9)

<span class="anker" id="stufe-9-5"></span>

:::aufgabe Aufgabe 34 ★★★ Ein anderer Kredit
<span class="anker" id="aufg-34"></span>

Ein Fernseher kostet 1000 Euro, alternativ 24 Monatsraten zu 45 Euro.

<ol class="al">

<li>

Sage mit Satz [7.3](die-bisektion.html#satz-7-3) voraus, wie viele Schritte die Bisektion mit $\varepsilon=10^{-9}$ braucht. Bestimme dann den Monatszins und den effektiven Jahreszins mit der Bisektion.

</li>

<li>

Bestimme den Monatszins mit Newton, einmal vom Startwert 0,01 und einmal vom Startwert 1. Schätze die zweite Schrittzahl vorher ab.

</li>

<li>

Rechne den Monatszins auch ohne Zinseszins auf ein Jahr um, also mal 12, und vergleiche mit dem effektiven Jahreszins. Warum ist der effektive Jahreszins größer?

</li>

</ol>

:::loesung
(a) Das Startintervall ist $[0,R/K]=[0;\,0{,}045]$, also $\lceil\log_2(0{,}045/10^{-9})\rceil=\lceil25{,}4\rceil=26$. Das Skript ist `kredit_bisektion.py` mit den neuen Werten und `eps = 1e-9`:

```console Linux
$ python3 fernseher_bisektion.py
Monatszins: 0.6251 %, Schritte: 26
effektiver Jahreszins: 7.76 %
```

(b) Vom Startwert 1 aus, also mit $q=2$, sinkt $q$ in jedem Schritt nur um etwa den 24. Teil. Bis $q\approx1{,}006$ sind das etwa $\ln(2/1{,}006)/\ln(24/23)\approx16$ Schritte, dazu einige für die letzten Stellen. Das Skript `fernseher_newton.py` ist `kredit_newton.py` mit den neuen Werten:

```console Linux
$ python3 fernseher_newton.py
Startwert für den Monatszins: 0.01
Monatszins: 0.6251 %, Schritte: 5
$ python3 fernseher_newton.py
Startwert für den Monatszins: 1
Monatszins: 0.6251 %, Schritte: 22
```

Das Kriechen ist kürzer als beim Auto mit 60 Raten, weil $q$ hier in jedem Schritt um den 24. Teil sinkt statt um den 60.

(c) Ohne Zinseszins ergibt sich $12\cdot0{,}6251\,\%=7{,}50\,\%$, mit Zinseszins der effektive Jahreszins von 7,76 %. Der Unterschied kommt daher, dass die Zinsen eines Monats zur Restschuld gehören und in den folgenden Monaten selbst verzinst werden. Ausmultipliziert ist $(1+r)^{12}=1+12\,r+66\,r^2+\cdots$; schon der Summand $66\,r^2=66\cdot0{,}006251^2\approx0{,}0026$ macht etwa 0,26 Prozentpunkte aus.
:::
:::

:::aufgabe Aufgabe 35 ★★ Wenn Newton bei `nan` landet
<span class="anker" id="aufg-35"></span>

Ein Baukredit über 200 000 Euro wird in 30 Jahren, also in 360 Monatsraten zu 1000 Euro, zurückgezahlt. Jemand denkt an „etwa 10 Prozent“ und gibt in `kredit_newton.py` mit diesen Zahlen den Startwert 10 ein. Was passiert, und warum endet die Schleife trotzdem? Läuft die Bisektion mit diesen Zahlen? Begründe mit dem Startintervall und rechne nach. Bestimme den Zins dann mit Newton von einem vernünftigen Startwert aus.

:::loesung
Das Skript `baukredit_newton.py` ist `kredit_newton.py` mit den neuen Werten:

```console Linux
$ python3 baukredit_newton.py
Startwert für den Monatszins: 10
Monatszins: nan %, Schritte: 1
```

Mit $r=10$, also 1000 % im Monat, ist $q=11$. Die innere Schleife multipliziert die Restschuld 360-mal mit 11, und $11^{360}\approx10^{375}$ liegt weit über dem größten `float` von etwa $1{,}8\cdot10^{308}$. Restschuld und Ableitung werden zu `inf` ([Kapitel 2, Abschnitt 5.5](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-5)), und $\infty/\infty$ ergibt `nan` ([Kapitel 2, Abschnitt 5.6](/wissen/informatik/programmieren/python/werte-typen-und-variablen/rechnen-mit-gleitkommazahlen.html#stufe-5-6)). Damit sind der Schritt und der neue Zins `nan`. Die Schleife endet trotzdem, denn jeder Vergleich mit `nan` außer `!=` ergibt `False`; [Kapitel 2, Abschnitt 7.3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/wahrheitswerte-und-vergleiche.html#stufe-7-3) hat das an `nan == nan` gezeigt. Hier trifft es den Vergleich in der Bedingung:

```console
>>> nan = 1e309 - 1e309
>>> abs(nan) > 1e-12
False
```

Die Bedingung `abs(schritt) > 1e-12` ist also falsch, und das Skript meldet nach einem Schritt ohne Fehlermeldung `nan`.

Die Bisektion läuft. Ihr Startintervall ist $[0,R/K]=[0;\,0{,}005]$, und sie rechnet $f$ nur in Mitten dieses Intervalls aus. Dort ist $q^{360}\le1{,}005^{360}\approx6{,}0$, ein Überlauf ist ausgeschlossen:

```console Linux
$ python3 baukredit_bisektion.py
Monatszins: 0.3656 %, Schritte: 33
effektiver Jahreszins: 4.48 %
```

Die Schrittzahl ist $\lceil\log_2(0{,}005/10^{-12})\rceil=\lceil32{,}2\rceil=33$. Newton mit einem vernünftigen Startwert, etwa der oberen Grenze 0,005, kommt zum selben Ergebnis:

```console Linux
$ python3 baukredit_newton.py
Startwert für den Monatszins: 0.005
Monatszins: 0.3656 %, Schritte: 6
```

10 % wären als Dezimalzahl 0,1; der Startwert 10 bedeutet dagegen 1000 % im Monat. Ein Programm für andere Leute sollte solche Eingaben vorher prüfen, etwa mit einer Bedingung wie in Abschnitt [2](entscheidungen-if-elif-und-else.html#stufe-2).
:::
:::
