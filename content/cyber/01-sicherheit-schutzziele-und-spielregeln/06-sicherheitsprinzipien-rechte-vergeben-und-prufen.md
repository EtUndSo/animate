---
title: Sicherheitsprinzipien: Rechte vergeben und prüfen
pfad: Informatik / Cybersecurity / Sicherheit, Schutzziele und Spielregeln
adresse: informatik/cybersecurity/sicherheit-schutzziele-und-spielregeln
knoten: Kapitel 1: Sicherheit, Schutzziele und Spielregeln
order: 6110600
summary: Wie baut man Mechanismen, die eine Richtlinie zuverlässig durchsetzen?
tags: Sicherheitsprinzip, minimalen Rechte, Aufgabentrennung, Zwei-Faktor-Anmeldung, sicheren Voreinstellung, lückenlosen Prüfung, TOCTTOU-Schwachstelle, atomar
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Wie baut man Mechanismen, die eine Richtlinie zuverlässig durchsetzen? Jahrzehnte an Erfahrung haben sich in wenigen Grundsätzen verdichtet. Dieser Abschnitt behandelt die Grundsätze dafür, wie man Rechte vergibt und wie man sie prüft.
:::

### Sicherheitsprinzipien

<span class="anker" id="stufe-5-1"></span>

Wer viele Sicherheitsvorfälle untersucht, sieht immer wieder dieselben Fehler. Aus dieser Erfahrung sind Grundsätze entstanden, an die sich gute Entwürfe halten.

:::definition Definition 5.1 (Sicherheitsprinzip)
<span class="anker" id="satz-5-1"></span>

Ein __Sicherheitsprinzip__ ist ein Grundsatz für den Entwurf von Sicherheitsmechanismen, der sich über viele Systeme hinweg bewährt hat.
:::

Sicherheitsprinzipien sind keine Gesetze, die man beweisen kann, sondern verdichtete Erfahrung. Mehrere von ihnen haben die Informatiker Jerome Saltzer und Michael Schroeder schon 1975 aufgeschrieben; sie gelten bis heute fast unverändert.

