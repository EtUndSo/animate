---
title: Die Kirchhoffschen Gesetze
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50500
summary: Von Grund auf – die zwei Bilanzregeln, mit denen sich jedes Netzwerk berechnen lässt: Was in einen Knoten hineinfließt, fließt hinaus, und auf jeder Masche summieren sich die Spannungen zu null. Leitbild ist das Wegenetz aus dem vorigen Artikel, jetzt mit Zählstellen an den Kreuzungen und Höhenangaben an den Wegen. Mit Knotenregel aus der Ladungserhaltung, Vorzeichen bei Zählpfeilen, der überzähligen Knotengleichung, Maschenregel aus der Wegunabhängigkeit, der Vorzeichenregel beim Umlauf, den unabhängigen Maschengleichungen, dem vollständigen Rechenrezept an zwei Netzen samt Leistungsbilanz und den Grenzen der Regeln. Mit Beispiel-Seite.
tags: Kirchhoff, Knotenregel, Maschenregel, Netzwerkanalyse, Ladungserhaltung, Energieerhaltung
---

## Anschaulich

Mit den Begriffen Knoten, Zweig und Masche aus dem vorigen Artikel lässt sich jetzt sagen, was in einem Netzwerk gelten muss. Es sind nur zwei Regeln,
benannt nach Gustav Robert Kirchhoff, und beide sind Bilanzen: eine für die Ströme an jedem Knoten, eine für die Spannungen auf jeder Masche. Zusammen
mit den Bauteilgleichungen, etwa dem Ohmschen Gesetz, bestimmen sie jeden Strom und jede Spannung.

**Das Leitbild dieses Artikels:** **das Wegenetz aus dem vorigen Artikel**, jetzt mit zwei Messgeräten. An jeder Kreuzung steht eine Zählstelle, die
zählt, wie viele Wanderer pro Stunde auf jedem Weg ankommen und weggehen. Und an jedem Wegstück steht, wie viele Höhenmeter man auf ihm gewinnt oder
verliert — die Höhe ist wie im Artikel über das Potenzial das Potenzial, ein Höhenunterschied eine Spannung.

Zwei Regeln kann man dem Wegenetz direkt ansehen:

- **Die Kreuzungsregel.** Niemand bleibt an einer Kreuzung stehen und niemand taucht dort aus dem Nichts auf. Pro Stunde gehen also genau so viele
  Wanderer weg, wie ankommen. Das ist die __Knotenregel__.
- **Die Rundwegregel.** Wer eine Runde läuft, steht am Ende wieder am Ausgangspunkt, auf derselben Höhe. Alle Anstiege und Abstiege der Runde heben sich
  auf. Das ist die __Maschenregel__.

Zwei Folgerungen gleich dazu: Stimmt die Bilanz an allen Kreuzungen bis auf eine, stimmt sie auch an der letzten — wer das Netz irgendwo betritt, verlässt
es irgendwo. Und eine große Runde, die sich aus zwei kleinen zusammensetzt, liefert keine neue Höhenbilanz. Beides bestimmt, wie viele Gleichungen man
wirklich aufstellen muss.

Das Bild hinkt an einer Stelle: Wanderer können an einer Kreuzung Rast machen, Ladung kann sich an einem Knoten nicht sammeln. Die Kreuzungsregel gilt für
Wanderer nur im Mittel, die Knotenregel in jedem Augenblick.

:::grafik
Szene: get1/stroeme-und-spannungen/05-wegenetz-bilanzen · Vorlage: zaehlstelle-hoehenmesser
Das Wegenetz des vorigen Artikels mit vier Kreuzungen und sechs Wegstücken, jetzt in Seitenansicht als Relief: Die Kreuzungen liegen auf verschiedenen
Höhen. An jeder Kreuzung eine Zählstelle mit zwei Zählern „kommen" und „gehen", die bei laufenden Wanderern stets gleich schnell hochzählen. Ein Klick auf
einen Rundweg schickt eine Wanderfigur los; ein Höhenmesser summiert Anstiege positiv und Abstiege negativ und steht am Ende der Runde wieder auf null.
Danach blendet ein Regler das Relief in die Schaltung um: Kreuzungen werden Knoten, die Zähler zeigen Ströme in Milliampere, der Höhenmesser Spannungen
in Volt. Kernaussage: An jedem Knoten gleicht sich der Strom aus, auf jeder Masche die Spannung. (Rot = Knoten und Zählstellen, blau = Wege und Ströme,
orange = Höhenmesser und Spannungen, grau = Relief.)
:::

## Die Knotenregel

**Die Akteure:**

- ein __Knoten__ $K$, an dem $n$ Zweige zusammentreffen;
- die Zweigströme $I_1, \dots, I_n$ in Ampere, jeder mit seinem Zählpfeil, der zum Knoten hin oder vom Knoten weg zeigt.

**Das Zusammenspiel:** *Was muss für die Ströme gelten, wenn sich am Knoten keine Ladung sammeln kann?*

:::formel Satz
$$\sum_{\nu=1}^{n} I_\nu = 0 \quad \text{(Pfeile zum Knoten)}, \qquad \sum I_\text{zu} = \sum I_\text{ab}.$$
:::

**So liest man das:** Zeigen alle Zählpfeile zum Knoten hin, ist die Summe der Ströme null, in jedem Augenblick. Zeigen einige
Pfeile weg, zählt man diese mit Minus — oder, gleichwertig, setzt die Summe der zufließenden gleich der Summe der abfließenden Ströme. Eingabe sind die Zweigströme mit ihren Vorzeichen, Ausgabe eine Gleichung, die sie verbindet.

