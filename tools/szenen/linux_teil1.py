"""Linux und Kommandozeile, Linux 1 (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\kap1_stufen.tex, kap1_stufen_b.tex): Abbildungen.

Szenenname linux/k1<name> = \\label{fig:k1<name>} im Heft. Stil wie tools/szenen/prog_teil3.py (Kästen, Pfeile, Code mit s.formel).
Bauen:  python tools/szenen/linux_teil1.py
Export: python tools/export_szenen.py linux/k1schichten linux/k1systemaufruf linux/k1wege linux/k1entscheidung linux/k1vm
            linux/k1snapshot linux/k1nat linux/k1wsl linux/k1pruefsumme linux/k1bootkette linux/k1live linux/k1datentraeger
            linux/k1stick --lang de   (jedes Bild höchstens 548 px breit)
Keine Rechenbilder: Das Heft enthält keine Summe, kein Produkt und kein Skalarprodukt mit Zahlen.
Die Zahlen (7,45 GB, 476,94 GB, 6,48 GB, Prüfsummen) prüft C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\rechnung_kap1.py.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
MITTEL = 24
WINZIG = 18
BLAU_HELL = "#e3eefb"
ORANGE_HELL = "#fdece3"
GRUEN_HELL = "#e6f3ea"
GRAU_HELL = "#efefef"


# Breite: Die Kästen sind großzügig gezeichnet; vor dem Speichern werden alle x-Koordinaten und Kastenbreiten mit dem
# Faktor der Szene gestaucht (Schriftgröße bleibt), damit jedes Bild höchstens 548 px breit wird.
FAKTOR = {"linux/k1schichten": 0.80, "linux/k1systemaufruf": 0.78, "linux/k1wege": 0.83, "linux/k1entscheidung": 0.84,
          "linux/k1vm": 0.83, "linux/k1snapshot": 0.90, "linux/k1nat": 0.82, "linux/k1wsl": 0.85, "linux/k1pruefsumme": 0.85,
          "linux/k1bootkette": 0.76, "linux/k1live": 0.74, "linux/k1datentraeger": 0.78, "linux/k1stick": 0.83}
_speichern = Szene.speichern


def _schmal_speichern(self):
    f = FAKTOR.get(self.name, 1.0)
    for o in self.objects:
        p = o["props"]
        for k in ("center", "position", "start", "end"):
            if k in p:
                p[k][0] = round(p[k][0] * f, 4)
        if o["type"] == "TextBox":
            p["width"] = round(p["width"] * f, 4)
    return _speichern(self)


Szene.speichern = _schmal_speichern


def T(s, key, de, en, es, zh, fr, tr):
    return s.tr(key, de, en, es, zh, fr=fr, tr=tr)


def kasten(s, mitte, breite, hoehe, text, groesse=KLEIN, fuellung="#ffffff", form="round", farbe=SCHWARZ, textfarbe=SCHWARZ,
           dicke=2.5, dash=""):
    """Kasten mit zentriertem Text (mehrzeilig mit \\n)."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form=form, farbe=farbe, fuellung=fuellung, deckung=1, dicke=dicke, dash=dash)
    if text:
        s.text(None, text, mitte, groesse, "center", textfarbe)


def flaeche(s, x0, y0, x1, y1, fuellung, farbe=None, dicke=0, dash=""):
    """Hinterlegter Bereich (Rahmen eines Systems oder einer Schicht)."""
    s.box("", ((x0 + x1) / 2, (y0 + y1) / 2), breite=x1 - x0, hoehe=y1 - y0, form="rect", farbe=farbe or fuellung,
          fuellung=fuellung, deckung=1, dicke=dicke, dash=dash)


def pf(s, a, b, knick="none", farbe=SCHWARZ, dash="", doppelt=False):
    s.pfeil(a, b, knick=knick, farbe=farbe, dicke=2.5, spitze=0.12, dash=dash, doppelt=doppelt)


# ------------------------------------------------------------------ Abschnitt 1
def k1schichten():
    """Programme / Betriebssystem / Hardware als drei Schichten."""
    s = Szene("linux/k1schichten")
    flaeche(s, -4.0, 0.9, 4.45, 1.7, GRUEN_HELL, GRUEN, 2.5)
    flaeche(s, -4.0, -0.4, 4.45, 0.4, BLAU_HELL, BLAU, 2.5)
    flaeche(s, -4.0, -1.7, 4.45, -0.9, GRAU_HELL, GRAU, 2.5)
    s.text(None, T(s, "prog", "Programme", "programs", "programas", "程序", "programmes", "programlar"), (-3.85, 1.3), KLEIN, "left")
    s.text(None, T(s, "bs", "Betriebssystem", "operating system", "sistema operativo", "操作系统", "système d’exploitation",
                   "işletim sistemi"), (-3.85, 0.0), KLEIN, "left")
    s.text(None, T(s, "hw", "Hardware", "hardware", "hardware", "硬件", "matériel", "donanım"), (-3.85, -1.3), KLEIN, "left")
    progs = (T(s, "editor", "Editor", "editor", "editor", "编辑器", "éditeur", "editör"),
             T(s, "browser", "Browser", "browser", "navegador", "浏览器", "navigateur", "tarayıcı"),
             T(s, "terminal", "Terminal", "terminal", "terminal", "终端", "terminal", "terminal"),
             T(s, "foto", "Fotoprogramm", "photo app", "app de fotos", "照片程序", "app photos", "fotoğraf uygulaması"))
    hws = (T(s, "cpu", "Prozessor", "processor", "procesador", "处理器", "processeur", "işlemci"),
           T(s, "ram", "Speicher", "memory", "memoria", "内存", "mémoire", "bellek"),
           "SSD",
           T(s, "netz", "Netz", "network", "red", "网络", "réseau", "ağ"))
    for i, x in enumerate((-0.9, 0.65, 2.2, 3.75)):
        kasten(s, (x, 1.3), 1.45, 0.45, progs[i], WINZIG)
        kasten(s, (x, -1.3), 1.45, 0.45, hws[i], WINZIG)
    s.text(None, T(s, "bs_text", "teilt die Hardware auf, schirmt die Programme voneinander ab,\nbietet einheitliche Dienste: Datei speichern, Speicher anfordern",
                   "shares out the hardware, keeps programs apart,\noffers uniform services: save a file, request memory",
                   "reparte el hardware, separa los programas entre sí,\nofrece servicios uniformes: guardar un archivo, pedir memoria",
                   "分配硬件，使程序彼此隔离，\n提供统一的服务：保存文件、申请内存",
                   "répartit le matériel, isole les programmes,\noffre des services uniformes : enregistrer un fichier, demander de la mémoire",
                   "donanımı paylaştırır, programları birbirinden ayırır,\ntek tip hizmetler sunar: dosya kaydetme, bellek isteme"),
           (-1.75, 0.0), WINZIG, "left")
    pf(s, (-3.35, 0.88), (-3.35, 0.42))
    pf(s, (-3.35, -0.42), (-3.35, -0.88))
    s.text(None, T(s, "dienst", "Dienst anfordern", "request a service", "pedir un servicio", "请求服务", "demander un service",
                   "hizmet iste"), (-3.2, 0.65), WINZIG, "left")
    s.text(None, T(s, "steuern", "steuern", "controls", "controla", "控制", "pilote", "yönetir"), (-3.2, -0.65), WINZIG, "left")
    s.speichern()


