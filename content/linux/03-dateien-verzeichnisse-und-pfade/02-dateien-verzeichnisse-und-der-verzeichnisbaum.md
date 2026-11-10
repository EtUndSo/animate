---
title: Dateien, Verzeichnisse und der Verzeichnisbaum
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080200
summary: Bevor man Befehle für Dateien lernt, braucht man ein Bild davon, was eine Datei ist und wie Linux viele Dateien ordnet.
tags: Datei, Verzeichnis, Verzeichnisbaum, Wurzelverzeichnis, übergeordnetes Verzeichnis, Unterverzeichnis
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man Befehle für Dateien lernt, braucht man ein Bild davon, was eine Datei ist und wie Linux viele Dateien ordnet. Dieser Abschnitt legt drei Grundbegriffe fest: die Datei, das Verzeichnis und den einen Baum, in dem alle Verzeichnisse hängen.
:::

:::::vorwissen Was du dafür brauchst: Shell, Befehl und aktueller Ordner

<span class="anker" id="stufe-1-1"></span>

Dieses Kapitel setzt [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) voraus. Daraus brauchst du vor allem fünf Dinge.

<ul>

<li>

Die Shell liest eine Befehlszeile und zerlegt sie an Leerzeichen in Wörter. Das erste Wort ist der Befehl, die übrigen sind Argumente; Argumente, die mit `-` beginnen, heißen Optionen ([Kapitel 2, Abschnitt 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2)).

</li>

<li>

Die Shell arbeitet immer in einem bestimmten Ordner, dem aktuellen Ordner. Die Eingabeaufforderung zeigt ihn an, `cd` wechselt ihn, und `cd` ohne Angabe führt in deinen persönlichen Ordner `/home/student`, den die Eingabeaufforderung mit `~` abkürzt ([Kapitel 2, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4)).

</li>

<li>

