# EK-6 — IFC sınıflarının öznitelik ile özellik tanımları

> Düzenlenebilir metin ve HTML tablolar. OCR yazımları ile hücre birleştirmeleri otomatik aktarılmıştır; TEYİT BEKLİYOR. Tablolar resim değildir. Grafikler varsa ayrı düzenlenebilir SVG vektörleridir. Bu aktarım hukuki doğrulama veya uygulama kapsamı onayı değildir.

Kaynak: RG 05.08.2026 / 33331.

EK-6 IFC SINIFLARININ ÖZNİTELİK İLE ÖZELLİK TANIMLARI

6.1- Tasarımda yer verilen varlıkların temsilinde kulfanılan zorunlu IFC sını/ları EK-5 Tablo 5.V'de ve kullanımı isteğe bağlı IFC sınıfları Tablo 5.2'de verilmiştir.

6.1.1- Tablo 6.1 ile Tablo 6.135 arasında yer alan IFC sınıfları, IFC 4.3 versiyonu esas alınarak düzenlenmiştir.

6.1.2- BIM modelinde alt sınıfı bulunan bir üst sınıfkullanılmaz. Bu durumda yalnızca alt sınıf modele dahil edilir.

6.1.3- BIM modelinde, IFC şemasında özel bir tanımı olmayan veya henüz sınıfı belirlenmemiş nesneleri temsil eden genel bir varlığa (nesne vekili- IfeProxy veya bina nesne vekili - IfcBuildingElementProxy) yer verilemez.

6.2- Uniclass 2015 sınıflandırma kodları (bilgi için verilmiştir): Her varlığa ait belirlenmiş olan öznitelikler ve özellikler ile birlikte Uniclass 2015 sınıflandırma kodları kullanılabilir.

6.3- Zorunlu IFC sınıflarında yer alması gereken zorunlu öznitelikler ve özellikler Tablo 6.1 ila

Tablo 6.68 tablolarında verilmiştir. 6.4 Zorunlu IFC sınıflarında yer alması isteğe bağlı olan öznilelikler ve özellikler Tablo 6.69 ila Tablo 6.135 tablolarında verilmiştir ve ilgili idare tarafından talep etmesi halinde ilgili IFC smufinda yer alır.

6.5- Tablo 6.1 ile Tablo 6.135 arasında yer alan TREpys ile başlayan tüm özellik setleri ve altında yer alan özellikler modelde kullanıcı tarafından oluşturulacaktır. Diğer özellikler IFC veri şemasında yer alan özelliklerdir.

6.6- EK-5 Tablo 5.2'de yer alan isteğe bağlı IFC sınıfların öznitelikleri ve özellikleri Yönetmeliğin 5 inci maddesinin birinci fıkrası kapsamında belirlenebilir.

