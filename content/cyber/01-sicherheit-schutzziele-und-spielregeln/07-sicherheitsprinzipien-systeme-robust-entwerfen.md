---
title: Sicherheitsprinzipien: Systeme robust entwerfen
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
order: 6110700
summary: Rechte richtig zu vergeben und zu prüfen genügt nicht, wenn der Mechanismus selbst Fehler hat.
tags: mehreren Verteidigungslinien, Produktzeichen, Einfachheit, vertrauenswürdige Basis, offenen Verfahrens, der Mensch als Teil des Systems, Sicherheit von Anfang an
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Rechte richtig zu vergeben und zu prüfen genügt nicht, wenn der Mechanismus selbst Fehler hat. Dieser Abschnitt behandelt die Grundsätze, die ein System als Ganzes widerstandsfähig machen, auch wenn einzelne Teile versagen.
:::

### Mehrere Verteidigungslinien

<span class="anker" id="stufe-6-1"></span>

Eine mittelalterliche Burg verließ sich nicht auf ihre Mauer allein. Vor der Mauer lag ein Graben, hinter dem Tor stand eine Wache, und der Schatz lag im innersten Turm. Wer hineinwollte, musste alle Hindernisse überwinden, nicht nur eines.

:::definition Definition 6.1 (Mehrere Verteidigungslinien)
<span class="anker" id="satz-6-1"></span>

Nach dem Prinzip der __mehreren Verteidigungslinien__ (englisch *defense in depth*, Verteidigung in der Tiefe) wird ein Schutzgut durch mehrere hintereinander liegende, voneinander unabhängige Mechanismen geschützt, sodass ein Angreifer alle überwinden muss.
:::

