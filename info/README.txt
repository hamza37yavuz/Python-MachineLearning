						MAKİNE ÖĞRENMESİ (NOTLAR)

NOT:
-Bu notlar MachineLearning klasöründe yer alan konuları başlıklar halinde açıklamak özet geçmek maksadıyla oluşturulmuştur. 

REGRESYON REGRESSION

	*Coklu Dogrusal Regresyon

	-basit dogrusall regresyonda y = a + bx + e seklinde yazilabilir
	-e: hata orani anlamina gelir. Coklu dogrusal regresyonda birden fazla b degeri vardir.
	-b1x1+b2x2+.... şeklinde y yi etkileyen b degerleri yazilabilir bu regresyon modelinde her x degeri icin degisen bir e degeri vardir.
	-Boy = a + b(kilo) + c(ayakkabi no) seklinde yazilabilir.
----------------------------------------------------------------------------
	*Dummy variable
	-Dummy variable daha önce kullanilan ve kategorize edilen bir sutunun birden fazla kere kullanimina verilen isim
	-Bu kullanimdan yapay zeka modelleri olumsuz etkilenmektedir.
	-Birden fazla veri varsa kategorize edilmelidir. ornegin bir kisinin nereli olduguyla ilgili olabilir.
	-Bu durumda kategorize edilen tum sutunlar kullanilmalidir
----------------------------------------------------------------------------
	*p-value
	H0 : null hypothesis sıfır hipotezi bos hipotez farksizlik hipotezi
	H1 : Alternatif hipotez
	p degeri : olasilik degeri genelde 0.05
	P degeri kuculdukce H0 hatali olma ihtimali artar
	P degeri buyudukce H1 hatali olma ihtimali artar
	H0 : Ornek : ders calisma saati artarsa basarili olunabilir varsayimi
	H1 : Ornek : ders calisma saati artarsa basarili olunmayabilir varsayimi
	ne kadar H1 olursa H0 curutulebilir onu anlatan deger p degeri olur
 ----------------------------------------------------------------------------
	*Degisken Secimi
	-Cok degiskenli modellerde her degisken ayni oranda mi sonucu etkiliyor?
	-Degisken secimi nasil yapilmali
	
	1* Butun Degiskenleri Dahil Etmek
       		-Butun degiskenler sisteme dahil edilir ve sonuc degerlendirilir.
       		-Bu yontem :
       		  degisken secimi yapildiysa
                  zorunluluk varsa
           	  kesif icin (hangi yontemi kullanmaliyim)
       		kullanilabilir
        
	2* Geriye Dogru Eleme (Backward Elimination) (stepwise yaklaşım)
       		a) Butun degiskenler dahil edilerek  bir model insa edilir Model başarı testi yapılır
       		b) Signifacance Level SL seçilir genelde 0.05
       		c) En yüksek p-value değerine sahip olan değişken ele alınır 
			şayet P>SL ise bir sonraki adıma değilse son adıma gidilir
       		d) Bu aşamada bir önceki adımda seçilen ve en yüksek p değerine sahip değişken sistemden kaldırılır.
       		e) Makine öğrenmesi güncellenir ve c ye geri dönülür.
       		f) Makine öğrenmesi sonlandırılır

	3* Ileri Secim (Forward Selection)
       		a) Butun degiskenler dahil edilerek  bir model insa edilir Model başarı testi yapılır
       		b) Signifacance Level SL seçilir genelde 0.05
       		c) En düşük p-value değerine sahip olan değişken ele alınır 
       		d) Bir önceki adımda seçilen değişken sabit tutularak bir değişken daha seçilir
			ve sisteme eklenir	
       		e) Makine öğrenmesi güncellenir ve c ye geri dönülür. Şayet en düşük p-değere sahip değişken için
			p<SL sağlanıyorsa c ye dönülür sağlamıyorsa diğer adıma geçilir
       		f) Makine öğrenmesi sonlandırılır

	4* Iki Yonlu Secim (Bidirectional Elimination) 	 ileriye ve geriye doğru eleem beraber çalışır 
       		a) Butun degiskenler dahil edilerek  bir model insa edilir Model başarı testi yapılır
       		b) Signifacance Level SL seçilir genelde 0.05
       		c) En düşük p-value değerine sahip olan değişken ele alınır 
       		d) Bir önceki adımda seçilen değişken sabit tutularak bütün değişkenler sisteme dahil edilir
			ve en düşük p değerine sahip olan sistemde kalır.	
       		e) SL değerinin altında olan değişkenler sistemde kalır.
			eski değişkenlerden hiçbirisi sistemden çıkarılmaz
       		f) Makine öğrenmesi sonlandırılır

	5* Skor Karsilastirma (Score Comparison)
		a) Bir başarı kriteri belirleyerek bütün olası modeller inşa edilir.
		b) Başta belirlenen kriteri en iyi sağlayan yöntem seçilir
		c) Makine öğrenmesi sonlandırılır.
----------------------------------------------------------------------------
	*POLİNOMAL REGRESYON
	- Aynı değişkenin farklı katsayılar ve üs değerleri ile parabolik bir eğri oluşturduğunu göserir.
	- Eğrileri tahmin etme sırasında kullanacağımız yöntemi barındırır.
----------------------------------------------------------------------------
	*SUPPORT VECTOR REGRESSION SVM (MACHINE)
	*DESTEK VEKTÖRÜ
	-Normalde iki tane sınıfı ayırmak için kullanılan metot iki kümenin maksimum aralıkla birbirinden ayırma
		ve regresyonda maksimun noktayı içine alacak şekilde bir aralık oluşturmak için de kullanılır.
	-Aralık ne kadar küçükse regression o kadar sağlıklı olur
	-Doğrusal olmayıp bu tahmin metodu kullanılan fonksiyonlar
	
	Doğrusal olan , doğrusal olmayan
	Linear re	exponential
		RBF gaussian 
		polynomial
----------------------------------------------------------------------------
	*Karar Ağacı DECISION TREE
	- 2 Boyutlu uzayda bir karar ağacı oluşturulur.
	- Verilerin dağılımına göre bölmeler oluşturulur.
	- Oluşturulan bölmelerin train kümesinden ortalamalar yardımıyla tahminler yapılır
	- Bu algoritmanın daha hassas olması gerekiyorsa bölüm sayısının artırılması gerekir
----------------------------------------------------------------------------
	*RANDOM FOREST rassal ağaçlar
	- Ensemble Learning kollektif öğrenme birden fazla model kullanma anlamlarına gelir.
	- Veri karar ağacı kullanılarak bölümlere ayrılır ve ayrılan bölümler bir daha parçalara ayrılarak bundan yararlanılır.
	- Bu ayrılan küçük ağaçlar arasında ortalamalardan faydalanılarak tahmin işlemi yapılabilir
	- Nasıl birleştirileceği ile ilgili yeni yöntemler vardır.
	- Karar ağaçlarında tüm değerlerin alınması bazen hataları artırabilir.
	- Bunu sebepleri: - tümünü öğrenirse ezberler overfitting olur
	       		  - çok veri alırsa ağaç çok dallanır bu da işlem hızını düşürür
__________________________________________________________________________________________________________________________

