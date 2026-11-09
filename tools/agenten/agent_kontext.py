"""Woraus der Kontext eines Agenten besteht: Zeichen je Werkzeug (Eingaben + Ergebnisse) und die größten Einzelposten.
Aufruf: python agent_kontext.py <agent.jsonl>
"""
import json
import sys
from collections import Counter
from pathlib import Path

zeichen = Counter()
posten = []
namen = {}
for z in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    try:
        d = json.loads(z)
    except Exception:
        continue
    m = d.get("message") or {}
    for t in m.get("content") or []:
        if not isinstance(t, dict):
            continue
        if t.get("type") == "tool_use":
            namen[t["id"]] = t["name"]
            n = len(json.dumps(t.get("input", {}), ensure_ascii=False))
            ziel = t["input"].get("file_path") or t["input"].get("command", "")[:60] or t["input"].get("description", "")
            zeichen[t["name"] + " (Eingabe)"] += n
            posten.append((n, t["name"] + " ein", str(ziel)[:90]))
        elif t.get("type") == "tool_result":
            c = t.get("content")
            if isinstance(c, list):
                n = sum(len(x.get("text", "")) if x.get("type") == "text" else 6000 for x in c)
            else:
                n = len(str(c))
            name = namen.get(t.get("tool_use_id"), "?")
            zeichen[name + " (Ergebnis)"] += n
            posten.append((n, name + " aus", ""))
        elif t.get("type") == "text" and m.get("role") == "assistant":
            zeichen["Text"] += len(t["text"])
gesamt = sum(zeichen.values())
print(f"gesamt {gesamt:,} Zeichen (~{gesamt // 3:,} Tokens)")
for k, v in zeichen.most_common(12):
    print(f"  {k:24s} {v:10,}")
print("größte Posten:")
for n, a, b in sorted(posten, reverse=True)[:12]:
    print(f"  {n:8,}  {a:12s} {b}")
