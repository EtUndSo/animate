---
title: Hesse matrisi ve ikinci dereceden yaklaşım
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230900
summary: Gradyan arazinin eğikliğini betimler, ama kavisini betimlemez.
tags: ikinci kısmi türevleri, Hesse matrisi, karma fark, ikinci yönlü türevi
lang: tr
---

<span class="anker" id="stufe-8"></span>

:::zweck
Gradyan arazinin eğikliğini betimler, ama kavisini betimlemez. İkinci kısmi türevleri Hesse matrisi toplar. Hesse matrisi simetriktir ve onunla doğrusal yaklaşım ikinci dereceden yaklaşıma dönüşür. Özdeğerleri, arazinin farklı doğrultularda ne kadar güçlü eğrildiğini söyler ve bu kesimi [Bölüm 2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html)'deki kuadratik formlara bağlar.
:::

### İkinci kısmi türevler

<span class="anker" id="stufe-8-1"></span>

$\partial_jf$ kısmi türevleri de yine $\mathbf{x}$'in fonksiyonlarıdır. Bunların aynı ya da başka bir değişkene göre bir kez daha kısmi türevi alınabilir. Bu, $x_i$ doğrultusunda ilerlendiğinde $x_j$ doğrultusundaki eğimin nasıl değiştiğini betimler.

:::definition Tanım 8.1 (İkinci kısmi türevler)
<span class="anker" id="satz-8-1"></span>

$f:\mathbb{R}^d\to\mathbb{R}$ fonksiyonunun __ikinci kısmi türevleri__ şunlardır:

<span class="anker" id="gl-8-1"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial}{\partial x_i}\Bigl(\frac{\partial f}{\partial x_j}\Bigr), \tag{8.1}$$

yani önce $x_j$, sonra $x_i$ değişkenine göre alınan türevler. $i=j$ için $\partial^2f/\partial x_i^2$ yazılır. $i\ne j$ için bunlara karma kısmi türevler denir.
:::

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için $\partial_1f=2x_1x_2$ ve $\partial_2f=x_1^2+2x_2$, dolayısıyla şu bulunur:

$$\begin{gathered} \frac{\partial^2f}{\partial x_1^2}=\frac{\partial}{\partial x_1}(2x_1x_2)=2x_2,\qquad \frac{\partial^2f}{\partial x_2\,\partial x_1}=\frac{\partial}{\partial x_2}(2x_1x_2)=2x_1,\\ \frac{\partial^2f}{\partial x_1\,\partial x_2}=\frac{\partial}{\partial x_1}(x_1^2+2x_2)=2x_1,\qquad \frac{\partial^2f}{\partial x_2^2}=\frac{\partial}{\partial x_2}(x_1^2+2x_2)=2 . \end{gathered}$$

$(1,\,2)$ noktasında bunlar $4$, $2$, $2$ ve $2$ olur. İki karma türev, farklı yollardan ortaya çıkmış olmalarına rağmen eşittir.
::::

⁠**Kısacası:** İkinci kısmi türevler, bir kısmi türevin bir kez daha kısmi türevini alır; karma olanlar, bir doğrultudaki eğimin başka bir doğrultuda yürürken nasıl değiştiğini betimler.

### Hesse matrisi

<span class="anker" id="stufe-8-2"></span>

$d$ değişkenli bir fonksiyonun $d^2$ tane ikinci kısmi türevi vardır. Birinci türevler gradyanda toplandığı gibi bunlar da tek bir nesnede, burada kare bir matriste toplanır.

:::definition Tanım 8.2 (Hesse matrisi)
<span class="anker" id="satz-8-2"></span>

$d\times d$ tipindeki

<span class="anker" id="gl-8-2"></span>
$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\cdots&\dfrac{\partial^2f}{\partial x_1\,\partial x_d}\\ \vdots&&\vdots\\ \dfrac{\partial^2f}{\partial x_d\,\partial x_1}&\cdots&\dfrac{\partial^2f}{\partial x_d^2}\end{pmatrix},\qquad \bigl(\mathbf{H}_f(\mathbf{x})\bigr)_{ij}=\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}), \tag{8.2}$$

matrisine $f$ fonksiyonunun $\mathbf{x}$ noktasındaki __Hesse matrisi__ denir.
:::