REGRESYON YÖNTEMLERİNİ KARŞILAŞTIRMA (EVALUATİON OF PREDİCTİONS)

	*R Square Metodu   
	
	- hata kareleri toplamı : topla(veri-tahminiveri)^^2
	- ortalama farkların toplamı : topla(veri-veriort)^^2
	- R^^2 = 1-HKT/OFT
	- R^^2 degeri 0 gelirse aptal bir algoritma olduğunu söylenir.
	- Çünkü 0 ise degerlerin ortalamasının tüm degerlerle ayni olması gerekir.
	- R^^2 negatif degerler alabilir ama negatif cıkması modelin kötülügünü gösterir.
	- Eger R^^2 = 1 ise mükemmel bir algoritma oldugunu söyler gerçek dünyada 1 görme ihitimalimiz yoktur.

	*Düzeltilmiş(ADJUSTED) R Square Metodu
	
	Rsquare metodunun eksileri:
	-R^2 değeri hassas bir değer değildir. Yaptigimiz bazi olumlu calismalari maskeleyebilir.
		*İki ayrı çarpan olan bir doğrusal regresyon düşünelim. bir R^2 değeri elde ettik.
		*Ama regresyona yeni bir çarpan eklemeye karar verdik.
		*Bu durumda 3 ayrı çarpan olan doğrusal regresyonu elde ettik.
		*Yeni R^2 değerini elde ettiğimizde ueni değerin eskisinden farklı olmasını bekleriz.
		*Çünkü yeni değişken ya olumlu ya olumsuz etki etmelidir. Lakin R^2 değeri değişmeyebilir. 
		*Çünkü eklediğimiz yeni değişken R^2 değerini hiçbir zaman azaltmaz. 
		*Çünkü olumsuz etkisi varsa çarpan 0 olarak alınır.
		*Bu sebeple algoritma üzerindeki etkiyi görmemizi engeller.
	-Yukarıda açıklamış olduğumuz durum sebebiyle düzeltilmiş R^2 yöntemi kullanılır.
	-Düzeltilmiş R^2=1-(1-R^2)(n-1)/(n-p-1) yukarıda yazdığımız problemi çözme bu şekilde saglanir.
	-Bu yöntemler dışında farklı yöntemler de vardır bunların dez avantajları var olduğunu bilmeliyiz.
	-Düzeltilmiş R^2 yönteminin de dezavantajları olduğunu unutmamak gerekir. 
	-Burada önemli bir durumun düzeltildiğini görelim ve alternatiflerin olabileceğini unutmayalım.
__________________________________________________________________________________________________________________________
	
---CLASSIFICATION SINIFLANDIRMA PROBLEMLERI---
-Sayısal olmayan verilerin tahmin edilmesi şeklinde tanımlanabilir.
-Sayısal tahmin yapıyorsak regresyon bir verinin kategorisini belirlemek istiyorsak sınıflandırma yapabiliriz.

--------------------------------------------------------------------------------------------------------------------------
	*LOGİSTİC FUNCTİON REGRESSION
	-Adımlı fonksiyon elde ederek sınıflandırma yapmamızı sağlar.
	-Adımlı fonksiyon: Belirli bir değerin altındaki değerler için 0 üstündeki değerler için 1 değeri veren fonksiyon.
	-Adımlı fonksiyon olarak doğrusal bir fonksiyon, adım fonksyionu ya da s tipi fonksiyon kullanılabilir.
	-Bir veya daha fazla değişken kullanılarak sınıflandırma yaptırılabilir
	-S şeklinde fonksiyonlar görmemiz mümkündür.
	-Bu algoritmada kullanilacak veriler olceklendirilmelidir.
	-Boy kilo değerlerine göre kadın erkek şeklinde sınıflandırma bu kategoriye girer.
	-Matematiksel olarak ifade L(t) = (e^t/e^t+1) = (e^t/e^-t+1)  t = A + Bx 
----------------------------------------------------------------------------	
	*KARMAŞIKLIK MATRİSİ (CONFUSION MATRİX)
	-Tıptan gelen bazı veriler için oluşturulmuştur.
	-Gerçek ve tahmin arasında doğruluk oranını verir.
	-Tahminler ve gerçek durumları barındıran bir matristir.
	-Bir karmaşıklık matrisi nasıl gözükür:
		[a,b] (a+d)/(a+b+c+d) oranının büyüklüğü modelin başarısını ifade eder
		[c,d] Yukarıda hesaplanan değer başarı oranı accuracy olarak ifade edilir.
		a-> true positive b-> false negative
		c-> false positive d-> true negative
	-True Positive Rate: gerçekte evet ise kaçı doğru sınıflandırılmış?
	-False Positive Rate: tahmin hayır ise kaçı doğru sınıflandırılmış?
	-Specifity: gerçekte hayır ise kaçı doğru sınıflandırılmış? d/(d+c)
	-Precision: tahmin evet ise kaçı doğru sınıflandırılmış?    a/(a+c)
	-Sensitivity: a/(a+b)
	-Prevalence: gerçekteki evet dağılımı oranı.
	-Bu matris sadece sınıflandırma problemlerinde anlam ifade eder.

	*HATA TİPLERİ
	-false positive Tip 1 Hata
		bizim evet dediğimiz bir şey hayır ise
	-false negative Tip 2 Hata
		bizim hayır dediğimiz bir şey evet ise
----------------------------------------------------------------------------
	-SVM'de Hata
	-Risk area içerisinde test verisi çıkması ve bunun yanlış sınıflandırılması

	*ACCURACY PARADOX doğruluk paradoksu
	-ZeroR algoritması eğitim için verilen veri seti içerisinde çoğunlukta olan sınıfa göre test verilerini sınıflandırır.
	-Normal bir sınıflandırma algoritmasına göre bazen daha başarılı gibi gözükebilir ama dikkatli olunmalıdır
	-Böyle durumlarda sadece Accuracy e bakarak karar vermememiz gerekir.
	-Denge elde etmeye yönelik karmaşıklık matrisi içerisindeki farklı değerleri kullanabiliriz

	-ROC EĞRİSİ Receiver Operating Characteristic
	-tpr = TP/TP+FN  TP-> true positive tpr-> true positive rate buranın değerinin yüksek olması hata oranını ARTIRIR
	-fpr = FP/FP+TN  FN-> false negative fpr-> false positive rate buranın değerinin yüksek olması hata oranını AZALTIR
	-Görsel olarak makine öğrenmesi algoritmasının nerede olduğunu anlamamızı sağlar
	-Farklı sınıflandırma algoritmalarını grafiksel olarak kıyaslama için kullanılabilir.
	-Accuracy Doğrularında positive/negative oranına göre veri setlerinin oranı bulunur.
	  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	*KNN K NEAREST NEIGHBORHOOD:
	-Sınıflandırılacak veriler uzaya dökülür.
	-Bir veri seçilir veriye en yakın 3 (k) komşu seçer.
	-Bu komşular içerisinde çoğunluk hangi sınıfta ise seçtiğimiz veri bu sınıftadır.
	-Eğer komşular sınıflardan eşit sayılarda ise bu drurumda uzaklığa bakılır.
	-Bu yukarıda anlattığımız lazy learning örneğidir. Yani başlangıçta öğrenme yapılmayan çeşittir.
	-Başka bir versiyonda (eager learning) önce veriler işlenir veriler çekilir.
	-Çektiği verilere göre uzayı bölgelere ayırır. Verilere bir daha ihtiyaç duymaz.
	-Eğer yeni bir veri gelirse hangi bölgede olduğuna bakarak karar verir.
	
	-İki veri arasındaki uzaklığı ölçmenin farklı hesaplama yolları da vardır.
	-Euclidean minkowski mahalanobis bu hesaplama örnekleridir.
	-Hangi ölçümün hangi veri seti için uygun olacağı önemlidir bu seçime dikkat edilmelidir.
	
	-Bu algoritma kullanılırken eğer veri setimizi bozacak uç verilerimiz var olabilir.
	-Bu durumda komşu sayısını fazla seçmek iyi bir şey değildir. 
	-Çünkü komşu uç değerler böyle bir durumda yeter sayıda komşu bulamayacaklar ve yanlış sınıfa dahil olacaklardır.
	-Yukarıda yazdığım madde göz önüne alınarak komşu sayısı seçilmelidir.

	KNN algoritmasında k değeri neye göre belirlenir:
		Voronoi hücreleri üzerinden algoritmayı gözden geçirelim.
		Bu hücre durumlarını webden araştırarak bulunuz resim ya da data.
		Bu veri üzerinden k nın durumunu düşünelim.
		Pattern Classification kitabında bu durum uzun uzun ele alınmıştır.
		Genel bir formül bulunmuştur karekök(eğitim boyutu)/2 bu tartışmaya açık bir formüldür.
		Bir kural değildir. K sayısı sizin isteklerinize göre değişebilir. 
	KNN algoritmasında veri sınır çizgisine düşerse ne olur:
		Bu durumda hangisine daha yakın olduğu hesaplanır.
		Örneğin mavi örneklerin sınıra daha yakın olması durumunda eşitlik bozulur.
		
	Kaynaklar	 
	sklearn knn yazıp kaynaklara bakabilirsin
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	*SVM ile SINIFLANDIRMA SVC MULTI CLASS 
	-Regression yöntemiyle neredeyse aynı şeyler söylenir.
	-Sınıflandırmada iki sınıfın birbirinden keskin ayrımı yapılmaya çalışılır
	-RBF ya da polynomal üssel kullanılabilir. bu kullanımlar veri setine göre seçilmelidir.
	-Uç değerler için çok uygun değildir.
	-Ayrıca ölçeklendirilmemiş veri setleri SVM'de kullanılamaz.
	-Çok uç değerlerin olduğu veri setlerinde kullanılamaz.
	-İki sınıf arasında bir ayrım yapıldıktan sonra veri seti unutulur
	-Sınıf ayrımı yani uzay bölgeleri üzerinde yeni veriler sınıflandırılır.
	-Yani verinin bulunduğu bölge sınıfını belirler. 
	-Eğer marjin içerisine hiçbir şekilde veri almyorsa hard svc olarak isimlendirilir
	-Eğer veri alıyorsa soft svc olarak isimlendirilir 	
