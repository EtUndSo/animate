"""Animierte Artikelbilder: die Zeitachse einer Editor-Szene als bewegtes SVG (Datenblock + Spieler der Website).

Aufruf über das Stapel-Werkzeug (vom Repo-Root):
    python tools/export_szenen.py --animiert prog/k3rquadrate        schreibt zusätzlich <szene>.anim.svg
Ohne Zeitachse (keine Animationen, keine ablaufende Operation) entsteht keine animierte Datei, die Artikelseite
zeigt dann wie bisher das statische Bild.

Verfahren (allgemein, gilt für jede Animationsart der Engine, auch für künftige):
1. Die Szene wird gebaut wie beim Abspielen im Editor (ModelScene.animating = True, build_timeline) und mit fester
   Bildrate abgetastet: seek(t) für t = 0, Δt, 2Δt, …, Dauer. Ein Aufzeichnungs-Painter (dieselben drei Methoden wie
   der SVG-Painter) merkt sich je Bild jeden Zeichenaufruf, zugeordnet dem gezeichneten Objekt (Blatt im Objektbaum).
2. Die Datei ist das Endbild der Szene, Element für Element so formatiert wie der statische Export (engine/svg_painter),
   plus ein Datenblock <metadata class="szenen-animation"> mit Spuren je veränderlichem Element. Ohne Skript (in
   <img>, beim Öffnen der Datei, bei „Bewegung reduzieren“) zeigt sie also genau das Endbild.
3. Jede Eigenschaft, die sich ändert, wird eine Spur aus Schlüsselbildern (Bildnummer, Wert); Bilder, die sich aus den
   Nachbarn linear ergeben, fallen weg (Toleranz TOL_PX in Szenenpixeln). Spuren:
     v   sichtbar (0/1, Stufe)              fo, so  Deckkraft Füllung/Strich (bei Text: Deckkraft)
     fc, sc  Farbe Füllung/Strich [r,g,b]   sw  Strichbreite
     m   Transformation matrix(a b c d e f) des Endbilds (Verschieben, Drehen, Skalieren; Text: Lage und Größe)
     p   Teilstück [Anfang, Länge] in 1/1000 der Pfadlänge (Zeichnen, Create/Write einer Linie: Strichmuster)
     d   Pfad (Stufe), wenn nichts davon passt (Umformen, Füllung wächst, ...)
     h   Inhalt eines Texts (Stufe), wenn sich der Text selbst ändert (Zähler)
   Lineare Spuren werden zwischen den Schlüsselbildern interpoliert, Stufen-Spuren gelten bis zum nächsten.
4. Sprungmarken: Beginn jedes Zeitachsen-Abschnitts (gleicher Schritt = ein Abschnitt), nahe Marken zusammengefasst.

Der Spieler steht in build_wissen.py (WISSEN_JS, Block „Animierte Abbildungen“).
"""
import json
import math
import sys

import numpy as np

from engine import export as _export
from engine.renderer import paint_scene
from engine.scene_model import ModelScene
from engine.svg_painter import SvgPainter, SVG_FONT, _hex, _num

FPS = 30                  # Abtastrate (Bilder je Sekunde); der Spieler interpoliert dazwischen
TOL_PX = 0.2              # erlaubte Abweichung der Geometrie in Szenenpixeln (= 0,11 px im Artikel)
TOL_OP = 0.01             # Deckkraft
TOL_COL = 2.0             # Farbe (0..255 je Kanal)
MIN_SCALE = 0.05          # kleinere Maßstäbe (fast ein Punkt) als Pfad statt als Transformation
MAX_SCALE = 8.0           # stärkere Vergrößerung des Endbild-Pfads (z. B. eine Glyphe, die zu einem Punkt schrumpft)
#                           ebenfalls als Pfad: Die Rundung der Endbild-Koordinaten würde sonst mitvergrößert
MAX_MARKS = 24
MARK_GAP = 0.35           # Sekunden: nähere Abschnittsanfänge zählen als eine Sprungmarke
BUDGET = 900_000          # Bytes für den Datenblock; darüber werden Pfad-Spuren mit halber Rate abgetastet
D_STEP = 3                # Pfad-Spuren "d" (stufenweise, je Bild ein ganzer Pfad): jedes 3. Bild = 10 Bilder/s
VERSION = 1