**Im Bild:** Die Zählstelle an der Kreuzung. Wer ankommt, geht weiter; pro Stunde gleich viele hin wie weg.

:::herleitung
**Die Ladung am Knoten.** Man denkt sich eine kleine Hülle um den Knoten. Nach dem Artikel über den Strom bringt ein Zweigstrom in der Zeit $dt$ die
Ladung $I\,dt$ durch seinen Querschnitt. Die Ladung $Q_K$ in der Hülle ändert sich deshalb um alles Zufließende minus alles Abfließende:

$$\frac{dQ_K}{dt} = \sum I_\text{zu} - \sum I_\text{ab}.$$

**Kein Speicher.** Ein Knoten ist eine ideale Verbindung ohne eigenes Speichervermögen: Ladung kann dort weder entstehen noch verschwinden
(Ladungserhaltung), und sie kann sich nicht ansammeln — das tut sie nur in Bauteilen wie einem Kondensator, und der sitzt in einem Zweig, nicht im Knoten.
Also bleibt $Q_K$ konstant, die linke Seite ist null, und Zufluss gleich Abfluss.

**Alle Pfeile zum Knoten.** Zeigt der Pfeil eines abfließenden Stroms stattdessen zum Knoten hin, zählt er denselben Strom mit umgekehrtem Vorzeichen
(Artikel über Zählpfeile). Bringt man so alle Ströme auf die Zuflussseite, steht dort ihre Summe, und sie ist null.
:::

**Vorzeichen.** Zeichnet man an einem Knoten mit fünf Zweigen alle fünf Ströme zum Knoten hin, können nicht alle positiv sein, denn ihre Summe ist null:
Mindestens einer ist negativ und fließt in Wirklichkeit ab. Man darf alle Ströme als zufließend oder alle als abfließend annehmen, muss dann aber mit
negativen Zahlenwerten rechnen.

**Im Bild:** Zählt man an einer Kreuzung jeden Weg als „ankommend", zeigen die Wege, auf denen in Wirklichkeit Leute weggehen, negative Zahlen.

::::beispiel Die Abzweigdose
In eine Abzweigdose fließen über die Zuleitung $10\,\text{A}$; abgehen ein Strang mit $4\,\text{A}$, einer mit $2{,}5\,\text{A}$ und ein dritter mit
unbekanntem Strom. Zufluss gleich Abfluss:

$$10\,\text{A} = 4\,\text{A} + 2{,}5\,\text{A} + I_3, \qquad I_3 = 3{,}5\,\text{A}.$$

**Alle Pfeile zur Dose hin gezeichnet:** Dann zählen die abgehenden Ströme negativ,

$$I_1 = 10\,\text{A}, \qquad I_2 = -4\,\text{A}, \qquad I_3 = -2{,}5\,\text{A}, \qquad I_4 = -3{,}5\,\text{A},$$

und ihre Summe ist null.

**Im Bild:** Eine Kreuzung, an der zehn Wanderer pro Stunde ankommen und sich auf drei Wege verteilen. Wer alle Wege als „ankommend" zählt, notiert auf drei
davon Minuszeichen.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/05-knoten · Vorlage: knoten-bilanz
Ein Knoten mit fünf Zweigen, in denen kleine Ladungspunkte strömen. Jeder Zweig hat einen umdrehbaren Zählpfeil und eine Anzeige
mit Vorzeichen. Anfangs zeigen alle Pfeile zum Knoten hin; die Anzeigen lauten zum Beispiel $+3$, $+1$, $-2$, $-1{,}5$ und $-0{,}5\,\text{A}$, ein Summenbalken
steht bei null. Dreht man einen Pfeil um, wechselt nur seine Anzeige das Vorzeichen, und die Bilanz „zu = ab" ordnet den Strom auf die andere Seite.
Eine kleine Hülle um den Knoten zeigt eine Ladungsanzeige, die stets bei null bleibt. Kernaussage: Am Knoten sammelt sich nichts; die Ströme gleichen
sich in jedem Augenblick aus. (Rot = Knoten und Hülle, blau = Zweige und Ladungen, orange = Anzeigen und Summenbalken, grau = Zählpfeile.)
:::

## Wie viele Knotengleichungen nötig sind

Stellt man für die Brückenschaltung aus dem vorigen Artikel die vier Knotengleichungen auf, an den Knoten $K_1$ bis $K_4$, zeigt sich: Die Summe der
Gleichungen an $K_1$, $K_2$ und $K_3$ ist die negative Gleichung an $K_4$. Die vierte Gleichung bringt also nichts Neues. Allgemein gilt:

:::formel Satz
$$N_\text{K} = k - 1.$$
:::

**So liest man das:** $N_\text{K}$ ist die Zahl der unabhängigen Knotengleichungen in einem zusammenhängenden Netz mit $k$ Knoten. Man stellt die
Knotenregel an allen Knoten bis auf einen auf; welchen man weglässt, ist gleich, seine Gleichung folgt aus den anderen. Der weggelassene heißt oft
__Bezugsknoten__ und ist meist die Masse.

**Im Bild:** Wenn an allen Kreuzungen bis auf eine die Zählungen aufgehen, geht auch die letzte auf: Wer das Netz betritt, verlässt es irgendwo wieder.