Matris adını matematikçi Otto Hesse'den alır; bazı kitaplar $\nabla^2f$ yazar. Matrisin $j$ sütunu, $\partial_jf$ fonksiyonunun gradyanıdır. Böylece matris, gradyanın, yani $\mathbf{x}\mapsto\nabla f(\mathbf{x})$ vektör değerli fonksiyonunun Jacobi matrisiyle yakından ilişkilidir: Bu Jacobi matrisinin $(i,j)$ elemanı $\partial(\partial_if)/\partial x_j$, yani diğer sırayla alınan türevdir. Sonraki alt kesim, iki sıranın neredeyse her zaman aynı sonucu verdiğini gösteriyor; o zaman Hesse matrisi gradyanın Jacobi matrisidir.

::::beispiel [Sayısal örnek]
$f(\mathbf{x})=x_1^2x_2+x_2^2$ için önceki alt kesime göre şu bulunur:

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}2x_2&2x_1\\2x_1&2\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}4&2\\2&2\end{pmatrix}.$$

Simetrik $\mathbf{A}$ ile ikinci dereceden bir $f(\mathbf{x})=\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ fonksiyonu için Kesim [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7)'ye göre $\nabla f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ ve dolayısıyla her noktada $\mathbf{H}_f=\mathbf{A}$ olur. Kesim [4](richtungsableitung-und-steilster-anstieg.html#stufe-4)'teki $x_1^2+4x_2^2$ çanağı için $\mathbf{A}=\operatorname{diag}(2;\,8)$ olur.
::::

⁠**Kısacası:** Hesse matrisi bütün ikinci kısmi türevleri toplar; ikinci dereceden bir $\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ fonksiyonunda her yerde $\mathbf{A}$ olur.

### Schwarz teoremi

<span class="anker" id="stufe-8-3"></span>

Sayısal örnekte iki karma türev eşitti. Bu bir rastlantı değildir; ikinci türevleri sıçrama yapmayan bütün fonksiyonlar için geçerlidir.

:::satz Teorem 8.3 (Schwarz teoremi)
<span class="anker" id="satz-8-3"></span>

$f$ fonksiyonunun bütün ikinci kısmi türevleri $\mathbf{x}$ noktasının yakınında varsa ve $\mathbf{x}$ noktasında sürekliyse orada

<span class="anker" id="gl-8-3"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial^2f}{\partial x_j\,\partial x_i} \tag{8.3}$$

eşitliği bütün $i,j$ için geçerlidir. Hesse matrisi o zaman simetriktir.
:::

Nedeni, sıranın hiç görünmediği bir hesapta görülür. $\mathbf{x}$ noktasından $x_1$ doğrultusunda $h$ kadar ve $x_2$ doğrultusunda $k$ kadar gidilir ve __karma fark__ oluşturulur:

$$\Delta(h,k)=f(x_1+h,\,x_2+k)-f(x_1+h,\,x_2)-f(x_1,\,x_2+k)+f(x_1,\,x_2).$$

Birinci terim üçüncüyle, ikinci terim dördüncüyle birleştirilirse $\Delta$, $x_2$ doğrultusundaki $k$ adımında $f(x_1+h,\cdot)-f(x_1,\cdot)$ farkının değişimidir: $x_2$ doğrultusunda gidilirken $x_1$ doğrultusundaki artış nasıl değişir? $hk$ çarpımına bölünürse bu, küçük $h$ ve $k$ için önce $x_1$'e, sonra $x_2$'ye göre alınan türeve yaklaşır. Bunun yerine ilk iki ve son iki terim birleştirilirse aynı sayı, $x_1$ doğrultusundaki adımda $x_2$ doğrultusundaki artışın değişimi olarak okunur ve bölüm diğer sırayla alınan türeve yaklaşır. İki limit de aynı $\Delta/(hk)$ sayısına aittir. Süreklilik, iki limite geçişin sırasının önemli olmamasını sağlar.

::::beispiel [Sayısal örnek]
$(1,\,2)$ noktasında $h=k=0{,}1$ ile $f(\mathbf{x})=x_1^2x_2+x_2^2$ için şu bulunur:

$$\Delta=f(1{,}1;\ 2{,}1)-f(1{,}1;\ 2)-f(1;\ 2{,}1)+f(1,2)=6{,}951-6{,}42-6{,}51+6=0{,}021,$$