`cd` ist ein eingebauter Befehl der Shell, weil nur die Shell selbst ihren eigenen Ordner wechseln kann ([Kapitel 2, Abschnitt 3.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/arten-von-befehlen.html#stufe-3-3)).

</li>

<li>

Der Seitenanzeiger `less` zeigt langen Text seitenweise; die Leertaste blättert weiter, `q` beendet ihn ([Kapitel 2, Abschnitt 4.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/hilfe-finden.html#stufe-4-4)).

</li>

<li>

Die Tabulatortaste vervollständigt angefangene Befehle und Namen ([Kapitel 2, Abschnitt 5.1](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/schneller-arbeiten-vervollstandigung-verlauf-tastenkurzel.html#stufe-5-1)).

</li>

</ul>

Dazu kommt ein Begriff aus der Informatik. Ein *Byte* ist die kleinste Einheit, in der ein Rechner Daten speichert: acht Bit, also eine ganze Zahl von 0 bis 255 (ausführlich: [Python, Kapitel 2, Abschnitt 3.3](/wissen/informatik/programmieren/python/werte-typen-und-variablen/zahlen-im-binarsystem.html#stufe-3-3)).

::::beispiel Ein kurzer Test
Öffne ein Terminal und tippe `cat /etc/hostname`. Der Befehl `cat` zeigt den Inhalt dessen an, was als Argument folgt; [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) hat ihn schon benutzt. Die Antwort ist der Name deines Rechners, hier `labor`.

```console
$ cat /etc/hostname
labor
```
::::

⁠**Kurz gesagt:** Du brauchst die Shell, den Aufbau einer Befehlszeile, den aktuellen Ordner mit `cd`, den Seitenanzeiger und das Byte als Zahl von 0 bis 255.

:::::

### Die Datei

<span class="anker" id="stufe-1-2"></span>

Ein Rechner soll Dinge aufbewahren, auch wenn er ausgeschaltet ist: einen Brief, ein Urlaubsfoto, ein Programm. Dafür braucht es eine Einheit, die man ablegen, wiederfinden und öffnen kann.

**Eine Reihe von Zahlen mit einem Namen.** Man kann sich eine Datei wie einen Streifen Kästchen vorstellen, in jedem Kästchen eine Zahl von 0 bis 255, und auf dem Streifen klebt ein Namensschild. Abbildung [1](#abb-1) zeigt die Datei aus dem Beispiel oben so: sechs Kästchen, darunter die Buchstaben, für die die Zahlen stehen.

:::abbildung linux/k3bytes 1
Die Datei `/etc/hostname` als Folge von sechs Bytes. Jede Zahl steht für ein Zeichen: 108 für `l`, 97 für `a` und so weiter; die 10 am Ende markiert das Ende der Zeile. Das Namensschild gehört nicht zu den Bytes.
:::

:::definition Definition 1.1 (Datei)
<span class="anker" id="satz-1-1"></span>

Eine __Datei__ ist eine Folge von Bytes, die unter einem Namen dauerhaft gespeichert ist. Was die Bytes bedeuten, ob Text, Bild oder Programm, legt nicht das System fest, sondern das Programm, das die Datei liest.
:::

Für das Betriebssystem ist eine Datei also nur eine Reihe von Zahlen mit einer Länge. Ob sie einen Brief enthält oder ein Foto, merkt erst ein Programm, das die Zahlen auf seine Weise deutet: Ein Texteditor macht aus ihnen Buchstaben, ein Bildbetrachter Farbpunkte.

::::beispiel Die Bytes einer Datei
Der Befehl `od` (kurz für „octal dump“, Ausgabe in Zahlen) zeigt die Bytes einer Datei als Zahlen. Die Option `-An` lässt die Positionsangaben am Zeilenanfang weg, `-tu1` verlangt jedes Byte einzeln als Dezimalzahl:

```console
$ od -An -tu1 /etc/hostname
 108  97  98 111 114  10
```

Die Datei besteht aus genau sechs Bytes. Die ersten fünf sind die Zeichen `l`, `a`, `b`, `o`, `r`; jedes Zeichen ist als Zahl gespeichert, nach einer festen Tabelle. Die 10 am Ende ist kein sichtbares Zeichen, sondern das Zeichen für „hier endet eine Zeile“. `cat` hat dieselben sechs Bytes an das Terminal geschickt, und erst das Terminal hat daraus die Buchstaben `labor` und einen Zeilenumbruch gemacht.
::::

⁠**Kurz gesagt:** Eine Datei ist eine gespeicherte Folge von Bytes mit einem Namen; was die Bytes bedeuten, entscheidet das lesende Programm.

:::hintergrund Warum das System nicht weiß, was in einer Datei steht
Ein Betriebssystem könnte Dateien nach Art getrennt speichern, etwa Texte anders als Bilder. Unix, das Vorbild von Linux, hat sich in den frühen 1970er-Jahren bewusst dagegen entschieden: Eine Datei ist nur eine Folge von Bytes, ohne Aufbau, den das System kennen müsste. Die Aufgabe des Dateisystems ist allein, die Bytes dauerhaft zu speichern und beim nächsten Lesen genau dieselben Bytes zurückzugeben. Dadurch kommt jedes Programm mit jeder Datei zurecht: Ein Programm, das Bytes zählt oder kopiert, funktioniert für Briefe, Fotos und Programme gleichermaßen, ohne sie zu verstehen. Den Preis zahlt das lesende Programm: Es muss selbst erkennen, was es vor sich hat.
:::

### Das Verzeichnis

<span class="anker" id="stufe-1-3"></span>

Ein System mit Tausenden Dateien braucht Ordnung. In [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) hieß das Mittel dafür Ordner. Unter Linux ist der übliche Name Verzeichnis, und dieser Name verrät, wie es funktioniert.

**Eine Liste von Namen.** Ein Verzeichnis ist im Kern eine Liste, ähnlich dem Inhaltsverzeichnis eines Buchs: Links steht ein Name, rechts der Verweis auf das, was dazugehört (ein Bild zur Orientierung). Abbildung [2](#abb-2) zeigt das Verzeichnis `/usr` als solche Liste. Jeder Eintrag führt entweder zu einer Datei oder zu einem weiteren Verzeichnis, das wieder eine Liste ist.

:::abbildung linux/k3verzeichnis 2
Ein Verzeichnis als Liste von Einträgen. Jeder Eintrag verbindet einen Namen mit dem, was dazugehört; hier führt jeder Eintrag von `/usr` zu einem weiteren Verzeichnis, und der Eintrag `bin` öffnet seinerseits eine Liste, in der unter anderem die Datei `bash` steht.
:::

:::definition Definition 1.2 (Verzeichnis)
<span class="anker" id="satz-1-2"></span>

Ein __Verzeichnis__ ist eine Liste von Einträgen. Jeder Eintrag verbindet einen Namen mit einer Datei oder mit einem weiteren Verzeichnis.
:::

„Verzeichnis“ und „Ordner“ meinen dasselbe; das Kapitel sagt ab jetzt Verzeichnis. Was [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html) den aktuellen Ordner nannte, ist also ein Verzeichnis. Den Namen eines Eintrags nennt man auch einfach Dateinamen, selbst wenn er zu einem Verzeichnis führt.

::::beispiel Die Einträge von /usr
Der Befehl `ls` (kurz für „list“) zeigt die Namen, die in einem Verzeichnis eingetragen sind:

```console
$ ls /usr
bin  games  include  lib  lib64  libexec  local  sbin  share  src
```

Das Verzeichnis `/usr` enthält zehn Einträge. Ob dahinter Dateien oder Verzeichnisse stehen, verrät diese kurze Liste nicht.
::::

⁠**Kurz gesagt:** Ein Verzeichnis ist eine Liste, die Namen mit Dateien oder weiteren Verzeichnissen verbindet.

### Der Verzeichnisbaum und die Wurzel

<span class="anker" id="stufe-1-4"></span>

Weil ein Verzeichnis weitere Verzeichnisse enthalten kann, entstehen Ebenen über Ebenen. Damit man trotzdem jeden Ort eindeutig benennen kann, braucht die Ordnung einen festen Ausgangspunkt.

**Ein Baum, der nach unten wächst.** Man zeichnet die Verzeichnisse wie einen Stammbaum: oben ein einziges Verzeichnis, darunter die Verzeichnisse, die es enthält, darunter deren Inhalt. Abbildung [3](#abb-3) baut einen Ausschnitt dieses Baums Ebene für Ebene auf.

:::abbildung linux/k3baum 3
Der Verzeichnisbaum wächst von oben nach unten. Ganz oben steht das Wurzelverzeichnis `/`; jedes andere Verzeichnis hängt an genau einem Verzeichnis darüber. Gezeigt ist ein Ausschnitt mit `/etc`, `/home/student`, `/tmp` und `/usr` mit `bin`, `lib` und `share`. Zum Schluss ist `/usr` hervorgehoben: ein Pfeil nach oben zu `/`, drei Pfeile nach unten.
:::

:::definition Definition 1.3 (Verzeichnisbaum, Wurzelverzeichnis)
<span class="anker" id="satz-1-3"></span>

Die Verzeichnisse eines Linux-Systems bilden einen einzigen __Verzeichnisbaum__: Jedes Verzeichnis außer einem ist unter seinem Namen in genau einem anderen Verzeichnis eingetragen. Das eine Verzeichnis, das in keinem anderen steht, heißt __Wurzelverzeichnis__; man schreibt es als einzelnen Schrägstrich `/`.
:::

Zwei Wörter für die Lage im Baum kommen ständig vor. Das Verzeichnis, in dem ein anderes eingetragen ist, heißt sein __übergeordnetes Verzeichnis__. Umgekehrt ist jedes Verzeichnis, das in einem anderen eingetragen ist, ein __Unterverzeichnis__ davon. So ist `/usr` das übergeordnete Verzeichnis von `/usr/bin`, und `/usr/bin` ist ein Unterverzeichnis von `/usr`. Am Ende von Abbildung [3](#abb-3) zeigt der Pfeil nach oben zum übergeordneten Verzeichnis von `/usr`, die Pfeile nach unten zu seinen Unterverzeichnissen: Jedes Verzeichnis außer der Wurzel hat genau ein übergeordnetes, aber beliebig viele Unterverzeichnisse.

**Keine Laufwerksbuchstaben.** Windows gibt jedem Laufwerk einen eigenen Baum mit eigenem Anfang, `C:\` oder `D:\`. Linux hat genau einen Baum, egal wie viele Datenträger angeschlossen sind. Ein weiterer Datenträger bekommt keinen Buchstaben, sondern wird an ein Verzeichnis des Baums eingehängt; sein Inhalt erscheint dann unterhalb dieses Verzeichnisses ([Kapitel 1, Abschnitt 8.1](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/das-live-system.html#stufe-8-1)). Unter WSL 2 ist so das Windows-Laufwerk C: unter `/mnt/c` zu sehen ([Kapitel 1, Abschnitt 4.5](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-5)). Abbildung [4](#abb-4) stellt beide Ordnungen nebeneinander.

:::abbildung linux/k3laufwerke 4
Links Windows: zwei Laufwerke, zwei Bäume, jeder mit eigenem Buchstaben. Rechts Linux unter WSL 2: ein einziger Baum mit der Wurzel `/`; das Laufwerk C: hängt als Teilbaum unter `/mnt/c`.
:::

::::beispiel Die oberste Ebene
`ls /` zeigt die Einträge des Wurzelverzeichnisses:

```console
$ ls /
bin   dev  home  lib    lost+found  mnt  proc  run   snap  sys  usr
boot  etc  init  lib64  media       opt  root  sbin  srv   tmp  var
```

Das sind alle Verzeichnisse der obersten Ebene; jede Datei des Systems liegt irgendwo darunter. Kein Eintrag heißt C: oder D:. Den Eintrag `init` gibt es nur unter WSL.
::::

⁠**Kurz gesagt:** Alle Verzeichnisse hängen in einem einzigen Baum mit der Wurzel `/`; weitere Datenträger werden eingehängt, statt einen Buchstaben zu bekommen.

:::hintergrund Warum Linux einen einzigen Baum hat
Unix hat den einen Baum schon in den 1970er-Jahren eingeführt, und Linux hat ihn übernommen. Der Vorteil: Ein Ort im Baum hat immer denselben Namen, gleichgültig, auf welchem Datenträger er gerade liegt. Ein Programm, das seine Einstellungen in `/etc` sucht, muss nicht wissen, ob `/etc` auf der ersten oder zweiten Festplatte steht; die Verwalterin des Systems kann einen Teilbaum auf einen größeren Datenträger umziehen lassen, ohne dass sich ein einziger Name ändert. Mit Laufwerksbuchstaben wäre der Datenträger Teil jedes Namens, und ein Umzug würde alle Angaben ungültig machen, die ihn enthalten. Windows hat seine Buchstaben von MS-DOS geerbt, aus der Zeit der Diskettenlaufwerke A: und B:. Auch Windows kann übrigens einen Datenträger an einen Ordner hängen statt an einen Buchstaben, doch üblich ist das dort nicht.
:::

### Aufgaben zu Abschnitt [1](#stufe-1)

<span class="anker" id="stufe-1-5"></span>

:::aufgabe Aufgabe 1 ★ Datei, Verzeichnis oder keins von beiden?
<span class="anker" id="aufg-1"></span>

Ordne zu: (a) ein Urlaubsfoto, (b) die Liste der Namen in `/usr`, (c) das Wurzelverzeichnis, (d) der Name `hostname`, (e) das Programm `bash`, (f) das Laufwerk C: unter Windows. Begründe jeweils in einem Satz.

:::loesung
(a) Eine Datei: Das Foto ist eine gespeicherte Folge von Bytes mit einem Namen; erst ein Bildbetrachter macht aus den Bytes Farbpunkte.

(b) Ein Verzeichnis, genauer sein Inhalt: Die Liste der Namen mit ihren Verweisen ist genau das, was ein Verzeichnis ausmacht.

(c) Ein Verzeichnis, nämlich das einzige, das in keinem anderen eingetragen ist.

(d) Keins von beiden: `hostname` ist ein Name, also ein Eintrag im Verzeichnis `/etc`. Er führt zu einer Datei, ist aber nicht die Datei selbst.

(e) Eine Datei: Ein Programm ist eine Folge von Bytes, die der Prozessor als Befehle ausführen kann.

(f) Keins von beiden: C: ist unter Windows ein Laufwerk mit einem eigenen Baum. Unter Linux gibt es so etwas nicht; unter WSL 2 erscheint das Laufwerk als Teilbaum unter dem Verzeichnis `/mnt/c`.
:::
:::

:::aufgabe Aufgabe 2 ★★ Bytes vorhersagen
<span class="anker" id="aufg-2"></span>

Die Datei `/etc/timezone` nennt die Zeitzone deines Rechners, auf dem Testrechner `Europe/Berlin`. (a) Zeige ihren Inhalt mit `cat`. (b) Sage voraus, aus wie vielen Bytes sie besteht und welches Byte am Ende steht. (c) Prüfe mit `od -An -tu1 /etc/timezone`. Welche Zahl gehört zum Schrägstrich?

:::loesung
(a) `cat /etc/timezone` zeigt `Europe/Berlin`. (b) `Europe/Berlin` hat 13 Zeichen, jedes ein Byte; dazu kommt das Zeilenende. Vorhersage: 14 Bytes, das letzte ist die 10. (c) Die Probe:

```console
$ od -An -tu1 /etc/timezone
  69 117 114 111 112 101  47  66 101 114 108 105 110  10
```

14 Zahlen, die letzte ist 10. Der Schrägstrich steht an siebter Stelle zwischen `Europe` und `Berlin`; er ist die 47. Steht auf deinem Rechner eine andere Zeitzone, zählst du ihre Zeichen und addierst 1.
:::
:::

:::aufgabe Aufgabe 3 ★ Ein Stück Baum zeichnen
<span class="anker" id="aufg-3"></span>

Führe `ls /`, `ls /usr` und `ls /home` aus und zeichne daraus einen Ausschnitt des Verzeichnisbaums mit drei Ebenen. Markiere das Wurzelverzeichnis, ein übergeordnetes Verzeichnis und eines seiner Unterverzeichnisse.

:::loesung
Ein möglicher Ausschnitt mit drei Ebenen, eingerückt statt gezeichnet:

```text
/                  <- Wurzelverzeichnis
    home
        student
    usr            <- uebergeordnetes Verzeichnis von bin
        bin        <- Unterverzeichnis von usr
        share
        lib
    etc
    tmp
```

In der Zeichnung steht `/` oben, jedes Verzeichnis hängt an genau einem darüber. `/usr` ist das übergeordnete Verzeichnis von `/usr/bin`, und `/usr/bin` ist ein Unterverzeichnis von `/usr`. Ebenso ist `/home` das übergeordnete Verzeichnis von `/home/student`.
:::
:::