----------------------------------------------------------------------------
	*SVM KERNEL TRICK
	-Doğrusal olmayan hiç bir şekilde doğrusal olarak çözümlenemeyen veriler için kullanılır.
	-Non linear alanın orta noktası bulunur ve veri setine bir boyut daha eklenir.
	-Belirlediğimiz orta nokta bize en yakın nokta olur.
	-Orta noktaya yakın değerler bize daha yakın orta noktaya uzak değerler bize daha uzak olur
	-Bu da bize uzak ve yakın olmak üzere iki küme oluşturma imkanı sağlar.
	-Bu şekilde boyut artırmaları yapılabilir.
	-Yeni oluşan çok boyutlu küme üzerine farklı çizimler yapılarak sınıflandırmalar hassas şekilde yapılır.
	-Ayrıca birden fazla kernel trick bir veri setinde kullanılabilir.
	-Bu çekme işlemi nasıl yapılır:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	*NAIVE BAYES
	-Koşullu olasaılıklardan yararlanarak sınıflandırma problemleri çözme amacıyla kullanılır
	-Koşullu olasılık ile gelir düzeyine göre bilgisayar alma oranı bulunabilir
	-Bilgisayar alan kişileri gelir düzeyine göre sınıflandırma yapabilirsiniz.
	-Dengesiz veri kümelerinde çalışabilmesi en önemli özelliğidir.
	-Önce bilgisayar alma ve almama oranı hesaplanır.
	-30 yaşından küçük bir kişinin bilgisayar alma ve almama oranı
	-Bu şekilde şartlara ayrılan durumumuz üzerinden sınıflandırmamız rahat bir şekilde yapılabilir.
	-Lazy learning: veri önce gelir o veri içerisinde beklenir veri akışı devam ederse öğrenmeyi yapar
	-Eager learning: veri gelmeden önce tüm veriler üzerinden tüm ihtimalleri öğrenmeye çalışır
	-Büyük veri çalışmalarında lazy learning daha avantajlıdır.
	-Gaussian naive bayes-multinomial naive bayes-bernoulli naiv bayes
	-Sürekli değerler    - kesikli sayılar için  - iki ihtimalli olan veriler için
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
	*KARAR AGĞACI İLE SINIFLANDIRMA DECISION TREE
	-Bölgelere ayrılması hususunu yukarıda analatmıştık
	-Çoğunluğun bulunduğu alan çoğunluğa göre sınıflandırılır
	-Ve yeni gelen veri için oluştururlan bölgelere göre karar verir
	-Bazen birbirine yakın değerler için bölme işlemleri devam edebilir.
	-Ama burada tüm verilerin teker teker ayrılmasından kaçınılması gerekir
	-Yoksa overfitting olur ve program tüm verileri ezberle
	-Karar ağaçlarında ordinal ya da nominal veriler bulunmuyorsa direkt sınıflandırmalara başlanabilir
	-Ama sayısal değerler barındırıyorsa sayısal değerlerin bölünmesi için ayrı bir algoritma kullanılır.
	-Ağaç dallanması Quinlan's ID3 information(Gain) yöntemi ile çözülebilir.
	-Burada değeri yüksek çıkan ilk dallanmayı yapacağını söyler.
	-Bilgisayarlar bu şekilde ağaç yapılarını oluşturur.
	-Dökümantasyondaki parametrelerden CRITERION parametresini kullanacağız
	-Geany: p*p lerin negatiflerinin toplamı
	-Entropy: p*log(p) nin negatifleri toplamı
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	*RASSAL AĞAÇLAR RANDOM FOREST 
	-Ensemble learning veriyi parçalara bölüp parçalar üzerinden karar ağacı oluştururlur.
	-Her karar ağacı en son birleştirilecek çoğunluğa göre sınıflandırma yapılır
	-Xboxlarda hareket algılama ile ilgili yazılmış makale microsoftun linki alt satırda
	-Majority vote algoritması üzerine kurulu bir algoritmadır.
	-N_estimators : kaç ağaç oluşturayım?
	-Criterion : karar ağacında belirtildi?
	
	ADA BOOST - QDA - GAUSSİAN PROCESS - NEURAL NET


	
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	*KÜMELEME BÖLÜTLEME
	
	-Görüntü işeleme ve müşteri segmentasyonu gibi konular buraya dahildir.
	-Elimizdeki örneklerin kaç sınıf olduğu ya da nasıl sınıflanacağı öncesinde verilmez.
	-Gözetimsiz öğrenme unsupervise öğrenmedir.
	-Burada train test verileri şeklinde bir ayrım yoktur.
	-Sınıflandırma probleminden farkı bir sınıf tanımı ve train test bölümü yoktur.
	-Kendi dünyasında kendi sınıflarını oluşturur şuan çok fazla gelişmiş modeli yoktur.
	-En çok Müşteri segmentasyonu , pazar segmentasyonu , sağlık görüntü işleme alanlarında kullanılır.
	-Müşteri segmentasyonu -> Collabration Filtering müşterinin kendisine benzeyen kişilerle gruplandırılması.
	-Yani daha önceden hakkında data bulunmayan bir kişiyi bir segmente koymayı sağlar.
	-Özel kampanyalar yapma, tehdit ve sahtekarlık yakalama,eksik veri tamamlama işlemleri gibi yerlerde kullanılır.
	-Tehdit ve sahtekarlık yakalama da outlayerda olan veriler kullanılarak oluştururlur.
	-Eksik veri tamamlamada verinin farklı segmentlerine göre veri tamamlamalar yapılabilir.
	-Daha çok oluşturulan sınıflandırılmış bir verinin alt sınıflandırmalar yapılarak segmentlerin oluşturulmasıdır.