:::herleitung
**Die Summe ist null gleich null.** Jeder Zweig verbindet genau zwei Knoten. Schreibt man an jedem Knoten die Ströme mit Pfeil zum Knoten positiv und die
mit Pfeil weg negativ, steht jeder Zweigstrom in genau zwei Gleichungen, einmal mit Plus, einmal mit Minus. Addiert man alle $k$ Gleichungen, heben sich
alle Ströme auf. Eine Gleichung ist deshalb stets die negative Summe der übrigen.

**Die übrigen sind unabhängig.** Das zeigt der Artikel über topologische Grundbegriffe: Ergäbe eine Kombination der Gleichungen ohne den Bezugsknoten null
gleich null, müssten benachbarte Knoten denselben Faktor haben, und weil das Netz zusammenhängt, wären alle Faktoren gleich dem des Bezugsknotens, also
null.
:::

::::beispiel Die Knoten der Leiterschaltung
Die Leiterschaltung aus dem vorigen Artikel, mit jedem Verbindungspunkt als Knoten: Zweig $1$ ist die Quelle von D nach A, Zweig $2$ führt über $R_1$ von
A nach B, Zweig $3$ über $R_2$ von B nach D, Zweig $4$ über $R_3$ von B nach C und Zweig $5$ über $R_4$ von C nach D. Die Ströme mit diesen Pfeilen, zum
Knoten hin positiv:

$$\text{A:}\ \ I_1 - I_2 = 0, \qquad \text{B:}\ \ I_2 - I_3 - I_4 = 0,$$

$$\text{C:}\ \ I_4 - I_5 = 0, \qquad \text{D:}\ \ I_3 + I_5 - I_1 = 0.$$

Die Summe aller vier ergibt null gleich null; die Gleichung an D ist die negative Summe der anderen drei. Mit den Werten, die das Rechenrezept weiter unten
liefert,

$$I_1 = I_2 = 5\,\text{mA}, \qquad I_3 = I_4 = I_5 = 2{,}5\,\text{mA},$$

sind alle vier erfüllt.

**Im Bild:** Vier Zählstellen; die vierte bestätigt nur, was die drei anderen schon sagen.
::::

## Die Maschenregel

**Die Akteure:**

- eine __Masche__ aus $n$ Zweigen, die nacheinander die Knoten $P_1, P_2, \dots, P_n$ besucht und zu $P_1$ zurückkehrt;
- die Zweigspannungen $U_1, \dots, U_n$ in Volt, jede mit ihrem Zählpfeil;
- ein frei gewählter __Umlaufsinn__, die Richtung, in der man die Masche abläuft.

**Das Zusammenspiel:** *Was folgt daraus, dass man nach einem Umlauf wieder am Ausgangspunkt steht?*

:::formel Satz
$$\sum_{\nu=1}^{n} U_\nu = 0,$$

jede Spannung mit Plus, wenn ihr Pfeil in Umlaufrichtung zeigt, und mit Minus, wenn er dagegen zeigt.
:::

**So liest man das:** Die vorzeichenrichtige Summe aller Zweigspannungen einer Masche ist null, gleich in welchem Umlaufsinn man
läuft; der andere Umlaufsinn dreht nur alle Vorzeichen um. Eingabe sind die Zweigspannungen mit ihren Pfeilen, Ausgabe eine Gleichung zwischen ihnen.

**Im Bild:** Der Höhenmesser auf einem Rundweg. Anstiege zählen plus, Abstiege minus, und am Ende der Runde steht er wieder auf null.

:::herleitung
**Spannung als Potenzialdifferenz.** Nach dem Artikel über Zählpfeile ist eine Spannung längs ihres Pfeils das Potenzial am Pfeilanfang minus das an der
Pfeilspitze. Läuft man in Umlaufrichtung von $P_\nu$ nach $P_{\nu+1}$, trägt ein Pfeil in Umlaufrichtung also $\varphi(P_\nu)-\varphi(P_{\nu+1})$ bei. Ein
Pfeil gegen die Umlaufrichtung misst die umgekehrte Differenz; damit die Summe dieselbe Differenz in Umlaufrichtung enthält, bekommt er ein Minus.

**Die Summe fällt zusammen.** Mit $P_{n+1}$ gleich $P_1$, dem Ausgangspunkt, heben sich die Potenziale aller Zwischenpunkte paarweise weg:

$$\sum_{\nu=1}^{n}\big(\varphi(P_\nu)-\varphi(P_{\nu+1})\big) = \varphi(P_1)-\varphi(P_{n+1}) = 0.$$

**Mit dem Feld.** Dasselbe lässt sich über das Feld schreiben: Die Spannung zwischen zwei Punkten ist wegunabhängig, und das Wegintegral des Felds um einen
geschlossenen Weg ist null,

$$U_{21} = \varphi(P_2)-\varphi(P_1) = -\int_{P_1}^{P_2}\vec E\cdot d\vec s, \qquad \oint_L \vec E\cdot d\vec s = 0.$$

Als Energie gelesen: Trägt man eine Ladung $Q$ einmal um die Masche, verrichtet das Feld an ihr insgesamt die Arbeit $Q$ mal null — auf einer Runde
gewinnt oder verliert sie keine Energie.
:::

Ein Beispiel: Zwei Widerstände $R_1$, $R_2$ hintereinander liegen parallel zu $R_3$ zwischen den Potenzialen $\varphi_1$ oben und
$\varphi_2$ unten, alle drei Spannungspfeile zeigen nach unten. Der Umlauf läuft gegen den Uhrzeigersinn, links hinunter und rechts hinauf. $U_1$ und $U_2$
zeigen in Umlaufrichtung, $U_3$ dagegen, und es folgt