def _rgb(c):
    if c is None:
        return (0.0, 0.0, 0.0)
    return tuple(float(x) for x in list(c)[:3])


def _rgb255(c):
    return [int(round(max(0.0, min(1.0, x)) * 255)) for x in c]


# ---------------------------------------------------------------------------- 1. Aufzeichnen
class _Recorder:
    """Painter, der nichts zeichnet, sondern je Bild die Zeichenaufrufe mit ihrem Objekt festhält. Das Objekt kommt
    aus dem Aufrufer (engine/renderer: _paint_leaf/_paint_center haben `obj`, _paint_3d hat `o`); ein Objekt mit zwei
    Aufrufen (Pfad + Mittelpunktmarke) gibt zwei Elemente. Alle gesehenen Objekte bleiben referenziert, damit keine
    id() doppelt vergeben wird."""

    def __init__(self):
        self.keep = []
        self._seen = set()
        self.reset()

    def reset(self):
        self.items, self._n = [], {}

    def background(self, color):
        pass

    def _key(self):
        f = sys._getframe(2)
        obj = f.f_locals.get("o" if f.f_code.co_name == "_paint_3d" else "obj")   # _paint_3d: `obj` is a loop leftover
        if obj is None:
            raise RuntimeError("szenen_animation: Zeichenaufruf ohne Objekt (engine/renderer geändert?)")
        k = id(obj)
        n = self._n.get(k, 0)
        self._n[k] = n + 1
        if k not in self._seen:
            self._seen.add(k)
            self.keep.append(obj)
        return (k, n)

    def draw_path(self, pts, fill_color, fill_opacity, stroke_color, stroke_width, stroke_opacity, contours=None, dash=None):
        a = np.asarray(pts, dtype=float).reshape(-1, 2)
        self.items.append((self._key(), ("p", a, _rgb(fill_color), float(fill_opacity), _rgb(stroke_color),
                                         float(stroke_width), float(stroke_opacity),
                                         tuple(int(c) for c in contours) if contours else None,
                                         tuple(float(v) for v in dash) if dash else None)))

    def draw_text(self, text, px, py, font_size, color, opacity, align="center", font=None, raw=False):
        self.items.append((self._key(), ("t", str(text), float(px), float(py), float(font_size), _rgb(color),
                                         float(opacity), align, _text_style(font, raw))))


def _text_style(font, raw):
    """Die Zusatz-Schlüsselwörter eines Texts für SvgPainter.draw_text (wie engine/text.text_style)."""
    st = {}
    if font == "mono":
        st["font"] = "mono"
    if raw:
        st["raw"] = True
    return tuple(sorted(st.items()))


def _frame(sc, rec, t, axes_on_top):
    sc.seek(t)
    rec.reset()
    paint_scene(rec, sc.objectList, sc.camera, background=None, axes_on_top=axes_on_top)
    return list(rec.items)


def _invisible(v):
    if v[0] == "t":
        return v[6] <= 0 or not v[1].strip()
    return (v[3] <= 0) and (v[5] <= 0 or v[6] <= 0)


def _merge_order(seqs):
    """Eine gemeinsame Zeichenreihenfolge aus den Reihenfolgen aller Bilder (das Endbild zuerst): Ein Element, das im
    Endbild fehlt, kommt hinter seinen Vorgänger im Bild, in dem es vorkommt."""
    order, pos = [], {}
    for seq in seqs:
        prev = None
        for k in seq:
            if k not in pos:
                i = order.index(prev) + 1 if prev is not None else 0
                order.insert(i, k)
                pos = {x: j for j, x in enumerate(order)}
            prev = k
    return order