----------------------------------------------------------------------------	
	*K-MEANS K-ORTALAMA
	-Kaç küme olacağı kullanıcıdan parametre olarak alınır.
	-Bunun kullanıcıdan almayan kendi karar veren şekli de vardır. (Ex means)
	-Rastgele olarak k merkez noktası seçiyor.
	-Her veri örneği kendisine yakın merkez noktasıyla ilgili kümeye atılır.
	-Her küme için tekrar merkez noktaları oluşturulur ve kaydırma yapılır.
	-Ağırlık merkezlerine göre kaydırma yapılır. 
	-Ağırlık merkezi devamlı aynı yerde çıkmaya başlayınca durur. 
	-Gözetimsiz bir öğrenmedir her veri model için eşit değer taşır.
	-Değişik varyasyonlarında merkez noktası seçimi kullanıcıdan parametre alma işlmeleri farklılık gösterebilir.
----------------------------------------------------------------------------
	**K-Means Başlangıç Noktası Tuzağı
	-Rastgele başlangıç noktasının yanlış veri uzaylarına dağılması bölütlemeyi kötü etkileyebilir.
	-Kolayca 3 adet sınıfa bölünebilen bir veri kümesi düşünelim.
	-Merkezlerin rastgele dağıldığı durumda bir sınıfa iki merkez gitme ihtimali vardır.
	-Bu ihtimal dikkate alınmalıdır. 
	-Rastgele merkez atama yerine farklı çözümlerin kullanılması daha doğru olur. 
----------------------------------------------------------------------------
	**K-Means ++ 
	-K-Means geliştirilmiş versiyonudur. 
	-Rastgele seçilen noktalardan en yakınına her noktada uzaklığı hesaplar.
	-Yeni noktaları mesafenin karesini olasılık alarak bulur.
	-Burada da bir rassallık vardır bu da sorun oluşturabilir.
----------------------------------------------------------------------------	
	**K nın kaç olduğunun önemi
	-K nın seçimi gözetimsiz öğrenme algoritması olduğu için önemlidir.
	-Ex means algoritması ise bir aralık verildiğinde bu aralıktaki tüm bölütlemelerin skorunu çıkarır
	-Ama başarının nasıl bulunacağı da başka bir sorun olduğunu unutmayalım.
	-Bu skorlama WCSS yöntemi ile yapılır. (within-cluster sums of squares)
	-Bir merkez seçilir ve onun kümesindeki verileri ona uzaklıklarının kareleri toplanır.
	-Bu skor ne kadar yükselirse bölütleme algoritması o kadar kötü olduğu söylenebilir.
	-Ama bu skor overfitting olmaması için çok düşürülmemelidir. 
	-Burada bir grafik oluşturulması ve grafiğe göre karar verilmesi daha doğru olacaktır.
	-Oluşturulan grafikte eğimin aniden değiştiği dirsek nokta genelde doğru nokta olarak alınır.
	-Overview of clustering methods dan hangi metodu kullanacağınızı bilgi edinebilirsin.
	-Bunu scikitlearn sitesinden alabilirsin.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
	*HIERARCHICAL CLUSTERING
	**Agglomerative
	-Aşağıdan yukarıya doğru çalışır. 
	-Her veri tek bir küme bölüt ile başlar
	-En yakın ikişer komşuyu alıp ikişerli küme oluşturulur.
	-En yakın iki kümeyi alıp yeni küme oluşturulur
	-Tek bir bölüt küme oluncaya kadar devam eder
	-İçerisindeki sınıf yapıları kaybolmaz
----------------------------------------------------------------------------	
	**Divisive
	-Yukarıdan aşağıya sınıflandırma şeklinde olur
	-Bütün veriler bir küme olarak kabul edilir.
	-Birbirine yakın olan noktalar kümelenir son tek nokta kümeye eklendiğinde biter
	-Kısaca agglomerative'in tam tersidir.	
	-Tek bir veri bir pakete yerleştiğinde sonlanır.
----------------------------------------------------------------------------	
	*Dikkat Edilmesi Gerekenler:
	-Bu algoritmalarda mesafe ölçümü bir problemdir
	-Mesafeler distance matrix ile gösterilebilir.
	-öklid mesafesi kullanılabilir.
	
	-Referanslar ise diğer problemdir. Buna farklı çözümler vardır. 
	-Referans olarak en yakın noktalar alınabilir.
	-En uzak noktalar hesaplanabilir.
	-Kümenin orta noktası referans alabilir.
	-Ortalamalar referans alınabilir.
----------------------------------------------------------------------------
	**Dendogram
	-Tüm noktaların yazılı olduğu ve aralarındaki mesafye göre yerleştirilmiş tablo yapısı.
	-Bu tablo yapısında birleştirmeler gösterilebilir.
	-Kümelerin birleşmelerinin mesafelere bağlı olduğunu okunabilir biçimde gösterilmesini sağlar.
	-Bu tablo yapısına göre hiyerarşik bölütleme görülmesi kolaylaşır.
	-Kullanıcının istediği kadar bölüt oluşturma imkanı sağlanır.
	-En optimum yapıyı elde etmek için dendogramın en uzun olduğu bölmeye bakılabilir
----------------------------------------------------------------------------	
	*WARD METHOD 
	-Her bölütün başka bir bölüte uzaklığı
	-Wcc değeri hesaplama yöntemini kullanır.
	-Ward methodu kullanılarak da optimum model bulunabilir.
	-Bunu sen araştır.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	*BİRLİKTELİK KURAL ÇIKARIMI ASSOCIATION RULE MINING LEARNING ARM/ARL
	-3 farklı tipi üzerinden inceleme yapılabilir apriori , fp-growth, eclat
	-Biz apriori ve eclatı inceleyeeğiz.
	-Fp-growth araştırılacak.
	-Bu algoritmalara alışveriş alışkanlıkları sebebiyle ihtiyaç duyulduğu söylenebilir.
	-Tekrar eden verilerin yakalanması durumunda kullanılan modeldir.
	-Armut alanlar elma da aldı gibi.
	-İlişkisellik mi nedensellik mi? sorusunu temel alır. Causation Correlation
	-Temeli makineler insanlar gibi düşünüyor mu temel sorusuna dayanır.
	-Bilgisayar için iki ürün beraber satılıyorsa bunun neden olduğunu sorgulamaz.
	-Sadece o iki ürünü beraber satar.
	-Bilgisayar dondurma satışı ve köpekbalığı saldrıları arasındaki ilişkiye bakar.
	-Burada bilgisayarlar nedenselliği dikkate almaz yani neden aynı anda oluyoru sormaz.
	-Biz sorarız ve bunu güneşe bağlarız.
----------------------------------------------------------------------------	
	**DESTEK SUPPORT
	-Yüz kişiye sorduk şeklinde düşünelim eylemin varlığı önemli
	-Yüzde kaç bir eylimin yapıldığı
	-Support(a) = (a varlığını içeren eylem)/(Toplam eylem sayısı)
----------------------------------------------------------------------------	
	**CONFIDENCE(a->b) = (a ve b varlığını içeren eylemler) / (a varlığını içeren eylemler)
	-a olayını yapan kişilerin yüzde kaçı b olayını yaptı şeklinde yüzdelik
	-Tek bir ürün eylm olmadığı zaman bu yöntem kullanılabilir.
----------------------------------------------------------------------------	
	**LIFT(a->b)  confidence(a->b)/support(b)
	-a eyleminin b eylemine etkisi nedir sorusuna cevap verir.
	-Lift değeri 1'in altında çıkarsa a olayı b olayını negatif etkiliyor
	-Lift değeri 1'in üstünde çıkarsa a olayı b olayını pozitif etkiliyor	
