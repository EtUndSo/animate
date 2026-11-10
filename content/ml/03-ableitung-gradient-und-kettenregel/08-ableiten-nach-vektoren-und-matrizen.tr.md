---
title: Vektörlere ve matrislere göre türev
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Türev, Gradyan ve Zincir Kuralı
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Bölüm 3: Türev, Gradyan ve Zincir Kuralı
nachschlagen: ja
order: 15230800
summary: a top x , x top Ax ya da lVerty-AxrVert 2 gibi ifadelerin gradyanlarına sürekli ihtiyaç duyulur.
tags: düzen kuralı
lang: tr
---

<span class="anker" id="stufe-7"></span>

:::zweck
$\mathbf{a}^{\top}\mathbf{x}$, $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ ya da $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ gibi ifadelerin gradyanlarına sürekli ihtiyaç duyulur. Bu kesim önce her türevin hangi şekle sahip olduğunu belirliyor, sonra en önemli formülleri bileşen bileşen türetiyor. Sonda bir matrise göre türevler ve bir duyarlılığı bir matris çarpımı boyunca geriye doğru hesaplamayı sağlayan kural yer alıyor.
:::

### Düzen kuralı

<span class="anker" id="stufe-7-1"></span>

Tek değişkenli fonksiyonlarda türev bir sayıdır ve düzenlenecek bir şey yoktur. Vektörlerde ve matrislerde ise çok sayıdaki kısmi türevin hangi biçimde yazılacağı belirlenmelidir: sütun olarak mı satır olarak mı, $m\times n$ tipinde mi $n\times m$ tipinde bir matris olarak mı. Böyle bir belirlemeye __düzen kuralı__ denir. Matematiksel olarak her seçim eşit derecede iyidir; yalnızca seçime sonuna kadar bağlı kalmak gerekir, yoksa formüller birden devrik görünür.

:::definition Tanım 7.1 (Bu bölümün düzen kuralı)
<span class="anker" id="satz-7-1"></span>

<ol class="rm">

<li>

Vektörler sütundur. Bir $f:\mathbb{R}^n\to\mathbb{R}$ fonksiyonunun gradyanı, $\mathbf{x}$ ile aynı şekle sahip bir sütundur.

</li>

<li>

Bir $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ fonksiyonunun Jacobi matrisi $m\times n$ tipinde bir matristir: her çıktı için bir satır, her girdi için bir sütun.

</li>

<li>

Bir $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ fonksiyonunun bir $\mathbf{A}$ matrisine göre türevi, $(i,j)$ yerinde $\partial f/\partial a_{ij}$ elemanını taşıyan $m\times n$ tipinde bir $\nabla_{\mathbf{A}}f$ matrisidir, yani $\mathbf{A}$ ile aynı şekle sahiptir.

</li>

</ol>
:::

