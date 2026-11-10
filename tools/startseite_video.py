"""Video für die Startseite mit dem Video-Export des Editors aufnehmen (headless, lokaler Server auf :8000).

    python tools/startseite_video.py                  # WebM (VP9) + MP4 (H.264, falls der Browser es kann) + Poster
    python tools/startseite_video.py --blick out.png  # nur die ruhende Editor-Ansicht der Szene als PNG (Layout prüfen)

Ablauf wie von Hand: editor.html?scene=… öffnen, warten bis Engine und Formeln bereit sind, im Menü „Animation ▾“
das Format wählen; den Download speichert Playwright. Der Editor nimmt mit 12 Mbit/s auf (für Downloads gedacht);
für die Startseite begrenzt dieses Skript die Bitrate, indem es MediaRecorder in der Seite umhüllt (editor.js bleibt
unverändert). Für MP4 braucht es einen Browser mit H.264-Encoder: zuerst Microsoft Edge, sonst Chromium.
Danach bekommt Bild k den Zeitstempel k/30 s (webm_takt, mp4_takt): Headless zeichnet Pyodide ein Bild langsamer
als in 1/30 s, und MediaRecorder stempelt mit der Wanduhr. Die Bilder selbst bleiben die des Editors.
Das Poster ist ein Einzelbild aus dem fertigen WebM (an der Stelle --poster-t, in Sekunden).
"""
import argparse
import json
import math
import base64
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "web" / "startseite"
BASIS = "http://localhost:8000/"
sys.stdout.reconfigure(encoding="utf-8")

BITRATE = """
(() => { const MR = window.MediaRecorder; if (!MR) return;
  const cap = %d;
  class Begrenzt extends MR { constructor(stream, opts) { opts = Object.assign({}, opts || {});
      opts.videoBitsPerSecond = Math.min(opts.videoBitsPerSecond || cap, cap); super(stream, opts); } }
  Begrenzt.isTypeSupported = MR.isTypeSupported.bind(MR);
  window.MediaRecorder = Begrenzt; })();
"""
# Zeitlupe: performance.now läuft K-mal langsamer. exportVideo taktet nach dieser Uhr, also kommt ein Bild nur alle
# K/30 s; Zeichnen (Pyodide) und Kodieren (VP9 in Software) haben so Luft, kein Bild fällt aus. webm_takt/mp4_takt
# setzen danach die Zeitstempel auf k/30 s. Die Bitrate wird dazu durch K geteilt (Bits je Bild bleiben gleich).
ZEITLUPE = """
(() => { const o = performance.now.bind(performance), t0 = o(), K = %g;
  performance.now = () => t0 + (o() - t0) / K; })();
"""


def editor_laden(page, szene):
    page.goto(BASIS + "editor.html?scene=szenen/" + szene + ".json")
    page.wait_for_function("() => { const s = document.getElementById('status'); return s && !/Loading/i.test(s.textContent); }",
                           timeout=180000)
    page.wait_for_timeout(5000)                         # MathJax-Glyphen der Formeln (asynchron) + Neuaufbau


def aufnehmen(page, label, ziel):
    page.click("#dl-video-caret")
    items = page.locator("#dl-video-menu .export-item")
    namen = [items.nth(i).inner_text() for i in range(items.count())]
    if label not in namen:
        page.keyboard.press("Escape")
        page.mouse.click(5, 5)
        return None, namen
    with page.expect_download(timeout=240000) as dl:
        items.nth(namen.index(label)).click()
    dl.value.save_as(str(ziel))
    page.wait_for_timeout(800)
    return ziel, namen


# ---------------------------------------------------------------------------- Zeitstempel nachziehen
# Der Editor schiebt jedes Bild einzeln in den Recorder (requestFrame): Bild k zeigt genau die Szene zur Zeit k/fps.
# MediaRecorder stempelt aber mit der Wanduhr; braucht ein Bild länger als 1/fps zum Zeichnen (Pyodide, voller
# Rechner), läuft das Video langsamer als die Szene. Hier bekommt Bild k wieder den Zeitstempel k/fps. Die Bilder
# selbst bleiben unverändert (kein neues Kodieren), nur die Zeitangaben im Container werden ersetzt.

def _vint(d, p, marker=False):
    b0, n = d[p], 1
    while n <= 8 and not (b0 & (0x80 >> (n - 1))):
        n += 1
    v = b0 if marker else b0 & (0xFF >> n)
    for i in range(1, n):
        v = (v << 8) | d[p + i]
    return v, n