dolayısıyla $\Delta/(hk)=2{,}1$ olur; bu, $2x_1=2$ karma türevine yakındır. Sapma, $2x_1$ ifadesinin $x_1=1$ ile $x_1=1{,}1$ arasında sabit olmamasından kaynaklanır.
::::

⁠**Kısacası:** İkinci türevler sürekliyse türev alma sırası önemsizdir ve Hesse matrisi simetriktir.

:::hintergrund İkinci türevler sürekli olmadığında
Süreklilik olmadan teorem yanlış olabilir. Klasik karşı örnek, $f(0,0)=0$ olmak üzere $f(x_1,x_2)=x_1x_2\,\frac{x_1^2-x_2^2}{x_1^2+x_2^2}$ fonksiyonudur. Birinci kısmi türevler eksenler üzerinde hesaplanırsa $\partial_1f(0,x_2)=-x_2$ ve $\partial_2f(x_1,0)=x_1$ bulunur. Birincisinin $x_2$'ye göre türevi alınırsa orijinde $-1$, ikincisinin $x_1$'e göre türevi alınırsa $+1$ elde edilir. Demek ki orijindeki karma türevler farklıdır, çünkü ikinci türevler orada sıçrama yapar. Bu bölümün köşe noktası olmayan fonksiyonlarında bu durum ortaya çıkmaz; bu fonksiyonlar polinomlardan, üstel fonksiyonlardan ve temel aritmetik işlemlerden kurulmuştur ve tanımlı oldukları her yerde her mertebeden sürekli türevlere sahiptir.
:::

### İkinci dereceden yaklaşım

<span class="anker" id="stufe-8-4"></span>

Tek değişkende teğet, Kesim [1.5](die-ableitung.html#stufe-1-5)'te bir parabolle iyileştirilmişti. Çok değişkende teğet düzlemin yerini, kavisini Hesse matrisinin betimlediği kavisli bir yüzey alır.

:::satz Teorem 8.4 (İkinci dereceden yaklaşım)
<span class="anker" id="satz-8-4"></span>

$f$ fonksiyonunun $\mathbf{x}$ yakınında sürekli ikinci kısmi türevleri varsa şu geçerlidir:

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x}+\mathbf{h})=f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{h}+r_2(\mathbf{h})\qquad\text{burada}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{r_2(\mathbf{h})}{\lVert\mathbf{h}\rVert^2}=0 . \tag{8.4}$$
:::

:::herleitung Bir doğru boyunca ikinci dereceden yaklaşım
$f$, $\mathbf{x}$ noktasından geçen ve $\mathbf{h}$ doğrultusunda uzanan doğruyla sınırlandırılır: $\phi(t)=f(\mathbf{x}+t\,\mathbf{h})$. Bu tek değişkenli bir fonksiyondur. [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4) uyarınca $\phi'(t)=\nabla f(\mathbf{x}+t\mathbf{h})^{\top}\mathbf{h}=\sum_jh_j\,\partial_jf(\mathbf{x}+t\mathbf{h})$ olur. Her terimin bir kez daha [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4) ile türevi alınır, bu kez $\partial_jf$ fonksiyonu için:

$$\phi''(t)=\sum_{j=1}^dh_j\sum_{i=1}^d\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}+t\mathbf{h})\,h_i=\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x}+t\mathbf{h})\,\mathbf{h} .$$