Tablo [2](#tab-2) bunu özetliyor. Bölüm bunun iki sonucunu zaten kullandı: Tek çıktılı bir fonksiyon için Jacobi matrisi satır olarak yazılmış gradyandır, $\mathbf{J}_f=\nabla f^{\top}$. Gradyanlar için zincir kuralı da devriğe ihtiyaç duyar, $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$. (iii) kuralına Kesim [7.5](#stufe-7-5)'te ihtiyaç duyulur: Bir matrisi küçük bir $\mathbf E$ matrisi kadar değiştiren kişi, $\nabla_{\mathbf{A}}f$ ile $\mathbf E$ matrisini eleman eleman karşılaştırabilmek ister.

<span class="anker" id="tab-2"></span>

**Tablo 2:** Bu bölümün uzlaşımına göre, fonksiyonun türüne bağlı olarak türevin şekli.

| Fonksiyon | Türev | Şekil |
|---|---|---|
| $f:\mathbb{R}\to\mathbb{R}$ | $f'(x)$ | sayı |
| $f:\mathbb{R}^n\to\mathbb{R}$ | $\nabla f(\mathbf{x})$ | sütun, $n\times1$ ($\mathbf{x}$ gibi) |
| $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ | $m\times n$ ($i$ satırı $\nabla g_i^{\top}$) |
| $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ | $\nabla_{\mathbf{A}}f(\mathbf{A})$ | $m\times n$ ($\mathbf{A}$ gibi) |

::::beispiel [Sayısal örnek]
$(1,\,2)$ noktasında $f(\mathbf{x})=x_1^2x_2+x_2^2$ için gradyan $\nabla f=(4,\,5)^{\top}$ sütunu, Jacobi matrisi ise $\mathbf{J}_f=(4\ \ 5)$ satırıdır. [(5.1)](die-jacobi-matrix.html#gl-5-1) bağıntısındaki $\mathbf{g}$ için $\mathbf{J}_{\mathbf{g}}$, $2\times2$ tipinde bir matristir; birinci satırı olan $(2\ \ 1)$, $g_1=x_1x_2$ fonksiyonunun satır olarak yazılmış gradyanıdır.
::::

⁠**Kısacası:** Bölümde bir gradyan, değişkeninin şekline sahiptir ve bir Jacobi matrisinin her çıktı için bir satırı vardır; $\mathbf{J}_f=\nabla f^{\top}$ ve gradyanlar için zincir kuralındaki devrik buradan çıkar.

:::hintergrund Literatürdeki başka uzlaşımlar
Birçok kitap gradyanı satır olarak yazar. O zaman gradyan, tek çıktılı bir fonksiyonun Jacobi matrisiyle aynı şeydir ve zincir kuralı hiç devrik almadan işler, çünkü $\nabla(f\circ\mathbf{g})=\nabla f\,\mathbf{J}_{\mathbf{g}}$ bu durumda bir satır ile bir matrisin çarpımıdır. Bunun bedeli, gradyanın artık $\mathbf{x}$ ile aynı şekle sahip olmamasıdır; en dik çıkış doğrultusundaki $\mathbf{x}+t\,\nabla f$ doğrusu o zaman bir devrik gerektirir. İki düzen birbirinden ayrılır: Pay düzeninde satırlar, bu bölümün Jacobi matrisinde olduğu gibi, fonksiyonun bileşenlerine göre belirlenir. Payda düzeninde satırlar değişkenin bileşenlerine göre belirlenir; o zaman vektör değerli bir fonksiyonun türevi, Jacobi matrisinin devriğidir. Bu bölüm yaygın bir karma biçim kullanır: sütun olarak gradyan ve pay düzeninde Jacobi matrisi. Bu yüzden farklı kaynaklardan alınan formüller denetlenmeden birleştirilmemelidir. Hızlı bir kontrol şekle bakmaktır: $\mathbf{x}\in\mathbb{R}^n$ vektörüne göre bir gradyanın bir sütunda $n$ elemanı olmalıdır. Daha güvenilir bir kontrol küçük bir sayısal örnektir.
:::

### Doğrusal fonksiyonlar

<span class="anker" id="stufe-7-2"></span>

Çok değişkenli en basit fonksiyon ağırlıklı toplamdır. Gradyanı o kadar basittir ki hemen yazılabilir; türetme ise bu kesimdeki diğer bütün formüllerin ortaya çıktığı kalıbı gösterir.

:::satz Teorem 7.2 (Doğrusal fonksiyonların gradyanları)
<span class="anker" id="satz-7-2"></span>

Sabit $\mathbf{a},\mathbf{y}$ vektörleri ve uygun şekle sahip sabit bir $\mathbf{A}$ matrisi için şu geçerlidir:

<span class="anker" id="gl-7-1"></span>
$$\nabla_{\mathbf{x}}(\mathbf{a}^{\top}\mathbf{x})=\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{a})=\mathbf{a},\qquad \nabla_{\mathbf{x}}(\mathbf{y}^{\top}\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\mathbf{y} . \tag{7.1}$$
:::

:::beweis Doğrusal fonksiyonların gradyanları
$\mathbf{a}^{\top}\mathbf{x}=\sum_ja_jx_j$ olur. $x_k$ değişkenine göre türev alınınca yalnızca $j=k$ olan terim, yani $a_k$ kalır. $\mathbf{x}^{\top}\mathbf{a}=\mathbf{a}^{\top}\mathbf{x}$ olduğundan aynısı $\mathbf{x}^{\top}\mathbf{a}$ için de geçerlidir. İkinci kısım için $\mathbf{a}=\mathbf{A}^{\top}\mathbf{y}$ konur, çünkü $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}^{\top}\mathbf{y})^{\top}\mathbf{x}$ olur.
:::

::::beispiel [Sayısal örnek]
[Bölüm 1, Kesim 2.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2)'de $\mathbf{x}_1=(60,\,2,\,3)^{\top}$ olan Daire 1 ve $\mathbf{w}=(3,\,10,\,-4)^{\top}$ ağırlıkları için tahmin $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$ idi. Ağırlıkların fonksiyonu olarak bu tahminin gradyanı $\nabla_{\mathbf{w}}\hat y_1=\mathbf{x}_1=(60,\,2,\,3)^{\top}$ olur. $w_1$, $0{,}1$ artırılırsa tahmin $60\cdot0{,}1=6$ artarak $194$ olur; gerçekten de $3{,}1\cdot60+10\cdot2-4\cdot3=194$ bulunur. Nedeni basittir: Her ağırlık kendi özniteliğiyle çarpılır ve bu yüzden bir ağırlığa göre duyarlılık tam olarak ona ait özniteliktir.
::::