$$U_1 + U_2 - U_3 = 0, \qquad U_3 = \varphi_1 - \varphi_2.$$

**Im Bild:** Zwei Wege von derselben oberen zur selben unteren Kreuzung, links über einen Zwischenpunkt, rechts direkt. Beide verlieren dieselben
Höhenmeter.

::::beispiel Ein Umlauf mit vier Spannungen
Ein Kreis aus einer Quelle und drei Widerständen; der Umlauf läuft im Uhrzeigersinn. Die Quellenspannung von $24\,\text{V}$ zeigt gegen den Umlauf, die
Spannungen $U_1$ von $6\,\text{V}$ und $U_2$ von $10\,\text{V}$ zeigen in Umlaufrichtung, der Pfeil von $U_3$ ist gegen den Umlauf gezeichnet. Die Maschenregel:

$$-24\,\text{V} + 6\,\text{V} + 10\,\text{V} - U_3 = 0, \qquad U_3 = -8\,\text{V}.$$

Das Minus heißt: Der Pfeil von $U_3$ zeigt gegen die tatsächliche Richtung; in Umlaufrichtung fallen am dritten Widerstand $8\,\text{V}$ ab, wie an den
beiden anderen. Die Probe in Umlaufrichtung gelesen: Die Quelle hebt um $24\,\text{V}$, die drei Widerstände senken um $6$, $10$ und $8\,\text{V}$,
zusammen ebenfalls um $24\,\text{V}$.

**Im Bild:** Ein Anstieg von $24$ Höhenmetern und drei Abstiege von $6$, $10$ und $8$ — einer davon war auf der Tafel falsch herum beschriftet.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/05-masche · Vorlage: maschenumlauf
Eine Masche: oben das Potenzial $\varphi_1$, unten $\varphi_2$; links $R_1$ und $R_2$ hintereinander mit
Spannungspfeilen $U_1$ und $U_2$ nach unten, rechts $R_3$ mit $U_3$ nach unten. Ein blauer Umlaufpfeil läuft gegen den Uhrzeigersinn. Eine Wanderfigur
startet oben links, geht hinunter und rechts wieder hinauf; bei jedem Bauteil leuchtet dessen Spannung auf, grün mit Plus, wenn der Pfeil in Laufrichtung
zeigt, rot mit Minus, wenn dagegen. Ein Balken summiert mit und steht am Ziel bei null. Ein Schalter kehrt den Umlaufsinn um: Alle Vorzeichen wechseln, die
Summe bleibt null. Kernaussage: Auf jeder Masche summieren sich die Spannungen mit Vorzeichen zu null, weil man zum Ausgangspotenzial zurückkehrt. (Rot =
Zählpfeile, blau = Umlaufsinn, orange = Summenbalken, grau = Bauteile.)
:::

## Wie viele Maschengleichungen nötig sind

Für die Brückenschaltung aus dem vorigen Artikel lassen sich vier Maschengleichungen aufstellen, $M_1$ bis $M_4$. Unabhängig sind aber nur drei; die
vierte ist eine Kombination der anderen:

$$M_4 = M_2 - M_1 - M_3.$$

Allgemein gilt, mit dem Satz über unabhängige Maschen aus dem vorigen Artikel:

:::formel Satz
$$N_\text{M} = z - k + 1.$$
:::

**So liest man das:** $N_\text{M}$ ist die Zahl der unabhängigen Maschengleichungen eines zusammenhängenden Netzes mit $z$ Zweigen und $k$ Knoten. Stellt
man die Maschenregel für so viele unabhängige Maschen auf, etwa die Maschen der Verbindungszweige eines Baums, sind die Gleichungen aller anderen Maschen
von selbst erfüllt.

**Im Bild:** Wer die Höhenbilanz auf allen unabhängigen Rundwegen geprüft hat, braucht keine weitere Runde mehr nachzumessen.

:::herleitung
**Die Gleichung einer Masche.** Zählt man jede Zweigspannung in Richtung ihres Zweigs, also im VZS zum Zweigstrom, dann zeigt ihr Pfeil in Umlaufrichtung
genau dann, wenn die Masche den Zweig in seiner Richtung durchläuft. Mit dem Maschenvektor $\vec c$ aus dem vorigen Artikel lautet die Maschenregel
deshalb:

$$\sum_{j=1}^{z} c_j\,U_j = 0.$$

**Kombinationen.** Ist eine Masche eine Kombination anderer, mit denselben Faktoren für die Maschenvektoren, dann ist auch ihre Gleichung dieselbe
Kombination der anderen Gleichungen, denn die linke Seite hängt linear von $\vec c$ ab. Eine abhängige Masche bringt keine neue Gleichung.

**Die Zahl.** Nach dem vorigen Artikel gibt es genau $z-k+1$ unabhängige Maschen, also ebenso viele unabhängige Maschengleichungen. In der Brücke prüft man
die Kombination direkt: Die rechte Seite $M_2-M_1-M_3$ ergibt mit den Maschengleichungen der Brücke

$$(U_2+U_4+U_5) - (U_1+U_3+U_5) - (-U_0-U_1+U_2) = U_0 - U_3 + U_4,$$

die linke Seite von $M_4$.
:::