::::beispiel
Zwei Sicherheitsprinzipien kennst du schon. „Sicherheit ist Ökonomie“ aus Abschnitt [3](risiko-angreifermodell-und-angriffsflache.html#stufe-3) gilt für den Tresor einer Bank ebenso wie für die Bildschirmsperre eines Handys. „Erkennen, wenn man nicht verhindern kann“ aus Abschnitt [4](richtlinie-und-mechanismus.html#stufe-4) gilt für die Alarmanlage eines Hauses ebenso wie für die Nachricht der Bank bei einer neuen Anmeldung. Keines der beiden hängt von einer bestimmten Technik ab; das macht sie zu Prinzipien.
::::

⁠**Kurz gesagt:** Sicherheitsprinzipien sind bewährte Entwurfsgrundsätze, an denen man Mechanismen misst.

### Minimale Rechte

<span class="anker" id="stufe-5-2"></span>

Wie viele Rechte soll jemand bekommen? Der Handwerker, der die Heizung wartet, braucht den Schlüssel zum Heizungskeller, nicht den zum ganzen Haus.

:::definition Definition 5.2 (Minimale Rechte)
<span class="anker" id="satz-5-2"></span>

Nach dem Prinzip der __minimalen Rechte__ (englisch *least privilege*) erhält jede Person und jedes Programm genau die Rechte, die für die jeweilige Aufgabe nötig sind, und nur so lange, wie sie nötig sind.
:::

::::beispiel
Eine Praktikantin soll in einem Unternehmen die Ablage für ein einziges Projekt pflegen. Bekommt sie Zugriff auf alle 200 Projektordner, so liegen alle 200 offen, wenn ihr Konto durch Phishing in fremde Hände fällt. Bekommt sie Zugriff auf genau einen, liegt einer offen. Dieselbe Rechnung gilt für Programme: Eine Taschenlampen-App, die das Adressbuch lesen darf, verrät beim ersten Fehler das Adressbuch.
::::

⁠**Kurz gesagt:** Jeder bekommt nur die Rechte, die er für seine Aufgabe braucht, und nur so lange, wie er sie braucht.

:::hintergrund Warum minimale Rechte wirken
Das Prinzip begrenzt den Schaden, bevor er entsteht. Fehler, Versehen und übernommene Konten lassen sich nie ganz ausschließen. Was danach passiert, hängt allein davon ab, welche Rechte das betroffene Konto oder Programm hatte: Es kann nie mehr kaputtmachen, als es darf. Minimale Rechte wirken deshalb auch gegen Angriffe, die man nicht vorhergesehen hat.

Saltzer und Schroeder nannten einen zweiten Grund. Je weniger Programme und Personen weitreichende Rechte haben, desto weniger Wechselwirkungen zwischen ihnen gibt es, durch die ein Recht unbeabsichtigt missbraucht werden kann. Und wenn doch etwas passiert, muss man nur die wenigen untersuchen, die das betreffende Recht hatten. Bei Militär und Behörden heißt dieselbe Regel seit Langem „Kenntnis nur, wenn nötig“ (englisch *need to know*).
:::

### Aufgabentrennung

<span class="anker" id="stufe-5-3"></span>

Ein Bankschließfach hat zwei Schlösser. Den einen Schlüssel hat die Kundin, den anderen die Bank, und nur mit beiden zusammen geht es auf.

:::definition Definition 5.3 (Aufgabentrennung)
<span class="anker" id="satz-5-3"></span>

Nach dem Prinzip der __Aufgabentrennung__ (englisch *separation of privilege*, auch *separation of responsibility*) wird eine folgenreiche Handlung nicht schon erlaubt, wenn eine einzige Bedingung erfüllt ist. Sie verlangt mehrere voneinander unabhängige Bedingungen, zum Beispiel die Zustimmung zweier verschiedener Personen.
:::

::::beispiel [Rechenbeispiel]
In einem Unternehmen braucht jede Überweisung über 10 000 € die Freigabe durch zwei Personen aus verschiedenen Abteilungen. Ein Betrüger muss nun beide täuschen oder bestechen. Gelingt ihm das bei einer einzelnen Person mit der Wahrscheinlichkeit $q=1\,\%$, und sind die beiden unabhängig, so gelingt es bei beiden nach der Produktregel [(3.2)](risiko-angreifermodell-und-angriffsflache.html#gl-3-2) nur mit $q^2=0{,}01\,\%$, also hundertmal seltener (Abb. [10](#abb-10)).

:::abbildung cyber/k1rtrennung 10
Aufgabentrennung mit zwei unabhängigen Freigebenden, die je mit $q=0{,}01$ getäuscht werden: Beide zugleich täuscht der Betrüger nur mit dem Produkt $q^2$, hundertmal seltener als eine einzelne Person.
:::
::::

Dasselbe Prinzip steckt in der __Zwei-Faktor-Anmeldung__: Man meldet sich mit zwei voneinander unabhängigen Nachweisen an, zum Beispiel mit einem Passwort, das man weiß, und einem Handy, das man besitzt. Ein gestohlenes Passwort allein genügt dann nicht mehr.

⁠**Kurz gesagt:** Folgenreiche Handlungen verlangen mehrere unabhängige Bedingungen, sodass kein einzelner Fehler und kein einzelner Verrat ausreicht.

:::hintergrund Warum zwei Schlüssel mehr als doppelt so gut sind
Der Kern ist die Unabhängigkeit. Saltzer und Schroeder begründeten das Prinzip so: Sind die beiden Schlüssel erst einmal an verschiedene Personen, Programme oder Organisationen verteilt, so reicht kein einzelner Unfall, keine einzelne Täuschung und kein einzelner Vertrauensbruch mehr aus. Ein Angreifer muss zwei Dinge zugleich erreichen, und ihre Wahrscheinlichkeiten multiplizieren sich.

Diese Rechnung stimmt nur, solange die Bedingungen wirklich unabhängig sind. Sitzen die beiden Freigebenden im selben Büro und kennen sich gut, so kann einer den anderen überreden; dann ist die zweite Bedingung kaum noch etwas wert. Steht das Passwort auf einem Zettel in der Handyhülle, fallen beide Faktoren mit dem Diebstahl des Handys zugleich. Gute Aufgabentrennung achtet deshalb darauf, dass die Bedingungen keine gemeinsame Schwachstelle haben.
:::

### Sichere Voreinstellung

<span class="anker" id="stufe-5-4"></span>

Vor einem Club gibt es zwei Arten, den Einlass zu regeln. Bei der ersten hat der Türsteher eine Gästeliste: Herein kommt nur, wer draufsteht. Bei der zweiten hat er eine Liste mit Hausverboten: Herein kommt jeder, der nicht draufsteht.

:::definition Definition 5.4 (Sichere Voreinstellung)
<span class="anker" id="satz-5-4"></span>

Nach dem Prinzip der __sicheren Voreinstellung__ (englisch *fail-safe defaults*) ist jeder Zugriff verboten, solange er nicht ausdrücklich erlaubt ist. Außerdem soll ein System, wenn ein Mechanismus ausfällt oder eine Handlung abbricht, in einem sicheren Zustand enden.
:::

Die Gästeliste folgt dem Prinzip, die Liste mit Hausverboten nicht.

::::beispiel [Beispiele]
<ul>

<li>

Ein Router lehnt ab Werk jeden Verbindungsversuch aus dem Internet ab. Wer einen Dienst von außen erreichbar machen will, muss ihn ausdrücklich freigeben.

</li>

<li>

Bricht eine Überweisung mitten in der Verarbeitung ab, so wird sie vollständig zurückgenommen. Es entsteht kein Zustand, in dem das Geld vom einen Konto abgebucht, aber auf dem anderen nicht gutgeschrieben ist.

</li>

</ul>

Was ein „sicherer Zustand“ ist, hängt vom Schutzziel ab. Eine Tür zum Rechenzentrum soll bei Stromausfall verschlossen bleiben, damit niemand hineinkommt. Eine Notausgangstür muss bei Stromausfall aufgehen, damit niemand eingesperrt ist. Beide folgen dem Prinzip, nur für verschiedene Ziele.
::::

⁠**Kurz gesagt:** Was nicht ausdrücklich erlaubt ist, ist verboten, und bei einem Ausfall endet das System in einem sicheren Zustand.

:::hintergrund Warum die Gästeliste sicherer ist als die Verbotsliste
Saltzer und Schroeder begründeten das Prinzip mit der Frage, was passiert, wenn man einen Fehler macht. Fehler passieren in jedem großen System; irgendein Fall wird immer übersehen.

Bei der Gästeliste führt ein Fehler dazu, dass jemand *nicht* hereinkommt, der hereindürfte. Das fällt sofort auf: Die Person beschwert sich, und der Fehler wird korrigiert. Bei der Verbotsliste führt ein Fehler dazu, dass jemand hereinkommt, der nicht hereindürfte. Das fällt niemandem auf, denn wer unerlaubt hereinkommt, beschwert sich nicht. Ein erlaubnisbasierter Mechanismus scheitert also laut und sicher, ein verbotsbasierter leise und gefährlich.

Dazu kommt ein zweiter Grund. Wer eine Gästeliste schreibt, muss für jeden Zugriff begründen, warum er nötig ist. Wer eine Verbotsliste schreibt, muss alle Gefahren vorhersehen, auch die, die er nicht kennt. Das Erste ist viel leichter.
:::

### Lückenlose Prüfung

<span class="anker" id="stufe-5-5"></span>

In einem Hotel öffnet die Schlüsselkarte nicht nur den Haupteingang, sondern auch jede Zimmertür, und jede Tür prüft die Karte neu. Würde nur der Haupteingang prüfen, käme jeder Gast in jedes Zimmer.

:::definition Definition 5.5 (Lückenlose Prüfung)
<span class="anker" id="satz-5-5"></span>

Nach dem Prinzip der __lückenlosen Prüfung__ (englisch *complete mediation*) wird jeder Zugriff auf jedes Schutzgut darauf geprüft, ob er erlaubt ist, und zwar bei jedem Zugriff aufs Neue.
:::

::::beispiel
Das Kundenportal aus Abschnitt [2](von-der-schwachstelle-zum-schaden.html#stufe-2) prüft beim Anmelden, wer der Kunde ist. Beim Abruf einer Rechnung prüft es nur, ob die Nummer existiert, nicht, ob die Rechnung diesem Kunden gehört. Die Schwachstelle ist eine Lücke in der Prüfung: Die Tür am Eingang prüft, die Türen zu den einzelnen Rechnungen nicht. Lückenlos wäre: Bei jedem Abruf prüft das Portal, ob die verlangte Rechnung zum angemeldeten Kunden gehört.
::::

⁠**Kurz gesagt:** Jeder Zugriff wird geprüft, jedes Mal.

:::hintergrund Warum man ein Prüfergebnis nicht einfach aufheben darf
Prüfen kostet Zeit. Deshalb liegt es nahe, das Ergebnis einer Prüfung zu merken und beim nächsten Zugriff wiederzuverwenden: „Der durfte vorhin, also darf er jetzt auch.“ Saltzer und Schroeder warnten genau davor. Ein gemerktes Ergebnis beschreibt die Rechte von *damals*. Ändern sich die Rechte, etwa weil einer Mitarbeiterin gekündigt wurde, so gilt das gemerkte Ergebnis weiter, bis jemand es ausdrücklich erneuert. Wer Prüfergebnisse aufhebt, muss sie deshalb bei jeder Änderung der Rechte zuverlässig mitändern.

Das Prinzip verlangt außerdem, dass man bei jeder Anfrage sicher feststellen kann, von wem sie kommt. Eine Prüfung „darf diese Person das?“ ist wertlos, wenn sich jeder als diese Person ausgeben kann. Lückenlose Prüfung setzt also Authentizität voraus.
:::

### Prüfen und Handeln im selben Moment

<span class="anker" id="stufe-5-6"></span>

Eine Prüfung schützt nur, wenn ihr Ergebnis noch stimmt, wenn man danach handelt. Zwischen Prüfen und Handeln vergeht aber oft Zeit, und in dieser Zeit kann sich etwas ändern.

:::definition Definition 5.6 (TOCTTOU-Schwachstelle)
<span class="anker" id="satz-5-6"></span>

Eine __TOCTTOU-Schwachstelle__ (englisch *time of check to time of use*, „vom Zeitpunkt der Prüfung bis zum Zeitpunkt der Nutzung“) liegt vor, wenn ein System eine Bedingung prüft, danach eine Handlung ausführt, die auf dieser Bedingung beruht, und sich der geprüfte Zustand dazwischen ändern kann. Die Prüfung ist dann wertlos.
:::

::::beispiel zwei Geldautomaten
Auf einem Konto liegen 100 €, und zwei Karten gehören zu diesem Konto. An zwei Automaten wird fast gleichzeitig je 100 € abgehoben (Abb. [11](#abb-11)). Automat 1 prüft: $100\ge100$, in Ordnung. Bevor er abbucht, prüft Automat 2: Auch für ihn stehen noch 100 € auf dem Konto, in Ordnung. Dann zahlen beide aus und buchen ab. Ausgezahlt wurden 200 €, das Konto steht bei $-100$ €, obwohl jede einzelne Prüfung richtig war.

:::abbildung cyber/k1toctou 11
Eine TOCTTOU-Schwachstelle: Beide Automaten prüfen den Kontostand von 100 €, bevor einer von ihnen abbucht. Jede Prüfung ist für sich richtig, aber zum Zeitpunkt der Auszahlung schon veraltet. Am Ende sind 200 € ausgezahlt.
:::
::::

Die Abhilfe besteht darin, Prüfen und Handeln untrennbar zu verbinden. Eine Handlung heißt __atomar__, wenn sie entweder ganz oder gar nicht ausgeführt wird und niemand einen Zwischenstand sehen oder verändern kann. Im Beispiel muss „prüfen, ob der Stand reicht, und abbuchen“ eine einzige atomare Handlung sein: Solange Automat 1 prüft und abbucht, muss Automat 2 warten. Er sieht dann nur noch 0 € und lehnt ab.

⁠**Kurz gesagt:** Eine Prüfung schützt nur, wenn zwischen Prüfen und Handeln nichts den geprüften Zustand ändern kann; deshalb macht man beides zu einer atomaren Handlung.

:::hintergrund Warum diese Lücke in Rechnern so häufig ist
In einem Rechner laufen viele Vorgänge gleichzeitig: Mehrere Benutzer arbeiten an denselben Daten, mehrere Programme greifen auf dieselben Dateien zu, mehrere Anfragen erreichen denselben Server in derselben Millisekunde. Zwischen zwei Schritten eines Programms kann deshalb immer ein anderer Vorgang etwas ändern, und der Programmierer bemerkt das beim Testen nicht, weil die ungünstige Reihenfolge nur selten zufällig eintritt. Ein Angreifer dagegen kann sie absichtlich herbeiführen, indem er im passenden Moment eingreift oder tausende Anfragen gleichzeitig schickt; das ist wieder der Unterschied zwischen Zufall und Gegner aus Abschnitt [2](von-der-schwachstelle-zum-schaden.html#stufe-2).

Die TOCTTOU-Schwachstelle ist eng mit der lückenlosen Prüfung verwandt. Die Prüfung zum Zeitpunkt $t_1$ ist ein gemerktes Ergebnis, das zum Zeitpunkt $t_3$ benutzt wird. Lückenlos wäre die Prüfung erst, wenn sie im Moment der Handlung selbst gilt.
:::

:::aufgabe Aufgabe 8 ★★ Welches Prinzip ist verletzt?
<span class="anker" id="aufg-8"></span>

Nenne für jeden Fall das verletzte Prinzip und schlage eine bessere Lösung vor.

<ol class="al">

<li>

In einer Firma arbeiten alle Mitarbeiter mit Konten, die Programme installieren und die Einstellungen aller Rechner ändern dürfen, „damit niemand die IT-Abteilung anrufen muss“.

</li>

<li>

Eine Webanwendung blockiert Anfragen, in denen bestimmte gefährliche Zeichenfolgen vorkommen; alles andere lässt sie durch. Die Liste wird gepflegt, sobald ein neuer Angriff bekannt wird.

</li>

<li>

Ein Online-Speicherdienst prüft beim Öffnen eines geteilten Ordners, ob der Besucher eingeladen ist. Die Dateien im Ordner liefert er danach an jeden aus, der ihre Adresse kennt.

</li>

<li>

In einem kleinen Verein kann der Kassenwart allein Überweisungen beliebiger Höhe vom Vereinskonto auslösen.

</li>

<li>

Ein Mitarbeiter wechselt die Abteilung. Seine alten Zugriffsrechte behält er, weil „man sie vielleicht noch braucht“.

</li>

</ol>

:::loesung
(a) *Minimale Rechte.* Jedes Konto, das durch Phishing übernommen wird, kann sofort Schadprogramme installieren und alle Rechner verändern. Besser: Alltagskonten ohne Verwaltungsrechte; Installationen über ein eigenes Konto oder eine Freigabe durch die IT.

(b) *Sichere Voreinstellung.* Die Liste verbietet nur, was bekannt ist; jeder neue Angriff kommt durch, bis jemand die Liste ergänzt, und niemand bemerkt es. Besser: genau festlegen, welche Eingaben erlaubt sind, und alles andere ablehnen.

(c) *Lückenlose Prüfung.* Geprüft wird nur der Ordner, nicht jeder Zugriff auf jede Datei. Wer eine Dateiadresse kennt, etwa weil ein früher Eingeladener sie weitergegeben hat, kommt an die Datei. Besser: bei jedem Abruf einer Datei prüfen, ob der Anfragende dazu berechtigt ist.

(d) *Aufgabentrennung.* Ein einziger Fehler, eine Täuschung durch eine gefälschte Rechnung oder ein Vertrauensbruch genügt. Besser: Überweisungen ab einer Grenze nur mit Freigabe durch eine zweite Person.

(e) *Minimale Rechte*, und zwar der Teil „nur so lange, wie sie nötig sind“. Mit jedem Wechsel sammelt das Konto mehr Rechte an, und wird es übernommen, liegt mehr offen. Besser: Rechte beim Wechsel entziehen und für die neue Aufgabe neu vergeben.
:::
:::

:::aufgabe Aufgabe 9 ★★★ Ein Gutschein, zweimal eingelöst
<span class="anker" id="aufg-9"></span>

Ein Onlineshop gibt Gutscheincodes über 50 € aus, die jeweils nur einmal eingelöst werden dürfen. Beim Bezahlen läuft Folgendes ab: (1) Der Shop liest den Gutschein aus seiner Datenbank und prüft, ob er noch nicht eingelöst ist. (2) Er zieht 50 € vom Rechnungsbetrag ab. (3) Er trägt den Gutschein als eingelöst ein. Zwischen (1) und (3) vergehen etwa 200 ms.

<ol class="al">

<li>

Ein Kunde öffnet zwei Browserfenster mit je einer Bestellung und schickt in beiden fast gleichzeitig denselben Code ab. Beschreibe mit Zeitpunkten wie in Abbildung [11](#abb-11), was passieren kann.

</li>

<li>

Ein Angreifer schickt 20 Bestellungen innerhalb von 100 ms ab, jede mit demselben Code. Wie viel Rabatt erhält er im ungünstigsten Fall für den Shop?

</li>

<li>

Schlage zwei Abhilfen vor, die beide auf eine atomare Handlung hinauslaufen. Warum hilft es *nicht*, Schritt (1) einfach zweimal hintereinander auszuführen?

</li>

</ol>

:::loesung
(a) Ein möglicher Ablauf mit den Zeitpunkten $t_1<t_2<t_3<t_4$: Zu $t_1$ liest Fenster 1 den Gutschein: noch nicht eingelöst. Zu $t_2$ liest Fenster 2 denselben Gutschein: noch nicht eingelöst, denn Fenster 1 hat noch nichts eingetragen. Zu $t_3$ zieht Fenster 1 50 € ab und trägt den Gutschein als eingelöst ein. Zu $t_4$ zieht auch Fenster 2 50 € ab und trägt ihn ein zweites Mal als eingelöst ein. Beide Bestellungen haben den Rabatt; jede Prüfung war richtig, aber beim Abziehen veraltet. Das ist eine TOCTTOU-Schwachstelle.

(b) Alle 20 Anfragen kommen innerhalb von 100 ms an. Die erste trägt den Gutschein frühestens 200 ms nach ihrer eigenen Prüfung als eingelöst ein. Im ungünstigsten Fall haben bis dahin alle 20 Anfragen geprüft und den Gutschein für gültig befunden. Der Angreifer erhält dann $20\cdot50=1\,000$ € Rabatt statt 50 €.

(c) Zwei Abhilfen:

<ul>

<li>

⁠*Prüfen und Eintragen in einem Schritt.* Die Datenbank führt eine einzige Anweisung aus: „Setze den Gutschein auf eingelöst, aber nur, wenn er noch nicht eingelöst ist, und melde, ob das geklappt hat.“ Nur die Anfrage, bei der die Änderung gelingt, bekommt den Rabatt. Da die Datenbank diese Anweisung atomar ausführt, kann keine zweite dazwischenkommen.

</li>

<li>

⁠*Sperren.* Die Anfrage sperrt den Gutschein vor dem Prüfen und gibt ihn erst nach dem Eintragen wieder frei. Jede weitere Anfrage wartet, bis die Sperre aufgehoben ist, und sieht dann „eingelöst“.

</li>

</ul>

Zweimal zu prüfen hilft nicht, weil sich an der Lücke nichts ändert: Auch nach der zweiten Prüfung vergeht Zeit bis zum Eintragen, und in dieser Zeit können andere Anfragen ebenfalls zweimal erfolgreich prüfen. Die Lücke schließt sich erst, wenn zwischen Prüfen und Handeln nichts mehr passieren kann.
:::
:::
