---
title: Ausgaben umleiten
pfad: Informatik / Linux und Kommandozeile / Ströme, Umleitung, Pipes und Exit-Status
adresse: informatik/linux-und-kommandozeile/strome-umleitung-pipes-und-exit-status
knoten: Kapitel 4: Ströme, Umleitung, Pipes und Exit-Status
order: 6090300
summary: Bisher landete jede Ausgabe auf dem Bildschirm.
tags: Umleitung, Anhängen, Kopie
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Bisher landete jede Ausgabe auf dem Bildschirm. Dieser Abschnitt zeigt, wie man die Shell anweist, die Standardausgabe und die Standardfehlerausgabe eines Programms stattdessen in Dateien zu lenken, an Dateien anzuhängen oder wegzuwerfen, warum dabei die Reihenfolge zählt und welche Falle beim Umlenken in die Datei lauert, die man gerade liest.
:::

:::warnung Nur im eigenen Übungsverzeichnis
Die Befehle dieses und der folgenden Abschnitte legen Dateien an und überschreiben sie ohne Rückfrage. Lege dir deshalb ein eigenes Übungsverzeichnis an und arbeite nur dort:

```console
$ mkdir ~/linuxk4
$ cd ~/linuxk4
```

Alle Dateinamen in den Beispielen beziehen sich auf dieses Verzeichnis. Schreibe nie mit `>` in eine Datei, deren Inhalt du nicht verlieren willst.
:::

### Die Umleitung der Ausgabe: >

<span class="anker" id="stufe-2-1"></span>

Manches Ergebnis will man aufheben, statt es nur vorbeiziehen zu sehen: eine Liste von Dateien, eine Einkaufsliste, ein Protokoll. Dazu müsste die Standardausgabe statt zum Terminal zu einer Datei führen.

