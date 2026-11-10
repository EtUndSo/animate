---
title: Das Arbeitsverzeichnis und Pfade
pfad: Informatik / Linux und Kommandozeile / Dateien, Verzeichnisse und Pfade
adresse: informatik/linux-und-kommandozeile/dateien-verzeichnisse-und-pfade
knoten: Kapitel 3: Dateien, Verzeichnisse und Pfade
order: 6080300
summary: Im Terminal gibt es keine Maus, die auf eine Datei zeigt.
tags: Arbeitsverzeichnis, Pfad, absoluter Pfad, relativer Pfad, Heimatverzeichnis, Tilde, cd
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Im Terminal gibt es keine Maus, die auf eine Datei zeigt. Man nennt eine Datei, indem man ihren Weg durch den Baum aufschreibt. Dieser Abschnitt zeigt, wo man sich gerade befindet, wie man Wege schreibt, vom Anfang des Baums oder vom eigenen Standort aus, und wie man sich mit `cd` bewegt.
:::

### Das Arbeitsverzeichnis

<span class="anker" id="stufe-2-1"></span>

Wer in einem großen Gebäude unterwegs ist, muss wissen, wo er steht, bevor er einen Weg beschreiben kann. Im Verzeichnisbaum ist das genauso.

**Ein Standort im Baum.** Man kann sich vorstellen, man stehe in genau einem Verzeichnis des Baums. Von dort sieht man die Einträge dieses Verzeichnisses, den Weg nach oben zum übergeordneten Verzeichnis und die Wege nach unten in die Unterverzeichnisse. Abbildung [5](#abb-5) markiert diesen Standort und zeigt, wie er sich bei einem Wechsel bewegt.

:::abbildung linux/k3arbeitsverzeichnis 5
Das Arbeitsverzeichnis als Standort im Baum. Zuerst steht die Markierung in `/home/student`; nach `cd /usr/bin` springt sie nach `/usr/bin`, und `pwd` nennt jeweils den Weg von der Wurzel bis zur Markierung.
:::

:::definition Definition 2.1 (Arbeitsverzeichnis)
<span class="anker" id="satz-2-1"></span>

Das __Arbeitsverzeichnis__ eines laufenden Programms ist das Verzeichnis, in dem es gerade arbeitet. Gibt man einem Befehl keinen Ort an, bezieht er sich auf dieses Verzeichnis.
:::

Für die Shell ist das Arbeitsverzeichnis genau der aktuelle Ordner aus [Kapitel 2, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/terminal-und-shell.html#stufe-1-4). Jedes laufende Programm hat ein eigenes Arbeitsverzeichnis; deshalb können zwei Terminalfenster in verschiedenen Verzeichnissen stehen. Der Befehl `pwd` (kurz für „print working directory“) schreibt das Arbeitsverzeichnis der Shell aus.

::::beispiel Wo bin ich?
Ein frisch geöffnetes Terminal steht in deinem persönlichen Verzeichnis. Der Kasten zeigt diesmal die ganze Eingabeaufforderung, damit du siehst, wie sie mitwandert:

```text
student@labor:~$ pwd
/home/student
student@labor:~$ cd /usr/bin
student@labor:/usr/bin$ pwd
/usr/bin
```

`pwd` schreibt den vollen Weg aus; die Eingabeaufforderung zeigt dasselbe, nur kürzt sie `/home/student` mit `~` ab.
::::

⁠**Kurz gesagt:** Das Arbeitsverzeichnis ist der Standort im Baum, auf den sich Befehle ohne Ortsangabe beziehen; `pwd` nennt es.

### Der Pfad

<span class="anker" id="stufe-2-2"></span>

Um eine Datei zu nennen, die nicht im Arbeitsverzeichnis liegt, muss man den Weg zu ihr beschreiben. Dafür gibt es eine knappe Schreibweise.

**Eine Wegbeschreibung aus Namen.** Ein Weg durch den Baum ist eine Folge von Abzweigungen: erst in dieses Verzeichnis, dann in jenes, dann zur Datei. Man schreibt die Namen hintereinander und trennt sie durch Schrägstriche. Abbildung [6](#abb-6) liest den Pfad `/usr/bin/bash` Schritt für Schritt.

:::abbildung linux/k3pfad 6
Der Pfad `/usr/bin/bash`, Schritt für Schritt gelesen: vom Wurzelverzeichnis in den Eintrag `usr`, von dort in den Eintrag `bin`, dort zum Eintrag `bash`. Jeder Schrägstrich ist eine Abzweigung.
:::

:::definition Definition 2.2 (Pfad)
<span class="anker" id="satz-2-2"></span>

Ein __Pfad__ ist eine Folge von Namen, getrennt durch Schrägstriche `/`, die den Weg durch den Verzeichnisbaum zu einer Datei oder einem Verzeichnis beschreibt. Jeder Name außer dem letzten muss ein Verzeichnis bezeichnen.
:::

Der Schrägstrich hat damit zwei Aufgaben: Am Anfang eines Pfads steht er für das Wurzelverzeichnis, zwischen zwei Namen trennt er sie. Windows benutzt als Trenner den umgekehrten Schrägstrich `\`; unter Linux ist das ein ganz anderes Zeichen.

::::beispiel Einen Pfad lesen
Der Pfad `/usr/share/doc` bedeutet: Beginne im Wurzelverzeichnis, gehe in dessen Eintrag `usr`, darin in den Eintrag `share` und darin in den Eintrag `doc`. `usr` und `share` müssen Verzeichnisse sein, sonst ginge der Weg nicht weiter; `doc` ist das Ziel und hier ebenfalls ein Verzeichnis.
::::

⁠**Kurz gesagt:** Ein Pfad ist eine Wegbeschreibung durch den Baum: Namen, getrennt durch Schrägstriche.

### Der absolute Pfad

<span class="anker" id="stufe-2-3"></span>

Manche Wegbeschreibungen sollen überall gelten, gleichgültig, wo man gerade steht, so wie eine vollständige Postanschrift mit Straße, Hausnummer und Ort.

:::definition Definition 2.3 (absoluter Pfad)
<span class="anker" id="satz-2-3"></span>

Ein __absoluter Pfad__ beginnt mit `/`. Er beschreibt den Weg vom Wurzelverzeichnis aus und bezeichnet deshalb von jedem Arbeitsverzeichnis aus denselben Ort.
:::

`/etc/hostname`, `/usr/bin` und `/home/student` sind absolute Pfade. `pwd` gibt immer einen absoluten Pfad aus, denn nur er sagt eindeutig, wo man steht.

::::beispiel Derselbe Ort von zwei Standorten aus
`cat /etc/timezone` zeigt die Zeitzone des Rechners. Der absolute Pfad führt von jedem Arbeitsverzeichnis aus zur selben Datei:

```text
student@labor:~$ cat /etc/timezone
Europe/Berlin
student@labor:~$ cd /usr/share
student@labor:/usr/share$ cat /etc/timezone
Europe/Berlin
```
::::

⁠**Kurz gesagt:** Ein absoluter Pfad beginnt mit `/` und gilt von überall aus.

### Der relative Pfad

<span class="anker" id="stufe-2-4"></span>

Absolute Pfade werden lang, wenn man tief im Baum arbeitet. Oft ist eine Wegbeschreibung vom eigenen Standort aus kürzer, so wie „zweite Tür links“ in einem Gebäude, das man schon betreten hat.

:::abbildung linux/k3absolutrelativ 7
Zwei Wege zur selben Datei `/usr/bin/bash`. Der absolute Pfad beginnt an der Wurzel. Der relative Pfad `bin/bash` beginnt am Arbeitsverzeichnis `/usr`; vom Arbeitsverzeichnis `/home/student` aus führt derselbe relative Pfad ins Leere.
:::

:::definition Definition 2.4 (relativer Pfad)
<span class="anker" id="satz-2-4"></span>

Ein __relativer Pfad__ beginnt nicht mit `/`. Er beschreibt den Weg vom Arbeitsverzeichnis aus; welchen Ort er bezeichnet, hängt also davon ab, wo man gerade steht.
:::

Ein einzelner Name wie `bash` ist der kürzeste relative Pfad: der Eintrag `bash` im Arbeitsverzeichnis. Abbildung [7](#abb-7) zeigt, wie derselbe relative Pfad von zwei Standorten aus zu verschiedenen Ergebnissen führt.

::::beispiel Derselbe relative Pfad, zwei Standorte
```text
student@labor:~$ cd /usr
student@labor:/usr$ ls bin/bash
bin/bash
student@labor:/usr$ cd
student@labor:~$ ls bin/bash
ls: cannot access 'bin/bash': No such file or directory
```

In `/usr` führt `bin/bash` zur Datei `/usr/bin/bash`; `ls` bestätigt das, indem es den Namen wiederholt. In `/home/student` gibt es keinen Eintrag `bin`, also findet `ls` nichts und meldet „No such file or directory“, keine solche Datei und kein solches Verzeichnis.
::::

⁠**Kurz gesagt:** Ein relativer Pfad beginnt ohne `/` und gilt vom Arbeitsverzeichnis aus.

### Die Sondernamen . und ..

<span class="anker" id="stufe-2-5"></span>

Mit relativen Pfaden kommt man nur nach unten, in Unterverzeichnisse. Um nach oben zu gelangen, braucht man einen Namen für das übergeordnete Verzeichnis, und manchmal einen für das Verzeichnis, in dem man selbst steht.

:::definition Definition 2.5 (die Einträge . und ..)
<span class="anker" id="satz-2-5"></span>

In jedem Verzeichnis gibt es zwei besondere Einträge: `.` (ein Punkt) bezeichnet das Verzeichnis selbst, `..` (zwei Punkte) sein übergeordnetes Verzeichnis. Im Wurzelverzeichnis bezeichnet `..` das Wurzelverzeichnis selbst.
:::

`..` steht in einem Pfad wie jeder andere Name: `../..` heißt „zwei Ebenen nach oben“, `../share` heißt „eine Ebene nach oben und dann in `share`“. Der einzelne Punkt scheint überflüssig, denn `./bin` und `bin` meinen dasselbe. Er wird aber gebraucht, wenn ein Befehl unbedingt ein Verzeichnis als Argument verlangt und das Arbeitsverzeichnis gemeint ist. Abbildung [8](#abb-8) verfolgt eine Reihe von Schritten nach oben.

:::abbildung linux/k3punkte 8
Schritte nach oben mit `..`: von `/usr/share/doc` eine Ebene hinauf nach `/usr/share`, mit `../..` zwei Ebenen hinauf bis zur Wurzel. Ein weiterer Schritt `..` bleibt in `/`: Über der Wurzel gibt es nichts.
:::

::::beispiel Nach oben, bis es nicht weitergeht
```text
student@labor:~$ cd /usr/share/doc
student@labor:/usr/share/doc$ cd ..
student@labor:/usr/share$ pwd
/usr/share
student@labor:/usr/share$ cd ../..
student@labor:/$ pwd
/
student@labor:/$ cd ..
student@labor:/$ pwd
/
```

Das letzte `cd ..` meldet keinen Fehler, es bleibt einfach im Wurzelverzeichnis.
::::

⁠**Kurz gesagt:** `.` ist das Verzeichnis selbst, `..` das übergeordnete; in der Wurzel führt `..` zur Wurzel zurück.

:::hintergrund Wie ein Pfad Schritt für Schritt aufgelöst wird
Einen Pfad in eine Datei zu übersetzen, ist Aufgabe des Kernels, nicht der Shell. Jedes Programm, das eine Datei öffnen will, übergibt dem Kernel den Pfad mit einem Systemaufruf ([Kapitel 1, Abschnitt 1.4](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/betriebssystem-kernel-und-distribution.html#stufe-1-4)), und der Kernel geht ihn Name für Name durch. Beginnt der Pfad mit `/`, startet er im Wurzelverzeichnis, sonst im Arbeitsverzeichnis des Programms. Dann schlägt er jeden Namen im jeweils erreichten Verzeichnis nach. Fehlt ein Name, scheitert der Weg mit der Meldung „No such file or directory“. Ist ein Name, der nicht der letzte ist, gar kein Verzeichnis, scheitert er mit „Not a directory“, denn in einer gewöhnlichen Datei kann man keinen weiteren Namen nachschlagen:

```console
$ ls /etc/hostname/x
ls: cannot access '/etc/hostname/x': Not a directory
```

Die Namen `.` und `..` haben dabei immer ihre feste Bedeutung, gleichgültig, wie ein Dateisystem sie speichert. Weil alle Programme diesen einen Weg benutzen, verstehen alle Programme Pfade gleich: `ls`, `cat` und jeder Texteditor.
:::

### Das Heimatverzeichnis und die Tilde

<span class="anker" id="stufe-2-6"></span>

Jeder Mensch, der einen Rechner benutzt, braucht einen eigenen Platz für seine Dateien, so wie jede Mitbewohnerin ein eigenes Zimmer hat. Weil man diesen Platz ständig braucht, hat er eine Abkürzung.

:::definition Definition 2.6 (Heimatverzeichnis)
<span class="anker" id="satz-2-6"></span>

Das __Heimatverzeichnis__ eines Benutzers ist das Verzeichnis, das ihm für seine eigenen Dateien gehört. Unter Linux ist es meist `/home/<name>`, für den Benutzer `student` also `/home/student`.
:::

Das Heimatverzeichnis ist der persönliche Ordner aus [Kapitel 2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/die-shell-erste-befehle.html); ein neues Terminal startet darin. Als gewöhnlicher Benutzer darfst du im Wesentlichen nur dort Dateien anlegen und ändern; die meisten Verzeichnisse des Systems darfst du lesen, aber nicht verändern. Die Abkürzung dafür ist die __Tilde__ `~`: Steht sie am Anfang eines Worts, ersetzt die Shell sie durch den Pfad deines Heimatverzeichnisses, bevor sie den Befehl startet. Deshalb funktioniert sie bei jedem Befehl. `~/fotos` heißt dann `/home/student/fotos`, und `~root` heißt „das Heimatverzeichnis des Benutzers `root`“. Mitten in einem Wort bleibt die Tilde ein gewöhnliches Zeichen.

::::beispiel Was die Shell aus der Tilde macht
Der Befehl `echo` gibt seine Argumente einfach wieder aus ([Kapitel 2, Abschnitt 2.3](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/der-aufbau-einer-befehlszeile.html#stufe-2-3)). Er zeigt deshalb, was die Shell aus der Tilde gemacht hat, bevor `echo` startete:

```console
$ echo ~ ~/fotos ~root
/home/student /home/student/fotos /root
```

Das Verzeichnis `/home/student/fotos` muss dafür nicht existieren; die Shell ersetzt nur Text. Das Heimatverzeichnis von `root` liegt nicht unter `/home`, sondern ist `/root`.
::::

⁠**Kurz gesagt:** Das Heimatverzeichnis ist dein eigener Platz im Baum; `~` am Anfang eines Worts steht für seinen Pfad.

### Das Verzeichnis wechseln: cd

<span class="anker" id="stufe-2-7"></span>

Mit Pfaden kann man jetzt jeden Ort beschreiben. Um dort zu arbeiten, ohne den Pfad jedes Mal mitzuschreiben, wechselt man das Arbeitsverzeichnis.

:::definition Definition 2.7 (cd)
<span class="anker" id="satz-2-7"></span>

Der eingebaute Befehl __cd__ (kurz für „change directory“) macht das Verzeichnis, das sein Argument bezeichnet, zum neuen Arbeitsverzeichnis der Shell. Ohne Argument wechselt er ins Heimatverzeichnis, mit dem Argument `-` zurück ins vorige Arbeitsverzeichnis.
:::

Das Argument darf ein absoluter oder ein relativer Pfad sein. Bei Erfolg schreibt `cd` nichts; die neue Eingabeaufforderung zeigt den neuen Ort. Nur `cd -` nennt zur Sicherheit, wohin es gewechselt hat. Wie die Markierung des Arbeitsverzeichnisses dabei springt, zeigt schon Abbildung [5](#abb-5).

::::beispiel Hin und her
```text
student@labor:~$ cd /etc
student@labor:/etc$ cd -
/home/student
student@labor:~$ cd -
/etc
student@labor:/etc$ cd ~
student@labor:~$ cd /etc/hostname
bash: cd: /etc/hostname: Not a directory
student@labor:~$ cd Etc
bash: cd: Etc: No such file or directory
```

`cd -` pendelt zwischen den beiden letzten Orten. Die beiden letzten Versuche scheitern: `/etc/hostname` ist eine Datei, kein Verzeichnis, und `Etc` gibt es im Heimatverzeichnis nicht. Die Meldung beginnt mit `bash: cd:`, weil die Shell selbst den Befehl ausführt.
::::

⁠**Kurz gesagt:** `cd` wechselt das Arbeitsverzeichnis: `cd pfad` hin, `cd` nach Hause, `cd -` zurück, `cd ..` eine Ebene hinauf.

### Aufgaben zu Abschnitt [2](#stufe-2)

<span class="anker" id="stufe-2-8"></span>

:::aufgabe Aufgabe 4 ★ Pfade vorhersagen
<span class="anker" id="aufg-4"></span>

Dein Arbeitsverzeichnis ist `/usr/share/doc`. Welchen absoluten Pfad bezeichnet jeder der folgenden Pfade? (a) `..` (b) `../..` (c) `~/x` (d) `/etc` (e) `../../../../etc` (f) `./bash` (g) `../doc/../man`. Prüfe (e) und (g) am Rechner mit `cd` und `pwd`.

:::loesung
Ausgangspunkt ist `/usr/share/doc`.

<ol class="al">

<li>

`..` ist eine Ebene höher: `/usr/share`.

</li>

<li>

`../..` sind zwei Ebenen höher: `/usr`.

</li>

<li>

`~/x` hängt nicht vom Arbeitsverzeichnis ab, denn die Shell ersetzt die Tilde durch das Heimatverzeichnis: `/home/student/x`. Ob es `x` gibt, spielt für den Pfad keine Rolle.

</li>

<li>

`/etc` ist absolut und bleibt `/etc`.

</li>

<li>

Schritt für Schritt: `..` führt nach `/usr/share`, das zweite `..` nach `/usr`, das dritte nach `/`, das vierte bleibt in `/`, weil es über der Wurzel nichts gibt; dann `etc`. Ergebnis: `/etc`.

</li>

<li>

`./bash` ist der Eintrag `bash` im Arbeitsverzeichnis: `/usr/share/doc/bash`.

</li>

<li>

`..` führt nach `/usr/share`, `doc` wieder nach `/usr/share/doc`, `..` zurück nach `/usr/share`, `man` nach `/usr/share/man`.

</li>

</ol>

Die Probe für (e) und (g):

```text
student@labor:~/linuxk3$ cd /usr/share/doc
student@labor:/usr/share/doc$ cd ../../../../etc
student@labor:/etc$ pwd
/etc
student@labor:/etc$ cd /usr/share/doc
student@labor:/usr/share/doc$ cd ../doc/../man
student@labor:/usr/share/man$ pwd
/usr/share/man
```
:::
:::

:::aufgabe Aufgabe 5 ★★ Absolut und relativ umschreiben
<span class="anker" id="aufg-5"></span>

(a) Dein Arbeitsverzeichnis ist `/usr`. Schreibe den absoluten Pfad `/usr/share/man` als möglichst kurzen relativen Pfad. (b) Dein Arbeitsverzeichnis ist `/usr/share/man`. Schreibe `/usr/bin` als relativen Pfad. (c) Dein Arbeitsverzeichnis ist `/home/student`. Wann ist der absolute Pfad `/etc/hosts` kürzer als jeder relative?

:::loesung
(a) Von `/usr` aus führt `share/man` zum Ziel; kürzer geht es nicht.

(b) Von `/usr/share/man` muss man zwei Ebenen hinauf bis `/usr` und dann hinein nach `bin`: `../../bin`.

(c) Von `/home/student` aus heißt der relative Weg `../../etc/hosts`, zwei Ebenen hinauf bis zur Wurzel und dann hinab; das sind 15 Zeichen gegen 10 für `/etc/hosts`. Allgemein ist der absolute Pfad kürzer, wenn Arbeitsverzeichnis und Ziel erst weit oben im Baum zusammentreffen, sodass der relative Weg viele `..` braucht. Liegt das Ziel unterhalb des Arbeitsverzeichnisses, ist der relative Pfad fast immer kürzer.
:::
:::

:::aufgabe Aufgabe 6 ★★ Fehlermeldungen von cd
<span class="anker" id="aufg-6"></span>

Erkläre jede Meldung: (a) `cd /ETC` meldet „No such file or directory“, (b) `cd ~root` meldet „Permission denied“, (c) `cd /etc/hostname` meldet „Not a directory“. Welche der drei Meldungen kommt von einem fehlenden Eintrag, welche von einem Eintrag der falschen Art, welche von einem Verbot?

:::loesung
```text
student@labor:~/linuxk3$ cd /ETC
bash: cd: /ETC: No such file or directory
student@labor:~/linuxk3$ cd ~root
bash: cd: /root: Permission denied
```

(a) Ein fehlender Eintrag: In `/` gibt es `etc`, aber nicht `ETC`, und Linux unterscheidet Groß- und Kleinbuchstaben. (b) Ein Verbot: Die Shell hat `~root` durch `/root` ersetzt, wie die Meldung zeigt. Das Verzeichnis gibt es, aber der Benutzer `student` darf es nicht betreten; dieselbe Meldung zeigte `ls /root` in Unterabschnitt [7.4](die-verzeichnisstruktur-von-linux.html#stufe-7-4). (c) Ein Eintrag der falschen Art: `/etc/hostname` gibt es, aber es ist eine Datei, und in eine Datei kann man nicht wechseln (Beispiel in Unterabschnitt [2.7](#stufe-2-7)).
:::
:::