# ---------------------------------------------------------------------------- 2. Geometrie
def _cubic_samples(pts, n=12):
    """Polylinie durch eine Bézier-Kette (N = 3k+1 Punkte, n Stützstellen je Segment) und ihre Bogenlängen."""
    k = (len(pts) - 1) // 3
    if k <= 0:
        return pts[:1].copy(), np.zeros(1)
    P = pts[:3 * k + 1]
    p0, p1, p2, p3 = P[0:-1:3], P[1::3], P[2::3], P[3::3]
    t = np.linspace(0.0, 1.0, n + 1)[1:][:, None, None]
    u = 1.0 - t
    seg = (u ** 3) * p0 + 3 * (u ** 2) * t * p1 + 3 * u * (t ** 2) * p2 + (t ** 3) * p3      # (n, k, 2)
    poly = np.vstack([P[:1], seg.transpose(1, 0, 2).reshape(-1, 2)])
    d = np.sqrt((np.diff(poly, axis=0) ** 2).sum(axis=1))
    return poly, np.concatenate([[0.0], np.cumsum(d)])


def _at(poly, cum, s):
    """Punkt der Polylinie bei Bogenlänge s."""
    s = min(max(s, 0.0), cum[-1])
    i = int(np.searchsorted(cum, s, side="right")) - 1
    i = min(max(i, 0), len(poly) - 2)
    L = cum[i + 1] - cum[i]
    f = (s - cum[i]) / L if L > 1e-12 else 0.0
    return poly[i] + (poly[i + 1] - poly[i]) * f


def _partial_of(base_poly, base_cum, pts, tol):
    """(Anfang, Länge) in Bogenlänge, wenn der Pfad pts ein zusammenhängendes Teilstück des Endpfads ist, sonst None."""
    poly, cum = _cubic_samples(pts)
    L = cum[-1]
    LB = base_cum[-1]
    if LB <= 1e-9 or L > LB + tol:
        return None
    p0 = poly[0]
    a_, b_ = base_poly[:-1], base_poly[1:]
    ab = b_ - a_
    den = (ab ** 2).sum(axis=1)
    den[den < 1e-12] = 1e-12
    tt = np.clip(((p0 - a_) * ab).sum(axis=1) / den, 0.0, 1.0)
    proj = a_ + ab * tt[:, None]
    dist = np.sqrt(((proj - p0) ** 2).sum(axis=1))
    cand = np.nonzero(dist <= tol)[0]
    checks = [0.25, 0.5, 0.75, 1.0]
    for i in cand[:12]:
        s0 = base_cum[i] + tt[i] * math.sqrt(den[i])
        if s0 + L > LB + tol:
            continue
        if all(np.linalg.norm(_at(base_poly, base_cum, s0 + q * L) - _at(poly, cum, q * L)) <= tol for q in checks):
            return s0, L
    return None


def _affine(base, pts):
    """Matrix [a, b, c, d, e, f] (SVG: x' = a x + c y + e, y' = b x + d y + f) mit pts ≈ M·base, sonst None."""
    A = np.hstack([base, np.ones((len(base), 1))])
    sol, *_ = np.linalg.lstsq(A, pts, rcond=None)                 # (3, 2): [[a, b], [c, d], [e, f]]
    if np.abs(A @ sol - pts).max() > TOL_PX:
        return None
    return [sol[0, 0], sol[0, 1], sol[1, 0], sol[1, 1], sol[2, 0], sol[2, 1]]


def _det_scale(m):
    return math.sqrt(abs(m[0] * m[3] - m[1] * m[2]))


_IDENT = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]


def _d(pts, contours=None, nd=1):
    def f(v):
        s = ("%.*f" % (nd, v)).rstrip("0").rstrip(".")
        return "0" if s in ("-0", "") else s

    def one(p):
        out = ["M%s %s" % (f(p[0][0]), f(p[0][1]))]
        for i in range(1, len(p) - 2, 3):
            out.append("C%s %s %s %s %s %s" % (f(p[i][0]), f(p[i][1]), f(p[i + 1][0]), f(p[i + 1][1]), f(p[i + 2][0]), f(p[i + 2][1])))
        return "".join(out)
    if contours:
        out, off = [], 0
        for n in contours:
            seg = pts[off:off + n]                     # a partly drawn glyph (Write) has fewer points than its contours
            if len(seg):
                out.append(one(seg))
            off += n
        return "".join(out)
    return one(pts) if len(pts) else ""


