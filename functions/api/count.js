// Cloudflare Pages Function — anonymous, AGGREGATE event counters.
// No cookies, no IP, no identifiers are stored: we only ever increment a running total per event type,
// so these numbers are not personal data (GDPR-uncritical; see also Cloudflare Web Analytics for traffic).
//
//   GET /api/count?event=site|editor&mode=hit     -> increment that counter, then return {site, editor}
//   GET /api/count?mode=read                      -> just return {site, editor} (per-minute refresh: never inflates)
//
// Storage: a Workers KV namespace bound as `COUNTERS` (keys "site" and "editor"). KV has no atomic
// increment, so we read-modify-write; under heavy concurrency a rare increment can be lost — fine for a
// visit counter. (For exact counts one would use a Durable Object; KV is the simple, free-tier choice.)
//
// NOTE: this file lives in <repo-root>/functions, NOT in the build-output dir (web/). Cloudflare Pages
// reads Functions from `/functions` relative to the project ROOT directory, independent of the static
// output directory. (If your Pages project's "Root directory" is set to `web`, move this into web/functions.)
const KEYS = ["site", "editor"];

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const event = url.searchParams.get("event");
  const mode = url.searchParams.get("mode") || "hit";
  const kv = env.COUNTERS;
  const json = (o) => new Response(JSON.stringify(o), {
    headers: {
      "content-type": "application/json",
      "cache-control": "no-store",
      "access-control-allow-origin": "*",
    },
  });
  // No binding yet (e.g. before the KV namespace is configured): fail soft so the page still renders.
  if (!kv) return json({ site: 0, editor: 0, pending: true });

  if (mode === "hit" && KEYS.includes(event)) {
    const cur = parseInt((await kv.get(event)) || "0", 10) || 0;
    await kv.put(event, String(cur + 1));
  }
  const out = {};
  for (const k of KEYS) out[k] = parseInt((await kv.get(k)) || "0", 10) || 0;
  return json(out);
}
