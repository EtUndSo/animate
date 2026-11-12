"""ANSI colours and attributes (F1 "Bildschirme und Fenster", 12.11.2026): the two terminal palettes and the SGR state
machine, shared by Text (prop `ansi`), the Terminal object (engine/terminal.py) and tools/szenen_lib.py. Pure Python.

Escapes in a label or a terminal stream: the real ESC character or the two characters backslash-e (`\\e[1;32m`); a
literal backslash before an e is written as two backslashes (`\\\\e`). SGR codes (CSI ... m) understood here:
  0 reset · 1 bold · 2 faint · 22 normal intensity · 7 inverse · 27 not inverse · 30-37 / 90-97 foreground
  39 default foreground · 40-47 / 100-107 background · 49 default background
  38;5;n / 48;5;n (256 colours) · 38;2;r;g;b / 48;2;r;g;b (24-bit, e.g. the colours of the figure palette)
Underline, italics, blinking are ignored (no colour change). Other CSI sequences are dropped from a Text (the Terminal
object interprets cursor movement and erasing itself).

The palettes and why they look like this: notizen/f1_terminal_palette.md (keep the table there in step with PALETTES).
"""
import re

ESC = "\x1b"
_ESC_TEXT = re.compile(r"\\([\\e])")


def unescape(s):
    """`\\e` -> ESC, `\\\\` -> one backslash; every other backslash stays as it is (C:\\, grep '\\w')."""
    s = str(s if s is not None else "")
    if "\\" not in s:
        return s
    return _ESC_TEXT.sub(lambda m: "\\" if m.group(1) == "\\" else ESC, s)


def hex_rgb(h):
    h = h.lstrip("#")
    return (int(h[0:2], 16) / 255.0, int(h[2:4], 16) / 255.0, int(h[4:6], 16) / 255.0)


# 16 colours 0-7 normal, 8-15 bright. "dunkel": GNOME-terminal palette, red/yellow/blue/magenta/grey brightened to at
# least 4.5:1 against the background; "hell": the same hues darkened for a white page. Table + reasons:
# notizen/f1_terminal_palette.md.
PALETTES = {
    "dunkel": {
        "bg": "#1e1e1e", "fg": "#d0cfcc", "cursor": "#d0cfcc",
        "ansi": ["#171421", "#ef5350", "#26a269", "#c28a52", "#4a8fe8", "#c061cb", "#2aa1b3", "#d0cfcc",
                 "#8a8990", "#f66151", "#33da7a", "#e9ad0c", "#5ea1f0", "#d27bdc", "#33c7de", "#ffffff"],
        "bold_bright": True,                     # bold 30-37 in the bright colour (prompt, ls --color as on screen)
        "bar": "#303030", "bar_text": "#f2f2f2", "sep": None, "border": "#0f0f0f",
        "button": "#474747", "icon": "#f0f0f0", "close": "#c01c28", "close_icon": "#ffffff",
        "shadow": "#000000",
    },
    "hell": {
        "bg": "#ffffff", "fg": "#1e1e1e", "cursor": "#1e1e1e",
        "ansi": ["#1e1e1e", "#c01c28", "#1b7f45", "#8a5a1f", "#1d4fa8", "#8b3aa0", "#16768a", "#5e5c64",
                 "#77767b", "#c01c28", "#1b7f45", "#8a5a1f", "#1d4fa8", "#8b3aa0", "#16768a", "#1e1e1e"],
        "bold_bright": False,
        "bar": "#ebebeb", "bar_text": "#2e2e2e", "sep": "#d6d6d6", "border": "#c4c4c4",
        "button": "#d6d6d6", "icon": "#2e2e2e", "close": "#c01c28", "close_icon": "#ffffff",
        "shadow": "#000000",
    },
}
THEMES = tuple(PALETTES)


def palette(theme):
    return PALETTES.get(str(theme or "dunkel"), PALETTES["dunkel"])