⁠**Kısacası:** $\mathbf{a}^{\top}\mathbf{x}$ ifadesinin $\mathbf{x}$'e göre gradyanı $\mathbf{a}$, $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}$ ifadesininki ise $\mathbf{A}^{\top}\mathbf{y}$ olur.

### Kuadratik formlar

<span class="anker" id="stufe-7-3"></span>

[Bölüm 2, Kesim 5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5)'teki $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ kuadratik formları, karelerin toplandığı her yerde karşımıza çıkar. Türev alınırken $\mathbf{x}$ iki yerde görünür ve Kesim [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2)'deki iki yol gibi ikisi de katkıda bulunur.

:::satz Teorem 7.3 (Bir kuadratik formun gradyanı)
<span class="anker" id="satz-7-3"></span>

Bir $\mathbf{A}\in\mathbb{R}^{n\times n}$ matrisi için şu geçerlidir:

<span class="anker" id="gl-7-2"></span>
$$\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\,\mathbf{x} . \tag{7.2}$$

$\mathbf{A}$ simetrikse bu $2\mathbf{A}\mathbf{x}$ olur. Özellikle $\nabla\lVert\mathbf{x}\rVert^2=\nabla(\mathbf{x}^{\top}\mathbf{x})=2\mathbf{x}$ olur.
:::

:::beweis Bir kuadratik formun gradyanı
$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{j=1}^nx_i\,a_{ij}\,x_j$ olur. $x_k$ değişkenine göre türev alınınca iki terim grubu katkıda bulunur: türevi $\sum_ja_{kj}x_j=(\mathbf{A}\mathbf{x})_k$ olan $i=k$ terimleri ve türevi $\sum_ix_ia_{ik}=(\mathbf{A}^{\top}\mathbf{x})_k$ olan $j=k$ terimleri. $i=j=k$ olan terim $a_{kk}x_k^2$ olup türevi $2a_{kk}x_k$ olur; bu terim iki grupta da birer kez $a_{kk}x_k$ olarak yer alır. Dolayısıyla gradyanın $k$ bileşeni $(\mathbf{A}\mathbf{x})_k+(\mathbf{A}^{\top}\mathbf{x})_k$ olur.
:::

[Bölüm 2, Kesim 5.2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-2)'ye göre kuadratik form yalnızca $\mathbf{S}=\tfrac12(\mathbf{A}+\mathbf{A}^{\top})$ simetrik kısmına bağlıdır. Formül buna uyar: $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=2\mathbf{S}\mathbf{x}$.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)$ için $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=x_1^2+2x_1x_2+3x_2^2$, dolayısıyla $\mathbf{x}=(1,\,1)^{\top}$ noktasında değer $6$ olur. [(7.2)](#gl-7-2) uyarınca şu bulunur:

$$\nabla f(1,1)=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=\begin{pmatrix}2&2\\2&6\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}2+2\\2+6\end{pmatrix}=\begin{pmatrix}4\\8\end{pmatrix}.$$

Kısmi türevlerle sağlama: $2x_1+2x_2=4$ ve $2x_1+6x_2=8$. Yalnızca simetrik matrisler için geçerli olan $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$ formülü burada yanlış olurdu.
::::

⁠**Kısacası:** $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ ifadesinin gradyanı $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, simetrik $\mathbf{A}$ için yani $2\mathbf{A}\mathbf{x}$ olur; $\lVert\mathbf{x}\rVert^2$ ifadesininki ise $2\mathbf{x}$ olur.

### Bir artığın kareler toplamı

<span class="anker" id="stufe-7-4"></span>

[Bölüm 2, Kesim 3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3)'te $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ artığı, çözümü olmayan bir $\mathbf{A}\mathbf{x}=\mathbf{y}$ denklem sisteminin hata vektörüydü ve en kısa artığa sahip $\mathbf{x}$ aranıyordu. $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ kareler toplamı $\mathbf{x}$'in bir fonksiyonudur ve gradyanı, onun $\mathbf{x}$'teki bir değişime nasıl tepki verdiğini söyler.

:::satz Teorem 7.4 (Kareler toplamının gradyanı)
<span class="anker" id="satz-7-4"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ ve $\mathbf{y}\in\mathbb{R}^m$ olmak üzere $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ için şu geçerlidir:

