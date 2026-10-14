// Loads the Python engine (web/engine) into Pyodide and renders "Hello Sine" to the canvas.
// The web variant uses the Canvas backend; the SAME engine core runs, just a different painter.

const ENGINE_FILES = [
  "__init__.py", "constants.py", "camera.py", "renderer.py", "AnimObject.py",
  "bezier.py", "simpleShape.py", "text.py", "axes.py", "animation.py",
  "rate_functions.py", "scene.py", "scene_model.py",
];
const WEB_PY = ["canvas_painter.py", "hello.py"];

const setStatus = (msg) => { document.getElementById("status").textContent = msg; };

async function fetchText(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error(`fetch fehlgeschlagen: ${path} (${r.status})`);
  return r.text();
}

async function main() {
  setStatus("Lade Pyodide …");
  const pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.27.2/full/" });

  setStatus("Lade numpy …");
  await pyodide.loadPackage("numpy");

  setStatus("Lade Engine …");
  pyodide.FS.mkdir("engine");
  for (const f of ENGINE_FILES) {
    pyodide.FS.writeFile(`engine/${f}`, await fetchText(`engine/${f}`));
  }
  for (const f of WEB_PY) {
    pyodide.FS.writeFile(f, await fetchText(`py/${f}`));
  }

  // hand the canvas 2D context to Python
  const canvas = document.getElementById("view");
  pyodide.globals.set("js_ctx", canvas.getContext("2d"));
  pyodide.globals.set("js_w", canvas.width);
  pyodide.globals.set("js_h", canvas.height);

  setStatus("Rendere …");
  await pyodide.runPythonAsync(await fetchText("py/hello.py"));
  setStatus("Fertig ✓  — gerendert aus derselben Python-Engine, nur über Canvas statt Cairo.");
}

main().catch((e) => { console.error(e); setStatus("Fehler: " + e.message); });
