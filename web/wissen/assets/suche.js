/* EtUndSo-Suche: ETSuche(sprache) -> Index mit start(), suche(text, rückruf), snippet(doc, q), fold(text).
   start() lädt titel.json (Titel, Brotkrumen, Schlagwörter, summary, Abschnitte). suche() meldet sofort die Treffer aus
   diesen Feldern und den schon geladenen Volltexten, holt dann die Volltexte der Module, deren Wörter das Suchwort
   enthalten (woerter.json; ohne Verzeichnis: alle), und meldet nach jedem Modul neu. Rang wie zuvor: Titel 0,
   Schlagwort 1, Abschnittsüberschrift 1,5, Text 2 + Lage (früher = besser). Nichts verlässt den Browser. */
window.ETSuche=(function(){
  var INDEX={};
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").replace(/ı/g,"i").replace(/œ/g,"oe").replace(/æ/g,"ae")
    .normalize("NFKD").replace(/[̀-ͯ]/g,""); }          // wie fold_js() in build_wissen.py
  function esc(s){ return (s||"").replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];}); }
  function json(u){ return fetch(u).then(function(r){ if(!r.ok) throw new Error(u+": "+r.status); return r.json(); }); }
  function Index(lang){
    var B="/wissen/data/suche/"+lang+"/", self=this, T=null, WP=null, WG=null, mods=[], docs=[], jetzt=null, warte=null;
    self.fold=fold; self.esc=esc; self.docs=docs;
    self.start=function(){
      if(!T) T=json(B+"titel.json").then(function(d){
        d.m.forEach(function(m){ mods.push({f:m.f, p:m.p, da:false, P:null}); });
        d.d.forEach(function(x,i){ var sec=x[6]||[];
          docs.push({i:i, title:x[0], crumb:x[1], path:x[2], tags:x[3]||"", summary:x[4]||"", m:x[5], sec:sec, klar:x[7]||x[0],
            fTitle:fold(x[0]), fTags:fold(x[3]||""), fSum:fold(x[4]||""), fSec:sec.map(function(s){ return fold(s[1]); }),
            ft:null, text:null}); });
        self.w=!!d.w; return self;
      }).catch(function(e){ T=null; throw e; });
      return T; };
    function woerter(){                                                 // Wortverzeichnis: [{m:[Modul…], w:" wort wort … "}]
      if(!WP) WP=(self.w ? json(B+"woerter.json").then(function(d){
        WG=Object.keys(d).map(function(k){ return {m:k.split(",").map(Number), w:" "+d[k]+" "}; });
      }) : Promise.resolve()).catch(function(){ WG=null; });          // ohne Verzeichnis: alle Module laden
      return WP; }
    function moeglich(q){                                               // Module, deren Text q enthalten kann (Menge) oder null = alle
      if(!WG) return null;
      var erg=null;
      q.split(" ").filter(Boolean).forEach(function(t){                 // ein Teil ohne Leerzeichen liegt in einem Wort
        var s={}; WG.forEach(function(g){ if(g.w.indexOf(t)>=0) g.m.forEach(function(k){ s[k]=1; }); });
        if(erg) Object.keys(erg).forEach(function(k){ if(!s[k]) delete erg[k]; }); else erg=s; });
      return erg; }
    function laden(m){
      if(!m.P) m.P=json(B+m.f).then(function(rows){
        rows.forEach(function(r){ var d=docs[r[0]]; d.text=r[1]; d.ft=fold(d.summary+" "+r[1]); }); m.da=true;
      }).catch(function(){ m.P=null; m.fehler=true; });
      return m.P; }
    function rang(d,q){
      if(d.fTitle.indexOf(q)>=0) return [0];                            // Titel-Treffer: höchster Rang
      if(d.fTags.indexOf(q)>=0) return [1];                             // Schlagwort
      for(var k=0;k<d.fSec.length;k++) if(d.fSec[k].indexOf(q)>=0) return [1.5,d.sec[k][0],d.sec[k][1]];   // Abschnitt
      var p=(d.ft!==null?d.ft:d.fSum).indexOf(q);                       // Text (summary steht vorn, gilt also schon vorher)
      return p>=0 ? [2+Math.min(p/500,1)] : null; }
    function treffer(q){
      var hits=[]; docs.forEach(function(d){ var r=rang(d,q); if(r) hits.push({d:d, sc:r[0], anker:r[1]||null, abschnitt:r[2]||null}); });
      hits.sort(function(a,b){ return a.sc-b.sc; });                    // stabil: gleicher Rang in Lese-Reihenfolge
      return hits; }
    self.suche=function(raw,cb){
      var q=fold((raw||"").trim()), ich={}; jetzt=ich; clearTimeout(warte);
      if(q.length<2){ cb({q:q, hits:[], laedt:false}); return; }
      self.start().then(function(){
        if(jetzt!==ich) return;
        var ok0=moeglich(q), offen=mods.filter(function(m,k){ return !m.da && !m.fehler && (!ok0 || ok0[k]); }).length;
        function melden(){ if(jetzt===ich) cb({q:q, hits:treffer(q), laedt:offen>0}); }
        melden();
        if(!offen) return;
        woerter();                                                      // schon holen, während noch getippt wird
        warte=setTimeout(function(){                                    // erst nach einer kurzen Tipp-Pause nachladen
          woerter().then(function(){
            if(jetzt!==ich) return;
            var ok=moeglich(q);
            var noetig=mods.filter(function(m,k){ return !m.da && !m.fehler && (!ok || ok[k]); });
            offen=noetig.length; if(!offen){ melden(); return; }
            noetig.forEach(function(m){ laden(m).then(function(){ offen--; melden(); }); });
          });
        },180);
      }).catch(function(){ if(jetzt===ich) cb({q:q, hits:[], laedt:false, fehler:true}); });
    };
    self.snippet=function(d,q){
      var t=d.text||d.summary||"", ft=fold(t), i=ft.indexOf(q);
      if(i<0) return esc(t.slice(0,130))+(t.length>130?"…":"");
      var a=Math.max(0,i-45);
      return (a>0?"…":"")+esc(t.slice(a,i))+"<mark>"+esc(t.slice(i,i+q.length))+"</mark>"+esc(t.slice(i+q.length,i+q.length+70))+"…";
    };
  }
  return function(lang){ lang=lang||"de"; return INDEX[lang]||(INDEX[lang]=new Index(lang)); };
})();