Genau das kann die Shell einrichten. Im Bild der Rohre aus Abbildung [4](prozesse-und-ihre-drei-strome.html#abb-4) gesprochen: Bevor sie das Programm startet, zieht sie das Rohr der Standardausgabe vom Bildschirm ab und steckt es an eine Datei. Das Programm schreibt wie immer in Deskriptor 1; es merkt nicht, dass die Bytes jetzt in einer Datei landen. Abbildung [6](#abb-6) zeigt den Vorgang.

:::abbildung linux/k4umleitung 6
Die Umleitung `ls /usr > inhalt.txt`: Die Shell verbindet Deskriptor 1 des neuen Prozesses mit der Datei `inhalt.txt` statt mit dem Bildschirm, erst dann startet `ls`. Die Namen fließen in die Datei; am Bildschirm erscheint nichts.
:::

:::definition Definition 2.1 (Umleitung, Umleitung der Ausgabe)
<span class="anker" id="satz-2-1"></span>

Eine __Umleitung__ ist eine Anweisung an die Shell, einen Deskriptor des neuen Prozesses vor dem Programmstart mit einer anderen Datei zu verbinden. Die Schreibweise `befehl > datei` verbindet die Standardausgabe mit der Datei `datei`. Gibt es die Datei noch nicht, legt die Shell sie an; gibt es sie schon, macht die Shell sie vorher leer.
:::

Die Zeichen `> datei` sind keine Argumente des Programms. Die Shell wertet sie aus und entfernt sie aus der Befehlszeile, bevor sie das Programm startet; das Programm bekommt nur die übrigen Wörter. Leerzeichen um das Zeichen `>` sind erlaubt, aber nicht nötig.

::::beispiel Den Inhalt von /usr aufheben
```console
$ ls /usr > inhalt.txt
$ cat inhalt.txt
bin
games
include
lib
lib64
libexec
local
sbin
share
src
```

Nach dem ersten Befehl erscheint nichts, denn alles ging in die Datei. In einer Datei stehen die Namen untereinander, je einer pro Zeile; nebeneinander in Spalten setzt `ls` sie nur, wenn es direkt in ein Terminal schreibt.
::::

::::beispiel [Zweites Beispiel] echo bekommt die Umleitung nicht zu sehen
```console
$ echo Hallo > gruss.txt
$ cat gruss.txt
Hallo
```

In der Datei steht nur `Hallo`. `echo` hat als einziges Argument `Hallo` bekommen; von `> gruss.txt` weiß es nichts.
::::

In [Kapitel 3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-verzeichnisse-und-pfade.html) brauchte man für eine Datei mit Inhalt den Editor `nano`. Mit einer Umleitung genügt `cat`: Ohne Argument liest es die Tastatur, und seine Standardausgabe geht in die Datei. So entsteht die Einkaufsliste, mit der die folgenden Abschnitte arbeiten. Tippe `cat > einkauf.txt`, dann die vier Zeilen `Milch`, `Brot`, `Äpfel`, `Kaffee` und zum Schluss Strg+D:

```console
$ cat > einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
$ wc -c einkauf.txt
25 einkauf.txt
```

Diesmal erscheint jede Zeile nur einmal, nämlich beim Tippen; was `cat` schreibt, geht in die Datei. Die Liste hat 25 Bytes, so wie die mit `nano` geschriebene in [Kapitel 3, Abschnitt 5.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-und-verzeichnisse-anlegen.html#stufe-5-3): vier Zeilen mit ihren Zeilenenden und ein Umlaut, der zwei Bytes belegt.

Eine Umleitung ohne Befehl macht eine Datei leer oder legt eine leere Datei an:

```console
$ > leer.txt
$ wc -c leer.txt
0 leer.txt
```

⁠**Kurz gesagt:** `befehl > datei` schickt die Standardausgabe in eine Datei, die die Shell vorher anlegt oder leert; das Programm merkt davon nichts.

:::warnung > überschreibt ohne Rückfrage
Gibt es die Datei schon, ist ihr alter Inhalt weg, sobald die Shell die Umleitung einrichtet. Eine Rückfrage gibt es nicht. Probiere es an einer Kopie aus:

```console
$ cp einkauf.txt probe.txt
$ echo Tee > probe.txt
$ cat probe.txt
Tee
```

Von der Einkaufsliste in `probe.txt` ist nichts übrig. Wer statt `probe.txt` den Namen einer wichtigen Datei tippt, verliert sie.
:::

:::hintergrund Wie die Shell eine Umleitung einrichtet
Die Shell braucht für jedes Programm einen neuen Prozess, und sie richtet die Umleitung in genau dem Augenblick ein, in dem es diesen Prozess schon gibt, das neue Programm aber noch nicht darin läuft. Die entscheidenden Schritte sind drei Systemaufrufe:

<ol>

<li>

Mit `fork` legt der Kernel eine fast genaue Kopie des Shell-Prozesses an, mit eigener Nummer. Die Kopie erbt die geöffneten Deskriptoren, also auch 0, 1 und 2 auf dem Terminal.

</li>

<li>

In der Kopie öffnet die Shell die Zieldatei, bei `>` mit der Anweisung, sie leer zu machen; die Datei bekommt die kleinste freie Nummer, etwa 3. Dann legt sie diese Datei mit dem Systemaufruf `dup2` auf Deskriptor 1 und schließt die 3 wieder. Jetzt führt Deskriptor 1 der Kopie zur Datei, Deskriptor 1 der eigentlichen Shell weiter zum Terminal.

</li>

<li>

Mit `exec` lädt die Kopie das gewünschte Programm, etwa `ls`, an Stelle des Shell-Codes. Die geöffneten Deskriptoren bleiben dabei erhalten. `ls` beginnt zu laufen, schreibt wie immer in Deskriptor 1, und die Bytes landen in der Datei.

</li>

</ol>

Die eigentliche Shell wartet unterdessen, bis der neue Prozess endet. Dass Unix das Erzeugen eines Prozesses (`fork`) und das Laden eines Programms (`exec`) in zwei Schritte trennt, ist genau für solche Fälle gedacht: Zwischen den beiden Schritten kann die Shell einrichten, womit das künftige Programm startet, etwa wohin seine Deskriptoren führen, ohne dass das Programm dafür eine einzige Zeile Code braucht. Und weil für ein Programm ein Terminal und eine Datei gleich aussehen (Unterabschnitt [1.7](prozesse-und-ihre-drei-strome.html#stufe-1-7)), funktioniert die Umleitung mit jedem Programm.
:::

:::hintergrund Ein Schutz gegen versehentliches Überschreiben
Die Shell kann sich weigern, mit `>` eine vorhandene Datei zu überschreiben. Der Befehl `set -o noclobber` schaltet diese Einstellung für die laufende Sitzung ein, `set +o noclobber` wieder aus. Wer dann doch überschreiben will, schreibt `>|` statt `>`:

```console
$ set -o noclobber
$ echo Tee > probe.txt
bash: probe.txt: cannot overwrite existing file
$ echo Tee >| probe.txt
$ set +o noclobber
```

Die Meldung kommt von der Shell selbst: `echo` ist gar nicht erst gelaufen.
:::

### Das Anhängen: >>

<span class="anker" id="stufe-2-2"></span>

Eine Einkaufsliste wächst, ein Protokoll bekommt jeden Tag neue Zeilen. Dabei soll der alte Inhalt bleiben und das Neue hinten dazukommen. Mit `>` geht das nicht, denn es leert die Datei zuerst. Abbildung [7](#abb-7) stellt beide Arten nebeneinander.

:::abbildung linux/k4anhaengen 7
Dieselbe Datei mit vier Zeilen, zweimal beschrieben. Oben mit `>`: Die alten Zeilen verschwinden, bevor die neue Zeile ankommt. Unten mit `>>`: Die alten Zeilen bleiben, die neue kommt ans Ende.
:::

:::definition Definition 2.2 (Anhängen)
<span class="anker" id="satz-2-2"></span>

Die Schreibweise `befehl >> datei` verbindet die Standardausgabe zum __Anhängen__ mit der Datei: Jedes geschriebene Byte kommt hinter den bisherigen Inhalt, und nichts wird gelöscht. Gibt es die Datei nicht, legt die Shell sie an.
:::

Die Einkaufsliste bekommt so eine fünfte Zeile:

```console
$ echo Butter >> einkauf.txt
$ cat einkauf.txt
Milch
Brot
Äpfel
Kaffee
Butter
```

Die vier alten Zeilen sind geblieben, `Butter` steht darunter. Die Datei hat jetzt 32 Bytes, sieben mehr: sechs Buchstaben und ein Zeilenende.

⁠**Kurz gesagt:** `>>` hängt die Standardausgabe an eine Datei an, ohne den alten Inhalt anzutasten.

### Die Umleitung der Fehlerausgabe: 2>

<span class="anker" id="stufe-2-3"></span>

Manchmal will man die Meldungen eines Programms für später festhalten, etwa um nachzusehen, was schiefging, oder man will sie vom Bildschirm fernhalten. Dazu muss man der Shell sagen können, welchen Ausgang sie umstecken soll.

:::definition Definition 2.3 (Umleitung der Fehlerausgabe)
<span class="anker" id="satz-2-3"></span>

Vor `>` und `>>` darf die Nummer eines Deskriptors stehen, ohne Leerzeichen dazwischen. `befehl 2> datei` leitet die Standardfehlerausgabe in die Datei, `befehl 2>> datei` hängt sie daran an. Ohne Nummer gilt die 1: `>` bedeutet dasselbe wie `1>`.
:::

::::beispiel Die Meldung in eine eigene Datei
```console
$ ls /etc/hostname /gibtsnicht 2> fehler.txt
/etc/hostname
$ cat fehler.txt
ls: cannot access '/gibtsnicht': No such file or directory
```

Am Bildschirm steht nur noch das Ergebnis, die Meldung ging in die Datei. Damit ist auch bewiesen, was Unterabschnitt [1.6](prozesse-und-ihre-drei-strome.html#stufe-1-6) behauptet hat: Die beiden Zeilen kamen durch verschiedene Ausgänge.
::::

⁠**Kurz gesagt:** `2>` leitet die Standardfehlerausgabe um; eine Zahl vor `>` wählt den Deskriptor.

### Die Datei, die alles schluckt: /dev/null

<span class="anker" id="stufe-2-4"></span>

Oft will man eine Ausgabe nicht aufheben, sondern einfach loswerden: Meldungen, die man schon kennt, oder Ergebnisse, die man nicht braucht. Eine Datei dafür anzulegen und wieder zu löschen wäre umständlich. Abbildung [8](#abb-8) zeigt, wohin die Fehlerausgabe stattdessen gehen kann.

:::abbildung linux/k4zweidateien 8
Zwei Ziele für die Fehlerausgabe. Links: Die Standardausgabe führt in `aus.txt`, die Standardfehlerausgabe in `fehler.txt`; jede Zeile landet in ihrer Datei. Rechts: Die Standardfehlerausgabe führt nach `/dev/null`, und die Meldungen verschwinden.
:::

Das Ziel ist die Gerätedatei `/dev/null` aus [Kapitel 3, Abschnitt 7.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/die-verzeichnisstruktur-von-linux.html#stufe-7-7): Sie nimmt alles an, was man hineinschreibt, und verwirft es; wer aus ihr liest, erreicht sofort das Ende des Stroms, `cat /dev/null` gibt deshalb nichts aus.

:::definition Definition 2.4 (Ausgabe verwerfen)
<span class="anker" id="satz-2-4"></span>

`befehl 2> /dev/null` verwirft die Meldungen eines Programms, `befehl > /dev/null` seine Ergebnisse. Das Programm merkt nichts davon: Jeder Schreibauftrag gelingt.
:::

::::beispiel Meldungen ausblenden
`find` durchsucht `/etc` nach Einträgen mit dem Namen `hostname` ([Kapitel 3, Abschnitt 10.1](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/dateien-finden-und-platz-messen.html#stufe-10-1)). Einige Verzeichnisse darf ein gewöhnlicher Benutzer nicht lesen; warum, spielt hier keine Rolle. `find` meldet jedes davon:

```console
$ find /etc -name hostname
/etc/apparmor.d/hostname
find: ‘/etc/credstore’: Permission denied
find: ‘/etc/credstore.encrypted’: Permission denied
/etc/hostname
find: ‘/etc/polkit-1/rules.d’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
$ find /etc -name hostname 2> /dev/null
/etc/apparmor.d/hostname
/etc/hostname
```

Die Meldungen über die verschlossenen Verzeichnisse verschwinden, die beiden Treffer bleiben. Die Treffer stehen jetzt auch nicht mehr zwischen den Meldungen versteckt.
::::

⁠**Kurz gesagt:** `/dev/null` verschluckt alles, was man hineinschreibt; `2> /dev/null` blendet Meldungen aus.

### Einen Deskriptor kopieren: 2>&1 und &>

<span class="anker" id="stufe-2-5"></span>

Für ein vollständiges Protokoll sollen Ergebnisse und Meldungen in dieselbe Datei, und zwar in der Reihenfolge, in der sie entstehen. Zweimal dieselbe Datei mit `>` zu öffnen, ginge schief, denn dann schrieben zwei Deskriptoren unabhängig voneinander an den Anfang der Datei und überschrieben sich gegenseitig. Stattdessen soll Deskriptor 2 einfach dorthin führen, wohin Deskriptor 1 schon führt.

:::definition Definition 2.5 (Deskriptor kopieren)
<span class="anker" id="satz-2-5"></span>

Die Schreibweise `n>&m` macht Deskriptor $n$ zu einer __Kopie__ von Deskriptor $m$: Danach führt $n$ zu derselben geöffneten Datei wie $m$ in diesem Augenblick. `2>&1` bedeutet also: Die Standardfehlerausgabe soll dorthin führen, wohin die Standardausgabe gerade führt. Ohne Zahl vor dem Zeichen gilt wieder die 1: `>&2` macht die Standardausgabe zu einer Kopie der Standardfehlerausgabe.
:::

Das Zeichen `&` sagt der Shell, dass hinter `>` die Nummer eines Deskriptors steht und kein Dateiname. Für den häufigsten Fall, beide Ausgänge in eine Datei, kennt bash eine Kurzform: `befehl &> datei` bedeutet dasselbe wie `befehl > datei 2>&1`, und `befehl &>> datei` hängt beides an. Die Kurzform verstehen nicht alle Shells, die lange Form dagegen jede.

::::beispiel Ergebnis und Meldung in einer Datei
```console
$ ls /etc/hostname /gibtsnicht > alles.txt 2>&1
$ cat alles.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
$ ls /etc/hostname /gibtsnicht &> beides.txt
$ cat beides.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
```

Am Bildschirm erscheint bei beiden Aufrufen nichts. Beide Dateien enthalten beide Zeilen, in der Reihenfolge, in der `ls` sie geschrieben hat.
::::

::::beispiel [Zweites Beispiel] Eine eigene Meldung in die Fehlerausgabe
Wer selbst eine Warnung ausgeben will, schickt sie mit `>&2` in die Standardfehlerausgabe, wie es sich für Meldungen gehört:

```console
$ echo "Achtung: Die Liste ist leer." >&2
Achtung: Die Liste ist leer.
```

Am Bildschirm sieht das aus wie jede andere Ausgabe, denn auch Deskriptor 2 führt zum Terminal. Die Anführungszeichen halten den Satz zu einem einzigen Argument zusammen, wie bei Dateinamen mit Leerzeichen ([Kapitel 3, Abschnitt 3.7](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/den-inhalt-eines-verzeichnisses-anzeigen.html#stufe-3-7)).
::::

⁠**Kurz gesagt:** `2>&1` lässt die Fehlerausgabe dorthin führen, wohin die Standardausgabe gerade führt; `&>` ist die Kurzform für beide Ausgänge in eine Datei.

### Die Reihenfolge der Umleitungen

<span class="anker" id="stufe-2-6"></span>

`> alles.txt 2>&1` und `2>&1 > alles.txt` enthalten genau dieselben Zeichen. Trotzdem tun sie Verschiedenes, und der Unterschied überrascht fast jeden, der ihn zum ersten Mal sieht. Abbildung [9](#abb-9) spielt beide Zeilen Schritt für Schritt durch.

:::abbildung linux/k4reihenfolge 9
Wohin die Deskriptoren 1 und 2 nach jedem Schritt führen. Oben `> alles.txt 2>&1`: Zuerst führt 1 zur Datei, dann übernimmt 2 dieses Ziel. Unten `2>&1 > nur.txt`: Zuerst übernimmt 2 das Ziel von 1, das ist noch das Terminal; dann wechselt nur 1 zur Datei, und 2 bleibt beim Terminal.
:::

:::satz Satz 2.6 (Reihenfolge der Umleitungen)
<span class="anker" id="satz-2-6"></span>

Die Shell führt die Umleitungen einer Befehlszeile von links nach rechts aus, eine nach der anderen. Bei `2>&1` übernimmt Deskriptor 2 das Ziel, das Deskriptor 1 genau in diesem Augenblick hat; spätere Umleitungen von Deskriptor 1 ändern an Deskriptor 2 nichts mehr.
:::

::::beispiel Zwei Zeilen, zwei Ergebnisse
Im vorigen Unterabschnitt landete bei `> alles.txt 2>&1` alles in der Datei. Mit der umgekehrten Reihenfolge:

```console
$ ls /etc/hostname /gibtsnicht 2>&1 > nur.txt
ls: cannot access '/gibtsnicht': No such file or directory
$ cat nur.txt
/etc/hostname
```

Die Meldung erscheint am Bildschirm, nur das Ergebnis steht in der Datei. Die untere Hälfte von Abbildung [9](#abb-9) verfolgt, wohin die beiden Deskriptoren nach jedem Schritt führen. In dieser Reihenfolge ändert `2>&1` gar nichts, denn Deskriptor 2 führte schon zum Terminal. Erst danach wechselt Deskriptor 1 zur Datei, und dieser Wechsel nimmt Deskriptor 2 nicht mit.
::::

⁠**Kurz gesagt:** Umleitungen wirken von links nach rechts; `2>&1` kopiert das Ziel, das die 1 in diesem Augenblick hat, deshalb steht es hinter `> datei`.

:::hintergrund Warum die Kopie nicht mitwandert
`2>&1` führt die Shell mit dem Systemaufruf `dup2` aus. Er trägt in die Liste der Deskriptoren bei der Nummer 2 dieselbe geöffnete Datei ein, die bei der Nummer 1 steht. Er legt keine Verbindung „2 folgt immer der 1“ an, sondern kopiert den Eintrag, so wie er gerade ist. Als Bild zur Orientierung: Wer die Adresse eines Freundes abschreibt, hat danach eine Adresse auf dem Zettel; zieht der Freund um, stimmt der Zettel nicht mehr. Wird Deskriptor 1 danach mit einer anderen Datei verbunden, bekommt er einen neuen Eintrag, und der kopierte Eintrag bei der 2 bleibt, wie er war. Das Bild hat eine Grenze: Beide Deskriptoren teilen sich danach wirklich dieselbe geöffnete Datei, samt der Stelle, an der als Nächstes geschrieben wird. Deshalb überschreiben sich Ergebnis und Meldung in `alles.txt` nicht, sondern stehen hintereinander.
:::

### Die Kürzungsfalle

<span class="anker" id="stufe-2-7"></span>

Eine Liste soll sortiert werden, und das Ergebnis soll wieder unter demselben Namen stehen. Der naheliegende Befehl dafür zerstört die Liste. Der Befehl `sort` sortiert die Zeilen der genannten Dateien und schreibt sie in die Standardausgabe; mehr braucht dieses Beispiel von ihm nicht. Abbildung [10](#abb-10) zeigt, was bei `sort probe.txt > probe.txt` der Reihe nach geschieht.

:::abbildung linux/k4kuerzung 10
Die Kürzungsfalle als Zeitleiste. Erst öffnet die Shell `probe.txt` für die Umleitung und macht die Datei dabei leer, aus 32 Bytes werden 0. Dann startet `sort`, liest die leere Datei und schreibt nichts. Am Ende ist die Liste verloren.
:::

:::satz Satz 2.7 (Kürzungsfalle)
<span class="anker" id="satz-2-7"></span>

Bei `befehl datei > datei` ist die Datei leer, bevor der Befehl startet. Die Shell richtet die Umleitung vor dem Programmstart ein, und `>` macht die Datei dabei leer. Das Programm liest danach eine leere Datei; der alte Inhalt ist verloren.
:::

::::beispiel Eine Liste wird leer
Probiere es an einer Kopie der Einkaufsliste:

```console
$ cp einkauf.txt probe.txt
$ wc -c probe.txt
32 probe.txt
$ sort probe.txt > probe.txt
$ wc -c probe.txt
0 probe.txt
```

Aus 32 Bytes sind null geworden. Eine Fehlermeldung gab es nicht, denn aus Sicht von `sort` ist alles richtig gelaufen: Es hat eine leere Datei sortiert.
::::

Sicher geht es auf zwei Wegen. Entweder schreibt man das Ergebnis zuerst in eine andere Datei und benennt diese danach um ([Kapitel 3, Abschnitt 6.3](/wissen/informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade/kopieren-verschieben-loschen.html#stufe-6-3)), oder man benutzt die Option `-o` von `sort`: Sie schreibt das Ergebnis in die genannte Datei und öffnet diese erst, wenn alles gelesen ist.

```console
$ cp einkauf.txt probe.txt
$ sort probe.txt > sortiert.txt
$ mv sortiert.txt probe.txt
$ cat probe.txt
Brot
Butter
Kaffee
Milch
Äpfel
$ cp einkauf.txt probe2.txt
$ sort -o probe2.txt probe2.txt
$ cat probe2.txt
Brot
Butter
Kaffee
Milch
Äpfel
```

Dass `Äpfel` am Ende steht, liegt an der Spracheinstellung des Testsystems, die nach den Nummern der Zeichen sortiert; das `Ä` hat eine höhere Nummer als alle Buchstaben ohne Umlaut.

⁠**Kurz gesagt:** Nie aus einer Datei lesen und mit `>` in dieselbe Datei schreiben; die Shell leert sie, bevor das Programm sie lesen kann.

:::hintergrund Warum die Datei schon vor dem Programmstart leer ist
Die Shell arbeitet eine Befehlszeile in fester Reihenfolge ab: Sie zerlegt die Zeile in Wörter, bereitet die Wörter auf, richtet dann die Umleitungen ein und startet erst zum Schluss das Programm. Beim Einrichten von `>` öffnet sie die Zieldatei mit der Anweisung an den Kernel, sie auf die Länge null zu kürzen; das geschieht im neuen Prozess zwischen `fork` und `exec` (Unterabschnitt [2.1](#stufe-2-1)). Wenn `sort` anfängt zu lesen, ist die Kürzung längst geschehen. `sort -o` umgeht das, weil `sort` dort selbst entscheidet, wann es die Zieldatei öffnet: erst nachdem es die ganze Eingabe gelesen hat. Mit `>>` statt `>` wird die Datei zwar nicht geleert, doch dann liest ein Programm womöglich immer weiter, was es gerade selbst ans Ende geschrieben hat, und die Datei wächst, bis der Datenträger voll ist. `cat` prüft das deshalb und weigert sich, in der uutils-Fassung von Ubuntu 26.04 wie in der GNU-Fassung:

```console
$ cat probe.txt >> probe.txt
cat: probe.txt: input file is output file
$ gnucat probe.txt >> probe.txt
gnucat: probe.txt: input file is output file
```

Auf diese Vorsicht darf man sich nicht verlassen: Die meisten Programme prüfen es nicht.
:::

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-8"></span>

:::aufgabe Aufgabe 5 ★ Ströme trennen
<span class="anker" id="aufg-5"></span>

Führe in deinem Übungsverzeichnis `ls /etc/hostname /gibtsnicht > aus.txt 2> fehler2.txt` aus. (a) Was erscheint am Bildschirm? (b) Was steht in `aus.txt`, was in `fehler2.txt`? (c) Was ändert sich, wenn du statt `2> fehler2.txt` die Umleitung `2> /dev/null` schreibst?

:::loesung
```console
$ ls /etc/hostname /gibtsnicht > aus.txt 2> fehler2.txt
$ cat aus.txt
/etc/hostname
$ cat fehler2.txt
ls: cannot access '/gibtsnicht': No such file or directory
$ ls /etc/hostname /gibtsnicht > aus.txt 2> /dev/null
$ cat aus.txt
/etc/hostname
```

(a) Am Bildschirm erscheint nichts, denn beide Ausgänge sind umgeleitet. (b) `aus.txt` enthält das Ergebnis `/etc/hostname`, `fehler2.txt` die Meldung. (c) Die Meldung verschwindet in `/dev/null`; `aus.txt` enthält dasselbe wie vorher, denn `>` hat die Datei geleert und neu beschrieben.
:::
:::

:::aufgabe Aufgabe 6 ★ Was steht am Ende in der Datei?
<span class="anker" id="aufg-6"></span>

Sage voraus, was nach diesen vier Zeilen in `tag.txt` steht, und prüfe es:

```console
$ echo Montag > tag.txt
$ echo Dienstag >> tag.txt
$ echo Mittwoch > tag.txt
$ echo Donnerstag >> tag.txt
```

:::loesung
```console
$ cat tag.txt
Mittwoch
Donnerstag
```

Nach den ersten beiden Zeilen stehen `Montag` und `Dienstag` in der Datei. Die dritte Zeile benutzt `>`: Die Shell leert die Datei, und danach steht nur `Mittwoch` darin. Die vierte hängt `Donnerstag` an.
:::
:::

:::aufgabe Aufgabe 7 ★★ Die Reihenfolge vorhersagen
<span class="anker" id="aufg-7"></span>

Für jede Zeile gilt der Befehl `ls /etc/hostname /gibtsnicht` mit anderen Umleitungen. Sage voraus, was am Bildschirm erscheint und was in der Datei steht, schreibe dazu wie in Abbildung [9](#abb-9) die Ziele der Deskriptoren 1 und 2 nach jedem Schritt, und prüfe am Rechner: (a) `> a.txt 2>&1` (b) `2>&1 > b.txt` (c) `2> c.txt 1>&2` (d) `1>&2 2> d.txt`.

:::loesung
```console
$ ls /etc/hostname /gibtsnicht > a.txt 2>&1
$ cat a.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
$ ls /etc/hostname /gibtsnicht 2>&1 > b.txt
ls: cannot access '/gibtsnicht': No such file or directory
$ cat b.txt
/etc/hostname
$ ls /etc/hostname /gibtsnicht 2> c.txt 1>&2
$ cat c.txt
ls: cannot access '/gibtsnicht': No such file or directory
/etc/hostname
$ ls /etc/hostname /gibtsnicht 1>&2 2> d.txt
/etc/hostname
$ cat d.txt
ls: cannot access '/gibtsnicht': No such file or directory
```

Am Anfang führen 1 und 2 zum Terminal (T).

<ul>

<li>

(a) `> a.txt`: 1 → `a.txt`, 2 → T. `2>&1`: 2 → `a.txt`. Am Bildschirm nichts, in der Datei beide Zeilen.

</li>

<li>

(b) `2>&1`: 2 → T, denn das ist das Ziel von 1. `> b.txt`: 1 → `b.txt`, 2 bleibt bei T. Am Bildschirm die Meldung, in der Datei das Ergebnis.

</li>

<li>

(c) `2> c.txt`: 2 → `c.txt`, 1 → T. `1>&2`: 1 → `c.txt`. Wie (a) mit vertauschten Rollen: Am Bildschirm nichts, in der Datei beide Zeilen.

</li>

<li>

(d) `1>&2`: 1 → T, denn das ist das Ziel von 2. `2> d.txt`: 2 → `d.txt`, 1 bleibt bei T. Wie (b) mit vertauschten Rollen: Am Bildschirm das Ergebnis, in der Datei die Meldung.

</li>

</ul>

In allen vier Fällen entscheidet, was zum Zeitpunkt der Kopie hinter dem kopierten Deskriptor steht; spätere Umleitungen ändern an einer Kopie nichts.
:::
:::

:::aufgabe Aufgabe 8 ★★ Die Kürzungsfalle
<span class="anker" id="aufg-8"></span>

(a) Lege mit `cat > zahlen.txt` eine Datei mit den Zeilen `3`, `1`, `2` an. Sage voraus, was `sort zahlen.txt > zahlen.txt` bewirkt, und prüfe es mit `wc -c`. (b) Lege die Datei neu an und sortiere sie auf zwei sichere Arten. (c) `head -n 2 zahlen.txt > zahlen.txt` soll nur die ersten beiden Zeilen behalten. Was geschieht wirklich, und warum hilft es nicht, dass `head` nur zwei Zeilen braucht?

:::loesung
(a) Vorhersage: Die Datei ist danach leer. Die Probe:

```console
$ cat > zahlen.txt
3
1
2
$ sort zahlen.txt > zahlen.txt
$ wc -c zahlen.txt
0 zahlen.txt
```

Die Shell hat `zahlen.txt` für die Umleitung geleert, bevor `sort` startete; `sort` hat eine leere Datei sortiert.

(b) Über eine Zwischendatei, die erst bei Erfolg die alte ersetzt, oder mit `sort -o`. Hier wird die Datei zur Abkürzung mit `printf` neu angelegt, das die Folge `\n` als Zeilenende schreibt; `cat >` mit drei getippten Zeilen tut es genauso:

```console
$ printf '3\n1\n2\n' > zahlen.txt
$ sort zahlen.txt > sortiert.txt && mv sortiert.txt zahlen.txt
$ cat zahlen.txt
1
2
3
$ printf '3\n1\n2\n' > zahlen.txt
$ sort -o zahlen.txt zahlen.txt
$ cat zahlen.txt
1
2
3
```

(c) Auch hier bleibt eine leere Datei:

```console
$ head -n 2 zahlen.txt > zahlen.txt
$ wc -c zahlen.txt
0 zahlen.txt
```

Es kommt nicht darauf an, wie viel ein Programm liest. Die Datei wird geleert, bevor `head` überhaupt startet; als es liest, ist nichts mehr da, nicht einmal die ersten zwei Zeilen.
:::
:::

:::aufgabe Aufgabe 9 ★★★ Das vergessene &
<span class="anker" id="aufg-9"></span>

Jemand will mit `ls /gibtsnicht 2>1` die Fehlermeldung in die Standardausgabe schicken. Sage voraus, was am Bildschirm erscheint und welche Datei danach im Übungsverzeichnis neu ist, und prüfe es. Erkläre mit der Definition aus Unterabschnitt [2.5](#stufe-2-5), wozu das `&` da ist.

:::loesung
```console
$ ls /gibtsnicht 2>1
$ cat 1
ls: cannot access '/gibtsnicht': No such file or directory
$ rm 1
```

Am Bildschirm erscheint nichts, und im Übungsverzeichnis steht danach eine Datei mit dem Namen `1`, in der die Meldung steht. Ohne `&` ist das Wort hinter `2>` ein Dateiname, auch wenn es nur aus einer Ziffer besteht. Erst `2>&1` sagt der Shell, dass die 1 einen Deskriptor meint, von dem Deskriptor 2 eine Kopie werden soll.
:::
:::