$\phi$ fonksiyonunun $0$ noktasındaki ve $t=1$ için hesaplanan [(1.6)](die-ableitung.html#gl-1-6) ikinci dereceden yaklaşımı $\phi(1)\approx\phi(0)+\phi'(0)+\tfrac12\phi''(0)$ olur ve bu, [(8.4)](#gl-8-4) bağıntısıdır. Hatanın $\lVert\mathbf{h}\rVert^2$'den hızlı sıfıra gitmesi, ikinci türevlerin sürekliliğinden çıkar.
:::

Yeni $\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$ terimi, [Bölüm 2, Kesim 5.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1) anlamında, matrisi Hesse matrisi olan bir kuadratik formdur. Demek ki fonksiyon $\mathbf{x}$ yakınında bir düzlem artı bir kuadratik form gibi görünür.

::::beispiel [Sayısal örnek]
$(1,\,2)$ noktasında ve Kesim [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4)'teki gibi $\mathbf{h}=(0{,}01;\ 0{,}02)^{\top}$ ile $f(\mathbf{x})=x_1^2x_2+x_2^2$ için şu bulunur:

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(4\cdot0{,}01^2+2\cdot2\cdot0{,}01\cdot0{,}02+2\cdot0{,}02^2\bigr)=\tfrac12\,(0{,}0004+0{,}0008+0{,}0008)=0{,}001$$

(Şekil [15](#abb-15)). İkinci dereceden yaklaşım $6+0{,}14+0{,}001=6{,}141$, tam değer $6{,}141002$ olur. Hata $0{,}001002$'den $0{,}000002$'ye düştü. Geriye kalan üçüncü mertebe terimdir: $x_1^2x_2$ içinde, hiçbir ikinci dereceden yaklaşımın yakalayamadığı $h_1^2h_2=0{,}0001\cdot0{,}02=0{,}000002$ terimi saklıdır.

:::abbildung ml/k3rtaylor2 15
Çift toplam olarak ikinci dereceden yaklaşımın eğrilik terimi; $h_1\cdot2\cdot h_2$ ve $h_2\cdot2\cdot h_1$ karma terimleri ortadaki terimde birleştirilmiştir.
:::
::::

⁠**Kısacası:** $\mathbf{x}$ yakınında $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{h}$ olur: düzlem artı kuadratik form.

### Bir doğrultudaki eğrilik

<span class="anker" id="stufe-8-5"></span>

$\mathbf{x}$ noktasından $\mathbf{u}$ doğrultusunda gidildiğinde arazi ne kadar kavislidir? Önceki alt kesimdeki türetme cevabı zaten verdi: $\phi(t)=f(\mathbf{x}+t\mathbf{u})$ fonksiyonunun $0$ noktasındaki ikinci türevi $\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{u}$ olur.

:::definition Tanım 8.5 (Bir doğrultudaki eğrilik)
<span class="anker" id="satz-8-5"></span>

Uzunluğu $1$ olan bir $\mathbf{u}$ vektörü için

<span class="anker" id="gl-8-5"></span>
$$\frac{\mathrm{d}^2}{\mathrm{d} t^2}f(\mathbf{x}+t\,\mathbf{u})\Big|_{t=0}=\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u} \tag{8.5}$$

ifadesine $f$ fonksiyonunun $\mathbf{x}$ noktasında $\mathbf{u}$ doğrultusundaki __ikinci yönlü türevi__ denir. Bu, o doğrultudaki kesit eğrisinin eğriliğini ölçer.
:::

[Bölüm 2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html)'nin sonuçlarıyla bu eğriliğin en fazla ve en az ne kadar olduğu hemen söylenebilir. Hesse matrisi simetriktir ve [Bölüm 2, Kesim 7.6](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-6)'daki spektral teoreme göre gerçel özdeğerlere ve birbirine dik özvektörlere sahiptir.

:::satz Teorem 8.6 (Eğrilik ve özdeğerler)
<span class="anker" id="satz-8-6"></span>

$\lambda_{\min}$ ve $\lambda_{\max}$, simetrik $\mathbf{H}_f(\mathbf{x})$ Hesse matrisinin en küçük ve en büyük özdeğeri olsun. O zaman $\lVert\mathbf{u}\rVert=1$ olan her $\mathbf{u}$ doğrultusu için şu geçerlidir:

<span class="anker" id="gl-8-6"></span>
$$\lambda_{\min}\le\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u}\le\lambda_{\max}. \tag{8.6}$$

Bir özvektörün doğrultusunda eğrilik tam olarak ona ait özdeğerdir. $\mathbf{H}_f(\mathbf{x})$ pozitif tanımlıysa eğrilik her doğrultuda pozitiftir; belirsizse arazi bazı doğrultularda yukarı, başka doğrultularda aşağı doğru eğrilir.
:::

Eşitsizlik, [Bölüm 2, Kesim 8.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-5)'teki, bir kuadratik formun birim çember üzerindeki en büyük ve en küçük değeri hakkındaki önermedir. $\lambda$ özdeğerine ait bir $\mathbf{u}$ özvektörü için $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\lambda\,\mathbf{u}^{\top}\mathbf{u}=\lambda$ olur. Pozitif tanımlı ve belirsiz kavramları [Bölüm 2, Kesim 8](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8)'den gelir; orada bir kuadratik formun biçimi, çanak, oluk ya da eyer olarak, özdeğerlerinden okunuyordu. [(8.4)](#gl-8-4) ikinci dereceden yaklaşımı aracılığıyla bu, $\mathbf{x}$ yakınındaki araziye aktarılır: Pozitif tanımlı bir Hesse matrisinde eğrilik teriminin eş yükselti eğrileri elipslerdir; [Bölüm 2, Kesim 7.7](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-7)'ye göre bu elipslerin asal eksenleri özvektörlerin doğrultusunda uzanır ve güçlü eğrilik doğrultusunda kısadır.

::::beispiel [Sayısal örnek 1]
$f(\mathbf{x})=x_1^2+4x_2^2$ çanağı için $\mathbf{H}_f=\operatorname{diag}(2;\,8)$ olur, özdeğerleri $2$ ve $8$'dir. $x_1$ doğrultusunda eğrilik $2$, $x_2$ doğrultusunda $8$, $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$ doğrultusunda ise $\tfrac12(2+8)=5$ olur. Bu, Kesim [4.4](richtungsableitung-und-steilster-anstieg.html#stufe-4-4)'teki uzamış eş yükselti eğrilerini açıklar: Çanak $x_2$ doğrultusunda dört kat daha güçlü eğrilir, çeperleri orada daha diktir ve elipsler bu doğrultuda dardır.
::::

::::beispiel [Sayısal örnek 2]
$(1,\,2)$ noktasında $f(\mathbf{x})=x_1^2x_2+x_2^2$ için $\mathbf{H}_f=\bigl(\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\bigr)$ olur. İz $6$ ve determinant $4$, [Bölüm 2, Kesim 6.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5)'e göre $3\pm\sqrt5$, yani yaklaşık $5{,}236$ ve $0{,}764$ özdeğerlerini verir. İkisi de pozitiftir, Hesse matrisi pozitif tanımlıdır: $(1,\,2)$ noktasının yakınında arazi her doğrultuda yukarı doğru eğrilir. $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$ doğrultusunda eğrilik

$$\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\tfrac12\,(4+2+2+2)=5,$$

olur ve $0{,}764$ ile $5{,}236$ arasındadır (Şekil [16](#abb-16)).

:::abbildung ml/k3rkruemmung 16
$f(\mathbf{x})=x_1^2x_2+x_2^2$ fonksiyonunun $(1,\,2)$ noktasında açıortay doğrultusundaki eğriliği; $\tfrac12$ çarpanı $u_iu_j=\tfrac12$ eşitliğinden gelir.
:::
::::

⁠**Kısacası:** $\mathbf{u}$ doğrultusundaki eğrilik $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$ olur; Hesse matrisinin en küçük ve en büyük özdeğeri arasında kalır ve özdeğerlerin işaretleri, arazinin bir çanak gibi mi yoksa bir eyer gibi mi eğrildiğine karar verir.

:::hintergrund Hesse matrisini kurmadan Hesse matrisi-vektör çarpımı
Çok sayıda değişkende Hesse matrisi devasadır: Bir milyon değişkende $10^{12}$ elemanı vardır. Ama çoğu zaman yalnızca onun bir $\mathbf{v}$ vektörüyle çarpımı gerekir. Bu çarpım, matris kurulmadan elde edilir. $\nabla f(\mathbf{x})^{\top}\mathbf{v}=\sum_jv_j\,\partial_jf(\mathbf{x})$ sayısı $\mathbf{x}$'in bir fonksiyonudur ve gradyanının bileşenleri $\sum_jv_j\,\partial^2f/\partial x_i\partial x_j$ olur, yani $\nabla_{\mathbf{x}}\bigl(\nabla f(\mathbf{x})^{\top}\mathbf{v}\bigr)=\mathbf{H}_f(\mathbf{x})\,\mathbf{v}$ olur. $f(\mathbf{x})=x_1^2x_2+x_2^2$ ve $\mathbf{v}=(1,\,1)^{\top}$ için $\nabla f^{\top}\mathbf{v}=2x_1x_2+x_1^2+2x_2$ olur; bunun gradyanı $(2x_2+2x_1,\ 2x_1+2)^{\top}$, $(1,\,2)$ noktasında yani $(6,\,4)^{\top}$ olur ve bu, $\mathbf{H}_f\mathbf{v}=(4+2,\ 2+2)^{\top}$ çarpımıdır. Demek ki $d^2$ elemanlı bir matris yerine iki gradyan hesaplanır.
:::

:::aufgabe Alıştırma 28 ★ Hesse matrisleri
<span class="anker" id="aufg-28"></span>

Verilen noktadaki Hesse matrisini hesaplayın ve simetriyi kontrol edin.

<ol class="al">

<li>

$(1,\,2)$ noktasında $f(\mathbf{x})=x_1^3+x_1x_2^2$;

</li>

<li>

$(0,\,0)$ noktasında $f(\mathbf{x})=\mathrm{e}^{x_1+2x_2}$. Matrisin rankı nedir?

</li>

<li>

$(1,\,2,\,3)$ noktasında $f(\mathbf{x})=x_1x_2x_3$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3x_1^2+x_2^2$ ve $\partial_2f=2x_1x_2$, dolayısıyla

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}6x_1&2x_2\\2x_2&2x_1\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}6&4\\4&2\end{pmatrix};$$

$\partial_2(3x_1^2+x_2^2)=2x_2$ ve $\partial_1(2x_1x_2)=2x_2$ karma türevleri eşittir.

(b) $f=\mathrm{e}^{x_1+2x_2}$ ile $\partial_1f=f$ ve $\partial_2f=2f$, dolayısıyla $\mathbf{H}_f=f\cdot\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ ve orijinde $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ olur. İkinci satır birincinin iki katıdır; rank $1$, özdeğerler $5$ ve $0$ olur. Bu uyumludur: $f$ yalnızca $x_1+2x_2$ ifadesine bağlıdır ve $(2,\,-1)^{\top}$ doğrultusu boyunca sabittir, dolayısıyla o doğrultuda eğriliği yoktur.

(c) $\partial_1f=x_2x_3$, $\partial_2f=x_1x_3$, $\partial_3f=x_1x_2$, dolayısıyla

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}0&x_3&x_2\\x_3&0&x_1\\x_2&x_1&0\end{pmatrix},\qquad \mathbf{H}_f(1,2,3)=\begin{pmatrix}0&3&2\\3&0&1\\2&1&0\end{pmatrix}.$$
:::
:::

:::aufgabe Alıştırma 29 ★★ İkinci dereceden yaklaşım
<span class="anker" id="aufg-29"></span>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$, Alıştırma [10](partielle-ableitungen-und-der-gradient.html#aufg-10)'daki gibi olsun.

<ol class="al">

<li>

$\mathbf{H}_f(2,0)$ matrisini hesaplayın.

</li>

<li>

$(2,\,0)$ noktasındaki ikinci dereceden yaklaşımla $f(2{,}1;\ -0{,}05)$ için bir yaklaşık değer hesaplayın ve bunu Alıştırma [10](partielle-ableitungen-und-der-gradient.html#aufg-10)'daki doğrusal yaklaşımla ve tam değerle karşılaştırın.

</li>

</ol>

:::loesung
(a) $\partial_1^2f=0$, $\partial_1\partial_2f=\mathrm{e}^{x_2}$, $\partial_2^2f=x_1\mathrm{e}^{x_2}$, dolayısıyla $\mathbf{H}_f(2,0)=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$.

(b) $\mathbf{h}=(0{,}1;\ -0{,}05)^{\top}$ ile

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(0+2\cdot1\cdot0{,}1\cdot(-0{,}05)+2\cdot0{,}05^2\bigr)=\tfrac12\,(-0{,}01+0{,}005)=-0{,}0025 .$$

İkinci dereceden yaklaşım $2+0-0{,}0025=1{,}9975$ olur; doğrusal yaklaşım $2{,}0$ idi, tam değer $1{,}997582$ olur. Hata $0{,}0024$ değerinden $0{,}00008$ değerine düşer. $-0{,}005$ karma terimi, Alıştırma [10](partielle-ableitungen-und-der-gradient.html#aufg-10)'daki etkileşimdir.
:::
:::

:::aufgabe Alıştırma 30 ★★ Eğik bir çanağın eğrilikleri
<span class="anker" id="aufg-30"></span>

$f(\mathbf{x})=x_1^2+4x_2^2+x_1x_2$ olsun.

<ol class="al">

<li>

$f$'yi $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ biçiminde yazın ve $\mathbf{H}$ matrisini verin.

</li>

<li>

$\mathbf{H}$ matrisinin özdeğerlerini ve $\mathbf{e}_1$, $\mathbf{e}_2$ ve $(1,\,-1)^{\top}/\sqrt2$ doğrultularındaki eğrilikleri hesaplayın. [(8.6)](#gl-8-6) bağıntısını kontrol edin.

</li>

<li>

Eğrilik hangi doğrultuda en büyüktür? Bir özvektör verin.

</li>

</ol>

:::loesung
(a) $\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&8\end{smallmatrix}\bigr)$ ile $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ ifadesi $\tfrac12\,(2x_1^2+2x_1x_2+8x_2^2)=x_1^2+x_1x_2+4x_2^2$ verir. Bu matris aynı zamanda $f$ fonksiyonunun Hesse matrisidir.

(b) İz $10$, determinant $16-1=15$, dolayısıyla $\lambda^2-10\lambda+15=0$ ve $\lambda=5\pm\sqrt{10}$, yaklaşık $8{,}162$ ve $1{,}838$. Eğrilikler $\mathbf{e}_1^{\top}\mathbf{H}\mathbf{e}_1=2$, $\mathbf{e}_2^{\top}\mathbf{H}\mathbf{e}_2=8$ ve $\mathbf{u}=(1,\,-1)^{\top}/\sqrt2$ için $\tfrac12\,(2-1-1+8)=4$ olur. Üçü de $1{,}838$ ile $8{,}162$ arasındadır.

(c) Eğrilik, $\lambda=5+\sqrt{10}$ özdeğerine ait bir özvektörün doğrultusunda en büyüktür. $(\mathbf{H}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ denkleminin ilk satırından $(2-\lambda)v_1+v_2=0$, dolayısıyla $\mathbf{v}=(1;\ 3+\sqrt{10})^{\top}\approx(1;\ 6{,}162)^{\top}$ çıkar; normlanmış hâli yaklaşık $(0{,}160;\ 0{,}987)^{\top}$ olur. Bu, $x_1x_2$ karma terimi nedeniyle biraz döndürülmüş, neredeyse $x_2$ doğrultusudur.
:::
:::

:::aufgabe Alıştırma 31 ★★★ Farklı karma türevler
<span class="anker" id="aufg-31"></span>

$\mathbf{x}\ne\mathbf{0}$ için $f(x_1,x_2)=x_1x_2\,\dfrac{x_1^2-x_2^2}{x_1^2+x_2^2}$ ve $f(0,0)=0$ olsun.

<ol class="al">

<li>

Fark bölümüyle $x_2\ne0$ için $\partial_1f(0,x_2)=-x_2$ ve $\partial_1f(0,0)=0$ olduğunu gösterin. $\partial_2f(x_1,0)$ türevini de aynı biçimde hesaplayın.

</li>

<li>

İki karma türevin orijinde $-1$ ve $+1$ olduğu sonucunu çıkarın. Schwarz teoreminin hangi varsayımı sağlanmıyor?

</li>

</ol>

:::loesung
(a) $x_1=0$ ekseni üzerinde $f=0$ olur. $x_2\ne0$ için

$$\partial_1f(0,x_2)=\lim_{h\to0}\frac{f(h,x_2)-0}{h}=\lim_{h\to0}x_2\,\frac{h^2-x_2^2}{h^2+x_2^2}=x_2\cdot\frac{-x_2^2}{x_2^2}=-x_2 .$$

Orijinde $f(h,0)=0$, dolayısıyla $\partial_1f(0,0)=0$ olur; demek ki $-x_2$ formülü $x_2=0$ için de geçerlidir. Aynı biçimde $\partial_2f(x_1,0)=\lim_k x_1\frac{x_1^2-k^2}{x_1^2+k^2}=x_1$ olur.

(b) Önce $x_1$'e, sonra $x_2$'ye göre türev alınınca: $\frac{\partial}{\partial x_2}(-x_2)=-1$. Önce $x_2$'ye, sonra $x_1$'e göre: $\frac{\partial}{\partial x_1}(x_1)=+1$. Orijindeki karma türevler farklıdır. Sağlanmayan varsayım, ikinci türevlerin orijindeki sürekliliğidir: Orijin dışında karma türev $x_2$ ekseni üzerinde her yerde $-1$, $x_1$ ekseni üzerinde her yerde $+1$ olur. Demek ki karma türev orijinde sıçrar ve türev almanın iki sırası orijine farklı taraflardan yaklaşır.
:::
:::
