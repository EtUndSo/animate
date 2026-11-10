---
title: Küçük ranklı matrislerle yaklaşım
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Bölüm 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15221100
summary: Tekil değer ayrışımı bir matrisin yapı taşlarını büyüklüklerine göre sıralar.
tags: Frobenius normu, kesilmiş tekil değer ayrışımı
lang: tr
---

<span class="anker" id="stufe-10"></span>

:::zweck
Tekil değer ayrışımı bir matrisin yapı taşlarını büyüklüklerine göre sıralar. Küçük olanlar atılırsa geriye, çok daha az sayıyla saklanabilen, daha küçük ranklı bir matris kalır. Bu kesim bu yaklaşımın asıl matristen ne kadar uzak olduğunu ölçüyor ve aynı ranktaki başka hiçbir matrisin daha yakın olmadığını kanıtlıyor.
:::

### Frobenius normu

<span class="anker" id="stufe-10-1"></span>

İki matrisin birbirine ne kadar yakın olduğunu söylemek için farklarının büyüklüğünü veren bir ölçü gerekir. Spektral norm böyle bir ölçüdür; en büyük uzatmayı ölçer. İkincisi daha da akla yatkındır: Matris, [Bölüm 1, Kesim 6.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1)'deki bir görüntü gibi satır satır okunarak uzun bir vektöre dönüştürülür ve bu vektörün Öklid normu alınır.

:::definition Tanım 10.1 (Frobenius normu)
<span class="anker" id="satz-10-1"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ matrisinin __Frobenius normu__ şudur:

$$\lVert\mathbf{A}\rVert_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^na_{ij}^2} .$$
:::

:::satz Teorem 10.2 (Frobenius normu ve tekil değerler)
<span class="anker" id="satz-10-2"></span>

Rankı $r$ olan her $\mathbf{A}$ matrisi için şu geçerlidir:

<span class="anker" id="gl-10-1"></span>
$$\lVert\mathbf{A}\rVert_F^2=\operatorname{iz}(\mathbf{A}^{\top}\mathbf{A})=d_1^2+d_2^2+\dots+d_r^2 . \tag{10.1}$$
:::

:::beweis Frobenius normu
$\mathbf{A}^{\top}\mathbf{A}$ matrisinin $j$ numaralı köşegen elemanı $\mathbf{a}_j^{\top}\mathbf{a}_j=\sum_ia_{ij}^2$, yani $j$ numaralı sütunun uzunluğunun karesidir. Bu elemanların toplamı olan iz, dolayısıyla $\mathbf{A}$ matrisinin bütün elemanlarının karelerinin toplamıdır. [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5) uyarınca iz aynı zamanda $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özdeğerlerinin toplamıdır; bunlar da $d_j^2$ değerleridir.
:::

