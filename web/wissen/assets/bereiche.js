/* EtUndSo Bereiche (W4b, 11.11.2026): Lernkarten/Quiz/Mischtest (/lernen/) und Aufgaben (/aufgaben/). Lernstand, gelöste
   Aufgaben und ein laufender Mischtest bleiben in diesem Browser (localStorage über LERNEN aus wissen.js); nichts wird
   übertragen. Wörter: _UI_BEREICHE im Build. */
var BEREICHE_UI={"de":{"lw_modul":"Modul","lw_artikel":"Artikel","lw_alle_art":"Alle Artikel","lw_arten":"Kartenarten","typ_h":"Herleitungen","typ1_l":"Zusammenhang","mod_lernen":"Lernen","mod_quiz":"Quiz","mod_test":"Mischtest","lw_waehle":"Wähle ein Modul.","lw_keine":"In dieser Auswahl gibt es keine Karten.","lw_karten_n":"{n} Karten","hl_ziel":"Ziel","hl_start":"Ausgangspunkt","hl_weiter":"Nächster Schritt","hl_schritt":"Schritt {n} von {m}","quiz_zahl":"Fragen","quiz_start":"Quiz starten","quiz_frage":"Frage {n} von {m}","quiz_p_b":"Welche Bestimmung passt zu diesem Begriff?","quiz_p_f":"Welche Formel gehört dazu?","quiz_p_l":"Was gehört in die Lücke?","quiz_p_w":"Welche Antwort passt?","quiz_weiter":"Weiter","quiz_ende":"Zur Auswertung","quiz_auswertung":"Auswertung","quiz_ergebnis":"{n} von {m} richtig","quiz_falsch":"Noch einmal ansehen","quiz_alle":"Alles richtig.","quiz_neu":"Neues Quiz","quiz_deine":"Deine Antwort","quiz_richtig":"Richtig ist","q_ok":"richtig","q_nein":"falsch","quiz_zu_wenig":"Für ein Quiz braucht diese Auswahl mindestens vier Karten einer Art (Begriffe, Formeln oder Zusammenhänge).","quiz_tasten":"Tasten: 1 bis 4 wählen, Eingabe geht weiter.","test_lede":"Eine zufällige Mischung aus Quizfragen und Aufgaben der gewählten Kapitel. Lösungen und Auswertung kommen erst am Ende; die Aufgaben bewertest du dann selbst.","test_kapitel":"Kapitel für den Test","test_alle":"Alle","test_start":"Test starten","test_aufg_hinweis":"Löse die Aufgabe auf Papier. Die Lösung folgt in der Auswertung.","test_selbst":"Wie lief es?","bew_richtig":"Richtig","bew_teil":"Teilweise","bew_falsch":"Falsch","test_punkte":"{p} von {m} Punkten","test_offen":"Noch {n} Aufgaben selbst bewerten.","test_ohne_aufg":"Die Aufgaben konnten nicht geladen werden; der Test enthält nur Quizfragen.","test_kein_kap":"Wähle mindestens ein Kapitel.","test_fortsetzen":"Laufenden Test fortsetzen","test_neu":"Neuer Test","w_aufgabe":"Aufgabe","ag_geloest":"gelöst","ag_stand":"{n} von {m} gelöst","ag_leer":"Keine Aufgabe passt zu dieser Auswahl.","zf_begriffe":"Begriffe","zf_formeln":"Formeln","zf_zusammenhaenge":"Zusammenhänge","lk_begriff":"Begriff","lk_formel":"Formel","herleitung":"Herleitung","loesung":"Lösung","lk_kapitel":"Kapitel","lk_alle_kap":"Alle Kapitel","lk_faellig":"Heute fällig: {n}","lk_davon_neu":"davon neu: {n}","lk_umdrehen":"Umdrehen","lk_gut":"Wusste ich","lk_mittel":"Unsicher","lk_schlecht":"Wusste ich nicht","lk_stelle":"Zur Stelle im Artikel","lk_fertig":"Für heute ist in dieser Auswahl nichts mehr fällig.","lk_mehr_neu":"{n} weitere neue Karten","lk_heute":"gleich noch einmal","lk_morgen":"morgen","lk_tage":"in {n} Tagen","lk_reset":"Lernstand zurücksetzen","lk_ohne_speicher":"Dieser Browser speichert gerade nichts. Der Lernstand gilt nur, solange die Seite offen ist.","lk_tasten":"Tasten: Leertaste dreht um, 1 / 2 / 3 bewerten.","baum_laedt":"Wird geladen …","baum_fehler":"Konnte nicht geladen werden.","reset_sicher":"Wirklich zurücksetzen?"},"en":{"lw_modul":"Module","lw_artikel":"Article","lw_alle_art":"All articles","lw_arten":"Card types","typ_h":"Derivations","typ1_l":"Key relationship","mod_lernen":"Learn","mod_quiz":"Quiz","mod_test":"Mixed test","lw_waehle":"Choose a module.","lw_keine":"There are no cards in this selection.","lw_karten_n":"{n} cards","hl_ziel":"Goal","hl_start":"Starting point","hl_weiter":"Next step","hl_schritt":"Step {n} of {m}","quiz_zahl":"Questions","quiz_start":"Start quiz","quiz_frage":"Question {n} of {m}","quiz_p_b":"Which definition fits this term?","quiz_p_f":"Which formula belongs to it?","quiz_p_l":"What goes in the gap?","quiz_p_w":"Which answer fits?","quiz_weiter":"Next","quiz_ende":"See results","quiz_auswertung":"Results","quiz_ergebnis":"{n} of {m} correct","quiz_falsch":"Worth another look","quiz_alle":"All correct.","quiz_neu":"New quiz","quiz_deine":"Your answer","quiz_richtig":"Correct answer","q_ok":"correct","q_nein":"wrong","quiz_zu_wenig":"A quiz needs at least four cards of one type in this selection (terms, formulas or key relationships).","quiz_tasten":"Keys: 1 to 4 choose, Enter continues.","test_lede":"A random mix of quiz questions and exercises from the chosen chapters. Solutions and results come only at the end; you then rate the exercises yourself.","test_kapitel":"Chapters for the test","test_alle":"All","test_start":"Start test","test_aufg_hinweis":"Solve the exercise on paper. The solution follows in the results.","test_selbst":"How did it go?","bew_richtig":"Correct","bew_teil":"Partly","bew_falsch":"Wrong","test_punkte":"{p} of {m} points","test_offen":"Rate {n} more exercises yourself.","test_ohne_aufg":"The exercises could not be loaded; the test contains only quiz questions.","test_kein_kap":"Choose at least one chapter.","test_fortsetzen":"Continue the current test","test_neu":"New test","w_aufgabe":"Exercise","ag_geloest":"solved","ag_stand":"{n} of {m} solved","ag_leer":"No exercise matches this selection.","zf_begriffe":"Terms","zf_formeln":"Formulas","zf_zusammenhaenge":"Key relationships","lk_begriff":"Term","lk_formel":"Formula","herleitung":"Derivation","loesung":"Solution","lk_kapitel":"Chapter","lk_alle_kap":"All chapters","lk_faellig":"Due today: {n}","lk_davon_neu":"new: {n}","lk_umdrehen":"Flip","lk_gut":"I knew it","lk_mittel":"Unsure","lk_schlecht":"I didn't know","lk_stelle":"Go to the place in the article","lk_fertig":"Nothing more is due today in this selection.","lk_mehr_neu":"{n} more new cards","lk_heute":"again shortly","lk_morgen":"tomorrow","lk_tage":"in {n} days","lk_reset":"Reset learning progress","lk_ohne_speicher":"This browser is not saving anything right now. Progress lasts only while the page is open.","lk_tasten":"Keys: Space flips, 1 / 2 / 3 rate.","baum_laedt":"Loading …","baum_fehler":"Could not be loaded.","reset_sicher":"Really reset?"},"es":{"lw_modul":"Módulo","lw_artikel":"Artículo","lw_alle_art":"Todos los artículos","lw_arten":"Tipos de tarjeta","typ_h":"Deducciones","typ1_l":"Relación clave","mod_lernen":"Aprender","mod_quiz":"Cuestionario","mod_test":"Prueba mixta","lw_waehle":"Elige un módulo.","lw_keine":"No hay tarjetas en esta selección.","lw_karten_n":"{n} tarjetas","hl_ziel":"Objetivo","hl_start":"Punto de partida","hl_weiter":"Siguiente paso","hl_schritt":"Paso {n} de {m}","quiz_zahl":"Preguntas","quiz_start":"Empezar el cuestionario","quiz_frage":"Pregunta {n} de {m}","quiz_p_b":"¿Qué definición corresponde a este término?","quiz_p_f":"¿Qué fórmula le corresponde?","quiz_p_l":"¿Qué va en el hueco?","quiz_p_w":"¿Qué respuesta corresponde?","quiz_weiter":"Siguiente","quiz_ende":"Ver resultados","quiz_auswertung":"Resultados","quiz_ergebnis":"{n} de {m} correctas","quiz_falsch":"Para repasar","quiz_alle":"Todo correcto.","quiz_neu":"Nuevo cuestionario","quiz_deine":"Tu respuesta","quiz_richtig":"Respuesta correcta","q_ok":"correcta","q_nein":"incorrecta","quiz_zu_wenig":"Para un cuestionario, esta selección necesita al menos cuatro tarjetas de un mismo tipo (términos, fórmulas o relaciones clave).","quiz_tasten":"Teclas: 1 a 4 eligen, Intro continúa.","test_lede":"Una mezcla aleatoria de preguntas y ejercicios de los capítulos elegidos. Las soluciones y los resultados llegan al final; entonces valoras tú mismo los ejercicios.","test_kapitel":"Capítulos para la prueba","test_alle":"Todos","test_start":"Empezar la prueba","test_aufg_hinweis":"Resuelve el ejercicio en papel. La solución aparece en los resultados.","test_selbst":"¿Cómo te fue?","bew_richtig":"Bien","bew_teil":"En parte","bew_falsch":"Mal","test_punkte":"{p} de {m} puntos","test_offen":"Faltan {n} ejercicios por valorar.","test_ohne_aufg":"No se pudieron cargar los ejercicios; la prueba solo contiene preguntas.","test_kein_kap":"Elige al menos un capítulo.","test_fortsetzen":"Continuar la prueba en curso","test_neu":"Nueva prueba","w_aufgabe":"Ejercicio","ag_geloest":"resuelto","ag_stand":"{n} de {m} resueltos","ag_leer":"Ningún ejercicio corresponde a esta selección.","zf_begriffe":"Términos","zf_formeln":"Fórmulas","zf_zusammenhaenge":"Relaciones clave","lk_begriff":"Término","lk_formel":"Fórmula","herleitung":"Deducción","loesung":"Solución","lk_kapitel":"Capítulo","lk_alle_kap":"Todos los capítulos","lk_faellig":"Pendientes hoy: {n}","lk_davon_neu":"nuevas: {n}","lk_umdrehen":"Dar la vuelta","lk_gut":"Lo sabía","lk_mittel":"Dudoso","lk_schlecht":"No lo sabía","lk_stelle":"Ir al lugar en el artículo","lk_fertig":"Hoy no queda nada pendiente en esta selección.","lk_mehr_neu":"{n} tarjetas nuevas más","lk_heute":"otra vez enseguida","lk_morgen":"mañana","lk_tage":"en {n} días","lk_reset":"Reiniciar el progreso de estudio","lk_ohne_speicher":"Este navegador no guarda nada ahora mismo. El progreso solo dura mientras la página esté abierta.","lk_tasten":"Teclas: Espacio da la vuelta, 1 / 2 / 3 valoran.","baum_laedt":"Cargando …","baum_fehler":"No se pudo cargar.","reset_sicher":"¿Reiniciar de verdad?"},"zh":{"lw_modul":"模块","lw_artikel":"文章","lw_alle_art":"全部文章","lw_arten":"卡片类型","typ_h":"推导","typ1_l":"关键联系","mod_lernen":"学习","mod_quiz":"测验","mod_test":"综合测试","lw_waehle":"请选择一个模块。","lw_keine":"当前选择中没有卡片。","lw_karten_n":"{n} 张卡片","hl_ziel":"目标","hl_start":"出发点","hl_weiter":"下一步","hl_schritt":"第 {n} 步，共 {m} 步","quiz_zahl":"题数","quiz_start":"开始测验","quiz_frage":"第 {n} 题，共 {m} 题","quiz_p_b":"哪条说明符合这个术语？","quiz_p_f":"对应的是哪个公式？","quiz_p_l":"空白处应填什么？","quiz_p_w":"哪个答案正确？","quiz_weiter":"下一题","quiz_ende":"查看结果","quiz_auswertung":"结果","quiz_ergebnis":"答对 {n} 题，共 {m} 题","quiz_falsch":"值得再看一遍","quiz_alle":"全部正确。","quiz_neu":"再测一次","quiz_deine":"你的答案","quiz_richtig":"正确答案","q_ok":"正确","q_nein":"错误","quiz_zu_wenig":"测验需要当前选择中至少有四张同类卡片（术语、公式或关键联系）。","quiz_tasten":"按键：1–4 选择，回车继续。","test_lede":"从所选章节中随机混合测验题和练习。答案和结果最后才显示，练习由你自己评分。","test_kapitel":"测试章节","test_alle":"全选","test_start":"开始测试","test_aufg_hinweis":"请在纸上完成这道练习，答案在结果中给出。","test_selbst":"做得怎么样？","bew_richtig":"正确","bew_teil":"部分正确","bew_falsch":"错误","test_punkte":"{m} 分中得 {p} 分","test_offen":"还有 {n} 道练习需要自评。","test_ohne_aufg":"练习无法加载，本次测试只包含测验题。","test_kein_kap":"请至少选择一章。","test_fortsetzen":"继续当前测试","test_neu":"新测试","w_aufgabe":"练习","ag_geloest":"已完成","ag_stand":"已完成 {n} / {m}","ag_leer":"没有符合当前选择的练习。","zf_begriffe":"术语","zf_formeln":"公式","zf_zusammenhaenge":"关键联系","lk_begriff":"术语","lk_formel":"公式","herleitung":"推导","loesung":"解答","lk_kapitel":"章节","lk_alle_kap":"全部章节","lk_faellig":"今天到期：{n}","lk_davon_neu":"其中新卡：{n}","lk_umdrehen":"翻面","lk_gut":"记得","lk_mittel":"不确定","lk_schlecht":"不记得","lk_stelle":"跳到文章中的位置","lk_fertig":"此范围内今天已没有到期的卡片。","lk_mehr_neu":"再学 {n} 张新卡","lk_heute":"稍后再来一次","lk_morgen":"明天","lk_tage":"{n} 天后","lk_reset":"重置学习进度","lk_ohne_speicher":"此浏览器目前无法保存数据，学习进度只在页面打开期间有效。","lk_tasten":"按键：空格翻面，1 / 2 / 3 评分。","baum_laedt":"加载中 …","baum_fehler":"无法加载。","reset_sicher":"确定要重置吗？"},"fr":{"lw_modul":"Module","lw_artikel":"Article","lw_alle_art":"Tous les articles","lw_arten":"Types de fiches","typ_h":"Démonstrations","typ1_l":"Relation clé","mod_lernen":"Apprendre","mod_quiz":"Quiz","mod_test":"Test mixte","lw_waehle":"Choisissez un module.","lw_keine":"Il n’y a pas de fiches dans cette sélection.","lw_karten_n":"{n} fiches","hl_ziel":"Objectif","hl_start":"Point de départ","hl_weiter":"Étape suivante","hl_schritt":"Étape {n} sur {m}","quiz_zahl":"Questions","quiz_start":"Commencer le quiz","quiz_frage":"Question {n} sur {m}","quiz_p_b":"Quelle définition correspond à cette notion ?","quiz_p_f":"Quelle formule lui correspond ?","quiz_p_l":"Que faut-il mettre dans le blanc ?","quiz_p_w":"Quelle réponse convient ?","quiz_weiter":"Suivant","quiz_ende":"Voir les résultats","quiz_auswertung":"Résultats","quiz_ergebnis":"{n} sur {m} correctes","quiz_falsch":"À revoir","quiz_alle":"Tout est correct.","quiz_neu":"Nouveau quiz","quiz_deine":"Votre réponse","quiz_richtig":"Bonne réponse","q_ok":"correcte","q_nein":"incorrecte","quiz_zu_wenig":"Pour un quiz, cette sélection doit contenir au moins quatre fiches d’un même type (notions, formules ou relations clés).","quiz_tasten":"Touches : 1 à 4 pour choisir, Entrée pour continuer.","test_lede":"Un mélange aléatoire de questions et d’exercices des chapitres choisis. Les solutions et les résultats ne viennent qu’à la fin ; vous évaluez alors vous-même les exercices.","test_kapitel":"Chapitres du test","test_alle":"Tous","test_start":"Commencer le test","test_aufg_hinweis":"Résolvez l’exercice sur papier. La solution suit dans les résultats.","test_selbst":"Comment cela s’est-il passé ?","bew_richtig":"Juste","bew_teil":"En partie","bew_falsch":"Faux","test_punkte":"{p} points sur {m}","test_offen":"Encore {n} exercices à évaluer vous-même.","test_ohne_aufg":"Les exercices n’ont pas pu être chargés ; le test ne contient que des questions.","test_kein_kap":"Choisissez au moins un chapitre.","test_fortsetzen":"Reprendre le test en cours","test_neu":"Nouveau test","w_aufgabe":"Exercice","ag_geloest":"résolu","ag_stand":"{n} sur {m} résolus","ag_leer":"Aucun exercice ne correspond à cette sélection.","zf_begriffe":"Notions","zf_formeln":"Formules","zf_zusammenhaenge":"Relations clés","lk_begriff":"Terme","lk_formel":"Formule","herleitung":"Démonstration","loesung":"Solution","lk_kapitel":"Chapitre","lk_alle_kap":"Tous les chapitres","lk_faellig":"À revoir aujourd’hui : {n}","lk_davon_neu":"dont nouvelles : {n}","lk_umdrehen":"Retourner","lk_gut":"Je savais","lk_mittel":"Incertain","lk_schlecht":"Je ne savais pas","lk_stelle":"Aller à l’endroit dans l’article","lk_fertig":"Plus rien à revoir aujourd’hui dans cette sélection.","lk_mehr_neu":"{n} nouvelles fiches de plus","lk_heute":"encore une fois tout de suite","lk_morgen":"demain","lk_tage":"dans {n} jours","lk_reset":"Réinitialiser la progression","lk_ohne_speicher":"Ce navigateur n’enregistre rien pour le moment. La progression ne dure que tant que la page est ouverte.","lk_tasten":"Touches : Espace retourne, 1 / 2 / 3 évaluent.","baum_laedt":"Chargement …","baum_fehler":"Chargement impossible.","reset_sicher":"Vraiment réinitialiser ?"},"tr":{"lw_modul":"Modül","lw_artikel":"Makale","lw_alle_art":"Tüm makaleler","lw_arten":"Kart türleri","typ_h":"Türetmeler","typ1_l":"Temel ilişki","mod_lernen":"Öğren","mod_quiz":"Test","mod_test":"Karma sınav","lw_waehle":"Bir modül seçin.","lw_keine":"Bu seçimde kart yok.","lw_karten_n":"{n} kart","hl_ziel":"Hedef","hl_start":"Başlangıç noktası","hl_weiter":"Sonraki adım","hl_schritt":"Adım {n} / {m}","quiz_zahl":"Soru sayısı","quiz_start":"Testi başlat","quiz_frage":"Soru {n} / {m}","quiz_p_b":"Bu kavrama hangi tanım uyar?","quiz_p_f":"Hangi formül buna aittir?","quiz_p_l":"Boşluğa ne gelir?","quiz_p_w":"Hangi cevap uyar?","quiz_weiter":"İleri","quiz_ende":"Sonuçlara git","quiz_auswertung":"Sonuçlar","quiz_ergebnis":"{m} sorudan {n} doğru","quiz_falsch":"Tekrar bakın","quiz_alle":"Hepsi doğru.","quiz_neu":"Yeni test","quiz_deine":"Cevabınız","quiz_richtig":"Doğru cevap","q_ok":"doğru","q_nein":"yanlış","quiz_zu_wenig":"Test için bu seçimde aynı türden en az dört kart olmalı (kavramlar, formüller veya temel ilişkiler).","quiz_tasten":"Tuşlar: 1–4 seçer, Enter devam eder.","test_lede":"Seçilen bölümlerden rastgele karıştırılmış test soruları ve alıştırmalar. Çözümler ve sonuçlar en sonda gelir; alıştırmaları o zaman kendiniz değerlendirirsiniz.","test_kapitel":"Sınav bölümleri","test_alle":"Tümü","test_start":"Sınavı başlat","test_aufg_hinweis":"Alıştırmayı kâğıt üzerinde çözün. Çözüm sonuçlarda gelir.","test_selbst":"Nasıl geçti?","bew_richtig":"Doğru","bew_teil":"Kısmen","bew_falsch":"Yanlış","test_punkte":"{m} puandan {p}","test_offen":"{n} alıştırmayı daha kendiniz değerlendirin.","test_ohne_aufg":"Alıştırmalar yüklenemedi; sınav yalnızca test sorularından oluşuyor.","test_kein_kap":"En az bir bölüm seçin.","test_fortsetzen":"Süren sınava devam et","test_neu":"Yeni sınav","w_aufgabe":"Alıştırma","ag_geloest":"çözüldü","ag_stand":"{m} alıştırmadan {n} çözüldü","ag_leer":"Bu seçime uyan alıştırma yok.","zf_begriffe":"Kavramlar","zf_formeln":"Formüller","zf_zusammenhaenge":"Temel ilişkiler","lk_begriff":"Terim","lk_formel":"Formül","herleitung":"Türetme","loesung":"Çözüm","lk_kapitel":"Bölüm","lk_alle_kap":"Tüm bölümler","lk_faellig":"Bugün sırası gelen: {n}","lk_davon_neu":"yeni: {n}","lk_umdrehen":"Çevir","lk_gut":"Biliyordum","lk_mittel":"Emin değilim","lk_schlecht":"Bilmiyordum","lk_stelle":"Makaledeki yerine git","lk_fertig":"Bu seçimde bugün için başka kart yok.","lk_mehr_neu":"{n} yeni kart daha","lk_heute":"birazdan tekrar","lk_morgen":"yarın","lk_tage":"{n} gün sonra","lk_reset":"Öğrenme ilerlemesini sıfırla","lk_ohne_speicher":"Bu tarayıcı şu anda hiçbir şey kaydetmiyor. İlerleme yalnızca sayfa açıkken geçerli.","lk_tasten":"Tuşlar: Boşluk çevirir, 1 / 2 / 3 değerlendirir.","baum_laedt":"Yükleniyor …","baum_fehler":"Yüklenemedi.","reset_sicher":"Gerçekten sıfırlansın mı?"}};
(function(){
  "use strict";
  var $=window.LERNEN; if(!$) return;
  var W=BEREICHE_UI[$.lang]||{}, D0=BEREICHE_UI.de||{};
  function w(k,o){ var s=W[k]||D0[k]||""; if(o) for(var x in o) s=s.split("{"+x+"}").join(o[x]); return s; }
  function tx(tag,cls,text){ var e=document.createElement(tag); if(cls) e.className=cls; if(text!=null) e.textContent=text; return e; }
  function hx(tag,cls,h){ var e=document.createElement(tag); if(cls) e.className=cls; if(h!=null) e.innerHTML=h; return e; }
  function knopf(cls,text){ var b=tx("button",cls,text); b.type="button"; return b; }
  function setze(e){ if(typeof mathe==="function") mathe(e); try{ window.dispatchEvent(new Event("resize")); }catch(x){} }   // resize: wissen.js passt breite Formeln ein
  function mische(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
  function heute(){ var d=new Date(); return Math.floor((d.getTime()-d.getTimezoneOffset()*60000)/864e5); }
  function param(){ var p=new URLSearchParams(location.search), o={}; p.forEach(function(v,k){ o[k]=v; }); return o; }
  // Sprachwahl: Auswahl (?m=&k=&a=…) mitnehmen; Kapitelnummer und Dateiname gelten in allen Sprachen
  function sprachLinks(){ [].forEach.call(document.querySelectorAll(".langs a.l-item"),function(a){
    try{ var u=new URL(a.getAttribute("href"),location.href); u.search=location.search; a.setAttribute("href",u.pathname+u.search); }catch(e){} }); }
  function adresse(o){ var p=new URLSearchParams();
    Object.keys(o).forEach(function(k){ if(o[k]!=null && o[k]!=="") p.set(k,o[k]); });
    var q=p.toString(); try{ history.replaceState(null,"",location.pathname+(q?"?"+q:"")+location.hash); }catch(e){}
    sprachLinks(); }
  // Formeln in zugeklappten Lösungen erst beim Aufklappen setzen (Klasse mathe-spaeter, KATEX_OPT in wissen.js)
  document.addEventListener("toggle",function(e){ var d=e.target; if(!d || d.tagName!=="DETAILS" || !d.open) return;
    [].forEach.call(d.querySelectorAll(".mathe-spaeter"),function(x){ x.classList.remove("mathe-spaeter"); setze(x); }); },true);
  function ohneTags(h){ var d=document.createElement("div"); d.innerHTML=h||""; return (d.textContent||"").replace(/\s+/g," ").trim().toLowerCase(); }

  /* ---------- Aufgabenseite eines Moduls ---------- */
  function aufgaben(leiste){
    var S="etundso-aufgaben", seite=document.querySelector(".ag-seite");
    var alle=[].slice.call(seite.querySelectorAll(".ag")), kaps=[].slice.call(seite.querySelectorAll(".ag-kap")),
        arts=[].slice.call(seite.querySelectorAll(".ag-art"));
    if(!alle.length) return;
    var kSel=leiste.querySelector(".ag-k"), aSel=leiste.querySelector(".ag-a"), oCb=leiste.querySelector(".ag-o"),
        zufall=leiste.querySelector(".ag-zufall"), zahl=leiste.querySelector(".ag-stand"), nichts=seite.querySelector(".ag-nichts"),
        reset=seite.querySelector(".ag-reset");
    function stand(){ return $.get(S,{}); }
    function artikelOptionen(){ var k=kSel.value, alt=aSel.value; aSel.length=1;
      arts.forEach(function(sec){ if(k && sec.closest(".ag-kap").getAttribute("data-k")===k)
        aSel.appendChild(new Option(sec.querySelector("h3").textContent, sec.getAttribute("data-a"))); });
      aSel.value=alt; if(aSel.value!==alt) aSel.value=""; aSel.disabled=!k; }
    function malen(){ var s=stand();
      alle.forEach(function(x){ var g=!!s[x.getAttribute("data-id")], cb=x.querySelector(".ag-ok input");
        x.classList.toggle("ag-geloest",g); if(cb) cb.checked=g; }); }
    function zaehlen(){ var s=stand(), n=0, m=0, k=kSel.value, a=aSel.value;
      alle.forEach(function(x){ var sec=x.closest(".ag-art"), kap=x.closest(".ag-kap");
        if((!k || kap.getAttribute("data-k")===k) && (!a || sec.getAttribute("data-a")===a)){ m++; if(s[x.getAttribute("data-id")]) n++; } });
      zahl.textContent=w("ag_stand",{n:n,m:m}); }
    function filtern(){ var k=kSel.value, a=aSel.value, nur=oCb.checked, s=stand(), sichtbar=0;
      arts.forEach(function(sec){ var kap=sec.closest(".ag-kap"), ok=(!k || kap.getAttribute("data-k")===k) && (!a || sec.getAttribute("data-a")===a), n=0;
        [].forEach.call(sec.querySelectorAll(".ag"),function(x){ var z=ok && !(nur && s[x.getAttribute("data-id")]); x.hidden=!z; if(z) n++; });
        sec.hidden=!n; sichtbar+=n; });
      kaps.forEach(function(sec){ sec.hidden=!sec.querySelector(".ag-art:not([hidden])"); });
      nichts.hidden=!!sichtbar; zaehlen();
      adresse({k:k, a:a}); }
    alle.forEach(function(x){ var f=x.querySelector(".ag-fuss"), l=tx("label","ag-ok"), cb=document.createElement("input");
      cb.type="checkbox"; l.appendChild(cb); l.appendChild(document.createTextNode(" "+w("ag_geloest"))); if(f) f.insertBefore(l,f.firstChild);
      cb.addEventListener("change",function(){ var s=stand(), id=x.getAttribute("data-id");
        if(cb.checked) s[id]=heute(); else delete s[id]; $.set(S,s); malen(); zaehlen(); }); });
    kSel.addEventListener("change",function(){ artikelOptionen(); filtern(); });
    aSel.addEventListener("change",filtern);
    oCb.addEventListener("change",filtern);
    zufall.addEventListener("click",function(){ var s=stand(), sicht=alle.filter(function(x){ return !x.hidden && !x.closest("[hidden]"); }),
        offen=sicht.filter(function(x){ return !s[x.getAttribute("data-id")]; }), pool=offen.length ? offen : sicht;
      if(!pool.length) return; var x=pool[Math.floor(Math.random()*pool.length)];
      alle.forEach(function(y){ y.classList.remove("ag-hl"); }); x.classList.add("ag-hl"); x.setAttribute("tabindex","-1");
      x.scrollIntoView({block:"start",behavior:"instant"}); x.focus({preventScroll:true}); });   // weite Sprünge ohne Gleiten
    if(reset){ reset.hidden=false; $.sicher(reset,function(){ var s=stand(); alle.forEach(function(x){ delete s[x.getAttribute("data-id")]; });
      $.set(S,s); malen(); filtern(); }); }
    var p=param(); if(p.k){ kSel.value=p.k; if(kSel.value!==p.k) kSel.value=""; }
    artikelOptionen(); if(p.a){ aSel.value=p.a; if(aSel.value!==p.a) aSel.value=""; }
    leiste.hidden=false; malen(); filtern();
    if(location.hash){ var z=document.getElementById(decodeURIComponent(location.hash.slice(1))); if(z && !z.closest("[hidden]")) z.scrollIntoView(); }
  }

  /* ---------- Lernkarten, Quiz, Mischtest ---------- */
  function lernen(app){
    var MODULE=[]; try{ MODULE=JSON.parse(document.getElementById("lw-daten").textContent); }catch(e){}
    if(!MODULE.length) return;
    var liste=document.querySelector(".lw-module");
    var TYPEN=["b","f","h","l"], TYP_N={b:w("zf_begriffe"),f:w("zf_formeln"),h:w("typ_h"),l:w("zf_zusammenhaenge")},
        TYP_1={b:w("lk_begriff"),f:w("lk_formel"),h:w("herleitung"),l:w("typ1_l")};
    var K="etundso-karten", N="etundso-karten-neu", T="etundso-mischtest", AB=[0,1,3,7,14,30], NEU=20;
    var p=param(), st={m:p.m||"", k:p.k||"", a:p.a||"", arten:(p.arten||"bfhl").split("").filter(function(t){ return TYPEN.indexOf(t)>=0; }),
        modus:(/^(lernen|quiz|test)$/.test(p.modus||"") ? p.modus : "lernen")};
    if(!st.arten.length) st.arten=TYPEN.slice();
    var D=null, cache={}, laeuft=null;            // laeuft: Tastatur-Handler des aktuellen Modus
    // Gerüst: Auswahl, Kartenarten, Modus, Bühne
    var wahl=tx("div","lw-wahl"), mSel=tx("select","lw-sel"), kSel=tx("select","lw-sel"), aSel=tx("select","lw-sel");
    function feld(lbl,sel){ var l=tx("label","lw-feld"); l.appendChild(tx("span",null,lbl)); l.appendChild(sel); return l; }
    mSel.appendChild(new Option(w("lw_waehle"),""));
    MODULE.forEach(function(e){ mSel.appendChild(new Option(e.name, e.m)); });
    wahl.appendChild(feld(w("lw_modul"),mSel)); var kFeld=feld(w("lk_kapitel"),kSel), aFeld=feld(w("lw_artikel"),aSel);
    wahl.appendChild(kFeld); wahl.appendChild(aFeld);
    var arten=tx("fieldset","lw-arten"); arten.appendChild(tx("legend",null,w("lw_arten")));
    var artCb={};
    TYPEN.forEach(function(t){ var l=tx("label","lw-art"), cb=document.createElement("input"); cb.type="checkbox"; cb.value=t;
      cb.checked=st.arten.indexOf(t)>=0; artCb[t]={cb:cb, n:tx("span","lw-n")}; l.appendChild(cb); l.appendChild(document.createTextNode(" "+TYP_N[t]+" "));
      l.appendChild(artCb[t].n); arten.appendChild(l);
      cb.addEventListener("change",function(){ st.arten=TYPEN.filter(function(x){ return artCb[x].cb.checked; }); neu(); }); });
    var modi=tx("div","lw-modi"); modi.setAttribute("role","group"); var modB={};
    [["lernen","mod_lernen"],["quiz","mod_quiz"],["test","mod_test"]].forEach(function(x){ var b=knopf("lw-modus",w(x[1]));
      b.setAttribute("data-modus",x[0]); modB[x[0]]=b; modi.appendChild(b);
      b.addEventListener("click",function(){ st.modus=x[0]; neu(); }); });
    var buehne=tx("div","lw-buehne"); buehne.setAttribute("aria-live","polite");
    app.appendChild(wahl); app.appendChild(arten); app.appendChild(modi); app.appendChild(buehne);
    app.hidden=false;

    function eintrag(m){ for(var i=0;i<MODULE.length;i++) if(MODULE[i].m===m) return MODULE[i]; return null; }
    function kapitel(n){ if(!D) return null; for(var i=0;i<D.kap.length;i++) if(String(D.kap[i].n)===String(n)) return D.kap[i]; return null; }
    function artIndex(){ var k=kapitel(st.k); if(!k || !st.a) return -1; for(var i=0;i<k.a.length;i++) if(k.a[i][0]===st.a) return i; return -1; }
    function artikelVon(c){ var k=kapitel(c.k); return k ? k.a[c.a] : null; }
    function stelle(c){ var a=artikelVon(c); return a ? a[2]+(c.h?"#"+c.h:"") : "#"; }
    function kopfText(c){ var k=kapitel(c.k), a=artikelVon(c); return TYP_1[c.t]+" · "+(k?k.t.split(/\s*[:：]\s*/)[0]:"")+(a?" · "+a[1]:""); }
    function antwort(c){ return c.q || c.r || ""; }
    // Auswahl: Modul -> Kapitel -> Artikel; ohne Kartenarten-Filter (für die Zahlen an den Kästchen)
    function ausschnitt(){ if(!D) return []; var ai=artIndex();
      return D.karten.filter(function(c){ return (!st.k || String(c.k)===String(st.k)) && (ai<0 || c.a===ai); }); }
    function auswahl(){ return ausschnitt().filter(function(c){ return st.arten.indexOf(c.t)>=0; }); }
    function schreibeAdresse(){ adresse({m:st.m, k:st.k, a:st.a, arten:(st.arten.length===4?"":st.arten.join("")), modus:(st.modus==="lernen"?"":st.modus)}); }
    function optionenFuellen(){
      kSel.length=0; aSel.length=0; kSel.appendChild(new Option(w("lk_alle_kap"),"")); aSel.appendChild(new Option(w("lw_alle_art"),""));
      if(D) D.kap.forEach(function(k){ kSel.appendChild(new Option(k.t, String(k.n))); });
      kSel.value=st.k; if(kSel.value!==String(st.k)){ st.k=""; kSel.value=""; }
      var k=kapitel(st.k); if(k) k.a.forEach(function(a){ aSel.appendChild(new Option(a[1], a[0])); });
      aSel.value=st.a; if(aSel.value!==st.a){ st.a=""; aSel.value=""; }
      kFeld.hidden=!D; aFeld.hidden=!D || !st.k; }
    function zahlen(){ var a=ausschnitt(), n={b:0,f:0,h:0,l:0}; a.forEach(function(c){ n[c.t]++; });
      TYPEN.forEach(function(t){ artCb[t].n.textContent="("+n[t]+")"; }); }
    mSel.addEventListener("change",function(){ st.m=mSel.value; st.k=""; st.a=""; laden(); });
    kSel.addEventListener("change",function(){ st.k=kSel.value; st.a=""; neu(); });
    aSel.addEventListener("change",function(){ st.a=aSel.value; neu(); });
    if(liste) liste.addEventListener("click",function(e){ var a=e.target.closest && e.target.closest("a.bm-t[data-m]"); if(!a) return;
      e.preventDefault(); st.m=a.getAttribute("data-m"); st.k=""; st.a=""; laden(); window.scrollTo(0,0); });
    document.addEventListener("keydown",function(e){
      if(!laeuft || e.ctrlKey || e.metaKey || e.altKey) return;
      var t=e.target, tag=t && t.tagName; if(tag==="INPUT" || tag==="SELECT" || tag==="TEXTAREA" || (t && t.isContentEditable)) return;
      var ov=document.getElementById("searchOverlay"); if(ov && !ov.hidden) return;
      laeuft(e, tag); });

    function laden(){
      var e=eintrag(st.m); mSel.value=e ? e.m : ""; D=null; laeuft=null;
      if(!e){ st.m=""; optionenFuellen(); zahlen(); arten.hidden=modi.hidden=true; buehne.innerHTML=""; buehne.appendChild(tx("p","lw-hinweis",w("lw_waehle")));
        if(liste) liste.hidden=false; schreibeAdresse(); return; }
      if(liste) liste.hidden=true;
      buehne.innerHTML=""; buehne.appendChild(tx("p","lw-hinweis",w("baum_laedt")));
      (cache[e.m] || (cache[e.m]=fetch(e.d).then(function(r){ if(!r.ok) throw r.status; return r.json(); })))
        .then(function(d){ if(st.m!==e.m) return; D=d; neu(); })
        .catch(function(){ delete cache[e.m]; buehne.innerHTML=""; buehne.appendChild(tx("p","lw-hinweis",w("baum_fehler"))); });
    }
    function neu(){ laeuft=null; optionenFuellen(); zahlen(); arten.hidden=modi.hidden=!D;
      Object.keys(modB).forEach(function(m){ modB[m].setAttribute("aria-pressed", m===st.modus ? "true" : "false"); });
      schreibeAdresse(); buehne.innerHTML="";
      if(!D) return;
      if(st.modus==="quiz") quizStart(); else if(st.modus==="test") testStart(); else lernStapel(); }

    /* Lernen: Leitner-Fächer wie W2 (Fach 1–5 = 1, 3, 7, 14, 30 Tage; neue Karten 20 je Tag und Modul) */
    function lernStapel(){
      var karten=auswahl(), gerade={}, extra=0, schlange=[], jetzt=null, schritt=0;
      var zahlEl=tx("p","lk-zahl"), karte=tx("div","lk-karte"), kopf=tx("div","lk-kopf"), vorne=tx("div","lk-vorne"), hinten=tx("div","lk-hinten"),
          steuer=tx("div","lk-steuer"), um=knopf("lk-um",w("lk_umdrehen")), bew=tx("div","lk-bew"), ende=tx("div","lk-ende"), neuB=knopf("lk-neu",""),
          fuss=tx("div","lk-fuss"), stelleA=tx("a","lk-stelle",w("lk_stelle")), reset=knopf("lern-reset lk-reset",w("lk_reset"));
      zahlEl.setAttribute("aria-live","polite"); karte.tabIndex=-1;
      karte.appendChild(kopf); karte.appendChild(vorne); karte.appendChild(hinten);
      [["lk_schlecht",0],["lk_mittel",1],["lk_gut",2]].forEach(function(x){ var b=knopf("lk-b lk-b"+x[1],w(x[0])); b.appendChild(tx("small"));
        b.addEventListener("click",function(){ bewerten(x[1]); }); bew.appendChild(b); });
      steuer.appendChild(um); steuer.appendChild(bew);
      ende.appendChild(tx("p",null,w("lk_fertig"))); ende.appendChild(neuB);
      fuss.appendChild(stelleA); fuss.appendChild(tx("span","lk-tasten",w("lk_tasten")));
      if(!karten.length){ buehne.appendChild(tx("p","lw-hinweis",w("lw_keine"))); return; }
      [zahlEl,karte,steuer,ende,fuss].forEach(function(e){ buehne.appendChild(e); });
      if(!$.ok) buehne.appendChild(tx("p","lk-hinweis",w("lk_ohne_speicher")));
      buehne.appendChild(reset);
      function stand(){ return $.get(K,{}); }
      function neuHeute(){ var e=$.get(N,{})[D.mp]; return (e && e[0]===heute()) ? e[1] : 0; }
      function neuZaehlen(){ var n=$.get(N,{}); n[D.mp]=[heute(),neuHeute()+1]; $.set(N,n); }
      function fach(b,r,id){ return r===0 ? 1 : r===1 ? Math.max(1,b) : gerade[id] ? 1 : Math.min(5,Math.max(1,b)+1); }
      function tage(d){ return d===0 ? w("lk_heute") : d===1 ? w("lk_morgen") : w("lk_tage",{n:d}); }
      function baue(){ var s=stand(), t=heute(), faellig=[], neue=[];
        karten.forEach(function(c){ var x=s[c.id]; if(x){ if(x[1]<=t) faellig.push(c); } else neue.push(c); });
        faellig.sort(function(a,b){ return s[a.id][1]-s[b.id][1] || s[a.id][0]-s[b.id][0]; });
        schlange=faellig.concat(neue.slice(0,Math.max(0,NEU-neuHeute())+extra)); zeige(); }
      function abschnitt(label,h,cls){ var d=hx("div",cls||"hl-teil"); d.appendChild(tx("span","hl-k",label)); d.appendChild(hx("div","hl-i",h)); return d; }
      function schritte(c){ return c.t==="h" ? (c.s||[]) : []; }
      function zeige(){
        var s=stand(), n=0; schlange.forEach(function(c){ if(!s[c.id]) n++; });
        zahlEl.textContent=w("lk_faellig",{n:schlange.length})+(n?" · "+w("lk_davon_neu",{n:n}):"");
        jetzt=schlange[0]||null; karte.hidden=steuer.hidden=fuss.hidden=!jetzt; ende.hidden=!!jetzt;
        if(!jetzt){ var rest=karten.filter(function(c){ return !s[c.id]; }).length; neuB.hidden=!rest; neuB.textContent=w("lk_mehr_neu",{n:Math.min(NEU,rest)}); return; }
        kopf.textContent=kopfText(jetzt); vorne.innerHTML=jetzt.v; hinten.innerHTML=""; hinten.hidden=true; schritt=0;
        if(jetzt.t==="h"){ if(jetzt.z) vorne.appendChild(abschnitt(w("hl_ziel"),jetzt.z,"hl-teil hl-ziel"));
          if(jetzt.s0) vorne.appendChild(abschnitt(w("hl_start"),jetzt.s0));
          var ss=schritte(jetzt), off=jetzt.s0?1:0;
          ss.forEach(function(h,i){ var d=abschnitt(w("hl_schritt",{n:i+1+off,m:ss.length+off}),h); d.hidden=true; hinten.appendChild(d); });
        } else hinten.innerHTML=jetzt.r||"";
        stelleA.href=stelle(jetzt); um.hidden=false; bew.hidden=true; um.textContent=jetzt.t==="h" ? w("hl_weiter") : w("lk_umdrehen");
        var x=s[jetzt.id], b=x?x[0]:0;
        [0,1,2].forEach(function(r){ var sm=bew.querySelector(".lk-b"+r+" small"); if(sm) sm.textContent=tage(r===0?0:AB[fach(b,r,jetzt.id)]); });
        setze(karte); }
      function umdrehen(){ if(!jetzt) return; if(!bew.hidden) return;
        if(jetzt.t==="h"){ var teile=hinten.children; hinten.hidden=false;
          if(schritt<teile.length){ teile[schritt].hidden=false; schritt++; }
          if(schritt<teile.length) return; }
        hinten.hidden=false; um.hidden=true; bew.hidden=false; karte.focus({preventScroll:true});
        var r=bew.getBoundingClientRect(); if(r.bottom>window.innerHeight) bew.scrollIntoView({block:"end",behavior:"smooth"}); }
      function bewerten(r){ if(!jetzt || bew.hidden) return;
        var s=stand(), x=s[jetzt.id], c=jetzt, f=fach(x?x[0]:0,r,c.id);
        if(!x) neuZaehlen();
        s[c.id]=[f, heute()+(r===0?0:AB[f])]; $.set(K,s); schlange.shift();
        if(r===0){ gerade[c.id]=1; schlange.push(c); }
        zeige(); if(!karte.hidden) karte.focus({preventScroll:true}); else if(!neuB.hidden) neuB.focus(); }
      um.addEventListener("click",umdrehen);
      karte.addEventListener("click",function(e){ if(!(e.target.closest && e.target.closest("a"))) umdrehen(); });
      neuB.addEventListener("click",function(){ extra+=NEU; baue(); });
      $.sicher(reset,function(){ var s=stand(), n=$.get(N,{}); karten.forEach(function(c){ delete s[c.id]; }); delete n[D.mp];
        $.set(K,s); $.set(N,n); extra=0; gerade={}; baue(); });
      laeuft=function(e,tag){
        if((e.key===" " || e.key==="Enter") && jetzt && bew.hidden){ if(tag==="BUTTON" || tag==="A") return; e.preventDefault(); umdrehen(); }
        else if(jetzt && !bew.hidden && (e.key==="1" || e.key==="2" || e.key==="3")){ e.preventDefault(); bewerten(+e.key-1); } };
      baue();
    }

    /* Quiz und Mischtest: Mehrfachauswahl. Falsche Antworten sind echte Antworten anderer Karten derselben Art, zuerst aus
       demselben Kapitel, sonst aus dem Modul; Herleitungen kommen nicht vor. */
    function quizfaehig(c){ return c.t!=="h" && !!antwort(c); }
    function optionen(c){ var ant=antwort(c), seen={}, pool=[]; seen[ohneTags(ant)]=1;
      if(c.x && c.x.length>=3)                                     // geschriebene falsche Antworten (seit 11.11.2026): Option "x:<id>:<i>"
        return mische([c.id].concat(c.x.slice(0,3).map(function(_,i){ return "x:"+c.id+":"+i; })));
      var kap=D.karten.filter(function(x){ return x.t===c.t && x.k===c.k && x.id!==c.id && quizfaehig(x); }),
          mod=D.karten.filter(function(x){ return x.t===c.t && x.k!==c.k && quizfaehig(x); });
      mische(kap).concat(mische(mod)).forEach(function(x){ var n=ohneTags(antwort(x)); if(pool.length<3 && n && !seen[n]){ seen[n]=1; pool.push(x.id); } });
      return pool.length<3 ? null : mische([c.id].concat(pool)); }
    function karteVon(id){ for(var i=0;i<D.karten.length;i++) if(D.karten[i].id===id) return D.karten[i]; return null; }
    function optText(o){ var m=/^x:(.+):(\d+)$/.exec(o||""); if(m){ var c=karteVon(m[1]); return c&&c.x?(c.x[+m[2]]||""):""; } var k=karteVon(o); return k?antwort(k):""; }   // Text einer Quiz-Option
    function frageText(c){ return c.w ? w("quiz_p_w") : w("quiz_p_"+c.t); }
    function zahlWahl(){ var l=tx("label","lw-feld"), s=tx("select","lw-sel lw-zahl"); l.appendChild(tx("span",null,w("quiz_zahl"))); l.appendChild(s);
      [10,20,30].forEach(function(n){ s.appendChild(new Option(String(n),String(n))); }); return [l,s]; }
    // Eine Mehrfachauswahl-Frage zeichnen. modus "quiz": nach der Wahl gleich zeigen, ob richtig; "test": nur die Wahl
    // merken (Mischtest); "zeigen": Ergebnis zeigen, nichts mehr wählbar (Auswertung des Mischtests)
    function mcFrage(ziel, f, modus, fertig){ var sofort=modus==="quiz";
      var c=karteVon(f.id), box=tx("div","qz-frage");
      box.appendChild(tx("p","qz-p",frageText(c))); box.appendChild(hx("div","qz-vorne",c.v));
      var ol=tx("ol","qz-opt"), bs=[];
      f.o.forEach(function(id,i){ var li=tx("li"), b=knopf("qz-b"); b.innerHTML='<span class="qz-nr">'+(i+1)+'</span><span class="qz-a">'+optText(id)+'</span>';
        if(f.w===i) b.classList.add("gewaehlt");
        b.addEventListener("click",function(){ waehle(i); }); li.appendChild(b); ol.appendChild(li); bs.push(b); });
      box.appendChild(ol); ziel.appendChild(box);
      function markieren(){ var r=f.o.indexOf(f.id);
        bs.forEach(function(b,i){ b.disabled=true; if(i===r){ b.classList.add("ok"); b.setAttribute("aria-label",w("q_ok")+": "+b.textContent); }
          else if(i===f.w){ b.classList.add("nein"); b.setAttribute("aria-label",w("q_nein")+": "+b.textContent); } }); }
      function waehle(i){ if(sofort && f.w>=0) return; f.w=i; bs.forEach(function(b,j){ b.classList.toggle("gewaehlt",j===i); });
        if(sofort) markieren(); if(fertig) fertig(); }
      if((sofort && f.w>=0) || modus==="zeigen") markieren();
      setze(box);
      return waehle; }
    function fehlerListe(items){ var ol=tx("ol","qz-fehler");
      items.forEach(function(f){ var c=karteVon(f.id), li=tx("li"); if(!c) return;
        li.appendChild(hx("div","qz-vorne",c.v));
        if(f.w>=0){ li.appendChild(hx("div","qz-deine",'<span class="hl-k">'+w("quiz_deine")+'</span> '+optText(f.o[f.w]))); }
        li.appendChild(hx("div","qz-richtig",'<span class="hl-k">'+w("quiz_richtig")+'</span> '+antwort(c)));
        var a=tx("a","lk-stelle",w("lk_stelle")); a.href=stelle(c); li.appendChild(a); ol.appendChild(li); });
      return ol; }

    function quizStart(){
      var kandidaten=auswahl().filter(quizfaehig), zw=zahlWahl(), start=knopf("lk-um qz-start",w("quiz_start")), box=tx("div","qz-setup");
      box.appendChild(zw[0]); box.appendChild(start); buehne.appendChild(box);
      var moeglich=kandidaten.filter(function(c){ return !!optionen(c); });
      if(!moeglich.length){ start.disabled=true; buehne.appendChild(tx("p","lw-hinweis",w("quiz_zu_wenig"))); return; }
      start.addEventListener("click",function(){ var n=+zw[1].value, fr=[];
        mische(moeglich).forEach(function(c){ if(fr.length<n){ var o=optionen(c); if(o) fr.push({id:c.id,o:o,w:-1}); } });
        quizLauf(fr); });
    }
    function quizLauf(fr){
      var i=0; buehne.innerHTML="";
      var kopf=tx("p","qz-kopf"), platz=tx("div"), weiter=knopf("lk-um qz-weiter",""), hinweis=tx("p","lk-tasten",w("quiz_tasten"));
      buehne.appendChild(kopf); buehne.appendChild(platz); buehne.appendChild(weiter); buehne.appendChild(hinweis);
      var waehle=null;
      function zeige(){ platz.innerHTML=""; kopf.textContent=w("quiz_frage",{n:i+1,m:fr.length})+" · "+TYP_1[karteVon(fr[i].id).t];
        weiter.hidden=true; weiter.textContent=i+1<fr.length ? w("quiz_weiter") : w("quiz_ende");
        waehle=mcFrage(platz,fr[i],"quiz",function(){ weiter.hidden=false; weiter.focus({preventScroll:true}); }); }
      weiter.addEventListener("click",function(){ if(i+1<fr.length){ i++; zeige(); kopf.scrollIntoView({block:"nearest"}); } else quizEnde(fr); });
      laeuft=function(e){ var z=parseInt(e.key,10); if(z>=1 && z<=4 && fr[i].w<0){ e.preventDefault(); waehle(z-1); }
        else if(e.key==="Enter" && !weiter.hidden && document.activeElement!==weiter){ e.preventDefault(); weiter.click(); } };
      zeige();
    }
    function quizEnde(fr){ laeuft=null; buehne.innerHTML="";
      var ok=fr.filter(function(f){ return f.w>=0 && f.o[f.w]===f.id; }).length, falsch=fr.filter(function(f){ return !(f.w>=0 && f.o[f.w]===f.id); });
      buehne.appendChild(tx("h2","qz-h",w("quiz_auswertung")));
      buehne.appendChild(tx("p","qz-ergebnis",w("quiz_ergebnis",{n:ok,m:fr.length})));
      if(falsch.length){ buehne.appendChild(tx("h3","qz-h3",w("quiz_falsch"))); buehne.appendChild(fehlerListe(falsch)); }
      else buehne.appendChild(tx("p",null,w("quiz_alle")));
      var nb=knopf("lk-um",w("quiz_neu")); nb.addEventListener("click",neu); buehne.appendChild(nb);
      setze(buehne); buehne.querySelector(".qz-h").scrollIntoView({block:"start"}); }

    /* Mischtest: Kapitel wählen, Zahl der Fragen; Quizfragen und Aufgaben gemischt. Aufgaben stammen aus der statischen
       Aufgabenseite des Moduls (einmal geladen). Lösungen und Auswertung erst am Ende; Aufgaben bewertet der Leser selbst
       (richtig 1, teilweise ½, falsch 0). Ein laufender Test bleibt gespeichert (etundso-mischtest). */
    var AUFG={};                                         // Moduladresse -> Promise {id: {k, html, stelle, titel}}
    function aufgabenLaden(){ var u=D.aufg;
      if(!AUFG[u]) AUFG[u]=fetch(u).then(function(r){ if(!r.ok) throw r.status; return r.text(); }).then(function(t){
        var doc=new DOMParser().parseFromString(t,"text/html"), o={};
        [].forEach.call(doc.querySelectorAll(".ag-kap"),function(kap){ var k=kap.getAttribute("data-k");
          [].forEach.call(kap.querySelectorAll(".ag"),function(x){ var a=x.querySelector(".aufg"), s=x.querySelector(".ag-stelle");
            if(a) o[x.getAttribute("data-id")]={k:k, html:a.outerHTML, stelle:s?s.getAttribute("href"):"#"}; }); });
        return o; }).catch(function(e){ delete AUFG[u]; throw e; });
      return AUFG[u]; }
    function testLaden(){ var t=$.get(T,{}); return (t.m===D.m && t.l===$.lang && t.f && t.f.length) ? t : null; }
    function testStart(){
      buehne.appendChild(tx("p","lede lern-lede",w("test_lede")));
      var alt=testLaden();
      if(alt){ var fb=knopf("lk-um mt-fort",w("test_fortsetzen")); buehne.appendChild(fb); fb.addEventListener("click",function(){ testLauf(alt); }); }
      var fs=tx("fieldset","mt-kap"); fs.appendChild(tx("legend",null,w("test_kapitel")));
      var alleL=tx("label","mt-alle"), alleCb=document.createElement("input"); alleCb.type="checkbox"; alleL.appendChild(alleCb);
      alleL.appendChild(document.createTextNode(" "+w("test_alle"))); fs.appendChild(alleL);
      var cbs=D.kap.map(function(k){ var l=tx("label","mt-k"), cb=document.createElement("input"); cb.type="checkbox"; cb.value=String(k.n);
        cb.checked=!st.k || String(k.n)===String(st.k); l.appendChild(cb); l.appendChild(document.createTextNode(" "+k.t)); fs.appendChild(l); return cb; });
      function alleStand(){ alleCb.checked=cbs.every(function(c){ return c.checked; }); }
      alleCb.addEventListener("change",function(){ cbs.forEach(function(c){ c.checked=alleCb.checked; }); });
      cbs.forEach(function(c){ c.addEventListener("change",alleStand); }); alleStand();
      var zw=zahlWahl(), start=knopf("lk-um mt-start",w("test_start")), meldung=tx("p","lw-hinweis");
      buehne.appendChild(fs); var box=tx("div","qz-setup"); box.appendChild(zw[0]); box.appendChild(start); buehne.appendChild(box); buehne.appendChild(meldung);
      start.addEventListener("click",function(){
        var kap=cbs.filter(function(c){ return c.checked; }).map(function(c){ return c.value; });
        if(!kap.length){ meldung.textContent=w("test_kein_kap"); return; }
        var n=+zw[1].value; start.disabled=true; meldung.textContent=w("baum_laedt");
        var karten=D.karten.filter(function(c){ return kap.indexOf(String(c.k))>=0 && st.arten.indexOf(c.t)>=0 && quizfaehig(c) && optionen(c); });
        function bauen(auf,ohne){ var ids=Object.keys(auf).filter(function(id){ return kap.indexOf(String(auf[id].k))>=0; });
          var nA=Math.min(ids.length, Math.round(n/2)), nQ=Math.min(karten.length, n-nA); nA=Math.min(ids.length, n-nQ);
          var f=mische(karten).slice(0,nQ).map(function(c){ return {t:"q", id:c.id, o:optionen(c), w:-1}; })
            .concat(mische(ids).slice(0,nA).map(function(id){ return {t:"a", id:id, b:null}; }));
          if(!f.length){ start.disabled=false; meldung.textContent=w("lw_keine"); return; }
          var t={m:D.m, l:$.lang, f:mische(f), i:0, ende:false, ohne:!!ohne}; $.set(T,t); testLauf(t); }
        aufgabenLaden().then(function(a){ bauen(a,false); },function(){ bauen({},true); });
      });
    }
    function testLauf(t){
      aufgabenLaden().catch(function(){ return {}; }).then(function(auf){
        t.f=t.f.filter(function(f){ return f.t==="q" ? !!karteVon(f.id) : !!auf[f.id]; });
        if(!t.f.length){ $.del(T); neu(); return; }
        if(t.ende){ testEnde(t,auf); return; }
        buehne.innerHTML="";
        var kopf=tx("p","qz-kopf"), platz=tx("div"), weiter=knopf("lk-um qz-weiter",""), hinweis=tx("p","lk-tasten",w("quiz_tasten"));
        if(t.ohne) buehne.appendChild(tx("p","lw-hinweis",w("test_ohne_aufg")));
        [kopf,platz,weiter,hinweis].forEach(function(e){ buehne.appendChild(e); });
        var waehle=null;
        function zeige(){ var f=t.f[t.i]; platz.innerHTML=""; waehle=null;
          kopf.textContent=w("quiz_frage",{n:t.i+1,m:t.f.length})+" · "+(f.t==="q" ? TYP_1[karteVon(f.id).t] : w("w_aufgabe"));
          weiter.textContent=t.i+1<t.f.length ? w("quiz_weiter") : w("quiz_ende");
          if(f.t==="q") waehle=mcFrage(platz,f,"test",function(){ $.set(T,t); });
          else { var d=hx("div","mt-aufg",auf[f.id].html); [].forEach.call(d.querySelectorAll("details.loesung"),function(x){ x.parentNode.removeChild(x); });
            platz.appendChild(d); platz.appendChild(tx("p","lw-hinweis",w("test_aufg_hinweis"))); setze(d); } }
        weiter.addEventListener("click",function(){ if(t.i+1<t.f.length){ t.i++; $.set(T,t); zeige(); kopf.scrollIntoView({block:"nearest"}); }
          else { t.ende=true; $.set(T,t); testEnde(t,auf); } });
        laeuft=function(e){ var z=parseInt(e.key,10); if(waehle && z>=1 && z<=4){ e.preventDefault(); waehle(z-1); }
          else if(e.key==="Enter" && document.activeElement!==weiter){ e.preventDefault(); weiter.click(); } };
        zeige();
      });
    }
    function testEnde(t,auf){ laeuft=null; buehne.innerHTML="";
      var kopf=tx("h2","qz-h",w("quiz_auswertung")), erg=tx("p","qz-ergebnis"), offen=tx("p","lw-hinweis"), nochmal=tx("div","mt-nochmal");
      [kopf,erg,offen,nochmal].forEach(function(e){ buehne.appendChild(e); });
      var ol=tx("ol","mt-liste"); buehne.appendChild(ol);
      function rechnen(){ var p=0, m=t.f.length, o=0, falsch=[];
        t.f.forEach(function(f){ if(f.t==="q"){ if(f.w>=0 && f.o[f.w]===f.id) p++; else falsch.push(f); }
          else { if(f.b==null) o++; else { p+=f.b; if(f.b<1) falsch.push(f); } } });
        erg.textContent=w("test_punkte",{p:String(Math.round(p*10)/10).replace(".",$.lang==="en"||$.lang==="zh"?".":","),m:m});
        offen.textContent=o ? w("test_offen",{n:o}) : ""; offen.hidden=!o;
        nochmal.innerHTML=""; if(falsch.length){ nochmal.appendChild(tx("h3","qz-h3",w("quiz_falsch")));
          var ul=tx("ul","mt-links"); falsch.forEach(function(f){ var li=tx("li"), a=tx("a");
            if(f.t==="q"){ var c=karteVon(f.id); a.innerHTML=c.v; a.href=stelle(c); li.appendChild(tx("span","hl-k",TYP_1[c.t]+": ")); }
            else { var x=hx("div",null,auf[f.id].html), h=x.querySelector(".aufg-h"); a.innerHTML=h?h.innerHTML:w("w_aufgabe"); a.href=auf[f.id].stelle;
              li.appendChild(tx("span","hl-k",w("w_aufgabe")+": ")); }
            li.appendChild(a); ul.appendChild(li); }); nochmal.appendChild(ul); setze(nochmal); } }
      t.f.forEach(function(f,i){ var li=tx("li","mt-e");
        if(f.t==="q"){ var c=karteVon(f.id), r=f.w>=0 && f.o[f.w]===f.id;
          li.classList.add(r?"mt-ok":"mt-nein"); li.appendChild(tx("p","qz-kopf",TYP_1[c.t]+" · "+(r?w("q_ok"):w("q_nein"))));
          var platz=tx("div"); li.appendChild(platz); mcFrage(platz,f,"zeigen",null);
          var a=tx("a","lk-stelle",w("lk_stelle")); a.href=stelle(c); li.appendChild(a); }
        else { li.appendChild(tx("p","qz-kopf",w("w_aufgabe")));
          var d=hx("div","mt-aufg",auf[f.id].html); [].forEach.call(d.querySelectorAll("details.loesung"),function(x){ x.open=true; });
          [].forEach.call(d.querySelectorAll(".mathe-spaeter"),function(x){ x.classList.remove("mathe-spaeter"); });
          li.appendChild(d); var s=tx("div","mt-selbst"); s.appendChild(tx("span","hl-k",w("test_selbst")));
          [["bew_richtig",1],["bew_teil",0.5],["bew_falsch",0]].forEach(function(x){ var b=knopf("mt-b",w(x[0]));
            b.setAttribute("aria-pressed",f.b===x[1]?"true":"false");
            b.addEventListener("click",function(){ f.b=x[1]; $.set(T,t); [].forEach.call(s.querySelectorAll(".mt-b"),function(y){ y.setAttribute("aria-pressed",y===b?"true":"false"); });
              li.classList.toggle("mt-ok",f.b===1); li.classList.toggle("mt-teil",f.b===0.5); li.classList.toggle("mt-nein",f.b===0); rechnen(); });
            s.appendChild(b); });
          if(f.b!=null) li.classList.add(f.b===1?"mt-ok":f.b===0?"mt-nein":"mt-teil");
          li.appendChild(s); var a2=tx("a","lk-stelle",w("lk_stelle")); a2.href=auf[f.id].stelle; li.appendChild(a2); }
        ol.appendChild(li); });
      var nb=knopf("lk-um",w("test_neu")); nb.addEventListener("click",function(){ $.del(T); neu(); }); buehne.appendChild(nb);
      rechnen(); setze(ol); kopf.scrollIntoView({block:"start"}); }

    // Start: Auswahl aus der Adresse
    if(st.m) laden(); else { optionenFuellen(); zahlen(); arten.hidden=modi.hidden=true; sprachLinks(); }
  }

  var leiste=document.querySelector(".ag-seite .ag-leiste"); if(leiste) aufgaben(leiste);
  var app=document.querySelector(".lw-app"); if(app) lernen(app);
})();
