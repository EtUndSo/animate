---
title: Yönlü türev ve en dik çıkış
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230500
summary: Kısmi türevler, tek bir girdi değiştirildiğinde fonksiyonun nasıl tepki verdiğini söyler.
tags: yönlü türevi
lang: tr
---

<span class="anker" id="stufe-4"></span>

:::zweck
Kısmi türevler, tek bir girdi değiştirildiğinde fonksiyonun nasıl tepki verdiğini söyler. Bütün girdiler aynı anda bir doğrultuda kaydırılırsa eğimi yönlü türev ölçer. Bu kesim yönlü türevle, gradyanın en dik çıkışın doğrultusunu gösterdiğini ve eş yükselti eğrilerine dik olduğunu gösteriyor. Bir örnek, buna rağmen yokuş aşağı en dik yolun en alçak noktaya doğru gitmek zorunda olmadığını gösteriyor.
:::

### Yönlü türev

<span class="anker" id="stufe-4-1"></span>

Arazide insan nadiren tam kuzeye ya da tam doğuya gider. $\mathbf{x}$ noktasında durup herhangi bir doğrultuda yola çıkan kişi, doğrultuya bağlı bir eğim hisseder. Bir doğrultu, uzunluğu $1$ olan bir $\mathbf{u}$ vektörüyle betimlenir. Uzunluk sabitlenmelidir: İki kat büyük adımlar atan, arazi daha dik olmadığı hâlde her adımda iki kat daha fazla yükselir.

:::definition Tanım 4.1 (Yönlü türev)
<span class="anker" id="satz-4-1"></span>

$\lVert\mathbf{u}\rVert=1$ olan bir $\mathbf{u}$ vektörü için

<span class="anker" id="gl-4-1"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\lim_{t\to0}\frac{f(\mathbf{x}+t\,\mathbf{u})-f(\mathbf{x})}{t} \tag{4.1}$$

ifadesine, limit var olduğu sürece, $f$ fonksiyonunun $\mathbf{x}$ noktasında $\mathbf{u}$ doğrultusundaki __yönlü türevi__ denir.
:::

$\mathbf{u}=\mathbf{e}_j$ için bu, $x_j$ değişkenine göre kısmi türevdir. Arazi resminde arazi yüzeyi $\mathbf{x}$ noktasından geçen ve $\mathbf{u}$ doğrultusunda uzanan doğru boyunca kesilir; yönlü türev bu kesit eğrisinin eğimidir. Ama onu her doğrultu için yeniden hesaplamak gerekmez.

:::satz Teorem 4.2 (Yönlü türev ve gradyan)
<span class="anker" id="satz-4-2"></span>

$f$, $\mathbf{x}$ noktasında türevlenebilirse uzunluğu $1$ olan her $\mathbf{u}$ vektörü için şu geçerlidir:

<span class="anker" id="gl-4-2"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}\mathbf{u} . \tag{4.2}$$
:::

:::beweis Yönlü türev ve gradyan
[(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5) içine özel olarak $t\ne0$ ile $\mathbf{h}=t\,\mathbf{u}$ konur; o zaman $\lVert\mathbf{h}\rVert=|t|$ olur. $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})-t\,\nabla f(\mathbf{x})^{\top}\mathbf{u}}{|t|}$ bölümü $0$'a gider, dolayısıyla $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})}{t}-\nabla f(\mathbf{x})^{\top}\mathbf{u}$ de gider.
:::

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $(1,\,2)$ noktasında $\nabla f=(4,\,5)^{\top}$ ile ve uzunluğu $\sqrt{0{,}36+0{,}64}=1$ olan $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ doğrultusu için şu bulunur:

$$D_{\mathbf{u}}f(1,2)=4\cdot0{,}6+5\cdot0{,}8=2{,}4+4{,}0=6{,}4$$