İki sonuç. $d_1^2\le\sum_jd_j^2$ olduğundan $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F$ olur. Ayrıca ortogonal bir matris Frobenius normunu değiştirmez: $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$, dolayısıyla $\mathbf{Q}\mathbf{A}$ ile $\mathbf{A}$ matrislerinin tekil değerleri aynıdır.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için $\lVert\mathbf{A}\rVert_F^2=4+9+0+4=17=4^2+1^2$ (Şekil [24](#abb-24)), dolayısıyla $\lVert\mathbf{A}\rVert_F=\sqrt{17}\approx4{,}12$ olur; bu, $\lVert\mathbf{A}\rVert_2=4$ değerinden biraz fazladır.

:::abbildung ml/k2rfrobenius 24
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ matrisinin Frobenius normunun karesi: bütün elemanların karelerinin toplamı; tekil değerlerin karelerinin toplamına eşittir.
:::
::::

⁠**Kısacası:** Frobenius normu bütün elemanların Öklid normudur; karesi, tekil değerlerin karelerinin toplamıdır.

### Kesilmiş ayrışım

<span class="anker" id="stufe-10-2"></span>

[(9.4)](die-singularwertzerlegung.html#gl-9-4) toplamı en büyük $k$ yapı taşından sonra kesilirse bir yaklaşım elde edilir.

:::definition Tanım 10.3 (Kesilmiş tekil değer ayrışımı)
<span class="anker" id="satz-10-3"></span>

$k<r$ için

<span class="anker" id="gl-10-2"></span>
$$\mathbf{A}_k=\sum_{j=1}^kd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} \tag{10.2}$$

matrisine $\mathbf{A}$ matrisinin $k$ yapı taşlı __kesilmiş tekil değer ayrışımı__ denir.
:::

$\mathbf{A}_k$ matrisinin rankı $k$ olur, çünkü $j\le k$ için $\mathbf{A}_k\mathbf{v}_j=d_j\mathbf{u}_j$ ve $j>k$ için $\mathbf{A}_k\mathbf{v}_j=\mathbf{0}$ olur; demek ki görüntüler $k$ boyutlu bir uzay gerer. Hata, toplamın geri kalanıdır:

$$\mathbf{A}-\mathbf{A}_k=\sum_{j=k+1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} .$$

Hatanın Gram matrisi $\sum_{j>k}d_j^2\mathbf{v}_j\mathbf{v}_j^{\top}$ olur, çünkü karma terimler $\mathbf{u}_i^{\top}\mathbf{u}_j=0$ nedeniyle düşer. Bu matrisin özdeğerleri $d_{k+1}^2,\dots,d_r^2$, geri kalanları sıfırdır. Dolayısıyla hatanın tekil değerleri $d_{k+1},\dots,d_r$ olur ve [(9.5)](die-singularwertzerlegung.html#gl-9-5) ile [(10.1)](#gl-10-1) uyarınca şu bulunur:

<span class="anker" id="gl-10-3"></span>
$$\lVert\mathbf{A}-\mathbf{A}_k\rVert_2=d_{k+1},\qquad \lVert\mathbf{A}-\mathbf{A}_k\rVert_F=\sqrt{d_{k+1}^2+\dots+d_r^2} . \tag{10.3}$$

$\mathbf{A}_k$ matrisini saklamak için yalnızca her biri $m$ elemanlı $k$ tane $\mathbf{u}_j$ vektörü, her biri $n$ elemanlı $k$ tane $\mathbf{v}_j$ vektörü ve $k$ tane $d_j$ sayısı gerekir; toplam $mn$ yerine $k(m+n+1)$ sayı.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ve $k=1$ için şu bulunur:

$$\mathbf{A}_1=4\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1{,}6&3{,}2\\0{,}8&1{,}6\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\mathbf{u}_2\mathbf{v}_2^{\top}=\begin{pmatrix}0{,}4&-0{,}2\\-0{,}8&0{,}4\end{pmatrix}.$$

Hatanın Frobenius normu $\sqrt{0{,}16+0{,}04+0{,}64+0{,}16}=1=d_2$ olur (Şekil [25](#abb-25)); spektral normu da öyle.

:::abbildung ml/k2rfehler 25
Rankı $1$ olan en iyi yaklaşımın Frobenius normundaki hatası, $0{,}4=\tfrac25$, $0{,}2=\tfrac15$ ve $0{,}8=\tfrac45$ ile: Karesi $d_2^2=1$ olur.
:::
::::

⁠**Kısacası:** $\mathbf{A}_k$ en büyük $k$ yapı taşını korur; hatanın tekil değerleri geri kalanlardır ve spektral normu $d_{k+1}$ olur.

### En iyi yaklaşım

<span class="anker" id="stufe-10-3"></span>

Rankı $k$ olan pek çok matris vardır. Kesilmiş ayrışım bunların en iyisi midir? Evet, iki normda da.

:::satz Teorem 10.4 (Eckart-Young teoremi)
<span class="anker" id="satz-10-4"></span>

$\mathbf{A}$ matrisinin rankı $r$ ve $k<r$ olsun. $\operatorname{rank}\mathbf{B}\le k$ olan, aynı boyutlardaki her $\mathbf{B}$ matrisi için şu geçerlidir:

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_2,\qquad \lVert\mathbf{A}-\mathbf{B}\rVert_F\ge\sqrt{d_{k+1}^2+\dots+d_r^2}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_F . \tag{10.4}$$

Demek ki rankı en fazla $k$ olan bütün matrisler arasında $\mathbf{A}$ matrisine en yakın olan $\mathbf{A}_k$ matrisidir.
:::

:::beweis Spektral norm
Rank-sıfırlık teoremine göre $\mathbf{B}$ matrisinin çekirdeğinin boyutu $n-\operatorname{rank}\mathbf{B}\ge n-k$ olur. Çekirdekte $n-k$ tane doğrusal bağımsız $\mathbf{b}_1,\dots,\mathbf{b}_{n-k}$ vektörü seçilir ve bunlara $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$ eklenir. Bunlar $\mathbb{R}^n$ uzayında $n+1$ vektördür ve [Bölüm 1, Kesim 13.4](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-4)'e göre doğrusal bağımlıdır, çünkü $n$ satırlı bir matrisin rankı en fazla $n$ olur. Dolayısıyla hepsi sıfır olmayan ve $\sum_l\alpha_l\mathbf{b}_l=\sum_j\beta_j\mathbf{v}_j$ eşitliğini sağlayan sayılar vardır. Bu $\mathbf{z}$ vektörü sıfır değildir, çünkü aksi halde iki listenin bağımsızlığı nedeniyle bütün sayılar sıfır olurdu. Vektör hem $\mathbf{B}$ matrisinin çekirdeğinde hem de $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$ vektörlerinin gerdiği alt uzaydadır. $1$ uzunluğuna normlanır. O zaman $(\mathbf{A}-\mathbf{B})\mathbf{z}=\mathbf{A}\mathbf{z}$ olur ve $\mathbf{z}=\sum_{j\le k+1}c_j\mathbf{v}_j$, $\sum_jc_j^2=1$ ile şu bulunur:

$$\lVert(\mathbf{A}-\mathbf{B})\mathbf{z}\rVert^2=\lVert\mathbf{A}\mathbf{z}\rVert^2=\sum_{j=1}^{k+1}d_j^2c_j^2\ge d_{k+1}^2\sum_{j=1}^{k+1}c_j^2=d_{k+1}^2 .$$

Demek ki $\mathbf{A}-\mathbf{B}$, $\mathbf{z}$ birim vektörünü en az $d_{k+1}$ katına uzatır ve $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}$ olur.
:::

İspat nedeni gösterir: Rankı $k$ olan bir matris koca bir doğrultular kümesini, yani çekirdeğini sıfıra götürmek zorundadır. Bu çekirdek, $\mathbf{A}$ matrisinin en çok uzattığı $k+1$ doğrultunun uzayıyla kaçınılmaz olarak kesişir ve $\mathbf{B}$ orada en az $d_{k+1}$ büyüklüğünde bir hata yapar.

::::beispiel [Sayısal örnek]
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ için rankı $1$ olan en iyi matris, iki normda da hatası $1$ olan $\mathbf{A}_1$ matrisidir. Rankı $1$ olan başka bir matrisin, örneğin ikinci satırı basitçe silen $\mathbf{B}=\bigl(\begin{smallmatrix}2&3\\0&0\end{smallmatrix}\bigr)$ matrisinin hatası $\mathbf{A}-\mathbf{B}=\bigl(\begin{smallmatrix}0&0\\0&2\end{smallmatrix}\bigr)$ olur, normu da $2$.
::::

⁠**Kısacası:** $\mathbf{A}_k$ kesilmiş ayrışımı, hem spektral normda hem Frobenius normunda rankı $k$ olan en iyi yaklaşımdır.

:::hintergrund Önerme Frobenius normu için de neden doğrudur
Frobenius normu için ispat, $\mathbf{A}$ matrisinin $\mathbf{a}^{(1)\top},\dots,\mathbf{a}^{(m)\top}$ satırlarını, bir veri matrisinin örnekleri gibi $\mathbb{R}^n$ uzayında $m$ nokta olarak görür. $\mathbf{B}$ matrisinin rankı en fazla $k$ ise satırları $k$ boyutlu bir $\mathcal S$ alt uzayında, yani $\mathbf{B}^{\top}$ matrisinin $k$ boyuta tamamlanmış sütun uzayında bulunur. İzdüşüm matrisi $\mathbf{P}$ olan sabit bir $\mathcal S$ alt uzayı için, Kesim [4](projektion-auf-einen-unterraum.html#stufe-4)'e göre her satırın $\mathbf{P}\mathbf{a}^{(i)}$ izdüşümü $\mathcal S$ içindeki en yakın noktadır. $\mathcal S$ alt uzayının bir $\mathbf{w}_1,\dots,\mathbf{w}_k$ ortonormal tabanıyla, Pisagor teoremine göre şu bulunur:

$$\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge\sum_i\bigl\lVert\mathbf{a}^{(i)}-\mathbf{P}\mathbf{a}^{(i)}\bigr\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_i\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2 ,$$

çünkü $\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\sum_l(\mathbf{w}_l^{\top}\mathbf{a}^{(i)})^2$ ve $\mathbf{w}_l^{\top}\mathbf{a}^{(i)}$, $\mathbf{A}\mathbf{w}_l$ vektörünün $i$ numaralı elemanıdır. Geriye $\sum_l\lVert\mathbf{A}\mathbf{w}_l\rVert^2\le d_1^2+\dots+d_k^2$ olduğunu göstermek kalır. $\mathbf{v}_j$ koordinatlarında şu geçerlidir:

$$\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2=\sum_{l=1}^k\sum_jd_j^2(\mathbf{v}_j^{\top}\mathbf{w}_l)^2=\sum_jd_j^2\,g_j\qquad\text{burada}\qquad g_j=\sum_{l=1}^k(\mathbf{v}_j^{\top}\mathbf{w}_l)^2 .$$

Her $g_j$, $\mathbf{v}_j$ vektörünün $\mathcal S$ üzerine izdüşümünün uzunluğunun karesidir; dolayısıyla $0\le g_j\le1$ olur ve bütün $g_j$ değerlerinin toplamı $\sum_l\lVert\mathbf{w}_l\rVert^2=k$ eder. Böyle ağırlıklarla bir $\sum_jd_j^2g_j$ toplamı, en büyük $k$ tane $d_j^2$ değeri tam ağırlık olan $1$ değerini aldığında en büyüktür; bu da $d_1^2+\dots+d_k^2$ eder. [(10.1)](#gl-10-1) ile birlikte $\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge d_{k+1}^2+\dots+d_r^2$ çıkar. Hesap yan ürün olarak şunu da gösterir: $\mathbf{A}$ matrisinin satırlarının en yakın olduğu alt uzay, $\mathbf{v}_1,\dots,\mathbf{v}_k$ vektörlerinin gerdiği alt uzaydır.
:::

### Birkaç sayıyla bir görüntü

<span class="anker" id="stufe-10-4"></span>

Gri tonlamalı bir görüntü bir matristir. Eckart-Young teoremine göre $\mathbf{A}_k$, $k$ yapı taşlı en iyi yaklaşımdır; [(10.3)](#gl-10-3) de ne kadarının kaybolduğunu söyler. Aşağıdaki oran

$$\frac{d_1^2+\dots+d_k^2}{d_1^2+\dots+d_r^2}$$

bütün parlaklık değerlerinin karelerinin toplamından hangi payın korunduğunu gösterir.

::::beispiel [Sayısal örnek]
[Bölüm 1, Kesim 6.1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1)'deki artı işareti şu matristir:

$$\mathbf{C}=\begin{pmatrix}0&1&0\\1&1&1\\0&1&0\end{pmatrix}.$$

Simetriktir. Karakteristik polinomu $-\lambda^3+\lambda^2+2\lambda=-\lambda(\lambda-2)(\lambda+1)$, özdeğerleri $2$, $-1$ ve $0$, özvektörleri de $(1,\,2,\,1)^{\top}$, $(1,\,-1,\,1)^{\top}$ ve $(1,\,0,\,-1)^{\top}$ olur. Kesim [9.7](die-singularwertzerlegung.html#stufe-9-7)'ye göre tekil değerler $2$, $1$ ve $0$; rank $2$ olur. $\mathbf{q}_1=(1,\,2,\,1)^{\top}/\sqrt6$ ile rankı $1$ olan en iyi yaklaşım şudur:

$$\mathbf{C}_1=2\,\mathbf{q}_1\mathbf{q}_1^{\top}=\frac13\begin{pmatrix}1&2&1\\2&4&2\\1&2&1\end{pmatrix},\qquad \mathbf{C}-\mathbf{C}_1=\frac13\begin{pmatrix}-1&1&-1\\1&-1&1\\-1&1&-1\end{pmatrix}$$

(Şekil [26](#abb-26)). Hata iki normda da $1$ büyüklüğündedir. $\mathbf{C}_1$, $\lVert\mathbf{C}\rVert_F^2=5$ toplamının $4/5=80\,\%$'ini korur. $\mathbf{C}_1$ matrisinin her satırı aynı $(1,\,2,\,1)$ satırının bir katıdır: Rankı $1$ olan bir görüntü, sütunların bir parlaklık profili çarpı satırların bir parlaklık profilidir; burada en parlak noktası ortada olan bulanık bir lekedir. $9$ yerine $1\cdot(3+3+1)=7$ sayının saklanması gerekir.

:::abbildung ml/k2bild 26
$3\times3$ pikselden oluşan $\mathbf{C}$ artı işareti (solda; $0$ siyah, $1$ beyaz), rankı $1$ olan en iyi yaklaşımı $\mathbf{C}_1$ (ortada; $\tfrac43$ değeri beyazdan daha parlaktır ve beyaz gösterilmiştir) ve $\mathbf{C}-\mathbf{C}_1$ hatası (sağda; kırmızı pozitif, mavi negatif). Hatanın kendisi de rankı $1$ olan bir matristir: $1$ tekil değerine ait yapı taşı.
:::
::::

$3\times3$ piksellik bir artı işaretinde bu pek tasarruf sağlamaz. Büyük görüntülerde fark önemlidir: $1000\times1000$ piksellik bir görüntünün $10^6$ elemanı vardır; $k=50$ yapı taşlı yaklaşım $50\cdot(1000+1000+1)=100\,050$ sayı, yani yaklaşık $10\,\%$ gerektirir. Yaklaşımın iyi görünüp görünmediği, tekil değerlerin ne kadar hızlı azaldığına bağlıdır. Pek çok fotoğrafta komşu satırlar birbirine çok benzer; satırlar o zaman küçük boyutlu bir alt uzaya yakın bulunur ve birkaç büyük tekil değer $\sum_jd_j^2$ toplamının neredeyse tamamını taşır.

⁠**Kısacası:** Rankı $k$ olan bir görüntü $k(m+n+1)$ sayı gerektirir; kesilmiş ayrışım bu türden en iyi görüntüdür ve $\sum_{j\le k}d_j^2/\sum_jd_j^2$ oranı ne kadarının korunduğunu söyler.

:::aufgabe Alıştırma 30 ★ Bir matrisin normları
<span class="anker" id="aufg-30"></span>

<ol class="al">

<li>

Alıştırma [27](die-singularwertzerlegung.html#aufg-27)'deki $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$ için $\lVert\mathbf{A}\rVert_F$ ve $\lVert\mathbf{A}\rVert_2$ değerlerini hesaplayın ve [(10.1)](#gl-10-1) bağıntısını doğrulayın.

</li>

<li>

$n\times n$ boyutlu ortogonal bir matrisin Frobenius normu nedir?

</li>

<li>

$\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F\le\sqrt r\,\lVert\mathbf{A}\rVert_2$ olduğunu gösterin. Sağdaki eşitlik ne zaman sağlanır?

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{A}\rVert_F^2=9+0+16+25=50=45+5=d_1^2+d_2^2$, dolayısıyla $\lVert\mathbf{A}\rVert_F=\sqrt{50}\approx7{,}07$ ve $\lVert\mathbf{A}\rVert_2=d_1=3\sqrt5\approx6{,}71$ olur.

(b) Ortogonal bir matrisin bütün tekil değerleri $1$ olur, dolayısıyla $\lVert\mathbf{Q}\rVert_F^2=n$ ve $\lVert\mathbf{Q}\rVert_F=\sqrt n$. Doğrudan da görülür: $n$ sütunun her birinin uzunluğunun karesi $1$ olur.

(c) $\lVert\mathbf{A}\rVert_2^2=d_1^2\le d_1^2+\dots+d_r^2=\lVert\mathbf{A}\rVert_F^2$ olur ve $r$ terimin her biri en fazla $d_1^2$ olduğundan $\lVert\mathbf{A}\rVert_F^2\le r\,d_1^2$. Karekök alınınca iki eşitsizlik de çıkar. Sağdaki eşitlik ancak ve ancak bütün pozitif tekil değerler $d_1$ değerine eşitse sağlanır; ortogonal bir matriste olduğu gibi.
:::
:::

:::aufgabe Alıştırma 31 ★★ Rankı 1 olan en iyi matris
<span class="anker" id="aufg-31"></span>

$\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$, Alıştırma [28](die-singularwertzerlegung.html#aufg-28)'deki matris olsun.

<ol class="al">

<li>

$\mathbf{A}_1$ matrisini ve $\mathbf{A}-\mathbf{A}_1$ hatasını iki normda da hesaplayın.

</li>

<li>

Bütün elemanları bir olan $\mathbf{B}$ matrisinin rankı da $1$ olur. $\lVert\mathbf{A}-\mathbf{B}\rVert_F$ ve $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ değerlerini hesaplayın ve (a) ile karşılaştırın.

</li>

<li>

Elemanların karelerinin toplamından ne kadarı $\mathbf{A}_1$ matrisinde korunur?

</li>

</ol>

:::loesung
(a) Alıştırma [28](die-singularwertzerlegung.html#aufg-28)'den: $d_1=2$, $\mathbf{u}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$. Dolayısıyla

$$\mathbf{A}_1=2\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1&1\\1&1\\0&0\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\begin{pmatrix}0&0\\0&0\\1&-1\end{pmatrix}.$$

Hatanın Frobenius normu $\sqrt{1+1}=\sqrt2=d_2$ olur. Hata $\mathbf{e}_3\,(1,\,-1)$ dış çarpımıdır; Alıştırma [29](die-singularwertzerlegung.html#aufg-29)'a göre tek tekil değeri $1\cdot\sqrt2$ olur ve spektral normu da $\sqrt2$.

(b) $\mathbf{A}-\mathbf{B}=\Bigl(\begin{smallmatrix}0&0\\0&0\\0&-2\end{smallmatrix}\Bigr)$ matrisinin büyüklüğü iki normda da $2>\sqrt2$ olur. Eckart-Young teoreminin gerektirdiği gibi $\mathbf{B}$, $\mathbf{A}$ matrisine $\mathbf{A}_1$ matrisinden daha uzaktır.

(c) $\lVert\mathbf{A}\rVert_F^2=6=4+2$ olur ve $\mathbf{A}_1$ bunun $d_1^2/(d_1^2+d_2^2)=\tfrac46=\tfrac23\approx67\,\%$'sini korur.
:::
:::

:::aufgabe Alıştırma 32 ★ Bellek gereksinimi
<span class="anker" id="aufg-32"></span>

Gri tonlamalı bir görüntü $600\times800$ pikselden oluşuyor.

<ol class="al">

<li>

$k=40$ yapı taşlı yaklaşım kaç sayı gerektirir? Bu, başlangıçtaki sayı miktarının ne kadarıdır?

</li>

<li>

Yaklaşım hangi $k$ değerinden başlayarak hiç bellek tasarrufu sağlamaz?

</li>

</ol>

:::loesung
(a) $600\cdot800=480\,000$ yerine $40\cdot(600+800+1)=40\cdot1\,401=56\,040$ sayı, yani yaklaşık $11{,}7\,\%$.

(b) Yaklaşım, $k\cdot1\,401<480\,000$ olduğu sürece, yani $k\le342$ için bellek tasarrufu sağlar, çünkü $342\cdot1\,401=479\,142$ ve $343\cdot1\,401=480\,543$. $k=343$ değerinden başlayarak yaklaşım görüntünün kendisinden daha çok sayı gerektirir. Rank en fazla $600$ olur; zaten $600$'den fazla yapı taşı yoktur.
:::
:::
