---
title: Seitenrechte: Kernel, Code und Daten trennen
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120800
summary: Die Seitentabelle sagt nicht nur, wohin eine Seite gehört, sondern auch, wie man auf sie zugreifen darf.
tags: NX-Bit, W^X, SMEP, SMAP, Bereichsliste
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Die Seitentabelle sagt nicht nur, wohin eine Seite gehört, sondern auch, wie man auf sie zugreifen darf. Dieser Abschnitt zeigt die Rechte einer Seite und drei Grenzen, die damit entstehen: zwischen Programm und Kernelspeicher, zwischen Code und Daten und, in umgekehrter Richtung, zwischen dem Kernel und dem Speicher der Programme.
:::

### Die Rechte eines Seitentabelleneintrags

<span class="anker" id="stufe-7-1"></span>

Ein Seitentabelleneintrag ist bei x86-64 eine Zahl mit 64 Bit. Ein Teil davon ist die Nummer des Seitenrahmens; einzelne andere Bits legen fest, was mit der Seite geschehen darf.

:::definition Definition 7.1 (Rechte-Bits einer Seite)
<span class="anker" id="satz-7-1"></span>

Die wichtigsten Rechte-Bits eines Seitentabelleneintrags bei x86-64 sind:

<ul>

<li>

Bit 0, P (present): Der Eintrag ist gültig. Ist P gleich 0, löst jeder Zugriff einen Seitenfehler aus.

</li>

<li>

Bit 1, R/W (read/write): Ist es 1, darf die Seite beschrieben werden, sonst nur gelesen.

</li>

<li>

Bit 2, U/S (user/supervisor): Ist es 1, darf Code auf Stufe 3 zugreifen; ist es 0, ist die Seite nur für Stufe 0 bis 2 zugänglich.

</li>

<li>

Bit 63, XD (execute disable): Ist es 1, darf der Prozessor aus dieser Seite keine Befehle holen. Das Bit wirkt, sobald der Kernel die Funktion beim Start eingeschaltet hat; Linux tut das auf jedem Prozessor, der sie kennt.

</li>

</ul>

Die Rechte wirken über alle Stufen der Tabelle: Verbietet eine Stufe etwas, ist es für die ganze Seite verboten. Die MMU prüft sie bei jedem Zugriff.
:::

