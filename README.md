# animate

Two **independent** animation projects in one repo. Same features, different rendering backend.
Pick one or use both — each works entirely on its own.

| Project | Folder | Backend | Use |
|---|---|---|---|
| **Local** | `local/` | Cairo + ffmpeg | code-only, renders PNG/MP4 on your machine |
| **Web**   | `web/`   | HTML5 Canvas (Pyodide) | runs in the browser; later with editor/GUI |

Code is intentionally duplicated between them (each has its own `engine/`), so the two stay
fully separate.

## Local project (`local/`)
Requirements: Python 3, then `pip install pycairo imageio-ffmpeg numpy`.
```bash
cd local
python run.py          # renders the demo scene -> local/output_videos/ and local/output_images/
```
Write a scene in `local/scenes/` (subclass `Scene`, override `construct()`), point `run.py` at it.

## Web project (`web/`)
A static site. It needs a web server (Pyodide fetches the `.py` files over HTTP):
```bash
cd web
python -m http.server 8000      # then open http://localhost:8000
```
You should see "Hello Sine" rendered by the Python engine via Canvas instead of Cairo.

Deployed with **Cloudflare Pages** — set the project's *Root directory* to `web`; every push to
`main` on GitHub auto-deploys.
