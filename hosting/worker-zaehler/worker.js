// Cloudflare Worker: anonymer Besucherzähler für EtUndSo, seit die Website vom Raspberry Pi kommt.
// Gleiches Verhalten wie die bisherige Pages-Funktion web/functions/api/count.js:
// keine Cookies, keine IP, keine Kennungen; nur zwei laufende Summen ("site", "editor").
//
//   GET /api/count?event=site|editor&mode=hit   -> Zähler erhöhen, dann {site, editor} zurückgeben
//   GET /api/count?mode=read                    -> nur lesen
//
// Einrichten im Cloudflare-Dashboard (Anleitung: hosting/ANLEITUNG.md, Schritt 8):
//   Worker anlegen, diesen Code einfügen, KV-Namespace als Variable COUNTERS binden (derselbe wie bisher
//   bei Pages), Route  etundso.de/api/*  hinzufügen.
const KEYS = ["site", "editor"];

const json = (o, status = 200) => new Response(JSON.stringify(o), {
  status,
  headers: {
    "content-type": "application/json",
    "cache-control": "no-store",
    "access-control-allow-origin": "*",
  },
});

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/api/count") return json({ error: "not found" }, 404);
    if (request.method !== "GET") return json({ error: "method not allowed" }, 405);

    const event = url.searchParams.get("event");
    const mode = url.searchParams.get("mode") || "hit";
    const kv = env.COUNTERS;
    if (!kv) return json({ site: 0, editor: 0, pending: true });   // noch keine Bindung: Seite läuft trotzdem

    // KV kennt kein atomares Hochzählen; bei sehr vielen gleichzeitigen Aufrufen kann selten einer fehlen.
    if (mode === "hit" && KEYS.includes(event)) {
      const cur = parseInt((await kv.get(event)) || "0", 10) || 0;
      await kv.put(event, String(cur + 1));
    }
    const out = {};
    for (const k of KEYS) out[k] = parseInt((await kv.get(k)) || "0", 10) || 0;
    return json(out);
  },
};
