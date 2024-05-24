[ * ] Öncelikle söylememe gerek var mı bilmiyorum ama yüklü değilse Pythonun kendi sitesi üzerinden (https://www.python.org/downloads/) Python paketini indirmemiz gerekiyor. İndirme işlemi zahmetli değil
en güncel sürümüne basıp (ki muhtemelen sitenin header kısmında sarı buton olarak duruyor olacaktır) indirmeniz ve indirdiğiniz dosyayı çalıştırıp setup kısmını bitirmeniz bu program ile işimizi bitirecektir. 
(Ayrıca söylememem gereken bi husus ise setup kısmında pip ile alakalı kutucuklara tik atmamız gerekiyor)
 
[ * ]Python'u indirmemiz ile artık kendi Windows tabanlı bilgisayarımızda pip gibi komutları cmd aracılığı ile kullanıyor olabileceğiz. pip komutları ile Python kütüphanelerini indirebileceğiz ve bu sayede Instagram 
hack aracını sorunsuz çalıştırabiliriz. Şimdi kütüphaneleri indirme işlemine geçelim. İlk önce Windows arama kutusuna => "cmd.exe" <= girip cmd komut istemcisini çalıştırıyoruz. Bu konsol Windows işletim sistemlerinin
terminali sayılır. Buraya kodlarımızı girerek kütüphaneleri indireceğiz.

[*]Sırası ile girmemiz gereken kodlar ise: 
- pip install selenium
- pip install pyauto
- pip install tk
- pip install playwright(en önemli)
- pip install chromium (Chrom eklentisi olarak bilinebilir)


Lütfen bir indirme bitemden diğer bi indirmeye geçmeyelim çünkü kütüphaneler tam olarak indirilmediği zaman program tam işlevli çalışamayabilir.
(Not olarak kendim için bıraktığım kod: playwright codegen)  => Sizi ilgilendirmiyor :)

[ * ]Evet tam olarak tüm indirme işlemleri bitti fakat bir eksiğimiz var compiler yada bir IDE ihtiyacımız var yani bu kodların çalışması için gereken altyapı bunun içinde pycharm veya Visual Studio kullanılabilir.
Bu kodlar için Pycharm'ı öneriyorum tab2. 
İndirme Linki : https://www.jetbrains.com/pycharm/download/?section=windows

[ * ]Evet bunu da kurduktan sonra KURULUM İÇİN HER ŞEY BİTTİ.

KULLANIMI 
----------------------------

[ * ] Öncelikle Pycharm üzerinden yeni bir python projesi oluşturuyoruz.

[ * ]Lütfen github.com/furkhangul/Instagram-Hacking-Tool-By-Python adlı linke girip prototiplerden en güncel olanına basın ve kopyalayıp yapıştırın.

[ * ]Programın mantığı gereği verdiğiniz şifreleri çok hızl bir şekilde sürekli denemesi ile şifreyi kırmaya çalışıyor bundan dolayı bizim bir şifre listesine ihtiyacımız var. Bunun için benim daha önce 
kodladığım FurOfTheWeak Word List adlı programı kullanacağım bu programı 
Link: https://github.com/furkhangul/Word-List-Hacking-Tool 
adlı linke girerek FUROFTHEWEAK.CPP adlı dosyayı kendi bilgisayarınızda açtığınız not defterine kaydedip bu uzantıyı .txt den .exe ye çevirerek çalıştırabilirsiniz 
hemen ardından istediğiniz uzunluk ve bilgideki milyonlarca şifreyi txt dosyası halinde elde edebilirsiniz. 

[ * ]Elde etiiğimiz bu txt dosyasının yolunu kaydedip Pycharm üzerinde daha önce kopyaladığımız kodu açıyoruz
with open(r'C:\Users\Furkan\Desktop\password.txt', "r") as file: 
adlı satırı bulup bu uzantıyı kendi uzantınız ile değiştiriyorsunuz.

[ * ]Programı çalışır tuşuna veya f11 tuşuna basıp çalıştırmanızın ardından alt tarafta kırmak istediğimiz instagram kullanıcı adını girmemiz yetiyor. Program kendisi hallediyor.


( DİP NOT ) : Program hızından memnun değilseniz 22. satırlarda time.sleep(3) adlı koddaki 3 saniyeyi kısaltabilirsiniz fakat bu programı hızlandırırken programı çalışamaz hale getirebilir. 
Bu daha çok internet hızınıza bağlı 50mgps altı kullanılmasını tavsiye etmiyorum 
