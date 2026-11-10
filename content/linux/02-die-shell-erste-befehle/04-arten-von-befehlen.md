---
title: Arten von Befehlen
pfad: Informatik / Linux und Kommandozeile / Die Shell: erste Befehle
adresse: informatik/linux-und-kommandozeile/die-shell-erste-befehle
knoten: Kapitel 2: Die Shell: erste Befehle
order: 6070400
summary: Hinter dem ersten Wort einer Befehlszeile kann Verschiedenes stecken: ein eigenes Programm auf der Festplatte, ein Befehl, den die Shell selbst erledigt, oder ein Kurzname für einen längeren Befehl.
tags: Programmdatei, Suchpfad, eingebauter Befehl, Alias
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Hinter dem ersten Wort einer Befehlszeile kann Verschiedenes stecken: ein eigenes Programm auf der Festplatte, ein Befehl, den die Shell selbst erledigt, oder ein Kurzname für einen längeren Befehl. Dieser Abschnitt stellt die drei Arten vor, erklärt, warum manche Befehle Teil der Shell sein müssen, und zeigt, wie man herausfindet, was hinter einem Namen steckt.
:::

### Die Programmdatei

<span class="anker" id="stufe-3-1"></span>

Wenn du `uname` tippst, läuft ein Programm, das nicht in der Shell steckt. Es liegt als Datei auf dem Datenträger, wie ein Foto oder ein Brief, nur dass es Befehle für den Prozessor enthält.

:::definition Definition 3.1 (Programmdatei)
<span class="anker" id="satz-3-1"></span>

Eine __Programmdatei__ ist eine Datei, die ein ausführbares Programm enthält. Die meisten Befehle sind Programmdateien; unter Linux liegen sie vor allem im Ordner `/usr/bin`.
:::

::::beispiel Ein Programm mit vollem Namen starten
Die Programmdatei von `uname` heißt mit vollem Namen `/usr/bin/uname`: die Datei `uname` im Ordner `/usr/bin`. Man kann sie auch unter diesem Namen starten, mit demselben Ergebnis:

```console
$ /usr/bin/uname -r
6.6.87.2-microsoft-standard-WSL2
```

Niemand tippt das im Alltag; `uname` allein genügt. Die Shell findet die Datei also selbst.
::::

⁠**Kurz gesagt:** Die meisten Befehle sind Programmdateien, Dateien mit einem ausführbaren Programm darin.

### Der Suchpfad

<span class="anker" id="stufe-3-2"></span>

Wenn du nur `uname` tippst, muss die Shell die passende Datei selbst finden. Den ganzen Datenträger zu durchsuchen wäre viel zu langsam, und es könnte mehrere Dateien dieses Namens geben.

