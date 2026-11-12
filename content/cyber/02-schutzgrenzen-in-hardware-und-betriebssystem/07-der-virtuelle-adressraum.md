---
title: Der virtuelle Adressraum
pfad: Informatik / Cybersecurity / Schutzgrenzen in Hardware und Betriebssystem
adresse: informatik/cybersecurity/schutzgrenzen-in-hardware-und-betriebssystem
knoten: Kapitel 2: Schutzgrenzen in Hardware und Betriebssystem
order: 6120700
summary: Jeder Prozess hat seinen eigenen Speicher, und keiner soll den eines anderen lesen oder verändern.
tags: virtuelle Adresse, physische Adresse, virtuelle Adressraum, Seite, Seitenrahmen, Versatz, Seitentabelle, Seitentabelleneintrag
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Jeder Prozess hat seinen eigenen Speicher, und keiner soll den eines anderen lesen oder verändern. Dieser Abschnitt zeigt, wie der Prozessor bei jedem einzelnen Speicherzugriff dafür sorgt, wer die Tabellen dafür einrichtet und was geschieht, wenn ein Prozess eine Adresse benutzt, die für ihn nicht vorgesehen ist.
:::

### Die virtuelle Adresse

<span class="anker" id="stufe-6-1"></span>

Zwei Prozesse laufen gleichzeitig, und beide benutzen Adressen wie `0x7ffd3c2a1f48`. Schreibt der eine dorthin, darf sich beim anderen nichts ändern. Also kann dieselbe Adresse in den beiden Prozessen nicht dasselbe Byte im Arbeitsspeicher bezeichnen.

Man kann sich vorstellen, dass jeder Prozess seinen eigenen Stadtplan hat. Auf jedem Plan stehen Hausnummern, und dieselbe Hausnummer kann auf zwei Plänen zu zwei ganz verschiedenen Häusern führen. Wer nur seinen eigenen Plan besitzt, findet Häuser, die nicht darauf stehen, gar nicht. Das ist ein Bild zur Orientierung; die genaue Fassung ist die folgende.

:::definition Definition 6.1 (virtuelle und physische Adresse, virtueller Adressraum)
<span class="anker" id="satz-6-1"></span>

Eine __virtuelle Adresse__ ist eine Adresse, wie ein Programm sie benutzt. Eine __physische Adresse__ ist die Nummer eines Bytes im tatsächlich eingebauten Arbeitsspeicher. Der __virtuelle Adressraum__ eines Prozesses ist die Menge der virtuellen Adressen, die er benutzen kann, zusammen mit der Angabe, zu welchen physischen Adressen sie gehören.
:::

