---
title: Sayısal türev ve gradyan kontrolü
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15231200
summary: Türevler formül olmadan da kestirilebilir: Fonksiyon birbirine yakın iki noktada hesaplanır ve fark bölümü oluşturulur.
tags: ileri fark, kesme hatası, merkezi fark, kayan noktalı sayılar, makine epsilonu, anlamlı basamak kaybı, Gradyan kontrolü, bağıl hata
lang: tr
---

<span class="anker" id="stufe-11"></span>

:::zweck
Türevler formül olmadan da kestirilebilir: Fonksiyon birbirine yakın iki noktada hesaplanır ve fark bölümü oluşturulur. Bu, çok girdili bir fonksiyonun bütün türevlerini hesaplamak için fazla yavaştır, ama türetilmiş ya da programlanmış bir türevi kontrol etmek için idealdir. Bu kesim, yaygın iki fark bölümünün ne kadar doğru olduğunu, fazla küçük bir adım büyüklüğünün neden zarar verdiğini ve bir gradyan kontrolünün nasıl yapılıp değerlendirildiğini gösteriyor.
:::

### İleri fark

<span class="anker" id="stufe-11-1"></span>

[(1.3)](die-ableitung.html#gl-1-3) tanımına göre fark bölümü, $h$ sıfıra giderken türeve yaklaşır. Sabit küçük bir $h$ ile hesaplanırsa bir yaklaşık değer elde edilir ve soru, bunun ne kadar iyi olduğudur.

:::definition Tanım 11.1 (İleri fark)
<span class="anker" id="satz-11-1"></span>

Sabit bir $h>0$ adım büyüklüğü için

<span class="anker" id="gl-11-1"></span>
$$D_+f(x)=\frac{f(x+h)-f(x)}{h} \tag{11.1}$$

ifadesine __ileri fark__ denir. Bu ifadenin, yalnızca $h$'nin sıfır olmamasından kaynaklanan, $f'(x)$'ten sapmasına __kesme hatası__ denir.
:::

Kesme hatasını [(1.6)](die-ableitung.html#gl-1-6) ikinci dereceden yaklaşımı verir: $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$ yerine konursa şu bulunur:

<span class="anker" id="gl-11-2"></span>
$$D_+f(x)\approx f'(x)+\tfrac12f''(x)\,h . \tag{11.2}$$

Demek ki hata yaklaşık olarak $h$ ile orantılıdır: On kat küçük $h$, yaklaşık on kat küçük kesme hatası verir.

::::beispiel [Sayısal örnek]
$2$ noktasında $h=10^{-3}$ ile $f(x)=x^3$ için $2{,}001^3=8{,}012006001$ ve şu bulunur:

$$D_+f(2)=\frac{8{,}012006001-8}{0{,}001}=12{,}006001 .$$

$0{,}006001$ hatası $\tfrac12f''(2)\,h=\tfrac12\cdot12\cdot0{,}001=0{,}006$ değerine uyar; kalan $0{,}000001=h^2$ bir sonraki terimdir.
::::

⁠**Kısacası:** İleri farkın kesme hatası yaklaşık $\tfrac12f''(x)\,h$ olur, adım büyüklüğüyle orantılıdır.

### Merkezi fark

<span class="anker" id="stufe-11-2"></span>

İleri fark, $x$ ile $x+h$ arasındaki kesenin eğimini ölçer ve bu kesen, kavisli bir eğride $x$ noktasındaki teğetten sistematik olarak daha dik ya da daha yatıktır. Kesen $x$ etrafında simetrik olarak, $x-h$'den $x+h$'ye konursa bu hata dengelenir.

:::definition Tanım 11.2 (Merkezi fark)
<span class="anker" id="satz-11-2"></span>

Sabit bir $h>0$ adım büyüklüğü için

<span class="anker" id="gl-11-3"></span>
$$D_0f(x)=\frac{f(x+h)-f(x-h)}{2h} \tag{11.3}$$

ifadesine __merkezi fark__ denir.
:::

:::satz Teorem 11.3 (Merkezi farkın kesme hatası)
<span class="anker" id="satz-11-3"></span>

$f$ fonksiyonunun sürekli bir üçüncü türevi varsa şu geçerlidir:

<span class="anker" id="gl-11-4"></span>
$$D_0f(x)\approx f'(x)+\tfrac16f'''(x)\,h^2 . \tag{11.4}$$

Demek ki kesme hatası yaklaşık olarak $h^2$ ile orantılıdır.
:::

:::herleitung Eğrilik neden sadeleşir
Kesim [1.5](die-ableitung.html#stufe-1-5)'teki ikinci dereceden yaklaşım bir terim daha sürdürülür. Oradaki parabolde olduğu gibi ek olarak üçüncü türev de eşleştirilirse $\tfrac16f'''(x)\,h^3$ terimi eklenir; $\tfrac16$ çarpanı, $h^3$ ifadesinin üçüncü türevi $6$ olduğu için ortaya çıkar. Böylece şu bulunur:

$$f(x\pm h)\approx f(x)\pm f'(x)\,h+\tfrac12f''(x)\,h^2\pm\tfrac16f'''(x)\,h^3 .$$

İki denklem birbirinden çıkarılırsa $h$'nin çift kuvvetlerini içeren terimler düşer, çünkü iki tarafta da aynı işarete sahiptirler: $f(x)$ ve $\tfrac12f''h^2$ eğrilik terimi. Geriye $f(x+h)-f(x-h)\approx2f'(x)\,h+\tfrac13f'''(x)\,h^3$ kalır ve $2h$'ye bölmek [(11.4)](#gl-11-4) bağıntısını verir. Görsel olarak: Eğrilik sağdaki keseni daha dik, soldakini daha yatık yapar ve merkezi fark ikisinin ortalamasıdır.
:::

İkinci dereceden bir fonksiyon için $f'''=0$ olur ve merkezi fark her $h$ için tamdır. Merkezi fark $f$ fonksiyonunun iki yeni değerlendirmesini gerektirir; ileri fark ise $f(x)$ zaten biliniyorsa yalnızca birini.

::::beispiel [Sayısal örnek]
$2$ noktasında $h=10^{-3}$ ile $f(x)=x^3$ için $1{,}999^3=7{,}988005999$ ve şu bulunur:

$$D_0f(2)=\frac{8{,}012006001-7{,}988005999}{0{,}002}=\frac{0{,}024000002}{0{,}002}=12{,}000001 .$$

Hata $0{,}000001=\tfrac16\cdot6\cdot h^2$ olur, ileri farktakinden altı bin kat küçük.
::::

⁠**Kısacası:** Merkezi farkın kesme hatası yaklaşık $\tfrac16f'''(x)\,h^2$ olur, çünkü eğrilik terimi sadeleşir.

### Bunun için gerekenler: kayan noktalı sayılar

<span class="anker" id="stufe-11-3"></span>

Kesme hatası için iki formüle göre $h$'yi yalnızca yeterince küçük seçmek gerekirdi. Hesap makinesiyle ve her hesaplama programıyla bu ters gider ve nedeni bilgisayarların sayıları saklama biçimidir.

Bilgisayarlar ondalıklı sayıları __kayan noktalı sayılar__ olarak saklar: ikili sistemde sabit sayıda basamağı olan bir sayı çarpı ikinin bir kuvveti olarak. Yaygın olan, IEEE 754 standardına göre $53$ ikili basamaklı, yani yaklaşık $16$ ondalık basamaklı çift duyarlıktır. Her hesap işleminin sonucu temsil edilebilen en yakın sayıya yuvarlanır. Bu yuvarlamanın bağıl hatası en fazla $2^{-53}\approx1{,}1\cdot10^{-16}$ olur. $1$ ile temsil edilebilen bir sonraki büyük sayı arasındaki uzaklık bunun iki katıdır,

$$\varepsilon_{\mathrm M}=2^{-52}\approx2{,}2\cdot10^{-16};$$

bu sayıya __makine epsilonu__ denir ve hesaplama programları onu eps adıyla verir. $24$ ikili basamaklı, yani yaklaşık $7$ ondalık basamaklı tek duyarlıkta $\varepsilon_{\mathrm M}=2^{-23}\approx1{,}2\cdot10^{-7}$ olur.

Yuvarlama, birbirine çok yakın sayılar çıkarılırken tehlikeli hâle gelir. Öndeki basamaklar birbirini götürür, arkadakilerin yuvarlama hataları kalır ve sonucun yalnızca birkaç basamağı doğru olur. Buna __anlamlı basamak kaybı__ (yıkıcı sadeleşme) denir. Bir fark bölümü tam olarak böyle sayıları birbirinden çıkarır ve $h$ ne kadar küçükse sayılar birbirine o kadar benzer.

::::beispiel [Sayısal örnek]
$2$ noktasında ve $h=10^{-8}$ için $f(x)=x^3$ fonksiyonunda $f(2+h)=8{,}00000012\ldots$ olur. İki fonksiyon değeri de yaklaşık $8$'dir ve her biri yaklaşık $8\cdot1{,}1\cdot10^{-16}\approx9\cdot10^{-16}$ büyüklüğüne kadar bir yuvarlama hatası taşır. Farkları yaklaşık $1{,}2\cdot10^{-7}$ olur; bunun içindeki $10^{-15}$'lik bir hata, neredeyse $10^{-8}$'lik bir bağıl hatadır. Demek ki çıkarmadan sonra $16$ basamaktan yalnızca yaklaşık $8$'i doğrudur ve $h$'ye bölmek bunu değiştirmez.
::::

⁠**Kısacası:** Bilgisayarlar her sonucu yaklaşık $16$ basamağa yuvarlar, $\varepsilon_{\mathrm M}=2^{-52}$; birbirine çok yakın sayılar çıkarılırken bunlardan yalnızca birkaç doğru basamak kalır.

### Hata eğrisi

<span class="anker" id="stufe-11-4"></span>

Demek ki bir fark bölümünde iki hata birbirine karşı çalışır. Kesme hatası küçülen $h$ ile küçülür. Yuvarlama hatası küçülen $h$ ile büyür: Pay kısmındaki farkın hatası yaklaşık aynı kalır, ama gittikçe küçülen bir $h$'ye bölünür.

:::satz Teorem 11.4 (Fark bölümlerinin toplam hatası)
<span class="anker" id="satz-11-4"></span>

Fonksiyon değerleri en fazla $\tfrac12\varepsilon_{\mathrm M}$ bağıl hatayla doğruysa toplam hata, ileri fark ve merkezi fark için sırasıyla kabaca en fazla

<span class="anker" id="gl-11-5"></span>
$$E_+(h)=\tfrac12|f''(x)|\,h+\frac{\varepsilon_{\mathrm M}|f(x)|}{h}\qquad\text{ve}\qquad E_0(h)=\tfrac16|f'''(x)|\,h^2+\frac{\varepsilon_{\mathrm M}|f(x)|}{2h} \tag{11.5}$$

olur. $E_+$ en küçük değerini $h_+=\sqrt{2\varepsilon_{\mathrm M}|f|/|f''|}$ noktasında, $\sqrt{2\varepsilon_{\mathrm M}|f|\,|f''|}$ değeriyle alır; $E_0$ ise en küçük değerini $h_0=\bigl(\tfrac32\varepsilon_{\mathrm M}|f|/|f'''|\bigr)^{1/3}$ noktasında alır.
:::

:::herleitung En iyi adım büyüklüğü
Pay kısmında, her biri en fazla $\tfrac12\varepsilon_{\mathrm M}|f|$ büyüklüğünde yuvarlama hatası taşıyan iki fonksiyon değeri durur, birlikte en fazla $\varepsilon_{\mathrm M}|f|$. İleri farkta bu $h$'ye, merkezi farkta $2h$'ye bölünür. Buna [(11.2)](#gl-11-2) ve [(11.4)](#gl-11-4) kesme hataları eklenir. $a,b>0$ olmak üzere $a\,h+b/h$ biçimindeki bir fonksiyonun türevi $a-b/h^2$ olur ve bu türev $h=\sqrt{b/a}$ noktasında sıfır olur; orada değer $2\sqrt{ab}$ olur. $a=\tfrac12|f''|$ ve $b=\varepsilon_{\mathrm M}|f|$ ile bu, $h_+$ değerini verir. $a\,h^2+b/h$ için türev $2ah-b/h^2$ olur ve $h^3=b/(2a)$ noktasında sıfır olur; $a=\tfrac16|f'''|$ ve $b=\tfrac12\varepsilon_{\mathrm M}|f|$ ile bu, $h_0$ değerini verir.
:::

Hata $h$'ye karşı log-log ölçekte çizilirse bir V ortaya çıkar (Şekil [20](#abb-20)). Sağda eğri $1$ (ileri) ya da $2$ (merkezi) eğimiyle yükselir, çünkü orada kesme hatası baskındır. Solda $-1$ eğimiyle düşer, çünkü orada yuvarlama hatası baskındır. Soldaki ölçülen noktalar dağılır, çünkü yuvarlama hataları sayıya göre daha büyük ya da daha küçük çıkar; [(11.5)](#gl-11-5) yalnızca bunların büyüklük mertebesini verir. Pratik kural olarak ileri farkta $h\approx\sqrt{\varepsilon_{\mathrm M}}\approx10^{-8}$, merkezi farkta $h\approx\varepsilon_{\mathrm M}^{1/3}\approx6\cdot10^{-6}$ seçilir; $|x|$, $1$'den büyükse her biri $x$'in büyüklük mertebesiyle çarpılır.

:::abbildung ml/k3vkurve 20
$2$ noktasında $f(x)=x^3$ için iki fark bölümünün çift duyarlıkla hesaplanmış hatası; $10^{-15}$ ile $10^{-1}$ arasındaki $h$ adım büyüklüğüne karşı, iki eksen de logaritmik. Sağda kesme hatası (eğim $1$ ya da $2$), solda yuvarlama hatası (eğim $-1$) baskındır. Kesikli eğriler [(11.5)](#gl-11-5) kestirimleridir; en alçak noktalar $h\approx10^{-8}$ (ileri) ve $h\approx3\cdot10^{-6}$ (merkezi) civarındadır.
:::

::::beispiel [Sayısal örnek]
$2$ noktasında $f(x)=x^3$ için $|f|=8$, $|f''|=12$ ve $|f'''|=6$ olur. İleri farkın en iyi adım büyüklüğü $h_+=\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8/12}\approx1{,}7\cdot10^{-8}$, hatası yaklaşık $\sqrt{2\cdot2{,}2\cdot10^{-16}\cdot8\cdot12}\approx2{,}1\cdot10^{-7}$ olur; $f'(2)=12$ değerine göre bu, yaklaşık sekiz doğru basamak demektir. Merkezi farkın en iyi adım büyüklüğü $h_0=(1{,}5\cdot2{,}2\cdot10^{-16}\cdot8/6)^{1/3}\approx7{,}6\cdot10^{-6}$, hatası yaklaşık $(7{,}6\cdot10^{-6})^2+2{,}2\cdot10^{-16}\cdot8/(2\cdot7{,}6\cdot10^{-6})\approx1{,}7\cdot10^{-10}$, yani yaklaşık on bir doğru basamak olur. Şekil [20](#abb-20) ikisini de doğruluyor: $h=10^{-8}$ için $7{,}3\cdot10^{-8}$ ve $h\approx3{,}2\cdot10^{-6}$ için $2{,}0\cdot10^{-11}$ ölçüldü. $h=10^{-14}$ ile ise iki bölümde de virgülden sonraki ilk basamak bile yanlıştır.
::::

⁠**Kısacası:** Fazla büyük $h$ kesme hatası, fazla küçüğü yuvarlama hatası verir; en iyisi ileri farkta $h\approx10^{-8}$, merkezi farkta $h\approx10^{-5}$ ile $10^{-6}$ arasıdır ve merkezi fark bu sırada sekiz yerine yaklaşık on bir doğru basamağa ulaşır.

### Gradyan kontrolü

<span class="anker" id="stufe-11-5"></span>

Bir gradyanı elle türeten ya da geri adımlar olarak programlayan kişi kolayca hata yapar: unutulmuş bir yol, eksik bir devrik, yanlış bir çarpan. Bir fark bölümü türetmeye ihtiyaç duymaz, yalnızca fonksiyonu hesaplar. İkisi karşılaştırılırsa bu tür hatalar güvenilir biçimde bulunur.

:::definition Tanım 11.5 (Gradyan kontrolü)
<span class="anker" id="satz-11-5"></span>

__Gradyan kontrolü__nde bir $\mathbf{x}$ noktasında hesaplanan bir $\mathbf{g}_{\mathrm a}$ gradyanı, bileşenleri merkezi farklar olan $\mathbf{g}_{\mathrm n}$ sayısal gradyanıyla karşılaştırılır:

<span class="anker" id="gl-11-6"></span>
$$g_{\mathrm n,j}=\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x}-h\,\mathbf{e}_j)}{2h}. \tag{11.6}$$

Bu sırada her bileşen için __bağıl hata__ hesaplanır:

<span class="anker" id="gl-11-7"></span>
$$\rho_j=\frac{|g_{\mathrm a,j}-g_{\mathrm n,j}|}{\max\bigl(|g_{\mathrm a,j}|,\,|g_{\mathrm n,j}|\bigr)}, \tag{11.7}$$

burada iki değer de sıfırsa $\rho_j=0$ konur.
:::

Bağıl olarak karşılaştırılır, çünkü $10^{-6}$'lık mutlak bir hata, $10^{6}$ büyüklüğünde bir türevde mükemmeldir, ama $10^{-6}$ büyüklüğünde bir türevde tam bir başarısızlıktır. Çift duyarlıkla hesapta ve $10^{-5}$ mertebesinde bir $h$ ile şu deneyim değerleri geçerlidir: $10^{-2}$'nin üzerindeki bir bağıl hata neredeyse kesinlikle formülde bir hata demektir. $10^{-2}$ ile $10^{-4}$ arasında sonuç şüphelidir. $10^{-4}$'ün altında sonuç, köşe noktaları olan fonksiyonlarda çoğunlukla sorunsuzdur ve $10^{-7}$ ya da daha azı iyi bir sonuçtur. Bir kontrol $f$ fonksiyonunun $2n$ değerlendirmesine mal olur; bu yüzden yalnızca birkaç noktada ya da yalnızca bazı bileşenler kontrol edilir. Asıl hesap için ters mod, onun denetimi için fark bölümü vardır.

::::beispiel [Sayısal örnek 1]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için birisi, unutulmuş bir $2$ çarpanıyla, $(2x_1x_2,\ x_1^2+x_2)^{\top}$ gradyanını türetmiş olsun. $(1,\,2)$ noktasında bu $\mathbf{g}_{\mathrm a}=(4,\,3)^{\top}$ olur. $h=0{,}001$ ile şu bulunur:

$$\begin{aligned} g_{\mathrm n,1}&=\frac{f(1{,}001;\ 2)-f(0{,}999;\ 2)}{0{,}002}=\frac{6{,}004002-5{,}996002}{0{,}002}=4,\\ g_{\mathrm n,2}&=\frac{f(1;\ 2{,}001)-f(1;\ 1{,}999)}{0{,}002}=\frac{6{,}005001-5{,}995001}{0{,}002}=5 . \end{aligned}$$

Merkezi farklar burada tamdır, çünkü $f$ her bir değişkende en fazla ikinci derecedendir. Bağıl hatalar $\rho_1=0$ ve $\rho_2=|3-5|/5=0{,}4$ olur: İkinci bileşen yanlıştır.
::::

::::beispiel [Sayısal örnek 2]
$\sigma'(x)=\sigma(x)(1-\sigma(x))$ formülü $1$ noktasında kontrol ediliyor. On basamakla $\sigma(1)\approx0{,}7310585786$ olur ve formül $0{,}7310585786\cdot0{,}2689414214\approx0{,}1966119332$ verir. $h=0{,}01$ ile $\sigma(1{,}01)\approx0{,}7330201492$ ve $\sigma(0{,}99)\approx0{,}7290879223$, dolayısıyla şu bulunur:

$$g_{\mathrm n}=\frac{0{,}7330201492-0{,}7290879223}{0{,}02}=\frac{0{,}0039322269}{0{,}02}\approx0{,}196611345 .$$

Bağıl hata $\rho\approx5{,}9\cdot10^{-7}/0{,}1966\approx3{,}0\cdot10^{-6}$ olur. Bu hata görece büyük adım büyüklüğünün kesme hatasından gelir ve $10^{-2}$ eşiğinin çok altındadır; formül doğrudur. Çift duyarlıkla $h=10^{-5}$ alınırsa hata yaklaşık $10^{-11}$'e düşer.
::::

⁠**Kısacası:** Gradyan kontrolü hesaplanan bir gradyanı bileşen bileşen merkezi farklarla karşılaştırır; $10^{-2}$'nin üzerindeki bağıl hatalar formülde bir hata olduğunu, $10^{-7}$'nin altındakiler doğru bir formülü gösterir.

### Köşe noktaları ve diğer tuzaklar

<span class="anker" id="stufe-11-6"></span>

Bir gradyan kontrolü, formül doğru olduğu hâlde alarm verebilir ya da formül yanlış olduğu hâlde susabilir. En sık nedenler önceden kestirilebilir.

Birinci neden köşe noktalarıdır. $|x|$ ya da $\max(x,\,0)$ fonksiyonunun $0$ noktasındaki gibi bir köşe noktasında türev yoktur. $x-h$ ile $x+h$ arasında bir köşe noktası varsa merkezi fark soldaki ve sağdaki iki eğimin bir karışımını ölçer, hesaplanan türev ise bunlardan yalnızca birini bilir. İkinci neden fazla düşük duyarlıktır. Tek duyarlıkta $\varepsilon_{\mathrm M}\approx1{,}2\cdot10^{-7}$ olur; [(11.5)](#gl-11-5) uyarınca merkezi farkın en iyi adım büyüklüğü o zaman yaklaşık $10^{-2}$ civarındadır ve formül doğru olsa bile $10^{-5}$ ile $10^{-3}$ civarındaki bağıl hatalar normaldir. Üçüncüsü, yuvarlama hatasını yükselten fazla küçük bir adım büyüklüğüdür. Dördüncüsü çok küçük gradyanlardır: İki değer de neredeyse sıfırsa bağıl hata pek bir şey söylemez ve ek olarak mutlak hataya bakılır. Son olarak, özel bir noktada değil, rastgele bir noktada kontrol yapılmalıdır: $\mathbf{x}=\mathbf{0}$ noktasında bir formülün birçok terimi sıfır olur ve onlarla birlikte bu terimlerde saklı hatalar da kaybolur.

:::warnung Yalnızca kontrol edilen kontrol edilmiştir
Bir noktada geçilen bir gradyan kontrolü, formülün her yerde değil, orada doğru olduğunu gösterir. Kontrol edilen noktada sıfır olan unutulmuş bir terim göze çarpmaz. Bu yüzden düzensiz sayılarla birkaç noktada ve farklı biçimde hesaplanan bütün bileşenleri kontrol edin.
:::

::::beispiel [Sayısal örnek]
$x=10^{-6}$ noktasında $f(x)=|x|$ için türev $1$ olur. $h=10^{-5}$ ile $0$'daki köşe noktası $x-h$ ile $x+h$ arasında kalır ve şu bulunur:

$$D_0f(10^{-6})=\frac{|1{,}1\cdot10^{-5}|-|-0{,}9\cdot10^{-5}|}{2\cdot10^{-5}}=\frac{0{,}2\cdot10^{-5}}{2\cdot10^{-5}}=0{,}1 .$$

Bağıl hata $0{,}9$ olur, oysa $x>0$ için $f'(x)=1$ formülü doğrudur. $h=10^{-7}$ ile köşe noktası dışarıda kalır ve merkezi fark tam olarak $1$ olur.
::::

⁠**Kısacası:** Köşe noktaları, tek duyarlık, fazla küçük adım büyüklükleri ve sıfıra yakın gradyanlar kontrolü bozar; birkaç düzensiz noktada kontrol yapılır.

:::aufgabe Alıştırma 39 ★ İki fark bölümü
<span class="anker" id="aufg-39"></span>

$f(x)=\mathrm{e}^x$ ve $x=0$, dolayısıyla $f'(0)=1$ olsun.

<ol class="al">

<li>

Hesap makinesiyle $h=0{,}1$ ve $h=0{,}01$ için $D_+f(0)$ ve $D_0f(0)$ değerlerini hesaplayın.

</li>

<li>

Hataları $\tfrac12f''(0)\,h$ ve $\tfrac16f'''(0)\,h^2$ yaklaşımlarıyla karşılaştırın.

</li>

</ol>

:::loesung
(a) $\mathrm{e}^{0{,}1}\approx1{,}105170918$, $\mathrm{e}^{-0{,}1}\approx0{,}904837418$, $\mathrm{e}^{0{,}01}\approx1{,}010050167$ ve $\mathrm{e}^{-0{,}01}\approx0{,}990049834$ ile:

$$\begin{aligned} h=0{,}1:&\quad D_+=\frac{1{,}105170918-1}{0{,}1}\approx1{,}05171,\\ &\quad D_0=\frac{1{,}105170918-0{,}904837418}{0{,}2}\approx1{,}001668;\\ h=0{,}01:&\quad D_+=\frac{1{,}010050167-1}{0{,}01}\approx1{,}005017,\\ &\quad D_0=\frac{1{,}010050167-0{,}990049834}{0{,}02}\approx1{,}0000167 . \end{aligned}$$

(b) İleri farkın hataları $0{,}0517$ ve $0{,}0050$ olur; $\tfrac12h$ yaklaşımı $0{,}05$ ve $0{,}005$ öngörür. Merkezi farkın hataları $0{,}00167$ ve $0{,}0000167$ olur; $\tfrac16h^2$ yaklaşımı $0{,}00167$ ve $0{,}0000167$ öngörür. On kat küçük $h$, hatalardan birini on kat, ötekini yüz kat küçültür.
:::
:::

:::aufgabe Alıştırma 40 ★★ Bir gradyan kontrolü
<span class="anker" id="aufg-40"></span>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ için birisi $\nabla f(\mathbf{x})=(\mathrm{e}^{x_2},\ \mathrm{e}^{x_2})^{\top}$ olduğunu iddia ediyor.

<ol class="al">

<li>

$(2,\,0)$ noktasında $h=0{,}01$ ile sayısal gradyanı ve iki bileşenin bağıl hatalarını hesaplayın. Hangi bileşen yanlıştır?

</li>

<li>

$(1,\,0)$ noktasındaki kontrol neden uygun olmazdı?

</li>

</ol>

:::loesung
(a) $x_1$'e göre: $\frac{f(2{,}01;\,0)-f(1{,}99;\,0)}{0{,}02}=\frac{2{,}01-1{,}99}{0{,}02}=1$; iddia $\mathrm{e}^0=1$ diyor, dolayısıyla $\rho_1=0$. $x_2$'ye göre:

$$g_{\mathrm n,2}=\frac{2\,\mathrm{e}^{0{,}01}-2\,\mathrm{e}^{-0{,}01}}{0{,}02}\approx\frac{2{,}0201003-1{,}9800997}{0{,}02}\approx2{,}0000333 .$$

İddia $1$ diyor, dolayısıyla $\rho_2=|1-2{,}0000333|/2{,}0000333\approx0{,}5$. İkinci bileşen yanlıştır; doğrusu $x_1\mathrm{e}^{x_2}=2$ olur.

(b) $(1,\,0)$ noktasında $x_1\mathrm{e}^{x_2}=1=\mathrm{e}^{x_2}$ olur: Yanlış formül orada rastlantı sonucu doğru formülle örtüşür ve kontrol, kesme hatasından kaynaklanan yalnızca yaklaşık $2\cdot10^{-5}$ bağıl hata verirdi. Bu yanlışlık fark edilmeden kalırdı.
:::
:::

:::aufgabe Alıştırma 41 ★★ En iyi adım büyüklüğü
<span class="anker" id="aufg-41"></span>

$f(x)=\mathrm{e}^x$, $1$ noktasında olsun, dolayısıyla $f=f''=f'''=\mathrm{e}$.

<ol class="al">

<li>

Çift duyarlık için [(11.5)](#gl-11-5) uyarınca $h_+$, $h_0$ ve bunlara ait en küçük hataları hesaplayın.

</li>

<li>

Hesabı tek duyarlık için tekrarlayın. O zaman en fazla kaç doğru basamak beklenebilir?

</li>

</ol>

:::loesung
(a) $|f|=|f''|=|f'''|=\mathrm{e}$ ve $\varepsilon_{\mathrm M}\approx2{,}22\cdot10^{-16}$ ile:

$$\begin{aligned} h_+&=\sqrt{2\varepsilon_{\mathrm M}}\approx2{,}1\cdot10^{-8}, & E_+(h_+)&=\mathrm{e}\sqrt{2\varepsilon_{\mathrm M}}\approx5{,}7\cdot10^{-8},\\ h_0&=(1{,}5\,\varepsilon_{\mathrm M})^{1/3}\approx6{,}9\cdot10^{-6}, & E_0(h_0)&=\tfrac{\mathrm{e}}6h_0^2+\frac{\varepsilon_{\mathrm M}\mathrm{e}}{2h_0}\approx6{,}5\cdot10^{-11}. \end{aligned}$$

$f'(1)=\mathrm{e}$ değerine göre bunlar yaklaşık $2\cdot10^{-8}$ ve $2\cdot10^{-11}$ bağıl hatalardır, yani sekizden ve on birden biraz az doğru basamak.

(b) $\varepsilon_{\mathrm M}\approx1{,}19\cdot10^{-7}$ ile $h_+\approx4{,}9\cdot10^{-4}$, $E_+\approx1{,}3\cdot10^{-3}$ ve $h_0\approx5{,}6\cdot10^{-3}$, $E_0\approx4{,}3\cdot10^{-5}$ olur. $\mathrm{e}$ değerine göre bunlar yaklaşık $5\cdot10^{-4}$ ve $1{,}6\cdot10^{-5}$ eder: En fazla sırasıyla yaklaşık üç ve beş doğru basamak beklenebilir. Bu yüzden tek duyarlıkta yapılan bir gradyan kontrolü, formül doğru olsa bile $10^{-5}$ ile $10^{-3}$ arasında bağıl hatalar verir.
:::
:::

:::aufgabe Alıştırma 42 ★★★ Grafikte köşe noktası
<span class="anker" id="aufg-42"></span>

$f(\mathbf{x})=\max(x_1,\,x_2)\cdot x_3$ olsun.

<ol class="al">

<li>

$(2;\ 2{,}000001;\ 3)$ noktasında gradyanı ters modda hesaplayın.

</li>

<li>

$x_1$'e göre merkezi farkı $h=10^{-5}$ ile, ayrıca bağıl hatayı hesaplayın. Formül yanlış mı?

</li>

<li>

Ters mod $(2,\,2,\,3)$ noktasında ne verir ve orada neden gradyan yoktur?

</li>

</ol>

:::loesung
(a) $(2;\ 2{,}000001;\ 3)$ noktasında $v=\max(x_1,x_2)=x_2=2{,}000001$ ve $f=6{,}000003$ olur. Geriye doğru: $\bar f=1$, $\bar v=x_3=3$, $\bar x_3=v=2{,}000001$; maksimum, $\bar v$ değerini büyük olan $x_2$ girdisine iletir, dolayısıyla $\bar x_2=3$ ve $\bar x_1=0$. Gradyan $(0;\ 3;\ 2{,}000001)^{\top}$ olur.

(b) $f(2{,}00001;\ 2{,}000001;\ 3)=3\cdot2{,}00001=6{,}00003$ ve $f(1{,}99999;\ 2{,}000001;\ 3)=3\cdot2{,}000001=6{,}000003$, dolayısıyla

$$g_{\mathrm n,1}=\frac{6{,}00003-6{,}000003}{0{,}00002}=\frac{0{,}000027}{0{,}00002}=1{,}35$$

ve $\rho_1=|0-1{,}35|/1{,}35=1$ olur. Formül yine de doğrudur. $x_1=x_2$ olan yerdeki köşe noktası $x_1-h$ ile $x_1+h$ arasında kalır: Onun sağında $f$, $x_1$ yönünde $3$ eğimiyle artar, solunda hiç artmaz; merkezi fark ikisini karıştırır.

(c) $(2,\,2,\,3)$ noktasında maksimumun iki girdisi eşittir. Ters mod $\bar v=3$ değerini, hesabın eşitlik durumunda hangisini büyük saydığına bağlı olarak bu ikisinden birine iletir; dolayısıyla $(3,\,0,\,2)^{\top}$ ya da $(0,\,3,\,2)^{\top}$ verir. Orada gradyan yoktur: $x_1$ büyütülürse $f$, $3$ eğimiyle artar; $x_1$ küçültülürse $f$ değişmez. Tek taraflı eğimler, $|x|$ fonksiyonunun $0$ noktasındaki gibi farklıdır.
:::
:::