Abbildung [27](#abb-27) zeigt einen Eintrag mit diesen Bits.

:::abbildung cyber/k2eintrag 27
Ein Seitentabelleneintrag als Leiste mit 64 Feldern, Bit 63 links, Bit 0 rechts. Nacheinander leuchten auf: Bit 0 „P vorhanden“, Bit 1 „R/W schreibbar“, Bit 2 „U/S für Programme zugänglich“, Bit 63 „XD nicht ausführbar“, dazwischen der Bereich „Nummer des Seitenrahmens“. Unten der Beispielwert `0x800000000a3b5067` mit den gesetzten Bits und der Deutung „Daten eines Programms: vorhanden, schreibbar, für Programme, nicht ausführbar“.
:::

::::beispiel Einen Eintrag deuten
Der Eintrag `0x800000000a3b5067` endet auf `67`, binär `0110 0111`. Die untersten drei Bits sind `111`: P, R/W und U/S sind gesetzt. Die erste Ziffer `8` ist binär `1000`, also ist Bit 63 gesetzt: XD. Der Rahmen hat die Nummer `0xa3b5`. Das ist eine typische Seite mit Daten eines Programms: vorhanden, beschreibbar, auf Stufe 3 zugänglich und nicht ausführbar.
::::

⁠**Kurz gesagt:** Jeder Seitentabelleneintrag trägt Rechte für Schreiben, Zugang von Stufe 3 und Ausführen, und die MMU prüft sie bei jedem Zugriff.

### Der Kernel in jedem Adressraum

<span class="anker" id="stufe-7-2"></span>

Bei jedem Eintritt in den Kernel muss der Kernel sofort seinen Code und seine Daten erreichen, und bei einem Systemaufruf muss er Daten aus dem Speicher des Programms kopieren. Am einfachsten geht das, wenn beides im selben Adressraum liegt.

:::satz Satz 7.2 (Kernel in jedem Adressraum)
<span class="anker" id="satz-7-2"></span>

Linux trägt seinen eigenen Speicher in die obere Hälfte des Adressraums jedes Prozesses ein, ab `0xffff800000000000`. Die Seiten des Kernels tragen U/S = 0. Auf Stufe 0 sind sie benutzbar, ein Zugriff von Stufe 3 löst einen Seitenfehler aus.
:::

Ein Programm sieht den Kernel also gewissermaßen hinter Glas: Die Adressen existieren in seinem Adressraum, aber die MMU lässt keinen Zugriff von Stufe 3 durch.

::::beispiel Dieselbe Kerneladresse auf zwei Wegen
Über die Tür des Kernels hat `tuer.py` in Unterabschnitt [4.4](der-eintritt-in-den-kernel.html#stufe-4-4) versucht, sechs Bytes ab `0xffffffff81000000` ausgeben zu lassen, und der Kernel hat mit `EFAULT` abgelehnt. Liest ein Programm dieselbe Adresse selbst, greift die MMU ein:

```console
$ python3 -c 'import ctypes; ctypes.string_at(0xffffffff81000000, 1)'
Segmentation fault         python3 -c 'import ctypes; ctypes.string_at(0xffffffff81000000, 1)'
$ echo $?
139
```

Zwei Grenzen, zwei Prüfer: Beim Systemaufruf prüft der Kernel das Argument, beim direkten Zugriff prüft die MMU das U/S-Bit. Keiner der beiden Wege verrät ein Byte des Kernels.
::::

⁠**Kurz gesagt:** Der Kernel liegt in jedem Adressraum, aber das Bit U/S = 0 macht ihn für Programme unerreichbar.

:::hintergrund Auch Hardwaregrenzen können Lücken haben
2018 wurde bekannt, dass viele Prozessoren das U/S-Bit bei vorausschauend ausgeführten Befehlen zu spät prüften. Ein Programm konnte so über Umwege Rückschlüsse auf Kernelspeicher ziehen, ohne dass je ein Seitenfehler zu sehen war; die Lücke heißt Meltdown. Betriebssysteme reagierten, indem sie auf betroffenen Prozessoren den Kernel bis auf ein kleines Stück aus den Seitentabellen der Programme entfernen und beim Eintritt in den Kernel die Tabelle wechseln; das kostet bei jedem Eintritt Zeit. Ob der eigene Prozessor betroffen ist, meldet Linux in einer Datei:

```console
$ cat /sys/devices/system/cpu/vulnerabilities/meltdown
Not affected
```

Der Fall zeigt, dass auch der Prozessor zur vertrauenswürdigen Basis gehört: Hat er einen Fehler, hält eine Grenze nicht, die auf dem Papier richtig gebaut ist.
:::

### Das NX-Bit

<span class="anker" id="stufe-7-3"></span>

Abschnitt [2](code-und-daten-im-selben-speicher.html#stufe-2) hat gezeigt, dass der Prozessor Bytes nicht ansieht, ob sie als Daten oder als Befehle gemeint waren. Das Bit XD aus Unterabschnitt [7.1](#stufe-7-1) schreibt genau diese Information in die Seitentabelle.

:::definition Definition 7.3 (NX-Bit)
<span class="anker" id="satz-7-3"></span>

Das __NX-Bit__ (no execute; Intel nennt es XD, execute disable) ist das Bit eines Seitentabelleneintrags, das das Holen von Befehlen aus der Seite verbietet. Zeigt der Befehlszeiger in eine solche Seite, löst die MMU einen Seitenfehler aus, und Linux schickt SIGSEGV.
:::

Jetzt lassen sich die Schritte 3 und 4 von `befehl.py` erklären. Das Speicherstück, das das Programm in Schritt 1 vom Kernel bekommt, ist genau eine Seite, lesbar und schreibbar, aber nicht ausführbar. In Schritt 3 bittet das Programm den Kernel mit dem Systemaufruf `mprotect`, die Rechte zu ändern: lesbar und ausführbar, nicht mehr schreibbar. Mit der Angabe `rw` lässt es Schritt 3 aus. Schritt 4 zeigt die Rechte so, wie der Kernel sie in `/proc/self/maps` angibt: `r` lesbar, `w` schreibbar, `x` ausführbar, ein Strich für ein fehlendes Recht.

::::beispiel Dieselben Bytes, andere Rechte
```console
$ python3 befehl.py rechnen rw
Stück 0x70a25bc8c000: Rechte rw-p
Segmentation fault         python3 befehl.py rechnen rw
$ echo $?
139
$ python3 befehl.py rechnen rx
Stück 0x787bad623000: Rechte r-xp
Ergebnis: 42
```

Beide Male stehen dieselben sechs Bytes in der Seite, und beide Male setzt das Programm den Befehlszeiger darauf. Mit `rw-p` ist das NX-Bit gesetzt, und der erste Versuch, einen Befehl zu holen, endet mit einem Seitenfehler und SIGSEGV. Mit `r-xp` läuft der Befehl. Ob der eigene Prozessor das Bit kennt, zeigt `/proc/cpuinfo`:

```console
$ grep -o -w -E 'nx|smep|smap' /proc/cpuinfo | sort | uniq -c
     14 nx
     14 smap
     14 smep
```

Jeder der 14 Kerne meldet `nx`; die beiden anderen Zeichen erklärt Unterabschnitt [7.5](#stufe-7-5).
::::

Abbildung [28](#abb-28) stellt die beiden Läufe nebeneinander.

:::abbildung cyber/k2nx 28
Zwei Spalten mit derselben Seite und denselben Bytes `B8 2A 00 00 00 C3`. Links trägt die Seite „rw-p, NX gesetzt“: Der Pfeil von `rip` trifft auf die Seite, die MMU zeigt ein rotes Kreuz „Befehl holen verboten“, es folgen „Seitenfehler“ und „SIGSEGV“. Rechts trägt die Seite „r-xp“: Derselbe Pfeil, die MMU zeigt ein Häkchen, „Ergebnis: 42“. Über beiden Spalten: „gleiche Bytes, anderes Bit“. Darüber ein Terminal mit den beiden echten Läufen von `befehl.py`.
:::

⁠**Kurz gesagt:** Das NX-Bit verbietet, aus einer Seite Befehle zu holen, und zieht so die Grenze zwischen Daten und Code, die der gemeinsame Speicher aufgehoben hat.

:::hintergrund Warum das NX-Bit die Antwort auf das Von-Neumann-Prinzip ist
Der Hintergrund am Ende von Abschnitt [2](code-und-daten-im-selben-speicher.html#stufe-2) hat festgestellt, dass die Information „das waren Daten“ nirgends im Speicher steht und der Prozessor sie deshalb nicht beachten kann. Das NX-Bit schreibt sie nicht in die Bytes, sondern in die Seitentabelle, und zwar seitenweise. Gesetzt wird es vom Kernel, der weiß, welche Bereiche eines Programms Code enthalten: die Teile der Programmdatei, die als Code gekennzeichnet sind. Stapel, Speicher für Eingaben und andere Daten bekommen das Bit. Geprüft wird es von der MMU bei jedem Holen eines Befehls, also ohne Lücke. Daten, die ein Angreifer in einen Datenbereich schreibt, laufen deshalb nicht mehr, selbst wenn er den Befehlszeiger dorthin lenkt. Die Grenze zwischen Code und Daten, die der gemeinsame Speicher aufgehoben hat, kehrt als Recht der Seite zurück. AMD führte das Bit 2003 mit seinen ersten 64-Bit-Prozessoren ein, Intel kurz danach unter dem Namen XD.
:::

### Die Regel W^X

<span class="anker" id="stufe-7-4"></span>

Das NX-Bit nützt nur, wenn keine Seite zugleich beschreibbar und ausführbar ist. Sonst könnte man in eine solche Seite schreiben und dann dort Befehle holen.

:::definition Definition 7.4 (W^X)
<span class="anker" id="satz-7-4"></span>

Nach der Regel __W^X__ („W xor X“, schreibbar oder ausführbar) ist jede Seite entweder beschreibbar oder ausführbar, nie beides zugleich. Unter Windows heißt der Schutz durch nicht ausführbare Seiten Datenausführungsverhinderung (DEP).
:::

`befehl.py` hält sich an die Regel: Es schreibt, solange die Seite `rw-` ist, und macht sie erst danach `r-x`. Der Name stammt vom Betriebssystem OpenBSD, das die Regel 2003 einführte. Abbildung [29](#abb-29) zeigt die erlaubte Reihenfolge.

:::abbildung cyber/k2wx 29
Eine Seite als Kasten mit drei Schaltern `r`, `w`, `x`. Schritt 1: `r` und `w` an, `x` aus; ein Stift schreibt `B8 2A 00 00 00 C3` hinein (Häkchen „schreiben“), ein Versuch, dort einen Befehl zu holen, prallt ab. Schritt 2: Ein Pfeil „`mprotect`, beim Kernel beantragt“ legt `w` aus und `x` an. Schritt 3: `rip` zeigt auf die Seite, „Ergebnis: 42“; ein Versuch, jetzt hineinzuschreiben, prallt ab. Daneben ein durchgestrichener Kasten mit allen drei Schaltern an: „`rwx`: verboten nach W^X“.
:::

::::beispiel Keine Seite mit w und x
In der Spalte mit den Rechten einer Zeile von `/proc/self/maps` (dem zweiten Feld) dürfen `w` und `x` nicht gemeinsam vorkommen. `awk` aus [Linux, Kapitel 6, Abschnitt 9](/wissen/informatik/linux-und-kommandozeile/textwerkzeuge-und-regulare-ausdrucke/rechnen-mit-spalten-awk.html#stufe-9) gibt alle Zeilen aus, auf die beides zutrifft:

```console
$ awk '$2 ~ /w/ && $2 ~ /x/' /proc/self/maps
$ echo $?
0
```

`awk` liest hier seine eigene Datei `/proc/self/maps` und findet keine Zeile: Der Prozess hält W^X ein. Der Exit-Status 0 sagt nur, dass `awk` fehlerfrei gelaufen ist, nicht, ob es Zeilen gefunden hat.
::::

⁠**Kurz gesagt:** W^X verlangt, dass jede Seite beschreibbar oder ausführbar ist, aber nicht beides.

Eine Grenze hat diese Regel, und sie ist wichtig: NX und W^X verhindern, dass *neu eingeschleuste* Bytes als Befehle laufen. Sie verhindern nicht, dass ein Angreifer *vorhandenen* Code des Programms und seiner Bibliotheken in einer Reihenfolge ausführen lässt, die niemand vorgesehen hat. Ein Programmfehler, der den Befehlszeiger lenken lässt, bleibt deshalb gefährlich.

:::hintergrund Programme, die zur Laufzeit Code erzeugen
Manche Programme müssen Befehle selbst schreiben und dann ausführen, genau wie `befehl.py`. Die JavaScript-Maschinen der Browser übersetzen häufig benutzte Teile einer Webseite zur Laufzeit in Maschinenbefehle, weil sie dann viel schneller laufen. Früher ließen sie solche Seiten einfach beschreibbar und ausführbar zugleich. Viele halten heute W^X ein: Sie schreiben den Code in eine Seite, die gerade beschreibbar ist, und schalten sie mit `mprotect` (unter Windows mit einer entsprechenden Funktion) auf ausführbar um, bevor sie dort Befehle holen. Firefox tut das seit 2016 standardmäßig. Das kostet ein wenig Zeit bei jedem Umschalten, verkleinert aber die Angriffsfläche: Es gibt keinen Moment mehr, in dem eine Seite für beides offen steht.
:::

### SMEP und SMAP

<span class="anker" id="stufe-7-5"></span>

Die bisherigen Rechte schützen den Kernel vor den Programmen. Es gibt auch die umgekehrte Richtung: Der Kernel soll den Speicher der Programme nur dort benutzen, wo er es ausdrücklich will. Hat der Kernel einen Fehler und folgt einem Zeiger in die untere Hälfte, landete er sonst in Speicher, den ein Programm nach Belieben vorbereitet hat.

:::definition Definition 7.5 (SMEP, SMAP)
<span class="anker" id="satz-7-5"></span>

__SMEP__ (supervisor mode execution prevention) ist eine Einstellung des Prozessors, die verbietet, auf Stufe 0 Befehle aus Seiten zu holen, die für Stufe 3 zugänglich sind (U/S = 1). __SMAP__ (supervisor mode access prevention) verbietet, auf Stufe 0 auf solche Seiten lesend oder schreibend zuzugreifen, außer der Kernel erlaubt es vorher ausdrücklich mit einem eigenen Befehl und nimmt die Erlaubnis gleich danach zurück.
:::

Beide Einstellungen kann nur Stufe 0 einschalten, und Linux schaltet sie ein, wenn der Prozessor sie kennt. Die kurze Erlaubnis für SMAP erteilt Linux nur in den wenigen Funktionen, die gezielt auf den Speicher eines Programms zugreifen, vor allem in den Kopierfunktionen aus Unterabschnitt [4.4](der-eintritt-in-den-kernel.html#stufe-4-4), also genau an den Stellen, an denen es Argumente aus dem Speicher eines Programms holt oder Ergebnisse dorthin schreibt. Abbildung [30](#abb-30) zeigt den Unterschied.

:::abbildung cyber/k2smap 30
Der Adressraum mit unterer Hälfte „Programm (U/S = 1)“ und oberer Hälfte „Kernel (U/S = 0)“. Der Kernel läuft auf Stufe 0. Ein fehlerhafter Pfeil „Kernel folgt einem Zeiger“ zeigt in die untere Hälfte, auf vom Programm vorbereitete Bytes: Mit SMEP prallt das Befehlsholen ab, mit SMAP das Lesen. Dann ein zweiter Pfeil aus der Funktion `copy_from_user`: Ein Schalter „Zugriff kurz erlaubt“ geht an, die Bytes werden kopiert, der Schalter geht wieder aus.
:::

::::beispiel Was die Einstellungen abfangen
Angenommen, ein Fehler in einem Treiber lässt den Kernel eine Funktionsadresse aus einer Tabelle lesen, die ein Programm überschrieben hat, und die Adresse zeigt in den Speicher des Programms. Ohne SMEP würde der Kernel dort auf Stufe 0 Befehle ausführen, die das Programm hineingeschrieben hat. Mit SMEP löst bereits das Holen des ersten Befehls einen Seitenfehler im Kernel aus, und Linux beendet den betroffenen Vorgang mit einer Fehlermeldung, statt fremden Code mit allen Rechten auszuführen. In der Ausgabe von `/proc/cpuinfo` im Beispiel „Dieselben Bytes, andere Rechte“ melden alle 14 Kerne `smep` und `smap`.
::::

⁠**Kurz gesagt:** SMEP und SMAP verbieten dem Kernel, Befehle oder Daten aus dem Speicher der Programme zu nehmen, außer an den Stellen, die dafür gebaut sind.

### Seitenrechte beobachten: /proc/self/maps

<span class="anker" id="stufe-7-6"></span>

Welche Bereiche ein Prozess hat und welche Rechte sie tragen, zeigt der Kernel in der Datei `/proc/<Prozessnummer>/maps`, für den lesenden Prozess selbst unter `/proc/self/maps`.

:::definition Definition 7.6 (Bereichsliste)
<span class="anker" id="satz-7-6"></span>

Die __Bereichsliste__ `/proc/<Prozessnummer>/maps` zeigt je Zeile einen zusammenhängenden Bereich des Adressraums mit gleichen Rechten. Die Felder sind: Anfang und Ende als virtuelle Adressen (das Ende gehört nicht mehr dazu), die Rechte, der Versatz in der Datei, das Gerät, die Inode und der Name. Die Rechte bestehen aus `r`, `w` und `x` und einem vierten Zeichen: `p` für privat (beim Schreiben bekommt der Prozess eine eigene Kopie), `s` für geteilt. Ein Name in eckigen Klammern bezeichnet einen besonderen Bereich, ein fehlender Name einen Bereich ohne Datei.
:::

Die besonderen Namen sind `[heap]` für den Speicher, den ein Programm während des Laufs nach und nach anfordert, `[stack]` für den Stapel, auf dem es die Daten seiner gerade laufenden Funktionen ablegt, und `[vdso]` und `[vvar]` für ein kleines Stück Code und Daten, das der Kernel jedem Prozess mitgibt, damit Abfragen wie die Uhrzeit ohne Eintritt in den Kernel gehen.

::::beispiel Die Bereiche von cat
`cat` liest hier seine eigene Bereichsliste; die mittleren Zeilen mit weiteren Bibliotheken sind weggelassen. Unter Ubuntu 26.04 steckt `cat` in der gemeinsamen Datei der uutils ([Linux, Kapitel 2, Abschnitt 7.2](/wissen/informatik/linux-und-kommandozeile/die-shell-erste-befehle/zwei-fassungen-der-grundbefehle-gnu-und-uutils.html#stufe-7-2)); auf anderen Systemen steht dort `/usr/bin/cat`.

```text
$ cat /proc/self/maps
62a019dc1000-62a019eb3000 r--p 00000000 08:30 1547    /usr/lib/cargo/bin/coreutils/cat
62a019eb3000-62a01a36b000 r-xp 000f2000 08:30 1547    /usr/lib/cargo/bin/coreutils/cat
62a01a36b000-62a01a72a000 r--p 005aa000 08:30 1547    /usr/lib/cargo/bin/coreutils/cat
62a01a72a000-62a01a88f000 r--p 00968000 08:30 1547    /usr/lib/cargo/bin/coreutils/cat
62a01a88f000-62a01a895000 rw-p 00acd000 08:30 1547    /usr/lib/cargo/bin/coreutils/cat
62a01a895000-62a01a896000 rw-p 00000000 00:00 0
62a0343be000-62a034400000 rw-p 00000000 00:00 0       [heap]
75980fa00000-75980fa28000 r--p 00000000 08:30 13613   /usr/lib/x86_64-linux-gnu/libc.so.6
75980fa28000-75980fbc0000 r-xp 00028000 08:30 13613   /usr/lib/x86_64-linux-gnu/libc.so.6
75980fbc0000-75980fc0e000 r--p 001c0000 08:30 13613   /usr/lib/x86_64-linux-gnu/libc.so.6
75980fc0e000-75980fc12000 r--p 0020e000 08:30 13613   /usr/lib/x86_64-linux-gnu/libc.so.6
75980fc12000-75980fc14000 rw-p 00212000 08:30 13613   /usr/lib/x86_64-linux-gnu/libc.so.6
...
75980ff3d000-75980ff3e000 ---p 00000000 00:00 0
...
7ffe148ff000-7ffe14920000 rw-p 00000000 00:00 0       [stack]
7ffe149f5000-7ffe149f9000 r--p 00000000 00:00 0       [vvar]
7ffe149f9000-7ffe149fb000 r-xp 00000000 00:00 0       [vdso]
```

Die Programmdatei erscheint in mehreren Zeilen: Ihr Code als `r-xp`, Konstanten als `r--p`, die Daten des Programms als `rw-p`. Dasselbe Muster zeigt `libc.so.6`. Heap und Stapel sind `rw-p`, also beschreibbar und nicht ausführbar. Die Zeile mit `---p` ist ein Bereich ohne jedes Recht; er trennt andere Bereiche, damit ein Zugriff, der über das Ende hinausläuft, einen Seitenfehler auslöst statt in fremde Daten zu geraten. Keine Zeile hat `w` und `x` zugleich. Alle Adressen liegen unter `0x0000800000000000`, in der Hälfte der Programme; den Kernel listet die Datei nicht auf. Auf vielen anderen Systemen steht am Ende noch eine Zeile `[vsyscall]` mit einer Adresse in der Kernelhälfte: ein kleines, festes Stück, das der Kernel nur noch für sehr alte Programme bereithält und das niemand lesen kann; unter WSL 2 fehlt es.
::::

:::abbildung cyber/k2maps 31
Ein Ausschnitt der Bereichsliste von `cat` als Text. Nacheinander werden die Rechte farbig markiert: `r-xp` grün „Code“, `r--p` grau „nur lesen“, `rw-p` blau „Daten, nicht ausführbar“, `---p` rot „Schutzlücke“. Rechts daneben eine Leiste des Adressraums, in der dieselben Farben an ihren Adressen erscheinen, oben die leere Kernelhälfte mit „nicht aufgelistet“.
:::

⁠**Kurz gesagt:** `/proc/self/maps` zeigt die Bereiche eines Prozesses mit ihren Rechten; Code ist `r-x`, Daten sind `rw-`, und keine Seite ist beides.

### Aufgaben zu Abschnitt [7](#stufe-7)

<span class="anker" id="stufe-7-7"></span>

:::aufgabe Aufgabe 18 ★★ Einträge deuten
<span class="anker" id="aufg-18"></span>

Deute die Seitentabelleneinträge `0x000000000a3b4025`, `0x8000000001234063` und `0x0000000000000000`: Welche der Bits P, R/W, U/S und XD sind gesetzt, und was für eine Seite ist es jeweils (Code eines Programms, Daten eines Programms, Speicher des Kernels, kein gültiger Eintrag)?

:::loesung
<ul>

<li>

`0x000000000a3b4025`: Die letzten zwei Ziffern `25` sind binär `0010 0101`, also P = 1, R/W = 0, U/S = 1. Die erste Ziffer ist 0, also XD = 0. Die Seite ist vorhanden, nur lesbar, für Programme zugänglich und ausführbar: Code eines Programms, Rahmen `0xa3b4`.

</li>

<li>

`0x8000000001234063`: `63` ist binär `0110 0011`, also P = 1, R/W = 1, U/S = 0; die erste Ziffer `8` setzt XD = 1. Vorhanden, beschreibbar, nur für den Kernel, nicht ausführbar: Daten des Kernels, Rahmen `0x1234`.

</li>

<li>

`0x0000000000000000`: P = 0. Kein gültiger Eintrag; jeder Zugriff löst einen Seitenfehler aus. Die übrigen Bits haben keine Bedeutung.

</li>

</ul>
:::
:::

:::aufgabe Aufgabe 19 ★ Richtig oder falsch?
<span class="anker" id="aufg-19"></span>

Begründe jeweils: (a) „Der Kernel prüft jeden Speicherzugriff eines Programms.“ (b) „Mit dem NX-Bit sind Programmfehler, die den Befehlszeiger lenken lassen, harmlos.“ (c) „Ein Programm kann die Kerneladressen in seinem Adressraum nicht lesen, weil sie dort nicht eingetragen sind.“ (d) „Unter W^X kann ein Programm zur Laufzeit keinen Code erzeugen.“

:::loesung
(a) Falsch. Jeden Zugriff prüft die MMU in Hardware anhand der Seitentabelle. Der Kernel legt die Tabellen fest und wird erst bei einem Seitenfehler gerufen.

(b) Falsch. Das NX-Bit verhindert, dass neu eingeschleuste Bytes in Datenbereichen als Befehle laufen. Wer den Befehlszeiger lenken kann, kann aber vorhandenen Code des Programms und seiner Bibliotheken in einer Reihenfolge ausführen lassen, die niemand vorgesehen hat.

(c) Falsch. Linux trägt den Kernel in die obere Hälfte jedes Adressraums ein; die Seiten tragen aber U/S = 0, und die MMU weist Zugriffe von Stufe 3 ab. Auf Prozessoren, die von Meltdown betroffen sind, entfernt Linux zusätzlich den größten Teil des Kernels aus den Seitentabellen der Programme.

(d) Falsch. Es kann, muss aber die Rechte einer Seite umschalten: erst schreiben, solange sie beschreibbar ist, dann mit `mprotect` auf ausführbar und nicht mehr beschreibbar stellen. So arbeiten `befehl.py` und viele JavaScript-Maschinen der Browser.
:::
:::

:::aufgabe Aufgabe 20 ★★ Die Bereiche eines eigenen Prozesses
<span class="anker" id="aufg-20"></span>

Lies mit `cat /proc/self/maps` die Bereichsliste und ordne jede Zeile einer der Gruppen „Code“, „nur lesen“, „Daten“, „Heap“, „Stapel“, „vom Kernel mitgegeben“ und „ohne Recht“ zu. Prüfe mit dem `awk`-Befehl aus dem Beispiel „Keine Seite mit w und x“, ob die Regel W^X eingehalten ist. Wie viele Seiten umfasst der Stapel?

:::loesung
Die Zuordnung hängt vom Programm ab; bei `cat` auf dem Testsystem: Die Zeilen mit `r-xp` und dem Namen der Programmdatei oder einer Bibliothek sind Code; `r--p` mit Dateinamen sind Bereiche zum Lesen, etwa Konstanten; `rw-p` mit Dateinamen und die namenlosen `rw-p`-Zeilen dahinter sind Daten; `[heap]` und `[stack]` sind Heap und Stapel; `[vvar]` und `[vdso]` hat der Kernel mitgegeben, ebenso eine Zeile `[vsyscall]`, falls dein System sie zeigt; die Zeile mit `---p` ist ohne Recht. Der Befehl `awk '$2 ~ /w/ && $2 ~ /x/' /proc/self/maps` gibt nichts aus, die Regel W^X ist eingehalten. Der Stapel reichte im Beispiel von `7ffe148ff000` bis `7ffe14920000`; die Differenz ist $\texttt{0x21000}=135\,168$ Byte, also $135\,168/4096=33$ Seiten.
:::
:::

:::aufgabe Aufgabe 21 ★★★ Ein Programm, das gegen W^X verstößt
<span class="anker" id="aufg-21"></span>

Angenommen, `befehl.py` würde in Schritt 1 gleich eine Seite anfordern, die lesbar, beschreibbar und ausführbar ist, und Schritt 3 weglassen. (a) Würde `python3 befehl.py rechnen` noch 42 ausgeben? (b) Was zeigte Schritt 4 als Rechte an? (c) Warum ist eine solche Seite in einem Programm, das Daten aus dem Netz verarbeitet, ein Risiko, obwohl das Programm selbst nur seine eigenen Bytes hineinschreibt?

:::loesung
(a) Ja. Die Seite ist ausführbar, also läuft der Befehl, und das Programm gibt 42 aus.

(b) Schritt 4 würde die Rechte `rwxp` anzeigen. Der Prüfbefehl mit `awk` aus dem Beispiel „Keine Seite mit w und x“ würde diese Zeile finden.

(c) Das Programm schreibt zwar selbst nur eigene Bytes hinein, aber die Seite steht dauerhaft für beides offen. Hat das Programm einen Fehler, durch den Daten aus dem Netz an eine falsche Stelle geschrieben werden, und trifft dieser Fehler die offene Seite, landen dort fremde Bytes, die sofort ausführbar sind. Unter W^X müsste ein Angreifer zusätzlich erreichen, dass die Seite umgeschaltet wird; diese zusätzliche Hürde entfällt. Eine Seite mit `w` und `x` ist deshalb eine Stelle, an der die Grenze zwischen Daten und Code fehlt.
:::
:::
