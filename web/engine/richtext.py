"""Formula-style labels without a TeX engine: parse a label string into RUNS so a painter can draw
subscripts, superscripts, Greek letters and line breaks with plain canvas/SVG text.

Syntax (a small, forgiving subset of LaTeX, usable in EVERY label of the editor):
    U_{GS}  I_D  10^{-16}  x^2  e^{U/U_T}   subscript / superscript (one char or a {...} group), nestable
    \\alpha \\mu \\Omega \\Delta ...          Greek letters
    \\cdot \\times \\pm \\approx \\infty \\rightarrow \\le \\ge \\neq \\sqrt \\deg \\ohm \\prime ...
    \\, \\; \\quad                            thin / normal / wide space
    \\\\ or a real newline                     line break (several lines are stacked, centred on the anchor)
    \\mathrm{...} \\text{...}                 the group as plain text
Unknown macros fall back to their name as text. `\\n` directly followed by letters that are not a
known macro also breaks the line, so "I_D\\nmax" reads as two lines.

parse(text) -> list of lines; each line is a list of (string, level) runs. `level` is a string of
'_' (subscript) and '^' (superscript) steps from the outside in: "" = normal, "_" = subscript,
"^" = superscript, "^_" = subscript inside a superscript (the T in e^{U/U_T}).
layout(level, font_size) -> (size, dy): the font size and the baseline shift (pixels, + = down) of a run.
"""

GREEK = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "vartheta": "ϑ", "iota": "ι", "kappa": "κ", "lambda": "λ",
    "mu": "µ", "nu": "ν", "xi": "ξ", "pi": "π", "rho": "ρ", "sigma": "σ", "tau": "τ", "upsilon": "υ",
    "phi": "φ", "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
    "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ",
    "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω",
}
SYMBOLS = {
    "cdot": "·", "times": "×", "pm": "±", "mp": "∓", "approx": "≈", "infty": "∞", "rightarrow": "→",
    "to": "→", "leftarrow": "←", "Rightarrow": "⇒", "Leftrightarrow": "⇔", "leftrightarrow": "↔",
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "neq": "≠", "ne": "≠", "sqrt": "√", "deg": "°",
    "circ": "°", "ohm": "Ω", "prime": "′", "ldots": "…", "dots": "…", "cdots": "⋯", "propto": "∝",
    "partial": "∂", "nabla": "∇", "sum": "Σ", "int": "∫", "sim": "∼", "simeq": "≃", "equiv": "≡",
    "perp": "⊥", "parallel": "∥", "angle": "∠", "hbar": "ℏ", "ell": "ℓ", "Re": "Re", "Im": "Im",
    "langle": "⟨", "rangle": "⟩", "mid": "|", "vert": "|", "lbrace": "{", "rbrace": "}",
    "%": "%", "&": "&", "#": "#", "_": "_", "^": "^", "{": "{", "}": "}", "$": "$", "backslash": "\\",
    "ast": "∗", "star": "⋆", "bullet": "•", "degree": "°", "micro": "µ", "Ohm": "Ω", "minus": "−",
}
SPACES = {",": " ", ";": " ", ":": " ", " ": " ", "quad": "  ", "qquad": "    ", "!": ""}
PLAIN_GROUPS = {"mathrm", "text", "textrm", "textbf", "mathbf", "mathit", "textit", "operatorname", "mathsf"}

SCRIPT_SCALE = 0.7                  # each sub/superscript step shrinks the font by this factor
SUB_SHIFT = 0.30                    # subscript: baseline down by this fraction of the parent size
SUP_SHIFT = -0.40                   # superscript: baseline up


def layout(level, font_size):
    """(size, dy) of a run at `level` for a base `font_size`; dy > 0 moves the run down."""
    size, dy = float(font_size), 0.0
    for step in level:
        dy += (SUB_SHIFT if step == "_" else SUP_SHIFT) * size
        size *= SCRIPT_SCALE
    return size, dy


def _macro_text(name):
    if name in GREEK:
        return GREEK[name]
    if name in SYMBOLS:
        return SYMBOLS[name]
    if name in SPACES:
        return SPACES[name]
    return None


def _group(s, i):
    """s[i] == '{' -> (inner, index after the matching '}')."""
    depth, j = 0, i
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def _parse_line(s, level, out):
    """Append (text, level) runs of s to out (one line, no newlines inside)."""
    i, n = 0, len(s)
    buf = []

    def flush():
        if buf:
            txt = "".join(buf)
            if out and out[-1][1] == level:
                out[-1] = (out[-1][0] + txt, level)
            else:
                out.append((txt, level))
            buf.clear()

    while i < n:
        ch = s[i]
        if ch in "_^":
            flush()
            lvl = level + ch
            i += 1
            if i < n and s[i] == "{":
                inner, i = _group(s, i)
                _parse_line(inner, lvl, out)
            elif i < n and s[i] == "\\":
                j = i + 1
                while j < n and s[j].isalpha():
                    j += 1
                if j == i + 1:                               # \, \{ ... as a script
                    name, j = (s[i + 1] if i + 1 < n else ""), i + 2
                else:
                    name = s[i + 1:j]
                t = _macro_text(name)
                _parse_line(name if t is None else t, lvl, out)
                i = j
            elif i < n:
                _parse_line(s[i], lvl, out)
                i += 1
            continue
        if ch == "\\":
            j = i + 1
            while j < n and s[j].isalpha():
                j += 1
            if j == i + 1:                                   # \, \; \! \{ \} \_ ...
                sym = s[i + 1] if i + 1 < n else ""
                t = _macro_text(sym)
                buf.append(t if t is not None else sym)
                i += 2
                continue
            name = s[i + 1:j]
            if name in PLAIN_GROUPS and j < n and s[j] == "{":
                inner, j = _group(s, j)
                flush()
                _parse_line(inner, level, out)
                i = j
                continue
            t = _macro_text(name)
            if t is None and name.startswith("n") and len(name) > 1:
                buf.append("\n" + name[1:])                  # "\nmax": a line break, then "max"
            elif t is None:
                buf.append(name)                             # unknown macro -> its name as text
            else:
                buf.append(t)
            i = j
            continue
        if ch in "${}":                                      # math delimiters / stray braces vanish
            i += 1
            continue
        buf.append(ch)
        i += 1
    flush()


def parse(text):
    """Parse a label into lines of (string, level) runs. See the module docstring for the syntax."""
    s = str(text if text is not None else "")
    s = s.replace("\\\\", "\n").replace("\r\n", "\n")
    lines = []
    for raw in s.split("\n"):
        runs = []
        _parse_line(raw, "", runs)
        cur = []                                             # a run may carry "\n" from the "\nmax" form
        for txt, lvl in runs:
            parts = txt.split("\n")
            for k, part in enumerate(parts):
                if k > 0:
                    lines.append(cur)
                    cur = []
                if part:
                    cur.append((part, lvl))
        lines.append(cur)
    return lines


def plain(text):
    """The label as plain text (no sub/sup positioning) - for width estimates and fallbacks."""
    return "\n".join("".join(t for t, _ in line) for line in parse(text))


def is_plain(text):
    """True when the label needs no rich layout (single line, no sub/sup, no macros)."""
    s = str(text if text is not None else "")
    return not any(c in s for c in "_^\\\n${}")