<span class="anker" id="gl-7-3"></span>
$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})=2\mathbf{A}^{\top}(\mathbf{A}\mathbf{x}-\mathbf{y}). \tag{7.3}$$
:::

:::beweis Kareler toplamının gradyanı
Fonksiyon bir bileşkedir: Önce $\mathbf{r}(\mathbf{x})=\mathbf{y}-\mathbf{A}\mathbf{x}$ afin dönüşümü artığı oluşturur, sonra $\mathbf{r}\mapsto\lVert\mathbf{r}\rVert^2$ onun kareler toplamını oluşturur. Kesim [5.4](die-jacobi-matrix.html#stufe-5-4)'e göre $\mathbf{J}_{\mathbf{r}}=-\mathbf{A}$, [(7.2)](#gl-7-2) uyarınca $\nabla_{\mathbf{r}}\lVert\mathbf{r}\rVert^2=2\mathbf{r}$ olur. [(6.3)](die-kettenregel-fur-mehrere-variablen.html#gl-6-3) zincir kuralı $\nabla f=(-\mathbf{A})^{\top}\,2\mathbf{r}=-2\mathbf{A}^{\top}\mathbf{r}$ sonucunu verir.
:::

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$, $\mathbf{y}=(1,\,0)^{\top}$ ve $\mathbf{x}=(2,\,1)^{\top}$ olsun. O zaman $\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, artık $\mathbf{r}=(-3,\,-1)^{\top}$ ve $f(\mathbf{x})=9+1=10$ olur. $\mathbf{A}^{\top}\mathbf{r}=(-3,\,-7)^{\top}$ ile şu bulunur:

$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}\mathbf{r}=-2\begin{pmatrix}-3\\-7\end{pmatrix}=\begin{pmatrix}6\\14\end{pmatrix}$$