Jede Adresse, die ein Programm sieht, ist virtuell, zum Beispiel die Adresse seines eigenen Textes, die `tuer.py` in Unterabschnitt [4.4](der-eintritt-in-den-kernel.html#stufe-4-4) ausgegeben hat. Die physischen Adressen bekommt ein Programm nie zu sehen. Abbildung [22](#abb-22) zeigt zwei Adressräume.

:::abbildung cyber/k2stadtplan 22
Links zwei Prozesse A und B, jeder mit einem eigenen Streifen virtueller Adressen, in beiden ist die Adresse `0x7ffd3c2a1f48` markiert. In A steht dort 1, in B steht dort 2. Rechts der physische Arbeitsspeicher als ein Streifen. Pfeile führen von der markierten Adresse in A und in B zu zwei verschiedenen Stellen im physischen Speicher. Ein drittes Feld im physischen Speicher ohne Pfeil trägt „für A und B ohne Adresse“.
:::

::::beispiel Dieselbe Adresse in zwei Prozessen
Zwei Prozesse eines Tabellenprogramms speichern an der virtuellen Adresse `0x7ffd3c2a1f48` jeweils die Zahl der Zeilen ihrer gerade geöffneten Tabelle, der eine 1, der andere 2. Für Prozess A gehört die Adresse zur physischen Adresse `0x3a1f48`, für Prozess B zu `0x9c0f48`. Beide lesen an „derselben“ Adresse ihre eigene Zahl, und keiner kann die Zahl des anderen erreichen, denn in seinem Adressraum führt keine Adresse dorthin.
::::

⁠**Kurz gesagt:** Programme rechnen nur mit virtuellen Adressen, und welches Byte im Arbeitsspeicher dazu gehört, legt der Adressraum des jeweiligen Prozesses fest.

### Seite und Seitenrahmen

<span class="anker" id="stufe-6-2"></span>

Für jedes einzelne Byte festzuhalten, wohin es gehört, wäre viel zu aufwendig. Deshalb teilt man den Speicher in gleich große Blöcke und ordnet nur ganze Blöcke zu.

:::definition Definition 6.2 (Seite, Seitenrahmen, Versatz)
<span class="anker" id="satz-6-2"></span>

Eine __Seite__ ist ein Block aufeinanderfolgender virtueller Adressen fester Größe; auf x86-64-Rechnern sind es in der Regel 4096 Byte. Ein __Seitenrahmen__ ist ein gleich großer Block des physischen Arbeitsspeichers. Eine virtuelle Adresse zerfällt in die Nummer ihrer Seite und den __Versatz__, die Stelle innerhalb der Seite.
:::

Weil $4096=2^{12}$ ist, bilden die untersten 12 Bit einer Adresse den Versatz, in der Hexadezimalschreibweise also genau die letzten drei Ziffern. Die übrigen Bits sind die Seitennummer.

::::beispiel Seitennummer und Versatz
```console
$ getconf PAGESIZE
4096
```

Die Adresse `0x7ffd3c2a1f48` hat den Versatz `0xf48`, also $15\cdot256+4\cdot16+8=3912$, und die Seitennummer `0x7ffd3c2a1`. Die Adresse `0x7ffd3c2a2000` liegt bereits in der nächsten Seite, mit dem Versatz 0.
::::

⁠**Kurz gesagt:** Speicher wird seitenweise zugeordnet, und die letzten 12 Bit einer Adresse sind die Stelle in der Seite.

### Die Seitentabelle

<span class="anker" id="stufe-6-3"></span>

Für jeden Prozess muss irgendwo stehen, welche seiner Seiten zu welchem Seitenrahmen gehört. Das ist eine Tabelle, die der Kernel führt.

:::definition Definition 6.3 (Seitentabelle, Seitentabelleneintrag)
<span class="anker" id="satz-6-3"></span>

Die __Seitentabelle__ eines Prozesses ordnet jeder Seite, die der Prozess benutzen darf, einen Seitenrahmen zu. Ein __Seitentabelleneintrag__ enthält die Nummer des Seitenrahmens und Angaben darüber, wie auf die Seite zugegriffen werden darf. Seiten ohne gültigen Eintrag gehören nicht zum Adressraum des Prozesses. Die Seitentabellen legt der Kernel an, und sie liegen in seinem eigenen Speicher.
:::

Abbildung [23](#abb-23) zeigt eine Seitentabelle mit drei Einträgen.

:::abbildung cyber/k2seitentabelle 23
Eine virtuelle Adresse `0x00402abc` wird in „Seitennummer `0x402`“ und „Versatz `0xabc`“ geteilt. Daneben eine Seitentabelle mit drei Zeilen: `0x400` → Rahmen `0x1a7`, `0x401` → Rahmen `0x033`, `0x402` → Rahmen `0x2f0`. Die Zeile `0x402` leuchtet auf, der Rahmen `0x2f0` wird mit dem Versatz zusammengesetzt: physische Adresse `0x2f0abc`. Eine Anfrage mit Seitennummer `0x403` findet keine Zeile.
:::

::::beispiel Eine Adresse übersetzen
Ein Prozess hat die Einträge Seite `0x400` → Rahmen `0x1a7`, Seite `0x401` → Rahmen `0x033` und Seite `0x402` → Rahmen `0x2f0`. Er liest an der virtuellen Adresse `0x402abc`. Seitennummer `0x402`, Versatz `0xabc`; der Eintrag nennt den Rahmen `0x2f0`, also lautet die physische Adresse `0x2f0abc`. Ein Zugriff auf `0x403000` findet keinen Eintrag; diese Adresse gehört nicht zum Adressraum.
::::

⁠**Kurz gesagt:** Die Seitentabelle eines Prozesses sagt für jede seiner Seiten, in welchem Seitenrahmen sie liegt; angelegt wird sie vom Kernel.

### Die MMU

<span class="anker" id="stufe-6-4"></span>

Der Prozessor greift bei fast jedem Befehl auf den Speicher zu, oft mehrmals. Würde der Kernel jeden Zugriff selbst übersetzen und prüfen, liefen Programme um ein Vielfaches langsamer. Also muss die Hardware das übernehmen.

:::definition Definition 6.4 (MMU)
<span class="anker" id="satz-6-4"></span>

Die __MMU__ (memory management unit, Speicherverwaltungseinheit) ist ein Teil des Prozessors, der bei jedem Speicherzugriff die virtuelle Adresse anhand der Seitentabelle des laufenden Prozesses in eine physische übersetzt und dabei prüft, ob der Zugriff erlaubt ist. Findet sie keinen gültigen Eintrag oder ist der Zugriff nicht erlaubt, löst sie eine Ausnahme aus.
:::

Damit die Übersetzung schnell bleibt, merkt sich die MMU die zuletzt benutzten Einträge in einem kleinen Zwischenspeicher. Die Prüfung selbst entfällt dadurch nicht: Auch ein gemerkter Eintrag trägt die Angaben, wie zugegriffen werden darf.

::::beispiel Wer was tut, wenn ein Programm eine Zahl liest
Ein Programm liest eine Zahl an der Adresse `0x402abc`. Der Kernel ist dabei nicht beteiligt: Die MMU sucht den Eintrag für Seite `0x402`, findet den Rahmen `0x2f0`, prüft, dass Lesen erlaubt ist, und holt das Byte von `0x2f0abc`. Der Kernel hat die Tabelle vorher angelegt, und er kommt erst ins Spiel, wenn die MMU eine Ausnahme auslöst.
::::

⁠**Kurz gesagt:** Die MMU übersetzt und prüft jeden Speicherzugriff in Hardware; der Kernel legt nur die Tabellen fest.

### Das Wurzelregister

<span class="anker" id="stufe-6-5"></span>

Jeder Prozess hat seine eigene Seitentabelle. Woher weiß die MMU, welche gerade gilt?

:::definition Definition 6.5 (Wurzelregister)
<span class="anker" id="satz-6-5"></span>

Das __Wurzelregister__ ist ein Register des Prozessors, das die physische Adresse der Seitentabelle des gerade laufenden Prozesses enthält. Bei x86-64 heißt es CR3, bei RISC-V `satp`. Jeder Kern hat sein eigenes. Schreiben kann es nur Code auf Stufe 0; bei x86 ist es eines der Steuerregister aus Tabelle [1](privilegstufen-und-schutzringe.html#tab-1).
:::

Beim Kontextwechsel lädt der Kernel die Adresse der Seitentabelle des nächsten Prozesses in das Wurzelregister. Von diesem Moment an übersetzt die MMU mit dessen Tabelle, und der vorige Adressraum ist nicht mehr erreichbar. Abbildung [24](#abb-24) zeigt diesen Wechsel.

:::abbildung cyber/k2mmu 24
Links ein Kern mit MMU und dem Register CR3, in der Mitte die Seitentabellen von Prozess A und B im Speicher des Kernels, rechts der physische Arbeitsspeicher. Zuerst zeigt CR3 auf die Tabelle von A; ein Zugriff von A läuft durch die MMU, die Tabelle von A und landet in einem Rahmen von A. Dann kommt die Zeitgeber-Unterbrechung, der Kernel lädt die Adresse der Tabelle von B in CR3 („nur Stufe 0“). Ein Zugriff von B an derselben virtuellen Adresse landet nun in einem Rahmen von B. Ein Rahmen mit Programmcode trägt die Aufschrift „in beiden Tabellen“: Beide Tabellen verweisen auf ihn.
:::

::::beispiel Zwei Prozesse auf einem Kern
Prozess A rechnet, CR3 enthält die Adresse seiner Seitentabelle. Die Zeitgeber-Unterbrechung führt in den Kernel, der Planer wählt Prozess B. Der Kernel sichert den Stand von A, lädt die Adresse der Tabelle von B in CR3 und kehrt zu B zurück. Liest B nun an `0x7ffd3c2a1f48`, übersetzt die MMU mit der Tabelle von B. Auf einem zweiten Kern kann gleichzeitig ein dritter Prozess mit seiner eigenen Tabelle laufen, denn dieser Kern hat sein eigenes CR3.
::::

⁠**Kurz gesagt:** Welche Seitentabelle gilt, steht im Wurzelregister, und das stellt nur der Kernel um.

:::hintergrund Warum das Isolation ist: Was nicht in der Tabelle steht, hat keinen Namen
Ein Prozess kann auf ein Byte nur über eine virtuelle Adresse zugreifen, und jede seiner virtuellen Adressen wird durch seine eigene Seitentabelle übersetzt. Steht der Seitenrahmen eines anderen Prozesses in keiner seiner Zeilen, gibt es für ihn schlicht keine Adresse, die dorthin führt. Er kann den fremden Speicher nicht einmal benennen, geschweige denn lesen. Das ist eine stärkere Grenze als ein Verbot, das bei jedem Zugriff abgefragt wird: Es gibt nichts abzulehnen, weil es keinen Weg gibt. Die Grenze hält, solange drei Dinge stimmen: Die MMU übersetzt jeden Zugriff, die Tabellen liegen in Speicher, den der Prozess nicht beschreiben kann, und das Wurzelregister ist privilegiert. Ein Programm, das CR3 selbst setzen könnte, würde einfach eine eigene Tabelle einhängen, in der aller Speicher steht.
:::

### Der Seitenfehler

<span class="anker" id="stufe-6-6"></span>

Findet die MMU keinen gültigen Eintrag oder passt der Zugriff nicht zu den Angaben im Eintrag, kann sie den Befehl nicht ausführen. Das ist eine Ausnahme, und sie hat einen eigenen Namen.

:::definition Definition 6.6 (Seitenfehler)
<span class="anker" id="satz-6-6"></span>

Ein __Seitenfehler__ ist die Ausnahme, die die MMU bei einem Speicherzugriff auslöst, den die Seitentabelle nicht erlaubt, weil es keinen gültigen Eintrag gibt oder weil die Art des Zugriffs nicht zu den Angaben im Eintrag passt (bei x86 Ausnahme Nummer 14, englisch page fault, kurz #PF). Der Prozessor teilt dem Kernel dabei die Adresse mit und in einem Fehlercode, um welche Art von Zugriff es ging: ob die Seite vorhanden war, ob gelesen, geschrieben oder ein Befehl geholt werden sollte und ob der Zugriff von Stufe 3 kam.
:::

Der Kernel entscheidet dann. Gehört die Adresse zum Adressraum, nur liegt die Seite gerade nicht im Arbeitsspeicher, holt er sie und lässt den Befehl erneut laufen; das Programm merkt nichts davon. Ist der Zugriff nicht erlaubt, schickt Linux dem Prozess das Signal SIGSEGV. Abbildung [25](#abb-25) zeigt die beiden Wege.

:::abbildung cyber/k2seitenfehler 25
Ein Zugriff an eine Adresse löst „Seitenfehler“ aus, ein Pfeil führt auf Stufe 0 in den Kernel mit den Angaben „Adresse“ und „Art des Zugriffs“. Der Kernel fragt „Gehört die Adresse zum Adressraum und ist der Zugriff erlaubt?“. Weg „ja, Seite nur nicht geladen“: Seite holen, Eintrag setzen, Befehl wiederholen, Programm läuft weiter. Weg „nein“: SIGSEGV, Prozess endet, Status 139.
:::

::::beispiel Ein Zugriff ins Leere
Die Adresse `4096` (`0x1000`) liegt in einer Seite, die unter Linux zu keinem Adressraum gehört: Die untersten Adressen bis $65\,535$ darf ein gewöhnliches Programm in der Voreinstellung gar nicht belegen (`cat /proc/sys/vm/mmap_min_addr` zeigt auf dem Testsystem die Grenze 65536). Python kann mit `ctypes` ein Byte an einer beliebigen Adresse lesen:

```console
$ python3 -c 'import ctypes; ctypes.string_at(4096, 1)'
Segmentation fault         python3 -c 'import ctypes; ctypes.string_at(4096, 1)'
$ echo $?
139
```

Die MMU fand keinen Eintrag, der Kernel stellte fest, dass die Adresse nicht zum Adressraum gehört, und schickte SIGSEGV. Der Name des Signals stammt aus einer älteren Art, Speicher einzuteilen; heute steht er für jeden unerlaubten Speicherzugriff.
::::

⁠**Kurz gesagt:** Bei einem Seitenfehler entscheidet der Kernel: fehlende, aber erlaubte Seiten lädt er nach, unerlaubte Zugriffe beendet er mit SIGSEGV.

:::hintergrund Warum Seitenfehler meistens harmlos sind
Linux lädt ein Programm beim Start nicht vollständig in den Arbeitsspeicher. Es trägt zunächst nur ein, welche Bereiche zum Adressraum gehören, und lädt eine Seite erst, wenn das erste Mal auf sie zugegriffen wird, also bei einem Seitenfehler. Auch Seiten, die der Kernel bei Speichermangel auf den Datenträger ausgelagert hat, holt er bei einem Seitenfehler zurück. Auf einem gewöhnlichen Rechner gibt es so Tausende Seitenfehler je Sekunde, und fast alle enden still. Nur wenn der Zugriff zu keinem Bereich gehört oder die Art des Zugriffs nicht erlaubt ist, wird daraus ein Fehler des Programms. Manche Lehrbücher unterscheiden diese beiden Fälle als Zugriff ohne gültige Adresse und Zugriff mit falscher Art; Linux behandelt beide mit SIGSEGV.
:::

### Gemeinsame Seiten

<span class="anker" id="stufe-6-7"></span>

Fast jedes Programm unter Linux benutzt die C-Bibliothek `libc.so.6`. Hätte jeder Prozess seine eigene Kopie davon im Arbeitsspeicher, läge dieselbe Datei hundertfach im Speicher.

:::definition Definition 6.7 (gemeinsame Seite)
<span class="anker" id="satz-6-7"></span>

Eine __gemeinsame Seite__ ist ein Seitenrahmen, den der Kernel in die Seitentabellen mehrerer Prozesse einträgt. Alle diese Prozesse sehen denselben Inhalt, oft an verschiedenen virtuellen Adressen.
:::

Der Kernel teilt vor allem Programmcode und Bibliotheken, die niemand verändert, und Dateien, die mehrere Prozesse lesen. Das ist keine Lücke in der Isolation, sondern eine Entscheidung des Kernels, für die er die Rechte prüft: Ein Prozess kann sich eine fremde Seite nicht selbst eintragen.

::::beispiel Eine Bibliothek für alle
Die Shell, `cat` und `grep` benutzen alle die C-Bibliothek in der Datei `/usr/lib/x86_64-linux-gnu/libc.so.6`. Laufen die drei gleichzeitig, sind die Befehle der Bibliothek in allen drei Adressräumen eingetragen, aber im Arbeitsspeicher liegen sie nur einmal. Schreibt einer der Prozesse in einen beschreibbaren Teil der Bibliothek, bekommt er vorher eine eigene Kopie der betroffenen Seite; die anderen sehen davon nichts.
::::

⁠**Kurz gesagt:** Der Kernel kann einen Seitenrahmen in mehrere Adressräume eintragen und spart so Speicher, ohne die Grenze zwischen den Prozessen aufzugeben.

### Die mehrstufige Seitentabelle

<span class="anker" id="stufe-6-8"></span>

Eine Seitentabelle mit einer Zeile für jede mögliche Seite wäre riesig, obwohl ein Programm nur einen winzigen Teil davon benutzt. x86-64-Prozessoren teilen die Tabelle deshalb in Stufen.

:::definition Definition 6.8 (mehrstufige Seitentabelle)
<span class="anker" id="satz-6-8"></span>

Bei einer __mehrstufigen Seitentabelle__ ist die Seitennummer in mehrere Teile zerlegt, und jeder Teil ist ein Index in eine Tabelle einer anderen Stufe. Ein Eintrag der obersten Stufe nennt eine Tabelle der nächsten Stufe, und erst die unterste Stufe nennt den Seitenrahmen. Bei x86-64 gibt es in der Regel vier Stufen; jede Tabelle hat 512 Einträge zu je 8 Byte und füllt damit genau eine Seite. Eine Adresse mit 48 benutzten Bits zerfällt so in vier Indizes zu je 9 Bit und den Versatz mit 12 Bit:

$$\underbrace{\text{Bits 47--39}}_{\text{Stufe 4}}\;\big|\;\underbrace{\text{Bits 38--30}}_{\text{Stufe 3}}\;\big|\;\underbrace{\text{Bits 29--21}}_{\text{Stufe 2}}\;\big|\;\underbrace{\text{Bits 20--12}}_{\text{Stufe 1}}\;\big|\;\underbrace{\text{Bits 11--0}}_{\text{Versatz}}$$

Das Wurzelregister CR3 zeigt auf die Tabelle der obersten Stufe.
:::

Mit $2^9=512$ ist klar, warum jeder Index 9 Bit hat: Er wählt einen von 512 Einträgen. $4\cdot9+12=48$ Bit ergeben $2^{48}$ Byte, also 256 TiB virtuellen Adressraum. Wie viele Bits ein Prozessor benutzt, zeigt `lscpu`:

```console
$ lscpu | grep 'Address sizes'
Address sizes:                        46 bits physical, 48 bits virtual
```

::::beispiel Eine Adresse zerlegen
Die Adresse `0x00007ffd3c2a1f48` ist eine typische Adresse eines Programms unter Linux; mit 48 benutzten Bits beginnt sie mit vier Nullen. Jede Hexadezimalziffer steht für vier Bit; die 48 Bit lauten in Gruppen zu 9, 9, 9, 9 und 12:

$$\texttt{011111111}\;|\;\texttt{111110100}\;|\;\texttt{111100001}\;|\;\texttt{010100001}\;|\;\texttt{111101001000}$$

Als Zahlen gelesen: Index 255 in der obersten Tabelle, dann 500, dann 481, dann 161 in der untersten, und der Versatz $\texttt{0xf48}=3912$. Setzt man die Teile mit ihren Stellenwerten wieder zusammen, entsteht die Adresse (Abbildung [26](#abb-26)):

$$255\cdot2^{39}+500\cdot2^{30}+481\cdot2^{21}+161\cdot2^{12}+3912=140\,725\,612\,846\,920=\texttt{0x7ffd3c2a1f48}.$$

Die Shell rechnet das mit der Arithmetik aus [Linux, Kapitel 5, Abschnitt 2.4](/wissen/informatik/linux-und-kommandozeile/wie-die-shell-eine-befehlszeile-liest-expansion-quoting-variablen-umgebung/variablen-befehlsersetzung-und-arithmetik.html#stufe-2-4) nach; sie versteht dort auch Hexadezimalzahlen mit `0x`. Teilen durch $2^{39}$ schiebt die Bits des obersten Index nach unten, der Rest bei Division durch 512 schneidet die höheren Bits ab:

```console
$ echo $(( 0x7ffd3c2a1f48 / 2**39 % 512 )) $(( 0x7ffd3c2a1f48 / 2**30 % 512 )) $(( 0x7ffd3c2a1f48 / 2**21 % 512 )) $(( 0x7ffd3c2a1f48 / 2**12 % 512 ))
255 500 481 161
$ printf '%x\n' $(( 0x7ffd3c2a1f48 % 4096 ))
f48
```

Die Vorlage `%x` von `printf` gibt eine Zahl hexadezimal aus.

:::abbildung cyber/k2radresse 26
Rechenbild. Oben die Adresse `0x00007ffd3c2a1f48`, darunter die 48 Bit, die sich in fünf farbige Gruppen 9|9|9|9|12 teilen. Unter jeder Gruppe erscheint ihr Wert: 255, 500, 481, 161, 3912. Dann läuft die Rückrechnung Zeile für Zeile ab: $255\cdot2^{39}=140\,187\,732\,541\,440$, $500\cdot2^{30}=536\,870\,912\,000$, $481\cdot2^{21}=1\,008\,730\,112$, $161\cdot2^{12}=659\,456$, $+\,3912$, Summe $140\,725\,612\,846\,920=\texttt{0x7ffd3c2a1f48}$. Zum Schluss ein kleiner Weg durch vier Tabellen: CR3 → Eintrag 255 → Eintrag 500 → Eintrag 481 → Eintrag 161 → Seitenrahmen, plus Versatz.
:::
::::

⁠**Kurz gesagt:** Bei x86-64 zerlegt die MMU eine Adresse in vier Indizes zu 9 Bit und einen Versatz zu 12 Bit und läuft damit durch vier Tabellen.

:::hintergrund Warum mehrstufig und was die oberen 16 Bit tun
Bei $2^{48}$ Byte Adressraum und Seiten zu $2^{12}$ Byte gibt es $2^{36}$ Seiten. Eine einstufige Tabelle mit 8 Byte je Eintrag wäre $2^{36}\cdot8\,\mathrm{Byte}=512$ GiB groß, und zwar für jeden Prozess. Mehrstufig braucht man Tabellen nur für Bereiche, die wirklich benutzt werden: Ein leerer Eintrag in einer oberen Stufe steht für einen ganzen unbenutzten Bereich, ohne dass darunter Tabellen existieren müssen. Ein kleines Programm kommt mit wenigen Dutzend Kilobyte für seine Tabellen aus. Der Preis ist, dass die MMU bei einem Zugriff ohne gemerkten Eintrag vier Tabellen nacheinander lesen muss; deshalb der Zwischenspeicher aus Unterabschnitt [6.4](#stufe-6-4).

Die Bits 63 bis 48 einer Adresse werden nicht übersetzt. Sie müssen alle gleich Bit 47 sein, sonst weist der Prozessor die Adresse zurück; solche Adressen heißen kanonisch. Deshalb beginnen Adressen von Programmen mit `0x0000`, die des Kernels mit `0xffff`, und dazwischen liegt eine riesige Lücke. Neuere Prozessoren können eine fünfte Stufe benutzen und kommen dann auf 57 Bit. Außerdem kann ein Eintrag einer höheren Stufe direkt einen großen Block von 2 MiB oder 1 GiB nennen, statt auf eine weitere Tabelle zu zeigen.
:::

### Aufgaben zu Abschnitt [6](#stufe-6)

<span class="anker" id="stufe-6-9"></span>

:::aufgabe Aufgabe 14 ★ Seitennummer und Versatz
<span class="anker" id="aufg-14"></span>

Gib für die Adressen `0x401000`, `0x401fff`, `0x402001` und `0x7ffe148ff7a0` jeweils Seitennummer und Versatz an. Welche der ersten drei liegen in derselben Seite?

:::loesung
Die letzten drei Hexadezimalziffern sind der Versatz, der Rest ist die Seitennummer:

| Adresse | Seitennummer | Versatz |
|---|---|---|
| `0x401000` | `0x401` | `0x000` |
| `0x401fff` | `0x401` | `0xfff` |
| `0x402001` | `0x402` | `0x001` |
| `0x7ffe148ff7a0` | `0x7ffe148ff` | `0x7a0` |

`0x401000` und `0x401fff` liegen in derselben Seite, am Anfang und am letzten Byte. `0x402001` liegt zwei Bytes hinter dem letzten Byte dieser Seite und damit schon in der nächsten.
:::
:::

:::aufgabe Aufgabe 15 ★★ Eine Adresse aus dem Code von cat
<span class="anker" id="aufg-15"></span>

Auf dem Testsystem lag der Code von `cat` bei einem Lauf in einem Bereich ab `0x5b9382c1e000`. Zerlege die Adresse `0x00005b9382c1e123` von Hand in die vier Indizes und den Versatz. Prüfe dein Ergebnis mit der Shell wie im Beispiel „Eine Adresse zerlegen“.

:::loesung
Jede Hexadezimalziffer von `5b9382c1e123` wird zu vier Bit:

$$\texttt{0101\,1011\,1001\,0011\,1000\,0010\,1100\,0001\,1110\,0001\,0010\,0011}.$$

In Gruppen zu 9, 9, 9, 9 und 12 Bit:

$$\texttt{010110111}\;|\;\texttt{001001110}\;|\;\texttt{000010110}\;|\;\texttt{000011110}\;|\;\texttt{000100100011}.$$

Die Werte: $128+32+16+4+2+1=183$, $64+8+4+2=78$, $16+4+2=22$, $16+8+4+2=30$ und der Versatz $\texttt{0x123}=291$. Die Shell bestätigt es:

```console
$ echo $(( 0x5b9382c1e123 / 2**39 % 512 )) $(( 0x5b9382c1e123 / 2**30 % 512 )) $(( 0x5b9382c1e123 / 2**21 % 512 )) $(( 0x5b9382c1e123 / 2**12 % 512 ))
183 78 22 30
$ printf '%x\n' $(( 0x5b9382c1e123 % 4096 ))
123
```

Die MMU geht also in der obersten Tabelle zu Eintrag 183, in der nächsten zu 78, dann zu 22 und in der untersten zu Eintrag 30, der den Seitenrahmen nennt; dort liegt das Byte an der Stelle `0x123`.
:::
:::

:::aufgabe Aufgabe 16 ★★ Wie viel Platz brauchen die Tabellen?
<span class="anker" id="aufg-16"></span>

Ein Programm benutzt drei Bereiche: Code, Daten und einen Bereich für Zwischenwerte. Jeder ist kleiner als 2 MiB und liegt innerhalb des Bereichs einer einzigen Tabelle der untersten Stufe. Die drei Bereiche liegen so weit auseinander, dass sie in der obersten Tabelle drei verschiedene Einträge brauchen. (a) Wie viele Tabellen braucht der Prozess mindestens, und wie viel Speicher belegen sie? (b) Vergleiche mit einer einstufigen Tabelle für 48 Bit. (c) Wie viel Speicher deckt ein einzelner Eintrag der zweituntersten Stufe ab?

:::loesung
(a) Der Prozess braucht eine Tabelle der obersten Stufe. Jeder der drei Bereiche braucht darunter eine eigene Tabelle der dritten, der zweiten und der untersten Stufe, weil die Bereiche schon in der obersten Stufe verschiedene Einträge haben und also keine Tabelle darunter teilen können. Das sind $1+3\cdot3=10$ Tabellen zu je 4 KiB, zusammen 40 KiB.

(b) Eine einstufige Tabelle für 48 Bit hätte $2^{36}$ Einträge zu 8 Byte, also 512 GiB. Das ist mehr als 13 Millionen Mal so viel wie die 40 KiB der vierstufigen Tabelle.

(c) Ein Eintrag der zweituntersten Stufe nennt eine ganze Tabelle der untersten Stufe mit 512 Einträgen zu je einer Seite, deckt also $512\cdot4\,\mathrm{KiB}=2\,\mathrm{MiB}$ ab. Deshalb genügt in (a) für jeden Bereich unter 2 MiB eine einzige Tabelle der untersten Stufe.
:::
:::

:::aufgabe Aufgabe 17 ★★ Ein Zugriff ins Leere, Schritt für Schritt
<span class="anker" id="aufg-17"></span>

Führe `python3 -c 'import ctypes; ctypes.string_at(4096, 1)'` aus. Beschreibe, was nacheinander geschieht: welcher Teil des Prozessors den Zugriff prüft, welche Ausnahme entsteht, was der Kernel prüft und entscheidet, welches Signal der Prozess bekommt und woher die Zahl 139 kommt. Warum kann derselbe Ablauf bei einer gültigen, aber nicht geladenen Seite ohne jede Meldung enden?

:::loesung
Auf dem Testsystem endete der Befehl mit `Segmentation fault` und dem Status 139. Der Ablauf:

<ol>

<li>

`ctypes.string_at(4096, 1)` lässt den Prozessor ein Byte an der virtuellen Adresse `0x1000` lesen.

</li>

<li>

Die MMU sucht in der Seitentabelle des Prozesses, ausgehend vom Wurzelregister, den Eintrag für die Seite `0x1`. Es gibt keinen gültigen.

</li>

<li>

Sie löst einen Seitenfehler aus, eine Ausnahme. Der Prozessor wechselt auf Stufe 0, springt an die Einsprungstelle für Seitenfehler und übergibt die Adresse `0x1000` und den Fehlercode: Seite nicht vorhanden, lesender Zugriff, von Stufe 3.

</li>

<li>

Der Kernel prüft, ob die Adresse zu einem Bereich des Prozesses gehört. Das tut sie nicht; die Adressen unter 65536 belegt Linux in der Voreinstellung für kein gewöhnliches Programm.

</li>

<li>

Also schickt er dem Prozess SIGSEGV. Die Standardreaktion beendet ihn, und die Shell meldet $128+11=139$.

</li>

</ol>

Bei einer gültigen, aber noch nicht geladenen Seite laufen die Schritte 1 bis 3 genauso. In Schritt 4 findet der Kernel aber den Bereich, etwa einen Teil der Programmdatei, lädt die Seite in einen Seitenrahmen, trägt sie in die Seitentabelle ein und lässt den Befehl erneut laufen. Diesmal findet die MMU den Eintrag, und das Programm bemerkt nur, dass dieser eine Befehl etwas länger gedauert hat.
:::
:::