----------------------------------------------------------------------------	
	**OLAY SIKLIĞI(APRIORI)
	-Önce parçalayarak oranlara bakıyoruz.
	-Sonra parçadan bütüne ilerliyoruz ve frekansı düşük olan verileri eliyoruz.
	-Sonra o parçaların birbirlerine etkisi dikkate alınarak bazı birleştirmeler yapıyoruz.
	-En iyi durum elde etmeye çalışıyoruz
	-Bir örnek yapalım:
		beraber alınan ürünler listesi elimizde olsun.
		itemset 1, 2, 3, 4, 5
		sup 	3, 3, 3, 1, 3         
		Burada 1 numaralı ürün 3 farklı ürünle farklı zamanlarda beraber sipariş edilmiş.
		APRIORI eleyerek parçadan bütüne gider. Örneğin ilk adımda 4 numaralı ürünü eler.
		Sonra farklı kombinasyonlar yapar 2 li tablo şeklinde tekrar gösterir.
		Tekrar eleme yapar ve beraber satan 3 ürünü bulur. 
	-Bu şekilde sınıflandırmalarda pazarlama önerilerinde kullanılır.
	-Bu algoritma için scikitlearn de bir fonksiyon ve sınıf yoktur.
	-Bunu kullanacağın zaman githubdan indir.
----------------------------------------------------------------------------	
	**ECLAT ALGORİTMASI
	-Equivalence Class Transformation
	
	-Apriori -> Breadth first search
	-Eclat -> Depth First Search 
	
	-Eclat adım olarak Aprioriye göre çok daha kısadır. Apriori'ye göre oldukça kısadır.
	-Dikey grafik olarak veri tabanı dizilir. Örneğin 1 numaralı ürün hangi çantalarda satın alınmış.
	-Bütün veriler okunmadan bir sonraki basamaklara geçilebiliyor.
	-Dikey olarak çizilen tabloda verilerin kesişimine bakılır.
__________________________________________________________________________________________________________________________

REINFORCED LEARNING TAKVİYELİ PEKİŞTİRMELİ ÖĞRENME
	-Reinforced learning robotlar ve hareketleri devamlı düşen bir robotun bir süre sonra düşme sıklığının azalması.
	-Kısaca bir algoritmanın hatalardan öğrenmesini ifade eder.
	-Bizim tanımladığımız hedefleri gerçekleştirme konusundaki en optimize duruma erişmek gibi düşünülebilir.
	-Yazılan algoritma bir aksiyon yapar ve gözlem yaparak aksiyonun puanlaması yapar.
	-Puanlamaya göre cezalar olur ve sistemler bu şekilde en iyi durumu elde etmeye çalışır.
	-AlphaGo kendi kendine oynayarak satranç öğrenmiş bir yapay zeka örneği (sen de araştırarak öğren)
	-Expert system lerde gelebileceği en iyi seviye insan olacak şekilde düşünülebilir.
	-Ama bu şekilde gelişen algoritmalar spesifik konularda insandan daha iyi olabilir.
	-Agent -> environment -> agent -> environment sonsuz döngüsünde model devamlı döner.
	-Aşağıdaki başlığı inceleyelim:

	*TEK KOLLU CANAVAR SLOT MAKİNALARI ONE ARMED BANDIT
	-Bir kumarahaneye gittiniz ve çok sayıda slot makinelerinden gördünüz.
	-Bu makineler sizin paranızın %80-90 oranında kısmını size geri verir.
	-Bu makinelari keşfettiniz ve dağılımları incelediniz.
	-Hepsi aynı oranda kazansa bile dağılımları inceleyip en karlı makineyi seçme işlemini yapmak istiyoruz.
	-Bu teori yukarıda yazdığım kısma dayanır.
	-Bir reinforced yöntemi ile bulunabilir. Bunun araştırması sana kalmış :)

	*A-B TEST
	-Bir reklamın kullanıcı tarafından tıklanıp tıklanmayacağını bulmak için kullanılır.
	-Kullanıcılara birden fazla reklam göstererek insanların tepkisi ölçülür ve sonuçlar kaydedilir.
	-Sonuçlara bakarak en hızlı ve en az denemeyle karar vermemiz gerekiyor.
	-Bir reinforced yöntemi ile karar verilebilir.

	[+] BU KONUNUN İLK ALGORİTMASI UCB Upper Confidence Bound
	
	*UPPER CONFİDENCE BOUND UST GUVEN SINIRI
	-Her olayın arkasında bir dağılım vardır.
	-Kullanıcı her seferinde bir eylem yapar (event e)
	-Bu eylem karşılığında skor döner. Bu eyleme örnek vererek adımları sıralayalım.
	-Örneğin bir reklanma oranı üzerinden hesap yapalım tıklanma 1 tıklanmama 0 gibi.
	-Amaç tıklanmaları maksimuma çıkarmak.
	-Alt sınır ve üst sınır olarak iki durumumuz var: mükemmel durum ve en kötü durum
	-Bilmediğimiz gizi dağılım durumunu tespit etmek için denemeler sonucu dağılımın bazı kısımları elenir.
	-Bu elenmelerden sonra en iyi durum en hızlı şekilde elde edilmeye çalışılır.
	-Bu algoritma belirli bir aşama sonrasında alternatifler arasında en yüksek değere sahip olanı baz alır
	-Belirli bir hata oranını göze alarak optimum duruma en yakın durumu elde etmeye çalışır.
	-Aşağıdaki senaryoya bir göz atalım:
	
	SENARYO
	Reklam Verileri: en fazla tıklanan reklam bulunacak ilk 5 güne bakılacak 6. gün en çok gösterilen reklam kullanıcı karşısına çıkacak
----------------------------------------------------------------------------	
	*Random Selection: 
		-Herhangi bir zeki seçim yapmaz rastgele seçer ödül kazanma mantığı işler.
		-Bir havuzun içerisinden rastgele reklamlar seçilir kullanıcılara gösterilir.
		-Kullanıcıların tıkladıkları puan kazanır. Es geçtikleri puan kaybeder.
		-Bu mantığa göre en optimize sonuca ulaşabilecek miyiz??
		-Bunun python kodunu yazarak deneyeceğiz.
		-Burada önemli bir şey var reklamların tıklanma sıklığı eşit değildir.
----------------------------------------------------------------------------	
	*UCB Algoritması:
	-ADIM1: Her turda tur sayısı n olsun her reklam alternatifi için aşağıdaki sayılar tutulur:
		Ni(n): i sayılı reklamın o ana kadarki tıklanma sayısı
		Ri(n): o ana kadar ki i reklamına gelen toplam ödül
	-ADIM2: Yukarıdaki iki sayıdan aşağıdaki değerler hesaplanır:
		O ana kadarki reklamın ortalama ödülü Ri(n)/Ni(n)
		Güven aralığı için aşağı ve yukarı oynama potansiyeli di(n)((3/2)*(log(n)/Ni(n)))^(1/2)
	-ADIM3: En yüksek UCB değerine sahip olan alınır.
----------------------------------------------------------------------------
	REINFORCED LEARNİNG:
	*THOMPSON ÖRNEKLEMESİ:
	-Adım 1 : Her aksiyon için iki sayıyı hesaplamalıyız 
		Ni1(n): o ana kadar ödül olarak 1 gelmesi sayısı
		Ni2(n): o ana kadar ödül olarak 0 gelmesi sayısı
	-Adım 2: her ilan için aşağıda verilen Beta dağılımında bir rastgele sayı üretiyoruz
		Oi(n) = B(N1i(n) + 1.N0i(n) + 1)
	-Adım 3: En yüksek Beta değerini seçiyouz
	-Bayes yaklaşımını takip eden bir algoritmadır daha çok bayese yakındır
	-UCB bu algoritmaya göre greedy algorithm olarak isimlendirilebilir.
	-Elinizde yeterli veri yok ve bir miktar veriden hem öğrenme hem uygulama yapma
	-Gözlemlerin eşit dağılmadığı durumlarda
	-UCB sıçramalarda kullanılır. Thompson ise lineer bir ilerleme ile yapılır.