(Şekil [13](#abb-13)). Sağlama: Açık yazıldığında $f(\mathbf{x})=(1-x_1-2x_2)^2+x_2^2$ olur; kısmi türevleri de $-2\,(1-x_1-2x_2)=6$ ve $-4\,(1-x_1-2x_2)+2x_2=12+2=14$ olur.

:::abbildung ml/k3rresiduum 13
$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ kareler toplamının gradyanı: $\mathbf{A}^{\top}\mathbf{r}$ vektörünün her bileşeni, $\mathbf{A}$ matrisinin bir sütunu ile artığın iç çarpımıdır.
:::
::::

Formül [Bölüm 2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) ile bağlantılıdır. Orada $\hat{\mathbf{x}}$ en iyi yaklaşık çözümünün artığı $\mathbf{A}$ matrisinin bütün sütunlarına dikti, yani $\mathbf{A}^{\top}\hat{\mathbf{r}}=\mathbf{0}$ idi ve normal denklemler $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ buradan çıkmıştı. [(7.3)](#gl-7-3) uyarınca bu şu demektir: $\hat{\mathbf{x}}$ noktasında kareler toplamının gradyanı sıfırdır; kareler toplamı orada, ikinci mertebe terimler dışında, hiçbir doğrultuda artmaz ve azalmaz. [Bölüm 2, Kesim 3.3](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-3)'teki örnek için, yani $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ matrisi, $\mathbf{y}=(1,\,1,\,1)^{\top}$ ve $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$ ile $\hat{\mathbf{r}}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ ve $\mathbf{A}^{\top}\hat{\mathbf{r}}=(\tfrac13-\tfrac13,\ \tfrac13-\tfrac13)^{\top}=\mathbf{0}$ olur.

⁠**Kısacası:** $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ ifadesinin gradyanı $-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$ olur; tam olarak artığın $\mathbf{A}$ matrisinin sütunlarına dik olduğu yerde sıfır olur.

### Bir matrise göre türev

<span class="anker" id="stufe-7-5"></span>

Bazen değişken bir vektör değil, bütün bir matristir: Bir matrisin bir elemanı değiştirildiğinde bir sayı nasıl değişir? Uzlaşımın (iii) kuralına göre $m\cdot n$ kısmi türev matrisin şeklinde düzenlenir. O zaman doğrusal yaklaşım alışıldığı gibi geçerlidir, yalnızca iç çarpım bütün elemanlar üzerinden alınır:

<span class="anker" id="gl-7-4"></span>
$$f(\mathbf{A}+\mathbf E)\approx f(\mathbf{A})+\sum_{i=1}^m\sum_{j=1}^n\bigl(\nabla_{\mathbf{A}}f\bigr)_{ij}\,e_{ij} \tag{7.4}$$

Burada $\mathbf E$, elemanları $e_{ij}$ olan küçük bir matristir. Çift toplam, [Bölüm 2, Kesim 6.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5)'teki izle yazılan $\operatorname{iz}\bigl((\nabla_{\mathbf{A}}f)^{\top}\mathbf E\bigr)$ ifadesiyle aynı şeydir.

:::satz Teorem 7.5 (Bir matrise göre iki türev)
<span class="anker" id="satz-7-5"></span>

Sabit $\mathbf{u}\in\mathbb{R}^m$, $\mathbf{v}\in\mathbb{R}^n$ vektörleri ve bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisi için şu geçerlidir:

<span class="anker" id="gl-7-5"></span>
$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top},\qquad \nabla_{\mathbf{A}}\lVert\mathbf{A}\rVert_F^2=2\mathbf{A} . \tag{7.5}$$

Burada $\lVert\mathbf{A}\rVert_F$, [Bölüm 2, Kesim 10.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/naherung-durch-matrizen-von-kleinem-rang.html#stufe-10-1)'deki Frobenius normudur.
:::

:::beweis Bir matrise göre iki türev
$\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\sum_i\sum_ju_i\,a_{ij}\,v_j$ olur. $a_{ij}$ elemanı tam olarak bir terimde, $u_iv_j$ çarpanıyla geçer. Dolayısıyla $\partial(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})/\partial a_{ij}=u_iv_j$ olur ve bu, [Bölüm 1, Kesim 9.5](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5)'teki $\mathbf{u}\mathbf{v}^{\top}$ dış çarpımının $(i,j)$ elemanıdır. Aynı biçimde $\lVert\mathbf{A}\rVert_F^2=\sum_{i,j}a_{ij}^2$ olur ve bunun $\partial/\partial a_{ij}$ türevi $2a_{ij}$ olur.
:::

::::beispiel [Sayısal örnek]
$\mathbf{u}=(1,\,2)^{\top}$ ve $\mathbf{v}=(3,\,-1)^{\top}$ için her $\mathbf{A}$ noktasında şu geçerlidir:

$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}=\begin{pmatrix}3&-1\\6&-2\end{pmatrix},$$

çünkü fonksiyon $\mathbf{A}$ bakımından doğrusaldır. $\mathbf{A}=\mathbf{I}$ için $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}=3-2=1$ olur. $a_{21}$ elemanı $0{,}1$ büyütülürse gradyan $6\cdot0{,}1=0{,}6$'lık bir değişim öngörür. Gerçekten de $a_{21}$ yalnızca $u_2\,a_{21}\,v_1=2\cdot a_{21}\cdot3$ teriminde geçer ve bu terim $0{,}6$ artar.
::::

⁠**Kısacası:** Bir sayının bir matrise göre türevi matrisin şekline sahiptir; $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}$ için $\mathbf{u}\mathbf{v}^{\top}$ dış çarpımıdır, $\lVert\mathbf{A}\rVert_F^2$ için $2\mathbf{A}$ olur.

### Bir matris çarpımı boyunca geriye doğru

<span class="anker" id="stufe-7-6"></span>

Çoğu zaman bir $\mathbf{y}=\mathbf{A}\mathbf{x}$ matris-vektör çarpımı, sonunda bir $f(\mathbf{y})$ sayısı duran daha uzun bir hesabın yalnızca bir ara adımıdır. Bu sayının $\mathbf{y}$'ye nasıl tepki verdiği, yani $\nabla f(\mathbf{y})$ zaten biliniyorsa, buradan sayının $\mathbf{A}$'ya ve $\mathbf{x}$'e nasıl tepki verdiği okunmak istenir. Bir yapı taşı boyunca geriye doğru yapılan bu hesap, Kesim [10](automatische-differentiation.html#stufe-10)'daki ters mod için kalıptır.

:::satz Teorem 7.6 (Matris çarpımının geri kuralı)
<span class="anker" id="satz-7-6"></span>

$f:\mathbb{R}^m\to\mathbb{R}$ türevlenebilir, $\mathbf{A}\in\mathbb{R}^{m\times n}$ olmak üzere $\mathbf{y}=\mathbf{A}\mathbf{x}$ ve $F(\mathbf{A},\mathbf{x})=f(\mathbf{A}\mathbf{x})$ olsun. O zaman şu geçerlidir:

<span class="anker" id="gl-7-6"></span>
$$\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\,\nabla f(\mathbf{y}). \tag{7.6}$$