(Şekil [8](#abb-8)). Ters doğrultu $-\mathbf{u}$ yönünde eğim $-6{,}4$, $\mathbf{u}$ vektörüne dik olan $(0{,}8;\ -0{,}6)^{\top}$ doğrultusunda ise $3{,}2-3{,}0=0{,}2$ olur.

:::abbildung ml/k3rrichtung 8
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $\mathbf{x}=(1,\,2)^{\top}$ noktasında gradyan ile doğrultunun iç çarpımı olarak yönlü türev.
:::
::::

⁠**Kısacası:** Bir $\mathbf{u}$ birim vektörü doğrultusundaki eğim, $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ iç çarpımıdır.

### En dik çıkışın doğrultusu

<span class="anker" id="stufe-4-2"></span>

Yokuş yukarı en dik biçimde çıkmak için hangi doğrultuda yürümek gerekir? [(4.2)](#gl-4-2) uyarınca $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ iç çarpımını en büyük yapan $\mathbf{u}$ birim vektörü aranır. Bunun aracını [Bölüm 1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) sağlamıştı: Cauchy-Schwarz eşitsizliği.

:::satz Teorem 4.3 (En dik çıkış)
<span class="anker" id="satz-4-3"></span>

$f$, $\mathbf{x}$ noktasında türevlenebilir ve $\nabla f(\mathbf{x})\ne\mathbf{0}$ olsun. O zaman uzunluğu $1$ olan her $\mathbf{u}$ vektörü için şu geçerlidir:

<span class="anker" id="gl-4-3"></span>
$$-\lVert\nabla f(\mathbf{x})\rVert\le D_{\mathbf{u}}f(\mathbf{x})\le\lVert\nabla f(\mathbf{x})\rVert . \tag{4.3}$$

Üst sınıra yalnızca $\mathbf{u}=\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$ için, alt sınıra yalnızca $\mathbf{u}=-\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$ için ulaşılır. Yani gradyan en dik çıkışın doğrultusunu gösterir ve uzunluğu bu doğrultudaki eğimdir; negatif gradyan ise en dik inişin doğrultusunu gösterir.
:::

:::beweis En dik çıkış
[Bölüm 1, Kesim 5.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-1)'deki Cauchy-Schwarz eşitsizliğine göre $|\nabla f(\mathbf{x})^{\top}\mathbf{u}|\le\lVert\nabla f(\mathbf{x})\rVert\,\lVert\mathbf{u}\rVert=\lVert\nabla f(\mathbf{x})\rVert$ olur ve eşitlik ancak ve ancak $\mathbf{u}$, $\nabla f(\mathbf{x})$ vektörünün bir katıysa sağlanır. Uzunluğu $1$ olan katlar $\pm\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$ vektörleridir. Bunlar yerine konursa $\pm\nabla f(\mathbf{x})^{\top}\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert=\pm\lVert\nabla f(\mathbf{x})\rVert$ elde edilir.
:::

[Bölüm 1, Kesim 5.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2)'deki, $\nabla f(\mathbf{x})$ ile $\mathbf{u}$ arasındaki $\varphi$ açısıyla $D_{\mathbf{u}}f(\mathbf{x})=\lVert\nabla f(\mathbf{x})\rVert\cos\varphi$ olur. Gradyan doğrultusunda gidilirse $\varphi=0$ ve $\cos\varphi=1$ olur. $90^\circ$ sapılırsa eğim sıfırdır. Ters yönde gidilirse eğim en güçlü biçimde negatiftir. [Bölüm 1, Kesim 5.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5)'e göre $\nabla f(\mathbf{x})^{\top}\mathbf{u}$, gradyanın $\mathbf{u}$ doğrultusundaki doğru üzerindeki gölge uzunluğudur ve bir gölge, üzerine düştüğü doğru okun kendi doğrultusunda uzandığında en uzundur.

Teoremde üç önkoşul gizlidir. Birincisi, $\nabla f(\mathbf{x})\ne\mathbf{0}$ olmalıdır; gradyan sıfırsa [(4.2)](#gl-4-2) uyarınca eğim her doğrultuda sıfırdır ve hiçbir doğrultu diğerinden daha dik değildir. İkincisi, $f$ türevlenebilir olmalıdır, yoksa [(4.2)](#gl-4-2) geçerli olmaz. Üçüncüsü, teorem Öklid uzunluğu aynı olan doğrultuları karşılaştırır; adımlar başka türlü ölçülürse en dik doğrultu değişir (aşağıdaki arka plan kutusu).

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $(1,\,2)$ noktasında $\lVert\nabla f\rVert=\sqrt{16+25}=\sqrt{41}\approx6{,}403$ olur ve en dik doğrultu $(4,\,5)^{\top}/\sqrt{41}\approx(0{,}625;\ 0{,}781)^{\top}$ olur. Hiçbir doğrultunun eğimi daha büyük değildir. Önceki alt kesimdeki $\mathbf{u}=(0{,}6;\ 0{,}8)^{\top}$ doğrultusu bundan yalnızca yaklaşık $1{,}8^\circ$ sapar; bu yüzden onun $6{,}4$ eğimi zaten neredeyse en büyük değerdeydi. Gradyana dik olan $(5,\,-4)^{\top}/\sqrt{41}$ doğrultusunda eğim $(20-20)/\sqrt{41}=0$ olur.
::::

⁠**Kısacası:** Gradyan en dik çıkışın doğrultusunu gösterir, uzunluğu oradaki eğimdir; gradyanın tersi yönünde en dik biçimde yokuş aşağı gidilir.

:::hintergrund En dik doğrultu, adımların nasıl ölçüldüğüne bağlıdır
Teorem, Öklid normunda $\lVert\mathbf{u}\rVert=1$ olan bütün $\mathbf{u}$ doğrultularını karşılaştırır. [Bölüm 1, Kesim 3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3)'te başka normlar da vardı. $\lVert\mathbf{u}\rVert_\infty\le1$ olan bütün adımlara izin verilirse, yani her bileşen $-1$ ile $1$ arasında olabilirse, $\nabla f^{\top}\mathbf{u}=\sum_j\partial_jf\cdot u_j$ ifadesi her $u_j$ bileşeni $\partial_jf$ ile aynı işaretli $+1$ ya da $-1$ değerini aldığında en büyük olur. En dik doğrultu o zaman bileşen bileşen $\operatorname{sign}(\nabla f)$ olur ve eğim $\sum_j|\partial_jf|=\lVert\nabla f\rVert_1$ olur. Buna karşılık $\lVert\mathbf{u}\rVert_1\le1$ olan bütün adımlara izin verilirse bütün bütçe, $|\partial_jf|$ değeri en büyük olan bileşene yatırılır: En dik doğrultu bir koordinat eksenidir ve eğim $\lVert\nabla f\rVert_\infty$ olur. $\nabla f=(4,\,5)^{\top}$ için bu, eğimi $9$ olan $(1,\,1)^{\top}$ ve eğimi $5$ olan $(0,\,1)^{\top}$ doğrultularını verir. “Gradyan en dik doğrultudur” cümlesi bu yüzden Öklid uzunluğuna ilişkin bir önermedir. Değişkenlerin birimlerine de bağlıdır: $x_1$ başka birimlerle ölçülürse adımların uzunlukları ve onlarla birlikte en dik doğrultu değişir, tıpkı [Bölüm 1, Kesim 4.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2)'deki uzaklıklar gibi.
:::

### Gradyan eş yükselti eğrilerine diktir

<span class="anker" id="stufe-4-3"></span>

Bir eş yükselti eğrisi boyunca yürüyen ne çıkar ne iner. Eş yükselti eğrisi doğrultusunda eğim dolayısıyla sıfırdır ve önceki alt kesime göre eğim tam olarak gradyana dik olan doğrultularda sıfırdır. Bu yüzden gradyan eş yükselti eğrisine diktir. Daha kesin söylemek gerekirse:

:::satz Teorem 4.4 (Gradyan ve eş yükselti eğrisi)
<span class="anker" id="satz-4-4"></span>

$f$, $\mathbf{x}$ noktasında türevlenebilir, $\nabla f(\mathbf{x})\ne\mathbf{0}$ ve $c=f(\mathbf{x})$ olsun. Doğrusal yaklaşımın $\mathbf{x}$ noktasından geçen düzey kümesi, yani $\nabla f(\mathbf{x})^{\top}\mathbf{h}=0$ olan $\mathbf{x}+\mathbf{h}$ noktalarının kümesi, iki değişkende $\mathbf{x}$ noktasından geçen ve gradyana dik olan doğrudur. Bu doğru, $f$ fonksiyonunun $c$ değerine ait eş yükselti eğrisinin teğetidir.
:::

Doğrunun eş yükselti eğrisine teğet olması büyüteçten çıkar: $\mathbf{x}$ yakınında $f$ ile doğrusal yaklaşımı yalnızca $\lVert\mathbf{h}\rVert$'den hızlı sıfıra giden bir hata kadar farklıdır; dolayısıyla $c$ değerine ait eş yükselti eğrileri de o kadar az farklıdır ki $\mathbf{x}$ noktasında aynı doğrultuya sahiptirler. Zincir kuralıyla bir ispatı Alıştırma [22](die-kettenregel-fur-mehrere-variablen.html#aufg-22) veriyor. İkiden fazla değişkende aynısı, o zaman bir yüzey olan düzey kümesi için geçerlidir: Gradyan ona diktir.

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2+4x_2^2$ çanağı için $\nabla f(\mathbf{x})=(2x_1,\,8x_2)^{\top}$ olur ve bu, $(1,\,1)$ noktasında $(2,\,8)^{\top}$ eder. Bu noktadan geçen eş yükselti eğrisi $x_1^2+4x_2^2=5$ elipsidir. $\mathbf{t}=(4,\,-1)^{\top}$ doğrultusu gradyana diktir, çünkü $2\cdot4+8\cdot(-1)=0$ olur. $(1,\,1)$ noktasından bu doğrultuda bir $s$ adımı gidilirse şu bulunur:

$$f(1+4s,\ 1-s)=(1+4s)^2+4\,(1-s)^2=5+20s^2 .$$

Değer yalnızca $20s^2$ kadar değişir, yani $s$'den daha hızlı sıfıra gider: Doğru eş yükselti eğrisine değer ve onun teğetidir. Şekil [9](#abb-9) birçok noktadaki gradyanları gösteriyor; her biri kendi başlangıç noktasından geçen eş yükselti eğrisine diktir.

:::abbildung ml/k3hoehen 9
Eş yükselti eğrileri (gri) üzerinde gradyanlar (kırmızı, kısaltılmış çizilmiş). (a) Yuvarlak çanakta bütün gradyanlar tam olarak merkezden dışarıyı gösterir. (b) Uzamış çanakta da eş yükselti eğrilerine diktirler, ama tam olarak merkezden dışarıyı yalnızca eksenler üzerinde gösterirler. $(1,\,1)$ noktasında (siyah) en dik inişin doğrultusu maviyle çizilmiştir. (a)'da bu doğrultu en alçak noktayı gösterir, (b)'de en alçak noktaya giden doğrultudan (kesikli) yaklaşık $31^\circ$ sapar.
:::
::::

⁠**Kısacası:** Bir eş yükselti eğrisi boyunca $f$ değişmez; bu yüzden gradyan ona diktir.

### En dik iniş ve en alçak nokta

<span class="anker" id="stufe-4-4"></span>

Yuvarlak bir çanakta yokuş aşağı en dik yolun merkeze götürmesi apaçıktır. Uzamış bir çanakta bu yanlıştır ve bu fark önemlidir, çünkü gradyandan kolayca bildiğinden fazlası beklenir.

$f(\mathbf{x})=x_1^2+x_2^2$ için $\nabla f(\mathbf{x})=2\mathbf{x}$ olur. Dolayısıyla $-2\mathbf{x}$ negatif gradyanı her noktadan tam olarak çanağın en alçak noktası olan orijini gösterir. $f(\mathbf{x})=x_1^2+4x_2^2$ için $-\nabla f(\mathbf{x})=(-2x_1,\,-8x_2)^{\top}$ olur ve bu yalnızca $x_1=0$ ya da $x_2=0$ olduğunda, yani eksenler üzerinde $-\mathbf{x}$ vektörünün bir katıdır. Başka her yerde en dik iniş en alçak noktanın yanından geçer.

Nedeni eş yükselti eğrilerinin biçimindedir. Gradyan yalnızca arazinin kendi başlangıç noktasında nasıl eğik olduğunu bilir; oradaki eş yükselti eğrisine diktir. Uzamış eş yükselti eğrilerinde dikme, merkeze giden doğrultuya eğik durur. Örnekte $f$, $x_2$ doğrultusunda $x_1$ doğrultusundakinin dört katı hızla artar; çanağın çeperleri $x_2$ doğrultusunda daha diktir ve en dik iniş daha çok onlara dik olarak ilerler.

::::beispiel [Sayısal örnek]
$(1,\,1)$ noktasında $-\nabla f=(-2,\,-8)^{\top}$ olur ve uzunluğu $\sqrt{68}\approx8{,}246$ olduğundan en dik inişin doğrultusu $(-0{,}243;\ -0{,}970)^{\top}$ olur. En alçak noktaya giden doğrultu $(-1,\,-1)^{\top}/\sqrt2\approx(-0{,}707;\ -0{,}707)^{\top}$ olur. İkisi arasındaki açının kosinüsü şudur:

$$\frac{(-2)\cdot(-1)+(-8)\cdot(-1)}{\sqrt{68}\cdot\sqrt2}=\frac{10}{\sqrt{136}}\approx0{,}857,$$

yani açı yaklaşık $31^\circ$ olur. [(4.2)](#gl-4-2) uyarınca en alçak noktanın doğrultusunda eğim yalnızca $-10/\sqrt2\approx-7{,}07$, en dik inişte ise $-8{,}246$ olur.
::::

⁠**Kısacası:** Negatif gradyan yokuş aşağı en dik doğrultuyu gösterir, ama en alçak noktayı yalnızca yuvarlak eş yükselti eğrilerinde gösterir; uzamış eş yükselti eğrilerinde onun yanından geçer.

:::aufgabe Alıştırma 13 ★ Birçok doğrultuda eğimler
<span class="anker" id="aufg-13"></span>

$f(\mathbf{x})=x_1^2+4x_2^2$ ve $\mathbf{x}=(1,\,1)^{\top}$ olsun.

<ol class="al">

<li>

$\mathbf{e}_1$, $\mathbf{e}_2$, $(1,\,1)^{\top}/\sqrt2$ ve $(-1,\,1)^{\top}/\sqrt2$ doğrultularındaki yönlü türevleri hesaplayın.

</li>

<li>

$\lVert\nabla f(\mathbf{x})\rVert$ ile karşılaştırın. Dört doğrultudan hangisi en dik doğrultuya en yakındır?

</li>

</ol>

:::loesung
(a) $\nabla f(1,1)=(2,\,8)^{\top}$ olur. [(4.2)](#gl-4-2) uyarınca:

$$D_{\mathbf{e}_1}f=2,\qquad D_{\mathbf{e}_2}f=8,\qquad D_{(1,1)/\sqrt2}f=\frac{2+8}{\sqrt2}\approx7{,}071,\qquad D_{(-1,1)/\sqrt2}f=\frac{-2+8}{\sqrt2}\approx4{,}243 .$$

(b) $\lVert\nabla f\rVert=\sqrt{68}\approx8{,}246$; [(4.3)](#gl-4-3) bağıntısının gerektirdiği gibi eğimlerin hiçbiri bundan büyük değildir. En dik doğrultuya en yakın olan, $8$ eğimiyle $\mathbf{e}_2$ doğrultusudur. $\mathbf{e}_2$ ile $\nabla f$ arasındaki açının kosinüsü $8/\sqrt{68}\approx0{,}970$ olur, yani açı yaklaşık $14^\circ$ kadardır; $(1,\,1)^{\top}/\sqrt2$ için açı yaklaşık $31^\circ$ kadardır.
:::
:::

:::aufgabe Alıştırma 14 ★★ Eş yükselti eğrisi olarak bir hiperbol
<span class="anker" id="aufg-14"></span>

$f(\mathbf{x})=x_1x_2$ ve $\mathbf{x}=(2,\,1)^{\top}$ olsun.

<ol class="al">

<li>

$\nabla f(\mathbf{x})$ gradyanını, en dik doğrultuyu ve bu doğrultudaki eğimi hesaplayın.

</li>

<li>

$\mathbf{x}$ noktasından geçen eş yükselti eğrisi $x_2=2/x_1$ eğrisidir. Bu eğrinin $x_1=2$ noktasındaki eğimini hesaplayın, teğet doğrultusunu bir vektör olarak yazın ve bu vektörün $\nabla f(\mathbf{x})$ gradyanına dik olduğunu kontrol edin.

</li>

</ol>

:::loesung
(a) $\nabla f(\mathbf{x})=(x_2,\,x_1)^{\top}$, dolayısıyla $(2,\,1)$ noktasında $(1,\,2)^{\top}$. En dik doğrultu $(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$, bu doğrultudaki eğim $\sqrt5\approx2{,}236$ olur.

(b) $x_2=2/x_1$ eş yükselti eğrisinin eğimi $-2/x_1^2$, dolayısıyla $x_1=2$ noktasında $-\tfrac12$ olur. Bir teğet doğrultusu $(1,\,-\tfrac12)^{\top}$ ya da $2$ ile çarpılmış hâliyle $(2,\,-1)^{\top}$ olur. $(1,\,2)(2,\,-1)^{\top}=2-2=0$: Gradyan eş yükselti eğrisine diktir.
:::
:::

:::aufgabe Alıştırma 15 ★★ Doğrusal fonksiyonlar
<span class="anker" id="aufg-15"></span>

Sabit bir $\mathbf{a}\in\mathbb{R}^d$, $\mathbf{a}\ne\mathbf{0}$ vektörü ve bir $b$ sayısıyla $f(\mathbf{x})=\mathbf{a}^{\top}\mathbf{x}+b$ olsun.

<ol class="al">

<li>

Her noktada $\nabla f(\mathbf{x})=\mathbf{a}$ olduğunu gösterin. $d=2$ için eş yükselti eğrileri nelerdir?

</li>

<li>

[Bölüm 1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)'deki daireler için $\mathbf{w}=(3,\,10,\,-4)^{\top}$ olmak üzere $\hat y=\mathbf{w}^{\top}\mathbf{x}+b$ olur; burada $x_1$, $\mathrm m^2$ cinsinden alan, $x_2$ oda sayısı, $x_3$ de km cinsinden merkeze uzaklıktır. Özniteliklerde $\lVert\mathbf{u}\rVert=1$ olan hangi $\mathbf{u}$ değişimi tahmini en çok artırır ve ne kadar?

</li>

<li>

Alan $10\,\mathrm m^2$ cinsinden verilirse $w_1=3$ ağırlığı $30$ olur. En dik doğrultu şimdi nedir? Buradan en dik çıkış teoremi hakkında ne öğrenilir?

</li>

</ol>

:::loesung
(a) $\partial_k(\mathbf{a}^{\top}\mathbf{x}+b)=a_k$, dolayısıyla her yerde $\nabla f=\mathbf{a}$. $d=2$ için eş yükselti eğrileri $a_1x_1+a_2x_2+b=c$ doğrularıdır; bu doğrular birbirine paraleldir ve $\mathbf{a}$ vektörüne diktir.

(b) $\mathbf{x}$'e göre gradyan $\mathbf{w}=(3,\,10,\,-4)^{\top}$, uzunluğu $\lVert\mathbf{w}\rVert=\sqrt{9+100+16}=\sqrt{125}\approx11{,}18$ olur. Uzunluğu $1$ olan en dik değişim $\mathbf{u}=\mathbf{w}/\sqrt{125}\approx(0{,}268;\ 0{,}894;\ -0{,}358)^{\top}$ olur ve tahmini yaklaşık $11{,}18$ bin avro artırır: biraz daha fazla alan, belirgin biçimde daha fazla oda ve merkeze biraz daha yakın.

(c) Yeni birimlerde $\mathbf{w}'=(30,\,10,\,-4)^{\top}$, uzunluğu $\lVert\mathbf{w}'\rVert=\sqrt{1016}\approx31{,}87$ olur; en dik doğrultu ise $\mathbf{w}'/\lVert\mathbf{w}'\rVert\approx(0{,}941;\ 0{,}314;\ -0{,}125)^{\top}$ olur: Doğrultu artık neredeyse tamamen alan yönündedir. Aynı daire, aynı fiyatlar, ama başka bir en dik doğrultu. En dik çıkış teoremi, seçilen koordinatlarda aynı Öklid uzunluğuna sahip adımları karşılaştırır; “uzunluk $1$” ifadesinin ne anlama geldiği de, tıpkı [Bölüm 1, Kesim 4.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2)'deki uzaklıklar gibi, birimlere bağlıdır. Farklı birimlerdeki özniteliklerde en dik doğrultu ancak [Bölüm 1, Kesim 4.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5)'teki standartlaştırmadan sonra anlamlı olur.
:::
:::

:::aufgabe Alıştırma 16 ★★★ En dik iniş ne zaman merkeze yönelir?
<span class="anker" id="aufg-16"></span>

$a,b>0$ sayılarıyla $f(\mathbf{x})=a\,x_1^2+b\,x_2^2$ olsun.

<ol class="al">

<li>

Şunu gösterin: $-\nabla f(\mathbf{x})$, ancak ve ancak $a=b$ ise ya da $\mathbf{x}$ eksenlerden biri üzerindeyse ($\mathbf{x}\ne\mathbf{0}$) $-\mathbf{x}$ vektörünün pozitif bir katıdır.

</li>

<li>

$a=1$, $b=4$ için $(1,\,1)$, $(2,\,1)$ ve $(4,\,1)$ noktalarında $-\nabla f$ ile $-\mathbf{x}$ arasındaki açıyı hesaplayın. $x_2=1$ doğrusu üzerinde dışarı doğru gidildikçe açı nasıl değişir?

</li>

</ol>

:::loesung
(a) $-\nabla f(\mathbf{x})=(-2ax_1,\,-2bx_2)^{\top}$ olur. Bu vektör, ancak ve ancak $2ax_1=c\,x_1$ ve $2bx_2=c\,x_2$ ise bir $c>0$ ile $c\,(-x_1,\,-x_2)^{\top}$ vektörüne eşittir. İki koordinat da sıfırdan farklıysa $2a=c=2b$, dolayısıyla $a=b$ çıkar. $x_1=0$ ise $c=2b$ yeterlidir; $x_2=0$ ise $c=2a$ yeterlidir. Demek ki yuvarlak bir çanakta en dik iniş her yerde orijine yönelir, uzamış bir çanakta ise yalnızca eksenler üzerinde.

(b) $a=1$, $b=4$ için $-\nabla f=(-2x_1,\,-8x_2)^{\top}$ olur:

$$\begin{aligned} (1,\,1)&:\ \cos\varphi=\frac{2+8}{\sqrt{68}\,\sqrt2}\approx0{,}857,\ \varphi\approx31{,}0^\circ;\\ (2,\,1)&:\ \cos\varphi=\frac{8+8}{\sqrt{80}\,\sqrt5}=0{,}8,\ \varphi\approx36{,}9^\circ;\\ (4,\,1)&:\ \cos\varphi=\frac{32+8}{\sqrt{128}\,\sqrt{17}}\approx0{,}857,\ \varphi\approx31{,}0^\circ . \end{aligned}$$

$x_2=1$ doğrusu üzerinde açı, $x_1=0$ noktasındaki $0^\circ$ değerinden önce büyür, sonra yeniden küçülür; çok dışarıda nokta neredeyse $x_1$ ekseni doğrultusunda bulunur ve en dik iniş orada yeniden neredeyse merkeze yönelir.
:::
:::