__________________________________________________________________________________________________________________________

NATURAL LANGUAGE PROCESSING
DOĞAL DİL İŞLEME

	2 tip hedef olabilir
	*Natural Language Understanding NLU
	-Tüm makine öğrenmesi modellerinde olduğu gibi 3 adımdan oluşan algoritmaya sahiptir.
	-Veri ön işleme - öznitelik çıkarımı - öğrenme AŞAĞIDAKİ KAVRAMLAR ARAŞTIRILMALI
		-Veri ön işleme: Stopwords, case, parsers
		-Öznitelik Çıkarımı: kelime sayıları, kelime grupları, N-gram, TF-ID
	*Natural Language Generetion NLG

	Yaklaşımlar
	*Linguistik (dil bilimi) yaklaşımı
		-Cümle yapısına göre analiz yapar kelimelerin ek kök analizini yapar.
		-Bu sebeple yavaş çalışır ama daha isabetlidir.
		-Bu yaklaşımın adımlarının bazı ayrıntıları aşağıdadır.
		-Morfoloji Şekilbilim bütün alternatifler listelenir, bir kelimenin bütün anlam ihtimalleri alınır.
		-Syntax Sözdizim anlamları sıralanan kelimenin cümle içindeki yeri tespit edilir.
		-Semantics Anlambilim morfoloji kısmında belirtilen anlamalardan hangisi syntaxa uygun olduğu bulunur.
		-Pragmatics Kullanımbilimi kullanılan kelimenin ironi olup olmaıdığına bakılır.
--------------------------------------------------------------------------------------------------------------------------
	*İstatistiksel yaklaşımlar 
		-Metin sınıflandırmada kelimelerin anlamını anlamadan metnin hangi konuda olduğu anlaşılabilir.
		-Kısaca bir kelimenin bir metinde kaç defa geçtiğini inceler.  
		-N-gram belirli karakterlerin peşpeşine gelmesi ihtimallerini bulur
		-TF-IDF
		-Word-Gram
		-BOW Bag OF Words mail spam mı değil mi gibi şeyleri tespit edebilir.
			spam mailde olan kelimeler ve olmayan kelimeler farklı çantalara konur ve metinden sayılır.
	*Hibrit yaklaşımlar  	 
		-İki yaklaşımı karıştırarak metni anlamlandırmaya çalışma yaklaşımıdır.
----------------------------------------------------------------------------	
	*KULLANILDIĞI ÖRNEKLER
	-Yazar Tanıma
	-Metin Sınıflandırma
	-Duygusal Kutupsallık Fikir Madenciliği
	-Anomali Yaklanması
	-Metin Özetleme
	-Soru Cevaplama
	-Etiket Bulurları ve Anahtar Kelime Çıkarımı
----------------------------------------------------------------------------	
	*KÜTÜPHANELER
	-nltk
	-Spacy : Endüstriyel
	-nlp : Stanfor university
	-OpenNLP : Apache açık doğal dil işleme
	-RAKE (Rapid Automatic Keyword Extraction)
	-Amueller Word Cloud
	-Tensor Flow Word2Vec
----------------------------------------------------------------------------
	*TÜRKÇE DOĞAL DİL İŞLEME KÜTÜPHANELERİ
	-Zemberek
	-İTÜ
	-TSPELL
	-Yıldız Teknik Üniversitesi Kemik
	-Wordnet Balkanet
	-TrMorph
	-TSCorpus
	-Metu-Sabancı Tree Bank ve ITU Dpğrulama Kümesi
----------------------------------------------------------------------------	
	-Makine öğrenmesinde hazır verilerden yararlanma durumu yoktur.
	DDİ de biz makinelerin insan öznitelikleri çıkarma konusunda insan yakınlaşmalıdır
	Makine öznitelik konusunda bizimle eşdeğer değildir.
	Bu sebeple veri ilk önce önişlemeden geçirilir sonra veri öznitelikleri çıkarılır.
	Sonrasında makine öğrenmesi algoritmaları çıkarılır.
	Veri ön işleme : preprocessing, stop wods, case, Parsers(html)
	Öznitelik Çıkarımı : feature engineering, kelime sayıları, kelime grupları, n-gram, RF-IDF
__________________________________________________________________________________________________________________________
	
YAPAY SİNİR AĞLARI: ARTIFICIAL NEURAL NETWORK:

	-İnsan vucudundaki sinir hücrelerine benzer yapılar oluşturarak bir yapay zeka oluşturmayı ifade eder.
	-Anahtar Kelimeler:
		Sinirbilim ve bilgisayar bilimi
		Nöron
		Sinapsis
		YSA çalışma mantığı
		Gradient Descent
		Stochastic Gradient Descent
		Backpropagation
	
	-Bu modelde veriler kesinlikle standartlaşmış olmalıdır 0-1 aralığında olmalıdır.

    Not: [+] Nöral sinir ağları her zaman ön işleme istemez eğer nöron sayınız yeterliyse.
	 [+] Çünkü ön işlemeyi sizin yerinize fazladan verdiğiniz nöronlar yapar

	-Bu modelde çıktılarda 0-1 aralığında gelir. Sonuçlar buna bağlı olarak oluşur.
	-Çıktılar çoklu bir şekilde de olabilir. Birden fazla çıktı görülebilir.
	-Sinapsislerin üzerinde ağırlıklar taşınır bu ağırlıklar karar verme sürecini etkiler.
	-İnputlar bir operatör yardımıyla ağırlıklarla güncellenir ve outputa aktarılır.
	
	-Örnek olarak girdiler ağırlıklarla çarpılır sonuçlar toplanır ve bu sonuca göre ağ output verir.
	
	-Bir nöronun aktive olması için bir aktivasyon fonksiyonu vardır. 
	-Nöronda aktifleşme olup olmayacağına bu fonksiyonun outputuna göre karar verilir.

	*Aktivasyon fonksiyonu ve çeşitleri:
		-Bu fonksiyonlar insan vucudunda bir nöronun elektriksel sinyalinin eşik değeri gibi düşünülebilir.
		-Herhangi bir fonksiyon aktivasyon fonksiyonu olarak kullanılabilir(genelde).
		-Ama bazı fonksiyonlar daha çok kullanılır.
		-Sigmoid fonksiyonlar: 1/(1+e^-t) en çok kullanılan fonksiyondur.
		-Adım fonksiyonu bir treshold değeri olan donksiyondur, belirli bir noktadan sonra atlama yapan fonksiyondur. Ya 1 ya 0 döndürür.
		-Sigmoid fonksiyonlar 0 ile 1 arasındaki değerleri belirli bir eşik değer olmaksızın alırlar 
		-Grafiksel olarak düşünülürse [0,1] aralığında değerleri çıktı olarak vereceği görülür. 
		-Düzleştirilmiş Fonksiyon ise belirli bir aralıkta 0 değeri verir. 
		-Belirli bir değer sonrasında 0 dan büyük değerler alır. max(0,x) şekilinde bir fonksiyon düşünülebilir.
		-Tanh fonksiyonu (bu araştırılacak)
		
	*Yapay Sinir Ağları:
		-Giriş katmanı gizli katman ve çıkış katmanı olmak üzere 3 katmandan oluşur.
		-Gizli katman sayısı artabilir. Ya da gizli katmandaki nöron sayısı artabilir.
		-Çıkış katmanı ve gizli katman bir nörondan oluşur.
		-Yapay sinir ağlarında gizli katmanda kaç adet nöron olacağı önemlidir.
		-Bunu belirlemek için koordinat sisteminden faydalanabiliriz.

		|   		Nöron sayısının nasıl belirleneceği aşağıdaki örneğe bakalım:
		| .       .           Yandaki karede köşegenlerin noktalarını içine alacak 
		|				yapay sinir ağı tasarlamak istiyoruz iki tane girişimiz
		| .       .			var bir çıkışımız var gizli katmanda kaç nöron olur						
		|________________		yalnızca doğrusal olarak uzayı bölebiliriz.
		
		Bu durumda köşegenlerin çıktı içerisinde olmasını istiyorsak en az iki nöron kullanmalıyız.
		
	*Yapay Sinir Ağları Nasıl Öğrenir:
		-Buradaki öğrenme ağırılık ve treshold sayısal değerlerinin artırılması ve azaltılmasından ibarettir.
		-En basit öğrenme Perceptron: bir ceza mekanizması işler. 
		-Ceza = 1/2 (gerçek-tahmin)^2 her yanlış tahminde ağırlıklar ceza ile çarpılır.
		-Bu çarpma işleminin farklı değerlerle de yapılabileceğini unutmamak gerekir.
