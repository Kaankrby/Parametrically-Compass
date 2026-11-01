# EK-5 — BIM modelindeki IFC sınıfları ve varlık isimlendirme esasları

> Düzenlenebilir metin ve HTML tablolar. OCR yazımları ile hücre birleştirmeleri otomatik aktarılmıştır; TEYİT BEKLİYOR. Tablolar resim değildir. Grafikler varsa ayrı düzenlenebilir SVG vektörleridir. Bu aktarım hukuki doğrulama veya uygulama kapsamı onayı değildir.

Kaynak: RG 05.08.2026 / 33331.

EK-5 BIM MODELİNDEKİ IFC SINIFLARI VE VARLIK İSİMLENDİRME ESASLARI

5.1- Tasarımda bulunması durumunda BIM modelinde tanımlanması zorunlu olan varlıklara ait IFC sınıf listesi Tablo 5.1’de verilmiştir.

5.2- BIM modelinde yer alması isteğe bağlı olan varlıklara ait IFC sınıf listesi Tablo 5.2'de verilmiştir.

5.3- Söz konusu varlıklar, IFC formatına dönüştürüldüğünde Tablo 5.1 ve Tablo 5.2'de belirtilen IFC sınıfları kullanılarak temsil edilir.

5.4- Tablo 5.1 ile Tablo 5.2'de yer alan IFC sınıfları, IFC 4.3 versiyonu esas alınarak düzenlenmiştir.

5.5- BIM modelinde yer alan varlıklar Tablo 5.3’de verilen şablona göre isimlendirilir. Şablondaki her bir bilgi alanı orta tire “-” işareti ile ayrılır.

5.5.1- “Disiplin”, varlığın ait olduğu disiplini temsil eder. İki karakterli alfabetik kısaltma ile ifade edilir, Disiplin adları ve kısaltmaları EK-2 Tablo 2.2'de verilmiştir.

5.5.2- “Kategori Kodu” varlığın IFC sınıfının Türkçe karşılığını temsil eder. Tablo 5.1’de ve Tablo 5.2'de verilen üç karakterli alfabetik kısaltma ile ifade edilir.

5.5.3- “Açıklama” yapı elemanına ait tanımlayıcı bilgilerin girildiği alandır. Karakter sınırlaması yoktur. Alfanümerik ifadeler kullanılabilir. Alt kategori, fonksiyon, ölçü, malzeme ve benzeri bilgiler buraya yazılabilir. Her yeni bilgi alanı boşluk bırakmaksızın alt tire “_” işareti ile ayrılır. Bazı IFC sınıflarının “Ön Tanımlı Tipleri” çok sayıda varlık içerdiğinden, bu tiplerin Türkçe karşılıkları verilmez. Gerekli görüldüğü takdirde, bu tip bilgiler “Açıklama” alanında verilebilir. Açıklama kısmında orta tire “-” kullanılmaz.

5.5.4- BIM modelinde mahal isimlendirmesi yapılırken şablondaki açıklama bölümünde, EK-3’te tarif edilen mahal numarası ve mahal ismi ayrı ayrı veya beraber kullanılabilir.

## Tablo 5.1 Zorunlu IFC sınıfları İçin Kategori Kodu Listesi