::::beispiel Zwei Quellen an einer Last
Zwei Knoten, oben N1 und unten N2, und drei Zweige zwischen ihnen. Links eine Quelle von $12\,\text{V}$ mit $1\,\Omega$ in Reihe, rechts eine Quelle von
$9\,\text{V}$ mit $1\,\Omega$ in Reihe, beide mit dem Pluspol oben; in der Mitte eine Last von $4\,\Omega$. Zählpfeile: $I_1$ und $I_2$ in den beiden
Quellenzweigen nach oben, $I_3$ durch die Last nach unten; die Widerstandsspannungen im VZS dazu, die Quellenspannungen von Plus nach Minus, also nach
unten.

**Wie viele Gleichungen?** Mit zwei Knoten und drei Zweigen:

$$N_\text{K} = 2 - 1 = 1, \qquad N_\text{M} = 3 - 2 + 1 = 2.$$

**Die Gleichungen.** Knoten N1, Zufluss gleich Abfluss; dann die beiden Fenster im Uhrzeigersinn, links (hinauf durch die linke Quelle, hinunter durch die
Last) und rechts (hinauf durch die Last, hinunter durch die rechte Quelle):

$$I_1 + I_2 = I_3,$$

$$-12\,\text{V} + 1\,\Omega\cdot I_1 + 4\,\Omega\cdot I_3 = 0, \qquad -4\,\Omega\cdot I_3 - 1\,\Omega\cdot I_2 + 9\,\text{V} = 0.$$

Die äußere Runde durch beide Quellen ist die Summe der beiden Fenster, dort hebt sich die Last heraus:

$$-12\,\text{V} + 1\,\Omega\cdot I_1 - 1\,\Omega\cdot I_2 + 9\,\text{V} = 0.$$

**Lösen.** Aus den Fenstergleichungen folgen $I_1$ und $I_2$ in Abhängigkeit von $I_3$; in die Knotengleichung eingesetzt:

$$I_1 = 12\,\text{A} - 4\,I_3, \qquad I_2 = 9\,\text{A} - 4\,I_3, \qquad 21\,\text{A} - 8\,I_3 = I_3,$$

$$I_3 = \tfrac{7}{3}\,\text{A} \approx 2{,}33\,\text{A}, \qquad I_1 = \tfrac{8}{3}\,\text{A} \approx 2{,}67\,\text{A}, \qquad I_2 = -\tfrac{1}{3}\,\text{A} \approx -0{,}33\,\text{A}.$$

**Das Minus.** $I_2$ fließt in Wirklichkeit nach unten, in den Pluspol der $9$-V-Quelle hinein: Die stärkere Quelle lädt die schwächere. Die Last liegt an

$$U_\text{Last} = 4\,\Omega\cdot\tfrac{7}{3}\,\text{A} \approx 9{,}33\,\text{V},$$

mehr als die $9\,\text{V}$ der rechten Quelle; darum fließt Strom in sie hinein.

**Leistungsbilanz.** Abgegeben im GZS, aufgenommen im VZS:

$$P_\text{ab,1} = 12\,\text{V}\cdot\tfrac83\,\text{A} = 32\,\text{W}, \qquad P_\text{ab,2} = 9\,\text{V}\cdot\big(-\tfrac13\,\text{A}\big) = -3\,\text{W},$$

$$1\,\Omega\cdot\big(\tfrac83\,\text{A}\big)^2 + 1\,\Omega\cdot\big(\tfrac13\,\text{A}\big)^2 + 4\,\Omega\cdot\big(\tfrac73\,\text{A}\big)^2 \approx 7{,}11\,\text{W} + 0{,}11\,\text{W} + 21{,}78\,\text{W} = 29\,\text{W}.$$

Die linke Quelle gibt $32\,\text{W}$ ab; davon gehen $29\,\text{W}$ in die drei Widerstände und $3\,\text{W}$ in die rechte Quelle.

**Im Bild:** Zwei Lifte heben Wanderer auf verschiedene Höhen und münden an derselben Kreuzung. Der höhere drückt so viele herüber, dass der niedrigere
rückwärts fahren muss.
::::

## Das Rechenrezept

Mit beiden Regeln und den Abzählsätzen lässt sich jedes Netz direkt berechnen, mit den Zweigströmen als Unbekannten; das Verfahren heißt oft
__Zweigstromanalyse__.

- **Schritt 1:** Für jeden Zweig einen Zählpfeil des Stroms festlegen, die Widerstandsspannungen im VZS dazu, die Quellenspannungen von Plus nach Minus.
- **Schritt 2:** Die Knotenregel an $k-1$ Knoten aufstellen.
- **Schritt 3:** Einen Baum wählen und für die $z-k+1$ Maschen seiner Verbindungszweige, je mit einem Umlaufsinn, die Maschenregel aufstellen.
- **Schritt 4:** In die Maschengleichungen die Zweiggleichungen einsetzen, im VZS das Ohmsche Gesetz in der Form $U=R\,I$.
- **Schritt 5:** Das Gleichungssystem lösen, die Vorzeichen deuten und mit einer Leistungsbilanz prüfen.

Nach Schritt 4 sind nur noch die $z$ Zweigströme unbekannt, und es stehen genau so viele Gleichungen da:

$$(k - 1) + (z - k + 1) = z.$$

**Im Bild:** Erst jedes Wegstück mit einem Zählpfeil versehen, dann die Kreuzungsbilanzen und die Höhenbilanzen der unabhängigen Runden aufschreiben, und
an jedem Wegstück, wie Gefälle und Andrang zusammenhängen.