--------------------------------------------------------------------------------------------------------------------------
	Gradyan Alçalış:
		-Yapay sinir ağlarında öğrenme esnasında ağırlıklar belirli değerlerle çarpılır.
		-Bu öğrenme süreci çok katmanlı yapay sinir ağlarında çok fazla işlemle olmaktadır.
		-Öğrenme sürecini sistematikleştirmeye ve doğru öğrenim yöntemine ihtiyacımız var.
		-Eğer büyük öğrenme oranları kullanılırsa ağırlıkların devamlı 2 farklı değer arasında kaldığı ve doğru değeri bulamadığı gözlenebilir.
		-Küçük öğrenme oranları kullanarak doğru koşulun sağlandığı nokta bulunmya çalışılır.
		-Gradyan alçalış tam olarak bu duruma verilen isimdir.
		-Kısaca ağırlıkların aynı değerler arasında gidip gelmesini engellemek için oluşturulmuştur. 
--------------------------------------------------------------------------------------------------------------------------	
	Stokastik-Batch (yığın) Gradyan Alçalış:
		-Gradyan alçalışın farklı bir çeşididir. Yerel minimum noktalar için geliştirilmiştir.
		-Mutlak minimum noktasını bulmaya çalıştığımızı varsayalım. 
		-Yerel minimum bir noktayı mutlak minimum olarak almamızı engelleyen bir algoritmaya ihtiyacımız olacaktır.
		-Stokastik verilerin tamamını görmeden karar verir. 
		-Batch bu minimum noktaları ayırt etmek için verşlerin tamamına bakılır.
		-Mini batch yaklaşım diye bir algoritma daha vardır. Verinin belirli bir kısmını okuyarak karar verme olarak adlandırılabilir. 
		-Bu yaklaşımlardaki amaç bize gelen veri setindeki en optimum veriyi bulabilmek ya da bize gelen verilere en uygun anlamı kazandırmaktır.
--------------------------------------------------------------------------------------------------------------------------	
	*Geri Yayılım (Backward Propagation)
		Algoritma Adımları:
		1 Bütün ağı rasgele sayılarla (sıfıra yakın ama sıfır değil) ilkendir.
		2 Veri kümesinden ilk satır giriş katmanına verilir.(Her öznitelik bir nöron)
		3 İleri yönlü yayılım yaparak YSA istenen sonucu verene kadar güncellenir.
		4 Gerçek ve çıktı arasındaki fark hesaplanır.
		5 Geri yayılım yaparak her sinaps üzerindeki ağırlık hatadan sorumlu olduğu miktarda değiştirilir. Değiştirilme miktarı ayrıca öğrenme oranına bağlıdır.
		6 1-5 arasındaki adımlar istenen sonuç elde edilene kadar güncellenir.
		7 Bütün eğitim kümesi çalıştırıldıktan sonra bir tur (epoc) Aynı veri kümeleri kullanılarak tur tekrarları yapılır. (tur sayısı sınırlanabilir)
--------------------------------------------------------------------------------------------------------------------------	
	-Learning rate Öğrenme hızını ifade eder. Epoc tur sayısını ifade eder.

	(Takviyeli öğrenme veya eldeki bütün verileri ilgili ağda çalıştırdıktan sonra bir seferde güncelleme yap)Bunlar madde 6 için

	*İleri Yayılım (Forward Propagation)
		-Geri yayılımla farkından bahsederek bu konuyu bitirelim.
		-İleri yayılım sinir ağının girdi verilerinden çıktı üretmek için ilerleme işlemidir.
		-Geri yayılım ise hatayı geriye doğru yayarak ağırlıkların güncellenmesi için kullanılan bir öğrenme mekanizmasıdır.
		-İleri yayılım aşamasında ağın çıktıları hesaplanırken, geri yayılım aşamasında ağın ağırlıkları güncellenir ve ağın daha iyi sonuçlar üretmesi sağlanır.
		-Aradaki fark biri sonuca giderken düzeltmeler yapar diğeri ise sonuçtan gelerek nöronlardaki ağırlıkları düzeltir.
 
__________________________________________________________________________________________________________________________
		
