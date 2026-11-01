# Parametrically Compass geliştirme kuralları

- Salt okunur mevzuat okuyucusu ve kaynak MCP araçlarıdır. Model/parametre/IFC değişikliği eklemeyin.
- `lib/compass` ve `Compass.tab` IronPython 2.7.12 üzerinde çalışır. Python 3 sözdizimi ve bağımlılıklarını yalnız `scripts`, `tests`, `mcp_server` içinde tutun.
- Parametrically'nin diğer eklentilerine bağımlılık eklemeyin. Gömülü modülleri `compass` ad alanında tutun.
- `corpus-lock.json` ile sabitlenen dosyalar ana Markdown deposundan gelir. Yerel OCR düzeltmesiyle bunları sessizce değiştirmeyin. Düzeltmeyi ana kaynak deposuna kanıtıyla taşıyın, ardından yeni commit'e kontrollü geçin.
- Orijinal PDF/HTML arşivlerinin SHA-256 değerlerini ve kaynak geçmişini koruyun. `OCR_UNREVIEWED`, `TEYİT BEKLİYOR` ve `UNVERIFIED` durumlarını tam doğruluk gibi sunmayın.
- Dosya yollarını katalogla sınırlandırın. MCP yalnız stdio, salt okunur ve sınırlı/sayfalı yanıtlar sunar. Revit API çağrılarını MCP arka plan işçilerine taşımayın.
- Kullanıcı verisi WebView2 için `%LOCALAPPDATA%/ParametricallyCompass/WebView2` altındadır. İnternet, host object ve WebMessage erişimi gerekmez.
- Kaynak snapshot güncellendiğinde `python scripts/build_reader.py`, ardından `--check`, testler ve gerçek stdio MCP smoke kontrolünü çalıştırın.
- Native doğrulamayı Revit sürümü, pyRevit ve Python motoruyla kaydedin. CPython testleri gerçek ribbon/WPF/WebView2 kabulü değildir. Kanıt olmayan sürümleri doğrulandı diye işaretlemeyin.
- Son paketi açıp dosya listesi, CRC ve özetlerini kontrol edin. Paket/uzak kurulum kanıtı olmadan kurulabilir sürüm iddia etmeyin.
- Kaynak projede kullanıcıya ait değişiklikleri koruyun; bu bağımsız depo dışında dosya değiştirmeyin.