# ---------------------------------------------------------------------------- 3. Spuren
def _reduce(frames, vals, err, step=False):
    """Schlüsselbilder: bei Stufen-Spuren jeder Wechsel, sonst so wenige Bilder, dass die lineare Interpolation jedes
    Zwischenbild innerhalb der Toleranz trifft (err(interpoliert, echt) <= 1). Ergebnis: flache Liste [k, v, k, v, ...]."""
    n = len(vals)
    if step:
        out, last = [], object()
        for k, v in zip(frames, vals):
            if v != last:
                out += [k, v]
                last = v
        return out
    # Läufe gleicher Werte auf Anfang und Ende kürzen: Der Fehler einer linearen Interpolation ist auf einem Lauf
    # konstanter Werte konvex, sein Maximum liegt an den Enden; die inneren Bilder brauchen keine Prüfung.
    idx = [i for i in range(n) if i in (0, n - 1) or not (vals[i] == vals[i - 1] and vals[i] == vals[i + 1])]
    if len(idx) < n:
        frames, vals, n = [frames[i] for i in idx], [vals[i] for i in idx], len(idx)
    keep = [0]
    i = 0
    while i < n - 1:
        j = i + 1
        while j + 1 < n:
            jj = j + 1
            ok = True
            for m in range(i + 1, jj):
                w = (frames[m] - frames[i]) / float(frames[jj] - frames[i])
                if err(_lerp(vals[i], vals[jj], w), vals[m]) > 1.0:
                    ok = False
                    break
            if not ok:
                break
            j = jj
        keep.append(j)
        i = j
    out = []
    for i in keep:
        out += [frames[i], vals[i]]
    return out


def _reduce_runs(frames, vals, err):
    """Wie _reduce, aber None (= Endbild) trennt Abschnitte: Innerhalb eines Abschnitts linear ausgedünnt, an den
    Grenzen stehen beide Seiten als Schlüsselbild (der Spieler interpoliert nur zwischen zwei Zahlenwerten)."""
    out, i, n = [], 0, len(vals)
    while i < n:
        j = i
        if vals[i] is None:
            while j + 1 < n and vals[j + 1] is None:
                j += 1
            out += [frames[i], None]
        else:
            while j + 1 < n and vals[j + 1] is not None:
                j += 1
            out += _reduce(frames[i:j + 1], vals[i:j + 1], err)
        i = j + 1
    return out


def _lerp(a, b, w):
    if isinstance(a, list):
        return [x + (y - x) * w for x, y in zip(a, b)]
    return a + (b - a) * w


def _constant(vals, err):
    return all(err(v, vals[-1]) <= 1.0 for v in vals)


def _fill(vals):
    """Fehlende Werte (Element unsichtbar) mit dem nächsten bekannten Wert füllen: Sie dürfen nichts kosten."""
    out = list(vals)
    last = None
    for i, v in enumerate(out):
        if v is None:
            out[i] = last
        else:
            last = v
    nxt = None
    for i in range(len(out) - 1, -1, -1):
        if out[i] is None:
            out[i] = nxt
        else:
            nxt = out[i]
    return out


def _round(v, nd):
    if v is None:
        return None
    if isinstance(v, list):
        return [_round(x, nd) for x in v]
    r = round(float(v), nd)
    return int(r) if r == int(r) else r


class _Element:
    """Ein Element des SVG (ein Zeichenaufruf eines Objekts) über alle Bilder."""

    def __init__(self, key, kind):
        self.key, self.kind = key, kind
        self.vals = []            # je Bild der Eintrag des Recorders oder None

    def base(self):
        for v in reversed(self.vals):
            if v is not None:
                return v
        return None


