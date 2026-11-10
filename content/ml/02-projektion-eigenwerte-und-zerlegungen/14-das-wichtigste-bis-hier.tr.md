---
title: Buraya kadarki temel noktalar
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Bölüm 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15221400
summary: En yakın noktalar, doğal doğrultular ve bir matrisin yapı taşları
tags: 
lang: tr
---

:::kern Buraya kadarki temel noktalar
<ul>

<li>

Ortonormal vektörler: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$; koordinatlar $c_i=\mathbf{q}_i^{\top}\mathbf{x}$ iç çarpımlarıdır; ortogonal matrisler uzunlukları ve açıları korur. $\mathbf{Q}$ kare değilse $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$ olur.

</li>

<li>

Bir doğru üzerine izdüşüm: $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$; kalan $\mathbf{a}$ vektörüne diktir ve $\hat{\mathbf{y}}$ en yakın noktadır. İzdüşüm matrisleri $\mathbf{P}^2=\mathbf{P}$ koşulunu, dik olanlar ayrıca $\mathbf{P}^{\top}=\mathbf{P}$ koşulunu sağlar.

</li>

<li>

En iyi yaklaşık çözüm: $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}$ artığı sütun uzayına diktir, dolayısıyla $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$; çözüm ancak ve ancak sütunlar bağımsızsa tektir.

</li>

<li>

Bir alt uzay üzerine izdüşüm: $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{Q}\mathbf{Q}^{\top}$; Gram-Schmidt $\mathbf{A}=\mathbf{Q}\mathbf{R}$ verir ve $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$.

</li>

<li>

$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ kuadratik formları yalnızca simetrik kısma bağlıdır; çanak, oluk ve eyer tam kareye tamamlamayla anlaşılır.

</li>

<li>

Özdeğerler: $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, $\det(\mathbf{A}-\lambda\mathbf{I})=0$; iz $=\sum\lambda_i$, $\det=\prod\lambda_i$; dönmelerin karmaşık özdeğerleri vardır.

</li>

<li>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ ayrıştırır, $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$. Simetrik: gerçel $\lambda_i$ ve birbirine dik asal eksenlerle $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$, yarı eksenler $1/\sqrt{\lambda_i}$.

</li>

<li>

Pozitif tanımlı $\Leftrightarrow$ bütün özdeğerler $>0$ $\Leftrightarrow$ bütün pivotlar $>0$ $\Leftrightarrow$ bütün baş asal minörler $>0$; $\mathbf{A}^{\top}\mathbf{A}$ pozitif yarı tanımlıdır; Cholesky $\mathbf{A}=\mathbf L\mathbf L^{\top}$.

</li>

<li>

Her matris için tekil değer ayrışımı $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$: döndürme, germe, döndürme; $d_j^2$ değerleri $\mathbf{A}^{\top}\mathbf{A}$ matrisinin özdeğerleridir, $\lVert\mathbf{A}\rVert_2=d_1$.

</li>

<li>

$\lVert\mathbf{A}\rVert_F^2=\sum_jd_j^2$; $\mathbf{A}_k$, rankı $k$ olan en iyi yaklaşımdır ve spektral normdaki hatası $d_{k+1}$ olur.

</li>

<li>

$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ en kısa en iyi yaklaşık çözümü verir; özel durumlar $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ ve $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$.

</li>

<li>

$\kappa(\mathbf{A})=d_1/d_n$ göreli hataların büyütülmesini sınırlar; $1/\kappa$, tekilliğe olan göreli uzaklıktır; $\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2$.

</li>

</ul>
:::

:::merke Üç cümlede cevap
<ol>

<li>

Çözümü olmayan bir denklem sistemi en iyi, sağ taraf sütun uzayı üzerine dik olarak izdüşürülerek çözülür: Artık vektörü o zaman bütün sütunlara diktir, buradan normal denklemler çıkar ve Pisagor teoremine göre daha yakın başka bir nokta yoktur.

</li>

<li>

Özvektörler, bir matrisin yalnızca uzattığı doğrultulardır; bunların tabanında matris köşegen olur ve simetrik matrislerde dik bir eksen takımı oluştururlar; her kuadratik formun biçimi bu eksen takımından okunur.

</li>

<li>

Her matris, rankı $1$ olan ve büyüklüğe göre sıralanmış $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ yapı taşlarının toplamıdır: İlk $k$ tanesi rankı $k$ olan en iyi yaklaşımı verir; $d_1/d_n$ oranı da verilerdeki hataların çözümü ne kadar bozabileceğini söyler.

</li>

</ol>
:::

**Tüm sonuçların ardındaki tek ilke.** Bu bölümdeki neredeyse her şey tek bir ilkeden çıkar: Dik bir eksen takımında bir uzunluk karesi Pisagor teoremine göre bağımsız paylara ayrılır ve bir doğruya, bir düzleme ya da bir alt uzaya giden en kısa yol dik olan yoldur.

| Sonuç | Nereden geliyor |
|---|---|
| İç çarpım olarak koordinatlar, $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ | $1$ uzunluğunda dik eksenler: karma terimler düşer (Kesim [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1)) |
| Doğru ve alt uzay üzerinde en yakın nokta | Pisagor: dik kalan artı alt uzay içinde kaydırma (Kesim [2](projektion-auf-eine-gerade.html#stufe-2) ve [3](die-beste-naherungslosung.html#stufe-3)) |
| Normal denklemler | artık vektörü her sütuna dik: $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ (Kesim [3](die-beste-naherungslosung.html#stufe-3)) |
| Gram-Schmidt ve QR | gölgeyi çıkarmak, dik kalanı normlamak (Kesim [4](projektion-auf-einen-unterraum.html#stufe-4)) |
| Çanak, oluk, eyer | bir kareler toplamındaki katsayıların işaretleri (Kesim [5](quadratische-formen.html#stufe-5) ve [8](positiv-definite-matrizen.html#stufe-8)) |
| Köşegenleştirerek ayrıştırma | öz tabanda her koordinat kendi başına etki eder (Kesim [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Spektral teorem | simetri: $\mathbf{A}$ iç çarpımda taraf değiştirebilir, bir özvektörün tümleyeni korunur (Kesim [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Her matrisin tekil değer ayrışımı | simetrik $\mathbf{A}^{\top}\mathbf{A}$ matrisi için spektral teorem (Kesim [9](die-singularwertzerlegung.html#stufe-9)) |
| Rankı $k$ olan en iyi yaklaşım | rankı $k$ olan bir matrisin çekirdeği, en çok uzatılan $k+1$ doğrultuyla kesişir (Kesim [10](naherung-durch-matrizen-von-kleinem-rang.html#stufe-10)) |
| En kısa en iyi yaklaşık çözüm | tekil vektörlerin koordinatlarında Pisagor: çekirdekteki paylar yalnızca uzunluğu artırır (Kesim [11](die-pseudoinverse.html#stufe-11)) |
| Koşul sayısı | en büyük ve en küçük uzatma, $d_1$ ve $d_n$ (Kesim [12](die-konditionszahl.html#stufe-12)) |
