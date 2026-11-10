// Tests the editor's LaTeX preparation (block series-spec in editor.js) without a browser, as tools/export_szenen.py uses it:
// localizeTex (decimal comma, code in \texttt/\mathtt: no gap after '.', straight ' and `), and Σ / ∏ with another running
// index (props.index) and exact fractions (props.exact). Run: node web/tests/test_texspec.mjs
import { readFileSync } from "node:fs";
const src = readFileSync(new URL("../editor.js", import.meta.url), "utf8");
const a = src.indexOf("// >>> series-spec"), b = src.indexOf("// <<< series-spec");
const api = new Function(src.slice(a, b) + "\nreturn { seriesSpec, localizeTex, _exactTermJS };")();
let fails = 0;
const eq = (name, got, want) => { if (JSON.stringify(got) !== JSON.stringify(want)) { fails++; console.log("FALSCH", name, "\n  bekommen:", JSON.stringify(got), "\n  erwartet:", JSON.stringify(want)); } };

// localizeTex
eq("Komma in de, Punkt in en", [api.localizeTex("x = 0.5", "de"), api.localizeTex("x = 0.5", "en")], ["x = 0{,}5", "x = 0.5"]);
eq("\\mathtt: '.' ohne Abstand, in jeder Sprache", [api.localizeTex("\\mathtt{einkauf.txt}", "de"), api.localizeTex("\\mathtt{a.b}", "zh")],
   ["\\mathtt{einkauf{.}txt}", "\\mathtt{a{.}b}"]);
eq("\\texttt ohne Anführungszeichen unverändert", api.localizeTex("\\texttt{ls -l 1.5}", "de"), "\\texttt{ls -l 1.5}");
eq("\\texttt: ' und ` gerade (Strich, Gravis) auf der Zelle", api.localizeTex("\\texttt{a'b`c}", "en"),
   "{\\texttt{a}\\kern0.2275em\\rule[0.36em]{0.07em}{0.26em}\\kern0.2275em\\texttt{b}\\kern0.0125em\\unicode{x60}\\kern0.0125em\\texttt{c}}");
eq("Code mit \\$ \\{ \\} bleibt geschützt (kein Komma)", api.localizeTex("\\texttt{echo \\${x} 2.5} 2.5", "de"), "\\texttt{echo \\${x} 2.5} 2{,}5");
eq("Längen behalten den Punkt", api.localizeTex("\\hspace{0.5em} 0.5", "fr"), "\\hspace{0.5em} 0{,}5");

// Σ / ∏
const terms = (c, lang) => { const s = api.seriesSpec(c, lang || "de");
  return { head: s.head, v: s.var, vals: s.cols.filter(x => x.t === "term").map(x => x.value), tot: s.cols.filter(x => x.t === "total").map(x => x.g) }; };
const p = { sum_mode: "number", from: 1, to: "4", show_terms: 4 };
eq("Laufindex k, exakte Brüche", terms({ type: "Summation", props: { ...p, term: "3/2^(4*k+1)", index: "k", exact: true } }),
   { head: "\\sum_{k=1}^{4} \\frac{3}{2^{\\left(4 \\cdot k + 1\\right)}}", v: "k",
     vals: ["\\frac{3}{32}", "\\frac{3}{512}", "\\frac{3}{8192}", "\\frac{3}{131072}"], tot: ["\\frac{13107}{131072}", "0{,}0999985"] });
eq("ohne exact wie bisher (Nenner über 10000 als Dezimalzahl)",
   terms({ type: "Summation", props: { ...p, term: "3/2^(4*k+1)", index: "k" } }).vals[3], "0{,}000022888");
eq("ohne index: i wie bisher", terms({ type: "Summation", props: { ...p, term: "1/i^2" } }).head, "\\sum_{i=1}^{4} \\frac{1}{i^{2}}");
eq("∏ exakt mit Index j", terms({ type: "BigProduct", props: { ...p, term: "1 + 1/j", index: "j", exact: true } }).tot, ["5"]);
eq("exakt, aber nicht rational: Dezimalzahl", terms({ type: "Summation", props: { ...p, to: "2", term: "sqrt(i)", exact: true } }).vals, ["1", "1{,}4142"]);
eq("Index e ist verboten (Euler): bleibt i", terms({ type: "Summation", props: { ...p, term: "i", index: "e" } }).v, "i");
const ex = api._exactTermJS("(-1)^n/n + 0.25*floor(n/2) - 7%n", "n");
eq("_exactTermJS: Potenz, Rest, floor, Dezimalzahl exakt (-1/3 + 1/4 - 1)", ex(3).map(String), ["-13", "12"]);

console.log(fails ? "TEXSPEC TESTS FAILED" : "TEXSPEC TESTS PASSED");
process.exit(fails ? 1 : 0);