def _path_tracks(el, frames, base):
    """Spuren eines Pfad-Elements relativ zum Endbild `base`."""
    _, B, bfc, bfo, bsc, bsw, bso, bcont, bdash = base
    tr, extra = {}, {}
    n = len(el.vals)
    vis = [0 if v is None else 1 for v in el.vals]
    can_partial = (bcont is None and bdash is None and len(B) >= 4)
    bpoly = bcum = None
    corners = None
    if len(B):
        lo, hi = B.min(axis=0), B.max(axis=0)
        corners = np.array([[lo[0], lo[1]], [hi[0], lo[1]], [lo[0], hi[1]], [hi[0], hi[1]], (lo + hi) / 2])
    M, P, D, FO, SO, SW, FC, SC = ([None] * n for _ in range(8))
    prev = None
    for i, v in enumerate(el.vals):
        if v is None:
            continue
        _, pts, fc, fo, sc, sw, so, cont, dash = v
        if (prev is not None and prev[0].shape == pts.shape and prev[1] == (cont, dash, fo <= 0)
                and np.array_equal(prev[0], pts)):            # Geometrie wie im Bild davor
            M[i], P[i], D[i] = prev[2]
        else:
            m = p = d = None
            if pts.shape == B.shape and cont == bcont and np.abs(pts - B).max() <= 0.01:
                m = None
            else:
                aff = _affine(B, pts) if (pts.shape == B.shape and cont == bcont) else None
                if (aff is not None and MIN_SCALE <= _det_scale(aff) <= MAX_SCALE
                        and (bdash is None or abs(_det_scale(aff) - 1) < 0.01)):
                    m = aff
                else:
                    if can_partial and cont is None and dash is None and fo <= 0 and bfo <= 0:
                        if bpoly is None:
                            bpoly, bcum = _cubic_samples(B)
                        part = _partial_of(bpoly, bcum, pts, TOL_PX) if len(pts) >= 4 else None
                        if part is not None:
                            LB = bcum[-1]
                            p = [part[0] / LB * 1000.0, part[1] / LB * 1000.0]
                    if p is None:
                        d = (pts, cont)
            M[i], P[i], D[i] = m, p, d
        prev = (pts, (cont, dash, fo <= 0), (M[i], P[i], D[i]))
        FO[i], SO[i] = fo, so
        FC[i], SC[i] = fc, sc
        scale = _det_scale(M[i]) if M[i] is not None else 1.0
        SW[i] = sw / scale if scale > 0 else sw                  # SVG skaliert den Strich mit, die Engine nicht
    # sichtbar
    if any(x == 0 for x in vis):
        tr["v"] = _reduce(frames, vis, None, step=True)
    # Geometrie: in einem sichtbaren Bild gilt genau eine Form (Matrix, Teilstück oder Pfad), die anderen sind neutral;
    # unsichtbare Bilder übernehmen den Nachbarwert (kosten keine Schlüsselbilder)
    shown = [v is not None for v in el.vals]
    if any(x is not None for x in M):
        mv = _fill([(x if x is not None else _IDENT) if shown[i] else None for i, x in enumerate(M)])

        def errm(a, b):
            A = np.array([[a[0], a[2]], [a[1], a[3]]]); Bm = np.array([[b[0], b[2]], [b[1], b[3]]])
            pa = corners @ A.T + [a[4], a[5]]
            pb = corners @ Bm.T + [b[4], b[5]]
            return float(np.abs(pa - pb).max()) / TOL_PX
        vals = [[round(x[0], 4), round(x[1], 4), round(x[2], 4), round(x[3], 4), round(x[4], 2), round(x[5], 2)] for x in mv]
        tr["m"] = _round(_reduce(frames, vals, errm), 4)
    if any(x is not None for x in P):
        pv = _fill([(x if x is not None else [0.0, 1000.0]) if shown[i] else None for i, x in enumerate(P)])
        LB = bcum[-1] if bcum is not None else 1.0
        errp = lambda a, b: max(abs(a[0] - b[0]), abs(a[1] - b[1])) * LB / 1000.0 / TOL_PX
        tr["p"] = _round(_reduce(frames, [[round(x[0], 1), round(x[1], 1)] for x in pv], errp), 1)
        extra["pathLength"] = "1000"
    if any(x is not None for x in D):
        dv, last = [], None
        for i, x in enumerate(D):
            last = x if shown[i] else last                     # unsichtbar: Pfad bleibt, wie er war
            dv.append(last)
        formen = {(len(x[0]), x[1]) for x in dv if x is not None}
        if len(formen) == 1:
            # Alle Pfad-Bilder haben dieselbe Punktzahl (Umformen: Punkte wandern): Zahlenspur "q", linear interpoliert
            # wie m; None = Pfad des Endbilds. Der Spieler baut den Pfad aus den Zahlen und den Konturlängen "qc".
            npts, cont = next(iter(formen))
            tr["qc"] = list(cont) if cont else [npts]
            qv = [None if x is None else [round(float(c), 1) for c in x[0].reshape(-1)] for x in dv]
            tr["q"] = _round(_reduce_runs(frames, qv, lambda a, b: max(abs(x - y) for x, y in zip(a, b)) / TOL_PX), 1)
        else:
            # Pfade ohne gemeinsame Punktzahl (Zeichnen einer Füllung, Schreiben einer Formel) gelten stufenweise; jedes
            # Bild wäre ein ganzer Pfad. Mit D_STEP Bildern Abstand (10 je Sekunde) bleibt die Datei klein, Anfang und
            # Ende eines Abschnitts (Wechsel zu/von None) bleiben genau.
            dv = [x if (x is None or i % D_STEP == 0 or dv[i - i % D_STEP] is None) else dv[i - i % D_STEP]
                  for i, x in enumerate(dv)]
            tr["d"] = _reduce(frames, [None if x is None else _d(x[0], x[1]) for x in dv], None, step=True)
    # Stil
    def num_track(name, vals, base_v, tol, nd):
        vv = _fill(vals)
        if _constant(vv, lambda a, b: abs(a - b) / tol) and abs(vv[-1] - base_v) <= tol:
            return
        tr[name] = _round(_reduce(frames, [round(x, nd) for x in vv], lambda a, b: abs(a - b) / tol), nd)

    def col_track(name, vals, base_v, need):
        vv = [_rgb255(x) for x in _fill(vals)]
        b = _rgb255(base_v)
        e = lambda a, c: max(abs(x - y) for x, y in zip(a, c)) / TOL_COL
        if _constant(vv, e) and e(vv[-1], b) <= 1.0 and not need:
            return
        tr[name] = _reduce(frames, vv, e)
    # Nur was je zu sehen ist: Ein Pfad ohne Strich (Glyphe) bekommt keine Strich-Spuren, sonst setzte der Spieler eine
    # Strichfarbe und SVG zeichnete mit der Standardbreite 1 (Glyphen wirkten fett).
    fill_ever = any(x is not None and x > 0 for x in FO)
    stroke_ever = any(x is not None and x > 0 for x in SW) and any(x is not None and x > 0 for x in SO)
    if fill_ever:
        num_track("fo", FO, bfo, TOL_OP, 3)
        col_track("fc", FC, bfc, need=("fo" in tr and bfo <= 0))     # Endbild ohne Füllung: Farbe muss mit
    if stroke_ever:
        num_track("so", SO, bso, TOL_OP, 3)
        num_track("sw", SW, bsw, 0.05, 2)
        col_track("sc", SC, bsc, need=bsw <= 0 or bso <= 0)
    return tr, extra