def webm_takt(pfad, fps, abstand_ms):
    """WebM (Matroska, TimecodeScale 1 ms): Cluster-Timecode und SimpleBlock-Versatz je Bild neu, dazu die
    Dauer in Info und die Zeiten der Cues (Sprungmarken). Alle Felder behalten ihre Breite (die Werte werden kleiner)."""
    import struct
    d = bytearray(pfad.read_bytes())
    MASTER = {0x18538067, 0x1549A966, 0x1F43B675, 0x1C53BB6B, 0xBB, 0xB7}   # Segment, Info, Cluster, Cues, CuePoint, CueTrackPositions
    cluster, cues, dauer_feld, seg0 = [], [], None, [0]

    def walk(p, end, eltern):
        nonlocal dauer_feld
        while p < end:
            eid, n1 = _vint(d, p, True)
            size, n2 = _vint(d, p + n1)
            body = p + n1 + n2
            e = end if size == (1 << (7 * n2)) - 1 else min(end, body + size)
            if eid == 0x18538067:
                seg0[0] = body
            if eid == 0x1F43B675:
                cluster.append({"pos": p - seg0[0], "tc": None, "bloecke": []})
            if eid == 0xBB:
                cues.append({"zeit": None, "cluster": None})
            if eid in MASTER:
                walk(body, e, eltern + [eid])
                p = e
                continue
            if eid == 0xE7 and cluster:                              # Cluster-Timecode
                cluster[-1]["tc"] = (body, size)
            elif eid == 0xA3 and cluster:                            # SimpleBlock: Spur (vint), Versatz int16, Flags
                spur, n = _vint(d, body)
                if spur == 1:
                    cluster[-1]["bloecke"].append(body + n)
            elif eid == 0x4489 and eltern[-1:] == [0x1549A966]:      # Info/Duration (float)
                dauer_feld = (body, size)
            elif eid == 0xB3 and cues:                               # CueTime
                cues[-1]["zeit"] = (body, size)
            elif eid == 0xF1 and cues:                               # CueClusterPosition
                cues[-1]["cluster"] = int.from_bytes(d[body:body + size], "big")
            p = body + size
    walk(0, len(d), [])
    alt = []                                                         # Wanduhr-Zeit je Bild (ms)
    for c in cluster:
        pos, w = c["tc"]
        tc = int.from_bytes(d[pos:pos + w], "big")
        alt += [tc + int.from_bytes(d[bp:bp + 2], "big", signed=True) for bp in c["bloecke"]]
    nummern = iter(_bildnummern(alt, abstand_ms))
    basis_von, k = {}, 0
    for c in cluster:
        if not c["bloecke"]:
            continue
        neu = [round(next(nummern) * 1000 / fps) for _ in c["bloecke"]]
        basis = basis_von[c["pos"]] = neu[0]
        pos, w = c["tc"]
        d[pos:pos + w] = basis.to_bytes(w, "big")
        for bp, t in zip(c["bloecke"], neu):
            d[bp:bp + 2] = (t - basis).to_bytes(2, "big", signed=True)
        k = round(neu[-1] * fps / 1000) + 1
    for c in cues:
        if c["zeit"] and c["cluster"] in basis_von:
            pos, w = c["zeit"]
            d[pos:pos + w] = basis_von[c["cluster"]].to_bytes(w, "big")
    dauer_ms = k * 1000 / fps
    if dauer_feld:
        pos, w = dauer_feld
        d[pos:pos + w] = struct.pack(">f" if w == 4 else ">d", dauer_ms)
    pfad.write_bytes(bytes(d))
    return len(alt), dauer_ms / 1000


def _bildnummern(zeiten_ms, abstand_ms):
    """Wanduhr-Zeitstempel -> Bildnummer k. In Zeitlupe kommt Bild k zur Zeit k·abstand_ms (+ wenige ms Streuung);
    verwirft der Encoder ein Bild, fehlt nur dessen Nummer und das Bild davor steht entsprechend länger."""
    out = []
    for t in zeiten_ms:
        k = round((t - zeiten_ms[0]) / abstand_ms)
        out.append(max(k, out[-1] + 1) if out else k)
    return out


