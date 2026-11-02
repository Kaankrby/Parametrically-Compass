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
| GitHub'dan pyRevit CLI kurulumu | Varsayılan Extensions dizinine temiz klon; 11 belge ve bütün manifest varlıkları Git blob özetleriyle eşleşti; CLI türü `UIExtension` |
| Kurulan kopyada native gezinme | 11 belge, 177 kaynak tablo, 9.614 hücre ve 11 SVG; aramada 13 sonuç ve tema değişimi geçti |
| Ribbon kaydı ve kullanıcı kabulü | Reload sonrası `Compass` görünür; bir panel ve bağımsız `Kitaplık` komutu kayıtlı. 02.11.2026 tarihinde kullanıcı gerçek düğmeden açılışı “Kitaplık açıldı” yanıtıyla teyit etti |
| ZIP | CRC/dosya listesi/SHA-256 kontrolü, diske çıkarılmış kopyadan corpus API ve gerçek stdio MCP istemcisi geçti |
| GitHub CI | Ubuntu / Python 3.12: Ruff, build güncelliği, 15 test, gerçek MCP stdio, ZIP ve diff kontrolleri geçti |

Sunucu yalnız paketlenmiş metni okur; modeli ve IFC'yi okumaz/değiştirmez. İnceleme geçmişi, konsolide güncellik, bütün OCR karakterleri, hukuki yorum ve proje uygunluğu tam doğrulanmış değildir.

Native kayıtlar: WPF/API `ed0efa620efd`; WebView2 `18c16b6f8e5a`. WebView2 testinde web mesajları, host object ve devtools erişimi kapalıydı; pencere kapandığında olay işleyicileri ve içerik bırakıldı. Modelin değişiklik durumu değişmedi. İlk WebView2 testinin sonuç aktarımı karakter kodlaması nedeniyle hata verdi; ASCII alanlarla yinelenen test geçti. Bu sonuç Revit 2024/2025 veya tüm kullanıcı etkileşimlerini doğrulamaz.

Kurulmuş kopyanın gezinme testi `2ca54e712843`, ribbon kaydı `455a5f3dd65c`. [Makinece okunabilir kanıt özeti](validation-evidence.json). Reload ve okuyucu testleri sırasında mevcut modelin değişiklik durumu korundu; modelde işlem veya kayıt yapılmadı.
