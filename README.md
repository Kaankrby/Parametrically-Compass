# Parametrically Compass

**pyRevit için bağımsız, çevrimdışı mevzuat okuyucusu ve ajanlar için salt okunur MCP kaynak araçları.**

Yönetmelik ana metni ve EK-1–EK-9'u Revit içinde okuyun, arayın, tabloları ve SVG şekillerini inceleyin. Gerektiğinde arşiv PDF ile karşılaştırın. Parametrically'nin diğer eklentileri gerekmez. Okuyucu bir Revit belgesi açık değilken de çalışacak şekilde tasarlanmıştır; model veya IFC verisi değiştirmez.

> İlk sürüm: **0.1.0 beta**. Kaynaklar yayımlanma nüshası ve OCR aktarımıdır; konsolide güncel mevzuat veya hukuki uygunluk onayı değildir. **TEYİT BEKLİYOR** durumları korunur. [Doğrulama kapsamı](docs/VALIDATION.md).

## Kurulum

Önce [pyRevit](https://github.com/pyrevitlabs/pyRevit) kurulu olmalıdır. Bu sürümün hedefi Revit 2024–2026, pyRevit 7 ve IronPython 2.7.12'dir. Sürüm bazındaki gerçek test durumu [doğrulama belgesindedir](docs/VALIDATION.md).

### GitHub'dan pyRevit CLI ile

```powershell
pyrevit extend ui ParametricallyCompass https://github.com/Kaankrby/Parametrically-Compass.git --branch=main
```

Revit'i yeniden başlatın veya açık pyRevit araçlarınızı kapattıktan sonra **pyRevit → Reload** kullanın. Ardından **Compass → Mevzuat → Kitaplık** düğmesini açın. `pyrevit` PATH üzerinde değilse kurulu sürümünüzün `bin/pyrevit.exe` dosyasını tam yoluyla çalıştırın.

### ZIP ile

[Releases](https://github.com/Kaankrby/Parametrically-Compass/releases) sayfasından `ParametricallyCompass-0.1.0.zip` indirin. İçindeki **ParametricallyCompass.extension** klasörünü, başka bir klasör içine gömmeden şu dizine çıkartın:

```text
%APPDATA%\pyRevit\Extensions\ParametricallyCompass.extension\
  extension.json
  Compass.tab\
  lib\
```

Sürümün `.zip.sha256` dosyası arşiv özetini içerir. Okuyucu kullanımında Python 3, pip, npm veya ağ bağlantısı gerekmez. WebView2 çalışma ortamı yüklenemezse WPF metin görünümü devreye girer. **Shift+tıklama** WPF görünümünü doğrudan açar.

Bu proje henüz pyRevit'in resmî Extensions kataloğuna dahil değildir. Doğrudan CLI/ZIP kurulumu kullanılabilir. [Resmî eklenti yapısı](https://github.com/pyrevitlabs/pyRevit/blob/develop/docs/extensions.md).

## Okuma

- Belge dizini ve madde/tablo içindekileri.
- Bütün belgelerde Türkçe arama; Ctrl+K veya /.
- Açık/koyu tema, yazı boyutu ve yazdırma.
- HTML tablolarında birleşik hücreler; 11 SVG şekli.
- EK-1–EK-9 için özgün 241 sayfalık PDF'ye isteğe bağlı geçiş.

WPF geri dönüşünde tablolar satır ve sütun ayırıcılarıyla düzleştirilir. Birleşik hücrelerin anlamı için web görünümü veya özgün PDF kullanılmalıdır.

## MCP ile kullanım

İki erişim yolu vardır; ikisi de aynı paketlenmiş kaynakları okur:

1. **Mevcut pyRevit MCP:** Revit içindeki ajan, `compass.library` üzerinden belge/arama/tablo işlevlerini çağırabilir. Ek bir MCP sunucusu gerekmez.
2. **Bağımsız stdio MCP:** Python 3.10+ ve resmî MCP SDK ile Revit kapalıyken de kaynak sorgulama yapılabilir. Revit modeline veya dosyalarına erişim sunmaz.

[Kurulum, örnek istemci ayarı ve pyRevit MCP betiği](docs/MCP.md).

Araçlar: `compass_source_status`, `compass_list_documents`, `compass_read_document`, `compass_search`, `compass_read_table`. Yanıtlar kaynak commit'ini ve inceleme sınırlarını taşır. Dosya kimlikleri katalogla sınırlıdır; satır/hücre okumaları sayfalıdır. MCP istemcisi ayrıca kurulup bağlanmalıdır; pyRevit eklentisini kurmak istemcinizin MCP ayarlarını otomatik değiştirmez.

## Kaynak ve lisans

Ana kaynak deposu: [dijital-proje-yonetmeligi](https://github.com/Kaankrby/dijital-proje-yonetmeligi). Bu paket `corpus-lock.json` içinde sabitlenen commit'in 26 dosyasını baytları korunarak taşır; otomatik eşitleme veya mevzuat güncelleme hizmeti yoktur.

Özgün araçlar MIT lisanslıdır. Resmî kaynak metinleri ve üçüncü taraf standartları için [NOTICES.md](NOTICES.md) geçerlidir. [Katkı rehberi](CONTRIBUTING.md) ve [ajan talimatları](AGENTS.md).

## Geliştirme

```powershell
python scripts/build_reader.py --check
python -m pip install -r requirements-mcp.txt pytest pyyaml
python -m pytest tests -q
python scripts/test_mcp.py
python scripts/package_release.py
```

Gömülü `lib/compass` ve `Compass.tab` kodları IronPython 2.7 uyumludur. `scripts/`, `tests/` ve `mcp_server/` ayrı CPython geliştirme/ajan ortamıdır. MCP SDK 1.x bakım hattı `<2` ile sınırlandırılmıştır; test edilen SDK sürümü doğrulama belgesinde kayıtlıdır.

Kaldırmak için Revit kapalıyken yalnız `ParametricallyCompass.extension` klasörünü kaldırın. Diğer Parametrically eklentileri bağımsızdır.