def mp4_takt(pfad, fps, abstand_ms):
    """Fragmentiertes MP4 (MediaRecorder): tfdt/trun je Fragment neu, Dauern in mvhd/tkhd/mdhd; mfra entfällt."""
    import struct
    d = bytearray(pfad.read_bytes())
    CONT = {b"moov", b"trak", b"mdia", b"minf", b"moof", b"traf"}
    boxen = []

    def walk(p, end):
        while p + 8 <= end:
            size, typ = struct.unpack(">I4s", d[p:p + 8])
            hdr = 8
            if size == 1:
                size, hdr = struct.unpack(">Q", d[p + 8:p + 16])[0], 16
            elif size == 0:
                size = end - p
            boxen.append((typ, p, p + hdr, size))
            if typ in CONT:
                walk(p + hdr, p + size)
            p += size
    walk(0, len(d))
    ts_film = ts_spur = None
    for typ, p, b, size in boxen:
        if typ == b"mvhd":
            ts_film = struct.unpack(">I", d[b + 20:b + 24])[0] if d[b] == 1 else struct.unpack(">I", d[b + 12:b + 16])[0]
        if typ == b"mdhd":
            ts_spur = struct.unpack(">I", d[b + 20:b + 24])[0] if d[b] == 1 else struct.unpack(">I", d[b + 12:b + 16])[0]
    schritt = ts_spur / fps
    if abs(schritt - round(schritt)) > 1e-9:
        raise RuntimeError("Zeitskala %d nicht durch %d teilbar" % (ts_spur, fps))
    schritt = int(round(schritt))
    # 1. Lesen: je Fragment die tfdt-Position und die Dauer-Felder der Bilder (trun mit Dauer je Bild)
    frag, alt = [], []
    for typ, p, b, size in boxen:
        if typ == b"tfdt":
            v1 = d[b] == 1
            pos, w = (b + 4, 8) if v1 else (b + 4, 4)
            frag.append({"tfdt": (pos, w), "felder": []})
            t = int.from_bytes(d[pos:pos + w], "big")
        elif typ == b"trun":
            fl = int.from_bytes(d[b + 1:b + 4], "big")
            if not fl & 0x100:
                raise RuntimeError("trun ohne Dauer je Bild: nicht vorgesehen")
            n = struct.unpack(">I", d[b + 4:b + 8])[0]
            q = b + 8 + (4 if fl & 0x01 else 0) + (4 if fl & 0x04 else 0)
            je = 4 * sum(1 for bit in (0x100, 0x200, 0x400, 0x800) if fl & bit)
            for i in range(n):
                alt.append(t * 1000 / ts_spur)
                t += int.from_bytes(d[q:q + 4], "big")
                frag[-1]["felder"].append(q)
                q += je
    # 2. Schreiben: Bild k beginnt bei k·schritt, dauert bis zum nächsten Bild (das letzte 1/fps)
    nr = _bildnummern(alt, abstand_ms)
    i = 0
    for f in frag:
        pos, w = f["tfdt"]
        d[pos:pos + w] = (nr[i] * schritt).to_bytes(w, "big")
        for q in f["felder"]:
            dauer_i = (nr[i + 1] - nr[i]) * schritt if i + 1 < len(nr) else schritt
            d[q:q + 4] = dauer_i.to_bytes(4, "big")
            i += 1
    k = len(alt)
    dauer = (nr[-1] + 1) / fps
    for typ, p, b, size in boxen:
        if typ in (b"mvhd", b"mdhd", b"tkhd"):
            v1 = d[b] == 1
            if typ == b"tkhd":
                off, w = (b + 28, 8) if v1 else (b + 20, 4)
                wert = round(dauer * ts_film)
            else:
                off, w = (b + 24, 8) if v1 else (b + 16, 4)
                wert = round(dauer * (ts_film if typ == b"mvhd" else ts_spur))
            d[off:off + w] = wert.to_bytes(w, "big")
    mfra = [p for typ, p, b, size in boxen if typ == b"mfra"]
    if mfra:
        del d[mfra[0]:]
    pfad.write_bytes(bytes(d))
    return k, dauer