def _text_markup(text, px, py, fs, color, op, align, style=()):
    sp = SvgPainter(10, 10, font_family=SVG_FONT)
    sp.draw_text(text, px, py, fs, color, op, align, **dict(style))
    return sp.parts


def _text_tracks(el, frames, base):
    _, btext, bx, by, bfs, bcol, bop, balign, bstyle = base
    tr = {}
    n = len(el.vals)
    vis = [0 if v is None else 1 for v in el.vals]
    if any(x == 0 for x in vis):
        tr["v"] = _reduce(frames, vis, None, step=True)
    M, H, FO, FC = ([None] * n for _ in range(4))
    for i, v in enumerate(el.vals):
        if v is None:
            continue
        _, text, px, py, fs, col, op, align, style = v
        s = fs / bfs if bfs > 0 else 1.0
        M[i] = [s, 0.0, 0.0, s, px - s * bx, py - s * by]
        if text != btext or align != balign or style != bstyle:
            H[i] = "".join(_text_markup(text, bx, by, bfs, bcol, bop, align, style))
        FO[i], FC[i] = op, col
    mv = _fill(M)
    if any(max(abs(a - b) for a, b in zip(x, _IDENT)) > 1e-3 for x in mv):
        def errm(a, b):
            return max(abs(a[0] - b[0]) * bfs, abs(a[4] - b[4]), abs(a[5] - b[5])) / TOL_PX
        tr["m"] = _round(_reduce(frames, [[round(x[0], 4), 0, 0, round(x[3], 4), round(x[4], 2), round(x[5], 2)] for x in mv], errm), 4)
    if any(x is not None for x in H):
        tr["h"] = _reduce(frames, H, None, step=True)
    fo = _fill(FO)
    if not (_constant(fo, lambda a, b: abs(a - b) / TOL_OP) and abs(fo[-1] - bop) <= TOL_OP):
        tr["fo"] = _round(_reduce(frames, [round(x, 3) for x in fo], lambda a, b: abs(a - b) / TOL_OP), 3)
    fc = [_rgb255(x) for x in _fill(FC)]
    e = lambda a, c: max(abs(x - y) for x, y in zip(a, c)) / TOL_COL
    if not (_constant(fc, e) and e(fc[-1], _rgb255(bcol)) <= 1.0):
        tr["fc"] = _reduce(frames, fc, e)
    return tr


