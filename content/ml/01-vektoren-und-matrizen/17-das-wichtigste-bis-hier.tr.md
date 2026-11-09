---
title: Buraya kadarki temel noktalar
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / Vektörler ve Matrisler
knoten: Temeller 1: Vektörler ve Matrisler
nachschlagen: ja
order: 15211700
summary: Sayı listeleri olarak veriler, doğrusal dönüşümler olarak modeller
tags: 
lang: tr
---

:::kern Buraya kadarki temel noktalar
<ul>

<li>

$d$ öznitelikli bir örnek bir $\mathbf{x}\in\mathbb{R}^d$ sütun vektörüdür; $N$ örnekten oluşan bir veri kümesi, her satırında bir örnek bulunan $\mathbf{X}\in\mathbb{R}^{N\times d}$ veri matrisidir.

</li>

<li>

$\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ iç çarpımı hem bir ağırlıklı toplam hem de bir örüntü karşılaştırmasıdır; $\mathbf{w}^{\top}\mathbf{x}$ ağırlıklı toplamı, tek çıkışlı en genel doğrusal kuraldır.

</li>

<li>

Normlar büyüklüğü ölçer: $\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}$, $\lVert\mathbf{x}\rVert_1=\sum_j|x_j|$, $\lVert\mathbf{x}\rVert_\infty=\max_j|x_j|$; etkin değer $\lVert\mathbf{x}\rVert/\sqrt n$ olur. $\lVert\mathbf{u}-\mathbf{v}\rVert$ uzaklıkları birimlere bağlıdır, standartlaştırma onları birimlerden bağımsız kılar.

</li>

<li>

$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$; açı $\cos\varphi=\mathbf{u}^{\top}\mathbf{v}/(\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert)$ ile verilir, ortogonal $\mathbf{u}^{\top}\mathbf{v}=0$ demektir.

</li>

<li>

$\mathbf{A}\mathbf{x}$ hem bir iç çarpımlar listesi (satır bakışı) hem de sütunların bir doğrusal bileşimidir (sütun bakışı); $\mathbf{X}\mathbf{w}$ bütün tahminleri aynı anda verir.

</li>

<li>

Her doğrusal dönüşüm bir matristir, matrisin sütunları birim vektörlerin görüntüleridir; afin $\mathbf{A}\mathbf{x}+\mathbf{b}$ demektir.

</li>

<li>

$\mathbf{A}\mathbf{B}$ “önce $\mathbf{B}$, sonra $\mathbf{A}$” demektir; birleşme özelliği vardır, değişme özelliği yoktur; art arda doğrusal aşamalar tek bir matristir.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$; $\mathbf{X}\mathbf{X}^{\top}$ örneklerin bütün iç çarpımlarını, $\mathbf{X}^{\top}\mathbf{X}=\sum_i\mathbf{x}_i\mathbf{x}_i^{\top}$ ise özniteliklerinkileri içerir.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$; $\mathbf{A}\mathbf{x}=\mathbf{y}$ sisteminin ya hiç, ya bir ya da sonsuz sayıda çözümü vardır ve sistem ancak ve ancak $\mathbf{y}$ sütun uzayındaysa çözülebilir.

</li>

<li>

$\dim\ker\mathbf{A}+\operatorname{rank}\mathbf{A}=n$; $\mathbf{A}\mathbf{x}=\mathbf{y}$ ancak ve ancak $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rank}\mathbf{A}$ ise çözülebilir ve o zaman çözüm ancak ve ancak $\operatorname{rank}\mathbf{A}=n$ ise tektir; bağımlı öznitelikler rankı düşürür ve ağırlıkları tek türlü belirli olmaktan çıkarır.

</li>

<li>

$\det\mathbf{A}$ işaretli hacim çarpanıdır, $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$ ve $\mathbf{A}$ ancak ve ancak $\det\mathbf{A}\ne0$ ise tersinirdir.

</li>

<li>

$\odot$ eleman eleman çarpar; tensörler, eksen sayısı istenildiği kadar olabilen sayı dizileridir.

</li>

</ul>
:::

:::merke Üç cümlede cevap
<ol>

<li>

Bir veri kümesi, satırları örnekleri vektör olarak içeren bir matristir; benzerlik, uzaklık ve büyüklük de bu vektörlerin iç çarpımları ve normlarıdır ve seçilen birimlere bağlıdır.

</li>

<li>

Doğrusal bir kural birim vektörlerin görüntüleriyle belirlenir, yani bir matristir; matris-vektör çarpımı onu bütün örneklere aynı anda uygular.

</li>

<li>

Art arda uygulamak matrisleri çarpmaktır; bir dönüşümün tersine çevrilip çevrilemeyeceğine ise rank, çekirdek ve determinant karar verir: Bunlar, dönüşüm sırasında doğrultuların kaybolup kaybolmadığını gösterir.

</li>

</ol>
:::

**Tüm sonuçların ardındaki tek ilke.** Bu bölümdeki neredeyse her şey iki işlemden çıkar: Vektörler toplanır ve sayılarla çarpılır; doğrusal dönüşümler de tam olarak bu iki işlemi korur.

| Sonuç | Nereden geliyor |
|---|---|
| Ağırlıklı toplam, örüntü karşılaştırması | iç çarpım: aynı yerdeki çarpımlar, toplanmış (Kesim [2](das-skalarprodukt.html#stufe-2)) |
| Uzunluk, uzaklık, açı | hepsi iç çarpımdan: $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$, [(4.1)](abstande-und-einheiten.html#gl-4-1), Cauchy-Schwarz (Kesim [3](normen-die-groe-eines-vektors.html#stufe-3) ile [5](winkel-und-ahnlichkeit.html#stufe-5) arası) |
| Uzaklıklar birimlere bağlıdır | her öznitelik, sayısal değerinin karesiyle katılır (Kesim [4](abstande-und-einheiten.html#stufe-4)) |
| Satır bakışı ve sütun bakışı | aynı çift toplam, farklı sıralanmış (Kesim [7](das-matrix-vektor-produkt.html#stufe-7)) |
| Bir doğrusal dönüşümün matrisi | $\mathbf{x}=\sum_jx_j\mathbf{e}_j$ ve dönüşüm doğrusal bileşimleri korur (Kesim [8](lineare-abbildungen.html#stufe-8)) |
| Matris çarpımı, değişme özelliği yok | bileşkenin matrisi (Kesim [9](das-matrixprodukt.html#stufe-9)) |
| Gram matrisi | iç çarpımların tablosu, $\mathbf{X}\mathbf{X}^{\top}$ ve $\mathbf{X}^{\top}\mathbf{X}$ (Kesim [10](transponierte-symmetrie-und-gram-matrix.html#stufe-10)) |
| $\mathbf{A}\mathbf{x}=\mathbf{0}$, $\mathbf{x}\ne\mathbf{0}$ ise ters yok | iki giriş, bir çıkış: bilgi kaybolmuş (Kesim [11](einheitsmatrix-und-inverse.html#stufe-11)) |
| Hiç, bir, sonsuz sayıda çözüm | iki çözüm varsa onlardan geçen doğrunun tamamı çözümdür (Kesim [12](lineare-gleichungssysteme.html#stufe-12)) |
| Tek türlü belirli olmayan ağırlıklar | çekirdekteki vektörler $\mathbf{X}\mathbf{w}$ çarpımını değiştirmez (Kesim [13](unabhangigkeit-basis-und-rang.html#stufe-13)) |
| $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$ | art arda uygulamada hacim çarpanları çarpılır (Kesim [14](die-determinante.html#stufe-14)) |
