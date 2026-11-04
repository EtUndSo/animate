
var NICHTS={de:"Nichts gefunden für „{q}\".",en:"Nothing found for „{q}\".",es:"Nada encontrado para „{q}\".",zh:"未找到 „{q}\".",
            fr:"Aucun résultat pour «\u00a0{q}\u00a0».",tr:"“{q}” için sonuç bulunamadı."};
// Suche: vorab gebauter Index (search.json), Teilwort-/Infix-Treffer, umlaut-/ß-tolerant, gerankt + hervorgehoben.
(function(){
  var overlay=document.getElementById("searchOverlay"), input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"), btn=document.getElementById("searchBtn");
  var DOCS=null, sel=-1, rows=[];
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").replace(/ı/g,"i").replace(/œ/g,"oe").replace(/æ/g,"ae")
    .normalize("NFKD").replace(/[̀-ͯ]/g,""); }                // wie fold() in build_wissen.py
  function load(){ if(DOCS) return Promise.resolve(DOCS);
    var L=document.documentElement.lang; L=(L&&L!=="de")?"."+L:"";
    return fetch("/wissen/data/search"+L+".json").then(function(r){return r.json();}).then(function(d){DOCS=d;return d;}).catch(function(){DOCS=[];return [];}); }
  function esc(s){ return s.replace(/[&<>]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;"}[c];}); }
  function safeSnippet(doc,q){
    var t=doc.text||doc.summary||"", ft=fold(t), i=ft.indexOf(q);
    if(i<0) return esc(t.slice(0,130))+(t.length>130?"…":"");
    var a=Math.max(0,i-45);
    return (a>0?"…":"")+esc(t.slice(a,i))+"<mark>"+esc(t.slice(i,i+q.length))+"</mark>"+esc(t.slice(i+q.length,i+q.length+70))+"…";
  }
  function search(raw){
    var q=fold(raw.trim()); results.innerHTML=""; rows=[]; sel=-1;
    if(q.length<2 || !DOCS) return;
    var hits=[];
    for(var k=0;k<DOCS.length;k++){ var d=DOCS[k], sc=-1;
      if(d.ft_title.indexOf(q)>=0) sc=0;                 // Titel-Treffer: höchster Rang
      else if((d.ft_tags||"").indexOf(q)>=0) sc=1;       // Tag
      else { var p=d.ft_text.indexOf(q); if(p>=0) sc=2+Math.min(p/500,1); }  // Text, früher = besser
      if(sc>=0) hits.push([sc,d]);
    }
    hits.sort(function(a,b){return a[0]-b[0];});
    hits.slice(0,25).forEach(function(h){ var d=h[1];
      var a=document.createElement("a"); a.href="/wissen/"+d.path;
      a.innerHTML='<div class="r-crumb">'+esc(d.crumb||"")+'</div>'+
                  '<div class="r-title">'+esc(d.title)+'</div>'+
                  '<div class="r-snip">'+safeSnippet(d,q)+'</div>';
      results.appendChild(a); rows.push(a);
    });
    if(!rows.length) results.innerHTML='<div class="searchHint">'+esc(NICHTS[document.documentElement.lang]||NICHTS.de).split("{q}").join(esc(raw.trim()))+'</div>';
  }
  function open(){ if(!overlay) return; overlay.hidden=false; load().then(function(){ input.value=""; results.innerHTML=""; input.focus(); }); }
  function close(){ if(overlay) overlay.hidden=true; }
  if(btn) btn.addEventListener("click",open);
  document.addEventListener("keydown",function(e){
    if(e.key==="/" && !/input|textarea|select/i.test((document.activeElement||{}).tagName) && (!overlay||overlay.hidden)){ e.preventDefault(); open(); }
    else if(e.key==="Escape"){ close(); }
    else if(!overlay||overlay.hidden) return;
    else if(e.key==="ArrowDown"){ e.preventDefault(); sel=Math.min(rows.length-1,sel+1); paintSel(); }
    else if(e.key==="ArrowUp"){ e.preventDefault(); sel=Math.max(0,sel-1); paintSel(); }
    else if(e.key==="Enter" && rows[sel]){ location.href=rows[sel].href; }
  });
  function paintSel(){ rows.forEach(function(r,i){ r.classList.toggle("sel",i===sel); }); if(rows[sel]) rows[sel].scrollIntoView({block:"nearest"}); }
  if(input) input.addEventListener("input",function(){ search(input.value); });
  if(overlay) overlay.addEventListener("click",function(e){ if(e.target===overlay) close(); });
})();
// Sprachmenü (build_wissen.lang_switch): Der Knopf öffnet und schließt die Liste. Esc, ein Klick daneben oder Tab aus dem
// Menü schließen sie; Esc bringt den Fokus zurück auf den Knopf. Mit der Tastatur geöffnet (Enter, Leertaste, Pfeil)
// steht der Fokus auf der aktuellen Sprache, Pfeiltasten, Pos1 und Ende wandern durch die übersetzten Sprachen.
(function(){
  var menus=[].slice.call(document.querySelectorAll("[data-langmenu]"));
  function btn(m){ return m.querySelector(".l-toggle"); }
  function list(m){ return m.querySelector(".l-menu"); }
  function links(m){ return [].slice.call(m.querySelectorAll("a.l-item")); }
  function isOpen(m){ var l=list(m); return !!(l && !l.hidden); }
  function close(m, focusBtn){ if(!isOpen(m)) return; list(m).hidden=true; btn(m).setAttribute("aria-expanded","false"); if(focusBtn) btn(m).focus(); }
  function open(m, focus){
    menus.forEach(function(o){ if(o!==m) close(o,false); });
    list(m).hidden=false; btn(m).setAttribute("aria-expanded","true");
    if(focus){ var ls=links(m), t=(focus==="last") ? ls[ls.length-1] : (m.querySelector("a.l-item.on")||ls[0]); if(t) t.focus(); }
  }
  function move(m, d){ var ls=links(m); if(!ls.length) return; var i=ls.indexOf(document.activeElement);
    i=(i<0) ? (d>0 ? 0 : ls.length-1) : (i+d+ls.length)%ls.length; ls[i].focus(); }
  menus.forEach(function(m){
    var b=btn(m), l=list(m); if(!b || !l) return;
    b.addEventListener("click",function(e){ if(isOpen(m)) close(m,false); else open(m, e.detail===0); });   // detail 0: Tastatur
    b.addEventListener("keydown",function(e){
      if(e.key==="ArrowDown"){ e.preventDefault(); open(m,true); }
      else if(e.key==="ArrowUp"){ e.preventDefault(); open(m,"last"); }
    });
    l.addEventListener("keydown",function(e){
      var ls=links(m);
      if(e.key==="ArrowDown"){ e.preventDefault(); move(m,1); }
      else if(e.key==="ArrowUp"){ e.preventDefault(); move(m,-1); }
      else if(e.key==="Home" && ls.length){ e.preventDefault(); ls[0].focus(); }
      else if(e.key==="End" && ls.length){ e.preventDefault(); ls[ls.length-1].focus(); }
    });
    m.addEventListener("focusout",function(e){ if(e.relatedTarget && !m.contains(e.relatedTarget)) close(m,false); });   // Tab hinaus
  });
  document.addEventListener("keydown",function(e){
    if(e.key==="Escape") menus.forEach(function(m){ if(isOpen(m)) close(m, m.contains(document.activeElement)); });
  });
  document.addEventListener("click",function(e){ menus.forEach(function(m){ if(isOpen(m) && !m.contains(e.target)) close(m,false); }); });
})();
// Inhaltsverzeichnis: aktuellen Abschnitt beim Scrollen markieren.
(function(){
  var links=[].slice.call(document.querySelectorAll(".toc a")); if(!links.length) return;
  var map=links.map(function(a){ var el=document.getElementById(a.getAttribute("href").slice(1)); return {a:a,el:el}; }).filter(function(x){return x.el;});
  function onScroll(){ var y=window.scrollY+80, cur=map[0];
    map.forEach(function(x){ if(x.el.offsetTop<=y) cur=x; });
    links.forEach(function(a){a.classList.remove("active");}); if(cur) cur.a.classList.add("active");
  }
  window.addEventListener("scroll",onScroll,{passive:true}); onScroll();
})();
// Hell/Dunkel-Umschalter + einklappbare Panels (Fokusmodus) + Mobil-Menü für den Themenbaum.
(function(){
  var root=document.documentElement, layout=document.querySelector(".layout");
  var tb=document.getElementById("themeBtn");
  if(tb) tb.addEventListener("click",function(){
    var dark=root.getAttribute("data-theme")==="dark";          // Wissen-Konvention: dunkel = data-theme="dark"
    if(dark) root.removeAttribute("data-theme"); else root.setAttribute("data-theme","dark");
    try{ localStorage.setItem("animate-theme", dark?"light":"dark"); }catch(e){}   // Schlüssel mit dem Editor geteilt
  });
  if(!layout) return;
  var side=layout.querySelector(".side"), mq=window.matchMedia("(max-width:720px)");
  var bL=document.getElementById("toggleLeft"), bR=document.getElementById("toggleRight");
  // Knopffarbe: Panel offen = orange (Klasse is-open), zu = Grundfarbe; aria-pressed folgt „offen".
  function mark(btn,open){ if(btn){ btn.classList.toggle("is-open",!!open); btn.setAttribute("aria-pressed",open?"true":"false"); } }
  function L(k){ try{ return localStorage.getItem(k)==="1"; }catch(e){ return false; } }
  function S(k,v){ try{ localStorage.setItem(k,v?"1":"0"); }catch(e){} }
  // Ist der Themenbaum sichtbar? Mobil ist er ein Overlay, sonst eine Spalte.
  function leftOpen(){
    return mq.matches ? !!(side&&side.classList.contains("open")) : !layout.classList.contains("hide-left"); }
  // Rechts (Gliederung): nur am Desktop sinnvoll, Zustand merken.
  if(bR){ if(L("wissen-hide-right")) layout.classList.add("hide-right");
    mark(bR,!layout.classList.contains("hide-right"));
    bR.addEventListener("click",function(){ var hidden=layout.classList.toggle("hide-right"); mark(bR,!hidden); S("wissen-hide-right",hidden); }); }
  // Links (Themenbaum): Desktop = beim Öffnen IMMER eingeklappt (Toggle gilt nur für die aktuelle Seite); Mobil = Overlay auf/zu.
  if(bL){ if(!mq.matches) layout.classList.add("hide-left");
    mark(bL,leftOpen());
    bL.addEventListener("click",function(){
      if(mq.matches){ if(side) side.classList.toggle("open"); }
      else layout.classList.toggle("hide-left");
      mark(bL,leftOpen());
    });
  }
  // Breitenwechsel aufräumen: Overlay nur mobil, am Desktop wieder eingeklappt.
  (mq.addEventListener?mq.addEventListener.bind(mq,"change"):mq.addListener.bind(mq))(function(e){
    if(e.matches) layout.classList.remove("hide-left");
    else { if(side) side.classList.remove("open"); layout.classList.add("hide-left"); }
    mark(bL,leftOpen());
  });
})();
// KaTeX automatisch rendern; zu breite abgesetzte Formeln danach passend verkleinern (höchstens auf 70 %),
// statt sie abzuschneiden – wichtig auf dem Handy.
(function(){
  function fitMath(){
    var ds=[].slice.call(document.querySelectorAll(".katex-display"));
    ds.forEach(function(d){ d.style.fontSize=""; });
    for(var pass=0;pass<2;pass++){                               // zweiter Durchgang: Skalierung ist nicht ganz linear
      var m=ds.map(function(d){ return [d.clientWidth,d.scrollWidth,parseFloat(getComputedStyle(d).fontSize)]; });
      ds.forEach(function(d,i){ var w=m[i][0],s=m[i][1];          // w=0: eingeklappte Herleitung -> beim Aufklappen
        if(w && s>w+1) d.style.fontSize=(m[i][2]*Math.max(0.7,w/s))+"px"; });
    }
  }
  var t=null; function later(){ clearTimeout(t); t=setTimeout(fitMath,120); }
  window.addEventListener("DOMContentLoaded",function(){
    if(window.renderMathInElement) renderMathInElement(document.body,{delimiters:[
      {left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}],strict:false});
    fitMath();
  });
  window.addEventListener("resize",later);
  window.addEventListener("load",fitMath);
  document.addEventListener("toggle",later,true);                  // Herleitung aufgeklappt -> Formeln darin einpassen
})();
/* Fassung (kompakt | ausführlich): Wahl merken; Themen-Links (Baum, Nachbarn, Übersicht) führen dann zur gewählten
   Fassung desselben Themas, soweit es sie gibt (data-alt). */
(function(){
  function get(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
  function set(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  document.addEventListener("click",function(ev){
    var f=ev.target.closest&&ev.target.closest(".fassung .f-btn");
    if(f) set("wissen-fassung",f.getAttribute("data-fassung"));
  });
  function apply(){
    if(get("wissen-fassung")!=="ausfuehrlich") return;
    document.querySelectorAll("a[data-alt]").forEach(function(a){ a.setAttribute("href",a.getAttribute("data-alt")); });
  }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",apply); else apply();
})();