def k1systemaufruf():
    """Benutzermodus und Kernel-Modus mit Wand und Tor; direkter Zugriff wird gesperrt."""
    s = Szene("linux/k1systemaufruf")
    flaeche(s, -4.0, 0.6, 4.6, 2.2, GRUEN_HELL)
    flaeche(s, -4.0, -1.0, 4.6, 0.6, BLAU_HELL)
    s.text(None, T(s, "user", "Benutzermodus", "user mode", "modo usuario", "用户态", "mode utilisateur", "kullanıcı kipi"),
           (-3.85, 1.95), KLEIN, "left")
    s.text(None, T(s, "kmode", "Kernel-Modus", "kernel mode", "modo núcleo", "内核态", "mode noyau", "çekirdek kipi"),
           (-3.85, 0.35), KLEIN, "left")
    s.linie(None, (-4.0, 0.6), (-0.4, 0.6), dicke=6)
    s.linie(None, (0.4, 0.6), (4.6, 0.6), dicke=6)
    kasten(s, (0, 0.6), 0.8, 0.36, T(s, "tor", "Tor", "gate", "puerta", "门", "porte", "kapı"), WINZIG, ORANGE_HELL, form="rect")
    kasten(s, (-2.6, 1.4), 1.5, 0.45, T(s, "p1", "Programm", "program", "programa", "程序", "programme", "program"), WINZIG)
    kasten(s, (2.7, 1.5), 2.2, 0.45, T(s, "p2", "zweites Programm", "second program", "segundo programa", "第二个程序",
                                       "deuxième programme", "ikinci program"), WINZIG)
    kasten(s, (0, -0.3), 4.6, 0.45, T(s, "kern", "Kernel: prüft den Auftrag, führt ihn aus", "kernel: checks the request, carries it out",
                                      "núcleo: comprueba la petición y la ejecuta", "内核：检查请求并执行",
                                      "noyau : vérifie la demande, l’exécute", "çekirdek: isteği denetler, yürütür"), WINZIG, form="rect")
    kasten(s, (0, -1.7), 1.9, 0.45, T(s, "ssd", "SSD, Netz, …", "SSD, network, …", "SSD, red, …", "SSD、网络……", "SSD, réseau, …",
                                      "SSD, ağ, …"), WINZIG, GRAU_HELL)
    pf(s, (-2.6, 1.17), (-0.4, 0.78), knick="vh")
    s.text(None, T(s, "aufruf", "Systemaufruf\nNr. + Angaben", "system call\nno. + details", "llamada al sistema\nn.º + datos",
                   "系统调用\n编号 + 参数", "appel système\nn° + données", "sistem çağrısı\nno. + bilgiler"), (-1.2, 1.05), WINZIG, "center")
    pf(s, (0, 0.42), (0, -0.07))
    pf(s, (0, -0.53), (0, -1.47))
    pf(s, (2.7, 1.27), (0.95, -1.7), knick="vh", farbe=ROT, dash=DASH)
    s.kreuzchen(None, 2.7, 0.6, farbe=ROT, groesse=0.3)
    s.text(None, T(s, "direkt", "direkter Zugriff:\nProzessor sperrt", "direct access:\nprocessor blocks it",
                   "acceso directo:\nel procesador lo bloquea", "直接访问：\n处理器阻止", "accès direct :\nle processeur bloque",
                   "doğrudan erişim:\nişlemci engeller"), (2.85, -0.3), WINZIG, "left", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k1wege():
    """Drei Wege nebeneinander: WSL 2, virtuelle Maschine, Live-USB-Stick."""
    s = Szene("linux/k1wege")
    rechner = T(s, "rechner", "ein Rechner", "one computer", "un ordenador", "一台计算机", "un ordinateur", "bir bilgisayar")
    win = "Windows"
    for x, titel in ((-2.85, T(s, "t_wsl", "WSL 2", "WSL 2", "WSL 2", "WSL 2", "WSL 2", "WSL 2")),
                     (0.0, T(s, "t_vm", "virtuelle Maschine", "virtual machine", "máquina virtual", "虚拟机", "machine virtuelle",
                             "sanal makine")),
                     (2.85, T(s, "t_live", "Live-USB-Stick", "live USB stick", "memoria USB live", "Live U 盘", "clé USB live",
                              "canlı USB bellek"))):
        flaeche(s, x - 1.3, -1.6, x + 1.3, 1.5, GRAU_HELL, GRAU, 2)
        s.text(None, titel, (x, 1.8), MITTEL, "center")
        s.text(None, rechner, (x, -1.42), WINZIG, "center", GRAU)
    # WSL 2
    kasten(s, (-2.85, -0.9), 2.2, 0.4, win, WINZIG, BLAU_HELL, form="rect")
    kasten(s, (-3.45, -0.2), 0.85, 0.4, "Word", WINZIG, form="rect")
    kasten(s, (-2.3, 0.0), 1.1, 0.6, T(s, "kvm", "kleine VM\nmit Linux", "small VM\nwith Linux", "VM pequeña\ncon Linux",
                                       "小型虚拟机\n运行 Linux", "petite VM\navec Linux", "küçük VM\nLinux ile"), WINZIG, GRUEN_HELL, form="rect")
    s.text(None, T(s, "neben", "Linux läuft neben\nWindows-Programmen", "Linux runs alongside\nWindows programs",
                   "Linux funciona junto a\nlos programas de Windows", "Linux 与 Windows\n程序并行运行",
                   "Linux tourne à côté\ndes programmes Windows", "Linux, Windows\nprogramlarının yanında çalışır"), (-2.85, 0.95), WINZIG, "center")
    # VM
    kasten(s, (0, -0.9), 2.2, 0.4, win, WINZIG, BLAU_HELL, form="rect")
    kasten(s, (0, -0.4), 2.2, 0.4, "VirtualBox", WINZIG, form="rect")
    kasten(s, (0, 0.2), 2.3, 0.6, T(s, "nachgebildet", "nachgebildeter Rechner\nmit Linux im Fenster", "simulated computer\nwith Linux in a window",
                                    "ordenador simulado\ncon Linux en una ventana", "模拟的计算机\n在窗口中运行 Linux",
                                    "ordinateur simulé\navec Linux dans une fenêtre", "taklit edilen bilgisayar\npencerede Linux"),
           16, GRUEN_HELL, form="rect")
    s.text(None, T(s, "abgeschottet", "abgeschottet, mit\nSicherungspunkten", "isolated, with\nsnapshots", "aislada, con\ninstantáneas",
                   "相互隔离，\n带快照", "isolée, avec\ninstantanés", "yalıtılmış,\nanlık görüntülerle"), (0, 1.0), WINZIG, "center")
    # Live-USB
    kasten(s, (2.85, -0.9), 2.2, 0.4, T(s, "ruht", "Windows ruht", "Windows at rest", "Windows en reposo", "Windows 静止",
                                        "Windows au repos", "Windows bekler"), WINZIG, "#dddddd", form="rect", textfarbe=GRAU)
    kasten(s, (2.85, -0.15), 2.3, 0.6, T(s, "vomstick", "Linux vom Stick,\ndirekt auf der Hardware", "Linux from the stick,\ndirectly on the hardware",
                                         "Linux desde la memoria,\ndirectamente en el hardware", "从 U 盘启动 Linux，\n直接运行在硬件上",
                                         "Linux depuis la clé,\ndirectement sur le matériel", "bellekten Linux,\ndoğrudan donanımda"),
           16, GRUEN_HELL, form="rect")
    kasten(s, (2.85, 0.85), 1.2, 0.36, T(s, "stick", "USB-Stick", "USB stick", "memoria USB", "U 盘", "clé USB", "USB bellek"), WINZIG)
    s.speichern()


def k1entscheidung():
    """Entscheidungsbaum mit zwei Fragen und drei Wegen (mit Abschnittsnummern)."""
    s = Szene("linux/k1entscheidung")
    ja = T(s, "ja", "ja", "yes", "sí", "是", "oui", "evet")
    nein = T(s, "nein", "nein", "no", "no", "否", "non", "hayır")
    kasten(s, (-1.4, 1.5), 4.6, 0.8, T(s, "f1", "Willst du Linux direkt auf der echten\nHardware deines Rechners erleben?",
                                       "Do you want to experience Linux directly\non your computer’s real hardware?",
                                       "¿Quieres usar Linux directamente en el\nhardware real de tu ordenador?",
                                       "你想直接在电脑的\n真实硬件上体验 Linux 吗？",
                                       "Veux-tu découvrir Linux directement sur\nle vrai matériel de ton ordinateur ?",
                                       "Linux’u doğrudan bilgisayarının\ngerçek donanımında mı denemek istiyorsun?"), 20)
    kasten(s, (-1.4, 0.0), 4.6, 0.8, T(s, "f2", "Brauchst du ein abgeschottetes Labor,\ndas du jederzeit zurücksetzen kannst?",
                                       "Do you need an isolated lab\nthat you can reset at any time?",
                                       "¿Necesitas un laboratorio aislado\nque puedas restablecer en cualquier momento?",
                                       "你需要一个可以随时\n还原的隔离实验环境吗？",
                                       "As-tu besoin d’un labo isolé\nque tu peux réinitialiser à tout moment ?",
                                       "İstediğin zaman sıfırlayabileceğin\nyalıtılmış bir laboratuvar mı gerekiyor?"), 20)
    kasten(s, (3.15, 1.5), 2.5, 0.75, T(s, "b_live", "Live-USB-Stick\nAbschnitte 5, 6, 8, 9", "live USB stick\nsections 5, 6, 8, 9",
                                        "memoria USB live\nsecciones 5, 6, 8, 9", "Live U 盘\n第 5、6、8、9 节",
                                        "clé USB live\nsections 5, 6, 8, 9", "canlı USB bellek\nbölüm 5, 6, 8, 9"), 20, GRUEN_HELL)
    kasten(s, (3.15, 0.0), 2.5, 0.75, T(s, "b_vm", "virtuelle Maschine\nAbschnitte 3, 5, 6, 7", "virtual machine\nsections 3, 5, 6, 7",
                                        "máquina virtual\nsecciones 3, 5, 6, 7", "虚拟机\n第 3、5、6、7 节",
                                        "machine virtuelle\nsections 3, 5, 6, 7", "sanal makine\nbölüm 3, 5, 6, 7"), 20, GRUEN_HELL)
    kasten(s, (-1.4, -1.5), 2.5, 0.75, T(s, "b_wsl", "WSL 2\nAbschnitte 3 und 4", "WSL 2\nsections 3 and 4", "WSL 2\nsecciones 3 y 4",
                                         "WSL 2\n第 3 和 4 节", "WSL 2\nsections 3 et 4", "WSL 2\nbölüm 3 ve 4"), 20, GRUEN_HELL)
    pf(s, (0.9, 1.5), (1.9, 1.5))
    pf(s, (0.9, 0.0), (1.9, 0.0))
    pf(s, (-1.4, 1.1), (-1.4, 0.4))
    pf(s, (-1.4, -0.4), (-1.4, -1.12))
    s.text(None, ja, (1.4, 1.7), WINZIG, "center")
    s.text(None, ja, (1.4, 0.2), WINZIG, "center")
    s.text(None, nein, (-1.25, 0.75), WINZIG, "left")
    s.text(None, nein, (-1.25, -0.76), WINZIG, "left")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 3
def k1vm():
    """Hardware, Wirt, Hypervisor, VM-Rahmen mit virtueller Hardware, Gast-Kernel und Programmen."""
    s = Szene("linux/k1vm")
    kasten(s, (0.2, -1.6), 8.2, 0.42, T(s, "hw", "echte Hardware: Prozessor, Arbeitsspeicher, SSD, Netzwerkkarte",
                                        "real hardware: processor, memory, SSD, network card",
                                        "hardware real: procesador, memoria, SSD, tarjeta de red", "真实硬件：处理器、内存、SSD、网卡",
                                        "matériel réel : processeur, mémoire, SSD, carte réseau",
                                        "gerçek donanım: işlemci, bellek, SSD, ağ kartı"), WINZIG, GRAU_HELL, form="rect")
    kasten(s, (0.2, -1.0), 8.2, 0.42, T(s, "wirt", "Wirt: Windows mit seinem Kernel", "host: Windows with its kernel",
                                        "anfitrión: Windows con su núcleo", "宿主：Windows 及其内核", "hôte : Windows avec son noyau",
                                        "ana sistem: Windows ve çekirdeği"), WINZIG, BLAU_HELL, form="rect")
    kasten(s, (-2.55, -0.4), 2.7, 0.42, T(s, "apps", "Browser, Editor, …", "browser, editor, …", "navegador, editor, …",
                                          "浏览器、编辑器……", "navigateur, éditeur, …", "tarayıcı, editör, …"), WINZIG, form="rect")
    kasten(s, (1.6, -0.4), 5.4, 0.42, T(s, "hv", "Hypervisor (z. B. VirtualBox)", "hypervisor (e.g. VirtualBox)",
                                        "hipervisor (p. ej., VirtualBox)", "虚拟机监视器（如 VirtualBox）", "hyperviseur (p. ex. VirtualBox)",
                                        "hipervizör (ör. VirtualBox)"), WINZIG, ORANGE_HELL, form="rect")
    flaeche(s, -1.1, 0.0, 4.3, 2.55, GRUEN_HELL, GRUEN, 2.5)
    s.text(None, T(s, "vm", "virtuelle Maschine", "virtual machine", "máquina virtual", "虚拟机", "machine virtuelle", "sanal makine"),
           (-1.0, 2.35), WINZIG, "left", GRUEN)
    kasten(s, (1.6, 0.5), 5.1, 0.62, T(s, "vhw", "virtuelle Hardware:\n2 Kerne, 6 GB, Platte (eine Datei), Netzwerkkarte",
                                       "virtual hardware:\n2 cores, 6 GB, disk (a file), network card",
                                       "hardware virtual:\n2 núcleos, 6 GB, disco (un archivo), tarjeta de red",
                                       "虚拟硬件：\n2 个核心、6 GB、磁盘（一个文件）、网卡",
                                       "matériel virtuel :\n2 cœurs, 6 Go, disque (un fichier), carte réseau",
                                       "sanal donanım:\n2 çekirdek, 6 GB, disk (bir dosya), ağ kartı"), WINZIG, form="rect")
    kasten(s, (1.6, 1.2), 5.1, 0.42, T(s, "gast", "Gast: Ubuntu mit eigenem Linux-Kernel", "guest: Ubuntu with its own Linux kernel",
                                       "invitado: Ubuntu con su propio núcleo Linux", "客户机：带自己 Linux 内核的 Ubuntu",
                                       "invité : Ubuntu avec son propre noyau Linux", "konuk: kendi Linux çekirdeğiyle Ubuntu"),
           WINZIG, form="rect")
    kasten(s, (1.6, 1.8), 5.1, 0.42, T(s, "pgast", "Programme im Gast", "programs in the guest", "programas en el invitado",
                                       "客户机中的程序", "programmes dans l’invité", "konuktaki programlar"), WINZIG, form="rect")
    s.speichern()


def k1snapshot():
    """Snapshot: Basisabbild (nur lesen) und Differenzabbild; Zurückspielen verwirft das Differenzabbild."""
    s = Szene("linux/k1snapshot")
    kasten(s, (-2.3, 0), 2.9, 1.0, T(s, "basis", "Basisabbild\nStand beim Snapshot\nnur noch lesen", "base image\nstate at the snapshot\nread only",
                                     "imagen base\nestado en la instantánea\nsolo lectura", "基础映像\n快照时的状态\n只读",
                                     "image de base\nétat au moment de l’instantané\nlecture seule",
                                     "temel kalıp\nanlık görüntüdeki durum\nyalnızca okunur"), WINZIG, GRAU_HELL, form="rect")
    kasten(s, (2.3, 0), 2.9, 1.0, T(s, "diff", "Differenzabbild\nalle Änderungen\nseit dem Snapshot", "differencing image\nall changes\nsince the snapshot",
                                    "imagen diferencial\ntodos los cambios\ndesde la instantánea", "差异映像\n快照之后的\n所有更改",
                                    "image différentielle\ntoutes les modifications\ndepuis l’instantané",
                                    "fark kalıbı\nanlık görüntüden bu yana\ntüm değişiklikler"), WINZIG, ORANGE_HELL, form="rect")
    kasten(s, (0, 1.7), 2.5, 0.45, T(s, "gast", "Gast liest und schreibt", "guest reads and writes", "el invitado lee y escribe",
                                     "客户机读写", "l’invité lit et écrit", "konuk okur ve yazar"), WINZIG)
    pf(s, (1.25, 1.47), (2.3, 0.52))
    pf(s, (0.0, 1.47), (0.85, 0.52), dash=DASH)
    pf(s, (0.83, 0.0), (-0.83, 0.0), dash=DASH)
    s.text(None, T(s, "schreiben", "schreiben", "write", "escribir", "写入", "écrire", "yaz"), (2.0, 1.15), WINZIG, "left")
    s.text(None, T(s, "lesen", "lesen:\nzuerst hier", "read:\nhere first", "leer:\nprimero aquí", "读取：\n先查这里", "lire :\nd’abord ici",
                   "oku:\nönce burada"), (0.2, 0.95), WINZIG, "right")
    s.text(None, T(s, "sonst", "sonst hier", "otherwise here", "si no, aquí", "否则查这里", "sinon ici", "yoksa burada"),
           (0.0, 0.22), WINZIG, "center")
    s.text(None, T(s, "zurueck", "Zurückspielen = dieses Abbild verwerfen", "restoring = discarding this image",
                   "restaurar = descartar esta imagen", "还原 = 丢弃此映像", "restaurer = abandonner cette image",
                   "geri yükleme = bu kalıbı atma"), (2.3, -0.8), WINZIG, "center", ROT)
    s.speichern()


def k1nat():
    """NAT-Modus: VM 10.0.2.15, Hypervisor als Router, Internet; Anfrage von außen endet beim Hypervisor."""
    s = Szene("linux/k1nat")
    flaeche(s, -4.0, -0.9, 1.05, 1.2, BLAU_HELL, BLAU, 2)
    s.text(None, T(s, "wirt", "Wirt", "host", "anfitrión", "宿主", "hôte", "ana sistem"), (-3.85, 0.98), WINZIG, "left", BLAU)
    kasten(s, (-2.8, 0.0), 1.4, 0.7, "", WINZIG, GRUEN_HELL)
    s.text(None, "VM", (-2.8, 0.13), WINZIG, "center")
    s.formel(r"\texttt{10.0.2.15}", mitte=(-2.8, -0.15), hoehe=0.1)
    kasten(s, (-0.2, 0.0), 2.1, 0.7, T(s, "hv", "Hypervisor\narbeitet als Router", "hypervisor\nacts as a router",
                                       "hipervisor\nhace de router", "虚拟机监视器\n充当路由器", "hyperviseur\nfait office de routeur",
                                       "hipervizör\nyönlendirici gibi çalışır"), WINZIG, ORANGE_HELL)
    kasten(s, (3.4, 0.0), 1.6, 0.5, "Internet", WINZIG)
    pf(s, (-2.1, 0.18), (-1.25, 0.18))
    pf(s, (-1.25, -0.18), (-2.1, -0.18))
    pf(s, (0.85, 0.12), (2.6, 0.12))
    pf(s, (2.6, -0.12), (0.85, -0.12))
    s.text(None, T(s, "anfrage", "Anfrage", "request", "petición", "请求", "requête", "istek"), (-1.67, 0.45), WINZIG, "center")
    s.text(None, T(s, "zurueck", "zurück", "back", "de vuelta", "返回", "retour", "geri"), (-1.67, -0.45), WINZIG, "center")
    s.text(None, T(s, "adresse", "unter der Adresse\ndes Wirts", "under the host’s\naddress", "con la dirección\ndel anfitrión",
                   "使用宿主的\n地址", "avec l’adresse\nde l’hôte", "ana sistemin\nadresiyle"), (1.8, 0.5), WINZIG, "center")
    s.text(None, T(s, "antwort", "Antwort", "reply", "respuesta", "应答", "réponse", "yanıt"), (1.72, -0.35), WINZIG, "center")
    s.linie(None, (3.4, -0.25), (3.4, -1.3), farbe=ROT, dicke=2.5, dash=DASH)
    s.linie(None, (3.4, -1.3), (-0.2, -1.3), farbe=ROT, dicke=2.5, dash=DASH)
    pf(s, (-0.2, -1.3), (-0.2, -0.37), farbe=ROT, dash=DASH)
    s.text(None, T(s, "aussen", "Anfrage von außen: niemand hat sie\nangestoßen, sie endet beim Hypervisor",
                   "request from outside: nobody started it,\nit ends at the hypervisor",
                   "petición desde fuera: nadie la inició,\ntermina en el hipervisor", "来自外部的请求：无人发起，\n止于虚拟机监视器",
                   "requête de l’extérieur : personne ne l’a lancée,\nelle s’arrête à l’hyperviseur",
                   "dışarıdan gelen istek: kimse başlatmadı,\nhipervizörde biter"), (1.6, -1.75), WINZIG, "center", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 4
def k1wsl():
    """WSL 2: Hypervisor von Microsoft, links Windows, rechts die kleine VM; Dateiserver in beide Richtungen."""
    s = Szene("linux/k1wsl")
    kasten(s, (0, -1.75), 8.0, 0.42, T(s, "hw", "echte Hardware", "real hardware", "hardware real", "真实硬件", "matériel réel",
                                       "gerçek donanım"), WINZIG, GRAU_HELL, form="rect")
    kasten(s, (0, -1.15), 8.0, 0.42, T(s, "hv", "Hypervisor von Microsoft", "Microsoft hypervisor", "hipervisor de Microsoft",
                                       "微软的虚拟机监视器", "hyperviseur de Microsoft", "Microsoft hipervizörü"), WINZIG, ORANGE_HELL,
           form="rect")
    flaeche(s, -4.0, -0.75, -0.4, 1.95, BLAU_HELL, BLAU, 2)
    flaeche(s, 0.4, -0.75, 4.0, 1.95, GRUEN_HELL, GRUEN, 2)
    s.text(None, "Windows", (-3.85, 1.75), WINZIG, "left", BLAU)
    s.text(None, T(s, "kvm", "kleine VM von WSL 2", "small WSL 2 VM", "VM pequeña de WSL 2", "WSL 2 的小型虚拟机",
                   "petite VM de WSL 2", "WSL 2’nin küçük VM’i"), (0.55, 1.75), WINZIG, "left", GRUEN)
    kasten(s, (-2.2, -0.35), 3.3, 0.42, T(s, "wk", "Windows-Kernel", "Windows kernel", "núcleo de Windows", "Windows 内核",
                                          "noyau Windows", "Windows çekirdeği"), WINZIG, form="rect")
    kasten(s, (-2.2, 0.35), 3.3, 0.56, "", form="rect")
    s.text(None, T(s, "expl", "Explorer", "Explorer", "Explorador", "资源管理器", "Explorateur", "Dosya Gezgini"), (-2.2, 0.48),
           WINZIG, "center")
    s.formel(r"\backslash\backslash\texttt{wsl.localhost}\backslash\ldots", mitte=(-2.2, 0.22), hoehe=0.13)
    kasten(s, (-2.2, 1.05), 3.3, 0.42, T(s, "lwc", "Laufwerk C:", "drive C:", "unidad C:", "C: 盘", "lecteur C:", "C: sürücüsü"),
           WINZIG, form="rect")
    kasten(s, (2.2, -0.35), 3.3, 0.42, T(s, "lk", "Linux-Kernel von Microsoft", "Linux kernel from Microsoft", "núcleo Linux de Microsoft",
                                         "微软构建的 Linux 内核", "noyau Linux de Microsoft", "Microsoft’un Linux çekirdeği"), WINZIG,
           form="rect")
    kasten(s, (2.2, 0.35), 3.3, 0.42, T(s, "distro", "Distribution Ubuntu", "distribution Ubuntu", "distribución Ubuntu",
                                        "发行版 Ubuntu", "distribution Ubuntu", "Ubuntu dağıtımı"), WINZIG, form="rect")
    kasten(s, (2.2, 1.05), 3.3, 0.42, "/mnt/c", WINZIG, form="rect")
    pf(s, (-0.55, 1.05), (0.55, 1.05), doppelt=True)
    pf(s, (-0.55, 0.35), (0.55, 0.35), doppelt=True)
    s.text(None, T(s, "server", "Datei-\nserver", "file\nserver", "servidor\nde archivos", "文件\n服务器", "serveur\nde fichiers",
                   "dosya\nsunucusu"), (0, 0.7), 16, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 5
def k1pruefsumme():
    """Ein Buchstabe anders, völlig andere SHA-256-Prüfsumme."""
    s = Szene("linux/k1pruefsumme")
    kasten(s, (-3.2, 0.5), 1.6, 0.42, "Hallo Linux", WINZIG, form="rect")
    kasten(s, (-3.2, -0.5), 1.6, 0.42, "Hallo Linuy", WINZIG, form="rect")
    kasten(s, (-1.1, 0.0), 1.2, 1.5, "SHA-256", WINZIG, ORANGE_HELL, form="rect")
    kasten(s, (2.0, 0.5), 3.4, 0.62, "99fe677717755bcd…\n…a042ca5c90157c1098", 16, form="rect")
    kasten(s, (2.0, -0.5), 3.4, 0.62, "bcfef736955e8b5f…\n…a6ef7c179d102bdd5", 16, form="rect")
    pf(s, (-2.4, 0.5), (-1.7, 0.5))
    pf(s, (-2.4, -0.5), (-1.7, -0.5))
    pf(s, (-0.5, 0.5), (0.3, 0.5))
    pf(s, (-0.5, -0.5), (0.3, -0.5))
    s.text(None, T(s, "anders", "1 Buchstabe anders", "1 letter different", "1 letra distinta", "仅 1 个字母不同", "1 lettre différente",
                   "1 harf farklı"), (-3.2, -1.05), WINZIG, "center")
    s.text(None, T(s, "hex", "64 Hexadezimalziffern, fast alle anders", "64 hexadecimal digits, almost all different",
                   "64 dígitos hexadecimales, casi todos distintos", "64 位十六进制数字，几乎全部不同",
                   "64 chiffres hexadécimaux, presque tous différents", "64 onaltılık basamak, neredeyse hepsi farklı"),
           (2.0, -1.05), WINZIG, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k1bootkette():
    """Bootkette mit Secure Boot: Firmware → shim → GRUB → Kernel, jedes Glied prüft das Siegel des nächsten."""
    s = Szene("linux/k1bootkette")
    glieder = ((-3.6, T(s, "fw", "Firmware\nkennt Microsoft", "firmware\nknows Microsoft", "firmware\nconoce a Microsoft",
                        "固件\n认识微软", "micrologiciel\nconnaît Microsoft", "üretici yazılımı\nMicrosoft’u tanır"), GRAU_HELL),
               (-1.2, T(s, "shim", "shim\nkennt Canonical", "shim\nknows Canonical", "shim\nconoce a Canonical", "shim\n认识 Canonical",
                        "shim\nconnaît Canonical", "shim\nCanonical’ı tanır"), ORANGE_HELL),
               (1.2, T(s, "grub", "GRUB\nBootloader", "GRUB\nboot loader", "GRUB\ncargador de arranque", "GRUB\n引导加载程序",
                       "GRUB\nchargeur d’amorçage", "GRUB\nönyükleyici"), ORANGE_HELL),
               (3.6, T(s, "kernel", "Linux-Kernel\nvon Ubuntu", "Linux kernel\nfrom Ubuntu", "núcleo Linux\nde Ubuntu",
                       "Ubuntu 的\nLinux 内核", "noyau Linux\nd’Ubuntu", "Ubuntu’nun\nLinux çekirdeği"), GRUEN_HELL))
    for x, text, farbe in glieder:
        kasten(s, (x, 0), 1.75, 0.7, text, WINZIG, farbe)
    laedt = T(s, "laedt", "lädt", "loads", "carga", "加载", "charge", "yükler")
    ms = T(s, "ms", "prüft Siegel\nvon Microsoft", "checks seal\nfrom Microsoft", "comprueba el sello\nde Microsoft",
           "检查微软的\n签名", "vérifie le sceau\nde Microsoft", "Microsoft mührünü\ndenetler")
    can = T(s, "can", "prüft Siegel\nvon Canonical", "checks seal\nfrom Canonical", "comprueba el sello\nde Canonical",
            "检查 Canonical\n的签名", "vérifie le sceau\nde Canonical", "Canonical mührünü\ndenetler")
    for x, siegel in ((-2.4, ms), (0.0, can), (2.4, can)):
        pf(s, (x - 0.32, 0), (x + 0.32, 0))
        s.text(None, laedt, (x, 0.22), 16, "center")
        s.text(None, siegel, (x, -0.75), 16, "center")
    s.text(None, T(s, "abbruch", "Passt ein Siegel nicht, bricht der Start an dieser Stelle ab.",
                   "If a seal does not match, booting stops at that point.",
                   "Si un sello no coincide, el arranque se detiene en ese punto.", "签名不匹配时，启动就在该处中止。",
                   "Si un sceau ne correspond pas, le démarrage s’arrête à cet endroit.",
                   "Bir mühür uymazsa önyükleme o noktada durur."), (0, -1.35), WINZIG, "center", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 8
def k1live():
    """Live-System: squashfs (unten, vom Stick) + tmpfs (oben, RAM) = ein Verzeichnisbaum; interne SSD nicht eingehängt."""
    s = Szene("linux/k1live")
    kasten(s, (0, 1.4), 5.6, 0.7, T(s, "sicht", "Verzeichnisbaum, den die Programme sehen: /\nlesen und schreiben wie auf einer Platte",
                                    "directory tree the programs see: /\nread and write as on a disk",
                                    "árbol de directorios que ven los programas: /\nleer y escribir como en un disco",
                                    "程序看到的目录树：/\n像在磁盘上一样读写",
                                    "arborescence vue par les programmes : /\nlire et écrire comme sur un disque",
                                    "programların gördüğü dizin ağacı: /\ndiskteki gibi okuma ve yazma"), WINZIG, GRUEN_HELL, form="rect")
    kasten(s, (0, 0.5), 5.6, 0.7, T(s, "ram", "obere Schicht im Arbeitsspeicher (tmpfs)\nnimmt alle Änderungen auf, ist beim Ausschalten weg",
                                    "upper layer in memory (tmpfs)\ntakes all changes, gone at power-off",
                                    "capa superior en la memoria (tmpfs)\nrecoge todos los cambios, desaparece al apagar",
                                    "内存中的上层（tmpfs）\n接收所有更改，关机后消失",
                                    "couche supérieure en mémoire (tmpfs)\nreçoit toutes les modifications, disparaît à l’arrêt",
                                    "bellekteki üst katman (tmpfs)\ntüm değişiklikleri alır, kapatınca silinir"), WINZIG, ORANGE_HELL,
           form="rect")
    kasten(s, (0, -0.4), 5.6, 0.7, T(s, "sq", "untere Schicht: komprimiertes Abbild (squashfs)\ndas System vom Stick, nur lesbar",
                                     "lower layer: compressed image (squashfs)\nthe system from the stick, read only",
                                     "capa inferior: imagen comprimida (squashfs)\nel sistema de la memoria, solo lectura",
                                     "下层：压缩映像（squashfs）\n来自 U 盘的系统，只读",
                                     "couche inférieure : image compressée (squashfs)\nle système de la clé, lecture seule",
                                     "alt katman: sıkıştırılmış kalıp (squashfs)\nbellekteki sistem, yalnızca okunur"), WINZIG, GRAU_HELL,
           form="rect")
    kasten(s, (-3.9, -0.4), 1.3, 0.42, T(s, "stick", "USB-Stick", "USB stick", "memoria USB", "U 盘", "clé USB", "USB bellek"), WINZIG)
    pf(s, (-3.25, -0.4), (-2.82, -0.4))
    kasten(s, (3.9, -1.35), 1.6, 0.6, T(s, "ssd", "interne SSD\nnicht eingehängt", "internal SSD\nnot mounted", "SSD interno\nno montado",
                                        "内置 SSD\n未挂载", "SSD interne\nnon montée", "dahili SSD\nbağlanmamış"), WINZIG, "#dddddd",
           textfarbe=GRAU, farbe=GRAU)
    s.linie(None, (2.95, -0.7), (2.95, 0.8), dicke=2.5)
    s.linie(None, (2.85, -0.7), (2.95, -0.7), dicke=2.5)
    s.linie(None, (2.85, 0.8), (2.95, 0.8), dicke=2.5)
    s.text(None, T(s, "overlay", "Overlay:\nzusammen-\ngelegt", "overlay:\nmerged", "overlay:\nsuperpuestas", "叠加：\n合并",
                   "overlay :\nsuperposées", "overlay:\nbirleştirilmiş"), (3.1, 0.05), WINZIG, "left")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 9
def k1datentraeger():
    """Datenträgerverwaltung schematisch: Datenträger 0 nie anfassen, Datenträger 1 (Stick) ist das Ziel."""
    s = Szene("linux/k1datentraeger")
    kasten(s, (-3.65, 0.6), 1.75, 0.95, T(s, "d0", "Datenträger 0\nBasis, 476,94 GB\nOnline", "Disk 0\nBasic, 476.94 GB\nOnline",
                                           "Disco 0\nBásico, 476,94 GB\nEn pantalla", "磁盘 0\n基本，476.94 GB\n联机",
                                           "Disque 0\nde base, 476,94 Go\nEn ligne", "Disk 0\nTemel, 476,94 GB\nÇevrimiçi"),
           16, GRAU_HELL, form="rect")
    kasten(s, (-2.37, 0.6), 0.75, 0.95, "260 MB\nEFI", 16, form="rect")
    kasten(s, (0.2, 0.6), 4.35, 0.95, T(s, "c", "Windows (C:)\n474 GB NTFS\nStartpartition, Auslagerungsdatei, …",
                                        "Windows (C:)\n474 GB NTFS\nBoot, Page File, …", "Windows (C:)\n474 GB NTFS\nArranque, archivo de paginación, …",
                                        "Windows (C:)\n474 GB NTFS\n启动、页面文件……", "Windows (C:)\n474 Go NTFS\nDémarrer, Fichier d’échange, …",
                                        "Windows (C:)\n474 GB NTFS\nÖnyükleme, Disk Belleği Dosyası, …"), 16, BLAU_HELL, form="rect")
    kasten(s, (2.87, 0.6), 1.0, 0.95, T(s, "rec", "2,7 GB\nWieder-\nherstellung", "2.7 GB\nrecovery", "2,7 GB\nrecuperación",
                                        "2.7 GB\n恢复", "2,7 Go\nrécupé-\nration", "2,7 GB\nkurtarma"), 16, form="rect")
    kasten(s, (-3.65, -0.6), 1.75, 0.95, T(s, "d1", "Datenträger 1\nWechselmedium\n7,45 GB, Online", "Disk 1\nRemovable\n7.45 GB, Online",
                                            "Disco 1\nExtraíble\n7,45 GB, En pantalla", "磁盘 1\n可移动\n7.45 GB，联机",
                                            "Disque 1\nAmovible\n7,45 Go, En ligne", "Disk 1\nÇıkarılabilir\n7,45 GB, Çevrimiçi"),
           16, GRAU_HELL, form="rect")
    kasten(s, (0.3, -0.6), 6.1, 0.95, T(s, "usb", "USB-STICK (E:)\n7,45 GB FAT32\nFehlerfrei (Primäre Partition)",
                                        "USB STICK (E:)\n7.45 GB FAT32\nHealthy (Primary Partition)",
                                        "USB (E:)\n7,45 GB FAT32\nCorrecto (partición primaria)", "U 盘 (E:)\n7.45 GB FAT32\n状态良好（主分区）",
                                        "CLÉ USB (E:)\n7,45 Go FAT32\nSain (partition principale)",
                                        "USB BELLEK (E:)\n7,45 GB FAT32\nSağlam (Birincil Bölüm)"), 16, GRUEN_HELL, form="rect")
    s.text(None, T(s, "nie", "nie anfassen", "never touch", "no tocar nunca", "切勿改动", "ne jamais toucher", "asla dokunma"),
           (3.5, 0.6), WINZIG, "left", ROT)
    s.text(None, T(s, "ziel", "Ziel", "target", "destino", "目标", "cible", "hedef"), (3.5, -0.6), WINZIG, "left", GRUEN)
    s.speichern()


def k1stick():
    """Stick vor und nach dem Schreiben des Ubuntu-Abbilds, schematisch und nicht maßstäblich."""
    s = Szene("linux/k1stick")
    tab = T(s, "tab", "Tab.", "table", "tabla", "分区表", "table", "tablo")
    s.text(None, T(s, "vorher", "vorher", "before", "antes", "之前", "avant", "önce"), (-4.1, 1.35), KLEIN, "left")
    kasten(s, (-3.7, 0.85), 0.62, 0.6, tab, 16, GRAU_HELL, form="rect")
    kasten(s, (0.35, 0.85), 7.5, 0.6, T(s, "fat", "Partition 1: FAT32, 7,45 GB  –  Referat.pdf, Fotos, …",
                                        "partition 1: FAT32, 7.45 GB  –  report.pdf, photos, …",
                                        "partición 1: FAT32, 7,45 GB  –  trabajo.pdf, fotos, …",
                                        "分区 1：FAT32，7.45 GB – 报告.pdf、照片……",
                                        "partition 1 : FAT32, 7,45 Go  –  exposé.pdf, photos, …",
                                        "bölüm 1: FAT32, 7,45 GB  –  ödev.pdf, fotoğraflar, …"), WINZIG, form="rect")
    s.text(None, T(s, "nachher", "nachher", "after", "después", "之后", "après", "sonra"), (-4.1, 0.0), KLEIN, "left")
    kasten(s, (-3.7, -0.5), 0.62, 0.6, tab, 16, ORANGE_HELL, form="rect")
    kasten(s, (-0.8, -0.5), 5.2, 0.6, T(s, "kopie", "Kopie des Abbilds, 6,48 GB:\nISO-Dateisystem mit squashfs",
                                        "copy of the image, 6.48 GB:\nISO file system with squashfs",
                                        "copia de la imagen, 6,48 GB:\nsistema de archivos ISO con squashfs",
                                        "映像的副本，6.48 GB：\n含 squashfs 的 ISO 文件系统",
                                        "copie de l’image, 6,48 Go :\nsystème de fichiers ISO avec squashfs",
                                        "kalıbın kopyası, 6,48 GB:\nsquashfs içeren ISO dosya sistemi"), WINZIG, ORANGE_HELL, form="rect")
    kasten(s, (2.15, -0.5), 0.7, 0.6, "EFI", 16, "#f8cdb5", form="rect")
    kasten(s, (3.3, -0.5), 1.6, 0.6, T(s, "rest", "Rest ungenutzt", "rest unused", "resto sin usar", "其余未使用", "reste inutilisé",
                                       "kalan kullanılmıyor"), 16, GRAU_HELL, form="rect", textfarbe=GRAU)
    s.speichern()


SZENEN = (k1schichten, k1systemaufruf, k1wege, k1entscheidung, k1vm, k1snapshot, k1nat, k1wsl, k1pruefsumme, k1bootkette,
          k1live, k1datentraeger, k1stick)

for f in SZENEN:
    f()
