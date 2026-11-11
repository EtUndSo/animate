---
title: Setting up Python
pfad: Computer Science / Programming / Python / Programs and the Python Interpreter
adresse: informatik/programmieren/python/programme-und-der-python-interpreter
knoten: Chapter 1: Programs and the Python Interpreter
order: 6020400
summary: To run Python programs, your computer needs CPython.
tags: terminal, prompt, Python install manager, version number
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
To run Python programs, your computer needs CPython. This section shows how to set it up on Windows and on Linux and how to check which version you have.
:::

:::::vorwissen What you need for this: opening a terminal

<span class="anker" id="stufe-3-1"></span>

Python is usually started with a command that you type into a terminal. A __terminal__ is a window into which you type commands as text; the computer runs each command and writes its response below it.

**Opening it.**

<ul>

<li>

⁠**Windows 11:** Right-click the Start button and choose “Terminal”, or search for “Terminal” in the Start menu. A window opens with PowerShell, the command shell of Windows.

</li>

<li>

⁠**Linux (Ubuntu):** Press Ctrl+Alt+T, or search for “Terminal” in the “Activities” overview.

</li>

<li>

⁠**Linux on Windows (WSL):** Start the “Ubuntu” app from the Start menu.

</li>

</ul>

**The prompt.** At the end of the last line there is a short text, after which the cursor blinks. It is called the __prompt__ and shows that the terminal is waiting for a command. On Windows, it looks something like this: `PS C:\Users\student>`. On Linux, something like this: `student@labor:~$`. It contains the user name `student`, the computer name `labor` and, with `~`, the home folder.

**Entering a command.** Type the command after the prompt and press Enter. Try it with `echo Hallo`; the command `echo` writes the text after it back to you.

In this chapter, terminal sessions appear in gray boxes. The prompt is shortened there: `PS>` on Windows, `$` on Linux. You type only what comes after it. Lines without this beginning are the computer's response.

```console Windows (PowerShell)
PS> echo Hallo
Hallo
```

```console Linux
$ echo Hallo
Hallo
```

Linux, Chapter 2 covers the terminal, folders and commands in detail.

:::::

### Python on Windows: the Python install manager

<span class="anker" id="stufe-3-2"></span>

Windows does not come with Python. Since Python 3.14, `python.org` has offered its own management program for this; the earlier installer for individual versions has been deprecated since then and will no longer be released for Python 3.16.

:::definition Definition 3.1 (Python install manager)
<span class="anker" id="satz-3-1"></span>

The __Python install manager__ is a program for Windows that downloads, installs, lists, removes and starts Python versions. You operate it in the terminal with the command `py`.
:::

**Step 1: install the install manager.** It is available as the “Python install manager” app in the Microsoft Store and as a download at `python.org/downloads`; both editions are the same. If you prefer to use a command, type in the terminal:

```console Windows (PowerShell)
PS> winget install 9NQ7512CXL7T -e --accept-package-agreements --disable-interactivity
```

**Step 2: install a Python version.** For example, version 3.14:

```console Windows (PowerShell)
PS> py install 3.14
```

If no version is installed at all, the first start of `py` or `python` also fetches the newest version on its own.

**Step 3: check what is installed.** `py list` shows the installed versions and which of them is the default version. `py list --online` shows which versions are available for download.

After that, `py` starts the default version; this is the newest installed one unless you set something else. The command `python` does the same. You choose a specific version with `py -V:3.14`. In this chapter, the command `py` is used on Windows.

::::beispiel checking the version
The option `--version` makes Python state its version number without doing anything else. On the computer used to test this chapter, Python 3.13 is installed:

```console Windows (PowerShell)
PS> py --version
Python 3.13.9
```
::::

**Two typical problems.**

<ul>

<li>

⁠**The Microsoft Store opens instead of Python.** Windows creates a placeholder named `python` that opens the Store. In the Start menu, open “Manage app execution aliases” and check that the “Python (default)” entries of the install manager are switched on.

</li>

<li>

⁠**`py list` reports “legacy py.exe command”.** Then the old “Python Launcher” from the earlier installer is still present and takes precedence. On the computer used to test this chapter, it looks like this:

```console Windows (PowerShell)
PS> py list
WARNING: The 'list' command is unavailable because this is the legacy py.exe command.
If you have already installed the Python install manager, open Installed Apps and remove 'Python Launcher' to enable the new py.exe command.
C:\Users\student\AppData\Local\Programs\Python\Python313\python.exe: can't open file 'C:\\Users\\student\\list': [Errno 2] No such file or directory
```

The old launcher does not know the command `list` and passes the word on to Python, which then looks for a file named `list`. The fix: in Settings, under “Installed apps”, uninstall “Python Launcher”. A Python that was set up with the earlier installer may stay; `py` still finds it.

</li>

</ul>

⁠**In short:** On Windows, you install the Python install manager and then start Python with `py`.

:::hintergrund Why Windows has a launcher of its own
On Windows, there is no fixed place where programs like Python have to be, and often several Python versions are installed side by side. In the past, every installer had to register by itself where Windows finds the command `python`, and several versions easily got in each other's way. A single launcher that knows all installed versions and selects the desired one solves this. Since Python 3.14, the Python install manager also takes care of installing and removing the versions.

Microsoft introduced the placeholder that opens the Store in 2019: anyone who types `python` without Python being installed is meant to be led directly to a way of installing it. If a Python is present, the placeholder only gets in the way, as long as it stays switched on.
:::

### Python on Linux

<span class="anker" id="stufe-3-3"></span>

Most Linux systems come with Python, because parts of the system itself are written in Python. On Linux, the command is called `python3`.

**Checking.** On Ubuntu 26.04, Python 3.14 is preinstalled:

```console Linux
$ python3 --version
Python 3.14.4
```

The command `python` without the 3 does not exist there. Ubuntu responds with a hint:

```console Linux
$ python --version
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
```

That is why this chapter always uses `python3` on Linux.

**If Python is missing.** On very minimal systems, Python can be missing. On Ubuntu and Debian, this command installs it:

```console Linux
$ sudo apt install python3
```

Here `apt` is the package manager of Ubuntu: it downloads programs from verified sources and installs them. The `sudo` in front runs the command with administrator privileges and asks for your password to do so.

:::warnung Do not remove or replace the system's Python
On Linux, the system itself uses its Python. On the Ubuntu computer used to test this chapter, removing `python3` would make the package manager remove more than a hundred other packages along with it, including the command helper that suggested `python3` in the example above. If you remove `python3` or replace it with a version you built yourself, you can damage these parts of the system. So leave the system Python as it is. If you ever need a different version, install it in addition, without touching the existing `python3`.
:::

⁠**In short:** On Linux, Python is usually already there and is called `python3`.

:::hintergrund Why the command is called `python3` on Linux
Python 3 appeared in 2008 and was deliberately not fully compatible with Python 2: some programs for Python 2 do not run under Python 3. At that time, many Linux systems had tools of their own written in Python 2 that were started with the command `python`. If `python` had simply been switched to Python 3, they would have broken. That is why Python 3 got its own command, `python3`, and a recommendation of the Python project for Linux systems laid down that `python3` always starts a Python 3.

Python 2 has no longer been maintained since January 1, 2020. Since then, many systems simply leave out the command `python` instead of letting it point to one of the two versions. If you want it anyway, install the small package `python-is-python3` on Ubuntu; it makes `python` a second name for `python3`.
:::

### The version number

<span class="anker" id="stufe-3-4"></span>

Python keeps evolving: new versions bring new language features and better error messages. To know what your Python can do, you should know its version.

:::definition Definition 3.2 (Version number)
<span class="anker" id="satz-3-2"></span>

A Python __version number__ has the form `3.14.4` and consists of three parts:

<ul>

<li>

the major version, here 3;

</li>

<li>

the minor version, here 14; every year in October, a new minor version with new language features is released;

</li>

<li>

the bugfix number, here 4; it increases when a minor version receives fixes without the language changing.

</li>

</ul>
:::

Version numbers are compared part by part from the left, not as decimal numbers: 3.14 is newer than 3.9 because 14 is greater than 9.