**Eine feste Liste von Ordnern.** Die Shell durchsucht nicht den ganzen Datenträger, sondern nur eine kurze Liste von Ordnern, in denen Programme liegen, und zwar immer in derselben Reihenfolge. Abbildung [10](#abb-10) zeigt die Suche nach `uname`.

:::abbildung linux/k2suche 10
Die Shell sucht den Befehl `uname` der Reihe nach in den Ordnern des Suchpfads. In `/usr/bin` findet sie die Programmdatei `uname` und startet sie; die übrigen Ordner sieht sie sich nicht mehr an.
:::

:::definition Definition 3.2 (Suchpfad)
<span class="anker" id="satz-3-2"></span>

Der __Suchpfad__ ist die Liste von Ordnern, in denen die Shell nach einer Programmdatei mit dem Namen des Befehls sucht; sie startet die erste, die sie findet. Unter Ubuntu gehören dazu unter anderem `/usr/local/bin`, `/usr/bin` und `/bin`.
:::

Der Befehl `which` nennt die Programmdatei, die die Shell für einen Namen im Suchpfad finden würde. Unter WSL 2 hängt WSL außerdem die Ordner der Windows-Programme hinten an den Suchpfad an; deshalb startet dort auch ein Windows-Programm wie `explorer.exe` aus [Kapitel 1, Abschnitt 4.6](/wissen/informatik/linux-und-kommandozeile/ein-linux-zum-uben-wsl-virtuelle-maschine-live-usb-stick/wsl-2-linux-neben-windows.html#stufe-4-6).

::::beispiel Wo die Programme liegen
```console
$ which uname
/usr/bin/uname
$ which head
/usr/bin/head
$ which bash
/usr/bin/bash
```

Auch die Shell selbst ist eine gewöhnliche Programmdatei: `/usr/bin/bash`.
::::

⁠**Kurz gesagt:** Die Shell sucht Programmdateien der Reihe nach in den Ordnern des Suchpfads und startet die erste passende.

### Der eingebaute Befehl

<span class="anker" id="stufe-3-3"></span>

Fragt man unter Ubuntu `which` nach `cd`, bekommt man keine Antwort, und doch wechselt `cd` zuverlässig den Ordner. Es gibt also Befehle, die keine Datei sind.

```console
$ which cd
```

:::definition Definition 3.3 (Eingebauter Befehl)
<span class="anker" id="satz-3-3"></span>

Ein __eingebauter Befehl__ ist ein Befehl, den die Shell selbst ausführt, ohne ein anderes Programm zu starten. Sein Programmteil steckt in der Shell, nicht in einer eigenen Datei.
:::

Ob ein Name ein eingebauter Befehl ist, verrät der Befehl `type`, der selbst eingebaut ist. Für Programmdateien nennt er den Ort der Datei.

::::beispiel Eingebaut oder Datei?
```console
$ type cd
cd is a shell builtin
$ type exit
exit is a shell builtin
$ type type
type is a shell builtin
$ type uname
uname is /usr/bin/uname
```

„Shell builtin“ ist der englische Fachausdruck für einen eingebauten Befehl. `cd`, `exit` und `type` erledigt bash selbst; für `uname` startet sie die Datei `/usr/bin/uname`.
::::

**Warum cd eingebaut sein muss.** Jedes laufende Programm hat seinen eigenen aktuellen Ordner, so wie jede Shell in Unterabschnitt [1.5](terminal-und-shell.html#stufe-1-5) ihren eigenen hatte. Startet die Shell ein Programm, bekommt es eine Kopie ihres aktuellen Ordners mit. Ändert das Programm diesen Ordner, ändert es nur seine Kopie, und wenn es endet, ist die Kopie verloren. Ein Programm `/usr/bin/cd` könnte deshalb nichts bewirken: Es würde den Ordner wechseln, sofort enden, und die Shell stünde genau dort, wo sie vorher war. Abbildung [11](#abb-11) zeigt beide Fälle. Nur die Shell selbst kann ihren eigenen Ordner wechseln, also muss `cd` ein Teil der Shell sein. Dasselbe gilt für `exit`, das die Shell selbst beenden soll.

:::abbildung linux/k2cd 11
Links ein gedachtes Programm `cd`: Es wechselt nur seine eigene Kopie des Ordners und endet; die Shell bleibt in `~`. Rechts der eingebaute Befehl: Die Shell wechselt ihren eigenen Ordner, und die Eingabeaufforderung zeigt `/etc`.
:::

⁠**Kurz gesagt:** Eingebaute Befehle erledigt die Shell selbst; Befehle wie `cd` und `exit`, die die Shell selbst verändern, müssen eingebaut sein.

:::hintergrund Was Systemaufrufe und der Standard dazu sagen
Den aktuellen Ordner verwaltet der Kernel für jedes laufende Programm getrennt. Der Systemaufruf, mit dem ein Programm ihn wechselt, heißt `chdir`, und er wirkt laut seiner Beschreibung nur auf das aufrufende Programm selbst. Ein neu gestartetes Programm erbt eine Kopie des Ordners des Programms, das es gestartet hat, kann aber umgekehrt dessen Ordner nie ändern. Der Standard POSIX zieht daraus ausdrücklich den Schluss, dass `cd` immer in die Shell eingebaut sein muss, weil es die Umgebung der Shell selbst betrifft. Aus demselben Grund sind `exit`, `history` und `type` eingebaut: Das erste beendet die Shell, das zweite liest ihre Liste der getippten Befehle, das dritte fragt ab, was die Shell mit einem Namen anfangen würde. Andere Befehle sind nur der Geschwindigkeit wegen eingebaut, siehe den nächsten Kasten.
:::

:::hintergrund Warum es manche Befehle doppelt gibt
Mit der Option `-a` zeigt `type` alle Fundstellen eines Namens, nicht nur die erste:

```console
$ type -a echo
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
```

`echo` gibt es also eingebaut und als Datei. Die eingebaute Fassung ist schneller, weil die Shell dafür kein neues Programm starten muss, und sie gewinnt, weil die Shell eingebaute Befehle vor dem Suchpfad prüft. Die Datei braucht man trotzdem: Manche Programme starten selbst andere Programme, und die können nur Dateien starten, keine Teile einer Shell. POSIX verlangt deshalb, dass Standardbefehle wie `echo`, `printf`, `pwd` und `test` auch als Datei vorhanden sind; `cd` ist ausgenommen, weil eine Datei dieses Namens nichts bewirken könnte. Ältere Fassungen des Standards verlangten auch dafür eine Datei; deshalb liefern manche Distributionen wie Fedora noch eine Datei `/usr/bin/cd` mit, die den Ordner der Shell natürlich ebenso wenig ändern kann. Dass `/usr/bin/echo` und `/bin/echo` beide erscheinen, liegt daran, dass `/bin` auf heutigen Systemen nur ein zweiter Name für den Ordner `/usr/bin` ist und beide im Suchpfad stehen; es ist dieselbe Datei.
:::

### Der Alias

<span class="anker" id="stufe-3-4"></span>

Fragt man unter Ubuntu `type` nach `ls`, kommt eine dritte Antwort, weder „builtin“ noch eine Datei:

```console
$ type ls
ls is aliased to `ls --color=auto'
```

Wer `ls` tippt, bekommt also gar nicht genau `ls`.

**Ein Kürzel, das ersetzt wird.** Wie ein Kürzel auf dem Handy, das beim Tippen „mfg“ durch „Mit freundlichen Grüßen“ ersetzt, tauscht die Shell bestimmte Befehlsnamen gegen einen hinterlegten Text aus, bevor sie die Zeile weiter bearbeitet (ein Bild zur Orientierung). Abbildung [12](#abb-12) zeigt den Austausch.

:::abbildung linux/k2alias 12
Der Alias `ls`: Beim Einlesen ersetzt die Shell das erste Wort durch den hinterlegten Text `ls --color=auto`. Erst danach sucht sie den Befehl `ls` und findet die Programmdatei.
:::

:::definition Definition 3.4 (Alias)
<span class="anker" id="satz-3-4"></span>

Ein __Alias__ ist ein Name, den die Shell beim Einlesen einer Befehlszeile durch einen hinterlegten Text ersetzt, wenn er als Befehl am Anfang steht. Erst danach sucht sie den Befehl, der im ersetzten Text vorn steht.
:::

Ubuntu hinterlegt in jeder Sitzung einige Aliase. `ls` wird zu `ls --color=auto`, damit die Liste farbig erscheint, und `ll` wird zu `ls -alF`, einer ausführlichen Liste. Aliase gelten nur in Sitzungen, in denen ein Mensch tippt; ein Programm, das selbst `ls` startet, bekommt die gewöhnliche Programmdatei.

::::beispiel Kürzel von Ubuntu
```console
$ type ll
ll is aliased to `ls -alF'
$ type la
la is aliased to `ls -A'
```

Einen Befehl `ll` gibt es als Datei nicht. Er existiert nur als Alias in deiner Sitzung, und die Shell macht daraus vor der Suche `ls -alF`, woraus mit dem Alias `ls` wiederum `ls --color=auto -alF` wird.
::::

⁠**Kurz gesagt:** Ein Alias ist ein Kürzel, das die Shell vor der Suche durch einen längeren Befehl ersetzt.

### Was hinter einem Namen steckt: type und which

<span class="anker" id="stufe-3-5"></span>

Mit `type` und `which` gibt es zwei Werkzeuge für die Frage, was hinter einem Befehlsnamen steckt. Sie antworten nicht immer gleich, und der Grund dafür sagt viel über die Shell.

:::abbildung linux/k2arten 13
Wie die Shell einen Namen auflöst, als Weiche: zuerst Alias, dann Schlüsselwort, Funktion und eingebauter Befehl, zuletzt der Suchpfad. `type` kennt alle Stationen, weil es Teil der Shell ist; `which` ist eine eigene Programmdatei und sieht nur den Suchpfad.
:::

`type` ist in die Shell eingebaut und kennt deshalb alles, was die Shell kennt: Aliase, eingebaute Befehle und die Programmdateien im Suchpfad. `which` dagegen ist selbst eine Programmdatei, `/usr/bin/which`. Als eigenes Programm sieht es nur die Ordner des Suchpfads, nicht das Innere der Shell, die es gestartet hat. Für eingebaute Befehle und Aliase findet es deshalb nichts oder nur die Datei, die gar nicht zum Zug käme. Tabelle [1](#tab-1) stellt beide gegenüber.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** `type` und `which` im Vergleich. Nur `type` beschreibt, was beim Tippen des Namens wirklich geschieht.

| Name | `type` antwortet | `which` antwortet |
|---|---|---|
| `uname` | `uname is /usr/bin/uname` | `/usr/bin/uname` |
| `cd` | `cd is a shell builtin` | nichts |
| `echo` | `echo is a shell builtin` | `/usr/bin/echo`, das beim Tippen nicht zum Zug kommt |
| `ls` | `ls is aliased to `ls --color=auto'` | `/usr/bin/ls`, ohne den Alias |
| `ll` | `ll is aliased to `ls -alF'` | nichts |

::::beispiel Die kurze Antwort und alle Antworten
Mit `-t` antwortet `type` mit einem einzigen Wort je Name, mit `-a` nennt es alle Fundstellen in der Reihenfolge, in der die Shell sie prüft:

```console
$ type -t ls cd uname
alias
builtin
file
$ type -a ls
ls is aliased to `ls --color=auto'
ls is /usr/bin/ls
ls is /bin/ls
$ which ls
/usr/bin/ls
```

Das Wort `file` steht für eine Programmdatei. Die erste Zeile von `type -a ls` ist die, die beim Tippen gilt.
::::

⁠**Kurz gesagt:** `type` sagt, was die Shell mit einem Namen tut; `which` findet nur Programmdateien im Suchpfad.

:::hintergrund Wie die Shell einen Befehl findet
bash geht für das erste Wort einer Zeile in fester Reihenfolge vor.

<ol>

<li>

Schon beim Einlesen ersetzt sie einen Alias durch seinen Text. Deshalb steht der Alias vor allen anderen Stationen.

</li>

<li>

Ist das Wort ein Schlüsselwort der Shellsprache wie `if`, verarbeitet sie es selbst; `type if` antwortet `if is a shell keyword`.

</li>

<li>

Hat jemand in der Sitzung eine *Funktion* dieses Namens festgelegt, einen kleinen Befehl aus Shell-Befehlen, führt sie diese aus. Dieses Kapitel legt keine an.

</li>

<li>

Ist es ein eingebauter Befehl, führt sie ihn aus.

</li>

<li>

Erst dann sucht sie im Suchpfad. Wo sie einen Namen schon einmal gefunden hat, merkt sie sich den Ort, damit sie beim nächsten Mal nicht suchen muss.

</li>

</ol>

Enthält das Wort einen Schrägstrich, etwa `/usr/bin/uname`, sucht sie gar nicht, sondern startet genau diese Datei. Findet sie nichts, meldet sie `command not found`; unter Ubuntu schaut dann noch ein kleines Hilfsprogramm nach, ob ein ähnlich benannter Befehl installiert werden könnte. Dass `which` auf Debian und Ubuntu selbst nur eine kurze Datei mit Shell-Befehlen ist, die die Ordner des Suchpfads abfragt, passt ins Bild; seine Handbuchseite sagt ausdrücklich, dass es nur den Suchpfad durchsucht. Wer wissen will, was beim Tippen eines Namens wirklich geschieht, fragt deshalb `type`, das der Standard POSIX für genau diesen Zweck vorsieht.
:::

### Aufgaben zu Abschnitt [3](#stufe-3)

<span class="anker" id="stufe-3-6"></span>

:::aufgabe Aufgabe 8 ★ Acht Namen einordnen
<span class="anker" id="aufg-8"></span>

Finde mit `type` heraus, was hinter diesen Namen steckt, und ordne sie den drei Arten zu: `cd`, `ls`, `echo`, `pwd`, `type`, `uname`, `history`, `ll`. Welche gibt es zusätzlich als Programmdatei? Prüfe es mit `type -a`.

:::loesung
```console
$ type -a cd ls echo pwd type uname history ll
cd is a shell builtin
ls is aliased to `ls --color=auto'
ls is /usr/bin/ls
ls is /bin/ls
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
pwd is a shell builtin
pwd is /usr/bin/pwd
pwd is /bin/pwd
type is a shell builtin
uname is /usr/bin/uname
uname is /bin/uname
history is a shell builtin
ll is aliased to `ls -alF'
```

Eingebaut sind `cd`, `echo`, `pwd`, `type` und `history`. Ein Alias sind `ls` und `ll`. Eine Programmdatei ist `uname`. Zusätzlich als Programmdatei gibt es `echo`, `pwd` und, hinter dem Alias, `ls`. Jede Datei erscheint zweimal, unter `/usr/bin` und unter `/bin`, weil beide Ordner im Suchpfad stehen und `/bin` nur ein zweiter Name für `/usr/bin` ist. Die erste Zeile zu jedem Namen ist die, die beim Tippen gilt.
:::
:::

:::aufgabe Aufgabe 9 ★★ type gegen which
<span class="anker" id="aufg-9"></span>

Sage vorher, was `which` für `cd`, `ll`, `uname` und `echo` ausgibt, und prüfe es. Bei welchen Namen gibt `which` eine irreführende Antwort, und woran liegt das?

:::loesung
```console
$ which cd
$ which ll
$ which uname
/usr/bin/uname
$ which echo
/usr/bin/echo
```

Für `cd` und `ll` gibt `which` nichts aus: `cd` ist eingebaut, `ll` nur ein Alias, und beides kann `which` als eigenes Programm nicht sehen. Für `uname` stimmt die Antwort. Irreführend ist sie bei `echo`: Beim Tippen läuft die eingebaute Fassung, nicht `/usr/bin/echo`. Ebenso irreführend ist `which ls` mit `/usr/bin/ls`, denn beim Tippen gilt zuerst der Alias `ls --color=auto`. Der Grund ist in beiden Fällen derselbe: `which` durchsucht nur die Ordner des Suchpfads und weiß nichts vom Inneren der Shell, die es gestartet hat.
:::
:::

:::aufgabe Aufgabe 10 ★★ Ein Programm namens cd
<span class="anker" id="aufg-10"></span>

Angenommen, es gäbe eine Programmdatei `/usr/bin/cd`, die beim Start den aktuellen Ordner wechselt und sich dann beendet. Beschreibe Schritt für Schritt, was geschieht, wenn du `/usr/bin/cd /etc` tippst; der Schrägstrich vorn sorgt dafür, dass die Shell genau diese Datei startet. Wo steht die Shell danach? Warum hilft es nichts, wenn das Programm länger läuft?

:::loesung
Die Shell findet keinen Alias und keinen eingebauten Befehl, denn der Name enthält einen Schrägstrich, und startet die Datei `/usr/bin/cd` als neues Programm mit dem Argument `/etc`. Das Programm bekommt eine Kopie des aktuellen Ordners der Shell, also `/home/student`. Es wechselt seinen eigenen aktuellen Ordner nach `/etc` und beendet sich. Damit ist auch seine Kopie verschwunden. Die Shell zeigt die Eingabeaufforderung wieder, und zwar mit `~`, denn ihr eigener Ordner wurde nie berührt. Auch ein länger laufendes Programm hilft nicht: Es könnte seinen eigenen Ordner ändern, sooft es will, den der Shell erreicht es nie, weil der Kernel jedem laufenden Programm einen eigenen aktuellen Ordner gibt und der Systemaufruf `chdir` nur auf das aufrufende Programm wirkt.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Was muss eingebaut sein?
<span class="anker" id="aufg-11"></span>

Entscheide für jeden Befehl, ob er eingebaut sein *muss*, nur der Geschwindigkeit wegen eingebaut ist oder gut eine Programmdatei sein kann, und begründe: (a) `exit`, (b) `echo`, (c) `history`, (d) `uname`, (e) `type`.

:::loesung
(a) `exit` muss eingebaut sein. Es soll die Shell selbst beenden; ein anderes Programm könnte nur sich selbst beenden.

(b) `echo` ist nur der Geschwindigkeit wegen eingebaut. Ein Programm `/usr/bin/echo` erledigt dieselbe Aufgabe, es muss dafür aber erst gestartet werden. Die eingebaute Fassung spart diesen Aufwand, was bei vielen Aufrufen zählt.

(c) `history` muss eingebaut sein. Der Verlauf liegt im Arbeitsspeicher der Shell; ein anderes Programm kommt an diesen Speicher nicht heran. Es könnte höchstens die Datei `.bash_history` lesen, und die wird erst am Ende der Sitzung geschrieben.

(d) `uname` kann problemlos eine Programmdatei sein, und das ist es auch: Es fragt den Kernel nach Angaben über das System und braucht dafür nichts aus der Shell.

(e) `type` muss eingebaut sein. Es soll sagen, was die Shell mit einem Namen tun würde, und dafür braucht es ihre Aliase und ihre Liste eingebauter Befehle. Ein eigenes Programm wie `which` sieht beides nicht.
:::
:::