:::herleitung
**Die Zahl.** Nach Schritt 1 hat jeder Zweig einen Strom und eine Spannung, zusammen $2z$ Unbekannte. Schritt 4 drückt jede Zweigspannung durch den
Zweigstrom aus (Widerstand) oder legt sie fest (Quelle); es bleiben $z$ Unbekannte. Die Knotenregel liefert $k-1$ unabhängige Gleichungen, die
Maschenregel $z-k+1$.

**Die Leistungsbilanz.** Zählt man in jedem Zweig $j$ Strom und Spannung im VZS, ist die Summe aller aufgenommenen Leistungen null. Jede Zweigspannung
ist die Potenzialdifferenz ihrer beiden Knoten, Anfangsknoten minus Endknoten — darauf beruht die Maschenregel. Sortiert man die Summe nach Knoten um,
steht bei jedem Knoten $K$ sein Potenzial mal der Summe der Ströme, die ihn verlassen, minus derer, die ihn erreichen:

$$\sum_{j=1}^{z} U_j\,I_j = \sum_{K} \varphi_K\Big(\sum I_\text{ab} - \sum I_\text{zu}\Big) = 0.$$

Jede Klammer ist nach der Knotenregel null. Das ist der __Satz von Tellegen__, und deshalb muss die Probe in Schritt 5 aufgehen.

**Eindeutig.** Hätte ein Netz aus Widerständen und Spannungsquellen zwei Lösungen, erfüllte ihre Differenz wieder beide Regeln, aber mit allen
Quellenspannungen null. Die Leistungsbilanz der Differenz lautet dann

$$\sum_{\text{Widerstände}} R_j\,I_j^2 = 0,$$

und weil alle Glieder positiv oder null sind, sind alle Widerstandsströme der Differenz null. Bleiben nur Ströme durch Quellenzweige; solange keine
Masche allein aus idealen Spannungsquellen besteht, bilden diese keinen Kreis, und die Knotenregel zwingt auch sie auf null — wie an einem Blatt im
Artikel über topologische Grundbegriffe. Die Lösung ist also eindeutig.
:::

::::beispiel Die Leiterschaltung, ganz durchgerechnet
Die Leiterschaltung aus dem vorigen Artikel, jetzt mit Werten:

$$U_\text{q} = 10\,\text{V}, \qquad R_1 = 1\,\text{k}\Omega, \qquad R_2 = 2\,\text{k}\Omega, \qquad R_3 = R_4 = 1\,\text{k}\Omega.$$

**Schritt 1.** Nur mit den Verzweigungen als Knoten gezählt hat das Netz die Knoten B und D und drei Zweige: $I_a$ durch Quelle und $R_1$ von D nach B, $I_b$ durch $R_2$ von B
nach D, $I_c$ durch $R_3$ und $R_4$ von B über C nach D.

**Schritt 2.** Eine Knotengleichung, an B:

$$I_a = I_b + I_c.$$

**Schritt 3 und 4.** Ein Baum aus dem Zweig $I_b$ allein verbindet B und D; die beiden Verbindungszweige ergeben das linke und das rechte Fenster, beide im
Uhrzeigersinn. Links zeigt die Quellenspannung gegen den Umlauf, $R_1$ und $R_2$ in Umlaufrichtung; rechts zeigen $R_3$ und $R_4$ in Umlaufrichtung und $R_2$
dagegen:

$$-10\,\text{V} + 1\,\text{k}\Omega\cdot I_a + 2\,\text{k}\Omega\cdot I_b = 0, \qquad 1\,\text{k}\Omega\cdot I_c + 1\,\text{k}\Omega\cdot I_c - 2\,\text{k}\Omega\cdot I_b = 0.$$

**Schritt 5.** Die rechte Gleichung ergibt $I_c$ gleich $I_b$, die Knotengleichung dann $I_a$ gleich $2\,I_b$; eingesetzt in die linke:

$$-10\,\text{V} + 2\,\text{k}\Omega\cdot I_b + 2\,\text{k}\Omega\cdot I_b = 0, \qquad I_b = 2{,}5\,\text{mA}, \qquad I_a = 5\,\text{mA}, \qquad I_c = 2{,}5\,\text{mA}.$$

Alle positiv, die Pfeile zeigen also in die wirklichen Richtungen. Die Potenziale gegen D: B liegt bei $10\,\text{V}$ minus $5\,\text{V}$ an $R_1$, also
$5\,\text{V}$, und C bei $2{,}5\,\text{V}$ — die Werte aus dem vorigen Artikel.

**Probe mit der Leistung.** Die Quelle gibt $10\,\text{V}\cdot5\,\text{mA}$ ab, die Widerstände nehmen $R\,I^2$ auf:

$$P_\text{ab,q} = 50\,\text{mW}, \qquad 25\,\text{mW} + 12{,}5\,\text{mW} + 6{,}25\,\text{mW} + 6{,}25\,\text{mW} = 50\,\text{mW}.$$

**Im Bild:** Fünf Milliampere steigen über die Quelle auf; an der Kreuzung B teilen sie sich zu gleichen Teilen auf die beiden Abstiege, die gleich viel
Widerstand bieten.
::::

