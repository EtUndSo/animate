---
title: Genel Bakış: İzdüşüm, Özdeğerler ve Ayrışımlar
kurz: Genel Bakış
pfad: Bilgisayar Bilimleri / Makine Öğrenmesi / Matematiksel Temeller / İzdüşüm, Özdeğerler ve Ayrışımlar
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Bölüm 2: İzdüşüm, Özdeğerler ve Ayrışımlar
nachschlagen: ja
order: 15220100
summary: En yakın noktalar, doğal doğrultular ve bir matrisin yapı taşları
tags: 
lang: tr
---

## Konunun özü

[Bölüm 1](/wissen/tr/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)'de bir soru açık kalmıştı. Dört daire alanları ve oda sayılarıyla betimleniyor ve fiyatları biliniyor. Aranan, ağırlıklı toplamın her fiyatı tam olarak tutturmasını sağlayan iki ağırlıktır. Böyle ağırlıklar yoktur: İki bilinmeyenli dört denklem birbiriyle çelişir. Ölçüm verilerinde durum neredeyse her zaman böyledir. Bilinmeyenlerden daha çok ölçüm vardır, her ölçüm biraz kusurludur ve denklem sisteminin çözümü yoktur. Yine de ağırlıklara ihtiyaç vardır, hem de hedeften olabildiğince az sapanlara.

Bu bölüm bu soruyu ve onunla yakından akraba olduğu ortaya çıkan iki soruyu daha ele alıyor. Bir matrisin bir oku döndürmeden yalnızca uzattığı ya da kısalttığı doğrultular var mıdır ve bu doğrultular matris hakkında ne söyler? Her matris, önem sırasına dizilmiş birkaç basit yapı taşına ayrılabilir mi, öyle ki önemsiz olanlar atılabilsin? Buna pratik bir soru eklenir: Veriler biraz hatalıysa bir hesabın sonucu ne kadar değişir?

Yararı şu: Bu cevaplar sayesinde ölçüm değerlerine bir doğruyu ya da başka basit bir kuralı, hata olabildiğince küçük kalacak biçimde uydurabilirsiniz. Çok değişkenli bir fonksiyonun bir çukuru, bir sırtı ya da bir eyeri olup olmadığını anlayabilirsiniz. Bir görüntüyü ya da büyük bir tabloyu birkaç sayıyla yaklaşık olarak ifade edebilir ve bu sırada ne kadar bilginin kaybolduğunu bilebilirsiniz. Ayrıca bir hesap sonucuna güvenip güvenemeyeceğinizi değerlendirebilirsiniz. Bu bölümün araçları serinin sonraki kısımlarının neredeyse hepsinde yeniden karşınıza çıkacak.

**Bu bölümle nasıl çalışılır?** Konular birbirinin üzerine kurulur ve her yeni kavramın örnek içeren kendi alt başlığı vardır. Açılır kutular arka plan bilgisini (bir yöntemin neden işe yaradığını ve nereden geldiğini), türetmeleri ve ispatları içerir; okumaya devam etmek için bunlara gerek yoktur. Alıştırmaları (★ ile ★★★ arası) önce kendiniz çözmeye çalışın ve programları gerçekten çalıştırın; çözümü her alıştırmanın hemen altında açabilirsiniz.
