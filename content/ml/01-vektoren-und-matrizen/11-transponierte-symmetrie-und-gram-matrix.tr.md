---
title: Devrik, simetri ve Gram matrisi
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211100
summary: Bir matrisin satırları ile sütunlarının yeri değiştirilirse matrisin devriği ortaya çıkar.
tags: devriği, simetrik, Gram matrisi
lang: tr
---

<span class="anker" id="stufe-10"></span>

:::zweck
Bir matrisin satırları ile sütunlarının yeri değiştirilirse matrisin devriği ortaya çıkar. Devrik sayesinde bir veri kümesinin bütün iç çarpımları tek bir matriste toplanabilir: bütün örneklerin birbirine benzerlikleri ve bütün özniteliklerin birbiriyle ilişkileri.
:::

### Devrik

<span class="anker" id="stufe-10-1"></span>

$^{\top}$ işareti daha önceden bilinir (alt kesim [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3)): Bir sütunu satıra çevirir. Matrisler için de aynı anlama gelir, yalnızca her sütuna uygulanır: $j$ numaralı sütun $j$ numaralı satır olur. Bu sırada matris köşegenine göre yansıtılır.

:::definition Tanım 10.1 (Devrik)
<span class="anker" id="satz-10-1"></span>

Bir $\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin __devriği__, şu eşitliği sağlayan $\mathbf{A}^{\top}\in\mathbb{R}^{n\times m}$ matrisidir:

<span class="anker" id="gl-10-1"></span>
$$(\mathbf{A}^{\top})_{ij}=a_{ji} . \tag{10.1}$$
:::