Daha genel olarak $\mathbf{C}=\mathbf{A}\mathbf{B}$ ve $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$ için şu geçerlidir: $\nabla_{\mathbf{A}}F=(\nabla_{\mathbf{C}}f)\,\mathbf{B}^{\top}$ ve $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\,(\nabla_{\mathbf{C}}f)$.
:::

:::beweis Matris çarpımının geri kuralı
$y_i=\sum_ka_{ik}x_k$ olur. $a_{ij}$ elemanı yalnızca $y_i$'yi etkiler, hem de $\partial y_i/\partial a_{ij}=x_j$ çarpanıyla. Dolayısıyla $a_{ij}$'den $f$'ye yalnızca bir yol vardır ve $\partial F/\partial a_{ij}=\frac{\partial f}{\partial y_i}\,x_j$ olur; bu, $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ matrisinin $(i,j)$ elemanıdır. $x_j$ değişkeni ise her $y_i$'yi $a_{ij}$ çarpanıyla etkiler; bütün yollar üzerinden toplandığında $\partial F/\partial x_j=\sum_i\frac{\partial f}{\partial y_i}\,a_{ij}$ olur, yani $\mathbf{A}^{\top}\nabla f(\mathbf{y})$ vektörünün $j$ bileşeni. İkinci önerme de aynı biçimde çıkar, çünkü $\mathbf{C}=\mathbf{A}\mathbf{B}$ sütun sütun bir matris-vektör çarpımıdır.
:::

::::beispiel [Sayısal örnek]
[Bölüm 1, Kesim 7.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-1)'de $\mathbf{A}=\Bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\Bigr)$ ve $\mathbf{x}=(2,\,1)^{\top}$, dolayısıyla $\mathbf{y}=\mathbf{A}\mathbf{x}=(4,\,-1,\,7)^{\top}$ idi. $f(\mathbf{y})=y_1-y_3=-3$, yani $\nabla f(\mathbf{y})=(1,\,0,\,-1)^{\top}$ olsun. [(7.6)](#gl-7-6) uyarınca şu bulunur:

$$\nabla_{\mathbf{A}}F=\begin{pmatrix}1\\0\\-1\end{pmatrix}\begin{pmatrix}2&1\end{pmatrix}=\begin{pmatrix}2&1\\0&0\\-2&-1\end{pmatrix},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\begin{pmatrix}1\\0\\-1\end{pmatrix}=\begin{pmatrix}-2\\1\end{pmatrix}$$

