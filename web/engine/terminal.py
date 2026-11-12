"""Screens and windows (F1 "Bildschirme und Fenster", 12.11.2026): a terminal window, a file view and full-screen
programs (top, a pager) as ONE composite object of the model, type "Terminal"; plus a small neutral lock symbol
("Lock"). Guide: notizen/animationen.md §11; palette: notizen/f1_terminal_palette.md.

Everything is built from the existing primitives: paths (window, title bar, buttons, cell backgrounds, cursor) and
labels in the typewriter font. One screen row is ONE Text with coloured sections (Text.spans -> <tspan>), never one
object per character. Editor (Pyodide), export (SVG, .anim.svg), vector PDF and the website player therefore need no
new rendering path.

Content (prop `text`) is a stream as a real terminal receives it:
  - characters, newline (line feed + carriage return), \\r, \\t (tab stops of 8), \\b;
  - ANSI: SGR colours and attributes (engine/ansi.py), cursor position ESC[r;cH, ESC[nA/B/C/D/G, erase ESC[J / ESC[K,
    ESC[?25l / ESC[?25h (cursor off/on), ESC c (reset);
  - escapes may be written as backslash-e (\\e[1;32m), a literal backslash before e as two backslashes;
  - four marks for the timeline:  \\e|  next state (step)   \\e>  from here to the end of the step: typed, character
    by character   \\e~  the cursor waits (blinks three times) in this step   \\e!  the window closes (× lights up,
    the window fades out).
A prompt at the start of a line (user@host:path$ or #) gets the colours of the default .bashrc (user@host bold green,
path bold blue) when prompt_colors is on.

State (prop `state`): a number (usually the name of a scene parameter, L3). Step 0 is everything before the first \\e|;
state k shows steps 0..k; between k-1 and k step k runs (typed text proportionally, fading, blinking). Empty = the
end state. tools/szenen_lib.py writes one ChangeValue per step (rate linear), so the steps are ordinary steps of the
timeline and the object is rebuilt per frame like every object under a moving parameter (ENGINE_CONTRACT, L3).

Geometry (world units, 1 unit = 135 scene px): `position` = top-left corner of the window; cell width 0.6 em, line
pitch `line_height` em, padding 0.6 em left/right and 0.45 em top/bottom, title bar 2 em. geometry() is the single
source for the builder and the column helpers of tools/szenen_lib.py.
"""
import re
from functools import lru_cache

import numpy as np

from .AnimObject import AnimObject
from .bezier import line_points
from .simpleShape import Circle
from .text import Text
from .richtext import MONO_CELL, is_wide
from .export import char_em as _char_em
from . import ansi as _ansi

UPP = 1.0 / 135.0                      # world units per scene pixel (engine/constants: 8 units = 1080 px)
FRAMES = ("fenster", "datei", "ohne")
BUTTONS = ("drei", "x", "keine")
BAR_EM = 2.0                           # title bar height in em of the terminal font
PAD_X_EM, PAD_Y_EM = 0.6, 0.45
TITLE_EM = 0.85                        # title font size relative to the terminal font
TAB = 8
_MAX_ROWS = 400                        # safety limits (a stream that runs away)
_MAX_COLS = 400

_PROMPT = re.compile(r"([A-Za-z0-9._-]+@[A-Za-z0-9._-]+)(:)([^\n$#\x1b]*?)([$#])(?= |$)")


# ---------------------------------------------------------------------------------------------------------------
# 1. The stream: tokens and steps
_TOKEN = re.compile(r"\x1b\[([0-?]*)([ -/]*)([@-~])|\x1b(.)?|(\n)|(\r)|(\t)|(\x08)|([^\x1b\n\r\t\x08]+)", re.S)
_MARKS = {"|": "step", ">": "type", "~": "wait", "!": "close", "c": "reset"}