⁠**Rechenbeispiel: die Burg in Zahlen.** Ein Angreifer überwindet den Graben mit der Wahrscheinlichkeit $p_1=0{,}3$, die Mauer mit $p_2=0{,}1$ und die Wache mit $p_3=0{,}05$ (Abb. [12](#abb-12)). Sind die drei Hindernisse unabhängig, so kommt er nach der Produktregel [(3.2)](risiko-angreifermodell-und-angriffsflache.html#gl-3-2) mit der Wahrscheinlichkeit $0{,}0015$ bis zum Schatz (Abb. [13](#abb-13)), also in 1,5 von 1 000 Versuchen. Das beste einzelne Hindernis, die Wache, ließe ihn in 50 von 1 000 Versuchen durch. Für ein solches Produkt vieler Faktoren schreibt man kurz $\prod_{k=1}^{n}p_k=p_1\cdot p_2\cdots p_n$; das große griechische Pi heißt __Produktzeichen__ und ist für Produkte, was das Summenzeichen für Summen ist.

:::abbildung cyber/k1schichten 12
Drei Verteidigungslinien um ein Schutzgut. Sind sie unabhängig, multiplizieren sich die Wahrscheinlichkeiten, sie zu überwinden: Durch alle drei kommt ein Angreifer nur in 0,15 % der Fälle.
:::

:::abbildung cyber/k1rlinien 13
Die Wahrscheinlichkeit, alle drei unabhängigen Verteidigungslinien der Burg zu überwinden: das Produkt der drei Durchbruchswahrscheinlichkeiten.
:::

⁠**Beispiel: ein Online-Konto.** Das Passwort ist die erste Linie, die Bestätigung auf dem Handy die zweite. Eine Nachricht bei jeder Anmeldung von einem neuen Gerät ist eine dritte, die erkennt statt verhindert. Ein Tageslimit für Überweisungen ist eine vierte: Sie begrenzt den Schaden, wenn alle anderen versagt haben.

⁠**Kurz gesagt:** Mehrere unabhängige Linien hintereinander zwingen den Angreifer, alle zu überwinden; ihre Durchbruchswahrscheinlichkeiten multiplizieren sich.

:::hintergrund Wann mehrere Linien wirken und wann nicht
Die Rechnung oben setzt Unabhängigkeit voraus, und daran scheitern viele Systeme. Haben zwei Linien eine gemeinsame Ursache für ihr Versagen, so fallen sie zusammen. Benutzt jemand für das Firmennetz und für den Server dasselbe Passwort, so ist mit dem ersten Durchbruch auch der zweite geschafft: Die zweite Linie überwindet ein Angreifer dann nicht mit 0,1, sondern mit 1. Dasselbe gilt für zwei Schutzprogramme desselben Herstellers mit demselben Fehler.

In der Unfallforschung gibt es dafür ein bekanntes Bild, das Schweizer-Käse-Modell. Jede Schutzschicht ist eine Käsescheibe mit Löchern, und ein Unfall geschieht erst, wenn die Löcher mehrerer Scheiben zufällig in einer Linie liegen. Für die Sicherheit muss man das Bild an einer Stelle verschärfen: Ein Angreifer wartet nicht darauf, dass die Löcher zufällig übereinanderliegen. Er sucht gezielt einen Weg durch alle Scheiben, und wenn er in jeder Schicht ein Loch kennt, nützen ihm die Wahrscheinlichkeiten wenig. Mehrere Linien wirken deshalb vor allem dann, wenn sie *verschiedener Art* sind, etwa ein Passwort, ein Gerät in der Hand und eine Benachrichtigung, sodass ein einziges Wissen oder Werkzeug nicht alle überwindet.

Schließlich nimmt der Nutzen jeder weiteren Linie ab. Die vierte Linie halbiert vielleicht eine schon sehr kleine Wahrscheinlichkeit, kostet aber so viel wie die erste. Auch hier gilt der Grundsatz „Sicherheit ist Ökonomie“ aus Abschnitt [3](risiko-angreifermodell-und-angriffsflache.html#stufe-3).
:::

### Einfachheit

<span class="anker" id="stufe-6-2"></span>

Ein Türschloss mit einem Zylinder hat wenige Teile, und man kann jedes davon prüfen. Ein Schloss, das über eine App, einen Server des Herstellers und eine Funkverbindung geöffnet wird, hat sehr viel mehr, und jedes davon kann falsch sein.

:::definition Definition 6.2 (Einfachheit)
<span class="anker" id="satz-6-2"></span>

Nach dem Prinzip der __Einfachheit__ (englisch *economy of mechanism*) werden Sicherheitsmechanismen so einfach und so klein wie möglich gebaut.
:::

⁠**Rechenbeispiel:** Ein Mechanismus bestehe aus $n$ Bauteilen, und jedes enthalte unabhängig mit der Wahrscheinlichkeit $p=1\,\%$ einen Fehler, durch den man ihn umgehen kann. Nach [(3.3)](risiko-angreifermodell-und-angriffsflache.html#gl-3-3) hat er mit $n=3$ Bauteilen mit der Wahrscheinlichkeit $3{,}0\,\%$ mindestens einen solchen Fehler, mit $n=10$ Bauteilen mit $9{,}6\,\%$ (Abb. [14](#abb-14)). Jedes zusätzliche Teil ist eine zusätzliche Gelegenheit, wie bei der Angriffsfläche.

:::abbildung cyber/k1reinfach 14
Die Wahrscheinlichkeit, dass ein Mechanismus aus $3$ oder aus $10$ Bauteilen mindestens einen Fehler enthält, wenn jedes Teil unabhängig mit $p=0{,}01$ fehlerhaft ist.
:::

⁠**Kurz gesagt:** Sicherheitsmechanismen werden so einfach wie möglich gebaut, denn jedes Teil kann einen Fehler enthalten.

:::hintergrund Warum Sicherheitsfehler beim Testen nicht auffallen
Saltzer und Schroeder begründeten das Prinzip mit einer Beobachtung, die bis heute gilt. Ein gewöhnlicher Programmfehler fällt im Betrieb irgendwann auf: Eine falsche Rechnung wird reklamiert, ein Absturz wird gemeldet. Ein Fehler in einem Sicherheitsmechanismus dagegen öffnet einen unerwünschten Weg zu einem Schutzgut, und diesen Weg benutzt im Normalbetrieb niemand. Die berechtigten Nutzer tun ja nur, was sie dürfen; der Fehler bleibt unsichtbar, bis ein Angreifer ihn findet.

Deshalb kann man sich bei Sicherheitsmechanismen nicht darauf verlassen, dass Fehler durch Benutzung ans Licht kommen. Man muss den Mechanismus Zeile für Zeile durchgehen und gezielt nach Wegen suchen, die es nicht geben dürfte. Das gelingt nur, wenn der Mechanismus klein und einfach genug ist, dass ein Mensch ihn vollständig überblicken kann.
:::

### Eine kleine vertrauenswürdige Basis

<span class="anker" id="stufe-6-3"></span>

In einer Bankfiliale hängt die Sicherheit des Geldes am Tresor, an seinem Schloss und an den wenigen Angestellten mit Schlüssel. Ob die Stühle im Wartebereich bequem sind, spielt für die Sicherheit keine Rolle.

:::definition Definition 6.3 (Vertrauenswürdige Basis)
<span class="anker" id="satz-6-3"></span>

Die __vertrauenswürdige Basis__ (englisch *trusted computing base*, TCB) eines Systems besteht aus allen Teilen, auf deren korrektes Funktionieren die Sicherheit des Systems angewiesen ist. Ein guter Entwurf hält sie so klein wie möglich.
:::

Alles in der vertrauenswürdigen Basis muss stimmen; ein einziger Fehler darin kann die ganze Sicherheit aufheben. Alles außerhalb darf Fehler haben, ohne dass die Sicherheit leidet.

⁠**Beispiel:** Beim Kundenportal aus Abschnitt [2](von-der-schwachstelle-zum-schaden.html#stufe-2) gehören die Anmeldung und jede Stelle, die Rechte prüft, zur vertrauenswürdigen Basis. Prüfen 50 verschiedene Seiten des Portals jeweils selbst, ob der Kunde die angezeigten Daten sehen darf, so gehören alle 50 Prüfungen dazu, und jede kann falsch sein, wie die Rechnungsseite gezeigt hat. Prüft eine einzige zentrale Stelle jeden Zugriff, so gehört nur diese eine dazu. Die Basis ist kleiner, und die lückenlose Prüfung aus Abschnitt [5](sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5) lässt sich an einer Stelle sicherstellen.

⁠**Kurz gesagt:** Die vertrauenswürdige Basis ist alles, was für die Sicherheit korrekt sein muss; je kleiner sie ist, desto eher kann man sie prüfen.

:::hintergrund Warum die vertrauenswürdige Basis klein sein muss: der Referenzmonitor
Schon 1972 beschrieb eine Studie für die US-Luftwaffe, was der Teil eines Systems leisten muss, der über jeden Zugriff entscheidet. Sie nannte ihn *Referenzmonitor* und stellte drei Forderungen auf: Er muss gegen Veränderung geschützt sein, er muss bei jedem Zugriff aufgerufen werden, und er muss klein genug sein, um vollständig untersucht und getestet zu werden, sodass man sicher sein kann, dass er richtig arbeitet. Die zweite Forderung ist die lückenlose Prüfung aus Abschnitt [5](sicherheitsprinzipien-rechte-vergeben-und-prufen.html#stufe-5). Die dritte ist der Grund für eine kleine vertrauenswürdige Basis.

Rechnen lässt sich das mit der Formel [(3.3)](risiko-angreifermodell-und-angriffsflache.html#gl-3-3). Besteht die Basis aus $n$ Teilen, von denen jedes mit der Wahrscheinlichkeit $p$ einen Fehler hat, so ist sie mit der Wahrscheinlichkeit $1-(1-p)^n$ irgendwo fehlerhaft, und jeder Fehler in ihr kann die ganze Sicherheit aufheben. Fehler außerhalb der Basis zählen dagegen nicht mit. Für die Sicherheit kommt es deshalb nicht darauf an, wie groß das ganze System ist, sondern wie groß seine Basis ist. Ein großes Programm mit einer kleinen Basis kann sicherer sein als ein kleines, in dem jeder Teil über Zugriffe entscheidet.
:::

### Kein Verlass auf ein geheimes Verfahren

<span class="anker" id="stufe-6-4"></span>

Wie ein Türschloss funktioniert, steht in jedem Lehrbuch für Schlosser. Trotzdem schützt es, denn geheim ist nicht seine Bauart, sondern nur der Schlüssel. Geht der Schlüssel verloren, wechselt man den Zylinder, nicht die ganze Bauart.

:::definition Definition 6.4 (Offenes Verfahren)
<span class="anker" id="satz-6-4"></span>

Nach dem Prinzip des __offenen Verfahrens__ (englisch *open design*) muss ein System auch dann sicher bleiben, wenn der Angreifer seinen Aufbau vollständig kennt. Geheim bleiben darf nur ein kleines, austauschbares Geheimnis wie ein Passwort oder ein Schlüssel.
:::

Das Prinzip ist alt. Der Kryptograph Auguste Kerckhoffs forderte schon 1883, ein Verschlüsselungsverfahren dürfe keine Geheimhaltung verlangen und müsse ohne Nachteil in die Hände des Feindes fallen können. Claude Shannon fasste es 1949 in den Satz, man solle annehmen, „der Feind kennt das System“. Den umgekehrten Ansatz, Sicherheit durch Verbergen des Verfahrens, nennt man abschätzig *security through obscurity*.

⁠**Beispiel:** Ein Hersteller von Funkschlüsseln für Autos hält sein selbst erdachtes Verschlüsselungsverfahren geheim. Sobald jemand einen Schlüssel ausliest und das Verfahren herausfindet, sind alle Autos dieser Bauart zugleich gefährdet, und ändern lässt sich das Verfahren nur durch einen Austausch der Elektronik. Benutzt der Hersteller dagegen ein öffentlich bekanntes und gründlich geprüftes Verfahren mit einem eigenen Schlüssel je Auto, so verrät ein ausgelesener Schlüssel nur dieses eine Auto.

⁠**Kurz gesagt:** Die Sicherheit darf nur von einem kleinen, austauschbaren Geheimnis abhängen, nie davon, dass der Angreifer das Verfahren nicht kennt.

:::hintergrund Warum das Verfahren nicht geheim bleiben kann und soll
Saltzer und Schroeder gaben drei Gründe an. Erstens lässt sich ein Verfahren, das in vielen Geräten steckt, auf Dauer nicht geheim halten: Jedes verkaufte Gerät kann untersucht werden, und jeder Mitarbeiter, der das Verfahren kennt, kann es weitergeben. Zweitens können Fachleute ein offenes Verfahren prüfen, ohne dass die Prüfung selbst den Schutz schwächt; ein geheimes prüft nur sein Erfinder, und der übersieht leicht seine eigenen Fehler. Drittens kann jeder Nutzer selbst nachvollziehen, ob das Verfahren für seinen Zweck taugt.

Dahinter steht ein allgemeinerer Gedanke: Geheimnisse sollte man so wenige wie möglich haben, denn jedes Geheimnis kann verraten werden. Ein Schlüssel ist ein gutes Geheimnis, weil er klein ist und sich schnell austauschen lässt, wenn er doch bekannt wird. Ein Verfahren ist ein schlechtes Geheimnis, weil es groß ist und sein Austausch Jahre dauert. Ein guter Entwurf plant deshalb von Anfang an, was zu tun ist, wenn ein Geheimnis verraten wird.

Das Prinzip verbietet nicht, Einzelheiten für sich zu behalten. Wer den Aufbau seines Firmennetzes nicht veröffentlicht, macht einem Angreifer die Arbeit etwas schwerer. Er darf sich nur nicht darauf *verlassen*.
:::

### Der Mensch als Teil des Systems

<span class="anker" id="stufe-6-5"></span>

Die sicherste Tür nützt nichts, wenn sie mit einem Keil offen gehalten wird, weil das Aufschließen lästig ist.

:::definition Definition 6.5 (Der Mensch als Teil des Systems)
<span class="anker" id="satz-6-5"></span>

Nach dem Prinzip __der Mensch als Teil des Systems__ (englisch *consider human factors*) wird ein Sicherheitsmechanismus so entworfen, dass die Menschen, die ihn benutzen, ihn im Alltag richtig und ohne großen Aufwand anwenden. Der sichere Weg muss der bequeme sein.
:::

Menschen umgehen Regeln, die ihnen das Leben schwer machen, und Angreifer zielen bewusst auf Menschen, weil sie sich leichter täuschen lassen als Mechanismen. Phishing aus Abschnitt [1](was-geschutzt-wird-schutzgut-und-schutzziele.html#stufe-1) ist das bekannteste Beispiel.

⁠**Beispiel:** Eine Firma verlangt, dass alle Mitarbeiter ihr Passwort alle 30 Tage ändern. Die Mitarbeiter wählen daraufhin `Herbst2026!`, `Winter2026!`, `Fruehling2027!`: Passwörter, die ein Angreifer leicht errät, sobald er eines kennt. Die Richtlinien der US-Standardbehörde NIST verbieten einen solchen Zwangswechsel inzwischen ausdrücklich, solange es keinen Hinweis gibt, dass ein Passwort bekannt geworden ist. Ein einmal gewähltes langes Passwort zusammen mit einer Bestätigung auf dem Handy schützt mehr und belastet weniger.

⁠**Kurz gesagt:** Ein Mechanismus, den Menschen umgehen, schützt nicht; der sichere Weg muss der bequeme sein.

:::hintergrund Warum Menschen Sicherheitsregeln umgehen
Saltzer und Schroeder zählten das Prinzip 1975 zu ihren Grundsätzen und nannten es *psychologische Akzeptanz*: Die Bedienung muss so einfach sein, dass die Menschen die Schutzmechanismen ganz selbstverständlich und richtig anwenden, und die Mechanismen müssen zu dem passen, was die Menschen selbst schützen wollen. Passt beides zusammen, entstehen am wenigsten Fehler.

Warum es so oft nicht passt, wurde später untersucht. Eine Befragung von 1999 fand, dass der scheinbar sorglose Umgang mit Passwörtern vor allem aus zwei Gründen kam: aus der Art, wie die Mechanismen gebaut waren, und daraus, dass die Menschen nicht wussten, wogegen sie sich eigentlich schützen sollten. Wer sein Passwort ändern musste, hängte oft nur eine Zahl an, nach dem Muster `tom1`, `tom2`, `tom3`.

Daraus entstand ein Erklärungsmodell, das Bild eines Budgets: Jeder Mensch ist bereit, nur eine begrenzte Menge an Zeit und Mühe für Sicherheitsregeln aufzuwenden. Verlangen die Regeln mehr, lässt er die lästigsten weg, und das sind nicht unbedingt die unwichtigsten. Eine Organisation, die viele kleine Regeln aufstellt, verbraucht dieses Budget für Nebensachen, und für die wichtige Regel bleibt nichts übrig. Ein guter Entwurf fragt deshalb bei jeder Regel, was sie die Menschen kostet, und verlangt Aufwand nur dort, wo er viel Schutz bringt. Das Bild ist eine Vereinfachung: Wie groß das Budget ist, hängt von der Person und der Lage ab, und eine Organisation kann es beeinflussen, etwa indem sie erklärt, wozu eine Regel dient.
:::

### Sicherheit von Anfang an

<span class="anker" id="stufe-6-6"></span>

Ein Haus, das ohne Fundament gebaut wurde, bekommt man nachträglich kaum noch stabil. Mit Sicherheit ist es ähnlich.

:::definition Definition 6.6 (Sicherheit von Anfang an)
<span class="anker" id="satz-6-6"></span>

Nach dem Prinzip __Sicherheit von Anfang an__ (englisch *design security in from the start*) werden Sicherheitsanforderungen schon beim Entwurf eines Systems berücksichtigt und nicht nachträglich hinzugefügt.
:::

Nachträglich eingebaute Sicherheit ist teuer und lückenhaft, weil das alte System weiter funktionieren muss: Jede neue Prüfung darf nichts kaputtmachen, was sich auf das alte Verhalten verlässt.

⁠**Beispiel:** Das Verfahren, mit dem E-Mails zwischen Servern weitergereicht werden, wurde 1982 für ein Netz festgelegt, in dem sich die Beteiligten kannten. Es prüft nicht, ob der angegebene Absender stimmt; jeder Server kann jeden beliebigen Absender eintragen. Seit Jahrzehnten gibt es Ergänzungen, mit denen der Empfänger die Herkunft prüfen kann. Weil aber alte Server weiter Post zustellen können müssen, sind diese Prüfungen nicht überall eingeschaltet, und gefälschte Absender sind bis heute ein Werkzeug für Phishing.

⁠**Kurz gesagt:** Sicherheit wird von Anfang an mitentworfen, denn nachträglich lässt sie sich nur mühsam und unvollständig einbauen.

:::aufgabe Aufgabe 10 ★★ Wie viel bringen mehrere Linien?
<span class="anker" id="aufg-10"></span>

Ein Firmennetz hat drei Verteidigungslinien: einen Zugang aus dem Internet, der ein Passwort verlangt (ein Angreifer überwindet ihn mit der Wahrscheinlichkeit 0,1), die Anmeldung am Server mit einem weiteren Passwort (0,1) und eine Überwachung, die einen Eindringling bemerkt und aussperrt (sie übersieht ihn mit 0,05).

<ol class="al">

<li>

Mit welcher Wahrscheinlichkeit kommt ein Angreifer unbemerkt bis zu den Daten, wenn die drei Linien unabhängig sind?

</li>

<li>

Die Administratorin benutzt für den Zugang und für den Server dasselbe Passwort. Wie groß ist die Wahrscheinlichkeit jetzt? Um welchen Faktor ist das System schlechter geworden?

</li>

<li>

Statt des zweiten Passworts wird eine Bestätigung auf einem Hardware-Schlüssel eingeführt, den ein Angreifer mit der Wahrscheinlichkeit 0,5 überwindet. Ist das besser oder schlechter als (b)? Als (a)? Begründe mit dem Begriff der Unabhängigkeit.

</li>

</ol>

:::loesung
(a) Nach der Produktregel: $0{,}1\cdot0{,}1\cdot0{,}05=0{,}0005$, also 5 von 10 000 Versuchen.

(b) Wer das erste Passwort kennt, kennt auch das zweite. Die zweite Linie überwindet er also mit der Wahrscheinlichkeit 1: $0{,}1\cdot1\cdot0{,}05=0{,}005$. Das System ist um den Faktor 10 schlechter geworden, obwohl jede einzelne Linie gleich geblieben ist. Die beiden Linien haben eine gemeinsame Ursache für ihr Versagen und sind nicht mehr unabhängig.

(c) $0{,}1\cdot0{,}5\cdot0{,}05=0{,}0025$. Das ist halb so groß wie in (b) und damit besser, obwohl der Hardware-Schlüssel für sich genommen fünfmal so leicht zu überwinden ist wie ein Passwort mit 0,1. Der Grund: Er ist von der ersten Linie unabhängig, wer das Passwort kennt, hat deshalb noch nicht den Schlüssel. Gegenüber (a) ist es fünfmal schlechter, weil dort zwei unabhängige Linien mit je 0,1 standen. Am besten wäre ein Hardware-Schlüssel, der schwer zu überwinden *und* unabhängig ist.
:::
:::

:::aufgabe Aufgabe 11 ★★ Entwurfsentscheidungen beurteilen
<span class="anker" id="aufg-11"></span>

Nenne jeweils das Prinzip aus diesem Abschnitt, das betroffen ist, und beurteile die Entscheidung.

<ol class="al">

<li>

Ein Hersteller smarter Türschlösser wirbt: „Unser Funkprotokoll ist geheim, deshalb kann es niemand knacken.“

</li>

<li>

Eine Sicherheitssoftware für Firmennetze umfasst nach Angaben des Herstellers 40 Millionen Programmzeilen und läuft mit den höchsten Rechten des Systems.

</li>

<li>

Eine Webanwendung prüft die Rechte der Nutzer in jeder ihrer 120 Funktionen mit einer eigenen, jeweils leicht anders geschriebenen Abfrage.

</li>

<li>

Ein Krankenhaus verlangt am Stationsrechner für jeden Blick in eine Akte ein 16-stelliges Passwort. Die Pflegekräfte kleben einen Zettel mit dem Passwort an den Bildschirm.

</li>

</ol>

:::loesung
(a) *Offenes Verfahren.* Die Werbung verwechselt Geheimhaltung mit Sicherheit. Jedes verkaufte Schloss kann untersucht werden; sobald das Protokoll bekannt ist, sind alle Schlösser zugleich betroffen, und ändern lässt es sich nur durch neue Hardware. Ein öffentlich geprüftes Verfahren mit einem eigenen Schlüssel je Schloss wäre vorzuziehen.

(b) *Kleine vertrauenswürdige Basis* und *Einfachheit*. Weil die Software mit den höchsten Rechten läuft, gehören alle 40 Millionen Zeilen zur vertrauenswürdigen Basis. Nach [(3.3)](risiko-angreifermodell-und-angriffsflache.html#gl-3-3) ist bei so vielen Teilen fast sicher, dass irgendwo ein Fehler steckt, und dann hat ein Angreifer sofort die höchsten Rechte. Eine Sicherheitssoftware kann so selbst zur größten Angriffsfläche werden. Besser: nur ein kleiner Teil mit hohen Rechten, der Rest mit minimalen.

(c) *Kleine vertrauenswürdige Basis*, dazu Einfachheit. Alle 120 Abfragen gehören zur Basis, und jede kann einen eigenen Fehler haben. Besser: eine einzige zentrale Prüfung, die jede Funktion benutzt.

(d) *Der Mensch als Teil des Systems.* Die Regel ist für den Arbeitsalltag auf einer Station zu lästig und wird umgangen; der Zettel macht das Passwort für jeden Besucher sichtbar. Besser: eine schnelle Anmeldung, etwa mit Chipkarte und kurzer PIN, die die Arbeit nicht aufhält.
:::
:::