def poster(page, video, t, ziel, breite):
    """Ein Bild aus dem Video (Zeit t) als JPEG, auf `breite` px verkleinert. Headless zeigt ein Video nach dem
    Springen (currentTime) nicht zuverlässig das neue Bild; darum abspielen und das erste Bild ab t abgreifen."""
    page.goto(BASIS + "startseite/")                     # gleiche Herkunft, sonst ist das Canvas „tainted“
    data = page.evaluate("""async ([src, t, w]) => {
        const v = document.createElement('video'); v.muted = true; v.src = src; v.preload = 'auto';
        document.body.appendChild(v);
        await new Promise((ok, err) => { v.onloadeddata = ok; v.onerror = () => err('video'); });
        const c = document.createElement('canvas'); c.width = w; c.height = Math.round(w * v.videoHeight / v.videoWidth);
        const g = c.getContext('2d'); g.imageSmoothingQuality = 'high';
        await new Promise(ok => { const cb = (_, m) => { if (m.mediaTime >= t - 1e-3) { v.pause();
              g.drawImage(v, 0, 0, c.width, c.height); ok(); } else v.requestVideoFrameCallback(cb); };
            v.requestVideoFrameCallback(cb); v.play(); });
        return [c.toDataURL('image/jpeg', 0.9), v.duration, v.videoWidth, v.videoHeight];
    }""", [video, t, breite])
    ziel.write_bytes(base64.b64decode(data[0].split(",", 1)[1]))
    return data[1:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--szene", default="startseite/fourier")
    ap.add_argument("--blick", help="nur die ruhende Ansicht als PNG speichern")
    ap.add_argument("--bitrate", type=int, default=4_000_000, help="Höchstbitrate im fertigen Video (bit/s)")
    ap.add_argument("--zeitlupe", type=float, default=4.0)
    ap.add_argument("--poster-t", type=float, default=9.8)
    ap.add_argument("--poster-breite", type=int, default=1280)
    a = ap.parse_args()
    name = a.szene.split("/")[-1]
    OUT.mkdir(parents=True, exist_ok=True)
    szene = json.loads((ROOT / "web" / "szenen" / (a.szene + ".json")).read_text(encoding="utf-8"))
    soll = math.ceil(sum(x["run_time"] for x in szene["model"]["animations"]) * 30) + 1   # Bilder 0 … ceil(Dauer·30)
    with sync_playwright() as p:
        try:
            browser, welcher = p.chromium.launch(channel="msedge"), "Edge"
        except Exception:
            browser, welcher = p.chromium.launch(), "Chromium"
        ctx = browser.new_context(viewport={"width": 1500, "height": 950}, accept_downloads=True, color_scheme="light")
        ctx.add_init_script(BITRATE % round(a.bitrate / a.zeitlupe))
        page = ctx.new_page()
        fehler = []
        page.on("console", lambda m: fehler.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: fehler.append(str(e)))
        editor_laden(page, a.szene)
        if a.blick:
            page.locator("#view").screenshot(path=a.blick)
            print("Ansicht ->", a.blick, "| Status:", page.inner_text("#status"))
        else:
            print("Browser:", welcher)
            page.evaluate(ZEITLUPE % a.zeitlupe)            # erst nach dem Laden: die Engine soll normal booten
            # Aufwärmen: Beim ersten Durchlauf braucht Pyodide für einzelne Bilder deutlich länger (erste Ausführung);
            # exportVideo holt den Rückstand mit einer Bilderserie auf, die der VP9-Encoder teils verwirft.
            warm, _ = aufnehmen(page, "WebM (VP8)", OUT / "_aufwaermen.webm")
            if warm:
                warm.unlink()
            webm, namen = aufnehmen(page, "WebM (VP9)", OUT / (name + ".webm"))
            print("Formate im Menü:", namen)
            mp4, _ = aufnehmen(page, "MP4 (H.264)", OUT / (name + ".mp4"))
            for f, takt in ((webm, webm_takt), (mp4, mp4_takt)):
                if f:
                    bilder, dauer = takt(f, 30, 1000 * a.zeitlupe / 30)   # exportVideo: 30 Bilder/s, hier in Zeitlupe
                    print("%s: %d von %d Bildern, %.2f s (Soll %.2f s), %.2f MB" % (f.name, bilder, soll, dauer, soll / 30, f.stat().st_size / 1e6))
                    if abs(dauer - soll / 30) > 0.05:
                        print("  ⚠ Dauer weicht ab: Bildnummern nicht eindeutig. Größere --zeitlupe wählen.")
            if webm:
                dur, w, h = poster(page, "/startseite/" + webm.name, a.poster_t, OUT / (name + "_poster.jpg"), a.poster_breite)
                print("Poster bei %.1f s, Video %.2f s, %dx%d, Poster %d kB" % (a.poster_t, dur, w, h, (OUT / (name + "_poster.jpg")).stat().st_size // 1000))
        if fehler:
            print("Konsolenfehler:", fehler[:8])
        browser.close()


if __name__ == "__main__":
    main()