<table>
<tbody>
<tr>
<td></td>
<td>IFC Sınıfı ((HcClass)</td>
<td>IFC Sınıfının Türkçe Karşılığı (Bilgi için)</td>
<td>Kategori Kodu</td>
</tr>
<tr>
<td>1</td>
<td>IfcAirTerminal</td>
<td>Havalandırma Menfezi</td>
<td>HVM</td>
</tr>
<tr>
<td>2</td>
<td>IfcAudioVisualAppliance</td>
<td>Görsel ve Ses Cihaz</td>
<td>GVS</td>
</tr>
<tr>
<td>3</td>
<td>IfeBeam</td>
<td>Kiriş</td>
<td>KRS</td>
</tr>
<tr>
<td>4</td>
<td>IfeBoiler</td>
<td>Kazan</td>
<td>KZN</td>
</tr>
<tr>
<td>5</td>
<td>IfcBridge</td>
<td>Köprü</td>
<td>KPR</td>
</tr>
<tr>
<td>6</td>
<td>IfcBridgePart</td>
<td>Köprü Parçası</td>
<td>KPP</td>
</tr>
<tr>
<td>7</td>
<td>IfcBuilding</td>
<td>Bina</td>
<td>BNA</td>
</tr>
<tr>
<td>8</td>
<td>IfcBuildingStorey</td>
<td>Bina Katı</td>
<td>BNK</td>
</tr>
<tr>
<td>9</td>
<td>IfeBurner</td>
<td>Brülör</td>
<td>BRL</td>
</tr>
<tr>
<td>10</td>
<td>IfcCableCarrierFitting</td>
<td>Kablo Taşıyıcı Bağlantı Parçası</td>
<td>KTB</td>
</tr>
<tr>
<td>11</td>
<td>IfeCableCarrierSegment</td>
<td>Kablo Taşıyıcı Segment</td>
<td>KTS</td>
</tr>
<tr>
<td>ir</td>
<td>IfcCaissonFoundation</td>
<td>Keson Temeli</td>
<td>KST</td>
</tr>
<tr>
<td>3</td>
<td>IfeChiller</td>
<td>Soğutma Grubu</td>
<td>SGT</td>
</tr>
<tr>
<td>14</td>
<td>IfeChimney</td>
<td>Baca</td>
<td>BAC</td>
</tr>
<tr>
<td>15</td>
<td>IfcCoil</td>
<td>Serpantin</td>
<td>SRP</td>
</tr>
<tr>
<td>16</td>
<td>IfcColumn</td>
<td>Kolon</td>
<td>KLN</td>
</tr>
<tr>
<td>17</td>
<td>IfeCommunicationsA ppliance</td>
<td>İletişim Cihazı</td>
<td>ILT</td>
</tr>
<tr>
<td>18</td>
<td>IfeCondenser</td>
<td>Kondenser</td>
<td>KND</td>
</tr>
<tr>
<td>19</td>
<td>IfcCoolingTower</td>
<td>Soğutma Kulesi</td>
<td>SKL</td>
</tr>
<tr>
<td>20</td>
<td>IfcCovering</td>
<td>Kaplama</td>
<td>KPL</td>
</tr>
<tr>
<td>21</td>
<td>IfcCurtainWall</td>
<td>Giydirme Cephe</td>
<td>GDC</td>
</tr>
<tr>
<td>22</td>
<td>IfeDamper</td>
<td>Damper</td>
<td>DMP</td>
</tr>
<tr>
<td>23</td>
<td>IfeDistributionBoard</td>
<td>Dağıtım Panosu</td>
<td>DPN</td>
</tr>
<tr>
<td>24</td>
<td>IfeDistributionSystem</td>
<td>Dağıtım Sistemi</td>
<td>DGS</td>
</tr>
<tr>
<td>25</td>
<td>IfcDoor</td>
<td>Kapı</td>
<td>KAP</td>
</tr>
<tr>
<td>26</td>
<td>IfeDuctFitting</td>
<td>Kanal Bağlantı Parçası</td>
<td>KBP</td>
</tr>
<tr>
<td>27</td>
<td>IfeDuctSegment</td>
<td>Kanal Segmenti</td>
<td>KNS</td>
</tr>
<tr>
<td>28</td>
<td>IfeDuctSilencer</td>
<td>Kanal Susturucusu</td>
<td>KSS</td>
</tr>
<tr>
<td>29</td>
<td>IfeElectricAppliance</td>
<td>Elektrikli Cihaz</td>
<td>ECZ</td>
</tr>
<tr>
<td>30</td>
<td>IfcElectricGenerator</td>
<td>Elektrik Jeneratörü</td>
<td>EJN</td>
</tr>
<tr>
<td>31</td>
<td>IfcEvaporator</td>
<td>Evaporatör</td>
<td>EVP</td>
</tr>
<tr>
<td>32</td>
<td>IfcFan</td>
<td>Fan</td>
<td>FAN</td>
</tr>
<tr>
<td>33</td>
<td>IfcFireSuppressionTerminal</td>
<td>Yangın Söndürme Terminali</td>
<td>YST</td>
</tr>
<tr>
<td>34</td>
<td>IfeFooting,</td>
<td>Temel</td>
<td>TML</td>
</tr>
<tr>
<td>35</td>
<td>IfcFurniture</td>
<td>Mobilya</td>
<td>MBL</td>
</tr>
<tr>
<td>36</td>
<td>IfcGridAxis</td>
<td>Aks</td>
<td>AKS</td>
</tr>
<tr>
<td>37</td>
<td>IfeGroup</td>
<td>Grup</td>
<td>GRP</td>
</tr>
<tr>
<td>38</td>
<td>IfcHeatExchanger</td>
<td>Isı Eşanjörü</td>
<td>IEJ</td>
</tr>
<tr>
<td>39</td>
<td>feLightFixture</td>
<td>Aydınlatma Armatürü</td>
<td>AYN</td>
</tr>
<tr>
<td>40</td>
<td>IfcMember</td>
<td>Eleman</td>
<td>ELM</td>
</tr>
<tr>
<td>41</td>
<td>IfcOpeningElement</td>
<td>Açıklık Elemani</td>
<td>ACL</td>
</tr>
<tr>
<td>42</td>
<td>TfeOutlet</td>
<td>Priz</td>
<td>PRZ</td>
</tr>
<tr>
<td>43</td>
<td>IfePavement</td>
<td>Asfalt</td>
<td>ASF</td>
</tr>
<tr>
<td>44</td>
<td>IfePile</td>
<td>Kazık</td>
<td>KZK</td>
</tr>
<tr>
<td>45</td>
<td>IfePipeFitting,</td>
<td>Boru Bağlantı Parçası</td>
<td>BBP</td>
</tr>
<tr>
<td>46</td>
<td>IfePipeSegment</td>
<td>Boru Segmenti</td>
<td>BRS</td>
</tr>
<tr>
<td>47</td>
<td>(fePump</td>
<td>Pompa</td>
<td>PMP</td>
</tr>
<tr>
<td>48</td>
<td>IfcRailing</td>
<td>Korkuluk</td>
<td>KRK</td>
</tr>
<tr>
<td>49</td>
<td>IfcRamp</td>
<td>Rampa</td>
<td>RMP</td>
</tr>
<tr>
<td>50</td>
<td>IfeRoad</td>
<td>Yol</td>
<td>YOL</td>
</tr>
<tr>
<td>51</td>
<td>IfeRoadPart</td>
<td>Yol Parçası</td>
<td>YLP</td>
</tr>
<tr>
<td>52</td>
<td>IfcRoof</td>
<td>Çatı</td>
<td>CAT</td>
</tr>
<tr>
<td>33</td>
<td>IfcSanitaryTermninal</td>
<td>Sıhhi Terminal</td>
<td>STT</td>
</tr>
<tr>
<td>4</td>
<td>IfeSign</td>
<td>Tabela</td>
<td>TBL</td>
</tr>
<tr>
<td>55</td>
<td>IfcSite</td>
<td>Saha</td>
<td>SAH</td>
</tr>
<tr>
<td>56</td>
<td>IfcSlab</td>
<td>Döşeme</td>
<td>DSM</td>
</tr>
<tr>
<td>57</td>
<td>IfeSolarDevice</td>
<td>Güneş Enerjisi Cihazı</td>
<td>GEC</td>
</tr>
<tr>
<td>58</td>
<td>IfcSpace</td>
<td>Mahal</td>
<td>MHL</td>
</tr>
<tr>
<td>59</td>
<td>IfeSpaceHeater</td>
<td>Mekan Isıtıcısı</td>
<td>MIS</td>
</tr>
<tr>
<td>60</td>
<td>IfcSpatialZone</td>
<td>Mekansal Zon</td>
<td>MZN</td>
</tr>
<tr>
<td>61</td>
<td>IfcStair</td>
<td>Merdiven</td>
<td>MRD</td>
</tr>
<tr>
<td>62</td>
<td>IfcTank</td>
<td>Tank</td>
<td>TNK</td>
</tr>
<tr>
<td>63</td>
<td>IfcTransformer</td>
<td>Transformatör</td>
<td>TRF</td>
</tr>
<tr>
<td>64</td>
<td>IfeTransportElement</td>
<td>Taşıma Elemanı</td>
<td>TSM</td>
</tr>
<tr>
<td>65</td>
<td>IfeValve</td>
<td>Vana</td>
<td>VNA</td>
</tr>
<tr>
<td>66</td>
<td>IfcWall</td>
<td>Duvar</td>
<td>DVR</td>
</tr>
<tr>
<td>67</td>
<td>IfcWindow</td>
<td>Pencere</td>
<td>PNC</td>
</tr>
<tr>
<td>68</td>
<td>IfeZone</td>
<td>Zon</td>
<td>ZON</td>
</tr>
<tr>
<td>69</td>
<td>IfcProject</td>
<td>Proje</td>
<td>-</td>
</tr>
</tbody>
</table>

| | |

## Tablo 5.2 İsteğe Bağlı IFC Sınıfları İçin Kategori Kodu Listesi

<table>
<tbody>
<tr>
<td></td>
<td>IFC Sınıf İsmi (1feClass)</td>
<td>IFC Sınıfının Türkçe Karşılığını</td>
<td>İsimlendirme (Kategori Kodu)</td>
</tr>
<tr>
<td>l</td>
<td>IfcActuator</td>
<td>Aktüatör</td>
<td>AKT</td>
</tr>
<tr>
<td>2</td>
<td>IfcAirTerminalBox</td>
<td>Hava Terminal Kutusu</td>
<td>HTK</td>
</tr>
<tr>
<td>3</td>
<td>IfeAirToAirHeatRecovery</td>
<td>Hava-Hava Isi Geri Kazanım Cihazı</td>
<td>HIG</td>
</tr>
<tr>
<td>4</td>
<td>IfcAlarm</td>
<td>Alarm</td>
<td>ALR</td>
</tr>
<tr>
<td>5</td>
<td>IfcCableFitting Ni</td>
<td>Kablo Elemanı (Uç)</td>
<td>KLU</td>
</tr>
<tr>
<td>6</td>
<td>IfcCableSegment</td>
<td>Kablo Segmenti</td>
<td>KBS</td>
</tr>
<tr>
<td>7</td>
<td>IfcCompressor</td>
<td>Kompresör</td>
<td>KMP</td>
</tr>
<tr>
<td>; .</td>
<td>IfcController</td>
<td>Kontrol Cihazı</td>
<td>KNT</td>
</tr>
<tr>
<td>9</td>
<td>IfcConveyorSegment</td>
<td>Konveyör Segmenti</td>
<td>KVS</td>
</tr>
<tr>
<td>10</td>
<td>TfeCooledBeam</td>
<td>Soğutmalı Kiriş</td>
<td>SKR</td>
</tr>
<tr>
<td>nu</td>
<td>IfcDiscreteAccessory</td>
<td>Küçük Donatı Elemanı</td>
<td>KDE</td>
</tr>
<tr>
<td>12</td>
<td>IfeDistributionChamberElement</td>
<td>Dağıtım Odası Elemanı</td>
<td>DOE</td>
</tr>
<tr>
<td>13</td>
<td>IfeDistributionCircuit</td>
<td>Dağıtım Devresi</td>
<td>DDV</td>
</tr>
<tr>
<td>l4</td>
<td>IfeDistributionPort</td>
<td>Dağıtım Portu</td>
<td>DPT</td>
</tr>
<tr>
<td>15</td>
<td>IfcEarthworksCut</td>
<td>Kazı İşleri</td>
<td>KZI</td>
</tr>
<tr>
<td>16</td>
<td>IfeEarthworksFill</td>
<td>Dolgu İşleri</td>
<td>DGI</td>
</tr>
<tr>
<td>17</td>
<td>IfeEleetricFlowStorageDevice</td>
<td>Elektrik Akış Depolama Cihazı</td>
<td>EAD</td>
</tr>
<tr>
<td>18</td>
<td>IfcElectricFlowTreatmentDevice</td>
<td>Elektrik Akış İşleme Cihazı</td>
<td>EAI</td>
</tr>
<tr>
<td>19</td>
<td>IfeElectricMotor</td>
<td>Elektrik Motoru</td>
<td>EMO</td>
</tr>
<tr>
<td>20</td>
<td>IfcEleciricTimeControl</td>
<td>Elektrik Zaman Kontrol Cihazı</td>
<td>EZK</td>
</tr>
<tr>
<td>21</td>
<td>IfcElementAssembiy</td>
<td>Eleman Montajı</td>
<td>EMN</td>
</tr>
<tr>
<td>22</td>
<td>IfeEngine</td>
<td>Motor (Engine)</td>
<td>MTR</td>
</tr>
<tr>
<td>23</td>
<td>IfcEvaporativeCooler</td>
<td>Buharlaşmalı Soğutucu</td>
<td>BSC</td>
</tr>
<tr>
<td>24</td>
<td>IfcExternalSpatialElement</td>
<td>Dış Mekan Elemanı</td>
<td>DME</td>
</tr>
<tr>
<td>25</td>
<td>IfcFacilityPartCommon</td>
<td>Tesis Ortak Bölümü</td>
<td>TOB</td>
</tr>
<tr>
<td>26</td>
<td>IfeFilter</td>
<td>Filtre</td>
<td>FLT</td>
</tr>
<tr>
<td>27</td>
<td>HeFlowlnstrument</td>
<td>Akış Ölçer Cihazı</td>
<td>AOC</td>
</tr>
<tr>
<td>28</td>
<td>IfeFlowMeter</td>
<td>Akış Sayacı</td>
<td>ASY</td>
</tr>
<tr>
<td>29</td>
<td>IfeGeographicElement</td>
<td>Coğrafi Eleman</td>
<td>COG</td>
</tr>
<tr>
<td>30</td>
<td>IfeGeomodel</td>
<td>Coğrafi Model</td>
<td>CGM</td>
</tr>
<tr>
<td>31</td>
<td>IfcGeoslice</td>
<td>Coğrafi Dilim</td>
<td>CDL</td>
</tr>
<tr>
<td>32</td>
<td>IfcGeotechnicalStratum</td>
<td>Jeoteknik Katman</td>
<td>JTK</td>
</tr>
<tr>
<td>33</td>
<td>IfeHumidifier</td>
<td>Nemlendirici</td>
<td>NML</td>
</tr>
<tr>
<td>34</td>
<td>IfelmpactProtectionDevice</td>
<td>Darbe Koruma Cihazı</td>
<td>DKC</td>
</tr>
<tr>
<td>35</td>
<td>Ifelnterceptor</td>
<td>Tutucu / Ayırıcı (Interceptor)</td>
<td>TTA</td>
</tr>
<tr>
<td>36</td>
<td>IfeJunctionBox</td>
<td>Bağlantı Kutusu</td>
<td>BKT</td>
</tr>
<tr>
<td>37</td>
<td>IfeKerb</td>
<td>i Bordür</td>
<td>BRD</td>
</tr>
<tr>
<td>38</td>
<td>ifeLamp</td>
<td>Lamba</td>
<td>LMB</td>
</tr>
<tr>
<td>39</td>
<td>IfeLiguidTerminal</td>
<td>Sıvı Terminali</td>
<td>STM</td>
</tr>
<tr>
<td>40</td>
<td>IfeMechanicalFastener</td>
<td>Mekanik Bağlantı Elemanı</td>
<td>MBE</td>
</tr>
<tr>
<td>41</td>
<td>IfeMedicalDevice</td>
<td>Medikal Cihaz.</td>
<td>MDC</td>
</tr>
<tr>
<td>42</td>
<td>IfeMobileTelecommunicationsAp pliance</td>
<td>Mobil Telekomünikasyon Cihazi</td>
<td>MTC</td>
</tr>
<tr>
<td>43</td>
<td>IfeMooringbDevice</td>
<td>Halat/Bağlama Cihazı</td>
<td>HBC</td>
</tr>
<tr>
<td>44</td>
<td>IfeMotorConnection</td>
<td>Motor Bağlantısı</td>
<td>MBA</td>
</tr>
<tr>
<td>45</td>
<td>IfcNavigationElement</td>
<td>Seyir Elemanı</td>
<td>SEY</td>
</tr>
<tr>
<td>46</td>
<td>IfcProjectionElement</td>
<td>Projeksiyon Elemanı</td>
<td>PJE</td>
</tr>
<tr>
<td>47</td>
<td>IfeProtectiveDevice</td>
<td>Koruma Cihazı</td>
<td>KRC</td>
</tr>
<tr>
<td>48</td>
<td>IfcProtectiveDevice TrippingUnit</td>
<td>Koruma Cihazı Açma Ünitesi</td>
<td>KAU</td>
</tr>
<tr>
<td>49</td>
<td>TfcRail</td>
<td>Ray</td>
<td>RAY</td>
</tr>
<tr>
<td>50</td>
<td>IfcRampFlight</td>
<td>Rampa Kolu</td>
<td>RMK</td>
</tr>
<tr>
<td>sı</td>
<td>IfeReinforcedSoil</td>
<td>Donatılı Zemin</td>
<td>DNZ</td>
</tr>
<tr>
<td>52</td>
<td>IfeSensor</td>
<td>Sensör</td>
<td>SNS</td>
</tr>
<tr>
<td>33</td>
<td>IfeShadingDevice</td>
<td>Güneş Kırıcı</td>
<td>GNK</td>
</tr>
<tr>
<td>54</td>
<td>IfcSignal</td>
<td>Sinyal</td>
<td>SNY</td>
</tr>
<tr>
<td>55</td>
<td>IfeStack&#x27;Terminal</td>
<td>Yığın Terminali</td>
<td>YTN</td>
</tr>
<tr>
<td>56</td>
<td>IfeStairFlight</td>
<td>Merdiven Kolu</td>
<td>MRK</td>
</tr>
<tr>
<td>57</td>
<td>IfeSwitehingDevice</td>
<td>Anahtarlama Cihazı</td>
<td>AHC</td>
</tr>
<tr>
<td>58</td>
<td>IfeSystemFumitureElement</td>
<td>Sistem Mobilya Elemanı</td>
<td>SME</td>
</tr>
<tr>
<td>59</td>
<td>IfcTubeBundle</td>
<td>Boru Demeti</td>
<td>BDM</td>
</tr>
<tr>
<td>60</td>
<td>IfcUnitaryControlElement</td>
<td>Üniter Kontrol Elemanı</td>
<td>UKE</td>
</tr>
<tr>
<td>6l</td>
<td>IfeUnitaryEguipment</td>
<td>Üniter Ekipman</td>
<td>UEK</td>
</tr>
<tr>
<td>62</td>
<td>IfeVibrationDamper</td>
<td>Titreşim Sönümleyici</td>
<td>TSD</td>
</tr>
<tr>
<td>63</td>
<td>IfeVibrationlsolator</td>
<td>Titreşim İzolatörü</td>
<td>TIZ</td>
</tr>
<tr>
<td>64</td>
<td>IfeVirtualElement</td>
<td>Sanal Eleman</td>
<td>SNE</td>
</tr>
<tr>
<td>65</td>
<td>IfeVehicle</td>
<td>Araç</td>
<td>ARC</td>
</tr>
<tr>
<td>66</td>
<td>IfeVoidingFeature</td>
<td>Boşaltma Özelliği</td>
<td>BOS</td>
</tr>
<tr>
<td>67</td>
<td>feWasteTerminal</td>
<td>Atık Terminali</td>
<td>ATK</td>
</tr>
</tbody>
</table>

|

|

## Tablo 5.3 BIM Modelinde Varlık İsimlendirme Şablonu*

<table>
<tbody>
<tr>
<td>Bilgi Alanı</td>
<td>Disiplin</td>
<td>Kategori Kodu</td>
<td>Açıklama</td>
</tr>
<tr>
<td>Karakter Sayısı</td>
<td>2</td>
<td>3</td>
<td>-</td>
</tr>
<tr>
<td>Veri Türü</td>
<td colspan="2">Alfabetik</td>
<td>Alfanümerik</td>
</tr>
</tbody>
</table>

* sadece ilgili varlığın isimlendirmesinde kullanılır
