/* EtUndSo Formel-Export: ETFormelExport(quelle, format, {kapitel, lang}) -> Promise (lädt die Datei herunter). */
(function(){
  var MJ="/wissen/assets/mathjax-3.2.2/tex-svg.js";   // dieselbe Fassung wie der Editor, vom eigenen Server (W3b)
  var W=794, H_SEITE=1123, RAND=48, INNEN=W-2*RAND;                   // A4 bei 96 dpi (Pixel = CSS-Pixel)
  var SCHRIFT="Arial, Helvetica, sans-serif", EXF=0.45;              // Mathe: 1 ex = 0,45 der Schriftgröße
  var FARBE={text:"#16191a", leise:"#5b6360", gruen:"#15633a", gruen2:"#1b7f4a", orange:"#c2410c", linie:"#d5dad7"};
  var mjP=null, messer=null;
  function mathjax(){
    if(mjP) return mjP;
    mjP=new Promise(function(ok,fehler){
      if(window.MathJax && window.MathJax.tex2svg){ ok(); return; }
      window.MathJax={loader:{load:["[tex]/color"]},tex:{packages:{"[+]":["color"]}},svg:{fontCache:"none"},
        startup:{typeset:false,ready:function(){ MathJax.startup.defaultReady(); MathJax.startup.promise.then(function(){ ok(); }); }}};
      var s=document.createElement("script"); s.src=MJ; s.async=true;
      s.onerror=function(){ mjP=null; fehler(new Error("mathjax")); }; document.head.appendChild(s);
    });
    return mjP;
  }
  function esc(t){ return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"); }
  function font(st){ return (st.i?"italic ":"")+(st.b?"bold ":"")+st.fs+"px "+(st.mono?"Consolas, 'Courier New', monospace":SCHRIFT); }
  function breite(t,st){ if(!messer) messer=document.createElement("canvas").getContext("2d"); messer.font=font(st); return messer.measureText(t).width; }
  // ---- Formeln: TeX aus der KaTeX-Ausgabe (annotation), Satz mit MathJax als SVG ----
  function tex(k){ var a=k.querySelector('annotation[encoding="application/x-tex"]'); return a?a.textContent:""; }
  function mathe(t,display,fs){
    var ex=fs*EXF, node;
    try{ node=MathJax.tex2svg(t,{display:display,em:fs,ex:ex,containerWidth:INNEN}); }catch(e){ return null; }
    var svg=node.querySelector("svg"); if(!svg || node.querySelector('[data-mml-node="merror"]')) return null;
    var w=parseFloat(svg.getAttribute("width"))*ex, h=parseFloat(svg.getAttribute("height"))*ex;
    var va=/vertical-align:\s*(-?[\d.]+)ex/.exec(svg.getAttribute("style")||""), tief=va?-parseFloat(va[1])*ex:0;
    svg.removeAttribute("style"); svg.removeAttribute("role"); svg.removeAttribute("focusable"); svg.removeAttribute("aria-hidden");
    var inner=new XMLSerializer().serializeToString(svg);
    return {w:w,h:h,tief:tief,svg:function(x,y,s){ s=s||1;
      return inner.replace(/^<svg\b/,'<svg x="'+x.toFixed(2)+'" y="'+y.toFixed(2)+'" style="color:'+FARBE.text+'" overflow="visible"')
        .replace(/ width="[^"]*"/,' width="'+(w*s).toFixed(2)+'"').replace(/ height="[^"]*"/,' height="'+(h*s).toFixed(2)+'"'); }};
  }
  // ---- Inhalt sammeln: Blöcke (Titel, Etikett, Name, Absatz, Formel, Trennlinie) aus den sichtbaren Elementen ----
  var BLOCK=/^(P|DIV|SECTION|ASIDE|UL|OL|LI|H1|H2|H3|H4|H5|H6|TABLE|PRE|BLOCKQUOTE|DL|DT|DD|FIGURE|DETAILS|NAV|HR|FIGCAPTION|ARTICLE|TR|TBODY|THEAD)$/;
  var WEG=/^(FIGURE|IMG|DETAILS|BUTTON|SCRIPT|STYLE|NAV|SELECT|INPUT|HR)$/;
  function versteckt(n){ return n.hidden || getComputedStyle(n).display==="none"; }
  function sammeln(quelle){
    var aus=[], vorWartet="";                                       // Aufzählungszeichen für den ersten Absatz eines Listenpunkts
    function absatz(z,einzug,art){
      if(z.runs.some(function(r){ return r.m || (r.t && r.t.trim()); })){ aus.push({typ:art||"absatz",runs:z.runs,einzug:einzug||0,vor:vorWartet}); vorWartet=""; }
      z.runs=[]; }
    function fluss(el,st,z,einzug){
      for(var n=el.firstChild;n;n=n.nextSibling){
        if(n.nodeType===3){ z.runs.push({t:n.nodeValue,st:st}); continue; }
        if(n.nodeType!==1 || versteckt(n)) continue;
        var c=n.classList, tag=n.tagName;
        if(c.contains("katex-display") || c.contains("mrow") || c.contains("gl-zeile") || c.contains("fb-gl") || c.contains("fb-n")
           || c.contains("fb-h") || c.contains("callout-h") || c.contains("fbox-h")){ absatz(z,einzug); block(n,einzug); continue; }
        if(c.contains("katex")){ z.runs.push({m:tex(n),st:st}); continue; }
        if(c.contains("katex-mathml") || c.contains("fb-nr") || WEG.test(tag) || tag==="svg") continue;
        if(tag==="BR"){ z.runs.push({br:true,st:st}); continue; }
        if(BLOCK.test(tag)){ absatz(z,einzug); block(n,einzug); continue; }
        var s2={fs:st.fs,b:st.b||/^(STRONG|B|TH)$/.test(tag),i:st.i||/^(EM|I)$/.test(tag),mono:st.mono||tag==="CODE",farbe:st.farbe};
        fluss(n,s2,z,einzug);
      }
    }
    function formel(n,einzug){                                     // eine Formelzeile: Teile (mrow) und Nummer
      var ks=[].slice.call(n.classList.contains("katex-display")?[n]:n.querySelectorAll(".katex-display")).map(tex).filter(Boolean);
      if(!ks.length) ks=[].slice.call(n.querySelectorAll(".katex")).map(tex).filter(Boolean);
      var nr=n.querySelector(".gl-nr, .fb-nr:not(.fb-ohne)");
      if(ks.length) aus.push({typ:"formel",tex:ks,nr:nr?nr.textContent.replace(/\)\s*\(/g,") (").trim():"",einzug:einzug||0});
    }
    function block(el,einzug){
      if(versteckt(el)) return;
      var c=el.classList, tag=el.tagName;
      if(WEG.test(tag) || c.contains("fb-dl") || c.contains("abb-knopf") || c.contains("gr-szene") || c.contains("zf-cue")) return;
      if(c.contains("fb-e")){ aus.push({typ:"trenn"}); }
      if(c.contains("katex-display") || c.contains("mrow") || c.contains("gl-zeile") || c.contains("fb-gl")){ formel(el,einzug); return; }
      if(c.contains("fb-h")){ aus.push({typ:"etikett",runs:[{t:el.textContent.toUpperCase(),st:{fs:11.5,b:true,farbe:FARBE.orange}}]}); return; }
      if(c.contains("fb-n") || c.contains("callout-h") || c.contains("fbox-h") || c.contains("zf-gh")){
        var z0={runs:[]}; fluss(el,{fs:15,b:true,farbe:FARBE.gruen2},z0,einzug); absatz(z0,einzug,"name"); return; }
      if(/^H[1-4]$/.test(tag)){ var lv=+tag.charAt(1), zh={runs:[]};
        fluss(el,{fs:lv<=2?20:16.5,b:true,farbe:lv<=2?FARBE.gruen:FARBE.text},zh,einzug); absatz(zh,einzug,"h"+Math.max(2,lv)); return; }
      if(tag==="UL" || tag==="OL"){ var k=0;
        [].forEach.call(el.children,function(li){ if(li.tagName!=="LI" || versteckt(li)) return; k++;
          var zl={runs:[]}; vorWartet=tag==="OL"?k+".":"•"; fluss(li,{fs:15},zl,(einzug||0)+22); absatz(zl,(einzug||0)+22); vorWartet=""; });
        return; }
      if(tag==="TABLE"){ [].forEach.call(el.querySelectorAll("tr"),function(tr){ var zt={runs:[]};
          [].forEach.call(tr.children,function(td,i){ if(i) zt.runs.push({t:"   |   ",st:{fs:14,farbe:FARBE.leise}}); fluss(td,{fs:14,b:td.tagName==="TH"},zt,einzug); });
          absatz(zt,einzug); }); return; }
      if(tag==="PRE"){ var zs=el.textContent.replace(/\n$/,"").split("\n");
        zs.forEach(function(l,k){ aus.push({typ:k===zs.length-1?"code-ende":"code",runs:[{t:l||" ",st:{fs:13,mono:true}}],einzug:einzug||0}); }); return; }
      var z={runs:[]}; fluss(el,{fs:15},z,einzug); absatz(z,einzug);
    }
    var t=quelle.getAttribute("data-titel")||"", u=quelle.getAttribute("data-unter")||"";
    aus.push({typ:"titel",runs:[{t:t,st:{fs:22,b:true,farbe:FARBE.gruen}}]});
    if(u) aus.push({typ:"unter",runs:[{t:u,st:{fs:13,farbe:FARBE.leise}}]});
    block(quelle,0);
    return aus;
  }
  // ---- Setzen: jeder Block bekommt Höhe und eine Zeichenfunktion (SVG-Text ab Höhe y) ----
  var CJK=/[⺀-鿿豈-﫿＀-￯　-〿]/;
  function tokens(runs){                                            // Wörter, Leerzeichen, CJK-Zeichen einzeln, Formeln
    var out=[];
    runs.forEach(function(r){
      if(r.br){ out.push({br:true}); return; }
      if(r.m!=null){ var m=mathe(r.m,false,r.st.fs); if(m) out.push({m:m,st:r.st}); else out.push({t:r.m,st:r.st}); return; }
      var t=r.t.replace(/\s+/g," ");
      var teile=t.match(/ |[^ ]+/g)||[];
      teile.forEach(function(w){
        if(w===" "){ out.push({sp:true,st:r.st}); return; }
        if(CJK.test(w)){ (w.match(/[⺀-鿿豈-﫿＀-￯　-〿][,.;:!?)\]，。；：！？）」』]*|[^⺀-鿿豈-﫿＀-￯　-〿]+/g)||[]).forEach(function(x){ out.push({t:x,st:r.st,cjk:true}); }); }
        else out.push({t:w,st:r.st});
      });
    });
    return out;
  }
  function absatzSetzen(b,breiteMax){
    var tk=tokens(b.runs), zeilen=[], z={el:[],w:0,auf:0,ab:0}, x0=b.einzug||0;
    function neu(){ zeilen.push(z); z={el:[],w:0,auf:0,ab:0}; }
    var fs0=(b.runs[0]&&b.runs[0].st&&b.runs[0].st.fs)||15;
    tk.forEach(function(t){
      if(t.br){ neu(); return; }
      if(t.sp){ if(z.el.length){ var ws=breite(" ",t.st); z.el.push({sp:true,w:ws}); z.w+=ws; } return; }
      var w=t.m?t.m.w:breite(t.t,t.st);
      if(z.el.length && z.w+w>breiteMax-x0){ while(z.el.length && z.el[z.el.length-1].sp){ z.w-=z.el.pop().w; } neu(); }
      z.el.push(t.m?{m:t.m,w:w}:{t:t.t,w:w,st:t.st}); z.w+=w;
      if(t.m){ z.auf=Math.max(z.auf,t.m.h-t.m.tief); z.ab=Math.max(z.ab,t.m.tief); }
    });
    if(z.el.length) neu();
    var zh=fs0*1.5, ys=[], h=0;
    zeilen.forEach(function(zz){ var auf=Math.max(fs0*1.05,zz.auf+3), ab=Math.max(fs0*0.45,zz.ab+3); ys.push({auf:auf,ab:ab}); h+=Math.max(zh,auf+ab); });
    return {h:h,zeichne:function(y){
      var s="", yy=y;
      zeilen.forEach(function(zz,k){
        var hz=Math.max(zh,ys[k].auf+ys[k].ab), base=yy+(hz-(ys[k].auf+ys[k].ab))/2+ys[k].auf, x=RAND+x0;
        if(k===0 && b.vor) s+='<text x="'+(RAND+x0-16).toFixed(2)+'" y="'+base.toFixed(2)+'" font-family="'+SCHRIFT+'" font-size="'+fs0+'" fill="'+FARBE.leise+'" text-anchor="middle">'+esc(b.vor)+'</text>';
        zz.el.forEach(function(e){
          if(e.m){ s+=e.m.svg(x,base+e.m.tief-e.m.h); }
          else if(!e.sp){ var st=e.st; s+='<text x="'+x.toFixed(2)+'" y="'+base.toFixed(2)+'" font-family="'+(st.mono?"Consolas, Courier New, monospace":SCHRIFT)+'" font-size="'+st.fs+'"'
              +(st.b?' font-weight="bold"':'')+(st.i?' font-style="italic"':'')+' fill="'+(st.farbe||FARBE.text)+'">'+esc(e.t)+'</text>'; }
          x+=e.w; });
        yy+=hz; });
      return s; }};
  }
  function formelSetzen(b){
    var teile=b.tex.map(function(t){ return mathe(t,true,16); }), nrB=b.nr?breite(b.nr,{fs:14})+14:0, platz=INNEN-(b.einzug||0)-nrB;
    var gut=teile.filter(Boolean); if(!gut.length) return absatzSetzen({runs:[{t:b.tex.join("   "),st:{fs:14,mono:true}}],einzug:b.einzug},INNEN);
    var luecke=28, summe=gut.reduce(function(a,m){ return a+m.w; },0)+luecke*(gut.length-1);
    var reihen=summe<=platz?[gut]:gut.map(function(m){ return [m]; });   // nebeneinander oder untereinander
    var hs=reihen.map(function(r){ var wR=r.reduce(function(a,m){ return a+m.w; },0)+luecke*(r.length-1), s=Math.min(1,platz/wR);
      return {r:r,s:s,w:wR*s,h:Math.max.apply(null,r.map(function(m){ return m.h; }))*s}; });
    var h=hs.reduce(function(a,x){ return a+x.h+10; },0)+6;
    return {h:h,zeichne:function(y){ var s="", yy=y+6;
      hs.forEach(function(x,k){ var xx=RAND+(b.einzug||0)+Math.max(0,(platz-x.w)/2);
        x.r.forEach(function(m){ s+=m.svg(xx,yy+(x.h-m.h*x.s)/2,x.s); xx+=(m.w+luecke)*x.s; });
        if(k===hs.length-1 && b.nr) s+='<text x="'+(W-RAND).toFixed(2)+'" y="'+(yy+x.h/2+5).toFixed(2)+'" font-family="'+SCHRIFT+'" font-size="14" fill="'+FARBE.leise+'" text-anchor="end">'+esc(b.nr)+'</text>';
        yy+=x.h+10; });
      return s; }};
  }
  function setzen(items){
    var lay=[];
    items.forEach(function(b,i){
      if(b.typ==="trenn"){ if(lay.length && !/^(titel|unter|h2|h3|etikett|trenn)$/.test(lay[lay.length-1].typ)) lay.push({typ:"trenn",h:14,zeichne:function(y){ return '<line x1="'+RAND+'" x2="'+(W-RAND)+'" y1="'+(y+7)+'" y2="'+(y+7)+'" stroke="'+FARBE.linie+'" stroke-width="1"/>'; }}); return; }
      if(b.typ==="formel"){ var f=formelSetzen(b); f.typ="formel"; lay.push(f); return; }
      var V={titel:0,unter:2,etikett:14,name:6,h2:22,h3:14,code:0,"code-ende":0}, N={titel:4,unter:18,etikett:2,name:2,h2:8,h3:4,code:0,"code-ende":6};
      var a=absatzSetzen(b,INNEN), vor=b.typ in V?V[b.typ]:4, nach=b.typ in N?N[b.typ]:4;
      if(b.typ==="h2") nach+=6;
      lay.push({typ:b.typ,h:a.h+vor+nach,zeichne:function(y){ var s=a.zeichne(y+vor);
        if(b.typ==="h2") s+='<line x1="'+RAND+'" x2="'+(W-RAND)+'" y1="'+(y+vor+a.h+4).toFixed(2)+'" y2="'+(y+vor+a.h+4).toFixed(2)+'" stroke="'+FARBE.gruen+'" stroke-width="2"/>';
        return s; }});
    });
    return lay;
  }
  function svgDoc(stuecke,h,skala){                                 // stuecke: [{y, s}] in CSS-Pixeln
    return '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="'+Math.round(W*skala)+'" height="'+Math.round(h*skala)
      +'" viewBox="0 0 '+W+' '+Math.ceil(h)+'"><rect width="'+W+'" height="'+Math.ceil(h)+'" fill="#ffffff"/>'+stuecke+'</svg>';
  }
  function fuss(y,text){ return '<text x="'+(W-RAND)+'" y="'+y.toFixed(2)+'" font-family="'+SCHRIFT+'" font-size="10.5" fill="'+FARBE.leise+'" text-anchor="end">'+esc(text)+'</text>'; }
  function lang(lay){                                               // eine lange Seite (SVG, PNG, JPG)
    var y=RAND, s="";
    lay.forEach(function(b){ s+=b.zeichne(y); y+=b.h; });
    y+=18; s+=fuss(y,"etundso.de"); y+=RAND-18;
    return {s:s,h:y};
  }
  function seiten(lay){                                             // A4-Seiten (PDF): Überschriften und Namen bleiben beim Folgenden
    var unten=H_SEITE-RAND-20, out=[], y=RAND, s="";
    function umbruch(){ out.push(s); s=""; y=RAND; }
    for(var i=0;i<lay.length;i++){
      var b=lay[i], need=b.h, j=i;
      while(j<lay.length-1 && /^(h2|h3|etikett|name|titel|unter|trenn)$/.test(lay[j].typ)){ j++; need+=lay[j].h; }
      if(b.typ==="trenn" && y===RAND) continue;
      if(y+need>unten && y>RAND && need<=unten-RAND) umbruch();
      else if(y+b.h>unten && y>RAND) umbruch();
      if(b.typ==="trenn" && y===RAND) continue;
      s+=b.zeichne(y); y+=b.h;
    }
    if(s) out.push(s);
    return out.map(function(x,k){ return x+fuss(H_SEITE-RAND+14,"etundso.de · "+(k+1)+" / "+out.length); });
  }
  function rastern(svg,w,h,typ,q){
    return new Promise(function(ok,fehler){
      var url=URL.createObjectURL(new Blob([svg],{type:"image/svg+xml"})), img=new Image();
      img.onload=function(){ try{
          var c=document.createElement("canvas"); c.width=w; c.height=h; var x=c.getContext("2d");
          x.fillStyle="#ffffff"; x.fillRect(0,0,w,h); x.drawImage(img,0,0,w,h); URL.revokeObjectURL(url);
          c.toBlob(function(b){ b?ok(b):fehler(new Error("canvas")); },typ,q); }catch(e){ fehler(e); } };
      img.onerror=function(){ URL.revokeObjectURL(url); fehler(new Error("svg")); };
      img.src=url;
    });
  }
  function pdfDatei(bilder){                                        // bilder: [{w,h,bytes}] JPEG, je eine A4-Seite
    var teile=[], len=0, off=[], enc=new TextEncoder();
    function add(x){ var b=typeof x==="string"?enc.encode(x):x; teile.push(b); len+=b.length; }
    function obj(n,body){ off[n]=len; add(n+" 0 obj\n"+body+"\nendobj\n"); }
    add("%PDF-1.4\n%âãÏÓ\n");
    var kids=bilder.map(function(_,i){ return (3+3*i)+" 0 R"; }).join(" ");
    obj(1,"<< /Type /Catalog /Pages 2 0 R >>");
    obj(2,"<< /Type /Pages /Kids ["+kids+"] /Count "+bilder.length+" >>");
    bilder.forEach(function(b,i){
      var p=3+3*i, c=p+1, im=p+2, cs="q 595.28 0 0 841.89 0 0 cm /Im0 Do Q";
      obj(p,"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595.28 841.89] /Resources << /XObject << /Im0 "+im+" 0 R >> >> /Contents "+c+" 0 R >>");
      obj(c,"<< /Length "+cs.length+" >>\nstream\n"+cs+"\nendstream");
      off[im]=len;
      add(im+" 0 obj\n<< /Type /XObject /Subtype /Image /Width "+b.w+" /Height "+b.h+" /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length "+b.bytes.length+" >>\nstream\n");
      add(b.bytes); add("\nendstream\nendobj\n");
    });
    var n=2+3*bilder.length, xref=len, z="xref\n0 "+(n+1)+"\n0000000000 65535 f \n";
    for(var i=1;i<=n;i++) z+=("0000000000"+off[i]).slice(-10)+" 00000 n \n";
    add(z+"trailer\n<< /Size "+(n+1)+" /Root 1 0 R >>\nstartxref\n"+xref+"\n%%EOF\n");
    return new Blob(teile,{type:"application/pdf"});
  }
  function speichern(blob,name){
    var a=document.createElement("a"), url=URL.createObjectURL(blob); a.href=url; a.download=name; a.rel="noopener";
    document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(url); a.parentNode.removeChild(a); },4000);
  }
  window.ETFormelExport=function(quelle,format,opt){
    opt=opt||{};
    return mathjax().then(function(){
      var lay=setzen(sammeln(quelle));
      var datei=(quelle.getAttribute("data-datei")||"formeln")+(opt.kapitel?"-kapitel-"+opt.kapitel:"");
      if(format==="svg"){ var l=lang(lay); speichern(new Blob(['<?xml version="1.0" encoding="UTF-8"?>\n'+svgDoc(l.s,l.h,1)],{type:"image/svg+xml"}),datei+".svg"); return; }
      if(format==="png" || format==="jpg"){
        var g=lang(lay), sk=Math.min(2,32000/g.h,Math.sqrt(2.6e8/(W*g.h)));
        if(sk<1) throw new Error("zu-gross");
        return rastern(svgDoc(g.s,g.h,sk),Math.round(W*sk),Math.round(g.h*sk),format==="png"?"image/png":"image/jpeg",0.93)
          .then(function(b){ speichern(b,datei+"."+format); });
      }
      if(format==="pdf"){
        var sk2=2.5, ps=seiten(lay);
        return ps.reduce(function(p,s){ return p.then(function(liste){
            return rastern(svgDoc(s,H_SEITE,sk2),Math.round(W*sk2),Math.round(H_SEITE*sk2),"image/jpeg",0.9)
              .then(function(b){ return b.arrayBuffer(); })
              .then(function(buf){ liste.push({w:Math.round(W*sk2),h:Math.round(H_SEITE*sk2),bytes:new Uint8Array(buf)}); return liste; }); }); },
          Promise.resolve([])).then(function(bilder){ speichern(pdfDatei(bilder),datei+".pdf"); });
      }
      throw new Error("format");
    });
  };
})();