@lru_cache(maxsize=256)
def steps(text):
    """The stream split into steps: a tuple of steps, each a tuple of tokens ("t", text) | ("nl",) | ("cr",) |
    ("tab",) | ("bs",) | ("csi", params, final) | ("type",) | ("wait",) | ("close",) | ("reset",)."""
    s = _ansi.unescape(text)
    segs, cur = [], []
    for m in _TOKEN.finditer(s):
        if m.group(3) is not None:
            cur.append(("csi", m.group(1), m.group(3)))
        elif m.group(0).startswith("\x1b"):
            kind = _MARKS.get(m.group(4) or "")
            if kind == "step":
                segs.append(tuple(cur))
                cur = []
            elif kind:
                cur.append((kind,))
        elif m.group(5):
            cur.append(("nl",))
        elif m.group(6):
            cur.append(("cr",))
        elif m.group(7):
            cur.append(("tab",))
        elif m.group(8):
            cur.append(("bs",))
        else:
            cur.append(("t", m.group(9)))
    segs.append(tuple(cur))
    return tuple(segs)


def step_count(text):
    """Number of steps after the start (the largest useful state)."""
    return len(steps(str(text or ""))) - 1


# ---------------------------------------------------------------------------------------------------------------
# 2. A tiny terminal: cells, cursor, scrolling
class _Screen:
    def __init__(self, cols, rows, pal, prompt_colors=True):
        self.cols, self.rows = cols, rows            # None = grows (auto size)
        self.pal = pal
        self.prompt_colors = prompt_colors
        self.lines = [[] for _ in range(rows)] if rows else [[]]
        self.r = self.c = 0
        self.attr = _ansi.Attr()
        self.cursor_on = True
        self.max_c = 0
        self.max_r = 0

    def _row(self, r):
        while r >= len(self.lines):
            self.lines.append([])
        return self.lines[r]

    def _put(self, ch, fg, bg, bold):
        if self.cols and self.c >= self.cols:        # deferred wrap, as xterm
            self.newline()
        row = self._row(self.r)
        w = 2 if is_wide(ch) else 1
        while len(row) < self.c + w:
            row.append((" ", None, None, False))
        row[self.c] = (ch, fg, bg, bold)
        if w == 2:
            row[self.c + 1] = ("", fg, bg, bold)      # second cell of a wide character (drawn by the first)
        self.c += w
        self.max_c = max(self.max_c, min(self.c, _MAX_COLS))
        self.max_r = max(self.max_r, self.r)

    def write(self, text, typed=False):
        if not typed and self.prompt_colors and self.c == 0:
            m = _PROMPT.match(text)
            if m:
                keep = self.attr.copy()
                for part, code in ((m.group(1), "1;32"), (m.group(2), "0"), (m.group(3), "1;34"), (m.group(4), "0")):
                    self.attr = keep.copy()
                    self.attr.sgr(code)
                    self._write_plain(part)
                self.attr = keep
                text = text[m.end():]
        self._write_plain(text)

    def _write_plain(self, text):
        fg, bg, bold = _ansi.resolve(self.attr, self.pal)
        for ch in text:
            self._put(ch, fg, bg, bold)

    def newline(self):
        self.c = 0
        self.r += 1
        if self.rows and self.r >= self.rows:        # scroll: the top line leaves the window
            self.lines.pop(0)
            self.lines.append([])
            self.r = self.rows - 1
        elif not self.rows:
            self._row(min(self.r, _MAX_ROWS))
        self.r = min(self.r, _MAX_ROWS)

    def tab(self):
        stop = (self.c // TAB + 1) * TAB
        if self.cols:
            stop = min(stop, self.cols - 1)
        while self.c < stop:
            self._put(" ", *_ansi.resolve(self.attr, self.pal))

    def clear(self, mode=2):
        if mode in (2, 3):
            n = len(self.lines)
            self.lines = [[] for _ in range(n)]
        elif mode == 0:                              # cursor to end of screen
            self.lines[self.r] = self._row(self.r)[:self.c]
            for i in range(self.r + 1, len(self.lines)):
                self.lines[i] = []
        elif mode == 1:
            for i in range(0, self.r):
                self.lines[i] = []
            row = self._row(self.r)
            for i in range(min(self.c + 1, len(row))):
                row[i] = (" ", None, None, False)

    def erase_line(self, mode=0):
        row = self._row(self.r)
        if mode == 0:
            del row[self.c:]
        elif mode == 1:
            for i in range(min(self.c + 1, len(row))):
                row[i] = (" ", None, None, False)
        else:
            row.clear()

    def csi(self, params, final):
        if final == "m":
            self.attr.sgr(params)
            return
        if params.startswith("?"):
            if params[1:] == "25" and final in "hl":
                self.cursor_on = final == "h"
            return
        nums = [int(p) if p.isdigit() else 0 for p in params.split(";")] if params else []
        n = nums[0] if nums and nums[0] > 0 else 1
        if final == "s":                             # save / restore the cursor (top, setze in szenen_lib)
            self.saved = (self.r, self.c)
            return
        if final == "u":
            self.r, self.c = getattr(self, "saved", (self.r, self.c))
            return
        if final in "Hf":
            r = (nums[0] if len(nums) > 0 and nums[0] > 0 else 1) - 1
            c = (nums[1] if len(nums) > 1 and nums[1] > 0 else 1) - 1
            self.r = min(r, (self.rows - 1) if self.rows else _MAX_ROWS)
            self.c = min(c, (self.cols - 1) if self.cols else _MAX_COLS)
            self._row(self.r)
            self.max_r = max(self.max_r, self.r)
        elif final == "J":
            self.clear(nums[0] if nums else 0)
        elif final == "K":
            self.erase_line(nums[0] if nums else 0)
        elif final == "A":
            self.r = max(0, self.r - n)
        elif final == "B":
            self.r = min(self.r + n, (self.rows - 1) if self.rows else _MAX_ROWS)
            self._row(self.r)
        elif final == "C":
            self.c = min(self.c + n, (self.cols - 1) if self.cols else _MAX_COLS)
        elif final == "D":
            self.c = max(0, self.c - n)
        elif final == "G":
            self.c = min(n - 1, (self.cols - 1) if self.cols else _MAX_COLS)

    def reset(self):
        self.lines = [[] for _ in range(len(self.lines))]
        self.r = self.c = 0
        self.attr.reset()
        self.cursor_on = True

    def token(self, tok, typed=False):
        k = tok[0]
        if k == "t":
            self.write(tok[1], typed)
        elif k == "nl":
            self.newline()
        elif k == "cr":
            self.c = 0
        elif k == "tab":
            self.tab()
        elif k == "bs":
            self.c = max(0, self.c - 1)
        elif k == "csi":
            self.csi(tok[1], tok[2])
        elif k == "reset":
            self.reset()


def _units(tok):
    """Typed units of a token: every character and every newline counts one (escape sequences none)."""
    if tok[0] == "t":
        return len(tok[1])
    return 1 if tok[0] in ("nl", "tab") else 0


def run(text, state=None, cols=None, rows=None, theme="dunkel", prompt_colors=True):
    """The screen at `state` (None = end). Returns a dict: screen (_Screen), close (0 open .. 1 gone), close_hl (× lit),
    blink (cursor shown in a waiting step), steps (number of steps after the start)."""
    segs = steps(str(text or ""))
    sc = _Screen(cols, rows, _ansi.palette(theme), prompt_colors)
    n = len(segs) - 1
    s = float(n) if state is None else float(state)
    close, close_hl, blink = 0.0, False, True
    for k, seg in enumerate(segs):
        if k == 0:
            f = 1.0
        elif s >= k - 1e-9:
            f = 1.0
        elif s > k - 1:
            f = s - (k - 1)
        else:
            break
        if close >= 1.0:
            break
        typed = False
        total = 0
        seen_type = False
        for tok in seg:
            if tok[0] == "type":
                seen_type = True
            elif seen_type:
                total += _units(tok)
        shown = total if f >= 1.0 else int(np.floor(f * total + 1e-9))
        for tok in seg:
            kind = tok[0]
            if kind == "type":
                typed = True
                continue
            if kind == "wait":
                if f < 1.0:
                    blink = int(f * 6.0) % 2 == 0
                continue
            if kind == "close":
                close_hl = True
                close = 1.0 if f >= 1.0 else min(1.0, max(0.0, (f - 0.4) / 0.6))
                continue
            if typed:
                u = _units(tok)
                if u == 0:
                    if shown > 0 or f >= 1.0:
                        sc.token(tok, True)
                    continue
                if shown <= 0:
                    break
                if tok[0] == "t" and u > shown:
                    sc.token(("t", tok[1][:shown]), True)
                    shown = 0
                    break
                sc.token(tok, True)
                shown -= u
            else:
                sc.token(tok)
        if f < 1.0:
            break
    return {"screen": sc, "close": close, "close_hl": close_hl, "blink": blink, "steps": n}


@lru_cache(maxsize=256)
def extent(text, cols=0, rows=0, cursor=True, prompt_colors=True):
    """(cols, rows) the window needs over ALL states: given values stay, 0 = the largest width/height the stream
    reaches (with a shown cursor its row counts). Independent of the state, so the window keeps its size."""
    segs = steps(str(text or ""))
    sc = _Screen(cols or None, rows or None, _ansi.palette("dunkel"), prompt_colors)
    used_r = 0
    for seg in segs:
        for tok in seg:
            if tok[0] in ("type", "wait", "close"):
                continue
            sc.token(tok, True)
            if tok[0] == "t":
                used_r = max(used_r, sc.r)
            if cursor and sc.cursor_on:
                used_r = max(used_r, sc.r)
        if cursor and sc.cursor_on:
            used_r = max(used_r, sc.r)
    c = cols or max(1, sc.max_c)
    r = rows or max(1, used_r + 1)
    return int(min(c, _MAX_COLS)), int(min(r, _MAX_ROWS))


def screen_rows(text, state=None, cols=0, rows=0, cursor=True, prompt_colors=True):
    """The plain text of every screen row at `state` (for the column helpers: fields, search)."""
    c, r = extent(str(text or ""), int(cols or 0), int(rows or 0), bool(cursor), bool(prompt_colors))
    sc = run(text, state, c, r, "dunkel", prompt_colors)["screen"]
    return ["".join(ch for ch, *_ in row).rstrip() for row in sc.lines[:r]]


# ---------------------------------------------------------------------------------------------------------------
# 3. Geometry (shared with tools/szenen_lib.py)
def geometry(args, cols, rows):
    """Window layout in world units for (cols, rows): x0, y0 (top-left), w, h, bar, cw (cell width), lh (line pitch),
    sx (left edge of column 0), sy0 (top of row 0), fs (font size, scene px), radius."""
    fs = float(args.get("font_size", 20) or 20)
    frame = str(args.get("frame", "fenster") or "fenster")
    lh_em = float(args.get("line_height", 1.2) or 1.2)
    x0, y0 = (float(v) for v in (list(args.get("position", [0.0, 0.0, 0.0])) + [0.0, 0.0])[:2])
    em = fs * UPP
    cw = MONO_CELL * em
    lh = lh_em * em
    bar = BAR_EM * em if frame in ("fenster", "datei") else 0.0
    padx, pady = PAD_X_EM * em, PAD_Y_EM * em
    w = cols * cw + 2 * padx
    h = bar + rows * lh + 2 * pady
    return {"x0": x0, "y0": y0, "w": w, "h": h, "bar": bar, "cw": cw, "lh": lh, "sx": x0 + padx,
            "sy0": y0 - bar - pady, "fs": fs, "em": em, "radius": (0.5 * em if frame != "ohne" else 0.15 * em),
            "cols": cols, "rows": rows, "frame": frame}


def _args_extent(args):
    return extent(str(args.get("text", "") or ""), int(args.get("cols", 0) or 0), int(args.get("rows", 0) or 0),
                  bool(args.get("cursor", True)), bool(args.get("prompt_colors", True)))


# ---------------------------------------------------------------------------------------------------------------
# 4. Building blocks: paths
_K = 0.5522847498                      # quarter circle as one cubic Bézier


def _rrect(x0, y0, x1, y1, rt, rb):
    """Closed Bézier path of a rectangle (x0 < x1, y0 < y1, world) with top corners rt and bottom corners rb."""
    rt = max(0.0, min(rt, (x1 - x0) / 2, (y1 - y0) / 2))
    rb = max(0.0, min(rb, (x1 - x0) / 2, (y1 - y0) / 2))
    P = [np.array([x0 + rb, y0, 0.0])]           # counter-clockwise, starting on the bottom edge

    def line_to(x, y):
        a, b = P[-1], np.array([x, y, 0.0])
        if np.abs(b - a).max() > 1e-12:
            P.extend([a + (b - a) / 3, a + (b - a) * 2 / 3, b])

    def arc(cx, cy, r, a0):                      # quarter circle from angle a0 to a0 + 90°
        if r <= 1e-12:
            return
        a1 = a0 + np.pi / 2
        p0 = P[-1]
        p3 = np.array([cx + r * np.cos(a1), cy + r * np.sin(a1), 0.0])
        t0 = np.array([-np.sin(a0), np.cos(a0), 0.0])
        t1 = np.array([-np.sin(a1), np.cos(a1), 0.0])
        P.extend([p0 + _K * r * t0, p3 - _K * r * t1, p3])
    line_to(x1 - rb, y0)
    arc(x1 - rb, y0 + rb, rb, -np.pi / 2)
    line_to(x1, y1 - rt)
    arc(x1 - rt, y1 - rt, rt, 0.0)
    line_to(x0 + rt, y1)
    arc(x0 + rt, y1 - rt, rt, np.pi / 2)
    line_to(x0, y0 + rb)
    arc(x0 + rb, y0 + rb, rb, np.pi)
    return np.array(P)


def _shape(points, fill, fill_opacity=1.0, stroke=None, width=0.0):
    o = AnimObject()
    o.points = points
    o.fill_color = _ansi.hex_rgb(fill) if isinstance(fill, str) else fill
    o.fill_opacity = fill_opacity
    o.color = _ansi.hex_rgb(stroke) if isinstance(stroke, str) else (stroke or o.fill_color)
    o.stroke_width = width
    return o


def _rect(x0, y0, x1, y1, fill, opacity=1.0):
    return _shape(line_points([[x0, y0, 0], [x1, y0, 0], [x1, y1, 0], [x0, y1, 0], [x0, y0, 0]]), fill, opacity)


def _stroke(pts, color, width):
    o = AnimObject()
    o.points = line_points([[p[0], p[1], 0.0] for p in pts])
    o.color = _ansi.hex_rgb(color)
    o.stroke_width = width
    o.fill_opacity = 0.0
    return o


def _buttons(g, pal, kind, close_hl):
    """GNOME-like round buttons at the right end of the title bar: (–, □, ×) or only ×."""
    grp = AnimObject()
    if kind not in ("drei", "x") or g["bar"] <= 0:
        return grp
    bar = g["bar"]
    d = 0.55 * bar
    gap = 0.2 * bar
    right = g["x0"] + g["w"] - 0.28 * bar
    yc = g["y0"] - bar / 2
    sw = max(1.2, 0.055 * bar / UPP)             # icon stroke in scene px
    names = ("min", "max", "close") if kind == "drei" else ("close",)
    for i, name in enumerate(reversed(names)):
        xc = right - d / 2 - i * (d + gap)
        hot = name == "close" and close_hl
        c = Circle(center=np.array([xc, yc, 0.0]), radius=d / 2)
        c.fill_color = _ansi.hex_rgb(pal["close"] if hot else pal["button"])
        c.fill_opacity = 1.0
        c.color = c.fill_color
        c.stroke_width = 0.0
        icon_col = pal["close_icon"] if hot else pal["icon"]
        a = 0.17 * d
        b = AnimObject()
        b.add(c)
        if name == "min":
            b.add(_stroke([(xc - a, yc), (xc + a, yc)], icon_col, sw))
        elif name == "max":
            b.add(_stroke([(xc - a, yc - a), (xc + a, yc - a), (xc + a, yc + a), (xc - a, yc + a), (xc - a, yc - a)],
                          icon_col, sw))
        else:
            b.add(_stroke([(xc - a, yc - a), (xc + a, yc + a)], icon_col, sw))
            b.add(_stroke([(xc - a, yc + a), (xc + a, yc - a)], icon_col, sw))
        grp.add(b)
    return grp


def _fade(o, k):
    o.fill_opacity *= k
    o.stroke_opacity *= k
    for s in o.subObjects:
        _fade(s, k)


# ---------------------------------------------------------------------------------------------------------------
# 5. The builder
def _state(v):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None                                # an unknown parameter name: the end state


def build_terminal(args, style, axes):
    """Model type "Terminal". Props: text (stream), cols, rows (0 = as needed), font_size (scene px), line_height (em),
    position (top-left, data coords), frame (fenster | datei | ohne), theme (dunkel | hell), title, buttons
    (drei | x | keine), cursor, prompt_colors, shadow, state (number / parameter name; "" = end)."""
    text = str(args.get("text", "") or "")
    theme = str(args.get("theme", "dunkel") or "dunkel")
    pal = _ansi.palette(theme)
    frame = str(args.get("frame", "fenster") or "fenster")
    cursor = bool(args.get("cursor", True))
    pc = bool(args.get("prompt_colors", True))
    cols, rows = _args_extent(args)
    p = list(args.get("position", [0.0, 0.0, 0.0])) + [0.0, 0.0, 0.0]
    if axes is not None:                           # the corner in data coordinates, everything else in world units
        w = np.asarray(axes.coords_to_point(float(p[0]), float(p[1]), 0.0), dtype=float)
        p = [w[0], w[1], 0.0]
    g = geometry(dict(args, position=p), cols, rows)
    res = run(text, _state(args.get("state")), cols, rows, theme, pc)
    sc = res["screen"]
    x0, y0, W, H, bar, rr = g["x0"], g["y0"], g["w"], g["h"], g["bar"], g["radius"]
    root = AnimObject()
    root.color = _ansi.hex_rgb(pal["fg"])
    # 0 shadow (two soft rings below the window)
    sh = AnimObject()
    if bool(args.get("shadow", True)) and frame != "ohne":
        for grow, dy, op in ((2.0, 1.5, 0.10), (5.0, 3.0, 0.05)):
            e = grow * UPP
            sh.add(_shape(_rrect(x0 - e, y0 - H - e - dy * UPP, x0 + W + e, y0 + e - dy * UPP, rr + e, rr + e),
                          pal["shadow"], op))
    root.add(sh)
    # 1 window body
    body = _shape(_rrect(x0, y0 - H, x0 + W, y0, rr, rr), pal["bg"], 1.0, pal["border"], 1.2 if frame != "ohne" else 0.0)
    root.add(body)
    # 2 title bar with its title
    tb = AnimObject()
    if bar > 0:
        tb.add(_shape(_rrect(x0, y0 - bar, x0 + W, y0, rr, 0.0), pal["bar"], 1.0))
        if pal.get("sep"):
            tb.add(_stroke([(x0, y0 - bar), (x0 + W, y0 - bar)], pal["sep"], 1.0))
        title = str(args.get("title", "") or "")
        if title:
            # centred like GNOME; when the buttons are in the way, centred in the room left of them; still too long:
            # shortened with … (widths of the bold sans font estimated 6 % above Arial regular, export.char_em)
            tfs = max(min(17.0, g["fs"]), TITLE_EM * g["fs"])   # not below 17 scene px (export minimum)
            nbtn = {"drei": 3, "x": 1}.get(str(args.get("buttons", "drei")), 0)
            left, right = x0 + 0.4 * bar, x0 + W - (0.28 * bar + nbtn * 0.75 * bar) - 0.15 * bar
            wid = lambda s_: 1.06 * tfs * UPP * sum(_char_em(ch) for ch in s_)
            while len(title) > 2 and wid(title) > right - left:
                title = title[:-2].rstrip() + "…"
            xc = x0 + W / 2
            if xc + wid(title) / 2 > right:
                xc = max(left + wid(title) / 2, right - wid(title) / 2)
            t = Text(title, position=np.array([xc, y0 - bar / 2, 0.0]), font_size=tfs,
                     color=_ansi.hex_rgb(pal["bar_text"]), align="center", raw=True)
            t.spans = ((0, len(title), None, True),)
            tb.add(t)
    root.add(tb)
    # 3 buttons
    root.add(_buttons(g, pal, str(args.get("buttons", "drei") or "drei"), res["close_hl"]))
    # 4 cell backgrounds (inverse, coloured backgrounds), 5 cursor, 6 rows
    bgs = AnimObject()
    texts = AnimObject()
    sx, sy0, cw, lh = g["sx"], g["sy0"], g["cw"], g["lh"]
    cur_r, cur_c = sc.r, sc.c
    show_cursor = (cursor and sc.cursor_on and res["blink"] and res["close"] <= 0.0
                   and 0 <= cur_r < rows and cur_c < cols)
    for r in range(rows):
        row = sc.lines[r] if r < len(sc.lines) else []
        chars, spans = [], []
        y_top, y_bot = sy0 - r * lh, sy0 - (r + 1) * lh
        run_bg, run_a = None, 0
        for c in range(len(row) + 1):
            cell = row[c] if c < len(row) else None
            bgc = cell[2] if cell else None
            if bgc != run_bg:
                if run_bg is not None:
                    bgs.add(_rect(sx + run_a * cw, y_bot, sx + c * cw, y_top, run_bg))
                run_bg, run_a = bgc, c
        for c, cell in enumerate(row):
            ch, fg, _bg, bold = cell
            if ch == "":                             # second half of a wide character
                continue
            if show_cursor and r == cur_r and c == cur_c and ch != " ":
                fg = pal["bg"]                       # the character under the block cursor
            a = len("".join(chars))
            chars.append(ch)
            if fg is not None or bold:
                rgb = _ansi.hex_rgb(fg) if fg else None
                if spans and spans[-1][1] == a and spans[-1][2] == rgb and spans[-1][3] == bold:
                    spans[-1] = (spans[-1][0], a + len(ch), rgb, bold)
                else:
                    spans.append((a, a + len(ch), rgb, bold))
        line = "".join(chars)
        t = Text(line.rstrip(), position=np.array([sx, sy0 - (r + 0.5) * lh, 0.0]), font_size=g["fs"],
                 color=_ansi.hex_rgb(pal["fg"]), align="left", font="mono", raw=True)
        n = len(t.text)
        t.spans = tuple((a, min(b, n), col, bo) for a, b, col, bo in spans if a < n) or None
        texts.add(t)
    root.add(bgs)
    # the cursor node exists in every frame (same tree); hidden = transparent (the export then skips it)
    cur = _rect(sx + cur_c * cw, sy0 - (cur_r + 1) * lh, sx + (cur_c + 1) * cw, sy0 - cur_r * lh, pal["cursor"],
                1.0 if show_cursor else 0.0)
    root.add(cur)
    root.add(texts)
    if res["close"] > 0.0:
        _fade(root, 1.0 - res["close"])
    return root


# ---------------------------------------------------------------------------------------------------------------
# 6. A small neutral lock (closed / open)
def build_lock(args, style, axes):
    """Model type "Lock": center (data coords), size (height, world units), open, color (body and shackle)."""
    import math
    c = list(args.get("center", [0.0, 0.0, 0.0])) + [0.0, 0.0, 0.0]
    if axes is not None:
        w = np.asarray(axes.coords_to_point(float(c[0]), float(c[1]), 0.0), dtype=float)
        cx, cy = float(w[0]), float(w[1])
    else:
        cx, cy = float(c[0]), float(c[1])
    s = float(args.get("size", 0.4) or 0.4)
    col = style.get("color", (0.45, 0.45, 0.45))
    col = tuple(col) if not isinstance(col, str) else _ansi.hex_rgb(col)
    opened = bool(args.get("open", False))
    bw, bh = 0.78 * s, 0.56 * s
    by0 = cy - s / 2
    body = _shape(_rrect(cx - bw / 2, by0, cx + bw / 2, by0 + bh, 0.12 * s, 0.12 * s), col, 1.0)
    r = 0.24 * s
    lift = 0.14 * s if opened else 0.0           # open: the shackle is lifted, its right leg stands free
    top = cy + s / 2 - r + lift                  # centre of the half circle
    inside = by0 + bh - 0.02 * s                 # a leg ends just inside the body
    pts = [(cx - r, inside), (cx - r, top)]
    for k in range(1, 13):                       # half circle over the top
        a = math.pi - math.pi * k / 12
        pts.append((cx + r * math.cos(a), top + r * math.sin(a)))
    pts.append((cx + r, by0 + bh + 0.12 * s if opened else inside))
    shackle = AnimObject()
    shackle.points = line_points([[x, y, 0.0] for x, y in pts])
    shackle.color = col
    shackle.stroke_width = max(1.5, 0.1 * s / UPP)
    shackle.fill_opacity = 0.0
    hole = Circle(center=np.array([cx, by0 + 0.62 * bh, 0.0]), radius=0.075 * s)
    hole.fill_color = (1.0, 1.0, 1.0)
    hole.fill_opacity = 1.0
    hole.stroke_width = 0.0
    hole.color = hole.fill_color
    stem = _rect(cx - 0.03 * s, by0 + 0.25 * bh, cx + 0.03 * s, by0 + 0.6 * bh, (1.0, 1.0, 1.0))
    obj = AnimObject()
    obj.add(shackle, body, hole, stem)
    obj.color = col
    return obj


BUILDERS = {"Terminal": build_terminal, "Lock": build_lock}
