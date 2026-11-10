
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
// Sprung auf einen Anker in einem zugeklappten Kasten (Beispiel, Hintergrund, Herleitung, Lösung …): erst alle umgebenden
// Kästen aufklappen, dann hinscrollen. Gilt für Adressen mit #anker (Link aus einem anderen Artikel, Lesezeichen), für Links
// innerhalb der Seite und für einen zweiten Klick auf denselben Anker (dann gibt es kein hashchange).
(function(){
  var start=null;                                                  // beim Laden aufgeklapptes Ziel
  function zeige(id, immer){
    if(!id) return null;
    try{ id=decodeURIComponent(id); }catch(e){}
    var el=document.getElementById(id); if(!el) return null;
    var auf=false;
    for(var d=el.parentElement; d; d=d.parentElement){ if(d.tagName==="DETAILS" && !d.open){ d.open=true; auf=true; } }
    if(auf || immer) el.scrollIntoView();
    return auf ? el : null;
  }
  window.addEventListener("hashchange", function(){ zeige(location.hash.slice(1), false); });
  document.addEventListener("click", function(e){
    var a=e.target.closest && e.target.closest('a[href*="#"]'); if(!a) return;
    var u=new URL(a.href, location.href);
    if(u.pathname===location.pathname && u.hash && u.hash===location.hash) zeige(u.hash.slice(1), true);
  });
  function beimLaden(){ start=zeige(location.hash.slice(1), false); }
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded", beimLaden); else beimLaden();
  window.addEventListener("load", function(){ if(start) start.scrollIntoView(); });   // nach KaTeX und Bildern stimmt die Lage erst ganz
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
/* Animierte Abbildungen: figure.abb[data-anim] = Adresse der Datei <szene>.anim.svg (tools/szenen_animation.py). Sie ist
   das Endbild plus Datenblock <metadata class="szenen-animation">; der Spieler setzt sie an die Stelle des Bilds und
   bewegt die Elemente mit data-a. Start, wenn die Abbildung ins Bild kommt (in zugeklappten Kästen also erst beim
   Aufklappen), Halt, wenn sie es verlässt; bei „Bewegung reduzieren“ kein Selbststart (Endbild). Ohne Skript, ohne
   Datei oder bei einem Fehler bleibt das statische Bild. */
(function(){
  var figs=[].slice.call(document.querySelectorAll("figure.abb[data-anim]"));
  if(!figs.length || !window.fetch || !window.DOMParser || !window.IntersectionObserver) return;
  var L=(document.documentElement.lang||"de").slice(0,2);
  var TX={de:{play:"Abspielen",pause:"Anhalten",neu:"Von vorn",zur:"Schritt zurück",vor:"Schritt vor",zeit:"Zeitleiste der Animation",von:"von",anim:"Animation"},
    en:{play:"Play",pause:"Pause",neu:"Restart",zur:"Previous step",vor:"Next step",zeit:"Animation timeline",von:"of",anim:"Animation"},
    es:{play:"Reproducir",pause:"Pausa",neu:"Reiniciar",zur:"Paso anterior",vor:"Paso siguiente",zeit:"Línea de tiempo de la animación",von:"de",anim:"Animación"},
    zh:{play:"播放",pause:"暂停",neu:"重新开始",zur:"上一步",vor:"下一步",zeit:"动画时间轴",von:"/",anim:"动画"},
    fr:{play:"Lire",pause:"Pause",neu:"Recommencer",zur:"Étape précédente",vor:"Étape suivante",zeit:"Chronologie de l’animation",von:"sur",anim:"Animation"},
    tr:{play:"Oynat",pause:"Duraklat",neu:"Baştan başlat",zur:"Önceki adım",vor:"Sonraki adım",zeit:"Animasyon zaman çizelgesi",von:"/",anim:"Animasyon"}};
  var tx=TX[L]||TX.en;
  var reduce=window.matchMedia?window.matchMedia("(prefers-reduced-motion: reduce)"):{matches:false};
  var ICON={play:'<path d="M5 3.5v13l11-6.5z"/>',pause:'<path d="M4.5 3.5h4v13h-4zM11.5 3.5h4v13h-4z"/>',
    neu:'<path d="M10 3.2a6.8 6.8 0 1 1-6.6 8.4h2.1A4.8 4.8 0 1 0 10 5.2v2.6L5.8 4.2 10 .6z"/>',
    zur:'<path d="M3.5 3.5h2.2v13H3.5zM16.5 3.5v13L7 10z"/>',vor:'<path d="M14.3 3.5h2.2v13h-2.2zM3.5 3.5v13L13 10z"/>'};
  function knopf(cls,ic,lab){ var b=document.createElement("button"); b.type="button"; b.className=cls; b.setAttribute("aria-label",lab); b.title=lab;
    b.innerHTML='<svg viewBox="0 0 20 20" aria-hidden="true">'+ICON[ic]+'</svg>'; return b; }
  function zahl(t){ var s=(Math.round(t*10)/10).toFixed(1); return (L==="en"||L==="zh")?s:s.replace(".",","); }
  // Wert einer Spur [k0,v0,k1,v1,…] im (gebrochenen) Bild f: Stufe = letzter Wert davor, sonst linear
  function such(tr,f){ var n=tr.length>>1, lo=0, hi=n-1;
    if(f<=tr[0]) return [0,0,0]; if(f>=tr[2*hi]) return [hi,hi,0];
    while(hi-lo>1){ var m=(lo+hi)>>1; if(tr[2*m]<=f) lo=m; else hi=m; }
    return [lo,hi,(f-tr[2*lo])/(tr[2*hi]-tr[2*lo])]; }
  function stufe(tr,f){ return tr[2*such(tr,f)[0]+1]; }
  function linear(tr,f){ var s=such(tr,f), a=tr[2*s[0]+1], b=tr[2*s[1]+1], w=s[2];
    if(typeof a==="number") return a+(b-a)*w;
    var o=[]; for(var i=0;i<a.length;i++) o.push(a[i]+(b[i]-a[i])*w); return o; }
  function r(v,n){ var p=Math.pow(10,n); return Math.round(v*p)/p; }
  function mische(a,b,w){ var o=new Array(a.length); for(var i=0;i<a.length;i++) o[i]=a[i]+(b[i]-a[i])*w; return o; }
  function pfad(v,qc){ var o="", i=0;                    // Bézier-Kette(n) wie engine/svg_painter: M p0 C p1 p2 p3 …
    for(var c=0;c<qc.length;c++){ var n=qc[c];
      if(n){ o+="M"+r(v[2*i],1)+" "+r(v[2*i+1],1);
        for(var k=1;k<n-2;k+=3){ var j=2*(i+k); o+="C"+r(v[j],1)+" "+r(v[j+1],1)+" "+r(v[j+2],1)+" "+r(v[j+3],1)+" "+r(v[j+4],1)+" "+r(v[j+5],1); } }
      i+=n; }
    return o; }
  function rgb(c){ return "rgb("+Math.round(c[0])+","+Math.round(c[1])+","+Math.round(c[2])+")"; }
  function setze(el,cache,name,v){ if(cache[name]===v) return; cache[name]=v; if(v===null) el.removeAttribute(name); else el.setAttribute(name,v); }
  function texte(el){ return el.tagName.toLowerCase()==="g"?[].slice.call(el.querySelectorAll("text")):[el]; }

  function Spieler(fig){
    this.fig=fig; this.img=fig.querySelector("img"); this.t=0; this.lauf=false; this.gestartet=false; this.nutzer=false; this.auto=false;
  }
  Spieler.prototype.laden=function(){
    var sp=this; if(sp.ladung) return sp.ladung;
    sp.ladung=fetch(sp.fig.getAttribute("data-anim")).then(function(r){ if(!r.ok) throw new Error(r.status); return r.text(); }).then(function(txt){
      var doc=new DOMParser().parseFromString(txt,"image/svg+xml"), svg=doc.documentElement;
      var meta=svg&&svg.getElementsByTagName("metadata")[0];
      if(!svg || svg.nodeName!=="svg" || !meta) throw new Error("kein animiertes SVG");
      var D=JSON.parse(meta.textContent); meta.parentNode.removeChild(meta);
      svg=document.importNode(svg,true);
      var w=svg.getAttribute("width"), h=svg.getAttribute("height");
      svg.setAttribute("class","abb-anim"); svg.setAttribute("role","img");
      svg.setAttribute("aria-label",(sp.img&&sp.img.getAttribute("alt"))||tx.anim);
      svg.style.aspectRatio=w+" / "+h;
      sp.D=D; sp.dauer=D.dauer; sp.N=D.bilder; sp.svg=svg; sp.el=[]; sp.cache=[];
      var nodes=svg.querySelectorAll("[data-a]");
      for(var i=0;i<nodes.length;i++){ var e=nodes[i], k=+e.getAttribute("data-a"); sp.el[k]=e; sp.cache[k]={};
        e._d0=e.getAttribute("d"); e._h0=e.innerHTML; }
      if(sp.img) sp.img.parentNode.replaceChild(svg,sp.img); else sp.fig.insertBefore(svg,sp.fig.firstChild);
      sp.leiste();
      sp.zeige(reduce.matches?sp.dauer:0);
      return sp;
    });
    sp.ladung.catch(function(){});                       // Fehler: das statische Bild bleibt stehen
    return sp.ladung;
  };
  Spieler.prototype.leiste=function(){
    var sp=this, bar=document.createElement("div"); bar.className="abb-spieler"; bar.setAttribute("role","group"); bar.setAttribute("aria-label",tx.anim);
    sp.bPlay=knopf("as-play","play",tx.play); sp.bNeu=knopf("as-neu","neu",tx.neu);
    bar.appendChild(sp.bPlay); bar.appendChild(sp.bNeu);
    var marken=(sp.D.marken||[]).filter(function(m){ return m>0 && m<sp.dauer; });
    sp.marken=marken;
    if(marken.length){ sp.bZur=knopf("as-zur","zur",tx.zur); sp.bVor=knopf("as-vor","vor",tx.vor); bar.appendChild(sp.bZur); bar.appendChild(sp.bVor); }
    var box=document.createElement("div"); box.className="as-leiste";
    var rg=document.createElement("input"); rg.type="range"; rg.min="0"; rg.max=String(sp.N); rg.step="1"; rg.value="0"; rg.setAttribute("aria-label",tx.zeit);
    box.appendChild(rg);
    marken.forEach(function(m){ var s=document.createElement("span"); s.className="as-marke"; s.style.left="calc(7px + (100% - 14px) * "+(m/sp.dauer).toFixed(4)+")"; box.appendChild(s); });
    bar.appendChild(box);
    sp.zeit=document.createElement("span"); sp.zeit.className="as-zeit"; sp.zeit.setAttribute("aria-hidden","true"); bar.appendChild(sp.zeit);
    sp.rg=rg; sp.svg.parentNode.insertBefore(bar,sp.svg.nextSibling);
    sp.bPlay.addEventListener("click",function(){ if(sp.lauf){ sp.nutzer=true; sp.halt(); } else { sp.nutzer=false; sp.spiel(sp.t>=sp.dauer-1e-3?0:sp.t); } });
    sp.bNeu.addEventListener("click",function(){ sp.nutzer=false; sp.spiel(0); });
    if(sp.bZur){
      sp.bZur.addEventListener("click",function(){ var z=0; for(var i=0;i<marken.length;i++) if(marken[i]<sp.t-0.15) z=marken[i]; sp.nutzer=true; sp.halt(); sp.zeige(z); });
      sp.bVor.addEventListener("click",function(){ var z=sp.dauer; for(var i=marken.length-1;i>=0;i--) if(marken[i]>sp.t+0.05) z=marken[i]; sp.nutzer=true; sp.halt(); sp.zeige(z); });
    }
    rg.addEventListener("input",function(){ sp.nutzer=true; sp.halt(); sp.zeige(sp.dauer*(+rg.value)/sp.N); });
  };
  Spieler.prototype.zeige=function(t){
    var sp=this; t=Math.max(0,Math.min(sp.dauer,t)); sp.t=t;
    var f=sp.N*t/sp.dauer, data=sp.D.el;
    for(var k=0;k<data.length;k++){
      var e=sp.el[k], tr=data[k], c=sp.cache[k]; if(!e) continue;
      if(tr.v) setze(e,c,"display",stufe(tr.v,f)?null:"none");
      if(tr.h){ var hh=stufe(tr.h,f); if(c.h!==hh){ c.h=hh; e.innerHTML=hh===null?e._h0:hh; c.fo=c.fc=undefined; c.kinder=null; } }
      if(tr.d){ var d=stufe(tr.d,f); setze(e,c,"d",d===null?e._d0:d); }
      if(tr.q){ var s=such(tr.q,f), qa=tr.q[2*s[0]+1], qb=tr.q[2*s[1]+1];   // Punkte wandern (Umformen): linear
        setze(e,c,"d",qa===null?e._d0:pfad((qb===null||s[2]===0)?qa:mische(qa,qb,s[2]),tr.qc)); }
      if(tr.m){ var m=linear(tr.m,f);
        setze(e,c,"transform",(Math.abs(m[0]-1)+Math.abs(m[1])+Math.abs(m[2])+Math.abs(m[3]-1)+Math.abs(m[4])+Math.abs(m[5])<1e-4)?null:
          "matrix("+r(m[0],4)+" "+r(m[1],4)+" "+r(m[2],4)+" "+r(m[3],4)+" "+r(m[4],2)+" "+r(m[5],2)+")"); }
      if(tr.p){ var p=linear(tr.p,f);
        setze(e,c,"stroke-dasharray",(p[0]<0.05&&p[1]>999.95)?null:(p[0]<0.05?r(p[1],2)+" 2000":"0 "+r(p[0],2)+" "+r(p[1],2)+" 2000")); }
      if(tr.so) setze(e,c,"stroke-opacity",String(r(linear(tr.so,f),3)));
      if(tr.sw) setze(e,c,"stroke-width",String(r(linear(tr.sw,f),2)));
      if(tr.sc) setze(e,c,"stroke",rgb(linear(tr.sc,f)));
      if(tr.fo||tr.fc){
        var ziele=(e.tagName.toLowerCase()==="g")?(c.kinder||(c.kinder=texte(e))):[e];
        var fo=tr.fo?String(r(linear(tr.fo,f),3)):null, fc=tr.fc?rgb(linear(tr.fc,f)):null;
        for(var j=0;j<ziele.length;j++){ var cc=ziele[j]===e?c:(ziele[j]._c||(ziele[j]._c={}));
          if(fo!==null) setze(ziele[j],cc,"fill-opacity",fo); if(fc!==null) setze(ziele[j],cc,"fill",fc); }
      }
    }
    if(sp.rg){ sp.rg.value=String(Math.round(f)); sp.rg.style.setProperty("--as-p",(100*t/sp.dauer).toFixed(2)+"%");
      var txt=zahl(t)+" "+tx.von+" "+zahl(sp.dauer)+" s"; sp.rg.setAttribute("aria-valuetext",txt); sp.zeit.textContent=zahl(t)+" / "+zahl(sp.dauer)+" s"; }
  };
  Spieler.prototype.spiel=function(ab){
    var sp=this; if(!sp.D) return;
    if(ab!=null) sp.zeige(ab);
    sp.lauf=true; sp.gestartet=true; sp.auto=false; sp.knopf();
    var t0=performance.now(), s0=sp.t;
    function tick(now){ if(!sp.lauf) return;
      var t=s0+(now-t0)/1000; if(t>=sp.dauer){ sp.zeige(sp.dauer); sp.lauf=false; sp.knopf(); return; }
      sp.zeige(t); sp.raf=requestAnimationFrame(tick); }
    sp.raf=requestAnimationFrame(tick);
  };
  Spieler.prototype.halt=function(){ this.lauf=false; if(this.raf) cancelAnimationFrame(this.raf); this.knopf(); };
  Spieler.prototype.knopf=function(){ var b=this.bPlay; if(!b) return; var l=this.lauf?tx.pause:tx.play;
    b.setAttribute("aria-label",l); b.title=l; b.innerHTML='<svg viewBox="0 0 20 20" aria-hidden="true">'+ICON[this.lauf?"pause":"play"]+'</svg>'; };
  Spieler.prototype.sichtbar=function(ja){
    var sp=this; if(!sp.D) return; sp.imBild=ja;
    if(ja){ if(reduce.matches || sp.nutzer || document.hidden) return;
      if(!sp.gestartet) sp.spiel(0); else if(sp.auto){ sp.spiel(); } }
    else if(sp.lauf){ sp.halt(); sp.auto=true; }
  };
  var spieler=figs.map(function(f){ return new Spieler(f); });
  var nah=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ var sp=e.target._sp; nah.unobserve(e.target);
      sp.laden().then(function(){ seh.observe(sp.fig); }); } }); },{rootMargin:"400px 0px"});
  var seh=new IntersectionObserver(function(es){ es.forEach(function(e){ e.target._sp.sichtbar(e.isIntersecting && e.intersectionRatio>=0.35); }); },{threshold:[0,0.35,0.6]});
  spieler.forEach(function(sp){ sp.fig._sp=sp; nah.observe(sp.fig); });
  document.addEventListener("visibilitychange",function(){ spieler.forEach(function(sp){        // Tab im Hintergrund: anhalten
    if(document.hidden){ if(sp.lauf){ sp.halt(); sp.auto=true; } } else if(sp.imBild) sp.sichtbar(true); }); });
})();