:::grafik
Szene: get1/stroeme-und-spannungen/05-rezept · Vorlage: zweigstromanalyse
Die Leiterschaltung mit $U_\text{q}=10\,\text{V}$, $R_1=1\,\text{k}\Omega$, $R_2=2\,\text{k}\Omega$, $R_3=R_4=1\,\text{k}\Omega$. Die fünf Schritte erscheinen
nacheinander: Zählpfeile $I_a$, $I_b$, $I_c$ und die Spannungspfeile im VZS; die Knotengleichung an B leuchtet am Knoten auf; der Baum (nur $R_2$) wird dick
gezeichnet, die beiden Fenster mit Umlaufpfeilen; die Gleichungen bauen sich daneben auf; zum Schluss die Lösung $5\,\text{mA}$, $2{,}5\,\text{mA}$,
$2{,}5\,\text{mA}$ als Strömungsanimation mit Potenzialfarben an den Knoten ($10\,\text{V}$, $5\,\text{V}$, $2{,}5\,\text{V}$, $0\,\text{V}$) und ein
Leistungsbalken, der $50\,\text{mW}$ abgegeben und aufgenommen zeigt. Kernaussage: Zählpfeile, $k-1$ Knoten- und $z-k+1$ Maschengleichungen mit Ohm
ergeben genau so viele Gleichungen wie Unbekannte. (Rot = Zählpfeile, blau = Ströme, orange = Gleichungen und Leistung, grau = Baum und Bauteile.)
:::

## Wann die Regeln gelten

Beide Regeln sind Bilanzen und fragen nicht, was in den Zweigen sitzt: Sie gelten für Widerstände, Quellen und nichtlineare Bauteile gleichermaßen. Sie
haben aber Voraussetzungen, die man leicht übersieht, wenn es heißt, sie gälten „in jedem Zeitpunkt".

- **Knotenregel:** Am Knoten darf sich keine Ladung sammeln. Für eine ideale Verbindung stimmt das. Bei sehr schnell wechselnden Strömen hat aber jede
  Leitung eine kleine Kapazität gegen ihre Umgebung; dann rechnet man diese als Kondensator in einem eigenen Zweig mit, und die Regel gilt wieder.
- **Maschenregel:** Die Spannung muss wegunabhängig sein. Für Gleichstrom stimmt das immer. Ändert sich ein Magnetfeld, das durch die Masche greift,
  entsteht nach dem Induktionsgesetz eine zusätzliche Spannung, und das Wegintegral um die Masche ist nicht mehr null; in Schaltungen schreibt man diese
  Spannung einer Spule zu, einem eigenen Bauteil im Zweig.
- **Grenze der Bauteilbetrachtung:** Werden die Leitungen so lang wie die Wellenlänge der Signale, versagen beide Regeln; dann braucht man die
  Leitungstheorie.

**Im Bild:** Die Kreuzungsregel braucht Kreuzungen ohne Rastplatz, die Rundwegregel ein Gelände, das sich nicht unter den Füßen hebt und senkt.

## Bedeutung und Ausblick

Die beiden Kirchhoffschen Regeln sind das Fundament der ganzen Schaltungsanalyse. Der nächste Artikel leitet aus ihnen die Regeln für die Zusammenschaltung
von Widerständen her: Hintereinander fließt durch alle derselbe Strom, weil an den Verbindungspunkten nichts abzweigt, und die Spannungen addieren sich
nach der Maschenregel. Nebeneinander liegt an allen dieselbe Spannung, und die Ströme addieren sich nach der Knotenregel. Man nennt das den
__Schaltungszwang__.

Die
[Strom- und Spannungsmessung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strom-und-spannungsmessung/strom-und-spannungsmessung.html)
folgt ebenfalls aus ihnen: Ein Strommesser wird in den Zweig eingeschleift, damit durch ihn derselbe Strom fließt, ein
Spannungsmesser parallel angeschlossen, damit an ihm dieselbe Spannung liegt. Die Verfahren der Netzwerkanalyse sparen Unbekannte: Das
[Maschenstromverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/maschenstromverfahren/maschenstromverfahren.html) rechnet mit
$z-k+1$ Maschenströmen, das
[Knotenpotentialverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/knotenpotentialverfahren/knotenpotentialverfahren.html) mit
$k-1$ Knotenpotenzialen — beide setzen die Kirchhoffschen
Regeln so geschickt ein, dass eine davon von selbst erfüllt ist. Und die Leistungsbilanz aus dem Artikel über Zählpfeile, nach der in jedem Netz die
Summe aller aufgenommenen Leistungen null ist, folgt aus genau diesen beiden Regeln, wie die Herleitung beim Rechenrezept zeigt.

:::kern
- __Knotenregel__: Die Summe der Ströme mit Pfeil zum Knoten ist null; gleichwertig ist der Zufluss gleich dem Abfluss.
- Grund ist die __Ladungserhaltung__: Ein Knoten speichert keine Ladung.
- Mit allen Pfeilen zum Knoten ist mindestens ein Strom negativ, er fließt in Wirklichkeit ab.
- Von $k$ Knotengleichungen sind $k-1$ unabhängig; die letzte ist die negative Summe der übrigen.
- __Maschenregel__: Die Summe der Spannungen einer Masche ist null, mit Plus für Pfeile in Umlaufrichtung und Minus dagegen.
- Grund ist die __Wegunabhängigkeit__ der Spannung: Nach einem Umlauf ist man auf dem Ausgangspotenzial.
- Unabhängige Maschengleichungen gibt es genau $z-k+1$, etwa aus den Verbindungszweigen eines Baums.
- Rezept: Zählpfeile, $k-1$ Knoten- und $z-k+1$ Maschengleichungen, Ohm im VZS einsetzen, lösen, Vorzeichen deuten.
- Probe: Die abgegebenen Leistungen der Quellen sind die aufgenommenen der Widerstände.
- Grenzen: Ladungsstau an Knoten und sich ändernde Magnetfelder durch Maschen werden als eigene Bauteile modelliert.
:::

