# 🤖 Otonom Matematik Botu

Bu proje, GitHub Issue'ları üzerinden çalışan, tamamen sunucusuz (serverless) bir hesap makinesi platformudur[cite: 12].

## 🚀 Nasıl Kullanılır?
Sistemi test etmek için herhangi bir kurulum yapmanıza gerek yoktur:

1. Deponun **Issues** sekmesine gidin[cite: 12].
2. **New Issue** butonuna tıklayın[cite: 12].
3. Başlık (Title) kısmına şu formatta komutunuzu yazın: `işlem: sayı1, sayı2`[cite: 12].
4. Bot saniyeler içinde hesaplamayı yapıp sonucu yorum olarak yazacak ve konuyu kapatacaktır[cite: 12].

## 🛠️ Desteklenen Komutlar
Aşağıdaki formatları kullanarak işlem yapabilirsiniz:
* **Toplama:** `topla: 10, 20`[cite: 8, 12]
* **Çıkarma:** `cikar: 50, 10`[cite: 8, 12]
* **Çarpma:** `carp: 5, 4`[cite: 8, 12]
* **Bölme:** `bol: 100, 2`[cite: 8, 12]

## 🏗️ Güvenli Mimari (CI/CD)
* **Kalite Kontrol:** `main` dalına gelen her kod otomatik olarak test edilir[cite: 9, 11].
* **Otomatik Dağıtım:** Sadece testleri geçen sağlam kodlar `stable` dalına aktarılır[cite: 10].
* **Kesintisiz Hizmet:** Bot, her zaman en son çalışan ve onaylanmış olan `stable` dalındaki kodu kullanır[cite: 10, 12].