// Tests the editor's numeric expression evaluator (evalExprJS) without a browser:
// it must compute ordinary terms and must never execute code from a scene file.
// Run: node web/tests/test_exprjs.mjs
import { readFileSync } from "node:fs";
const src = readFileSync(new URL("../editor.js", import.meta.url), "utf8");
const start = src.indexOf("const _JS_FUNCS");
const fnStart = src.indexOf("function evalExprJS", start);
const tail = /\r?\n\}\r?\n/.exec(src.slice(fnStart));          // closing brace of evalExprJS (LF or CRLF)
const end = fnStart + tail.index + tail[0].length;
const evalExprJS = new Function(src.slice(start, end) + "\nreturn evalExprJS;")();   // our own source

const near = (a, b) => Math.abs(a - b) <= 1e-12 * Math.max(1, Math.abs(b));
const cases = [
  ["1/i^2", 2, 0.25], ["2i", 3, 6], ["i(i+1)", 3, 12], ["-2^2", 0, -4], ["2^3^2", 0, 512],
  ["(-1)^i/i", 3, -1 / 3], ["2pi", 0, 2 * Math.PI], ["e^i", 1, Math.E], ["1e-3*i", 2, 0.002],
  ["sqrt(i)+abs(-i)", 4, 6], ["max(i,3)-min(i,3)", 5, 2], ["i**2", 4, 16], ["7%i", 4, 3],
  [" 1 / ( i + 1 ) ", 1, 0.5], ["log(e)", 0, 1], ["sin(pi/2)", 0, 1],
];
let fails = 0;
for (const [t, i, want] of cases) {
  const got = evalExprJS(t)(i);
  if (!near(got, want)) { fails++; console.log("FALSCH", t, "i=" + i, "->", got, "erwartet", want); }
}
// code-shaped input must evaluate to NaN and must not run
globalThis.__hit = 0;
const evil = ["globalThis.__hit=1", "(()=>{globalThis.__hit=1})()", "constructor.constructor('globalThis.__hit=1')()",
              "Math.PI", "alert(1)", "i;globalThis.__hit=1", "this", "[1][0]", "'a'"];
for (const t of evil) {
  const v = evalExprJS(t)(1);
  if (!Number.isNaN(v)) { fails++; console.log("NICHT NaN:", t, v); }
}
if (globalThis.__hit) { fails++; console.log("CODE WURDE AUSGEFÜHRT"); }
console.log(`${cases.length} Rechenfälle, ${evil.length} Angriffsfälle`);
if (fails) { console.log("EXPRJS TESTS FAILED:", fails); process.exit(1); }
console.log("EXPRJS TESTS PASSED");