(Şekil [14](#abb-14)). Sağlama: Açık yazıldığında $F=(x_1+2x_2)-(3x_1+x_2)=-2x_1+x_2$ olur, gradyanı da $(-2,\,1)^{\top}$ olur. $\nabla_{\mathbf{A}}F$ matrisinin ikinci satırı sıfırdır, çünkü $y_2$, $f$ içinde geçmez; $\mathbf{A}$ matrisinin ikinci satırındaki elemanlar yalnızca $y_2$ üzerine etki eder.

:::abbildung ml/k3rrueck 14
Bir matris-vektör çarpımının girdisine göre gradyan: Her bileşen, $f$ fonksiyonunun $y_i$ çıktısına ne kadar güçlü tepki verdiğini üç $y_i$ çıktısının hepsi üzerinden toplar ve bunu, $x_j$'nin $y_i$ üzerine etki ettiği $a_{ij}$ çarpanıyla ağırlıklandırır.
:::
::::

:::warnung Şekil kontrolü bir ispat değil, bir akılda tutma yoludur
Şekiller [(7.6)](#gl-7-6) bağıntısını neredeyse belirler: $\nabla_{\mathbf{A}}F$, $m\times n$ şekline sahip olmalıdır ve $m$ elemanlı $\nabla f(\mathbf{y})$ sütunu ile $n$ elemanlı $\mathbf{x}$ sütunundan yalnızca $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ bu şekli verir. Kural bu yolla akılda tutulabilir. Ama şekil kontrolü ne yanlış bir işareti ne eksik bir çarpanı ne de kare matrislerde yer değiştirmiş bir sırayı fark eder. Kural ancak bileşenlerle yapılan hesapla gerekçelendirilmiş olur.
:::

⁠**Kısacası:** $\mathbf{y}=\mathbf{A}\mathbf{x}$ boyunca geriye doğru: $\mathbf{A}$'ya göre gradyan $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, $\mathbf{x}$'e göre gradyan $\mathbf{A}^{\top}\nabla f(\mathbf{y})$ olur.

:::aufgabe Alıştırma 24 ★ Matris yazılışıyla gradyanlar
<span class="anker" id="aufg-24"></span>

Bu kesimin formülleriyle hesaplayın ve her seferinde kısmi türevlerle sağlamasını yapın.

<ol class="al">

<li>

$\mathbf{b}=(2,\,-1,\,4)^{\top}$ olmak üzere $f(\mathbf{x})=\mathbf{b}^{\top}\mathbf{x}+5$;

</li>

<li>

$(1,\,-1,\,2)$ noktasında $f(\mathbf{x})=\lVert\mathbf{x}\rVert^2$;

</li>

<li>

$(1,\,-1)$ noktasında, $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\3&4\end{smallmatrix}\bigr)$ olmak üzere $f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$.

</li>

</ol>

:::loesung
(a) [(7.1)](#gl-7-1) uyarınca $\nabla f=\mathbf{b}=(2,\,-1,\,4)^{\top}$. Sağlama: $f=2x_1-x_2+4x_3+5$.

(b) $\mathbf{A}=\mathbf{I}$ ile [(7.2)](#gl-7-2) uyarınca $\nabla f=2\mathbf{x}=(2,\,-2,\,4)^{\top}$. Sağlama: $\partial_jf=2x_j$.

(c) $\mathbf{A}+\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&4\\4&8\end{smallmatrix}\bigr)$, dolayısıyla $\nabla f(1,-1)=(4-4,\ 4-8)^{\top}=(0,\,-4)^{\top}$. Sağlama: $f=2x_1^2+4x_1x_2+4x_2^2$ fonksiyonunun kısmi türevleri $4x_1+4x_2=0$ ve $4x_1+8x_2=-4$ olur.
:::
:::

:::aufgabe Alıştırma 25 ★★ Bölüm 2'deki en küçük kareler doğrusu
<span class="anker" id="aufg-25"></span>

[Bölüm 2, Kesim 3.6](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-6)'da $(0,\,1)$, $(1,\,2)$ ve $(2,\,4)$ noktalarından, $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$ ve $\mathbf{y}=(1,\,2,\,4)^{\top}$ ile bir doğru geçirilmişti.

<ol class="al">

<li>

$\mathbf{x}=(1,\,1)^{\top}$ noktasında $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ değerini ve $\nabla f(\mathbf{x})$ gradyanını hesaplayın.

</li>

<li>

$f$ en hızlı biçimde küçülsün diye $\mathbf{x}$, $(1,\,1)$ noktasından hangi yönde küçük bir parça kaydırılmalıdır?

</li>

<li>

[Bölüm 2](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html)'deki $\hat{\mathbf{x}}=(\tfrac56,\,\tfrac32)^{\top}$ noktasında gradyanın sıfır olduğunu gösterin.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$, $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}=(0,\,0,\,1)^{\top}$ ve $f=1$. $\mathbf{A}^{\top}\mathbf{r}=(0+0+1,\ 0+0+2)^{\top}=(1,\,2)^{\top}$ ile $\nabla f=-2\mathbf{A}^{\top}\mathbf{r}=(-2,\,-4)^{\top}$ olur.

(b) $f$ en hızlı biçimde $-\nabla f/\lVert\nabla f\rVert=(2,\,4)^{\top}/\sqrt{20}=(1,\,2)^{\top}/\sqrt5\approx(0{,}447;\ 0{,}894)^{\top}$ doğrultusunda küçülür: Eksen kesişimi biraz, eğim ise bunun iki katı kadar artmalıdır. Bu, $1+t$ doğrusunun üçüncü nokta olan $(2,\,4)$ noktasını $1$ farkla tutturamamasıyla uyumludur.

(c) $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\ \tfrac73,\ \tfrac{23}6)^{\top}$, dolayısıyla $\hat{\mathbf{r}}=(\tfrac16,\ -\tfrac13,\ \tfrac16)^{\top}$ ve

$$\mathbf{A}^{\top}\hat{\mathbf{r}}=\begin{pmatrix}\tfrac16-\tfrac13+\tfrac16\\0-\tfrac13+\tfrac26\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$

Gradyan sıfırdır: En iyi yaklaşık çözümde hiçbir küçük yer değiştirme kareler toplamını birinci mertebede değiştirmez.
:::
:::

:::aufgabe Alıştırma 26 ★★ Bir matrise göre türevler
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Kare bir $\mathbf{A}$ için $\nabla_{\mathbf{A}}\operatorname{iz}\mathbf{A}=\mathbf{I}$ olduğunu gösterin.

</li>

<li>

[(7.6)](#gl-7-6) ve $\nabla\lVert\mathbf{y}\rVert^2=2\mathbf{y}$ ile $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$ olduğunu gösterin ve bunu $\mathbf{A}=\mathbf{I}\in\mathbb{R}^{2\times2}$ ve $\mathbf{x}=(1,\,2)^{\top}$ için hesaplayın.

</li>

<li>

(b)'yi [(7.4)](#gl-7-4) doğrusal yaklaşımıyla kontrol edin: $a_{12}$, $0$'dan $0{,}01$'e artırılırsa $\lVert\mathbf{A}\mathbf{x}\rVert^2$ yaklaşık ne kadar değişir? Hesaplayarak doğrulayın.

</li>

</ol>

:::loesung
(a) $\operatorname{iz}\mathbf{A}=\sum_ia_{ii}$. $a_{ij}$'ye göre türev $i=j$ için $1$, aksi hâlde $0$ olur; $\mathbf{A}$ şeklinde dizilince bu $\mathbf{I}$ verir.

(b) $\mathbf{y}=\mathbf{A}\mathbf{x}$ ve $\nabla f(\mathbf{y})=2\mathbf{y}$ ile $\lVert\mathbf{A}\mathbf{x}\rVert^2=f(\mathbf{y})$ olur. [(7.6)](#gl-7-6) uyarınca $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\mathbf{y}\,\mathbf{x}^{\top}=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$. $\mathbf{A}=\mathbf{I}$ ve $\mathbf{x}=(1,\,2)^{\top}$ için:

$$\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\begin{pmatrix}1\\2\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix}=\begin{pmatrix}2&4\\4&8\end{pmatrix}.$$

(c) Gradyanın $(1,2)$ elemanı $4$ olduğundan [(7.4)](#gl-7-4) yaklaşık $4\cdot0{,}01=0{,}04$ kadar bir değişim öngörür. Tam hesap: $a_{12}=0{,}01$ ile $\mathbf{A}\mathbf{x}=(1{,}02;\ 2)^{\top}$ ve $\lVert\mathbf{A}\mathbf{x}\rVert^2=1{,}0404+4=5{,}0404$, yani $5$'e göre $0{,}0404$ kadar bir değişim.
:::
:::

:::aufgabe Alıştırma 27 ★★★ İki matrisin çarpımı için geri kuralı
<span class="anker" id="aufg-27"></span>

$\mathbf{C}=\mathbf{A}\mathbf{B}$ ve $\mathbf G=\nabla_{\mathbf{C}}f$ olmak üzere $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$ olsun.

<ol class="al">

<li>

$\nabla_{\mathbf{A}}F=\mathbf G\mathbf{B}^{\top}$ ve $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\mathbf G$ olduğunu bileşen bileşen gösterin.

</li>

<li>

$\mathbf{A}=(1\ \ 2)$, $\mathbf{B}=\bigl(\begin{smallmatrix}3\\4\end{smallmatrix}\bigr)$ ve $f(\mathbf{C})=c_{11}^2$ için iki formülü de $F$'yi açık yazarak kontrol edin.

</li>

</ol>

:::loesung
(a) $c_{ik}=\sum_ja_{ij}b_{jk}$ olur. $a_{ij}$ elemanı, $i$ satırındaki bütün $c_{ik}$ elemanlarına $b_{jk}$ çarpanıyla etki eder; bu yollar üzerinden toplanınca $\partial F/\partial a_{ij}=\sum_kg_{ik}b_{jk}=(\mathbf G\mathbf{B}^{\top})_{ij}$ bulunur. $b_{jk}$ elemanı, $k$ sütunundaki bütün $c_{ik}$ elemanlarına $a_{ij}$ çarpanıyla etki eder; dolayısıyla $\partial F/\partial b_{jk}=\sum_ia_{ij}g_{ik}=(\mathbf{A}^{\top}\mathbf G)_{jk}$ olur.

(b) $\mathbf{C}=1\cdot3+2\cdot4=11$, $F=121$ ve $\mathbf G=2c_{11}=22$. Formüller $\nabla_{\mathbf{A}}F=22\,(3\ \ 4)=(66\ \ 88)$ ve $\nabla_{\mathbf{B}}F=(1,\,2)^{\top}\cdot22=(22,\,44)^{\top}$ verir. Açık yazılınca $F=(3a_{11}+4a_{12})^2$ olur, türevleri $2\cdot11\cdot3=66$ ve $2\cdot11\cdot4=88$; ayrıca $F=(b_{11}+2b_{21})^2$ olur, türevleri $22$ ve $44$.
:::
:::