Bir $\mathbf{x}\in\mathbb{R}^d$ vektörü $d\times1$ tipinde bir matristir; devriği $\mathbf{x}^{\top}$ ise aynı elemanlara sahip $1\times d$ tipindeki matristir. Böylece $\mathbf{u}^{\top}\mathbf{v}$ yazılışı (alt kesim [2.1](das-skalarprodukt.html#stufe-2-1)) artık kelimenin tam anlamıyla bir matris çarpımıdır: $1\times d$ tipinde bir matris çarpı $d\times1$ tipinde bir matris; sonuç $1\times1$ tipinde bir matris, yani bir sayıdır.

:::satz Teorem 10.2 (Devriğin hesap kuralları)
<span class="anker" id="satz-10-2"></span>

Tipleri uygun matrisler ve $c$ skalerleri için şunlar geçerlidir:

$$(\mathbf{A}^{\top})^{\top}=\mathbf{A},\qquad(\mathbf{A}+\mathbf{B})^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top},\qquad(c\,\mathbf{A})^{\top}=c\,\mathbf{A}^{\top},\qquad(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top} .$$
:::

:::herleitung Bir çarpımın devriği
$\mathbf{A}\in\mathbb{R}^{m\times n}$ ve $\mathbf{B}\in\mathbb{R}^{n\times k}$ için [(10.1)](#gl-10-1) ve [(9.1)](das-matrixprodukt.html#gl-9-1) uyarınca şu bulunur:

$$\bigl((\mathbf{A}\mathbf{B})^{\top}\bigr)_{li}=(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^na_{ij}\,b_{jl}=\sum_{j=1}^n(\mathbf{B}^{\top})_{lj}\,(\mathbf{A}^{\top})_{ji}=(\mathbf{B}^{\top}\mathbf{A}^{\top})_{li} .$$

İlk üç kural doğrudan tanımdan çıkar.
:::

::::beispiel [Sayısal örnek]
$$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^{\top}=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.$$

$\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ ve $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ için $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$, dolayısıyla $(\mathbf{C}\mathbf{D})^{\top}=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$ olur. $\mathbf{D}^{\top}\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$ aynı sonucu verir; $\mathbf{C}^{\top}\mathbf{D}^{\top}=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$ ise başka bir şeydir.
::::

⁠**Kısacası:** Devrik almak satırlarla sütunların yerini değiştirir; çarpımda sıra tersine döner, $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$.

:::hintergrund Bir çarpımın devriği alınırken sıra neden tersine döner?
$\mathbf{A}\mathbf{B}$ çarpımında $\mathbf{A}$ matrisinin satırları $\mathbf{B}$ matrisinin sütunlarıyla buluşur. Devrik alındıktan sonra $\mathbf{A}$ matrisinin satırları $\mathbf{A}^{\top}$ matrisinin sütunları, $\mathbf{B}$ matrisinin sütunları da $\mathbf{B}^{\top}$ matrisinin satırları olur. Satırların yine sütunlarla buluşması için $\mathbf{B}^{\top}$ solda durmalıdır. Tipler de bunu gösterir: $(\mathbf{A}\mathbf{B})^{\top}$ matrisi $k\times m$ tipindedir ve $\mathbf{B}^{\top}\mathbf{A}^{\top}$ çarpımı $(k\times n)\cdot(n\times m)$ biçimindedir, yani tipler uyar. $\mathbf{A}^{\top}\mathbf{B}^{\top}$ ifadesi $(n\times m)\cdot(k\times n)$ olurdu ve ancak rastlantı sonucu $m=k$ ise tanımlıdır. Kuralın özel bir durumu $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ eşitliğidir: Bir sayı kendi devriğidir, dolayısıyla $\mathbf{u}^{\top}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{u}$ olur.
:::

### Simetrik matrisler

<span class="anker" id="stufe-10-2"></span>

Bazı tablolar köşegenlerine göre yansıtıldığında değişmez. Şehirler arası bir uzaklık tablosu böyledir: Münih'ten Köln'e giden yol, Köln'den Münih'e giden yol kadar uzundur.

:::definition Tanım 10.3 (Simetrik matris)
<span class="anker" id="satz-10-3"></span>

$\mathbf{A}^{\top}=\mathbf{A}$, yani bütün $i,j$ için $a_{ij}=a_{ji}$ ise bir $\mathbf{A}$ kare matrisine __simetrik__ denir.
:::

Her köşegen matris simetriktir. Simetrik matrislerin önemli bir kaynağı, bir matrisin kendi devriğiyle çarpımlarıdır: Her $\mathbf{A}$ matrisi için şu geçerlidir:

<span class="anker" id="gl-10-2"></span>
$$(\mathbf{A}^{\top}\mathbf{A})^{\top}=\mathbf{A}^{\top}(\mathbf{A}^{\top})^{\top}=\mathbf{A}^{\top}\mathbf{A} , \tag{10.2}$$

dolayısıyla $\mathbf{A}^{\top}\mathbf{A}$ simetriktir; $\mathbf{A}\mathbf{A}^{\top}$ de öyle.

::::beispiel [Sayısal örnek]
$\bigl(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\bigr)$ simetriktir, $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ dönmesi değildir. $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ için şu bulunur:

$$\mathbf{C}^{\top}\mathbf{C}=\begin{pmatrix}1&3\\2&4\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}10&14\\14&20\end{pmatrix},$$

ve bu matris, [(10.2)](#gl-10-2) eşitliğinin gerektirdiği gibi simetriktir.
::::

⁠**Kısacası:** Simetrik bir matris kendi devriğine eşittir; $\mathbf{A}^{\top}\mathbf{A}$ ve $\mathbf{A}\mathbf{A}^{\top}$ her zaman simetriktir.

:::hintergrund Ağırlıklı iç çarpımlar
$\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ iç çarpımında her yer aynı ağırlıkta sayılır. Yerler farklı ağırlıklarla sayılmak istenirse pozitif $d_1,\dots,d_n$ ağırlıkları alınır ve $\sum_jd_j\,u_jv_j$ oluşturulur. $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$ köşegen matrisiyle bu, $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$ olur, çünkü $\mathbf{D}\mathbf{v}=(d_1v_1,\dots,d_nv_n)^{\top}$.

Bu sayı, sıradan iç çarpımla aynı hesap kurallarına uyar. İki vektörün her birinde doğrusaldır ve her $\mathbf{u}\ne\mathbf{0}$ için $\mathbf{u}^{\top}\mathbf{D}\mathbf{u}=\sum_jd_ju_j^2$ pozitiftir. $\mathbf{D}$ simetrik olduğu için simetriktir: Bir sayı kendi devriğidir ve bir çarpımın devriği için kural iki kez uygulanınca $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{D}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{D}^{\top}\mathbf{u}=\mathbf{v}^{\top}\mathbf{D}\mathbf{u}$ bulunur. Cauchy-Schwarz eşitsizliğinin ispatı yalnızca bu kuralları kullandığı için $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$ ile de uzunluklar, uzaklıklar ve açılar ölçülebilir. Bunlar yalnızca farklı çıkar. Örneğin $(1,\,1)^{\top}$ ve $(-1,\,1)^{\top}$ sıradan anlamda ortogonaldir, ama $\mathbf{D}=\operatorname{diag}(2,\,1)$ ile değildir: $(1,\,1)\,\mathbf{D}\,(-1,\,1)^{\top}=2\cdot1\cdot(-1)+1\cdot1\cdot1=-1$.

Standartlaştırma (alt kesim [4.5](abstande-und-einheiten.html#stufe-4-5)) tam olarak böyle bir ağırlıklandırmadır. Standartlaştırılmış iki örneğin uzaklığı, $\mathbf{D}=\operatorname{diag}(1/s_1^2,\dots,1/s_d^2)$ ile $\sqrt{(\mathbf{x}_a-\mathbf{x}_b)^{\top}\mathbf{D}\,(\mathbf{x}_a-\mathbf{x}_b)}$ olur. Tersine, bu türden her ağırlıklandırma bir birim değişikliği gibi etki eder: $j$ özniteliği $\sqrt{d_j}$ ile çarpılırsa dönüştürülmüş vektörlerin sıradan iç çarpımı $\sum_j(\sqrt{d_j}\,u_j)(\sqrt{d_j}\,v_j)=\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$ olur. Demek ki birimlerin seçimi ile $\mathbf{D}$ içindeki ağırlıkların seçimi aynı karardır.
:::

### Örneklerin Gram matrisi

<span class="anker" id="stufe-10-3"></span>

Bir veri kümesinin her örneği öbür her örneğe ne kadar benzer? Bütün ikili iç çarpımlar bir tabloya yazılabilir: $i$ numaralı satır ile $k$ numaralı sütunda $\mathbf{x}_i^{\top}\mathbf{x}_k$ durur. Bu tablo tek bir matris çarpımıdır.

:::definition Tanım 10.4 (Gram matrisi)
<span class="anker" id="satz-10-4"></span>

$\mathbf{v}_1,\dots,\mathbf{v}_k$ vektörlerinden oluşan bir listenin __Gram matrisi__, ikili iç çarpımlardan oluşan ve $i$ numaralı satır ile $l$ numaralı sütununda $\mathbf{v}_i^{\top}\mathbf{v}_l$ elemanı bulunan $k\times k$ tipindeki matristir.
:::

Bir veri kümesinin örnekleri için bu, $\mathbf{X}\mathbf{X}^{\top}\in\mathbb{R}^{N\times N}$ matrisidir. Çünkü bu matrisin $(i,k)$ elemanı, $\mathbf{X}$ matrisinin $i$ numaralı satırı çarpı $\mathbf{X}^{\top}$ matrisinin $k$ numaralı sütunu, yani $\mathbf{x}_i^{\top}\mathbf{x}_k$ olur:

<span class="anker" id="gl-10-3"></span>
$$(\mathbf{X}\mathbf{X}^{\top})_{ik}=\mathbf{x}_i^{\top}\mathbf{x}_k . \tag{10.3}$$

Bu matris simetriktir, köşegeninde $\lVert\mathbf{x}_i\rVert^2$ uzunluk kareleri durur ve [(4.1)](abstande-und-einheiten.html#gl-4-1) uyarınca bütün uzaklıklar ondan okunabilir:

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{x}_i-\mathbf{x}_k\rVert^2=(\mathbf{X}\mathbf{X}^{\top})_{ii}+(\mathbf{X}\mathbf{X}^{\top})_{kk}-2\,(\mathbf{X}\mathbf{X}^{\top})_{ik} . \tag{10.4}$$

$(i,k)$ elemanı $\sqrt{(\mathbf{X}\mathbf{X}^{\top})_{ii}\,(\mathbf{X}\mathbf{X}^{\top})_{kk}}$ değerine bölünürse $\mathbf{x}_i$ ile $\mathbf{x}_k$ vektörlerinin kosinüs benzerliği elde edilir.

::::beispiel [Sayısal örnek]
Üç metin için (alt kesim [5.4](winkel-und-ahnlichkeit.html#stufe-5-4)) şu bulunur:

$$\mathbf{X}=\begin{pmatrix}3&2&0\\6&4&0\\0&1&3\end{pmatrix},\qquad \mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}13&26&2\\26&52&4\\2&4&10\end{pmatrix}.$$

Metin 1 ile Metin 3 arasındaki uzaklık [(10.4)](#gl-10-4) uyarınca, daha önce hesaplandığı gibi $\sqrt{13+10-2\cdot2}=\sqrt{19}$ olur. Metin 1 ile Metin 2 arasındaki kosinüs benzerliği $26/\sqrt{13\cdot52}=1$ olur.
::::

⁠**Kısacası:** $\mathbf{X}\mathbf{X}^{\top}$ Gram matrisi, örneklerin bütün ikili iç çarpımlarının tablosudur; bütün uzunluklar, uzaklıklar ve açılar ondan çıkar.

:::hintergrund Gram matrisi veri kümesinin bütün geometrisini içerir
Örnekler arasındaki uzunluklar, uzaklıklar ve açılar tek tek koordinatlara değil, yalnızca iç çarpımlara bağlıdır. Bütün veri kümesi sözgelimi orijin etrafında döndürülürse bütün koordinatlar değişir, ama hiçbir iç çarpım değişmez ve Gram matrisi aynı kalır. Demek ki aynı Gram matrisine sahip iki veri kümesi geometrik olarak aynı görünür. Bu yüzden yalnızca hangi örneklerin birbirine benzediğini bilmek isteyen kişinin veri matrisinin kendisine değil, yalnızca onun Gram matrisine ihtiyacı vardır.
:::

### Özniteliklerin Gram matrisi

<span class="anker" id="stufe-10-4"></span>

Roller değiştirilirse öznitelikler hakkında bir tablo elde edilir: İki öznitelik bütün örnekler boyunca ne ölçüde birlikte hareket eder? Bu iki özniteliğin öznitelik sütunları $\mathbb{R}^N$ uzayında vektörlerdir ve iç çarpımları bunu ölçer. Sütunların bu Gram matrisi $\mathbf{X}^{\top}\mathbf{X}\in\mathbb{R}^{d\times d}$ olur:

<span class="anker" id="gl-10-5"></span>
$$(\mathbf{X}^{\top}\mathbf{X})_{jl}=\sum_{i=1}^Nx_{ij}\,x_{il} . \tag{10.5}$$

$(j,l)$ elemanı $j$ ve $l$ öznitelik sütunlarının iç çarpımıdır; köşegende bir özniteliğin kareler toplamı durur.

:::satz Teorem 10.5 (Örnekler üzerinden bir toplam olarak Gram matrisi)
<span class="anker" id="satz-10-5"></span>

<span class="anker" id="gl-10-6"></span>
$$\mathbf{X}^{\top}\mathbf{X}=\sum_{i=1}^N\mathbf{x}_i\,\mathbf{x}_i^{\top} . \tag{10.6}$$

Her örnek kendi dış çarpımıyla katkı yapar.
:::

Sağ tarafın $(j,l)$ elemanı $\sum_ix_{ij}\,x_{il}$ olur, yani [(10.5)](#gl-10-5) formülündekiyle aynıdır. Demek ki yeni bir örnek eklenirse $\mathbf{X}^{\top}\mathbf{X}$ yalnızca bir $\mathbf{x}_{N+1}\mathbf{x}_{N+1}^{\top}$ katmanı kadar değişir; her şeyi yeniden hesaplamak gerekmez.

::::beispiel [Sayısal örnek]
Metinler için şu bulunur:

$$\mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$

Birinci satırın elemanları, “gol” sütununun üç öznitelik sütunuyla iç çarpımlarıdır (Şekil [37](#abb-37)).

:::abbildung ml/k1rgrammerk 37
Özniteliklerin Gram matrisinin birinci satırı: $(3,\,6,\,0)^{\top}$ “gol” sütunu çarpı kendisi, çarpı $(2,\,4,\,1)^{\top}$ “top” sütunu ve çarpı $(0,\,0,\,3)^{\top}$ “seçim” sütunu.
:::

$(1,3)$ yerindeki $0$ şunu söyler: “gol” ve “seçim” sözcükleri hiçbir metinde birlikte geçmez. Üç dış çarpımın toplamı olarak:

$$\begin{pmatrix}9&6&0\\6&4&0\\0&0&0\end{pmatrix}+\begin{pmatrix}36&24&0\\24&16&0\\0&0&0\end{pmatrix}+\begin{pmatrix}0&0&0\\0&1&3\\0&3&9\end{pmatrix}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$
::::

⁠**Kısacası:** $\mathbf{X}^{\top}\mathbf{X}$ öznitelik sütunlarının Gram matrisidir; bütün örneklerin $\mathbf{x}_i\mathbf{x}_i^{\top}$ dış çarpımlarının toplamıdır.

:::aufgabe Alıştırma 24 ★ Devrik almak
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

$\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ için $\mathbf{B}^{\top}$ matrisini verin ve $\mathbf{B}^{\top}\mathbf{B}$ ile $\mathbf{B}\mathbf{B}^{\top}$ çarpımlarını hesaplayın. Bunlar hangi tiptedir ve simetrik midir?

</li>

<li>

Hesap kurallarıyla gösterin: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{B}^{\top}=\Bigl(\begin{smallmatrix}1&2\\0&1\\2&0\end{smallmatrix}\Bigr)$ olur. Buradan şunlar bulunur:

$$\mathbf{B}^{\top}\mathbf{B}=\begin{pmatrix}5&2&2\\2&1&0\\2&0&4\end{pmatrix}\in\mathbb{R}^{3\times3},\qquad \mathbf{B}\mathbf{B}^{\top}=\begin{pmatrix}5&2\\2&5\end{pmatrix}\in\mathbb{R}^{2\times2}.$$

İkisi de [(10.2)](#gl-10-2) bağıntısının gerektirdiği gibi simetriktir. $\mathbf{B}^{\top}\mathbf{B}$ matrisinin $(1,1)$ elemanı $1^2+2^2=5$, yani birinci sütunun kareler toplamıdır; $\mathbf{B}\mathbf{B}^{\top}$ matrisinin $(1,2)$ elemanı $1\cdot2+0\cdot1+2\cdot0=2$, yani iki satırın iç çarpımıdır.

(b) Çarpımın devriği kuralı iki kez uygulanır: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\bigl((\mathbf{A}\mathbf{B})\mathbf{C}\bigr)^{\top}=\mathbf{C}^{\top}(\mathbf{A}\mathbf{B})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.
:::
:::

:::aufgabe Alıştırma 25 ★★ Küçük bir veri kümesinin Gram matrisleri
<span class="anker" id="aufg-25"></span>

Bir veri kümesinde iki öznitelikli üç örnek var: $\mathbf{x}_1=(1,\,0)^{\top}$, $\mathbf{x}_2=(2,\,1)^{\top}$, $\mathbf{x}_3=(0,\,3)^{\top}$.

<ol class="al">

<li>

$\mathbf{X}$ matrisini kurun ve $\mathbf{X}\mathbf{X}^{\top}$ ile $\mathbf{X}^{\top}\mathbf{X}$ matrislerini hesaplayın.

</li>

<li>

$\mathbf{x}_2$ ile $\mathbf{x}_3$ arasındaki uzaklığı $\mathbf{X}\mathbf{X}^{\top}$ matrisinden okuyun ve doğrudan kontrol edin.

</li>

<li>

Üç $\mathbf{x}_i\mathbf{x}_i^{\top}$ dış çarpımını toplayarak [(10.6)](#gl-10-6) eşitliğini doğrulayın.

</li>

</ol>

:::loesung
(a) $\mathbf{X}=\Bigl(\begin{smallmatrix}1&0\\2&1\\0&3\end{smallmatrix}\Bigr)$ olur ve şunlar bulunur:

$$\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}1&2&0\\2&5&3\\0&3&9\end{pmatrix},\qquad \mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}5&2\\2&10\end{pmatrix}.$$

(b) [(10.4)](#gl-10-4) uyarınca $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert^2=5+9-2\cdot3=8$, dolayısıyla uzaklık $\sqrt8\approx2{,}83$ olur. Doğrudan: $\mathbf{x}_2-\mathbf{x}_3=(2,\,-2)^{\top}$, uzunluğunun karesi $4+4=8$.

(c) $\mathbf{x}_1\mathbf{x}_1^{\top}=\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$, $\mathbf{x}_2\mathbf{x}_2^{\top}=\bigl(\begin{smallmatrix}4&2\\2&1\end{smallmatrix}\bigr)$, $\mathbf{x}_3\mathbf{x}_3^{\top}=\bigl(\begin{smallmatrix}0&0\\0&9\end{smallmatrix}\bigr)$; bunların toplamı $\bigl(\begin{smallmatrix}5&2\\2&10\end{smallmatrix}\bigr)=\mathbf{X}^{\top}\mathbf{X}$ olur.
:::
:::
