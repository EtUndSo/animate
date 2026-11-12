---
title: Das Wichtigste bis hier
pfad: Informatik / Linux und Kommandozeile / Prozesse, Signale und Dienste
adresse: informatik/linux-und-kommandozeile/prozesse-signale-und-dienste
knoten: Kapitel 8: Prozesse, Signale und Dienste
order: 6131000
summary: Wie man laufende Programme beobachtet, anhält, im Hintergrund weiterlaufen lässt und beendet, und wie Linux Dienste startet, überwacht und ihre Meldungen sammelt
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

Ein Prozess ist ein laufendes Programm samt Speicher, Stelle im Programm, Dateien, Arbeitsverzeichnis, Umgebung und Benutzer. Der Kernel teilt die wenigen Kerne reihum zwischen allen Prozessen auf.

</li>

<li>

Jeder Prozess hat eine PID und einen Elternprozess (PPID); alle bilden einen Baum mit `systemd` (PID 1) als Wurzel. Neue Prozesse entstehen als Kopie (fork), laden ein anderes Programm (exec) und melden ihr Ende dem wartenden Elternprozess (wait).

</li>

<li>

`ps` (`-ef`, `aux`, `-o`), `pgrep`, `top` und `/proc/<PID>` zeigen Prozesse. Der Zustand ist R, S, D, T oder Z; ein Zombie wartet darauf, dass sein Elternprozess den Exit-Status abholt.

</li>

<li>

Eine Shell verwaltet Jobs: `&` startet im Hintergrund, Strg+Z hält an, `fg` und `bg` lassen weiterlaufen, `jobs` zeigt die Liste, `wait` wartet.

</li>

<li>

Signale sind Nachrichten des Kernels mit einer Standardreaktion: SIGTERM (15) bittet zu enden, SIGINT (2) kommt von Strg+C, SIGKILL (9) und SIGSTOP (19) lassen sich weder abfangen noch ignorieren, SIGCONT (18) setzt fort, SIGHUP (1) kommt beim Schließen des Terminals. `kill` und `pkill` schicken sie, nur an eigene Prozesse; der Exit-Status $128 + n$ verrät das Signal $n$.

</li>

<li>

`trap` legt in der bash eigene Reaktionen fest, `timeout` setzt eine Zeitgrenze, `nohup` und `disown` schützen vor SIGHUP.

</li>

<li>

Die Last zählt Prozesse in R und D, gleitend gemittelt; der Nice-Wert ($-20$ bis 19) teilt je Stufe das Gewicht durch etwa 1,25; erhöhen darf jeder, senken nur root.

</li>

<li>

Dienste laufen ohne Terminal, oft unter eigenem Benutzer, verwaltet von `systemd` über Unit-Dateien; `systemctl` zeigt, startet, stoppt und schaltet sie ein, `journalctl` liest ihre Meldungen.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Was gerade läuft, zeigt der Kernel als Baum von Prozessen mit Nummern, Besitzern und Zuständen, den `ps`, `pgrep`, `top` und `/proc` lesbar machen.

</li>

<li>

Anweisungen von außen gibt man einem Prozess mit Signalen, die der Kernel zustellt: Die Shell nutzt sie für Strg+C, Strg+Z und ihre Jobs, `kill` schickt sie gezielt, und `systemd` nutzt sie, um Dienste zu stoppen und nach einem Absturz neu zu starten.

</li>

<li>

Strg+C beendet ein Programm nicht immer, weil SIGINT nur eine Bitte ist, die ein Programm abfangen oder ignorieren darf; nur SIGKILL und SIGSTOP kann kein Programm abfangen, und deshalb schickt man zuerst SIGTERM und erst zuletzt SIGKILL.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Gedanken. Erstens: Ein neuer Prozess ist eine Kopie seines Elternprozesses, die ein anderes Programm lädt; was sie erbt, Benutzer, Deskriptoren, Nice-Wert und ignorierte Signale, behält sie, und ihr Ende meldet sie dem Elternprozess. Zweitens: Von außen erreicht man einen laufenden Prozess nur über Signale, die der Kernel zustellt und dabei prüft; jedes hat eine Standardreaktion, die das Programm ändern darf, außer bei SIGKILL und SIGSTOP.

| Ergebnis | Woher es kommt |
|---|---|
| `exec ps` zeigt die PID der bash | exec lädt ein Programm, ohne einen neuen Prozess anzulegen (Abschnitt [1](prozesse-und-ihre-verwandtschaft.html#stufe-1)) |
| `strace` zeigt `openat liste.txt` vor `execve` | die Shell richtet Umleitungen zwischen fork und exec ein (Abschnitt [1](prozesse-und-ihre-verwandtschaft.html#stufe-1)) |
| `[sleep] <defunct>` bleibt stehen | der Elternprozess ruft nie wait auf (Abschnitt [2](prozesse-beobachten.html#stufe-2)) |
| `kill -9` beseitigt keinen Zombie | er ist schon beendet; nur wait entfernt ihn (Abschnitt [2](prozesse-beobachten.html#stufe-2)) |
| `cat &` hält sofort an | nur der Vordergrund darf vom Terminal lesen (Abschnitt [3](vordergrund-hintergrund-und-jobs.html#stufe-3)) |
| Strg+C erreicht keinen Hintergrundjob | der Kernel schickt SIGINT nur an den Vordergrund des Terminals (Abschnitt [3](vordergrund-hintergrund-und-jobs.html#stufe-3)) |
| `kill $$` lässt die Shell weiterlaufen | eine interaktive bash ignoriert SIGTERM (Abschnitt [4](signale.html#stufe-4)) |
| nach `kill -STOP` steht 147 in `$?` | $128 + 19$, SIGSTOP (Abschnitt [4](signale.html#stufe-4)) |
| `kill` an `sudo sleep` scheitert | das Ziel gehört root, nicht dir (Abschnitt [4](signale.html#stufe-4)) |
| `trap "" TERM` überlebt `kill`, nicht `kill -9` | SIGKILL kann kein Programm abfangen (Abschnitt [5](mit-signalen-arbeiten.html#stufe-5)) |
| `timeout -k` endet mit 137 | nach SIGTERM kam SIGKILL, $128 + 9$ (Abschnitt [5](mit-signalen-arbeiten.html#stufe-5)) |
| nach dem Schließen läuft `nohup sleep` weiter | SIGHUP bleibt über exec ignoriert (Abschnitt [5](mit-signalen-arbeiten.html#stufe-5)) |
| die Last steht nach einer Minute bei 2,54, nicht 4 | gleitendes Mittel mit $\mathrm{e}^{-5/60}$ (Abschnitt [6](last-und-prioritat.html#stufe-6)) |
| Nice 0 gegen Nice 10: 90 zu 10 Prozent | Gewicht je Stufe durch 1,25 (Abschnitt [6](last-und-prioritat.html#stufe-6)) |
| `renice` von 15 auf 5 scheitert | senken darf nur root (Abschnitt [6](last-und-prioritat.html#stufe-6)) |
| die Eieruhr läuft nach `kill -9` wieder | `Restart=on-failure`, systemd ist ihr Elternprozess (Abschnitt [7](dienste-und-systemd.html#stufe-7)) |
| nach `enable` läuft der Dienst nicht | enable legt nur einen Link für den nächsten Start an (Abschnitt [7](dienste-und-systemd.html#stufe-7)) |
| `journalctl -u cron` zeigt nichts | student ist weder in `adm` noch in `systemd-journal` (Abschnitt [8](protokolle-das-journal.html#stufe-8)) |
