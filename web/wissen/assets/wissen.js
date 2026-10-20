
// Suche: vorab gebauter Index (search.json), Teilwort-/Infix-Treffer, umlaut-/ß-tolerant, gerankt + hervorgehoben.
(function(){
  var overlay=document.getElementById("searchOverlay"), input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"), btn=document.getElementById("searchBtn");
  var DOCS=null, sel=-1, rows=[];
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").normalize("NFKD").replace(/[̀-ͯ]/g,""); }
  function load(){ if(DOCS) return Promise.resolve(DOCS);
    return fetch("/wissen/data/search.json").then(function(r){return r.json();}).then(function(d){DOCS=d;return d;}).catch(function(){DOCS=[];return [];}); }
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
    if(!rows.length) results.innerHTML='<div class="searchHint">Nichts gefunden für „'+esc(raw.trim())+'".</div>';
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
  function mark(btn,on){ if(btn){ btn.classList.toggle("off",!!on); btn.setAttribute("aria-pressed",on?"true":"false"); } }
  function L(k){ try{ return localStorage.getItem(k)==="1"; }catch(e){ return false; } }
  function S(k,v){ try{ localStorage.setItem(k,v?"1":"0"); }catch(e){} }
  // Rechts (Gliederung): nur am Desktop sinnvoll, Zustand merken.
  if(bR){ if(L("wissen-hide-right")){ layout.classList.add("hide-right"); mark(bR,true); }
    bR.addEventListener("click",function(){ var now=layout.classList.toggle("hide-right"); mark(bR,now); S("wissen-hide-right",now); }); }
  // Links (Themenbaum): Desktop = beim Öffnen IMMER eingeklappt (Toggle gilt nur für die aktuelle Seite); Mobil = Overlay auf/zu.
  if(bL){ if(!mq.matches){ layout.classList.add("hide-left"); mark(bL,true); }
    bL.addEventListener("click",function(){
      var split=root.classList.contains("bsp-on")&&layout.classList.contains("has-bsp");   // geteilte Ansicht: Baum als Overlay
      if(mq.matches||split){ var o=side&&side.classList.toggle("open"); mark(bL,mq.matches?!!o:!o); }
      else { var now=layout.classList.toggle("hide-left"); mark(bL,now); }
    }); }
  // Breitenwechsel aufräumen: Overlay nur mobil, am Desktop wieder eingeklappt.
  (mq.addEventListener?mq.addEventListener.bind(mq,"change"):mq.addListener.bind(mq))(function(e){
    if(e.matches){ layout.classList.remove("hide-left"); mark(bL, side&&side.classList.contains("open")); }
    else { if(side) side.classList.remove("open"); layout.classList.add("hide-left"); mark(bL,true); }
  });
})();
// Beispiel-Seite (geteilte Ansicht): Theorie links, Beispiele rechts. Beide Spalten laufen synchron – jedes Beispiel
// steht auf Höhe der Formel, zu der es gehört (Bezugslinie bei 35 % der Fensterhöhe, dazwischen linear überblendet).
// Zu schmale Fenster: Die Beispiel-Seite legt sich als Ebene über den Artikel.
(function(){
  var root=document.documentElement, btn=document.getElementById("toggleBsp"),
      layout=document.querySelector(".layout.has-bsp"), pane=document.getElementById("bspPane");
  if(!btn) return;
  if(!layout||!pane){ root.classList.remove("bsp-on"); return; }
  var wide=window.matchMedia("(min-width:1180px)"), REF=0.35;
  var refs=[].slice.call(document.querySelectorAll(".bsp-ref[data-bsp]"));
  var cards=refs.map(function(r){ return document.getElementById("bsp-"+r.getAttribute("data-bsp")); });
  function isOn(){ return root.classList.contains("bsp-on"); }
  function paint(){ var v=isOn(); btn.classList.toggle("on",v); btn.setAttribute("aria-pressed",v?"true":"false"); }
  function set(v,remember){
    root.classList.toggle("bsp-on",v); paint();
    var sd=layout.querySelector(".side"), bL=document.getElementById("toggleLeft");
    if(sd && !window.matchMedia("(max-width:720px)").matches && sd.classList.contains("open")){
      sd.classList.remove("open"); if(bL){ bL.classList.add("off"); bL.setAttribute("aria-pressed","true"); } }
    if(remember && wide.matches){ try{ localStorage.setItem("wissen-split",v?"1":"0"); }catch(e){} }
    try{ document.dispatchEvent(new Event("wissen:layout")); }catch(e){}   // Spaltenbreite geändert -> Formeln neu einpassen
    if(v) requestAnimationFrame(sync);
  }
  function anchorEl(r){ return r.previousElementSibling || r; }     // Formel/Aussage direkt vor dem Verweis
  function sync(){
    if(!isOn() || !wide.matches || !refs.length) return;
    var ref=window.innerHeight*REF, k=-1, A=[], P=[];
    for(var i=0;i<refs.length;i++){ A.push(anchorEl(refs[i]).getBoundingClientRect().top); P.push(cards[i].offsetTop); if(A[i]<=ref) k=i; }
    var p;                                                       // Stelle der Beispiel-Seite, die auf die Bezugslinie gehört
    if(k<0) p=P[0]-(A[0]-ref);
    else if(k===refs.length-1) p=P[k]+(ref-A[k]);
    else { var t=(ref-A[k])/Math.max(1,A[k+1]-A[k]); p=P[k]+t*(P[k+1]-P[k]); }
    pane.scrollTop=p-(ref-pane.getBoundingClientRect().top);
  }
  var tick=false;
  function later(){ if(tick) return; tick=true; requestAnimationFrame(function(){ tick=false; sync(); }); }
  window.addEventListener("scroll",later,{passive:true});
  window.addEventListener("resize",later);
  window.addEventListener("load",later);                          // nach Schriften/KaTeX noch einmal ausrichten
  document.addEventListener("toggle",later,true);                 // Herleitung auf-/zugeklappt -> Höhen ändern sich
  document.addEventListener("wissen:fitted",later);               // Formeln eingepasst -> Höhen ändern sich
  function flash(c){ if(!c) return; c.classList.remove("flash"); void c.offsetWidth; c.classList.add("flash");
    setTimeout(function(){ c.classList.remove("flash"); },1600); }
  function toAnchor(i){                                          // Artikel so scrollen, dass die Formel auf der Bezugslinie steht
    var y=window.scrollY+anchorEl(refs[i]).getBoundingClientRect().top-window.innerHeight*REF;
    window.scrollTo({top:Math.max(0,y),behavior:"smooth"});
  }
  refs.forEach(function(r,i){ var a=r.querySelector("a"); if(!a) return;
    a.addEventListener("click",function(e){ e.preventDefault(); if(!isOn()) set(true,true);
      requestAnimationFrame(function(){ if(wide.matches){ toAnchor(i); sync(); } else { pane.scrollTop=cards[i].offsetTop-12; } flash(cards[i]); });
    }); });
  [].slice.call(pane.querySelectorAll(".bsp-back")).forEach(function(a){
    a.addEventListener("click",function(e){ e.preventDefault();
      var i=refs.indexOf(document.getElementById("bspref-"+a.getAttribute("data-bsp"))); if(i<0) return;
      if(!wide.matches) set(false,false);
      requestAnimationFrame(function(){ toAnchor(i); });
    }); });
  btn.addEventListener("click",function(){ set(!isOn(),true); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape" && isOn() && !wide.matches) set(false,false); });
  (wide.addEventListener?wide.addEventListener.bind(wide,"change"):wide.addListener.bind(wide))(function(e){
    if(!e.matches){ set(false,false); }
    else { var st=false; try{ st=localStorage.getItem("wissen-split")==="1"; }catch(x){} set(st,false); }
  });
  paint(); if(isOn()) requestAnimationFrame(sync);
})();
// KaTeX automatisch rendern; zu breite abgesetzte Formeln danach passend verkleinern (höchstens auf 70 %),
// statt sie abzuschneiden – wichtig in der geteilten Ansicht und auf dem Handy.
(function(){
  function fitMath(){
    var ds=[].slice.call(document.querySelectorAll(".katex-display"));
    ds.forEach(function(d){ d.style.fontSize=""; });
    for(var pass=0;pass<2;pass++){                               // zweiter Durchgang: Skalierung ist nicht ganz linear
      var m=ds.map(function(d){ return [d.clientWidth,d.scrollWidth,parseFloat(getComputedStyle(d).fontSize)]; });
      ds.forEach(function(d,i){ var w=m[i][0],s=m[i][1];          // w=0: eingeklappte Herleitung -> beim Aufklappen
        if(w && s>w+1) d.style.fontSize=(m[i][2]*Math.max(0.7,w/s))+"px"; });
    }
    try{ document.dispatchEvent(new Event("wissen:fitted")); }catch(e){}   // Höhen haben sich geändert -> Beispiele neu ausrichten
  }
  var t=null; function later(){ clearTimeout(t); t=setTimeout(fitMath,120); }
  window.addEventListener("DOMContentLoaded",function(){
    if(window.renderMathInElement) renderMathInElement(document.body,{delimiters:[
      {left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}]});
    fitMath();
  });
  window.addEventListener("resize",later);
  window.addEventListener("load",fitMath);
  document.addEventListener("toggle",later,true);                  // Herleitung aufgeklappt -> Formeln darin einpassen
  document.addEventListener("wissen:layout",later);               // geteilte Ansicht an/aus
})();
