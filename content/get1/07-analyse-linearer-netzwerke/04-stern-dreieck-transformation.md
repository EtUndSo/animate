---
title: Stern-Dreieck-Transformation
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70200
summary: Von Grund auf – wie man Widerstandsnetze zusammenfasst, die sich mit Reihe und Parallele allein nicht auflösen lassen. Leitbild sind drei Anschlüsse eines Wassernetzes, die entweder durch eine Ringleitung oder über einen Verteiler verbunden sind, und Rohre zwischen Punkten gleichen Drucks, durch die nichts fließt. Mit Gruppenschaltungen und Kettenbruch, Punkten gleichen Potenzials aus Symmetrie samt Beweis, Halbschaltungen und Widerstandswürfel, der Dreieck-Stern- und Stern-Dreieck-Umwandlung in Widerstands- und Leitwertform mit Herleitung durch Knotenelimination, dem symmetrischen Sonderfall, der Brückenschaltung und der Umwandlung von π- in T-Schaltungen am Dämpfungsglied. Mit Beispiel-Seite.
tags: Stern-Dreieck, Transformation, Kennelly, Brückenschaltung, Ersatzwiderstand
---

## Anschaulich

Viele Widerstandsnetze lassen sich mit Reihen- und Parallelschaltung Schritt für Schritt zu einem einzigen Widerstand zusammenfassen. Manche aber nicht:
In einer Brückenschaltung liegt kein einziges Paar von Widerständen rein in Reihe oder rein parallel. Zwei Werkzeuge helfen dann weiter. Die __Symmetrie__
verrät Punkte gleichen Potenzials, zwischen denen kein Strom fließt. Und die __Stern-Dreieck-Transformation__ ersetzt drei Widerstände durch drei andere,
ohne dass der Rest des Netzes etwas davon merkt.

**Das Leitbild dieses Artikels:** **Ringleitung oder Verteiler.** Ein Wassernetz besteht aus Rohren, in denen der Druckverlust proportional zum
Durchfluss ist, so wie in einem elektrischen Netz die Spannung am Widerstand proportional zum Strom. Drei Anschlüsse 1, 2 und 3 dieses Netzes sollen
untereinander verbunden werden. Man kann je zwei von ihnen durch ein eigenes Rohr verbinden, eine __Ringleitung__ aus drei Rohren: das Dreieck. Oder man
führt von jedem Anschluss ein Rohr zu einem gemeinsamen __Verteiler__ in der Mitte: der Stern. Mit passend gewählten Rohren kann niemand, der nur an den
drei Anschlüssen pumpt und misst, sagen, welche Verrohrung hinter der Wand liegt.

Drei Folgerungen:

- **Umbauen, ohne dass es jemand merkt.** Ein Netz, das irgendwo eine Ringleitung enthält, verhält sich genauso, wenn man dort einen passenden Verteiler
  einbaut — und oft lässt es sich danach mit Reihe und Parallele zusammenfassen.
- **Der Verteilerarm folgt aus den Ringrohren.** Wie eng der Arm vom Verteiler zu einem Anschluss sein muss, bestimmen die beiden Ringrohre, die an
  diesem Anschluss ankommen, im Verhältnis zum ganzen Ring.
- **Zwischen Punkten gleichen Drucks fließt nichts.** Ein Rohr zwischen zwei solchen Punkten bleibt leer; man darf es entfernen oder neue Verbindungen
  ziehen. Solche Punkte findet man an der Symmetrie eines Netzes.

:::grafik
Szene: get1/analyse-linearer-netzwerke/04-ringleitung-verteiler · Vorlage: ringleitung-verteiler
Links drei Anschlüsse 1, 2, 3 an einer Hauswand mit einer Ringleitung aus drei Rohren unterschiedlicher Weite, rechts dieselben drei Anschlüsse mit einem
Verteiler in der Mitte und drei Armen. Eine Pumpe lässt sich wahlweise zwischen zwei der Anschlüsse setzen; Manometer und Wasseruhren an allen drei
Anschlüssen zeigen links und rechts dieselben Werte. Ein Schieber macht eines der Ringrohre enger, und die passenden Verteilerarme ändern sich mit. Darunter
ein zweites Feld: ein symmetrisches Rohrnetz zwischen Zulauf und Ablauf mit einer Querleitung zwischen zwei gespiegelten Punkten, deren Manometer gleichen
Druck zeigen; die Wasseruhr in der Querleitung steht still. Kernaussage: Ringleitung und Verteiler sind von außen gleichwertig, und zwischen Punkten
gleichen Drucks fließt nichts. (Blau = Wasser und Drücke, rot = Ringleitung und Verteiler, orange = veränderliche Rohre, grau = Wand und übriges Netz.)
:::

## Gruppen zusammenfassen

Die meisten Netze bestehen aus __Gruppen__, deren Widerstände für sich in Reihe oder parallel liegen. Man fasst sie __von innen nach außen__ zusammen, wie
im Artikel über die Zusammenschaltung von Widerständen: zuerst eine innerste Gruppe, deren Teile wirklich nur in Reihe oder nur parallel liegen, dann die
nächste, bis ein einziger Widerstand zwischen den Klemmen steht (Bild 7.1 bis 7.3 des Skripts).

Zwei Schreibweisen helfen, den Überblick zu behalten. Mit dem Zeichen $\parallel$ für die Parallelschaltung zeigen Klammern die Reihenfolge. Als
__Kettenbruch__ geschrieben wechseln sich die beiden Regeln ab: In Reihe addiert man Widerstände, parallel Leitwerte, und dazwischen nimmt man den
Kehrwert. Für einen Längswiderstand $R_1$, einen Querleitwert $G_2$ und dahinter die Reihe aus $R_3$ und $R_4$:

$$R_1 + R_2 \parallel (R_3 + R_4) = R_1 + \cfrac{1}{G_2 + \cfrac{1}{R_3 + R_4}}.$$

**So liest man das:** Jede Stufe des Kettenbruchs ist ein Wechsel zwischen Reihe und Parallele; wer ihn von innen liest, rollt das Netz von seinem fernen
Ende her auf. Das Verfahren endet, sobald keine Gruppe mehr rein in Reihe oder rein parallel liegt. Dann braucht man Symmetrie oder die
Stern-Dreieck-Umwandlung.

