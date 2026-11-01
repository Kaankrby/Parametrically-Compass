# Doğrulama kapsamı — 0.1.0 beta

Bu belge ilk sürümün doğrulama kanıtlarını ve kabul sınırlarını izler. Başarılı kaynak testleri tam mevzuat uygunluğu veya tüm Revit sürümlerinde kabul değildir.

| Alan | Durum |
| --- | --- |
| Kaynak snapshot | `f1b8e50f1c33cd7b93bcc6b908532970844323d1`; 26 upstream dosya baytlarıyla korunur |
| Çevrimdışı kaynak/API testleri | 15 test geçti; büyük EK-6 satır sayfalaması, Türkçe arama, tablo koordinatları, yol sınırları ve değişmiş dosya reddi |
| Gerçek MCP stdio | SDK 1.30.0; handshake, beş araç, kaynaklar ve geçersiz kimlik reddi geçti |
| IronPython derleme | 2.7.12.0: üç kitaplık modülü ve bir düğme betiği, sıfır hata |
| Revit 2026 / pyRevit 7 native | Revit 26.4.10.51, pyRevit 7.0.0.26278+2233, IronPython 2.7.12: bağımsız API ve pencere yaşam döngüsü geçti |
| WebView2 ve WPF | WebView2 yerel sayfada 11 belgeyi yükledi; ofis koleksiyonu yok. WPF EK-6 metni/tablo ayırıcıları ve kapanış temizliği geçti. Tam kullanıcı kabulü ayrı izlenir |
| Revit 2024 ve 2025 | Test edilmedi |
| Açık belge olmadan ribbon düğmesi | Metadata `zero-doc`; canlı kabul TEYİT BEKLİYOR |
| ZIP ve uzak kurulum | TEYİT BEKLİYOR |

Sunucu yalnız paketlenmiş metni okur; modeli ve IFC'yi okumaz/değiştirmez. İnceleme geçmişi, konsolide güncellik, bütün OCR karakterleri, hukuki yorum ve proje uygunluğu tam doğrulanmış değildir.

Native kayıtlar: WPF/API `ed0efa620efd`; WebView2 `18c16b6f8e5a`. WebView2 testinde web mesajları, host object ve devtools erişimi kapalıydı; pencere kapandığında olay işleyicileri ve içerik bırakıldı. Modelin değişiklik durumu değişmedi. İlk WebView2 testinin sonuç aktarımı karakter kodlaması nedeniyle hata verdi; ASCII alanlarla yinelenen test geçti. Bu sonuç Revit 2024/2025 veya tüm kullanıcı etkileşimlerini doğrulamaz.
