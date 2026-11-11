
var NICHTS={de:"Nichts gefunden für „{q}\".",en:"Nothing found for „{q}\".",es:"Nada encontrado para „{q}\".",zh:"未找到 „{q}\".",
            fr:"Aucun résultat pour «\u00a0{q}\u00a0».",tr:"“{q}” için sonuç bulunamadı."};
// Suche: Teilwort-/Infix-Treffer, umlaut-/ß-tolerant, gerankt + hervorgehoben. Der Kern steht in suche.js (W3a, gemeinsam
// mit der Startseite) und wird erst beim ersten Öffnen geladen; er holt zuerst nur Titel und Abschnitte, den Volltext je
// Modul, sobald gesucht wird (und nur Module, die das Wort enthalten können).
var KATEX_OPT={delimiters:[{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}],strict:false,ignoredClasses:["fb-spaeter","mathe-spaeter"]};   // Formelblatt (W4a): erst beim Öffnen setzen
function mathe(el){ if(window.renderMathInElement) try{ renderMathInElement(el,KATEX_OPT); }catch(e){} }
(function(){
  var overlay=document.getElementById("searchOverlay"), input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"), btn=document.getElementById("searchBtn");
  var S=null, P=null, sel=-1, rows=[], frage="";
  var LANG=(document.documentElement.lang||"de").slice(0,2);
  function kern(){                                     // suche.js einmal einbinden, Index starten
    if(!P) P=new Promise(function(ok,nein){
      if(window.ETSuche){ ok(); return; }
      var s=document.createElement("script"); s.src="/wissen/assets/suche.js?v=c4d05471b2"; s.onload=ok; s.onerror=nein; document.head.appendChild(s);
    }).then(function(){ S=window.ETSuche(LANG); return S.start(); }).catch(function(){ P=null; throw 0; });
    return P;
  }
  function esc(s){ return (s||"").replace(/[&<>]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;"}[c];}); }
  function zeigen(raw,res){
    if(raw!==frage) return;                            // inzwischen anders getippt
    results.innerHTML=""; rows=[];
    if(res.q.length<2) return;
    res.hits.slice(0,25).forEach(function(h){ var d=h.d;
      var a=document.createElement("a"); a.href="/wissen/"+d.path+(h.anker?"#"+encodeURIComponent(h.anker):"");
      a.innerHTML='<div class="r-crumb">'+esc(d.crumb)+(h.abschnitt?' › <span class="r-abschnitt">'+esc(h.abschnitt)+'</span>':"")+'</div>'+
                  '<div class="r-title">'+esc(d.klar)+'</div>'+
                  '<div class="r-snip">'+S.snippet(d,res.q)+'</div>';
      results.appendChild(a); rows.push(a);
    });
    if(sel>=rows.length) sel=rows.length-1;
    paintSel();
    if(res.laedt){ var w=document.createElement("div"); w.className="searchHint laedt"; w.textContent=LERNEN.w("suche_volltext"); results.appendChild(w); }
    else if(!rows.length) results.innerHTML='<div class="searchHint">'+esc(NICHTS[LANG]||NICHTS.de).split("{q}").join(esc(raw.trim()))+'</div>';
  }
  function search(raw){
    frage=raw; sel=-1;
    if(S && S.fold(raw.trim()).length<2){ results.innerHTML=""; rows=[]; return; }
    kern().then(function(){ S.suche(raw,function(res){ zeigen(raw,res); }); }).catch(function(){});
  }
  function open(){ if(!overlay) return; overlay.hidden=false; input.value=""; results.innerHTML=""; rows=[]; sel=-1; input.focus();
    kern().catch(function(){}); }
  function close(){ if(overlay) overlay.hidden=true; }
  if(btn) btn.addEventListener("click",open);
  [].forEach.call(document.querySelectorAll("[data-suche]"),function(b){ b.hidden=false; b.addEventListener("click",open); });
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
  // W4b: „Hell/Dunkel“ im Bereichsmenü (nur sehr schmale Artikelseiten, dort fehlt der Knopf in der Leiste)
  [].forEach.call(document.querySelectorAll(".b-thema-b"),function(b){ b.addEventListener("click",function(){
    var t=document.getElementById("themeBtn"); if(t) t.click(); menus.forEach(function(m){ close(m,false); }); }); });
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
  // Ohne eigene Wahl folgt die Seite der Systemeinstellung (der Kopf setzt sie beim Laden), auch wenn sie sich ändert.
  var sys=window.matchMedia?window.matchMedia("(prefers-color-scheme: dark)"):null;
  function folge(e){ var s=null; try{ s=localStorage.getItem("animate-theme"); }catch(x){} if(s) return;
    if(e.matches) root.setAttribute("data-theme","dark"); else root.removeAttribute("data-theme"); }
  if(sys){ if(sys.addEventListener) sys.addEventListener("change",folge); else if(sys.addListener) sys.addListener(folge); }
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
    var auf=false, A=window.ETAnsicht;                             // W4a: Ziel in der gewählten Ansicht versteckt -> „Ausführlich“
    if(A && id==="formelblatt"){ if(A.jetzt()!=="formeln"){ A.setze("formeln",false); auf=true; } }
    else if(A && id==="kurzfassung"){ if(A.jetzt()!=="kurz"){ A.setze("kurz",false); auf=true; } }
    else if(A && A.verborgen(el)){ A.setze("voll",false); auf=true; }
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
    if(window.renderMathInElement) renderMathInElement(document.body,KATEX_OPT);
    fitMath();
  });
  window.addEventListener("resize",later);
  window.addEventListener("load",fitMath);
  document.addEventListener("toggle",later,true);                  // Herleitung aufgeklappt -> Formeln darin einpassen
})();
// Kopierknopf an Code-Blöcken (Konsole: nur die Eingaben, ohne Prompt), Ankerlink an Überschriften (Klick kopiert die
// Adresse des Abschnitts), Druck: zugeklappte Kästen aufklappen und danach wieder schließen (Lösungen bleiben zu).
(function(){
  var L=(document.documentElement.lang||"de").slice(0,2);
  var W={de:{k:"Kopieren",ok:"Kopiert",link:"Link kopiert"},en:{k:"Copy",ok:"Copied",link:"Link copied"},
    es:{k:"Copiar",ok:"Copiado",link:"Enlace copiado"},zh:{k:"复制",ok:"已复制",link:"链接已复制"},
    fr:{k:"Copier",ok:"Copié",link:"Lien copié"},tr:{k:"Kopyala",ok:"Kopyalandı",link:"Bağlantı kopyalandı"}};
  var w=W[L]||W.en;
  function kopiere(text){
    if(navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function(ok,fehler){ var t=document.createElement("textarea"); t.value=text; t.setAttribute("readonly","");
      t.style.position="fixed"; t.style.opacity="0"; document.body.appendChild(t); t.select();
      try{ if(document.execCommand("copy")) ok(); else fehler(); }catch(e){ fehler(e); } document.body.removeChild(t); });
  }
  function codeText(block){
    var c=block.querySelector("pre code"), t=c?c.textContent:"";
    if(/\bcode-console\b/.test(block.className)){                  // Sitzung: Eingabezeilen ohne $, #, >>>, ..., PS>
      var ein=[]; t.split("\n").forEach(function(z){ var m=/^(?:\$ |# |>>> |\.\.\. |PS> )(.*)$/.exec(z); if(m) ein.push(m[1]); });
      if(ein.length) return ein.join("\n");
    }
    return t.replace(/\n+$/,"");
  }
  [].forEach.call(document.querySelectorAll(".code-block"),function(block){
    var b=document.createElement("button"); b.type="button"; b.className="code-kopie"; b.textContent=w.k;
    var kopf=block.querySelector(".code-kopf"); if(kopf) kopf.appendChild(b); else block.insertBefore(b,block.firstChild);
    b.addEventListener("click",function(){ kopiere(codeText(block)).then(function(){ b.textContent=w.ok; b.classList.add("ok");
      setTimeout(function(){ b.textContent=w.k; b.classList.remove("ok"); },1600); },function(){}); });
  });
  document.addEventListener("click",function(e){
    var a=e.target.closest && e.target.closest("a.h-anker"); if(!a) return;
    kopiere(location.href.split("#")[0]+a.getAttribute("href")).then(function(){ a.setAttribute("data-kopiert",w.link); a.classList.add("kopiert");
      setTimeout(function(){ a.classList.remove("kopiert"); },1800); },function(){});
  });
  var zu=[];
  window.addEventListener("beforeprint",function(){
    zu=[].filter.call(document.querySelectorAll("details:not([open])"),function(d){ return !d.classList.contains("loesung") && !d.closest(".side"); });
    zu.forEach(function(d){ d.open=true; });
  });
  window.addEventListener("afterprint",function(){ zu.forEach(function(d){ d.open=false; }); zu=[]; });
})();
// Abbildung antippen: groß in einem Overlay mit voller Breite. Das Bild bzw. die animierte Fassung samt Spielerleiste wandert
// hinein und beim Schließen zurück an ihren Platz, so laufen Animation und Knöpfe weiter. Schließen: Klick (außer auf den
// Spieler), Esc, Knopf oder Zurück im Browser. Mit der Tastatur: Bild fokussieren (Tab), Enter oder Leertaste.
(function(){
  if(!document.querySelector("figure.abb")) return;
  var L=(document.documentElement.lang||"de").slice(0,2);
  var W={de:["Abbildung vergrößern","Schließen"],en:["Enlarge figure","Close"],es:["Ampliar figura","Cerrar"],zh:["放大图","关闭"],
    fr:["Agrandir la figure","Fermer"],tr:["Şekli büyüt","Kapat"]};
  var w=W[L]||W.en, SEL="figure.abb>img,figure.abb>svg.abb-anim";
  var ov=null, buehne=null, text=null, zuBtn=null, fig=null, platz=null, verlauf=false;
  window.abbVergroesserbar=function(m){ m.setAttribute("tabindex","0"); if(!m.getAttribute("title")) m.setAttribute("title",w[0]); };
  [].forEach.call(document.querySelectorAll(SEL),window.abbVergroesserbar);
  function bauen(){
    ov=document.createElement("div"); ov.className="abb-gross"; ov.hidden=true; ov.setAttribute("role","dialog"); ov.setAttribute("aria-modal","true");
    zuBtn=document.createElement("button"); zuBtn.type="button"; zuBtn.className="ag-zu"; zuBtn.setAttribute("aria-label",w[1]); zuBtn.title=w[1];
    zuBtn.innerHTML='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>';
    buehne=document.createElement("div"); buehne.className="ag-buehne";
    text=document.createElement("div"); text.className="ag-text";
    ov.appendChild(zuBtn); ov.appendChild(buehne); ov.appendChild(text); document.body.appendChild(ov);
    ov.addEventListener("click",function(e){ if(e.target.closest(".abb-spieler")) return; zu(); });
  }
  function auf(f){
    if(fig) return; if(!ov) bauen();
    var teile=[].filter.call(f.children,function(k){ return k.matches(SEL) || k.classList.contains("abb-spieler"); });
    if(!teile.length) return;
    fig=f;
    platz=document.createElement("div"); platz.className="abb-platz";
    platz.style.height=teile.reduce(function(s,k){ return s+k.getBoundingClientRect().height; },0)+"px";
    f.insertBefore(platz,teile[0]);
    teile.forEach(function(k){ buehne.appendChild(k); });
    var cap=f.querySelector("figcaption"); text.innerHTML=cap?cap.innerHTML:"";
    ov.setAttribute("aria-label",(cap && cap.textContent.trim()) || w[0]);
    ov.hidden=false; document.documentElement.classList.add("abb-offen");
    try{ history.pushState({abbGross:1},""); verlauf=true; }catch(e){ verlauf=false; }
    zuBtn.focus();
  }
  function schliessen(){
    if(!fig) return;
    while(buehne.firstChild) fig.insertBefore(buehne.firstChild,platz);
    platz.parentNode.removeChild(platz);
    ov.hidden=true; document.documentElement.classList.remove("abb-offen"); text.innerHTML="";
    var m=fig.querySelector(SEL); fig=null; platz=null;
    if(m) try{ m.focus({preventScroll:true}); }catch(e){}
  }
  function zu(){ if(!fig) return; if(verlauf){ verlauf=false; history.back(); } else schliessen(); }
  window.addEventListener("popstate",function(){ if(fig){ verlauf=false; schliessen(); } });
  document.addEventListener("click",function(e){
    var m=e.target.closest && e.target.closest(SEL); if(!m || (ov && ov.contains(m))) return;
    auf(m.parentNode);
  });
  document.addEventListener("keydown",function(e){
    if(fig){
      if(e.key==="Escape"){ e.preventDefault(); zu(); }
      else if(e.key==="Tab"){                                    // Fokus bleibt im Overlay
        var f=[].slice.call(ov.querySelectorAll("button,input,a[href]")); if(!f.length) return;
        var i=f.indexOf(document.activeElement);
        if(e.shiftKey && i<=0){ e.preventDefault(); f[f.length-1].focus(); }
        else if(!e.shiftKey && (i<0 || i===f.length-1)){ e.preventDefault(); f[0].focus(); }
      }
      return;
    }
    var t=e.target; if(t && t.matches && t.matches(SEL) && (e.key==="Enter" || e.key===" ")){ e.preventDefault(); auf(t.parentNode); }
  });
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
  // Kamerafahrt in 3D (L4): Die Datei trägt je Element Weltpunkte (w; wl = nur Ecken gerader Stücke) und eine
  // Kamera-Spur cam [theta, phi, zoom, Blickpunkt]; projiziert wird wie engine/camera.py (z oben, orthografisch),
  // gezeichnet von hinten nach vorn wie engine/renderer (Tiefe = Mittel aller Punkte, Achsen bei top zuletzt).
  function kamera(c){ var ct=Math.cos(c[0]), st=Math.sin(c[0]), ce=Math.cos(c[1]), se=Math.sin(c[1]);
    var cam=[ce*ct,ce*st,se], fw=[-cam[0],-cam[1],-cam[2]], rt=[fw[1],-fw[0],0], n=Math.sqrt(rt[0]*rt[0]+rt[1]*rt[1]);
    rt=n>1e-9?[rt[0]/n,rt[1]/n,0]:[1,0,0];
    var up=[rt[1]*fw[2]-rt[2]*fw[1],rt[2]*fw[0]-rt[0]*fw[2],rt[0]*fw[1]-rt[1]*fw[0]], m=Math.sqrt(up[0]*up[0]+up[1]*up[1]+up[2]*up[2]);
    return {r:rt,u:[up[0]/m,up[1]/m,up[2]/m],c:cam,z:c[2],o:[c[3],c[4],c[5]]}; }
  function gerade(w){ var o=[w[0],w[1],w[2]];
    for(var i=3;i<w.length;i+=3){ for(var k=1;k<=3;k++){ var q=k/3; o.push(w[i-3]+(w[i]-w[i-3])*q,w[i-2]+(w[i+1]-w[i-2])*q,w[i-1]+(w[i+2]-w[i-1])*q); } }
    return o; }
  function punkte3(e,tr,f){ if(!e._w) e._w=tr.wl?gerade(tr.w):tr.w;
    if(tr.Q){ var s=such(tr.Q,f), a=tr.Q[2*s[0]+1], b=tr.Q[2*s[1]+1]; if(a===null) return e._w; if(b===null||s[2]===0) return a; return mische(a,b,s[2]); }
    if(tr.D){ var d=stufe(tr.D,f); return d===null?e._w:d; }
    return e._w; }
  function drehe(P,K){ var n=P.length/3-1, cx=P[3*n], cy=P[3*n+1], cz=P[3*n+2], o=new Array(3*n);   // bb: Scheibe zur Kamera
    for(var i=0;i<n;i++){ var dx=P[3*i]-cx, dy=P[3*i+1]-cy;
      o[3*i]=cx+dx*K.r[0]+dy*K.u[0]; o[3*i+1]=cy+dx*K.r[1]+dy*K.u[1]; o[3*i+2]=cz+dx*K.r[2]+dy*K.u[2]; }
    return o; }
  function projiziere(P,K,pj){ var n=P.length/3, o=new Array(2*n), s=K.z/pj[2], W2=pj[0]/2, H2=pj[1]/2, t=0;
    for(var i=0;i<n;i++){ var x=P[3*i]-K.o[0], y=P[3*i+1]-K.o[1], z=P[3*i+2]-K.o[2];
      o[2*i]=W2+(K.r[0]*x+K.r[1]*y+K.r[2]*z)*s; o[2*i+1]=H2-(K.u[0]*x+K.u[1]*y+K.u[2]*z)*s; t+=K.c[0]*x+K.c[1]*y+K.c[2]*z; }
    o.tiefe=n?t/n:0; return o; }

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
      if(window.abbVergroesserbar) window.abbVergroesserbar(svg);  // antippen zum Vergrößern wie beim Bild
      sp.leiste();
      sp.zeige(sp.dauer);                                // bis zum Abspielen das Endbild (kein fast leeres Startbild)
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
    var f=sp.N*t/sp.dauer, data=sp.D.el, K=sp.D.pj?kamera(linear(sp.D.cam,f)):null;
    for(var k=0;k<data.length;k++){
      var e=sp.el[k], tr=data[k], c=sp.cache[k]; if(!e) continue;
      if(tr.v) setze(e,c,"display",stufe(tr.v,f)?null:"none");
      if(tr.h){ var hh=stufe(tr.h,f); if(c.h!==hh){ c.h=hh; e.innerHTML=hh===null?e._h0:hh; c.fo=c.fc=undefined; c.kinder=null; } }
      if(K && tr.w){ var P3=punkte3(e,tr,f), o3=projiziere(tr.bb?drehe(P3,K):P3,K,sp.D.pj); e._tiefe=o3.tiefe;
        if(tr.b){ var s3=tr.s?linear(tr.s,f):1, x3=o3[0]-s3*tr.b[0], y3=o3[1]-s3*tr.b[1];
          setze(e,c,"transform",(Math.abs(s3-1)<1e-4&&Math.abs(x3)<0.005&&Math.abs(y3)<0.005)?null:
            "matrix("+r(s3,4)+" 0 0 "+r(s3,4)+" "+r(x3,2)+" "+r(y3,2)+")"); }
        else setze(e,c,"d",pfad(o3,(tr.wc&&!tr.D)?tr.wc:[o3.length>>1])); }
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
    if(K){ var top=sp.D.top, li=[];                     // Maler-Algorithmus: hinten zuerst, bei Gleichstand der Rang r
      for(var k2=0;k2<data.length;k2++) if(sp.el[k2]&&data[k2].w) li.push(k2);
      li.sort(function(a,b){ var A=data[a], B=data[b], ga=(top&&A.ax)?1:0, gb=(top&&B.ax)?1:0;
        if(ga!==gb) return ga-gb; if((A.ly||0)!==(B.ly||0)) return (A.ly||0)-(B.ly||0);
        var dd=sp.el[a]._tiefe-sp.el[b]._tiefe; return dd?dd:A.r-B.r; });
      var reihe=li.join(",");
      if(li.length && reihe!==sp.reihe){ sp.reihe=reihe; var par=sp.el[li[0]].parentNode;
        for(var i2=0;i2<li.length;i2++) par.appendChild(sp.el[li[i2]]); } }
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
  window.addEventListener("beforeprint",function(){ spieler.forEach(function(sp){ if(sp.D){ if(sp.lauf){ sp.halt(); sp.auto=true; } sp.zeige(sp.dauer); } }); });   // Druck: Endbild
})();
/* ---------- Lernen (W2, 11.11.2026): Lesefortschritt, Link-Vorschau, Selbsttest, Begriffe-Filter, Lernkarten ----------
   Alles bleibt in diesem Browser (localStorage), nichts wird übertragen. Ohne Speicher (privates Fenster, gesperrt) gilt
   es nur, solange die Seite offen ist; Fehler beim Lesen und Schreiben werden abgefangen. Wörter: _UI_LERNEN im Build. */
var LERNEN_UI={"de":{"bg_leer":"Kein Begriff passt.","bg_anzahl":"{n} Begriffe","lk_faellig":"Heute fällig: {n}","lk_davon_neu":"davon neu: {n}","lk_fertig":"Für heute ist in dieser Auswahl nichts mehr fällig.","lk_mehr_neu":"{n} weitere neue Karten","lk_begriff":"Begriff","lk_formel":"Formel","lk_luecke":"Lückentext","reset_sicher":"Wirklich zurücksetzen?","lk_heute":"gleich noch einmal","lk_morgen":"morgen","lk_tage":"in {n} Tagen","lk_ohne_speicher":"Dieser Browser speichert gerade nichts. Der Lernstand gilt nur, solange die Seite offen ist.","aufdecken":"Aufdecken","gelesen":"Gelesen","lf_kapitel":"{n} von {m} gelesen","lf_artikel":"Gelesen. In diesem Kapitel: {n} von {m}.","weiterlesen":"Weiterlesen","fs_reset":"Fortschritt zurücksetzen","fs_lokal":"Der Lesefortschritt bleibt nur in diesem Browser.","vs_oeffnen":"Öffnen","vs_schliessen":"Schließen","baum_laedt":"Wird geladen …","baum_fehler":"Konnte nicht geladen werden.","suche_volltext":"Volltext wird durchsucht …","begriffe":"Begriffe","lernkarten":"Lernkarten","ans_kurz_min":"Kurz: {n} min","dl_laeuft":"Wird erstellt …","dl_fehler":"Das Erstellen hat nicht geklappt.","dl_gross":"Zu lang für ein Bild. Wähle ein Kapitel oder nimm PDF.","fb_titel":"Formelsammlung","ans_formeln":"Formeln","fb_titel_ref":"Befehlsübersicht"},"en":{"bg_leer":"No term matches.","bg_anzahl":"{n} terms","lk_faellig":"Due today: {n}","lk_davon_neu":"new: {n}","lk_fertig":"Nothing more is due today in this selection.","lk_mehr_neu":"{n} more new cards","lk_begriff":"Term","lk_formel":"Formula","lk_luecke":"Fill in the blank","reset_sicher":"Really reset?","lk_heute":"again shortly","lk_morgen":"tomorrow","lk_tage":"in {n} days","lk_ohne_speicher":"This browser is not saving anything right now. Progress lasts only while the page is open.","aufdecken":"Reveal","gelesen":"Read","lf_kapitel":"{n} of {m} read","lf_artikel":"Read. In this chapter: {n} of {m}.","weiterlesen":"Continue reading","fs_reset":"Reset reading progress","fs_lokal":"Reading progress stays in this browser only.","vs_oeffnen":"Open","vs_schliessen":"Close","baum_laedt":"Loading …","baum_fehler":"Could not be loaded.","suche_volltext":"Searching the full text …","begriffe":"Glossary","lernkarten":"Flashcards","ans_kurz_min":"Short: {n} min","dl_laeuft":"Creating …","dl_fehler":"Creating the file did not work.","dl_gross":"Too long for one image. Choose a chapter or use PDF.","fb_titel":"Formula collection","ans_formeln":"Formulas","fb_titel_ref":"Command reference"},"es":{"bg_leer":"Ningún término coincide.","bg_anzahl":"{n} términos","lk_faellig":"Pendientes hoy: {n}","lk_davon_neu":"nuevas: {n}","lk_fertig":"Hoy no queda nada pendiente en esta selección.","lk_mehr_neu":"{n} tarjetas nuevas más","lk_begriff":"Término","lk_formel":"Fórmula","lk_luecke":"Completar","reset_sicher":"¿Reiniciar de verdad?","lk_heute":"otra vez enseguida","lk_morgen":"mañana","lk_tage":"en {n} días","lk_ohne_speicher":"Este navegador no guarda nada ahora mismo. El progreso solo dura mientras la página esté abierta.","aufdecken":"Descubrir","gelesen":"Leído","lf_kapitel":"{n} de {m} leídos","lf_artikel":"Leído. En este capítulo: {n} de {m}.","weiterlesen":"Seguir leyendo","fs_reset":"Reiniciar el progreso de lectura","fs_lokal":"El progreso de lectura se queda solo en este navegador.","vs_oeffnen":"Abrir","vs_schliessen":"Cerrar","baum_laedt":"Cargando …","baum_fehler":"No se pudo cargar.","suche_volltext":"Buscando en el texto completo …","begriffe":"Glosario","lernkarten":"Tarjetas de estudio","ans_kurz_min":"Breve: {n} min","dl_laeuft":"Creando …","dl_fehler":"No se pudo crear el archivo.","dl_gross":"Demasiado largo para una imagen. Elige un capítulo o usa PDF.","fb_titel":"Formulario","ans_formeln":"Fórmulas","fb_titel_ref":"Referencia de comandos"},"zh":{"bg_leer":"没有匹配的术语。","bg_anzahl":"共 {n} 个术语","lk_faellig":"今天到期：{n}","lk_davon_neu":"其中新卡：{n}","lk_fertig":"此范围内今天已没有到期的卡片。","lk_mehr_neu":"再学 {n} 张新卡","lk_begriff":"术语","lk_formel":"公式","lk_luecke":"填空","reset_sicher":"确定要重置吗？","lk_heute":"稍后再来一次","lk_morgen":"明天","lk_tage":"{n} 天后","lk_ohne_speicher":"此浏览器目前无法保存数据，学习进度只在页面打开期间有效。","aufdecken":"揭开","gelesen":"已读","lf_kapitel":"已读 {n} / {m}","lf_artikel":"已读。本章已读 {n} / {m}。","weiterlesen":"继续阅读","fs_reset":"重置阅读进度","fs_lokal":"阅读进度只保存在本浏览器中。","vs_oeffnen":"打开","vs_schliessen":"关闭","baum_laedt":"加载中 …","baum_fehler":"无法加载。","suche_volltext":"正在搜索全文 …","begriffe":"术语表","lernkarten":"学习卡片","ans_kurz_min":"简要：{n} 分钟","dl_laeuft":"正在生成 …","dl_fehler":"文件生成失败。","dl_gross":"内容太长，无法生成一张图片。请选择一章或使用 PDF。","fb_titel":"公式汇编","ans_formeln":"公式","fb_titel_ref":"命令速查"},"fr":{"bg_leer":"Aucun terme ne correspond.","bg_anzahl":"{n} termes","lk_faellig":"À revoir aujourd’hui : {n}","lk_davon_neu":"dont nouvelles : {n}","lk_fertig":"Plus rien à revoir aujourd’hui dans cette sélection.","lk_mehr_neu":"{n} nouvelles fiches de plus","lk_begriff":"Terme","lk_formel":"Formule","lk_luecke":"Texte à trous","reset_sicher":"Vraiment réinitialiser ?","lk_heute":"encore une fois tout de suite","lk_morgen":"demain","lk_tage":"dans {n} jours","lk_ohne_speicher":"Ce navigateur n’enregistre rien pour le moment. La progression ne dure que tant que la page est ouverte.","aufdecken":"Révéler","gelesen":"Lu","lf_kapitel":"{n} sur {m} lus","lf_artikel":"Lu. Dans ce chapitre : {n} sur {m}.","weiterlesen":"Reprendre la lecture","fs_reset":"Réinitialiser la progression de lecture","fs_lokal":"La progression de lecture reste uniquement dans ce navigateur.","vs_oeffnen":"Ouvrir","vs_schliessen":"Fermer","baum_laedt":"Chargement …","baum_fehler":"Chargement impossible.","suche_volltext":"Recherche dans le texte intégral …","begriffe":"Glossaire","lernkarten":"Fiches de révision","ans_kurz_min":"Court : {n} min","dl_laeuft":"Création …","dl_fehler":"La création du fichier a échoué.","dl_gross":"Trop long pour une image. Choisissez un chapitre ou utilisez le PDF.","fb_titel":"Formulaire","ans_formeln":"Formules","fb_titel_ref":"Aide-mémoire des commandes"},"tr":{"bg_leer":"Eşleşen terim yok.","bg_anzahl":"{n} terim","lk_faellig":"Bugün sırası gelen: {n}","lk_davon_neu":"yeni: {n}","lk_fertig":"Bu seçimde bugün için başka kart yok.","lk_mehr_neu":"{n} yeni kart daha","lk_begriff":"Terim","lk_formel":"Formül","lk_luecke":"Boşluk doldurma","reset_sicher":"Gerçekten sıfırlansın mı?","lk_heute":"birazdan tekrar","lk_morgen":"yarın","lk_tage":"{n} gün sonra","lk_ohne_speicher":"Bu tarayıcı şu anda hiçbir şey kaydetmiyor. İlerleme yalnızca sayfa açıkken geçerli.","aufdecken":"Aç","gelesen":"Okundu","lf_kapitel":"{m} makaleden {n} tanesi okundu","lf_artikel":"Okundu. Bu bölümde: {m} makaleden {n} tanesi.","weiterlesen":"Okumaya devam et","fs_reset":"Okuma ilerlemesini sıfırla","fs_lokal":"Okuma ilerlemesi yalnızca bu tarayıcıda kalır.","vs_oeffnen":"Aç","vs_schliessen":"Kapat","baum_laedt":"Yükleniyor …","baum_fehler":"Yüklenemedi.","suche_volltext":"Tam metinde aranıyor …","begriffe":"Sözlük","lernkarten":"Çalışma kartları","ans_kurz_min":"Kısa: {n} dk","dl_laeuft":"Oluşturuluyor …","dl_fehler":"Dosya oluşturulamadı.","dl_gross":"Tek bir resim için çok uzun. Bir bölüm seçin ya da PDF kullanın.","fb_titel":"Formül derlemesi","ans_formeln":"Formüller","fb_titel_ref":"Komut başvurusu"}};
var LERNEN=(function(){
  var L=(document.documentElement.lang||"de").slice(0,2), W=LERNEN_UI[L]||{}, D=LERNEN_UI.de||{}, ok=false, mem={};
  try{ localStorage.setItem("etundso-probe","1"); localStorage.removeItem("etundso-probe"); ok=true; }catch(e){}
  function get(k,d){ var v=null;
    if(ok){ try{ v=localStorage.getItem(k); }catch(e){ v=null; } }
    if(v==null && Object.prototype.hasOwnProperty.call(mem,k)) v=mem[k];
    if(v==null) return d;
    try{ var x=JSON.parse(v); return (x==null || typeof x!==typeof d || Array.isArray(x)!==Array.isArray(d)) ? d : x; }catch(e){ return d; } }
  function set(k,v){ var s=JSON.stringify(v); mem[k]=s; if(ok){ try{ localStorage.setItem(k,s); }catch(e){} } }
  function del(k){ delete mem[k]; if(ok){ try{ localStorage.removeItem(k); }catch(e){} } }
  function w(k,o){ var s=W[k]||D[k]||""; if(o) for(var x in o) s=s.split("{"+x+"}").join(o[x]); return s; }
  function pfad(h){ try{ return new URL(h,location.href).pathname; }catch(e){ return h||""; } }
  function el(tag,cls,text){ var e=document.createElement(tag); if(cls) e.className=cls; if(text!=null) e.textContent=text; return e; }
  // Zurücksetzen in zwei Schritten: Der erste Klick fragt („Wirklich zurücksetzen?“), ein zweiter binnen 5 s führt aus.
  function sicher(btn,tun){ var t=null, text=btn.textContent;
    function zurueck(){ clearTimeout(t); btn.classList.remove("frage"); btn.textContent=text; }
    btn.addEventListener("click",function(){
      if(btn.classList.contains("frage")){ zurueck(); tun(); return; }
      btn.classList.add("frage"); btn.textContent=w("reset_sicher"); t=setTimeout(zurueck,5000); }); }
  return {lang:L, ok:ok, get:get, set:set, del:del, w:w, pfad:pfad, el:el, sicher:sicher};
})();
// Seitenleiste (W3a): Im HTML stehen nur Bereich (offen) und Gruppen (zu). Beim ersten Aufklappen einer Gruppe holt
// dieser Teil den Baum der Sprache (data/tree*.json; einmal je Seite, danach aus dem Zwischenspeicher des Browsers) und
// setzt Module, Kapitel und Themen ein, wie sie früher im HTML standen: alles zugeklappt, der aktive Artikel markiert.
// Danach meldet er „etundso-baum“; der Lesefortschritt malt dann Häkchen und „N/M“ auch in den neuen Zeilen.
(function(){
  var $=LERNEN, side=document.querySelector(".side[data-baum-url]"); if(!side) return;
  var P=null, aktiv=side.getAttribute("data-aktiv")||"";
  var lang=($.lang==="de"?"":$.lang+"/"), fassung=null;
  try{ fassung=localStorage.getItem("wissen-fassung"); }catch(e){}
  function laden(){ if(!P) P=fetch(side.getAttribute("data-baum-url")).then(function(r){ if(!r.ok) throw r.status; return r.json(); })
    .catch(function(e){ P=null; throw e; }); return P; }
  function knoten(nd,tiefe){                          // wie build_wissen.sidebar_html vor W3a
    var d=$.el("details","lvl lvl"+tiefe), s=$.el("summary",null,nd.name); d.appendChild(s); inhalt(d,nd,tiefe); return d; }
  function inhalt(d,nd,tiefe){
    if(nd.mp){ var z=$.el("div","side-lernen"), a1=$.el("a",null,$.w("begriffe")||"Begriffe"), a2=$.el("a",null,$.w("lernkarten")||"Lernkarten"),
        a3=$.el("a",null,nd.ref?$.w("fb_titel_ref"):($.w("ans_formeln")||"Formeln"));   // W4a: Informatik: Befehlsübersicht
      a1.href="/wissen/"+nd.mp+"/begriffe.html"; a2.href="/lernen/"+lang+"?m="+nd.m; a3.href="/wissen/"+nd.mp+(nd.ref?"/uebersicht.html":"/formeln.html");
      [a1,a2,a3].forEach(function(a,i){ if(i){ var p=$.el("span",null," · "); p.setAttribute("aria-hidden","true"); z.appendChild(p); } z.appendChild(a); });
      d.appendChild(z); }
    if(nd.articles && nd.articles.length){ var ul=$.el("ul");
      nd.articles.forEach(function(x){ var li=$.el("li"), a=$.el("a",null,x.kurz||x.title), p="/wissen/"+x.path;
        a.href=(x.alt && fassung==="ausfuehrlich")?"/wissen/"+x.alt:p; a.setAttribute("data-lf",p);
        if(x.alt) a.setAttribute("data-alt","/wissen/"+x.alt);
        if(p===aktiv){ a.className="active"; a.setAttribute("aria-current","page"); }
        li.appendChild(a); ul.appendChild(li); });
      d.appendChild(ul); }
    (nd.children||[]).forEach(function(c){ d.appendChild(knoten(c,tiefe+1)); });
  }
  function fuellen(d){
    if(d.getAttribute("data-gefuellt")) return;
    var ix=d.getAttribute("data-baum").split(".").map(Number), mehr=d.querySelector(".side-mehr");
    var warte=$.el("span","baum-hinweis",$.w("baum_laedt")); d.appendChild(warte);
    laden().then(function(baum){
      var b=baum[ix[0]], nd=b&&b.children&&b.children[ix[1]];
      if(!nd || nd.name!==d.firstElementChild.firstChild.nodeValue) throw 0;   // Baum passt nicht zur Seite (anderer Stand)
      d.removeChild(warte); if(mehr) d.removeChild(mehr);
      inhalt(d,nd,1); d.setAttribute("data-gefuellt","1"); mathe(d);
      document.dispatchEvent(new CustomEvent("etundso-baum"));
    }).catch(function(){ warte.textContent=$.w("baum_fehler"); setTimeout(function(){ if(warte.parentNode) d.removeChild(warte); },4000); });
  }
  [].forEach.call(side.querySelectorAll("details[data-baum]"),function(d){
    d.addEventListener("toggle",function(){ if(d.open) fuellen(d); });
    if(d.open) fuellen(d);
  });
  function vorab(){ laden().catch(function(){}); }    // Leiste in Sicht oder unter dem Zeiger: Baum schon einmal holen
  side.addEventListener("pointerenter",vorab,{once:true}); side.addEventListener("focusin",vorab,{once:true});
  var bL=document.getElementById("toggleLeft"); if(bL) bL.addEventListener("click",vorab,{once:true});
})();
// Lesefortschritt: Ein Artikel gilt als gelesen, wenn seine Zusammenfassung (sonst sein Ende) 1 s lang sichtbar war.
// Häkchen in der Seitenleiste und in der Übersicht, „N/M“ an Kapiteln, Balken je Kapitel in der Übersicht, Zeile am
// Artikelende, „Weiterlesen“ (zuletzt geöffnet, nicht gelesen) auf der Übersicht, Knopf „Fortschritt zurücksetzen“.
(function(){
  var $=LERNEN, G="etundso-gelesen", V="etundso-verlauf";
  // Adresse jedes Themen-Links festhalten, bevor „Fassung“ ihn auf die ausführliche Fassung umlenkt (data-alt)
  [].forEach.call(document.querySelectorAll(".side li a, .theme-card a"),function(a){ a.setAttribute("data-lf",$.pfad(a.getAttribute("href"))); });
  function gelesen(){ return $.get(G,{}); }
  function zahl(as,g){ var n=0; as.forEach(function(a){ if(g[a.getAttribute("data-lf")]) n++; }); return n; }
  function balken(n,m){ var d=$.el("div","lf-balken"), s=$.el("span");
    d.setAttribute("role","progressbar"); d.setAttribute("aria-valuemin","0"); d.setAttribute("aria-valuemax",String(m));
    d.setAttribute("aria-valuenow",String(n)); d.setAttribute("aria-label",$.w("lf_kapitel",{n:n,m:m}));
    s.style.width=(m?Math.round(100*n/m):0)+"%"; d.appendChild(s); return d; }
  // Artikel: Adresse, Kapitelname und Themen des Kapitels stehen an der Seitenleiste (W3a: deren Kapitel lädt erst beim Aufklappen)
  var art=document.querySelector("main.article > article"), side=document.querySelector(".side"), aktiv=document.querySelector(".side li a.active");
  var key=(side&&side.getAttribute("data-aktiv"))||(aktiv?aktiv.getAttribute("data-lf"):null);
  var kapitel=((side&&side.getAttribute("data-kap"))||"").split(" ").filter(Boolean).map(function(p){ return "/wissen/"+p; });
  function malen(){
    var g=gelesen();
    [].forEach.call(document.querySelectorAll("a[data-lf]"),function(a){
      var on=!!g[a.getAttribute("data-lf")], sr=a.querySelector(".lf-sr");
      a.classList.toggle("gelesen",on);
      if(on && !sr) a.appendChild($.el("span","lf-sr"," ("+$.w("gelesen")+")"));
      if(!on && sr) a.removeChild(sr); });
    [].forEach.call(document.querySelectorAll(".side details, details.mk-kap"),function(d){   // Kapitel (Leiste, Modulkarte): „5/12“
      var ul=null; for(var c=d.firstElementChild;c;c=c.nextElementSibling){
        if(c.tagName==="UL"){ ul=c; break; } if(c.classList.contains("theme-card")){ ul=c.querySelector("ul"); break; } }
      var s=d.firstElementChild; if(!ul || !s || s.tagName!=="SUMMARY") return;
      var as=[].slice.call(ul.querySelectorAll("a[data-lf]")), n=zahl(as,g), z=s.querySelector(".lf-z");
      if(!n){ if(z) s.removeChild(z); return; }
      if(!z){ z=$.el("span","lf-z"); s.appendChild(z); }
      z.textContent=n+"/"+as.length; z.title=$.w("lf_kapitel",{n:n,m:as.length}); });
    [].forEach.call(document.querySelectorAll(".theme-card"),function(c){         // Übersicht: Balken je Kapitel
      var as=[].slice.call(c.querySelectorAll("a[data-lf]")), n=zahl(as,g), alt=c.querySelector(".lf-kap");
      if(alt) c.removeChild(alt);
      if(!n) return;
      var box=$.el("div","lf-kap"); box.appendChild(balken(n,as.length)); box.appendChild($.el("span","lf-text",$.w("lf_kapitel",{n:n,m:as.length})));
      c.insertBefore(box,c.firstChild); });
    [].forEach.call(document.querySelectorAll(".mk"),function(k){                // Übersicht: Balken je Modulkarte
      var as=[].slice.call(k.querySelectorAll("a[data-lf]")), n=zahl(as,g), f=k.querySelector(".mk-lf");
      if(!f) return; f.innerHTML="";
      if(n){ f.appendChild(balken(n,as.length)); f.appendChild($.el("span","lf-text",$.w("lf_kapitel",{n:n,m:as.length}))); } });
    if(art && key){                                                              // Artikel: „Gelesen …“ in der Kennzahlenzeile neben der Lesezeit (User, 11.11.2026)
      var zl=document.querySelector(".art-meta .am-zahlen"), z=zl?zl.querySelector(".am-lf"):null;
      if(g[key] && zl){
        var m=kapitel.length?kapitel:[key], n=0; m.forEach(function(p){ if(g[p]) n++; });
        if(!z){ z=$.el("span","am-lf"); zl.appendChild(z); }
        z.textContent=$.w("lf_artikel",{n:n,m:m.length});
      } else if(z) z.parentNode.removeChild(z);
    }
    weiter();
  }
  document.addEventListener("etundso-baum",malen);                               // Seitenleiste hat Zeilen nachgeladen
  if(art && key){
    var titel=document.title.replace(/\s+—\s+EtUndSo$/,"");
    var v=$.get(V,[]).filter(function(e){ return e && e.p!==key; });
    v.unshift({p:key, t:titel, k:(side&&side.getAttribute("data-kapitel"))||"", l:$.lang, z:Date.now()});
    $.set(V,v.slice(0,12));
    // W4a: in „Formeln“ ist die Zusammenfassung verborgen, dort zählt das Ende des Formelblatts
    var enden=[document.getElementById("zusammenfassung")||art.querySelector(".neighbors"), art.querySelector(".fb-ende")].filter(Boolean);
    if(enden.length && !gelesen()[key] && window.IntersectionObserver){
      var t=null, io=new IntersectionObserver(function(es){
        es.forEach(function(e){ e.target._lfSicht=e.isIntersecting; });
        clearTimeout(t);
        if(enden.some(function(x){ return x._lfSicht; }))
          t=setTimeout(function(){ var g=gelesen(); g[key]=Date.now(); $.set(G,g); io.disconnect(); malen(); },1000); });
      enden.forEach(function(x){ io.observe(x); });
    }
  }
  // Übersicht: „Weiterlesen“ und „Fortschritt zurücksetzen“ unter dem Einleitungssatz
  var box=null;
  function weiter(){
    if(!document.querySelector(".field-block")) return;
    var g=gelesen(), v=$.get(V,[]), e=null;
    for(var i=0;i<v.length;i++){ if(v[i] && v[i].l===$.lang && v[i].p && !g[v[i].p]){ e=v[i]; break; } }
    if(!box){
      var lede=document.querySelector("main.article .idx-suche")||document.querySelector("main.article .lede"); if(!lede) return;
      box=$.el("div","lf-weiter"); box.hidden=true; lede.parentNode.insertBefore(box,lede.nextSibling);
    }
    box.innerHTML="";
    if(e){ var a=$.el("a","lf-weiter-a"); a.href=e.p; a.appendChild($.el("span","lf-wh",$.w("weiterlesen")));
      a.appendChild($.el("span","lf-wt",(e.k?e.k+" › ":"")+e.t)); box.appendChild(a); }
    var r=$.el("button","lern-reset lf-reset",$.w("fs_reset")); r.type="button"; r.title=$.w("fs_lokal");
    $.sicher(r,function(){ $.del(G); $.del(V); malen(); });
    box.appendChild(r);
    box.hidden=!(e || Object.keys(g).length);
  }
  malen();
})();
// Link-Vorschau: Links auf Artikel (data-vs, vom Build gesetzt) zeigen ein Kärtchen mit Titel, Kapitel und „Worum es geht“
// aus der vorschau.json des Zielmoduls. Maus: nach kurzem Verweilen; Tastatur: beim Fokus; Handy: langes Tippen (dann mit
// „Öffnen“ und „Schließen“). Schließt beim Verlassen, mit Esc, beim Tippen daneben und bei Größenänderung.
(function(){
  var $=LERNEN; if(!document.querySelector("a[data-vs]") || !window.fetch) return;
  var cache={}, karte=null, ziel=null, tAuf=null, tZu=null, tLang=null, unterdr=null, sx=0, sy=0;
  function modul(p){ var s=p.replace(/^\/wissen\//,"").split("/"); return s.slice(0,-2).join("/"); }
  function daten(p){ var m=modul(p);
    if(!cache[m]) cache[m]=fetch("/wissen/"+m+"/vorschau.json").then(function(r){ return r.ok?r.json():{}; }).catch(function(){ return {}; });
    return cache[m]; }
  function bau(){ if(karte) return karte;
    karte=$.el("div","vs-karte"); karte.id="vs-karte"; karte.setAttribute("role","tooltip"); karte.hidden=true;
    karte.addEventListener("pointerenter",function(){ clearTimeout(tZu); });
    karte.addEventListener("pointerleave",function(e){ if(e.pointerType==="mouse") spaeter(); });
    document.body.appendChild(karte); return karte; }
  function zu(){ clearTimeout(tAuf); clearTimeout(tZu); if(karte) karte.hidden=true; if(ziel) ziel.removeAttribute("aria-describedby"); ziel=null; }
  function spaeter(){ clearTimeout(tZu); tZu=setTimeout(zu,220); }
  function lage(a,k){
    var r=a.getClientRects()[0]||a.getBoundingClientRect(), vw=document.documentElement.clientWidth, b=Math.min(340,vw-16);
    k.style.width=b+"px";
    var x=Math.max(8,Math.min(r.left,vw-b-8)), h=k.offsetHeight, y=r.bottom+8;
    if(y+h>window.innerHeight-8 && r.top-h-8>64) y=r.top-h-8;
    k.style.left=(x+window.scrollX)+"px"; k.style.top=(y+window.scrollY)+"px"; }
  function auf(a,touch){
    var u; try{ u=new URL(a.href); }catch(e){ return; }
    if(u.pathname===location.pathname) return;
    ziel=a;
    daten(u.pathname).then(function(d){
      var e=d[u.pathname.replace(/^\/wissen\//,"")]; if(ziel!==a || !e) return;
      var k=bau(); k.innerHTML="";
      if(e[1]) k.appendChild($.el("div","vs-k",e[1]));
      k.appendChild($.el("div","vs-t",e[0]));
      if(e[2]) k.appendChild($.el("p","vs-p",e[2]));
      if(touch){ var f=$.el("div","vs-f"), o=$.el("a","vs-o",$.w("vs_oeffnen")), s=$.el("button","vs-s",$.w("vs_schliessen"));
        o.href=a.href; s.type="button"; s.addEventListener("click",zu); f.appendChild(o); f.appendChild(s); k.appendChild(f); }
      k.hidden=false; lage(a,k); a.setAttribute("aria-describedby","vs-karte");
    }); }
  function link(e){ return e.target && e.target.closest ? e.target.closest("a[data-vs]") : null; }
  document.addEventListener("pointerover",function(e){ if(e.pointerType!=="mouse") return; var a=link(e); if(!a) return;
    if(a===ziel){ clearTimeout(tZu); return; } clearTimeout(tAuf); tAuf=setTimeout(function(){ auf(a,false); },350); });
  document.addEventListener("pointerout",function(e){ if(e.pointerType!=="mouse") return; var a=link(e); if(!a) return;
    if(e.relatedTarget && a.contains(e.relatedTarget)) return; clearTimeout(tAuf); if(a===ziel) spaeter(); });
  var beruehrt=0;                                                   // Fokus nach Antippen: kein zweites Kärtchen (ohne „Öffnen“)
  document.addEventListener("focusin",function(e){ var a=link(e); if(!a || (a===ziel && karte && !karte.hidden) || Date.now()-beruehrt<1500) return;
    clearTimeout(tAuf); tAuf=setTimeout(function(){ auf(a,false); },250); });
  document.addEventListener("focusout",function(e){ var a=link(e); if(!a) return;
    if(karte && e.relatedTarget && karte.contains(e.relatedTarget)) return; clearTimeout(tAuf); if(a===ziel) zu(); });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape" && karte && !karte.hidden) zu(); });
  document.addEventListener("touchstart",function(e){ var a=link(e); unterdr=null; beruehrt=Date.now();
    if(karte && !karte.hidden && !karte.contains(e.target)) zu();
    if(!a || e.touches.length>1) return;
    sx=e.touches[0].clientX; sy=e.touches[0].clientY; clearTimeout(tLang);
    tLang=setTimeout(function(){ tLang=null; unterdr=a; auf(a,true); },500); },{passive:true});
  document.addEventListener("touchmove",function(e){ if(!tLang) return; var t=e.touches[0];
    if(Math.abs(t.clientX-sx)>10 || Math.abs(t.clientY-sy)>10){ clearTimeout(tLang); tLang=null; } },{passive:true});
  function ab(){ clearTimeout(tLang); tLang=null; }
  document.addEventListener("touchend",ab,{passive:true}); document.addEventListener("touchcancel",ab,{passive:true});
  document.addEventListener("click",function(e){ var a=link(e); if(a && a===unterdr){ e.preventDefault(); } unterdr=null; },true);
  document.addEventListener("contextmenu",function(e){ var a=link(e); if(a && a===unterdr) e.preventDefault(); });
  window.addEventListener("resize",zu);
})();
// Selbsttest in der Zusammenfassung: Der Knopf deckt Bestimmungen, Formeln und Zusammenhänge zu (die Begriffe, Formelnamen
// und der Abschnitt bleiben als Stichwort stehen); Antippen, Enter oder Leertaste deckt einen Punkt auf.
(function(){
  var $=LERNEN, zf=document.querySelector(".zf"), knopf=zf&&zf.querySelector(".zf-test"); if(!knopf) return;
  var teile=[].slice.call(zf.querySelectorAll(".zf-d,.zf-f,.zf-a")); if(!teile.length) return;
  knopf.hidden=false;
  function decke(el,zu){
    el.classList.toggle("zu",zu);
    if(zu){ el.setAttribute("tabindex","0"); el.setAttribute("role","button"); el.setAttribute("aria-label",$.w("aufdecken")); el.setAttribute("data-auf",$.w("aufdecken")); }
    else { el.removeAttribute("role"); el.removeAttribute("aria-label"); el.removeAttribute("tabindex"); } }
  function an(on){
    zf.classList.toggle("zf-abgedeckt",on); knopf.setAttribute("aria-pressed",on?"true":"false");
    teile.forEach(function(el){ decke(el,on); });
    [].forEach.call(zf.querySelectorAll(".zf-cue"),function(c){ c.hidden=!on; });
    if(on) [].forEach.call(zf.querySelectorAll("details.zf-mehr"),function(d){ d.open=true; }); }
  knopf.addEventListener("click",function(){ an(knopf.getAttribute("aria-pressed")!=="true"); });
  zf.addEventListener("click",function(e){ var t=e.target.closest&&e.target.closest(".zu"); if(!t || !zf.contains(t)) return;
    e.preventDefault(); e.stopPropagation(); decke(t,false); },true);
  zf.addEventListener("keydown",function(e){ var t=e.target; if((e.key!=="Enter" && e.key!==" ") || !t.classList || !t.classList.contains("zu")) return;
    e.preventDefault(); decke(t,false); });
})();
// Begriffe: Filter über die Begriffe der Seite (Teilwörter, ohne Umlaute und Akzente wie die Suche)
(function(){
  var $=LERNEN, such=document.querySelector(".bg-such"); if(!such) return;
  var inp=such.querySelector(".bg-filter"), n=such.querySelector(".bg-n"), nichts=document.querySelector(".bg-nichts");
  var es=[].slice.call(document.querySelectorAll(".bg-e")), gs=[].slice.call(document.querySelectorAll(".bg-g")), dt=null;
  function fold(s){ return (s||"").toLowerCase().replace(/ß/g,"ss").replace(/ı/g,"i").replace(/œ/g,"oe").replace(/æ/g,"ae")
    .normalize("NFKD").replace(/[̀-ͯ]/g,""); }
  function text(e){ var d=e.querySelector("dt"); return fold(d?d.textContent:""); }
  such.hidden=false;
  inp.addEventListener("input",function(){
    if(!dt) dt=es.map(text);
    var q=fold(inp.value.trim()), k=0;
    es.forEach(function(e,i){ var on=!q || dt[i].indexOf(q)>=0; e.hidden=!on; if(on) k++; });
    gs.forEach(function(g){ g.hidden=!g.querySelector(".bg-e:not([hidden])"); });
    n.textContent=$.w("bg_anzahl",{n:k}); if(nichts) nichts.hidden=k>0; });
})();
// Lernkarten (W2) sind seit W4b ein eigener Bereich: /lernen/, Code in assets/bereiche.js (Leitner wie hier früher).
/* ---------- Ansichten (W4a, 11.11.2026): Ausführlich | Kurz | Formeln ----------
   Der Kopf der Seite setzt data-ansicht an <html> schon vor dem ersten Zeichnen (?ansicht= in der Adresse, sonst die Wahl
   unter „etundso-ansicht“; sie gilt für alle Artikel). Umschalten = Attribut ändern; die Adresse bekommt ?ansicht= zum
   Teilen. Ein Sprung auf ein Ziel, das die Ansicht verbirgt (Anker, Link aus Zusammenfassung, Suche, Begriffen), schaltet
   für diese Seite auf „Ausführlich“, ohne die Wahl zu ändern (Teil „Sprung auf einen Anker“ ruft dazu ETAnsicht). */
window.ETAnsicht=(function(){
  var $=LERNEN, root=document.documentElement, K="etundso-ansicht";
  var art=document.querySelector("main.article > article.art");
  function jetzt(){ var a=root.getAttribute("data-ansicht"); return a==="formeln"?a:"voll"; }
  function verborgen(el){ for(var x=el; x && x!==document.body; x=x.parentElement){ if(getComputedStyle(x).display==="none") return true; } return false; }
  if(!art){ root.removeAttribute("data-ansicht"); return {jetzt:jetzt, verborgen:function(){ return false; }, setze:function(){}}; }
  var seg=document.querySelector(".topbar .ansicht"), sel=document.querySelector(".topbar .ans-sel");
  var blatt=document.getElementById("formelblatt"), zeit=art.querySelector(".am-zeit"), zeitVoll=zeit?zeit.textContent:"";
  // Formelblatt: KaTeX erst beim ersten Öffnen (vor DOMContentLoaded übernimmt das der Durchgang über die ganze Seite)
  function blattSetzen(){ if(!blatt || !blatt.classList.contains("fb-spaeter")) return;
    blatt.classList.remove("fb-spaeter"); if(document.readyState!=="loading") mathe(blatt); }
  // Lesezeit der Kurzansicht: sichtbare Wörter (ohne Formeln und Code) / 170, wie lesezeit() im Build
  function kurzZeit(){ var n=0, wurzel=art.querySelector(art.classList.contains("hat-kurz")?".ans-kurz":".art-body"); if(!wurzel) return 1;
    [].forEach.call(wurzel.querySelectorAll("p,li,dt,dd,td,th,figcaption"),function(x){
      if(!x.getClientRects().length || x.querySelector("p,li")) return;
      var c=x.cloneNode(true); [].forEach.call(c.querySelectorAll(".katex,code,.katex-display"),function(k){ k.parentNode.removeChild(k); });
      n+=c.textContent.split(/\s+/).filter(function(w){ return /[A-Za-zÄÖÜäöüß0-9]/.test(w); }).length; });
    return Math.max(1,Math.round(n/170)); }
  function malen(){
    var a=jetzt();
    if(seg) [].forEach.call(seg.querySelectorAll(".ans-b"),function(b){ b.setAttribute("aria-pressed",String(b.getAttribute("data-ansicht")===a)); });
    if(sel) sel.value=a;
    if(a==="formeln") blattSetzen();
    if(zeit) zeit.textContent=a==="kurz" ? $.w("ans_kurz_min",{n:kurzZeit()}) : zeitVoll;
  }
  function setze(a,merken){
    a=a==="formeln"?a:"voll";                                     // „kurz“ (alte Links, gemerkte Wahl) -> Ausführlich
    var vorher=jetzt(), oben=null;
    if(scrollY>200 && a!=="formeln"){                               // Lage halten: Abschnitt oben im Fenster merken
      var hs=art.querySelectorAll(".art-body h2,.art-body h3");
      for(var i=0;i<hs.length;i++){ var r=hs[i].getBoundingClientRect(); if(!r.height) continue; if(r.top<=130) oben=hs[i]; else break; } }
    if(a==="voll") root.removeAttribute("data-ansicht"); else root.setAttribute("data-ansicht",a);
    if(merken){ try{ localStorage.setItem(K,a); }catch(e){} }
    try{ var u=new URL(location.href); if(a==="voll") u.searchParams.delete("ansicht");    // Informatik: ?ansicht=uebersicht
      else u.searchParams.set("ansicht",a==="formeln" && art.classList.contains("ref")?"uebersicht":a);
      if(u.href!==location.href) history.replaceState(history.state,"",u.href); }catch(e){}
    malen();
    if(a!==vorher && merken){                                       // ohne weiches Scrollen (html hat scroll-behavior:smooth)
      root.style.scrollBehavior="auto";
      if(a==="formeln" && blatt){ if(blatt.getBoundingClientRect().top<0) blatt.scrollIntoView({block:"start"}); }
      else if(oben && oben.getClientRects().length) oben.scrollIntoView({block:"start"});
      else if(scrollY>art.offsetTop) window.scrollTo(0,0);
      root.style.scrollBehavior="";
    }
    window.dispatchEvent(new Event("resize"));                      // abgesetzte Formeln neu einpassen (fitMath)
  }
  if(seg){ seg.hidden=false;
    seg.addEventListener("click",function(e){ var b=e.target.closest(".ans-b"); if(b) setze(b.getAttribute("data-ansicht"),true); });
    seg.addEventListener("keydown",function(e){                      // Pfeiltasten wandern und wählen (wie eine Optionsgruppe)
      if(e.key!=="ArrowLeft" && e.key!=="ArrowRight" && e.key!=="Home" && e.key!=="End") return;
      var bs=[].slice.call(seg.querySelectorAll(".ans-b")), i=bs.indexOf(document.activeElement); if(i<0) return;
      e.preventDefault();
      i=e.key==="Home"?0:e.key==="End"?bs.length-1:(i+(e.key==="ArrowRight"?1:-1)+bs.length)%bs.length;
      bs[i].focus(); setze(bs[i].getAttribute("data-ansicht"),true); }); }
  if(sel){ sel.hidden=false; sel.addEventListener("change",function(){ setze(sel.value,true); }); }
  [].forEach.call(document.querySelectorAll("[data-ansicht-setzen]"),function(b){
    b.addEventListener("click",function(){ setze(b.getAttribute("data-ansicht-setzen"),true); }); });
  malen();
  if(jetzt()==="kurz" && zeit) window.addEventListener("load",malen);   // Lesezeit nach dem Setzen der Formeln
  window.addEventListener("pageshow",function(e){ if(e.persisted) malen(); });
  return {jetzt:jetzt, verborgen:verborgen, setze:setze};
})();
// Modulseiten (Formelsammlung, Kapitel auf einer Seite): ?kapitel=N zeigt und druckt nur Kapitel N; die Kapitelliste
// wechselt dann das Kapitel, statt an eine ausgeblendete Stelle zu springen. „Drucken“ öffnet den Druckdialog.
(function(){
  var leiste=document.querySelector(".kap-leiste"); if(!leiste) return;
  var sel=leiste.querySelector(".kap-sel"), main=document.querySelector("main.article");
  var kaps=[].slice.call(document.querySelectorAll(".fs-kap,.sz-kap"));
  function hat(n){ return kaps.some(function(k){ return k.getAttribute("data-k")===n; }); }
  function zeige(n,schreiben){
    if(!hat(n)) n="";
    if(n) main.setAttribute("data-kapitel-filter",n); else main.removeAttribute("data-kapitel-filter");
    kaps.forEach(function(k){ k.classList.toggle("kap-an",k.getAttribute("data-k")===n); });
    sel.value=n;
    if(schreiben){ try{ var u=new URL(location.href); if(n) u.searchParams.set("kapitel",n); else u.searchParams.delete("kapitel");
      u.hash=""; history.replaceState(null,"",u.href); }catch(e){} }
  }
  leiste.hidden=false;
  zeige(new URLSearchParams(location.search).get("kapitel")||"",false);
  sel.addEventListener("change",function(){ zeige(sel.value,true); });
  leiste.querySelector(".kap-druck").addEventListener("click",function(){ window.print(); });
  document.addEventListener("click",function(e){                    // Kapitelliste bei aktivem Filter: Kapitel wechseln
    var a=e.target.closest && e.target.closest(".kap-nav a"); if(!a || !main.hasAttribute("data-kapitel-filter")) return;
    var k=document.getElementById(a.getAttribute("href").slice(1)); if(!k) return;
    e.preventDefault(); zeige(k.getAttribute("data-k"),true); k.scrollIntoView({block:"start"}); });
})();
// Download des Formelblatts (Artikel) bzw. der Formelsammlung (Modul) als PNG, JPG, SVG oder PDF. Die Dateien entstehen
// im Browser aus der angezeigten Seite; assets/formel-export.js (setzt die Formeln mit MathJax als SVG, PDF ohne fremde
// Bibliothek) lädt erst beim ersten Klick.
(function(){
  var boxen=[].slice.call(document.querySelectorAll(".fb-dl")); if(!boxen.length) return;
  var $=LERNEN, P=null;
  function laden(){ if(!P) P=new Promise(function(ok,fehler){ var s=document.createElement("script"); s.src="/wissen/assets/formel-export.js?v=0ee537d6a8";
      s.onload=function(){ window.ETFormelExport ? ok(window.ETFormelExport) : fehler(new Error("laden")); };
      s.onerror=function(){ P=null; fehler(new Error("laden")); }; document.head.appendChild(s); });
    return P; }
  boxen.forEach(function(box){
    var status=box.querySelector(".fb-dl-s"), seite=box.closest(".fb-blatt")||document.querySelector("main.article"), quelle=seite.querySelector(".fb-inhalt");
    if(!quelle) return;
    box.hidden=false;
    box.addEventListener("click",function(e){
      var b=e.target.closest(".fb-dl-b"); if(!b || b.getAttribute("aria-busy")==="true") return;
      var main=document.querySelector("main.article"), kap=main && main.getAttribute("data-kapitel-filter");
      b.setAttribute("aria-busy","true"); status.textContent=$.w("dl_laeuft"); status.classList.remove("fehler");
      laden().then(function(X){ return X(quelle,b.getAttribute("data-format"),{kapitel:kap||"", lang:$.lang}); })
        .then(function(){ status.textContent=""; },
              function(err){ status.textContent=(err && err.message==="zu-gross")?$.w("dl_gross"):$.w("dl_fehler"); status.classList.add("fehler");
                if(window.console) console.warn("Formel-Export:",err); })
        .then(function(){ b.removeAttribute("aria-busy"); });
    });
  });
})();