**Im Bild:** Rohrgruppen von innen nach außen durch Ersatzrohre ersetzen, bis ein einziges Rohr zwischen Zulauf und Ablauf übrig ist.

:::herleitung
**Parallel als Kehrwert.** Parallel addieren sich die Leitwerte. Für einen Widerstand $R_2$ parallel zu einem Teilnetz mit dem Widerstand $X$ ist der
Gesamtleitwert $G_2 + 1/X$, der Widerstand sein Kehrwert:

$$R_2 \parallel X = \frac{1}{G_2 + 1/X}.$$

Mit $X$ gleich $R_3 + R_4$ und dem Längswiderstand $R_1$ in Reihe davor ergibt das die Formel. Jede weitere Stufe des Netzes schachtelt einen weiteren
Bruch hinein.
:::

::::beispiel Ein Kettenleiter, von innen nach außen
Ein Netz zwischen den Klemmen A und B: Von A führt $R_1$ zu einem Knoten X, von X führt $R_2$ nach B; von X führen zwei parallele Widerstände $R_3$ und
$R_4$ zu einem Knoten Y, und von Y führt $R_5$ nach B.

$$R_1 = 15\,\Omega, \qquad R_2 = 70\,\Omega, \qquad R_3 = R_4 = 20\,\Omega, \qquad R_5 = 60\,\Omega.$$

**Von innen nach außen.** Die innerste Gruppe ist die Parallelschaltung von $R_3$ und $R_4$; sie liegt in Reihe mit $R_5$, das Ganze parallel zu $R_2$,
und davor $R_1$:

$$R_3 \parallel R_4 = 10\,\Omega, \qquad 10\,\Omega + 60\,\Omega = 70\,\Omega, \qquad 70\,\Omega \parallel 70\,\Omega = 35\,\Omega, \qquad R_{AB} = 15\,\Omega + 35\,\Omega = 50\,\Omega.$$

**Als Kettenbruch,** mit den Leitwerten $G_2$ und $G_3 + G_4$:

$$R_{AB} = R_1 + \cfrac{1}{G_2 + \cfrac{1}{\cfrac{1}{G_3 + G_4} + R_5}} = 15\,\Omega + \cfrac{1}{\frac{1}{70}\,\text{S} + \cfrac{1}{10\,\Omega + 60\,\Omega}} = 50\,\Omega.$$

**Im Bild:** Zwei gleiche Rohre nebeneinander wirken wie eines mit halbem Widerstand; mit dem Rohr dahinter ergibt das ein Ersatzrohr, das zusammen mit
dem Abzweig $R_2$ eines von $35\,\Omega$ bildet.
::::

## Symmetrie: Punkte gleichen Potenzials

Ein zweites Werkzeug beruht auf einer einfachen Beobachtung: Durch einen Widerstand zwischen zwei Knoten gleichen Potenzials fließt kein Strom. Man darf
ihn deshalb entfernen, und man darf zwei solche Knoten durch einen Draht verbinden, ohne dass sich irgendein Strom oder eine Spannung im Netz ändert.
Woher man weiß, welche Knoten gleiches Potenzial haben, sagt die Symmetrie.

Geht ein Netz durch eine Spiegelung in sich über, bei der die Klemmen A und B vertauscht werden und jeder Widerstand auf einen gleich großen fällt, dann
gilt für jeden Knoten P und seinen Spiegelpunkt P':

