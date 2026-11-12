"""UI-Test der Editor-Welle F1 „Bildschirme und Fenster“ im echten Browser (Pyodide): Palette „Bildschirm & Fenster“,
Terminal einfügen, Inhalt im Textfeld ändern, Zustände als Schritte anlegen, abspielen (das Bild läuft), PNG-Export,
Auswahllisten (Stil), die übrigen Palette-Einträge. Aufruf: editor_terminal_test.py <ausgabeordner> [basis-url]
Voraussetzung: Vorschau-Server (python -m http.server 8000 --directory web); andere Adresse als zweites Argument,
z. B. http://localhost:8007/editor.html."""
import hashlib
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright  # noqa: E402

OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
BASE = sys.argv[2] if len(sys.argv) > 2 else "http://localhost:8000/editor.html"
ok_all = True
NEU = ("student@labor:~$ \\e|\\e>echo Hallo Welt\n\\e|Hallo Welt\n\\e|student@labor:~$ \\e|\\e~")


def check(name, cond, extra=""):
    global ok_all
    print(("  OK   " if cond else " FAIL  ") + name + (("  :: " + str(extra)[:300]) if extra != "" and not cond else ""))
    ok_all = ok_all and bool(cond)


def canvas_hash(pg):
    return hashlib.md5(pg.locator("#view").screenshot()).hexdigest()


def wait_ready(pg):
    pg.wait_for_function("document.getElementById('status') && /Ready|Szene geladen/.test(document.getElementById('status').textContent)",
                         timeout=120000)
    pg.wait_for_timeout(1500)


def status_ok(pg):
    st = pg.locator("#status").text_content() or ""
    return not (st.startswith("⚠") or "error" in st.lower() or "Fehler" in st), st


def prop(pg, name):
    return pg.locator("#props .prop").filter(has=pg.locator("label", has_text=re.compile("^%s$" % re.escape(name))))


