// Cloudflare advanced-mode entry (at the build-output root). A single Worker that serves the dynamic
// /api/count route and passes EVERYTHING else through to the static assets (env.ASSETS). Having this file
// flips the project out of "static assets only" mode, so a KV binding (COUNTERS) can be added and
// Functions run. Works whether the project is a classic Pages project or the new Workers+Assets model
// (both provide the ASSETS binding automatically). The functions/ copies become redundant when this
// file is present (advanced mode ignores functions/), but are harmless.
//
// Counters are anonymous, aggregate, cookieless, no IP stored -> GDPR-uncritical.
//   GET /api/count?event=site|editor&mode=hit  -> increment that counter, then return {site, editor}
//   GET /api/count?mode=read                   -> just return {site, editor} (per-minute refresh)
const KEYS = ["site", "editor"];

async function count(url, env) {
  const event = url.searchParams.get("event");
  const mode = url.searchParams.get("mode") || "hit";
  const kv = env.COUNTERS;
  const json = (o) => new Response(JSON.stringify(o), {
    headers: { "content-type": "application/json", "cache-control": "no-store", "access-control-allow-origin": "*" },
  });
  if (!kv) return json({ site: 0, editor: 0, pending: true });   // KV not bound yet -> fail soft
  if (mode === "hit" && KEYS.includes(event)) {
    const cur = parseInt((await kv.get(event)) || "0", 10) || 0;
    await kv.put(event, String(cur + 1));
  }
  const out = {};
  for (const k of KEYS) out[k] = parseInt((await kv.get(k)) || "0", 10) || 0;
  return json(out);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/count") return count(url, env);
    return env.ASSETS.fetch(request);                            // all other paths -> static files
  },
};