::::beispiel
The test computer for this chapter reports `Python 3.13.9` on Windows and `Python 3.14.4` on Linux. Both have the major version 3; the Linux version is one minor version newer. In November 2026, 3.15 is the newest minor version, 3.14 still receives bug fixes, and 3.13 receives only security fixes. All examples in this chapter run on Python 3.12 or later; they were tested on Windows with Python 3.13 and on Linux with Python 3.14. Where the output of the two versions differs, this is noted.
::::

⁠**In short:** The version number tells you which Python you have; version numbers are compared part by part.

:::hintergrund How long a Python version is maintained
Since Python 3.9 in October 2020, a new minor version has been released every year in October. Each one is maintained for about five years: at first it receives bug fixes every few months, later only fixes for security vulnerabilities, and after that nothing at all. Python 3.10, for example, reached its end of life in October 2026. The fixed rhythm makes it possible to plan when you should switch to a new version. A version without maintenance keeps running, but known security vulnerabilities in it are no longer closed.
:::

### Exercises for Section [3](#stufe-3)

<span class="anker" id="stufe-3-5"></span>

:::aufgabe Exercise 7 ★ Setting up and checking Python
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Open a terminal and enter `echo Hallo`.

</li>

<li>

Set up Python if it is missing: on Windows with the Python install manager, on Linux with the package manager.

</li>

<li>

Display the version number: `py --version` on Windows, `python3 --version` on Linux. Write it down. Is it at least 3.12?

</li>

<li>

Windows only: What does `py list` show? If a warning appears, solve the problem as described in Subsection [3.2](#stufe-3-2).

</li>

</ol>

:::loesung
(a) The terminal responds with `Hallo`.

(b) and (c) On the computers used to test this chapter:

```console Windows (PowerShell)
PS> py --version
Python 3.13.9
```

```console Linux
$ python3 --version
Python 3.14.4
```

Both versions are at least 3.12, so they are sufficient for this series. Your number may be different; all that matters is that the minor version is at least 12.

(d) With the Python install manager, `py list` shows a list of the installed versions and marks the default version. If the warning about “legacy py.exe command” appears instead, the old “Python Launcher” is still installed. Uninstall it in Settings, under “Installed apps”; after that, `py list` responds with the list.
:::
:::

:::aufgabe Exercise 8 ★ Ordering versions
<span class="anker" id="aufg-8"></span>

Order the version numbers from oldest to newest: `3.14.10`, `3.9.18`, `3.13.9`, `3.14.4`, `3.12.0`. Which of them meet the requirement “Python 3.12 or later”? Why is it misleading to read the numbers as decimal numbers?

:::loesung
From oldest to newest: `3.9.18`, `3.12.0`, `3.13.9`, `3.14.4`, `3.14.10`. All except `3.9.18` meet the requirement “Python 3.12 or later”.

You compare part by part, starting from the left: the major version is 3 everywhere; for the minor version, 9 is smaller than 12, 13 and 14; with the same minor version 14, the third number decides, and 4 is smaller than 10. Read as a decimal number, 3.9 would be larger than 3.14, because $0.9>0.14$; and 3.14.10 would look like a smaller number than 3.14.4. Both are wrong, because each part is a separate whole number and not a fractional part.
:::
:::

:::aufgabe Exercise 9 ★★ Troubleshooting the setup
<span class="anker" id="aufg-9"></span>

In each case, explain what the cause is and what you do.

<ol class="al">

<li>

On Windows, `python` opens the Microsoft Store, even though you have installed the Python install manager.

</li>

<li>

On Ubuntu, `python hallo.py` responds with “Command 'python' not found”.

</li>

<li>

On Windows, `py list` responds with a warning about “legacy py.exe command”.

</li>

</ol>

:::loesung
(a) The Windows placeholder that opens the Store takes precedence over the install manager's command. In the Start menu, open “Manage app execution aliases” and make sure that the “Python (default)” entries of the install manager are switched on. Alternatively, use `py`, as in this chapter.

(b) On Ubuntu, the command `python` does not exist, only `python3`. The correct command is `python3 hallo.py`. If you absolutely want to type `python`, install the package `python-is-python3`.

(c) The old “Python Launcher” from the earlier installer is installed and hides the new command `py`. Uninstall it in Settings, under “Installed apps”. Until then, you can also reach the install manager under its second name `pymanager`, that is, with `pymanager list`.
:::
:::
