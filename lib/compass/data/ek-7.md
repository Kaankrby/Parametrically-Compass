# EK-7 — Proje ile ilgili IFC sınıflarının öznitelik tanımları

> Düzenlenebilir metin ve HTML tablolar. OCR yazımları ile hücre birleştirmeleri otomatik aktarılmıştır; TEYİT BEKLİYOR. Tablolar resim değildir. Grafikler varsa ayrı düzenlenebilir SVG vektörleridir. Bu aktarım hukuki doğrulama veya uygulama kapsamı onayı değildir.

Kaynak: RG 05.08.2026 / 33331.

EK-7 PROJE İLE İLGİLİ IFC SINIFLARININ ÖZNİTELİK TANIMLARI

7.1- BIM modelinde projeye ait bilgilerin temsilinde kullanılacak zorunlu IFC sınıfları Tablo 7.1 ile Tablo 7.12 arasında verilmiştir.

7.1.1- Tablo 7.1 ile Tablo 7.12 arasında yer alan IFC sınıfları, IFC 4.3 versiyonu esas alınarak düzenlenmiştir

7.1.2- Zorunlu IFC sınıflarında yer alması gereken zorunlu öznitelikler ve özellikler Tablo 7.1 ile Tablo 7.9 arasında yer alan tablolarda verilmiştir.

7.1.3- Zorunlu IFC sınıflarında yer alması isteğe bağlı olan öznitelikler ve özellikler Tablo 7.10, Tablo 7.11 ve Tablo 7.12 tablolarında referans olarak verilmiştir ve ilgili idaresince talep edilmesi halinde ilgili IFC sınıfında yer alır.

7.2- Projeye ait temel bilgiler zorunlu “lfeProject” sınıfında tanımlanır. Bu sınıfa ait zorunlu öznitelikler ve özellikler Tablo 7.1’de verilmiştir.

7.2.1- Her bir disiplin modelinin “IfeProject” sınıfının ortak öznitelikleri aynı olmalıdır.

7.3- IfeProject sınıfı içerisinde tariflenen JfePerson sınıfı zorunlu öznitelik listesi Tablo 7.2'de, IfcPersonAndOrganization sınıfı zorunlu öznitelik listesi Tablo 7.3°te, IfcOrganization sınıfı zorunlu öznitelik listesi Tablo 7.4”te ve IfcActorRole sınıfı zorunlu öznitelik listesi Tablo 7.5'te verilmiştir.

7.4- lfeProjectedCRS, IfcMapConversion, | IfeGeometricRepresentationContexi o ve IfcAnnotation sınıflarının zorunlu öznitelik listesi sırasıyla Tablo 7.6, Tablo 7.7 ve Tablo 7.8 ve Tablo 7.9'da verilmiştir.

## Tablo 7.1 IfcProject Simfi Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Proje (IfcProject)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: IfeProject”in bir veri alışverişi yapısındaki temel amacı, tüm diğer bilgi öğeleri için kök örneği (root instance) ve bağlamı (context) sağlamaktır.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-1*e göre isimlendirilecektir)</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Proje Tipi</td>
<td>ProjectType</td>
<td>Pset_ProjectCommon</td>
<td>Metin</td>
<td>Bir projenin ek tip tanımlaması</td>
</tr>
<tr>
<td></td>
<td colspan="4"></td>
</tr>
</tbody>
</table>

## Tablo 7.2 IfePerson Sınıfı Zorunlu Öznitelik ve Özellik Listesi (IfcProject içerisinde tariflenir)