def color256(n):
    """Hex of xterm colour n (16-231: 6x6x6 cube, 232-255: grey ramp); 0-15 come from the palette."""
    n = max(0, min(255, int(n)))
    if n >= 232:
        v = 8 + (n - 232) * 10
        return "#%02x%02x%02x" % (v, v, v)
    n -= 16
    steps = (0, 95, 135, 175, 215, 255)
    return "#%02x%02x%02x" % (steps[n // 36], steps[(n // 6) % 6], steps[n % 6])


class Attr:
    """Current SGR state. fg/bg: None (default), ("i", 0..255) or ("rgb", "#rrggbb")."""
    __slots__ = ("fg", "bg", "bold", "faint", "inverse")

    def __init__(self):
        self.reset()

    def reset(self):
        self.fg = self.bg = None
        self.bold = self.faint = self.inverse = False

    def copy(self):
        a = Attr()
        a.fg, a.bg, a.bold, a.faint, a.inverse = self.fg, self.bg, self.bold, self.faint, self.inverse
        return a

    def sgr(self, params):
        """Apply the parameters of one CSI ... m."""
        ps = [p for p in str(params).replace(":", ";").split(";")]
        nums = []
        for p in ps:
            try:
                nums.append(int(p) if p != "" else 0)
            except ValueError:
                nums.append(-1)
        if not nums:
            nums = [0]
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == 0:
                self.reset()
            elif n == 1:
                self.bold = True
            elif n == 2:
                self.faint = True
            elif n == 22:
                self.bold = self.faint = False
            elif n == 7:
                self.inverse = True
            elif n == 27:
                self.inverse = False
            elif 30 <= n <= 37:
                self.fg = ("i", n - 30)
            elif 90 <= n <= 97:
                self.fg = ("i", n - 90 + 8)
            elif n == 39:
                self.fg = None
            elif 40 <= n <= 47:
                self.bg = ("i", n - 40)
            elif 100 <= n <= 107:
                self.bg = ("i", n - 100 + 8)
            elif n == 49:
                self.bg = None
            elif n in (38, 48):
                c = None
                if i + 2 < len(nums) and nums[i + 1] == 5:
                    c = ("i", max(0, min(255, nums[i + 2])))
                    i += 2
                elif i + 4 < len(nums) and nums[i + 1] == 2:
                    r, g, b = (max(0, min(255, v)) for v in nums[i + 2:i + 5])
                    c = ("rgb", "#%02x%02x%02x" % (r, g, b))
                    i += 4
                if c is not None:
                    if n == 38:
                        self.fg = c
                    else:
                        self.bg = c
            i += 1


def _col(c, pal, bold=False):
    if c is None:
        return None
    if c[0] == "rgb":
        return c[1]
    n = c[1]
    if n < 16:
        if bold and pal.get("bold_bright") and n < 8:
            n += 8
        return pal["ansi"][n]
    return color256(n)


def _mix(a, b, w):
    ra, rb = hex_rgb(a), hex_rgb(b)
    return "#%02x%02x%02x" % tuple(int(round((x + (y - x) * w) * 255)) for x, y in zip(ra, rb))


def resolve(attr, pal):
    """(fg hex or None = default, bg hex or None = none, bold) of an Attr in a palette; inverse swaps the colours (a
    default colour becomes the palette's foreground or background), faint mixes the foreground 40 % toward the
    background."""
    fg = _col(attr.fg, pal, attr.bold)
    bg = _col(attr.bg, pal)
    if attr.faint:
        fg = _mix(fg or pal["fg"], pal["bg"], 0.4)
    if attr.inverse:
        fg, bg = (bg or pal["bg"]), (fg or pal["fg"])
    return fg, bg, bool(attr.bold)


# ---------------------------------------------------------------------------------------------------------------
# A label with ANSI codes (Text with ansi=True): the plain text and its coloured sections.
_CSI = re.compile(r"\x1b\[([0-?]*)([ -/]*)([@-~])|\x1b[^\[]?")


def parse_sgr(text, theme="hell"):
    """(plain text, spans) of a label with ANSI codes. spans = ((start, end, rgb or None, bold), ...) over the plain
    text (end exclusive); rgb None = the label's own colour. Only SGR changes the look; every other escape sequence
    vanishes. Background colours and inverse need a cell background and are left out (Terminal draws them)."""
    s = unescape(text)
    pal = palette(theme)
    out, spans = [], []
    attr = Attr()
    i = 0
    for m in _CSI.finditer(s):
        if m.start() > i:
            _add_run(out, spans, s[i:m.start()], attr, pal)
        if m.group(3) == "m" and not m.group(2):
            attr.sgr(m.group(1))
        i = m.end()
    if i < len(s):
        _add_run(out, spans, s[i:], attr, pal)
    return "".join(out), tuple(spans)


def _add_run(out, spans, txt, attr, pal):
    a = sum(len(x) for x in out)
    out.append(txt)
    fg = _col(attr.fg, pal, attr.bold)
    if attr.faint:
        fg = _mix(fg or pal["fg"], pal["bg"], 0.4)
    if fg is None and not attr.bold:
        return
    rgb = hex_rgb(fg) if fg else None
    if spans and spans[-1][1] == a and spans[-1][2] == rgb and spans[-1][3] == bool(attr.bold):
        spans[-1] = (spans[-1][0], a + len(txt), rgb, bool(attr.bold))
    else:
        spans.append((a, a + len(txt), rgb, bool(attr.bold)))


def strip(text):
    """The label without escape sequences (plain text)."""
    return parse_sgr(text)[0]


def sgr_rgb(hexcolor, bold=False):
    """An SGR prefix for a figure colour (24-bit), e.g. sgr_rgb("#eb6834") -> ESC[38;2;235;104;52m."""
    r, g, b = (int(round(v * 255)) for v in hex_rgb(hexcolor))
    return "%s[%s38;2;%d;%d;%dm" % (ESC, "1;" if bold else "", r, g, b)


RESET = ESC + "[0m"