:::formel Satz
$$\varphi_P + \varphi_{P'} = \varphi_A + \varphi_B, \qquad \varphi_P = \frac{\varphi_A + \varphi_B}{2}\ \text{ auf der Achse}.$$
:::

**So liest man das:** Gespiegelte Knoten liegen gleich weit über und unter dem Mittelwert der Klemmenpotenziale. Alle Knoten auf der Spiegelachse haben
genau diesen Mittelwert; man darf sie verbinden (Bild 7.4 des Skripts) oder das Netz entlang der Achse in zwei gleiche __Halbschaltungen__ zerschneiden
(Bild 7.5 und 7.6). Ein Widerstand, der die Achse kreuzt, wird dazu in zwei Hälften geteilt, deren Mittelpunkt auf der Achse liegt; ein Widerstand, der
auf der Achse liegt, führt keinen Strom. Ebenso haben Knoten gleiches Potenzial, die eine Drehung des Netzes um die Verbindung von A und B ineinander
überführt, wie die Ecken des Widerstandswürfels im Skript (Bild 7.8).

**Im Bild:** In einem symmetrischen Rohrnetz zwischen Zulauf und Ablauf hat jeder Punkt so viel Druck über dem Mittelwert wie sein Spiegelpunkt darunter;
auf der Symmetrielinie herrscht überall der mittlere Druck, und Querrohre dort bleiben leer.

:::herleitung
**Gleiches Potenzial, kein Strom.** Nach dem ohmschen Gesetz fließt durch einen Widerstand $R$ zwischen Knoten gleichen Potenzials der Strom
$(\varphi_C - \varphi_D)/R$, also null. Entfernt man ihn, ändert sich keine Knotenregel. Verbindet man zwei solche Knoten durch einen Draht, erfüllt die
alte Lösung mit dem Strom null im Draht alle Gleichungen des neuen Netzes, auch die Maschenregel über den Draht, denn an ihm liegt die Spannung null.
Weil die Lösung eindeutig ist (Artikel über die Kirchhoffschen Gesetze), ist sie die Lösung des neuen Netzes.

**Gespiegelte Lösung.** Aus der Lösung $\varphi$ bildet man eine zweite Potenzialverteilung, indem man an jedem Knoten den Wert des Spiegelknotens nimmt
und ihn am Mittelwert der Klemmen umklappt:

$$\tilde\varphi_P = \varphi_A + \varphi_B - \varphi_{P'}.$$

Weil die Spiegelung Widerstände auf gleich große abbildet, erfüllt $\tilde\varphi$ dieselben Knotenregeln wie $\varphi$; der feste Anteil
$\varphi_A + \varphi_B$ fällt in den Potenzialdifferenzen heraus. An den Klemmen hat $\tilde\varphi$ dieselben Werte, denn A ist der Spiegelpunkt von B. Wegen der Eindeutigkeit ist $\tilde\varphi$ gleich $\varphi$, und das ist die Formel. Für einen Knoten auf der
Achse ist P' gleich P, und es bleibt der Mittelwert. Eine Drehung, die A und B festhält, liefert ebenso, dass einander zugeordnete Knoten gleiches
Potenzial haben.
:::

::::beispiel Der Würfel über die Flächendiagonale
Zwölf gleiche Widerstände $R$ bilden die Kanten eines Würfels; gesucht ist der Widerstand zwischen zwei Ecken A und C, die sich auf einer Seitenfläche
diagonal gegenüberliegen. In Koordinaten liegen die Ecken bei 0 und 1 jeder Achse:

$$R = 1\,\text{k}\Omega, \qquad A = (0, 0, 0), \qquad C = (1, 1, 0), \qquad U_{AC} = 6\,\text{V}.$$

**Die Spiegelebene.** Die Ebene, in der die Summe aus erster und zweiter Koordinate eins ist, vertauscht A und C und bildet jede Kante auf eine Kante ab.
In ihr liegen vier Ecken, $(1, 0, 0)$, $(0, 1, 0)$, $(1, 0, 1)$ und $(0, 1, 1)$; sie liegen alle auf dem Mittelwert $3\,\text{V}$ und werden zu einem Knoten
M verbunden.

**Die Halbschaltung.** Von A führen zwei Kanten direkt nach M, parallel also $R/2$; die dritte Kante führt zur Ecke $(0, 0, 1)$, und von dort zwei Kanten nach
M, zusammen $R + R/2$. Beide Wege liegen parallel:

$$R_{AM} = \frac R2 \parallel \frac{3R}{2} = \frac38\,R = 375\,\Omega, \qquad R_{AC} = 2\cdot375\,\Omega = 750\,\Omega = \frac34\,R.$$

**Strom und Potenziale.** Bei $6\,\text{V}$ fließen $6\,\text{V}/750\,\Omega$, also $8\,\text{mA}$. Die Ecke $(0, 0, 1)$ liegt als Teiler zwischen A und M auf

$$\varphi_{(0,0,1)} = 3\,\text{V} + 3\,\text{V}\cdot\frac{R/2}{R + R/2} = 4\,\text{V}.$$

Zum Vergleich: Über die Raumdiagonale ergibt der Würfel im Skript $\frac56\,R$, also etwas mehr, denn der Weg ist länger.

**Im Bild:** Vier Ecken auf halber Höhe zwischen Zulauf und Ablauf haben denselben mittleren Druck; ein Rohr zwischen ihnen bliebe leer.
::::

Die Beispiele des Skripts nutzen genau das: In Bild 7.4 liegen C und D auf der Spiegelachse und werden verbunden, in Bild 7.5 und 7.6 wird ein
Widerstand auf der Achse in zwei Hälften $2R \parallel 2R$ und ein kreuzender in $R/2 + R/2$ geteilt, um die Halbschaltung abzutrennen. Beim
Widerstandswürfel über die Raumdiagonale (Bild 7.7 bis 7.9) liegen die drei Nachbarecken von A auf gleichem Potenzial, denn eine Drehung um die
Raumdiagonale führt sie ineinander über, und ebenso die drei Nachbarecken der Gegenecke. Verbunden ergeben sich drei Gruppen paralleler Widerstände in
Reihe, drei, sechs und drei Kanten:

$$R_g = \frac R3 + \frac R6 + \frac R3 = \frac56\,R.$$

## Stern und Dreieck

Drei Widerstände können drei Knoten 1, 2 und 3 auf zwei verschiedene Arten verbinden (Bild 7.10 des Skripts). Sind die Knoten Teil eines größeren
Netzes, das sich so nicht zusammenfassen lässt, ersetzt man die eine Form durch die andere.

**Die Akteure:**

- die __Dreieckschaltung__: zwischen je zwei der drei Knoten ein Widerstand, $R_{12}$, $R_{23}$ und $R_{31}$;
- die __Sternschaltung__: von jedem Knoten ein Widerstand zu einem gemeinsamen inneren Knoten 0, dem __Sternpunkt__, also $R_{10}$, $R_{20}$ und $R_{30}$,
  mit den Leitwerten $G_{10}$, $G_{20}$ und $G_{30}$;
- die Potenziale $\varphi_1, \varphi_2, \varphi_3$ der drei Knoten und die Ströme $I_1, I_2, I_3$, die von außen in sie hineinfließen.

Beide Schaltungen haben drei Anschlüsse und enthalten keine Quellen. Sie sind __äquivalent__, wenn sie bei beliebigen Potenzialen der drei Knoten
dieselben Ströme aufnehmen; der Sternpunkt ist von außen nicht zu sehen.

**Das Zusammenspiel:** *Welcher Stern ersetzt ein gegebenes Dreieck, und welches Dreieck einen gegebenen Stern?*

Für die Richtung vom Dreieck zum Stern, die __Dreieck-Stern-Umwandlung__ (Bild 7.11):

:::formel Satz
$$R_{10} = \frac{R_{12}\,R_{31}}{R_{12} + R_{23} + R_{31}}, \qquad R_{20} = \frac{R_{12}\,R_{23}}{R_{12} + R_{23} + R_{31}}, \qquad R_{30} = \frac{R_{23}\,R_{31}}{R_{12} + R_{23} + R_{31}}.$$
:::

**So liest man das:** Das Skript fasst es in einen Merksatz: Sternwiderstand gleich Produkt der __Anliegerwiderstände__ des Dreiecks, geteilt durch den
__Umfangswiderstand__. Anlieger sind die beiden Dreieckswiderstände, die an demselben Knoten ankommen wie der gesuchte Sternwiderstand; der
Umfangswiderstand ist die Summe aller drei. Nach Arthur Edwin Kennelly, der die Umwandlung 1899 veröffentlichte, heißt sie auch Kennelly-Umwandlung.

Eine Probe ist der Grenzfall, in dem ein Dreieckswiderstand fehlt. Ist $R_{23}$ unendlich groß, wird $R_{10}$ null, und $R_{20}$ und $R_{30}$ werden zu
$R_{12}$ und $R_{31}$: Die beiden übrigen Widerstände bilden schon einen Stern, mit dem Knoten 1 als Sternpunkt.

**Im Bild:** Der Arm vom Verteiler zu Anschluss 1 entsteht aus den beiden Ringrohren, die an Anschluss 1 ankommen: ihr Produkt, geteilt durch den ganzen
Ring.

:::herleitung
**Paarweise messen.** Bleibt Knoten 3 offen, fließt im Stern Strom nur durch $R_{10}$ und $R_{20}$ in Reihe; im Dreieck liegt $R_{12}$ parallel zur Reihe aus
$R_{23}$ und $R_{31}$. Beide Widerstände zwischen 1 und 2 müssen gleich sein, und ebenso für die beiden anderen Paare. Mit dem Umfangswiderstand $\Sigma$,
der Summe der drei Dreieckswiderstände:

$$R_{10} + R_{20} = \frac{R_{12}\,(R_{23} + R_{31})}{\Sigma}, \qquad R_{20} + R_{30} = \frac{R_{23}\,(R_{31} + R_{12})}{\Sigma}, \qquad R_{30} + R_{10} = \frac{R_{31}\,(R_{12} + R_{23})}{\Sigma}.$$

**Auflösen.** Die Summe der drei Gleichungen, halbiert, ergibt die Summe der drei Sternwiderstände; zieht man davon die mittlere Gleichung ab, bleibt
$R_{10}$:

$$R_{10} + R_{20} + R_{30} = \frac{R_{12}R_{23} + R_{23}R_{31} + R_{31}R_{12}}{\Sigma}, \qquad R_{10} = \frac{R_{31}R_{12}}{\Sigma}.$$

Ebenso folgen $R_{20}$ und $R_{30}$. Im Bild: Je zwei Anschlüsse durchpumpen, der dritte zu — dreimal gemessen, und die drei Verteilerarme liegen fest.

**Volle Gleichwertigkeit.** Drei paarweise Messungen sind nur drei von unendlich vielen Beschaltungen. Dass der so gefundene Stern dem Dreieck bei
beliebigen Potenzialen gleicht, zeigt die Gegenrichtung unten: Sie gilt für alle Potenziale, und auf diesen Stern angewandt liefert sie das Dreieck zurück.
:::

::::beispiel Eine Brücke, die sich nicht zusammenfassen lässt
Eine Brücke zwischen A oben und B unten. A ist der Knoten 1; von ihm führen $R_{12}$ zum linken Mittelknoten 2 und $R_{31}$ zum rechten Mittelknoten 3.
Zwischen den Mittelknoten liegt der Brückenwiderstand $R_{23}$, von 2 führt $R_{2B}$ und von 3 führt $R_{3B}$ nach B.

$$R_{12} = 10\,\Omega, \qquad R_{31} = 20\,\Omega, \qquad R_{23} = 20\,\Omega, \qquad R_{2B} = 26\,\Omega, \qquad R_{3B} = 12\,\Omega.$$

Kein Paar liegt in Reihe oder parallel, und abgeglichen ist die Brücke auch nicht, denn die Verhältnisse 10 zu 26 und 20 zu 12 sind verschieden.

**Das Dreieck 1, 2, 3 wird zum Stern.** Der Umfangswiderstand ist $50\,\Omega$:

$$R_{10} = \frac{10\cdot20}{50}\,\Omega = 4\,\Omega, \qquad R_{20} = \frac{10\cdot20}{50}\,\Omega = 4\,\Omega, \qquad R_{30} = \frac{20\cdot20}{50}\,\Omega = 8\,\Omega.$$

**Zusammenfassen.** Jetzt liegen $R_{20}$ und $R_{2B}$ in Reihe, ebenso $R_{30}$ und $R_{3B}$; beide Zweige liegen parallel, und davor $R_{10}$:

$$R_{AB} = 4\,\Omega + (4\,\Omega + 26\,\Omega) \parallel (8\,\Omega + 12\,\Omega) = 4\,\Omega + 30\,\Omega \parallel 20\,\Omega = 16\,\Omega.$$

**Ströme bei 32 Volt.** Es fließen $2\,\text{A}$; der Sternpunkt liegt auf $24\,\text{V}$, und die beiden Zweige führen $0{,}8\,\text{A}$ und $1{,}2\,\text{A}$.
Damit liegen die Knoten 2 und 3, die die Umwandlung unverändert lässt, auf

$$\varphi_2 = 0{,}8\,\text{A}\cdot26\,\Omega = 20{,}8\,\text{V}, \qquad \varphi_3 = 1{,}2\,\text{A}\cdot12\,\Omega = 14{,}4\,\text{V}.$$

Die Ströme in den Sternarmen sind aber nicht die Ströme in den ursprünglichen Dreieckswiderständen. Diese folgen aus den Potenzialen:

$$I_{12} = \frac{32\,\text{V} - 20{,}8\,\text{V}}{10\,\Omega} = 1{,}12\,\text{A}, \qquad I_{13} = \frac{32\,\text{V} - 14{,}4\,\text{V}}{20\,\Omega} = 0{,}88\,\text{A}, \qquad I_{23} = \frac{20{,}8\,\text{V} - 14{,}4\,\text{V}}{20\,\Omega} = 0{,}32\,\text{A}.$$

Der Arm $R_{10}$ führt die vollen $2\,\text{A}$; im Dreieck teilen sie sich auf $1{,}12\,\text{A}$ und $0{,}88\,\text{A}$, und durch die Brücke fließen
$0{,}32\,\text{A}$ von 2 nach 3.

**Im Bild:** Die Ringleitung oben wird durch einen Verteiler ersetzt; danach sind es nur noch zwei Rohrstränge nebeneinander hinter einem Zulaufrohr.
::::

Für die Gegenrichtung, die __Stern-Dreieck-Umwandlung__ (Bild 7.12), rechnet man am bequemsten mit Leitwerten:

:::formel Satz
$$G_{12} = \frac{G_{10}\,G_{20}}{G_{10} + G_{20} + G_{30}}, \qquad G_{23} = \frac{G_{20}\,G_{30}}{G_{10} + G_{20} + G_{30}}, \qquad G_{31} = \frac{G_{30}\,G_{10}}{G_{10} + G_{20} + G_{30}},$$

$$R_{12} = R_{10} + R_{20} + \frac{R_{10}\,R_{20}}{R_{30}}, \qquad R_{23} = R_{20} + R_{30} + \frac{R_{20}\,R_{30}}{R_{10}}, \qquad R_{31} = R_{30} + R_{10} + \frac{R_{30}\,R_{10}}{R_{20}}.$$
:::

**So liest man das:** Der Merksatz des Skripts ist das Spiegelbild des ersten: Dreiecksleitwert gleich Produkt der Anliegerleitwerte des Sterns, geteilt
durch die Summe der Leitwerte des Sterns. Widerstände und Leitwerte, Dreieck und Stern tauschen die Rollen. In Widerständen ist der Dreieckswiderstand
zwischen zwei Knoten die Reihe ihrer beiden Sternwiderstände, vergrößert um deren Produkt geteilt durch den dritten Sternwiderstand — umso mehr, je
kleiner dieser dritte ist.

**Im Bild:** Das Ringrohr zwischen 1 und 2 ist umso weiter, je weiter die beiden Verteilerarme 1 und 2 sind. Ein weiter dritter Arm lenkt Wasser zu
Anschluss 3 ab, und das direkte Ringrohr zwischen 1 und 2 wird entsprechend enger.

:::herleitung
**Den Sternpunkt eliminieren.** In den Sternpunkt fließt von außen nichts; nach der Knotenregel heben sich die Ströme aus den drei Armen auf. Sein
Potenzial ist deshalb der mit den Leitwerten gewichtete Mittelwert der drei Knotenpotenziale, mit $G_\Sigma$ als Summe der drei Sternleitwerte:

$$G_{10}(\varphi_1 - \varphi_0) + G_{20}(\varphi_2 - \varphi_0) + G_{30}(\varphi_3 - \varphi_0) = 0, \qquad \varphi_0 = \frac{G_{10}\varphi_1 + G_{20}\varphi_2 + G_{30}\varphi_3}{G_\Sigma}.$$

**Der Strom in Knoten 1.** Eingesetzt, mit $\varphi_1$ als $(G_{10} + G_{20} + G_{30})\,\varphi_1/G_\Sigma$ geschrieben:

$$I_1 = G_{10}(\varphi_1 - \varphi_0) = \frac{G_{10}G_{20}}{G_\Sigma}\,(\varphi_1 - \varphi_2) + \frac{G_{10}G_{30}}{G_\Sigma}\,(\varphi_1 - \varphi_3).$$

Im Dreieck fließt in Knoten 1 der Strom durch $G_{12}$ und $G_{31}$:

$$I_1 = G_{12}\,(\varphi_1 - \varphi_2) + G_{31}\,(\varphi_1 - \varphi_3).$$

Beide stimmen für beliebige Potenziale überein, wenn die Faktoren gleich sind; das sind die Leitwertformeln, und für die Knoten 2 und 3 geht es ebenso.
Damit ist die Gleichwertigkeit für jede Beschaltung bewiesen. Im Bild: Der Verteiler ist ein Knoten, in den von außen nichts fließt; sein Druck stellt
sich als gewichtetes Mittel der drei Anschlussdrücke ein.

**In Widerständen.** Der Kehrwert von $G_{12}$, mit $R_{10}R_{20}$ erweitert:

$$R_{12} = \frac{G_{10} + G_{20} + G_{30}}{G_{10}\,G_{20}} = R_{10}R_{20}\Big(\frac{1}{R_{10}} + \frac{1}{R_{20}} + \frac{1}{R_{30}}\Big) = R_{20} + R_{10} + \frac{R_{10}R_{20}}{R_{30}}.$$

**Hin und zurück.** Der Stern aus der Dreieck-Stern-Umwandlung hat die Leitwerte

$$G_{10} = \frac{\Sigma}{R_{12}R_{31}}, \qquad G_{20} = \frac{\Sigma}{R_{12}R_{23}}, \qquad G_{30} = \frac{\Sigma}{R_{23}R_{31}}.$$

Eingesetzt ergibt die Leitwertformel wieder das ursprüngliche Dreieck:

$$G_{10}\,G_{20} = \frac{\Sigma^2}{R_{12}^2R_{23}R_{31}}, \qquad G_{10} + G_{20} + G_{30} = \frac{\Sigma^2}{R_{12}R_{23}R_{31}}, \qquad G_{12} = \frac{1}{R_{12}}.$$
:::

::::beispiel Dieselbe Brücke, andersherum
Die Brücke von oben, diesmal ohne Dreieck-Stern-Umwandlung: Am linken Mittelknoten 2 treffen sich genau drei Widerstände, $R_{12}$ von A, $R_{23}$ vom
Knoten 3 und $R_{2B}$ von B. Sie bilden einen Stern mit dem Knoten 2 als Sternpunkt.

$$R_{12} = 10\,\Omega, \qquad R_{23} = 20\,\Omega, \qquad R_{2B} = 26\,\Omega, \qquad R_{31} = 20\,\Omega, \qquad R_{3B} = 12\,\Omega.$$

**Der Stern wird zum Dreieck** zwischen A, 3 und B, in der Widerstandsform:

$$R'_{13} = 10 + 20 + \frac{10\cdot20}{26} \approx 37{,}69\,\Omega, \qquad R'_{1B} = 10 + 26 + \frac{10\cdot26}{20} = 49\,\Omega, \qquad R'_{3B} = 20 + 26 + \frac{20\cdot26}{10} = 98\,\Omega.$$

**Zusammenfassen.** Jetzt liegt $R'_{13}$ parallel zu $R_{31}$, $R'_{3B}$ parallel zu $R_{3B}$, beide Paare in Reihe, und das Ganze parallel zu $R'_{1B}$:

$$20\,\Omega \parallel 37{,}69\,\Omega \approx 13{,}07\,\Omega, \qquad 12\,\Omega \parallel 98\,\Omega \approx 10{,}69\,\Omega, \qquad R_{AB} = 49\,\Omega \parallel 23{,}76\,\Omega \approx 16{,}0\,\Omega.$$

Beide Richtungen führen auf denselben Widerstand; die erste Rechnung war nur glatter.

**Im Bild:** Statt die Ringleitung oben durch einen Verteiler zu ersetzen, ersetzt man den Verteiler am Knoten 2 durch eine Ringleitung zwischen A, 3 und B.
::::

Sind alle drei Widerstände gleich, $R_\Delta$ im Dreieck und $R_Y$ im Stern, schrumpfen beide Umwandlungen auf einen Faktor drei:

:::formel
$$R_Y = \frac{R_\Delta}{3}, \qquad R_\Delta = 3\,R_Y.$$
:::

**So liest man das:** Ein Dreieck aus drei gleichen Widerständen wirkt wie ein Stern aus Widerständen mit einem Drittel des Werts. Schließt man deshalb
dieselben drei Widerstände einmal im Dreieck und einmal im Stern an dieselben drei Knoten an, nehmen sie im Dreieck dreimal so viel Strom und Leistung auf.
In der Drehstromtechnik, beim dreiphasigen Wechselstrom des Stromnetzes, nutzt man das beim __Stern-Dreieck-Anlauf__ großer Motoren: Man startet im Stern
mit einem Drittel des Stroms und schaltet erst danach ins Dreieck um.

**Im Bild:** Drei gleiche Ringrohre gleichen einem Verteiler mit drei Armen, die jeweils ein Drittel des Widerstands haben.

:::herleitung
**Einsetzen.** Mit drei gleichen Dreieckswiderständen und drei gleichen Sternwiderständen:

$$R_Y = \frac{R_\Delta\cdot R_\Delta}{3\,R_\Delta} = \frac{R_\Delta}{3}, \qquad R_\Delta = R_Y + R_Y + \frac{R_Y\cdot R_Y}{R_Y} = 3\,R_Y.$$

**Dreimal so viel Strom.** Dieselben Widerstände im Stern haben den dreifachen Wert des gleichwertigen Sterns. Verdreifacht man in einem Netz ohne Quellen
alle Widerstände, bleiben die Knotenregeln mit denselben Potenzialen erfüllt, wenn alle Ströme auf ein Drittel sinken; bei festen Potenzialen an den
Anschlüssen sinken also Ströme und Leistung auf ein Drittel.
:::

::::beispiel Drei gleiche Widerstände im Dreieck und im Stern
Drei Widerstände von $60\,\Omega$ liegen im Dreieck zwischen drei Knoten mit festen Potenzialen:

$$R_\Delta = 60\,\Omega, \qquad \varphi_1 = 12\,\text{V}, \qquad \varphi_2 = 0\,\text{V}, \qquad \varphi_3 = 6\,\text{V}.$$

**Im Dreieck.** In Knoten 1 fließen die Ströme zu den beiden anderen Knoten:

$$I_1 = \frac{12\,\text{V}}{60\,\Omega} + \frac{6\,\text{V}}{60\,\Omega} = 0{,}3\,\text{A}.$$

**Im gleichwertigen Stern** mit $20\,\Omega$ je Arm liegt der Sternpunkt bei gleichen Leitwerten auf dem einfachen Mittelwert der drei Potenziale:

$$\varphi_0 = \frac{12\,\text{V} + 0\,\text{V} + 6\,\text{V}}{3} = 6\,\text{V}, \qquad I_1 = \frac{12\,\text{V} - 6\,\text{V}}{20\,\Omega} = 0{,}3\,\text{A}.$$

**Dieselben 60 Ohm im Stern** führen nur ein Drittel, und auch die Leistung sinkt auf ein Drittel, von $3{,}6\,\text{W}$ im Dreieck auf $1{,}2\,\text{W}$:

$$I_1 = \frac{6\,\text{V}}{60\,\Omega} = 0{,}1\,\text{A}, \qquad P_\Delta = \frac{(12\,\text{V})^2 + (6\,\text{V})^2 + (6\,\text{V})^2}{60\,\Omega} = 3{,}6\,\text{W}, \qquad P_Y = \frac{(6\,\text{V})^2 + (6\,\text{V})^2 + 0^2}{60\,\Omega} = 1{,}2\,\text{W}.$$

**Im Bild:** Ein Verteiler mit drei Armen von je einem Drittel des Ringrohr-Widerstands ersetzt den Ring; baut man dieselben Rohre als Verteiler ein, fließt
nur ein Drittel.
::::

## π- und T-Schaltung

Zeichnet man ein Dreieck zwischen zwei Klemmenpaaren, wird es zur __π-Schaltung__: zwei Querwiderstände und ein Längswiderstand, und der dritte Knoten ist
die gemeinsame untere Leitung (Bild 7.15 des Skripts). Ein Stern wird ebenso zur __T-Schaltung__ aus zwei Längswiderständen und einem Querwiderstand.

In der π-Schaltung liegt $R_1$ zwischen dem oberen Eingangsknoten und der unteren Leitung, $R_2$ zwischen den beiden oberen Knoten und $R_3$ zwischen dem
oberen Ausgangsknoten und der unteren Leitung. In der T-Schaltung sitzt $R'_1$ am Eingangsknoten, $R'_3$ am Ausgangsknoten und $R'_2$ an der unteren
Leitung. Dann gilt:

$$R'_1 = \frac{R_1\,R_2}{R_1 + R_2 + R_3}, \qquad R'_2 = \frac{R_1\,R_3}{R_1 + R_2 + R_3}, \qquad R'_3 = \frac{R_2\,R_3}{R_1 + R_2 + R_3}.$$

**So liest man das:** Es ist die Dreieck-Stern-Umwandlung, nur anders gezeichnet. Das Skript nennt Anwendungen in der Nachrichtentechnik: Ein
__Dämpfungsglied__ schwächt ein Signal um einen festen Faktor ab und soll an beiden Klemmenpaaren denselben Eingangswiderstand haben wie die Leitungen und
Geräte, an denen es hängt, damit dort __Leistungsanpassung__ herrscht, die größtmögliche Leistungsübertragung, ein Thema am Ende dieses Kapitels. Und
Filter aus Spulen und Kondensatoren lassen sich in π- und T-Form ineinander umrechnen.

**Im Bild:** Eine Ringleitung, deren eines Rohr am Boden entlangläuft, und ein Verteiler, dessen einer Arm zum Boden führt.

:::herleitung
**Zuordnen.** Die drei Knoten des Dreiecks sind der obere Eingangsknoten, der obere Ausgangsknoten und die untere Leitung. Am Eingangsknoten liegen $R_1$
und $R_2$ an, am Ausgangsknoten $R_2$ und $R_3$, an der unteren Leitung $R_1$ und $R_3$; der Umfangswiderstand ist die Summe aller drei. Die
Dreieck-Stern-Umwandlung liefert damit die drei Formeln.
:::

::::beispiel Ein Dämpfungsglied für 50 Ohm
Ein Dämpfungsglied für Leitungen mit $50\,\Omega$ soll die Spannung halbieren. In π-Form hat es die Werte

$$R_1 = R_3 = 150\,\Omega, \qquad R_2 = 37{,}5\,\Omega.$$

**In T-Form.** Der Umfangswiderstand ist $337{,}5\,\Omega$:

$$R'_1 = R'_3 = \frac{150\cdot37{,}5}{337{,}5}\,\Omega \approx 16{,}67\,\Omega, \qquad R'_2 = \frac{150\cdot150}{337{,}5}\,\Omega \approx 66{,}67\,\Omega.$$

**Probe am Eingang.** Mit $50\,\Omega$ am Ausgang liegt hinter $R'_1$ die Parallelschaltung aus $R'_2$ und der Reihe $R'_3$ plus Last; die π-Form gibt dasselbe:

$$R_\text{ein} = 16{,}67\,\Omega + 66{,}67\,\Omega \parallel 66{,}67\,\Omega = 50\,\Omega, \qquad R_\text{ein} = 150\,\Omega \parallel (37{,}5\,\Omega + 150\,\Omega \parallel 50\,\Omega) = 50\,\Omega.$$

**Die Spannung.** Am Mittelknoten der T-Schaltung liegen zwei Drittel der Eingangsspannung, an der Last davon drei Viertel:

$$\frac{U_2}{U_1} = \frac{33{,}33\,\Omega}{50\,\Omega}\cdot\frac{50\,\Omega}{66{,}67\,\Omega} = \frac23\cdot\frac34 = \frac12.$$

Das Glied halbiert die Spannung und belastet die Quelle genau wie eine Leitung mit $50\,\Omega$.

**Im Bild:** Ringleitung und Verteiler mit einem Arm zum Boden; von außen dieselbe Bremse für das durchfließende Wasser.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/04-stern-dreieck · Vorlage: stern-dreieck-umwandlung
Nach Bild 7.10 bis 7.12 und 7.13 des Skripts, an der Brücke der Beispiel-Seite: links die Brücke mit A oben (Knoten 1), B unten, $R_{12} = 10\,\Omega$ und
$R_{2B} = 26\,\Omega$ links, $R_{31} = 20\,\Omega$ und $R_{3B} = 12\,\Omega$ rechts, $R_{23} = 20\,\Omega$ als Brücke, das Dreieck 1, 2, 3 gestrichelt
hervorgehoben. Ein Knopf „umwandeln" lässt die drei Dreieckswiderstände schrumpfen und an ihrer Stelle einen Stern mit $R_{10} = 4\,\Omega$,
$R_{20} = 4\,\Omega$ und $R_{30} = 8\,\Omega$ um den Sternpunkt 0 wachsen; neben jedem Sternarm leuchten die beiden Anliegerwiderstände und der Umfang auf.
Danach fassen sich die Zweige zu $30\,\Omega \parallel 20\,\Omega$ und zu $16\,\Omega$ zusammen. Ein Regler legt $32\,\text{V}$ an; Anzeigen zeigen, dass die
Potenziale von 2 und 3 vor und nach der Umwandlung gleich sind ($20{,}8\,\text{V}$ und $14{,}4\,\text{V}$), die Ströme in den Ersatzwiderständen aber andere.
Kernaussage: Dreieck und Stern sind an den drei Knoten gleichwertig, innen nicht. (Rot = Dreieck und Stern, blau = Potenziale, orange = Anlieger und
Umfang, grau = übrige Widerstände, gestrichelt = umzuwandelndes Dreieck.)
:::

## Bedeutung und Ausblick

Gruppen, Symmetrie und die Stern-Dreieck-Umwandlung reichen für sehr viele Widerstandsnetze. Für Netze, die sich in der Ebene ohne Kreuzungen zeichnen
lassen, ist sogar bewiesen, dass sich jedes mit Reihe, Parallele und den beiden Umwandlungen auf einen einzigen Widerstand zwischen zwei Klemmen
zurückführen lässt (Satz von Epifanov, 1966). Der Sternpunkt ist dabei ein Beispiel für die Elimination eines Knotens: Ein Knoten mit beliebig vielen
Zweigen lässt sich stets durch ein Vieleck ersetzen, in dem jeder seiner Nachbarn mit jedem verbunden ist. Umgekehrt geht das ab vier Zweigen im
Allgemeinen nicht, weil das Vieleck mehr Widerstände hat als der Stern.

In der Wechselstromtechnik gelten beide Umwandlungen genauso, mit komplexen Widerständen; so vergleicht man Drehstromlasten im Stern und im Dreieck und
rechnet Filter zwischen π- und T-Form um. Bisher enthielten die Netze nur Widerstände. Der nächste Artikel bringt die Quellen hinzu: ideale und reale
Spannungs- und Stromquellen.

:::kern
- Gruppen fasst man von innen nach außen zusammen; im Kettenbruch wechseln sich Widerstände in Reihe und Leitwerte parallel ab.
- Zwischen Knoten gleichen Potenzials fließt kein Strom: Man darf sie verbinden oder den Widerstand zwischen ihnen entfernen.
- Bei einer Spiegelung, die die Klemmen vertauscht, liegen Knoten auf der Achse auf dem Mittelwert der Klemmenpotenziale.
- Dreieck → Stern: $R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}}$, Anlieger durch Umfang.
- Stern → Dreieck: $G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}}$, Anliegerleitwerte durch Leitwertsumme.
- Stern und Dreieck sind nur an den drei Knoten gleich; die Ströme in den Ersatzwiderständen sind andere.
- Bei drei gleichen Widerständen gilt $R_Y=R_\Delta/3$.
- π- und T-Schaltung sind Dreieck und Stern zwischen zwei Klemmenpaaren.
:::