:::quiz
F: Warum gilt die Knotenregel, und in welchen beiden Formen schreibt man sie?
A: Ein Knoten ist eine ideale Verbindung ohne Speichervermögen; die Ladung in einer Hülle um ihn ändert sich um Zufluss minus Abfluss, und weil sie konstant bleiben muss, ist der Zufluss gleich dem Abfluss (Ladungserhaltung). Mit allen Pfeilen zum Knoten ist die Summe der Ströme null, gleichwertig ist die Summe der zufließenden gleich der der abfließenden.
F: Was bedeutet es, wenn alle Ströme an einem Knoten als zufließend eingezeichnet sind?
A: Ihre Summe ist null, also können nicht alle positiv sein: Mindestens einer ist negativ und fließt in Wirklichkeit ab. An der Abzweigdose mit $10\,\text{A}$ Zuleitung und Abgängen von $4$, $2{,}5$ und $3{,}5\,\text{A}$ stehen bei Pfeilen zur Dose die Werte $10$, $-4$, $-2{,}5$ und $-3{,}5\,\text{A}$.
F: Warum reichen $k-1$ Knotengleichungen?
A: Jeder Zweig verbindet zwei Knoten; sein Strom steht in genau zwei Knotengleichungen, einmal mit Plus und einmal mit Minus. Die Summe aller $k$ Gleichungen ist deshalb null gleich null, und eine von ihnen folgt aus den anderen. In der Brückenschaltung ist die Summe der Gleichungen an $K_1$ bis $K_3$ die negative Gleichung an $K_4$.
F: Wie folgt die Maschenregel aus dem Potenzial?
A: Jede Spannung mit Pfeil in Umlaufrichtung ist das Potenzial ihres Anfangs- minus das ihres Endpunkts; Pfeile gegen den Umlauf bekommen ein Minus. In der Summe heben sich die Potenziale aller Zwischenpunkte weg, und es bleibt das Potenzial des Ausgangspunkts minus sich selbst, also null. Gleichbedeutend ist das Wegintegral des Felds um die Masche null.
F: Wie lautet die Maschenregel für zwei Widerstände $R_1$, $R_2$ in Reihe parallel zu $R_3$, und warum?
A: $U_1+U_2-U_3=0$: Der Umlauf läuft gegen den Uhrzeigersinn, links hinunter und rechts hinauf. $U_1$ und $U_2$ zeigen nach unten, also in Umlaufrichtung, $U_3$ ebenfalls nach unten, also gegen den Umlauf. Dabei ist $U_3=\varphi_1-\varphi_2$ — beide Wege von oben nach unten verlieren dasselbe Potenzial.
F: Was bedeutet $U_3=-8\,\text{V}$ in einem Umlauf mit $24\,\text{V}$ Quellenspannung und den Widerstandsspannungen $6$ und $10\,\text{V}$?
A: Der Pfeil von $U_3$ wurde gegen die tatsächliche Richtung gezeichnet. In Umlaufrichtung fallen am dritten Widerstand $8\,\text{V}$ ab, und die Quelle hebt um $24\,\text{V}$ — genau so viel, wie $6$, $10$ und $8\,\text{V}$ zusammen senken.
F: Warum bringt die äußere Masche der Brücke keine neue Gleichung?
A: Ihre Gleichung $U_0-U_3+U_4=0$ ist die Kombination $M_2-M_1-M_3$ der anderen. Allgemein ist die Maschengleichung linear im Maschenvektor: Eine Masche, die sich aus anderen zusammensetzt, hat als Gleichung dieselbe Kombination der anderen Gleichungen. Unabhängig sind genau $z-k+1$.
F: Warum fließt im Netz mit zwei Quellen von $12$ und $9\,\text{V}$ an einer $4$-$\Omega$-Last ein negativer Strom?
A: Die Lösung ergibt $I_2=-\frac13\,\text{A}$: Der Strom fließt in den Pluspol der $9$-V-Quelle hinein, denn die Last liegt an rund $9{,}33\,\text{V}$, mehr als diese Quelle hält. Die $12$-V-Quelle gibt $32\,\text{W}$ ab, $29\,\text{W}$ gehen in die Widerstände, $3\,\text{W}$ lädt die schwächere Quelle.
F: Wie geht man beim Berechnen eines Netzes vor, und warum gehen die Gleichungen genau auf?
A: Zählpfeile festlegen, Knotenregel an $k-1$ Knoten, Maschenregel an $z-k+1$ unabhängigen Maschen eines Baums, Ohm im VZS einsetzen, lösen, Vorzeichen deuten. Nach dem Einsetzen bleiben $z$ Zweigströme unbekannt, und es gibt $(k-1)+(z-k+1)=z$ Gleichungen. In der Leiterschaltung mit $10\,\text{V}$ ergeben sich $5$, $2{,}5$ und $2{,}5\,\text{mA}$, mit $50\,\text{mW}$ abgegeben und aufgenommen.
F: Wann gelten die Kirchhoffschen Regeln nicht mehr unverändert?
A: Die Knotenregel setzt voraus, dass sich am Knoten keine Ladung sammelt; bei schnellen Vorgängen rechnet man Leitungskapazitäten als eigene Kondensatoren. Die Maschenregel setzt Wegunabhängigkeit voraus; ein sich änderndes Magnetfeld durch die Masche induziert eine Spannung, die man einer Spule zuschreibt. Sind die Leitungen so lang wie die Wellenlänge, braucht man die Leitungstheorie.
:::
