"""Kontextgröße und Werkzeugaufrufe der laufenden Agenten aus ihren Protokollen.
Aufruf: python agent_tokens.py <subagents-ordner> <id> ...
"""
import json
import sys
from collections import Counter
from pathlib import Path

ordner = Path(sys.argv[1])
for aid in sys.argv[2:]:
    p = ordner / f"agent-{aid}.jsonl"
    letzte = None
    werkzeuge = Counter()
    lesen = Counter()
    zeit = ""
    for z in p.read_text(encoding="utf-8").splitlines():
        try:
            d = json.loads(z)
        except Exception:
            continue
        m = d.get("message") or {}
        if m.get("role") == "assistant":
            u = m.get("usage") or {}
            if u:
                letzte = u
                zeit = d.get("timestamp", "")
            for t in m.get("content") or []:
                if isinstance(t, dict) and t.get("type") == "tool_use":
                    werkzeuge[t["name"]] += 1
                    if t["name"] == "Read":
                        fp = t["input"].get("file_path", "")
                        if fp.lower().endswith((".png", ".jpg", ".pdf")):
                            lesen["Bild/PDF"] += 1
    kontext = sum((letzte or {}).get(k, 0) for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
    print(f"{aid}: Kontext zuletzt {kontext:,} Tokens, Stand {zeit}")
    print("   Werkzeuge:", dict(werkzeuge.most_common(8)), "| Bilder/PDF gelesen:", lesen.get("Bild/PDF", 0))