:::quiz
F: Warum lässt sich eine Brückenschaltung nicht mit Reihe und Parallele zusammenfassen, und was hilft stattdessen?
A: Der Brückenwiderstand verbindet die beiden Mittelknoten so, dass kein Paar von Widerständen rein in Reihe oder rein parallel liegt. Helfen kann Symmetrie, wenn sie Knoten gleichen Potenzials verrät, oder die Stern-Dreieck-Umwandlung, nach der wieder Reihen- und Parallelgruppen entstehen; bei der Brücke mit $10$, $20$, $20$, $26$ und $12\,\Omega$ ergibt sie $16\,\Omega$.
F: Wie fasst man Gruppen zusammen, und was zeigt die Schreibweise als Kettenbruch?
A: Von innen nach außen: zuerst eine Gruppe, die rein in Reihe oder rein parallel liegt, dann die nächste. Im Kettenbruch wechseln sich Reihe (Widerstände addieren) und Parallele (Leitwerte addieren) mit Kehrwerten ab; der Kettenleiter mit $15$, $70$, $20\parallel20$ und $60\,\Omega$ ergibt so $15\,\Omega+70\,\Omega\parallel70\,\Omega=50\,\Omega$.
F: Warum darf man zwei Knoten gleichen Potenzials verbinden oder einen Widerstand zwischen ihnen entfernen?
A: Durch einen Widerstand zwischen gleichen Potenzialen fließt nach dem ohmschen Gesetz kein Strom; ohne ihn ändert sich keine Knotenregel. Mit einem Draht zwischen den Knoten erfüllt die alte Lösung mit dem Strom null im Draht alle Gleichungen des neuen Netzes, und wegen der Eindeutigkeit ist sie dessen Lösung.
F: Was folgt aus einer Spiegelsymmetrie, die die Klemmen A und B vertauscht, und warum?
A: Für jeden Knoten und seinen Spiegelpunkt ist $\varphi_P+\varphi_{P'}=\varphi_A+\varphi_B$; Knoten auf der Achse liegen auf dem Mittelwert. Denn die gespiegelte und am Mittelwert umgeklappte Lösung erfüllt dieselben Knotenregeln und Klemmenwerte, und die Lösung ist eindeutig.
F: Wie bestimmt man den Widerstand eines Würfels aus zwölf gleichen Widerständen über eine Flächendiagonale?
A: Die Spiegelebene zwischen den beiden Ecken enthält vier Ecken, die alle auf dem Mittelwert liegen und verbunden werden. Von jeder Ecke zu diesem Knoten liegen $R/2$ und $R+R/2$ parallel, also $\frac38R$; zweimal ergibt das $\frac34R$, mit $1\,\text{k}\Omega$ also $750\,\Omega$ und bei $6\,\text{V}$ $8\,\text{mA}$.
F: Wie lautet die Dreieck-Stern-Umwandlung, und wie leitet man sie her?
A: Sternwiderstand gleich Produkt der beiden Anliegerwiderstände geteilt durch den Umfangswiderstand, etwa $R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}}$. Man fordert, dass zwischen je zwei Knoten bei offenem drittem derselbe Widerstand liegt, addiert die drei Gleichungen und zieht eine ab.
F: Warum rechnet man die Stern-Dreieck-Umwandlung mit Leitwerten, und woraus folgt sie?
A: Aus der Knotenregel am Sternpunkt: Sein Potenzial ist das mit den Leitwerten gewichtete Mittel der drei Knotenpotenziale. Eingesetzt hat der Strom in Knoten 1 die Form eines Dreiecks mit $G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}}$, für beliebige Potenziale — so beweist diese Richtung die volle Gleichwertigkeit. In Widerständen ist $R_{12}=R_{10}+R_{20}+\frac{R_{10}R_{20}}{R_{30}}$.
F: Warum sind die Ströme in den Sternarmen nach einer Umwandlung nicht die Ströme der ursprünglichen Dreieckswiderstände?
A: Gleichwertig sind beide Schaltungen nur an ihren drei Knoten; erhalten bleiben deren Potenziale und die Ströme, die in sie hineinfließen. In der Brücke an $32\,\text{V}$ führt der Sternarm $R_{10}$ die vollen $2\,\text{A}$, während sie sich im Dreieck auf $1{,}12$ und $0{,}88\,\text{A}$ aufteilen; die wahren Ströme berechnet man aus den Potenzialen $20{,}8\,\text{V}$ und $14{,}4\,\text{V}$.
F: Was gilt bei drei gleichen Widerständen, und warum nehmen dieselben Widerstände im Dreieck dreimal so viel Strom auf wie im Stern?
A: Ein Dreieck aus $R_\Delta$ gleicht einem Stern aus $R_\Delta/3$. Im Stern haben dieselben Widerstände also den dreifachen Wert des gleichwertigen Sterns, und bei festen Potenzialen sinken alle Ströme auf ein Drittel: Drei mal $60\,\Omega$ an $12$, $0$ und $6\,\text{V}$ nehmen im Dreieck $3{,}6\,\text{W}$ auf, im Stern $1{,}2\,\text{W}$.
F: Was sind π- und T-Schaltung, und wozu rechnet man sie ineinander um?
A: Ein Dreieck und ein Stern zwischen zwei Klemmenpaaren, mit der unteren Leitung als drittem Knoten; die Umrechnung ist die Dreieck-Stern-Umwandlung. Ein Dämpfungsglied für $50\,\Omega$, das die Spannung halbiert, hat in π-Form $150$, $37{,}5$ und $150\,\Omega$, in T-Form $16{,}67$, $66{,}67$ und $16{,}67\,\Omega$; beide zeigen am Eingang $50\,\Omega$.
:::