BOYUT İNDİRGEME 

	*PCA:
		-Kullanım alanları: Gürültü filtreleme, Görselleştirme, Öznitelik çıkarımı
				   Öznitelik eleme dönüştürme, Sinyal işleme, Görüntü işleme 
		-Boyut dönüştürme olarak tanımlanabilir. Tabi boyutlar dönüştürülürken veriler kaybolabilir. Dikkatli olunması gerekir.
		-Eigen value Öz değer ve Eigen vector Öz vektör burada hatırlanması gereken iki kavramdır.
		-Bir örnekle hatırlayalım:
		[+] Bir matris için özdeğer ve özvektör sayısı birden fazla olabilir.
			[1 2 0]   [1]   [3]      [1] 	A*v = x*v x: özdeğer v:özvektör
			[0 1 2] * [1] = [3] = 3* [1]   Bu matris için 3 öz değer
			[1 0 2]	  [0]   [0]	 [0]      1,1,0 ise özvektördür

		-Projeksiyon matrisi w:bir vektörün bir uzaydaki yansımasını temsil eden bir kare matristir. 
		-(ayrıntı https://medium.com/kaveai/matemati%C4%9Fi-ve-python-uygulamas%C4%B1yla-lineer-regresyon-normal-denklem-dd38c43e0941)

		Algoritma Adımları:
		 -İndirgenmek istenen boyut k olsun
		 -Veri standartlaştırılır.
		 -Kovaryans veya korelasyon matrisinden öz değerler ve öz vektörler elde edilir Veya SVD kullanılır. (SVD: singular value decomposition)
		 -Özdeğerler büyükten küçüğe sıralanır k tanesi alınır.
		 -Seçilen k özdeğerden w projeksiyon matrisi oluşturulur.
		 -Orijinal veri kümesi X w kullanılarak dönüştürülür.
		 -K boyutlu Y uzayı elde edilir.
		

	LDA: LINEAR DISCRIMINANT ANALYSIS
		-PCA benzeri bir boyut donusumu yapar. Fakat gözetimli bir şekilde bu işi yapar.
		-Yani PCA gözetimsiz bir indirgeme yaparken LCA gözetimli olarak yapar.
		-LDA sınıf farklarını ve etiketleri göz önüne alarak indirgeme yapar.
		-LDA'de amaç sınıfları birbirinden ayıran en iyi boyutu bulmaktır
		-PCA'de ama ç verileri birbirinden ayıran en faydalı boyutu bulmaktır.
		-Şu makaleyi oku https://sebastianraschka.com/Articles/2014_python_lda.html
		-Algoritma adımları aslında PCA dan çok farklı değildir.
		-En büyük fark ilk adımında olur. Ayrıntılı bilgi için yukarıdaki makaleyi okuyabilirisiniz.
__________________________________________________________________________________________________________________________
		
PROBLEME GÖRE MODEL NASIL SEÇİLMELİ:

	-Modellerin başarısı, parametrelere bağlıdır.
	-Makine öğrenmesi parametreleri optimize etmez. 
	-Bizim kendi tecrübemiz ve isteklerimiz doğrultusunda parametreleri optimize etmemiz gerekir. 
	-Model seçiminden önce dikkat edilmesi gereken ilk nokta model değerlendirilmesidir (evalution)
	-Şimdiye kadar test kümesindeki başarıyı ölçtük. (split validation yaptık)
	-Veri bölündükten sonra makine öğrenmesinin uygunluğuna bakıyorduk artık öyle değil !!
	-Yeni terimler: K-fold cross validation (k-katlamalı çarpraz doğrulama), Grid Search (Izgara Araması)
		Problemin tipine göre model seçimi için kullanılan algoritma farklılık gösterebilir.
	-Bu farklılık konusunda bağımlı değişken var olması da önemli bir ölçüttür. 
	-Eğer bağımlı değişken yoksa gözetimsiz öğrenme olacağı söylenebilir.
	-Bağımlı değişken yoksa sınıflandırma ya da regresyon olacaktır.
	-Bu aşamadan sonra bağımlı değişken kategorik mi sürekli sayı mı da önemli bir ölçüttür.
	-Bir diğer aşama doğrusal olan ya da doğrusal olmayan şeklinde ayrım yapılması da önemlidir.
	-Yani kısaca verilerin iyi bir şekilde incelenmesi ve bunun sonucunda kararlar verilmesi en doğru yoldur.

	**K-Fold Cross Validation (k-katlamalı çarpraz doğrulama):
	     -Cross validation n-fold ifadesinde n = 4 olsun.
	     -İlk olarak veriyi +++- şeklinde - test kümesi + lar ise train kümesi olarak ayırır. Başarı oranını hesaplar.
	     -Sonra ++-+ şeklinde tekrar başarı oranını hesaplar. +-++ olarak tekrar hesaplar. -+++ olarak tekrar hesaplar.
	     -Bu hesaplamalarda bulduğu değerlere göre karar verir. Bu kısımdan sonra bu algoritmanın farklı varyasyonları vardır.
	     -Karar mekanizması değerler ortalamasına bağlı olarak, minimum değeri alarak ya da farklı bir şekilde olabilir.
	     -Buradaki n değerine bağlı olarak veri n kez gezilir.
	     -Bu algoritma çoğunlukla sınıflandırma algoritmaları için kullanılır.
	   
	
	** Grid Search
	     -Çalıştırdığımız algoritmanın alacağı parametrelerin optimize edilmesi de önemlidir.
	     -Bu kısım kod üzerinden bakacağız, ve anlatacağız.
	      
__________________________________________________________________________________________________________________________
	
XGBOOST EXTREME GRADIENT BOOSTING
	-Okunması gereken link -> https://xgboost.readthedocs.io/en/stable/ 
	-Çoğu ortamda çalışabilir.
	-Hızlı çalışır.
	-Yüksek verilerde iyi performans gösterir.
	-Problem ve modelin yorumunun mümkün olması.
__________________________________________________________________________________________________________________________

MODELLER NASIL KAYDEDİLİR
	-Pickle Joblib Pmml isimli 3 farklı kaydetme standardı vardır.
	-Pickle üzerinden bu işlemin nasıl yapıldığını görelim.
	-Makineyi train edildikten sonra model bir dosyaya nasıl kaydedilecek
	-Python ile pickle için kodlamayı yapacağız.

__________________________________________________________________________________________________________________________	

NOT: [+] Görüntü işleme ile ilgili 2001 Jamie Hutchinson IEEE makalesine bir bak

CNN CONVOLUTIONAL NEURAL NETWORK EVRİŞİMSEL SİNİR AĞLARI
	-Yapay sinir ağları resimleri işlerken bu modeli kullanabilir.
	-Özniteliklere göre resmin algılanmasının değişebileceği unutulmamalıdır.
	-CNN donanım birimlerinin gelişmesiyle hızla gelişmiştir
	-Facebook resim etiketlemede kişi sorma onaylama işlemi.
	-Çek imzalarını tanıma.
	-CNN farklılıkları bulmak üzerine kuruludur.
	-CNN'in en önemli özelliği öznitelik çıkartma ve farkları bulma konusunda diğer modellerden avantajlıdır.
	-Kısaca CNN'in makine öğrenmesinin bazı adımlarını kendi içinde barındırıyor.
	-CNN 3 temel işlemden oluşur:
		Convolution and Non-Linear
		Pooling: (resmi küçültmemize yarıyor)
		Flattening (düzleştirme)
		Neural Network (Aktivasyon Fonksiyonu özelleştirmeleri)
		
	*CONVOLUTİON:
	-Aslında bir filtredir.
	-Resimden gelen inputların bir dönüşüm operatörü ile dönüştürüldüğü söylenebilir.
	-Küçük bir resim düşünelim. 
	-Öğrenilecek ağ parametrelerinin de elimizde olduğunu varsayalım.
	-Öğrenilecek ağ parametreleri bir filtre gibi kullanılır.
	-Her filtre küçük bir alanı öğrenir.
	-Bu filtrelerin boyutu algoritmadan algoritmaya değişebilir.
	-6*6 bir resiminiz varsa 3*3 lük filtreleriniz olabilir.
	-Ama CNN'in farklı çeşitlerinde bu filtrelerin boyutları da değişecektir.
	-Filtre ile resim üzerinde kıyaslamalar yapılıyor.
	-Bu karşılaştırmalar sayesinde model öğrenmini gerçekleştiriyor.
	-Bu filtreleme işlemi sonrası convolution matrisi elde edilir.
	-Birden fazla filtre için birden fazla convolution matris elde edilir.
	-Convolutionun bu kısmında borderlarda bulunmuş olur.
	-Resim renkliyse bu filtreler her renk için uygulanır.
	-Convolution ya da diğer işlemler yapılmadana matrisler direkt nural networke bağlanabilir.
	-Ama bu durumda bütün pikseller neural networke dahil olacaktır.
	-Convolution yaparak neural networke girecek olan pikseller azaltılır.
	
	*POOLİNG
	-Convolution ve pooling adımları istediğimiz sayıda tekrarlanabilir.
	-Maks havuzlama ya da ortalama havuzlama gibi çeşitleri vardır.
	-Buradaki havuzlama ksımında olan operatörler de değişebilir.
	-Convolution sonrası pooling yapıldığında resim küçültülmüş olur.
	-Pooling resmi alır ve önemli özniteliklerini öne çıkarır.
	-Önemsizleri de aynı şekilde göz ardı eder.
	-Bu şekilde uç noktalar ve önemli olan değerler kaybedilmeden resimler küçültülür.
	
	FLATTENİNG DÜZLEŞTİRME 
	-Matrislerin 1 boyutlu duruma dönüştürülmesine denir.
	-Gelen input convolution matrisini yapay sinir ağlarına bağlamak için bu işlem yapılır.
	-Düzleştirme işlemi farklı yollarla yapılabilir.
	-Örneğin satır bazlı ya da sütün bazlı olabilir. 

	Yapay sinir ağına bağlanamsı ve bu kısımdan sonrası için derin öğrenme bölümüne bakılabilir.
	Keras dokumantasyonu okunması tavsiye edilir.