## Tablo 6.1 IfcAirTerminal Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Havalandırma Menfezi (IfcAirTerminal)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir havalandırma menfezi, dağıtım sistem(ler)i ile bir veya birden fazla mahal arasındaki hava transferinin başlangıç veya bitiş noktasıdır. Ayrıca, bitişik mekanlar arasında hava transferi için de kullanılabilir.</td>
<td>DIFFUSER, GRILLE, LOUVRE, REGİSTER, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRoot)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-3&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>IfeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfeProduct örneğinin (sistem (üyelerinin) gruplandırma ilişkisi, (IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Hava Akış Debisi Aralığı</td>
<td>AirFlowRateRange</td>
<td>PsetAirTerminalTypeCom mon</td>
<td>Sayı</td>
<td>Sağlanabilecek hava debisinin olası aralığı. Hava terminalinin çalışmak üzere tasarlandığı hava debisi aralığı.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler (FC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

,

## Tablo 6.2 IfcAudioVisualAppliance Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Görüntü ve Ses Cihaz (IfcAudioVisualAppliance)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir görüntü ve ses cihazı veya görüntüyü gösteren, kaydeden, ileten veya alan bir aygıttır.</td>
<td>AMPLIFTER, CAMERA, DİSPLAY, MECROPHONE, PLAYER, PROJECTOR, RECEİVER, SPEAKER, SWITCBER, TELEPHGONE, TUNER, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım - (Bilgi Amaçlı)”.</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>“(Bilgi Amaçlı)”:</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-<br>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (f1fcRootJ) smıfınm bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>&#x27;Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
</tbody>
</table>

1 i i | i | i

## Tablo 6.3 LfcBeam Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kiriş (IfeBeam)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir Kiriş, genellikle yatay veya neredeyse yatay bir yapısal elemandır ve yükleri esas olarak eğilme taşıma gücü ile Karşılar. Mimari açıdan böyle bir elemanı da temsil edebilir. Yük taşıyıcı olması gerekmez.</td>
<td>BEAM, JOİST, HOLLOWCORE, LİNTEL, SPANDREL, TBEAM, GIRDER SEGMENT, DIAPHRAGM, PJERCAP, HATSTONE, CORNİCE, EDGEBEAM, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<td>Türkçe Tanimi “(Bilgi Amaçlı)</td>
<td>Öznitelik.</td>
<td>İlişki</td>
<td>-.. Veri Tipi (Bilgi Amâçl) ©</td>
<td>Me Aa m</td>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>İFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (HfcRootj| sınıfının bazı ali tipleri için İsim niteliğinin eklenmesi gerekedilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale igetirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki ctket tanımlayıcısı, Örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. N</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Atiribute(lfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>İL1fcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım: (Bilgi Amaçlı)</th>
<th>© Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>“(Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>.FireRating</td>
<td>Pset BsamCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (HfeRelAssociatesMaterizl&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi, Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik 5355 Beton C25)</td>
</tr>
</tbody>
</table>

| | | i | | |

## Tablo 6.4 IfcBoiler Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="5">Kazan (IfcBoiler) i Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kazan, doSal gez, fuel-oil veya elektrik gibi bir enerji kaynağı kullanılarak suyun veya başka bir akışkanın ısıtıldığı, basınca dayanıklı kapalı bir basınçlı kaptır. Kazandaki akışkan daha sonra çeşitli süreçlerde veya ısıtma uygulamalarında kullanılmak üzere kazanın dışına sirküle edilir.</td>
<td>WATER, STEAM, USERDEFİNED. NOTDEFİNED</td>
</tr>
<tr>
<td>Türkçe Tanım “(Bilgi Amaçlı)</td>
<td>emÖznitelik b :</td>
<td>İlişki</td>
<td>ço Veri Tipi “(Bilgi Amaçlı)</td>
<td>e Kİ e e ie 2 © i “Açıklama Mi ei i Gi</td>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>İFC uyumlu yazıhm sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfeRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanım)ayıcıdır. N</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;Ifc System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık. Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev va da hizmet sunmak üzere bir araya getirilmiş ilişkili &#x27;parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel .olarak ilişkili ürünler grubudur. Bir veya birden fazla ifcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, HeRelAssignsToGroup aracılığıyla yönetilir. Ni</td>
</tr>
<tr>
<th>(Bilgi Amaçlı):</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>ogywMeri Tipi “(Bilgi Amaçlı)</th>
<th>ii o m © Açıklama an, |</th>
</tr>
<tr>
<td>Nominal Enerji Tüketimi</td>
<td>NominalEnergyConsumpti fon</td>
<td>PsetBoilerTypeCommon</td>
<td>Sayı</td>
<td>Toplem kazan ısı gücünü sağlamak için gerekli nominal yakıt tüketim debisi. .</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

i | |

## Tablo 6.5 IfcBridge Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Köprü (IfcBridge))</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Köprü, yayaların, hayvanların, araçların ve altyapı hizmetlerinin engellerin üzerinden veya yerden yüksekte bulunan iki nokta arasında geçişini sağlayan bir inşaat mühendisliği yapısıdır.</td>
<td>ARCHED, CABLE STAYED, CANMLEVER, CULVERİ, FRAMEWORK, GIRDER, SUSPENSION, TRUSS, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya Kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. |JIfcRootJ) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5”e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute (IfcRelAssociatesMaterial &gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Atıribute (IfcRelAssociatesMaterial&gt;IfeMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek: Çelik $355 Beton C25)</td>
</tr>
</tbody>
</table>

,

## Tablo 6.6 IfcBridgePart Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Köprü Parçası (IfcBridgePart)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir köprünün parçası.</td>
<td>ABUTMENT, DECK, DECK SEGMENT, FOUNDATION, PIER, PIER SEGMENT, PYLON, SUB STRUCTURE, SUPER STRUCTURE, SURFACE STRUCTURE, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Aüribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir) a,</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(lfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik 355 Beton C25)</td>
</tr>
</tbody>
</table>

## Tablo 6.7 IfcBuilding Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Bina (IfcBuilding)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir bina. içindekilere veya içeriğine barınak sağlayan ve sabit bir konumda duran bir yapıyı temsil eder. Bina aynı zamanda, bir bina projesinin bileşenleri için (arsa, kat ve mahal ile birlikte) mekânsal yapı hiyerarşisinde temel bir eleman olarak kullanılır.</td>
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
<td>Uzun İsim</td>
<td>Attribute:LongName</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute:Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. HfIfcRootj)| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Bina Kimliği</td>
<td>BuildingID</td>
<td>Pset_BuildingCommon</td>
<td>Metin</td>
<td>Bir binaya atanan benzersiz bir tanımlayıcıdır. Planlama başvurusu yapıldığı anda geçici bir kimlik atanır. Bu geçici kimlik, bina yasal binalar ve taşınmazlar veri tabanına kaydedildiğinde kalıcı bir kimliğe dönüştürülür.</td>
</tr>
<tr>
<td>Kalıcı Kimlik</td>
<td>IsPermanentID</td>
<td>Pset_BuildingCommon</td>
<td>Mantıksal</td>
<td>Nesneye atanan kimliğin kalıcı (= DOĞRU) mı yoksa geçici (= YANLIŞ) mi olduğunu belirtir.</td>
</tr>
<tr>
<td>Yapım Yöntemi</td>
<td>ConstructionMethod</td>
<td>Pset_BuildingCommon</td>
<td>Metin</td>
<td>Nesneye ait inşaat eyleminin türü; örneğin yeni inşaat, yenileme, tadilat vb. Ni</td>
</tr>
<tr>
<td>Yangın Koruma Sınıfı</td>
<td>FireProtectionClass</td>
<td>Pset_BuildingCommon</td>
<td>Metin</td>
<td>İlgili ulusal bina yönetmeliğinde verilen yangın koruma sınıflandırma tablosuna göre binaya atanan ana yangın koruma sınıfı.</td>
</tr>
<tr>
<td>Kullanım Türü</td>
<td>OccupancyType</td>
<td>Pset_BuildingCommon</td>
<td>Metin</td>
<td>Bu nesneye ait kullanım türü; yürürlükteki ulusal bina yönetmeliğine göre tanımlanır.</td>
</tr>
<tr>
<td>Brüt Planlanan Alan</td>
<td>GrossPlannedArea</td>
<td>Pset_BuildingCommon</td>
<td>Sayı</td>
<td>Mekânsal yapı elemanının toplam planlanan brüt alanı. Mekânsal yapı elemanının planlanmasında kullanılır.</td>
</tr>
<tr>
<td>Net Planlanan Alan</td>
<td>NetPlannedArea</td>
<td>Pset_BuildingCommon</td>
<td>Sayı</td>
<td>Nesnenin toplam planlanan net alanı. Nesnenin planlanmasında kullanılır.</td>
</tr>
<tr>
<td>Kat Sayısı</td>
<td>NumberOfStoreys</td>
<td>Pset_BuildingCommon</td>
<td>Sayı</td>
<td>Binadaki kat sayısı. IfeBuildingStorey varlığının kullanılmadığı! durumlarda belirtilir. IfcBuildineStorey kullanılmışsa, kat sayısı oradan belirlenmelidir.</td>
</tr>
<tr>
<td>Adres Satırları</td>
<td>AddressLines</td>
<td>Pset_Address</td>
<td>Metin</td>
<td>Posta adresidir. NOT: Bir posta adresi kaydedilirken birden fazla satır (veya öğe) içerebilir. Normal kullanımda, aşağıdaki adres kavramlarının ilgili unsurlarını içermesi beklenir: Bina içindeki konum (ör. 3. Kat) Bina adı (ör. Interoperability House) Bina numarası (ör. 6400) Sokak adı (ör. Alliance Boulevard) Adres satırlarının tipik içeriği ülkeden ülkeye değişiklik gösterebilir.</td>
</tr>
<tr>
<td>İl/ Kasaba</td>
<td>Town</td>
<td>Pset_Address</td>
<td>Metin</td>
<td>Bir kasaba veya şehrin adıdır.</td>
</tr>
<tr>
<td>Bölge/ İlçe</td>
<td>Region</td>
<td>Pset_Address</td>
<td>Metin</td>
<td>Bir bölgenin adıdır.</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>Qto_BuildingBaseQuantities</td>
<td>Sayı</td>
<td>Karakteristik yükseklik. Bu binanın standart brüt yüksekliği; inşaat döşemesinin üst yüzeyinden bir üst döşemenin veya çatının üst yüzeyine kadar olan yükseklik. Sadece yüksekliğin sabit olduğu durumda belirtilir.</td>
</tr>
<tr>
<td>Saçak Yüksekliği</td>
<td>EavesHeight</td>
<td>Qto_BuildingBaseQuantities</td>
<td>Sayı</td>
<td>Bu katın standart net yüksekliği: inşaat döşemesinin üst yüzeyinden bir üst döşemenin veya çatının alt yüzeyine kadar olan yükseklik. Sadece yüksekliğin sabit olduğu durumda belirtilir.</td>
</tr>
<tr>
<td>Taban Alanı</td>
<td>FootPrintArea</td>
<td>Qto_BuildingBaseQuantities</td>
<td>Sayı</td>
<td>Binanın veya binaların kapladığı arsanın brüt alanı.</td>
</tr>
<tr>
<td>Brüt Kat Alanı</td>
<td>GrossFloorArea</td>
<td>Qto_BuildingBaseQuantities</td>
<td>Sayı</td>
<td>Mekânsal yapı elemanı içindeki tüm brüt kat alanlarının toplamıdır. Bina katındaki yapı elemanlarının alanlarını içerir. Katla ilişkilendirilmiş mekân ve yapı elemanlarının miktarlarına ek olarak belirtilebilir. Tutarsızlık durumunda, mekân ve yapı elemanlarının bireysel miktarları geçerlidir.</td>
</tr>
<tr>
<td>Net Kat Alanı</td>
<td>NetFloorArea</td>
<td>Qto_BuildingBaseQuantities</td>
<td>Sayı</td>
<td>Tüm net kullanılabilir kat alanlarının toplamıdır. Binadaki yapı elemanlarının alanlarını içermez. Binaya atanmış mekân metrajına ek olarak belirtilebilir. Tutarsızlık durumunda, mekânın bireysel metrajları önceliklidir.</td>
</tr>
<tr>
<td>Posta Kutusu</td>
<td>PostalBox</td>
<td>Pset_Address</td>
<td>Metin</td>
<td>Tanımlı bir posta kutusuyla ilişkilendirilen adrestir.</td>
</tr>
</tbody>
</table>

| | | |

| |

  

## Tablo 6.8 IfcBuildingStorey Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Bina Katı (IfcBuildingStorey)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bina katı bir kota sahiptir ve genellikle düşeyde sınırlanmış, (neredeyse) yatay bir mahal grubunu temsil eder.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım: “(Bilgi Amaçlı) &gt;</th>
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
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. |HfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<th>— Türkçe Tanim (Bilgi Amaçlı)”</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Net Kat Alanı</td>
<td>NetFloorArea</td>
<td>Qto_BuildingStoreyBaseQuantities</td>
<td>Sayı</td>
<td>Tür net kullanılabilir kat alanlarının toplamıdır. Binadaki yapı elemanlarının alanlarını içermez. Binaya atanmış mekân metrajına ek olarak belirtilebilir. Tutarsızlık durumunda, mekânlarn bireysel miktarları önceliklidir.</td>
</tr>
<tr>
<td>Taşıyıcı Döşeme Ust Kotu</td>
<td>ElevationOfSSLRelative</td>
<td>Pset_BuildingStoreyCommon</td>
<td>Sayı</td>
<td>Taşıyıcı döşeme seviyesinin üst yüzey kotu, yerel sıfır yüksekliğine göre verilen kot değeridir. Seviye değişkenlik gösteriyorsa ve belirgin bir baskın kot bulunmuyorsa, bu özellik girilmeyebilir. Üst yüzevin geometrik okonumlandırmasıyla herhangi bir tutarsızlık olması durumunda, geometrik gösterim dikkate almnır.</td>
</tr>
</tbody>
</table>

i | |

## Tablo 6.9 IfeBurner Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Brülör (IfcBurner)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Brülör, yakıtı yanma yoluyla ısıya dönüştüren bir cihazdır. Gaz, yağ ve odun brülörlerini içerir.</td>
<td>USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım “(Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>.... Veri Tipi... &lt;&lt;(Bilgi Amaçlı)”</th>
<th>e Aşıklama e</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((HfeRoorj| sınıünın bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kurah ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>“Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, ömeğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>I£cSystem</td>
<td>YeRelAssiğnsToGroup&gt;fe System</td>
<td>| Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir &#x27;amaç, işlev va da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla ifcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssigns?ToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td>Türkçe Tanım -— (Bilgi Amaçlı) —</td>
<td>Özellik</td>
<td>© © Özellik Seti / İlişki ©</td>
<td>| çeri Tipi. “(Bilgi Amaçlı)</td>
<td>2 n 5 &#x27; z AL yi - Açıklama Rİ eyi ie</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpt ön</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

| | 1 | | | |

## Tablo 6.10 IfcCableCarierFitting Sınıfı Zorunlu Öznitelikve Özellik Listesi ;

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kablo Taşıyıcı Bağlantı Parçası (fcCableCarrierFitting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir kablo taşıyıcı bağlantı parçası, kablo taşıyıcı sisteminde bir bağlantı noktasına veya geçiş yerine yerleştirilen bağlantı elemanıdır.</td>
<td>BEND, CONNECTOR, JUNCTION, TRANSITION, ÜSERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>© Türkçe Tamm “(Bilgi Amaçlı)”</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>su VeriTipi» - (Bilgi Amaçh)</th>
<th>Aşama e e</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedTyvpe</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRoor)| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir) ği</td>
</tr>
<tr>
<td>Etiket</td>
<td>Atiribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş ömek düzeyindeki tanımlayıcıdır...</td>
</tr>
</tbody>
</table>

|

## Tablo 6.11 [fcCableCarrierSegment Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kablo Taşıyıcı Segment (IfcCableCarrierSegment)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir kablo taşıyıcı segmenti, özellikle kabloları taşımak ve desteklemek için kullanılan bir akış segmentidir.</td>
<td>CABLE BRACKET, CABLE LADDER SEGMENT, CABLE TRAY SEGMENT, CABLE TRUNKING SEGMENT, CATENARY WİRE, CONDU!T SEGMENT, DROPPER, USERDEFINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. |(IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir) m,</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş önek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde. ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfeProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Nol: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.12 IfcCaissonFoundation Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Keson Temeli (IfcCaissonFoundation)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Keson temeli esasen açık veya kapalı olabilen boş bir kutudur.</td>
<td>WELL, CAİSSON, USERDEFİNED, NOTDERİNEB</td>
</tr>
<tr>
<td>Türkçe Tanım © “(Bilgi Amaçlı)</td>
<td>0 Özmitelik</td>
<td>İlişki</td>
<td>“(Bilgi Amaçlı)</td>
<td>i Açıklama</td>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td colspan="2">Metin “Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>,Attribute;: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootlJ sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (XK-S*egöre isimlendirilecektir) a,</td>
</tr>
<tr>
<td>Etiket</td>
<td>“Atiribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>iBir ürünün belirli bir örmeğindeki etiket tanımlayıcısı, örneğin seri İnumarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. i Ni</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Atiribute (fcRelAssociatesMaterial &gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(HeMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
</tbody>
</table>

| | |*Attribute (IfcRelAssociatesMaterial>[fcMaterial): Name* bilgisi giriliken: "Malzeme İsmi Dayanım" formatı kullanılmalıdır. (Örnek:Çelik, $355 : |Beton_C25) a Ni a Ni a, |

## Tablo 6.13 IfcChiller Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Soğutma Grubu (ifeChiller)</td>
<td>Ön Tanımlı Tür</td>
</tr>
<tr>
<td colspan="4">Tanım: Soğutma grubu, bir sıvıdaki ısıyı uzaklaştırmak için buhar sıkıştırmalı veya absorbsiyonlu soğutma çevrimini kullanan bir cihazdır. Genellikle su veya su-glikol karışımı olan akışkanı soğutmak için kullanılır. Soğutulmuş akışkan daha sonra bir binadaki havayı soğutmak ve nemini gidermek için kullanılır.</td>
<td>AJR COOLED, WATER COOLED, HEAT RECOVERY, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((fcRootj) sınıfının bazı alt tipleri için İsim niteliğinin ekijenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;fc Svstem</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Soğutucu Kapasitesi</td>
<td>ChillerCapacity</td>
<td>PsetChillerTypeCommon</td>
<td>Sayı</td>
<td>Yetkili kurum tarafından tanımlanan standart koşullarda, soğutucunun nominal soğutma kapasitesi.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.14 IfeChimney Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="3">Baca (IfcChimney)</td>
<td colspan="2">Ön Tanımtı Tip Listesi |</td>
</tr>
<tr>
<td colspan="3">Tanım: Bacalar genellikle bir binanın yapısının dikey ya da dikeye yakın bölümleridir ve bina kabuğunun bir parçasını oluştururlar. Genellikle prefabrik veya yerinde dökme betondan inşa edilirler; günümüzde tuğla ile yapılmaları ise nadirdir.</td>
<td colspan="2">UŞERDEFİNED, NOTDEFİNEBD</td>
</tr>
<tr>
<th>Türkçe Tahım&gt; (Bilgi Amaçlı)</th>
<th>© Öznitelik</th>
<th>İlişki</th>
<th>“eri Tipi «5. “(Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((ifeRootl! sınıfının hazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir) . il</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>&#x27;Bir ürünün belirli bir örneğindeki etiket tanıumlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. . Ni</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfeRelAssociates Material&gt;IfeMaterial): Name”</td>
<td>-</td>
<td>Metin</td>
<td>ı(IfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
</tbody>
</table>

| | | *Attribute (IfcRelAssociatesMaterial>]fcMaterial): Name* bilgisi giriliken: "Malzeme İsmi Dayanım" formatı kullanılmalıdır. (Örnek:Çelik S355 ,Beton C25) a Ni ni _ ae Ni

Zorunlu Öznitelik ve Özellik Listesi

## Tablo 6.15 IfcCoil Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Serpantin (IfcCoil)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Serpantin, birbirine karışmayan akışkanlar arasında Isı transferi sağlamak için kullanılan bir cihazdır. Yaygın bir örnek, yüzeyi boyunca hareket eden havadan ısıyı uzaklaştırmak için soğutulmuş su, antifriz veya soğutucu akışkan dolaştırılan kanatlı bir serpantinin kullanıldığı soğutma serpantinidir. Bir serpantin, bir ısıtma veya soğutma akışkanı taşıyan bir dizi borunun (serpantin) bir hava akımına yerleştirilmesiyle ısıtma veya soğutma amaçları için kullanılabilir. Serpantin, serpantin formunda demetlenmiş borulardan veya genişletilmiş bir ısı transfer yüzeyi sağlayan kanatlı borulardan yapılabilir.</td>
<td>DXCOOLING COIL, ELECTRİC HEATING COİL, GAS HEATING CO!L, HYDRONIC COİL, STEAM HEATING COİL, WATER COOLING COIL, WATER HEATING COIL, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedIype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IHeSystem</td>
<td>YeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct ömeğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nominal Gizli Kapasite</td>
<td>NominalLatentCapacity</td>
<td>PsetCoilTypeCommon</td>
<td>Sayı</td>
<td>Nominal gizli kapasite.</td>
</tr>
<tr>
<td>Nominal Hissedilir Kapasite</td>
<td>Nominal SensibleCapacity</td>
<td>PsetCoilTypeCommon</td>
<td>Sayı</td>
<td>Nominal hissedilir kapasite.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.16 IfcColumn Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve ÖzellikListesi</td>
</tr>
<tr>
<td colspan="4">Kolon (IfcColumn)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kolon genellikle statik akslarla hizalanan, düşey yapısal veya mimari bir elemandır. Çoğu durumda. basınç yoluyla üst yapıdaki yükü alttaki diğer yapısal elemanlara aktaran düşey ya da düşeye yakın konumlu bir yapısal elemanı temsil eder. Mimari bakış açısından da böyle bir elemanı temsil edebilir; bu durumda yük taşımayan bir eleman olabilir. Bir kolonun yapısal olarak yük taşıyan veya yük taşımayan bir eleman olup olmadığı |(PsetColumnCommon||.((LoadBearingi| özelliğiyle belirlenir.</td>
<td>COLUMN, PIERSTEM, PIERSTEM_SEGMENT, PILASTER, STANDCOLUMN, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. f((1fcRootjl sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir ömeğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute (IfcRelAssociatesMaterial &gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>i((fcMaterial), yapı elemanları (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>Pset_ColumnCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td>Taşıyıcı</td>
<td>LoadBearing</td>
<td>Pset_ColumnCommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir .</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi_Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik_S355 Beton_C25)</td>
</tr>
</tbody>
</table>

, | İ

## Tablo 6.17 IfcCommunicationsAppliance Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="5">İletişim Cihazı (1fcCommunicationsA ppliance) Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: İletişim cihazı, elekironik veya dijital bilgiyi veri ya da ses olarak ileten ve alan bir aygıttır.</td>
<td>ANTENNA, COMPUTER, FAX, GATEWAY, MODEM, NETWORK APPLIANCE, NETWORK BRIDGE, NETWORK HUB, PRINTER, REPEATER, ROUTER, SCANNER, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootjj sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir) Ni</td>
</tr>
<tr>
<td>Etiket</td>
<td>Atiribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
</tbody>
</table>

; 7

## Tablo 6.18 IfcCondenser Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kondenser (IfcCondenser)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kondenser, genellikle bir soğutucuyu (refrigerant) gaz halinden sıvı hale yoğunlaştırarak ısıyı dağıtmak için kullanılan bir cihazdır.</td>
<td>AIR COOLED, EVAPORATIVE COOLED, WATER COOLED, WATER COOLED BRAZEDPLATE, WATER COOLED SHELL COIL, WATER COOLED SHELL TUBE, WATER COOLED TUBE IN TUBE, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where” kuralı ile zorunlu hale getirilecektir. (EK-57e göre isimlendirilecektir) Ni</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssiznsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde. ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nomina!| toplam güç tüketimi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.19 IfcCoolingTower Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Soğutma Kulesi (IfcCoolingTower)</td>
<td>Ön Tanımlı Tip Listesi |</td>
</tr>
<tr>
<td colspan="4">Tanım: Soğutma kulesi, su gibi bir akışkanı dolaştırarak sıcaklığını kısmi buharlaşma yoluyla düşürmek için ısıyı ortam havasına atan bir cihazdır.</td>
<td>NATURAL DRAFT, MECHANICAL INDUCED DRAFT, MECHANICAL FORCED DRAFT, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRoot)| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. .</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;Ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir. Ni</td>
</tr>
<tr>
<th>i Türkçe Tanım © (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nominal Kapasite</td>
<td>NominalCapacity</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Sayı</td>
<td>Kulenin toplam nominal veya hacimsel soğutma kapasitesi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

| ,

## Tablo 6.20 IfcCovering Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kaplama (IfcCovering)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kaplama, başka bir elemanın bir kısmını örten ve tamamen o elemana bağlı olan bir elemandır. IfcCovering, bir kaplama türünün oluşumunu tanımlar ve (varsa) bu tür IfcCoveringType tarafından ifade edilir.</td>
<td>CEILING, CLADDING, COPING, FLOORING, INSULATION, MEMBRANE, MOLDING, ROOFING, SKIRTING BOARD, SLEEVING, TOPPING, WRAPPING, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>İFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. f(1fcRootj)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örmek düzeyindeki tanımlayıcıdır. il Ni</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(fcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td>Kaplama Malzemesi</td>
<td>Attribute: Material</td>
<td>Attribute(IfcRelAssociatesMaterial&gt;IfcMaterialLayerSetUsage&gt;IfcMaterialLayerSet&gt;IfcMaterialLayer): Material**</td>
<td>Metin</td>
<td>Katmanın oluşturulduğu malzemeye yönelik isteğe bağlı referans. Bu değerin boş bırakılması, katmanın malzeme içermediğini (örneğin hava boşluğu olduğunu) ifade etmez; yalnızca ilgili aşamada malzeme bilgisinin tanımlanmadığını gösterir.</td>
</tr>
<tr>
<td>Kaplama Kalınlığı</td>
<td>Attribute: LayerThickness</td>
<td>Attribute(IfcRelAssociatesMaterial&gt;IfcMaterialLayerSetUsage&gt;IfcMaterialLayerSet&gt;IfcMaterialLayer): LayerThickness**</td>
<td>Metin</td>
<td>Malzeme katmanının kalınlığıdır. “Kalınlık” teriminin anlamı, kullanımına bağlı olarak değişir. IfcMaterialLayerSetUsage kullanan yapı elemanlarında, bu boyut IfcMaterialLayerSetUsage içinde belirtilen pozitif LayerSetDirection doğrultusunda ölçülür. NOT: Zar (membran) gibi kalınlığı sıfıra çok yakın olan malzemeler için bu öznitelik değeri O olabilir. Kalınlığı O olan malzeme katmanları geometrik gösterimde görüntülenmeyebilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>Pset_CoveringCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td rowspan="3"></td>
<td colspan="4">** Kaplamalarla ilgili bu özellikler: (1) IfcSpace içindeki tanımlardan faydalanılarak yada (2) IfcCovering&#x27;de belirtilen ilişkiler kurularak doğrudan modelleme ile tanımlanacak. Bu nedenle belirtilen bu iki yöntemden biri zorunludur.</td>
</tr>
<tr>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi_Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik_S355 Beton_C25)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.21 IfcCurtain Wall Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Giydirme Cephe (IfcCurtainWall)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir giydirme cephe, zemine oturmaktan ziyade döşemel/çatı strüktürünün kenarına asılmış bileşenlerin bir araya gelmesiyle oluşturulan bir bina duvarıdır. Giydirme cephe, bir bina elemanı bileşimi olarak temsil edilir ve ((IfcBuihtElement|| alt tipi olarak IfcRelAgeregates ilişkisini kullanarak (o uygulanır. o Giydirme (oOcephe (ogenellikle Odış cephe Olur Oo ancak (Pset CurtainWaliCommon)||.((isExtemal|) kullanılarak iç mekân giydirme cepheleri de tanımlanabilir.</td>
<td>USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociatesMaterial&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfeMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti/ İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>Pset_CurtainWallCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi_Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik_S355 Beton_C25)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.22 IfcDamper Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Damper (IfcDamper)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir damper, tipik olarak bir HVAC kanal dağıtım sisteminde yer alır ve hava akışını kontrol etmek veya düzenlemek için kullanılır.</td>
<td>BACK DRAFT DAMPER, BALANCING DAMPER, BLAST DAMPER, CONTROL DAMPER, FİRE DAMPER, FİRE SMOKE DAMPER, FUME HOOD EXHAUST, GRAVITY DAMPER, GRAVITY RELİEF DAMPER, RELİEF DAMPER, SMOKE DAMPER, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. /((IfcRootjl| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>| Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>| Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;Ye System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmakiadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.23 IfcDistributionBoard Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Dağıtım Panosu (IfcDistributionBoard)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Dağıtım panosu, belirli bir amaç doğrultusunda elektriksel veya iletişim cihazlarının bir araya getirildiği enerji dağıtımını ve devrelerin kontrolünü sağlayan merkezi bir akış kontrol cihazıdır.</td>
<td>CONSUMER UNİT, DISTRIBUTION BOARD, MOTOR CONTROL CENTRE, SWITCH BOARD, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özmitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRoot)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>feSystem</td>
<td>YeRelAssignsToGroup&gt;1f cSystem</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde. ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen. işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi. IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>Nominal PowerConsumptio n</td>
<td>PsetElectricalDeviceCo mmon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

## Tablo 6.24 IfcDistributionSystem Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Dağıtım Sistemi (IfcDistributionSystem)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir dağıtım sistemi, bir dağıtım ortamının akışını almak, depolamak, sürdürmek, dağıtmak veya kontrol etmek üzere tasarlanmış bir ağdır. Yaygın bir örnek, bir pompa, bir tank ve sıcak suyu terminallere dağıtmak için birbirine bağlı bir boru sisteminden oluşan bir sıcak su ısıtma sistemidir.</td>
<td>AIRCONDITIONING, AUDIOYISUAL, CATENARY SYSTEM, CHEMİCAL, CHILLEDWATER, COMMUNICATION, COMPRESSEDAIR, CONDENSERWATER, CONTROL, CONVEYING, DATA, DISPOSAL, DOMESTICCOLDWATER, DOMESTICHOTWATER, DRAHNAGE, EARTHING, ELECTRICAL, ELECTROACOUSTIC, EXHAUST, FIREPROTECTİON, FİXEDTRANSMISSIONNETWORK, FUEL, GAS, HAZARDOUS, HEATING, LIGHTING, LIGHTNINGPROTECTION, MOBILENETWORK, MONITORINGSYSTEM, MUNICIPALSOLIDWASTE, OlL, OPERATTONAL, OPERATIONALTELEPHONYSYSTEM, OVERHEAD CONTACTLINE SYSTEM, POWERGENERATION, RAINWATER, REFRIGERATION, RETURN CIRCUIT, SECURİTY, SEWAGE, SIGNAL, STORMWATER, TELEPHONE, TV, VACUUM, VENT, VENTILATION, WASTEWATER, WATERSUPPLY, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tür</td>
<td>PredefinedT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tür.</td>
</tr>
<tr>
<td>Uzun İsim</td>
<td>Attribute:LongName</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRoot)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu. bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.25 IfcDoor Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kapı (IfcDoor)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kapı, esas olarak insanlar, eşyalar, hayvanlar ve araçlar için kontrollü erişim sağlamak üzere kullanılan bir yapı elemanıdır. Menteşeli, eksenel. kayar ve ayrıca döner kapı veya katlanır kapı yapılarını içerir.</td>
<td>BOOM BARRIER, DOOR, GATE, TRAPDOOR, TURNSTILE, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>© Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. |((IfcRootj| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu. bir “where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>Pset_DoorCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Yangın Dayanımı Sınıfı</td>
<td>FireRating</td>
<td>Pset_DoorCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td>Asil Çıkış |</td>
<td>FireExit</td>
<td>Pset_DoorCommon</td>
<td>Mantıksal</td>
<td>Bu nesnenin yangın durumunda çıkış olarak kullanılmak üzere tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir. Burada, çıkış kapısı ulusal bina yönetmeliğine uygun olarak tanımlanmaktadır.</td>
</tr>
</tbody>
</table>

| |

Ni 7 ni

## Tablo 6.26 IfeDuctFitting Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kanal Bağlantı Parçası (lfeDuctFitting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kanal bağlantı parçası, kanallı akış dağıtım sisteminde bir bağlantı veya geçiş elemanıdır ya da kanal segmentlerini bağlamak için kullanılır. Bu, akışkanın yönü ve debisi gibi akış özelliklerinde değişikliklere neden olur.</td>
<td>BEND, CONNECTOR, ENTRY, EXIT, JUNCTION, OBSTRUCTION, TRANSITION, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootJj smıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kural; ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı. örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanmlayıcıdır..,.,,, Ni</td>
</tr>
<tr>
<td>Sister</td>
<td>IfcSystem</td>
<td>HeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfeRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

| | |

## Tablo 6.27 IfeDuctSegment Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kanal Segmenti (IfcDuctSegment)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kanal segmenti, tipik olarak kanal ağı şebekesinin iki bölümünü birleştirmek için kullanılır.</td>
<td>FLEXİBLE SEGMENT, RIGID SEGMENT, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IEC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (hIfcRoorjl sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hate getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>IfeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfeRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmakladır.</td>
</tr>
</tbody>
</table>

## Tablo 6.28 IfcDuctSilencer Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Kanal Susturucusu (I1fcDuctSilencer)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kanal susturucusu, tipik olarak bir kanal dağıtım sistemine, hava hareketi, fan gürültüsü vb. kaynaklı gürültü seviyelerini bitişik alanda veya susturucu cihazın aşağı akışında azaltmak amacıyla monte edilen bir cihazdır.</td>
<td>FLATOVAL, RECTANGULAR, ROUND, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (|(IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş önek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;ife System</td>
<td>Metin |</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örmeğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.29 IfcElectricAppliance Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Elektrikli Cihaz (IfeElectricAppliance)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Elektrikli cihaz, elektrikle çalışan ve tüketici kullanımına yönelik bir aygıttır.</td>
<td>DISH WASHER, ELECTRIC COOKER, FREE STANDING ELECTRİC HEATER, FREE STANDING FAN, FREE STANDING WATER COOLER, FREE STANDING WATER HEATER, FREEZER, FRIDGE FREEZER, HAND DRYER, KITCHEN MACHİNE, MICROWAVE, PHOTOCOPTLER, REFRİGERATOR, TUMBLE DRYER, VENDİNG MACHİNE, WASHING MACHINE, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootjj| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir ömeğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. ii</td>
</tr>
</tbody>
</table>

| | | | 7 oe

## Tablo 6.30 IfcElectricGenerator Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Elektrik Jeneratörü (IfcElectricGenerator)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Elektrik jeneratörü, mekanik enerjiyi elektrik enerjisine dönüştüren bir makine olan bir motordur.</td>
<td>CHP, ENGINEGENERATOR, STANDALONE, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IEC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;fc System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

## Tablo 6.31 IfcEvaporator Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi |</td>
</tr>
<tr>
<td colspan="4">Evaporatör (JfeKvaporator)</td>
<td>Ön Tanımlı Tip Listesi |</td>
</tr>
<tr>
<td colspan="4">Tanım: Evaporatör, sıvı haldeki bir soğutucu akışkanın buharlaştığı ve çevresindeki akışkandan 151 emdiği bir cihazdır.</td>
<td>DİRECT EXPANSJON, DİRECT EXPANSION SHELL AND | TUBE, DİRECT EXPANSION TUBE IN TUBE, DİRECT | EXPANSION BRAZED PLATE, FLOODED SHELL AND TUBE, | SHELL AND CGOTL, USERDEFİNED, NOTDEFİNED i</td>
</tr>
<tr>
<th>“Türkçe Tanım” (Bilgi Amaçlı) *</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>- (Bilgi Amaçlı) &gt;”</th>
<th>Açıklama</th>
</tr>
<tr>
<td>,Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>” Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IEC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanımak üzere isteğe bağlı bir ad. ((IfcRooti) sınıfının bazı alt tipleri için isim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>, Atiribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş ömek düzeyindeki &#x27;tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>WeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfeProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, HeRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td>- (Bilgi Amaçlı)</td>
<td>©Özelik ©</td>
<td>(Özellik Seti/ İlişki©</td>
<td>&gt; (Bilgi Amaçlı)”</td>
<td>00Am e</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpt on</td>
<td>PsetEleciricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.32 IfcFan Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Fan (IfcFan)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Fan, bir gaza mekanik iş uygulayan bir cihazdır. Bir fanın tipik kullanımı, bina servisleri hava dağıtım sisteminde hava akışı sağlamaktır.</td>
<td>CENTRIFUGAL AIR FOIL, CENTRIFUGAL BACKWARDI NCLINED CUÜRVED, CENTRIFUGAL FORWARD CURVED, CENTRIFUGAL RADIAL, PROPELLOR AXIAL, TUBE AXIAL, VANE AXJAL, USERDEFINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((ifcRootj| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK- 5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örmeğindeki etiket tanımlayıcısı, ömeğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>IfeRelAssignsToGroup&gt;lfe System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nominal Toplam Basınç</td>
<td>Nominal&#x27;TotalPressure</td>
<td>PsetFanTypeCommon</td>
<td>Sayı</td>
<td>Fan boyunca nominal toplam basınç artışı.</td>
</tr>
<tr>
<td>Nominal Hava Debisi</td>
<td>NominalAirFlowRate</td>
<td>PsetFanTypeCommon</td>
<td>Sayı</td>
<td>Nominal hava debisi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.33 IfcFireSuppressionTerminal Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Yangın Söndürme Terminali (IfcFireSuppressionTerminal)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Yangın söndürme terminali, bir yangını söndürecek akışkanı (gaz veya sıvı) iletme amacına sahiptir. Yangın söndürme terminali, bir boru sistemiyle bağlantılı olan ve yangını söndürme görevini yerine getirmek üzere tasarlanan tüm sprinkler, dağıtıcı ve diğer terminal biçimlerini kapsar.</td>
<td>BREECHINGI NLET, FIRE HYDRANT, FIRE MONITOR, HOSEREEL, SPRINKLER, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((ifcRoot)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5*e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örmeğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örmek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, JfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

{ i

## Tablo 6.34 IfcFooting Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Temel (IfcFooting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Temel pabucu, bir yapının yükünü yayarak toprağa ileten bir yapı parçasıdır. Temel pabucu, yüklerin yüzeye yakın bir alana aktarıldığı sığ temel olarak da tanımlanır.</td>
<td>CAISSON FOUNDATION, FOOTING BEAM, PAD FOOTING, PİLE CAP, STRIP FOOTING, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootjj sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örmek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute (IfeRelAssociatesMaterial &gt;IfcMaterial): Name*</td>
<td>-</td>
<td>ll Metin</td>
<td>(fcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Atiribute (1fcRelAssociatesMateria)&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.35 IfcFurniture Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Mobilya (IfcFurniture)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Mobilya, binanın yapısına sabitlenmiş ya da sabitlenmemiş masa, sandalye, dolap gibi tefriş elemanlarını ifade eder.</td>
<td>BED, CHAIR, DESK, FILE CABINET, SHELF, SOFA, TABLE, TECHNICAL CABINET, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootjj sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
</tbody>
</table>

## Tablo 6.36 IfcGridAxis Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Aks (IfeGridAxis)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Tekil bir aks, 1f6GridAxis, bir tasarım aks sistemi bağlamında tanımlanır. Aks tanımı, iki boyutlu (2D) bir eğriye dayanır. Grid aksı, IfcGrid (aks sistmei) tarafından tanımlanan konum koordinat sisteminin XY düzlemi içerisinde yer alır.</td>
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
<td>Aks Etiketi</td>
<td>Attribute: AxisTag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bu aks eksenine ait etiket veya isim.</td>
</tr>
</tbody>
</table>

| !

## Tablo 6.37 IfcGroup Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Grup (IfcGroup)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: IfcGroup, herhangi bir nesne grubunun genel bir temsilidir. Grup, nesnelerin mantıksal olarak bir araya getirildiği bir topluluktur. Grup nesnesinin kendisine ait bir konumu bulunmaz ve geometrik bir temsil içermez. Bu nedenle grup, geometrik veya topolojik özelliklere dayanmayan bir ilişkilendirme kapsamında değerlendirilir.</td>
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
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir.</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>| Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. |</td>
</tr>
</tbody>
</table>

| |

## Tablo 6.38 IfcHeatExchanger Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Isı Eşanjörü (IfcHeatExchanger)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Isı Eşanjörü, plaka veya gövde-boru tipi eşanjörler gibi, birbirine karışmayan ortamlar arasında ısı transferi sağlamak için kullanılan bir cihazdır.</td>
<td>PLATE, SHELLANDTUBE, USERDEFİINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5?e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>eRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

## Tablo 6.39 IfcLightFixture Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Aydınlatma Armatürü (MfcLightFixture)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Aydınlatma Armatürü, bir veya daha fazla lambayı ve isteğe bağlı olarak bu lambaların ışık yayımını kontrol eden, sınırlayan veya değiştiren cihazları barındırmak amacıyla tasarlanmış bir muhafazadır.</td>
<td>DIRECTION SOURCE, POINT SOURCE, SECURİTY LIGHTING, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRoofjl sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfeSystem</td>
<td>YeRelAssignsTaGroup&gt;lfe System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>&quot;Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Nor: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

## Tablo 6.40 IfcMember Sınıfi Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Eleman (IfcMem ber)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: ((1feMemberJ), destek noktaları arasında veya ötesinde yük taşımak üzere tasarlanmış yapısal bir elemandır. Taşıyıcı olması zorunlu değildir. Elemanın yönelimi (yatay, düşey veya eğimli olması) tanımı açısından önemli değildir ( ((1f4cBeam)J) ve ((4fcColumn))&#x27;un aksine). ((IfcMember)), mimari veye yapısal modelleme bakış açısından doğrusal bir yapısal elemanı temsil eder ve eğer daha özel olarak ((1fcBeamJ) veya ((IfcColumnjJl| olarak ifade edilemiyorsa kullanılmalıdır.</td>
<td>ARCH SEGMENT, BRACE, CHORD, COLLAR, MEMBER, MULLION, PLATE, POST, PURLIN, RAFTER, STAY CABLE, STIFFENING RIB, STRINGER, STRUCTURALCABLE, STRUT, STUD, SUSPENDER, SUSPENSION CABLE, TIEBAR, USERDEFINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (fIfcRootl)| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir.</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş ömek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelA ssociates Material&gt;IfcMaterial): Name”</td>
<td>-</td>
<td>Metin</td>
<td>IIfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExtemal</td>
<td>PsetMemberCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">&quot;Attribute:&quot;: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik 5355 Beton C25)</td>
</tr>
</tbody>
</table>

i

## Tablo 6.41 IfcOpeningElement Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Açıklık Elemanı ((fcOpeningElement)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Açıklık elemanı; açıklık, girinti veya tesisat kanalı gibi boşlukları temsil eder. Fiziksel bir yapı elemanı içinde yer alan bir boşluğu ifade eder. Açıklıklar duvarlara. döşemelere, kirişlere, kolonlara veya diğer elemanlara yerleştirilebilir.</td>
<td>OPENİNG, RECESS, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.42 IfçOutlet Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Priz (IfcOutlet)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Priz, elektrik enerjisi veya iletişim için bir veya birden fazla fişin takılmasını sağlamak amacıyla belirli bir noktaya monte edilen bir cihazdır.</td>
<td>AUDIO VİSUAL OUTLET, COMMUNICATIONS OUTLET, DATA OUTLET, POWER OUTLET, TELEPHONE OUTLET, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootjl sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;ife i System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduci örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

## Tablo 6.43 IfcPavement Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi |</td>
</tr>
<tr>
<td colspan="4">Asfalt (If”cPavement)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Yol veya diğer kaplamalı bir alanda, genellikle birden fazla tabakadan oluşan ve araçlar ya da yayalar tarafından gelen yükleri taşıyarak düzgün bir yüzey sağlayan yapı elemanı türüdür. NOT: ISO 6707-1&#x27;e göre tanım: yol, pist veya benzeri, taban zemini üzerinde yer alan yapı.</td>
<td>FLEXİBLE, RIGID, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım | (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootJ) sınıfının bazı alt tipleri için Isim niteliğinin eklenmesi gerekebilir. Bu, bir “where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute (fcRelAssociatesMaterial &gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(HcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td>Kaplama Malzemesi</td>
<td>Attribute: Material</td>
<td>Atiribyte(IfeRelAssociates Material&gt;ifcMaterialLaye rSerUsage&gt; IfeMaterialla yerSet&gt;/fcMaterialLayer): Material*</td>
<td>Metin</td>
<td>Katmanın oluşturulduğu malzemeye yönelik isteğe bağlı referans. Bu değerin boş bırakılması, katmanın malzeme içermediğini (örneğin hava boşluğu olduğunu) ifade etmez; yalnızca ilgili aşamada malzeme bilgisinin tanımlanmadığını gösterir.</td>
</tr>
<tr>
<td>Kaplama Kalınlığı</td>
<td>Atiribute: LayerThickness</td>
<td>Atribute(IfcRelAssociates Material&gt;IfeMaterialLaye rSerUsage&gt;/fcMaterialLa yerSei&gt;(feMaterialLayer): LayerThickness*</td>
<td>Metin</td>
<td>Malzeme katmanının okalınlığıdır. “Kalınlık” teriminin anlamı, kullanımına bağlı olarak değişir. ifcMaterialLayerSetUsage kullanan yapı elemanlarında, bu boyut IfcMaterialLayerSetUsage içinde belirtilen pozitif LayerSetDirection doğrultusunda ölçülür. NOT: Zar (membran) gibi kalınlığı sıfıra çok yakın olan malzemeler için bu öznitelik değeri 0 olabilir. Kalınlığı 0 olan malzeme katmanları geometrik gösterimde görüntülenmeyebilir.</td>
</tr>
<tr>
<td rowspan="3"></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
<tr>
<td colspan="4">&quot;Attribute:”: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Atribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.44 IfcPile Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="3">Kazık (IfcPile))</td>
<td colspan="2">Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="3">Tanım: Bir kazık, bir yükü desteklemek amacıyla yere dik olarak yerleştirilmiş ince bir ahşap, beton veya çelik yapısal elemandır. Ayrıca, yüklerin daha derin yer altı katmanlarına aktarılmasıyla karakterize edilen derin temele de kazık denir.</td>
<td colspan="2">BORED, DRIVEN, JETGROUTING, COHESION, FRICTION, SUPPORT, ÜSERDEFİINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td colspan="2">Ön Tanımlı Tip | PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRoofjl sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu. bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>,Malzeme</td>
<td>Atiribute(IfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(ifeMateriall, yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">&quot;Attribute:&quot;: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Aftiribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

Zorunlu Öznitelik ve Özellik Listesi |

## Tablo 6.45 IfcPipeFitting Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Boru Bağlantı Parçası (IfcPipeFitting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Boru bağlantı parçası, borulu akış dağıtım sisteminde bir bağlantı veya geçiş elemanıdır; boru segmentlerini birleştirmek için kullanılır ve akışkanın yönü veya debisi gibi akış özelliklerinde değişikliklere neden olur.</td>
<td>BEND, CONNECTOR, ENTRY, EXIT, JUNCTİON, OBSTRUCTION, TRANSITION, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootjJ| sınıfının bazı al tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örmek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt; fe System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen. işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct ömeğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmakladır.</td>
</tr>
</tbody>
</table>

## Tablo 6.46 IfcPipeSegment Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Boru Segmenti (IfcPipeSegment)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Boru segmenti, tipik olarak bir boru şebekesinin iki bölümünü birleştirmek için kullanılır.</td>
<td>CULVERT, FLEXIBLESEGMENT, RIGIDSEGMENT, GUTTER, SPOOL, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootj| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir ömeğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>.Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;fe System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım . (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nominal Çap</td>
<td>NominalDiameter</td>
<td>PsetPipeSegmentT&#x27;ypeCo mımon</td>
<td>Sayı</td>
<td>Nesnenin nominal çapı veya genişliği.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler /FC&#x27;ge ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.47 IfcPump Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Pompa (ifePump)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Pompa, akışkanlara veya çamurlara mekanik enerji aktararak bunların bir kanal veya boru sistemi içinde taşınmasını sağlayan ekipmandır. Pompanın tipik bir kullanımı, bina dağıtım sisteminde soğutulmuş su veya ısıtma sıcak suyunun dolaştırılmasıdır.</td>
<td>CIRCULATOR, END SUCTION, SPLIT CASE, SUBMERSİBLE PUMP, SUMP PUMP, VERTİICAL INLİNE, VERTİCAL TURBINE, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRoot)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Atiribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. o</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Akış Debisi Aralığı</td>
<td>FlowRateRange</td>
<td>PsetPumpTypeCommon</td>
<td>Metin</td>
<td>Belirtilen dirence karşı pompalanan akışkanın izin verilen hacim aralığı.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Nor: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

, i |

## Tablo 6.48 IfcRailing Sınıfi Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Korkuluk (IfcRailing)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Korkuluk, insan veya araç dolaşım alanlarının bitişiğinde ya da bazı mekân sınırlarında, duvarların yerine veya duvarları tamamlayıcı bir eleman olarak kullanılan çerçeve biçimindeki bir yapıdır. İnsanlara fiziksel destek sağlamak veya düşme ya da çarpışma sonucu oluşabilecek yaralanma ya da hasarları önlemek amacıyla tasarlanmıştır.</td>
<td>HAND RAIL, GUARD RAIL, BALUSTRADE, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (((fcRootjl sınıfının bazı alt tipleri için İsim nitetiğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı. örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
</tbody>
</table>

| |

## Tablo 6.49 [fcRamp Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Rampa (IfcRamp)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Rampa, farklı kotlardaki iki döşeme seviyesini birbirine bağlayan dikey bir geçiş yoludur ve insan dolaşımını sağlar. Ara bir döşeme plağı olarak bir sahanlık içerebilir. Bir rampa normalde basamak içermez.</td>
<td>STRAIGHT RUN RAMP, TWO STRAIGHT RUN RAMP, OUARTER TURN RAMP, TWO OUARTER TURN RAMP, HALF TURN RAMP, SPIRAL RAMP, USERDEFİNED, NOTDEFIİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>TEC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-S5e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş ömek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(fcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">&quot;Atiribute:&quot;: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Ömek:Çelik 5355 Beton C25)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.50 IfcRoad Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Yol (1IfcRoad)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Karayolları, caddeler, bisiklet ve yaya yolları dâhil ancak demiryolları hariç olmak üzere, bir yerden başka bir yere seyahati sağlamak amacıyla kara üzerinde inşa edilen bir güzergâhtır. Bir tesis türü olarak yol, yol projesinin bileşenleri için (örneğin tasarım, inşaat veya bakım gibi herhangi bir çalışma) proje yapısı hiyerarşisinde temel unsuru oluşturur.</td>
<td>BICYCLE CROSSING, BUS STOP, CARRIAGEWAY, CENTRAL ISLAND, CENTRAL RESERVE, HARD SHOULDER, İNTERSECTION, LAY-BY, PARKING BAY, PASSING BAY, PEDESTRIAN CROSSING, REFUGE ISLAND, ROAD SEGMENT, ROAD SIDE, ROAD SIDE PART, ROADWAY PLATEAU, ROUNDABOUT, SHOULDER, SIDEWALK, SOFT SHOULDER, TOLL PLAZA, TRAFFIC ISLAND, TRAFFIC LANE, USERDEFINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Malzeme</td>
<td>| Attribute(1feRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">&quot;Atiribute:&quot;: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Attribute (I1fcRelAssociatesMaterial&gt;IfeMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örmek:Çelik $355 Beton C25)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.51 IfcRoadPart Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Yol Parçası (IfcRoadPart) ,</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir yolun parçası.</td>
<td>BICYCLE CROSSING, BUS STOP, CARRIAGEWAY, CENTRAL ISLAND, CENTRAL RESERVE, HARD SHOULDER, INTERSECTİON, LAY-BY, PARKING BAY, PASSING BAY, PEDESTRIAN CROSSING, REFUGE ISLAND, ROAD SEGMENT, ROAD SIDE, ROAD SİDE PART, ROADWAY PLATEAU, ROUNDABOLUT, SHOULDER, SIDEWALK, SOFT SHOULDER, TOLL PLAZA, TRAFFIC ISLAND, TRAFFIC LANE, USERDEFINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRoot)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelA ssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfeMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">&quot;Attribute:&quot;: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

i

## Tablo 6.52: IfeRoof Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Çatı (IfcRoof)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Çatı, bir binanın en üst kısmını örten yapı elemanıdı; binayı hava koşullarının etkilerine karşı korur.</td>
<td>FLAT ROOF, SHED ROOF, GABLE ROOF, HIP ROOF, HIPPED GABLE ROOF, GAMBREL ROOF, MANSARD ROOF, BARREL ROOF, RAINBOW ROOF, BUTTERFLY ROOF, PAVILION ROOF, DOME ROOF, FREEFORM, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir ömeğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>Pset_RoofCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Yangın Dayanım Sınıf</td>
<td>FireRating</td>
<td>Pset_RoofCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
</tbody>
</table>

| '

## Tablo 6.53 IfcSanitaryTerminal Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Sıhhi Terminal (IfcSanitaryTerminal)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Sıhhi terminal, genellikle su ile beslenen ve içme, temizlik veya atık suyun uzaklaştırılması için kullanılan sabit bir cihaz veya terminaldir ya da böyle bir cihaz veya terminal ile doğrudan kullanılan bir ekipman öğesidir.</td>
<td>BATH, BIDET, CISTERN, SHOWER, SINK, SANITARY FOUNTAIN, TOILET PAN, URINAL, WASH HAND BASIN, WC SEAT, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootl) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. il</td>
</tr>
</tbody>
</table>

| |

Zorunlu Öznitelik ve Özellik Listesi |

## Tablo 6.54 IfcSign Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Tabela (IfcSign)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Levha (tabela), yazılı, sembolik veya başka bir biçimde bilgi ya da talimat veren görsel bir bildirimdir. Tabelalar pasiftir; en yaygın biçimi görsel panodur. IfçSign örneği, duvar gibi bir yüzeye uygulanan bir panelin yerleştirilmiş veya bir Sinyal Bileşimi içinde toplanan birden fazla tabela örneği yerleştirilmesini ve ilgili taşıyıcı yapısal elemanlarını ifade eder.</td>
<td>MARKER, PICTORAL, MIRROR, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRoot)| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Atiribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
</tbody>
</table>

## Tablo 6.55 IfcSite Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Saha (IfcSite)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Saha, projenin inşaatının gerçekleştirileceği, suyla kaplı olabilecek sınırları belirli bir kara alanıdır. Bir saha, bina inşa etmek, mevcut yapıları yenilemek veya yıkmak ya da diğer inşaatla ilgili geliştirme faaliyetleri için kullanılabilir.</td>
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
<td>Attribute:ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFİNEDJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve (lfcBuiltElementi|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Uzun İsim</td>
<td>Attribute:LongName</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute:Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((fcRootjJ sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Referans Kotu</td>
<td>Attribute:RefElevation</td>
<td>-</td>
<td>Sayı</td>
<td>Deniz seviyesine göre referans (datum) kotudur.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Kat Alanı Oranı</td>
<td>FloorAreaRatio</td>
<td>Pset_SiteCommon</td>
<td>Sayı</td>
<td>Yerel imar yönetmeliklerine (Planlı Alanlar İmar Yönetmeliğine) göre belirlenen. toplam kat alanının yapılaşabilir alana oran: olarak ifade edilen azami kat alanı kullanım oranıdır.</td>
</tr>
<tr>
<td>Saha Kapsama Oranı</td>
<td>SiteCoverageRatio</td>
<td>Pset_SiteCommon</td>
<td>Sayı</td>
<td>Kullanım oranı, |((ToplamAlan|| / ((YapılaşabilirAlan|) biçiminde azami bir değer olarak ifade edilir. Bu oran değeri, |(YapılaşabilirAlan)T&#x27;ın türetilmesinde kullanılabilir.</td>
</tr>
<tr>
<td>Toplam Alan</td>
<td>TotalArea</td>
<td>Pset_SiteCommon</td>
<td>Sayı</td>
<td>Arsaya ilişkin toplam planlanan alandır. Arsa alanının programlanması amacıyla kullanılır.</td>
</tr>
<tr>
<td>Adres Satırları</td>
<td>AddressLines</td>
<td>Pset_Address</td>
<td>Metin</td>
<td>Posta adresidir. NOT: Bir posta adresi kaydedilirken birden fazla satır (veya öğe) içerebilir. Normal kullanımda, aşağıdaki adres kavramlarının ilgili unsurlarını</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>içermesi beklenir: Bina içindeki konum (ör. 3. Kat) Bina adı (ör. Interoperability House) Bina numarası (ör. 6400) Sokak adı (ör. Alliance Boulevard) Adres satırlarının tipik içeriği ülkeden ülkeye değişiklik gösterebilir.</td>
</tr>
<tr>
<td>İl / Kasaba</td>
<td>Town</td>
<td>Pset_Address</td>
<td>Metin</td>
<td>Bir kasaba veya şehrin adıdır.</td>
</tr>
<tr>
<td>Bölge/ İlçe</td>
<td>Region</td>
<td>Pset_Address</td>
<td>Metin</td>
<td>Bir bölge veya ilçenin adıdır.</td>
</tr>
<tr>
<td>Parsel Numarası</td>
<td>LandID</td>
<td>Pset_LandRegistration</td>
<td>Metin</td>
<td>Yasal tescil makamı tarafından bir taşınmaz parseline atanan kimlik numarasıdır.</td>
</tr>
<tr>
<td>“Tapu Numarası</td>
<td>LandTitleID</td>
<td>Pset_LandRegistration</td>
<td>Metin</td>
<td>Yasal tescil makamı tarafından bir taşınmaz parseline ait tapuya atanan kimlik numarasıdır.</td>
</tr>
<tr>
<td></td>
<td>TAKS</td>
<td>TREpys_ParselOzellikSeti</td>
<td>Sayı</td>
<td>Taban Alanı Kat Sayısı&#x27;nı ifade eder.</td>
</tr>
<tr>
<td></td>
<td>KAKS</td>
<td>TREpys_ParselOzellikSeti</td>
<td>Sayı</td>
<td>,Kat Alanı Kat Sayısı&#x27;nı ifade eder.</td>
</tr>
<tr>
<td></td>
<td>CekmeOn</td>
<td>TREpys_ParselOzellikSeti</td>
<td>Sayı</td>
<td>&#x27;Ön bahçe mesafesi: Yapı ile parselin ön sınırı arasındaki yatay uzaklıktır.</td>
</tr>
<tr>
<td></td>
<td>CekmeYan</td>
<td>TREpys_ParselOzellikSeti</td>
<td>Sayı</td>
<td>Yan bahçe mesafesi: Yapı ile parselin yan sınırları arasındaki yatay uzaklıktır.</td>
</tr>
<tr>
<td></td>
<td>CekmeArka</td>
<td>TREpys_ParselOzellikSeti</td>
<td>Sayı</td>
<td>Arka bahçe mesafesi: Yapı ile parselin arka sınırı arasındaki yatay uzaklıktır.</td>
</tr>
</tbody>
</table>

| | |

| | |

## Tablo 6.56 IfcSlab Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Döşeme (IfcSlab)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Döşeme, düşey olarak bir hacmi kapatabilen yapı bileşenidir. Döşeme, alt taşıyıcıyı (kat döşemesi) veya üst katı (çatı döşemesi) sağlayabilir ve bir binadaki herhangi bir mekânda yer alabilir.</td>
<td>APPROACH SLAB, BASE SLAB, FLOOR, LANDING, PAVING, ROOF, SIDEWALK, TRACK SLAB, WEARING, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootJJ sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5”e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociatesMaterial&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(HfcMateria!J), Elemanlar (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>Pset_SlabCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>Pset_SlabCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmaşına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi_Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik_S355 Beton_C25)</td>
</tr>
</tbody>
</table>

| ;

## Tablo 6.57 IfcSolarDevice Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Güneş Enerjisi Cihazı (IfcSolarDevice)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Güneş enerjisi cihazı, güneş radyasyonunu elektrik akımı veya ısıl enerji gibi diğer enerji türlerine dönüştürür.</td>
<td>SOLAR COLLECTOR, SOLAR PANEL, USERDEFİINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>(IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK -5&#x27;e göre isimlendiritecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı. örmeğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfeSystem</td>
<td>HfeRelAssignsToGroup&gt;lfe System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct ömeğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

| ' l

## Tablo 6.58 IfcSpace Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Mahal (IfcSpace)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir mahal, gerçek veya varsayımsal olarak sınırlandırılmış bir alanı veya hacmi temsil eder. Mekanlar, bir bina içinde belirli işlevleri yerine getiren alanlar veya hacimlerdir.</td>
<td>SPACE, PARKING, GFA, INTERNAL, EXTERNAL, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootjj sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Zemin Kaplaması</td>
<td>FloorCovering**</td>
<td>Pset_SpaceCoveringRequirements</td>
<td>Metin</td>
<td>Mahal döşemesi için malzemeyi veya bitişi belirtmek amacıyla kullanılan etiket. Etiket, mahal listesi (room book) bilgileri için kullanılır ve genellikle mahal kaşesinde gösterilir. Malzeme bilgisi, kendi şekil gösterimine ve malzeme atamasına sahip bir IfeCovering (typesFLOORING) nesnesinin bulunmaması durumunda sağlanır. Tutarsızlık halinde If6Covering elemanlarına atanmış malzeme dikkate alınır.</td>
</tr>
<tr>
<td>Zemin Kaplama Kalınlığı</td>
<td>FloorCoveringThickness**</td>
<td>Pset_SpaceCoveringRequirements</td>
<td>Sayı</td>
<td>Mahal döşemesine âit malzeme katman(lar)ının o kalınlığı. Kalınlık bilgisi, kendi şekil gösterimine sahip bir IfcCovering (type-FLOORING) nesnesinin bulunmaması durumunda sağlanır. Atanmış bir IfcCovering”in geometrik parametreleri ile bu özelliğe bağlı değer arasında tutarsızlık olması durumunda geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Duvar Kaplaması</td>
<td>WallCovering**</td>
<td>Pset_SpaceCoveringRequirements</td>
<td>Metin</td>
<td>Mahal duvar kaplaması için malzeme veya bitişi belirtmek amacıyla kullanılan etiket. Etiket, mahal listesi bilgileri için kullanılır ve genellikle mahal kaşesinde gösterilir. Malzeme bilgisi, kendi şekil gösterimine ve malzeme atamasına sahip bir IMeCovering (type-CLADDING) nesnesinin bulunmaması durumunda sağlanır. Tutarsızlık halinde IfcCovering elemanlarına atanmış malzeme dikkate alınır.</td>
</tr>
<tr>
<td>Duvar Kaplama Kalınlığı</td>
<td>WallCoveringThickness**</td>
<td>Pset_SpaceCoveringRequirements</td>
<td>Sayı</td>
<td>Mahal duvar kaplamasına ait malzeme katman(lar)ının kalınlığı. Kalınlık bilgisi, kendi şekil gösterimine sahip bir IfcCovering (iype-CLADDING) nesnesinin bulunmaması durumunda sağlanır. Atanmış bir IfcCovering&#x27;in geometrik parametreleri ile bu özelliğe bağlı değer arasında tutarsızlık olması durumunda geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Tavan Kaplaması</td>
<td>CeilingCovering**</td>
<td>Pset_SpaceCoveringRequirements</td>
<td>Metin</td>
<td>Mahal tavanı için malzeme veya bitişi belirtmek amacıyla kullanılan etiket. Etiket, mahal listesi bilgileri için kullanılır ve genellikle mahal kaşesinde gösterilir. Malzeme bilgisi, kendi şekil gösterimine ve malzeme atamasına sahip bir HfeCovering (iype&gt;CEILING) nesnesinin bulunmaması durumunda sağlanır. Tutarsızlık halinde ifeCovering elemanlarına atanmış malzeme dikkate alınır.</td>
</tr>
<tr>
<td>Tavan Kaplama Kalınlığı</td>
<td>CeilingCoveringThickness**</td>
<td>Pset_SpaceCoveringRequirements</td>
<td>Sayı</td>
<td>Mahal tavanına ait malzeme katman(lar)ının kalınlığı. Kalınlık bilgisi, kendi şekil gösterimine sahip bir IfcCovering (type=CEILING) nesnesinin bulunmaması durumunda sağlanır. Atanmış bir IfcCovering&#x27;in geometrik parametreleri ile bu özelliğe bağlı değer arasında tutarsızlık olması durumunda geometrik parametreler dikkate alınır..</td>
</tr>
<tr>
<td rowspan="3"></td>
<td colspan="4">** Kaplamalarla ilgili bu özellikler: (1) IfcSpace içindeki tanımlardan faydalanılarak yada (2) IfcCovering&#x27;de belirtilen ilişkiler kurularak doğrudan modelleme ile tanımlanacak. Bu nedenle belirtilen bu iki yöntemden biri zorunludur.</td>
</tr>
<tr>
<td colspan="4">&quot;Attribute:&quot;: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi_Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik_S355 Beton_C25)</td>
</tr>
</tbody>
</table>

| | , l | |

## Tablo 6.59 IfcSpaceHeater Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Mekan İstıcısı (IfcSpaceHeater)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Mekân ısıtıcıları, sınırlı bir mekânı veya alanı ısıtmak için elektrik, buhar veya sıcak su gibi bir ısıtma kaynağı kullanarak ışınım (radyasyon) ve/veya doğal konveksiyon kombinasyonundan yararlanır. Mekân ısıtıcılarına örnek olarak radyatörler, konvektörler, süpürgelik tipi ısıtıcılar ve kanatlı borulu ısıtıcılar verilebilir.</td>
<td>CONVECTOR, RADIATOR, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((IfcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>HeRelAssignsToGroup&gt;Ife System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Çıkış Kapasitesi</td>
<td>OutputCapacity</td>
<td>PsetSpaceHeaterTypeCo mmon</td>
<td>Sayı</td>
<td>Üretici tarafından listelenen toplam nominal ısı çıkışı.</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

## Tablo 6.60 IfcSpatialZone Simfi Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Mekansal Zon (IfcSpatialZone)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Mekansal zon, belirli bir işlevsel amaca göre projenin hiyerarşik olmayan ve potansiyel olarak örtüşebilen bir alt bölümlenmedir. Mekânsal zonlar örneğin bir ısı bölgesi. inşaat bölgesi, aydınlatma bölgesi veya kullanılabilir alanı temsil etmek için kullanılabilir. Bir mekansal zon, kendi konumlandırmasına ve biçim (geometri) temsiline sahip olabilir.</td>
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
<td>Attribute:Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Uzun İsim</td>
<td>Attribute:LongName</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. |(IfcRootJ) smıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>EmsalDurumu</td>
<td>TREpys_EmsalOzellikSeti</td>
<td>Metin</td>
<td>İlgili mekansal zon, emsale dahil alanı temsil etmesi halinde &#x27;DAHIL”, emsal dışı alanı temsil etmesi halinde “HARIC, ilgili idarenin özel imar düzenlemelerine bağlı olarak, emsal artışı alanı temsil etmesi halinde &#x27;DIGER&#x27; girilir. DİGER olması durumunda açıklama &quot;Attribute: Description&quot; bölümüne girilir.</td>
</tr>
</tbody>
</table>

## Tablo 6.61 IfcStair Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Merdiven (IfcStair)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Merdiven, kullanıcıların bir döşeme seviyesinden diğerine yürüyerek (adım atarak) çıkmasına/ inmesine imkân tanıyan düşey bir geçiş yoludur. Ara kat döşemesi gibi bir sahanlık içerebilir.</td>
<td>STRAIGHT RUN STAIR, TWO STRAIGHT RUN STAIR, QUARTER WINDING STAIR, QUARTER TURN STAIR, HALF WINDING STAIR, HALF TURN STAIR, TWO QUARTER WINDING STAIR, TWO QUARTER TURN STAIR, THREE QUARTER WINDING STAIR, THREE QUARTER TURN STAIR, SPIRAL STAIR, DOUBLE RETURN STAIR, CURVED RUN STAIR, TWO CURVED RUN STAIR, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((HcRootjJ sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociatesMaterial&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(fcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>Pset_StairCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td>Acil Çıkış</td>
<td>FireExit</td>
<td>Pset_StairCommon</td>
<td>Mantıksal</td>
<td>Bu nesnenin yangın durumunda çıkış olarak kullanılmak üzere tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir. Burada, ulusal bina yönetmeliğine uygun olarak bir acil çıkış merdiveni tanımlanmaktadır.</td>
</tr>
<tr>
<td colspan="5">İvAttribute:&quot;; Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi_Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik_S355 Beton_C25)</td>
</tr>
</tbody>
</table>

i , _

## Tablo 6.62 IfcTank Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Tank (IfcTank)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Tank, sıvı veya gazın daha sonra kullanılmak üzere depolandığı bir kap ya da haznedir.</td>
<td>BASIN, BREAK PRESSURE, EXPANSION, FEED AND EXPANSION, OILRETENTION TRAY, PRESSURE VESSEL, STORAGE, VESSŞEJ, USERDEFIİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((fcRootj)| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Tank Nominal Kapasitesi</td>
<td>TankNominalCapacity</td>
<td>PsetTankTypeCommon</td>
<td>Sayı</td>
<td>Tankın toplam nominal veya tasarım hacmi.</td>
</tr>
</tbody>
</table>

, |

## Tablo 6.63 IfcTransformer Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="5">Transformatör (IfcTransformer) | Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Transformatör, elekirik enerjisini bir devreden başka bir devreye aktaran, endüktif ve sabit bir cihazdır.</td>
<td>CURRENT, FREOÇUENCY, INVERTER, RECTİFLER, VOLTAGE, USERDEFINED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (|I£cRootj)| sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Maksimum Görünen Güç</td>
<td>MaximumApparentPower</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Transformatörün maksimum görünen gücü (veya kapasitesi), VA (volt- amper) cinsinden ifade edilir.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.64 IfcTransportElement Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Taşıma Elemanı (IfcTransportElement)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Taşıma elemanı, bir bina veya bina kompleksi içinde insanları, hayvanları veya eşyaları taşıyan tüm ulaşım ile ilgili nesnelerin genelleştirilmiş halidir. Taşıma elemanı, (varsa) IfeTransportElementType tarafından tanımlanan bir taşıma elemanının yerleştirilmiş örneğini ifade eder.</td>
<td>ELEVATOR, ESCALATOR, MOYING WALKWAY, CRANEWAY, LIFTING GEAR, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5?e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>İnsan Kapasitesi</td>
<td>CapacityPeople</td>
<td>PsetTransportElementCommon</td>
<td>Sayı</td>
<td>Taşıma elemanının kapasitesi, kişi sayısı cinsinden ölçülür.</td>
</tr>
<tr>
<td>Ağırlık Kapasitesi</td>
<td>Capacity Weight</td>
<td>PsetTransportElementCommon</td>
<td>Sayı</td>
<td>Taşıma elemanının kapasitesi, ağırlık cinsinden ölçülür.</td>
</tr>
</tbody>
</table>

## Tablo 6.65 IfcValve Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Vana (IfcValve)</td>
<td>Ön Tanımlı Tip Listesi !</td>
</tr>
<tr>
<td colspan="4">Tanım: Vana, bina tesisatı boru dağıtım sisteminde akışkanın akışını kontrol etmek veya düzenlemek için kullanılır.</td>
<td>AIR RELEASE, ANTI VACUUM, CHANGE OVER, CHECK, COMMISSIONING, DIVERTİNG, DRAW OFF COCK, DOUBLE CHECK, DOUBLE REGULATING, FAUCET, FLUSHING, GAS COCK, GAS TAP, ISOLATING, MIXING, PRESSURE REDUCING, PRESSURE RELIEF, REGULATING, SAFETY CUT OFF, STEAM TRAP, STOP COCK, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Atiribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak ,üzere İsteğe bağlı bir ad. |(IfcRootj) sınıfının bazı alt tipleri için İsim jniteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale “getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Sistem</td>
<td>IfcSystem</td>
<td>YeRelAssignsToGroup&gt;lfe System</td>
<td>Metin</td>
<td>Bir sistem, Mimarlık, Mühendislik ve Yapım ürünü içerisinde, ortak bir amaç, işlev ya da hizmet sunmak üzere bir araya getirilmiş ilişkili parçalardan oluşan düzenli bir kombinasyondur. Sistem esasen, işlevsel olarak ilişkili ürünler grubudur. Bir veya birden fazla IfcProduct örneğinin (sistem üyelerinin) gruplandırma ilişkisi, IMfcRelAssignsToGroup aracılığıyla yönetilir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Boyut</td>
<td>Size</td>
<td>PsetValveTypeCommon</td>
<td>Sayı</td>
<td>Vananın bağlantı boyutu (veya musluklar, karışım vanaları vb. için her bir bağlantının boyutu).</td>
</tr>
<tr>
<td></td>
<td colspan="4">Not: Bu parametreler IFC&#x27;de ilişkiler yoluyla kurgulanmaktadır.</td>
</tr>
</tbody>
</table>

| i

## Tablo 6.66 Ifc Wall Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="3">Duvar (IfcWall)</td>
<td colspan="2">Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="3">Tanım: Duvar, mekanları sınırlayabilen veya bölebilen düşey bir yapısal bileşendir. Duvarlar genellikle düşey veya düşeye yakın düzlemsel elemanlardır ve yapısal yükleri taşımak üzere tasarlanabilir. Ancak, taşıyıcı olmak zorunda değildir.</td>
<td colspan="2">ELEMENTED WALL, MOVABLE, PARAPET, PARTITIONING, PLUMBING WALL, POLYGONAL, RETAINING WALL, SHEAR, SOLIDWALL, STANDARD, WAVEWALL, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootj) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociatesMaterial&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterial|, yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>Pset_WallCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Yangın Dayanın Sınıfı</td>
<td>FireRating</td>
<td>Pset_WallCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">&quot;Attribute:&quot;: Standart bir IFC elemanının attribute (öznitelik) listesindeki özellikler</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi_Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik_S355 Beton_C25)</td>
</tr>
</tbody>
</table>

| | | |

## Tablo 6.67 IfeWindow Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Pencere (IfcWindow)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Pencere, esas olarak doğal ışık ve temiz hava sağlamak için kullanılan bir yapı elemanıdır. Düşey açıklıkları içerdiği gibi çatı pencereleri veya ışıklıklar gibi yatay açıklıkları da kapsar. Açılır, döner, kayar, döner kanatlı veya sabit panellerden oluşan yapıları içerebilir. Bir pencere, bir kasadan ve bir veya birkaç panelden oluşur.</td>
<td>WINDOW, SKYLIGHT, LIGHTDOME, USERDEFINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Ön Tanımlı Tip</td>
<td>PredefinedType</td>
<td>-</td>
<td>Metin</td>
<td>Ön Tanımlı Tip.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. (J1fcRoot)) sınıfının bazı alt tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-5&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir ömeğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş ömek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>Pset_WindowCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
</tbody>
</table>

| |

## Tablo 6.68 IfcZone Sınıfı Zorunlu Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Zorunlu Öznitelik ve Özellik Listesi</td>
</tr>
<tr>
<td colspan="4">Zon (IfcZone)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Zon, mekanların, kısmi mekanların veya diğer zonların gruplanmış halini ifade eder. Bu mekanlar bitişik veya bitişik olmayabilir. Bir zonun kendi geometrik biçim temsili yoktur. Zon yapıları hiyerarşik Oolmayabilir (bir projenin mekânsal yapısının aksine — bkz. SpatialStructureElement). Yani, tek bir mekân (Space), sıfır, bir veya birden fazla IfeZone ile ilişkilendirilebilir. Mekânlar, üst tür olan Group&#x27;ta tanımlanan IfcRelAssignsToGroup ilişkisi kullanılarak bir IfcZone içinde gruplanır. Örneğin, zon bir daireyi temsil mekanları gruplandırarak temsil etmek için kullanılabilir.</td>
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
<td>Uzun İsim</td>
<td>Atiribute:LongName</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı.</td>
</tr>
<tr>
<td>İsim</td>
<td>Attribute: Name</td>
<td>-</td>
<td>Metin</td>
<td>IFC uyumlu yazılım sistemleri veya kullanıcılar tarafından kullanılmak üzere isteğe bağlı bir ad. ((1fcRootJJ sınıfının bazı alı tipleri için İsim niteliğinin eklenmesi gerekebilir. Bu, bir &quot;where&quot; kuralı ile zorunlu hale getirilecektir. (EK-3&#x27;e göre isimlendirilecektir)</td>
</tr>
<tr>
<td>Nesne Tipi</td>
<td>Attribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. O) Ön Tanımlı Tip özniteliğinin değeri listeden &#x27;((USERDEFINEDJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa . İkinci durum, bazı istisnai &#x27;yaprak sınıflarında ve ((1fcBuiltElementi)&#x27;i doğrudan öreklendirirken &quot;geçerlidir.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.69 IfcAirTerminal Sınıfı İsteğe Bağlı Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Havalandırma Menfezi (IfcAirTerminal)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir havalandırma menfezi, dağıtım sistem(ler)i ile bir veya birden fazla mahal arasındaki hava transferinin başlangıç veya bitiş noktasıdır. Ayrıca, bitişik mekanlar arasında hava transferi için de kullanılabilir.</td>
<td>DIFFUSER, GRİLLE, LOUVRE, REGİSTER, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut ömeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa . İkinci durum, bazı istisnai yaprak sınıflarında ve /(IfcBuiltElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirici yorumlar paylaşmak için isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre. Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Üfleme Yönü</td>
<td>DischargeDirection</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Havalandırma menfezinin üfleme yönü. Paralel: montaj yüzeyine paralel şekilde üfleme yapar, akış yüzeye yapışacak şekilde tasarlanmıştır. Dik: montaj yüzeyinden uzağa doğru üfleme yapar. Ayarlanabilir: hem paralel hem de dik üfleme yapılabilir.</td>
</tr>
<tr>
<td>Efektif Alan</td>
<td>EffectiveArea</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Havalandırma menfezinin efektif üfleme alanı.</td>
</tr>
<tr>
<td>Havalandırma Menfezi Şekli</td>
<td>AirTerminalShape</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Havalandırma menfezinin şekli. Slot, genellikle en-boy oranı 10:1&#x27;den büyük olan uzun ve dar bir hava çıkış cihazıdır.</td>
</tr>
<tr>
<td>Yüzey Tipi</td>
<td>FaceType</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Havalandırma menfezinin ön yüzeyinin nasıl imal edildiğini belirtir.</td>
</tr>
<tr>
<td>Slot Genişliği</td>
<td>Slot Width</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Slot genişliği.</td>
</tr>
<tr>
<td>Slot Uzunluğu</td>
<td>SlotLength</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Slot uzunluğu.</td>
</tr>
<tr>
<td>Slot Sayısı</td>
<td>NumberOfSlots</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Slot sayısını belirtir.</td>
</tr>
<tr>
<td>Akış Patemi</td>
<td>FlowPatterm</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Akış paterni.</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum sıcaklık. Havalandırma menfezinin kullanım için tasarlandığı sıcaklık aralığı.</td>
</tr>
<tr>
<td>Hava Atış Mesafesi</td>
<td>ThrowLength</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Bir hava akımının, Hava Menfezi&#x27;nden çıktıktan o sonra. AirFlowrateRange&#x27;in üst değerinde ve izotermal koşullar altında, maksimum akış hızının belirli bir menfez hızına düşmesine kadar yatay veyâ düşey eksende kat ettiği mesafe. Verilen koşullar altında, bir cismin iki noktası arasındaki mesafenin (0), termodinamik sıcaklık (T) ile değişimini karakterize eden büyüklük (EC 115-04-27). Bu oran Kelvin başına tanımlanır.</td>
</tr>
<tr>
<td>Hava Dağılım Performans İndeksi</td>
<td>AirDiffusionPerforman celndex</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Hava Dağılımı Performans İndeksi (ADPTI). soğutma modu koşullarında kullanılır. Bir mekanın kullanılan zonunda hava hızı ve hava sıcaklığına ilişkin birden fazla ölçüm yapıldığında ADPI, bu ölçüm noktalarının efektif cereyan sıcaklığı ve hava hızı şartlarını karşılama yüzdesini ifade eder.</td>
</tr>
<tr>
<td>Kaplama Tipi</td>
<td>FinishType</td>
<td>PsetAirTermina!TypeCommon</td>
<td>Metin</td>
<td>Havalandırma menfezinin kaplama tipi.</td>
</tr>
<tr>
<td>Kaplama Rengi</td>
<td>FinishColour</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Nesnenin kaplama rengi.</td>
</tr>
<tr>
<td>Havalndırma Menfezi Montaj Tipi</td>
<td>AirTerminalMounting Type</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Havalandırma menfezinin tavana, duvara vb. nasıl monte edildiği. Yüzey: Bir yüzeye (ör. duvar, kanal) monte edilir. Düz ve gömme: Yüzeye düz ve gömme monte edilir. Asma tavan montajı: Asma tavan sistemine monte edilir (Asma tavan taşıyıcı sistemi).</td>
</tr>
<tr>
<td>Çekirdek Tipi</td>
<td>CoreType</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Havalandırma menfezinin iç çekirdeğinin nasıl imal edildiğini belirtir.</td>
</tr>
<tr>
<td>Kanat Yatay Açısı</td>
<td>CoreSetHorizontal</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>, Yatay (LocalPlacement X ekseninde) kanat açısı.</td>
</tr>
<tr>
<td>Kanat Dikey Açısı</td>
<td>CoreSetVertical</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Dikey (LocalPlacement Y ekseninde) kanat açısı.</td>
</tr>
<tr>
<td>SıcaklıkKontroludur</td>
<td>HaslntegralControl</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Mantıksal</td>
<td>DOĞRU ise, kendi enerjisini sağlayan sıcaklık kontrolü içerir.</td>
</tr>
<tr>
<td>Akış Kontrol Tipi</td>
<td>FlowControlType</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Metin</td>
<td>Havalandırma menfezinin entegre edilmiş olabilecek akış kontrol elemanının tipi.</td>
</tr>
<tr>
<td>Susturuculudur</td>
<td>HasSoundAttenuator</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Mantıksal</td>
<td>DOĞRU ise, nesne ses yalıtımı içerir.</td>
</tr>
<tr>
<td>Isı Yalıtımlıdır</td>
<td>HasThermallnsulation</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Mantıksal</td>
<td>DOĞRU ise, havalandırma menfezi ısı yalıtımı içerir.</td>
</tr>
<tr>
<td>Boğaz Alanı</td>
<td>NeckArea</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Havalandırma menfezinin boğaz alanı.</td>
</tr>
<tr>
<td>Hava Akış Hızı ve Akış Kontrol Elemanı</td>
<td>AirFlowrateVersusFlo wControlElement</td>
<td>PsetAirTerminalTypeCommon</td>
<td>Sayı</td>
<td>Nominal basınç düşümünde, hava debisinin akış kontrol elemanı konumuna göre değişimi. Nominal basınç farkında, hava terminalinden geçen hava debisinin akış kontrol elemanı konumuna göre değişim karakteristiği.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoAirTerminalBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Çevre</td>
<td>Perimeter</td>
<td>OtoAirTerminalBaseÇOuantities</td>
<td>Sayı</td>
<td>Elemanın çevresi.</td>
</tr>
<tr>
<td>Toplam Yüzey Alanı</td>
<td>TotalSurfaceArea</td>
<td>OtoAirTerminalBaseOuantities</td>
<td>Sayı</td>
<td>Elemanın toplam yüzey alanı. Hava menfezinin ön plakası ile ilgilidir.</td>
</tr>
<tr>
<td>Hava Akış Tipi</td>
<td>AirFlowType</td>
<td>PsetAirTerminalOccurrence</td>
<td>Metin</td>
<td>Açıklama mevcut değil.</td>
</tr>
<tr>
<td>Hava Debisi</td>
<td>AirFlowRate</td>
<td>Pset AirTerminal Occurrence</td>
<td>Sayı</td>
<td>Hava debisi. Tasarlandığı şekliyle gerçekleşen hava akış miktarı.</td>
</tr>
<tr>
<td>Havalandırma Menfezinin Lokasyonu</td>
<td>AirTerminallocation</td>
<td>PsetAirTerminalOccurrence</td>
<td>Metin l</td>
<td>Konum (tek bir difüzör tipi birden fazla konumda kullanılabilir); yüksek, tavan yakın: olduğunu ifade eder</td>
</tr>
</tbody>
</table>

i |

## Tablo 6.70 IfcAudioVisualAppliance Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Görüntü ve Ses Cihaz (IfcAudioV&#x27;isualAppliance)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir görüntü ve ses cihazı veya görüntüyü gösteren, kaydeden, ileten veya alan bir aygıttır.</td>
<td>AMPLIFIER, CAMERA, DISPLAY, MICROPHONE, PLAYER, PROJECTOR, RECEIYVER, SPEAKER, SWITCHER, TELEPHONE, TUNER, USERDEFİINED, NOTDEFINED</td>
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
<td>Atiribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değeri listeden NUSERDEFINEDİ| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirime amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumption</td>
<td>Pset Electrical DeviceCommon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetEleciricalDeviceCommon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>Pset Electrical DeviceConımon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>| GrossWeight</td>
<td>OtoAudioVisualApplianceBas eOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve oyuklar dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

, | | | '

## Tablo 6.71 IfcBeam Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kiriş (IfcBeam)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir Kiriş, genellikle yatay veya neredeyse yatay bir yapısal elemandır ve yükleri esas olarak eğilme taşıma gücü ile karşılar. Mimari açıdan böyle bir elemanı da temsil edebilir. Yük taşıyıcı olması gerekmez</td>
<td>BEAM, JOIST, HOLLOWCORE, LINTEL, SPANDREL, TBEAM, GIRDER SEGMENT, DIAPHRAGM, PIERCAP, HATSTONE, CORNİCE, EDGEBEAM, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden İLUSERDEFINEDJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement|)&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendime amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>|</td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>, Taşıyıcı</td>
<td>LoadBearing</td>
<td>Pset BeamCommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoBeamBaseOuantities</td>
<td>Sayı</td>
<td>.Nesnenin uzunluğu. Kesit boşluğu gibi imalat özellikleri dikkate alınmaz.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>.GrossWeight</td>
<td>OtoBeamBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat &#x27;detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>&#x27;NetWeight</td>
<td>OtoBeamBaseOuantities</td>
<td>i Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGen eral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengthClass</td>
<td>PsetConcreteElementGen era)</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
<tr>
<td>Beton Dayanım Sınıfı</td>
<td>SitrengthClass</td>
<td>PsetConcreteElementGen cral</td>
<td>Metin</td>
<td>Projede uygulanan beton tasarım standardına göre beton dayanımının sınıflandırması.</td>
</tr>
<tr>
<td>Eğim</td>
<td>Slope</td>
<td>Pset BeamCommon</td>
<td>Sayı</td>
<td>Eğim açısı — yataya göre relatif (0,0 derece). Şekil bilgisi, şekil temsilinin yanı sıra kullanılan geometrik parametrelerle birlikte sağlanır. Geometrik parametreler ile şekil özellikleri oarasında tutarsızlık Olması durumunda, geometrik parametreler dikkate alınır. Geometri düzenleme uygulamaları (ör. CAD) için bu değer yalnızca &quot;yazılabilir&quot; olmalıdır.</td>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExtemal</td>
<td>PsetBeamCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOGRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Kesit Alanı</td>
<td>CrossSectionArea</td>
<td>Oto, BeamBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin kesitinin (veya profilinin) toplam alanı.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>OtoBeamBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın), genellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td>Brüt Yüzey Alanı</td>
<td>GrossSurfaceArea</td>
<td>OtoBeamBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt alanı, genellikle çevre * uzunluk * 2 * Kesit Alanı olarak hesaplanır. Bu, Dış Yüzey Alanı * (2 x Kesit Alanı) toplamıdır ve yalnızca Dış Yüzey Alanı ve Kesit Alanı ayrı olarak belirlenemediğinde verilecektir.</td>
</tr>
<tr>
<td>Net Yüzey Alanı</td>
<td>NetSurfaceArea</td>
<td>OtoBeamBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin net yüzey alanı genellikle, olası imalat özelliklerini (kesit boşluğu vb.) veya açıklıkları ve girintileri dikkate alarak., çevre * uzunluk -2 * Kesit Alanı olarak hesaplanır.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>Gross Volume</td>
<td>OtoBeamBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoBeamBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özellikleri (kesit boşlukları vb.) veya açıklıklar ve girintiler dikkate alınarak hesaplanır.</td>
</tr>
</tbody>
</table>

| |

| l

## Tablo 6.72 IfcBoiler Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kazan (IfcBoiler)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kazan, doğal gaz, fuel-oil veya elektrik gibi bir enerji kaynağı kullanılarak suyun veya başka bir akışkanın ısıtıldığı, basınca dayanıklı kapalı bir basınçlı kaptır. Kazandaki akışkan daha sonra çeşitli süreçlerde veya ısıtma uygulamalarında kullanılmak üzere kazanın dışına sirküle edilir.</td>
<td>WATER, STEAM, USERDEFİNED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED|) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve /((1fcBuiltElementil&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Enerji Kaynağı</td>
<td>EnergySource</td>
<td>PsetBoilerTypeCommon</td>
<td>Metin</td>
<td>Yakıt kaynağını veya yakılan enerjiyi tanımlayan liste</td>
</tr>
<tr>
<td>Su Depolama Isıtıcısı</td>
<td>IsWaterStorageHeater</td>
<td>PsetBoilerTypeCommon</td>
<td>Mantıksal</td>
<td>Kazanın depolama kapasitesi olup olmadığını belirlemek için kullanılır. (DOĞRU) ise vardır, (YANLIŞ) ise, kazanda dahili bir depolama kapasitesi yoktur; örneğin anlık sıcak su ısıtıcısı gibi.</td>
</tr>
<tr>
<td>Su Girişi Sıcaklık Aralığı</td>
<td>WaterlnletTemperatureRange</td>
<td>PsetBoilerTypeCommon</td>
<td>Metin</td>
<td>İzin verilen su giriş sıcaklığı aralığı.</td>
</tr>
<tr>
<td>Su Depolama Kapasitesi</td>
<td>WaterStorageCapacity</td>
<td>PsetBoilerFypeCommon</td>
<td>Sayı</td>
<td>Su depolama kapasitesi</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumption</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedClurrent</td>
<td>PsetElectricalDeviceCommon</td>
<td>Metin</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>Pset Electrical DeviceCommon</td>
<td>Metin</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Isı Transfer Yüzey Alanı</td>
<td>HeatTransferSurfaceArea</td>
<td>PsetBoilerTypeCommon</td>
<td>Sayı</td>
<td>Kabın toplam ısı transfer alanı.</td>
</tr>
<tr>
<td>Nominal Kısmi Yük Oranı</td>
<td>NominalPartl.oadRatio</td>
<td>PsetBoilerTypeCommon</td>
<td>Sayı</td>
<td>İzin verilen kısmi yük oranı aralığı.</td>
</tr>
<tr>
<td>Çalışma Modu</td>
<td>OperatingMode</td>
<td>PsetBoilerTypeCommon</td>
<td>Metin</td>
<td>Kazanın çalışma modunu tanımlar.</td>
</tr>
<tr>
<td>Çıkış Sıcaklık Aralığı</td>
<td>OutletTemperatureRange</td>
<td>PsetBoilerTypeCommon</td>
<td>Sayı</td>
<td>Su veya buhar için izin verilen çıkış sıcaklığı.</td>
</tr>
<tr>
<td>Kısmi Yük N Verimlilik Eğrileri</td>
<td>Partiall.oadEfficiencyCurves</td>
<td>PsetBoilerTypeCommon</td>
<td>Sayı</td>
<td>Kazan verimliliği, kısmi yük faktörünün bir fonksiyonu olarak; E - #partialLoadFactor).</td>
</tr>
<tr>
<td>Basınç Sınıfı / Basınç Dayanımı</td>
<td>PressureRating</td>
<td>PsetBoilerTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin basınç dayanımı. Kazanın, yetkili kurum tarafından belirlenen nominal basınç sınıfıdır.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>GrossWeight</td>
<td>OtoBoilerBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır. İçerdiği sıvı miktarı dahil değildir.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>NetWWeight</td>
<td>OtoBoilerBaseÇuantities</td>
<td>Say:</td>
<td>Nesnenin toplam net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır. Tasarlandığı şekilde içerdiği sıvı dahil olmak üzere yapı elemanın ağırlığı.</td>
</tr>
<tr>
<td>Toplam Yüzey Alanı</td>
<td>TotalSurfaceArea</td>
<td>OtoBoilerBaseOuantities</td>
<td>Sayı</td>
<td>Elemanın toplam yüzey alanı.</td>
</tr>
</tbody>
</table>

|

, |

## Tablo 6.73 IfeBridge Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Köprü (1feBridge))</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Köprü, yayaların, hayvanların, araçların ve aityapı hizmetlerinin engellerin üzerinden veya yerden yüksekte bulunan iki nokta arasında geçişini sağlayan bir inşaat mühendisliği yapısıdır.</td>
<td>ARCHED, CABLE STAYED, CANTILEVER, CULVERT, FRAMEWORK, GIRDER, SUSPENSION, TRUSS, USERDEFINED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. (1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED|) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement)|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi. (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGeneral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmelikierine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında Kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengihClass</td>
<td>PsetConcreteElementGeneral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
</tbody>
</table>

İ İ | |

## Tablo 6.74 IfcBridgePart Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Köprü Parçası (IfcBridgePart)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir köprünün parçası.</td>
<td>ABUTMENT, DECK, DECK SEGMENT, FOUNDATION, PIER, PIER SEGMENT, PYLON, SUB STRUCTURE, SUPER STRUCTURE, SURFACE STRUCTURE, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu öznileliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değeri listeden (USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((1fcBuiltElement)l&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirici açıklamalar paylaşmak için isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys, PozÖzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGeneral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü. boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengthCla s5</td>
<td>PsetConcreteElementGeneral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
</tbody>
</table>

| | © l |

## Tablo 6.75 IfcBuilding Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Bina (JfcBuilding)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir bina, içindekilere veya içeriğine barınak sağlayan ve sabit bir konumda duran bir yapıyı temsil eder. Bina aynı zamanda, bir bina projesinin bileşenleri için (arsa, kat ve mahal ile birlikte) mekânsal yapı hiyerarşisinde temel bir eleman olarak kullanılır.</td>
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
<td>Atiribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİJ olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve /(IfcBuiltElementll&#x27;i doğrudan ömeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirici açıklamalar paylaşmak için isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoBuildingBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özellikleri (kesit boşluklarıvb.) veya açıklıklar ve girintiler dikkate alınarak hesaplanır. Binanın kapsadığı tüm mahallerin net hacimlerinin toplamıdır. Binadaki yapı elemanlarının hacimlerini içermez. Mekân metrajlarına ek olarak verilebilir. Tutarsızlık durumunda mekânların bireysel miktarları önceliklidir. :</td>
</tr>
<tr>
<td>Sprinkler Sistemi Koruması</td>
<td>SprinklerProtection</td>
<td>PsetBuildingCommon</td>
<td>Mantıksal</td>
<td>Bu nesnenin yağmurlama sistemiyle korunduğunu (DOĞRU) veya korunmadığını (YANLIŞ) belirtir. .</td>
</tr>
<tr>
<td>Sprinkler Sistemi Koruması Otomatiktir</td>
<td>SprinklerProtectionAutom atic</td>
<td>PsetBuildingCommon</td>
<td>Mantıksal</td>
<td>Bu nesnenin otomatik yağmurlama sistemiyle korunduğunu (DOĞRU) veya korunmadığını (YANLIŞ) belirtir. Yalnızca “SprinklerProtection&quot; özelliği DOĞRU ise belirtilmelidir.</td>
</tr>
<tr>
<td>Yapım Yılı</td>
<td>YearOfConstruction</td>
<td>PsetBuildinglommon</td>
<td>Mantıksal</td>
<td>Binanın inşa yılı, tamamlanması beklenen yılı da dahil eder.</td>
</tr>
<tr>
<td>Son Yenileme Yılı</td>
<td>YearOfLastRefurbishment</td>
<td>PsetBuildinglommon</td>
<td>Manüksal</td>
<td>Binanın son büyük yenileme veya yeniden yapım yılı (yeniden inşa işlemleri için geçerlidir).</td>
</tr>
<tr>
<td>Tescilli Yapı Durumu</td>
<td>IsLandmarked</td>
<td>PsetBuildingCommon</td>
<td>Mantıksal</td>
<td>Bu binanın tescilli bir tarihi yapı olduğunu (DOĞRU), olmadığını (YANLIŞ) veya bilinmediğini belirtir.</td>
</tr>
<tr>
<td>Referans Kotu</td>
<td>ElevationOfRefHeight</td>
<td>PsetBuildingCommon</td>
<td>Sayı</td>
<td>Tüm kat kotu ölçümleri için kullanılan referans yüksekliğin deniz seviyesine göre kotu; yükseklik 0.0&#x27;a eşittir. Genellikle zemin kat seviyesidir.</td>
</tr>
<tr>
<td>Arazi Kotu</td>
<td>ElevationOfTerrain</td>
<td>PsetBuildingCommon</td>
<td>Sayı</td>
<td>Binanın oturum alanı çevresindeki en düşük arazi seviyesinin deniz seviyesine göre yüksekliğidir.</td>
</tr>
<tr>
<td>İç Konum</td>
<td>IntemalLocation</td>
<td>Pset Address</td>
<td>Metin</td>
<td>Bir organizasyon tarafından, kurum içi posta teslimatı amacıyla tanımlanan adres.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>Gross Volume</td>
<td>OtoBuildingBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz. Kapsanan tüm mahallerin brüt hacimlerinin toplamıdır. Eleman içindeki yapı elemanlarının hacimlerini içerir. Mekân ve yapı elemanı miktarlarına ek olarak verilebilir. Tutarsızlık durumunda mekân ve yapı elemanlarının bireysel miktarları önceliklidir.</td>
</tr>
<tr>
<td>Pazar Kategorisi</td>
<td>MarketCategory</td>
<td>PsetBuildingÜse</td>
<td>Metin</td>
<td>Kullanım kategorisi; örneğin konut, ticari, rekreasyon vb.</td>
</tr>
<tr>
<td>Pazar Alt Kategorisi</td>
<td>MarketSubCategory</td>
<td>PsetBuildingüse</td>
<td>Metin</td>
<td>Kullanım kategorisinin alt kümesi; örneğin çok aileli/birimli, 2 odalı, alçak katlı vb.</td>
</tr>
<tr>
<td>Posta Kodu</td>
<td>PostalCode</td>
<td>Pset Address</td>
<td>Metin</td>
<td>Ülkenin posta servisi tarafından kullanılan kod.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.76 IfcBuildingStorey Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Bina Katı (IfcBuildingStorey)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bina katı bir kota sahiptir ve genellikle düşeyde sınırlanmış, (ncredeyse) yatay bir mahal grubunu temsil eder.</td>
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
<td>Uzun İsim</td>
<td>Attribute:LongName</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı.</td>
</tr>
<tr>
<td>Bileşim Türü</td>
<td>Attribute: CompositionType</td>
<td>-</td>
<td>Metin</td>
<td>Önceden tanımlı mekânsal yapı elemanının kendisini, veya bir bütünü (kompleksi) yoksa bir parçasını mı temsil ettiğini belirtir. Yorum, her mekânsal yapı elemanı alt türü için ayrı ayrı verilir. Eğer bu değer girilmemişse, varsayılan değer &quot;ELEMENT&quot; olarak kabul edilir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Nesne Tipi</td>
<td>Attribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED)J| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak smıflarında ve |(IfcBuiliElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Brüt Yükseklik</td>
<td>GrossHeight</td>
<td>OtoBuildingStorey BaseOuantities</td>
<td>Sayı</td>
<td>Bu katın standart brüt yüksekliği, inşaat döşemesinin üst yüzeyinden bir üstteki döşemenin veya çatının üst yüzeyine kadar olan yüksekliktir. Sadece yüksekliğin sabit olduğu durumda belirtilir.</td>
</tr>
<tr>
<td>Net Yükseklik</td>
<td>NetHeight</td>
<td>OtoBuildingStorey BaseOuantities</td>
<td>Sayı</td>
<td>Bu katın standart net yüksekliği, inşaat döşemesinin üst yüzeyinden bir üstteki döşemenin veya çatının alt yüzeyine kadar olan yüksekliktir. Sadece yüksekliğin sabit olduğu durumda belirtilir.</td>
</tr>
<tr>
<td>Brüt Kat Alanı</td>
<td>GrossFloorArea</td>
<td>OtoBuildingStorey BaseOuantities</td>
<td>Sayı</td>
<td>Mekânsal yapı elemanı içindeki tüm brüt kat alanlarının toplamıdır. Bina katındaki yapı elemanlarının alanlarını içerir. Katla ilişkilendirilmiş mekân ve yapı elemanlarının miktarlarına ek olarak belirtilebilir. Tutarsızlık durumunda, mekân ve yapı elemanlarının bireysel miktarları geçerlidir.</td>
</tr>
<tr>
<td>Bitmiş Döşeme Üst Kotu</td>
<td>ElevationOfFFLRelati ve</td>
<td>PsetBuildingStorey Common</td>
<td>Sayı</td>
<td>Bitmiş döşeme seviyesinin üs yüzey kotu, yerel sıfır yüksekliğine göre verilen kot değeridir. Seviye değişkenlik gösteriyorsa ve belirgin bir baskın kot bulunmuyorsa, bu özellik atlanabilir. Üst yüzeyin geometrik konumlandırmasıyla herhangi bir tutarsızlık olması durumunda, geometrik gösterim dikkate alınır... |</td>
</tr>
</tbody>
</table>

| | |

## Tablo 6.77 IfcBurner Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Brülör (IfcBurner)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Brülör, yakıtı yanma yoluyla ısıya dönüştüren bir cihazdır. Gaz, yağ ve odun brülörlerini içerir.</td>
<td>USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan öze! bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDJ) olarak seçilmişse veya 2) somut örmeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((1fcBuiltElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>.Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Enerji Kaynağı</td>
<td>EnergySource</td>
<td>PsetBurnerTypeCommon</td>
<td>| Metin</td>
<td>Yakıt kaynağını veya yakılan enerjiyi tanımlayan liste.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>Rated Voltage</td>
<td>PsetEleciricalDeviceCommon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üstsınırı maksimum kabul edilir...</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoBumerBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

## Tablo 6.78 IfcCableCarrierFitting Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kablo Taşıyıcı Bağlantı Parçası (IfcCableCarrierFitting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir kablo taşıyıcı bağlantı parçası, kablo taşıyıcı sisteminde bir bağlantı noktasına veya geçiş yerine yerleştirilen bağlantı elemanıdır.</td>
<td>BEND, CONNECTOR, JUNCTION, TRANSITION, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nesne Tipi I</td>
<td>Attribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((CSERDEFINEDJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement|J&#x27;i doğrudan öreklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoCableCarrierFittingB aseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Bükülme Açısı</td>
<td>BendAngle</td>
<td>PsetFittingBend</td>
<td>Sayı</td>
<td>Akış yönündeki değişim</td>
</tr>
<tr>
<td>Bükülme Yarıçapı</td>
<td>BendRadius</td>
<td>PsetFittingBend</td>
<td>Sayı</td>
<td>Eğer dairesel yay ise bükülme yarıçapı, keskin dönüş ise sıfır.</td>
</tr>
<tr>
<td>Bağlantı Tipi</td>
<td>JunctionType</td>
<td>PsetFittinglunction</td>
<td>Metin</td>
<td>Bağlantı tipi. TEE —3 çıkışlı, CROSS — 4 çıkışlı.</td>
</tr>
<tr>
<td>Sol Bağlantı Açısı</td>
<td>JunctionLeftAngle</td>
<td>PsetFittinglunction</td>
<td>Sayı</td>
<td>Sol bağlantı için akış yönündeki değişim.</td>
</tr>
<tr>
<td>Sol Bağlantı Yarıçapı</td>
<td>JunctionLeftRadius</td>
<td>PsetFittinglunction</td>
<td>Sayı</td>
<td>Sol bağlantı için bükülme yarıçapı.</td>
</tr>
<tr>
<td>Sağ Bağlantı Açısı</td>
<td>JunctionRightAngle</td>
<td>PsetFittinglunction</td>
<td>Sayı</td>
<td>Sağ bağlantı için akış yönündeki değişim (0 değeri düz segmenti gösterir). m</td>
</tr>
<tr>
<td>Sağ Bağlantı Yarıçapı</td>
<td>JunetionRightRadius</td>
<td>PsetFittinglunction</td>
<td>Sayı</td>
<td>Sağ bağlantı için bükülme yarıçapı (0 değeri keskin dönüşü gösterir).</td>
</tr>
<tr>
<td>Nominal Uzunluk</td>
<td>NominalLengih</td>
<td>PsetFittingTransition</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal uzunluğu. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Y Ekseninde Eksantriklik</td>
<td>EccentricityinY</td>
<td>PsetFittingTransition</td>
<td>| Sayı</td>
<td>Nokta bağlantısında yer alan iki nokta (veya köşe noktaları) arasındaki y yönündeki mesafe.</td>
</tr>
<tr>
<td>Z Ekseninde Eksantriklik</td>
<td>EccentricityinZ</td>
<td>PsetFittingTransition</td>
<td>ı Sayı</td>
<td>Nokta bağlantısında yer alan iki nokta (veya köşe noktaları) arasındaki z yönündeki mesafe.</td>
</tr>
</tbody>
</table>

İ | | | =

## Tablo 6.79 IfcCableCarrierSegment Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kablo Taşıyıcı Segment (IfcCableCarrierSegment)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir kablo taşıyıcı segmenti, özellikle kabloları taşımak ve desteklemek için kullanılan bir akış segmentidir.</td>
<td>CABLE BRACKET, CABLE LADDER SEGMENT, CABLE TRAY SEGMENT, CABLE TRUNKING SEGMENT, CATENARY WIRE, CONDUIT SEGMENT, DROPPER, ÜSERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. .c.oSU Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED)) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuilElement)J&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td colspan="2">- i Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoCableCarrierSegment BaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesit ortasında hesaplanır, giriş ve çıkış portları arasındaki mesafeye eşittir.</td>
</tr>
<tr>
<td>Nominal Genişlik</td>
<td>Nominal Width</td>
<td>PsetCableCarrierSegment TypeConduitSegment</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal genişliği. Boyut bilgisi. şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Nominal Yükseklik</td>
<td>NominalHeight</td>
<td>PsetCableCarrierSegment TypeConduitSegment</td>
<td>Sayı</td>
<td>Nesnenin nominal yüksekliği. Boyut bilgisi, şeki! temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Nominal Çap</td>
<td>NominalDiameter</td>
<td colspan="2">Pset CableCarrierSegment Sayı TypeConduitSegment Yy</td>
<td>Nesnenin nominal çapı veya genişliği.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoCableCarrierSegment BaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Kesit Alanı</td>
<td>CrossSectionArea</td>
<td>OtoCableCarrierSegment BaseOuantities</td>
<td colspan="2">Sayı Nesnenin kesitinin (veya profilinin) toplam alanı.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>OtoCableCarrierSegment BaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın), genellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td>İç Çap</td>
<td>InnerDiameter</td>
<td>OtoConduitSegmentBase Çuantities</td>
<td>Sayı</td>
<td>Nesnenin iç çapı.</td>
</tr>
<tr>
<td>Dış Çap</td>
<td>OuterDiameter</td>
<td>OtoConduitSegmentBase Çuantities</td>
<td>Sayı</td>
<td>Nesnenin dış çapı.</td>
</tr>
<tr>
<td>Kanal Şekil Tipi</td>
<td>ConduitShapeType</td>
<td>PsetCableCarrierSegment TypeConduitSegment</td>
<td>Metin</td>
<td>Kana! segmentinin şekli.</td>
</tr>
<tr>
<td>Rijittir</td>
<td>IsRigid</td>
<td>PsetCableCarrierSegment TypeConduitSegment</td>
<td>Mantıksal</td>
<td>Kanalın rijit (&lt; DOĞRU) mi yoksa esnek (- YANLIŞ) mi olduğunu gösterir</td>
</tr>
<tr>
<td>Akım Taşıma Kapasitesi</td>
<td>CurrentCarryingCapacity</td>
<td>PsetCableCarrierSegment TypeDropper</td>
<td>&#x27; Sayı</td>
<td>Belirtilen koşullar altında, bir iletkenin, cihazın veya ekipmanın sürekli olarak taşıyabileceği maksimum elektrik akımı; sabit sıcaklığı verilen sınır değeri aşmayacak şekilde. IEC60826-11-13&#x27;e dayanır. NOT: Belirtilen sıcaklık, maksimum tasarım ortam sıcaklığıdır.</td>
</tr>
<tr>
<td>Çekme Dayanımı</td>
<td>TensileStrength</td>
<td>PsetCableCarrierSegment TypeDropper</td>
<td>Sayı</td>
<td>Uygulanan kuvvet altında kırılmaya karşı dayanıklılığını gösterir.</td>
</tr>
<tr>
<td>Kurulum Yönergesi</td>
<td>Assembilyinstruction</td>
<td>PsetCableCarrierSegment TypeDropper</td>
<td>Metin</td>
<td>Sistem / ekipman / tesisin nasıl monte edildiğini tanımlayan talimatlar.</td>
</tr>
<tr>
<td>Maksimum Çekme Dayanımı</td>
<td>UltimateTensileStrength</td>
<td>PsetCableCarrierSegment TypeDropper</td>
<td>Sayı</td>
<td>Bir malzemenin veya elemanın gerilme veya çekme sırasında kırılmadan önce dayanabileceği maksimum gerilme.</td>
</tr>
<tr>
<td>Ayarlanabilirdir</td>
<td>IsAdjustable</td>
<td>Pset CableCarrierSegment TypeDropper</td>
<td>Mantıksal</td>
<td>Elemanın ayarlanabilir olup olmadığını gösterir.</td>
</tr>
<tr>
<td>Akım Taşıyordur</td>
<td>IsCurrentCarrying</td>
<td>PsetCableCarrierSegment TypeDropper</td>
<td>Mantıksal</td>
<td>Akımın düşey iletkenden geçip geçmeyeceğini belirtir.</td>
</tr>
<tr>
<td>Nominal Yük</td>
<td>NominalLoad</td>
<td>PsetCableCarrierSegment TypeDropper</td>
<td>Sayı</td>
<td>Bir bileşenin taşıyabileceği nominal yük.</td>
</tr>
<tr>
<td>Merdiven Konfigürasyonu</td>
<td>LadderConfiguration</td>
<td>PsetCableCarrierSegment TypeCableladderSegment</td>
<td>Metin</td>
<td>Kullanılan merdiven yapısının konfigürasyonunun açıklaması.</td>
</tr>
<tr>
<td>Bölme Sayısı</td>
<td>NumberOfCompartments</td>
<td>PsetCableCarrierSegment TypeCableTrunkingSegme nt</td>
<td>Sayı</td>
<td>Kanal gövdesi (trunking) içindeki ayrı iç bölmelerin sayısı.</td>
</tr>
<tr>
<td>AC Direnci</td>
<td>ACResistance</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Metin</td>
<td>AC altındaki direnç.</td>
</tr>
<tr>
<td>Katenary Tel Türü</td>
<td>Catenary WireType</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Sayı</td>
<td>Katenary (askı) telinin tipini belirtir.</td>
</tr>
<tr>
<td>Isıl Genleşme Katsayısı</td>
<td>ThermalExpansionCoeffici ent</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Sayı</td>
<td>Bir gövdenin iki noktası arasındaki | mesafesinin, verilen koşullar altında (EC 113-04-27) termodinamik sıcaklık T ile değişimini tanımlayan nicelik. Oran, Kelvin başına tanımlanır.</td>
</tr>
<tr>
<td>DC Direnci</td>
<td>DCResistance</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Sayı</td>
<td>Doğru akım (DC) altında ve 20 *C sıcaklıkta direnç.</td>
</tr>
<tr>
<td>Büküm Oranı</td>
<td>LayRatio</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Sayı</td>
<td>Büküm uzunluğu ile tek iletken çapı arasındaki oran.</td>
</tr>
<tr>
<td>Uzunluk Başına Kütle</td>
<td>MassPerLength</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Sayı</td>
<td>Uzunluk başına kütle; yani birim uzunluktaki ekstrüzyonun kütlesi (ör. kg/m cinsinden ölçülür).</td>
</tr>
<tr>
<td>Mekanik Gerilme</td>
<td>MechanicalTension</td>
<td>PsetCableCarierSegment TypeCatenary Wire</td>
<td>Sayı</td>
<td>Bir akış segmentine uygulanan nominal mekanik kuvvet.</td>
</tr>
<tr>
<td>Fiziksel Tanım Referansı</td>
<td>PhysicalDescriptionRefere nce</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Metin</td>
<td>Ekipmanın dış İsteğe Bağlı fiziksel tanımı; örneğin ağırlık, şekil, model, uzunluk, yükseklik, çap.</td>
</tr>
<tr>
<td>Büküm Yöntemi</td>
<td>StrandingMethod</td>
<td>PsetCableCarrierSegment TypeCatenary Wire</td>
<td>Metin</td>
<td>Kablonun büküm yöntemini belirtir. Büküm (stranding), belirli sayıda tel elemanının ortak bir eksen etrafında sarılarak birleştirilmesi işlemidir.</td>
</tr>
<tr>
<td>Young Modülü</td>
<td>YoungModulus</td>
<td>PsetCableCarrierSegment &#x27;IypeCatenary Wire</td>
<td>Sayı</td>
<td>Malzemenin Young modülü elastisite ölçüsü.</td>
</tr>
</tbody>
</table>

İ ;

| j | i

|

|

## Tablo 6.80 IfcCaissonFoundation Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Keson Temeli (IfcCaissonFoundation)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Keson temeli esasen açık veya kapalı olabilen boş bir kutudur.</td>
<td>WELL, CAISSON, USERDEFINED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt üplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir oO|) Ön Tanmlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve /((IfcBuiltElementJl&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: ,Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
</tbody>
</table>

## Tablo 6.81 IfcChiller Simfi İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Soğutma Grubu (IfcChiller)</td>
<td>Ön Tanımlı Tür</td>
</tr>
<tr>
<td colspan="4">Tanım: Soğutma grubu, bir sıvıdaki ısıyı uzaklaştırmak için buhar sıkıştırmalı veya absorbsiyonlu soğutma çevrimini kullanan bir cihazdır. Genellikle su veya su-glikol karışımı olan akışkanı soğutmak için kullanılır. Soğutulmuş akışkan daha sonra bir binadaki havayı soğutmak ve nemini gidermek için kullanılır.</td>
<td>AIR COOLED, WATER COOLED, HEAT RECOVERY, USERDEFİNED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: . 1) Ön Tanımlı Tip özniteliğinin değeri listeden NUESERDEFINEDİ| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve |(IfcBuiltElementll&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim değişiklii bakanlığı İnşaat ve Tesisat Birin fiyat Poz No&#x27;sudur.</td>
</tr>
<tr>
<td>Nominal Yoğuşma Sıcaklığı</td>
<td>NominalCondensingTemp erature</td>
<td>PsetChillerTypeCommon</td>
<td>Sayı</td>
<td>Soğutucunun yoğuşma sıcaklığı.</td>
</tr>
<tr>
<td>Nominal Buharlaşma Sıcaklığı</td>
<td>NominalEvaporatingTemp erature</td>
<td>PsetChillerTypeCommon</td>
<td>Sayı</td>
<td>Soğutucunun buharlaşma sıcaklığı.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Kapasite Eğrisi</td>
<td>CapacityCurve</td>
<td>PsetChillerTypeCommon</td>
<td>Sayı</td>
<td>Chiller soğutma kapasitesi, yoğuşma sıcaklığı ve buharlaşma sıcaklığının bir fonksiyonudur; veriler tablo formundadır. Kapasite — f (TempCon, TempEvp), kapasite -altbl*Teitc1*TeilW2-d1*Tcitel*TcMm2*f1*Tei*Tci. Bu tablo birden</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>fazla giriş değişkeni kullanır; bunu temsil etmek için hem Defining Values hem de DefinedValues listeleri (Onull&#x27;dur ve o IfcTable, IfcResourceConstraintRelationship ve IfcMetwic kullanılarak iliştirilir. Sütunlar aşağıdaki sırayla tanımlanmıştır: 1. IfcPowerMeasure: Capacity 2. IfcThermodynamicTemperatureMeasure: CondensingTemperature 5. IfcThermodynamicTemperatureMeasure: Evaporating Temperature</td>
</tr>
<tr>
<td>Performans Katsayısı Eğrisi</td>
<td>CoefficientOfPerformance Curve</td>
<td>PsetChillerTypeCommon</td>
<td>Sayı</td>
<td>Chiller performans katsayısı (COP), yoğuşma sıcaklığı ve buharlaşma sıcaklığının bir fonksiyonudur; veriler tablo formundadır. COP- f (TempCon, TempEvp), COP ii a2*b2*Teitc2*TeiW2td2*Tcire2*TciW2-42*Tei*Tci. Bu tablo birden fazla giriş değişkeni kullanır: bunu temsil etmek için hem Defining Values hem de DefinedValues listeleri (o null&#x27;dur Ove o IfcTable, IfcResourceConstraintRelationship ve IfcMetric kullanılarak tliştirilir. Sütunlar aşağıdaki sırayla tanımlanmıştır: 1. IfcPositiveRatioMeasure: CoefficientOfPerformance 2. IfcThermodynamicTemperatureMeasure: CondensingTemperature 3. IfcThermodynamicTemperatureMeasure: Evaporating Temperature</td>
</tr>
<tr>
<td>Tam Yük Oranı Eğrisi</td>
<td>FullLoadRatioCurve</td>
<td>PsetChillerTypeCommon</td>
<td>Sayı</td>
<td>Belirli bir yoğuşma ve buharlaşma sıcaklığında, gerçek güç ile tam yük gücü oranı; kısmi yükün kuadratik bir fonksiyonu olarak. FracFullLoadPower &gt; #PartLoadRatio).</td>
</tr>
<tr>
<td>Nominal Verimlilik</td>
<td>NominalEfficiency</td>
<td>PsetChillerTypeCommon</td>
<td>Sayı</td>
<td>Nominal koşullar altında nesnenin nominal verimliliği.</td>
</tr>
<tr>
<td>Nominal Isı İkame Oranı</td>
<td>NominalHeatRejectionRat €</td>
<td>PsetChillerTypeCommaon</td>
<td>Sayı</td>
<td>Soğutma etkisinin ve kompresöre gelen güç girdisinin ısıl eşdeğerinin toplamı.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoChillerBaseOuantities |</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat ,detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate Jalınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

|

|

## Tablo 6.82 IfeChimney Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Baca (IfcChimney)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bacalar genellikle bir binanın yapısının dikey ya da dikeye yakın bölümleridir ve bina kabuğunun bir parçasını oluştururlar. Genellikle prefabrik veya yerinde dökme betondan inşa edilirler; günümüzde tuğla ile yapılmaları ise nadirdir.</td>
<td>USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden İLUSERDEFINEDJ) olarak seçilmişse veya 2) somut ömeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuihtElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>, Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>PsetChimneyCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td>Taşıyıcı</td>
<td>LoadBearing</td>
<td>PsetChimneyCommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir .</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoChimneyBaseOuantiti es</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Temelden (veya başlangıçtan) en üst noktaya kadar, hiçbir kesit boşluğu veya diğer imalat özelliği dikkate alınmaz.</td>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>PsetChimneyCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eer (DOGRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Baca Kanalı Sayısı</td>
<td>NumberOfDrafts</td>
<td>PsetChimneyCommon</td>
<td>Sayı</td>
<td>Tek bir bacada, hava geçişinin olduğu kesintisiz boşluklar olan baca kanallarının sayısı.</td>
</tr>
</tbody>
</table>

| i

## Tablo 6.83 IfcCoil Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Serpantin (IfcCoil)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Serpantin, birbirine karışmayan akışkanlar arasında ısı transferi sağlamak için kullanılan bir cihazdır. Yaygın bir örnek, yüzeyi boyunca hareket eden havadan ısıyı uzaklaştırmak için soğutulmuş su, antifriz veya soğutucu akışkan dolaştırılan kanatlı bir serpantinin kullanıldığı soğutma serpantinidir. Bir serpantin, bir ısıtma veya soğutma akışkanı taşıyan bir dizi borunun (serpantin) bir hava akımına yerleştirilmesiyle ısıtma veya soğutma amaçları için kullanılabilir. Serpantin, serpantin formunda demetlenmiş borulardan veya genişletilmiş bir ısı transfer yüzeyi sağlayan kanatlı borulardan yapılabilir.</td>
<td>DXCOOLING COIL, ELECTRIC HEATING COIL, GAS HEATING COIL, HYDRONIC COJL, STEAM HEATING COHL, WATER COOLING COJL, WATER HEATING COJL, USERDEFİINED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut al tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örmeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((1fcBuilElement)l&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Hava Akış Debisi Aralığı</td>
<td>AirFlowRateRange</td>
<td>PsetCoilTypeCommon</td>
<td>Sayı</td>
<td>Sağlanabilecek hava debisinin olası aralığı. Serpantin boyunca hava akışının olmadığı durumlarda (örneğin, döşeme plağına gömülü elektrik serpantini gibi), değer sıfırdır.</td>
</tr>
<tr>
<td>Serpantin Yerleşimi</td>
<td>CoilPlacement</td>
<td>PsetCoilTypeCommon</td>
<td>Metin</td>
<td>Serpantinin yerleşimini belirtir. FLOOR, serpantin tipi WATERHEATINGCOIL veya ELECTRICHEATINGCOLIL ise, yerden ısıtıcıyı ifade eder. CEILING, serpantin tipi WATERCOOLINGCOIL ise, soğutma tavanını ifade eder. UNIT, serpantinin soğutulmuş kiriş vb. gibi bir soğutma veya ısıtma ünitesinin parçası olduğunu belirtir.</td>
</tr>
<tr>
<td>Nominal UA</td>
<td>NominalUA</td>
<td>PsetCoilTypeCommon</td>
<td>Sayı</td>
<td>Nominal UA değeri (toplam ısı transfer katsayısı x yüzey alanı).</td>
</tr>
<tr>
<td>Çalışma Sıcaklık Aralığı</td>
<td>Operational TemperatureR ange</td>
<td>PsetCoilTypeCommon</td>
<td>| Sayı |</td>
<td>İzin verilen çalışma hava sıcaklığı aralığı.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoCoilBaseOuantitics</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

i | | |

7

|

## Tablo 6.84 IfcColumn Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kolon (IfcColumn)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kolon genellikle statik akslarla hizalanan, düşey yapısal veya mimari bir elemandır. Çoğu durumda, basınç yoluyla üst yapıdaki yükü alttaki diğer yapısal elemanlara aktaran düşey ya da: düşeye yakın konumlu bir yapısal elemanı temsil eder. Mimari bakış açısından da böyle bir elemanı temsil edebilir; bu durumda yük taşımayan bir eleman olabilir. Bir kolonun yapısal olarak yük taşıyan veya yük taşımayan bir eleman olup olmadığı (/PsetColumnCommon||.|iLoadBearing|)) özelliğiyle belirlenir.</td>
<td>COLUMN, PIERSTEM, PIERSTEM SEGMENT, PILASTER, STANDCOLUMN, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nesne Tipi |</td>
<td>Attribute: ObjectType</td>
<td>-</td>
<td>| Metin | |</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tüpi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: . 1) Ön Tanımlı Tip özniteliğinin değeri listeden (LUSERDEFİNEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve /((IfcBuiltElement|)&#x27;i doğrudan ömeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Isıl İletkenlik Katsayısı</td>
<td>ThermalTransmittance</td>
<td>PsetColumnCommon</td>
<td>Sayı</td>
<td>Bir bileşenin, ısı akışı yönünde (tüm malzemeleri içeren) ısı iletkenlik katsayısı (U-Value).</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>Oto Column BaseÇuantiti es</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesitler veya kesit boşlukları gibi imalat özellikleri dikkate alınmaz.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoColumnBaseÇOuantiti es</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>Net Weight</td>
<td>OtoColumnBaseÇOuantiti es</td>
<td>Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGe neral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengihClas s</td>
<td>PsetConcreteElemeniGe neral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
<tr>
<td>Beton Dayanım Sınıfı</td>
<td>StrengthClass</td>
<td>PsetConcreteElementGe neral</td>
<td>Metin</td>
<td>Projede uygulanan beton tasarım standardına göre beton dayanımının sınıflandırması.</td>
</tr>
<tr>
<td>Eğim</td>
<td>Slope</td>
<td>PsetColumnComman</td>
<td>Sayı</td>
<td>Eğim açısı — yataya (ogöre relatif oo (0.0 derece). Şekil bilgisi, şekil temsilinin yanı sıra kullanılan geometrik parametrelerle birlikte sağlanır. Geometrik parametreler ile şekil özellikleri oOarasında tutarsızlık Oolması durumunda, geometrik parametreler dikkate alınır. Geometri düzenleme uygulamaları (ör. CAD) için bu değer yalnızca &quot;yazılabilir&quot; olmalıdır.</td>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>PsetColumnCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Kesit Alanı</td>
<td>CrossSectionArea</td>
<td>OtoColumnBaseOuantiti es</td>
<td>Sayı</td>
<td>Nesnenin kesitinin (veya profilinin) toplam alanı.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>OtoColumnBaseOuantiti es</td>
<td>İ Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (kolon başlarının alanları dikkate alınmaksızın), genellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td>Brüt Yüzey Alanı</td>
<td>GrossSurfaceArea</td>
<td>OtoColumnBaseOuantiti es</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt alanı, genellikle çevre * uzunluk * 2 * Kesit Alanı olarak hesaplanır. Bu, Dış Yüzey Alanı - (2 x Kesit Alanı) toplamıdır ve yalnızca Dış Yüzey Alanı ve Kesit Alanı ayrı olarak belirlenemediğinde ;verilecektir.</td>
</tr>
<tr>
<td>Net Yüzey Alanı</td>
<td>NetSurfaceArea</td>
<td>OtoColumnBaseOuantiti es</td>
<td>Sayı</td>
<td>Nesnenin net yüzey alanı genellikle, olası imalat özelliklerini (kesit boşlukları vb.) veya açıklıkları ve girintileri dikkate alarak., çevre * uzunluk * 2 * Kesit Alanı olarak hesaplanır.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>. GrossVolume</td>
<td>OtoColumnBaseÇuantiti es</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkmtılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoColumnBaseÇuantiti ı es</td>
<td>Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özelliklerini (kesit boşlukları vb.) veya açıklıklar ve girintiler dikkate alınarak hesaplanır.</td>
</tr>
</tbody>
</table>

|

|

## Tablo 6.85 IfcCommunicationsAppliance Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">İletişim Cihazı (IfcCom municationsA ppliance)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: İletişim cihazı, elektronik veya dijital bilgiyi veri ya da ses olarak ileten ve alan bir aygıttır.</td>
<td>ANTENNA, COMPUTER, FAX, GATEWAY, MODEM, NETWORK APPLIANCE, NETWORK BRİDGE, NETWORK HUB, PRINTER, REPEATER, ROUTER, SCANNER, USERDEFİNED, NOTDEFİNED</td>
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
<td>Attribute: ObjectType |</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir... 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve /((IfcBuilhElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>Pset Electrical DeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Cihazın. tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>Rated Voltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoCommunicationsAppl ianceBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.86 IfeCondenser Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kondenser (IfcCondenser)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kondenser, genellikle bir soğutucuyu (refrigerant) gaz halinden sıvı hale yoğunlaştırarak ısıyı dağıtmak için kullanılan bir cihazdır.</td>
<td>AIR COOLED, EVAPORATIVE COOLED, WATER COOLED, WATER COOLED BRAZEDPLATE, WATER COOLED SHELL COIL, WATER COOLED SHELL TUBE, WATER COOLED TUBE IN TUBE, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) OÖn Tanımlı Tip özniteliğinin değeri listeden I(USERDEFINEDİJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve (J1fcBuiltElement)|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>İ Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>Pset Electrical DeviceCommon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>ExternalSurfaceArea</td>
<td>PsetCondenserTypeCommon</td>
<td>Sayı</td>
<td>Dış yüzey alanı (birincil ve ikincil alan).</td>
</tr>
<tr>
<td>İç Soğutucu Hacmi</td>
<td>IntemalRefrigerantVolume</td>
<td>PsetCondenserTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin iç hacmi (soğutucu akışkan tarafı).</td>
</tr>
<tr>
<td>İç Yüzey Alanı</td>
<td>IntermalSurfaceArea</td>
<td>PsetCondenserIypeCommon</td>
<td>Sayı</td>
<td>İç yüzey alanı.</td>
</tr>
<tr>
<td>İç Su Hacmi</td>
<td>Internal Water Volume</td>
<td>PsetCondenserIypeCommon</td>
<td>Sayı</td>
<td>Nesnenin iç hacmi (su tarafı).</td>
</tr>
<tr>
<td>Nominal Isı Transfer Alanı</td>
<td>NominalHeatTransferArea</td>
<td>PsetCondenserTypeCommon</td>
<td>Sayı</td>
<td>Nominal toplam ısı transfer katsayısı ile ilişkili nominal ısı transfer yüzey alanı.</td>
</tr>
<tr>
<td>Nominal Isı Transfer Katsayısı</td>
<td>Nomina!HeatTransferCoeffi cient</td>
<td>PsetCondenserTypeCommon</td>
<td>Sayı</td>
<td>Nominal ısı transfer alanı ile ilişkili nominal toplam ısı transfer Katsayısı.</td>
</tr>
<tr>
<td>Soğutucu Akışkan Sınıfı</td>
<td>RefrigerantClass</td>
<td>PsetCondenserTypeCommon</td>
<td>Metin</td>
<td>Nesne (o tarafından (o kullanılan (o soğutucu (Ooakışkan (o sınıfı, Kloroflorokarbonlar.; Hidrokloroflorokarbonlar.; Hidroflorokarbonlar.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoCondenserBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

| |

## Tablo 6.87 IfcCoolingTower Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Soğutma Kulesi (IfcCoolingTower)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Soğutma kulesi, su gibi bir akışkanı dolaştırarak sıcaklığını kısmi buharlaşma yoluyla düşürmek için ısıyı ortam havasına atan bir cihazdır.</td>
<td>NATURAL DRAFT, MECHANICAL INDUCED DRAFT, MECHANICAL FORCED DRAFT, USERDEFİNED, | NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; 1) Ön Tanmlı Tip özniteliğinin değeri listeden ((USERDEFİNEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve /((I1fcBuiltElementil&#x27;i doğrudan örmeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Aftribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Dış Ortam Tasarım Kuru Termometre Sıcaklığı</td>
<td>AmbientDeşignDryBulbTe mperature</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Sayı</td>
<td>Soğutma kulesinin seçimi için kullanılan dış ortam tasarım kuru termometre sıcaklığı.</td>
</tr>
<tr>
<td>Dış Ortam Tasarım Yaş Termometre Sıcaklığı</td>
<td>AmbientDesign WetBulbT emperature</td>
<td colspan="2">Pset CoolingTowerTypeC Sayı ommon</td>
<td>Soğutma kulesinin seçimi için kullanılan dış ortam tasarım yaş termometre sıcaklığı.</td>
</tr>
<tr>
<td>Hazne Rezerv Hacmi</td>
<td>BasinReserve Volume</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Sayı</td>
<td>Soğutma kulesi haznesinde işletme ve taşma seviyeleri arasındaki hacim.</td>
</tr>
<tr>
<td>Kapasite Kontrolü</td>
<td>CapacityControl</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Metin</td>
<td>Görevi kontrol etmek için fan açılıp kapatılır. Görevi kontrol etmek için fan düşük ve yüksek hız arasında değiştirilir.; Görevi kontrol etmek için fan hızı değiştirilir.; Görevi kontrol etmek için damperler hava akışını düzenler.; Görevi kontrol etmek için baypas vanası su akışını düzenler.; Görevi kontrol etmek için birden fazla seri pompa açılıp kapatılır.; Görevi kontrol etmek için pompa hızı yüksek/düşük arasında değiştirilir.; Görevi kontrol etmek için pompa hızı değiştirilir.</td>
</tr>
<tr>
<td>DolaşımTipi</td>
<td>CircuitType</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Metin</td>
<td>Açık Dolaşım (OpenCircuit): Su doğrudan soğutma atmosferine maruz bırakılır.; Kapalı Dolaşım (CloseCircuit): Akışkan atmosferden bir ısı eşanjörü ile ayrılır.; Islak (Wet): Hava akımı veya ısı değişim yüzeyi buharlaşarak soğutulur. Kuru (Dry): Hava akımına buharlaşma olmaz.: Kuru Islak (Dry Wet): Kuru kule ile ıslak kulenin birleşimi.</td>
</tr>
<tr>
<td>Kontrol Stratejisi</td>
<td>ControlStrategy</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Metin</td>
<td>FixedExiting WaterTemp: Kapasite, sabit bir çıkış suyu sıcaklığını koruyacak şekilde kontrol edilir. WetBulbTempReset: Ayarlanan hedef değer (set noktası), yaş termometre sıcaklığına göre yeniden ayarlanır.</td>
</tr>
<tr>
<td>| Akış Düzeni</td>
<td>FlowArrangement</td>
<td>PsetCoolingTowerlypeC ommon</td>
<td>Metin</td>
<td>Isı eşanjörü veya soğutma kulesi için temel akış düzenlemelerini tanımlar: Ters Akış — hava ve su akışı farklı yönlerden girer. Çapraz Akış — hava ve su akışı birbirine dik yönde hareket eder. Paralel Akış— hava ve su akışı aynı yönde girer. Çok Geçişli Akış — birden fazla geçişe sahip ısı eşanjörü düzenlemesidir. Diğer — yukarıda tanımlanmayan diğer ısı eşanjörü akış düzenlemelerini ifade eder.</td>
</tr>
<tr>
<td>Asansör Yükseklik Farkı Kule içi Su Kot Farkı</td>
<td>LiftElevationDifference</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Sayı</td>
<td>Soğutma kulesi çukuru ile kule tepesinin kot farkı.</td>
</tr>
<tr>
<td>Hücre Sayısı</td>
<td>NumberofCeils</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Sayı</td>
<td>Soğutma kulesi ünitesindeki bağımsız soğutma hücrelerinin sayısı.</td>
</tr>
<tr>
<td>Çalışma Sıcaklık Aralığı</td>
<td>Operation TemperatureRan ge</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Sayı</td>
<td>İzin verilen çalışma ortam hava sıcaklığı aralığı.</td>
</tr>
<tr>
<td>Püskürtme Tipi</td>
<td>Spray Type ı</td>
<td>PsetCoolingTowerTypeC ommon</td>
<td>Metin</td>
<td>SprayFilled: Şu, hava akışı içine püskürtülerek dağıtılır., SplashTypeFill: Su, ardışık sıçratma çubukları üzerinden kademeli olarak aşağıya doğru akarak soğutulur., FilmTypeFill: Su, birbirine yakın levhalar üzerinde ince bir film tabakası halinde akar.</td>
</tr>
<tr>
<td>Su Gereksinimi</td>
<td>WaterReguirement</td>
<td colspan="2">Pset CoolingTowerTypeC&#x27; we set Cooling TTyp Sayı ommon |</td>
<td>Besleme suyu gereksinimi.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoCoolingTowerBaseO uantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

|

| | , | i a,

_ _ | |

## Tablo 6.88 IfcCovering Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kaplama (IfcCovering)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kaplama, başka bir elemanın bir kısmını örten ve tamamen o elemana bağlı olan bir elemandır. IfcCovering, bir kaplama türünün oluşumunu tanımlar ve (varsa) bu tür IfcCoveringType tarafından ifade edilir.</td>
<td>CEILİNG, CLADDING, COPING, FLOORING, INSULATION, MEMBRANE, MOLDING, ROOFING, SKIRTING BOARD, SLEEVİNG, TOPPING, WRAPPING, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir... 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement)|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Brüt Alan</td>
<td>GrossArea</td>
<td>OtoCoveringBaseOuantit ies</td>
<td>Sayı</td>
<td>Nesnenin brüt alanı. Boşluklar, girintiler, çıkıntılar ve kesit boşlukları dikkate alınmaz. Mekâna bakan kaplamanın tüm brüt alanlarının toplamıdır.</td>
</tr>
<tr>
<td>Net Alan</td>
<td>NetArea</td>
<td>OtoCoveringBaseOuantit ies</td>
<td>Sayı</td>
<td>Nesnenin toplam net alanı. Açıklıklar, girintiler ve kesit boşlukları çıkarılır, çıkıntılar ise eklenir. Mekâna bakan kaplamanın tüm net alanlarının toplamıdır.</td>
</tr>
</tbody>
</table>

## Tablo 6.89 IfeCurtain Wall Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Giydirme Cephe (IfcCurtain Wall)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir giydirme cephe, zemine oturmaktan ziyade döşeme/çatı strüktürünün kenarına asılmış bileşenlerin bir araya gelmesiyle oluşturulan bir bina duvarıdır. Giydirme cephe. bir bina elemanı bileşimi olarak temsil edilir ve |(IfcBuiltElement)) alt tipi olarak IfcRelAggregates ilişkisini kullanarak uygulanır. Giydirme cephe genellikle dış cephe olur, ancak ((PsetCurtainWalliCommonJ|.((IsExternal)) kullanılarak iç mekân giydirme cepheleri de tanımlanabilir.</td>
<td>USERDEFİNED, NOTDEFINED</td>
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
<td>Metin |</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED)|) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve |(IfcBuiltElementj|l&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>| Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi , (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Isıl İletkenlik Katsayısı</td>
<td>ThermalTransmittance</td>
<td>PsetCurtainWallCommon</td>
<td>Sayı</td>
<td>Bir bileşenin, ısı akışı yönünde (tüm malzemeleri içeren) ısı iletkenlik katsayısı .(U-Value).</td>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExtemal</td>
<td>Pset Curtain WallCommon</td>
<td>Mantıksal</td>
<td>Öğenin dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>Oto Curtain WallOuantities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Orta hat/eksen boyunca (duvar hattından farklı olsa bile).</td>
</tr>
<tr>
<td>Genişlik</td>
<td>Widih</td>
<td>Oto Curtain WallOuantities</td>
<td>Sayı</td>
<td>Nesnenin genişliği. Sadece, nesne sabit kalınlığa sahipse (prizmatik) verilir. Yalnızca giydirme cephe hattı boyunca sabit olduğu durumda verilmelidir.</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>OtoCurtainWallOuantities</td>
<td>Sayı</td>
<td>Karakteristik yükseklik. Giydirme cephenin toplam yüksekliği. Yalnızca giydirme cephe boyunca sabitse verilmelidir.</td>
</tr>
<tr>
<td>Akustik Performans Sınıfı</td>
<td>AcousticRating</td>
<td>Pset Curtain WallCommon</td>
<td>Metin</td>
<td>Bu nesne için akustik performans sınıfi.; Ulusal yapı yönetmeliğine göre verilmiştir. Bu nesnenin ses iletim direncini, tam ses yutum değerleri vermek yerine bir indeks oranıyla gösterir.</td>
</tr>
</tbody>
</table>

|

|

## Tablo 6.90 IfcDamper Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Damper (IfcDamper)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir damper, tipik olarak bir HVAC kanal dağıtım sisteminde yer alır ve hava akışını kontrol etmek veya düzenlemek için kullanılır.</td>
<td>BACK DRAFT DAMPER, BALANCING DAMPER, BLAST DAMPER, CONTROL DAMPER, FIRE DAMPER, FİRE SMOKE DAMPER, FUME HOOD EXHAUST, GRAVITY DAMPER, GRAVITY RELİEF DAMPER, RELIEF DAMPER, SMOKE DAMPER, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden İLUSERDEFINEDİ) olarak seçilmişse veya 2) somut öreklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. Ikinci durum, bazı istisnai yaprak sınıflarında ve |(IfcBuiltElementil&#x27;i doğrudan örmeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Hava Debisi</td>
<td>NominalAirFlowRate</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Nominal hava debisi.</td>
</tr>
<tr>
<td>Nominal Yükseklik</td>
<td>NominalHeight</td>
<td>PsetElementSize</td>
<td>Sayı</td>
<td>Nesnenin nominal yüksekliği. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Nominal Uzunluk</td>
<td>NominaiLength</td>
<td>PsetElementSize</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal uzunluğu. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması ,durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Nominal Genişlik</td>
<td>Nominal Width</td>
<td>PsetElementSize</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal genişliği. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan İgeometrik parameireler ile boyut özellikleri arasında tutarsızlık olması idurumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Çalışma</td>
<td>Operation</td>
<td>PsetDamperIypeCommon</td>
<td>Metin</td>
<td>Damperin çalışması için kullanılan çalışma mekanizması.</td>
</tr>
<tr>
<td>Yönelim?</td>
<td>Orientation</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı veya Metin</td>
<td>Üretici tarafından belirtilen damperin tasarlanan vönelimi.</td>
</tr>
<tr>
<td>Kanat Kalınlığı</td>
<td>BladeThickness</td>
<td>PsetDamperIypeCommon</td>
<td>Sayı</td>
<td>Damper kanadının kalınlığı.</td>
</tr>
<tr>
<td>Kanat Hareketi</td>
<td>BladeAction</td>
<td>PsetDamperTypeCommoen</td>
<td>Metin</td>
<td>Kanat hareketi.</td>
</tr>
<tr>
<td>Kanat Şekli</td>
<td>BladeShape</td>
<td>PsetDamperTypeCommon</td>
<td>Metin</td>
<td>Kanat şekli. Düz. üçlü V-oluk anlamına gelir.</td>
</tr>
<tr>
<td>Kanat Kenarı</td>
<td>BladeEdee</td>
<td>PsetDamperTypeCommon</td>
<td>Metin</td>
<td>Kanat kenarı.</td>
</tr>
<tr>
<td>Kanat Sayısı</td>
<td>NumberofBlades</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Kanat sayısı.</td>
</tr>
<tr>
<td>Yüzey Alanı</td>
<td>FaceArea</td>
<td>PsetDamperIypeCommon</td>
<td>Sayı</td>
<td>Hava akımına açık olan yüzey alanı.</td>
</tr>
<tr>
<td>Maksimum Hava Akış Debisi</td>
<td>MaximumAirFlowRate</td>
<td>PsetDamperIypeCommon</td>
<td>Sayı</td>
<td>İzin verilen maksimum hava akış debisi.</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>PsetDamperIypeCommon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum sıcaklık.</td>
</tr>
<tr>
<td>Maksimum Çalışma Basıncı</td>
<td>Maximum WorkingPres sure</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin dayanması için üretilmiş olduğu maksimum basınç.</td>
</tr>
<tr>
<td>Sıcaklık Sınıflandırması</td>
<td>TemperatureRating</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Sıcaklık sınıflandırması.</td>
</tr>
<tr>
<td>Açık Konumda Basınç Düşümü</td>
<td>OpenPressureDrop</td>
<td>PsetDamperTypeCammon</td>
<td>Sayı</td>
<td>Damper boyunca toplam basınç düşümü.</td>
</tr>
<tr>
<td>Tam Kapalı Durumda Sızıntı</td>
<td>LeakageFullyClosed</td>
<td>PsetDamperTypeCommon</td>
<td colspan="2">Sayı Tamamen kapalıyken sızıntı.</td>
</tr>
<tr>
<td>Kayıp Katsayısı Eğrisi</td>
<td>LossCoefficentCurve</td>
<td>PsetDamperTypeCommon</td>
<td colspan="2">Sayı Kayıp katsayısı — kanat pozisyon açısı eğrisi; basınç düşümünün hız basıncına Yy oranı, kanat açısına göre; C — f (kanat açısı).</td>
</tr>
<tr>
<td>Sızıntı Eğrisi</td>
<td>LeakageCurve</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Sızıntı — basınç düşümü ilişkisi; Sızıntı — f (basınç).</td>
</tr>
<tr>
<td>Yeniden Üretilen Ses Eğrisi</td>
<td>RegeneratedSoundCur ve</td>
<td>Pset DamperTypeCommon</td>
<td>Sayı</td>
<td>Yeniden üretilen ses — hava debisi ilişkisi.</td>
</tr>
<tr>
<td>Çerçeve Tipi</td>
<td>FrameType</td>
<td>PsetDamperTypeCommon</td>
<td>Metin</td>
<td>Damperin kullandığı çerçeve tipi (ör. Standart, Tek Flanş, Tek Ters Flanş, Çift Flanş, vb.).</td>
</tr>
<tr>
<td>Çerçeve Derinliği</td>
<td>FrameDepth</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Çerçevenin uzunluğu (veya derinliği). Damper için, damper çerçevesinin uzunluğu (veya derinliği).</td>
</tr>
<tr>
<td>Çerçeve Kalınlığı</td>
<td>FrameThickness</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Çerçevenin kalınlığı. Damper için, damper çerçevesi malzemesinin kalınlığı.</td>
</tr>
<tr>
<td>Kapatma Sınıfı</td>
<td>CloseOffRating</td>
<td>PsetDamperTypeCommon</td>
<td>Sayı</td>
<td>Kapatma sınıfı.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>GrossWeight</td>
<td>Oto DamperBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

| j |

|

## Tablo 6.91 IfcDistributionBoard Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Dağıtım Panosu (IfcDistributionBoard)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Dağıtım panosu, belirli bir amaç doğrultusunda elektriksel veya iletişim cihazlarının bir araya getirildiği enerji dağıtımını ve devrelerin Kontrolünü sağlayan merkezi bir akış kontrol cihazıdır.</td>
<td>CONSUMER UNİT, DISTRIBUTION BOARD, MOTOR CONTROL CENTRE, SWITCH BOARD, USERDEFİINED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik.</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Nesne Tipi</td>
<td>Attribute:; ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kutlanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED)| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElementJl&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti/ İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetEleciricalDeviceCommon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetEleciricalDeviceCommon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Ana Dağıtım Noktasıdır</td>
<td>IsMain</td>
<td>PsetDistributionBoardOccurrenc e</td>
<td>Mantıksal</td>
<td>Geçerli örneğin bir elektrik dağıtım hiyerarşisinde ana dağıtım noktası veya en üst seviye olduğunu (&gt; DOĞRU) ya da alt-ana dağıtım noktası olduğunu (# YANLIŞ) tanımlar.</td>
</tr>
<tr>
<td>Yetkin Operatör Gerektirir</td>
<td>IsSkilledOperator</td>
<td>PsetDistributionBoardOccurrenc e</td>
<td>Mantıksal</td>
<td>Geçerli oOömekteki dağıtım panosunda işlemlerin, yetkin veya talimatlandırılmış bir kişi tarafından yapılmasının gerektiğini (DOĞRU) ya da uygun beceri veya talimat olmayan bir kişi tarafından yapılabileceğini (SYANLIŞ) tanımlar.</td>
</tr>
<tr>
<td>Nominal Frekans Aralığı</td>
<td>NominalFreguencyR ange</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Cihazın çalışması için sertifikalandırıldığı frekansın alt ve üst sınırları.</td>
</tr>
<tr>
<td>Güç Faktörü</td>
<td>PowerFactor</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>İletken Fonksiyonu</td>
<td>ConductorFunction</td>
<td>PsetElectricalDeviceCommon</td>
<td>Metin</td>
<td>Yükün bağlandığı iletkenlerin işlevini gösterir. IEC 60446 standardına göre LI, L2 ve L3 faz hatlarını temsil eder (bazı durumlarda faz hatları renk (Kırmızı, Mavi, Sarı) veya numara (1, 2, 3) ile de ifade edilebilir). Koruyucu</td>
</tr>
<tr>
<td colspan="2"></td>
<td></td>
<td></td>
<td>Topraklama (Protective Earth) bazen CPC veya ortak koruyucu iletken olarak da adlandırılır. Elektriksel bir cihaz için bir grup hat iletken işlevi uygulanabilir.</td>
</tr>
<tr>
<td>Hat Sayısı</td>
<td>NumberOfPoles</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Nesnenin etkileyeceği kutup sayısı. Cihazın işlemeye/iletmeye yönelik tasarlandığı enerjili hat (faz) sayısı.</td>
</tr>
<tr>
<td>Koruyucu Topraklama Bağlantısı Mevcut</td>
<td>HasProtectiveEarth</td>
<td>PsetElectricalDeviceCommon</td>
<td>Mantıksal</td>
<td>Nesnenin koruyucu topraklama bağlantısına sahip olduğunu (SDOĞRU) veya olmadığını (YALIŞ) gösterir.</td>
</tr>
<tr>
<td>Yalıtım Standardı Sınıfı</td>
<td>InsulationStandardCi ass</td>
<td>PsetElectricalDeviceCommon</td>
<td>Metin</td>
<td>Yalıtım standart sınıfları, elektrik çarpmasına Karşı temel koruma bilgileri sağlar. Yalıtım seviyelerini, yapısal gereksinimler (yüzeysel mesafe ve boşluk mesafeleri) ve elektriksel gereksinimler (elektrik dayanıklılık testlerine uygunluk) açısından tanımlar. Temel yalıtım, tek arıza koşulları altında kısa devre yapmış olarak kabul edilir. Gereken gerçek değerler, yalıtımın maruz kaldığı çalışma voltajına ve diğer faktörlere bağlıdır. Ayrıca, elektrikli cihazın koruyucu toprak bağlantısına sahip olup olmadığını da belirtir.</td>
</tr>
<tr>
<td>IP Kodu</td>
<td>IP Code</td>
<td>PsetElectricalDeviceCommon</td>
<td>Metin</td>
<td>IP Kodu (Uluslararası Koruma Sınıflandırması, IEC 60529), dış etkilere karşı sağlanan koruma derecesini sınıflandırır ve derecelendirir.</td>
</tr>
<tr>
<td>IK Kodu</td>
<td>IK Code</td>
<td>PsetElectricalDeviceCommon</td>
<td>Metin</td>
<td>IEC 62262 (2002)&#x27;ye göre IK Kodu, elektrikli ekipman muhafazalarının dış mekanik darbelere karşı sağladığı koruma derecesi için sayısal bir ,sınıflandırmadır. Not Daha önceki etiketlemede, ilgili IP Koduna (dış etkilere karşı koruma) üçüncü bir rakam (1..) eklenerek darbe koruma seviyesi gösterilmişti.</td>
</tr>
<tr>
<td>Topraklama Tipi</td>
<td>EarthingStyle</td>
<td>PsetElectricalDeviceCommon</td>
<td>Metin</td>
<td>Elektrikli cihazın topraklama tipini gösterir.</td>
</tr>
<tr>
<td>Isı Dağılımı</td>
<td>HeatDissipation</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Elektrik cihazının güç cinsinden ölçülen ısı yayılımını belirtir.</td>
</tr>
<tr>
<td>Güç</td>
<td>Power</td>
<td>Pset ElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Gerçek güç ve çalışabilir aralık.</td>
</tr>
<tr>
<td>Güç Besleme Port Sayısı</td>
<td>NumberOfPowerSup piyPorts</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Elektrikli cihazın güç besleme portlarının sayısını gösterir.</td>
</tr>
</tbody>
</table>

| | | \

## Tablo 6.92 IfcDistrubitionSystem Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Dağıtım Sistemi (IfcDistributionSystem)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir dağıtım sistemi, bir dağıtım ortamının akışını almak, depolamak, sürdürmek, dağıtmak veya kontrol etmek üzere tasarlanmış bir ağdır. Yaygın bir örnek, bir pompa, bir tank ve sıcak suyu terminallere dağıtmak için birbirine bağlı bir boru sisteminden oluşan bir sicak su ısıtma sistemidir.</td>
<td>AIRCONDITIONING, AUDIOVISUAL, CATENARY SYSTEM, CHEMICAL, CHILLEDWATER, COMMUNİCATION, COMPRESSEDAIR, CONDENSERWATER, CONTROL, CONVEYING, DATA, DISPOSAL, DOMESTICCOLDWATER, DOMESTICHOTWATER, DRAINAGE, EARTHING, ELECTRICAL, ELECTROACOUSTIC, EXHAUST, FIREPROTECTTION, FIXEDTRANSMISSIONNETWORK, FUEL, GAS, HAZARDOUS, HEATING, LIGHTING, LIGHTNINGPROTECTTION, MOBILENETWORK, MONITORINGSYSTEM, MUNICIPALSOLIDWASTE, OL, OPERATIONAL, OPERATIONALTELEPHONYSYSTEM, OVERHEAD CONTACTLINE SYSTEM, POWERGENERATION, RAINWATER, REFRIGERATION, RETURN CIRCUIT, SECURİTY, SEWAGE, SIGNAL, STORMWATER, TELEPHONE, TV, VACUUM, VENT, VENTILATION, WASTEWATER, WATERSUPPLY, USERDEFİNED, NOTDEFINED</td>
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
<td>Attribute:Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Nesne Tipi</td>
<td>Atiribute: ObjeciType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kultanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden (USERDEFINED)J) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve (MfcBuiltElementil&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<th>Türkçe Tanım</th>
<th rowspan="2">Özellik</th>
<th rowspan="2">Özellik Seti / İlişki</th>
<th>Veri Tipi</th>
<th rowspan="2">i Açıklama</th>
</tr>
<tr>
<td>(Bilgi Amaçlı)</td>
<td>(Bilgi Amaçlı)</td>
</tr>
<tr>
<td>Elektrik Sistem Tipi</td>
<td>ElectricalSystemType</td>
<td>PsetDistributionSys temTypekElecirical</td>
<td>Metin</td>
<td>Elektrik yönetmelikleri doğrultusunda IEC 60364 standardına göre sistem tiplerini tanımlayan tip belirleyicileridir. Bu belirleyiciler, enerji kaynağının ve tesisatın açıkta kalan iletken kısımlarının toprakla (topraklama sistemiyle) ilişkisine bağlı olarak atanır. TN, TN-C, TN-S, TN-C-S, TT ve IT sistem tiplerini içerir.</td>
</tr>
<tr>
<td>Elektrik Sistem Kategorisi</td>
<td>EleciricalSystemCateg ory</td>
<td>PsetDistributionSys temTypekElectrical</td>
<td>Metin</td>
<td>Devrenin gerilim aralığını IEC standardına göre belirtir. YÜKSEK GERİLİM: &gt;1000V AC veya &gt;1500V DC; DÜŞÜK GERİLİM: 50-1000V AC veya 120—-1500V DC; ÇOK DÜŞÜK GERİLİM: &lt;50V AC veya &lt;120V DC.</td>
</tr>
<tr>
<td>Çeşitlilik Oranı</td>
<td>Diversity</td>
<td>PsetDistributionSys temTypeElectrical</td>
<td>Sayı</td>
<td>Belirli bir zaman aralığında, bir grup elektrikli cihazın veya tüketicinin eşzamanlı maksimum talebinin, aynı dönemdeki bireysel maksimum taleplerinin toplamına oranıdır. Genellikle bir devreye bağlı cihaz gruplarındaki eşzamanlı yük tahminini ifade eder.</td>
</tr>
<tr>
<td>Canlı İletken Sayısı</td>
<td>NumberOfLiveCondu ctors</td>
<td>PsetDistributionSys temTypeElecirical</td>
<td>Sayı</td>
<td>Bu devre içinde bulunan faz (canlı) iletkenlerin sayısıdır. Bu özellik kullanılabilir veya ConductorFunction özelliği (eğer sadece tek iletken varsa) kullanılabilir.</td>
</tr>
<tr>
<td>İzin Verilen Maksimum Gerilim Düşümü</td>
<td>MaximumAllowedVol tageDrop</td>
<td>PsetDistributionSys temTypsElectrical</td>
<td>Sayı</td>
<td>Devre boyunca izin verilen maksimum gerilim düşümüdür; bu değer aşılmamalıdır. Varsayılan olarak tali devrelerde 901.5, son devrelerde 942.5, toplamda 44 sınırı uygulanabilir.</td>
</tr>
<tr>
<td>Topraklama Döngü Empedansı</td>
<td>Netlmpedance</td>
<td>PsetDistributionSys temTypeElectrical</td>
<td>Sayı</td>
<td>Devrenin yukarısındaki maksimum topraklama döngü empedansıdır (genellikle Zs olarak ifade edilir). 559C (1509F) sıcaklık koşulları için geçerlidir.</td>
</tr>
<tr>
<td>Nominal Voltaj Aralığı</td>
<td>RatedVoltageRange</td>
<td>PsetDistributionSys temTypeElecirical</td>
<td>Sayı</td>
<td>Üretici tarafından beyan edilen alt ve üst sınır gerilim değerleriyle ifade edilen nominal voltaj aralığıdır.</td>
</tr>
<tr>
<td>Tasarım Adı</td>
<td>DesignName</td>
<td>PsetDistributionSys temTypeVentilation</td>
<td>Metin</td>
<td>Tasarım değerleri için verilen ad.</td>
</tr>
<tr>
<td>Kanal Boyutlandırma Yöntemi</td>
<td>DuctSizingMethod</td>
<td>PsetDistributionSys temTypeVentilatlon</td>
<td>Metin</td>
<td>Sistem bileşenlerinin boyutlandırılmasında kullanılacak yöntemi tanımlayan liste.</td>
</tr>
<tr>
<td>Basınç Sınıfı</td>
<td>PressureÇlass</td>
<td>PsetDistributionSys temTypeVentilation</td>
<td>Sayı</td>
<td>Nesnenin nominal basınç sınıfı. Sistem bileşenlerinin nominal basınç değerini belirtir.</td>
</tr>
<tr>
<td>Sızdırmazlık Sınıfı</td>
<td colspan="2">! Pset DistributionSys LeakageClass temTypeVentilation</td>
<td>Sayı</td>
<td>Sistem bileşenleri için nominal sızdırmazlık sınıfı.</td>
</tr>
<tr>
<td>Sürtünme Kaybı</td>
<td>FrictionLoss</td>
<td>PsetDistributionSys temTypeVentilation</td>
<td>Sayı</td>
<td>Birim uzunluk başına sürtünmeden kaynaklanan basınç kaybı. (Veri tipi &gt; Basınç/Uzunluk ölçüsü) iğ</td>
</tr>
<tr>
<td>Fire Oranı</td>
<td>ScrapFactor</td>
<td>Pset DistributionSys temType Ventilation</td>
<td>Sayı</td>
<td>Sac malzeme fire oranı.</td>
</tr>
<tr>
<td>Kanal Sızdırmazlık Malzemesi</td>
<td>DuctSealant</td>
<td>PsetDisiributionSys temTypeVentilation</td>
<td>Metin</td>
<td>Kanal ve bağlantı parçalarında kullanılan sızdırmazlık malzemesinin türü.</td>
</tr>
<tr>
<td>Maksimum Hava Hızı</td>
<td>Maximum Velocity</td>
<td>PsetDistributionSys temTypeVentilation</td>
<td>Sayı</td>
<td>Kanal veya bağlantı parçasındaki maksimum tasarım hava hızı.</td>
</tr>
<tr>
<td>En Boy Oranı</td>
<td>AspectRatio</td>
<td>PsetDistributionSys temTypeVentilation</td>
<td>Sayı</td>
<td>Varsayılan en-boy oranı.</td>
</tr>
<tr>
<td>Minimum Yükseklik</td>
<td>MinimumHeight</td>
<td>PsetDistributionSys temTypeVentilation</td>
<td>Sayı</td>
<td>Dikdörtgen, oval veya dairesel kanallar için minimum kanal yüksekliği.</td>
</tr>
<tr>
<td>Minimum Genişlik</td>
<td>Minimum Width</td>
<td>PsetDistributionSys temTypeVentilation</td>
<td>Sayı</td>
<td>Oval veya dikdörtgen kanallar için minimum kanal genişliği.</td>
</tr>
</tbody>
</table>

' , '

| . ; | | | İ

## Tablo 6.93 IfcDoor Sınıfı Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kapı (IfcDoor)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kapı, esas olarak insanlar, eşyalar, hayvanlar ve araçlar için kontrollü erişim sağlamak üzere kullanılan bir yapı elemanıdır. Menteşeli, eksenel, kayar ve ayrıca döner kapı veya katlanır kapı yapılarını içerir.</td>
<td>BOOM BARRIER, DOOR, GATE, TRAPDOOR, TURNSTILE, USERDEFİNED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özmiteliğe cirilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((LUSERDEFINEDİİ olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ove ((ifcBuikElement)&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys, PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Isıl İletkenlik Katsayısı</td>
<td>ThermalTransmittance</td>
<td>PsetDoorCommon</td>
<td>Sayı</td>
<td>Bir bileşenin, ısı akışı yönünde (tüm malzemeleri içeren) ısı iletkenlik katsayısı (U-Value).</td>
</tr>
<tr>
<td>Genişlik</td>
<td>Width</td>
<td>OtoDoorBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin genişliği. Sadece, nesne sabit kalınlığa (prizmatik) sahipse verilir. Kapı kasasının toplam dış genişliği. Yalnızca dikdörtgen kapılar için tanımlanmalıdır.</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>OtoDoorBaseÇuantities</td>
<td>Sayı</td>
<td>Karakteristik yükseklik. Kapı kasasının toplam dış yüksekliği. Yalnızca kapı dikdörtgen biçimindeyse verilmelidir.</td>
</tr>
<tr>
<td>Toplam Genişlik</td>
<td>Overall Width</td>
<td>Attribute</td>
<td>Sayı</td>
<td>Genişliğin genel ölçüsüdür; kapı açıklığını çevreleyen sınırlayıcı kutunun (bounding box) X boyutunu ifade eder. Eğer belirtilmemişse, Toplam Genişlik değeri, kapının yerleştirildiği OpeningElement&#x27;in geometrik temsilinden alınmalıdır.</td>
</tr>
<tr>
<td>Engelli Erişimine Uygun</td>
<td>HandicapAccessible</td>
<td>PsetDoorCommon</td>
<td>Mantıksal</td>
<td>Bu nesnenin engellilerin erişimine uygun olarak tasarlanıp tasarlanmadığını belirtir. Yerel bina yönetmeliklerine göre engelli erişimine uygun olarak</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>değerlendiriliyorsa (DOĞRU), değilse (YANLIŞ) olarak girilir. Ulusal bina yönetmeliği gereklerine göre belirlenir.</td>
</tr>
<tr>
<td>Akustik Performans Sınıfı</td>
<td>AcousticRating</td>
<td>PsetDoorCommon</td>
<td>Metin</td>
<td>Bu nesne için akustik performans sınıfı.; Ulusal yapı yönetmeliğine göre sağlanmıştır. Bu nesnenin ses iletim direncini, tam ses yutum değerleri vermek yerine bir indeks oranıyla gösterir.</td>
</tr>
<tr>
<td>Alan</td>
<td>Area</td>
<td>OtoDoorBaseOuantities</td>
<td>Sayı</td>
<td>Nesne için hesaplanan alan. Kapının dış kasasının toplam alanıdır.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">“Attribute:&quot;: Standart bir IFC elemanının özniteliği</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial). Name” bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

|

## Tablo 6.94 IfcDuctFitting Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kanal Bağlantı Parçası (IfcDuctFitting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kanal bağlantı parçası, kanallı akış dağıtım sisteminde bir bağlantı veya geçiş elemanıdır ya da kanal segmentlerini bağlamak için kullanılır. Bu, akışkanın yönü ve debisi gibi akış özelliklerinde değişikliklere neden olur.</td>
<td>BEND, CONNECTOR, ENTRY, EXIT, JUNCTION, OBSTRUCTTION, TRANSITION, USERDEFINED, NOTDEFİNED</td>
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
<td>Metin |</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden (USERDEFINED)J|) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement|l&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterialJ, yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td></td>
<td>Debi</td>
<td>TREpys PozOzellikSeti</td>
<td>Sayı</td>
<td>Kanal bağlantı parçasından geçen hava akış miktarını ifade eder. Belirli işletme koşullarında kanal içindeki akışkanın hacimsel debisini gösterir.</td>
</tr>
<tr>
<td>Basınç Sınıfı</td>
<td>PressureClass</td>
<td>PsetDuctFittingTypeCom mon</td>
<td>Sayı</td>
<td>Nesnenin nominal basınç sınıfı. Yetkili kurum tarafından tanımlanan basınç sınıflandırması (öm. SMACNA, vb.).</td>
</tr>
<tr>
<td>Basınç Aralığı</td>
<td>PressureRange</td>
<td>Pset DuctFittingTypeCom mon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum çalışma basıncı (ortam basıncına göre).</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>PsetDuctFittingTypeCom mon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum sıcaklık.</td>
</tr>
<tr>
<td>Brüt Kesit Alanı</td>
<td>GrossCrossSectionArea</td>
<td>OtoDuctFittingBaseOuan tities</td>
<td>Sayı</td>
<td>Kesit alanı. Girişte, kanal bağlantı elemanının kendisini ve iç akış alanını da kapsar.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoDuctFittingBaseOuan tities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>Oto DuctFittingBaseOuan ttles</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesitin orta noktasından hesaplanır ve bağlantı ağzı girişinden bağlantı ağzı çıkışına kadar olan akış yolu boyunca olan mesafeye eşittir. Bağlantı parçaları için, en uzun akış yolunun uzunluğunu gösterir.</td>
</tr>
<tr>
<td>Net Kesit Alanı</td>
<td>NetCrossSectionArea</td>
<td>OtoDuctFittingBaseOuan tities</td>
<td>Sayı</td>
<td>Nesnenin kesit alanı. Kanal bağlantı parçaları dahil, iç akış alanı hariç.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>Oto, DuctFittingBaseOuan tities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın), genellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Atiribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name” bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

|

|

## Tablo 6.95 IfcDuctSegment Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="3">Kanal Segmenti (IfcDuctSegment)</td>
<td colspan="2">Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="3">Tanım: Kanal segmenti, tipik olarak kanal ağı şebekesinin iki bölümünü birleştirmek için kullanılır.</td>
<td colspan="2">FLEXİBLE SEGMENT, RIGID SEGMENT, USERDEFİNED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: Oo 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>| Metin</td>
<td>(IfcMateriall, yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>&#x27; Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td></td>
<td>Debi</td>
<td>TREpys PozOzellikSeti</td>
<td>Sayı</td>
<td>Kanal bağlantı parçasından geçen hava akış miktarını ifade eder. Belirli işletme Koşullarında kanal içindeki akışkanın hacimsel debisini gösterir.</td>
</tr>
<tr>
<td>Nominal Çap Veya Genişlik</td>
<td>NominalDiameterOrWWidth</td>
<td>PsetDuctSegmentTypeCo mmon</td>
<td>Sayı</td>
<td>Kanal segmentinin nominal çapı veya genişliği.</td>
</tr>
<tr>
<td>Nominal Yükseklik</td>
<td>NominalHeight</td>
<td>PsetDuctSegmentlypeCo mmon</td>
<td>Sayı</td>
<td>&quot;Nesnenin nominal yüksekliği. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoDuüctSegmentBaseOu antities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesit ortasında hesaplanır, giriş ve çıkış portları arasındaki mesafeye eşittir.</td>
</tr>
<tr>
<td>İç Pürüzlülük Katsayısı</td>
<td>InteriorRoughnessCoeffici ent</td>
<td>PsetDuctSegmentOccurre nce</td>
<td>Sayı</td>
<td>Nesnenin malzemesinin iç pürüzlülüğü.</td>
</tr>
<tr>
<td>İç Kaplamalıdır</td>
<td>HasLiner</td>
<td>PsetDuctSegmentOccurre nce</td>
<td>Mantıksal</td>
<td>İç kısmında kanal yalıtım kaplaması varsa DOĞRU, yoksa YANLIŞ.</td>
</tr>
<tr>
<td>Renk</td>
<td>Colour</td>
<td>PsetDuctSegmentOccurre nce</td>
<td>Metin</td>
<td>Bu nesnenin rengi.</td>
</tr>
<tr>
<td>Çalışma Basıncı</td>
<td>WorkingPressure</td>
<td>PsetDuctSegmentTypeCo mmon</td>
<td>Sayı</td>
<td>Çalışma basıncı. Yetkili kurum tarafından tanımlanan basınç sınıflandırması (öm. SMACNA, vb.).</td>
</tr>
<tr>
<td>Güçlendirme Türü</td>
<td>Reinforcement</td>
<td>PsetDuctSegmentTypeCo mmon</td>
<td>Metin</td>
<td>Kanal segmenti için kullanılan güçlendirme türü (varsa).</td>
</tr>
<tr>
<td>Basınç Aralığı</td>
<td>PressureRange</td>
<td>PsetDuctSegmentIypeCo mmon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum çalışma basıncı (ortam basıncına göre).</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>PsetDuctSegmentTypeCo mmon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum sıcaklık.</td>
</tr>
<tr>
<td>Kesit Şekli</td>
<td>CrossSectionShape</td>
<td>PsetDuctSegmentTypeCo mmon</td>
<td>Metin</td>
<td>Kesit şekli. Bu şeklin segmentin uzunluğu boyunca aynı olduğunu unutmayın. Değişken şekiller için bunun yerine bir geçiş bağlantı parçası kullanılmalıdır.</td>
</tr>
<tr>
<td>Boyuna Kenet</td>
<td>LongitudinalSeam</td>
<td>PsetDuctSegmentIypeCo mmon</td>
<td>Metin</td>
<td>Kanal segmentinin boyuna ekseni boyunca kullanılacak dikiş (birleştirme)/kenet tipidir. il</td>
</tr>
<tr>
<td>Güçlendirme Mesafesi</td>
<td>ReinforcementSpacing</td>
<td>PsetDuctSegmentT&#x27;ypeCo mmon</td>
<td>Sayı</td>
<td>Güçlendirme elemanları arasındaki mesafe.</td>
</tr>
<tr>
<td>Brüt Kesit Alanı</td>
<td>GrossCrossSectionArea</td>
<td>OtoDuctSegmentBaseOu antities</td>
<td>Sayı</td>
<td>Kesit alanı. Kanalın kendisini ve iç akış alanını da kapsar.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoDuctSegmentBaseOu antities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Kesit Alanı</td>
<td>NetCrossSectionArea</td>
<td>OtoDuctSegmentBaseÇu antities</td>
<td>Sayı</td>
<td>Nesnenin kesit alanı. İç akış alanı hariç.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>OtoDuctSegmentBaseÇu antities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın), genellikle eksirüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfeMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

I |

.

## Tablo 6.96 IfcDuctSilencer Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kanal Susturucusu (IfcDuctSilencer)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Kanal susturucusu, tipik olarak bir kanal dağıtım sistemine, hava hareketi, fan gürültüsü vb. kaynaklı gürültü seviyelerini bitişik alanda veya susturucu cihazın aşağı akışında azaltmak amacıyla monte edilen bir cihazdır.</td>
<td>FLATOVAL, RECTANGULAR, ROUND, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir OI) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFİNEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((1fcBuiitElement)J&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Hidrolik Çap</td>
<td>,HydraulicDiameter</td>
<td>PsetDuctSilencerTypeCommon</td>
<td>Sayı</td>
<td>Hidrolik çap.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>PsetDuctSilencerIypeCommon</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu.</td>
</tr>
<tr>
<td>Hava Akış Debisi Aralığı</td>
<td>AtFlowRateRange</td>
<td>PsetDuctSilencerTypeCommon</td>
<td>Sayı</td>
<td>Sağlanabilecek hava debisinin olası aralığı</td>
</tr>
<tr>
<td>Çalışma Basıncı Aralığı</td>
<td>li “WorkingPressureRange</td>
<td>PsetDuciSilencerTypeCommon</td>
<td>Sayı</td>
<td>İzin verilen minimum ve maksimum çalışma basıncı (ortam basıncına göre).</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>GrossWeight</td>
<td>OtoDuctSilencerBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Ağırlık</td>
<td>Weight</td>
<td>PsetDuctSilencerTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin toplam ağırlığı.</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>PsetDuctSilencerIypeCommon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum sıcaklık.</td>
</tr>
<tr>
<td>Dış Yalıtımlı</td>
<td>HasExteriorlnsulation</td>
<td>ı PsetDuctSilencerTypeCommon</td>
<td>Mantıksal</td>
<td>Susturucunun dış yalıtımı varsa DOĞRU, yoksa YANLIŞ.</td>
</tr>
</tbody>
</table>

i ;

## Tablo 6.97 IfcElectricAppliance Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Elektrikli Cihaz ((fcElectricAppliance)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Elektrikli cihaz, elektrikle çalışan ve tüketici kullanımına yönelik bir aygıttır.</td>
<td>DISH WASHER, ELECTRIC COOKER, FREE STANDING ELECTRİC HEATER, FREE STANDING FAN, FREE STANDING WATER COOLER, FREE STANDING WATER HEATER, FREEZER, FRIDGE FREEZER, HAND DRYER, KITCHEN MACHİNE, MICROWAVE, PHOTOCOPTER, REFRIGERATOR, TUMBLE DRYER, VENDİNG MACHİNE, WASHING MACHİNE, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED)Jİ olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisna; yaprak sınıflarında ve ((1fcBuiltElement)l&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Metin</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Metin</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoElectricApplianceBas eOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

| , i

## Tablo 6.98 IfcElectricGenerator Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="5">Elektrik Jeneratörü (IfcElectricGenerator) Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Elektrik jeneratörü, mekanik enerjiyi elektrik enerjisine dönüştüren bir makine olan bir motordur.</td>
<td>CHP, ENGINEGENERATOR, STANDALONE, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tüp bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFİNEDİ| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve (NfeBuikElement)l&#x27;i doğrudan ömeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>| |</td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>ı &quot;Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Elektrik Jeneratörü Verimi</td>
<td>ElectricGeneratorEfficienc y</td>
<td>PsetElectricGeneratorTyp eCommaon</td>
<td>Sayı</td>
<td>Çıkış kapasitesinin giriş kapasitesine oranı</td>
</tr>
<tr>
<td>Başlangıç Akım Faktörü</td>
<td>StartCurrentFactor</td>
<td>PsetElectricGeneratorTyp eCommon</td>
<td>Sayı</td>
<td>TEC: Başlangıç akım faktörü, motorun çalıştırılması sırasında oluşacak tepe başlangıç (Oakımının O büyüklüğünü (tanımlar. (o StartCurrentFactor, NominalCurrent (nominal akım) ile çarpılarak başlangıç akımı elde edilir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>,GrossWeight</td>
<td>OtoElectricGeneratorBas eÇuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

## Tablo 6.99 IfcEvaporator Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Evaporatör (IfcEvaporator)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Evaporatör, sıvı haldeki bir soğutucu akışkanın buharlaştığı ve çevresindeki akışkandan 1sı emdiği bir cihazdır.</td>
<td>DİRECT EXPANSION, DİRECT EXPANSION SHELL AND TUBE, DİRECT EXPANSION TUBE IN TUBE, DİRECT EXPANSION BRAZED PLATE, FLOODED SHELL AND TUBE, SHELL AND COİL, USERDEFİNED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tp bilgisi bu özniteliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değeri listeden İİUSERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement)l&#x27;i doğrudan ömeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti.</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetEleciricalDeviceCom mon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetEleciricalDeviceCom mon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Evaporatör Soğutucusu</td>
<td>EvaporatorCoolant</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Metin</td>
<td>Evaporatörde soğutucu olarak kullanılan akışkan.</td>
</tr>
<tr>
<td>Evaporatör Ortam Türü</td>
<td>EvaporatorMedium Type</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Metin</td>
<td>Evaporatör, soğutucu akışkanla 1sı alışverişi yapmak için sıvı tipinde bir akışkan kullanır.; Evaporatör, soğutucu akışkanla ısı alışverişi yapmak için hava kullanır.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>ExtemalSurfaceArea</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Sayı</td>
<td>Dış yüzey alanı (birincil ve ikincil alan).</td>
</tr>
<tr>
<td>İç Soğutucu Hacmi</td>
<td>InteralRefrigerantVolume</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Sayı</td>
<td>Nesnenin iç hacmi (soğutucu akışkan tarafi).</td>
</tr>
<tr>
<td>İç Yüzey Alanı</td>
<td>IntemalSurfaceArea</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Sayı</td>
<td>Evaporatörün iç yüzey alanı.</td>
</tr>
<tr>
<td>İç Su Hacmi</td>
<td>Internal Water Volume</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Sayı</td>
<td>Nesnenin iç hacmi (su tarafı).</td>
</tr>
<tr>
<td>Nominal Isı Transfer Alanı</td>
<td>NominalHeatTransferArea</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Sayı</td>
<td>Nominal toplam ısı transfer katsayısı ile ilişkili nominal ısı transfer yüzey alanı.</td>
</tr>
<tr>
<td>Nominal İsi Transfer Katsayısı</td>
<td>NominalHeatTransferCoef ficient</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Sayı</td>
<td>Nominal ısı transfer alanı ile ilişkili nominal toplam ısı transfer katsayısı.</td>
</tr>
<tr>
<td>Soğutucu Akışkan Sınıfı</td>
<td>RefrigerantClass</td>
<td>PsetEvaporatorTypeCom mon</td>
<td>Metin</td>
<td>Nesne tarafından kullanılan soğutucu akışkan sınıfı., Kloroflorokarbonlar.; Hidrokloroflorokarbonlar.; Hidroflorokarbonlar.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>GrossWeight</td>
<td>OtoEvaporatorBaseOuant ities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

| |

i | | !

## Tablo 6.100 IfcFan Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Fan (IfcFan)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Fan, bir gaza mekanik iş uygulayan bir cihazdır. Bir fanın tipik kullanımı, bina servisleri hava dağıtım sisteminde hava akışı sağlamaktır.</td>
<td>CENTRIFUGAL AİR FOIL, CENTRİFUGAL BACKWARDI NCLINED CURVED, CENTRIFUGAL FORWARD CURVED, CENTRIFUGAL RADIAL, PROPELLOR AXLAL, TUBE AXIAL, VANE AXIAL, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: O1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElementll&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Statik Basınç</td>
<td>NominalStaticPressure</td>
<td>PsetFanTypeCommon</td>
<td>Sayı</td>
<td>Hava akımı içindeki statik basınç, fanın tasarlanan hava dolaşımını sağlamak için aşması gereken basınçtır.</td>
</tr>
<tr>
<td>Nominal Güç Oranı</td>
<td>,NominalPowerRate</td>
<td>PsetFanTypeCommon</td>
<td>Sayı</td>
<td>Nominal fan güç oranı.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>&#x27;NominalPowerConsumpti on</td>
<td colspan="2">Pset EleciricalDeviceCom| — Sayı mon</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>, Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Çalışma Sıcaklık Aralığı</td>
<td>Operation TemperatureRan ge</td>
<td>PsetFanTypeCommon</td>
<td>&#x27; Sayı</td>
<td>İzin verilen çalışma ortam hava sıcaklığı aralığı.</td>
</tr>
<tr>
<td>Hava Çıkış Türü</td>
<td>DischargeType</td>
<td>PsetFanOccurrence</td>
<td>Metin</td>
<td>Fan çıkışındaki bağlantı tipini tanımlar. Duct: Kanal tesisatına çıkış. Screen: Izgara çıkışına çıkış. Louver: Panjur çıkışma çıkış. Damper: Damper çıkışına çıkış.</td>
</tr>
<tr>
<td>Motor Konumu</td>
<td>MotorPosition</td>
<td>PsetFanOccurrence</td>
<td>Metin</td>
<td>Motorun hava akımına göre konumunu tanımlar. InAirStream (HavaAkımında): Fan motoru hava akımı içindedir, OutOfAirStream (HavaAkımıDışında): Fan motoru hava akımı dışmdadır.</td>
</tr>
<tr>
<td>Motor Tahrik Tipi</td>
<td>MotorDriveType</td>
<td>Pset FanTypeCommon</td>
<td>Metin</td>
<td>Doğrudan tahrik, Kayış tahriki, Bağlantı, Diğer motor tahrik tipi, Bilinmeyen motor tahrik tipi.</td>
</tr>
<tr>
<td>Kapasite Kontrol Türü</td>
<td>CapacityControlType</td>
<td>PsetFanTypeCommon</td>
<td>Metin</td>
<td>Giriş kanadı ayarı ile kontrol, Değişken hızlı sürücü ile kontrol, Kanat açı ayarı ile kontrol, Yüksek ve düşük hız arasında geçiş ile kontrol, Çıkış damperi modülasyonu ile kontrol.</td>
</tr>
<tr>
<td>Nominal Dönme Hızı</td>
<td>NominalRotationSpeed</td>
<td>PsetFanTypeCommon</td>
<td>Sayı</td>
<td>Nominal koşullar altında nesnenin dönme hızı. Nominal koşullar altında fan çarkı hızı.</td>
</tr>
<tr>
<td>Çalışma Kriteri</td>
<td>OperationalCriteria</td>
<td>PsetFanTypeCommon</td>
<td>Sayı veya Metin</td>
<td>Maksimum çalışma ortam sıcaklığında çalışma süresi.</td>
</tr>
<tr>
<td>Basınç Eğrisi</td>
<td>PressureCurve</td>
<td>PsetFanTypeCommon</td>
<td>Sayı</td>
<td>Basınç artışı — f (debi).</td>
</tr>
<tr>
<td>Verim Eğrisi</td>
<td>EfficieneyCurve</td>
<td>PsetFanTypeCommon</td>
<td>Sayı</td>
<td>Fan verimliliği — f (debi).</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoFanBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate almmadan hesaplanır.</td>
</tr>
<tr>
<td>Fan Uygulama Türü</td>
<td>ApplicationOfFan</td>
<td>PsetFanOccurrence</td>
<td>Metin</td>
<td>Fanın fonksiyonel uygulaması. Besleme havası fanı, Dönüş havası fanı, Egzoz havası fanı, Yukarıda tanımlanmamış diğer uygulama türü.</td>
</tr>
<tr>
<td>Serpantin Pozisyonu</td>
<td>CoilPosition</td>
<td>PsetFanOÖccurrence</td>
<td>Metin</td>
<td>Bir fan ile serpantin arasındaki ilişkiyi tanımlar. Fan, serpantinin aşağı akışında bulunur, Fan, serpantinin yukarı akışında bulunur.</td>
</tr>
<tr>
<td>Fan Montaj Türü</td>
<td>FanMountingType</td>
<td>PsetFanOccurrence</td>
<td>Metin</td>
<td>Fanın binadaki montaj yöntemini tanımlar.</td>
</tr>
<tr>
<td>Motor Isısının Hava Akımına Oranı</td>
<td>FractionOfMotorHeatToAi rStream</td>
<td>Pset FanOccurrence</td>
<td>Tamsayı</td>
<td>Motor ısısının akışkana salınan kısmı.</td>
</tr>
<tr>
<td>Pervane Çapı</td>
<td>impellerDiameter</td>
<td>PsetFanOccurrence</td>
<td>Tamsayı</td>
<td>Nesnenin çapı — geometrik olarak benzer nesnelerin performansını ölçeklendirmek için kullanılır.</td>
</tr>
</tbody>
</table>

| H | |

, | | |

## Tablo 6.101 IfcFireSuppressionTerminal Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Yangın Söndürme Terminali (IfcFireSuppressionTerminal)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Yangın söndürme terminali, bir yangını söndürecek akışkanı (gaz veya sıvı) iletme amacına sahiptir. Yangın söndürme terminali; bir boru sistemiyle bağlantılı olan ve yangını söndürme görevini yerine getirmek üzere tasarlanan tüm sprinkler, dağıtıcı ve diğer terminal biçimlerini kapsar.</td>
<td>BREECHİNGI NLET, FİRE HYDRANT, FİRE MONİTOR, HOSEREEL, SPRINKLER, USERDEFINED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: o 1) OÖn Tanmlı Tip özniteliğinin değeri listeden İ(USERDEFINEDİ| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((1fcBuihElement|)&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoFireSuppressionTerm inalBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

j

## Tablo 6.102 IfcFooting Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Temel (fcFooting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Temel pabucu, bir yapının yükünü yayarak toprağa ileten bir yapı parçasıdır. Temel pabucu, yüklerin yüzeye yakın bir alana aktarıldığı sığ teme) olarak da tanımlanır.</td>
<td>CAISSON FOUNDATTION, FOOTING BEAM, PAD FOOTING, PILE CAP, STRIP FOOTING, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, öreklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden İLUSERDEFINEDİİ olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve |(IfcBuiltElementlli doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Yük Taşıyan</td>
<td>LoadBearing</td>
<td>PsetFootingCommon</td>
<td>Manttksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlanıp tasarlanmadığını belirtir (DOĞRU) veya tasarlanmadığını (YANLIŞ).</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoFootingBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesit boşlukları gibi imalat özellikleri dikkate alınmaz. Şerit temeller için yol boyunca ölçülür, diğer temeller için ise yatay ölçülerden biridir. Sadece sabitse verilmelidir.</td>
</tr>
<tr>
<td>Genişlik</td>
<td>Width</td>
<td>OtoFootingBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin genişliği. Sadece, nesne sabit kalınlığa (prizmatik) sahipse verilir. Şerit temeller için, temel hattına (veya boyuna eksene) dik olarak ölçülür. Diğer temeller için, yatay boyutlardan biridir. Yalnızca sabit olduğu durumda verilmelidir.</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>Oto FootingBaseOuantities</td>
<td>Sayı</td>
<td>Karakteristik yükseklik. Temelin toplam nominal yüksekliği. Yalnızca sabitse verilmelidir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoFootingBaseÇuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>NetWeight</td>
<td>OtoFootingBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGeneral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengthClass</td>
<td>PsetConcreteElementGeneral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
<tr>
<td>Kesit Alanı</td>
<td>CrossSectionArea</td>
<td>OtoFootingBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin kesitinin (veya profilinin) toplam alanı.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaccArca</td>
<td>OtoFootingBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın), genellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır. a,</td>
</tr>
<tr>
<td>Brüt Yüzey Alanı</td>
<td>GrossSurfaceArea</td>
<td>Ota,FootingBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt alanı, genellikle çevre * uzunluk t 2 * Kesit Alanı olarak hesaplanır. Bu, Dış Yüzey Alanı * (2 x Kesit Alanı) toplamıdır ve yalnızca Dış Yüzey Alanı ve Kesit Alanı ayrı olarak belirlenemediğinde verilecektir.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>GrossVolume</td>
<td>OtoFootingBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoFootingBaseOuantities</td>
<td>, Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özellikleri (kesit boşluklarıvb.) veya açıklıklar ve girintiler dikkate alınarak hesaplanır.</td>
</tr>
</tbody>
</table>

| | | |

| _

## Tablo 6.103 IfcFurniture Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Mobilya (IfcFurniture)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Mobilya, binanın yapısına sabitlenmiş ya da sabitlenmemiş masa, sandalye, dolap gibi tefriş elemanlarını ifade eder.</td>
<td>BED, CHAİR, DESK, FİLE CABINET, SHELE, SOFA, TABLE, TECHNICAL CABINET, USERDEFINED, NOTDEFINED</td>
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
<td>Attribute: ObjeciType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; o 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td colspan="2">. &quot;Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Metin N N JFiyat Poz No&#x27;su.</td>
</tr>
</tbody>
</table>

## Tablo 6.104 IfcGroup Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Grup (HcGroup)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: IfcGroup, herhangi bir nesne grubunun genel bir temsilidir. Grup, nesnelerin mantıksal olarak bir araya getirildiği bir topluluktur. Grup nesnesinin kendisine ait bir konumu bulunmaz ve geometrik bir temsil içermez. Bu nedenle grup, geometrik veya topolojik özelliklere dayanmayan bir ilişkilendirme kapsamında değerlendirilir.</td>
<td>-</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçin</th>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((JSERDEFINEDJ) olarak seçilmişse veya 2) somut ömeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement|)&#x27;i doğrudan örmeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.105 IfcHeatExchanger Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Isı Eşanjörü (fcHeatExchanger)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Isı Eşanjörü, plaka veya gövde-boru tipi eşanjörler gibi, birbirine karışmayan ortamlar arasında ısı transferi sağlamak için kullanılan bir cihazdır.</td>
<td>PLATE, SHELLANDTUBE, USERDEFİNED, NOTDEFİNED</td>
</tr>
<tr>
<th>Türkçe Tanım © (Bilgi Amaçlı)</th>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan üp bilgisi bu özniteliğe girilir: 1) OÖn Tanımlı Tip özniteliğinin değeri listeden İLUSERDEFİNED)| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement|J&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Akış Düzeni</td>
<td>FlowArrangemeni</td>
<td>PsetHeatExchangerType Common</td>
<td>Metin</td>
<td>Isı eşanjörü veya soğutma kulesi için temel akış düzenlemelerini tanımlar: Ters Akış — hava ve su akışı farklı yönlerden girer. Çapraz Akış — hava ve su akışı birbirine dik yönde hareket eder. Paralel Akış — hava ve su akışı aynı yönde girer. Çok Geçişli Akış — birden fazla geçişe sahip ısı eşanjörü düzenlemesidir. Diğer — yukarıda tanımlanmayan diğer 1sı eşanjörü akış düzenlemelerini ifade eder.</td>
</tr>
<tr>
<td>Nominal Yükseklik</td>
<td>NominalHetight</td>
<td>PsetElementSize</td>
<td>Sayı</td>
<td>Nesnenin nominal yüksekliği. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Nominal Uzunluk ı</td>
<td>NominalLengih</td>
<td>PsetElementSize</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal uzunluğu. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Nominal Genişlik</td>
<td>Nominal Width</td>
<td>PsetElementSize</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal genişliği. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoHeatExchangerBaseO uantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

ee

|

## Tablo 6.106 IfcLightFixture Sınıf İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Aydınlatma Armatürü (IfeLightFixture) |</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Aydınlatma Armatürü, bir veya daha fazla lambayı ve isteğe bağlı olarak bu lambaların ışık yayımını kontrol eden, sınırlayan veya değiştiren cihazları barındırmak amacıyla tasarlanmış bir muhafazadır.</td>
<td>DIRECTION SOURCE, POINT SOURCE, SECURITY LIGHTING, USERDEFINED, NOTDEFINED |</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>jNesne Tipi</td>
<td>Attribute: ObjectT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değeri listeden İ((LUSERDEFINED|) olarak seçilmişse veya 2) somut öreklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve /(IfcBuiltElementJl&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Toplam Güç</td>
<td>Total Wattage</td>
<td>PsetLightFixtureTypeCo mmon</td>
<td>Number</td>
<td>Tüm ışık kaynakları takılı haldeyken aydınlatma armatürünün toplam güç tüketimi (watt değeri).</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Kaynak Sayısı</td>
<td>NumberOfSources</td>
<td>PsetLightFixtureTypeCo mmon</td>
<td>Sayı</td>
<td>Kaynak sayısı.</td>
</tr>
<tr>
<td>Aydınlatma Armatürü Montaj Tipi</td>
<td>LightFixtureMountingTyp €</td>
<td>PsetLightFixtureTypeCo mmon</td>
<td>İ . Metin</td>
<td>Aydınlatma armatürleri için mevcut montaj tiplerinden, ihtiyaç duyulanın ,seçilebileceği bir liste.</td>
</tr>
<tr>
<td>Aydınlatma Armatürü YerleştirmeTipi</td>
<td>LightFixturePlacingType</td>
<td>PsetLightFixtureTypeCo mmon</td>
<td>Metin</td>
<td>Aydınlatma armatürleri için mevcut yerleştirme tiplerinden, ihtiyaç duyulanın seçilebileceği bir liste.</td>
</tr>
<tr>
<td>Bakım Faktörü</td>
<td>MaintenanceFactor</td>
<td>Pset LightFixtureTypeCo mmon</td>
<td>Tamsayı</td>
<td>Kir, duman veya eskime nedeniyle lambaların ve yansıtıcı ekipmanların ilk değerlerinden düşüşü için yapılan aritmetik düzeitme.</td>
</tr>
<tr>
<td>Maksimum Plenum Duyulur Isıl Yükü</td>
<td>MaximumPlenumSensible Load</td>
<td>Pset LighiFixtureTypeCo mmon</td>
<td>Sayı</td>
<td>Aydınlatma armatürünün dönüş havası plenumuna aktardığı maksimum veya pik duyulur ısıl yük.</td>
</tr>
<tr>
<td>Maksimum Hacim Duyulur Isıl Yükü</td>
<td>Maximum SpaceSensibleL oad</td>
<td>PsetLightFixtureTypeCo mmon</td>
<td>Sayı</td>
<td>Armatürün iklimlendirilmiş mahal içine aktardığı maksimum veya pik duyulur ısıl yük.</td>
</tr>
<tr>
<td>Duyulur yükün Işınıma Oranı</td>
<td>SensibleLoadToRadiant</td>
<td>PsetLightFixtureTypeCo mmon</td>
<td>Tamsayı</td>
<td>Duyulur ısıl yükün radyant ısıya olan yüzdesi.</td>
</tr>
<tr>
<td>Hat Sayısı</td>
<td>NumberOfPoles</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nesnenin etkileyeceği kutup sayısı. Cihazın işlemeye/iletmeye yönelik tasarlandığı enerjili hat (faz) sayısı.</td>
</tr>
<tr>
<td>Koruyucu Topraklama Bağlantısı Mevcut</td>
<td>HasProtectiveEarth</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Mantıksal</td>
<td>Nesnenin koruyucu topraklama bağlantısına sahip olduğunu (DOĞRU) veya olmadığını (YANLIŞ) gösterir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoLightFixtureBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

| ' | |

## Tablo 6.107 IfcMember Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Eleman (Ifc Mem ber)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: ((IfcMember)), destek noktaları arasında veya ötesinde yük taşımak üzere tasarlanmış yapısal bir elemandır. Taşıyıcı olması zorunlu değildir. Elemanın yönelimi (yatay, düşey veya eğimli olması) tanımı açısından önemli değildir ( ((1fcBeaml| ve ((IfcColumn)J)&#x27;un aksine). ((1feMember)), mimari veya yapısal modelleme bakış açısından doğrusal bir yapısal elemanı temsil eder ve eğer daha özel olarak ((1fcBeamlJ| veya ((1fcColumnj|| olarak ifade edilemiyorsa kullanılmalıdır.</td>
<td>ARCH SEGMENT, BRACE, CHORD, COLLAR, MEMBER, MULLION, PLATE, POST, PURLIN, RAFTER, STAY CABLE, STIFFENING RIB, STRINGER, STRUCTURALCABLE, STRUT, STUD, SUSPENDER, SUSPENSION CABLE, TIEBAR, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>i Türkçe Tanım (Bilgi Amaçlı) |</th>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özmiteliğe girilir. 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement)J&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atıribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys, PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>Pset MemberCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı, Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td>Yük Taşıyan</td>
<td>LoadBearing</td>
<td>PsetMemberCommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlanıp tasarlanmadığını belirtir (DOĞRU) veya tasarlanmadığını (YANLIŞ).</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Lengih</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesitler veya delikler gibi işleme özellikleri dikkate alınmaz.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>GrossWeight</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>NetWeight</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Eğim</td>
<td>Slope</td>
<td>I Pset MemberCommon</td>
<td>Sayı</td>
<td>Eğim açısı — yataya gör relatif (000 derece). Şekil bilgisi, şekil temsilinin yanı sıra kullanılan geometrik parametrelerle birlikte sağlanır. Geometrik parametreler ile şekil özellikleri arasında tutarsızlık OOlması durumunda, geometrik parametreler dikkate alınır. Geometri düzenleme uygulamaları (ör. CAD) için bu değer yalnızca &quot;yazılabilir&quot; olmalıdır.</td>
</tr>
<tr>
<td>Kesit Alanı</td>
<td>CrossSectionArea</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin kesitinin (veya profilinin) toplam alanı.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın), genellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td>Brüt Yüzey Alanı</td>
<td>GrossSurfaceArea</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam orüt alanı, genellikle çevre * uzunluk *2 * Kesit Alanı olarak hesaplanır. Bu, Dış Yüzey Alanı - (2 x Kesit Alanı) toplamıdır ve yalnızca Dış Yüzey Alanı ve Kesit Alanı ayrı olarak belirlenemediğinde verilecektir.</td>
</tr>
<tr>
<td>Net Yüzey Alanı</td>
<td>NetSurfaceArea</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin net yüzey alanı genellikle, olası imalat özelliklerini (kesikler vb.) veya açıklıkları ve girintileri dikkate alarak., çevre * uzunluk - 2 * Kesit Alanı olarak hesaplanır.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>GrossVolume</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoMemberBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özelliklerini (kesit boşlukları vb.) veya açıklıklar ve girintiler dikkate alınarak hesaplanır.</td>
</tr>
</tbody>
</table>

| | | l ‘

|

|

## Tablo 6.108 IfcOpeningElement Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Açıklık Elemanı (IfcOpeningElement)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Açıklık elemanı; açıklık, girinti veya tesisat kanalı gibi boşlukları temsil eder. Fiziksel bir yapı elemanı içinde yer alan bir boşluğu ifade eder. Açıklıklar duvarlara, döşemelere, kirişlere, kolonlara veya diğer elemanlara yerleştirilebilir.</td>
<td>OPENİNG, RECESS, USERDEFİNED, NOTDEFİINED</td>
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
<td>Attribute: ObjeciType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; O) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve /(IfcBuiltElement|l&#x27;i doğrudan ömeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Etiket</td>
<td>Atiribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır. Ni</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>&quot;Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
</tbody>
</table>

,

## Tablo 6.109 IfcOutlet Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Priz (IfcOutlet)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Priz, elektrik enerjisi veya iletişim için bir veya birden fazla fişin takılmasını sağlamak amacıyla belirli bir noktaya monte edilen bir cihazdır.</td>
<td>AUDIO YISUAL OUTLET, COMMUNICATIONS OÜTLET, DATA OUTLET, POWER OUTLET, TELEPHONE OUTLET, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; o1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFİNEDİ! olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve ((IfcBuilhtElementJl&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td colspan="2">Açıklama Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanıradır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Güç Tüketimi</td>
<td>NominalPowerConsumpti on</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nominal toplam güç tüketimi.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Tak-çıkar bağlantı</td>
<td>IsPluggableOutlet</td>
<td>PsetOutletTypeCommon</td>
<td>Mantıksal</td>
<td>Prizin tak-çıkar bir fiş bağlantısını kabul ettiğini ( DOĞRU) ya da sabit bağlantı olduğunu (* YANLIŞ) veya bağlantı biçiminin henüz belirlenmediğini ( BİLİNMEYEN) gösterir.</td>
</tr>
<tr>
<td>Priz Sayısı</td>
<td>NumberOfSockets</td>
<td>PsetOutletTypeCommon</td>
<td>Sayı</td>
<td>Bağlanabilecek priz (soket) sayısı. Tutarsızlık durumunda. portlar üzerinde tanımlanan prizler dikkate alınır.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>GrossWeight</td>
<td>OtoOutletBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenm toplam brüt ağırlığı, ek parçalar olmaksızın ve olasi imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

| | li | i —

## Tablo 6.110 IfcPavement Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Asfalt ((fcPavement)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Yol veya diğer kaplamalı bir alanda, genellikle birden fazla tabakadan oluşan ve araçlar ya da yayalar tarafından gelen yükleri taşıyarak düzgün bir yüzey sağlayan yapı elemanı türüdür. NOT: 1SO 6707-1&#x27;e göre tanım: yol, pist veya benzeri, taban zemini üzerinde yer alan yapı.</td>
<td>FLEXIBLE, RIGID, USERDEFİNED, NOTDEFİINED</td>
</tr>
<tr>
<th>e Türkçe Tanım (Bilgi Amaçlı)</th>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut ali tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED)||) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve |fIfcBuiltElemenill&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Etiket</td>
<td>Attribute: Tag</td>
<td>-</td>
<td>Sayı veya Metin</td>
<td>Bir ürünün belirli bir örneğindeki etiket tanımlayıcısı, örneğin seri numarası veya konum numarasıdır. Bu, yerleştirilmiş örnek düzeyindeki tanımlayıcıdır.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.111 IfcPile Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Kazık (IfecPile))</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir kazık, bir yükü desteklemek amacıyla yere dik olarak yerleştirilmiş ince bir ahşap, beton veya çelik yapısal elemandır. Ayrıca, yüklerin daha derin yer altı katmanlarına aktarılmasıyla karakterize edilen derin temele de kazık denir.</td>
<td>BORED, DRIVEN, JETGROUTING, COHESİON, FRICTTON, SUPPORT, USERDEFINED, NOTDEFINED</td>
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
<td>Atiribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. o 1) Ön Tanımlı Tip özniteliğinin değeri listeden (NUSERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve |jIfcBuiltElement)|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>|</td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Taşıyıcı</td>
<td>LoadBearing</td>
<td>PsetPileCommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir .</td>
</tr>
<tr>
<td>&quot;Uzunluk</td>
<td>Length</td>
<td>OtoPileBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesitler veya kesit boşlukları gibi işleme özellikleri dikkate alınmaz.</td>
</tr>
<tr>
<td>“Brüt Ağırlık</td>
<td>Gross Wcight</td>
<td>OtoPileBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>Net Weight</td>
<td>OtoPileBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplamı net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGen era)</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengthCla ss</td>
<td>PsetConcreteElementGen eral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı geneilikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
<tr>
<td>Kesit Alanı</td>
<td>CrossSectionArea</td>
<td>OtoPileBaseÇuantities</td>
<td>Sayı</td>
<td>Nesnenin kesitinin (veya profilinin) toplam alanı.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>OtoPileBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın). genellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td>Brüt Yüzey Alanı</td>
<td>GrossSurfaceArea</td>
<td>OtoPileBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt alanı, genellikle çevre * uzunluk *- 2 * Kesit Alanı olarak hesaplanır. Bu, Dış Yüzey Alanı * (2 x Kesit Alanı) toplamıdır ve yalnızca Dış Yüzey Alanı ve Kesit Alanı ayrı olarak belirlenemediğinde verilecektir.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>Gross Volume</td>
<td>OtoPileBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoPileBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin topiam net hacmi, olası imalat özellikleri (kesit boşlukları vb.) veya açıklıklar ve girintiler dikkate alınarak hesaplanır.</td>
</tr>
</tbody>
</table>

| i |

## Tablo 6.112 IfcPipeFitting Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Boru Bağlantı Parçası (IfcPipeFitting)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Boru bağlantı parçası, borulu akış dağıtım sisteminde bir bağlantı veya geçiş elemanıdır; boru segmentlerini birleştirmek için kullanılır ve akışkanın yönü veya debisi gibi akış özelliklerinde değişikliklere neden olur.</td>
<td>BEND, CONNECTOR, ENTRY, EXFT, JUNCTION, OBSTRUCTION, TRANSITION, USERDEFINED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: i) Ön Tanımlı Tip özniteliğinin değeri listeden |((USERDEFINEDJJ olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve JJ(IfcBuiltElemenilli doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute (IfcRelAssociatesMaterial &gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak ıçın kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti/ İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Renk</td>
<td>Colour</td>
<td>PsetPipeFittingOccurre nce</td>
<td>Metin</td>
<td>Bu nesnenin rengi.</td>
</tr>
<tr>
<td>Basınç Sınıfı</td>
<td>PressureClass</td>
<td>PsetPipeFittingTypeCo mmon</td>
<td>Sayı</td>
<td>Nesnenin nominal basınç sınıfı. Bağlantı parçasının test veya nominal basınç sınıflandırması.</td>
</tr>
<tr>
<td>Basınç Aralığı</td>
<td>PressurgeRange</td>
<td>PsetPipeFittingTypeCo mmon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum çalışma basıncı (ortam basıncına göre).</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>PsetPipeFittingiypeCo mmon</td>
<td>Metin</td>
<td>İzin verilen maksimum ve minimum sıcaklık.</td>
</tr>
<tr>
<td>Bağlantı Elemanı Kayıp Faktörü</td>
<td>FittingLossFactor</td>
<td>PsetPipeFittingTypeCo mmon</td>
<td>Sayı</td>
<td>Bağlantı parçası boyunca sürtünmeden kaynaklanan basınç kaybını belirleyen bir katsayı.</td>
</tr>
<tr>
<td>Brüt Kesit Alani</td>
<td>GrossCrossSectionArea</td>
<td>OtoPipeFittingBaseOua ntities</td>
<td>Sayı</td>
<td>Kesit alanı. Boru bağlantı elemanının kendisini ve iç akış alanını da içerir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoPipeFittingBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoPipeFittingBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Kesitin orta noktasından hesaplanır ve bağlantı ağzı girişinden bağlantı ağzı çıkışına kadar olan akış yolu boyunca olan mesafeye eşittir. Bağlantı parçaları için, en uzun akış yolunun uzunluğunu gösterir.</td>
</tr>
<tr>
<td>Net Kesit Alanı</td>
<td>NetCrossSectionArea</td>
<td>Ço,PipeFittingBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin kesit alanı. Boru bağlantı parçaları dahil, içakış alanı hariç.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>NetWeight</td>
<td>OtoPipeFittingBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalardan bağımsız olarak ve olası imalat özellikleri (kesit boşlukları vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır. Tasarlandığı şekilde içerdiği sıvı dahil olmak üzere boru bağlantı parçasının ağırlığı.</td>
</tr>
<tr>
<td>Dış Yüzey Alanı</td>
<td>OuterSurfaceArea</td>
<td>OtoPipeFittingBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin yüzeylerinin toplam alanı (uç kesit alanları dikkate alınmaksızın), igenellikle ekstrüzyon durumunda çevre * uzunluk olarak hesaplanır.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (JfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik 5355 Beton C25)</td>
</tr>
</tbody>
</table>

1

|

## Tablo 6.113 IfcPipeSegment Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Boru Segmenti (IfcPipeSegment)</td>
<td>m l On Tanımlı Tip Listesi İ</td>
</tr>
<tr>
<td colspan="4">Tanım: Boru segmenti, tipik olarak bir boru şebekesinin iki bölümünü birleştirmek için kullanılır.</td>
<td>CULVERT, FLEXIBLESEGMENT, RIGIDSEGMENT, GUTTER, | SPOOL, USERDEFINED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: . 1) OÖn Tanımlı Tip özniteliğinin değeri listeden ((USERDEFİNED|) olarak seçilmişse veya 2) somut ömeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((1fcBuilElemeniJ)&#x27;i doğrudan ömeklendirirken geçerlidir. a, ,</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(IfcRelAssoci atesMaterial&gt;IfcMateri al): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(IfcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>PsetPipeSegmentTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu.</td>
</tr>
<tr>
<td>İç Çap</td>
<td>InnerDiameter</td>
<td>PsetPipeSegmentTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin iç çapı.</td>
</tr>
<tr>
<td>Dış Çap</td>
<td>OuterDiameter</td>
<td>PsetPipeSegmentTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin dış çapı.</td>
</tr>
<tr>
<td>Basınç Aralığı</td>
<td>PressureRange</td>
<td>PsetPipeSegmentTypeCommon</td>
<td>Sayı</td>
<td>İzin verilen maksimum ve minimum çalışma basıncı (ortam basıncına göre).</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>PsetPipeFittingTypeCommon</td>
<td>Metin</td>
<td>İzin verilen maksimum ve minimum sıcaklık.</td>
</tr>
<tr>
<td>Çalışma Basıncı</td>
<td>WorkingPressure</td>
<td>PsetPipeSegmentTypeCommon</td>
<td>Sayı</td>
<td>Çalışma basıncı.</td>
</tr>
<tr>
<td>Renk</td>
<td>Colour</td>
<td>PsetPipeSegmentOccurrence</td>
<td>Metin</td>
<td>Bu nesnenin rengi.</td>
</tr>
<tr>
<td>Eğim</td>
<td>Gradient</td>
<td>PsetPipesegmentOccurrence</td>
<td>Sayı</td>
<td>Boru segmentinin eğimi,</td>
</tr>
<tr>
<td>Boru Alt Kotu</td>
<td>InvertElevatton</td>
<td>Pset PipeSezmentOccurrence</td>
<td>Sayı</td>
<td>Proje için belirlenen datuma göre taban kotu.</td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
</tbody>
</table>

|

Attribute (IfcRelAssociatesMaterial>IfcMaterial): Name* bilgisi giriliken: "Malzeme İsmi. Dayanım” formatı kullanılmalıdır. (Omek:Celik $355 |

,Beton C25) N |

## Tablo 6.114 IfePump Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Pompa (IfcPump)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Pompa, akışkanlara veya çamurlara mekanik enerji aktararak bunların bir kanal veya boru sistemi içinde taşınmasını sağlayan ekipmandır. Pompanın tipik bir kullanımı, bina dağıtım sisteminde soğutulmuş su veya ısıtma sıcak suyunun dolaştırılmasıdır. ii</td>
<td>CIRCULATOR, END SUCTION, SPLIT CASE, SUBMERSIBLE PUMP, SUMP PUMP, VERTICAL INLINE, VERTICAL TURBINE, Ni © USERDEFİNED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden |((USERDEFINED|| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElementll&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>i Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Bağlantı Ölçüsü</td>
<td>ConnectionSize</td>
<td>PsetPumpTypeCommon</td>
<td>Sayı</td>
<td>Nesnenin bağlantı boyutu.</td>
</tr>
<tr>
<td>Akış Direnci Aralığı</td>
<td>FlowResistanceRange</td>
<td>PsetPumpTypeCommon</td>
<td>Metin</td>
<td>Akışkanın pomnpalanmakta olduğu izin verilen sürtünme direnci aralığı.</td>
</tr>
<tr>
<td>Nominal Akım</td>
<td>RatedCurrent</td>
<td>PsetElectricalDeviceCommon</td>
<td>Sayı</td>
<td>Cihazın, tasarımına göre taşıyabileceği akım.</td>
</tr>
<tr>
<td>Nominal Voltaj</td>
<td>RatedVoltage</td>
<td>Pset Electrical DeviceCommon</td>
<td>Sayı</td>
<td>Bir cihazın (çalışmak üzere) sertifikalandırıldığı izin verilen voltaj aralığı. Bu değerin üst sınırı maksimum kabul edilir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoPumpBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Pozitif Emme Yüksekliği</td>
<td>NetPositiveSuctionHead</td>
<td>i — PsetPumpTypeCommon</td>
<td>Sayı</td>
<td>, Kavitasyonu önlemek için pompa girişinde gerekli minimum sıvı basıncı.</td>
</tr>
<tr>
<td>Nominal Dönme Hızı</td>
<td>NominalRotationSpeed</td>
<td>PsetPumpTypeCommon</td>
<td>Sayı</td>
<td>Nominal koşullar altında nesnenin dönme hızı. Nominal koşullar aitında pompanın dönme hızı.</td>
</tr>
<tr>
<td>Sıcaklık Aralığı</td>
<td>TemperatureRange</td>
<td>Pset PumpTypeCommon</td>
<td>Metin</td>
<td>İzin verilen maksimum ve minimum sıcaklık. j Akışkan sıcaklığının izin verilen çalışma arahığı.</td>
</tr>
<tr>
<td>Pervane Çapı</td>
<td>ImpellerDiameter</td>
<td>PsetPumpOccurrence</td>
<td>Sayı</td>
<td>Nesnenin çapı — geometrik olarak benzer nesnelerin performansını ölçeklendirmek için kullanılır.</td>
</tr>
</tbody>
</table>

| | |

## Tablo 6.115 IfcRailing Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="3">Korkuluk (IfcRailing)</td>
<td colspan="2">Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="3">Tanım: Korkuluk, insan veya araç dolaşım alanlarının bitişiğinde ya da bazı mekân sınırlarında, duvarların yerine veya duvarları tamamlayıcı bir eleman olarak kullanılan çerçeve biçimindeki bir yapıdır. İnsanlara fiziksel destek sağlamak veya düşme ya da çarpışma sonucu oluşabilecek yaralanma ya da hasarları önlemek amacıyla tasarlanmıştır.</td>
<td colspan="2">HAND RAJL, GUARD RAJL, BALUSTRADE, USERDEFİNED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir... 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement)|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute(lfcRelAssociates Material&gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>(fcMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su. a,</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>PsetRailingCommon</td>
<td>Sayı</td>
<td>Karakteristik yükseklik. Zeminin veya merdivenin üzerindeki korkuluğun üst yüksekliğidir. Boyut bilgisi, şekil gösterimine ve içinde kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde (property set) belirtilen boyut özeilikleri ile geometrik parametreler arasında bir tutarsızlık olması durumunda, geometrik parametreler dikkate alınır...</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfeMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

' | |

## Tablo 6.116 IfcRamp Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Rampa (IfcRamp)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Rampa, farklı kotlardaki iki döşeme seviyesini birbirine bağlayan dikey bir geçiş yoludur ve insan dolaşımını sağlar. Ara bir döşeme plağı olarak bir sahanlık içerebilir. Bir rampa normalde basamak içermez.</td>
<td>STRAIGHT RUN RAMP, TWO STRAİGHT RUN RAMP, OUARTER TURN RAMP, TWO OUARTER TURN RAMP, HALF TURN RAMP, SPIRAL RAMP, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan üp bilgisi bu özniteliğe girilir; . 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve |(1fcBuiltElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirici açıklamalar paylaşmak için isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>: Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Gerekli Eğim</td>
<td>ReguiredSlope</td>
<td>Pset RampCommon</td>
<td>Sayı</td>
<td>Nesnenin yataya göre gerekli eğim açısı (0,0 derece). Geçerli yapı yönetmeliğine veya ek gerekliliklere göre geçit için gerekli maksimum eğim.</td>
</tr>
</tbody>
</table>

H

## Tablo 6.117 IfcRoad Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Yol (IfcRoad)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Karayolları, caddeler, bisiklet ve yaya yolları dâhil ancak demiryolları hariç olmak üzere, bir yerden başka bir yere seyahati sağlamak amacıyla kara üzerinde inşa edilen bir güzergâhtır. Bir tesis türü olarak yol, yol projesinin bileşenleri için (örneğin tasarım, inşaat veya bakım gibi herhangi bir çalışma) proje yapısı hiyerarşisinde temel unsuru oluşturur.</td>
<td>BICYCLE CROSSING, BUS STOP, CARRIAGEWAY, CENTRAL ISLAND, CENTRAL RESERVE, HARD SHOULDER, INTERSECTION, LAY-BY, PARKING BAY, PASSING BAY, PEDESTRIAN CROSSING, REFUGE ISLAND, ROAD SEGMENT, ROAD SIDE, ROAD SIDE PART, ROADWAY PLATEAU, ROUNDABOUT, SHOULDER, SIDEWALK, SOFT SHOULDER, TOLL PLAZA, TRAFFIC ISLAND, TRAFFIC LANE, USERDEFINED, NOTDEFİNED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 01) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINED|) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement)l&#x27;i doğrudan ömeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzeilikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
</tbody>
</table>

## Tablo 6.118 IfcRoadPart Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Yol Parçası (IfcRoadPart)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir yolun parçası.</td>
<td>BICYCLE CROSSING, BUS STOP, CARRIAGEWAY, CENTRAL ISLAND, CENTRAL RESERVE, HARD SHOULDER, INTERSECTION, LAY-BY, PARKING BAY, PASSING BAY, PEDESTRJAN CROSSING, REFUGE ISLAND, ROAD SEGMENT, ROAD SIDE, ROAD SIDE PART, ROADWAY PLATEAU, ROUNDABOUT, SHOULDER, SIDEWALK, SOFT SHOULDER, TOLL PLAZA, TRAFFIC ISLAND, TRAFFIC LANE, USERDEFİNED, NOTDEFİNED</td>
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
<td>Attribute: Objectl&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. ömeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir. o1) Ön Tanımlı Tip özniteliğinin değeri listeden MUSERDEFINEDİ| olarak seçilmişse veya 2) somut öreklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak smıflarında ve ((IfcBuiltElement)|&#x27;i doğrudan ömeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti/ İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim |Fiyat Poz No&#x27;su.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.119 IfcRoof Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Çatı (IfcRoof)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Çatı, bir binanın en üst kısmını örten yapı elemanıdı; binayı hava koşullarının etkilerine karşı korur.</td>
<td>FLAT ROOF, SHED ROOF, GABLE ROOF, HIP ROOF, HIPPED GABLE ROOF, GAMBREL ROOF, MANSARD ROOF, BARREL ROOF, RAINBOW ROOF, BUTTERFLY ROOF, PAYVILION ROOF, DOME ROOF, FREEFORM, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; o1) Ön Tanımlı Tip özniteliğinin değeri listeden ((WSERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve /(IfcBuiltElement)l&#x27;i doğrudan örmeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>i Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Isıl İletkenlik</td>
<td>ThermalTransmittance</td>
<td>PsetRoofCommaon</td>
<td>Sayı</td>
<td>&quot;Bir bileşenin, ısı akışı yönünde (tüm malzemeleri içeren) ısı iletkenlik katsayısı (U-Value).</td>
</tr>
<tr>
<td>Taşıyıcı</td>
<td>.LoadBearing</td>
<td>PsetRoofCommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlandığını (DOĞRU) veya |tasarlarmadığını (YANLIŞ) belirtir .</td>
</tr>
</tbody>
</table>

| tas A

## Tablo 6.120 IfcSanitaryTerminal Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Sıhhi Terminal (IfcSanitaryTerminal)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Sıhhi terminal, genellikle su ile beslenen ve içme, temizlik veya atık suyun uzaklaştırılması için kullanılan sabit bir cihaz veya terminaldir ya da böyle bir cihaz veya terminal ile doğrudan kullanılan bir ekipman öğesidir.</td>
<td>BATH, BIDET, CISTERN, SHOWER, SINK, SANITARY FOUNTAJN, TOILET PAN, URINAL, WASH HAND BASIN, WC SEAT, USERDEFINED, NOTDEFINED</td>
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
<td>Attribute: ObjectT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDJ) olarak seçilmişse veya 2) somut örreklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuütElement)|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozÖzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Nominal Derinlik</td>
<td>NominalDepth</td>
<td>Pset SanitaryTerminalTyp eCommon</td>
<td>Sayı</td>
<td>Nesnenin nominal derinliği.</td>
</tr>
<tr>
<td>Nominal Uzunluk</td>
<td>NominalLength</td>
<td>PsetSanitaryTerminalTyp eCommon</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal uzunluğu. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Nominal Genişlik</td>
<td>Nominal Widih</td>
<td>PsetSanitaryTerminalTyp eCommon</td>
<td>Sayı</td>
<td>Nesnenin toplam nominal genişliği. Boyut bilgisi, şekil temsiline ve kullanılan geometrik parametrelere ek olarak verilir. Ekli özellik setinde sağlanan geometrik parametreler ile boyut özellikleri arasında tutarsızlık olması durumunda, geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Renk</td>
<td>Colour</td>
<td>PsetSanitaryTerminalTyp eCommon</td>
<td>Metin</td>
<td>Bu nesnenin rengi.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoSanitaryTerminalBas eOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (Kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.121 IfcSign Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Tabela (IfcSign)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Levha (tabela), yazılı, sembolik veya başka bir biçimde bilgi ya da talimat veren görsel bir bildirimdir. Tabelalar pasiftir; en yaygın biçimi görsel panodur. IfcSign örneği, duvar gibi bir yüzeye uygulanan bir panelin yerleştirilmiş veya bir Sinyal Bileşimi içinde toplanan birden fazla tabela örneği yerleştirilmesini ve ilgili taşıyıcı yapısal elemanlarını ifade eder.</td>
<td>MARKER, PICTORAL, MIRROR, USERDEFİNED, NOTDEFİNED</td>
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
<td>Attribute: ObjeciType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanmlı Tip özniteliğinin değeri listeden ((USERDEFINEDİJ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su. Ni</td>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>PsetSignCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış sleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>OtoSignBaseOuantities</td>
<td>Sayı</td>
<td>| Karakteristik yükseklik.</td>
</tr>
<tr>
<td>Genişlik</td>
<td>Width</td>
<td>OtoSignBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin genişliği. Yalnızca nesne sabit kalınlığa (prizmatik) sahipse verilir.</td>
</tr>
<tr>
<td>Kategori</td>
<td>Category</td>
<td>PsetSignCommon</td>
<td>Metin</td>
<td>Popülasyondaki aktörlerin dahil olduğu kategorinin tanımlanması</td>
</tr>
<tr>
<td>Dokunsal İşaretleme</td>
<td>TactileMarking</td>
<td>PsetSignCommon</td>
<td>Metin</td>
<td>Elemanın Dokunsal İşaretleme türü.</td>
</tr>
<tr>
<td>Kalınlık</td>
<td>Thickness</td>
<td>OtoSignBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin geometrik kalınlığı.</td>
</tr>
<tr>
<td>Ağırlık</td>
<td>Weight</td>
<td>OtoSignBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam ağırlığı.</td>
</tr>
</tbody>
</table>

| |

|

## Tablo 6.122 IfeSite Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Saha (1feSite)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Saha, projenin inşaatının gerçekleştirileceği, suyla kaplı olabilecek sınırları belirli bir kara alanıdır. Bir saha, bina inşa etmek, mevcut yapıları yenilemek veya yıkmak ya da diğer inşaatla ilgili geliştirme faaliyetleri için kullanılabilir.</td>
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
<td>Bileşim Türü</td>
<td>Attribute:CompositionType</td>
<td>-</td>
<td>Metin</td>
<td>Önceden tanımlı mekânsal yapı elemanının kendisini mi, bir bütününü (kompleksi) mü yoksa bir parçasını mı temsil ettiğini belirtir. Bu değerlendirme her mekânsal yapı elemanı alt tipi için ayrı ayrı yapılır. Eğer bu değer girilmemişse, varsayılan değer &quot;ELEMENT&quot; olarak uygulanır.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute:Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Brüt Alan</td>
<td>GrossArea</td>
<td>OtoSiteBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin brüt alanı. Boşluklar, girintiler, çıkıntılar ve kesit boşlukları dikkate alınmaz.</td>
</tr>
<tr>
<td>İç Konum</td>
<td>InternalLocation</td>
<td>Pset Address</td>
<td>Metin</td>
<td>Bir organizasyon tarafından, kurum içi posta teslimatı amacıyla tanımlanan adres.</td>
</tr>
<tr>
<td>Yapılaşabilir Alan</td>
<td>BuildableArea</td>
<td>PsetSiteCommon</td>
<td>Sayı</td>
<td>Yerel imar yönetmeliklerine (Planlı Alanlar İmar Yönetmeliğine) göre ifade edilen, arsa kullanım alanının azami değeridir.</td>
</tr>
<tr>
<td>Bina Yükseklik Sınırı</td>
<td>BuildingHeightLimit</td>
<td>PsetSiteCommon</td>
<td>Sayı</td>
<td>Bu arsa üzerindeki binalar için yerel imar yönetmeliklerine (Planlı Alanlar İmar Yönetmeliğine) göre izin verilen azami bina yüksekliğidir.</td>
</tr>
<tr>
<td>Brüt Çevre</td>
<td>GrossPerimeter</td>
<td>OtoSiteBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin dış sınırı boyunca ölçülen brüt çevresidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Description</td>
<td>Pset Address</td>
<td>Metin</td>
<td>Nesnenin açıklamasıdır.</td>
</tr>
<tr>
<td>Posta Kutusu</td>
<td>PostalBox</td>
<td>Pset Address</td>
<td>Metin</td>
<td>Tanımlı bir posta kutusuyla ilişkilendirilen adrestir.</td>
</tr>
<tr>
<td>Posta Kodu</td>
<td>PostalCode</td>
<td>Pset Address</td>
<td>Metin</td>
<td>Ülkenin posta servisi tarafından kullanılan koddur.</td>
</tr>
</tbody>
</table>

| |

## Tablo 6.123 IfcSlab Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Döşeme (IfcSlab)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Döşeme, düşey olarak bir hacmi kapatabilen yapı bileşenidir. Döşeme, alt taşıyıcıyı (kat döşemesi) veya üst katı (çatı döşemesi) sağlayabilir ve bir binadaki herhangi bir mekânda yer alabilir.</td>
<td>APPROACH SLAB, BASE SLAB, FLOOR, LANDING, PAYING, ROOF, SIDEWALK, TRACK SLAB, WEARING, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özmiteliğe girilir: o) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFİNEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve (JIfcBuiltElementil&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td colspan="2">Metin Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Taşıyıcı</td>
<td>LoadBearing</td>
<td>PsetSlablommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlanıp tasarlanmadığını belirtir (DOĞRU) veya tasarlanmadığını (YANLIŞ).</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoSlabBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Sadece dikdörtgen olması durumunda girilir.</td>
</tr>
<tr>
<td>Genişlik</td>
<td>Width</td>
<td>OtoSlabBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin genişliği. Sadece, nesne sabit kalınlığa (prizmatik) sahipse verilir.</td>
</tr>
<tr>
<td>Derinlik</td>
<td>Depth</td>
<td>OtoSlabBaseÇuantities</td>
<td>Sayı</td>
<td>Nesnenin derinliği. Döşemenin derinliği (döşemenin izdüşümsüz - projeksiyonu alınmamış taban alanının bir doğrultudaki derinliği). Yalnızca döşemenin dikdörtgen biçiminde olduğu durum için verilmelidir.</td>
</tr>
<tr>
<td>Net Alan</td>
<td>NetArea</td>
<td>OtoSlabBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net alanı. Açıklıklar, girintiler ve kesit boşlukları çıkarılır; çıkıntılar ise eklenir. Nesnenin çıkıntılı alanını belirtir. Sadece prizmatik olduğunda verilir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoSlabBaseÇuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>Net Weight</td>
<td>OtoSlabBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalardan bolmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGe neral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengthCla ss</td>
<td>PsetConcreteElementGe neral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
<tr>
<td>Eğim Açısı</td>
<td>PitchAngle</td>
<td>PsetSlabCommon</td>
<td>Sayı</td>
<td>Döşeme, çatı bileşeni olarak kullanıldığında yataya göre eğim açısı (çatı bileşeni olarak kullanılmayan durumlarda O derece olarak belirtilir veya belirtilmez). Şekil bilgisi, şekil gösterimine ve kullanılan geometrik parametrelere ek olarak sağlanır. Geometrik parametreler ve şekil özellikleri arasında tutarsızlık durumunda, ekli özellikte sağlanan geometrik parametreler dikkate alınır.</td>
</tr>
<tr>
<td>Brüt Alan</td>
<td>GrossArea</td>
<td>OtoSlabBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin brüt alanı. Açıklıklar, girintiler, çıkıntılar ve kesit boşlukları dikkate alınmaz. Elemanın ekstrüzyon (uzatılmış) alanını belirtir. Yalnızca elemanın prizmatik olduğu durumda verilir.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>GrossVolume</td>
<td>OtoSlabBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoSlabBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özellikleri (kesit boşlukları vb.) veya açıklıklar ve girintiler dikkate alınarak hesaplanır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.124 IfeSolarDevice Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Güneş Enerjisi Cihazı (IfcSolarDevice)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Güneş enerjisi cihazı, güneş radyasyonunu elektrik akımı veya ısıl enerji gibi diğer enerji türlerine dönüştürür.</td>
<td>SOLAR COLLECTOR, SOLAR PANEL, USERDEFINED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değer listeden ((USERDEFINEDJJ olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa, İkinci durum. bazı istisnai yaprak sınıflarında ve (J1fcBuiltElementl)&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Atiribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellik$eti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Brüt Alan</td>
<td>GrossArea</td>
<td>OtoSolarDeviceBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin brüt alanı. Açıklıklar, girintiler, çıkıntılar ve kesit boşlukları dikkate alınmaz. Dış çerçeveyi de kapsar.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>GrossWeight</td>
<td>OtoSolarDeviceBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.125 IfcSpace Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Mahal (IfcSpace)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Bir mahal, gerçek veya varsayımsal olarak sınırlandırılmış bir alanı veya hacmi temsil eder. Mekanlar, bir bina içinde belirli işlevleri yerine getiren alanlar veya hacimlerdir.</td>
<td>SPACE, PARKING, GFA, INTERNAL, EXTERNAL, USERDEFİNED, NOTDEFİNED</td>
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
<td>Atiribute:Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır (EK-5 Tablo 3.1 ve 3.2&#x27;de verilen isimler birleştirilerak kullanılabilir)</td>
</tr>
<tr>
<td>Bileşim Türü</td>
<td>Attribute:CompositionTyp e</td>
<td>-</td>
<td>Metin</td>
<td>Önceden tanımlı mahal yapı elemanının kendisini mi, bir bütününü (kompleksi) mü yoksa bir parçasını mı temsil ettiğini belirtir. Bu değerlendirme her mahal yapı elemanı alt tipi için ayrı ayrı yapılır. Eğer bu değer girilmemişse, varsayılan değer &quot;ELEMENT&quot; olarak uygulanır.</td>
</tr>
<tr>
<td>Uzun İsim</td>
<td>Attribute:Long Name</td>
<td>-</td>
<td>Metin</td>
<td>Referans amaçlı olarak kullanılan bağlamın uzun adı (EK-3 Tablo 3.2&#x27;de verilen uzun isimler kullanılabilir)</td>
</tr>
<tr>
<td>Nesne Tipi</td>
<td>Atiribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDJ| olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa . İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuihElement|l&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Karakteristik yükseklik.</td>
</tr>
<tr>
<td>Çıta</td>
<td>Molding**</td>
<td>PsetSpaceCoveringReguir ements</td>
<td>Metin</td>
<td>Mahal tavanı çevresindeki çıtanın malzemesini veya yapımını belirtmek amacıyla kullanılan etiket. Etiket, mahal listesi bilgileri için kullanılır. Malzeme bilgisi, kendi şekil gösterimine ve malzeme atamasına sahip bir IfeCovering (type-MOLDING) nesnesinin bulunmaması durumunda sağlanır. Tutarsızlık halinde IfcCovering elemanlarına atanmış malzeme dikkate alınır.</td>
</tr>
<tr>
<td>Çıta Yüksekliği</td>
<td>MoldingHeight**</td>
<td>PsetSpaceCoveringReguir ements</td>
<td>Sayı</td>
<td>Çıtanın yüksekliği. Yükseklik bilgisi, kendi şekil gösterimine ve malzeme atamasına sahip bir IfcCovering (typexMOLDING) nesnesinin bulunmaması durumunda sağlanır. Tutarsızlık halinde IfcCovering elemanlarına atanmış yükseklik dikkate alınır.</td>
</tr>
<tr>
<td>Bitmiş Tavan Yüksekliği</td>
<td>FinishCeilingHeight</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Askı tavan yüksekliği. Bitmiş tavan yüksekliği (döşeme üst kotundan asma tavan alt kotuna kadar). Yalnızca mahalde sabit yükseklikte bir asma tavan varsa girilir.</td>
</tr>
<tr>
<td>Zemin Kaplama Yüksekliği</td>
<td>FinishFloorHeight</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Döşeme yüksekliği (kaplamasız temel döşeme üstünden bitmiş döşeme kotuna kadar). Yalnızca mahalde sabit döşeme yüksekliği varsa girilir.</td>
</tr>
<tr>
<td>Brüt Çevre</td>
<td>GrossPerimeter</td>
<td>OtoSpaceBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin dış sınırı boyunca ölçülen brüt çevresidir. Döşeme seviyesinde ölçülür; sanal sınırlar ve açıklıklar (örneğin kapılar) tarafından oluşturulan çevre bölümleri de dâhil olmak üzere mahalin tüm kenarları dikkate alınır.</td>
</tr>
<tr>
<td>Net Çevre</td>
<td>NetPerimeter</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Bu mekânın döşeme seviyesindeki net çevre uzunluğu. Sanal sınırlar ve açıklıklar (örneğin kapılar) tarafından oluşturulan çevre bölümlerini hariç tutar. Süpürgelik hesaplarında kullanılan ölçüdür ve kolon gibi iç sabit elemanların çevresini içerebilir.</td>
</tr>
<tr>
<td>Brüt Kat Alanı</td>
<td>GrossFloorArea</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Mahal yapı elemanı içindeki tüm brüt kat alanlarının toplamıdır. Bina katındaki yapı elemanlarının alanlarını içerir. Katla ilişkilendirilmiş mekân ve yapı elemanlarının miktarlarına ek olarak belirtilebilir. Tutarsızlık durumunda, mekân ve yapı elemanlarının bireysel miktarları geçerlidir.</td>
</tr>
<tr>
<td>Net Kat Alanı</td>
<td>NetFloorArea</td>
<td>OtoSpaceBaseÇOuantities</td>
<td>Sayı</td>
<td>Tüm net kullanılabilir döşeme alanlarının toplamıdır. Mahal içindeki elemanların (kolonlar, iç duvarlar, sabit mobilyalar vb.), döşeme boşluklarının veya diğer çıkıntılı elemanların kapladığı alanı hariç tutar. Değişken yükseklikler dikkate alınmaz (örneğin minimum kafa kurtarma yüksekliği altında kalan alanlar için eksiltme yapılmaz).</td>
</tr>
<tr>
<td>Brüt Duvar Alanı</td>
<td>GrossWallArea</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Mekân tarafından sınırlandırılan tüm duvar (ve kolon gibi diğer düşey sınır elemanları) alanlarının toplamı. Duvar alanı içindeki elemanların (kapılar, pencereler, diğer açıklıklar vb.) kapladığı alanı içerir.</td>
</tr>
<tr>
<td>Net Duvar Alanı</td>
<td>Net WallArea</td>
<td>OtoSpaceBaseÇuantities</td>
<td>Sayı</td>
<td>Mahal tarafından sınırlandırılan tüm duvar (ve kolon gibi diğer düşey sınır elemanları) alanlarının toplamı. Duvar alanı içindeki elemanların (kapılar. pencereler. diğer açıklıklar vb.) kapladığı alanı hariç tutar.</td>
</tr>
<tr>
<td>Brüt Tavan Alanı</td>
<td>GrossCeilingArea</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Mekânın tüm tavan alanlarının toplamı. Mekân içindeki elemanların (kolonlar, iç duvarlar vb.) kapladığı alanı içerir. Tavan alanı gerçek alandır (izdüşüm alanı değil; örneğin eğimli tavanlarda).</td>
</tr>
<tr>
<td>Net Tavan Alanı</td>
<td>NetCeilingârea</td>
<td>OtoSpaceBaseÇOuantities</td>
<td>Sayı</td>
<td>Mahal tüm tavan alanlarının toplamı. Mahaliçindeki elemanların (kolonlar, iç duvarlar vb.) kapladığı alanı hariç tutar. Tavan alanı gerçek alandır (6izdüşüm alanı değil; örneğin eğimli tavanlarda).</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>GrossVolume</td>
<td>OtoSpaceBaseÇuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoSpaceBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özellikleri (kesit boşlukları vb.) veya açıklıklar ve girinitler dikkate alınarak hesaplanır. Mahal tarafından çevrelenen net hacmi ifade eder; mahal içindeki yapı elemanlarının hacmi hariç tutulur.</td>
</tr>
<tr>
<td>Park Birimi Sayısı</td>
<td>ParkingUnits</td>
<td>PsetSpaceParking</td>
<td>Sayı</td>
<td>Parkingüse özelliğinde belirtilen türdeki ulaşım araçlarının mekânda barındırılabilecek sayısını belirtir. Genellikle bu değer varsayılan olarak | birimdir. Ancak park alanı motosiklet veya bisiklet içinse, aynı mahalde birden fazla araç için düzenleme yapılabilir.</td>
</tr>
<tr>
<td rowspan="2"></td>
<td colspan="4">** Kaplamalarla ilgili bu özellikler: (1) IfcSpace içindeki tanımlardan faydalanılarak yada (2) IfcCovering&#x27;de belirtilen ilişkiler kurularak doğrudan modelleme ile tanımlanacak. Bu nedenle belirtilen bu iki yöntemden biri zorunludur.</td>
</tr>
<tr>
<td colspan="4">*Attribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik $355 Beton C25)</td>
</tr>
</tbody>
</table>

| |

| |

|

## Tablo 6.126 IfcSpaceHeater Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Mekan Istıcısı AfcSpaceHeater)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Mekân ısıtıcıları, sınırlı bir mekânı veya alanı ısıtmak için elektrik, buhar veya sıcak su gibi bir ısıtma kaynağı kullanarak ışınım (radyasyon) ve/veya doğal konveksiyon kombinasyonundan yararlanır. Mekân ısıtıcılarına örnek olarak radyatörler, konvektörler, süpürgelik tipi ısıtıcılar ve kanatlı borulu ısıtıcılar verilebilir.</td>
<td>CONVECTOR, RADIATOR, USERDEFINED, NOTDEFINED</td>
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
<td>Atiribute: ObjeciT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: . 1) OÖn Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve |(IfcBuilhElementll&#x27;i doğrudan örmeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>.CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Lengih</td>
<td>OtoSpaceHeaterBaseÇua ntities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoSpaceHeaterBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkae alınmadan hesaplanır.</td>
</tr>
<tr>
<td>,Net Ağırlık i</td>
<td>Net Weight</td>
<td>Oto,SpaceHeaterBaseOua ntities</td>
<td>Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır. Tasarlandığı şekilde içerdiği sıvı dahil olmak üzere yapı elemanın ağırlığı.</td>
</tr>
<tr>
<td>Mekan Isıtıcısı Konumu</td>
<td>SpaceHeaterPlacement</td>
<td>PsetSpaceHeaterT&#x27;ypeCo mmon</td>
<td>Metin</td>
<td>Mekan ısıtıcısının nasıl tasarıma göre nasıl konumlandırılacağını belirtir.</td>
</tr>
<tr>
<td>Sıcaklık Sınıflandırması</td>
<td>TemperatureClassification</td>
<td>PsetSpaceHeaterlypeCo mmon</td>
<td>Metin</td>
<td>Mekân iısıtıcısının yüzey sıcaklığına göre sıcaklık sınıflandırmasını tanımlayan listeden aldığı değer. Düşük sıcaklık: Yüzey sıcaklığı nispeten düşüktür; genellikle sıcak su</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>veya elektrikle ısıtılır. Yüksek sıcaklık: Yüzey sıcaklığı nispeten yüksektir; genellikle gaz veya buharla ısıtılır.</td>
</tr>
<tr>
<td>Isı Transferi Boyutu</td>
<td>HeatTransferDimension</td>
<td>PsetSpaceHeaterTypeCo mmon</td>
<td>Metin</td>
<td>Mekân ısıtıcısının şekline bağlı olarak ısının nasıl iletildiğini gösterir.</td>
</tr>
<tr>
<td>Isı Transfer Ortamı</td>
<td>HeatTransferMedium</td>
<td>Pset SpaceHeaterTypeCo mmon</td>
<td>Metin</td>
<td>Varsa, ısı transfer tanımlayan liste değeri.</td>
</tr>
<tr>
<td>Enerji Kaynağı</td>
<td>EncrgySource</td>
<td>PsetSpaceHeaterTypeCo mmön</td>
<td>Metin</td>
<td>Yakıt Okaynağını veya yakılan enerjiyi tanmlayan liste. Not: Hidronik ısıtıcılar için “Tanımsız”, hem hidronik hem elekirikli çalışan ısıtıcılar için “Elektrik” değeri kullanılmalıdır.</td>
</tr>
<tr>
<td>Gövde Kütlesi</td>
<td>BodyMass</td>
<td>PsetSpaceHeaterTypeCo mmon</td>
<td>Sayı</td>
<td>Isıtıcının toplam gövde kütlesi.</td>
</tr>
<tr>
<td>Termal Kütle Isı Kapasitesi</td>
<td>ThermalMassHeatCapacit y</td>
<td>PsetSpaceHeaterTypeCo mmon</td>
<td>Sayı</td>
<td>Bileşen kütlesi ile özgül ısısınm çarpımıdır.</td>
</tr>
<tr>
<td>Termal Verimlilik</td>
<td>ThermalEfficiency</td>
<td>PsetSpaceHeaterTypeCo mmon</td>
<td>Sayı</td>
<td>Genel Isıl Verimi (Overall Thermal Efficiency), bir ısı transfer cihazının brüt enerji çıktısının, enerji girdisine oranı olarak tanımlanır.</td>
</tr>
<tr>
<td>Panel Sayısı</td>
<td>NumberOfPanels</td>
<td>PsetSpaceHeaterIypeCo mmon</td>
<td>Sayı |</td>
<td>Panel sayısı.</td>
</tr>
<tr>
<td>Bölüm Sayısı</td>
<td>NumberOfSections</td>
<td>PsetSpaceHeaterTypeCo mmon</td>
<td>Sayı</td>
<td>Bölüm sayısı. Akış yönünde ölçülen dikey bölüm sayısı.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.127 IfcSpatialZone Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Mekansal Zon (IfcSpatialZone)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Mekansal zon, belirli bir işlevsel amaca göre projenin hiyerarşik olmayan ve potansiyel olarak örtüşebilen bir alt bölümlenmedir. Mekânsal zonlar örneğin bir ısı bölgesi, inşaat bölgesi, aydınlatma bölgesi veya kullanılabilir alanı temsil etmek için kullanılabilir. Bir mekansal zon, kendi konumlandırmasına ve biçim (geometri) temsiline sahip olabilir.</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir o 1) Ön Tanımlı Tip özniteliğinin değeri listeden (MÜSERDEFINEDİ! olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa . İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElementj|)&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Brüt Planlanan Alan</td>
<td>GrossPlannedAreâ</td>
<td>PsetZoneCommon</td>
<td>Sayı</td>
<td>Mekânsal yapı elemanına âit toplam planlanan brüt alandır. Mekânsal yapı elemanının programlanması amacıyla kullanılır.</td>
</tr>
<tr>
<td>Net Planlanan Alan</td>
<td>NetPlannedArea</td>
<td>PsetZoneCommon</td>
<td>Sayı</td>
<td>Nesneye ait toplam planlanan net alandır. Nesnenin programlanması amacıyla kullanılır.</td>
</tr>
<tr>
<td>Toplam Hava Akışı</td>
<td>TotalAirFlow</td>
<td>PsetAirSideSysteminfor mation</td>
<td>Sayı</td>
<td>Açıklama verilmemiştir.</td>
</tr>
<tr>
<td>Toplam Enerji Kazancı</td>
<td>EnergyGainTotal</td>
<td>PsetAirSideSysteminfor mation</td>
<td>Sayı</td>
<td>Sistem tarafından hizmet verilen mahallerin maksimum soğutma koşullarındaki toplam*enerji kazançları ile sistem düzeyindeki tüm enerji kazançlarının toplamıdır.</td>
</tr>
<tr>
<td>Enerji Kaybı</td>
<td>EnergyLoss</td>
<td>PsetAirSideSysteminfor mation</td>
<td>Sayı</td>
<td>Sistem tarafından hizmet verilen mahallerin maksimum ısıtma koşullarındaki toplam enerji kayıplarının toplamıdır.</td>
</tr>
<tr>
<td>Isıtma Sıcaklık i Farkı</td>
<td>HeatingTemperatureDelta</td>
<td>PsetAirSideSysteminfor mation</td>
<td>Sayı</td>
<td>Mekan hava debilerini hesaplamak için kullanılan ısıtma sıcaklık farkıdır.</td>
</tr>
<tr>
<td>Soğutma Sıcaklık Farkı</td>
<td>CoolingTemperatureDelta</td>
<td>PsetAirSideSysteminfor mation</td>
<td>Sayı</td>
<td>Mekan hava debilerini hesaplamak için kullanılan soğutma sıcaklık farkıdır.</td>
</tr>
<tr>
<td>Sıcaklık Ayar Noktası</td>
<td>TemperatureSetPoint</td>
<td>PsetSpaceHVACDesign</td>
<td>Sayı</td>
<td>Sıcaklık ayar noktası aralığı ve varsayılan ayar noktasıdır.</td>
</tr>
<tr>
<td>Nem Ayar Noktası</td>
<td>HumiditySetPoint</td>
<td>PsetSpaceHVACDesign</td>
<td>Sayı</td>
<td>Kullanıcı veya tasarımcı bakış açısından. mekan veya zon için gerekli olan nem oranıdır. Eğer yaz veya kış dönemi için özel bir nem gereksinimi belirtilmemişse, tüm yıl için geçerlidir; aksi halde geçiş dönemine uygulanır. Nem aralığı (Min-Maks) mevcut değilse bu özellik belirtilmelidir.</td>
</tr>
<tr>
<td>Hava İşleme Adı</td>
<td>AirHandlingName</td>
<td>PsetSpaceHVACDesign</td>
<td>Metin</td>
<td>Hava tarafı sisteminin adıdır. Doğru AirHandlingSystem (I1fcSystem)&#x27;e referans vermek için IfcRelServicesBuildings kullanılmalıdır.</td>
</tr>
<tr>
<td>Acil Çıkış</td>
<td>FireExit</td>
<td>Pset SpaceFireSafeiyRegu irements</td>
<td>Mantıksal</td>
<td>Bu nesnenin yangın durumunda çıkış olarak kullanılmak üzere tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir. .Burada, bir mekanın (örneğin bir koridor gibi) yangın kaçışı için hizmet iverecek bir çıkış alanı olarak tasarlanıp tasarlanmadığını ifade eder</td>
</tr>
</tbody>
</table>

| | ' |

|

## Tablo 6.128 IfcStair Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="3">Merdiven (IfcStair)</td>
<td colspan="2">Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="3">Tanım: Merdiven, kullanıcıların bir döşeme seviyesinden diğerine yürüyerek (adım atarak) çıkmasına/ inmesine imkân tanıyan düşey bir geçiş yoludur. Ara kat döşemesi gibi bir sahanlık içerebilir.</td>
<td colspan="2">STRAIGHT RUN STAIR, TWO STRAIGHT RUN STAIR, OUARTER WINDING STATR, OUARTER TURN STAIR, HALF WINDING STAITR, HALF TURN STAIR, TWO ÇUARTER WINDING STAIR, TWO OUARTER TURN STAIR, THREE | ÇOUARTER WINDING STAIR, THREE OUARTER TURN STAIR, SPIRAL STAIR, DOUBLE RETURN STAJR, CURVED RUN STAIR, TWO CURVED RUN STAR, USERDEFINED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özmiteliğe girilir: 1) OÖn Tanımlı Tip özniteliğinin değeri listeden ((CSERDEFINEDJ) olarak seçilmişse veya 2) somut örmeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltElement|)&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Dışarıda</td>
<td>IsExternal</td>
<td>PsetStairCommon</td>
<td>Mantıksal</td>
<td>Yapı elemanının dışarıda kullanıma yönelik tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) gösterir. Eğer (DOĞRU) ise, bu bir dış eleman olup binanın dışına bakmaktadır.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteElementGe neral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıktır)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengthClas s</td>
<td>PsetConcreteElementGe neral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
<tr>
<td>Rıht Sayısı</td>
<td>NumberOfRiser</td>
<td>PsetStairCommon</td>
<td>Number</td>
<td>Merdiven veya merdiven kolunda bulunan toplam rıht sayısı.</td>
</tr>
<tr>
<td>Basamak Sayısı</td>
<td>NumberOfTreads</td>
<td>PsetStairCommon</td>
<td>Number</td>
<td>Merdiven veya merdiven kolunda bulunan toplam basamak sayısı.</td>
</tr>
</tbody>
</table>

, \ ! |

## Tablo 6.129 IfcTank Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Tank (IfcTank)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Tank, sıvı veya gazın daha sonra kullanılmak üzere depolandığı bir kap ya da haznedir.</td>
<td>BASIN, BREAK PRESSURE, EXPANSION, FEED AND EXPANSION, OILRETENTION TRAY, PRESSURE VESSEL, STORAGE, VESSEL, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örmeklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: o 1) OÖn Tanımlı Tip özniteliğinin değeri listeden I((USERDEFINEDİİ olarak seçilmişse veya 2) somut ömeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuikElement|l&#x27;i doğrudan örmeklerdirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th colspan="2">ALAM Ga il Veri Tipi Özellik Seti / İlişki (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozÖzellikSeti</td>
<td>i Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Depo Türü</td>
<td>StorageT&#x27;ype</td>
<td>PsetTankTypeCommon</td>
<td>Metin</td>
<td>Depolanması amaçlanan genel malzeme kategorisini tanımlar.</td>
</tr>
<tr>
<td>Etkin Kapasite</td>
<td>EffectiveCapacity</td>
<td>PsetTankTypeCommon</td>
<td>Sayı</td>
<td>Tankın toplam efektif veya gerçek hacim kapasitesini belirtir.</td>
</tr>
</tbody>
</table>

| ,

## Tablo 6.130 IfcTransformer Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Transformatör (IfcTransformer)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Transformatör, elektrik enerjisini bir devreden başka bir devreye aktaran, endüktif ve sabit bir cihazdır.</td>
<td>CURRENT, FREÇUENCY, INVERTER, RECTİFIER, VOLTAGE, USERDEFINED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir... 1) Ön Tanımlı Tip özniteliğinin değeri listeden İLUSERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve ((IfcBuihtElementll&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Primer Görünen Güç</td>
<td>PrimaryAppareniPower</td>
<td>PsetTransformerTypeCo mmoön</td>
<td>Sayı</td>
<td>Primer tarafta transformatöre giren ve dönüştürülmüş olan VA (volt- amper) cinsinden güç.</td>
</tr>
<tr>
<td>Primer Akım</td>
<td>PrimaryCurrent</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Dönüştürülmek üzere transformatörün primer tarafına giren akım.</td>
</tr>
<tr>
<td>Primer Frekans</td>
<td>PrimaryFreguency</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Dönüştürülmek üzere transformatörün primer tarafına giren frekans.</td>
</tr>
<tr>
<td>Primer Gerilim</td>
<td>PrimaryVoltage</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Dönüştürülmek üzere transformatörün primer tarafına uygulanan gerilim.</td>
</tr>
<tr>
<td>Sekonder Görünen Güç</td>
<td>SecondaryApparentPower</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Transformatörün sekonder tarafında dönüştürülmüş ve çıkışta verilen VA (volt-amper) cinsinden güç.</td>
</tr>
<tr>
<td>Sekonder Akım</td>
<td>SecondaryCurrent</td>
<td>Pset TransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Dönüştürülmüş ve transformatörün sekonder tarafından çıkan akım.</td>
</tr>
<tr>
<td>Sekonder Akım Türü</td>
<td>SecondaryCurrentType</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Metin</td>
<td>Transformatör çıkışından elde edilebilecek sekonder akım tiplerinin listesi.</td>
</tr>
<tr>
<td>Sekonder Frekans</td>
<td>SecondaryFreguency</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Dönüştürülmüş ve transformatörün sekonder tarafından çıkan frekans.</td>
</tr>
<tr>
<td>Sekonder Gerilim</td>
<td>Secondary Voltage</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Dönüştürülmüş ve transformatörün sekonder tarafından çıkan gerilim.</td>
</tr>
<tr>
<td>Transformatör Vektör Grubu</td>
<td>Transformer VectorGroup</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Metin</td>
<td>Transformatör için gerekli olanın ayarlanabileceği olası vektör gruplarının listesi. Bu enum listesindeki değerler uluslararası standart bir koda göre belirlenmiştir: İlk harf birincil sargıların nasıl bağlandığını. ikinci harf ikincil sargıların nasıl bağlandığını ve rakamlar birincil taraftan ikincil tarafa voltaj ve akımların dönüş açısını (30 derece Katlarıyla) o tanımlar. D: sargıların üçgen (delta) bağlı olduğunu belirtir. Y: sargıların yıldız (star) bağlı olduğunu belirtir. Z: sargıların zikzak (2ig-zag) bağlı olduğunu belirtir (düşük reaktans sağlayan özel bir yıldız bağlantı biçimi). Bağlantı tipi yalnızca üç fazlı transformatörler için geçerlidir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoTransformerBaseÇua ntities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Koruyucu Topraklama Bağlantısı Mevcut</td>
<td>HasProtectiveE£arth</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Mantıksal</td>
<td>Nesnenin koruyucu topraklama bağlantısına sahip olduğunu (DOĞRU) veya olmadığını (YANLIŞ) gösterir.</td>
</tr>
<tr>
<td>Yalıtım Standardı Sınıfı</td>
<td>InsulationStandardClass</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Metin</td>
<td>PYalıtım standart sınıfları, elektrik çarpmasına karşı temel koruma bilgileri sağlar. Yalıtım seviyelerini, yapısal gereksinimler (yüzeysel mesafe ve boşluk mesafeleri) ve elektriksel gereksinimler (elektrik dayanıklılık testlerine uygunluk) açısından tanımlar. Temel yalıtım, tek arıza koşulları altında kısa devre yapmış olarak kabul edilir. Gereken gerçek değerler, yalıtımın maruz kaldığı çalışma voltajına ve diğer faktörlere bağlıdır. Ayrıca, elektrikli cihazın koruyucu toprak bağlantısına sahip olup olmadığını da belirtir.</td>
</tr>
<tr>
<td>Hat Sayısı</td>
<td>NumberOfPoles</td>
<td>PsetElectricalDeviceCom mon</td>
<td>Sayı</td>
<td>Nesnenin etkileyeceği kutup sayısı. Cihazın işlemeye/iletmeye yönelik tasarlandığı enerjili hat (faz) sayısı.</td>
</tr>
<tr>
<td>Sanal Empedans Oranı</td>
<td>ImaginarylmpedanceRatio</td>
<td>PsetTransformerlypeCo mmoön</td>
<td>Sayı</td>
<td>Sıfır dizisi empedansının sanal (imajiner) kısm: ile pozitif empedansın sanal kısmı (yani kısa devre geriliminin sanal kısmı) arasındaki orandır. N iletkenini (nötr iletken) içeren üç fazlı ıransformatörlerde kullanılır.</td>
</tr>
<tr>
<td>Birincil Nötr Terminal Mevcut</td>
<td>IsNeutralPrimaryTerminal Available</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Mantıksal</td>
<td>Birincil sargının nötr noktasının terminal olarak mevcut olduğunu (DOĞRU) veya olmadığını (YANLIŞ) gösterir.</td>
</tr>
<tr>
<td>&quot;İkincil Nötr | Terminal Mevcut</td>
<td>IsNeutralSecondaryTermin alAvailable</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Mantıksal</td>
<td>İkincil sargının nötr noktasının terminal olarak mevcut olduğunu (DOĞRU) veya olmadığını (YANLIŞ) gösterir.</td>
</tr>
<tr>
<td>Gerçek Empedans Oranı</td>
<td>ReallmpedanceRatio</td>
<td>PsetTransformerTypeCo ramon</td>
<td>Sayı</td>
<td>Sıfır dizi empedansının gerçek kısmı ile transformatörün pozitif empedansının gerçek kısmı (yani kısa devre geriliminin gerçek kısmı) arasındaki oran. N iletkeni içeren üç fazlı transformatörler için kullanılır.</td>
</tr>
<tr>
<td>Kısa Devre Gerilimi</td>
<td>ShortCircuitVoltage</td>
<td>PsetTransformerTypeCo mmon</td>
<td>Sayı</td>
<td>Transformatörün nominal akımında kısa devre geriliminin gerçek ve sanal bileşenlerini yüzde (©4) cinsinden belirten karmaşık sayı.</td>
</tr>
</tbody>
</table>

| | |

## Tablo 6.131 IfcTransportElement Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Taşıma Elemanı (IfcTransportElement)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Taşıma elemanı, bir bina veya bina kompleksi içinde insanları, hayvanları veya eşyaları taşıyan tüm ulaşım ile ilgili nesnelerin genelleştirilmiş halidir. Taşıma elemanı, (varsa) IfcTransportElementType tarafından tanımlanan bir taşıma elemanının yerleştirilmiş örneğini ifade eder.</td>
<td>ELEVATOR, ESCALATOR, MOVING WALKWAY, CRANEWAY, LİFTİNG GEAR, USERDEFİNED, NOTDEFİNED</td>
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
<td>Attribute: ObjectT&#x27;ype</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım. örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFİNEDİ) olarak seçilmişse veya 2) somut ömeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((IfcBuiltglement|l&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Acil Çıkış</td>
<td>FireExit</td>
<td>PsetTransportElementCo mmon</td>
<td>Mantıksal</td>
<td>Bu nesnenin yangın durumunda çıkış olarak kullanılmak üzere tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir. Örneğin bir asansör gibi taşıma elemanının, yangın tahiiyesi amacıyla kullanılacak bir yangın çıkışı olarak tasarlanıp tasarlanmadığını gösterir.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.132 IfcValve Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Vana (IfcYalve)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Vana, bina teşisatı boru dağıtım sisteminde akışkanın akışını kontrol etmek veya düzenlemek için kullanılır.</td>
<td>AIR RELEASE, ANTI VACUUM, CHANGE OVER, CHECK, COMMISSTONING, DIVERTİNG, DRAW OFF COCK, DOUBLE CHECK, DOUBLE REGULATING, FAUCET, FLUSHING, GAS COCK, GAS TAP, ISOLATING, MIXING, PRESSURE REDUCING, PRESSURE RELİEF, REGULATING, SAFETY CUT OFF, STEAM TRAP, STOP COCK, USERDEFİNED, NOTDEFINED</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Öznitelik</th>
<th>İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>,Nesne Tipi</td>
<td>Attribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; oO1) Ön Tanımlı Tip özniteliğinin değeri listeden (İUSERDEFİNEDJ) olarak seçilmişse veya 2) somut ömeklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum. bazı istisnai yaprak sınıflarında ve ((1fcBuiltElement)|&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>«CSBPozNo</td>
<td>&#x27;TREpys, PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Çalışma Basıncı</td>
<td>WorkingPressure</td>
<td>PsetValveTypeCommon</td>
<td>Sayı</td>
<td>Çalışma basıncı. Vananın normalde beklenen maksimum çalışma basıncı.</td>
</tr>
<tr>
<td>Kapatma Sınıfı</td>
<td>CloseOffRating</td>
<td>PsetValveTypeCommon</td>
<td>Sayı</td>
<td>Kapatma sınıfı.</td>
</tr>
<tr>
<td>Akış Katsayısı</td>
<td>FlowCoefficient</td>
<td>PsetValveTypeCommon</td>
<td>Sayı</td>
<td>Debi katsayısı (tamamen açık bir vanadan, birim basınç düşümünde geçen akışkan miktarı), genellikle vananın Kv veya Cv değeri olarak ifade edilir.</td>
</tr>
<tr>
<td>Test Basıncı</td>
<td>TestPressure</td>
<td>PsetValveTypeCommon</td>
<td>Sayı</td>
<td>Test sırasında vananın maruz kaldığı maksimum basınç.</td>
</tr>
<tr>
<td>Vana Mekanizması</td>
<td>ValveMechanism</td>
<td>PsetValveTypeCommon</td>
<td>Metin</td>
<td>Vana fonksiyonunun gerçekleştirildiği mekanizma türü: Küre: Gövde oturma portlarına göre döndürülebilen delikli bir küreye sahip vana. Kelebek: Akış ekseni boyunca dönebilen aerodinamik diske sahip vana.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Biçimlendirilmiş Kapak: Kapatma kapısı özel biçimlendirilmiş olan ve basınç ile akış değişimini daha hassas kontrol eden vida kontrollü vana. Salmastra: Konik oturma yüzeyine sahip. döner tapası salmastra ve salmastra keçesiyle tutulan vana. Küresel: Küresel gövdeye sahip vida kontrollü vana. Yağlanmış Tapa: Tapası ile gövde arasına basınç altında yağlayıcı enjekte edilen tapa tipi vana. İğne: Akış yönü boyunca hareket eden ince koni biçimli bir elemanın sabit konik oturma yüzeyine kapanarak akışı düzenlediği vana. Paralel Kayar: İşlenmiş bir plakanın şekillendirilmiş oluklar içinde kayarak sızdırmazlık sağladığı vida kontrollü vana. Tapa: Gövde oturma portlarına göre döndürülebilen delikli tapaya sahip vana. Kamalı Kapak: Kamalı biçimdeki plakanın konik kılavuzlara oturarak sızdırmazlık sağladığı vida kontrollü vana.</td>
</tr>
<tr>
<td>Vana İşletim Yöntemi</td>
<td>ValveOperation</td>
<td>PsetValveTypeCommon</td>
<td>Metin</td>
<td>Vana işletim yöntemini tanımlar: Ağırlık Düşürmeli: Ağırlıklı bir kolun serbest bırakılmasıyla kapanan vana; ağırlık genellikle bir tel ile tutulur, tel üzerindeki eriyebilir bağlantının ısıyla etkilenmesi sonucu kapanma gerçekleşir. Şamandıralı: Su seviyesiyle birlikte yükselip alçalan bir şamandıra tarafından açılıp kapanan vana. Şamandıra bir kola veya başka bir mekanizmaya bağlı bir küre olabilir. Hidrolik: Hidrolik tahrikle açılıp kapanan vana. Kollu: Vana içindeki kapıyı döndüren bir kolun hareketiyle açılıp kapanan vana. Kilit Korumalı: Açma ve kapama işlemi için özel bir kilit anahtarı gerektiren ve normal çalışmada mekanizması bir koruyucu kapakla örtülü olan vana. Motorlu: Elektrik motoru tarafından bir aktüatör aracılığıyla açılıp kapanan vana. Pnömatik: Pnömatik tahrikle açılıp kapanan vana. Manyetik Bobinli: Manyetik alan oluşturan bir bobin akımıyla açık tutulan, ancak akım kesildiğinde hemen kapanan vana. Yaylı: Bir yay basıncıyla konumda tutulan, ancak akışkan basıncı yay kuvvetini yendiğinde açılan vana. Termostatik: Portları, istenen önceden belirlenmiş sıcaklığı korumak için açılıp kapanan vana. Tekerlekli: Vana içindeki kapıyı bir tekerlek aracılığıyla hareket ettirerek açıp kapatan vana.</td>
</tr>
<tr>
<td>“Vana Düzeni</td>
<td>ValvePattem</td>
<td>PsetValveTypeCommon</td>
<td>Metin</td>
<td>Vana portlarının, akışkanın vana içindeki doğrusal akış yönüne veya port sayısına göre düzeni: i Tek Portlu: Hizmet ettiği sistemden tek giriş portuna sahip, çıkış portu çevre ortamına olan vana. Açılı İki Portlu: Akış yönünün 90 derece değiştiği vana. Doğrusal İki Portlu: Akışın doğrusal olarak geçtiği vana. Doğrusal Üç Portlu: Üç ayrı porta sahip vana. Çapraz Dört Portlu: Dört ayrı porta sahip vana.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoValveBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
</tbody>
</table>

i |

'

## Tablo 6.133 Ifc Wall Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Duvar (fc Wall)</td>
<td>Ör Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Duvar, mekanları sınırlayabilen veya bölebilen düşey bir yapısal bileşendir. Duvarlar genellikle düşey veya düşeye yakın düzlemsel elemanlardır ve yapısal yükleri taşımak üzere tasarlanabilir. Ancak, taşıyıcı olmak zorunda değildir.</td>
<td>ELEMENTED WALL, MOVABLE, PARAPET, PARTITIONING, PLUMBING WALL, POLYGONAL, RETAINING WALL, SHEAR, SOLIDWALL, STANDARD, WAVEWALL, USERDEFİNED, NOTDEFINED</td>
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
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut ali tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir: 1) Ön Tanımlı Tip özniteliğinin değeri listeden ((USERDEFINEDİ) olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı istisnai yaprak sınıflarında ve ((1fcBuiltElementi)&#x27;i doğrudan örmeklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti/İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Isıl İletkenlik Katsayısı</td>
<td>ThermalTransmittance</td>
<td>PsetWallCommon</td>
<td>Sayı</td>
<td>Bir bileşenin, ısı akışı yönünde (tüm malzemeleri içeren) ısı iletkenlik katsayısı (U-Value).</td>
</tr>
<tr>
<td>Taşıyıcı</td>
<td>LoadBearing</td>
<td>PsetWallCommon</td>
<td>Mantıksal</td>
<td>Nesnenin yük taşıma amacıyla tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir .</td>
</tr>
<tr>
<td>Uzunluk</td>
<td>Length</td>
<td>OtoWallBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin uzunluğu. Orta hat boyunca (duvar yolundan farklı otsa bile).</td>
</tr>
<tr>
<td>Genişlik</td>
<td>Width</td>
<td>OtoWallBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin genişliği. Sadece, nesne sabit kalınlığa (prizmatik) sahipse verilir. Duvar hattına dik olarak ölçülür. Yalnızca duvar hattı boyunca sabit olduğu durumda verilmelidir.</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>OtoWallBaseÇuantities</td>
<td>Sayı</td>
<td>Karakteristik yükseklik. Duvarın toplam nominal yüksekliği. Yalnızca duvar boyunca sabitse verilmelidir.</td>
</tr>
<tr>
<td>Brüt Ağırlık</td>
<td>Gross Weight</td>
<td>OtoWallBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınınadan hesaplanır.</td>
</tr>
<tr>
<td>Net Ağırlık</td>
<td>Net Weight</td>
<td>Oto, WallBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net ağırlığı, ek parçalar olmaksızın ve olası imalat detayları (kesit boşluğu vb.) veya açıklıklar ve girintiler dikkate alınmadan hesaplanır.</td>
</tr>
<tr>
<td>Beton Örtüsü</td>
<td>ConcreteCover</td>
<td>PsetConcreteslementGen eral</td>
<td>Sayı</td>
<td>Yerel inşaat yönetmeliklerine göre donatı çubukları üzerindeki beton örtüsü (Türkiye Bina Deprem Yönetmeliğine göre beton örtüsü, boyuna donatı ağırlık merkezi ile en dış beton lifi arasında kalan uzaklıkur)</td>
</tr>
<tr>
<td>Donatı Dayanım Sınıfı</td>
<td>ReinforcementStrengthCla ss</td>
<td>PsetConcreteElementGen eral</td>
<td>Metin</td>
<td>Projenin uygulanmakta olduğu beton tasarım standardına göre donatı dayanımının sınıflandırılması. Donatı dayanım sınıfı genellikle dayanım ve deformasyon özelliklerini birleştirir.</td>
</tr>
<tr>
<td>Akustik Performans Sınıfı</td>
<td>AcousticRating</td>
<td>Pset WallCommon</td>
<td>Metin</td>
<td>Bu nesne için akustik performans sınıfı.; Ulusal yapı yönetmeliğine göre sağlanmıştır. Bu nesnenin ses iletim direncini, tam ses yutum değerleri vermek yerine bir indeks oranıyla gösterir.</td>
</tr>
<tr>
<td>Net Cephe Alanı</td>
<td>NetSideArea</td>
<td>OtoWallBaseÇOuantities</td>
<td>Sayı</td>
<td>Nesnenin, orta düzleminin cephe görünümünden görülen Alan&#x27;ı. Açıklıklar gibi tüm nesne değişikliklerini hesaba katar.</td>
</tr>
<tr>
<td>Brüt Hacim</td>
<td>GrossVolume</td>
<td>OtoWallBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam brüt hacmi. Açıklıklar, girintiler, kapalı nesneler ve çıkıntılar dikkate alınmaz.</td>
</tr>
<tr>
<td>Net Hacim</td>
<td>NetVolume</td>
<td>OtoWallBaseOuantities</td>
<td>Sayı</td>
<td>Nesnenin toplam net hacmi, olası imalat özellikleri (kesit boşlukları vb.) veya açıklıklar ve girinitler dikkate almarak hesaplanır.</td>
</tr>
</tbody>
</table>

|

## Tablo 6.134 Ife Window Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="3">Pencere (fc Window)</td>
<td colspan="2">Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="3">Tanım: Pencere, esas olarak doğal ışık ve temiz hava sağlamak için kullanılan bir yapı elemanıdır. Düşey açıklıkları içerdiği gibi çatı pencereleri veya ışıklıklar gibi yatay açıklıkları da kapsar. Açılır, döner, kayar, döner kanatlı veya sabit panellerden oluşan yapıları içerebilir. Bir pencere, bir kasadan ve bir veya birkaç panelden oluşur.</td>
<td colspan="2">WINDOW, SKYLIGHT, LIGHTDOME, USERDEFİNED, NOTDEFINED</td>
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
<td>Atiribute: ObjectType</td>
<td>-</td>
<td>Metin</td>
<td>Tip, nesneyi daha ayrıntılı tanımlayan özel bir tipi belirtir. Kullanım, örneklenebilir somut alt tiplerin seviyesinde belirlenmelidir. Şu durumlarda kullanıcı tarafından tanımlanan tip bilgisi bu özniteliğe girilir; . 1) Ön Tanımlı Tip özniteliğinin değeri listeden NUSERDEFINEDİJ olarak seçilmişse veya 2) somut örneklenmiş varlıkta bir Ön Tanımlı Tip özniteliği yoksa. İkinci durum, bazı İstisnai yaprak sınıflarında ve |(IfcBuiltElement)||&#x27;i doğrudan örneklendirirken geçerlidir.</td>
</tr>
<tr>
<td>Açıklama</td>
<td>Attribute: Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<td>Malzeme</td>
<td>Attribute (fcRelAssociatesMaterial &gt;IfcMaterial): Name*</td>
<td>-</td>
<td>Metin</td>
<td>l(ifeMaterial), yapı elemanlarını (fiziksel ürünler veya bileşenleri) oluşturmak için kullanılabilecek homojen veya heterojen maddelerdir.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td></td>
<td>CSBPozNo</td>
<td>TREpys PozOzellikSeti</td>
<td>Metin</td>
<td>Çevre, Şehircilik ve İklim Değişikliği Bakanlığı İnşaat ve Tesisat Birim Fiyat Poz No&#x27;su.</td>
</tr>
<tr>
<td>Isıl İletkenlik Katsayısı</td>
<td>ThermalTransmittance</td>
<td>PsetWindowCommon</td>
<td>Sayı</td>
<td>Bir bileşenin, 1sı akışı yönünde (tüm malzemeleri içeren) ısı iletkenlik katsayısı (U-Value).</td>
</tr>
<tr>
<td>Acil Çıkış</td>
<td>FireExit</td>
<td>Pset WindowCommon</td>
<td>Mantıksal</td>
<td>Bu nesnenin yangın durumunda çıkış olarak kullanılmak üzere tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir. Burada, ulusal bina yönetmeliğine uygun olarak bir çıkış penceresini tanımlanmaktadır.</td>
</tr>
<tr>
<td>Genişlik</td>
<td>Width</td>
<td>OtoWindowBaseOuantiti es</td>
<td>Sayı</td>
<td>Nesnenin genişliği. Sadece, nesne sabit kalınlığa (prizmatik) sahipse verilir.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Pencere kasasının toplam dış genişliği. Yalnızca dikdörtgen pencereler için sağlanmalıdır.</td>
</tr>
<tr>
<td>Yükseklik</td>
<td>Height</td>
<td>OtoWindowBaseOuantiti es</td>
<td>Sayı</td>
<td>Karakteristik yükseklik. Pencere kasasının toplam dış yüksekliği. Yalnızca pencere dikdörtgen biçimindeyse verilmelidir.</td>
</tr>
<tr>
<td>Alan</td>
<td>Arca</td>
<td>OtoWindowBaseÇuantiti es</td>
<td>Sayı</td>
<td>Nesne için hesaplanan alan. Pencerenin dış kasasının toplam alanıdır.</td>
</tr>
<tr>
<td>Yangın Dayanım Sınıfı</td>
<td>FireRating</td>
<td>Pset WindowCommon</td>
<td>Metin</td>
<td>Bu nesnenin yangın dayanım sınıfı. Ulusal yangın güvenliği sınıflandırmasına göre (Türkiye için: Binaların Yangından Korunması Hakkında Yönetmeliğe göre) verilmiştir.</td>
</tr>
<tr>
<td>Akustik Performans Sınıfı</td>
<td>AcousticRating</td>
<td>Pset WindowCommon</td>
<td>Metin</td>
<td>Bu nesne için akustik performans sınıfı.; Ulusal yapı yönetmeliğine göre sağlanmıştır. Bu nesnenin ses iletim direncini, tam ses yutum değerleri vermek yerine bir indeks oranıyla gösterir.</td>
</tr>
<tr>
<td>Cam Panel Alan Oranı</td>
<td>GlazingAreaFraction</td>
<td>Pset WindowCommon</td>
<td>Sayı</td>
<td>Panel toplam alanına göre cam panel alanının oranı.: Eğer cam panel alanı dolgu elemanı içindeki tüm paneller için ayrı ayrı verilmemişse kullanılmalıdır.</td>
</tr>
<tr>
<td>Güneş Geçirgenliği</td>
<td>SolarTransmittance</td>
<td>PsetDoorWindowGlazing Type</td>
<td>Sayı</td>
<td>Gelen güneş radyasyonunun doğrudan bir sistemden geçen oranı (Te olarak da adlandırılır). Aşağıdaki eşitliğe dikkat edilmelidir: Asol * Rsol * Tsol — |</td>
</tr>
<tr>
<td>Görünür Işık Geçirgenliği</td>
<td>VisibleLightTransmittance</td>
<td>PsetDoorWindowGlazing Type</td>
<td>Sayı</td>
<td>Normal geliş açısında nesneden geçen görünür ışığın oranıdır. Bu, birimsiz bir değerdir.</td>
</tr>
<tr>
<td></td>
<td colspan="4">*Aftiribute (IfcRelAssociatesMaterial&gt;IfcMaterial): Name* bilgisi giriliken: &quot;Malzeme İsmi Dayanım&quot; formatı kullanılmalıdır. (Örnek:Çelik S355 Beton C25)</td>
</tr>
</tbody>
</table>

| | ' i |

| ' İ

## Tablo 6.135 IfcZone Sınıfı İsteğe Bağlı Kullanılabilecek Öznitelik ve Özellik Listesi

<table>
<tbody>
<tr>
<td colspan="4">Zon (IfcZone)</td>
<td>Ön Tanımlı Tip Listesi</td>
</tr>
<tr>
<td colspan="4">Tanım: Zon, mekanların, kısmi mekanların veya diğer zonlarıngruplanmış halini ifade eder, Bu mekanlar bitişik veya bitişik olmayabilir. Bir zonun kendi geometrik biçim temsili yoktur. Zon yapıları ohiyerarşik (Oolmayabilir (bir projenin mekânsal yapısının aksine — bkz. ,SpatialSiructureElement). Yani, tek bir mekân (Space), sıfir, bir veya birden fazla IfcZone ile ilişkilendirilebilir. Mekânlar, üst tür olan Group&#x27;ta tanımlanan IfcRelAssignsToGroup ilişkisi kullanılarak bir IfcZone içinde gruplanır. Örneğin, zon bir daireyi temsil mekanları gruplandırarak temsil etmek için kullanılabilir.</td>
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
<td>Attribute:Description</td>
<td>-</td>
<td>Metin</td>
<td>Bilgilendirme amaçlı isteğe bağlı olarak verilen bir tanımdır.</td>
</tr>
<tr>
<th>Türkçe Tanım (Bilgi Amaçlı)</th>
<th>Özellik</th>
<th>Özellik Seti / İlişki</th>
<th>Veri Tipi (Bilgi Amaçlı)</th>
<th>Açıklama</th>
</tr>
<tr>
<td>Brüt Planlanan Alan</td>
<td>GrossPlannedArea</td>
<td>PsetZoneCommon</td>
<td>Sayı</td>
<td>Mekânsal yapı elemanına ait toplam planlanan brüt alandır. Mekânsal yapı elemanının programlanması amacıyla kullanılır.</td>
</tr>
<tr>
<td>Net Planlanan Alan</td>
<td>NetPlannedArea</td>
<td>PsetZoneCommon</td>
<td>Sayı</td>
<td>Nesneye ait toplam planlanan net alandır. Nesnenin programlanması amacıyla kullanılır.</td>
</tr>
<tr>
<td>Toplam Hava Akışı</td>
<td>TotalAirFlow</td>
<td>PsetAirSideSystemInforma tion</td>
<td>Sayı</td>
<td>Açıklama verilmemiştir.</td>
</tr>
<tr>
<td>Toplam Enerji Kazancı</td>
<td>EnergyGainTotal</td>
<td>PsetAirSideSystemInforma tion</td>
<td>Sayı</td>
<td>Sistem tarafından hizmet verilen mahallerin maksimum soğutma koşullarındaki toplam enerji kazançları ile sistem düzeyindeki tüm enerji kazançlarının toplamıdır.</td>
</tr>
<tr>
<td>Enerji Kaybı</td>
<td>EnergyLoss</td>
<td>PsetAirSideSystemInforma tion</td>
<td>Sayı</td>
<td>Sistem tarafından hizmet verilen mahallerin maksimum ısıtma koşullarındaki toplam enerji kayıplarının toplamıdır.</td>
</tr>
<tr>
<td>Isıtma Sıcaklık Farkı</td>
<td>HeatingTemperatureDelta</td>
<td>PsetAirSideSystemInforma tion</td>
<td>Sayı</td>
<td>Mekan hava debilerini hesaplamak için kullanılan ısıtma sıcaklık farkıdır.</td>
</tr>
<tr>
<td>Soğutma Sıcaklık Farkı</td>
<td>CoolingTemperatureDelta</td>
<td>PsetAirSideSysteminforma ion</td>
<td>Sayı</td>
<td>Mekan hava debilerini hesaplamak için kullanılan soğutma sıcaklık farkıdır.</td>
</tr>
<tr>
<td>Sıcaklık Ayar Noktası</td>
<td>TemperatureSetPoint</td>
<td>PsetSpaceHVACDesign</td>
<td>Sayı</td>
<td>Sıcaklık ayar noktası aralığı ve varsayılan ayar noktasıdır.</td>
</tr>
<tr>
<td>Nem Ayar Noktası</td>
<td>HumiditySetPoint</td>
<td>PsetSpaceHVACDesign</td>
<td>Sayı</td>
<td>Kullanıcı veya tasarımcı bakış açısından, mahal veya bölge için gerekli olan nem oranıdır. Eğer yaz veya kış dönemi için özel bir nem</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>gereksinimi belirtilmemişse, tüm yıl için geçerlidir; aksi halde geçiş dönemine uygulanır. Nem aralığı (Min-Maks) mevcut değilse bu özellik belirtilmelidir.</td>
</tr>
<tr>
<td>Hava İşleme Adı</td>
<td>AirHandlingName</td>
<td>PsetSpaceHVACDesign</td>
<td>Metin</td>
<td>Hava tarafi sisteminin adıdır. Doğru AirHandlingSystem (İfcSystem)&#x27;e referans vermek için IfcRelServicesBuildings kullanılmalıdır.</td>
</tr>
<tr>
<td>Acil Çıkış</td>
<td>FireExit</td>
<td>PsetSpaceFireSafetyReguir emenis</td>
<td>Mantıksal</td>
<td>Bu nesnenin yangın durumunda çıkış olarak kullanılmak üzere tasarlandığını (DOĞRU) veya tasarlanmadığını (YANLIŞ) belirtir. Burada, bir mekanın (örneğin bir koridor gibi) yangın kaçışı için hizmet verecek bir çıkış alanı olarak tasarlanıp tasarlanmadığını ifade eder,</td>
</tr>
</tbody>
</table>

|