<table>
<tbody>
<tr>
<td colspan="4">Kişi (AfcPerson)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bu varlık, bir bireyi temsil eder. NOT: Birçok ülkede, veri tabanlarında kişilerin tanımlanmasına ilişkin yasal düzenlemeler bulunmaktadır. IFC Modeli&#x27;nin amacı veri değişimi ve paylaşımı için bir tanımlama standardı olarak hizmet etmek olsa da bazı durumlarda bir IFC dosyası bu tür mevzuatlar kapsamında belirli bir kişiyi tanımlamaya olanak sağlayan bir veri tabanı olarak kabul edilebilir. Kullanıcılar, IFC dosyalarının kullanıldığı yerlerde geçerli olabilecek yasal kısıtlamaların farkında olmalıdır.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama .</th>
</tr>
<tr>
<td>Kimlik No</td>
<td>Attribute: Identification</td>
<td>-</td>
<td>Metin</td>
<td>(Oda Sicil numarası). Kişinin tanımlanması.</td>
</tr>
<tr>
<td>Aile Adı</td>
<td>Attribute: FamilyName</td>
<td>-</td>
<td>Metin</td>
<td>Kişinin (oOoaille (kimliğinin Oo tanınmasını Oo sağlayan (addır. NOT: Coğrafi konuma ve kültüre bağlı olarak, soyad bir ismin ilk veya son kısmında yer alabilir.</td>
</tr>
<tr>
<td>Ad</td>
<td>Attribute: GivenName</td>
<td>-</td>
<td>Metin</td>
<td>Kişinin aile (oiçinde O bilindiği ve O tanındığı addır. NOT: Coğrafi konuma ve kültüre bağlı olarak, ad bir ismin ilk veya son kısmında yer alabilir.</td>
</tr>
<tr>
<td>Rol</td>
<td>Attribute: Roles</td>
<td>-</td>
<td>Metin</td>
<td>Kişinin üstlendiği roller.</td>
</tr>
</tbody>
</table>

|

## Tablo 7.3 IfcPersonAndOrganization Sınıfı Zorunlu Öznitelik ve Özellik Listesi (IfcProject içerisinde tariflenir)

<table>
<tbody>
<tr>
<td colspan="4">Kişi ve Organizasyon (IfePersonAndOrganization)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Bu varlık, bir kuruluş adına hareket eden bir kişiyi Otemsii (eder. NOT: Bu varlık, ISO 10303-41&#x27;de tanımlanan person and organization kavramından uyarlanmıştır.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Kişi</td>
<td>Attribute: ThePerson</td>
<td>-</td>
<td>Metin</td>
<td>Kuruluş ile ilişkili olan kişi.</td>
</tr>
<tr>
<td>Organizasyon</td>
<td>Attribute: TheOrganization</td>
<td>-</td>
<td>Metin</td>
<td>Kişinin ilişkili olduğu kuruluş.</td>
</tr>
</tbody>
</table>

## Tablo 7.4 IfcOrganization Sınıfı Zorunlu Öznitelik ve Özellik Listesi (IfcProject içerisinde tariflenir)

<table>
<tbody>
<tr>
<td colspan="4">Organizasyon (IfcOrganization)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kurumsal bir kimliğe sahip, adlandırılmış ve yapılandırılmış bir gruplamadır. NOT: Bir şirket içindeki departmanlar arasındaki ilişkilerde olduğu gibi, IfcOrganization varlıkları arasındaki ilişkiler, nesneleştirilmiş ilişki olan 1fcOrganizationRelationship aracılığıyla ifade edilebilir.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Firma Vergi No</td>
<td>Attribute: Identification</td>
<td>-</td>
<td>Sayı</td>
<td>Kuruluşun tanımlanması (Vergi Kimlik Numarası).</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (fcRootll sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir.</td>
</tr>
<tr>
<td rowspan="2">Rol Adres</td>
<td>Attribute:Roles &gt; ifcActorRole</td>
<td>-</td>
<td>Metin</td>
<td>Kuruluşun üstlendiği roller.</td>
</tr>
<tr>
<td>Attribute: Addresses &gt; ifePostalA.ddress, ifcTelecomAddress</td>
<td>-</td>
<td>Metin</td>
<td>Bir (okuruluşun (Oo posta Ove telekomünikasyon (o adresleri. NOT: Bir kuruluşa ait birden fazla adres bulunabilir.</td>
</tr>
</tbody>
</table>

## Tablo 7.5 IfcActorRole Sınıfı Zorunlu Öznitelik Listesi (1fcProject içerisinde tariflenir)

<table>
<tbody>
<tr>
<td colspan="4">Rol (IfcActorRole)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kurumsal kimliğe sahip, adlandırılmış ve yapılandırılmış bir gruplama. NOT: IfcOrganization&#x27;lar arasındaki ilişkiler (örneğin bir şirket içindeki departmanlar arasındaki ilişkiler), nesneleştirilmiş ilişki IfcOrganizationRelationship kullanılarak ifade edilebilir.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Rol</td>
<td>Attribute: Role</td>
<td>-</td>
<td>Metin</td>
<td>Bir aktörün üstlendiği rolün adıdır. Eğer Rol değeri USERDEFİNED ise, kullanıcı tarafından tanımlanan rol, UserDefinedRole özniteliğinin değeri olarak verilmelidir.</td>
</tr>
<tr>
<td>Kullanıcı Tanımlı Rol</td>
<td>Attribute: UserDefinedRole</td>
<td>-</td>
<td>Metin</td>
<td>IfcRoleEnum türündeki Role özniteliğinde tanımlanan listelenmiş değerlerin ötesinde, kullanıcı tanımlı rollerin belirtilmesine izin verir. UserDefinedRole özniteliğine bir değer verildiğinde, Role özniteliğinin numaralandırılmış değeri USERDEFINED olmalıdır.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>,Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
</tbody>
</table>

## Tablo 7.6 IfeProjectedCRS Sınıfı Zorunlu Öznitelik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Yansıtılmış Koordinat Referans Sistemi (IfceProjectedCRS)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: IfeProjectedCRS, bir inşaat veya tesis mühendisliği projesinin yerel mühendislik koordinat sisteminin harita koordinat sistemine dönüştürüldüğü koordinat referans sistemidir (CRS). Yansıtılmış (projected) koordinat referans sisteminin 2B veya 3B, sağ el kuralına göre tanımlanmış Kartezyen bir koordinat sistemi olduğu varsayılır. Haritada kullanılan uzunluk birimini belirtmek için isteğe bağlı MapUnit özniteliği kullanılabilir.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım | (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>Koordinat referans sisteminin tanımlandığı isimdir. Not: Modelin bulunduğu TUREF (Türkiye Ulusal Temel GPS Ağı - ITRF96) 39 dilime karşılık gelen EPSG kodu kullanılır: EPSG:5253, EPSG:5254 , EPSG:5255, EPSG:5256, EPSG:5257, EPSG:5258, veya EPSG:3259</td>
</tr>
<tr>
<td rowspan="2">Açıklama ,Jeodezik Datum</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bu koordinat referans sisteminin gayriresmi açıklaması.</td>
</tr>
<tr>
<td>Attribute: GeodeticDatum</td>
<td>-</td>
<td>Metin</td>
<td>Bu datumun tanımlandığı isim. Jeodezik datum, koordinat referans sistemi ile ilişkilidir ve dönel elipsoidin şekli ile boyutunu ve bu elipsoidin gerçek dünya / yerküre ile olan bağlantısını ve yönelimini gösterir. Türkiye Ulusal Temel GPS Ağı — ITRF96 çerçevesinin Türkiye&#x27;deki gerçeklemesidir. GRS80 elipsoidi kullanılır.</td>
</tr>
<tr>
<td>Yansıtılmış Koordinat Referans Sistemi (Düşey Datum)</td>
<td>Attribute: VerticalDatum</td>
<td>-</td>
<td>Metin</td>
<td>Düşey datumu tanımlamak için kullanılan addır. Düşey datum, koordinat referans sisteminin yükseklik ekseni ile ilişkilidir ve bir yükseklik sisteminin başlangıç düzlemini ve temel referans noktasını tanımlar. Not: Yükseklik referans sistemi olarak ITRF96 kullanılır. Gerektiğinde yerel deniz seviyesi referansına (TUDKA99) dönüşüm parametreleri ayrıca belirtilir.</td>
</tr>
<tr>
<td>Yansıtılmış Koordinat Referans Sistemi (Harita Proieksiyonu)</td>
<td>Attribute: MapProjection</td>
<td>-</td>
<td>Metin</td>
<td>Harita projeksiyonunun tanımlandığı addır. Not: Transverse Mercator (39 dilimlere bölünmüş Gauss-Krüger tipi Enine Merkator projeksiyonu. Her dilim 39&#x27;lik meridyen genişliğine sahiptir.)</td>
</tr>
<tr>
<td>Yansıtılmış Koordinat Referans Sistemi (Harita Zonu)</td>
<td>Attribute: MapZone</td>
<td>-</td>
<td>Metin</td>
<td>Merkez meridyeni değeridir (derece cinsinden). Modelin coğrafi konumuna göre ilgili zona at değer seçilir Ove açıkça belirtilir. Not: 27,30,33, 36,39, 42, veya 45 -</td>
</tr>
<tr>
<td>Yansıtılmış Koordinat Referans Sistemi (Harita ,Birimi)</td>
<td>Atiribute: MapUnit</td>
<td>-</td>
<td>Metin</td>
<td>Harita koordinat sistemini oluşturan koordinat eksenlerinin birimidir. Not Yalnızca uzunluk ölçülerini kapsar ve harita koordinat sisteminin iki veya üç ekseninin tamamı aynı uzunluk birimine sahip olmalıdır. Not: METRE kullanılacaktır</td>
</tr>
</tbody>
</table>

| İ

## Tablo 7.7 IfcMapConversion Simfi Zorunlu Öznitelik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Harita Dönüşümü (IfcMapConversion)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Harita dönüşümü, yerel mühendislik koordinat sisteminin —genellikle dünya koordinat sistemi (world coordinate system) olarak adlandırılır— temel alınan haritanın koordinat referans sistemine dönüştürülmesiyle ilgilenir. NOT: IfcMapConversion, haritanın jeodezik koordinat referans sisteminden projeksiyonunu gerçekleştirmez.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Harita Dönüşümü (Doğu)</td>
<td>Atiribute: Eastings</td>
<td>-</td>
<td>Sayı</td>
<td>Hedef harita koordinat referans sisteminin doğu (casting) ekseni boyunca konumu belirtir. NOT: Sağ el kuralına göre tanımlanmış Kartezyen koordinat sistemlerinde bu değer, x ekseni üzerindeki konumu ifade eder.</td>
</tr>
<tr>
<td>Harita Dönüşümü (Kuzey)</td>
<td>Attribute: Northings</td>
<td>-</td>
<td>Sayı</td>
<td>Hedef harita koordinat referans sisteminin kuzey (northing) ekseni boyunca konumu belirtir. NOT: Sağ el kuralına göre tanımlanmış Kartezyen koordinat sistemlerinde bu değer, y ekseni üzerindeki konumu ifade eder.</td>
</tr>
<tr>
<td>Harita Dönüşümü (Düşey Yükeklik)</td>
<td>Attribute: OrthogonalHeight</td>
<td>-</td>
<td>Sayı</td>
<td>Belirtilen düşey datıma göre düşey (orthogonal) yüksekliği tanımlar. NOT: Sağ el kuralına göre tanımlanmış Kartezyen koordinat sistemlerinde bu değer, z ekseni üzerindeki konumu ifade eder.</td>
</tr>
<tr>
<td rowspan="2">Harita Dönüşümü (Yerel X Ekseninin Doğu Bileşeni) Harita Dönüşümü (Yerel X Ekseninin Kuzey Bileşeni)</td>
<td>Attribute: XAxisAbscissa</td>
<td>-</td>
<td>Sayı</td>
<td>Yerel mühendislik koordinat referans sisteminin yerel X ekseninin yönünü gösteren vektörün uç noktasının, hedef harita koordinat referans sisteminin doğu (casting) ekseni üzerindeki değerini tanımlar. NOT: Sağ el kuralına göre tanımlanmış Kartezyen koordinat sistemlerinde bu değer Ox ekseni o üzerindeki konumu Ooifade (o eder. NOT: Bu değer, XAxisOrdinate ile birlikte kullanıldığında, yerel X ekseninin harita koordinat sisteminin yatay düzlemi içindeki yönünü tanımlar.</td>
</tr>
<tr>
<td>Atiribute: XAxisOrdinate</td>
<td>-</td>
<td>Sayı</td>
<td>Yerel mühendislik koordinat referans sisteminin yerel X ekseninin yönünü gösteren vektörün uç noktasının, hedef harita koordinat referans sisteminin kuzey (northing) ekseni üzerindeki değerini tanımlar. NOT: Sağ el kuralına göre tanımlanmış Kartezyen koordinat sistemlerinde bu Oo değer, y ekseni üzerindeki konumu ifade eder. NOT: Bu değer, XAxisAbscissa ile birlikte kullanıldığında, yerel X ekseninin harita koordinat sisteminin yatay düzlemi içindeki yönünü tanımlar.</td>
</tr>
<tr>
<td>Harita Dönüşümü (Ölçek Değeri)</td>
<td>Attribute: Scale</td>
<td>-</td>
<td>Sayı</td>
<td>Koordinat referans sisteminin (CRS) birimleri ile mühendislik koordinat Ni sisteminin birimleri aynı olmadığında kullanılacak ölçek değerini belirtir. Eğer belirtilmezse varsayılan değer 1.0 olarak kabul edilir.</td>
</tr>
</tbody>
</table>

| |

## Tablo 7.8 IfcGeometricRepresentationContext Sınıfı Zorunlu Öznitelik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Geometrik Temsil Bağlamı (IfcGeometricRepresentationContext)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım:IfcGeometricRepresentationContext, bir proje içindeki ürünlerin çeşitli şekil (geometri) temsillerine uygulanan geometrik bağlamı tanımlar. Bu bağlam, şekil temsilinin içinde tanımlandığı bağlam türünü ve bu bağlamdaki geometrik temsil öğeleri için geçerli olan sayısal hassasiyet (numeric precision) değerini belirtir. Buna ek olarak, WorldCoordinateSystem özniteliği kullanılarak projenin koordinat sistemi, küresel bir referans noktasından öteleme (offset) verilerek tanımlanabilir.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Geometrik Temsil Bağlamı (Koordinat Uzayı Boyutu)</td>
<td>Attribute: CoordinateSpaceDimension</td>
<td>-</td>
<td>Tam Sayı</td>
<td>Geometrik temsil bağlamında modellenen koordinat uzayının boyut sayısının tamsayı olarak ifade edilmesidir.</td>
</tr>
<tr>
<td>Geometrik Temsil Bağlamı (Hassasiyet)</td>
<td>Attribute: Precision</td>
<td>-</td>
<td>Sayı</td>
<td>Geometrik modeller için model hassasiyetinin değeridir. Bu değer, genellikle 1lE-5 ile 1E-8 aralığında olan, iki noktanın özdeş kabul edildiği toleransı gösteren bir çift değeridir (REAL). Bu değer örneğin brep modellerinde bir kenar eğrisinin alttaki yüzey geometrisine olan en fazla uzaklığını belirlemek için kullanılabilir.</td>
</tr>
<tr>
<td>Geometrik Temsil Bağlamı (Dünya Koordinat Sistemi)</td>
<td>Attribute: WorldCoordinateSystem</td>
<td>-</td>
<td>-</td>
<td>Projede kullanılan tüm temsil bağlamları için mühendislik koordinat sisteminin (CAD&#x27;de genellikle dünya koordinat sistemi olarak adlandırılır) oluşturulmasıdır. NOT Bu, binaların konumu orijinden çok uzakta olduğunda daha iyi sayısal kararlılık sağlamak için kullanılabilir. Ancak çoğu durumda orijin (0.,0.,0.) ve yönler x(1..0..05), 0..1..0.), z(0..0..1.) olarak ayarlanır. Eğer coğrafi yerleşim IfcMapConversion kullanılarak sağlanmışsa, WorldCoordinateSystem özniteliği, yerel mühendislik koordinat sisteminin sıfır noktası ile IfcMapConversion ötelemesinin ilişkili olduğu coğrafi referans noktası arasındaki ötelemeyi tanımlamak için kullanılır. Tercih edilen uygulamada her iki nokta (genellikle “proje baz noktası” ve “ölçüm noktası” olarak adlandırılır) çakışık olmalıdır. Ancak coğrafi referans noktasının yerel sıfır noktasından ötelenmesi</td>
</tr>
<tr>
<td>Geometrik Temsil Bağlamı (Gerçek Kuzey Yönü)</td>
<td>Atiribute: True North</td>
<td>-</td>
<td>Sayı</td>
<td>Gerçek kuzey yönü (true north) veya coğrafi kuzey yönü, projenin kendi koordinat sistemine göre tanımlanır. Bu yön, proje koordinat sisteminin XY düzlemi içinde verilen iki</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>boyutlu bir yön vektörü ile ifade edilir. Eğer belirtilmemişse varsayılan değer 0., 1. olarak alınır; bu da proje koordinat sisteminin pozitifY ekseninin coğrafi kuzey yönüne karşılık geldiği anlamına gelir. NOT: Eğer coğrafi oyerleşim IfcMapConversion kullanılarak sağlanmışsa, True North yalnızca bilgilendirme amaçlıdır. Herhangi bir tutarsızlık durumunda, IfcMapConversion ile verilen değer geçerli kabul edilir ve önceliğe sahiptir.</td>
</tr>
</tbody>
</table>

|

## Tablo 7.9 IfcAnnotation Sınıfı Zorunlu Öznitelik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Anotasyon (IfcAnnotation)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Anotasyon, bir projenin geometrik (ve mekânsal) bağlamı içerisinde yer alan ve proje modelini oluşturan nesnelere açıklama veya anlam katan bir bilgi öğesidir. Anotasyonlar; ek noktaları, eğrileri, metinleri, ölçülendirmeleri, taramaları ve diğer grafiksel not biçimlerini içerir. Ayrıca ürünleri veya mekânsal yapıları temsil etmeyen, ancak modele ait ek bileşenlerin sanal ya da sembolik gösterimlerini de kapsar; örneğin ölçüm/nirengi noktaları ve çizgileri, eş yükselti eğrileri (kot eğrileri) veya benzeri gösterimler buna dahildir.</td>
<td>SURVEY</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td rowspan="2">İsim Açıklama</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRoot)| sınıfının bazı alt tipleri için isim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir.</td>
</tr>
<tr>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
</tbody>
</table>

## Tablo 7.10 IfcProject Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Proje (IfeProject)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: IfcProject&#x27;in bir veri değişim yapısındaki temel amacı, tüm diğer bilgi öğeleri için kök örneği (root instance) ve bağlamı (context) sağlamaktır.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nesne Tipi</td>
<td>Attribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Not IfeContext alt türleri PredefinedType niteliğini içermez. Bu nedenle, ObjeciType kullanımının PredefinedType enum değerleri arasında USERDEFİNED seçilmesine bağlı olması gerekmez.</td>
</tr>
<tr>
<td>Uzun İsim</td>
<td>Attribute: LongName</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı.</td>
</tr>
<tr>
<td>Aşama</td>
<td>Attribute: Phase</td>
<td>-</td>
<td>Metin</td>
<td>Mevcut proje aşaması veya bu projenin yaşam döngüsü aşaması. Uygun aşamalar, görünüm tanımları veya uygulayıcı sözleşmeleri üzerinden belirlenmelidir.</td>
</tr>
</tbody>
</table>

## Tablo 7.11 IfcPerson Sınıfi İsteğe Bağlı Kullanılabilecek Öznitelik Listesi (IfcProject içerisinde tariflenir)

<table>
<tbody>
<tr>
<td colspan="4">Kişi (IfcPerson)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bu varlık, bir bireyi temsil eder. NOT: Birçok ülkede, veri tabanlarında kişilerin tanımlanmasına ilişkin yasal düzenlemeler bulunmaktadır. IFC Modeli&#x27;nin amacı veri değişimi ve paylaşımı için bir tanımlama standardı olarak hizmet etmek olsa da, bazı durumlarda bir IFC dosyası bu tür mevzuatlar kapsamında belirli bir kişiyi tanımlamaya olanak sağlayan bir veri tabanı olarak kabul edilebilir. Kullanıcılar, IFC dosyalarının kullanıldığı yerlerde geçerli olabilecek yasal kısıtlamaların farkında olmalıdır.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Orta Ad</td>
<td>Attribute: MiddleNames</td>
<td>-</td>
<td>Metin</td>
<td>Aynı veya benzer soyadı ve adı taşıyan diğer kişilerden ayırt edilmesini sağlayan, kişiye verilen ek adlardır. NOT: İkinci adlar genellikle gündelik iletişimde kullanılmaz, ancak gerekirse belirli bir kişiyi tanımlamak için ek tanımlayıcı olarak kullanılabilir. Bu adlar, özellikle kişinin soyadının bulunduğu bölgede çok yaygın olarak kullanıldığı durumlarda yararlıdır.</td>
</tr>
</tbody>
</table>

7

## Tablo 7.12 LfcOrganization Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik Listesi (IfcProject içerisinde tariflenir)

<table>
<tbody>
<tr>
<td colspan="4">Organizasyon (IfcOrganization)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kurumsal bir kimliğe sahip, adlandırılmış ve yapılandırılmış bir gruplamadır. NOT: Bir şirket içindeki departmanlar arasındaki ilişkilerde olduğu gibi, IfcOrganization varlıkları arasındaki ilişkiler, nesneleştirilmiş ilişki olan IfcOrganizationRelationship aracılığıyla ifade edilebilir.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
</tbody>
</table>