with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    ctx = b.new_context(viewport={"width": 1500, "height": 1100}, accept_downloads=True)
    ctx.add_init_script('try{localStorage.clear();localStorage.setItem("animate-theme","light")}catch(e){}')
    pg = ctx.new_page()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(BASE, wait_until="domcontentloaded")
    wait_ready(pg)
    for _ in range(20):                                  # leere Szene: das Startbeispiel (3D-Fläche) entfernen
        d = pg.locator("#scene-objs .obj-row .del")
        if not d.count():
            break
        d.first.click()
        pg.wait_for_timeout(400)
    pg.wait_for_timeout(1500)
    h0 = canvas_hash(pg)

    # 1. Palette: Gruppe „Bildschirm & Fenster“, Terminal einfügen
    grp = pg.locator("#palette details", has_text="Bildschirm & Fenster")
    check("Palette-Gruppe „Bildschirm & Fenster“", grp.count() == 1)
    grp.locator("summary").click()
    items = grp.locator(".palette-item").all_text_contents()
    check("Einträge: Terminal, Datei-Ansicht, TUI: top, TUI: Pager, Textblock, Schloss",
          items == ["Terminal", "Datei-Ansicht", "TUI: top", "TUI: Pager", "Textblock", "Schloss"], items)
    grp.locator(".palette-item", has_text=re.compile("^Terminal$")).click()
    pg.wait_for_timeout(3000)
    good, st = status_ok(pg)
    h1 = canvas_hash(pg)
    check("Terminal eingefügt und gezeichnet", good and h1 != h0, st)
    vm = pg.locator("#view-mode")
    check("Bildschirme sind flach: Ansicht 2D", (not vm.count()) or vm.input_value() == "2d")
    pg.locator("#view").screenshot(path=str(OUT / "f1_terminal_eingefuegt.png"))
    check("Eigenschaften: Inhalt als Textfeld, Auswahllisten frame/theme/buttons",
          prop(pg, "text").locator("textarea").count() == 1 and prop(pg, "frame").locator("select").count() == 1
          and prop(pg, "theme").locator("select").count() == 1 and prop(pg, "buttons").locator("select").count() == 1)

    # 2. Inhalt ändern
    ta = prop(pg, "text").locator("textarea")
    ta.fill(NEU)
    ta.dispatch_event("change")
    pg.wait_for_timeout(2500)
    h2 = canvas_hash(pg)
    check("Inhalt geändert: das Bild ändert sich", h2 != h1 and status_ok(pg)[0], status_ok(pg)[1])
    pg.locator("#view").screenshot(path=str(OUT / "f1_terminal_inhalt.png"))
    hint = pg.locator("#props .hint", has_text="Zustände").text_content() or ""
    check("Hinweis zählt die Zustände (4)", "Zustände: 4" in hint, hint)

    # 3. Zustände als Schritte
    pg.click("#terminal-steps")
    pg.wait_for_timeout(2500)
    rows = pg.locator("#scene-anims .anim-row")
    texts = [rows.nth(i).text_content() or "" for i in range(rows.count())]
    state = prop(pg, "state").locator("input").input_value() if prop(pg, "state").locator("input").count() else ""
    par_row = pg.locator("#scene-objs .obj-row", has_text="term1").count()
    check("Zustände als Schritte: 4 × ChangeValue auf den neuen Parameter term1, state = term1",
          len(texts) == 4 and all("ChangeValue" in t for t in texts) and state == "term1" and par_row >= 1, (texts, state, par_row))
    times = [(rows.nth(i).locator(".hint").text_content() or "").rstrip("s") for i in range(rows.count())]
    check("Dauer je Schritt: getippt 14 Zeichen/s, Ausgabe 0,6 s, Warten 1,2 s", times == ["1.14", "0.6", "0.6", "1.2"], times)
    h3 = canvas_hash(pg)
    check("Bearbeitungsansicht zeigt den Anfangszustand (nur der Prompt)", h3 != h2)
    pg.locator("#view").screenshot(path=str(OUT / "f1_terminal_start.png"))

    # 4. abspielen: das Bild läuft durch mehrere Zustände
    pg.click("#play-btn")
    seen = []
    for i in range(24):
        pg.wait_for_timeout(250)
        seen.append(canvas_hash(pg))
        if i in (6, 12):
            pg.locator("#view").screenshot(path=str(OUT / f"f1_terminal_spielt_{i}.png"))
    pg.wait_for_timeout(1500)
    check("Abspielen: mindestens vier verschiedene Bilder (Tippen, Ausgabe, Prompt, Blinken)", len(set(seen)) >= 4, len(set(seen)))
    pg.locator("#view").screenshot(path=str(OUT / "f1_terminal_ende.png"))

    # 5. PNG-Export (Knopf „Photo“)
    with pg.expect_download(timeout=60000) as dl:
        pg.click("#dl-png")
    data = Path(dl.value.path()).read_bytes()
    (OUT / "f1_export.png").write_bytes(data)
    check("PNG-Export liefert ein PNG", data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) > 5000, len(data))

    # 6. Stil wechseln (hell) und die übrigen Palette-Einträge
    trow = pg.locator("#scene-objs .obj-row", has_text="Terminal")
    if trow.count():
        trow.first.click()
    pg.wait_for_timeout(500)
    sel = prop(pg, "theme").locator("select")
    if sel.count():
        h4 = canvas_hash(pg)
        sel.select_option("hell")
        pg.wait_for_timeout(2500)
        check("Stil hell: das Bild ändert sich", canvas_hash(pg) != h4)
    for name in ("Datei-Ansicht", "TUI: top", "TUI: Pager", "Textblock", "Schloss"):
        hb = canvas_hash(pg)
        grp.locator(".palette-item", has_text=re.compile("^%s$" % re.escape(name))).click()
        pg.wait_for_timeout(2500)
        good, st = status_ok(pg)
        check(f"Palette {name}: eingefügt, gezeichnet, kein Fehler", good and canvas_hash(pg) != hb, st)
    pg.locator("#view").screenshot(path=str(OUT / "f1_alle_bausteine.png"))
    check("keine Seitenfehler (pageerror)", not errors, "; ".join(errors[:3]))
    b.close()
print("F1-UI-TESTS OK" if ok_all else "F1-UI-TESTS MIT FEHLERN")
sys.exit(0 if ok_all else 1)