def _marks(timeline, dur):
    """Sprungmarken: Abschnitte mit "mark" (eine Operation markiert so ihre Rechenschritte), sonst jeder Abschnitt."""
    t, marks = 0.0, []
    nur = any(seg.get("mark") for seg in timeline)
    for seg in timeline:
        if seg["dur"] > 0 and seg["anims"] and (seg.get("mark") or not nur):
            for m in [t] + [t + x for x in seg.get("marks_in", [])]:      # marks_in: Zeilen einer Formel
                if 0.0 < m < dur - 1e-6 and (not marks or m - marks[-1] >= MARK_GAP):
                    marks.append(round(m, 3))
        t += seg["dur"]
    if len(marks) > MAX_MARKS:                            # gleichmäßig ausdünnen
        step = len(marks) / float(MAX_MARKS)
        marks = [marks[int(i * step)] for i in range(MAX_MARKS)]
    return marks


# ---------------------------------------------------------------------------- 4. Datei
def build(model, view, size, background, axes_on_top, fps=FPS):
    """Das animierte SVG einer Szene. model = Engine-Modell (export_szenen.python_model, mit Formeln), view/size = Zuschnitt
    und Anzeigegröße des statischen Bilds. Ergebnis (svg, info) oder (None, Grund)."""
    sc = ModelScene(json.loads(json.dumps(model)))
    sc.animating = True
    sc.build_timeline()
    if not sc.timeline or sc.duration <= 1e-3:
        return None, "keine Zeitachse"
    dur = float(sc.duration)
    N = max(1, int(math.ceil(dur * fps - 1e-9)))
    times = [dur * k / N for k in range(N + 1)]
    rec = _Recorder()
    frames_items = [_frame(sc, rec, t, axes_on_top) for t in times]
    end = frames_items[-1]
    order = _merge_order([[k for k, _ in end]] + [[k for k, _ in fr] for fr in frames_items[:-1]])
    els = {k: _Element(k, None) for k in order}
    for fr in frames_items:
        d = dict(fr)
        for k in order:
            els[k].vals.append(d.get(k))
    # Ein Bild, in dem ein Element ganz durchsichtig ist (ausgeblendet, noch nicht eingeblendet), zählt als „nicht
    # gezeichnet“: Im Endbild fehlt es dann wie im statischen Export, der solche Hilfsobjekte gar nicht erst baut.
    # Elemente, die in jedem Bild unsichtbar sind, bleiben unverändert (der statische Export zeichnet sie auch).
    for el in els.values():
        unsichtbar = [v is None or _invisible(v) for v in el.vals]
        if not all(unsichtbar):
            el.vals = [None if u else v for v, u in zip(el.vals, unsichtbar)]
    warn = []
    # 3D: Reihenfolge ändert sich mit der Tiefe?
    endpos = {k: i for i, (k, _) in enumerate(end)}
    for fr in frames_items[:-1]:
        seq = [endpos[k] for k, _ in fr if k in endpos]
        if any(b < a for a, b in zip(seq, seq[1:])):
            warn.append("Zeichenreihenfolge ändert sich während der Animation (3D-Tiefe), die Datei behält die des Endbilds")
            break
    frames = list(range(N + 1))
    budget_fps = fps
    for attempt in range(3):
        parts, data, n_anim, plain = [], [], 0, []
        sp = SvgPainter(1920, 1080, font_family=SVG_FONT)
        for k in order:
            el = els[k]
            b = el.base()
            if b is None:
                continue
            if attempt and b[0] == "p":                   # zu groß: Pfad-Spuren mit geringerer Rate
                step = 2 ** attempt
                el_vals = [el.vals[min(len(el.vals) - 1, (i // step) * step)] for i in range(len(el.vals))]
                el2 = _Element(k, None); el2.vals = el_vals
            else:
                el2 = el
            if b[0] == "p":
                tr, extra = _path_tracks(el2, frames, b)
                n0 = len(sp.parts)
                sp.draw_path(b[1].tolist(), b[2], b[3], b[4], b[5], b[6], list(b[7]) if b[7] else None, list(b[8]) if b[8] else None)
                svg_parts = sp.parts[n0:]
            else:
                tr, extra = _text_tracks(el2, frames, b), {}
                n0 = len(sp.parts)
                sp.draw_text(b[1], b[2], b[3], b[4], b[5], b[6], b[7], **dict(b[8]))
                svg_parts = sp.parts[n0:]
            del sp.parts[n0:]
            hidden = el.vals[-1] is None
            if not hidden:
                plain.extend(svg_parts)                    # das Endbild ohne Spuren (Vergleich mit dem statischen Bild)
            if tr:
                attrs = ' data-a="%d"' % n_anim + "".join(' %s="%s"' % kv for kv in extra.items()) + (' display="none"' if hidden else "")
                if len(svg_parts) == 1 and not (b[0] == "t" and "h" in tr):
                    svg_parts = [_add_attrs(svg_parts[0], attrs)]
                else:
                    svg_parts = ["<g%s>%s</g>" % (attrs, "".join(svg_parts))]
                data.append(tr)
                n_anim += 1
            elif hidden:
                continue
            parts.extend(svg_parts)
        meta = {"v": VERSION, "dauer": round(dur, 3), "bilder": N, "marken": _marks(sc.timeline, dur), "el": data}
        blob = json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        if len(blob) <= BUDGET or attempt == 2:
            break
        budget_fps = fps / 2 ** (attempt + 1)
    if budget_fps != fps:
        warn.append("Datenblock groß: Pfade mit %.1f Bildern/s abgetastet" % budget_fps)
    blob = blob.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    sp.bg = _export.article_background(background)
    sp.parts = plain
    endbild = sp.to_svg(view=view, size=size)
    sp.parts = parts
    svg = sp.to_svg(view=view, size=size)
    svg = svg.replace("\n</svg>\n", '\n<metadata class="szenen-animation">%s</metadata>\n</svg>\n' % blob, 1)
    info = {"dauer": dur, "bilder": N + 1, "elemente": len(parts), "animiert": n_anim, "daten": len(blob),
            "marken": len(meta["marken"]), "warn": warn, "endbild": endbild}
    return svg, info


def _add_attrs(part, attrs):
    """Attribute in das erste Tag eines Elements einsetzen (<path .../> oder <text ...>)."""
    i = part.index(" ")
    return part[:i] + attrs + part[i:]
